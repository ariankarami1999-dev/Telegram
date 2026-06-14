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
<img src="https://cdn5.telesco.pe/file/gNNVh2833jllNBAAH0LtGceiQcALpzka1QtHFEjyV2-vEJydTmamlHEyCM4cWvCzGzfPZROuz29eXgqDhzrBDAt_EeGVWUFJ8Za8-uBiExI8_oaAaS-DnjZaOIzumN-DCI8oi03mS2fymuFA_itAzKqDNGDXc_gqKbPNJ97heZ03tq4NhSQeSIbiTVDDfY5zFnA0rCiu1rxZWfvx4R58G-ntJbB02j5ev6sxDuG4UWiOAGa14KOcQ_U6cd5ywP5eugl11OuUwU-1Gou5u1SU1lMuids4XdZz5x1tlNWe9XIVGe72ueAJz3MotP7TDt1YyIjtK3o6D3hrIgu5Mr0OiA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 535K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 18:06:42</div>
<hr>

<div class="tg-post" id="msg-92928">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پایان ست اول والیبال
🇧🇪
بلژیک
1⃣
| 25
🇮🇷
ایران
0⃣
| 23
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/92928" target="_blank">📅 18:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92927">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🙂
‼️
🏆
یه هوادار ایرانی بلند شده رفته تو مکزیک و از خودش ویدیو گرفته. نزدیک بود زیر دست و پا خفه بشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/Futball180TV/92927" target="_blank">📅 17:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92925">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNFKT-jyKjJMMgSMjmMXzfZ0Fd8YpP7MvUWr50fwjJXUZUOz1Zy06xWopZRp9S7Te1mLZhIB5k8HkXo6IdLTIz4WPaKPOIVONZNKhEBeECmR7KA7Vu4DEz0LtCtAbF8cBQmxiDkeHS4_9hBMzIETNuhfwnFlclrY3V-MkJE2UfxIaq46A-WcXhnIvi9cXdaxIxFFJ6tl6Fw8r2hzJvqF36HBmioZ6RuiJUOhgoxES5lob3_U0M-Zs9cfHKJOrwUk4-WCN3733jKapM1ocPdAVqNYxezMGHcQO75DoX0JKW_NWpupxYudFucS4fIteuEUNQbeGUsL8Uw7cUu8_Hi_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bab5S1oB9zeV5MM6CnxuY4g38gbbSwJ2z8IFCUS-xxkPJYURBoYRzeMh-ux2GbNpqVbx6qJWhsfm1i0F4PYClsWd0XmRiqP7vq_NR91pKfnyNWag4Hvn8pjcUOItaof5mlvSgihvvuwDJnEpP3v7b4Sqffk9ltlzJrMfQapZko-WfjSayIIQ_1oSDmos0VpXvOHewVOP15YsKi1P1nyjei0H7laItg99mWAjlAlRzCOdfMIBDmCO4v1N7Mj5hNZ5blbPY8v_2syCr-RFxw1JnN1QbCk3sIP44sE0TlRVhUtFKfmy1Wr0f7kJ2VF8BY5UVadHgLa8sjCYFIIGExGHqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا در بارسلونا
⚽️
رافینیا در تیم ملی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/Futball180TV/92925" target="_blank">📅 17:53 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92924">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUTEE-1VYYcGw6EmU0GglQecT8VI8mgeaSaxmcvFhB6eVWwUkG1Cat72L-II48Zbs4TcpC0E59bfL5JYY67yg080YJcDQVr0UiX2Xu0tIn4qormbuuv6XKOqVs9kJuC0LDtePsuZuWKQmHWdEvB2MsSSNtIxKtrtrOkwSM2qB3PuOD2P4SkL_r9nRG0pvUEXV-x_kDJBO2C1UbpFWfnMGKt5i2RWXwMG1UCOPGLy5840wyleKfuiRZZz1YQ2u0GuCwlp9aLheP0e46df4SYBRbjvij36CNUx3dShj1shZUaulOM8m32HDjYxIMDQrRoAK3ISdGNxHJPD5C2EBi0V6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
🏆
رسانه‌های‌مکزیکی گفتن که یه پدر در مراسم افتتاحیه جام‌جهانی دخترش رو بین جمعیت گم میکنه و با نشون دادن عکس دخترش به مردم سعی داشته پیداش کنه اما تا امروز موفق نشده. ظاهرا احتمال آدم‌ربایی طبق گزارش پلیس مکزیک زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/92924" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92923">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MbveW6XmyFoYSwRrF4-LP-o6BMNCjnDfIwUD96LNWQWwL7tEPa51F7BzfV7TKbnurlZb7Ajy-KAx6wZo57t4PeDXq-89rmEdRYMDFawWKgbtRrnuop8gaLGho8L8hh7Xk1lhM0cadpCHvwePG1rkT4_Ydr-kDMTyg1L-F4vdhDVIx9XBHn0uXclZmOeZvPOZ_h_8HHgGdNcvOh8jPDiWrj8xYfV6P9N_azkW0zot2YvoirokJu0tg_dQajtpwCqvRWZ7MvWEBcJxYGGh8_VdTFjPPFSZ8VNMx-O7gLrOoDhBm8mWGfyOgWh4PP8SY4HJJpauD1QvCTOeR8L1rPh5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یورگن کلینزمن درباره قهرمان جام جهانی:
اسپانیا تیم مورد علاقه‌ست، اما آنچلوتی برزیل رو قهرمان خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/92923" target="_blank">📅 17:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92921">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9y4OK6yN1fVHQLXkRiHDcwRENfJU7a_hpyoIuzT39o5Cdu4brhh1ou6cOdmtDfF3kzBHZTdaBuz_xutHaG7FlBXsKmzHGOCtEyAAIhZftjOxhwLkOWK09o_p2z_q5TGkmPrpyZi8JdJNje3f_6xl399d8bgeiwKhZR0UxtdqaFLrvP1iBgpv3LjqmlTibdGNNZZqagwO1O7-4IObpewGwRdUFxb5TKOi-2WCxW0q3dsx8jHbpxRybuBGLEFFGMXCYRG5YYjSgXX2Y0msEEsQ2VGD1jAaNkRES206oAmWM_Z-q49qUevLrTQCbtO3p6NkBSYewZbV4JWjC7AtvU3mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/Futball180TV/92921" target="_blank">📅 17:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92920">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b3d55458.mp4?token=SPGB4JzStTflFKvKwTE_PSWWCokAOWOLQyweKBfuE6WzE_XSdqXn32cHwC0nyreLJE7hcttihU72tpVcm7sx9BuKjPXG4qyM_63_Y8wK1a_0IzmzRKjbAGCk94WKtL20W8nlCnzDTo-YVdUiVY4WK-I76YPbY3cAahYDXRvex7Hp1FTsUYR8foE_4Iqb2yP3rEOs8vZWfEfRq_IxCXB14KWUoeE4QQVFxIjtjLsmCOw5TwoK2Sv8IBTXL-SsGZUILPQPGT_KVQ9hO3vBYGoSsOPsYEqcv5MbgCqQj5VP6YG01nMn9x5EjH1t96oYedXRQ3ZoRGZvcXCqqkQUuBFT_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b3d55458.mp4?token=SPGB4JzStTflFKvKwTE_PSWWCokAOWOLQyweKBfuE6WzE_XSdqXn32cHwC0nyreLJE7hcttihU72tpVcm7sx9BuKjPXG4qyM_63_Y8wK1a_0IzmzRKjbAGCk94WKtL20W8nlCnzDTo-YVdUiVY4WK-I76YPbY3cAahYDXRvex7Hp1FTsUYR8foE_4Iqb2yP3rEOs8vZWfEfRq_IxCXB14KWUoeE4QQVFxIjtjLsmCOw5TwoK2Sv8IBTXL-SsGZUILPQPGT_KVQ9hO3vBYGoSsOPsYEqcv5MbgCqQj5VP6YG01nMn9x5EjH1t96oYedXRQ3ZoRGZvcXCqqkQUuBFT_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صف‌طویل عکاسان بازی برزیل برای ثبت‌قاب از نیمار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/92920" target="_blank">📅 17:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92919">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXtotUCceVUYfSXPrsmXCc92dbNJRsClWKBJYksO486rL9xCqgBlDycIYj1jLESGSwOEYqaKNUuO0fQj7wVdC0DHt2W773jrISJP_LuOlB-ltU_IPBcXbwb1suSt9wFS0w84uEhRHHlKPWOoNARwkpIUV9rM73eSBph9yAtO1kXw-4N7QvS7MoQBfadE06yr5-Hgu7qyrc1sCI4OPVRrPwtmBYq9bRVav9xneup6NvQccaTO50zjfVKdkP7IVEjQI30Jh90RQU48zgOSFlye6pqQF6h-BEDTY4S3Yxaqc-TxgaOBtrczQcdVqfCTLZVPGhB1dHCiVeQqmxRQUFrb7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم‌ملی والیبال مقابل بلژیک؛ ساعت 17:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/92919" target="_blank">📅 17:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92918">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🇧🇪
رودی گارسیا سرمربی بلژیک:
⏺
تو هر بازی ۲ ۳ گل میزنیم و اول صعود میکنیم
🍿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/92918" target="_blank">📅 17:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92917">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae33cfeb0a.mp4?token=Teg1wDoULCnGN0XZeJ0Fh96K_j5OL2ErTLYKVJrTiNSmdMC2LspQmZAF3zDr6oQ7vBCtU3Q07KN9lEv0UWyRaGyNgtg2Lp-3ua4MP2s3b3N7_H9eL49Wgy1n6p1qX4TXTILIxJZGN_Pu7nbrk19fDjqnfLjGNvi1xpJmtzweuyVNXJI_d8hYD4C_FcGmkY91lm7_0FJvlmhGa5Uye2VK6_UB5kCey4-aTyK62JwX8-ElfTZmKKrAFfsOxWcNbURK9infPQTmwEGPuxzk47pljIj_DWgErIiDotha_FMEPZIMYoUTVuAhdnpCRp3Drz0bLWUcZbS_77FeemwhU5VmIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae33cfeb0a.mp4?token=Teg1wDoULCnGN0XZeJ0Fh96K_j5OL2ErTLYKVJrTiNSmdMC2LspQmZAF3zDr6oQ7vBCtU3Q07KN9lEv0UWyRaGyNgtg2Lp-3ua4MP2s3b3N7_H9eL49Wgy1n6p1qX4TXTILIxJZGN_Pu7nbrk19fDjqnfLjGNvi1xpJmtzweuyVNXJI_d8hYD4C_FcGmkY91lm7_0FJvlmhGa5Uye2VK6_UB5kCey4-aTyK62JwX8-ElfTZmKKrAFfsOxWcNbURK9infPQTmwEGPuxzk47pljIj_DWgErIiDotha_FMEPZIMYoUTVuAhdnpCRp3Drz0bLWUcZbS_77FeemwhU5VmIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇰🇷
هوادار کره‌ای و دوس‌دخترش در مکزیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/92917" target="_blank">📅 17:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92916">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c830c9efc.mp4?token=J4nJ1HacuRWoqqRjpaSx4At3jcOIHNA23UKbcWZ-ld6EVyYBvLDOXGHYZJS66DymD9M7E2uAI3zsILgrQPZaC0p96L2ZzS1kXS_niDStls9qrQGAUrYXQ6sBSnKyOwh1VCYm_Yn8bifDH34ewxcD2oyM-2m1Wje0d4LOwEmi5zkkhdnwMNjdxVh2yr5KpeRNAXMBAV8oNh3gZfxyeomFIOeZJe0l4rO6IHkh5kQ5W9yd33PgVbP3hB0xL34fH06T9hDWlAYjGaiGyq3j2rPmP3uBi3VV0ko8rU_y1nGHx_NQ-Mg7LTMsm5R2_5531t-DZQD1wNOyYMsvdIYd86Vuyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c830c9efc.mp4?token=J4nJ1HacuRWoqqRjpaSx4At3jcOIHNA23UKbcWZ-ld6EVyYBvLDOXGHYZJS66DymD9M7E2uAI3zsILgrQPZaC0p96L2ZzS1kXS_niDStls9qrQGAUrYXQ6sBSnKyOwh1VCYm_Yn8bifDH34ewxcD2oyM-2m1Wje0d4LOwEmi5zkkhdnwMNjdxVh2yr5KpeRNAXMBAV8oNh3gZfxyeomFIOeZJe0l4rO6IHkh5kQ5W9yd33PgVbP3hB0xL34fH06T9hDWlAYjGaiGyq3j2rPmP3uBi3VV0ko8rU_y1nGHx_NQ-Mg7LTMsm5R2_5531t-DZQD1wNOyYMsvdIYd86Vuyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
این‌بخش از برنامه ابوطالب که حسابی وایرال شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/92916" target="_blank">📅 16:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92915">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f7f647c15.mp4?token=kp7XR2soFPxBG65pHrfQIfDW_V-pnL5cRjpwCgYouA_BXB_aLWxUDnq0N6a-h_g0iRsK7gN9tXmYV0vmK2osggp0fiRY-QTdvjko1h2opI1zIirm9dJduf-iIV_OmbnKapH_JfpnZylDkqFzHQBSLo8Nry3JBNzcDlXaEchZAXElRU2SV40rj9NMnpSvS5c3nOiiqnptJE0I4Pjw3G7v7-MySjJSm4w8eWv6M1zSmsXh8eJ0EmDTA5re0dcKy7_toDgIQLaywOcx9w72WCC6hHEE3GCF_k-wQa4DzVoXyoi-5N-6JtwFl8ZGexxCk-sK8cOvU2fT7fGNsrKy9O9qeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f7f647c15.mp4?token=kp7XR2soFPxBG65pHrfQIfDW_V-pnL5cRjpwCgYouA_BXB_aLWxUDnq0N6a-h_g0iRsK7gN9tXmYV0vmK2osggp0fiRY-QTdvjko1h2opI1zIirm9dJduf-iIV_OmbnKapH_JfpnZylDkqFzHQBSLo8Nry3JBNzcDlXaEchZAXElRU2SV40rj9NMnpSvS5c3nOiiqnptJE0I4Pjw3G7v7-MySjJSm4w8eWv6M1zSmsXh8eJ0EmDTA5re0dcKy7_toDgIQLaywOcx9w72WCC6hHEE3GCF_k-wQa4DzVoXyoi-5N-6JtwFl8ZGexxCk-sK8cOvU2fT7fGNsrKy9O9qeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
دیویس رفته توی خیابونای کانادا یه دوری بزنه و با یکی روبرو میشه که کیت کانادا با اسم دیویس رو پوشیده. بعد جالبه وقتی باهاش روبرو شد تخمشم نبود و طرف اصلا نمیدونست دیویس کی هست :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/92915" target="_blank">📅 16:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92914">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efae1e173c.mp4?token=mmjDQFveeYEI1lRmZm8Y4WZ7ljiaDd-YFIwCltlymq1Koa8uKUd_KkhgQHVqcmOpWynKB5ORrM0qzGe_FzekYtfpr95guswtEV1ya5MrpFJECN8lGhEmO9Vo-ilidKL3f8PjNiUTfVrSsHuZ9Vo_zmmByHe-0ZYjc5PczmznyqcdrY8SieegprXuj80HTGFAON19FVLcD6V-W23nRixx9RFvnF99MtR414JnQNS4Fd77GW4R6Vy1NZJNnBafnv_chS4-3pThGBb6JlI3SThyKG4SSt0xXzrP_7__BiPm69gPz-kK8sNsjlYpSUlE33UrsFXphXSTHsRfAbEVcfx8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efae1e173c.mp4?token=mmjDQFveeYEI1lRmZm8Y4WZ7ljiaDd-YFIwCltlymq1Koa8uKUd_KkhgQHVqcmOpWynKB5ORrM0qzGe_FzekYtfpr95guswtEV1ya5MrpFJECN8lGhEmO9Vo-ilidKL3f8PjNiUTfVrSsHuZ9Vo_zmmByHe-0ZYjc5PczmznyqcdrY8SieegprXuj80HTGFAON19FVLcD6V-W23nRixx9RFvnF99MtR414JnQNS4Fd77GW4R6Vy1NZJNnBafnv_chS4-3pThGBb6JlI3SThyKG4SSt0xXzrP_7__BiPm69gPz-kK8sNsjlYpSUlE33UrsFXphXSTHsRfAbEVcfx8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از جام‌جهانی ۲۰۱۸ تا ۲۰۲۶؛ تفاوت از زمین تا آسمان...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/92914" target="_blank">📅 16:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92913">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
فووووری قالیباف: پس از چراغ سبز آمریکا به رژیم برای تجاوز به ضاحیه، سخن گفتن از ادامه مسیر ممکن نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/92913" target="_blank">📅 16:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92912">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bc_11qxmLaM7YNPGyxt_4Dc5zXjaQ7D7yoXFmWMbXHSfasnzahnfeHSLDKvo7L8RRsuTUAkQmi78vlcUCfXGzFLzwQ_LvNv9dbt21kTvQGpga-ILf3dtL8S9D61xb4w1AC4Hl8c9OVy_nI8mm0ic3x71T-t5_y-ZglFzfedi7ZSlnF68xEckNDhCax9DMHrheDUFLA7QfG_CjoZluS6Xix8FQen-3_9Dc8JWu2IaE8WiUxs5AyE4dtuzxbxuOgd-3LtpIefd4QtWKHlCxzIqaAwot6wOCOQeEva-yODWPbMWTd2rexXaUlzzTMUd_Z6l9aHVfVfKDeuVUEl0_Y6OGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی که از این بانو شدیدا وایرال شده و همه اعتقاد دارن تا اینجا زیباترین صحنه جام‌جهانیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92912" target="_blank">📅 16:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92911">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgLxm0DbL97iX2O3NqruuIwa15-HX4AhUdUVUXpUvwE0P0KoIZc_2PFTqIodmF20eBTa9d-AcGkOUUfMdgxgSRTJ5wXtYyJoyT_xqyYaknyc43MW1tu2z5ebtqMtQGsSxyhFWElztuXmT8RpCLDk0N7pldTaNS4XtAhNlz_O-UfzS1Xn2Pph3KBNuNUXfGMH9S7a7UjvPw3ivTrBHewTRHpIvL-JP5eU9jTOSQBU0YNljhqBmbyGzWPiRjIgSmCr5GyCU3lDPM7Cp_OioPVmSW05dqvcPAJMSU_adGjvHYJfkNdc-WhxXaX6y0_yQgNcYmxpC8w2uxxZCpBIwHznDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
تموم بازیکنان پرتغال دستبندی از نخست‌وزیر پرتغال، دریافت کردن که نام دیگو ژوتا و تمام بازیکنان پرتغال در جام جهانی روی آن حک شده است.
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/92911" target="_blank">📅 16:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92910">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/173f746cf4.mp4?token=dxryGLcvhPp-rCvEOUuR22iqiOvjAhGwM5qWrGG_4s0OklD-YzzRl1363vFMy5kvSB7VPaScsALeBHRcnokt2Tu2R7nNvco9SnTt0DeR3lXDTDKwn8fq4B8VXz73TRvsPsvLZW1u5SmjuB3iP8a9j0PbLLv4iK7Ek5317S-WZAib5rYoLVI0Yhq4GhYQ2oNNgSHheLYSW7zvqS4eCOUAOKhdvDLMP1KxNRmbnlNqYqJJE3WxN4LlK04RY0XBS7glXa3ElAFqqmY3XKC1u67Ny75AW6JN1LsMvu5gfB6PG5DMDtxnImVbk0PqophUPj5IqESUO5pDCQ7XyhZMIQB7Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/173f746cf4.mp4?token=dxryGLcvhPp-rCvEOUuR22iqiOvjAhGwM5qWrGG_4s0OklD-YzzRl1363vFMy5kvSB7VPaScsALeBHRcnokt2Tu2R7nNvco9SnTt0DeR3lXDTDKwn8fq4B8VXz73TRvsPsvLZW1u5SmjuB3iP8a9j0PbLLv4iK7Ek5317S-WZAib5rYoLVI0Yhq4GhYQ2oNNgSHheLYSW7zvqS4eCOUAOKhdvDLMP1KxNRmbnlNqYqJJE3WxN4LlK04RY0XBS7glXa3ElAFqqmY3XKC1u67Ny75AW6JN1LsMvu5gfB6PG5DMDtxnImVbk0PqophUPj5IqESUO5pDCQ7XyhZMIQB7Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره دردناک و ناراحت کننده کانسلو از مادر و برادرش…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/92910" target="_blank">📅 16:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92909">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMsCYu498yGow3TFhlA8t4MlkJ-sotSwqSJFM9y0sBH7YBmMFJlNpe6mhusAtgF_socQtEGnEBQ0KtXsYT5U2LnQj3QF_harUYVz70rxtWcbHqgDJgGjowyuAgvGgmgWe7InzPMXvyFRkjV2oEO4O__nhrV-aCwzaJ8NQ8qly1Y0F-YZ8QNb-jwucCA4NmuycGU8JhyE1NwOF5Uwe1cvjlVEshQZPlRFD1yJX4nNfqJ9ou_D1Y07_ecUSwcgR5fyOK41k5jA_DWfz4SCiYEMcEJgQIRatO6NkiNvJdR6WrgXq70EVDRJl4EPsCMHJvGXWmLjNpeSIKG4JQrFSnOfHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایوب بوادی 8 سال پیش، بازی ایران و مراکش‌
حالا اون دیشب تو جام جهانی مقابل برزیل بازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/92909" target="_blank">📅 15:59 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92908">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugrsTagSvW2_id964jOqZAqA3lBj0UqsIoJwF6a4FdG6TmJ4fDJO8IXLeBcx1xduLwvH5r83x_WczFprGOrDeKAvjjobCBLu90URhlSrzTICWrYX7Lf7aGR1UCuABsdwjT4x5YdZLVjV7u7qlZC2ZT7FJQ-Mz7dGtg34kFmhunOPMmO9SDeOYzV4GEnyiEWV-pI5rwFJXpowQSW_sBVEvlaK10A0uj9eswekCfmWN1IkVQ9PvaBfGQbrmyStj0Vurjv9OFYlbm2oI7jjUVxSNhUQTD5RK_Ssyy4XNTZd-IZEpqMaRkxMsNyZnE_Bs2eBEv48JiR5w7QQr_E8ACVisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ادعای اسپورت کرواسی:
گوارديول قراردادش را با منچسترسیتی تا سال ۲۰۳۲ تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/92908" target="_blank">📅 15:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92907">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/431d2a83b7.mp4?token=nfLgBW8Z8tRWnlIaqAAsYsFoyLeVn0GKpp-uYIHK58T9_PRItvNZxBENzMwpJoYF1xsyAIOtAX0d7vpxZgaYmpp4DTEp71hqXx2ULdN6c7CO3TvsZRat9pYVGcgwh4k5c2aHiiISlWQzWrLB1-aPsKZgXhEgixmQgi3siPSqFMLdlDfnQxhv4Jo_Mh9d9aFxN7Qxi5W6bkJvaq8z_hR6Tm9bLUUn5hw0UiFaCycZ2KWIkW6FgSG0-xmJvs6aFJVQvg6t0yZlbEK6k9Y4KixI5RVhh3mWU5gdwFoMiOxsQgT85ki-qcrpor2R86yw3Bl55tufzSsxs6_F_Drbs0a9ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/431d2a83b7.mp4?token=nfLgBW8Z8tRWnlIaqAAsYsFoyLeVn0GKpp-uYIHK58T9_PRItvNZxBENzMwpJoYF1xsyAIOtAX0d7vpxZgaYmpp4DTEp71hqXx2ULdN6c7CO3TvsZRat9pYVGcgwh4k5c2aHiiISlWQzWrLB1-aPsKZgXhEgixmQgi3siPSqFMLdlDfnQxhv4Jo_Mh9d9aFxN7Qxi5W6bkJvaq8z_hR6Tm9bLUUn5hw0UiFaCycZ2KWIkW6FgSG0-xmJvs6aFJVQvg6t0yZlbEK6k9Y4KixI5RVhh3mWU5gdwFoMiOxsQgT85ki-qcrpor2R86yw3Bl55tufzSsxs6_F_Drbs0a9ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ماموران امنیتی جام‌جهانی یه لول خاصن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/92907" target="_blank">📅 15:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92904">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r26IGMYJ0r9yB042oARR2C_el8-8pSmjrKFSKDM5VFjUXI50mu3T3M2ylZpvVUPBDQwOuu1tMVY0ch7htJODWpy7okOVslyIOdhbJWTfq1IeiYaAl5HBOwb3RDcKzPeNsAEzC7OM4Q061y0R609QKbvZx06ay9mN8A9eBk9DJIym8qrrgxI0ThBt5KIbWQN-mD7K4ZiZ7Py_afY5GAhmm3gEHJzh8s542KZPgGcpLDNRnAVHJxjxGg3WHZZan1XwuLv8S142mscJEfk_rf_sHVUqknzetS25YGfsFhQqlJl5KmbgE1Xmfbgo160fMdjCwBNh2u1yGrmNe61pSMvUZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AkPKD8Lj_OFz6GKr5qXNlSawMzyicvx05w9KBFja9ok1rrNiEfd0W6HSzYR1LqczIR2iDFPb-o2ILEQjsZ7W56y3d1UuwMOwjJ8nB2-x5tcMf58PUUjq9xfAv8-3u8Sw2yE9WiJqRNq6Tp4UpdaDS1WEArJ0nwq9JYOxttmKddIFWuhTzHtC3hTLUm2NPdBXqZmZh0K4Si_Gt889yv-OEuOPJlriKmlFVre_iSacZwUnfX04YrBcAYsoQrMrEYmCpg4gE_88qbbAvesz2gCLPsCFK2xFGDGUIvEOyh0TIYbR3ZRSeT7_i4DPZ7cYRdMa76GzL-dVVw3jvv5xg1uQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oW40gRVayyRJSdZ4GOFBOU_fax1LNggcLAhiWHdZQFWYMH3T9xxpJPlipa2A2aCd8W5Swru0jZiXGT5uWs_PZaanfLQMZvQM5jMOZgINUABkzXYFD-JntVlqwXkrnsDbI76lTJosFmNMAPveB_mkFWyaH6KrLihdHhNa-in6kcpV3Fa19XfO5gix7ValKX6wBp89hBowR0dG7tmuHk6Oagqnb3YRHNY5NSKvupmOLTeAS0JG_1vhKUGgoIuYhHhMKvyUp5eqt6wPA3gxc3iW3nCQrbnVStFu7_dm1tamdusIBmF7UkWJWmX2apJMhqHNgtK9Flsw4A-pfDBkEFEwNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور بانو ویرجینیا در استادیوم بعد از آشتی با وینیسیوس
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/92904" target="_blank">📅 15:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92903">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20da7b34f9.mp4?token=S-9-7RcqzCdEFDrRoCsa6L3S4hZ48se3IYPnKdLNmB01eo4J0bxzHCjEkKBymzbLgjWL-lQwEsStjoXPg9a5lLKbUfYIG1SKfqSyXYepYzlYgmjUWC24MHZX3E1HV4W79fSnQ2YfMbuX_DFoiu585fG5wwajUqSivlci-Pg7B87JfwC_Xh0xMSHQq8eTYGJFnJb1VSwWbqH2LPcqIHmtSeIj1dVJQBDb-gyncqR1m4jZdA9aexeJFVUtjzAy8OTSdeJ_0IWV0CJ_pJo28IzltiexAk2Dblitr83dWJzyN2fuvIsDOaITtSY2HT2nLK8KP4_gqvYPtmIjlJQdEHW-eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20da7b34f9.mp4?token=S-9-7RcqzCdEFDrRoCsa6L3S4hZ48se3IYPnKdLNmB01eo4J0bxzHCjEkKBymzbLgjWL-lQwEsStjoXPg9a5lLKbUfYIG1SKfqSyXYepYzlYgmjUWC24MHZX3E1HV4W79fSnQ2YfMbuX_DFoiu585fG5wwajUqSivlci-Pg7B87JfwC_Xh0xMSHQq8eTYGJFnJb1VSwWbqH2LPcqIHmtSeIj1dVJQBDb-gyncqR1m4jZdA9aexeJFVUtjzAy8OTSdeJ_0IWV0CJ_pJo28IzltiexAk2Dblitr83dWJzyN2fuvIsDOaITtSY2HT2nLK8KP4_gqvYPtmIjlJQdEHW-eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیح پیرس مورگان از برتری مارادونا نسبت به مسی و پاسخ جالب جان تری از تجربه بازی مقابل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/92903" target="_blank">📅 15:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92902">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc3493e5a4.mp4?token=jhRPJAYz7wDg49BIati8kIfHXl-rqa1DHEbejTYha-Dqg5oQK5aFChATMZSdADZkT8yogd_gwrRKGNQihEFv79bccRtDmL6jj6N8vPzFM02vIkzAbgcRmTM33mvYYXhzgWmZy3K6iF1oAe_hxW_Bk-rAF3UN2FBS5FTvr8Q40nTivffKwIFpVyruJ5PgrrHO8NFSb0h5IZJSGXWR09O3sIWiGeBA000txMSD2-em1d2k6Xj6bHVSrhdiwxpEgWNLgmS6r8uLXSWiA_OJSVXE5wAVGFcNHK6BifplSQ2TSM2R0AvzQ_tjCW7gM3Bu1fYHuopU1F8n5ZMV8YwJJ0UVmJSQ0nbX6Rew7tdYeIAMX6oUWVdMx3xi9Ptc1Hxfe21M3thrviungdvuP2d2FSNUyV_C6tvhBxFzdE_j8-I2c3j2lNJrRMrTIwHHCMVd9KscyqyvcBRtBCzU2zcEspXVNjl5FfeDqNvzszKbWe3XSagZv6APkdOVIGmpMqnpYKnfTNRENjQ9VaxT3BZmMPOvokVmmspnQDoK-GSfMnar-w5dnb5OiSKbe3ki1BdMoHFPgdxiXR3-8x3-HSjNhSmF8g34ZeciGtetamCoATm2qJuiF0f3iuUfvwl77kS3YLCJuVfFndmnQmpth3kCyzmSeC8jN03rwccZb5trqKCK-Mo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc3493e5a4.mp4?token=jhRPJAYz7wDg49BIati8kIfHXl-rqa1DHEbejTYha-Dqg5oQK5aFChATMZSdADZkT8yogd_gwrRKGNQihEFv79bccRtDmL6jj6N8vPzFM02vIkzAbgcRmTM33mvYYXhzgWmZy3K6iF1oAe_hxW_Bk-rAF3UN2FBS5FTvr8Q40nTivffKwIFpVyruJ5PgrrHO8NFSb0h5IZJSGXWR09O3sIWiGeBA000txMSD2-em1d2k6Xj6bHVSrhdiwxpEgWNLgmS6r8uLXSWiA_OJSVXE5wAVGFcNHK6BifplSQ2TSM2R0AvzQ_tjCW7gM3Bu1fYHuopU1F8n5ZMV8YwJJ0UVmJSQ0nbX6Rew7tdYeIAMX6oUWVdMx3xi9Ptc1Hxfe21M3thrviungdvuP2d2FSNUyV_C6tvhBxFzdE_j8-I2c3j2lNJrRMrTIwHHCMVd9KscyqyvcBRtBCzU2zcEspXVNjl5FfeDqNvzszKbWe3XSagZv6APkdOVIGmpMqnpYKnfTNRENjQ9VaxT3BZmMPOvokVmmspnQDoK-GSfMnar-w5dnb5OiSKbe3ki1BdMoHFPgdxiXR3-8x3-HSjNhSmF8g34ZeciGtetamCoATm2qJuiF0f3iuUfvwl77kS3YLCJuVfFndmnQmpth3kCyzmSeC8jN03rwccZb5trqKCK-Mo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های حمید محمدی از دلایل شکر‌آب شدن رابطه میثاقی با عادل فردوسی‌پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/92902" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92901">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/92901" target="_blank">📅 15:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92900">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hmxygqt07reJA8u6MMMi0GOEhsY5fIeDfJdPkWHfLOGTH-If1tUR4sqBdfF3ygEkqiVsqzC1QqQc16XtTWa1T7IeF2Ovzp8LeZeYaK9ImQ6HFiOsv4gXhIjIIXAOLI8PUocv4BpE1Elp7a_OULODC0DBWW9hS_UPDGIwQgeUcHV21v-NqD2nOGGNLdAJ3qPoMrZzRIGSraBG_tHM-FXOJOc9i-xPxfJ4G5TyZXwbnNMofLZt5jPICALo7q1rS5Kf9c-dSEZpDeD9dfGUhyztVd9gzo5-pAFkdU4G5MfultoHAhmpmJ5usAnNYn2eTQO0MW_PEvNTv7KBdpYLqaUVkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
رومانو:
🔹
پدرو پورو مدافع راست تاتنهام که گزینه رئال هم بود تا 2031 با تاتنهام تمدید کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/92900" target="_blank">📅 15:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92899">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0194235547.mp4?token=Un-zQac9Xir_OASLZhLBLFH0Pcwf2Kn5n1xGhtPmDqnHN4Opa177zUgYbym-0SrW8mqJcvBKgLwZkOEb6HqqM0ikntlaynvXtRHWO2G2P1c9usFRGdZDi1C1utFJMhhelW5uGmWoQ4DS5bFKBijJ_zXVZwr3A1vCpatCEhuhiHaEu8oH7RfiOx5tCBzM0E3KqlN42W5RUHCQpBCSBASKgMoMD60IDqQ8OXdRlNUb8Dw18d7OinZtfYmtaJDr3zhavSbGsWIDE96nx1DxdJJv2op-dnFC37AWOpi8VwcSZPlhsDI-ha3r8xHZb9CHiehs2j0NzEtoj2M032QOcoY1QqOUXTDbpuTFiFhj0zUoojOF7jPTVVQxdg6p7g23yh6s8sbf0jhD-HHstLyL8oIuIJoSilu15IuBquo0H60ktTWcsyFRfY-Pdd_9nNxu7vJC5jX7ZW3TfXufD95gYCj32ZbIu8WwzFFSFO5rVwjsXZFpiDmAg06ZexBioQlAin3bdhBblfqem5mdJQn7SRWsr-bjzQHE1UHgt1CkO7tIq6014D_JQqAuoVn_VhCwTGrhP9nKKVRuTXuG3W3yvJzmiDVbxSqmG9fbGCpzRrSF-yT1hyCL_b6HR3lxsa9jSWxUZA-bJtBnosX74QJK2DfMVsf4FRi7itpZcT9lUCz7CM8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0194235547.mp4?token=Un-zQac9Xir_OASLZhLBLFH0Pcwf2Kn5n1xGhtPmDqnHN4Opa177zUgYbym-0SrW8mqJcvBKgLwZkOEb6HqqM0ikntlaynvXtRHWO2G2P1c9usFRGdZDi1C1utFJMhhelW5uGmWoQ4DS5bFKBijJ_zXVZwr3A1vCpatCEhuhiHaEu8oH7RfiOx5tCBzM0E3KqlN42W5RUHCQpBCSBASKgMoMD60IDqQ8OXdRlNUb8Dw18d7OinZtfYmtaJDr3zhavSbGsWIDE96nx1DxdJJv2op-dnFC37AWOpi8VwcSZPlhsDI-ha3r8xHZb9CHiehs2j0NzEtoj2M032QOcoY1QqOUXTDbpuTFiFhj0zUoojOF7jPTVVQxdg6p7g23yh6s8sbf0jhD-HHstLyL8oIuIJoSilu15IuBquo0H60ktTWcsyFRfY-Pdd_9nNxu7vJC5jX7ZW3TfXufD95gYCj32ZbIu8WwzFFSFO5rVwjsXZFpiDmAg06ZexBioQlAin3bdhBblfqem5mdJQn7SRWsr-bjzQHE1UHgt1CkO7tIq6014D_JQqAuoVn_VhCwTGrhP9nKKVRuTXuG3W3yvJzmiDVbxSqmG9fbGCpzRrSF-yT1hyCL_b6HR3lxsa9jSWxUZA-bJtBnosX74QJK2DfMVsf4FRi7itpZcT9lUCz7CM8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇨🇴
این پسر آرژانتینی وقتی بزرگ‌بشه میفهمه چه نعمتی بغل دستش بود و استفاده نکرد
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/92899" target="_blank">📅 15:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92898">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Osw4xiXfwDlzA7eCPbQIofmSZftFbOcftfuL0mF65cf3rd-Q-NBkvEH6b2ZTGaISJLqo7mym6jSP0GNKl9FLWMkaA3qGgnNZ9rbFAuulmM8gorEmXkPmHPdaA3QKTfqMMyBwf1KjaLFKNKDQ44jw7zeQL6qUPbrbLs9utYZZvReH_D6tVzeqiXQKEb8cvKDWcO7sMucBCKTyq0TmoXiteY_XsJL9mrZ7_m7YVa45vGVIpFYPhBOgvAhvOrOsQ3Cozav7sgkucWXu34PpzPVrTJxw7VIZs4ZOuZNxcbrL830hjyErGIZjvVbiUaY_K5tA1LrdGYah4mq5KLOuSsSDjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار و ارقام تیم ملی آلمان در تاریخ جام جهانی
🇩🇪
:
🏆
• ۲۱ حضور در جام جهانی
🏟️
• ۱۱۲ بازی
✅
• ۶۸ برد
🤝
• ۲۱ تساوی
❌
• ۲۳ شکست
⚽️
آلمان در مجموع ۲۳۲ گل به ثمر رسونده و ۱۳۰ گل دریافت کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92898" target="_blank">📅 14:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92897">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
#فوووووری؛ حمله دوباره اسرائیل به ضاحیه بیروت، توافق به هم میخوره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92897" target="_blank">📅 14:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92896">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92896" target="_blank">📅 14:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92895">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPgNkVSJiYcuvKvVahOvA840_rrUZ5W8lKZUeMQoPaD39S7eqluVEyjhPOSJkh9VyT9hwnf-rRlPoKGR2-dSTN91PLEv8Og1839UsYRfwiY_xNgwn7fcQB3vY2-LpRYU0_3IEBYM280c8m6TZfumrU58kzhVqVdbkD2hTzxSA0EKdvJDkfyrJHxqaF64YnTX9RkJPqYKN7tAJaCXMl7BFv0uzG6YBsoAffdp_JwIwBtYJA-rkbsnO1qVRnn8AkRlktONd4MnClavz8ULeVGY6GyMPN6MTeOd9OIHkrKyA6B2Gcc5NdzNAzSQKxYTyh4hTomLVHJW3XfnEvQh1ubVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#
فوووووری
؛ حمله دوباره اسرائیل به ضاحیه بیروت، توافق به هم میخوره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/92895" target="_blank">📅 14:21 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92894">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b1d4f272c.mp4?token=dAPYeZNRJJEavrbzFqrDCGtnxBtxp0TSP0xjeCDIH9RVNCrASpw07x7Y5SLXs6S5CE5cQb5FhcGV0--w89u5_FIGinzORwonpaCUNKeOZfn5rECinU8uvFh-9LtbDlg5tIb0dvpBO6yCOXpkpxLGtxwBgDRP7lPG0mQZTFbdijv9MS9qebuu6eKILV0KxQuSbo8MXF55hmoF9Ca1rVcYBYUNoEkndicYiD8ZfYFiTvKLbgl_80g7DJ3Oa97mCaUMe926o9te5K5tmcOtK9N0QU7xNg7KH5SBbqU7vrs9cYIBER2S6HX3YVdirv9d2dbjMZK8jYd3B3Y03bHEfOznng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b1d4f272c.mp4?token=dAPYeZNRJJEavrbzFqrDCGtnxBtxp0TSP0xjeCDIH9RVNCrASpw07x7Y5SLXs6S5CE5cQb5FhcGV0--w89u5_FIGinzORwonpaCUNKeOZfn5rECinU8uvFh-9LtbDlg5tIb0dvpBO6yCOXpkpxLGtxwBgDRP7lPG0mQZTFbdijv9MS9qebuu6eKILV0KxQuSbo8MXF55hmoF9Ca1rVcYBYUNoEkndicYiD8ZfYFiTvKLbgl_80g7DJ3Oa97mCaUMe926o9te5K5tmcOtK9N0QU7xNg7KH5SBbqU7vrs9cYIBER2S6HX3YVdirv9d2dbjMZK8jYd3B3Y03bHEfOznng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باشگاه بدنسازی تو یکی از روستاهای مملکت
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92894" target="_blank">📅 14:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92893">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxxNXg1e-o34d6yEyIk6XN7slHm-Fjco6GfWJTKlRfFzm6M2eRvpQFGqWybY3j_omr3RIiIb-HydAHdHyux_5qOfovn-Y-8wVj_2UZnC6Hqy4bO66vAVyMltA-5TAwi7fTX0ZXBy9upkq5Ml4Lf9_KbHUIpnwqkUbBH1hPmemE62DGI7gzfj8vpvETGDak5_vN_CQrppaMeq2wSNaiE4CbxhnEm-L6fSC_eetlZyu1PzqxuyEkfvBL6ULsT47moDstgB6QjiWNA_05vDOnwCmj80wjcWm9MyGJpkvw2o_h2Mamihti0wWGkT-Y7UOY36w4xZ8xk-FaXPwpJbvf-IFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیبی که استیون جرارد دوست داره تیم ملی انگلیس با اون در جام جهانی بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92893" target="_blank">📅 14:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92892">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da69a4b2bc.mp4?token=boKESNbqN9P_17fEa8khWiMsTYE12RA7TBm_E2qA_Ll3c24SfAXjPP42B6gWUhzcw1z-UMBfi56D15X56uiVg_iJlsQIK4RxjoPnCCnPZ3y1UA1FND3UDP3L4My92VG0CpxERsY-QNHLS_IbdHbOWgtamvHqEaiKYv1OfDcSmccIU-DwWQ-RRFXpWnCazgeW2n8ZAJbvr5xXKOPh_e8-NFxztg2-WZunXg_dVlTzbbTbFBpha-zfNygj2kAjsR1_CKSeLlMbnZkFjsF_jz2pUyh7KqgPfh6QKP_BAU6e9ro1suA3T_kOOvnt_yzE6f2LgjN8A19P479Mocl9qMoBYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da69a4b2bc.mp4?token=boKESNbqN9P_17fEa8khWiMsTYE12RA7TBm_E2qA_Ll3c24SfAXjPP42B6gWUhzcw1z-UMBfi56D15X56uiVg_iJlsQIK4RxjoPnCCnPZ3y1UA1FND3UDP3L4My92VG0CpxERsY-QNHLS_IbdHbOWgtamvHqEaiKYv1OfDcSmccIU-DwWQ-RRFXpWnCazgeW2n8ZAJbvr5xXKOPh_e8-NFxztg2-WZunXg_dVlTzbbTbFBpha-zfNygj2kAjsR1_CKSeLlMbnZkFjsF_jz2pUyh7KqgPfh6QKP_BAU6e9ro1suA3T_kOOvnt_yzE6f2LgjN8A19P479Mocl9qMoBYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇧🇷
ویدیو همسر نیمار برای جام‌جهانی در حمایت از شوهرش و تیم‌ملی برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/92892" target="_blank">📅 14:07 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92891">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNjBOpe33GFlpls7egJehzSabg7YVYtyhbHponv_CTSJ2Ua5iaYNUigE2_rqB6b4rHxYQxM1nuph8VLhfB5771x6ukHOG_3UexKEKA0ZK0_UaGRM6dJ2_xniQK185smyRgGzb_GyNhdymd88TDwJ2RW0u7o_HrmJhhY9Z_sD_yPJf-MRgTzz3VfjdWTW2djFYeA77Y3xTcj-cas6CeXR_aHWaM0Xsj9iW7ZycIazPD9JvcciH0_awhUA5RiqT_HOtkSXmCx2B7qnmcAdTc16CgZP-U0lDQXol0YeulIK60wCxFkpJ9KVyUUSwo3sz0H6q19NnkK55eUiQmqOpg2gcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁳󠁣󠁴󠁿
یه فکت بی‌اهمیت بخونیم باهم: به جز گل‌های به خودی، هفت گل از نه گل آخر اسکاتلند در مسابقات بزرگ توسط بازیکنانی به ثمر رسیده است که نام خانوادگی‌شان با Mc شروع می‌شود.
‏
✅
مک‌استای
‏
✅
مک‌لیر
‏
✅
مک‌آلیستر
‏
✅
مک‌کوئست
‏
❌
کالینز
‏
❌
بورلی
‏
✅
مک‌گرگور
‏
✅
مک‌تومینای
‏
✅
مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/92891" target="_blank">📅 14:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92890">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCF0-4-YJtzL1EsK-FAI2EY_3UbPwIkDTAWdEVQFM4IZBn4OSmJauUW_lrcN1xE6AHOp1t2m09kBwSLmwB9_fCnhFHnnYCOOlBe2po60Gs4qzabMvaGATRBzMBclDy8cyiHyn6qO1KosUohqs4EfnHU4TcU6QOeZZ7t6poU1RE5IX5sC2X1vG8L50EOOiKt7Nabi_oTPY5eST3cwJOW0IRbRYe7tBazW41d6bMze4_kk5PRz0miH6f8yYb_s7etD6fh2O6K1flLXfT1PdjFvHeG49BozjdHAOU8c4tHO29wK2B7Z4beG7DMIZO_iG30LUivEw_Ifi1X-b8-_DvJn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
فیفا اعلام کرد که به عمر آرتان داور اهل سومالی که توسط آمریکا دیپورت شد، مبلغ ۱۰۰ هزار دلار حق‌الزحمه پرداخت خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/92890" target="_blank">📅 13:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92889">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LNwr-Qv7Jo95gCJoH0Xo9Km4-KQFvlfO8TC9BYuc0UvS0TqNn8-aMCz699yfd5mYjK9z0Q7hka8v92siV6zqWjrWdVSfqQ4EkAmZaKy2N4nHx4WQXytSnPuoMA_hswxVigp3ckGrVm3YYGFOQ4H7hnA4fTSSeW3U_zCZALyzVoXaBTq_tBnW7kAcQCh7kKZJh0Ikgp9raUbzIua2-GUm5demgvDMm3KUVIBXllA9Okrv0JEeuPwpTv0qEs60aM6U_Q7dO8_XamhYt96YcrlHEC6gUFBRtaB5IxxzmiiKDPwmxYlt_KQn7dG-gO17H9im2Zuari1qVdTP9XnwTrGyoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نیوکاسل برای فروش ساندرو تونالی خواهان دریافت ۱۰۰ میلیون پوند شده. آرسنال و منچسترسیتی جدی‌ترین مشتریان این بازیکن هستن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/92889" target="_blank">📅 13:46 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92888">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1AlOtHZnnN6eW_JOGYrbvelEHDmgETf_jE9-7vYBhardvTzcobFCv2Sh6Plf8Dk_F5lRq-YkGBCVwYnGoKj3srYhVNj-iLQST40WmyIY40Go764BT9YQ-p7mZ_K5LrXEbItyYcRLzLBzMrdMswEtWscGweJ2lXKcomEXzxG3VmsBwt06JUtmfVJA9I3qI5TA-nizMKfV0uwe2SsV8Hk-MifqTAmbX9gUHkzkihycvWqVTdwcCLUzVtD42JpIaUJvU51nuv5PpeENhdF_-_YbcKRqGE2DT_h5asHEqK3vEgO9UIzqtANqenYImEgdDzozEK8qxpE7lXVa6Ocy3899g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏆
🇵🇹
ویتینیا:
🔴
برای من، اینکه با دو تا از بزرگ‌ترین بازیکنان تاریخ، کریستیانو و مسی، بازی کرده‌ام، چیز بزرگی است، ممکن است بعد از تکرار زیاد عادی به نظر برسد، اما اینطور نیست. به نظر من آن‌ها از بهترین‌های تاریخ هستند. افتخار بزرگی است و غرور عظیمی که بتوانم زمین بازی را با آن‌ها شریک شوم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92888" target="_blank">📅 13:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92887">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ab1ae15fb.mp4?token=eoUYYXEdhpk67ct84J06fekxMhyCedyVpB_7fE4dyThOAPECp0x2jFhSD6Qarx4z8NVoEwrFyNbIawFk8qVgC8M1Gqb9P3Mos1-PORcv775CZJ78WSgWtMQYtBeLoH9eMCVUQj4yC8vGc4ZsY6ub5gne4apVScmz4qnzDb-t0-0e-mjx4ZIfdoRHhxzH7_2PWcR6D-QeAN5UD5YGVLxs3OVUYzWmTpFQoWeIlkVHzA9f3yBjYV2TzAP27vSGMHrXOwruhNUY6l8-V1eW5lhErG2kLGXeEXx6BgSLlYRGQ5fMym78u97-3RRm2F3aLAXq5c5v6TljHurP6xU8kjOWAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ab1ae15fb.mp4?token=eoUYYXEdhpk67ct84J06fekxMhyCedyVpB_7fE4dyThOAPECp0x2jFhSD6Qarx4z8NVoEwrFyNbIawFk8qVgC8M1Gqb9P3Mos1-PORcv775CZJ78WSgWtMQYtBeLoH9eMCVUQj4yC8vGc4ZsY6ub5gne4apVScmz4qnzDb-t0-0e-mjx4ZIfdoRHhxzH7_2PWcR6D-QeAN5UD5YGVLxs3OVUYzWmTpFQoWeIlkVHzA9f3yBjYV2TzAP27vSGMHrXOwruhNUY6l8-V1eW5lhErG2kLGXeEXx6BgSLlYRGQ5fMym78u97-3RRm2F3aLAXq5c5v6TljHurP6xU8kjOWAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دیس‌بک ابوطالب به میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92887" target="_blank">📅 13:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92886">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPa1pkj7bWzMAnlpsVRQmA9PEWBfk-s2VN_ggTY9CX-O2e7zl66UhoLbT8VhkkBcDPw-B9TyfDm3jrrLLVKxKQYs9Xxedvgv6Lukuuo4X3tpxwcNIXLfd2dkzV7pi8MbUQZLFE2MCQRc7gvaE7dUGv2ojPsVQH-YXbBIsy77x6zmQYXd2PrtiULk3zPm-6eGppDjfdTeX0NfjqcbPnEd2hwALarKylZylfsTF9ktkORkYsdMSJFFozD9omIVBx-QsZ5ucSNyKVD-dKtU6c5mrJG2FppHlGjszAmfoOpaeNXM_xUKSFwvdIDCWtTOD75_8D3nFWylUxa_FtjFwqZ5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جام جهانی پر سروصداش خوبه!
🔊
بازی ها رو تو ویلاهای جاجیگا دورهم و پرهیجان ببین
وقتی بازی‌ها نیمه شبه، یه جایی بهتر از خونه برای دیدن فوتبال لازم داری. جایی که بتونی با دوستات در نهایت هیجان بازی‌های جام‌جهانی رو تماشا کنی
🏠
⚽
ویلاهای مخصوص تماشای جام جهانی جاجیگا رو اینجا ببین
⚽
🥅
🥳
https://j1g.ir/t7
⭕️
جاجیگا، خونه خودته ;)</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92886" target="_blank">📅 13:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92885">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94684b60b2.mp4?token=Mpi1jm3UALKDAd2ryUdZm_zSJQ0jmjs8LMe1oqPVjjo1QtwBv_YG-93qjk3fis80J_HyYrUxdMsOFfdj-i5tZnM4ulVUDW9tMWU54J4HF6nH5ilA_JX4HLPCDp07kEHnIniQ8q7SdEfmhXbhV-fAjgUD8zjhtqle0ZosaE6MpairMx_UJHVWaSPNMtgQ-0rSJsjEBDriS6bpOQ_0LAg5jHQTrnp83FOMoC0u3WKGDsdPMkQTRwtivrvGbfgPOxEXeZeYouBpUKnBAqyPRFiINiShhjxH-SIhmXkp8WQvml3gZ1hFLdt-iRKI6Lz_WpN63srtMIsISSDqmnhSH4orDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94684b60b2.mp4?token=Mpi1jm3UALKDAd2ryUdZm_zSJQ0jmjs8LMe1oqPVjjo1QtwBv_YG-93qjk3fis80J_HyYrUxdMsOFfdj-i5tZnM4ulVUDW9tMWU54J4HF6nH5ilA_JX4HLPCDp07kEHnIniQ8q7SdEfmhXbhV-fAjgUD8zjhtqle0ZosaE6MpairMx_UJHVWaSPNMtgQ-0rSJsjEBDriS6bpOQ_0LAg5jHQTrnp83FOMoC0u3WKGDsdPMkQTRwtivrvGbfgPOxEXeZeYouBpUKnBAqyPRFiINiShhjxH-SIhmXkp8WQvml3gZ1hFLdt-iRKI6Lz_WpN63srtMIsISSDqmnhSH4orDIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید با همین کسخل‌بازیاش اینقدر ویو میگیره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/92885" target="_blank">📅 13:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92884">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tXAVScJ2TC6dXAU9fiGDxEqUbQYGShRTv1n8mOo_GR-yn9595_K9DjKj-hwfS0lhBDA5w9E4PIExhZSNtTJoh4uI_v9HN9_6f0RaFKUX9nj3E_VK2lpcbAfuSu8xJaIa16v6D4ebVk7TTIqUsDOcGXeLSAwT6AcdIcNVUF7OsNmI5YAYOCUnLcMpt4nXMIfr6SXyerl9jppsj6Zdq8HP67qWOpQsZByVQKjYBDsEC-V8FS9GqdrDdZPN4EaIesAflwsN1yshdluOBaaN9-Bae3o5MAz0gO73pgp25xYGd3fanhvr2vbS__WCQDX1UvziOhNPe9qitdpdSjKd9irC5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🎙
کوین دی بروین درباره جرمی دوکو:
عملی‌کردن دفاع مقابل دوکو به صورت تک‌به‌تک به مدت ۹۰ دقیقه تقریباً غیرممکن است. او همیشه در هر بازی بین ۱۰ تا ۱۵ دریبل انجام می‌دهد. با سبک بازی‌اش، به طور مداوم چندین بازیکن را جذب می‌کند و این فضا را برای ما ایجاد می‌کند. بازی کردن با او زندگی من را آسان‌تر می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/92884" target="_blank">📅 13:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92883">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d82ee8274f.mp4?token=E-G2UT1snt-mmAbnfLXVsoiyjJZeZw3wACuhfLV-4c7ISCOOlof867hQoezrSy3B3Ue2G52_X5BOODCjfGs25wvs5SaNRGdQlsqdu15KoFPhQLC444jbdJSunm__664e3A7M8CCBoRBBMHWd7Eao4i9KvLGPT4iXs85sk9OJkY2LXN8C4u6qTs100t5qrroezgZnyrz3iZPfZPvMZZSuhrg3jjhUzmxnqgXmLzMqg-Ahhm6vbQz2zEk1wJly_ib3yCiOHwIzBw2oLlCm3pA1ihHNqESEINMT6pwzRkM61y4zTvTv_qBApXNSpOWA2-Kf-10fpIM3FNr1PUswv8tVUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d82ee8274f.mp4?token=E-G2UT1snt-mmAbnfLXVsoiyjJZeZw3wACuhfLV-4c7ISCOOlof867hQoezrSy3B3Ue2G52_X5BOODCjfGs25wvs5SaNRGdQlsqdu15KoFPhQLC444jbdJSunm__664e3A7M8CCBoRBBMHWd7Eao4i9KvLGPT4iXs85sk9OJkY2LXN8C4u6qTs100t5qrroezgZnyrz3iZPfZPvMZZSuhrg3jjhUzmxnqgXmLzMqg-Ahhm6vbQz2zEk1wJly_ib3yCiOHwIzBw2oLlCm3pA1ihHNqESEINMT6pwzRkM61y4zTvTv_qBApXNSpOWA2-Kf-10fpIM3FNr1PUswv8tVUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
خبر خوب برای هواداران کرواسی؛ این رفیق عزیزمون گفته که براتون تو جام‌جهانی حسابی برنامه دارم و منتظرم باشید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/92883" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92882">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/dCim27bO1qlirHvvF7t40F0an9RLe1k5FUuFobKbuMhNZ8KUHsl1p5XHh88B297yqGvVYCxoiBSnolVDioB_e3KhwBLf7hb6d-xtxsSXsF5dHDiiT96Q5jFIVKHnTLHyC273LUeHKDg97YXNJPqw6Ew53FI4CRMEbXb6gL3S12puu0HB1-tdzzyzdQZ2TkOL5a30QH30O6TaaNJnrAZnx2A610wQ0SpzofjMEcxpV1hJIJUiklJ3ofEHCRQyvgaVD0fJKeE079IvO0kF77kRlha0A8wxwXtcFtRmEpePoLol-FwaI4QbLzuqPmDj7ohB13brmcwl1JC2VZE4N5CGgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
🇲🇦
‏مراکش اولین تیمی است که با ۱۱ بازیکن متولد خارج از کشور در یک بازی جام جهانی شرکت کرده است
🇫🇷
‏۴ نفر در فرانسه (دیوب - نائل - بوعدی - المرابط)
🇪🇸
‏۳ نفر در اسپانیا (صیبری - حکیمی - شادی)
🇧🇪
‏۲ نفر در بلژیک (الخنوس - طالبی)
🇳🇱
‏۱ نفر در هلند (مزراوی)
🇨🇦
‏۱ نفر در کانادا (بونو)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92882" target="_blank">📅 13:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92881">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K46JVBaowM41qf-1238vyWnPjhcXqIHTCvpL6R7s5a6wi9Ca-Qv_0wBIw8dF1SrEcIgMh3BKUT4Ss61miCnUNlUC0aFV3n2CswnxCOSTT7HncrKnMMKuP_W4XCMIzsrISlKO2kf5JLWOlPv5tmg0ZpJM6oNBz9yohEaj57Xp00ZaPtFknKPj01ExjH_QHDD5m368cvilw3kV-B031Wu1oBczS2Ktl_aW6pRZ1kUsQtMn3oOiPMzUVXxiEtsfbVSz1e57PEhu0VC7VUmfGONnyvqxJCvR6_P3nDrmBDN8axj2dO6kNbWR2JtDxjEEMihuXyhgwdyGjrvuDB9C_3zXtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🏆
آمار مسابقات جام‌جهانی تا اینجا:
💥
8بازی؛ 19 گل؛ میانگین 2.38 گل در‌هربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/92881" target="_blank">📅 13:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92880">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">‼️
یه هوادار کره‌ای بلند شده رفته استادیوم بعد مکزیکی‌ها اینجوری پشت سرش حرکت نژاد پرستانه میرن که طرف پشماش ریخته
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92880" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92879">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b98e2b8a04.mp4?token=NVLOczLZgeX8zz84VuuvGbEMGUVU0azIXYrEEiQi6ZdS2TWyVd2TJRvGHC2sI4bAuxSb6dTi1b_1-HvY4O8OoITSVk7FRQMIk3zIZ1suhuZTUkK9ARwKfHPVBQ7xYW1XU277eTPypzzGVTMCLqhaMGFeRJgWyZYqkZJeJXginC9uRnx1g_-6U_ID56f36CUyLzqxvMsk91vyPDHu-qhNwtY_VWEuq8KgldTaViEgqEP67sNzoklKbaECjWr9XtCiaZhnqCfNb3FzefIO7QnQNbEHKvBowK2804GbXQgzHvU5ZUBJrwhTLs3IAQlF5eXkvsE2vLVH4GoRdCpCCUUj_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b98e2b8a04.mp4?token=NVLOczLZgeX8zz84VuuvGbEMGUVU0azIXYrEEiQi6ZdS2TWyVd2TJRvGHC2sI4bAuxSb6dTi1b_1-HvY4O8OoITSVk7FRQMIk3zIZ1suhuZTUkK9ARwKfHPVBQ7xYW1XU277eTPypzzGVTMCLqhaMGFeRJgWyZYqkZJeJXginC9uRnx1g_-6U_ID56f36CUyLzqxvMsk91vyPDHu-qhNwtY_VWEuq8KgldTaViEgqEP67sNzoklKbaECjWr9XtCiaZhnqCfNb3FzefIO7QnQNbEHKvBowK2804GbXQgzHvU5ZUBJrwhTLs3IAQlF5eXkvsE2vLVH4GoRdCpCCUUj_TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
جمعیت فوق‌العاده آرژانتینی‌ها در آمریکا برای حمایت از تیمشون مقابل الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/92879" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92878">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/92878" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/92878" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92877">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kgrq2jZAndNcvSA2_76cStLdyj5CIgWSqDp9NR1efpeLirRkElQbIDpe8rsExUB_iwzjkSx3OsSMMvYjDH7Ark262Z0pDAUCbRQgWbNhHIzc0vNr9POrnwYubx0aJNqmv9buJDTLmIT9nisPXlj-xecNpEWug0CAAZMHLG2NFkr8FTr_2npoCG9tdkcX0Qj33xh9kbiCPDU74bbS1pQEPcbItml2CVl2-ovBJFwjgc5iAjv23SqM3eLtc-RDHod5KvqxYaXcZ9ydB9rjhG21-JrZer0RZzYtA9Ac5Am2O9EoBucx1T1HG6mODpztP4EDEOHQPixoNPQAUtMMdz8_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/92877" target="_blank">📅 13:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92875">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🏆
🇺🇸
ویدیویی دیگر از برافراشته شدن پرچم شیر و خورشید در استادیوم‌های آمریکا حین برگزاری جام‌جهانی؛ به گفته ایرانی‌های حاضر در اونجا، پلیس گفته که هیچ محدودیتی در آوردن پرچم وجود نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92875" target="_blank">📅 12:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92874">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f330d63e81.mp4?token=HPQVQPeMGnxDwyBxU8FRDRlYNo2GhAZwKxhBy1w43az1VCHLPV8UTbX5jKbaYoHf9pyfqgh8k3Ml0JKiCxiuHrbmeUVgRZ3xPfSGZtLvJhIMUwBD34B5SJXTho7-gLYz4nEsQl9453xhuFepzi3VmPLFXRyoGLM0Rul2LDnB1nE0IiNVvH42M622hxT0P8wzrM9eSPQQ8oKklEijyJd9BLJDkVvpkqGVOafNa7_ibDtugvhdLaZhdhbd9NKZukp8TdApRvmF8EmlbOPdq3UIj-AgxWQkSKK34vBnlL19HIAf9d96CboP-tTSjy0QIT2HtGDuoy2O7gQr6KvySKfn8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f330d63e81.mp4?token=HPQVQPeMGnxDwyBxU8FRDRlYNo2GhAZwKxhBy1w43az1VCHLPV8UTbX5jKbaYoHf9pyfqgh8k3Ml0JKiCxiuHrbmeUVgRZ3xPfSGZtLvJhIMUwBD34B5SJXTho7-gLYz4nEsQl9453xhuFepzi3VmPLFXRyoGLM0Rul2LDnB1nE0IiNVvH42M622hxT0P8wzrM9eSPQQ8oKklEijyJd9BLJDkVvpkqGVOafNa7_ibDtugvhdLaZhdhbd9NKZukp8TdApRvmF8EmlbOPdq3UIj-AgxWQkSKK34vBnlL19HIAf9d96CboP-tTSjy0QIT2HtGDuoy2O7gQr6KvySKfn8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
روایت جواد نکونام از پنالتی چیپ یحیی گل‌محمدی به چین در جام ملت‌ها آسیا ۲۰۰۴، در گفتگو با امیرحسین قیاسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/92874" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92873">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تمام بلیت های بازی ایران نیوزلند فروخته شد
و مجموعا 70 هزار هوادار در استادیوم حضور خواهند داشت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92873" target="_blank">📅 12:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92872">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1c285036.mp4?token=MBB5mCV0xraxuOwtElGYfnB-X7cgy4OBXOfkXsc60pJX6P2b8QRJ1oHpET-8j-_cwbeMZCgMqhglFb6dmjuDUCCfZZDfIYb_W2zGrLzWTHjNicR1feCLOv0tnf4gL_uPdgmWyWHStCml2ZFGydJzIhTfOupQV-68PM5oXmfGFSCgWrdXeFAkylb0_U8IuMwj-1UBstZwnWV-F_ax_MiWrIGtMn2_SLUCal5lELP3DM8OhmhtTQoOXKAX2cN2dFG-JNczMeYqsZ7G0ZOgdjgo31hgv38F4IhcFqhNAd2n1DSMVbUsAHCzTqGAOqbZ19H5PR79c7IGNtv0ghR6IU2UkRItbV9HIQJ30PT4ZN5IWYPxA8neOFGLMp78mdb8gvPtuaYU2YQ9cN66e0FDoqF4kMcFlvknkJu1AQNhrIvV5RLge7z1kGR-aY5IDuAsanSGDJtbvckUV3aGqxM9SxD01lQI19b1l-F_sR0Cb_0rOdGUIqSxIX7u48saZMFAQeOcbvccVC_P9SA9X1GytoN6v7N6oSUZuoIxFNCLp4ZWHfR3p37fyWrmZUnecR63n-6Rjh1GlbvlkVXemWfwn3VSWVGNP4jF_fZkC5CoYHyUwuJqEjgLQ-rE5Wg0icKlOlPRoKtICGU3I0Vk7P7NfgGG_mFxoOhqj79c261E04F_WFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1c285036.mp4?token=MBB5mCV0xraxuOwtElGYfnB-X7cgy4OBXOfkXsc60pJX6P2b8QRJ1oHpET-8j-_cwbeMZCgMqhglFb6dmjuDUCCfZZDfIYb_W2zGrLzWTHjNicR1feCLOv0tnf4gL_uPdgmWyWHStCml2ZFGydJzIhTfOupQV-68PM5oXmfGFSCgWrdXeFAkylb0_U8IuMwj-1UBstZwnWV-F_ax_MiWrIGtMn2_SLUCal5lELP3DM8OhmhtTQoOXKAX2cN2dFG-JNczMeYqsZ7G0ZOgdjgo31hgv38F4IhcFqhNAd2n1DSMVbUsAHCzTqGAOqbZ19H5PR79c7IGNtv0ghR6IU2UkRItbV9HIQJ30PT4ZN5IWYPxA8neOFGLMp78mdb8gvPtuaYU2YQ9cN66e0FDoqF4kMcFlvknkJu1AQNhrIvV5RLge7z1kGR-aY5IDuAsanSGDJtbvckUV3aGqxM9SxD01lQI19b1l-F_sR0Cb_0rOdGUIqSxIX7u48saZMFAQeOcbvccVC_P9SA9X1GytoN6v7N6oSUZuoIxFNCLp4ZWHfR3p37fyWrmZUnecR63n-6Rjh1GlbvlkVXemWfwn3VSWVGNP4jF_fZkC5CoYHyUwuJqEjgLQ-rE5Wg0icKlOlPRoKtICGU3I0Vk7P7NfgGG_mFxoOhqj79c261E04F_WFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇱
جمعیت پشم‌ریزون هلندی‌ها در آمریکا قبل بازی امشب با ژاپن؛ بازی ۱۱/۳۰ شب از دست ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/Futball180TV/92872" target="_blank">📅 12:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92871">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK4sRHw8bF0sqIsefhYl3LBgWKG24kBuXB8nq11DIID9WjpD1GEB03SEt0B3T1tp7XUEMj1rYerVhPDqbM4lqItPG9hFQjb4lduRWQLlME-J9rXgY9gZ436XwzkvgIQdfO7mpoT8sa2fJ4WGlI_fsAqqKkXpgylnu3ghNpxBzz6QfosUF8QtltDsi26PgNC-ZeUeRHNqQNPHjQrEE6kxOp2GjT9sEfImVL0EB2ynd5l0Foe8OcwFE68drOHGQiuuLxLHcrpzalql7kctB2EiBnJ1NvFdCcUhv2JxGGj2ot8qBfDdiwVn6-A6uZpFP_EeZ09EtbZxvcH3fjQWWEIlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
میگل سرانو:
ژوزه مورینیو تصمیمش رو گرفته؛ فران گارسیا در تیم میمونه و آلوارو کارراس باید به دنبال تیم جدیدی باشه.
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/Futball180TV/92871" target="_blank">📅 11:56 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92870">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وضعیت تنگه هرمز  پاره شدم
😂
😂
😂
@sammfoott</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/92870" target="_blank">📅 11:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92869">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">💥
🏆
پارت‌دوم لب‌گرفتن کره‌ای‌ها و مکزیکی‌ها
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/92869" target="_blank">📅 11:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92868">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vMbb7HDuN4kjFMaclwQr4Nd-ugDxoTNgxVkWt3ASWWu_gGjilT8C1SYxM3fUocldHm1KX8K_bryyBqw7C64K0HVCklyHOqH0dw0nJdy1oTqsJ69L9iLbkQEp6BHVxwVNdjv1_MRH2_39qu0lniPb11daRy6onQP-gwz26-flJlbdIOmt4lwYsB7KA6625ds4hDrOjJN74kLNImvHDFNWrMoxBVVBE3zk1PBlxA8tIRzgcnxneIF5cxW4W2RMD0EMAG7oHJewf5FUQZJkAZU1xC9kjb2VzN4C2j933-ZWuxSmYBXhIM1GHVrf-i4ZrZUaemTcGfhSp1R1IAOFTaRNlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسانه‌های اسپانیایی مدعی شدن که مورینیو از عملکرد کارراس و گارسیا در دفاع چپ رئال‌مادرید رضایت نداره و ممکنه در صورت پیدا شدن گزینه مناسب، این بازیکنان رو در لیست فروش قرار بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/92868" target="_blank">📅 11:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92867">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cb205515.mp4?token=Cwdd44c_i29ucsQGV2qkr5_0n3hKK4i_zt4FR6Dc_rT_LqxKAXgMxWbSxVZfk4YL44HhnvBiNkg5Psp1ll0iPBgDn-5ORwLdPqsYCaA9yR40vIq05OrZL5Felt0uviVOO85pZS74usrO8b86XSKOcX_XELY8RS7lIIFJygJvBjuCmq2_doA7vNSGRAJEHn2wRSfYdIWf2jysTyhPxpJ1NjJa0BxjRiPqPxZeO5HokPxh504r5zk1HPYlPtnUVb6gnpoUtfgklBqUTU52nG5-Li_fwAnW_VxHaufG9GeLJyoXSExRaVpEOSXf5Zs5HyszWS5TLFLhQkZpajGeJrqeFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cb205515.mp4?token=Cwdd44c_i29ucsQGV2qkr5_0n3hKK4i_zt4FR6Dc_rT_LqxKAXgMxWbSxVZfk4YL44HhnvBiNkg5Psp1ll0iPBgDn-5ORwLdPqsYCaA9yR40vIq05OrZL5Felt0uviVOO85pZS74usrO8b86XSKOcX_XELY8RS7lIIFJygJvBjuCmq2_doA7vNSGRAJEHn2wRSfYdIWf2jysTyhPxpJ1NjJa0BxjRiPqPxZeO5HokPxh504r5zk1HPYlPtnUVb6gnpoUtfgklBqUTU52nG5-Li_fwAnW_VxHaufG9GeLJyoXSExRaVpEOSXf5Zs5HyszWS5TLFLhQkZpajGeJrqeFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🇺🇸
ویدیویی دیگر از برافراشته شدن پرچم شیر و خورشید در استادیوم‌های آمریکا حین برگزاری جام‌جهانی؛ به گفته ایرانی‌های حاضر در اونجا، پلیس گفته که هیچ محدودیتی در آوردن پرچم وجود نداره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/92867" target="_blank">📅 11:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92865">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VbJhqGPi8KxoC-96RJk8PmRle-9kjk3tDX06zQ2hHfY1__LjrkkAOh4WsmFqlEarTv7JFDKixUJOkjSm0zum_3CU4au_46XUlLzcjAfuFkhbUpfRCWP7uWAhG6U3mN_TpKFAvpCnvdOQawpFwecRUhRctTLEbKc85IuJoVFZxA7BRZGTOY6qS1dHIYDfep7x064qkKpkYbVjLlROfZT3M7YFHzPDgb_PYZ8OtNb9QlL8i3iuDdC4So6fh-65O0f2EUr4iB1tpMxoQQad3Kky8EuIIHDKjGm8mwbIhKFWRLjZzPcuIExxsVbJAun29H6gD5jqXPThQzFTlLkwcnFo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lA9VhhVGCYNwWGOtkdnawcBMpTpUXEoVXShDgm4XS_bHH8PxoTH3Iy2GKxKQ_beEFVIXzDrKiOZBdVK2irZ3BqtkGG74DaOzmRoG4mApTKa0F3MmRs58LWELgx5QukVHy16T3utdPVo7LyQMV08S4qFQy6vly2G27zJY9Yh2f9Crrcv4hGp_MkFPzP1B6ceDBQPRUHRqE3NQ8G2eTvKIU7MjNSxKRiTjZ5KN4uqXyGZ9Drd1uE1Rm28GCb9dXSBkcxcwiDoV2CLqCTLvSui7_Qkeo01SR17gbCRalt__mmNJVOzKnf23GLTOl0Z5P_NCPo30OwaiZOTcXQnt6RJVPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
❌
برخلاف ادعای فدراسیون که به نقل از فیفا گفته بود ورود پرچم شیر و خورشید به استادیوم‌های آمریکا منع شده، تصاویر دریافتی از روزهای اخیر نشون میده که فیفا و مسئولان امنیتی هیچ سخت گیری نشون ندادن و به نظر در بازی‌های تیم قلعه‌نویی قراره حسابی از این مدل پرچم در ورزشگاه ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/92865" target="_blank">📅 11:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92864">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cfe6bdbc.mp4?token=vrpa4mVVPbNWMMv1qs04bKS2msUdHwhYRcJtKcdHHvtCWi5NUVNepVdAUVfbNax0TsyyhtvHXsd9LSMxD_m5z8c7LLtFxXVDE7CKy1yN9jsnOWjNbaQcRPbF2sz0fxnyEAGn11VnlnlRbTO8BOXFddBxHjySZtXjAAEuirSwFxjHnKSkCVxLq1LXVqiTzS9VlZWheDVcz_DWFw2r-Ap47eK300mo7pfgcf-enWzLgBYfI957DlIGcJVgNPHY8bUVh554k4Cct5KcksrrJ7zHBY9T0G_xxyrtVaYyB6bbTrCayaepWCVnbhTwXl_gck2oZ95OJBVhg8tahD2LvV2mvlFZZJCnDByoaeWeFC_3li614RphXZcspU-LeBHJxlJ4vVx5SbJkPgXEKStHd5c__tl9vmCBZS0UoMLKvk7_qM1RKrPtQmkJ3bw6DlHzSt49Gvpa63orwzSlwEvRNXVJmbSDj_ht9rGday7J806ZJAFr2f-RKzPML2i2zDBO6pbt0pmH__FVdUlJT3YHiH-hC4N65NMElB-AapN7r4VxCFQ56MMRa1V4wov2AI-aRwOcJb48e1Kz95_WKOjf5w8GnvQPuVR76OIgjT_LMh6jXevIl_YyRNpLVy-vDp6FJZ8eF22MKEN_cC3MyncUptM38K1pjOP7jcX-0RKU9tcWALE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cfe6bdbc.mp4?token=vrpa4mVVPbNWMMv1qs04bKS2msUdHwhYRcJtKcdHHvtCWi5NUVNepVdAUVfbNax0TsyyhtvHXsd9LSMxD_m5z8c7LLtFxXVDE7CKy1yN9jsnOWjNbaQcRPbF2sz0fxnyEAGn11VnlnlRbTO8BOXFddBxHjySZtXjAAEuirSwFxjHnKSkCVxLq1LXVqiTzS9VlZWheDVcz_DWFw2r-Ap47eK300mo7pfgcf-enWzLgBYfI957DlIGcJVgNPHY8bUVh554k4Cct5KcksrrJ7zHBY9T0G_xxyrtVaYyB6bbTrCayaepWCVnbhTwXl_gck2oZ95OJBVhg8tahD2LvV2mvlFZZJCnDByoaeWeFC_3li614RphXZcspU-LeBHJxlJ4vVx5SbJkPgXEKStHd5c__tl9vmCBZS0UoMLKvk7_qM1RKrPtQmkJ3bw6DlHzSt49Gvpa63orwzSlwEvRNXVJmbSDj_ht9rGday7J806ZJAFr2f-RKzPML2i2zDBO6pbt0pmH__FVdUlJT3YHiH-hC4N65NMElB-AapN7r4VxCFQ56MMRa1V4wov2AI-aRwOcJb48e1Kz95_WKOjf5w8GnvQPuVR76OIgjT_LMh6jXevIl_YyRNpLVy-vDp6FJZ8eF22MKEN_cC3MyncUptM38K1pjOP7jcX-0RKU9tcWALE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
کنایه‌های امیرحسین قیاسی به قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/92864" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92863">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdGen2XSe1b38JDcdtpT-n-OL7aaOFpxoUFudgF301tt5pQ86jL-J6fgSOkJ_A5PmWhhCEfXRUxiCOid3DZgbERKE0ykYzkxadQPVGhBTFsZPqhcrmnit3H1zfUIdDLOBXYrOstIoHDBcdlXEEAk69oSVG-uiuKscTdHe0nfZMcWpNB9f8aFffBGckAicDnBrN8QdI-mBw5m86VLJcFZO_fdjJn8AgU-rUbUeaspIOQvOGgkFTkpybSFomdyl3OfWpeUuc0JG_fCWTZo4jbOYDzCiTV4guBH35ubKjp5FqSSaR8oLj-dM9eFoorGGaDge0P29OpFRonSjrJHxjhe1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
در طول سه جام جهانی گذشته، تنها دو دروازه بان در یک مسابقه 8 سیو به همراه کلین شیت ثبت کردند:
✔️
اوچوا در مقابل آلمان (2018)
✔️
پاتریک بیچ در مقابل ترکیه (2026)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92863" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92862">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🔥
🏆
🇦🇺
شادی‌فوق‌العاده مردم استرالیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/92862" target="_blank">📅 10:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92860">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBT8iXJZ9SHkD1ThPSgqnihYPwK5Ue7ja4e9fehiuU0jgmJoEjMLKI7elvP1JK4K_zjgMfVfVqPR2SmrkAqVy22gBOeDBqBtPNx8Ywasm-Yi1dTsAQdDl3oXK5Zq7Xi7fNqs7Fke7lmrboFdTSPRnp5rR0MxqvTuw_krvdxrjbPm7xALRTwZcF7nqG9Fx8VheBEyvjJdjswYoomRzBxCy4fhgzSe0sg_4gQxreRCkRCQWYi9tEL8UPK5RHBTpD-MAM2SmdBPxpbrzC0_sCknOTN5o6qm6cEwb9pmyZw57RTYmLbJnu7uWmlLzzjsmtObQFViXW7riic7IeI12GCnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دیشب اسطوره‌های واقعی هم تو ورزشگاه حضور داشتن :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/92860" target="_blank">📅 10:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92859">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088ff3d6a4.mp4?token=ZB3qIic4HQgvJwKqqvuCNGaycs3bUVDA3W62G3KuPelO09EvKy28XSL4RUPUAZeokWdBqYWYmK3ujiiI4jI08fVTcZ8I552kvNbrWChR798mM5cugl3rq337hacEjz2VKT3uXjidLLNW4ITiV7_W4mxOGyK-O1gYbr2LMH2FiJ4pxnyWujw5Pb75XF2Ez-5m3Plv_PMA4JkSagyL2L1cgjIO4O44DGKeny1ATvvEjj7UI7JJZfcFK-Gn2bzIJbQnO4lxtLPyd968MCabL9MnhVdOJZCSW9vqrd4NdKJUuIdoKS4GbE4L6LerO5X05xWrwelxFGQkmMMfSzpZdtS16z598M-HPZyAUcJqqlwYixO_dgBL552ihUnvP2myEZ7XKWf4fKpMyC-Vwzve6qJmjNqVEr0R6CEBfoWKjZ0Lh6LfZ0cnVL2iwmJFhgBMOgs48sm8Qrq1JkOPT6Sl5L80bAP3-loly0RCbzW8BlJeiHkCPAFUGKMBSEyXVZnnlWl-BJYzG_c3l_b8KM-XbqIA0NO8qRzNEilpKEbYK8gbt5-SfUT2jcvnaINBHX5V0BzrGQ3e_yHmQ7OYyutUTEji_NvvrOaAGtKLfdjmiql-89vEpp2DqfqD_vfgg2KIUQVh3MWqopj1kgg5mISn6Z4SlOTHS-AeGHzSiJBKzYRfVFs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088ff3d6a4.mp4?token=ZB3qIic4HQgvJwKqqvuCNGaycs3bUVDA3W62G3KuPelO09EvKy28XSL4RUPUAZeokWdBqYWYmK3ujiiI4jI08fVTcZ8I552kvNbrWChR798mM5cugl3rq337hacEjz2VKT3uXjidLLNW4ITiV7_W4mxOGyK-O1gYbr2LMH2FiJ4pxnyWujw5Pb75XF2Ez-5m3Plv_PMA4JkSagyL2L1cgjIO4O44DGKeny1ATvvEjj7UI7JJZfcFK-Gn2bzIJbQnO4lxtLPyd968MCabL9MnhVdOJZCSW9vqrd4NdKJUuIdoKS4GbE4L6LerO5X05xWrwelxFGQkmMMfSzpZdtS16z598M-HPZyAUcJqqlwYixO_dgBL552ihUnvP2myEZ7XKWf4fKpMyC-Vwzve6qJmjNqVEr0R6CEBfoWKjZ0Lh6LfZ0cnVL2iwmJFhgBMOgs48sm8Qrq1JkOPT6Sl5L80bAP3-loly0RCbzW8BlJeiHkCPAFUGKMBSEyXVZnnlWl-BJYzG_c3l_b8KM-XbqIA0NO8qRzNEilpKEbYK8gbt5-SfUT2jcvnaINBHX5V0BzrGQ3e_yHmQ7OYyutUTEji_NvvrOaAGtKLfdjmiql-89vEpp2DqfqD_vfgg2KIUQVh3MWqopj1kgg5mISn6Z4SlOTHS-AeGHzSiJBKzYRfVFs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🏆
وضعیت این‌روزهای دوس‌دخترای عزیز:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/92859" target="_blank">📅 10:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92858">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TUSNxGbuHm2PoAoZ65oRhVHeRKlYBSXBUP5EMtSa3bmlguu1ne7UBEpm3ZXniIqpCTOS521KE-MQu8bD9jHZFR0au9wTpC0iGlVHNsYB8ufgd8Ag8ObpHmGrqOEBanfkVaffOLmHXO-Rnyv16MVNzGx_F61V7J6e8QBIamHXgN8upk-FFM-53QNKMF_BMYfkul8XgSCvIYePeFqDPEaI6Sc_3rJOWi2xsb3ui_qBiGUZEnqDvstDH6BdzGLi5Eyz-BJGVyFJ-lRxaNYLifOpMo75FoBOfwT32kuCdRYqkwJX6oQCASVjWwPEEEydKYXiRf5fL5khyIHpMxK05swl7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایج تیمهای آسیایی تا این لحظه در جام جهانی 2026‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/92858" target="_blank">📅 10:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92857">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcfc7ed9f.mp4?token=cV4ozZtUhgZr3SuMepqijsd6Hn5RoKuIcGaHjhFPYaFLgczyLaicsx3HmQBzPC-n4W-25JmzWjPU344Z5vcMWcmmJv04MFXbc6SIPDDrNIaE9fWsCziCMVg0Ig7MvGHCA3mloC66bxZSUrEEm-C9bURTf9p-1H5g7kw9R-rTi7Pqas42VC9GFbDxLVcPeUiMbJjEDp3m_6PXfXMdpB6UOdVdmG9UED8UL4NijEEXSekreizoeCJa3r9O7gYi9SiSKI8fRbrQ5BSBB6sNeCpf4zDmn7ZdEWzG_q1ITBCfr7knPXGoS7G6e6nH7TNrsOOmoqYAZWXpBHYmysOI5pw9oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcfc7ed9f.mp4?token=cV4ozZtUhgZr3SuMepqijsd6Hn5RoKuIcGaHjhFPYaFLgczyLaicsx3HmQBzPC-n4W-25JmzWjPU344Z5vcMWcmmJv04MFXbc6SIPDDrNIaE9fWsCziCMVg0Ig7MvGHCA3mloC66bxZSUrEEm-C9bURTf9p-1H5g7kw9R-rTi7Pqas42VC9GFbDxLVcPeUiMbJjEDp3m_6PXfXMdpB6UOdVdmG9UED8UL4NijEEXSekreizoeCJa3r9O7gYi9SiSKI8fRbrQ5BSBB6sNeCpf4zDmn7ZdEWzG_q1ITBCfr7knPXGoS7G6e6nH7TNrsOOmoqYAZWXpBHYmysOI5pw9oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92857" target="_blank">📅 10:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92856">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLiKem_Re2e3xpOso6LSHjq0YyundC76WTniucoXZTkw2NeD31sYTdeBkCiJgen5TNcORZBu8l8i0BRdr3MSTIqCZEgbt2-w5kEEJVY2s1kj3KDtmALIz1oH6-Cahq1-MdVmC04tt2xPHgrtIOkOz-ApuswE4F_Slv58ZkZUCc4fNEfjYiDRw9thODArs95X603kpq-SurX-xcZmNU1jN3gpRPIU-t1MbdjWhP_0xlYPdPnAwJzwYf2i3DJDypZdl4J7XeU5-DafHICr4oWgYQ1eUPRCcVKlmPrLLYZjDtd4y6M09yfcZTj6zI4p7_tBx_dO5fg-AAuPciZLE30Lxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/92856" target="_blank">📅 09:54 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92854">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohI8Y4t75G4PMepFWY8gvIwCt5-pqWmYmg13el9BhfbyElAFsJpxOEwjuO8uSYHqhpw0PQX8sZoANvKlxr6F0RMxFIUiOjt63RYKRyLtaj1WJ93wUzh-ZoAiHA1w77oPjOKT7-cMSHwSzAu11fDYY7gW5Qu324xy7rC-xoywj4xHWoyJB08t1bngGNxfopCUFTQ6qgFnWsKEvUrKdrXXVFgeNgWbu29S67cAXiXmHDmm9TLbIN_PXjZLIGQtZgjUw_zR7xKoJX9Uy2VekhugDILG2QjPpmI0eqxF1DPmvy_0M5afYsuk8BknW5SvcO4O8ND_hAn5fmV3qycn3jefrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو:
روبن آموریم آماده پذیرش تمامی شرایط میلان برای هدایت این تیم است و تنها منتظر چراغ سبز مدیریت است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92854" target="_blank">📅 09:44 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92853">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRBmQdXt2JbVujqKN3ic3VlotHEa41JQu_eMr_38b8wFEc1hqeIz-a5F-hmA_wW3MZ_J84CudJMmQQW7kjemMnTP_XUZ2NV4w19hFivJHafp-BBnRtBW8n8LBREK7bDUk9Morid_8v_U2ty_KoQ7pDQrpi0uLa-RxSji35BDhut3ySYAdwD7ydAClH_nO3w_XIPCMYcDnc7jbtzNf-jJt3euLK2T-MUs7CHrnI_uThTvaqFxwLCm-JoSkBznMEF_ST24AMqlVTI_Qba-lCTrPKNiUzPoKF2uwJqhXERkFnT74yg9teASCw8A1NaZ77Bbix36durRsEO5aM4SI2aJwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
بیشترین تعداد پیروزی تیم‌های آسیایی در جام جهانی:
۸ پیروزی —
🇰🇷
کره جنوبی
۷ پیروزی —
🇯🇵
ژاپن
۵ پیروزی —
🇦🇺
استرالیا
۴ پیروزی —
🇸🇦
عربستان سعودی
۳ پیروزی —
🇮🇷
ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92853" target="_blank">📅 09:38 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92852">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKw1y6P4rmXuqZSOnYjfsQ6LdlsU0YEqjPdhiqOyOOezRQfdApu_bvf8abXUE83XHI_hgQleA6jhrzJXAAIiCukSiteh0fX-WrOj9aGeF0Co4u7w_bnt8qlZ0qxSvc5rl5NRaPrGLl-N04cbcSr-dBOkGEVtw5Z1DxYndeIRWH6BkTgfiYAVokGqdwyOukb5h5DN4NCy_ycIPhCflR24CgNfQIvW26GMkZe-gPkjaSeRktQ2RgFLxYS72uzQkj8voRzng2vH7ZmwlJafowvzEfIzrp8EbGtUJZ27bugprbJGu07SgLJLCyB1lZzudP_D9qesquBu-beOsEVFJwTNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پاتریک بیچ گلر استرالیا تو بازی امروز با 8 سیو بهترین بازیکن تیمش بود
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92852" target="_blank">📅 09:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92851">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AgbKJaGOQqVy9lpSUBMh916NnXUMdHYRCtGhE7f4i9ErcYRsM_sF9z6CzqeONzbp5Uvrcqay98oFD2XrKbGJ2x3lTCNqo0ve2krb7O8QOEEMeIWD87bOU7nMTR_25PEe6OiV3-2ek0EAOOYdW_TpgYMgJHZZgxbLyCH-Ya3jbN_Ch3x0tBayTxeN3VCxLsA1Edc1Xxcf6_RATs6A1G3gwwTqu5KHEKqae4CJWxH3Z2K1LUn8EQChU9mhp-4mQ5F0bJvRm2g1Ix9gqMn8DSTI2_YSWCXhHeR2KGUriHEomJ9FQHhE5lRIG3jIAZVf5h9eO7kyAlKo_jWsLOzFLEuCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه D جام‌جهانی پس از پایان هفته اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92851" target="_blank">📅 09:31 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92850">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frVC3GNbpFmBWMrl6nLvdOkyG2ZIk21C9ulaStyy5u3t9G_xW_93JQ9lLrkH4aToXHKPNli3HUuwdwX8ctfdyC6SobJf0Je1rZRl9lhD_8zfRWwL5zhWnRWaLhzZ_eaZHukvonfwj9m-J9yhDe31t00ELGnNdogF7MxDCqAitOv2h5poqGhGkuOZH183AkADmZYL_uTZaeCErbjEXFXfuoQ3OFswpeTFlYofn5pILX0eZoKV-0DpW7QUBrxh_AlHH63tuVX1nWtUqcjzovubr94eLh1_7SZ6WDJ5Hu7gTiHTL_OVO1V4vFX2Naf4BlFEQ6hd1c0WYpS-oCR3ISA5hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
هفته‌اول‌مرحله‌گروهی‌جام‌جهانی|تیم‌های آسیایی به دومین برد خود در این جام رسیدند، ترکیه بعد از 8 بازی شکست ناپذیری بالاخره باخت
🇦🇺
استرالیا 2 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92850" target="_blank">📅 09:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92844">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H7kEu28YwfrZXY4BIqy4npoDYP8aUBqND4sp73BktMQ2rl1dbhusciIy8oOvrr3YicEzcO1hlnJXJ3fyfh4qKyOgTnIX-lgUl6uVI6eQLAs2r8X6AyabCzXpPAZjYLugm3jeJDk_1hA0nrIBDjYmEu5PJCNLc-wR_XQOu_5FIZFvVOBOJWbir2QaW66XC7GcU8sAiOnakB7L3zite45MgBvzQmwSP8Vh6bdlVST9Ve6EI_KAw3RmdqTtOTBb6pyj9txPgIFklXS6OjaRwIiA_k76TxOiq-0TQ4DDtfd511FCULUE2npDVZGPe8sr0JNjyAOpgGLBv0RkPJZ2nIXuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIwpyLNVxjDesfdnL_jSLpW-2DdwHInrs55qT84BOfpPfipKca83T4SWorSR1Bs9swidDbnzOAGwEVbllFhVUr9s_cWgd_kdM86Vt4N4FIOLItm1RfkgPWJPUxmNjscb6DSraOfH4ONolz_5TBAsKJiitKmYzVph9QKd_IDWyt3EhTjFroEQn2rRd0Un-62zPT0sC9HgnoDUdHxL4qxp8oZmctDdOz9r7dfCwiI7NEXy0UD8kj0Gvc6hs_n5QMjYjDucazi1xhxr5HpV7pnR3DZQcTzXppmLyRDZhpSfoaFYHVZnokPPbirVPFjflfKcGRx3KIAav2spP8i9Rh2JRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eO-fdgxjE9CPTyx1CXUEmGhOm0CXUhTGytgq8goldn07kPufzSjjskuvQwHJ7oHY14MBde8VNvVB1Rik03rC03L-Ywfgs_zphU3118Am7E07O9lUOqJMR_0BthlxmrdjgPV8xt3xjVYI7ep37-VJUZMNhh3nt6JNSSesZpehjGm3c75M5r6ttGY63iGU8BQ3r53RMW2KZ--LkxLgJ1COo-pTUhPrQY_VUH8qeQL8AVQKXBPLS7I8TrWfTWWHkJwbUOmdi23CTZWpSDSj9UGpiijsalKD_ZsWRRNA4FZ-fTGBNTAHAGkymyRodl7Jr1bb-ea9h4eZDajOuyVTD6atgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZuBNez2VEt7Ig8EoC3MXYR6DNUyekI8Vy-ftduHTyFv7k0L4Ki8su6SJlA2hCVxAzbMH_HSVIJEorPam9Peni3f4HIAM6KvIkWS1zmqtVBqBoa7gqsQ3U-8YBLxpdDSNCzwqLlpdlV3qoEjayZl7dbLrVKTdXHS-fkAJa2Ds9h7fY1TvZfHa9eQmQLcivNMJynxrWr-JWzq9KmpUHaWOUrgdM25qT8XQEQRBGPDWeDOnHBmGrnVAmVpASsyyxZnoDdPEg-dNHNDXKnY8zYjPkheyJzt1XCPwCLZ8ShPIxdHE_jXdrqOKitdP-2caq5IWPiEPtQ6c4NRzoKJwFyjkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk81fqV-tY0q7osEalQPGayScPxtB0y0HSDOsWMlMTM3IzajDhkK7r96GUD5_9Q94CYLGfLyCH5_90YZOIBVVui6bolET7u9v9lHRbiBiPAGzYUHXdzhKAQugtf5IDpQf0pVPEwEVthNb7AQR4OuiIPIpAXlLbOkacfcbjzndjywvVV5C9jmQQ9qnBqZg5mt5hSiQvbhL01LpgVkpp2tDumv7MH7L2lFpaboZDUiL5lmt-t5ClKTKRQ0peb7xGAYNZhtNp8Lu2ruOrPL5-zFKQErhQ9zyi6dRVxkYS1uktF-mceprkuOxduVmZ9qbmcbaq-AEAD_sqzcs75YOTORzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzQ2onVLo3tZHK7ZiVSoES7CYlAeRMu_KThDouAd0VlzyEERPYlCpNjaLzZKdrg5g73wa1CT-duul1zFuIxB2_21_-XUmKR_1mzffDdhod31Zdw45M0iNU5DdwxIYo-cyxFyqZvfTpGv8PpnJdyAWxA_Q5VogPc1fa2TJOfKKC9veGMw2gHC0ffatRKtI_SYYsMIQU9X9Yn1pJHWNwZPYgSV_iH2ADsP4d96X60IJHC2xaqyNWh8y5H5DyT4qU2W_5nIA3x135QKHWfzPR2qnUPX4zh63zlgipQULj7t4nNpTYyIKpH0euJeU3v6dWHbDko-pe4MQ-P8aS9NLeiEng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
استایل جذاب همسران برخی از ستاره‌های برزیل به مناسبت جام‌جهانی
💚
💛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/92844" target="_blank">📅 09:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92843">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دفاع تیمی استرالیا واقعا شاهکاره</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92843" target="_blank">📅 09:18 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92842">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6857d54a.mp4?token=AAB-FU8zs5OeqB0JH6ym6tUcIEHO_ggkgPoDC1AQrbHvhrY9WE_r_UVXOB6EicxOagxNgXAr4j9s0QpRRzVvkvqE2Zz_Olrj3bQMw1xmGQ-mAPCrPOz0J73om5z1D0z5EZz7-pOGku_G0XNac6k1vnVHn7d3F8x6NZHlI0pyY1YVXBFfOm4SeWhP_VYMZlo01ngM5iO-0v4V8eVuJ3DKlHH10j0mRgMp2BavxCzd5BVr6imQN3-XF-g5_AKoOOULPbbftDn5lykSoi-9g0HjdONmkBw66F0v_0TYQctrrBrP-_xq02a9xOVsIcQi7pZMeRU6btw8ZBzLAEsD20_lrK3EJksDob7eEu4lb0y19vwu7OH6xPHug4Ad_AgmgYDl0BNN4Bxblaq_uuGAzfYdjvnwj_zPhiTIkRGVCUI5ACeMrUCgUPQ6vTnV3NYpwNEKtoVdKVGkZimegEN6WEDuOPUIH7iOs8aymk_L_2P6eXqWU_2jFT9f1c3VY58oAvamdber8Wvyx2yo2d-ZhrvbvupFfv9oIq7sTpOs6tc5rkdZ9spLb8HmQUvZPy9DO6XiGbDjnl2KYPqx2g30Oo1M2MVkpUntVPUqY_8JMmOjmMTDbCvfCbuVzLt4ly3LeBC6XbuCfc1EnZXEnk1Rm1cjBpk5f5DWTYEWwxEOiAg9DOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6857d54a.mp4?token=AAB-FU8zs5OeqB0JH6ym6tUcIEHO_ggkgPoDC1AQrbHvhrY9WE_r_UVXOB6EicxOagxNgXAr4j9s0QpRRzVvkvqE2Zz_Olrj3bQMw1xmGQ-mAPCrPOz0J73om5z1D0z5EZz7-pOGku_G0XNac6k1vnVHn7d3F8x6NZHlI0pyY1YVXBFfOm4SeWhP_VYMZlo01ngM5iO-0v4V8eVuJ3DKlHH10j0mRgMp2BavxCzd5BVr6imQN3-XF-g5_AKoOOULPbbftDn5lykSoi-9g0HjdONmkBw66F0v_0TYQctrrBrP-_xq02a9xOVsIcQi7pZMeRU6btw8ZBzLAEsD20_lrK3EJksDob7eEu4lb0y19vwu7OH6xPHug4Ad_AgmgYDl0BNN4Bxblaq_uuGAzfYdjvnwj_zPhiTIkRGVCUI5ACeMrUCgUPQ6vTnV3NYpwNEKtoVdKVGkZimegEN6WEDuOPUIH7iOs8aymk_L_2P6eXqWU_2jFT9f1c3VY58oAvamdber8Wvyx2yo2d-ZhrvbvupFfv9oIq7sTpOs6tc5rkdZ9spLb8HmQUvZPy9DO6XiGbDjnl2KYPqx2g30Oo1M2MVkpUntVPUqY_8JMmOjmMTDbCvfCbuVzLt4ly3LeBC6XbuCfc1EnZXEnk1Rm1cjBpk5f5DWTYEWwxEOiAg9DOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇺
گل دوم استرالیا به ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92842" target="_blank">📅 09:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92841">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پشمام استرالیا دومی هم زد</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92841" target="_blank">📅 09:05 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92840">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
پشماتون بریزه؛ یه پسره ۳۰ ساله تو یمن که بهش میگفتن مرد عنکبوتی و شهرت خاصی تو صخره نوردی بدون تجهیزات ایمنی داشت، چند روز‌ پیش موقع انجام کسخل بازیاش تو دهانه یه آتشفشان اینجوری سقوط کرد و بعد حدود ۳ روز تونستن جنازه‌ تیکه‌پارش رو از اعماق آتشفشان بیرون بیارن
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/92840" target="_blank">📅 09:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92839">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">استرالیا عجب اتوبوسی چیده</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/92839" target="_blank">📅 08:57 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92837">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qms1R04l9cLEy5fB5N5tQMb2qYZO89rqnd6y9qoJ-47CqWB8YK_bmr1iST84GJVm0wh5ybDDrltWm5jqsUl5eBnLpb0sj444qOrcVyycjILoO_u1rBuuIhCsQZ9JDCpzvsLQvAcduSXUDud3SApRdWW1MktH1WN-oMlAolCWSwPIVAk8eAJYC0SCU4WDLW5ahsbInjL0x_Nm1ZgPtppwapMEXVmIJcL6vTu9ZcCmBFhS2NntOImx__kiZA9I214tRchZyprtBdMYpTdPo4ZWT5P-8C5lG0HnKCl7_vV1fNvnevf_HLL3NOU05OLCx2MWkRNPWmOECNlJ4CZ4M2muew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه ای جالب از بازی ترکیه و استرالیا:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92837" target="_blank">📅 08:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92836">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترکیه تو نیمه دوم فشار آورده تا گل مساوی رو بزنه</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/92836" target="_blank">📅 08:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92834">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شروع نیمه دوم</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/92834" target="_blank">📅 08:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92833">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJwk-vALlnDYGW5Hb9Gr1JaqRN72hOdkbXJI5rLmnUdYGYBuWGCgMlIyBnODWYeFUGIJhNClSZXDTq3SkpwQ0gW6nlgRb96gxYsOrL3kAhLNk1yJmOAFojobaB8Fn6uPyoHzsTTwOfH-rSpCMuTvPq4yBzm8NehrHOB8ZBIyXCR5CVzuMGXoFsVDscsqxCEP7Yucr_GMeFOsVlyv1oIPxEQezKOfGjS_v83wGlauy5BYfEvXFAxT_Zm1VTA2O0GimhhcT3mibmrMsOKt0yul2uEQihuWTFdFv5Xh5y2iD4XIZ1pF4QnOO0U52khogeIc7nqdxtqPPUhHsmkiBbYSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نستوری ایرانکوندا با 20 سال و 4 ماه به جوان ترین گلزن تاریخ جام جهانی برای یک تیم آسیایی تبدیل شد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/92833" target="_blank">📅 08:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92832">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پایان نیمه اول
🇦🇺
استرالیا 1 -
🇹🇷
ترکیه 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/92832" target="_blank">📅 08:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92831">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqDOUrOcPPB0JPovO0UcA6duYyWRUWa-QObwT5zDpkhFQlR44HKMrtBYeR4EzZDYJe-n1BqR_AV5kfrjXMy6p9sf0cyLVwjlJkpEiFyImhKT811-2FMrnI0G3S8G9DRmRulO8ZNpIC9GtCZaWMl3bhYss0abcLK8eAXUIrdmuuNnMrPLsVizQRCHKd3djfo8zbpm5zNFG_fFz72mgrxz48KWgDOcZ5iuB16rLNtdnqmEnSF-XG8jzO8vl3IWMyYKIHasgGbfNmmJNmkO-VdEgixdXSRR0ZHp4_otM-rjnnGeUeEHs4Nf__sxd_8xerY7uO8xutFGLTPQVP1Esl5FLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
خوشحالی ایرانکوندا به سبک تیم کیهیل اسطوره استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/92831" target="_blank">📅 08:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92830">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29527446d1.mp4?token=qa8UU3WoFu-uDs-S9qu3oo7PNbSS1FpMRc30MQJNia2TcteVRDMXO4uLPun__7XwGEWsG2VlyIFnSRHZAVzx2lkDaNFzxSDpdT0yrn81UfYUXbsTVAMmM9D1PLZsLiJrTWSZyBCW9ElhPr1zbK7GbD82y_XBhgtTTAJJ2rJNHh5oUln0uOL-MaS2J7corqObG8M8QwPERAYToRDqp0P0uq3PmFnrJh8rMMsl-JwSj1kAe_HRSXrWbL7Ic96ZQ3c_-OkQS7KglCjK8T_E7hMAgUxtLIEvyvcgmAOKHxVpZbb1OPjRNIMJkqctx0_6j2u3flsbVRJjUI-DJn62-g8EuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29527446d1.mp4?token=qa8UU3WoFu-uDs-S9qu3oo7PNbSS1FpMRc30MQJNia2TcteVRDMXO4uLPun__7XwGEWsG2VlyIFnSRHZAVzx2lkDaNFzxSDpdT0yrn81UfYUXbsTVAMmM9D1PLZsLiJrTWSZyBCW9ElhPr1zbK7GbD82y_XBhgtTTAJJ2rJNHh5oUln0uOL-MaS2J7corqObG8M8QwPERAYToRDqp0P0uq3PmFnrJh8rMMsl-JwSj1kAe_HRSXrWbL7Ic96ZQ3c_-OkQS7KglCjK8T_E7hMAgUxtLIEvyvcgmAOKHxVpZbb1OPjRNIMJkqctx0_6j2u3flsbVRJjUI-DJn62-g8EuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇿
گل اول استرالیا به ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/92830" target="_blank">📅 08:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92829">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">زننده گل استرالیا اسمش ایران‌کوندا هستش
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92829" target="_blank">📅 08:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92828">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بازی اونقدر جذابه خوابمون گرفت</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92828" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92827">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گللگلگلگگل استرالیا زددد</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/92827" target="_blank">📅 08:00 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92826">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شروع بازی ترکیه و استرالیا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/92826" target="_blank">📅 07:51 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92825">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxIh_tLvvyiMHnmVOak_F-R4E_pbGyo_9XISicQ4sC-aFKnqCNzKb0gtmhwLbw-JM5XgY82bPmSD5zLSUqKp3QVdCoRFrhFHGjU1QbhmvSgPDsqe7uQs85EcghOUmU1e3B1F6VbIFIDy67oUE0sv_TJgF4uVJzyl5afXk1lTZpEar082NSuFTEStPHiC2JxxKb4kqmAi3najMEZM4gkhYT-je2UFmH2837SlZfdojxiFvTa1ktZYrQTU0cZU0ZZ7Jxung_Eran209tlKRWB0g0VVe0hoi-whauSENbU7DRNRSKoMb5t93msC61D-JB2jjPak0eoo-qqWJsreXHLDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل عجیب هوادار ترکیه ای
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/92825" target="_blank">📅 07:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92824">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شروع بازی ترکیه و استرالیا</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92824" target="_blank">📅 07:30 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92823">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9SjY9C3ct8SZHekyz0obdlgG1_5T0VhTvdufyEo2hmDoMZlXucQ6qyawwyLUqOK0jMlnBeO_g0miKZY12F1Wz_0aNFNsoX8bw6Ujn0r-ra1nt6VnIX0Q8BAdcN3imXFcobeHzAQRhzO8FLIPz983XpoIMwbU9G-k-YM7sAoep3p03tG5rGchBfexNaC_FelKJP3CEWFNBBgybStug8IaHKx-hMy396SxWOwn0y3TtJiiTqavxbjo-jqaRKcawNpoeo_NYa8AGa3Q1nAul0Db9XVLO8p655BASFt2EkSLii2sJm7Om8NE8U9h2nMnQCHHMlYoRNW74X3vFThlMv-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇺
🇹🇷
نمایی از استادیوم 54 هزار نفری BC Place ونکوور پیش از شروع بازی استرالیا و ترکیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/92823" target="_blank">📅 07:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92822">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PuXRZkDlo-sSd4ByVIPxYgrylxVh8v6vswYUWriTIGUbaHcvc1uKRdk7MqHYl9ZOo9RfSXcADJKMPlow45pYgnqCo_NcGdkyNYQE_reehLYXB-Cn-Z5iEyMB72joFIpwmjBRfpVPpJDSGW_3l3JNEy47czUML657R2SC9XkvheCWsVikitmljXYZBnirWh2UGGE2hW8W1is2-UNkSKDpmbPMvPk-ikeHwERpCKYPr7aHyHwdogTLF42d4fPIXR2ix_DajAdj9CTz8sYr_IIutoKnZpI1kgcuCOCf9KANrosK23I0yui6xkIQN8eWZnJFA4IQMAV7GJiJJk21_HkQTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
گل‌اول اسکاتلند به هائیتی توسط جان‌مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/92822" target="_blank">📅 07:27 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92820">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fmu2Gl2grgSFU6je5fJmUk4X2U6Vyyk7HylBGuobwDWu_JtIzBnNXieumyiO6ikpwIxM0uAGqshZPxRNOeV1BxTkMQ_Xs4L_7rILxDhmMyW1pX37kXYXNlb54yZuvwwOUU06knEHBvDB1v9rc2V_hTWMprwCSkuhZZMgEWpSC2QLECDrur6dcz6c7YY2O_RdxqUNr8SAsztwMNufJW5SZvQ7OKIfYa1GujA6LtZo_MVf_rThRXhriZZP-5gV8OGY8nzdbkcrvvpr88Np1D882meW4gFBw6qKk14xG2QpUVSH6rrDAwRjfCpSxZ1qJGT4Y4p1_aoBlDY9Ewc2Dkw3Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mp08jc7lruxUQ-Ii3A29dSrZOD6ISXVJHs6dI9vzkupLVDcgfs2eyA2YGsL4nEJuvBEhF_DtdOOtCLdSGfbtpxMrBlheBFfeiIKhOzkulAXfmukOqTt-vk10wKwK2lzCsReRFDfIfTueK7ccWRBh_NTD0th7yNXsY0mp6fCmXfm8M679JdZN6BWmKFuPC2MOc4elzEZYeCzAAMli2WDDXnNruFFAcZxMTpk0VNlESPsdqjZEgi3PLYhNAoXegXkKxDtLacBApbbDqQyh1V-FUSc54hC_cfFpzNn4IQTJlYTxTpDiVrJc6-VW0zu1bHiD6BoHAkwtR--ClkxrLpDaHA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🏆
ترکیب دو تیم ترکیه و استرالیا
/ساعت ۰۷:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/92820" target="_blank">📅 06:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92819">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این بازی کصشر خالص بوده تا اینجا</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/92819" target="_blank">📅 06:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92818">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlgBgDoOXh-uHjjhk840eGwgdkl3E-atkQAGxKq_QUzQQ_j3FP_VnNAAIIJV2YXn-R-Goqvr-mN7y_PO00lAID-Ysa8aq2c_AcCKYIp_J3vXFwSo_hoOfS-_JgO1CGetHipZ-kZmX0TwcU-JAR51j8GwCvB1kmqRI57c3eD7DlFJPEgckUxB_70qG0yJM_d8JfFHx8zaRSPIS2moRiSZzg2qOyDSm7G3ROAGjC2m9ZP7OtYsmLRXtaFnHHj9-d_IAzpV_4ZHhurS6R8TBCaEEoD_q3Lgw0JzMwv50fAASPsZ45BWHEIq4K7MjtP-V7SQu6DSVD9G1ZVS1SryI2i-gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دوست دختر رودریگو دی‌پائول:  «بعد از جشن قهرمانی آرژانتین در جام جهانی، رودریگو مست به خانه آمد. من مجبور شدم مثل یک بچه از او مراقبت کنم چون نمی‌توانست جشن گرفتن را متوقف کند. به او گفتم که دوستش دارم تا آرام شود. سپس او پاسخ داد: «من هم تو را دوست دارم…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/92818" target="_blank">📅 06:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92817">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsjTDuIrpw6Es_DbuvCZgw18lasGjQUKFjHUxo7F4xchDcNPQXG2Uaxd3IIP7TQp3FBKlVBToA99q0pD10WL8lw5vxfXay6n6l2rrCKu7P5y4rhwqU0RbXjV-uN2E6olcSzAjeMPBiARm_XrEwyJ2Cy5ob0zz4ZWjAJ7tdZ0caJigMRTYnvM-KBnBMcJlf02VI8C_GSIaRe8OE1676tbTUK2ZSF9lhGoFTMPGJxfwwd2iKVWGmVuEmQd2r-wrCPLcwCYKKvO6pwZVdrfd9QX53oW56LLNqB1PyL0rnNrJByBrfqzqtKbil6AP7BKBbAcRuz3SuxM10HblspfOSdJrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوادارای برزیل دیگه خیلی جوگیر شدن و اندریک رو پله جدید میدونن
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/92817" target="_blank">📅 05:36 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92816">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAfWyTSpU7PXlVfr8TW1EV4Xfjt_WX9X89I_-34jO2WsgaFC6Q-QvgycIzgYKhLMVppMnHmHHGM2ZvfxE0wiKnnBA2KZMu02uLv_hTBF8t8au96U9fdg8zOw4j6lq6wUvW9oAir4NX2xhWRUwTDYb2W6d8vVitwvL1AG9AgUdSplJjzuvzlTQBkqpjfEB6R595cjIDgqwiY_i4lpG54sIOG8ITjHrbGiGQ3mR32Az0uehY6DmTLy_Ba64qhuUH5ofogAUw363bJBRxFio2Mo9j2QRvflhYQiZl-22x_1YtcJrlUo5hlHuI09BRETpnG0ga5vqebd-pTaqpXnI24xpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴
جان مک‌گین اولین گل اسکاتلند در جام جهانی از سال 1998 را مقابل هائیتی به ثمر رساند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/92816" target="_blank">📅 05:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92815">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🏆
🔥
پایان نیمه اول بازی
⬛️
🏴󠁧󠁢󠁳󠁣󠁴󠁿
1️⃣
🏆
0️⃣
🇭🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/92815" target="_blank">📅 05:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92814">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCcYqZglNBLS2pIQPm_z6-L-XI0N8EA06vxvD3X6l3HkUNRUBOzWO8w8JqKkOG5Oco8sQ07iJiPTgdrLtv-s6omtVdlzmjeFZUO8fr-uAwz8T27tC03xDtrB6R_uGcfZUbkJaryOmGpIaZihKG1N_YO5ntQGOhk025hFQT6iNty1OCajnJm8UqeQy2ucCOPIVfwFbpB-I0Kbalu_GQcoxzjkjGMnGkB_nhBk60jwP0zjNvAMfUYV-V2eNDdcK5eyNYDbrmu6G9z7oLP1BoSAvALdmIBvUexwc2GMhNhXuct8HqzI484L0VUO0a0LojUH94kDkI85MV9-IrZJwEekNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
بازیکن متولد ۲۰۰۷ و ۱۹ ساله خط هافبک مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/92814" target="_blank">📅 05:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-92813">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=SaJVycwVLtcMAQCGDbh37VtT3S6ts9kUct7eh0aDbifEbMUqfmjVSCIA8EioRxTduo7b1hHI21KysEi56EnevFWrkN1-BykkBgJAWmnFDQJsGIABdc9z52TyyPLaip264nkEnGwH-5FL6lCv3gvMbBpIGjiu4mKfWIVJPM-YpzaIRxCcxMzbD5jWy-MA3qZBzmr1aP2FRmOh1Xx2NwqTwq3cc5Bi56r9mofm1SIO2N8xvSJWtDNT0jNPwSU4V-TFA_UNFTOLF4sCF1xOe5Ayaw-QDMEjNJV5H06hfbCcIm18dSwFU-ZR0DPlx88QW_LhaiPA66iAhUEs7WPRt7Cy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bcbb2b8e.mp4?token=SaJVycwVLtcMAQCGDbh37VtT3S6ts9kUct7eh0aDbifEbMUqfmjVSCIA8EioRxTduo7b1hHI21KysEi56EnevFWrkN1-BykkBgJAWmnFDQJsGIABdc9z52TyyPLaip264nkEnGwH-5FL6lCv3gvMbBpIGjiu4mKfWIVJPM-YpzaIRxCcxMzbD5jWy-MA3qZBzmr1aP2FRmOh1Xx2NwqTwq3cc5Bi56r9mofm1SIO2N8xvSJWtDNT0jNPwSU4V-TFA_UNFTOLF4sCF1xOe5Ayaw-QDMEjNJV5H06hfbCcIm18dSwFU-ZR0DPlx88QW_LhaiPA66iAhUEs7WPRt7Cy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁳󠁣󠁴󠁿
گل‌اول اسکاتلند به هائیتی توسط جان‌مک‌گین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/92813" target="_blank">📅 05:03 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
