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
<img src="https://cdn4.telesco.pe/file/CiZGMBNWMltb52ip6FFVQ_MdPlrw446EJCS2fInK8He-cmh35qVVrv5qRFzT8dRUXgf4nxKz5EcQJ942ev-oQpn3Qd67Z9o__p7n5FUUHZ0J50uXGBiufluMo-bYUE1v1Y2DSghfpZIVXEiEU7reW0ukZzq09n34joeapxxJthATJPyvJ235-Wtia9gtDbFLgJhhnRBqsSygkCCFfExnmUtko5yh6YUtffsTQKQeB_UD34qlP_3qG-365qp924abFFBfp0xKrzcweyHx1Od-TEyVY8jDvdbVaVzKME6G4aFrjOkGj23KYzm_hfvWCbNXfSs154KaG3t7d7MC9PGnpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 423K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 16:09:05</div>
<hr>

<div class="tg-post" id="msg-25359">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kqvNrUWa9zLCqijb1p_4nQM_9R41WWLgxVGo9zW98KWNcBgmFy8xtiUUiR2pHUQylFV89O0nW8R7SmcpTcVkF0ybrxxXcNTrvPUBUyR37pCpNIGQ0zGjjMfBNb3-B2qzoXV4EMWoEJ_4P0VyXj1la_yomAkxh_spDPPCbpX3Isq4j9Ocv2jcXKZW-twEaZgRVNu_4YTdaHmMuYpWcJtb55kZ2rs4Ci_qA-uBbNHfRTc_AbVfaaQ-yRhFHG7ICpgB22NUtNBFnOzO2rdgUVyITNY9oFAvTgvGXAMNsH8ektobksvOaONNFCrrPq6MWYFBT_t4hUNfaPx7RlfTYuvnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنانی که در یک دوره جام جهانی +8 گل به ثمررسانده‌اند؛ امباپه و مسی به لیست اضافه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/persiana_Soccer/25359" target="_blank">📅 16:09 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25358">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇵🇹
10سال‌پیش‌درچنین‌روزی
؛پرتغال‌باشکست دادن فرانسه میزبان تو بازی که رونالدو مصدوم و تعویض شد موفق شدن به اولین جام تاریخ خودش برسه.
🇵🇹
رونالدو درباره‌اون‌بازی‌تاریخی:اون‌روز با اختلاف بهترین روز زندگی من بود هیچ جام یا افتخاری برای من به اندازه یورو بردن با پرتغال ارزش نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/persiana_Soccer/25358" target="_blank">📅 15:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25357">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGdpjqhm0a3mztTx5vdxE5UTOtx-bvJ4ZCcDm8DQmhxRvRcfVEZMjxaWN1hZ1vkN2edWjLUGXi-9Aqwqh2beuvi2ZShyuqvD5K4oErF08IczvfE44qykW9hUqbPHNPEICC8HAALDTRyfOZT-QxQ45vKRHYH-CHud_kBE4hLKw_UVU6_tDX1UjC6oClSbAk9kRk0F-d1D-qANqg06hKGRalPZi-ARYCFFt3Sh68iB3iJ3-y4LwB-e_xpV5mC8ClpChzXTL7u6ZaPUeMDaRfLNPlG1wdi9L2VL6-PwlICkqVpjGAt7K_ZCkNkqxqgH-P90L60VwG82BYDMzglh-DTHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
تلفظ‌نام‌مدافع راست فرانسوی بارسا در بازی شب گذشته فرانسه مقابل مراکش توسط عادل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/25357" target="_blank">📅 15:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25356">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=lUYGlGUb1h3T3T1ziJFqZxJpbonp93yv84nLlLRD47yLI96iSvYwbPWxQYkhlzjz6PSsN_h3ZlROF7hwQtB384q6GzYHO5cb_uQVqLrAXlSGtD9ir4LNjOxVbH7ejmyGBa-jIuDmB7iC2aF64EAmyfawcjn8ordNz4vAVXhmlRNlKf1yL9GrD6_QOap5NRD6uArO5oxNkcyWakhjGkybSSODIGNnE7ZAeFuCWFR8jb_mSu5AYxnKuhUAeKiKlDvlb4tiraJOQWWsn-eiqa-WjCBFdMLEkeGL6Uy8a467n303I1abOPbk_M64DSIP5hvAUOzn3w1o9yQmFikmMPtz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4ccb72a09.mp4?token=lUYGlGUb1h3T3T1ziJFqZxJpbonp93yv84nLlLRD47yLI96iSvYwbPWxQYkhlzjz6PSsN_h3ZlROF7hwQtB384q6GzYHO5cb_uQVqLrAXlSGtD9ir4LNjOxVbH7ejmyGBa-jIuDmB7iC2aF64EAmyfawcjn8ordNz4vAVXhmlRNlKf1yL9GrD6_QOap5NRD6uArO5oxNkcyWakhjGkybSSODIGNnE7ZAeFuCWFR8jb_mSu5AYxnKuhUAeKiKlDvlb4tiraJOQWWsn-eiqa-WjCBFdMLEkeGL6Uy8a467n303I1abOPbk_M64DSIP5hvAUOzn3w1o9yQmFikmMPtz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
ویدیویی‌ازکریس‌رونالدو
🆚
لیونل‌مسی که به پر بازدیدترین ویدیو چندروزاخیر دراینستا تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/25356" target="_blank">📅 15:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25355">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=LL1g89JSDtZd6Za2usVjjjrqJ12aOaldEpdrUDyPh38iHwrydBESAxJ0opTkgcCdBiCAxh2Rv98TLuKFGyVHSKBkaePhU80TWk759PCw2rNYmIB-g4_MUHyjIXq5KRl5mJjJJVjZCNZcFqaxSehg7N7smJV105cgUL10VzUAYHUhmFvRl_86FJh67Xc0NMAvy9GP-wfiOcIceDa2AiZbH0SQ-X2QPggEU2JVWEZebci1QOwijDt5pBsYlKi1FbmGYtHMBqfE-elqfNBRkQKBZSGZkMkg0cPlng-QTlSNrR9a9OctASc0ptcXG1jB0ScY89g5BYwsx421FFvoqkWQag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c711fc4ec9.mp4?token=LL1g89JSDtZd6Za2usVjjjrqJ12aOaldEpdrUDyPh38iHwrydBESAxJ0opTkgcCdBiCAxh2Rv98TLuKFGyVHSKBkaePhU80TWk759PCw2rNYmIB-g4_MUHyjIXq5KRl5mJjJJVjZCNZcFqaxSehg7N7smJV105cgUL10VzUAYHUhmFvRl_86FJh67Xc0NMAvy9GP-wfiOcIceDa2AiZbH0SQ-X2QPggEU2JVWEZebci1QOwijDt5pBsYlKi1FbmGYtHMBqfE-elqfNBRkQKBZSGZkMkg0cPlng-QTlSNrR9a9OctASc0ptcXG1jB0ScY89g5BYwsx421FFvoqkWQag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/25355" target="_blank">📅 14:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25354">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H-XymLA0rXiPAqJw6Vs_eXKndH0rUpsSsqZseVgMAwSYUUA2aH3JqHlejbZ3ihRUuGBX7xs58FMDZTpAqwZjKRPcAsM-k-kb6wZEFrkvpLvFbKtDWAk3P5mt4R-fg32fVmWS4I7vSkvnsE7Ro_c9uaWHOAP6cR_MZAKslb6o0SR3bDX3aqdjt4inr_414p5jHYJ8-__vgP0MDEykCMD4FXnmxIn6ehqIa8agPINHPGuvBawW5VodYZILFJS-_CstjoSO7EIffaESzG8ws_Zm2fqZ0mH5nTpwONrlUw2MSdmu6zknV6xHDHYOflA6SDqzTMKwMFaaL56SnoeKINljFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
ابوالفضل‌جلالی‌مدافع‌سابق استقلال با عقد قرار دادی دو ساله رسما به باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/25354" target="_blank">📅 14:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25353">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoohAQJP7iP0aPAl9IBVAb2cO35qWPYby6QELzDjcktNxS8_M60T3SmOKeuOr2V_9JAmLPht7ugoItQn1Cry8ceTaaOBlge2tcLuv5NzO-JnQoPWSVaP93038JJcBHbuAoN1e2kCULv4Gz92AnBAI_mnLZ9k2CG2c21rdsjemM_dIoKVGgwyWANDrHPxDK7PMRRQUkeQ3PKdYJGDexyQDfJESU8iy5GwfeINLQ60IPkNGZO-yp6E5TNQofNRz5EUqVB26dHB43ad9v_UmXZouD-QRAx-it3U9u6vcG9ofkhrFnliaYvk72kX-1P7gkYu8xkd1ohXjjI1sgxg8B9ZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری #اختصاصی_پرشیانا؛ سیدابوالفضل جلالی دقایقی قبل‌ازطریق مدیربرنامه‌هایش به پیمان‌ حدادی مدیرعامل پرسپولیس خبرداده که فردا صبح برای عقد قرارداد وارد ساختمان باشگاه خواهد شد.
‼️
حالا بایستی‌صبرکرد و دید تاساعات اینده باشگاه استقلال برای تمدید قرارداد جلالی…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/25353" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25352">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOA9gG1o2zhW0yfwT06DSHxEiOBsBxWx7nALrAy3pL4OK_68Px94P9kjPKqvhABnCrZdnj-qYodhdWwoAZyUqDt038YJ_c6HKIpIEqJJpaXhLWmtkQOer5xnx336pf5Io72ftnZRKpfqWVpkt96X0TVkgxQ8HmjDxfQmZHItUWQhSaUiyh2NtzGfnSZC2Z_BFgUzEUqfsRFHFNTb19hoqu-l3KYOzjQ_9IHzJzIbFBYJcvSg1sKm9EHWtVWHi8YUepTM_FY1563eA6dqpNaI1VohZzMpHHlylt-Usl6-t6LuO6aflIiHDdfm8bySvQGo4NQhpkJSPDW4UP48XGQFyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
نماینده اوستون اورونوف به مدیریت باشگاه پرسپولیس اعلام کرده یا رقم قرارداد این بازیکن رو برای‌فصل‌جدید افزایش بدهید یا با فروش اورونوف موافقت کنید. مهدی تارتار هم در این باره به پیمان حدادی گفته اگه با ترابی ببندید مشکلی با فروش اوستون اورونوف ازبکستانی…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/25352" target="_blank">📅 14:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25351">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjbceL5nbJFzaHeR-X_0sIiNPAvHOPoFayEZ5Wvb2XAGC-p_zFBrCcDg4oePR5oT4MGmIzW5rHGgl1ZrrvfWqzgrU3kN785E0yN_kRpDvGSmrPMHQLsUvyswGcliR6JRSRUnPYzmjyeV1-20kD28Ks6PMkeBHAMsH-CiVBFj1MSwYoCk2W8Gt6-KxviPCWSF6w1UF6Ca4ACFXK8dWLLhmi51pz_ySkvgworWx_AjvE_V4ymSuHiXEOrDfdYtCvXhrztgg0Rdq5NScAHaGhq3zf67ClA0MWeL9HGXja07bJDMj447RpUyGlTYr-5jl8Cwo52UOFJe8K0Nfzq6LtMinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا
#فوری
؛
باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/25351" target="_blank">📅 14:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVjrPLcUGhViC4Xdn3s5ljrZL4hhHzeMof5X1euJgBUjd_I3Bln2FKQmc7ibm5QnuwHma4uuwa9jEj6vJPiFcS4UbFv8Iva348eBUejd3LgGXLTbF-8nyHvGtXoKWfHsaW8AVp0pFGQZcVoHX4K-edRDswU6sAPA5x-ZgoKmIX2ULWPkoniSL3-cJswEPWkhreQ1DEUThFgCPJpYeMgelzoZmGewiAMNQdLLIMg5KYCbjMrpuKoB1CX_7E6OXSWJA9zPOZg3zWGCg3i8FIebTn3KLtk2eGreGst-b8zMzXu3aDJ1xxdeL6he0Fw-XLZrc4XQAUji4YAM1ITtXFRBeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/25350" target="_blank">📅 13:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR4u6ejCdOHPKxH33cF4bV4Xa3beSQNhD_XVhLXaiWFTSRx20JLkVgp1WE3wCQIn5cNwbtyK7SORtRG8g3yC2B85V56JjQX2E7WrLV05h5LgJJK_YdxFZNTO7-hSLYe8wUE7k-JTL1tyNbPDZql7GJY0eD6-EOMKa4luNwyhmHBRBqQr3CkegRswu_07cqgzWk6BXJMX7WY5OiPJml4-TbdUKIruE_-LiN1zadUm2xbBgFBgfCEPQfHvnODipNCekIsAcjLC0GuwSsaOHmVlKxzQIs4IEfgNEabAJxWkpJ1rL8PNiz7Gw0E3LeqNQ-Yd3OQWYF-4-o4kwr8rjU3CAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال ساعتی قبل باباشگاه آلومینیوم بر سر انتقال محمد خلیفه دروازه‌بان ملی‌پوش ایرالکو به جمع آبی ها به توافق‌نهایی‌رسیدند‌. باشگاه استقلال بزودی 60 میلیارد تومان به حساب باشگاه اراکی واریز خواهد کرد و رضایت نامه خلیفه دو…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/25349" target="_blank">📅 13:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBNkh_stvNK6hNnSBABKwqCe0lHryqqwP9BiY-0UhnJJCO_N8lTZH2vngaKPwbRk9GKS_oh3_i4-Ev2f8VKaGX4MM1l0GacutDW-Ahk1vFwtkTYDJ1ZiEwz6ki3JTNQAlR9fNgl6RUedio1FuLVxrSI1y3KWilsIM6N4FZEp8Y-IUpjaxZ0mcQPEhaxG2MYUdnla5ymY1jguRGfFBf3jSwV4pf58xWRCaV1odxaAluGkf4XKHjIxqa1YucmugMykjaYFU20ksvqobkPhRx-jPlU_ifdPZwJcDwKawVGw6iz8xu2ejma6biov2S_eY1wH3FJIFmQJpd3pzHiVwC2uxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/25348" target="_blank">📅 12:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN0kcgVjIRl0N9OXtFFAKmrEFwDooGG85X98Ks-kefAaHj-Kcukeq6D0d6AFou3ZncXK893aTL7JEhagGmlY7NY2lE85vJez9AbHC7fg8eot2AO7yrhZOq7VFDhSTlUWxROMeOHqWKexeRJDYFrJTBEJ5celCP1mhTb68JCTPyNG9b5RpI2L5Q4NwF8gXiSX0wNKN4EiLZzFp5HVQ7WjRSYv0H0EooRXu7lTXMvGr2LM_uRDdXoMPvGFAEYCA595CONeFnGEGULULIUOy3MsLhDAhiRpl-gbgmHxGf7r8OLSTEMl9P7DczhVJr8pxDQCWAIbedeW2H73e8IsijbbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره استقلال ازباشگاه الشارجه امارات که سرمربی‌آن‌مورایس‌است پیشنهاد دریافت کرده اما به مدیریت باشگاه استقلال اعلام کرده درصورتیکه کادر فنی آبی‌پوشان به‌سبک‌بازی او اعتقاد داشته باشند به قراردادش با آبی‌ها…</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25347" target="_blank">📅 12:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25346">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">📱
اینستاگرام دراقدامی‌عجیب، قابلیتی اضافه کرده که با آن بقیه می‌توانند از عکس‌های شما برای ساخت تصاویر هوش مصنوعی استفاده کنند! اگر اکانت شما پابلیکه این قابلیت هم به‌صورت پیش‌فرض فعاله؛ به این‌صورت آن را خاموش کنید که مشکلی پیش نیاد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25346" target="_blank">📅 12:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmABbc4rhwADA5JBexbIQA3s3E8Kyz2_sMFpRiYGJvTBjKDSQniNlYWs-mjp6Vl4oJ8LlDaQaFUMIXdywNOttzIMmR29ABgnDuQUtCaDgPzVVHUBGkfL5PtV80Oul46F2dp-hfi9FvvjFOVJkHsrvTLOEjNTJZpjCNrsRQp-nyH7gRdl-mv-YsFXLsthCoOsk3ZSt02QjCRXYbDB1VTYrYFvKfCEI8JhLRfjbw5voOrlgO3aU2Og83D4CahFvDabzcRJDwLPnTylIcwXlDZQ9CnNQarpYyJ7N-aUw2O8mL68c9reppUiiC-1JhMtWEBM5rWw6y9cE5mgTJrCOYsgpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25345" target="_blank">📅 12:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1IIOYSsnNm6eHigd5uFKglqDxNt-UzEw63oAQWvdmqIikA4FO8jcPqiFdLebjIK_PAWciAtXoN38xlUTfvrKeMMbF67wCYtKRv1B080XIZsQPs47l_MsJORYCMm4SpXXt6ZgEYXCY7xOdi4saH7KGFBkfi88Y2FpQPSAHgPRNg-b5twkMl4usK3dzLysok21RI5QMrt2f8-S6m93uDvroyL8ucRd2Uc_V5JMilc9mA3WtBndxdYXAFij070KsBiProwrIFVIqlPtr01-_1iaJ0hQX7vLG7dUr9vXwP4lqQzuLBkrnPDAnLUW-jlqVHi0BN6j35jxfxStExkQGBwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/25344" target="_blank">📅 12:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25343">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c669eea570.mp4?token=fqRwsCoiAW4NWqCNvkA9BeMLJPze5flfmfHWpWuSZrzBM-oWT_zNgz-Lj0oFeTaSiY8QOUC-POSW0Xasod8DqAvWxVs-xskRbzOZgt0BwkSHRzy2_V-1tOuBreeJZr5cqa9QL_BiEckhL3O2dsDxDtCqjISFO6HUx_klgzO4ejd7VwYrC7Og8xYKHeiBgp4WPez8mwTFD0bhpuIfmqMm_gw_gxVcmfWvGpLUBhAwAfbVgaDg8NNbnpK5Ci37zIymOq2iO4nZojtnOgmBpJEkxx6xSD8S-ilIRO9OlIsjp-ITqzgj7le0iprGOtnX3roLakFR9IpfsGZZqKwI3C3AArUvAFAUU4LxCpW7izg1hnJ5skceJXDZCIS28pj95ThrUuusPDzv56kjx6-_BM7b9ye9JMy4B1Afl7Ad06xB9XYblM6H0YgRpynMNFrcvXVgUOwdN3KSXJqI_iYZWX4P6FLq56ySF1aQDounzlfxk5O7oF6pQvbC8eZnBRI1NaNzix7bVo0_tscq4JkhehcxPQG3vQktZYRsT9WEbX7UEFooZG2wF9o3SPb2Bg2TMFqQoUCiZdTm1qwwTK2lW7zULzgVvQx6zw-PzMgAys28DAO1s_1orDorN2aV9jDx5MVBnOaS830zLvtQoRr__xFSRb12Ky01Z3Y4J7jlGZAn45k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c669eea570.mp4?token=fqRwsCoiAW4NWqCNvkA9BeMLJPze5flfmfHWpWuSZrzBM-oWT_zNgz-Lj0oFeTaSiY8QOUC-POSW0Xasod8DqAvWxVs-xskRbzOZgt0BwkSHRzy2_V-1tOuBreeJZr5cqa9QL_BiEckhL3O2dsDxDtCqjISFO6HUx_klgzO4ejd7VwYrC7Og8xYKHeiBgp4WPez8mwTFD0bhpuIfmqMm_gw_gxVcmfWvGpLUBhAwAfbVgaDg8NNbnpK5Ci37zIymOq2iO4nZojtnOgmBpJEkxx6xSD8S-ilIRO9OlIsjp-ITqzgj7le0iprGOtnX3roLakFR9IpfsGZZqKwI3C3AArUvAFAUU4LxCpW7izg1hnJ5skceJXDZCIS28pj95ThrUuusPDzv56kjx6-_BM7b9ye9JMy4B1Afl7Ad06xB9XYblM6H0YgRpynMNFrcvXVgUOwdN3KSXJqI_iYZWX4P6FLq56ySF1aQDounzlfxk5O7oF6pQvbC8eZnBRI1NaNzix7bVo0_tscq4JkhehcxPQG3vQktZYRsT9WEbX7UEFooZG2wF9o3SPb2Bg2TMFqQoUCiZdTm1qwwTK2lW7zULzgVvQx6zw-PzMgAys28DAO1s_1orDorN2aV9jDx5MVBnOaS830zLvtQoRr__xFSRb12Ky01Z3Y4J7jlGZAn45k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شوهی‌های‌بامزه هاشم‌بیگ‌زاده با حسین ماهینی دو مدافع‌چپ و راست سابق استقلال و پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25343" target="_blank">📅 11:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25342">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TNdGRzrQxVlAFtN7Pi-s6PL3Yw_3n2j86O292qvHRM_TiL9cUHwhT_vjCTsVZpkoOl10T0Gmc4lgQDZcI-_EDjsW5vmN4f_SFP7IjDNyOoPr0-GC_-ntdwFTog_lMntR7Aqp42mSrSqC9usHeuL23KeQK_N9EK9KdWNMmWK-IKUU0sgRRCNF5IEtwoucV5hM0mXAKpkAGleRtNVqpl5nMsYTcj77B2FhvL3Qb5m0Vl2fMdIPePUfhNDK27z72-0S7X3lG4QMTo6Ar55NHNSIXtZvq272FkXzWhwKjanO-0sjlH1XJ2cl02ioMkef2VCUMp_b8Kbk1LZqFk4VyePoOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25342" target="_blank">📅 10:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsScjKLAfd-7ox1BwgTAFB7p8Zd8UO-_L7C8BnKIjwFMvaCDjaAcPf5LYCNfYfuYG6_C_ArP3iLF9FxJnk2tSO8PN94pQ7oPCfh1ePVPb5SebJ-2lCMz1X7ylPQMK6NFHrwD8hDL-ENELpLtFBClyMdEpoLq4cSAgTHp_1EOOy5kFXDhac0do5bEPB0tANC4K1_7spZNX8yxtMDSc_jjIuO7lR5c2lMlLTMQMBwTeq72rU-hJ_aia2UwaBPbhXAEeEctQa8k2VC7dAmJp-KJ2GWqrbqpEbNV0dxsd9vxYD40veE0ILQLDEIbGdnjD9orVAfiBeGzMyPihNdEn0WWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی جدید پرسپولیس بعداز منصرف کردن پوریا شهرآبادی برای‌رفتن‌به استقلال؛ ساعتی قبل با دانیال ایری مدافع 22 ساله تیم نساجی تلفنی صحبت کرده و از او خواسته بافشار به‌مدیران نساجی کمک کنه تا رضایت نامه اش رو صادر کنند…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/25340" target="_blank">📅 10:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQ84qBwmX77R1LcVPFxsUyfnI3uXvIlEdxvXLUflEKtMS6OsC6vvcYZS7OhrT6_XTZtzB21_CoBiuUGora4TP-7GLvmeM8C3YWkWwsnSk4pYO0N7ZcyygXx0TMoppvDAzx1-Kqj6TqCfD2pOa1S8VmhtAlEWeORiWhX_zy_Cwmm8m2bMubbCWXIKlNF9rpCVToz74RgdIe015aqkw0HSDRGnXL1IkuGOm3R4az64tUwun8zoGl118OF96qtTvzgA-EsiQsAsEKzZ858Ul59MVYqMTAZKwE8CFgx2kiFuyn_GkVaxY9sjxyOXbd3CE6kscneazA-xcXvYnlNG4jSCKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
«وزینا»همبازی مسی میشود؟ براساس گزارش روزنامه مارکا، باشگاه اینترمیامی قصد دارد ووزینا دروازه‌ بان 40 ساله تیم ملی کیپ ورد را به خدمت بگیرد. او پس از پایان قراردادش با تیم چاوس در لیگ دسته دوم پرتغال بازیکن آزاد شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25339" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45277758ee.mp4?token=gvfahH4mCHFb9ZUKmfJo801F3CDMmptF8cwDWH_h-h5MrNs8E0sdbhuS_BOj3j8Sz0h9ZdyxPhtaDASj3XXkGA5y8W1a_yxLxttkjFVb-CRk1vunQ4E62wUhKfB17SpuIi_3tDT-QLYrAmxqw_OMMbfCneKeTtCwm37YVcHsTyEGZkmhnqWaInmZSiItkwbb6iB2Ev0MZABxz1j0WGKUQsFokMvaen8QoqOCm8x-6bGxtkqmQXqMbBk4ctR2vmPt0ArXT2sCeA3-V9WK1r2vCx5qEbNG--ak3Cyl1rWkVocdsSgmsZsqp3misCH2y_wnn0RvNgD6pn1-ItFrEHkceQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45277758ee.mp4?token=gvfahH4mCHFb9ZUKmfJo801F3CDMmptF8cwDWH_h-h5MrNs8E0sdbhuS_BOj3j8Sz0h9ZdyxPhtaDASj3XXkGA5y8W1a_yxLxttkjFVb-CRk1vunQ4E62wUhKfB17SpuIi_3tDT-QLYrAmxqw_OMMbfCneKeTtCwm37YVcHsTyEGZkmhnqWaInmZSiItkwbb6iB2Ev0MZABxz1j0WGKUQsFokMvaen8QoqOCm8x-6bGxtkqmQXqMbBk4ctR2vmPt0ArXT2sCeA3-V9WK1r2vCx5qEbNG--ak3Cyl1rWkVocdsSgmsZsqp3misCH2y_wnn0RvNgD6pn1-ItFrEHkceQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی بعد از دیدار برابر مصر: خدا سر ناسازگاری با ما داره. شایدم خدا داره من رو می‌کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25338" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEdXilpWtSSQ3saVbsamFzdS22FM_pjxkqsq12he-XPJvwiVlG2_vXcWcoFAjA1NzgEXHa97oo2npC3mSntJY5ew-R8lq3YL7q2BaF41vd37LFpp0KeTeUVN1lkzLoqvgEUn3oHNi22DcHMiU4LSANy4JRvIhY6A0IejgWh5E4KnDa38UznogVvfGxJKJ0uf74Jv2cm2Qxkq34KsDrU2lfIlU2gdHMb6WhWgmFgpBr7wEa-xiFWsAl1hcWxAz4uSPqQUtKP1DDIy7e2KKv8hGdY4lvambACuup5yMeEXpOMLh5NYTTFBS4MIARSfhdJOlK8CZaoSrvjdX9jjNTvHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی
⚽️
⚽️
اسپانیا
🇪🇸
✖️
🇧🇪
بلژیک
⏰
امشب ساعت 22:30
🚨
ورزشگاه سو فای
💰
در صورت پیش بینی اشتباه مسابقات جام جهانی ،
5️⃣
میلیون ریال فری بت دریافت کنید
🔥
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
سایت وینرو
با بیش از 400 گزینه متنوع برای پیش‌بینی
📊
ضرایب ویژه و رقابتی
🎲
ثبت نام آسان و سریع کلیک  کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
🎰
پخش زنده‌ی تمام مسابقات
کلیک کنید
💰
درگاه اختصاصی برای کاربران
🔊
اپلیکیشن حرفه ای
📱
🔊
همین الان وارد شو و فرصت را از دست نده!
📩
Winro.io
معتبرترین سایت ایران
🎲
🎲
🎲
🎲
🎲
📱
کانال اخبار و هدایــا
🌟
sr19
📩
@winro_io</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/25337" target="_blank">📅 10:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_ya46_JdJ6ayzPSoFPO5rhjVwdsQIbW7atpx-hoe4M02WS9lAk47d-4g10CtCWsMyyKkT4oMH3j2uWBw5F9NpGICP9K_2pDss2pFkoYxqfuDNpTTdUIAuVbPYnInLOu4wCqxit8mXGrDLPw4jKT8o-z1BKcNetoa0LLgsZsQU0ZcWhlCFOcLxtPBLUwgZEGxeQC1ZD5IQn8hGSJS8Jt85DuKsyamen9SPsbxG-mwvnSjRXBIU-E1m7lQEhgVAnzMooi13ry8vEV5GV-Yn-3kjmc7UzLy_i9zFFrs5k2EE0VxX5zRgE_LuwzbG4KagWM_G8YxhTCokVZhtwaay1osQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ دوستان میگن امکان داره مشکل سربازی مهدی ترابی برطرف شود؟ باتوجه به عقاید او و همسویی‌اش‌بااین‌نظام بله یه تبصره‌ای همچون تمدید معافیت تحصیلی پیدا میشه و خدمت سربازی او تا یه مدتی به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25336" target="_blank">📅 10:10 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sES2dzWw07tQpPgCa4YOC4UjtfN7JO-IChEnyx5sCnSCQsDE-VOUZ8tizPxA-0nsIOmMMt_gAphO4Krz69SfxkXRzsXgMmawI0hCHdVhDjrCFw3RSVE1FCH3oo3QOf9oCTSW7OntOCSG2kcDYMwntI4YYn0SuIIzVtq291rEzZxg4HrXbjql4a-EroIvfenew5CZ43Z9kz5zlLg0cKzo69wDbpxUrU5zL_iOfInroEHhjkMRbJp5B6r8viIEjlp8z9NpOufpgXRa6T3bMPKuk73pzAntJzWKLeqKcBxGzjbd99LhS2HoODyfxMOWG2n07LDk7he7_EXg9XHcu6rC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
ابوالفضل بابایی و سروش رفیعی دو بازیکن دیگری هستند که بااعلام‌رسمی مدیربرنامه‌هاشون در ترانسفر مارکت از جمع سرخپوشان جدا شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25335" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25334">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSDoDkqcWTkN6gsSeZ2gwiE3RNOkcUSJLqgRq1IoZBv1g0WWRjqDFG-v670pBopqM1yo_JMYtjuRdhg7AvnFGFQxvEHy9f_o7rk0zcOY0dnKbi0GGCOLaxUKfGWGokVj5rHz68RRBouEYYnOQ22EPzTMrnnUaJMEM0cfsuFTKrKUkYLe1hAxYYPaZt1Gy0sLAVlb6HRrLR04zmvin7f5c6iyTlZ2LWHJUX66_kFuDrf7Spx5RRYtg_Tt-eJ9C9CxKkBan28xcUnzSFgvXXpGadpPV1pyAU8OO8wfiKCRsAXqfNlRTMMxXSwU3uPr-wVESbQHz9ePy5blXIu5At2QTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد..بااعلام‌مدیربرنامه‌های مرتضی پورعلی گنجی، امیدعالیشاه و میلادسرلک در ترانسفرمارکت؛ این 3 بازیکن رسما از باشگاه پرسپولیس جدا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25334" target="_blank">📅 08:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25333">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyqZRwNaWgoIpKhd_ew3Hda2GUA97pQtGtaNAtk-rcLfPRA43OOjfvS7--WQdPXBgoR436mlyi7cdC9m_X4G9uOBYAa_0KDVM-hJdCg-smwIegl6z8aQv0BAIZ6upMQraFU7NRMmbyzwive8X8nzEwLxghJj1ZfQMkMQT5aNIcGwKtwbXH9VoMa8Z9r6lVCExZAFAcq7nF3lYoWbxLJlLzfTpl_MvvTAot2Addivs0_Q2v2t-7P3c8mABouVuyQ40lFSh6Te9eGEFUpB4oLbb0EYkVLxOmuR8GnJPKm-GxqAiLQs2_mqhZfEvGd8A5H4lEs_RrqhI0nWUDFcuIYuDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25333" target="_blank">📅 08:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25331">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OIglDWH8-9VvWf4ZKQlUUh7djO4tRJSvbSeg2GB17WMMkMYFlZVBmld6URSVbI336h5t-WcItrSJ1QCB2tSO_ph8_MvF7oQiIYrWIyIBx_lpGpS-UkDLaf-BpVdRuIniInG6_760DH7YIQawO-E9tGbCCWVLaUpRZDhNT0hqyqvj1SbyUTiPr-L6ZO4JbYDys2E3VDHxCS9hfK87cOLsVnLXEGut9eS_Fg5nPdpJtf4NrDw3Jo3030UgjOVrOwvocggE36o4LatEl52-EqnBur1JW8YCmDelyX-y3EZPrAbFbdtUGJu2SM25aJlz9PiJab9hrRNLzBeNrJcYqKx1hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LOPhgMC43DPXLOg3btpMQvcFTCIpWvOfzGbxqFOsvIpSCFD8Gm0xC7tV5q5txoHSLKFXlBBbwfYVlSapUC6GJDpcoGJBsrQeBPBjc43aHSgxQhuiQ9NiyNyj62h2j5lWmFMKs17ByatJO9W52jLTTQFXRh6F1t9aqeIkL0m_AxaE8F70J9jsXBJqtoUwK75LaBVRCuT6puyU2Mfmv7QRhQ-e-Am_FDi0flYewwNxLoK1ITBsDmZi3-WR2cFIKikAhg3N0-ae_QYod-guqJxoD74v6UmlpiCuk_XY-ANAcsQDX8jsSZbFHZzaCkj6ZB1quyF0ghbQVKDW3LnUcqk1JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🗓
#تقویم؛ 10 سال پیش درچنین شبی؛ تیم ملی پرتغال با کاپیتانی کریس رونالدو به اولین قهرمانی خود در رقابت‌های یورو 2016 شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25331" target="_blank">📅 02:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25329">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rW6UVKyurR5yjrFrcfiLyAbm5aL9nOI06e2X5I27NPJlltVlIKpJKhYVyaXoS_TrC81VJ6pqppIoLtBqiEvXHANCiM89zzOFXwtNDT6BFtu7s_MdS9sei91GvmDglmKTR6Y37uAe5jy9KCTWZvz_p_OzRhS6bOVmKBsifhcxjLdRcsQ-cOrXLJrc5bIWEfYKN8O7Wm5egGylhH9QULLKULTUQuR-L_ojl_PX0Da8OOqNTetkpXdNiZkgt__6tqgkpmyTxDQRYNBSbklPhW6pIFCL0TIPMfJnl3NwMkiQmIN7JKFpnRuaPZS6-aSQThrkP7a_B2eT8G4Pzu2EjkJivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qubd-or5OnLdxAOEB9Ho3DsGYcrvHKcz4vFU1Pva_1hiRWouS0isJIZqwPhmxbU1XKa2RMDf9Rdc0OMDRQc4kmRKmvNfnGZdeGpLNBCh3VF3f2oua9VmBFriaRzBwmSzpxYCOrG7w2yRdRbRbHz-T9V56iZD1BZseOIntVVRkPmruUqDoFh2BkUSsfrZtPm8_qeS3i9Og6v9-3MM1Vv72VHvldAFIcjBb2vYse2LUREw_ARA7WB7VSfsbnOlSAB4zGuLDI6e5036bbmT2vBQhimdMmEBMHXJvNDd8dDO4O0rFI0b3R0jGp5fj5mG1pDlTAXgs6yzXXkEG4lLOMnK5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
ویدیویی‌زیباوالبته تلخ در وصف کریستیانو رونالدو کاپیتان پرتغال بعد از حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25329" target="_blank">📅 02:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25328">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ3mrw21dTDM32Xhkc9oJUa1F_-_j7PDHx572YQZUuR1NAZONeOQhHBd-uFrT0cG8KA-dMEOQsFIQqSHqLQk4oFGaDybB_5KoWDZPJsfM9j5xjHoUgGtTGzpzPx2SIfj_v8gCU-mSqMrS0G2uF8TN44cw4Yz9FVRutUOW13t4Q-Vkr86E-jeRPfha-oCLPlHDS9yNZcrMLBWAfZmr9rRkg0o33I_fPAaaVphVd5Z4dvs_s8pJtTyywfcTObiubxqD03EiMuACbEaBW_0MoA7TKqRKVxg4fv8NyyFzf7k9NY6rZW8QmKyAF9BkR2MQr9X34YrfOG8cWUZhe551YZX9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25328" target="_blank">📅 02:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25327">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsTFG3dUco0SRS6lDt2h9WZOTKwRo_c9ecKAtG6bChWPsmixfPBqt2LLu9xDyn3d0MBoq196pWwY8hbuk8XRtQEOF3cS4ZI6kU9omv6CAFR-DqQsOlgMguTvgoWYS1O8fvrcgYONdBhgATMCVY4sE0xgZWOlSmNFdZ--e3c9I-x6xEtHWVZVq79PhCg1yD0tWmuYA6mannRPolp3bU0jXfVLBstO1G5U1ZLeG-Di_oxfkNKZx1OXnlQHO3d3Sv6w6h0gKO9GP6mv6Zg9w5GwDd_ulxYWgnrwm6xsx8_ZxIGzq9EjTCTbsG6_hkBQQ5ASfksSQjGsJMxW2DW5x_X4yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25327" target="_blank">📅 02:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25326">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l24lX3mtdGc1qwr6Xg8gTGHw4C3VeEyM1L2KLRS51Qob2PIpmnTZz5_eSmQWBwdPD-_0yp65ZbyZd-ZMVJKC1yrIJ2k0mQr6yHzQh_FwucW-YEqB6G1yuxj6cH5L31qlbXLKXnZa7c8W-c6Op_cQug0jsHN5mmbD16ix8hKkmbseTmcT8blBWvsMqEBdMXF-1BK8CkU-EP4iFUXwWRvhSijMEQlb7ZdbFj5z4SShwKWzkWOOrVuR59iTLUJr2iOmYKu_aX61yP0nIvqZeXA_ZW-CkRqnVFkchH8hWBhO7f0l-xRjd3bYwSiFLglaLjjJ8krhg0-LViVzI4lbdb8yUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25326" target="_blank">📅 02:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25324">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lv0mptURIIWymCGoYd2M1RLI_i6ZKmWAVVLXQDfJK-LM5OMcpveoZUyDJ_fPmwHlfWHZLPfof89sD3-UWfpRUQdpyug6zjr1K9E0lcdS62Mf2As8VBOs5ZTDfqzZRoq2gs7HagJTOm-nwD8AylC2tWxf1V-PVXaE_jaLgrmuoR802CdED8h3ED6UCapfwSi6EwLwPLP9tQHtoc09ITry12xEcVBZKHzlolcqCp9t0fmDFGgNoiqxSiKwIes1OVuEoJXO33-AM3pcWvw5mo9kUPJaNdn_yfC7XGXXdPSQMqE2yadGSuQwZLme7VRdI299_4C_iLbPmJC-PULFPSDJGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DEoCyDFbInRkff1-08-qYN81W0dtvuC0OcnuV5ja7jhhs4lxopOynVarp5YUXykzdd_0CxOHDma-CfhH7whr2_3h7O3uTXdShHH7AptYdR18uIIETrVvcWTp7oENCXZuq09QfjlDADdftuOPKoGqCcUuaImX40BGAVe5w0vLYOeNE56pssmUr5ZTrOJLMk9pdJbSJ7hRN85pOh00x83zg14eHZU0fsU9BaW7SMTaKPLyHrMplWqUS154PxlLmChHZSpaDiQK3xyIAjgFPbCnT514u2YxQV8eFW7znckUbyjqb482bC7PIgIBhu3EC0ALBv6zCci-7T96KBvYtr_5XQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25324" target="_blank">📅 01:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25323">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeDry0iwDaVNvzMxuhjueGO7aHQJj_KA2GwocZbwUTBW9MCzWe5QUnvSWuArKtMo_oP--eKuGCuuInEAL4dgida-Eu2Nbx-7SLzHIYjch1f6pfq1ZvWRS-QONizQ46Mz3h2eH8gI-Kn53oIJ-pgQzIq0dKZXBm9x3ukwAEQYsKT9UloGf_3JrBx78tQbtj1l2wTH2sMpN4oztNXwa1cmO42jeut3iL4UJPTmBdR2sCIwJ0cRgeiA3QIoGlaFcpR0zE4-aw5kf67OxZMRdx9YeenMzRm_nYnvKoyysaIlxWmXSEANbKn1QH3synbYupo5uvFMWlrxFfDz--vlpuj16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌امروز؛
جدال‌اسپانیایی‌ها با یاران دی‌بروینه برای رسیدن به فرانسه در نیمه‌نهایی جام‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25323" target="_blank">📅 01:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25322">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzsQRazrofipKptGSFs8VEYHUhrHxKqZErITAjeoj_0PYT3bdJUQpAMi_P50B6KI62QfLgsavcL2mr_ALwkj4F1hlsajO2UUxQ8-jlo0yRuaznn8-8KQicKBxLJe3oDQd8XK_Z_jijka0_ymUd6reuFkUUdRjKVUOXyJ73aiZ87Unu47XRY_MnxaUeQH_PKAhGqxaj1PZfLXSVkRADIUTHcSD2Sw3_0wqa2PVqolOXLBS-WENMHLpgHQfxk3wkwAotDqpV5VQ56XuEHp4F4iS2DQmTvFv98Pr4lvcfSEVNGhpX6w7CY6HA5RkzavCmRCS0q7i_fzS9QnqR33w65dmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
برتری شاگردان دشان مقابل مراکش با درخشش همیشگی کیلیان امباپه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25322" target="_blank">📅 01:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25321">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnjyAF310Lvy2cIl-qJPjxF-XoBI_ijDFpOhjRh8xwyOIHhtpNaBaOrQyE08U0lP0GLb3ZWaVTBEwuAl-7qY55Pw-rr4XRe9TzTYI6JmgKamrsUayIeNaVpe9bckV66PP144W9QDyuWdzYAZQrngafNX-fy9ehSsrM9_kGJA1dqwhyPgDECeUe4b-_QajMUf5hVcXiwdBHr_a5Gi-604X9HPkIQQvFZczrc7cx4ajI__ymr3BPyYW5B4Lel-vi2SOM05GOAHbFjAn7RiLqNw1uZ9FRigmoFJ-g3E6oa5UJfGXPNLUcKHqWFZOeMS-1Ec9pWr2fnRE6WivmSb6sQbOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ مدیریت باشگاه پرسپولیس بعد از عقد قرارداد با ابوالفضل جلالی و پوریا شهر آبادی از آن‌ها خواسته هیچ مصاحب‌ای مبنی بر عقد قرارداد قطعی باسرخپوشان دررسانه‌ها نداشته باشند تا زمان انتشار پوسترشون‌توسط باشگاه؛ بخش رسانه ای هم پوستر رو اماده کرده و بزودی…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25321" target="_blank">📅 01:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25320">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaS78fKcUpW0ld8p6iZ9OJ_XJIWkEY9WhE5GBLgM2cdYl5p_5oQ62cSVqhY8g9S4BgF5m8Cw6EqD8w5vLVpAkCYtIXRvAepzthBDOIxYZiB4ZQOM_Oeb7Lil8FyGTsy-smgwlrjzuPrEZRnTG_D94RDphpgjqDPcHaZ3J1g_cInt12bX45DpqCGlRQEzjniBWHIX8fWk0pkRfaXDP1BCFgu1Zg5mF9lWJg42BJdB9SccdE3MckhtGvk62-SDjbEsb8L_y_H_gjt6tCGc0bOM2ocmEd4spvItIMIffntPgL1c9GjK9tPFqw_orW0jN4z9nwl80JYKLn_uqsAULcGi8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25320" target="_blank">📅 01:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25319">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huB3p0NVYpJUyw6SJqeap-xV_bgyo5xQaZfOSUiEZvDZ4PrWFY3x8sFOq9r-fIzTur3NzXyeh0zw944qdhRcQUFXfEwz6RBcBnovYi1thb7jRw3MEbIn-4134wpVQ4VAQ0JoR9Zrwf903kvaGDnQfCgZMkkm1BDeqsHu0UBBSQlv0BHFxy9gARBcFz_h8iQG5h7nWG6shV_8ysyRMZnYl0QURkwbaGHnnOPC36jrut5c_ks2MkKm-ayJHI3AXdELTNoW_l99_SqV_17dM2WSfDYUY47C9QOApwNYQZHbM46NUeR_yDTYRKqVWaQXIVgCpaX8ccw_Cz9-ta6H1v_C3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ طبق صحبت‌های امروز وکیل ایتالیایی استقلال؛ تا روز 25 تیرماه پنجره‌باز خواهد شد. کانال پرشیانا موظفه اخباری‌که از باشگاه ها دریافت میکنه روپوشش‌بده. بسته یا باز شدن پنجره دست ما نیست بخدا قسم که از ما گلگی میکنید‌ خبر موثقی که به ما میرسه در کانال…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25319" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25318">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2548666d77.mp4?token=vIgw8S8n8MPcq9RF3o_7qc35rTt1K9x7GGoaCpmQtCaETCi1IcUqtGpIEf8dw8pMYMiQcLXYNjgJAhN045gsPn5XXJyKlDtNmL8SXGzyUU1N7o5vo-bJzvTicaANouyw9zpqomwbEtgb7F8DGaWrlvoelSUu4Wty0AsCyK0Nc9FDIuojZqJPF7P1cV3mtOzs-Uq6wVgq2OUf1OsQJ8do1u76BkYhL1-p-q4OCKquea29Y2dy9Pj8O0daNM2NqSHV-eg-5wIhxMPOzm83Oh5uZ1VqNT_jho8eGAcOBM7qBFJDA-X0H_db7SBN0fUuV1Tezehd-PLkiSqDycFht9o0KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2548666d77.mp4?token=vIgw8S8n8MPcq9RF3o_7qc35rTt1K9x7GGoaCpmQtCaETCi1IcUqtGpIEf8dw8pMYMiQcLXYNjgJAhN045gsPn5XXJyKlDtNmL8SXGzyUU1N7o5vo-bJzvTicaANouyw9zpqomwbEtgb7F8DGaWrlvoelSUu4Wty0AsCyK0Nc9FDIuojZqJPF7P1cV3mtOzs-Uq6wVgq2OUf1OsQJ8do1u76BkYhL1-p-q4OCKquea29Y2dy9Pj8O0daNM2NqSHV-eg-5wIhxMPOzm83Oh5uZ1VqNT_jho8eGAcOBM7qBFJDA-X0H_db7SBN0fUuV1Tezehd-PLkiSqDycFht9o0KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
شما حتی خارج از زمین‌بازی‌هم لایق احترام هستی آقای کریس رونالدو؛ شخصیت بینظیر و قلب بزرگی که داری رو هرگز فراموش نخواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25318" target="_blank">📅 01:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25316">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=nUmntet3_f35K6ZK33OV0nChIqDXuX3QLSwZTVGR2X3tb0EysEx9AVlhH0lL-lj5aMcWKMwNWvYGpCqJNHxhxDrZh1n2wCb0Vht8MW6XeBnGC0NK1wuw-nD4ZFIuNBVft4uwJ0VyUlRoUFNlSAJaDPKM_sap6wI8HPpySXApdoBSZ5BfW8aNVyIB2Vr2K8LIB-Y0Yhh02EXqE-tbCIWRIC-zWtkRJkoTp8WbufPr5YN__uyyvpTP-aOi8B4qmLJr4Q_UCOE-s2u9wzhlKI0jFXyN1ngZmKuXzJusI-un6taPYuSHpaJ4Sj_-pfe7NDdu_bmtszB_vHz8RrtxjZb5cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f822cfdb19.mp4?token=nUmntet3_f35K6ZK33OV0nChIqDXuX3QLSwZTVGR2X3tb0EysEx9AVlhH0lL-lj5aMcWKMwNWvYGpCqJNHxhxDrZh1n2wCb0Vht8MW6XeBnGC0NK1wuw-nD4ZFIuNBVft4uwJ0VyUlRoUFNlSAJaDPKM_sap6wI8HPpySXApdoBSZ5BfW8aNVyIB2Vr2K8LIB-Y0Yhh02EXqE-tbCIWRIC-zWtkRJkoTp8WbufPr5YN__uyyvpTP-aOi8B4qmLJr4Q_UCOE-s2u9wzhlKI0jFXyN1ngZmKuXzJusI-un6taPYuSHpaJ4Sj_-pfe7NDdu_bmtszB_vHz8RrtxjZb5cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇫🇷
دیکتاتور جبران کرد؛ سوپرگل دیدنی کیلیان امباپه دربازی‌امشب‌دوتیم‌فرانسه
🆚
مراکش؛ این 20 امین گل امباپه در تاریخ رقابت های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25316" target="_blank">📅 01:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25315">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=S7LVn-nksTAgqTiHsvo5ElJHX3b4PZUqMREclieOBRbC2APHJM3Qgp9o3-wJ_LBRAVMxRIloR3DbDCQi9xvayjpn71r55oeAOE2Q4C74tqE5FbUAWF0Pavf-z5_mQxLam8AVfjJsGNX4ailzGGhhh3soUuUzXiijBQ-rhz1MiIaTxXpxZmCGPsbwllqLeJZgmy3IASSfRkgiJd4Z1N7l0AvzkZxPp_6z1Q13cBe_-0-de_mS5qciv9JFftdTnenL9cxYtL0negciCaUXIphjfZfzE9_5zRULZxVUmk5YIIuAjB0daVDk1K49dGNsFE7pjKPtIyuotQ_GARcOI7n-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c42773d2.mp4?token=S7LVn-nksTAgqTiHsvo5ElJHX3b4PZUqMREclieOBRbC2APHJM3Qgp9o3-wJ_LBRAVMxRIloR3DbDCQi9xvayjpn71r55oeAOE2Q4C74tqE5FbUAWF0Pavf-z5_mQxLam8AVfjJsGNX4ailzGGhhh3soUuUzXiijBQ-rhz1MiIaTxXpxZmCGPsbwllqLeJZgmy3IASSfRkgiJd4Z1N7l0AvzkZxPp_6z1Q13cBe_-0-de_mS5qciv9JFftdTnenL9cxYtL0negciCaUXIphjfZfzE9_5zRULZxVUmk5YIIuAjB0daVDk1K49dGNsFE7pjKPtIyuotQ_GARcOI7n-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25315" target="_blank">📅 00:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25314">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGCI7BrdbG6nLTM5HQZLH6gjAOQhvxZowMsOnknhNUdaPZx4pa9eRLXSwt-CMHS4oDTigWAgYI_llEZWkN0pxfSwCkuMvUTyohDKqvJcKUA9hshONuHvGwIjum6ao46mlnXTBuKFhbN5FFRl5Hsx5iCKLlvTxZf_YCpx4Jlw1UVZN2IEmfrxKuDEif2_zaDy00bne9IJF2gOy3-xarxH0_SL3xrOdh10mNY9FS1Nr7jTjesf-agvH17gw1Mpj0i-dfl2azOg3CHaa8kjZ4iGb3DuX5xfuvDlRrEZlHSFQz5ijtk7J39jDqh6PVoDFcGp6_Z0ow1pewQbxV_TQ-cxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇲🇦
🇫🇷
پنالتی‌از دست‌رفته کیلیان امباپه در بازی امشب مقابل‌مراکش؛ یاسین‌بونو بازهم پنالتی گرفت. ازهشت‌پنالتی‌اخیر که براش زده شده در جام جهانی تنها دوتاش گل شده. شش تاش رو به راحتی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25314" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25312">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAUehUhjq1tve25e9hjpvHgOcM21R7jSDrKzwB8wcIeZ9AlCMbxRni2gnQhH1mlD141RjEufjNck7RK4F9AFOeI9Hb8XGaZ63GL3wLt41mhx4ArqxpaE0RgRbFKTZhqbbFCQUDsU-cnKQqjtRU6dvuRRJPPL4w6ihNjXKOTTMuB2cpfLlhodAjt__ZaKCvU0nGo0bK2oqkn4C8ncj30Oy5I6mG04-fcZS_jivNgwn2MxzxtR3vuzDXcX8rwRu9dD6dzxhTXtBD__kt3p-FSpMXukSLqS87x6lrLkBIXLlXCt7YqtrSJLYGq1Lzhgv7Tf1UxDWUKRSadoQHpT0H2S2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز خان کریمی برای کارشناسی مسابقه امشب مراکش - فرانسه رفته شبکه ماهواره‌ای جم اسپورت؛ خنده‌هاش رو ببینید دهن سرویس چه ذوقی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25312" target="_blank">📅 00:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25311">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=khM8GN8mfDvS-DL2eG_Qct2EPAyIWqjib-urOtPPlpz6WnmImERduCfT0fg7DbKb7QY76plMwx6PkRLh7RGWtxp0d6WGJ3LR1Dt1TwlUtse5qbOn0B2fhEMUprjrj4_-5Dpr1Zj1-B9CDiXs8pF9dCfqtbSLBAi4iONADmC3gVML83-1Tb0SADkmPD0b1_z1rZ9XgpkJD8yF67zBmOYc3R1CgL2l7w8LdlmD-lySXHY6x6FjGEZi_qXOjSdLM4ldqn8MKO2iaxQgjEgYqA592GdjhqzcZEDRmoBD_tAYjdyCEHDa77KVZpYuCSIQFl6qvJABck9A5WLW5i25STmm8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7769fa4e86.mp4?token=khM8GN8mfDvS-DL2eG_Qct2EPAyIWqjib-urOtPPlpz6WnmImERduCfT0fg7DbKb7QY76plMwx6PkRLh7RGWtxp0d6WGJ3LR1Dt1TwlUtse5qbOn0B2fhEMUprjrj4_-5Dpr1Zj1-B9CDiXs8pF9dCfqtbSLBAi4iONADmC3gVML83-1Tb0SADkmPD0b1_z1rZ9XgpkJD8yF67zBmOYc3R1CgL2l7w8LdlmD-lySXHY6x6FjGEZi_qXOjSdLM4ldqn8MKO2iaxQgjEgYqA592GdjhqzcZEDRmoBD_tAYjdyCEHDa77KVZpYuCSIQFl6qvJABck9A5WLW5i25STmm8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم نهایی‌جام‌جهانی 2026؛ شماتیک ترکیب دو تیم فرانسه - مراکش؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25311" target="_blank">📅 00:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25310">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3y_QToI1iQpV7o5KQrv5uPD0OO9wF-ldgW24PEpL1JDICXu6lTDIV8Xx89jfJa1ACrEA9vqHofpsbOAPEE3a3oCJ7rwI-39n3DP36QG337PzxC-xfoGgGlqArX9MbadN1pYsAV4COOkul8DR1RAuRyW3Ibw7zm64kxYwjnFnDM2w7uz7OeeKHTEUlFWsEI-rqmpnUFv-xF_f_Q94JDm7XaH3x_-I1y_5suPkaDNB_1fKm9YvYscdKBY2liT7acQkwRN_Y9tEAnBjWKhZrcQqNchaYwguNRlf1H0A9AcQJUsWfL4ArYJotkxSORW9RZ9BoPq3_H1cwqJf7ot_IJDtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌مقدماتی جام جهانی در آسیا. علی دایی با 35 گل زده در صدر و سردار آزمون با 29 گل و کریم باقری با 28 گل در رتبه دوم و سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25310" target="_blank">📅 23:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25309">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXWwfb2EUOBdYdva2JqcZrMmM6WyRdoUENmxQZKyUoQ1UWct2JjYJLZz9XPSdkkiUeYBDv3E2v7V3BnD2enkEd8PpaKCEm748wvzarX2JFJcsy6FRlvgf-2_hoEs3FijZ3qTiqZdkBzZlC87FLxDSw1LQcvhRFgmhtIj4S1BA1Zefv20kOrq3laPtmwqcm9W1ufjqWbxPBywsnb-HgNhZcCQ_oPsnAmgSASMuWEATJ6XI6_McYX_I4VP6T1SFMoK0WY91RF_i0NxlLby-9vufGbyixXpcK9x6DHhlKRGBygI2lcrnrD5kBNmyy13HSNcnvIYcds4oL9NDJX3LCngvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌ترانسفر مارکت؛ باشگاه پرسپولیس برای جذب پوریاشهرآبادی20ساله؛ سهیل صحرایی مدافع راست جوان‌خود + 500هزار دلار حدود 90 میلیارد تومان به باشگاه گل‌گهر سیرجان داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25309" target="_blank">📅 23:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25308">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUayqKKUXqNqFoAGhsen_2r8k2ZunMP_RmAqAgtW6OQBGUctElwqn-06pRFbuVavNPx1LrDj_svlFi_DuYoEkcPyC87HQnS9GiYabR94Qd1zGclT_q44HEQ84l8Ulp0aRVSjngxUXByLfBDHBIiL4_tG-svyfxEzaUHJZzY_QNfc53RRzOTZyTAcIT-_XB8-Cesj_EsaUi2FNC1gYphkwH50fwACdTkty0NioQAU18tDD6Yx6HdmYRZJVTBCv7sEvH4pyIcSCUwywBBzVn-N5ZOvWrg-ejuIXEf0_dg__Wg_lxVCYkwEA16DKCbz4gQa4W4gOZr94SE-bE3OaTHwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛ میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25308" target="_blank">📅 23:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25307">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UJphovuy3jdx4yLiu1bGqjFCnoHethNkzTJ4badh8FC0hWdHTNNQL7-tdH7nMhFXh3GuJaGZ0KDLLvK8lu_P3LRdLS5zPF3brOUUU48bySnBXYSw0JdyUKDufAO8RrumI2W-Yh2N-ReZOdPPCSXLTRLQ2DuMmU08S03WT3a8vdpHA1Hwq8jwL_Cf-wJ4SWsILGctxdhXMkjG_65xfZMKxnJD1uCTuOrXlGcHD07p1bLT7ZTP1m1-v6yaJKCFPJ0lcj40ZE8s8ZL6tjSlLAtbMdQhzmGrZxQfZxmcuWDUov_Kxf_Ubu-ryiWfqJF7-AIRhjSoJpX00ghtojCF1WjY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25307" target="_blank">📅 22:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25306">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S57WZ5Vsjort-6ZoBCXjcxabWdr-_0qf_HwtCpwh8-iBNMSi_zT2nU_Wy8zePsxQ0bJxPzww4OIW69W06LIeD309XDbwmpCUIe8DfJ_Ce--rim_vGzvZitqPJlrrnpJu2iAHG4tI-rxaYGQhPiyZDzj5NsyKNCzKtWYiofM4bt9vUIqry_kSz--c-wXufodM0j3U2pWDiwbiAkIz3QgSb6E7_F4x3FDjQelFaZVMttvMdaPFtZJVU3SUHMyndq2TkFZ09rNfXVoZUuvAky3Iq76JUzA2eB_6wYXMMinLDR9C0Lq6agww2_PULK3FYnhdcweNTZLsGt74EUbONJq9kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25306" target="_blank">📅 22:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25304">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LJQ30Ztfo8ScaYh9sIRo-eolB9MFoihiKeS5NA_r4s2ighDWbfhxGlYMSygh-CeSrG9QnYriJhJU5-1Bm9OxkQ5kxY0-7TzpQnP1XVvbqggKSxm03GM4QCXSH1TQPzPFRQE6dfB8PuEsse7_3JICVXqZunPh8Iy2cWPcdQS9_M-r3pke5PfhPX1OAW52jGVNj1ZCXUyKRqKAe9RmGmeGvRe_2Gw9z2pDpECjFYojqavcT2VkRpqc_rHt08T1Ovw4VscGOsl3auwJ8SuG-PguXG1ImgJQtEocQxffb6OOCZl23tbeDrN-DwYPBARntqvFceW3x84SrP7rCyoYcBHNUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FBVzvU6GeLd_lSe7f82Wd9bBdyqFCqKBU5QOxrG0_ooyPB9BMIPjsD9AKXEWIdXTqpAaHvaCxi11XY_9YpkwGtu88_lmE1L3dwwBuFlhT9xpee-fAIvjT63p4ZY_44OblcdBuVcCuyZf8L5fn36HoLZNv__BdXJffbXi6MnzNJ48y-u7TlOTVsIiucd_tvZbV9ysYw9q51bBGGyeVFC9-lDsSHSygwsGqsygLpS3PL1KIgR58yTHbYWZ-UojSSa4olF8OVJR6pZVZsKfQ70GL7qupbjx0yDZEP36L6L2LJK0ZaORjoedUsfnK4jPbDiTDPReyWwu9qHOcf7KpgxBJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ازترکیب دوتیم‌فرانسه-مراکش در جام جهانی 2022 فقط 9 بازیکن همچنان در این دو تیم باقی‌موندن. بقیه‌خداحافظی‌کرده‌اند از بازیهای ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/25304" target="_blank">📅 22:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25303">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNjZX80BP80BK3PAd5WcV_9nMR7Uhqy790EjHhjWd1aZC826Bd83xnUYclsRp8t5Ygka84l-fSs3DamPpCxDygsWBxbXjJbJKxNgR1r3fPMKEh0Oi--DI5mWsL-yX94tQKntC8QKJhu2Y-wVd6n-5sXNc3Vvzk8_SxY8zWDlByh111esTnoIUI-oqconNblgqzi1C20ZtL8FXK0lI6uArnzUro8AYRO8SvZYYmAn8rsD-5LyoMgcPK0Cocsk99QVxBQSDt3RJqJDtwo_trMUCbTh62yque8Ov87vixLd1husurgLh9EgfZUJVrpw3WlK2TiMIEI0Ni7MnXVboJAV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی‌پرشیانا؛ جلسه مدیر عامل پرسپولیس با مهدی ترابی در منزل این بازیکن برگزار شد و دقایقی‌قبل به اتمام رسید. مهدی ترابی برای عقد قرار داد 2+1 ساله با باشگاه پرسپولیس به توافق کامل رسید و به پیمان حدادی اعلام کرده درصورتیکه تا هفته آینده مشکل…</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/persiana_Soccer/25303" target="_blank">📅 22:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25302">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hlBfqN8qK1aR7IGK0pYeEVqSVi6lXe61VcAmzf2AvyKUgFM5SaSV9Xp-o_9UfVf1AbuX7CWHDOdVIdEhsEWuMXKKDCE4NWBwq7oyFtCBHtEg5Jh61sC9W7KFUwz2FDQs9p6i8wYYQHvfjVUCS-nvVYX5MwhhPUB9CQOTi99UXJX9ng2EGj23npBx92d72Z5XBjjy08Nj0SGrI-iBwJlwSmo-4-EC9P7e-dZX4fZg6idBSVKFg_rA6Y5blTRFa1qzZ4a7uJyiLZ9TxyZ1tDeAoiA4aj06mStRZt8tR7YaJtLNd7ugF-9ivUyO2xDTzPFRvumsUiRmsULyn-YtWOyA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌مدیران باشگاه پرسپولیس با مهدی ترابی و نماینده اش شروع شده است. تا ساعات آینده تکلیف ترابی با مدیران باشگاه پرسپولیس مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/persiana_Soccer/25302" target="_blank">📅 22:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25301">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iI7vNDPP19eqActHwO5hBYoVwglIRXaFYWGsNpYtaWGIFwGdC0CQoRprdvUIj3WZXeBgHH2YqYlW4423RgH54AX9twjyKkMl-eSaCsmhqRPh3WvbNOnZ8oKVXDHzcBFUhp6Pi_k15DlmYuyqSXZ83bwH2-3KZ4pLvqp1fhUcnXaeywuFozVjXZfR9EEirTiEbgC6iDvQc-SUlhG58LNW4diHtIQ6iI-HwFPGUsYnrahUqDPkPuw8UgY3ImVqyAAZpim43v2kIbymdGRoKEbTHVmCADTlZHpeq3n_zYxmrAJKbhREZ70XztR1-JDbm4JwJVQWywp0F_gh4dQkB3Oc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دیدارامشب‌ دوتیم‌‌ ملی‌ مراکش
🆚
فرانسه در ¼ نهایی جام جهانی رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/persiana_Soccer/25301" target="_blank">📅 22:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25300">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSAoNYB1h_BslB_sZXm8NVtD1VT29jOxu8-6kL-Uk9ltbn1K3Hjhqx1xGXA0Py5oYOMYHJbtNhIbfFIsXLmYr80LmYnYNZxO2QMcjb68zaG88paBjurSCnUgeZJG5e5eTi20jss8jZe8_4aihL_XnhONAIme4YS3eeNvuYvresR_p2OwLNMOm88-DczgiikGCKFAmSeBUWQH_iekQ-VEeYBmOEmSWxiGEep2Zi6h6WMNjZRgETBG0_ROrdipDGkeI_vgy5UyYSgs-c4rtG9oPPisRohaUSiQVF7s9hTxBJce11iYZofpGjZAjMRwIgfCfk3PPBil3GRJgjPgrQhr-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ…</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25300" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25299">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHiwSMWZAKGeuDmNnUoCByr5hilQogiuk_5aN8_Q_voWduSlrbBWppaM1EQQyLSY2Fn1zG_td58RUa_oiTOqlRLDp5I0ZxacEBzA6snyGMM2wMojonXH8pXRFc3TXeSdpoL4vvxG4DJvcZSmDnrlO4uWRsDMXStsaIkOFX0AM2SErJa1Vk33yu--SOhWMsFSMnWdeV_LeJJoaEzflQj6y8L8ePR-JYvWFuLu4AdElyRDXcMUiMzMv8dtAI1Ih5Jl2PGIfByWYOAAcf_h_6Jy17OrZXBf1Nq3a8S6yuPZiHQbbvAaL3uYj739pTig5EM70LzoV0oOZkJmpf8az8T48w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25299" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25298">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClPIx8Pwfiro9j_eEPIHZR-_ohCjnyXZ2GJGU-LYX8gJWX1euoJvpJ1kv-LFzmAvw7F_yWTdx1BEJopefqXPFCmkRi43pRHmrMSevR_kL4-0ygVmIHNxYUq_dcwKOZwQ-7vRKHtdxp_BnZQA3vtWRQy_9BMMtH8I0KaDXhb5KkW6lAtNBMEL3u9D2wAA6MKoGzZL8XsqoxDKDAXz31Bx8RpkuBBz4rX_970UhKsQwoS_ELWIOqQiaXXq8Y1SRMRsi1WEMVDjaN1QVt1kM3PsH5zAhT6jtKr18_ZQVIeZR8oEGgZJiPZhzTia_25rcetxQt6r8OkfToP_CDAtTSAHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
مراکش
🆚
🇫🇷
فرانسه
فکر می‌کنی کدوم تیم برنده می‌شه؟
👀
🎁
۵۰۰ دلار جایزه
بین تمام افرادی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، طبق قوانین سایت تقسیم می‌شود.
👇
همین حالا پیش‌بینی‌ات را ثبت کن:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/25298" target="_blank">📅 21:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25297">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qh-pg18dumo4pJXEVXRXtH85v0VBDxTrA0pn-kxUkb8DHNRGGRcHPXRRL9VTCxBgp8JdwpG5Y5xyIpZin0YESTm0EvJ95q9ZfnYqgw3dA3f40IB4XlJGiOFLt9XV4gD0wuLYEDKWDgIN41EaEaa-0t_S_fP13iyX8sMLnznlmjJpAAjBCYU1kEG-Ky9oSN6LA1gRhs-5ndyIKYa0BNCnFq9OijLRZUpkmRM_RXOdOiH-07tR29_Q8KgNQ-Tje96ii_iRmSkb9bC3g_bTe7YFbLYjrxdebryj2K8t23Tr8PZo2HKyEGP-WSdGjCfBA-_RNtd1orVV6uvrhrWvycQjQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25297" target="_blank">📅 21:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25296">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ov7AwrD7IT21y1H3Nd-bqKaNiMrppep0vx8Sxql7EJzxkQ38S7Kha2p8uNkoxWu66Btd3qqijY2q5VOpCkHeCx3nhfr856dY29uOWaF44wmm0lXnntxcQfMxM5z7dgE-YTQhgWrmsAydobEhL80YEpKiqUcUOXt9zqpHHYoDOyfCz-HD0AqEGWNI8E-rFeazP5MqFJhh0F1AgnMbUICdrqUJuybLWtW5j_gYW0sApiUHG4o1Uh_Do4K-C_31C0sb8q2X1T1S-_k_YgGmT7ggQUYbmEw6KJQfbOt2aFqTeezVRghnqiYmNq0FOQtZbkyxYE2uzix7WT864PjbZbDmUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بنیامین تانیاهو
: راستش‌روکه بخواین لیونل مسی 39 سالشه و اون قبلاً هر چیزی که میخواست توی فوتبال به دست بیاره رو به دست آورده و بارها شجاعت و بزرگی‌خودش‌رو ثابت کرده. ولی واضحه که هنوز حرف‌های زیادی برای گفتن داره. من در جام جهانی طرفدار آرژانتین هستم؛ حالا از فردا بازی های آرژانتین از صداوسیما پخش نشد تعجب نکنید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25296" target="_blank">📅 20:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25295">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHEYaDfih03ZCrAzqEhC-73KTkP3VyYN8kCeiCFn6_nujdxwYYrNgjk8rUlg3JzqBh4eiNRKbywbFE3UoTWwd_ZzdVZ8uTj0bXbdJDfSafxoZEHLXs-wu_5uq5CAxVcth84TT6mGqyaio6Oamxw1LTicE9vwQESuFFANm1DE3u9CRP5kj6bqra3AfglXtFlsxUEvQiptzO4TwvznNZuODteDtsAaSLYwXJJcx1-MJZwQEPs5ZwHZMXxT8qYp35FSPNO-I1X88vWy8fM8Ww_KpOvVnIdaRk2xMwgJOcS8VQvxXSNnrT3AbcB26kwsCcc7vAmrG72o7B7wXxHn5rciQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25295" target="_blank">📅 20:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25294">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmtHQuc1aMeXOBpXnzTl9hRod9tGkG23e89-JngL41BdFg52cg3qNN8X6F7kArPkW0ysboPxDAIlK5dIyGwUEO18Z_j3NJFwSMbdlREFs7uZsYQLLZGS_GzQ-4-3ZKD-s08gqAZoPZgL59FLpdKmQgWnMj8TwZjPytKpAEWTDVB9FcKChr1uPgsMgicbvsqFTZyOiOQ6moY8jRfUkmf4o1eGomgf1NaSZVgr7uYFQHXFtAt1XDcFZpD7bYNpMwtzfa1y8bKACtsF4r4Lm7JZSh_9JHCUC5maIRngigDmSKU27Dbq_S-O5sShmloYZPgn2B-LpiYAZueBTxJfEy6sFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ طبق اخبار دریافتی پرشیانا؛فرداشب‌حوالی‌ساعت 21:00 مدیر عامل باشگاه پرسپولیس در منزل مهدی ترابی جلسه مهم و سرنوشت‌سازی خواهد داشت و احتمال اینکه قرارداد 2+1 ساله امضا شود بسیار زیاد است.
‼️
پ.ن: دیگه داریم لحظه تمام اخبار داغ نقل…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25294" target="_blank">📅 20:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25293">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnAyPLFEdZhUcy6_1xYRDirXERrYZUe1TBH33jq7vl8H9PPrOMD1WKo2BUbD1pGtiqtvL3fRZdL9MEt6f5OMzfB3kQWbl_xaEPIsQGPPoJClh1O7JbR-kanbJ72cSFaURaEJ9ZH47mfNayzdhBbYq3pW8cbjIzae47qlwCkDT45B_NOeUohu0uaOHyBxgkAlfgW_C4MAnumIS8HwugYtW0j2Q7D68MPE9DHZyik2Mgw5U2d6QvIWH2kOWknhjXJyeyENAIzmoWQGAj5RtXDNnz6Ts3RgDxhUQ9MQEBrWo-z6ETaShxikH2HZMheFk8MV4QgaQf5cE2ic4xWvgtjXrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
امید ابراهیمی هافبک 39 ساله سابق استقلال با عقد قراردادی یک ساله به تیم لوسیل قطر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25293" target="_blank">📅 20:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25292">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft8RcIoAIUQ8ypsKXV8V1A9D_tRgkkdDAiz_wfWck8hhRLf-_88I6Y4C8aqs-z2xSNpzbnw7ycTvWFHGwKNy2wAH6hqzP135oyI5jvJZqi1tWKWQL7celY5EbSm4hHk_9BY81cRfiI_waly2d8xGSU_TH5sL0C2OnBhkpxkMEPuGGgg1WF1VkC3fnpK4T4IMaEfMitp0dGmCwpDfRtD5af27dcUNdTZ2jJTm0i35gVl8KEg-hiJqnRnqEk4mRBiI-DMr5d24TC12eanvXv9tflti6AbDM6PsUJfXJA26Sy1ruE_oaVjhYwEjygZ9AP0RYIVfyWXWXdQk7ZqmXssIFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هادی حبیبی نژاد قبل از اومدن تارتار مذاکرات مثبتی باسران‌پرسپولیس‌داشت امابعد اومدن تارتار و درخواست جذب مهدی‌ترابی دیگر قید این بازیکن رو زدند و او با قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25292" target="_blank">📅 19:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25291">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTj27Tc6M4TOI8PE_gGPjHT0Rm3AjLGf7GjqsE63mODMYAunFJEO216RfEEy5repx67pTu7eoRz6A1UB4rGpSsUOgBteibjkXb7w6pX5w6oUaIfhmtUeYhZ-iiQPqtxLPqdTuUjTi9PZAiw0IqlPXsxDDNsj37Ar5RUzRTqsoMVNRPX-djbH0Nkzecm_x4qlZ2Mtmzb2wnyugIBZSNMMA2c-OKRqtUCHNoBXV7CmuQl7zQwgm1FQsikbt2yV_n8kfM1xyUjLwAlSFrgfF-0W3M0G5SLsDOQXWeoQNAY3avtcP2nYrSIeLFByuD3xffqa5YhDcmjiuhF7iwuOcpUWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرورزشی باشگاه‌الوحده به محمد قربانی گفته هرباشگاه ایرانی دو میلیون دلار پرداخت کنه رضایت نامه ات رو براشون صادر میکنیم. همانطور که دیروز گفتیم باشگاه پرسپولیس گفته ما تا 1.5 میلیون دلار حاضریم بابت رضایت نامه پرداخت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25291" target="_blank">📅 19:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25290">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmXlDlwb2SHvPGxOJBCrNdn8HvqGTUM9MPg64VvVFuMm_F-z9Jb523Iru6dVAvN-k45Mqv0FKDqmh2sSCZsvxCGAg8FhLnhjhO36_7h1r4loZuS2gdJuVSIrnd1oqZ4QJU5wyNci2pKOXzbmqcPqrz6nHQQeMw1zcgPHiaS3ZlpzKsJnt2tT6kI9Ioliw29QPNwxgbzXStNoeBl-dvf2Z956bDUJWShxYVHyfW7x3fXtp6wa0SvGIyhcrAByge1qWUGIw7Sa4psCYlfmzs-una9M4k8cW5enX7FTDTPiGCLF83OiMAlCa-TpC1fZy0JY4GtWOWZQCGxk4YZAxXRKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
تونی‌کروس اسطوره باشگاه رئال مادرید:
مردم همیشه دنبال‌بهانه‌اند. تکلیف‌فوتبال‌در ۹۰ دقیقه تعیین می‌شود، نه یک‌لحظه. مصر نیمه‌اول عالی بود اما بعد از اینکه ۲-۰ پیش‌افتاد کنترل‌را از دست‌داد و آرژانتین استفاده کرد. این تخصص تیم‌های نخبه است.
🔵
مردم مدام درمورد داور و VAR صحبت می‌کنند، اما دلیل‌بازگشت‌آرژانتینی‌ها کیفیت و ذهنیت‌شان بود. مصر نتوانست‌سطحی‌که ابتدا نشان داده بود را حفظ کند. اینکه مسابقه "دزدیده شده" یا به آرژانتین هدیه داده شده تئوری‌ توطئه است.
🔵
بخش‌سخت‌فوتبال پس از باخت، پذیرفتن اینه که حریف بهتربوده. آرژانتین‌شایسته تقدیره. مصر باید به عملکردش افتخارکند اما از اشتباهاتی که برایش گران تمام شد، درس بگیرد. فوتبال همین است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25290" target="_blank">📅 18:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25289">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWxRCJIB8WdZqIl0fsp5ZFv0Kckxhw-5hiJA635HQPNmqlpDabT--inaZssS80zWnekiIjVkzas-aIMGpAP2DRXGLxeqhBuqOwB4DUTSuI65pHx95AwG2Mxy6GMsJpFP2icFYRo36RVm0zgxSxLedqZwJDmvW7Wu_cJEoCNKgqTXkvZyYqZEP0IBz2GaHpmj5c-XHKQAqjFeEq4K_3bZiw3dHTyMDeO5Y7YCgFc6bNXH-nXqeqU4Z0Eyam81CKXFJ3KcvwjEwiEk9d8qhnfNmpMq8oBt67lv1NqgyVBFBptL7lnxW7Gyk93KlGd-JuuRMIpYfqmofOX2-FXEp4iyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25289" target="_blank">📅 18:40 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25288">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4GznwzkaHcB77A0H9yOrHWrfoe2VJjzdasgCtxScJ4tFBWuLrtEwZlc9XwVofawntv8Z050SA_CbZPwae0MBgPpJ7eXnI-Xzp21kAf3O3rC_LfWVWxLcSIrHH5XqyTpWQiAT1TUdBX7XoK0u2nkA5dHsMUGeDJbrn3yCwKcFFf0-B1RxMO9EtW6aSstgrQcmz52YTvgr8wIXECD7rRlHf1f6n8wBvk475UzqgMup08-0ZL3-XNftQrqAg40Ca0bVpKiUdj6ijbLscOlYhMoVpIBVFQavacGmKIPLtjiSkA3MStEjhUosSwhBlefo_qCH4J-Dbvmw9b8s8_65MeANA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تقویم
؛ بیست سال پیش همچین روزی ایتالیا با غلبه بر فرانسه در ضربات پنالتی قهرمان جهان شد. با این حال، این مسابقه همیشه به خاطر اشتباه فاحش زیدان و ضربه‌ سرش‌به‌ماتراتزی تو یادها باقی مونده.
‼️
زیدان: از همهٔ کودکانی که اون صحنه رو دیدند عذرخواهی میکنم. هیچ توجیهی برای اون کار ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25288" target="_blank">📅 18:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25287">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvW2BJfAeGCll-8SwLlOD0CPm84-rCbuMbFF1KgDG4P99UfvrAkE16Up4_FAA3SIx7nEVDQxtwb8h-XORyqK4xfkRokFPWWP-XUtESGab9vrqpv768wgsTp2WxKODsGSmlrHFchR_Fmhx9YgaKLdJqUtzArhceGgPPKkrf2O2uuVIxlXXIxOg3gXG7QpC2SMWG-0fbLgA5puoajgt8bXSf5PQPCpo2h_mpq7Y-x-Hy5x0g-HJXeYeBsg35H9ZDZdB-FF4fbkUKzgLDeL90cvExgPFoRfFsJ0wjWrQ0mllp-XMn_qt9FMtV57lY9qdFNEuCRen-rQxV3WKRJHsTdCLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ طبق‌شنیده‌های پرشیانا؛ مدیریت باشگاه سپاهان درتماس بامدبربرنامه های علی نعمتی خواستار جذب این‌مدافع ملی پوش شده و به نعمتی اعلام‌کرده‌حاضره‌برای دوفصل‌حضور دراین تیم رقم مدنظرش که 150میلیاردتومانه روبه‌او پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25287" target="_blank">📅 17:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25286">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bohXr7TH5tJDe0TerOt_Oms5A5OVgDTu5PUvIB7cZpaIjj-aqwu6sLXCNC6jYsqiP87iqtyb3fncGXG21dlhI5KaOSKQtr0whpWpCIe0p5T1F2cYGahEQys0cjw1RiI7YL8d3Z0rLfNI8mYMhzleI5qMTJfyVrxaD0GKjmjGOXLX8vLlRGu0Y8amfWGb46m70vrR_TeypKflC6hs-q_JMCOA1jS1TV3BO4kT1_jdET6ksLjPkeARYaWykfymI3Gny_MWhvfQGyk5vRrONFELr3T4wuBxSBmIbGGsUXVW-sTs9n_62OtkrmlBy-0e2hnHnl-UYt1f1lRdkY10-IefGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
درخصوص اوستون اورونوف هم پنج روز پیش خبردادیم که چندپیشنهاد از جمله پیشنهاد الشمال رو‌ی‌میز مدیریت‌سرخ‌ها قرار داره و با توجه به‌ چراغ سبز مهدی تارتار برای فروش ستاره ازبکی درصورت پیشنهاد مالی مناسب؛ احتمال جدایی اوستون اورونوف از جمع سرخ ها وجود داره.…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25286" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25285">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCIDephzplhhBCO-9mMg7RE96uTzVkGsm5ZT-ABPP9NtGv4VGj9P0ca2ffhsAQ2cBeXBzCMe4UNglqoIk3F-RuD6_wVXNvjlaaA_G3iXQlK3IiuLQgcGDyLarQwIYUBptMae_DY8Ru32ZU8SjOdHHdVl2cskY7oWMMDrEZ-guzPScnnP2bZDSpO2mWnNqKpa6EySl8LbMMC16BHr5PheeyL0pkn7YRFILmlfzYdDZiFfQmxBWGCKUp4lw-Vos0wMaEky3UzdFQxh78agp7Sfko4DAeXJGravsNHaxk4mFfmUcQeqww5VIDe9HukOxbe3ynY_o8sJ-FdN1G914TbYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه خرس غذا می خوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25285" target="_blank">📅 17:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25283">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU9pzPxvpMkbr0QtUNi0Xjmy2N3W2JvKPM_tGHa0AehnLcOELiXpkoKf0e9CLHKQQXFtFJASpoozPnUMeXcbVj1OPQoMkYVyE5sco55ck3yout1RFpbVRNm5Px4H3t1GUWdRR0NsCieesnlr5LZoDQxKWBp-NIvwwIdUo_XnDa_ZKRpvLRCveexo4jrcShSWxRw59b8VjtzOH7uqhAf45QJ1cnaAOUSbQxopEm261SFOq9Vb0wUKnzeZ7vFmkjJb8BfFIz8gDCvilZ2BJv0l5Pux5zdgwmapOGmf81UD06JPU3jHPiUVsjvY5tzOtkk4RskPBhuwL072y_j8L8i1_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25283" target="_blank">📅 17:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25282">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvcoikZKBBgh8-byd7hWSr7Y3ncG2G3TwF-c1W2oltiqBtqi_sCFlD2-Ppj07nDyqRnXOqhJnZI7IKy8-RD-CEj0KxrSDtkkY0_XE94Lh5gZySo-RNBfb_8VGS_5GVVPPBnFTb4390G5YhnzoZbyrJIcZvqmxdT3h_UCwlQs1038js6AH8PelRzxQSr8ZrMnckJhIOSCYh7yNt-T2mOXyUnE9dsvT4s47HEMIJg_quzNh5JA7-23bkqUQc58ax5Xj2TCTntJcnLGrYvVxqq5WtxCMYDcFag_yLfwqsik8aiIU8ksAqFytj_iUysaCX3APQyQtBQr4OjK8pdxGnaHwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی دو روز پیش پرشیانا
🔴
پوریا شهرآبادی مهاجم جوان گل‌گهر با عقد قرار دادی چهار ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25282" target="_blank">📅 16:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25281">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm6h-0TwcaP1Kta2UarBiIlilpL8JqhvyAejuIg7L2k9jKZSHhIqmtekTnpHQc7CLWh2_gZ8BLtQ5Ad3dVrO-n4vPd8vx2wjXZYuGgtUowQR2J4HkdjIHH_mo4mQxCtpPSAihcKBL_p9vXGZnW8S6kDr3180Anx4eA4iB8HwDswk8aQS5AODd773c84saUZ2pKvOaaazcedJcG7n5MBLtnpYYfu42WRd_wlMPCbAp0PS76sV_C7w7-l1B7X8Fkx-s9vxeYVQ1MH-wnwRoa2RiB_Cky04_HgK4GunMQFVshzFYjVBhHKaR7ToMMWkwwh2Rg7l-nf3nq0xAgyUHvBLBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ پیرو خبر روز گذشته پرشیانا؛ پوریا شهرآبادی مهاجم 20 ساله تیم گل گهر سیرجان دقایقی‌قبل درتماس با مهدی تارتار اعلام کرده که قید حضور در تیم استقلال رو زده و اماده عقد قرارداد با باشگاه پرسپولیسه. بدین ترتیب شهر آبادی ظرف 48 ساعت آینده با حضور درساختمان‌باشگاه…</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25281" target="_blank">📅 16:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25280">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
رونمایی‌از تاکتیک‌اصلی تیم قلعه نویی در رقابت های جام جهانی 2026 که سه مساوی بدست آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25280" target="_blank">📅 16:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25279">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr6br53CZyfUHQRso5qeV52vQG9ijRYZeXcfwlVgxHlMq-ckGgsrDMYUvGPUO509x3KGPlYPe0HWynDREivhufMoVUmwf5NH9UOPpQ1cWusQuzpKFTIYPHD0wMv34vXQEH87I_Q8HitM6WCiErVJMhZN46AmrL468lvnxtND48Asryg2rxpvjVP246WNlQpqQg93y18Atv4s8eOZglLykGAy0yZiV7_C6S_15LYC8K6-0LYhU0r9fpOkXMixJB_EkzZdKYc6q-TLGtA3wjOA276MaveBs7RDkMZLcFwMVahSdse0VU9CTgnAlYNxF78QZKR9gNkPx5aBeYxkz0WBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25279" target="_blank">📅 15:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25278">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQbhKWlHpNf-cr7PF_DGZHlqZjEZtih0K4AesVjmUjCBfu9Vjekf5srVFTrC-wRV0xYOje-cse_LxaKJu81UoEGh343c64jHqZhtnp73tOjQ7HsWsLkgUtrvIp1Vwfp3i2peT9m4j3Gsl8n-WeaVrCA5vYJWT50yx3wLmu0aL7C_CWOR5O1tDHMCI9iKVuGuYVXMu_CTgTelU2aYDeqCI84EbfgLiPL9zXVb4TSWg_sVj6rT03f-7mllbtj9w4s1QJtszfZXBZ5Vz56PYoLe5f8kkpgsGbQIufRqqzO08p1d46LpxR_KuB5PujjBaWpef5DS1J_KYBdm4GnAJCQPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛مدیریت‌باشگاه‌استقلال میخواد بعد از تمدیدقرارداد یاسر آسانی قرارداد رستم آشورماتف مدافع 28 ساله خود را نیز تا سال 2029 تمدید کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25278" target="_blank">📅 15:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25277">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrn-vpZYtk0IVAxOErA890YTg2MTmrqudLDpqL4Qoi2piGf46w7t38eG17fcLG8jxikqmYLT0Osuh6T9vkDyT2ntPnTgIdtr7HkkWparvmpybmmAapnwdcsdlGuZmoyGmiYCUOZ6TI4gbIiPAfOHlV7dIprM6kP4IqsRMQEQ5T19hH3wRCjXlrUQ1qBBRWOQryGeLRe1Rpf7RHO6-QF9pyO1VF0zLZzRk5K-QkgkqLXBIR7EVR8Fyq-yGmg9HU_GMaqj3QfV_LXsnh4V6pZUJcASM3wovtu0ycMNIgYbmuDtd4tppXVbfNAJdaTAkBnElzC3Fzky2-Qtv91Hl883bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
#تکمیلی؛ کریم آدیمی ستاره23ساله بورسیا دورتموند برای عقدقرارداد پنج‌ساله با سران بارسا به توافق نهایی رسیده و تنها توافق با مدیران دورتموند باقی مونده که باتوجه به علاقه آدیمی برای پیوستن به بارسا بزودی بند فسخ او رو فعال خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25277" target="_blank">📅 15:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25276">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTBKTB18rzOgg9euCKdbTMjHoE5xCCNaEQpL_OUUI5oqyLhwnAUUXEm38yAaXj2rZtuGsjJbNYR6RmauDlFdkioE36gQF1w4LJXbfnZWplRVbgDwvtIvaCcpYoDhdRW9u6fPwXd4lHEFKtS-WRnDJrPTge1Jgw-bAfxPbRD88ECVn7nJpyoM3e96murDcUgdWI13SplsB6PlmlTiacCa0ZJuUnYRt1_h5Ziyg7N2QBNKxkEAr0KzYfXq1m4qXuz3YaMWDQTeW7MQgBN-Zgo5pyB1OW694DLUoZlhT9WIMnPUzKozPT4tJnwhQgXi3A7aHWSrRGKuDMdPfV_-Efnc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌رومانو؛ ژابی آلونسو باعقد قراردادی پنج ساله بعنوان سرمربی جدید چلسی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25276" target="_blank">📅 15:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25275">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k17hi2NMFg0_2mqP_p3LrhAr_JlI68eMTNARtraXLJ1dI9ReQOfneXu_Xt1rxnufFSzsl0mUgXD6kQN_uhwX41ju28SuXtNhN3TOYe-BwUjbEoGiuyM2XGnd3lQ_alQpF7odgfOC1GVvF27hRjZBle85MXzA3IYmRnP87-oq-oD7_O4wF1EUzOjpdTEOh1P_FEpeb1FPPdj9VbvIsVDjcIy5Nwrt6G0qUYjZq2jeKRjhBF77meiW8ysbv1Xp1wV707XRDMhsQSrqgeiaKwkBaacw939wmSo8n1VBzI5nZEZwhAhiYn5y8JZKbcjLeTNAqBOGSbf3SRMqpfOhWPPYUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#تکمیلی؛ ایگور سرگیف مهاجم ازبکستانی تیم پرسپولیس‌نیز درگفتگوبارسانه‌های ازبکستانی اعلام کرد که به قراردادش با سرخ‌ها پایبند خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25275" target="_blank">📅 15:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25274">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igdc6x7mxx5LH08gK6ARBMDSB_Ty7hWJ2KnUCz3XfUxwYCsnN1NxXjkF3iSICbHGHzDMp4e5j1qf9f9ce9JJBSgCnkCgwbt-LRiaznvJ14mekI47RsVp2k_1h5xJhu1eTQYT4km_KwVyFshYkP_bM_j7cbFyqyXQH48UQnujBLdGHsU8uYnX6QthKbA4E-hSAVJOTevMgu1C_4AynH1NiieMVa30E1NCh-oZ0fLD-9Swv1L6LQaC-HJVFyqsqtNGpzToBZc_k_K-ZVk4cFmNkMp7dkYspnaHekwx4AaUa0pEpXlyWUoIj-OAT_r01dL4d8_RZ72uglkytc5RLy0NXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آمار فینیشینگ و ایجاد موقعیت بازیکنان جام جهانی؛
همه چیز خوبه تا زمانی که گوشه راست بالا رونگاه‌نکنید. رامین‌رضاییان هم تو این لیست هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25274" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25273">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8fLHW-jXdhMrOFyicjPrIzqFbkKmDTAcnDAiGFhsVuxXeVm4-mIIoeXYcfB1wg4ACI1WKs2Re2fLEDyu3p81n3ylBFvYvydfgKfPiYek-_nL8RFHoDWerBq-iEwopgLFHB_JKYd7xjJnRiV-9qwjcLnm58K3q-YfHxkpcBKq5L0uxgGVLdnTv1uejecVKjISupADzNFs3oCIblHlSHbyCHG__KUTe-v5R2zdOTAKbUgRZaxnNkgVg86GHS6gQIkXlIa-NPx5PSIaRGjwCzUti_SH4gyrnFozZitOfB0ZFbQzsTnDZ9nMOsTYkLXKMl2IJnVa1sbf80Hx2zx6Z22_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25273" target="_blank">📅 14:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25272">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWw1QlklJK-bWI2aXkV5b3-iiwd71mThw1i0d93MEPnx7Ruulz6el-MrHkbkWwwsYMhGY5M9rO-oTq3m3My3aaUPCVXhqOpPDMlxgRz6UskKQYTZeXiNnDH_hOiLzCwHMJNlkv2GhaJo4ra9z39X2CjqYMQXTJT6IPTxZXQvIQ7jaP6437UZ3czEV2nhAHDazRRZ7i7bf7WEujRhe2O_YBGBG_C1K_qnuqtLr75zMlyRLABuC_iZ-87blhZQb6-ILluBBWbnUPL6g60HMtRRLWjGZUU8IlRDo2m-Yme3XD1G5SEYN0TPf0KEMtTjdQBySJmLwfmqUalbiOtJXTzlnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا؛ علیرضا کوشکی فصل آینده در استقلال خواهد بود. تمام‌توافقات برای تمدید قراردادش‌ انجام‌ شده و بزودی‌راهی ساختمان باشگاه خواهد شد تا قراردادش رو سه ساله تمدید کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25272" target="_blank">📅 13:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25271">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu9kKmoGWcZT7y1sgfrz_rS7oTrGBhw_GmhU4gPYoljh0ADoiL7u1y7c_R2RSi49HjssHMCv1m2F3hYO4kjA-9pRYoc_OrkoY34yfgDuIzPxyxXalZzWDoFTeeFWBsqfoQkkG5KeaAvLDFmNrYL9V9kKWRl_bXBRUS7kO0D4a6Zi0Wu87UuG606hUmQicHdnyMjgM8OaN4mnkBGLtnp6mxfwaDirI1_kZsfmouFRqiO4Oh-PT2JKA8fgjzUPm19zbR2rDq9Ct4N2uK-XSkPKsDbpfPu8cNmrRZVP2c-sJ41Y82sM4AX6Hdz6lbtSEO9NNeyJ3ScnNNafPQcEq1iCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه استقلال باشخص امید نورافکن برای عقد قراردادی 3 ساله به توافق کامل رسیده و هافبک سابق استقلالی‌ ها برای بازگشت به این تیم منتطربازشدن پنجره آبی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25271" target="_blank">📅 13:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25270">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPtA7peb1X-fUcyMmyqlBB7Ca0qn2o4j6M2_jdRCExDqQaMJ_wxB0lx-SYu6x0wU-0WmOEBB9ZOu91BmyX7Fv0fnwQreAA0-576_76Z40urremz6aPONoRsDbdnG8gX8yKCiCC3fARoLzjQmNUA99v1WdtL-VjopGN3iobrjbXIlbJpUxI8y6pQmDur17nFOKPXRxMRJC_Wd-J1Jg3AmdlcPkJkA8LyrS5DEyupFnQGWwK4dFI8Bu2mbXfF6nu5u-RY5tP0ctutSSOX_B2IaQIY2SAh2UALcLbIyt7coHge6f2bZO-pGMYbroDmlOmCJm5hAaUs00e6SfGMdIZU_NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
باشگاه یوونتوس برای عقدقرارداد دو ساله با امیلیانو مارتینز دروازه‌بان تیم ملی آرژانتین به توافق کامل رسید و تنها توافق با آستون ویلا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25270" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25269">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myGj5zG4rW8Wbj96Iw-irOeF9vaQXyZWONzDIc2Rx1vMjsQGS_hjJdwtq22m5Emo27fTtI-fiNOWs2oCLHuiwwmbrVm9kl5rZ9hD-Z0tZS8hWvpdhmwjUwGeXMlO0i3e0s_llzsEjP8V2yFYXRdVtTeW-768D8dKODQNyJhLghi58BIOs8chFs5pUf5PTyt6Tm3LCECG3sk4pvaKlfuVGPVNyfVtOKvTtfQTV0uA2vzCvaKa8kp9p_F3RDVHDwiCXoUE4R49hRGayUn2tsFbndaRYcpIRjs7RBlO0R3OS2VQQGdBEhyvheSIx2WVWTbuiaaHQELHBPECPiZfusypWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
کریم آدیمی‌درسال۲۰۲۱: بارسلونا یکی‌از بهترین باشگاه‌های جهان است و برای من مایه افتخار است که‌آن‌ها خواهان جذب من هستند. در خودم میبینم روزی به این باشگاه بزرگ بپیوندم و بدرخشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25269" target="_blank">📅 12:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25268">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SxQSgk3YEWS5g-RMKJGLO3lPZxG8ds55rgiTkGmDU1S2ci5A9ZywmDeObw1CtZ8_EWsoUqlwjSdSnU62lNBvgRKr--5v1FQN0YvoCvRthKTAeBG0DuMhS85GczghrsmY9fbI0gbMg4x9RnYOpPqnolLu1O48jRE5bwX05FtqWIN9SRNw3RPBEwzAULPHBU_fS-l82ycVvx2aA-UzAyVkDwbJFYo93Azy-kUIpcvITC5qydJD_LLNo6jc6XqfzHFzBxcJTQgePN_Mc4qMtAv07BqlJkETIyks8KXEyLCYkicC86YLPr-NtzL0aMypbrD9OElsAsWAINXNhjHBx7fiyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت‌عملکردکلی لئو مسی فوق‌ستاره آرژانتینی 39 ساله فوتبال جهان در کل دوران حرفه ای خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25268" target="_blank">📅 12:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25267">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=mXPFfwW1plQ8Q6ckv5uzja8jAgtx52FcctVcx0LOAXAesxomTW15HG0T5idgVP1HSgqgmtvb4AR9EldX9weZuJxzK7OCDeHBe4kwyHnIvllqLMPzi6AGL6H9LyMm-ZuwBj8zTDskJHeB9LU1p__YAsG5vHfzAyRLoiF2etVobwVtYUk0gnKNw79w_lj9AdHvr6HoPxmzU6PImr0TKSGFmDQooTO0JNU6ijVbOx2W8NuOKBsENA8a6JqYkLiaXePj6QREYQY8pOxSAzLlUqgVUoEylGk2G73NSv_KQLaSFmegpATSEWQ_eNokL8rHOZfBH7IsBnH6mqITYbcAkFLtCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30af4fbd6d.mp4?token=mXPFfwW1plQ8Q6ckv5uzja8jAgtx52FcctVcx0LOAXAesxomTW15HG0T5idgVP1HSgqgmtvb4AR9EldX9weZuJxzK7OCDeHBe4kwyHnIvllqLMPzi6AGL6H9LyMm-ZuwBj8zTDskJHeB9LU1p__YAsG5vHfzAyRLoiF2etVobwVtYUk0gnKNw79w_lj9AdHvr6HoPxmzU6PImr0TKSGFmDQooTO0JNU6ijVbOx2W8NuOKBsENA8a6JqYkLiaXePj6QREYQY8pOxSAzLlUqgVUoEylGk2G73NSv_KQLaSFmegpATSEWQ_eNokL8rHOZfBH7IsBnH6mqITYbcAkFLtCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
جواب‌ فوق‌ العاده رونالدو به‌ سوال خبرنگاری که گفته بود میتونی‌ اسپانیا رو ببری: من تموم تلاشم رو بکار میبرم تاوجدانم‌راحت باشه حالا هرچی شد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25267" target="_blank">📅 12:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25266">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRN9QzkZ9g3gSDmBGqyVFeuipHxVrk1rW9W5YI0Fjv4NK-yFWlfD08Dpg3SWXSF4GIv1ZlMHj69BHHUoEh7nwe1c7lNi_NOOw3-7QvT488o-PEoBj9XhuAGGyKUPL7dRoujf5osgiFJ8zrYJ5Ic13ByPzC8ScLwusO9FUiyKbCoeffdy18ffUmU-HJpZPVHH5Y0Y7p_mEeUZhj79An0YW-u7veOh7RAm5cq2PvkmVxj6rft9GQPNW936YUIea-bdEt-OgWr1Ql7V00FiBWrXpK0JHaTDI7XAx-yNNlvr_eh5LYaJpNRdPMgagqfnfuCJz_7sF7wFV-9AcMf8bw5MnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛آمادگی پرسپولیسی‌ها برای‌ پرداخت رضایت نامه قربانی ستاره الوحده.
🔴
باشگاه پرسپولیس ساعاتی‌قبل‌باارسال‌نامه ای به باشگاه الوحده امارات اعلام کرده تا 1.5 میلیون دلار حاضر است برای رضایت نامه محمد قربانی پرداخت کند. اماراتی‌ها 2 میلیون دلاربرای…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/25266" target="_blank">📅 11:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25265">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biUbUw9a_LkeLNn4CuMZxgB5zboqz99Tx4Zho_MwhiWCP-qiykr0b0KkxbhXavUhOkQL0w8dK_kyowVwTmNXOgLSHX9axGoLkp7xeHmXKdVSmACnHdGagM3uBwK5YCrvgdXXZvjUa43a2e8XXiXo9v1t0tMxE9viVz5YOI-b92LikXl7cLAFTCAudhWjjpaNRzJ1jN_wTx40uxR3naRwOhMCBCrWpveiYYMIO4w6Ir8x9iTLUKYQn8Eu6JDDDPh2hJG_gABS17hj9n8f287dlsTQxObKpfCfmjYGtdYBz4K9zZhd0TWnUNX64n1pcHPKxnLHkrU698trXTaiV1fNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی: شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25265" target="_blank">📅 11:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25264">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBzI0T6_ikQ8Rfix7AHVMLJIsh8Wmm6LFPfAb6bpEjMmxcJu9H4NkvzCPkk4NMN6nEihmxK2GzwJ38j8x7Tut-X6F-PeHL-WhpDwg4sAacIM9x-qil8Ef8ml2twCf2V-IBoJpIgsHCklawk6LjypTsvhSP2PZ0dwvHpXMzDs_IcfOrBsKcVckmPgJwlfQQCrUgJsLuvg6Gg2l52BPcHC6uEqo8zCu_FYMyxsyNwCp7Fp62qnL-jCjj-xpIHL1yhCyMfeom4d0owZ5mZchD_NiP8H7lzGpJb27HR0CQvqw-GnAtNyZEBR-DO637PcIoZhL8Ows-c931zz_VVI9_Owag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ پیغام‌جدید محمد قربانی به پیمان‌حدادی مدیرعامل باشگاه پرسپولیس: پیشنهاد مالی شما رو پذیرفته‌ام، رضایت نامه ام رو بگیرید روز شنبه قراردادم رو امضا خواهد کرد.
‼️
پیشنهادمالی‌پرسپولیس: سه ساله بوده. سال اول 80، سال دوم 110 و سال سوم 150…</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25264" target="_blank">📅 10:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25263">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=i2XX83juDt1CFYL5cSkRtkUqmgT1B0khPDhjgAU504YowSdM-FFax2K8eBVtcM6U3oZKGlqtLHkMymJEH9mI0AChAllxnqIQFq4jdOaSZvvIXyfZ7Fo9CXf88v-yFlGoLBaVzpY_YNR4ePvAvqPu_bMW07zA6QOtUgNBqsevI4a_AtSBhz2d9CW0xE0EsNPgO6g7RTQ2UAbBJgHQkZGxubuWh4L7LY3NQO9yifosUWR6EvP1KSRJxYo3g9xfkFy-Ae-WqzV5djUG2yjFbPEvUT7IAwYz4XNMO76j48EhoVsvyyFvtE3d75drrzocfo08TwbxO7Z2aoYpbfCzo6JYnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e6448be0.mp4?token=i2XX83juDt1CFYL5cSkRtkUqmgT1B0khPDhjgAU504YowSdM-FFax2K8eBVtcM6U3oZKGlqtLHkMymJEH9mI0AChAllxnqIQFq4jdOaSZvvIXyfZ7Fo9CXf88v-yFlGoLBaVzpY_YNR4ePvAvqPu_bMW07zA6QOtUgNBqsevI4a_AtSBhz2d9CW0xE0EsNPgO6g7RTQ2UAbBJgHQkZGxubuWh4L7LY3NQO9yifosUWR6EvP1KSRJxYo3g9xfkFy-Ae-WqzV5djUG2yjFbPEvUT7IAwYz4XNMO76j48EhoVsvyyFvtE3d75drrzocfo08TwbxO7Z2aoYpbfCzo6JYnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس‌خاص‌وعجیب‌وغریب از 18 سالگی جواد خیابانی؛ خیابانی به خداداد میگه تعجب کن ببینم چطوری میشی. زنوزی‌هم به خداداد گفته بعد جام جهانی اول باید یه ماه تو تیمارستان بستریت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25263" target="_blank">📅 10:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25262">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am0LrPtXeGYyU8cGxlqwVvitQjP0al-HUW4Q0FY9sRnEt0C5xJJ0goWeFVS--P51nOVN5qUImj0_j-Urnx6OYJyXS1_r1JZxaJA6O29uMo9Et2YVuIiiNV9EsW7i9RJCul3FON3Mieqa4YHIrpbAKxdg_p80CppFWd8a2HNQOg9eDiBBUyeTOWCeMziuTVC8RDBobtcoZa49JdldXhxtsvfCksNRCRv0pSP83aGXi8mNJzlLvI47V-0u8ielFtSyK06e3oWLGKMCMTLaXfJj_AvWOBjKBlZRIFpwFEAYwGTfSVS7AWe_M4a8XDHC4q5ihxKhZ6SS7pr-MD8XtPRR1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نوع‌حکومت در ۱۰ کشور برتر و ۱۰ کشور پایین جهان از نظر شادی و کیفیت زندگی؛ منبع: گزارش جهانی شادی ۲۰۲۴ و شاخص کیفیت زندگی ۲۰۲۴
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25262" target="_blank">📅 10:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25261">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-vR3yMmMNAMUXXGgAG6-Q_BzVyLBCszsgEmNSyBYGzmbLW3Cqx_CT0_sYFjEzIb3SlO9bFs4VvgHvYtQlbhwX1eO_H6uGCw__V-UUviFvX-2TIza53Sjp-tB-2Ot3Ob8YVa4VmYQiyH0Kv4lxHSp2sX4LAEanwybw0pJRVLabaz-VpIhbxA4kxeEMFxlcLUn-4y-EOqC3F3NSUvW5NnYgskLu2qc7RFRyW6Lf2gz0rNMlz9HyLVY1ko2AxLLtmVlgYAf-0QKy-4-YW8EOMFyOnzWlLSpInD2pEQ3i4IRK974IkTH9-hj_BCPGPUtksva3lvpDc9vN1ja0DmbwICjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیو لو رفته از کلاس‌درس‌محرمانه امیر قلعه نویی برای سرمربیان آلمان، هلند، ژاپن و برزیل در خانه‌اش بعد از حذف این تیم‌ها از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25261" target="_blank">📅 10:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25260">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxKFtksgUEvlMNLJhqI4U2_-QlKBFijiB-YpNH2wG5yfMrOggoj2-KQdLLirf3wL_Auz1kAksmh0GmwjHHzey-Rn09RHI6pI5Lkun952Ng3Ik--p4NGMlSkFJaWecQe88GFXtZtCSfmhtftk48SzqXtyb1ywqnQietzN2KySQUXJxZPBqwbAgBLimx5jHEliJrlyPduTrSJWHYQ7w0b4tqBhDv6VJLkZAIX__2D9qqmywlEJwhvnIFl_pABWJK7NiiF-S43zscXAXTXZlGRxbOzeBpKlp1w22yHshrkbYGwkGhoxjxq6MYod9rryEGQfMySQEVzX4excgvWcE64xeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
تصویری دیدنی از لئو مسی هنگام زدن کرنر دربازی شب‌گذشته آرژانتین مقابل مصر؛ آلبی سلسته شب گذشته با جادوی اعجوبه آرژانتینی خود سه بر دو از سد یاران محمد صلاح در مصر گذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25260" target="_blank">📅 10:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25259">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxX2McI-kSP7MutprTNonmSXInYuoghu-4Eq3eduQaMQUUC7xUqYn9CLBRznLIm1HhzXEG4Yxz7yHqJA_JRJlQ9KFNhSbIpkQJFriLokwsLiBJYwiW08QIE21YQt9miZKezxhPQyGYMqNsZfMEWUaqv6fCnBliFGA5f479gT2ECiAZHqIdWIM3W5PxzFdDylQAfxrPiGFXcA0zMGBTp0snoLrsu1D4qXvxQiMolRHQV_Dp--W_kmrJTv28lTNM9qwrj5xBRemhJvIEONdEdZR9g5BPVDfNbMFHiQ8mqecnyh4P-MGGG9mk7BfA5iA4B2huJsEqqX41AA3_2tL-5GMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/25259" target="_blank">📅 09:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25258">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHv0S1sDyXdis2jP2oEiiMKbvfrtehEzDQlNywVw3zsd8rLAsOVnSDF8rUUSFgqZlwMHyr2wMcEOg_clAWKNQL2xEJIArDFRQaslqB4EQYCCwxeliHWS1DW3Wu5s1b0hshIzL90ukEfET45-lecX2rtCToO1LxRPI1jHloLQHn3B0rLuTmFuBc39ykw_6IDO_LWXIBlWNqb-5deQ57jT6z37hZJ09oyYASg-ief33ftaYrCZIUhDOt6vA76-MfU2CZD-MhB8do-6lKtiEfqkJsxXkpl8GvSWXZ1Rrz19afneyzUUN78wmgWaIBrVIdRH9eVFCNSe9QFF19bdYu7Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25258" target="_blank">📅 09:35 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25257">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/camMdHBnCHgncebOvNDOnx0Ja8bYQxN_Gal1Sc0NUuRQEkUY-kvunR2_5QyqoHyobcfQBSqgHpauYE-H3RjfX8107K5FABAqCeQNa8G3FGteUTlanI4mcsq5_j_OwkniBr2pYz9C5UFpaCfHDPd5qBpoU5O2GDjSmR6pETxpC9JxJ1yYiz-HmWgosLt1XM1Km0hnQnY03abghoTPb8m4I7-9oimeAyUMy2l7Q195kAfA-B2E1Xzy3vj6B-wPyxbWeyBK3-mIbeJi4vhaBwzStUf-NyDCupGr1LH7rcL93VTzT96YJju4bvZ7I9mSoVgSwcxrKVql48TfpHfQ6ikodA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25257" target="_blank">📅 09:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25256">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwR3cPOouqM68kmMcnvilPCTrbQRdELALkUlJJo_LWlPgdK_Lx4NSxn5EWN-E2mE1OP4OS1q7mRnGoDxxC0662c3hJzreicrPQJHA2wWnbrByeC0SVCxFeSIaY65eMKqEAM_ApycqatUSXNjO78o7l9NJA0ubNblNLsje-zm-z_GhK5Krj6AtFn0OjeZiUG6ekTul9ac3XC5poQagGFYsgrY4XAfFcoDtSiZ3-sYry0N0jY2ZmIO9eE3G1S67GaDXx12nE8mkdVscwNIP2xAODm0p4EqaEJXgfhgo-Pv8CNKLoe9QZk8DifOZFSJbHnYRwpY-yRmEjJQDvxyHNUXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25256" target="_blank">📅 09:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25255">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=n_0ilgI1vV9wJyE2co0FH2GOLi6C8QEa-uai8RrKwua1G8hq_cpBzKAWAXyQwr9kxuug9pW8eaFiVCupJBVzV3Mq90UhuqSSx02I7eEADAMY9U89Lq9tBkmWRsrwJ__W-LoJtK8rp2QBFRqE7dtWAq5yRLvtcJggBiNO0cg8uUVqd2MwXFFTDOk2XL1JKb72tA6MB_v7j8Z2rLOD_WVAfCcQzl08-4vCvNx_Ms0eepy2NF_YwUU_x7fzzNLKiGPajNanb33ILxEo0yaHzLZi8Z21RMY0VtVhbI6ldLqpNtic5bMfTviZQ5rU2Cl_F8nf3TvP5UujxI0V4_SX8SLC_Tf3-irm92YX5CrZEZHx7-9QCQpFfVZ4AGo2aBL-3fPMOUcVsZeG-y-LmlyiT9M7wr4fDF4xhc5nCXA3SbwHhcOscwEl8QuI_xyTRg8ULKG7ZpL4cDtWVmh69j1sjF3fQkIalXCDXWBRtycp6ZtPCZa6uOxNOxE0PVUyddqmBb4_kWNpuuS-7O3mXV40T6mZrQbp8rFlubB5BgGDTtwy1UQRgBDLbTlVRIzDe0HcTaKEzsVXQe-NYVf9oVIbJYNq3TL2DyYQypb_WK8yoYMwxAdysKlCT6jZRY8ARzJJjDaqGu3wSJp9f1eSgUSCrF0UcPCHzl8gb6RClXSYuS3PezE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8869652ba6.mp4?token=n_0ilgI1vV9wJyE2co0FH2GOLi6C8QEa-uai8RrKwua1G8hq_cpBzKAWAXyQwr9kxuug9pW8eaFiVCupJBVzV3Mq90UhuqSSx02I7eEADAMY9U89Lq9tBkmWRsrwJ__W-LoJtK8rp2QBFRqE7dtWAq5yRLvtcJggBiNO0cg8uUVqd2MwXFFTDOk2XL1JKb72tA6MB_v7j8Z2rLOD_WVAfCcQzl08-4vCvNx_Ms0eepy2NF_YwUU_x7fzzNLKiGPajNanb33ILxEo0yaHzLZi8Z21RMY0VtVhbI6ldLqpNtic5bMfTviZQ5rU2Cl_F8nf3TvP5UujxI0V4_SX8SLC_Tf3-irm92YX5CrZEZHx7-9QCQpFfVZ4AGo2aBL-3fPMOUcVsZeG-y-LmlyiT9M7wr4fDF4xhc5nCXA3SbwHhcOscwEl8QuI_xyTRg8ULKG7ZpL4cDtWVmh69j1sjF3fQkIalXCDXWBRtycp6ZtPCZa6uOxNOxE0PVUyddqmBb4_kWNpuuS-7O3mXV40T6mZrQbp8rFlubB5BgGDTtwy1UQRgBDLbTlVRIzDe0HcTaKEzsVXQe-NYVf9oVIbJYNq3TL2DyYQypb_WK8yoYMwxAdysKlCT6jZRY8ARzJJjDaqGu3wSJp9f1eSgUSCrF0UcPCHzl8gb6RClXSYuS3PezE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
علی رضا فغانی:
دوست داشتم هرجا داری کنم نماینده ایران باشم اماخودشون‌گفتن ما نمیخوایمت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25255" target="_blank">📅 08:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25253">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jA5lgcdxk7tFT5o7np-3Trud7loU_6Pc51FAKrDvATM1syJowwnR69zPZdebUx-j4ntXd4HC9On0nXZV6FNijFWv6SIrvzf3lMDWF3XU0JM9Wb3AN8hh-phn1LDPOIKrFl75e-bTkCzx1abeGrbBfmqh4tF6YSMT3W6HU76j9Ol4GjauXoaLlpe1eFNpGqrjVpRflfa68TiChdXw5doUob-eRI-nwW1WxhxoqmcjCVONTSWPB-f2Hir401bXOuf2S7K0TviRSqb5lddOoF9x1Cv_7-nMe8s6NW6gq9twKP8nRWFtIDzdS9jYaqJitRlc7QUZApj4ZPt2neyRfCyfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امشب؛ آغاز مرحله حساس یک‌ چهارم نهایی بارویارویی‌مجدد فرانسه و مراکش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25253" target="_blank">📅 08:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25252">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSY4jdcPH3hkMzDYl5XYxKTxc7FmNGgxc70ixu4saSuOyObJXbbgIN7jWBnbxbaKfTmG24qw-xf00Uc-QncpA_pkDLvAeogKYD5z4Q_xr2AxIZw8Fhrke4h7SlcB7KrSpDiKrIPus51nte6s7c3OMBQNjcqVV7wwZUxppFtBKR37mxMITQ3w3OjHDUQC9vwB6C-xMaypS_vU6PE-L-KlNt1dhcscRbd-Lzt391or0JwFF6YZVK2qiXGXbS9x8aodqd_aCGSBCgcFXAsyddCyvAesRWylUNF7MrmS_4DzPcrXdLx6p974uAkK5lA2sz0tq6uhO3t7i3vDaTxLqSO8vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
جرارد رومرو: ممکنه‌ طی‌ روزهای آینده کریم آدیمی ستاره جوان دورتموند با عقد قراردادی 5 ساله به بارسلونا بپیوندد. مذاکرات مثبتی صورت کرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25252" target="_blank">📅 01:53 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25251">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Foe5HUp5rpQbaybRmndfsWOcKsOCxCrGh5sYVri13JkbATP2YyQYsUGa1SwgmyStAPRxR535G4B0Q-Bc407iS93DaMUqscUHpoH56tDPnADwyfBmiTzoUF_mGjnfQHbSy6WnIE3D21QZlUnjMZ8bZTSf0UbcDuHzZVbqKzNbctkp8zurCFkFE9uJUKUsQ-bdRLmNv5B0BvSLOLgy49Y90X4MHNzW2vustrHaYxc3VwVxQG3aMwgp8lFVhXZ5FbdxFGX958jEaKwwKuX4neltduZ4bhWuPB8b59b-9IF4LdiksaYfPfQAXq0TwkXzOPwS14X2EtWhI06Zgo46J4SvJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
نشریه‌بیلد: کریم آدیمی ستاره 23 ساله تیم دورتموند به مدیران این باشگاه اعلام کرده که قصد داره از این تیم جدا بشه. منچستریونایتد و بارسلونا به شدت دنبال این ستاره آلمانی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25251" target="_blank">📅 01:45 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
