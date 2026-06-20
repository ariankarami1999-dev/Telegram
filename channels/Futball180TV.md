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
<img src="https://cdn5.telesco.pe/file/KPm2JpNcySCLoD792yKLp5hFKu9bjs53jR6nvetrIXqnvFBi03zUAEYu-HrE9Msxl-bmuepnmKE1W5P-CL_Mg3-L-EqH_O7W-bs2-A4rLf0EKQm3ivnftoDWvurjF80Xu8oGeKfN9z9ktzXilYBJR2QZsllciy3capovzqFXXFsBmdX-ESTQfwpG21nn5QXOIsOZv8jqhc9fWS2BIA2XL0L1Cq2ELmpM_D7MEn9Sl8zRsaQhhOj-WXfoxp4mUx6YVnWSPs7E5aYJRuCu_9PzQKa7vF9S-7YAsBvA73am8GbeqqvAexA8cGGoKvwlultsbwn8DFBi6Pk7BpM1g9v4hw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 676K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-30 11:47:27</div>
<hr>

<div class="tg-post" id="msg-94640">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4XQrH3Jxc4k7_y4WAe13EJL4IJVA52zSB6ZlNvhDV_P9nlxk0UoTlIGApM1hQsoIDpyhSgsSUPbC1tMYI2Y_Xkd1auOk4SAD62H_Ja2nDW2EEtBuIRtBYe7ylHX1fgytZCjBeKLb1kJD3Ny08_vjmwNFpeYUeIDFk1kRLLBhKKTzK9GCYvyob6cwfEmqdc7SJ2PvwGQ__WMhnQSja3cYmuQG8GmZdiwoeNOCjB7ASddpUYhoYl5_9AvVTodMtgplLNbeHFubAMVSS8Ewcu7UHycEQtID0SCT9sEbiAI0QQWrWVMtTN45COQd59Z_7FtD87fQgfAFhgJTndO8sQ_9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
🏆
تیم‌هایی که تاکنون در جام جهانی ۲۰۲۶ موفق به گلزنی نشده‌اند:
🇹🇷
ترکیه — ۰ گل
🇪🇸
اسپانیا — ۰ گل
🇩🇿
الجزایر — ۰ گل
🇭🇹
هائیتی — ۰ گل
🇪🇨
اکوادور — ۰ گل
🇨🇻
کیپ ورد — ۰ گل
🇵🇦
پاناما — ۰ گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/94640" target="_blank">📅 11:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94639">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6bcd7de2.mp4?token=P4eFAaps_o3iaZg2EbQLXjsJlx4PwpzOfET786voVOfz5kyfJ8Ghu3vE-HjnQ1xVlDz3O4b47M1-s66zcv8FVfk_a6mvGjWs2y1kkge3z6bjUAbSao1pi9eZ9WDHamrzIJmU1GrdAcrPsZIf_vIiIl_TNORzyPsA70332Vij7DGiJ7PjUVtGf2SLW53-pAYO5ZUetnaPrX2wu5YQ7SFcMoYFoGZKMgq_dICguottiBjPodNXhNZ0U0uQxcjiOJkwqGBQuN2U-QWU_4Efv9lp9g-kmYoLUuQpdHDeKwa8_GiExiIqFmXulzxnjmLMfN9hpbmtAKl442mikgnP7C097Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6bcd7de2.mp4?token=P4eFAaps_o3iaZg2EbQLXjsJlx4PwpzOfET786voVOfz5kyfJ8Ghu3vE-HjnQ1xVlDz3O4b47M1-s66zcv8FVfk_a6mvGjWs2y1kkge3z6bjUAbSao1pi9eZ9WDHamrzIJmU1GrdAcrPsZIf_vIiIl_TNORzyPsA70332Vij7DGiJ7PjUVtGf2SLW53-pAYO5ZUetnaPrX2wu5YQ7SFcMoYFoGZKMgq_dICguottiBjPodNXhNZ0U0uQxcjiOJkwqGBQuN2U-QWU_4Efv9lp9g-kmYoLUuQpdHDeKwa8_GiExiIqFmXulzxnjmLMfN9hpbmtAKl442mikgnP7C097Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇲🇽
حرکات موزون بازیکنان و سرمربی در رختکن مکزیک بعد صعود به مرحله حذفی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/Futball180TV/94639" target="_blank">📅 11:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94638">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b6c764c3b.mp4?token=rBdOhwDxif2sD5PLixCvg8LFWXbEFvKfJvPN7_h7ErzhbAG70dAKORsCR_ZbD2ECanf8gd_AR1R4a1CsEw7EhTHx-b5al5l6oGE38L8U0032LKnvRZsHKIZ9MY4h3UVHDTq69YOihZDGvhOgjBtVkhscTJbHd9Sfw9xxW5KTJq8FD0AZqSRMuMxIAPYiml0xMaLU7DfGZxDj3HcKX_QztsAZKrGvwj2r1QsiogXh6e1y6pWx5xl0fOvX6tBW1uBcW0V6AD5-GQ_jSApHYHexsicohe3sdOer1DRxL-AubyK83Kj0eKGyRxcabf_ihXK1Ry8I1w4Zqfs89S2vj1arrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b6c764c3b.mp4?token=rBdOhwDxif2sD5PLixCvg8LFWXbEFvKfJvPN7_h7ErzhbAG70dAKORsCR_ZbD2ECanf8gd_AR1R4a1CsEw7EhTHx-b5al5l6oGE38L8U0032LKnvRZsHKIZ9MY4h3UVHDTq69YOihZDGvhOgjBtVkhscTJbHd9Sfw9xxW5KTJq8FD0AZqSRMuMxIAPYiml0xMaLU7DfGZxDj3HcKX_QztsAZKrGvwj2r1QsiogXh6e1y6pWx5xl0fOvX6tBW1uBcW0V6AD5-GQ_jSApHYHexsicohe3sdOer1DRxL-AubyK83Kj0eKGyRxcabf_ihXK1Ry8I1w4Zqfs89S2vj1arrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🏆
اقدام تحسین‌برانگیز یک‌پدر ایرانی درحال نمایش فوتبال برای پسر نابیناش که در رسانه‌های بین‌المللی حسابی مورد توجه قرار گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/Futball180TV/94638" target="_blank">📅 10:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94637">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f084797b56.mp4?token=TcIx1bROJRxrWmJfzoILwTwFRSG_RJvN2YKX_9vnv679pJLAvAzaq6scnfWgjuD_qnDxskreSW3Qs-wQTxKtwUTz-zsEtrF2Jp8mNWZUS0O40qdlwDnGpCaPYe6CZ3FEFXOYYZwrYttlAgEZy0a4spsCX5Ilfsew97Fn1fdldAb1xTaek-9xpPalTejf1joYH4FcDyxzvOdROTtkfTM6n52RZofX7mG0VbGoQPsZsHIs686Ji9lePyXs2sMqX-DES8FfM-OrkpV3xxnnd3I7Nfocu3Ce9nI6ih6QzBP-HVcX0YoHjJUQBru5KGuRtS5KBLq-cVJBHaL-3rxmuUAjuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f084797b56.mp4?token=TcIx1bROJRxrWmJfzoILwTwFRSG_RJvN2YKX_9vnv679pJLAvAzaq6scnfWgjuD_qnDxskreSW3Qs-wQTxKtwUTz-zsEtrF2Jp8mNWZUS0O40qdlwDnGpCaPYe6CZ3FEFXOYYZwrYttlAgEZy0a4spsCX5Ilfsew97Fn1fdldAb1xTaek-9xpPalTejf1joYH4FcDyxzvOdROTtkfTM6n52RZofX7mG0VbGoQPsZsHIs686Ji9lePyXs2sMqX-DES8FfM-OrkpV3xxnnd3I7Nfocu3Ce9nI6ih6QzBP-HVcX0YoHjJUQBru5KGuRtS5KBLq-cVJBHaL-3rxmuUAjuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🏆
🇳🇴
شادی‌ جذاب هواداران نروژی‌ در‌ جام‌جهانی به بیمارستان‌ها هم رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.75K · <a href="https://t.me/Futball180TV/94637" target="_blank">📅 10:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94636">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🇧🇪
🎙
تیبو کورتوا دروازه‌بان بلژیک: در بازی فرداشب آماده گلباران ایران هستیم چون برای صدرنشینی و صعود باید برنده شویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/94636" target="_blank">📅 10:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94635">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d6852b83.mp4?token=kODNXc3-_HLjSxcVAmle6lgyVVZlW_-m-Vzeb-11sCi2ZbV5-0oGUGeGJT4zYSKrRAWcAQUmlrTb8oEeB2ZzeZe6_jVwuNHf41ZLSnEBjLHwjL5syy3eVQPPG0HRFe9wD2FXeu-ToF297QeM3mOFdAsrd0EzMcxeu072Un_8aw2LT2n_lXOD2ZKWMms6L4o3pUZf0XcN7_quZT3wia8YcFF1ahywJBN-79zpRnT50yKgCeujdO0iuh5pAt_rKW-gde_xr6k9EmU9PURThc1hS_aPYFeOQTPU750Di9Cvs4C5Tvv7HPCHwj8g0NESbM0zOeIv2X82twImrkwmFmGMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d6852b83.mp4?token=kODNXc3-_HLjSxcVAmle6lgyVVZlW_-m-Vzeb-11sCi2ZbV5-0oGUGeGJT4zYSKrRAWcAQUmlrTb8oEeB2ZzeZe6_jVwuNHf41ZLSnEBjLHwjL5syy3eVQPPG0HRFe9wD2FXeu-ToF297QeM3mOFdAsrd0EzMcxeu072Un_8aw2LT2n_lXOD2ZKWMms6L4o3pUZf0XcN7_quZT3wia8YcFF1ahywJBN-79zpRnT50yKgCeujdO0iuh5pAt_rKW-gde_xr6k9EmU9PURThc1hS_aPYFeOQTPU750Di9Cvs4C5Tvv7HPCHwj8g0NESbM0zOeIv2X82twImrkwmFmGMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
🇲🇽
🇰🇷
هوادارای مکزیک برا اینکه کره‌ای ها ناراحت نشن بعد بازی دیروز با پسراشون لب‌بازی داشتن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/94635" target="_blank">📅 10:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94634">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYezfBE-88-HS20ZYDZ1YlDr_igNH8EnKYBVx8pFlviqoqRhWteu5yopLP5Lla-mFydUtPpTjvWrF1EwPcrKiW0qbieBRqSjIwWvUnvSqvw57ha9E5s7KoDYkd-zuly1Wh-vM7ihGXR0NB2DQe5-UKD4QwHbMkY5Q41NpI3K2s4HDf9FgWETwmY_FLrPbcxdt3DLRAELm45b08W9RG5OmB6g5eZOtTgQ6HHLRj-4mHAa900Qmbx5k7vLime3T8sCgRaoSCCQtdSpfs8LktQ6ZgRqiYO1NwN1fPoAvnA7byB3vA7WyvnCetdD2s_qSu8Q0uLkvcX4SmpxFBowvOlacw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/94634" target="_blank">📅 10:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94633">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LzxsTYjLtAarmfLsirmL_rSTpa7tdpnMSfsxpx9Xt09QyNWWu3mJrlF1jVjuRVcwmiNUe1dirzVOe9UKYqvg5DISij7Rgj6_vbvj7OY5GQ5MuCtky6KAmf6HVWQtbqZYuT_KBs7M6mgMRKla0XMplR6Jnl9aaktUIkdXRHbMLBWg9ljLk97GtmK1Pxdv9rGY9NM8yAEOHYxmqOXBmsB-kZWdzsWhG9vORFD1978NFs8fFqOMhOQJ4YRvtIX2N8Z3Z-RV5U0aO7ZePwF_SOsXwwOeYB9t0sqnSbb74ITyMLfIxG8N5NNb4kzkRN1B9vU19szJgv61Lq0G9haDZNLD6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
فوووووری؛
با اعلام آنچلوتی نیمار هفته آینده جلوی اسکاتلند میتونه بازی کنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/94633" target="_blank">📅 10:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94632">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/060b592f3d.mp4?token=t-uBFyLE9zGko_-_kjAXu7wgBpBr5cXZZO2BkXe9cjeS4-J3gjOgYu-MOaTJU-DeUgwLYeHAO5bCyeF4No4ngoBvP4IXjM0-N4GlBCxhjgNkSZujSBzbSTq7FxiJAFKPyzTWf95ITFJ4ZGZDxPVD0mFB_FxwmjjkmPWdolgIQaxr1wLaESSFk6YpNojx6PXo3j346E0z4jWWtMLB3KX_VpM63wAO9nIuuD0TcT38qoB-1EGVAg5BPlOd9JH1H1BpIpWjI-u2nBUXzErcbSQLJHHqPbL-uSamh4XQI33PCTwQBUypbO8F-nnTFyHWU3EdSR6svVhmicUPOkUjiaXOUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/060b592f3d.mp4?token=t-uBFyLE9zGko_-_kjAXu7wgBpBr5cXZZO2BkXe9cjeS4-J3gjOgYu-MOaTJU-DeUgwLYeHAO5bCyeF4No4ngoBvP4IXjM0-N4GlBCxhjgNkSZujSBzbSTq7FxiJAFKPyzTWf95ITFJ4ZGZDxPVD0mFB_FxwmjjkmPWdolgIQaxr1wLaESSFk6YpNojx6PXo3j346E0z4jWWtMLB3KX_VpM63wAO9nIuuD0TcT38qoB-1EGVAg5BPlOd9JH1H1BpIpWjI-u2nBUXzErcbSQLJHHqPbL-uSamh4XQI33PCTwQBUypbO8F-nnTFyHWU3EdSR6svVhmicUPOkUjiaXOUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁳󠁣󠁴󠁿
شومبول اسکات‌مک‌تومینای تو بازی دیشب با مراکش که حسابی وایرال شده
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/94632" target="_blank">📅 10:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94631">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4864edf2.mp4?token=lj6UQXKxhgYQVKlYCNa6qrCEWgZrJSRT0uTVA8SvwrzuxGBj5B27tpe1GKASs-0660-pSkNXRKTZ1JsMI0Opw73h79K1RGrccvorZWVV6um6nJ8_d55boxYo-b55z5EB-6MFMIoTmC7H9HVjN1soQ2JEa4aO8UE4i7bmzxR0w8XxSZnzjYd7UZ1WbwORZJNMIqh6CADs-SSJWJzqv6ictpDTAkeK9j9eZKSTPJLOzyL6O7zS67YzxoMx2Kha7AUv1t_hWSvofwazGlVfVO_rZPzwsnEiz085sggSjG5Vze5mE4lrCYNBdJs2KeoAI5uTzXr6bvcQ5pWHhec1YJZudQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4864edf2.mp4?token=lj6UQXKxhgYQVKlYCNa6qrCEWgZrJSRT0uTVA8SvwrzuxGBj5B27tpe1GKASs-0660-pSkNXRKTZ1JsMI0Opw73h79K1RGrccvorZWVV6um6nJ8_d55boxYo-b55z5EB-6MFMIoTmC7H9HVjN1soQ2JEa4aO8UE4i7bmzxR0w8XxSZnzjYd7UZ1WbwORZJNMIqh6CADs-SSJWJzqv6ictpDTAkeK9j9eZKSTPJLOzyL6O7zS67YzxoMx2Kha7AUv1t_hWSvofwazGlVfVO_rZPzwsnEiz085sggSjG5Vze5mE4lrCYNBdJs2KeoAI5uTzXr6bvcQ5pWHhec1YJZudQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇿🇦
بازیکنان آفریقای جنوبی بعد از مساوی مقابل چک، جواهرات و ساعت‌های لوکسی به ارزش بیش از 50 هزار دلار پاداش گرفتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/94631" target="_blank">📅 09:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qybBZSvn1_D_htqD0vYMsl0zVStAMKK9d72baJGdaPRigrEO2w-4BY7GMMezLMYmLeDczYVQ_YBtAApliFBbWpV0W72ts4d6QqnZDRO-ZCYOX4eR-QzUfNGN9_lavqclZAuLjfoUsbkcjmAn2hNbJIdlzmO8HtbDoJVn98lCReEAFKTDPuv7tO0WnWt5xp04l2kJ3Ce4OINQelOEPceNs8_JkElrUTbungXLImdh2xX5oxOj75itHf1qaMQfRaqs0DcUQlXpVJUmDt7yos8ZE9n6OWHyXtdqb9A-lz2E8EH4ADkb-wl-xP-iuE4Q-SSEvAzi28Ht-cbTm1tLU32fWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gkLxKkt_vlI1DQB5H4TiN7vTLAqinmg5qVZUmqUGjoq1Y-y_6YStPnsQxLpXLk5Wx9mLgoDdEJGajandYeBLubhTc3flD8dtmIikAM-23hAG3rxqlevR42H0v4xWLlpMxKeCHPWsVx0BSstWKw78ambwCaceD-5oH2F-u-6kkXMV1Ou8gsBdu27NbDwkWJq7b1eST6JKtUw5cjrjOAHNQC9YrrWjJMJ5ImBIWCbYgvrNaKg1zNqLqe9KRhiOnP0ZfVFeWfGYQYKMwGqxPZjjH3YvBoWtpkKvbJQL_OEiIxCMns1QEyQ7OsXRCj6tx9Rnt4MJHlEu1zuc21ypSjY0Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ft4LSv9Mpo6tr_X7aP2JlhWNO3XqzUNugvQa5AV-zp_4obNqq2Ac_B0GKg5vc1y-7QHXjMmlzPQ7A2sNfFKIXHOD1idXeG_uiFYRZmwxUYaWdPXZUwlRL7c_btewknxFt8zYQnAofPU-qv_gf3cLGrulk_Ro_4_hJPuMW88osl_L7ZiP4j0hlgb09juWc1C4F32YwY_NSyQItaIj7uUZopJ_OqGNqeXYoD4zbldNHrdBfBb9QHZQX36AXmjteljaiWb4clh3d8lLAHczNwE6g_lbaKDMtvLTMMlJ6KLr1dmjdaOLEx6_O2Ugr48YLqIK6fJ1MbFGg__JFJfV19oCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eo7mDHkiHyGD8sX3hn6NJGVcz8ye443AulmIsE3MmVqAHh-h_8cniN1OG3rmCicdoWC_yMJZU8BIxxXjn7cf-nMh_HSyQub-9egUPGKrllc1T5kfWAFI30YxUPSDZLvIgvhG8is2CXwlCC66E8rsX5MokFhneh7iqGvN2iWr-W1_h_vxtbrTXvGhMHOqzY_ETxR_RLYeP3Y3H2Zc5oOmgkqzFrNNMpvf1jLnEOyOI-6Q1KtnSx9jLqA-Hr8Ukt7kJMmW_NFJgJHyoLGZa6acfV5dpr95PBL6vel--qcsInOpB4SaAieQ2X4QEJIVmNcQMEvST06zd5gUFgXSkCkd5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇹🇷
هوادار ترکیه در روز ریدمان کشورش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/94627" target="_blank">📅 09:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7c76bf8a.mp4?token=B3yzPWX7kP_QJHiNRogvSTgZmtXug6lhp-xlyi42-BzbgDkHCjtBCC72rDDIgsP8fD5zoAj99d8jBul_828vbPmi5Z1cf5uXifhI_y8-nxawwER0EADdqJ26vzrVyP2KN8DH18usNkMNVZ--8jV2whjbrDoTQVFf8JQeLQY1ittnTsqqGlOlZVpAV-rq88fVCS7mDGitQ_jY7788SLMnBBiH8lxqJUL9UFpuiRRidUccXyW23ynmZO07lq0aFlSXT_HRALmdugB4CPrhEp_geYcvCtyiWuSqGDpdf9yj9wsGTPZ_REblIKbudTwT7GdOQJrNYZKrBnYlTiH83d4Paw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7c76bf8a.mp4?token=B3yzPWX7kP_QJHiNRogvSTgZmtXug6lhp-xlyi42-BzbgDkHCjtBCC72rDDIgsP8fD5zoAj99d8jBul_828vbPmi5Z1cf5uXifhI_y8-nxawwER0EADdqJ26vzrVyP2KN8DH18usNkMNVZ--8jV2whjbrDoTQVFf8JQeLQY1ittnTsqqGlOlZVpAV-rq88fVCS7mDGitQ_jY7788SLMnBBiH8lxqJUL9UFpuiRRidUccXyW23ynmZO07lq0aFlSXT_HRALmdugB4CPrhEp_geYcvCtyiWuSqGDpdf9yj9wsGTPZ_REblIKbudTwT7GdOQJrNYZKrBnYlTiH83d4Paw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇲🇽
مکزیکی‌ها داغ و جذاب بعد صعود از گروه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/94626" target="_blank">📅 09:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d20f3a10.mp4?token=FJtrZD0G8bx4OauqsAFyjkD7NYVSiylpD8dAAVDQwhpAiRS3HG-shQB51S3wCLlbRL7FRyCsCD4elrwcFYKzGbZVopwKUjsBRuu0XtlBtFejB5vbkn2Hf9Wu3RLRmg13eE-vvw7qr8KMpu1nhO9LY0hBroHESJV7MK9teKpGnAdqciJtzDve-9lg30Ycvr8Z2REdB9N-ghw7xVLEjl_fTaemxMA8RUBF7Sx7VqZ8fMntMS-wyYMPQK3_72sbM7WaQQ-15UY6V6bZD6JVkXM51rbNYb44N87T7-smldGeqYnXwJRjokJej3ZqTITnsx0aNVDT5UHN6_UEw61pQ8PW0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d20f3a10.mp4?token=FJtrZD0G8bx4OauqsAFyjkD7NYVSiylpD8dAAVDQwhpAiRS3HG-shQB51S3wCLlbRL7FRyCsCD4elrwcFYKzGbZVopwKUjsBRuu0XtlBtFejB5vbkn2Hf9Wu3RLRmg13eE-vvw7qr8KMpu1nhO9LY0hBroHESJV7MK9teKpGnAdqciJtzDve-9lg30Ycvr8Z2REdB9N-ghw7xVLEjl_fTaemxMA8RUBF7Sx7VqZ8fMntMS-wyYMPQK3_72sbM7WaQQ-15UY6V6bZD6JVkXM51rbNYb44N87T7-smldGeqYnXwJRjokJej3ZqTITnsx0aNVDT5UHN6_UEw61pQ8PW0zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
بدل‌مارادونا رفته کف لس‌آنجلس سفره پهن کرده چنتا حرکت میزنه مردم بهش پول بدن
🌟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/94625" target="_blank">📅 09:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94624">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🙂
🇹🇷
آردا گولر بازیکن گنده‌گوز ترکیه هفته‌قبل: ما از هیچ تیمی نمی‌ترسیم و فقط به میخوایم صعود کنیم و مطمئنم موفق میشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94624" target="_blank">📅 09:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94623">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7068c129f6.mp4?token=jv3L1sYzRev5M-UGr11cyAIq7tqAOwsVwLQDIAHfX-SE_3_hyXCyEfDGwgCjYi8yVv0In9qsMFi9A0Ox94KbTKx52oEAxv-1djo2TOB_29tydCorj0_7tG9EQCRG0o7o_gj633sloKmUxWw3U21bFO93SSS-utyeIyYKqXDtlHRnUyFO2TnFpkNesqmUzzHa5kcvHg9KAPWwTkDEcIcfHKNy7V4-8Tay-UQUvGrS4mKHWcl4w_ovJM2F2-ELE9F11V4yMV2L_oPzPSc5x6OUzhsP4xLqd-gsfbOaipTGf8UoVY0CC8dqHCM-tPKxlZoe4ljbnowf2vfvsNeyg_rfyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7068c129f6.mp4?token=jv3L1sYzRev5M-UGr11cyAIq7tqAOwsVwLQDIAHfX-SE_3_hyXCyEfDGwgCjYi8yVv0In9qsMFi9A0Ox94KbTKx52oEAxv-1djo2TOB_29tydCorj0_7tG9EQCRG0o7o_gj633sloKmUxWw3U21bFO93SSS-utyeIyYKqXDtlHRnUyFO2TnFpkNesqmUzzHa5kcvHg9KAPWwTkDEcIcfHKNy7V4-8Tay-UQUvGrS4mKHWcl4w_ovJM2F2-ELE9F11V4yMV2L_oPzPSc5x6OUzhsP4xLqd-gsfbOaipTGf8UoVY0CC8dqHCM-tPKxlZoe4ljbnowf2vfvsNeyg_rfyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
رونالدو که تو اردوی پرتغال حضور داره، جورجینا رو فرستاده خونه تا واسه پسرش که ۱۶ ساله میشه تولد بگیره. پسرش اینقدری بکیرشه که حد نداره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/94623" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94622">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWhWJurB1nHc8GYDJI5rQVummKGRvBoWzihvZ2g3yKqwoDciQbG6QPHJmJaY9Z51ZWJzb3b2D7OtPQQ16vh6wGqIYbMsWc3nwL3kTYaf230Nb5zWZH8-_rS9jQySCeSvyz7x_qUM6i4oyrMq3kNmtlEV9aTIlPGlE0FCaHlSEyR25e5MPr0l6rqVYa55ZTGRjnbef2S6CFsgt5m1Xd4KykXRpBe1FseG6JMutRtzGzzof2fOVLB-Jor1lARLr097opNMtqdATkTZlqKMFW9YXyLr6DCKaV4Dsy_qR_MIGx5DVLi-9uabK806HWOKPqkGaEp5Y3AmACkKn5om0OWoqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیه در دو بازی در جام جهانی:
۳۰ شوت مقابل استرالیا: ۰ گل
۳۲ شوت مقابل پاراگوئه: ۰ گل
۶۲ شوت، ۰ گل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94622" target="_blank">📅 09:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94621">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7F2FxHVNW7ai7fuuD-V0pd8kaqyzuAHjBsOaBQr7nREbf6KzbtAkQriH24fYMElVgjWE1peJ8MNoUlNnHCQn2vEjQzZceciBm89DwVZPuOMGbFjC0rOJS-3w5h58NSA1_1dsE1dnn-bgBQVukSIjmgZ2CIHpTjJ88tBzkJI9qA4SA0Fs2SR_Rc6j7uieHDmcEC9FZjbmqmVvbxMULl73LgXvaXqFnFhF1Iu0nE5Z5QzoNbEebbFiMGjMrLMWIByEvii54ouZKtt6wHs9b5SzsikkPVqPlaNjLymXomfADkzyyCW_UzSu3TQfg9fBkrJ946Tc1Z5JW6a3urhsMI0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
نمودار مراحل حذفی جام‌جهانی؛ آمریکا و مکزیک به عنوان صدرنشین صعود کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94621" target="_blank">📅 08:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE5huovr4tS_oRAKq95Ozw3I5DYents-cxVsSEqYPUGRWfqnP5esGUgOrtr2AkjHzvhoA2GfJfnbQDT39RSK6HVrPShMM2qpRBOhFU-RhWgschZZIJgM5pPMlKfankumA9HbfFlx_ucAzva_QSVXS30Tac-b1fK1n5BsyWvPfsMdliUsqVVJ8PkisSW7gQTeWfp97AA4YneQlZO-UcUn9-j7Rbf-7D-NVJHLuLiXvFi66SplbllmPybZF880xJs7j3mR4xlbh1jNMZ-kAJeJpABXVXpi71Lw0SW5O2RXWH-QACcBPt06nDrpqxoJgEtxSIJSK5K2L6B9cInPO6g-ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇹🇷
آردا گولر بازیکن گنده‌گوز ترکیه هفته‌قبل: ما از هیچ تیمی نمی‌ترسیم و فقط به میخوایم صعود کنیم و مطمئنم موفق میشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94620" target="_blank">📅 08:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94617">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/srW50-S47mPvpt_YVah6qo_bQX1P4OWYB1hiv8kJ0rXcm9_6g--O4YxfXlHpIcLVFU-fVmtxBM06f3Dv6fimxbyQoGsTFV2QJ9dh7sOVVhZpB603Ozmyyt82OEbXeoW33cgB0gNsFFZatiJZCwn8OXsT5QCw_Q2zTxUD7Y6_qQY8fnYp3xZ_UK7qfB8sbzT6vqTZo4pIYf7vXo2QiXi_9_LSnWnKtA7s_t2pqdzmNec3QOOjh-HXfxehGx9yxW7EswXxYJd8xUce4MVgvDxf1FbP1RKIAqejO474_hTl8jUpWiwE_89CfdT5ECLDXLm0EqRH8gLocWdF73GJJeqgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YcbJX1OskfLEo29ifGIW9q26PnvcNE-cmJV17ZiDnxs5SWxK78TOguffhs7U0oIKWkUi9UCJ_pikEzYx8q_JzHx-1ULzFbeTY8xdrwGl3Q25lAPYLMIIHnEw2yolwmsFgwiE-krTxBMxXSkUu5jOm1A5Cuu3TDVOgY6_MWGiAV0g7ogaYLMhcZss9m9KYo08zVNM7KCiSEtj2xTXdkS-SqB4RRLhaJ2RaGrogDbNMO0-FrGeAcIB0yosQRvQktf7m7AqutgW4MCohpQ0AVT1XrXBIzqeIuMAhi2bl43FNf4e88UdZZrqKVqO0_PHN0_m7hfVDLeYkCfxv4j3-Cy7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RuzWEnfn4HIAZlZn_nbpim6d4AZjoWLxqqbzIyhL7yQXmJQx4fLuI9fWPE6bHZpqY9USQPmALQiTDvTHKWjAKo2PWDng7ipnfiQV6kpWG17vjaay65CXCZFon5npbttXNE-XI8imfYd7DifnPhZGLClQa0Fqk5qthJbHavbNcj4CGjrM5kMglSb08WTMnMn-A3HJH7SVd2a9IIQub26mfZa-jLIxu2QJzjnmgk83PV3piBVUfq694gOCUMmzcgrC6VEZVQ5zJcuC_mM6lz3NiQcK_gLkgXtYSZNPJug9fHrnKzfh6V7aHoZrEmjXwiXoBsKjY7iDwTK8FsjA4ysaig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
حسرت بازیکنان ترکیه بعد از حذف از جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94617" target="_blank">📅 08:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94615">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rncN5BbPRbqylGnAv01gTJFhn-9Q_YcTgC8VJ-1sDM9P-3I1VWhNiAr_4AJ5ITcJ1gXE4_SPPxJ9GrOGDH10Q3a0BistQMcsAe1geYPTt-xFkEdNug729V8Ua9j3BCKvbyXxoeVy7GNSEGHGBU7W0S1yw4kLKbL84J_JA7y5tt0jVQ8g0ykUFAZm4pT55QcjSFWvi38sOWVUDmUkeWWH5bAdtIWyHBVU21cPNUHZ04NhW4PFN8JcSJazPEau_UQK8wLHAcE69rMlJke15U68lS9i8RwLCVGpIi71uXLfGSgxuUNyPTuccmJsC_C9kRIyoCoFKVABTEmDCmbmQXgsjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|مقاومت فوق‌العاده پاراگوئه ده‌نفره برای کسب سه امتیاز مقابل ترک‌ها؛ شانس با تیم آمریکای جنوبی یار بود
🇵🇾
پاراگوئه
😃
-
😏
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94615" target="_blank">📅 08:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94614">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-acAeOptBz1GenvzXjQ6GTxjMya7zvOQsHrx4hwjTHFt7zG4r6bzGuJO_TipZ-zF58-gnpXVIXSJgb4euTF6bMTLwRP0CJF229OJZJMCfGDX6w3BSDwCPFZfaQgdcOdOlroBIPwjRyOMV8NnzbFEOef3c5PEwEtiWXAlJ4K9N7p8tLCS56hAVuEQBjzLI8yG4YSmk8RlFd7EG4EKG-Fpc5ZXhDrQn3tRKnmBuyIePml2uQUnsJd69CjZRGy1esxT9irsYIEHF13NlnoGuhXWWnFjC2Fe3xchc3IQXet5bUVgvt5G4er6al5RZEFiFhu-dlNxcMtwMQ6bcjsXLrtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی
|مقاومت فوق‌العاده پاراگوئه ده‌نفره برای کسب سه امتیاز مقابل ترک‌ها؛ شانس با تیم آمریکای جنوبی یار بود
🇵🇾
پاراگوئه
😃
-
😏
ترکیه
🇹🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94614" target="_blank">📅 08:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94613">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
۷ دقیقه تا حذف تقریبا قطعی ترکیه</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/94613" target="_blank">📅 08:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94612">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🏆
🇧🇷
#فووووووری
؛ شایعات رسانه‌های برزیل: رافینیا بدلیل مصدومیت از ناحیه همسترینگ ادامه جام‌جهانی را از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/94612" target="_blank">📅 08:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94611">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">آغاز نیمه دوم بازی</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/94611" target="_blank">📅 07:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94610">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/viKttt7MWrXinfY7pWkOyuOQa7qa7cFsK_ykjPFss8cNq2mciFnvPMIC9GBcGesUzULF8HLaCn0cjpe23Y9p7FNJi8j-VyOKK5ov7euQ3Hc5JElEcCllCFCr82gWSeJSnKBCYhTN6a6Yh8hKMirTitp5lLsDXET--p5mO-Hqfeu4eWcHmXfp0zapeF7FHtOtYwiFCCfmUg4OLWXheUOiIBdLsM5PGWNCQo5stLTgtg7SdA0RMJ7ojAiDuPyZQQvKm1At8--J7S2RQJ4Iwz8lSlxejM5tOar2drTkGcTut0p2q4SE0_7ohVvNOf9GBsGU5ta3C6KoJxrsXSqMkkjVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🏆
میکل‌آلمیرون اولین‌بازیکن تاریخ است که با قانون موسوم به "پرستیانی" یا همان  دست بر دهان هنگام صحبت کردن با بازیکن حریف، اخراج شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/94610" target="_blank">📅 07:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94609">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANHlNJvIwfbXDaAxy3yxDPItn-NiqVIS-e4QAgDqTLqX6WIzP0Y8foani_lslW6h9b9vP6MGMswfwLayywbCNcrzCfUctmcbq7GIFZtSNdj1D8HNbNdQi4WSUeZd_FPWG4FcE3ewsOztMYqE58wD9ZPi6QO8hy80aKoxizgBljPnMO_UzIXwuPekPmF6JllLH3gagXVKge06VQMgLFtjrzIQPXqBWcQahaj0s6Q_hNc0q57KUwBNS7LP30-mLcnHFGznyEno5_k01_5WnYP5mGs_n0lejb1Axe18mqthPcc6aXHg_2hifNhov50_asGBch7jAhR-IPP4WBq1ssmahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇾
گل پاراگوئه به ترکیه در ثانیه 64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/94609" target="_blank">📅 07:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94608">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVdMgfIx1OPp7GjVzeKJHwVgzf3GHMXYZRqn0wvtRV0CU-T7HsDdErbELJ6UDpTONb3Bmzj_vjZfWfIvAAPMhgJ_OTlXcUcrShW3n5TA4HNh0peal17KqEGci_c8ausnHVTBZ5XJe2L_wK6wRjaHEDNVHFDjoLeAlXA1tCTpeafhOPLLTyPK7QkgBJoZrwK8jiK9S-aHtJRkjKlrqMa8GLFHqTNu1G5X1co5-CzEYAz9Uhjhc2_IyTBrMc5gFUU3KdEKviVAfb9Y_AJF0HFlIF3kXBwVlZVm6HVPfWvN6oIUzU6JKZZJSXa1Ox3YncWlmovsxGih4-itHmy002by-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داور بازی چون آلمیرون دستشو گذاشت جلو دهنش و با بازیکن ترکیه حرف زد، اخراجش کرد :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94608" target="_blank">📅 07:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94607">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a087e0f84.mp4?token=HDStPXjXC1FQ_Ntn3gTz7UmSsF8lhbxcxy_kIa45I6bkFC_fWAxNXPQtJJHlBlzGhBzLM0e2Rkr4MehR7N-aj_-2DdBV6tvpq8i8zwOvJeFcXFI6_UhmJerGv4BSDC5mNy3wkaTzERty1xtrAQd3RUWk-FqF6k3Rddoj5skO4YIon27yQ86VcHVgDqpyOJfyxoGASdr_VGUT25PqHXMu-onkiGx_YDrrJTJoQy9Ckk_TNwUdkqSv0Te1aTkoBmQ4Vsf0NLO0kLeMKjiscJopm21KgIowbqoHbUrnk4JBYWiFLfmS64BTnKggrOa9DoYs4HG-cCnXuFU2HTIaCHYJUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a087e0f84.mp4?token=HDStPXjXC1FQ_Ntn3gTz7UmSsF8lhbxcxy_kIa45I6bkFC_fWAxNXPQtJJHlBlzGhBzLM0e2Rkr4MehR7N-aj_-2DdBV6tvpq8i8zwOvJeFcXFI6_UhmJerGv4BSDC5mNy3wkaTzERty1xtrAQd3RUWk-FqF6k3Rddoj5skO4YIon27yQ86VcHVgDqpyOJfyxoGASdr_VGUT25PqHXMu-onkiGx_YDrrJTJoQy9Ckk_TNwUdkqSv0Te1aTkoBmQ4Vsf0NLO0kLeMKjiscJopm21KgIowbqoHbUrnk4JBYWiFLfmS64BTnKggrOa9DoYs4HG-cCnXuFU2HTIaCHYJUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇾
گل پاراگوئه به ترکیه در ثانیه 64
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/94607" target="_blank">📅 06:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94606">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترکیه خداست
😂
😂</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/94606" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94605">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دقیقه 1</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/94605" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94604">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پشمامممممم پاراگوئه زد</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/94604" target="_blank">📅 06:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94603">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شروع بازی ترکیه - پاراگوئه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94603" target="_blank">📅 06:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94602">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc234e406.mp4?token=H-M-0QT2pvac8qC_Xr37r734k9AU9LXIPmLaFGPPJZuCKFSIyX9aUHSNOU0y-ULcmTjnbL-Sf0fJLuW5EbQDOtwuViAIRWQloyoRqHfB-puqEwa54SLB30qrkb2PhOmzOx3FuH_WD6dF_9lfAQqwKGefEL37tmbLMDHUGJMqEkQmCATzVckvhlzaeilnVKZczx15q11FNBShhFipR6j4pZ8084MyOKYILMkVR2wlMPtUv_D6WlJ7QRFrMB6Fyz_O9UoNQZjypnM-LktrxSiPBwM38HrgWR4YpfKgC_z7z62K6NImktXMfvJGBhsjy_OYbJWxGVH_2zvBJWDvTNC0vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc234e406.mp4?token=H-M-0QT2pvac8qC_Xr37r734k9AU9LXIPmLaFGPPJZuCKFSIyX9aUHSNOU0y-ULcmTjnbL-Sf0fJLuW5EbQDOtwuViAIRWQloyoRqHfB-puqEwa54SLB30qrkb2PhOmzOx3FuH_WD6dF_9lfAQqwKGefEL37tmbLMDHUGJMqEkQmCATzVckvhlzaeilnVKZczx15q11FNBShhFipR6j4pZ8084MyOKYILMkVR2wlMPtUv_D6WlJ7QRFrMB6Fyz_O9UoNQZjypnM-LktrxSiPBwM38HrgWR4YpfKgC_z7z62K6NImktXMfvJGBhsjy_OYbJWxGVH_2zvBJWDvTNC0vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری از اولین برد برزیل تو جام جهانی
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94602" target="_blank">📅 06:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94600">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P23a8hjAXQh1jQcJc4VSJF05TtpwGNvQOVswSw3XoFadqxqM_ECBy_beiUsKGB3_20M9lzsU4hJgLc6qxRCXBsdLO7t7dHNfJfP5H9nh-q2AI2jNhaO-yREwnCr4sQrJYfjhVxI0HYHY2jxqDtZIHwm9IJHaxFBUt2UX1pD4JQ3sbesQDyBqFCUXxHNxxb53mrfw41hCTHNd2QaWkBXp1elWBQlf_4UPOrv6KVII4zgzgUGylp5nD1TVB_Z1hee3EIJ6SQKV-v-bjlVWaSJM1mcUEjLgLy3osm0eTe91-XKNylLPvTEKfdPiwZWwZQKMFjTVY4i8YUjPJZMGB5p9mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
📊
آما
ر
وینیسیوس جونیور زیر نظر کارلو آنچلوتی :
‏199 بازی
‏
91 گل
‏68 پاس گل
159
مشارکت در 199 بازی!
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/94600" target="_blank">📅 06:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94599">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjCLlpCOTWnX2JqbbXvw7P7sY0Z9SkcJJFFkAF7qgz57dTAMGvnQqJB5SpgTjBoCwjx-uK5Be6APaYBmmaggKi7DBI1zaYy4UGSPAjSparJmcsVSAxVzaDGjssXzgfJonLDyoj89ducQqixs5G1fhU3L9kib5_TPut_7AULIQXkW41eip0kvkumW1B7DT7msiftv9zGZzrWGjxR64grSYXVhHCpqh_zngSjv0bGxoAskmGNXqRcPGHxkW3a5eRUsK3n3kL24SiOxKqym_pewB4JEofTpyQ5fQ-WBIi-oD5JWZopxV3rf7j3fDDNQ51FdQ3oNV1rCCgBAyZXXfMvFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کمرم رگ‌به‌رگ شد از سنگینیِ این عکس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/94599" target="_blank">📅 06:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94598">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLKkkEBP66b7DCO7reyaTz2fEbko2kSrJHT9JojxHRu6x2-z20GVmvNHH2uKHJDrs-b_dlxeSIqTPdftbujsSWF35NVDXKqG51GmaV6iJMxY6SUd_S7lgcvOv5TnT69c97rURVgAs9r74aF83AoAzCylNjKswZzB36JlceMPsT0IUYSy-foiruNP-Wbyn_a1mBg-xaAQgWaWScBgZ_z5nNkQ8AKRQAUHVk5O-qI4NoRhbP6iYVmbfj9t6pFUQqWJIQOxyLRxE_Cbm9aDQUUUsQhFUdwfzdo_Bx7niD8GB3zJiNg2TkQdbAFLBj6LzkPHwKToHfS_SqPU8GoZkvlGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع شاگردان کارلتو در شب گلزنی وینیسیوس و بریس کونیا
🇧🇷
برزیل 3 -
🇭🇹
هائیتی 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/94598" target="_blank">📅 06:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94597">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AFzJ2kkkn17oVSi_hcLb8SvuR13KEr9CKadJYe-f2t3E8-gQ6QrZQp33HihU6IYpMyNDx-5O1BqdgTBYkm5FmbhpKpdjlNc7MNyxwBoy9sg4gwwUla2TC4X5i4xkIEoInBTdtv0A4IbVzraX2L8O86VFqerfmfensjjUISy9ue6EL_1qHmuICOGyPrs9BXHju5jXpPPI3WWSu8xmwdY-rma1Ha6hZVTswYeoMsz1qKqh4A652t-AvIo9kXHUI_ftX5Hv4yoU2ZwM0d14JytKrzVVwWbOga3-DCLcnmT1WSdPUIZwzfCBUeCBFKIAHmuSK4YcKEtuDblp8Ccz6PRSaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | برتری قاطع شاگردان کارلتو در شب گلزنی وینیسیوس و بریس کونیا
🇧🇷
برزیل 3
-
🇭🇹
هائیتی
0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94597" target="_blank">📅 06:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94596">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXd5pNS7KPqfD1aQoNGQxlOyBKxT4KBZi-ore7qxCK-UOC7GpzAUwERKBmv7FyppZHqZTx3cmQEf7EemHuEGisxjRWVT2At4oI2R7n8PZCbdNzTkL3E3FvU0mSPf-IlLzIUdpA_HP1VYC8Dbrmrl82JoMycxpBPQELEScnrgXSwM0MprR6tqjgLs1H-fiW7WFlWVVJWKv4NwGb2CeTxc0vjotAv_HyDSrdjbeyiJLUMR9_LxZJhkGbrdcgPqMZvHOHRGmje82nXs-ImCwfAGVZcoKn4KYLSVMMaeyORSwfe4kOiDxiStU2hJ8km_xQtmeoiuU2Sd2p47RnZWyNfGxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🔺
خوشحالی گل وینیسیوس به سبک کریستیانو رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/94596" target="_blank">📅 05:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94595">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZ7g9Zrqh9mMqruOnqD5nsGcmvQpGzTcg8_CLboqkY0Wu2jHkkMDxiq6q-2eSCSuZZLhLwTbLH7RIKnj-RqTcZtnpPn1EYNJlzlPfpMyxPVq3pFaes2p75QWDiQeLQ2BDM5R04Dk9QQeyyOPk_Z4l-6QwLINaHhUU6BIJRXJojoC8fvixqyFbs9SjEmkUlMXJwiVz74FQE5cMl1cfZJyNKBz_Yuah82QJSpefFCpSKrAbKvR8PsVDYWEI1jPJ3I9lnETS5U_1hT7IIiDWXf-INmB8cJicXmof6_KLr5C3a71hHi-vW_NHzZ_D6XrJQuE0hll4KtfTKrbBn-AthDyLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرف 2.9 میلیون دلار روی اینکه بازی برزیل - هائیتی زیر 4 تا گل داره بت زده
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94595" target="_blank">📅 05:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94594">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اندریک زد ولی آفساید</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/94594" target="_blank">📅 05:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">پله زمانه وارد بازی شد</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94593" target="_blank">📅 05:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a84e25e78.mp4?token=NQa5IDtS5QMcGvQneE1BlkU3csCHnVZKh1FN6mDeXhdfYbT1jKTqZDklJkMkCYpCemR5B5GYoQOxueudpaXgcDu78lGJSYA1jwr5YfmBoTufSzJqbWZkdMkx4L7GhPtgD3nJRdGo6_MpDBa2YT3e-UUmgNCXRiquNeuA46wnrwPn0zoLZfvd_IE5zyKEGKM6Alvu7-vUMjBH2paJLFcOsxlbNQze1DPOpgAQGfurVESZdg_2yLTM23CLZvg_3r3JaEOML4MFvg2UZCC7Bi89Hvdx-N6Rzj2nFTbTXhWi_qCgK0flC39MAZwmNioBlPbCRPpoyYNPsyLm6JS4D8oZCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a84e25e78.mp4?token=NQa5IDtS5QMcGvQneE1BlkU3csCHnVZKh1FN6mDeXhdfYbT1jKTqZDklJkMkCYpCemR5B5GYoQOxueudpaXgcDu78lGJSYA1jwr5YfmBoTufSzJqbWZkdMkx4L7GhPtgD3nJRdGo6_MpDBa2YT3e-UUmgNCXRiquNeuA46wnrwPn0zoLZfvd_IE5zyKEGKM6Alvu7-vUMjBH2paJLFcOsxlbNQze1DPOpgAQGfurVESZdg_2yLTM23CLZvg_3r3JaEOML4MFvg2UZCC7Bi89Hvdx-N6Rzj2nFTbTXhWi_qCgK0flC39MAZwmNioBlPbCRPpoyYNPsyLm6JS4D8oZCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وینیسیوس: ۳ گل در جام جهانی
رونالدینیو: ۲ گل در جام جهانی
کاکا: ۱ گل در جام جهانی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/94592" target="_blank">📅 05:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s_h8Ufe8zccBi-b31hbbFmvpKa1W7k6eAW7SQqCgjFEkoIU9wqyD_zVw-JiohOgls5Psq5BvA9FOuX1UX4Lbu8VkjxpK5GoqN5u2_TTrZ_CeW1k6NGOzddV_VLaIYfoJuKI3KR7952Dg8tu-xK6njMtoOLILFrHVzgjKuNjwK5zg-oiDDLNKDJQ967VbVvk80lbNWmZPPjBNNHVp_ssdfznBqSSnlOhPU8K6w2qJ_5B8e42NckK3dV4nl8FSVT-79UOg_eCf5jw7-yi6NbNuX59Bmk4diWhTmQJuED5XTnDkdvNiXcWOaUtVcXM9a80bd5xeDbzV2mvYXZU1Ej2G9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPdIjHPvIz_OcqdEZc83wjWPnc6qCp4gaZ_hub44pz9jybhBkpDpnfCbo-RfR0cCHZZE5qh5WkmlAvV2mXTflSSV_dLmiLviHU98iGL09sUuNcEgJhUOsBts9X2VkPXdKYTWYM6__4_aVBX_2RUwupoKjhDYlfaa7C3nvNKk--VFu-tYQutnm6lVfd31FQUC_BBS0CHuQnoD2p4M6R5GplZvCH0A4NId6EEhBfJ3CW9RMjsEIrEdaLoib22mSM8ELglSMSjILf9bh_Bp4yguLgN0bCIqGXFSwF23qv0iXhRLtCZQYaAFWiV9oAoQE_nglgVRzfShaOFN-5ByK5txGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇾
🇹🇷
ترکیب ترکیه و پاراگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94590" target="_blank">📅 05:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94589">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(ммd)</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=reMp37Jpsy_fzE_997GsaQ4YFCn4xj8uOcB-Bk8tdYqj1dkgHW8RxpkzKc6O_yn5HhFVTKmysXwslMO2yCl-QFeIv4uAcuyfqfIvMBnZoQnRvO9q7tKRDfY3VqV9G1YYgnbkaVrq1_oD_PIeDjk0hS4Dgetu4JiNlQLUhDxJZlJ8N11OAJMG8sSfn0A4N1iEE8CUdMTGB4QtG4pEDVv_OMNhTQe6B1IPdN2leQq_jLG4Wl5rzEjv1Hbt_6XwcXoJBxhim5IS2e1r4N-k2_OtXtpFVP2KReXJ8eisTv-Q7B1yFC1WCar0YGMsexkdDEbrfDsFotkWHMVHi3VFR_8kLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=reMp37Jpsy_fzE_997GsaQ4YFCn4xj8uOcB-Bk8tdYqj1dkgHW8RxpkzKc6O_yn5HhFVTKmysXwslMO2yCl-QFeIv4uAcuyfqfIvMBnZoQnRvO9q7tKRDfY3VqV9G1YYgnbkaVrq1_oD_PIeDjk0hS4Dgetu4JiNlQLUhDxJZlJ8N11OAJMG8sSfn0A4N1iEE8CUdMTGB4QtG4pEDVv_OMNhTQe6B1IPdN2leQq_jLG4Wl5rzEjv1Hbt_6XwcXoJBxhim5IS2e1r4N-k2_OtXtpFVP2KReXJ8eisTv-Q7B1yFC1WCar0YGMsexkdDEbrfDsFotkWHMVHi3VFR_8kLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94589" target="_blank">📅 05:12 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">بریم برا نیمه دوم بازی
🔥</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94588" target="_blank">📅 05:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94587">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8BxQokOQnJNjHIjrFE-SigWhYBdYhyooxLDsHfxaRgvYCniWhnJzh6nd9x-SLREQOxwxd-d9TKnRXPFGeEUfUY7seHYhP4_c-vmLwXvz0eBf7sz2Jy_p_mLjfQVjdRbHb13rJvLCAca8VxzkL1nu9InjMI1f5OG7fWzu9c9pgJZRpdd6jmDNKFDWkMyZv5ty57s2uud4ZBedh4XVwy6G3tdMCRjPd3jY_7t3lcPLZw19AMzCQazHBwmhcTz0YtrrKlzhHvnPRZADYvrG-aoZZNTYrnADGIy4u0aDWIZf3PnSOuNeglfEs86cACaLI73k4QJxaDL4ZWR1vqm4PT0jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
آمار فاجعه‌آمیز برای رافینیا این فصل :
🔺
پنجمین مصدومیت رافینیا در این فصل
🔺
رافینیا به مدت ۱۱۲ روز در این فصل به دلیل مصدومیت در بارسلونا و تیم ملی حضور نداشت.
🔺
رافینیا به دلیل مصدومیت ۲۴ بازی این فصل رو از دست داد.
🔺
در مهم‌ترین مرحله این فصل در بارسلونا مصدوم بود و در جام‌جهانی هم مصدوم شده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/94587" target="_blank">📅 05:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94586">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgqgWsd00aoowDFqGOchVAELXAchdGdwwGa5RQsXwRW3BzNjC-acfy9xwxqx1B1BwSYV2O3SqZYmrJ4mNBwmQcGXMpsxqUJJMUSEpVoBKW6JI3Am3SPQqUMHoYVUvfAOD1PO0S4zeHb1Uv0FQ5liB7C5y0lehz9x_aAq8gX8-8TDp5EHmh6EPxJ5ZcnrSeRvpqR4sUqEX4q4UXF4IdE162CBoyxGIvEffI-0bRGyBfsVBjdJTkK4i2UOwSIlPM1z7aAfP13venZCxeIjAiclXdCbbZs3eGPtwcWC7JiLfdAdofpPcapwwTFX5mx7DKlW8TCyUTmYtVuyTbYiW0wLmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
وینیسیوس جونیور در 6 بازی حضور در جام‌جهانی 6 مشارکت در گلزنی ثبت کرده
🔥
🔥
⚽️
3 گل
👟
3 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/94586" target="_blank">📅 05:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94585">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9330025fac.mp4?token=jO3Y8_cDkrgWGJC4GQGQyaYST5F4YP8yA8TCIAb4MF5c2SRGTVOYDXpPehByfY_tMrz1AJp-bIEbBJktZWXRMXmsMtTuwSlM432Bf-nKDH3MMk86F2pIKSdtuxZKvvaBQXix8CQWcUTAMl9M2M-wlQNIskI6jaLpPsLdzrGQV_eeLMmbg7alx8b5myPWwk9olk-WBmCZDlxXIuAI9cWgEhzwggVI1aMEKJ0LfI27SsmZv9HIOhU5VSimYQWNgg_Bx1iFHu53nxt9hKzSK1JNlH9ehMpe3TR3_E9yKQ6dRgWIVLx7jYY3Qg7FEhQXUNF6slqXqTGucTYVZlXSoR8etw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9330025fac.mp4?token=jO3Y8_cDkrgWGJC4GQGQyaYST5F4YP8yA8TCIAb4MF5c2SRGTVOYDXpPehByfY_tMrz1AJp-bIEbBJktZWXRMXmsMtTuwSlM432Bf-nKDH3MMk86F2pIKSdtuxZKvvaBQXix8CQWcUTAMl9M2M-wlQNIskI6jaLpPsLdzrGQV_eeLMmbg7alx8b5myPWwk9olk-WBmCZDlxXIuAI9cWgEhzwggVI1aMEKJ0LfI27SsmZv9HIOhU5VSimYQWNgg_Bx1iFHu53nxt9hKzSK1JNlH9ehMpe3TR3_E9yKQ6dRgWIVLx7jYY3Qg7FEhQXUNF6slqXqTGucTYVZlXSoR8etw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🔥
گللللل وینیسیوس به هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/94585" target="_blank">📅 04:51 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94584">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وینیسیوس</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94584" target="_blank">📅 04:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94583">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سومیییییی</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94583" target="_blank">📅 04:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22a4caa6b9.mp4?token=V3rITqaP9eU-tDHza12bwxm379G9OOKnQYA74qIlaqREXStqdW1A87NmWbQcMrcaKK_xWTyQYYQ8DAKzJ8xKcKWd67q6bhAR53IjtY7qVXvfbU8xlMPGeuP4UvzmKqp1etOyXqeU2EWFqZi27iqIYUzDGa5GoqRFmmqZJ_jLVtPmG6vmNgeP3cQX-XA7-YLECJ35246q8aZ2kge5Wx2RwH-vjBTsP_1Nxzi7ACBJLmBQiVLcwbj19Mv9YESdz2o2FDwP5hJMVUFX_KbMewJRHFDT4qHiJFyBo0l94UMvhNgRq9LHxsA8U6q3TbiFLm4zp5z_QdMDiFD45tRIe3Ic5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22a4caa6b9.mp4?token=V3rITqaP9eU-tDHza12bwxm379G9OOKnQYA74qIlaqREXStqdW1A87NmWbQcMrcaKK_xWTyQYYQ8DAKzJ8xKcKWd67q6bhAR53IjtY7qVXvfbU8xlMPGeuP4UvzmKqp1etOyXqeU2EWFqZi27iqIYUzDGa5GoqRFmmqZJ_jLVtPmG6vmNgeP3cQX-XA7-YLECJ35246q8aZ2kge5Wx2RwH-vjBTsP_1Nxzi7ACBJLmBQiVLcwbj19Mv9YESdz2o2FDwP5hJMVUFX_KbMewJRHFDT4qHiJFyBo0l94UMvhNgRq9LHxsA8U6q3TbiFLm4zp5z_QdMDiFD45tRIe3Ic5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
دبل کونیا مقابل هائیتی
شادی بعد از گلش فقط
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94582" target="_blank">📅 04:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رافینیا بگا رفت و تعویض شد</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94581" target="_blank">📅 04:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اوه اوه</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/94580" target="_blank">📅 04:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">عجب پاس گلی داد وینی</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94579" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دبل کرد، کونیااااااا</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/94578" target="_blank">📅 04:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94577">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دبل کرد، کونیااااااا</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94577" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94576">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دومییییی</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/94576" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94575">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">گللللللل</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/94575" target="_blank">📅 04:38 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94574">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003b58fa6.mp4?token=EYg2ZwZf1_i0jixu6cHzB9H9cHqzQNmeYIfy5Qlubr7Cx_jZt8g5n_T70TnL34dMMPwmB5SrfQThn_Hl5aCQ0QswuUeam5Cd7UQGlHEwWIlnLjRLILtVGWgTxRfZJQDpbuaISja0a6toCbo1d2R8MlnccU0QVddeOmagTRdN4yx-rTAp7UEwa6976VkOo0DgcrQ3lkW7xTHFqq-3OZQ29Vcnk76rwfz8kP_rF7d8JYwosngfHiOPWCUCCYZ3W9al8RYOE7REL6pupjrp4y5BQStOL8aliiGaH3k7iXv2eD-6LExzGvtVFPTde6iEqMAkI4enam5FQtnoOslJqOhgjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003b58fa6.mp4?token=EYg2ZwZf1_i0jixu6cHzB9H9cHqzQNmeYIfy5Qlubr7Cx_jZt8g5n_T70TnL34dMMPwmB5SrfQThn_Hl5aCQ0QswuUeam5Cd7UQGlHEwWIlnLjRLILtVGWgTxRfZJQDpbuaISja0a6toCbo1d2R8MlnccU0QVddeOmagTRdN4yx-rTAp7UEwa6976VkOo0DgcrQ3lkW7xTHFqq-3OZQ29Vcnk76rwfz8kP_rF7d8JYwosngfHiOPWCUCCYZ3W9al8RYOE7REL6pupjrp4y5BQStOL8aliiGaH3k7iXv2eD-6LExzGvtVFPTde6iEqMAkI4enam5FQtnoOslJqOhgjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل برزیل به هائیتی توسط کونیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/94574" target="_blank">📅 04:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94573">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfaFXW4w77uN1r5iqsD-1NDO6flWeQ-EpOLfgD0te_niRwu5TYN3xN-Wm1loTN2pPxZhou79_Jsp69rZLgLnX7X4CHjlV63JmrLBWpPbsNHjrUKPrImojqmv826KuCAmhQ_rztjqdHGRrFdMaGJTXiJPFiZwXaUlbrIEeoX4oKAH9FP8gKvzD2hxWzKNznl0CywyuGY6rke_ebjyXkA0p7Z-8WDswhD95d43Pnry63TT3KFBSKyBfAp6psIhntmY2PWEXZlafZ6lnTLKPCAP4XzW-7XKUFZishF-ppFgCiLOkvsi03LsUOA4vZ2H-eLNbdzPAGVFSAso3WLbWLlx8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز دلقک بازیو شروع کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/94573" target="_blank">📅 04:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">کونیا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/94571" target="_blank">📅 04:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">برزیل بالاخره زد.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/94570" target="_blank">📅 04:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/94569" target="_blank">📅 04:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رافینیااااااا زد ولی آفساید شد
❌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/94568" target="_blank">📅 04:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGG1e51c0rqoHzJ9A4z3yzxHJGpDyWHOlormHnTLjsRE8AmPZ4KY8-XVBEENYIEVC3NmNtcvrEp9PQ6Sa1KefowJof0Vc-mzGW3qZG99JyvEUusEmm3ND3GXQGac_Q2hTsilQI6eH0aTzVRmh-UJGcDhY68Tc4C7MqHjueuadAZWjmQjLO_Yn70cBuyf81o8KtDVO-flPwJVm6k4cPVlhuyYs7KnKEJ5l_G7u_k8AaTvVUIuzcfxllBiLLbhLVD5JaC2MEPI1QBXpWJVMxbW7FSnt9YNlI_eKr4s05HCCPmN3u1an3AxIPql6A2L-GbqLSyPIs2v1S4N3nsui3-qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
استادیوم فیلادلفیا محل برگزاری بازی برزیل - هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/94567" target="_blank">📅 04:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بریم برا شروع بازی جذاب برزیل - هائیتی</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/94566" target="_blank">📅 04:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kE2yw-2CTe2eAiIbjXnz-tXPfY1hNtbiwxhkv9lOQYPvW1P7zZ43wFdEZjclQ5WtTEy25zbpyma8T73NWfbI4HkqbUqD3C9eJ1epPHUsXVEd2Li-9pRVej1mwDiKiy-1PNZ37Q7vVKNiWvH6SP2FHGCZGXOXqwr0RYBbrvUpk7RX5PCmCcuC4BvHfD5rsxJ_UIClp4mX42s_KxGHZ6F9CSPn-5oQWe7uB3QrBm0vkwt5Dv9FXIANLfHlgfOc10CrhJiW-pPUpDSxAcHFHaV2i9FcZcXt8YKpaBaKJtMNLyr98QSnLrP1U7g6F-TCRpQifjx2hth1PQg3knKnvjUFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین پسر
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/94565" target="_blank">📅 03:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KijJXyYysjpTtmTMyRYN2Cqq-am7VWlyjH_U56PPmMinTNdeyoz6WaUnqHjWfMS1QZeqXcDNdPe05IkIi-fZPDdW6Y8hjFfcEJ8wMzGpt0EawG1dCk0z30OkR8OLDP9IyqkIogoL_z6s5r1IYSW1G9Ht5eUI4Zx8s32a-5OnQ7uCQYzvo3EuXbo9hHlm7MCiNzrj9Old1pL5RzKlWDjf5ZN802_6qbZWdsKBxzXFTUctpCDT1ae1CjLdeKG_C_2dRQUI6q3_OZJLqlo3CtaNZfOjmpM24FFqA7Mp5SoM0WD1Ul1LReOryMzj3GO0H6LitzqFk2i5P6RVKf4UUJLIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراکش با عبور از برزیل و پرتغال به رنک 5 بهترین‌تیم‌های ملی جهان رسید
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/94564" target="_blank">📅 03:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEWva2fnKqLnTPuG59kQaRlbzve8L6ihFhyNNz3ybyOuIyigK2hrh2O1OVRgOBjHFBNIdzQDNUirq_cmilznW48DSDq508DHrY8tiIWvWCw2QNkdTtak9J1aRw0U2dvteHpCW71xMDKUd4bHpQMioBqHm4SbP9XukouIObpPP5TV4LrRz8g8FIRs1MGKKnVPNunw6RzjsQvBNSIXss_APBTXn5CIkA4TZ6lSTXV0WVT00I95corIMOj8ymLiStTudOAm27CWIeYKAyJgeJlMEQh11ViBCVqADeQTSXn7cwslH5K1DdxCE4UESW4ZSaiOPA2zKLnLqNkoInnNu8jAxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🏆
اسماعيل الصيباري مهاجم تیم ملی مراکش به عنوان بهترین بازیکن زمین انتخاب شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/94563" target="_blank">📅 03:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNnFHCj8bY2lRbSTwuXVwGpuzfKlHobK9zbMHn4xBBDb__mbfSEEYdnRjulMSMw9Vl2bBDmJ-QzMlbyljC3RYCmOMjrzV-dw8FdD8BopOWKcjiEDTTBAfmQG_NAyBHMd_32NyrtSStXVSdxQa6n-yGkAedV2g-LjaSupn4HM9nJUNYGzlAiqwS1VMbXnyf8J2oZv0Ez_r4RkN9R_SGfXZRBelc6_mU4mICzNydUFHYVKEtUXqNSmAo-eohp7klshwNwvC9zSWaWKcFt0U_B88UIqgJl2rl66OfPIv6mKGbw68D3uuIySNSMltOXm7DYL5yTYjFZO682SyvkS_u3s4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
طولانی‌ترین روند بدون شکست در تاریخ تیم‌های ملی:
🆕
🔥
‏۳۹ بازی —
🇲🇦
مراکش (۲۰۲۳ تا کنون)
‏
۳۷ بازی —
🇮🇹
ایتالیا (۲۰۱۸ تا ۲۰۲۱)
‏۳۶ بازی —
🇦🇷
آرژانتین (۲۰۱۹ تا ۲۰۲۲)
‏۳۵ بازی —
🇩🇿
الجزایر (۲۰۱۸ تا ۲۰۲۱)
‏۳۵ بازی —
🇪🇸
اسپانیا (۲۰۰۷ تا ۲۰۰۹)
‏۳۵ بازی —
🇧🇷
برزیل (۱۹۹۳ تا ۱۹۹۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/94562" target="_blank">📅 03:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Br82rIS7276EDoRsP-NqJoaoDiKkh7GucDnWPyJcOuxTWKP1sSb5UYfWd4QqYqG2UOyk4jlVPLS_tpnpqZ5G0XlxmwOJXCA3jCtsMTv5oCPArnvflBShko9-aWtQWnjZiFSxmS2m_8UISU5mJ4j7iL4LQ77HOpdg9nMhZL9KGgFu3kGJIvSTazrF80fh81noV6iDb1mnDNUnE6s9sh3L7uPPHBgfaFVcrVGFjmysj0vB7AloQqUoir-LqL1DDAt_FT03yFH_2ApOePqQdgkS-3yb4Vkq08n4rWuVigSnwV8QNc5i1KR0Wouhwdu-ipcRATrQkJtuH4IoitGOKnCFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه C جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/94561" target="_blank">📅 03:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDLT0qNaFNQJ_iqMgfnumJ2elv8B6TCbXNyMlDPGSR6BiMB0uH_SiJ1MnipyY2_SIskFJPoYrT5IuvaBiiJlIeDeImGRoBynahx3oiX2S7CsejzSrTIrDCf18ph2WLlH_6-DM9SIlWFLI8vshidmbkN-hqUGjKfD6uvYJ-aJhix0R-c3ccJhBDHXCgyCwcIvqPk-wPDKqfz0XnJgj6OMZzS3nIwN6ayMn3tik3av4BoPiL3_NDiAC-5fDuGUqtvY7LfG_ygmJ0qsKh5Q_ZEU6Sh4Nk_VQ0wR2Wyi5c9xhyN7YQykLqFftesSUD-0f8xvK8AoTX-13dHcxb4fM3QcyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|برد دشوار و مهم شیر های اطلس مقابل اسکاتلندی ها!
🇲🇦
مراکش
1️⃣
-
0️⃣
اسکاتلند
🏴󠁧󠁢󠁳󠁣󠁴󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/94560" target="_blank">📅 03:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94559">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCuCBtW-lNO724Cuonz5CuDq6ycW7muo8HGm1ZTZiop8C1iBOgjsp6N4phpYtVq1AAz9uMF14_4nMdxSbg8iCRDHP4xWU18xTetLshY5ox4aw-D_SNHPp5J9r7FLHizi5sG5GUgHNvaaZEzF4FtaC2m8Bqop1oS0VUWYcMKh04Sm-TExZYXaFmwDuHoXH2fURpVqE5DZ2PA4SgX_qV8wru3nCCX1z8UBQweDKZ5p1zXBICF8v2ZBV9aq2YMYPm7-4kh1etS20Wh97ycrQE-e5RrickkxUhXnUpIktseGnTLWiRNFbwT8KXx6_lhWla0ef8ps9koeUvud9oiMNXzYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
کامنت فنای رونالدو زیر پست ژوتا: روحت شاد ولی به رونالدو پاس بده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/94559" target="_blank">📅 03:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94558">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgoetFHEdTKbp9YH0WxRaHJ_ZgXpIX8Yk7JKKhvE79GUwNtmJgTVR23o5rVJzEvksrYvtUgvC4AtRhajexYacI_HgRP2_B7P9Z_-fy-YAkm5mGlSC_-leQX2X3W7SZ8Kujrl0Bq_VYLwdff8bpEyge6j74h5zoa1hwDem8L0ZyyntjQyi9BcEcX1Ju44qiiBc5-W9MatqIRO_D6ASq9gyefbMW4Sl7ICyALEjR4MKU8o54zwlZt-_d7pqz5D7QVFdiqujBHNC_HQGaKF_IoJIofCvWo7_iweObTeI4APiZMKDGX2SMmL1M7uuLXKw23bReTJokGMDv2i6ZTDfrkyow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکاری دیگر از پوما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/94558" target="_blank">📅 03:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94557">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">قلعه‌نویی که تصمیم گرفته بود روزبه چشمی مصدوم رو با خودش به جام‌جهانی ببره، ظاهرا تو بازی بلژیک هم غایبه تا شاهکار دلالی اردشیر بیش از پیش نمایان بشه
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/94557" target="_blank">📅 03:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94556">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-bTTFjrsAcQIw7G9NcjhgQwicPFH97lBuR90sgUTr5bCjVc-aEZapiM906dBjY4KGKYpEmkvkf0-e4fEI05JG_YSinyRXPd3Ul8PoVxziXS4RHd3xno-Rye67ml0THBtJt01i6qHI7y6Peq2YFcgsEAQBzV88ihj1xnf6onV2NUCNdQP-zp4uqPW0uyT2pw8mValfCnucOfP72CVkId8uuqLedDMF2gLF_Yi42QYJEjxNrYHKHqELIbSeUALDx82s3xlCJouDjoiphTAndrS3oUorZ3cfY8bp25mxO-xobTiVwJQGcqp2uiclzEqRRkZV8mvGRe3YNms6bUWt4p4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
#منهای_ورزش
؛ مجله تی‌سی کندلر در رده‌بندی زیباترین زنان جهان در سال ۲۰۲۶، نام کیمیا حسینی بانوی ایرانی رو در بین ۱۰ نفر برتر قرار داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/94556" target="_blank">📅 02:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94555">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGukqbPPlxsfNIw-G34ydr4Q9El4fxJAQkOsLBe9WVaGya-36OJqnFTTc16p_ZFvDYlIPhiE1QejARzaeqzxHOWfErQ-fjB1Ytm6bItsu2sWoZqlfl1N9apG1qZfyXrAWdp9nXXzyPwrnEdU2vyD3kGDZSeEcoof_KubvueER3Q_6DkpbK8w0vsvTWabNT-QkLG4qeuEmCfiMnYoBzMWsr7TVgqJ-Kyo2inftADziEwhljNX3NDq_cjzghvGh--ShO6FU4iPr2iJ1POLQnZIwwfwy0nlhAmBefA2FXDch-cHM9zaVEQGCb_Ybou67gcnlzFEUBUkV3L-1KFKo0P_sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل هائیتی؛ 04:00
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/94555" target="_blank">📅 02:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94554">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a5a95aac0.mp4?token=ohu6TM5Nkt59oIQdO-ZjMl4cCC8FylDSHYyppSquIB4aZE3p_1AEXGuKOqG8PK99XHArETch0KzruhYkox8Xyu6p08xaAPIi1epLzj8qG7815FbpD8pmw9YX7gfcNrZ38KxDJdw_TLRW4lZ2oB9KY-jt6hz-JL0DOlFOTGahFNgGBAUl4po01XgScztZgeOunRJWhE9PgJl6z7g59hO0x2Y9j22jh4gnqRNBzjiwttZ8DILCZaT4HHhikDdUXW_tUJWd391uwk27h4hmGlZGfxWoLfGFFY65eOc-of1P8LtdhMDCze_hXy5JvvBa0QWbrbfX-tlKz5PbNclZl0GldQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a5a95aac0.mp4?token=ohu6TM5Nkt59oIQdO-ZjMl4cCC8FylDSHYyppSquIB4aZE3p_1AEXGuKOqG8PK99XHArETch0KzruhYkox8Xyu6p08xaAPIi1epLzj8qG7815FbpD8pmw9YX7gfcNrZ38KxDJdw_TLRW4lZ2oB9KY-jt6hz-JL0DOlFOTGahFNgGBAUl4po01XgScztZgeOunRJWhE9PgJl6z7g59hO0x2Y9j22jh4gnqRNBzjiwttZ8DILCZaT4HHhikDdUXW_tUJWd391uwk27h4hmGlZGfxWoLfGFFY65eOc-of1P8LtdhMDCze_hXy5JvvBa0QWbrbfX-tlKz5PbNclZl0GldQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇺🇸
نمایی‌دیگر از پرواز بالگردهای ارتش آمریکا بر فراز استادیوم‌ محل برگزاری بازی‌امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/94554" target="_blank">📅 02:31 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94553">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پایان نیمه‌اول با برتری مراکش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/Futball180TV/94553" target="_blank">📅 02:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94552">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25cfcc20c6.mp4?token=gQZjjnbp7PZClIR1fqrcewMH9NIiDTm-4c9qmFV4_lKDvETQw4ytj88M2gFb9IAG8N2R9-WWMLedXqUFTGfiLkFX6YZ54fufnn_ZwD8MlYJiVGGUUpeSO-mFArcIXTkFRHZhWFrkm1m3EQ2cDLlW4p92pNZoh5XhHpBANrheNCNKt832SFiK-TA-twzQLlhRHcuSkO8NlafgFSJQhreLRqI2xHA1Hxg-s6uLR1yn-s7JNQh-YvfaHRQqMK4V9evbNhlwCBJcNw90dfHsVve7Wop6jxtZTQelHeIfFQ0xHUv59397rp5GrAbiT1GqRE6iNwHy-knTqrYf62PKVhdX3FvYgxHdQ8hl1aeLeVAEHRjy5JOZaFi1oLzADDYaofMNWX15mIgZB0IBIuQYPufvkMhzJesE7c6fJfRJ8K1fiZ-znpm4SbvTx5w_IDBBSPP5qEJMXLlbeKF8HMgdMcnPZ_tCWqjMUGNRyWdMTX0h2LKOmhvC4h8-SOeCAEuePb_iWZxuidkljdneNgu_sMa6qy6JDXVM1ENi6jKuGjBT5fCsWdxXCJIrbtRTTJWLaB7DkfjwIkv-HGss1NcjMDV9MrO_3laWOb42abvmE8aKDRUkD_kvGY5RddRbon6DdbQcDt6mRtoOgySoH68cv6_kvC02Ny_1D8w65qg-7vSJ_1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25cfcc20c6.mp4?token=gQZjjnbp7PZClIR1fqrcewMH9NIiDTm-4c9qmFV4_lKDvETQw4ytj88M2gFb9IAG8N2R9-WWMLedXqUFTGfiLkFX6YZ54fufnn_ZwD8MlYJiVGGUUpeSO-mFArcIXTkFRHZhWFrkm1m3EQ2cDLlW4p92pNZoh5XhHpBANrheNCNKt832SFiK-TA-twzQLlhRHcuSkO8NlafgFSJQhreLRqI2xHA1Hxg-s6uLR1yn-s7JNQh-YvfaHRQqMK4V9evbNhlwCBJcNw90dfHsVve7Wop6jxtZTQelHeIfFQ0xHUv59397rp5GrAbiT1GqRE6iNwHy-knTqrYf62PKVhdX3FvYgxHdQ8hl1aeLeVAEHRjy5JOZaFi1oLzADDYaofMNWX15mIgZB0IBIuQYPufvkMhzJesE7c6fJfRJ8K1fiZ-znpm4SbvTx5w_IDBBSPP5qEJMXLlbeKF8HMgdMcnPZ_tCWqjMUGNRyWdMTX0h2LKOmhvC4h8-SOeCAEuePb_iWZxuidkljdneNgu_sMa6qy6JDXVM1ENi6jKuGjBT5fCsWdxXCJIrbtRTTJWLaB7DkfjwIkv-HGss1NcjMDV9MrO_3laWOb42abvmE8aKDRUkD_kvGY5RddRbon6DdbQcDt6mRtoOgySoH68cv6_kvC02Ny_1D8w65qg-7vSJ_1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
واکنش یه هوادار مراکشی بعد گلزنی کشورش به اسکاتلند مقابل دوتا در و داف طرفدار رقیب
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/Futball180TV/94552" target="_blank">📅 01:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94551">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f84c4794.mp4?token=iD2522yOudHoz2xerDrBSfWLhycLdzDKRm2Zo7cY2ioFblAwSDTifcvr5EK-_B2fl888dvtl3xhINivKR6h0koNtDXdlkgp8me4i4oN_a5_YdKJJbZGO1cwaJ5yrI06HI15ZyV6Y7HbzSKwjx5jI7TkvXNuzaeocx6OE8hSpKwcRY2-6w4Vx18Bny5NKXb7WCj1xgNd07EDfXnIKkrycuTrk8Tw2Xe66vAi__vZgk2dIKunvjQYpVzIrOJzT3BhR7nsmrnNZb5jlQ8Z7BaFMO5Gm9XXSNx8LNFqz1AVVdHu9Avdbol9l3HsZnqeB95_aO_dnZSzMjlPKMtNuohoGr6LZ6mk2ni61NCEsTtt_GhVjTKe90mFdpJAtnvtChgL3-VSvhWQwP_LdobuCQ5avyjm8wwkvQCKE3wLET3L0xMQhI2n0eD3PL5mWvVXdc9p37IlIyhHozFoVFMUJfBFkxqth1ZNeKkA0h_FmonOBkGq3nZ71N_VWaJL6bctT7bJjtxn-m_4kVGSzm_dsTKbQCFWj82bPwivy4lg_RjLj_hRcVv3Glq8u6rBQyHeKdihFbnP4-vXil87hdljImrpE-7aXKPHs9ZIkbVQqELZ1t0P6UuuFivJ1GaBrH8Ny6S-RruAb5G8kb9c7J6TeSTjX9wakVG0cLLaTK-WhP-6MUm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f84c4794.mp4?token=iD2522yOudHoz2xerDrBSfWLhycLdzDKRm2Zo7cY2ioFblAwSDTifcvr5EK-_B2fl888dvtl3xhINivKR6h0koNtDXdlkgp8me4i4oN_a5_YdKJJbZGO1cwaJ5yrI06HI15ZyV6Y7HbzSKwjx5jI7TkvXNuzaeocx6OE8hSpKwcRY2-6w4Vx18Bny5NKXb7WCj1xgNd07EDfXnIKkrycuTrk8Tw2Xe66vAi__vZgk2dIKunvjQYpVzIrOJzT3BhR7nsmrnNZb5jlQ8Z7BaFMO5Gm9XXSNx8LNFqz1AVVdHu9Avdbol9l3HsZnqeB95_aO_dnZSzMjlPKMtNuohoGr6LZ6mk2ni61NCEsTtt_GhVjTKe90mFdpJAtnvtChgL3-VSvhWQwP_LdobuCQ5avyjm8wwkvQCKE3wLET3L0xMQhI2n0eD3PL5mWvVXdc9p37IlIyhHozFoVFMUJfBFkxqth1ZNeKkA0h_FmonOBkGq3nZ71N_VWaJL6bctT7bJjtxn-m_4kVGSzm_dsTKbQCFWj82bPwivy4lg_RjLj_hRcVv3Glq8u6rBQyHeKdihFbnP4-vXil87hdljImrpE-7aXKPHs9ZIkbVQqELZ1t0P6UuuFivJ1GaBrH8Ny6S-RruAb5G8kb9c7J6TeSTjX9wakVG0cLLaTK-WhP-6MUm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🇺🇸
پرواز بالگردهای نظامی آمریکا حین بازی امشب با استرالیا و ذوق‌زدگی جالب تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/Futball180TV/94551" target="_blank">📅 01:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94550">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb8Vb9ueSHOnR26-FIWiLXamzEdKmriSR2GRU0poXT_814C9zgSUxUGIW_rj6RNFBsG8tpjPvukyX94tAfINX9hHvQXEocwXyCH69n7ddE4Dxuu83_gFcvqgRxhPQsvtWZaPHAe6y7G5DdiUBlMSRjEmLo0LLaw8nApQSvepjjRci5CKw5OiKpmL0jd6RKG96T9GijE1vqu0x14-hJJ_9XQRbpFAgJrS8JtT_v6f9jLxCs8SBrL4E-4y0qy7qe9pOjSK4nMWfFjo8SicyKZtalAnQ3H8J_OD5dzjAFpv6WW8ZS3-qFzsaG7jM2gKbdEElzUGrDjdAQSoL4TqG9zQhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل‌اسماعیل سایباری سریعترین گل جام‌جهانی ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/Futball180TV/94550" target="_blank">📅 01:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94549">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ceedb0fae.mp4?token=spPATADoTMAb8swq0jAneoihYDa7mCDfB-voe3Hbw9czOK075lJjYDMjTDdHf2k8saSmYmqg0JdpGzrRvArVSJWP92xlJuaoN--w-GJnvWyrjbzhJn8OSO6w_mkIHoAVrFmKWcjFDw4rHg460yub9TZP55s-S2tdUALSs7byoxLM-F9AUCy-Nz016jgE8Grw-5Vs822URMTUjAKfyglVgL681NLVazHWkkuLqklyrThyp6DCSLfOHpAGPqTB9w6A606q2SMrFKbzWdtjL4sicLtRkwt9W0e2oa58q4mXK8FeJejWxpG4v-BcBKecunVX0ScUsrcNzwJ9Gu0oE0pJ4QH2FkDM250jiZsj2Z8iQkaUnV_2v6r453G0uCBZp2o6SScsohn4y3biiFCT0w8Nrpw7hYgujHGuGL2c5zhhxO7Frdsjok_gRikdSpIexcv3mSHzzcinD-x9gzB1Svl4ib47MGYAULoUGm32ewtxond2W9dsx8AvlHlx-DybRMkpxmqf48fAyPy-WasCtEJ0LrVKXaGebH2-8wuypXhYc1SFFQX7vMJHBh7EcVeyBNxa1MqjMTWhpD7fr0lEl_8xeLlQqZKd9kUfH32_MnLo_-wPwr_1jOvqGoiDU1YTx0XGqObJdSlnohgyY1a5AnwVB_SVxr5U0oEjgXvS8U-kMU8" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ceedb0fae.mp4?token=spPATADoTMAb8swq0jAneoihYDa7mCDfB-voe3Hbw9czOK075lJjYDMjTDdHf2k8saSmYmqg0JdpGzrRvArVSJWP92xlJuaoN--w-GJnvWyrjbzhJn8OSO6w_mkIHoAVrFmKWcjFDw4rHg460yub9TZP55s-S2tdUALSs7byoxLM-F9AUCy-Nz016jgE8Grw-5Vs822URMTUjAKfyglVgL681NLVazHWkkuLqklyrThyp6DCSLfOHpAGPqTB9w6A606q2SMrFKbzWdtjL4sicLtRkwt9W0e2oa58q4mXK8FeJejWxpG4v-BcBKecunVX0ScUsrcNzwJ9Gu0oE0pJ4QH2FkDM250jiZsj2Z8iQkaUnV_2v6r453G0uCBZp2o6SScsohn4y3biiFCT0w8Nrpw7hYgujHGuGL2c5zhhxO7Frdsjok_gRikdSpIexcv3mSHzzcinD-x9gzB1Svl4ib47MGYAULoUGm32ewtxond2W9dsx8AvlHlx-DybRMkpxmqf48fAyPy-WasCtEJ0LrVKXaGebH2-8wuypXhYc1SFFQX7vMJHBh7EcVeyBNxa1MqjMTWhpD7fr0lEl_8xeLlQqZKd9kUfH32_MnLo_-wPwr_1jOvqGoiDU1YTx0XGqObJdSlnohgyY1a5AnwVB_SVxr5U0oEjgXvS8U-kMU8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇲🇦
گل‌اول مراکش به اسکاتلند توسط سایباری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/Futball180TV/94549" target="_blank">📅 01:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94548">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">مراکش همین اول کارییییی زددددد</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/Futball180TV/94548" target="_blank">📅 01:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94547">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گلگلگلگلگل</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/Futball180TV/94547" target="_blank">📅 01:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94546">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">کم کم بریم سراغ بازی حساس امشب</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/Futball180TV/94546" target="_blank">📅 01:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94545">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPQLMqwxT4jMMcCM4Msts9JyU6EYQ2jFfuS0_D9YNt4kITSi_4448Y4oirq-eoC23r9cMRXeN26Myv8nGF9hMqt5BEUq64q4ofExCyCzUxqdFj1jFpM3gSIfzA_kbQyMS9noQaGi0jwtDg8gwpRC8eVB_mvi4N1mgStlsQPzv2D2VOfsuHIfEnmctAoIIumlhIKavGjZlcV2j-2-2n-1eTUf3KilYiO2B3B2t2cQZI8bj3jl8R9XCU4DoE69eFs4p0K7CKG5_OyOZ3TdtUpSKShoFZPsloQzFXzKhaBi1akZ4e8IgVPUASJowxq8-JOTKZ6xoFO3DEOoYKyi3Sq93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇳
تیم ملی سنگال از مشکلات متعددی رنج می‌برد: پرداخت نشدن حقوق بازیکنان، انتخاب نامناسب هتل، برخی از بازیکنان به دلیل کیفیت پایین غذا مجبور به سفارش غذا از خارج از هتل می‌شوند و سرمربی این تیم چند ماه است که بدون قرارداد و دستمزد کار میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/Futball180TV/94545" target="_blank">📅 01:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94544">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🇮🇹
👀
یه‌سری منابع خبری مدعی شدن که رونالدینیو تصمیم گرفته به فوتبال برگرده و‌ میخواد تو تیمی از لیگ‌سه ایتالیا فوتبال بازی کنه. باید دید رنگ‌و‌بوی واقعیت میگیره این خبر یا نه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/Futball180TV/94544" target="_blank">📅 01:07 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94543">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XteLQTn_OEc9KTVpGcoYlhXEUcOUJnSxXGA9ObLQafO0VzoiIcxRNuriyW8aGGPCMcoca6XoFsp49YtC695Jq7I9gEuApofrozHqlcnUazlWT7tnzLvbviZUXUS1A6d8iXrOfaZ3ZX3KGfU_kFchUp2m0GdTopf6aKhIeedcdD8iNQHm7XqB0YT17pJye1FrUQ1vRwJLvWZb63ILrkjwYXCBRJ2H7j7H2VUOWQeEQhj2Aw22yuOVXrKwy5MmkokhmcfDEpe-mq6ig_Z-jfrK3h8W8c18f5AJjgl2pUIIq5O-QOU5e9GoLIYJLHJ2Iv6xP6p1DpUxmM33N_XRWlkrPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووری
از فابریزیو رومانو؛ کانگ‌لی بازیکن پاری‌سن‌ژرمن مورد توجه اتلتیکومادرید قرار گرفته. بازیکن با باشگاه به توافق شخصی رسیده ولی مذاکرات بین دو باشگاه در روزهای آینده آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/Futball180TV/94543" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94542">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuARCvV8wKHsO8bkug_TV6edt2FaVgrnQKx7eN1H0iOef44R1fsHp3ym6Fn6Hfjf6OCmZb_rXAh8PVkXq9DV9jFml1iodyi3DOMXLLeh6tCgSy47aF5ioNRAS1Uw5JQo-XoRe3kxhWLIlsFK7Ueivztnr5Za5jzRQKQfehZRqCrlmBx5BrcBiZjySvIzNW7YlcQvxOfkHGQlrmEWyQJSgaxziIB9KpwDq5gHbGS_yYEgewd23BUPf5nDiOFrxIaoHK_EWrzgCMt5AwfkbcY89ExFOCYdkuzrZrWMtiF0xxO53wwNmvo2O4dojHBhNJEK2kttC_dN292PgU64RRMdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
طبق گفته رسانه های انگلیسی مارکوس رشفورد از ناحیه کون مصدوم شده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/94542" target="_blank">📅 00:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94541">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jysNcZ-cwrQBgZnHQX1NDbvQ-vKkNP77BYtgdQySA2VnNLKCMNUDShwvmBFfmxPioIxyucnMtz5vnSm_81-JZ7bIEtkqCmgqnuLH2AEdaDEXqfJky1q_4GvuQlDq6413v3frQMNGgR_hQx3HPwAt_IWLxoc66aUiotkiqFe_Q8ClDw9FrfK-MXi0Vjb7PMurzWCH34R7VVaXrNNIMOfeMNYX8vcLd4cIyitmOjvQXM-DdxWKUwVI6dVHyjTttYx2xEKFz03y7u1-MLFm9179eBOUcoIvJez-F6MjqvFDSzaEmknPB2s23BSvvhBKmrevHs8DaQMtwtEeREEkmNyATQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
📊
تیم ملی آمریکا تنها یک بازی از ۱۱ بازی آخر خود در مرحله گروهی جام جهانی رو باخته و اون هم مقابل آلمان در نسخه ۲۰۱۴ با نتیجه ۱-۰ بود.
✔️
۵ پیروزی
🤝
۵ تساوی
❌
۱ شکست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/94541" target="_blank">📅 00:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94540">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvNOha6om5oUuekLMZkdpQUu-LVdL3_DKz4xKx4NQixh3Q5oLDSbG5mHB6tFM-C4oym2vuO5XreJppqm80bSgX0KTyx4m4vkrW_87v6STKU5y5mR-ALznJfD-1cDMpq7CjSBcaR79ZgbKVOd3DnVux4oE3d_eEQQHISGH3T6eyVf-IxOdzHr9j_jHHjGNbD4nrwPszn9kydSaITDz36seFsYFlTbkdgkGje4eQHR3BP2idwruWrVNoV72Gf9KdnyhrjKyTPGnaYG0DodBoQpSi7L5Kv6_pIpme9k2FTE3wzFgrTIChDO5NRejZbBdc4xc95fwrs9cn6_4_CjwaSnhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
بالوگون مهاجم تیم ملی آمریکا به عنوان بهترین بازیکن زمین انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/94540" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94539">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">✅
🔴
فقط نظاره گر فوتبال نباش پیش بینی کن و پول دربیار
💵
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/94539" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94538">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSUaLqt9QY46kteK_4nZ4zldry7R8Wq0a7QnFFsAimBP7azW4TflKf02Bjc7UrEdabxFXxZFIR_xYGXW906c_XO2lQrcQCuR3U8uqt4V9D6mz5bT8fsQ86_UJ4Ddn0RG8irGgNAcf5wVH-uEOcBHKNP1Rjw1ejel3QurAeLeBp3XAqMk5Uo2fFfg-TEFsGD2n7NY7OUeweYLh-N1XTbQDXkKK6EtU5qp_29TIB7a8CHYZcjiaAQEudZ3l5fD-lh1qXYZ0t0XHSaeH6eWS-nn3HfA8vjElCm2-wyFLq0W4gkBbbWaS3R3bdBCA-8ZN_3CtnTr1YBY6txmenOytBKOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/94538" target="_blank">📅 00:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94537">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JumKMszzPwMDVuad2-VvuoXOfJkYpsufL1rfdO-2z927_X53ZlsjZl53NDD1ueRaWvFLTgCkw95Vj_zxlt5_6lKHO0k_qypSD_P4YvWByCBSkR8zNs9Q7XqNVyPuZ483TuABe0Py2o8J4jyxVxRrOxS4euTxt4Abi8k7ivhsxOnosPq-VC9FKN6BrzML9a6WurU8Rlo71-BGW_yEfgcNyo3tqnLfX5zHY4hqgnJyyjanNDE5Nd1g1_S8y1Lh8X1Hfewa69fnhQqSUVdVweIncartvhBLc2Xb6O_hGHTVB7oNSODq9c4281qkc9QbviBcBPURl_FK9uzHGIcVQn0pxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی گروه D جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/94537" target="_blank">📅 00:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94536">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BIm1BEnXKcwNE3OvhSb-8Nsc_iqp8uioNNlvDKEtr8YFDm7FGL8gNUod0VjD5KDavKozWmKvDaNOhwWdcLT1Qk-slzt8dlpI9imxoU4Hv8SGDrjZBIOyCaMO8Oc2waX4yTinn_Ych8iGJK8C9SBEKet3OSGtAeknRWq5ErYihA6L0uwzJj7EH0sc237bkrZhy4QKHFjac76LxWSbuXyWHc8AieQGrcnUCSu6KXSEL211HjjWGNcu8gIzp-BtCnInoBtmGbs_WmP2c_8BzVsUrXOxbS7P8GRYJXHdqsSYrcX1pTWg4it11BaQOIPG8SqcT5pnww2rz5ASkkKbscx67g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داور مصدوم شد</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/94536" target="_blank">📅 00:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94535">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqXktpP-zgLUtcT52xFmmhx9D3dSAJP4NvdNJa4Y_UtDrqSmdTwP0aJ_SYlfWMrIPJEnTzHxTrD12S80WBHpINRFXWz5MeIqgZYVp5HL7swlf0mf5g9kBhRZ4ZAQHX1Ai6m1MbiSC8qbAwqwYswS08NrMUrO3k0B-cuA_m7_vVpO0KhwfMkSPF6OVMR7uqfHmn5I2kOLXO-txh1K_rW9tyWAChRFNquhwU9ZC-zK4-OY03CyTdHbmcVU-QhORQS4bZ23CVQWIpf85EOMm3fPhfuECGuUrrpH8Ap4T-eyKsFYHGXMjkhOtfY4uWi9l71W4U04SfOltzJL_9g_ssmrmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🚨
تیم ملی آمریکا هم به عنوان دومین تیم به مرحله حذفی جام جهانی ۲۰۲۶ صعود کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/94535" target="_blank">📅 00:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94534">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tD62-mRDQc-GaqSJxuISCvco9QZZXaaXdJYOg1EXBoYRXDuWNMYxwewhJBIOl5U7KYuavCBrTrA60xtSwT3Iyv-Yoxoe_37pxN40ekoMKNo3D-G2mmSNQ5UTgMGyKHm_VstLI6JcPGAXrpBt-q44ZqKXfIx1OArxIuL2MP0xrbpgqksX3xAec7mM2Dl2ZgNVWSduhIkwwxzqPOF2h6a_zuXNElDx3C7_5l3xAXTw3POAIDerm1EvkAMVDoJ2s7oNu-MUa9cxlZ2TICKZURGrT6Yt_OUcldzr-FlqVRHyKLpjChiEsVVZrFbFsalisaCOCwrAWT5q2sRhls1NwsPDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|نمایش برتر آمریکا؛ کانگوروها دست خالی زمین را ترک کردند.
🇺🇸
آمریکا
😀
-
😏
ا
سترالیا
🇦🇺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/94534" target="_blank">📅 00:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94533">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">داور مصدوم شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/94533" target="_blank">📅 00:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-94532">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/94532" target="_blank">📅 00:26 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
