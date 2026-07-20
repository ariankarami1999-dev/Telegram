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
<img src="https://cdn5.telesco.pe/file/azStJDTFKUSNZkWUALg_zugCGkUySLRdgeTgKzlE7R8oCOp5WZ1gNsKtQkZYrIAvC94oCQdQLCdVa2QDrnNnvYFtbD1qtrX3DV6sVtRukGsrT3Tuy-Z9XFX4OA0ocfc-2V9x5Qqnht_-NKvErhMHitUpLz7Q1ijfi5fMgQuH8mDqwINJhsbWE9oFv4lEFEwknpsZERVhUUO0pjmrPdVp7v1AoIViCfIIdNjxxlCYaxXsHLpQzaAXomXlyOAaY3HA8abqIfwhYb5lDZ1Kew3TwDLmwHsmCdkrvAVeBbprKtX-dOHXop0g3soItUznqNZUs2TTFZk29Ly7SkxLQgPz7Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 551K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 22:18:40</div>
<hr>

<div class="tg-post" id="msg-101369">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇮🇹
🔴
فابریزیو رومانو:
🔻
منچستر یونایتد این تابستان به مارکوس رشفورد فرصت جدیدی خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 605 · <a href="https://t.me/Futball180TV/101369" target="_blank">📅 22:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101368">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZKjgyi2NKSoWHmq6YyNDzXpQnunLtV8CuK9tyjACdIFvPpDx37Q2rMPgFDGTX6nSS-6DP4wPzRyOiXX3gqAk2qDulF9XhrXSXCwKSVHSuz0_GlfaTR_sBH5bbCIQJr4OXzv5Jnp1q0yml_ExN7ou1OIvSe6daPyqUoEy6FSCMotoFmq1arL-57PnzV08eAO9IQ0jrXb1-ZzJiTymaPzOJccpGSFPLRBIdueY7g8baw7NozBI1z46b6AALLwURuAxNIIqvzW_18zowF-LbykL0LGmHJsG7-07X1O_js-65lR2Zqq6QR-sgSiudprig_IC_b_jTQfrAN_kyfhpQlsoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
فوریییی از فابریزیو رومانو:
رودری آرزو داره که پیراهن رئال مادرید رو بپوشه اما پریز مانع این انتقال شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/Futball180TV/101368" target="_blank">📅 22:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101367">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgdJtRapxOvi5RlcqUHKRxJCSsfXzczx9BLz69JYDUTzkznY3flwszVecSrUQFYaulVlCfeUe6i1LcIZjbrP0Tlz8FnQOF0Nbs3w_6_evFzEP2YE8ppgF0jS1GMjX8A8u6BGVLaVcFybmJVW_4qFC4qhHe2OCb5NaGjPKtZyBz467AV_i712Na_uFqX0JJDkPDyNqHcMEfAIPp-tKU7WQHnVHW94cOU37lT4nFnFXd7rCXVix4CRM-SqfgLCeCV8bGZHZdM6xlSPTNeF-7njTnLTBW2Ia0T8y_NJQrC_p6FbDPlgVPNjhCGB45GRwbqOoZCiqoOoBzbrfpw1GBhdCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دزدی قهرمانانه لامین‌یامال از اسطوره مسی :)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/101367" target="_blank">📅 22:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101366">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e69c82de10.mp4?token=bic7bgUoHREkG-suUVZG6OdvlDcaTtt7Za7SzzxWZTNoT8x4-_cykzU3ttD2_N5-tf5MuLvyVctC_0AvJoEnYXyqJ_j0akEPeNLrsUvbNGXho7C_XQXvjYonEu10WY-InIOldnugYAYvMfDDwh9HLFnhUS39smhxfDl7GyGPEWac6b1ieE6sT7tyQkx6ZIQGvb8PJrx-TWomyVIBxXJlupZUUvrCv_bDs8DU8kQyenegI1ON-KzI6Hsi9O5KctZrn6JqayYZXRzh9ol6kpI4xbKC-iskNxWum6mGGNIx9Q7j6XdKwMStDJGF9Q8c9nnWd9BaOxkYTl8AKEho-QsnZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
کارلس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/Futball180TV/101366" target="_blank">📅 21:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101365">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a26571e61.mp4?token=KDDOJhE2RXYsevbVcsKlyEqbKhhYAykCKkAQZ-xZ3QxZLBltnSWwQSzH1i0i8tIRcqNo6IiR_e01d1r9DYR6zhM35Utx_7a6uukOwHISnkOzKYz6HCsLYjaCee2ZEmcmsaPufLCMt5S9_wrO5GBoQgEcjhRHmCqdjKDL4qbY_D5_G3BvR6EiLLJMxsYLvURKU_gXv3r4FnnQTiykrhVcqNKYRKjODLJ2gb2oNXxsyyF_96NirqCU-jH72C7QjetCuf8D_f7-TUHJAS2xupAtaNRztauCTAMTOO35ygudQrT_4wobl6UHbylBg3qZqCHyA_0ABS56YjKK9iE6QBG6JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
🏆
پرنسس‌های اسپانیا بیشتر از اسطوره رونالدو دستشون به جام‌‌قهرمانی‌جهان خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/101365" target="_blank">📅 21:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101364">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tgOKUuMaKvgGp8HSXCEMpvS24yJ-xzMKrPoMe6AFdlUtiwiddbb5BwdKeggK8lOvk3MPVTQlKsCNEGyutGBORQQifhP1T6xDkYhoP1BKGdP65yHR1yuXj78tZP6Hc6qmH-Dppc78bcgi_KZSSKSPRCm7kbWVQfliU3tq8NkxeoFTfENIPXfo6r7OYYUBqKOmYsznx3pl_kWJI5sCV12bCy4d428mnVi3Mj6woDTrQY1YQC2w1tRRDM0gChyxi6u5xeWbRUJksE1Xna8LQKrfLqtrjIe5RINa-JGAh49GnouIgD7YPsuWx0tYz8KKiR6ZVwMWRf0w6HM7lFCr9VHfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال 2010 خوان کاپدویلا دفاع چپ تیم ملی اسپانیا  قبل از بازی فینال سکه ای در چمن دفن کرد تا کمک کنه اسپانیا قهرمان  جام جهانی بشه.
🔻
شب گذشته به مارک کوکوریا گفت همون کار رو انجام بده چون هر دو دفاع چپن و کوکوریا هم این کار رو انجام داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/101364" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101363">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnTFWPMMD5cYvzye2l3O39VSfLEk_d_iJjZl8_GWrDQUuX9DQ1FoSZ4qq7X50j46BtSKIgQ5Wj8w--MbL6Gja_SUQeRN8polKNmh389gTip7gLQ-RVEbgmtbl4YgGHc5YKYhb54EKBYxnASrP14gi9qOWiyeqZaXF7oSYpJYLvdTmB5Qz4yD6Vt3cKYDIGal2we2mZR22U7PD_ckZTxeMCoxljiDCCGTRr9cx-wlc1k_3BdpODlb6d8DwW86EEOWfhid3xYo6kSFaEvPLcnfKYoIWQ8DlLkoL8Z-ZrRUJ3Axebh4vByLo1fuucJk4GXDvYWZcKd0maBsyI_q8cSLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📸
مسی، اسطوره فوتبال، از طریق صفحه اینستاگرام خود:
🔺
"درد بسیار زیاد است و التیام این زخم زمان می‌برد. اما من تمام چیزهای خوب را نیز به یاد خواهم داشت... مسابقاتی که نتیجه را تغییر دادیم و تمام تلاش خود را به کار گرفتیم، و این خاطرات برای همیشه در ذهن باقی خواهند ماند. با حمایت یک کشور کامل، و در کنار تلاش و زحمات این تیم، ما دوباره به یکی از بهترین‌های جهان تبدیل شدیم.
🔻
امروز، درک آنچه انجام دادیم دشوار است، اما این تیم به فینال دو دوره متوالی جام جهانی رسید.
🔻
از صمیم قلبم، از تمام پیام‌ها و تبریک‌های شما سپاسگزارم. ما بار دیگر به عنوان یک کشور متحد بودیم و در کنار هم، افتخار بزرگی را به خاطر اینکه آرژانتینی هستیم، به اشتراک گذاشتیم.
🔺
همچنین، به اسپانیا بابت قهرمانی تبریک می‌گویم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/101363" target="_blank">📅 21:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101362">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
😔
لیونل‌مسی در بدو ورود به آرژانتین: درد بسیار زیاد روحی را تجربه میکنم. زمان بسیار زیادی باید بگذرد تا درد من التیام یابد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/101362" target="_blank">📅 21:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101361">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqA3iDGDYvQbFLS7xvoAPntReAKEFCGCVVYjY3Q_SOnbRS_GdcdIIFeG9iGdtHjKVXoTGINEDjLjpNtFRJQE1yAuah9TF9f1Zzeht9QCHillw2OTEuqtFYLmpvFCLs_M5_-U-HC3FgKMt3vs5g5foBgD3uJEObCUC_bdMCjje-RQQROwqVcwffzv-nIR8ssm-ndP2lWQowCdk_rSBbprt8x-MwJllEWz4q69hLByBdlQLkHHA2awIM9tgubuAIhhqo_0JYrmCbyPsEQXA6PNtGyl0dakuXhoTgSAU8VGW0WxqUH8727bguAdq8u-eHUMjEZJWemmJv9PGNdZUPE7tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🇪🇸
انتظاری‌که مردم از بازیکنان اسپانیا بعد قولشون درباره قهرمانی دارن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/101361" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101360">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erWEaal7dLZ4wpBv_P1V-7yL3B9fEizht00EJmcN9Qf-6ebRUu6qeRzcGl3n4bh6fPBg5z3QgonftIZOeXvYROhDMJpuS6bY3gLcY4Tv3dj3LvqZYlKhgGterYN4OFvtpjYOBQXXPdiWdtdAzItW6y61XVoQPpeJD7QEjhsbUOTgmM8t94QxtRkLb5Hk3-TaE0hnLwr9qAPjzlwBNJ1KsZZwTyWU7N_jzAmw__mH0TxYIT8lt9dhFYsUY3Obpgwdn7BylhimMW8NRjj-caj-yN6ENjvn1Z2ldaQEfp_vfhGqUBSgsT3YXFexH7ZoRuJFVOzO0xEbHoMmnEeSBZln6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصاحبه قدیمی سرالکس فرگوسن: حمله خوب براتون پیروزی میاره، دفاع خوب براتون جام میاره!
🇪🇸
اسپانیا در جام جهانی:
🇨🇻
کیپ‌ورد - 0 گل خورده
🇸🇦
عربستان - 0 گل خورده
🇺🇾
اروگوئه - 0 گل خورده
🇦🇹
اتریش - 0 گل خورده
🇵🇹
پرتغال - 0 گل خورده
🇧🇪
بلژیک - 1 گل خورده
🇫🇷
فرانسه - 0 گل خورده
🇦🇷
آرژانتین - 0 گل خورده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/101360" target="_blank">📅 21:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101359">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZy9_CW90W9Juie4sBfKEFGdjH-OAYZmF5l1-4n7PLNYOnNp3T65D8aN2Kb-u_YdPj1RoinsxsTdSz3Pqk1Choxk__gyspYDa1b7KrhgOrxaZN66ssdA3Bky7y2m3SRm37jUdDP3ZYpsuBi7cj6Fwcpr6rtRc_UGt2Mpf1dOK0y_hAFhjnvFXUB_LTlrLWAfwjQ3DPtpiTYH4hU5UpXnryYREV30AbZ-H2Qvqo1fsCwRs5d7kPVbq3ii2ytsG4cfVgAM0dtIJkiLQbtu1fJ-6MEuVBdk7V-jx7Orsop9nxj-YDfzSo1brnp_KVxllXXH-utmKAqvY3avncuZl0PPKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
‼️
کریستیانو رونالدو، یک ویدیو از یک شبکه اسپانیایی لایک کرده است که در آن درباره فیفا و آرژانتین صحبت می‌شود:
آرژانتین تیمی بود که باید حدود پنج مسابقه پیش از این از مسابقات حذف می‌شد، اگر کمک‌هایی که از فیفا دریافت کرد، نبود.
و فیفا یکی از فاسدترین سازمان‌ها در جهان است.
به همین دلیل، من اصلاً از آرژانتین نمی‌ترسم، بلکه از اینفانتینو (رئیس فیفا) بسیار می‌ترسم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101359" target="_blank">📅 20:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101358">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/101358" target="_blank">📅 20:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101357">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c31a87807a.mp4?token=eO_IMTt7TJaYskD_m8o5Mupyr6kRGy_rEN1KoPcJXVmSOR5h7K_2vzcyid2de2p4fgFz-1JQtbaKg_1Rf_CNwBs89qrTz1kLImtA3UCG-_3w6p9TiMmJP7Luf356NW8aWjdTfbSvqgRSH7PK_M6k-wqWseSqh_ixRO_uoPyREqPhVKz_9Rjb4ARH5fvlG-_c4IjsmrNkrw8AaXbAIrcQi41ZKTPZXUFqunIG14ORVh3GxwktAUZ5-zzCdVPSwG4hqGameBLC1Sar31KjT06voLmlDXzbuEPNWn8BvYUqkjEjHsrbBQB6rBAofsucBB4VXrJGbfDZfiWhrtMP36KLuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
پایان دوران ستارگان دهه‌اخیر فوتبال جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/101357" target="_blank">📅 20:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101356">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
نایا: احتمال دارد تا ساعات آینده ایران به کویت حمله زمینی کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101356" target="_blank">📅 20:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101355">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgwqYn9GxntkU1Qts5-hQoKtxcwk2ynn09mdbmTY8na_VwN9fvhtxv2u8Rc4_3dUcfQ_BBgJvcbHPFVErtpT9WZl6vETqnnaqyBRcjnzZutT8HVEDXUI0lqq9Gq45nt5idGjteao9_RhgOjzni28MRYWJlh1w-x_ZEOhnS9oiKwfC6jKHEJNyIc7zRWSXbyDzqkrTtrc7YBHzOr-mnYopwlKWwC8KhAtzazO6wYtRAl24qLzqYPr4lkgCuk327z8dScZlVJdv_uKPPzs3OWil_Mm1y9vKmCdm5BAStLM8LuKZMKb6qGVlayIJaX2T-TU9GYTQmcnKtOF2QQnmRJwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ: هر بار که ایران یک سرباز آمریکایی را به قتل برساند، بهای این قتل را چندین برابر پرداخت خواهد کرد!
این دستورالعمل به پیت هگست، وزیر جنگ، دنیل کین، رئیس ستاد مشترک نیروهای مسلح، و تمام فرماندهان ارشد نظامی ابلاغ شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101355" target="_blank">📅 20:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101354">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/896a99e3b8.mp4?token=h3RJdax75POU9jPD8OO2e4Nn4q9ghH0PsfKpj-VSH56QCr7WsGmwvIjcL4LkBdGIP5SDNspwyLR-LK2vI2PqBf4UBBfbQXmAhPYXkQ2SoaVZg9PTq-a4CQA4I23KYDFxMfl-gYLMhE0_94JerwaEtzHu0WeA2prrfNs_Hq9RejfW4r3NhNFXeXKBl569TI7slY7lOOR-F1-E9-xGVy_09Hf66kIvmGziwXLcwNB_Qk9u_MWvbfUw_PkYftChg7E7GAJfc0aBfQLbDcdgusazwVxoIigR_KL7LTRntRYH85Sm67ME9eU68tJqG7D5WWC3bIobRn5fYIa6j9AvcjwhQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
لب‌بازی امباپه و اکسپوزیتو در میامی حین فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101354" target="_blank">📅 20:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101353">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6f0f5682.mp4?token=uHmOi-DDSJ-lTAksk5bsmdiXcZfAiEtLW6bIDv70kl6CFWrYBcwXAZnK1jrVsn7wMgTF8_hI5C0Sye3jTfEFUZuMwXrBqk2yQlELBM-0aNVRMgN94zUVXQsLX2R6j_4RQ85UphFMARtoWzDsf9qiVur3zPYkLNi13t9w5OMZ-AvccxqPt66fyz9TKCiONzxWlCzQcCHLV9iL9UEbRgKe-bChDtQC1nMfPi1WGxX0myibuC2R6BkMY2aXsZya7KsVYdtVFqU_pUDHPFhJgEo22Pgu45SH81_tzU3RbZW9myEROPofcV8qakYeIdJr0vzeG-9Pey505xJNNDj3SwaVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😂
صداوسیما مثلا دیشب اومده با ریوالدو داشته مصاحبه می‌کرده فقط چرا ننه ریوالدو مقنعه سرشه رو نمیفهمم
😢
😢
😢
😢
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/101353" target="_blank">📅 20:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101351">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTNWKxXfavKiZwB2KzZnAz_RmiqQHyt2e6J0mrp9B27b0-ZkFxquros-cChCDiVABj-DGH8h7goaVaGz9gQg0hxZ9w95MyJwRxm5lCj6_Kvn5pUVLis7L2SVoobzz87Jupe1mSdcZkP4-DwTwudtAl0hopwxNL7kQy2f0NTZgr4KkZGZc72V1GWCAYeEB6HPRP688R8paRSnuTIO20zOcJ43ttyY7PJ92wL3YupSNDvAaL7bQN1RevsmAmwNBQRMjz9ceQEVzYscvW1hVwyaLG06v9ClPMFg8an1GIGZGpUQxlXXqyx9UDZXhTejJacFncRWfeYM7NHuv2uAorxnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RjW_LbEK_80xS4A8T_-y0KrzxMR1o44sUmb1Rq7Lv8VlSaTysvI1bQm29f1KPfBrLDI7d8C3jHPPi4EoFEtNf6K2fFdjRi5ZHY8efkNBMc5EsDrm_HrFctqldiS2t1Layl7qmzEQAGSC2muiBRzTMGKyKn16QB3Xo9E4nE-jFd3DPP04zETJnKPum9k2XR2f4KMxbqrndzRGnoNSTFGsYndF30CgF1AHhKRSz0wDZGzxCWMIGhk550bRbA1dFts8xwcnsH5f1CS1bQbAcLVUBiHX5tR8pEHNXaW4q1RSYz3TF9hEi2QlnU7WnrYO1XlS7jtxBwo1HyC9Pji57zLYAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👍
اسپید، یوتیوبر معروف دیشب حین اجرا در اختتامیه جام جهانی مقابل چشم میلیاردها بیننده رو کُتش "فروهر" نماد ایران باستان و آیین زرتشتی داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101351" target="_blank">📅 19:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101350">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ihd9VAeymAVA3M7ayDa72fImv1qC_B49ozgsR5LJ_IW_jxq9wbSanntTxQiye3u_GrZ-prxJ3ftzi1Zlh9gT5V9eYPpSJZR-MOmR4W_6k5ocUzrKmj-W9qcPnuzbNACBVJ9vQAbCVR7v8TVV_wpfJHgREFrGUVcAy6IFv7_oR43o6FmWvlLZ0kj6JnSCcki9YPgCXfX-48SVHA60ssiQBUfSjK28_afbVXcIrZUkJW3zwjv8YS1i8nyatprzvC9Uxas6U859yVzQHvk5HdnKVhuqrQKk0GvwTy_cAJgFg5fLHWmUqIkzLxmmR2RhrJs9jRkOl2tHZ4OBtxGjBPoIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بالاترین میزان حضور تماشاگر در یک دوره از تاریخ مسابقات جام جهانی
✔️
جام جهانی 2026: بیش از 6 میلیون تماشاگر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101350" target="_blank">📅 19:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101349">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6626cfb5.mp4?token=R4v0zi2xtNLm4s5gIBvkpTNPh_EYu54lh_rczCyfN_rreJeUKA310fvKADLnKRS1PABHx8UiqCjQDQTjOEpOeWRJLgEIoMEyRbT6PWPP79QcR3MkAVrOEjwSnB6BGLNNVTadEU2oegP_DIsCkFfkW8dwuO_JkQCyyvgnFXo0X2TO0D3ZeHJFKN5NIP2vvqcVHh-fG8rLBHydJpkyW40Hx30OLJz_pb7HDq0HijEEtXDLLfRM9pAnocXTnDKUnOuexMj1JeD7HS-QFk1r_i-wzxZzqjWrhojc_wzoA3mbT3oA7snzLiQkqcNLwN7pcpIr8OvUSKhJ2eCSdUd_Wo_c8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
هوادار تیم‌ملی اسپانیا بعد قهرمانی جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/101349" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101348">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0058133a45.mp4?token=l0Bb06s1LMJ_4Cw9mMxHr6EhJTwulXvLRtFxEOe_jzB1-hPfEHgC0UQOJ1KRZgvp6ziIAKCKXZJ7q6VBghgRIvxdHLzm4kRhsObfdozgjSGYdZibKWDBLpj4v7nU4gEYlghPWAJDD1SaZemKQWhHzAhdULjH87FszNvenqu7yi5E5mOh9MvV6tgVYmoDLKRZb_t9oXzoN3MkHXwFmEHtZe0SQsiOoytaQjrq9oPZzIRXbZOjtA3cgo1_N9kUmCg3oNpnkJfUmhTfkBjJR8_l5cKhAx8489u5_Z5T28A5SjIvUnAb9EajYRLn5htxQjSG3dV2cC9WTelB_9jGkPbAsJTq0nLZ6ZalCw7JPMdDm_nuUTvJmn054ZyxtuRmYiNqiXNFKV7HJkA9vBcQdwbj6cKqY32XyWk4iukMYYbqUs44UY20h26sLTR8Ifx4FN2LTpNm093jVQmKOfhbFlXWKsBNpSjmGqB_tQEGKEUPoZGYiJzgmN8_2jukY0I2RyckGQfBFsy8n9hMcRHzU32cJSLVowXkrclUncRib1vgOXD3wYDttL72pDb9779QSu2sET_v8UdxsWgCiESCH28mkPKOImLzdemYGzB9kqN3L5ZORNfiS50zD24es7oEC8aicDdcyo5o37U84bL_ObqHMmS8ZwzJQVBoFuKCSr4ZA4o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن باشکوه دیشب مردم مظلوم لبنان در بیروت برای قهرمانی اسپانیا
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/101348" target="_blank">📅 19:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101346">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=h8tASxVCG3auJER7QggvpvNeQxxKSTLsiTRqJPSgcZYUkr7LtpQCBsSwbpCOKaeLQTy9hVYfUmXyLAUd8ZYO7eXHejdr77Lq9M9sNcNY_H1QtbR4puhAXvFOKVrY34I_0V-lnPWb4gRsZLhFPixxz_3YzYIqA9rEWR9v0Lxv1Lk0y9n_-DCCHHS00tcZIZ4pPAbgnkE24coYhPO6iMy7CYRQQEKqAkcGeaF_JfM2A0CzuhhTVnyoOWgvhczRprfaK_FgMr04cqdLnslPxnbkn-8aZTzcLNF2TXjDITZRvRHimzOJAuwn8RAB2ySv3lepv-czAfqoXnEXZsi2fTesZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79908eeea2.mp4?token=h8tASxVCG3auJER7QggvpvNeQxxKSTLsiTRqJPSgcZYUkr7LtpQCBsSwbpCOKaeLQTy9hVYfUmXyLAUd8ZYO7eXHejdr77Lq9M9sNcNY_H1QtbR4puhAXvFOKVrY34I_0V-lnPWb4gRsZLhFPixxz_3YzYIqA9rEWR9v0Lxv1Lk0y9n_-DCCHHS00tcZIZ4pPAbgnkE24coYhPO6iMy7CYRQQEKqAkcGeaF_JfM2A0CzuhhTVnyoOWgvhczRprfaK_FgMr04cqdLnslPxnbkn-8aZTzcLNF2TXjDITZRvRHimzOJAuwn8RAB2ySv3lepv-czAfqoXnEXZsi2fTesZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇺🇸
بخور بخور پرزیدنت در جایگاه ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/101346" target="_blank">📅 19:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101345">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpPRQIHpPOF-iIUqj0ygdfS1hTPIe5mHkhrmaaE1NCCnvdjnfwSQUnrHUD0Hg6mKVa1hEXx73pzemzuYoGMgbTf0Mdx98bofVsNO2V1VddMhNTnumNadpIM2K9X7tmaFhv6t0iBrNpRT48eoOzWGRgFP3wqEsQf4ZmkI8YvK08RFlaHHs8M5fV9pEViKQUcB7FxarDo_hEsab2YJTln6Y-3Omg86Xid_mP3gLs1zD0X_Lr04-oS6zJdQNeSbBM3um6yVFLylBl16381p5IVgmiMmgj6NE_bXkGy-D5xnE2_jhRkOVP41Muf2hmw7kMEZ6k5oR7wTRLF7m9khEkLDlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه با ۱۰ گل اقای گل این دوره جام جهانی هم شد. برای اولین بار دو جام پیاپی یک بازیکن اقای گل جام شد.
و برای اولین بار یک بازیکن در یک فصل آقای گل لیگ داخلیش، چمپیونزلیگ و جام جهانی شد.
عملکرد فردی: کم‌نظیر
عملکرد تیمی: فاجعه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101345" target="_blank">📅 19:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101344">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLSZzbMm2eLFjRu1aL9Xp_vBcpCOlH_-hyX3kFoZ-yosQD0BZQBF0WLu1DLTnfTLPBi-9TH-0r_g0hsbUH6hJ3MsxCHvWe3kUrdd8inpmF0O3AoQ0j7QrKA3fkmuKVjpQBIUwGs8eIdHIwonWkW2NYqYE-n0oJHgW9-32Hp638kgnqxbDE6e2qCf0375F8reqKFFwyDBKIKYuzHgyPP-5AXUKbIlk0h8ZfDx73t4idFSrcJfv3RNNn7HNrnDF2yW5q-l9EchFwp4_AX0FnCxtWVwv5pM1JLQOIhIBjA_lR6m3T3c2SCrAYMbKZEqN8-31W1g_uRy77VduohCb7IeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بایرن مونیخ از تمدید قرارداد لایمر تا سال 2029 خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101344" target="_blank">📅 19:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101343">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773a69b961.mp4?token=CPl6LaS2UmzhJgm4WIEPOjyZct90eS5l8uVUlbFOaje_o-6ISCy-N5xkUs4FAxiw2LTnFkrLh18yE4WiumGkysO66b5Fr6kVuywg06yB-4DsBh2ltzJzXIcceMGbTI7D4I7KiMblCr6GvBSc8cBkMa92u-sU1EdIMwaX4AC2_FQMH70ZOjIYJt08TMZx5UewSBupH4HSC8fEqPLHXIzPkxJiHIaE7NbCZEyvtnQjJKfnu-2bgbjV108yQVINkffMkBNBtzigiKIo48zLl6KVplgDgiZD6-KFy9CoM55VXjLZowInVNuS8I6AWmVmC29ZGVsNBQmmSf6q-I_scV7DoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773a69b961.mp4?token=CPl6LaS2UmzhJgm4WIEPOjyZct90eS5l8uVUlbFOaje_o-6ISCy-N5xkUs4FAxiw2LTnFkrLh18yE4WiumGkysO66b5Fr6kVuywg06yB-4DsBh2ltzJzXIcceMGbTI7D4I7KiMblCr6GvBSc8cBkMa92u-sU1EdIMwaX4AC2_FQMH70ZOjIYJt08TMZx5UewSBupH4HSC8fEqPLHXIzPkxJiHIaE7NbCZEyvtnQjJKfnu-2bgbjV108yQVINkffMkBNBtzigiKIo48zLl6KVplgDgiZD6-KFy9CoM55VXjLZowInVNuS8I6AWmVmC29ZGVsNBQmmSf6q-I_scV7DoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های زیبای دلافوئنته درباره اسکالونی
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101343" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101342">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eFlYS97TglWPQt6IV5VDPbZ-g8xXYmjiKK2oUwQJlrjhMLzSanGdYer8mrZZ-yJlMmDV2hHjwSm-sIyEv68BqfDNlQfbeAq69JM6e9bQH9B6lTixtv6ULMwZjxZZ53Q3QpeIzidt_q3nxOTaGUVeYymkiLecqvGAaVtZfutEfQEyvjRY8ZYc2zcazBTfkqfUNbKoMxOG1-lq8TDZA1c8kLP85yD4lMrCy3z0Qwi2uCAnMjz-AInTT2NgkbRAS9lCuQfeMl-9tqmje6ZQwiHXnJxUAVljDAtRQGdSXjW6io8v24HF_NgJluC9EyVMQYiL44hlQ-tWDfhdZz565gRMXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
#فوووووری
؛ به نقل از منابع آرژانتینی، لیونل‌مسی تا امروز تصمیم به خداحافظی از دنیای ملی نگرفته و احتمال داره در کوپا ۲۰۲۸ نیز شرکت کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/101342" target="_blank">📅 18:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101341">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=g3sY4D0c0igGpOfVTofu6S1RPeAqQRvdvXr9ryDKhUtq58TXCcNN2jRh8bxKbqJHTioCgUG5mjxent4HBGkiPehlnTTcD3qXMH4abX2SonT_AtsesPxUZf94GZ-69bLqvpGU5t5loHWsmi3FZdbIRl13xjWZOjs75kMl8dNBOGWjk2iokE7PzHPVPkmuxM-UWghRiIuLP5L6klArp_LzZpHVsWbhYFCawjCW19EXb1uXEZOsvdXAcMWtODp7Nhe2fxK1PZh601bPArq4AQyDGd7rusYuLA8Mn2j7l_VSnbjiozV4ETm4i-JAtdaCaEPg6mfhLlUYmVSiRkidlhEifDKoyxxBb8qHopkwpLrjSVleEev6YzHYO9aJ0iNkSEPEAg6J7WorfCnBcsQmK1YasjiSkH1I5Kzzz72yx3khW3euPeI84LylHAIYp8wbQLNFj3mzaKjI_EevZJNC0zrmE_mEYVhuv4BA7hDCJmw3T0fYyzRT2hI25qb52DSIStw4kba4Qm2LmkPpeJCocHSPpmA2NtECgiEoAucLLE19biKg9_Gkg-LRFWq_fku5SlwKFyLO3W_fMd95bu9Y5PGEVTT-g4z8018ecKam-3lDtNZaQY8JpWo23zclCw7-8PBK5fzoApe0soUN8ooycIkL7TBP7cyjnFTWgD599DsXCg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f3ee1c7be.mp4?token=g3sY4D0c0igGpOfVTofu6S1RPeAqQRvdvXr9ryDKhUtq58TXCcNN2jRh8bxKbqJHTioCgUG5mjxent4HBGkiPehlnTTcD3qXMH4abX2SonT_AtsesPxUZf94GZ-69bLqvpGU5t5loHWsmi3FZdbIRl13xjWZOjs75kMl8dNBOGWjk2iokE7PzHPVPkmuxM-UWghRiIuLP5L6klArp_LzZpHVsWbhYFCawjCW19EXb1uXEZOsvdXAcMWtODp7Nhe2fxK1PZh601bPArq4AQyDGd7rusYuLA8Mn2j7l_VSnbjiozV4ETm4i-JAtdaCaEPg6mfhLlUYmVSiRkidlhEifDKoyxxBb8qHopkwpLrjSVleEev6YzHYO9aJ0iNkSEPEAg6J7WorfCnBcsQmK1YasjiSkH1I5Kzzz72yx3khW3euPeI84LylHAIYp8wbQLNFj3mzaKjI_EevZJNC0zrmE_mEYVhuv4BA7hDCJmw3T0fYyzRT2hI25qb52DSIStw4kba4Qm2LmkPpeJCocHSPpmA2NtECgiEoAucLLE19biKg9_Gkg-LRFWq_fku5SlwKFyLO3W_fMd95bu9Y5PGEVTT-g4z8018ecKam-3lDtNZaQY8JpWo23zclCw7-8PBK5fzoApe0soUN8ooycIkL7TBP7cyjnFTWgD599DsXCg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپانیا اینقدر طرفدار داخلی داشته و‌ نمیدونستیم
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101341" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101340">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101340" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101339">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L20ecoaosr6OSwzYtrsf3SHjontOaYvr3m71-LrkRztoN-yAeHglrzT32FYqaeenSpmanTIszxaZgdwxJUKe2bQWRJwl_K3x1LAciS1PeChGaxmM_djtyBc-sOgz7m4ZbAodIBgSc4RbgWdCHAn3enfSS11dREahpcPzsEyWQ_LuiNxrzi7jOv8X1izDZDs4Dx1bOG-43lXzeOn6Us9SueMpvk40MVxbMd6hk30NPgG_kony_RUH-hB71_GdCKg1cAxFLlUJ2xFSbnRQ1ARaTMFnpMKO8cvv2IRowR0biobGJKa9Viy1FkM2zRlQvnrzFtxH6uqT1EM0x7ESbbp05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/101339" target="_blank">📅 18:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101338">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oInOHmu8ZtumWdQ-fOT15ULjBzUM0q4tTe3aNH928ZlAVQBcBgnHfZBi19grthdfZhh2Odbgn-Yt-Oyy1t9FMm-Kv1dxZNztCLzwxTDbahaACBTr7i0XKrpUhYA8QSFZYXVIvCjqD3qu4cUynp1B36tqc6eFzn6LVRmufJLPK5ZXUG6fSjqZ21tStmU0E6VNcewYx5pHKC_O0R-QdYd49cobJ6rfJGorzBmRnJnJcjgnkUXW5Y5jSxxil02qzf704ggP-65F3xjLqac2V4Oq0Er2Np6XmkIeXcxaUZKGCkpOyFgIb9kEv7bDZQ5SwdyjZFnG1sNBuujPg0zak0z1ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی براساس سایت آنالیز اپتا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101338" target="_blank">📅 18:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101337">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBGqLHXP1KvsIHvWvnkL0YX8KG2PII6iaESkR3mJ-Vp5wQTVfBo6JJ5QHKk-6bE7BMflKwD4H26KNacWaIwFb3vK1sHTNq8SY8d4vJztdnwhwgEIU8f1ORmQgoKiyYfq6-hqckhvp5rwgwQKvH8l7kmaJY9DhPI07qo-oylGmFjr-1apPkoaNueuFFq23vNJ-yNBHCWbA2jTxhJdwads2FZv4MWoCjam8qZjggcuZaYvAUqmm4NLGY0Mcbc8qHEOJu0ZkbYlaU_YrsT4y9OPCbtHhcGvfM9gftgTBLN603lLODxQzLQzsjtr1JoCtUyj-WNvRqMltZ92sZVKJ3boEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتین:
انتظار می‌رود مارکوس رشفورد دوباره به ترکیب منچستریونایتد بازگردد. این بازیکن همچنان به بررسی پیشنهادهای دریافتی از بارسلونا، پاریس سن ژرمن، بایرن مونیخ یا رئال مادرید علاقه‌مند است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101337" target="_blank">📅 18:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101336">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-Wu1OcadWbU5e48FWrCmwqoSTTsI075pZWULYn3duuG9nI2S_CCok2K2L00TwBXOgxSX5twgDWU71rgOanQmTjNZU_DfCR-x8wWOWc5riZP0j-_UnYaxqyY6smizOpbUYW1umfkzgQZsOCevyUVeJtwAyE5X-K8FNBhmqapMt04Lm7eehfkIuoGudyyXLLVnmCrRyXgNOa5-kB8L0rGIg8BYSVjGav6UbUqI6nmixP_90VsrTrGS2rrRW2x4f7OTIj7pFbyfZqxZuXetL1dHI-PFWw9cBwdUlSfGNPrENViZ6MCF07sqIP0SQQI8u3bhFAGduG_UaUGCGrFd3Jdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیست لیورپول برای تور پیش‌فصل آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/101336" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101335">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=pihc_F3wPldUm0zAIDiVtHfeTFM7zn0GR7nO2eut03N0pur3iIJ_6KmRHUo32NGf8Ye-BlzOZSY4j8YkBMc8tkUp0w00NbD8hebW2m0MkW_T5Ox9DS65ePnHeMN2OF_MqhOkkScw_RP-zCAe95_tF0anvgiPxWU2W1BcBwjC_XfpVBJ9oNDtTH5ZUExfvGhDcG8WV1XqQo80V9dBhwj3Mv-SUyF9fX1a3OE8qtkc001aEsknN5JVUeaMArn0e6ZURZZbX3gW66jnuuTCqRQ6-7LuVl7HPZhB_Jy64-whYME-cn0ryKMN8hxi_kLnRjZXCjiZFEuVRKwAsyPLVsoA4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5737427fd0.mp4?token=pihc_F3wPldUm0zAIDiVtHfeTFM7zn0GR7nO2eut03N0pur3iIJ_6KmRHUo32NGf8Ye-BlzOZSY4j8YkBMc8tkUp0w00NbD8hebW2m0MkW_T5Ox9DS65ePnHeMN2OF_MqhOkkScw_RP-zCAe95_tF0anvgiPxWU2W1BcBwjC_XfpVBJ9oNDtTH5ZUExfvGhDcG8WV1XqQo80V9dBhwj3Mv-SUyF9fX1a3OE8qtkc001aEsknN5JVUeaMArn0e6ZURZZbX3gW66jnuuTCqRQ6-7LuVl7HPZhB_Jy64-whYME-cn0ryKMN8hxi_kLnRjZXCjiZFEuVRKwAsyPLVsoA4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ اسطوره های بچگیمون
❤️
🥲
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/101335" target="_blank">📅 18:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101334">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=IJ1QIM9oq6V93lJqPZCcMcIyuGXKulcP1ErELdlSQJxDAMpsHY2EGLlq0hSIdYlVO8eJL9X1FdtkSWWKTVgI3iJiMm5fLx78b9IyAvB2fedC-Nlon4k0tO3aMmVJnLHLbelmgKfqMf6jIWKuN-p0dZWyoorlFtlTg-IONjUP9_t852m4idf7JU1hmzoYWY1nMIMbIHa2tBksObLWMNEzC8OggNXa7ViFub2yDUf5yF8zUC4aEkdyCp2o-RBsUgE9aEepwj9IQUlE2WaQWxa88JthLvoI7cGnpAaYJxqucn2OYxdz-RIYELn05YDBH6s1j67aEC18sUuKoTBSbb3_iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f8e9bfa.mp4?token=IJ1QIM9oq6V93lJqPZCcMcIyuGXKulcP1ErELdlSQJxDAMpsHY2EGLlq0hSIdYlVO8eJL9X1FdtkSWWKTVgI3iJiMm5fLx78b9IyAvB2fedC-Nlon4k0tO3aMmVJnLHLbelmgKfqMf6jIWKuN-p0dZWyoorlFtlTg-IONjUP9_t852m4idf7JU1hmzoYWY1nMIMbIHa2tBksObLWMNEzC8OggNXa7ViFub2yDUf5yF8zUC4aEkdyCp2o-RBsUgE9aEepwj9IQUlE2WaQWxa88JthLvoI7cGnpAaYJxqucn2OYxdz-RIYELn05YDBH6s1j67aEC18sUuKoTBSbb3_iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇪🇸
نیکو ویلیامز هم تصمیم گرفت که مدال قهرمانی جام‌جهانی رو به مادرش اهدا کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101334" target="_blank">📅 17:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101333">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=EMyedATXYqEJ-xWlRJ6qOdLj_CWjQ5BWULfA9Is61dCSbgjRP7T5cKC5KY3xaKxtEEXLEMPHf1l4jTwIsuo9uQEzAq_8lluTz4n6HixvxVHNBNNkhecWMusJd6-LBiOr80G86VEvPrgCdhoXJHqgCfKKG9Dpi9DHhFzqMyD8Ad2migbg1oXXHqjG5rey2pw8A-BDDRI1JphexaTqoDv357dWvz0IXA2WOyVs2cKdVNgyhb2Gunn-BeaFnr8u6GOYRgJ_dStnZ3Szk2ksxkP6sxvY7kwzl02z8js3ADC6aQ6ifCAcwTIhVQkWaNyZ1Uz1NpJ_jG-AzEfvgC8ZfChf6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd0e4aba5.mp4?token=EMyedATXYqEJ-xWlRJ6qOdLj_CWjQ5BWULfA9Is61dCSbgjRP7T5cKC5KY3xaKxtEEXLEMPHf1l4jTwIsuo9uQEzAq_8lluTz4n6HixvxVHNBNNkhecWMusJd6-LBiOr80G86VEvPrgCdhoXJHqgCfKKG9Dpi9DHhFzqMyD8Ad2migbg1oXXHqjG5rey2pw8A-BDDRI1JphexaTqoDv357dWvz0IXA2WOyVs2cKdVNgyhb2Gunn-BeaFnr8u6GOYRgJ_dStnZ3Szk2ksxkP6sxvY7kwzl02z8js3ADC6aQ6ifCAcwTIhVQkWaNyZ1Uz1NpJ_jG-AzEfvgC8ZfChf6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
اشک‌های لیونل‌مسی در حین تشویق تماشاگران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/101333" target="_blank">📅 17:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101332">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e0946a77a.mp4?token=vanV0WtR_K-hC-ydV-XQu_TvLZa80vecxE_zgmtw5z0Uw_DW3TeylSFWw_PY5SdP7jRb8vSiChOcVffiitrEjRD7q6sHnjoJhqYYs8nwjQSS35czeE71U7y69D-HlfM8Lv-26F1zEfIcth0FGhO-XEKPl0SOh862q-_uQX4HKehsyC8CL-wrkl-KNOdV5wZOkG8Hu8YSt8y-65Fw5TGdU-QdNJTIE0B5kPITAC1L7BbRA6VscVcbNj7HNmYUCydaVMiyMe8y5jLwMX48_05FvstnHnnIvAt89ZChqs6aYYwnUja1fTqcjQnsKPX4UeaVtUgDiBV1bw-s1BoewKHp9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
خبرنگار: کوکوریا و بعضی بازیکنا قول داده بودن بعد از قهرمانی تصویر صورت تو رو روی بدنشون تتو کنن⁣. نظرت در این باره چیه
🎙
دلافوئنته: کار اشتباهی کردن که قول دادن اما اونا به قولشون عمل میکنن چون آدمای متعهدین
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/101332" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101331">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l48lGb-U6GyuRWLxu50Y6I0L8XfrhlCWx9WsG6Eeu-z7JeMj2br1-iomqA7aU32wAIz_J8qiJRAB6o6klYh9DZ6NXaufDJV5LIjdoZ9TznULTayzKE4NEka9juVLRrDe8S8k0uv1FHWi1gkD28B6zeSLwuj4mRKzw6iiS2Qm51Tir3DxDyuY-Fl8lO4ydCFytT5-dGp4Z_9JudprrEynblwWJ053wniFl1EQ1uq2zr4DiLa10lPRH74aUGJd_31ws5IespKKB6JE_A0lRsBDPXkJZ8S7BqgA7mJZhTJFOnUHQeV6GEDQAbq4FzoK597UlurhQTgA9-JdS-xWl8znyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسکای اسپورت:
فیفا تحقیقاتی را درباره رفتار بازیکنان آرژانتین پس از پایان مسابقه نهایی جام جهانی آغاز خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/101331" target="_blank">📅 16:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101330">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=kv0QgakJZSWJDDvAJn4PFzv94VKTCUF2qUqwsL8cj2SScWe7bKjoZsQEk7X1_gdZCUDyJiscPpBWOsH2YZYnczQGH-CR7PFYQBhjGIvt1tQnZ8B6a7JkPj0sUP5byl1xD57_WKaEOL4bhAhC7szcmg7_HFVpkcKHZ7WqXxeOUsKynM8Rx7ucXWZDoqsw6XGMcv8Q9uXqiv0i-3kvL0sK0VSggZIYdLpLWSsvFna-3I-EfD8lxpszipuvlqBsDnrtO0wDKTxiCnyWQueM2Pw7K3M4Ck0MPH8os4YW7oSNmo6HOkbKiS-goO1z6u66-YYuSlKheREWoZXWPyP3MToRfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f3ec6d627.mp4?token=kv0QgakJZSWJDDvAJn4PFzv94VKTCUF2qUqwsL8cj2SScWe7bKjoZsQEk7X1_gdZCUDyJiscPpBWOsH2YZYnczQGH-CR7PFYQBhjGIvt1tQnZ8B6a7JkPj0sUP5byl1xD57_WKaEOL4bhAhC7szcmg7_HFVpkcKHZ7WqXxeOUsKynM8Rx7ucXWZDoqsw6XGMcv8Q9uXqiv0i-3kvL0sK0VSggZIYdLpLWSsvFna-3I-EfD8lxpszipuvlqBsDnrtO0wDKTxiCnyWQueM2Pw7K3M4Ck0MPH8os4YW7oSNmo6HOkbKiS-goO1z6u66-YYuSlKheREWoZXWPyP3MToRfzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت داداش یامال در بین ماموران امنیتی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101330" target="_blank">📅 16:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101329">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cm5jb8dJhoxVn7HPZzu--pO-AxZX0Bdm-LtRMRk3TTlLFZcwiu9cf1R3WmXFLtbJF--LqQkYojY17d3hTWb4-j4Z6awzdb0SUF1nfAEg5xfGWtc2JaZbXDGiyGSOiAQFIBn55W4nVGSCBOOADybI0uz3AnmGDO1mZGrRRCrhhX8rpvPClMjAHmLZOv8A4A90x2psXJxDxx94rNbIu1cwn5XvjnlET_To1IN4n8cg7YVMwtwGc9j5sLNkr4Rw8AxRWV_WCewMatS7DNFTg9YyVu_zLsUhK9Sa87x5OsO-U3_gTqTGYOMh8vFB8t5EV_gR5ktLhfij90qpE2BUL8u2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
قهرمان جام‌جهانی به کشورش برگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/101329" target="_blank">📅 16:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101328">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHiwzNhCw6yeVIPPKdZ2tHdCaWa8J8vZ8VymxTtw3at5oJzvvQnhhQpn2NvTRDcuMDyFo8iNPWmUc6dosXIi-VxLsDU-XBRLJrTMloNgSUoiUau0QfuK-xHp5eOkvTyvJV5gqNc3TineI72yx_PW898S04INS7iY3ktWAdTcQPHb8kDNIg3fcuJxU4e9YI7m2B6nvpcFQWGcBt_U0l_NZH3o9XXfq9DW76vGYkZb4rI5xDvvF41wHA7jG2KsCtRPCW-ZhBMw6rhjA86ZzG_1ul7Tf-p2mGyGn0SF8VNqezEYCXSolOJ7No1DDY5hV0BUlWyzEHYcTrGAOWOA_16NyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
گاوی و بانو در مراسم دیشب فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101328" target="_blank">📅 16:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101327">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxKaljJiovmzFFKoofboQb-dLFuJfVb5XYiM59koKYBWOFD-KByD4FpyLfMyb9xc15i8fJie9omefP1xTNDzSApyAGzMkeIfHpySwtL_ILOMufvUsKCge5AIsWpHgzocJMQ6lw4mpq_Rs-J9KNFkmGgQ_DHOGwBhc5iYpsUSLcOX4ono44PnxFxrDgaRyd5fCUEESFjLIkj3aH5HF7B96uaK-vZS0DV2qI5DDwhzsrvLfx4m6qVLhxTZkA_r0U8-6JL3DMkY9EZoIpPvZVkVSvEeA2DGzisCWhBq4Zjf_mtN5BxoYrk-p6t9fw5WdU9eT5SkyM6UN9cv7npkKV814Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رودی گارسیا از سرمربیگری تیم ملی بلژیک برکنار شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101327" target="_blank">📅 16:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101326">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=aNMvaEqBWJq8teDstJzYQQHpPT0qr1KKeaSoLqI75SIUUxidaVkb9iBpdtFVBdJVhtPqp0IzN8QTwLGCtHOKoIhLGgG3GsefsTDqk7UJ23TIBabGxlOozu_JUiCGpnUl9g_yiH4gLa5ZaXgLZoKx__atJBplxBWOf7h0hoNo-mShDatzKPua8xzfG45kHcsoHvtgS27qj8k7REQ42N2xyrdgUfJ8CNima5qElfiAucXYs3k5A78DlbReZ65gMr-OjZ6X0DFiDfiBm-L-EQMppDPlPwIRGBBBCt7lFgxOVEuS9MaKOxgDHBuF43wQ9qQOEph-R_GS3tOvwbl5rS2EAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be537ad6b8.mp4?token=aNMvaEqBWJq8teDstJzYQQHpPT0qr1KKeaSoLqI75SIUUxidaVkb9iBpdtFVBdJVhtPqp0IzN8QTwLGCtHOKoIhLGgG3GsefsTDqk7UJ23TIBabGxlOozu_JUiCGpnUl9g_yiH4gLa5ZaXgLZoKx__atJBplxBWOf7h0hoNo-mShDatzKPua8xzfG45kHcsoHvtgS27qj8k7REQ42N2xyrdgUfJ8CNima5qElfiAucXYs3k5A78DlbReZ65gMr-OjZ6X0DFiDfiBm-L-EQMppDPlPwIRGBBBCt7lFgxOVEuS9MaKOxgDHBuF43wQ9qQOEph-R_GS3tOvwbl5rS2EAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکت خشن و اخراج انزو فرناندز از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101326" target="_blank">📅 16:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101325">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936d28a634.mp4?token=uE3fRWvN-z6S6vkVFXLEuE23kVhCSQwA9HgHhlPUfCcyLuiW6e00JeXpG6zp2UojvbmesYjB6VuBHw5dTixl43Lalx9ch2MYmIJ_zrlaF0XU__DuAI9dbskEirsM1ODJ6KBsXder6bRE9FGcfjJU8rgJ8nGJ-q7AfTXJP5Ry5PnG0f1FKFWuQnQEV_NrkrMt7ifwEOzDzw3ZdOhafkVcXH8TmzU1o1u3aHfKvDRd-vQ9HTSyQi3Xll8No2kUrQTfOOhCzqGQVTaGpomSbYS67cWQWHr2Z6LCIgEF05PRwR86UlMXyjYCwHnVgZoZRPqZEcLyY9xqpBy-Q_m2F76rig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این ویدیو از تفاوت رفتار مسی و رونالدو از دیشب وایرال شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101325" target="_blank">📅 15:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101324">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubf1Ogecv7K2_WUGH6VaamoKsLHPVmzVtGcIaa5T3z4ejaw3hanYGWt-kuBnJ2aQ6crbjS9EVImEEW4cAz8ecfKtdO5swgSLLDTxgly4paLXDua__q3nEwsk_KfhfEzpNJglxcHC6WMd2fDk8rdDVApZ-JhkW_oZN2-WJT6Zr3jhZcsu2JKQjNRpEZ8sefJqGpfBf-QB-EsSfMByX-Te-9hdyh6MXL8OU1lCy5rPHqyW95zDT7dAgrWa3Q0Vf25otosYk9OzQ-n0Z2O_WRgRNbu-c30CfsLEaBzJLR4H0b2jvDrU66cS-q26lWDNvtJ_8GeRMudL5_Meq5nGhmhkmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارک کوکوریا:
قهرمانی جام جهانی و انتقال به رئال مادرید؟ این یک تابستان بی‌نظیر است و من آن را تا پایان عمرم به یاد خواهم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101324" target="_blank">📅 15:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101323">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46470a010c.mp4?token=DcGoKiraraaxo7QdYL0RQcnYAaDS0qLuu5f1PLyX75fd0kKYRzq1cC1zqQrJSxfiSoIwOAvOuFW1MmO_sHLt8Pvklx0-70bXYe1xGFg8sxGiJD7YBoJeiaf1l75iHSTync_c4ZmcWoaM38BnSFXyjBwatSr7OKAXkPwvDKLzr2iEDLgWd3g_Owt9_M4BVEWkLJKPdzlEonwI2B9d-E6FmVvEZhT1S1L0l8IPf9-p8N3HmAx3fm8p6gh0OYnHFHz8Fq5-jFOQZZHh98odNnpXOJ3Il81A418s_19qRpRMwivwyflRtsyE9NqkarBtJK8iBSmDCExL-HPLDuzYe1S1zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46470a010c.mp4?token=DcGoKiraraaxo7QdYL0RQcnYAaDS0qLuu5f1PLyX75fd0kKYRzq1cC1zqQrJSxfiSoIwOAvOuFW1MmO_sHLt8Pvklx0-70bXYe1xGFg8sxGiJD7YBoJeiaf1l75iHSTync_c4ZmcWoaM38BnSFXyjBwatSr7OKAXkPwvDKLzr2iEDLgWd3g_Owt9_M4BVEWkLJKPdzlEonwI2B9d-E6FmVvEZhT1S1L0l8IPf9-p8N3HmAx3fm8p6gh0OYnHFHz8Fq5-jFOQZZHh98odNnpXOJ3Il81A418s_19qRpRMwivwyflRtsyE9NqkarBtJK8iBSmDCExL-HPLDuzYe1S1zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان یورو در ۱۷ سالگی
قهرمان جام‌جهانی در ۱۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101323" target="_blank">📅 15:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101322">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=m5BRrK9SJ5F1fgqNJwQrCOxtr8WIBxQOLucueoi6y1M2LEHrM7JB-SHgF-SBzgXLaIwQbQENQxlhmXdQGcNz_bsFCd1gUnfSjIpQhf5wCEkNVsjesili29Irm0DaYMCXR1MCuveEwu7L-p16-syfE15TgaDAceZftskooChc2u1MOO0Zk20WUHxIy2vmZVAuuhiDUC8lfFS3G9mRiZCvOhm8a3R_ah0XE2Qm04PXblrbW1E0QXRbjbZKP2w7FaUP9adD4vSSC-mj_Z8_Wkj4WPIIDnGXmMflHCUMbr_HBDJkKDYDnXkoq3M_n6k8uQDp3VWnnl9YcCsJvXVYgjX_qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55be40ae63.mp4?token=m5BRrK9SJ5F1fgqNJwQrCOxtr8WIBxQOLucueoi6y1M2LEHrM7JB-SHgF-SBzgXLaIwQbQENQxlhmXdQGcNz_bsFCd1gUnfSjIpQhf5wCEkNVsjesili29Irm0DaYMCXR1MCuveEwu7L-p16-syfE15TgaDAceZftskooChc2u1MOO0Zk20WUHxIy2vmZVAuuhiDUC8lfFS3G9mRiZCvOhm8a3R_ah0XE2Qm04PXblrbW1E0QXRbjbZKP2w7FaUP9adD4vSSC-mj_Z8_Wkj4WPIIDnGXmMflHCUMbr_HBDJkKDYDnXkoq3M_n6k8uQDp3VWnnl9YcCsJvXVYgjX_qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😐
چه ابهتی داره سرخیو راموس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/101322" target="_blank">📅 15:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101321">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v38kvNfhd55G_5-oZYJrSD0ikjBmwOw1S7B5oKwNpHQueRli2ChtPSmhrUp_0ZgF3oF5BdgcaD13IudZX1Lo8z0oG6GDCVbboBVeCcTJauOkWBMkr8xoWdxGvREFgvjaoOUQ9rDify2R9ge9XKplN1WLkBMB2lc5pFTB4S7FU3grUx_mhUPh8xJ4s7v5yjWt18WOXQTBYdjGJ4qTRDEQvXXkmRI91hGLtyed59Dub1sgXx7CYyxw77YXzW69TV0RRxR4vZlVtHnHWyfW4GMrwVjmZmGukPBneaTC3aJZ3xP2dQCpb07FfM3JjCPdJze-Vv57y3E8TEGI3oyEOW3N3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی اولین فینال خود را با تیم ملی آرژانتین در غیاب دوستش، آنخل دی ماریا، باخت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/101321" target="_blank">📅 15:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101320">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYluZ0vx0s2DO6EPAPsarq6VuO2EIJ5bEAbKC1JmA5Z2gRIUChJUOr8KiD6OcModfcSm98hBUkAwymo7_I_CoVR_iIFEbBZh6rrGrHMrKtDKw2AzAcCpkiAsUESkfPrF82eTwcngpPGfQevQ4zDTRR4z4iliHaCqEjwL6EtRpPfj5nrTKvU-pLdbJ8-gxpuC7rhkfg5OBzW5toke9uGtMvNPROz1qfpNFC0QjkOYACWp9pCJefb9GJHP_2HdAdKMhKrCkq_Dkavfd2vDqoKrg2-CITQra2SM5FLgKWrQm_VO4mKdw4dHkAPXFj3bfO26gviwpvSOL2lmbUBfH3nLzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دی مارتزیو:
پائولو مالدینی و لئوناردو با پپ گواردیولا ملاقات کردند و ایده سرمربیگری تیم ملی ایتالیا را به او ارائه کردند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/101320" target="_blank">📅 15:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101319">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=skadgyK5VHgtEvFSh0UNEbiI15Hq4ZMkFYe9QMFOIx6IT2IqydhJqMPdjRDNGDjpW-5Dyfdp732-jszIIe4jlfohsY1K4zmjkmasaZGpLENwhyIrxcU39qANv2UtiVnWLYXfL0wk6xqMChK3SEUDvIUUQj9-QQ0If1V860pQRDae2Hw4so1od91gZl-y4N_0ro_SxTrKlPW2bHIBy14hHyJ95-0DrgW4htPDQMG46RZ2MAI5t_8a2nALlm-njdE1RkyipZGZCzlkEig7hZeuLWSNCFf-sT3Rhgt37fr8Hhkn15i1LHCPlDCEm6mRQXmlm419Z3OszXP9gSSxepJoTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a4e613e2.mp4?token=skadgyK5VHgtEvFSh0UNEbiI15Hq4ZMkFYe9QMFOIx6IT2IqydhJqMPdjRDNGDjpW-5Dyfdp732-jszIIe4jlfohsY1K4zmjkmasaZGpLENwhyIrxcU39qANv2UtiVnWLYXfL0wk6xqMChK3SEUDvIUUQj9-QQ0If1V860pQRDae2Hw4so1od91gZl-y4N_0ro_SxTrKlPW2bHIBy14hHyJ95-0DrgW4htPDQMG46RZ2MAI5t_8a2nALlm-njdE1RkyipZGZCzlkEig7hZeuLWSNCFf-sT3Rhgt37fr8Hhkn15i1LHCPlDCEm6mRQXmlm419Z3OszXP9gSSxepJoTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
نمای هوایی دونالد ترامپ از استادیوم مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101319" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101318">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0i-3egmHjqh9z086Qv0Ryka03m8keeLhsL3VMeCDvt7Lf1FnU-IN6I4JHN-H-b54hGeotOjJiBXxJqjgOVZvuNj09ZzQp69am5-rQUBtkaF40ALryjBSEQ3qe_OGnQrFcuLVRMj4ujB5TpxLaeesRMHSShVyOqOB3lCxqOOcRVLDg127Ik7wj1_OOoSBm41Qf9JilQlr-Rs-NcRB8ITFvK9Noj41VqROx6rGzN2nuu6WEWxpzFndWTtUlEo_gBOOliIROfqmf5eAKgkEzAaY7OnB1eqp8PzPq5312Z7DWm5tVKBWdvt9JYeicxPmnGYGC2cgFNmyXHca2vrR9E7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کیلیان امباپه در فصل 2025/2026:
کفش طلای جام جهانی
کفش طلای لیگ قهرمانان اروپا
کفش طلا لیگ اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/101318" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101317">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101317" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101316">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLJ98-sFBNsjW6bkmgCf2C--0S2hNWi0jTXTFvn49GbR4w0q4T4cIYw_5HzuAb9UZPWe8t_RG-jDeGSQ26ZzS7FvnKITizkDC_80oAKgYtsLmBAWVlc4WtV6GH2YOEmeatHCyThvkFCuRMd0dVzKbbHUX-W0WXfgwnXFfL2mNrt-I5aHIAWj2Hp0j7j4dyc84iA6XP8fGlw8Arhvx9pmiffusMW1-MK0GBAJoV3zOBpzFqaLs2QNi-MS7brUBK8oSrMUbkn2Z_Vm9OBZ8YDFQeqwlnqKMPeUx5dvyv49H43REiOrJt20pBx1hRdW6pv7cbwj3IRLiYruBAbqlz5WiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/101316" target="_blank">📅 14:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101315">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=qhMy4QpE53fhI_cX5KqtxauaXhg33d6ZEbwGSQR8VAOGPI_w7JpkBjcvAaO5XEZYkMXonf1JmUCr88jUQMPgWDTh5urVwvowRgpJggVextgK4yL9P1S5WNvV_4FySk7_DSjSmKNxqOtUZWuB25lXDvfV8__REvLRjeqpOKsad3oOKG7k0mOKPubUIoSwf6gVaRGGFzLSlFPyS0vT3Ja_FZ5-gqUcmlV_Ixz_EffzroRbcZI8hBe8t-YRdmN-3gUmtqtfj57XZ_F2f1sQ7iamwOApeAtspsxmiZ17d795UEKOWERI-NdV6KSn8OrZLHZUgATAG0QtOfQ5nmCFiZh7Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a9e5cdee.mp4?token=qhMy4QpE53fhI_cX5KqtxauaXhg33d6ZEbwGSQR8VAOGPI_w7JpkBjcvAaO5XEZYkMXonf1JmUCr88jUQMPgWDTh5urVwvowRgpJggVextgK4yL9P1S5WNvV_4FySk7_DSjSmKNxqOtUZWuB25lXDvfV8__REvLRjeqpOKsad3oOKG7k0mOKPubUIoSwf6gVaRGGFzLSlFPyS0vT3Ja_FZ5-gqUcmlV_Ixz_EffzroRbcZI8hBe8t-YRdmN-3gUmtqtfj57XZ_F2f1sQ7iamwOApeAtspsxmiZ17d795UEKOWERI-NdV6KSn8OrZLHZUgATAG0QtOfQ5nmCFiZh7Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد ترامپ دیشب طبق معمول صحنه قهرمانی بازیکنان اسپانیا رو ول نمیداد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/101315" target="_blank">📅 14:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101314">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=e0xL4pCyUAyJvB-KLZHhHvq4fup86PbH51hHCpXwKiLc7kb7M9Na563d62_wcVQFq7rqTWPvCxCnRb58nKOoPMCEqMvhqJ0xYd4YFmwrCIdBq2Rhk44ynWRW4FlbgciXt9uCpr_Z1PkbtcQKU5rlYh_rSkI6cKMVIImscDGzLLya9NjkZa_t3gB9zACfYNTEroFWERKQfYCqvOqYoOe5YWIPFz1a2SnSGN3q_E9IWf1cm2WHmskzNikUPS-43E4OJ6g7QPKjeGaOx50614iAHfRnRYEU6tq85No9HQ3LO1X4PAs-3jkIhT5nUCeIM79G3rWPNJ5hZJWrHpw9hD07VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12a251e59.mp4?token=e0xL4pCyUAyJvB-KLZHhHvq4fup86PbH51hHCpXwKiLc7kb7M9Na563d62_wcVQFq7rqTWPvCxCnRb58nKOoPMCEqMvhqJ0xYd4YFmwrCIdBq2Rhk44ynWRW4FlbgciXt9uCpr_Z1PkbtcQKU5rlYh_rSkI6cKMVIImscDGzLLya9NjkZa_t3gB9zACfYNTEroFWERKQfYCqvOqYoOe5YWIPFz1a2SnSGN3q_E9IWf1cm2WHmskzNikUPS-43E4OJ6g7QPKjeGaOx50614iAHfRnRYEU6tq85No9HQ3LO1X4PAs-3jkIhT5nUCeIM79G3rWPNJ5hZJWrHpw9hD07VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🔥
وضعیت کریستیانو رونالدو هم‌اکنون:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101314" target="_blank">📅 14:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101313">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=TVVThKjN2QFi42dhk8nQA9MGG-8eCB-Q0PRZV2-arVbRP7vNsnXBO4TIw14Z4sfkqD3risocDMZFOlTXagf-ETkX3dG8R_9l3fSRrzqqJl8qHNF1KjpgjLQBxwRereWVgKmldWvzSMBbUoOKzLJ50SUWWZy2RY-3XB-UeUQIrOoSpWCN4IiEQCjeYFVIkxUxeyGLUEh1WX0GvgrH3Cqt_Ur209OClWhLTqak50k19XKkBWhalleV45-pk9az54WA2oVqaAvHSE4MWCb_FuKu5idWFdC-meiuJXamh4pQ7FB8kQGRiU8R4uNiw2OXTN74XGbahpJxBI32OB4Hokfatw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d483e9b5b0.mp4?token=TVVThKjN2QFi42dhk8nQA9MGG-8eCB-Q0PRZV2-arVbRP7vNsnXBO4TIw14Z4sfkqD3risocDMZFOlTXagf-ETkX3dG8R_9l3fSRrzqqJl8qHNF1KjpgjLQBxwRereWVgKmldWvzSMBbUoOKzLJ50SUWWZy2RY-3XB-UeUQIrOoSpWCN4IiEQCjeYFVIkxUxeyGLUEh1WX0GvgrH3Cqt_Ur209OClWhLTqak50k19XKkBWhalleV45-pk9az54WA2oVqaAvHSE4MWCb_FuKu5idWFdC-meiuJXamh4pQ7FB8kQGRiU8R4uNiw2OXTN74XGbahpJxBI32OB4Hokfatw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
The end of an era..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/101313" target="_blank">📅 14:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101310">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSI3M2rnbrfnwAag4iisiJtBdhOI6e3lBDXGvzClKdMeGbLkVfaVojI5ZlvyYNmmGlXp50aTAGRwMVN8a-BUBccT8ghRCy-hvQbup-R4brdWiDozdLxaHFMN1GZTnJLghKs_TTDVEHLm8ZBrHnwMD3dcfls9F2KDJuZYRMtBifL9OuZJewXsX2uSTmITVEoAPWPS8Fs9_rMGyt-gIU79eA1miHaJWTOBODpcSfXE_cbesGVVsS4MELS4QvjVuUSUdq5CJ_rio2RfjtM1WkFdIf5eVI0MtfQ8bre8oXx1JUPUfYnJF22GylT0AMBNut4-qJNwDe47Br_dr7KPZTkEAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJv__C0QbOqyTBcUX2rWkbh96uyK-y251VoAnec88rbM6ZTU6EUw0GQPS3Qp6ZPA0Zg-A1tfIzBYg7K3WhABTPCAMPikne1XNRZROUtjbwK5bLiXo8fuxc0R9S1W6SqH7_nzNE9cakpuRAF-GWxobjO_T832N5tX-BL_5CuRnqoItR2c8aGQz3eNxHZi-Yu1sL70l5WV4wXKsTAD4lXclcOrdjNuLKzB4CkwsVd1riqPOOY8ttCi6OoLxxHgDAWbA61FKG2gbnSyTg89xQo9Llfsi2on5v5xV19K1TJJz3mnB8WTsnOegg7ij3wZxuZQh2o0RQZtX6shAGkM7y4WFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XAJjBTaSwEG5mGGVCxNbmjiUscJ-Jm2gYkmcHuMpC52TC0qSGKQblCxzfPne2orRQTO4_FSc1TSePc7FvUuuGdq2mNgPoaEl5gDCvxLVfTNY7nGO9LvujSg_kUxKxDw3XJNqAFHn0opMZIivbX-Ns-6WiznqmStzgr_x8AtufcKKUZ2i-lU5lhYVyeJiIwA30YbCK9q9vO0QU-sB6PUho-htMtZFeyzUwXEDgBfwP8OkoTqQEUWHW1ijWcDEvhjtImT0hG5gR2TzkTjuiVGmuJzSj_8_hhDFOz5g4w7nsglixQjzj7o9T3eiqJK-Ej4NWz8sb7N1rzFoqf69LTSxNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😆
🔥
کوچولوی دیوانه رو داشته باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/101310" target="_blank">📅 14:07 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101309">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuYGQNJ42QUkGaNhKi-_VCdFcNT1ILLt-gQ9A25oOh0Uuwy4SkKKNQF04Doug0oS2lkynHxpup20nXEBOaW09NCr7A5iljPob21ChStZnq5DiPOXcSMNACKcqgGgZPwbzk4ykxGvIuFUVCj86fRSNVPBqoseBsMumQVevZvbr2S-5urEBp5l37-F6uJPQxzPGndxmSfWIQK1sDUr7nEwPp_BRdeSPaQkoluNJJIvYNb0PSA2lruAmvJ5lMXSDoYBNNzqQy7wD0nugDAi6DqzrqiMZIUiWB8I7KID_N7sPcFHwtQXjORD7Y6vkb-oTx3cujM7iSpvYEEu7JpqSb_H0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📆
😔
🏆
تنها 1420 روز (34,080ساعت) مانده به آغاز مسابقات جام‌جهانی 2030 فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/101309" target="_blank">📅 14:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101308">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=bCCiK5oNCycAQ264lu7bGyh_emawVCL1PUbGoePBU8h3Dk5K7xrNVzDkjeeIKIsm1zzUPho1_HO14Pcq_Zwn-3TUcxKxfWOmreeHMYeEKplDhGBwHgDNBNuqoT-lnZCiMnb_my5FEAuNMJg2JNDdamOj7Ar6-kuwzCcVngPWpvJQMS1DGzoBFA7-n7O41J5iCOfIi9_UN9YDSLrNPdoPhD5SBGbvrcXl9Tw8fz5BhxyjgrJYk7mAZh6LpLrtMU5UIpZjHbwoKozcXHDIFhgtoMf-DqA7_yzKMXV15Jo7_ssgrdjB01GiaXXD8KSmwXSUuIoazGjOrHk18uzZEZELWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/367be64c4e.mp4?token=bCCiK5oNCycAQ264lu7bGyh_emawVCL1PUbGoePBU8h3Dk5K7xrNVzDkjeeIKIsm1zzUPho1_HO14Pcq_Zwn-3TUcxKxfWOmreeHMYeEKplDhGBwHgDNBNuqoT-lnZCiMnb_my5FEAuNMJg2JNDdamOj7Ar6-kuwzCcVngPWpvJQMS1DGzoBFA7-n7O41J5iCOfIi9_UN9YDSLrNPdoPhD5SBGbvrcXl9Tw8fz5BhxyjgrJYk7mAZh6LpLrtMU5UIpZjHbwoKozcXHDIFhgtoMf-DqA7_yzKMXV15Jo7_ssgrdjB01GiaXXD8KSmwXSUuIoazGjOrHk18uzZEZELWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شکیرا روی صحنه ورزشگاه، پیکه روی سکوها
و ساشا در حال تشویق مامانش، در حالی که شکیرا روی صحنه غوغا به پا کرده بود، پیکه از روی سکوها فینال رو تماشا می‌کرد. و ساشا هم با تمام انرژی مشغول تشویق مامانش بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/101308" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101307">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=cJoMBsljZDQYWnuTNG9viFxbmC62r8_IeFLzaq0zUrcBi1iW-RO5qUqwzjOS5g5hFxkWWYHIPPQR62duJMw24mD2zjRcB3a1n83-gFN6XffwKp6Fw7wek1ZFsnB3Wd0A2oEzE98SFoEvn38FS8vEUXCPkliGZIu9TZoT1cddjEhIRgysonItPj48ib2Fv7SNclZdsGFyhQrEZLnZEIJo5RmgO5dX5nW5HbpLb8C-cq9mZGHMkgYdfweCN-g9kSNXr5E-4mIhZ0dutsOypBktWyPq_z9Bcs9R5nRfwXw3u_xeHtcUnQDO1AEWZIzhyAfE4agi9vhn0UAn2HcsxBXH0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b927fa3e3a.mp4?token=cJoMBsljZDQYWnuTNG9viFxbmC62r8_IeFLzaq0zUrcBi1iW-RO5qUqwzjOS5g5hFxkWWYHIPPQR62duJMw24mD2zjRcB3a1n83-gFN6XffwKp6Fw7wek1ZFsnB3Wd0A2oEzE98SFoEvn38FS8vEUXCPkliGZIu9TZoT1cddjEhIRgysonItPj48ib2Fv7SNclZdsGFyhQrEZLnZEIJo5RmgO5dX5nW5HbpLb8C-cq9mZGHMkgYdfweCN-g9kSNXr5E-4mIhZ0dutsOypBktWyPq_z9Bcs9R5nRfwXw3u_xeHtcUnQDO1AEWZIzhyAfE4agi9vhn0UAn2HcsxBXH0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
اساطیر اسپانیا در هنگام گل‌اول به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/101307" target="_blank">📅 13:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101306">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B0rJbhKQiMnPGmZRi0CvI_KeTketzbVP2ABexZJo5myTqm4Ekyace1Uc4EmKTXIqZKOCgjouL2-tgIaJBHUI-O28jjzPfF4yTTXBWue3ss1y0po6ZLXeHZqFmhFwP5DDsshYIiRTM8UCS95ucf95Bu1DXpeHc-NuQcSD5mA3HIdTn1CBuvj3tOl9sGi8p-oNbWsfKiVmAYJFTWrpEmxg76msK275us7Fz3X5e0iRv6HzZetwRGD3bGnXsW4yHZG7BDqHFnv2OcaXZj5iGF4K_WBBx9NiX0jksRq2IOLaFcZtzDD5SRfLIcdQWzNythWoh6_wfO6e2WVngXaTrHjqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
رومانو:
رم در حال آماده شدن برای سومین پیشنهاد رسمی به وستهام برای جذب کرسنسیو سامرویل است.
پیشنهاد دوم به ارزش بیش از 45 میلیون یورو نیز از سوی وستهام رد شد اما رم قصد دارد امروز دوباره تلاش کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/101306" target="_blank">📅 13:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101305">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=dwkHkI-O3TpJ6P-dLHrFf4aT4aqajqduVksM4zedNyt52YsOL9v0sSkBxumdkX_jHUALn6NaetJ28DkZQ_y-8g_TePJHxRuWbQMLa1hrCLHJI6ShS0NZyTOYOBqVS9MDkVTKYSBG1OcVk7ijGSVa1eUoDrt_6mstco7IjyYsAXsn6J1wbZ6jK-1SPLmUOvAnmXBkLZGYgZ6xfLz7fORYlurzoNjHDycdrUURwvibe3DmRezdj6kNfQhLKuGAT5w7p6EYvEis7ATClr8bo-DeU5RkCA3AuIqXcMAaRyPJZVFh2WIJPKLvz3rwTtQM8HSvpx2XICiRS3MfILqNGCGRow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98cd4848c0.mp4?token=dwkHkI-O3TpJ6P-dLHrFf4aT4aqajqduVksM4zedNyt52YsOL9v0sSkBxumdkX_jHUALn6NaetJ28DkZQ_y-8g_TePJHxRuWbQMLa1hrCLHJI6ShS0NZyTOYOBqVS9MDkVTKYSBG1OcVk7ijGSVa1eUoDrt_6mstco7IjyYsAXsn6J1wbZ6jK-1SPLmUOvAnmXBkLZGYgZ6xfLz7fORYlurzoNjHDycdrUURwvibe3DmRezdj6kNfQhLKuGAT5w7p6EYvEis7ATClr8bo-DeU5RkCA3AuIqXcMAaRyPJZVFh2WIJPKLvz3rwTtQM8HSvpx2XICiRS3MfILqNGCGRow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
خداحافظی جواد خیابانی با مسی و میراث مارادونا با شعر مدونا: هرگز انتظار نداشتم اینگونه شود، برای من گریه نکن آرژانتین، حقیقت این است که من هرگز تو را ترک نکرده ام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/101305" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101301">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kcYrkk1fMEOrWnytYoWHR9tWk7H_ZfFfARjGouiesdrsy4papnyiqC3UkN_rJfZCEq3Wc1BznLnu60RI1G_3xJKzGT3k68_L2586g7malFONrKKC-nXMf_kCPDUBhC8NzlTNwmAbcGXeOhb-GyIBvIyb2XYUMCE0CoxzJgpBlq1HZb-tCR1QDTeisala7n3lip1SDl4AVhmvmhq67nSNyYkI_TtS32T61G_dpZRA49vS7Uy0ALjGrLgCQfQuWfAaNrQGWF8-L8QDWNtIVMzio4HWTMn0DS0AhYUSRJAZXuNmJDrsu1Em5x9fAQHGyXPOtDZr6jYpZiqWKfiZCRnARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UyvT3g1IZcMeguRyse6R2DilUiRM-Foh1fLmslXRvBgBBuNBerPipBIXXKlhJJXd4Kzfd6mMKZo8QpaPvwFg21cYFvw37xj8YO3HyypqX-R0xu6CJxMq4z1U47GOaErlTDtyN-r5u2oDfVX8xsEmUjZ0ZK6wxoaQB4KCrrL_U7FHEfYuHcJOlanJPxSf0fFGlCdCIt0sDoq7MnoUfEuPGr35xJ2LPtHtdkn-FTg5P2Qv1eLHndiKf7NZeHCggc5Z35Ox4UyvfHmvJy-xOlPq4xzRGnn25xPh9luqi2961-1AtAlYPdKoSz_zMRwk_-_O3Doa985-_r81Z8IXBsRbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WmeCdKuptVleB2k39uy6CgkaTKL1gaFr9Nb-IqXI6jhvx5ej1uXSj0GK_DO2iswbspwaqWQT9ZoZD6dBkqA-UTppeuQJU008pVeW3xzI8uri-AvIkRYHM2dauJjIRcrvSMdJKg7EE9lKrpPyrjOvNhFt8_RjI7WdeP32LQT3jkmVZPK58lVwheUJ95F53FHs1jqiYC2Vw8SucU3ALn27y7xWXsOeQktAuLsPypp7Rjn95ed8_y_x7VUXyrCl0PgbAaYziS2aRhkEIoR242kfFNlBY8E-gV4dfW7gkPPTh1qEGpzg7jhKe1ypocfB1C371inAIpCsTnzJ8lc273YLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEaPK_nMydDIZrJtnVAtuKQEX_w_B-By0YTFhKTSLrYtoYzdWKeluXUTkYCTcJlYEWDkbQmJlROOKtj8MWM1FcFyKYQWEC-PAgKja5HD30tswGOMR0HPAXsVpHsfllTDE882dlBzZc-pd5_amQJQHUTkB6YoZGmunF3XibBIoCjkJahHEBQcTy8ehwhFdb1HyovQxTKm3a3PnZe6-RcX7e3KpTIMcMzMPscojizHYyFDRNDozc4FfdijXFvgVMbItJa6NzMym2KpXkZOxG-2tt4sa53hpHWwT0ggfg1kglrBRlsm-BY5JGx57U4sPPOOK3OHwNEvePVcWnbzZgb4sA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
👍
پائو کوبارسی ستاره ۱۹ ساله اسپانیا و زیدش بعد فینال دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101301" target="_blank">📅 13:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101300">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad81ee87a2.mp4?token=vU3ZyT6sFDqQfH5Qn7AlptiIP0c5_3YfvT0ujknm0TjdtvsWRF3xsjQdoIdbPatkm0jpIeXo3kKoH7uxbKF4YrquTsGbieBen9YPPs39aj7KXHoLZES_vIj_x558Nk8psLeA6_j7WGl-jw7FUbxZWa53cSQ-p3THlZrN97eKxAff8tjQESQ3iLiPqSZ3xgTjNyshuhArFXBkG4QvQ7myPoQKnkBG6E9Vq9t7FdvhJKuM5WwpKgkwVx6Y1qo-7vV5H0sErjHGHUZCiKj_lAlELteZ81xOLGyn95qWZAnQTYC-Fn4oPU39rQLm503UjRnGyZ9Run9y9oWQoRnkDcwuaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شما با دیدن این ویدیو یاد چی میفتید؟
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101300" target="_blank">📅 12:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101299">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qpwg2MyBwqDN6jC7IQY82S3Obh4gDn95PYcKJFnB2oj_ky3YBnPLWs1Ze9Edznq_oQUjYWyBO2ZtaDPqjkdhzrqwTjYe4vkfF5omRPl5k1w5xzbtWYs9EZ8C38mHEgu5n0XRuF-892v1nPPzmyF2zC4U9dSp6oqmgRX3225eYK1arANh6sdP0WjWV3Rk1CP3_kykJ6_Q8ClQUh2wIFFCVQ6Dp1-xBZEV5z2cur9DRc7SV848YQsD1VYcKYvNFt1AuRb5TsFhLWelvEcvA42xCXII__wAEVU9gx3gLWGkhZjG6AaXCpXcg2oV8LIEL_xVsaPETxAih6a_CiZSKgHw6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نوزادی مسی کونش رو شست
تو دوره نوجوونی کلی جام با بارسلونا برد
تو 16 سالگی قهرمان یورو شد
تو 19 سالگی جام جهانی رو برد
این وسط هم بالای 10 تا دوست دختر داشت لاس خشکه میزد
این بشر دیگه از خدا چی میخواد؟ چی روش میشه اصلا ازش بخواد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101299" target="_blank">📅 12:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101298">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5934b1abe1.mp4?token=U1-NiThxVxsiJpMtAfWANJbVRcCFJ47OitO-F03hGLyzZ_s5Y-GQRNaTth9hdC69VIGJ9zU8qiOUSsZtFmcZNqoOJwfgrO1-2lRNC1Z0OSjb_KHc5OCAzYvlj5ko9RHBWtdIlSqeEDAulkEG2omMpugVLifq1l4gUKBmNas9CU-Qio1h9OBEDbQnTLjdTW2gqLveDGYCHLBmreA3HtVZCMzaKKLWlPoYa87H52OtkOJ2BUKIyIOxJo6gMPBGQcis4AEDmjnk4dHLiJ70iw7O902qqDtyZj1OjtKr6AEoKK4PlSdE1dMyGZpc1xIUjaY38nAFkxdtgiMIbBrW2eoi6HjQAXDlq7FwoJnjlXQR-1p_MSzKbXDPWTYU_y0frpBgRSGOPOOrKA4j14XMqYGABgP1RMehALpk95PAg3t378l1ShMq7KXQE3WR50VLMzMQTcHGsFK8aYwM234Oe4vcCxN_yJdVUXkrZUUQdMGH7cyG7XGWJt6nT_MNu7h4wM6QQAbeNaaYYKL_A06gwTyqXuPqIKKGQE7xIKZn8QXmfV_79HSpIQYAEEEF1OP8yuR4jj5hizsQG02jvY5G7_tYRj1dkmifT3ihq8DVUBT1bhJvwF7UT-EJkfsPT4qeSjwtHPnSXpGLyn0epclEqCa_Xtkms1bjwqWYvrlnp6Tsdug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملاقات اسپید با گروه BTS در فینال
🙂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/101298" target="_blank">📅 12:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101297">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/242475ed92.mp4?token=g4aaZ5YMb51i0AJF-u2Vu3W-LZ28XH6v_woqCIDHJ4sct3qwpjfDTCB1u7X8pb3XGiL7YkNVgrxRkMxlZBq8j_JdI9HFrrqrmOoo-GUSXalhNtihNcggwJQpqEvpjJyWtV7wkZXDK30iGOjKfbBoLfN95UrXehjAf5XenDBG09cEYxco7hyVHJ4tozzrw9QYOvidyZ4Pgk0IARpjXlNVjfIcQjVn8ON3sCWhBhZDiQeAqZI_EmRc8J5TAQBsR-kfxy5-M4kG9Xl465y1ID-DFApE8VL37hGgjSf4E8jeWKYw1dtzv_V-YXdSJhwXQc6UxeT8xYnIzfYwvSiNNbmEzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکوریا با نایلون داره جام‌جهانی رو میبره
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/101297" target="_blank">📅 12:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101296">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c93fe59da.mp4?token=OszNyOe4N_rrRXbpOgfBcQ0oOSF00fM3r95AbPRJGfQoolSLs9ncq2esyzCnTIFaCCt6j9OgsSrt4yHElQ4pPgIKYS4TlLNqmDl-ms_TPI0chmCFRUxQmlpS4gNmGnyp6Co5ieMkGaboBGF8YAobfCguJD3AuHXky78nqNVKSeWXtAc3BJALxx4vCTOxQShpgwPsn56e8RKrlMDOBfBOUinIXtpu-FSxa46QwK8nT0BBoTKnccVmQIZkA5PUKYGRSFna87q1UOWcS02J8DZ8aHCCZ0nblHG5TYVbhWZZ7Gi4I12hS-PtNdEZ3FCSQ5yc_M_O_u47Ga9rGUsurIL8Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
👍
جملات عادل فردوسی‌پور درباره آخرین بازی لیونل‌مسی با لباس تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101296" target="_blank">📅 12:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101295">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bE7FWcM0I8dJey0Nu7yIcqk9jBL0gNC-whKKhmR9TCnPXx84WvD_Q_2O3Twmeh2iVjj5DBp11FWZWceS-tm-dE8w7DNCw688IG3XrkmFZfmPUUyvzyU79U9iNYeJKZfKRHBkvMeMekmdUtPTawbKTyPqMsG6HHVWXBdyfYmpwSlvu9h1BLTIa3knFNwHovQJ1eYpTNUSLnqBKKpiaFsJgMJRGqFgayeYSK-l7OoaThrXE0qjlGhP0J_R4LTnfp7VMPt2FfBt9dSjQNmcUOi5-6gsf2xzH85-wR6tTxx-o42o2A0dRYfl8T6ORmxFOTC80Se1TLOSPEuoxN3KAyHZnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😢
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/101295" target="_blank">📅 12:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101294">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln5jV3xM5HwlD_1Q_dfaWdh1YOkBfGXKUCvZKOAp_c98M5ccaHXRErF0LF2XVubK5EHhZ5B6GREVeUDItBxrPLI3FjaPAIDFgrJWikHaeusHEfP0VBxYJS5nBZ180EgQJZycqr-VGCwxklRHEzmGkrE-28Bgu71ksAD0y4dauCnuqYmKAAI-J6UNZxmpFutYpm8CHxWKlGkAmRRjSmSnkblawK9RqvB6uYpoAU8EfNNsAbaEWv73ALSGNMbhOJe9WcNHNhjvW_qz_YUVic-qlL0_NVxPjM8wYkyWaLLLbX_NHWr--AUizbv6jdHXHdVK3MGKHqcdUjBbH97yuktW_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
👍
لامین‌یامال و بانو در مراسم قهرمانی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/101294" target="_blank">📅 12:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101293">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9dRi6G5upGGG_GoS7ja0PtsFmDTrqg031JS_uBICllsY_SYiHFq96Ez6y3iivXOdF-Z-LqrMmALXewh04nNsCkY-RItHbdu0SuX3z0ngJh6XVO_cbwwqQf5NukFC2Y2F8FkOc-AhKOZ3oI5LkoxoFDoQaIAbfwM_ZEZhv78mQC3VhZJ9oFtozzDhYF37Cv9B88nSFlj75Hz4aau0rHM9pds27VZpEWUOowfjD25GlrCm1i_M7qXaBnk1-RH8rBtE4EaIiEpayPhQSUGTf7GAXEFiNNxM7ZBLV5eA5hx0wy0Hcz-MLq7DK2DjVX702nxpcWKdpEt1aYRT7ViQzkKGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام‌جهانی 2026 از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/101293" target="_blank">📅 12:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101292">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTahRu3vG45Ezwt1_th2QSzlub0gNsN3csR7JB8-0uyP_5LXYjZ7HuvQ3V2tVriW1U0J6mx_QMq6iKrok2ttagcevho44C2bIqh_xTcQGVf8wGfzTJwZ7xYpkdhrA6cKc57FtCCymjJ-4btjG97s7mkVO2OpzhLKg8vn0arKd5B0RBhRGn-wGF07zCwb4MDTU1lRAK5YXQDsjjdZi2T0nE14YUbEZNwLuSHuHObOqgQya7j1i-dZ89t3v667-zAFDzI6OU6I383cdT8BRlNMn_XbqgCeFD1TMAhIrJAvMBowuu95CM2556-EmPzlwFFCTWraa_SIuVn8tZ9HoL2fHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وبسایت سوفا اسکور برای دومین بار متوالی پس از جام جهانی 2022، لیونل مسی را به عنوان بهترین بازیکن جام جهانی 2026 انتخاب کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/101292" target="_blank">📅 12:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101291">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su5_htAznFZ0z_QE0hPfDkUkR8c2VHFwUXZ1EQlOCrTkZ3V33Oz9uPgGntdiQdlr5nISKRVy38_JSPsXL82cgYkNyjhfm88ER3hqrn7YiurMv2DjJNRy0WDQ0bRiJIw-IIAyof_yH6KBINdq2duGqhhSLtbyPsn3TaV0AFIJCzS5N3Fo-W1NrMzc1lCHRbKyXPoGGQfpd_slWV4kRrlVB-v68XWXGW20-bakLn99JSf0610wQSJ0-cbmy7bOsXWKtSnEWD7GihZ1zSF4WVlfpU4M8zEdfzr9tl9t5wJENQsegZ13N9oEyb14jRwk_AtneXmg7gQ4cc0uy8JxUlu2sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
پرزیدنت مسعود پزشکیان: شادمانی ملت عزیز اسپانیا، شادمانی ملت و دولت ایران است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/101291" target="_blank">📅 11:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101290">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AVHpa4Qa42FUXUL7Qjh6eYDHdPNpELyhVFdfLJ2oWDkxGXaUk2DX2aqR5NHKUB9Cxh8GeywZb1299DYtM5DHk4S2d5KWEaYW0eHQqvjb_RyPnYLnQ9s1l9hbEw1H1z-py572OYHTZR3sEjB4Vzm1WfKssMyyNyLQsFsgZDspTyXb6df-3s90a6hHFPJ9MMCWD0b3b_mImEY-lrvWhF2E4XzaSH5Ock7EUoUByHbH-7fy1ofVuhFylOWOkjDK2sDAr8EhJvMqP2T33gQnlv0Gcz66rv9BchE8Vh8K6oBhDgGisFuOPRE_R8083Wzogs11pzREUUtYrFfUPRLdWRNkzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fa95c026.mp4?token=AVHpa4Qa42FUXUL7Qjh6eYDHdPNpELyhVFdfLJ2oWDkxGXaUk2DX2aqR5NHKUB9Cxh8GeywZb1299DYtM5DHk4S2d5KWEaYW0eHQqvjb_RyPnYLnQ9s1l9hbEw1H1z-py572OYHTZR3sEjB4Vzm1WfKssMyyNyLQsFsgZDspTyXb6df-3s90a6hHFPJ9MMCWD0b3b_mImEY-lrvWhF2E4XzaSH5Ock7EUoUByHbH-7fy1ofVuhFylOWOkjDK2sDAr8EhJvMqP2T33gQnlv0Gcz66rv9BchE8Vh8K6oBhDgGisFuOPRE_R8083Wzogs11pzREUUtYrFfUPRLdWRNkzoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇪🇸
کاملا جدی دیشب پرچم اسپانیا تو تجمع مردم ولایت‌مدار مشهد به اهتزاز دراومد
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101290" target="_blank">📅 11:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101286">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEFY4k7AyMcaqC9XvMANfA4QVDuV3-2BuhZsd4BDYdKLNTULS2bKZs1bY1HOKuKPTDmNk1mnxb6LakD7w4fkP5pb6psV05fKUYTITfyvMX0oXVp69BJ105OwVdrtOyV4HQ-B0BTaAmAFVR-t1y0Sd4I9Uk_bw5gnMC9zLRtu_L80-DYubgJvpFTDI3j9SRRW5HYT_IXfXr-GoyPyvUIN9zsV3FeTXdyygGVcvs0fq_sKnCxxd0a7zvUBCmigJetfo1iTHdTn6HtGxDlD-Ba2_ylxqY075Vwio6wBamjHWIaOMw5AT_Msk4XtAMUH3cuI8yOPAJsC5M0DhWVqv9lwBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bbABmLv4y8H0XfmG_SkfTcehZKUurU_OHOPaxzmStTovYvSPTsHrGni0KhsAoU3pfTCVI00NkW7Hzf3CrZ8r3BOh8JoOLCVINtT_Z4HJ3q7SDOMNpbI_eRHozDfWgOrnTI4_QDb4FqvZjW8Q23uY4Zr9fH5Luj9pXvtvNGHx8Aawoco1CxiXjvztsUI9D-PFyDw_M49zkvXuNCfBniJa0aMGjSEJCNYVsLpAQ6iwAk8m9ADHB3PEh1iQ4sOmcHLATx_tcrfE1bglD6XuLCpxvfgwhkuNOzy-oUvr8as5jqTBWvNPPBVpneTY5FYmwO94MlaaE45jdpa0HA9E23e_Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W7AUIcjCb0Ak0BLDvb8VKulzLtNsR4pyAHxVMuGvNs26M7g8F55dlY9Do3f-sB94DdSgN9ECC6ZDBrAuxOq6mlASekhDHz2UH2_VZ-FXBUdIBENgYCCT0SurtCLPO3bjRpsdPG_sq94JMAxkpQs4GpW6XPx_cAxUvWumbVa_iNa3FDyeDcONmQS4yClwP04WOVvvQOQXp_rn0JTlvb7yxivgSFUONnn5x8zbtU36NI0rsQwpZbflAOEyzNF1-ezZM-WlxZAyvMD0PxpTJjZlwhJgg-MAEtM_z1E1r-LpkfxEOSkffWH6oUr68p2iyxb7BhVwtKS8I0kR-PPJ0MTZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K9XP-UaRMPAQy-VggKxZrirNGZV-yhTSF8dLsaSAdXXy5wNzKlAuR-Axwawv5RJxEMkPIUsF-kmrmHDSVMHwDaLNrKIFzFIJ6l-Nzi8z5snAYnivaQFsq7dJCgSwbPy1PeIBPAyDiTZUQSuyaFWIYCbUcyB_XX2YzmXXzo_n2MV12-bKYYcW-e6T6imFYFhY7t0uGI9-U3i_5MA-uAaNnlzb4gNCnHar3fe2j_I02GoOH2QTOJBUx2LY_veCjnn7Lu9wWO0d5cyI1RgyOdtzrnsF_XVwg-wnMmUt3NP8riGkzJnP8-Kq5AwIwwo_Nnf4WVRbbKWgJ31EtiMNU67gJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
رونمایی بایرن‌مونیخ از کیت‌دوم فصل‌آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/101286" target="_blank">📅 11:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101285">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=QwLAdSwof--mpVq95DmTZsZ8XdHfpA1AswAkhWZhBGUyvrLdPzUmBRF3kMRnwXkGdGT88xJoZfo_Ibx1XW2LkbRJqjX_RHkw5Etsq5be-hJWLOTdslhDx-ULSCNb4-WCbpbP5VfW-5Fx7LPsCuWgkrxhEIcoUHgMjfLb8MKAjH062JLaK2hm1_Jm0wSZFlXV6b5XHyMNFOS3JlR_S4oqNvV8vjKL3rk70ki1aRTZISxfBEVAX2yOGzCM96A7u9Jf4cn-HIKaup3e-rb2Z7QjQlw5VlF365nWyX2OAHII-aj8nH7_DntEUXcPsniJbifJx0vv4uFokrir1wO69gSxmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33ff615c2c.mp4?token=QwLAdSwof--mpVq95DmTZsZ8XdHfpA1AswAkhWZhBGUyvrLdPzUmBRF3kMRnwXkGdGT88xJoZfo_Ibx1XW2LkbRJqjX_RHkw5Etsq5be-hJWLOTdslhDx-ULSCNb4-WCbpbP5VfW-5Fx7LPsCuWgkrxhEIcoUHgMjfLb8MKAjH062JLaK2hm1_Jm0wSZFlXV6b5XHyMNFOS3JlR_S4oqNvV8vjKL3rk70ki1aRTZISxfBEVAX2yOGzCM96A7u9Jf4cn-HIKaup3e-rb2Z7QjQlw5VlF365nWyX2OAHII-aj8nH7_DntEUXcPsniJbifJx0vv4uFokrir1wO69gSxmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچارلیسون بعد قهرمانی اسپانیا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/101285" target="_blank">📅 11:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101284">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=KUezX73NxLGVAIojJkAseOqGwb8pPPc0XDQLhZrmMIfRjg4bBPCObkwz9O8MlpAwnOJsSTXZlkVI2ICU9U9YzkEZmt5hS_cs5CTfHFEbnu8VPDFZ12FrpRbBX-X9NrRXqzh68gA3Mk7vrpweEJhCM-2Fx4k_aOkf-glQHBgSx1R27AzBDPLqetMP5jb1w_B0wZ0d9NTdllzGxXy-EOXhXrU7k7tM987h4Z-RSLSPNLLBX398LP3OUEzsBrpeGTOHGZmD42N2Mp3DH0_CgXfAnBWmlzTSA9yh2qBx5KBj2nQjUsdsK25tN2KyFBxRTbPcOgeQujsC1uwd7ujUFA3t1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e24a7448c.mp4?token=KUezX73NxLGVAIojJkAseOqGwb8pPPc0XDQLhZrmMIfRjg4bBPCObkwz9O8MlpAwnOJsSTXZlkVI2ICU9U9YzkEZmt5hS_cs5CTfHFEbnu8VPDFZ12FrpRbBX-X9NrRXqzh68gA3Mk7vrpweEJhCM-2Fx4k_aOkf-glQHBgSx1R27AzBDPLqetMP5jb1w_B0wZ0d9NTdllzGxXy-EOXhXrU7k7tM987h4Z-RSLSPNLLBX398LP3OUEzsBrpeGTOHGZmD42N2Mp3DH0_CgXfAnBWmlzTSA9yh2qBx5KBj2nQjUsdsK25tN2KyFBxRTbPcOgeQujsC1uwd7ujUFA3t1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
🇦🇷
🙂
مسیر آرژانتین تا فینال از زبان عادل فردوسی پور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/101284" target="_blank">📅 11:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101283">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=YAKyKK9ZtKE3ceKWC6GmR_eCVqDhlmm_pPOhbZvqoJ0XqNZtJ08uhsG8BqbRjNa2mH1RfZ8QTMTg0HLcQyxnop-C9Y1BiUPROqboak4zp7RXhk_uRoAKu7F2S2CBCe7j6FohdXPHWbi49_61MDJ5mqWiPPo-jwrQbDT9DUTAjoYwZdZE92ef5j4F_WqPHHsuoPf9ii_1qvKC11-IxjwoEWjcpgpKyXA0USfIqMS4yKq-D2v4XOEY-hlkemTAYYaSA_jqbYwaPW3TUdomHDpMtc4hyrebwCrEm4pePCpM9fC6w_5pMGVyQCyX6q-qGm4KExoUgsIKlaXMQNXPdNt5UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05de87eb61.mp4?token=YAKyKK9ZtKE3ceKWC6GmR_eCVqDhlmm_pPOhbZvqoJ0XqNZtJ08uhsG8BqbRjNa2mH1RfZ8QTMTg0HLcQyxnop-C9Y1BiUPROqboak4zp7RXhk_uRoAKu7F2S2CBCe7j6FohdXPHWbi49_61MDJ5mqWiPPo-jwrQbDT9DUTAjoYwZdZE92ef5j4F_WqPHHsuoPf9ii_1qvKC11-IxjwoEWjcpgpKyXA0USfIqMS4yKq-D2v4XOEY-hlkemTAYYaSA_jqbYwaPW3TUdomHDpMtc4hyrebwCrEm4pePCpM9fC6w_5pMGVyQCyX6q-qGm4KExoUgsIKlaXMQNXPdNt5UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏆
میثاقی درباره عدم پخش مراسم قهرمانی اسپانیا: «حالمان بد می‌شود وقتی مجبور باشیم چهره این جنایتکار کثیف یعنی ترامپ را به تصویر بکشیم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101283" target="_blank">📅 11:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101282">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6kyDjGP6VgPPjUzf-5U0xsx3mwwBVgapXeceiTKdwA0yWzAQDOYW6fOZWA5d-hkd_HaS-CdefscmOr95Y19Tm78Rh1wpOUYg-c6oFyxwhC9Gp9H8HMCS1JxxUXVWuRhPgLru_nAWA92NRTU8-98mau_5as015MiVBi9B07LK8_MGx_mqEPTbpwTOnwBXFI5JXLTtaYkghT6xvrvYwphezLMx1f6HSilPJLWzZ8U9ZXpTs5IURtHFozYiRwvx2R94dY66yiwFtO9g6iKdlWx6sthTPzoPHZvW2ZUjfpUJKMnUa_jCqH8YZ8vI6LeAoUlfI0Co5NPYEE5bEkHVrp97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لامین‌یامال هم سیگاری شد
😆
😆
😆
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/101282" target="_blank">📅 10:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101281">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DF09OHzZf8CpELnlK_TTy1LtN9jHxUhKkJNM-7yKBru0eG7gc5Y4PEROOMRTLjVc7NeeA2OXAIgsgvbwIv9GLitN4of3ZWMd6xVlvS0f_C2suhcmiKLM_gxIBVYn7PTnO7o0BED7NRmo95yghqHxZ_7Y8G83BidnYLzWA5paTJXlQ-4bCvTrORFuPSmDwewFt1yzIZyCcpq5hzlz-DQV9wmvB9tmf5vbqxZAStEgRM1Yz0pxJzvDrI1EwqYtu8ugfIr6WyatUVkuKcKBNZicVuZ_-KEFZIJKm501b1cPCqVsSalSkfQJ5tGENiCaMuv_yHPVOWGjy3lC298skZsG2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇺🇸
🎙
دونالد ترامپ:
"این یکی از بزرگترین رویدادها در تاریخ بود. هیچ رویدادی مانند این وجود نداشته است، نه از نظر کلی و نه از نظر فوتبال. این رویداد چهار تا پنج برابر بزرگتر از هر نسخه قبلی بود که توسط فیفا برگزار شده بود، و ما به کشور خود و به تلاشی که همه انجام دادند، بسیار افتخار می‌کنیم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/101281" target="_blank">📅 10:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101280">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=V9nzH2xMBwzgE4TQhC4wJsm3idfkAnhPja7kNPAmaIU1a6KywriZV03z7oQo7_7AYyKef8A5bYck5U7KTTw3SNpnN12LyZ8d-ZzGc_GHTWvO6AF8rt9IR34QxgQztterWNLFKjNT2O4z9Nmmu3bsDHz-CIGMFw_WFXZV-PEGL4cwTP_QEUehgqxIUE0GhD3LXNkNiejlTdcoloNlIZynis12Q09S3xzwpbiInjGKmoQOyY1Dy9CDbiMJyNhIIVOaKk0l01lF9WiRnsbRGmUgEu4galDl8akarn7teGeffwYZqMJYMSqUQ9R9-fUaUk1n8uQbXIgN--1WDnKAMjmnOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28c62d68d.mp4?token=V9nzH2xMBwzgE4TQhC4wJsm3idfkAnhPja7kNPAmaIU1a6KywriZV03z7oQo7_7AYyKef8A5bYck5U7KTTw3SNpnN12LyZ8d-ZzGc_GHTWvO6AF8rt9IR34QxgQztterWNLFKjNT2O4z9Nmmu3bsDHz-CIGMFw_WFXZV-PEGL4cwTP_QEUehgqxIUE0GhD3LXNkNiejlTdcoloNlIZynis12Q09S3xzwpbiInjGKmoQOyY1Dy9CDbiMJyNhIIVOaKk0l01lF9WiRnsbRGmUgEu4galDl8akarn7teGeffwYZqMJYMSqUQ9R9-fUaUk1n8uQbXIgN--1WDnKAMjmnOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
تنها موقعیت آرژانتین مقابل اسپانیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101280" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101279">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=WHX3VBMCjoUrfhtAclX1k9xw1_cm3npSBdohonCFgU6hGzHBw6yCh_5t-tr44gv0GsHH5N6pMCcJbUWBRDcjthqYsmrbzTkxRIGMNCnNY7czBWbOfhPgdaGuOqwlghqA-3xGCfo2tddWE_8FHRWDhPd7CsjObZ_giFXpUuMgfkYzKochKhm6Y_SQyTIEqxr_AZbrE4XP52touEf_zsVw2cYLlwBnaStiEE35hOlONe-pS1YZ-h_XrRQZ_KNlnlaRjj3tJ4-LB1oyuwLQjJfb4fhXcW2Ei0zjWqfswCtTuJBpdNNCtyuAktVe4V6w_slmD4JIenIfevdNr7Cxb_Tm8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf91e3776d.mp4?token=WHX3VBMCjoUrfhtAclX1k9xw1_cm3npSBdohonCFgU6hGzHBw6yCh_5t-tr44gv0GsHH5N6pMCcJbUWBRDcjthqYsmrbzTkxRIGMNCnNY7czBWbOfhPgdaGuOqwlghqA-3xGCfo2tddWE_8FHRWDhPd7CsjObZ_giFXpUuMgfkYzKochKhm6Y_SQyTIEqxr_AZbrE4XP52touEf_zsVw2cYLlwBnaStiEE35hOlONe-pS1YZ-h_XrRQZ_KNlnlaRjj3tJ4-LB1oyuwLQjJfb4fhXcW2Ei0zjWqfswCtTuJBpdNNCtyuAktVe4V6w_slmD4JIenIfevdNr7Cxb_Tm8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
و حالا پس از ۱۹ سال، لیونل‌مسی ایستاده قهرمان جدید جهان را تشویق کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/101279" target="_blank">📅 10:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101278">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=Q17qjDQspUIxpLuVU8OWEAl3L0gdjD_-MuZ2tKAQTTL2Hwk5ds46U8VALnYTeRkVSJWccDvl6_IiBB9tmHl3wvA9DoP8qSaydvgq6s_68CTlFprKWCK0eQJ9Rh7LA_CRN_gXZE7zVFbF3L72D3-7DXtFMnQ2DFNAuhOrFD1Paylw8YctSjOocd5X95FMiROvgctkBAY1ao4QMEE_d5zOG3Lv9XcF1QIIc9YZLo6_RN37uiTzHoo2IACJ9MnathfjiehlC6i3Ynk3_f9Hw1imiMVBT-LZ2BX4XJPMgDrauujG7miSUEA6CptnSxAomZNVz_QLi_w1HtgGwn_HuBJ_mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3de45ea42.mp4?token=Q17qjDQspUIxpLuVU8OWEAl3L0gdjD_-MuZ2tKAQTTL2Hwk5ds46U8VALnYTeRkVSJWccDvl6_IiBB9tmHl3wvA9DoP8qSaydvgq6s_68CTlFprKWCK0eQJ9Rh7LA_CRN_gXZE7zVFbF3L72D3-7DXtFMnQ2DFNAuhOrFD1Paylw8YctSjOocd5X95FMiROvgctkBAY1ao4QMEE_d5zOG3Lv9XcF1QIIc9YZLo6_RN37uiTzHoo2IACJ9MnathfjiehlC6i3Ynk3_f9Hw1imiMVBT-LZ2BX4XJPMgDrauujG7miSUEA6CptnSxAomZNVz_QLi_w1HtgGwn_HuBJ_mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی دیگر از جنجال دیشب پاردس در فینال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/101278" target="_blank">📅 09:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101277">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgNFVRhq9SGNw6HOoFtbP7p3-5R1-GHPfXeEVYvorCZ0no1SNJ_npW68GSPDX-Kfwfk8CpGOwY7qlCGtOxHWWn6Kf5Y0iIglQVwz4P6m9oQ9i_44meYL_10Y57OB720rIp0c3dTGcDCfYFRq_uXUiUTi7MizdFdR7fdYJsbQ4d26jClJdlgl9Z_FzUG-QyiAVPjz7ozIY0j6_5zgbMQXKUJPKZSLtEokUJJxXvH_pHlEGY69erWdhQSnxCRMpfG-9SaOLN5q5ibs2JHsGEX2hDJ0geqeKhC5R7WpEcz_vy6pnwblvGhF3kFakLJU7xpuGwCKYwstKsfIAa9EHC9kmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرنوشت دلافوئنته اگه تو ایران به دنیا میومد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/101277" target="_blank">📅 09:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101276">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=QY35iZr8nxErY3ssM3EANpYsQuGZzF8GLIEosOKJNe-K_EjfDP-ukYU9kxRgUQJP6udCVUDrDov0K0xtSx3PTJOCp43X_uoFHQ7-MDQ0q29dNvqb04msuzB9eB6kOpwro388DeCrQrXLc01v4eYW57G8Nfh2dVy03kUrXAfjWie5xwI1i2z_7wRf3e8gzsu79PljUe0rNswDKn5xuwwbB8PxEmTu2_ukfLd5ijFIioi5sQaH92qWsDB8Yfc9oNgFwcWtCn8gLbKi0U3aNWZfnVsShccUut1SJDBN2iJBVhBHj0JCoSbNEJGLpOAcNHwvqgHWLtDm4nFfZoI8aOOH_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61d46d00d3.mp4?token=QY35iZr8nxErY3ssM3EANpYsQuGZzF8GLIEosOKJNe-K_EjfDP-ukYU9kxRgUQJP6udCVUDrDov0K0xtSx3PTJOCp43X_uoFHQ7-MDQ0q29dNvqb04msuzB9eB6kOpwro388DeCrQrXLc01v4eYW57G8Nfh2dVy03kUrXAfjWie5xwI1i2z_7wRf3e8gzsu79PljUe0rNswDKn5xuwwbB8PxEmTu2_ukfLd5ijFIioi5sQaH92qWsDB8Yfc9oNgFwcWtCn8gLbKi0U3aNWZfnVsShccUut1SJDBN2iJBVhBHj0JCoSbNEJGLpOAcNHwvqgHWLtDm4nFfZoI8aOOH_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گاهی فوتبال فقط یک جام را می‌برد، اما بعضی بازیکن‌ها قلب میلیون‌ها نفر را برای همیشه فتح می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/101276" target="_blank">📅 09:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101275">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJhyqX489MzWGrjCdp42e0-jr-gdRIOtaShud2DexXjEBzBI1mPMFbq-ZBnJtvQ9r1mVsxcU0dYjqRtNEA7l48Z5Th9lBuqBNFjqk4ivTe25NZkOPlyxy_Nl_ewL_xhZJoJsNVDyJ5DKe3iqiW2UagrP_W7Dze372cscYHJUVD9219AY03_cXZdWw6aBq8t24x9-1YCMQuR2SOi2_QME_3XxqejJXkluOCEkqI35W8huJOzuOU4Q38a1MlNOvbf2Bz5pSvkUQPlA9dauH6qsOB4ig08iCREBoctNKztK5DqLltUw9Bj1g6KNj_EP4W3tRbHnBAurFQkign6j93l7Nws_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a634e3021.mp4?token=sTT1u_MPVTsjWsarT4D4e3ELrzOXQ_e3JVGUgJp7mjneJbGfaoEy3rRfor52q0Ik3p1n4TNG4hcO6Vs0iorJnQ_9LqeTT8GRFpqaqSxYSne7DyrDOiqcoANgbgYLF4ltPHXH2SXIBqzX0MV-_3iym5LOiSJjHou_UXXjB_sCtUBoYzLYY6VIaMnC8jNuV6FNoYGK_H2S-YSQYlW_SRTvy8rNXbdhVPfcSpNbIPev31Ec1VqmEdmAw0CWKBhkQeG6kAlaBtdzu5eKvigAq2rAQrlmFGA7l6N1SQKsa8_ZZOURA3l7Jkzm2akkGHVeGAUt-tLULRVRZpO7UQEnv-TJhyqX489MzWGrjCdp42e0-jr-gdRIOtaShud2DexXjEBzBI1mPMFbq-ZBnJtvQ9r1mVsxcU0dYjqRtNEA7l48Z5Th9lBuqBNFjqk4ivTe25NZkOPlyxy_Nl_ewL_xhZJoJsNVDyJ5DKe3iqiW2UagrP_W7Dze372cscYHJUVD9219AY03_cXZdWw6aBq8t24x9-1YCMQuR2SOi2_QME_3XxqejJXkluOCEkqI35W8huJOzuOU4Q38a1MlNOvbf2Bz5pSvkUQPlA9dauH6qsOB4ig08iCREBoctNKztK5DqLltUw9Bj1g6KNj_EP4W3tRbHnBAurFQkign6j93l7Nws_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو کامل‌تر از داداش یامال در جشن قهرمانی اسپانیا؛ دیوانست قشنگ
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/101275" target="_blank">📅 09:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101274">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPsF2cUlQr1J9qTj09Ls7I0Ked4GcRlBh5WHLJ34zonBsdKV9OC04Oe8tqh1IPZvhlcaMj7KvKcoQp6MrbwWa4UXvv5r6Bsxhna61lu_h1lEC0FqzXAIH-TwHpnOdLdXH4dRs6EJjN2xV72iGOQZ6Ac8DWZNwN8O5G7m52V8TrYVoyywC70pUgahnDZx1qGBEAI9NaUcOcLbk6Im5Un7fuHCKGsOec6ExVgG_lQi7k3Wl7dEhOtjRLnreP1qL4h9P5dGf3WPjVpNIuC8FMLllXIRTb7AWvWfP0l9CM1nqFy-cxQW76Gn3GK-zv9piuOExT8Nw8ojpyJbN9CHPYU0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
رودری یازدهمین فوتبالیستی شد که قهرمانی جام جهانی، لیگ قهرمانان و توپ طلا را کسب کرده است:
🇧🇷
کاکا
🇧🇷
ریوالدو
🇧🇷
رونالدینیو
🇩🇪
فرانس بکن‌باور
🇩🇪
گِرد مولر
🇫🇷
زین‌الدین زیدان
🇫🇷
عثمان دمبله
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بابی چارلتون
🇮🇹
پائولو روسی
🇦🇷
لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/101274" target="_blank">📅 08:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101273">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=uLu4_RJmczouPiFYP4cBeepZ0ASO3UJSyylM4fIs-_8mvmnXGrejeLFey7Zp9rcYAvaeFIwEzGvpEEyqTgrRt0JQ7gu5Agj8ZAPo-oO8DQlCFOdQUrHF3mwzNuJQ9uDAqwzyaVMAcdwqDCx3t-Bbfc_KwzxCYFpjSuZN0LEkHNX_E1yRGxojsCH1ZAPV8aXd4llqRfFjaFB5UPIzgwt6WXd51XtpyClwZ9usZW01q0EOd6t797n4KmrBTbNW1v5Ge0oy3TG-Cq4y6VKXXs31wCX2v4hNQgPpO9zKrfzHckzknO2mDQgk10qnMyQ51P5KnPTwbfCMM4nMLux1ldIbDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deea9feba7.mp4?token=uLu4_RJmczouPiFYP4cBeepZ0ASO3UJSyylM4fIs-_8mvmnXGrejeLFey7Zp9rcYAvaeFIwEzGvpEEyqTgrRt0JQ7gu5Agj8ZAPo-oO8DQlCFOdQUrHF3mwzNuJQ9uDAqwzyaVMAcdwqDCx3t-Bbfc_KwzxCYFpjSuZN0LEkHNX_E1yRGxojsCH1ZAPV8aXd4llqRfFjaFB5UPIzgwt6WXd51XtpyClwZ9usZW01q0EOd6t797n4KmrBTbNW1v5Ge0oy3TG-Cq4y6VKXXs31wCX2v4hNQgPpO9zKrfzHckzknO2mDQgk10qnMyQ51P5KnPTwbfCMM4nMLux1ldIbDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیسی که داداش یامال با جام گرفته خداست
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/101273" target="_blank">📅 08:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101271">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vT65YSZFIJg6scy-M1CDAmXX7jqbmdkQpW39iNHFLn8nO1GdZZaHTXE6Sp5B3_sc5HLMp_ql6r4HbFrbJFO1ySJLc5OgJRlDb_MjzwLP1qsbfXGgnW9AHcfcjnGFoKSgdP6So0obJItnyzN1WpcR_3_aHcOvXSUySTGs0_sOSRzlpA3oJgYuOKXmgtoZLYags5S5nWIfyMLFtf6Qc-UCuM6qkRkglyQyxl1yQQXiWDZ-aHNWLc7vFA8UK-OlzE3gOQWsOWvoqwIStaI75N4UGIU_cCfdZ3ZJ31xbxLMLPgeXKwvVUy_nJ-hTB7n1zXb0NiuRD8umlp-8kNPHqaxJ4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AR1JjIPDMifFi8eCOyqOES_7kYLbm_ZLMU8rKwEFNqLNksYpdWNY48rZ1VtA-FpmFiM0o47wcm7dliZ5frG7tPV3fFdAlmdqYRKYF_Oc3FGgsglnv6YT704tjS9H61UE78z_itTTa6KvCErbP32DEYmNgORdsBMAy4gwo4wchG21ld2MxImgUsPzqt0slkuKt-DOVvQM1KmOFcRrFo8Q_VajLeX1WBOY3U8Ir4qQG1kvYKI68CUJaz7R5kPRDObtndTR2rCkMyj-BJlTI_2nZqG_5Rnh3DLLR5gjHXTaPNayVRZxUTfIoZVij5kfEeXlPL7mB7gXIyCWQoFhQpj3dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوبارسی و بانو تو جشن قهرمانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/101271" target="_blank">📅 08:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101267">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fcT3KIbsNgQ_-2pZHHD3QHtK4xBaSSBheMKuEPmcx1EYninXvTTYAieJ7ob3P4ymL-nE7OmN3gEejehAQxp30jg1KaPlj4r2fVCCMBcUhBJKxYns6rmmwvb1KGvnGHePPJs7S6QhGKwp0mj1L7jluXKroMEjdvxwEGJ3_uEs2iGd6LB6BgngAPn-b7pfL6XJnCp94Emw996VbXGtiNeSJVM2U5R9b2ndifdK1eAI8LSuh_VPJ_izOx8VGbZV7a2CkktzAeJ2kgJylKx8zbwl78Gs3CsE049CqdB2OuIIPo-eWENtkIME1VpPqlLG9Dn30xlU5Rj4lSLMyQHHGCgTHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RC6kosSekbJoWepDEs2yy8iAH8OS7PJv1_s0cIjt9RtyxD9t5jKRDFiyFvbgrLv9V1hzSeTY6roQCNetRMyD62FO3eYmCxgRWF3MhWhiBe7e12_gchcnGJRtVo2f2uoAFw65os2QDLQ-9DkHjnjFbFTeK8IxtxjinpqAqJopmRxirLiQbealln1qmCT8N6-v7F-8c323mtCe30OuKP3htrFAxffHwZGQkNy9id7QTSL6WePWRKy-3SSJVNMUp5-Ixh_PN5i5kxMBYcATsyh1ZpgQe8kz1TGDucMt256aVRKVss_481U_gtnYz8Hq-M02zTYF8nx352qwWdaO2hqSGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S02j80ZyuVTOYMI5zu-vsDpiQLscNtdJ-OG3TlVJPaU_kruKA8WwNd5PU1PvbTXx7HSUkWucFJzhvNDE976iIaWHwQllQ8pIFrSwUskWJgtTRr9NKWw0JiVF88QncTNczi5_6hH_IcNj4BNVA-f5crMZodaKfUfa7J-3oimeb6zF0YTwP4sSkQ3kLje0k8yqfpy_2wcz7JYlDI4OXTlw9oYo7MHmYkhbc2qFILVo5QL6McboIrPbFV57zmci2VDXcvfvX5dKEejW4M58AdOAe-Mnq8aWvyvjSLsOF7ClfJjCwr7cta4KMiE8R-01uTUyWXBK0GJevnm92I7-fSgurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bcv99adP0cdojdeIGRfDQv6k4iGv2BCp6qYZ5O9Mlz8w5YZ4VuAFm8FnwSum91IWyU1c0ZLQ_m157MOPKchw5KwnTUcwfFEkwfaD7eZB_AUyY0Hi_bdnUyXYVv_AVvzLas61IrCnLh2vAZ_iZGnHpQ8OcNSoht4oaGU5MHOaCbB7zvKhpT5veQWg2_CBV1XHxRIthp6XzMr5fb2vY6Cg0SJx0_DsgOof-unUfRP_S2GP6a1nExI0dfJ8P6nu031v0jIk2bvLll13oU5_2LIXID0LlzrXspcsce9kiHDf2aX9XUtYBfDLTUOp2YlLK1jUfEBbU9gICuqUGlvu6oYJVQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اینم چنتا شات از یامال با جام قهرمانی برای نیازمنداش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/101267" target="_blank">📅 07:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101266">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=T9L7dZ_iz1Oh18n1PC5clrfg82aiRnLBv8cE2GVz65oWkSo41TLn41wfEgXHOQhYFoZ7rL-Hha4fQXZXeCCTFf02KeMgnvx_FAUxjNxF5Rtrx7WKbDWd4CWkc8MKoe0gbBnyyct93XB89v6p5GcOidioZtEwpevgKQqSn1y45YQ4i3GoLtl2soWvUP_nh81RhzgPpxhu-Qk8VzzYBG1Ovvyce9wo0bBJ617o5uRnblfRhyzAA5J7iqsvcnUT8qdeeDmUhWNGA264K1_VTrmpoGiBtEIe_4bJCIIKyWU3i11gmNhHiRUH5Ez0R9LNoZczq_BRZEUZGWdbLGOfYywRUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79dd52c94d.mp4?token=T9L7dZ_iz1Oh18n1PC5clrfg82aiRnLBv8cE2GVz65oWkSo41TLn41wfEgXHOQhYFoZ7rL-Hha4fQXZXeCCTFf02KeMgnvx_FAUxjNxF5Rtrx7WKbDWd4CWkc8MKoe0gbBnyyct93XB89v6p5GcOidioZtEwpevgKQqSn1y45YQ4i3GoLtl2soWvUP_nh81RhzgPpxhu-Qk8VzzYBG1Ovvyce9wo0bBJ617o5uRnblfRhyzAA5J7iqsvcnUT8qdeeDmUhWNGA264K1_VTrmpoGiBtEIe_4bJCIIKyWU3i11gmNhHiRUH5Ez0R9LNoZczq_BRZEUZGWdbLGOfYywRUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
💔
اشک های اسکالونی در کنفرانس خبری بعد از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/101266" target="_blank">📅 07:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101265">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=TYPPXJthDJIkiynW4oigPsMpoUiY4HD7ed1OIdUIMsX0USUXmEfIuvnXeSVShQAQjzT-v52qcfBxq9CgqpbJUtaxEr9LX_O4cuUeEtmqU554WmefDyU82TipX1PaxCSDgAfYI-6UZCEuN_7s7lEdv6fI9a_DC2BZel8C6Kvr4Z0vTLM_4cW0NyZxugsXqjF-c3N7gB_CBZ2Pa_uEnNK6jydmh0Gz4DzSd9H9Mq8s5WUQQLq8lLrB7YliCfs5MrX-HA7OY2g-PqkE_WlMWji50IDKt6Sd0lDYzlcEQukOPacgW7NOjBJF5fg1TggxSQ_5sganHtbPgvX3rpXghgzfDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b524eb5176.mp4?token=TYPPXJthDJIkiynW4oigPsMpoUiY4HD7ed1OIdUIMsX0USUXmEfIuvnXeSVShQAQjzT-v52qcfBxq9CgqpbJUtaxEr9LX_O4cuUeEtmqU554WmefDyU82TipX1PaxCSDgAfYI-6UZCEuN_7s7lEdv6fI9a_DC2BZel8C6Kvr4Z0vTLM_4cW0NyZxugsXqjF-c3N7gB_CBZ2Pa_uEnNK6jydmh0Gz4DzSd9H9Mq8s5WUQQLq8lLrB7YliCfs5MrX-HA7OY2g-PqkE_WlMWji50IDKt6Sd0lDYzlcEQukOPacgW7NOjBJF5fg1TggxSQ_5sganHtbPgvX3rpXghgzfDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🔥
کارلوس پویول: "من فکر میکنم اگه این تیم ملی آرژانتین به فینال رسیده، همه‌ش به خاطر مسی بوده. به نظرم اونا به مسی تکیه کردن و اون بود که تیم رو تا فینال بالا آورد. من به احترامش کلاهم رو برمیدارم. همیشه و تا ابد از لئو مسی ممنونم."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/101265" target="_blank">📅 07:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101262">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nSz4ZoT3xJXOhN2nUGlq4CB3IyuHYgqb84ogt0dF-SqjwQfy4wM4OtsMLLbTS4mf5rNrj8-Zg87CIeVxOs8HB2wr8BeGE7qcy7gdKpcUF-iqUfSLdz_lORdCHRLcAsvcsag7ddHNG6VtU9eJl4X2Ju5PGr4o3W3Q6JKyHzzThHyABz4IdZIOndpIxL1x4lsZhcqcFK9n2uYlrw8bfpnCVJTb2Nsnw8G8df7MVCGFSgzkLt5EdJ2zOpJu0YzUmrAKpl8bdIXmzfLGnSNs4B28p2xsdqSh-_3gRP6ZhxkpA-18seUr5nNd6pfWoUjhyzmq4C_Ww8ZE-A_55dpj9KFxsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ry6uHI33i_Sl1kiv1WMPZ-G32udlvRNt51lABOyVfCqAiJSh7ANesw4ypISXBUHtj7GUx6dysd_gpWpIxcgTSNROnYBGBkVUt0xS2VbL7brG4xFcO0yTSba8OJBsvhS2RjfFQoMWLM_zu2_vIhChuTdW5yNSdCTCiS7GXZdCLBi8xNwWUsBF0_KpNU_6VArMLo_747JFIzmlT76Wk5DOjJHv7a6u_BYZB6deoKTVrZg7u7Ah0FxnaHOwX1eAt96q_Lk0psk2CRT2laJrGJ7sLhUSZpg0FytHRzM-6qwCRvL0D48zK192HLGb4yfTgaWFmWYebAR9bb932Awlx8kl3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UOIUXLOtwDWEwn-R-LtCX5rGcP2QcTxApzZLqG-Ud_sSlDjlc6pOj4qTxN7EXD8txxTnaFXd0QxPMh6KL_ggDnLX7S4RD1DkGt1bFaJ183kRIMFjpaZ-CCwiHkSdaeLUqORLz7w21DR9hoZMYPm2KrugcIa2QGGJd0P-si8dwr60tQ0w6ptvX6GCujp8_f_ZZ-arme7ZMljWnakw6-8Y9r_SxXplvbYPC77SeAACWgtIAjvlSKzWT5fL6PhLaYGEERrrkX1mtU3mgyBvqeUXVl98l7llb7ha0oIdbOwl6oqi80U5PU0ATTsnkqRQIdfMWiMw4wlvS2iaozEX8CR95g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
❤️
مینی یامال برنده ویژه فینال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/101262" target="_blank">📅 06:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101261">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qw9R91E2dS4BIArSS19hYqFZQGHzo8Y4eAC1vaJkFDrTTI6m3ms1z__gXIIx4513nW7pJLjJenQ3Hzfnm8alYeGnitNIkG-EfZ07rcd4RwWLilSaW_JTtZODewpOD5AexKwvPZ1A8gWqO0FcPZMV6lQK6d7x5s8x5PwmrlZ-yrbmc6WjTJ5tn3euFXptmdKxAQWUzxRSNT4XPhUCXnrofxyM9Vi6UeK_1B9bafLJ5E-NW6V6Qc-Rb3YblCytklGh0LWV8TbT_3vUEXaGfi7l6hjSFnDYM8GP21Dx_43Y0W8sLP3CVIv79gY3lrMjynMRkwn5MbFSIIj0SuY-U4Z2ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
میکل مرینو:
هنوز هم در شوک هستم... ما قهرمانان جهان شدیم و این یک دستاورد بزرگ است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/101261" target="_blank">📅 03:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101260">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqRnow-0H6FO9XYAyR1gAN4TvtXHPWiDO44oEf849vsQy8joHoxMmwLRK9pQ48SVwIRBxzenmNjMokKoIPQZbV2vwqszxmIvQZz_LnHEPNjn1IKqAYAQa0ViHm2Np2ITW2Mf6Z9MrMJEwTSzCq8KcJwvq4A-RUcTix270hdcCJC7mJ2TbR3h8-29kM9pfkIhP8iS75HE3KfASfX3Zk_DxbRxuWR9lPr9qDBAtxV7PjWH40dusyE0brxYkhaY5uWifKE3iGN85UDIDJv3gzuTm01WXUsdxrV-lmomdUwCPcQJi27J9sBAgfRkl9DVtXfquuSfIw4ViPRNaDiGpYE2gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دلافوئنته:
رودری بهترین بازیکن جهان است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/Futball180TV/101260" target="_blank">📅 03:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101259">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=OaEdNHY1XfjfyEuYB2fVxN-r33-kbOpgWZiQxbQbNfe54Y9ZUh2CU78d8T1javpJulafwCbAY1WlgZVBs9ID3f0mGHBpfwCrBjRoWkWVwFFdIGXJJcQH1SJ98aGz6PitgGcnOQfU9BmRO4PuuCCR2h2BedUmL5asDbSoTHsQXQV8OajWPvSrW2R76GkQKqx1lfaRopKDLj88_0RrDtdIOcq6819Vp5f1viJlTn8VBm7jwUe2ia7p0iE1aM_XCyopc_dYxz9V6QsNPeJcTsqZjkVLhNHle-wU5S5gaqDf1PgptJkC988OgInGugkei-FXdKoaAzBDYN8Bj1Gq-R5XwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecc89e4277.mp4?token=OaEdNHY1XfjfyEuYB2fVxN-r33-kbOpgWZiQxbQbNfe54Y9ZUh2CU78d8T1javpJulafwCbAY1WlgZVBs9ID3f0mGHBpfwCrBjRoWkWVwFFdIGXJJcQH1SJ98aGz6PitgGcnOQfU9BmRO4PuuCCR2h2BedUmL5asDbSoTHsQXQV8OajWPvSrW2R76GkQKqx1lfaRopKDLj88_0RrDtdIOcq6819Vp5f1viJlTn8VBm7jwUe2ia7p0iE1aM_XCyopc_dYxz9V6QsNPeJcTsqZjkVLhNHle-wU5S5gaqDf1PgptJkC988OgInGugkei-FXdKoaAzBDYN8Bj1Gq-R5XwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نمایی دیگر از لحظه بالا‌بردن جام توسط رودری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/101259" target="_blank">📅 03:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101258">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwZr33tlW-UzYx4krpqNbN5xvlL9gYUzyj-9hCBDmXYig7pLAu7CzvUq4gtXMN9ApTtFxRgkDzu_0tanenpoX9OZv9IocIblhsHLe956ToAoDod8Tr6SwTigR7Weg8nGILcHir43ofLCBPjb8ZikhvBZLM5hBLfY2GwHtaJlVuAvIoY3Bxbv9BD2jKjrHkxcDiYnx7AIPqWTOfn_1CWGf_30npEwC3v1vFvqfeV4Zf5oYQWHhgyADvRpbE1ING4KHHwyG3AkUBbzlCJPRGw6Kety7FcJm3OekL-UN7WqUxc6-T4Xj3WSqi5F2eB6FJC6eghqvmDFZcRuZ79f24-P7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
لیونل اسکالونی:
مسی بهترین بازیکنی است که تا به حال پا به زمین گذاشته است.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/101258" target="_blank">📅 02:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101257">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhRIX1ZfxaYnlCFt-47DNRXnSASraWnh80RNxRVCiD6y0-s1xMV48cs0_fbgomWop72lA2aYKr8AYEYP88NurCauUgSUgD5otYgQ-jfRo_400KmEZH82BN-ABiV_oPYI2zebPaxj8GcHcT96xwI3Y52UD5uP8SZ-V4eVcoqEs0l-r_DK96RhQenAFLbeYXe3zV_U3h6R5FtBit0cIO51q8o0IDdNMo6xiswVTh3t4WZcOYUiNrBy45bowx-zi_mjm2Y67Ss2gYyOcgjwrp0eXq5ob-tUFcwT366RHes1vYo06NFI0Qyt0-_U9jz1ySBal_mWBMG25X79n0nl3Dkt4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
😍
لامین‌یامال و برادرش پس از بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/101257" target="_blank">📅 02:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101256">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Um5969zzSWFNNs9N8ObEp60vees4BpKtMD_80isL_x-gVoO2ZQ88akEzYfPQ4N8xCXD0mIFndOnD7RzwgoROxVwXtxeEoBvNVxu5eY-9VjgsiD7YHZaqzv9GedDC8uiQjwFJ5sBNLL_R5DXKuqc2HFRYDY0OPr-qARPRxsyM6DtOg4-OScnljQgsVsJZcH_dkAwCQJcE1lv4SobkOXX3J01lMF35QllrxyiLRa1V2PHrIxNsBIU7Lnl76XAJNHiZcFIAy_3AJDltc8JGomxKwdDLTqw9k7-CQ99MQEa7mzIK8JoCxy-Bvfld5Qb18SK5r0bE0RrEGlKQGuVc_uhGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فران تورس:
دوست دارم همیشه در موقعیت‌های سخت گلزنی کنم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/101256" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101255">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4HjUzaT22QRqr_ok_0lq0atte6K_EYsJLfMxGQnz1C06TA4Dik32POuaONpiX3LYvYWTSSs0d0fDPbOD9ngHJv2O4BEqWgSW9DpSSDEu-dwkh2nYkNcHXS8H3F0ZauDDEguUXnuUETDCEnVXJH4rEgsF9j9zGr2OSd8adZNH4xwHuls9Jfgs2VjJ8A6CLoUYgJM05yK4_iwtdZjFchsnKsqnSwTUPnZxEu_qR0op35RiRLCdPI9NPLlQ83E1XWY7eLNQFdHuwx5fJ7Ix98gxTmOWpZ5q84d1nRvISqBcL_g93ZZAizD-cWejxkGZ_UZoqUfRK6q_w_uSXK8psSzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سنتکام: حملات ما به ایران برای نهمین شب پیاپی آغاز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/101255" target="_blank">📅 02:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101254">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
چندین انفجار در تبریز و ماهشهر رخ داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/101254" target="_blank">📅 02:49 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
