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
<img src="https://cdn5.telesco.pe/file/uzU0bHE8WD7WLD1RwrUy61HU63NqUuMbybJyaDwe2uMEWy-sY8kJBkNF3wDbNPJlmbjmKYpOMIvSmmjzHwwX0XH6FeII2MwZbr2YgW50TzttE7SKep-pC0Jz8wZPiSDdsvKlAigj6kbmPw09Z42NN9wYTb4jp9es8F7EDBbDmt9bIhbhpJlTArGKpskuqhxmyZXgBU_TZoxZnY-zgtLYoDbEpkqKelZ7Ext0yE9wDoa8PIyTdodov5BmagSUrsTuAMRHNNxbyVoGt5BzLcTSzb1N3s7KqLPTN-aHqUt1N31ZFaMw1fpHCQYhqrcBrk3l0zW_nwIzjdYsq3y_fTt9sA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 400K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-107324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUSqJduvM2oaAPDiJ2wQ9z-k6u0hrZm3MdqGSDV24d9TpK9p_s6aNlmP573Zmn8Cgkf4zI3x-RH2d7zZq0HGk8PkFixLUIMRCTZfZH4KxZ2F3ASiPk6U_utBzTX0SeLKgyUoODJ1CPhjh4gsaSyVY9qM6srSaH1buquO-39G4nmY8M9fuVdqfLWXd_ZEtIOjsZh_HWvWyiRpg2u4Mb-yuZH5yhj57uPFiJ8zEhNjTFf_Cni2O3yR9xgLzgO-BZ3coFcWE39W-b30jYhA4dAptTDCwor0mEQC8TEVOmubrnpUSJ-IDPb12kLN1HNfdrqcGeO93B7OGQDXEr8vAEvMKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👤
علیرضا دبیر: چطور مهدی مهدوی‌کیا با یک گل به آمریکا از سربازی معاف می‌شود؟ حالا هم علیرضا بیرانوند بخاطر مهار پنالتی رونالدو باید از خدمت سربازی معاف شود و هرکاری از دستم بر بیاید برایش انجام خواهد داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/107324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=KP3FsvcRa_TtDPOKwHWkZOpylWNBhbiRACcPwJaR2E6v8c66feL4Cf08D6nERs0dZKYpgfhrucinKda1Zq8k43JTz_aCnqeAFxBTyr_XsgjDcrW-EkEBvLD1W3dWrwCzTaWdE_7Eu20cAFPBIBXdR88y3fMIoAmErRQIWtM-n6DUd4iy8GYm3YmD2y_Ya1IR-ua9stU61EOmNPim6bWnxhymg3TXZB0y8g5-9EUDJB2ZMUCJss7kwvNjPRXRfUvFn2dUmNYlKPhFhKeSTkgrhuMblfl7Lt15_s6orVvc-k16sG-CPeCH62pjcQ-1Yk60BuJqvvt1-N9N1_aXO-AnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
عصبانیت‌شدید یاسرجلالی آنالیزور فوتبال از وضعیت وخیم تیم‌ملی با قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/107323" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🇪🇸
بعد از تست‌های پزشکی مشخص شد که کیلیان‌امباپه حدود دو هفته از میادین دور خواهد بود و مشکل خاصی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/107322" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=bJUpfOZbk5Ilm0Qb0i-oHAql415yOcvvwiDFXG_jFoSBzypvKSfSxFkmOjDrZnlYU96rr4UxGaa1n4JSKkjwdMUKZLHrgSmDJqij0bNloxYlxXjO7EO-q8uTJhvKgu5c7v5CuB7dt0n9d-uKcMRUYKI7QypMzJWBk_MiUL3i93xnj0wsCuC0bRiNok4ts8bhAa5ffAtyC3VTOZDzFI50BreCK8pys0-CZLdE6MPBBA2DLSu9AizscHbqRP8r6S8klkyXsn00Jrp_zMNP5Lyk0-p0a0b-mWy_xNOB_HvEjZzsWP234kkHgDKBhLObyO0mFJLXRJ7PXR3K-Dax0orYdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تو مسابقات کبدی بانوان در ناگویا، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش بابت حرکتش
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/Futball180TV/107321" target="_blank">📅 20:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=Q4WhJMYxl0YD77MjVR9EQ1fxPhRAegxlnEOnIAG7iOjRZQjwCHNpxwCc3DzZIOWtHRt7Y7_PqjYJhULMGzjsJIAKDLdIFKeyProawzc6dqtI3vLmfpfTmY5bDfQwqqy_N-OciqgyXHKIg2ynGue_QpfFGUoox-aBuvCBL7pII0xAcvqMNLzJTjwT-6J9aaPTnuQ8zTdqNpZZw1XeRrYcHGsZQZgbgEuoPz1wSIxxapc1aQVA_ovqnTZytbmEltIRMmPg3xeDMBJDpcPUjUDz-xXoFLKCE3Y4xGH3kcXdHuFWaxoI31ShPS-NYPevONR8wfFuvrOlvgQYWTn8XDUPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
حمید مطهری سرمربی فولاد خوزستان: دوست دارم یاسر آسانی بازیکن من باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/Futball180TV/107320" target="_blank">📅 19:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=nc7AuqJ0PeSA6qAiFNKtzhsxv5_-elSSSIwivZmQ3fXUsw9R1I0Ttk1Ugt39ul0vs66VwF3kvOhV9k633sGLaV4nupnLJprFIgNZz78IOmAzNhr_UTwzgRfn6Y3Kj6NDszAkiaixda-rR3XB7dFVphwIqpyGYy0PCiMnF-nYMdCZHvhWaj_GITCQBqD4j5DSmkBWEFGHJ51bxezF0G45-cQAvfl62diKdFsaon5fsQOxN9Y8IlGw7HM74lbXVQXVt8a_OZC7f6bLm6cm-CbI8yNIUlk8eKUMqUM2lpf2kqjQ8KOUyFHbQxlUY57d1zhk4UVcmLk_eNXvKYFY0tLaDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
عصبانیت رافینیا بدلیل عملکرد ضعیف وینیسیوس در بازی مقابل استرالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/Futball180TV/107319" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO2sTbwt_sv-qrcjTNEkJHkgdFkHt1HJUW-IirgGXlVQnq698vFeWunMIOMjgFYOpWmwnZVcW_58DlGRoreC2vkZzXVvgcWYI7A56XLxkofhSjL19enT1evfkX1OVT4T4ajV4myKG58KcP3YDYXwI9tOfD73GRwgb_899kJJoHXRi8LVJxSp4tbY0IuOWI2Qt-pGIVJsmqY5uq27NYkIZvOJPxCgPTh6ZOlNNIcMv-KOcpxU9_xGvWG7s3-wrcUSNhv6i63vXoBl_emeZ_Nc1FdBCvaBVEzsY72cICGuSfRlbGbXX9lmqVwfajv98DALFEuV7Sh4w0S4UOrbmkFAYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پیام‌تبریک مالک باشگاه استقلال به مناسبت سالگرد تاسیس آبی‌پوشان پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/107318" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aq8cB_xZ9TbuJAbE3_QJIEW4l-0TvJiFYOsl7VqxTh-F8_KTNSfTamanBHnNy2MpBSOqo9CkzZltwANPI6YLn6wlupEnVbC1rkyWqAnmw1IOmlmvWaE7orCsJQyp3s_NaB1LwFSzy0ELT6RW_AzE83MwoSDZozTa4G5nbA3zfnmdtxShLtKkp-qZlAd2zJNLcIMPz-50AzaAXYtsSjynU3K3kSykmJgPI30-JWmfdoCDHfY7RVS1x5ozsR34y9kXv87U6FJgImS6YdBRXL8qYTmloVrnqwS3mZDcfB4EcAVuF76Cu5YwWwB1lX1JR0p_GpeVvZIz91fCr5_rv2kXVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چند روز پیش موقع آغاز سال تحصیلی تو تهران، تو یه مهدکودک مربی از بچه ها پرسید شغل باباتون چیه یه پسر ۶ ساله برای اینکه جلوی بقیه بچه ها لاتی پر کنه بلند شد گفت بابام سرقت می‌کنه تو خونمون اسلحه ام داریم
🔻
مربی میره به پلیس میگه پلیس میریزه تو خونه این پسر بچه میبینه چندین اسلحه تو خونه دارن و پدر این بچه، رئیس یک باند سرقت مسلحانه از منازل مسکونیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/107317" target="_blank">📅 19:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107316">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xcb-6f020xGg4yUh9XrMI816nO_WIbt_PXG0WEFv9TEVvfPXIXKGTGYVnacaMiGy0eje50qrOJSgHNs2Jx5PkvQ1FLXNVx_Lr6VZzxhDiZaDxuBKQxRBGLhgZG5v3W20amzjU6tH00BGSvqUgm_v84o-go5VL1E3ylUo3A-kYUGt-N5NCUnXUyIPVxgucnMriYefVJw7bsZEQZMcXjy3GnlzmKJbz6tQdvAD2Ub2626fIbUZ3sZY7FvmqrJ011VJkJ5nmOpU8G2JJsxQfRrsdR92wRiNeiezIioWTYyEny-3ccr7i1oyg4wIIdJJANejCOKuAdggVUbkBpY_XTC03g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
تیم منتخب انگلیس و اسپانیا از دید هو اسکورد به بهانه بازی حساس و دیدنی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/Futball180TV/107316" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107315">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107315" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/Futball180TV/107315" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107314">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKSBBY_7KsrtjNizvFOseIR1DI7bgX7PO2zL_V2D8EYr_CruZk_trA7Ohur-GlTOaMt9N7IOVzSGMdx8MaBkjiXzSy3UqJfCjvRFeTv8s0zRDOHfS8QsPB06ZDCYOza_PCn0Z9NnOw85GUpahKhbljNeafyGCghPzpez818on_VBAnVO7AW6ogZtG2m6V_Um6bsQcsnon6RWCS-Xu1Wl3NScjTp7ApKPmcZOUvIkiz1kB47n41zdySsaKRvcVUfL3mdj-ichzFipZE5yOjxn0CVYolqcPA0IZVZyGbuZ5gN4EIlHDXVQcEThbPr3MIfR0b4NP_XjsKzRV4lPLKCzBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/Futball180TV/107314" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107313">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=clHPZluLud7yn49YsTuGkvF9nThinFwuc8cft-3qeXd-M9iGrVkyYZO7rSqIKu8ripK7_4b5SRrPLtlxYpDTfOjJ0dT1r-17ecUswWjoUGN7B4ff8jFOaSlzinVe63SwTE3yQn6gMjvqFIPiL_l804MLKoVz7kb5E_cZmX9ZHYt1CWeME40h5wvMdZHW4f29r-gZd9wL0up44lKmONd83cIuLtKhTYzdYGzcfXf_St2NXiczLsbo5LJBcZTuNM68wZ0qI2GoRHI88l99N5fDu-N6ZzRQhisyTesSgHNS2GswC7QnD03Un1207RAawXrNiZNQp0QBDJ-Dhhue2TiuXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=clHPZluLud7yn49YsTuGkvF9nThinFwuc8cft-3qeXd-M9iGrVkyYZO7rSqIKu8ripK7_4b5SRrPLtlxYpDTfOjJ0dT1r-17ecUswWjoUGN7B4ff8jFOaSlzinVe63SwTE3yQn6gMjvqFIPiL_l804MLKoVz7kb5E_cZmX9ZHYt1CWeME40h5wvMdZHW4f29r-gZd9wL0up44lKmONd83cIuLtKhTYzdYGzcfXf_St2NXiczLsbo5LJBcZTuNM68wZ0qI2GoRHI88l99N5fDu-N6ZzRQhisyTesSgHNS2GswC7QnD03Un1207RAawXrNiZNQp0QBDJ-Dhhue2TiuXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گزارش جالب توجه گزارشگر مهمترین مسابقه هفته دوم لیگ زنان بین استقلال و خاتون‌بم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/Futball180TV/107313" target="_blank">📅 18:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107312">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uRBj8tc_HF7cfrDI3zeyf3J1CzCH3I9XfgrZS0fTZE0baq7tWcPrce21ryXuwVfyImv5CpRDI2Hcw6_DBIz-SktiRvftsAzgjxzboVvKDFwhKxz8uA6H2hVK5D58lQcSXdcfCOyT2SjdU_zTlfh0uuWDQPrUoHiY-M8XcAxyZjmOsYStejB-XhA1FBkSPMucp_WzAVNf4u6dDtpbrB7TVBPPek0XG3fKltrK-O0ycldg7HWg_-zBCdz4iAylzvJtH0H4CXhO2uvqgi-icCXZI-o8c0lFZ2dBcFgjCRSi_DIjauOMoIjkPgRS08RExFaC2lv4sD7_JruxN421LeQxDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودری ستاره سابق سیتیزن‌ها: آنچه ما در این سال‌ها انجام دادیم قابل سلب کردن نیست. قدرت و سیطره تاریخی سیتی در لیگ‌‌برتر هرگز با رای دادگاه از بین نخواهد رفت و قهرمانی‌هایی که کسب کردیم در عین شایستگی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/Futball180TV/107312" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107311">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRrlcVHzgjKtxCpDHLN6Legf5JXrdD3Yt9eyIm1QtBvo6ivC5mgfkEB0jNe83q9Pe_5yglTisGfkHlX_3Rf3j5ArkyjpDEuxKT0UylBEy2ebmIZKfwVDFdbWOhK3vTQE_jYJElNpbSDGujwGJqAJBsAj8iN_0L9cvX-HHG2-uOwUtq8eV6wuInY_z2fqJqZyb5LS-Tu0llurv5vGPNFS04wKtDRn3HbJ7NXHqEtf1hplS8CzgJ1Bdbxw9ztkDYT8uVI-f034l9ZPcBEgoeZKnCcxFHYmwZjsERE0qVcxOnl5shN7jIGyyJ-dZzdraiWCeoc1g-lUzjh-EvYTs4nRRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
لامین یامال ستاره بارسلونا:
🔻
من برای پول فوتبال بازی نمی‌کنم، چون دوستش دارم بازی می‌کنم!
🔻
بازیکنانی که وسواس گل زدن یا پاس گل دادن دارن از بازی لذت نمی‌برن.
🔻
من برای خوشگذرونی بازی می‌کنم؛ برای دریبل زدن، برای بازی با یک یا دو ضربه، برای اینکه به هم‌تیمی‌ای که هنوز گلی نزده کمک کنم تا گل بزنه؛ من برای شادی بازی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107311" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107310">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
⭕️
⭕️
🇺🇸
ترامپ: پیشنهاد ۷ بندی ایران را رد کرده و اصلا مورد پسندم نیست
🔻
ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است. ایران خواهان بازگشایی فوری تنگه هرمز است زیرا متحمل خسارات سنگینی شده است. من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم زیرا متحمل ضررهای بزرگی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/107310" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107309">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB08Fge3tXi_a7fEpAOLQipIlo-S9BHp7G3CGjex9vMiKlZxZ3duSq2eM1nIZ7SzMPFCMHm7aEvx3dBxVdYWSm5q8mgLt_D2kFq_XorcJeBMQcnRdDtrOQIuMSvqcIxO_RVt6DqMY0xll-VIKYi4KFmKfDyUeB60T2b_qUfqIZOmf8UaemzW2OQDT3NDihLFxSkDJjku7S42q7kX29hPo8NakOZVyldjTd3kZFzSi2Etv_eiVCeMcYY63VuMfnVwdJNF9oJYlTbsANXgn5nCSL4DRgz8WpgMrDxvZVX8iwL8rr_ee0rM-bJEhPljzdRscole-npl2CUYKmvMyT_YV2eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB08Fge3tXi_a7fEpAOLQipIlo-S9BHp7G3CGjex9vMiKlZxZ3duSq2eM1nIZ7SzMPFCMHm7aEvx3dBxVdYWSm5q8mgLt_D2kFq_XorcJeBMQcnRdDtrOQIuMSvqcIxO_RVt6DqMY0xll-VIKYi4KFmKfDyUeB60T2b_qUfqIZOmf8UaemzW2OQDT3NDihLFxSkDJjku7S42q7kX29hPo8NakOZVyldjTd3kZFzSi2Etv_eiVCeMcYY63VuMfnVwdJNF9oJYlTbsANXgn5nCSL4DRgz8WpgMrDxvZVX8iwL8rr_ee0rM-bJEhPljzdRscole-npl2CUYKmvMyT_YV2eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از روزی که رونالدو نتونست مثل قبل بدوه و هتریک کنه، موتور تیم ملی پرتغال از کار افتاد!⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/107309" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107308">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=F5iHJJXbZs2sU8jgsoSMU5P4ZEe0kwgn8ITf8KcHyvBxF7DJpi5cyiEZBFZXoZwJn9MFFQuYuYEs9R_ekAobiFE6PizndbWyvIejjHzRqHjqy8-a2Ulsxp3ZB2FiZ_Y5kq54DL7J6f5g08vFtjBttr1fG4ulCAtvBathfk3bDinC9v6jAZFkooWuZFKskDFHj5vobUVJj0AFctRQenNvZoOnow5yNbDAhRAqoNR-ywASEV629RRHPTVyGxG8XniMsUyJcAQtasQQfjzeE_zVrQ8zOR1XcEVDR6lxEqAA_7F1KbegQzSvsWZfxlOVIiRi7BQW_upk5zJTraDTzmCFlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=F5iHJJXbZs2sU8jgsoSMU5P4ZEe0kwgn8ITf8KcHyvBxF7DJpi5cyiEZBFZXoZwJn9MFFQuYuYEs9R_ekAobiFE6PizndbWyvIejjHzRqHjqy8-a2Ulsxp3ZB2FiZ_Y5kq54DL7J6f5g08vFtjBttr1fG4ulCAtvBathfk3bDinC9v6jAZFkooWuZFKskDFHj5vobUVJj0AFctRQenNvZoOnow5yNbDAhRAqoNR-ywASEV629RRHPTVyGxG8XniMsUyJcAQtasQQfjzeE_zVrQ8zOR1XcEVDR6lxEqAA_7F1KbegQzSvsWZfxlOVIiRi7BQW_upk5zJTraDTzmCFlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ابراهیم‌شکوری دستیار حسین‌عبدی بعد حذف از آسیا، از ژاپن برای خودش آیفون ۱۸ آورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/107308" target="_blank">📅 16:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107307">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275c393efd.mp4?token=o6F9DlsBSN1KPSFO1gH3T4d71ChCEE9QyNCxOrADRW-LNCN3uXNg8dKk1f0YPLO9gvFzpqw_dc462ECyZf5xwpoHp8tCQJaKFzYssp0BIfs9Gur1IpBSGaQy2fH2_Yn3DcTRkzZJExi34AIlOlMLz_aDFtD2H4zbQm7VIGTK3bwfQfH4fE7dxNkYfgvGzyMVxGXDor0O-cF9-TLNZm95fAmfg6r3k3q2buDroBZ1z0zJYRh-RWtbrueE8Ph6I712GokErj-Bkivze_w-q0a1gONn9kCUfsrgsACb5prC5Bj_kf-mvAb_LAr5vpkJmR_wijDS2-2hh42P6TeUaz4rkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275c393efd.mp4?token=o6F9DlsBSN1KPSFO1gH3T4d71ChCEE9QyNCxOrADRW-LNCN3uXNg8dKk1f0YPLO9gvFzpqw_dc462ECyZf5xwpoHp8tCQJaKFzYssp0BIfs9Gur1IpBSGaQy2fH2_Yn3DcTRkzZJExi34AIlOlMLz_aDFtD2H4zbQm7VIGTK3bwfQfH4fE7dxNkYfgvGzyMVxGXDor0O-cF9-TLNZm95fAmfg6r3k3q2buDroBZ1z0zJYRh-RWtbrueE8Ph6I712GokErj-Bkivze_w-q0a1gONn9kCUfsrgsACb5prC5Bj_kf-mvAb_LAr5vpkJmR_wijDS2-2hh42P6TeUaz4rkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❌
آنجلوتی بازهم به رافینیا استراحت نداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107307" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107306">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR60vB_q1Oi8GWRdBeFdA1yvU8raLOKjrUx_Cc-HRmAAcoXdZ96K_g_Rf8UkfU6PL2UuME2PLBN0npCcc9LW1iFmcwjZY9kXVWiIPtenIPC9B5aDKqbqvz9pwz_GiiGQtFGADI6EkK87WZOksYUnmUnSfpoLacmPJHW7ovlYkp3BWYgx7YR1I1-kpmEczDZycCjSmXkVW9GkQCGLoIkeUI1_CvrlC5zvZcov4Hr450AjqSpI9vwAITavTX_0NUeg2jXzHASC0fov5FOdw-4fxqCDBQnMiWWpbNkX7S9c8ttt45X1auiyVJ1k_LhJnZAboh-Ggt1JuFLXJJUmjVPAuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
🇮🇪
چند بازیکن تیم‌ملی ایرلند از بازی مقابل اسرائیل انصراف دادن و گفتن که مقابل این کشور بازی نمیکنن. در صورتی که این اعتصاب گسترده‌تر بشه و ایرلند وارد زمین نشه، اسرائیل برنده بازی معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107306" target="_blank">📅 16:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107305">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=nVYjrJwh-JVke7eeBSDGpQen_AVaiVFvOkcgkTptgBsMQdvt_UPw8uv5IeSn-otxSnu9Yk4xIQpgRGt8L9MEeEcHGX7DKnj3SdbuFCuab4ZLbQmUPC4rH2CNMndlI1vJZGFcR6AVtCAOqpbyVcJOjCwFOz_ZJ4osdFNY51OpB_ZerI30kWOzz74VBQ6sKuP-cMX6x8QvIGDy4YA2lgkva4qW8zJNTNrEcnuaf8glghMnjlKnFlqgk6UmMXKwcVRe8soyokcjPVw8mgd5FoJvjtcJuKpDIaN3etgWxLCVCoguC2a0r6KXohW_BKXm0aIaJBDEkW1fOgR9FTsAOuXiJGCYQZ-jE1TeOkq4K-bKS8RV-i2qSaRff3TQuXZ6FE0lI14MO9SB5M7okTXqsLjmfOVUd3uso7Qaf5uow7wsjytMNZyEdi8xg2AlHIruisfSHkuX-NumImuGr2AUh8s-nmBuuAGKDMrKyBLcxvcOiKYzvI6Fqx1FmPcRFl8--RiEeY0RtcsyC-a12ogvVVubIj8KHggiO8lr7QtX3az4QAmvT4-4V2vVOKsbG0AlH-XbamJuWoqJXaotkt9ekz1ojpXNUk9pJqU4ZxZjVuyusyMNi6JTxFFblQL8nWSiSaCocvzHqfoEj0miDi6dLPzU_39A7NNK1cB6SFMD3MBM8pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/107305" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107304">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc52d28f2d.mp4?token=gskElv-1WtQzq7itsurCtEGDvTjh9WUoojMqxyCEPDgwJaH1Z2PgBOXwDmIz66sCTiQQ-hlF4zMyWRD1kYBL49ET_IIj_c21XXEH_imiaUmdztIB_F1GTu9rfrzkHE2ntKHRKvazPHQPmq_sJrwAKH9y2LiG5I_I-CKcl3pJQBRwZ12xYoCrUiWqZvdYzHRb6Fzp5YyTSmTonO3aKoRungS-4AH5lhs9tkd3ps65Ma7kMSoA5UPzc9R2UF_RnzfapH1BQpTGjK481DAByIX-iDnRkRE9FZht6aTsdwaI2vVO0pVhNrSuStXifGJQSU1-D2wDTGqruzc0uAsQB1Nz-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
حسن پاجانی، قهرمان مسابقات ورزش‌های الکترونیک (بازی efootball) بازی‌های آسیایی ۲۰۲۶ ناگویا: دلیل قهرمان شدنم اینه که یه سال و نیمه ایران نیستم و اینترنت بهتری دارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107304" target="_blank">📅 15:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107303">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b2e1cd171.mp4?token=Pmra6-CfstpqxvG1DQFkFEoZyIv8tKeKDUzoV_F34PSr4FXw5DZY2uYsddXeh7QnaLaikfIYstB8ucwVbGRpzWY4vBxhyS1UkXyVJI0CHLkOwqlaWu1colsW6LaEIRB_z99nLalL_KpWE6PsXevyOSJcgcTDmMLkxkGz5_CNXeWCVBwr1j-pao2b4fipw6PmrF4MngfjDwgRyW1b8EvA30qW5lrRnbSHhYDJuGQB92BFYdG0ILTTG-vvZW98hB75xWQbMRtwPsYdGLFifMr4yok3LIIvSgAPkBZX2kYSX79UPQH0z1XPbkEkpxW3JNSRRYMg6Zwp6Kk28tIUZFRglA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
هانی رامبد: امسال سال‌بسیار سختی بود اما برای آینده تمام تلاشم را برای گرفتن ویزا ورزشکاران ایرانی برای حضور در مسترالمپیا انجام می‌دهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107303" target="_blank">📅 14:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107302">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90efab6fe.mp4?token=WHjT_NmbVz-fCKo6YWdd4Pym5lQD7wOTXYLI8vTvhmyB1DpYr4ihK9A5UJredYkgpT9fzyoranv3batGIEwiLbfKtaHjH2XPk7iVun6Oxlfdi-6UpzBEf1nNRvpMe69cnoFh4zAXJvDZIMOf8EosZREYJ5--KCrHKSgEv3d3mfZfXdvHcmsPnuv0t86dyKgud7f0bHFtBEqyksZDXCJ51fmDr6U9eXQFaNk8v16Mj77EWkUzYxd_VL05wRomCZF0cU1ky3b66dki_mWvjslDqHCS1qId9BfAMAgu5_kaausZiq7aLaIT2lZS_w5Z0hTfg-s4aGdsJv8uI0PqjsGTWDF70e0dLr6pccw7Otq3fA5haopuUWlh65vPhbLNaqwvj9geJ-pZcCgA_ncMrgT4mlwo3dOE7bnRoaMZHzFOfjMFl7klwLIGRWyj47CABaPazL7roe7Rys2wUOjVEVeDS0h3LlRgcSN50FbSZWrPFJ08flNPDetXk-d8mkD-yNe3CIbOfW1wtVc-T7WM16zlklxMhdEOmwUsrwnCAAQSdFJROs_rZGVMla3YcBqilpy7u4dzoCM6ri8YYotu7Q1Vm9jq91OlkrZ1c4HoWmOc07UCm1ggGOwwRPfAVJNq34vzaItpfVErBT7QIhXnFeMYp_O9iH3PFqZyOAAxP7YoAAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
هری کین یا لامین یامال؟ تفاوت فوتبال انگلیس و اسپانیا؟ وضعیت جود بلینگام؟ مقایسه توخل و فلیک؟⁣
✔️
جواب همه سوالات با آنتونی گوردون در مصاحبه پیش از بازی انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107302" target="_blank">📅 14:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107301">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e44add616.mp4?token=gibOLSKfBglfRBPcPs4QqLNfgxY9iMPgg6oDUGq1hhNJgPc_yavv5371NAQwyY2cZu06rQFlUAJaE46341BdyR96yOXNLWkPQIFI2_MNHigoba_dkaF0cLf2SJBaSS0t1QeuBkI_RDTSksudxmTLV1w7UNt955T1009sXLxR4aZiYiPS5cPYxuH4ytMp1VG8vifgyJSh2bJHdbs897ywfgIN1AlXc6WW7Qedw2zm_Ibomo5qh4w9Smyl-deQcrsvwPTCqItbX3rz9Ltm6MdQhWpiHPpsAEGpeizg3smp9-gyPcOepnGOed0ZBjar7yZ3DeWePxQUh5KDwBn-0T31JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بیرانوند سر صحنه پنالتی بازی با ازبکستان به چه چیزی داشت فکر میکرد؟
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107301" target="_blank">📅 14:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107300">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d96c298a1.mp4?token=kcPeswaOXgp6xUh9foAt9I7JOEt9Vmp8IotahWcQSrPt5pFAtk7W8gxldon2Ig2ni7aXaaqgDLAWcC1zijmbLQK-j8YsbOqIGYx_0amCAjkoVZrsGEalfUbTTOM4HimfVOVLz29oEQ1rltq_d1-ioZ8YJlocFIrUo1F6YG6CbmWphQ3mVzpvetzD3hdLoJewFAkflCPGP-ALL6CcNjfcYSeVqQl3MRWN_vf938E_GQ24tjJVcBS0D_Z0iCQHe5xHKVsA-nbMUcefR75sNr3wEae6QjjoAuWhogkUHXgvBbSiit1ghWY1NU5kF2OY-rdUnUnXX0Hswaiywma1BTJujA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
کری خوانی های عجیب هندی‌ها برای ایران؛ لحظات پایانی فینال کبدی مسابقات ناگویا و قهرمانی هند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107300" target="_blank">📅 13:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107299">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0woe22zJH8J78Fh-mt01wktPL9201vXDU_69hHXHMEP_JYuesMEszkWnb2qfCtuEaTNkdW7IlMsqXATeaMZZxUpyo7pVXrC5at0l9wkNyffJfJNZtQKQeGhwLNqmvVR_3EE7jxRTCeZaIdXOCilwsl-6y830eIpANGtjYqPTiIdAm26VGEHw2A92a0Ahy9-IM84y7JQO1BZi3EDCs6-w5ciMbjKvEtQk6uiDpcNfMGyBu4wiyi7gjiciVM4Zp0IEQxIQ3iI04NDDOZM4-B-k0TV8r8f8Y-oMQGYTQY8JWv872NZnUcOmRvaDV9bpy-ne3Xvl90WcpC5HEnIwYQDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
😳
تو حرم مشهد این آقا صد میلیون چک نذر کرد و انداخته تو ضریح واسه شفای زنش؛ حالا بعد یه مدت اومده رفته بالای ضریح میگه زنم مرده تا پولم رو پس ندید پایین نمیام.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107299" target="_blank">📅 13:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107298">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221e00ddf.mp4?token=UuhBzoqR_B9BNqGav-cv42VStsbNmPcyD-Ih4PAPqShIsGVWYsW5dnb044cVJ1moyGIGO0x-4pevW3o9DEepFU80v2yxb47b3dHR4rVExAe97-hQb8M19JZA7creVwUZ91LaNNhfLyFH5AUpi8F4TYVaOcwLr6vAcROkcohNc8wpRHwqAdskN1VybjQfgoRB6CfwbT8nfsitCVvl3VYn-y8fO0Sie_qyNLL3pT0WNB5EX-SmSyrLCcV23oINRcc05DA42dxdVBVS00-H0dSki4y-cJszkMyZe_c9sedtbUr0l_l3XNBtBwNXRyYR3NHft6ZiRJRy3vEDEpT9UmtxNxYmBkHhtCAEa3Wit0LPbZ4_uUme80xahiMUyiYs7ww5R7QxyggIXMXDdEWWXRLWU57_r3V7afqDia6KhKM72SpoyMq3XaZNU-GqIY6ZnhrvKS_TV801Q7vPsKLefZRJokl4wOUB8xKaXJzyarMKiP3ay8F-SqAZzeRbp1yuF5HvHWjN2rvWk66m4N4YM5V0oGCgUen6D_t0eDI26ADpjdud2LGzqCk6XX0w7bTugsIFoej7oQlPcLHvxzgQgNeWFn7LL5riyjdOnoq6AcIid0ZzEwpzwmX66G9EIC1namPvSDPC3M-zsrlS05gF5GIoAtJ5p-xRIQMK6Ed3PWhMBF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیز دربی مادرید: چرا رئال به گل نرسید؟
🧐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107298" target="_blank">📅 13:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107297">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75d0bcba0b.mp4?token=A3l5yp16JnCU6TDGOKBs0R4nd_hI-iaFSDXs6mm2jGcEA_QsjHTOnYV7Df-Drf_xyvceOSWy9y4pBkS1iqNOucX5ZNBPrjxpeUiDeIfqW3MB0LgvjIDv8ZAsEg7DwoMMcnXFcS0-_71KlKO_ZGexngtiNSGw-1AyaoZcOyaFz0JOUXR8VIGbY-Zd4GPWFQpfQ5dtAzThai7LhMLIohvonp_Rpg-ft2Zyy70jvjZy13cehiMXHstF_cdnWlzEwykQOpLR3LjD6zcxszP86k7SFoGmtj_yT8sttA9NDWXzATUnAj1f9T1k7oCcDOA6QI3mIbTxeUBXuL76UdW2oPMKOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
دبیر: تراکتور برای من هیچ فرقی با استقلال و پرسپولیس ندارد
مراسم امضای تفاهم‌نامه همکاری باشگاه تراکتور و فدراسیون کشتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107297" target="_blank">📅 13:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107296">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd-x0bsZXLZ70sZtjn8wAPZLNNCiZRgiaCorme2LfM0AqTTDuvaCkXlvHSvLIyDQkKDv-C6c_WHbxYJuDNkN04F4YqvkAlHLP8vh8S5BgeuL_DiLUeC1z9u72iIGQKlcLgYUYhFFzFstXHygwXPb2r5GYCvYjkhQCSM55AUsg2LyKvkiswvnHKsqZ_vr1p0sTTsrImvNRRC31MlqqxttoUttXcPQZiQ99dBpZjmuQswcAlgGFKdHDQDb4aqxe29Btzi-IW5RR_fPLMzbW27kFeiJCP7oFduzGGX8IXhoUkzbcjV0Vx2pApRqoVpUidbUCc4HdpTEXXZbmO6lNMBlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
👀
همسر سابق سپهر حیدری درباره رامین رضاییان: ایشون بااختلاف چه از نظر فنی چه ازنظر اخلاقی‌بهترین‌بازیکن حال حاضر فوتبال ایرانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107296" target="_blank">📅 13:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107295">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJBUz01LVO8Q9kuFB7U74LKgO21HhQC5oynMOUgojdUnypOy8cK8EiDj1aJfUuxWs9FFPujRZOrnvOe0YTwt_vt6cU1B-t8oyuTgm2oSj4anSE3gMIRP91kktSImKb8BtVQELesLpNE1yxFKAzJl3j_Gj1QlhpK3B0qdHgC9R5xpEA-w50kboEqbqMD9CcbqUgO6L3isvd-fPcAHWYfEE3OQjXz-x0KFjneUxQfA_daINn8g3pUVIUITBuzjA13fo6FUAFTJ6_EdB_UTXvuU_Nb2JMIO8rD-mSBxcJU7ICTn38w_Ai2KdMDx3uudjdtMU474ERVB9CnQjqL_2svXVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگر قهرمانی‌های‌سیتی گرفته بشه نتیجش میشه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/107295" target="_blank">📅 13:07 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107294">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107294" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107294" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107293">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZo_hgBxoD2_quLX9o2zRGMHRLOFUertLAxyHeIVpomnqcxNulgse4HgbavfzzcoDplCsbKnQn1-mIAKsEznRvmZvVw4obzHPM0vjuA3QBdeoA6kh0-fkHjliLdlmsCYzXv4KJY7hyRS4T8azoTYKA1qE96uKftkYphWcV2skkRzY9wmuGyOp8FSuIT--ruzSDt7m-x_mINm4DovJLLhaCXTiHBl8pJIYDYH2pHFNJ4fAAUAGTlTmwOjISiLd67_X5oUjk1rmMh1t9BO8TfHLlRCgqlcoZZ3GtLVeWiINorHOYLTE6JtiCbP9HGMyZKhConba5tmJunHEUCL0oZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107293" target="_blank">📅 13:06 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107292">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fa254372b.mp4?token=olwWVNX50upcFlkBjGYV1fYRuG8N2l3cu87bRqBepE2khqdpFu1ky53nP2ZZya4RfZrYxlaLwptmnL7LHc8iZwgEs3HtBj5FX3FwetoPZbcU0lgDORTtuM4jX2qG_-NLRXvkyyD6E6aixrcUiuGBw-_a8lOz56IKZ8G8wN6LjMHBvGaBqucG46qz4JHpSQnEKsZbjTXDqzPY0F19B5WXxI3LHzef4Z3j7zcG9vZr5MJeCNKZw2J2R56VF20Dwuij9LEiMmX5Wkfe3h1B_d1P3tA_CdxmWFqxL0_SbQZDRKcN2ktMq0zpuQ2VwN8vcIUjtV7gdNN4s7amE0B21CljrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
👀
بهزاد داداش‌زاده بازهم یک ادعای جنجالی داشته و گفته که مجید جلالی جادوگر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107292" target="_blank">📅 12:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107291">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=RIsdBalpPWFkFRQinAzbA0LpfIcL57i4zb5VDEoacPpIlKqVaK_-pRQ4sJElC13iVRFPCV6Gd8mgHxYiU2xtUkUV160J3bYI7eczmWGmfC_uy1rO0Lrxrg2hxY0pczH_r213HtQXeQePB2Yt4H9pcfsPVp1yFevzsjvmcNnnEeycARCaLLIByCj5Y8N2h0C3nFlNSZ_vfi5NsKWi-X9dXuDIt9msURICOtDWRHPDZrR3I7hpB5n-vURwLR-fE6taBxLZJLiJznae4kC_ZRAJ_AUPwGKAJYnMhTm6NQ9DD6sPxlKMbKe7UO_p54YEhEX1tlh3XGcWTLVRlipFHgh6bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbf4bbaac4.mp4?token=RIsdBalpPWFkFRQinAzbA0LpfIcL57i4zb5VDEoacPpIlKqVaK_-pRQ4sJElC13iVRFPCV6Gd8mgHxYiU2xtUkUV160J3bYI7eczmWGmfC_uy1rO0Lrxrg2hxY0pczH_r213HtQXeQePB2Yt4H9pcfsPVp1yFevzsjvmcNnnEeycARCaLLIByCj5Y8N2h0C3nFlNSZ_vfi5NsKWi-X9dXuDIt9msURICOtDWRHPDZrR3I7hpB5n-vURwLR-fE6taBxLZJLiJznae4kC_ZRAJ_AUPwGKAJYnMhTm6NQ9DD6sPxlKMbKe7UO_p54YEhEX1tlh3XGcWTLVRlipFHgh6bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
💥
گوشه‌ای از نمایش‌جذاب هلند زیر نظر ژاوی در اولین مسابقه رسمی مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107291" target="_blank">📅 12:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107290">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b671734a24.mp4?token=EGdjExZBX4mIThLdLpImX-iBCeHllc2ec9RULskratgNqwKRh3_mmLEiTpsxYEYEH5rnGed2znz3ody1FN-xXHvV-4Vm2ZR6r2wXwyAJD-m6_RdyxkknSBQNHCKFsDPm-cXhvYVO7a9QIYeYn0upWNh3YMH1mYfOCwmE3rl8pEHJ7IhWRkWgaTpkMBuiVJYbN-UKZ_vZXC9Kv5YSTjpidPthLpt0OStrgiQCqqE5ofm033HSJvvbHxddVsjd02IzHZ4wq_nWIrTx_ZSbNjLjgGvnIDLIjqAivNk79uSFbiDM1DKK8g_vVCSrjal8vbiN5O55Lz-vJQ1to3gvf4IV5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b671734a24.mp4?token=EGdjExZBX4mIThLdLpImX-iBCeHllc2ec9RULskratgNqwKRh3_mmLEiTpsxYEYEH5rnGed2znz3ody1FN-xXHvV-4Vm2ZR6r2wXwyAJD-m6_RdyxkknSBQNHCKFsDPm-cXhvYVO7a9QIYeYn0upWNh3YMH1mYfOCwmE3rl8pEHJ7IhWRkWgaTpkMBuiVJYbN-UKZ_vZXC9Kv5YSTjpidPthLpt0OStrgiQCqqE5ofm033HSJvvbHxddVsjd02IzHZ4wq_nWIrTx_ZSbNjLjgGvnIDLIjqAivNk79uSFbiDM1DKK8g_vVCSrjal8vbiN5O55Lz-vJQ1to3gvf4IV5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت ریدمان کریم‌آدیمی در بازی مقابل هلند که حسابی اعصاب کلوپ بهم ریخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107290" target="_blank">📅 11:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107289">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
❌
⭕️
#اختصاصی_فوتبال‌180
🔹
با تصمیم اعضای فدراسیون فوتبال، حسین‌عبدی پس از رقم زدن فاجعه در ناگویا، طی روزهای آینده از هدایت تیم‌ملی امید برکنار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/107289" target="_blank">📅 11:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107288">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=UUBAKbRxsX0Yj1IsTutlqA4PbdWvO79LkwFQPJnXnvlOk9Clsxv6hk8BOr2N29ySksdftv4FQwHQOZ2_IzalW9lQxvJbl5QDMOL8cocbBxx_x7xBopp7yEaYgzx76GRu3wTfXS28w1CsDIyR71_Sf0S0cO0yyvA1Ojr9a10DNYAzO-fFK2PiG0Qfl-kp-Ci5QFub9sfMxljytldAegUuDxcN_Z6o4AAlhcC3hRRL8FCTtDmpUT3uxO4JGi5GzNx-DoWEs2xjntZ5a65iAmMsWIqi_4HJQ8t1zSMbO2bQPaGkw7szR4PpAiYBTjqSgwPkT5T8nwrIy0nQiwMPvzx5yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dcbb333fe.mp4?token=UUBAKbRxsX0Yj1IsTutlqA4PbdWvO79LkwFQPJnXnvlOk9Clsxv6hk8BOr2N29ySksdftv4FQwHQOZ2_IzalW9lQxvJbl5QDMOL8cocbBxx_x7xBopp7yEaYgzx76GRu3wTfXS28w1CsDIyR71_Sf0S0cO0yyvA1Ojr9a10DNYAzO-fFK2PiG0Qfl-kp-Ci5QFub9sfMxljytldAegUuDxcN_Z6o4AAlhcC3hRRL8FCTtDmpUT3uxO4JGi5GzNx-DoWEs2xjntZ5a65iAmMsWIqi_4HJQ8t1zSMbO2bQPaGkw7szR4PpAiYBTjqSgwPkT5T8nwrIy0nQiwMPvzx5yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
کنایه حسین‌گودرزی بازیکن استقلال به ماجرای سربازی نرفتن علیرضا بیرانوند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107288" target="_blank">📅 11:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107287">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=KD6J2RYW3B_J-kE40cmdiadBPgO3vPpNL9hO2gFj0516lAodiPQ9bYD48PM0rSii2vQ3fCCC82PYQgpfoWpZNzyoEDtSbA5Mt9_u-car4uYYHqvCUvljNgutCKkfq_GDNC1hYWg0TAXzGej8ZSOZeQM0GklJlf6pswA4j25nXnrdyyj07awBIpMxQX9yNWZR275CliPC1WLOtz10Fxs_1tvFY-Hhf48fs0vGar-PkVznXJZ2UVBlAm9Mvc67jgOou7QMpg-wnnWkNA3eSYh5oJ30AoV9baFTD1bEK4Xle9DhfehZkRNObg9H50_bb37emu3-aLn-t1vS1fva8vVL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06c8b89d1e.mp4?token=KD6J2RYW3B_J-kE40cmdiadBPgO3vPpNL9hO2gFj0516lAodiPQ9bYD48PM0rSii2vQ3fCCC82PYQgpfoWpZNzyoEDtSbA5Mt9_u-car4uYYHqvCUvljNgutCKkfq_GDNC1hYWg0TAXzGej8ZSOZeQM0GklJlf6pswA4j25nXnrdyyj07awBIpMxQX9yNWZR275CliPC1WLOtz10Fxs_1tvFY-Hhf48fs0vGar-PkVznXJZ2UVBlAm9Mvc67jgOou7QMpg-wnnWkNA3eSYh5oJ30AoV9baFTD1bEK4Xle9DhfehZkRNObg9H50_bb37emu3-aLn-t1vS1fva8vVL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
تعجب کریستیانو از تاریخ تولد هم‌تیمییش در تیم ملی پرتغال
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107287" target="_blank">📅 11:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107286">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd536968a.mp4?token=OYziJtLtHdnNfJ8sFSKQo4KyVopnKB6dtaVhicZCi9cIdUcLebVFtS9jDf1NdMtEuM8ZNQ3aV7os5d5kxorl3PWUPQkdj4eapssZDcgY4OA3XB9JKUshXs2H81W_VV3wveEjAsg_b2Jfree_RIX592ZCPKOCUGOv91LGiw_oy6e0qfIK5yK_eM9Qa7AExQQCG6JG1kMTSgeqzE66oZxKyixReguYKYO2Vr_HZdSnkhUY3iyvS1wIDqziESsy_zKXMiApZ-roJqWwZA_8Pye38I0mXTx6A47FmnvHQjIpZeoEq6WKwxBTJHMbTpxRsTqbomOCi-QeCOresoh8WkDyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
محمدصلاح رفته تو کوه‌های ترابوزان رو یه سنگ نشسته و حالا شهردار اون منطقه اومده سنگ مورد نظر رو جاذبه گردشگری کرده‌ تا مردم از نشیمنگاه صلاح دیدن کنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107286" target="_blank">📅 10:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107285">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c6cfb864.mp4?token=RFnVpdsMHcz4qQr2zqlVMTrtQ8d8x_Zw7UtuY63PA32oGis6YVFqB9lY52YWoq5pJllYTWWZByuU9E_T1YxV2ZWBLvcb0UnHLrPxSYB1oUnt3FYp5ymZRpvFLhWV2jMZUFkauJM7555myV_uds96pBrSv9ZnQh_DIg8q2Gqj6Nd95Wv6Hj4bDKVtkUEfz-y-wM74l_0EYrPR9H_n0n-D-5-wd510MXjmOlXfCeakH4IeE6KwCXiCTIcuqV7kwUzsSdTxjbV8ldZcSZW1OA7IFJ594UJgRkXGCE_vR1iL2BjCP0Ukmn9dUd6qzN6q4MzWrpdh2FeUGO2DB667us8KsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
کنایه گودرزی به ابوالفضل‌جلالی مدافع فعلی پرسپولیس: زمان مشخص میکنه کی استقلالیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107285" target="_blank">📅 10:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107284">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4908c84c8.mp4?token=NDkL9XIgqBOLs9MtWdyzDtaKtULjRI-e5L83fXxkC9VqsIIlbB4C8857ECS-0aa4A4haTnO9eERKd3XquIwhRyDJ5IdAJXPABu2UPgFag_tOyts5rt8Jaz6B2o0eEDgLqOabI7QFL1MRQcR-0qRoM0-qXMydm3JERoAgTaDjvrIXpLp5Om23N_cHpdH09wyeqRTgVhU49-ngYYhHbsiYCwXS5bquT1UUFLpXumkGP5LbQdHXjzt0OIRcL7-fAbSsta-n5fJFOUjn_7MMuYLxN78_fur_KXX8S8bVjnmj5Tko84d_VgHRx_yRMENi-s5VWGfCoRF9j0S0JuMYvIJo1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇸
وضعیت روحی مورینیو، هم اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107284" target="_blank">📅 09:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107283">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02c187832.mp4?token=i62g5bYnBbWUDEriKLRjzDKEmlvUmA5UH_7T43mmGOPjnaYgvGPMImQ6vM1McIRq2TiXOVa0ZRA3zz3yZAMfmwLKOwV2a-8wFjU1vemA2oiO0t3G4NKMUcJu2rIqW_spMx6T9gK4aqTXiH6g7nMFnZIIDLgVGjF2FebWO8j3VR7fTVqXAXct3Rx7QxBBACTU0u0s09KZK9rdz-apQJqNOFYhOz_xVzdtJEps3zfXKmEBn4nyAYcmrORlT38UICvtnOuOtZvg8uZSPXfXj9ldulQVOp6QB2Q08wk17GsId8wGxTsM287cTPZ5aX3Fe4ic9SYnDR4uhOYd8vxyEl5OYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
🇮🇷
کنایه توتونچی به ابوالفضل جلالی: یادش رفته بود، که گفته استقلالیه!
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107283" target="_blank">📅 09:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107282">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGf-xqvpSMbbhqNZWR1yRLi9s-cMed6nko_thHteXW0XcAqejsNQqzs_9lU0V24yihQ7VG37lwAKBUdI_Wa80HP4MK3YSvlNQaGK-Lpyhi2VAZCyyNY_ieti032LANrVO11uJleiwQ9VZU_GKrVOnhhDUbhjAXQxXJFnWMKuRw6yhcOqRwmaILwKww58vkRB-828Pnyw_SyGrjAcyjE2SDrSKWoskvN1XGZ1rlmjlLP4l53as20gr_YGg245uX-YZFJ_kRlvi_YOdGILrPZMyby5Dp0jYVSWwQeUbKtHH9wvhW6xegNFZjLSE57D67KNV9YPdiHH4xPl1JXsx5EJjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚑
🇪🇸
آخرین آپدیت از بیمارستان شلوغ رئال که کیلیان امباپه هم به این لیست اضافه شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107282" target="_blank">📅 09:03 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107281">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEnJThVaxbOkDPDNl_8lPFXnxUjrrOhtOlotfZnZ4ao9AmHNN1gADi-Xliqjcz1D4ESM9JNf9aZPhdeuEVEw2IpRYo5jmo0fIazJR3k3-_VKkFtPFBtsXlRBH9ADje7SbrzeWWQbWLCZ5t3Ui4i9jKlAcknLGMF4oOWJNuQ6gh-UIU3Jlp7NgHrshJgu_UrVZS7Wx3bvI4vyQAKvLs-Q0XG5oBCGURMMAvHrNv-XN_AI1vHDBbiApnqJrjqyuzS6SLnTa4le-eGISrsD_xaAHjX82GAMiOYEjXSdCcLrWHPFWSRMaSr4zCJUXU_HgWdirryoT7UoL-xU9d3fvLe18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥈
تیم‌ملی کبدی بانوان ایران با شکست مقابل هند به نایب‌قهرمانی مسابقات ناگویا دست یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107281" target="_blank">📅 08:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107280">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=GQuHLJjbQiLozuAyUji57mWJENcCS84SDSL6bPIqO33976po5hX3CjKSE9rxYXo8glRAJ-gDKH0nXVrScxYdCMGmhgMjvca-yVOlV76cfUCMs0DL6v17tdbFCWdEtqu7a5vcM6wh4i9f2G1kmC4C5x_OUwPz8HgnRJccQiavZJyTRzsG3oXnSu2HmnjeP5MHCwFtiXWsJ6ms2suFvcjvkoxsEah2t3y2Vq7u28jiVi2DAHgUtdMqYgk1qi1cT1juIR5nod_mG0NOdtJJIT1mWu0a0v83s2onIWLLmvtDo-455XvIRamHcqAOO6y5yxzmZIbAPtb3QNOxrioWD4Xb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d41de8e91.mp4?token=GQuHLJjbQiLozuAyUji57mWJENcCS84SDSL6bPIqO33976po5hX3CjKSE9rxYXo8glRAJ-gDKH0nXVrScxYdCMGmhgMjvca-yVOlV76cfUCMs0DL6v17tdbFCWdEtqu7a5vcM6wh4i9f2G1kmC4C5x_OUwPz8HgnRJccQiavZJyTRzsG3oXnSu2HmnjeP5MHCwFtiXWsJ6ms2suFvcjvkoxsEah2t3y2Vq7u28jiVi2DAHgUtdMqYgk1qi1cT1juIR5nod_mG0NOdtJJIT1mWu0a0v83s2onIWLLmvtDo-455XvIRamHcqAOO6y5yxzmZIbAPtb3QNOxrioWD4Xb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
وضعیت دیشب امباپه که شرایط نهایی این بازیکن تا ساعاتی‌دیگه مشخص میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107280" target="_blank">📅 08:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107279">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107279" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107279" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107278">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvIP3aT1E0QarzO9XZZqIYvHywEoo17N59Ot7Z69xa7tjpukpdmGvz94RJiGEjOHurI1ckqi4pG6oZbev6SaM9ms7xbwPpt3B298hRwfFYWYCURJMcXcVjd02FWCCK2ixrlk7zfSNPRbGeMfF5lqG1Ig1V1AF4d2PZuP33KlfTuGMla49YNQTpswh3iZyThJFbhUvlnOpA2DF3NHlx5552VFw57zzdbwYtbLFzLVZdh00H9lkagIJ0Q4Z_-aIRb9tdBhHdrEVqU9MlfGm2fe8Ptfxzacp8SfXYpKEv1yJdpKShAyqtw6r4h7BIbWG_I3l10hNNYRfDZtsQ1WIU9Xdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107278" target="_blank">📅 01:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107277">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfo2YaF_d-5bAeHuUHZxHb5xDHDkE3it8DNxNWdVCEJ8fJEiIyRTmoe7ypFMWK8gGHap6SyMpnCdUCaxwphVudXqRKmgfcZve0P7fUleLLzE4p1ZnMaKoWPWXCmPfAc7K-eKE9whxyRAN51CMC9yxTHQt-EbBteHDSEmGczgHeu_UNOhWqKSMvQh4ImgGgfJh2OPtb_N-PFyIlVwGOpjPfOoDnT8sCj2VhaUAUtCnj-YQ9LhAJQCRpDhensTUx1dJM06qiPpeVUx9il06wsMJQX4BacqxcYS3VRHDf2ZkuoGqZ578UXVAshzA3BY6SkKJBM9MPI5KYgZ5xNG-gL_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
©️
با اعلام سرمربی تیم‌ملی آرژانتین، کوتی رومرو کاپیتان اول تیم‌ملی آرژانتین پس از خداحافظی لیونل‌مسی افسانه‌ای شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107277" target="_blank">📅 01:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107276">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkXB5jWpxmOfXTho4MrvGhnrxU7kFmQXbBM-kOBnlWpBM6MliZS7Oh_rFOo-_qwsxsOV3rKcQ0ezYwvflKeAKnG0kPYysj6Hz8hvw6dw3vX2k3LaQnLUrssD491o2qTPagsbxbgIEI_bzuT2IHiz7v7_IWrPuyvd4bMdCdX-JMNGwRGcSojCbLMxiLvrY4Nvcf-rPA2bxEKaQ_XR8JHyja9F07_Ijw1cN8Zhz6eQmVapbRJdbrO6-XX6C_eSfe-9mTOrwnpC1lt72MDdTQrnsYmgpZKwCdcBMCUNtRB8ISk90M4vFP958rxn7h7zj-gJiLhi3wJTbAkBw5Vusmpe2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107276" target="_blank">📅 01:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107275">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9kx-GOS-qjS5KQ8O_Ab-8PDt5MxRJ11gtPKI8-_FRKAnAaAQS02QQK7bpwsDuwqhqrpjj4lHrJKnPqf3CH4UbhAvkyod-1e4DHKyARwmNjAJx1hOGPhOVT4NBTvGRYqOZLT-tvocIyESFoTQtma6LgQIvUy964jWcbzgHlH3wr_Iez165rdu30wDfWph7iRPDeWo5le0QcRQlG7eYYHTWff4hig9raL1d32HAeHpCgMcixyqd8bzslPe4YEHUOrRFa5hGuq0crtzzyvk4h3gSnjv-yX5jCrO0lv1tnI8jC06Mb1jGIo_te_sTCftmHwmStr6gxeX93P2Q40qHJYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
رومانو: امباپه بدلیل مصدومیت زانو از اردوی تیم‌ملی فرانسه جدا میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107275" target="_blank">📅 01:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107274">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcF-SXIRt72KGiXP7Vw9RB3x7A4HAuywURx54B7fQlZaAjI6GBioCuw_PIo_DS8WFfkm3WbtdDjhv64ihods4Ty6-HPN9Rb9D_yFGTUGcL6B5SaTVdszU51TlBgGuCbNFnJMdjEMEKaHGaSpwezRo6zE7N_mvG8yUM9ERxzwC6ceyhu0DE132pTMVG_Fk3x1ZgRrbAPgFYx-ZccTDdJSGsY_yJUsRBvpJJOWCiOESGdsuMCF8Rppmv2QdsB8ezL5HarJmcDzJ3J0PUQ71NZCzjQF-rs3nCzf3GS8YVWj31107Kp6EuXKGlOHQ_92B2xy-5ws1hagJeEeTkBXJbFeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
• امباپه به 107 بازی ملی رسید و رکوردی را که قبلاً باتریک ویرا ثبت کرده بود، شکست.
• او هشتمین بازیکنی در تاریخ تیم ملی فرانسه است که بیشترین تعداد بازی را در این تیم داشته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107274" target="_blank">📅 00:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107273">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdlAXmAfLMlEYgRFgZ0FeA4h41b90kw7Qb3kQaUXGRhV-eq2yu7FF7Cj9tgY9mjcajMFp4t4qbNCSmuryUBrnu2kC1nI17hF1_IIgEBqbW6PcVxOGsUWzv_vphTnw9db4HUXZ88EZp3MJTU1sJVu1oAPO18TLf286f2oSOrRFoQcG3NarAzysaaCH-UWdeKQFTfYPALrWfzrv-RhxLMorCMg9xyEgVcr3oWRukjXMjDUbKl7IysE_7EGWjXB81cnLuul2aWp3PfILkDCPri9yUtabaq--m6kQadU_T4FplnzKJ-1JEYHwsnxtDU0z6cexoi0J-ZkBThqMmoZ2yIVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107273" target="_blank">📅 00:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107272">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWAOGM4cKCN2omM6T4KKiola1lHdxLNmk-GciK-8ji-33-bf5shqGGjc2d67QN6hVRUa-gcGFLpDO1gTWm44-paru5M4qcs03PAgwh7Cd6pAF_HKrVEIE5mB2eCs0SoKhSEArV8CdLBFy0IOVrKGa5BzGKk0I9xIN3Ex75yyojX7arr3Xb8bF9loyRSG2ctfm-LzSGa66bE-DZSEo8zzWt3s6DegIA0rFTJnmnFr6LGrPFsyD6rcH1JQdP579d0IKfGV_m64x1vpmR4Aihi2UMDrKOeDXtCfUHOGTrBR3lh_SVDatR-ORbibzjjN7OLRkV3_B-_2p259dM93wdtnYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107272" target="_blank">📅 00:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107271">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=gDBP_vPtDxYKPXBHiPnrqK3m7CFWwfGKmGb_cbnOfpYWG1ZgydHlixsuwXdQIOrKmvjRd-0rhHY9Q60405R2IBrH-m1FHsHFmRPV7Kcx0O-gWsTwTQXTu5jge_JEyHYDJr5RuYyLewM5JE42dTAn1YVErI8FbmJeE-MKb6m5Xg3C2zZR1l6MtRFXYSpmXQfpkCrbPzWupcAhhD1FELJuMw7ueaUph8PPOFg7WJAMmCFD8gQm1AjbuLk8atJrImM3O98s-YOddvdlulQIyT5UASN3u5whn5AFRUGTH6MMKxDFKKRONdso1wICjanvDuClomf68dAzb9T97N0pEEq3Lg-72BB_KDNMGNvhIHWaWi7LhD9ASBv1IWWmAwkzDEcYbsovTjVjagndY5jjRo6Tx2MYC7vtDgjHn0cMkrUddQs3GS6l8nJuRFcBZAfKcUKl2IR-KgrJp1zTVPFaEyPsMWhmTlMeYc7Hf9CoXXxHZuU9SnFCPOmhlHHb-P_vRCaf-sAPQNU7T7JMTeuPr-Kg3IqMPYl4qsQzm97Yz9StEgU90aRFRlB2mFTQce711atAFxyzUdYByVEuY7sBinqsXFm7vnbCO7mWA7l1FbNYd_E_MRKQzt457U8P0BAfB0KSUbQFnViYGm1IXgkkHNWbgrcA3zthI8ky2d0KR6eu7fU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d6892ba52e.mp4?token=gDBP_vPtDxYKPXBHiPnrqK3m7CFWwfGKmGb_cbnOfpYWG1ZgydHlixsuwXdQIOrKmvjRd-0rhHY9Q60405R2IBrH-m1FHsHFmRPV7Kcx0O-gWsTwTQXTu5jge_JEyHYDJr5RuYyLewM5JE42dTAn1YVErI8FbmJeE-MKb6m5Xg3C2zZR1l6MtRFXYSpmXQfpkCrbPzWupcAhhD1FELJuMw7ueaUph8PPOFg7WJAMmCFD8gQm1AjbuLk8atJrImM3O98s-YOddvdlulQIyT5UASN3u5whn5AFRUGTH6MMKxDFKKRONdso1wICjanvDuClomf68dAzb9T97N0pEEq3Lg-72BB_KDNMGNvhIHWaWi7LhD9ASBv1IWWmAwkzDEcYbsovTjVjagndY5jjRo6Tx2MYC7vtDgjHn0cMkrUddQs3GS6l8nJuRFcBZAfKcUKl2IR-KgrJp1zTVPFaEyPsMWhmTlMeYc7Hf9CoXXxHZuU9SnFCPOmhlHHb-P_vRCaf-sAPQNU7T7JMTeuPr-Kg3IqMPYl4qsQzm97Yz9StEgU90aRFRlB2mFTQce711atAFxyzUdYByVEuY7sBinqsXFm7vnbCO7mWA7l1FbNYd_E_MRKQzt457U8P0BAfB0KSUbQFnViYGm1IXgkkHNWbgrcA3zthI8ky2d0KR6eu7fU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
گل‌دوم بلژیک به ایتالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107271" target="_blank">📅 00:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107270">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yYGUvsinEnTbv5nCkUDYQdo_wB_OM8p33JGq3IRnf2rQmi98BL07vZpa-Wt6rMHA7ZQ6iXwDN5sdvJetQa68m2u5mRT-FlBLILY1i0dNVuknsYUhzaQ_yOBQUeKYAs-KJwKKdPWmdh8Yi9eINXeOzIHyneWZ1iqjCdSNxnNxJwPMiHXhW4cvpLPpEWBeL4sSwxVG6UnKBo0C8-lyeOnlNu-M9dsYNak_oIAYs7bat5dC9uwslkDzLXdEX2Xa6PjWk1C2wNJ0ts_K1Znvk4pBV1XNLXj1fIYfNFrhhFH3dnUJ6H6PsMwhc3_e_TDuDdm35y1iXAtegQBwmtYwkS13zJA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fcef0287f9.mp4?token=IOtG0BAdQbjpwkRE9XckNpR5-f-or2GL-T88hApyEU-iGj24w_G08TD5fgvvE8yBaXzGvGC1UnzW5125Pt-4cvpQf9yQGIXI0swO0B9ZaxgRpy6uFAq-I4ld9Lu1oOuGI0qe3H9YhT67onLNkeXBTHpIGAH25mI59GjmZmFYh00r06Be0I8Dp3UAy6MBJeyU0riDSi0fkjgDlSRyO4qDuKBGZcFKmjNK_TOW2t8yF2N_7qx5nLPiz3prQdyZ7XOkqP0y-f2qHIU60s5Mo8cAH0LZ_79xjnatlIeiuEaQMuvyMqp9V4tWTYuzWLSniIqE9FkR43HrNIMq_TD7flM7yYGUvsinEnTbv5nCkUDYQdo_wB_OM8p33JGq3IRnf2rQmi98BL07vZpa-Wt6rMHA7ZQ6iXwDN5sdvJetQa68m2u5mRT-FlBLILY1i0dNVuknsYUhzaQ_yOBQUeKYAs-KJwKKdPWmdh8Yi9eINXeOzIHyneWZ1iqjCdSNxnNxJwPMiHXhW4cvpLPpEWBeL4sSwxVG6UnKBo0C8-lyeOnlNu-M9dsYNak_oIAYs7bat5dC9uwslkDzLXdEX2Xa6PjWk1C2wNJ0ts_K1Znvk4pBV1XNLXj1fIYfNFrhhFH3dnUJ6H6PsMwhc3_e_TDuDdm35y1iXAtegQBwmtYwkS13zJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل‌اول فرانسه به ترکیه توسط کیلیان‌امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107270" target="_blank">📅 23:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107269">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107269" target="_blank">📅 22:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107268">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=CT_Ce2yZzce5tDRv06ds7sg-eVN0V7zZlgniXU_A4gA7lKEicAACE14jBjNljU3cwQt5p0qTGgCzTOw2iv1mp7bhuxMRe_Qc9xTpEuQE1umFBzNJxha_KgibtSTJc5MhEGRx38yTbqaCPDh231tLrH5G96slbT4YouQAIbN7KGOcoV6vim90Yox8pEESewavy7OaUHmi9nvc20uiNHYpjex5LIpne06uCBI5pP83i6XtVRdXGmdrydYh-4Rz7tF1l3p2FQT5kgSBOH1hfJGhOtIuE_3bfA3uMIDl-7JDd4fw_13bRh_0kZsYnTs9kUdsPwMTLfbXCN_KjRNdD0vIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a64700b02a.mp4?token=CT_Ce2yZzce5tDRv06ds7sg-eVN0V7zZlgniXU_A4gA7lKEicAACE14jBjNljU3cwQt5p0qTGgCzTOw2iv1mp7bhuxMRe_Qc9xTpEuQE1umFBzNJxha_KgibtSTJc5MhEGRx38yTbqaCPDh231tLrH5G96slbT4YouQAIbN7KGOcoV6vim90Yox8pEESewavy7OaUHmi9nvc20uiNHYpjex5LIpne06uCBI5pP83i6XtVRdXGmdrydYh-4Rz7tF1l3p2FQT5kgSBOH1hfJGhOtIuE_3bfA3uMIDl-7JDd4fw_13bRh_0kZsYnTs9kUdsPwMTLfbXCN_KjRNdD0vIATzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بلژیک به ایتالیا توسط میکا گودتس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107268" target="_blank">📅 22:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107267">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ایتالیا یکی از بلژیک خورد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107267" target="_blank">📅 22:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107266">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYTT-fgruvr3J3D9VX9tAgXpmyqZz1w1kRdldHNRDyj0sD3YaITVrnhkHaxxvn9GlPsqQfL6FdVP1Rf1vZ7ijWvj-qTae9lwPq66atrLqjz0e3xXDNwkrb2kaXhyiCDTvgWZUYZLyDdsA6hi4fgFH0TD2OBl8KlTSodq2zB_ZDpZWMVNzUBRF3ynbtjhoRvhieZilyYS0jCv7HwH1xPgu4mIMy0pcHJQGaF9mVw3WwoTwOzzXPYrciWDXk1EYs3ny4YteMHK_tPDHherqQTeO6L2yefBJ87ZpCnfG4zr7Z1JSeUR7Amf31KQTm93HnYkPYUuXz5To9yNtcnq4suF5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107266" target="_blank">📅 21:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107265">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKLEWmBLmvJ2s2LwetNRYPTYS7UdmZeKMGMexPTi2le427OJawbDLGDYJJhC25woRb-8hQkKcBEyyXTaUFEkxwyLVJYwi5QlBjamWBLUp43VGWEMJpoBhuPepODfMTHDSMw1JuHyx8jGk_G6iocCwq2UXK1pVRv5KDftpup_C5_a_eco55Rnz3WTzrtxD8xSbrSSFa0SkvtLc0WhAb7EX73owOLtreXIa1GGwiEQdx-oqi2Q8F01vx1WFkr6jRnwo-moNsD7JWfjkZZATZpS2zth-lBRgybU8iZfcBdvOWaEx-svvb_2NOHqg8xUkJyy9yk9a1DaLPU0my-GX7cdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب ایتالیا و بلژیک | لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107265" target="_blank">📅 21:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107264">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgKQvWNkVCJADHI_VAsPvDz_VAMXx5xb_4v4LuDSc9RSKeeuleoWOnrfa3cb1t5S7-KX2auDAqgb78kYbGzYJXKMgjwfKpeFPq9T_hfRU9k8g-xawdk1GzPUZMRkA1JalQ3qeXaagGXoNtgciA9wMJu28Hu73BmasKMZZHhnp4HExagdL-Bz4NiVWJPnS-o-zQN0XKwV3lBlTh9AuRNXUJ_-yOoC8uKBkzeRsaG5wF07CYNUkO9kklENzHfodml9oysUsceXoX5Bt46Wvh9wAyADt6X4XOhUx0qcWEZ4Lgcn3oh2rRUZZjGNv9LfOXsOd6oA91NpOUXADZq7PUnV6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب فرانسه و ترکیه؛ لیگ ملت‌های اروپا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107264" target="_blank">📅 21:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107263">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=fsKjqh81gHIvA6piBj8n5Rx3_2u6o2mb6A4unvDSEOje0-He6Efv5Jdoc2YXDUSRSuG_yjQItwE89Ydi-5VjUOHmZGeMr_RpfAndOGmKl4GCdYzOH-a1CEZaxnHqtlEwL44R5Wp63QixDQ91dFmwG5i0_4UNMOK96JAldbUoHJBSNDuI9-2b50VRdarJkMz46j_6kuyfQDp5JmXl_2NAFOCiO78bnVT4OIBx1O0myooy-lx0S-6M1D2R5MQrxN6dciafNh_spVtFMiUhywaSEIbuMJlWmBiXEZ9RhhvyMTKMQkpTo3wjqz7_xC50lTkc8RkIA_jJ3XhMq1cdXgOqjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=fsKjqh81gHIvA6piBj8n5Rx3_2u6o2mb6A4unvDSEOje0-He6Efv5Jdoc2YXDUSRSuG_yjQItwE89Ydi-5VjUOHmZGeMr_RpfAndOGmKl4GCdYzOH-a1CEZaxnHqtlEwL44R5Wp63QixDQ91dFmwG5i0_4UNMOK96JAldbUoHJBSNDuI9-2b50VRdarJkMz46j_6kuyfQDp5JmXl_2NAFOCiO78bnVT4OIBx1O0myooy-lx0S-6M1D2R5MQrxN6dciafNh_spVtFMiUhywaSEIbuMJlWmBiXEZ9RhhvyMTKMQkpTo3wjqz7_xC50lTkc8RkIA_jJ3XhMq1cdXgOqjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقلید صدای جالب یاسر آسانی توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107263" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107262">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔺
✅
🇬🇷
روایت شنیدنی نوید استادرحیمی از تیم‌رویایی یونان که در سال ۲۰۰۴ قهرمان یورو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107262" target="_blank">📅 20:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107261">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=uQD5l2xtbtxKplmKwcOwLvmDTy9BUx4X19ltVdzB6rl0XQoRxKfvC7hnbVogDQW7xT8i5U06TPIxnoJ4OC9A5telB7cEQpk9uDFoRbOcHxwwYAXMvDIFGh0GWJkps7fV51VNW20elrCsJHFwG-a4qrk45rX9kYyZQHGznrD_Ml2uO6JogGJSWgP_PzGx7lkMb0xcHu795-9TZHVoHOGjDSHX-DP5ERHP67uH6pi8qa-fPGzBxEgssfMFqIU13eB2JlkcQYz-TsjHbkoEkbO3P2agToyGem4dzTIOzaY0KChf00pMV1KmIsEtOVno3kFEKnbR3okNb9Jyku0Pf1vTdBprirjlmeW3O3lg3lsfJkuANCsvsB8kxmoKB4W45JcEIqBZeI1fpGEjgRxiQw87b5xIyIvz_mzuCpKBBqpXWkYnC-Y0ddqALc6NaU9PnuN-rQ7-xbcK3fi9yxKmYTHQM8XjK4OrM1ZBtz6jK_K7GSJkuYbTUFvR4YCMw7a6wTCdAF9LNI_8d2IOPScQJoEY5Q9Eajv3Rjv_3roUveuscHODUjwA7uiwEmkLpXYmsSb93Wn024Ci4-SglcoR6pb_ZQX8YmWJEB3T4naCOrahEOqpi4gm_3Bw4SOJ9fXy_odNEN3L8q1DUXiAmKJrobfUNZOfSDmh_kmSypi4_fKHrso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=uQD5l2xtbtxKplmKwcOwLvmDTy9BUx4X19ltVdzB6rl0XQoRxKfvC7hnbVogDQW7xT8i5U06TPIxnoJ4OC9A5telB7cEQpk9uDFoRbOcHxwwYAXMvDIFGh0GWJkps7fV51VNW20elrCsJHFwG-a4qrk45rX9kYyZQHGznrD_Ml2uO6JogGJSWgP_PzGx7lkMb0xcHu795-9TZHVoHOGjDSHX-DP5ERHP67uH6pi8qa-fPGzBxEgssfMFqIU13eB2JlkcQYz-TsjHbkoEkbO3P2agToyGem4dzTIOzaY0KChf00pMV1KmIsEtOVno3kFEKnbR3okNb9Jyku0Pf1vTdBprirjlmeW3O3lg3lsfJkuANCsvsB8kxmoKB4W45JcEIqBZeI1fpGEjgRxiQw87b5xIyIvz_mzuCpKBBqpXWkYnC-Y0ddqALc6NaU9PnuN-rQ7-xbcK3fi9yxKmYTHQM8XjK4OrM1ZBtz6jK_K7GSJkuYbTUFvR4YCMw7a6wTCdAF9LNI_8d2IOPScQJoEY5Q9Eajv3Rjv_3roUveuscHODUjwA7uiwEmkLpXYmsSb93Wn024Ci4-SglcoR6pb_ZQX8YmWJEB3T4naCOrahEOqpi4gm_3Bw4SOJ9fXy_odNEN3L8q1DUXiAmKJrobfUNZOfSDmh_kmSypi4_fKHrso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی بازیکن سابق استقلال:
🔺
به ولله برای خودم اشک نمی‌ریزم. مگه میشه ایرانی باشی و با این همه ثروت کشور از گرسنگی بمیری؟ وطن مثل ناموسه، برایش جان هم میدهم اما الان شرایط اصلا خوب نیست
🔺
در مراسم عروسی‌ام چهار هزار تا مهمان داشتم و پول یک خانه را خرج کردم اما فدای سر همسرم چون به عشق اون عروسی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107261" target="_blank">📅 20:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107260">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=bK5xnKCXBW0PMuZhsZTxpm2TvJFqDLknFqc_A-1GEdPyAMKc5NCYTrf_lxSw55znFCtBMizJaH2hsrFCmnp6RRIY9WtA6wsIwW_K9z3e0Hto27FdvXv6DYGglcSC2tUatH1Q92ustvAFNacwlX0lyTvTP-FMoJdxQSZtzOe5GC4cU3geHXob8rOItU73zV0A9OIygLsTFpXNomDdPYTA0OjsnYBacpCYlsSSJNlopKVZ-xFYuxigf9u1fs7z57e0hPA9ao0FoZdMpnqbPe1zJ5baI4ZS5oOhuzN1RUqVd9FxQIj3u0hA819KUf1XEBUqokyV7ueGoZpsHDo0xH78VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=bK5xnKCXBW0PMuZhsZTxpm2TvJFqDLknFqc_A-1GEdPyAMKc5NCYTrf_lxSw55znFCtBMizJaH2hsrFCmnp6RRIY9WtA6wsIwW_K9z3e0Hto27FdvXv6DYGglcSC2tUatH1Q92ustvAFNacwlX0lyTvTP-FMoJdxQSZtzOe5GC4cU3geHXob8rOItU73zV0A9OIygLsTFpXNomDdPYTA0OjsnYBacpCYlsSSJNlopKVZ-xFYuxigf9u1fs7z57e0hPA9ao0FoZdMpnqbPe1zJ5baI4ZS5oOhuzN1RUqVd9FxQIj3u0hA819KUf1XEBUqokyV7ueGoZpsHDo0xH78VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
مورگان راجرز: رونالدو بازیکن مورد علاقه منه اما من در نیمه‌نهایی جام‌مهانی در برابر مسی ۳۹ ساله بازی کردم و باورنکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107260" target="_blank">📅 19:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107259">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=mUokxrf9-xad0ssznEfo7FfiZPQvGTY8gS-rXUA4n8-lN5fhGuNlcLHOkGuTVyDblK_eTyYOZx7jQAeaIG0b0YYLUCkafknFMFChHeqAk5-0yQ-_5EmTYSTIRtl9D59-qH2zvpGp-k3y0VdrUudbAvjDXINaQXo7YEvZeM0kNtBI_9cVkKKwkk-sCg5rw43hUW76hq7BiJlAf4faDy2fo9uYC6RUVHVRGYxkYy3V3AXw-32_GptGkRCXrz0EK8uGPklJ_X8I3FU8TQwOtv5F0C-hjy8hANoLNcLCvAgE-iT488zqF_dK6l_adJu0M6ORQCOLT6CDWUJ0mweqc6RKNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=mUokxrf9-xad0ssznEfo7FfiZPQvGTY8gS-rXUA4n8-lN5fhGuNlcLHOkGuTVyDblK_eTyYOZx7jQAeaIG0b0YYLUCkafknFMFChHeqAk5-0yQ-_5EmTYSTIRtl9D59-qH2zvpGp-k3y0VdrUudbAvjDXINaQXo7YEvZeM0kNtBI_9cVkKKwkk-sCg5rw43hUW76hq7BiJlAf4faDy2fo9uYC6RUVHVRGYxkYy3V3AXw-32_GptGkRCXrz0EK8uGPklJ_X8I3FU8TQwOtv5F0C-hjy8hANoLNcLCvAgE-iT488zqF_dK6l_adJu0M6ORQCOLT6CDWUJ0mweqc6RKNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه‌کردن ترامپ از پرواز جنگنده‌های آمریکا در مراسم استقبال از رییس‌جمهور چین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107259" target="_blank">📅 19:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107258">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=SVF4N6_4YoLsSwWA6koCcTSrZRgO76wzNRUreuWwNbxwb-HYWXlzsc6jQaxHwU1A7wREkKDi4fQ0UR31PHA7xFm9Vsh3K8283pf9e3jE2JLBTgkbvXNwMSjEGxtin2JyxBynFz7ZKTbAZj12j5nResv3ZYRKU_Nej828h1uyuV_aG2fAu_z7JbqnwXpbuoCIi5nmTW31g_3ozRlP5zW7l_dckwx56DbYiD4A-sRK7nrLjDn2_9jQ-oN2PGM3R9ymCtNLnKuiHbGxuL7kWWEmmDaDMiUJAqNhKyoKck4ZhskIiorbsZpmcx5jF_pTLW5CeBzKXGK7wMlT_0aYp6fPuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=SVF4N6_4YoLsSwWA6koCcTSrZRgO76wzNRUreuWwNbxwb-HYWXlzsc6jQaxHwU1A7wREkKDi4fQ0UR31PHA7xFm9Vsh3K8283pf9e3jE2JLBTgkbvXNwMSjEGxtin2JyxBynFz7ZKTbAZj12j5nResv3ZYRKU_Nej828h1uyuV_aG2fAu_z7JbqnwXpbuoCIi5nmTW31g_3ozRlP5zW7l_dckwx56DbYiD4A-sRK7nrLjDn2_9jQ-oN2PGM3R9ymCtNLnKuiHbGxuL7kWWEmmDaDMiUJAqNhKyoKck4ZhskIiorbsZpmcx5jF_pTLW5CeBzKXGK7wMlT_0aYp6fPuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇳🇱
در بازی هلند-آلمان چه گذشت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107258" target="_blank">📅 18:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107257">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugUMvfpIx-6N0ra3jXNVMmrioShng4OY6_qxaKc1lEezSQ9USSQH6h4pJz5UxIOR6s3Tky8KW9U4Rl-qrQLRSMwMO-QpupDocKLsB9YEQGycXxburZBl5U_QAlhUkPWSopiuqRCjQbHP9aSoc-PWo4OkQFFwCvQRRJf7441Q1VHT-WTOExegreAV9R0LCOUNoemFqINQx3gQx3HIMEq5Pg82f7TnaFmn-EG_AemSPda7tEsBSrugsZzY2bde8RO2v7VBd4VMPtT333QlUywAxkJhVRGb-7fZN_56EB35VYyNbojbAxG4NIktGibWudr8-mCr1ck6A5iau0hQLgyMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
پرسپولیس در دیداری تدارکاتی مقابل چادرملو با یک گل شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107257" target="_blank">📅 18:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107256">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=FzHG7uoisPaHaVe59wiG5zBvG1zepmh3hw_0EczkfeGig6t5OGCeuek8jVolSwbAdnf-VSyfMPAalnLukancsd-8rDl3pYr_ZOkVwkPzNiln5-0c223HpasUj_-zg2__HaDfyJvqgAAadIsYU8KOAJg6FcFubvPNv9_f4H33E2ekgC4lqwDXIf5o5n3HBHGB2m-atuEoFUxlmFDK1zud_qbhbOrwUn1GJU9eSyyBHuMKySFg33OcwpMgD2vnRBC8pE9ZFzpLw5FJieosN3sqAY_GGdfU4vRZl1Zhzc-eEniIMRkbuEdUKDXjZcgYtiOH4ZG-Vp1l612FvRwZNnYnJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=FzHG7uoisPaHaVe59wiG5zBvG1zepmh3hw_0EczkfeGig6t5OGCeuek8jVolSwbAdnf-VSyfMPAalnLukancsd-8rDl3pYr_ZOkVwkPzNiln5-0c223HpasUj_-zg2__HaDfyJvqgAAadIsYU8KOAJg6FcFubvPNv9_f4H33E2ekgC4lqwDXIf5o5n3HBHGB2m-atuEoFUxlmFDK1zud_qbhbOrwUn1GJU9eSyyBHuMKySFg33OcwpMgD2vnRBC8pE9ZFzpLw5FJieosN3sqAY_GGdfU4vRZl1Zhzc-eEniIMRkbuEdUKDXjZcgYtiOH4ZG-Vp1l612FvRwZNnYnJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
واکنش رسول‌مجیدی به شکست عجیب روز گذشته تیم‌ملی ایران در مقابل ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107256" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107255">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107255" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107255" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107254">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YW3DW9Ij9D7xzAtbq3f0r-MJVUeDyJhxq93EugOCF1figkswcGWCtXhpWkJgy-1V649iFhBHRXCkSyIXVJjiwLZX8cZMpZsf6fFcoh9jHEuYcSqaSYXgzYaRvPJwd8fbzHcq-15qnKGkU8VadcCy7aMGOEG-VxVh9J9A7kzI2VibfDR8bKVmjDDq1NcovYPRt_UUvmchhMJ2WDiZRuQZqjkPBYTP2ovU0f9DfXaer_EN5G_D6Y__MARu5e-UnHeQsJOxfcpRtmKuYsp8tcIJDy4V9R6MuWyI4WxspMf-mfXrWDG-2UfRp-XytyEU0Kev30xVe9Wcvu2AXCtsJxh1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107254" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107253">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
🇮🇷
اشتباه عجیب مریم‌یکتایی گلر بانوان استقلال در بازی مقابل خاتون‌بم که‌دروازه‌اش باز شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107253" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107252">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccC-kFIoSCsYJqYJaoWH8hDrJYOMjACFvVJ4nP6Q9SQ-cUV2l0c-HbgKolhtjfQduvTYWInOzvocquVmmi0i9yV9r0_brPJ8_K7fCQTpipn1rmoQkvmXKmRUTvcd4hNxdDaFihnwsgN2orAgyN2F-eFsuJXnDTk9U-s8Bl1jIv-5PnkCX3nzJZ5Igc7Zb-akmYTvr4CNZrmTBnTdyWVMaxrISqyCWE0M-Ra9YyzOuEpSbg80Md03ShcRRswemdp4IZddX2zwU2XXVmlK_v5fNy0Rmd2nur00UOhoK_2s4O7xQtP1wrWsXF_UNYi3hry3tvxwXg3zHFxs1huMPEcICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107252" target="_blank">📅 17:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107251">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNFlDY6kiuL9MoODOGTiYmD9h5vHUztC6OJSOonuApEjFIzV28QjzvwUmfuoweeWqyqiStXATD1KC8NxpboyjrOGAAyfc_qVgiU7eSjxH9Wp_qK2mGp77Qv_HkTmggCAzjfk_MVQbjj-KzwlQ_BUlMHIDkM2XsAB4il580u1ailahsP1PLhXcXrWtU6IwN3IvDktAAizWIaMTYuKrXNK54Ldsy8jCF-s517ZwYuFaaMbZdb2dDQWRbZvAqTgY-1vZ2YbEseS9FDnaV8IHr8xGJXcitH8ng5hc71eRDPDO2-325yKYCSTlw3DfW-GzxYC1XpJ5UUPR9kEFTfopPglXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107251" target="_blank">📅 17:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107250">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhbCSqvPyXWNkCR9CaEbEoAhzo0iVg00XHEPjrbn2WqO7I1Pwjlh9tIor6mDjQjM6MARGU5mqA5riWqaHYaQ_HgRZrDntsb-LXVYCgtArA0Wtd2-QdwTIIZK1Vxgdx6Is3pqKeU76DFTdMH4gN_5WHx-JbkYu5bdkJ9f2w3xGH3OGJ3xgt5dwt4CiiUhIl-dVbj42lY0Fozxd4c-UyRkJ4Wt_NqQz4Z6vAoo7XelNpEguKuQbwOElAX6vzHjNPTx36_e2isBpWdrxwUW4jnpSUYhsGOi8oaSA3tOJrOsmD5X0mQi-DbFi90XHKQjUsN6U9gKi0ZrYTivL2jOHnPsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز در مورد تحریم‌ها تصمیمی گرفته نشده و روند رسیدگی ادامه دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107250" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107249">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638e170672.mp4?token=d0rAOiySYC2eQXGo0QlV7VgSbWr8lxZWGodOA4RYPCo9fZLJuh1id17nKvzT_3woZVFHMoeqEep3F9vULADrKfuiG5HTiufPXkkpg39h45c73vibQaK2W9_5CMS9Y3rcBB8bzVD-l1dlarzFh6yiBHK4ZaigOh2okBqb0sM6iYWkMNEWSGOC8boKtRIkFzLgFUjK27ZfwTX837FsFo6d08Sw73u6qknWM0RnWPoD5DMX_tirEur_vespmHsvrx31GJuWQYAqdTZHtij8vQW1oPj6MAAoi96h_Ltrxyrovj_HC8hnGGGsLCF96WTp_hJCxFrpAwEkQz3Ufcqw7O3KgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638e170672.mp4?token=d0rAOiySYC2eQXGo0QlV7VgSbWr8lxZWGodOA4RYPCo9fZLJuh1id17nKvzT_3woZVFHMoeqEep3F9vULADrKfuiG5HTiufPXkkpg39h45c73vibQaK2W9_5CMS9Y3rcBB8bzVD-l1dlarzFh6yiBHK4ZaigOh2okBqb0sM6iYWkMNEWSGOC8boKtRIkFzLgFUjK27ZfwTX837FsFo6d08Sw73u6qknWM0RnWPoD5DMX_tirEur_vespmHsvrx31GJuWQYAqdTZHtij8vQW1oPj6MAAoi96h_Ltrxyrovj_HC8hnGGGsLCF96WTp_hJCxFrpAwEkQz3Ufcqw7O3KgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
هادی چوپان: من حکومتی نیستم هنوز فکر میکنم دارم خواب می‌بینم؛ وطن‌پرستی دلیل حکومتی بودن نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107249" target="_blank">📅 16:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107248">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=Uirnm5WvO6x_PswrOoCZWr7hd6uIihEXGMYlAJWsKkWodPfAmgFVFdaE8i-09VKLNL_2PIpZGycLioUfMZtj4vsT_xM5omyaA-eoNbMjqIEQ7cZ1x4UviZ_oxOTrWjCJMk3IcxGP0IC12YzJXRGbcVQ1omVQJFtPN3BXyXhpXbgPnd1v8DhUfW5WExmS3dTu2MNDI5e_gs4VxuT5xi60aKD2UktPX8wt4Q-vp6Q-w7WnVKi0H33OV19f_Xifkx_QAEM8O9aF2yQpxlNVvcV9zOowG0YmdKepQTVd1zlGz1Y5ENcWYVCcDHfaG-27KW1RZmDLx-YtwOoNo3Epl3jbgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=Uirnm5WvO6x_PswrOoCZWr7hd6uIihEXGMYlAJWsKkWodPfAmgFVFdaE8i-09VKLNL_2PIpZGycLioUfMZtj4vsT_xM5omyaA-eoNbMjqIEQ7cZ1x4UviZ_oxOTrWjCJMk3IcxGP0IC12YzJXRGbcVQ1omVQJFtPN3BXyXhpXbgPnd1v8DhUfW5WExmS3dTu2MNDI5e_gs4VxuT5xi60aKD2UktPX8wt4Q-vp6Q-w7WnVKi0H33OV19f_Xifkx_QAEM8O9aF2yQpxlNVvcV9zOowG0YmdKepQTVd1zlGz1Y5ENcWYVCcDHfaG-27KW1RZmDLx-YtwOoNo3Epl3jbgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
عادل فردوسی‌پور: کاش زلاتان ابراهیموویچ یه روزی برای تیم دیگو سیمئونه فوتبال بازی می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107248" target="_blank">📅 16:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107247">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c917893c10.mp4?token=S2cV1lyL-uCUIs_t6qoiW1VuLny-rQqBojzngUeOLIGrCbzg3lHmXLYIjPMhTLOeUNy6RQb4EUl5fekZCTBGkBy5RiS8vco_JUKj9GS01n2LGWsWyGf52iX3bK_u49ZMcEcGl05dGDCkXzWzriSr-NcIDf5Ys7k27n_ra2VDjDs-kPD8NlcgqelJXBVjO4diUu8lSpdTyQGEZ17WmHz7ANL87kFHQyhuK8mt286onikiQrjUaqNo0Zv6ZYrwGGsyiMxF-GrBs9YdC-YuI6gMGf0GxsummH0uBaxVDgGVxXhZ_sWB35QewYJ4XljG-vofA2HcvswGVgBcaaBIdn6shw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c917893c10.mp4?token=S2cV1lyL-uCUIs_t6qoiW1VuLny-rQqBojzngUeOLIGrCbzg3lHmXLYIjPMhTLOeUNy6RQb4EUl5fekZCTBGkBy5RiS8vco_JUKj9GS01n2LGWsWyGf52iX3bK_u49ZMcEcGl05dGDCkXzWzriSr-NcIDf5Ys7k27n_ra2VDjDs-kPD8NlcgqelJXBVjO4diUu8lSpdTyQGEZ17WmHz7ANL87kFHQyhuK8mt286onikiQrjUaqNo0Zv6ZYrwGGsyiMxF-GrBs9YdC-YuI6gMGf0GxsummH0uBaxVDgGVxXhZ_sWB35QewYJ4XljG-vofA2HcvswGVgBcaaBIdn6shw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
صحبت‌های شنیدنی رودری درباره تفاوت‌های اساسی فلیک‌ و پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107247" target="_blank">📅 16:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107246">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=c2_oVDlXGZEneI9Ejzk-VtPVx-YiORs09bZ32BdF5P3_wqA5fp0UeG1PzWe9jqh3TdkeQMrpTmG8lG2RlAtAcRKoKbRoa1d8lb01nfEYlDzq1r8wYhbg2IAEIixjO-nhNl7o_482nFPoMZBHMib7q8vZSIXPUqcYrIs9JxV1vSPgmeIX674u4lRIWtyd0zHfzXCxfkTQtZVYD3UWVHG90dZ9MHU-fokbTii8nhshvK7jM86DQrFA9H4847adjpukmdeYqxFbl3PAQn_9MyCrIQtuXV5Vloh8KY67z9V85fl7Yl2kyd2fEjbgC4DsC1Kz8Zr-FclMbtlMWnZyRqg1iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=c2_oVDlXGZEneI9Ejzk-VtPVx-YiORs09bZ32BdF5P3_wqA5fp0UeG1PzWe9jqh3TdkeQMrpTmG8lG2RlAtAcRKoKbRoa1d8lb01nfEYlDzq1r8wYhbg2IAEIixjO-nhNl7o_482nFPoMZBHMib7q8vZSIXPUqcYrIs9JxV1vSPgmeIX674u4lRIWtyd0zHfzXCxfkTQtZVYD3UWVHG90dZ9MHU-fokbTii8nhshvK7jM86DQrFA9H4847adjpukmdeYqxFbl3PAQn_9MyCrIQtuXV5Vloh8KY67z9V85fl7Yl2kyd2fEjbgC4DsC1Kz8Zr-FclMbtlMWnZyRqg1iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آندره‌اونانا گلر ترابوزان‌اسپور از روزهای خودش در فیفادی؛ معلوم نیست چه غلطی‌میکنه
🥸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107246" target="_blank">📅 15:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107245">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=TTaFUxr2eXNB4JG00o2re3D1gCrXd4z_fqihbcn7iDWsSmP1LXjCz8E0VHujC1EYyq1OXpbjHkWQ-gS3vBzbxCRswQ9sQQ-c1AcatUVmPx0YwO0VQj2YG_JkL8uZPV_vi9jb1WceMMByrRxIUU9dxE7ATxhRmDLTqGFAz0vIf-TZ4BtXNqWhj3f_-GkuP9Si5CjBJ0Bwl9-li_iVaFybX4Z5xzg3xBSK0K_CKz1-9s3LWsPb8QMFygy7NRU-1RPkNddsehZx6JnrZTwhpS0koBrzgfrEA5ekE2I6MoyqPKcnRy1AHrsCM8-wQjboe-bWtEskrPh7BFTavjfc2NANsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=TTaFUxr2eXNB4JG00o2re3D1gCrXd4z_fqihbcn7iDWsSmP1LXjCz8E0VHujC1EYyq1OXpbjHkWQ-gS3vBzbxCRswQ9sQQ-c1AcatUVmPx0YwO0VQj2YG_JkL8uZPV_vi9jb1WceMMByrRxIUU9dxE7ATxhRmDLTqGFAz0vIf-TZ4BtXNqWhj3f_-GkuP9Si5CjBJ0Bwl9-li_iVaFybX4Z5xzg3xBSK0K_CKz1-9s3LWsPb8QMFygy7NRU-1RPkNddsehZx6JnrZTwhpS0koBrzgfrEA5ekE2I6MoyqPKcnRy1AHrsCM8-wQjboe-bWtEskrPh7BFTavjfc2NANsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌خوشکل سون‌هیونگ‌مین مقابل اکوادور که تنها با یک‌گل دیگر به بهترین گلزن تاریخ کره تبدیل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107245" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107244">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=mbEEHZMJGLkQZU1Jn49RnRiCzmflg2roxM_3PDd4QLtGgNOzIyihqwAfRDnhTqUlbxxlA3_qoKBqN9h6JE7iOcbvatw2V2pG4qCgVSgSqrFeP3rlLx7RqaAHsNe5M2gsV4uoSzyQTIzw9ym4zVj4PxBVZoRxlJ_yHhDFFloipvOqF_UPy6av13Qp1X8nIuIjvQKOd7fxZFMhGsauesgLItAEPprbLhxuloENBDqq-Y_WL32_DFazrwKyksBJOsUwmKb3l67RBiLipmvXDNIcY_p08UzDnlpd3DAZx4zJxuqJEpUAK8uhw53bTPZm5IiXbPVN5raAeFJyDSydNhbJOxwOR3rO33h0AwySOiGP-Erh7Hh_yUQjudTTciXFPNhkmE1EwMqB3e95zX9IAAHLfqgZP2XxxVQQHX5RDTvg5nZkDa64l7QVyncEXrx-DuFfYZV0WNTdg2iTFOPH5YSVkYofR2Q7kjse2qG4dzmQ6yRVFUGySX_EyZhQORqtZUkgF0ZqyyXTWtE1j_gmGjJua1KQ1Z-tyFKAmcFHn-6N_2T4QxybKimaH1vWXOFwBokvO1b9SKd4bJs0Ma3FHPk6-QN__8589A3s6fPF-HW-lbUjJpYs63otk_CHpRYEezUFJt4_qGWmI_r_gJQnJlNe9_K5qTzYk5dJ44lXSzLnNZ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=mbEEHZMJGLkQZU1Jn49RnRiCzmflg2roxM_3PDd4QLtGgNOzIyihqwAfRDnhTqUlbxxlA3_qoKBqN9h6JE7iOcbvatw2V2pG4qCgVSgSqrFeP3rlLx7RqaAHsNe5M2gsV4uoSzyQTIzw9ym4zVj4PxBVZoRxlJ_yHhDFFloipvOqF_UPy6av13Qp1X8nIuIjvQKOd7fxZFMhGsauesgLItAEPprbLhxuloENBDqq-Y_WL32_DFazrwKyksBJOsUwmKb3l67RBiLipmvXDNIcY_p08UzDnlpd3DAZx4zJxuqJEpUAK8uhw53bTPZm5IiXbPVN5raAeFJyDSydNhbJOxwOR3rO33h0AwySOiGP-Erh7Hh_yUQjudTTciXFPNhkmE1EwMqB3e95zX9IAAHLfqgZP2XxxVQQHX5RDTvg5nZkDa64l7QVyncEXrx-DuFfYZV0WNTdg2iTFOPH5YSVkYofR2Q7kjse2qG4dzmQ6yRVFUGySX_EyZhQORqtZUkgF0ZqyyXTWtE1j_gmGjJua1KQ1Z-tyFKAmcFHn-6N_2T4QxybKimaH1vWXOFwBokvO1b9SKd4bJs0Ma3FHPk6-QN__8589A3s6fPF-HW-lbUjJpYs63otk_CHpRYEezUFJt4_qGWmI_r_gJQnJlNe9_K5qTzYk5dJ44lXSzLnNZ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های جنجالی هادی‌چوپان درباره جاویدنام مسعود ذات پرور: منو شیر شاه، سلطان و شاه خطاب میکرد! عکس منو از باشگاه ها پایین میکشن؛ ولی من بخیل نیستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107244" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107243">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947rv-cKvDHL9XwW-XyWSY2Lp-ZzrDAR0QAVIbbZxMoxx8HY6rBiN8zo4i2-0E5HCmkSA7iACPWj5hyrCtuPJVmm7iM6A1gfUk_lQ31Y_IOMDD_409x0Z3fIFC9Uv7FZnJ6ZcS5V6JqUA9PshxzoVs6no_BOtR8lJxrUF_47BxU3EdUc2yIdItiZq0y3wa3-niO7RNFI62_1p7GlfOhqbgDFwgNzJzXJhy3i_W_Yte4Mw_Mbd8Nh0yalA5LUnoYEy7ALQbr9B5_H6HwvToc4mbsJ_31SImw5aIRnL5iGnTM54IO_GHGFrPUAo39d-Ftykl9D79aM2HNrj_LHWCmYmdjE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947rv-cKvDHL9XwW-XyWSY2Lp-ZzrDAR0QAVIbbZxMoxx8HY6rBiN8zo4i2-0E5HCmkSA7iACPWj5hyrCtuPJVmm7iM6A1gfUk_lQ31Y_IOMDD_409x0Z3fIFC9Uv7FZnJ6ZcS5V6JqUA9PshxzoVs6no_BOtR8lJxrUF_47BxU3EdUc2yIdItiZq0y3wa3-niO7RNFI62_1p7GlfOhqbgDFwgNzJzXJhy3i_W_Yte4Mw_Mbd8Nh0yalA5LUnoYEy7ALQbr9B5_H6HwvToc4mbsJ_31SImw5aIRnL5iGnTM54IO_GHGFrPUAo39d-Ftykl9D79aM2HNrj_LHWCmYmdjE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
به‌مناسبت بازگشت زیدان به فرانسه یادی‌کنیم از این عملکرد تاریخی اسطوره مقابل برزیل در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107243" target="_blank">📅 14:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107242">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🎙
👍
احمدزاده سرمربی سابق ملوان از کمک‌های اسطوره احمدرضا عابدزاده می‌گوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107242" target="_blank">📅 14:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107241">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=fTCJCXw0uNBpLpLnxbLLbHwPTUPOvLKIE_-yCV_R7xiTXxvfHSwHyslserux_k68Vae_LCqlSaX30mpbu1gnbSEL4oAWINpuepn2z9fuuNFMPk6iYub7kA6iwvvb2PY9oU-konMBSORH1zcgKFwqXY1IDO04k2nsY0g_lHiPTDhUZbpI7b7kGuqNhNXy0wswh34HZx5oWkupyX6Ho8Fxu1YMdeRb60FapSmgVeBz8iypNiZq-43XMFVsk62pcqmArMPR5zH1YcW01XQqRaAKCe0cFtfH3u4FNwg7BlQ1orHMT5-drcxmUpT48_uPElEunLF9HXCgu98FwXU2rFhnxoQFwTmPlYL_PfAz3MTYs6798eAXxrkN3xqhtwYyjzg0jZeP24m0v1Zv6epRg9jWndTySYuh-iTxlt2fK1pXCbfAmVQt-C0slb8wvIGb9mEzWfXZ_JGpdujw4e4C0lmAVl98-QOGkpSx6-ZVR9yWPCl8vEnJX2ZeH03BOIGQzwGaqELVrY6YADSnZWnicrW_XQ8MA7i0VKw5Ht1efl-JfDFnjVePhBz8E1guU2B1NEm_pNu7vyDMSSIGkresUBN35GF3AEmqz7MTQZg09VOA6FKhX-OzJXdpBPASvRpmAgJ5lYiNGXzPYQKxrD1W4vbd9Z_B7zOPiJBrUJvKYFEtxzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=fTCJCXw0uNBpLpLnxbLLbHwPTUPOvLKIE_-yCV_R7xiTXxvfHSwHyslserux_k68Vae_LCqlSaX30mpbu1gnbSEL4oAWINpuepn2z9fuuNFMPk6iYub7kA6iwvvb2PY9oU-konMBSORH1zcgKFwqXY1IDO04k2nsY0g_lHiPTDhUZbpI7b7kGuqNhNXy0wswh34HZx5oWkupyX6Ho8Fxu1YMdeRb60FapSmgVeBz8iypNiZq-43XMFVsk62pcqmArMPR5zH1YcW01XQqRaAKCe0cFtfH3u4FNwg7BlQ1orHMT5-drcxmUpT48_uPElEunLF9HXCgu98FwXU2rFhnxoQFwTmPlYL_PfAz3MTYs6798eAXxrkN3xqhtwYyjzg0jZeP24m0v1Zv6epRg9jWndTySYuh-iTxlt2fK1pXCbfAmVQt-C0slb8wvIGb9mEzWfXZ_JGpdujw4e4C0lmAVl98-QOGkpSx6-ZVR9yWPCl8vEnJX2ZeH03BOIGQzwGaqELVrY6YADSnZWnicrW_XQ8MA7i0VKw5Ht1efl-JfDFnjVePhBz8E1guU2B1NEm_pNu7vyDMSSIGkresUBN35GF3AEmqz7MTQZg09VOA6FKhX-OzJXdpBPASvRpmAgJ5lYiNGXzPYQKxrD1W4vbd9Z_B7zOPiJBrUJvKYFEtxzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اولین‌گزارش نیما‌تاجیک پس از ترک صداوسیما و پیوستن به پلتفرم اینترنتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107241" target="_blank">📅 13:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107240">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=H020HZFN8mRBJLMy3zQ8sq6xq6bGZUDjdXPQ-QJ8ILRegpmXIdWVmh2EUyQ-rUIdc30y4pltoNpg2FS9S_2fKpK-OcZIbfg2lHZBfibNBmAuoTrI1SoJ3rCeI7iMiE02w0Jh_jSGmJbwcKTe39KWcZyNtQpzZa3Q0JW9_4ksJpxF0O2Uf8tPEXWnAXG3Yqt0U-aAVNewcqHBfS6-m2j9J11VRfHhWZeT0W-EQPo4p6H0YVCzYlC6v4lFhN6072-YiGtA_bib5pYhWvOTQjUtLYnD0xxWUODwO17jfj4MmgV6O201rw-ZfxCNHIwLQvS6o7vE75_15CgV_dbwPABiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=H020HZFN8mRBJLMy3zQ8sq6xq6bGZUDjdXPQ-QJ8ILRegpmXIdWVmh2EUyQ-rUIdc30y4pltoNpg2FS9S_2fKpK-OcZIbfg2lHZBfibNBmAuoTrI1SoJ3rCeI7iMiE02w0Jh_jSGmJbwcKTe39KWcZyNtQpzZa3Q0JW9_4ksJpxF0O2Uf8tPEXWnAXG3Yqt0U-aAVNewcqHBfS6-m2j9J11VRfHhWZeT0W-EQPo4p6H0YVCzYlC6v4lFhN6072-YiGtA_bib5pYhWvOTQjUtLYnD0xxWUODwO17jfj4MmgV6O201rw-ZfxCNHIwLQvS6o7vE75_15CgV_dbwPABiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رد رشوه میلیونی برای امتیاز دادن به استقلال
🔻
اتفاقات هفته آخر فصل ۸۱-۸۰ لیگ برتر؛ قهرمانی پرسپولیس بعد از شکست باورنکردنی استقلال به ملوانِ محمد احمدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107240" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107237">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LjLOyKa0Thfku9FnGYUqzbUYkt_LbkWCHgEg8PUt3MuZ-hoR7-AZ1Lcqy3N5NVIHIErKDO7bP4PTq7p_fIisuht2zG4dqPFAN8rFtZSl59Ct-qLAtcgP38DcSD_BK5FNgumvJmZ_FmxkAW0Hm3v0I5rCoht5oJPGIstb5gn3pgyI0pqiWYSBDwdLIV_4pVMLFVsiFtpyX2DvfOr8TWH_y8Q4JFCjSQEVgnRZdo9_BVdxqq4e0xAN4Zb_3e5AS-WuW6GxacGyJDw4rWuhx50U9y1RI_FsdPfr9QxpS8Hnxam8ulQ5MlHEs0JdEVUXXW7VJei_JGv02tMSvP4op84WEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N3KlE3ixIOzRPdyEGLcnqaCdFWeIfTVyDXAbvb8FVDTwXRG1KwFLL35MID58QL0V9Jn6PjrX3fzCgTCx4LlOzqPVB4IlVft-MO-AEgb_FriHM0Wm4kwZFN_L16BOym9bkH_1k6ucpVCQe_5qT6_22gNY7n7NJdG6hBVOUMZMFrWEe1n07fOzVvpv2cTzqRFqIpyirhAU8ZxDaz82fsnF2It4IRnLPeVznXCI_wt_QWJ0gR5iYNSfpCeOANCHJwC0GinGZCKxCbul4D_Bww6rTP1IaK-Z-xnhloJDtUsUcLr16ul6ZJiLzJy0H23VFJxmtrxul4ofp8RUoxDEJU3CNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bo74jNXN6oyIL26uh1VtnNbFsKkSOdz7wwCa-ZareXjXdMuKosYm5PrbTY2dZhPOajF05lyU7VLbYKzsWTaByLoXHRd6rNPfxFrn-r0vOVQO9X_8ue8AbpClDLALjNnN419Pr72k5ztbtV-ooTUbg4eDRGhfOiY_pkgwz9NesZuif-zJZHYD2C56Kpd32X_TqzftXNrLE6MmFN-Yk9-uCpMesYgGMFlARK07WMMhrY2Sr-t_lI5lxyEY4OhttcNOmjBApTY6oF8X9Iq7sJC64WJcKEiQKocEBxu45Fzi-nRw-iqXuXE7439-MFC5P76_I76O5anPB2GEhAVA4D865w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🐐
🇦🇷
تصاویر اسطوره لیونل‌مسی در آخرین جلسه عکاسی با تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107237" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107236">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FeHGxPX-0Zz9jqXDWoKWh6TdKMJsg7umkQMRsahd7zOEo7OqoRUZ0NtDM0jbYXGSIVZKVAp4W6pwt-GZ5pgC-tzrfKluY9pfE-7SKTqKurZ0IzazZ1QtJE4VYiejKcHYD0lBNHme-lak7xeUePJoDBzbfe0f595xKO2DPi9a8Wb0VZ7zflSsfZCKTv4-UB-cQ7NCumpg3PBxyyoKcqQb1kyxqnzPtZhKi_DuP-B1Bgh_SFoWg2VmZnCKYY32mxG59Ob6hq-agU_6oqMtnBmN3rjwx4KM1g0SgP7OsEMAqJTmjefYS_KhL2l63YAIFGHx9FY06ilwU1ndqZ1qJhO9yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107236" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107235">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=RQeB3KqSDDGgFF91NOGG5WbpGtyIZAn8hnDq9hyzkDtGUXAtDxtQIzTnjamPlY9pX42B1oWMzVjUZMj8ipeYGl8jlJls6LkYLX0hbpIGhCQNF0mU2fcK2aUNPBi2qtFsfyFQW5Fvcp5aankstMQ7ZPYrPjtyPDDZTHCxU1g173GTJ3DQADUuERuIXSFlb9wefqdgnOZYBsj4ot0TGAHisZW1E4aYHhnexTciAe9tkOiQtbghW-500Ao35_GGUQeb94BOpAKJsrgkfq4tukFxqPlp1ifPAOyUwH_BPslDwd6G-JnFfP9RRHnmXC5bDg7h9DgbpsoI9GqZb5WWdaGteokARGvMlv9y-KiOtR9K9s7AiRjqw90H9sl8CyRpRoJShqmyOvVhI1bK5jgGBjs-C8RWMo0Vr71pbr6nMMlkkMr5Skogqm8Y2vBrQ3DtFOXsD4sWj2F--_hrfisufevdmHl_UX1sORVI_VaT7cYsufxdWQLxVk8AcBIvW532hjaCm50MgSA4r-gCRbXKDB9X_QXLmE0rCIVTAEYuywSzUgvZXBkmtdoj-UMCl_DWisA6Vr7Z5HPOpzCmljrEDX0Qc8y1Cw4tkjdMibPExkrqXaTOcOJFtmZvLc6KnWNtClos1W2AgagNKJeO-IGGESqp__mYMJy6IHWGpkUeaElsxWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=RQeB3KqSDDGgFF91NOGG5WbpGtyIZAn8hnDq9hyzkDtGUXAtDxtQIzTnjamPlY9pX42B1oWMzVjUZMj8ipeYGl8jlJls6LkYLX0hbpIGhCQNF0mU2fcK2aUNPBi2qtFsfyFQW5Fvcp5aankstMQ7ZPYrPjtyPDDZTHCxU1g173GTJ3DQADUuERuIXSFlb9wefqdgnOZYBsj4ot0TGAHisZW1E4aYHhnexTciAe9tkOiQtbghW-500Ao35_GGUQeb94BOpAKJsrgkfq4tukFxqPlp1ifPAOyUwH_BPslDwd6G-JnFfP9RRHnmXC5bDg7h9DgbpsoI9GqZb5WWdaGteokARGvMlv9y-KiOtR9K9s7AiRjqw90H9sl8CyRpRoJShqmyOvVhI1bK5jgGBjs-C8RWMo0Vr71pbr6nMMlkkMr5Skogqm8Y2vBrQ3DtFOXsD4sWj2F--_hrfisufevdmHl_UX1sORVI_VaT7cYsufxdWQLxVk8AcBIvW532hjaCm50MgSA4r-gCRbXKDB9X_QXLmE0rCIVTAEYuywSzUgvZXBkmtdoj-UMCl_DWisA6Vr7Z5HPOpzCmljrEDX0Qc8y1Cw4tkjdMibPExkrqXaTOcOJFtmZvLc6KnWNtClos1W2AgagNKJeO-IGGESqp__mYMJy6IHWGpkUeaElsxWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دلیل عدم دعوت مهدی قایدی به تیم ملی؛ ناراحتی قلعه نویی از عدم واکنش قایدی به صحبت‌های یک مجری در یک گفت و گوی تلویزیونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107235" target="_blank">📅 12:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107234">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=AmDRJvCKw4rWVWbBLQYmI9bAFSErnKbJOUS-JyEv1Nyq0A_i0B4ipM2VDDWyZhdfQu3c-062a5TCfNu3mdvJnlPrDo7zhbVME6DJDoLDr1ATjQ1bCnmMXZB2RnP3YrA-enw7jjipG8t-8yJYSX_2QNK9fLqiKBdDWJOChsBMz3B5OOZi5yP26abnmgpU25Yf8oweykzWEDLA5U1uvzOKNCmJdw8qJAEwYtVAQyPEZpRpx7Del0iN7LEN9sgKrfObt-IOYlMOnvB6zoovE8OQvpotg8ax1etXjZUFwDbDVCuInRyEgSPuCtk-RVQuQh677atPrCcKYb7o7-cC3ysU5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=AmDRJvCKw4rWVWbBLQYmI9bAFSErnKbJOUS-JyEv1Nyq0A_i0B4ipM2VDDWyZhdfQu3c-062a5TCfNu3mdvJnlPrDo7zhbVME6DJDoLDr1ATjQ1bCnmMXZB2RnP3YrA-enw7jjipG8t-8yJYSX_2QNK9fLqiKBdDWJOChsBMz3B5OOZi5yP26abnmgpU25Yf8oweykzWEDLA5U1uvzOKNCmJdw8qJAEwYtVAQyPEZpRpx7Del0iN7LEN9sgKrfObt-IOYlMOnvB6zoovE8OQvpotg8ax1etXjZUFwDbDVCuInRyEgSPuCtk-RVQuQh677atPrCcKYb7o7-cC3ysU5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
درگیری با عارف آقاسی و تهدید سامان فلاح؛ دلیل دعوت نشدن کنعانی‌زادگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107234" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107233">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107233" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107232">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXjJFSFN_1zvb5bKKagC2PuXijE6Z5aEtIoDPYE06F7-fBINYETg-b2zmgZNoVdZyTo7zWKeOSXIEMgRZT6MA5SffSunA6AYXWTiRPmUOvjFOuOyQicJC9nu6v4jSKEOIR3py1IPL2n5_qsDjx_-aoE2CxmGwcyCUb59jDvXI5s9UT-_CHgbptMknSLSG3GYQBaXBn0fITzofGAuwCVanC2K6EYflydj0fC-AKCTmOvfelUirWN_0IE2e76FLYpHDZodKL2X1DQuFi9mq41pib1174Cj2uugW57U1gsRd3CpOp8QuQuBTddctK4wVGWi7j3fNUk_gxU_ok4jV0QL2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
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
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107232" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107231">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=gk0jTq6F2FWHPpI_9gtaNYOBvQr8pXfbRUwYaKUSNeZS7hftHT-ZuwMow5U0k3bHDEw5EompaYPfMn4BB1Mw0a2kMRcHN98kChW_oCNo694t6e9vfkrCU5welJSZul-eHYEoLP-H3L3WMbTZDD8B83fzDFfXkcM6afI5tqXhewEyLbWSpF86erGhfPt9aDy2FbQqQaMyEb334gbdxIVQcneG8qKBLiYg4sKlwfBhjpKjFyjSj7l4ZEXfFDAGfuQXPGdBEkSuhslkbR3KRFC-HIpRPJDfaLWIAMAaxmbDyXk1zydrEVxBtvvxKRGSMIe0Kb4nQ-qcPJfSGypBhtIkqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=gk0jTq6F2FWHPpI_9gtaNYOBvQr8pXfbRUwYaKUSNeZS7hftHT-ZuwMow5U0k3bHDEw5EompaYPfMn4BB1Mw0a2kMRcHN98kChW_oCNo694t6e9vfkrCU5welJSZul-eHYEoLP-H3L3WMbTZDD8B83fzDFfXkcM6afI5tqXhewEyLbWSpF86erGhfPt9aDy2FbQqQaMyEb334gbdxIVQcneG8qKBLiYg4sKlwfBhjpKjFyjSj7l4ZEXfFDAGfuQXPGdBEkSuhslkbR3KRFC-HIpRPJDfaLWIAMAaxmbDyXk1zydrEVxBtvvxKRGSMIe0Kb4nQ-qcPJfSGypBhtIkqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107231" target="_blank">📅 12:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107230">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
بهانه‌‌های عجیب حسین‌عبدی در بدو ورود به تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107230" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107229">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=J55oyCH3CZomlySK6r0SjxtzfXmF9E6JGnOvggTXsp7P_lfBDfpo4NGpk1PfwBEpaXBE8fArdeKwerjDn0QIAjG422QBALOS-S98IOxqMNKqk7otmhyvVwT1YJyZdYnQw5SrwIvq8OsSfW5zuJ0NnmLme0xKAOd0pBzo_Wbff4aKMqxF-oZB8WHqfDl5UseN1iOaTw1J3QhauYMalpVQ14Gmm42i3P8JLxsb_9ntQbNc0y5fwM1dbkixm7Caqi_F7QS7s1jVenVEDnrDAF5t6Y3QZbqH84xjBy4ZlKi9KU4UZG9rv_qapPaaK5rzrKNtOPTek3ltjL8Y0taiAduxeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=J55oyCH3CZomlySK6r0SjxtzfXmF9E6JGnOvggTXsp7P_lfBDfpo4NGpk1PfwBEpaXBE8fArdeKwerjDn0QIAjG422QBALOS-S98IOxqMNKqk7otmhyvVwT1YJyZdYnQw5SrwIvq8OsSfW5zuJ0NnmLme0xKAOd0pBzo_Wbff4aKMqxF-oZB8WHqfDl5UseN1iOaTw1J3QhauYMalpVQ14Gmm42i3P8JLxsb_9ntQbNc0y5fwM1dbkixm7Caqi_F7QS7s1jVenVEDnrDAF5t6Y3QZbqH84xjBy4ZlKi9KU4UZG9rv_qapPaaK5rzrKNtOPTek3ltjL8Y0taiAduxeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
دیدار هانی رامبد پرافتخار ترین مربی بدنسازی دنیا با بهروز تابانی قهرمان سنگین وزن ایران حاضر در مسترالمپیا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107229" target="_blank">📅 11:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107228">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی محمد احمدزاده سرمربی سابق ملوان که این‌سال‌ها به شغل دیگری مشغول شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107228" target="_blank">📅 11:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107227">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LuH53HB8r4mGZxi7qcVp1zlua_gKUSeaB2MzaEz8r7-RpYvC02fcnAcQu5pL_h9hc_y4wjk84ioTsNih2d8Ozwu4kH-L3p12oR4L7gHxnD3Ia5sXw_pEOinnU4MQsEwkGyTdx1ieQGl47pcq7L1R91hn-g5xW15g_-GtiJRmVgbP5khkXHX9qfUn6rpgD6jgCqrojSZ-HMf10gOEGv5PQXUzvyDcY_Sg7NudEmC0Z3o9ChwiCYC_80GpfMqEVnOmmnlR0w8ACIXl1HaSs-QlKux_4b9jG9726sE_ZsdjeoJAVPCA7MQMZ58rbhEJw1CmaNGZ-dTyEX7xTZlm1Uu8sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عذرخواهی اسماعیل قلی‌زاده بازیکن تیم‌ملی امید و استقلال: از همه مردم عذرخواهی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107227" target="_blank">📅 10:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107226">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHZ_Nfx_u9ItnfdOU0Eub8rX8E6yvPwZ3nji4QHiigiIGtmriMIQHkuUaZ7O8RJ8GVGTlIUK4V6aQ4tPski4CYeSyqxi4nX_G7ukEUr2mOlouKCe6jrBSkFlvoPlYZpObTZ3SUVs2H5rota0-kJ62ecqqNshVi3ou2jxg9JICGXAMP2Yy32x-aRVxO6-zCrfkuNnfJewu7nAzQxaKDyVSphVJwaqU5RdY8REUrFTiF6d4RQbESZk70FtrbuonUQjUrZWzBr5jRaFsGabF2FsbNgmzdHVVDxQtrcPZqIL38Cak7f2L7nOxq6HawqFWSqLtZiyT_Jj9TsKvrJFxI1O8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تیبو کورتوا: بدون شک من عملکرد بسیار بهتری از کاسیاس، نویر، بوفون و ... داشتم و خودم را از آنها بهتر و برتر میبینم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107226" target="_blank">📅 10:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107225">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTmKykItZgUlVU8hWj9h1A1ZNIWHiT2rD5LODVFfgnKWFHzdIt5k4_iOA_JI1HqC0SZXFzGFdmfRAN-CHKh8rVjCT8M97se7g6AuorQwkT-5D1Rrz31VuDmsrR6xwqM4-k1L-UpIif-ZKHuWTRj0wiC7AOukT1s-813fBHjOkzrw29PzL7XM28dqV16Y1Tic7cHEwdm2zci7iHFakZx3iZDzSMUjYhMKqCWAScZ8HaPxc-igYjtk4-j2po805Cq1cLl4yakFBLJqVrbtKaZ6NZwEvXkuYLsgt6nGNhBUVMmCsYQmdkhuaMtjxb1OP3Mp6GTYjXgyHoFcnJuybfMZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
رودری ستاره بارسلونا:
🔻
"من در حال کشف چیزهای جدید هستم. بازی با پاریس در ماه آینده، به همراه رئال مادرید در ال‌کلاسیکو، تجربیات جدیدی خواهند بود. احساساتی که قبلاً نداشته‌ام و مشتاقم به عنوان بازیکن بارسلونا آن‌ها را تجربه کنم. و اگر مجبور باشم یک بازی را انتخاب کنم که بیشترین اشتیاق را برای آن دارم، پاریس سان ژرمن را انتخاب می‌کنم، زیرا آن‌ها در حال حاضر بهترین تیم هستند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107225" target="_blank">📅 10:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19143fc835.mp4?token=W1Xha_oMDIQvQLzEPW-dUQT4EdntaW0kbo4b6SSyzDqJT-v5tM5NTha5v6KQ4nune4L968cW4e-vG_hP9-cTuHC6EoU0-zq4E6ZpBKPBT_K5Mj93yvqkHmDyxsSEA7H6iZ08N3HcGfn4W9S6gTsVGV5DHAuZA1B8KKwlHq9LYmhgatpAZSQA4VJjb6nCzRw8U1nvKwh9RYyTzK01xE7rwSfkz6ojRvu24F944cl9bhYWq4cH1vZQPGIk1BsyVAQQIJgZ4r9Ik0qjvsNfbHeBkuqc6ffnVpDJtztLt68siE5I0NpdH231QiuW1XyF-3ZMnQmr38xpVCb4fcop7M52Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19143fc835.mp4?token=W1Xha_oMDIQvQLzEPW-dUQT4EdntaW0kbo4b6SSyzDqJT-v5tM5NTha5v6KQ4nune4L968cW4e-vG_hP9-cTuHC6EoU0-zq4E6ZpBKPBT_K5Mj93yvqkHmDyxsSEA7H6iZ08N3HcGfn4W9S6gTsVGV5DHAuZA1B8KKwlHq9LYmhgatpAZSQA4VJjb6nCzRw8U1nvKwh9RYyTzK01xE7rwSfkz6ojRvu24F944cl9bhYWq4cH1vZQPGIk1BsyVAQQIJgZ4r9Ik0qjvsNfbHeBkuqc6ffnVpDJtztLt68siE5I0NpdH231QiuW1XyF-3ZMnQmr38xpVCb4fcop7M52Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌صحبت‌های بامزه ابوطالب‌حسینی رو برای دوستان خرج‌نکنتون بفرستید
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107224" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=dzcugutw7ezUKt6Orz3lWtCQnHcOUGjrCDP-Kmt0q7YdEsbIJ1SzGqG3Ci41DNJAPznOu-8h-OBG0VLqQTRqHJPN62G57ZrtHiQUM-JYx8M5vT2n71uT_WwU5GD9LMCS3DwTTo0k-0y2yNhnOXIefskMJjDDsu9otvVu6vCBw-RS2m1GOMA2uiMpmnvgJtQmX1WQa_iQeiJll1EP5KiXBSvcBZMhEQmHfoOLJxiC6e3JlLFVCmxybT2YNOs0BYqN70JkcLFLmLqW3Fbw3wt-FTBfNxAUuBf64v_OCREoLhvAv6XXOtWMxzzmmpBWKr96huowCoZH5THUsbiftF5fDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=dzcugutw7ezUKt6Orz3lWtCQnHcOUGjrCDP-Kmt0q7YdEsbIJ1SzGqG3Ci41DNJAPznOu-8h-OBG0VLqQTRqHJPN62G57ZrtHiQUM-JYx8M5vT2n71uT_WwU5GD9LMCS3DwTTo0k-0y2yNhnOXIefskMJjDDsu9otvVu6vCBw-RS2m1GOMA2uiMpmnvgJtQmX1WQa_iQeiJll1EP5KiXBSvcBZMhEQmHfoOLJxiC6e3JlLFVCmxybT2YNOs0BYqN70JkcLFLmLqW3Fbw3wt-FTBfNxAUuBf64v_OCREoLhvAv6XXOtWMxzzmmpBWKr96huowCoZH5THUsbiftF5fDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
و بشنوید از زندگی سخت دیومانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107223" target="_blank">📅 09:25 · 03 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
