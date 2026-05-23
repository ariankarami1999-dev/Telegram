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
<img src="https://cdn4.telesco.pe/file/CmKw1pFb7QyoxyUqPP-u-Nv6jUIk4L6QGECl6j22YJqQzO1loyqgk9zsVwFsbEEUjP7joBvz421hSd0Ruzxg1erSUcvWEtCOybXngvtKAcdtOloS_LvUMFIrKzSXM9XZ92RCtEaYHyfujDbvbZ4VibhoBlciyv_7K89WsRYT6Iif8cRb6PTs-HQVyF1TqslQPxTtJ5MGXVcC4RvvePg1V_Q2MySfmqFHv9iAiEgLm7K17wlywAJiwRENX9WsNjwa2cvaFl8sAM_BeTbw_Ik-lGLyRVja4g4uqtu_M2M4C7oQHcVPs-6GGk3gWvV0KtYAoK_9VlS3_ILzk2bwZ-iRpA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 128K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-03 02:56:48</div>
<hr>

<div class="tg-post" id="msg-90183">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90183" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 1.3K · <a href="https://t.me/Futball180TV/90183" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90182">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kLykryookI5in01stvTwUl4rwztA0ILCnrBfNLOITxXeLc7QTxqAFcxtcCgk2G7uPCOD8E82T_LQvek4CbBKkCD7QAWk86Ax3_KXf5VW-k91BowMKl7M29MsJgbLsen6hgJdCjP8UebrL1utWHoLw5dTNVbmAa4oSEv4coRoJC4aI62EFx9h0Fs5_JuzWWKZos2dMTRAnVynErXDiG0DonNh251GdvKottBEcKdJ1_l-Y5dZZUjeXtRXogn5sm31AcwvIiplwbK2X51agN43QSysx6YS1cNNliMye4ZstmkOA6TJ51Y0ODquHIdszgvBivTdMANcckkEK3exSyPGKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/Futball180TV/90182" target="_blank">📅 00:20 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90181">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m-g7QIEr0uzsfAgR-btOuqQQ3XPOnQ8kxaE1iesIcp1U3dRbRr7_-KCW779uoio1UqG1UOLZw8Dx6unec4TcQUvgU_l6mZfZUzva1iYYBNpWJdGfCDFWe1wqFDJ26oirbyDWUgb2rbGLCaFlg_3KBTNHdXb9Qjdlppmie8Fi6y2etlS7A-YWWPZ-KRPMr33qlYiPE2saEkd4ctGpUC0UlvPocJZDH_JmtdrvZTDLyVfZY7ZoQzdKn-nvLMTmcEt22ienrD88mZEQ_MjqXce3EDAgLYrx5n_di5XEKPOCmOjPV7LmggDGvaKxUNzohm6-zjRFeFWgRq2KyNmRt2cdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
ترامپ: یادداشت تفاهم با ایران تا حد زیادی مورد مذاکره قرار گرفته و در حال نهایی شدن است و به زودی اعلام خواهد شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/Futball180TV/90181" target="_blank">📅 00:04 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90180">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T60liMzl6ckWSrUzVpQpbkwl32yxXIBVRDS6SqNmtbyD_B6nCfv4_DkSAeRkMcscaq3O6GKqLyvH6eti70sIoGIGxjsQ3HbAVhPOuEXB2SKbsEOhNnKo4Edr-Sc7vCRYC9JKXm5vt7Wc1o3Artbt_sOaRK2HlUBphEVEu3mJcOq9thUN1JXF-TGyTPA0coszxDbl783QpKhrYD2iJXMM-O_wuocDlTZr_d2p2dEFDn7LgZWg0VJJuWQjh3nnbaaku-LOKS_PV926p5b9sRRCiKI_yVvfpA2yJRBdnn3DIBh-VCJa-m7XivsR0kwZjDpE173lkkc7sh6zHsuFt_lj2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تیم‌فوتبال زنان بارسلونا با برتری قاطع مقابل لیون قهرمان لیگ‌قهرمانان اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/90180" target="_blank">📅 23:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90179">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdiQ4NhUs3ppt6oZxjAszHzZP4-GA75d18DfpQd0OdTSPWNjkzNlnc3wDCl3D3YeE9cD19e4Hl4qtLmKP4LuVf_mcAh2kqrMLRdqUeiSy_ilUg41YC5NDQjWUuCepFs5Wu4SFXeh6_fI3uTqvbt46AIRiBd9tTiqjafs5UfLe4wlcSSKx6rI5mS_q3ID_UC9NEfpli2aHFntkqGcq7l88ZVGDeAjfFkB-xKyEWkE9DMLNUDi8a0zLPzidbOQJiRnTabGUpJmRnSrDVxhx3feUI3Oy0kbNjwAj-pN0xOiO0ak0CABPaQ2aYOJ6wIL2wURLHtX7hZtSOUo2A0njHH6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون درگذشت پرویز قلیچ‌خانی را تسلیت گفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/Futball180TV/90179" target="_blank">📅 22:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90178">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoVtIm9Euss1T9UWfh-mMieiwRi9xyNDACLv_OJ5l98Ytd1c3IcdvlEW0whZb4wyb1qaylLe3dSgsz2XEVXEUKtRF5yMIInNhoKEmvd8sxOq98oOXA0uI4mtD7CoY5Qzlebbqsk1YCtEYCUM98BI6o5ov5KQBnsRMEWuppxpR6_TUxRRwC9kOQ9Phnotk5uVjRCZIS-q7Gk1IxVbYc840yeRf946OrTDl8IO3yj8BiGWMzrj4jVtFAUOXNwjcaZ8SvZjwgW1p4UcuGkgSISj2mtVl6LdoaNBBcWtFwbZps2jmb9SY_0PNhqc_8OO5pQ4OTx_v9PqSvDh02bqcPSzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
تورینو - یوونتوس
🏆
سری آ ایتالیا
⏰
یک‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه المپیک تورین
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
تورینو در ۱۰ دیدار اخیر خود در سری آ، چهار برد و دو تساوی کسب کرده و در چهار بازی شکست خورده است.
✅
یوونتوس در ۱۰ دیدار اخیر خود در سری آ، شش برد و سه تساوی کسب کرده و فقط در یک بازی شکست خورده است.
📈
میانگین گل در ۱۰ دیدار اخیر تورینو در سری آ ۲.۹ گل در هر بازی بوده است.
📈
میانگین گل در ۱۰ دیدار اخیر یوونتوس در سری آ ۱.۷ گل در هر بازی بوده است.
🧠
خروج را از قبل تعریف کنید، نه وسط هیجان.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/Futball180TV/90178" target="_blank">📅 22:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90177">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=mz6t-mPFJrnCJy-k4Utr0yJ14SiA3k669b20-6qVzEY04fDfBvn7zK-jWDM6QoyyfwJf7D5Vcu_ve1n5BacTq3I2btj2sbNSG_pr_CK6wIDictrhLBlhwje917WblqSSSC7Dme7sehpIgQWCQDHQ0XAltk3jmXdw-RcqNBy4j2WEyzSbas5qtWNycgI4fQm2DQRGtm5Va1dPhfR-IghNO6vjv3BBzB2Pb7T8oOj3dRxcs4iDk38lOjnWavxbxmjYSZhkdbQHoVMUJkHfdLXIRf87YVw9Ota5dB2xm9c8AiR_FlszsU2fB7msLm1JYMeHJEKneg0df9cYHPtad4MjEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1b20643b.mp4?token=mz6t-mPFJrnCJy-k4Utr0yJ14SiA3k669b20-6qVzEY04fDfBvn7zK-jWDM6QoyyfwJf7D5Vcu_ve1n5BacTq3I2btj2sbNSG_pr_CK6wIDictrhLBlhwje917WblqSSSC7Dme7sehpIgQWCQDHQ0XAltk3jmXdw-RcqNBy4j2WEyzSbas5qtWNycgI4fQm2DQRGtm5Va1dPhfR-IghNO6vjv3BBzB2Pb7T8oOj3dRxcs4iDk38lOjnWavxbxmjYSZhkdbQHoVMUJkHfdLXIRf87YVw9Ota5dB2xm9c8AiR_FlszsU2fB7msLm1JYMeHJEKneg0df9cYHPtad4MjEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
افشاگری همسر ناصر حجازی؛ علی دایی تمام هزینه‌های درمان را پرداخت کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/Futball180TV/90177" target="_blank">📅 20:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90176">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLy2XF3s5E5Yp7cms2I5eC86C8IWhDyvsDAIaPRZXNWyzmW0Y1fB5QozWJWNoqJhVcYHadyvAnb9JXYNI7ToDp3kiwamy4uNvL9n_Ns6lvfuQFsjWphXQJhOY1Fk_7d0kr3FnyFWmV727qIB_Qp1__hFAWjlfUb4VfusXjAKtQJu2WVA0Tzf8CyEGzshdDflh7Mxkckdjqfy4hyoymYY-v2SuPLH4_-hVOKHE0GyoFmrinFHFosAf2P-Ok7skiPWEU663idiI119-lLJA8asa1xUgGVZUHpUQq45wR4pTHfrCPzJVd5A0wjezjsad215nl-CaNo_5mlktkFyn218TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مائوریتسیو ساری با جدایی از تیم فوتبال لاتزیو سرمربی آتالانتا در فصل‌آینده شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/Futball180TV/90176" target="_blank">📅 20:39 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90175">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=eRcdGQVWWVteKbyHGQE-7kvs5EaCffhYqn_yrmkzmO5meFpeSST7K1JUDSZKreWdQr7SSsMxjC8Z_MkZ4Z-rQo8knR3yJDuTuz3YxHtR9uW9ZE1jeZUXeQ7lPPoHXnIpAwIXXRVsuXpA_jWR9gduha5ULMHpkXm4HBFJuIwQpkbDUyTEfIv5mRrboapnEjAtIjtXrqbca1pARXA6J_y2r02L0hZzUXheMKBE3jxjy48m2Y8E-gNTIB9EyKpobRgCxrKk_8Uqir90SPj2H9pvECtKtWUxV2Tu9slP6Sezf6DRsbu2ghXb-q8cIgnxa1k-ggYEx0_ntQ3uqQKWxb2aow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa5fa3b89.mp4?token=eRcdGQVWWVteKbyHGQE-7kvs5EaCffhYqn_yrmkzmO5meFpeSST7K1JUDSZKreWdQr7SSsMxjC8Z_MkZ4Z-rQo8knR3yJDuTuz3YxHtR9uW9ZE1jeZUXeQ7lPPoHXnIpAwIXXRVsuXpA_jWR9gduha5ULMHpkXm4HBFJuIwQpkbDUyTEfIv5mRrboapnEjAtIjtXrqbca1pARXA6J_y2r02L0hZzUXheMKBE3jxjy48m2Y8E-gNTIB9EyKpobRgCxrKk_8Uqir90SPj2H9pvECtKtWUxV2Tu9slP6Sezf6DRsbu2ghXb-q8cIgnxa1k-ggYEx0_ntQ3uqQKWxb2aow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهناز شفیعی، همسر اسطوره فوتبال ایران ناصر حجازی، گفت حقوق بازنشستگی او ۲ میلیون تومان است.
او در ادامه با انتقاد از وضعیت مالی در فوتبال ایران گفت چرا باید کارلوس کی‌روش با پول این مردم به سطحی از درآمد برسد که بتواند برای خود در پرتغال جزیره‌ای بخرد، در حالی که ناصر حجازی در آن زمان حقوقی بسیار پایین دریافت می‌کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/90175" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90174">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90174" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/Futball180TV/90174" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90173">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPBRupA4Yb6YpYJeQusAEVUqGc3bDbFf56RklDROAYgVNfSd-fCRrhxeL_4tWUO3YxdIvS0h7KUnLpqYkrrqOOa8g9q5OP6JDLoKegDt2sdC9qDrtZKgEUZJ-pVugZBodg6_dijeh11D-pOrW6jsBizOcHKyp0YjDa3sckcjtLepBlsvb4YejprCoep2vQCTgZpuhFGJy0kqq2iSbIahA4hIWY8FM2lNJMcoOJzxdOlF-f74XDv-jZOGMZA_6lUksQQD4ir-RcPpabr-42PmtYEIhE8bLUuLvc55RrYjKLfaswfNnoEHq7-3gIWp4sJtKNylTiqeR7qSEC-mcoYcjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/Futball180TV/90173" target="_blank">📅 19:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90172">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=CHZPIIuKS_AWUk3D1mlOnkc46GN-c5wIYleUvhbnj8_iJY9PCNMNOyV6ZD8UFZCAL4OfOZJzBBKjYKxlOOezc8UPsLH5fbHhYvTsfQ20GwcDOJC3buiQi96OcJRH6F49lio_nOef_5BRjQmJJEhqya_tBIPlnP20AGEGVMT0BX08aendWJs8VsF08L8OabgKww6W_5vV33JNUFUzWVbeZQf26C4UqalVGDI4TiOlgvqGTlM80DCVAF0YGxIhs4zOnD4GZIDNvMuMzy0V-6Nb4kvMyTElyw_ht_WdgLvjCD7y03wlVaj4HOd2Mezv0koFItm9w7P_t_hqpkkUPY_iKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba990f9ec.mp4?token=CHZPIIuKS_AWUk3D1mlOnkc46GN-c5wIYleUvhbnj8_iJY9PCNMNOyV6ZD8UFZCAL4OfOZJzBBKjYKxlOOezc8UPsLH5fbHhYvTsfQ20GwcDOJC3buiQi96OcJRH6F49lio_nOef_5BRjQmJJEhqya_tBIPlnP20AGEGVMT0BX08aendWJs8VsF08L8OabgKww6W_5vV33JNUFUzWVbeZQf26C4UqalVGDI4TiOlgvqGTlM80DCVAF0YGxIhs4zOnD4GZIDNvMuMzy0V-6Nb4kvMyTElyw_ht_WdgLvjCD7y03wlVaj4HOd2Mezv0koFItm9w7P_t_hqpkkUPY_iKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
دوم خرداد، سالگرد زنده‌یاد ناصر حجازی، اسطوره باشگاه استقلال و فوتبال ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/Futball180TV/90172" target="_blank">📅 18:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90171">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwfwV65Le76oiISqjVXhgRKjtaN1LBacKgmR0crXPPJDqwSLUOVB2X8ozE1VGPjVIKv6eNp6hbK6qEc5n9vhsGspuS2nNG81W96AlBfX7wQ9s-a8xJKpWM7onpiDus_MdQaeEh4xCxEVpREEqQYWa_ZAjRLUgSO6I8Jc_wGvmsh_CUU-407j3RBO8Np8ZMdahlVW4-Q88siJOaPrV0idBzrnsPeF9TImqxs9nKHenrKsmWh_QkEnuOdnR13ZxfJxJ_nQpZoweDwT1yOcXbtUIGzgnOSglKaii_SUg2DeEa0kMis9_RI9YR-Z4T8C61T0qAYtDnVEkU6md1LKKBIUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖤
تلخ و ناگوار؛ درگذشت چهره افسانه‌ای فوتبال ایران
پرویز قلیچ‌خانی، چهره تاریخی فوتبال ایران و یکی از بزرگ‌ترین تاریخ این رشته ورزشی ساعاتی قبل در حومه پاریس جان به جان آفرین تسلیم کرد. قلیچ‌خانی متولد ۱۳۲۴ و در 81 سالگی پس از ماه‌ها تحمل بیماری از دنیا رفت. او تنها بازیکن تاریخ فوتبال ایران است که سه بار به صورت متوالی قهرمان جام ملت‌های آسیا شده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/Futball180TV/90171" target="_blank">📅 18:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90170">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b0-Vbngjp7Qq_sxB8FX9LwstEH0iyINjjyOPH6t9NfYms2F2CTReh6277KEylqFDyKYoYsEieFE8WZXk-PHkLr1jsGH8ifds78QXOuQcAeN3saIMhfiq79F1XLz4kA9dCBXF8O5qLQseO9AtBOHX4waYMc4qUQcZbsissN0xTtR30XDKfdc8Bi-sI_U-GpYf4R8BxJxBlAORxSBG2Rc9ajlRizjOP1QpZBcrAIpd8NsIL-mZwGGJeFiGABrwDrc4hMOjGtzxb3NFQo_Hx7pMXgRQAve14_35Rqm9W8OKKRiaVW_b4JC_rQMoGxlXwVwMLNjnlhfQ_GhI_OaEERY4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
عکس جدیدی که ترامپ منتشر کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/90170" target="_blank">📅 17:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90169">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=HTlLcX0SrdhZEFNB7XJqMmKmP6yAPJQlrQwEVxqp-1lz2zkcaLBm1T1cKdouWfr-3EJfS2WTeM8XRDLnSa4hTt6m0n_kt28ESRJ7FvTtWYh21-IOHh-HHJC_jddlnI3qlF94OdbC67HMJpL-B0WCJJNNYu8SaLcMHSwy8tIani8OYFOYVA2Awdja5eu12_pXY4yn16W11q4wglomOPGB4TqXNzUNSnMfaE_IBxgyg6LIPZOo1Yuizau8udTH1BVOoEA3mS6Eexa-NN3EkzG-qePUfPRzrjLdDkT_2LM0Ousn5zaW1xHPAqzY9wcAVmA2S-5G8RohTF_sa_wNU5eviA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/420b451a8a.mp4?token=HTlLcX0SrdhZEFNB7XJqMmKmP6yAPJQlrQwEVxqp-1lz2zkcaLBm1T1cKdouWfr-3EJfS2WTeM8XRDLnSa4hTt6m0n_kt28ESRJ7FvTtWYh21-IOHh-HHJC_jddlnI3qlF94OdbC67HMJpL-B0WCJJNNYu8SaLcMHSwy8tIani8OYFOYVA2Awdja5eu12_pXY4yn16W11q4wglomOPGB4TqXNzUNSnMfaE_IBxgyg6LIPZOo1Yuizau8udTH1BVOoEA3mS6Eexa-NN3EkzG-qePUfPRzrjLdDkT_2LM0Ousn5zaW1xHPAqzY9wcAVmA2S-5G8RohTF_sa_wNU5eviA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پادرمیانی همسر ناصر حجازی برای برگشت فرهاد مجیدی به تمرینات تیم استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90169" target="_blank">📅 14:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90168">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q-IricJo7hJ8nBJ1dk3EPQMATGZERJC_-tn_7ses0l_Nos_LOSZe6veyJZ2vIW5yNUikyyYTHGY6rA1JcLxHFphfwveLj6rW--MwW9hFjCuj1oop6_bMd2wtT3RAPvkL5kRLJ6lgisvgKDZalfjmBu7VGI_wrs7l5tJU8j_GnXfO2Wcsw0Ip_8WmQsDOLMnARU2Wn1w4suiiHBGZsdCgQCa3lPqP8b3qnfqEVSOROAvQUoKD5oKVeOqDHd13bUkLG6fqhdfkLryHhcqiPivdBmGebI9gQap0dGCM9j0qHZ_rBgLFXDwqDdhmbU7u6Qr9Lv5S7KAamvhqlUWhayxUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو فرناندز به عنوان بهترین بازیکن فصل ۲۰۲۵/۲۶ پرمیرلیگ انتخاب شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/Futball180TV/90168" target="_blank">📅 14:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90167">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbobwbn8W2uw6meLmNPsdPWbWScV288zGxFYQj92_y6OEjoGL73eP1mpei2MsYqAFqXv0ZMFQjqlMwONzKuu-W7EBnTvNPRa_nt7-LlqRuLjUNgEXRQnKqLbq1jtZV6w6D4LNv2S1PNuFAhXvmCbvVB0BU92oaboilI7WdKL6sohlJqzoH25ww0hsytkhOlojtPn9DlFH8j5t1weJ8UKaz2sknH2DMkRom7P3I6mSpuMTPvTjOa_WtJDk6M7AA8AoWkVRx4_Jl0w00c3WzBOW8r1f4TC-YZ6Kv0iSzfWAublCX8KcOa0Hqu85ylpyPdH_kHLdOGtTLKuz_bRsSaRfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گستون ایدول (روزنامه‌نگار آرژانتینی):
🔻
فکر می‌کنم ۲۰٪ احتمال داره بره آرسنال، ۳۵٪ پاری‌سن‌ژرمن، و ۴۵٪ بارسلونا.
🔻
اگه بارسلونا واقعاً می‌خوادش، باید این رو با یه پیشنهاد قوی ثابت کنه. تنها تیمی که واقعاً قدم برداشته پاری‌سن‌ژرمنه. بهش قول یه حقوق خوب دادن و پول کافی برای مذاکره با اتلتیکو مادرید رو هم دارن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90167" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90166">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/Futball180TV/90166" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90165">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eY_dUeD78BetQ166zGxb0qRTdxOIp3yIHmtT-cnfzZ2DEAX_RZ9g0TGigOrVd_vhCd-hbLFZJosRD60gBZW1BAxaDZLdqDV4QZopurzZAPpWDk57Awjn9cPR0t_RDD32OeMXpArUOYGHiuBI0MhuO78NbWiVSiXD9CBl5hjvuxD-SiPlGjB7xM3aY_Dy714nH1kL2xNOtWnCBpjTfRw9z5UfpdPFw4MBHqcAYOc7CCqXPDxuuiGGXeQGT2kNq2RR6-_oomPsQ9CukmtffhyHXdbl74zhnvz3hgM56RfGdGWFvz_fDYjF0D1gIdhu1ZbELYWyRYV6Wvp1fU0r6ia2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/90165" target="_blank">📅 12:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90164">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=p9TDvSlij3TTQzyI_gceMoROO6jrMUU4hakZ4tAgTSr8jLYJ_9Pz2JvZ1ieSN-CP4dLZGLsYZYt6QgSkpLVyA-96_qpoUKJvQR6HcqCoqP2Lg8xHNhoYFwlRyhHufjl_78aS3C53y3ipBIb9GES3uKUQHc_BVezXCbnKdXXjA7BYuN5lIp8bVlcue2eRp472gyaK6iWcGqOIXttG9NNjfNiEXAaZZvW0HdncojWPHYDzOyUAwG45VRheyv9iSDtNRUvrNURBVeESdA6LMmcRD2ofQgOtAxcksZrkIrWEOsTLMUtjnHHB_QSQAn_0NFR8w-eS8TzH5OLUpONTLwnZ7FOcHWHbF9BScf9fZ-h25Gidby6mccHgaxEPYGzbxR0NUoySK0Oso7Zyd3kCG2tay6ttpBV_2XSelgwT59vUyLKhqQZ0xDwxx3Esfw7p62vkYy6HD5Ot_dKMx_YRvXlKu7dEHR2vGV9td9tKOQsTdzNy0wArwQXIe4et_0Sm89K_6SfwYcIx0uz8vX4-8jCNZ55Kankfp6EubN8U7B8TPpfyFmP_F1s50ovLQ5mHLBbXAFATXD95MHsTx13u9CSOa7K_u76G7GvCesNpCQR3kJClw8aUIMxvsxLGpixrDAtn4h0JxAmyOY0Q_VmsJ73Y66mugP0fb3g1l7b06GsuZ5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb02d75b.mp4?token=p9TDvSlij3TTQzyI_gceMoROO6jrMUU4hakZ4tAgTSr8jLYJ_9Pz2JvZ1ieSN-CP4dLZGLsYZYt6QgSkpLVyA-96_qpoUKJvQR6HcqCoqP2Lg8xHNhoYFwlRyhHufjl_78aS3C53y3ipBIb9GES3uKUQHc_BVezXCbnKdXXjA7BYuN5lIp8bVlcue2eRp472gyaK6iWcGqOIXttG9NNjfNiEXAaZZvW0HdncojWPHYDzOyUAwG45VRheyv9iSDtNRUvrNURBVeESdA6LMmcRD2ofQgOtAxcksZrkIrWEOsTLMUtjnHHB_QSQAn_0NFR8w-eS8TzH5OLUpONTLwnZ7FOcHWHbF9BScf9fZ-h25Gidby6mccHgaxEPYGzbxR0NUoySK0Oso7Zyd3kCG2tay6ttpBV_2XSelgwT59vUyLKhqQZ0xDwxx3Esfw7p62vkYy6HD5Ot_dKMx_YRvXlKu7dEHR2vGV9td9tKOQsTdzNy0wArwQXIe4et_0Sm89K_6SfwYcIx0uz8vX4-8jCNZ55Kankfp6EubN8U7B8TPpfyFmP_F1s50ovLQ5mHLBbXAFATXD95MHsTx13u9CSOa7K_u76G7GvCesNpCQR3kJClw8aUIMxvsxLGpixrDAtn4h0JxAmyOY0Q_VmsJ73Y66mugP0fb3g1l7b06GsuZ5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
یکی از جذابیت‌های فصل آینده لالیگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/Futball180TV/90164" target="_blank">📅 11:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90163">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
⭕️
شنیده می‌شود کشور آمریکا ویزای مهدی طارمی، احسان حاج‌صفی و شجاع خلیل‌زاده را بدلیل گذراندن خدمت سربازی خود در سپاه صادر نخواهد کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90163" target="_blank">📅 11:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90162">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiR46SmWCMS8TbtX2fIDYixHWWzHes50UM9VdQv3UOlU_eswWWjADFxZGD9kRU3xGmjf7ESj6Yc8DfANIZfR5RHwQMJH81agP3GfAY5-3tPUH9s3h8n_9-Q3dHma-wik_dmF3sV4_K5TiDhYUGaBvulR656VsPBVjpa8moBG6l3obKS6CL3uJ524A_lOzHhRL5rzkoJpqFjiUzHM0_w_0LZ3MPYDx1EkObDea33mZ1M8E3HMwRpiLX50ZL8Krb1I-buB-71mDKAC4JhpwHc1xbOKgkkmweilP1nBSGITf42KzhjaBVvq7Uy69bUtfLquISQgmfZtx8wuoXchJaD04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توخل: این فقط یک مسئله ساختاری برای ایجاد تیمی متوازن است تا پنج بازیکن در پست شماره 10 نداشته باشیم. حتی اگر این تصمیم دردناک باشد، معتقدم که برای تیم ملی انگلیس تصمیم درستی بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/90162" target="_blank">📅 09:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90161">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90161" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90160">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lmxd9squKELroL1kbDGnAcfqFDPXE004T51JoktTEki8Lu0WLbVa6WJSjZiECeJyRutZHhUfPYSdeT0l86qUreW8ekMR_A0vWs9jTjqYhv8iY3PkhXkNj8bZhJ1XRGMjJg5hOkFgaXkqfUQ3jvGhHpMLGmwpo2FJiAAgjczq5eXajlowT5uNQsBtCV89xfSpAJMoDtaboCTw77jQv5DtTagJsdWMvscq2m6Cln3qWQDDtaQJtFe51YtIOQl6QqIdPqnz2i0JXK8UkLdIuEGUJJVIng7BB7PGsftMq4_jbUs8rKvjCtGlN7IxS7ROvglFwa6aqbRDcB0ocV1X0hmy4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90160" target="_blank">📅 00:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90159">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=II1T9l_JqDedujPoyu6typ4SsI57O3XL4C3DUzyYJpGpYvvy4JFPMO8-exaYqc1MpH2nZYHidFg30Q17UsijWMypyKntVHeCxp7-XKpte-kAYqowlUVQ1IHadQ7cwhM-KIiRUfAMGQhfTdbqtP0h3_0PXwjCe6WdyKcF0Kk4vI3PGrzIHuswxJXkmOApgMIjab4r31qVD9J-yduQ-OUhzH2YmSKqyaxozorADV_0HEuDF23YHNsKgO9e22pTA9VqwcnQRVW-EkLFrOJM3uOsswIGrNpi4-yzCQO048u58cAmMJkCtBMktlmn1FAZ3Or5SagXcY2z3queYOVtxWs1rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12eda9dfdf.mp4?token=II1T9l_JqDedujPoyu6typ4SsI57O3XL4C3DUzyYJpGpYvvy4JFPMO8-exaYqc1MpH2nZYHidFg30Q17UsijWMypyKntVHeCxp7-XKpte-kAYqowlUVQ1IHadQ7cwhM-KIiRUfAMGQhfTdbqtP0h3_0PXwjCe6WdyKcF0Kk4vI3PGrzIHuswxJXkmOApgMIjab4r31qVD9J-yduQ-OUhzH2YmSKqyaxozorADV_0HEuDF23YHNsKgO9e22pTA9VqwcnQRVW-EkLFrOJM3uOsswIGrNpi4-yzCQO048u58cAmMJkCtBMktlmn1FAZ3Or5SagXcY2z3queYOVtxWs1rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت ترامپ در سخرانی امشبش:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90159" target="_blank">📅 00:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90158">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1bstidk2h2-bVHmTVl75ScPc2OTjU15rsr1sakorqrcQqJJdoYRfWkhgmDcOyymJ0sV_69r0SbsEAy0KlXYIFOPGTFRUqKFKJYJBges3R40iJlG7-iBEqhjzHs_WFY7ZgQx0UlgVvIg-yj2BuAMkczxGS-hmbrxVKWQkKEV4v_x8Es_B8tsVb0YEdZCV2KdpI4pjgKGK6Y2vSndvqJE7t0VJeeRLKRM-mNbLlN7RBApMsCakj47N8cy2HVv-UaFN8LNLXxQ9Goz5gPp6a7v-v6Inv1AiRaCeqjjvB3hK5xtpyGF64CTWZ_oi52xL0Es4vS8F-aSD9_TmBUXzKCtmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی کریمی خطاب به شاهین نجفی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90158" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90157">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCAwuyoO_wG1CH4EshIb1DtoeB3cjoPEvwdczV0i5DqKUcRwDMhhU1quSlJK3yPxyeVPU-DpyvUr36IILY5BmGWgI7A-CpH0MXXjlduodrtEO4BBqbOu6bjVWqVNS6vPzTSsgDPPJB-ps8Eb4-gsGevw6OTTzYHMzsPRSInjRm4EcrKwDNNBvsDm19es_FoL7ht-kOsniNPhMIyqYsb504aB9QajexEqIphs79BjTqOLMt2vnKFW4N4J0i_WkuanwyeZ1OkA5OvxHySxjbK4ENsrBGxO_BG4AXXIU8vFBU87Bd_fHzv5BcO9WqhZxec-eczyX8UEg2s2a_g7GKGrRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید - اتلتیک بیلبائو
🏆
لالیگا اسپانیا
🇪🇸
⏰
شنبه ساعت ۲۲:۳۰
🏟
ورزشگاه برنابئو
🎲
با بیش از ۵۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال در
۱۰
دیدار اخیر خود در لالیگا،
۶
برد و
۲
تساوی ثبت کرده و در
۲
مسابقه شکست خورده است.
✅
اتلتیک بیلبائو در
۱۰
دیدار اخیر خود در لالیگا،
۲
برد و
۱
تساوی ثبت کرده و در
۶
مسابقه شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر رئال مادرید در لالیگا
۲
.۷ گل در هر بازی بوده است.
🧠
وقتی نتیجه از تصمیم مهم‌تر شد، تفریح تمام شده است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/Futball180TV/90157" target="_blank">📅 23:31 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90154">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AY7DWmBqjb8aYZavY8Li1nwStKjTOW91H6B0jp6MCcoqS7BSzLaac5GBa4GvOUoWIxeEqI__qcR5ER58dgWNLkGBkcPbA_ufSL6pYQ4zn85Kv3hdt0C97ArV0DM_dwuQQWENCKo6h2FL5GucbvSOe62lZAI1uizrQcUa7dRQVbmeiFgWVCKbWzp9fUbX6RdxXbBh0IpClNSAejNqW61LhNyVJ7J55dAUgyvrv33lfQIkHU5xtGLSdGwHUrwGOOqsaCJ_GaT0SpbgIBSfEe6vKHuUJtc6cfiwGfW-5DQvnCXCs6xi8xXWiBYYeKTLoY6RQvjiki7ZhRLeTYzTN03Ljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RClsDU2mYwT0FssfNjRuhdaXuVQ4e9e_W_2kjMiu67VNyYgbZeo8c2IJP4s7h-MTXb7jK6c2213jXHX0atBahqkmCq11eTOdNE2beMhn2VXVedMmg9eMgY-NKdCHsE7YeERbRTBBDVL5IHmsBzu0gGyLEcgNYPa1HT4DIBrQmTmVr0jdkB7Rv2LSq1Kz5hmtlBB7_l3k3g0JCxciBawHF5NledVAjgbHJpuywBZik0ZuztxXcrySfsFhbbmECd4wcnHZwg261B4-5dwHO4Znokq6DwIZHMpVYaEqX_FHL3UdQFZW8VcYEix7lGIzODTczlsirbK3Z_AiCCS84vs_hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/khj_wY5C0IJkUWRCwtRLWRvi9RuUExw13ZIZfiJTTwB1Qxq2NH-g8VTeJES_LokQA_AutzB2-KiFtmYxGVsMNY1wk2R4E1jHnLPJjUoEgE8GVURV_3oY7wrQRzu-JUlapzbKSmLYSNSKEnpc2W0sBG33HkKPTj6oNLqZYHx3ofwRa9vHltAUZBAyzs5d_gFPTTtU-mhk0RJ-HjdOkfTHWj5Jm2SjB5-6m0I1SZZmOdLH3qP-N-2z-IGL5AeYHGKC6hrN0DiAUMksQN_o2pomBT-D-limrP6K-k8s8r_cjIhGPIto6DN_26Ob4LF6po2NLNPZdZcLcUaIfh0QRN2w_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عناوین برتر سری آ تو فصل 2025/26
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90154" target="_blank">📅 20:43 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90153">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/90153" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90152">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL0Utz3IJOutPnAep7UxUIImEDngHpiTSVxO9tzlvQmuYQQDd5_FQLmg7Qp7BGSfXRMNGwShAPfY-4_yK9P9lHDNo93vDWwp6pbQzQ0kOstjuoJsYEMCvqe-Qi6WxkLvNzKws9IOhu3n-mQwbSHqOTX7zjIFQPvWw8fM-AXxk1mWVn6yEyVT4_BwWV3tLnZjZxTzWLF27P9TkqGbeAQgMzPtj0GugGfHAij40P0qLlNzdbBqOKvE6nlNSkYuVk9-NRjtiAFmTqjFQRimwDBJqWH2Ho0LbXpfjZuvy2vnML6X_ycV_BQ-QP5hH1DiydFC3dw4i81iXxjQ1c3zhWkcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/Futball180TV/90152" target="_blank">📅 20:42 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90151">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">❌
العربی الجدید به نقل از منبعی در وزارت خارجه پاکستان: واشنگتن و تهران انعطاف کافی در پرونده‌های اصلی از خود نشان نمی‌دهند/ سفر فرمانده ارتش (پاکستان) به تهران ممکن است آخرین تلاش برای جلوگیری از بازگشت منطقه به جنگ باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/Futball180TV/90151" target="_blank">📅 19:52 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90150">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZiE68zxzGS6oWjwMmMp3VaXoYyFzHDtB4-AJNfykq5QJan4qkDGARzmwRbCciQc90pVMtO_4d8ZQYugvZZAImoTy0TPBBXD_PJ6kqTv2HsZRq26enksNrStMwrK5u_0sYIQthEI_WdK-VVGSMks0TPFJZ4NDBHsEsPAKfubyAZuJJJwW4Q_NDTMaAMCliMkVf2R53TQ4XHvAKFLheFbot-LCJf_dV6aApN-UJ9Tcfqt_pNMiqTpRVit-Fj5ugVJExpTWPpgHvqFsv6ui8cjkHd37PY6b9IhqI3jeGjyPixgrVpQLMe4UsrtGlBdYGkHrdolpIsgYYbtKxUxgX22_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۴ کیت اصلی بارسلونا برای فصل آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/Futball180TV/90150" target="_blank">📅 19:33 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90149">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmoAdmin</strong></div>
<div class="tg-text">⚠️
مدت این آفر 3 روز هست
⚠️
💎
پلن حرفه ای
1 گیگ : 280,000 ت
5 گیگ : 1,150,000ت
10 گیگ : 2,050,000ت
20 گیگ : 3,900,000ت
40 گیگ : 6,900,000ت
💎
پلن اقتصادی
5 گیگ : 850,000ت
10 گیگ : 1,600,000ت
20 گیگ : 2,800,000ت
40 گیگ : 5,100,000ت
🟢
کد تخفیف به صورت خودکار روی ربات فعال هست و نیاز به وارد کردن چیزی نیست
✈️
آیدی ربات جهت خرید :
@AmoAdmins_bot</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/Futball180TV/90149" target="_blank">📅 18:22 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90148">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🔵
باشگاه استقلال مذاکرات مثبتی با آلومینیوم اراک برای جذب محمد خلیفه سنگربان جوان این تیم انجام داده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90148" target="_blank">📅 17:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90147">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8BThKseW30AslqsZ8ynyyEcjmR4Uo03ZoR1cHAAqSSD8th27ske_uGpp3UcMOREk7vsWSLpf8oG6Mmeqiz_6HRQT-Cu5Gjax7e7uoc91XTCx0IqBv_j5Pp7ijPX5RRgr3KE1ir4CclzxVyqMxji_ZSxo6pGxppZrOd8oUslhU0G-pQfmwQ-P4mXLnzZFIQJUjkCMOGjDdEy376vbhRf8i7NSQ5KTRkr1KyXhBVKMU8PIivs4Yov7t-zCyJ-z0V22e_0JEwndywvqX38YCg-QCB3CsHlmKa91lgcGpbhwLVh4v5ckMoWuPwAxViG6p1L7wn8ifGjhmfhLIV2lBn1yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب‌منتخب بازیکنان خط‌خورده انگلیس از فهرست توخل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/Futball180TV/90147" target="_blank">📅 14:13 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90146">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzUvT4UjHtYpjvqHkx8QavZLpl0cO3ehWQrELx0dBmkMy6SGTjPw5EQ2nH8CQHThH012WKjvQ6pvaI-UqG04xHQPGHBChcH4w6pXzkrgFtNFfk6OlznbtGp-4YDEOVyj0B8B5Oh20P9V2HsyDLeA7jjNTJzl421AF32voG4QgkVgnh7ziDe9FWBVY442Wq2mp4Otv49jjuuKg4MVymYexauOlV5c6VbB15ndZqHiDLEo3-KB8J4K99izKxheGi-woAuJNRjjaXznKZTx_AOlsyTel6JANQPcuucXcvtrYbCOAc-1m4sgCtoTK4Sm3iyZ5PLdvbYZAYz99PAugpR8YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک با عقد قراردادی دوساله رسما سرمربی دائم منچستریونایتد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90146" target="_blank">📅 14:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90145">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hj4ThLVtTbzigF2Nt0Yhifvqg36BfRxL_Xsp44_vPatD5rqOx0qF77_ID2a9-KBPUoG8MGo7ly7iqlsGHncmGi14jzC9tSVKPgF5r9dPQ6RUKLppVbyoZ_LmWvZjehvpH7DNYSgklbdJbSf2oY_6YUrzweo2p9sT7PUj8X5xtTuttHqs88IOSyq6PuuixDPk4-lUEpGYP_C0jxmnoB6cjkqcXfI6UYpp-i6xXY7P_D7iQsrrSo6PjooNH2OHy2W5VEB5VlGybh35Xstdo5IzQr_OOwuD86o1M9vx_3BUkaFb3vO82Gf2Q0rMn4RoCAvYBNdZPsBkPbLqsM9Td7RynQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمی
؛ پپ‌گواردیولا از سیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/90145" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90144">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90144" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/Futball180TV/90144" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90143">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLEtXTBv0tmZmijXYeFCJigmmjq9-8bLC57BALE4LMtLGqsoEXYZAoGr_ZZiucQJX9ncuB4KYva0DgNK8HrU8G5ggl5fqA3qtFkqrK0bUUu6lBzXB1sKNFeMbfJUJg34AONzrXbxUBWIUMaCnHOVhl-4u2nzRMMN0flW4zPBm-XConF5bMmwMmJ-k3FF976hN1pLuC6K58TectI95imDQGlXOq-by0DlagcNIw_hdNVFAhKt36jGl0JfQlrLiQqRXHNYXuv3_sW5Iya6-ZWRgzAxrCTQQjnS1SCK3YN_kiq3q9oIze8np4p8OlZAFGe4cjy0z1BOO7QGjhSOaW7X3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
وان‌ ایکس بت برترین و خفن ترین سایت پیشبینی بین المللی که به کاربران  ایرانی خدمات میدهد
🔥
🎁
با افتتاح حساب در 1XBET از طریق کد هدیه
1x_1566529
تا سقف ۱۳۰ درصد به شما کاربران گرانقدر  بازپرداخت هدیه میدهد
🌐
Link:
bitly.uk/connect1xbet
🌐
Link:
bitly.uk/connect1xbet
🔑
برای ورود به سایت از کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
⬇️
اپلیکیشن وان‌ایکس بت
🔽
🔽</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90143" target="_blank">📅 14:03 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90142">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90142" target="_blank">📅 12:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90141">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZLdSOL_ntMVn8fm7Zpg9OwsMsze1PSiUHhxTiJYq2y3C4Hj5Z_rK4GC6BQ7Q30ve88n1wBeUYQHhuV9NmqMhhPOaSN56aJK7Pn4QfU8LVs8KUgS7b-leJaWmM6Jbm7lsyTjJ7zYtP6rmACxc-_A1xifsdIE5mVLDmKmS4HXKJYrec187vwB6sQC_HSkyjsH9KzUyUd6w3jtcMG6NmVev6xq5Oh9xzJy3_OZUJ46bXqyoT_ufJgapUXGGK1mRiPw77K_IzWz-GMoLRyHWXUBJOLpxj87a44mZqV_JMK5uedOXkLMlo4WrLSC2QM58i1pMu50BryeADIQiUkELJKKnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست تیم‌ملی انگلیس برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/90141" target="_blank">📅 12:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90140">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🇪🇸
آربلوا: با عشق و احترام فراوان،‌ فرداشب پس از بازی رئال‌مادرید را ترک‌ خواهم کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90140" target="_blank">📅 12:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90139">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🟡
باشگاه سپاهان با انتشار اطلاعیه‌ای با کنایه فراوان به سایر تیم‌ها، عدم صدور مجوز حرفه‌ای خود را تایید کرد و بدین‌ترتیب باید شاهد تیم جایگزین برای طلایی‌پوشان در آسیا باشیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90139" target="_blank">📅 12:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90138">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/Futball180TV/90138" target="_blank">📅 12:05 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90137">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpvSP6eUoV-VaDnOXOK0YbQn-6QyTe4bYeetVgfM31TM6G4ujGacNDBd7Eh8fPhktG093I8tiEuCycbS6g-AfNK7VdH_23ehznpo-u0Nwzx-y1be8--AgeL8bObxVZS-gjlTu16tOys2wNtPyrut0nlSoDWfwM9pdkHVqaWpiDmyW_Su-gh9IexUjfU6l2Xm4_w-UcNuCrSROZEhIsZDyk058BLcTXtgg4mrfEJdrrvB8h0mhzyz7M6kK-dxM9i21tNc94TMZrzKkU4QDrj6UVElgxVqYSJsXUSi8Ex9mQMuxNzUPOxYeL-aNK1QzRxcvxeSYA9OInAoKtgnXNybzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کیت‌اول تیم‌فوتبال میلان برای فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90137" target="_blank">📅 11:32 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90136">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
❌
در صورت عدم کسب مجوز حرفه‌ای توسط سپاهان، یک تیم از میان گل‌گهر، چادرملو و حتی پرسپولیس راهی سطح دوم آسیا خواهند شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/90136" target="_blank">📅 11:11 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90135">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCcDMPbeKI41ZtYTDnbzo7RCqr87xYITuy6GVmAji54m40HcothTG0CkH_ARIs6dJydUBoIFPHcwZT2xT7REccsOjg7Ln24McaW4kuQk3hyLVN5z5qQCNdzjk1SuLrAdaflEix10pRMa80jprthbJJhazN36yppBqslr0pkd9sIcRI1Du30jImDnvS_S9JtAqhjwAEDfmtMcDJQ3WAz14vH4B1qZsJd4Ih4F7oCIEKO-Hkw8DctSBrs6JevcMfjQ-iMx6u2waQwKJx6_KezKUh32R2fKGa6p9j10AD-tHDjjiY_hzRQ9nw1qbquWtA4554ZWI5dNpCNf9YhR3OZp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
آرنولد ستاره خط دفاعی رئال‌مادرید از لیست انگلیس برای جام‌جهانی خط خورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/90135" target="_blank">📅 10:35 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90134">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt7hM2v3qoQNeqvaRVygWawsRjOzZ21aga8l5xy_1hN6rr_6Ik8XODKXtj4DR-Ag264Aj7eWu2k0-hk6jOgOu-rfbMG4JJR0N3_8tNVzwgFZQbBc8Svvqo5heQolrW8ZWp85gGHPMjeWf7NtqWxPZy7cqZ-q3bDj3PB3ZUUanNN8lJNW17GKz9-rcFJ6YU0tAvUyNNNHWZQs2mvPnjlFAnbzy53SwvD1aa0Wt3abRpv_PJTzPajbyYt5QEK_atVCLfi5zhx1YHNqtXAmptYuvd_It1q_2QSCLIlIRagyrU8FebCsAFNhjKXwlxulv6Z4HpGiZ5OHLWEO8MBfjGeRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کارنامه بازارهای کشور در اردیبهشت ماه:
دلار ۱۸%+
💵
طلا ۱۱%+
🥇
بورس ۱.۷%+
📊
مسکن ۱۷%+
🏠
خودروی داخلی ۴۵%+
🚗
خودروی خارجی ۲۲%+
🚘
بیت کوین ۱%+ دلاری
🪙
اوراق بدهی ۳.۳%+
📜
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/90134" target="_blank">📅 10:34 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90133">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90133" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/90133" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90132">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RexAEivHmAmmiFCiVG_ombRTxU_qIG4ZQG9Nfx20cfxCpnUeBdGCHPGX74Ufw0U0v3hzX0izFfXcjrqsjDcZgSocj2G_fIAYVeDfO8mCVebejbpbINMH-d127k7oDjSPMW22wk91jHDwdYZ77EJPruHYPGPR9H_Njy9Uyr8dA1ZdfuwjgxV-mbIX-I7SdKw2TL2Yi7BexsU5EfRI7PKwwWMLXvm8psm7yqUPKm9-cnq_kVDTNGqP2qttHPwgFOrphAwN0uy-IFHecqs77-vUpAw3hYyHU6Bwir8VyjsIguzBSo4_FA0EVNnDrjN2-RAr2V47l4ewaaaW-s8oM20NeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
با پیش‌بینی روی مسابقات افسانه‌ای Roland Garros در پروموی Grand Slam Tournaments، فری‌بت‌های تضمینی و شانس برنده شدن جوایز بزرگ رو به دست بیارین!
🏆
جوایز ویژه قرعه‌کشی:
📱
گوشی iPhone 17 Pro Max
📱
گوشی Samsung Galaxy Z Flip7
⌚️
ساعت Apple Watch Ultra 2
🎧
هدفون Samsung Galaxy Buds3 Pro
🎫
فری‌بت و امتیازهای بونوس
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/Futball180TV/90132" target="_blank">📅 02:01 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90131">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuYlAVUW5tl-oykRdgho5CYte2Enmoa3JSeruKQK_G0zZC6QuO3vytDClvnTDKbQFOnCbGUKgdnoEp2Hr0JmhgZjXUmjdItZa_H-6OdslG6_CnwTTKa0qi8Uzl4s5ggFSzecz1oGXTcFCrUYvMKDiWfsFpXHBcwcI4knNv8MJyFk6BJD04l1KGI4MFgwDy_4OjyVXWzPNF86GL24Ul4UlHgFQoal-jFS2nskfH7SZ2Mvu0_bED541g5IqTLaPVOhFfsDATL9fjKO5vfZShMhXJ68-L2pH2JaMdxK9EtjFH9QDQstd-G0uyzGrySrTW7CzeqcfRzoX7XlbLX8M_nUKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/90131" target="_blank">📅 01:27 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90130">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=cGdZLZsa_liPT89UpeccES1Uq4dyFGWqlqcLRubSt_ju_rXdqeXgHJKuHG0WMYWeE0XRTyysROrhYz77PSolyf5axygBhO2xpjZHq6FWPwkh9jimm2qUqJ7LwiKskXw8_JQbkvfa_t5ED2PKuV7IgovpC4OFocO5i6_Hbt8vx9IlzJ9Qiko7w-CIiOORMS-QcJtX1GW0OjRUD2IsRL-ayWaVDVll3GY_vrmM5D2jPFEoqh14SAFbZAn6bVTbpbhKTn-KqkWLqbuoRQXXjQVyXjEUOyGArTu7vebe4vSabBOnVsFNz3FEXlBeKnfj37KlbyJSTPyZ2_IgbtjnhjXcaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90dbd94917.mp4?token=cGdZLZsa_liPT89UpeccES1Uq4dyFGWqlqcLRubSt_ju_rXdqeXgHJKuHG0WMYWeE0XRTyysROrhYz77PSolyf5axygBhO2xpjZHq6FWPwkh9jimm2qUqJ7LwiKskXw8_JQbkvfa_t5ED2PKuV7IgovpC4OFocO5i6_Hbt8vx9IlzJ9Qiko7w-CIiOORMS-QcJtX1GW0OjRUD2IsRL-ayWaVDVll3GY_vrmM5D2jPFEoqh14SAFbZAn6bVTbpbhKTn-KqkWLqbuoRQXXjQVyXjEUOyGArTu7vebe4vSabBOnVsFNz3FEXlBeKnfj37KlbyJSTPyZ2_IgbtjnhjXcaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی فوق‌العاده رونالدو پس از قهرمانی در عربستان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/Futball180TV/90130" target="_blank">📅 00:06 · 01 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90129">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHGIRisgHw1TCaX9F6EBSOVcMLhCVzEhzFYPOH4tXR8OUZNbJbvVVPP_MDWdfkFtXQMgFmLHqnvi0FyY902eAXzY9ZgdjufkE5NyHb9THk3nny9I7j8WeP07mQdxGhiQQElzLSrvhovLUGUdN7gtARsP0hfd6W4MODjoYePb_54StSHmuvCIV9zF0nmillEYvmuYbpwaGDOMBwpxsiB4YkjkfhGNxX3w3QZCxVFt4vze0RYVeqowVgysEz8XUCTX0eBhqOkZnH_WXkqA0MwkWXk-GWTXkz0ilJHxTlD6QGW01--zBHcZAyo7p0eqGOlMyMUhdfALU4tCnxR0YW7gFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
النصر قهرمان لیگ‌عربستان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/Futball180TV/90129" target="_blank">📅 23:27 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90128">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdad6VVshyb-sPgPKezl33YNcT5BYyX30_fk92D34MHd_v69C2K-YKr9yhq0gh66PHCWyjZDetk_EVWhrb_DosubtKeAODxNuKo7xU_-X3ONuITBaf8_G6kg0Z0ne9Ury-_QcrPl2mKtGqBbJtUF7oQ0epm-lIiXuYpmeFiKGjkP-Lz_cxVFcbL0yJgZgF_wOCDwwo8utqg7m1LzLwwMBFrB-QNrS9BtYRu0jUh5_vWEEvVT03fENCqWFYLlu8vWDIfXqFWcjeSoclZKIOrxlAUHSU1JXEA5VqecRIZgCORO4A1bU0NYucOkpfSDKhVfax0YHx4NSxxX43WfWfx9Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیم گل کریس‌رونالدو به جورجینا همسرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/Futball180TV/90128" target="_blank">📅 23:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90127">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdJG6U7RyIE4rXdtR6OlPnXI6SXBom3LQ0-aiIqiY2-LjhoHx19mUaKt6P6gqUsiTGQLi2gn_l6-yDqGpy9WXc4jMq7dG0YRY0sboiAqiGEk3E2dgcszvovtZuE35xQ2SVK51lAqbhLk6K_rSXaau28XGGdatrpZVul6AZaMvVoavOXhUF2m8jJtJJcEuAtL_2uJBKTUotU9TiBBHWvouaGSlPo5wjDSfQ1XL4g-iVYFWGqYlO82uZzlzHqgHdEjT1RKyIsDhRsKdHOGBMaF9iCxdf1lMK8DcCAIp5GsZWcBPq6mI19a8ML6HaIC_M4AMsQb-29It_KDkViWew3L0zb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9421ab7b51.mp4?token=oEnA9E_SyPpuA6Ee8VbG6bOIFXV30BUfr9dF0nlKcMaTTAEQupSIY_LTYibKS_9VdRVNapaFBOEWmq0LXW8NkERwT7rCsvdFG46aKx5ujlpvkelt8xspsvi5fOOPhIqjKh1ihns0LSh1WTW9riFhyVojwzrS6iVsbxCJnBTauIXVskz6DngsgB3GcjRD8UHWu3AE6t6Z1mQvdc8V6MPkLqS9uunSml_BQp2Xjnma4Uo820PVCsbl6BD4DmI2qeT-XF_wUwwKxxgFmcbBv3FxsJY6xOcrifAKea7ykW2YnsOL09TcQf-nTGL-SeDUbHTAvxwCQ83_vhoeAmGGg_jUdJG6U7RyIE4rXdtR6OlPnXI6SXBom3LQ0-aiIqiY2-LjhoHx19mUaKt6P6gqUsiTGQLi2gn_l6-yDqGpy9WXc4jMq7dG0YRY0sboiAqiGEk3E2dgcszvovtZuE35xQ2SVK51lAqbhLk6K_rSXaau28XGGdatrpZVul6AZaMvVoavOXhUF2m8jJtJJcEuAtL_2uJBKTUotU9TiBBHWvouaGSlPo5wjDSfQ1XL4g-iVYFWGqYlO82uZzlzHqgHdEjT1RKyIsDhRsKdHOGBMaF9iCxdf1lMK8DcCAIp5GsZWcBPq6mI19a8ML6HaIC_M4AMsQb-29It_KDkViWew3L0zb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبل رونالدو در دیدار امشب النصر مقابل ضمک
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90127" target="_blank">📅 23:17 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90126">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=kHP4whrzfkupJuMKM69GZ9n9NdzauaBOlDE6QkeUoqnjD9wqI5ODenfcWTEkHEIUDaQRR9otBxDe5ou2prjl_5_pVurR-F7SWBIvLT9OpjB1mfBn9kWl02BwI01YGCphVDmvgek09BhwFMkRhQYnXG3g5S2U9-sD789lExop4glQ_ilssenhQXJqtyOkqsrNV-6TrU9cLyl57obGp-zJkdKSqJge3ZZZhY-6ptNOwTCPTJ3M8kwU4tQ4vnbIhUF08RZeK_O5DKgUeasbHUJVBa7BFqFVwzc9kB48WC8YkGDPX_eN5uC54ZyTR2t6077JdHB-EVpKLUnE5gR6CSo-aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cbf0b75a.mp4?token=kHP4whrzfkupJuMKM69GZ9n9NdzauaBOlDE6QkeUoqnjD9wqI5ODenfcWTEkHEIUDaQRR9otBxDe5ou2prjl_5_pVurR-F7SWBIvLT9OpjB1mfBn9kWl02BwI01YGCphVDmvgek09BhwFMkRhQYnXG3g5S2U9-sD789lExop4glQ_ilssenhQXJqtyOkqsrNV-6TrU9cLyl57obGp-zJkdKSqJge3ZZZhY-6ptNOwTCPTJ3M8kwU4tQ4vnbIhUF08RZeK_O5DKgUeasbHUJVBa7BFqFVwzc9kB48WC8YkGDPX_eN5uC54ZyTR2t6077JdHB-EVpKLUnE5gR6CSo-aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
سوپرگل کریس‌رونالدو برای النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/Futball180TV/90126" target="_blank">📅 22:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90125">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SS8nqLvccjEd4DkVP9db962gqvNIepux76i4jDnmsepI2_TbcPtAE_KLDmeGEfGts8iNyhbuQmJlmIEeCrrS-OacFWIaN9nKoyHChYUyqJieHF8mzv9H5l6iuh3MTRiSAWLlEq7twWzRS9korMqkSSIIvgAU1s5eZy7g3txI1VOsmlxcb3lW_UFod7ZfNAwrHgacz00ChtS8ycRcFR4R2IwZI1uj-3swUdEgrE0CdEQ1ssx9gpTbDdHqlJXDkHIhVUdqinowMo1YruSQB7aRXWYVBd5Hen00cFu88j_bOUO6oCCbX47meMwjfjuhLxcAb_UPXLbNnjdmYnHE4uvQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚬
فیفا قصد داره جام جهانی ۲۰۳۰ را با ۶۶ کشور برگزار بکنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90125" target="_blank">📅 19:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90124">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpT469K-2k4mxau5r3JS465GvaGQe_D3D2yLCP8i5i9XN5ch5VXQ-x1kaW0bSYPQDYyJpodsSHEmxhQcSQbRh5HbIyDi7ZoMswGEzy21988_I5tVOjlrXyiu7jx_cEw5nRTn3okNDtXLENVWddRHINbAwDZFsWq-0ygLA5wWeph3aSntduqOPLOGDz-4Fyxi_sI8N-v_NTMKTR9uLrkCDU2mEvwOra6m-_bn5kRu-1kiQtJluL-bXkhkMJ_h7Dl8WqVaLPjTpVoliBLa8eU0NrF4vqlwE0R9OMhfXBjYeNeDXGeFpFrxeO_TUJWSYHzAKJEusvYtuhWYGq_Ig3caUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دوس‌دخترهای لامین‌یامال در سه سال اخیر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/Futball180TV/90124" target="_blank">📅 19:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90123">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90123" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90123" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90122">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjkzY72MWLmeQ68Ptq6SP4UxU7sENxvVNnWPCE_Ar3iwxNPXZNWqrhDRG9JWVvXgyRxQhCC84ZE551tAwvth3PMQz-QA66dUpvWVdMhwDzuByR6sz0Y5U0ZLSoycvcxiTNAFcmCx6DcRaPSuYF8YMdvSKR0TSrCmWDqatRtO0xVkBMQhtvDLnoav5i0H0J1HCZVh7drB8QtKdNoXR0XPq_QVdxcMMdSYWrMiekovSiKo8xrIjKVsx-dZW6Xe6ayyxpUAG66dRkTniI-LJ2CeWXAoGujoqqxYrWpUvnZWVePw5lrm9lnLaLQEmHVrmXnA2DSJN8vwQGk-T_DATUTjyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90122" target="_blank">📅 19:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkpUbt1BnSVt_jkp_BtunnR4ed7sIH_1hJWtkEuG98XHKrhVctq2f7g5Z_ILldxhxcyNqVEM9FVKFIxMH4mHK0xNafBxc4mZKfGAuaj2d2OLInAKNvFgefAIQMIN4Qupq2U06oiGxyWep_yWRAVKHMY_pjWWgdrjhHkVQldF-JnpjXrKBfUZkfiWjNWhxIAjueSfgbTQ1l5ndL4M8NdsSIrA9aRBwIf8JYjtSSqVSSGiRGfmfyZvWYOS1wQZpP_umFNtT4y_pJLSk3__1z8P3HqS-qJ5g3hA03rjNYFQf_pK93LAXHSSmacQmfY9JE2nd7uJDGLr6bOnonodoAubnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
لیست آلمان برای جام‌جهانی اعلام شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/90121" target="_blank">📅 18:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90120">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW8j5dv42o0qgbFSVieZN1iI6Rbdbv77oPdXBBWY_Xzaa1ksQ3FBtqAHs96uG6Ly7eC7J0nxpkXE0wZKXUtoiV0FWWwclrnhcTQDA_Ge9YJ5UlUsA2gGK6Tvs-dCWBLVPwy1tfrPYCZWBFa67gugf7pjP6-NsIbcb55juwusolMmFmjlkpqN-GxKfEtZvGdvlK06v9yqBiBlK6W035gcxJDejIp7aezAlRJLHZmo1cgkRN05FQwp2DsZbSv_XkPaKe197h3zPuIz9W0XsZ0ty1R349HZ2OefHigrpJfHoqo-GZRb1haGKWYTKinUZLGdfHIU7jzkLCj_JggFE-R35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آرتتا به مانند آرسن‌ونگر‌ پس از سه فصل نایب قهرمانی، بالاخره موفق به فتح پریمیرلیگ شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90120" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90119">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7sy8rMsztkzbNt1cyOyYtzoi1uZ4zdDarWBIII7r_Wn-0nb_ijIinRizOF9WLK5OlPlUjC7VW7a9Yyi_M9XFBXA4ozAlChjvhl-wQAEx-7t5lU6kp1PWFH36iWGcWz7OfpJGVyKXp89dZiOXAlue3XlX8A_Zrp2kNMfVb9hrrv5Mo1srzYYEt_Wx8KbDjSmlDOlUh_ezGkNLehgb2eZyC9heiQpojmiVimmzJG0JwfEuux6RomotD9y7a7zc7KgtKfq9RSqDleMbGFq6FMucF6OPNlgRyaDwsXQPAjSj73kw4BeXT9PrjbjKc4T38k-Ne0MvdQH5RyqAiDSMEeTOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی جمهوری چک برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/Futball180TV/90119" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90118">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90118" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/90118" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvZNbNKqSNkIUsAqdNSLtZQX1GHotb1ni0UltMvHsvZ4TO8bZHvlTTG-SqD9PUIy80RD9zzz_flix5gmm4Kl-M4R63TZXj-VlF-ZOEmgFyE8Jyf3CaVmZvC7oOPB_J6zifSgwu9yNnCnmUUp1CkF1n6cDaeC0D7BI2t2E0HAEXUVX7B4SSPqgyvnqpEKAGQcvdoUK40B60keD89O7ghHpnTXyo-NzEsr_EqeiPPXBsJ-rBh4x2NdDyIVQ-NWHEsoDl-EM-v740RBOtXFwqV9iIKRSHt5TCKai4PaIgYwZ3I7SmBqX4vrTaRH4nieA63rxbH-xz-5_QUiQ0WSTJ12-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎰
با 1XBET راه خود را به سوی ثروت بچرخانید و از سرگرمی های بی وقفه لذت ببرید!
🎁
تنوع گسترده از اسلات ها و جوایز فوق العاده را از دست ندهید!
💸
فقط کافیست ثبت نام و واریز کنید تا از جوایز و بونوس های فراوان 1XBET جا نمانید.
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/Futball180TV/90117" target="_blank">📅 13:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90116">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
فرمانده ارتش پاکستان، عاصم منیر دقایقی پیش وارد تهران شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/Futball180TV/90116" target="_blank">📅 12:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90115">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDeCaiWTefmPqjORpiw5ivDqtC0RqUQ3Y_WjsAZicAFOtLQel25hRB_dzebmIm5R1eByBvekqImpqZag3_sKxRqHueDFhJpNK5jlqRg2RLHIsViw6IrIiX0qorU35lm2HZ92iXDmq_MS4AE5bN2uoUeMuOyPulqVzEbHE2Gk1ITK0J7ZERI8k5YrK37EI4l7lGj8gJ2PHqFIN9MiiHP5WJo-tboXNtgTYIVdBzxYiLZAAIT83cD9wQ9pU3f9rLHs78DUmO9ef4udI_SCIfY9PtcsXZJH3lmcI7J98EaZ42H9V_rMwVh91EZG63Ps5cN2oUVHn7d5HV6DhxsAfGuxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه کریر فوتبالی لیونل‌مسی و رونالدو
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90115" target="_blank">📅 08:03 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kkn7N5BKcuw91b55_DvZry59ml2_xjvsxffcumjhf_cyf5hHXSzxtMsgrnHNpTxERWup5Q85cBHLhq9y2OwbqM4eHk1PWB2e56xN8Hk8kwlDzyp5ye6HBYl3K1bjTswg396UUh2r3RaGROmVx4SWhPrFs-ZoiPrmYJL_hP-lSYbMP6ZrWaAQVmI7dwIyI_wSu0iGXbBk1Bc6w1dfyRSn7Ze7IrOTk_ROYGU3cFgQAXFytv8KmqKVTqNwSgT13HDwvVCTBdsgZjcMi8N9YDCmK34tR_iSsWcrm2fcuRdBC0_SgBKvLwQ6UGr8LY3j6SCqKqiBTCVbvdv4xCtN6R1RdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🇪🇺
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل فرایبورگ قهرمانی لیگ‌اروپا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/Futball180TV/90112" target="_blank">📅 00:48 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
👤
برخلاف اخبار منتشر شده، سردار آزمون بزودی قراردادش با شباب الاهلی تمدید می‌شود و‌ این بازیکن قصدی برای حضور در ایران ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/Futball180TV/90111" target="_blank">📅 00:13 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
ترامپ: منتظر پاسخ مناسبی از ایران هستیم تا از تشدید بیشتر جلوگیری کنیم.
چند روزی منتظر پاسخ ایران خواهیم ماند.
تا زمانی که به توافق نرسیم، هیچ تحریمی را از ایران برنمی‌دارم.
در ایران افراد باهوش و بااستعدادی وجود دارند و امیدواریم معامله‌ای خوب برای هر دو طرف انجام دهند.
اگر پاسخ‌های ۱۰۰٪ صحیح از ایران دریافت کنیم، زمان، تلاش و جان‌های زیادی را صرفه‌جویی خواهیم کرد.
امور ممکن است خیلی سریع پیش برود یا چند روز طول بکشد، اما ممکن است خیلی سریع هم به پایان برسد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/90110" target="_blank">📅 22:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhhKVa9OP9LLxhK6P4LGvs9J2u0j10W0t6wdqCttbx4tTvcHgJJbvHyNtZmzYprgCDpKbWMtIFO9e48V3mflRlpSXeXro58FvMJlV2MCU4v49uFEncfi5P-01xAM3GJGnTKLgSIjpFlLmUXlaXM2NxPsXRgb36kQIq5t_T-pupHAtlXjYFYH6gSqDD9Hkpm3DzX91Yw1Htwp-uoSiBwVpMuMBLwzpIgo1L0i_9DNoAZVz_kxXLflf6X5hz70ixAdx7q6LjJY9wtwQtKNA777gAjhuT4T9VffZl8Kcvjis66Yu6jCsBrCYEVxRKS40tRDNZqeqVKrQ-tEjAgYr1alMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار آزمون: ایران هویت، قلب و افتخار من است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90109" target="_blank">📅 22:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🔵
مجوز حرفه‌ای باشگاه استقلال برای حضور در لیگ‌نخبگان آسیا صادر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/Futball180TV/90108" target="_blank">📅 19:43 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjnjVqBHa8Qn5KGUDzTYs3E7yXIXrh-rzXkT-D7yG0emg2-Pw6Oxq_hod94pSD9PYoCubxEgJkW1WbmMk_S0Zv4LNDRciB7uGJ77zarYqM9yZI_FAMOos35VE9APJFkaj9SveccRidrt7TjLSGrcmD5-vP1SMmFCCn9qZqtTqOmKCCbJH76BuWgcolJamzvaTcqA3rokrz1p9ISbfhFDjQkzDR5HheVz7SpdreQT7o1wX0BTAu6J7ZkcYg-clbVa3FiDPh0MkGAHPB6k3NpdGAUd9dPznxe7V5GX_dSknGOahj0XwIp_njESUr_xMKKa3_Ne9tYrFqmz9NBI9OB0_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کریستیانو کریستیانو؛
همان شور و افتخار همیشگی؛ بیایید همه چیز را برای پرتغال ارائه دهیم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/Futball180TV/90107" target="_blank">📅 19:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90104">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=f9MyPn2pB2aKv7UT3je_JFUTRI3bxM-4M1gA9e3Vig2y3xLx5uUfMZdKNTQ7iC5XRa5CaWuxZ4snPwBb6icm2AoIj8XfVYULXnPCBlb8IpRgxeqXZ4IO7F_03IH5SOcOYUjYZN8KsBsWYIPKjTSerRkFSINtW_siSRqRCos2NIMgtgAPmGtFmzh3mIht7K4NTyMXqjt4C6_oJTsPas3kRxBXCtBfDcK1m8CKELeA8Y2X49JXcdAnoKtBHU0pDOT3tOEjX2G7k_c4bf_YyTDufcYLvQbZeld_vgP1h8KMzeIo2QSMZ63KFpob7avJ8IE1qjO7BlCh_vFJhfdJHi5npw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ca121cc7d.mp4?token=f9MyPn2pB2aKv7UT3je_JFUTRI3bxM-4M1gA9e3Vig2y3xLx5uUfMZdKNTQ7iC5XRa5CaWuxZ4snPwBb6icm2AoIj8XfVYULXnPCBlb8IpRgxeqXZ4IO7F_03IH5SOcOYUjYZN8KsBsWYIPKjTSerRkFSINtW_siSRqRCos2NIMgtgAPmGtFmzh3mIht7K4NTyMXqjt4C6_oJTsPas3kRxBXCtBfDcK1m8CKELeA8Y2X49JXcdAnoKtBHU0pDOT3tOEjX2G7k_c4bf_YyTDufcYLvQbZeld_vgP1h8KMzeIo2QSMZ63KFpob7avJ8IE1qjO7BlCh_vFJhfdJHi5npw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
ترامپ : الان تو اسرائیل ۹۹٪ طرفدار دارم. می‌تونم برای نخست‌وزیری کاندید شم، شاید بعد این ماجرا برم اسرائیل واسه نخست‌وزیری
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/90104" target="_blank">📅 17:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=urVa7_tPDvtWGGuExOWpnPtuv-Cd-QONv2M2QEvgj_SjsYLqECGe1KxLp6qldC87hycFOVLB20e1C45qa1cJqGxlKxpyUmwoEm1zFz0KDVaS-R3EhAyN9ufC8hJCWrcLw1x0OspJyqX0aYSBtiAe7VmmbgKePmVSMK1GHCIXSR83st0My_M_FgysR59oAWwmGszPFi29Y0Vc6GUDlScl-EAE9_rzsMdIt6Cr-b1Akks87GFmmP-Ouj7DRIdDneeB9fMfyupS3BseKFysVF7h0gFeIoH-m7abehvnzRtJLPl1SotJc2WAI-3Hc8vSuyzDFZsWBlXxvaNtGUil21B0ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dc000d4d3.mp4?token=urVa7_tPDvtWGGuExOWpnPtuv-Cd-QONv2M2QEvgj_SjsYLqECGe1KxLp6qldC87hycFOVLB20e1C45qa1cJqGxlKxpyUmwoEm1zFz0KDVaS-R3EhAyN9ufC8hJCWrcLw1x0OspJyqX0aYSBtiAe7VmmbgKePmVSMK1GHCIXSR83st0My_M_FgysR59oAWwmGszPFi29Y0Vc6GUDlScl-EAE9_rzsMdIt6Cr-b1Akks87GFmmP-Ouj7DRIdDneeB9fMfyupS3BseKFysVF7h0gFeIoH-m7abehvnzRtJLPl1SotJc2WAI-3Hc8vSuyzDFZsWBlXxvaNtGUil21B0ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جدایی رسمی برناردو سیلوا از منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90103" target="_blank">📅 17:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90102">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/252c545abf.mp4?token=U0mnIkoftVfv0ZtzoGqKojCRntXlfkN2CGnhVTXA6YDiN2-Vl6c47OGB0Wu0xub05c779tZmaxw8c6kys4sWX5nFW1y37wDGKEsXgENB4w61sATs5FxOEmG9_iy2ZWr_l1i7Ym9xxhGgT_MHTW8V0_5VwHTmFZwUo4ywMrQhTkuCo6zMzYeD_UiwxBBEIBXyXYQgZ-57IRY1h8LvJ7QuFqsxNRQsjre1JqAqv2OR3pvx74BNi6NZQyEQId1sr5HQOjmwSklOyHHOcVLF0a0l9xF9h0-56yVus0ckCDrd0fBaTwRVW3UrQgW_tmeyEwK-0zu7FJPQBy_mr90-lzrHTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/252c545abf.mp4?token=U0mnIkoftVfv0ZtzoGqKojCRntXlfkN2CGnhVTXA6YDiN2-Vl6c47OGB0Wu0xub05c779tZmaxw8c6kys4sWX5nFW1y37wDGKEsXgENB4w61sATs5FxOEmG9_iy2ZWr_l1i7Ym9xxhGgT_MHTW8V0_5VwHTmFZwUo4ywMrQhTkuCo6zMzYeD_UiwxBBEIBXyXYQgZ-57IRY1h8LvJ7QuFqsxNRQsjre1JqAqv2OR3pvx74BNi6NZQyEQId1sr5HQOjmwSklOyHHOcVLF0a0l9xF9h0-56yVus0ckCDrd0fBaTwRVW3UrQgW_tmeyEwK-0zu7FJPQBy_mr90-lzrHTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چنتا شبکه‌اجتماعی غیر معتبر روسی با این ویدیو مدعی زنده بودن علی خامنه‌ای شدند و گفتند که به این کشور پناهنده شده :)
❌
سطح اعتبار این ویدیو : 0
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90102" target="_blank">📅 17:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90101">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
⭕️
⭕️
🇪🇺
تمام باشگاه‌های لیگ‌برتر ایران بجز پرسپولیس و گل‌گهر سیرجان با ارسال نامه‌ای به مراجع مرتبط خواستار لغو ادامه مسابقات لیگ‌برتر و مشخص شدن تکلیف نهایی تیم قهرمان و سهمیه‌های احتمالی شدند
🔵
این تیم‌ها با عنوان کردن مشکلات مالی و ...، موافقت خود را با قهرمانی این‌فصل استقلال اعلام کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/90101" target="_blank">📅 16:16 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qpn4Ay5bsslK_Uv_OPiKG1qPG-lQ18ToxOH9CzDdm4SnUywkeocZ22_0SKtf-6EGzI4050QyWNQkRL9Pf3nXhDP_DBSCV9OgpkEe12jpIrl-jk5fjoMciYsKKsK6M72jhg_wrre42hBngKSfVHRe_-nR_7pxTV65KcNo9HaDp-uZJHwsb9UM4rd6CTFawxw_QVu_kRa9-LkRFem9gmM4mpXdCHa3fQE-h2ShqgeQgCk5MBLrQOnKrOhN-AtzLTs5TwIF8a8OEvFhm7FLL5EsSCg6TpWW_QY1DrdZORIfL6xsqwPMhM1ZH5o62Wwlw9yynWquIurQnP5TAgT48k5VUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtBnKU2Y64cFeoM1aQTbKXZ6Se0uV-fMpofNoMEGCecdopO3dwgfarC4odBQUbGCMIwkofq-kN0YFEX5NWEOPLMT5n6URueqFvQ_L-tjkJDhmb3-5qzL4Pbi6o0ruAXuV-N7MZo8R4CgaAXtk0Q5EuWBesxYdAGz08mzaVg05s9QDSI4BAj79n6tMpSN20KMJXBqBdhAZflRLeZ-nJOoq1qO9ImqUE1f51SDjsTpKIVeO_kgILy7focCMSlRd1HWSE6Rd8TcYz4cjz7fGdPcOYC5s9KiNXnke7lVfK2v2zMFgv-fbcxBy12SMOuNkcmZj8pInkdXFZmOHKSgaQhmqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینس گارسیا بلاگر ۲۱ ساله اسپانیایی و دوست دختر جدید لامین
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/Futball180TV/90099" target="_blank">📅 14:27 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
⭕️
رشید مظاهری سنگربان شریف سابق فوتبال ایران در حین خروج از کشور در فرودگاه بازداشت شد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/Futball180TV/90098" target="_blank">📅 14:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=rIapx1jYMywzvPavYoBtTPqKjqWYnQHe96mhhykXhiTOF6F7HvlSm3uLjdCui4iTRMYSEfAlf5q6wNhPZronIrkKVBYpcM_LdA_srKiSKMJn0_aoJs1ssIu6pPfyRmsXNCRmutwBWPy5VT8sblnrexCf43oxIxfP8IaQwqMjntxFwil4o0emR6l2yl1dAbIcGBGrmxwEHw8q7pl3Z5jPkQLwVwiOmkt635ns0VxDwaMMDymdSIF_ACYyKlt6ulUWDJt8YuVz9Q5ys8S1AG_JSzHzOJ8j8FZwAUVHmS-9VBiMDWCI5V906QTzhmHIGyEmKQN4Z3azZlN24ZoD2AaJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ece86e352.mp4?token=rIapx1jYMywzvPavYoBtTPqKjqWYnQHe96mhhykXhiTOF6F7HvlSm3uLjdCui4iTRMYSEfAlf5q6wNhPZronIrkKVBYpcM_LdA_srKiSKMJn0_aoJs1ssIu6pPfyRmsXNCRmutwBWPy5VT8sblnrexCf43oxIxfP8IaQwqMjntxFwil4o0emR6l2yl1dAbIcGBGrmxwEHw8q7pl3Z5jPkQLwVwiOmkt635ns0VxDwaMMDymdSIF_ACYyKlt6ulUWDJt8YuVz9Q5ys8S1AG_JSzHzOJ8j8FZwAUVHmS-9VBiMDWCI5V906QTzhmHIGyEmKQN4Z3azZlN24ZoD2AaJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
شادی گابریل مدافع آرسنال با خانواده‌ش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90097" target="_blank">📅 13:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90094">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnhYhWpgjzqNXXXFaIg-u6HCPTp6h3y-2j-HUW972D98v2T47naGwdh8yWy5xggswgkJbY02q2PBgUMUAJdhGd59p-6urSLZKSAORlLAvJVpuABZcnX00wgqi36picZpqT-ftDyCmJYwNI9nRKBqM28Fl2fwFZbGqipzHDjUCeD8YFwVqapobUaALNGCcoROKQ6MX-zkjK2t2BQYYFd3NkHoKZj9nhv1ZrpMYMaAlmm5Y6AcXO2dhhDQnkBN47XZ2xsAq9t8dmjloM_oSKx1zDYFtP6Z65N-gDBrsRx_RXFnnKGU9CdBTzI_qH652-TXanztmRv5SJ9TrLcRKXgZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
توییت تاجرنیا در واکنش به شائبه‌ دخالت غیر فوتبالی در تعیین تیم‌های آسیایی: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده نباشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90094" target="_blank">📅 12:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90093">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e56d546629.mp4?token=Z-zTotQHE8mREeqk4b1xmw3U6wX2JmCFSPPm4NhQJLxHUb8uGwVF93_nl116SzchYNkLUNOtGsHT3aZ0Dzxtfj0znju-Y1hfTFVCfSEFNAgNcqrtseaiCLgMwVdC42cQ2rQWNzYBd4g78lBPamQyPnaHjnIbAGW3TsZpPNCIO6XoOA633NFjy0LlDxBKm5fRQUUcfVp95V4zsYQJYmKIGcuJxbTzu0v-NCuW1ycOKTWJ5SEs5n6D_-7M2LIDF4hEZaPuiLiJoFSnsMdeSkYVhKVY12-aTSXNl0JQr7VZIZPC6xuPAmvTab0vroR5OAfXIStZ_sXgkIMy6tmNx9sVcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e56d546629.mp4?token=Z-zTotQHE8mREeqk4b1xmw3U6wX2JmCFSPPm4NhQJLxHUb8uGwVF93_nl116SzchYNkLUNOtGsHT3aZ0Dzxtfj0znju-Y1hfTFVCfSEFNAgNcqrtseaiCLgMwVdC42cQ2rQWNzYBd4g78lBPamQyPnaHjnIbAGW3TsZpPNCIO6XoOA633NFjy0LlDxBKm5fRQUUcfVp95V4zsYQJYmKIGcuJxbTzu0v-NCuW1ycOKTWJ5SEs5n6D_-7M2LIDF4hEZaPuiLiJoFSnsMdeSkYVhKVY12-aTSXNl0JQr7VZIZPC6xuPAmvTab0vroR5OAfXIStZ_sXgkIMy6tmNx9sVcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداوسیما: هر کی جنگ نمی‌خواد، جمع کنه بره‌‌‌‌...
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/Futball180TV/90093" target="_blank">📅 11:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90092">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🟢
باشگاه آلومینیوم اراک بدلیل مشکلات مالی در آستانه ورشکستگی و انحلال قرار دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/Futball180TV/90092" target="_blank">📅 11:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90091">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=v3A6LyQ-cH8MFV700SNpBhbwe9pZXR06cD9LvMcSMZ34sM0_FEEW3GSacz8f0LW-VWB3Nud1tA5Kx-ZjCum2TedLKpP-xLB4bxGXKqi-tTGyiavQe8HM1FlAhuLMDn481PGrKx1Zm60j3p9C3SnkCveK9F21kgsx-xVNBEFX_P9sMsMBhBE8EalPwfoNO1rhj0QOEeSpOMiw50YrkpM_RHJ5bcBnWVxoomcYknM6osaIze8_hBYEnAK607vtku5yFQ0DYjVlz3rBLIUBosom5C8s5tX1B8FY1JjrWFhM9MrKmq8LQr6dJDdSeNH9zOg1Kj7eQW2cvs_JmmGA1oE3PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e96fba692.mp4?token=v3A6LyQ-cH8MFV700SNpBhbwe9pZXR06cD9LvMcSMZ34sM0_FEEW3GSacz8f0LW-VWB3Nud1tA5Kx-ZjCum2TedLKpP-xLB4bxGXKqi-tTGyiavQe8HM1FlAhuLMDn481PGrKx1Zm60j3p9C3SnkCveK9F21kgsx-xVNBEFX_P9sMsMBhBE8EalPwfoNO1rhj0QOEeSpOMiw50YrkpM_RHJ5bcBnWVxoomcYknM6osaIze8_hBYEnAK607vtku5yFQ0DYjVlz3rBLIUBosom5C8s5tX1B8FY1JjrWFhM9MrKmq8LQr6dJDdSeNH9zOg1Kj7eQW2cvs_JmmGA1oE3PzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
واکنش تند مامک جمشیدی، خواهر پژمان جمشیدی به خبر منتشر شده درباره صدور حکم پرونده برادرش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90091" target="_blank">📅 10:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90090">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
خیابان‌های لندن در تسخیر هواداران آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90090" target="_blank">📅 10:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90089">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7pWnGt3cVa0j-5UTMbeWuY240P5F4Qy5GRhSVcvDWuBNaie0pylB7YZ0RLG2Phi9SWXdKksp8hTW2Dg4szHF2mX8QReek3iU2Evp7xJEJMai8xXgSlNvTkt-JfWFuRr4pysRy3m8tzahJnG7agCLLKVsDAppsrtyVT7gUXJiTh-t46kiRymYl_sS3eG95XdpSZkSeMQmBK4orM6nJNd7RfVFAEZd8uO8mCFRdNdNk5Omh9WjUp7zQUwTzqQDQsNGAOvHHoe-Yx7B_QXlJcAWQps7tCys4iovZFeRDlAxevIEW-Ei6xgeFlEdLKnf_bslZColPnQ9Phy32MStnholA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد مسی، نیمار و رونالدو در ادوار جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/Futball180TV/90089" target="_blank">📅 09:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90088">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=GRXwxacVNjPirhDKzJ2N0l11HA5sTUXOLrrhLfVScXK7lAnb3qVmTvuMZRfdZStU9TMbbUdUV9p0Sd__qUKxcLLs5P7uELuvVYifL4LljO6pZr1bp5hwLVmPX4iUMcL-LzyG7DPuXtC-5-Vk8uEWsq2ZWgVo0DTC9Aeg4oiKz0pFBlzUmnrgq5I9s76UH3Na3zs8u2UOA5ZqfwscLgtlvuLcEMCM_6_u1rD2vnOglsRvkHM73GuxUDCBTSF9QwBiMdyM8dEqmAo_9FPKOcIOzJQRDPqpGS_9cWpjPZLP8mWmy4LPyV_Yb-5CMzBLaZAMocUnb3GYZsmd1m4t-eVI6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7578a72.mp4?token=GRXwxacVNjPirhDKzJ2N0l11HA5sTUXOLrrhLfVScXK7lAnb3qVmTvuMZRfdZStU9TMbbUdUV9p0Sd__qUKxcLLs5P7uELuvVYifL4LljO6pZr1bp5hwLVmPX4iUMcL-LzyG7DPuXtC-5-Vk8uEWsq2ZWgVo0DTC9Aeg4oiKz0pFBlzUmnrgq5I9s76UH3Na3zs8u2UOA5ZqfwscLgtlvuLcEMCM_6_u1rD2vnOglsRvkHM73GuxUDCBTSF9QwBiMdyM8dEqmAo_9FPKOcIOzJQRDPqpGS_9cWpjPZLP8mWmy4LPyV_Yb-5CMzBLaZAMocUnb3GYZsmd1m4t-eVI6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
رختکن آرسنال دیشب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/Futball180TV/90088" target="_blank">📅 08:42 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=TZ3nb48ZGqu24iyBNvVKMWRz-MjPF5D2ef6BgvnwS-72uzy6aj3HbowM66c2DSQV3V4bl6_kx7S4CFq36Sr8-NEJfxIxY4b7Ql7QPCV7wetLQ0bxh1kgiCx-u9HO0tUIsFMxdxGEDf1CduEsUrbGX2t31nupLWRcUVWpIa84RkPe2COf56qX5cjJl7N614Oz9OQiCltu3wPNdLA-FSknj7h0R0F9svPbP05DXAsKYdIVEv7_VsohZzHEng3bcFYNzCHxNb_KYRcbH2MVJqeKrOtMtQgavGGGw5guO1tCD5-qNkmgzTbBFFK6jnoxP6bmHu4KSw3uCPxdUBsqdi0y4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4882a411.mp4?token=TZ3nb48ZGqu24iyBNvVKMWRz-MjPF5D2ef6BgvnwS-72uzy6aj3HbowM66c2DSQV3V4bl6_kx7S4CFq36Sr8-NEJfxIxY4b7Ql7QPCV7wetLQ0bxh1kgiCx-u9HO0tUIsFMxdxGEDf1CduEsUrbGX2t31nupLWRcUVWpIa84RkPe2COf56qX5cjJl7N614Oz9OQiCltu3wPNdLA-FSknj7h0R0F9svPbP05DXAsKYdIVEv7_VsohZzHEng3bcFYNzCHxNb_KYRcbH2MVJqeKrOtMtQgavGGGw5guO1tCD5-qNkmgzTbBFFK6jnoxP6bmHu4KSw3uCPxdUBsqdi0y4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارجدید حمیدسحری با کپشن:
تاج‌گذاری میکل آرتتا در لیگ برتر.
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال قهرمان لیگ برتر در فصل 2025/26 شد.
🥳
⚽️
Channel:
@Futball180TV</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/Futball180TV/90085" target="_blank">📅 00:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90082">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=BcYfcQevStN5wme85Yet6f4SgoUOujobBdLmh3SXO6so9mqSWRoUcd3jgeOrcVsJUkF57ixCE9TAFHItoS0AYMeZg-On80nh4oAVQxlbMj3PiSalHO60nZy8pjWYA_BTa7DonH9JwPNBUljgBpw1C7ax2G47_Em_-uJ-DxxP9Lx8l3BNf2_mxPOfBZYikklNp-lmagOBKeNVLaFBJpIhZSXN-QvrKEyXWBOHZ6xcI3WNXZdEwjXlg3ynC_hridAuNG9fY_ib82X2p4kqTl3tXrxZBFZCkxR1id512m35yxZsLzKXVCQsu3hgdKtITom8iwSa3RfXBxNQD_UfIz53MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eae73a44.mp4?token=BcYfcQevStN5wme85Yet6f4SgoUOujobBdLmh3SXO6so9mqSWRoUcd3jgeOrcVsJUkF57ixCE9TAFHItoS0AYMeZg-On80nh4oAVQxlbMj3PiSalHO60nZy8pjWYA_BTa7DonH9JwPNBUljgBpw1C7ax2G47_Em_-uJ-DxxP9Lx8l3BNf2_mxPOfBZYikklNp-lmagOBKeNVLaFBJpIhZSXN-QvrKEyXWBOHZ6xcI3WNXZdEwjXlg3ynC_hridAuNG9fY_ib82X2p4kqTl3tXrxZBFZCkxR1id512m35yxZsLzKXVCQsu3hgdKtITom8iwSa3RfXBxNQD_UfIz53MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💙
سهراب بختیاری زاده سرمربی استقلال: یک ذهنیت به وجود آمده است که پرسپولیس عادت کرده است که بعضی وقت‌ها با فساد بازی را ببرد یا به این عادت کرده است که همیشه دستش را  به نحوی بگیرند و کمکش کنند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/Futball180TV/90082" target="_blank">📅 20:07 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90081">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjxNLX3WnLdsek3dFIgqRsvS691KvIVSJyov-LB1ttsMGG6WUfiTR27xDoT_mUq4fBiZ4Jmy97iLwcbpNoo0MD1qefuAnqomzTIWLlLqeew2acymdCJwosq127axsbglFcjA9NPb8ms7zOL_V_uZq3mF8HiuQtFGQ4rfgpT2n3p9tyXfw_5AP6OWOOJaiV58EU6VUUr0VUmVvJHHydhHHwzlNj3Dc1GceUvYj3agEXJ4z0fzg0X_swEJRxiqytT_EVcz3STf3oLXvmIc_iOwMetOkJSXQF97Vdbjx8u02EknSdZQ-7uz5Rm1TwE5zDXmRjgPVV1yoIGeC5UgpimCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
از این منظر نگا کنیم؟
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/90081" target="_blank">📅 19:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=mwmDf73fQOlCzfXb9UejbEUjcx1qAnWqYiar4GZHEQAKih-42U4o0jh4wQZy9taTFlx0hFWJhD3v3LLzA72SQcJKcZkixHM2ekxmCbLV2M5N7qDpWA8X4nIN2Sqz9eqaIhos-XpJOvXtihNPLby6TdC68ExiuZbM63a6jz8qtf3IzOzlMH167EC5l-D3N6c5IECPEPtiWbLBZf4dDKnViw8HV9PadriZGC9Y4CdbWRYkflkbQm9KFEBLIvThsnkqsWWAQ7eZihfRg4Zk4TuJOvTftMxQClHiExR_UJJtDiKUg-6sqfgaJhNUDv9CiQYV5dz8FhQ0Mmbn4s_YzzH67DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dd848eb99.mp4?token=mwmDf73fQOlCzfXb9UejbEUjcx1qAnWqYiar4GZHEQAKih-42U4o0jh4wQZy9taTFlx0hFWJhD3v3LLzA72SQcJKcZkixHM2ekxmCbLV2M5N7qDpWA8X4nIN2Sqz9eqaIhos-XpJOvXtihNPLby6TdC68ExiuZbM63a6jz8qtf3IzOzlMH167EC5l-D3N6c5IECPEPtiWbLBZf4dDKnViw8HV9PadriZGC9Y4CdbWRYkflkbQm9KFEBLIvThsnkqsWWAQ7eZihfRg4Zk4TuJOvTftMxQClHiExR_UJJtDiKUg-6sqfgaJhNUDv9CiQYV5dz8FhQ0Mmbn4s_YzzH67DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
۵ صحنه بامزه از گزارشگران عربی :)
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/Futball180TV/90078" target="_blank">📅 17:31 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90077">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=W3SjkkJxLc7wcgn_cGcaqjpd0dDP_qfOWRxBQFO73WFSKk9m2aBv3f4-kfRAZ6GT4m5cXZvbG0GU6RlDAxmodVhlWuqK0wb_AOhmy7m0BSv9Rt3V6lwasxJ3nN0A1WJUAtIrFkhKdFa8Ld0a9gUM0eqJ8wbGykisICIWrnzJ5JI1l9xER30tSEBqKYYPXtDnER8VRBr8ZUNyffgovgyFQZawjL7giIa4RJWHLs1GOzgxMIMT5NYHwQq13qZMiyLaZU6aYy6RsMg4TpVNFkkS5DrTh-VL8Z_SwMWTxfLndP9seRGSOD5o-zl51rOi_bbcy95U5PgQmJ0SOcMKlBk1BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bf46e469.mp4?token=W3SjkkJxLc7wcgn_cGcaqjpd0dDP_qfOWRxBQFO73WFSKk9m2aBv3f4-kfRAZ6GT4m5cXZvbG0GU6RlDAxmodVhlWuqK0wb_AOhmy7m0BSv9Rt3V6lwasxJ3nN0A1WJUAtIrFkhKdFa8Ld0a9gUM0eqJ8wbGykisICIWrnzJ5JI1l9xER30tSEBqKYYPXtDnER8VRBr8ZUNyffgovgyFQZawjL7giIa4RJWHLs1GOzgxMIMT5NYHwQq13qZMiyLaZU6aYy6RsMg4TpVNFkkS5DrTh-VL8Z_SwMWTxfLndP9seRGSOD5o-zl51rOi_bbcy95U5PgQmJ0SOcMKlBk1BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
شادی نیمار از حضور در لیست تیم‌ملی برزیل
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/90077" target="_blank">📅 17:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90076">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B3q8miZT78fKtTSmKU6QY0bmTDeppePKDOu0Htn6Ndukmr7jpXAZSC_Jo40ubbDLN20NQCNeacziNbkroItK5lRetI2jrl58ruiCNE9Bak4xWGqcX6NUuIHZ3fvelc2HxI7Ba-6gA_IbXPLapwVFIFbpcSarD1NghDaAdNElTY7dd4ssG0tAVncTTi5J8igevB6bJ5wrwlh8NId48ADpzwWL7aURyn6wcppmWHzz2wR9uRIFgIv9JgfrzdKTWeHFpU6UifI-u_WIBZkKg2k6n_QrURseofOL9mlio8lHJR63x1rsqYm7I7AZTqi96H6QS5kLwVEhzS7F_PusDhFpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
لیست تیم‌ملی پرتغال برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90076" target="_blank">📅 16:29 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90075">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=Exjs33vByN8nvW-FIBRpIxjPxitxqUBVJYsyEXvOzTKDmAlW22GKACw14w8E13ssso1gOQJa-Mo9Slly2ZXjZKwEinxYvFjkUS7ocDt9p-0-jZlSVKJZmI2n4R5rJehE8CgwkR2h-yNHyIMlVo12rBqfCyQDb1nS-naxVfm5vI5yN1xYq12ifyyWwpza72B5CStpDCM34g4c-x2cbR9PpIeu2drnUTpI6PMN1eEXMHGtFI71pQb8_JLjZCYCTsTCT-g4kcgfPIbbdHVTl_NqnBJsEqN1lk8eFfuszXVqTpsZlKSry8Py7q5_E7TfMItuPt_tiL6EREZmtlh3roKNFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3576e35.mp4?token=Exjs33vByN8nvW-FIBRpIxjPxitxqUBVJYsyEXvOzTKDmAlW22GKACw14w8E13ssso1gOQJa-Mo9Slly2ZXjZKwEinxYvFjkUS7ocDt9p-0-jZlSVKJZmI2n4R5rJehE8CgwkR2h-yNHyIMlVo12rBqfCyQDb1nS-naxVfm5vI5yN1xYq12ifyyWwpza72B5CStpDCM34g4c-x2cbR9PpIeu2drnUTpI6PMN1eEXMHGtFI71pQb8_JLjZCYCTsTCT-g4kcgfPIbbdHVTl_NqnBJsEqN1lk8eFfuszXVqTpsZlKSry8Py7q5_E7TfMItuPt_tiL6EREZmtlh3roKNFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدا رحمت کنه زنده‌یاد علی‌انصاریان عزیز
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/Futball180TV/90075" target="_blank">📅 15:30 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90074">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1631168f15.mp4?token=lv4WHNDdv7xqnbaZYgfgkCaBVh01vTZRQDuerX_sTMLN8Nes8ZjHfskkjMEcWXGlhJViPSau8OTaF7qbTj7j3IYnR7ygyR0RSzY6CWRnhh3nElUaH0GfbpDPWB2mRdgwVW8_0LELEJBjuDbEt6HSeOODQ7VoZdof_Ga_RRFjwIj6d4zBZlwW0QYS06OGc0y0Hf3NgcfOiQKOEvXQ-iJHi4WM6jWc3-eWNWVqANHmTpq1Bjpv9woFCED9PzMkFR42no91wq_zekO7BC-3wHC5YESrexyL7aJ1UL1ezKsWg2L_Cv58SeHgiFxEMXX-lnB3rGAJe6OhVJB6l6DWtZsRxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1631168f15.mp4?token=lv4WHNDdv7xqnbaZYgfgkCaBVh01vTZRQDuerX_sTMLN8Nes8ZjHfskkjMEcWXGlhJViPSau8OTaF7qbTj7j3IYnR7ygyR0RSzY6CWRnhh3nElUaH0GfbpDPWB2mRdgwVW8_0LELEJBjuDbEt6HSeOODQ7VoZdof_Ga_RRFjwIj6d4zBZlwW0QYS06OGc0y0Hf3NgcfOiQKOEvXQ-iJHi4WM6jWc3-eWNWVqANHmTpq1Bjpv9woFCED9PzMkFR42no91wq_zekO7BC-3wHC5YESrexyL7aJ1UL1ezKsWg2L_Cv58SeHgiFxEMXX-lnB3rGAJe6OhVJB6l6DWtZsRxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
ناراحتی شدید خانواده ژائو پدرو ستاره چلسی از عدم حضور در لیست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/90074" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqYo6YI9U1tuye3KcE1STrI8_4z7qKz6YHET3rid7to5_yTCKUlAiqbjejaVuZDV3AObSDpHVJP9ZCcnELBSxQ_79hPTu4AR5HX9TtvDOeghkGufa3OsCaMC2Av3bqZV69oJzIC82F8LTPBta9BVEiBYvTYiiACQRA7mEezsJbdHKk0uRhzae6kMHB3JuBvt4i3rmPaBSewg9ZX-zgItRGI1eRyzxD0-0fXqT9afl7EvX30QR2XBPVE2fObW3IJI_R8-X0oaCT-WbB0-zUegITfbMhgCA8LtgOElRaGlw3xfm36c7hQ-Fz7dwT1tTHNPIBoX5tpgoy72c9ze6qgq0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با ارائه پیشنهادی خواستار تمدید قرارداد یکساله با آنتونیو رودیگر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90073" target="_blank">📅 13:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AK2Oa4DtLDh9lFblgitdLW3P5EJBHLm7_tzU4sAA85Dcj8rFl40UTfD-pKqwJNlGQ30whgKFvgzhsoWkfLMKgP5uZeCprieHo8XvJNBbh-6NfNOVKSFMBHMgNEZQQaudX7YqKkwnhuGNpS_xMz3T9YZ-ygQ5w2r5ldJUkpSnJ40OEpBbO0SlV-uM_D8o2ryXmSGY3_E_lj2nJimOr1zuG_-nZG7EfpxOVo2VTm9-waLuBbGhLqgBbOlaE088Lnrc2GLp5Yhpad5ixbzBI7-WURw12P70ipyrj-6qsSf8i6SOVHNq4gaauLgHlNMhVcndQ5fCv_dBNlgovFaGIbBOsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد قصد دارد با ارائه پیشنهاد هنگفت با لوئیز انریکه سرمربی فعلی پاری‌سن‌ژرمن قرارداد امضا کند اما در عین حال این مربی پس از پایان‌فصل قراردادش را تمدید می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/90072" target="_blank">📅 13:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c098031df0.mp4?token=EzWmqrRCE2jYmRzSAEh6Nj8epDOznUpC4Ae130nF_QmzVK9-H7RGPdnDvrgtPaA-M3xLKy2Ay85IrNxZnwnBcEfUpXb06VKF1yRvT3PRh9JY2EMojeveIP9iDt05EvAA8ectqB2JSH2N5j52l4kK-RpqO-8klEU1sK4-GLidpE6buKqwfc_8QpUUpCsD193jGQzehdqyOD2Wyma2w23tWaHUDqHQiAtH7ABPjwyESgh6m7xVZFpO2Rh3uza2KvLEClb-_ue0So0FIsSq8XVFINKSMRDHARHyrrJABnPocun-MBql6N1ifC8VLiqdQyKJEcUeGi7x5F6-r2Z_KKu4dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c098031df0.mp4?token=EzWmqrRCE2jYmRzSAEh6Nj8epDOznUpC4Ae130nF_QmzVK9-H7RGPdnDvrgtPaA-M3xLKy2Ay85IrNxZnwnBcEfUpXb06VKF1yRvT3PRh9JY2EMojeveIP9iDt05EvAA8ectqB2JSH2N5j52l4kK-RpqO-8klEU1sK4-GLidpE6buKqwfc_8QpUUpCsD193jGQzehdqyOD2Wyma2w23tWaHUDqHQiAtH7ABPjwyESgh6m7xVZFpO2Rh3uza2KvLEClb-_ue0So0FIsSq8XVFINKSMRDHARHyrrJABnPocun-MBql6N1ifC8VLiqdQyKJEcUeGi7x5F6-r2Z_KKu4dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پاکتا هافبک تیم‌ملی برزیل و دوس‌دخترش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/Futball180TV/90071" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZA3t2X30yNqdZAA_7t9BJpXKhfcdqy_QA_8gjiPAtJdnLape45ekyrcom4CuWXWh7KcdvnOyiKif8zLvz4JzAvKydX8pYN52IXnlsTgyvkFKRaeZepi0SB2IDZVvVntKnthnf9t_-76t4UXktIkQ0mC8ZoW3qofrj3NoLKGSbZ_5n5mNTpxz73ijNVyKbjNGi0ggBYUVA197bof-1QV5daRj9axOJSom2_ZWz3jlsQ6fFcB95fvK57sQ1b4NdeMYDuFvXy6z8RrmeNEpYUpJyWW3W0tbbCCssY8gEOcPjgXGfqoFhAz60qyGHUWSYditrxesUCdVQsPgRy8EGXiQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کیت‌اول باشگاه اینتر در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/Futball180TV/90068" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y569r41q-ZSJcuFuYFzu9hvDZcTT5hSdFtP_Uf5aIVDPet3OXru3j5WPsT8PDNpGvTLsoURYPIGyEj2P9OlT110ZBfCYzzikPd_tSp-uFXfvlX-itdLQnf0L4_P2HveEvMBMn1mftbeE3be-3GV8IZVNyEeHfLJJJzcGi2hbeWf0uNoxsShkOhpA8_QweY9l_A9Rkik2yNCAHCm7RYvq6oxnK0G53-r7fLxniu7r61g_h7r8F6e8w3MfnQ6V4SdF8rPPysv8htLdQvqwT3w_9qlPPdTzeUTZ8fywX8lWMUo1qbFwO7IAIxdm9sKfw1aup02sIC_ra1D0tsPUB2TGvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول فصل‌آینده لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/Futball180TV/90067" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
