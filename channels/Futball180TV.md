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
<img src="https://cdn4.telesco.pe/file/ZXgNxLRwGeFgrDEcxLYBwncoRleNzzsGzS8a6uz6ogWlj1d4lmtFsDXOqTiNH5_ohJqZIP6j5NfKEaU4s2RlIUy-F0rbA3C5_WR4OZ2oS-jMQLUXpXufhKVtdK9eR_M-9BlOIA419_nKHySppgwFZoe1kr7MDmGp_DP0LWTxAQe2sdBbD3lnrvfxLOwYXfLqWqY6q0PqcWLpn6hqwItlWNEqfa0NJNCHOs-9A4ZDvJmVasBlSKxv3LdpHawF-cwQsu9j_ErKIHRl4D87sPAIZ9_xrFOJjf_T6EUsyxX3l58GQUmy6gIfFmhuZ0vS1DOm6sjppqDJfOG83Y70s1OtbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 124K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-06 21:09:14</div>
<hr>

<div class="tg-post" id="msg-90300">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KInlT9wEkb3vaIuEqlinV4EzZw_Hq53bRXbwjQ4-uiVjx0xxQkqplT2cvI9ULRBd0l-vxMhaoea-A0OWeL_iwFH2gZ7rCRdWk9SPZx6NLloWAp_dCOUAJyaj_keM0Lzh5q7HuFODt_Rgu5_lpapQHymSSoxptu-hHePMIaZDA2n03jiu9_9z7QD9gL5745wyaehpS_ZLgkHZDctw7kDE_T1IXbSeDjVKquHUYiW0veP__StD2Wp7lOD33S5mQtewaHkz_hT59EIRfyYGd1MkYOm3K26AKRD3goHqdK1FFGf8x7Gh6yYdu26GGKUl__BzfEbERiZXQVjOozBClsaH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات‌تاریخی از مراسم جدایی الکس‌پوتیاس ستاره تاریخ فوتبال زنان بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 832 · <a href="https://t.me/Futball180TV/90300" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90299">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q-trhlD_zjHfP9Z1RBOA8c8q0NsYhyPezdNUpaH6e-hjIuSZej5JtJLnSZQVoYX1NTE_laNDErlBjT4-UFu5jND1Cm443lzHWM-W4mBXzRTmk1VzOPdEunz1qOsw7OTfj62Rs0CY_2qbncA0J5Obh_Rshc5F-zM5fU1vRbIRWXgxlD3bALyxVG4Chy8WZX2Yhi31CB9MtA2Gv8DdS21XD8V9nWequWrB2j7MqNPWiS_ZaSG9Cm9VNotzrZYVy622SEEGq9pnrDM15CJRvakRITh0EkXEtpWLhY-aVuUPmOI-eq6pm8OPx8bW0hROA2HP45mobtrUngDolJxbsJnKTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قهرمانان تاریخ لیگ‌کنفرانس اروپا به مناسبت فینال امشب این‌فصل از رقابت‌ها
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/Futball180TV/90299" target="_blank">📅 20:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90298">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a28e2aed.mp4?token=pVF1O8YNWNx5oGtz249NF-_wpSku1kW4dPFXp4WTYoIVkyk1sru5KktfV6bSwPwmaGx7ng8IYot8J2JHpVoxDk5e1IZcW5a1Z1w390n_p2FEI8HaKhqvQ-u7DVn3_4OTuoEXvXWtl19BiROn_alqAbrK9PEmtGD3sTjyaGeJ0rnwqDWKW9elSm1tA6Bb9u6rw5AAY0z8SfPLT02zupw1q5bChMntp4Miyf7jfwsZ2NEyP_3ihHEsnYPnkTDRfKlt4qoC9ucszt3ulz2X_WWRTH-g4qVlg9KMTyplj1CEEHlz3lvj-pGM2k6BQJ_C3dbXQYh_PR7bwJXdVunGp1slnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله عجیب مجری پرسپولیس صداوسیما به سروش رفیعی: پرسپولیس باید یقه بازیکنی را بگیرد که حال نداشت بازی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/90298" target="_blank">📅 20:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90297">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac28b3311.mp4?token=tLIN2-KIzc7z12ZQb0uoxK9aGOuApf9JRddMMx_edPO1CBwnRx18lCbMaeswiOeRkcCppGjD7aWlEWDq_fgWXQtp2C8kLfrr2U_spJTtBLZEDls6bzJ9coQrcBBuYPeIQbbFzY5paKUaMkG8rJheZE9ntxyCeI3QZC4wMtYnmp8VsEMp_AGheKWKcdpYgVacvMnwDZW1gATl4GfeMOp582tdNr7r4-PNpA4vtOfKbqZSllCrPtoIHTZXgqN3qoDJzpAvHgBrDrpR2s6JAfENqbBR9wVMlR2CgnEqAluIj9Ganqj8D0WzRZtgDlau8Ou96gdeLYQF4Ovu0HZv2ZB3aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استقبال شیک نمایندگان آمریکا از تیم‌ملی عربستان در بدو ورود به این کشور برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90297" target="_blank">📅 19:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90296">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4496fe5fe.mp4?token=OCoLVxE1kFCLVhEDIonDcm5Wyurqc82uMLd1l-WGuBbcWWNVUt-zZGpSCAOJKd6MWbKHPbpvtMX2YlRZiuJ0_8USV1qxsKv9tXo1e3luXRweHOuCo9_p92nPwOodQYX5zVxA2nHk55ZhE1Rz0hGjK-Fp5mJQErGsYX42QCOUXtq17yHRxGbz6O3EpSlKpAdOfkqd-QC9BshK0O2sbm0b8Bll76w-i0DltK92n_qOtN0X89JmdrT3mGww26Yvzvte507u5mPyK6AI-RlE8OuZRW2jmSWBigDAkIZfjk9HKcfP0FtSH_8MY6YuWMdfmyE92NHpHbdhStxeimpTVCdMzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور نیمار در اردوی‌تیم‌ملی برزیل با بالگرد شخصی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/90296" target="_blank">📅 19:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90295">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFKqbup26FCEMHhtNHLFItxy8ExxXhmfrMcln3jTN4_4RS1Q7nDH3C2EWQNpqHgA9mYLe22lN09uf89PPIyGOouBvHYYB2fzSdqcQkzR1aY3o2baErX0t64NYBgWXHvfM6bX8ks7C5g38Zv-umLB1uSEzQcxHp2raifuG2nuPQPfkoDmDflk1IV2pB9he92PYdUwubtjAwcGsLmXnBJDT_wjq37V5-OoYD2eXsoksb0l1tKQZBFflbqttJrB1nemOfDaMLQLybXzBclPQUY0WRryoFMI1ru6hKv6EYtFLdALTsvRkVFNN6TgH0lu2Ms8lpsOdg8lH0cIIjQRpScOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جیکوبز خبرنگار مطرح اروپایی: چلسی برای فروش انزو فرناندز درخواست ۱۲۰ میلیون یورو از رئال‌مادرید که جدی‌ترین مشتری وی است، داشته!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/90295" target="_blank">📅 19:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90294">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c0fba26b8.mp4?token=vrb9jf-euJTJmMdkV-W2Icv_G5X274ea1ttQZIQVvcHVFldY9-IT3JGOHoWsHnr1T0EfL3kkTfFjBr5aCa6y631GFDHRyc2pbR5IAhloHlQ8vzb_KSQSOiPUydEFCnlV_gTnXKspEBbScjFiqKlVXtom7EahVwOA69b1NifNEP9sm3_mchE2KuSVmMK-UJQopZegTnvZOs3_YnVqlkWOKcJtqIEaylPwFpzEtqPR0H83C7e1koUAWxj4ZoUczP-zO8PCuXv15VNbHrYWk0R-WFS2fha4yFMwDCvC4UGe0k4niVMz1OhA1jHm1lX74mM_-deA7uS0TgMSSzDxULBrs1gZtWtZ8nDHuuYwIHWjXkXeEKcCIhpf6x7JPZaoy4C9JGM4uoRUVeZoMM_WG0z1L7vUxGa4gU1Fu1FM-QLLxzEonI76swZv2KLtf13TeWXc1Hq2oufS2Ls7hBCs2_XsA69KCBE02FSjJI4xjn3U3EZAtLP3Y8cerAyLKEeiK4PsNg_Fgdv-PPLIkmyO_3W_ltlohb91PCpalX7R8BBIT5WMkEmMb2iztj22sykcLUPdDMYJzlwRej0ESHmvAFr6_iNzS8JBZEvqOgYRq9BomicIA4JwRJQsJZN4R7fMBcswWaVYRUyH8NaWxtQ415UEdDHwDus5CuW3nQoW56vewYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ماجرای بازداشت نیکبخت در پارتی شبانه؛ این همه آدم معروف آن‌شب آن‌جا بودند چرا فقط چسبیدید به علی نیکبخت؟ گفتم نفرینت می‌کنم یک روز جای من زندگی کنی ببینی جنبه‌اش را داری!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/Futball180TV/90294" target="_blank">📅 18:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90293">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvgOTvvQ9xpGz60O5qNam82e68sujU4h377XekGO4iPlKPK1vfkZmiQMECJcSCM9ZWU53Ca1JeewAYiVuIsIYwRsS_rEimyUjCyX6inDWPN9pe8MAxZe5JDpCM4qbZKAYPlDFdWwLRlRhzkNRIrrED6S5YNkqyfFM5T8ziG6zWS-WA8S7BY9Pgyfjg84OilKDuAgfNv8royGUPF2k5NSj6SjtU0K15onNZiH11bgteuvNe7wwiC60VETnuQHyGDkCa5ATQWd8icGHbslhNpou1zNgtSIvnOAzsXAXSH-XXeW6_zBRelIomHvmUJw3pDmcztx0w8pRMBuYOtQY01gYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین هتریک‌های تاریخ ستارگان فوتبال
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/Futball180TV/90293" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90292">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:…</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/Futball180TV/90292" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90291">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBMN4k15SFfLweXvwG9RYaJpfHf3kmxyFLWt5cA6LlerM9ySF4SbfXHTN_78R6QiTAtWgw19zk-Uxc4m07J6XQU4OhZevCT_rmLX6567bjDw7Pl28zuAughMhDfUyvPl_1YMEg9E8fK9eVcXrxvdBaSTv43F0ppGo4FlB6XYxDI1G9Ve7TqMovzN8NfnLg4KrCWulUMbdISn5PoYKzlLrSt6WYXd1dabOmB5eKaDboG2w-73cC-HCwWsxQ-MNCOsuHZbQnGgEhWu8vz9RwW84N3pyB9gF6sWS-gdbtNpqsNuzy5j2Lijl5nIgf_CckMAYkvPKQE1Fu-UEBd7zyu39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تا حالا بدون واریزی روی فوتبال ها شرط بستی؟!
🎉
500 هزارتومن بونوس رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
شارژ سریع و امن با درگاه ریالی ، تتر یا ترون فقط با یک کلیک!
⌛
پشتیبانی 24 ساعته
💖
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
g6
📱
@winro_io</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/Futball180TV/90291" target="_blank">📅 18:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90290">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs5XFl-scToXIR1p0vwnjz4hBffCfxhyPF4hh541h3-uy2xCrENigDuwhnSBlhmiuZn3PKhSXS5LoBCfSmuM3pbVM2pESSqh13vpsPygXdGPEPh63r3l_vjfhJqrqciY5PshiC--pJAH_j-c9anF-9fGrHt0vm6M_1FWa5nJ6qN-V0kEg-_9Rzw2e_M3pJP5Hm5bGc2qw_PbSpYVNvlrAq-PyxMOr-sBEgFGmM5QDhifq2RDziKT87vLTHbjgAoB7XCBMmzfi8-4AKPB0T6V3fUUi3sN5l1Wx8NrdL0bGjLjRHhfn1OgX4Z8jpQC-1zBjRD_RZiq5rgCFpKlqZNvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی قهرمانان جام‌جهانی در یک نگاه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/Futball180TV/90290" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90289">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Coe5SXlJ3GBuYSYiHIlHmtS8FHeabG6JQn42kdqxBVHz8db5JstUmCVxF2CAaebbVki7w78-vEzKTLKRoBpW5X7DCBVjlcfovcOxVmP4IFBaYRfZx1TMbc25f9qViV6qElYvtE7uGqBjgddUXOtvr541DR7C-i6G7I6JtotoIRIqM87NSj337LwApTNX5uNiJLbyBlpKljAZ71y098lUWFkYpYgoV4oE5H4Jf6yGB0KT-hJsoRH0ubSsIb5V4y-sFEpGt8rwnGMLKYzYPpVdMK40yOSk2Bxpp_5chfNt51BOac0NZ3eV18bI7R-vfqz9VqKIWbhchK3jw2YvHqksIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گفته اکثر منابع خبری، قرارداد آنتونی گوردون با بارسلونا تا ساعاتی دیگر نهایی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/Futball180TV/90289" target="_blank">📅 17:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90288">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXzQW_o8F2W6gqwPid1kVl_qJF6SlrfJ6gmfjJRiR-ULDRwFvMS70YbwgPF4T5FhlTSY0YlrbTf3w6MFE15KkV5Z8e-l6xnBg5HZeu3-doF1Ir0KhXHf_nPiO20gw_D3hWuEYlBEgAsRWxgVWqGDD_nxgALi4zMetfDSwacnFppD7FvIq1cHs4keIwBnDhMZuqqM0Xsi5VbsUnFE3sUHOnZU3wuXnm_q6tsML3U08gQoSSXzv3TyqezOzTxSdZcQ6FJlyqHOMgeoOCQvDNLGPKqjedD3KRO1l3bxnvd0RqxtsC3g7ZcgZBLpWLuWtXg-qRt7Pw81G-ERHVCam1FjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه میزان بازدید پست معروف جام‌جهانی با پست اخیر نیمار در صفحه شخصی‌اش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/Futball180TV/90288" target="_blank">📅 17:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90287">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hu729zj7E4x21Qjz9ZkvIK4XzNuvtPRNt6toX1q4hT4v3nJXQ8BmYt_JIw7cEeAC7wOqTuOMNEFjVPM7rPqHWfmjUP9dKqASVvQc5S9iJqAIkyOgvT9Wu0pelPdEpKrSiC_mxQNTOMFjlm-kOMT3vo-FdxwuIpsFcdtz3GIwsw9YVfKRNVpehKcdXm6DH5JvFzgmTft5YrJJJ2PyINjTY7SjZejKacRWaqkOmUDUKJGpc6BSkpGrn1CEHow27KNv7KxfAeIJ6CpScf9OBPym6eiM8dI0Qbd2ZouF6mYgn4xsF9m7P0YySXh8iUJVU51uwz3f8jBq1gqydx_m8YaXZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جرارد رومرو: بارسلونا قصد داره قبل از جام‌جهانی قرارداد گوردون رو نهایی کنه و سپس به آرامی در طول تابستان مذاکرات با آلوارز و اتلتیکومادرید رو جلو ببره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/Futball180TV/90287" target="_blank">📅 16:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90286">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=sQmW_I_RMzPoLCGX04LpAYWfHi0RPlBCKBOSURqQfCZw7XhhlOPht1aScJLJrhZaRy4RYjSmt2zctV85H-G8opQYxf0oj-2xrRfy-MFP8ZDH1ncfKIfdidvMhYWj8LvHCOoK9YP5p94YUJScJ--tiS7nX3XxpZpq2W0kpKQa2GcXOBXeptuAeJgdF23hf0gWatQWxa13Edmtc0rjaY7ln0i74OEen4HHlL1rXVqwetStBGIAwecoHe_HkT67EZ7cB-E9VrOr5z8FV1kbEVB_QegSwL3XM-vh7bK4Fu1MEQgU82Qrblid8YYNOSRsGBr0m-HIFvBxYt3S3AEmXjs8wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/90286" target="_blank">📅 16:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90285">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c42b3ba26.mp4?token=HsprUocrlvDe_Ki-suB-S_FbrGMwMGNk5rPP7LPI7wdcy2ElXMBGvPLoSnyCaSNRaBjQqC9jaOxuIuh5WpHTjTCNQKH7YOfFOmAT7tAMpVxz4WpzIxCaArsCNx5ZOi8UOnE2kYf7RIi83vzDby6PAUPybazLgvq8VsHijxMbwUGBdv7p5XPkmBCgN0AwlcNllW3ED3q2MdmAQiM4AIwjVujxM5KuyIjT0KzEBOrgg_SDz-568IXXx0Yr7UPO5KzrTTZw9-I0LJdbnPxc1NqLYrZ6PoUL54r82vjX_6zYZcTS9EUA1MRB_2zYCwVG3TQGQoDNzlNEIO_HM4NYw-uQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتتا و همسرش در جشن قهرمانی آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/90285" target="_blank">📅 16:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90284">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZZUBhClMlC2Pffqsey1BSCVonztJMGScNWDPvcguZDmO3pvHDOw5E9soAcI32tJP3RR4bTzFEvMdgrjFxnkNn3lcaJssnQ6SvrC1KBGb61oVanHiC4lIsdHhCO_U2qANWhoNI0-PyY_ZtTygkGSfT6PdIzqC1MIk5qShRDIMnkhgRMlCjoom2b2OHjjtB-GMYCSEv3z0j3QMzCg-wpx30-hLAFBTfflVz2foOQ0IOvqTpEiyhaoqHEUE-y0UxNAsvY4TlX8WTjV7SqDxfibiHi2035iYLDJEXF1Th8-MfaQoz2eVVivZ1joRfMdcXt5jcrrcoMIjQ_8CWeHHVmtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست تیم‌ملی هلند برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/Futball180TV/90284" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90283">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDAmxhI6I1VGqJBIMfP2JcSIIdO6Gr3YlkPzT4rxvVWBIEtVi5RZ8vbIiRhp-oxvlYUr335S1BXzSGkxCEDmxc6xSH_HdUbN0vpAJq7i7ziH-pPu0Sm2DENh_ohbc-T4SrfgJY_hHH9N6Z160ugx80MC2GCS5wYReB4ScNBDhv_s1QfWoaWJRv7_Hib-67MqWF0TL1rlyIomAAmkBuYKjb0nxwVWbuxYou7Y_WcMXQpd3xTGj-QvbTvl92gMTsCXDM3Mw75c5IIaoIyVyfGUo1_w2XoCPBpm78bippvdQHGAaj_pW0GYs5023RdnJUzMDqowLwX7Wq_eCbvGi9yFfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنج سال گذشته: کریستیانو رونالدو ۵ عنوان کسب کرده است، در حالی که لیونل مسی به طور چشمگیری ۱۳ عنوان به دست آورده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/Futball180TV/90283" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90282">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZMVn6YWe3uDlsjKCPt1H469iSvqVsvHgWpYJS1rOt6-CtEvRWTftUVEYWvq49dbNtsnAu5sdwBpwyJyR8MhnE37pMmSCC6xaCPmHrJxX_2q3RViBaK4RBIks05r0N7HNpZ-j2DxTVydxdIL-VaK_5LkezCxv0LqMT0epYsAVvPBwHA08QJRFEq_0hs0pUXodNHyhAJSE2VVHyB3dvZJP9V9O2w3gnrlml4maY_ZP0vUxmF00umGQq2w1SVgOASR3CE4yDCv2_V9odvzDUtYinjDuQlD5DeWVA3GULK1EAEXhoignczJGvxUvbqXcUufZwMQk0xaMf6hzGF9il2GRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">180TV
🤩
🌐
دوست‌دختر جدید دوگلاس لوییس در عرض چند روز به ستاره اینستاگرام فوتبالی تبدیل شد.
👙
طرفداران نه تنها درباره رابطه عاشقانه این فوتبالیست‌، بلکه درباره عکس‌های نیمه‌برهنه این مدل ۱۹ ساله با مایو بحث می‌کنند.
1️⃣
جذاب‌ترین عکس‌های دوست‌دختر جدید این فوتبالیست در کانال ما قراردارد</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/90282" target="_blank">📅 15:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90281">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">آخرین وضعیت بازسازی ورزشگاه آزادی؛ 3.2 هزار میلیارد تومان دیگر بودجه نیاز است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/Futball180TV/90281" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90280">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbe3da6710.mp4?token=PyY4CFc5hOP5Jm2klbwah4LaQnsctRsXZNi5qAvB-QyjgFhcPx1FUFJWUWwq-FZ47CYViU_1U3vz9PxZqxR3JGsSdcjcTOM8u-FsyP20slkobce4b6R3RGuzJHP1ysSQjXPTW1PWnG1qJBCvOzqLbZ6jlUsB5QdW4zbZYDiX5xesbJwO3madtPj7AgN5wVPLWWYoN98flyTwX6OW5ejd9T5rYwOp4tpV4htgunCggjZ7OWEYN0DMNbTSvuGzp3-BG7QTMtce_EyFC8Gpuz1-5v1alHctItZSu1TL5yd3msOSiuoACumqk0HNvf1HuE5XinYyzsLd7JdJv8i17MKiAKZdghAV6N3RDlPEzggS7Iiw3H844wWcPuEnBKgIStn27tmDtFuSfGfa8ZIkYTNPrT2YIy1Qo8yPFnRnorc8xx-ruM-tooW-WGLZeV29ox8b4ybZT9dowdMTfRJRNOLjPNzV_gTZZk_ImfU-FvHq7QPOw1G0bRBN3L68h-T_shCnisYltGZRPfCZZObgmRA5YBsTQeiONmBSvxT29ii4Rws0q4v_DT2Rd66X4YCRdyRrwsxa4TElG-9sfeDt9l0VfDG4O6qMvjyZPvBiTN9HgCXWe6KSijWu9W_-6eOB8Qhzq43zoM2-h48jNtrOnjve9NHomwD1u3jn3SBLEFM4tI0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رمزگشایی سامان آقازمانی بازیکن سابق پرسپولیس از علت اختلاف با قدیمی‌ترهای باشگاه: جوان بودم و خوب بازی می‌کردم برای همین از من خوششان نمی‌آمد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/Futball180TV/90280" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90279">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7_BJmb0ABTb-aDUQFjvvcXEoEoZzQ_28-drbG7sjEN-PJOsNKAo-CGXDpP8UOZMCmBvTkOvdK4VkBbitMCo01zLiqlPKsvkUOVx83_H9q8iNv1s_us_N_jggmg7ymlpXL6nZ69iOsHO3UqGCwPaUnPVwiY-wfIZ3nivlr1vZn0WYxW77DNkADVHUBG67upnIw1DzjXQvbG2yphqFcmtKmFoHUK5byYBRvhFEL5qt8UJx0MnvKM0K8Db4drSbRXEBOQxBMkZTg-RfY2iUOiT6IcKkgkgeyThggiixefnomOZdDHqTmzU9pDpffZmT3BLGJmjfz6-kHbpIfk56G3-Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم‌های ملی که توانسته‌اند دو بار پیاپی قهرمان رقابت‌های جام‌جهانی شوند؛ تاریخ برای آرژانتین رقم خواهد خورد؟!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/Futball180TV/90279" target="_blank">📅 15:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90278">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cbec1c58c.mp4?token=tJzVN8U2puyDIy-d8yR_vs0Yd18qpj9LkHcQY9PLodlkLzQ5ti4ea4vsV31pkqkz4_ull27V6b7Rsd0cHgqiTiEbBIjnBZgfdbeCHu01An1mzdsJTCzmoaUKfF3p0IZSpz-mQXKZzb9QNnDkIcZ4f3c2HffsH1b4RtbKdAFGsy0EEV6IdhHvMh03jjlQgblvEaF-scAIIWSsNpWVJBjDcFTWPFLrKbSIqgiJKoxL49D8HBYlKwV0fxdfJ_fBqz4D6rsaf8_PK328EwZHHwV1GaFh1WUMKbUXkbbc9JHxgr_THJ1gpda_mEYhVgyquvnp1agETH4mwAi8slblQ955Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شدید صداوسیما از دستور پزشکیان برای اتصال اینترنت بین‌الملل!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/Futball180TV/90278" target="_blank">📅 14:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90277">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/083cb252a0.mp4?token=bMm5zKvi6CUrXm_3nxNs03WGAqZVzSe3rL7Yh4a1FFn9sSpescEPmB67dKyYM3bGK4tTVwQrCZ2vO_X_6mNpLjfoowK44jOLcEPpe6CWCKXOtbjIowx045yFrs8JtufZbvB4FS1ThiqUKhjDR0O-pw_WpY1wqUc6N0yAbEpI_oihxBBh-Pnc3cZXQfwusoseBukPTNfgg1Wer0DtmYFU4bRLfT2cFch6pz4wxH0oLQLEiljf9ZP2R8uJ7H5XM99sTTDFOOz-zChCkaolO7nGqGrNWxJUvT5zeb0scNv2LF9s0ylLIFT7gWRjxUILXqTuwmLetWLKHymG4K2SPUnXig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد نوری پیشکسوت فوتبال: سردار آزمون را ببخشيد. اشتباه كرده و عذرخواهى ميكنه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/Futball180TV/90277" target="_blank">📅 14:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90276">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ThkrgbjTwkYQEtBcqiAFVgbEFaWw7cUSmcXx5mkwCApxPaYIVXSvaIxHbkc7eq8FYac-hx7ylIFIyy_HhIXg7G8zWssaj8PD0UoaUpVH8aMA5tpHCViWSaScElCiYRnNcOjExQZ8xFunVJHd94M4hpxKA5r9HpDb3iCuR6LJxgBirHiOYZqRCX0-RLvqHbv72nQipQT4i1qcvFQ_wXOr9Fu-Z0rbDL5KLTeGfczElyZ2BXhNEh_RTgWcLi299ysYengs5gNZeWQc1sW3kT6UO23yXbumiim8r6cBdBj0H2yiN92I0N8d0Bi7DMXzvGSqFAvJjDE1XjEp7kBn6Ex94w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین باری که باشگاه بارسلونا ۸ بازیکن در تیم‌ملی اسپانیا داشت، این کشور قهرمان جام‌جهانی شد و حالا پس از گذشت ۱۶ سال بار دیگر ممکن است تاریخ تکرار شود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/90276" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90275">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=QY_2vAYOKxGmLv-qZPRSgj_nPsoNCc-SG5FNlOvwTN1FxNvs-Y2P31NUEyBx59VTUU5oCzw0r87BraHD_YJp4xs-HbzRFmVqilCEBysLZgL1gx6UDaksQTRVa6Rt67jq9fTqIDhSZl_kOhE0_JMsrQKuMgdaP_3wmwraEvZrDUsPrLiWLOLV80PZuxGHHoim7jP3szUO7B0HhreU5x54YpDPzHPQg2M_PnHCDtbtcw5W0FPbZ_JB-IcKYnAHq-mSNZDvcITZqhPP_-QQ21NFFpWl3exVGZEZ4R5cpg7AnMEJcN7OdzdqS0j9jDY8Wv3ZvbknCJ9UgHtbCzLkOtLinQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از عجایب فوتبال بانوان در آمریکا؛ بازیکنی باردار درحال انجام بازی🫪
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/Futball180TV/90275" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90274">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMolkyy4GZIjfMPJIci9P6Q9LZ1tJiiLuknNWO4jIjL-GbXhe9OjvSD-jc9gXbE3wBWJJP-_MJJa_0FafozdAloCl79QQtpnKtRbA5VwQWPDaeeeYNV90jPQxohp-fWSFwKpC9qWliCwDWD8Fay6BEojOzNvoDCJOWDhNq4Wgf_F6lpwJqVta3P6q8bJEV7rtaVeV2GCvQx0OdWwnxLuBypzR0m2aqI_FyEofsgtSkuo-xBY0ga5oIN723ExHt6QkaMsTnbjGR404PovKm5ZCVFUOOr4ghVSMopETtc5-yrbxCdd2OLlx6iVGy8AWwhGpfmsNqWrMxlkgAi9o7e1fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
متئو مورتو:
مذاکرات بین بارسلونا و نیوکاسل برای جذب آنتونی گوردون در حال انجام است. با وجود علاقه باشگاه‌های لیگ برتری و بایرن مونیخ، گوردون اولویت خود را به بارسا داده است. نیوکاسل برای جدایی او آماده است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/Futball180TV/90274" target="_blank">📅 13:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90273">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rL2VHTcMfywk8L202XFA9ptpGQ9uPVhylLDsXgukp4HDV01_f6QztiR07l22KvWt6JoFrrGFHcFUVOtKB71NUw-shm0dEWVVzcKsc1rQRJjw4xsFwbe-lRghyJm1oI7x7g6FwZEPUv92eRCZw_LrHAGJycQtavPvS9hp8gB_Hnqjuwp1q-SJfEsNMYZZaT_4-JWy1_d36Ye4Xt1tafuXZzT2CPb258Pl-Moz95QGX-CK4csgOi_RhbTNIPsALyWWlznyYFkueUzfgX-nStWimnmeiKybWApClUcTlb2y4QfD36RZ58Dx83KEAzLo31ew4p8Qpt-RB2SzW00QNVUwIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین گلزنان فصول اخیر لیگ‌قهرمانان اروپا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/Futball180TV/90273" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90272">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا #وینرو  بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/Futball180TV/90272" target="_blank">📅 12:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90269">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZt9fe6UkoXe0Kamvw7y8LJCXY4jwHTYZXiuJ_2yZP5I3IczxHObl-QKQS7OzlDnc-EgT2jVVZKjwkuOzFzvRzL1byAyNd76UV9BYJQJb0rAa4Uc5Y8rCqQYHlDwYbXoAQCMsCvMg2JXanfeCrDfpbmL7AZPXZ8lW35t_W5nt5hoyWsRBKcFvCuZGe-KArGBd9MZZoJRfSoUNNVgJ6-btYdDKVVSyKQr9wDD2GnDJRzF5o8URgpRKKu0qCUD4HShxtlSvkjlqh2rAUGT91R6GdGKJLeMnkJfWosHYm1eZzee2GYxwy-qeivX8uPeoKTEJWX50JOxl-69mX2E2WXOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
تنها جایی که در لحظه عضویت بهت 500 هزارتومان موجودی میده اینجاس
❌
🎉
کافیه فقط عضو بشی تا
#وینرو
بهت
🤩
🤩
🤩
هزارتومان جایزه بده ، نیازی هم به واریز نیست.
⌛
پشتیبانی 24 ساعته
🍆
تنها سایت مورد اعتماد ما با بونوس های کاملا واقعی و رویایی:
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r6
📱
@winro_io</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/90269" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90268">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cf55f690d.mp4?token=mrWYiTgoDaY72J9di8zZkvULMffgWX3EPKobFxXZJ9SI0m4E3cKuxk42Kf838dPLVbEM9oM0F8VMudqgHrjumHIsXrA5-G2FRF9PPIsNt6JNMfXeGePPhL8_JmokmSRPcOc-oWzKPEQWHZhHdN-q-MTMKh1eF8HnKibLUPOXrnrFslEpk4v08XgE6lP1inIAo0akKUq0cKXYzcFybnTu56hXuBsykd9WfWMea6zA9eaPNdKS8x6GNP4Ns9nyKtVX0_Bnwvjm7_d1gd5d9BRJG5JLnK0IUaatN92pgBtw9ukwoTkMtaC_y7xwCpaB8VmfzyBRzdMwqP49YK8KD0Yl3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات تند نیکبخت واحدی: افشین قطبی کاره‌ای نبود. چرا در تیم ملی نتیجه نگرفت؟ قطبی ذات قشنگی نداشت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/Futball180TV/90268" target="_blank">📅 12:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90267">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98d2b87299.mp4?token=S8QvqawS2cO6n-_SDB_yzUmn6AEPON28vKCocAlz79L1O6J-28D4wT4lpzhRzirAMd5u-BuoAJQqL8luwXfpLohKhZpVceQcr-C8oVyjb3Jac4Evwz0daYsfnJhor3okzB4r9f06cCiYkbrwEKsD_Wd1xjfPd0XrLD-lsIsl9qey_LmRa4Q32pyCnJ-wRPoVImnLK2-Yo85fJlV5ZI_YEV8FiDIaYO1dYUtWSZniz2HnR8Tz9xoAwdH_JCXvp4Nz5X0hcT9ql7xEAHPQYDWtdShvpijaKwVFdqaA1xlFYws-40sTbk0x5WTdfCUPiIwLWccdLQ9L0nOhBacsytswAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اسپویلِ بازی آرسنال و پی اس جی.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/90267" target="_blank">📅 12:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90266">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99be172cd9.mp4?token=sm1bEC9RENAiixs2J0u_9GtXdOcgb6-QbG276IijDwFFlzzcOStJwDOke-SEDW-_IRDsI1elhXDUk498C8VR65GNVzLkVtcEiGa3UtD6NqP_fwSZF8vkT8F5iVHsQ_7AVIg6dcvpFUJLOsrHEIi49AKLElctYFi5_0zWzF5LV2DPKlhx4Xr87HjpToWhTI1jiPo5f3_lFnLvKyhtnajEzpIXCg_JeAiUPrQWksfh5SkaSGtWj9s_-6CVDBv7WUY_eNboCZ84GXOyccw6fDm01t6Pnlno9qxncXQfel9P5dAwqQS3Yj97czsi8YAWu41YyIBRpAPkXY7btm-90-Ql6gUKBYPzHV_Y1fwFhy9ktEXQukn5Yr7q04xwYOC9pMS83jvg32rTy6NoEuhTJ05QLRWfdu_r4y569RJ6CGIwQOupslSXD284n-PnvzLTfXILvXiY5i7xDIgehL5FS-2sFmCmM55cJNFDvWHKVmnWKC5KcA4uChuPErv1qT_VZlv33CmtjIEC5R0_qBe9Yta7mBgegrSnynbcfSJSVWbkVOjdBBfMxG20DYwuqv1spEQXRIQ3NZwWWhx4AWM3wE-tIXwCkmVZKpBC_TMmHcqPzikbSXKD1HC1FuhVWWfMISUxbxP9eQLrLM7M06GZo4AlWohrwUXH1mU5rARcHZ3pLNU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاسخ شفاف سهراب بختیاری‌زاده سرمربی استقلال به پرسپولیسی‌ها: فاسد نیستم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/Futball180TV/90266" target="_blank">📅 11:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90265">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VNDnq0wzrNdDzTYnBlLOoMvXLbMGTsUhKckiepBlnS5Ja_tiV22vy-xtKvxN_kd3MGwu2hgSgdmCCaA4jddlmWSdQw2Kj6IuFnPwwYU8m3drYZMRiyXDdSb2cC5ntsrIhMZ4TjqXpSpsXMBiLjxBKU-qZE-Q8mXpvsy1g3jL8yv0vOHCg2WL_8DiX9QFn1KWIus1230qFc8scyJ1d3UtP-7Nnp2y9dyRY0cB7lnSMx653yu7TdrrPLZ3af6H8RlZQ7FLSMSh64IIQ29GHvydhF-dFM5WwP9SIGhwQKJCZNkd1GB18UetuColLSw51QXX_mq1QHSWPrSUX5xaQpkAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به گزارش رومانو، باشگاه بارسلونا بدنبال عقد قرارداد با آنتونی گوردون ستاره نیوکاسل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/Futball180TV/90265" target="_blank">📅 11:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90264">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/426e74bc07.mp4?token=ot9F94mn8WicqtB02S7skhFNy_1cpUJnroCxlM6iW7gwPkklPS6GpjxAcF9jTfOMHkHZxQfB7MMCPu7bS2HN4yMNtOe55djHS3oDWhtaAuqrJ1241vxiMzNC5B93qw6hH-guhubXMI8I9Ak5NAUao0bVPohJ9vZr9oNgfM6_56BbH6nKCQ73r1BkgATK3uV_g2rJrn4hrxF8yZqer6NRIG836ITPqMed5rBdC6AbUUjvpabEpJUYMQerjNOkNX4tOtq0C99XkzFbyDhFih-jgtgB9dUmu6qqTSP4hJDVdLRzFVtkroDiMm6XQJP6hkTv4x5tWBGsrVcpNU3l_djtMCKfiM6Mj_s2MuLSH3mNebvIFtOI9Pm4gQiQE8SS6-rTtYTLUsfppu1Jg7dFnrFW-bQblD1jHQ9WbReeNSu94rH5XWdZPGvPPdGXJyQNxC8bkhNvImMKQw4RvT6DKoR9Y9ho0vXqdQOX4pohFGCWNA4R40IxKJ89OHYCHIgNoqjUS-Hox6JB9xfBSWYQtRkmOblk06oQvYGlhd14gL5Swat7_3bq6gPyGgO14G0G__WHyglr2CpCballuGABXpy3SH4tD7QEjKrW_ZIB7UKi4oqGgxNRWxLu0FkePS4HJYxj7Nlou2UqdrAV0E4Q1N9-VGqRibjrlYAT82inT-IuEwU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از اظهارات عجیب شیدا یوسفی بازیگر گمنام سینمای خانگی: در کارخانه پدرم، روی شمش‌های طلا راه می‌رفتم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/Futball180TV/90264" target="_blank">📅 11:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90263">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=f4ZHVnhw5oiJs1xJjMWWdgYxfZ1_kKgzaHnOE0dHQ9Rr3X9Sntw5MHTLdrRnPt7EdPazZ3Nz-GP8RezGkQ0_RM_k8W7634CkJSIrg1zZ2hN4kMN4HWRIQyo9sW3AiemGVnexeW9yOjsTDx7HVZr1R4P0S8pyOuAmEEtFaC3t1NLUhERU5Iz1kdvvVzaj1PyxT9mzpHhbfocVz-dHFF36niNK3zyYTB4Vg67bOriD6AnWFk1ndHA383k3i-YKwEs8XARwvda_Wx-DnIg-9TzMmbUHcDA0K9r2375273XxiLofHbcmbYNiaHMEdxvuuKQo21LCxhrF4aHRMlqB8DhaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b5959b18a.mp4?token=f4ZHVnhw5oiJs1xJjMWWdgYxfZ1_kKgzaHnOE0dHQ9Rr3X9Sntw5MHTLdrRnPt7EdPazZ3Nz-GP8RezGkQ0_RM_k8W7634CkJSIrg1zZ2hN4kMN4HWRIQyo9sW3AiemGVnexeW9yOjsTDx7HVZr1R4P0S8pyOuAmEEtFaC3t1NLUhERU5Iz1kdvvVzaj1PyxT9mzpHhbfocVz-dHFF36niNK3zyYTB4Vg67bOriD6AnWFk1ndHA383k3i-YKwEs8XARwvda_Wx-DnIg-9TzMmbUHcDA0K9r2375273XxiLofHbcmbYNiaHMEdxvuuKQo21LCxhrF4aHRMlqB8DhaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی صحبت از مهارت و دقت میشه
🔥
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/Futball180TV/90263" target="_blank">📅 10:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90262">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWhhTmfl5omiq0MChMEiRKuSHvzGI9LLv7cRCbWNaYKmfnViRg3GoOYyhRJ4tx0Pnm5xfU_Psxfmq5Y41nBQoAWu4avgMYhew5x3HWZUhtcmWofkQ2flRnU-2StjoDQvAKmXcx_oT69Yv0N2cKlur6NVh4L8Rb5cdw0PU5mvIemxw058xmSbhzqQ8Au-uCr_ib9MM_VtbMA-mBt4cIte_iYC2ejpj3BqPFztKp9mBYt2TGM2mEmcbR_qRsQ6fU0Bobn0xP4eVl7TDQQzjELWhscJuI7pi_rbjRiIqrmsMIZin1aYFXjKqnDFhujgH5868TkoRWjjVcLNF9oRtrtCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ترکیب اصلی رئال‌مادرید در فصل گذشته هیچ بازیکنی از اسپانیا فیکس نبود و بنظر عدم حضور بازیکنی از این تیم در تیم‌ملی اسپانیا برخلاف بارسلونا طبیعی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/90262" target="_blank">📅 10:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90261">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d64b58d74.mp4?token=eKcavSO-R9I4VQjH7Gks-yOmiNR1EvkfYp6KqWHHO5V4beVHxtyml5OsDgPhbelLhms7ySWQK0anBuieQiGV_USZ7taD-1-vJ96kfT7m6dgdcfLUL_euSsU0VfMynCNKHUDKjsHa9yJMPzJ8lMTp1lqc09CuMAaMUPdEXU2JHdMpSMRGOnyhbemMwKOJZyv7ER-KojkO32QruXHUlLE9ittdjtBk703UvVKloNXzxTfh8c2kUM_Prc365-U2Y29TnVC96sTV69WbVjLLmzdpRhX1EU3mllOeo1Afj5mzXuFPqhC9X8KRMm0yyIjq58wkxcBlbZUydaKYNxNzsndBSIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل‌های فعلی در سال ۲۰۲۶ فوتبال
🔥
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/Futball180TV/90261" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90260">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26b4bc8543.mp4?token=nMc_Gikoq9ouO3MdhYKTjxHEbD8q5smHrHTSsfw7SLUQ20TZa7DWTPFdG3Tk95P2m10zKwdu43LnOcNHr-r14YzDjuEDfFxTe5L3rBzc4Od9R9cp3NjCHCxCsHX2MdggtH6AojdfmkRtFiSs87c3t5PI-q2DRGJvTZQOHjxDWe1Fwp7eNUQvUveVMGTHokScevakAAzD2bXH_k66jdv1NnwSFaT91wPT1TloAHAT4DrHHOstF1TvAo2SwTES92HKC90vzSeyeXIVEbo-UfhLTebvZSWvwyS_Z_91Hflc2WjW573b8fDTO8AQiMGqwDwqse9-NVIcuUWq6Vl2izx4Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ برا خودش عالمی داره
😂
😂
😐
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/Futball180TV/90260" target="_blank">📅 09:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90259">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=gMtvYpWe9e3QL-V3ueMwbYkDNGBdpy_g-vrB6yMll7KPqLT6qCJSMREcXHJP1cjSk06RJ7B6zGi55V7I-S0y6pG663lcZEi64OPRl3tWUYZ54fdpybVBQDJGKh-nyuS84twf8jdDFT_X7xQtme_aOxEqtNuKCE_8XdHR7bX0dl3xrDx8DAL6w9PIULy100h4qTt2dP1nt56OZsDgdgHhIMXvefyABf9ztP_GnEhnMGvoHPPIxnMW8zzqZ6EsT71dOKo6SRCPFkRd79L4kRFmhcDTjP3nQRfQBaer4lbp9jIciZYv7WSD-jViqZG83Ab8_MqprDgd5_TXkNVw4I8u2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4b0e0df75.mp4?token=gMtvYpWe9e3QL-V3ueMwbYkDNGBdpy_g-vrB6yMll7KPqLT6qCJSMREcXHJP1cjSk06RJ7B6zGi55V7I-S0y6pG663lcZEi64OPRl3tWUYZ54fdpybVBQDJGKh-nyuS84twf8jdDFT_X7xQtme_aOxEqtNuKCE_8XdHR7bX0dl3xrDx8DAL6w9PIULy100h4qTt2dP1nt56OZsDgdgHhIMXvefyABf9ztP_GnEhnMGvoHPPIxnMW8zzqZ6EsT71dOKo6SRCPFkRd79L4kRFmhcDTjP3nQRfQBaer4lbp9jIciZYv7WSD-jViqZG83Ab8_MqprDgd5_TXkNVw4I8u2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
همسر ناصر حجازی: به او یک میلیون تومان پیشنهاد دادند تا گل بخورد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/90259" target="_blank">📅 08:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90258">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">روایت قرارداد نجومی فرزاد آشوبی با راه‌آهن در ایام مالکیت بابک زنجانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/Futball180TV/90258" target="_blank">📅 08:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90257">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">Soren-VPN.apk</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/90257" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90256">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Soren-VPN.apk</div>
  <div class="tg-doc-extra">62.2 MB</div>
</div>
<a href="https://t.me/Futball180TV/90256" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔵
فیلترشکن سورن (اندروید)
• نسخه 2.1
برای اینترنت ملی و بین‌الملل، عملکرد خوبی داره.
وصل نشد، مجدداً برای اتصال تلاش کنید.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/90256" target="_blank">📅 01:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90255">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/otW_lbD7_zKRILGsNTJiDsO4xPkC9nMAGHL5kZTz8PX_j1potRSAp9r8zD950KViOYF0OCD_HXxYeLQX8gzuGEkDQbPCuSXeQwYBqYTOpcgaubvQKuBow37BGpsXlS5PVM7bRkwaZ5PSqkcQQBP2fInHgQ2opNf-YXTSvt47LjBIP5nHpDc14PNxa7cJyDDZnh09NqxB2-DSNYeGwu38JMz_jqkaIhrZGchK1Clc1KLQt22eMRLd1yBAWTE6IjBtuxkS0E_jerEqJGmgsJMzqRRR4XrdVT2j2os5cjECvBMasEcQXncUWY9f69PL8MIZTF_hdmPflCJwAchJ3VDAZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکل آرتتا بهترین سرمربی فصل لیگ‌برتر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/90255" target="_blank">📅 00:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90254">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔥
برترین گل‌های این فصل سوبوسلای در لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/90254" target="_blank">📅 00:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90253">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EsjaYvtQcrNXuEXtUjP3r392s-b1I0c8pNv70lLZOQORh6soYezQXLs3GDtSRyW2amFxf7PkN6yOxlm0j8MnyaXa0-wlJNh0CxBdPuE332I9qVXKWYXxackOUfeiQmU9UwwFxDOm7MXH7j1Amm0VJoifIhZPjIfZEFMZ2zwLA816q_-Pio1VTq6wil3lgaSMVP8IIqmrY28d2iYLkxbijfRYm2N1v1-2xrCp--jbsvokOZhCNkmg9CIEqJVIDxVH37KNEKLTIOPoXwqookXPMZ26DmIS1lcIIgjtDy0zzFXPGMKb_7gi8xuDUq6zjVCGhepev0eBThFr72EmikXixQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الکسیا پوتیاس بعد از ۱۴ سال از بارسا جدا شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/90253" target="_blank">📅 21:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90252">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=scyQEwH5IMRA5eKABOyDUZUyG9_qv9xKYAgywVbuh_OejTGbn8sUD0Y9IOafsCsVPATc9YsIg8yZ3TbM3QiLnukYHACsaHDIjjwEFHc9nid0IILvza4VUk1RrZi3sdQjwTdgBhumcVPhSY80CU96oHn76vGoE2hUI8axz5-TK5WdYsWNwSh8bam9jW5XWrcl7qwzt8DnmfzEmKhrxAR4AX77cZfEFCwN-70JGa-0H2jT4S98jhSN8Ie9DW2mTFT1fnHObF6F_Ju_-wlv1KsDQurk1IvH1cP20wGU3ZtqBK21ae1JdtiZlR90eDFrVhq-KH42tdJ4pbpWZmGEzGKebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea61c87680.mp4?token=scyQEwH5IMRA5eKABOyDUZUyG9_qv9xKYAgywVbuh_OejTGbn8sUD0Y9IOafsCsVPATc9YsIg8yZ3TbM3QiLnukYHACsaHDIjjwEFHc9nid0IILvza4VUk1RrZi3sdQjwTdgBhumcVPhSY80CU96oHn76vGoE2hUI8axz5-TK5WdYsWNwSh8bam9jW5XWrcl7qwzt8DnmfzEmKhrxAR4AX77cZfEFCwN-70JGa-0H2jT4S98jhSN8Ie9DW2mTFT1fnHObF6F_Ju_-wlv1KsDQurk1IvH1cP20wGU3ZtqBK21ae1JdtiZlR90eDFrVhq-KH42tdJ4pbpWZmGEzGKebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش ناصر حجازی به پیشنهاد گرین کارت؛ آمریکایی ها باید به دستبوس ما بیایند!
همسر مرحوم حجازی: وقتی بهش پیشنهاد گرین کارت آمریکا رو دادم چنان فریادهایی میزد که ستون خونه می‌لرزید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/Futball180TV/90252" target="_blank">📅 21:15 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90251">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90251" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/Futball180TV/90251" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90250">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKohGsPy68BNX0pMqhX5wtE4R9DmsMiDuc2SQx8xDfAmGoGOtdaYmRLzXfpre-rMWxFrUAQWcDXBPGye_8p1gxhGOVkF4nNtVYT-NPC48ptfCt05f3OkVqVVZQuygNe5_BFzkaICty_UF6PyiVaCmiUiOxWLLIR0YJI65c-K-mC_WszyIx51Xhv6SuFlSnhz5CtDUdTSkzBQn-2alEuNwYVbNXE_uo1eleuUtGjB7LzRLcq9WvUd-SX8Fe8sKgFLVmr-7xZWuQHEl1tm4eAMoTV35K_82ygoQsI_hmuSg2lTE9bVqGIat3_xRb85S_jMOfZwKd4btDQa430HcBShSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/Futball180TV/90250" target="_blank">📅 21:14 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90249">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=QmFtsY8f1AKmikzCTvLySxza9Zmgd49jHN48mEmuoRR75uyusEiNvOoupJ1lZrMRIb15t3H7dvazui1L-W3rDqu1gzRSzjHJ7yRUtit_LcaXmz3ivr874E84c1VxuBCiYJJSuMDgR1CkadxKNF9IYFMnc0VenZ890nyxDufSHLAcXNX2kMHAxcAykg1KHXEjmm35simIRxB-LdZZmf5sHX9nxffOB6Xx_vAnsqxhKbZwwbifhnmr0q4QFeRWZ9IsuGcxiyHWN8xXep4UNDZqi9IrfXjAkSG-E8FsRcU68vQXBcaNjwRYCGKig4-_GLQdI4i7yyMgdOcZSLECRewWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/baad93a3a8.mp4?token=QmFtsY8f1AKmikzCTvLySxza9Zmgd49jHN48mEmuoRR75uyusEiNvOoupJ1lZrMRIb15t3H7dvazui1L-W3rDqu1gzRSzjHJ7yRUtit_LcaXmz3ivr874E84c1VxuBCiYJJSuMDgR1CkadxKNF9IYFMnc0VenZ890nyxDufSHLAcXNX2kMHAxcAykg1KHXEjmm35simIRxB-LdZZmf5sHX9nxffOB6Xx_vAnsqxhKbZwwbifhnmr0q4QFeRWZ9IsuGcxiyHWN8xXep4UNDZqi9IrfXjAkSG-E8FsRcU68vQXBcaNjwRYCGKig4-_GLQdI4i7yyMgdOcZSLECRewWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ازبک‌ها آماده حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/Futball180TV/90249" target="_blank">📅 20:28 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90248">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnssZXpvfiT_-Z8YwIujw3cO3BXS_Cz5uQZ3Jqq-4_w8irOHi4cjFnxRsl6vyKYse52njTJHq5ZQc0ZVfdjpQqhFjv7Eqh9BHqbfhVQ_AmbZzxLyeJlq6W8mf80XuBD7JYtjaXFhVvPWqJR72DgfdWXDDWWxvNVmsMOPo3Th1txvR71QwUPCw54_S-FALSHi1PNE8RHsZ7WTnCcfjF_a9PIJhTHVc7r_UZFbknz0g-8H2ncUpoBG1AC9xZLNnYxW1YwRnIx8rWy-GRLlHTmEClbXP3zHZ2T2FYLHsnKmgIAw8JT3UchFJNRHU6BkaJ0yWGnxFDhe4dVvNf_eCuf0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با اعلام رومانو، قرارداد آنتونی رودیگر با رئال‌مادرید یکسال دیگر تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/Futball180TV/90248" target="_blank">📅 20:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90247">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🔺
دسترسی به ChatGPT روی خطوط همراه اول و ایرانسل برقرار شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/Futball180TV/90247" target="_blank">📅 19:59 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90246">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHavH04Yx_mgtIfXik6I1kLGNww_LMbGQIZ-2FTmH5CS1TGVI9uNovt9oL3PoLX8pfvOqVAVrMNskWd8qct4LdX2qDwn-cpRVB-BZGyNJgg8ZZal1KKDZZmmk8rEWYOSROkN7-pJskoBmBJma5lHYeS6_KwTBIUKb5IltljHygmxgVBMuFEE1B-c_HKiUXd-8N5kxIDX8mv2igt0zUKMoXYw-vQcgjvg1043PSQgtYqLagtalm7ttVd5yZ6ONF1bHcdreaGT_u5yhZfR0LYo2Fl027sOvA4jO1dOuubMgxctMJngf_Yvvxs7-SuCIW30v6mNXMlXEkK4z5NSUFLRRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سیدبندی فصل‌آینده لیگ‌قهرمانان مشخص شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/Futball180TV/90246" target="_blank">📅 19:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90245">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/Futball180TV/90245" target="_blank">📅 19:16 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90244">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تا ۲۴ ساعت آینده سطح دسترسی به اینترنت به حالت قبلی برخواهد گشت. درحال حاضر اتصال وای‌فای درحال بازگشت به شرایط قبل است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/Futball180TV/90244" target="_blank">📅 19:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90243">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLgdSPhKQC5ZOxkcZo1QUQ-wReCt5P20BGfGZkucJ--I34HkuR2NYN9CtZVkaRgl8kc8T9oPOhRg8upZ3bR0RRwLeztPho-RigYhlIOpnDwHWwfYzOvGUSaCy-ZKAwTfPt1oCUU4WS71I-dpK6QI6yYp3soSLuUMr7CbkA0-Qw5l5wUtMXmOvO4JJ738AI4CGM2z8pDEBFSjJe1CQDlo27gSDBOhkQ3bVb5LTjpxnthENxnOI3QF9huZe9V91TfXhwrVofc_BvReTe47_LuP9FbhRkSipJxdKiwSDd5RAn03L8PnPIE6hbXdGYk1S5zE9JJPziTHlaAzWhBbpYDcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ‌فصل 2026/27 سری‌آ ایتالیا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/90243" target="_blank">📅 18:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90242">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN4VUFmiJWTfdREE0aR_kLSQiubXFF3dVmeIcE79krVbOujFXNwzMuq5OmIteQaGmgV2DXkUoflMLb4PLcjUJv14fvzHGRNckBx-qOzQLzFza6XgeBBiGmmMW-HULOFsXvcN9x-5slmH32tA3tjkB0aHcUt6-OhY7ubGwmp1cA_YBMIfoxs1fxbFXUFYYqIHg0PkKKPf76RdW86l4p3aa6J529UpcrqMO0f3C0bP1dpmzD7xvM4-ZU7_QA-TsIyykW6a8-4_dC1aYZpxYHefBszfRyFHo3NbLcD3oJ6XUm6F9v9Jtg6gZ-u0Le91Lf9XzcAqLczo7Z3_QUbViVO-yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل 2026/27 لیگ‌برتر جزیره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/Futball180TV/90242" target="_blank">📅 17:53 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90241">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_ob8S3L2qE4Cdw906iMX7DQm4_HtxfhWjXpCnLiATYey7C376b1wy7LRaRvmq6x59ec1Ic3DuGk16Kc0wDO_z5wcefIRtcaX1CzLgtwZQi1Q-wGZxMJvnA4V-6b_l-hmh1jNJGCkO3r5tqKfQ5a7vrOn6OZ9_-SMnBpzlU0muR4ddAsofreizcQmRpQ6t1KfU-GSUMvg4fpsu6BTWjpdaRvoZwx4Rh4YkSTbScilFSRNkfmp9EgujdV1pFdKYqutUG3bNtdLj7iS-dnPbB14St2wv1cuBeNpY66OW7QRsp4uBFtc1Zz9vXHdd53WsRtLXQZQXiBWKDpW242PVhLEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باشگاه بارسلونا برای جذب آلوارز پیشنهاد پرداخت ۱۰۰ میلیون یورو + مارک کاسادو را به اتلتیکومادرید ارائه کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/Futball180TV/90241" target="_blank">📅 17:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90240">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oYlnRrSc7256Y_UqfU6uoBGrxcfkgXVkCYG9S9F3jp41LfO7l4_PY9LyCNBYF4fbeFvKuDKBW7jXEcZjRnLExwX2R4dxyv--6QpwUtvlILVbwU_o5AqDh1UACNRqUgpCREJ8d9DJ9w19zXMoAnGmRPteNzlVTQF_a1wzJ2Q-daaSOwmXRk3weIBVXDmshIB7t1JjwRPQzafPAOw4CHuzG21-2YXJzQld5pNPHX4kjCFvKmf70LdUCfbduPLepBCjcknQARDoqkdn9WHw8gff3NpvmO8qhoel6t_3PIEsGo2nk5Z6EdzAO0WEmqFh3M-xNIV_54T5zumhXVLSnh9sCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۶ ورزشگاهی که میزبان بازی‌های جام‌جهانی هستند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/Futball180TV/90240" target="_blank">📅 17:21 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90239">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5H2EY7BjZEe-8IEmREywH48zhi9XquT0UO8KHE6YlK5ouA-sZiMm4DYIOfpwKCJyZxfRcBDwK4a7OO09vmvHoOKjccFctQCFYOHCVbq6cMZm8LaySauNx07b-myllaXxZ8UeYeGPUujKui_ifO9dL3K70NmU1eld2t97XZ6CJyVUTiOPd1Exwt_K591uez80J6ugf9pYc4yEy7nDBOts_uc2X4s6ZbLHgF3r6bkTl-Pb3nmFiIeik4VcKifqjbfyAfT05nMXJoywySxqQhhPyNGDSXP9xPGs_UIkFnTp7zMMdyIrPqCzgaqlpVHjvvTBCBWdz-aPaXWw2UKlDSVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
محمدرضا عارف معاون اول پزشکیان: اینترنت بین‌الملل در دسترس قرار گرفت
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/Futball180TV/90239" target="_blank">📅 16:58 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90238">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مخصوص وای‌فای :
https://t.me/proxy?server=87.248.129.199&port=25565&secret=79e344818749bd7ac519130220c25d09</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/Futball180TV/90238" target="_blank">📅 16:40 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90237">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq77jnUqGUq5Q3qKzvs08dhRzWdk_m_TEnHk0iM5ZyHx1V4lnkvp6IjUkHDDjKjvQA9aJCkqLt3zPtiW7k--7gb3q5xXBWGx6fM0kFo5MfmRbH8JD0ESHNIpxg9Qdk9Baq74t0OA1iMFxwGfeHTQdffW-hSPzUeBio2CBo2DHT9rU_IaAKiSVd2GHyiA2BRx1RUolBS6SQbGytIB82TJ7-nmwOyzP_EN7Ubtg9rPZVD96iipOmN0z8VDazZiRiT0QzaUFi89pZ3R5FxONZDEAiawVHcw8vWItEMbblL8PnT2jSTYQeyvuAbKZzkq-m0cZ_QN_BNl6Mex-fFIPd_2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نت بلاکس: نمودار زنده نشان‌دهنده بازگشت نسبی اتصال اینترنت بین‌الملل در ایران است.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/Futball180TV/90237" target="_blank">📅 16:34 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90236">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQFtDntXf1u4goCc_G2dPKY_uiwYU6BGF7pyp13wZqECqSkhkNH5pJZhaEyRbrrg7gNNdWQmOLTz0m0L7oZl8J9abCstZP0Nk2rHrMhcHOkSWN9n3BSCrnA5Ux7lzXpVt1fev6N1s9D_FwVQr75Jv2GQjTxbMK-eC3cAM8DG8XfmGahk9cSFXXHB7DimshMSXrCCzexbs5gDq4riQuKzqM-FvzWFxeB7EMEtb43DFS-C2LT0VOSUJ16sAmzD7eKTKWteoqnQ6DomVUwVsZqH8zN7DOOiE7Rlba4fG7Qy8-nOHzEXVZC9lP6YvyvqbGfCb1f0CdD9iD17czmMSzShqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور خوسلو در مراسم خداحافظی کارواخال؛ این دو نفر باجناق هستن و با خواهران دوقلو ازدواج کردند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/Futball180TV/90236" target="_blank">📅 14:35 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90235">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZaul7h3s3SON6Qs8eWTNCFgZFI5vR_1X9igovKqUOtUho65X32mSPI7Yyn7rswqhkNGiJIsAP9alznqm9mEGy7xVg4sBITPGRN496iIc7RmQWJK0vTAQYWvBt_osuO-dCNfvDXKW7_nwuavkaefeBQstuB_TaAzFseyffGOW7DnlwvAT6UbtdXuLc3sUQ74B5sIpNFgKoqr8C0gY5zISBGxuVANmgzaD2chRZa9nk6MLaKmrugrlEL84tQ2-8zaHtSZFLXfuUIeP3QYkVE4JaITu-EK3xH2hq4r-v5S0tHLbPlTBy7MKsBvO0MbkaopTmApYg2Cu_lvzACu1lPcvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این ۴ نفر، شاکی قضایی «اتصال اینترنت بین‌الملل» هستند
خبرنگار «انتخاب» دقایقی پیش کسب اطلاع کرد که ۴ نفر شاکی حقیقیِ «توقف اتصال اینترنت بین‌الملل» هستند. این ۴ نفر که گرایش سیاسی آن‌ها کاملاً مشخص است و تحت راهبری یک مقام ابقا شده‌ی دولت رییسی، دست به شکایت زده‌اند، عبارتند از
کامیار ثقفی، رضا تقی پور، رسول جلیلی و محمد حسن انتظاری
. / انتخاب
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/Futball180TV/90235" target="_blank">📅 14:24 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
وزیر علوم اعلام کرد که تکلیف امتحانات پایان ترم دانشجویان کارشناسی طی چند روز آینده مشخص و اعلام خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/90234" target="_blank">📅 13:54 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90233">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
#فوری؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی…</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/Futball180TV/90233" target="_blank">📅 13:44 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpn-njCDkz4cRMOGToJuL3JIwjDktTqOFQFXmyZZcxA05xxft1L5eXldxTOv9yCdXaQSfA_LCfWBMHVvVCI8z31Vh_FTAer6-TDqQQ9Qt2kl1gGlZzNXSl0SfQoHRAxDlNg0s3jH2DFmFS3th15Zs84ahQicK8x_Yc0R8Q7Oq5Z_QcfqkdvQu0cgMj95sEV4ecZsOerb6ZKGCO0IxLexlzujQIjCxjoMApFMpgNVkrHexdJB9qmpEE770ejIMNfJNsHsKFK1VqpaDR_lUiERCUJaqSbl3bUo7cdf6djUSaxlIiT4jUOwgw7AdjkhJYREMSq0EQKbJVbOsAY9vzIcww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری
؛ سیتنا:
🔸
دستور وزیر ارتباطات برای اتصال اینترنت صادر شد؛ اتصال جهانی ایران از همین دقایق احیا می‌شود؛ اتصال کامل مردم تا 24 ساعت آینده
🔸
معاون سیاست گذاری و برنامه‌ریزی توسعه فاوا و اقتصاد دیجیتال وزارت ارتباطات، در پی دستور رییس جمهور از بازگشایی تدریجی اینترنت تا دقایقی دیگر خبر داد و گفت: دسترسی کامل مردم به اینترنت تا 24 ساعت آینده میسر می شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.92K · <a href="https://t.me/Futball180TV/90232" target="_blank">📅 13:17 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=C-zcjlbCPjH4sM8NGZydyL7it8lGmqgTkTle-T3gAI398sJhP_QNoDof0AjHXgpZthVDP4u149wEbbU1NvBtu8_NrpE7rSB6u5gdjEUUGIWvQlv7ZqpMpqLS67n_Wx1pf56Wlfjq4r23daHLZNXmhYwwJMtXc4uUSy1DgpDR2Kt3b0LSS8CgYEOFmDR9QSrpASB3M-tLNSLEVA4ZKnbwCzgtY_4QXT0Tj_CFz7SiDLKmiNf3yG-KGxMawB7xzjg4bYhoTdQKx4I6HURlr-L7uBrTxu-clWKDowaZ7ZpctwBmR5K1NVDwM7KEx3iLmi28VVhQKGGVkx2Rm5TD0g-_A25ZJmqnAGxujQLltYpqmYoJsRL4SmGJhdTErCY9u6DNKcJpl-dywOdZHXgN1e3O2XKnlULD9n2vEU-rHCVQk90kHqkdeXqsRVtLZpruRXqoVLRdL8A-lcdUENE3_P0PND2qKuMrbiCrXSrZ5e4zcs0DTjA-TCqe0H4Pfot394KAsEY0W8-nO9U9nXPpV7t3JpHdjJXKWK2aSP36qRdnH8Rhj61t80LmyxTJ6S_YfpFcCHKex-knjTMRVaUk3VP4GLkhxoHMrUHXFADE8gVYyX2YGcQMiY9Hp-90cM5VrQbSSDkBrbTiwEWJY0fQydl9-kS5suDZNNCfNRSf8ZR8_w4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0edb93becd.mp4?token=C-zcjlbCPjH4sM8NGZydyL7it8lGmqgTkTle-T3gAI398sJhP_QNoDof0AjHXgpZthVDP4u149wEbbU1NvBtu8_NrpE7rSB6u5gdjEUUGIWvQlv7ZqpMpqLS67n_Wx1pf56Wlfjq4r23daHLZNXmhYwwJMtXc4uUSy1DgpDR2Kt3b0LSS8CgYEOFmDR9QSrpASB3M-tLNSLEVA4ZKnbwCzgtY_4QXT0Tj_CFz7SiDLKmiNf3yG-KGxMawB7xzjg4bYhoTdQKx4I6HURlr-L7uBrTxu-clWKDowaZ7ZpctwBmR5K1NVDwM7KEx3iLmi28VVhQKGGVkx2Rm5TD0g-_A25ZJmqnAGxujQLltYpqmYoJsRL4SmGJhdTErCY9u6DNKcJpl-dywOdZHXgN1e3O2XKnlULD9n2vEU-rHCVQk90kHqkdeXqsRVtLZpruRXqoVLRdL8A-lcdUENE3_P0PND2qKuMrbiCrXSrZ5e4zcs0DTjA-TCqe0H4Pfot394KAsEY0W8-nO9U9nXPpV7t3JpHdjJXKWK2aSP36qRdnH8Rhj61t80LmyxTJ6S_YfpFcCHKex-knjTMRVaUk3VP4GLkhxoHMrUHXFADE8gVYyX2YGcQMiY9Hp-90cM5VrQbSSDkBrbTiwEWJY0fQydl9-kS5suDZNNCfNRSf8ZR8_w4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
جزئیات درگیری علی دایی و علی کریمی در مراکش:
🔺
رضا جباری: فکر نمی کردم اینقدر علنی و شدید با هم اختلاف داشته باشند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/Futball180TV/90231" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90230">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90230" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/Futball180TV/90230" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MN0rfTzJqvoqC5BfIRrN3pJC0_6FJHeNyP0yp5z-ZwGBYiUQSSx_BntZSG5mwrvYnV0xGs8n0144LhjGUwLjsuitwA3ALqyy4tNSI9l3dIWZiQzjmsJX_zbfy0k9KuQZvIA6Ebe1pjKOFzTvvUZTQuNToixyvrcabm0Y8WkYvRMAcDC6IEdN0bU2vPeOTIrnRsv0LOIuQxEQA8sUWlYpnEkr_a_NtX_wfVqoZBLK-zEypm5nAPUYzhSCWQjKpBpAyRgVQWj_Z7ALexn1cmTbZpDAOE7YwMnrfvtRh4isPioRj-FHCTI1Fwi97OdGyhmDoqRP-keDfZ0Yn0ja8WkIMQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/Futball180TV/90229" target="_blank">📅 12:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=WEgg7-sJqMW6nzk23xCS4_99w4uCeSjHrERp0y-NDWhOvGtJbKr5cbwXDDYa3TQ-WHwn8PxaaErUoI20_HDoijiSoHK6Chrpbsfrb41Ws_CC-G3S87SKPPFVd9Y_9FaO2xcHS2GaDjyBtRzWmTjZuMJ4GE7E7o6H_zIc75zN0YkbT_KWy5c58zTUsWqTaXzUMWEvdSVLxVSD5Un7OqBOcur2bv6YxcHTwJP3-eBGL1IMD8dcR4n5uAjcIJfKOIWw-duBKLtkO8lW7uY1wCPq6f_wtwQ18lUYDtWEHa0IJvw9otiIQ7vidqZyxVPv-KNni5sa0Q45RzN0fCdwzERBdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d9611d964.mp4?token=WEgg7-sJqMW6nzk23xCS4_99w4uCeSjHrERp0y-NDWhOvGtJbKr5cbwXDDYa3TQ-WHwn8PxaaErUoI20_HDoijiSoHK6Chrpbsfrb41Ws_CC-G3S87SKPPFVd9Y_9FaO2xcHS2GaDjyBtRzWmTjZuMJ4GE7E7o6H_zIc75zN0YkbT_KWy5c58zTUsWqTaXzUMWEvdSVLxVSD5Un7OqBOcur2bv6YxcHTwJP3-eBGL1IMD8dcR4n5uAjcIJfKOIWw-duBKLtkO8lW7uY1wCPq6f_wtwQ18lUYDtWEHa0IJvw9otiIQ7vidqZyxVPv-KNni5sa0Q45RzN0fCdwzERBdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریکشن گاوی و لامین‌یامال پس از حضور در جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/Futball180TV/90228" target="_blank">📅 11:30 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90227">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
آیت‌الله مجتبی خامنه‌ای: رژیم صهیونیستی مطابق گفته پدرم، ۲۵ سال آینده را نخواهد دید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/Futball180TV/90227" target="_blank">📅 11:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90226">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=QD4xiTmdTSQDKQK21JjGHIhzfVxKOrRi5sjzoEMQckxraDgzaB1JS97KquqEzc-RgwaQYZNDqMXpZ4oeLGvAoRJw05wddfjci8piA6ZpnDMM58gafG3pXK33dG1tSF00DE_7bSEAhs-5KKPS_x3cqXExJ-xlceiCFL0_xmPemWUiPHJXnuA2Re3c3hh-d0R6z0q-5DJSNKFK6NfYppqEPhYiIuRj1Otz4BqzqHdMaaEprjY54UEVKdyzOYMMUXdwXriZOs_ETXj380wGdySSiIki_n60NfiqZxztliN-UsJYn4ovY7g9-A8IV91nXDiCOgaM3TpahIqsbRnKHeS-yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0834d346.mp4?token=QD4xiTmdTSQDKQK21JjGHIhzfVxKOrRi5sjzoEMQckxraDgzaB1JS97KquqEzc-RgwaQYZNDqMXpZ4oeLGvAoRJw05wddfjci8piA6ZpnDMM58gafG3pXK33dG1tSF00DE_7bSEAhs-5KKPS_x3cqXExJ-xlceiCFL0_xmPemWUiPHJXnuA2Re3c3hh-d0R6z0q-5DJSNKFK6NfYppqEPhYiIuRj1Otz4BqzqHdMaaEprjY54UEVKdyzOYMMUXdwXriZOs_ETXj380wGdySSiIki_n60NfiqZxztliN-UsJYn4ovY7g9-A8IV91nXDiCOgaM3TpahIqsbRnKHeS-yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینترنت بین الملل چه زمانی وصل می‌شود؟
🔘
سخنگوی دولت: امیدواریم با ابلاغ رئیس جمهور ظرف روزهای آتی اینترنت بین الملل بازگشایی شود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/Futball180TV/90226" target="_blank">📅 11:07 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90225">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9Y6Fla1XMPborb0mnsH0Sl3ys9VZPO55TWXRLbpllpIp4sYCtEg5GMhmYd-c4IryZlDEf86n0vvWohx5CWV5hk8iDvVxawaTgKmzR4s45Nb8DZR8GjOPPydrCxGxCCvrEjnu5K1apa-_4LrbzflQkUsBk1vTUWCqF_h1Qdbg1lGMcYx9PT8_h6g5QD3_ojgW7MEWDF0NuiEACwaKi0ogzUtgtGnTcbs_bLslocw7yl4vj6Bx58aNsHMjvRZby3pSdYoP6_-thZvfkhV4LDbInW1Ztgqsm_XW3149__56IRPSl06fa7g2RjWGQ2vYulgPmjrqiTaBOPG9eDHuVssKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C قرار داشتند. برزیل مهمترین تیم گروه C در جام‌جهانی است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/Futball180TV/90225" target="_blank">📅 11:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDcUNuu5X8nBkiuTEt_w8MWj_y2_Ark0BrOQYn1iLizCtRymq0QhYydgDN16GYOT648d4D417O85xVcoJl4uhH7qA4KwfCeqo7IUjALfR2_Kk-PKGjkxiMsbPfLB-Ba0oqJenysnlnhyvFIY8ljW6KWmOkQTJFfzuhLT51DQCCAAEYI_e9DYpvUfv7pigHQAMEACGap0F8lAuaoHUyx2KKj4CScO29HWM7R2LrS3lOrQl-eesgaobzkMBZ9iXFAKKg51BunsfyKTw4hpe7JbenOvZy_ddY5Bp7LKNqB0PE-cUhhiMeBqXMgIJccUGPl2EerNJHpMnM66v1sIWfJr5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با آغاز اتصال احتمالی اینترنت بین‌الملل؛
ساعاتی است جیمیل در دسترس کاربران ایران قرار گرفت.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/Futball180TV/90224" target="_blank">📅 10:26 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=XAox9lunF6MSIxYYGPlTrn6G4YjEe05EAEvfWPBmszY8hiq1ciwvWDlWU8_hdoFeMG26EdxXTykNGr0SklcQUi_cuHb6EP-X7df0Yc_lF-_RFbajYBfYU76_6q-b5Qomq9TyaVF5fxRTqIss8OjLJRf67Wu4IvKCh6TiMcDTpGNNzZWmSoPhKniQ_3xrxxBiFAQYF1xs0GzsuMMaTIMOKNmS6PQpsU4zTD-Uer_tiNkD3tb4him5tyof3ogt0wWN2ZMu4R4-kgL3cEwSp5gpwine_migzheZLk6EZhIghHO5dpbCpL7EY4Du34nNcw1EGosO-Dbf23xpmrPlwDYsDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7673ee9149.mp4?token=XAox9lunF6MSIxYYGPlTrn6G4YjEe05EAEvfWPBmszY8hiq1ciwvWDlWU8_hdoFeMG26EdxXTykNGr0SklcQUi_cuHb6EP-X7df0Yc_lF-_RFbajYBfYU76_6q-b5Qomq9TyaVF5fxRTqIss8OjLJRf67Wu4IvKCh6TiMcDTpGNNzZWmSoPhKniQ_3xrxxBiFAQYF1xs0GzsuMMaTIMOKNmS6PQpsU4zTD-Uer_tiNkD3tb4him5tyof3ogt0wWN2ZMu4R4-kgL3cEwSp5gpwine_migzheZLk6EZhIghHO5dpbCpL7EY4Du34nNcw1EGosO-Dbf23xpmrPlwDYsDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترکیه در آستانه جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/90223" target="_blank">📅 10:03 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=Re00sxrH3yXKY4bkeNdl2nXx9resdYaHpxwrikbr0sSKjs0TnhmKZ_OpYSH5HdxYyP8XMozgFd-QUyVy58Wb9FI1_gtWnwQK2z18HD_YH7CCNmQEtxkLU0-yiYcTOUAzyOZPjDcgHsESWQkxrRDoHpQeBsayUywi7Jdno_L7bkhzuZ9mIfCG7uoGwFhAZ_Az4IhylwNIXOR4ALw2mVwwtjrMSJL5IVnwSKUko3l4FVrzvrXKdVsnA-aFlKYPdrY74K9UgTn9yEo9qf1wwHiteM3vZmyq90yj8TRtkMK4tGOKeJsBIHlxeYyJBCctQQxyuqxSOpe3pmtlk9wyi4jgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ed589fd9b.mp4?token=Re00sxrH3yXKY4bkeNdl2nXx9resdYaHpxwrikbr0sSKjs0TnhmKZ_OpYSH5HdxYyP8XMozgFd-QUyVy58Wb9FI1_gtWnwQK2z18HD_YH7CCNmQEtxkLU0-yiYcTOUAzyOZPjDcgHsESWQkxrRDoHpQeBsayUywi7Jdno_L7bkhzuZ9mIfCG7uoGwFhAZ_Az4IhylwNIXOR4ALw2mVwwtjrMSJL5IVnwSKUko3l4FVrzvrXKdVsnA-aFlKYPdrY74K9UgTn9yEo9qf1wwHiteM3vZmyq90yj8TRtkMK4tGOKeJsBIHlxeYyJBCctQQxyuqxSOpe3pmtlk9wyi4jgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
سیاوش اکبرپور: جرمی دوکو رو می‌شه مهار کرد!
😁
محسن مسلمان: ولی نمی‌شه؛ فکر نکنم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/Futball180TV/90222" target="_blank">📅 08:51 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/90221" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzxUMAQejH0Rg1PRASNl1Q0x-2Cnq3qf9u5LGAjKQmNiEazrUuMzvGvTCPSdh_br6mOM5L1-vYqDaE6VhdwX2oAwxoq-87JJ3J-FzTXa2oAvYqsHSkIzkUKcy3zdpIH0DLNOBOVprSXFE5zA1Mpw7_r7dAvVczr9qfNCKIdHp73CpTveMJFzem-Hy-zf8bM0mFqT7szpQbOiUf6bzbzASUHwlQHITJSOMUxIZwBlcEs5RAnCnFL8MYk1bobXiVR4eOZJOkMW0aocSLe8aJNS6oaoMX73ZT-xdK9CO5HjuMFIewcWvIw3xfRX1QqzNqnRuGF3lpqJDjA1ep9zLbqUSg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6K · <a href="https://t.me/Futball180TV/90220" target="_blank">📅 00:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90219">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuABEr23abHGi_iuO5ht7uTo4e0SvabaT_YdnAFzClsPlApnX_5GEbMMpJGwfupH8fDQKVW1ckg9T54uYPCF2QBMFlzT7FWiaaAuCJqQ0mnDQGQQMoEW7E2rhY3HBfrxl6gh5yfCNQ-T_-rsnFaSEIVxS2Wy0mYRiRIZ74t-KZJ0EPdmJa-JxeU1aKvVFhql1-UDq9wPIzncQnG71H7RpO0LrhDzJ6gWrQnqow9yPppvoR4rYUWMwHxIkhGcesxfJwjrtpEkwqTsJ2q3BBl3uPpcXlCGjWhLZgWBi_qXPI2sbMWjkpzLuP-qySpE5ijP-OfVkNCm7qeAte8SR17L8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇴
لیست تیم ملی کلمبیا برای
#جام_جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/Futball180TV/90219" target="_blank">📅 23:43 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90218">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aIvCgTkm64Uc0cNQ4J4JdhR1rcbbMFq9D4bxKaIe5IiiQMzAxzDXajG_QF7p22Hsr8DbjWvKqa9aTk_CZMjXIku1M2CRov1rIRslY2ytneKgl_k_kwTlJIHYIb5yoS0oEGIO0o8-nnRCBD4Op89LeGvvw-JPdJYVKlUiVf7aTMozfViay6VGUZ0rftGBdOX8vRbNAfcjccym1oJ4APKiDSJraL996XlD_X9QrT2OAY54EDacCkV4RyuzKwgWsKT85vQ4ZFmQQyqqfoziYPV7ywXsba4z7XVM3-gYdfjleNRRhOLWQHit8h9NTVywk_dqFCN8omCGtIntYoPYKHFhuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکس آلگری از هدایت میلان برکنار شد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/90218" target="_blank">📅 23:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90217">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=uS2CB4v-9zi73TutlF5V3cglMkgsZDqjmcrHTyl6thF9XkhbdDGt9QPGHq31Itd790qfE2ae5YMNbTdJL8VhxwreM43xSU61kQlGDJV1CaRFWkCJnWjJzk5nCkcuFjk0JsaDnxujWkXtnUNRRtNp8KB73g9MqmzoPM17F104YP1-0jeRIXffpjSQFTSZkrCwOOm1BYTkCPcuqHmwjvpVLEZtIIArkFhVEmyzhmgxwyy17ZG7PEV8mbq4dwDc38KqrIzMksA3Iln3sS1Hv74e_MU5gkqDLzIA1tpA8WUF-qNz9LE3y2CjhRI6ScCtAnUggtg-cnXyePZRtB0HyHoQk6CySgeHLgr3qpFONLYUHujFyKWUUv281hMmIM7ekbeic9wZZCbvyTX5Nzc2UEBJQkWMzwSFOT1tpGSYzZEHhAwHhslv0lQi8wWpX4GTD0lDVyT95zmILhssWNsKrRzGCIhxZ-vC0dgCyUF6wcL1ElPzp6xK_ydrKuxz15M7EctFZqS3mg8AJYIhIyVKwlwxdvnHYWb8pDuusMw0rYX-SnqOzjuc77hSsDvbZjoz8shY4IdXvr70sqgKRaofVRj9xhZ8irTK_CoIRr99v7eYrlvsc250hHIBYVf_jcr22QZ3RT9OQmjvd9wv7YcadFhREtH8JeS206NYLVIxMnB6QYI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3602a6e5c9.mp4?token=uS2CB4v-9zi73TutlF5V3cglMkgsZDqjmcrHTyl6thF9XkhbdDGt9QPGHq31Itd790qfE2ae5YMNbTdJL8VhxwreM43xSU61kQlGDJV1CaRFWkCJnWjJzk5nCkcuFjk0JsaDnxujWkXtnUNRRtNp8KB73g9MqmzoPM17F104YP1-0jeRIXffpjSQFTSZkrCwOOm1BYTkCPcuqHmwjvpVLEZtIIArkFhVEmyzhmgxwyy17ZG7PEV8mbq4dwDc38KqrIzMksA3Iln3sS1Hv74e_MU5gkqDLzIA1tpA8WUF-qNz9LE3y2CjhRI6ScCtAnUggtg-cnXyePZRtB0HyHoQk6CySgeHLgr3qpFONLYUHujFyKWUUv281hMmIM7ekbeic9wZZCbvyTX5Nzc2UEBJQkWMzwSFOT1tpGSYzZEHhAwHhslv0lQi8wWpX4GTD0lDVyT95zmILhssWNsKrRzGCIhxZ-vC0dgCyUF6wcL1ElPzp6xK_ydrKuxz15M7EctFZqS3mg8AJYIhIyVKwlwxdvnHYWb8pDuusMw0rYX-SnqOzjuc77hSsDvbZjoz8shY4IdXvr70sqgKRaofVRj9xhZ8irTK_CoIRr99v7eYrlvsc250hHIBYVf_jcr22QZ3RT9OQmjvd9wv7YcadFhREtH8JeS206NYLVIxMnB6QYI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما ۱۳ نظامی در عملیات خشم حماسی از دست دادیم تا مطمئن شویم ایران به سلاح اتمی دست پیدا نمی‌کند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/Futball180TV/90217" target="_blank">📅 21:10 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90216">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0L_lgQgw_M9elY28SWPhTeVSlEH8pGwc4yoaGZ8aIVPiQKvaF2VTNOe8ne8yriI7tDfOtGTotqeLGci23aNKAS6_URU_4RIGmJrAE2Pu-DxFbSwXq5mrI7uNcnQe0mLyjtcHpFNYOF9guEeeKMB5HnH0O9_JOREXT8YSSzBKuz4Lrb481c3imikxefdYK4LQC6O3i83s7guXcYD9KP5CJUfYuHtX_ywaQyQADTWR_f3QRbduSTrG1nv0yDeowMQO2YrT5GxAF9WUSwn-nNtZqT7ie836mSCuQPQcIu159Z02iPM_ONUOrfmWdAifzTKAJBvkgGlWzCb6z-FrkkwPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سن-اتین - نیس
🏆
پلی‌آف لیگ ۱ فرانسه
🇫🇷
⏰
سه‌شنبه ساعت ۲۲:۱۵
🏟
ورزشگاه جفری-گیشارد
🎲
با بیش از ۴۵۰ نوع آپشن پیش‌بینی
⚡️
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
سن-اتین در
۱۰
دیدار اخیر خود، چهار برد و سه تساوی کسب کرده و در سه بازی شکست خورده است.
✅
نیس در
۱۰
دیدار اخیر خود،
پنج
تساوی کسب کرده و در
چهار
بازی شکست خورده و تنها در
یک
بازی پیروز شده است.
📈
میانگین گل در
۱۰
دیدار اخیر سن-اتین
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیس
۲.۳
گل در هر بازی بوده است.
🧠
اطمینان صددرصدی نشانه خطای شناختی است.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/Futball180TV/90216" target="_blank">📅 21:09 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90215">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=SEh2NS75yaXMQOJ7BPA9blk1evFWgx1BFTv5URxprbi-8OlLiMTQxPm_sWqMOj7NGcR0XUZB8RmFdjrt6Qi0PF_hE0x2erBRApb42hJUZaO78OopIxR2jvYrxehDXwunBrF8ZMzrL15f9RtJoEBawM9r8BuFi9ATfh6AQT6kW-Dh88le3Ui9i2pOECjF3Xur-hsXrSd1WGtIK_X6FcvFCa4_kDZ7iRCgkJuaHO1uy8oGsP4MdgNJ0V_GQ123HT7Gx983DPm8oSrz3Hi5-IsgHSGNiHK6plT7k8pKUIrJYTy7heHMuYY-xWNZQxHkBEYwDfdEnJ3MKfmewWNDCZ9frQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a7263cfb5.mp4?token=SEh2NS75yaXMQOJ7BPA9blk1evFWgx1BFTv5URxprbi-8OlLiMTQxPm_sWqMOj7NGcR0XUZB8RmFdjrt6Qi0PF_hE0x2erBRApb42hJUZaO78OopIxR2jvYrxehDXwunBrF8ZMzrL15f9RtJoEBawM9r8BuFi9ATfh6AQT6kW-Dh88le3Ui9i2pOECjF3Xur-hsXrSd1WGtIK_X6FcvFCa4_kDZ7iRCgkJuaHO1uy8oGsP4MdgNJ0V_GQ123HT7Gx983DPm8oSrz3Hi5-IsgHSGNiHK6plT7k8pKUIrJYTy7heHMuYY-xWNZQxHkBEYwDfdEnJ3MKfmewWNDCZ9frQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن‌روشن: فيتيله ترامپ رو بكشيد پايين وگرنه با "اسلحه ژ ٣ "ميريم آمريكا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/Futball180TV/90215" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/90214" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CyyMRJR1S5GwXUFebypDMzPvD8bbw2ilhN_NsLfzXrksubTa97AetYZVu4LC4p_rAlJvEpzU8_w_3fyUPdr0SXRvlhXh6EyljWJVc4LTZq9FhUMRn3F1XHpVZlt34c3530Vxw_JRRwiLMhZWPkpQyCilJWuGgSFJeGTD8UVHhN21lTTKVPi5V8IqiyWXuAb2Th26IUCyKoMRPIDa_x9ftrSc_HmWN2FMwXdD-7vnX2aqUe1RciqCK9S429f7GWX6fqqf4qfR55PqlWyB5ImISN4puz2b3uHRYErYqsQ08MfJuzLLNASzTLSUtCOcm9dZ5hbn9r9EQeRc4LLRbhKQqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/90213" target="_blank">📅 20:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🔷
جواد نکونام سرمربی سابق استقلال از طریق ارتباطات خود با افشین عبداللهیان مجری سابق شبکه ورزش که نفوذ گسترده‌ای در هلدینگ‌خلیج‌فارس دارد، خود را برای سرمربیگری فصل‌آینده استقلال معرفی کرده هرچند که در این میان تاجرنیا قصد دارد با سهراب بختیاری‌زاده در فصل‌آینده ادامه دهد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/90212" target="_blank">📅 16:53 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeQUHL5NhGguks9uR4DTeJmt3iFUrQddnDM8Gjula2zj-HN9IuxxC7A2yCx5cyGuSxYyQ2vlNi1S1yykZSZen2-yEy3ETUdjDqpARVog0e3FH89Z0bHmy_rbZrOaBKRGub5MKmHi3ULLluqIgbazOtQdAuxhRHQx2VyabsCJa__32VA1zDO_SBm5-M0M_rgBvZm0Y61EEzfLIL5QcwaDMJEEBQZ3taSDJWLwhpj7X-V1zOTVgv3xYSjf_HKHqfTXnuCHcPsmtKnUxwsM57p3J5WscJBLCon8NjlWl_7xplZYICDtlsYsF66ZVTVAjUlVDLV6Z3m4at60w2-ZlxsbTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست تیم‌ ملی اسپانیا برای جام جهانی 2026؛ بدون حضور حتی یک بازیکن از رئال مادرید!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/Futball180TV/90211" target="_blank">📅 14:52 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromV2rayYar</strong></div>
<div class="tg-text">🔐
سرور اختصاصی با پینگ فوق‌العاده پایین
مناسب گیم، ترید، استریم و استفاده حرفه‌ای
✅
سرعت و کیفیت عالی
✅
آی‌پی ترکیه واقعی
✅
پایداری بالا و بدون قطعی
✅
مناسب استفاده 24/7
✅
بدون محدودیت زمان و بدون ضریب
💰
قیمت تک: هر گیگ 150 هزار تومان
🤝
قیمت همکاری: هر گیگ فقط 120 هزار تومان
با ضمانت عودت وجه در صورت قطعی
🙏
برای تست و ثبت سفارش پیام بدید و از طریق ربات هم میتونید خرید هاتونو انجام بدید
✉️
:
@V2rayYar_bot
@V2rayyar_sup</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/Futball180TV/90210" target="_blank">📅 13:37 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
ستاد راهبردی فضای مجازی صبح امروز موضوع اتصال اینترنت بین‌الملل را مشابه دی‌ماه سال ۱۴۰۴ مصوب و به رئیس جمهور ابلاغ کرد تا در صورت تایید نهایی،‌ وزارت ارتباطات موضوع اتصال اینترنت را اجرایی کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/Futball180TV/90209" target="_blank">📅 12:47 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=FXHUU8dsemWsjVBuKPB8BB1TvObc2ihSOR23hAyk0yGgGIY_65DC5cWMWBhTNquMVfzwtxue5WarWxWwA90l-6fhYtTKpaFVJGDeWN0ZOj2bU5JxRHsvHp9LO_49mZakjS-j3yUpkr4k1fTWPy_WKveIpOtK70YH0Svd1G7yM1YZBDCyOPubsqRE5jLiTX4QFsz-oMC0RLMtzSJa1eQKNH7J0qyvbgJnCcCHGrGsc8K0eR85Y6mqarq-VS4FDTqCs_Vj-Ig68Y-JKespngU_EWJQX4yj8Kukzh6P5bHX4hjRj9gHXIZqCSifjzACg-Vqj9LbziLAWi0Zy4dbBlkW9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa22a668b.mp4?token=FXHUU8dsemWsjVBuKPB8BB1TvObc2ihSOR23hAyk0yGgGIY_65DC5cWMWBhTNquMVfzwtxue5WarWxWwA90l-6fhYtTKpaFVJGDeWN0ZOj2bU5JxRHsvHp9LO_49mZakjS-j3yUpkr4k1fTWPy_WKveIpOtK70YH0Svd1G7yM1YZBDCyOPubsqRE5jLiTX4QFsz-oMC0RLMtzSJa1eQKNH7J0qyvbgJnCcCHGrGsc8K0eR85Y6mqarq-VS4FDTqCs_Vj-Ig68Y-JKespngU_EWJQX4yj8Kukzh6P5bHX4hjRj9gHXIZqCSifjzACg-Vqj9LbziLAWi0Zy4dbBlkW9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین ریکشن‌های پپ‌گواردیولا در منچسترسیتی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/Futball180TV/90208" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90207" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/Futball180TV/90207" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnkdmxKhFr6lN6IeKlJG-6QK9SBa4FrZ6kHphycy3nD6UTZbYePg2kZK2lVaEnEV7uIG4DIqPujvrIn-Qg5_wBH0sJ8INt7za4DzxrR6HlCUy3KjpG38Y208G0bn3g5fJcAnK_ISBDguVsmmLOzommMEL6VfaBJpFg54WrXra6Fv3imzuKr7ZEHbE_PhvueY7yMIdagnVVoeE3NQWK_1yTYAAXw7a9elaqRvi7ikexAE3OTuVjb9czEAJqsbinTHjsl17XCCZRZVvXOC0-pocL1Wlxv9JoezKv-FNVIqP47W73hFrriSZACu64q1CxblmjPB-CtKg2eqbST1iU1vtw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/Futball180TV/90206" target="_blank">📅 12:39 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940870b589.mp4?token=WHuCRofL2OxGt_nUpO8xUgO0hJFFgaTs2UGa0i4jwsmsRoJE0PHFw0RhZy0rBym8yJx1oN0q_y-IzyWrs6o4YQImE9b4IvRESei-tTTXNSRWgq6xf1gIPClYy58KSycNL_oRgdvevOB3RJ3Al7C7bksqUWsgp4JuLRSlbbOw62cK6taRNifvsMle65J0ssNhZQTLHxt7iXxaAKi5_lT-3Q20PemMPCMX8rRKk8QF5R2VZeGG-8r1eoYde04r8D-Ak6GQ6ESN51FnSgc1OovzxC0eN6sBY_pE5aHZIRns5Z1A1-BfFyKblNII1LWf8p20XmaBuBZgy99m6SiVspDyqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940870b589.mp4?token=WHuCRofL2OxGt_nUpO8xUgO0hJFFgaTs2UGa0i4jwsmsRoJE0PHFw0RhZy0rBym8yJx1oN0q_y-IzyWrs6o4YQImE9b4IvRESei-tTTXNSRWgq6xf1gIPClYy58KSycNL_oRgdvevOB3RJ3Al7C7bksqUWsgp4JuLRSlbbOw62cK6taRNifvsMle65J0ssNhZQTLHxt7iXxaAKi5_lT-3Q20PemMPCMX8rRKk8QF5R2VZeGG-8r1eoYde04r8D-Ak6GQ6ESN51FnSgc1OovzxC0eN6sBY_pE5aHZIRns5Z1A1-BfFyKblNII1LWf8p20XmaBuBZgy99m6SiVspDyqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیگه محمد صلاح تنها قدم خواهد زد.
💔
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/Futball180TV/90205" target="_blank">📅 11:00 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=fCe-S2cvhVHzUk7D4K4t8PrlNcVGHL8fSYSrUoon-2UeFemzhYuYVcdgQ7tQ13kpT2AIpv9GbIgvqNF-0un_PeEd3Q1FRKGi70mdwUvTfDVETkc3j3q0P2FOtqFheKZelkcU5SOsd1oRu3CFlTiwzDhfUqTzlznwiWLWuuK9CKGGnp3itJ2EQKFfwtdxsXsJM8skZl9wKqByrfjWCUPRCga_PpGD-zA7uXYApV7-jIglpWpOsfcyR3otxMtAlKinCmjsqmrQGjhMJfTM_w9k8Xb4sF6qz8VpeQtBtyd8iplNnx5yDLHJ3sczVhL8BI4tueGQy1Hh4xyhKdhYADB60A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/392ebb3ce3.mp4?token=fCe-S2cvhVHzUk7D4K4t8PrlNcVGHL8fSYSrUoon-2UeFemzhYuYVcdgQ7tQ13kpT2AIpv9GbIgvqNF-0un_PeEd3Q1FRKGi70mdwUvTfDVETkc3j3q0P2FOtqFheKZelkcU5SOsd1oRu3CFlTiwzDhfUqTzlznwiWLWuuK9CKGGnp3itJ2EQKFfwtdxsXsJM8skZl9wKqByrfjWCUPRCga_PpGD-zA7uXYApV7-jIglpWpOsfcyR3otxMtAlKinCmjsqmrQGjhMJfTM_w9k8Xb4sF6qz8VpeQtBtyd8iplNnx5yDLHJ3sczVhL8BI4tueGQy1Hh4xyhKdhYADB60A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدومیت لیونل‌مسی در فاصله ۱۷ روز تا جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/Futball180TV/90204" target="_blank">📅 09:58 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76980eb486.mp4?token=rr0l_Yfb5cCE7oMYzfFiUJLAIZNJntk6L5oTehCGanyVtSPIocFfaY-UFPulwFpJlMUYIgbcmcfILu5OgaONpVGskfJ13ulBTvovZVpn2Huy34AwBKJlI4eMGwB8FaV1XFQD640h89zxrX5GYh2J4M2WnW5Zt_badw3g1_1lMD0XYuKArXvKwOqxNpIBo39ffYNuD3hEEkm47Nej7YuvTFaAGHZpFZQ75SEBF3cSivB1Opsi6MYBKivfZPx4WEIrEqQBVkN0UAwUYEMwaeYmNrFoukLwMq2AHugTMunvMG7VkCZGmHY40YC30ua1WhE-oFvdqGpV-DQOI_ZlmyB77g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76980eb486.mp4?token=rr0l_Yfb5cCE7oMYzfFiUJLAIZNJntk6L5oTehCGanyVtSPIocFfaY-UFPulwFpJlMUYIgbcmcfILu5OgaONpVGskfJ13ulBTvovZVpn2Huy34AwBKJlI4eMGwB8FaV1XFQD640h89zxrX5GYh2J4M2WnW5Zt_badw3g1_1lMD0XYuKArXvKwOqxNpIBo39ffYNuD3hEEkm47Nej7YuvTFaAGHZpFZQ75SEBF3cSivB1Opsi6MYBKivfZPx4WEIrEqQBVkN0UAwUYEMwaeYmNrFoukLwMq2AHugTMunvMG7VkCZGmHY40YC30ua1WhE-oFvdqGpV-DQOI_ZlmyB77g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وحید قلیچ در گفتگو با بهاره افشاری: امیر قلعه‌نویی واقعا غیرت و معرفت دارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/Futball180TV/90203" target="_blank">📅 09:01 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90200">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuRkrwqZn5rSraDtZQpfKPUu8xNqsK9cDdj5MW8EdqHOEat2fswqpzDVx7rN6bNTdhd_i2rDRuWoVHUf52uPiWllFtxR9I89hJYoT-U4XNC-pfb2N7CR4Qp41az40wcck5imcvIXzu5876cf3mncn1nnkjVdJgFFA2dK139g8Ku2HXbkR6Hl_wKsMg9jj59CINh3dhWvdqXXLg8GC_1_QkEeyE637t0b96nKwZqjZ_JNB4-7Jh0syVREBpNNid4HOaL6SQs3WWNU3UHTXWt6vpy1UbCSSZyxcy2CuXHjYdr6gHmq3gi4QzsjI2zX1bTgWxSl7NqjOX8YNk4PHbIdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درخشش کومان ستاره النصر در دوران باشگاهی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/Futball180TV/90200" target="_blank">📅 00:11 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90199">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=SqwtgOI7nDnuqKZkKWW93DjmasXLW4NV5J98EKM8pncILNEitQEakzEYLvIa34h3luOoapr5prVPsnry7CWCMFq_5ub_Z9LLhYhaUir8S4SF_7mVblrDcG-r6Xbwz5n-dyPRlCi-Dw0nN6xY-RO0VQC1v0a-C41i3jgTuKm9GUZOoGL0tO2X3W0BIfGsQMd0yD-O1KLU5wqsZx0G0QtfpIe9OewJggLm7jX7W9He_9VaHFyaH7ht5CVNU9Vh5_AOOXNLoKLm4-PrB5LO3paT_fLc_DDGI-suBRnRtaGiOEvnp6LcOcwAhckn8RYaZ4QpB7RdrD0BboC34w3h7RBaZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bf21c6839.mp4?token=SqwtgOI7nDnuqKZkKWW93DjmasXLW4NV5J98EKM8pncILNEitQEakzEYLvIa34h3luOoapr5prVPsnry7CWCMFq_5ub_Z9LLhYhaUir8S4SF_7mVblrDcG-r6Xbwz5n-dyPRlCi-Dw0nN6xY-RO0VQC1v0a-C41i3jgTuKm9GUZOoGL0tO2X3W0BIfGsQMd0yD-O1KLU5wqsZx0G0QtfpIe9OewJggLm7jX7W9He_9VaHFyaH7ht5CVNU9Vh5_AOOXNLoKLm4-PrB5LO3paT_fLc_DDGI-suBRnRtaGiOEvnp6LcOcwAhckn8RYaZ4QpB7RdrD0BboC34w3h7RBaZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
بازیکن تیم‌ملی والیبال ترکیه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/Futball180TV/90199" target="_blank">📅 21:43 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90197">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028fa17067.mp4?token=ZuVemcA_PO8XP5nm_tHr_DQhEntVtLtDUq82vc_PlHV6xYO4BZF9Xi1phal1oT1Q_jBKeaW2s7HKNQk3a93hMuMpqoxsZmqY4eIThPGnEuwTAAVBpIPS_JHH7qEXsNScGMuWdMdrUlLuYJazkBpUX1h7YdCZJN1ojeEVsn2ZJpkDuzkKmv1JTA_KkyPrhpY09lRcQ1qVjVHGa5t2VYmuB9GDvlFlDY1EFjvqCJnW2LZS4ocPwMJpp93IYJZfp0hWltf_OEvKGTBCNzFWdMBV-ZyGwo0X4cs3MFBeLrIJK0YLVijCyW5zeoWcOuqnji80oR1drtAzuOTznUrfTuNqew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028fa17067.mp4?token=ZuVemcA_PO8XP5nm_tHr_DQhEntVtLtDUq82vc_PlHV6xYO4BZF9Xi1phal1oT1Q_jBKeaW2s7HKNQk3a93hMuMpqoxsZmqY4eIThPGnEuwTAAVBpIPS_JHH7qEXsNScGMuWdMdrUlLuYJazkBpUX1h7YdCZJN1ojeEVsn2ZJpkDuzkKmv1JTA_KkyPrhpY09lRcQ1qVjVHGa5t2VYmuB9GDvlFlDY1EFjvqCJnW2LZS4ocPwMJpp93IYJZfp0hWltf_OEvKGTBCNzFWdMBV-ZyGwo0X4cs3MFBeLrIJK0YLVijCyW5zeoWcOuqnji80oR1drtAzuOTznUrfTuNqew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و دیشب آخرین بازیِ دنی کارواخال با پیراهن رئال مادرید بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/Futball180TV/90197" target="_blank">📅 20:05 · 03 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-90194">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=e72OhPLcLVBwHhgRwLUWOugMr5UZzEtFNaf5b75gNFxCknywWp2CuvXGz4WyxK4mTrjIQ5kYp5ed_SP7y_Lmxdy8Gc1RmGGR3svhnHskJxIDJCCV39-1aZTum9e8hRynCrpGT54nCbDjanAzd3JeFz8zkWVCye40uZUa1YfjCgFjhKY4y0VjmpoX-wwchMRTLQnuOpbFU4dzzrVgKKtqYTjvdpuQghLTtCNLzophBsUByTmILOKVmr_vm79I46WNYco19B3BcbLw2eKBMAbToxBHtsmo4s2AIzZBTekI0xjk463xHBz5XtPbhMyyY3xe4gpo30fbEhTpCjdsVPEi1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d995db72.mp4?token=e72OhPLcLVBwHhgRwLUWOugMr5UZzEtFNaf5b75gNFxCknywWp2CuvXGz4WyxK4mTrjIQ5kYp5ed_SP7y_Lmxdy8Gc1RmGGR3svhnHskJxIDJCCV39-1aZTum9e8hRynCrpGT54nCbDjanAzd3JeFz8zkWVCye40uZUa1YfjCgFjhKY4y0VjmpoX-wwchMRTLQnuOpbFU4dzzrVgKKtqYTjvdpuQghLTtCNLzophBsUByTmILOKVmr_vm79I46WNYco19B3BcbLw2eKBMAbToxBHtsmo4s2AIzZBTekI0xjk463xHBz5XtPbhMyyY3xe4gpo30fbEhTpCjdsVPEi1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بهناز شفیعی :«می‌گفتم ناصرخان یک کم کلاس بگذار و با زنگ اول تلفن را جواب نده اما ناصر قبول نمی‌کرد!»
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/Futball180TV/90194" target="_blank">📅 19:47 · 03 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
