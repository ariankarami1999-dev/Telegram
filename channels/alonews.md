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
<img src="https://cdn4.telesco.pe/file/jzgVPbyU1DDeXZwZWIyF5-IMwSOTVweNrNxilHDNV0X7BZijn-0TFUQIkPDeuaBbrfth20WjyxhxfYv7gY7r3DvzPG3YhrzvsPvtQEzSGnUmBYw3Gw2-oPu10ETEGq0FGMJFFwPJbTmmDDUO5493H0sKSBgg50J5SI880HlQhCBST8Dci3vC-CcEWaHdKjQ73R946UNXs0JTlS7dGw0SUHl9wusA-nBxnCzPOXeRUtPy-0G6FuIvYZBFD4SvQfpS3lCEcskI_420-4oIJRNvTZqZeUa77cKrHmsq3-0uPEo70p5-_hOcmKJMhA5ET3f1mbpwF3lOp5VpvMFQY3FG8Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 988K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 16:41:34</div>
<hr>

<div class="tg-post" id="msg-138893">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=Q1fz3IowPz8oft3fDVnw5SzFRBAZiy6nkv6PT1KUO1fr_j6v0tNcKEdTMOZBdRx-PF-TEk--ljjJKDNh04znqj5S2lT7KJS9QYkWQvp-xnSjvEyWYv0pzNC8G-bny3ot2telP1JwxAmByZri40RFUAPoIE7g43bsOsZACFKB-zVXEPRCoDjHgjUGa61UbLSLaPLSLgRSX0w0zLkX4gglwtmNxnTpi9hFYn-G7XiqZ6ZWv9D5d_SWLpgGAfcDIxFTucj69nhYhXZdn-79VMDt269f-fjF7G6jc9BFFm8DBwDuO7mznvgPX6hk9S1DTYPyIkHGXqQn0Sn-abBwyxS0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4421416b9.mp4?token=Q1fz3IowPz8oft3fDVnw5SzFRBAZiy6nkv6PT1KUO1fr_j6v0tNcKEdTMOZBdRx-PF-TEk--ljjJKDNh04znqj5S2lT7KJS9QYkWQvp-xnSjvEyWYv0pzNC8G-bny3ot2telP1JwxAmByZri40RFUAPoIE7g43bsOsZACFKB-zVXEPRCoDjHgjUGa61UbLSLaPLSLgRSX0w0zLkX4gglwtmNxnTpi9hFYn-G7XiqZ6ZWv9D5d_SWLpgGAfcDIxFTucj69nhYhXZdn-79VMDt269f-fjF7G6jc9BFFm8DBwDuO7mznvgPX6hk9S1DTYPyIkHGXqQn0Sn-abBwyxS0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهاجران مراکشی که از طریق دریا وارد منطقه سوتای اسپانیا میشن :
🔴
یه نفر دوچرخشم آورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/138893" target="_blank">📅 16:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138892">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOm_rb24WpauS_QcwUxtUuXPGsMalwL2Pb_UYlVltvmiiABwvH8TyEvgeVA-hp56yYhQYY4mQzqPGoOuXWmIX99QwxjTtNqM1TzAed5VCwgtIx_cjV2ABBfZ41h6J2dB3Tkv6iJ_4WhaYUyZYehRRps34AneGJR9zfJUmts79LBBGnsivOMMFVihU89h04ZEzVhVTqp3D3wnbUJsjZCMhjauQBdW6iQ_C3P2hVygCqsuqvkEny4R1cYemFIN-XpJQds_B0_mUQQR6I76NP4Qe5dkWslFCsC3g0W70EcDckjx8WM0POplc8JwJW68HmpbwGz_OX6QbERP2qnuZ2TKng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لوومر، فعال سیاسی و مشاور نزدیک جریان محافظه‌کار آمریکا
از کارخونه تولید پهپادهای
SkyFall
تو اوکراین بازدید کرد
و روی دو پهپاد رهگیر
P1-SUN
امضا زد؛ و یکی از اونا‌ها به عنوان «
تقدیم به ایران»
علامت‌گذاری شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/alonews/138892" target="_blank">📅 16:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138891">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‏
👈
ترامپ در مورد اتفاقی که در اسپانیا افتاده:
واقعاً افتضاحه، ببینید وقتی آدم نادرستی به قدرت برسه چجوری یه کشور رو نابود میکنه. این تصاویر رو بخاطر بسپارید، اگر دموکرات‌ها دوباره به قدرت برسن همین بلا سر آمریکا هم میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138891" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138890">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5CF8DIHUJnVU622eHRzp-ujIUtgE_LU1KQYLSmlU6BDb42b4X9WhMeAHHoL56WaWEApKPAjb0inpUEoY3Qh0VJ1xkXRK-FULYmHCxqew9NwhjOFiAQJc6WVcOrg6Qkk6FnbUYP4G-P9n91_LcsnvXyPkITSJoVdiC87yocTAGaNBZO-b7_Ob7MNV-_LMq0CfydLU0DehIaxyhbQgiIRviL0Abm0iL3uq8slegGgF1N1D_Gt35vMV0YODEoW9yGEQ1RLz1kVVJGVElJHzHzpGulUjMHSjr97wOF6e-3gwrRg5W6FwcXUumOyFfII--S7yN7lzoRg6UdCHj4hdz-FXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سوال و پاسخ هوش مصنوعی
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/138890" target="_blank">📅 16:27 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138889">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/re6I59c_C0eBZRqAWXdyfY3NAvm_T8gLO-f8A4QT5t5ptjczvkNdJUQLWmD80cn_NAQH86zyqjjrSiQxA7Mf5bQymGvRoNo0nUK0CCePjv5kamBsCUt25N55PnBFxLBotOMhNx9ql4nWMHF6R6UHOSNXQ4r1KJAdOiUsKy5ri-I1nQYwLPAiUNHBwAdYLRfs-FsWg50KNOdq2pHQWiy5ke2V2vc8uvwRivf4t3PZKUSdcKOXwy_comizTxzYK8ml4jxvfxb8K1jkZZwvJtjyorn_FjQRry0uY7xFMuC45PyNIhomnSqO2V1hXugT8pgyXaeeuHzq3rzf0uOYK-953g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی از ترامپ خواست تا از ایلان ماسک بخواهد که اجازه دهد از سیستم استارلینک برای هدایت حملات پهپادهای اوکراینی به پایگاه‌های پرتاب موشک‌های بالیستیک در داخل روسیه استفاده شود.
🔴
ترامپ به این درخواست پاسخ قطعی نداد و سرنوشت این پیشنهاد نامشخص باقی ماند.
🔴
اوکراین استدلال می‌کند که این اقدام به جبران کمبود سیستم‌های دفاع هوایی پاتریوت کمک خواهد کرد.
🔴
در حال حاضر، شرکت SpaceX استفاده از استارلینک را در داخل روسیه محدود کرده است و فقط اجازه می‌دهد اوکراین از آن در خاک خود، از جمله مناطق اشغالی مانند کریمه، استفاده کند.
روسیه پیشتر ایلان ماسک را تهدید کرده بود اگر بیش از حد به اقدامات خصمانه خود ادامه دهد، ماهواره های شرکتش را در فضا هدف قرار خواهد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/138889" target="_blank">📅 16:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138887">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GJ5AODmCKeBb6-2EWRLMXTKVXpOyXC1Cf-yhmjXXXhUkS7V9xtWvo4OBNSVuSjp5z79KYiVPfRVyqpnCvVBsoxR7IDSe48VmJYw3tlwhAXxV1P5wglmGS-C2cgD72e1wyZl6uozkvRAyRcs25TH9IRmbMrT6l6hHCvWe1uy_MfVOki0Hk9FfmCMecvIelkvmyp6tXRgubTytPhymxmAQDQgLyFbAAH2OayGxNV_GRFMlfbMPumoyBzn5AESIOMFF4Ct_d0VFOQhbsWgKUSEwZUDsuT9X5Y7JF7OVHS5_I5Db6wDc9xFAuMMzsR46uBY2Pg-EmrjvvaU_tfQTs3kBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=Xe12nTOskuDGZfYbIBk8HAQ6s_TR_zdLvMzsOa-36qibMtkmsadum7032gb2se18cCC5cyjlxa4sEH5Vzylwv0O_PTKLNVMH6LWvE2gha6tiJ2zy_JvB0FtyzMVK3FH6PDg44jHym03iTFAIdWqQlEpsTAWsJvV-tawY_6Nrkn6azpzeuIfjWjLSwIVnKYZVCacqmdUextn6eZw1ZQ5HQ_ncz3Ub4rdHsQeBgp0vXGj_MWjfGrNBfGKs381PvDUQ3J9Rm_WrjId_-vTsT5H6iV4DNwkDOd_UaPoumZvCrFdUWqHaJamvKWoRwyDYK4dc8xwKWyGLuFm0msCy8flnCw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bb843e99ad.mp4?token=Xe12nTOskuDGZfYbIBk8HAQ6s_TR_zdLvMzsOa-36qibMtkmsadum7032gb2se18cCC5cyjlxa4sEH5Vzylwv0O_PTKLNVMH6LWvE2gha6tiJ2zy_JvB0FtyzMVK3FH6PDg44jHym03iTFAIdWqQlEpsTAWsJvV-tawY_6Nrkn6azpzeuIfjWjLSwIVnKYZVCacqmdUextn6eZw1ZQ5HQ_ncz3Ub4rdHsQeBgp0vXGj_MWjfGrNBfGKs381PvDUQ3J9Rm_WrjId_-vTsT5H6iV4DNwkDOd_UaPoumZvCrFdUWqHaJamvKWoRwyDYK4dc8xwKWyGLuFm0msCy8flnCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بدل علی خامنه‌ای در عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/138887" target="_blank">📅 16:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138886">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc2bce2332.mp4?token=RH04ukA4F9Q4AawCvtQQfFr19rAJwAjn8Bprqek-QEZBd7IFyKrDR_g-_tum4dLAYram-RN-Fk2qPZ_LMHirIPZLSxa-j3IUk1Ov7HXJLvurAIu8F03f24_xEENt_oCd80ynfgH7hwF5LFUczSfVrXYbDgWhINx93Awzk3CZbl9fF4fKgm4KowPj660zs45J4cf_L1H2rkPiNsxDaiN6cUIgyIT4rlcO77daVuakYL2umlm8HTbwwNNvS25EUTPuGrMWOWIpUkLK8uz3fRIfjC1gkH-tF3Zv1QaEutgAH45uc6LaFpOTvtCtq6KZSeuZeuXTx0xXjdYU9RKYxMKgH4oyu8TnfQPvRxZAOlAXmXEqNlFa7ydmcdWCuKj3fOgYBwUOtDKaoGaiZk27ukQKW7s10tgwOGfkxpVqGDKMTD_eqEG7cW973a69NlOtaRaRvvEc0LNvn7PrOYWoJbCGVR_enE2q1WabTwZh-wzTZw_KJGQHL0D3ehRnzWihonSrLEpfYqjFh2O1zB5OL45wjze2F1PbLvJsFuI5rhX979RKYTZewdxBB4fyNAxQb8q4Tot7iGbHBL0JmOxpVO2qmQR1DRoFLjAkFPRmyzZ5uejIltOMwvJpUUHgoS9YNkoCOwJIVdCXhzDVqgyQBU9ZI6RsaHLfeTG91qNaYpsggi0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc2bce2332.mp4?token=RH04ukA4F9Q4AawCvtQQfFr19rAJwAjn8Bprqek-QEZBd7IFyKrDR_g-_tum4dLAYram-RN-Fk2qPZ_LMHirIPZLSxa-j3IUk1Ov7HXJLvurAIu8F03f24_xEENt_oCd80ynfgH7hwF5LFUczSfVrXYbDgWhINx93Awzk3CZbl9fF4fKgm4KowPj660zs45J4cf_L1H2rkPiNsxDaiN6cUIgyIT4rlcO77daVuakYL2umlm8HTbwwNNvS25EUTPuGrMWOWIpUkLK8uz3fRIfjC1gkH-tF3Zv1QaEutgAH45uc6LaFpOTvtCtq6KZSeuZeuXTx0xXjdYU9RKYxMKgH4oyu8TnfQPvRxZAOlAXmXEqNlFa7ydmcdWCuKj3fOgYBwUOtDKaoGaiZk27ukQKW7s10tgwOGfkxpVqGDKMTD_eqEG7cW973a69NlOtaRaRvvEc0LNvn7PrOYWoJbCGVR_enE2q1WabTwZh-wzTZw_KJGQHL0D3ehRnzWihonSrLEpfYqjFh2O1zB5OL45wjze2F1PbLvJsFuI5rhX979RKYTZewdxBB4fyNAxQb8q4Tot7iGbHBL0JmOxpVO2qmQR1DRoFLjAkFPRmyzZ5uejIltOMwvJpUUHgoS9YNkoCOwJIVdCXhzDVqgyQBU9ZI6RsaHLfeTG91qNaYpsggi0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما نوادگان یهودیان اصیل سرزمین مقدس هستیم، و ما بخش اولی از میراث یهودیت و مسیحیت هستیم که آن را گرامی می‌داریم و که به جهان تمدنی مبتنی بر آزادی و ایمان بخشیده است.
🔴
بار دیگر، ما باید ایستاده و از آن دفاع کنیم. این میراث در معرض حملات ناشی از افزایش موج‌های یهودستیزی و مخالفت با مسیحیت انجیلی قرار دارد.
🔴
این اتفاق تصادفی نیست که این دو [یهودیت و مسیحیت] به طور همزمان مورد حمله قرار می‌گیرند، زیرا ما یکی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/138886" target="_blank">📅 16:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138885">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ba8d8342.mp4?token=OFuRN8EnUYC1jJ8e6G8OVoJREaFKVCbuQspRs-xDcFvnvSk1uK8aG2YJiG9K5GOv-av-B01TNFD_3n4WU3wVI9A_Wd2UadCpJWx30P_Hu5ExBjrrxVQKDK5DK6QIlUMWPDFHkUjvW-kzLJWCTiZYO7d4V1m6bScdUbmzp0fzlXK8_s6zt4XUXw4BECRr-EMcnK7gQCRiwNuguj2dtYGwQ6N88mi8Go2jyJy8EoD2IxM6sqvi_h4zkgQ0oKK41C9VIDXHJkAaN4P0LpVVIAY4hWVmEI5zu97LcR-kD0upqCx9r38nu7YE51s5InDNoCXFQ824SqTsP6UVzbue6ymGjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ba8d8342.mp4?token=OFuRN8EnUYC1jJ8e6G8OVoJREaFKVCbuQspRs-xDcFvnvSk1uK8aG2YJiG9K5GOv-av-B01TNFD_3n4WU3wVI9A_Wd2UadCpJWx30P_Hu5ExBjrrxVQKDK5DK6QIlUMWPDFHkUjvW-kzLJWCTiZYO7d4V1m6bScdUbmzp0fzlXK8_s6zt4XUXw4BECRr-EMcnK7gQCRiwNuguj2dtYGwQ6N88mi8Go2jyJy8EoD2IxM6sqvi_h4zkgQ0oKK41C9VIDXHJkAaN4P0LpVVIAY4hWVmEI5zu97LcR-kD0upqCx9r38nu7YE51s5InDNoCXFQ824SqTsP6UVzbue6ymGjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مراقب باشید در این روزهای حساس گول پروژه های رژیم رو نخورید.
🔴
از سرتنگ راستی بگیر تا رپرهایی که الان شروع کردن به دعواهای مختلف و اختلاف های قومیتی.
🔴
با آنفالوکردن مهره های رژیم بزرگترین خدمت رو کردین.
#پروژه_حکومت
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/138885" target="_blank">📅 16:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138884">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل:
اگر ترامپ از ما بخواهد، به حمله علیه ایران خواهیم پیوست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/138884" target="_blank">📅 16:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138883">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/euSQ5wo6nj4hRrWH_doaY9q6AbHPdG-o8B8RmW79EWRGT5eluyQxn44NzGdpDM_go8BoBnxiAohVVwF7xZEXXGOuenv4GbAPEvm7tZPoIaTecVu5y5isCKzI8CA46osj9rNr90GQLZwrJL_UyAw4NX8ddgpZ5LjtoQNJ5tUR10wIiAPf2ZpZA7Hs88o2EOS_y4Cf0S0wnrPDim7FRYwV921SYn9CcQ696YGMHsJalxPjnIpfPezxVgm57CZmwx8PSOZjWRTLkRI-encX-TtdcIrPTizrmJRKe3L45KzO4Qpn3-mtril__FPC-8uy6QqwS-4r-TotFJbRPFAXaUxVyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گاردین: عربستان قصد داره یه عملیات بزرگ دریایی یا زمینی علیه حوثی‌ها انجام بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/138883" target="_blank">📅 16:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138882">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66529904ed.mp4?token=ITNX2EepU8bvY_mW46WRkKEPb2wQm70It20svjJ8AUOu3Y_sxbD_iaO_b0uXQ9skPNG7pETqxuISMcnQ2QEDsahpL5-y6t29an2nQZB-CL-Cx6A8rJROQy2Tkp6NFY-cfDwhxsoHrS8s7L_fVwOsUYKOeHBBGV8eOaOxqadLmx744DkGQtPEjto74LQ3hI3W_ajsJOSXWJxYFOKCqMyk7BYoqb14sYOHld7vWPvOeoyiqQTxWog4vxlY4UKHmwGkHkY9pmYeoyKK6O6IvVEXNrgTPz8i-wWej1Fkhr1NJDwLa2DOzwJZAxQt2BYuYwCQjy0tejMcUQRmce5ddLswcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66529904ed.mp4?token=ITNX2EepU8bvY_mW46WRkKEPb2wQm70It20svjJ8AUOu3Y_sxbD_iaO_b0uXQ9skPNG7pETqxuISMcnQ2QEDsahpL5-y6t29an2nQZB-CL-Cx6A8rJROQy2Tkp6NFY-cfDwhxsoHrS8s7L_fVwOsUYKOeHBBGV8eOaOxqadLmx744DkGQtPEjto74LQ3hI3W_ajsJOSXWJxYFOKCqMyk7BYoqb14sYOHld7vWPvOeoyiqQTxWog4vxlY4UKHmwGkHkY9pmYeoyKK6O6IvVEXNrgTPz8i-wWej1Fkhr1NJDwLa2DOzwJZAxQt2BYuYwCQjy0tejMcUQRmce5ddLswcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تبلیغی جالب در ایتا
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/138882" target="_blank">📅 15:55 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138881">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byXuivMr0W76Fdecra-oJb_giUipgUf2wqn3BgTkGaeSSk7KFalYX54zS1Ma4o9WnbiK3d8JMr24rkRgdmXAUvt4XTpyZanLyER3RVQ9IUEOSYHT_9cnsO9H9BaQWH6K4GJ69VmXEmuq3edbnOLd-PKohE26xtX05wXeL21a5wbYfjWBbfQ1ctICR94jj9vXQhY2xZdOlnhuNrIFKvyVvC6DicdTV1UPowxiXUNszu3AKfHBPxLWp_lBsGZ8L2MVKmbZNkP3P5N9WnxdNi-M7sstadRHQ77AhNwtBx7YYHLXBzx5qXkiLR3ndGyOMOuBXT6sUOvUeYDo9W5wPq7wtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ایالات متحده، کشتی قطری را از رسیدن به پاکستان منع کرد، زیرا این کشتی به جای مسیر آمریکایی، از مسیر ایران استفاده کرده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138881" target="_blank">📅 15:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138880">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">⭕️
هشدار درباره کلاهبرداری‌های اینترنتی
🔴
کلاهبرداران اینترنتی معمولاً با ایجاد هیجان، ترس، اعتماد یا عجله تلاش می‌کنند شما را وادار به واریز پول، نصب برنامه، بازکردن فایل یا ارائه اطلاعات بانکی کنند. با رعایت نکات زیر می‌توانید از خود و خانواده‌تان محافظت…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/138880" target="_blank">📅 15:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138879">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh26dInvcZlDJQfsdwakMLNxPXRxqyp4ZpWlxvNSiiWShI6iOE7S98FfiLyvf-bQKUp79jEfRrXVmrDnRkI70JopAoR0liI6vkA9Gu6Xn3tXvXanSTunNCo20y024BXdPYxGReW-dZunppuj6MfvYUP679LHuOQoqhck0Q2K9lDl3MrAmWWcEcdyqD3WOJTVkTAx7_dGuG8zThkA9rWOsBVWauCMQGHvtduylWCPkntuTpKgrbOht5Crk8fYn-596w9YZKe1NhuppdtP6bopI0DV9HlnZQpDk_cyC5d_UKKKzJzPzhD7jY7-g0o9DYKsInPfCjZKgynOWsVpFzh8rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش باراک راوید به خبر طرح آمریکا برای اعمال محاصره زمینی ایران
🔴
آیا اصلاً کسی زحمت کشید قبل از اینکه همه سایت‌های خبری اسرائیل این خبر را بزنند که اسرائیل و آمریکا "در حال بررسی" اعمال محاصره زمینی علیه ایران هستند، یک نگاهی به نقشه بیندازد یا فقط یک لحظه از مغزش استفاده کند؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/138879" target="_blank">📅 15:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138878">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRbLCZhMmFVjFGI0-FDmag9p8KRop4yHkO_hHlZsW49vjAtfnHR6jRyPkVLdamjIpNew8srVH7_iG0cT_IBCPDYcF32zx4G3xPdyexBJYYG_AAOkzAnXOdpgDRVNhAX_K9S-ZxaIEhyqwfhktdWFJ-SHFMur8ESjWHEb8OTaua-dP5w1Wmrrf3ldTGHc5pLLeMSDFRpWM2PqxHKzhYix1g4ED6uXSKDS51acxflrZcyjijvayG3nijNNaSbfjt4oB-PU1n9VAmAWP-T9xJorAdlhEXo3fjKjYelAXb8_4sF1Cr0_6Q5b8VaY2nywARVS0L7GzLvvbDFQXEDEFmF_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
با یه
مهاجم مراکشی
که اومده اسپانیا مصاحبه کردن؛ میگه تو مراکش منو اذیت میکردن فرار کردم اومدم اسپانیا
خبرنگار :
چجوری؟
مهاجم :
من تو مراکش با یه نقشه همکارم رو کشتم اما بعدش پلیس و مردم اذیتم کردن و میخواستن من رو بگیرن برای همین اومدم اسپانیا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/138878" target="_blank">📅 15:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138877">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/844225751b.mp4?token=Kw9qGPkla5bEJ0SHIDpqv-obNmX8_womDIM4Pr38Jz_g22RzDy1McF2AUmDYFUIx26IjQ00ziRfmmumeid8Ay53WcgcLp1Rj3wSfu-Y1r2tzq3VTr8z15kjAeufAh2NdRr3GRZzzZEA81rvLO-dhyYs8Bf2NK_Budgt4xfc7oI6JjX6x5iTKg8bQ5c6DUvb9n5KQpM4oqb_0BPvemvpJRCySQsocoiy94lywyozdZkEc71hKAstkoIOVR-S7bPx_B5_-_jKsdcW-4v7Mm-c-J6q1UstcpY0ynm-wZ80BEswTirvVbehriCWNPGTUhBw2Pigl4MnaIY0NGK5X6VIctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/844225751b.mp4?token=Kw9qGPkla5bEJ0SHIDpqv-obNmX8_womDIM4Pr38Jz_g22RzDy1McF2AUmDYFUIx26IjQ00ziRfmmumeid8Ay53WcgcLp1Rj3wSfu-Y1r2tzq3VTr8z15kjAeufAh2NdRr3GRZzzZEA81rvLO-dhyYs8Bf2NK_Budgt4xfc7oI6JjX6x5iTKg8bQ5c6DUvb9n5KQpM4oqb_0BPvemvpJRCySQsocoiy94lywyozdZkEc71hKAstkoIOVR-S7bPx_B5_-_jKsdcW-4v7Mm-c-J6q1UstcpY0ynm-wZ80BEswTirvVbehriCWNPGTUhBw2Pigl4MnaIY0NGK5X6VIctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خضریان:
نیاز داریم مدیران و مسئولان کشور را در
زیر زمین و در دل کوه
از ترور ایمن نگه داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/138877" target="_blank">📅 15:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138876">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/415999864d.mp4?token=tDuhXfgnm_sr_olnPjTK1j9rqqvwyA35z_lx0NkIdutF6pLC02ugpzxqWJ0ZrE-zw3rR6fwvAhqSBQobY_uxBaJ6GhNX6-hTyP-zEr0_-lKZdKTcOrC4PrBy7a591DOPfvLI3jgpRY8qxSE_tdhfkyBUyRgkTbmtlsWPeCynqGqBkyzb0k13y4D4A7o5l915szbW-4gMd-1kRx73-v_BPKWbo0m4oVozJmsfY4HAPuWxo66Ej6HtS6vb8pPw0E3NvmkmntylATM81GfVxTaw2xbaFw01ibbM_Fe0baNEU19UFwoQU0CLSHgLy92Tms1SaD0pyVkR3QckKeYB_4vApw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/415999864d.mp4?token=tDuhXfgnm_sr_olnPjTK1j9rqqvwyA35z_lx0NkIdutF6pLC02ugpzxqWJ0ZrE-zw3rR6fwvAhqSBQobY_uxBaJ6GhNX6-hTyP-zEr0_-lKZdKTcOrC4PrBy7a591DOPfvLI3jgpRY8qxSE_tdhfkyBUyRgkTbmtlsWPeCynqGqBkyzb0k13y4D4A7o5l915szbW-4gMd-1kRx73-v_BPKWbo0m4oVozJmsfY4HAPuWxo66Ej6HtS6vb8pPw0E3NvmkmntylATM81GfVxTaw2xbaFw01ibbM_Fe0baNEU19UFwoQU0CLSHgLy92Tms1SaD0pyVkR3QckKeYB_4vApw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیوی وایرال شده از دو پرچمی:
هشتگ نه به اعدام میزنین؟ خودتون و خاندانتون و سس خرسی رو باهم اعدام میکنیم!
هر ۴۰ هزار نفرتون فدای یه تار موی تازه عروسِ شهید علیخانی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138876" target="_blank">📅 15:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138875">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVJzQgdZjcVRghj8qMo5CNehDPwYGbTJx5LxXwgrNZDqxVI8q_jYlrrZVgry5zSjQvD5eNAQ0hB5mZJ8P7g93ebjDFK8V9ZO1pPHCfEaJh-zQ_5yqXyB2u2GCCQ6xDgI_weqLQPkC83kDjfZGoVkWLZDAb6oUmDPz5srhfGk4SYSPSBm1p3R_le7gakuY3eMMSeR9adeINfKsp10ppN62ay-QW6W7VVCSV-x2z9vg1meUv-Ge4YjgLhAbx5hxoqctTDOiTxGASH1zbKjA04rfzjIIp1TS0X7J-AYDhISXI85J-7u55OeMZU95PkyCC2vcGUC8ZdjPr-jxlJVs8wIgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی: اکثرا خانواده هایی که بی حجاب هستن با مشکلات اقتصادی و خانوادگی رو به رو میشن ، خانواده های مومن و با حجاب مشکلات خانوادگی ندارن و فقیر نمیشن و اکثرا ثروتمند هستن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/138875" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138874">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uteYEN8DwCXRX5eiwviruHk5oxP-DWjVso0NoQ0GVAzckI-SjenMLBP0J7kAqwqbroqPW_cTbTGQs8NHVATUB6wqXYdt_uiFN3h3YBya_qbI4xeqhUV2F5I8PW3gMzARjdrqm_URNsbyx_AhwKRpB3kk5Oj9HrBxB_U_5zIJtIbOdFd0pAbDDBgmXpPX_BdPPwiPSaey8f-_ThRrN0FnNbsuCj_-32MmioES2tsgyNUHa5Os2w2YcU8F6SblMc0gMQz8fq9YqpZ7gO5x71eshwxhoniJYTBY79lIxq7D7OVR48Kqtq9aY-YX-Wh73UKJc-WDMsZFKpHKCXzxvOQdcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوید کلهرودی، نخبه علوم سیاسی دانشگاه تهران: با جمهوری اسلامی هیچ چشم انداز مثبتی برای ایران‌ نمیبینم و این نظام روز به روز ایران رو بدبخت‌تر میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/138874" target="_blank">📅 15:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138873">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
استانداری هرمزگان: دود در شرق بندرعباس ناشی از آتش‌سوزی انبار ضایعات و درختان نخل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/138873" target="_blank">📅 14:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138872">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
تا الان در پی هجوم مهاجمان مراکشی به اسپانیا، ۱۸ نفر از مردم این کشور کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138872" target="_blank">📅 14:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138871">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-Mez-nn3NtWZ91ZWeEjfdurV6sLvCj3IDQrMH5jKPIawaatf4sGjEaAjH7Ekp6KrioX_owLGXm9_mRNqvtPIqk-j72UR8jEhYrm4eoQw_MkHi3Fs5LFWCA6xVyBbAriaKblpUerEBDxfIkNQOtcnooy_9ErF7mZOyzvooG3goTYSImiNXJ4TU2M67wM2Au83TnhGFRXXlf9mhFvaawC-4D2cWfTD5uSPUhcYlTuqu9g5UP9f_fck0JiDSfGX5gckKXOWhnnYLOy3CBjMw9iB6UIS7e9zh0ggOio2K_uj-o0Sg67mro2NyUtRGndrx60AtowGNetoFMUSEO_ArdANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت ترکیه احتمال داد کودتای صهیونی آمریکایی(اعتراض مردمی) شکل بگیره و اینترنت مردمشو قطع کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/138871" target="_blank">📅 14:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138870">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ قرار است امروز در میان تشدید تنش‌ها، جلسه‌ای با کابینه خود در کمپ دیوید برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/138870" target="_blank">📅 14:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138869">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9Mf7MB-fc6Q2TKXfusy7fsM5yR-XTE7EWs8dgEcjAXdsw8xrHRKss2uN1sQXypStU2T7T_KZ4P5Ut-txWnF-1aQnO0DfL7UnjHQMQ6wiGlV9XMDf7cbI9mpBD7DfmWlNAXSPxNF-cPh3OJrWQpMtj63okYqGDRRmhMPRkK0ejo-s3CmLQyDzeixgXcNL5YB6uqOtGX6Rgr3njiZjsGxnTp8pn9faL9ZX08zTug3LfTSi6IdQ9nLYaCqRoC92zLFJab5UuQYChZUakpXuBqNJNqVOJd4LJoG9v0Y6p4IdORV6uwKp23H_1B-UWKvTGRDUF6vlP2eVci_8fi6kercpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله نیروی هوایی اسرائیل به غرب شهر غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/138869" target="_blank">📅 14:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138868">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
کویت : از صبح امروز چند پهپاد
وارد حریم هوایی کویت شدن که نیروهای مسلح اون‌ها رو شناسایی و منهدم کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/138868" target="_blank">📅 14:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138867">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0HU3YhjIGc1TudVbe4YJMNy71pdm0EWY170eJQTMnql-vFZxEyCQsOamWWxGk5lTEmROCV-iOmgUPBrx9beHSm6QdHo0BMKjRiEyubTe-IO32gPa8YjpcFAcAL2Idsf9fzaujB55DfhwumScf6EmJeI66-fpInHIUYmA38knPB6b68hDiQYpIqm269hdlnNhvbQdr3Idi-OdN5u1PrWPWIDxCh06s3Xze-5TIV2syPKZKq45WRLlZdCdlhhL4O_T-oL3qPbuTRZhGjmLO7jwN4i_Uj7VXmQhyako0P3azPhZeGkP5fv3CO9ebBMyQXOmbkASk9o0wrEOjVC5zRU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در یک مصاحبه، از یک مهاجم مراکشی می پرسند که در کشور شما جنگ نیست، پس چرا دارید به اسپانیا فرار می کنید؟
🔴
‏او می گوید چون در مراکش مردم مرا اذیت می کنند. من همکارمو کشتم و پلیس و مردم دنبال من هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138867" target="_blank">📅 14:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138866">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
وزیر جنگ اسرائیل :  اگه ترامپ از ما بخواد، به حمله علیه ایران ملحق می‌شیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138866" target="_blank">📅 13:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138865">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
سخنگوی آتش‌نشانی تهران:
دود مشاهده شده در آسمان شرق تهران، مربوط به حریق ضایعات و فضای سبز در محدوده جاجرود است.
🔴
حریق در دره است و آتش‌نشانان در حال اطفای آن هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138865" target="_blank">📅 13:58 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138864">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4La_MtauETFjOTDWWCg_cYyi95BqYiv7aBWR9Ingk5vXAc3GZf9JkKUX0O1ewVj9n9KvtntOoT3ik_TqK2FFSYOFYTIWXHvhmwTLlaeWTGaPuzwVfnay23U-XlRf8Br9aDaYGqsoeHpFH1HDPVe0UwApfRBLAGDvHkGGgUAbfX-k334eXQ7N-yMj8Zptdbx6-V-SA5aUsJyT4df9c3JI3wGKcEUzXutkTEoWu74iufcGJdxaUDpP3v9rEjwp_0vL5emCBOALAt0UI32As1QpCw1bQaMTWbHFxIjslmxxDkTmmZoBJ8uJBviggInEpdeI4vxuPRolr185jZVwn13IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اینترنت در ترکیه دچار اختلال شد
🔴
بزرگترین ارائه دهنده اینترنت در ترکیه در حال حاضر از ارائه خدمات باز مانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138864" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138863">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
عباسی، عضو کمیسیون آموزش مجلس:
چون کنکور یک ماه دیرتر برگزار شده است، سال تحصیلی جدید دانشگاه‌ها نیز یک ماه دیرتر و احتمالا در آبان‌ماه شروع خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/138863" target="_blank">📅 13:50 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138862">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPDQ9zkiMpHBqR4LlnyvO0hhLN-o-OVkOUUnvo6iGPEYjLr5b-IWheVefM97uYaycXlggP9KQuPTrk0meuq8PkEDY8hu9f9fvuu_BhjNKFIwznBikwNc7zaEQNMSRHDLLGTUZUaVLNhQTZlBj-gWDfnStE1sCjqNoI-GXw8vtkE51puu_pOtSVLFO_uzDVOLlb9gRi4683nF1hq-D-rRLIMxd9Xj1qOSlLai4KX4AoG1RyrQBqocgbLSvYoamnbxj3T8r-ukHPAWFzI3G-sYsUf-dl0AZPDPyM28PsEd2ujyceARoCjXLg6jYQuYcl_wrB1SopCTpNHuGMnuQYjX8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی پیش انفجارهای در تنگه هرمز رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138862" target="_blank">📅 13:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138861">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
منابع عربی: ایالات متحده، کشتی قطری را از رسیدن به پاکستان منع کرد، زیرا این کشتی به جای مسیر مدنظر آمریکا، از مسیر ایران در تنگه هرمز استفاده کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/138861" target="_blank">📅 13:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138860">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c38ab5a46.mp4?token=C0h-zFc4ewlO33tuz-bdypYmJqEuxvD6bsMMmxlFIv-TTZOjqGqvwXuLx7_qY3ARknjvNrq7GeexJcdN6ZfksV-t0zQ09Vi2x-fKH98RGKFPGTmJs7fJI4kHrPRExjAslasXNbwtnYcPTq-D9CfHLu-fhO3UCux2Z-wQ6bfLHhsch4_isQLrG05dpQzMp2uAQKuBjDhMw3S3RG58MUv5oRi_phfE17ClWPyhBgNLSDM1nFITSzBU2gc--QMndR8ck3sO6v6_CqhgVdH5n4fl8dEB6YqRC3Dw18vZwfI7eZf4Rd1wrvMHVSc_6w6KdfB99b6SwLUTfndireIvVaqqJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c38ab5a46.mp4?token=C0h-zFc4ewlO33tuz-bdypYmJqEuxvD6bsMMmxlFIv-TTZOjqGqvwXuLx7_qY3ARknjvNrq7GeexJcdN6ZfksV-t0zQ09Vi2x-fKH98RGKFPGTmJs7fJI4kHrPRExjAslasXNbwtnYcPTq-D9CfHLu-fhO3UCux2Z-wQ6bfLHhsch4_isQLrG05dpQzMp2uAQKuBjDhMw3S3RG58MUv5oRi_phfE17ClWPyhBgNLSDM1nFITSzBU2gc--QMndR8ck3sO6v6_CqhgVdH5n4fl8dEB6YqRC3Dw18vZwfI7eZf4Rd1wrvMHVSc_6w6KdfB99b6SwLUTfndireIvVaqqJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سپاه در واکنش به تکذیب‌های سنتکام تصاویر انهدام یک نفتکش در تنگه هرمز رو منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138860" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138859">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
تلگراف : آمریکا و اسرائیل درباره احتمال تحمیل یک محاصره زمینی به ایران بحث می‌کنند.
🔴
این پیشنهاد، یکی از طرح‌هایی است که رئیس‌جمهور ترامپ و نخست‌وزیر نتانیاهو برای افزایش فشار اقتصادی بر ایران بررسی می‌کنند.
🔴
چنین اقدامی مستلزم آن است که آمریکا و اسرائیل از کشورهای همسایه ایران بخواهند مرزهای خود را با ایران محکم‌تر کنند یا ببندند و تردد کالاها به این کشور را محدود کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138859" target="_blank">📅 13:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138858">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=H0aNX9E_I7SWQKuNXlvXb-CTIjs_C12JRt2SgRyMgy1Wi5BDkJPcyLIi288SVsASxQefD91MdiRipTjt87RFBmShAUHtHk1wd8PexFz0n0r94oNHQSEw_fDjqifx5sV18NnKwO3JVgris3ADrj64EDua2Fc7eTCtdcBLHW1HAOZgv1sKzLVkzG7wQfltw1aL5ICyt2g4EEQLxQcyZ5WOhiUVbkn8NA3zMB7DeMCFZad-Xc6-qtEU-NjrvFFIwv5oomovF8RP-AAy3bYNXLooSHwXruX567hWwfzvlf39OybOW9YH3sHwfv7edN6i1zKFJaC-pz3gZswMecT5OhtT7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=H0aNX9E_I7SWQKuNXlvXb-CTIjs_C12JRt2SgRyMgy1Wi5BDkJPcyLIi288SVsASxQefD91MdiRipTjt87RFBmShAUHtHk1wd8PexFz0n0r94oNHQSEw_fDjqifx5sV18NnKwO3JVgris3ADrj64EDua2Fc7eTCtdcBLHW1HAOZgv1sKzLVkzG7wQfltw1aL5ICyt2g4EEQLxQcyZ5WOhiUVbkn8NA3zMB7DeMCFZad-Xc6-qtEU-NjrvFFIwv5oomovF8RP-AAy3bYNXLooSHwXruX567hWwfzvlf39OybOW9YH3sHwfv7edN6i1zKFJaC-pz3gZswMecT5OhtT7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رائفی پور: بصورت زمینی میتونیم بریم اسرائیل رو بگیریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138858" target="_blank">📅 13:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138857">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9f540d88d.mp4?token=flMqQ6OjQdbJEqTlD74prO-bAm3FV9Zw8Hw-zD7KN6CfPZRsaGjISeuNH461ataZV93TvjdIQcBbzRoAoForvJlXi3iBoGFxNvwrvdKNuV8egQHCvYDVuHmvsF1yBq-7MbzXYdsAa_COvDkkmddZ1ZHFixXeTrZ8eAFxjfYSHlqzxHDStQNyf0cbACNphZ-IpOR91m8knGRet-ZazHGkUaXVbc1dFroopL0g5DDmIAsG94aiKwZUpF5xg_6A7PtNIPMij6MxHZMoSOpIqXMP-TSS96lOpOLXd5eM6TqVh0vOn_WYFBb14fPzuQpTghaWmRuufoKJH6QPmKy-IIxxJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9f540d88d.mp4?token=flMqQ6OjQdbJEqTlD74prO-bAm3FV9Zw8Hw-zD7KN6CfPZRsaGjISeuNH461ataZV93TvjdIQcBbzRoAoForvJlXi3iBoGFxNvwrvdKNuV8egQHCvYDVuHmvsF1yBq-7MbzXYdsAa_COvDkkmddZ1ZHFixXeTrZ8eAFxjfYSHlqzxHDStQNyf0cbACNphZ-IpOR91m8knGRet-ZazHGkUaXVbc1dFroopL0g5DDmIAsG94aiKwZUpF5xg_6A7PtNIPMij6MxHZMoSOpIqXMP-TSS96lOpOLXd5eM6TqVh0vOn_WYFBb14fPzuQpTghaWmRuufoKJH6QPmKy-IIxxJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ستونی از دود در میدان نفتی الاحدب در استان واسط عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/138857" target="_blank">📅 13:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138856">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmMUmw3Qr8zE9_waObvwPi_MKRcx4skI3EgeYQ4I96WJ7ER4ChmXWhCdgyYdIr6yzfhdfZoJ81nxfIilt7N7GlHgE-UoFy_fhv6WBSkYVULLDtjDvTrUSdfrzjGfUEjbs2R_YBLkt3ErK4VYxoIMuwe_fR6eQ9c9o6xIXQWvyoMYbmq6IzekaLOmu5P43eOHRbhyVN43aTIHLna5_V02Rhz1O0Yx4af72eKZMFd7Ddom61A-j7IyQyruVPHONNsx_3soe1wTiPmVFeH29S6RqNMXc2QW6_RQ2SwX0ohd0QvAmHUupE-91o_nHpj5hT3WCGsswG05pcsRk73Uvef_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک سوخت‌رسان هوایی KC-135R نیروی هوایی ایالات متحده که در یک برخورد هوایی کشنده در مرز عراق در مارس ۲۰۲۶ درگیر شده بود، برای اولین بار پس از حادثه در فرودگاه بن گوریون تل‌آویو روی زمین شناسایی شده است
🔴
این هواپیما با شماره دم ۶۳-۸۰۱۷، در برخورد با یک KC-135R دیگر آسیب دید و با بخشی از دم خود که گم شده بود، فرود اضطراری انجام داد.
🔴
هواپیمای سوخت‌رسان اکنون در حال پخش کد تماس "RCH564" است که نشان می‌دهد تعمیر شده و ممکن است به زودی به ایالات متحده قاره‌ای بازگردد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/138856" target="_blank">📅 13:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138855">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAIJj9LS26Mtp1ekMKn0jUOPd_ucGG3RiRd1wEzsoQpQQF9h2eMzfmYtljcC-FEqR_1ZtfYvXsZ2fI8UYoA4ByIxQAmicGYl2bIOa_3WKuEcenraCBegB9nluHPHg23-jjANWY01_9XiB0vu0W3C2tJg5tpeWGIQyDcfr-kXcoSdIggkkA5RPXyAxm5GMOZlf8ujvgi8yjwV6wCE6cykJPzyoSJxuyRGondZtCjPCRWxzMh4G2vfElpwG_HlPkwU4Bw8e7A-nDouWvuGZVjw2dRyvXEIhY1ccHqgYjTGqXJeJoCDo-L1mm1-_OA3P98R7kflJeEFHJH4XtZ2Y_f74A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده ولی فقیه تو‌ سپاه:
آقا مجتبی خامنه‌ای رو
خدا
انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138855" target="_blank">📅 13:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138854">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
زمین‌لرزه‌ای به بزرگی 4.6 ریشتر، ظهر امروز منطقه دیباج در استان سمنان را لرزاند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/138854" target="_blank">📅 13:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138853">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
روایت سی.بی.اس از رقابت نتانیاهو و بن‌سلمان برای شکل‌دهی به سیاست ترامپ در قبال ایران: سعودی نگران است نخست‌وزیر اسرائیل به دنبال تشدید بیشتر درگیری‌ها باشد
🔴
نتانیاهو سه پیشنهاد به ترامپ دادن، از جمله ادامه محاصره و اجرای حملات علیه مسیرهای زمینی انتقال تجهیزات
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138853" target="_blank">📅 13:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138852">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a7007d893.mp4?token=PaBscM-lo_S9RQlCndXAx86W28ao_H_gNXpWgVNJOM-IsRiVx_X_J1CPTT6DHMc0F-74z38MeMRM8Qck52sf4ptcl8FBi-EchmpLMRyYtY6jks_ubPi4gFM6PTfsNRZy0dMpmbfleKxL2dxF16e9YBV-AI4fPAA89dO3CA_xJrDb1s1lwXmGnwduSOc5gZpGgTXaO4xNrORKtKh27-2thQShjQIYaJE44LViGRdswso4IJMn1xw_ovuK7heAGGua8M5By7cFKjqCWEDyl3bpCLTSVgga4bVlrp1q4WcjRDh5jLbc92wElx5yik-7cLbISs43-h8-TWnJfPxgx2Xa4XwqhROvlDNzYAdoBIQFf5Zsd7k3LzSWVhWh960yM2C_TeZlBqaojB_ATjWIVGt7XyW9s843yYF9yp3l_hy-uxzolRgHaxdJilGL7tw6dGyE-hKEFfHMjPqPbB45IjWEEcS_9gv0hAvH5eehX6sj-ZLRmMO_HKlMY4egvdJsLdblqcKOSpplVRuPVTFldIrOSAWuQMw4W4aM6ggUYocP-OXMTSWSIfmN75b_-wapz848z-LF9ukYLjKZshaJs_vcITpJX60vkXBEitUAxJJ22I39CRAX9PxMB1rOf39UzenH809ufqxaQ5JTmbDdqxKiDJXmQWlFXnFtK_lUHvG2lJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a7007d893.mp4?token=PaBscM-lo_S9RQlCndXAx86W28ao_H_gNXpWgVNJOM-IsRiVx_X_J1CPTT6DHMc0F-74z38MeMRM8Qck52sf4ptcl8FBi-EchmpLMRyYtY6jks_ubPi4gFM6PTfsNRZy0dMpmbfleKxL2dxF16e9YBV-AI4fPAA89dO3CA_xJrDb1s1lwXmGnwduSOc5gZpGgTXaO4xNrORKtKh27-2thQShjQIYaJE44LViGRdswso4IJMn1xw_ovuK7heAGGua8M5By7cFKjqCWEDyl3bpCLTSVgga4bVlrp1q4WcjRDh5jLbc92wElx5yik-7cLbISs43-h8-TWnJfPxgx2Xa4XwqhROvlDNzYAdoBIQFf5Zsd7k3LzSWVhWh960yM2C_TeZlBqaojB_ATjWIVGt7XyW9s843yYF9yp3l_hy-uxzolRgHaxdJilGL7tw6dGyE-hKEFfHMjPqPbB45IjWEEcS_9gv0hAvH5eehX6sj-ZLRmMO_HKlMY4egvdJsLdblqcKOSpplVRuPVTFldIrOSAWuQMw4W4aM6ggUYocP-OXMTSWSIfmN75b_-wapz848z-LF9ukYLjKZshaJs_vcITpJX60vkXBEitUAxJJ22I39CRAX9PxMB1rOf39UzenH809ufqxaQ5JTmbDdqxKiDJXmQWlFXnFtK_lUHvG2lJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دو سرباز روس هنگام حرکت؛
با (ATV) روی مین ضدتانک رفتن و انفجار رخُ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138852" target="_blank">📅 12:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138851">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02807afcad.mp4?token=kBGAAH-fDqPDHnHeC9OHdoVVTJUJLF95menqiCgf6izCSEMC3FpI2zKORnh57gDcomKjND5QQR-FnibJZrGg4IoUB50zz72uOwiKz0Orlq94AL7UzjIuR9CospjGp7tcD7YiQRPKPsNhxxrg0hrLfy5_CU4ONGDj7vZ9C60KVfO1IO8RwJXrfmwV-dyx3k4NrsHmzDs4cVGJKtGpVeuC-v4m5td4UJLGjOsrD-KsPV2yNQFXWbm1VtnScBjyIranUOzkIgrG7Smu_PYqsq-HiipZ7_X5YHxc3eXms2LnDTUzxlaeLPKrRBqkWBrzDn7H2HUPe4aEGswtpl0ygS3UQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02807afcad.mp4?token=kBGAAH-fDqPDHnHeC9OHdoVVTJUJLF95menqiCgf6izCSEMC3FpI2zKORnh57gDcomKjND5QQR-FnibJZrGg4IoUB50zz72uOwiKz0Orlq94AL7UzjIuR9CospjGp7tcD7YiQRPKPsNhxxrg0hrLfy5_CU4ONGDj7vZ9C60KVfO1IO8RwJXrfmwV-dyx3k4NrsHmzDs4cVGJKtGpVeuC-v4m5td4UJLGjOsrD-KsPV2yNQFXWbm1VtnScBjyIranUOzkIgrG7Smu_PYqsq-HiipZ7_X5YHxc3eXms2LnDTUzxlaeLPKrRBqkWBrzDn7H2HUPe4aEGswtpl0ygS3UQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آزاده آل ایوب(خاله نرگس) مجری برنامه کودک دهه ۸۰ و ۹۰: تک تک بازداشتی‌های اعتراضات رو باید اعدام کرد و نباید به هیچکدومشون رحم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138851" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138849">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d9b65cfa.mp4?token=eQSQIXsR7A5CfeHnSkz6km0cQIabTSBUD2Lc9iu8xBKjQNkHt1RRYLpI3oo73z4p31RmviW9ibGA3nFCuvZ6NYUgqutKzKPwQv4Dp7NX1l0JyfGI8HlujSvCX5gilDm6NJHKwrnVjwkJVNBOvD55kX83MoA5_jy4l4QdyytnAw7n1xCBWyhzKgieXNYT9UQCsudqaH1FhNRb9GvpZJmhyLkgJa7Ak7M4PjIHAgSf9mK2i1o0yLwaQMFN3kWM0hEYBzdbZ4UvhD_m6XODmYKPtg_2ROOCxJfa7ZBV_a85UfYLQxtpabli-pmq8aR2J5DneA9zVRWuKml2egvBPr9AcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d9b65cfa.mp4?token=eQSQIXsR7A5CfeHnSkz6km0cQIabTSBUD2Lc9iu8xBKjQNkHt1RRYLpI3oo73z4p31RmviW9ibGA3nFCuvZ6NYUgqutKzKPwQv4Dp7NX1l0JyfGI8HlujSvCX5gilDm6NJHKwrnVjwkJVNBOvD55kX83MoA5_jy4l4QdyytnAw7n1xCBWyhzKgieXNYT9UQCsudqaH1FhNRb9GvpZJmhyLkgJa7Ak7M4PjIHAgSf9mK2i1o0yLwaQMFN3kWM0hEYBzdbZ4UvhD_m6XODmYKPtg_2ROOCxJfa7ZBV_a85UfYLQxtpabli-pmq8aR2J5DneA9zVRWuKml2egvBPr9AcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بخش هایی از مصاحبه محمد عرفان؛ بازپرس سابق جنایی:
ما همیشه از اعـدامی ها میپرسیم آخرین خواستتون چیه و هرچی باشه اجرا میکنیم. یکیشون گفت آخرین خواستم نیمروه. نشست ۱۵ تا تخم مرغ نیمرو خورد و بعدش اعـدامش کردیم.
یکی دیگم بود میگفت آخرین خواستم اینه که با خانوادم صحبت کنم؛ هرچی زنگ زدیم تلفنشون مشغول بود. ماهم دیگه اعـدامش کردیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/138849" target="_blank">📅 12:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138848">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b1eec1722.mp4?token=ZTTChgtycse8SpSiGpEAfx5Oce7y321ZdXalIGbZ0JVcJGsBeu0zvug9pr8aV7Kn4u1bv_rb2htzHcy9siKl7S-fyyjtB1ZPVgbLYEoEYRpARjhqDUBtzvFOg0Yv4DoSSrzUvYZids8nBbZrzT-ynHxnw8B8Bq8BpLnOn-YT6mlOXSHH-QyxDvc3ib0xA0Dip2Kedl-fFBIDLKlwv4z9YoPUhh6Vz-FivKHfB6xV0NOjZV2-AwapkSQFAYIcHIHxAkE5ck5RF0zM1_vKQ_U79BNHSq8soeTjxJ0huDWC538zdCcr5dpcZxXS3DcTCJs76-gmZuuLsY2WIGNcfk_2HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b1eec1722.mp4?token=ZTTChgtycse8SpSiGpEAfx5Oce7y321ZdXalIGbZ0JVcJGsBeu0zvug9pr8aV7Kn4u1bv_rb2htzHcy9siKl7S-fyyjtB1ZPVgbLYEoEYRpARjhqDUBtzvFOg0Yv4DoSSrzUvYZids8nBbZrzT-ynHxnw8B8Bq8BpLnOn-YT6mlOXSHH-QyxDvc3ib0xA0Dip2Kedl-fFBIDLKlwv4z9YoPUhh6Vz-FivKHfB6xV0NOjZV2-AwapkSQFAYIcHIHxAkE5ck5RF0zM1_vKQ_U79BNHSq8soeTjxJ0huDWC538zdCcr5dpcZxXS3DcTCJs76-gmZuuLsY2WIGNcfk_2HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شهروندان اسپانیایی در بارسلون اسپانیا، در حال نصب سیم خاردار بر روی بالکن های خود از ترس مهاجمان مسلمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138848" target="_blank">📅 12:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138847">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
سپاه : دو نفتکش متخلف تو تنگه هدف قرار گرفت و متوقف شد
🔴
۴ نفتکش دیگه هم بعد از هشدار، مسیرشون رو عوض کردن و برگشتند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/138847" target="_blank">📅 12:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138846">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU-QY2X4YXtZq8oq7_5YRuUHQQ28rVXG6gjIJwoGamIpBVuW0LIsdsPv3xr_fRsisRtpjQTxtKAIp0X58xf7xvhMN9eSA8RyjhcNE3sElO4zDhXrtjbAH6o_TItYkNl3Q4VJeADtQYgBVfDUbu4t3H5MNfDj6LIUROwZ3TlhpTXAuxawD-2GeRyWjBJb6QzQo0w_cbvepKan12HfvfBgA7tQoTU1PLXTJjKPoys01x3Sjw-TWuwDxMOdVJ1CMDVpE9OrT0F7SyF4O1JHd3KMMx7ZOjzEN27zvtvWsYeoKQ3FFQ6yzUDOWjrTn0nPpWvPKq30ILJ9JMIPrEMkfAYaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مسلمانان مراکشی به منطقه‌ای خودمختار متعلق به اسپانیا در شمال مراکش حمله کرده‌اند و تقریبا این شهر یعنی سئوتا را فتح کرده‌اند
🔴
سئوتا خارج از خاک اصلی اسپانیا هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/138846" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138845">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDC9BI6cYFLw0KWVJqOgP0glrXYebVnylptieSjwTNSixkeXyd2H7d0Qt2xLDFgyvVPmIa_U4QikGrIp8hasCB1-PWduikeAWPl_L_z5zuT0fMztOOdlVrVP-sIbVTZZl-h3O7nqLDmJMnzkiJZzjNZVN52uAV1oyJyzMVxqJK1gncObpokb7HOge8aN-ZeWC6UTFixPPr-zdncFRTwJbtgrxoZVCZjHkGm5bT9n7MSuQn-f73IkS3SKvMUgybXJGGY1xLFDWmCtOWTLiH5SAeeo9Xr8RMZGcHW-t359m0Yhts6dMN0fnWnSEpoXsyNDt1WxTmI_Hx1EGRikDTEPYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از پشت صحنه «مرد سه هزار چهره» به کارگردانی مهران مدیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/138845" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138844">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1225749b49.mp4?token=D66rxxH8s5unHRB6UcUqcGxTX5GQGw6OJ7lIxaIlYw6yQ02N_s0q1eG0EKn-4etgil8upNqa2_zVKjGMKqa9BbujtpWubxG_zrfaaQSbIUssKu-RufTAeIK27vPmQ_1-8id3f4t9FBbpo9rwBCvla7vEj-XaW9nkIxHEw2a44wYNV-8i_QhG5R7s2tEWtFD4gGTwitmI965veOB71hvfx98w1OSVavjp8zqZqrGz3_wUF-uwb4VONCFLVk_txXwmOviGylCS4BLcp5dP2xz5BkOvPQRMci9Bz4LbWsOsT0arUVW0alAMRPJXD6rf7mW2JZJNUPOajcYjM1jSePR8JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1225749b49.mp4?token=D66rxxH8s5unHRB6UcUqcGxTX5GQGw6OJ7lIxaIlYw6yQ02N_s0q1eG0EKn-4etgil8upNqa2_zVKjGMKqa9BbujtpWubxG_zrfaaQSbIUssKu-RufTAeIK27vPmQ_1-8id3f4t9FBbpo9rwBCvla7vEj-XaW9nkIxHEw2a44wYNV-8i_QhG5R7s2tEWtFD4gGTwitmI965veOB71hvfx98w1OSVavjp8zqZqrGz3_wUF-uwb4VONCFLVk_txXwmOviGylCS4BLcp5dP2xz5BkOvPQRMci9Bz4LbWsOsT0arUVW0alAMRPJXD6rf7mW2JZJNUPOajcYjM1jSePR8JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
هشتاد جلسه‌ی دادگاه برای اثبات جرم حمید نوری از جانیان شکنجه‌گر دهه ۶۰ در زندان گوهردشت در سوئد برگذار شد که این حرام زاده محکوم شناخته بشه که البته بعد از چند سال هم تاختش زدند و به رژیم جمهوری اسلامی برگشت.
🔴
برای حکم اعدامی که به محسن شکاری دادند فقط ۱۷ روز وقت گذاشتند.
🔴
حالا چطور میشه که کسانی که در دی ماه خونین بر اساس گفته های رژیم جمهوری اسلامی تعدادی از نیروهای انتظامی رو دستگیر کردند، شکنجه کردند و بعد آتش زدند ، بررسی مدارک جرم فقط در مدت ۶-۷ ماه انجام شده باشه!؟
🤔
مردم به وقتش پوست از کله این حرام زاده ها میکنن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/138844" target="_blank">📅 12:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138842">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6414829db4.mp4?token=bm_16AGLk8TWi09895ZMAZJsTA_kkemtEhSGtXES76VktjGM7SBP5kKcDsGXHAw1-FGgtBnC9n2XWTj39Gl9g-zZZniZQmSDWRmprOWCjvYbyGt70jAoeRgU0TpI80XXzkW6h8zkA6A2t6QTjtrkl3_SPuFexKfaNkKfBfXxXHe-IgKvhAtsIjdWIfAd-JS1UA_OvnY_41YsxF80dREo-yftpHh5tCJiq6zaKH8Nd2mnhqKpPqJAkHZj3xqW7Bte2jpnaEjj1EC6rnpO1yqFKJ3YyjjwojIdO9ev5boZqUKyQH4Fxa8I4cytjXycJ_fRV87-YavynWEEc8dsqBjHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6414829db4.mp4?token=bm_16AGLk8TWi09895ZMAZJsTA_kkemtEhSGtXES76VktjGM7SBP5kKcDsGXHAw1-FGgtBnC9n2XWTj39Gl9g-zZZniZQmSDWRmprOWCjvYbyGt70jAoeRgU0TpI80XXzkW6h8zkA6A2t6QTjtrkl3_SPuFexKfaNkKfBfXxXHe-IgKvhAtsIjdWIfAd-JS1UA_OvnY_41YsxF80dREo-yftpHh5tCJiq6zaKH8Nd2mnhqKpPqJAkHZj3xqW7Bte2jpnaEjj1EC6rnpO1yqFKJ3YyjjwojIdO9ev5boZqUKyQH4Fxa8I4cytjXycJ_fRV87-YavynWEEc8dsqBjHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اگر براتون سواله چرا این همه وحشت؟
🔴
چون دیشب مهاجمان مسلمان که تازه رسیده بودن به اسپانیا، ماشین های مردم را به آتش کشیدن و آهنگ های عربی را در خیابان های اسپانیا پخش کردند و به خونه مردم وارد شدند و از آنجا دزدی کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/138842" target="_blank">📅 12:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138841">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=MI-dX3SpRnl287hZECMqKiO9ffTpb0GPD7wwh9CFdRdRE7OXfDv2xWniD4xeiqdv6z01mrJZdXBcGu2Gchc42d3CWWi3g02V5d1ds5d0Qrbtjg_K-GCxIfD2sSWpd_huo0veTXi2lHAJBIR7wXwwp18so9ppL4BhEmE1AMQfeYxG0iGDY3vGSarPZ9xRSFHciDidaRG1ike8durxjso2PK7gGKc-WO4BfqFxsvreVnuEIJg9GtotbYXmnV46RwfYOEEK-CVOFinCNaMW4yinMGVM8usfO_z8CRFVfy1dGFKgMgaebCKoi18rFOxc1WD5Y13xBCbR70bf49xyq-1gNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff08dba4f.mp4?token=MI-dX3SpRnl287hZECMqKiO9ffTpb0GPD7wwh9CFdRdRE7OXfDv2xWniD4xeiqdv6z01mrJZdXBcGu2Gchc42d3CWWi3g02V5d1ds5d0Qrbtjg_K-GCxIfD2sSWpd_huo0veTXi2lHAJBIR7wXwwp18so9ppL4BhEmE1AMQfeYxG0iGDY3vGSarPZ9xRSFHciDidaRG1ike8durxjso2PK7gGKc-WO4BfqFxsvreVnuEIJg9GtotbYXmnV46RwfYOEEK-CVOFinCNaMW4yinMGVM8usfO_z8CRFVfy1dGFKgMgaebCKoi18rFOxc1WD5Y13xBCbR70bf49xyq-1gNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روز دوم تهاجم مسلمانان به اسپانیا آغاز شد.
🔴
خیلی از اسپانیایی ها از پادشاه اسپانیا خواسته اند پدرو سانچز را خلع کند و ارتش اسپانیا را به مرز های جنوبی بفرستد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/138841" target="_blank">📅 12:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138840">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gr0zqmSQMeMMgAa5cYG7YQ4WFgfHhK-kQi7uZpdMQhq9-sTLjob55ylFMFdnSvYMq1-StB6ta_ewAm_EfN8mY68fe-fGT3WqZuAy5pQEW6x3hHmrm6AGJjMWe8ySEX1_4M30V2vIspU83xaccsFc6dc0wyi3pDRaM3sXPlHdb617pJjO--sCY3_JIThBfAaw1Hb8UXSlkRLR_rNgSspp4eMIvXNgXfVFoQmgUpMNlMkEEhxxKYdiUnBPhtnXoNX2giwt4mG6BKuhPVaqe2WQ_vL6To1IfSDC-DHC0DBdKS_t0PyuFJnLGY8K0wBoPI3T5b2LfG4uNNQYomn9hnLhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار بلومبرگ: جالب است که سنتکام هیچ حمله شبانه‌ای علیه ایران انجام نداد. خیلی زود است که بگوییم آیا ایالات متحده به الگوی اعمال محاصره برمی‌گردد یا خیر. و اینکه آیا این نشانه‌ای از ادامه مذاکرات دیپلماتیک است (یا خیر)
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/138840" target="_blank">📅 12:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138839">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DITrDiAFZB0xu86-3fMQGmCKO09pt-byGvoG37rRuDcX-lyi27429ZU3UGpGcfSndkgZk6cJj6wXhQVR9rDoZxDxRN-o_odI6csbHuA6G2zXCLIVbRH76cztQbx0FLmi56vWzDSm7Ku1kz5ZalHjqbMNwg8MMZGgaDPRrYXgmoHM4Vzy-rkthHDC4mLsrBxk5fR-wpOEJlCF3g6dSMgdE6cVjkVpNM-5asCkxGVIemtb8UEQIhtsb7mBlGobpcUIFBQOhJXU3VXj-BBFSE1LkQv2lJWjj_5ij_J8b6Ec2-LUQrCY48_-XQDnMI-wgG1LZki_hmiCHVug6uwAAF4JkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/138839" target="_blank">📅 12:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138838">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
حادثه امنیتی در اسرائیل /منابع عربی: یک سرباز، سلاح یک نظامی را ربوده و به سمت سربازان ارتش اسرائیل شلیک کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/138838" target="_blank">📅 12:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138837">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
بلومبرگ گزارش داده شش نفتکش سعودی پس از تهدید حوثی‌ها علیه کشتی‌های عازم بنادر دریای سرخ، مسیر خود را از تنگه باب‌المندب تغییر داده‌اند.
🔴
دو نفتکش بسیار بزرگ به‌سوی جبل‌الطارق و چهار نفتکش دیگر به‌سمت بنادر آفریقای جنوبی می‌روند؛ مسیری طولانی‌تر و پرهزینه‌تر که نشان می‌دهد ناامنی دریای سرخ حالا مستقیماً مسیر صادرات نفت عربستان را به هم زده است
🔴
یک تهدید، هزاران کیلومتر مسیر اضافه
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138837" target="_blank">📅 12:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138836">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بر اساس گزارش‌ها، نیروهای سعودی مشاهده شده‌اند که از مناطق شرقی یمن عقب‌نشینی می‌کنند، که احتمالاً در حال آماده‌سازی برای یک عملیات نظامی زمینی علیه حوثی‌ها هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/138836" target="_blank">📅 12:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138835">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a16a391bce.mp4?token=OWxbxFW05EWruZLI-2wsBKTF0UgSPXWM3qjoVn2t8oAZT2XsU-Clllivpg3bdT6fy8UJaa43hxgCOB747Xh3_UgvJGAiLVvz_-qFteS4dZQN-qSlvoLliyGK88iGWV0jIrAwvb6I5PhwvNchjYvYPc2Ce4AySKtEGUeYACwdah0DNjZO7IuzUpjPQqFOTRpLm7BWWrcacyQFhwqEMqvhzApRU17xt79kpk3H-mM2ITpREXs3WxC-tBLIpI_eKpKCGWr-6aMlInrc7VzRgPXL37hX9FheoLQZqIbSCB1Y4gtckWY9uBRIv09WK9ROACHsKtVoH_qQJeTuw5rrpCoE4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a16a391bce.mp4?token=OWxbxFW05EWruZLI-2wsBKTF0UgSPXWM3qjoVn2t8oAZT2XsU-Clllivpg3bdT6fy8UJaa43hxgCOB747Xh3_UgvJGAiLVvz_-qFteS4dZQN-qSlvoLliyGK88iGWV0jIrAwvb6I5PhwvNchjYvYPc2Ce4AySKtEGUeYACwdah0DNjZO7IuzUpjPQqFOTRpLm7BWWrcacyQFhwqEMqvhzApRU17xt79kpk3H-mM2ITpREXs3WxC-tBLIpI_eKpKCGWr-6aMlInrc7VzRgPXL37hX9FheoLQZqIbSCB1Y4gtckWY9uBRIv09WK9ROACHsKtVoH_qQJeTuw5rrpCoE4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک عبور مهاجران از مرز و ورود آنها به شهر سئوتای اسپانیا را به آخرالزمان زامبی‌ها تشبیه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/138835" target="_blank">📅 12:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138834">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/094c83504a.mp4?token=VCGYQ61Z_Y8Z3JrlQVAFrIKxTon4aDZa4b5E3Yg8KQaxEHHLqA2bSBInu8T-fmL-KKQOeQZUBNNYasSnYzHh9wA7XAA5YFQHQbrlb_61cNXN9ujR14lMVWPCd2bgQ5cAiG6IOUh11xymMgmKBPKXEp5svrckRWZscsdSM35gxVbCcqQbkFlmd3tO2Dfnk1K6iY0NLrhcJAEh8VpYgLslfEGglfGgQjQ5EKrrLwKymfii3vSt6zelz0YHNP5BREqflnS8i124xRcGUbzXkds54bedUNbCTK_rEPNt2vZfl2SRPP6Tb5PGLaLp1PajjemREJrN4XLsxj236xshFM9-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/094c83504a.mp4?token=VCGYQ61Z_Y8Z3JrlQVAFrIKxTon4aDZa4b5E3Yg8KQaxEHHLqA2bSBInu8T-fmL-KKQOeQZUBNNYasSnYzHh9wA7XAA5YFQHQbrlb_61cNXN9ujR14lMVWPCd2bgQ5cAiG6IOUh11xymMgmKBPKXEp5svrckRWZscsdSM35gxVbCcqQbkFlmd3tO2Dfnk1K6iY0NLrhcJAEh8VpYgLslfEGglfGgQjQ5EKrrLwKymfii3vSt6zelz0YHNP5BREqflnS8i124xRcGUbzXkds54bedUNbCTK_rEPNt2vZfl2SRPP6Tb5PGLaLp1PajjemREJrN4XLsxj236xshFM9-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال : می‌دونید تا الان چند نفر از روس‌ها تو این جنگ کُشته شدن؟ آماری ازش دارید؟
🔴
زلنسکی : طبق برآورد ما، مجموع تلفات نیروهای روسیه به حدود ۱ میلیون و ۶۰۰ هزار نفر رسیده
🔴
از این تعداد، حدود ۷۰۰ هزار نفر کُشته شده‌، البته این فقط یک برآورد تقریبیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138834" target="_blank">📅 12:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138833">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
وزارت خارجه چین کشته شدن یک شهروند چینی در کویت را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/138833" target="_blank">📅 12:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138832">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بی‌بی‌سی: در ۲۴ ساعت گذشته ۴۹ هزار نفر از مهاجرین مراکشی از طریق دریا وارد شهر سئوتا اسپانیا شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138832" target="_blank">📅 12:03 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138831">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgL-dGtmiSAveieYngbyiBwgZ-b-_-1gQlcZRWdQp6uMB6IHwMp3I7GwHFbKMArSQrlCFLBU88bsXglFtSn2skx9DF_HoEhjLQCygzbe-s5GVG6-5-EqXYF5kpfPFKG4taD4vPPk2dAzxkaKEBMGExutnwKfE8VYLvdfcU01cUo5Ilm0o8Ss23_SjjjEMS2uq_6c3iUe6sGM6owUterm6fPaDS513uVXdVdAE9PXfcYV3eX496JiXVKrWCJ8mFrw4aoVcL2ANgdzMPkiFbay4NJgUsJwpulZOq3HmhBjiy_N0JEInPkRZLcPxtRjGYTIN--MKpDwEXak_dA_Q8XOmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوووووری/زیرنویس شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138831" target="_blank">📅 11:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138830">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=vUGvwX3Ck7R7daZ6SPMaJslk4YcYa3CqSDhxFjpDBtK7QwEY82HfMEI3g_BbnQxbFSeHI0hycjDFCHFtBZzO6_CSk0eJI2ACpGIljLzZitx19YtXKJNyiWdR6-FzoA4VJzHePGcNLIKIV5vWz0aGpd-xU-xkcw17_MVrA5zNEl1TBUEvVkf6YA-XxTXBwL2Y28cTJ5UrIJ2Qkjw8V8uaxm3WpD0vmtFyCUx-7Ft38ycPTBFEwCXOuXWwF5aCeAfwoVNAlESH3PBraZQxZNm1v6njT67XUEpVI5t3a00gbDy45on9QcTioLD1pP9nc_uDivgx8x6GDtPzlLFgbScKxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2b5c3f0e5.mp4?token=vUGvwX3Ck7R7daZ6SPMaJslk4YcYa3CqSDhxFjpDBtK7QwEY82HfMEI3g_BbnQxbFSeHI0hycjDFCHFtBZzO6_CSk0eJI2ACpGIljLzZitx19YtXKJNyiWdR6-FzoA4VJzHePGcNLIKIV5vWz0aGpd-xU-xkcw17_MVrA5zNEl1TBUEvVkf6YA-XxTXBwL2Y28cTJ5UrIJ2Qkjw8V8uaxm3WpD0vmtFyCUx-7Ft38ycPTBFEwCXOuXWwF5aCeAfwoVNAlESH3PBraZQxZNm1v6njT67XUEpVI5t3a00gbDy45on9QcTioLD1pP9nc_uDivgx8x6GDtPzlLFgbScKxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ی هجوم مهاجران غیرقانونی که حصار مرزی را در ملیلیا  شکسته و وارد خاک اسپانیا می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138830" target="_blank">📅 11:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138829">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/138829" target="_blank">📅 11:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138828">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا در حال بازنگری در حضور نظامی خود در کویت است
🔴
ایالات متحده در حال بازنگری در سطح حضور نظامی خود در کویت است. واشنگتن روابط مستحکمی با کویت دارد و این کشور را شریکی مهم در حفظ ثبات منطقه می‌داند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/138828" target="_blank">📅 11:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138827">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9Xq11_J_6S9-CkbaV3Y-QZ7yZPUrasBFWwV06vJIQz78AkjLbLHx2sQjfiATG_YqAiZJ8XLLmft-aaYVlHplxaXzD3WJ3fgua9QNOzrfeuyjI1_ACmxAug0jyrA67y7qHA9-_AqCUfPDYxyYaFuPahAO3KqGE1_1gL2U0klt3MQsJTHl9jQl8KoFH8_LjRz4EDwhh57PmGeDh5rd0PZYgzZuQHAd7flThq37hp2oT2euKub0A6Aw3C1JZfHHN2-TUzqUQFBtf3i5fC1M2tsUJBoKvaqNZ_hrVKhEXM6GDnkLz_m5In7adicSooJtCOzuTM0DhAAqU11XlOBJ5-IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار آکسیوس: به گفته یک منبع آگاه، مقامات سپاه پاسداران از هیئت حماس که برای مراسم تشییع جنازه علی خامنه‌ای، رهبر سابق ایران، به این کشور سفر کرده بود، خواستند که در امضای توافق‌نامه عجله نکند و وقت‌کشی کند
🔴
یک مقام ارشد آمریکایی ادعا کرد که ایران سعی کرده حماس را متقاعد کند که توافق‌نامه را امضا نکند، اما این گروه ترجیح داده به حرف آنها گوش ندهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138827" target="_blank">📅 11:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138826">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
یک مسئول حماس به خبرگزاری رویترز گفت: توافق غزه باید به صورت مرحله‌ای اجرا شود، اما اسرائیل باید نیروهای خود را از این منطقه خارج کند.
🔴
پس از توافق طرفین بر سر متن این توافق، اسرائیل باید اجرای مرحله اول را آغاز کند.
🔴
همچنین، گروه‌های مسلح مورد حمایت اسرائیل باید منحل شوند. اگر اسرائیل با این توافق موافقت نکند، ما آن را اجرا نخواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/138826" target="_blank">📅 11:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=D7_as1YvZTPge_pNCbrbQraNyxt6YzRcxYDcpf97fp3PHj63eKWjdSqaVGvPKv60eVTfqDcWf-FS36rYbuUDbke55eDirUEYe_9FMiZUn8K4h15vzRAHRnIOAWmVxnjGnngMcd8BqOfhkleyIurtvokG-46UQlnX3KBwx6aajBA7-sC7q_bxWcoSnmqeg0WcfkquOhSU44lKCo9sJPvvrffjsFgJpncmAsbwcPJOy15Lv98tB_nwIA6k-SiIzrSB-6vzmRAF-teTJkzc6uPz_eC61-gumNzSrJA0hX63sGstTc5e5U0XUjmxHpkOh0pESNzXnX_TSMgyw4bZh5SRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2964e2f72d.mp4?token=D7_as1YvZTPge_pNCbrbQraNyxt6YzRcxYDcpf97fp3PHj63eKWjdSqaVGvPKv60eVTfqDcWf-FS36rYbuUDbke55eDirUEYe_9FMiZUn8K4h15vzRAHRnIOAWmVxnjGnngMcd8BqOfhkleyIurtvokG-46UQlnX3KBwx6aajBA7-sC7q_bxWcoSnmqeg0WcfkquOhSU44lKCo9sJPvvrffjsFgJpncmAsbwcPJOy15Lv98tB_nwIA6k-SiIzrSB-6vzmRAF-teTJkzc6uPz_eC61-gumNzSrJA0hX63sGstTc5e5U0XUjmxHpkOh0pESNzXnX_TSMgyw4bZh5SRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جواد موگویی جای همه رو لو داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138825" target="_blank">📅 11:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rctaq5prVhaeaPR7tuj_AWk9Cwm-uFc3OrGrI_gEtZ_7QytZEDSu6mxB2BSOT80lFFHTGxDiRHCsxICCIKSnxz3UO2IJtvkpLyupKLoOo2pZS9NONPXXc_mYnp8GwAUH3uUAuisnZ52qH4QKowclydysULTA3cSGlqH3XFKyirx4iofmJ5slHPPTMF9gb88Mxoq_t503jJCMZkNYJGo1m8bLq9RxOEeiy670cXnTVzFziVTDAczAdf5HGL3WpEIQAFDztSsv6Yhg5cr1SRaw0LpfZ1zh1P060l_ivMLddOgvBI6LWXC0FsEp9apKjk8PnVYzNRPVS3QFWXM36sRtXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: فک نکنم‌ جنگ بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138824" target="_blank">📅 11:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
ارتش روسیه به وسیله کوادکوپترهای انتحاری، تعدادی از پمپ بنزین های اوکراین را منهدم کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138823" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hsnf-MACyQJoRr0xPnE28rgxuFHvZfg5iDblUEVwp4iN7CP1L4Sd-Xreb-vGL-5eR3Mrj3mFQfZilQsVjORbGY5TthfsOE-c4QKg1R6paKy1fTdxnYWwgL-oyC_yOQQ9zhoZC-fonNNzn9rZTtklXmzaTOEuLhxqb1_4rc0UJLFRcyQD-wCQfnJyn9UK2nQhhlHS05UPM7ld5bQvV3pzL_LBlcu_UzkoaQXnEGDyz7z0hxftsfdmJ3La7bRjT8bnyZhOjhYeznfszKoyuHJS2cNwaYFGe-JFBiDTHK88a2nV3dWn1jn3yCmSFX3H2V-EsD1dWJe28PVGULS6sq6rtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پسر دهه هشتادی رئیس بانک سپه، معاون بانک دی شد
🔴
پ.ن: لابد اینم امام زمان انتخاب کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138822" target="_blank">📅 11:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
روزنامه «الاخبار» نوشته اردوغان در گفتگو با عون، رئیس‌جمهور لبنان، به او توصیه کرده در توافق با اسرائیل شتاب نکند زیرا اسرائیل هدفش صلح با هیچ‌کسی نیست.
🔴
اردوغان به عون توصیه کرده که سعی کند با سفر به دمشق و دیدار با الجولانی،  روابط خود با سوریه را تقویت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138821" target="_blank">📅 11:11 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138820">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/138820" target="_blank">📅 11:04 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138819">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=XFoNXzT3NUdHgrxEd4ZXDAIWnTYieVLcE-4CZ6U6MGG56jLlJLonVBghfFWUkPIIoFD18kil7HLmfsnrKq7XKW_Z8f5Ho9Abz1BNOaII0aaTnH1f0V35JDAbqqEt6ZzhkF-A0I5zYY-DGfUuwALPlLNUdui22U58QKVkO7PzctXh9SsRd4BbxUHGoaBY1oG9BBnr0uytHc5Bv57j82i65x0jWK51J3kI_9gSW534TlFTx8LkQx_g8DVKW0VVU9fFubsnft5UFJtdZQiPJeZFOxl9SNRJ72KftxV3zH5LJ6HDABwCARLJg9CEiCOkZjwAXSyMB6zv81e9B01-5-0oVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5451fd068.mp4?token=XFoNXzT3NUdHgrxEd4ZXDAIWnTYieVLcE-4CZ6U6MGG56jLlJLonVBghfFWUkPIIoFD18kil7HLmfsnrKq7XKW_Z8f5Ho9Abz1BNOaII0aaTnH1f0V35JDAbqqEt6ZzhkF-A0I5zYY-DGfUuwALPlLNUdui22U58QKVkO7PzctXh9SsRd4BbxUHGoaBY1oG9BBnr0uytHc5Bv57j82i65x0jWK51J3kI_9gSW534TlFTx8LkQx_g8DVKW0VVU9fFubsnft5UFJtdZQiPJeZFOxl9SNRJ72KftxV3zH5LJ6HDABwCARLJg9CEiCOkZjwAXSyMB6zv81e9B01-5-0oVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون منتسب به یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138819" target="_blank">📅 10:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره: قیمت نفت کاهش یافت، اما در مسیر ثبت رشد ماهانه ۲۰ درصدی قرار دارد
🔴
قیمت نفت روز جمعه کاهش یافت، اما همچنان در مسیر ثبت رشد ماهانه نزدیک به ۲۰ درصد قرار دارد. نفت برنت با کاهش ۱٫۰۳ دلار (۱٫۲ درصد) به ۸۸ دلار در هر بشکه رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138817" target="_blank">📅 10:45 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nt-lpZpjBJIvLmsOW6IDTVWLyBL5sd1m8Ehp5KLHlKA1kqYjhFxRuogY_R47HF6hf_hq85R15aBRQMdWNk4CiF0zw7Q6u113FtgkjjrXlwhIJ8zkZhJLbXjNysm-kn6Jxl0RYO8biaNJAdZTGScHHpok1TZ3VX-1FJYG5TJmtxB5JqejQGCDEHm1MK--vf3w5YcZ3TrpWkpf4Fj1Vo6rZuNcduoJCPb8Ydw4OY-FaBWzVnRg4cCGZcduztbYFRTfPhJS3XE3zze22h27spWcmXykZBO7jjvb8AngGjLb3Er_7yDItWXHEjNk7khCg-iYBSoVIRUMUuNdEdMc8uk_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بی‌بی‌سی:یک شهروند بریتانیایی به اتهام جاسوسی برای سپاه پاسداران انقلاب اسلامی ایران، دستگیر شد. او به جمع‌آوری اطلاعات درباره یک پایگاه نظامی بریتانیایی در قبرس متهم است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/138816" target="_blank">📅 10:40 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmrWlHz_r4ldo_GuuoJ6gwa1xrX9eCWwhv6AawzfHoRBzJTUhQ-_mO3JCksTQoJHFdMHExhCqYm_M1i49lJT4oXX30SZkiL29sfJwPsTZkhLpL8mAJrL7R1fe5B7UwROU-Gje_ohFZhtixQOQp6qR_6ABIowXUb4CsFj4oXOSXbfgIE-NfY1_Kwk9p55kBurt0FA-jYxccqDNO8nwQ3s1cJWDHyZ0hthf0IMG_Y2po4lyIL-7i_n9dQcBfkydRNbYG1oBmW44FVsPnI9BeWFhAc2mzcdkwc0XIpl__1dQfy5SEWA5o6d3XEZ2TVNmSU9lfSMUDM1v9SlaE6qW-aIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مطهری: ممکن است یک آمریکایی انتقام خون رهبر را بگیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138815" target="_blank">📅 10:35 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شورای صلح غزه: حماس به‌طور رسمی متعهد شده است یک برنامه اجرایی برای واگذاری همه سلاح‌های خود را اجرا کند.
🔴
اقدامی که در ادامه آن، خروج نیروهای اسرائیلی از غزه انجام خواهد شد.
🔴
این طرح همچنین «نویدبخش مزایای قابل‌توجهی برای مردم غزه است؛ مردمی که مدت‌هاست در انتظار آینده‌ای بهتر هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138814" target="_blank">📅 10:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmJdY-LGjGFRDKVovFLc6rOz_h4CTqQmdV5auIlxOOCIaF2Rqx5rNjFUXo3ozqslS6-3QLhGchj28IaibQG2UeWFViT3TB1l5v4dKh14iaucri78cWIriPxIqSveMi4u17E9W1qn-0U77HF6_pZuNwuQA4XJw0P4c2hkw7I6HJdaZWy8irLZzc-eHfTFPjF00CGyXdvWoa4-qxByn3m_WKJrS3-6R1Wncc0Q_3sn19hhxfwNu3b0RNQ6pAGlJ8edwzYGhx_K19c1OlTPBXi-LxdOinOnGl3Vc6ZT6ngnHvq2gkbfzAcWYz8EoYM0YWyLCcscFTdsm3tJfgASfNDRzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آپدیت بازار کریپتو ۹مرداد ماه
🔴
مارکت کپ: ۲.۲  تریلیون دلار
🔴
شاخص ترس/طمع: ۳۷%
🔴
قیمت تتر: ۱۹۳,۱۴۷ تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138813" target="_blank">📅 10:26 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138812">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1510e3d07f.mp4?token=NYr5IcJFXQnph69WeSmLRYkpN1BvvJz9iUNJ0qIFsRXu7zsCxxwHauV3slFLHV0CI4qpFFsoiGSRT9otrf8kMw6ZTdnKniXl1ShfvKphHtfxGJ8W4EKWl-ecF-dsPyLiChw7lCjHgbfYi4op4LffuuAKL_IUR8-BIhWOi70zTJMK9QP9z7aIsAJ2C7xORXvc9ZSGcoG1phUZ2IGCE3FvoGmvgnCaN8bowkbAOA9P_e3mRoSvMEI0nKxutUP6KgZvshU5xIKR_dlxQtelz1bB_8DvtG2soT9pLDnUZHfaOBPJBwqTO-EoI4HmV_g6kWPyRUBmn7L-ywFg5sCPXwAhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1510e3d07f.mp4?token=NYr5IcJFXQnph69WeSmLRYkpN1BvvJz9iUNJ0qIFsRXu7zsCxxwHauV3slFLHV0CI4qpFFsoiGSRT9otrf8kMw6ZTdnKniXl1ShfvKphHtfxGJ8W4EKWl-ecF-dsPyLiChw7lCjHgbfYi4op4LffuuAKL_IUR8-BIhWOi70zTJMK9QP9z7aIsAJ2C7xORXvc9ZSGcoG1phUZ2IGCE3FvoGmvgnCaN8bowkbAOA9P_e3mRoSvMEI0nKxutUP6KgZvshU5xIKR_dlxQtelz1bB_8DvtG2soT9pLDnUZHfaOBPJBwqTO-EoI4HmV_g6kWPyRUBmn7L-ywFg5sCPXwAhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی: در نیمه شمالی کشور دمای هوا روند کاهشی خواهد داشت
🔴
برخی مناطق جنوب کشور و سواحل دریای خزر با رگبار و رعد و برق همراه خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138812" target="_blank">📅 10:21 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138811">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7007c9b457.mp4?token=JXJ-p1VBS3hiir-Krir9F0ePUw2x1yoN8g9w6vyd_Wk6864YMxGzUBtVCpT3lwtmwdvcg1QoiM0xYRCMGgO2MuhxAC3h1_brFWM1F9eQsqehBDp-Wx3thxZoRH6KrZVChnifS1crlAUrCzLC5s5Ih6RuB50dyk8yS5YiMgnNEYru90KQ5o5b6wOGNIIOhUJO8LXC4yC3bwijFQPTWk9R3AcQAummSRJdpP-72A6OFD7tQiusgHQwDlxHUeBfuxkSb1zFnrKePO0HaoAK9iaXhKyqL5BjWnsRI2GZ8ESU14N4-YQcQxvGv75RzSR8onUPejYRHBIHwNMFUDKIezcWUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7007c9b457.mp4?token=JXJ-p1VBS3hiir-Krir9F0ePUw2x1yoN8g9w6vyd_Wk6864YMxGzUBtVCpT3lwtmwdvcg1QoiM0xYRCMGgO2MuhxAC3h1_brFWM1F9eQsqehBDp-Wx3thxZoRH6KrZVChnifS1crlAUrCzLC5s5Ih6RuB50dyk8yS5YiMgnNEYru90KQ5o5b6wOGNIIOhUJO8LXC4yC3bwijFQPTWk9R3AcQAummSRJdpP-72A6OFD7tQiusgHQwDlxHUeBfuxkSb1zFnrKePO0HaoAK9iaXhKyqL5BjWnsRI2GZ8ESU14N4-YQcQxvGv75RzSR8onUPejYRHBIHwNMFUDKIezcWUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای Sentinel-2 نشان می‌دهد که پس از حملات اخیر موشک‌های بالستیک ایران، آسیب‌های جدیدی در پایگاه هوایی علی السالم کویت ایجاد شده است.
🔴
در این تصاویر، یک اثر سوختگی در یک سوله انبار که توسط نیروهای آمریکایی استفاده می‌شود، مشاهده می‌شود؛ اثری که با اصابت مستقیم یک پرتابه مطابقت دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138811" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138810">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1da03a51b1.mp4?token=lEXybn0OJ2IyKK0Wnf1m4hkZ36KAL4cZtwXnbdYisl2I0faH9iwF2xqj30rJTBCt4C2WsZ0kOy_jpVFa7xx4Fl1fh36jpkDzETIFwlUA9tk81VOzQ9n3KdBbeDSo5jx4XygxH6B0MXcWq_Vq9Ts3GU0Z86fTWNDJILFBwcPkGP5UjylXhfmZeh7D5a-3nGF1hIYJoETWtYrbW6z6jJhukCYZ7mEXMe1o5-acHMhyLksPaxqWc8S7gqAIJ1-xZXYErXm4ujlC8ze2EvUjagWElh3SpDQp87mBXnlT3H7f-edIjB_6gUu8F7fL0wBamusquB9rEQv5pl9jmdWGbZzCgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1da03a51b1.mp4?token=lEXybn0OJ2IyKK0Wnf1m4hkZ36KAL4cZtwXnbdYisl2I0faH9iwF2xqj30rJTBCt4C2WsZ0kOy_jpVFa7xx4Fl1fh36jpkDzETIFwlUA9tk81VOzQ9n3KdBbeDSo5jx4XygxH6B0MXcWq_Vq9Ts3GU0Z86fTWNDJILFBwcPkGP5UjylXhfmZeh7D5a-3nGF1hIYJoETWtYrbW6z6jJhukCYZ7mEXMe1o5-acHMhyLksPaxqWc8S7gqAIJ1-xZXYErXm4ujlC8ze2EvUjagWElh3SpDQp87mBXnlT3H7f-edIjB_6gUu8F7fL0wBamusquB9rEQv5pl9jmdWGbZzCgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظاتی پیش، یک اردوگاه متعلق به گروه‌های تجزیه طلب کرد، در اربیل مورد حمله قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138810" target="_blank">📅 10:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138809">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
نخست وزیر و وزیر جنگ اسرائیل با صدور بیانیه مشترک گفتند که ارتش اسرائیل در حملات شب گذشته خود علیه جنوب لبنان از ۷۰۰ تن مواد منفجره استفاده کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138809" target="_blank">📅 10:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138808">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
پاکستان: مذاکرات میان تهران و واشنگتن ادامه دارد
🔴
سخنگوی وزارت امور خارجه پاکستان:
اسلام‌آباد نهایت تلاش خود را برای بازگرداندن ایران و آمریکا به اجرای تعهدات‌شان در یادداشت تفاهم پایان جنگ به کار می‌گیرد.
🔴
مذاکرات میان طرفین با وجود درگیری‌های اخیر ادامه دارد.
🔴
پاکستان از طرفین می‌خواهد که حداکثر خویشتنداری را به کار گیرند.
🔴
گفت‌وگو و دیپلماسی همچنان تنها مسیر ممکن در میان تنش‌ها و خصومت‌های جاری در غرب آسیا است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138808" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138807">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
مدودف: روسیه در مرحله‌ای مهم از پایان جنگ قرار دارد
🔴
مقام روس گفت: مناقشه اوکراین بدون تردید با پیروزی روسیه پایان خواهد یافت و اکنون مرحله کلیدی از پایان آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/138807" target="_blank">📅 09:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138806">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
واژگونی یک دستگاه خودرو سواری پژوپارس در مسیر دهلران به اندیمشک، به جان باختن چهار مسافر و آسیب‌دیدگی یک نفر دیگر انجامید
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/138806" target="_blank">📅 09:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138805">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBBCppgzG4B5pcKwRBHYay_Vjuy4z5Q0xdRnACn7Qqje0KUBJ8iSEmqnCFZ_cmCMCAnkY6P-QHBiRErHaqpKENRogwWy5D85WQHCHt4fAhdWQaBdM1YNIN5He9z_obOKEar2o64zqaMEE7z8L_b66fNsZCClARWOoLT_GO3S0x2Hxi1FzeDscUaUE168I_2FyqCHcZxVP4Nps-K7vhx0CxQY6oFAAzTmYyp6LnjVp3Xgj9Y1HPw7Wgj8HeVWFQo0mEaJPfi_uwNE6Zg3HwjxmDk5ONPcuHgHsZEJpATokMLjEg7l6AKdJxWk7TtLURtNPDM3s95uVgblTfnsZ2eg8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخستین رای‌گیری غیررسمی شورای امنیت سازمان ملل متحد درباره هفت نامزد دبیرکلی سازمان ملل برای جانشینی «آنتونیو گوترش» دبیر کل کنونی این نهاد بین المللی، روز پنجشنبه به وقت محلی در حالی برگزار شد که خانم «ربکا گرینسپن» معاون پیشین رئیس جمهوری کاستاریکا پیشتاز این رقابت بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138805" target="_blank">📅 09:46 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138804">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=BpSQU2LKpRVYweUk-M72zp-S8Q0WuuZ83D97NH029bw7sINTdSeU5ztwNf63Dx61yGpDbRsxz37W1UYnKo0wg9Vy3oh5Vlto7qTxUiamr7uA0HWboSnPvYEfHg44W3oI1qOIQFqB7uie7W-qRoqsxSsfNg9hDjXRNSLehsARDZXGwWPc5HtSunXcURCtAzIsBQTLYPK64Fw5cnwHCcVEGDi6YmoIL-JV9Ozd0zDfYs6r3rdfBJ8QJB2POkmaGT4sv7R6W7i7wyxT2bztzOjU_xWX-X6cg9wZaAzMQhqk1wSnTTmFKqEhMXHv5tlacl-CwtzjagXoRTIAHkelBkysXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b065ff04b.mp4?token=BpSQU2LKpRVYweUk-M72zp-S8Q0WuuZ83D97NH029bw7sINTdSeU5ztwNf63Dx61yGpDbRsxz37W1UYnKo0wg9Vy3oh5Vlto7qTxUiamr7uA0HWboSnPvYEfHg44W3oI1qOIQFqB7uie7W-qRoqsxSsfNg9hDjXRNSLehsARDZXGwWPc5HtSunXcURCtAzIsBQTLYPK64Fw5cnwHCcVEGDi6YmoIL-JV9Ozd0zDfYs6r3rdfBJ8QJB2POkmaGT4sv7R6W7i7wyxT2bztzOjU_xWX-X6cg9wZaAzMQhqk1wSnTTmFKqEhMXHv5tlacl-CwtzjagXoRTIAHkelBkysXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ارتش : پهپادهای نظامی، مراکز استراتژیک آمریکایی را در کویت مورد هدف قرار دادند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/138804" target="_blank">📅 09:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138803">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tfdunqbMjSWU722jLgGkDxypQS2xt6UE-VP2YOYoJWOO6rwclKwg93DfeDrISCBdxxywpAEXPrmYGIO565VKENoBy8BBTGLzCZcTN6QRMIKldm_f4ua3yd2S9RYxonMy1E8ws6d44jkjV8coQnNGkH8mcR_qwyfBD6xJJDroFKewXXJwNcjD05VdJKj3aK-0JdkwH8Wm2wDjiV7jUmd1ij6pYLPMr3zH5qGhclh_uVz0zqgmM_56o9fTvr643ZwJSGY3h-Ckp1j_R157uxFIshA2iFQ-ShshCsWZQvAs-PBlOoNiAHXFGST_GX4Ljab0YlQuqczXIgGFPG1Bt2mc4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ان‌بی‌سی: ترامپ از ایران «خشمگین» شده است، زیرا مقامات ارشد نمی‌توانند بر سر یک استراتژی مشخص، به توافق برسند
🔴
رئیس‌جمهور در جلسه اخیر خود با برخی از مقامات ارشد امنیت ملی خود به شدت برخورد کرده است.
🔴
او از عدم پیشرفت در زمینه پایان‌دادن به جنگ با ایران و همچنین اختلاف نظرهایی که در داخل دولت خود در مورد استراتژی وجود دارد، ناراضی است.
🔴
برخی از مقامات از ادامه عملیات نظامی حمایت می‌کنند، در حالی که برخی دیگر هشدار می‌دهند که حملات طولانی‌مدت می‌تواند ذخایر تسلیحاتی ایالات متحده را کاهش داده و اوضاع را وخیم‌تر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/138803" target="_blank">📅 09:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138802">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGG9-eaMnHRurzC-Rv8gyRuyc134xmhqzn42ujFnNq2Szk-9cCJU0yvLcy80DkikbjsAoY1ftwPRCCgde58-n5sHhpxMc5XydgZY0q_Od3LEQOdlaFlawm4hhkKuOSnEKfIhsTFGEC-J8Z_RUV8zIzC2ij4cxXNZ44EjAi1VFFlb01VvNil95_8il35mjTdmCXUe_26dQ2dklZVwULu1a9FhtLIWRZdyz9BO39q0SWq8eBmFQ3DbqLulHE-DCZVBOObT0Bb09W0YsMRTWpLcF35_TdxycbgFqnccchQm9luhtWUELV-RyoI0y57fAgGquYpvgHdhfmsP7lJd0eRuDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظاتی پیش، فرانکو بارسی، اسطوره فوتبال ایتالیا، در سن ۶۶ سالگی درگذشت
@AloSport</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/138802" target="_blank">📅 09:32 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138801">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
مقامات آمریکایی به وال استریت ژورنال:
«پنتاگون در واکنش به حملات ایران به پایگاه‌های ایالات متحده، حضور خود در کویت را کاهش داده است تا خطرات را به حداقل برساند.
🔴
پنتاگون پیش از شروع جنگ با ایران، در حال بررسی امکان کاهش نیروهای خود بود.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/138801" target="_blank">📅 09:28 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138800">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=fx3IMQ5zwxv9kSZQtcQPXGXQe5gSN_SPTK3uzL3qu__zLuHwRdA31vY-J2jJw_rFfIzhcY8wJMFCW_2py49904JdgvtdRzeu8pj2FQY78-GMOTGak5TjsRfogz9Lsfi_dZzBzlG9ktUMTph3Xr0hmxSFIfdu92q_CnOjHxs8H10JgNV0_eo0-TwejAcralRlBWXsQbP2ZMT0x6q47M8an5z9X_PtKG7H95JljQLMQQaIukcNhcPAUmH0tAyYTtEcZBMSP2OzmpXahf8_xoZMoKufhso7iAmaLh98EivwyyZJADjKm40p0cFRGBqoFSNguDup79sQGM2aa0ojtHGeKrAcXfiyX-HWzUFPQ0X7HWtiTktWPn0VCqxPg1CttuE53JlSTNDVbn5OqbpVwsG_mclOvxRGE_VGs0Aq3noDos_TfrZUBg2eZ6kMTkenjOSv8tfiZaKlCmOYGcHhE8PCaVgAerEA5qaviHe9Ko0u0S6pa1ZitZXQh6-6vPR_HfFFUZvjI1KXUqySUWTOTL7-in3LJNS4cBa6osAY_PwKbJv3NyIZ6qnk9d2LIS0Z_N3tYjPrMqKikWgFodNZ5LqrGbKgE4RGdXHpCeBVrlz2SiS5aX-ATUV6tPeY__xyD_769jcikD7_3FMOr_VpsQd57z2oirt7SFjOe-YGdzhZSik" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0085b8d38d.mp4?token=fx3IMQ5zwxv9kSZQtcQPXGXQe5gSN_SPTK3uzL3qu__zLuHwRdA31vY-J2jJw_rFfIzhcY8wJMFCW_2py49904JdgvtdRzeu8pj2FQY78-GMOTGak5TjsRfogz9Lsfi_dZzBzlG9ktUMTph3Xr0hmxSFIfdu92q_CnOjHxs8H10JgNV0_eo0-TwejAcralRlBWXsQbP2ZMT0x6q47M8an5z9X_PtKG7H95JljQLMQQaIukcNhcPAUmH0tAyYTtEcZBMSP2OzmpXahf8_xoZMoKufhso7iAmaLh98EivwyyZJADjKm40p0cFRGBqoFSNguDup79sQGM2aa0ojtHGeKrAcXfiyX-HWzUFPQ0X7HWtiTktWPn0VCqxPg1CttuE53JlSTNDVbn5OqbpVwsG_mclOvxRGE_VGs0Aq3noDos_TfrZUBg2eZ6kMTkenjOSv8tfiZaKlCmOYGcHhE8PCaVgAerEA5qaviHe9Ko0u0S6pa1ZitZXQh6-6vPR_HfFFUZvjI1KXUqySUWTOTL7-in3LJNS4cBa6osAY_PwKbJv3NyIZ6qnk9d2LIS0Z_N3tYjPrMqKikWgFodNZ5LqrGbKgE4RGdXHpCeBVrlz2SiS5aX-ATUV6tPeY__xyD_769jcikD7_3FMOr_VpsQd57z2oirt7SFjOe-YGdzhZSik" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روایت حمله به خوابگاه دانشجویی اهواز از زبان یکی از دانشجویان
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138800" target="_blank">📅 09:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138799">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عبور ۲۵ کشتی تجاری از باب‌المندب
🔴
بر اساس داده‌های شرکت ردیابی دریایی Kpler که خبرگزاری رویترز به آن استناد کرده است، روز پنج‌شنبه ۲۵ کشتی تجاری از تنگه باب‌المندب عبور کردند، در حالی که تردد در تنگه هرمز همچنان بسیار محدود بود و تنها دو نفتکش از آن عبور کردند.
🔴
از میان این ۲۵ کشتی:
۱۸ فروند وارد آبراه شدند.
۷ فروند از آن خارج شدند.
🔴
این کشتی‌ها شامل چندین نفتکش، از جمله: دو نفتکش بسیار بزرگ (VLCC)،
یک نفتکش سوئزمکس،
و پنج نفتکش آفرامکس بودند.
🔴
در همین حال، هیچ‌یک از دو کشتی عبوری از تنگه هرمز حامل محموله نبودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138799" target="_blank">📅 09:17 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138798">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
واشنگتن پست به نقل از یک مقام آمریکایی گزارش داد که واشنگتن از اسرائیل فقط می‌خواهد که با طرح ۲۰ ماده‌ای که قبلاً به‌طور اصولی با آن موافقت کرده بود، کنار بیاید. این مقام افزود که دولت آمریکا اطمینان دارد اسرائیل به این طرح پایبند خواهد بود و اشاره کرد که اگر چنین نکند، دونالد ترامپ، رئیس‌جمهور، «به‌شدت ناامید خواهد شد».
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/138798" target="_blank">📅 09:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138797">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک منبع اطلاعاتی آمریکایی به شبکه نیوزماکس گفت:ایران از داده‌های مربوط به فناوری تبلیغات برای ردیابی نیروهای آمریکایی و هدف قرار دادن آن‌ها استفاده کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/138797" target="_blank">📅 09:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=LnFPben8Aa2olmuEpLpp81fblO8bwa6oOU-muEVkA-GdfN0tZ3FLiPXcpcxARaM_wYzJdWBcekR991y32GSNVHzfxheDosdEDULHXnzh8zXPomnKsSwmd1jIRrr-G6ebFrXh2sULGjFKMdne-o9T33h4D5TmmMmebBZi6HGSxr89ll-U3Gl2EUfXwsd7dbJ_u88x5P2SgRTmW-VcpYRu-Bz_HbNbblPkccsrNoAQCEh-niA86XXkOIJeio9JPml05UQThsyZLZs6AY0jbID_nFYuRrBYsRNL-cZFJQoNuCeQdonwUGn3zZaqLlvsnrd8fKcYbMdCkLowHOVcXI665g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cb5776e72.mp4?token=LnFPben8Aa2olmuEpLpp81fblO8bwa6oOU-muEVkA-GdfN0tZ3FLiPXcpcxARaM_wYzJdWBcekR991y32GSNVHzfxheDosdEDULHXnzh8zXPomnKsSwmd1jIRrr-G6ebFrXh2sULGjFKMdne-o9T33h4D5TmmMmebBZi6HGSxr89ll-U3Gl2EUfXwsd7dbJ_u88x5P2SgRTmW-VcpYRu-Bz_HbNbblPkccsrNoAQCEh-niA86XXkOIJeio9JPml05UQThsyZLZs6AY0jbID_nFYuRrBYsRNL-cZFJQoNuCeQdonwUGn3zZaqLlvsnrd8fKcYbMdCkLowHOVcXI665g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ایران به کُردهای تجزیه طلب در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138795" target="_blank">📅 09:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
شمار قربانیان زلزله ژاپن به ۳۴ نفر رسید/ ۳۵۰۰ خانه هنوز برق ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/138794" target="_blank">📅 08:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138793">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
اکسیوس به نقل از مقامات اسرائیلی و آمریکایی: ونس و نتانیاهو عصر سه‌شنبه در یک دیدار دوجانبه در واشنگتن، گفت‌وگوی «مستقیمی» درباره اختلافات خود داشتند
🔴
تانیاهو با ونس درباره انتقادات اخیر او از دولت اسرائیل گفت‌وگو کرد
دو طرف توافق کردند که به دنبال فرصت‌هایی برای همکاری اسرائیل و ایالات متحده در حوزه‌های دارای منافع مشترک و اهداف مورد توافق باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138793" target="_blank">📅 08:52 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138792">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزارت جنگ آمریکا در به‌روزرسانی آمار تلفات اعلام کرد شمار نظامیان زخمی این کشور در جنگ با ایران به ۶۵۳ نفر رسیده است. بر اساس این گزارش، ۱۱ نظامی دیگر مجروح شده‌اند و تاکنون ۱۸ نظامی آمریکایی نیز در جریان درگیری‌ها کشته شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/138792" target="_blank">📅 08:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
ترامپ: مطمئن نیستم به اوکراین اجازه تولید موشک‌های پاتریوت را بدهم
🔴
این یک سلاح فوق‌العاده است و باید کمی درباره اینکه به چه کسانی مجوز تولید می‌دهیم، احتیاط کنیم
🔴
تمرکز اصلی من پایان دادن به جنگ روسیه و اوکراین است؛ کوشنر و ویتکاف، برای نخستین بار طی روز‌های آینده به اوکراین سفر خواهند کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/138791" target="_blank">📅 08:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fRZvayYlqP1925SmQkaffuNvDfgd_8RxkwuaUyELVbTY87gl4NkLX_PpHdgI2ia6-CxILiyojExN_bfZPC7_tEjh8zSsU-_4HshEXaV9faI84J9CTJ_O3H-e14QbAjKFY9d8b61mMlAxSCsVPBDC9Di7zgxadcBlo43TdfHFDo9TmcnO7WRv1auripiE7NfC__-L5o-efie3oXibKDQyzrvH6aZxZsKF_bw3_AoaYD7huQhrXMdzGhBJ1Gho2qlEvMULG6K12UQLfDezlRZKImjGtTMa1UDWMcqkYy87Ol-qUAgqJ-kKJUYD9hKRWHbIXFukQNibrkQG8SOjU8ZSxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت اینترنت استارلینک در عراق چقدر است؟
🔴
یک ماهه سرعت ۱۰۰ مگابیتی؛ حجم نامحدود: ۹ میلیون تومان.
🔴
یک ماهه سرعت ۴۰۰ مگابیتی؛ حجم نامحدود: ۱۵ میلیون تومان.
🔴
میانگین درآمد مردم عراق: ماهی ۱۰۰ میلیون تومان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/138790" target="_blank">📅 08:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-138789">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Mse2VKz75y4XGsywrxw1shE57QSPMXf-0cejmHig6FUZqLJPPTGNjvIs-tkFjzy5q-AyTdbNzykjWiE_mga7t_VrJhrtXJjUdUvo_RE58NzaN_y1E476VdbIqzjkWl-DrxrQkq2KO6Xsqke-OErh3WGyLhe6JqplyY3wyh0A-KNo2PQsm2wAOgmwokjkGciBCBFxH0oxh6YDOMNcHPtAxmRutgSWeogQmdVP7zP7LXdqRUGgE5FOB1t1ROppqRaLQvKIDr8Y4D-bJoQZYeJpxmF2VYERfcIm9rh_z5L90kCsEMWelLnLEQNdvoN5Zd3-OondyWkxRZolDX5rNEuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: حماس خلع سلاح شد
ترامپ:
امروز، شورای صلح به یک توافق تاریخی در مورد خلع سلاح کامل حماس و تمام گروه‌های مسلح دیگر در غزه دست یافت. این یک گام بزرگ به سوی صلح و امنیت پایدار است.
این توافق، یک گام حیاتی برای این است که دولت فلسطینی جدید، که با شورای صلح برای کمک به مردم فلسطین همکاری نزدیکی خواهد داشت، سرانجام بر غزه حکومت کند. در عین حال، اسرائیل امنیت مورد نیاز خود را به دست خواهد آورد، زیرا غزه دیگر به عنوان پایگاهی برای حملات تروریستی مورد استفاده قرار نخواهد گرفت.
این یک نقطه عطف مهم در اجرای طرح 20 ماده ترامپ است. این توافق به صورت مرحله‌ای و با ساختاری مشخص اجرا خواهد شد. با تکمیل فرآیند خلع سلاح، نیروهای اسرائیلی عقب‌نشینی خواهند کرد و نیروهای بین‌المللی حفظ صلح با پلیس فلسطینی جدید همکاری خواهند کرد تا امنیت غزه را برای ساکنان و همسایگان آن تضمین کنند.
یک سال پیش، جنگ وحشتناکی در جریان بود، بحران انسانی وجود داشت و افراد به عنوان گروگان در اسارت وحشیانه نگهداری می‌شدند. ما به پیشرفت تاریخی دست یافته‌ایم و هنوز کارهای زیادی باید انجام شود.
می‌خواهم از میانجی‌ها - مصر، قطر و ترکیه - به خاطر تلاش‌های مهمشان تشکر کنم، و به ویژه از تیم برجسته‌ام که تلاش‌های بی‌وقفه آنها، این پیشرفت تاریخی را ممکن ساخت.
تهدیدی که از غزه در 7 اکتبر ایجاد شد، دیگر فرصتی برای بازگشت نخواهد داشت.
در چارچوب این توافق، غزه سرانجام به دست دولت فلسطینی جدیدی خواهد افتاد که به مردم خود خدمت خواهد کرد.
به همه تبریک می‌گویم برای این دستاورد شگفت‌انگیز که، همانطور که همه می‌گفتند، هرگز قابل تحقق نبود
✅
@AloNews</div>
<div class="tg-footer">👁️ 97.8K · <a href="https://t.me/alonews/138789" target="_blank">📅 02:08 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
