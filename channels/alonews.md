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
<img src="https://cdn4.telesco.pe/file/ThMvhdtBjjYMojPYZoSGz2EJTiTD1gKwe2RaQVGWezO7L5aW-E0JlSy9MgKZ3iPklMYpXEDNw2exjtZI5bhEhQrQCNzXvnwO1PoSf1HvJwkjRvadVg2dTHPhYyV-R--uAL_wN6t4Ho1Ow-xgQVaEwU-biaEwD5VKuYY5ePPrmtpAIQMBtYh9zx1s74zYqAAp3rYoOBoOs9qO46Oi5HItagSuCotFD2TCEoygjrWSGeOx7O1-AZSTz5VEuwES-6ZwiRS3gu8UIjYACqrCvAAwE65LdHHLKsV3yf-z1-Nx0iM2Rd8tntbM-FPF8ARkY8YqsgykGXq5rbmwL-luztcTcw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 974K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 08:13:16</div>
<hr>

<div class="tg-post" id="msg-140681">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
طبق گفته بعضی رسانه ها یک پسر جوون برای مراسم ختم آیت الله خامنه‌ای از آلمان اومد ایران،ولی موقع برگشتن نذاشتن برگرده،چون کارت پایان خدمت سربازی نداشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/alonews/140681" target="_blank">📅 08:03 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140680">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=KIBCAg6USV6SwBNXU0UHSTJjysgC_hPw4PteyufDDqYP8N13kxGhdPL5fr9w7lxS8quH3APDHHYDb5J41ILWGoAYzH69hweTVJn6OURCSDKoReSsGdYu58WoC57tEQk559wCEdLcr_Y6htgJ_EwLUl49Xodq5_dDGXn-YYTK7fJOVsuCZkvfDR0D-af56WK0EUj23lBieXXFoRiN1Cn9iTI4v4xn0JA_gAij6E_NHoVeZSMVAH1m_AdgXi8X4zHyR-IKgEVxmInvkD5igA5yWpSMnFET50diwxG1vlnEwlseOLUB9fHLcSA9pGz8-7M0BH7j_FqmkO-3QIBOEul8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=KIBCAg6USV6SwBNXU0UHSTJjysgC_hPw4PteyufDDqYP8N13kxGhdPL5fr9w7lxS8quH3APDHHYDb5J41ILWGoAYzH69hweTVJn6OURCSDKoReSsGdYu58WoC57tEQk559wCEdLcr_Y6htgJ_EwLUl49Xodq5_dDGXn-YYTK7fJOVsuCZkvfDR0D-af56WK0EUj23lBieXXFoRiN1Cn9iTI4v4xn0JA_gAij6E_NHoVeZSMVAH1m_AdgXi8X4zHyR-IKgEVxmInvkD5igA5yWpSMnFET50diwxG1vlnEwlseOLUB9fHLcSA9pGz8-7M0BH7j_FqmkO-3QIBOEul8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/140680" target="_blank">📅 07:45 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GB_fBXixQxtYKw-OsfrEzqbxkp7Ad5_Qe__1842zmXX8SHHwECyxqLB5IqlP0R_hIiGmprJEaIpqhupp4rjYdwbv2krbPKF1lBwii_XQnl4aOZfl63jDUsUFeuzDpVwP-Mr5kmYfuyKc7fU03wJTrlXr1H9R3EucV9dSjUjYSKVTIl15MBgi_fGDtL0BYgI3P3k_8V_sK1nbIhOJJot5AKzRTJ3oX4xPFbOIVXfMzcpJ92Lwem5nNJQn6s7UdvPY1SGYNCvfX_ZWmwfCRSF0Sg5e7dKU4Bm65TascD5a2RXuWR9YGegnWdvWrzj9QqghMCCiD8wmenF9Nw9iILF7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/T3yQ40a0oHIMiOThljGqnkavyALLji_BV75qE5n-DxWiPtOAaXLKuOFpHAAVf1cs5GBdi52mneCg_tO_gOLGiN-jCd4QmTQt6Sx1c37j46ZZWDR25xPJaD32eVe-OHa9hdZrq2aPsYBEy1QDMlY1Vo5vx7K49-rREe822F6GTi0jlVBRlz8PaakyXX8PVYk9-Bjqgi5ltB30zg9z-Yvd1tDKsZ-ToR4MMkI4-ep6fEuRBko7OTL30-GaXp5_8fgcj08NnwTqbyPg9TLkrOMwu2afHKPwNCGjsRUBmj1zPKdbtANc2---AYo0LDTls61R2m_bscEcB7g3bQHaPwNALA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر عجیب از بندر شهید رجایی  که بزرگترین بندر ایران است اما به دلیل محاصره خالی خالی شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/alonews/140678" target="_blank">📅 07:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">⭕️
⭕️
قیمت طلا و دلار هم اکنون !!!   سایت دلار و طلای تهران@nerkhBroz  داره لحظه ای قیمت میزنه
👇
👇
@nerkhBroz  معتبرترین نرخ طلا ابشده
☝️</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/140677" target="_blank">📅 01:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⭕️
⭕️
قیمت طلا و دلار هم اکنون !!!
سایت دلار و طلای تهران
@nerkhBroz
داره لحظه ای قیمت میزنه
👇
👇
@nerkhBroz
معتبرترین نرخ طلا ابشده
☝️</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/140676" target="_blank">📅 01:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
به مناسبت روز خبرنگار برای خبرنگاران  ۲۰۰ گیگ اینترنت رایگان فعال کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/140675" target="_blank">📅 01:30 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
‏سنتکام: اجازه دادیم حدود ۳۰ کشتی از منطقه تحت تحریم عبور کنند تا کمک‌های بشردوستانه به ايران منتقل بشه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/140674" target="_blank">📅 01:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acf3aa5132.mp4?token=Wo9IiVKdECP_RSjbB1mrzKBakjwFOiL4b9I225fXDuJtNY4FRpunoQAqgqnkNmkiVyT2_lOdRP4uKgfQ6IEIYX_BN_-NhqVX0rKnCkarm7NUgAwR-T0OsvbWBZEZkjN8Y9kLvriIYFby_vM4zFQV_6z4ZTD30eiA8Fen_FHxDO-iw1CbH1a_jxtTn9tR4ia_RVEaXN3KaD68FDGZoj7yxk0Cr-5EmxS-XqvA8tiRlrJbtjDEoya5ZrslTT5U6DqoEM5hY9Ibtn9bqnIti6dsyw2RBMEDu_-yqaasxuTSgUF1cPSCodc_vPSlyr7EVaDDlksDUYWTfjB4PwoM2NupTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acf3aa5132.mp4?token=Wo9IiVKdECP_RSjbB1mrzKBakjwFOiL4b9I225fXDuJtNY4FRpunoQAqgqnkNmkiVyT2_lOdRP4uKgfQ6IEIYX_BN_-NhqVX0rKnCkarm7NUgAwR-T0OsvbWBZEZkjN8Y9kLvriIYFby_vM4zFQV_6z4ZTD30eiA8Fen_FHxDO-iw1CbH1a_jxtTn9tR4ia_RVEaXN3KaD68FDGZoj7yxk0Cr-5EmxS-XqvA8tiRlrJbtjDEoya5ZrslTT5U6DqoEM5hY9Ibtn9bqnIti6dsyw2RBMEDu_-yqaasxuTSgUF1cPSCodc_vPSlyr7EVaDDlksDUYWTfjB4PwoM2NupTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ریاض برای جشن توافق دفاعی جدید مکه
🔴
خیابون‌ها و ساختمون‌های مهمش رو با پرچم‌های عربستان، پاکستان و ترکیه، نورپردازی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/140673" target="_blank">📅 01:21 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
نیویورک‌پست: ترامپ ممکن است حمله به ورودی‌های «کوه کلنگ» (Pickaxe Mountain) را برای جلوگیری از راه‌اندازی مجدد برنامه تسلیحات هسته‌ای ایران بررسی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/140672" target="_blank">📅 00:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b213e05880.mp4?token=XqZxrwTB-PTeja7af39bfdrham-_ZTOAsjM4HjPXwNqhE2wIqO3SHgLILKX1C6_73Rtt2K8-9OYEMBA_IF3tAsyTdy2Z8QDIvjXgs1lL42LxTa7q8fjw3yILG8Uzbt8keFrp-Vngr_Cw1gf6jEu-ZVdj94_2BXkq-lNOt3EvpxWPVxiedcTBVeCSmCYxIQAGbyPk2kkKNogR1b25jINjwFgStPmfDuWxshpWUUtcO7ji-Cmd8DbOqQBdd0dBZQrO9tsG4TZyDOwCzjqENnZUht6-5mgzhSoxDmNPgYbjclohVVJ1eOY8aJEsJZKe8YD39vaQK7P2L3rdH-BG3diRpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b213e05880.mp4?token=XqZxrwTB-PTeja7af39bfdrham-_ZTOAsjM4HjPXwNqhE2wIqO3SHgLILKX1C6_73Rtt2K8-9OYEMBA_IF3tAsyTdy2Z8QDIvjXgs1lL42LxTa7q8fjw3yILG8Uzbt8keFrp-Vngr_Cw1gf6jEu-ZVdj94_2BXkq-lNOt3EvpxWPVxiedcTBVeCSmCYxIQAGbyPk2kkKNogR1b25jINjwFgStPmfDuWxshpWUUtcO7ji-Cmd8DbOqQBdd0dBZQrO9tsG4TZyDOwCzjqENnZUht6-5mgzhSoxDmNPgYbjclohVVJ1eOY8aJEsJZKe8YD39vaQK7P2L3rdH-BG3diRpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این ویدیوی ناراحت کننده از پدری پایدارچی که موهای دخترشو بخاطر حجاب نداشتن کچل می‌کنه خیلی وایرال شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/140671" target="_blank">📅 00:24 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
فوری / شلیک موشک بالستیک توسط حوثی‌ها به سمت مواضع دولت یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.7K · <a href="https://t.me/alonews/140670" target="_blank">📅 00:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سی‌ان‌ان: بعید است تردد کشتی‌ها در تنگه هرمز به سطح قبل از جنگ برگردد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/140669" target="_blank">📅 00:02 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان: یک تیم باید تشکیل می‌شد تا نقض تفاهم‌نامه را بررسی و حل کند نه این که دعوا کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/140668" target="_blank">📅 23:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل درباره ایران: از دیدگاه ما، بهتر است که هیچ توافقی وجود نداشته باشد
🔴
به نظر من، از دیدگاه ما، بهتر است که هیچ توافقی وجود نداشته باشد. ما می‌توانیم به اعمال فشار بر ایران ادامه دهیم.
🔴
و من به شما می‌گویم: با کمک خدا، طی دو یا سه سال آینده، رژیم حاکم در ایران سقوط خواهد کرد.
🔴
به یاد داشته باشید که این ماجرا از کجا شروع شد—ما اطمینان حاصل کردیم که تمام بذرهایی را بکاریم که به سقوط این رژیم منجر خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/140667" target="_blank">📅 23:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvis7Q0XkHKy933z_rl9NkAJoIo2LYCWM-zCyV3eczR308Sdjnrn_kPpev8G1Y49OY1zQ-T_cccIsaxy6qzi4-N-ldgYLca6aDwyxpqYytEo9qVqIwV06P-FcFiR9o1bus8Zx_ETyRynEa3ehxqqXjmXE8-fb1Y9JsR3_lxuwci-I7Ay_H6RC7bNIa4eRdnP_G9eYYHtWg0bnZVni7xp_Wm1eTYyhe6V5cMI_YnhGDaAVZCJAJD2Z1c1HxtluHFK6l6SEG5-BR6aV7eVA3vioOoSDW5ngO3mZ9AMS6EG4rhAv1mB4je3S7LYPzUHhWxqTK8MH6iuaMi665trDczEJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تانکرترکرز مدعی شد همین حالا ۵۶ نفتکش در تاریکی دیجیتال در کریدور عمانی تنگه هرمز فعالیت می‌کنند و جریان نفت کشورهای عربی را زنده نگه داشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/140666" target="_blank">📅 23:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIRkC5TYLqu-Ps3jxldPbgRIuWpx3EBMttS5JIIyMYMBNX8-2Ilxvr9p4N7G0TBchGBog-_7EIHIifMNsBm_ax8nerMQTQ2CpnTJVnqrSegJnY1jjiE1aRksCuOnb-kjTQekuRHvJwef4_v19lhpl0y8T6McKfdWHvUvzCJcRdDNgylZS-VgncNCts1K6254yujSoelpxlEo5P51jDxnTfHJHdjdfnK9tTOUWOu5Lh2aPZ2DFMw8PbCWwsc4_Lawxe8BzWDn3zoolk9kOWUL732G_h-OoOwZs5tGE66JA0YoEdY7yh6qv4hXlkb2yxBBg7txSc-SskYzMppATuyjRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۲۵ سال پیش، جبهه پایداری افغانستان(طالبان) این مجسمه رو با ۱۴ قرن قدمت به علت غیر اسلامی بودن تخریب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/140665" target="_blank">📅 23:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
سنتکام : ملوانان نیروی دریایی آمریکا در عرشه پرواز ناو هواپیمابر «یواس‌اس آبراهام لینکلن» (CVN-72) در حال انجام عملیات تعمیر و نگهداری جنگنده‌های F/A-18E سوپر هورنت هستند تا تجهیزات و جنگنده‌های گروه ضربت این ناو برای ادامه اجرای محاصره دریایی علیه ایران در آمادگی عملیاتی باقی بمانند.
🔴
ارتش آمریکا همچنین ادعا کرده است که بیش از ۳۰ کشتی حامل کمک‌های بشردوستانه با مجوز نیروهای آمریکایی اجازه عبور از محدوده محاصره را دریافت کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/140664" target="_blank">📅 23:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140663">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
عراقچی: موضوع «سهم ایران از دریای خزر» در این کنوانسیون تعیین نشده است
🔴
ایران در دریای خزر داده شد و رفت» اصلاً واقعیت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/140663" target="_blank">📅 23:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=FA_TXBKHm8r1YwktU0yzEFZ4-iQClGihXc4RP1Ru15x7HMfzjiZ5pvWe45MV20QAbcr4cuEuHBEQxliJI1pDdZGh2icUQILUJpevPPYPndGAbvQ7zBWA6yC8UMFoqLCXx47fBW-N-kbAQYK7ggTfWTLvjCd3zSEBFhhEOuSYazRqARcGX3t1hKT9jP_Mgads7k28lOt07SoJTCBLqAA4OYDAHkoWM68aNswinOKZWXzN7hJEQS2_7y4VGMDNslZOZqD3hmHBSNEneZDlSX4xQ4vweMDHoUIgf-XjxzOMxk1G3SSfBZalNrDZKYFmbkFQpRxutx2cHVVzKnQ2h-MF6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c32fad0f32.mp4?token=FA_TXBKHm8r1YwktU0yzEFZ4-iQClGihXc4RP1Ru15x7HMfzjiZ5pvWe45MV20QAbcr4cuEuHBEQxliJI1pDdZGh2icUQILUJpevPPYPndGAbvQ7zBWA6yC8UMFoqLCXx47fBW-N-kbAQYK7ggTfWTLvjCd3zSEBFhhEOuSYazRqARcGX3t1hKT9jP_Mgads7k28lOt07SoJTCBLqAA4OYDAHkoWM68aNswinOKZWXzN7hJEQS2_7y4VGMDNslZOZqD3hmHBSNEneZDlSX4xQ4vweMDHoUIgf-XjxzOMxk1G3SSfBZalNrDZKYFmbkFQpRxutx2cHVVzKnQ2h-MF6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایشون به اسم آرش، خودشو اولین:
همجنس‌بازه، شیعه، پادشاهی خواه، دو رگه تُرک و لر معرفی کرده که پشمای همه ریخته!
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/140659" target="_blank">📅 23:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDCoZA9rUSUQoSbEvoN3N_vgRRgeOx4wNpzb9w5DBYeLna2He1R5XF-8DEVwyElTz729ofq-ZyJFZdY2Yn_in1zwUZ2V9eFXu7AjkOLrAIR7sFJjd23NSM058Z3KxQuBmHyFC7L4-Va2eeToyMr2yaI6I6mRhzuaytoTIh2HXACcl4cO4Qf_QAGgPxden1DQjLJrwxMS5VaRVCVQeh27bAcdbDKHWilcl_hghOEQRZ1fRMc8j-G0LxC6LZWTBvlQCNtzOJ8XXrhBWzf-PbB5wPGpq3yVbporYbV0InAdXpgG3AqpXqT-5Ep8dRlyN9VzYns4ELL_nNb6vxb1gU5fKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/140658" target="_blank">📅 23:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان: برخی توقع دارند در آمریکا و اروپا گرانی باشد اما در کشور ما که در جنگ هستیم گرانی نباشد؛ این در ذهن من نمی‌گنجد
🔴
وقتی در جنگ باشیم کمبود پیدا می‌کنیم و باید برای مقابله با سختی‌های آن آماده باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/140657" target="_blank">📅 23:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
نیویورک پست: تأسیسات هسته ای کوه «کلنگ» در تیررس ترامپ قرار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/140656" target="_blank">📅 23:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
منابع یمنی گزارش دادند مقرهای عناصر وابسته به عربستان سعودی در مأرب، هدف حملات موشکی قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/140655" target="_blank">📅 23:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140654">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
الجزیره : پیامدهای بحران تنگه هرمز دیگر تنها به محموله‌های نفت محدود نمی‌شود، بلکه به صنعت خودروی جهانی نیز کشیده شده
🔴
مصرف‌کنندگان احتمال با افزایش قیمت خودروها یا طولانی شدن دوره‌های تحویل آنها مواجه خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/140654" target="_blank">📅 23:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: تکلیف جنگ ربطی به دولت نداره و به رهبری ربط داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/140652" target="_blank">📅 22:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
کارشناس صدا و سیما: باید نیروی نظامی ببریم و بحرین را پس بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/140651" target="_blank">📅 22:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: سال تحصیلی آینده حتماً حضوری است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/140650" target="_blank">📅 22:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سنتکام : ۲ کشتی از کار انداختیم، و ۲ کشتی متوقف و بازرسی شد
🔴
تا تاریخ ۸ اوت (امشب) نزدیک به ۳۵ کشتی برای کمک‌های بشردوستانه اجازه عبور یافتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/140649" target="_blank">📅 22:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
پزشکیان:
از روزی که اومدم هر روز یه داستانی داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/140648" target="_blank">📅 22:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140646">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
زلنسکی : تصمیم گرفته شده ۳۰ تا ۵۰ هزار شهروند کره شمالی به روسیه اعزام بشند
🔴
اون‌ها دارن این جنگ رو بررسی و تجربه می‌کنند
🔴
ما قبلاً موشک‌های کره شمالی رو در خاک اوکراین پیدا کردیم
🔴
موشک‌هایی که برای حمله استفاده شدن، امروز دیگه این یک واقعیت اثبات‌شده
🔴
کره جنوبی باید همکاری خیلی نزدیک‌تری با اوکراین داشته باشه و ما برای این همکاری آماده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/140646" target="_blank">📅 22:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140645">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a550a2187f.mp4?token=AxKq7CLy6eNc5630ZWfEyBx506wf4AlKWGpmjhYg8MXMJLCWgkvuACENcWybjPlfRjjEFBY2LRDZ9Ezifhk-ChIfAFYI2p9QzMcLT2p-JlBWi-P8US4Hjg9LfUjqzsdnf0PVdhH594zVn_j7Y99ruZh7dOb_lhXgqKs-QmcKVOknkPijKRgDEixXlZXQ7uI1mhFk9wxrIi5J1FX25HHGJM5JONFXrpgCOpY1DepMU6eu3thxcF8DRBfRxRi4YXKS0afbhS5Ed94-i81dB86iK9glN0kTIP3qJp6PeowGZzW5bSSEMuKNWqAKje2RifZ9W82ie7Aeytl0d2jJaFQyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a550a2187f.mp4?token=AxKq7CLy6eNc5630ZWfEyBx506wf4AlKWGpmjhYg8MXMJLCWgkvuACENcWybjPlfRjjEFBY2LRDZ9Ezifhk-ChIfAFYI2p9QzMcLT2p-JlBWi-P8US4Hjg9LfUjqzsdnf0PVdhH594zVn_j7Y99ruZh7dOb_lhXgqKs-QmcKVOknkPijKRgDEixXlZXQ7uI1mhFk9wxrIi5J1FX25HHGJM5JONFXrpgCOpY1DepMU6eu3thxcF8DRBfRxRi4YXKS0afbhS5Ed94-i81dB86iK9glN0kTIP3qJp6PeowGZzW5bSSEMuKNWqAKje2RifZ9W82ie7Aeytl0d2jJaFQyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولودیمیر زلنسکی رئیس‌جمهور اوکراین درباره صربستان: صربستان اکنون، به باور من، در مسیری برای بازسازی استقلال خود از نفوذ روسیه قرار دارد.
🔴
آن‌ها یک «روسیه کوچک» نیستند. این‌ها روایت‌هایی هستند که عمدتاً توسط روسیه ترویج می‌شوند.
🔴
آن‌ها یک دولت مستقل هستند. به باور من باید آن‌ها را تا حد امکان به اتحادیه اروپا نزدیک کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/140645" target="_blank">📅 22:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140644">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
زلنسکی : اوکراین بعد از تموم شدن جنگ, از آمریکا تضمین‌های امنیتی خیلی قوی‌ای دریافت می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/140644" target="_blank">📅 22:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140643">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhqsmNxHbf5zO8gDEAyjBo0EGYrbEpLqoKRUO8uLIDs_Yxk03Ba8x9AXhNM4OFSW2Vs3LOkuw0HnpoRR02UfdTzFvvNs9n8s4yRecuMOSswCSS5wUSeGhWwnkzj9KOMJN2s-HMJD5Aou9ewI1eso5iA3QOBoDWLhgrEBJG3UN3mT33uTF6adYGoNrV39oGifp5F6Q8rUpkk3tk7PmLid0vIqDiVPpMH2o8WqoGjql7QQsfg4G-BCfjfrPuAoR4GWF3f7kLwghLnjOa6ByXbdLG0iQ3gHZW6kZI1rd8uXTd20VJ9u32LdGfpVxBVDJEoJtWxqByQqLbECND9AehKssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
از صبح امروز تعدادی اسکرین شات فیک منتسب به مژده نظری عضو تیم‌ملی بسکتبال توسط برخی منتشر شده که تماما دستکاری و شیطنت رسانه‌ای بوده
🔴
این عضو تیم ملی هم با انتشار متنی این حاشیه‌ها را تکذیب کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/140643" target="_blank">📅 22:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140642">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd6ed49d.mp4?token=TllBiLXN2yvHZXaEin5tJj7aeOaSkiAockGEg6mN7tqkXXY_nFfAQYq_wJpTT3oq0acJBW_ApvvFs_UBdFw6yMhEInOVlwdVEZ4GGAk0CepTJBgnAtSCR4NL66fNwmUw8N0Mx42aKbbh4iq_W6iEF2BiWRT2FTfOK6L_QKAkgqaoS9rZpzqJPCAW9IU9O03YzT173eB-PwcbE_5AlxHRX2Qo3cF96xQDwUuzXkHq4LE4cdhIyaUQwCczbab9UDO6r-Ed_OaYb24caUjHM9Wbl14POnzBuUQqg3tNQyyDaCho8Mmg2bOSRi_sQgDKR0Y-6u-HstQJppL4BpFUqTU3tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd6ed49d.mp4?token=TllBiLXN2yvHZXaEin5tJj7aeOaSkiAockGEg6mN7tqkXXY_nFfAQYq_wJpTT3oq0acJBW_ApvvFs_UBdFw6yMhEInOVlwdVEZ4GGAk0CepTJBgnAtSCR4NL66fNwmUw8N0Mx42aKbbh4iq_W6iEF2BiWRT2FTfOK6L_QKAkgqaoS9rZpzqJPCAW9IU9O03YzT173eB-PwcbE_5AlxHRX2Qo3cF96xQDwUuzXkHq4LE4cdhIyaUQwCczbab9UDO6r-Ed_OaYb24caUjHM9Wbl14POnzBuUQqg3tNQyyDaCho8Mmg2bOSRi_sQgDKR0Y-6u-HstQJppL4BpFUqTU3tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بن گویر، وزیر امنیت داخلی اسرائیل، با انتشار این ویدیو نوشت: تروریست ها شبا گریه می کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/140642" target="_blank">📅 21:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140641">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال شریف رو بخون هر خبری لازمه بدونی اینجا هست:
https://t.me/+rIN7nnv4nEwwZjk0</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/140641" target="_blank">📅 21:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140640">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از مقامات رسمی:
ترامپ تصمیم گرفت با وجود هشدارهای ستاد مشترک ارتش در مورد مهمات، جنگ را آغاز کند و انتظار پایان سریع آن را داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/140640" target="_blank">📅 21:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140639">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: روسیه و چین از نزدیک ذخایر تسلیحاتی آمریکا را زیر نظر دارند.
🔴
ما در کره جنوبی پس از انتقال تجهیزات دفاعی به خاورمیانه آسیب‌پذیر شده‌اند.
🔴
گزارش‌های مربوط به کمبود سلاح نادرست است و ما هر آنچه را که برای انجام هرگونه حمله‌ای نیاز داریم، در اختیار داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/140639" target="_blank">📅 21:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140638">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نیویورک تایمز: ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/140638" target="_blank">📅 21:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140637">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
نیویورک تایمز به نقل از یک مقام آمریکایی: نیروهای ما در کره جنوبی پس از اعزام تسلیحات دفاعی به خاورمیانه، در معرض خطر قرار گرفته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/140637" target="_blank">📅 21:43 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140636">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
فیدان: مصر هم به توافق مکه خواهد پیوست
🔴
مصر، شریک طبیعی ما در تمام مسائل است.
🔴
من معتقدم که در مرحله بعدی، مصر نیز به عنوان بخشی از این ائتلاف، به ما خواهد پیوست.
🔴
چند موضوع فنی وجود دارد. پس از اجرایی شدن این موارد، هیچ دلیلی وجود ندارد که مصر نیز نتواند بخشی از آن باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/140636" target="_blank">📅 21:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140635">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
نماینده دائم روسیه در سازمان‌های بین‌المللی در وین اعلام کرد که تنها راهبرد مؤثر برای پایان دادن به درگیری آمریکا علیه ایران، استفاده از مسیرهای دیپلماتیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/alonews/140635" target="_blank">📅 21:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140634">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزیر خارجه ترکیه: ما باید در اتحادیه دفاعی دریایی سعودی شرکت کنیم، چون امنیت دریای سرخ برای ما هم اهمیت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/140634" target="_blank">📅 21:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140633">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
فرماندار الضالع در یمن اعلام کرد نیروهایی را برای مقابله با حوثی ها به خط مقدم مقابله با آنها فرستاده
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/140633" target="_blank">📅 21:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qF7eB_KxMXbfexDD7s1M7WFpVt3n56m3zQS8Wz_C3oiJLzJFVkZstshNFg3rYoscDL9FxY_OCj-kRGvCCLkebr1sWrwuEoUNTVRcdVtjd3B9oVE_U2SUQrQ_eWj1nNZ_xiqkDxHQpzYljdaogeGejvHSTZH7JQWFShNm9WstoAoAiEmumvOImwj7PUDdoVJCfkNPe-dpsOVPByRZdpeuZwrwdKYGX7HirETUeE92h8OOZY4f7PVbgFyaMxuiXkK4qmBC8wPAPJzF49TPQd7xNCY0qrwjTIjtxvB43DfZ-r67p68SAraBd2hfrAlDVziHvxpWn93M7H4OQ1o1EM-qaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سردار جباری:
یبار آقا از من ۳۰۰هزار دستی گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/140631" target="_blank">📅 21:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سخنگوی ارتش یمن: مواضع حوثی‌ها را در چندین جبهه هدف قرار داديم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/alonews/140630" target="_blank">📅 21:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0e272670.mp4?token=fWhpVB3oeeJAoH9aRRUmwMJPiyDrtYvMGYu2XPryrSOTkEFoEtTbyck6KDn7hf0QLxAGxkDduwgj2UFyKjKNmMj6bwLyqJcHV-XFoRzDWjM3Hjx_gr3E3Xmg6fuY9svWdq-UglI2Lb3tV5bnBDiWRm6zv_p3KaO6wS6C0S6TeOlDlgt9VXzAZ1FVKstJHGzlIRxgr6VwKlBQYHnqYJk7ZzbsaGK4e3Q0uwu2QrxFIDlR6_A4LRKC5TM2SF1OkIX0fkK_5Bsj3bJ-8HFVVlD-yI1H9Jfrr0EeOrt3UrUfP1xoDF_Fyg_zFElUtgspCeaQFyzKoFOfSqL3cUu0CFR8Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0e272670.mp4?token=fWhpVB3oeeJAoH9aRRUmwMJPiyDrtYvMGYu2XPryrSOTkEFoEtTbyck6KDn7hf0QLxAGxkDduwgj2UFyKjKNmMj6bwLyqJcHV-XFoRzDWjM3Hjx_gr3E3Xmg6fuY9svWdq-UglI2Lb3tV5bnBDiWRm6zv_p3KaO6wS6C0S6TeOlDlgt9VXzAZ1FVKstJHGzlIRxgr6VwKlBQYHnqYJk7ZzbsaGK4e3Q0uwu2QrxFIDlR6_A4LRKC5TM2SF1OkIX0fkK_5Bsj3bJ-8HFVVlD-yI1H9Jfrr0EeOrt3UrUfP1xoDF_Fyg_zFElUtgspCeaQFyzKoFOfSqL3cUu0CFR8Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عراقچی: مذاکرات با عمان برای تعیین مسیر موقت تقریبا به نتیجه نزدیک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/140629" target="_blank">📅 21:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgQyqPOgERMjMrf3bTYbXNWilhmq6KBN-agRJcynbpoAsGgSbhFItLpWlNKuROaPnEx4boZ7QLQ_08U8HFwgsno-5qTCF3J6Y0dTp4MzvpaRpPZ56FfqCv1AN7lDqX8bsjf47d3UIdKH-I8FwCaUhGTzq0iYdAguoyhNAANitIxIul9dSAijSQXmIMK_VPwMQbU3atcdYRfM2U65tF625kCnJcM-GVTyW0OdnCpH9nz-ehyZr_DDR8bMEcUC-24YA0TTzU_LMCD9ac4OYyrkC9bYOaxtmHYDjZDACTXgbX1jIBA7AkrNCvuhyG-bFy_Yzvmx0O7kgGjYIzi3GHWdZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / کانال ۱۳ اسرائیل: اسرائیل در حال آماده‌سازی برای احتمال اقدام یک‌جانبه علیه ایران است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/140628" target="_blank">📅 20:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140627">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
کان نیوز: ژنرال برد کوپر، فرمانده سنتکام، برای رایزنی‌های امنیتی وارد اسرائیل شد.
🔴
فرمانده سنتکام پس از دیدار با مقامات بحرین و امارات، با رئیس ستاد ارتش اسرائیل، زمیر، و دیگر مقامات ارشد دیدار کرد. این سفر در بحبوحه مذاکرات آتش‌بس و فشار آمریکا بر اسرائیل برای ورود به مرحله بعدی طرح غزه انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/140627" target="_blank">📅 20:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140626">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae182bf78b.mp4?token=aXoHoJ5C7SDMgdsqvdPxmr_0EorDb-BXfwsW_fq3pSHIY5bB2Y9i5lYkcNikR5rul1CQ0rH5HNqX4gWxCbFEYtd9kpsWcJtioj5OrWc4CQNqc0gJ99BnIy1Jr8uOuDDQPVYMaFMRMhI6QmxXjaX3F5XquluDTiCk7XZWi7AzHl5Gaqg56aB1Egtsp8zV8imYHC6zbGMpImWEappCag1aGhZj63PADeT1K9jUn8doDfStXGf8h7I1ikBfbob9SIdBu1iHrw_LGBMB49MYBTEHv_h97HAJ17oknAwK-L-WCMZsKbYU1dCZTw5IEMzgDxe3IYNQGEiBFz43lyN46mAkYHRG1dqbuvSC4t1VklS9f1BamCrTM3xN00NCwTccBKj7sG4tjh2sPGnm3LPaGhYHkpkKBFyFK4H-R8nVELEMXGUE4aRM3QDSfeHyYGcAIPsIHEs3CDOGBkHiw4AnojqhaIjaVkkfLw8GAd0DBJhodQSVlEQ1ZtNi_hXeuS4fIkYhrtaxp2OJ8fVaumKS6R8PeZTx9gVT3LXRFLTlZg7AS7zHSpR90veM6tygshz9-w6Q3mHwnvbzfryAGaBwf6zn-RMHk4thb8X1ErpLqWqeHepUPKK81SqNUtN4OD2NsrcR8KaxPz72zQSgsnijbAanuSfRCdVn1Z5drFDJitMAcdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae182bf78b.mp4?token=aXoHoJ5C7SDMgdsqvdPxmr_0EorDb-BXfwsW_fq3pSHIY5bB2Y9i5lYkcNikR5rul1CQ0rH5HNqX4gWxCbFEYtd9kpsWcJtioj5OrWc4CQNqc0gJ99BnIy1Jr8uOuDDQPVYMaFMRMhI6QmxXjaX3F5XquluDTiCk7XZWi7AzHl5Gaqg56aB1Egtsp8zV8imYHC6zbGMpImWEappCag1aGhZj63PADeT1K9jUn8doDfStXGf8h7I1ikBfbob9SIdBu1iHrw_LGBMB49MYBTEHv_h97HAJ17oknAwK-L-WCMZsKbYU1dCZTw5IEMzgDxe3IYNQGEiBFz43lyN46mAkYHRG1dqbuvSC4t1VklS9f1BamCrTM3xN00NCwTccBKj7sG4tjh2sPGnm3LPaGhYHkpkKBFyFK4H-R8nVELEMXGUE4aRM3QDSfeHyYGcAIPsIHEs3CDOGBkHiw4AnojqhaIjaVkkfLw8GAd0DBJhodQSVlEQ1ZtNi_hXeuS4fIkYhrtaxp2OJ8fVaumKS6R8PeZTx9gVT3LXRFLTlZg7AS7zHSpR90veM6tygshz9-w6Q3mHwnvbzfryAGaBwf6zn-RMHk4thb8X1ErpLqWqeHepUPKK81SqNUtN4OD2NsrcR8KaxPz72zQSgsnijbAanuSfRCdVn1Z5drFDJitMAcdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال: آیا در توافق دفاعی ترکیه-عربستان-پاکستان اصل مشابهی با ماده ۵ ناتو وجود دارد؟
🔴
وزیر خارجه ترکیه، هاکان فیدان: از نظر فنی، این همان است. به همین دلیل است که شما یک پیمان امنیتی برقرار می‌کنید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/140626" target="_blank">📅 20:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140625">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVr-Z8NmtMhqfwlT9U7oOFI247khICmD34NRZ3k3fgXJd3nFvecrSJEpVOSuY8ra6iPqQiKd28n03jQ3Pnps4B8dB1nopEF3AkO88294SP3EuXoIuPm_DuGEqM7FtRE5ODwuIdrZiJtiSdPALgUrfViZaD9vXjcAjD5OwTQ47GTFjb6dTNBnrkabNLkvZt_nm8h43nsNfvz_IDdeKNmKvZbp1pAPEb0w11zs1lHCPoCH2CQjp10KxPg55Iffkj9Y-fKXZ0y7CsdJnx7NalCBXRSfJ-mdDjCPWlcW0rxBsx_NQkwwtSE30FKX9KTLPuNX3CH-d7OLx4-JRzqqC4FdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش رئیس کمیسیون امنیت ملی به توافق مکه: هیچ اشتباهی بی پاسخ نخواهد ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/140625" target="_blank">📅 20:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140624">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsLgRCNI5uJ4iXiV84D0XyuqkWWdYYVRjS7mylHkmmGM7pxNaYK7ukqmT9826wPHzsnMCdezyUCisGg7vNIuev1OqDcpaNyiSyEjY-oEPaNOQkmWXfCaswztZrPyjb_wMphyWsxyxef7_9tRMbgQmk4fAh3WtOs0ypVCpb-7icp8Z6BUFPvJe2k5RGm2-3LooKSML1x-nKzNk2-92tqa9_TYKyuTqsXTnaA2HJPKq0GO6S5bez_IPfUaWkqG1W6PA4_0b0tbvfgR9uSwleSgnmCe6-K39lHN0TSpWDybyjg4etDkuJa409bagGMfklDVh8IHQzzPLrdgndmbrctsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لحظاتی پیش حمله ارتش اسرائیل به منطقه ای در شهر المنصوری در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/140624" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140623">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9edd1e07f.mp4?token=Q7bRRkgSGVadmEDDXXjyNgaXrGmF4qHKUBH1IQBH4UPfYrqQ-joQ77Dc4B4bVU0p3jobveHaU-eLypT4YcY0vce2WPHI8VHn0jNd2j8lmkOqKYbDjsFdF61LuADgn7Rojeii6-bQ9LtbVz1mmG72-gGuAoMeCpy_0DxdWb0WJ7-eFyc5my8MdL0tVyirsj5ZRe3VRwNRZeUarOFobxrcMef3bh45QFAfRoaoz248hE4dBBx_piUysU2NENM2QAw3rjLFYv-ObqD3iq5MsZsT3fwK9dO-9O_HwUWiEzyL5AKmrM7fEFqGxwoQfdQHUmwiHstS_1jPz806sSen1ZDSxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9edd1e07f.mp4?token=Q7bRRkgSGVadmEDDXXjyNgaXrGmF4qHKUBH1IQBH4UPfYrqQ-joQ77Dc4B4bVU0p3jobveHaU-eLypT4YcY0vce2WPHI8VHn0jNd2j8lmkOqKYbDjsFdF61LuADgn7Rojeii6-bQ9LtbVz1mmG72-gGuAoMeCpy_0DxdWb0WJ7-eFyc5my8MdL0tVyirsj5ZRe3VRwNRZeUarOFobxrcMef3bh45QFAfRoaoz248hE4dBBx_piUysU2NENM2QAw3rjLFYv-ObqD3iq5MsZsT3fwK9dO-9O_HwUWiEzyL5AKmrM7fEFqGxwoQfdQHUmwiHstS_1jPz806sSen1ZDSxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایب رئیس‌مجلس
:
رهبری با وجود بی‌اعتمادی به آمریکا نظر رئیس‌جمهور پزشکیان رو برای تفاهم پذیرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/140623" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140622">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecee27ab5.mp4?token=qFir92o3eCR_2_Xcg4Eu_7o3J78bNcq-Yov4it5OzQPLJDL-PPHfSuEy1fzJlMj7RgvU3yQ8h0KKYk-LbzG2e063PVjT-SlddmnXhmTGZ54rGV39FuBSqjVLN8PPW09W0z3OXzJphZ9U3bbOtcrHtwOM_a8WaE30pNYPN7ZOyGhfkN1qEu9eOOFKpNOh8Wm9r_H_wItLRS2ME-eXN95zgT4kllCkEwOKQzBvZg5dqrX2Ti_D1RiYwYq7QKDvPX4_pme4DlJ0wvZkO3IN4FbsGWRjuylcbdppO0SieH6IF4u0qWRKtFd51y5y_kIHypE59v0-R0lUmSq638RW4Kncvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecee27ab5.mp4?token=qFir92o3eCR_2_Xcg4Eu_7o3J78bNcq-Yov4it5OzQPLJDL-PPHfSuEy1fzJlMj7RgvU3yQ8h0KKYk-LbzG2e063PVjT-SlddmnXhmTGZ54rGV39FuBSqjVLN8PPW09W0z3OXzJphZ9U3bbOtcrHtwOM_a8WaE30pNYPN7ZOyGhfkN1qEu9eOOFKpNOh8Wm9r_H_wItLRS2ME-eXN95zgT4kllCkEwOKQzBvZg5dqrX2Ti_D1RiYwYq7QKDvPX4_pme4DlJ0wvZkO3IN4FbsGWRjuylcbdppO0SieH6IF4u0qWRKtFd51y5y_kIHypE59v0-R0lUmSq638RW4Kncvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایب رئیس‌مجلس
:
رهبری با مذاکره مشکل نداشتن
🔴
فقط گفتن مذاکره باید طبق همون چارچوبی باشه که مشخص کردن، نه اینکه هر چیزی بخشی از اون کنار گذاشته بشه
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140622" target="_blank">📅 20:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140621">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3fc02684.mp4?token=qY8-a1bLCatfD3T6JNm4J1pKrnZFVwL11j4hboSyTnUXhTWN2ZJ6KfnPI0_nz1_kWh9o1qsS1MDjKh9vtlE71PJta9vqaemi7Rb5Fjy10SaXHFvdFV47SOmSY6MZ2CmysPVu50K4zN7G-OyNggw6NuKeP4rRyMpgr6lGIAwOciToL3TPB-W3dmb5E4ybwbpkoYP7plvAMFSVR5zfwULkkTtY6pt8nzIPzuh79SFqSc3X1kCl2D0rAQetLyfiZeOnjpuCPWPVnp0yJVxRf0_q9mV8MADfL97KJ2fAQ8CqEPsaq9K-JMMWMfoQV4xrKdeZZMO1UXOSNlEaG0q0ZM42YwLPF2w7qcseLK1t4wKEYLtT2Nfy6zQTpHqpTBWft-plGKYgQS52C9cKhQSQ1rwXcM6DePVuRfOrEmj-FSaTOdesdn8oLhk2DDaITXxIYmJbVzwKwZObwh7QHajIhlnzDubUqwdMlYjcBwt5yrdiPTKLwOY9ivZvx-CATEM9ySF5V3ib3g5Z7AxSWZqqQV0aw1FnLSy2eoHy7_exBobNKV6IE860kEfbV6vZ0PML7KkGaaY9AKvOwJW-TXJvKe3j7_a_553zGIQq1_8xWPh-pZBmS_3dPmzU8pDAzazwJ7NaaClZWOtjpku9caD4jzABp3gaapHg5lW3iTmNAj7__9k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3fc02684.mp4?token=qY8-a1bLCatfD3T6JNm4J1pKrnZFVwL11j4hboSyTnUXhTWN2ZJ6KfnPI0_nz1_kWh9o1qsS1MDjKh9vtlE71PJta9vqaemi7Rb5Fjy10SaXHFvdFV47SOmSY6MZ2CmysPVu50K4zN7G-OyNggw6NuKeP4rRyMpgr6lGIAwOciToL3TPB-W3dmb5E4ybwbpkoYP7plvAMFSVR5zfwULkkTtY6pt8nzIPzuh79SFqSc3X1kCl2D0rAQetLyfiZeOnjpuCPWPVnp0yJVxRf0_q9mV8MADfL97KJ2fAQ8CqEPsaq9K-JMMWMfoQV4xrKdeZZMO1UXOSNlEaG0q0ZM42YwLPF2w7qcseLK1t4wKEYLtT2Nfy6zQTpHqpTBWft-plGKYgQS52C9cKhQSQ1rwXcM6DePVuRfOrEmj-FSaTOdesdn8oLhk2DDaITXxIYmJbVzwKwZObwh7QHajIhlnzDubUqwdMlYjcBwt5yrdiPTKLwOY9ivZvx-CATEM9ySF5V3ib3g5Z7AxSWZqqQV0aw1FnLSy2eoHy7_exBobNKV6IE860kEfbV6vZ0PML7KkGaaY9AKvOwJW-TXJvKe3j7_a_553zGIQq1_8xWPh-pZBmS_3dPmzU8pDAzazwJ7NaaClZWOtjpku9caD4jzABp3gaapHg5lW3iTmNAj7__9k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایب رئیس‌مجلس
:
رهبری با پیام اخیرشون مشخص کردن که تصمیم‌گیری و اجرای کارها با دولت و مسئولانه و ایشون نقش نظارتی دارن
🔴
البته اگه لازم باشه می‌تونن وارد بشن و مسیر رو تغییر بدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140621" target="_blank">📅 20:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140620">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d6e7a00d.mp4?token=D8Vxa920E_yrXcRDi1GiFGB0Wf95IZvqip0aizXtSIGy2o6JqRzpUR-jn102p1upuTUtxpmrJUAawR1GuEAf6UweyYbGIvnEOJf49JjvP7hJJbJuu88j17hPqbnzpGBX40ok30ZaAxjpke8wBS0pv_aekYUPyEmVJWnPCtkNhp0mBmJJOYkociAkoljFNxZxmXXvP-so66VPIdOIbK7gIQKr0Fpi8BP5cWQtf0W7z5a7RhKy73URbE0Ip1J0yqkk6GwMZt515zOM_vYhOb_jtQQyWzUNlQYPOt57Of4a2eSb_4iGCd7ckGP3BCbpeXUQ2DPjUbpAhM_nxmDq_FAtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d6e7a00d.mp4?token=D8Vxa920E_yrXcRDi1GiFGB0Wf95IZvqip0aizXtSIGy2o6JqRzpUR-jn102p1upuTUtxpmrJUAawR1GuEAf6UweyYbGIvnEOJf49JjvP7hJJbJuu88j17hPqbnzpGBX40ok30ZaAxjpke8wBS0pv_aekYUPyEmVJWnPCtkNhp0mBmJJOYkociAkoljFNxZxmXXvP-so66VPIdOIbK7gIQKr0Fpi8BP5cWQtf0W7z5a7RhKy73URbE0Ip1J0yqkk6GwMZt515zOM_vYhOb_jtQQyWzUNlQYPOt57Of4a2eSb_4iGCd7ckGP3BCbpeXUQ2DPjUbpAhM_nxmDq_FAtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایب رئیس‌مجلس
:
عاشق مجلسی هستم که هر کسی حرف خودش رو بزنه و مردم هم در جریان صحبت‌ها قرار بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/140620" target="_blank">📅 20:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140619">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f0dcfa163.mp4?token=WHdvmfc2lBhBtsLD8tY8zORAiv0aM7a_hklsQ39qHdygxzBNjrK04rx3fnm22vcTeWlggseGU36k9qI00eT2BHe02c5M4C8RlZuSjlj_PSiO8GeL038DaDoSov-Uz-hbmmjznkfVgBwrZ2IJuW2pJ4EJk7UTFyxGgAv-poeewVrtE9uMp0CZWyVYMfpiHz9xOz-eolDN8CwBE6TUDaeljAGhdV2_5OJ1XQpZ6BsNkiFjRl26BTw22hbALIuVXV1FBRJ4AGl6kUK2SE3O1zBIasgAWnxr8oN44L1L8oTsj3zhsES7nqi1XhN4NaJqRSwklwpNN3eCGzvsxOcIZkt0kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f0dcfa163.mp4?token=WHdvmfc2lBhBtsLD8tY8zORAiv0aM7a_hklsQ39qHdygxzBNjrK04rx3fnm22vcTeWlggseGU36k9qI00eT2BHe02c5M4C8RlZuSjlj_PSiO8GeL038DaDoSov-Uz-hbmmjznkfVgBwrZ2IJuW2pJ4EJk7UTFyxGgAv-poeewVrtE9uMp0CZWyVYMfpiHz9xOz-eolDN8CwBE6TUDaeljAGhdV2_5OJ1XQpZ6BsNkiFjRl26BTw22hbALIuVXV1FBRJ4AGl6kUK2SE3O1zBIasgAWnxr8oN44L1L8oTsj3zhsES7nqi1XhN4NaJqRSwklwpNN3eCGzvsxOcIZkt0kIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نایب رئیس‌مجلس، بابایی
:
جلسه علنی مجلس رو شبانه برگزار کردیم
🔴
دشمن خبر داشت و شورای عالی امنیت ملی اون رو خیلی خطرناک می‌دونست
🔴
مجلس تو زمان آتش‌بس تعطیل نبود، فقط کار نظارتی انجام می‌داد و قانون‌گذاری نداشت
🔴
جلسات مجلس هم فعلاً به‌صورت وبیناری ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/140619" target="_blank">📅 20:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140618">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
لحظاتی پیش ۷ سوخت‌رسان از اسرائیل بلند شدند . به علاوه آنها ، ۲ فروند سوخت‌رسان KC-135 نیز در اسمان خلیج فارس و کشور های عربی حضور دارند
🔴
همزمان ۲ فروند هواپیمای ترابری C-17A نیز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/140618" target="_blank">📅 20:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140617">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سخنگوی ارتش: نظم ایرانی حاکم بر تنگهٔ هرمز غیرقابل بازگشت است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140617" target="_blank">📅 20:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140616">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزیر نفت عراق اعلام کرد که کشورش با ائتلافی از شرکت‌ها به رهبری یک شرکت آمریکایی برای احداث خط لوله انتقال نفت خام از بصره تا شمال عراق با ظرفیت ۲ میلیون بشکه در روز و هزینه برآوردی بالغ بر ۱۵ میلیارد دلار توافق کرده است.
🔴
باسم محمد خضیر گفت که شرکت آمریکایی «شورون» و شرکت قطری «تی‌ای‌وی‌یواس‌اس» اجرای این پروژه را برعهده خواهند گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/140616" target="_blank">📅 20:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140615">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت دفاع بلغارستان مدعی شد که تحلیل اولیه نشان می‌دهد پهپادی که امروز از رومانی وارد شد و منفجر شد، به احتمال زیاد یک پهپاد طعمه مایا بوده است، نوعی که به طور گسترده توسط نیروهای مسلح اوکراین استفاده می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/140615" target="_blank">📅 19:56 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140614">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ارتش لبنان اعلام کرد که سه سرباز در حین خنثی‌سازی مهمات منفجر نشده در شهر زواتر غربی در جنوب لبنان زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/140614" target="_blank">📅 19:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140613">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8fb1n3sgP-_yB0mySIhucDEvCnt_AC_bQtAt6kgcgsK07NReVWRmiVX0Lz_65Z4x-ghy6tOlPaYbSLjyOP6mnPzi0myI7ok6xICp0_IqKwZDw0QJwmDfwdZeEbowyGDAHPpa3atFigE3NgkFck1ZygVF40G36CrQGr1Np5MqQR5-32_8a4clgslX18Udl-q7ISkQauljeDLp3Qh0qKH6KFGTQgpOObMTv-mt1zeH2BHV-ycu8_shvpStbudBZurA3gS6esA1OUQHl_xxlIEtWSYcD-fUCMIKwbgpj3bKT51kTUT7mmSU0CwqfmoY9KQnZ8dpzaKWhhMY_1J-GiYzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سهمیه بنزین خودروهای تولید ۱۳۸۵ به قبل حذف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/alonews/140613" target="_blank">📅 19:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140612">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97b52ebc9d.mp4?token=rTn9GE06L6GpSK6W_axROKUyM-VDYpW5ljC5MorQASAuhErUcvszkV3HIUIzUGJNcqJnoHeIbViDFTXy-lldZfCU1oVZE-E_GeQBXgcSKAUArf0xm9Oh3qi4vHb2dVfWuyMH6iD_RPJN-Q1kl-qIKF5tpaFB2YwnWF7Z8D03sH0urlp_IpPtO2TMfexcRJwP0QmZ9S-5HyePN0AjXggjt-hyWMkwD7bjcSooBsyFNNkzUpoHhDo353DQkcKoTwtQP70vLnPMFnhmtsYIODYMqXUD7OpGba-LYswo41i5y43c1GvkDtYg8_dPu5tRPjiVAMY0A0EICM4jmDgTgliXKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97b52ebc9d.mp4?token=rTn9GE06L6GpSK6W_axROKUyM-VDYpW5ljC5MorQASAuhErUcvszkV3HIUIzUGJNcqJnoHeIbViDFTXy-lldZfCU1oVZE-E_GeQBXgcSKAUArf0xm9Oh3qi4vHb2dVfWuyMH6iD_RPJN-Q1kl-qIKF5tpaFB2YwnWF7Z8D03sH0urlp_IpPtO2TMfexcRJwP0QmZ9S-5HyePN0AjXggjt-hyWMkwD7bjcSooBsyFNNkzUpoHhDo353DQkcKoTwtQP70vLnPMFnhmtsYIODYMqXUD7OpGba-LYswo41i5y43c1GvkDtYg8_dPu5tRPjiVAMY0A0EICM4jmDgTgliXKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تست‌ هواپیمای هشدار زودهنگام و کنترل هوابرد ارتش چین همچنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/140612" target="_blank">📅 19:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140611">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
هانتر بایدن: سرطان جو بایدن به استخوان‌هایش سرایت کرده است
‏
🔴
پسر «جو بایدن» رئیس‌جمهور سابق آمریکا: سرطان پروستات جو بایدن به سایر قسمت‌های بدنش سرایت کرده و باعث درد او شده است. این بیماری بسیار دردناک و ناتوان‌کننده است.
‏
🔴
سرطان گسترش یافته به استخوان‌هایش رسیده و از بسیاری جهات او را بسیار دردناک و ناتوان کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/140611" target="_blank">📅 19:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140610">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
وزیر امور دیاسپورای اسرائیل، امیحای چیکلی، درباره بریتانیا: ما تحریم علیه تامی رابینسون را شکستیم، که او یکی از چهره‌های مهم و یکی از دوستان بزرگ ما در بریتانیا است.
🔴
ما نه تنها توسط مبارزه با اسلام رادیکال، بلکه همچنین توسط ارزش‌های مشترک به هم متصل هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140610" target="_blank">📅 19:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140609">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WUA72bu9BcjBGFOjD9Z-dGQqT1yr75Sy6aoEfk0Iqam9zRPBZkoqTzcRdyds8pXPyDfn7VaiajDx6kSCemwyv7sJbP21C0AsFpbo5_WFKfbpRXAHxBXIZl5PuJm4TbDu_VWk-rCMxBpjLcalDTTHRhAKh5kT7zT39sprnn2td8iVC3xOsbjyN3sjvtqEEoweD858WA64lT9MP0WgwLcGONrAWEwuCDrsb9RqjZoRoASywEcQuX9v9WfqjS0bCu-cLIjtej1D1ejcTsZfsTxtoqYRboHchl3zR8B1bz2BsOYC2MMnicjr6h3yRwnZmPRdctjM_KSQFf2k3mRmAOMgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عمان بدون اینکه سپاه پاسداران را مقصر بدونه برای اولین بار حملات به کشتی‌های عبوری از تنگه هرمز را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140609" target="_blank">📅 19:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140608">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
یه زن مازندرانی با وجود اینکه بچه هاش مستاجر بودن ۱٠میلیارد ارث بخشید به هلال احمر!
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140608" target="_blank">📅 19:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140607">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
مسرور بارزانی: اقلیم کردستان نمی‌خواهد به درگیری‌های منطقه‌ای کشیده شود و هیچ فشاری برای پیوستن به جنگ ایران به ما وارد نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/140607" target="_blank">📅 19:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140606">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پزشکیان‌: برخی افراد آب به آسیاب دشمن می‌ریزند
🔴
رئیس جمهور در نشست خبری گفت: برخی افراد، آگاهانه یا ناآگاهانه، با طرح مطالبی که از واقعیت فاصله دارد، آب به آسیاب دشمن می‌ریزند. بهتر است از این رویکرد پرهیز شود؛ زیرا ممکن است فردی اطلاعات کافی درباره یک موضوع نداشته باشد و بر اساس برداشت ناقص یا شنیده‌ها، مطلبی را منتشر کند که پیامدهای آن برای جامعه و کشور قابل توجه باشد.
🔴
هیچ ظلمی بالاتر از آن نیست که انسان چیزی را که نمی‌داند، تکذیب کند یا درباره موضوعی که نسبت به آن آگاهی ندارد، قضاوت و روایت نادرست ارائه دهد.
🔴
بخش قابل توجهی از مطالبی که در فضای عمومی منتشر می‌شود، ممکن است مبتنی بر شنیده‌ها و اطلاعات غیرواقعی باشد. بنابراین باید در اطلاع‌رسانی و تحلیل مسائل، به ویژه در موضوعات مرتبط با امنیت ملی و منافع کشور، دقت و مسئولیت‌پذیری بیشتری وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140606" target="_blank">📅 19:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140605">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2282e633c7.mp4?token=Cv5e0boduhnYPUDWcf-Vg0b7Lx1W5eOQHLWWnyyhQsohdbudXfGcBUqYwMBT8jE6XR5bslhfZyMCjsoKzId1EawsIMSe4z-s40A91Ix11WOAw4RbtFkL7zTvXTiQar4o7UHPp4mv_Ie5PocRZoRXPSuwQjDl8plcycDkgK8viuxOOXLzUmg3fKzxcm1AhtwKRs4k9SbmbgZbBb8_d6G68Xd1w-gHPkNHkU3rNxmzmjdSxsyBtwPMC-K_7zHRGWhLIxwCo49Ix6IsSOPqjWIsd84p9BOAIqi8O4Dblh7gGjg1REGeHh9TJjQgvb1YKE8YrcSeYCCIsEcjOYOrC9-odQo9pQHfCo7xMYO-knXQapMYCl9d0RaplMjRvfrSXWCY0ch6UgvhFvTxd19bmAW-JBs73V5h6TX1xAQnzYh9-Wm8cznHY89L3j2w7EG4F-5Xlj3HlSzw1NKbb1lQlVpMXrXHoe9T62-KBBevM0M-Y4kEvhER_5v3A_jzdx1eR8ZGGat7W_lAl9Tz_a4IqJOtRZJ4_aZUv-dNUbj3EHQahFyQr8PthppIFVcxzQl5icauDf8lE_et7xozeht-ryGDEKMAfpdI9iSwSwS-HXWqT7z4LHsB6FeVFd4ednSkPnBJHjq_jnPsZ10rg5ZpCoU3cHlq59RrMCuwysJfww6OmbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2282e633c7.mp4?token=Cv5e0boduhnYPUDWcf-Vg0b7Lx1W5eOQHLWWnyyhQsohdbudXfGcBUqYwMBT8jE6XR5bslhfZyMCjsoKzId1EawsIMSe4z-s40A91Ix11WOAw4RbtFkL7zTvXTiQar4o7UHPp4mv_Ie5PocRZoRXPSuwQjDl8plcycDkgK8viuxOOXLzUmg3fKzxcm1AhtwKRs4k9SbmbgZbBb8_d6G68Xd1w-gHPkNHkU3rNxmzmjdSxsyBtwPMC-K_7zHRGWhLIxwCo49Ix6IsSOPqjWIsd84p9BOAIqi8O4Dblh7gGjg1REGeHh9TJjQgvb1YKE8YrcSeYCCIsEcjOYOrC9-odQo9pQHfCo7xMYO-knXQapMYCl9d0RaplMjRvfrSXWCY0ch6UgvhFvTxd19bmAW-JBs73V5h6TX1xAQnzYh9-Wm8cznHY89L3j2w7EG4F-5Xlj3HlSzw1NKbb1lQlVpMXrXHoe9T62-KBBevM0M-Y4kEvhER_5v3A_jzdx1eR8ZGGat7W_lAl9Tz_a4IqJOtRZJ4_aZUv-dNUbj3EHQahFyQr8PthppIFVcxzQl5icauDf8lE_et7xozeht-ryGDEKMAfpdI9iSwSwS-HXWqT7z4LHsB6FeVFd4ednSkPnBJHjq_jnPsZ10rg5ZpCoU3cHlq59RrMCuwysJfww6OmbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمیخای چیکلی، وزیر دیاسپورای اسرائیل، درباره آلمان: در جاهایی مثل آلمان، با احزاب راست‌میانه مانند CDU روابط خوبی داریم.
🔴
اما حزب راست‌گرای آلترناتیو برای آلمان (AfD) مواضع روشنی درباره حماس، ایران و حزب‌الله اتخاذ نکرده است. بنابراین فعلاً پیشرفتی در روابط با آنها نداریم. صرفاً اینکه یک حزب راست‌گرا باشد به معنای رابطه خودکار با ما نیست. آنها باید موضعشان را در قبال حماس، ایران و حزب‌الله مشخص کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/140605" target="_blank">📅 19:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140604">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7105e037.mp4?token=APFqA3vDaMyUmQFjTE17f9TaLs9QJuo10IbbexC1K8zMwcqjSYCnUCIO_adCgRhCuPMqrzdJSAHjkp8gia5n_69Ezkh13BdOOoDW28fdAAnQZXgSm-uRQXT2bCNA6Otqafg_ctwOmhiFa8QCfjjBx-ylqr54byzVQ05utQZmFZQlakfVbJsnV9xyLaFy8FH1vxDFPx4qt5HN4Q4dQ3YsjQJz5Kc6usx2zOZFmTrAUMtVPKOqOeY-Yu9dNJOzvG96XtfKFwQnc2G4XCatP9iNuwVaIFqBWdoB8Dol2Hjio5dfFZQw8zmxI3dVLs_fGZxxFGobBsne2xxKCoDtapr9zjiGL5Ad8p-0-Fh-fY75LjpAx4WH-R6kSQLw82cDkX2B7NoQmV6PNRjKXsJ4VVIfVfX3SVJgAoZR8bi-jR6lp3VyteeZJRKV_Aj6W5FQcWoa-oDw8b-KzaPVYlOCTCShzGNPVrG01B82hS--K1WwhK6q_TngGthZlgyoHmN1ya50NKd0aSqJziEpfpnvSqThbi_jb7E3YJnKdetwuNIvZBehrWV3Mv7cJVo41sKoZrSMmq63g7c9F1At9P8jYM45bu019ysTiXih-Hl3B5SxSRrlgQyObYPejKGiR_f-zRZLDqfupbrQfc6Oe6iNSnI5OxZpNgWbKmkITDaSQGjitzk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7105e037.mp4?token=APFqA3vDaMyUmQFjTE17f9TaLs9QJuo10IbbexC1K8zMwcqjSYCnUCIO_adCgRhCuPMqrzdJSAHjkp8gia5n_69Ezkh13BdOOoDW28fdAAnQZXgSm-uRQXT2bCNA6Otqafg_ctwOmhiFa8QCfjjBx-ylqr54byzVQ05utQZmFZQlakfVbJsnV9xyLaFy8FH1vxDFPx4qt5HN4Q4dQ3YsjQJz5Kc6usx2zOZFmTrAUMtVPKOqOeY-Yu9dNJOzvG96XtfKFwQnc2G4XCatP9iNuwVaIFqBWdoB8Dol2Hjio5dfFZQw8zmxI3dVLs_fGZxxFGobBsne2xxKCoDtapr9zjiGL5Ad8p-0-Fh-fY75LjpAx4WH-R6kSQLw82cDkX2B7NoQmV6PNRjKXsJ4VVIfVfX3SVJgAoZR8bi-jR6lp3VyteeZJRKV_Aj6W5FQcWoa-oDw8b-KzaPVYlOCTCShzGNPVrG01B82hS--K1WwhK6q_TngGthZlgyoHmN1ya50NKd0aSqJziEpfpnvSqThbi_jb7E3YJnKdetwuNIvZBehrWV3Mv7cJVo41sKoZrSMmq63g7c9F1At9P8jYM45bu019ysTiXih-Hl3B5SxSRrlgQyObYPejKGiR_f-zRZLDqfupbrQfc6Oe6iNSnI5OxZpNgWbKmkITDaSQGjitzk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار اسکای: ترامپ می‌گوید شما پر از گوه (
💩
) هستید.
🔴
عبدل السید (کاندید مصری و چپ گرا و دموکرات سناتوری میشیگان در سنا): حداقل من اجازه نمی‌دهم  در وسط دفتر بیضی ریخته شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140604" target="_blank">📅 19:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140603">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
پزشکیان: استعفای ما مسئله‌ای نیست! هرکس می‌تواند کمک کند، به میدان بیاید؛ نه اینکه از کنار میدان بگوید لنگش کن!
🔴
رئیس جمهور در نشست خبری گفت: برای من، به‌عنوان یک ایرانی که در این کشور زندگی می‌کنم، قابل قبول نیست که پس از 48 سال وضعیت اقتصاد، صنعت، کشاورزی، آموزش و فرهنگ کشور به این شکل باشد و به جای حل مسائل، صرفاً افراد را تغییر داده باشیم.
🔴
استعفای ما مسئله‌ای نیست. من به قدرت نچسبیده‌ام و این‌گونه نیست که چون رئیس‌جمهور شده‌ام، تغییر کرده باشم. همان آدمی هستم که زمانی نماینده بودم و همان آدمی خواهم بود که اگر فردا هیچ‌کاره باشم.
🔴
تنها تفاوت این است که اکنون بار سنگین مسئولیت مشکلات این کشور بر عهده ماست و به همین دلیل می‌گوییم هرکس می‌تواند کمک کند، به میدان بیاید؛ نه اینکه از کنار میدان بگوید لنگش کن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/140603" target="_blank">📅 19:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140602">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
پزشکیان: تخریب تیم مذاکره‌کننده کشورمان بی‌انصافی است
🔴
نمی‌شود شعار بدهیم که می‌جنگیم، اما فردا در بازار همه‌چیز هم باشد و گرانی هم نباشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/140602" target="_blank">📅 19:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140601">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
به گزارش بلومبرگ، استیو ویتکاف، فرستاده ویژه دونالد ترامپ، و جرد کوشنر، داماد رئیس‌جمهور آمریکا، ممکن است طی هفت تا ۱۰ روز آینده به کی‌یف و مسکو سفر کنند.
🔴
این سفر احتمالی در چارچوب تحرکات تیم سیاست خارجی ترامپ برای پیگیری پرونده جنگ اوکراین و رایزنی با طرف‌های درگیر ارزیابی می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/140601" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140600">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نیویورک تایمز: ایران فهرستی از خواسته‌ها را ارائه کرد که این موضوع، امیدها را برای بازگشایی تنگه هرمز کمرنگ‌تر می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/140600" target="_blank">📅 18:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140599">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc383788bc.mp4?token=vsY103OSgFJP2SKJGbL40UZSaWafTmYDFJnqTRM5M8rR0y4Ug9NiIyZmyGrkfbcyde7e8O_hrpoJ-t5dZjr8Xr75IahEWjSEhbaXbocNs57ePpGikxFfpce0Sqe3CWbeeoxR09OYHK-sgcoWcNgYwIwhiNRU1PE1iCfpntef6fh1ckM2raCSw3xpUTfi6FPAFiMCeX1vw4Dk7eLbdIFZ-vEEweZ1HvxTaE_aP6jrKnFbVxK7z74AnhoCPMqnyZXo2QnWJKXSwTgvQTxTuM6QqrcX6ViRfJql6HCNk8VOMzG6tmEnvB0Qu7TCsRR6C1YxPKBZF0pkTHkFMKUTxQ7F6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc383788bc.mp4?token=vsY103OSgFJP2SKJGbL40UZSaWafTmYDFJnqTRM5M8rR0y4Ug9NiIyZmyGrkfbcyde7e8O_hrpoJ-t5dZjr8Xr75IahEWjSEhbaXbocNs57ePpGikxFfpce0Sqe3CWbeeoxR09OYHK-sgcoWcNgYwIwhiNRU1PE1iCfpntef6fh1ckM2raCSw3xpUTfi6FPAFiMCeX1vw4Dk7eLbdIFZ-vEEweZ1HvxTaE_aP6jrKnFbVxK7z74AnhoCPMqnyZXo2QnWJKXSwTgvQTxTuM6QqrcX6ViRfJql6HCNk8VOMzG6tmEnvB0Qu7TCsRR6C1YxPKBZF0pkTHkFMKUTxQ7F6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره عبدال السید
:
او نوعی فرد عجیب است. فکر می‌کنم این مرد دیوانه است و برای مردم میشیگان سناتور بسیار بدی خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/140599" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140598">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پزشکیان: برای همیشه که نمی‌توان جنگید؛ بالاخره باید آن را در نقطه‌ای به پایان رساند.
🔴
من معتقدم اکنون بهترین زمان برای توافق است؛ چرا که انسجام، قدرت و وحدت در کشور وجود دارد و تا جایی که من اطلاع دارم، ایران را در این جنگ و این درگیری، پیروز و مقتدر می‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/140598" target="_blank">📅 18:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140597">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e160691826.mp4?token=VPjsjRfpsCc3iPa2yZvqy8L48xmPTJdgcVMGhyE1fO8rhD1wv8YIHRnnkfRffJYOydSywUndhj_2zeNLpKOGoFw5YMO5Qe08NJ1OlIcrlaM9GEEkGivNRpzHBTy-HwrN6c29JY3fvRzOlmRhEaMvw44jqifxofa3AxnkVsR-UQOIUFewAhHcFflVny7QcK5xD4hLyf30TQLdPSDXlIdZAgu8QVW1FQEIExdmtjbaHEMPI-MQTUrLvdlX5gRZfXtdL8QuVlkViw7Wm7VnSkdzjtp8GCSvW7lHeEv5NiM5pQ5ljPx2maFPgD-Ki8OxCRInfEioIXEKgKRLRtPmLeo97phpGgV6tgHTysfeh4g2LuCbbZRL1dJs2UBgPfnnHQFP9ZuKxPiRfdOjxOI5pcXE6T9wG8sWlRmrTG4FXRzFymUBJoagjC4rMaRdClViGZubnPWy-Zvk1irvBDbWdHY5ks7BFbAVnTNlNTd2uzsUrELiPGaDlhSgzlqkKIXI-xn7YQv6trRFcNuKdwt6dRUU_i9UdsUmHQa0H5-oO4XLyKCGuaLR39oLxd2rpr9SrunzK1ofd0LC6ODeZxA1qBlUSQPdb0kJb_rV_9Zabpi3vWR_9lfzTU7ma94l_ybHWV9q_BN8Rn6DiImbEzt7ux1Ivngqw6grLU2Es4gbOzI54fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e160691826.mp4?token=VPjsjRfpsCc3iPa2yZvqy8L48xmPTJdgcVMGhyE1fO8rhD1wv8YIHRnnkfRffJYOydSywUndhj_2zeNLpKOGoFw5YMO5Qe08NJ1OlIcrlaM9GEEkGivNRpzHBTy-HwrN6c29JY3fvRzOlmRhEaMvw44jqifxofa3AxnkVsR-UQOIUFewAhHcFflVny7QcK5xD4hLyf30TQLdPSDXlIdZAgu8QVW1FQEIExdmtjbaHEMPI-MQTUrLvdlX5gRZfXtdL8QuVlkViw7Wm7VnSkdzjtp8GCSvW7lHeEv5NiM5pQ5ljPx2maFPgD-Ki8OxCRInfEioIXEKgKRLRtPmLeo97phpGgV6tgHTysfeh4g2LuCbbZRL1dJs2UBgPfnnHQFP9ZuKxPiRfdOjxOI5pcXE6T9wG8sWlRmrTG4FXRzFymUBJoagjC4rMaRdClViGZubnPWy-Zvk1irvBDbWdHY5ks7BFbAVnTNlNTd2uzsUrELiPGaDlhSgzlqkKIXI-xn7YQv6trRFcNuKdwt6dRUU_i9UdsUmHQa0H5-oO4XLyKCGuaLR39oLxd2rpr9SrunzK1ofd0LC6ODeZxA1qBlUSQPdb0kJb_rV_9Zabpi3vWR_9lfzTU7ma94l_ybHWV9q_BN8Rn6DiImbEzt7ux1Ivngqw6grLU2Es4gbOzI54fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس درباره عبدال السید: مشکل السید این است که ادعا می‌کند از مردم کارگر حمایت می‌کند، و با این حال با سیاست‌های دونالد ترامپ که به طور تحت‌اللفظی صنعت خودروسازی میشیگان را نجات داد، مخالفت کرده است.
🔴
او کسی نیست که بخواهد اقتصاد شکوفا داشته باشد که در آن کارگران خودروسازی و همه دیگران بتوانند در صورت تمایل، خانواده‌ای را با یک حقوق تأمین کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/140597" target="_blank">📅 18:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140596">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb34a4f6ba.mp4?token=qXO6OkfoiRYxbrhtGvULx8PNM_J7ysTFfwItjQDYfzXWaobjUbfucp93XfSHD2ylYc5byYytgqVNc0WHFI3Diu006UTmMvxQSX0fJM8NhqIgQ4DJlrupgGLH6gGn0PIL6tHUXdz7uIvDwmWi9hK0PfJziYzv_9RCvwU1nsHCXuIDdTCISssJhWJsTFVSj606O_gKat7OApsbMmIZMXme5bZpIE-8pjsHaxTB0kSnTZ4IP3j2Wik8y4SzplBM930XgEmQiodoM0ClCEVrJRF_UGPhBzukVfUheHaQqpkzK-OC0_l8Wt7G2F0UaVa33ac8IsKZzitOrR6hIierEURGcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb34a4f6ba.mp4?token=qXO6OkfoiRYxbrhtGvULx8PNM_J7ysTFfwItjQDYfzXWaobjUbfucp93XfSHD2ylYc5byYytgqVNc0WHFI3Diu006UTmMvxQSX0fJM8NhqIgQ4DJlrupgGLH6gGn0PIL6tHUXdz7uIvDwmWi9hK0PfJziYzv_9RCvwU1nsHCXuIDdTCISssJhWJsTFVSj606O_gKat7OApsbMmIZMXme5bZpIE-8pjsHaxTB0kSnTZ4IP3j2Wik8y4SzplBM930XgEmQiodoM0ClCEVrJRF_UGPhBzukVfUheHaQqpkzK-OC0_l8Wt7G2F0UaVa33ac8IsKZzitOrR6hIierEURGcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس : من لمس خدا را احساس کردم... خدا همیشه این پیام‌های کوچک را برای ما می‌فرستد.
🔴
لحظات ظریف زیادی وجود دارد که فکر می‌کنم خدا سعی دارد با ما صحبت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/140596" target="_blank">📅 18:48 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140595">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f75369c9d.mp4?token=bbozpVN9_F2ZfOIeXAcZbl5DDpg6YyBCdiCpNgmvm9vjb3MSn-0ziqQACDfpmoD-uLlYmEHEeby1MIkORTdI_UJI5o3kxNk3XvO6aySSurA3HCLY1sD4-q4UqWb2e6n2McQeKwpwhU0z1V3udvexsXiX50AwoZiHuuBxUg3o4YRsCZeWOotVRXETJhAyfl9i0fKYu3qC5Eghlge8oKlTvUXVyGqeOhQDgGYcIAtvZXy-rvhf7RihzBK2lWur-eUzX3Dpv-pNtPQ3eNVJ4vCmqqaENoJxTDeU3TVRtbrWQTcQQASlOhSFzvmv6s1hfCtY4awiXGpcVUWjXfe6gjTxAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f75369c9d.mp4?token=bbozpVN9_F2ZfOIeXAcZbl5DDpg6YyBCdiCpNgmvm9vjb3MSn-0ziqQACDfpmoD-uLlYmEHEeby1MIkORTdI_UJI5o3kxNk3XvO6aySSurA3HCLY1sD4-q4UqWb2e6n2McQeKwpwhU0z1V3udvexsXiX50AwoZiHuuBxUg3o4YRsCZeWOotVRXETJhAyfl9i0fKYu3qC5Eghlge8oKlTvUXVyGqeOhQDgGYcIAtvZXy-rvhf7RihzBK2lWur-eUzX3Dpv-pNtPQ3eNVJ4vCmqqaENoJxTDeU3TVRtbrWQTcQQASlOhSFzvmv6s1hfCtY4awiXGpcVUWjXfe6gjTxAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس
:
آن‌ها به شدت آسیب دیده‌اند. آن‌ها می‌خواهند این موضوع تمام شود.
🔴
سوال این است که آیا سیستم آن‌ها قادر است چیزهایی را که برای خوشحالی ما و احساس ما که آنچه را که نیاز داریم از این تعامل خاص به دست آورده‌ایم، فراهم کند یا خیر.
🔴
این هنوز باید تعیین شود، اما فکر می‌کنم ما در چند روز گذشته پیشرفت‌هایی داشته‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/140595" target="_blank">📅 18:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140594">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a6fdf0018.mp4?token=s1qnQK1Bhg54BK6igWeHtGCY2TY2MlRRYiAipN6m7E-zMYlilPyNBxv3rd9PfTJeivE1yEt2AlvFJ2d18HmHUya_aKQlo_EaPc7eJw6TaT3ZyQevHvscLje_Ml-TiXvo1HEpegmwQrWKh97SaWL3f_VSTPldyZREPhR2isTJpFboLTl5UrCkt06iJp2Me8Lzl7vwDg8qxhHNqmhA_16BdCJqxA0n3Y31jLvzC2_kk_-687d5-uBBwL1x22l61jZ1d7_OsARzusYoQtIlMEXkDTX-VbdNeV4xFMFBvwMPeQ-K90wqVfmeGFbrICLFdKr0PEdOh25_tlyh3P808BuAJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a6fdf0018.mp4?token=s1qnQK1Bhg54BK6igWeHtGCY2TY2MlRRYiAipN6m7E-zMYlilPyNBxv3rd9PfTJeivE1yEt2AlvFJ2d18HmHUya_aKQlo_EaPc7eJw6TaT3ZyQevHvscLje_Ml-TiXvo1HEpegmwQrWKh97SaWL3f_VSTPldyZREPhR2isTJpFboLTl5UrCkt06iJp2Me8Lzl7vwDg8qxhHNqmhA_16BdCJqxA0n3Y31jLvzC2_kk_-687d5-uBBwL1x22l61jZ1d7_OsARzusYoQtIlMEXkDTX-VbdNeV4xFMFBvwMPeQ-K90wqVfmeGFbrICLFdKr0PEdOh25_tlyh3P808BuAJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس:
آنچه در هفته گذشته یا حدود آن در جریان بوده، این است که ایرانیان و کشورهای خلیج فارس، به‌ویژه عمان، در حال گفتگو درباره چگونگی تضمین جریان ایمن ترافیک بوده‌اند.
تنها مشکل، البته، این است که ایرانیان در آغاز جنگ تعداد زیادی مین کاشته‌اند. بنابراین آنچه اکنون واقعاً در حال حل و فصل آن هستیم، چگونگی ایجاد یک طرح ترافیکی است تا کشتی‌هایی که عبور می‌کنند، بتوانند به‌صورت ایمن عبور کنند.
این موضوع شامل، البته، عملیات خنثی‌سازی مین است. همچنین شامل تعهدی از سوی ایرانیان است که به کشتی‌های تجاری شلیک نخواهند کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/140594" target="_blank">📅 18:44 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140593">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea692c7628.mp4?token=fxTGLwZ8kta5UAxdMhXulBjfClt0G8rNmLASOda-Ux_Q3FMjzlTNlCUdLuVxZ0tBEiX33dIcK2YDOGxE_EGoPsxjOaXRxzvhLjhl5p0QIVJMt7h8qg1sy_bGsIido3qB150Bioe6j50R6WFkWuaOFR-IqXCwyq_13g1Q--hjtrZuybDTG_Ku8A59HlL0699hK0wNs3Iys9cmRYGXzLY2-Xfk55rzQkDmfk3KjG-snmvAb011VE50bR92g8Zucqo2KNzLb9M02d5hdbtSoxGOOhGAMCGJwKnIKZr0MDJABH8QU_ARVTuHY56vxrueZ4gljQDOPuliSDqdXYBEHxopzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea692c7628.mp4?token=fxTGLwZ8kta5UAxdMhXulBjfClt0G8rNmLASOda-Ux_Q3FMjzlTNlCUdLuVxZ0tBEiX33dIcK2YDOGxE_EGoPsxjOaXRxzvhLjhl5p0QIVJMt7h8qg1sy_bGsIido3qB150Bioe6j50R6WFkWuaOFR-IqXCwyq_13g1Q--hjtrZuybDTG_Ku8A59HlL0699hK0wNs3Iys9cmRYGXzLY2-Xfk55rzQkDmfk3KjG-snmvAb011VE50bR92g8Zucqo2KNzLb9M02d5hdbtSoxGOOhGAMCGJwKnIKZr0MDJABH8QU_ARVTuHY56vxrueZ4gljQDOPuliSDqdXYBEHxopzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس:
انتظار ما این است که همان مقدار نفت و گازی که پیش از آغاز درگیری از خلیج فارس خارج می‌شد، مجدداً استخراج شود.
این همان چیزی است که ایرانیان به ما گفته‌اند که انجام خواهند داد. این همان چیزی است که ائتلاف کامل خلیج فارس نیز می‌خواهد انجام دهد. اما، می‌دانید، ما اعتماد نمی‌کنیم، بلکه تأیید می‌کنیم.
ما در واقع به کلمات افراد نگاه نمی‌کنیم، بلکه به اعمال آن‌ها می‌نگریم.
شما برخی افراد را در داخل سیستم ایران می‌بینید که درباره بستن تنگه صحبت می‌کنند. ایرانیان به ما گفته‌اند که هیچ برنامه‌ای برای بستن تنگه هرمز ندارند. اما باز هم، ما خواهیم دید که چه اقداماتی واقعاً رخ می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/140593" target="_blank">📅 18:42 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140592">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec574036c0.mp4?token=qGrKiAJKNMUeJ75Wm82-WaSlEAne0K_HJrPBW6UIX4SDdx_ktSxZU4XJs1ArPRXRwSzSxz_Igii3nFqUf3OGOcH1R9jbHxMuRd4DuziLiCErJOcbplO0rBj1fTejRfGIJJZxNWALhTpCETL0c8CJnofQRYBwbv1Jq7sBGDKQP0gbuJRgUj9aZ0NEl0S1iQGV7lF5V5_hTv6M7RmWds5n92f1-BKfhnvECf-s8GLJ24d1p-_bPxiMnqCwDgUIg22vVvwyu6rYL3luUkzv8bzDvWk8zZSxRIT5atoL3U7hJ_H-AgVA76oSPjmM1v6kpmylKpo_uESEuljnnr7byFPYIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec574036c0.mp4?token=qGrKiAJKNMUeJ75Wm82-WaSlEAne0K_HJrPBW6UIX4SDdx_ktSxZU4XJs1ArPRXRwSzSxz_Igii3nFqUf3OGOcH1R9jbHxMuRd4DuziLiCErJOcbplO0rBj1fTejRfGIJJZxNWALhTpCETL0c8CJnofQRYBwbv1Jq7sBGDKQP0gbuJRgUj9aZ0NEl0S1iQGV7lF5V5_hTv6M7RmWds5n92f1-BKfhnvECf-s8GLJ24d1p-_bPxiMnqCwDgUIg22vVvwyu6rYL3luUkzv8bzDvWk8zZSxRIT5atoL3U7hJ_H-AgVA76oSPjmM1v6kpmylKpo_uESEuljnnr7byFPYIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
معاون رئیس‌جمهور جی‌دی ونس در مورد جمهوري اسلامي ایران:
ما واقعاً در میانه بازی هستیم. این موضوع تمام نشده است.
به وضوح در ابتدای کار نیستیم. ما در میانه بازی هستیم و در حال به کارگیری طیف وسیعی از ابزارها، دیپلماتیک، اقتصادی و نظامی هستیم تا اطمینان حاصل کنیم که بهترین نتیجه را برای مردم آمریکایی به دست می‌آوریم.
من نسبتاً مطمئنم که به آنجا خواهیم رسید، اما هنوز کمی در میانه بازی هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/140592" target="_blank">📅 18:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140591">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3nZaQdBfSvgmED6tj-_Dgp8U1qWgyfPOMOX73pRk1xz5gmBcfGYSXe5BswrzbzO8_1F3DJfVzybTzpAiC3ik8m3xyMXjSUbjOSf5pYk7IyPvTpOYTSJOfZaFznff_3PKIrLs8rovbRn2JIBusTJYbSf0deMYneQ2onyHWCVVw5yJvYUyXRJGWLYpktyJpXSFAKVu_GTY7eqBjGB-tedQLZVUnSgMTpmRYbuplmJuiKxg41rg_9qiRVAYgfvukJaNQFyIeyu6zHdjzLihdQl0872Ka70ry5FidBzdXQls-D9L9_DCte33KUBQF790grqaoyIcg_sgywE4Ro1gPLVtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روزنامه سازندگی روز شنبه به نقل از یک منبع آگاه اعلام کرد که
مسعود پزشکیان،
رئیس‌جمهور،
با استعفای محمدباقر ذوالقدر
، دبیر شورای عالی امنیت ملی،
مخالفت کرده است.
در روزهای اخیر برخی رسانه‌ها از کناره‌گیری ذوالقدر و انتصاب محسن رضایی به عنوان دبیر جدید شورای عالی امنیت ملی خبر داده بودند.
این روزنامه که ارگان رسانه‌ای حزب کارگزارن سازندگی است، در گزارش خود به نقل از منبع آگاه نوشته خبر استعفای دبیر این شورا «صحت ندارد» و پزشکیان به او گفته است که با «قوت و قدرت» به کارش ادامه دهد.
با این حال سازندگی تأیید کرده که ذوالقدر پیش‌تر استعفای خود را ارائه کرده بود «اما این استعفا با مخالفت مسعود پزشکیان روبه‌رو شد و در نتیجه او همچنان در سمت خود باقی ماند».
محمدباقر ذوالقدر در پی کشته شدن علی لاریجانی در اسفند ماه گذشته در جریان حملات آمریکا و اسرائیل، به عنوان دبیر شورای عالی امنیت ملی منصوب شده بود.
علاوه بر برخی رسانه‌ها، محمدباقر خرازی، روحانی تندرو نزدیک به بیت علی خامنه‌ای، نیز هفته گذشته در یک سخنرانی خبر استعفای ذوالقدر و جایگزین شدن محسن رضایی را اعلام کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/140591" target="_blank">📅 18:29 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140590">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82fcd24626.mp4?token=jV3Yg7yrcFCXy4JRDc3nc5T-pj4kndwEl4ngmXV2ajUKz6h-URAJjIDLVVy2svbtQvdLi2NWgzYZCD-DjY7Cfvar6maWoLE5lm_xPT97TsAkzJPDHvI3Npkz3KOoXANySQfcNwRnfSVQk4K7qgCZhjIqYZ5O4sBs60I01iSWGsg8D9TxXW2iWhUsQ2LTt9q58-04ywnsEm_NaA6aPtZEoEbO2Xi5bN70DeXQDcc77ykZwjkphtDVfEVmfsR9FtdpDzgzgByWTemb6q8rkoi372RgYFD4DuIL5EDxORggSVdMtD3JbHki17psi7Qi_s9ptr6UDr0KB7cGGN_cB_07XYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82fcd24626.mp4?token=jV3Yg7yrcFCXy4JRDc3nc5T-pj4kndwEl4ngmXV2ajUKz6h-URAJjIDLVVy2svbtQvdLi2NWgzYZCD-DjY7Cfvar6maWoLE5lm_xPT97TsAkzJPDHvI3Npkz3KOoXANySQfcNwRnfSVQk4K7qgCZhjIqYZ5O4sBs60I01iSWGsg8D9TxXW2iWhUsQ2LTt9q58-04ywnsEm_NaA6aPtZEoEbO2Xi5bN70DeXQDcc77ykZwjkphtDVfEVmfsR9FtdpDzgzgByWTemb6q8rkoi372RgYFD4DuIL5EDxORggSVdMtD3JbHki17psi7Qi_s9ptr6UDr0KB7cGGN_cB_07XYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس:
ایران به ما گفته برای عبور از تنگه هرمز عوارض نخواهد گرفت
🔴
جی‌دی ونس، معاون رئیس‌جمهور آمریکا، اعلام کرد انتظار واشنگتن این است که میزان انتقال نفت و گاز از خلیج فارس به سطح پیش از آغاز درگیری‌ها بازگردد؛ موضوعی که به گفته او، مقام‌های ایرانی نیز در گفت‌وگوها بر آن تأکید کرده‌اند.
🔴
ونس در واکنش به اظهارات برخی چهره‌ها در داخل ایران درباره دریافت عوارض از کشتی‌های عبوری گفت:
«مذاکراه کنندگان ایران  به ما گفته‌اند هیچ برنامه‌ای برای دریافت عوارض یا دیگر مبالغ از تنگه هرمز ندارند.»
🔴
او با این حال تأکید کرد واشنگتن صرفاً به این وعده اعتماد نخواهد کرد و عملکرد واقعی تهران را زیر نظر می‌گیرد: «ما اعتماد نمی‌کنیم؛ راستی‌آزمایی می‌کنیم. به حرف‌ها نگاه نمی‌کنیم، به اقدامات نگاه می‌کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/140590" target="_blank">📅 18:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140589">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0r0CFCPya7yTGoYFQW6wxEg7DoipifioG7ZEKKi8Hqf0xclWBT4SmtlPawNB2vRZRw_HzbM-AqME4iDz2gXDSTGVaaEfidIEXfmX_3ME499dnIZH5rpzrV2i8Wc4xCl4-r6AYxxoaqFsIReBgv0txCigy40Lm9a2avmj_4PPf88VcYjXSCRYc-dzVZt4QJYV_blVqukmmX5q8wrb1s92QAl_tBIjW2VGkw5ymOdBLH4qEtHXwKsM2JyEr-8dc_BgXwEm3Sx4qZlH_O-EYG1vfMvI6h7faoJz6BZp1lfTpDpE0rUQuoq4r7yBAUfSf0pqmS44n0wDoOq_OpY0dCt-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت بعضی از خونه های بالاشهر تهران از هزار میلیارد تومن هم عبور کرده.
۱۳۰۰ میلیارد یا ۱۷۰۰ میلیارد رو حتی نمیتونم تصور کنم چقدره‌؛ چه برسه بخوام‌ بهش برسم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/alonews/140589" target="_blank">📅 17:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140588">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfXGuYyNqms1pGFBAMNXY0GQj1fV_Xbn3wVjfVWOTRHtV25gvKs99gU5vGCdgI6KUDQcCITNv2Toqs6JEiEZ_Dms5MW2G2jE1xxmtrJCZt7XmdRjbhWqyKqvrPZ9PiTtH-NqdrounzCa7ISEF6l7Q2Jxt50GYlvEIv8dZ4p_1fy2GIHkyXdvg44xyr3Cd4kU5ZUJ1e9Qli9LBrtABAvfDfBNjjwRfZTJ18wBMeT6TqTX3ym7AjW95d0dq3yXOY2qBsGGXpJGX9sqkjTBZv8f3HY_JqpBwMH5JdvyvkVx7mR1t1prZ9r0YVd8HqWi47spYnaMcaAVhNpt6FlU6RUjqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک بمب‌افکن B-1B آمریکایی، بریتانیا را در مسیر بازگشت به ایالات متحده ترک می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/140588" target="_blank">📅 17:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140587">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=shvh0HSdUrJ4H873-zygjiHZ8saxm6uijLgATSfuopXf8NbqAjoIUlVmrjlWvYh-vpDOAqDUwWTSGs76JIlTcAGa9L4h6BOFU-4UoTOkjMYQXQ96ZNRFz7a_u1wwpU8sVmXj3sz1ByINAtezI4JpyIlPz-1FbY1RwJT2Yeqh1ino2H96c9iDXuau7t3PcNUazfJ2ShdTF-W8hkw28IBIy30BE5NMRXlQPg61ka4ORoigj4cPimhBoOrN0Vvyv-c2T47N5Hgh2qZv3jfWMpZjJwi5hyH1JiG_y5fGrkNTyYlNuzvs1Y4x2SvRjWV3JdDoVGHzEJG56WR06QjZuTVR8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9bc484b9d.mp4?token=shvh0HSdUrJ4H873-zygjiHZ8saxm6uijLgATSfuopXf8NbqAjoIUlVmrjlWvYh-vpDOAqDUwWTSGs76JIlTcAGa9L4h6BOFU-4UoTOkjMYQXQ96ZNRFz7a_u1wwpU8sVmXj3sz1ByINAtezI4JpyIlPz-1FbY1RwJT2Yeqh1ino2H96c9iDXuau7t3PcNUazfJ2ShdTF-W8hkw28IBIy30BE5NMRXlQPg61ka4ORoigj4cPimhBoOrN0Vvyv-c2T47N5Hgh2qZv3jfWMpZjJwi5hyH1JiG_y5fGrkNTyYlNuzvs1Y4x2SvRjWV3JdDoVGHzEJG56WR06QjZuTVR8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادمهر عقیلی، قطعه‌ی معروفِ گل یاس(برای حضرت زهرا) از البوم مسافر رو که سال 1377 منتشر کرده بود، بعد از 28 سال دوباره بازخوانی و تو اینستاگرام منتشر کرد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/140587" target="_blank">📅 17:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140586">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فالح الزیدی، نخست وزیر عراق: ۳۰ سپتامبر آخرین مهلت خروج نیروهای ائتلاف از عراق است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/140586" target="_blank">📅 17:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140585">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmNxGVnyNdJsAtAbjxnLuUxzy4jl_8cMyiEX7gX6QRS-HEjLb5J1uJEcIqBrNwxKA_PNTtqnYQ0_aXrWIXj21PWS2_XFpSVW9o3jX9wo7H-2DptVMs_XyywaScL1KJ9c_4sCCsLChd9-7n-RY88WEylKk5jUKrN8Tb0Cs4hdNIO1A-n22g3P6pCjrzASdsfxuYmA869Cng0Pw9-MtZAKrl76mILxxkOEmK_pwpBdfwpzmGO6lY2aaUfdmba_Kn22WYo2E09IRIXzmwyfOnCStbEdzSByupv_pBRyk4PMyGbBPJKbGEMZSjbfW_5x6KDqe4DQhPbj_JBD47YhD7gK_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق برخی گزارشات تایید نشده چند نفر از عوامل قتل حمیدرضا رجب زاده بازداشت شده‌اند
🔴
حمیدرضا رجب زاده مدتی قبل ربوده شده بود و به شکل غیرانسانی به قتل رسیده بود و فیلم این جنایت در سطح مجازی پخش شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/140585" target="_blank">📅 17:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140584">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
ذوالقدر دبیر شورای عالی امنیت ملی:  تا آمریکا رفتارش را تصحیح نکند، تنگه هرمز باز نخواهد شد.
🔴
شورای عالی امنیت ملی هرگز کوتاه نخواهد آمد؛ چه در جنگ و چه در مذاکره
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/140584" target="_blank">📅 17:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140583">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNY_SIkMessTBrPCP8x7CTYWq7ivqZgAr0vL9f-PU4Bv4Kz5lCHMT3p8Y9wzyf4XvDAka8LOwlnxIDWWBRJRGB-8Fi_-Xbf2v_DlW1F0pkwOAluYQE8Nbc2P7mzbDmmUDUbR5v8UEArjR0zzqo-Ij9eJZx_ABIpl09Z4t_7r3KiySd0pohfPU1u7V_mfMvgeDFt_xNKUNwsaLFhigg5hh6WTAk6rzVPFL91YfeGhiJENOOVkk2UyHfowMxRLzXkhBWtKRzzTP508qBzhzrx2b-EoiG5-74TIFU5YkO4RoHqjyU12c3PPn2jYMU3WEwI74uZQpbeoUee5zIlKxNkEIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/140583" target="_blank">📅 16:59 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140579">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی 9500
ممبر از کایی ۵۰.۰۰۰
⚡️
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/140579" target="_blank">📅 16:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140578">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
بی‌بی‌سی: عربستان سعودی، خرید شرکت بزرگ بازی‌های ویدیویی، الکترونیک آرتز (EA) به ارزش ۵۵ میلیارد دلار را به پایان رساند. این اقدام باعث می‌شود که شرکت منتشرکننده بازی‌هایی مانند Battlefield، EA Sports FC، The Sims، Apex Legends، Mass Effect و Need for Speed، پس از ۳۶ سال فعالیت به عنوان یک شرکت سهامی عام، به یک شرکت خصوصی تبدیل شود.
🔴
این معامله همچنین نگرانی‌هایی را در میان منتقدان در مورد نفوذ رو به رشد عربستان سعودی در صنعت بازی ایجاد کرده است. سوالاتی در مورد احتمال سانسور، مسیر خلاقانه آینده فرنچایزهای EA و استفاده این کشور از سرمایه‌گذاری‌های بزرگ در صنعت سرگرمی برای بهبود تصویر بین‌المللی خود، با وجود سابقه ضعیف آن در زمینه حقوق بشر، مطرح شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/alonews/140578" target="_blank">📅 16:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140577">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5cc4ef375.mp4?token=gjQN559eI71oMfa1QmX7P_Sl10bsvtqOXvhM4TRtW5SLUJ5c1tYpin-G9cdAbIBlyRuLeOXZHjxOpEx6UDHZnG-DiBD-_dLMKmWUrxMgmAtC91Fu2UNP6M7Z-eG2ZRzIIZw15hbZRGaqa1Yca1pLnoiCeBTQbsYgVPYS2fsGWNaUWTyRWlsKvtpcjkjp0OEF9D_G9HeYUodWwzFrwRWBoHQQia5IGaW8lM--JtUg4jgKSuafXMO1qP7eDFQecGdJXD6LsLtIcvzvafCqd1hRqIrw3tZis21yEEV0LMEvkXsF2Xnle5M1TmUCFWxloEqdnpWmwA1Lb8hLL--AloyL7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5cc4ef375.mp4?token=gjQN559eI71oMfa1QmX7P_Sl10bsvtqOXvhM4TRtW5SLUJ5c1tYpin-G9cdAbIBlyRuLeOXZHjxOpEx6UDHZnG-DiBD-_dLMKmWUrxMgmAtC91Fu2UNP6M7Z-eG2ZRzIIZw15hbZRGaqa1Yca1pLnoiCeBTQbsYgVPYS2fsGWNaUWTyRWlsKvtpcjkjp0OEF9D_G9HeYUodWwzFrwRWBoHQQia5IGaW8lM--JtUg4jgKSuafXMO1qP7eDFQecGdJXD6LsLtIcvzvafCqd1hRqIrw3tZis21yEEV0LMEvkXsF2Xnle5M1TmUCFWxloEqdnpWmwA1Lb8hLL--AloyL7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله‌ توپخانه‌ای اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/140577" target="_blank">📅 16:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140576">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uj449LwGSxP4n2NM9tRDW4SSdZ6mlrcubDDlkE2rP9GJCzKT3rQTmbXRQl5OCLcP0Mz-fITuEPkgKYO8u8kfzPrgm-HV--coBoB-OFxTjSLlhZX4xE1sZi9S5_MDxOf_mAoM-UYn0A_pg5bzIVbmpdHeMzJ_nPMbIyNWRWulDTrSeud9jkSq0YBwUJBMGlLOcrYwbo6X0Ccl32t5KF4VcOGZbGYFEDJVwbVpTiH-PrNyqPYeXhual7cu-3Ib4MFlw7JvBwq7G2HT07eMOfylDbbUGiA3TVlXVvqak5xpRR4XG9heO5Bz8n3xb5VKRMSs5OqLXILYugP_9t8KelKI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر سقوط قدرت خرید: قیمت یک جک؛ معادل ۱۸ سال حقوق یک کارگر
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/140576" target="_blank">📅 16:19 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140575">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7edca33567.mp4?token=HNUzTc8O3CPySQQ0_xwR8kjhrWomx8ZKYYsfgCkYisWuv2mBGPKV7BAsxcEYAvJTgsUJQ19gg6bCUNy9EMS4mtUEUDEFkSwvseUi62OSij4lDnSCXg0HpZEhCjxp0HNPT4ybwptZ2J4E8gi26W48qKoocs8uda2PxTy1dmgFiUnwx-wA8tSNguYctcTlOlVgfpuI5IVaVC3KMhfkUZo-pSFJq_OeALnxplPHsyAvx1GwmF8BoKz5pC_AMyKihEoOGRVLchsq5aBFxSxrfDPhPYi0DRkDrkFthdG7GnofJ6_sI_3727pAE-FnmQSBoJqjbKHre_6QBrDIV-9qYrcV2l-P3KnL16ZbOcQ0HOWE9PX8Yfg5xW9e2ISkDv7DfejeDfUMU9qKRULCcCp9kys4CLGuuG3kNTZUbIaJtfTSr2If50CYZCluCJMkgO8ItCbk6oy9EPA5Rin6UWCKdmh3lrd7lFshDoUsTbpWht_Ytgk-5JBPR34jJfnFYrIqwrRD7le7gNZHCHXCFWHrobx1dtbFkuWtXo8FSon2SH2xTz-i1y__DvZMgaT0uCGF4LSHqLJSTUxhND4MA4djhmpQu5ll6RVwAr8ftqOVLbVsGAhlERqcU21Z-zzk1d31Z5AYMtjI-VVkkJbCp024kH2V0vH0JgfDdKrbgJYtdyXhi2I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7edca33567.mp4?token=HNUzTc8O3CPySQQ0_xwR8kjhrWomx8ZKYYsfgCkYisWuv2mBGPKV7BAsxcEYAvJTgsUJQ19gg6bCUNy9EMS4mtUEUDEFkSwvseUi62OSij4lDnSCXg0HpZEhCjxp0HNPT4ybwptZ2J4E8gi26W48qKoocs8uda2PxTy1dmgFiUnwx-wA8tSNguYctcTlOlVgfpuI5IVaVC3KMhfkUZo-pSFJq_OeALnxplPHsyAvx1GwmF8BoKz5pC_AMyKihEoOGRVLchsq5aBFxSxrfDPhPYi0DRkDrkFthdG7GnofJ6_sI_3727pAE-FnmQSBoJqjbKHre_6QBrDIV-9qYrcV2l-P3KnL16ZbOcQ0HOWE9PX8Yfg5xW9e2ISkDv7DfejeDfUMU9qKRULCcCp9kys4CLGuuG3kNTZUbIaJtfTSr2If50CYZCluCJMkgO8ItCbk6oy9EPA5Rin6UWCKdmh3lrd7lFshDoUsTbpWht_Ytgk-5JBPR34jJfnFYrIqwrRD7le7gNZHCHXCFWHrobx1dtbFkuWtXo8FSon2SH2xTz-i1y__DvZMgaT0uCGF4LSHqLJSTUxhND4MA4djhmpQu5ll6RVwAr8ftqOVLbVsGAhlERqcU21Z-zzk1d31Z5AYMtjI-VVkkJbCp024kH2V0vH0JgfDdKrbgJYtdyXhi2I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو آمل یک شخص فضول رفته به یکی گیر داده که چرا پوششت اینه
🔴
اما فارغ از بحث پوشش طرف، نکته جالب اینجاست که این شخص به اصطلاح آمر معروف به چه اجازه‌ای از ناموس مردم فیلم میگیره و پخش میکنه؟
🔴
این زن فضول سپس میگوید من اطلاعاتی هستم و پدرتو درمیارم و حسابی تهدید میکند و قانون هم طبق معمول مشمول این اشخاص فضول و بد دهن نمیشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/140575" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140574">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H522K9NQcConrHEWk083YMA1uusHfFVz_QRYpTuLF2qlaxagYw7tDQWt9QY2Nmbok1avW4foURE4XDMEC0fHtpDPNvSYnhkDc4hpCNZzNxc_QyBUb46-KUvr65Cykk6xxs9WZDV3MLPk0D1mgnRYdv7l3nO9Lq3veaUoDdcD2g9VNnZkPAagkRVnqqQvYIJ-0vuSjD3bfMRuz4mc5PDe8hYfMWCGiEgA8H2zveVSIU6znVbG1_g8pRc8SEwEKvLap7PJYnki1UNYltMewis3h5dWORuRri20urE4Sp7Od6f9pvQnJJIijs6zpPeS3nQbWjjvLK7NX5Je6scT68SGmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیلاری کلینتون: کاخ سفید ترامپ شبیه کاخ‌های صدام در زمان سقوط است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/alonews/140574" target="_blank">📅 15:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140573">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
وزارت امور خارجه عربستان:
ما ایران را مسئول عواقب اتفاقات آتی در خاورمیانه می‌دانیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/140573" target="_blank">📅 15:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140572">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc109ca33f.mp4?token=ADdwE3cV5XIVWEPqomgOCC51A-_HXwHkhTWW-IqsZWpnPB00NHF6Ig_ATfPVmguCZXNY4A3XkqZTDvr395qmF4e1fXi_H9NlLA3J0x7TBf4Q20Jc2YpBnjzGAiUMnlm6y7j9GV6VtM3r22eEfI0gHQjwuPWEZx7VjZgvoMvf3gGF4yUtDECeZKd1uBYYWGN3pFzFzq4pwKdeRihKkokrnmCx4NCnjaWWX6xErfUt5tWrBDHYOE8HM120sRmlWByK0IygfqnAd174qk9MUsRTzPHqXnn5z4T_PxoGZxF1d3bNfamgSROQaaluCOctaEripS3VmoCzbFvEAg9KUd3NIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc109ca33f.mp4?token=ADdwE3cV5XIVWEPqomgOCC51A-_HXwHkhTWW-IqsZWpnPB00NHF6Ig_ATfPVmguCZXNY4A3XkqZTDvr395qmF4e1fXi_H9NlLA3J0x7TBf4Q20Jc2YpBnjzGAiUMnlm6y7j9GV6VtM3r22eEfI0gHQjwuPWEZx7VjZgvoMvf3gGF4yUtDECeZKd1uBYYWGN3pFzFzq4pwKdeRihKkokrnmCx4NCnjaWWX6xErfUt5tWrBDHYOE8HM120sRmlWByK0IygfqnAd174qk9MUsRTzPHqXnn5z4T_PxoGZxF1d3bNfamgSROQaaluCOctaEripS3VmoCzbFvEAg9KUd3NIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اجرای حرکت میشِنِری توسط یکی از جان فدا‌ها و اعلام آمادگی جهت جنگ با دشمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/alonews/140572" target="_blank">📅 15:28 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
