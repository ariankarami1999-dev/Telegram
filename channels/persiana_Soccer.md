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
<img src="https://cdn4.telesco.pe/file/VodC7mPs4FrQXNI7816SdJh8oz1GJxa1vr6Qo63Hy4sSZ0Drh5plf5xmY9lEj6aY4UCtQLNcQzbxB99TAXB2qf2Wa1ra4Ka5NdmZi5S6dAwKE6OjMOiWkJgtyi7UHglsutJ2uc3YQZRLQbM4yD6hI63HLxwO1Afrrm5VVrhxh0LqRU9O7NY4_v03619P7ozwcAzfz01Az9MuhN_dZ5Q3BLgOEgxCoPYwdBY9XP4zztZDBLTL5dLe7NaGjg4H6t5sZSKnkQ6BsSYVUgOSv0hUZoPwVKE_6JlW7nICtdbQh-Eg6NocZEycvj09DYEJl0MYoHN-p_qHIro2Rf1FQ1hAnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 527K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 14:49:00</div>
<hr>

<div class="tg-post" id="msg-26138">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sftX0W9nj_Y6fQEZeT9GLtDijRZkt3w0pJcvWDYA7n4MiRJu3DAIwanVNKpgZhSGy0SZe7MD4BcCPaH_-8z2EWCFxWe-ufmRyIib_4Z2RjDgiKmbnf9LCWulFcwlutL7RbzTDO97jQoDXM1ILj-vKmuQTg2mVffB1Qu9yMP0Ort1WFVraQE6zBPsydpt_5tVtoAiVeOKPgTYORDi6Wy0iCW7_0y_drhHY_HkyVKx2mK_aQ0EpYvun6Ynzlbfzq1kuCpJIUPUNb3-x2pDdFXsbwc_ObV9zrzDRud9SgSMZ07ZALz0I5dZ8EcllQ4liD_0Y_IP86jmNnCa1tWdtIKBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
آرمین سهرابیان مدافع میانی سابق تیم استقلال باعقدقراردادی دو ساله رسما به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/persiana_Soccer/26138" target="_blank">📅 14:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26137">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gom1r_2UpwmMSlVfe6YTTN485mJj1PQ6o3XkrksXXPyM7A91GLVinAGSBvIDGpguBOToJvewj0rzgGLIPwksuXsFgRdBh_pDaeEMF3jUEBmilUsnr7IY1ueWS6FglkvdjODS2R1_0mYN4xH5aAuCJyb2ZjyyXTZObY4SFyvff3tdredsgpLjrXAvo9QN2ft0nf9fvxmqHFSnTRPIsPln35GRAxTRgTcwejEnskUhvO0DWid4zWz8-TMFj9ci8_M4rsVrSJDs7g0Nm-jfCAkMw-LqHIlP_H_2DWpULGYAKKjD45ur7OsFglzKpfVWPEpYzpT9LpJvAmg4C5WAFfA7bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام مدیربرنامه‌های عارف غلامی و آرمین سهرابیان در ترانسفر مارکت؛ این دو مدافع میانی از جمع آبی پوشان پایتخت رسما جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/26137" target="_blank">📅 14:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26136">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">📹
ویدیو کامل ویژه برنامه فینال جام جهانی 2026 شب گذشته عادل فردوسی پور؛ برنامه جذابی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/persiana_Soccer/26136" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26135">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbkR_UUOz2FCZYJGPFE3K33F0JZEWxm4zwT4COkbec6p0P5ZgR8XzmmA4p-vTsYJfYJwsHPiaK8t7xwzHsvNgU18NESrXLRAuUPc-GvGLj8Vl26aRVL0ZDP1pT_Wkvbis-oWXV-C4kJ18-TW-85OBgjoiYYRBtZeJzBxF5vEAvLafOflknCzQ7ThDtCgpym-1tJmmJEGi7BPnpPRYqmVf0etkV7wBbIlywJPi-bxgTvextONXrXykqoy-4EESCIoe5flN50gGUSZlmgXm1Bbh_NjgFBu9ugo8GphoVeBRTF6MjciMAffPi5vI2QRz2-5ttuYC40HLJYiuWe0wpudMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیران هلدینگ خلیج فارس از عملکرد مدیریت‌فعلی باشگاه استقلال به هیچ‌عنوان رضایت ندارد و در هفته پیش تغییرات گسترده‌ای که مدیریت آبی پوشان رخ خواهد داد.
❌
علت نارضایتی هلدینگ بابت هزیته هنگفت برای جذب ستاره های خارجی استقلال در…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/26135" target="_blank">📅 13:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26134">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzKcFse0x8u7b7o_Oon8PLXIiJC8GSAPmUhib-aRC0JJGtEPrQRMftZzlKwQYxlOi_nUYn4_PH2VAJ_fBE-3VdmIYTYJjRdH-g1ogCfQDBMkshiB24iBT2n37z1bRYRVi7FHkROoSWXROsE68gIYv3Axc-LSMapQtF0NYUPqoiSV92MbpG-n2qlLEJULCd-X3FZvdbCaxAuHJkvYj_3GuqRpRTjSVcag6sZjT1jA1ELH4ZiMfdXVrQAqFmnrqhfCpiSJAzhp3Iw6zBMIc1rcaw15WlVsJFNhkpRhRYIWLKB7GcnFXj1MF9uHUkxb_kktLoov0nHNplZEfoMOaAq9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
🇪🇸
#فکت؛ مارک کوکوریا مدافع جدید تیم رئال مادرید درمرحله‌حذفی‌جام‌جهانی تا فینال حتی یک‌بار هم دریبل‌ نخورد. یکی از بهترین‌های این جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/26134" target="_blank">📅 13:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26132">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHO7FXrO-66cWx8Dtp-Y5v-MoS4FcGGvmPIf3iFEGOeZT1vlXzwT-7fjcHoI2BNosNGVc4lWKeZ-Cvo6JWz-Uz6whF6vchhq1ewjXNNiRsvE93zmbRtNSG4cE6PCFuNLL65-G5fWr6Z7LVRVxhq3gDTNMZl8fkC2iTxa2BLLEoW_aTFPwcFXdTk5x1peNcPAFVuPVcdpZECmpf-YrVyEepYm4IZmM9VG1LuGYDsSb7IQGh8ubWip7spyJv_A2zWiR0V6ctDOzt9gtSjL-b4s9Irh44r6PftDhbQq6vviK87Hl5hlayP8UyWVuCyZIwE8kEqDMac5J1pB4dDY5TUllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/26132" target="_blank">📅 12:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26131">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxoSh4SnMnbyVWseKGQqRZDPiZdknzCoiqtExYh397A-PO7oXLRzXVWb2YR5nsCCAuNTlKT66p65oTK-mdzKBW22c-ZTAXiEiRzNcIjflZ9eTle765wKeRD8xeMK2fQ2D0m3vO-fMF1WWV4sWokI_X89oR9Yqx2t7jE6l_PV9375KofSvXYGemElvocfcMbF-cfmbMgRJM5ORg21eIVM7cffHN-CeY4AdSpDucjfVQNpIFs9WPSyL_EICLmsX6_iDJJvih9smZtp8S9T2ZiyHsHaaGVwQI86GebffEg2joBS9BzZBQ6zFXruHkMmrW9B6Q8Tmyolg1tDw5bXXxCU7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/26131" target="_blank">📅 11:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26130">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFN-Uf3bdPoHILSJBUa2Yr8EO15msXCmj4Yju0cOSZv43NIfknYOy04cfsKt75s88RumZVOTVGSEPW58hnK6eycvxeQG3DEoFBs4zo41e3e2nw57HeYXWW0HCfb59-Er5A2uWbxT6c6dZvUMUT8BPT1PD4Udnfc-kYLmYF2dC-9wAJZx2gi4NV7WPyVA2thfoq0GSUrm9sjnY4LdGoqYBLAisFH2hw8DnJ7FCP75NfQzCs0Y5VYdtmMeiizhWx8AveLRxDKZ-gSYaMxJJ-95IvkVBrYGfX7tJbenBQh3oxKfelusvB98NPR2QoPd_YZmEuqxIGNipirFfBf6P-aJYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون بریزه؛ میثاقی روی آنتن زنده شبکه سه خیلی‌جدی‌گفته آه مردم غزه  ایران تیم ملی آرژانتین روگرفت و باعث شد که این تیم قهرمان جام جهانی نشه. بعد همین شخص اون شب در گفتگو با گلر تیم قلعه‌نویی‌میگفت این چه‌حرفیه‌که میگن کارما مردم باعث شد که تیم‌ملی‌ایران…</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/26130" target="_blank">📅 11:33 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26129">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyHFyxZcKWYlsa9iGMUDNG6cZ5kn_-dvv_rV33sZpJC0DcmhI_EAu6RhIq-ls7WZIt8XXqrK9CyQkOiKTI_DPIpF9ZPZMV-vbw2sSGLSzh0fmXPHCSxgpVCnvdh7Gn-yvJd0EasNrlkMcTm0ltn-j8oqu132_6RlnoRNYGNvOMVQGYkZ1KXAtwYFOaVUZ63tKEyvN4s6evTrp2Si87KTZ_ZXG4Y0562Bne7rtkvoSS5ZUHkyoVJZHs3h3GTb0IENm1SEEjOEgJBPSKkBejbnr6Tuad6ogBREbBX6x4mjVacJSevnFfIKcmx2H7GBIqBqaaksQc5Xr06AWbq1R_FpRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#فوری؛ باشگاه پاری‌ سن ژرمن بزودی قرار دادی چهار ساله به فران تورس اسپانیایی تا تابستان 2030امضاخواهد‌کرد. تورس به مدیران‌بارسا اعلام کرده که‌دیگر‌علاقه‌ای به موندن دراین باشگاه ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26129" target="_blank">📅 11:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26128">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si7fKE7DenOr7fzfUGXagk-onfzC1XxjofrkUPY5K9B49bXxR2HLTY1i2qz0KWX5ZqY5r4Wz3MGDkv0Aq_1ZuV8OpWz4XOu9-AzBIDi8VTAnu0zTPsml6MGcxj_l2xqwgAfuUGIqMAJOcxgkQ44Xxkv71DuZt2EvERQRhinE7-c-JMGJW6GzJr1R_FLoEcUNjiTb9pWY5Ewv9VE9mUkJqLLw-kf7mKfwclVXcx23RCdWW2jsIXHlzn0OHgafTYVtySc79hyujB4HfqE649axb8GhRbW1irU859L2cKxyfer2nqKCKYUe_9_4xOT1TStQpB0jvXZ39dMUWz-M66aOmvtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202f77d369.mp4?token=EzVPGDyzWBj599KTeFBF9zrqZeX6oDBsgLCWVd4soqMjpqCOXuds7KMqzJo0Jryay_AUxW7-pcjQy-qYXDF1dVJUmf7-WhcrrnPZC5wAXqeYVjqz99Xu_q00_sTDklVEA79sF7PBmYXruzEUm5tdLpxDax-u62N5s66UWJTaf50xYSiLOyFg7WF4gSvdgelQH0qWcAzYya5a-iQg5ot6DiP2YC1MYt-dWqDJSwi5ov6BVtfud6AHYBgYDGgBHLueNV3IJtXqGV5fq11-maZNjTJvzX8cVGrurdd1yCexj5d7t-ZGwW_UIzwF-F_6Rukvtw9x42K1lYKuwGOS764Si7fKE7DenOr7fzfUGXagk-onfzC1XxjofrkUPY5K9B49bXxR2HLTY1i2qz0KWX5ZqY5r4Wz3MGDkv0Aq_1ZuV8OpWz4XOu9-AzBIDi8VTAnu0zTPsml6MGcxj_l2xqwgAfuUGIqMAJOcxgkQ44Xxkv71DuZt2EvERQRhinE7-c-JMGJW6GzJr1R_FLoEcUNjiTb9pWY5Ewv9VE9mUkJqLLw-kf7mKfwclVXcx23RCdWW2jsIXHlzn0OHgafTYVtySc79hyujB4HfqE649axb8GhRbW1irU859L2cKxyfer2nqKCKYUe_9_4xOT1TStQpB0jvXZ39dMUWz-M66aOmvtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/26128" target="_blank">📅 11:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26127">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcihDwsCoyDfqG3i8XhpAoytQlrCZSZvWX7lHI0tEMKQOvsA2fBYJ_aHU7NjASKSafbW_mkAH_-vgHne7zpYrT7TeqoqN_YUeAB3TYLVXo1dhSKPfjXZ9QmYw_gaSw8GMEhw-POyveROiD7l_BkaxrXXbAA0pSs-1RWVmB0TFFBzm2ZXRWcrHa1VfVgGRjeePadNGS3UwY8k2mHB9qx3WhVpBKZF4Vj4zo4nuV2YMGBW9jCo4Q1NyDBPIJNuSDlNsovRBPIrSIUIRAfwH8Oj_MNUeFSw3Z7BzB5hiQ5ddzPV5sDpC_lDXbRQ-1zih7aHOp_2NUGj6FmH1pyFDXWkvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
طبق اخبار دریافتی پرشیانا
؛ رضا شکاری وینگر فصل گذشته پرسپولیس دو پیشنهاد از لیگ ستارگان قطر و سوپرلیگ‌بلژیک‌دریافت کرده و به احتمال زیاد درصورت‌توافق‌راهی یکی از این دو لیگ خواهد شد.
‼️
پیش‌تر در روزهای‌اخیررسانه‌ها مدعی شده بودند که شکاری قصد داره به باشگاه استقلال بپیونده اما پیگیری‌ها نشان داد هیچ مذاکره‌ای انجام نشده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/26127" target="_blank">📅 10:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26126">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=POsPw7obDXZSZdJA3mKo7IajoBmjrwvgCy0do82dFlOLxNwq7KtcX_KaWOj1ynuf6D-mlhm9VA1IystaLD__OX4o-ZhDL2udvPnt0gulvmc7TXjwPfrMyBXEeZc8hquqKLJ3m7dEVyamlKGzxH3yWcXv0akRTaA8RKpa3dvfHNd3cRN2Z2zjWhWvUrZLs5k6WRlh6og17F9W5xjH7K6ZBDN3KaI8CfMSzpczW2UhUex5qBgDQ1xw7-3JdadlYi0d6Lw092L9fnVxABhqZ41Z1JvE4Cxytd_FA4XpiihcT2iGypKwrTeS_-qu-RTId9OnlUi91_A18vG6xKwrAoXL6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27dd0a5169.mp4?token=POsPw7obDXZSZdJA3mKo7IajoBmjrwvgCy0do82dFlOLxNwq7KtcX_KaWOj1ynuf6D-mlhm9VA1IystaLD__OX4o-ZhDL2udvPnt0gulvmc7TXjwPfrMyBXEeZc8hquqKLJ3m7dEVyamlKGzxH3yWcXv0akRTaA8RKpa3dvfHNd3cRN2Z2zjWhWvUrZLs5k6WRlh6og17F9W5xjH7K6ZBDN3KaI8CfMSzpczW2UhUex5qBgDQ1xw7-3JdadlYi0d6Lw092L9fnVxABhqZ41Z1JvE4Cxytd_FA4XpiihcT2iGypKwrTeS_-qu-RTId9OnlUi91_A18vG6xKwrAoXL6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🩵
آپدیت جدید تلگرام دیشب اومد؛
چند تا قابلیت جدید بااستفاده‌از هوش‌مصنوعی اومده. چندتا عکس رو میتونید مثل اینستگرام پست کنید تو یک پست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/26126" target="_blank">📅 10:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26125">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=k-oTW9uTi9w1VZ5CT3jdgWWs0zXRqriBZN2zwYoLCliZKPMD0q5HMcVZ1f1FQbW7twVvzdmRIP5F5bZ8n03ESs8agFI_hI2cNIhcrpORttuM2J9zKqYR5490X7oMlq0tLUmF7MpScjDuAhVFv1n4H8d5GYO5Y9eKSuc6nFgNzfVdk0fqbiavZL9A2OAardorjMRr48odUvzXU4oJ6VnxSRe3qg2IZAjCKH1JHpXBqQk45cDMgOfR-xPqPO2GrHsCDObxpbPACJxBB-X4Xbkex2x9MvDQGbfYK4b5Pr23I6V4-xQs9v8KUk7IcfdUy2mfAjMQOAfXRdrAAnex5ATlvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a101f8f4.mp4?token=k-oTW9uTi9w1VZ5CT3jdgWWs0zXRqriBZN2zwYoLCliZKPMD0q5HMcVZ1f1FQbW7twVvzdmRIP5F5bZ8n03ESs8agFI_hI2cNIhcrpORttuM2J9zKqYR5490X7oMlq0tLUmF7MpScjDuAhVFv1n4H8d5GYO5Y9eKSuc6nFgNzfVdk0fqbiavZL9A2OAardorjMRr48odUvzXU4oJ6VnxSRe3qg2IZAjCKH1JHpXBqQk45cDMgOfR-xPqPO2GrHsCDObxpbPACJxBB-X4Xbkex2x9MvDQGbfYK4b5Pr23I6V4-xQs9v8KUk7IcfdUy2mfAjMQOAfXRdrAAnex5ATlvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/26125" target="_blank">📅 10:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26124">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FoS3q79XJZqJ9UecqStz5SvEMoyYLwmDBcfKnE3tm2tyMsJM16qXdxSel_lr3Iosyu9hOyBNbSrQcTk9qZ_eW_m2JHMLn8YqsVR_C_JTyoHble2pu-HYYUMdT0RAaqTURQCjZ7humZfWQD7nRegBhYJl_jbOUfjmdLfSIuaAstUryQTFfUoMwT8lT8qQ2Bov34Wx4HGTMyqDkc9ZeYZ-Yo5d4ZJBg1ujLUQiH6EP3VywJSrqWQUEXH_gxyBZSl12ovdmTz_0Ms0CQgYfpsx_WDktGVp5e8cvza7sSg9mvIUdn0s_u_GPhiLFZDrECxlqNrNQree0FsjjU_P2Hb9fOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1235d344e.mp4?token=FoS3q79XJZqJ9UecqStz5SvEMoyYLwmDBcfKnE3tm2tyMsJM16qXdxSel_lr3Iosyu9hOyBNbSrQcTk9qZ_eW_m2JHMLn8YqsVR_C_JTyoHble2pu-HYYUMdT0RAaqTURQCjZ7humZfWQD7nRegBhYJl_jbOUfjmdLfSIuaAstUryQTFfUoMwT8lT8qQ2Bov34Wx4HGTMyqDkc9ZeYZ-Yo5d4ZJBg1ujLUQiH6EP3VywJSrqWQUEXH_gxyBZSl12ovdmTz_0Ms0CQgYfpsx_WDktGVp5e8cvza7sSg9mvIUdn0s_u_GPhiLFZDrECxlqNrNQree0FsjjU_P2Hb9fOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ‌موقعی‌که‌کاپ‌رومیخواستن ببرن بالا ازپیش بازیکن‌هانمیرفت‌ بره‌ کنار؛ رئیسفیفا اینفانتینو دست ترامپ رو گرفت جدا شه از بازیکن‌ها، جدا نشد وایستاد تاکاپ ببرن بالا؛ فِش فِشه ها اتیش بازی بالای استادیوم چرا آبی بود. قرمزنبود! ازقبل بازی چرا آبی تدارک دیدن!؟ فکر میکردن تیم ملی آرژانتین میبره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/26124" target="_blank">📅 10:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26122">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rmSVF-_FTtoTJ6fRG7HYeX20Vlsw0wCdgsGW0SM-IeXJgHRlAB4B2__AICkWb7G-Fe9mLnEPBb54UzBrXwLYLDOuxbsV_wwua_cqUPCmMt2tPtmoSDKdtk2fBm-7Bm_pEwgrjalkDOtErT_X64HE1LCeLVNrW-0Y5YuBOd4uKZnj0yJ5PuAgA97BoD-UFmaHPw2CffMLgCG_Ioy8v4gu46cBW7UR3i1zmN3CIEDCFeShaSFYrJVS0pQm_LZba34THtXwiH7eczvYPq9kGmXXdGuLtNf2hHh7Kj1jHNA0TtzIVB_KA4HotwWN568aoP6l7f_0W3Jfp7aELrAPqEEl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DDgzcDrhislvPaPBGvetnfulgEzLyONP2R2t99y8kV7gTZBJMrZ0v8uH4wYOIn4_zaAcJWZCKtp13D_wJPhQXJ8d5mbc3xuUb5SoSMOQ4TdbyscNe2gRmUAY0LGCKPsdoVsaN0excMFwEmB8P59WL8TQ8lMo9ZW7xkYvmkgJN2FA_cwA8eQoAliZPRaBHRses2X12OydiBHDeJacNtSfhSbJ1JrXEh2chAxZazrIWJFLzRaAGhQLxKrDCZ_hHyYEri60ng6F5B0YGzhlfJ3FzYujVXXiLs9tUtpNJb8EcJG2ki-rrUt4RPObHZcf9FmidMLTDg_723nSQ8nify9lrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
گاوی در جشن قهرمانی خواست لئونور دختر پادشاه اسپانیا روبغل‌کنه‌که لئونور پسش زد و نذاشت بهش نزدیک بشه تا به‌نوعی انتقام گرفته باشه. لئونور در عوضش با پدری برخورد خیلی گرمی داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26122" target="_blank">📅 10:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26121">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=pdI6_3-5GLs_oPRhYg0lk0fbbeOzXAWaW6gJzqhipZbVgfYw8vakHt3q9FiJb_6szG6UlPjeIkuRdZ93OXXn3hATXByA-7P8WO__rbf2A8kaiA-LGWLhyJqI4VkppWxZ7FQK5jQRwT4Q08v39j2XIQgz6n2mKum1MgIjvgAI5gCCWLeBBf2Mwfg0fuV9KAeaAoTVQ4yEY5W5r3G_trgqK7Eq1PS6rg0mLIV4HxyuF2CUl_YWxk7tpPBXbiCfaK9x6SI52dyxYRMw7LTvH1TMp6Nf5nvxuIh5Cd-tKQHXiLlymdvU5fMZuXmuDKezKgdqCN512OlTI7nOGAC2q5p1fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c071bd0be.mp4?token=pdI6_3-5GLs_oPRhYg0lk0fbbeOzXAWaW6gJzqhipZbVgfYw8vakHt3q9FiJb_6szG6UlPjeIkuRdZ93OXXn3hATXByA-7P8WO__rbf2A8kaiA-LGWLhyJqI4VkppWxZ7FQK5jQRwT4Q08v39j2XIQgz6n2mKum1MgIjvgAI5gCCWLeBBf2Mwfg0fuV9KAeaAoTVQ4yEY5W5r3G_trgqK7Eq1PS6rg0mLIV4HxyuF2CUl_YWxk7tpPBXbiCfaK9x6SI52dyxYRMw7LTvH1TMp6Nf5nvxuIh5Cd-tKQHXiLlymdvU5fMZuXmuDKezKgdqCN512OlTI7nOGAC2q5p1fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حماسه‌جدید خیابانی دربرنامه زنده؛ خداحافظی اوس جواد با مسی و میراث مارادونا با شعر مدونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/26121" target="_blank">📅 10:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26120">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=U0gT-FYfVP-g7HvgE6h0x71uBanInd8pxhRc0USPSGM01U7-cbGPf_sWykPJEHHVExhvXuUuKWyuOoclzF_BrXCwwFgx_GXNREFw54KdFIOtSBLSUuzHDvemZFJJSwVdHwvAv9o87DHz68aeYmFQfFxAhvJJ-oTNh7Zp-NGb6LCnfpr1BDRLDLMy34NF-q7k1Zq0lSbSeUw-N7Q94jT32zBPEPguAVf1_Xk2L4uTV0Qrxkgpy5nySFEf8U41DYu_5SnvgnIPp_tLmaQnn7fWvBbbM7i32XU0Edf9grz0aBKVvBV_aCOKSLywQkwXanEV4GnOF5WqM9UUfdFO2QhPWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec0657aa93.mp4?token=U0gT-FYfVP-g7HvgE6h0x71uBanInd8pxhRc0USPSGM01U7-cbGPf_sWykPJEHHVExhvXuUuKWyuOoclzF_BrXCwwFgx_GXNREFw54KdFIOtSBLSUuzHDvemZFJJSwVdHwvAv9o87DHz68aeYmFQfFxAhvJJ-oTNh7Zp-NGb6LCnfpr1BDRLDLMy34NF-q7k1Zq0lSbSeUw-N7Q94jT32zBPEPguAVf1_Xk2L4uTV0Qrxkgpy5nySFEf8U41DYu_5SnvgnIPp_tLmaQnn7fWvBbbM7i32XU0Edf9grz0aBKVvBV_aCOKSLywQkwXanEV4GnOF5WqM9UUfdFO2QhPWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
#تکمیلی؛ اینجا دیگه عادل آن‌فایر میشه و خطاب به قلعه نویی میگه من تو جنگ‌های این یک سال اخیر ازتهران‌تکون‌نخوردم ولی‌تویی‌که خودت هرسری فرار میکردی تو ویلات‌نیا ازاین‌حرفای‌عجیب‌وغریب بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26120" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26119">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa1c44954.mp4?token=MA8WmKcC1iba_rYFI2ZHwTiiSHspXibMSpJJnn0-m3woBx4pMyvW0jzYZRz-G2-su0F6s8gd3HfWUEH1IzWMWTVg44U0f5I9TrETsurBsvU70UzYHlCY5QTnKmm922svqD4qmaGO_fLvodtKAZSZpD6NIh8vttrqAJ5xn56lqk_83cYHyDx0B4N0vtiY83jiNulGVzKpXdH4sFrRN2H8Nrku-gz3xXYJw6PoVtkftqTXo0bjVJrZgV3ce4AuUoOwfyDyLylHut8NJQ-WDBWlzwH2Sev505NGo2JxPZKeSavAzKzT6KXLaK0GDxWKfjFhWegFj9kT4TppconbECCoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جملات‌زیبای عادل‌فردوسی‌پور برای لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌دنیا در پایان جام‌جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26119" target="_blank">📅 03:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26118">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BtEM1AvtgX8wwaRje-tFdXEEg2OlhxgkEYweG7en48h8gUYbHLtydvEoD_cfxzp4G3zkg1fhjzdbDgZAzEMlWpF1bnko59IKKAZCv0ZXtsppV7-8mZJqcWd-Oz8x8Ycqd78XJX6RNv2ITuch0PXHy6Ns41hMXrYcCbbglqMqNgQwx5Txlwfj8UlOYeYEAVI_7sldUriOXgkA0ZB1iGC-AbEjj5N3sEvQUeEPUR-msZcKJSRynWMhlOMr5nHZck1Zl1faWullMr5wPExCIQ3L_mZRml5-b4fN_eXVxuj-prLvaYlOWClJXbEnKlL9AWP9KWUyQbANOIewMWS5eNQGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d171bce1.mp4?token=BtEM1AvtgX8wwaRje-tFdXEEg2OlhxgkEYweG7en48h8gUYbHLtydvEoD_cfxzp4G3zkg1fhjzdbDgZAzEMlWpF1bnko59IKKAZCv0ZXtsppV7-8mZJqcWd-Oz8x8Ycqd78XJX6RNv2ITuch0PXHy6Ns41hMXrYcCbbglqMqNgQwx5Txlwfj8UlOYeYEAVI_7sldUriOXgkA0ZB1iGC-AbEjj5N3sEvQUeEPUR-msZcKJSRynWMhlOMr5nHZck1Zl1faWullMr5wPExCIQ3L_mZRml5-b4fN_eXVxuj-prLvaYlOWClJXbEnKlL9AWP9KWUyQbANOIewMWS5eNQGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/26118" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=iUgniqkKsoqAs9DZ0JUgHCPTdDeDr3uJhiBaFd1BlIOKsXKLh9UoTl5xZMD-APD6Qzr-H5Y4YSNcPN_1zEuOjO7XCiGXLimPqlbukMPrkWCnO2x66eYgA1nTZFTKaci_lMPGoNyrQd-3hlmtNQxYUtqozFP7jjhK-nyPFVXno4OqSoImILJHMixg3jJ32KRlZUtOv_FCBP335AU95CdtQsB4zHOay-oRaxOTMMn8vEbezv6WfpU3-jui66LJAoBcAUZNm3Mt3b5VBH_T7O5CSymmrZDJd7H74vwWkG_W1qe44njkY6CSQ288LbXexd2s1Gv5ZrqYzhzBP9sSXzIKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b94e4b0c7b.mp4?token=iUgniqkKsoqAs9DZ0JUgHCPTdDeDr3uJhiBaFd1BlIOKsXKLh9UoTl5xZMD-APD6Qzr-H5Y4YSNcPN_1zEuOjO7XCiGXLimPqlbukMPrkWCnO2x66eYgA1nTZFTKaci_lMPGoNyrQd-3hlmtNQxYUtqozFP7jjhK-nyPFVXno4OqSoImILJHMixg3jJ32KRlZUtOv_FCBP335AU95CdtQsB4zHOay-oRaxOTMMn8vEbezv6WfpU3-jui66LJAoBcAUZNm3Mt3b5VBH_T7O5CSymmrZDJd7H74vwWkG_W1qe44njkY6CSQ288LbXexd2s1Gv5ZrqYzhzBP9sSXzIKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26117" target="_blank">📅 02:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26116">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=Ye2-H6nvxnxTC0D5ralhSTYowkO3X9NVtfxL7qSTC3UGSfzAOcxahylEguuYiM4cLNkX-SF9aBpxMatJg8PforC4dVUJueZ0uIY0s3Vglocxk0MERyjdF_tCSMQDJki9Q_NhE8i4MD8Wy3a9GFlQ5b1lBNjuHdbyskJH9sglbi85fBTzjeHhtOsL4X93WedPRGpm13USUIEXaPwra_i_Yhe5bE_md31_GohMFx2S2GXocyJm-NalQmWKvUmQQSb3-Fr3OPbPFoSAV8TAzYutij1F0ZFZuMZ06Fk_tmLjwkKKnDWxmUjdzJ0txFCGzI22nQlp5oDtelvQHdkkr-UKFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e72188ac69.mp4?token=Ye2-H6nvxnxTC0D5ralhSTYowkO3X9NVtfxL7qSTC3UGSfzAOcxahylEguuYiM4cLNkX-SF9aBpxMatJg8PforC4dVUJueZ0uIY0s3Vglocxk0MERyjdF_tCSMQDJki9Q_NhE8i4MD8Wy3a9GFlQ5b1lBNjuHdbyskJH9sglbi85fBTzjeHhtOsL4X93WedPRGpm13USUIEXaPwra_i_Yhe5bE_md31_GohMFx2S2GXocyJm-NalQmWKvUmQQSb3-Fr3OPbPFoSAV8TAzYutij1F0ZFZuMZ06Fk_tmLjwkKKnDWxmUjdzJ0txFCGzI22nQlp5oDtelvQHdkkr-UKFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نسل‌جدیدعلاقمندان‌به‌فوتبال:
اینادقیقاکی بودن که بازی اسپانیا
🆚
آرژانتین روداشتن نگاه میکردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26116" target="_blank">📅 02:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26114">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qI9LFeqmAO-K0sPt0_EArkNZffobjr2m4qg3gfYkTCwjC09lqgPVhpuYuXiELwFIOUKE-vlQ1DqilzGB3shvTkSMy2vkSHbGCCyycCSoHTqpoLn5tRQkrvkHrcEC1pGWHc_s7wS164CQicC0bAr8nZv72PNm7NSvAEJ27hrp0wOCoMs1LiTCYBqUleSZbzbE5wnbEfRpXUKmtaPgzveVZTBvitC2AobRH3WFOfWnsFJhoih3o_N97IV35jgydIp4B2EXbQUfIf79itcpKKGZ66wbGI_UbIacCzDCcdDhWygctVh8B2mOMfq09cVBIHcBQjZjCsAb-zgrplX1wu_sRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26114" target="_blank">📅 02:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4tRFLishIuQCSb36yaFcM5i-aQgWKs1ChbZVlv5n8f17x3W9vxfo3J6631WiG_b8UXTDtRb57fye2A_qPJ9OqmFUgOYn95Oaapr2VZ-e37jUid1Zfiu97iFrQeQp9B9wd0nIG1n81R4H6fDnOHT5HHKbJpAqAaLhHe6VMwfjfg7hGCOBmXBl4u8D0eEkDKb6zOG9PWBHO6rtTGSOZPAgId5I4Eg9WL9m0bz0pI5iCIU5bXHn9TAlvpXU_WByhCwtA1eHUf2uQWZWwK8KUYsFls21ZNDlwfF9LgNRMN0hFJ1wM9HkkWz5nkyAMFU9LgRY1RXq-kXJ51xOTTgZFes3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
این هم برای هواداران لیونل‌مسی؛ مسیِ ۳۹ساله اگر نبود آرژانتین‌حتی‌از گروهشم صعود نمیکرد اما او یک‌تنه تیمش رو تافینال‌جهان برد و تهش به هم‌تیمیای خودش باخت. توخودت‌رو قبلا بارها ثابت کرده بودی لئو ممنونیم ازت که حتی در آخرین نمایشت هم درخشان بودی و مثل همیشه…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26113" target="_blank">📅 02:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWH3_iVTgsbfizoB6iYvplR1P1X6guFSGqIpyxm2jnctb1ZbkeHTWhxJ0bVY7DeJKsSEWkirJSigSb1XX-tHVT4sn02DU3pUOftW0ngM5Iixa1UiMv_zl0g30IyciZUoLNvKi70h-m0-7Nsxr_scyAjyjEtCjkLySUvUBVUjFgtLFlJErCYbgzdpd-sCy7KOc3_ipYmqDNgZrIFOurAAzxDYqvJjE3uHv_gTqN1ecYmH5IxzzqzE-ZwFa_tNRHmgV4-SqqzrOueCp2PI3RtWiCsOkJVKiQwQiQqCf5nRvU1KutHx3FAMZenvgpo5dLm5USGSCLQ9k9uHUYRPKHCLhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#فکت؛باحذف انگلیس،ایران، اسپانیا و آرژانتین تنها تیم‌های شکست‌ناپذیرجام‌جهانی هستند! اسپانیا و آرژانتین بدبخت باید تا آخرین نفس برای قهرمانی بجنگند، اما ایران؟! ایران یک مأموریت مهم‌تر دارد؛ حفظ رکورد شکست‌ ناپذیری! دو تیم برای بالا بردن جام‌جهانی میدوند…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26112" target="_blank">📅 02:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiTb6qMJH7yfUOPFKWKLqVIq_Gjxv-8FraxKb96rGlUw4gx5omP_7V-X6fzcu__JB224Bp3AxsVujwcjxb0WawZazcll9BjKMY2iesQ5LQlI3fFlYExJgsxy5xRBw392ahbpFs4lIotpKTyv4F6x1PQNVFsUERhY75sqRKDvJ9iL_KI4wGloSUYm1lJv4CRUxuCAhOaDAFfntyf1PTpDq-H_EkHG9z5MxyzefDFwx3_MuE2ZB8XliSSy78b8X-R8zQLJ85IbN9J0PwA30teUUIcu703_ALJ-K3819Ub1PFKu-bwhD8zW9DjErYhXZU2-Y59UyNYie0qm32KrJtHmVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با عدم گلزنی لیونل مسی در فینال؛ کیلیان امباپه با 10 گل‌زده آقای گل‌ جام‌جهانی 2026 شد. همچنین امباپه با 22 گل‌زده‌لقب‌بهترین گلزن‌تاریخ رقابت های جام جهانی رو دوره بعدی مسابقات از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/26111" target="_blank">📅 02:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM00x27LQkf_40B4N3dCBDHYf6xCadiPuvq6qlGE2JDasmPrPeI-03CHwa3Ue3O9LG4TuRXc_Toaks5rfuhIEj5yt0s5513Hu3szhMIX4b5TcxmSe0m8bRih0bN9P7OTjnga5ETCte6fSl_Af7VtnV-xn7ABK6ALgPJINUWl2SqVW9KPeRSlZY317mZ0gtjH3E3KnqyMSDW1u3k05Vr2sNKsKcqusRpi9lPEiBUm0DMx6vCs6TtO2uVkdji-DtNqQho_YeSLyBVecnAk1pypCMsOTSc4os2o6Dk6cspd4RARFAASCu1AvvMa7M0QGui1ghIDRzoMNQg7Ibn-mInvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
پایان جام‌جهانی 2026 باقهرمانی اسپانیایی‌ها و گل نجات‌بخش فران تورس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26110" target="_blank">📅 01:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stFNfaUglje7qzyXfSgxP68_a_SIYS1UQ84bJtbQNwHDxGuxjmhBAlgZ6BvhXIitWeOEP6XL0WYbUdROWOzvzJ7WLpkXaTykLTFsjBuqjZzc7Mn60y1ZqljOJDKuFyfcMpb9EN-gn2ajcdy84SHcw7uasX9N-U1N-RwHRt76rVFs7Cjmv1oMUU4KmhctzAR1rBm_c8tSDhADM2bkMa_zwFuqg-HO4iVJZn-KruXBQ6AQlg7JSFRiBAKV8J2iv8TzpTF9b2zGRhuqfJXpnVGZ8im37aRFBt7pZ_qEWmF5gI-HJC44A5uKfmq1UmF8jaktUZ3YXgPhR5ccensUsLtaFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرژانتین وقتی فینال رو به‌اسپانیایی‌ها باخت که دریک رپر کانادایی روبرد آرژانتین شرط بسته بود. او در این جام جهانی روی هم 10 میلیون دلار باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26109" target="_blank">📅 01:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lver-fIw873wxBFiB6wui2TVWIdvOiHaf_-CweX8ShuY-JM4CvtGS2Z8plajxXPtiRDZ40DbLa9Hq8AXQqeTHEzVHzHCVDEzAOUU2nYYqUBfUqtAHPCsOuTggb6YlkPgQ2KXltnYW-afu_tRYUCP0fxSmBiIV2G3bCebLdlk0M9azrcxeuzpdSgOnna6lBxcwFdPT6sCtDswIvVuT0Mh770dPLH5z64ElqLf_UJtEDZRgF8BH8Ox4qbnSnhMvSa1teVlqAqdFJKvolTNcLMAA7tAEM4ins0G3T5Iydgp6GsWRexetBtZA9xDcMsU7pptUVlR4dOCLLARIv46RNpwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید بلینگهام هم اومد:) فینال هم یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26108" target="_blank">📅 01:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26106">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbNmMLXzsstkA2rSIQMlG-KkjZ65WuZFtIIFvy8vZ0yG6bi3yOZhdN_8Q8jGDv2h9DdppMN30G3Eh2rlP7pRFTEovcfohcyIwFeMWXE20JTB73xqQF7987YdM0goDoj6Li3TStAJYCdk-PW3klDZojEKxAjzIOKR6yJ88FJYWmkYGlCNFRZd-t4fQHWtkq8iPuJRd_JyOTjdjjK0k8m84X9NELG08POE1Z2aXIGpR1gTuikknTTM-Tilzwd17OOGLEIdZhmq4XvbzDfQ9gAIsA6PkN7DpKXYnH05Bx8JRWnQ928IrInTk0mkuNu59IZXyqMyHnUNEXXLww3WShV7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26106" target="_blank">📅 01:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26105">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ02qp7N57Vezo8ZLVpkW0LXMWK8fc6ZiiUdXu17x66SCFTTx2K_bqt2UrP-E-DzAJdipZC2BeLeOORKluSe7lN7TxdFbFwpydNDQDeS7-_bzmfuO4WsZ4qCfCj6DEix8ks3PloJmzB_InPBNlPftVSKEI4MMNAsCKdAaQc3BVxE4GJODa2kw4ksvmeUV0_CpoVr-eOTfNEckc0F_-e-vI_agTksNDedDrWdDsrB9IhQvWh6VF5b1MWKc9cE57iTgR822dp9cyJICRwBoALvbOB73STtfe-pfW6Oiu2V6h7Syf9gVORvWM7yyRJcwRUO6bTWZI2GGvbUoSLEw05vKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26105" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26104">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRzR4r2dYK9jRrisyaq_qDElsJjlhqY0WHIqeO6-YtO-dBWYBkiQkZSj9N1pambZ9AESAMmVQrtKDaRzmWTHlAu8CL1t0Of3o8o6lITB3DqWitGu2EZfFKWyUNWNL4fBDWsLL4W2d8H1oU0ldY1_WnsdSZtG9KYCIAEyhmBWi4nKreyH5QhAXWdoR9wgA6vmyqgxNoWYs7vAuSrZZjwtuJZoPtt22dXF4DCTit_0-5s806nHPKXtXV50APR9YR94BAgpmnq4VOQelDt5v5A0CYYHCPqNojJr6N6yRzoDfJWy8LCA9Dle-jIXFcTlxiJBZdP1_aghm9ONpr7KIrvEtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
بعداز 12 سیو بالاخره‌مارتینز تسلیم‌شد؛ گل اول اسپانیا به آرژانتین توسط فران تورس در دقیقه 108
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/26104" target="_blank">📅 01:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26103">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Asqy6g_hhh9wa_sBx7EjauoD_C7LHyvbotXEUSzGN28E7f_fmHIGbFPFtRhoNv-sckb9zTtqsKLazOdKypa41S5EwTf1SNe9mE2t9YSrk7LKLl9p8OOc7mlqeooWPSEMi9QrWi-j1em4StCC5Jiasil-QWttbf1ge3TLxaUO7KXh00o0QxjF5GvRjngPwL9UDkOIw2T0Qo0tbH-F0594IocqWsJmC4oexAPDVU5Wu5EJymyhBwZQF52ZpfXEdd89_T_qukEafnCbtRMIEXGmrsJRbjjQXGBPUzd6ht1L1gZ-WHvQzVls1Be1RUqtmcaUmfuWEc3M05MD-vlBov9nTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b656d9cc6.mp4?token=Asqy6g_hhh9wa_sBx7EjauoD_C7LHyvbotXEUSzGN28E7f_fmHIGbFPFtRhoNv-sckb9zTtqsKLazOdKypa41S5EwTf1SNe9mE2t9YSrk7LKLl9p8OOc7mlqeooWPSEMi9QrWi-j1em4StCC5Jiasil-QWttbf1ge3TLxaUO7KXh00o0QxjF5GvRjngPwL9UDkOIw2T0Qo0tbH-F0594IocqWsJmC4oexAPDVU5Wu5EJymyhBwZQF52ZpfXEdd89_T_qukEafnCbtRMIEXGmrsJRbjjQXGBPUzd6ht1L1gZ-WHvQzVls1Be1RUqtmcaUmfuWEc3M05MD-vlBov9nTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/26103" target="_blank">📅 01:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26102">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdlzaliFrSORCBZxVYqQKDuRgeVATAf3nc7AHpOy8Cl8ulfrubEN7cM_4xmk_-IPWlECjkosCrNFK-pX2XjF5xiHpSEs2KG-ZGahsxmMyESjQtQYQ-cUlo0JLIX2ULGhZiWC9w-NwWsRNNyboNFXEeReqjxf5bvzJcF5awoKjwqPxM7GNxguets2VzahSocwypbL9yvJhe7ZLnPWlG_1R52kc9AthGj0Y94nqLA3-v5xHOMFFctuHlMme44SKG2K2QXhBSuFV9tGceNtYGulDPG9806LwavfSznEdKKrWpo0luAOmxfV5gJh8DJZS0oTGaarWyxoVTpnHauOeh_j9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
ارزانترین بلیط برای فینال جام جهانی ۴۴۵۱ دلار و گرانترین آن ۱۸۸,۸۰۳ دلار قیمت خورده است. به‌عبارتی ارزانترین : ۸۴۱ میلیون تومان و گرانترین: ۳۵ میلیارد تومان و ۶۸۳ میلیون تومان ناقابل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/26102" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Alipvzr1sqef7u9St_ypqZ1UxInp73ewkJX2_IIR0iKl8ao7-zGXDgHGg-DSYWUC4v1wk_CH8dKpYd0sVXFWcX_56kl-snSzcnSzPT6kHySz7TaTe_lqVazBK_RQTiCv19tXwsbFliWIxuz0usi2GH4jaBo7kJ8jLrHrMhjF__azc_hUG97WtvxS4Ynh3oWrhP3vRx6oD9xoWvQZ18Ua6Bih37TecrTyIstSpM789EfJUIQLDNaA3jbe0G7AmAJtjIi4Np25xWCk4Ey0Rav8KVfGKbRlKh9NaepNsCplNbeHk0-lH2WRMJO0pfa4KuHNeYGeTqLC2H9deGSz43FQXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qaqd0ggb5bnqYE6HEVE5oWfsAtF-C7oD49gTvHt_lmxvDTSmdid39VNH1eUef4JRNqbVZzyAyrPDXDZ-t6oMrP3D3NfKqqN_zMJN7XCl-UhVNGGfyo6m_8vSZKBfDldAcihlxo1YYaAmkdVjw2swrT6og6gcDBIOSgSpGeYKahoD11BoUmPPUt7co3DBqJNxQ570JYLqiSGIFLyW0i3WJhaxGSjMiWOeNwAzgq6PBOs98uGBHLnnAPZH-jPVwGNtPpy-3wJtk0vE7SPkqenw4XtTgAwR0Ximwl4P3o8n4rKQkZZ1-riIs948Sj7PvlHeBZjm-Npnugic2xTQIFdLmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
ملکهٔ آیندهٔ کشور اسپانیا به‌تازگی به‌ طور رسمی سه‌سال‌آموزش‌نظامی خود را به پایان رسانده است؛ ازش پرسیدن هنوزهم به گاوی فکر میکنی؟ خندیده گفته دیگه نمیخوام راجب این موضوع حرف بزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26100" target="_blank">📅 00:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26098">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kn_lKtNyDuoylcTKeGE14IKus8nbsJGvSqWHTrYHju14v6sLV43qGtqxH5Zv50WHUx35e6sSj7fHTF_3slaigl7UfbXeclXc_5Uur9yAIw7q3iNezNPjWwnREWwAuHfgeiNLvXA-vZRZ0ZDtuoxeHAcYUA_0VhPV0egoMuPlcdGTzxL7jDbPhhMLB7cAfk0ZRaDH-AsLO6CWtllfgWz1grF-6sfXx8RvfU22p0u7Rpt89UxZD21cMDYOJX0FJRmunHHq24TcqgEVC54PSuGhzHbMYcR5bPW_q74ECgDA8u3MlOq_sWdGHANpo0fo5GB2Z_A22l_Yfh3LQoyDYDCj1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F_Qc0wd6ZAPyE5V3B9pD9DnTIeMGso3J1IxuKstbY0kIhcOojryFLyAvf_qbiWIer2mzHEFPGsJyfvmZtqeq9hGZVQuBpvcVRwUPyxT47vCV_t1C_SpUpByIoTVIsXof-rR9yKUDMavdEx4gUtSlvoHPSZhoxTRCi8Qt1LAcETrtZCxdTaIaFMngXR9Dd4QAveSqkE8WkGJc3ntiwMeedmKuS9jT_tsCXk8E08KhKKciDC1mMhcLUvgnO0lbTWx2M6GXxrOebQKxc-OPrqzovUzKsz61XC99NkvSUbPhFGcpfXQzB2Nfi6DRh1OUgGUmyjJ7O80EZ7o94GgTCv_Cnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ویدیو کامل اجرای بین دو نیم فینال جام جهانی با حضور شکیرا و بیژن مرتضوی؛ عالی بود ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/26098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26097">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🏆
لحظاتی کوتاه و جذاب از اجرای امشب شکیرا خواننده کلمبیایی درمراسم بین‌دونیمه بازی فینال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26097" target="_blank">📅 23:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26096">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrVd1OKhvg243FL5p6GJRYdeY7XxoLMdZZ8o9myyl3olwTEsnKf463Q7Tt_y_2u5Zg5bMkfYhcfGyLUaiD7J9pIvfVmip4bfGLpkSupAoQ0z1Js7NFD5D0me5_XuJDDsLqHVg2sses_vTM2A_ZqdA1IkmkVkIf6NK_08oHlrFTQM2O3yNgLQ9jwU7yHAQyDIyJXyecAe-hg5Z8jkdcD0g0ElkyRE6Sc7E06iz8p-DCRCLSe4Y3dfbHOGAG_gvUyDvwXid4ixlGbNV1jTHiU3vj_zqXcvyFrbKwYYED69DyZ432yQfC-Omu4zNIp3wQZZMidoCwR2j6Yr-Nps1S7UcAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6a67771f7.mp4?token=bAQNUQnjuLBVy6lV2aP0luPgvMNzJxE6QP-B42bnnAOf8o5eWHENFk4TCSLneADaxdC1CYQruha1QYvE5LypPXfyAWiHqLRyV5kqzv8efclYP6_j_48D4teaMkD2EKJqKcsig5yN326skkJRq0WFd0Y1TgNF0akuen-2ELtfZnEXDxVE9mv89sKMNkKFGvcg5KHa85h2IXybuwinr8-YQaDHIh9Q43t6nGUmP8NKQDp88sO0PkalWhHvaX3Kqdohc7cAd4luc8Qx5rJXPr2P8dhETOgOf4YEeHGSOUVaN0OphNaQWy9aXn-5rZOY09ZKwTVPEYbTkdR9x8ndbIhyrVd1OKhvg243FL5p6GJRYdeY7XxoLMdZZ8o9myyl3olwTEsnKf463Q7Tt_y_2u5Zg5bMkfYhcfGyLUaiD7J9pIvfVmip4bfGLpkSupAoQ0z1Js7NFD5D0me5_XuJDDsLqHVg2sses_vTM2A_ZqdA1IkmkVkIf6NK_08oHlrFTQM2O3yNgLQ9jwU7yHAQyDIyJXyecAe-hg5Z8jkdcD0g0ElkyRE6Sc7E06iz8p-DCRCLSe4Y3dfbHOGAG_gvUyDvwXid4ixlGbNV1jTHiU3vj_zqXcvyFrbKwYYED69DyZ432yQfC-Omu4zNIp3wQZZMidoCwR2j6Yr-Nps1S7UcAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26096" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26095">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=ve_Ql8j_uFL7VEBVzkIlmNqInZE0lz5rjHEL63rlScae1oFujayp7-sKIHhnI4hz19gRITkC4-gwosMQt3w4Tlp-iXOnxIcmNwd0Y-VgoMGg9djitgC0JjiNQpuqMH3dfctQ9sekGksNjlgtcjAmcrAZVIfNOOQrxSb3nbA6Q1oOf5PvFI5sEOSM-xux76q--1p5v9pDhKlbFwV6H5MLasJQmQIE3myyXjX1TyxVsAJ-xcP4edzNMCTlevLpvRTvVECMyFhJqELofdvb64giXTfuqURid92lsI-t2xk59OMO09n4m-mb-zR7CR8xZ6tDYmfiuVG4_WfQOmLEKP_MNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fe73d8b.mp4?token=ve_Ql8j_uFL7VEBVzkIlmNqInZE0lz5rjHEL63rlScae1oFujayp7-sKIHhnI4hz19gRITkC4-gwosMQt3w4Tlp-iXOnxIcmNwd0Y-VgoMGg9djitgC0JjiNQpuqMH3dfctQ9sekGksNjlgtcjAmcrAZVIfNOOQrxSb3nbA6Q1oOf5PvFI5sEOSM-xux76q--1p5v9pDhKlbFwV6H5MLasJQmQIE3myyXjX1TyxVsAJ-xcP4edzNMCTlevLpvRTvVECMyFhJqELofdvb64giXTfuqURid92lsI-t2xk59OMO09n4m-mb-zR7CR8xZ6tDYmfiuVG4_WfQOmLEKP_MNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
اجرای شکیرا همین الان شروع شد؛ بزنید شبکه پرشیانا اسپورت نگاه کنید. ویدیو کامل مراسم براتون میزاریم که ببینید. نمیزاریم چیزی از دستتون بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/26095" target="_blank">📅 23:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26094">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoVv2_m_IYLJrxq-rhNmURkC-ilDnLXe0G7qMNHIuPx16YGEmTUe6P9ZHoSEGMSHr5T5hAT8HZqepyPDiqjnuI88o3nzVEotrB-BDb0EA7zUjsPzJS-osbvn98wiCSVVbSqiFmkbvzDyetk7Q68_SJrZO3brBLyBVlHlbO3KdRu_D2XsQKTL5sSFuJli-eZmfnuH0hQ-ddSTpv60xZRfPCDaqKzjkuIYePl1_XZdok3VUyio30_9UkfRtVwK-ecL2SCxhJ6FX38C4xFor_f01RF2HxFovrEZfv4seym-3k9jdwNJBTpHQ2C8Q7o4z7yucGVXHzdLRf7TYFcC6Sznlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/26094" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26093">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=JCMbCTZRlqyTP8wArZVl_YbdRfferL4oLNRHRO6dAhQYMBmo6Adst9GD0mtCTkpmZnpKjW9llw2v7Cs_AQpbZ1B5_6m_tHOAaotKgNC1qN9SVhgNIwIvB0vzhf2lMnTS6Z30A_es-uq-5W7FkTAi43HhVQQC7E8Y0VeRG7zyy00dtevtLA50Soe7B6to61cRi1QEbXgd77HQ3ggXjimrnOgEtJsoNnAUr2VEF2NpY8FEFzgure41ZhTA_rq8MYdBYitF-ovubZYhCvNa--DFCk6KXqNX2hUvg1D9uzWi0LJXpBzbePeUEnBVhs_dtQUkwG6bA8Nm1Hd9rzRIhMNbHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2daebffff4.mp4?token=JCMbCTZRlqyTP8wArZVl_YbdRfferL4oLNRHRO6dAhQYMBmo6Adst9GD0mtCTkpmZnpKjW9llw2v7Cs_AQpbZ1B5_6m_tHOAaotKgNC1qN9SVhgNIwIvB0vzhf2lMnTS6Z30A_es-uq-5W7FkTAi43HhVQQC7E8Y0VeRG7zyy00dtevtLA50Soe7B6to61cRi1QEbXgd77HQ3ggXjimrnOgEtJsoNnAUr2VEF2NpY8FEFzgure41ZhTA_rq8MYdBYitF-ovubZYhCvNa--DFCk6KXqNX2hUvg1D9uzWi0LJXpBzbePeUEnBVhs_dtQUkwG6bA8Nm1Hd9rzRIhMNbHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
خب‌تادقایقی‌دیگه؛
عمو بیژن‌وشکیرا خانوم میان وسط برامون برنامه اجاره میکنند حدود نیم ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26093" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26092">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A11u0099I7O13j-q39lUSvkBpj-rliKeD5rebW4YaPzJ3bMZvh3ClbZc0B8zBFkDW-piZ2Sh8DZ-VvXIfuXnCaRa126P4bMYbfmpdsUkbI9WCPHtovm4IaHFIJmOYvkK0thlEjakkwOfZ1hJ_bPWVfsb6oxxNF8mWexEa3PQJqj7UZ4WFUzMGxf-9bV48uckAjHKp-Kecj5PMM5QGcoEtOET9eo6cGiz2Lr4fll47sllh4Ta1_0NCQ_FEQOaF-Nknpckqaf6epKOC0N03Us6Mwm-FMvBb_CB4o5831ghCVLAAmyyRZeeraNlL4UDZcBby2mhYNK4quAfIc7VzjJI0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تقابل لئو مسی
🆚
لامین یامال بعد از 19 سال؛ لیونل مسی: چقدر بزرگ شدی بچه جون! انگار همین پارسال بود که داشتم تو حموم باسن‌تو میشستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/26092" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26091">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfr4KfCTsD9oMH5jZJDqUP6ylxvc7vKLWcXRaSziAgGgCGyLb0xENP-cqPcereFkhWyJP_gNWszGajZcpmF-7K6_HNgcLHo2ho6RsOypXRRdp-MdHdjNverdOd1IBLJWiLPZnfsDjyW_GIo1bDin14PxPnTRUXcn4p7bfLz7ZZ_1ggo2CfcrlRFKLPgQwBZVYeYib7efZrP4bITuq_UV_w5Iq5TYyPY7Vl3FRxbGBN1WH-OyNiiJapfFuNotElsEdPgPgtnqhRGjj4KdV5czS2x19CKjsU0iB_mRQvDX1rz8MIOHKCkQQp6sotBmjSxXWbUlIrJk6JUWhdr-IfYSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الان‌فهمیدم CR7 چرا انقدر بچه‌داره؛ جورجینا: من آرژانتینی هستم و تو کل زندگیم طرفدار تیم ملی کشورم بودم و امیدوارم‌امشب آرژانتین قهرمان بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/26091" target="_blank">📅 23:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26090">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🏆
روایت‌جالب فیروز کریمی در ویژه برنامه امشب جام‌جهانی‌از غش کردن معروفش کنار زمین مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/26090" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26089">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=HZDO8EdLYvO1Fz_pWbVOUD0FuU2AXOyCAFmOWoQlJBkOeKM3EyA3P4ARd-oPYN3Lb9fOdOsx241b4jVe7NYk85L1YFJ9DomGY8hLgbmnhxSEIzVqQRgwCX1u3TQS6VRyHt4YxmTvJRqF_CLXkdCXk8RsQ3Vs7N7khNUrewnVhASKEGL0B_CWmZx26kHXGXyek8b-LhKqdnx3jNi3eOmdsAyaViUeEgxl4_XE-ubmcLzKTV34XnG8_uTkOg1ZOTMTEzdmgnrPxlBw8X4tUnHKxSSGEXmTZS_og4lRdulvUYoeUFLxDg8FHCLgwOLzjC7Tjoor62OFeAAQ1QtVl7KAaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de9d2fca55.mp4?token=HZDO8EdLYvO1Fz_pWbVOUD0FuU2AXOyCAFmOWoQlJBkOeKM3EyA3P4ARd-oPYN3Lb9fOdOsx241b4jVe7NYk85L1YFJ9DomGY8hLgbmnhxSEIzVqQRgwCX1u3TQS6VRyHt4YxmTvJRqF_CLXkdCXk8RsQ3Vs7N7khNUrewnVhASKEGL0B_CWmZx26kHXGXyek8b-LhKqdnx3jNi3eOmdsAyaViUeEgxl4_XE-ubmcLzKTV34XnG8_uTkOg1ZOTMTEzdmgnrPxlBw8X4tUnHKxSSGEXmTZS_og4lRdulvUYoeUFLxDg8FHCLgwOLzjC7Tjoor62OFeAAQ1QtVl7KAaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/26089" target="_blank">📅 22:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J6DODH0vn6AtNeF7NenYfs1f3Hn2tKrHWvoY_ktSUEIX0od2slm5rtKBbbmtqQ3LFLDYh3xNYiOm7U3IouIIeSYkeCd_Bki1rAr8Fzwb5VJoozUQcSg3BIcuQkAg4v1bwAKL0uv7o_GdNM9qA0kWYRz91O4_HTICxwa0CGUAkop2bWNRfmZR5Glz0jzgMwyyWeu45XiQ0xJCzaS6S8eB2SjRGNnswoP2SqdmeCn_lSQs-50zOLoT0F2Q1Aq3WJIdU-qJgrfnTEfuqYctDM0MBVht-C2uPU8YZ5vgWTKMUawXZHXcw_O149Q4knnFaB7zctIczYhwfR4Vknr6UYcGDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26088" target="_blank">📅 22:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26086">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TZR7sfHUHEMmRbxX8tjKhZBG7N88f-nCiWAYv0Aorc-9VFcRXw8kSAllWEORD3G0iha6QR-_jJpyTlQ5CIHPzFGkqJlttiIyU1WC71As7rYFjLssisGnu_dZM2aAKUC2p6tuD4OTFyGRtRMUDjEwft4PckEFQ0h84Tb5-fHtygyBtPs8OQSRTnxCNh-PpyJc_7cVZuJHgAX4U-1Es6QRE_Ic1OERpB5vpm9PRDoJKaK35IOVgJrY6NgrxwuXGlqSt0EQifRjDTqsuOCxxyxCyTopQrlUA-_4SYegGGzCefAdZ9Lc_eP_LFbUmL3bSfqCBuyaKnHqkN90x4AG9w8KWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68101d4663.mp4?token=TZR7sfHUHEMmRbxX8tjKhZBG7N88f-nCiWAYv0Aorc-9VFcRXw8kSAllWEORD3G0iha6QR-_jJpyTlQ5CIHPzFGkqJlttiIyU1WC71As7rYFjLssisGnu_dZM2aAKUC2p6tuD4OTFyGRtRMUDjEwft4PckEFQ0h84Tb5-fHtygyBtPs8OQSRTnxCNh-PpyJc_7cVZuJHgAX4U-1Es6QRE_Ic1OERpB5vpm9PRDoJKaK35IOVgJrY6NgrxwuXGlqSt0EQifRjDTqsuOCxxyxCyTopQrlUA-_4SYegGGzCefAdZ9Lc_eP_LFbUmL3bSfqCBuyaKnHqkN90x4AG9w8KWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
عادل‌فردوسی‌پور: سعی کردم تیم ملی رو خیلی منصفانه نقد کنم امااین‌حرف‌که هر کی نقد کنه وطن فروشه نمیره تو کتم هر کاری میخواین بکنید. وقتی اینترنت بین الملل نیست من چجوری میتونم برنامه بسازم. عادل از اوردن اسم قلعه نویی خوداری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/26086" target="_blank">📅 21:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26085">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9df505731d.mp4?token=imw9ZXJuMAaNe3e1I9R7u5AUEwQwbDUdQI60de0RiWBVG5rxxDSzUkpdKwc_8I_59RB0RiWabmJFls8M0O2EVvBe-DQH2OUqIurLw6fECqH7hs3sKpSLWx4gdLlxD_7NQrQaZQ2QztwDCMPfpUhIMeNwsaZk0nK0_zkswS72zaa37N5Toy2I186LXj_59F78zxbTOxUpl_lOjKWLuN_3kp2cvXT9YVO7ZJKzSyrgTWoSKDL8qPW9uHuUpr8uXXIgXFRRs3TOSLax2Vyc76zkcftwzwfKTtytFuR6aFpPbLlXPoOu68HamvOvuqr2CQfBnpRhklG4Ml5LAGIDVaZ-CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9df505731d.mp4?token=imw9ZXJuMAaNe3e1I9R7u5AUEwQwbDUdQI60de0RiWBVG5rxxDSzUkpdKwc_8I_59RB0RiWabmJFls8M0O2EVvBe-DQH2OUqIurLw6fECqH7hs3sKpSLWx4gdLlxD_7NQrQaZQ2QztwDCMPfpUhIMeNwsaZk0nK0_zkswS72zaa37N5Toy2I186LXj_59F78zxbTOxUpl_lOjKWLuN_3kp2cvXT9YVO7ZJKzSyrgTWoSKDL8qPW9uHuUpr8uXXIgXFRRs3TOSLax2Vyc76zkcftwzwfKTtytFuR6aFpPbLlXPoOu68HamvOvuqr2CQfBnpRhklG4Ml5LAGIDVaZ-CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی تو این دو ویدیو به بد ترین شکل ممکن‌جواب‌صحبت‌های‌قلعه‌نویی رو داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26085" target="_blank">📅 21:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26084">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0_ZqT798I3sGF1Mta84pMtwH_32MDns3jvF7q5-2UZ68qRnUwUmBppDNmTsBfpb1I1FPRFtY_opO4VrWiOn0FMT-yiWffzdenQliiZ0vYywFP3Hz80S3NFAuMDzZRTQwE3vszqp8gbWtm5fQPNkOR6Tn_RMT47b9PDc1ykhAH6Z075tCIfZHmjdBJE6OBSAXvW-nVSt-epJVhnCUhK8GoBRcq_ermivuO6zcF_DWNhm0n9LtnbNxOeSIuh5kETNR6QEgOm8AT2xeTPLcJ6dkNEO6uyHzB_zJ8MyQ-5iMDhcu13rQmUQ2xhpzQsJa6BwWE2aYpSF-keMaeGK68UG1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26084" target="_blank">📅 21:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26083">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=G5lYJOgf3HDvpohGslu3WsMcx7OltuE5XTpkNcO6AohaN5OMKZn9eOvksbCjxaFMFfkLYcysymlUpeu4RmJ8wnF-PCZRpqKi16NW-wZBIwIpVjO9gcZq9BafEkDS9tS2mao4Lfri_hqOpo9NAlOyLhKzqGNNd5BxR_q3nxmtFeMSZeN-Dg3uTuGf8DcRmb-wsJdl0I8ald_YNDggVtx-hSqVO-oeO_Y2lNH7ODfR5ZGLLAlcKs849NqOfZnhKXiOdHsp8qy7l5-T_gAUOYh3t7YfHzmbwPGNhmxus6shvBiUXDGU_v89eANcdMOJzESlpw2Kcfq1FMhiRYETEqNYLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f87ee3ff.mp4?token=G5lYJOgf3HDvpohGslu3WsMcx7OltuE5XTpkNcO6AohaN5OMKZn9eOvksbCjxaFMFfkLYcysymlUpeu4RmJ8wnF-PCZRpqKi16NW-wZBIwIpVjO9gcZq9BafEkDS9tS2mao4Lfri_hqOpo9NAlOyLhKzqGNNd5BxR_q3nxmtFeMSZeN-Dg3uTuGf8DcRmb-wsJdl0I8ald_YNDggVtx-hSqVO-oeO_Y2lNH7ODfR5ZGLLAlcKs849NqOfZnhKXiOdHsp8qy7l5-T_gAUOYh3t7YfHzmbwPGNhmxus6shvBiUXDGU_v89eANcdMOJzESlpw2Kcfq1FMhiRYETEqNYLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه برنامه جام جهانی یه هدیه به ایمان صفا میدن که میگن این هدیه کوچیک برای شما! بعد صفا میگه این اصلا ک چیک نیس چرا اعتماد به نفس ما پسرا رومیاری‌پایین. جفت مجریان‌برگاشون میریزن میفهمن منظورصفا چی‌بودمیگه‌تموم‌کنین‌برنامه رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26083" target="_blank">📅 21:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26081">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">❌
کنایه‌قلعه‌نویی‌به‌علی‌دایی: ساعت‌بستن و کت و شلوار پوشیدن نشانه شخصیت منه. اگر لباس یقه باز بپوشم و زنجیر طلا بیندازم میشوم مربی خوب؟!
‼️
همچنین قلعه نویی از مسئولان جمهوری اسلامی خواسته که مانع پخش برنامه عادل شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/26081" target="_blank">📅 20:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26079">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n8J6whL41NTa6a25yTjPXCC02x7R1kdJIFh_i9xFQQyUqYIfxA-k9OrBUJiXKfgEHa52lG7M0s2Gqua6iNBLSDYHpWoHTXyg5kQHFtF5hbftIHMrtCxMXLOdbrXrW-fQcnCFwct58KSnB-1zsU5V2Hj2GRFONbO2KTJkdIhjeLd-gNJ5lcbQ10Q0q4GHnT13UavzP-I6jCW63FHKCSTgrSQwYhx--GqT7IEf5ZhTWqpYi2kf7af83sctcLo2nkPX9XYKJ6jL4K2098EJe9bShqKoiH5ZOH49jMorKDN6YU1aKSuucyElxa2YEI9OufvJfbZ1Yml7CxJlNJAP8G4KNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/evDxnIVakTty2as2d9ec1yfk0j3FC77pc9fwbjeHd9hw7LTXZ1ncZ0AjGWmsSUf44lBpMLwVuBsDqMMA9aV6F5cTdPynfiXA6GdEbgaDD1WwaeHKhP00lHC8RSAq7Dg4CAmHPa7_yvroUNpR0g_yAWTDerOup-z2_DPi4-QTK86bLSY8EcX1WZMSGS9NruBajdA5brESsBYD98EOmZBbUodSRHL554PGhoQpda-fonxBaQPwh2qSdMFUytB8rI2i6TXq1FN7bLhIVHdjHcDcuTKD8eODdYpnbSR9_pzFRQGP7MhcS8u7oUDkkcCKKymkiz4jWQJhG5hDPb62cHbVxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فینال جام جهانی 2026
؛ شماتیک ترکیب دوتیم ملی اسپانیا
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26079" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26078">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQQmSYmZICRQKMENx59Uc6Uz5qnaYR9wBnXyYe3bHvcQpE3lr_FKDYA1-REpBz2LDw-eYeNyZNR2UJRzVqF5978JAMntpfn233X_E4mxL1JyCpT0tCb0m3B3BwNZXOmu8afbgc9V4tGn-FuOWwW1b1sF7kxHwCqLbrbRTVIvHvURG5CnqIZOG36DuI4jbQhXkcx3jQV39pT68j1VjI07T2vevZE6L_oVeRZAoI8K-3QHRv5aRBpvalFLEx8pjCv5cqTtLCwJXFIdzZ31ZdTItPu2Bq9rvv719CwHYvV-YZjxaRUJbaY1IyhPwdHLbUX04K2NUXa9CCuGs6mqFEhzEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26078" target="_blank">📅 20:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26077">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwQL659sEL5Jz6QhCPuc7BHmihPAQvlI2GOfTBhpYwLwda6BlhTsk9ZazPehXog1CRAKqqJR91twrG4Uh9awK_JhcCXgfM7N1IYBBvEEZj4JbPoar5l_DDZDaxVfuYW3NkEpABSUPVG7mTl8vJsWbt6We7yjR3JkH7spBQjksUXPpIpfSV12C2HJD_aPgpaYTILfSSgB-s1KU3ATqXN-MUBas4ZhAGp-01qlNlA8341i1Tvy8YMOrf0Ff043CE5KyrLOo_J0c7ulGSZEw5BgzX7YaLqLhShSia-q8qqQXn9MTexUsfjAaDq-BfvjapH5HHCXoE80IR1uG3vSSUqvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/26077" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26076">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXO6mSRlHhWuwBsHNUoez6EYHNGML8256CCUMtsrPZLhak-AYkp4gKwHTWOJcXeyTUl7t2XzvrUtebJx5Dac9h28Y43cEvVqspZ2xsdjw6y78eNboLLircWvLO2pAIrra3jFPyYJ1MuCkUyIIqob_89T9YRvwuLx-URG74OWHQ571ICWzoHfPzu5kFBMrJudhJp-wYE_DrLcQ_Dg35c9T-RQUlJT3VsoEO5oG1f4ecB_HEheFVEcINDA8vxmlxeGRp6rk9prYc4K1HGDTuaXaqCd8y2Mr95WS89HxaVIdlCHsCC2FIsOpNuitTab0ggc1f8xUeSMScAB5rTiDhohzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
خداداد عزیزی سرپرست باشگاه تراکتور: تراکتور بزوی پنج خرید بسیار بزرگ خواهد داشت. 3 تا از این 5 بازیکن لژیونر هستند و سابق بازی در دوتیم‌ پرسپولیس و استقلال روکارنامه خود دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/26076" target="_blank">📅 20:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26075">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTQDNLkJcA30vA-MI0BiSQnDb02zgP8_0yPEuYRq_c-0D90PgLcx65DEGfQGhSzyoIAuVZ996zOK4_q2Vjte_hkVHY-evhU73R9msnW-MmWiZss39J0iZRGL7hN2OAoewOeox3yST_3pk_HvVt6zaBHngALrQlYueY--31PqPrRHYEsw7kmpsC_piYicl8X5a6tjcoQH4FVaZERI4LXUQRRd-7wVaZ2ppl-JJSyR7MRtnwevWM5yThGG4RtNet7ejScWI7f1KMWHvgwvFjaZwNdp8U2syWVRl3KZHT1w6WppI-_c0iOZwNkdIB_ibcDgn8uJK00hirnIDOGe0lNjSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛ سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26075" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26074">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXtu3FdPlYwO6Da9CVO6M5GmFH9OsOp0Pik4gvPtJ6hvFJwICj-xpQG7t-HGJn_FbwPSkl-kT6OiN1jtW3dA1PFd8FzZvBSX7CQ_pJyGKHx4mjjh38eaQTHuQ165xncDz6YovjeRzvwAbysLizMYgcwW7d73mI8uRLG7WXtb0waQ0ZArJ4fnvPPicb5PC6EmaL4bfGZ1-mQdlvDFA9AZSQwj_aA-WLHSLkqXGSp1kgqifzWWQMWUhxU8ImandZqtnaeEQRe9TvdQ8HxGpO7Y4Z7ZvWT2GPijv9JCGgtHauDbU2q1RDumWR9TOyir7OQlN1TPXAgLeBCxLhdS0isW5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
علی دایی بهترین میانگین گل ملی در مقایسه با کریس‌رونالدو و لیونل‌مسی دو اسطوره فوتبال دنیا؛ بعضی رکوردها شکسته میشوند، اما بعضی از نام‌ها برای همیشه در تاریخ بشر به نیکی می‌مانند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26074" target="_blank">📅 19:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26072">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3AMANXL9YTCy37IR89TIfkvEfNr_x5G40iRSoXzWSUTKEP8_Kk7hH2mUq9oxjugO0htkRoMdxGA0l0qw9ubtRIzCMWCVrDAe6ODgHThUJz5bj_F1LTMamx86WybyHdTn4HY_0afJ-34wEQvKLILyFFWJ_WMwYWqDVbuyYNOlCwN11WfpZg5QKx5ztQK6RFKfQ7OrG1Fi0T-CV-a3gwNzcV35jem2Z5ohMiWVrVNXVMUUMNRsUuglI1KJz4qjddlZuyAlEgMjXBCAMinuwjdBFrWK4cDdBili-UxUNlqhRqfzBJrOWycfRqdrQfM_7wZEeI27pY0vzleeLvMtk2DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مزدک میرزایی:
عوامل‌شبکه ایران اینترننشنال در سه مقطع پیشنهادمالی‌بسیار بالایی به عادل فردوسی پور داد که‌به‌این‌شبکه ملحق بشه اما او هر سه بار این پیشنهادات رو رد کرد و اعلام‌کرد هرگز خاک ایران رو به خاطر رفاه و منافع خودش ترک نخواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/26072" target="_blank">📅 19:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26071">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCiShKAuVHvPnloWd7Qbc8XTLgt5qONMWoX_az4N44VTXOe4N5Y4el3OUf5kcSmE_w9BEMQ0-t8tcsDjj-7kVUiFU0mJ-aH_F29xnqYUlw4cjIcpFS3TqNqCJKjGMdnMM-X8Nk7-Z7t7HO37FOXt9k4dl4wAVGOQV96CS-fMhMq5LQBSTUP96hsSix7eu-iN8abErO4Zy1mhHzDkLcLt_qdgbkwfZuoX8p9PvNbXUk8jXyrkj4Q8ek6l_cIy6rt2naXlWPBE26LO8l9kCvIAW5U5mLh4HeT76IjaD3XSI9FaBotKv_nDIRgoESl4Q7vkzVH5RR6Zxa71U3S4VNws4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/26071" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26069">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=JC11nfgiC5kq4JEs6WBrUdh7FG9i1QeQFaXzJFprIuTobX42572rL52cjzdQzuz-zeN-hEVninvo_i5cvPR8eXJpENpRZ6GUsswidFA-hEbbvqb6iju1peH_pqrBKzQYDO_DpLpFYYIRas5nTsIoLu-agfJwjugYu-yw894v6T8t7nqNZSglFkSwRY7VGswwbu1rIn00xIBl6B0hZoUDlcwuiGdEjF6TnzUux1A2yQrunGgVCTmG7sLcxcv7YIKX6xSCkK9C81ilISSzfSVCcZJZb0FAzIDvJ3_ncjyEMWFx9t9wFHmacUuyOeFeuZnVxEunKnH7-2f6JeFP_k9OJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76a250b46c.mp4?token=JC11nfgiC5kq4JEs6WBrUdh7FG9i1QeQFaXzJFprIuTobX42572rL52cjzdQzuz-zeN-hEVninvo_i5cvPR8eXJpENpRZ6GUsswidFA-hEbbvqb6iju1peH_pqrBKzQYDO_DpLpFYYIRas5nTsIoLu-agfJwjugYu-yw894v6T8t7nqNZSglFkSwRY7VGswwbu1rIn00xIBl6B0hZoUDlcwuiGdEjF6TnzUux1A2yQrunGgVCTmG7sLcxcv7YIKX6xSCkK9C81ilISSzfSVCcZJZb0FAzIDvJ3_ncjyEMWFx9t9wFHmacUuyOeFeuZnVxEunKnH7-2f6JeFP_k9OJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام دیشب نیم ساعت دنبال دوست دخترش گشت پیدا نکرد مورگان راجرز یهو اومد گف اوناهاش اونجا نشسته؛ فقط ذوقش رو ببینیند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26069" target="_blank">📅 18:55 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26068">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_Vmb-OMg9BmOWjm5JbvQFlqsmuwqheOriCzZcUoOaKQ-03h-ki8cIm1n4DRWRxNZrFcGgq5hIV8iBomgGc9WzaW6ifhESKglE0w7V9qNdr-JhVWiabqidelUVGBG8c8leANnFvtPdHIPH-lVoUL5JnXTCXztBzv_ZFMYkp8YTeAuGUz1EQ9BVgn0weCLGt9Ufk0BW5xWWdfVrEJfYYd5Hkdq7NY7W_CcGQMgpd1ZfqkhSnKZOw1rA6L1KcmmRmfXfzRHqhCq531SguovHyUJAUQUDkk3EZQLIiPRvkEHEuhXklvYFHXLtzd_nd7em_inMk8iVPHd8YVRDGZ4ArJVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در دو جام جهانی گذشته؛ تیمی که در مرحله حذفی با نتیجه ۲ - ۱ انگلیسی‌ها رو شکست داده در نهایت درفینال‌باخته. این اتفاق برای کرواسی ۲۰۱۸ و فرانسه (۲۰۲۲) افتاد. در این جام جهانی، آرژانتین در نیمه‌نهایی انگلیس رو با نتیجه ۲-۱ شکست داد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26068" target="_blank">📅 18:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26067">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uSzv_gwARiijvz0RXzDRLBUGUwm1ebOoleMUYa4ay5_yhmkSdR_cNvo8tBj26gfWqRqTQgI8aMJVzbUTOH4iny5m15Ms6hUAprKw4ObBbenMNsPsxbUr8IMXxqDW7tmydBe94GPMs711I9tfpPxDwcfIT_C7tBDBMNvndlVkDzRsa69kPkeoqbtxkVzDCwzGA23B0EZiaTOoeWgauGKC1dj2jy6vMkkpXjYmvN1Gd4CiuT363KgXycmdk5AWMte8ooHke4xzT9KYjgC_d04uO25gzuscEXEJyHyiVIiZdb799HH1OpKJejO8kFkBx4xSIPkbGgydFz__HPtFaYiwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد محمدی مدافع‌چپ‌فصل‌گذشته پرسپولیس باعدم تمدیدقراردادش با سرخ‌ها با عقد قراردادی یک و نیم ساله به مکس لاین ویتبسک بلاروس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26067" target="_blank">📅 18:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26066">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXIFYZ1_gcQjGobtAJTrRJ2dxqUquE_Xt-nbe3DCyQ6jVg3BzsQ9-qtmEIWa3eNWgLDH7fRE7U-FPYE7QQWFT_6yqC0GMAJrI6aVGXpFjNgrAFszsM3CYSYxBqzbEt-LMWrf-mHpdim2XOq7Bxfe-QHWN1T0_3E_sX3AcP2uXQbCqNA8Hupp1U5ZBJ1U8e0fSphlaParsKFCpDbxBbiJ-59uB_huv14Ec2x0wjyA6OxHB97ZvuABtlzRsi8EXBLsA7CsS1nBoAZMGZsm6o00HVRc1ONV6-5jaNOMiyY8HnLUtLn1tzyMc1Yc_naAfxpp__UCO6EdXRh0kdO4B-CG5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
طبق‌شنیده‌های‌پرشیانا؛ مهدی‌تارتار سرمربی تیم پرسپولیس از وضعیت فنی سیدابوالفضل جلالی مدافع‌چپ‌جدیدسرخ‌ها راضی نیست و به او گفته اگه عملکرد فنی‌اش بهتر نشود مجبور به فسخ قراردادش خواهند شد. تارتار نیم نگاهی به جذب مدافع چپ نیز داره. جلالی سه‌فصل قبل آقای…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26066" target="_blank">📅 18:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26065">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=d4gurNouEnwdGp2WY1bSZaLBkedPnCdkL4cOApbc_QnXKB4QzlRQZO3OsYjtH0t59JUEmjNJcM9EQBn05VYGz-u6Uj-Bpa4dtu5x6qGRmw6MFx0AoaHphgG375kdWck2NiV5CTAQ3W167qqZ5KbqMWB8Httyd-THkii39Dab7HXs0LyzLp5ACTXvg6Y5SCfYwZTzeT7cI5j3xbFFM0BXORL7uodHTu6n_SfuYM__knZyk2nsjlI0J4QdJ9MxgHmlo1PQVwNAUXWGs2Qpc3Bw7m4TmUF2QHgG_i502LeMF4-nffOHq1Yubpc1p9_DJTaKbi4NefG16Di2HP8dEvjoWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33544e2a7b.mp4?token=d4gurNouEnwdGp2WY1bSZaLBkedPnCdkL4cOApbc_QnXKB4QzlRQZO3OsYjtH0t59JUEmjNJcM9EQBn05VYGz-u6Uj-Bpa4dtu5x6qGRmw6MFx0AoaHphgG375kdWck2NiV5CTAQ3W167qqZ5KbqMWB8Httyd-THkii39Dab7HXs0LyzLp5ACTXvg6Y5SCfYwZTzeT7cI5j3xbFFM0BXORL7uodHTu6n_SfuYM__knZyk2nsjlI0J4QdJ9MxgHmlo1PQVwNAUXWGs2Qpc3Bw7m4TmUF2QHgG_i502LeMF4-nffOHq1Yubpc1p9_DJTaKbi4NefG16Di2HP8dEvjoWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تمام امتحانات نهایی پایه‌های یازدهم و دوازدهم چهار استان هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، تاآروم‌شدن شرایط لغو و به تعویق افتاد. وضعیت دانش آموزای  بقیه استان های ایران:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26065" target="_blank">📅 17:10 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26064">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGp1q_SIDUZn_ho7VaYMvHTfZyIWzeTrUT993MR2to6SzyXFOmy1m1KxL-FuNKXcMGWWQP3jO4Z1mLq_QS9IPPR-oE2vvfvy_TMbsHn62U9p1xONTglujR7BEdcun6gITUTG9_MOkoYodLWwitjEfjOJmZ_SD-jMCfC5Kn8t9uGF6pLe2e-JxR-cI1VIMGBZLm-ycMx8VCWCofCRVrbaQvX7Q115VPGVzBe3y2NKgUFFTbVoqiQJfe8af3wrOQb30OKYZ4E6HGXdA3ARcFIvfIOMih3O2pLqY1NBLBiGjn8Iy3j6opkrkT9hggvFnftluZ6JZutv9OCNK4fL-pGEog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/26064" target="_blank">📅 17:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26063">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=qS2GPW0Zfym18bwiBHIohBxd4bkLgOkfYV8lDpXfa0isHAo06ZOwT4C37uNHsqJCjZOfnkZswpaAt6vHyco7o2sZw2Cj2v56nNsSSX6FklzXvT5hDj1sIrQaaUPfmuxsHNW1Sur0B4ATUA51MGL6zSTOFhb-MA6YAl9J7RFar39AjB0pRTKfHRq6tal6iX2t6L2qNaWFRknZybiIOOAhP4Eijy7VvEAJ9cSezeopjG8MvFdRJnK47OfpPtHX531J6fcpMpufvC-zyzzrhYCZZjR0zVzY3W-I5d3do2TMJqBRh3M_c-ahoiAOwiUYSIiX322G5iRwHU5XFzWdk6cmiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3d2e6f73c.mp4?token=qS2GPW0Zfym18bwiBHIohBxd4bkLgOkfYV8lDpXfa0isHAo06ZOwT4C37uNHsqJCjZOfnkZswpaAt6vHyco7o2sZw2Cj2v56nNsSSX6FklzXvT5hDj1sIrQaaUPfmuxsHNW1Sur0B4ATUA51MGL6zSTOFhb-MA6YAl9J7RFar39AjB0pRTKfHRq6tal6iX2t6L2qNaWFRknZybiIOOAhP4Eijy7VvEAJ9cSezeopjG8MvFdRJnK47OfpPtHX531J6fcpMpufvC-zyzzrhYCZZjR0zVzY3W-I5d3do2TMJqBRh3M_c-ahoiAOwiUYSIiX322G5iRwHU5XFzWdk6cmiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
مسی و آنتونلا ازکودکی‌و‌ازسال ۱۹۹۲ در روزاریو باهم آشنا شدن. بارفتن‌مسی‌به‌بارسا ازهم دور شدند، اما سال‌ها بعد دوباره به هم رسیدند و در سال ۲۰۰۹ رابطه‌شان را رسمی کردند. آن‌ها ۲۰۱۷ ازدواج کردند و امروز همراه سه فرزندشان، یکی از ماندگارترین داستان‌های عاشقانه دنیای فوتبال را رقم زده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26063" target="_blank">📅 16:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26062">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUKb8n_ZWEBT33xMwQu1pN9Xrm1Rn_4fCHD9iksohnhG4nf8kOeRGkHg-_7KQpOSg3jdhPvsbHC9z7D4sXlhehQZxPrMLnhIlgDY-9UGMdWpcQXnKE4FgdHllzmStcnldVUPmtt9HRQlOenp-KrSjP6reTeO_eoYcvgcNP7xKiT1nJkWHxD07f83E7A5e6py44HYMWOy-tscpGOnweuK_CibvPuTAwUGPqajikacaz_wxZ0VYv95mk7XiUqMhHqFcuWsd6sTFLDJhz3BGgxxHh9BDJKhmVTMmukPd0_H57T10vXiwGM5nqy8YJ17_LTjMlyKfdnC43NybDKzblST7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیگ ملت‌ های والیبال مردان 2026
؛ فقط یک ست خوب و دیگرهیچ؛ پایان‌تورنمنت برای شاگردان روبرتو پیاتزا ایتالیایی با یک شکست ناامیدکننده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/26062" target="_blank">📅 16:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26061">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlI96U2Q4IXGCzSJaMMftioYASqt470VEZfUDmueghJuCUZxLiscNxfe_YM9rejhmITKJZT6BAhddCuIxFLZ8QD5DbVs1hwL7VELDRySIEsGRHQsHf0VosOik3ZpuLS3NGa_Zh9TKxPVcZT200ti0Fx86x8GGxkOTolWFsErS94-p31_UcoZTEA9mz0Dq62iqhm0eBWpOQbDh-XLY6KA84ie4Tu8VP9h4sgeEb0LRVyJTHl1forOPmSQxFD-GfqlYhtDv1MsTJIZP966Nlp_kcGbANbkDNoGglJni6V_8Z-aYwAueuXTtwWRGhn6Ir6uUWfsBNrON5y1ZAEtsvhjow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق‌ اخبار دریافتی رسانه پرشیانا؛
به درخواست مهدی‌تارتار؛ مدیریت باشگاه پرسپولیس با 3 مربی‌ایتالیایی،اسپانیایی و ترکیه ای در حال انجام مذاکرات نهایی است تا یکی رو به عنوان دستیار اول تارتار در فصل جدید رقابت‌ها حضور داشته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26061" target="_blank">📅 16:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26060">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHcn5rmuzboxeJ1BqAU37VQ2W39Vnb-kg9qujFNns_cFaSVcwabywe8z8jWw7sSZBt7O8iHJ7CU-pBiOyTBpkgAQu8pV38Sd44hmBU03hp2zAE4K-ffaSJ9EN3_VXhfCTlxqifHURFR_b5H-6C6Dr8sbZFfyBqLblYvp-G2L_9mUEwWvOJuW0dITwySs0MP_VhZpaC4P8L1bgiaGPMH1sZI0BjpYHQRazhGfLw6DAgC-4PfDII3cO2f4wZr-uDJibwVnJWzJEVhrw9xDUaMXHr-I_gqyC4XjX2XxTzY7J0uEygEVkSJt42y_BzGyHfbHfALuG3ZG_D02sYooFHRHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: وینیسیوس جونیور تصمیم نهایی خود را گرفته و اعلام کرده بعد از جام جهانی قراردادش رو تا سال 2030 با رئال تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26060" target="_blank">📅 16:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26059">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=qB8N1CbP79ZgwJbsB0hOJtRBwzKfCZcxGi7fPucJlE6Qyp_vriD6pLV5aO5Z5OZnwAgs46pZJina6ZBbblOq4phHUPFW2pYGsUJRTmt1Km70tSrfbR1xuSeuyTmniUQP_GfjyOr-UU80XQpdGGOZ9YJlxW8so9kbNhAhteEjM1pOLAxAYltlSEu4eypw7yHIpUo1il-kC2xBcks1Rgkp-GC2hbUB4qBr8BViLl6Cv08H13XxZQMMNZG4ykjaEKommBnjuNAmI3KC3gRiVaKjl6ijbiT896Lj0izlvO2kXEnJYzcUwb81O9r5zyWl2Z0ztili0nm_7nw9s8FT2TtszQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=qB8N1CbP79ZgwJbsB0hOJtRBwzKfCZcxGi7fPucJlE6Qyp_vriD6pLV5aO5Z5OZnwAgs46pZJina6ZBbblOq4phHUPFW2pYGsUJRTmt1Km70tSrfbR1xuSeuyTmniUQP_GfjyOr-UU80XQpdGGOZ9YJlxW8so9kbNhAhteEjM1pOLAxAYltlSEu4eypw7yHIpUo1il-kC2xBcks1Rgkp-GC2hbUB4qBr8BViLl6Cv08H13XxZQMMNZG4ykjaEKommBnjuNAmI3KC3gRiVaKjl6ijbiT896Lj0izlvO2kXEnJYzcUwb81O9r5zyWl2Z0ztili0nm_7nw9s8FT2TtszQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26059" target="_blank">📅 15:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26058">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1Vlqwkiw6_AUe2Y2IBYrh1hbu0HSb3eX5WQVeOdZ8TE4wTPG6KE4gvHk38X84ZU-2exzJiXX7TmP7GAxoitGTvmHn6JJ-1fs2AwknDuq4EHY2cNWUheTkpCT4Dr34DHvFk2AwStbj5AMa2RaOI0GT5RHzWoaUvdyUDYfuB9SPzTBbfLMVXMG9q4d_I2fgtEwBa18FJ4DMFxrkxFVnewSue2rUvFk4xPzltLt5m0Vq0VlsmLc4pet92UDJoPbx6SQ5itUxt3njJwnUOWOuwsnHDHjCRAO3VubbyJ-lhVijHvn07FnRP6FcL9x1o-xyZE2DwjowJtpKTh-wBW_n6waA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
باشگاه‌استقلال‌اخیرابدون‌مجوزو مدرکی 80 هزار دلار دستمزد به اوزجان بیزاتی مربی ترکیه این تیم داده‌ و بیزاتی چند روز مرخصی گرفته بود و به ترکیه برگشته بود که بابت به همراه داشتن این پول بازداشت شده و باشگاه درتلاشه‌ مشکل رو حل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26058" target="_blank">📅 15:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26057">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HWSvyTx0vLagxaaC_hfO0JKrWMM26zEIk40UzyRT_bcr3150XAUBRMVu7EdX8RWZQ0z-L-VKgGYya-XaJthURt8gbaDf7EBIWS-z0aU3TkhfC4L21galxDRXejIe182eaS8KA5VNgBagaJMhreg3fXVu_Xj6mioSSKojC_EWB5ROencqSdDleEMLctvMPVPdqYEz0Or6PoaFppQG90mHXsEeWmyDCzHxwWckUSsYr5aVpawXm_JlR4N3B-c0fvZoX1dwHn__L2GFOEGCHyPx_Qt8Tkj9UhfKTabDhuIst0zifYtDN9uwUEFgMoDlcpL8pU1nGORWckE41qekjknACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26057" target="_blank">📅 15:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26056">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=Ydnt1KPPcV-wnEKDqX5yVkCiT1K3JFL_Rc5hYAEidwPQfLw-9MNFD9MvqbAPVZTy4Da3yYWiNAiTvVAlwF0p7Km3YN2iMQHItKa25S4V83GgIwozyDYhcNHxmM26cFGrAchoyiSL5kiYUXdQR-FtNRJHW_fo_0bf-6NaKV3VJWe4tN1FLcbb3A2zRReXKDkrdvhhY9qf38jZ1V93xIpNiXnOCA19uIMsFJ2JsVsVeRurEZA5RzYzDkYyiTRIx39OFpb5BOpF994seRepOoqYypdgHhxD0zmQpSIXh0fZ-DpV5ApwPT2aNUitINtT099tgTEgDExYX5N43FmFdiVZag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebd306e48a.mp4?token=Ydnt1KPPcV-wnEKDqX5yVkCiT1K3JFL_Rc5hYAEidwPQfLw-9MNFD9MvqbAPVZTy4Da3yYWiNAiTvVAlwF0p7Km3YN2iMQHItKa25S4V83GgIwozyDYhcNHxmM26cFGrAchoyiSL5kiYUXdQR-FtNRJHW_fo_0bf-6NaKV3VJWe4tN1FLcbb3A2zRReXKDkrdvhhY9qf38jZ1V93xIpNiXnOCA19uIMsFJ2JsVsVeRurEZA5RzYzDkYyiTRIx39OFpb5BOpF994seRepOoqYypdgHhxD0zmQpSIXh0fZ-DpV5ApwPT2aNUitINtT099tgTEgDExYX5N43FmFdiVZag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
از تاثیرات جام جهانی فوتبال بر والیبالیست ها در لیگ‌ملت‌ها؛ دریافت‌جالب بازیکن‌تیم‌ملی آرژانیتن با پا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26056" target="_blank">📅 14:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26055">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=FrvGTT0WQjjLFe6cYKkmunKp7MX0-M-QTkyLih1LAn60pEzWPO14PbcL5fuqmGUa5GBkyylcQHl3kPaNw6TjKHBaJDkuC_Pxmg9u4FoDyMUiqboJI3gz7NoVPhGaTkN27-TOOKCs28725LiIFlostaSIKZK_KsRhhwaHwq4lYR0GSHRBY-sDJVpP3HPFcm4-rJ-L7q4cPC-w_HzplgGyr7y7PXu385ilLlGHZHGWLUaxUK42nG7PNpPq1So6vQNBYo2NESpJVtflvK42QKWst-gz3hHPcGGRWx6dxeC5pQkhfHRZar_LtfxY7vtF9kYH5JtWN6RgkSkuTAvMUBZhDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e509ae8f31.mp4?token=FrvGTT0WQjjLFe6cYKkmunKp7MX0-M-QTkyLih1LAn60pEzWPO14PbcL5fuqmGUa5GBkyylcQHl3kPaNw6TjKHBaJDkuC_Pxmg9u4FoDyMUiqboJI3gz7NoVPhGaTkN27-TOOKCs28725LiIFlostaSIKZK_KsRhhwaHwq4lYR0GSHRBY-sDJVpP3HPFcm4-rJ-L7q4cPC-w_HzplgGyr7y7PXu385ilLlGHZHGWLUaxUK42nG7PNpPq1So6vQNBYo2NESpJVtflvK42QKWst-gz3hHPcGGRWx6dxeC5pQkhfHRZar_LtfxY7vtF9kYH5JtWN6RgkSkuTAvMUBZhDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پله همیشه می‌گفت زیباترین گل زندگیش رو در ۲ اوت ۱۹۵۹ مقابل تیم‌یوونتوس زده! اما از اون مسابقه هیچ گونه فیلمی وجود نداشت. حالا گوگل با همکاری خانواده پله و با استفاده از Google DeepMind، فیلم این گل رو ساخته. این ویدئو، فیلم واقعی اون گل‌نیست؛ بلکه‌بازسازی‌مبتنی برAI و اسناد تاریخیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26055" target="_blank">📅 14:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26054">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h4zshxGek0KX-LFGJwkNjX2331_dwaG5ziyz1uxhUI6jqq98uj6DbLt8KwOlSOSSPJjl26aZt83F_f9D07Cbs7YIOm6IVN72q1uAqjufgT6p289Sb5-BkRRQxiS6O0hRywLuJFQMZ3j_v5iNRr2rW4aa_4Osj4mgDnU1xDp9nG6LAfhTXVZuDTZByf9xwrTifoOBuXzoDD5kRXw9CJIhqaSH6A6-8qAW9BngmJsTLD77yUWyS85UyNSkV-3vSjQ3iC2D3YjQ64b-9nT8sKTQx87cyfZ7UY2nwipczIFEgn4uIl3_7ro7_HcvbI8N0UfXr0Gc8g3ToL5fqZfA60fDNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دریک رپر آمریکایی اعلام کرد که؛ این بار روی قهرمانی آرژانتین 5 میلیون دلار شرط بسته. تا حالا هرچی شرط بسته‌بود برعکس در اومده حالا ببینیم این بار درست در میاد یا 5M$ بی زبون هدر میره.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26054" target="_blank">📅 14:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26053">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwQeuo59iys3yyK06uwE6GTvRK41-rbu2gQA7BmeAoUU-5zEZ6CwRqDiV9gxWDcSX4Ah3LTT3Kn3sPeQ_s9oh_uRjj1TSPc3OlT-HwtwUp-xFZguvDiSodeY23Iybt9-k08S0IgfMZG4Ei5ivbPk6tCHl8Uzdxk6KRY7fiaZOamSVX74ynXNMXitKLKEf_aXt7exh4LC8GRvmHLWk5oH43eUH_CoPMpWxXtLM7qUGKs4Yz1Qw-PbIn6k231E7Qcl9aq6BXE91dxu7qYgijFm2d0RwNdYmmO4uBpzaUWvtHMmkfzXyq4lMo5SK87nx7YgZS_yDM-Wnc1L-BS-VGSHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26053" target="_blank">📅 14:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26052">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7wQ4VyxRCdb3UZYs_kO7FViinsefu0d5bOoVmMAlBrDYZUKPP-crtKjsZniKf-rxH17frS9aFd_l792P5oI3dvo_TkPivIhacMrF49OZv8CN3TbizRk1VYe6mvUFLjzS43zxb-7pLIQMlAKbROvvPGUjW32QfcawGfgbtZjmr3wxOK3gT11huTT-InbCZo1_tKH6NpgHmFZ9K5s92l2gMpk4YR8YeMchgGlwnjvGbiq_QiTFoNK57Uo2pqAIH7FjV6j_fIb3DdEgMcYoiz9uvRZqoEhuH_Zha6hlPJkvbU9HxLxNSJ5rElvHTdadw7KP-M0r6gszm-60_6xe7nbZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26052" target="_blank">📅 14:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26051">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEX5HlTzTj7ZtCghE1VAhzD_QszUm0jUN7HyRezUwaZ5WVXqRs7d6kbHpDWe_1Rj0CE1Mt8aI74MRnbQmwWnPh-m91gOOqIMQwmvdVN4Cg_G1XxwHGNQtF_f6bSYwvxFiH8u762b5zDWutmF7-2Qb-sKuYpz0f9Jj81GF1lZxKuS8u_GhrHm0a4PMuFJ2grrQG2S8GfiDym-iwhUOfcesRLu4bb2jo9zC0fqJFT5R7esdDaIYq2NxVEIprhVLSWgZnOAUe_74kW6QIxA1k9kZBApXbVUYj_HCd12oWvT75vcmEmdOlYPb1uSw2xWir3AaikdvVbKSxAn-o5NAAHShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26051" target="_blank">📅 12:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26050">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/thbouaBxKjI4ipJPbrJunjuvtUs2dxoFN22tEZyRI6cOnNxZNx0B8-zeY4Ljf7XQSwUn8dynaXrX7ru5Oz-CzLfBfun_C3EiQFgnCBsSNOfIQs6ozfBGbugO59vi5sC4e5WuJ2NsZj5yUt9nTzdc8Tprp3NdMXGS1eJdfGbHRtSkEbYvAfzM85f0sQmt6kM62Xc5XLCk09QWwLycg6BhgFA4aeHNDyRFeoeaw1hO1SIP-lbMqrKksknQ6eqoks3NHC5BCP3ZMcnafK3_8GYdikquloeOygbBj9uteb6258HtLxjf5TOHeKvT1bhUfbRxihfj_4bGpdRBN7oMVHibaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇦🇷
#تکمیلی؛ نشریه لکیپ: فلورنتینو پرز قصد داره به محض اتمام جام جهانی پیشنهاد فوق سنگین خود 200 میلیون یورو برای جذب مایکل اولیسه به بایرن مونیخ ارائه بدهد. بعد از کارهای اولیسه پرز میخواد انزو هم به برنابئو بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26050" target="_blank">📅 12:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26049">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnFfgrn4fzdIf9hZVhCpLOWGjCFqmgaL2WQTULNW99N8r2BWVoqYHTkS-dVoezzcpthMaibXMg_bjBI4l7q0ondbeGvBxFb7GRnBmeMOOuyya7uFnrX9rABIQa0wHA13oNyu7vEKjpXi7NR0j9uJJnltCWU6UGB4obNdmn1LTeDP2Vt1j2PzJhT6IoP7D1OK9Lu7h-dDeqpRW5nT5jSy5scxAgvhNaM02BT-rNUg162weWQ69AyLX5uJGwRjhiW7EV-tHsturmjktck6LHDARfb0I69ZeDJL8xN0uPXOvnhqac0guW323O2JGdfD8cv8wP6N2CbfUI96v7FugTwHAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
کلارنس سیدورف اسطوره‌باشگاه‌آث‌میلان و رئال مادرید درکنار همسر ایرانی خود؛ سیدورف فصل قبل بعنوان مشاورمدیرعامل آبی‌ها 250 هزار دلار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26049" target="_blank">📅 11:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26048">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojQzSAVrVdBMuKqh5lrEqQ0FmXBd_72Tk3wLDqENqyXllJLWzl5HNMhGUuMaHGtdu9t1lP5aO4ZnYNEQMwCbL0Re6Yi0757_xiGmxS9Tt-jeftedAV7jhg4RcBxXUoDT6_DIEv9evA7Qc_I9NrMemb9-nwLbfJBzCPTiRiEkI1GTx9zvpWXtZ5GSoMiYEU_Ed1u90U4vxqweofr4x_YYIOrp7_MT5l5DPdMJh0jJSKhVSRoenzVB_l-jiItIWdYstin4Tqo3Mgu27Lq1UU3_ufN2CBJR_gJgIBmtnrjdZDsDvcN2qW_1YvctGhz1ZsGvEXJOlU810GMZGZM1WslVzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26048" target="_blank">📅 11:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26047">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Weg1H8dznq5M-UTNqRxrd6p4mCqHxVBf05SBHR99lR8wU_fNOTMjeWJ_lqYyO4p7nU90u9Ag7hE_WIu3nEJUh_NO3BDjG4fMuob0p4dLq7K5JHy05JF0lWA5KsDlYypd84rMBbaZFH4IgNoEImjrbCxU0rIJYq74lc3Op-EjAMvMrt37VXDdHmW8uayex_I2DhjZlfth1c5AiKdBg2EF9er9ZOOWtC5WzqQ5bJkZavwAe9MsIhmU7jVhus3nCtDOVDFovaAlLJGH9uEtsUYUS4cAK9nx5sETYa5-HGOonCTq2rRHXjRg_WEABVCkd3CPNYkktSgy9kkZDa9HlOTHmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26047" target="_blank">📅 11:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26046">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlZYsj5Eu-vS9ErUYtEG5mI4IPazFKguVRIBuzoM6gQR8RKCXuJx4r-HWzQ4sM7qGl1C1DT3vyi2377aD6NceiDY5LuBS_Wa8T12paByICFGVD870LZf5-W_1biDVxjGIDkT2YKojLDE9Ia50jNrAsc0VcwSgDZvoOgyx4FoQxcjzteyclinJl9HzK0wE5yoc3t6SubBvUoZoGoSexedh28nX8YT_Jf_Qt7VFRPHw1_miTYjy5MFFe36ZVKQjxZEdujyg_ZIIpXfVUe3ecT8ViCVX9ptYA7cxfdml1OONU1TyL_sIPvssGgo22uWC1S4Y4YegLujZ9j4hT2VPDjvfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26046" target="_blank">📅 10:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26045">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ptk2YFuVf51S1uNfDThoDYDf0OrnVFou6HaqZiALRoTDLXvdYUMFiVfyFhDBC_jeqWzAUn9a_J27NZRiuq7ylNHD5S7ehoX1pGvEBndJJTd9b0dfstq5JZ4HCfUCEs8WNvRHGlDjyxcVuJ61pQKwq1Ey0VSreaOcATugy7LpiCUY-MZfVL-f4kNdhhnB5VnaSz-eFuEL4KvmtTuNazy2J5uyg5zTzqgHapLp2zsxrbCnZeTVVShdrV_ueDzJurWsKQunS_n04wua1nEVEP09_IqodnH-UN6WmkYKWRykvk7FwExBLG2AJd9NoH_8Qj3heZgcPyxJH7FzqR2bI48rMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
◽️
🔴
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه نساجی بعد از جلسه امروز با باشگاه پرسپولیس رقم رضایت‌نامه دانیال ایری مدافع تیم خود را از 190 به 150 میلیاردتومان‌کاهش داده و72ساعت به‌ مدیران پرسپولیس فرصت‌داده تااین‌رقم روپرداخت کنند در غیر این صورت توافقات طرفین بهم…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26045" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26044">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">📹
ویدیوجدیدوبرگ‌ریزون‌میلادکرمی بلاگر معروف و محبوب ایلامی و ببینید. رفته رو پل B1 کرج!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26044" target="_blank">📅 10:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26042">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05254735f5.mp4?token=o0MU3qvq6h3nA1WRsj6P09oag5noPX4r7kIN-TFQd7tj2ikOWw7CYUSqJMjMJbWDA03L9C_6EywB8NMrB1-8d2ceYMzc0Sgwk1jlkT6IrDqJNpf2M_yE_V-DDZI8qL4tp6XzPK8Ouvq1sHIkBer3XnLN4TQrysooh4PzHXYFjU_wB_Q9lTPUbjE9omcXVki0UmgMit-451FeizE8oFZzaRjoPOjkL2VURJXAU6XpxnBrVv1-Jbxx14oaDOioUjJogrboqK4wJ9iLfuO6XSxP1fsLg4mRRN4gZr95Txbtxx2jF6LMCCbr8N9umO5L_I5R9YdJnTld46BQN1AcbM1SIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05254735f5.mp4?token=o0MU3qvq6h3nA1WRsj6P09oag5noPX4r7kIN-TFQd7tj2ikOWw7CYUSqJMjMJbWDA03L9C_6EywB8NMrB1-8d2ceYMzc0Sgwk1jlkT6IrDqJNpf2M_yE_V-DDZI8qL4tp6XzPK8Ouvq1sHIkBer3XnLN4TQrysooh4PzHXYFjU_wB_Q9lTPUbjE9omcXVki0UmgMit-451FeizE8oFZzaRjoPOjkL2VURJXAU6XpxnBrVv1-Jbxx14oaDOioUjJogrboqK4wJ9iLfuO6XSxP1fsLg4mRRN4gZr95Txbtxx2jF6LMCCbr8N9umO5L_I5R9YdJnTld46BQN1AcbM1SIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26042" target="_blank">📅 09:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26041">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=PfgodRt-YIZFDKyrZIrbHb2yOJk6tBAiFpRlkaqxx1IPHY_flZd0Gf69tXyagYf9REdVc1WK9ffuKTWzu4Vm9PQk_KGxb2-gXA98pUEdrGtE06eVvNBQJnPrqhD43S8Ks8vZQvavglIkQBJ6L8A5gJx7-eaMgt17lcxkQo4uV03PQLI-gDmePvE26g4lTmK1rYHMKZWalkrCuLCJT1TQbm4kqQa6p2mcu6p3RngGVD8nQtqPk79u2gyCU6mMpRN4XxiFdNtlIvATQ0jdkvKER4-vn57FyhiAkxtIO3FMNWFjzIHv3iPEumdmXcq26OrshQZKqDjlexpaT1s3Wx-d4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59f65ac5ad.mp4?token=PfgodRt-YIZFDKyrZIrbHb2yOJk6tBAiFpRlkaqxx1IPHY_flZd0Gf69tXyagYf9REdVc1WK9ffuKTWzu4Vm9PQk_KGxb2-gXA98pUEdrGtE06eVvNBQJnPrqhD43S8Ks8vZQvavglIkQBJ6L8A5gJx7-eaMgt17lcxkQo4uV03PQLI-gDmePvE26g4lTmK1rYHMKZWalkrCuLCJT1TQbm4kqQa6p2mcu6p3RngGVD8nQtqPk79u2gyCU6mMpRN4XxiFdNtlIvATQ0jdkvKER4-vn57FyhiAkxtIO3FMNWFjzIHv3iPEumdmXcq26OrshQZKqDjlexpaT1s3Wx-d4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
تیکه‌های‌سنگین و پی‌درپی عادل فردوسی پور به امیر قلعه‌نویی سرمربی ایران در برنامه شب گذشته
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26041" target="_blank">📅 09:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🏆
گل‌های دیدار فوق العاده و مهیج شب گذشته دو تیم انگلیس - فرانسه در رده‌بندی جام جهانی 2026
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26040" target="_blank">📅 08:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26038">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPZqckFkYEY7L4KnaxyTYCBmWvou58qeEFViY62kSuZbR_DZmauNpB_Ruy_NYVNBcLqecIgUNF3IxCUnqOakpHOADghB9NGciYmbod1_-4RR0ehB-cyQfXC95DEOI4sv1cnpeZtDd7_tUmlbZW7ZE_7FIzb5vM2ZFnnUrMO2TJ_Bw7eGnwarrfwM8I6NhsozYqjfPFHs0pGNa8PtNeAbJwgHyxP1a5pkN6Ml3QJCKx2-bLH2tUG3hqMI0YFAgO5yt3z4IN1JmnhDjZ1K6M7M4KrLdjrlUzMDEpay2YdBrnsRdpVex3eFTSIQZo_NccQhjVAO97FZ9WjN6a8TRN4Vmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFno5tZQi0le5EefxptCQ_1nEebNTdrOucIJfdTmurFWJRtzL-I2Pr5ByYR1A0pCrkg4EP14Zr04kZU2CmNSm94V-mDP4Si6QdvqkkXcNrFgRykvpRJWOMzcFuRLSzfpR0aXEf9qAsJlplEWMf7jSMBeKMoFkflh4FqGcyJW6rrAFko0hl07lpTWGnfGdpOGAxJQfQTUUlXTxT482SKTY1EtwbZmVUFno7ctA77jd1-igf8F__NsZ9cMpCjXV-R4SZujeVHQjEo2t-UPFl-8KO3CAhVBFOHiKykyxFXZvwyfpcB4Ppn1PaqrTkWzdIh2CFe9YqkEhYakuFIzICAHww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
تیم‌ملی‌انگلیس شب گذشته در دیدار فوق العاده تماشایی بانتیجه6بر4 از سد تیم ملی فرانسه گذشت و رتبه سوم رقابت‌های جام رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26038" target="_blank">📅 08:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2HxaFmDA2GHo0YbXBlbjPuUkXy7dzoONX4YVlYv4tYxrhCQ4xMiwWngYNgaOEKEQPGvXpsn7OwZFPpF_CvC0vGhpQwiaYBD8GZUBQhJ2EO1VtLYIuipoT-G6wct9ZOpFT6xpehvs1HVAZPonXvJ-B7x37kDDGhGbCmkIRVwr3X_jWa1ys8K4cfwLtxnHGaNqVmx64H84EB7OT5YwZWzgffCj80LeM0_cxoAHGV22eaVHgMBw1iTr179rauvbfNTXnAOmR4zvbZRmPL1YURhBWDhWx1_8tCvUGoST9qCkJraQL9BNBggVAV4ujV48M70WeWmrC5Vr0RhhO7EObxNvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
مسابقه‌رده‌بندی‌ جام‌جهانی 2026؛ شماتیک ترکیب دوتیم انگلیس
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26037" target="_blank">📅 07:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=TB_7_3XMDNh2X-4LFOcLPrKm8_h7z9nZezLHibRhalG5HLD-r161R-rFj6U15jKe_LGTSXSsOie5JxePWQOADbFTlfN0iqe6-si_NRgRedvlSNw3wfMUxrWbEflZIjcnFim5z7QiggiFg-mHDQI4kqn9YGMIWNjIU99LndC19j-7dhIAGzZQyRr152uIsJBATSCEF4FV5D3YqzBrUP_AYu9IlViB17CMwgXthDGMFLmrcm_pFLJLzWs9LMXmsyXrRaGDvWAi3IyqfI1SIRqs0nh4Kur4l8Hmhracc_JWrkUBZdnHZvPJGKbMjQ0Sxdwsyy8hNXhedlLXleFiA6PQQYOu3LxBFzyH3Esl7AH5ZHtkf_0V6x7czcXMWdChuNTTvU6MnPrMZWqqrGtwbmFF29ynsXhaATfsvJ4zDLjQadiPRoMD5Zzebv1TXRwG93ITsPFVDUHoG7BC0Ci5-3cQxWjzp1FQUa2WrKgRH2Q5u-C2JfoJsNdQFF445RKCZCmpb2YMQZ9W6JfwFvygyGEZgtcqVW1xd9bymdBA6Lfxbd7A6dqkbLg_rHEhZd8BOly8L62TQI_Quo8J3gyGBtzFVp60k-LfvrOvy8-EX_TmxHBY318kjEwwGwcdI1tdZXNqr-jIl8scIbCDsNyew19JAuHLv91c6-9VJgtyo6wYRpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8dc0f4db.mp4?token=TB_7_3XMDNh2X-4LFOcLPrKm8_h7z9nZezLHibRhalG5HLD-r161R-rFj6U15jKe_LGTSXSsOie5JxePWQOADbFTlfN0iqe6-si_NRgRedvlSNw3wfMUxrWbEflZIjcnFim5z7QiggiFg-mHDQI4kqn9YGMIWNjIU99LndC19j-7dhIAGzZQyRr152uIsJBATSCEF4FV5D3YqzBrUP_AYu9IlViB17CMwgXthDGMFLmrcm_pFLJLzWs9LMXmsyXrRaGDvWAi3IyqfI1SIRqs0nh4Kur4l8Hmhracc_JWrkUBZdnHZvPJGKbMjQ0Sxdwsyy8hNXhedlLXleFiA6PQQYOu3LxBFzyH3Esl7AH5ZHtkf_0V6x7czcXMWdChuNTTvU6MnPrMZWqqrGtwbmFF29ynsXhaATfsvJ4zDLjQadiPRoMD5Zzebv1TXRwG93ITsPFVDUHoG7BC0Ci5-3cQxWjzp1FQUa2WrKgRH2Q5u-C2JfoJsNdQFF445RKCZCmpb2YMQZ9W6JfwFvygyGEZgtcqVW1xd9bymdBA6Lfxbd7A6dqkbLg_rHEhZd8BOly8L62TQI_Quo8J3gyGBtzFVp60k-LfvrOvy8-EX_TmxHBY318kjEwwGwcdI1tdZXNqr-jIl8scIbCDsNyew19JAuHLv91c6-9VJgtyo6wYRpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب‌وغریب میلاد کردمی بلاگر ایلامی از افتادنش از روی صخره بخاطر یک تبلیغ کلینیک.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26036" target="_blank">📅 01:29 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26034">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=Y86TcgNAS2PnlfSnb1q_3fvpZROm64sAEovLNlhXQiXRacFbph3hTeY9nKrANtKuSGTL56ieSXutV4jAVW2L_ilEa2uJNEZYZMOnl9tRTxzR6tZb0M5ylAcoBJOQU2-Preklvv5ra8nk3eUKSnmP9vQzirkrr2cDIb9-DFhYjtNNm5WmWlNYcj7ng93rFpsJ7484GQ4PiaDr037SxrAw8Rxgq1Lb9lHVQhjkENQwDOed8BW49azCXLZLmwS6OSECxyut0otXh5hkla-dcfxECG4h_hV6mjMcoGi86XalDacd4PzhGEshstAPkKs2IJ2daeQdahOZwkpqaMBijmMPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf49687f0b.mp4?token=Y86TcgNAS2PnlfSnb1q_3fvpZROm64sAEovLNlhXQiXRacFbph3hTeY9nKrANtKuSGTL56ieSXutV4jAVW2L_ilEa2uJNEZYZMOnl9tRTxzR6tZb0M5ylAcoBJOQU2-Preklvv5ra8nk3eUKSnmP9vQzirkrr2cDIb9-DFhYjtNNm5WmWlNYcj7ng93rFpsJ7484GQ4PiaDr037SxrAw8Rxgq1Lb9lHVQhjkENQwDOed8BW49azCXLZLmwS6OSECxyut0otXh5hkla-dcfxECG4h_hV6mjMcoGi86XalDacd4PzhGEshstAPkKs2IJ2daeQdahOZwkpqaMBijmMPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🎙
علاقه‌ شدید‌ جواد کاظمیان به مونیکا بلوچی ایتالیایی در گفتگو با ابوطالب: خیلی دوسش دارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26034" target="_blank">📅 01:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26033">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=eWv58FIeLWnzjSyglzWtf6h7QQVDZn3-EFyN1I-zRUyepWArCunCjs6R-ZE-wkrfzISF6ZezlMGTU0PWuJTibqN_r5klWLuPP7vX2ESgEDZCOBQTqypbTpN_QXLmpj5X7BuFqjomSAansr92qHs9ZOc9HcmtcFS01zHH-U6l5IMezx94VQTKwdT9PGwNW-CQKzJHWQ_C9mvt-oGCmS8qaV5cCzFEkLiU1WqR4bVHDW9Uu00PmkQqlMJ6LQXCAAyZ6xjNrxE0JwntFKYlAdKbAT1YXxYzB-m_8hqqC6XniLY2liBdu8uuT9jx0tP15F4_LKTnxiPpjqpW-6RFIeMBFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b649a7091.mp4?token=eWv58FIeLWnzjSyglzWtf6h7QQVDZn3-EFyN1I-zRUyepWArCunCjs6R-ZE-wkrfzISF6ZezlMGTU0PWuJTibqN_r5klWLuPP7vX2ESgEDZCOBQTqypbTpN_QXLmpj5X7BuFqjomSAansr92qHs9ZOc9HcmtcFS01zHH-U6l5IMezx94VQTKwdT9PGwNW-CQKzJHWQ_C9mvt-oGCmS8qaV5cCzFEkLiU1WqR4bVHDW9Uu00PmkQqlMJ6LQXCAAyZ6xjNrxE0JwntFKYlAdKbAT1YXxYzB-m_8hqqC6XniLY2liBdu8uuT9jx0tP15F4_LKTnxiPpjqpW-6RFIeMBFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی کنیم از دست دادن فرصت طلایی توسط گاوی؛
سه سال پیش شاهزاده اسپانیا لئونور ۱۷ ساله به بازیکن جوان‌تیم‌بارسلونا «گاوی» علاقه‌مند شد به طوری‌که همه عکس‌های گاوی رو داخل پیج اینستا و توییتر خودش پست‌کرد و ابراز علاقه نشون داد؛ بعد مدت‌ها به گاوی پیشنهادداد اما گاوی در کمال تعجب قبول نکرد و گفت تنها عشق فعلی من بازی فوتباله!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26033" target="_blank">📅 01:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26031">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpMRpIWfqACXoxcjP85hoNbG-3d5VzLS3FikOdm8adlgvbvPVgr2qDO6VJ3y4QIlG1GahJTSq8lioCAowcjGnFZPGmlmii4IIx3VTtDcZCAhMkNPD68-jep_RuUGOEQ8CeCX-x8Vyh6odFalmyOc7hl_htlQkHxqJFGNKZZmo2IFtzh_KmXcieaHMA_GYdk1S2EEh4_5igOs_G9x-OJdwOSBQ3ilpZSreNbnaZkwp0Maxm6EJuZYtiH9wY2aYKfEzYRe5GacR9Ys8Ha4P2V05sUs4j1BIiMUNpJbL7fndDfsGhTjWIOab_eNn6q4zSuOrmbrr1DfFilBxgabG2U4FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
🔴
#تکمیلی؛ رومانو: آلن هلیلوویچ هافبک هجومی 30 ساله کروات در آستانه امضای قرارداد با پرسپولیس قرار دارد و مذاکرات این باشگاه با او در حال نهایی شدنه. هلیلوویچ طی 63 بازی در فورتونا سیتارد آخرین تیم او 6 گل به ثمر رسانده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26031" target="_blank">📅 00:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26029">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=lRTc7nKd3MsmpEgZjK24ceYCdVGEinDGlMryd5e0gE4KHGylSZ_yiARJYFKDWfADXigREmUPHlXF1R9Gh_rFQ_a5s9F01ZEJldfTix98VxP7nHgbQTKj_DQNe7Mj35yVXggoHTj7QE2-USujmvBN669RoO9oQh9jdqga3i9XZctvexl_xiAgGEzt8xeWTQ3hI4fr9QF6VXmuDxs4t1LLOy0jS6EkpWKszDstqejRAKzDKJvecGv3LTxyxiKCObugix7YNRTHEl50A7xKOVN0MvF9Ewd9m134l2wsvIpWGHnghoFdKDouEn_lilW9Na5WoSrQf9h8GLNy5M3OwgRLvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/767b719cdd.mp4?token=lRTc7nKd3MsmpEgZjK24ceYCdVGEinDGlMryd5e0gE4KHGylSZ_yiARJYFKDWfADXigREmUPHlXF1R9Gh_rFQ_a5s9F01ZEJldfTix98VxP7nHgbQTKj_DQNe7Mj35yVXggoHTj7QE2-USujmvBN669RoO9oQh9jdqga3i9XZctvexl_xiAgGEzt8xeWTQ3hI4fr9QF6VXmuDxs4t1LLOy0jS6EkpWKszDstqejRAKzDKJvecGv3LTxyxiKCObugix7YNRTHEl50A7xKOVN0MvF9Ewd9m134l2wsvIpWGHnghoFdKDouEn_lilW9Na5WoSrQf9h8GLNy5M3OwgRLvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
خاطره علی کریمی هافبک ملی پوش سابق استقلال از اسپانیایی صحبت کردن میلاد محمدی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26029" target="_blank">📅 00:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26028">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxWtdYAK4XR3L_fxheBjj_TeTwjkuKZtHyjedBlnO4N78b6IgyBw2KBH5MWNePqsdJumm3Ff2Jipz4GiW75rR5afGRoPfos2NaqFid9ONyvtYomFtZ93GWsoB9lPWFgbEuBgE-ubvVI-bkwJULM4LXCD75MY9WSYesnmw3gLyCY6gvCLvBKFDGEVWGYkyeRX-D3gAygJnalFlqrPRmxih2YgSX3GwzDF5txmUukhCdF1o_AxecaCa5Ky-5kVqYANLVMgnv4RT2uXIBSMkqVay6d2V7P8FHsjzQMI9HgeOFcy--r7IbF8STokQ7XzxXm92ZDRBenu-fgx_aPMKnb7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌دیدارهای‌امروز؛
کمتر از 22 ساعت تا نبرد تمام‌ عیار آرژانیتن
🆚
اسپانیا در فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26028" target="_blank">📅 00:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26026">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vamB4S3d9JLNAxp2AF_IXaB78uv3Ko-WpLt7QFP53xOwwQTsnzR50ux88hPRGRJhdbtx8_7JWjQECCTlQhw87HqAWDCrWaZU56K2cKkp34JqzuctUej5VPNZjQNH5N63WWRO8Qbt_IikTBUttHssmHMmTd2xatd8o1jPekJcdP56QP5kJxNni0Bi8FU6F79D2MUAd4ceepOT4trBr419LbK9_qKZ8eB5RiKHubJL7zGTwBuaccLuHsChUouP0hIPg4WhRPPbqAuXZvxgIAiPHL4MTYWoxU_5tbMMswWFgjqJZC6L2S8OKAkiipFR-0mmOu_AoXJhSlJpZTxi6Wa-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26026" target="_blank">📅 00:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26025">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9vnnDwT2_UMSrIdzxClK9z1H4p2iq69suwU8rPY3i-YmhcnU5yGfxCQbOgF0-g7nE-8JbIreUz_ZWjviVw1PM9dw9UVdin8HGxEYxgSThROyNT-UeK-EPnTRhhmqtw0wAuJbC4dkRB_T8FkPNLdBlqwI_wg4mRSEJ7SDN811aGaqarD8xEkPgdBAigbJ4fYuwrvL8LGHCLLX3Iaot-KprU1rz83fZ1evs3CIyy5qnaAR4NiuBJVULDbwdb_KZ37VFduDsFCJtKZjGIYQa0eTIDS6eCMEgzDk-VWPatnQ-NiS0qrXJ0JYchcCbJYEQCsBBZoZsFZD_0lMesMvkUcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال موافقت کامل خود را با افزایش 300 هزار دلاری رقم‌قرارداد یاسر آسانی اعلام کرده و به مدیر برنامه های این بازیکن گفته که یاسر آسانی به ایران برگردد قراردادش رو سه ساله تمدید خواهیم کرد و پیش پرداختی یک میلیون دلار به…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26025" target="_blank">📅 00:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26024">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=g3jbpR1VcFEBdTg6QP5QWlJ1LkC5HhoKwnz6Uu_t7lJuWXwVpCo8C67dUWe5aJmQ5lY2f3Cl1VtzHdBDi2P-JQdFml8fgZWAbc-tlui_marpVDilH0EFBWe_91SSU75JK1JPx3s42HMv5zMlHHv2WMl3jaBYpd-WKF_X8612oc5u6YaWLomkut8T2kkIXgjM86HOGr5iPRtXRig-eUWWzz4GDESkkNgHgD0PVlhVIJabbMohGgk1rOvtl3XS6VLuV81o2izI4Xz6Qs0mVj_mbBwEr73rjyT_oauS4Pt82X9x_h1eY0YiWlVkLo6Z0Zr2yMLcsCWvrOfcU46Y3enrgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ae80f717c.mp4?token=g3jbpR1VcFEBdTg6QP5QWlJ1LkC5HhoKwnz6Uu_t7lJuWXwVpCo8C67dUWe5aJmQ5lY2f3Cl1VtzHdBDi2P-JQdFml8fgZWAbc-tlui_marpVDilH0EFBWe_91SSU75JK1JPx3s42HMv5zMlHHv2WMl3jaBYpd-WKF_X8612oc5u6YaWLomkut8T2kkIXgjM86HOGr5iPRtXRig-eUWWzz4GDESkkNgHgD0PVlhVIJabbMohGgk1rOvtl3XS6VLuV81o2izI4Xz6Qs0mVj_mbBwEr73rjyT_oauS4Pt82X9x_h1eY0YiWlVkLo6Z0Zr2yMLcsCWvrOfcU46Y3enrgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابوطالب‌حسینی امشب دربرنامه‌اش و در گفتگو باجوادکاظمیان ازجدایی‌اش از اکیپ عادل فردوسی پور خبر داد و گفت جدایی ما کاملا دوستانه بوده و ممکنه بزودی به اکیپ ایشون در پلتفرم ۳۶۰ برگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26024" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26023">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=V94QyJT4Aaq8k50yd9qeP08Ef2uVDxLBav5btP4D51ro7Sb3QlsDGSRjK_V1rEKD8qw6ch1sU5iYKHIncOobbSADEOValxo9Opl5gPv-AoFsGPq8VXD7o7wrBkEdiBCHDamlcr4yhXSN9SDRYwhhpwhaL5lpe4jqcE9v264YhfA3m2xmkgKXtaiBnfeBiphbcUj5q7ma254A-9ACHFWEnvgQlihYoKYkdMGSN1rxk-g1vTk-Ldp1RKTuTayLQQCY6UpKadw5gd4wAxwT9ZvKHcxP007O68ewF9BXn3XMHRJgzZ4-nItMRjzDn-e-VW9c1jp9iOaAo0R8D3FSBKipGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69396b76bf.mp4?token=V94QyJT4Aaq8k50yd9qeP08Ef2uVDxLBav5btP4D51ro7Sb3QlsDGSRjK_V1rEKD8qw6ch1sU5iYKHIncOobbSADEOValxo9Opl5gPv-AoFsGPq8VXD7o7wrBkEdiBCHDamlcr4yhXSN9SDRYwhhpwhaL5lpe4jqcE9v264YhfA3m2xmkgKXtaiBnfeBiphbcUj5q7ma254A-9ACHFWEnvgQlihYoKYkdMGSN1rxk-g1vTk-Ldp1RKTuTayLQQCY6UpKadw5gd4wAxwT9ZvKHcxP007O68ewF9BXn3XMHRJgzZ4-nItMRjzDn-e-VW9c1jp9iOaAo0R8D3FSBKipGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب‌شروع‌شد؛ جواد کاظمیان با انتشار این استوری و تگ کردن مونیکا بلوچی تولد او رو تبریک گفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26023" target="_blank">📅 23:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26022">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCVwT8AZleFxUck7FSgxe_z15YXOw_AmQ0Q6Y0wJ7bvD-1JbvJrWjmYKXkaEEImJ8QTh6XLiFADYUH6jzVsHNjyGAgD1c3N4pXIz-y0ZigryPJTKmgpdtnFwef0vHHJ1cj7VWtQScilVGxJKqRH3p-YRB4UUwVY6ri1MtMxHr1bJtRROR1NWfBiG1HbdfeUJL40b-5CsuNRl7GCCNihVPEmkVO4KvQbZ3zSrrLvK7zRMCmyrZnqtEG7O4F50zNYmxRgEJ3AuuwSRPTTiaTKa9prHGSIj0eplrvNpnBuliSXo66Cs5_WL-ViS5qhJDKVeBWIuCb5PBGI55jxudWVaLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🏆
باشگاه اتلتیکومادریداسپانیا برای دومین بار متوالی بیشترین‌تعدادنماینده را در فینال جام جهانی دارد: فینال‌سال2018: 4 بازیکن؛ فینال سال 2022: 4 بازیکن؛ فینال سال 2026: 9 بازیکن
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26022" target="_blank">📅 23:30 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
