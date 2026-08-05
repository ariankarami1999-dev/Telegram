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
<img src="https://cdn5.telesco.pe/file/iTBzodE_UCx794G3vGbEbUCKZIZSVFLA0j0AHhZq8l4mOts-zDCa-Qq1pMB_hKWwAmIswISzzkha4X57htRvf3lyytkH4UgnZQDXkDEml35A9JrfHtem5bM5vIX33sAw67DSHSO1CHlXCxC0Y-JSTVmThfvC5O8G5gjRgc__W_iDL1irWry24y7L6va47caScFBjUnoX4sGnsP228kTK7P5AlCrbT5uqgF7MNgiZR9AHdMLtzo1F4U5ByUG1hSZVHJMRMy8kdv0QFy7l6NzxLuKkIOhIkVFbQHO-r_QvZs321DES5hX0dxPSfrpUHT1kcOvPTYBMr0m_67uD13Tq1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 493K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-14 21:31:18</div>
<hr>

<div class="tg-post" id="msg-102805">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tvHirn6fUa7Y_wJyv1gGcRh8av2JKBn_MIsnUlQtU8oxncF8s2U4O8yV4PHEqt0sUkYk13U46BG5j4TAXCtFi602dkiEgeiz2vuE88dm4-vo7LZSGYLbEtWdUmHwrJhvIfitr8VR3AxPj8UHMp-pTCzsCHiq3_Ea4N7G4zZnDatQ77I6H7Cj1WuNQKjffO06E3Z6sSDs3A5IEoHbNGfn651q_hbAmtr-wMJ3MnNBm23R3ZbRDfLuhN0Nn0MqS6kTjrHogDgJ-OK2Mn1Ef4KXaPvA2BojUJ9vERxbAvIeHE49yG5SUF4J7B3k8K-n8qxHKWmxxHgLi96gmSClJmVfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
رومانو: ژوزه‌مورینیو شخصا در پرونده تمدید قرارداد وینیسیوس جونیور وارد عمل شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/Futball180TV/102805" target="_blank">📅 21:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETCNBPUc-WD5DG1hU8mdFnqqFss5MzjbSxibxWVMbiZTDA_A9i9tJJ0p1mLGD_bOy1IHDd4qknEK9WeYfO8t1EHJIQS4WWu-tku2oBcUQrGbY9hWYWno_REAueYSDp0i8R6tNaxjXkxPBQOWrz_JSLkrtNnwJZs3UpbUYWWGwYHW7jqjhTXB8HkLxnHFvGBdavJ31WsQnbvjDPSd9UXtjdNg1T9w_8xH2a_rEZA8ho1_4wJJ_1q3X8dXd8_MZWfX1FLRUFKrvlwUPrELSE3kIwltwQ_b8F3azhg-abBBLQgI5YHwJpzKaN-fl9lMJeAwVxUbDNhFwi56Rpe1t-Unmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
کوکوریا و بانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/Futball180TV/102804" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102803">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCduLpiQbvJRhW2eTS1-mxX2MzKQ73X6ZBEY2ZGQXJ0CkQsd4f5IRJBZnnzZSBU_Ae2NjDNfvibqR4Z_WT8ngmjw_Ju72PjXwf0dlDDDU23siGsr_q9dp9ChTFmiC8pa77jXt7wJoGQmzXnOD9rDzSo0Rx9mN6xfr6tixhVjnHlOimzXaWksJjy6HrYYZVayMcHarnFo3qM7tA4RQvNXw1tii18I4nSQI6PeXuLXMglI7_oj8AsIjuqbvQSsrDcdjePv37ILkwJh7AmHmNx9_Rcop_cUhKXgVdQZ1-P4k4LeK6w80_7Pk_xtTXPjwU_avA2KOTffG7SGEuWwhM9uwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
تاریخ
مرحله گروهی لیگ قهرمانان اروپا:
هفته اول: 8 تا 10 سپتامبر 2026
هفته دوم: 13/14 اکتبر 2026
هفته سوم: 20/21 اکتبر 2026
هفته چهارم: 3/4 نوامبر 2026
هفته پنجم: 24/25 نوامبر 2026
هفته ششم: 8/9 دسامبر 2026
هفته هفتم: 19/20 ژانویه 2027
هفته هشتم: 27 ژانویه 2027
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/Futball180TV/102803" target="_blank">📅 20:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102802">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/My7Tae5s9W3MhluxVUAra9BGYJC5m2g4hR1oUeHRQLTQ93MA7YqfFk0QAgpmduRDJuk89U1AaBVzmYeSKRysJ2yBkA0p4fcwM4Y-6WyeCRn1RdTFFzhFnY2WLH3jSuAGVptGYoYYzTYz1a1-9BXmD-fA9uhcTWZqHOMEUilHO9a0xJBwwJ45hjq8dBpnD2b8SdOjcwQm6cr0K6CLLpbRQjco98Kzh0U-zUxkFwJ2yo9KSTs5CAr9PzfD53M__2ySHqoV0Xa2DAW6kmxdCXF6CMvIgkIziVmprkOOYx7MCsC6DVD-Rk43srHxn8b0NRsJK-IKrX-fj5qY29u-_FgMjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
🇲🇦
جیانی اینفانتینو به مراکش پیشنهاد داد که در صورت حمایت این کشور برای ابقای او به عنوان رئیس فدراسیون بین‌المللی فوتبال (فیفا)، میزبان فینال جام جهانی 2030 باشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/Futball180TV/102802" target="_blank">📅 20:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=abFWD9rULuGBgl3KHQGvUR-aHwMagot2IbrsPKMI2fSRadO0Cj4n7SNBr0Kqx8kgmhnpxvUz9uHLq3Enrrf1CeinNTPr_n3ygEmZiKTGFeqqxeEtpHNIgeCvMY8bbfmkOTUEM6BaNdgPgRatfpEKQJQPG4QG3z53-pBvV3Ct2IgRES-ST7o37dkAGUTZZ8cXlBDZQxtv_eAxIkzqVi-Z3FyDJjtCK1S64Dvxn7HR1gwJVFQ18TZLU0nc2YpUGRypyJHN27mV9a9K1uSeQKbrpMJd_2ZXJEUwoggqr6TJRtjLRnyUO2iIuUcbyQW_1QYp6UmobAF-VBNBK1nDod7JYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e865a76e80.mp4?token=abFWD9rULuGBgl3KHQGvUR-aHwMagot2IbrsPKMI2fSRadO0Cj4n7SNBr0Kqx8kgmhnpxvUz9uHLq3Enrrf1CeinNTPr_n3ygEmZiKTGFeqqxeEtpHNIgeCvMY8bbfmkOTUEM6BaNdgPgRatfpEKQJQPG4QG3z53-pBvV3Ct2IgRES-ST7o37dkAGUTZZ8cXlBDZQxtv_eAxIkzqVi-Z3FyDJjtCK1S64Dvxn7HR1gwJVFQ18TZLU0nc2YpUGRypyJHN27mV9a9K1uSeQKbrpMJd_2ZXJEUwoggqr6TJRtjLRnyUO2iIuUcbyQW_1QYp6UmobAF-VBNBK1nDod7JYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">8/5/2021
💔
🇪🇸
🗓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/102801" target="_blank">📅 20:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn4MYVcUer6hFSA_1APDFjTYj_8Co2gpgkxmtLast69jAO7vYPTQ5EEDA8eoQ1b0cva6innlF6d4QH-M160-_idYf1GVuNOpNaKl0UBl175HCjgYl7jk2nCh2RQ0bl1-RnA48s7G1L3q0NuiFxqRV9dlQjKENplPfHc4j8VctFrsemEFGhk771YSvcAE9mtQ2ltKtcXqXO0nAdpg-p0VGrAjKnfgjTuFj42AKdPU_liG_GF5RXTrUSPSs_NjIoSGNPhtD04jOxQb0KQMwFZbqioS-0XL2Oab667foX5FIhcNrLvWu0UgIWf0ejc8JHu2H1cf4Bd-vCtwCZJkxl2hJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
استوری جدید رونالدو در حال صفا و آرامش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/Futball180TV/102800" target="_blank">📅 19:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b7936557.mp4?token=d0tXlzlg626kMjmQr6NNks0AwX8mKn78H0XJJiRskiadlBcVh83LVQiYMrqa_sozVFKdS_hqZyUOPG4APlFwdM2GVzbE2EuAZtMZSAb3BFzKhFpkD7QiCY8CsEMnIAnHOlmVH8k6WIEHXnkQUQIirNk0JbDIGH59LCsVBCZumz7--K3-WPgMN9A0IaxESboz6BZYXC8me21EtrfDeOXUQSjLFFDEsk_jvy3fWem-IwHrjzqulpeTqly47Gt6zr6RCmEBQnVNuDdHrUtN03_AdVRYa9XyBDLTod6fFOzvY9ahMp0jhp9Dn3B8aID66bb1ZOLfAb1YeD45X4QAtxMNZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادمین صفحه رئال‌مادرید بازیکناشو اسکل کرده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102799" target="_blank">📅 19:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKLs9OnZx1-hGG0Gi9cWge_F7mLqLhDSH34ra37a0_6sc5jbz3U18ZzkxMHhROW3teYDg4ZlyDvydga-omGAMVN1_QIOCMCchrVNGlJRoeYsaF81G5aiYL0M-6dGG3IG95R-mOJL54yCNJYFAPZt8E11uATQMAdjtd83-yL3E-mFPg12gqgJfEP2_Nh_ACsxmeyL5OXg42OV7MYuwhkZ3iBnkUaMcS8BXYpt_4PZgo0c-a1B6RoxNxduRAEj2TnSfpp7VhvREVvCO4DiWmXTh-ZPLpOhmaZDvqR_J756q7pO7811mmcdAHzFwTKULLkjJlJvsPealLD8bIguhJSPUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🗞
با اعلام رومانو، مولینا مدافع راست اتلتیکومادرید راهی آا‌س‌رم شد
HERE WE GO
✅
✅
✅
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102798" target="_blank">📅 19:38 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a21bec45c.mp4?token=I-c9M_mbZiz4l5ZXmATRig-FucPPXPxXK3xrcRXjeQBQwKa5sz09UWuXI2cyvgGJjI6T_wBrVh5Ya_C8S4QxzPmL9l0aPtT9AEYwpymfZ8cBoKs4_TpJuorTpqHUkSmvbajQpgPZ1mrEwWirS55Xj3bPE-_zUDQt6BlV1iaVlIX-vJ7l2OEjbg_N2QjSo4_puQU-qA-810Ri5txXivGphI2R2D18vwCumtKW4DSwTneBcHhuVgUEkpvVScK8iuXa2tkgZVAgMYXIvNtRw-UORGjorKWGbp7zDIRxXdQk_qA697Y6NmNkv2eAkQaIpeahMosjfxPzzRPtaySGEnDkAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
⚠️
هشدار، ویدیو حاوی صحنه دلخراش می باشد: صاعقه یک بازیکن فوتبال را در حین مسابقه در تایلند کشت
❌
تلاش‌ها برای احیای او در زمین بی‌نتیجه ماند. به گزارش رسانه‌های محلی، ۱۲ نفر دیگر نیز مجروح شدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102797" target="_blank">📅 19:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq00Y6IF7KhBN2VSulcgs4wYTapBmIo7CqNG6K-gYBNNfWTAjfQ5jEgRNbcHudWa6mdZvnZemrEa5QHU8MZXpw9wm-GtzculHX8eB6NLwqtrhIaeDPDLaG-PJyRg08HhxeYa2j2NvQB797GtO2R2XI8gXlMqG4mAQRw6b8C6z3JBi6Q2sMD1QWPGc9dY0l3ZFP8borr1RiwmKJ56dmJ0iQlEufdfprR5r3gz28bxzJ3HBOcv24no9cLKOgQFzesMvgrov36TlEWpMPLPhN5WWpV33rk7vnhPW9PoR_DZnjClB-rCoavz87VhXJQdzkv2J2xkmgoTHRVxlGCOcJp0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
✅
💥
جزئیات انتقال دیومانده از لایپزیگ به رئال‌مادرید به نقل از فلوریان پلتنبرگ:
🥶
مبلغ اصلی ۱۲۵ میلیون یورو
🫣
مبلغ اصلی با آپشن حدود ۱۳۵ میلیون یورو
✅
۵ درصد از حق فروش به لگانس‌اسپانیا تعلق داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/102796" target="_blank">📅 19:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFYs7hntxT2LOPMUDH7MTtMnW-XjzmGtIx3v3p6Ql7VTx3QZMAkghtaNjGpGcXIWe2uM_HsIRmTXPOziq-J0NjRKoPWNFAf4SN7NzmWIkRC2sqgQsej_Adi3nVysntEPhdAtTHpkxI7iNMuZDRYxxdt_zKLWi0VPWcrYi30T0mdSzYZSDE38csxaArFcVZk4ghB4QNI4Np6qy5SVJvY0ZEvAWyy16fFnBlVdmX9sPLwRiAHJY-D6lIRfivqd78LQC__5Ro0uLZahAAVvju_u2KagYbmVSYYz_Lc5CvI-pX0hDFn71JafPeV_FaV4wYsAtEdWtkBI5SnR3Id3DW0RZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
از اسکای‌اسپورت: وینیسیوس جونیور پس از مذاکرات امروز با رئال‌مادرید شانس بسیار زیادی برای تمدید قراردادش دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/102795" target="_blank">📅 19:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833c1a2554.mp4?token=CVGPqgRGiz66P2WQcD6g8I9CyGBB1o0rXQ5dVn0sC_8x55BtfLCyicDdRM_jypx8tlLyTYzM9Ck6-aIg_urFzjMv86XKqot-7EOGyPHdGVcXoFLIZmu3GBRWd5BUeb3x5xMcDjr4Y24ublMTRv8Am6jXTIF-UmU0O10YpgVnFOikqOr2Ubs5bNWaPFFA166onUTcCK16xfj2D734SytKiiCG_jf1cjT0vZ-XAinPFso0drECoWNiyye1G33Lw5N6VbHX2p1iStqIZqRGT0qA8UPm7DW9-_aht_K4BxvPuoItD68AGeHXFfEc_Zztka9fBnpIWLZy1XYJrW4k9c1idQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
وینیسیوس گذشته خودشو فراموش کرده؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102794" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/Futball180TV/102793" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cX450VxPkNwhbNqhA9xvNBzkJQ9Epz1hfFQfmgKbhuXgsIuIMaUe_r7VT3rvKWQmtG1UXQEuafS6JJlwys6ZdN4Gg3OhIBc7ZS9Xh3i9o3IiUKbvZJZKkGm-bAnP-mbVUPl9-u39jgowWUoKwNiPnlw6wZnoQwrjyN8rUSCuuzlWdps_y-qH5i9sGeYIpQMhOe6S5E2PFQK73tqL3ZWYIVrCY0EGpTpOtGmD0z240AvsIs9lxp33AnLmi4ucBS6LDy_jpcwTbfTotiVdJNwKPYgOz5kP2WAxaCJ6mvMQj_-zRCnW6vdad72_4EI9qtr2MT4U3h-3niY7hyg9PLufIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/Futball180TV/102792" target="_blank">📅 19:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a91c5460c.mp4?token=qbGiWhw6uI9k3D6bdFzvJWJinWBVydL7uyDCsoXvP8HjIWRkvd0MuXE3ekGIJQyJnxFYd964rKgRdSqwB0dHsf0BQV9WIRBujmKD3gw_cHG1vWmXxjVBXlLRg1-EkgM0M-MfXNRh6JSVCR3b1WWdo1UIQ36_JfY8cd0yORAjJ26TjkIbC_06hmFQkLAfj-62l2JNsoqnC4zgmaku3URFbJM8HlGf4xFbsrvC6frcyyJB3MomLNCQAEiaESIW36_9HbNBaEgW98kpsVe_0vO2Tu2ByRxnB2zxfiJUcEnAKH6WAvjXP9PxmsEpmyaSXHeALfobP3ooW9kddj83hSIAPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
⚽️
برادر گارناچو که فوتبال‌بازی‌کردن یادش رفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/Futball180TV/102791" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59768147dc.mp4?token=P6ueERHNiFolUajE3UxcKd4UA8neDCB5TpMmikuFVUuQVGgwEPNlWoKLrWds4DrroZcgisR4otA06pbEMtd7X4WjtGRz2kfLo01k5EDQXQZJQo0E9yMa5I0R9vWnoA275VNn6tUBhhFPGtSbd7aO5DcdDGQBu7Wgex1MK6b4Llr1Zn3GR3IwOZis9bFNgk2flipyhKngehuUoKttr63Qp85aKV2UEv0LYiANJdKpHWmJ2wpouuFSSlxCgJ0kdFTFpeUjGUlqZJzr2SdVslOtAvwhBZmGO8jawGsEf79AVRrQeCQKoYiyPxmegdLQZyGUCJbmnjqlkLVdZCWhRQyvZyoTau1Eli_F5i0uqQlSui9DDZ_tRvGMRdqTQU05wQLZuqxxlaiBxw-X2Bk6GvDjtIlj7jCthUVZBJ8JNcjDMNa4dKi8IuzGKuvMm6PSwnRilmKTCszmkp8ZAZvX6lkVaz1xZa-3TJiFP_ZdksuAHQ2ZckMktPorXLx7PTodBm6YANZ09XrwE1Pn_Pnqvm1IC4wyOqfI2uhrufB49BWxpsSQw_ps7QbdnpJ92WR_v0wlW9x-nbKlHlCs33jjPADo7cBUU7HwzJUPFp3sXfoaGwJsOl6ktqLWLMGf1RVDU6PIs3GONysXA5Tk_edU_HJXyZ6RiAn57ycyGQTpdm7pq8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
روایتی شنیدنی و جذاب از لوکا مودریچ افسانه‌ای
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/102790" target="_blank">📅 18:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/102789" target="_blank">📅 18:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bL0D1clbb_8mHOrPH0a8ohuknTdJNyHGJc5WAoZd7Gl_sF8i0fVRtKDLPqppK-qSyt85z4EGXmcWJRT9VYH1SdQVdrRJ_HRgJDWZJkT9I8nYNvFkMytaejOub25eScTrIAg2cobSW2ezmd39DFGveZ1X1A9Y1RwWhfddxRnmEaZuUox2rAfzFxfawapNz8vpjdi3T_FQhIpv8XlQHbgb_VGmU_VUxu45m2BDumwyMl2nywTmOWnOgzdMoASv7AghCnLAqQSHibuPJ6YNGUACdmM1cfub-cYzBYa04Mht3xciCPzF6Y3i-I2IJ0U4plDYKpRfLZrJ13X2Vo2Nr-Jn8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
دیوید اورنشتین:
🔹
وینیسیوس جونیور برای موندن تو رئال مادرید 28 میلیون یورو درخواست کرده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/102788" target="_blank">📅 18:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UehO3pRaWzYnUFLetJs0EJu1aaDR1q-tIV_DcmKw-vT1wwl259uDXM1yVa3oKs_VSi94wPWj9alBJkfaT8EUulLFeRVMNvJGYEnX5VeX5SCPBYnMN_bMoxlKDnqhsIq8hlQy39kDWTE6vB6YG_no4dj1eJISU_8HdkhL0Nf-d70w2y7jWCArCSHVr0NraH2EQigkHgMdXbDuIip2GkZgGflFYWoKzuxO98dAhcFqe5IjN-D0iHaM0ocay9t8M2m62gSUL5SmyLNjqhQMCZ642QIlHavr2MJMT13kOmCXq1Hi8XbUBKv5bl3ZD7YseDRKE8s9_zsiKILlNn871_RCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لوئیس فیگو:
اینفانتینو همین الان باید کنار بره! رفتار او پست‌ترین، فریبکارانه‌ترین و خودخواهانه‌ترین رفتاریه که تا بحال دیدم، او برای خوشحال کردن رفقاش از هیچ کاری دریغ نمیکنه. ما باید شرافتمندانه زندگی کنیم و به یک قانون متعهد باشیم، فیفا هزاران مشکل داره، اما فقط یه راه‌ برای حلش وجود داره اونم رفتن اینفانتینوعه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/102787" target="_blank">📅 18:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d841566422.mp4?token=dcEgxIzsYM39LHvINabosAk2x3UYAHY07mL03X46zuflDm8bdNokBb2Gc5znRuNuWDsKBXEzVluDKFkMAQWKzpZ_3cTPSRZ_-4R5m3kJ3Uam4A8DctE0oaEjFm1RG9_qe7deRAjCG3VYHn5qfG6MdiNfNFHGTtTDizANe3kN3JnfHETCVVOLmJD8ixS9RBPPUs_V8IT3u-DdrqZMmL8ksYSBy18OlTw1HRNtu_H_hlK06wg2xSP49TURGZH6ucFMsYd5nfp-ctzO5DVE5W3A5SZ5T_ndCYR8e5SI1yQgmJ_8gkGrqoeJMAmQkYrKXhu3Lf6tKwtd8RD7mRK-SFhz-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
سکانس‌های تاریخی ورزش ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/102786" target="_blank">📅 18:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W1Nq2JxWHixCXK2aNhfB92lLbGvy9kW2euu1pt0Lhb-0qCzTJ0UID_yqVLazE8GHumyqeMCm_Ff1fH0OFLTPgoIOX6YKY6TwhpeD_rTonyc0Ji_JPvfXFlimzBu0glq3eMcJiIW8Mn19GrLsCe3LfqctWymCxTNg10Hy-zOx2JPbEfZovk4mSZeKv86T_q-tsdbCPkd0Io5q61d8qWa3d0V5M9kKRPRLWjGqTcFdZCTTbasLV0hODontadOQZNsFhKJxzIXR-EWZtcflWq7DxpHBupfz8NzZ0xwrcjblqlPByF42e-nYzy9IcyyXyZyuEk45Q_PnndQhmlmyWy5bBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنالی اینو داشته باش فعلا تا ببینیم چی پیش میاد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/102785" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
وزارت خزانه‌داری آمریکا: تحریم‌های ۳ نهاد مرتبط با ایران لغو شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/102784" target="_blank">📅 17:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa7464e72.mp4?token=D5a5cgqBko1V6mi-T3Lq3kJwBqfLyx-6U006DlA-MKLkWljQGFggpED-dl2FPvpoEjilPEH_JrG8w5O_v4uzVpMobH1rug1Z3VlwILJe1g8eFpBwiiquNheb482yOzd7fHmzo4YPFBVLMEhekuwgz3KAX7L_L7pQ3PT_y7E4TAApR8zEfw_5TAIFDmG19V7phqIKN80KRXOahvx6H3Ms-FTF6wPZfVgmjX-Xw9DumCFTz953QbyAE9-4_bFJtnzU28yBSqP9DHu62E8WmXQzqvJVQZI0BPsc8teO9193mJiMSRUY3Q5CvFeCOO6hPcclbRSphGA_qwTYmcqBfOGQmwBNyWPG0gdZfEX9k8iGHFL44QkNWfPOWcZLBOdGncs8b1aXogAOGtB9SgT0WEjonpTjkptUTyIOuXAuL5bM8M6BEy_nvtIN09IT5Hj_Oocb3TkejLuOS-c4bBuXqc-EycUrwMMaHgRgn_Wl8h6JSr86NgujY1roimrkghq3emy5m7JvZLJwQuWLj4IPNaneqb3xDmgYVRo_aYy6h1mRwXIPKPBqjeQChBnow8H7ROeZXb9FQAEruxIuXO3SiwgXjvzq6zhq-0bD_GUaHONUyu3isO78SEDWEJFDdwbOVohEVXLdqF7hb1YaOaqWKyOV1A_eXFbVv6fZcVwFUKU6blI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات فری استایل یه دختر خانوم با توپ فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/102783" target="_blank">📅 17:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDYuZCrUU4iVRNhEVRVUiL2_LNpsjScPb2HM_8Lsc2EJliZYQvaqzxAkS-w2uQbPNigajFk_nPJloAT0YWZfF5du1qZuDgC87FcXKja3AQPKpNwgNfuzUFtHGFAfNdlQBP-PgL8ln4Dl9Nkzj4hry5P7lEBp9RIfJfR-GD0mh5zWbRJDeQjwg_EkWKPl--NMAoX_GXeN_ckOg6prkLjNXzv3ESVf38IDr3EmY_U-nwIP9H6H3hFuHR62BA-OJB-W3HO1UsmS1WTzzkWtqncgf15zuUi4FzKzVMDmGT_fSWY5H13XYHb0XGPgWFb-MN-KDwI-iPAW_yFRQ8A1t3HsMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وندا جان دیگه کار از کار گذشته.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/102782" target="_blank">📅 17:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gB_7hsfd60WLtcePNY16yOa5vnMSGMHQJ1xUmz-kLd3JUwQ5t98xbAXaNcESatnRRCmIOIpjGQMMlCWqt2y4PRUTphpYJE6U5Ejt0X4PnA_4vCm_pff9LZz2PsQ8ZZVwLKFvueCm7qGs540DJn5nyw-eEIYR4T39Ugz6JqqT01qWqXD8htnvZL_I2zlRRXO_GYLwU7PZcp5pqPYDoyD-izz6FgP48fVVS97e-EcPyEbjhYlGwkB2cGKdWY67TGrwPP4bUvZnphSjMMnUlfCZntCAFThB8AuNbu0VcQZQMqNODM1htq7a7BwFNlkhe9HXXczrsp6DZ7TPmF-tVrTKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیمار در بارسا
🆚
پاری‌سن ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/102781" target="_blank">📅 17:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvaHtjwurhXGqWimkoaxscL5dWTNHbJpPgIO654ErvthSZrq3CmkDBYDekg5an7uux4WUjTY-gOJIFcqdQ8kg2UYQ7GrP8VW899UBobJqORC_tMAcWMl6mKHcVxHKaBzB4UgV8SPO3SS7NQ0S_l-I1z5gti1o5zRCYaFdhqPMUtUNjk-FtCLEQrelXnwofqMpk8UK1Gzqdk6R_UTQXyUW-cFfW2ATkvyiwgeqIHsT5cfh-yRrXlRXHTC-eOF7KtGGaRVOcSF1muMHf0EVpv17LunOVTzjN9AReYDuwlOmwI8S0ctdrczXZ207uqK01cqeKSPo8jtLSlXa7D7sxp2CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بازیکنای مطرح حاضر در این فصل سوپرلیگ ترکیه:
🇹🇷
ترابزون اسپور: صلاح و اونانا
🇹🇷
بشیکتاش: تروسارد و نوبل
🇹🇷
گالاتاسرای: اوسیمن، گوندوغان و سانه
🇹🇷
فنرباغچه: گرینوود، کانته، آسنسیو، تالیسکا، آکه، اشکرینیار، سمدو، ادرسون و لیواکوویچ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/102780" target="_blank">📅 17:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtSsVisNQdef9zeXkWJa60MBEXmd2XZijj4nIaL4Ewca3XLxC1uydieRVfOtEE9TcnkgrDkhWB4x9ikdlAhegiVctcvAT8A4GeAcnMjAtn6IeIPtnTrDdu8cKD-yIz-VkW8mXDm6pxn6m45TFCADTKxUgVUblvuqtyOP7LmZ0mOjtiWwhmqFfiIZQq7j7po0qwOaHcqnbV5KqYG_VND-Y6h8DN6xogDHBT_XX57RbD4wXgzKV8I0z4Ge3b9FDcG1kXKTW1wi5fS3xtpDR4USg5vyW2hRmX_rxI5pO4AYgt7bjFA_dl3pcm-X9ZoHX-l-zKkKMN1ypgzSGrsuGL338w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
چلسی بازم تو بازی دوستانه باخت؛ این بار مقابل یوونتوس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102779" target="_blank">📅 17:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHjNRJwm8wCM4a1SFwjRK-XmEMTTgwaVwff-JAnb_zQ_zj4bwvK5OnG-wgWuJbMquJZtCWZiRU81tL84elnKLQt45ZGq_Jp79JILnpa7Vy7D-MJ1InlImCtUY04o0_tpW0N9A2pnnq2pgXHmZaRsw1Xb9yqGWBX7U4fB6HOrZIaWFKorP5D35d4mIv9eA7CX3TCNusz2ch15kImIxj-KAs7_zoU-vhO3b0XzBeilcUe7wCXGb7e_3vgnfzrbtdahnuTXnM-gdljoHnvvzM52USghUFav-6f9KueMyzxJYB1lQJbz6xZrSfnTg0GxA6xJXt5mydsODPw6NXXc3Zmwcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
چهار خرید رویایی رئال مادرید در سال 2009
:
🇵🇹
کریستیانو رونالدو (94 میلیون یورو)
🇧🇷
ریکاردو کاکا (67 میلیون یورو)
🇪🇸
ژابی آلونسو (40 میلیون یورو)
🇫🇷
کریم بنزما (35 میلیون یورو)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/102778" target="_blank">📅 16:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyVN60snFb_QYS57y-66RMqaoVe1BOOBg9MKvbyOhGZd7lLbZUXNzw2gVuoPgKeryjpqCZlHMmND5B2O9agNhb0S06kiQwDTGE3WIk3_Ey9r6Q48o_aQQighTAkg6pFn2VccYE2VydAuF6o4zAy2KK_KWiaBXk2tYh3zHAkORjjLbRACViaIzLM4UZzZIHAlY9L_vn4DMdUj-peX0zcFWUHdYTznT1kjPM-VWJkfN1ur0BhGEMYKsxGfH4ol4TcyspK2mt0k0YETM-EeA1Rv0QKnbi1mql0XX3eSjFclxwdnbA_uYb_y4lpLo0_Lo1PmZLQ2UAp7Erl2NUlzwuhsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
🇪🇸
بارسلونا قرار است بزودی رقم ۱۳۰ میلیون یورو برای آلوارز به اتلتیکو پیشنهاد دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/102777" target="_blank">📅 16:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=rhGFTFNDxI0Li3XU6aaZ3zriq6nzLuXZ5bgw01f6dJwZuVdtBSg9i2lZoiXPp-a87O6TX20oN-3F9RoUj6SBtGNBzTNV4RrbHdwj2AyAoqvZUuQ3Mu4v6jJ8H0h5nz_iq23SR0CtmjMPa8D-A6D0sCGQysh-aWjH43Eye5EL6WX7lR3OQPzFXTUhh4HWKuYZFJlectlbwzDzxb5di0j3B-pmCdP0xqROY3u-S_f8MIUZh2wI6Sg9QY1zdCJMuVh9rAnF2ibcW1ExQNIFRxLklz1BU5trUuUvf5httBQTX7zoRKyv68g5lBEYz9Pr6GFjanP4VysiLiR_frlxj7Tg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb91a96282.mp4?token=rhGFTFNDxI0Li3XU6aaZ3zriq6nzLuXZ5bgw01f6dJwZuVdtBSg9i2lZoiXPp-a87O6TX20oN-3F9RoUj6SBtGNBzTNV4RrbHdwj2AyAoqvZUuQ3Mu4v6jJ8H0h5nz_iq23SR0CtmjMPa8D-A6D0sCGQysh-aWjH43Eye5EL6WX7lR3OQPzFXTUhh4HWKuYZFJlectlbwzDzxb5di0j3B-pmCdP0xqROY3u-S_f8MIUZh2wI6Sg9QY1zdCJMuVh9rAnF2ibcW1ExQNIFRxLklz1BU5trUuUvf5httBQTX7zoRKyv68g5lBEYz9Pr6GFjanP4VysiLiR_frlxj7Tg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🔥
🔥
🇮🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/102776" target="_blank">📅 16:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/stidUZnm1IMoLxbxrGUf3hUlGi8RcJlyl5bTWHoc5w1iWbS1tkASh_QYXzybCiT9j-vZcAEW2frK6Zjv3Ed_spsyEHERlpD2HVb3JObySvXKbSDz2xYgWCAAz-54HfNKI9VKTtX-GlG4A5l23EH-vJMqzqOVq9RjMuf2JE8h1kqx3qMKDaqICC-nl4GRX074XVexX0g5X5Zlgk8hfQkEGufap116PViTIsTFRXIoPu1d85xVUuWeKDZ6aglEzMuBN-ek9WMC5ipvoH3yVWlMJK7ntaTJG0AC80kNWsGDzfUNNottTq3o-OT6DR2Jb0QG6YJ_V0u3zmtYu9ZS9BtoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VmycOOThZA7XZUqjvHPknI_fZPpgixbF3QuSWBz_98fkh0As54ouXauAtyE8U8RCHjaNHIQ25JFUkE1gIC5ONK1hj7Zec0SClTGt2e1aCqFmQFmXD-TAdjwJz81j1gRyX-xiaafvmQT5_YsjU2reC-Btx4iUNSi-YX9uGeu_TlMgMtyRR_BhV1ajumk71oED6QWNRo0SjCGXDXxsd5hYEMLufs-B2TmHrqeKvmqAPiP01NlcOEC58i5TFpqkkoDZD9taBGG5XuPFF0ZP5SoVNmTvBGfhrGCs-8yZBnJuGf2vWkHlFM7q6MBY_LwnA8e6QTQKee7kEwphn4myg0pLHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HqIggQhirsAcpT-oJ_IEsxm0ZVrGczqN7kCylhi1RaUXVF2Lesbvr5d9yJZKgwky_umOPbab7mHSgCu_0p0jejH8k4YcgXAixbqggHRQeXz1qVrfl4ZKsQSzzE41HFeHjFd17dpBZUq6QVF71LN1jh8RrrzlqwgPksM5nnIx6vwkzE9W6EYW09HloMn1pziM3x3p6YzeeMiZBfLcObcPYdyFQ2c5jv4mMzpACYhV86UAS92qi38RlgMpwCmomwLEC8wZq0Rja8pF97mto6McZGSz6bzPRWp-R_OiXrIVpDPproEQJei0VEnoLc_bH2a2xCUhGBxjCJ9sGlgJmHhUAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به نظرم «کومو» یکی از قشنگ‌ترین تیم‌های دنیاست.
لباسشون، شهرشون، استادیومشون و جوری که مرحله به مرحله و از سطح پایین‌تر ایتالیا رسیدن به سری آ و گرفتن سهمیه اروپا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102773" target="_blank">📅 16:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=uxVuwyiSgmVNKw67AtNNLmCtgYKmk1S2-OrhrWbcfBBP9DG6fqvPZus4dc5oqGyD2M0eps3BL_KxQiZqQxHFWhd0WoLSyj-Wd2iagkaP27C7hmZDwZmWrJwevFl60IFbiKPnmUcUXcuYO8GfABJS1mTlD6ILpBb-hWmY7I15YSFBtG0ve9QMZUkPvkAFG0cZNodls0wnc9Mp7kxU5KLmcIUas8wkn44J70hxiN7ufOuWI9nyJW1ZF7idkFnsb8zDlrY4QFksLVVvTeIDvlL4gj-vrGo8_SvDC4bkLxROpNNTOOXRukS3QSEFBNN6tbB4A0sMAg80mY1EbsFig08Qsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ba5d6f365.mp4?token=uxVuwyiSgmVNKw67AtNNLmCtgYKmk1S2-OrhrWbcfBBP9DG6fqvPZus4dc5oqGyD2M0eps3BL_KxQiZqQxHFWhd0WoLSyj-Wd2iagkaP27C7hmZDwZmWrJwevFl60IFbiKPnmUcUXcuYO8GfABJS1mTlD6ILpBb-hWmY7I15YSFBtG0ve9QMZUkPvkAFG0cZNodls0wnc9Mp7kxU5KLmcIUas8wkn44J70hxiN7ufOuWI9nyJW1ZF7idkFnsb8zDlrY4QFksLVVvTeIDvlL4gj-vrGo8_SvDC4bkLxROpNNTOOXRukS3QSEFBNN6tbB4A0sMAg80mY1EbsFig08Qsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
روزی روزگاری رئال مادرید در بازیای پیش فصل:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102772" target="_blank">📅 16:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qk0Ht8wM6WfATOrXKeCpJZgllY0nKBsd_p4-UvAjZfaIioq1II1DrQQvvJGN2ZACVcLdSGX3bi3z_O_9Wnrho2S6OiEasAuNzgIGLVRTCQH4xyAir9u5LVQ383PwEy6IkTXn3lqJMy79QQ7JVNydMWbY6f0WnbK4tSCS67KZzJmLVu9Sfd1ZJw5vJD-2aFlXlLsYCvOV7KG6lcJb7vpgEqhWvL4o9dBXOZDad72mkmeVDgrpd1dKMZb2FVnISe1BJ3T5Ksqe85fHO_NpYzaTf5za-6yDzYjMEXeBoNtVySz8AUxU7yTtdmUCkz6PM88-GMx5BLfDeIxCc3HqaN6tsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینیسیوس در واکنش به هوادارای رئال که فریاد می‌زدن: "وینی، بمون"، با علامت
👍
بهشون پاسخ داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/102771" target="_blank">📅 15:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0143fadc66.mp4?token=kA4ArFnMQ1xjcTINk57J1f6I8-1ruL9vGicxBNXSwQppyemjlQCEs0noT6zTY13s9bApnC5U0xl9FrlQgMqjg1HKdGAjaQJK7RSXwuZQ-TLtsNQAub_pTBDpXy8N1aHXqRVEXx6dvaofGiNSfGfMt2SyNG7GBYTmvm0iy1tOcIJj3yh0yBFKfD2KjHHoBjfMolXfwaqMZzgoX4j9XEWdnLyEBFzndTiMgPWRWUw3A-BcDZ_yQYS47RTfC4ea2ss6Bvb4yss3D45rsCQkyWxLMc6OszOuK-1JigNnzf1mqylGyP7T6-YQH_G0pF8sIBsBFNNEDOq1Jc5C34XKg8QL8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی نیازی به تست دی‌ان‌ای نیست:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102770" target="_blank">📅 15:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f7f8280c0.mp4?token=ecpluie9P2qKaIjbPJUJiMeq9WLsJay04m7qlMZUHNAmJyfnJ10LkkjsFzuoNc5DstvYducJXVnOAMe2hAUu3c6pctm3OLLJSzMLX6EOYD23kq6oBI6da4cDsoFPq8wQd_Qr9Lw8hwx96c6avyA0ojB5iGoixKcwwb3qAs9APp9XYaUPLWIyrhNek6fwuT6aw2IDy1E01YFM5D4gumk6L5foJCxeNg8At2Z5kR7Kfn2ozdPnBx0lCc0SX8d4sTsi3Fgy7r-TNyBmkjWNeZHBdnMYIYD4W2-Sm23mHBMfwEjvAPiwiykL2FXbq5EJD1XK8Tljn2pnFF-FEd-5ilYsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
ياسين‌چوکو بادیگارد لیونل‌مسی این‌روزها علاوه بر بدنسازی به تمرینات دروازه‌بانی مشغوله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102769" target="_blank">📅 15:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad8597e812.mp4?token=k3CGNPUeck5vDil5gIQkr29ypV5JJsN33jfbFYsvaezIxORGUYVZucYhitGLe9mhW9uDcVbQcFtgiWKvnyBP6f6aS3ymX2O4DlYKPlklqjnGsyaK9XqKi5XFZZMLcbE0fGbBQErKojtVb-WKJLnnLrS4KPMXDV1QzJf2WrQUoOe6y7mgFE5xOnPT6CWI5AH-NMo2GtEpCHdh11rzHTxQK0chRPfQll3YTyF4B-b1J47HoE7Ns0GtxUju5JASi0qLri7KZDu4ic8JzdPrYirprh6Wz2kXdwB6YB8pZZKh64NOZ8oDdm01CfKanBgjaU0nMZ9eiwOUI8yZc_fqEwW-wA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
▶️
#نوستالژی
؛ مروری بر آخرین تیم قهرمان پریمیرلیگ انگلیس لسترسیتی دوست‌داشتنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/102768" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e70775585.mp4?token=WZVXZHT_eKpg6G_BIa1-75MwQbAaqj01ftioMIsXCXLNL5JKWQv2b9RMfUjXEbkQIhm8yP-hjLekigUdjf8Nc58iZt7-rDazq-YQBJ714yTeqHNKzMOAMM8yhJG31Djrc302fhGmaOheZzAqj34r0hBRbTj-xZbJ36L_jKJdImZaYDLNvo-cg1BYyIr3o9LgQf452gnFj8j-0BHwirHOgxLDtY7KyzNYA0tl5I3eENa00tFWKUgU5GGlVofgFYRljMYHAKhXiYb43VfTpUEyV1KQCE4TV2mok0Nye6ogRFr50iXeHpZdc_VWY4JAeSzC764laSQLW7bYDcOyTBu3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
▶️
خیلی از بازیکنای جوون دنبال اینن که سریع‌تر بدَوَن یا تکنیک بیشتری داشته باشن، ولی فوتبال سطح بالا بیشتر از هر چیزی به فکر کردن و تصمیم درست گرفتن توی زمان درست وابسته‌ست.⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102767" target="_blank">📅 14:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ddc5f55ee.mp4?token=mhbbmVJ3yaiT2mbPoUa_Sp8Vf4tGmZHxvm6AxLonaqD_2geVFycbqs248xdQZoxujCuLoJwnSsyQucIlZBbeNWJ0OXBfakdTMNCHYETh4cQuhJxgkIDOL-QrcN2MmZuNieNVJ5v3uaRkkEvXAMp38D2yW4r6BOUR-KfaIMIFBz7nDO5EJY8dxx2TE3a4bwGVDHtRbX_y2mJl4FWLK4mIE1KxWkdAYLoC8I_sq6HaAeavHQLsahZflHYA_7W5VXQF_1Op8q8-iaZy6ZSqo152s3kvIaFdwifAdxDWhqZVVSHnrCes4M3sX41PyWTF-zDMNT9NKgV_h3UkN7cgX2k5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
وقتی میراث فرگوسن نابود می‌شود :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/102766" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWLVSjpY8R-fTH6MeBdDzPG-8uswfQGLKQ8Z0e7TooU3YRSZ1t_Z70XRwZMrdA81nsWn5J3362sgaNHM0dtW1Cv2lH2b3nqg2jAYq1sxCQddG54v1D8y_jlOvzk5L-f8DHYTMbFxbF648C0fZo1oo_XY6jJ7ivIx2xCDx43i8lWDRbxSin-iwp_M_VeUUoVW_O0UokA1TMemUXsnS4k-wicT2CZxfTrin9dDkzUlauX9DCXsIKfhuBBi8o4fvND4HffCQW8RpRuzmCpMLYu8_WTrohFU-nNrT_6kpETk_WmPFFlGBAsiQZ0HmQ9nLda9mhRVoYPbU6LkAUPwimmOLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔴
7 سال پیش تو چنین روزی کینگ هری مگوایر اسطوره فوتبال انگلیس با 80 میلیون پوند به منچستریونایتد پیوست و تبدیل به گرون قیمت ترین مدافع تاریخ شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/102765" target="_blank">📅 13:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctDVQIuEVBf9PpBHSqIwcXZzfdnb5XndiO59QEDaryP165XTkxldn7AlccIjhYiittBsVGpkybOWV6FI2RaswmlSLLaaHVISCRG8eOmf9hnQJtSLLtoM0BwJ9rPiEnJExbzOGAj7vkqhQnVk8qmmIoQvbnmCSkK0Ed9BLOlL9uPWzVWyaC9xu9hDGNnC6_hW51twvfTtaNRKqn8vZPSqXuZgcpJrccjrIk3t46DL_Lis_zuctiVnFayXMQnfqZlfx6Svv13PNSoti_8B52Pi8bzUq97SSX-KkZoQneenbfjk_jT6b5sfhYnmyYJHfURKqAOZBHOpUWepRWWsqllxHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102764" target="_blank">📅 13:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102762">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0EFZeN3xeLeUGJdDzn8tLmoMj1drgpK-Kmu-HXgg6wOePobzMGQhQeuGTNLQEs7J9ksuQB59Nuc8w09uMvCncWDprDvlHI2nKb5v1EQtAYJqa8npeG042epiMzkKiMDxlfSMzOMeW2Xz6eLH7MIUyRLUivA16GFEjkeK3jet328IVExHga83WhzPSb8-nc1xtGKIcyJflf6PgwZDFsHbQygvW7SRoAKsIAFJDoDmBMwIQ1G3VHd-Gy9p4-5G2Xxlpa1do0f27CyTvzBQm6qcrONC1kYubeT_07-8CGSPqirQX61kO7DjO0fi84NNHErIpR8lngkdeQMv0WEhcjT7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جالبه که بدونید فصل گذشته
فران تورس لورد بزرگ ۱۵ بازی پیاپی رو بدون گلزنی پشت سر گذاشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/102762" target="_blank">📅 13:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102761">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a97462a8e8.mp4?token=giqdvrCi45rWauSNLB2Z_AVztO6T0_kov6ve_pr1QvBkwoIpTV4UvgnAZed79y7KgXG8FPmrTwaR_Xdlwz0Es3HVr4tQNEdPMDLvAV85E8Hw8wbkyvDkadPKj_eulK5I-MPorwhT4TC2ZJva7e6be-d0GHp9O_kdDmy0sTwoLIsguLkimgRMEDWlhAva6bzEhof-ht9JkveQ4lFEPslavDUrLVuH_XSn-G3RxzezFpEEQCNeRxwzvxa5hknpeGIH4yKnqQyAInTTIsRXJv2R-qp2XI-xNHMwsy5mKzzu9XkxG9-UsIx9o6TehAS88BMuVLE0MdE6E3LpK1WF8u3vuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
😐
⚠️
ارتش‌روسیه دیروز با پهپاد یه سبزی‌فروش اوکراینی‌رو تار و مار کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102761" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rkYjwiq0J5LPSPOdGRTa26jMTjxNR4AEasVyFHPu5FkvzG0QyhTgaAx0c5y3TiRGi--GIMyy4DcOm7tOrrNMfJzwsFjQntfpWLzF0d0cc4TRfi51cIaxoBevwVWM9G-orfDGvo_GamIxiDkby-hHcT2E98N2eKX9OAsqanW9zwBUhDyUnknzfibflz58WAiDgz6a_owDBcxQrGp-_GzZpvity7wSK-sl3Ai9BFJs02guUSfRShtukk9PtNejvljHXAz2peBawFBGmt8gDlQ9rNSc8kVAz5EHryipIoqnXYEQpuVPqVdXxWQTyEJuWYou_XEeBS7k7xSrW7pFLbgjMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
بازی‌دوستانه؛ ترکیب اینتر مقابل میلان
⏰
✅
ساعت ۱۴:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102760" target="_blank">📅 13:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPujSNbe-ZyZYG-4f6FMpP9RbMWS4xCOXtY_-_pOr6OTJ4iFLyUFPb7vBF1alcX6plDOzA6XfRuAH8qIfrKFgNyEBhrObeCpytarQZOg7y5yKgYS4Svu1OqflenYGLRpqGPQeEMxW1XIq5PUt9YFjgLNtPBqwamVw207kepcWsvS8kXk5H10KHJqVGKG5k3xu82L-LFOIhAjYfFNfDEngWh3QIswAAnsGLnmz1W7kmZVxavxXo0QkTi2dnO_wpvnkXc4ge7bjuZRzoR351SU_8Mc4QVUMULTXCXX3BmLB_nT4zQSGjSeyF20bTy-5ekvk_UUKDPzXZhWXWWesqv_Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
بازی‌دوستانه؛ ترکیب منچسترسیتی مقابل منتخب ستارگان لیگ‌کره‌جنوبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102759" target="_blank">📅 13:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfQTDFqT15Iab5cY22cCWv8Rqz39gGqEniLvnsQwiTH5ZJlV4jEpnlfBxaL8lKrrYVOu7gEc-5h6y71mHYYSGOe3yC6KhtSL7rugBm1oylQ4MdsLglMjjhyco3V5Y5sGYE_F3a1gWA3lwu9mnw69WPWjUb20gN0lQi6Ideinl1cYiJNR2tURQj5Lu6yM9OXfIyeRa5m8HhM9EJqVt4d2mp8iyhSmP8d-HVuo3CWvZikqNwSNNvdDEdl56wa01VNtMEL4pznMpVuGpNKePEjIs6I3twpTSAOo6VbN9h8zjJKro8A9iy5IIPSboLSKOfaNbEX-O5nLm8JFILVvNAGcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇮🇹
متئو مورتو: جاشوآ زیرکزی بازیکن شیاطین‌سرخ در آستانه انتقال به یوونتوس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/102758" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fed5c521c.mp4?token=jiM9kaKS-SbMZj-YuhZDE-qu1qWRANrkYKDgDqOmNWZXleGVTB33ClS8zR0RwnSHyTamMt2QXHH7lz__ZXYOCO2tCQaX2Umg11i8aG3631cI3M7BJndotBUNs-UbAxxAyTXnUehaHqWZ4mIspAfaJzwvQRR0tFmtuoqXfZK_pxGVJq6b8sCCEsQOyh1HDDFFGy04ORozAPnWbCI3epQ3wzkaJLZ_5v1aRXg8Z-WNxZ-8xEeSdDok8uy3L9U0Pstp9Q1N-jB7gWSepR9VwjsrAgKmXDydaDry5PsOjRl3-BflDzZ7NNGl76TKR4F8GnzH06qw7HSAwYIOusZG3nQcEZyGm3TrQ8cxylB72ir_FiaN7AzNAEG9CiwtgR2MELUNLPPS6xdeki3EHM2vZ759-I7s1KFFHmv5bLxa8QbzO53KZ3br5QbS-KxOZ5yk3mRIjJvMCeDxeuuR11m7EMpwujwxvvfxseUhJE_2SzS8hLUEb8xxVDBTM_mcrXLr4pe44OFjsU-fvleoO2U7JMz3geUT6X0Y_EsiD7UR8j0fD0yYh867E2eNxdYJGkLy5Gz15a-ZfPdlWW9cMKJ-dm6ccwUBY0ArJ9ecJIA-eM6FrEnA9R4c72W3XDx9VnUTsWl097DHxAWJ8rfk7AUmOKFo9alE_e0jxD7TQbAapgQeLic" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
⚽️
روایتی از تحقیرآمیز‌ترین گل‌تاریخ‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/102757" target="_blank">📅 13:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d7cbff6ad.mp4?token=EU59GdjGxsj8YiGPmTaukec9NMvYTIqXchca_VBsd10Clc_YeKRn20DWUbl8u0vyPCo3xVEg5UtnDxhkEIgPxBK2HuKV97kQtj05sN6ocdArrx6AaPGw1efyH2o8vGzh5U6FgkDMMavV7xSCKnZfjDcXVTLWNXsMtyj5pOKUE4xZPeuXf37EF-iNhfDU5YRRPW2FOsWyTPW_UcdWdvcVSTSftRy0sibZw45sXx3xXttcgLZnevy4hrYqaFqAh0u4AvM_Bdf3ShejWc-Ti76065JKrfpVJX_Vz70IgB-KCx_AR__KaPIU25McoPc7alPLZ-iy7FcEDqzNseQNUkYX3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
تحول تاکتیکی تماشایی انریکه در پاری‌سن‌ژرمن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102756" target="_blank">📅 12:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c1773cb48.mp4?token=IXhTjpL7yQhDIZI7tkgvpYM_DbKkwKOWYXWPO0-y2pkwruWf9oDlKSmC5ztB48c7NQouqPpPBmFPb_3SQy5ax-E9Us213SCiqxlivYpT1_KypTN9k7l1awwmUHVZg6nx63wjqiFGhYc68UQrozlDp5Bz5M_Zzkoxpop_A9qvrd7SUyW79nKOtP33fFxhTb0sNLrPZqq72oI2Yy4314H9yTXrV2AJBeiNOQuvuTJ-Dvzs3bxYKNbYoGiVR30MA1g52WmD6x_I2-x3Dr7dnmGUJbCJaMjIbMFhJDEmKLQNQHC1rvSsGczV8Uyh6wM_6nO3AndQOCyRs6B4Ccm7Mt0-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇺🇦
آردا توران در تمرینات شاختار اوکراین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102755" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960818b54d.mp4?token=QAJnwp2NXYb4Roii-d1xrjck8tRPiNTXihun35cQfnnpK7ED7FuRsYYeOL1YRnHTNGwKIY56n3IlCsdm0dpvgElJ_wcKZ5xI7gwSwEwC8dUr3ivx8EMPGArem-QbfzRoMYJSF8_eW31p4DY1gydMpHkxtH7FUjj0Z2Cplhj-m0D8OlV2fkvMwQTgnvtj20PBqWeUywMcOCz21ZTLpDzn9pntRRF3KkNcdGJ6qWRn1QNKSCBeBjAeO15mlEmXVjeBDYYo6udnl67go6gJuPfeOFs5-k8OWSD7bEhXvE4QZwaS3gbB5WbpA6VLMan97mXqvwRaFklWYjOM22aRk1WW1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
بنده خدا احسان علیخانی خوب مچ میثاقی رو گرفت قبل اینکه بخواد علیه عادل کودتا کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/102754" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpSa68N18Ni385jC-I9XFsK93hsPVoO9mwOxYwsCdsJC-MSeoQzGi8MIem5yOqlMEo2zTb9daJhEJlQizfQriG22oadLWFh_NbVH39c4i_1AtDeEGMj7lT8_GEbUCIEEfNvjHyCFAgzmQ9kyqfO7l3IzsaynTnHPschNzFFnXkfwP6Pg65ppqpnwqyteBPjQKvIHzrc6AkfSaSUn-uya96pldEhvvapbFkrYdWHxL8vEHwt1lWNK2eFtksyhH_JYZXAuPFkq3GEStZ7j7r-AubdgyfHBq_tM2bVoGEC5jLS8nBWk_LKD6ydRbwn9Z1xu1XPeVRhww730xaFMB142Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
بازگشت دیومانده به کمپ‌تمرینی لایپزیگ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102753" target="_blank">📅 12:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TF7jA_Dri-rABMwaaREtZH4-i-TRJsArb1LcAyrVemQi4VgQ4KDS50D7w2j9gx7DY7avEUd2MRpE-c3Hway-S5ze4O6fydr1pxP4wB-JrM43KXzPiR1E-QvIHlAQD3yx913LLzNlnUURN5NVIi5nl7DQKNvLYwl0xmapMb8SP-GMn1tbUvp3IebrX_oqyQPBwbM92MXihY_VDK6-IhlQ7L8HkGIOFWvNeMpzLsMx3_LBUigR6qLUzCIFhdJme1Y6wFXcnanrZTH6fLZARbuoP5FHvlmHXH86iC2UASshp36_ZXIFbUjEyD3MHVVbL0DJf8dFA_tPtHP7VJddOukMlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
🗞
با اعلام رومانو، ماستانتانو بازیکن رئال‌مادرید با قراردادی قرضی راهی فیورنتینا شد
Here We Go
✅
✅
✅
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/102752" target="_blank">📅 12:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102751">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co_13zn0NENMR1Tj6xFSFyuZkzkUpot-bkeZ23kZtOhp9MtXEMgp54oeeJlQ4sZ6zOi__3VmDdazlCLs3Upmlai01t95wjswAIg4UlOid2SSm6OYXqJTuTqjl81G6XOl6mkkEdED07DpeJwyw75WQ5aa61MHyPLw-RqoRa1qDxafCqmLpCB3j2cgpPDs7fAVwc58AAUPyjboiiyuyvKiew5GCK2kDD-eH5pPAmSg8mmkZ-SqBvbts0GM7vsgJcsVHIOXxhbTURegxNBicxP8FcwltOi753tHN9FNuwGvzMO4XyB6wsKq7dwd8ZhBg-ijJoCdx9eRAGgQZnxW1U7qvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامین رضاییان رسما از استقلال جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/102751" target="_blank">📅 12:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YL5lan6UvaTHgo1s148G7UJZ7HeUmuYA1tNlT3maxCmQRAdrWE46EN-pVroSzxc9LZQ_0UAvvQ13zaqHMlDBGhnRu5nO3SfqigM2Dnf5eTc2iUV5MhIWR0HqdBQh5Rn8ttbwTGqLrIT_B7u9xA2PnHCjZU0yT83KEHbz4In3-ulORI_jcUAcQW83GS50lITXPlwXP9562lTp3J9V3VMimmaBcHUZVdQ-FBQW5EJ92sN5-P-Hy19W-JDT6BgJgE8dFcA6TOy0r0G1mIQQpKjY-4SUcsaGXxw-kLmreS9pl2bvPxGYdYACUuEMdSWVZiFrb0SI9qFm509fkQ_qkHb7uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sii5pMjVrHeo5GNFhB8BXbgQ6gcAdOzMLgquI9_fm4vPxkQB_yRTVfupEcBqHIMxRFkTco0KhhlCnzUc4Bn2-CV-WY6yZQdy4zhz4KO7pwOS-Fd15MBCZWrX8uC7QPtqdqT46U5TmFwExdIAU-SEjiIwhBK3qxVBFpbmvXGLtE2Asb5SM9ECujExdjirIvZ69YfpkDjgnE6h0SQR4nXqHm5g1JCMpZUR-xeJqMJjeaVvUHI6YYgZLO7prYhsrkqiWULVcqVN3wBwKPRKP-k5awzjLxPvntgbTEgtY4KduYWbCuqRFrBxAFXzjkEKaizXI9QmyQR9q6EL3vIQkRVJ4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqYmCAp5ni6ukfeB-94lFL-lnX6QhMIwFY-bcI16UIkweNo42cNc8mlkBbIIeH6oOpuy4OHDYL6r80g0ry2pF8PHvBdbU5Igh0R-z-_24c6yjfbp-FOuYehX8qTi3bnWP9fUFd9939YPmBkvUtV92hCWqGYSmTJIVkXvhJv82N2i3flDzfAX0_9B_bgX6Cnwo69O9Sdi4NX0viu7eqHGe4gXG7HncWkZhBEcVpe1uxPY1ow0jDVGthd6UxO5bHdBbR1V7KtMyWTvlO--vM6HOeb-fGLzc-2yQFX2XvX29by-ZTddef79_OMeqV1OLqnEClS3vBpRiwd74nA1uTdP-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d56wTIX-rWPEewTFbPyxpsXA19ff3_qgosvS5lpmWG9f1WXAXQVdZUJcb4U6wFczREpvJsafVki_7iZRdtWCD1vSfMx467BdEWyLSeY9EmcrnhG1bB4GDFwaIg-PgKTEOu6hZINTZKM8Ob2-VhF-cNLqaknloK4u9f_5Nhs00iexiqzZHTyCdWgDnyvaRF-7h7Kr298Bv3PkPhbEZdcVmO7JyvIE4Fj6Uxc_exQueOxPX_CHIny4pdTHoYwytgtWMEXrdFsXyhT4J4ul4hxwmoNQFcslkntsWN-IFhNN0pIp_we7SnDkBCklt1uziqAP0KYpSVN2qsQLioirpXvKdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
🔺
تیم کومو 7 سال پیش تو دسته چهارم فوتبال ایتالیا بازی میکرد و حالا به لطف نتایج درخشان با سرمربیگری سسک فابرگاس اونا فصل آینده یکی از تیم‌های حاضر تو چمپیونزلیگ هستن.
🔺
جالبه بدونید مجموع ارزش کومو تو ترانسفر مارکت تو فصل 2019/2020، 2.4 میلیون یورو بود و الان به 489 میلیون یورو افزایش یافته
👏
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/102747" target="_blank">📅 12:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=CdPZtuUiHtjcU0Se74MsqTFrN_9wuE4mO240e-zy4xj0o7sm3nF-FR6x5kw73Vdwa59VILu53U8cFbOlsxBlMdWr_J5JXJl0WraqYGRm0nvUMAXj4dZm9W6TrKaarthux-KS-OU17qwjxY1qY7ZFY2QPHz_Hcgs53sb9T7JbGRFF5S31NIo0W9sSTgThIdLL3U2RJ2Q68YabJrmCVph3IM5gZV9eq-Wi74FL5gQIfIa0JXiTXkS9jR8MZzsh4vtECL68poDmRNjg5FGVFdYGMz76onfwbMnfHttkN1RfTiLaW7Bw2v6x6GogAVXWwAzNI6bICSVgBDU25Keng0tdYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c832d40c29.mp4?token=CdPZtuUiHtjcU0Se74MsqTFrN_9wuE4mO240e-zy4xj0o7sm3nF-FR6x5kw73Vdwa59VILu53U8cFbOlsxBlMdWr_J5JXJl0WraqYGRm0nvUMAXj4dZm9W6TrKaarthux-KS-OU17qwjxY1qY7ZFY2QPHz_Hcgs53sb9T7JbGRFF5S31NIo0W9sSTgThIdLL3U2RJ2Q68YabJrmCVph3IM5gZV9eq-Wi74FL5gQIfIa0JXiTXkS9jR8MZzsh4vtECL68poDmRNjg5FGVFdYGMz76onfwbMnfHttkN1RfTiLaW7Bw2v6x6GogAVXWwAzNI6bICSVgBDU25Keng0tdYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
✅
رونمایی رسمی باشگاه ترابزون‌اسپور از صلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102746" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=VanuIwCO30UHezWf-xQQrwbejrr9ei77rH_Ee3Ilgy12RBHi0gKUlBSb8MT9pkPbwuLxpckt9vjW4YV7p3x-cuZWkUOV_M0Ko6HNdZIvB7UodnzPXz-rEuUxeMBmJt5riQzMDQUEdulGadEb6fr_C648fIof2BOYbUHS5xuJlMXZL5F3hQD5KdHYncUz5sfQT2gutGs09iVruVCV48vMWsuLMFzX9oMmhjLo6PT_FA7D6cgR70IMItuM9DtArEycT-1rRAlk86QHPm5WcwYTDOhrcoUMozYJMkbydSwTK1PgOWh4UBZKx9DBA_-OSJrGghsjxysk7LHqioQkd9i-tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ace4b7d7.mp4?token=VanuIwCO30UHezWf-xQQrwbejrr9ei77rH_Ee3Ilgy12RBHi0gKUlBSb8MT9pkPbwuLxpckt9vjW4YV7p3x-cuZWkUOV_M0Ko6HNdZIvB7UodnzPXz-rEuUxeMBmJt5riQzMDQUEdulGadEb6fr_C648fIof2BOYbUHS5xuJlMXZL5F3hQD5KdHYncUz5sfQT2gutGs09iVruVCV48vMWsuLMFzX9oMmhjLo6PT_FA7D6cgR70IMItuM9DtArEycT-1rRAlk86QHPm5WcwYTDOhrcoUMozYJMkbydSwTK1PgOWh4UBZKx9DBA_-OSJrGghsjxysk7LHqioQkd9i-tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این وزن و هیکلش یه حرکتی کرد که واسه نصف بازیکنای لیگ مملکت قفله:)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102745" target="_blank">📅 11:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102744">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcgxfao7r5GzxsxAyi5UWkDSCwxBiPv_X3E4l3kFu10a4GoSHk8weGy0tGyjCCecCWoC2KaiaqohqKN2NYwiIUEvACPbwHHJhKQmJiaFreTSHSD2b1QEpXMLAqv4nvGPe2QqetSQcZpiS5or2Hkv5pykn_NuWcVf4bgRnmAd_v31pNDNp-uaLzFZzi5YmYmfFC6A2C1ymke6xo-MtjBc8O98jNkYH4oteuuDkCMDr9zgErJQJPsgHp-43xt-6Yhl4Hd9TKn_g0RbndtWH79uxsN9MEcVLJdg76RMGS6C6M_XKJdPuSclEyXe_3muzUyPjrrU5k1owFo0TSCZCKknzQos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c80f4ab4.mp4?token=rLtkbUrakU4AZKNshZ5f3RpnB6nArGXUM6FvnzKywDPEctWZXRCRrxBonM_oUCe6GVoqIShNL_2MSYyw7Gdeu8e4sfRmjlMQ6LNXcXHgmYddcwFTN1fe1_a4UT1ProB3-08ej8V-aVCkkw6NDi81WpjdI_kj2uPrScOvEXn_wHvwSoimB83_m1RhMtqeZ9VLqN15L5vIhWbh_d0KiuQIHev83CxN4C85e9HjlrGDMPIsZEApiIyAE7lxN-HCvNDyWfrm6zcrTUNuAYTAfWsouYuzt61PP0rk5nlYG8XqbR54YLHyjfpQZD0TDn8408JKsR4Si1eBucwHe0rhAocWcgxfao7r5GzxsxAyi5UWkDSCwxBiPv_X3E4l3kFu10a4GoSHk8weGy0tGyjCCecCWoC2KaiaqohqKN2NYwiIUEvACPbwHHJhKQmJiaFreTSHSD2b1QEpXMLAqv4nvGPe2QqetSQcZpiS5or2Hkv5pykn_NuWcVf4bgRnmAd_v31pNDNp-uaLzFZzi5YmYmfFC6A2C1ymke6xo-MtjBc8O98jNkYH4oteuuDkCMDr9zgErJQJPsgHp-43xt-6Yhl4Hd9TKn_g0RbndtWH79uxsN9MEcVLJdg76RMGS6C6M_XKJdPuSclEyXe_3muzUyPjrrU5k1owFo0TSCZCKknzQos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
⚽️
⚽️
روزی که لیونل‌مسی به مورینیو در الکلاسیکو درس فوتبال یاد داد و پاسخ تمسخر سرمربی رئال‌مادرید رو با درخشش فوق‌العاده‌ داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/102744" target="_blank">📅 11:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد   HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/102743" target="_blank">📅 10:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5hCqh6hweY2ROIYdQKKh60oRPP5qxThc56eESm1INiJgq3tYeD7oLFTzYVJGD17ihtxZKER3UsUQDHj1IZAwtXJ5U_sxTbg26vdVRS2FaW6hVDYM9s0lQnyw1I2sDJ2vNWFAfEqpgMRLsgMzYKRB3xgKab_OkZU9BuUps-HA17CaWebSQ_s7vo089re3ZnlFmfEKhaVtINzePm-ZfGAqnSEDAZSk_9fadWfB4Gga7aIHT9V6GdItEFEC5FP_XqKG8r5DojRU3SN0lZqmDVsFjGPhKMahiAFNHQbvSl5ZoQnZTgeBq-zqOuntylB_OabGD61_qrubLmMCH7_enpDqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
از رومانو: برونو گیمارش با عقد قراردادی راهی آرسنال شد
HERE WE GO
🔥
🔥
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102742" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=mxXnIw23c4QuXeQy4QSL5SdI-5ChX4SWg5wKNFq00haNrAZVwk4N5l5LvYWXrLNfZNrhAYoToUh_AXYz9r7Qp3avRCYs2aIP7lgVsaQkv4ToGG3ernEdSySxFM3-reCp1dx5DIdnYSIdCxcb8_G341cFWIuNkAGwNNbDRhnIs4K2PohstYwjaR2yCoY48wmO5jPbT_L2vmkC0XOQBaKQolG8p-HPdtsYIZKmn0AR7yUfmasykNjfFqkWeQQAcHlF8lcf1MSbkSZEnd6juGp3GnY3hQd2Uz8F8bC3ZQqmCHBYy8sdNLmEmmwH1xHfAZ-5sbHC7m3B_23Rsr2ZPTckCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f2e64a450.mp4?token=mxXnIw23c4QuXeQy4QSL5SdI-5ChX4SWg5wKNFq00haNrAZVwk4N5l5LvYWXrLNfZNrhAYoToUh_AXYz9r7Qp3avRCYs2aIP7lgVsaQkv4ToGG3ernEdSySxFM3-reCp1dx5DIdnYSIdCxcb8_G341cFWIuNkAGwNNbDRhnIs4K2PohstYwjaR2yCoY48wmO5jPbT_L2vmkC0XOQBaKQolG8p-HPdtsYIZKmn0AR7yUfmasykNjfFqkWeQQAcHlF8lcf1MSbkSZEnd6juGp3GnY3hQd2Uz8F8bC3ZQqmCHBYy8sdNLmEmmwH1xHfAZ-5sbHC7m3B_23Rsr2ZPTckCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
▶️
تیزر دیدنی ترابوزان‌اسپور برای محمدصلاح
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/102741" target="_blank">📅 10:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Op_TosdOOSN4vP8WV__uBjUE-z96cT7J-uZpgKa9_X87Sm2ekc-bYL_0n-SO9fmwIUZHmhzV4dM-blHh7RUm4ecAA1l468z3-ZandS5FrvXCY35Q7s4yWMU-qq_txT7CEwQ0FrGJHvYsEjBHgUkB_Fz4i0GJiZvhnmZJ85FwKe0abe2TKNT6t7hYn3B9bIiXv11ZNd3qNgFV_tEc1WPBLRPOKTGPppxZ1nPMhKrUyQ7jqHYA4dmiizUJdz5K6MQ1T_hzAqmvyr-NCPQFcAUXKCisoKPbcglosVYFBbzBsuS2ER2ndw8lliF0LjH6h1lklQMaDiimnivKUsMKGmKdIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ وینیسیوس و وکلاش برای مذاکره با رئال‌مادرید وارد کمپ این تیم شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/102740" target="_blank">📅 10:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=gJVLkwOhndoFKZnDa_5Mve5NGebeH_RFb7Zs80fBUBAt6ZZzdoTnyGfOE3mdMUVQSG8Gy8zYMusxoNSZPvxdU4IkPK67bebTWTZ3HbUrhQHODDkGml83YoBySL9Ir1e69a5bWkvTxFyQmONlaa-2lxkVJHtAGIO8D93LjwMo9VhNjCRn9Y5gHlWFf3lCPKhad9QdxifvxuWev_zKjP4cZPE47BT02lefRdXaThtSu5jNHaf6jvGlMeRNuvWBwpJV1Q9UUvuHEanFrgOrPKlSs2atD_cMKHd6XVONKAU7Q3rcS4e4-bwrgbsN5KQL7TNd1_AUugf3CLL1Cj9se3f0c6AXZ-im2fcfja2midlPlXRqQxjuZBfr_CDOBY6Do8bH8UrrrriEBoDj0-evHx1jQHTnW6G0t0z1iN61cd5OzbbcQUqI8RdkxLXiiNp-s6On-3tbT1FuRlgK31lG2IslTuiwp-un2ZoUbYxvNsRu9y8UOqhJFP7Eih7k4MII7ZICjmNvnlJ1XOVLXcGXGco2P2QM1mOSOF1GyACkbWF6sQnABHopmeyu_OUVA2DEXGSRJJkJymRu2hBifKn90y2MQXZ6gi7Avmkk5WoT7OIyfz8PfKo1lmLrFUQNP6jJRa-Nx9YWHUm_ZPrBbr4v7fZLt16T1Exlxz03bzzqzfLkbnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d431d3ca7.mp4?token=gJVLkwOhndoFKZnDa_5Mve5NGebeH_RFb7Zs80fBUBAt6ZZzdoTnyGfOE3mdMUVQSG8Gy8zYMusxoNSZPvxdU4IkPK67bebTWTZ3HbUrhQHODDkGml83YoBySL9Ir1e69a5bWkvTxFyQmONlaa-2lxkVJHtAGIO8D93LjwMo9VhNjCRn9Y5gHlWFf3lCPKhad9QdxifvxuWev_zKjP4cZPE47BT02lefRdXaThtSu5jNHaf6jvGlMeRNuvWBwpJV1Q9UUvuHEanFrgOrPKlSs2atD_cMKHd6XVONKAU7Q3rcS4e4-bwrgbsN5KQL7TNd1_AUugf3CLL1Cj9se3f0c6AXZ-im2fcfja2midlPlXRqQxjuZBfr_CDOBY6Do8bH8UrrrriEBoDj0-evHx1jQHTnW6G0t0z1iN61cd5OzbbcQUqI8RdkxLXiiNp-s6On-3tbT1FuRlgK31lG2IslTuiwp-un2ZoUbYxvNsRu9y8UOqhJFP7Eih7k4MII7ZICjmNvnlJ1XOVLXcGXGco2P2QM1mOSOF1GyACkbWF6sQnABHopmeyu_OUVA2DEXGSRJJkJymRu2hBifKn90y2MQXZ6gi7Avmkk5WoT7OIyfz8PfKo1lmLrFUQNP6jJRa-Nx9YWHUm_ZPrBbr4v7fZLt16T1Exlxz03bzzqzfLkbnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
نیمار دیشب اینجوری بعد برد تیمش برای هواداران رقیب کری خوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/102739" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/102738" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/102738" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiIFWRS_ucmlZTnd_BK3z6FkYViJ0tpPApsAEQOdQIlB9olxF71xhRFp5rRmXPNGgOEdwF5I-Sp1zLCGC-29dFGi2FUnIa1reYcRAJsq-kY1qpcuIqU3uA_05Bm858YSkLBOIFtyzxv2q_pltzLHFDGOtLkp8IIgjSbK1X21XNvijAq7Aww7hmY6FzWQ6MtL9iQvm-0WgtEmEXia67h9NT3jm77dZ0zm9sSTdY5hRTEeDKjxj85fLdOLGX7qYtnBeAIfzUXyKqBYiCI3F5hTOnu8khIhFXKbpNWMhMaUbRvpknUarKqlMGokbow1kvBljqN9_UzeXVKVbRrXoRs8Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/102737" target="_blank">📅 10:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6bf58ac0.mp4?token=f9Z97pxi2IRzkSA5GZwTg4nOz05FsNl-AIWEdcigzVRtaPUwXi_ZUubQVPaUS2sDpKF0dVfMP1Qzt2tEV2JZN26QhjzA_4I5XzhHURzLDS7JEkYcrVnHs3xn52QrH6DOkJrzHyLGhK_hj7XWbGRfJTy8AsNQFHsdBK-mspHuwuSBD6gFzMhZ7NnmkHWM6uLXwImw9r8UjJSGl1xLpQJ99UZdC7arK0Sn3LuH_Z99XKD9qgJXcTgE8M_aoa-CKGcvFmcJPTJLEUQvTiBbef7fdIjVHiqiWA3JqIcR61sjJKR8S_WcNJA05BgYRgrGP8LWVFdV8ptqR63UoFQQhxkCJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🪄
🔥
نیمار در بازی دیشب سانتوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/102736" target="_blank">📅 10:16 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102735">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a45508d652.mp4?token=KlSd1liEyUVi0x23tWZxUiKNTBN8Fk9r3LkAWThTrIlFjokfRSdkSyoOEZAqLa0DlleHVe6fz7xWCRBAkNl-I7kA-Dh3iEEhufdJb1EWhBw6hEjyAg1rP7knuBeGGKZqEjhaISvQX0fD2YljveSNghiyaq8h4w267vaXtJRhSYFUffoqUIKPs-9ECAEFCpJtYa1FdxLhCHWXX36pghe2aQi4bbRNtiMZIRyo7nITYOYXR62gFw6mKreCh00FjcNvunobbISCCypf7HOm-bTfKFWHBqF9A67Ae-vovOO1I04Ohk4E-rDouFMdTDurUJ1ER1gy5b-yoAHed83DFRMcMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a45508d652.mp4?token=KlSd1liEyUVi0x23tWZxUiKNTBN8Fk9r3LkAWThTrIlFjokfRSdkSyoOEZAqLa0DlleHVe6fz7xWCRBAkNl-I7kA-Dh3iEEhufdJb1EWhBw6hEjyAg1rP7knuBeGGKZqEjhaISvQX0fD2YljveSNghiyaq8h4w267vaXtJRhSYFUffoqUIKPs-9ECAEFCpJtYa1FdxLhCHWXX36pghe2aQi4bbRNtiMZIRyo7nITYOYXR62gFw6mKreCh00FjcNvunobbISCCypf7HOm-bTfKFWHBqF9A67Ae-vovOO1I04Ohk4E-rDouFMdTDurUJ1ER1gy5b-yoAHed83DFRMcMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین گل مدنظر شما چیه؟
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/102735" target="_blank">📅 09:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoGnn8NROYxZqJSTgql6ZIql_xwGCfglwHJLZBXuXsldhDYQa3Zf2Eo5yCfj16-mzGUdofMel3gHIEmXfwzZtMo9SbNNsY7e9JwTfV9MAYRAvjqcV7f-x4ofadHK9V6pX-75o75BHlfYnkR6uz5vlK3wLyqC42qyW9WrEDwFafo3f2W6F6moZyybKwOLCwQ6qmfy8f21fJ3AaWusXZfeJ1FK3GwTsm_e5bVpcoCMPCMtBHam0_XIIu1whzhOotLFYbTcRio-H1wMdvE9uuqcpv_wwAMqYDu8y8GJ7RNc4H4KMsYX3NmWtovt1dx7WI-tcUYVclGmxF6qE4xx7heoiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
🗓
روزشمار آغاز رقابت‌های فوتبال اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/102734" target="_blank">📅 09:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxufuNJABn1DBT1eUUCKXIyYAeHGfogS0O4AvVE3ITqqc3GNiXdeZ456MohfCKCg7TXhxFdxi6aubmEfi_gF3TzgCFMgCzwSFG6ellHro4xq8FA1Zd6Hg_2wgl1p4YxUDYpu4e3ZB2vwrV6loj4ELfBNmMx9mdR-MjL0acIlFdOgejqFbPFuAfatzkh7qBuXCaYJdUFbUPhODyyoURLsXfXKAScxMGUBnNCCdzUJFE0VoYs3eJAFN55E4VYvT433DD9rxQqzFlGammUXTRAovJrWDsfZkKleYQFDkkbpnOPu0Pnc0chuAlY-u2uJZVepemBMBRwDdkCWs-pUljuTWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیم اگه تا الان مونده بود کنار هم شاید یه لسترسیتی پرومکس میشد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/102733" target="_blank">📅 09:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/663702a362.mp4?token=m4nzieRHzOLfFn40DHHwbM33_sZjP6BbJRdCjrLlErsNT8ENHt9nGg9GFGzErv_rGYCv_8nHxP4e6Aeo4D97Egd_Kj4gCBKorCxRG1VtT4VpvfzfaA7JV8nv7KgVeeZacApK-QSrcI3ya0qujxkoLK-MFLSAXKFQf722op_QU2lLD5_yD1cdc0xcQ44AzyTjqxh4AhsZq9XoGWC6DKMo4xQrw9VSliwhDDH56q9mvVdCV4g3LhTPPlhDAqefdx7unQ1wE-p-xGwaQxoHpVKJ_-GW2sIwj4H-MxJ6go1PWZqekzkT7Pxn68mHh8Gx7D1TMDZC6JPsADrF0mrfpu_mKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/663702a362.mp4?token=m4nzieRHzOLfFn40DHHwbM33_sZjP6BbJRdCjrLlErsNT8ENHt9nGg9GFGzErv_rGYCv_8nHxP4e6Aeo4D97Egd_Kj4gCBKorCxRG1VtT4VpvfzfaA7JV8nv7KgVeeZacApK-QSrcI3ya0qujxkoLK-MFLSAXKFQf722op_QU2lLD5_yD1cdc0xcQ44AzyTjqxh4AhsZq9XoGWC6DKMo4xQrw9VSliwhDDH56q9mvVdCV4g3LhTPPlhDAqefdx7unQ1wE-p-xGwaQxoHpVKJ_-GW2sIwj4H-MxJ6go1PWZqekzkT7Pxn68mHh8Gx7D1TMDZC6JPsADrF0mrfpu_mKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
دیماریا: دربی روساریو با حضور مسی خیلی سخت میشه، چون ما همه آدمیم اما اون از یه سیاره دیگه است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/102732" target="_blank">📅 09:01 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCVgVzdUxIVHHnIsG-Ca5Z34i_zK3EgLNsWN4a7T5mF1aR0QRF1oJ0b0qnqJg82x5Toi0ZeJ07NcPf0KwSX-njE2PADI5bLs7o8KQUoanz6yjaGhtbCHBSZjoBfSRREgk2f7ynZn9_bGbGNRTgOs7Pw4HFcLGzAxn2VOxrsqiXBTJndlfwi7RiueDfpVwkLYPcvS9QgNZcel7c4NXbduVf3yORCDhlcRC9FsdtA-OMMYERcDF_wbmkevGmv23u8JWMR0zrlVFmhccUUwTG_7F6seh29gf4g8_buSTyjne29mgrW4Jiil3PRNnLFt6NwwaYi_46MXKh0lyYav7rAg7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
✅
💔
#رسمیییییی
؛ اتحادیه فوتبال اروپا، تعداد کارت‌های زردی که منجر به محرومیت می‌شود را در لیگ قهرمانان اروپا از 3 به 4 افزایش داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102731" target="_blank">📅 01:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ee1TcITiq6jK3AHpRDICiUKKLym8YtDmZMhUDuuelMbrDdEXN62o8RCy57UaTX1B5v-6ynHAEdw8kLTRu6WDlkDnvILE9SzJDdhFZaCTvm0E9Av7WuJpUwYkXuPsLQWKHNqZuPwkUfK3ApnEfjxXdH0zyuiqcxHx2DTSXjfLfcuVMZwoPOtO_IYjg9OZ8XuLYu1nwZZByEK2bTK33MynRpeZRKHthoqc-g2nY7-k2tGL2u5MmaTzcyWO1OrZ6Vqg4LXuYtp6slMpPEGI8EHGAjolWk71QgQRYFsZUGLSfk8fGOw4QYa2lP616ulFVmtI8-wofRE0uMOcdNl2u0_1IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ به نقل از روزنامه SER، جلسه سرنوشت‌ساز رئال‌مادرید با نمایندگان وینیسیوس جونیور فردا چهارشنبه برگزار خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/102730" target="_blank">📅 01:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO3nn0gccqm3LjcMc3S4MfBvN52369glmKnVfguts8hbiQm0oVxx2AmCIh11BmMRxI2pFvWCrisUphlbiHU61WF5l_SKqb-CAJ390EHZIbrMJj61mSdQrTU8bWkyuml8IrbfJr22RK3UMvF0mu5teN_C9_Sp0vhb1kzmGzowGStC-8mR2nvvxi-sFKW-B1rNUbHmI7xKjkTR6X9NoiyQv09R_ukUPq5uqIPO1byxbUb-ppLLvbzSP_5BYnU0xGTMt-1kvUJHOusTXFXc954bnAKr0ATzMCW13YXwmFMFVc7ndTD_4m_BtwX4-YBfgHK6QDstaEqGkjo1OKh-AVrwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
👤
جوادحسین‌نژاد در مراسم رونمایی از کیت‌جدید تیم ماخاچ‌قلعه روسیه حضور یافت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/102729" target="_blank">📅 01:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHbov-j6l8igw2WBeNXjnG3ZZb3njAQ95r_JlJcd14AYxcUycYz0rEGRWT_zWn8fT7yDT7SkuROyr-f79YGqXNANgs0OOtiCa05L7RZXbQ0SvYu7R0Vij8igwiTfY_kwqv1am-kbat6qDQxb0PFVrz2jdoAmnnvhW0XTaZLJypvnzs7-d8ciDWA7v_Cdt2Ldx9xMitkzNk50aO8lz36cjUxncdfEra8YYFzk0bV6oQ37wo9pWG6F7rQB9r5a8uj691jIIcCsaFmBXWtJdshU80m0J9EdrDC1tqVLreDNyi3W3ocYgJseAkZ3j9Y51hObL9tWoEz8BeZEXH3AHXYQSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت انگشتهای دیدا در مراسم تشییع بارزی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/102728" target="_blank">📅 01:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102726">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=HPI7H0ogPJRxrwwpd_ZIxgTo3CpeYQAJa25kIwdl6xyZxDJjXzuCBtV5fYh5TqGBfWzAAHQJfuB_GR67VOYMOyFFmT4Z53UEWcM7c3W8c5IWwEROI3ht98tBtIAmrDGXVISqSThVDlgMBNU63rISpEvZkbFvMHew3Wu2wKQG1_csyZPHLBPGon8kOOLuWqV_yFwKAzvp6z0znQGevBHU_qnifS2blFX_xSCYKGOujqHMQSkTjghW73XLURAuESL4ZN05y5brST0jFHt5lMxhAbgMGJ_93Ajn0TrhZqAPCyjgp9R6EnT6mRhEvbSbtIISU5zBe5dLN5KK60eS8x27nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c707c5bf8.mp4?token=HPI7H0ogPJRxrwwpd_ZIxgTo3CpeYQAJa25kIwdl6xyZxDJjXzuCBtV5fYh5TqGBfWzAAHQJfuB_GR67VOYMOyFFmT4Z53UEWcM7c3W8c5IWwEROI3ht98tBtIAmrDGXVISqSThVDlgMBNU63rISpEvZkbFvMHew3Wu2wKQG1_csyZPHLBPGon8kOOLuWqV_yFwKAzvp6z0znQGevBHU_qnifS2blFX_xSCYKGOujqHMQSkTjghW73XLURAuESL4ZN05y5brST0jFHt5lMxhAbgMGJ_93Ajn0TrhZqAPCyjgp9R6EnT6mRhEvbSbtIISU5zBe5dLN5KK60eS8x27nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
فریادهای مجری کشمیری تلویزیون جمهوری اسلامی درباره تنگه هرمز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/102726" target="_blank">📅 01:00 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102725">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5sdob0uT2l3oIf4o1gRm6dj78uLWm2pQ7AUgRbx_mcod1E9HwOZ74la-qCiHgg-khnLKzeLwiq0esNNYCIrb7UTOTqFzc-pzOLqs1PbOuy2KgKq1mpQ13_NqennXRfjcTsEWZFYJV1PB2s81bZomo_bmGNjIPOKsNB5-tHpGel2hhgb9wYV8HcdgFqITSmxW3wy0ByakxkNbWiCn8B-0vVXeedFLwtARDN7u1WRM2Q87soFW9Z-tZCsE44PAjuNqgOyTA9XEssFxo2I5eFo4ohPDd_4A00S2yGHULgJr8dpLQem0ShNYKfMjrb8kb8dWsVJbo5G-Fc7adpMjW_sHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
باشگاه لیورپول درحال تلاش برای جذب ابراهیم امبایه‌ بازیکن PSG است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/102725" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102724">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
بازگشت ستاره سابق استقلال در آستانه بازگشت دوباره قرار گرررررررفت
💣
💣
💣
💣
https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/102724" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102723">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EWzoBA9AOpOnhR925zQO4REiTLZ5Ley0zXG9VA2BiSfPnv34dTQrnho4zQOfEbqKsmKbLpiD3fYErkttoDAg29xlmZ3eSrDmXILxhzHIhFTetzvRNlqsIzKsiM_6gF7dRsMP__jO9KL1nnjdYnFMeF9vWLblaJPRJbjJpmS-Ea7w64lN-5idIJ-HIXGsnpcQgUY8u-HkkiU-OrDG9X3EA0JUhbXASpV0RLnwptNDzjbNCVv4MhyY-NhcsEU2lkC3AH2PWq1aL9v_UQB1XuG7PsHGoYAa5k-BZ2hLmN238iw2iX55dorzXOalIM9CPYp_6NDWT78hBYjFL3UNCmzB5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازیکن را به استقلال پیشنهاد داده است</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/102723" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102720">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WJJqKecGVEawSijOl-ZwM6WOVP0MvL07eMUO86k_RmLAUijUs1K70YBVJH3LHLzq_rtsslTZn6PSHrebRCDjOh-mqOqI-P6KzM6Z_UxO0mjwVGxozPSUmMUyua5AlnSUAQVvecpncRiZFEmmXWldTUuLXMEjQP7p-u_SvOuePkUgYTiDs0rkxTz4jZ5xLqV4ziOsJN4tMjv0M2YiKYCXh-06eJEqat1aIw4fJgIIoIl6WUdUc6XKOKj1CdxcwZIrPmRKTusRGYP5Aojxs0aAvXrvi02S90I7OK15CnnTw1zokwfBgJwTRiGxJQ8QpptzrRJtY_DwJubq7uH1_PGnag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWcZLOa9Er7LqIXKfTDWcxAaM_OWDT0AKsDbzMLGtxLb9IXMFFdjjG7Nd7f_Ob_TbF921xdAcPO-C4LmZ1uN5syKfX2GjpO2A9stmYTknUFVBOAfrQKfLzUePD9lft5y6M0AH6FiGJ_02UQ79vJR83Vq11H2szVfLE0At1ZvRm5HEpcfHzqBvl2zRylzJR-7sJ0fOxWSEIQV-OlOBPZtRpUR9UTjUz8H1ZyS8MpIvlGRIMlgpcApdAmpH9MV-gbinSACNG464dso5m1rEYoxXlt8Xz8oS-gpxwwjaQg16QGS5yJZUKbk69e8LLBpT9loYZdnnONVgaQH3QqFykNSVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AOafMD4w_Mm1R_LCcc4MTknrU8hSDMvsJNatFzYu9-rsMXXItgCN7XZLu_zJnfK3PsYLR3p5Rz02_9m0kq4ioEpolizHr9KVKdI6yALi9m111XQD_j6et7BWNOmznWHdtkAqMf_jhGI1qDf7CZ14Z57fzRAiCge7YWiLNOriKBWmQKV4sZ2GXe-1Zwc5Moiz4ByOYdyAsLw8jWVwNuOw1Zd5gKGtZpYjcIKiK8ed2ssKXp4GmVz2lsoFMPfSzVx2szeh9rAuq2WGE2EnOmS794J25B7SJMNrO6-MYUGz9hsMEfYpr4F56OmThrUW1i0HS6Ssd92J3lv8YeS48Xg4iA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو اینا رو با کپشن: « اسباب بازی های من » پست کرده
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102720" target="_blank">📅 00:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dF0nstKdNko0Z3YcOd7wM8OKWysFLO_wjKHTEDRldStfhY8OGOXwTEEM_Ew-_nm02UBKq-yhZ0yaOj-evbtmc0WSy5sab05epTSu_smwIunqjgmnY363lfLtVH-5K7UD2AWyLTULE_Iw68Kau19brF7qGsdkc-WfKDQVG8F9hzS9VmBj9AObiOCtrBlo-Op0umdUncD5IjFzdoXV7AbAJEUyUxPNtAjCUrzg0SWfpCjzajqEEGNk2ml3Urj_I6WoIkdDuAoC7lT5Ha-5VdfjZit6cuqa0fkyTeaKsojAGSbpV-oOZX3ItqCEjpe5Fftyi_GhdXvZBgS2zchIV8J__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔵
۵ سال پیش در چنین روزی؛ لیونل‌مسی اسطوره بارسلونا پس از سال‌ها درخشش بدلیل مشکلات مالی کاتالان‌ها از این تیم جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/102719" target="_blank">📅 00:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFJKYqHoGhFo2vtl4Wf5qLXjmSfpCd_7wbwpeQ1clXKqNe2NRmskZmpwv4Iz0RVffu7UYvwz7ElA19QyK0HJ4jxQPbS2hS5X1xs5ywPnn_2tyqUSxqQ0Ruhd-i6xcTpZ6FFHLMy-N8urXnloOcjQLTHaZNwKgVaayA8TNmUdCZjswXzJlb0TdWcja5m_d-XL2awfcn-oifQWl3XmwIqJbpJRiCIITsA-a1Zz3XRDQtP5fdiNcig8KohZeVmlRPj74_eC0stTAn6Kr9Wx1L48h3ncZ8oqh4iewEYMHWw40MigbGNFrdcZH4SLVemyy93EdNhPfvse3fXWUB_m0af-Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇹🇷
فنرباغچه ترکیه بدنبال جذب پاولیدیس مهاجم بنفیکا هست و برای این انتقال باید رقمی بیش از ۵۰ میلیون یورو پیشنهاد بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/102718" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvWys8ZUKbP29kJzO3OaCUd7KzhIRxJzHaClKnd2YG5kb5qGaOrKkXxRA9OOXd9YnX3dDfSxPqoq-T2ZSB27crnrMB4edisWMTBgHb6wd0TwWtI536kDT_NFFXSXpw8SpDxZR2XrTNmR6qSlLr7lQ7VCQtZtP1_wrB-LIyh_m0ed9D53_0Cb9aCCYTYUk9bcMD_0IC9x0y1-sFE0x_MFSm2IklGMeV6m1IGIvtz9-EzyDNieGxFEVPXbg0U6FE6ctNeaMRT4T6Ny0Pesu_Vn-WAjiRN_bHCRGCdT30HkaS2nHKUnDMHXzt1hbanl3lOEaRg7kxZvifohfEkBkhnyyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/102717" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kgyASjJblze21Xx1aph1NiCXOzMcQEOcKbrkgN6Yf38vcveW6I0rzEeTvetTbTd0jLLQ-9pBjwc14zFnTOSL-Y_yqonqE0gFZQ-o1MA8ZCcoUbmje48O0mwmNVIVa8Efy5d9pOyFhqLLvYsIt-LM-G2vRnvxuJFXewuIoTWeNdvnbyF-umwt-3mX0UerY0N4bMMFV3CPkvQ3MXKJEiIWEPs20W_EGmJcENdS5KRm2DRNPmS6dTNy7vcXnb9bUNvaMMqxyLl70yaWSNVXHsmGWTbJaUBin-R4ruHxqrSf4iZauWw_dGNBPYDy8lJkKsbEG1An0dN-ypHqBP_hLxAslA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
جرارد رومرو خبرنگار نزدیک به بارسلونا: امروز تو مادرید دکو با ایجنت آلوارز دیدار داشته. طرفین میخوان هرکاری برای نهایی شدن این قرارداد انجام بدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/102716" target="_blank">📅 23:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEDbJBzUBIY85qpACppFvGw5vrgWe7aBaSsP9N3UXpCRwNg8UktMlldRmP7Sv6YtYXtK17hc4m9KFKhEq7gUYFWfccol07c6KY2080Bw7kYhpCMGbiJ9NaZCeIKnPd312Ft_6ocVnFhL04vJiEgI34Jq_oL9HXS7kYsB17DbXAX2AzIgeTkhLjD2ePxAzwfcNRKnhOBDaFQKkoXuuvOMAGcVl7LVTghK2ncQ4ckrrzTSv-qqwrQuGB2r7bfz9MIpdp9MBjlNkqp4hynLO5EDOEZL-Zq6XdGXEBG9cJMB75o56XW2CmXzqtMbYNdxhrS35Q7XFbxn0hS59Ndi0uWxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
رونالدو و پوستکوگلو تو تمرینات النصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102715" target="_blank">📅 22:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZMxhgJ4kUSi9_MxwsKH9xDS7zryL0NIVxoVOjCqybZENJ_NNF-tPes1l6Tda2KxwCmLS9bJIl1eE7ahFV64Oy_ei9N8W1ZpwibE-r24bH8BlSlXRSTE8ZdGHsqz3wEAIv_cAXW7bslUtJEz2PM2mssV_xSPoJow3L5GXAOLJ5HiKlntCyGIOATy9SPQAaj85pyiSb8i45DIahu0ynIGaW2wnxInzk3omLMBzYzmvapXtQNDUrvHZuaftdGIu6MApbPX-Jqp9C4U_c6AN0hNxAW04VFrhy_5Sfu1uSiw2z1gakU0-NA31v4mc4a6FUOjPeMkrEzUp5RqgrGWKJpcxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/102714" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=Gf8cdc440LuTaY3HdNOhKKp9aHHneS3cSd6GFDA_Kopg3K4U7FalEYNQmpWFtfiizwSEoGxIZUlbxF7ICgCXyAH6noV16eMG8LL9nba79agFrLzG3kV0LlQx7IDrSisBtiga36Sa5hTtSb_6UDUbBLT-R0oEvKYnWjuUwGXzO84PJSW3AQG6R2R9q-VqNvPxnDpSKwmA7kefUXoLlfyBNcSN4OjvKBzsPlR8Com14NZZN-FHsIGHLg1klzx4Qbp8ZnwNggsjYI8rZNerjwLQztMjswUo2DXFAvtmjjVhVH_wUxtmmCDz76UycS8TD8VJHccPWP05Jb-REbDFNcPCvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=Gf8cdc440LuTaY3HdNOhKKp9aHHneS3cSd6GFDA_Kopg3K4U7FalEYNQmpWFtfiizwSEoGxIZUlbxF7ICgCXyAH6noV16eMG8LL9nba79agFrLzG3kV0LlQx7IDrSisBtiga36Sa5hTtSb_6UDUbBLT-R0oEvKYnWjuUwGXzO84PJSW3AQG6R2R9q-VqNvPxnDpSKwmA7kefUXoLlfyBNcSN4OjvKBzsPlR8Com14NZZN-FHsIGHLg1klzx4Qbp8ZnwNggsjYI8rZNerjwLQztMjswUo2DXFAvtmjjVhVH_wUxtmmCDz76UycS8TD8VJHccPWP05Jb-REbDFNcPCvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…..
❌
تصاویر مناسب دیدن برای همه نیست.....
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/102713" target="_blank">📅 21:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gvMH5e3l1iRKrXA7Co6DJtViB1BVYU6RgWPAf3CVzb6JKSmNIDM1a7bsNoWt5bGspHw39DaKutJ_L31WXYTJpdPDhcE3OjxqheoukFlvyr04ZYHZuC-ubJE_K5ahWtxvUt5xBHKew-2ua8JnfU1x1RIP6wbnLvAJzsXPubmoX3mkbpEhkrPCBQJc2KtXXJWf7KsE9zvyd7gVQVceLR-pz0Wkj6BJZ_-eDkTT7X7rJ-hnuojmbYyVJ0CHZuPQP3i7jlpXvk5Qw7qz938lwJSG89kFsuD-NlwmcVxSejPQqsAUbjnet6ioWgl0O_La_qljkNHbXRSpJ7Xrsz01CDdv6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری از پسر تبدیل به مرد شد
😍
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102712" target="_blank">📅 21:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpOCuSo6FUXP5-oXQDbi_fn1k4n_70vUX6ZrpcvOyhpVTMHI7F4W4ereJIZitLx0aG9-0A5hs0tUOZ8fFCiUkQJV6PjlL6VeiwjE0Fdr5pnlobEx3wG4CQ1A1GEwG7O3j1oK_sV8t66jRsd58GDofSN6d6poUUBdqlW9K7xEutlHjaIYRoYZ_DtK3siFwfhVF3MoeCfPEoOPU29W0k3QkNFIkGxhbTm_SmrMRnGIt-oA1lYKzxzPOoBlf8zTtOXpXQDZ7vLyaDd49pWuwckm_GcUV4dnuwrrKA3fcxhc4ma_IKtfC73IlmJwWejrzplMY0hiq8iV7FvcJcZlKVbTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده در 10 فصل اخیر 5 لیگ معتبر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102711" target="_blank">📅 21:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102710">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuYuUvOu20Phah_OYbsa-i1rmX984YsjyAYmjX69CmBXoZuSV2lbgD19xSJEk_N4bAv_DR9Yv6hNBxyTvjSQNneLNqggKOJgOVTxpsQDDPmdmgZsx0Yxvx5QgsnFXwhaW2EVDC-pAqH6zrZ3hd_-xeJ50DbGkizMywxf3qKOUNbj4511lB5pOqDm38ZQ4sjfvvhS2ssfi3XyORqtyA4zloX0RCcbmrHmyz313oKP6uYs7SZsKCIkkdwzkGcO6tcUpFP0r3vzbHQwser4cF46gSvRUKjElvMP5lUqSjFY_tl1FZmGFoakqdFmmSiYIYMAW8n5SWTrFwT-iuNWgdBoxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
رامین‌رضاییان خطاب به مدیران استقلال: دست از اینکه منو بذارید جلو هوادار بردارید. من حرفامو تو زمین میزنم نه فضای مجازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/102710" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X2Yr-N69_Sy_dDrROtIbpnJM8IsQyQM9aQbwIyzUpF_i-m6Pz02s_-ip0jTYgWv4tzHL11P5eSX3VggiUkPBECdjwyvCZ6rx4icTsWtlQ6uv5v9QX8Nna9r7lcx4UQ8Lg_5QLVHgsjlHdAlOaITtNhDfYdbE-8Ltc7YnXfNOFlbaG5x3JWzGSpLHE2TwVXHGsLpITd-zPPheQPfmvihcxMgBAkRP36pDDYKOxT3AGS3Rtcd0EaTK6GUwp19fUMvTAJQ7ENgmVaomWmRb1K6BKy7mkuYX5gW7QSlK0WvIACWPfTZ3o9UevPrmrUirnfMlp5lm6taGTyirYGE_q0PUNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
#فوووووری
؛ محمد صلاح با عقد قراردادی به ترابوزان‌اسپور ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/102709" target="_blank">📅 20:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyyTONgy6okUnT4-ejYqEFrfU9zV-x4t9ukRO3G-8Zf8__AZkM6HT40G8_nJCeFIj3b3P5eWnjTDxjqebJGPYeBg0--gjfsvOGqLict9f0namX77rPI5F98gaV2jCGtdjBTV01FYJCqgGKWg_0ESLv0j7bCCHjkhbPl4bjdOlr-AWiFsJ26flGL0q31GLUw7Qu76Ml4n4CBslxvFaqH2QruolbQXop20SZnoyKqS-AcEwuu7_JDuQQuAAEVvaJgmxruixtqXDZoJKxzj8ILs4ZY_bmo3LatZRiADx4fioUzpmlhRYpDbmgJnvbihnEDUhsiIjJfM58NnHjdDHt50IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CW0qNQQPCcjkqRICiyiUANaZV84UAGFRW91PBM01h2IHZWu1wJg9q43wNQfz98lekAVEXOwEdmupUg3A7nfRU9MsNVBXJG3VUd1AczIoc6vzMKLc9yzMTT8yeGVaEv3F7o62GHhwAE6RklXYI3eNemVmF52acaiMgjjC608xUyUkI9-gUlQCGe4YrhAz9ulJR0QpdBno6aZDiXbb4aV4cugD39Au3N-A0UieCbysmGvcTwAu_SSLYkhKL20EqaL9pnKa4CmsWFDK2fTGJ7cg_rKZ0rf-vKxGUv6bkp_fyz1K1N0JG_M9Mv4AHy1wLh_lPcM-X-oNLprl4da1uGad2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
ویریجینیا:
من اصلا حسودی نمی‌کنم. به نظرم وینی جونیور خیلی هات و سکسیه؛ اتفاقا باید همین‌جوری عکسای بدون پیرهنش رو بذاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/102707" target="_blank">📅 20:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P658d9NOwsNzRpL87j6fNNfg0Wfd7w213zz1F0xb99IIRZZbgalscsqVb8HEZuAC8Rw7b5b0-5e90oI8ixhDQNKA0_gQa-0aeNf-fBsuszQtB_le8d6G2UJmjDKVc87pSmCLnh23a83-CJpj2prOM22qc_-exuAbiPT8OkdRHbHJS7rlMCFfGYHcCDt_8hwXRE4V6s4Fg1g30lbv1GszYnorOTUR2cCHAmlYBW-jl933HysjvEon_5iZs_QA46RXEsrJ-v4uPyYdyqSxz3yU6Djgdqj_tjJerkmnB18htMJI1yrL_Y3150Xi55_peJbR69GS851YXjZLTTzLoXbDyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇹
فووووری از فابریزیو رومانو؛ سیتی به دنبال جذب پدرو نتو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/102706" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102705">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=hWUlEnwq-EJGwxZpLAHAWFYjFjByjy7zUedSIDztkG_bKnBTUtoA3XDq-6uMV4-5EnBf8P3zF2za5PwSf8z6o1CH7meo96eZR-FDnzgZwtq41x7tdFybZsooOOKwM5pNq5rxyaRlPqlVs7zoRSwLntaqELu1SAxhtYZwMRl8Vnhy3PwyTemiEFjwIFoPpWAHQeR3bRMfJ4tBB8AeD5J8UDIKZZ5XC58dnmeVt381AOjroq6B66gIV51eygOVKer5nAJXf2Kl_AUnsfsMillb2dgmusKYFznKPXADHCtRQmpuodZiD-eoHw5Rk06dGZdCTKFCx72k_TViPwDM3p_b9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b139a17c.mp4?token=hWUlEnwq-EJGwxZpLAHAWFYjFjByjy7zUedSIDztkG_bKnBTUtoA3XDq-6uMV4-5EnBf8P3zF2za5PwSf8z6o1CH7meo96eZR-FDnzgZwtq41x7tdFybZsooOOKwM5pNq5rxyaRlPqlVs7zoRSwLntaqELu1SAxhtYZwMRl8Vnhy3PwyTemiEFjwIFoPpWAHQeR3bRMfJ4tBB8AeD5J8UDIKZZ5XC58dnmeVt381AOjroq6B66gIV51eygOVKer5nAJXf2Kl_AUnsfsMillb2dgmusKYFznKPXADHCtRQmpuodZiD-eoHw5Rk06dGZdCTKFCx72k_TViPwDM3p_b9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⚽️
#فوووووری
و
#رسمیییییی
: تریلر جهانباز FC 27 منتشششششر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/102705" target="_blank">📅 19:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRDrV82syJojnc4uVI19HPQiQN5y-Bh7ii-x_kUDjL5iH4u7YCm3y7CmvTUlfedw3GF6SFXxW1xXnA8kb7OaqE1h4-K8SH5aO4joFSohsmH6Y5RY-uiGtGtB0KeMWc2F_6ffew1CNYCBMU6WWKlVPRSqsS7ClTEFQdrhYcKIPg4SyeUYCfrRzJF9gzKQEnOKXhi0qc_0yOGt5WzLDPqcIT1YQR05iL9023mfsnR2c5rIbpQW6VoZQpzBfjeDFBHrRxLrS9AOOTZwHvUHEK4GPZJLnb1u7NPpMaamIcGE49XEDfgnYCCgxM-J_eNDEKDuBPBkw_wx9pdlMn2KjWBvuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
👤
پست جدید خاله جورجینا در تعطیلات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/102704" target="_blank">📅 19:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102702">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZEiuN2D7XxroahGga9azzeOqsjIIEDlu2dqPUA2A96Tv4ACDHIov1Dv352smxN0n0xHbSf-OPZRonsBOJhVByXPzVepcB0_zbjRAY6OVyiKC7uwFgnSisa7JyRqqAjh9rrOE1CWM_4F4-Ctjhfv0uIeQcfw03HLEfk1V5eT9QF3OkU1j-l026emWzGg0y_COAzcZCbMzOPYwapV_E59jnUjsfMxBFNn0piTisvrQUCmedLdYhpOF9bUWeCHNNxQnSwOmJYBbGN2clp917KDRxLe4f3KPInbxhdkhO5rWY_b4vAWu5cMZJoUX7dYsr3rNbX4zxglbkZPiGd_C2FaH0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsqB3C1NNl1CF78ovb4E_2_goNiBQ9CG7OCGDA4rEUXUOf2EQEQKHwXYJK6H4EgK4-JwZkoUIk_VAdACgVDoW-GQ45w_iIiXrSYrL3QdXgvN5RpyIAkU8xSQGeMdJiQt9lOMx38BildbuNRPVYIGrkClvlRu2y-nbdQ_xyvhUJQl0zGh6J1H_50ofMzj9zyV0U-iA-1t80xK_y_SYzSuq6Sf0x3mloiyLOqdEi_JkZrxKsdIh7iO42o8D2mqJ3KahOIMjnV9EkCW3gjAJbOoNd5ZsQ659knlbkckiiEhPB7GMjaQs5dG3JPM6ijokBj9TQDMr1V1nMs3tqjqyMImIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
رونمایی موناکو از کیت سوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/102702" target="_blank">📅 19:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102700">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=ZBPUo-XugvzecOk8BJgUglwjAhZ_oUhhO3mOOztThFLL0s1W9z21pIbgBJ8MX_0jouDN9ZbZdf8nD6PUvN6_YRMEJZdi-2t5TRspkCw_m5BcClH6CdiSQRx0bDHdldptrZu5CxHVpXeIFnWceerBfCHwRxGEH5axYE3xulf5NCx0hQl-ZR_Gt1xFN2v9JyUtFC_5YtFbv7C0vvYa2MRMe-zyhOJU9jms7SbMFtS4eH7JO6Tmls134X2dKestNcBgKPVZeVOA91CqkemCULRqgR9J-lJUSSK_Ignq3Q1LiiE1lsJ27SXtOdYagA_hvw3X2pyLE6LaZ5tvXvp6PgMWQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94b7db1a6b.mp4?token=ZBPUo-XugvzecOk8BJgUglwjAhZ_oUhhO3mOOztThFLL0s1W9z21pIbgBJ8MX_0jouDN9ZbZdf8nD6PUvN6_YRMEJZdi-2t5TRspkCw_m5BcClH6CdiSQRx0bDHdldptrZu5CxHVpXeIFnWceerBfCHwRxGEH5axYE3xulf5NCx0hQl-ZR_Gt1xFN2v9JyUtFC_5YtFbv7C0vvYa2MRMe-zyhOJU9jms7SbMFtS4eH7JO6Tmls134X2dKestNcBgKPVZeVOA91CqkemCULRqgR9J-lJUSSK_Ignq3Q1LiiE1lsJ27SXtOdYagA_hvw3X2pyLE6LaZ5tvXvp6PgMWQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
مطمئنم شکیرا ومپایره مگه میشه آخه تو 50 سالگی اینجوری باشی و با 30 سالگیت فرقی نکنی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/102700" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=KBiEVuE4LY2hAYkf468MEVZK_l4RclIPkvMQ0I4LJfeSCPIz4LNhH0bD3eY1DArY6yrxnJ4lYIbJvB1DecmiQKmXH9oPYNIwRCG7zchJM0dDnMwHgvsVON_o6oLO4HeiXPTzHRfAK8pGfydLx3YcKABu1A3i342HYIaMnMJSpM3ziPjNcfbhJtucmDZlNDE--9ITVPupj7BbXU0n2OA7f2VBtdAI0lk4fXV5VRUwTiyl6Tb-cWYPfMOI901wA1sXzwjIcadtwmzQLzeeTRJmjCTmfuHHcHEsrKNr6Bdrd7M4UsDv_aXkj2EOwW1hWFr_hDEnEIG9jDMYpAsJb6gXqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abd0cef8d4.mp4?token=KBiEVuE4LY2hAYkf468MEVZK_l4RclIPkvMQ0I4LJfeSCPIz4LNhH0bD3eY1DArY6yrxnJ4lYIbJvB1DecmiQKmXH9oPYNIwRCG7zchJM0dDnMwHgvsVON_o6oLO4HeiXPTzHRfAK8pGfydLx3YcKABu1A3i342HYIaMnMJSpM3ziPjNcfbhJtucmDZlNDE--9ITVPupj7BbXU0n2OA7f2VBtdAI0lk4fXV5VRUwTiyl6Tb-cWYPfMOI901wA1sXzwjIcadtwmzQLzeeTRJmjCTmfuHHcHEsrKNr6Bdrd7M4UsDv_aXkj2EOwW1hWFr_hDEnEIG9jDMYpAsJb6gXqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره خنده دار پیمان حسینی از عکس گرفتن با دخترهای بلاروسی
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/102699" target="_blank">📅 19:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FimYgSHFjeAUDtWSiW3A-EurXn1CCe5beC_FBgOR9EiVSDw8Jw3FqFa5pYc63CVEJYNzx7bjW7kNcbU9kLjqQXf9ysButebY5Rr1-C-vNfgFVWZE-0NMAwguPfmDdGOEqjVy4qxM45d3lpFrGSOkqbm4PiweuwWSWZS9baLsHRb4wxxyJR0wu6EwkarjCSbbqsD92qow6jjeOoQvCD5fsUD27E2OLFtgKb5iYz3ZwRNlfbCodA8ydEjE4q3xuvN4gWJWnbgORp52Fn_T029-TIoSwq_lm71pkQ_a_1TdCzK1Y97WjMp__gVQRjUJf8pt_nioIDh43XJNYCgcRdyrjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/102698" target="_blank">📅 19:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQc974oVr4xAtqwP9Gprg863unMBxzUiuzxX-L7Sf8VJCe83Jd3LrkuuaYIzT4CCxz2gs-b8nzSdWIlfwoLBYtNOkNVolWDoHUZvDmsuH52QK5PC0-YLH3xW-fMakgv0On3EndRbIQrCapEWy4CY6OHL0fiNTl7me6WxEF3dw0OHZhc3ix0kPTUsodv8frk7n5TKY2J07VhbkM0WtyLH_DDX1x7GZ1CdxOabsdnwCMfbyXWGoe59vCFk-lSScSMcZlYAYvNoe1ZWaBYUX0Ok6kKvqpt8Fa60vPV2CPOvZ2MJyF3VAWscwdQt0Pt86xVrDveG0W2GQqJevkT1toJ-hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🇹🇷
#فوووووری
از رومانو: ترابوزان‌اسپور ترکیه اولین پیشنهاد رسمی خود به مدت دو فصل را به محمد صلاح ارائه کرده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102697" target="_blank">📅 19:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrY2ALxhyMV6EtE8zJhVrZJnMTdAfCR68yX5k3P42VqSZP2oPa-k2KYPM0X4wlWgwdB0zIVRT8LuZtP9Z3KRIySDJ3Sp3-hHw86hFaar5-rODuL1-FuAF5Uv3ZsME9ZmDKb5hnWzuLbCYM49UnJTRlq570Mx9Iv3mC0hsgq79bXxHrgaXk4p4Tf5aiiK2xuXfqpTOhAsxZlTJKABZglLiwtgb_PKZNvYpYxaMEwNyMlsR2OpC5hiIhF-CqL3yt5WbncfHRE27pM3LDSz7Vo92MWs79_M2sVA_2a3JsNwjQ1bQ3yfkhMkCzrWMm6g8IsfiwwfDXRJKJRvrTBssIbVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#رسمیییییی
؛ علی‌نعمتی با عقد قراردادی به تیم لوسیل قطر پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/102696" target="_blank">📅 19:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b46370582.mp4?token=AbuX4nDLKaf5g5WmlqPl8KKnEoBojV_zkXlnru9NvCoyUO4ZvVe0lRMl03jJevVthMlyeP6DdF-ZsBAmh_eHO2tHa1d9ACVkDNiOQHrKx7jzFjM7NPXrXpMC-0xooMuIRNbevs8NDnOR0H3K2eyoz0lPKeNCTtNpsp2qMOHZT-M6PE9Qy-Dg_0iTP7n56c3i9JnRZxthe3ia2zktPeYW_ZvNIL_27fRWiNgJmm2TgZOlZ6vqoDa4gBGCvI98_PQ5n5JJQRYfzVFOqQEE4IpI4JUQIK_WQzCFPU_DS8ssYvk9-uSMiyY2x7FLc6y_gQpOAzj4v3_vpziOEZanQp-AIgsg7rqFMMNPyr-nwHGaWif0yLcHyVUCF3vDLbA-j0u81hDj1YfpoOZsNN881tbT8rq3mTFUMwfnWKxoc4s68LQg9U3tOhwnjx3n78AyIr2AaeDPoweWR99-OZ8bcFmsYhl-Vf_G822YLPrwfIf0zzcPgl-eHaQ17b-EOlzR9jY9oVyT95b_19kgO3ZHlxm2fN9C3lvUcKU5rfGVbPpkpDDfcs_nb3FncdJKk0rh9FcTOHSELEcwwMGR0Bunqi04S2-b4_rEwuPjjNAnXkGDZWOb-8o6eZtNnq0LQ67IOKQA714sWSudpAXlqrZQbqz1jmq1dkQrb4opWocZh-Al1mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b46370582.mp4?token=AbuX4nDLKaf5g5WmlqPl8KKnEoBojV_zkXlnru9NvCoyUO4ZvVe0lRMl03jJevVthMlyeP6DdF-ZsBAmh_eHO2tHa1d9ACVkDNiOQHrKx7jzFjM7NPXrXpMC-0xooMuIRNbevs8NDnOR0H3K2eyoz0lPKeNCTtNpsp2qMOHZT-M6PE9Qy-Dg_0iTP7n56c3i9JnRZxthe3ia2zktPeYW_ZvNIL_27fRWiNgJmm2TgZOlZ6vqoDa4gBGCvI98_PQ5n5JJQRYfzVFOqQEE4IpI4JUQIK_WQzCFPU_DS8ssYvk9-uSMiyY2x7FLc6y_gQpOAzj4v3_vpziOEZanQp-AIgsg7rqFMMNPyr-nwHGaWif0yLcHyVUCF3vDLbA-j0u81hDj1YfpoOZsNN881tbT8rq3mTFUMwfnWKxoc4s68LQg9U3tOhwnjx3n78AyIr2AaeDPoweWR99-OZ8bcFmsYhl-Vf_G822YLPrwfIf0zzcPgl-eHaQ17b-EOlzR9jY9oVyT95b_19kgO3ZHlxm2fN9C3lvUcKU5rfGVbPpkpDDfcs_nb3FncdJKk0rh9FcTOHSELEcwwMGR0Bunqi04S2-b4_rEwuPjjNAnXkGDZWOb-8o6eZtNnq0LQ67IOKQA714sWSudpAXlqrZQbqz1jmq1dkQrb4opWocZh-Al1mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این خانم باتجربه نکات خوبی رو در مورد دفاع شخصی به خانم ها میگه، حتما ببینید :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/102695" target="_blank">📅 19:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-102694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8tSGgxnyohZD_vP8yLUt7ByFB3LJrPhNQDIB5hUdR03OirUMi_RLvEUYFCxVGmp6fdIHt4s0qx2fLboH9_J4N5P65lELp7DkX5nAwmJ2PTtjn_6jURzExru6m0-l4CIaFvcpACnQQ7vDzL7VZHJsbj9QTtE698-AT1gJ4XGlFIhzvOF1gTrndYJG2IsqXaajAel3O7_C1DQ-IjnZx5RXdc3EOc8tuqQU80XaSpruM9QpPByVAKioevApa2Y2azTTrlBo0vERglQc15HzLAvyQ6OYWhjmGCp64zYyXJhJjU1WUKyuQ9udXLJmLADfjbfstGqVk-ik_4hjVX9MFiPfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی برای حمایت از بازسازی مناطق آسیب‌ دیده در سیرا اوئیسته مادرید، 80 هزار یورو کمک کرد.
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/102694" target="_blank">📅 18:51 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
