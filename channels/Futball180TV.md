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
<img src="https://cdn5.telesco.pe/file/CH1tcVEJret5meoBP-vGYlqORPKg7tV7eRGo4e48DFhlV0SOS_OnuaK7y2Ji0TzslvxCtA3Z8mJodGOXqxai-QQhqhq64yDrvvZ2-BdMZKaieE4xDT1-fc67mOiEIdV_D5EH3ngQoaZJVGJ2xb178UfSmNLGRoS57E7nkF_gu_fXLWQOdDrASiiieC6wSZsNlSMxMqfoC8zNSR2fz-EkO5C25D1UeCWwI-sG0X71vUCgFDCkTc07C9MYKF2KGgFtywwZLzrrZCxNNbxStRMHeJAZro_MqhFrsifixFO09fAcSUnsnB39xPdooZzbXcblnLD1-A5WfCYb826UTzyVBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 242K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 16:26:06</div>
<hr>

<div class="tg-post" id="msg-91302">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7bOGioyTcjyA1UGJAbkwLd-Ogh_JeQFgJOx6VmGL0Urck8LmwWXIWt3kHOqV1NV_sm6qJCY8NuuoJszKg6tgG6FK2cJlDwaJ0aeYVXj9TEUkdpMvesptBgf-qoxNJ1adcceHrT2ERSWjCEcF1JLpHC6fGglpcnfu5zqWTN9Kjt4x-MtBtDrBeX5Np-DT6ssi92lm3eYHDf3WXLhL-rjglXO-oVyMtbQMV9WVl4kdjOmlFpFscXDXfqDd_Jhdr5KZ7QqIV1B0wA4efXzMSvxiyOfOuE0XHlDeAJfWApZkQCuB_PLQ2djJJL8TFNMRInsCtd8sW6XjUJSrXWnOCp_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیت‌های سکسی پرتغال مناسب برای انواع و اقسام مراسم‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/91302" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91301">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=jsb-DO6po5VnN4nMXISZuSrMynrScyLF_j_x7qIoP40aJCxKDUO2NpVfx3YtwaVBN7qcVLMY9eLtXosCn7FWPl55njnnhMTa096iFJHgSvbpkrpxLMg62AiMpusLN9L9v1KfdXlHNMwaQ3BRxa3OlYuwkNlDeubbcNl1osEYvvyZMZM3glcMY9BYyW3ICkpUdppEv2XRh3K9qTPjfAIowsHD8ZiV-nEPfwzcLaW8LxZok_RkBfPiwGTPiOqui7ZCMTeNulw533H_4KcQ16oK5jJ8S_dv3h2iWTdyQHyJop5AguS2iuz-b4nY7Z_xd8IfxaTsCnwOKYzdE6knXcKLpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcfec576e.mp4?token=jsb-DO6po5VnN4nMXISZuSrMynrScyLF_j_x7qIoP40aJCxKDUO2NpVfx3YtwaVBN7qcVLMY9eLtXosCn7FWPl55njnnhMTa096iFJHgSvbpkrpxLMg62AiMpusLN9L9v1KfdXlHNMwaQ3BRxa3OlYuwkNlDeubbcNl1osEYvvyZMZM3glcMY9BYyW3ICkpUdppEv2XRh3K9qTPjfAIowsHD8ZiV-nEPfwzcLaW8LxZok_RkBfPiwGTPiOqui7ZCMTeNulw533H_4KcQ16oK5jJ8S_dv3h2iWTdyQHyJop5AguS2iuz-b4nY7Z_xd8IfxaTsCnwOKYzdE6knXcKLpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
شیث‌رضایی مدافع سابق پرسپولیس: در دربی معروف آی‌بدو آی‌بدو، علی‌دایی تقصیر باخت رو گردن من انداخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.14K · <a href="https://t.me/Futball180TV/91301" target="_blank">📅 16:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91300">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=sWwwfXi_naZcJRCh7XFoQr4EaxmmEhCo7xrRF7C8ZsbURERhaLDlHhAV33C7FVZKC3Ctku0THEkgIWIL7BEXHjC80mrDYDbgxpn-ocUug4ALCUlSp1XWwZVFlQ8vqsy3k9PdnyfolShy1JO4lES4_VYG7JmydJHaOh7ntD6KYYV6gx51EjHmyati36QYGqIBgGZLfjWeUWliry7a626ZnbPF1_rgwKD2LIbtNRJ0oj4iWEKQqNUUu53i9NERa0DJp7FuXhaTrlioONOxERJYEtMOxGjuIGUOmVPL_ZJb0l5yDOd6EX8zVoEryi-DP8VvbtTtX53Nyg3iScn8ucLqlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9db9b67547.mp4?token=sWwwfXi_naZcJRCh7XFoQr4EaxmmEhCo7xrRF7C8ZsbURERhaLDlHhAV33C7FVZKC3Ctku0THEkgIWIL7BEXHjC80mrDYDbgxpn-ocUug4ALCUlSp1XWwZVFlQ8vqsy3k9PdnyfolShy1JO4lES4_VYG7JmydJHaOh7ntD6KYYV6gx51EjHmyati36QYGqIBgGZLfjWeUWliry7a626ZnbPF1_rgwKD2LIbtNRJ0oj4iWEKQqNUUu53i9NERa0DJp7FuXhaTrlioONOxERJYEtMOxGjuIGUOmVPL_ZJb0l5yDOd6EX8zVoEryi-DP8VvbtTtX53Nyg3iScn8ucLqlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🙂
تنها چالشی که واسه تیم‌قلعه‌نویی ساختن و پسند همه مردم ایرانه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/Futball180TV/91300" target="_blank">📅 16:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91299">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcJkMuepDCQxH56mu-bX1vOMnqklHmK3dkCPjWJM0fBMLERnfZg1uqQA0UDh7GzOmBcjvIzBQoypfUpHN9PBj9Bp9nHaL7qmxMDG1ZfdOxsQg0sl-Z47-P11Lv4ma8At5h7OT-Igfw0hFKwX7QLzDOC9IhcbjxJ6f2BS8gDug1sP_KC1-GmEDliPk0zQC70a30zzC9U9RD5bYxDA-Ebrmrk73YTZ1r0XA9Uc0FVs_2OlHibgs9FQELsVqUKoHRhpZ8kMEouqlS4bZec956cDPJVnugoOsBQh_LrD90_llr9-JeSPi0zwyR2UeUZwe_28dzAqN_ndBNU470ToYA2nGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای فرانسه دیگه بیخیال رایان چرکی نمیشن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/91299" target="_blank">📅 15:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91298">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EjDYBYu5CXu56aYMkGV0nj6TRePV1EYtVmvPHglXoC0QRiG2xIXCYLfclXyui9CGRJmTfsqYvDS8EFg9ZlqvsHTP9unQpHV-h1HgiEGQnxrG_9v-JRTOZZyx--MorKUUwY46iBUy7VBxg6MIUR8iKkcF4Cke1REj6SttxWRpVN17Ldi3pX7aBvBGeidsbge1R3dkjwRG21yBoPfV3AQYeMZm3JwUWgYmluDyme-nEaeayyk68YnCzg_ayCma7HyAv0GMONdERiaBdvEAvzSqhXHLcYsdHZsHQcdgoJrmIS2qQUSSFUHeB_T2qd2Z8lZDXilLo_Sc-3JhmcPce6WMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمیز از نظر پسرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/Futball180TV/91298" target="_blank">📅 15:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91297">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nBEBtGH5vkGB99XhGdGvxczYLgstdujaREWncObVP0zlSqZRKnMaDOkAt77DRntnDav0_sq-QTomK-CYoJi8wivKWk0kN5EaxYZJbhMhC3RWOAQfu4Tv5zFpoWsuZ9wUFYpgMesfE-w6nkSfTjHEEE1Brcb1DLYeYvLjY6g603p3xRWnHIVnAAs82CfnO6oMCzEr-VGe5zFQErt8Tg-vXPDMQzKW23dOKMq6dTTKls1Z73qLCuKcW9RWtsUeea2U8t5oY_4kFPyNUk9hWBleFDIJE_ryD_DuipMSiZ_Y3KFvkvjO3_C1hgjvg3m-QffSqnUI415bFXn-LhSYmOWVCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c920142fb.mp4?token=nBEBtGH5vkGB99XhGdGvxczYLgstdujaREWncObVP0zlSqZRKnMaDOkAt77DRntnDav0_sq-QTomK-CYoJi8wivKWk0kN5EaxYZJbhMhC3RWOAQfu4Tv5zFpoWsuZ9wUFYpgMesfE-w6nkSfTjHEEE1Brcb1DLYeYvLjY6g603p3xRWnHIVnAAs82CfnO6oMCzEr-VGe5zFQErt8Tg-vXPDMQzKW23dOKMq6dTTKls1Z73qLCuKcW9RWtsUeea2U8t5oY_4kFPyNUk9hWBleFDIJE_ryD_DuipMSiZ_Y3KFvkvjO3_C1hgjvg3m-QffSqnUI415bFXn-LhSYmOWVCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه نفر تو ایالت هرات که ادعای پیامبری میکرد، این شکلی توسط طالبان بازداشت شده
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/Futball180TV/91297" target="_blank">📅 15:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91296">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeAFcVZhgybxxA_CqFgzeu6OLwNwvgih385HFkprbIgVT8H6MC3DDldLfQ2ubfIhd1ahTkaq8k5DYBj3EQNNFPxNN-ZF9hintf96wpVcCSJq_Uat0e3WXv1NQ2YKvO-tkSpwBHd8-pjjfFRVeFKanFpgJQXFMr_E5vkhWMBUWjnZCi0WYM8uuAz6WomQFAiQ7oEMGalSaVGY7PdaFbgftoroEYpWpnzb3htKn-x-R82vuqDs8k9obPQg0xwHtA-QcQra2K-L__nnJTHvRbcsMkekCwNJqQKGEw9OxHyWQG3srfG7pbt3ghqOZUdui-EQIz1xIatc70Q0-d7uSsYd3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 7
🇺🇸
استادیوم آتلانتا (Mercedes-Benz Stadium):
🔴
موقعیت: آتلانتا، جورجیا
🔴
افتتاح: ۲۰۱۷
🔴
ظرفیت: حدود ۶۷ هزار
🔴
سقف متحرک به شکل گلبرگ‌های گل
🔴
یکی از زیباترین طراحی‌های ورزشی مدرن
🔴
صفحه نمایش دایره‌ای عظیم ۳۶۰ درجه اطراف…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91296" target="_blank">📅 15:12 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91295">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Onay55DZDmx20RsuJ-vX8V-q4Qq8Uhgs_odbFAWGUbqZoVvWHRzn7caTwsC7PvnLcwAzRxjNEwhg-vM__KOjDknvEa3Sl6R2Y-O1LjWXwoNdk8cBJ_In75ZBPWDAxziGVEJuuHFza0C7l6JyiSC5Y298ez-u8x12gvR2u1aDAMmRHdxP3Mz5VUEQD18-yIlcpqTQp5rSHCj1C2SoPPa5N7h5_05NSLHa0HA_8t2Ibw6c6WrT9aRme4ayhJWvAMum0u3BqVK_n7n6TDzWWDfCmkW6PAXffjhPoibR0E6HCnyBwBd5AagIinSZ4COj3iPg77cHh08E_m0a5fOuSh5XAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 6
🇺🇸
استادیوم منطقه خلیج سان فرانسیسکو (Levi’s Stadium):
🔴
موقعیت: سانتا کلارا، کالیفرنیا
🔴
افتتاح: ۲۰۱۴
🔴
ظرفیت: حدود ۶۹ هزار
🔴
یکی از استادیوم‌های مدرن اولیه آمریکا
🔴
استادیومی هوشمند و دوستدار محیط زیست
🔴
دارای فناوری‌های…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/91295" target="_blank">📅 15:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91294">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A6Z_NlXMAnHX5Kx-9Zs6DUV7xpkBKrMFXgAF9a7gWAUu0hfyXHjEmHk92rg0SHf6aCOk0nNoXImdPaM71V_ibNC4PDrH2W9FKEgyOXK1xJz_02JMs-0f0OSl285JUiCJV4HNxh9cKiXtt_SjFZtrmXMxpjtbc1Ml_9XvB92GAi9AO97XRZ4oNI7eMkbKoLkOjmyLhfdEODwFsjE2DhtuZpyz_f0jzsMi9Yu5aeo59LnMwfaxBOLEg8LIqbHNVpcmA4hKqo-3l9IQBZ1mOkt-OMvIKaXacb85JTZbzgfIoS2LdO4oMTLyDC57i5srGSq2owrMlb6d628q2QziTdHHZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 5
🇺🇸
ورزشگاه کانزاس سیتی (ورزشگاه اروهید):
🔴
مکان: کانزاس سیتی، میزوری
🔴
افتتاح: ۱۹۷۲
🔴
ظرفیت: حدود ۶۷ هزار
🔴
قدیمی‌ترین ورزشگاه‌های مسابقات
🔴
دارای سر و صدای بسیار زیاد و شناخته شده به عنوان یکی از پر سر و صداترین ورزشگاه‌های…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91294" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91293">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2aCCnG2nv82574PlJ7Xu-UCtYWhfTRl0wnK7KHZGWPbidbtSdEbrATdIUV0xC12IrcNmZjnRuq8Xu3RBZgWnrLkkuv4aT_BmR06EdCBpY1O7VYe_FAmO4Dy3XYxqLNH25sz0xB_Mg8gOiHCKdtOfJL7uWzTsrard5jShl3GLestTTEhdRaQCWevLzcZDZ_0lRLyiD0O1cz8URZYfHEPzRFBqatqYlElKeid8KMao-BQQ_Ir3yK04LcVl6CLVDdqJJHdwnlKSRTo9iQ5AFFOlRIK0IjzKmS5VLlZlkHfxcX11iQCUISwhReF_4zUXUwbZFpOJoetJtzT1haRmLGwyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوناهم مجری دارن ماهم مجری داریم
😔
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91293" target="_blank">📅 15:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91292">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bmvg0vPoEL7CTKsGNoYIy1EWfoqFE-s-0kbC9WB5TjN-H3b6d_9-Mu64kczmVTjvaF89NRlChkJmtDZaZq52DliaoQXv7yU78APRYYkH3pK_F6nQ9Xncx7yECtsgYWHJD75L8JLxe9QZoCNRA3ovX6DWQhysUMJdCZ8n1Tc3Y-2peZssR1NV-aj-StuIgUC1o_Z0o-ZXQI_t2-ID0XYQCh6ReqMoF9zJ1tD7iGGQJicQpzCOCk5NP-9y08Wdlnd0bnurtWwr0-Q8I3WbnyW1NhpfXM2HFpbOWkDPq--JXwb28aGSryijkHPNb0kYzVOD2zcUxVjhjR6v_GuVmEACsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 4
🇺🇸
ورزشگاه فیلادلفیا (Lincoln Financial Field):
🔴
موقعیت: فیلادلفیا، پنسیلوانیا
🔴
افتتاح: ۲۰۰۳
🔴
ظرفیت: ۶۵,۸۲۷
🔴
جو بسیار پرشور و هیجان‌انگیز تماشاگران
🔴
ورزشگاهی باز با سبک سنتی آمریکایی
🔴
خانه تیم Philadelphia Eagles فوتبال…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/91292" target="_blank">📅 15:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91291">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrl1uiOdQKReH03QfqshUzVnF_fb3xp46muNtA3qI24h6-NtXuNxyV0UolhSGNx5mWUIvvDq5Mrpy_QAoQYo2mXNVFMuYXJeRA-WZFNHq3FCFzsicfNqoc3ZFexe5zCj9PN9JWlUgde7vjgRpKPmx9V_Z4ThPlqalQifh4fNLXRS69eKn5s1-BNFBGbGZmWnKYYFj7ES03sUVjZI76h5MCwQfnrewg6q4p0VR2zm9SuXvKSeAesqyxI84Iy2IWb-JCKXl2BWYULuK_wfwTe3_z-y7Vrgzo1AEdIGKAXOVdazs_eb9L9Vr0pDo0OherWwHwRSrdEVkr4KcsMt1EB2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های‌جام‌جهانی؛ شماره 3
🇺🇸
استادیوم دالاس (AT&T Stadium):
🔴
ظرفیت: ۷۰,۱۲۲
🔴
ساخته شده در سال ۲۰۰۹
🔴
استادیوم تیم فوتبال آمریکایی Dallas Cowboys
🔴
سقف بازشو
🔴
صفحه‌نمایش‌های سه‌بعدی غول‌پیکر از بزرگ‌ترین صفحه‌نمایش‌های استادیوم‌ها
🔴
استادیومی با…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91291" target="_blank">📅 14:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91290">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hC9baIl9ATl7AZZEbx-OsouxMEmsdJz4-4KjlURTQXlcw6apyMUI5H033PY2Z-QuwnD-IOWC65dOSx66b11Sj_66cjhxtHBKqfR-BhP_8cTACzAUanijYF3oU7KBAU9JEc94wd0Z8mXoqQnSQwwXUVjRwbhforHU7GJu51Yol_bCXCNXpItvSHFeheb30UX4upXXyQhAqcG_NYOeRknM4PM0OI5JNXNqTpi3x7SK4_jTd6aEiEFTPICGny5e-GqLJZZGI6KqLErRFs_GPKFGdGbN-6D7CEhxOr_vZ50EtZV-KGGEEEC13XjPa1Jrx_eFPIrQyruqiWwmZJe_HlQhMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی‌ورزشگاه‌های جام‌جهانی؛ شماره 2
🇺🇸
ورزشگاه هیوستون
🔴
مکان: هیوستون، تگزاس
🔴
افتتاح: ۲۰۰۲
🔴
ظرفیت: تقریباً ۶۸ هزار
🔴
بسیار مناسب برای هوای گرم
🔴
اولین ورزشگاه NFL با سقف باز
🟣
خانه تیم Houston Texans فوتبال آمریکایی است.
✅
میزبان ۷ بازی در جام جهانی ۲۰۲۶…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91290" target="_blank">📅 14:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91289">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfRHxoirZXIahbYe28mEMRco1qVFzODMXyLdqiRSBJhqY8I9FraSnYjZ8Z7rt87o68Y8ghfv-QM7ThFPwqLtXF9ro4Qx3nGmZ8wgysEUheyvKsOKApw2X-rPno4aF8YhVuZqjLg2Bs9JRR8w0NoKOi_P6BLYc3i9o9mPCuwUVcNkrPocdx4YfHhAPM3fHf8_saex1fH8I9uALGQdwLm-Bss0rSxXt2-P1uyF9qKOJ_pyXf1onV5tfSQDdZACLlqab79W4g34Z1__8vpyNGVaplsQiFT9Pk1JM7ipogd6rox4XGK4hoCqbFdbvpAxNrRqu-Hbcd_MgwnN6XILzwSStA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود. ۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/91289" target="_blank">📅 14:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91288">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlRyTCJBiAPZVwhG0_EeiX5X_BkEexbl1eS9OBx2J5_Zb1g0TL31pZDWqqg5sGPfrgSYEZHBzAJ35V3lSNuqlPNMbEkXDIlPyWDJtEH65FkNxkhdWUi77iBbBTME_Qdnp6MQ3bjffgMjIL5Xs7XpZwSrg7M2YvmyZWtJSCkATyBcgMZO1vDqNGjatl8wdMU21AdmAZh7hXKiyl9Ls83T0jY9K2tng2rwssJfR_B-vZsh_UhOMByjMDm6qLsRKbaPHEKnR18kPIPlRcX36hVBhyNXwCjMGADZXHFVrRY8ZNtqyxoqDjrWeqj0t5AhF7vlYdhkqsz_gH2dUU_fqza5fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏟
معرفی ورزشگاه‌های جام‌جهانی؛ شماره 1
🇺🇸
ورزشگاه لس آنجلس (SoFi):
🔴
ظرفیت: ۶۹,۶۵۰   /  افتتاح: ۲۰۲۰
🔴
جدیدترین ورزشگاه‌های جهان
🔴
سقف شفاف
🔴
صفحه نمایش ۳۶۰ درجه بزرگ
✅
میزبان ۸ بازی در جام جهانی ۲۰۲۶ خواهد بود.
۵ بازی در مرحله گروهی + دو بازی در مرحله ۳۲ تیمی + یک بازی در مرحله یک‌چهارم نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/Futball180TV/91288" target="_blank">📅 14:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91287">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S4WY1P9ahGssmo3UrNo7-DBR4sR3JA41fOvlCzIC7xMFZiyZemgFaAlTgcWmbSb6QibJjLrC96LeXeEywNRO9leHWRTzm3yahs3y_aXfSa7xNJ6Yrq92B1It6WwY1KcG9v_o11SWfa163iu0_q3GIdgFdXKGGnfK2yVL-ZOFTpZ1YwVGGz589Bt5L_TqHBuIFXsm21XvSewbEfTjeI0VpOwjhnseA7ofIP2pWNNXOi9jDadS65-gM9qJAfe2EkK62-sFN1ziNBAp0lz7gg-ZYikLPWxGBQPbzQhqhQU4fvO0sdN-_ayMO6fQ4mCYV3X_cObuNty_tpA1fCMWlQ7zUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🤩
#فووووووری
؛ رسانه‌گل: الوارز پیشنهاد ارسنال رو رد کرده و اعلام کرده نمیخواد به لندن بره و دوست نداره در تیم رقیب منچسترسیتی بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91287" target="_blank">📅 14:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91286">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhtdoLCEahKSM-o7Nps4mJmWW_x9Efet2sbnyBWNfCyxhrdHDEwtwkKUI6lSfuG0dEORrRYLq_WJxfTveHfy9Vyzp9maGmO1ljHnFWjbkFYelzuSupt0plimiTtcUClKyYRtF92z8wZhCRKi_4x7F3-blDnSEsRZFk3pfxAbfUzlPGW2zKAm7k0BOytsXM6O3TNC4nHvmmxUfGDtO83MWnhhZ21pkmH_A-srEFb9UPOp9HvEddZsx8EvQNt05nqTYlkBGSRQQOypQDFLbpLKphDWHwcegFr7Y_52VG0y3rSIeyG7YOpel87l2lrLntchBfxAbTE1rmemOMznAhPuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ براساس شمارش اولیه انتخابات رئال، پرز بار دیگر برنده شد
- فلورنتينو پرز 65%
- ریکلمه 35%
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/91286" target="_blank">📅 14:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91285">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=oJVvIC2dE8PndtLfAUM6meu-BmMDFrZyH7UkHpLyo7Yp8SBvkAaSyWjrtlA-cCIu2k-WT3KfkcTb1uWq4icKQrf_k4_AEPps_vwC30d4YtQKr6ld3smwNVnKQbhbrlMHotg_CK6B0caa5FZ0AADpmq3H-NKk86zcK8tX3r6FQ6khoRSNRDXPcIZxsyvi3GMD4-osgKsu8BBTx1TcVcriJYLSXI4X_OdZbRHOyQoMW97nGbHXCtILwY9FgGmY68K6xTigtYADJc0tizJtcytzpG7UDdO7mMC6HPp20Tnzv5dd0Td8i4wyiVO5LVxlf21LebJMx_kkjGO7XP8_Gn-Arg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdeda036cd.mp4?token=oJVvIC2dE8PndtLfAUM6meu-BmMDFrZyH7UkHpLyo7Yp8SBvkAaSyWjrtlA-cCIu2k-WT3KfkcTb1uWq4icKQrf_k4_AEPps_vwC30d4YtQKr6ld3smwNVnKQbhbrlMHotg_CK6B0caa5FZ0AADpmq3H-NKk86zcK8tX3r6FQ6khoRSNRDXPcIZxsyvi3GMD4-osgKsu8BBTx1TcVcriJYLSXI4X_OdZbRHOyQoMW97nGbHXCtILwY9FgGmY68K6xTigtYADJc0tizJtcytzpG7UDdO7mMC6HPp20Tnzv5dd0Td8i4wyiVO5LVxlf21LebJMx_kkjGO7XP8_Gn-Arg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐸
🐸
قر دادنای شیدا مقصودلو زید مورایس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91285" target="_blank">📅 14:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91284">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=dbK-fiWGA8W4NvWtSxiwpG1zWROzQwibUlRkmBqTlOEIGNmZnldLJFKoTzNK7IaPZZtlZ49pIRxNghu5qtVczkzjuYk46kRLxZ13HG5k9cn_gC6UnnOPVDQQ0lMgUY8B5HMURbpn0tkVsm3mBkCp6DqBPgUSXl21lenfKSV5wolKEJz_Ph4dcvQgqjZqIGk2AP53E-qWaJE3AX8RyqFJMCeL_qAXrDVQ-scs0C_ukpMhN27HV2XagPiwgX356MEVeCERV9eGlyS-4T8e_tZSsunNeulcv_LNSvZZTfiHX6zXrdlTFCE5_i7jCO14UW1sKBPHm7ZLCpeiCYJN1lEDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21f03b77a9.mp4?token=dbK-fiWGA8W4NvWtSxiwpG1zWROzQwibUlRkmBqTlOEIGNmZnldLJFKoTzNK7IaPZZtlZ49pIRxNghu5qtVczkzjuYk46kRLxZ13HG5k9cn_gC6UnnOPVDQQ0lMgUY8B5HMURbpn0tkVsm3mBkCp6DqBPgUSXl21lenfKSV5wolKEJz_Ph4dcvQgqjZqIGk2AP53E-qWaJE3AX8RyqFJMCeL_qAXrDVQ-scs0C_ukpMhN27HV2XagPiwgX356MEVeCERV9eGlyS-4T8e_tZSsunNeulcv_LNSvZZTfiHX6zXrdlTFCE5_i7jCO14UW1sKBPHm7ZLCpeiCYJN1lEDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زن مسی ماشالااااا چه بدنی ساخته
💪
💪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91284" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91283">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=YLAWxzUa6aZpQ7hgoVklPWAAnuema9_HJvhglaNb0d7sHsAemAH4hWUIxe8161qzBogTY7AbpqE7X_tyQK4fqIdLZw_QZgmOvIy9lk9kqTfhl7SmiPP3DdkBrzL6qDws9ln7bSFekZEWIRxuEBwtd1AvmU2n4hJ-eDBdIP9sdBrFpV5W2z9V6hhADr8IVdWopTPbbnTWBtmS8lCIl57RxhrMKUiIPKwVVOxBAgJig18-6FOTVjjrzudtopTTft7ijfK-JYgdKa4MMKxnXWJJ2_mztScBCr2RFeI8juRl4wMAv6Wb4c3Vv3IvWHT_O5AIONDtle9FDTsnuIpU02RqpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5a8cca451.mp4?token=YLAWxzUa6aZpQ7hgoVklPWAAnuema9_HJvhglaNb0d7sHsAemAH4hWUIxe8161qzBogTY7AbpqE7X_tyQK4fqIdLZw_QZgmOvIy9lk9kqTfhl7SmiPP3DdkBrzL6qDws9ln7bSFekZEWIRxuEBwtd1AvmU2n4hJ-eDBdIP9sdBrFpV5W2z9V6hhADr8IVdWopTPbbnTWBtmS8lCIl57RxhrMKUiIPKwVVOxBAgJig18-6FOTVjjrzudtopTTft7ijfK-JYgdKa4MMKxnXWJJ2_mztScBCr2RFeI8juRl4wMAv6Wb4c3Vv3IvWHT_O5AIONDtle9FDTsnuIpU02RqpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
بانوی جذاب آدریانا اولیوارز مکزیکی روند زن برزیلی رو تکرار کرد و بدن خودش رو پر از برچسبای بازیکنا کرد و از دختران سراسر جهان خواست تا قبل از جام جهانی ۲۰۲۶ به این ترند بپیوندن.
🤝
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91283" target="_blank">📅 14:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91282">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34842d0797.mp4?token=azr7Ads5p_CTDzvDg60W0be0aYZdgnZB5SE1FHZ3SQ14ZLbUY7eIsW51zN2bo2Ih8D7wFk3cDLOH4hpymkCKGQid93VkIdE5_9YgfsmirtBGSCUd2QWF2XQdJN5ibRplRXDtkHlVkqG0GDbbKOgIu5Dnyxwkcyq6xa2bWyMqAVvMKWlkXKtHpma8XVLLcuejozrO2Pdvwpc4-Lrl77nnZ18vs1akA03OrZQyIhVkgA033LH_A-eBoTDxjQNpRRoIaYniTfcYVe_TSgkKZrMTkCrkhLoQH-b3WkFpGn91RlToP4ACpOmPyYYqBeGqnxUj_mVTYvuXR6w1uNNcbEw-4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34842d0797.mp4?token=azr7Ads5p_CTDzvDg60W0be0aYZdgnZB5SE1FHZ3SQ14ZLbUY7eIsW51zN2bo2Ih8D7wFk3cDLOH4hpymkCKGQid93VkIdE5_9YgfsmirtBGSCUd2QWF2XQdJN5ibRplRXDtkHlVkqG0GDbbKOgIu5Dnyxwkcyq6xa2bWyMqAVvMKWlkXKtHpma8XVLLcuejozrO2Pdvwpc4-Lrl77nnZ18vs1akA03OrZQyIhVkgA033LH_A-eBoTDxjQNpRRoIaYniTfcYVe_TSgkKZrMTkCrkhLoQH-b3WkFpGn91RlToP4ACpOmPyYYqBeGqnxUj_mVTYvuXR6w1uNNcbEw-4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
گاوی تو تمرینات اسپانیا اینجوری رو پای رودری تکل زد که نزدیک بود مصدوم بشه و کلش کیری شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/91282" target="_blank">📅 13:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91280">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lOpBMhEPS_0KqxNkwr1NvGi4NGJ5pLg9KlIPu8tMarOW2KuUP_gaRbfJWaDUPpdIE5NTo-kkzwjxkpnqdS43rKh5-lRQ-KR__pnjshkWOfgGmoOgsMXMGp3tIaK5uGjuMWN65AH4GhO8P6psksFAs_0w8LSHkzQu8DMIupozS0ryQEHe62S-qUEUlzVCQAJ1MgZqoy93EVNQkIMSGviwngoMyb0iw8TLD-dx3q3GGksx62KjWzGvZqfWchx-zCfzkOYfe4BIXMsh90r2w3cMNp97TFWoZCCrcgJMKR_XFFL5QOgNWygLwznmt1_AC08QwyOPnVDwsEvBeI2y8-p3XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VNBF6cmZxIbaNMuXee367JxB3PslqLhMQ1HFWztzb2BG45_u-x36l4WFY9Zq_QIZCxrvnhLfesSBA6X_5h0zVI41RPGpOosS2JBx9P-QIH14IUnnaKyvuM6rIx2aJ9p2uOINPAHES0_W0GbyRn-7hfomNtar_DbhbSlTT0H1zKQaYD_NxGUvoQxfgOaFFUmYTxOyWsvy9uQPWqFO8bF4sVkBjLz_N93w8bq2NC3KQ76bPwqRqZUwf7ArWyatLUsBGVvVRiB1CiU_t-EirghFl71PxasHaLhmzPSAHoSf5L94Rg_NrNeVacC5U0lkEzbjs8p2APgcQmsiKK1a9UGY9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مدل مو نیمار برای جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91280" target="_blank">📅 13:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91277">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFbtOnJ-kXbjLPcypMsWHiblWRkmFIfRd5tAnZCs1YBaoT6YWqjubMc236TTwGfD4t-TOBNHRbgzSW-CNciXJXEt2DzhrvHaMFNreOz_b64R7QKXBMZPPlE_98cRavLp_hLU5gpP-OcU3jJfWJMyXbxL0msITgtR6vqh0_dkUPXgxel8FS35RFKYf6zGYL4MOLajkU5UxYEmo0aglHal2JaoTL9RdoavlI2Ad92OzPfCWaudYgnF0dxLQZ3IBmwfbPw6VbRbHxX78dMm1FR4-Kqg0HyE4w9gXhsLahBU3L5M8fEIXnODcIbsPKoezsP5kNzrU6x8H0VSKqk90IkK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUQiMz_EmTx6GGplnP44XT5j5XPUwyYZuGSKarlXhxsibnvv24E2Kc89zl4zSNCQjaCS-V4NtGUKIr1TX2htgjXgKh7YrCAF8vrrDNOKd_9eKvOm6Od56UVXtBTUWdt5J6YDX2Ia60aA1aymkC94yIEJwBKn-MvLLhbrPQhX1lo2jQLyPIjv7JM2L4WHVP3EaZadZG3ghl9fJkNThUzUp22zCqQQBp2d5V7EmaS3MMyQIzJbFnugS_xqGM-VJzRHVbegZLX6r95gOrrdrxYYGRx2bQtt0KN1NsEZtqjNndERN9QizBOgEB5OAGEBsTdejoXuUKl0zQS0a5nQBqjnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1MWrq_FElRwO2MtRdPpD0KkYU7TMBnv6QZ0EaBUlyvfm8pvwHZrRdkcDbnPs1wsTf3MhEAgj7wkrzBp914T8fK0wgwkewM1uDA4nZnWcCHFO0BeRLE0CQFK4Yg1B-FC3vSZ9Bvrvq7m2kN0WrMANLzk7iSkwHeT2byCmxK9NG_CtPW-n2K_ZbloyXYDbA9uTgLsKGeLO8L9P34v1kSoDgiv6VImJKeGwFIEXnfde9uuXsW2X8_VZfGfT4XOTwUmmfXSluyo4IHOZq0_3JCPvxxrHS3XFLvKKBzXF32MkKCaNjrBzaWeDQ3N4UJpoi5x91SC31N_dxsiOV4koE9G-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور پرز و ریکلمه در انتخاب ریاست باشگاه رئال مادرید.
کی رای میاره؟
❤️
فلورنتینو پرز
🔥
انریکه ریکلمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91277" target="_blank">📅 13:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91276">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqVIVDGJNhlEQVEg0Ld9FeaKLR8Dddf8-_jkwXnmzYvVXAK3CB47XzbfJdg8MlZ_GXxAnVRtGrJUwyD2bCVn5ehwY5fptvveo1AaLJHMne92VSCqpT0zpoMlNuFceBtP15Z064oXA0rsA9nn8RErkegXPG8dDEkiCB48aMPSABArHaKFJ9_r-QFf6Z7ik8Nu4l6mIYrlN1qEo1XcX33MfIR0EXtPRSjN2D1OmMprDC1vHaPj3w_MNKdIwZFtMNdpRDCV9kGRQFUWUgmyIBrWh2Wna-LMS7Zrrl84mPP2AvU8KAvOxoHFG1E6cSGzjyhXe-g_xJEvI--YecsRZs1mErBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqVIVDGJNhlEQVEg0Ld9FeaKLR8Dddf8-_jkwXnmzYvVXAK3CB47XzbfJdg8MlZ_GXxAnVRtGrJUwyD2bCVn5ehwY5fptvveo1AaLJHMne92VSCqpT0zpoMlNuFceBtP15Z064oXA0rsA9nn8RErkegXPG8dDEkiCB48aMPSABArHaKFJ9_r-QFf6Z7ik8Nu4l6mIYrlN1qEo1XcX33MfIR0EXtPRSjN2D1OmMprDC1vHaPj3w_MNKdIwZFtMNdpRDCV9kGRQFUWUgmyIBrWh2Wna-LMS7Zrrl84mPP2AvU8KAvOxoHFG1E6cSGzjyhXe-g_xJEvI--YecsRZs1mErBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دریاچه‌ارومیه که حسابی جون گرفته، این روزها میزبان پرندگانی هست که چند سالی از این مکان مهم مهاجرت کرده بودن
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91276" target="_blank">📅 13:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91275">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2oom7KQmtC1PbfrxvF3cdRz8VToV9X1_Z8bwi1n07ZiBD93kA7iEJ0V1FZX-Nbjxv_UCbdz2RF_NwrI4SLIUN_8SM82oWhQbdofJM3-OraBX4Avuw6g1lEJkBTRkWIUUAqASuzb_T3aphT53QcwzuN2ORTKuhQH5-yWYzpZO-SHF74IKdZsgZjwI6H6IXlDSChfLAuV3ycguvf9h_Ta-h326qD9F_f6UVN8RFj9LEZANJZIRSxbelvsBUZ9GYafma0uszdJ6VSo_LycZ5MeIuEq3HqjHs8skP88xFMMo7cqM6N38TMkt2DNz32AwyWhCcZffLSAmWyX1Zz9P8pqlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چند ماهشه امیرخان؟
🫃🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91275" target="_blank">📅 13:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91274">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rb4RDGJ0q-FfxZOephg3obso5iGxIzMB8ANamuCT6-UENSJnjk_qV7t3YkqYk3spygk17qB9DAdygo2Qf0X2pQeLo-rBXY3WCPSPbdUYtjSDG7rCLZeVAtX9GZhUAYduSmq4epWdCAZLAST41BkzW7asFtdOjXoloGgqhD6xrphwJdYY_P75im0JuZjgz2eRPjFS97mNkzhkE77zicSayhhEsVm67SKcmRTPEcmHz0YFdf6MReDJtPoFPUPbggbHLO-wIytJ1CUiM4Pd1NfsnwsVsvA3KiAjizkLvuqyluZZ87IY_4sV87rohJaXBdTB9pSVRS4aVzALRQjpgsKmEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نیکولو شیرا:
ساوینیو و تاتنهام برای قراردادی تا سال ۲۰۳۱ به توافق اولیه رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91274" target="_blank">📅 12:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91273">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBM8Ist0r5QV_N-Kj6IIyJG0F6M_knPf4ltC8I0ZX9qOEOgQY75wNpRiYkUUyroejHwiAGxL78dPc6gWuA0M_omqQB74t9bbca5PYTeujEa-Zog3O2Vm8wJZgCOgxFqMPM4Pp7daKjyMbvnJE-9ltViAjV2xxC2kLHkRdjXX33BmbvJz5MBMr0dZmAxeZvGBNRK5l6-uvLACn4q7EApYVQ-QXLwdzH-mOTcjPtD88jb-WCsQf918sTY_R9wPcEAPulaIshxS0yBkDfxatYbwxEVdpqMqxMBawJEaViV60FdvbYJKzYt2zGbTTSprDZYVTV6X6B3xagu7C5x5_9gntg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز جام جهانی شروع نشده دارن شاهکار خلق میکنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/91273" target="_blank">📅 12:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91272">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=G015a-FxsFNXnpAppL5e-WA7A3GPY8kqdhGrO9Stck_t1Hcm0mBKK3pVOWoBiZzkjh36vmiTIg93NQtHJ6pbfLK9hPAjF81cloztSjLr9_LSvb2utwqRfgjVHGSih-fuI-OWNhBenNqfxEokH2zgfGPtL1v6yuc467SRJWrbA3nxBfj_yJFifQXjK0fhpAg7hGgimKH9_N2yPqPUh0wZ8UozHK1lEw_0kyyijcSD34WNoLrdS6hzeg_G0TT3sfhQS-x91mU6-3Tsnk1yjxABKwoS6rBchk_e7uwOQQD7HTUU7tM_FOCixZhlpk5cts4cwq2z1_oFh5q1lxbeVLvSaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b9ee999ec.mp4?token=G015a-FxsFNXnpAppL5e-WA7A3GPY8kqdhGrO9Stck_t1Hcm0mBKK3pVOWoBiZzkjh36vmiTIg93NQtHJ6pbfLK9hPAjF81cloztSjLr9_LSvb2utwqRfgjVHGSih-fuI-OWNhBenNqfxEokH2zgfGPtL1v6yuc467SRJWrbA3nxBfj_yJFifQXjK0fhpAg7hGgimKH9_N2yPqPUh0wZ8UozHK1lEw_0kyyijcSD34WNoLrdS6hzeg_G0TT3sfhQS-x91mU6-3Tsnk1yjxABKwoS6rBchk_e7uwOQQD7HTUU7tM_FOCixZhlpk5cts4cwq2z1_oFh5q1lxbeVLvSaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گروه E جام‌جهانی فوتبال
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91272" target="_blank">📅 12:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91271">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">😂
جمهوری اسلامی پاکستان دسترسی به اینترنت را بدلیل اعتراضات در کشورش قطع کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/91271" target="_blank">📅 12:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91269">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX-4AZOZsjlU9YOpYUnCwDFijr_QHZH5ASfQqIqArqXbOAdEx9TKf3JczFsXlkDO2TDhH1JPgal9-tvJJJ9eSTmE1pTJyGdC-ZVATFZChv5GrxmCvQdqQHwhrvLfYD-fQ2oVQ0Wh5DFWHuroWewVYC4Ld13PNF0TE9T2e2UCYKfiRwRmtqTG0YaJNe61MHvVVtaMA3ERjMbwqbh5J2Xj3v89ID-mWB5VwqfYdi0q2-074yg9fm6EeASd3DSPVeaoUslzC7xG8JN1fcimo1z3Yf_RSpRmdIJVCWZV4VdsGmG0E2h8PN9OfsXbnuhRAh1leoHEr37CaepRxIgFJAWe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
‼️
🇪🇸
هفت‌سال پیش در چنین‌روزی ادن هازارد با رقم ۱۰۰ میلیون یورو به عنوان جانشین رونالدو به رئال‌مادرید اومد و‌ در ۷۶ بازی با ثبت ۷ گل این تیم‌رو‌ ترک کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91269" target="_blank">📅 12:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91268">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=P-VkqqHm8Qz6l8xnHlLI7gzOGR1mv9aCDtB0WFubOFQp7rAPw0PDyHNa03k1ZwKs5GYTRSf-a513Kjj57qmdcIWYJidxb3rsBhwa0CHEMjDW6KMXxh4Ex_KqeWPepnxrABya9qvbqwzJV7Xyl0ir7qepiuZFZKWY41uMC9Nq9Nq_-dhygfhLUDmjIxMpXL32AlgPL7pdqu_N0pWJOSpJdYxYhb5DUoryo01L14IXR9qo73pbHp3k4gjmHFnidURqd8_vxu01hngMDipSUSHuyxog8wjzu-XeC4gm0kU3J-MhnjahbIbWDXOjQKZ8zEcBqx7_yoxWPSHbenkCuxzdCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2d1881201.mp4?token=P-VkqqHm8Qz6l8xnHlLI7gzOGR1mv9aCDtB0WFubOFQp7rAPw0PDyHNa03k1ZwKs5GYTRSf-a513Kjj57qmdcIWYJidxb3rsBhwa0CHEMjDW6KMXxh4Ex_KqeWPepnxrABya9qvbqwzJV7Xyl0ir7qepiuZFZKWY41uMC9Nq9Nq_-dhygfhLUDmjIxMpXL32AlgPL7pdqu_N0pWJOSpJdYxYhb5DUoryo01L14IXR9qo73pbHp3k4gjmHFnidURqd8_vxu01hngMDipSUSHuyxog8wjzu-XeC4gm0kU3J-MhnjahbIbWDXOjQKZ8zEcBqx7_yoxWPSHbenkCuxzdCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باباها جام جهانی امسال ساعت ۳ صبح:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91268" target="_blank">📅 12:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=CV82_SgCAkDzcQKFMzZEZwHdAO95AN4P8TQTFFW5tg7Uwr16wNDI-dBZkHLN1jDZcctjHcUMjK58RdLJWHnWTzHdjjmCZwokq6Jh6D80lazmeZlS79NhGVcp9ujIEHhefS8j3-jYqZ7ScUgSystQNVW1aqW55c9RIRdssADegYT1bktsMIXzaTPaXPPOcuQtIwdwZMzlLxudYmSlUO9rEK7uTYDWlhx6DDBfZ_g7sI8Bkb7KQ7MTSzm1ZThopkpQ089lchuda6CWHZcxpPELFuJ4A-jp2QHbP48CS6rgJjBiLq8yVvCKWR_MBqzgRyVgFOsTVaUOcTco46jln_2B8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2e6f956c.mp4?token=CV82_SgCAkDzcQKFMzZEZwHdAO95AN4P8TQTFFW5tg7Uwr16wNDI-dBZkHLN1jDZcctjHcUMjK58RdLJWHnWTzHdjjmCZwokq6Jh6D80lazmeZlS79NhGVcp9ujIEHhefS8j3-jYqZ7ScUgSystQNVW1aqW55c9RIRdssADegYT1bktsMIXzaTPaXPPOcuQtIwdwZMzlLxudYmSlUO9rEK7uTYDWlhx6DDBfZ_g7sI8Bkb7KQ7MTSzm1ZThopkpQ089lchuda6CWHZcxpPELFuJ4A-jp2QHbP48CS6rgJjBiLq8yVvCKWR_MBqzgRyVgFOsTVaUOcTco46jln_2B8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
رأی دادن فلورنتینو پرز در انتخابات ریاست باشگاه رئال مادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91267" target="_blank">📅 12:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDWiRALm1TAbN5bekzyRqUHvacIePwSmOLM4iQzuk1EE20q-6LhxCrWQJpPOE4DcpAZa-0E3c7aU0BizwuPa1WXikhMhoePkIihRyxgcmcTLSsoRedNPm89fQLdkJ3Z3HvnIBZKgkHYWm0p3YYOg_dj1-7sE1K_XDnEjYE_N1kxBFzrsefGO-EK_moB66_VVd-rSPNs-4luLbv1_F89Qo6WakazGbS2N1lPIw2k6bGf1nXNo1SG77Co9CNjDADPjpouX8E0ycP_n3xsvJFx9GuufUqDyERQC5sKZn_R3cIjNvJnicPAert9diCtBw9xYZds7QNqTxBlgHFPdis2DSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
⚽️
«سال 2003 پِرِز به خاطر سیا‌ه‌پوست بودن رونالدینیو از قرارداد با او خودداری کرد»
+ بازیکنان رئال مادرید در فصل آینده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91266" target="_blank">📅 12:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91265">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=VtEByax7j-CQu25aEfj30uK36aWDQ4h1mZSh510axRHre_JD_mjr-VoeqY8pzAIf-myBLWwpI1oZg9dBR_-Mry2jMkSLje1wGQjS1R9NMEFw2XnX9GCs1nTAj8QUfw4BVP0hGPmvhOzRHLfKr6y2rNanwuWw-QmNZJNaa5yoyMmVedl0kcyQMkUF-YdMcA1NFouvkqh_u6zqrDmE-wy7AL-tdTVGDUrRmob-YgEmz88HJuFrxKArvCwC39fgfWNmhBn29CukJfP927UNuw7JO_xZGPkRwMiH6Lm2kEKaO6C7gTbhMv8SvsKaPtXg37BR-zfRNGAaCiSOHfGiQSwqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c6904cff7.mp4?token=VtEByax7j-CQu25aEfj30uK36aWDQ4h1mZSh510axRHre_JD_mjr-VoeqY8pzAIf-myBLWwpI1oZg9dBR_-Mry2jMkSLje1wGQjS1R9NMEFw2XnX9GCs1nTAj8QUfw4BVP0hGPmvhOzRHLfKr6y2rNanwuWw-QmNZJNaa5yoyMmVedl0kcyQMkUF-YdMcA1NFouvkqh_u6zqrDmE-wy7AL-tdTVGDUrRmob-YgEmz88HJuFrxKArvCwC39fgfWNmhBn29CukJfP927UNuw7JO_xZGPkRwMiH6Lm2kEKaO6C7gTbhMv8SvsKaPtXg37BR-zfRNGAaCiSOHfGiQSwqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
پشت‌صحنه تصویربرداری جذاب از نروژی‌ها به سبک وایکینگ‌ها؛ ایده و زیبایی 10/10
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/91265" target="_blank">📅 11:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91264">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCq0TEJ8WiXxMAQMB2hoIyvn7hyigtxMyX8n8EEhRlW5qQjI8Y4UHW-ULbhFKRpjh42rrSklQUyoR5ASIOup_Jd4liedy_eBML_GuKE7b9aQGGpIp6Po9DmkmbPKoE9qg8Wy86v8sawtW1dsX9tgT-h8MeC5qFCAuGI59JgUNu8zR1x6A_1lym18GjIfi8ghrd7ggJflElO8lUlCjC1I8gYUMmVOSYEG6LphZv4SS7SyiEjy2lMoAo4tqjeiqdiidNWaPdkq4eIlL599rj9HSgIkfYsAFc9xgU-QVg3-oqMOP-01BBGaEfXQPQlQoLH8vEqL-1HkVyiDBf_f1BxL7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ قرارداد جرمی‌دوکو پس از جام‌جهانی با سیتیزن‌ها تا ۲۰۳۱ تمدید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91264" target="_blank">📅 11:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHlmn-K7jPlV2G9tHuhxJgXFzW62TGKpgG9lGpdFCTW8v33eXDt61q3y19d2FsAZp8zdZWnlHXvX3-A53D-cj1q5TbNclaOOEu-ygGQe-K0CajHUDooGVS6ZaZHqZwQgLSDbhc9jcPh9sNsVWayGYg_wazcr7i7n47qjHAgbxGoODQo3zq6pBvi53DsaU_5Sh7xMEggKJe19pqs1WIkBUh7dzxgohCkyc_dx6Gccw09i0jHf-XVUBpdkc2Ml2Rn9D98mOE_v_AanTnWCUNb8RwI0KDfgMgPoxHKsqpbc9sXoT-yKift2bs0RixPy9OqdzlK06zzJh_otDFt7fvq1uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Milan 2009
🙂‍↔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91263" target="_blank">📅 11:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91262">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
❌
امیر تتلو واسه ماه محرم درخواست مرخصی داده که بیاد مداحی‌ کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/91262" target="_blank">📅 11:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tqozz5EGlTNOAhwVyr77ZfzDGD59IZyv8UkFvH8xHeEGjUwfl-ISHGk5fFlHZWBPxqSnGo7QI1kaPnvfE5cCMbMwG6N5zvzIfbA6LXveZN1KuUeRddKvxI_J53DFAd-5KeMg7JRZgywoTrpsVF596Qc1gxMAaytcN9upINnhxsTIUdCu08ZeBNV8Zv9igFiXLwOBqxntOObznBioQZ1nMS6ttuk9MFYvhferDQZK32w7zdyxMHSP7tL4q_7rS-LZAhfASO4s3aviWnxbeAyAZTpZqRkyNI6MMUuFehJ4Rh1yxkOkIIgrhguRAyjhWd8_O2EU84wqO-HdmjbaqOq41Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t92QoWl90-qA11bKSgwf43F8AYN1o3gf2PiGhLq_ylBZ_eciatfJQvZtseQCpfSiIIOGVTsPOGlxpi5yIW2tqVRT_5TSo1hA5woiHGwyqjWsoDZN7Nr9j8864YHroE_LrGocUCvExJDlxsE8oWzRYGP42I-27hY4lz4GdUAgpMJVQ2yIqEbFajPpfrvoWmeNDpifbLceJl7wftGqP7MaNG_6tTF9mIv7SR-vFkaXcS2T3lrur6GygMtK3JKvCd-zvBJGrCFQrlpr7Gs-gNVstpCtuiGxzMDF4TzQgh3GD_Dcx92NFK-NpDHAELKC32nVHm2F0fwtJ8JAEn4-Hx_MpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KvjyGmswsmRRMh8a6CT_VwD_xAA_UQo4Syv8wUOHnAboEGmCcKQB6nae3Zf35NLQUiYFza2U1PX3vDw6b02Ko_QEVn4Kq_VxKPauzBUmRcw8OfgG-vqeW31Y7EwAJY3Jq25Mi-F_MiNlP1lGp43wCzZruP8rjN6tQDwQknl1tImnk8j9nVMdCpKxtIr11CAwmkbpJ7W3rHOhn1Jy8yNElo0p7cONYM4fHoHj4byWrMKSbh8KXLMKTC2fTy_G4nu62vfGuxsZj3hPFRqvw1Y9l7kT-_kwvpeLIvUF5uuxjZ11-UOoQLLuKAE5-vf3HwT4uYJ4mrPIf8aVdUkt9H3NqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مراسم ازدواج عمر مرموش ستاره سیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/91259" target="_blank">📅 11:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b13497284.mp4?token=ClA5qRn6tuBN7tb4Qkg8-7QWZRJq_xbTVPXe_hAYXszjWRXU6apFILdzq2ijQ_Pjw6ZOqdc9pLrccMcUJ2khCejLkRrHx1HiQx-MSBJjPknwvYvc7ymN2bhW0HD5H1Yxq66fi6bQRbm6rKQMwiVj-gjmg9-McV8hTfLrDFNhIJj6RV5PFrJXC6bSO2Qn10kYxTtN-O3X3GTGoDVXDXN1jk4eL7h1pkx7L3XmxtOLAP8b3g4KfUtUjkHt5Ual6hVWuJdqsUFF3R4HB-YcIG140AqAZ3jZQm-Rjp1urEFgqxwFnbZv40jdamZlrD3JyiNaxfXtR2SNweB5t5DARGnzx4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b13497284.mp4?token=ClA5qRn6tuBN7tb4Qkg8-7QWZRJq_xbTVPXe_hAYXszjWRXU6apFILdzq2ijQ_Pjw6ZOqdc9pLrccMcUJ2khCejLkRrHx1HiQx-MSBJjPknwvYvc7ymN2bhW0HD5H1Yxq66fi6bQRbm6rKQMwiVj-gjmg9-McV8hTfLrDFNhIJj6RV5PFrJXC6bSO2Qn10kYxTtN-O3X3GTGoDVXDXN1jk4eL7h1pkx7L3XmxtOLAP8b3g4KfUtUjkHt5Ual6hVWuJdqsUFF3R4HB-YcIG140AqAZ3jZQm-Rjp1urEFgqxwFnbZv40jdamZlrD3JyiNaxfXtR2SNweB5t5DARGnzx4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇦🇷
امی‌مارتینز دیشب حوصلش نشد بره رو نیمکت آرژانتین و شروع کرد به عکاسی از بازیکنای تیمش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/91258" target="_blank">📅 10:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adea9b401d.mp4?token=vER7oKgOv_geyCIRDYX9IY0ClPteeVT2uT2-h6haASN6c6XO0lF5tJu4kG0T1XxUB8t6HkUIHve27NroNEe3EiQM6bMJTiv2G8tai_7Rc1Oxv6NOODQODjSSIwMUHN1Ko23BjGPjqHs3NmicfTu_ASa-7bh5lWNjinnwRrIvP91jj7nyVagU2dwZFSp4k_XJ2p0_i5a3n_o3cGNCcbPpiIUculBoexE3_9-6cNEyUNKgY0eWgiDRyfXgsgBgQXXz-Jp2bgWlVxD65-gTrGB3gU69jFC2eG5F3NHOBZQTmeyHv8lf25JAnc1oJHGTh5gM5wD68pTuW-C7X3xyVNFFvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adea9b401d.mp4?token=vER7oKgOv_geyCIRDYX9IY0ClPteeVT2uT2-h6haASN6c6XO0lF5tJu4kG0T1XxUB8t6HkUIHve27NroNEe3EiQM6bMJTiv2G8tai_7Rc1Oxv6NOODQODjSSIwMUHN1Ko23BjGPjqHs3NmicfTu_ASa-7bh5lWNjinnwRrIvP91jj7nyVagU2dwZFSp4k_XJ2p0_i5a3n_o3cGNCcbPpiIUculBoexE3_9-6cNEyUNKgY0eWgiDRyfXgsgBgQXXz-Jp2bgWlVxD65-gTrGB3gU69jFC2eG5F3NHOBZQTmeyHv8lf25JAnc1oJHGTh5gM5wD68pTuW-C7X3xyVNFFvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">30 ثانیه از اولین بازی لوکا مودریچ در جام جهانی
و حالا اون آخرین جام جهانیش رو به عنوان اسطوره کرواسی و رئال مادرید تجریه میکنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91257" target="_blank">📅 10:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91256">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a80a11077.mp4?token=UiPi-hWwmwlJyzqC2DvWZHZlvtbzEhp0NKnYAQkIZcaSiTnvWZ4Er7zdkKy8Sd67YR6_xZ5jsytN2NmE-6Lzo3Qg0uJFkICVZke33yEaKF2g0icIeKIhaBk_QVy8a6wium1AasUgY8ZpvGRWjthxDBPfRR1t1vd9j_1f0Qs8psyFBI0m61zcV4T8nnF8XD7uWwmeHXlbiSR2vV1oikO9Qn2CCZcJLC8PUdxykxxZqM1C47TgFDzaViQ-gjV3kjAMCbCBs6hI05TFEilIUVUQJrm307pL9euuZk9ZC0oTVy2KeTLVdZ_mcQ326n1VlcSnIIvREvzbYCnUlH8NqPa6vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a80a11077.mp4?token=UiPi-hWwmwlJyzqC2DvWZHZlvtbzEhp0NKnYAQkIZcaSiTnvWZ4Er7zdkKy8Sd67YR6_xZ5jsytN2NmE-6Lzo3Qg0uJFkICVZke33yEaKF2g0icIeKIhaBk_QVy8a6wium1AasUgY8ZpvGRWjthxDBPfRR1t1vd9j_1f0Qs8psyFBI0m61zcV4T8nnF8XD7uWwmeHXlbiSR2vV1oikO9Qn2CCZcJLC8PUdxykxxZqM1C47TgFDzaViQ-gjV3kjAMCbCBs6hI05TFEilIUVUQJrm307pL9euuZk9ZC0oTVy2KeTLVdZ_mcQ326n1VlcSnIIvREvzbYCnUlH8NqPa6vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی تاج: اصلاً برای ویزا درخواست نداده بودم که آمریکا بخواهد به من ویزا بدهد یا ندهد؛ خودم هم کلاً نمی‌خواستم به آنجا بروم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/91256" target="_blank">📅 10:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91255">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇲🇽
صدها نفر روز شنبه ۱۶ خرداد در بلوار «پاسئو د لا رفورما» در مکزیکوسیتی گرد هم آمدند تا رکورد جهانی بزرگ‌ترین «موج مکزیکی» را ثبت کنند. این رویداد به مناسبت چهلمین سالگرد مشهور شدن این حرکت در جام جهانی ۱۹۸۶ برگزار شد، اما گینس هنوز شکسته شدن این رکورد را تایید نکرده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91255" target="_blank">📅 10:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91254">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
😡
هواشناسی: امسال سال خیلی گرمتری نسبت به پارسال هست و به طور خلاصه کونمون پارست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91254" target="_blank">📅 10:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91253">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇪🇸
دقایقی‌پیش انتخابات رئال‌مادرید آغاز شده و تا امشب مشخص میشه که ریاست جدید این باشگاه به پرز میرسه یا ریکلمه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91253" target="_blank">📅 10:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91252">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e8a50238.mp4?token=IwrpPeCNzZ7v-XKh5Lm_VrhtMwSH2Jbvl--9H4W7EVvpFX6Y5FUWQ96uEOhOT_HlbdHaar34J3MK8e_ZPC1AfdyUNx2wt7IUwOwseR7TNJvdsOay8V636AsDFjRYlMIyPKiS0Icyep3kqDUBvXoHlG3vgKQK6wZLx3pt1ePNPkYKQlfleSue40ParfMS0SY56XTaCgc1gQ4x7jQSsaZIop-SsDRkl7ZoFSDnkLqFA7EelWVCWN7eKdvTS6GQ9YJ_k-_by0fNqVTtGu0Zo-wunB31Ga-ScsSGgVyhxIlwxSulMDOJDaTZGcUCNNRNFqOw8ZV7TX4Vv9PIVwIOumG7Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e8a50238.mp4?token=IwrpPeCNzZ7v-XKh5Lm_VrhtMwSH2Jbvl--9H4W7EVvpFX6Y5FUWQ96uEOhOT_HlbdHaar34J3MK8e_ZPC1AfdyUNx2wt7IUwOwseR7TNJvdsOay8V636AsDFjRYlMIyPKiS0Icyep3kqDUBvXoHlG3vgKQK6wZLx3pt1ePNPkYKQlfleSue40ParfMS0SY56XTaCgc1gQ4x7jQSsaZIop-SsDRkl7ZoFSDnkLqFA7EelWVCWN7eKdvTS6GQ9YJ_k-_by0fNqVTtGu0Zo-wunB31Ga-ScsSGgVyhxIlwxSulMDOJDaTZGcUCNNRNFqOw8ZV7TX4Vv9PIVwIOumG7Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
واقعا جای چین با اینهمه استعدادش تو جام‌جهانی امسال خیلی خالیه
🐸
🐸
😊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91252" target="_blank">📅 10:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91251">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0ffffee7d.mp4?token=j5wqFE4lYd4GecEGCQ_Zf2Y9DbvX1fnLKogLEIgnwITSNmvadxhROpJtKT3UwVOOCO1Vsin-ljRp27f2W-IgfjRyH15pqFhHY2lL5fN95vruNfZBX0ZNvHO-yTlfvRZuYuOzJkRVxFk85RVPu48pg75HEj2TYldUoiMYYw5Ws4tcjwz4RRBkYFMugvqcrw7SzJCs3FdksSpw3I4L0WbcvS_sygzlANmVi4qm85XXjYxg4-C9-GDD393k4q10jRK5KAsLnTFU8RTxCX3E8K2FofBomI5pVEL9ZbwtNfjerUSo4YuelPVu35j1h155IPJI-YX0zJiTJN8pWZS8QvScwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0ffffee7d.mp4?token=j5wqFE4lYd4GecEGCQ_Zf2Y9DbvX1fnLKogLEIgnwITSNmvadxhROpJtKT3UwVOOCO1Vsin-ljRp27f2W-IgfjRyH15pqFhHY2lL5fN95vruNfZBX0ZNvHO-yTlfvRZuYuOzJkRVxFk85RVPu48pg75HEj2TYldUoiMYYw5Ws4tcjwz4RRBkYFMugvqcrw7SzJCs3FdksSpw3I4L0WbcvS_sygzlANmVi4qm85XXjYxg4-C9-GDD393k4q10jRK5KAsLnTFU8RTxCX3E8K2FofBomI5pVEL9ZbwtNfjerUSo4YuelPVu35j1h155IPJI-YX0zJiTJN8pWZS8QvScwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇳
🔥
هوادار تونس در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/91251" target="_blank">📅 09:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91250">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f42ba19fd.mp4?token=sFQ5MGOCC0RTtMpuaVHxyOm2Jnmm5_NIt2zRIvtiPfIH7TZmlDeOSNhcbuZ36qctZ3-_WQqunyNdssr8XPzV904_UiK-L7cvCP2t-66GTyY11tZD-d_qeyC_ybgvMsufhXLUc12FenZgvAlAKPz6xSpJ9LnNd8rv6TuTAnt9lB6yvmTUQYdkAKR2z5kVJPRNvXmebAJMdf1ZcHNhDTRK2aTXAQsyLKeVOFGopKSCDrjNwb8WsfrWauW2Nte-GxDVHF7pHKvxRbqBWiXTGp1MkGL4v56x8CUio3-zBEqL9OEN6qz-gPgNpXLEwMnrruAyTwgIbCqdHmHfFAUU68kWDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f42ba19fd.mp4?token=sFQ5MGOCC0RTtMpuaVHxyOm2Jnmm5_NIt2zRIvtiPfIH7TZmlDeOSNhcbuZ36qctZ3-_WQqunyNdssr8XPzV904_UiK-L7cvCP2t-66GTyY11tZD-d_qeyC_ybgvMsufhXLUc12FenZgvAlAKPz6xSpJ9LnNd8rv6TuTAnt9lB6yvmTUQYdkAKR2z5kVJPRNvXmebAJMdf1ZcHNhDTRK2aTXAQsyLKeVOFGopKSCDrjNwb8WsfrWauW2Nte-GxDVHF7pHKvxRbqBWiXTGp1MkGL4v56x8CUio3-zBEqL9OEN6qz-gPgNpXLEwMnrruAyTwgIbCqdHmHfFAUU68kWDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پارت چهارم ورزش در خانه برای دوستان گلم
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/91250" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91249">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e859cb5ce7.mp4?token=fJsruDszNy-YGig9-xwxfeACvdkB9Ikxv3HCbkl2klEULmRlLtY13kuWqF5lXgeW3ryyKMmZumOFjqV75iu_NLCszKgtdqGRkpcuhnz7idf6fgEXZLecXH5IxaoO9xN01gM-xGs41nt9X9o8AdqVNvWGbnWxi9pT9snvjkLpSqZKG-f9v8t6Ew-ees5xq10d8p2x-eYYzDCz4cT9V8ezawV4Ub_9ICPp_5n6ooMudchmpLelUB19MbC2KZ5PJx-V5b3g3Pxy5MEVgr9rrQKmcnAMkATO13F79Jf9ZKkFi-1TWxQf06ozrhhBHttKfn4Z6G4ncJ5SDb9EkHAD1Ugb4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e859cb5ce7.mp4?token=fJsruDszNy-YGig9-xwxfeACvdkB9Ikxv3HCbkl2klEULmRlLtY13kuWqF5lXgeW3ryyKMmZumOFjqV75iu_NLCszKgtdqGRkpcuhnz7idf6fgEXZLecXH5IxaoO9xN01gM-xGs41nt9X9o8AdqVNvWGbnWxi9pT9snvjkLpSqZKG-f9v8t6Ew-ees5xq10d8p2x-eYYzDCz4cT9V8ezawV4Ub_9ICPp_5n6ooMudchmpLelUB19MbC2KZ5PJx-V5b3g3Pxy5MEVgr9rrQKmcnAMkATO13F79Jf9ZKkFi-1TWxQf06ozrhhBHttKfn4Z6G4ncJ5SDb9EkHAD1Ugb4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
به‌بهههههههه یچی آوردم عشق کنیددددد. آقای کوکسل‌ بابا برآب کشورش ترکیه چالش رفته
😂
😂
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91249" target="_blank">📅 09:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91248">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHHb4Jz7ZGu0mquHMYrI1olD7PnKfpdAiacocXH7pELpbI1m53YP7bo4759oDf_ln2oI-GbPg2w6aeYJGEuQRzBr-yPP3FKwSnFiSz3tGZt0H3PgFyFF1kVF8SxEGbPSy4zOHYg0ExsmHm3LFoTDU883YqEE3erwkW0H8w0kZc8457N-eMuR5zBm_9RaPsZiWLyjEBksxNfK2yLfz1e8d-e-_4KGnegJ2okYCTSls8UWTGF39fznXE-UzJncKQnM_q8GdvPGnZcVPGKZf1i7ezknztTbH5-QvrdAK1_H6fIpa6CiLyAEHwoNLKqoADuCdTN4My87zrdWnKUvGDuBIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
هموطن ایرانی صبحت بخیر باشه؛ در ادامه فیلم‌های هالیوودی که تو مملکت رخ میده، توی ورامین چنتا دوست صمیمی سر یه دختر باهم دعواشون میشه، در نهایت در جریان درگیری ۴ تاشون به قتل میرسن و ۳ تاشون متهم به قتل هستن و منتظر حکم دادگاه!
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91248" target="_blank">📅 08:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91247">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJimWy4l-UzfXmtPiV_9ljJ0QtbWhUe-2RnVpEE0MS5B27Tjr_-TOD4_Sdg5flRbowCoIMv-P4sKdLD9K6phDkNPqTGEexnAXRDjhMb7Yvn1JQj041VJ5MtXJmC8VnjWMhkpgv1RpJEuBFoJbUC0pAl4gpU6olcIqMrvCqH1MZYwbkRhv5zq89H46582decL2Q0p4gcrrXmj4MeQwnnP0hhc_bomynFO_BqAVTEMFUkY09HshSb7ESoskEK8Li592t24awkzx_WdFPPw1t1eDYyNmZkGoWLlLpJmZil9isEEhpxI1hsSCoL45pWfzNkWmhKf1FRb55CVTYoa1IHg6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91247" target="_blank">📅 07:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91246">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=E3vZShbRZPhoGgPHhRpnhJDuStmWoQYfd6IEIWt3ZGfMOXQ6ANMd4M_2cTVaaeoyH9fqIa099yx0J5XWJHWPuZzCvJ9QXIufI_42tRCM_WYDIY69qGDK072S7vb-cRhoAR7WX1bbGXbQ0tPM4aMt6KWMCemi7gpAaVr1Tdt_7dgZUaw6CRXbZYzyjY67M_LQCk067-S-8c7gj894NMkAgNDgF7o6Lzp7ACHDGSoDmVPepvE-NKW1xkhnzwcX2TLLNG7eeimvbPLuF4LZ_tLIgAPlKy2y1kp1zy1Cu81WXdFhmN-nonsiuaB0sZSe7tW3R-7DUsEfh0q6bYnLVi18ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74203b9c2e.mp4?token=E3vZShbRZPhoGgPHhRpnhJDuStmWoQYfd6IEIWt3ZGfMOXQ6ANMd4M_2cTVaaeoyH9fqIa099yx0J5XWJHWPuZzCvJ9QXIufI_42tRCM_WYDIY69qGDK072S7vb-cRhoAR7WX1bbGXbQ0tPM4aMt6KWMCemi7gpAaVr1Tdt_7dgZUaw6CRXbZYzyjY67M_LQCk067-S-8c7gj894NMkAgNDgF7o6Lzp7ACHDGSoDmVPepvE-NKW1xkhnzwcX2TLLNG7eeimvbPLuF4LZ_tLIgAPlKy2y1kp1zy1Cu81WXdFhmN-nonsiuaB0sZSe7tW3R-7DUsEfh0q6bYnLVi18ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیو کوتاه و جالب محمدرضا سنگ‌سفیدی بازیکن تیم‌ملی فوتسال از مراسم ازدواجش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/91246" target="_blank">📅 02:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91245">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4xu5G6bSsnKZ3eWOcsx7EVDbXYf3KEfp3QKtD9qfNp5ZoEQzBp7sZosY4-wdpdr4elS1uYAX-9W8Ivg3cATrkhuL9Ws4qRJhT0uKi1azJMwJfhItbNHSVupasxxkb2sfi9ZJioj-Wd3uUjT2jQJ0ckpcIWxPrnJAd3BHAeC2i2PSeksuVOuZ3ub9ey-tG6l7MNaM3a9JGzyryPwEXvqenhuFWdXo5WfZha3ju3IiYi_Hp0Fmw5JhtDjVc5L9b7z2eABkEO0zaBnqYP_7x8E0tTR75csYQuPMzvYGgQz4HCle1JkbhiwyxMSDiHa1QSfEamtg_QInMba-1-7V0BY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توان مقابله با این طوفان و این حرفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/91245" target="_blank">📅 01:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91244">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🎙
برناردو سیلوا: بارسلونا یکی از تیم‌های خواهان منه. چند گزینه خوب دیگه هم در دسترس قرار دارن اما در نهایت تیمی رو انتخاب می‌کنم که عاشقانه من رو بخوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/91244" target="_blank">📅 01:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91243">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhtBQ_rowhQU_OlWu4dJGkqRUHlJ_M1PytdTN4u5CzovtShevFGA-qE6M4rWK6Kpo7eaPVA9J8BEMNIZTCmr0jE671glJR9sAyo0XIfvPle7zGHlC6G3yeJhTgiDXExhRqW0OebfvsDdtW6MmtMucDmndGCjhh0mHBuUVBZD2CcHMD-W5Jsnxxw3ERJyBK8xdvn6c4AQJD6rmYBOGOl72-fMJhz0etm0spydsuAh5BcUi2c1Ou8e0I-UWVemU_smcnfZJFLX7LPehfrVRz7YJQGQBroyyMEwKrLRekmcEFmaQJT88hM7IjNf2GoW6_PxiXQeYnN8oTLucoOKa2ooAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یجوری استایل زدن که انگار نیسان رو اسپورت کردن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91243" target="_blank">📅 01:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91242">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42162246f8.mp4?token=auihacECDIosX5aU0jzwaLIticdxvqO0GbrPayLk8UfpW8m_1zk4KEgHcJbZdYsTJLtW9A8d0NhNwZlb_hprEpU_AQIsa92fiPVj363DkxFcyhxg9eHOAVyYo20E2iNUFa8P_c4LfGKBxnMPkN8GzaTGOG2PVdE7SCaZPqWUm5CPheJf3jV3-cmf28yF6yqtw9h8VmQoyePmAG-c8i1KxMPVrjrLyJjwEr_iBxd8f1GLVzATQKYjoW7VDz6lddoWdmVhcfXH0oTZmANmH9Nw5MACBBDAd42VaQeHy2reo5iM3av1-bYJfp-WCotgAS0vqmVFZEeALsz0YAJozT1q0KXumLotzRbuUlA2thc_rX_CuDWhK2j8a5S5uKmSC10qh8pzunOWDXrsh4JFrfJTa6JueSk1aiG59GjbOmOkIeKpB7UK2IG4CLk_X9ek1uVPalDgZlNV3iknWMb_SFlI_XerjXNH7inlm2el3jibYxepyFRgbnJEwFtq-F4aVtaVNz6y67PFzjRB8Hi5rKJdmInEJSP_4d56__o5WdbKTZR69q8IkgmoT0xKF6EbegWYKP8ssGXgOG0PPslirsmzz3R239jdVdbGV9nLh57azB5fhjZcKWjSKj6phRCA9oz3_Sz3U7XCddGHqAI2SVW3Du0CMYmU5BBefg9-aRNdH_E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42162246f8.mp4?token=auihacECDIosX5aU0jzwaLIticdxvqO0GbrPayLk8UfpW8m_1zk4KEgHcJbZdYsTJLtW9A8d0NhNwZlb_hprEpU_AQIsa92fiPVj363DkxFcyhxg9eHOAVyYo20E2iNUFa8P_c4LfGKBxnMPkN8GzaTGOG2PVdE7SCaZPqWUm5CPheJf3jV3-cmf28yF6yqtw9h8VmQoyePmAG-c8i1KxMPVrjrLyJjwEr_iBxd8f1GLVzATQKYjoW7VDz6lddoWdmVhcfXH0oTZmANmH9Nw5MACBBDAd42VaQeHy2reo5iM3av1-bYJfp-WCotgAS0vqmVFZEeALsz0YAJozT1q0KXumLotzRbuUlA2thc_rX_CuDWhK2j8a5S5uKmSC10qh8pzunOWDXrsh4JFrfJTa6JueSk1aiG59GjbOmOkIeKpB7UK2IG4CLk_X9ek1uVPalDgZlNV3iknWMb_SFlI_XerjXNH7inlm2el3jibYxepyFRgbnJEwFtq-F4aVtaVNz6y67PFzjRB8Hi5rKJdmInEJSP_4d56__o5WdbKTZR69q8IkgmoT0xKF6EbegWYKP8ssGXgOG0PPslirsmzz3R239jdVdbGV9nLh57azB5fhjZcKWjSKj6phRCA9oz3_Sz3U7XCddGHqAI2SVW3Du0CMYmU5BBefg9-aRNdH_E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⭕️
به‌روزرسانی شبکه World Cup HD
🔴
شبکه +Mifa از مجموعه GEM با هدف پوشش برنامه‌های مرتبط با جام جهانی ۲۰۲۶، با نام جدید World Cup HD فعالیت خود را ادامه می‌دهد.
📡
اگر این شبکه در لیست کانال‌های شما دیده نمی‌شود، لطفاً فرکانس زیر را دوباره اسکن کنید:
Yahsat                 /          12034 V 27500
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/91242" target="_blank">📅 01:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91241">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
#فوری از خوزه فلیکس دیاز:    ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91241" target="_blank">📅 01:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91240">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF_q938MjUaSzlByYpNwmxPXeWAvB7N2sZgFTF4MkQSy9i5H_WkFzw4SsPxnYTFSSuPyY6d2d8_XpFv54A515efYtigp40epRHAwAJ25G4dRRNd0gMsUin2fs4TxJ1-Aq-tmLOXkOOqGgope4gHmsUdAmJqHVR0XDfpWucEBNknzKEhRts_ehBim0_1UlsRGplNP2NcNfGWARZ04TBJdiTnrP5XeKnkEzODyraVsY-UOnNXgX0-uV_rIGMlBD1JL1Z9gIPy7To8Y1p9nc_AzSQirl17BQTR5QZcQVi5iotnC2_kU-gD9aDGHaGY6c6Bs1T0Yd8me1qjhy042wXYpVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#
فوری
از خوزه فلیکس دیاز:
ژوزه مورینیو رسما درخواست جذب برناردو سیلوا رو برای رئال داده. رئال مادرید چند ماه پیش از جذب برناردو سیلوا خودداری کرد اما با درخواست ژوزه مورینیو، ممکن است اکنون همه چیز تغییر کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/91240" target="_blank">📅 01:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91239">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBJ7Qm-hjmULXCUeYGUIBHTdNDlM16GDkJkA2SYgeduO3FFiM98DK-idXxnyG_b_2qeia1QqA4L6k5qvhMN0Luy4Hx2QpNE4xQudJ1-dsy9Kher4Yixdgq0q9rhszGtb72P7IUbkmiomojJy7rP08rdcLJwChB3ZjoKADur36U4Ce6PM965E-Zri8rXLrgod5kikNFq4Y3RnWBQXq5AJZgdvVzKZumEzgu57Ylv_76yOziPUjw4QIR1Fsp-CzDtgjKoovwPKYyZrOMCJEEzWa9LtE9biWeUT3oCKgsza6BgKKIySnvS2yd70RkSYpPafIw33NXqbjzY2NsqMfAsPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5 روز تا جام جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/91239" target="_blank">📅 00:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91238">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=b2h9_9ocblceELWgePWDz_GqBOwfnBTM_cRQqRpE4G-JFxp2HL6JF7n0ufbQclFwTctCukDEEXtDlyoiiGCr2ZXPeGx8ziPsA1ywLAaznyACEyoykiIJ6rRfL_-IBH7Vd6PO5qQE2AXodyz9uP6_3UWHH5EKEL87tTautA82PveqjdP8bywCHoyJBU9yZAvD4ARCWAXAQVkEqnu_WTf-byKww2vhmSErNvNAUnB-w1RceHrV8RVpYmsB9GcUIzHU0-ZpmkoVWMuQVuHud61GZ3LEHCvyzxWmZ5hRWeCmCMzo_b1_ejVPbeSQ2sJgeB6ER3U5AB5OJFwMkBEZuSSSKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f6380c33.mp4?token=b2h9_9ocblceELWgePWDz_GqBOwfnBTM_cRQqRpE4G-JFxp2HL6JF7n0ufbQclFwTctCukDEEXtDlyoiiGCr2ZXPeGx8ziPsA1ywLAaznyACEyoykiIJ6rRfL_-IBH7Vd6PO5qQE2AXodyz9uP6_3UWHH5EKEL87tTautA82PveqjdP8bywCHoyJBU9yZAvD4ARCWAXAQVkEqnu_WTf-byKww2vhmSErNvNAUnB-w1RceHrV8RVpYmsB9GcUIzHU0-ZpmkoVWMuQVuHud61GZ3LEHCvyzxWmZ5hRWeCmCMzo_b1_ejVPbeSQ2sJgeB6ER3U5AB5OJFwMkBEZuSSSKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
🔥
پیش‌بینی مارادونا از قهرمان جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/91238" target="_blank">📅 00:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91237">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkTh6CckpnLeWrfTkvGkThsfua1HofxR6YSb23ZyzSvX932daXT9lQgCyjW7SplsOzoKXzi3E1-y2bYsk1Py4l6OuLUkwxsps4VA7v0pQv4G2coOnwMC4L113HaxPjdbPFpD2ZPM0RSiZmVfIJiYi5ekFWPXvO1dHskC8b2CCAgL9fpO8dAqaR6Hj9l7E1vJO9ss4w0p4QXm7rvsgphhUOBCBJmzd8uLb2XcGPGZ7Fno26LSYox_0rIaHLg7C2LuIcbsRq3jgI5n0bko3zhsmSJAAaJ84fEA-0VAABRYAzNJhe68d7NyA0S-o0zdAZrvx-G_q0hYQJRsqTpuVzodnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پردرآمدترین سرمربی های ملی حال حاضر جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91237" target="_blank">📅 00:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91236">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk2RND1_OBLBPblZMbVey-M5kjZBpdkmw9VWXpbfddJwaqP-GJukxLL8d0aI43zVkUnLpb9_uucIhTFedKfHFyCRvtRdh6_1U1nwW8PcxZ0Ro8VJiwSlhwbGhRdwzMQ7hF6CszVLawxA4KtaCVgYRhdcth5NlucxkyA3HSnyf07YPzKa_U0BHhCS0UEy5mlSsaBr5CAp0DsJSC2qEAm7_iyTrZxzY00uK2BM-6ybOtm98126qVYjj2vUSED-P_K87joM-DgIVcSCRFSxgH92oAulGAXlJTqoUQXDL0YsSShdiYV54sZcJoWIBU6EJmtAxQZevL6QbIBqHTbTp5vpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیلور سوئیفت و شوهرش قراره یه مراسم عروسی با حضور هزار نفر بگیرن که اینم قیمت بلیت جایگاه هاشه، ارزون‌ترین جا 8035 دلار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/91236" target="_blank">📅 00:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91235">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇦🇷
#رسمیییییی؛ مارکوس سنسی جانشین لئوناردو بالردی در تیم‌ملی آرژانتین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/91235" target="_blank">📅 00:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91234">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JOh00t2V5y_j4m4OHl6qBkHekVo4ckhJiUPmTBPkr0rHRQvkV17BcuFHGSAmPUlMrtxuZWqihImX7Y1TDh-AHIfJAEdz9bF69N7kGXw1jc6qzhHD20KP2mIKUNDAsAlIMgy9CVQ4xA2BMZhYUXNRKn-F-dMJMGLf-xli92oU9fIwBoEZLcM38W1Iu9io9TvoJJ_MVgGdQ3KyWFCksi81pwqCiwSX1xwGt17FWE26eXh6zaGCTPMTrSxwIjlEztXXxmMq3RV7fUxRHf5E7D2l9ZX8TGoxhGJGy1Eqs78w-2jCgX1sUmHHZe4oHV7SlcODveTWyYjI-nEC3gOvjdpJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
اعلام ترکیب برزیل مقابل مصر؛ نیمار در این بازی بدلیل مصدومیت غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/91234" target="_blank">📅 23:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91233">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=BR_T5B1ulPDTvIbLIOHVF60QlvWgnR1oY7MF20_5f0Ae_dED16bNoYvtXP77qO0ALcYbY8b6OqxpMea4ydGYIUrcivj7YTTQTuoGNwzCWGmBw5lkNocHOZRvhmPsov0YUjiq7ojvt5Fv1QQQjEMUVfXz6nrk5ungeRF3ieuis1hPRAHGJsNmiovYVIXTRLvoSMMFKov-L74W5oEKePEkwJiFpGCoCj0OHMBLUOITD2im6ZAni451SjM3k6Ah1ec0R8Uc-b1ywWvfFQcC1Sba-PVo4nK_UlJ1sYJBy4JlN3xxAWXDD0bkPXDL1FlqlrngZgVyliE-4aP-VIUobacVqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea39da6f0d.mp4?token=BR_T5B1ulPDTvIbLIOHVF60QlvWgnR1oY7MF20_5f0Ae_dED16bNoYvtXP77qO0ALcYbY8b6OqxpMea4ydGYIUrcivj7YTTQTuoGNwzCWGmBw5lkNocHOZRvhmPsov0YUjiq7ojvt5Fv1QQQjEMUVfXz6nrk5ungeRF3ieuis1hPRAHGJsNmiovYVIXTRLvoSMMFKov-L74W5oEKePEkwJiFpGCoCj0OHMBLUOITD2im6ZAni451SjM3k6Ah1ec0R8Uc-b1ywWvfFQcC1Sba-PVo4nK_UlJ1sYJBy4JlN3xxAWXDD0bkPXDL1FlqlrngZgVyliE-4aP-VIUobacVqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی داماد فوتبالی و رونالدو فن هست و اضطراب اجتماعی نداره. خداوکیلی حرکتش شاهکار بووووود
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/Futball180TV/91233" target="_blank">📅 23:36 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91231">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oV0pxiYMrWDDkxozU52A_IYQg1TmrWv_Qee9574iqJkWJ2rvF5VCdi-HoWHa_mafEWlysQYcLlX0JEmSjir4-c5vzqelZxL9m7N9noFOGEk6w5y4XOVo3d7K9sSVE38_J-vQDGdxYGitc2B-mNKueIwgtSd548XI4pRPUthBDBbBCEWsLn7-G26CXDFQ1AmeefC00H_Ma-HOR6gvU4026ydwTbWY7rv7nJzUGI42nBmD9tbD1WbyfkQFa7T3soBg_9oDetvVPqq4VTaOYIywKiHKhSln_yicyxBlC7ET205KxL_RZZh32hy2CyCJiMQDYcaztk6bkqm86voMGpUVqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
❌
مونا آذر پورن استار ایرانی هم اعلام کرد که قراره به کشور برگرده و مجوز داره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/Futball180TV/91231" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91230">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=ATvGgr9nKPtTNFbWhhWorcuSnqAu0-kkEUAUQ4Z18xBnSvltaUnjP1iHPdjub6nwlGBysTHaCnbXIebl8_lnHqal3tA8RG60uctts2pd891DABldB3FLf8gvw3IlOJ-FzR7F4kYTboQFynfMRL0xVnCYK1gpBp1vhN4UC6i2-sFwnLYU7aqcwqk4v9ZjGIh0m3gNovxaM9DIy_Yo3lX1wemOaJib5o4dH1azpJ3Qr6HQMWEqDOxc2jQueAzGGN5FV3PVonHgfRBQkmM3TW866Ge6sU5GVgnSeiHb1z8_f0YZuwXulvH3_N-S-d2qoBLZ3l3DMAV77xHIQoFTxzr4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a25be77cd.mp4?token=ATvGgr9nKPtTNFbWhhWorcuSnqAu0-kkEUAUQ4Z18xBnSvltaUnjP1iHPdjub6nwlGBysTHaCnbXIebl8_lnHqal3tA8RG60uctts2pd891DABldB3FLf8gvw3IlOJ-FzR7F4kYTboQFynfMRL0xVnCYK1gpBp1vhN4UC6i2-sFwnLYU7aqcwqk4v9ZjGIh0m3gNovxaM9DIy_Yo3lX1wemOaJib5o4dH1azpJ3Qr6HQMWEqDOxc2jQueAzGGN5FV3PVonHgfRBQkmM3TW866Ge6sU5GVgnSeiHb1z8_f0YZuwXulvH3_N-S-d2qoBLZ3l3DMAV77xHIQoFTxzr4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇵🇹
گل‌تماشایی برونو فرناندز مقابل شیلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/Futball180TV/91230" target="_blank">📅 23:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91229">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZJ-bCSMGuqaCcK_0l9hv-S3dg5J9AHqRYpSImorM8DQKoU32XNcYUXGreEYd5ZVKR-BgHiQY6pHtOF6MYinpfDvbI3Eb2RvVFFgkIvjzYfSfNpWxhEFqM5Tfngkrw2sGo9mOsKE-JSKvRtoBGK_Uln6vzArxsIRFK3nroNQ0MdTvPhgI4xUSv10ymhNXBVsePTrc4NFJXJfbdwZd4YMZm3HaFzTtXhV8kPs0iNZfUo9OkL9FHa-SvT48jqUOrPiR3fCz2bgD1423MSTKunnhCj_9m5wbyxt-gSdKsMIV07c7daQWpxRaLYcabbZcxfluZ3fW4G2xWKkVhx-BofDhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وقتی میگن پرتغال قهرمان جام‌جهانی میشه
همون لحظه پرتغال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/Futball180TV/91229" target="_blank">📅 22:55 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91228">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=swLTd3OVewH61AE8Vpe8QcV2Tb86vCzBrxH_eHpfXVa0MG5rfKXJdtYyExOb-6BCZgNB6yc2EaHxaVXqtx9gNWA1UoodGletuqCMzNSAcjcCiXfXf8YJbWjg5sCShypO2BvdzRD7GXD1QAX9f1ymjED770gl9AdHMZVJhzMCurb2j2RGetc7o_fdPie0KngI4D-11GamCAqCIkdgiecU0zPXOPtu3NPflPqx3SILCnMQfWtTtsuGKR1iPz-nvUAiY3s32ftZtjSefnPW-JV2UzEc-8KkutJEIpYNGAg62CEgA8IvzMtFZk61-_K4RpjP1zbVMo90I9wXpQhceSIOLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1050253ed.mp4?token=swLTd3OVewH61AE8Vpe8QcV2Tb86vCzBrxH_eHpfXVa0MG5rfKXJdtYyExOb-6BCZgNB6yc2EaHxaVXqtx9gNWA1UoodGletuqCMzNSAcjcCiXfXf8YJbWjg5sCShypO2BvdzRD7GXD1QAX9f1ymjED770gl9AdHMZVJhzMCurb2j2RGetc7o_fdPie0KngI4D-11GamCAqCIkdgiecU0zPXOPtu3NPflPqx3SILCnMQfWtTtsuGKR1iPz-nvUAiY3s32ftZtjSefnPW-JV2UzEc-8KkutJEIpYNGAg62CEgA8IvzMtFZk61-_K4RpjP1zbVMo90I9wXpQhceSIOLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
سوپرگل تماشایی آمریکا مقابل آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/Futball180TV/91228" target="_blank">📅 22:53 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91226">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5RJWUVNK_EZQci7B1KF4X7EpZWqmHpzDHoa127InHadAoUhrSTEaDo0Nx9NVZb0SyP0kkdcsNZyA_vB_O-iQSZTIcjGjei5-d5neAUasEUniSjveoV9dubZGPC8wVLUdS3w5CdS-prXTrVqv8OngXRp-8sFoOcXdpVq2_4tipJled_tYDBjkcA3UqSqfUmcxagdlRjChoKuixkmX_BsRKDcTOIm5OiO4BZ4-_Zo5iyWhM36eYK6PKW4UJPaLWCv4HrJjHfJdywXzmMGDQHHynKfdp-Xq9p1j2PJdaPoQjGOnrEFsNEZ_rvKLD0Mj7uGVkoZlmGpzqoTt8APXHIA3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ig1yLKzE9JZ946dlMPIVrQF_DwFx949vaFjnNEe_ZoOOXQKZpYXovzl3uNV_nmpAkd3Zo3pX_gI_Wau8e12mbSru8Hvfx0eu49Ml2JWIHJFk7GBfyx3EUONlTaIIEyntkLqhxhIfc6VoBi0qm9H6XF2jqNYgZZwh5ZB8dBQ9JD71NRZ2bKBXse3Xj7LtuRCQm8QTjDmhbASo4LbOW27xORxAv4Tbu4sjxQ_fOnnWhBEXTp5Syps0m5EWc-g97g51i6xFQ1g0ByYq4CpFp5PpiEeVRlHBfQPvoZnBgvV3wexFrhtVKqM3c-ASeMgU-7gZgfmAM_T1ecPNH3i-wN6_Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🙂
🐸
ضمن عرض تسلیت به برادران سرزمینم ایران باید اعلام کنم که کراش والیبالی شما یعنی خانم آیتک‌سلامت از خوبای والیبال بانوان ایران، امروز رسما و شرعا ازدواج کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/91226" target="_blank">📅 22:45 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91225">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saLgKR-noc50Q8sZziQViv38JQ5ntjjdXHIY5k-nIgqrrLm50rZrscQb9jQ05RqUhPLMddfSnofwa7L7iLLnilFLv8coeafpH6l008pMkvsawVHP9Tczk5675rZuv9M0e7hgzxnPY-vy0umGMC_LbjOjL6r-JYp_GvyompAWZ4tRFbrIda0KxHuNahRNmDJ9E4FXv9SsJp9AzUNh7aiHC8-SaxAWdr6IdrGQWAjPbNnaIA2Twr5SmpcFmDYQVB5jJ_jNayELSPnB2T1KPwfqivMOiBjtP6FqxW6lPHQHt10N3w3eYyus3HWUApjsU3t4NMAWy8oZFP0AUCCps0HKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
شرکت EA پیش‌بینی می‌کند اسپانیا قهرمان جام جهانی ۲۰۲۶ شود
🏆
.
⚽️
• این شرکت از سال ۲۰۱۰ هرگز در پیش‌بینی قهرمان جام جهانی اشتباه نکرده است:
• ۲۰۱۰ → پیش‌بینی قهرمانی اسپانیا
🇪🇸
• ۲۰۱۴ → پیش‌بینی قهرمانی آلمان
🇩🇪
• ۲۰۱۸ → پیش‌بینی قهرمانی فرانسه
🇫🇷
• ۲۰۲۲ → پیش‌بینی قهرمانی آرژانتین
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/91225" target="_blank">📅 22:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91224">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIexZwL1CIhoqCz9zfKpIEbdVF_IoOCzg472eGw9eAezVjpsrB9oVFPPt0XdNl6jvnPljvl-RAVgWYnHTCiis7IrI45gRdGzFTmuSwy1L3UAeZXHVmElyK2q6rpBRT6gEgNx6hGrevh2CTxD5FOZHM2HUvrar9v9LX25p6kTY46jHP0vSeySxBE4gTP70a3ymW3jxXo_jwyYeZmElMoJqackEMKdy0RhvA6WMtS89l7R2kQvbpYS4knyYJdZUyhVa489SgMEyLrryRKW-c5nKwcIhX3ifkfTTlbt08ho173iDeUGtPnCuDHmPNOVME47qKRDHE8Zm8ZwAOi6yUnNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاماوینگا بعد خط خوردن از ترکیب فرانسه برای جام‌جهانی، پاشده رفته هاروارد برا ادامه تحصیل
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91224" target="_blank">📅 22:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91223">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVNLVbUfy4rNO233CakgDUcgMSf71SDFXGIXp1iOVQdMunC9I_gZRZ8LWWGmhiBtC2JnRvqhJonwiys5CK6h9VUQfGO4U2F0sE4RcfIJjgAaJPbwJFfKyf3NyPhOdolDr0IvnXtxh9bjucnMep0I4cu_K-6hVbE81CcMRzlJeBmnA-1zlq2ZPcOa5CNAN7trn_RZ7_dyyOEqB0higo9VxR67UDyRPPMFgtZVkr_Q5vqD8YCAKRSzEzhntkK7-HoOYz8Lm1Q7pjIvAue39jfEN6Q0uFnmdpQyc26HYuRLp3gTCNbWzh0N4PH9KPgyrjlrJsCMC1iO_S9xru_o6I-0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
⏰
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/91223" target="_blank">📅 22:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91222">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csMLWUt7LvlO6Ne67vsWIcuDJQ024zwXHW4X20U2DMvzJtBl6Vv1M0IDTghFbff7gzFB4snp6ZqlfbkSpFWbQU83fpVXUQ5Y8nQ91n0c8tVH3TzxlHcorniJqwiWa6EIntluJLsDZ9tVfY5IvFqO0xL3fkarR6kEJcEZ7BpUXmIa3puBZJHq5sbMalvwZqRzOFNbGmtCkpbQO1XXa9z1hbwr74LrTPBunxzKAlXMD4IFzhaurpPZUqSaHj2XO70lM-Zp0k3Zg6q00mSKcbOm3Tgo_K13M5dNLNj5WyhXb0o_QTn1KJBmiUrXmrY88oAUIYi-pDDgyDTXnpdFRll9dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیائو با این کار اگه نخواد جام جهانی محروم نشه باید نماز بخونه
😂
😂
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91222" target="_blank">📅 22:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91220">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbaPEgyBqqzGRFhHldaGpQtcFucesy2BXM6coU2kjDv50d1u9OVNDSJGKRIUZRe1aqtq04B1qgK9d9Xn_gqrahBVDjyO8yDV5EUtY5Rs6Sm_OCsLORlTK-41uyL8gkQRlnuf5XEQO5rGmhktYc8igT5sFBKrs9m9-mMg2v2bTDEgVTvdbCapKr1b8dmiYXjTVCeNON9gyyFuOgf9vnb2wB7X_oEgRsgVBJMuSleoSIxkkBj26R8Viua471-Esz85sxb8_1XQ6fynuzjrbMlOvOty-5RS4UnMNgu1mT6Lcn40s_x3gnKE_orllio8cZ-ltn0F45EALLDWRCaAIjvTcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکاس تیم ملی عراق به جرم همکاری با حشد الشعبی پس از ورود کاروان این تیم به آمریکا برای جام جهانی، ۱۳ ساعت در بازداشت بود و در نهایت دیپورت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/91220" target="_blank">📅 22:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91219">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3LRoosjYGd76dVlwcGaSiZGy4rUtpciyYTjtwoKQ8QAZ1JfdABEBKLJ0seoWz_kgQddlBtozZGMykFP6jBpaOqTE-ij9_ra2emHK9BLppkNY9eOp98ptJzO2fb-VJhJg_kJB_fPVn5S5LfuVoPff9XTpnyoZy1RpoOQqO6b5mKxYvyWhSTkfERaYQY1aAI3-yLG4S4bwuUw0e_W60Nj5N69Ydtmay5mpI598njgM5AR8NU4qJMsTHyokRUDYELXGSPsZFwpsAXMCmzLjXflamYFPJvjY9EaRj6eRTMEpL2dtJBIFrQtQH6_XCwzM1zPuQ1dRj2ke29mTh-kmiyLXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سال 1998 مجله بزرگ FourFourTwo⁩ پیش‌بینی کرد که دلتونو خوش نکنید چون دیوید بکهام سال 2020 این شکلی میشه اما تو 50 سالگی این شکلی شد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/91219" target="_blank">📅 22:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91218">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAKLnEqh9hoivV5KXKxB7LyOPoCaWfQqv2_r_3HbJ_z7wZZvzsSu0qG5lW9260KcZoRWogBj2ZrUOUbRiVxMUU_-AULxCutTbVW1Pbq7wEkvmil2CH77eqWkVqZapfgBfPOvcZlo6QXZEhOyLPkxVJtT0e_tgyBJzam8qLsuFBuDSYiBXJIcLKJYStHt6Tp_jMAoqBIH1oZtH_7_10y1v2wl32Zl25InzMIKQIpOO36bqMx7mN26letCBIGoQwzeR5_5M9nhP-MSDp8BYsVgfzXkNLc2bOIp_Ojr9X4uv7cYUu4xhKuThBcIGnDGDNOyvPD729qkTOB6l_2FR4yEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ناخودآگاه یاد اون عکس افتادم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/Futball180TV/91218" target="_blank">📅 21:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91217">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EiKThQ1VI2fdx8I10cSEVsnt85sRerdY7tvFm-fwEdq4-FLPnaV0NIm8RaI-b-4Es3KZE2YfcjxH_FuMIRJTyhOxJdVM1wy5DyucbLR9CjcaUvXw_qUOVq-MqPHMS9NLE1c5niE4WzsGumolWN7CCa1bB6vZthrnsO6O0E9nBT_h0kCyHYUhmZYfRWY33WIoa9lTJoUhn9diWMEllORlB_rw5saQyoBbONH3Rr6fwmHQwWhktYpbDWXH3acQOSu7Ypxl7yt0QMvW8cwE0nJ5zQsaRF6ua3UBbj3rg4fI0Fh_wibboMgXQJLT6zGyXWJnsX0lvXL4-51_EITR00C3yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپید لاشی چه دافی مخ کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/Futball180TV/91217" target="_blank">📅 21:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91216">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpYwmWbka8jbHrO9TX2aRw3hW7Gc4mdbhxdcggBrMhFus6MxxRU15bYvLb0PvpWYyCTy4AbCesoCA-xPB6fTfJheAHrRjm-49J9NrW3SQmxEKW3nQeXTfOuTLiu0DSzdnBXPa1mwSYQM7Tz7GPyJe6h3P8A598BI3rbr0VwZoQ_hqdPjzIokeMsEdGGyZVYWgBlwvdBdHza0meL65In7pUJdQAQ5QBeqwgq9I2GXFq4-PJeh1nSUu222nJMq6KBeKpoc9IJPoWJbcpOODMwKStCPYMCrZli1ROYAHQSL7BRBrVPLh9W4qqzq5H4K0KQrf9wR3OmhFymHuQzeAUAIsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اولین جلسه تمرینی تیم ملی اسپانیا در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/91216" target="_blank">📅 21:39 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91215">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPgL5xR4Kax9VcJvD24kmTb4UL3NC-PwtLyh2kTQFQEzkI1aWDg_ydtqH_kpJu1celWx0lR25nTzLjHxXxM1vdIyU1Dxs1rT8_RKiCm_QcVubzmksb2VpbgqvvDhjR1oT_mJjCDlogXtKSmk_Nb_1T0xBB5Ow3Qz42--xYl2P3bErpgpMi8FLgdFlz_h8Fi_lBpDxh88uvR6GSLkRI1oJcLHxKkw9ehezrjOPzr6qjQei7oCiEnQnFpkvp483q8Q2nlHdMlf0ifL1TKAkoUX1QcXGWxJd1GwVaKl8nllCZBVSX6QsP5h1ysiR1D7HK6BhhpLAxZS_Yld2spqWVRNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنری کویل یا علی ضیا؟ مسئله این است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/91215" target="_blank">📅 21:30 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91214">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV18HIt1ZKpJJ50-kFTO4Xrowes-f1ORnmdsYqJQlXV5TxnAL1PSghlMr9d96RwBG31wGn1u-X6joYakqqE_SLT2CJ_qR3hWduFzgqxxSPyeAVMJj3MXPSrrZrJP2gdrK_qyT3WFKuqsJfiTkb75EAEQPGlG69K0UzZo5HFc1CM1PGX416qY4tao3V8sDufeCKTmKqPrT9uYBeDPCmo1-In3YipJdBxhrBVnzAv6p0wuxZ6mtxhzhSynZG5qEVs-kmAgl-5DrN5W-ymO9j8lzhWjanmfn9P4U5mzD7BiqweCV2GqhRmARp66HOzcKbEotOyt1R9frgbjbuyAXkjMMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91214" target="_blank">📅 21:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91212">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vht-fwzbw75SyKl3xeUjwZoehtZqaKrH65h57IY9prLJuROOYn2c9O1SHRqNLIJzgNHOFlkz7FhSyDZbE59GoDps_I1KAcUhdGMWeELg-IR1H63SfmgGKr5gawAHxDDBlrHuXP01_dHIXDbEl0vynx8iT2GgnLPxyVCcK91nfj0BqAw-r3vsek03Nc7jT16qpUwzuqYeNaVZqHwY7ZhfuxTmGO-DgJjk9WO-BIUNOEvUPjJ7wPQhUXGwO85sKYWYmYAjXjEpeU4Drog-1pT8H8sshnUjfLM_DVtjjR3j03mOQWv4ME3JV8gdLUwNg_Skcz2vhpwwD6OYUxCSKEl0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qZSia1NRDIM80WACqy17X0MtYfTeTdBmgp5bgxnRS5MiBBgrsVHm5XQA9aPdTxcTvT4PASF6yvf61xeSEy0mGJ7BDjCEV9Ixgnr-WvaGDwmhfnZzsLmjU-NbMXeEdJ3lEfhtZdld7Dk78NgKoOR6HWtzediWF-pX5kCht1Ut767vBjgGEZLNtDgDpSIcn1RL8HiGRktF3xK3Tv8fewEs88LpqpHK1j9K6wUC7VupeFtQOfVIoMIgsZadMDfUukTx64ENyf0kvl9e-ilygrUjtElDjt8gW1NRa-p5z1xY8yWdZee6pM9RP0RSsO9obS2VXlcnnqkGJEsoWCmqJLr7Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تیم‌های اروپایی در جام جهانی 2026 و تعداد بازیکنان با اصالت آفریقایی آن‌ها:
🇹🇷
ترکیه: 0
🇧🇦
بوسنی: 0
🇭🇷
کرواسی: 0
🇨🇿
جمهوری چک: 0
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند: 1
🇪🇸
اسپانیا: 2
🇳🇴
نروژ: 2
🇦🇹
اتریش: 4
🇵🇹
پرتغال: 4
🇸🇪
سوئد: 6
🇩🇪
آلمان: 9
🇧🇪
بلژیک: 9
🇨🇭
سوئیس: 11
🇳🇱
هلند: 14
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان: 15
🇫🇷
فرانسه: 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/91212" target="_blank">📅 21:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91211">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ap1dnTkTXsFon0fjv88_waGno111j2Nh8P86fIbRGL_9K5SEACoIm7b_ZQHj6RpcW_0yW0cuulMt-KqdG-Vp2Yx1hjkDKp7IngWuRAu5ZEiOLHNGTKT0nRpe8uFekkngyTtyhqO50JIr31Fc0xpPnboD2JgYAEBBYTKooFMniSA8cPyFhlIO5q9rj-vL_OobgKM4CtTUCsG1hQSwBMUYgkcDcYADAQP0gssWTmkfREdNJ_CGlm9qrBvWGoW2ihM4p7v3XnxxZXCEe3kL7d0vdEvaXdo5Sinf4qzHgwjcQpf6UfV0ZdUMgyPY30Abg2BS_dfYLB54o3rS0Nyx_9ouRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سون تو جام جهانی های اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91211" target="_blank">📅 21:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91210">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK-TzLkFgZ3Yt0b1w-UjwN-B3_LmkKM4ucTSlGtdIrHpCc6XLXI-GbhvjLZSG4xEf9Ny_d215j_VHP2Sji7SgD4vYmTN_ZJRryyzcZSkBCqNBfXXIOFvZa4wQN4BwaIyA-0QrIxp3YifgEqNJcxmyAEmNhCFNpKSThIMuk79bJwLdga4gryZZNGiHUoIhTuT000ypTbYk1TZ7eU1W0iY374h6bbTFdTzcMur47MMPiBtBMYk4mLyVYEIZE7IcjujyUnDBIkFP1N4BFOFkKvaNIHa1VxKhjhpLgXd_NHmCbS_KM-HJ6Vf79vvQ3Vv-ZS-05wHWnfeATluTTdhhhChmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
ترکیب تیم‌ملی آلمان مقابل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91210" target="_blank">📅 20:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91208">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPReH66o20lSIPQANWIcEBzTbicf8Ao7lzLkupQcEtWS_4Tn7rXndAX-US8cNrxEAV9CR8orkELBjzdu5sISI8rTdq5Ti_F8awSbwDLd4NJI9ukroil_JwoGGXGeswa2ccsm-xcxB1s3yjob-ZAzYoZPPssFitH7AUpdwNoxVC0AzHGnmQuAeNGjXX8BWAV9v5v14Qd286m6ZDHToLgAeOFc69bYEDq0QF9A-vbnDkozaTqjGI2GNSRiP0eAvLnHbeWaOx4d8EQui9am4rUacl3zFEk-ZwtZQvgkk5VOZXz7WEb6wYw4cZBiJx7dCfER1ahZdGIYdiGRxCpXXzCbew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
ترکیب آرژانتین مقابل هندوراس در غیاب لیونل‌مسی در ترکیب اصلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/91208" target="_blank">📅 20:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91204">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V92lbPJE87Yk2zisXi9nrZ0kqTJ9MUjhSMe5ag8XeJC-wWre4l9JXl9anHTU-_shpn6SH_deaVifuK9xR30O_BSyfQ54TTvWRil2rLUASViSedcjj-vLn0RATRzPADAdgPI32Pw1uavAU_siE0nWiyjLKEi5scZHBfLn7y3gSCDSj3oGjCPo9i98vIX8o6RfIidjQFG4RnlBre8t8FytpHGl3EEayCAg5Obxa0IOjKuWerWZ_cZViFGN5ycDFYglh2S9ZR4qIku1Mgk7UKxbDL9WaMoREAKOXsEHvC3phFWAnwj0vQIXT6l_RHXESqZ7ymsyt5eMWe3WCpVAo2VmkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bvTwj4kifcXeMql_p5jet4i4Xro7ySXkrw0m3YeDeFW69ysVGkgEh833Lq1yBRUdanPrNNdpdOlKByut6DjGf6qQtSbkd0krCKZvrnskzMulhlLX7QMiDuYD3ZtFwKO00usRJrjBxDeJ6Q_fTsgDZm80mFgxuWf1SdQuiyvuGXRrFFlA400uTcbul8ReISd6V6gSRugKwkYY881Ab-k-PDZhHb3D0ecfSFri1gAVllsXIxe1JjsG9xFmTEq9QxaSV-Tvfl7JDFJeaUR-NMVZ8AIXFhMIv-pU00RDr1eAKceHdap6Wr4x-xF7ToPLDoX2pI9i9-I75mNvYm6X_nSGVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/veQJ72ZKNYu1QmmSRH5mqdotwwcsXRHTn8hlml47tvRp14vwEU0eF4Yyly5urUfNcTXUwQOpzCtRIl4DRWKsOvxSTPIDcgRNydXmPrjn8uiGplOhInWuX4_XR-nF-gcWw9QUwKGftAHR1wlOHTJZD8miriPxEiJtY2hY_twiydZ_sXxE4JKzzjhikffcJNoU1IPufbRTlYE4q7Msll6C1YA3jsIiwXixDSr692Lcvk5xvvLvLZBCHA4I2Fa33KCaLC9yst6JwU4Gh-MyvyHN3u9MFoeqZCx7ZyFcIrMF3NxR4t1044fYPMsEi4nx5RQBySmkW0ko2hyA-_XMeqK2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzh8CY9KDUW5_Y5hbn9PoPnl9ThVsn5BVZyQ5Zb5Uv_hh65kIDfXnqITfjNz7T9judXhdm6AhlTpDCZ-0G0g2sijILIt-RMQI8L0WVRsZsj4aiyHPwjPm5eJ_9dXJ7JvApzf944x3lQxWE5YzmEGYJ8LthCAkWDhIfB8zEBlwCGsejGeY2dFvCQLIvMXYvD3fjo5qAS_9pYcj5ffS9v3drFOyCfYjo-cLtiWQWF-rdAFyLUO36qofdaMrb9Y2NyZhHIBel0vGwO5kC5M_5Lrpkjhd4ikSFPX4o_zSU9VCKPyz9FtYlGbaD4WLlWgT1vJ1nS0svH5coP76-qolsp-0g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکم زیبایی از ورزش شریف والیبال بانوان ببینید تا خستگیتون در بره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91204" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91203">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ye5y02TQk3fpjeNrDTNRERwlWfGHxCMRIIm2B8kMm3Ml02iykUmHEbvmdbdDbGgGmWUm9oaI3EHZf9rjWqsKYR9-k613WQzFjiCscNCnm3ExQ0d_SQZ65bQNj72ST1_BtTuu7yiwYJj-Rv-gHmQ4OHKOHw1r_kAe4QTba7OFpIQGdFUB3pMkHK0u_L3AFj21BuephScIJS9R_DkYWaRSXVgH184UQSaOTMBijHTSMsmljscwFT1PAbsFNWo_GdPcHCF2ZPwkAojiUV4iRvvKTpGNJn2GnaT5kvK36wdSncUbr_c481il1gN1kLOGNH21apSbLdZKjnvrh9ewvCFpDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ترکیب پرتغال مقابل شیلی با حضور کریستیانو رونالدو
؛ ساعت ۲۱:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91203" target="_blank">📅 20:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91202">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cazsvv9IX5ZNg7fuvwQ3zwr76J1BXLhjywxhNdoXkfl8PO-wVmqdRX6nwvRIy1HZpPcPqzpVldIeUX2KIT5VRYiQ5I4tQEywVJ5N1y9mPbD4yahHICFPufuXMx15hKCx_nFvi90YmH1FB3YqPIxocU1MLIxOIC-bpHXIGxuSvfDgUtptKrYPASNTu7ZimiJp3qKCgWMG2zGnLV133QoJaqiOHy_7ZBlrFkdWVmHxC1N2pL-qe3NcVa6WfM8xi4sWbGa1UAV4Benuxes5-OH0Kp63F3vuYt98NliT9an9wCAXVi-fihnFoG2KPGX6FjUx6VWWplVt3q0Vn2Yn3kcQFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان رو نبینید برای آلوارز 150 میلیون یورو باید هزینه کنی، یه‌زمانی با 50/60 میلیون یورو میتونستید اینارو داشته باشید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91202" target="_blank">📅 20:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SwTAq8AQkvROtxKkDl8bk2Ofm1hbBzdKydHEXXH1yGGwI9PzXyjGTJnd_zM_tSD0lsCylZp8ek60Dd8SRQ5HYNR576R45mUeAvpzEKBRQ5Bu-cNUYNpUe8SJD0-cCPjiZi31MHF3Ycv-4mRLwZ2pvCzT1s7izZ1qdbQDwHGBLzlxKBfniOhQqBn8AljzfpSg53jpHIQxT4sSlkwEn1bmz57CteFe6X7dgLFVbBjDut-PWDxuMeGS34rtOA3vG1VBgs4Ps6YgjlS2wrJHxhtWrivKpqrxqO9CFsxG28jBdo4swrQmXFuDB_oujQffIDWKusx4Ae5jzJ8xRX39s3n16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqWMB8XyIs6drW3gFCFtxR8n_qeJV9nmR6_3dqWqrnfBHQ5LRVEyjcJ3m-G50pIOHrgVPXa6iOKB2F1ziI_TzKsUeLDrWrKGNkeeXwEq5aCXCZZ3fHVhpoSuyaaQ9tBVaUo-d3j1xSnCr5-ICgnga1dq2MyS_JVH8DzJRmvacKMngQFtHYNKrCKyjHytOulFcxJknE8ISiUtKEZ2b4SMDrEfRPdSCjs3vGJOz5fY5ZL5QAJfZC1xXmLWK5qRTdqOnpyqKcDwGy0IPTg9x7LsXxg0v0DVyu8SWD7j37MEKmvV2YkdVrXMGs3HhlN_WLrm0by-JX3Q8X2pV2_9o6aJ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🤯
💵
طبق اعلام مجله فوربس، ثروت رونالدو به عنوان اولین ورزشکار تاریخ به بیش از 2 میلیارد دلار رسیده. ثروت لیونل مسی نیز از 1.1 میلیارد دلار عبور کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/91200" target="_blank">📅 19:54 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffdd5cda06.mp4?token=ltAZkKJd6Cw0t7D1YQsA6gbQKpZjMLcl5aMTao0u2mCpcSW0Mjq-V3JhHYbS5nRMVK1W3s6jA4-OKMCC-jyMhmawPuBBlV_FLNT2tNh6ZykM_nA_bJsx_EWPaGfjxTlSypXf-dYOCHnLD1cn9IrEP4bOy_xywDIbMASi0fFKiXxOWvosd3jer74KJS1osyRPSlVrxsUnac1rW9bIBzo5ahkXNvd1c2nI6y1v8Ujd0uo_M8PfrWr-OYUwA4IfLn8rTdTU7UjP0Yx3bDPy30PNBAjzNFdsL8nT_c8lVLhTiEhaNNtNuAHM0_fNiuWgQZwHwNzJGdGIwW2DYKKdN8hvfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffdd5cda06.mp4?token=ltAZkKJd6Cw0t7D1YQsA6gbQKpZjMLcl5aMTao0u2mCpcSW0Mjq-V3JhHYbS5nRMVK1W3s6jA4-OKMCC-jyMhmawPuBBlV_FLNT2tNh6ZykM_nA_bJsx_EWPaGfjxTlSypXf-dYOCHnLD1cn9IrEP4bOy_xywDIbMASi0fFKiXxOWvosd3jer74KJS1osyRPSlVrxsUnac1rW9bIBzo5ahkXNvd1c2nI6y1v8Ujd0uo_M8PfrWr-OYUwA4IfLn8rTdTU7UjP0Yx3bDPy30PNBAjzNFdsL8nT_c8lVLhTiEhaNNtNuAHM0_fNiuWgQZwHwNzJGdGIwW2DYKKdN8hvfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
شما شاهد عادی ترین زنگ ورزش کلاس نهم هستید( همه تو دوران اوج )
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/91199" target="_blank">📅 19:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqBbxxPai5q8zmoBC6EMvq21eZdJMoo0rdOTEyD7dMJ-ZEEtPP9q1cBR8DPP-DSCu-ETj43T4rkPOnl4OslEg5uActJLCdEHi9qHwWxn8vORqjIZ1DCxXpuOuTywrwUJjEARBXCSg9E6FpZ7LtkTKiWbM5nsz9Se_ciI_Nhty86ZazeNXpdDWK4hRjVpzof6f_wkZFuNC-ESu3OEjpZXYqd3U21EOJ_FkyzfR-8BtExdiaayNH0tkJc616gH7ptbJkkrw26M1LR6rwQYSzMMfSIhQUlXE97HC1wXNnqxAulf7SKoYwdPWpMoI-UTXOaOKQI9C9wmTDWArlR2AyJdMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ساليبا:
اون زمانی که ما فوتبال زیبایی ارائه میدادیم و لیگ رو با رده دوم تموم میکردیم همه به ما میخندیدن ولی حالا دیگه نمیتونن به ما بخندن و سکوت کردن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/91198" target="_blank">📅 19:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtfqcT5F_Pf_uXv8WlnlO95caJ7NXUARNt7QW_79H4kSlcxPTgKOOJkhktU-5IdL4MpM_Tuu2wBxI8kDlUnhjQXEG9G9hwJ4QOxFGw-OQ8GUnhh4jQMUyfK3jh1yNoJ_u4FUY1fUpsUHtDIFsglTQlNlvBTRFpGtN94mFG68iLL4d9aTx5r_AZ6whFqiwJVQy5DTxbnISkjWR-OG8qINJxl1mWSR5-h2U00POkaaaUsPiaGAF0Bq45ZqW9_H93t7uyzk-ppIpnk0bpmvDCcHH_era-7nKSAohslTiEIIK2beS3WuLtMB-Vu9mOzt98kmr6v4tK8MgwThikH7OTMv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🏆
🇳🇱
ناکام و بدشانس بزرگ جام جهانی هلند؛ این کشور سه بار درسال های ۱۹۷۴, ۱۹۷۸, ۲۰۱۰ نایب قهرمان جام جهانی و درسال ۲۰۱۴و ۱۹۹۸ سوم و چهارم جام جهانی شد
✨
اسطوره های هلند: کرایوف ( جز پنج تا تاریخ)، فان باستن، رایکارد، رود گولیت، کومان، سیدروف، کلایورت، داویدز، برکمپ، نیستلروی، روبن، فن پرسی
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91197" target="_blank">📅 19:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYudx2_QyoU0EZwfRIIuBe4xoG4Af8FoKKZuRxP3cOO9Z8_d9S9zz6-JNkVbXgK5a2png9z53-iUOLl6HzJAL5uZop7Mr9MEO5kLrpfA3s-WuzkwpNmfywhdaE1emmr6y3Ov1twAOYc2xNQ7bYjCbUJ2yeafj7ec_yg5PizSLiHNm2dvgXZ2dayYADmJsh-znTle3gosZxyrK0GPHPcvA0_mYfIOtk31eYtsJq7N3y9zbQLqnMScZnxNuxHD3GGwF_sV5r3I8xZSRe5pMPSK8eCgv6raE4hkypqZULURfSF-NoIY5yKsTgVs8R-I0gOue0athIzx3Du6N_1lt-8qbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91196" target="_blank">📅 19:17 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nperU1tBOzcyCWfROGIO2tfL6zdboELNnYzHpo0RwQe2L4NMIufuSFi6ybNiQ2MfrdTt2Q_AzmlOcbABV2yaHY79dykn_ZSGQKb1NhFtXQ0hQNRlEGHukIFjOeUtftQ0iGbrgtw4Ok5L0bsglE3AxOaqsy-dqNuIafv3-jbLH56xfEkhYZA7rEEpPyTjLetb5CRM-_MJzf9-8XyUl6aB5jG9De-UAyCQTqRZehXDKVdF8O1aVqv9gdp2xvM-z03IN-zAeFKbhX7aQkTpkwhsYzOfjzTWIsDrD2TsvcP4Qs1r22uucGHWceXk-U6K9_m6LZRRA4f6byr1szTgzVgZ4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه نیوکاسل چربش کن
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/91195" target="_blank">📅 19:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10990086be.mp4?token=I1ENTcc8kn6w0_4-zdwRj48FcRdEMGeU5w47lheG4q2AVrs5NZX6aN-WxMFn_aSuOgBwNxNsrV943WugX1XI4-TwBeMJ1CYQfIBMqsYepoW_-KnrrJZY9Bn3K0_5CTr7wBUVzyTPMCI5AiE0vafaLLBIV-TOib_eA-2hKB2_ua_TRuz1l9rVx-g5R1PWDQs6pfvB0YWOfQgApbdr_FVw5A5wxS2c62NbGnC7FqeUOCeVQzdvZKiy0kso2KUhr-94Ze62tpegDBRdCuvfj6fOby_nTXz4oe_zBrkjHXfXAGlSEuTApKMy6rMdctbP0OazOgb6z1Lq_Y_O1UJCAzeTcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
چیشد چیشد ازگل؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91194" target="_blank">📅 19:04 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
الرياضية عربستان: الهلال رسما برای جذب عثمان دمبله به پاریسن ژرمن آفر فرستاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/91193" target="_blank">📅 18:51 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb8fab7e29.mp4?token=VILca6qm2gr7v7hNukGoqYpIsi2sVjPj-JoQbRKFUJUmkgQTTI_blDfIAOtZe9e1IS2CQwLzkeCcz4OZBDStKdPQ9vZhuiMmYVk7SpdQbQNAOGi0I8a99BgOt7IjRxMnt3hzgZe5Vc9zxTFKXMrZvmEgfg1Fu74n8u2ooO9K7P4IOm768CzeFaHIeUQ8LyIqimt5qzjhS164FxLY-c-6Kkhr5pkideuRfjLnOlb9SGGvWJk-k1PKbaKn07MXcXgN76buZHcUswoQ3T5biEhLgfLk4MG7SIuZki4-6ojW3WQ1_W_NIeaZ5s6mo-Qs3QcQTFX8njOs4roJQAnE081aZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
اعتراف نیکبخت به تبانی استقلال و پرسپولیس در دربی!
‼️
😐
نیکبخت: اومدند گفت چون جو استادیوم بهم ریخته است بازی باید مساوی تمام شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91192" target="_blank">📅 18:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tavvniJVoYpYUTjFq9885uX261S3BlX9HOUMxbQdBBkhdLWw8REHhYcnUH7rNsfBFn91pSECKHddL7psMdc8n1zL2Y7hA2JG5lGKcADhbBYo-qEdK-5gqs2Y4wxnWNSxCdrmYrK-9vzs8iqFCUey0UbjPzvT_kyvUc-_zlYtsSlUCPe0o50rTXqLigqlLq65TpyCUEJggrh4dk7sIUd5SCLLS1kUwhkelXKMufiZnW6sK5DmQm2z_pHwXFuPaXjqdJ0yz-l2F7aW7nB8f_i6Q4ZY9O_gL8TctHPzLgs8tx9xZZmQk4ZWca354c4d5sYImdktiDafDbeTDND5fxhozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/91191" target="_blank">📅 18:24 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یحیی گل‌محمدی لژیونر جدید فوتبال مملکت:
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/91190" target="_blank">📅 18:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RnsZ0G9YnifIfawEQkt5sOQxP7da35yT_rLafmTb-4WsBn65AmDY7qf7QMr-TbjEacTmwrKgGWkpUt1faY52Vp7pegnpV2zkqqq23Zqkx4zZGQuerL9DWUHeKZ135kI-C4sh6HbGaf1zLFCT-M71ifvdQusneZdVRkdFg4s4XEUIUUacXxKPqSAEL1iRLUMkxj5Ok-s7ox4RDz7KP119mtXrevJx5JFSwRFcgKTNsc3sNgyGgoR9_7DtW0JJAhDqZJ8kEkqSYw2d2ZBrOWWM3r8c16iuQwjDat4i1DUgAEK90i0MzBh1Y5o1pvGjM3vAnnRfCQMiXckO-6to0QSb-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع خیلی خیطه:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/91189" target="_blank">📅 18:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3kwhqAr6Q68ltTL7-HgJxw4n2AM_vdN_jGg60Ix9KJrJTTj7OMNM_ztg573JecpjGbjXGoZ8hSmim0iViDtUkQi_RqqMYqrKGb6fhiaaeEj-36cz2xEOe-9wgzG35bFkmHKq1lqFleyUli_RUSoAQCgRONEOmWVvTwtf_zgm0jOxAptYwS_op4lbYGa_qKEy9ukcY6x8spn9dBl4kghk7xbbVYzJCHIYyKtp_Cwd_pwhg0YIMRC1pH3jUBSC2x1W55l70gzyAU8hLkq8Latwpi_W6xr7p9LkqEa8G7l4w5HdmHHbaO-EiUz6sAOLDj2ytJyJzkcF-8tuwb2kEz39g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
به برکت میانجی‌گری(همون خایه‌مالی) برای جمهوری اسلامی، اینترنت جمهوری اسلامی پاکستان هم دچار اختلال شده
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91188" target="_blank">📅 18:17 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
