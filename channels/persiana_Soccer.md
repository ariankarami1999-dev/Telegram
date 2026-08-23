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
<img src="https://cdn4.telesco.pe/file/SJsRXNsIPgfSqQloQ_Ckj9Ii9irng4E-hoZXXHAOM54h5Mqz_nJ1zTighorMC5wE8YNSjBJb2u2C_NKGV97HsjwyExmHD9SokS-ny0T1tMX4lGFa1YUHrlEI7YIaNxF7bxP6c_TQ5tbsNEvbDFnqbmNEkM3_vL6OI2LyfLJPt5M-K7PRc2svfdlZJrYehq_MDFIAW7njHsn6Rs4etvyNNn7r6VY91pyIsZOivTTCDUNHAIALHtfD4DFwOZQX2x09_TYqGZhJEZKGJtS6nstvnx7GAC8unI6B30fRzvZKhHl2CPbSwmawRUKOW3vkDD8OVsqZBek1UPPcfbpMwvSulQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 614K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 13:44:23</div>
<hr>

<div class="tg-post" id="msg-28304">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy48jQdp5YAe1uwZtr801UpApzssTASmninC4PjfOgBPmFVMBnT0j71g8nN8ePeZMXk-g_CL-YaEWyXna14TLt-OJYPCuuUPJ385OL5pdi3ifHr6XyV56tXfa8xuB12zPw_bXgyT6PUJZJfVt1rChVJymbnEqmcF3wSLSfApllkXQvZuvnJQY-k9agMXMZ0nyoGlT8HKXaxr2kq-Eg9dbd7RRUEH9cu0eP1ZGnQIdUXPsFKR7xtd8Cr6lPG68rZGnbPzFFURHEOh3Y7g_xiuoyVZA-lgasfzgzhlvQQY7-eLT7icJrZzJ_ooydAw9K4Wd0Bz3UFVhKtmypsa_Dha_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارلینگ‌هالند مهاجم نروژی منچسترسیتی موهای آیکونیکش رو اصلاح‌ کرد؛ الان خوبه یا قبلش؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/persiana_Soccer/28304" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28303">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBEJN3tB-uJl4Q3rU2mDRGwBAXqupXKP3sBgC7bJsHocJbFyP8XaN_k4W1FXFNdNPZ6UaYNM7KxJhLhez1rwX3lopbJEWsPr3-g4-PK0rvDRpHKJ6R1jRlI-Olm9_nU0Ji6AttXNdaWCX-XvA4gMfuuFYIaCeeNUuIa1snNM0Re4_rFbAVU_bD_W4tLZ_NfYmhH9Gow2qLlRFK_fBMEq6U43GldBsmVUIbNBS3ifFcATUHXcvrQoMYetQpoRgiMHxnxIo5g3AJTS6CbWHWRBJRtvqwY55JXIEU3b_FG_-doPnWg4Sw8OdUUd4-Xu44G0Zgux1Fr1HkUkAy1j88lIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛خبرنگاراماراتی در ادامه خبرش هم گفته مقصدبعدی محمدقربانی یکی‌از دوتیم تراکتور و پرسپولیسه و سران الوحده با هر دو تیم ایرانی برای فروش محمد قربانی در حال انجام مذاکرات هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/28303" target="_blank">📅 13:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28302">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=qp9gbTMsGumObmsh64S542MlPWnaI-5-0CLWoSKl77W9J17O5niBKRoYiIXOdMYQfR1tF4PETpNd64mZEYy7cYMRzGsPBRfSjxfx3TiHKLpECmNIG06GsxUCNpiu574U0aIkKaGLhhbPXCjt9WVtQ3m0WyRxWkney-diNsM1aHjiDUCdCgsVGd55uRZKiP3bg-Rfd6y6l1v5e8VUqIg6H56TPrhL-9WVIMv1lARfbBKDbrLo23tOZR_zkrJIhF9b82npU6qqhbuS0S07nMcRAYMCGrjT4mWKyt6P6CNIJNX6r7ceS_8n4liLyIEtBi8HBFAzaDknwSkXoen0rR8cmzQy5txK7c-6OVUSwnqFKHv4vWoC3sxfGrA8FGFNnfRewtDmImxstwypfPKL4lEtYebVHJmFNpUQ6MrEsYwd03YKWmbNm4-D8xdC82e0JwAXzNSqkuoSFxLaPtQLr1KMInnr1wbHN-RoYSZnAw19TVYZcpIhqsB6bldhUIq4J9AFxtXAx73E0JJyzfCEABVYZT9ZhOJaj-GSRf7U-Q5grtbqLjNtgiZkWucH4K3Kb2ch76UGs2j3kE2kqbR5Cw9r5lqhasmk-rXngUzPt2UMpvh1bbLhJQFsnlY7TPN3onCr7ZPsy-AdoCs7I7vEvN4dewi5HuQWvto2zKAbRg-0B2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=qp9gbTMsGumObmsh64S542MlPWnaI-5-0CLWoSKl77W9J17O5niBKRoYiIXOdMYQfR1tF4PETpNd64mZEYy7cYMRzGsPBRfSjxfx3TiHKLpECmNIG06GsxUCNpiu574U0aIkKaGLhhbPXCjt9WVtQ3m0WyRxWkney-diNsM1aHjiDUCdCgsVGd55uRZKiP3bg-Rfd6y6l1v5e8VUqIg6H56TPrhL-9WVIMv1lARfbBKDbrLo23tOZR_zkrJIhF9b82npU6qqhbuS0S07nMcRAYMCGrjT4mWKyt6P6CNIJNX6r7ceS_8n4liLyIEtBi8HBFAzaDknwSkXoen0rR8cmzQy5txK7c-6OVUSwnqFKHv4vWoC3sxfGrA8FGFNnfRewtDmImxstwypfPKL4lEtYebVHJmFNpUQ6MrEsYwd03YKWmbNm4-D8xdC82e0JwAXzNSqkuoSFxLaPtQLr1KMInnr1wbHN-RoYSZnAw19TVYZcpIhqsB6bldhUIq4J9AFxtXAx73E0JJyzfCEABVYZT9ZhOJaj-GSRf7U-Q5grtbqLjNtgiZkWucH4K3Kb2ch76UGs2j3kE2kqbR5Cw9r5lqhasmk-rXngUzPt2UMpvh1bbLhJQFsnlY7TPN3onCr7ZPsy-AdoCs7I7vEvN4dewi5HuQWvto2zKAbRg-0B2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
به‌بهانه‌دیدار امشب‌دوتیم استقلال - سپاهان یادی کنیم از تقابل فوق‌العاده جذاب این دو تیم در شهریور ماه 89 که هفت گل تماشایی در برداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/28302" target="_blank">📅 12:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28301">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=jfIWPkl-5oUZiG-bKvCTGNCIqFExmcht_ugAl8YclhXFiLE3VizaHXO7hN6ZDXvDBlgBWVFMiLmAaWn8qG9RY4xfNKS6PWN-oa1wKVnmu31ePWH8i-hD-bGAbv77E_0KddEMEBqCIkpFMQs9qpuNMtWiVU2QlFTzUxK-r2M5UuYQDqFJ3PaHArnINHMYf0fcmLtDxzusuzTtIKY7F4Deo2F6yoPfQu-0W6geSHTDR2gM10JC0vKCPT8n46owqi4hy__ldJkKdu3feWY89yeaRJJ5q-BKUsH4W1NEYVaJXRJodPjuHJOzFfdL5wUalvdyWuQtBT2eH1BxZaBgAyaf9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=jfIWPkl-5oUZiG-bKvCTGNCIqFExmcht_ugAl8YclhXFiLE3VizaHXO7hN6ZDXvDBlgBWVFMiLmAaWn8qG9RY4xfNKS6PWN-oa1wKVnmu31ePWH8i-hD-bGAbv77E_0KddEMEBqCIkpFMQs9qpuNMtWiVU2QlFTzUxK-r2M5UuYQDqFJ3PaHArnINHMYf0fcmLtDxzusuzTtIKY7F4Deo2F6yoPfQu-0W6geSHTDR2gM10JC0vKCPT8n46owqi4hy__ldJkKdu3feWY89yeaRJJ5q-BKUsH4W1NEYVaJXRJodPjuHJOzFfdL5wUalvdyWuQtBT2eH1BxZaBgAyaf9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لالیگا|برد سخت و نفس گیر شاگردان مورینیو در ایستگاه نخست با گلزنی کارلوس اسپی.
🟠
اسپانیول
1️⃣
-
2️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/28301" target="_blank">📅 12:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28300">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3pY4HGKUcJ2iszyfi_kULpp4uUk0o631-XM2vUcPnHiG18wvTJuwydN7gKXt0ttMBVorsiQykgv3d1bd7i6Fcd3ltZGDyBp6fTn7sqbhAa-sPVGI37EM_c_mAgZvZQRVm0_Oe0CW2MS3lAM1hxkySgPfTB7wLRP8tcZbk84_UFbSAeK8tSRKXjlcWoylajqJNKz1grv7TocLZgZIdLlzTJ9EEQVu55lP55WOY4t9-i_blGENjY5w64cR5aKvgl5ITJUhTRIpml3g99JEVdTbwf8Mo1fnAEkCZjD8LaUVbBi7Xkfyelt8VHJo5t0EnvhS0TghQJPZIyG5bASCPnRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/28300" target="_blank">📅 12:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28299">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGogk1Z_HmB1Rk9pQxSrgqpbsR3x7cq8fW1ZycD03oIWc8quK_TmSmeryB3yBP0xRHy7q_eiNlVckg0ov-Z6KBDbh0xMEB1BshnXt31q2o_5DvNR9NPLEPqxo2PP1U94nLWxxvjS1UxytJRFAU6il1QHGFO69yVgxWPK2KEzIdBbqg41WL3VDr2TdfQ7XCUchrsO0XHspJMdR3BAzqyk1o72tk6hq-1ev-FFD5HmUr1ePYrLk5A9DEKto9kOue4ybJ7LmDXn1IMjsfNr-7DyWIHhfTLYscZejDotuk98guOgfb1eQ93GDaZv34Or_iEtv7wDv_nxKPMeDrD7EAbdvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
داداشی‌های‌فوتبال ایران؟! پوستر دو باشگاه استقلال و سپاهان برای بازی‌حساس فردا شب دو تیم که شبیه به هم طراحی و منتشر شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/28299" target="_blank">📅 11:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28298">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBAqx9EscWZhDEVr1oHI4sfKrgcrkdxXRMhZR76K6J_OzUJYknIonb2ahyMjFMtw9u4TzbRkAjlXDJByIQVWQvKwdmoQZC7wbDqnQt5Oth0SWM3uhBo6dGsTEEp0anzzTI-p0Cbn3OMPhgYwVv8Cp_g0RdO6WbLg_cbDafbmbNeNpznNQ2etUzH0S_LNJV9-0GOsklQ8JKC8vmxiBhV5vEn_7tfHYoNrKpPofiOjTYJHgU-qV5Xr3WIV9oso8fPOdsV7jnGSDjQnfvj7vyouwfzIdmTuCepW3DOI0J9lSzq5D4nU-va1WVmgvEUFchMt4sSQSjKGoe9fls2P6WSrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه‌تقابل‌های دوتیم سپاهان
🆚
استقلال!
‼️
این دو تیم تا امروز ۸۴ تقابل رسمی داشته‌اند که سهم سپاهان ۳۲ برد و سهم استقلال ۳۲ برد بوده. ۲۰ دیدار از تقابل‌ های این دو تیم نیز با تساوی به پایان رسیده است. درتقابل‌های لیگ برتری سپاهان ۱۷ برد و استقلال ۱۸ برد…</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/28298" target="_blank">📅 11:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28297">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2XLQ9HZo731IoFKhg2587QtKpLlBnM1s33ygpCZWu2LkTGy2HwPrSUc1bqiq7X7vYqcJnoIXE3qujE9_UNVSuc74b0j9JuKfsxpltYCtUXvasFHdFe36vPCf-SCRdPj4qa00MxXdiPJkNJuaVKM-iulOOwKGlAol2C2NosPlrsjvGltTEimEiZs-k_FNPEFPatRcljnNIk1N4LvjQJ9rRjfaQTQs7VXbtNM3gvho-QPCndYJN1gUyo0mMvZEiiMXnFl5ehD5y65qSKsrXa2icE6Idl-n-Ph0Uon6Oo4ApxTHQxqhy4qXfv7pJK5cV1BZdCbk3Wc-fMAIxNkEPnwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/28297" target="_blank">📅 10:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28296">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7MlxUbEDATZs4nITfRBiSt1yfKoi0MkmaOBh7pVBGfLg2ZrEu34Y4qOeTksp1IYITX63lIweo6LzHHRAG7f-HpGdolAoWzIhDVFhXJtzGL-efYBkBMIIoQwaMABrnf8s29AZlRo7TKpnfpnpf0hg5y9KdhCalJr4kPZMD_DgpAZ6OV14RC4ttCOOyn67nZlSWiKhsHi7W-YB16DPqGs9vZRK0BIo0kkc1MVZk8PltSJZPqp0xp1jIXSJWwZSbYzHZ6YjWxRbXd_iYlRPKlvHHp3aU8q4XWiiNP28S8MtYM5mWnz9BQ9MU6-V_FOH_EooJUuLSA82MeHDz4cEYS5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/28296" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28295">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNyR_58ocjI5jwdJBQU1bKSSjkPVS8O6qZVmrbDJcE6eBBPtxKc5UtRqBb460X3bysubkV0Y5lhKwTLrT44C6ldgAcgkG5xmwgaUZMsSp1tTGuerd63xmeoLywtrdo1y7Lpm5sJodfRPn9JHBA4NZe8BHLrFNzamjshy1fXtL8xO7QqummLy6UuE20eoWX4nXB8VD5Pf7FCAUGCvnBnC4jnWa5dkY7Ks1CVP_Gu5EdvwNTjZzigsINjNvWQNDVoTgXpAivqzyonUGTuFHnYC-KA7XJMJku0vmFukEDrWf6sWYPMbvn9PnbyqFukrK0gjshT2k9uE1aHOjBCsuSyoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در سال ۲۰۲۳ بود که لیونل مسی از یک رستوران درمیامی ۸ پیتزاسفارش‌داد. صاحب رستوران خودش سفارش را برای مسی برد و از روی احترام به کاپیتان تیم ملی آرژانتین، حاضر نشد هزینه‌ای از او دریافت کند.  اما ماجرا پیتزا فروشی همین‌جا تمام نشد!
‼️
چند ساعت بعد مسی یک اسـتوری از پیتزا با نام رستوران دراینستا منتشر کرد و همین استوری، باعث شد، به یک‌باره‌افرادزیادی به سمت پیـج پیتزا فروشی هجوم بیاورند. تعداد فالورهای‌رستوران‌که‌حدود شش هزار نفر بود، در مدت کوتاهی به بیش از ۱۰۰ هزار نفر رسید و این‌پیتزافروشی خیلی‌زود برسر زبان‌ها افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/28295" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28294">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDOULZSo5i5qRfPNq9a7pea5vcAe7KZKr2K_ykll7EVzo2w7-ff4xVpOVJCRoRRcTo_8hgtfyKvA6UnuofjVATh8RFcxwxv48mqo6tUIQAZ6gBA3Q2WpmyiwiFYgtbu0E2kda9-13P4aLVkl5fHSPs9n9RI1QQu_rMjtqF5h5XfFFLubODilRy3xLVRO5l_psGcrybE4wlTTIIZ3_TEyiQgFfbT04KmRYqJdEGcuUcHVpBDpDHYDlDsdHPByNqKIFYNwl0X1LfcuVHiRuqpQ9xGmxBKlYUu673k_cemxUpjzFYmIazn8XHI0OnYwkvhsk8RXqrgEk4hbu7jnq3RQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بدنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
؛
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/28294" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28292">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=q-5rbmS1I4MwBTNrPhEKHz8kBhVkwWISZtg71IaN3B_5yxpc-HJWfQ9CadAK37bp9M4MZUhyPexX1ViNuo3RgPdO8p63K04Ug83rL3y6G11TZ3fOXLjQ9mtnnfIabJ8yJYoRHCXsD_7nxCb-SZAGaA0T1iqQ-Ualq5XzEyHVenhwdSROsuTPM7ADD68ne5i2ek0xXG0v85xyhXhRuF-j4mStL7AyYygFzWo-mbaMnJaPV-hsYQm_-iy6AeisnLa3ijjZMczGO06o7o-QR2ISE7ojZIT_pqsjdb1v7oGwWuMYN0fi-OVX63G3HhXbJoR8zjUsUYZ5jATB4wHNTqGW5J_vPxGOcAAEiiZV9F4XxgehYmle7SCFznwLzuisDBl82gjorjab72sj29sbM58ceYvnnSQfIwN8Pljyv4zD0X3j7qXE6MVe64CG5CXyNvhI37Rc11B8glSoONQOeFPbCt1fH7Skpdb4bYY0YB8ICh_jqiREcvKurd0uTUM32Pv_hLU70AhEKlSTf0of0VBrc6TXHK_l_jYLYEe0iqulvTcviJjd6YCDvQoMLH3naqbNJ6LfjMLFZjNUFDx1_mJaXlP7hjL6z_kF2UZZMo4hxe5_oSIl2kby2RtIvt_eMDVPb2C7me2qe7xRTyiohWbGFL3CY6of3cOGlRyeecJNTDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=q-5rbmS1I4MwBTNrPhEKHz8kBhVkwWISZtg71IaN3B_5yxpc-HJWfQ9CadAK37bp9M4MZUhyPexX1ViNuo3RgPdO8p63K04Ug83rL3y6G11TZ3fOXLjQ9mtnnfIabJ8yJYoRHCXsD_7nxCb-SZAGaA0T1iqQ-Ualq5XzEyHVenhwdSROsuTPM7ADD68ne5i2ek0xXG0v85xyhXhRuF-j4mStL7AyYygFzWo-mbaMnJaPV-hsYQm_-iy6AeisnLa3ijjZMczGO06o7o-QR2ISE7ojZIT_pqsjdb1v7oGwWuMYN0fi-OVX63G3HhXbJoR8zjUsUYZ5jATB4wHNTqGW5J_vPxGOcAAEiiZV9F4XxgehYmle7SCFznwLzuisDBl82gjorjab72sj29sbM58ceYvnnSQfIwN8Pljyv4zD0X3j7qXE6MVe64CG5CXyNvhI37Rc11B8glSoONQOeFPbCt1fH7Skpdb4bYY0YB8ICh_jqiREcvKurd0uTUM32Pv_hLU70AhEKlSTf0of0VBrc6TXHK_l_jYLYEe0iqulvTcviJjd6YCDvQoMLH3naqbNJ6LfjMLFZjNUFDx1_mJaXlP7hjL6z_kF2UZZMo4hxe5_oSIl2kby2RtIvt_eMDVPb2C7me2qe7xRTyiohWbGFL3CY6of3cOGlRyeecJNTDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/28292" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28291">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqfxIhP2lb0HAzwE5AWgE3jUR62rEuqDy9BScZQueZZyfFHKG-Y78An1vQw1QrIh3EOHPhDDI_76nQWS5VO6pKxosOrl1OYTWbksZhdQ6nF6K2URmnljaV_MGadIS7lE5hljL3r5_Y7awbX8Wi2OPnplzvfEbhoWSroP0dm5LRrxE-_CaqEAyF6VrRj0DkDgSNtt9xJoLaqGkCWIyY6PPVyd1GAkmEZaj4wVjb7Y_e-2NkL9McuG6ko0cDUgfIZaIVGiSMhGnJyIgJ4HYx0og-8wkD8BwkpigKJsXcsfncH2rSU25VdB33-_mI5t5HQi8MbIVO6dRPzzOumk6DqFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/persiana_Soccer/28291" target="_blank">📅 09:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28290">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=abdup8E7E4_1hI_W38-kz-57GsErQQ51Lk9bG8ApTK9vVGD8UKqZZR48dscI69baxhOnOrZPndPiZV1iJcMpkeK50FXVpwwsh12gp6dPwsP-S1svHImBswHrgwjI4awF8two74emXLgrVmB-IRJBQJImW2L54TuAaoAbOHV651q_2ehj23xaDk1_-tZYoeQ-i5DUEBgD8nAUn_Mb3BommUjWoy_tWfTJt_ZmPYi_hpAh1PptMjkr_Eg78IW9Cug0V5RivkLl_cOy7-diuUGBvzwSsyDmFvVxZ_eH2pXnmpVLH1UJlSWuRSWM3Ja-9dDtLeX1piPfygb-2eSuz-Uaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=abdup8E7E4_1hI_W38-kz-57GsErQQ51Lk9bG8ApTK9vVGD8UKqZZR48dscI69baxhOnOrZPndPiZV1iJcMpkeK50FXVpwwsh12gp6dPwsP-S1svHImBswHrgwjI4awF8two74emXLgrVmB-IRJBQJImW2L54TuAaoAbOHV651q_2ehj23xaDk1_-tZYoeQ-i5DUEBgD8nAUn_Mb3BommUjWoy_tWfTJt_ZmPYi_hpAh1PptMjkr_Eg78IW9Cug0V5RivkLl_cOy7-diuUGBvzwSsyDmFvVxZ_eH2pXnmpVLH1UJlSWuRSWM3Ja-9dDtLeX1piPfygb-2eSuz-Uaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوم بالارد ستاره بریستول‌سیتی رور گذشته این سوپرگل پشم‌ریزون رو در دقیقه 85 به بیرمنگام زد. گلی که اولین گل رسمی او برای بریستول و نخستین گلش‌درچمپیونشیپ‌بود و خیلی زود به‌عنوان یکی از مدعیان گل فصل و حتی جایزه پوشکاش مطرح شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/28290" target="_blank">📅 09:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28289">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">📊
🇵🇹
🤩
تفکیک‌گل‌‌های‌زده کریس رونالدو و لیونل مسی درکل دوران‌حرفه‌ایش براساس باشگاه‌هاشون.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/28289" target="_blank">📅 09:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28288">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d382486c.mp4?token=nW2jdlsf7pbTp6r3AyifS83uqhXcIyMSI6uZrCG4Xgv9MmOfW0QTAogPO99dQwfWX7wVTp5EFTKSmFHXZVFTMMVOPVnSAU9TkujK84If-JKznfs-x3I2ufmsZyXxFK2oKzc3nVCgCYNiMlxlARcnWyy73qnYYr_3rd96-B0WV2fWmznX2vK0LD_riU9oirfLNHE7m76SuCy_ufplQHJOPlLfMJxM59yFBDQa8VCxtxLw7pqOx3fuyiCz7lBgHMrtd5vNNbP4Wx9t5h6Uj9fcRe8hOFBK392RMyPMNfz86Hq_rofsS9Ms6rq4mun4S69sdli4WpbA1KQMF8e8oWOxoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d382486c.mp4?token=nW2jdlsf7pbTp6r3AyifS83uqhXcIyMSI6uZrCG4Xgv9MmOfW0QTAogPO99dQwfWX7wVTp5EFTKSmFHXZVFTMMVOPVnSAU9TkujK84If-JKznfs-x3I2ufmsZyXxFK2oKzc3nVCgCYNiMlxlARcnWyy73qnYYr_3rd96-B0WV2fWmznX2vK0LD_riU9oirfLNHE7m76SuCy_ufplQHJOPlLfMJxM59yFBDQa8VCxtxLw7pqOx3fuyiCz7lBgHMrtd5vNNbP4Wx9t5h6Uj9fcRe8hOFBK392RMyPMNfz86Hq_rofsS9Ms6rq4mun4S69sdli4WpbA1KQMF8e8oWOxoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/28288" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28287">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYwR69UMZErj3HnR8I2eC9HYKQ-y1N5qBF-tRunNh29HPaGLM6-RTJtpXhZ_XfdT14yFC4aaQweeZGCntefEOcm1-k8g9DdDeoEszN5_vgvOJ42kNzvV8_-Q3qbB1kYdOyCvrv_j5qhKqnf1lJnTnAxgOzkSQJEeZHh7UxR8G_DZiwjAkQKyUwdt2Y1T_nELdfsTLBEfs7O6wtm3-2HQ9XpvJxGWdnzpm7qj-mUigFMTLOP9COIOyJ74m5GXVJ_wPZ8u_rs_AZ9_Kqv-R09Pjcuxi8oUViZLUKwF-QL3eXjhNd2ZvhJdjaKf6z5E1l7gIf6lcvueE6daQ2ZWCGLpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ مدیربرنامه‌ های‌ یحیی گلمحمدی در روزهای اخیر نشست‌هایی با مدیران باشگاه سپاهان برای پیوستن احتمالی یحیی گلمحمدی به جمع طلایی‌پوشان زاینده رود درصورت شکست سپاهان در بازی فردا مقابل استقلال داشته. درصورتیکه توافقات‌نهایی‌بین‌نماینده…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/28287" target="_blank">📅 01:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28285">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZfaCD7RmXgcgeiW0Gh6O34wcYOxmlbMtMFQOROX9g4BJCucpX83XTq6iJjM2tTWXXkRoyFx57x2KQ2Lp0ASVCY1d4VYx-Zeh6Ecb_6xCZUcdSaVQghAZsOCECpkeqsP5ii1oOA3clWl3W7tDKu51jqZwR2fcbVerRU0QVjKSdDiHSeidRR9RkgZmnBOIj3xDV-WH3kJsyhwGZ3Vw_MQwilESprogBkDZLNFrj3mZs_0UzgKaT2X3OKQ8613AlgWh0KezYsV79nF9GzoiAqk34GppTfrNpUtx6JBs1091QTSuK-AAfBiPNU7Ki7w817QEoG_isbNu7ELP7wk0d9xiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از تقابل استقلال و سپاهان درهفته‌سوم‌لیگ‌تارویارویی شاگردان فلیک برابر الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/28285" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28284">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrIAxheHRpON62LjsXzJP1lWYUcHjKy--_c1tpwpRFijYJChZpp2TMgu7DRXensSzfTsxSuUz3r8iuOL9qkx1BVkZgnUOynsd37emnyuG-cliID-txmfFiJ-N6pXzzFMn1lG53NK19uMZECQRHUm9XCgLBE1P729m08h3FNjtJfjwIPA8sgryOQWJnTpi7wMEo_q0GfuPQPg7bKcn-HucA7auOSBcHTQlHSRX67HJCZ4QNcHfTlkos42vgUnUnWTVIMGPNHNvpZPslr3djv8NCAnqU-kDHAx1fhwXGVm7OCuYF8DkcSh71J-ckiFCF9czKolgMAEExoWcLGYKN5Nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌ دیروز؛
بردارزشمند رئالی‌ها با گل اسپی تازه‌وارد و سومین‌باخت پیاپی دورتموند مقابل شاگردان کمپانی این بازی در مسابقه سوپرکاپ آلمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/28284" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28282">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUP1alk3GGHLnvuABQJ7d5eOer7O043c4sn3vviGO7FY9n5hoBVsCN7vdX1UzxSXZ_WgKep53ZhVuz5UczWgQ0AEFrD6iS7TM1QVwlo7ZPfcTuPhiUwFDfY-Sl2NQ7wzqt5EC3ZkEaxuKGn48UPF4plELfl7shqLXJsO4zf7ZWRXzhiYVZPMRMHu4VhMxxuItX1AimGuH8Elz7zPdFegfsKG51tlm60Xb_8c-PfgPRVKUpYZE34JCoAi_ImIAep2xkuTKPEAO76G2cGxGusmZhoxlQuFH1JJOphNkPEId0Q2RVjkTnChDCeSTRE9yuVU-8MV4zX_oxkSRmxFr3PMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب با اسپانیول؛ ساعت 23 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28282" target="_blank">📅 00:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28281">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZoC-Me01-4QLmn__5YSF5bZCviYXDvcM-Zu2qbk537ZwqLxPsUOspLSYVsXxPctp9dnSmDCOdM7XDzk8Q6Itsao0c5UNvHJK1UVoUtTN9NpgKWDFLpgCuuC482AIXMRe2app2e1eNMSikA-uJg1MJqbV6xEXJbI51OULpz_ZsjaakVwSQCpcpFSFWdR23somySkhKN8mChQojKyKDyLxlm7EsSW8glJ0W3bvE3rprLMhKcNkwwcZYHS3Elg6AmO0NYXfx9dh-Gm-b6uqbH-oyl8Nx7W5xjkxb9l8K7hI-RYG5pQ89fHG_STghFmuVyjkPEQxvQi_kfX2alc3k9ANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگردیم به روزی که هواداران تیم ملی کلمبیا رو سرو صورت خونواده داروین نونیز مشروب ریختن و اذیتشون‌کردن داروین هم برای دفاع از خونوادش یه تنه زد به قلب هوادارای کلمبیا و باهاشون درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/28281" target="_blank">📅 00:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtrqYmM168vMkHZzhWQEzlkkMUyv-Tg4_Aivvbr-W4RSZWsy06teTtTmskeJHV6lxS7AHrmI7SGOxvkJvwpf9Qbk0SQDASy-L626M1GAyXxIDHteGW_2G-jdY0i0XD3vgwPG0JB4P3WeQpJUOv0NlsN6WjDmqCK2kUwHkGaep_PKMKJiM0edlauKtdHj843TZrhmTxZze67ybbTCs7Cdro30gSFTF-XeHsM5mrM3p2-MAZGHxV-I4gnZHMbhGxxJbuaD6r7JUd9w-2w3OwXEYe7j4BdRQzaXgjTFFsVGWdJdK5yNdDU4xgovXqI320JpHa8LITWDfPhbaViph7B9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R39QBp56N1m4oOQHzeynK676znbn5nebagpsoVxF5Kh7b2u7cwgP8WnIF_KqK8CcuMsUPvPg08K0pN1VtQ-zIA0lpUJIkPw-xEpH7PGcMqi0o3NRjTqiG91N_EaQimA56wl4D-h4Hzs6dOoi_Z4OhWOrR1ZEE9nEWRfN2BryBnnUtzGG_H_mGTZ3YpQokkxnuJ_BisGKq3PhJGTNWOg4hxI-H9M43WP8FHs-K8ry4H5YgSDVntSRe_cea8em3apVqMrQpR7oFCllZj_03yhxZEpFpACvI7i28Xf1i8W3tgK4GjuBRKt9gnwdNKqgGmVaGwP8xmhiTiIJ3xkwpJIJjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/28279" target="_blank">📅 00:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmq8kkV2A__gAAMMtBeKWGDb5SZ9dbUiil2erFLc3Y_kdwwbxwi4_YBVutpVGATR36obSujQblS1yPoOJxHrpiaCvuTKiuJmf01vPZCQqc38bnX_sAfjtINH9twTkuxsAdOB7ouuRlfjxb50VX17e8HmhCsa2vZBWGPqHioFGAY5JD7wgaSe-ELlK6arYLGcZxbaMFYhuep-KXBlxq-0KaK86lEyrRN3LHZzk1FvhoGRWWX9kgarAb2ZaLnDW7Aoq5H1qGZBBiuF7stuAXIdoTTOk5dXRb8xsm77u9mD5q5r4tMOJDLoDwPFho3zpWFezqkLxQO06MixvMKWgiy9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ احتمال‌دارد یحیی گلمحمدی بزودی‌ازهدایت دهوک عراق استعفا بدهد و به لیگ برتر باز گردد. بوی یحیی در اصفهان می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28278" target="_blank">📅 00:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMYRrrOSNeLC5exBJ7XEbS80dbfrlhXYs7agz0l0l8m_ToEetlQ02oy9vdwuAI72VxrZtvMe5i7LkC-8uKeP7zj6lFEhBBlkiLQPat8n4LIq-Bj-0dBw85ASfjm5-lMGfXEMzmJJjM8JUkjess7A48X25cKeHMNEZRfLFcaupVQl7gOdUuwnl59FUicwLIMqsPcUaYqRDd5AwUNrsGMBo_b0l48T1v8atJ4oicJrayXXpH0T5m0LeYXgZKSn8X6cbY6Z1J4K4l0uRobRRiq12S51CG3lFkMnToD0whXS1ASnFyxfBTTKsgxV8jCKG9OOxjsP0Yh03SyYdJnLkKzfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپر کاپ آلمان؛
قهرمانی باواریایی‌ ها پیش از شروع‌فصل‌جدید بابرتری‌مقابل زنبورها در سوپرکاپ؛ کمپانی فصل شروع نشده اولین جام رو گرفت.
🔴
بایرن مونیخ
2️⃣
-
1️⃣
بورسیا دورتموند
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28277" target="_blank">📅 23:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt1KPT9fdZ3zufcW07VSdJSe0fa9TXiaQQxvNxcYL8koCOSYXhkyrhedxo0iLfW9XYv9n0lFHysWdDl0oQLh1toToUCjupcmfK4NRiZsvVjVA4p_cJVbBUXkQuLNauYmpIOxOIlmx0SXX2_eflCfmyEKiiyoh5OJNO36A0_APZaDxaeVHXBxeEW20z8wprWg_2lR2cuczV8NbUa7FoR3qq0LUG9lNRNFFA3YxeGUDyWqLbS-G9hsDeLabjxZHjj1RHjGiz9BOQ4gJngfIaDF8VONtQCNmVNrtMCIZOh00Le2TZIDESqKt-YP2VACwq6el3TzYngj2cVKGyuDgGpx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛ تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28276" target="_blank">📅 23:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBC1KnB2FW5dgjd7k-W3zwhyJJ2VaqexWod2rk2pmg2W8f1bTTbyMhE8YpnyJexTYTHc1UloM107sj9woxQOHKM5A_oXm2H84CuSnfCNOJZvanS47CgJbpfo1hClqAgN6wy-mraJLYoWP9CmS1IRsl6HoA0fzHWlfCvCO_qFxfRuib52tJtWCWVs1FIAbHQ_zHqKir8fSqKekcJnM0j8HAQ54GYWZyuNUDq2iCZW2ORxqw4KG3fbqp1vJfvz81WdmZJnEXjXa6pdCStjSZkHkWH-8QDGdxfefx_IWJnN5XtHOc1y3NlfjuSatc9LytdTnsQqsVzxFVsFHZY7nI1eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛
تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/28275" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=eZ3N0V5aEVHKADlHrZuYTLYeGNyjNQyOXE8gjY1OL7h_5Cx7Bo-562VTMCXrMfXpDdU8n6E13Bz4bzxUXyVrQot4KWLfjxMa7bTMm03Tw-8-5sBXIV1ZavqH6H1o8dp-ZOr_x-WIrkGnNaXAe-oXzYu4DZxc-awiC5wBdpAGWOEWPQXJ-626klrs1DOQbcn9nvUw4jP4tRWE9x8S61TjxqAXyn_BJaT9Njnx2YrbZsajb5AahDPwuKIFKwa7aZtVitKbulUp6swWV9RL6WAIg0MteWa7tHzIsltbu_w0ghhAK4y8waHhotxXvBOf5cAeIDx0B0LtvlSULdaRsPEhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=eZ3N0V5aEVHKADlHrZuYTLYeGNyjNQyOXE8gjY1OL7h_5Cx7Bo-562VTMCXrMfXpDdU8n6E13Bz4bzxUXyVrQot4KWLfjxMa7bTMm03Tw-8-5sBXIV1ZavqH6H1o8dp-ZOr_x-WIrkGnNaXAe-oXzYu4DZxc-awiC5wBdpAGWOEWPQXJ-626klrs1DOQbcn9nvUw4jP4tRWE9x8S61TjxqAXyn_BJaT9Njnx2YrbZsajb5AahDPwuKIFKwa7aZtVitKbulUp6swWV9RL6WAIg0MteWa7tHzIsltbu_w0ghhAK4y8waHhotxXvBOf5cAeIDx0B0LtvlSULdaRsPEhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اون‌هوادارمنچستریونایتد که قول داده بود تا منچستر 5 تا بازی پشت‌هم نبره موهاشو کوتاه نمیکنه رو یادتون میاد؟خواستم‌بدونید امروز 683مین روزیه که موهاش رو اصلا کوتاه نکرده و این شکلی شده:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28274" target="_blank">📅 23:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix9Wf5n6OCVWupQzPNhArK1uWKzyHGkoJqhSa55vQLFE6BCCe2Btu8HkHI_G-uFxP2u0TBpTB-0JtiMdkv2fiBUVX7lF6KhoW6jt9ezRXgUWBatbcEkgY_ZhfDYq9AibwYA-MukBxYhx9hIlNJR5qefbtSlzm1h84JHCwcIQSWdmOZvoVvLlVsw9bEQCbVofgWX_Zk_k_HI56HHpDKP4k02cAweQLjwT9R5SmF_gnXxXmg1bOBAr5bXp4tIBh9fFEkfUyR10PBjrywvoGJlC9MQggrhEfXRALnGzt_jBR7S0SjRvZI8W5QFM14LuPEVQVqgAwPJiIMCeCE4i1F48Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
العازی‌خبرنگاراسپورت‌امارات: محمد قربانی دراین پنجره‌از تیم‌الوحده‌امارات جدا خواهد شد. این باشگاه‌بزودی‌ازپیونتک و اوندر دو خرید خارجی خود رونمایی خواهد کرد و سهمیه‌‌های خارجی این باشگاه تکمیل خواهد شد و محمد قربانی رفتنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28273" target="_blank">📅 22:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=bai6rhg02jRBK0zDdZl-ffY2pbJ6AZqU8R0eMNovwSCdIeXQPeDMbNhADYReUg1pEZ88X_ST-M8U8Mn8YBH71Zpr-9SBmqQ-CS4tolWXU5lPB_KdXZgc0e0escL36-YduoRgbKs0B5njT2sAzZ19n0hc-brLKu_J18GOpdSpduFpSIq6NBdz2k1BGlfxC1X8tN73bp1PSGPAKkiWAIpWfPYTT1-_AqFY0MdecAPYL60ZYayvxxSUmCW_p65lD2eOC1t8vpIbm-WcK5P_7CooFLcppsc7uSHjmkbURP7gGjLZ5sdmrrdD06Wv6SHZ-6mnPkO5VuzAKizkEfoM19EoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=bai6rhg02jRBK0zDdZl-ffY2pbJ6AZqU8R0eMNovwSCdIeXQPeDMbNhADYReUg1pEZ88X_ST-M8U8Mn8YBH71Zpr-9SBmqQ-CS4tolWXU5lPB_KdXZgc0e0escL36-YduoRgbKs0B5njT2sAzZ19n0hc-brLKu_J18GOpdSpduFpSIq6NBdz2k1BGlfxC1X8tN73bp1PSGPAKkiWAIpWfPYTT1-_AqFY0MdecAPYL60ZYayvxxSUmCW_p65lD2eOC1t8vpIbm-WcK5P_7CooFLcppsc7uSHjmkbURP7gGjLZ5sdmrrdD06Wv6SHZ-6mnPkO5VuzAKizkEfoM19EoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/28272" target="_blank">📅 22:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28271">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=C8C62wVazY03K_e92kJD51B4P8QtSoSpz0Jdpe9Z0Y2kmQxfFuPO1Ov4RRKv7gLK9OdQvH9m33WZCBeDPAJHwc3kiUEkarSkxeeCPe2Jhfj4CvLoR4S9MlBMsmLk1uPFw0m-ZcfqsUjogYfIRmVUbcSxSzIsiDnAUoqLNwWUrA-MkOBbKtH7OgKvXe0NIPtObcVKj-t9ESadlJb1WdWGzTGSSL5nJu7MMpEqPrPDgSRK9pZWXRTFNuHmCSvtSlacbIhC1NOYEE5aLj34Ir61Aq7HTmBmRxcCcKtPie9h1metg3K8K2iU_SyvP4nDI5jxrqhyzCOf4ZMTtZuKbEZyeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=C8C62wVazY03K_e92kJD51B4P8QtSoSpz0Jdpe9Z0Y2kmQxfFuPO1Ov4RRKv7gLK9OdQvH9m33WZCBeDPAJHwc3kiUEkarSkxeeCPe2Jhfj4CvLoR4S9MlBMsmLk1uPFw0m-ZcfqsUjogYfIRmVUbcSxSzIsiDnAUoqLNwWUrA-MkOBbKtH7OgKvXe0NIPtObcVKj-t9ESadlJb1WdWGzTGSSL5nJu7MMpEqPrPDgSRK9pZWXRTFNuHmCSvtSlacbIhC1NOYEE5aLj34Ir61Aq7HTmBmRxcCcKtPie9h1metg3K8K2iU_SyvP4nDI5jxrqhyzCOf4ZMTtZuKbEZyeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
سوپرگل دیدنی امیرحسین جولانی در بازی این هفته فولاد مقابل شمس آذر به سبک تونی کروس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28271" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28270">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28270" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESDm8lUyFnv-ZIF5O3dX-lxk8vgkZWWTplFpMJo1hS5DeLeSLNGVAbvCtK0F1cOUQUPrP0lwxWo7kesxt5hH107tIy9OGk64k6b1LrvAfRJcddxhg1kHizw_WOG_Nv0P1iOx1uo6521Sp8wNjsK5NQ7l48-MNZjDPhDgXGYlyQ6O60Zgoe-yTlfqKqa9_cpGEnqL29vu5zIiLtMlbMvno4_12ZcUNwd0j3ETeFKLeN2YvQmiMxKWTYBUHM-a5P78Tzl-mHTq1X4ut-t9pLff9b0szY2HHEmgA_VjC2eDWEdkJPQhN7ZMgLoXWnGfaEX_x7gsNXQjbSIN3_uk2lvlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWo-FHzSbO1wyfYMRBZNHEA1fPhw5OEy2IydHrNrWz9o3HRrcMJ8FMfPYvvNOzhN2CgIDhBiRhY_RJ3hSjr7W_Pj3PsCcG535ko41yGkCqKEwcMMeahjDvqRzMPoUSkGDYCJZpH3vrZ62THIOJFxJpygp_5Q7nIkr-iIcKcJAEJpY3XpdHt-ZBkLNCMJL2ggRI1tU4MLLAoRTZmYgBaz-xTtyF4VawX1xfqcx2BB9qK7ohbmhou1NTePcbqMVMeUmZHoJxUahvQllTNi-NLiIUmwak4jcMCtVJSnC49bFsS9W210ntQ-sVkwBqXBhUBHvPI2_lt0RL4mZhI0E9HBfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛
مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28267" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpmn4NGqhsecU4j8n2Op9fuKGVm2j6VKUGPjtUt8nu_oIIxlQ3OdTafrGBthn6xpGSENcazXQvbgFXSIMtl6bgOx2v8jL_Iv2Cc8jYqIiuwzKMDWucLYylTNbWEI28uCqhmjhkkYj3Q3WpChdqRhoxiNoKgHv8F9HN_wm3CXdhhLHLQej40AYSLOuSVeI0m4AGrB8tppSi0Fuvad6OOxNMz4FFITiyx4Je2W9pw1XKotavtZ4J_JkevtYftDHM1nwufdrIbWf7i5CRfSofoYw6DDMctoagpiCBnzuVpekWusia5lvkzJbaCe-SX5p9M_sCCPIPrrMVnbONUPCvJSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب با اسپانیول؛ ساعت 23 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28266" target="_blank">📅 21:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28265">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqHCp0Z4dTnBaYwka8i2GEf5WuSXqOtNIxkIxNiy_69MqPE_oitEgVLHo1Z6NnIZ6pEElZ6d_QCOvHVsL0-1_2u-bkOLuzZ5yjjZMfEN-pYqEkVA9tN-bnGcwTnR-5orlwXSYx63teMB8GNlVFOuKy8hv6riGyOaT5OErLxEUCnjUhbgUrk7FBSAGtdOyzxdSRS8w5Kegmjsu8o71b7MOKNFUpIwUsoii9IvyKDS8vrBsdaQPL0czCXtYtjjkqTmXb70MTJL5w4bo0rvyynT7-gZ571HslD74wqk2VXP6jh8sirasAB5uGO4q0YkNSvqT6SPwtX-CdP1064DTOu26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
24 ساعت از 72 ساعتی که مدیران الوحده به مدیران‌پرسپولیس‌وتراکتور برای‌پرداخت رضایت‌نامه قربانی فرصت‌دادند گذشت‌و‌خبری‌ ازهیچ‌کدوم از دو باشگاه نشد. رقم مدنظر اماراتی‌ها 1 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28265" target="_blank">📅 21:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28264">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfDlj_F934Xao9lHXEG8KeAC4aW6qXwSCYgRbiDkuNDQ3WP83QdFHVIYcJchN0qLQ7kVfL5QxAF11z3rgP0ZLe0Y2vB4ln1ZehRG6X400uAvu3WGBWQSHVTlVJdif8VfMeDl4p28QdfKJXgo8IIKI2k626A5qFJi1xaE5mT5EY30N4uo6T4k3_mQiVcSLfLGjcUre3rVVciN2vgha3HBMIUelj5hn2t_4RpRghwNJs5DloyFy9hECrS9GoEA3lSxeMhKQuqytXbuhB2S3Y643U5oL-MxP-vuOQi56OIuS7PiZcyNRaS3YfGpSAxqF7nq9bNG5Y-MhorP9yA5NGn_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رئیس هیات‌مدیره استقلال: اگه استقلال رو قهرمان لیگ‌معرفی‌نکنند از طریق فیفا و کنفدراسیون فوتبال آسیا پیگیر حق این باشگاه خواهیم بود. چهار شهریور پنجره نقل و انتقالات تابستونی بسته خواهد شد و ما برای جذب سه بازیکن آزاد از فیفا استعلام میگیریم اگه مثبت باشه…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28264" target="_blank">📅 21:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495f39b6de.mp4?token=k_4dUgV10bsAxG0f8jXe4eo9Dr0kpmZ9TqiSrtYw1Ja7Z4meKvs8JxanPql0PnnGVY2b6psE93nZAyrCoc6_0HvZzz949_E_7TIl_CVO2pH2zASU7HcsyQyyDr8eRwZMgvEXefvH_rvTd_jjST1uMAuHoSsdTvGAazCU1CXHFnUPHjrQ-XCnFVP6y0mHXOohkoHXJZclTElWOHpZsEjRjERwTNsd9KyEVcDsYeT21eOM5IPocRw2Nur_T6sf4z2Olkn91VVa_EHNo6ySqGMPz1xMjNQO47UxT72toDwc_7DYaEFX142DqbfUn53A0O0-h7HhqXYdKLcoWoV8IBGt-JEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495f39b6de.mp4?token=k_4dUgV10bsAxG0f8jXe4eo9Dr0kpmZ9TqiSrtYw1Ja7Z4meKvs8JxanPql0PnnGVY2b6psE93nZAyrCoc6_0HvZzz949_E_7TIl_CVO2pH2zASU7HcsyQyyDr8eRwZMgvEXefvH_rvTd_jjST1uMAuHoSsdTvGAazCU1CXHFnUPHjrQ-XCnFVP6y0mHXOohkoHXJZclTElWOHpZsEjRjERwTNsd9KyEVcDsYeT21eOM5IPocRw2Nur_T6sf4z2Olkn91VVa_EHNo6ySqGMPz1xMjNQO47UxT72toDwc_7DYaEFX142DqbfUn53A0O0-h7HhqXYdKLcoWoV8IBGt-JEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28263" target="_blank">📅 21:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28262">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b6436f17.mp4?token=KU779UgC-7PpKYOOR1naOPZL8o5WEmazrIYucODCkMTKGNriiex-_Lsx9skIlE3hMhDrrbChMac5f3w5zR1wmpFQfGk6pAIgVNu0grbxiGmdmgEk3Fwg52psHePGj9Bqwysac-7Fqop7sc-QfPsYoS9aGAekZ0m84g76BjF31X1yJIYVCV06X-M9VhINfUGMNTkWsXvsFdMvvHi0wKnJ9lAv1GwwmFZZEDuYdrdXYmjlVxchk72bWbCZvYU0YrZPQeHoGLyiS2_eK5-ByJWsYWlHiyp9-v_hGEmWCubXlx-rl44NoObk1eRocHf1zy7rlbSVmAhK5DTO6DoDxyZ-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b6436f17.mp4?token=KU779UgC-7PpKYOOR1naOPZL8o5WEmazrIYucODCkMTKGNriiex-_Lsx9skIlE3hMhDrrbChMac5f3w5zR1wmpFQfGk6pAIgVNu0grbxiGmdmgEk3Fwg52psHePGj9Bqwysac-7Fqop7sc-QfPsYoS9aGAekZ0m84g76BjF31X1yJIYVCV06X-M9VhINfUGMNTkWsXvsFdMvvHi0wKnJ9lAv1GwwmFZZEDuYdrdXYmjlVxchk72bWbCZvYU0YrZPQeHoGLyiS2_eK5-ByJWsYWlHiyp9-v_hGEmWCubXlx-rl44NoObk1eRocHf1zy7rlbSVmAhK5DTO6DoDxyZ-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28262" target="_blank">📅 20:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiOcKp-YDGwM_D0GDynd_hrR_dWZW7Ev0jElajQCXJah8LncEMqL4RY0p9-jcvfXIMFwHMDCH7bi3DLL6vks4ZrGw0pUt1t-J2hXuB2qjdpZGIyJB9ulJ3RTZGWfpoIepnCEZIY3FKYmBBQBpmP2qHzlaFymBmHQGuvJiPr7pkJkxKh7kiTWVCs6nRn4zShDoQkQrV8NjV4A3X-y74X-kd8eMFyWAPL76eptPr0pXhIgaWWWHtrZmfJybPSXjTHB9oS8OFx057ERdsA7RLPaHuupablBqbc52jYooSPMsnxxRAFB848sAf7P_ip9o5FccgpsSyX5P7hnQRJZEXqZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باپیوستن‌طارمی به الوصل. الان بالاترین سطحی که لژیونرهای ایرانی بازی‌میکنن لیگ لهستان و هلنده سراشیبی سطح فوتبالمون خیلی وقته شروع شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28261" target="_blank">📅 20:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136a8275f3.mp4?token=lIZ-TaX5G5twwq32ux6Wdw_ca6rFZ_lmpBBdR-d6wEOM8sh6vgfgbWyTCCfB4h6eU3JMf38-hl9cVkp5BEAjiRlH5rV8WE6PiRmh9y1gAiR_HlDDPXoX0H4QvXX747FHTKidoDteaixnsxj5vb2v8Q21ifdCYpWJZaJaHw5-6NHAiJGjZDz1S6FRUlHl_bVv8fIZhqwEmYLAq_7YZiKAVwyCqT7LMUt0YFWIpV1m9yjzh-EjxPWBR3x-XqzH1wOMOb4zzhqjKMraHQHClyBFpByuKXLZfUQo_iJrKw4zIAgTovfu2N4eD5AYeZCFaVtEj_I1lx3vubz2DFaoCjBqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136a8275f3.mp4?token=lIZ-TaX5G5twwq32ux6Wdw_ca6rFZ_lmpBBdR-d6wEOM8sh6vgfgbWyTCCfB4h6eU3JMf38-hl9cVkp5BEAjiRlH5rV8WE6PiRmh9y1gAiR_HlDDPXoX0H4QvXX747FHTKidoDteaixnsxj5vb2v8Q21ifdCYpWJZaJaHw5-6NHAiJGjZDz1S6FRUlHl_bVv8fIZhqwEmYLAq_7YZiKAVwyCqT7LMUt0YFWIpV1m9yjzh-EjxPWBR3x-XqzH1wOMOb4zzhqjKMraHQHClyBFpByuKXLZfUQo_iJrKw4zIAgTovfu2N4eD5AYeZCFaVtEj_I1lx3vubz2DFaoCjBqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
سولوگل‌دیدنی زبیر نیک نفس در بازی هفته دوم مس شهر بابک با خیبر خرم آباد؛ قرارداد زبیر با مس برای یک فصل 8.5 میلیارد تومان امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28260" target="_blank">📅 19:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28258">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYQGjlIlT7Q6WilMcRbVh_RMcodZZZB2G4ALWsS4u29B4k5HJcYW8qeSiniU6lOHwhR_4_Tn4IlvFRlcBlunEnyDN-r1lspASOIfVLuDhx9911_xziE5e0OpaJVeE5ywYAaD2UfO_frO41QxHs7CjmMxjzLv7g1zr6vc2om4afIu04AMtZOhFUKMxo4BMIGJg2d2SHcWlM29Dukd6O-aYenSUlGe-Ra62rG_1l1aRz-x1KRqyHB_kkf_jVTy5pRYXNhzrmrzJfX9g0PrcfShO34SlAIPLZxvyAibl0cmLCLp_pS5nyp1EyUD6v5OYXCTWW1Oc62IAGx99qw1w_wCEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای جذاب هفته سوم لیگ برتر؛ 24 ساعت تا دیدار حساس دوتیم سپاهان
🆚
استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28258" target="_blank">📅 18:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28257">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvSzPRqOb_DUjUD1z_PSNeWNRNvAM4EiZ00D6zqKlk3ODBAeE-DXKZK48AugtFgOxR1zEad2aFh75JbKO7hmPVVntWd1AXwTNdCPjjbzPhcmQPo-0v-MtWwN_bkXX_L17-P0hN5gtl4cl6LlbNUYYrWylOsLLj_YEc22e4Ok6nyJJQrz-pQ7kG0GZktmLELyeJpcEJdyyPsV117Gbnux9J1c4bt-kORqZCb2VKg0jpbmjUwt3SgKSA3Vmqwx27EF9hV-5nit_BtJeYPyO2aR-h0Bf6hcb2Q2VLGzbrdrx6q7g7pg1LfsylDxBBtyGQOw9tyY4c3b51kaSSvpjMHIAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام خبرنگار باشگاه الوصل: رقم قرارداد مهدی طارمی برای دو فصل حضور در الوصل معادل پول خودمون حدود هزار و سیصد میلیارد تومانه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28257" target="_blank">📅 18:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28256">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5-w0_QHUKxsVahhmpcOxiMT7EjxkE3Xg10iV0V8rzzA5rRmNjmCCgHX4pN8WFlbJ84VX_lcI0OZiJBRzhd0UynPqQdMseTcBLJzeZ1m6A_DFkjRyFm10C3a9XsUu6rpTOIEq12Jq_DkfJbrOCnuC4FrRaM9zF1ddZiyHDseE82jzmFuzAWhefsi7ALG-LD1Xjz0VZftjq02ex-dMEywkokDXn7pmf3gd8cY38yLNihZ3pxSRH-_2PhX7j-hCtD-GXysU06oKHDVex1gUFbUbSVmOpdudeq_Wz0J7i2xBgJXcH4uDZ6x8nyZoBFAIgMudibjYYJN8ybXksWDyuTQ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28256" target="_blank">📅 17:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28255">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01212702.mp4?token=WBCJBAYy6CGcGVaNU3XfWZvX3iZQeNcbnCmm1M72MW0Wopto_I0ox645GkbhDBAEIKO0OQmvlEnZBEj3cIewoOkA23c30myD7DW4rQ546DB4vwUFuk1zcptHFBSZ10L2BN97tGvv5EPXX0Tu0wVn3NBAd73za_ZClXZmUCTxjBMreZXroBKjnlCOLMBBsdfwavvH0FTonQWoYCe3F6Yt0Zh7lCWK0h0xsfjUaJ3NNqy4c_IHdW4MkArEna8yy_pZQKpFyMWuwGv6JeLGhG7auVDHDRE0cw0SDudhtPhRSzne37JPljiGl-HJ4TxBqL7jL0gMhFDIIiCbSpHs2T2W8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01212702.mp4?token=WBCJBAYy6CGcGVaNU3XfWZvX3iZQeNcbnCmm1M72MW0Wopto_I0ox645GkbhDBAEIKO0OQmvlEnZBEj3cIewoOkA23c30myD7DW4rQ546DB4vwUFuk1zcptHFBSZ10L2BN97tGvv5EPXX0Tu0wVn3NBAd73za_ZClXZmUCTxjBMreZXroBKjnlCOLMBBsdfwavvH0FTonQWoYCe3F6Yt0Zh7lCWK0h0xsfjUaJ3NNqy4c_IHdW4MkArEna8yy_pZQKpFyMWuwGv6JeLGhG7auVDHDRE0cw0SDudhtPhRSzne37JPljiGl-HJ4TxBqL7jL0gMhFDIIiCbSpHs2T2W8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28255" target="_blank">📅 17:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28254">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOHndrFmCt6C2e3QctyvH4AZlI08Q03fyemjh412HiO65qAOXG9SWMH7wFwSX2o3_QrRsuMGcTt7VTAGakLbR8vGvIAfrSGAkYvEqW6BqO-c0pJ9eT1VyK_tzv_MlQBLVLkVziIXsEHShbLzUslqtl54seWMDk_3wYqH7_Gyu1ZoOdNZlhOvE3jFZoKzIdCS0loW3MUVX6x3gAOoMI8mQRNuMT2UsoLeRVJWvQwJ1o8R62yt3ffLBg3U3r799wT5Kvm904X2Ss_c-Y8uMoch4XvRYM8HB_cpzRQuIb7J04xqeFFzwxJq6s43I5cf2gRlAPkSF1XEdc2reGtxdXmDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ژوزه مورینیو: یه‌فصل بدون‌جام تو رئال نشونه‌ شکسته. حالا هر نتیجه ای هم بگیریم. شما میتونید ساختار روتغییربدید همه‌چیز رو بهبود ببخشید، من دوست دارم برنده شم تنها چیزیکه مهمه نتیجست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28254" target="_blank">📅 17:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW_sTM-nAMbNhyZdn0At5sUgZApVLEEi7EIZTk1h0gl7shR0KlAW9w86bKxC58Ux6UVknMPdLkvNJn9nUnvqEzMHs1wvEAkHIfzPrsIQP4xEsbLWwZc69SX2JiJdxECTbcaog-7oMEeyoLv-QyQ3SVYQV8WgkfYJg2O1oRqQr6_wFjOi6ZjpyABSdPHqVRsRC560-j3NDaRunHbJlcxW9sJkP5PQCeLbi8ldf4GpnQEsmoMyeVwPk7tI1RZ2xfmIJj-QjGI6aWra9ZIXXwqGxWu8mW8AxdFuKYMdjEZAxxvoz4qKLqs4zqROzkvULeJhR7TpxZzfuZyaXaOsyDrJIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛
الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/28252" target="_blank">📅 17:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b6b8171.mp4?token=ty0gW1NhjT86lLK_0yWzJ2vVEOFJbw3Bzp6-ahRmk4SyhYOflw6DiOuXRVVEDWGCVvcHhXeGGQQf_nnVd0dyHCn5l_DmzvmzdW1z-eMQbW4Rkt3I3IOGhmagkrRMWcSWWLKBv7q6ZTBjEetBF9CWU-vRg_FwJ5heH5EeY4q1pnOUj0E2I8MhHSjS2I8SyaznOaKIz7SXNaEZGYWKMBu3JR3QBvoBFMzaGWdTuLN2DhlYXw6DVsQsxsnFBpxSab1aiqRBR3t1lBSqoo-6C5ddHn_Cg04rpRuE2RBlKO2EWVw3c7Khfr0JZPkttz9pr7qfUfYK7xiX0y-FjSHrFdxFqCCmi1pcVXj6v_xq2YVw7NMamDEyeZKqqt7rbx1XkE6eUtnGjSf_MbX98Puq7cf4FwMMlAN8MIqp5X5WVFesjrLpBz2xO2JVCvVoAd1acvxsSY02kV0mY2p3mD0xKXLA3Z_baRY2U3ByTWz7c5XmZAAaZ7E9Ah-j1MueGfiaw0A9KRDt5Tixeau9it_YlTZnOnwn__Noh-Tt_GTzbwH1RWi6MV-QQKWBnID8d9KFNu2MTyUn2oIjBH5BEyV5xRkqvviC4IiwDZlnfxgHDPoOUEoWjdyid9oKPmV7gXZfIy3wywMSvbF87pvvpDRZR46bXO7G0rA9G049dw5-4hz_zLU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b6b8171.mp4?token=ty0gW1NhjT86lLK_0yWzJ2vVEOFJbw3Bzp6-ahRmk4SyhYOflw6DiOuXRVVEDWGCVvcHhXeGGQQf_nnVd0dyHCn5l_DmzvmzdW1z-eMQbW4Rkt3I3IOGhmagkrRMWcSWWLKBv7q6ZTBjEetBF9CWU-vRg_FwJ5heH5EeY4q1pnOUj0E2I8MhHSjS2I8SyaznOaKIz7SXNaEZGYWKMBu3JR3QBvoBFMzaGWdTuLN2DhlYXw6DVsQsxsnFBpxSab1aiqRBR3t1lBSqoo-6C5ddHn_Cg04rpRuE2RBlKO2EWVw3c7Khfr0JZPkttz9pr7qfUfYK7xiX0y-FjSHrFdxFqCCmi1pcVXj6v_xq2YVw7NMamDEyeZKqqt7rbx1XkE6eUtnGjSf_MbX98Puq7cf4FwMMlAN8MIqp5X5WVFesjrLpBz2xO2JVCvVoAd1acvxsSY02kV0mY2p3mD0xKXLA3Z_baRY2U3ByTWz7c5XmZAAaZ7E9Ah-j1MueGfiaw0A9KRDt5Tixeau9it_YlTZnOnwn__Noh-Tt_GTzbwH1RWi6MV-QQKWBnID8d9KFNu2MTyUn2oIjBH5BEyV5xRkqvviC4IiwDZlnfxgHDPoOUEoWjdyid9oKPmV7gXZfIy3wywMSvbF87pvvpDRZR46bXO7G0rA9G049dw5-4hz_zLU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
بااعلام خبرنگار باشگاه الوصل: رقم قرارداد مهدی طارمی برای دو فصل حضور در الوصل معادل پول خودمون حدود هزار و سیصد میلیارد تومانه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28250" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sa5t-viifu5OqgW4AY17r7cSKNS4eP5-dhlSIw2gqJ-8toGzyUq3uO-DMdz0KvGi7ax92-Vmm_8MDF35nxruGGRztfV2xnJFnpFmfT7O33f6Kn30-i9Mb1zBU2dDmz2_8AJkbb0r0Jqwb6CJcTTU40-YhITp_m8yACkLgiiMAn9K-YcDWIV8EhsB6oQ7hUT0kEG-W0yxqZM8SK1YuWFcReNQIUtwh2_4NJ6o0MEXiSBpUHGZWJCRPXSAQ5BGIGwVWVszkfwsMx9vsMIOf6hisgNLM5eyOBZfJh9ILhouE_qRRcOIVLubBgQWYlFgZrmRCmCyalk2mQ9ayx4C1WJomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28249" target="_blank">📅 17:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653009269.mp4?token=UwtnRRIYbAvl-lcKychr4TrdS6Au64JhZpOVB_hf5l4PC79iRttjA0u4Tc75NR94EhJd0VqRbuF6OO4OoJR4WerRnxorRsCw0X5D1JjEk3US9Gyn5Aum1Agf7akzLGljnj4rRQM014b5PaS0_4iypGrJGunXV1IRKT7oe2gcly1q5kRQ3Tp1qKdohPiD86Ey1c0F2BseB4hW6DMZl6QqjZ7pIz4XlWZ9ocmizMWcfNtcdIGakuwptjK_my7GazReiAfChfOM07fHaC0GKSzLlnBMDiZiEGEj1BeJhkzW14W10bEVyzCTlR6OWcIAgDrGfCI_pQb6TCbpcuPsIuTGRYyIDDSVpnoJDg6lTLg5_zKX-lCWKJ07IIiBOLsBvN19bCtEmaYpL1n_gKe7ua_uEDh_g-uE0mhl3N54gf8lgt36G33aaORM5gB0ZlgpPQnu4umuGmspRUCjDkZF_TjlPrbzSSkVpJsY9g-eOizpzzn4IbFwvjwzpvikpcc9y4OWd_bBamXAWqPyEXWrkTSXYhWcC1VMHl7VMj6Tp0hNgkEs43oT8tRrAllXo-UeYTUkdf-vtCsEMaZO5XM1ulHqHLXLRCofZG8xmq3Uefor-u4tGIyBnLloLHQKf33NrAs814rYUWEnh7MbuhUEfsohwBbK3o2ySUr4ZqGAfVa169M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653009269.mp4?token=UwtnRRIYbAvl-lcKychr4TrdS6Au64JhZpOVB_hf5l4PC79iRttjA0u4Tc75NR94EhJd0VqRbuF6OO4OoJR4WerRnxorRsCw0X5D1JjEk3US9Gyn5Aum1Agf7akzLGljnj4rRQM014b5PaS0_4iypGrJGunXV1IRKT7oe2gcly1q5kRQ3Tp1qKdohPiD86Ey1c0F2BseB4hW6DMZl6QqjZ7pIz4XlWZ9ocmizMWcfNtcdIGakuwptjK_my7GazReiAfChfOM07fHaC0GKSzLlnBMDiZiEGEj1BeJhkzW14W10bEVyzCTlR6OWcIAgDrGfCI_pQb6TCbpcuPsIuTGRYyIDDSVpnoJDg6lTLg5_zKX-lCWKJ07IIiBOLsBvN19bCtEmaYpL1n_gKe7ua_uEDh_g-uE0mhl3N54gf8lgt36G33aaORM5gB0ZlgpPQnu4umuGmspRUCjDkZF_TjlPrbzSSkVpJsY9g-eOizpzzn4IbFwvjwzpvikpcc9y4OWd_bBamXAWqPyEXWrkTSXYhWcC1VMHl7VMj6Tp0hNgkEs43oT8tRrAllXo-UeYTUkdf-vtCsEMaZO5XM1ulHqHLXLRCofZG8xmq3Uefor-u4tGIyBnLloLHQKf33NrAs814rYUWEnh7MbuhUEfsohwBbK3o2ySUr4ZqGAfVa169M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته‌اول‌لیگ‌جزیره|شکست‌عجیب‌ودوراز انتظار شاگردان مایکل کریک در ایستگاه نخست رقابت‌ها.
⚽️
هال سیتی
2️⃣
-
0️⃣
منچستریونایتد
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/28248" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzAO4LPL9K5U-LTnNmb9YPVtBrdNWUs4fNwDKoqq-IkM60ludWO8HH6CMgZjysb0hzTCa5VqVRohYNHR60BFZ19JaltcTBdriZRIaCDBRdpKsA1tQZmEBDbYE4lf13Okmjj3brHJgJxkkNk3dm7DEo3rycaULPR_uNVHgjtI3YV-nhh7qAY2TQRLIQG2YjdOZyW1BT_qFvQlhV5Z42ppuBUbsJscJiP-hWOrcy930Kfrt84o1d7jTb6rdwsGvuaoxBzjhM11vYGIaqvDftMzXl_82iU2N8U8gRgmZydRxfWY2PQxM4LJfCwgZTO8k71l08IivESV7MM61qJ6_FeQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته‌اول‌لیگ‌جزیره
|شکست‌عجیب‌ودوراز انتظار شاگردان مایکل کریک در ایستگاه نخست رقابت‌ها.
⚽️
هال سیتی
2️⃣
-
0️⃣
منچستریونایتد
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/28247" target="_blank">📅 16:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28246">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smrg1j8Dh2HR98-rY_d-IKggIVoT2-mI7J_5XluXcSIq1636drrmyT01EKnfgp_KB4a73_vDQGk3mC-hK_2ovYwZ9oHFP12KZaGoEL115SbvTQmdH4EBM7bd2ZBjht5oBJEC0JLyAGlnXHxDILmfd-nKo7x2MA3jeoU3iw1rBOW_-iwELV2cUTLnd706Oc_Krs760eG742taRt9Yioum4qhgwTfAv8oHMr1e8x22stu3w5bR3XVSrGM4-uGOEy3BzEH0RO2lhq11s97Rnc6A-awT4lXongHdRqPdp0HOq8UJxx3zw5WDY3dEOG8qHekSNIO2s5MTS5mnSYRVyzp6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ حدود یک‌ماه از بستن سایت و پلتفرم عادل امروز پلتفرم ایشون باز شد و از این هفته دوشنبه شب‌ها تحلیل رقابت‌های لیگ رو خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28246" target="_blank">📅 16:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28245">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f79O3-1H-2jhUHbx1pnVAQxbw9UHCOOKTsUpSfNMVEVfS-rynJURgtG14FhRkXyewRgg5BoEZ4I8A2Gqv8GJwqDUgjZa9qiTkbaZULnFIsY0lLAnKaooxeBof_MHgOix1NEb5SAAQbr_dI7cqMRKW871o6i19z3-ki9O6Nlwn41q2ymHOrNZoIe8NCc5toBwKZyCnWhDV8PLTL369U54jAk2eTbG7EdALTC_Gdo3rN8GRuadWerDMHwBiXQWYoMnSFOVxsowH3ER2WjiV9P2EirHUnmp72aSbaQ-mALj8C3fHfpoTSbB25y0d7xaij7OcC-Km-Jio7ET-hNc2-fnQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌های‌اماراتی؛رقم‌بندفسخ مهدی طارمی 500 هزاردلار ثبت شده است. مهدی طارمی پس از غلامحسین مظلومی، فرهاد مجیدی، علیرضا نیکبخت، حامد کاویانپور، ایمان مبعلی و محمدرضا خلعتبری، هفتمین بازیکن ایرانی تاریخ الوصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28245" target="_blank">📅 16:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28244">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cr5vUV9JPvB_x-CU_CA68lOvT9omsNutbMb6fxxws5WckliQ9FAjDbwl3pI7yChGZjqe3zWgaVXgn1oDlJc46j1AWEj_HRJuFNH4hnovcc2ZaZbpG7oyrC4e5TTlMOwCb3MxlTt9D_MiJvEeCgvP1cQK9jYsu8RDyB43bNR6F3J9ANlZCStqbgNADxZ_OO5fjwDSb-awabIB2wCeYaY91Hf3uQkjM_VbCBWX8KtC_Pp2RMakQi4LfmQxSFT1dF4EPqiX3eH_1mnyGpkCNX0QRBsruOJlQVVYaptTzp-GtkWmoeuCRsIm2mavEq_y5tBPGgK22BR7htKcPNJ6-6WibQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی ستاره34ساله سابق تیم اینتر میلان و المپیاکوس با عقد قراردادی دو ساله رسما به الوصل پیوست. الوصل یکی از رقبای استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28244" target="_blank">📅 16:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28242">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E0bnaP4O4RyBMTBtqtbpfebra2xbicOpLjtH0JhM4v5AxfkNxulIxkpG1xCUUJNtBAxcdp3ROVSJ3WtYb3QMP_cEN0TZrbaFgWdHx1tCJwakM4oIz8M5LmnYhGiZxcbRx81kVaExrmHanFraCjkzPRXCN5Vr1sBexHfUtm6pDghDNAD0NeFhAr49-2Nfp9TV0P-BAUey2RIcfzpk4EvaRnRoctPrBqC8UQ-3g2cHvcgAWG0lLBL9p4BcXDlSsJloBSN1cIumt230-PEBtB3KSRmqF11hHx_2Uia1hm73otZ5VD7cVsojnpemA-E6wk76_T17h7kiOEEao3OCKMOh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU4544mCI6ASZaVceQ7FKPNgzpyyDnl8k_OK_LAw1HXLJAU5MsWXJbJ4dTYMqppHjzscpNojHDhc7uJp4yEYBm8hU6Gfgs9F6SN0OX0XdKHsn2D5OO3ni2OoFoa2lHrXjQSu6T3rQXo2XKxCLYjrcFpzU-5TYN83sOp-4M9HKY94QHsbxWW5nW_C2NHfyibaWZQ1KgNLspMcRoaXYm6mRQ1des8GKwrZ_C30mNdjtEV1lkSH0z0WDt36ADU8GGVkajCJGH0AzUno85WdTQBmKZ6ydP2PL5R0lRxFHgSGcx_qAqsJYTNIxqKDu8-5tF-sQEtuCiKH2By6YlLkX_g75Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28242" target="_blank">📅 15:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28241">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTS8OaGN7If8c8myBvfNyr47b_sIiKUZLn9-VmX57kCb4u7qsU4b-7eEzv1IrTvBuzLTZ0NBo22IwV8nYDOdUWNzYVkZZ2JJuwJKnqrXJuYhdLp7FKcoTWWPBCsv9JgkhYrhcy9Fwf_VWyf4ZkH2Pjx009oUUKQuRz4pVONZnCHAmJ0-VDe0tZYvk2Xj4sSqhQby_Xi1RbMYvWjRQSdD8Wl1cCftAduzuGjGY0iPXu2M67Cp-8jQYV6Efva8flrpeTFKI6avDQl_QJskqC5GqDifN4wt-JBnxGIvIeAzwgeMnX0w573DBIPSVxKcPw096vMhVMC8U2D3ofj8NuoEmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بنده‌خدا که یه دوخرچه سوار حرفه‌ای بود و ۱۲کشورجهان‌ روبا دوخرچه‌رفته‌بود و هیچیش نشده بود روز های گذشته تو جاده کرمان با میکسر سیمان برخورد میکنه و جونش رو از دست میده. طرف هم بجای اینکه تلاش کنه جونش‌رونجات بده فرار کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28241" target="_blank">📅 14:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28240">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-6k5V_Ii7V2vrKj1qYBKGFfUrMmoDNi_qdmaxccKQC2RyvMsx2F8OqZ4BpWAwyVgKXw9KF9ZYUo1sHK0obh5heJfVVkL96n_l2wUAnvpRMedrn94QYqnJz6nRVmQMUeC-NKmjJfZLHsxUrUTQIny5lIbQ6AEosUUogki6Xqm6KV5nacctuWOXibQmLTp6e5LeX7OaXlcRqiMWi3TtT-s0O_is1ROfTFX5fiHX1jVoioulKKQrKMCDsI3ccIIEX4WzLpR-RashpJ6cZomuACaaArx7b9J0SFXZjaZ4myNJdWiZxQF1hiXyyCYesa61tpSm0OJIukPtxjTK6o1BHcTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌کامل‌بازیکنان ایرانی در ترانسفر مارکت که فعلا بدون‌تیم‌هستند و در مارکت بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28240" target="_blank">📅 14:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28239">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnLmJVcUMwW1s8SN1FS8B85quB8_-CMzH-Ko3qG1FbEmB4PXSxr6OlsDe-s9tps7HJI7o8AOGnK8J7tqICRV414DGWC6-FKw10Lq4MbOnwjwM6rwKTeYvrDgE2wa0V_5PvrvyvFI69HRjUjFpFh58e6awcYx8gZ6MJid5FdOaKD1A6sddQzARoIiCX5I0ih-_cUGJXd0UUxEWDNYIt4QEha3BD3-yPSiRvCKcVbJd9ArzsEVo2qQ3w_zAmUUFnlw0swO7NSsDmTkNtwTQ6av9MxaqmJZhQuAZreOvnK-O82CF-8-ZqC22msZLWHy9w8yc0WJ_m2F2OLNvCRcWQ5-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28239" target="_blank">📅 13:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28238">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1fb0883a.mp4?token=MJ2z80ft2Jd6J1cQXXINGGX00hHrq-vSY7cHu19rPKsIx7WUb4K58ZUs9O00FIcUqZSzC8B42hAyns_SwS1sDFD3REGFAKq4sRHvp5CU4brUv8Hkj9NfNKdVC1j1RMemcoqj0uKNwyBuE03X28ZDxpjLm_GFz2NUIBs7wbbKFnPa530T_k4pG-B02-ss6aeBFtvkO1wtaNZEXtigebUSV0aTV2cpqOhvQjvLwtulRnSemXobSpmHpnPqzoRmCd9C_N2vFVpdCWieWUYGtgXRvlU6Gz5QpURmJKkFDVq4n0gKPIEllrGivigarf6BetBgiZDpAeVxnkNf58NTkl5uLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1fb0883a.mp4?token=MJ2z80ft2Jd6J1cQXXINGGX00hHrq-vSY7cHu19rPKsIx7WUb4K58ZUs9O00FIcUqZSzC8B42hAyns_SwS1sDFD3REGFAKq4sRHvp5CU4brUv8Hkj9NfNKdVC1j1RMemcoqj0uKNwyBuE03X28ZDxpjLm_GFz2NUIBs7wbbKFnPa530T_k4pG-B02-ss6aeBFtvkO1wtaNZEXtigebUSV0aTV2cpqOhvQjvLwtulRnSemXobSpmHpnPqzoRmCd9C_N2vFVpdCWieWUYGtgXRvlU6Gz5QpURmJKkFDVq4n0gKPIEllrGivigarf6BetBgiZDpAeVxnkNf58NTkl5uLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سهراب‌بختیاری‌زاده‌سرمربی استقلال: نظم و انضباط برای من از هر چیزی مهم‌تره. فردا علیرضا کوشکی رومقابل تیم‌سپاهان فیکس نمیزارم تا بفهمه اینجا استقلاله و نباید رفتارخارج‌از عرف انجام بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28238" target="_blank">📅 13:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28237">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21259a9796.mp4?token=Zy-5gyvruTbxiPAAzrZn8YgfM9rRNUlI2JxhDE0JmuzrFlQRWK3S0B2embBhYtiKGrt7i2bYxj4yi8hcnS0oT3ONnWDGo0AAsKrfjdhogNp0PEnok2ZjQgCo5lyIqg6Qo1G0LFUO5itLdGASfLjnSbqYn7DjU1vOJIuroeD4IuTF7o8P1NFctd30qzE_d9EBnatC3CA8Sj35K-ynmrZ9XYG85O1JZ4TYLyRy6XoQIz6wKk6L21_W5oZmMfmjjnE4xivugvO-njPXqVZqlk87SkS5dVMv282NTSqpQ4fXzIyIM9r_X5MbZ7Qld9_tZdw_ru7HSlhfI0_CtYzxMV-IrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21259a9796.mp4?token=Zy-5gyvruTbxiPAAzrZn8YgfM9rRNUlI2JxhDE0JmuzrFlQRWK3S0B2embBhYtiKGrt7i2bYxj4yi8hcnS0oT3ONnWDGo0AAsKrfjdhogNp0PEnok2ZjQgCo5lyIqg6Qo1G0LFUO5itLdGASfLjnSbqYn7DjU1vOJIuroeD4IuTF7o8P1NFctd30qzE_d9EBnatC3CA8Sj35K-ynmrZ9XYG85O1JZ4TYLyRy6XoQIz6wKk6L21_W5oZmMfmjjnE4xivugvO-njPXqVZqlk87SkS5dVMv282NTSqpQ4fXzIyIM9r_X5MbZ7Qld9_tZdw_ru7HSlhfI0_CtYzxMV-IrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
تغییر چهره برگ ریزون و باور نکردنی رابعه اسکویی بازیگرسینما و تلویزیون درسن 60 سالگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/28237" target="_blank">📅 13:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28235">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciqTnbK9-v_fzYty-Z34nxnUas4IGD6C8SSbczIdjovSmA0y4e84Sx14-cctsKwluvhRjrIg39bZAJXGXI9uwLgN0pn1lTBwCxphC6H2Ub9pLWCh_X7o64ho7JO9C9gr5-dljzkPmO5ZaRRIiXL20BqZMTDoiGoYqHBaZ4S_1e91uYdWXW1u4Vr4D3je0yhjhvQFQ0Bm7Zwzo6ssqbdNZFdxk3EAIodLNrYEoUu6IIxBxr-r2oJhI-bnsXVYXfX5sQJIQNJtEF5Fm4_iJ7vVieGjd_-nURcQQzE0AsZkKdre4nEMZAesIy6VfFMoG4apEpmZi41jvMPkG7mRJ_yCHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری با پیراهن بارسلونا پیش از دیدار با الاهلی مصر در جام چهار جانبه خوان گامپر؛ این اولین بازی رودری برای آبی اناری‌ها بعد از پیوستن به این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28235" target="_blank">📅 13:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28234">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s88t43r9uzgGHGZ5cCP6a4J-Rky6ZEVr1y8E3zqrPNQcPv0iS4ySRcKuBr3m3EP9YC-KlABzeEwhGBXTQLAoAt0z3uKdfC0qI2ASt7pXaEDU7u1vA1cJm0RB1tVEU8Jkr4Iqf2G4HUiRfpe18PgShPNB8NtgoAS43KH6cNETgKtF4h2pdUaBUY-z8tTaEVwwnWq7QXFeyhgkZqM8D5aJ98QOQJscrat2bDt8KwV726C1z-M95UkHbbwEtw7nY6deNi7FyfRPDug-jZU2Btu34sCQu2ZD6w2yTYoWv3ic4J8kEqiveEIpEUFJSdMJkZWO3zxYU7HtOeIMpbLzh_KsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
مدیران دو باشگاه تراکتور و استقلال به فدراسیون‌فوتبال‌اعلام‌کردند باتوجه به همزمان بودن بازی‌های آسیایی این دو تیم با بازی‌های آسیایی تیم امید هیچ بازیکنی رو به تیم امید نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28234" target="_blank">📅 12:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28233">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP2MT3JA8zE1jt018ksgBlZiyZ1Hjmq4fINrM6exNL_gN7ZBtJ3KWn8GNdTStkb0RaExj81bgdYdaEANTCAQmcpkFn5nKlIUWJZ_v_7hasWPC_8bEhzU1bVxowkB3zPV0Tqok9_tuLquAbPGHmJi38wzF8FCElY4ceL1BV679Uq8lRnxJ73IdQBuiUoZoZHUjmFZJ4lAZAXww72bHyxSQhfj1lwadt0zbHlQmpdY_T0BnuysjBpJ7QSXYvhjGtOZVSxnkJbGUIZMEYgcGNBlInD3nNj6c7V6vRLMAb6DrK7nZ_bbt8cxtpZaGxVGH3nFvXf_RmAgbnYD5qzcPrfR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سهراب‌بختیاری‌زاده‌سرمربی استقلال:
نظم و انضباط برای من از هر چیزی مهم‌تره. فردا علیرضا کوشکی رومقابل تیم‌سپاهان فیکس نمیزارم تا بفهمه اینجا استقلاله و نباید رفتارخارج‌از عرف انجام بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28233" target="_blank">📅 12:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28232">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7zXEXXqdgKHgJ6LdmyvrhcZBf-xNg_rtvm9iLonsSkaC6Dkfe5ZDO7OrV--QhGq6sexM-5ZKpdoaqK6_0-YA9eHJ7rR-fhejPy0-uVa5gMqLDHdoFdGzo9mpaeataLhSjHilrfgMY_F7LQ2k25kVbXlawx3AWu2tE-NCfvEKp1iZunqziXhw-TEJbCL0_OhVpBHKesYFTXUmQBghTwAMpMkYdqs4ltCBmxzzBT49cM97GNbURpoJPXV5CbYnIJjsvQVnXInwCIzOD14jX2oVh8jXywTOTtnN4ycfjOu727a7WTpT7qAsjHj4o5L9JJKq0c18G9BlBkNgebWREYnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ژائو پدرو مهاجم برزیلی25ساله تیم چلسی قرار داد خود را با این باشگاه تا سال 2034 تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28232" target="_blank">📅 12:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28231">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXotGEwyrKHHVVFOaSGZRHpVA8NPHU5kVE3JVzFBreJgDeZRt9iKgDWAmV6sD3mMBY0v_w88dVjIPCkDq4vKJ3o87COr5cy3yf6Il5SmXD16pWekAWhku4xxr9qm6-8lFV84bf8nmn3TEMLAnf4hOngffTHSnvNlQdWqf3jy0hJo6PODd5D65bvLGivefiWUgkkTOcpXwTAW68Ce9Sezs7fWajWeQ8Esu8NX49151EqE2r-yzjKMfWGCLrPr7cLyZ93Sp1kQ0dDARZDI4kVCpfD89Fgj9g_6va5jiiqY5ItokC30hT9DCKe07bUdlH5fpnW90a8jS0ATASR_TRi2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
داداشی‌های‌فوتبال ایران؟!
پوستر دو باشگاه استقلال و سپاهان برای بازی‌حساس فردا شب دو تیم که شبیه به هم طراحی و منتشر شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28231" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28230">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRd3jnWtvzDog8QIWguDS9qTSsbpsARVxG55WMQBhoQBaH8O0GHX8eaqqlsrNNTTl31n09W2zCPwbwBfwImG9ABV7Zw1zJflgE_v8ro9W_R6h8BlHwcYy6I3qSZkaoMbUlsaAPtg-J22V28so9wLhmVXbT1ZqleQ9zdzITIx0QCUSdDO93wARQ0f5xMb9qU0VTjQDVvb6i2E23B63I_0bOt4Emb12mySih2PyzihUGzi1wRzzhFmzIvPpImS64tlDqCIgI4i9txKme9hzkFd4RWL4-c9U7aFk4xCOq0CgMksHezmAVbWm8k3TsIsoSEwMmzQ1YTdxjmP3Ks_KuNzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درشب‌پیروزی‌شیرین‌چهاربرصفر النصر مقابل الریاض؛ کریس‌رونالدو موفق به‌گلزنی در این مسابقه شد. این 977 امین گل دوران حرفه ای CR7 بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28230" target="_blank">📅 11:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28229">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPJ2qmyLfxjfjMfuBwmFQLO9m1pKUoVSb24Ur7n1ov11lbBwIAoayaTOGFeQGWVdvno4-j5jWtu7vN-UfsI37v-K0W9SCkmEdMatS2AQT3oxIdteaKCe8zHLGiOo5f4mdwqH4CsGeFk5iVpZPh_b_7zU2srY1jT4_LAU8dwX2lJuNcC9P8H2Vez_nz8UlvGWPT8voYgGIExMIxx5cv-SDYOQqIe8IZiTVZJAHye2vkWtjcS5Yyge9nOkyChNlRX1b-fbMNOUy-r9R5Rkzb6bi-CsrLt5V0pYVQdHYAB0dwqAI7zSKKSm9bLJvEbxgxjsWXGoRRMIlcKYel9wDdSJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
با اعلام کادر فنی تیم ملی امید؛ علیرضا کوشکی، مهدی‌هاشم‌نژاد و امیرحسین حسین‌زاده سه بازیکن بزرگسال‌تیم‌امید برای مسابقات‌آسیایی هستند و خبری از علیرضا بیرانوند نیست. همچنین تراکتور و استقلال گفتن به خاطر تداخل بازی امید با بازی هفته اول این دو تیم در…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28229" target="_blank">📅 10:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28228">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y73QhBpRjiF0SztqUG02aU7tho6I9vjfj6TsQFLz-srH0b9EhjTFMeqDgSqooAvsX4L4Puu6so6eOTXwTD_45AqR8nQOlYNXXrss0GAJWfsOhx2yru43qE3gEXvMBwuVjThLSTEXLgXIdO2kHCXUP7Cv4X135gzzHx6y0yGao3YF97PnsWFa8th7AJ8KN2c3X9f4i_MdSKQGd1cq93pwXER-RTYsrpxZ2RaZohkPL6hdylV4dLMwtfq_vd_fqTxG6igySoNA3FTo5wJljOumpYhQzJmJNTgiZtzRKT97IwhF42ujgTph7y2VcD8bPEKdZDQe0l4IYYE5KAJHFR4zZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28228" target="_blank">📅 10:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28227">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a06b6F2eWnP_jqGfURoL3rWGv5HuPcZTUo_H50jGmW-B0Q2MOTTJh9a39PYOcDElsCWK-DyueYaQ2WF-jJbinz4P-JUN41vs0Pqy4b285uni1WoEcEYtWpCFfHYOM3ba_cwg89OqsrmZzV_esA0kR9QoWQar94ONUQ7a5I3vzuHgTx-KxGD1Gbk5OjlyhoUICfR-LTq6FEhyMb6C0BfT8pq1ps0hbQu0PIYck-W9rgC1OTk7fXd5JTQ5f3V-mJxV5Cw_ZcS9NUaM_ZShHi2Nk2uv-4bcB7hqGB6ouJwjm9kMLF3STMB_PyovUVWV0U_dYNafpDSVzjJFVvP5nkDYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک‌باشگاه‌مختلط در تهران به خاطر مختلط بودن و کارای +۱۸ پلمپ شد و هفت نفر هم دستگیر شدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28227" target="_blank">📅 10:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28226">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpOWE5AFS5yCY1Znlv6fu59TomePcbMqdHylNfZxaPbiKA5RL0V99pu0GpR5tPvmthbUK2N6rwJu7IaIQ0inKC_N8s7eWvi0Lg74SQt1RmiRZeBkj9IaQ3ceoa9uKbHYvIOhHqLoGG4V4-yenZiEQkBXFtp-enNwf5lt1tODcXNAinfJrH5FabGy6Puo_04TaEIjFDySyEMMPgwUEXNuwG-VVip3sU01t38HGnXvmjRPJGCuFW3ywxTSYOsy2yniS62oBYzTulaCu_o4m42yQIJy9afMssr0tJSlA6kBApyZUVAORiu0LYfYaDAhk7sr2dFpiyjtfXxkXKd-HhIu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام اسامی داوران هفته سوم لیگ برتر
؛ پیام حیدری داور دیدار استقلال-سپاهان شد و امیر عرب براقی دیدار تراکتور-پرسپولیس رو سوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28226" target="_blank">📅 09:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28225">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9413e45de6.mp4?token=LVWIQIPizRGoJg0pcpUO9-fs9gJoPDLXv6_SIUFwDiXXkB0NMMWBfFLEg3s6ijHTNPZ6soydcPY-xUCJsjKLDAOaORvbXvbhD5il3AOeMNKCpHrdZ54bm_AExZgl3t5TYMUDOogPCi2OsIvJ7lhrwOl_Hpj7RuEhScJ1nzW-anl6wvxc0N8fTeh2Q_YK84rSiVI7zxskTh0OChxLoflqyxm12gSLUeIoBmqvpVm6sdP938dX5qDSMGWGzZudiYUgW-S7B8JZAwjbgh_MqlE12bgPqVFME8bpTgzfShBH-wRkX-gACtWCnkaN9_5OqkHr2kayrSC4hKmBBH-kNmAyrGg3dgJWy380hVxtFMXz5nI821tZgUs4oXtwa8qUCiTM7V051t9AxoweSXRrxE-Xj_yHX9_PjLUE6fTRzxAQDQPcw2GnW5GLjmLt55o3jZEZCwmxVlOfrwwBebfuangu5Y7aX7waX3l5pkatmAHxDWDl63Nxx0_8H3fO5L9bubmucd0Ln_s2MHziHuSnpHctWRR4p3NEzjtX2N-XGON4wT0XHICuB9eRHsQbWY2HsqFsrJIbwQFy6hV2JC67v1AzgeAnoMGiTcbTTDaD_b_QApzY_zTVzkOHrj-Apvc3HjJaNjCWPFlfCcxOShTWLC88XhpxAeH_R5Z6V2igliRtMQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9413e45de6.mp4?token=LVWIQIPizRGoJg0pcpUO9-fs9gJoPDLXv6_SIUFwDiXXkB0NMMWBfFLEg3s6ijHTNPZ6soydcPY-xUCJsjKLDAOaORvbXvbhD5il3AOeMNKCpHrdZ54bm_AExZgl3t5TYMUDOogPCi2OsIvJ7lhrwOl_Hpj7RuEhScJ1nzW-anl6wvxc0N8fTeh2Q_YK84rSiVI7zxskTh0OChxLoflqyxm12gSLUeIoBmqvpVm6sdP938dX5qDSMGWGzZudiYUgW-S7B8JZAwjbgh_MqlE12bgPqVFME8bpTgzfShBH-wRkX-gACtWCnkaN9_5OqkHr2kayrSC4hKmBBH-kNmAyrGg3dgJWy380hVxtFMXz5nI821tZgUs4oXtwa8qUCiTM7V051t9AxoweSXRrxE-Xj_yHX9_PjLUE6fTRzxAQDQPcw2GnW5GLjmLt55o3jZEZCwmxVlOfrwwBebfuangu5Y7aX7waX3l5pkatmAHxDWDl63Nxx0_8H3fO5L9bubmucd0Ln_s2MHziHuSnpHctWRR4p3NEzjtX2N-XGON4wT0XHICuB9eRHsQbWY2HsqFsrJIbwQFy6hV2JC67v1AzgeAnoMGiTcbTTDaD_b_QApzY_zTVzkOHrj-Apvc3HjJaNjCWPFlfCcxOShTWLC88XhpxAeH_R5Z6V2igliRtMQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌کوتاه‌وخاطره‌انگیز ازحرکات دیدنی و محشر لئو مسی در دوران حضورش در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28225" target="_blank">📅 09:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28223">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv__OhyT0G-cHN7AsX5KIfbvfTmwPkDHNJXizpDzDXgLtkqaEu38tAfE6SlzwmFUKHc_1HRUHCbfBY9YwnJY-lT5HVRgs19Hc_Bil1mwyUCM6tHMSYG7Wg892hi_zIJEZXe4RltqtN322ga3KBVPT_hSeqnla4wSSiapH2cuNZmMDhy-nkOKV1UWgydUhNW9PovrsFzjOgASw0OkpjEKZbK5WuQ_MnoHckWwauJXd9-iXn_RP9zEum_Wm1EtvksZ28tfZFlxL_ToAyUo4MwtoXcxwADihzdQ29FNw0R1JAOqgzKz9Mr9FxEcLMOtE6JImRx4IqHxi0_H0IfUIrojLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد حساس دِرکلاسیکر در سوپرکاپ و اولین گام آقای خاص درفصل‌جدید لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/28223" target="_blank">📅 01:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28222">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbSYD8zUqKa7LOgbbIKXp1Jij7jOWIYBdx-f72RngaDtNXRJECSKRmsAxP98YGi_Woz2h-31eu645WLhtpX7BHy4LNHn2KRK6Ztm9bN84w4dMi3PHbn49uLIah8Kz9xay6KGglSU3vii2inIpioFhFVEp2LhFN5yuXNU0l8NdDh68JgoibpEccHDYLS8lC3f0gT9zewgHOxLHihvKmSymn8w_RdrUrfXJ5TJ2uo4MCPdGDUQs77ZLpvrJO82Us84DxF4sGgwL4MfcHG5QRkgm6OS7LQkpXQhZy110NvKglfxwKTkLCXxLNngviUz-i1eWhN6xaeC5xqrXa2o8Zq3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
از برتری آسانِ آرسنال تا اولین گل رونالدوی 41 ساله در آغاز فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/28222" target="_blank">📅 01:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28221">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=iDXFdzoA75CYgyOSFyIl_0WsTjG-lPMWfdz3Yo6Oy__eLCN-lBeKt-UCxem2XOxweK8aGYvJZcwPJaPPGXTavsEg_L6oxx2_yOYSQIARHoVyWRemsM-j-_l8ZK-QDQcBQz1VFYzL8egy_IybbvwxDDF4ld4KwObf509886m_PWFX0GnBBYr6shRHA1bxECWkBHHZjOl9_bAFeYoZXXgSU_CK7EyOodXUEraSbaKrU02jmTBvedPTQQkJdu8QqPBfd2gwI1Kb1wrTxlNYmhEgqeGFbClcISsyFNz9-HHT2y-WNXurjdQWgLHP1sl8UQzPWNs-ab6ESB3Qwhm_9Tnz7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=iDXFdzoA75CYgyOSFyIl_0WsTjG-lPMWfdz3Yo6Oy__eLCN-lBeKt-UCxem2XOxweK8aGYvJZcwPJaPPGXTavsEg_L6oxx2_yOYSQIARHoVyWRemsM-j-_l8ZK-QDQcBQz1VFYzL8egy_IybbvwxDDF4ld4KwObf509886m_PWFX0GnBBYr6shRHA1bxECWkBHHZjOl9_bAFeYoZXXgSU_CK7EyOodXUEraSbaKrU02jmTBvedPTQQkJdu8QqPBfd2gwI1Kb1wrTxlNYmhEgqeGFbClcISsyFNz9-HHT2y-WNXurjdQWgLHP1sl8UQzPWNs-ab6ESB3Qwhm_9Tnz7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حشمت‌مهاجرانی‌سرمربی‌تاریخ‌ساز فوتبال ایران، به‌ثمر رسیدن اولین‌گل‌تاریخ ایران در جام‌‌های جهانی رو با روشن کردن یه سیگار جشن گرفت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28221" target="_blank">📅 01:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28220">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80639b9fd3.mp4?token=rmVQ61bFDITH7aG46aL74KraB6kDBBXtYVKoTLd6vnXneiGHYZ660kTa4-St5XMwQSpVPxYX6ExLviAKkg7maOcEVf4x1d7s_0lP59cAb7MpEghCJDwKKe8vmjsUJH2j8lTDqHMv14s2eH5B7L4kNjdfP7jy_pjT04ge1xBm8Rmjo2jHRPkqsV6p-l6NoVrbwSdO457GhLGoXkQHyFbPZFngKSKVv7xPAHZHQnNyxN1GVPCBkemyNL20fjepKphx5KpA8iP6DSpk0jefdIToy_MyPLKriAUhzHtiKbzw-tUSCyJVRRpeytnHHZ3_QIMAoJvCC2YtP9Xlvw3HwHTEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80639b9fd3.mp4?token=rmVQ61bFDITH7aG46aL74KraB6kDBBXtYVKoTLd6vnXneiGHYZ660kTa4-St5XMwQSpVPxYX6ExLviAKkg7maOcEVf4x1d7s_0lP59cAb7MpEghCJDwKKe8vmjsUJH2j8lTDqHMv14s2eH5B7L4kNjdfP7jy_pjT04ge1xBm8Rmjo2jHRPkqsV6p-l6NoVrbwSdO457GhLGoXkQHyFbPZFngKSKVv7xPAHZHQnNyxN1GVPCBkemyNL20fjepKphx5KpA8iP6DSpk0jefdIToy_MyPLKriAUhzHtiKbzw-tUSCyJVRRpeytnHHZ3_QIMAoJvCC2YtP9Xlvw3HwHTEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار از ژوزه‌مورینیو میپرسه؛ دیومانده گفته حاضرم برای‌مورینیو بمیرم مورینیو هم میگه این یه اصطلاحه من که دوس‌ ندارم این اتفاق برای کسی بیفته ولی کاش میگفت حاضرم برای رئال بمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28220" target="_blank">📅 01:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28218">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5613ee8bb.mp4?token=vc3aUD6sl0fvf8XgruNDGqjjAh8rGVmbxjrfvW3Y7PwrPIfQCEAVonWpXQAMs3B1noRQqY-kypIDyHDG3DGv5dOlz6dV34qfEuekfJtr_S_uTDwlnMqNOWycEZA-6pee_dULYVve05-Nim5MKf7bmjA_Zj6Txx4BQwfcd8sZBlv2quNBZswZk2B9uXt_17y5nHdcVNgtIMV7_JHvZk7v7p9_5i8n62X8oYY1SrvlBISiGOa3Tb38ieKgebrQLdtjr9DTgs-mIGg_9wiOGEqeABfsJ7EYm-n4PQtHaonl8k8282S3O6asxJN0m_bWhNOK1JaEYiNRWWBNPNvv4bSJeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5613ee8bb.mp4?token=vc3aUD6sl0fvf8XgruNDGqjjAh8rGVmbxjrfvW3Y7PwrPIfQCEAVonWpXQAMs3B1noRQqY-kypIDyHDG3DGv5dOlz6dV34qfEuekfJtr_S_uTDwlnMqNOWycEZA-6pee_dULYVve05-Nim5MKf7bmjA_Zj6Txx4BQwfcd8sZBlv2quNBZswZk2B9uXt_17y5nHdcVNgtIMV7_JHvZk7v7p9_5i8n62X8oYY1SrvlBISiGOa3Tb38ieKgebrQLdtjr9DTgs-mIGg_9wiOGEqeABfsJ7EYm-n4PQtHaonl8k8282S3O6asxJN0m_bWhNOK1JaEYiNRWWBNPNvv4bSJeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار از ژوزه‌مورینیو میپرسه؛ دیومانده گفته حاضرم برای‌مورینیو بمیرم مورینیو هم میگه این یه اصطلاحه من که دوس‌ ندارم این اتفاق برای کسی بیفته ولی کاش میگفت حاضرم برای رئال بمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28218" target="_blank">📅 00:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28216">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZEOoZdcYyfVuNKJNPL9fFyLN8b8cTSRHicbV4BykGMCQ6BGJcmB33djZS_WGrflJx8AU0wjxW25TXP0ANrEJzJ0DaVqFOzaE6_G0fmO8yZ2UxLsW29NrCOW1PS46unRq3klKfsF66Wbx7koXE6bdphbHxvJy-plhAaSl7cL5Q7a-g_noW8hbbV2CR00HtEFRdccQzyHIkyBjz5REUZCvgYbrFg9WnOjTsDtmZ-XKWFrA8FBQC-8CrPg9n3z6C6PVlK3lKALgUd8QppjnMJACszYV2lI5rqBcD1J7SCV81GyMzX2RDEseBZxhASElNdrGAWu-S4DJNlxizAQ26xp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس: هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و…</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28216" target="_blank">📅 00:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28215">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🟣
هفته اول لیگ جزیره|برد قاطع و پرگل توپچی ها در گام نخست رقابت‌ها مقابل شاگردان لمپارد.
🔴
آرسنال
3️⃣
-
0️⃣
کاونتری سیتی
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28215" target="_blank">📅 00:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28214">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVFEFfnZRdLTplZhtMSb9x8p3NiUZASK23lIOBd6UqDj_WqgPTEXkYdvT_9C0beSPQg1LZQ5ZAhs-tp7MmeFMpBSJEyEyPp-gOLDQerodayy77bLRQXWgoZJrJCkDED-RIWhqs7d3VM-3sT79zJ9YPI3K_NfHhhS9jjJlk746a74Gs9npsNzOjunp-damOKM0nwA3q08Ie3FbbSzIQDNR5ggnFJ0BYw9P5SjogBeyBJ65KGBQ1aT_fDr577436BPokctrBrL7hwxmdn-fur5GHyP5WOQMd3iEzkmSm0dxqnM79Qv9Hh03CbBb9EqtspB_NZlEmEvGneCYbLhdLeMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ بازی افتتاحیه فصل جدید پریمیرلیگ با دوئل تماشایی شاگردان آرتتا vs لمپارد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28214" target="_blank">📅 00:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28213">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6905786d2a.mp4?token=WDHtlnMpoZfVo7II10ktVbglKTtG6rpxo1_K4TuhKuyE93hnbmhbuwD3QMy0ZG8Nm-GnXV6EUT1XTcsEq-gN-9Y_x39pityUlLG7IJ6KP8KGqX-ph1c10W6NIQcV9-1cji5XmMKRg5FYi_ek_9TmZTVNNFEIbSnu3GvRTUtZvVa8lGWZK9tP2V1WPGeEPKNxyDHAQHwzH0ZnA9WmSRkpg-HVm7jcLMhM0kHJtYVknmp6QRRRb7O7iTgHm-f28ujH8cAC4TXo-BbJNyQffazU81CYPluCxLGQnhWhHOFeviWwYnDHjN6x6WFDGDX_AeI5ZDechrBQH9VP8JuGoshmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6905786d2a.mp4?token=WDHtlnMpoZfVo7II10ktVbglKTtG6rpxo1_K4TuhKuyE93hnbmhbuwD3QMy0ZG8Nm-GnXV6EUT1XTcsEq-gN-9Y_x39pityUlLG7IJ6KP8KGqX-ph1c10W6NIQcV9-1cji5XmMKRg5FYi_ek_9TmZTVNNFEIbSnu3GvRTUtZvVa8lGWZK9tP2V1WPGeEPKNxyDHAQHwzH0ZnA9WmSRkpg-HVm7jcLMhM0kHJtYVknmp6QRRRb7O7iTgHm-f28ujH8cAC4TXo-BbJNyQffazU81CYPluCxLGQnhWhHOFeviWwYnDHjN6x6WFDGDX_AeI5ZDechrBQH9VP8JuGoshmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکت خفن و فوق العاده دیگر برای در آوردن سیکس پک‌های‌شکم؛ این‌پست‌های‌کابردی رو یجایی سیو کنید و برای‌دوستانتونم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28213" target="_blank">📅 00:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28212">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWiu3DNuZ0ZewIi2_FTdlWmudAaqpdGuAyMjdxBkN29JM8Pee4ueNOkzf6Tbf_OS53C3yDNEGPW0uXoYsjuvI7exWl-kgh4n9x4sgYnZjuct3APIUd-OgrrK14BAhewgFAhEBdsAR4fNJZ6h17zc2gwWhqQuu6oytY9zbtjCJCGJeeL4j8JL1BIhfAm-PDA0iN0da1S1LudhvddzU1sjiWxPVnexRVcCgFpnLuidSI78vimyxykZn3MEEvsIib8w4JHTclNai-gMy0c_fBuugLINs4fSUOUZEdW8nzlPHrZB0JvxjCkUKoCdGPi9PX6ytSDZArvI_Ne5w3GwsatlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باتوجه به‌اینکه ابوالفضل جلالی در پیش‌فصل مصدوم‌شد و جدیدا هم‌از ناحیه کشاله ران دوباره‌مصدوم‌شد. مهدی تارتار رسما درخواست جذب امیر جعفری مدافع‌چپ 25 ساله فصل گذشته گل‌گهر داده و باشگاه بزودی باهاش مذاکره خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28212" target="_blank">📅 23:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28211">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS5-Rhth-fUu01DMWBGdCH8dnQbFjGatuEvW-qG2gmnL1z-vAASOYP3_4LvN9GiiRLyEMVV6RGkB3U9rWIygyh4T3vmmG9ZLI-ioRT_arBG5T86FbY_t3bgxcGs4YKbTynD8yqHIXDZ9ikGIXc2TKnN4npFQ_o7ok6iLQBTLEyg3oel6rTwQNKWPyC_8_UnAZgdXMNBR4n65hgHY2wc9n5GJw3HURWRhO5zwnlPt5X076QMbgmU89mXztApuYYUKkVVXYJZP-bJjjNXSziQ3XOJTfyFMjTZ3_fl0nyd0N56kRixGXqh9LWQN5SlEOHf66TDZePS6-QVLc6xE3Sc0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
طبق جدید ترین اخبار دریافتی پرشیانا؛ باشگاه الوحده72ساعت همون"سه روز" به دو باشگاه تراکتور و پرسپولیس فرصت داده که یک میلیون دلار بابت رضایت نامه محمد قربانی پرداخت کنند تا این انتقال نهایی شود در غیر اینصورت منتفی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28211" target="_blank">📅 23:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28210">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6rhGs7BAdurAtB2nm6T_hPQl3OqVaIDfutKILLLPCHGiyIbKcm1msKCPSQxLQAorZl9QE9oPb3tZJUtH5P_x67WBBLhLvU5yBAGHOwVxZsahijgjZcBEOJ-IPKD_AM0FlBZWjZvOK3yoRUCV9QM_7C19nP1OeuZUadmD3Z_Vw3P6nOy1yN3ttyTWYrXUQZp5TY5sgzd_APiddl4rly7HNSeOT9P10jUjivaTkkVhWFaNFBNCtMD7CehSWx46Xi75friZu_JwVj_imnkBRBK5hi0ummEAxJ7y6SpExpd7JL9vBuXqJf1ve1kWAv8dhA6dwgExX0Tm3cbBZtbfCqO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فردین رابط ستاره‌سابق استقلال در کنار همسرش در پایان دیدار روز گذشته تیمس در لیگ دو لهستان؛ تصاویر بیشتر در این باره در ‌کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/28210" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28209">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snOxOKy7nVvyb-np4xLoJwc8jqZUkjs8_IrZUsXV2OJTRgakvbHQPwA2LHvbDMeqkbiJdZKKuYghNUyYV2c-c9aGQohbRlPiH0OufZJ2XYVVehPooPZ4bhrvQFYhxCodUyfHWCoF7FfwlQ8b9_a4AI1OlY5zNbLS2tH8ix1Rc8U3GRo1WiNmBpKRKVuqqlG9Rajp1GOgQNi07PucvsOjl17isTplKkyrPd-yTzTG5XpCBMy5itHPmU0cwf7lpexSfzNM3DoEunXGXgxxMVuoudZkMaCp9P4MBlpoGm3mfUHUqqV_VOyIIxJQj4LWa9ZmHYQ_T06q3p7EzPKN3gx-Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
گاستون ایدول خبرنگار آرژانتینی:
لائوتارو مارتینز قطعا دراینترمیلان‌باقی‌میمونه‌. هیچ مذاکره و پیشنهادی ازسوی‌باشگاه بارسلونا برای لائوتارو ارسال نشده و این انتقال در این پنجره انجام نخواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28209" target="_blank">📅 22:38 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28208">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/948db539fb.mp4?token=cg5AagQhelNCVRIN-YF2dwzKwdI6X_EM1aM7qn83_oBbmOE6MqzX0g03BHbNxNuPL3ZJ4crGrJtBrrOWj1RjQC7GLZVMwAZxhFFW4Hh_4v11_xoHwiOL8g99JLJ-Q287qtNpan8Fe_ffWyhQ4XPmfX-ZM8d21eMA2mSGqan9eytmXRrlhPpdVk_baEeKiOTS3uFwIrN4AFjtDiNi4bGdA4pCBy5eYq5EZE_CWn24T_mEvEs9DQRrNtZjJX7JCXGFJo4JsS3f8dDWVwosMiK-76Gc-RoAgc3yJzgZI7AlSjYFce9sEqZ6KBuOUYZcsP7-od6RaiNi05T4LJgtnLI3UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/948db539fb.mp4?token=cg5AagQhelNCVRIN-YF2dwzKwdI6X_EM1aM7qn83_oBbmOE6MqzX0g03BHbNxNuPL3ZJ4crGrJtBrrOWj1RjQC7GLZVMwAZxhFFW4Hh_4v11_xoHwiOL8g99JLJ-Q287qtNpan8Fe_ffWyhQ4XPmfX-ZM8d21eMA2mSGqan9eytmXRrlhPpdVk_baEeKiOTS3uFwIrN4AFjtDiNi4bGdA4pCBy5eYq5EZE_CWn24T_mEvEs9DQRrNtZjJX7JCXGFJo4JsS3f8dDWVwosMiK-76Gc-RoAgc3yJzgZI7AlSjYFce9sEqZ6KBuOUYZcsP7-od6RaiNi05T4LJgtnLI3UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28208" target="_blank">📅 22:28 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28207">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROrd_fmohZDqMYpCoouPVYNM50pyWuafQZiWDYAGkDZzwMh3PKq7XRHaDEu-wm5Lt-LcQ3ZGkV7fEentFLJrimBfHD7818vKDn03RPumDxm65nNsR5ImNcxNf7a4eURU1URmVQi4XyDfYA3txzAMMpuZXnJwnV0ymozGnb9XrejNwefp4Y7cdpCov_gP74MxB4c3UkTLyZWzGttPH0XunWVxdT3C8vviJeioSdu_W2Ks9Kf-eGDjhImCJLcNToIzx205dBoNAMZ8LKOur_vqkhFWWciCPOyx26aULT--NUEcUHb8-IoCGhZRvym_h0KNa8TqLn4j4lo3Zh2JUDhdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درشب‌پیروزی‌شیرین‌چهاربرصفر النصر مقابل الریاض؛ کریس‌رونالدو موفق به‌گلزنی در این مسابقه شد. این 977 امین گل دوران حرفه ای CR7 بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28207" target="_blank">📅 22:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28206">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ijQhgiCPNwEbBuRGEZxdRgkJ89RKTX0OK7aDLQsOmNt-w73rA-tBbdfv0xZZ5KhJf_ukjiiejogttVTTTip09ik9xIFXR4MyTNM6JbTTDxySnlQZ4O28OIrAYL5RLGrxbWZl0EaJk3ryoYAVK5dIW5TpVe3EBwogrniO8QrnZ2JbzkahCIMtneQoucZLRFWxw7Paf4OkfVFtj15Gcp62-2k95ZGLachR8ovR9PpKMjm2lWB14WGTl0sTEDa8xSTdz2VAC81YCQA9e95PcGvrHaEb3ydv8dWwgnSAC_BHUblmubQ5Ed9_VdqoyOePmVpHi6Vl2UmgVGKrJ52cIEp1tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ایجنت‌ایرانی‌نزدیک‌به مدیریت تیم استقلال به فابیو آبرئو اعلام‌کرده درصورتیکه باشگاه چینی بیجینگ گوان به او پیشنهاد تمدید قرارداد داد این پیشنهاد رو رد کنه. مشاور نقل‌وانتقالاتی تاجرنیا به‌آبرئو اعلام کرده که هیچ مشکلی در ایران برای او رخ‌نخواهد داد…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28206" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28205">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxTZ5vIVWgCcWUS5ikd7zvQJ62c3FFepMwleCziiNSYvSDd8oiSeNjku4QMyNMnR5s0PYvClsS-4uLxIHuVlgwxbvaODs6VQ102j6_yXyOT8ML7USp5db3uygpoUcWdJ95VdlIW0iOjEQYJaX_3LGvk7v3DG7lqinfh4jnm17mUPYEXo2Nxe6miwsbcoNDKbAVrC0A_fLmQ_418Hq9Sy6Vd9uq0dhevRX9QpTZ0Pb3mPjkgKGrSEDzZYyAnpic3o2Sem_Oxp85GXpBrdn6MoxMxalCMj21TA8ylpv6Ppkb4U5pIUzOhBIOe2mWRU8jvSpPt0iVeEfhpxC6p-0BoV4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی طارمی از لیست المپیاکوس برای مسابقه این‌تیم درهفته‌اول‌سوپرلیگ یونان خط خورد و عملا از این تیم جدا شد و بزودی پوستر خداحافظی با او منتشر خواهد شد. مقصد بعدی او لیگ‌برتر اماراته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28205" target="_blank">📅 21:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28203">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6923293dae.mp4?token=EtXWQB9ZFC5S-3-PShrT2NqqpSeAOLM5CEmDE7v4v69DbgXOBlSDCfl45U1UjmSFqqAJSHq2awtavrBREZTAYyLPhnB2tOwdLgtuUIk2Pp9jyfPgLVgLyWzzlXG-NydYYw-JvU7EpTcnGo4VZVA8Xe_kGD9h3Q4HcDI7YWAcgCzyH-ER3Gl6tLFoB10BHEtC051Dw-iT8MjvnDjirV0RPuimTVVX9nnOkZ_vHOQQ6Pgt-ZFMztWiSvo3Gv-aRyQV7xSU8IWnfAq2BGHSJ80oobKR0-DQrT6DqBq4VLc5U45gTT3MbT7yU78SlNnPIwsmTAY0aJP8Ad3m8m31mY1iRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6923293dae.mp4?token=EtXWQB9ZFC5S-3-PShrT2NqqpSeAOLM5CEmDE7v4v69DbgXOBlSDCfl45U1UjmSFqqAJSHq2awtavrBREZTAYyLPhnB2tOwdLgtuUIk2Pp9jyfPgLVgLyWzzlXG-NydYYw-JvU7EpTcnGo4VZVA8Xe_kGD9h3Q4HcDI7YWAcgCzyH-ER3Gl6tLFoB10BHEtC051Dw-iT8MjvnDjirV0RPuimTVVX9nnOkZ_vHOQQ6Pgt-ZFMztWiSvo3Gv-aRyQV7xSU8IWnfAq2BGHSJ80oobKR0-DQrT6DqBq4VLc5U45gTT3MbT7yU78SlNnPIwsmTAY0aJP8Ad3m8m31mY1iRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آمادگی بدنی فوق العاده کریستیانو رونالدو کاپیتان پرتغالی النصر عربستان در سن 41 سالگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28203" target="_blank">📅 21:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28202">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jazf29o8qkTzRSAKQ67AAsFF5Eh88XWqbEFr6M-PbUFqDlHzylIEGyMiONqE42Umn_XrC1ShWRQ8GAgNrsAbZ_yLNTrNCtnbN9VK1ecjRess_nY0iIgoR3POKsLbW11czqWCX-IfUdXZ5Ok1nA1yXj3KY1qDMuFyZ_fTUoiHqTy_dE3rYc8QYqVdkVZwScam8Tr5oq1cDKLFb2HPjUYF-GRefrMzapCsaTQAZtpGF3PSMxzvDCuNqM63KAOEMKBxdlmCA2UZqssUM1g8OkkWa5C5gqcLdq_8TtraFpE_EvouNJE6xHfYGcvmOp_Mjr63aJtzGopHbmVFTwI7gmzhTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/28202" target="_blank">📅 21:13 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28201">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-5rsXm3mxlxBkBk25z0aqO80qIckwTBC8NXtjgtSB1sktP6G1sRIRsynxmp3jCBDdxwrb9_a83iIvqJN7rwCMcsXFl4KixkmC1UZu2f5NFDIKLJ4diAaBShKfnQNxztZarSPGdJLbwBXAlaiY1kLJfuRJ3Fw40Zf6OpFIhDdZwxs1NFmwCki0_XlxIzXwufFg_5e0culI9sMC7ut2ZV9BUDQFCwdIjY1cNt80c-u8LOXmGjj7JYYC1pmUjzK_QelDWWUz5TAzjWoL2Z9ue2jvScyJFsRnZLy_DRcA1j1x-3Y1lq4AXJZQ1_YEkilhQ1l1RwBrGITk59C6od5IioXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
شروع فوق العاده الهیار صیادمنش در لخ پوزنان لهستان:
8 بازی، 360 دقیقه حضور در زمین معادل 4 بازی کامل، 4 گل و 2 پاس گل، نمره 8.3.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/28201" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28200">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ui43KM3JhmQF2bIq0UeC9Yo2hCKFa-pX5FxuUN6YoH_y_5pIzpfkTOMckxkssElwmG7Erx61mRIvBS-G0X-xH0qCqzh9SyXubVsQiRSXnv__4BR4PNPBQF5AX7jtiqkoRbKB3gnpvjdI8ye98kwTeIrPFBTpEr9qhro4lmS3fyt1nUx-ee48LULwO1BmjrvIfFuSTIIiPdMRF97zyrfZT3OQIwMimDjhCACwjEheO_PJ94ZvoFge2AD006_Q8iQuRPiZYp51A-4T7ot8O8W-UO5N_Vegp-35Q0uUA4Op05OMAj-XP0PLsRjRnckurw50qnfN2mgzMw67vAlQUE4kDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
گاستون آیدول منبع معتبر: بارسا میخواد آفرش برای آلوارز به‌120میلیون‌یورو برساند. بازیکن هیچ علاقه‌ای برای بازی دوباره در تیم اتلتیکومادرید ندارد.  هنوزشانس‌خوبی برای این انتقال وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28200" target="_blank">📅 20:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28199">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3847125faa.mp4?token=IXiB2F-a6_paiyjerY_Rynz_Xd9YPhLh6fhZhb1u0Ksysz6L8hDrYvwJtIddPLtskQ08F2mxEPG4av3--j6Q41N8_o4kPwWB-4OCKd4FXR3wVbjMRdp8HFn4I6kSnrqYJ-3YdU0xaVXUZuvexwuvqbN604dHFBoHBU8Xf1GIj-xMcF7zg2lssFJbPQPN0j0Nv86Go6-K97qS2sAsH5CG6gHIkUe44FYKRQr1ZpOQLD8s1mA8yRu9HsTeY3P9scMOUVcvD-EyB-R6JsTwsOUiUHQV9Hq-wIMlvebRJUQh8WKuYoNU4U6fKanCx8tnNCLX_ijoNJLownCRJa9FF-lZIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3847125faa.mp4?token=IXiB2F-a6_paiyjerY_Rynz_Xd9YPhLh6fhZhb1u0Ksysz6L8hDrYvwJtIddPLtskQ08F2mxEPG4av3--j6Q41N8_o4kPwWB-4OCKd4FXR3wVbjMRdp8HFn4I6kSnrqYJ-3YdU0xaVXUZuvexwuvqbN604dHFBoHBU8Xf1GIj-xMcF7zg2lssFJbPQPN0j0Nv86Go6-K97qS2sAsH5CG6gHIkUe44FYKRQr1ZpOQLD8s1mA8yRu9HsTeY3P9scMOUVcvD-EyB-R6JsTwsOUiUHQV9Hq-wIMlvebRJUQh8WKuYoNU4U6fKanCx8tnNCLX_ijoNJLownCRJa9FF-lZIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شهاب زاهدی ستاره سابق پرسپولیس: قهرمانی فصل قبل رقابت‌های‌لیگ‌برتر حق باشگاه استقلالست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/28199" target="_blank">📅 19:45 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28198">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03ed3b401.mp4?token=BIr9kgSEBTqZM2epCkZZBu0yAwcmK1aj2Xixo55XCle1ogGnBtR1vApYKkWC_xCDIcLxTD2qmR1jH9tWXuTl38wshgWc1BWilNAT0FDRQsLq0VUcpxw6NW04d4q2y0txU5BieIlZmFiX6bJOg6Rh40vfPia5bC9mJO5N5YMEJENFDegceZFF46nyzKu5RRmC1PJCKT1wRzr1L6tlSmZdIaoy_lHbgHySuNC7xHj9spyvbRyPv7No_Ym87RIvj3L9s3KbI_pt1Pnb9A3ymfI1owatmytfCjTLk0n4J2AOCLYaH8FHvaG44txUKrxcLQYHe5vfQmFpJ5RE14Dy5yOtiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03ed3b401.mp4?token=BIr9kgSEBTqZM2epCkZZBu0yAwcmK1aj2Xixo55XCle1ogGnBtR1vApYKkWC_xCDIcLxTD2qmR1jH9tWXuTl38wshgWc1BWilNAT0FDRQsLq0VUcpxw6NW04d4q2y0txU5BieIlZmFiX6bJOg6Rh40vfPia5bC9mJO5N5YMEJENFDegceZFF46nyzKu5RRmC1PJCKT1wRzr1L6tlSmZdIaoy_lHbgHySuNC7xHj9spyvbRyPv7No_Ym87RIvj3L9s3KbI_pt1Pnb9A3ymfI1owatmytfCjTLk0n4J2AOCLYaH8FHvaG44txUKrxcLQYHe5vfQmFpJ5RE14Dy5yOtiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
بازگشت‌عارف‌آقاسی به دوران خوب خوبش؛ اعتقاد بختیاری‌زاده به عارف آقاسی او رو به دوران اوجش برگردوند. مدافعی که دیگر سوتی نمیدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28198" target="_blank">📅 19:20 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28197">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb84d0efe1.mp4?token=TgIEjIA75lS8BtODf06YKvLiEQI7aIJQyxfBF-OMLY2skdj21sjChaX_O82N1v_2wwb-capOei83WoW-iKYWV2MraXeXLpkqt3E6yCOOqL1gaaGrLRyrvkcnEP7X8ioAXsOL8dclIwetp7aDQAYqqGbvfnKZFiU8_rmm_yXsrF4H7YVkAW63VMss3eoOF6l1kZCB9We4B1s-33MyEM6oV0Lw4584WZBtl77tPcGvIWiDn9ntF83d4RASYS98DChqgZeOHsI8_uGK12722kWcvADg0TLlaZYGuWLSLVeGnh3WleaWbA8loYiYA0WLGOo50kFSY7Qm_xni0aVZE8z0EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb84d0efe1.mp4?token=TgIEjIA75lS8BtODf06YKvLiEQI7aIJQyxfBF-OMLY2skdj21sjChaX_O82N1v_2wwb-capOei83WoW-iKYWV2MraXeXLpkqt3E6yCOOqL1gaaGrLRyrvkcnEP7X8ioAXsOL8dclIwetp7aDQAYqqGbvfnKZFiU8_rmm_yXsrF4H7YVkAW63VMss3eoOF6l1kZCB9We4B1s-33MyEM6oV0Lw4584WZBtl77tPcGvIWiDn9ntF83d4RASYS98DChqgZeOHsI8_uGK12722kWcvADg0TLlaZYGuWLSLVeGnh3WleaWbA8loYiYA0WLGOo50kFSY7Qm_xni0aVZE8z0EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
میثاقی‌مجری‌صداوسیما دیشب‌از پوریا شهر آبادی مهاجم جوان‌پرسپولیس انتقادکرد و گفت باید میرفتی‌ قدردانی‌‌میکردی‌ بابت‌‌پاس‌گل دیدنی‌ بیفوما که این‌حرفش‌واقعا درست‌بود اما آیا خودت از عادل که تورو بزرگ کرد و به رسانه‌ملی آورد تشکر کردی؟ یااینکه رفتی شکایت‌کنی‌که پلتفرم 360 رو ببندند؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/28197" target="_blank">📅 18:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28195">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QLpZ3EwaDPHVO3TSbE7AnZJB57fvhBv085mCtTaqIVns29Pjwv0f2ntsJxkxzbrYUA7yT3jBHlwxXJxrHoQ1ArNfD6pCiaw-V2KPy_ZqB5-p_l2BedxT_mVHnjO5SaVZRLaW9JwGnZXs08IWCnR8yWPNxxmNmCXAKCJKAySkvylZ47qx3q65RIptPbR6UEl2YeAo-Hq3ThRPIiOdMb5UmOegN37Hyrid7BFzRWAP8DnqHa2ZmgdEZpPFq9ouPKM3x1-OqHXxB6LbVP1aNu3JhZX2BRiq7NUQ6a8d22ujqrSweP7oQ-g5m5b_SSqIGLbV_m7G9c_MXSveiyBD8oyIsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5PNnYBakJz4IFOlifR_ldsd_NAEMRwjQDMSoW3lz9QGd5nnOEipB8OGh0Iaxw-qVLMg_F_TUyYnTiCxGltPCsSuwfo90Kdf4PHoOldIEzEcAbWU5EoteWTJFg-2mY1LckIw7svgbzfjvQTTCWDLTFm3Aw9YX_MNuznfsvb1kGnqAv5hBlybr0i0XI8s8hgfhx5ZxFy4DCvW545FRzs5evdAecxPPRt5VyQZNgXqN1K6tLmrD9gShkLRpKh56Cb7c12mOJgT74iaypSWPTuLFYcZPBaZV1uORDTjleBdM_SafEV9Oy0ZZDHMW_PmiPM7Pc91hCPRpWv2qiAPElJFOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
علی‌دایی اسطوره‌فوتبال‌ایران بمناسبت تولد دخترش کادو براش BMW X2 2025 خریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/28195" target="_blank">📅 18:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28194">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FXUk5ddk3qV0R3jleRQokxOJuPXIwU7u-H7HA9trCyvUfeWu_WKSvua8O_4z0QvREeWcnojH93syAkS3E5CV_QLcsdH0x73cuzMXfijNoVau9cY5RWzOfch8SA88czZmu7mNDXA_FD0wYr-kgJxAXViwNvcDNbCvPRHWmc2R1Cy9sVWxNKsrHTj43U6A7fwo5hd7EECOfol3XoNTb9YOk-Op8UnPgS4D_BJEKW_JybyDCaRWdEWppR-MuKEulT88d_JN8EFY_15u6AT6btYkGRk7By3m0CdZ6z41Rt1Z6i-e4KAJn9jFKFhozk49xfKurAw_Vt3fLFgifFuuL6N83Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا ستاره تیم ملی آرژانتین رو نقره داغ کرد؛ بااعلام فیفا لئاندرو پاردس به دلیل ضربات مشت به گاوی ستاره لاروخا در پایان بازی فینال جام جهانی 2026، از حضور در ده دیدار ملی محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/28194" target="_blank">📅 18:35 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28193">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZuMXv_7XoIwOfR7mGQ9erCyc-fUHDHbKSqFnTNgcWoJ93c56E7mvvo0aAh2XxlPHC1dQ3gv4FDUWxSx0jOyR_EF-d2PANP8tzKQnZcL_B3uhgcmnHNhTGTHyIB-K_AiEVrHPTAp2CyB3pu1EIOVVHferRQyYjs1sJj7vAlRPsk3yp7w5jqTeQ4_t3ylWVf52iSg0VQvM8kZoxJnF7kXV3Kw_sBMl1O7Vx54UZyXdhs1540tq2o05zQZUfYJYbzkS17j_mWrFy2C9SoGg8rNxRNg1bVepci4enGx9CYkkcHdVh-EDA_vmvviAIlswYRr9cZvqjSV2vWIdZVvLipLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیفا ستاره تیم ملی آرژانتین رو نقره داغ کرد؛
بااعلام فیفا لئاندرو پاردس به دلیل ضربات مشت به گاوی ستاره لاروخا در پایان بازی فینال جام جهانی 2026، از حضور در ده دیدار ملی محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/28193" target="_blank">📅 18:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28192">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTUoknvw-CJ_yKldLT2LG_dHnp0Rw6nZUcbNS8phIPdY_1_a86Drh-PIhZL5CZp95Y-HYb2xyJMW89wa-LQbsxdYKeZzGgMBqCyuhabA48LalzJQctzYzXeV3ZDGo5y63dgKiHHI3MzE9Lbj9_3UGK6xzDMPw6rHWv0NRx5xekhkv77HkgEUNUTXY60ByC7L5jF755C5g6pC-ma7Gjutm2IOPDMkOKxqSldqIBqhu0atFO1fX6Os2wfiGgdp3kyz8xx02wipH-BCkNIWdJNqu8oEZrWJN0ViJPylsDWwhGsALtsPWsWoU0m6-iYKMKXA5MaZCrldGUumSM-OHEFgZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ امیر جعفری مدافع چپ گل‌گهر در هفته‌پیش‌رو برای‌انجام‌مذاکرات نهایی و عقد قرارداد باباشگاه‌پرسپولیس‌راهی ساختمان‌این باشگاه خواهد شد. حدادی با ایجنت او مذاکرات مثبتی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/28192" target="_blank">📅 17:51 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28191">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGk_7jf9tbBWm3HWASpCGJQnItBFNvUsG6WePTSM3cRDPgpsMj37re-_6ppWRgOcfhje0RqXQOyrjTf7wTjNXFOevhNoNkZtIUC4qHx0qMhgIddGSCyJH6rK1CWPJ-zElA1QHvbZHM-3IlO55_2ugy1KRA-Qyh3I6pXr-o0lwGq48vWoDhD_QCIrM_My8ZUX6YjZcNkQ-Dhv_7q7-V68GvfzJbE8R1C37c8kZcduLtx2cCWeRm7QaRJVDIzrJe_k-yHFSgPgl45ZFlyHKK2Lf_fV173QRfhfw0TOznzM-bNqFaNQcnWI3oVxkJ4JZCilges7Ly7wx9Dh1MTUCb28MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28191" target="_blank">📅 17:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28190">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RGY2T3xNhFAzLRmsFemF0AZ-sByox7tWF6sKXGRq1ZRmfMkiccIeQSpkFHVlsnsrbgNKKhrw5rA8aPh6xg59YlWl9JNhb_j_uSj9DDmdt-odbGZ1Mu7KoJfH42-iB4DetuZBaOQRaUEGjeTJGf4VhNzCehS0NnZYBv40SCKfXrMVlQGXVSZfpSMWooFIt9VLRNJtLMppfnqMTGABGUNMtImUSL7SfkYKMBy_Np3du-cqf9iyErFnau1rxFKqP86C9JKmq7SMK-EoaTyMXZl8Ww6RRiMM52aVB1u58NS8mIbVCNwVc5dC97zCvJXylN_lNvt3-8z8xtlrydl3foHSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه الهلال برای جذب اولی واتکینز پیشنهادی 45 میلیون‌یورویی به آستون ویلا داده که به احتمال فراوان باآن موافقت خواهدشد و این‌ستاره انگلیسی با قراردادی سه ساله راهی عربستان میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28190" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28189">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18f9090bb.mp4?token=Ss7Exf6yR3xt_BMcrpDlgdSXJ-a1KBoS_Mn8JNmjaq9UPqrj0J1taYy-zOwBNQaGp5eDqfMU5Hn5txJT_h_40qJRQVZDvwe7Az1uMzTNPYbE2yHB6DYriV2mCkWqc75UfaqBeTAshvuJNw1vEyAFe7M6NqMmHV83WU7jsdQTuTsLpLW-Q2u-Ehg0UfiGvraGmmRQfbwOf62enHSRh_44z96yAYFjEduYxERTG3dLzYKe46gycsTCtNgMWDBQWWS05qXt5SEFZhsps1PMQ-pUWrsB3cPtknMVXWnL94kqXYuTns5IXQaJnLy5H7bUciQiMGPgJYv_0H6e_BpfFx-iEKgXXM-fXujIYfrhe4AuW4YlDdTWzDvvxH-AvwVKoXrQyg8Qfhuapw0O3N4FVXNgCNw7OyucldCdHdlehI2iSLza2U2wVMevYgXCCCq4U7bSQlEs7MZTqdAAtFioQH6ONxbgtL41qT5-IpmT31uKMxbncMZ3kn_OiJtLjrrPY0q6pRu7sPvWPmdKkPQMDymTlN6vCWiN3o0mmVw8hEiq7ouqDDOy0blSlxJ6wL7R_M-Df0_sJkSXcyH-5k0y83UfiKl1Uuvz2znaNg9xilpwYYtJZZe4MgN-OD1bh-QOmsR56dw_fyTxID03zTbSwdWBuI4QUeTmwjeWUxEvQq2Rfvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18f9090bb.mp4?token=Ss7Exf6yR3xt_BMcrpDlgdSXJ-a1KBoS_Mn8JNmjaq9UPqrj0J1taYy-zOwBNQaGp5eDqfMU5Hn5txJT_h_40qJRQVZDvwe7Az1uMzTNPYbE2yHB6DYriV2mCkWqc75UfaqBeTAshvuJNw1vEyAFe7M6NqMmHV83WU7jsdQTuTsLpLW-Q2u-Ehg0UfiGvraGmmRQfbwOf62enHSRh_44z96yAYFjEduYxERTG3dLzYKe46gycsTCtNgMWDBQWWS05qXt5SEFZhsps1PMQ-pUWrsB3cPtknMVXWnL94kqXYuTns5IXQaJnLy5H7bUciQiMGPgJYv_0H6e_BpfFx-iEKgXXM-fXujIYfrhe4AuW4YlDdTWzDvvxH-AvwVKoXrQyg8Qfhuapw0O3N4FVXNgCNw7OyucldCdHdlehI2iSLza2U2wVMevYgXCCCq4U7bSQlEs7MZTqdAAtFioQH6ONxbgtL41qT5-IpmT31uKMxbncMZ3kn_OiJtLjrrPY0q6pRu7sPvWPmdKkPQMDymTlN6vCWiN3o0mmVw8hEiq7ouqDDOy0blSlxJ6wL7R_M-Df0_sJkSXcyH-5k0y83UfiKl1Uuvz2znaNg9xilpwYYtJZZe4MgN-OD1bh-QOmsR56dw_fyTxID03zTbSwdWBuI4QUeTmwjeWUxEvQq2Rfvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
جو سکوهای ورزشگاه پارس شیراز در بازی این هفته فجرسپاسی برابر صنعت‌نفت آبادان درلیگ‌برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/28189" target="_blank">📅 17:24 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
