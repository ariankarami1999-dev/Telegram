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
<img src="https://cdn5.telesco.pe/file/NPgNU6Upn7n_QkiwczOxy6nsArHPrZjdfeAj97nBBnnxr1yw0fEZ6LDS2Ah_NaP-gWEFHYNpvTi-497vBifLfy_CyjZTXEfNobQ-tIgZjONrcGCba0g-1sDUc9YmsarFiGHM9-6S656QuvGc_G1stUEGZ4VLL9K--4wFBELcGmbliQorYTsYH7i1u-o5L3KWZmHl5pEAseUphXqCqqYTz8iiZgY-rkILNk9UU0-bb8dosRB5qKBf0dThdJfegHluIZ6-TwtoaBjiErPpd498FuiSUFkAYbBlLMfet1MZIzoeQcLjEfqSVwtPXXSqfqVBq4qHKP-MzqWup6BtWkm23Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 382K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-108710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWoKYVXKlgWduXO5hCsq-Q5JcREaRl1tDdBGesSr7XqdhuP8MHVcGcgggtqRuMoTJwINn_SBRGwrITqttauPZctsESTp05LrGq62Oag_JqoQF9h_KlmShAmTsqIyDhG8FVT00OjQ7KUivXSFrtlIy7rPQve1sCD6B5P1aPSP2Y_dz7GdxL4uFbu23ZBdixiFtDvW06HA4qyCHFffdnLcVgm6asyz8voDKT75ot4oBivF3S6fkPTxvSXmJBWGLkvqjS3SSyt56N7fs-L4DjVTSadZPYVckGmOe_UkdYM5ep5BmuDxFVRaj_zWfeh8UfyOLbESIAHATTKinUrXrYbSQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
🇪🇸
وینیسیوس مقابل بارسلونا:
- ۲۴ بازی | ۸ گل و ۷ پاس گل
- ۱۱ برد | ۱ مساوی | ۱۲ باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/Futball180TV/108710" target="_blank">📅 21:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🇪🇸
#رسمییییی؛ وینیسیوس جونیور بدلیل تخلف در بازی با ویارئال ۴ بازی از همراهی رئال محروم و الکلاسیکو را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/108709" target="_blank">📅 21:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108707">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqlUeK6XM7TdPFZoYG8fKZEcAN_8HROqc1hFaYcVkwiu3FSaFxi1lLDfHG9_JXt34VO9it4uRGADtru62XEU8Mv_cnABsUkaq6FeTOJB-oarKVxbysBXKTkM3sH0d07goLmw4e6V_msHDOV0xx-jMqXficzOXTWQSGtjfUIhusExQo-3NC-JKglaDcoF3_PG9o0GSZbKqJMZUDd4u71Ha_iyzCrUaV3lY6mTSQwRZI5m6SR0wCMKzBJlYbWPDsT6t5csOWdQlAoh7I-2sII6xl8kXSraWSzZ9DY9GEN8ruXgPhSkzTH2Hz_FBUzm3_UTNZqrt8zVltx6zWI15dwCPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇺
🇫🇷
ترکیب منچسترسیتی و PSG
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/108707" target="_blank">📅 21:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108706">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5I1dZ4-o31T_laqUNI8SYLopIG49Chgu1Uyt-B6lsbXEn7z0nTBmoFaS48ZSgPTIqcJDT3xlhaQpobSkq6-0Ek7EY5Ys-Gtqy7inVm0skLeFKAayC6FHNebEIbxePpj5015KzvCO2w46MQ5gdVmNrCbWfAhvBMvhXn9kPXw2S6tm288itl_hNuXp-8kRv-M5dj9ODt67UuMYXddP5Rm5T8IRm5-rS13pwRV9gG9XjlInGyvBgHodpHEgFQjZYXJx4vZgq4EZDIrbg_zq9mKoC82B4gbmNKS-k766bBGL2DOdBegExhzv2IP6a1tkXIrcdABBope_4Ija9dfjuRF2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇪🇸
🇮🇹
ترکیب رئال‌مادرید و آاس‌رم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/108706" target="_blank">📅 21:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108705">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6fa60164c.mp4?token=uuVph59IYKRS74D2Ez5RRjlgYumZzo6lwMFk-1Pc_RVwbbCYa-lfnwBOF894WVwCId5oaQE-7JBN2q42WNOKK7HiDgIPhm9lo_Wab56tVubntfu9q_d2Z46gbRingRUc_6xoDHRZ1pgjSQsrY71GTIApDT1wW2Bi9hxrCXLbBtkbuctomR_RtzeApgpiIR4NnR8ynElfhtuEo2hEqOso_DA50YF03EjiVP_3t-RjCivzI5uUOUjZQM2gTwoyfmMxiS86NFnxJfc4fMirRKK_TAACxQYXXbAdBtTPee8Wsm8z-I2jEP8xUV0hf9kJqEarlRwUMQknTQ2ONUV-J90FRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6fa60164c.mp4?token=uuVph59IYKRS74D2Ez5RRjlgYumZzo6lwMFk-1Pc_RVwbbCYa-lfnwBOF894WVwCId5oaQE-7JBN2q42WNOKK7HiDgIPhm9lo_Wab56tVubntfu9q_d2Z46gbRingRUc_6xoDHRZ1pgjSQsrY71GTIApDT1wW2Bi9hxrCXLbBtkbuctomR_RtzeApgpiIR4NnR8ynElfhtuEo2hEqOso_DA50YF03EjiVP_3t-RjCivzI5uUOUjZQM2gTwoyfmMxiS86NFnxJfc4fMirRKK_TAACxQYXXbAdBtTPee8Wsm8z-I2jEP8xUV0hf9kJqEarlRwUMQknTQ2ONUV-J90FRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بطری‌باران سردار آزمون توسط هواداران الاتحاد پس از گلزنی دیشب مقابل این‌تیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/108705" target="_blank">📅 21:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108704">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX_aJY70fvX1CqVAzjJef0Ob9CE4I-6RE_90qgzNhLl6voChow6Q1Y6g__AXyyP5V3ThY7JadDGwMXIG9s7ihHkr4iEb8YUGlp4Q50kUDTKjmv_BLm3cxXQVtvsmA_njcrwLruCUo1YZgwftYIg3EfIGs5d6fIp5_wRlK0Cl6TmoUp1_3I1uE2HnN-_thyRdkPa3Zlflo27spTT21xLIHAG8W5VyoKr15_hCJKJ_CYW7YyXO_DvXaBT4VNMygud4WgZI_Zh8t3l-K5KJmBW8JAcnPoqsJoQjypAAS6vAR5vB3W1_AzUub2KlK5SMbZLSv1sRSdS_6SYfN3Knn0rciw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#رسمییییی
؛ وینیسیوس جونیور بدلیل تخلف در بازی با ویارئال ۴ بازی از همراهی رئال محروم و الکلاسیکو را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/Futball180TV/108704" target="_blank">📅 20:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108703">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6d0eadf8.mp4?token=I8bqKBmJmbM9AIxM2NwUOUgorvayI1SpzuJw2MQ_usKBmrOZK7v5QSLvoAl30NcdvWjnCra7cdK8rwtC4YJdFvJHEHBocMos9SYajK8DMJPDth4H6oyXN8Ls5eh0vN3KEkIb2F1ifRjYeLPfwfpIHJYa-mJbcejgkrAuwny_R9oHc4fPewdJ4aZjuP45ydoIuAla40CEtjvUunhL6tyZyZoMQXGzjlalW4CRjMTLqeOUC1HPV5qXcAvUUms7jQ3VgV_hC7Lvu3jfyjb3qqkhU6QytrFEBUTKaVJKLtEVp-aMSALjk0vfiUf3OjPhLLKCR3k7rEUPQx0cA4bzy5pRNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6d0eadf8.mp4?token=I8bqKBmJmbM9AIxM2NwUOUgorvayI1SpzuJw2MQ_usKBmrOZK7v5QSLvoAl30NcdvWjnCra7cdK8rwtC4YJdFvJHEHBocMos9SYajK8DMJPDth4H6oyXN8Ls5eh0vN3KEkIb2F1ifRjYeLPfwfpIHJYa-mJbcejgkrAuwny_R9oHc4fPewdJ4aZjuP45ydoIuAla40CEtjvUunhL6tyZyZoMQXGzjlalW4CRjMTLqeOUC1HPV5qXcAvUUms7jQ3VgV_hC7Lvu3jfyjb3qqkhU6QytrFEBUTKaVJKLtEVp-aMSALjk0vfiUf3OjPhLLKCR3k7rEUPQx0cA4bzy5pRNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گل اول المحرق بحرین به گل گهر ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/Futball180TV/108703" target="_blank">📅 20:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108702">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c81f4ea6e9.mp4?token=sZz66SLzHtc25nc13Nu-w57oRtYWthYIQVhxrO8gL0iOfQqHRVbzGM82DXIl3lF1D2QAGLq-TbMDfX0KwDv5c-_NNRSI-v8iXEwcEl2y2rRlp4XoPiTD_3x3pb6FzVaITXqh0gFL81RMgxmZQv1u8_zGGXbgfpovNLM9CTLYJB4CJv3Z2YEIiDVsyVjX3XNtqjhfFG-CmNfReWGdujuSSFcxSj5Tb6JElBmlxdyqwLRBSI5M9rbUUv3NJRTcZlfCIdSmt0Okil_5bG61AsT7uAr5BxW4rnUgpHXIwCOa0NbRDvAB4LYkiR_cRhokKIDyxpS8-xX1OKwR3Fgyh7qY6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c81f4ea6e9.mp4?token=sZz66SLzHtc25nc13Nu-w57oRtYWthYIQVhxrO8gL0iOfQqHRVbzGM82DXIl3lF1D2QAGLq-TbMDfX0KwDv5c-_NNRSI-v8iXEwcEl2y2rRlp4XoPiTD_3x3pb6FzVaITXqh0gFL81RMgxmZQv1u8_zGGXbgfpovNLM9CTLYJB4CJv3Z2YEIiDVsyVjX3XNtqjhfFG-CmNfReWGdujuSSFcxSj5Tb6JElBmlxdyqwLRBSI5M9rbUUv3NJRTcZlfCIdSmt0Okil_5bG61AsT7uAr5BxW4rnUgpHXIwCOa0NbRDvAB4LYkiR_cRhokKIDyxpS8-xX1OKwR3Fgyh7qY6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🚨
باشگاه خیبر با انتشار این ویدیو نوشت: نمایی دیگر از خطای واضح روی مسعود محبی در محوطه جریمه پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/Futball180TV/108702" target="_blank">📅 20:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108701">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1370be90f0.mp4?token=Ma94F96n1dYJPTh7twfbq52YKaEEt3nwfZhDRiSfokL0sfvDY9BFRAL5BJjhGUqxZKy3xQoEFIEkqmCVC7LXfSDvIL-cgYoV1LDKRg69Lqx_B2EBjZGQYr2A3xgwo7ncg-1WwFm-cMTq-Y-3I1Ht0DQDrClo0c6OBnYdwg6fA3mPiGnnIaX364abUKPZHqJIurShggE7ww-8XEuChRwTPDrltauhfMcu4PkfzaK0F3XfuX7NGm9HEmgXcDdKLmbzFsZes1A5BhGi61NtspLZ8g2DdMhXh3_mJf7jdIy4mn7jL5Myev74SrWa5c4q20aNeD84FENePWHMl6SnbjIe0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1370be90f0.mp4?token=Ma94F96n1dYJPTh7twfbq52YKaEEt3nwfZhDRiSfokL0sfvDY9BFRAL5BJjhGUqxZKy3xQoEFIEkqmCVC7LXfSDvIL-cgYoV1LDKRg69Lqx_B2EBjZGQYr2A3xgwo7ncg-1WwFm-cMTq-Y-3I1Ht0DQDrClo0c6OBnYdwg6fA3mPiGnnIaX364abUKPZHqJIurShggE7ww-8XEuChRwTPDrltauhfMcu4PkfzaK0F3XfuX7NGm9HEmgXcDdKLmbzFsZes1A5BhGi61NtspLZ8g2DdMhXh3_mJf7jdIy4mn7jL5Myev74SrWa5c4q20aNeD84FENePWHMl6SnbjIe0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
برخورد زشت امیرمحمود داودی‌نژاد، روابط عمومی هیئت فوتبال لرستان با خبرنگاران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/Futball180TV/108701" target="_blank">📅 20:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108700">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">❤️
محسن خلیلی مدیر پرسپولیس: بیفوما در بازی امروز بدشانس بود/ بیژن حیدری بهترین داور ایران است و در مورد پنالتی باید دوباره صحنه را ببینیم
.
شکایت استقلال از دوپینگ بیفوما؟ اگر مشکل داشت امروز بازی نمی‌کرد؛ مس شهربابک باید هتل ما را فراهم کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/Futball180TV/108700" target="_blank">📅 20:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNRnhMyjuqC7FSrai8kOi0NfwfKPmTQ52GL6YlGewazPBOhNhpYiRE4tOmUCbYg-OMj9QiA7Uh8HqNNVYtQIv4zKBmtUz-8p_P96UZ3INLgGXxhfxHFqAmopye-_w_4s6vfKhfhT9dZmaSA_oH875ORQdUCo6tGQIF3Uougcy4pG8Wr02kj0W3tK8UQ8860cozpgN6KY0L5T7bECAdUARhKHahXVScm3Wc7BoaWfXK5dlLwCSf51dboX5AK1-HJRawjqsh5UPvUsgP_WCAbLrwggxFCnGAwN23UyJqEGPYiVcMmGMxv1eH0faQM395HA3ot87Fbfgl3d7byQytyqZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معوقه‌هفته‌هفتم لیگ‌برتر؛ تساوی بد موقع سرخپوشان در نبرد سنگین با خیبر؛ دیناروند ناجی تیم کمالوند شد
🇮🇷
پرسپولیس
0️⃣
-
0️⃣
خیبرخرم‌آباد
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108699" target="_blank">📅 19:08 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108698">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vNMuQBYLPTX_Tqrpbgru52dHZ-MPS-KrAo0wAvj__8_ynvW1TpcURd50LmkwwOotg0xOSoPZKT5RDzTSMhHhDQ3QMMhESMxtaNvMayWyqJjm7K-Lhf_jQzTvAJ27_DwSlUXMbXhuFotonP92kX8X71cGP4eRDLbyyzRS0ITE0Ra3Ptas9QicTz9VRGIrwW3yCAzuARqNoKbrVyUehHXihlvKDIcYd_96DF-gy7eQe21IianILtczJg9tXU-AwPnA3RFh1Ez7bgiQ76FXt2e0FAc0akQvaz1h98d5BcEaI_svsLmwevP8bEZ5bqZTxr417yMyLAfkTsmV_1gORGAY6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
معوقه‌هفته‌هفتم لیگ‌برتر؛ تساوی بد موقع سرخپوشان در نبرد سنگین با خیبر؛ دیناروند ناجی تیم کمالوند شد
🇮🇷
پرسپولیس
0️⃣
-
0️⃣
خیبرخرم‌آباد
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/108698" target="_blank">📅 19:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108697">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TB7b3nMnOheDhcky5K9No67oEOIcQteG1RwjaTK-LyrAOrcQMzY0VX4p2B5jYb1wkvq6Fxbli2AywMchjdqYQ1srkE1iLIN2KY1rGeIjEo9mo1YCPuY7gO3qvxh47GmALxoEDLiBizB7i5v15sCex_3ac6ylt3PBiAhzDKIaSvUajvFclbw5sAib5wNjKtEwR1jzuud0Q83LhC-z1g08wCLZ7Em21M0tWVqbrCvv-F9B0nGHekJ14lvfbiO_EOPXwnipvzEFtQkn_ohsZw7EYlL65pxf-kDQvaPEvu1048Y4kdHd7MKAewENG6XL6ZEeYXNfxJsow8hu4ya7K_nWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇹
ترکیب لیورپول مقابل لاسک‌اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/108697" target="_blank">📅 19:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fd1c54704.mp4?token=H2ni8-SZNwgd6vjNAcxFPdMsI60ab26Z7xRsw0aypQLpoE8c4egUbA6iMD5p-mPCb3mcNXSdMDDCmx48tuTfKdLhO11r-bYaTNYE7jXnrGqLYmi2IkYWfL3zEUfQLbLlarSyqAIvVmQ3wMP2wI26c-_PX8SVj9sgeZ8WDwA7wAQifWJT8sM8ChsvrZ7d6WLvFvryqHqyLPiAmiOdp7U8gXipIHm01Nz8m1cf_jFfh-vApI0f17IMAEMLQ0_d3nJqcg17rQmH0TEiLqpXw3-DOGm0u2YIqYG0SPwKwxJQqwqawCQLS4k-ivX4fUK0o_nQmxYOhiL4n_4cvJ4oS1CipA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fd1c54704.mp4?token=H2ni8-SZNwgd6vjNAcxFPdMsI60ab26Z7xRsw0aypQLpoE8c4egUbA6iMD5p-mPCb3mcNXSdMDDCmx48tuTfKdLhO11r-bYaTNYE7jXnrGqLYmi2IkYWfL3zEUfQLbLlarSyqAIvVmQ3wMP2wI26c-_PX8SVj9sgeZ8WDwA7wAQifWJT8sM8ChsvrZ7d6WLvFvryqHqyLPiAmiOdp7U8gXipIHm01Nz8m1cf_jFfh-vApI0f17IMAEMLQ0_d3nJqcg17rQmH0TEiLqpXw3-DOGm0u2YIqYG0SPwKwxJQqwqawCQLS4k-ivX4fUK0o_nQmxYOhiL4n_4cvJ4oS1CipA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🙂
عباس قانع گزارشگر دیدار خیبر - پرسپولیس در واکنش به موقعیت‌سوزی تیوی بیفوما: تیوی بیفوما کاری کرد که شاید خیلی از هواداران پرسپولیس تی وی را خاموش کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/108696" target="_blank">📅 18:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF-EXXjkKMatzKKZ8yisscKvOziSDEKWMb7e-EzKACLK-1mXHi-S4OkaFIBMaHESFQPTLzZTKmhyQ7-f6ij7sU0jQnXYxoPdGUNHgwurS-i5Q3H9eBV7pZaqqnyNPpRlsi09eR6vtoEnLV_COrY6CbdEJABNsXK2c6T_jCiM5pD3Z0jNUdSMCXwwOGbwe6NGWtqwz7aZt4lWY2FtKygZe7WFR1FLE-aXfGz6rARsDcx1aT4LXYgNb1AISkeR7OPQFo6NJZeMaGpcAprEiNREdVSH-yz0HRz_6UpeFwAUv5kYZ5GfVi-QHCgOhbaWJcT10WFyu9OAcK6QxzQDVHVL6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب گل گهر برای دیدار با المحرق بحرین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108695" target="_blank">📅 18:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108694">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38ff4c42d8.mp4?token=CCfV06R-5ZWBY3xsNLvzd7PfrXEF8ujGxk4cbiZgDGcKEj8UuPr3eConD07I5428TSbK2f51U2xlMvgtzMIMQ2Ju2hB8xqct8uLnPAlm1HuPhxraUDuXENIqBJE9K505znhPiamSN-B6OHOPd7SJVqJs_E072qpp0WpGeu4o6cTaJddhCrhj7htqhv5c7SxM4UmJXnINgDVd6ylB9ipStbZZYEBxzAFNIiucArCZDmQjHeBrigmGlZgMHmqb8MRLo641Br0C6hftMXy-6sF0LFQGf8DpR2XyQXgWT1ZAWdnUdJP4i1WzB0lKVR4pD68qFG_Gc4jtQzBUtUCrxixbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38ff4c42d8.mp4?token=CCfV06R-5ZWBY3xsNLvzd7PfrXEF8ujGxk4cbiZgDGcKEj8UuPr3eConD07I5428TSbK2f51U2xlMvgtzMIMQ2Ju2hB8xqct8uLnPAlm1HuPhxraUDuXENIqBJE9K505znhPiamSN-B6OHOPd7SJVqJs_E072qpp0WpGeu4o6cTaJddhCrhj7htqhv5c7SxM4UmJXnINgDVd6ylB9ipStbZZYEBxzAFNIiucArCZDmQjHeBrigmGlZgMHmqb8MRLo641Br0C6hftMXy-6sF0LFQGf8DpR2XyQXgWT1ZAWdnUdJP4i1WzB0lKVR4pD68qFG_Gc4jtQzBUtUCrxixbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرصت سوزی محض بیفوما با وجود دروازه خالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/108694" target="_blank">📅 18:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108693">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0b102f02.mp4?token=krMiUYvHSWBuqz-jOH7_LRGdoat0yagVS8J0RTyJpmMc6ET6JdQ_3EIN0qF51Xv-ZhrqinK_zew4K0yIuLeSDoIs9u9JUrDEQwW-igAWkd5YobBD4BR1siHIkUlIs7t3YVk4ZpbYePyZ5n-3Yzk4xQSzz9VFdugt-E3DEqKJol3zN-DAD3kzeYf-viYfbWTBnZKsPvl5evmQnMvIvV1Dz7jtnRH1hHErswnJYT1EU83QHrlaD73PNRFLbgMJ_N9QywS7bBXI4s-RzQumQBAlPYg8Q3KYW-ktEkfZMhonfwLLIwU7sHdeBzYTdTO5nvhtUpeb-6Gcc0dn7korLnK3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0b102f02.mp4?token=krMiUYvHSWBuqz-jOH7_LRGdoat0yagVS8J0RTyJpmMc6ET6JdQ_3EIN0qF51Xv-ZhrqinK_zew4K0yIuLeSDoIs9u9JUrDEQwW-igAWkd5YobBD4BR1siHIkUlIs7t3YVk4ZpbYePyZ5n-3Yzk4xQSzz9VFdugt-E3DEqKJol3zN-DAD3kzeYf-viYfbWTBnZKsPvl5evmQnMvIvV1Dz7jtnRH1hHErswnJYT1EU83QHrlaD73PNRFLbgMJ_N9QywS7bBXI4s-RzQumQBAlPYg8Q3KYW-ktEkfZMhonfwLLIwU7sHdeBzYTdTO5nvhtUpeb-6Gcc0dn7korLnK3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
فرصت‌سوزی تک‌به‌تک عجیب محبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/108693" target="_blank">📅 18:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108692">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575fb08f89.mp4?token=roV7Bqj13x_pt-hA611eQB3r3Z3Aa_ciQ3xR5Plhs9-Ce1HYfMjaPnUk7J1FJ-wVe1F0HqpaVQev39HcZgkrq3yTgGT5_ylh-fV4z7JNmiE48XMznDO2aaFlnEPpOdtIIRNYCNMqAzzgTIq5sgjoXiWnXk-gNaILNgNWmFZWCAlKt_RF3a9CRfeyR0nEGnCiUH8S_NgANGLQi5ee6oSurpzDeL5rmYaBgM0R6qZBqMK9zFddh8q7ADYwsPSo5167ClmekI3iO3FhEoVMGER-u9_jgaIw8SewtRuRqaHL-zpX4FDe19upo1IpuMnZo6aCjDKYR8YnCFg_zmw0ut8s5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575fb08f89.mp4?token=roV7Bqj13x_pt-hA611eQB3r3Z3Aa_ciQ3xR5Plhs9-Ce1HYfMjaPnUk7J1FJ-wVe1F0HqpaVQev39HcZgkrq3yTgGT5_ylh-fV4z7JNmiE48XMznDO2aaFlnEPpOdtIIRNYCNMqAzzgTIq5sgjoXiWnXk-gNaILNgNWmFZWCAlKt_RF3a9CRfeyR0nEGnCiUH8S_NgANGLQi5ee6oSurpzDeL5rmYaBgM0R6qZBqMK9zFddh8q7ADYwsPSo5167ClmekI3iO3FhEoVMGER-u9_jgaIw8SewtRuRqaHL-zpX4FDe19upo1IpuMnZo6aCjDKYR8YnCFg_zmw0ut8s5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ماریو لمینا قبل از بازی: یامال کیه؟ من سانه رو می‌شناسم ولی یامال رو نه!
🙄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/108692" target="_blank">📅 18:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108691">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108691" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/Futball180TV/108691" target="_blank">📅 18:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108690">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfeJra8PxFbTSkMqR_ZOzk4U9eT9U8FBkWPXBlHbuwCvd3Snxm_Y86H00gv-ecqScx6mnedTh9w2I4wPb4R-2GZvgYquMBSYzXgOpdYRudZF2-yqkxyrKJE9kZe-BTRihh4pyOvUPta0zNbkvfDVB3u9uaNz0mG2WoBKMPjRkd7AkWNjiTod_1hdAPHJpo8XDtwlzZCRw9l4nQj94jbsBHzqADVMAvsjT2uOYJPd9QZtc7FfA0rO2kLmqLrLQ_VVcWcIVFKzdFuVlykQ3Go-89-fCkgrw4N9eD_2nfCN3udMqyYKP4luiQdATAyF_CcQrc2CZkDVTMygav1jySJPzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئال مادرید
🆚
آاس رم
🦖
این نبرد حساس چمپیونزلیگ را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۲ تیم در ۵ بازی اخیر:
رئال مادرید: ۴ برد، ۱ شکست و ۱۱ گل زده
آاس رم: ۲ برد، ۳ تساوی و ۷ گل زده
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
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/Futball180TV/108690" target="_blank">📅 18:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108689">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">❌
لحظات بررسی صحنه پنالتی رد شده پرسپولیس توسط بیژن‌حیدری و اتاق وار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/108689" target="_blank">📅 18:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108688">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_UAJV6X1BRbgqJ0UI-PUSkAP8l-e2LfROA_CdQE5bsOWJ1q_4rw7guS9imwwIkva_tKCSH-TIXuDYZZV9imv3n9DNncIXCJWLWZiPtm6IOSvQot8W1LRLd7AudR7fYy4HACvcyvq1IHfFwre3fh_1IMKu9X5ZypAXkzusIAVED7s2N90Naoi2oZLploimm0Eyfpn-tq7j3ceSDE3XBV0hvGkdbFmel3E7pdjvbWZW00t86TRiCK7nPAthzNd5aFwg5oYuQ6i_z5LWdEoXkzjZ-ZkH2fvpK0EeiZxUweEcQBflPyQSh4ua6d0mrq4foUzFDSFUS5iPFsIzLKzW2uqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇩🇪
شفق قطبی، آسمان بالای استادیوم تیم بؤدو گلیمت را قبل از بازی آن‌ها در لیگ قهرمانان اروپا با تیم بوروسیا دورتموند روشن کرد.
🌌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108688" target="_blank">📅 18:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108687">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">❌
لحظات بررسی صحنه پنالتی رد شده پرسپولیس توسط بیژن‌حیدری و اتاق وار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108687" target="_blank">📅 17:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108686">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
پنالتی پرسپولیس رد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108686" target="_blank">📅 17:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108685">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🇮🇷
صحنه پنالتی پرسپولیس روی اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108685" target="_blank">📅 17:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108684">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=naEDxlLzvDuAsB6wAII3fAIk6SsfacqzRIKCaq05FoS3TDO9klGQhb9I0I8fbCU-plmbNeu7Yx14vlxjz4VeTeCzaitd0OP4_sDb2ghsnpQfO59roXPABfCIoBrJE-vrEV9eDWsdkj7Y9tmSieppby6uqIm9OcMSR86xvrvipP-jV-yDwKWcBGE99z5EPsR2hdKrbezqjt0fFUFCvEEAao_qNrMy3oSCW6_a_J8aRJRLo8zXH_oHKM5iqqnEyTD92eQb5BLoJ4z-Dm_wXA5fy9zpqueSd_Ny-RMhBoXhfQlcm4aezFshGLT0c5mLWLPGemxWFB-cX_6kHlqmfurDpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab522e8e81.mp4?token=naEDxlLzvDuAsB6wAII3fAIk6SsfacqzRIKCaq05FoS3TDO9klGQhb9I0I8fbCU-plmbNeu7Yx14vlxjz4VeTeCzaitd0OP4_sDb2ghsnpQfO59roXPABfCIoBrJE-vrEV9eDWsdkj7Y9tmSieppby6uqIm9OcMSR86xvrvipP-jV-yDwKWcBGE99z5EPsR2hdKrbezqjt0fFUFCvEEAao_qNrMy3oSCW6_a_J8aRJRLo8zXH_oHKM5iqqnEyTD92eQb5BLoJ4z-Dm_wXA5fy9zpqueSd_Ny-RMhBoXhfQlcm4aezFshGLT0c5mLWLPGemxWFB-cX_6kHlqmfurDpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
صحنه پنالتی پرسپولیس روی اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108684" target="_blank">📅 17:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108683">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79edc7079.mp4?token=TPlozajcRauM2-YO4jhGyF_TiTMU7i3HUuj5OVyMo_5JANDJoWMtPQEbHQYCCge_Qo84F3NaYwKe84yQhihrvQdNqJuFizZiQWvvLKp9FMa6BdoSbm6AXPi_0gWOZg0nr4nHEcYcoIBGr2qwGYRgaMuPjVooA67wXNPYCWvpRHY3b2ohr0S14Q5G83hFiay-y_nCgSKLd9LobaeNCU1ohWluyVU9uDi6TyFXEZkKUJT2weJa9yl9hVv9MXURblrIJ9wLH5KuKa76o7r-Lxmz40kIy6MHGo8KJjVFMsQ6HErB_NaXjNP6Y5H0LRTclrmoIaaSy4wL4GPy-BiRBcWkcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79edc7079.mp4?token=TPlozajcRauM2-YO4jhGyF_TiTMU7i3HUuj5OVyMo_5JANDJoWMtPQEbHQYCCge_Qo84F3NaYwKe84yQhihrvQdNqJuFizZiQWvvLKp9FMa6BdoSbm6AXPi_0gWOZg0nr4nHEcYcoIBGr2qwGYRgaMuPjVooA67wXNPYCWvpRHY3b2ohr0S14Q5G83hFiay-y_nCgSKLd9LobaeNCU1ohWluyVU9uDi6TyFXEZkKUJT2weJa9yl9hVv9MXURblrIJ9wLH5KuKa76o7r-Lxmz40kIy6MHGo8KJjVFMsQ6HErB_NaXjNP6Y5H0LRTclrmoIaaSy4wL4GPy-BiRBcWkcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇶🇦
🇮🇷
#رسمی
؛ ریاض‌محرز ستاره سابق سیتیزن‌ها با عقد قراردادی به الشمال قطر حریف استقلال پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108683" target="_blank">📅 17:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108682">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVuaEVbVbLTOPaMD2iDZeISrgADlfMFrjxsfSsVTYLIVnb8YSuOZRFQzr85Dk9HpMhIb14MyqKRdAE2NthvRHwJcn7y3Y1zGSbZlFUhapwLV_QIxL84cFUrk2lQLO3j9iU-PDaFkVKwgvNBscGG73KpiuHW-c_W5jBDiizvxA5hAkdaCQgFKdJxXMelzX4Ma7F1IHPuRyIXFDD4UTb6THBMT1ZMs4by9UuWJ51Jf1nZFSi0l62qYI2iDuxHUm4ayyEbFaCA1C2qU4EJISZOLtNOmZ0E8QlOc7CUWB2Zu_i_Z5Gn8MhI5s_ocXniOHvHW6282hR2WEes2fBjLuCcM-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇪🇸
ترکیب منتخب بازیکن رئال‌مادرید و آاس‌رم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108682" target="_blank">📅 17:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108681">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
⭕️
❌
رسانه‌های حکومتی از افزایش قیمت اینترنت به میزان ۴۰ درصد از بامداد فردا خبر دادند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108681" target="_blank">📅 16:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108680">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f36bfce94.mp4?token=aG-cZYVoXxI-Exl6jLqdLpEadw4rEe5_uvzeca6xHZ8dJrWGb9cvH5X5guVvV3hrfeArIjeBHTRut0Q0N95jh9o39ZKuo0yejN-GvPe6GxAKkMeg4Bs1yaTXm12FkDIWK7KamjpKwceY_06d_S-d8hmIJAjD2ngOgVuOGjiglGDrXHuJ2Sncm0ltz95Vx9_-zIKc6TU1SHSski8KsgrGDMXkSHk8NOfYJY14FF2w9rcLfdSno1ZFAf5Ah1-SeBcoxyAp8iqT3wZOD4tlN6PX0xrDn1OKYU2Y-Po0TviI4rHGGXPPYZ8VHlO0UgiIdrffIZgH1xrrLz7mLM4qMKj4bG5CZkz3C2v7PhvSib2bgHg6FqV1wu5lzmRLljjsEomQPQoCwL1W352D1QLQD_75L5BMvqomyjfOjwkUl07v2hAq4-Vh_i8mjYgtxGEWEK7DFsZSBQAycR-cnCtZoEmK87LBGdie8-GFOO97vdZ9chBjXhMYRejm7IKHqUm16vWUv0eMfdF_nU9MDoXooqrsKO7bJFUGhrYGXL6kzhJzoxrqvV9cWANYVlKanFRxkRx569fFf0hdxYREhnnbqCh-dRUVpUPcESEYLEIQR2xNffcy_gn4XhKxU4URJ84mWCIkSzHsmj4IN4JgYacVw84du5HHGQ4t6mbDwvEfdrcgjpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f36bfce94.mp4?token=aG-cZYVoXxI-Exl6jLqdLpEadw4rEe5_uvzeca6xHZ8dJrWGb9cvH5X5guVvV3hrfeArIjeBHTRut0Q0N95jh9o39ZKuo0yejN-GvPe6GxAKkMeg4Bs1yaTXm12FkDIWK7KamjpKwceY_06d_S-d8hmIJAjD2ngOgVuOGjiglGDrXHuJ2Sncm0ltz95Vx9_-zIKc6TU1SHSski8KsgrGDMXkSHk8NOfYJY14FF2w9rcLfdSno1ZFAf5Ah1-SeBcoxyAp8iqT3wZOD4tlN6PX0xrDn1OKYU2Y-Po0TviI4rHGGXPPYZ8VHlO0UgiIdrffIZgH1xrrLz7mLM4qMKj4bG5CZkz3C2v7PhvSib2bgHg6FqV1wu5lzmRLljjsEomQPQoCwL1W352D1QLQD_75L5BMvqomyjfOjwkUl07v2hAq4-Vh_i8mjYgtxGEWEK7DFsZSBQAycR-cnCtZoEmK87LBGdie8-GFOO97vdZ9chBjXhMYRejm7IKHqUm16vWUv0eMfdF_nU9MDoXooqrsKO7bJFUGhrYGXL6kzhJzoxrqvV9cWANYVlKanFRxkRx569fFf0hdxYREhnnbqCh-dRUVpUPcESEYLEIQR2xNffcy_gn4XhKxU4URJ84mWCIkSzHsmj4IN4JgYacVw84du5HHGQ4t6mbDwvEfdrcgjpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🇮🇷
صحبت‌های جالب بانوی هوادار خیبر
: رویای من حضور مانوئل نویر در خیبر است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108680" target="_blank">📅 16:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108679">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50fbec86e.mp4?token=gIKczPKuvuctnerP57Svu9gZg5kHwxiFV6YHYINoGmojtZ_cfhFSHaQiimLR0qTxdJ_VzArw4V4Esuu94-mkMci8bIysQoNILAhhjsVwoPe6KaLAUCQzPIW8zzN4TfURksZSPD94GAVGnXs1uWg3GlT4PJa6wUvKvyrP5z_oZEP94fJTAxmhmHi0mh3TutueTBOPcZwupmDKNicOEICPfBAbM01mB_ohQxTCa46qTSm_P5wTPMc_DTvzXUrkgNIQSUkLZmTVAxS8pYuy_vC3SJguWsjiWwuaWjYJvQSkvV9IexOs4Kwg26fzGDWPHC5dUFLIzi_XTVNOluy1WxxxtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50fbec86e.mp4?token=gIKczPKuvuctnerP57Svu9gZg5kHwxiFV6YHYINoGmojtZ_cfhFSHaQiimLR0qTxdJ_VzArw4V4Esuu94-mkMci8bIysQoNILAhhjsVwoPe6KaLAUCQzPIW8zzN4TfURksZSPD94GAVGnXs1uWg3GlT4PJa6wUvKvyrP5z_oZEP94fJTAxmhmHi0mh3TutueTBOPcZwupmDKNicOEICPfBAbM01mB_ohQxTCa46qTSm_P5wTPMc_DTvzXUrkgNIQSUkLZmTVAxS8pYuy_vC3SJguWsjiWwuaWjYJvQSkvV9IexOs4Kwg26fzGDWPHC5dUFLIzi_XTVNOluy1WxxxtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیری آنری: چرا اون رابونا رو زدی؟⁣
یامال: اونجوری قشنگ‌تر بود.⁣
تیری آنری: سه‌گانه ممکنه؟⁣
یامال: همیشه ممکنه، ما بارساییم و به نظر من، بهترین تیم دنیا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108679" target="_blank">📅 16:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108678">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108678" target="_blank">📅 16:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108677">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hFLOMrq6PhvvtxN_3ko9fjUSQQyEo7i_FpuKn7t0NW-v_AJn7D0f-Pi3pT9Jo2Yxvn3U7C7iDbgqFaJHwHkxcfpd0UJcz9q_cP3OmXsSS8ADVoYcj-LTiRcBFmxPp_G8zanSaU4YMMhRpCZawuM6Umzz0th79iUxh7bfX86XhEezZioCwChNi84n5J0rOc0ppl5Nhtu8PeAjATH5iHUoMJcbq4221G4SdUeHiz2nnve2js4cYRupi2c1i14_k8FOMJABcVaPH6dZnl4KIPihM0R4_iwZpwhylLVwyau-gPUoWCUkP6tM7R8m3GUcrO6De8BtdZ-rJ6GPWSuWwANbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108677" target="_blank">📅 16:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108676">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94a2dc84c7.mp4?token=aVQHUebJTDya8Ls3YqKiOxwOODmqBzSWalPoFg7iNS9XKM_JqmLLBeXp1llryQ2SICTi89kp2jGq8EqOwMJvulJj4GttaUpe-2OH8G735HQUrAf7tJ_wsV-4Am1KjDpLL7vqqZHhvSJmDX0te6K4ueBkGCVjL2_s9vS1I60mKRxTkOlx_TBccRqmLspOGPmnqf2L5IT6X3FH4RWnAAjm4LAX201uPmGC1sTdWBlJjKRMsxvtUtIK0DIeElR-iozhtzoJyRoG0RZ5UHU5y9AtJScVJ9OXuj4F5DdGMQPaGUroRktaKqtqL41udDVRExYDg7n0iamQmZl9EbA24of8uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94a2dc84c7.mp4?token=aVQHUebJTDya8Ls3YqKiOxwOODmqBzSWalPoFg7iNS9XKM_JqmLLBeXp1llryQ2SICTi89kp2jGq8EqOwMJvulJj4GttaUpe-2OH8G735HQUrAf7tJ_wsV-4Am1KjDpLL7vqqZHhvSJmDX0te6K4ueBkGCVjL2_s9vS1I60mKRxTkOlx_TBccRqmLspOGPmnqf2L5IT6X3FH4RWnAAjm4LAX201uPmGC1sTdWBlJjKRMsxvtUtIK0DIeElR-iozhtzoJyRoG0RZ5UHU5y9AtJScVJ9OXuj4F5DdGMQPaGUroRktaKqtqL41udDVRExYDg7n0iamQmZl9EbA24of8uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
هوادار بارسلونا دیشب در استادیوم گالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108676" target="_blank">📅 16:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108675">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOR-YTVJy9apBIq9r9sQ9iNLmOlR1MWQFjkv_kPeRppksZWyfHAWfuT43une56IP4tXdDL4N3-SAGFk0F9AH90ojodtRqOZIcDO80PqT4aIVQmFpQNoSg0jGqb3-LwWfvwxTG125R4QXUXcPaqFx1KXJvIkIRpCa4gJnzDao1Yt-EfhD3oFrZOUmWit3LNIkCPrZKo9KSQ_9acpq7xWO8emR0bAmjWpBli2xHKJZZob87dRjOLFp7_CuOZ2KxCdSmM9Dk17S3zCOsunlJ0eOlosotcbQTCLOkKUzv7ZzLiVTs1lRnJANS_y4gDdmQezcu8JOYgZX5LXkGaqLuIDDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
ترکیب پرسپولیس مقابل خیبر خرم‌آباد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/108675" target="_blank">📅 16:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108674">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1611c80de0.mp4?token=VaYePdAGmRsrTa7cG7b4WHH4oYx2RsTQhun6FRUD9rByWou7OWASg3-DLpX8h8QVkhXUDdv9vbXz1zyIS9CC2Pe9CpXjT7qnc1BblGLA4a3UmZb3VhPFzETiAIVzo7PH2qeeMDqb8v1upc8sNi3GdObfoc41YFWf-m2WEUXvgDAR9iCRIKRy2xVjfRqf9tXIT9meISw70HdKdSgFcc58mAQ1PggAVO5aDTRieaJBfI6qjJuRWsbIM-wr1temPRMOv1i5rZkS7_qiXyVvwPpW8f1P18_LHn0q_WaSvgWsfYk_yhxTClz8cWW6DvSBHJ1fvtNSfSINWwpUZ135qMnSyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1611c80de0.mp4?token=VaYePdAGmRsrTa7cG7b4WHH4oYx2RsTQhun6FRUD9rByWou7OWASg3-DLpX8h8QVkhXUDdv9vbXz1zyIS9CC2Pe9CpXjT7qnc1BblGLA4a3UmZb3VhPFzETiAIVzo7PH2qeeMDqb8v1upc8sNi3GdObfoc41YFWf-m2WEUXvgDAR9iCRIKRy2xVjfRqf9tXIT9meISw70HdKdSgFcc58mAQ1PggAVO5aDTRieaJBfI6qjJuRWsbIM-wr1temPRMOv1i5rZkS7_qiXyVvwPpW8f1P18_LHn0q_WaSvgWsfYk_yhxTClz8cWW6DvSBHJ1fvtNSfSINWwpUZ135qMnSyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
کنایه‌جالب ژوله به درگیری دبیر و فوتبالی‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108674" target="_blank">📅 15:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108673">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=VIYVjoDCLslK5EhJksBCW9cJpyzXLxT5XEtlA7t9aXI5MtpQ0N4FI_a_Opn601feZR0Z_m1XA11B3WcTajdBdbTIZUfWHX64V2M9r7m_MfJQOmue95m5PbxIX3dzo1n-YtP1qXpcJnEAMvNbSnZsBZVS857XmCIKyVJ81FYd0SLabj1kM8qD58YC-9xMK9hFso9GoMh6g_eZnIDB7pEk3_pVT_6t6ZEpnnd6ReaoQDYRXlN1CQhfizdeUAC3P-pj9Qi0BKDFDEQrDTS26teRl4EJtWvBNM_T0zgr_oUdxmQwwryKrxiY8P9gT3IiMGgMu3mhh4-ob5tGlMiYMQxv1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=VIYVjoDCLslK5EhJksBCW9cJpyzXLxT5XEtlA7t9aXI5MtpQ0N4FI_a_Opn601feZR0Z_m1XA11B3WcTajdBdbTIZUfWHX64V2M9r7m_MfJQOmue95m5PbxIX3dzo1n-YtP1qXpcJnEAMvNbSnZsBZVS857XmCIKyVJ81FYd0SLabj1kM8qD58YC-9xMK9hFso9GoMh6g_eZnIDB7pEk3_pVT_6t6ZEpnnd6ReaoQDYRXlN1CQhfizdeUAC3P-pj9Qi0BKDFDEQrDTS26teRl4EJtWvBNM_T0zgr_oUdxmQwwryKrxiY8P9gT3IiMGgMu3mhh4-ob5tGlMiYMQxv1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🔴
هوادار خیبر: اینجا اصلا پرسپولیسی نداریم؛ بیرانوند بچه سوم را بیاورد و معاف شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108673" target="_blank">📅 15:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108672">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2535928121.mp4?token=UI0aRZCuK8Brr2sfbqOJGdY5Z9xesM3jGbBJ43rd157ZZTEBGiPhcFI4rIB_ZmnozU6sG_GXVIAK8IjExxeQdjDt7b9a26vvkBheTE2vpmYAoLwlCugjHwBOvskPqZKtnTxRwAQIGIO49ySNGf-xGEtG_9Ei0q-HozDU8fXKg05osdGB6Qw01OqWVCyMpLaDe76LUs3ZHbbZGn6RIE1XW0FGySnRRqVF6NV-BZP7b1rVgqdXJ4qML3gX6fgRItibRvgq1vLRAcytEbgFFYEA778vqsNUq8IX9Ss5FnFwxMUS8pXSJUp431Vuj-zcWOdP261WDx9B7BkiUkAvBKIkkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2535928121.mp4?token=UI0aRZCuK8Brr2sfbqOJGdY5Z9xesM3jGbBJ43rd157ZZTEBGiPhcFI4rIB_ZmnozU6sG_GXVIAK8IjExxeQdjDt7b9a26vvkBheTE2vpmYAoLwlCugjHwBOvskPqZKtnTxRwAQIGIO49ySNGf-xGEtG_9Ei0q-HozDU8fXKg05osdGB6Qw01OqWVCyMpLaDe76LUs3ZHbbZGn6RIE1XW0FGySnRRqVF6NV-BZP7b1rVgqdXJ4qML3gX6fgRItibRvgq1vLRAcytEbgFFYEA778vqsNUq8IX9Ss5FnFwxMUS8pXSJUp431Vuj-zcWOdP261WDx9B7BkiUkAvBKIkkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
‼️
کلا هفته خوبی برای گیس کِش سیوس نبود. ویرجینیا هم ازش جدا شد.
💔
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108672" target="_blank">📅 15:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108671">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33db152fe.mp4?token=s6I4vaZ-d4DqC2na2lKYUdptuuKhNWIapAyIYxVpgWbVvRkH7G0tIkvh4uutYEdldyzzU-SeqeLeZAwtl8awYBqwIW0CO4vNmc0IAIia7KqswfSXhrlW94Em0vpeW_3IvdOp8_pIOGv4or2VV6WzD5jhGDB_eo6PepJ0yWFEW6m518FU0cHWY1PfbGt_9pycaBSMAqiN5OJCfrGOpQGuo-urE_p-Z09SvYCqk0q5OnS8-jfXQY3iKM5rLyJF9IF6R48CqqkvFys9Iu1rgMVT3G_1NKrby7cyyeOEqJhso7DZnhYrtCJ2WhphKfKOjZtuJ5KPJHsD1MngmXV57zIHIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33db152fe.mp4?token=s6I4vaZ-d4DqC2na2lKYUdptuuKhNWIapAyIYxVpgWbVvRkH7G0tIkvh4uutYEdldyzzU-SeqeLeZAwtl8awYBqwIW0CO4vNmc0IAIia7KqswfSXhrlW94Em0vpeW_3IvdOp8_pIOGv4or2VV6WzD5jhGDB_eo6PepJ0yWFEW6m518FU0cHWY1PfbGt_9pycaBSMAqiN5OJCfrGOpQGuo-urE_p-Z09SvYCqk0q5OnS8-jfXQY3iKM5rLyJF9IF6R48CqqkvFys9Iu1rgMVT3G_1NKrby7cyyeOEqJhso7DZnhYrtCJ2WhphKfKOjZtuJ5KPJHsD1MngmXV57zIHIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥶
حجم‌صدایی که دیشب در ورزشگاه گالاتاسرای از سوی هواداران تولید میشد، معادل شنیده شدن صدای اره‌برقی یا هلیکوپتر از نزدیکه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108671" target="_blank">📅 14:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108670">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9VPwlHHscs8zGXJs7iaOHSaUdUJ3v3CtOGLJKC-LDLyV-_p_jGu54nWbE5X2uBSazj5Pez65bZ3N67Zrsztl-87O6ozIN0aohTJGXv6uPMrB9x9LHWMdn2ZGdan0eCGWzQT8zcgFgF9wneBGhsAuVNmlB-vPpEre-76j0aGcvUH70r_F3yKAzITw770x8FY-GdY0a1fjtQnglIcjmaAlCt6qNaXw1Tghgabgjx4xRK3DgLYCfYxhJV-CyFVRBTaI066s1doIzwOIjgAOqfHcIyKaluO9eW0fxP_SiHAli01B4TaeZe4w7BI-CMXCEa28FpodaVlM7LlQUSKBNXUHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول لیگ‌نخبگان آسیا پس از پایان هفته‌دوم
🗓
برنامه هفته‌سوم نمایندگان ایران:
🇮🇷
استقلال - شباب‌الاهلی
🇦🇪
در امارات
🇦🇪
العین - تراکتور
🇮🇷
در امارات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108670" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108669">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8eb9d1b0.mp4?token=WdLBwYYfdl_-CD7ywENS8eWJiu4qSBAR1JmkcvFlPpO9OB_fzAwpY1qyIWe7ko-K3xgWL6Z6mjh4IrbItbU6bKVJijkk3TtxtKgw1IZUA_1bafw0eCJEpAbdCXfpcs8BNQXdLxe3eycUZIQW-mzHmaY1hkGJVPHA3NA22BaDtxTnykNgAtFd1je4Ag14BS2YhisZWfNJ38AzhTo_wHlNAQUyeWh56P4sSMCp1JYvEGfXyZrIIW-ynPhf2aFAOCbEGWVGJ-4BAeFIBSbKRkp1IU6Qlr9wey8PEAOAQzY3wXKAW6Bkfu5f3ffh5os09foozpi7TRecUXPema_A0DtJjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8eb9d1b0.mp4?token=WdLBwYYfdl_-CD7ywENS8eWJiu4qSBAR1JmkcvFlPpO9OB_fzAwpY1qyIWe7ko-K3xgWL6Z6mjh4IrbItbU6bKVJijkk3TtxtKgw1IZUA_1bafw0eCJEpAbdCXfpcs8BNQXdLxe3eycUZIQW-mzHmaY1hkGJVPHA3NA22BaDtxTnykNgAtFd1je4Ag14BS2YhisZWfNJ38AzhTo_wHlNAQUyeWh56P4sSMCp1JYvEGfXyZrIIW-ynPhf2aFAOCbEGWVGJ-4BAeFIBSbKRkp1IU6Qlr9wey8PEAOAQzY3wXKAW6Bkfu5f3ffh5os09foozpi7TRecUXPema_A0DtJjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇹🇷
گالاتاسرای 1-4 بارسلونا!
بارسای ترسناکِ فلیک به هیچ تیمی رحم نمی کنه!
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108669" target="_blank">📅 14:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108668">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3NhitZ-Ubi_74wDsKuyudWmaQ2CHISigB-NVqV3eIvTlvA__iTG0Y-jp6uOXE_W6qq-Ub-bqmEdOQhLP9o72TrbrqHJH6I0M73sku7xIixfqjJEonIiyNsh9HC03_C4tQHtqll5eHGRuBmTrK9AM7XlPlePTXc3b9U3l9TY5x1Yelh3j3n3--bG27eyefbiIzFQnO2pbIBeqGJwtRfvDKEC826j9zBXHkkJRqx6CI1Xca8XeMykouC4xiUPiCwQTTuDh2rTcYAwHTmEOCmuuG98Y9k9FY5sv86YiEJd-ZDD0yhvV032pWCoFqw7UmwV670DRgoYSG4V9BSj3Pwr5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
✔️
با توجه به برتری استقلال مقابل تیم های قطری در دو بازی قبلی، امتیاز ایران از فوتبال قطر بیشتر شده تا شانس برای حفظ سهمیه‌های فصول آتی در آسیا بیشتر شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/108668" target="_blank">📅 13:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108667">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805c98c083.mp4?token=qr64Ce01NZVeTHoK3rqCsENeepfxALu-y3GFy5iNRBmPUC-Jbm4m8W9kW4CgH6Y0_M2A2dCQqWkEH9ZfNRevzHxcQtucgA-BfMe-m11L2x7nCrd3u9Gg5w3xVJP-zEjXAAP83fPsBU1SNlB_8X0uAlsSoRwdmEq1k7g00IqDsB956RtRj6Rq7yAS-Jset7_klkdW-EuTIKngG3TScxN6mh4qU4pzJB1CpB_76i8gTVPqv0IG9zkypNBREogzkzUTmMCaSJMLWIs5bci8B2FUb-gc3lZKA_w7cW1ncPZbPXTfkc1JmwgexP9HWW0ma0UxNR8KVI5RzapNGUxAOiJ_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805c98c083.mp4?token=qr64Ce01NZVeTHoK3rqCsENeepfxALu-y3GFy5iNRBmPUC-Jbm4m8W9kW4CgH6Y0_M2A2dCQqWkEH9ZfNRevzHxcQtucgA-BfMe-m11L2x7nCrd3u9Gg5w3xVJP-zEjXAAP83fPsBU1SNlB_8X0uAlsSoRwdmEq1k7g00IqDsB956RtRj6Rq7yAS-Jset7_klkdW-EuTIKngG3TScxN6mh4qU4pzJB1CpB_76i8gTVPqv0IG9zkypNBREogzkzUTmMCaSJMLWIs5bci8B2FUb-gc3lZKA_w7cW1ncPZbPXTfkc1JmwgexP9HWW0ma0UxNR8KVI5RzapNGUxAOiJ_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
صحبت‌های جنجالی پیروز قربانی خطاب به فجرسپاسی پس از شکست دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108667" target="_blank">📅 13:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108666">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/37d4792646.mp4?token=BXP5aLdf0bE2yaq_P3z677gnBEzUwnvbonTVt90o416AMXllohWMX3E8qgZuGMtDTlIe_5deeE5kgEMxJucDvAT911mhz9oIredyjuBkIuBe9Q6h189gqETzLER59hEGZYRkNj4UMSuvVB6yeduL3-rJtfk5dW7ZdnNZfiBiba5S4xedPJ6BGjm6YCTWA1GiR614PiwLBWg5VzOxjyUUSm2oe1FBqE56aEmRHMvfDXScT82T97sWoRF-cSJZ8PzRY-fOv-LOsU_YB6DwEn_YYaQvHxSbaVOUUMhbSr3iXlj1BopMLnbvgCFObiTLcal7NItdAQPnUMNLMXW5HF3BYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/37d4792646.mp4?token=BXP5aLdf0bE2yaq_P3z677gnBEzUwnvbonTVt90o416AMXllohWMX3E8qgZuGMtDTlIe_5deeE5kgEMxJucDvAT911mhz9oIredyjuBkIuBe9Q6h189gqETzLER59hEGZYRkNj4UMSuvVB6yeduL3-rJtfk5dW7ZdnNZfiBiba5S4xedPJ6BGjm6YCTWA1GiR614PiwLBWg5VzOxjyUUSm2oe1FBqE56aEmRHMvfDXScT82T97sWoRF-cSJZ8PzRY-fOv-LOsU_YB6DwEn_YYaQvHxSbaVOUUMhbSr3iXlj1BopMLnbvgCFObiTLcal7NItdAQPnUMNLMXW5HF3BYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
این کلیپ شاهکار از کنسرت چند تا پسر توی خوابگاه دانشجویی، فقط توی چند ساعت میلیونی بازدید خورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108666" target="_blank">📅 13:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108665">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a20b75a47.mp4?token=cy5Eovj3IlmFCKD19Ot3iChz9XmXHJ9ygreckOHTVpnJNH-sl0Fu6awM7_CE1hSLHTv8xSZrQKQ0uIAAZX-MCJJFw9tOas5fUQK_JkOH9RU3sRJItEQJwrlz6iU_9qcAj3M4dmXrlVjdixRnXp4wAmaTg8YlaFmsFokYZtxsEIihIosAKVkdMyykn9QR0Psd2nqmsqvxxaG4wXajA87UIll2Md6di7ShFp4NbBGWi7ibCCO7FIPUWsG4y2svz5sGLdE7saR50SWxXfHvKSz73JuQhl7m4OsKTmS--1D8lbM5C1aXPJI8obI4DmvCYEHjJo02qFCGNc8qyhqevWfwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a20b75a47.mp4?token=cy5Eovj3IlmFCKD19Ot3iChz9XmXHJ9ygreckOHTVpnJNH-sl0Fu6awM7_CE1hSLHTv8xSZrQKQ0uIAAZX-MCJJFw9tOas5fUQK_JkOH9RU3sRJItEQJwrlz6iU_9qcAj3M4dmXrlVjdixRnXp4wAmaTg8YlaFmsFokYZtxsEIihIosAKVkdMyykn9QR0Psd2nqmsqvxxaG4wXajA87UIll2Md6di7ShFp4NbBGWi7ibCCO7FIPUWsG4y2svz5sGLdE7saR50SWxXfHvKSz73JuQhl7m4OsKTmS--1D8lbM5C1aXPJI8obI4DmvCYEHjJo02qFCGNc8qyhqevWfwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
💥
حرکت زیبا و دیدنی دیشب لامین‌یامال قبل از شروع بازی مقابل گالاتاسرای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108665" target="_blank">📅 13:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108664">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFTusWO6NobAiGHsNZ1eMOOHvK133eXadAwrttDhrMvJKW99UuQ1kFExGrbm2e4OgTAhQhFIev0NjCNDpgSMJrCOMaIMJY7HRQEiCPHmJ4LUM-pNa2KdliSXCVpoK9Tnr3rFKauIWbPqex9EoIPxu63xN4tHz0s3dgJYde5_3N2SAHKbrjfXfPaKBANt5T20Ip7AZpWSASB0BtZUI5ywpb5nxWNAEG9kkkouYwcWu3MVeE0IIhx79LTZ6T5JY26jbJcqG6L9AFVryChncIkF_0TnzcX_6j_4UUuTSRdjpujA12-8a8pt5U9xNQO8kpSSgVz0Lz6iUQD6qVc9RjdvcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⁉️
🇪🇸
کدام تیم‌ها در لیگ اسپانیا بیشترین گل‌هایی را که به دلیل استفاده از سیستم VAR باطل شده است، داشته‌اند؟
🤔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108664" target="_blank">📅 12:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108663">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e1b2f756.mp4?token=DyP4DoW4_UlUsk-E70jQT3t0uuqMWN8-sCDo_BBYtoNBs04x5MhdzFFkRhQA12PDG-syZ7mElPR0bXOtC8jqKH-jqMm_dsMu43Zp-R1elPODCbsgmH2_ZKtRXxEXFbBvCr6SSEEGSMArsY-Tuq6DzDwv_eTC5AZBwfOy3UiwNux-HSM8xxUzcp8T_2b_1SO5JQBXLQmyBmkg6-eLKdJqwgC_DZb7eKSpumqKbLnHMl1b3uh93ESSKQIBxK899wtKeRbsXqgKfrMDH2rsMN99yzuYwJwsl4dz7qrVcu7XRVnujfagOXBP8Pl6Y6ZP4WbCjYeyNZFWCenDQT5d-dKVGWXUv9qPR3rkeWkA_TstzwGqhYfg3Jv4itEuzfqLGVkMYgBOGFEd-u8VjNpEt5CslSbV7OGbQCDf09C2prAEiuFPMrKsDJrOBaBtKh_itqP0WvNEcgzq9zYMrwoAyAMm-ziqIKzM5pJ_kOqJGE9ttvYj5EFiasjIlehKW-ORDBq0wwRncU0H5PYQWoynM5gOpg_7XF68YIwg2Sx4ZJrlwwWs2WJ1uvbsvMo2CtKZ6aFD9nwOaXRUurrFy5bZ48ANVHnJYpxyiLBwGn-g2DoGKUNQCoK9Q_LlRDONq1OYzVnNbSKgbLC81b99QIbz_-mLBcSDPcmeJB_kBY2yLoj7I6k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e1b2f756.mp4?token=DyP4DoW4_UlUsk-E70jQT3t0uuqMWN8-sCDo_BBYtoNBs04x5MhdzFFkRhQA12PDG-syZ7mElPR0bXOtC8jqKH-jqMm_dsMu43Zp-R1elPODCbsgmH2_ZKtRXxEXFbBvCr6SSEEGSMArsY-Tuq6DzDwv_eTC5AZBwfOy3UiwNux-HSM8xxUzcp8T_2b_1SO5JQBXLQmyBmkg6-eLKdJqwgC_DZb7eKSpumqKbLnHMl1b3uh93ESSKQIBxK899wtKeRbsXqgKfrMDH2rsMN99yzuYwJwsl4dz7qrVcu7XRVnujfagOXBP8Pl6Y6ZP4WbCjYeyNZFWCenDQT5d-dKVGWXUv9qPR3rkeWkA_TstzwGqhYfg3Jv4itEuzfqLGVkMYgBOGFEd-u8VjNpEt5CslSbV7OGbQCDf09C2prAEiuFPMrKsDJrOBaBtKh_itqP0WvNEcgzq9zYMrwoAyAMm-ziqIKzM5pJ_kOqJGE9ttvYj5EFiasjIlehKW-ORDBq0wwRncU0H5PYQWoynM5gOpg_7XF68YIwg2Sx4ZJrlwwWs2WJ1uvbsvMo2CtKZ6aFD9nwOaXRUurrFy5bZ48ANVHnJYpxyiLBwGn-g2DoGKUNQCoK9Q_LlRDONq1OYzVnNbSKgbLC81b99QIbz_-mLBcSDPcmeJB_kBY2yLoj7I6k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحبت‌های جنجالی قلعه‌نویی علیه فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108663" target="_blank">📅 12:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108662">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiST7Xo67ImuVs3KhJXbnoNhjurDUKNiiiKT7gzQS8sWaHV0w7ta9gdLV89Nl6flFYSJo_o1dB3Az-KpJBwqfhy9W4BecB7nlVqmUOybCrYgYkyQDeosx_7_HBWYdpBPqK2dO3Wz7_g_NRC1tHNlmSpUtUSEz1GmGieaW8CBPU7_6NJqEPf9ohNTZqA4NryOFhA-6oqhoqpxpFwGuUrw9qXBJoWRmI4-PQqW52KPtFIo287wsyFg3LI8uToGqo3cPNBPZnvLhEmOLYlWrH1cJERNFwJxWQjYJnHQmfKLhRzUU5TQg9aLVWnEJlZMJUKJMqK17c4uSP_9jHxrEmXdRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیجان فوتبال رو با لیگ ایرانسل چند برابر کن و با پیش‌بینی نتایج، امتیازت رو ببر بالا!
✨
🎁
هرچی پیش‌بینیت دقیق‌تر باشه، شانست برای بردن جوایز جذاب مثل موتور، اسکوتر، پلی‌استیشن ۵ و... بیشتر میشه.
همین الان به سوپراپلیکیشن ایرانسل‌من سر بزن و اولین پیش‌بینیت رو ثبت کن:
ثبت پیش‌بینی (هایپرلینک شود)</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108662" target="_blank">📅 12:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108661">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be51a8784d.mp4?token=YBUOUYhvHfN2Urnd4vpogAUekkji5ew7baKb15HMfytakiaZ7niMvz-qjauWE4RnIeUQeVUuNnBo0iZ2mHJOAzY5gvb_mWWmDcFKhK_l0ygSNf2jR6m10ejnAfgtQlcS6TQZsh_bXN99MGgMJmvClUEM5hhJuqlu8n-leFbFQn-kKQGio908N27rPBmr_RcQNiyropGbJyjYnd4aaXib2ENnpetEcwVfL2cxj4UIFk6pggdB-EoLNwO64Le2Dit5BLM_8wV88I1nXUPKqYOHBenqDqC5Th6pgWMnL5xNp9Dzqmc8yx9z6gxZVYAvE-752R1EZjldTNfTCIAxnHSf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be51a8784d.mp4?token=YBUOUYhvHfN2Urnd4vpogAUekkji5ew7baKb15HMfytakiaZ7niMvz-qjauWE4RnIeUQeVUuNnBo0iZ2mHJOAzY5gvb_mWWmDcFKhK_l0ygSNf2jR6m10ejnAfgtQlcS6TQZsh_bXN99MGgMJmvClUEM5hhJuqlu8n-leFbFQn-kKQGio908N27rPBmr_RcQNiyropGbJyjYnd4aaXib2ENnpetEcwVfL2cxj4UIFk6pggdB-EoLNwO64Le2Dit5BLM_8wV88I1nXUPKqYOHBenqDqC5Th6pgWMnL5xNp9Dzqmc8yx9z6gxZVYAvE-752R1EZjldTNfTCIAxnHSf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب یامال جایزش رو به دوس‌دخترش هدیه داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108661" target="_blank">📅 11:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c48214e32.mp4?token=ZLOtZPDGe0eD1Qsk5g9HW8AUjw-HLtE2b05P-9X0MQTKXCyz15DDGCQfpvQXQzLC2y_LNnNvj3uXKZY6Ucfv23dg6tiCtV_x9CtQzAWuwLDvdDG0km75_orxSobSyH0B_NIWO8-QrOVoMtirVIMNKsceLl7JNgaJ80v_RU7Yfg1HlGF0FDHqYRylYiUirAUOyrCFh1XlBtmecuT3ng0llDwsEEaUAIuXUEnGzO6UAcDhJfZPKZPborEGY07PWirQebs837Z55PRn86QKzayfJI8OIlntd7wF0l-XxAFgtGDe4axHTg0NFYVJl-sbHeZw1-r-1xtfpp2Dhg30ioXMAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c48214e32.mp4?token=ZLOtZPDGe0eD1Qsk5g9HW8AUjw-HLtE2b05P-9X0MQTKXCyz15DDGCQfpvQXQzLC2y_LNnNvj3uXKZY6Ucfv23dg6tiCtV_x9CtQzAWuwLDvdDG0km75_orxSobSyH0B_NIWO8-QrOVoMtirVIMNKsceLl7JNgaJ80v_RU7Yfg1HlGF0FDHqYRylYiUirAUOyrCFh1XlBtmecuT3ng0llDwsEEaUAIuXUEnGzO6UAcDhJfZPKZPborEGY07PWirQebs837Z55PRn86QKzayfJI8OIlntd7wF0l-XxAFgtGDe4axHTg0NFYVJl-sbHeZw1-r-1xtfpp2Dhg30ioXMAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داره یه صدایی میاد
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108660" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108659">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108659" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108659" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108658">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ccp0VLEPR-KqRA7gLZHVWRYUXFSGGg-1mJgofAJ9NvF3S9EqQggxkk6SjehSogEa-KWIJtrNJBz4QPjUw6s7LnsC621HeynjRUkX1j734wPYrTzmSKgoTVTY3gMCvkSzjGyPw1Q2U_vOPDzHWFKNytO9NLHTndNvIyF5cq7sNS_eaCjOMXy2zQjkbUU2Pae3Qyhge5ZJsOiIODud1vhbS68wc-iSCCO3xpAdLiMMb9AEyv_kgVB6O9bJreoL_BD0LdfRRRLZvuYOT73r8gIj03s2jGjsG9KWNYTcD8oNllcR4veqtIlBkGyxNSChAKVfYWaFdDpkI6oKmMKF9p69Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
لیورپول
🆚
لاسک
فنرباغچه
🆚
استون ویلا
دورتموند
🆚
بودو/گلیمت
پاریسن‌ژرمن
🆚
منچستر سیتی
پورتو
🆚
رئال بتیس
رئال مادرید
🆚
رم
پرسپولیس
🆚
خیبر
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت، ووچر، کریپتوکارنسی
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108658" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108657">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69bfab0b19.mp4?token=vBN5EDfZjWyYkrkt5hM0gSa_PvZMDSVrm9vO0r1lFzI7_ho9omCfQTjWJTfvM7EgUfXqaxWGeNnLRDfE6ArfAjSFUAZ70lqRHFiNlXwKClZdzwJBiUydWradhu0FXMGykxCeILg3wt1KwfuhSXOs7SMjLSCLqbRDHMKt9ZTu6s3yByOexRTsJ_pPHqLZW4JifOhGULHiAYInHl4venY7p2D42wOvqMs7KAIVKu5M0FK2Olq4ee_DB-TZ-Z6hANtDyzWvAQJHOX7cPB_-Z8IS8tBPxLW_BBww9gtVzmsfBSjurGpDQzw9dHdgiH0qbXpsXMEDjodXqsQIJU_pbzkXnU5uTUeLe12Fn3fz5Hy8yqoSDlz71cmSCgjIdmejnyTYm_j98F5aBW5jx7hyMJHq1hkMKd4CGjVgN96aaWHH18XfwXxUUw3otrm-QyUnmlojCRi-Mlom2xOnsEOlhPpORbb-V3wA-jjgq73ynC4Q6NpKvq-zCjEJZcMw6n6tkRg2hj8i7rG41HOh3rzP2QYGTu1GW1OQJKzwujUrVWYWbMvN_rBNOvRu3FVaj6xS5UeEVPm9tT8sD68oq85dx-VBhCp9ojZXzv3ifjEnLS93YxRgOw6PbayxHfBj2RESnoHmzjr71cfRGWafQCqObPETshkLK3yCjLskbwM9yo-gtVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69bfab0b19.mp4?token=vBN5EDfZjWyYkrkt5hM0gSa_PvZMDSVrm9vO0r1lFzI7_ho9omCfQTjWJTfvM7EgUfXqaxWGeNnLRDfE6ArfAjSFUAZ70lqRHFiNlXwKClZdzwJBiUydWradhu0FXMGykxCeILg3wt1KwfuhSXOs7SMjLSCLqbRDHMKt9ZTu6s3yByOexRTsJ_pPHqLZW4JifOhGULHiAYInHl4venY7p2D42wOvqMs7KAIVKu5M0FK2Olq4ee_DB-TZ-Z6hANtDyzWvAQJHOX7cPB_-Z8IS8tBPxLW_BBww9gtVzmsfBSjurGpDQzw9dHdgiH0qbXpsXMEDjodXqsQIJU_pbzkXnU5uTUeLe12Fn3fz5Hy8yqoSDlz71cmSCgjIdmejnyTYm_j98F5aBW5jx7hyMJHq1hkMKd4CGjVgN96aaWHH18XfwXxUUw3otrm-QyUnmlojCRi-Mlom2xOnsEOlhPpORbb-V3wA-jjgq73ynC4Q6NpKvq-zCjEJZcMw6n6tkRg2hj8i7rG41HOh3rzP2QYGTu1GW1OQJKzwujUrVWYWbMvN_rBNOvRu3FVaj6xS5UeEVPm9tT8sD68oq85dx-VBhCp9ojZXzv3ifjEnLS93YxRgOw6PbayxHfBj2RESnoHmzjr71cfRGWafQCqObPETshkLK3yCjLskbwM9yo-gtVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
با داغ شدن دوباره بحث تخلفات منچسترسیتی پس از برد قاطع این تیم مقابل لیورپول، مروری داشته باشیم بر دیدگاه یورگن کلوپ درباره این پرونده؛ پرونده‌ای که لیورپول و دیگر رقبای سیتی از ذی‌نفعان اصلی اون به شمار میرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108657" target="_blank">📅 11:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108656">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qbwvOiPXXvkTEkZEYnGmZfxzAJHl1VKtoXFRayKIY-b4749xaSGEGscpWsKAHnIj9jip0j2kNVrT_TRamK-8FiEmiKatWelxD_zS5RvsPdYK8UI2DPRFFZjnvs5yFM05FTaaOsfL58H18TOZhjKofOcISmHORa0H2DCqFuoiZOeS2gRNz87ZxDc29UHBwyGKE-VCC-0ZB0v1p8LIpV-BrjwtmFyKAQxmcmyzfTl7pQHi8VXh31pRI6VezuDt2MwCOIGIDHhQD4SabJVxhEDsz3H0JP2UqtnA9VJzP2qs0uwqaTxQAVji9RlWE1idXnGs5YljoWs3NVnQXy7sEMizjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
براساس آزمایشات اولیسه، رزاقی‌نیا هافبک استقلال بدلیل مصدومیت حدود سه هفته از میادین دور خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108656" target="_blank">📅 10:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108655">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9746e98953.mp4?token=CmsXpyEIHkJY5z0ChrKKvoHcUE6lpeHASeI48KMGdHawOsrQYZ6YxsLvfX2E2pCGYPqkhKllp-RO-L9Br8eWPPOdizc9x9Zf79lW-WyZ-utLquW600x8fxS-ZX_OveQnAg5hVDPW2gBoqM48mwb-mIUgazKiJq6-lmJIIR9YC0WErUVs_FUiLnaLqYqCHBSKPWKXPcE864QCUODjgaEFtr6GIERQEK_D744sWjT9RMmwniikHcT_TLPguxZYDT8WgT4o8oJd5EyI-jQ5RlGoYbOHAyk5dqtvD9qEpGR4Ul4rj3qg_8X0HbbUIcnWWKPYsRA0ArEkeaHu9Zy10Z5YGznHQGCwMOZxHsejTLHCHX0iVKpOkIZvZoevSgeCXrqL3Vapq20luXlFx_ESaqgwJ3hEw2J394-ptxBZmuurWktor4aCzQ4yzJ7gb8Es13MX0L9ExYgfx3XCGBLHDV9kyZF9zxH51ytRWZnUhJMVhQUxYlOU7VFkZskJ-rqoeBr0H1We9AANTzQk3WaOekm1uhbOsU5HK5q3ApnDihEV1rjML4zzuZ2j57cuN_CE6pil5iUHux-yIkgdqw70Sq5lF_kqEsLmcsf7oXQ6ayyGfIF6DfUrmEeCMDnDSXoDqOz1Cp19P1eZOXs1KEabnW8pkeGe-XDtlSpdsffhJ8DkNjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9746e98953.mp4?token=CmsXpyEIHkJY5z0ChrKKvoHcUE6lpeHASeI48KMGdHawOsrQYZ6YxsLvfX2E2pCGYPqkhKllp-RO-L9Br8eWPPOdizc9x9Zf79lW-WyZ-utLquW600x8fxS-ZX_OveQnAg5hVDPW2gBoqM48mwb-mIUgazKiJq6-lmJIIR9YC0WErUVs_FUiLnaLqYqCHBSKPWKXPcE864QCUODjgaEFtr6GIERQEK_D744sWjT9RMmwniikHcT_TLPguxZYDT8WgT4o8oJd5EyI-jQ5RlGoYbOHAyk5dqtvD9qEpGR4Ul4rj3qg_8X0HbbUIcnWWKPYsRA0ArEkeaHu9Zy10Z5YGznHQGCwMOZxHsejTLHCHX0iVKpOkIZvZoevSgeCXrqL3Vapq20luXlFx_ESaqgwJ3hEw2J394-ptxBZmuurWktor4aCzQ4yzJ7gb8Es13MX0L9ExYgfx3XCGBLHDV9kyZF9zxH51ytRWZnUhJMVhQUxYlOU7VFkZskJ-rqoeBr0H1We9AANTzQk3WaOekm1uhbOsU5HK5q3ApnDihEV1rjML4zzuZ2j57cuN_CE6pil5iUHux-yIkgdqw70Sq5lF_kqEsLmcsf7oXQ6ayyGfIF6DfUrmEeCMDnDSXoDqOz1Cp19P1eZOXs1KEabnW8pkeGe-XDtlSpdsffhJ8DkNjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
رویانیان مدیرعامل سابق پرسپولیس و رییس پلیس سابق ایران: راه حجاب، گشت ارشاد و برخورد فیزیکی نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108655" target="_blank">📅 10:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108654">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0060865794.mp4?token=GlyOrH4mVJ1u7VPHv9DqTXtNFL3kfDd--T4xdYLJxD7Y4CMT3bNtmO2WXp3Sp4i6YZIM2wYoU0bAKqFGqvMJytLBU_C_lRupTYxqvRIr1y5XylqBS0OFoNTJW9iXhFR65TUYUqtRlx8ksCKOpB3HZtvV5usH947f6QmQr3MLFH42nBZjQF9OGBIzdwpT7x1wG0sxfLG7xTiZNwNsk0mutKxrRz2PSc2nxu7t0sRENSLrfkZSBqwoP-1F-GtzSpGM-uE-uNVgitYm6KHv8NNvGw71PAlG7AVrIjKRXqUUz_O0p9mNMIIVNUlgnwMYJx2IWud1TZKKtDicJ65KoI57rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0060865794.mp4?token=GlyOrH4mVJ1u7VPHv9DqTXtNFL3kfDd--T4xdYLJxD7Y4CMT3bNtmO2WXp3Sp4i6YZIM2wYoU0bAKqFGqvMJytLBU_C_lRupTYxqvRIr1y5XylqBS0OFoNTJW9iXhFR65TUYUqtRlx8ksCKOpB3HZtvV5usH947f6QmQr3MLFH42nBZjQF9OGBIzdwpT7x1wG0sxfLG7xTiZNwNsk0mutKxrRz2PSc2nxu7t0sRENSLrfkZSBqwoP-1F-GtzSpGM-uE-uNVgitYm6KHv8NNvGw71PAlG7AVrIjKRXqUUz_O0p9mNMIIVNUlgnwMYJx2IWud1TZKKtDicJ65KoI57rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشتِ احتمالی ستاره های منچسترسیتی در صورتِ سقوط این تیم.
😕
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108654" target="_blank">📅 09:50 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1661f71c8.mp4?token=EwtGirQb8PWtwgUS6KNpHerEKMqy8Plvm48uBmnRmfm5dsg4NVvULvntRygjOumKi4wqvP8zClBxL0CeYY3XPQxmkDkaubndZycWXtFPJnMFGmmiVMfPq25gZaV0ms-qqzKR4bQzoJG0rAKeWhSwjWi0B779Vz47bKVu25gKMmilbkYlnwprilLwZYXDfXoJIXa7kwxyfMpon32KS5OdcHElIerJIaIJidOAsJr4Eeo_2H-YlbfxuIevqSirc9xMIDWtIzyDv5V7x8SnRHt3kLtpcoW7UvrtHpBIZyMueJ7-b6F9p37p1tEX_CYCajnuZOPaX47xO5HL8C8DxZ5Jkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1661f71c8.mp4?token=EwtGirQb8PWtwgUS6KNpHerEKMqy8Plvm48uBmnRmfm5dsg4NVvULvntRygjOumKi4wqvP8zClBxL0CeYY3XPQxmkDkaubndZycWXtFPJnMFGmmiVMfPq25gZaV0ms-qqzKR4bQzoJG0rAKeWhSwjWi0B779Vz47bKVu25gKMmilbkYlnwprilLwZYXDfXoJIXa7kwxyfMpon32KS5OdcHElIerJIaIJidOAsJr4Eeo_2H-YlbfxuIevqSirc9xMIDWtIzyDv5V7x8SnRHt3kLtpcoW7UvrtHpBIZyMueJ7-b6F9p37p1tEX_CYCajnuZOPaX47xO5HL8C8DxZ5Jkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامسونگ هم داره آیفون می‌سازه؟!
👀
🔥
طبق کانسپت‌ها و شایعات جدید، گلکسی S27 Ultra ممکنه یکی از بزرگ‌ترین تغییرات طراحیچند سال اخیر سامسونگ رو تجربه کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108653" target="_blank">📅 09:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1136457e.mp4?token=SAZ7nZjwajVHcwNd2NdwYpi3I0mly1NdRjtUSIC1qRMJ6egIqXgfvArc2obd8EKvcrZMH7b5zWn7iwPOPaCl05D6vZga_XpptMgmysDS0D7k7hFvawpjhUs8h1FqQFN79mjxLNeC2ErCiGIiKxgrFJQcHoWcNLdspAoueQOx_2H9E8AwbhhjK0b5xZ8qDhlsk0YoBPDfqPdMzRhqNXxzDmt_Ev7u8YMk7U1TDvmotea4EHh-DOm12QHQs5141oYThtu6ZLtT07R1GDKJGJXFJ_O2Alailig_GpWJsJXAvBBzaL6j7bQrMsNqYBZu-yj5NZ5c7ZqwMRmBuLl4ifKxXbvGXISIGLA8vz30VTAOQ18qESphCOSf4K9hyTZXNlZL4Gjpt0sXhV9gyHrQ8GW4xHdQW8H-HB1w_upbqWiWNpEq3BhCcgpFVF7y_AaeeGm66ocskn188ATalBg8Y4Vj289g-RStBMGaEmN0IYrLZpFK1YgdA9ModFELOgbL2c3yCqQY7oECLdQUrHdUBAt6SY2648qcdyrSU7neOqiQ8v9j03m0aFCBp5LHI7vPJojzRxtN6U7AdkoNl0oNOcjp1mQzrJv89Bz_oH6lZlQ1n12URn8E239nmvkYRWVDc2_nzy7wgyB0waLeQaqsQl3ncrAqQdMErR-rGrJSk6CIGSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1136457e.mp4?token=SAZ7nZjwajVHcwNd2NdwYpi3I0mly1NdRjtUSIC1qRMJ6egIqXgfvArc2obd8EKvcrZMH7b5zWn7iwPOPaCl05D6vZga_XpptMgmysDS0D7k7hFvawpjhUs8h1FqQFN79mjxLNeC2ErCiGIiKxgrFJQcHoWcNLdspAoueQOx_2H9E8AwbhhjK0b5xZ8qDhlsk0YoBPDfqPdMzRhqNXxzDmt_Ev7u8YMk7U1TDvmotea4EHh-DOm12QHQs5141oYThtu6ZLtT07R1GDKJGJXFJ_O2Alailig_GpWJsJXAvBBzaL6j7bQrMsNqYBZu-yj5NZ5c7ZqwMRmBuLl4ifKxXbvGXISIGLA8vz30VTAOQ18qESphCOSf4K9hyTZXNlZL4Gjpt0sXhV9gyHrQ8GW4xHdQW8H-HB1w_upbqWiWNpEq3BhCcgpFVF7y_AaeeGm66ocskn188ATalBg8Y4Vj289g-RStBMGaEmN0IYrLZpFK1YgdA9ModFELOgbL2c3yCqQY7oECLdQUrHdUBAt6SY2648qcdyrSU7neOqiQ8v9j03m0aFCBp5LHI7vPJojzRxtN6U7AdkoNl0oNOcjp1mQzrJv89Bz_oH6lZlQ1n12URn8E239nmvkYRWVDc2_nzy7wgyB0waLeQaqsQl3ncrAqQdMErR-rGrJSk6CIGSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
📊
آنالیز تاکتیک جذاب این‌فصل آرسنال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108652" target="_blank">📅 09:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f591d52518.mp4?token=U_jfTtzd-1hwfXKPsN6Ya7RpSPLcuLqROXNgiHYNgQY0h6xjnNZSiNctdABSxd7YIOE2Z0JHU0xy9dJ-NTuF7UJ37ucz2XuzjZHrNoto6UrIUR3P3czkB776xbZRGcJtmrikiwAOAlRS82E2LHtjGT5B1ssy_y8pha7oja3lSQYmYkZbs-DwpP6kq4ysF2N54b8H5Ow1sk4UZtUdztCtbcgtzQc3V5H5KipztOzHuIHBCHr8T0u8-sydQkBFnIFjBPrVRr6uhiERjqFQ7PK3OBcR9d_lqaelpTn2tOiyB2e77s0RnEiDCdI625DnkYVCNIFs6PmygdEJIjqOfahOJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f591d52518.mp4?token=U_jfTtzd-1hwfXKPsN6Ya7RpSPLcuLqROXNgiHYNgQY0h6xjnNZSiNctdABSxd7YIOE2Z0JHU0xy9dJ-NTuF7UJ37ucz2XuzjZHrNoto6UrIUR3P3czkB776xbZRGcJtmrikiwAOAlRS82E2LHtjGT5B1ssy_y8pha7oja3lSQYmYkZbs-DwpP6kq4ysF2N54b8H5Ow1sk4UZtUdztCtbcgtzQc3V5H5KipztOzHuIHBCHr8T0u8-sydQkBFnIFjBPrVRr6uhiERjqFQ7PK3OBcR9d_lqaelpTn2tOiyB2e77s0RnEiDCdI625DnkYVCNIFs6PmygdEJIjqOfahOJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
مرور خاطره گل عقربی اولیویه ژیرو به کریستال پالاس، با بازگشت اسطوره به امارات⁣
ژیرو: من آدم متواضعی هستم و اشتباه برداشت نکنید، اما فکر نکنم دیگه مثلش رو ببینید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108651" target="_blank">📅 08:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108650">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108650" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108649">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z_fdUJUOECLdSnDfy0F4IWKvQwF2gxYo8A-nEtSwZb8izIfTs4S6pZkwJlRCimGpMz0oLHblH1XhyNiyW2e6VA84GtcI8u2VoMO_IrZ_xfDEcC6gjy6XoT7kBtQZ5S-I2YiF8P5bwpx3YekpXIrDRfFm5DIp1Vqwwmkt3OtlzVsSLlIWH_rsUOMhg5JA0_INWvH63zNSA4J0N5rwEZNoAwKNxspUX67XC6zitZehNcvP769GQMSipEGfC7t2qddWh7DkgH0MDhv3Jvy9k1Z9Hwdcs5N17tvr8HwOKMMxr0BHjm5X2dApU7Td7gm6tA9WSnz2c7L4wgZ4porrfeD_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب :)
😊
😂
میگی نه؟ بیا تو چنلمون و ببین!
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108649" target="_blank">📅 01:41 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108648">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108648" target="_blank">📅 01:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108647">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNupDjmmr-h1jjtH4jsD2h8kGBXdSyZMsKlqEok81Gi_9Zr3lXwj3N65K8_1jKFFon6Z2feba-PypNI9XJkyysfSKdzXdTEadyiF6nTXTVRsph71yYkcYKBghC2w6qzjDQjKQ_HQO7S4tZwesAv-3lclKFMAU3ajxdzq8XCEUKjLjrLHF6Mv0cd3bjtInIUTWX2tnqXNTejvbqkCgecaCW_N8Q_v1MTA4swkLpMFQCWAsmY0pARkPSsxDHLr9OneU-QzwsizKfu-m5A_Myt5YBgWOrwmv4c6rc8yEWG9mPfyZ56lnhyCerVg0CsIVFGjahJN2HZ84rnE_vc48EqE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108647" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108646">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Trym7wfJWKFyCGU4qekPwPPBKIy4fycai8QwmDrbH8C7K11m5X_2fgtQmsQUinJRDm6mvowjcGJ_n52BmjTsxhw1xrvnrtAhLMoPKuUJglvEQ0Lq9iNLVvL_DA8vqqgmb3p65ycbmJPR5W70q6oqDgaiGezXXrSVAGZ7KEDRmdrexwq6xRHwuP7p1R0wNrUECZMF4ByCbrlH5ebHSkWHEw-EOfosMbXj2YqsbZ19mUr_6_m2m2iRAw1uW4WMW3S4MsAAV1xuYyoWOCVt_ht-VhFbLwbK3VjTJeng-dbDUWfyfryVMUU9xJlHjjIdOqWuk5oOm1nnpDmH_xD3LGaQuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
نتایج بازی‌های امشب لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108646" target="_blank">📅 00:30 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108645">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCYhB2KQ7vSqvIn06AHlDdfTV8NQhvtvFtjShX2bS6h2n_3n4y34x7Y_0Vtu-Nq5nc_i0jNVl_KSXX9MMnrS4vUak2mQqfPsQWn1wTbjdbrBBZF3L8fNCbakdsAWocrrplu0m-Ib9DYtUE4h-Wfu20Z-_HWiFGeJtEefifCCOR0gBqwp4ICZ2UhWGrhaxR1riIhi5-uPMitXFOTbR1mJYwAizVuHkWvzqZfNPBBZBHp4fdQ7AuT3hveKHIx2p74SkglJzC7fIJwDcktaMMrBtgzSC_qPdVc0yVp3F23ZvDAl-lguSNTdtVFvYX5zbb6iJRUC6lyxs3FrDZmMNERp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | در همان ثانیه‌های ابتدایی غافلگیر شدند؛ وضعیت کریک در منچستریونایتد بحرانی شد
🇪🇸
اتلتیکومادرید
😀
-
😏
منچستریونایتد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108645" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108644">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2Oa2uToOu4WY5nGZSgO5juKjlfZULpJstMwHY6xw7ZFa6_lqjLajD7mjUsrkmeAp5h75sffjMru5Nk6rr0WYgdJTdpEcrBwPb-1aTMtYGBxoruWKHOJ-yUNXn14ryEwy0bpaJDByq6Yh75fy7dQpr8edEGtQijcUlBuY3f_uSyB3BtfQIfnbVhtWNkb6_crnzZWrNqyomjDmup0AKrgROKhIaxta5x7yrNEqfcN6l8-RO0HiRv0VNyjMMsYhaYs36SVhqTmamrkrnDi3LlJ0HkUavkYz5Kb5DpxiyggIwa6A_FEbA58XPrrRentUEXeyvklYVLnu4sK9kN47lHuYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ قهرمانان اروپا | تساوی دور از انتظار بایرن‌مونیخ مقابل نماینده نروژ؛ توقف شاگردان کمپانی در دیداری جذاب
🇳🇴
وایکینگ
😆
-
😆
بایرن‌مونیخ
🇩🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108644" target="_blank">📅 00:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108643">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_yUKpZsR4DimyjuZuo2McbUUOpFRKlDblHKjO1UpCvqzonBJOC_ld9WKTa11q7rjbFTjr_KKT5RjP-NKhBGkPiOZ1By-1WEtvNNNp5h9v73vl2EXHfVpjUdKoWchwosfMgAXznOlsZz4XyB4_MonSsC_vR2DHOGx04YKvMqFOVwga43hOASVtzpZxqc-zZXVX9pdqT8mjG_Kohia4s0VxAo6Fl5gfQkw4-3l8msMDzn7J-V-WWnHcb4XDQf9u_VpKHZkcw0K0_g93BR95wlJ2slxOypT034gqM4DZj_S0WZCLOT3q9RyG6A0wQGqD-T7yGIu5Pk5C2k3dYpe21ncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
🏆
هفته‌دوم لیگ‌قهرمانان اروپا؛ دهمین برد در دهمین بازی فصل؛ جهنم استانبول هم مانع پیروزی پرگل شاگردان فلیک نشد
🇪🇸
بارسلونا
😀
-
😃
گالاتاسرای
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108643" target="_blank">📅 00:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108642">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/def4417737.mp4?token=P8wZOF2eXKUJeSP1TOoWP-Eg5rpYmDuFMhmjYfglX1Oa05rENyPx8stDGbGOnCeLNtZ5SS_QLm_sr94kJbAIfyOcmraHfL84pNDK0qfM46fRLx3kwsWSmBLq5ZilTSs9LIRUuXTGFVtdUllbc-V8tKbcnLmdAkxcJ8CBhgG_ey5snD15rbY9Gd8TmNgwovoJOHSMchM7arBlg0bK6yEsPGD3InNyyy2UgycG5-n1icoCcR0rYt6i3sSvzC2V3aKu8maUyuu80nTCauq--JyYQOu41GbcFFHunDbSNFWRx4WGndB9Cix0al4lprmFmFazowS19NSBe20ABtdL9_MTxAg0xACWSP7__iIVNf0h6S4TOBmSvBDysS6NpvCtvthsxC4HKykec7dPYs5SGCuSLkPbr4-f6jsMWjZkEGIMGi_nZwlV8G5APByf5f8Qe1iBj7Fz5fo94xfVNVh1r_agsgdcR3jjm_TBUl_GN5OaUAPy2FSGGJ8CLFrKMqR3egtBXG-WPiVHqFO3u6IBhqvkCyQcsVdGpoagjP16u6pg6yDZlE5QFdrXsEcPX9QXTs7wlpcDEEWMzpwMQpyIbjDKvoLL2HfXkhl0iynSauvDLTTKCarT7OQABptmmJbL2tEmNNfn4kthAuSrfaT7gVqfKsTSR4CfW4n9yIisZq-EoMk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/def4417737.mp4?token=P8wZOF2eXKUJeSP1TOoWP-Eg5rpYmDuFMhmjYfglX1Oa05rENyPx8stDGbGOnCeLNtZ5SS_QLm_sr94kJbAIfyOcmraHfL84pNDK0qfM46fRLx3kwsWSmBLq5ZilTSs9LIRUuXTGFVtdUllbc-V8tKbcnLmdAkxcJ8CBhgG_ey5snD15rbY9Gd8TmNgwovoJOHSMchM7arBlg0bK6yEsPGD3InNyyy2UgycG5-n1icoCcR0rYt6i3sSvzC2V3aKu8maUyuu80nTCauq--JyYQOu41GbcFFHunDbSNFWRx4WGndB9Cix0al4lprmFmFazowS19NSBe20ABtdL9_MTxAg0xACWSP7__iIVNf0h6S4TOBmSvBDysS6NpvCtvthsxC4HKykec7dPYs5SGCuSLkPbr4-f6jsMWjZkEGIMGi_nZwlV8G5APByf5f8Qe1iBj7Fz5fo94xfVNVh1r_agsgdcR3jjm_TBUl_GN5OaUAPy2FSGGJ8CLFrKMqR3egtBXG-WPiVHqFO3u6IBhqvkCyQcsVdGpoagjP16u6pg6yDZlE5QFdrXsEcPX9QXTs7wlpcDEEWMzpwMQpyIbjDKvoLL2HfXkhl0iynSauvDLTTKCarT7OQABptmmJbL2tEmNNfn4kthAuSrfaT7gVqfKsTSR4CfW4n9yIisZq-EoMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ به وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108642" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108641">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">گلگلگل سوم وایکینگ‌ها به بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108641" target="_blank">📅 00:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108640">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=UR9idKo1CjnO-him7zIPwHAPOMjltTDftTaTTZBywvap4neMMGrVx5rcZKZhzlD2HI-BZELFOV7Mhtu0Dq_w8QqcFtXBsXMpip9OAJGEPUTk8vKPBLUJjsmmqbURevuQScKyPPHRZsVGfjybe_Zz23Oq3rcbOVuL9t3aRe4wv16QC0B0q5kW-3sh1sp5906TVNB1yfSTnsrjkSHlF1LKS9OSdZ762IyHs76knk_f1rM5tbsjZGsVGvclHw93pOroF7EkkmGZ-4JQsqHfnWDB6_2zPgF3gl4Sce61KI8AgXISR28z-v27J_-iMhHYcsDWlTAha5we0YtiokuStHC5vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abdfe06f9c.mp4?token=UR9idKo1CjnO-him7zIPwHAPOMjltTDftTaTTZBywvap4neMMGrVx5rcZKZhzlD2HI-BZELFOV7Mhtu0Dq_w8QqcFtXBsXMpip9OAJGEPUTk8vKPBLUJjsmmqbURevuQScKyPPHRZsVGfjybe_Zz23Oq3rcbOVuL9t3aRe4wv16QC0B0q5kW-3sh1sp5906TVNB1yfSTnsrjkSHlF1LKS9OSdZ762IyHs76knk_f1rM5tbsjZGsVGvclHw93pOroF7EkkmGZ-4JQsqHfnWDB6_2zPgF3gl4Sce61KI8AgXISR28z-v27J_-iMhHYcsDWlTAha5we0YtiokuStHC5vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم اتلتیکو مادرید به منچستر توسط لوکمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108640" target="_blank">📅 00:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108639">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">گلگلگگلگلگلگلگ اتلتیکومادرید دومیو زددددد</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108639" target="_blank">📅 00:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108638">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=b0bWEH1FgRsRXOewYj7Xn4PfuMDUxfLuXqmw1iRLUyM_q4FqAOkCRO8r5FZeRufd97Xp9q7_YMxrReLej1_ZJQQPPd8dYvh8Kwp8uMPY4R8TT8Au76qmyKPCh9kFYvE4EHMwKAgYc56itCB1hdkFxrsad86KU_YsUB6F5g0PtcKglTgFi56U70G7m7j3v-ZFtWe3cXWtQgXRbXhNYaTHqA2usUi_6pAXVN5bPhz3bcHEX_VCnQymJ8Bjduny_3gcSXpRh8RpsMQlPUIis8wHIPLq2498Ou8ljAkWhVWNynBSXBLhjVJz4zCt9ccBKnbWH6XhNbDHiynyg5Sl-vTdsIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d76e2a5b60.mp4?token=b0bWEH1FgRsRXOewYj7Xn4PfuMDUxfLuXqmw1iRLUyM_q4FqAOkCRO8r5FZeRufd97Xp9q7_YMxrReLej1_ZJQQPPd8dYvh8Kwp8uMPY4R8TT8Au76qmyKPCh9kFYvE4EHMwKAgYc56itCB1hdkFxrsad86KU_YsUB6F5g0PtcKglTgFi56U70G7m7j3v-ZFtWe3cXWtQgXRbXhNYaTHqA2usUi_6pAXVN5bPhz3bcHEX_VCnQymJ8Bjduny_3gcSXpRh8RpsMQlPUIis8wHIPLq2498Ou8ljAkWhVWNynBSXBLhjVJz4zCt9ccBKnbWH6XhNbDHiynyg5Sl-vTdsIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم بایرن‌مونیخ توسط لوئیز دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108638" target="_blank">📅 00:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108637">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🟥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لنی‌یورو جلو اتلتیکومادرید اخراج شد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108637" target="_blank">📅 00:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108636">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🟥
🇩🇪
مایکل اولیسه بدلیل دریافت کارت قرمز بازی هفته بعدی مقابل آرسنال رو از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108636" target="_blank">📅 00:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108635">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">گلگلگلگلگگلگلگل سوم بایرن مونیخ به وایکینگ‌ها</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108635" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108634">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=MwY5ZPOV0braHKqgVvaCrY2T8u3uNNeebSTFYBS5-wDJ8hQxqe9Fxd-fEfh3MWiNhuQWdw6sXP8HDb4XVMKzL74at_3mm9dcrOjIR3ZiPL988_W8qf77-i4_i4QDnb0qWo93D0HqaVY-Jh_2q2dctdWtSGWwGFcQDZ79sVNyxSwmnXZLe226HoNkzpQSdhXR813kGHz0Ck6-uNn6-7aHUrpFNLax88XGb5xEas9ByIqgHyZ-_S2h13z2sQ3KTft7T-iXOK3my4JfDtddqFJGyaN-qe7a-9OfUqkARoA4Sr_4yo-UZbQvDlV4beBzwNcFkLr6WQxWftRpMsEPENpGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99b2a48903.mp4?token=MwY5ZPOV0braHKqgVvaCrY2T8u3uNNeebSTFYBS5-wDJ8hQxqe9Fxd-fEfh3MWiNhuQWdw6sXP8HDb4XVMKzL74at_3mm9dcrOjIR3ZiPL988_W8qf77-i4_i4QDnb0qWo93D0HqaVY-Jh_2q2dctdWtSGWwGFcQDZ79sVNyxSwmnXZLe226HoNkzpQSdhXR813kGHz0Ck6-uNn6-7aHUrpFNLax88XGb5xEas9ByIqgHyZ-_S2h13z2sQ3KTft7T-iXOK3my4JfDtddqFJGyaN-qe7a-9OfUqkARoA4Sr_4yo-UZbQvDlV4beBzwNcFkLr6WQxWftRpMsEPENpGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌چهارم بارسلونا به گالاتاسرای توسط آدیمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108634" target="_blank">📅 23:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108633">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگلگگلگل سوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108633" target="_blank">📅 23:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108632">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پاس گل از گابریل ژسوس
🔥
🔥
🔥
😂</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108632" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108631">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">گل زیبای کریم آدیمیییییییییییی</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/108631" target="_blank">📅 23:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108630">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">گلگگلگلگلگلگگلگلگل چهارم بارساااااا</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108630" target="_blank">📅 23:55 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108629">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل دوم آرسنال به لیل</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/108629" target="_blank">📅 23:54 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108628">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_bSAi5kHyGuPs1zBMQDFTNRKeIPw9pkEygmHfbmWHaf2ho3gR2WS6I2PJearOLtYp8OawVGg4Kt4gFzbHAxVpN-fitc7fhBxxyt924GcXSvRaUVuCakZprS2xd7RPrd12ek0KPO43lq0LquOTFgTJP-PXyM8G158VVmfzjnHWcqNVel7GLWNTu8daL_mjH0tY2LSBIzjeSODJXxvLARzTOq4oGGDnN7E6xEBINIv15otia26lAw1Xo9zkW1ZhWHcRZteFvjJV80-6_GPd0e9Oq6FB2vi-iAqfmV0fMW2OW72ezuxp8hnsvkbrNdepzW4hh2vHjLlS6H4Uu97zjTMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
▶️
🇪🇺
نتایج بازی‌های تا این لحظه</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108628" target="_blank">📅 23:53 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108627">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
گلگلگلگگلگلگل آرسنال یکی به لیل زددددد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/108627" target="_blank">📅 23:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108626">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=CYzZ78STJf5WeRV1o-CUkjx0xsqlyCgfllSYJic2Gc3M4wHCXoXrIj96mFlhH5oXiJMLd2stkJry-EZO9DvoFAfFJ14f4lQJFVLu6_AOfn-jK2PD00hLQ7WeyLVq88UfqsjuZJMIdb3xUbzDKCUB8-ptouo5zZAtLj3ouCVGpszJZmVftD8r8vlsPBm00iC1IkMSiw7L7CMr88BZFZRg0QE3YjfzIf5PajdxD1HWWwm8Sc8elRNTj6A9pULXOP227vR4LnLJKUDoXCUzJqwuv_DwibalwCBLDY_MMcKxM5Slv-ndlM1vXCN40quY7xsidRq8_DHqt3WduzARxbWqISHq7EAvXGR-3sI1AFCOi593QZZYOEefHOpIpnuY_2o7xmTJQVD-G1VwrqYCHDL1I1TLVO78GfV50gyJ67ywLeEBVEEKY26EF5ltt8W12Mel3vRgWyb_2XnZbZXWRCL-adVsPQSNkd_jvTEfYQfGkVEI0X_V5A-JGBMe0zQD_RbKAahk6A88S4y4TfS7iq1va6HWsdEBgpd74vcZY2YrMuQhakNPbQGzc2UMtTm3oqW1IUBXyO-0V7dVi1KPnAa1Y2aeocpvtO5ORebhcQQg4i1y45OrTdwemP4Z5FoYNFch8fNsVfLQqnJ3GetfiIjBBCX9GTEk2VNXxQhWvktXKLk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cf53f669cc.mp4?token=CYzZ78STJf5WeRV1o-CUkjx0xsqlyCgfllSYJic2Gc3M4wHCXoXrIj96mFlhH5oXiJMLd2stkJry-EZO9DvoFAfFJ14f4lQJFVLu6_AOfn-jK2PD00hLQ7WeyLVq88UfqsjuZJMIdb3xUbzDKCUB8-ptouo5zZAtLj3ouCVGpszJZmVftD8r8vlsPBm00iC1IkMSiw7L7CMr88BZFZRg0QE3YjfzIf5PajdxD1HWWwm8Sc8elRNTj6A9pULXOP227vR4LnLJKUDoXCUzJqwuv_DwibalwCBLDY_MMcKxM5Slv-ndlM1vXCN40quY7xsidRq8_DHqt3WduzARxbWqISHq7EAvXGR-3sI1AFCOi593QZZYOEefHOpIpnuY_2o7xmTJQVD-G1VwrqYCHDL1I1TLVO78GfV50gyJ67ywLeEBVEEKY26EF5ltt8W12Mel3vRgWyb_2XnZbZXWRCL-adVsPQSNkd_jvTEfYQfGkVEI0X_V5A-JGBMe0zQD_RbKAahk6A88S4y4TfS7iq1va6HWsdEBgpd74vcZY2YrMuQhakNPbQGzc2UMtTm3oqW1IUBXyO-0V7dVi1KPnAa1Y2aeocpvtO5ORebhcQQg4i1y45OrTdwemP4Z5FoYNFch8fNsVfLQqnJ3GetfiIjBBCX9GTEk2VNXxQhWvktXKLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی بایرن‌مونیخ به وایکینگ‌ها هری کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/108626" target="_blank">📅 23:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108625">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/108625" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108624">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">لوووووویز دیازززززززز</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/108624" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108623">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلگلگگلگلگلگلگلگ سوم بایرن‌مونیخ</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/108623" target="_blank">📅 23:49 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108622">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هری کین دبل کرددددددد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/108622" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108621">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بایرن‌مونیخ مساویووووو زددددددد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/108621" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108620">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گلگلگلگگلگلگلگلگگل</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/108620" target="_blank">📅 23:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108619">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=HxaSCi8ualpr5S5hdT0qwqFV9HG7brZWE5CaW7KKBPz79vdhxgM3M2D5ZOiouul9TI0i2XRWo8N-Cn7_31LvMrzZwR9DeZ0SQC59iom1R8mlL_HOAx6QallS82wVBtadcIhnaTYL6ND7uOh8mw6ILQhruzivKBzXQwXbb68TUQf3F_q0GModm93jxV7TYqNg1-iid7oXnhEB4bAQ4UCmWoeAjivedyw4VBgPusYC0DuneAADmgY8aJaqB-xqFsU41dZ8Qzq0z3LWywaY0y8rCxCXBVCpjZEyofnpwhRFkpUWgcRgc56JkeePXBixC6WLsbceCNQQPBmNuTZ_H7LL_J2hMElyF_mpBNNDpJwqR3cFfSDY3pfTrLvjMwPnn9WTzIAq3JEiouE6EEUkaZ6L9O0b5vLXtv4bRTwVX7bZ5Bh1QY6nPvRQvmD_mF2GiWPWAm5qt9vxmpzn2WE6WTh550Cvyv_PZwKFNMm5D9L4nfVUcZTd6PjP37KPTNUSsiyXa86yfw6ledE6RJ7srcs2J9etT4nym35Ord1G_4PE0_EBLg_jcUkxlLCVLqRWW8X-_X-uTs6h86xOniN1RcAAuzh5g8DlnsFrdcgDTJEGfBG8SaocTIYMhPtVLpVmtZW5VQjxGSEnMMj80OEyAkRI34JBXlysDiwG3ykREDBVkj8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/93ba7eabbb.mp4?token=HxaSCi8ualpr5S5hdT0qwqFV9HG7brZWE5CaW7KKBPz79vdhxgM3M2D5ZOiouul9TI0i2XRWo8N-Cn7_31LvMrzZwR9DeZ0SQC59iom1R8mlL_HOAx6QallS82wVBtadcIhnaTYL6ND7uOh8mw6ILQhruzivKBzXQwXbb68TUQf3F_q0GModm93jxV7TYqNg1-iid7oXnhEB4bAQ4UCmWoeAjivedyw4VBgPusYC0DuneAADmgY8aJaqB-xqFsU41dZ8Qzq0z3LWywaY0y8rCxCXBVCpjZEyofnpwhRFkpUWgcRgc56JkeePXBixC6WLsbceCNQQPBmNuTZ_H7LL_J2hMElyF_mpBNNDpJwqR3cFfSDY3pfTrLvjMwPnn9WTzIAq3JEiouE6EEUkaZ6L9O0b5vLXtv4bRTwVX7bZ5Bh1QY6nPvRQvmD_mF2GiWPWAm5qt9vxmpzn2WE6WTh550Cvyv_PZwKFNMm5D9L4nfVUcZTd6PjP37KPTNUSsiyXa86yfw6ledE6RJ7srcs2J9etT4nym35Ord1G_4PE0_EBLg_jcUkxlLCVLqRWW8X-_X-uTs6h86xOniN1RcAAuzh5g8DlnsFrdcgDTJEGfBG8SaocTIYMhPtVLpVmtZW5VQjxGSEnMMj80OEyAkRI34JBXlysDiwG3ykREDBVkj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول بایرن‌مونیخ به وایکینگ‌ها توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/108619" target="_blank">📅 23:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108618">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=PbgdoaHQk14sYpgq1nxn8ml23ZBp3gkNmfUut_cXPRvIO4tO5rhc7KuOZxVYliPtSClUXat16uzqv6ZWtbWo8SFBHyzcQaEKu2sl-9XSJzW1Z9Ez524B8FZVpDYYknzabPGNrxpf_29G3hU7houbVe-wgoepwd3md3fsk0i6N6wz8Lh3uauPZM1_lw_4APC6Xp2m5-ciuchZ6IE2xhgysjewZpDUJXlnP9xG83-Zenqu5-zg9ZjymQddhtcXSaMSUPYA7rQIW7ksOlQ3TlCkHutYOqCasEXIGDeTFVQzJIG9VQqtkWsbWM7FsG-mMAY46_AanYoexPRjvPCUzKkypCNv8IbZqgYikU-5TuqVmforqBqSPvnZYVNkatKar62XI4JSl2IrSU5pOl1YcpXgWTpFuxmD-I9PoSe29tpAqPWcKU4Mh7pvzagFNYfjmbcJeoGNLrPrx1MXo5VlQmPQdzWjRalnVlAm0EkmWd0Z3xxR8Io9wvBOyG6SbUAIA4so8m42mmkchHZZiij2XBL7roLRdM4YWMM2MAAT9JoUno_RXF3MLlHnevTCoaiMCwh1LZ21H39hqH_dVJM7pRT4LXw6h8WDmRv70S0abPo72fNKzviNfGClfLGUjlvtp41DJSo07YVB9JFJ8VVCyZupDWZYNx7Al2Gg0BjvWXIaTfk" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c86178bbb0.mp4?token=PbgdoaHQk14sYpgq1nxn8ml23ZBp3gkNmfUut_cXPRvIO4tO5rhc7KuOZxVYliPtSClUXat16uzqv6ZWtbWo8SFBHyzcQaEKu2sl-9XSJzW1Z9Ez524B8FZVpDYYknzabPGNrxpf_29G3hU7houbVe-wgoepwd3md3fsk0i6N6wz8Lh3uauPZM1_lw_4APC6Xp2m5-ciuchZ6IE2xhgysjewZpDUJXlnP9xG83-Zenqu5-zg9ZjymQddhtcXSaMSUPYA7rQIW7ksOlQ3TlCkHutYOqCasEXIGDeTFVQzJIG9VQqtkWsbWM7FsG-mMAY46_AanYoexPRjvPCUzKkypCNv8IbZqgYikU-5TuqVmforqBqSPvnZYVNkatKar62XI4JSl2IrSU5pOl1YcpXgWTpFuxmD-I9PoSe29tpAqPWcKU4Mh7pvzagFNYfjmbcJeoGNLrPrx1MXo5VlQmPQdzWjRalnVlAm0EkmWd0Z3xxR8Io9wvBOyG6SbUAIA4so8m42mmkchHZZiij2XBL7roLRdM4YWMM2MAAT9JoUno_RXF3MLlHnevTCoaiMCwh1LZ21H39hqH_dVJM7pRT4LXw6h8WDmRv70S0abPo72fNKzviNfGClfLGUjlvtp41DJSo07YVB9JFJ8VVCyZupDWZYNx7Al2Gg0BjvWXIaTfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌سوم بارسلونا به گالاتاسرای توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108618" target="_blank">📅 23:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108617">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c2159385.mp4?token=ZQme4jGoA2KpnA5Ey90lvKverzDynLHWARtDy_tCTn_JPYQWyOoaynn9shlb12o3xA_pZaZJdJRuf6NUBKbZM508Y8VmZrzrdYPfXQncVabf4-SZjZuMZTVDVJAvxs1lAfSy5W0t5oN-wMNGmCUE8X7r91IaDKplxJAN1ePnW9-0bsdRQdFZPCFgD4sV2RdydrxUZAlzCOI7tQuhP9nWq1Wxhga1sYdaAmbVZU9qWJqtvSuhF9lz3u1ckeN6zmL_ccNIR0xGPsYqt4Lrc9s1kiRZz7RKyxNps6q0ShWhKX5aYay6gf9G4yWJa7MKQDCjkbYMDIz_hoDSYHs-DbHN7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c2159385.mp4?token=ZQme4jGoA2KpnA5Ey90lvKverzDynLHWARtDy_tCTn_JPYQWyOoaynn9shlb12o3xA_pZaZJdJRuf6NUBKbZM508Y8VmZrzrdYPfXQncVabf4-SZjZuMZTVDVJAvxs1lAfSy5W0t5oN-wMNGmCUE8X7r91IaDKplxJAN1ePnW9-0bsdRQdFZPCFgD4sV2RdydrxUZAlzCOI7tQuhP9nWq1Wxhga1sYdaAmbVZU9qWJqtvSuhF9lz3u1ckeN6zmL_ccNIR0xGPsYqt4Lrc9s1kiRZz7RKyxNps6q0ShWhKX5aYay6gf9G4yWJa7MKQDCjkbYMDIz_hoDSYHs-DbHN7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم بارسلونا به گالاتاسرای توسط لوپز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108617" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108616">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سوپر دریبل و حرکت فوق‌العاده یامال فقط
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108616" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108615">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آنتونی گوردون</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/108615" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108614">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بارسلوناااااااا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108614" target="_blank">📅 23:44 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108613">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگ سوووووووم</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/108613" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108612">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گلگلگگلگلگگگل بایرن‌مونیخ یکی زد هری کین</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/108612" target="_blank">📅 23:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108610">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سوپر پاس گل لامین‌یامال
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108610" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108609">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فرمین لوووووپزززززز</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/108609" target="_blank">📅 23:41 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
