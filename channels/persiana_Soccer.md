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
<img src="https://cdn4.telesco.pe/file/OZQE00_PfM34szbpFST-nn5Oy-xyWdh3B2bpb_YlQvdCxXe_j0Lc5p_xv77MRw9WMxtSSJNyBFYKGIQdY2l3BynHxE2CZ5tuSoc9hUFE_RqmxhUKrOeEYzJ-_9y9xFgv3WqwnKdzmeAU0sTl5--GSQvWC9VSGYrnEfeuLJ0hQyaK-G-akiUcsobqh32bKdOjFFpNNXlTE-Nkv17ek4kVU2uVHlWNDJY2GHbfbSG8gy5SPKU4qiDCeBgY_4CDSg-h6Hhit0aE92oB1mJMokA_-b3AfwbTngL_VArdjqrnkQ6bi6vBJ0FGYMKh7e5y7TqB1F9Q8DYhoq5qBbDbHUmBwA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 496K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
<hr>

<div class="tg-post" id="msg-29966">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX3xfYtVFI_VIdEOxjIJw8qsJgi5mzYq-5HrYLmjjLLRS6PcX8HWRT63XdQphlcyoCr5qL_OTj4YTZuQ_tf9KVvhjZcrFVkGQFNVnKxxK_ubA6UMQwJnHGvEOiDMI6uPwCcBr9DImkChgFY9QKbmyCtmOCxKhMEA4bVFg3bGBfe2s4bBS2SyV23eC1KLxTHfuv3bra9BzVW1xu-OScbzVkc7wuuY_lpjOc1VCxnEbrh-r2ugAsu-a1JwWzoX3Ep9pIAcJJo0-n4ihq_bcZBKtzmcEHu4x1JbjM5fbVUVy1aHBjJWavo2qN-8LEUV2l8V03ySMN3PDSDCobVgp5aOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/persiana_Soccer/29966" target="_blank">📅 22:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29965">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKmd0x3SvhpvfZU3XMArG8DLcRXaon2CeJ3RqmUkhbdr-yFsOdvtFpW8iZkZmth6haPrZM2DE5VJx4SUvn7zKEP5VlN17Nc7Wkaa3G6Zl60BewoWFfqiPnORNurGkGPCZDZST_aRJAs2pC6cKH5v7i0Zw_yrRe7b_y7MJ2irlBRxAYXZCStxahVniGpgQ3fS-haWacd7gYc9fc3s9gBaooHlSByg1A53OlSegiBP6S7l4N-yxW4K3JO56zA8sVepX2oqTgp0fpsp53Qt6B6C-UvkGVWUm97sdcMbCPwbeNFHZ4HaBDjacCt6ESySgw82PT27OyIVfb5KsCRPSsrAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تفکیک‌تعدادقهرمانی‌ستاره‌هایی‌که‌بیشترین تعداد جام رو در کل دوران حرفه‌ایشون بدست آورده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/29965" target="_blank">📅 21:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29964">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ojt9KO6jkgZXp1S-wlQCBPALBXr5ayh4Zjztbl-A0E6KJnY19ML3w96KQhbp5UZ4oq3h-ymdkeMSZPUgteLOQRHxYXJhBFNCQY2dk0vjt5he6y7b_2Y7BVK8YboCJ8Vu2krOZbHC_ujex10iVlc7bdECP31IdFmXwOMCDGRDsO7hv0TDmGIVoRY8rMC02lEXvRvwXWhehcGxL50lAS9SBC_fgli6DZ5har__NQTZMlOpx-rLuNv6rlMw2AzuGDK7Foamap7SG9p8pIBp-BFqceCEsqAGue24rrFFp-WDZ7eRyy9nJuExrjm3N3PZu-mjc8xcZGr37zOtV5IMD3w81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/persiana_Soccer/29964" target="_blank">📅 21:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29963">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_QerDCJn-JNhONgvGs4AS0Y3JaB9zsr62aTqNSwp3OEZJJKauB_05hZeqiOZqfWMJxUs3cT6ui1TCxmbpmPG7R79qO-nm_gXWKhIAvCR62dnsQa5kiG-KTDTd3CPRp3WKRVU5Rp0KUH2KY2twedJ89bXYe__fRExVaBNt-QXLIwuX92D8dw18SPCNTAVrgtXLIAgrq0DLrHG_--0nrSl22NFBgRgm72IypjHlcbbI2X_xq-O62AtyMe6iN0xCFeG711_-SskGGI2RSEoCnzw6ExIykIsMRNpPNuMMiX1huonJDV8-4a6waIhGiVV268wCYxDMWUCzKEJEOYpfajyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
علیرضا بیرانوند دروازه‌بان ملی‌پوش تراکتور قبل از اعزام به خدمت از تیم تراکتور آفر تمدید قرار داد سه ساله‌دریافتی‌کرده. درصورتیکه بیرو به‌این آفر پاسخ منفی بدهد بعداز خدمت بازیکن آزاد به حساب خواهد آمد و به هر تیمی که بخواهد میتواند برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/persiana_Soccer/29963" target="_blank">📅 21:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29962">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbMknA5fmDlBuIWZYfbN1S-nDR2ijNZEVv_Qc0G4nKbjdeulIUilWx7g225bxKl5EMZb2KB_NYY8rcUOv3-1PJGu7ofv49q2LW4AIE1hgSIcoYGCMtz5obRtxxGnJLtNUFM2ys1Y3PO8LpIgrv1AFleD9qhTpBqqL3DYu2sdKwUPBc5QwiGDlaB4KfTc_2Rwy6fk8Hdj7RggeRNWH4jkHumy5QI3DQyMGEV2a5ydbs7Ayu12zS0UTc83y0DczTwG8PAlu29AhPVsOMqPdVYRja07E9MUyECHsszlRDgOuNJ-9ILyOc_nXC7dh4PGVkOqIIdbtsl68kLFezkg57Alfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛ ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/persiana_Soccer/29962" target="_blank">📅 20:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29961">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2ioLJxJkeYuCdbAMwV23D0qG-SaOHdn3dhAzehkRdPqxYmsjWGCn91K8Mhz-bFSRrSaFWVv24nQay2goO_Jn6toFoxcEXWcCBy7gocv4krK8meGdqLkBVUd9GgmFAUHjPd8Gd33L9bbg7s1eA48jRKdN2Y8DZyk_KmBAnV4wdtTyvQLUC0jlIbI23jIJ2oljzSLFdTUHZZfpv0BlGdWHtrhOJh8h1SuvJmBkHGmsM_MQ85dXgcx5cG-JUFNNEBEkShEXy9PyMQ8mHM1bfEVRljYdrmVseCNeShJNebhmzYzc59hpasT-mLHqZC6E2TjpfforY6qqX60vVUUhTNjYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگهداری درست از کنسول بازی، عمرش رو بیشتر می‌کنه! اگه داری این‌نکات رو رعایت کن و قدرش رو بدون. الان‌شده‌حدود 300 تومن. دوهفته‌دیگه 400.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/29961" target="_blank">📅 20:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29960">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KE8pGjYjoRoyxRF5dwouWCHZodhHU2rzXXp9DFWzWyOVLLMxCtIukKjKwWBjYcKbgHf7hIKJtVxrSsLHFpLsbSHCU6PcJFusghswtWBMwTf0VY6LrdjV65IfVsILlFigXYkAecUJbnoMweYYuVaAEKmXpyMoiSCY6xwX5C-MG-O4PlUbLCU3aq6E76f1fAPSBu8P9S5zvZLTH9JTYYCR-v5nk7ZTMRLCrXHUWeD998PeB4bmpBSIfUpYcZiUMGQBUttCQS6tLgQyZrvHMF4oE3b4pd77NdfkiPsD2xJeRP8QWnNXRrBx3Fsw8vtYGbNQCe0ync34gkQwrTLnoAyR8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/29960" target="_blank">📅 20:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29959">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef9E8x8eO3sMToBkoANjo-aROECWV6C2XqDWUnHfdF3b2WvtHjUnbEekoZIq4BpbBLcGXbFm0WoAgH-8gbmUrbCf2D3o3oDC1hPvh-1iAoiVvWvZSirU01lAwEFP_WnsiAiRqk2HMVexKHblms7JtqmHoZvYdxzcHAH0IhL3ltpZNvdnQFK1HAIbWklB7kmYKBEG6SV1ukH14XUwRz-siEhy0kY7K2Gh2Fy9MLd-60nnGwqwk0F-rr290hKgvKvEpczVi1iBt5NEgRnspOz1M-sReVJxb2fUN2cAkgyOPiSu1ktRISLBRWcvRQ3fZFR9tf69BGXwSx-BgOwEY5Qazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بازیکنان رکوردار بیشترین تعداد جام در کل دوران‌حرفه‌ایشون؛ لیونل مسی با 49 جام بااختلاف پر افتخار ترین بازیکنان تاریخ مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/29959" target="_blank">📅 19:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29958">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAemwGuvWj_CXVzEEWBrVqRHshD8vHgniOQ3Ohf8l8YgLYUJZgGE7uuv-zgOrSMxb0CSPoPVvSgxlSMNTQAY4_MrMVKENLL5w6GsLDo-O5bETK-Z68yjP91T_3bNuN3rnGgfoyT5ran6EHd7fZAHSWa9XB2ySaWyFjdI9kG0oqCuXJZkE7ySDXK1jtfmyATBa_pW4OXs93AofBM58cUipT5mgYVC1ibim2CZQKRAC1CvB-wCplb_LWa3oDRb3NljSPVUEFqISk5RKy-sXr5TVd1IWGUH_uAJTBcn3bFQTpI_ohkfPE9soNsUCqXsMbmCknq-ZCK92ObzmJcqqygEnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/29958" target="_blank">📅 19:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29957">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMVY2ds2o6kh87PoV1OFCer8eyx8onQaAnpFYsBT5sYOFnXsGkwwN879q9cangozSh_0d2oPIlFGpIELxLboUcagbjz5LDiRGMYHCYXQCGh-SMGTUouEJnmRFr8aPbUAY_hd5C7a-MF0ePXSNx4pGj5-9q-NrASdgZiSAf263YlHPHaLZqhBRjtjx5ySF8Gn3Lk-WuWWoBwR4r5SPBlengeJI_p6Wa3V4xR1-Bx3ThI7ll_Y4uFYb8yPNolucVhi2iNv_UVr-VhPCylLOnhC0SSHSdqEMGqTmhkMpn-Qk0oLbV5DWYoQlfvjGxf9qcEYuwR-h1ynkvW3rkTa1rnQ2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ باشگاه پرسپولیس میخواد درپایان جام ملت‌های آسیا برانکو ایوانکوویچ‌سرمربی‌سابق سرخپوشان روبعنوان مدیر فنی این باشگاه به جمع سرخ پوشان برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/29957" target="_blank">📅 19:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29956">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4vfa0Fk2gjRD464R_eZI4Fc6MUp8wBN4iHqmTK7LDZ6560ikkmmQSXDFgz3Hd3Gcl5YVkxPlmaT7F3aX0a73tNyIwa8wdCs22eJKvl1y0czDgVL6Hg-V2QKQCZyT5Ly7mbRsnU_CKn7tOf3R_bEOlNcOCxfvPtD1iASaWZr_mbd-ry9rLFaopQJvINgrTYJx2aHb4usjKMYdWqKUZWi9KITkhgjUa_k_Z89399DlHyWbUokCLKj2rXxg2rpVWrHTuhdp5XjjsW-2KuUmI-Fe7c86E0Wc6ovl4AZ_jMqPjjMuN1vqxjtFNIaOE6ANFDNUpksUH1wCBJ_ACAkjQVeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرد پرافتخار کروات روی نیمکت امارات؛ زلاتکو دالیچ سرمربی‌سابق تیم ملی کرواسی با قراردادی سه ساله هدایت تیم ملی امارات را بر عهده گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/29956" target="_blank">📅 18:51 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29955">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M51WCf6yGIu-qvS_sdXCZEzLv-etimQTrcW-kmpVKf00j093XC-zRqLZAqnvGXFyoyxfnfPCaazuO5ntIF6mYcC-hTD9JE3ZciaDJoHw2kXNrd2Nnp6wH-MJOOHvgHqtX3BC1xQxkc3oW6UVvqbEWdhhq6cVRJxe9pomgaMoAP4rjQ0f81aDhHJUi-8DuZDzLjfIH6KIn4WHAXU2sYq_9C2Hw8Q9iHUB_GYiCpT0VkYRtFGdf1ADyRXIHRHNoOPaENgrXVgix-cpNZmgEmuUrlu47M84jOnReSR4_TXSNEg9OPa6z3enbTWLv5jSUpVYAQ2Piri80wSUs3oMJn1_Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ارزش باشگاه‌های لیگ برتر ایران براساس آخرین اپدیت سایت ترانسفر مارکت؛ پرسپولیس ارزشمند ترین تیم این فصل لیگ برتر ایران لقب گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/persiana_Soccer/29955" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29954">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=l4LQvCHEPi-UtytybufBTczHEQfgm6XXmgfzImSulX3e-tBBQ8kuVh07O4T3PBgl3kA_vrRir07QNfYx-S6l5oknHFQDtQFWJoT1xYpXmGDq93CRpZgQOdGYVMLiIFvF2L8LYkb9mco6W2gp6-4CORxjMSjpaUFjhN4oTAjOXzHswPQVT361t3dftEuWUyCWSQdOUw195EhYdNJ6dp_EvDnYDTXfl9WX6-JAmXvKQtfS9vzueIs20IFUwbeL6pGmP7r3M_vxr10BVkaKKR3WSM2BuQ0LU5p4sba7_72H-9rAM3U_3JhEtRUkSOuB7Th1xuUacxfp7v7augWWDwSOCDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7c4dede4f.mp4?token=l4LQvCHEPi-UtytybufBTczHEQfgm6XXmgfzImSulX3e-tBBQ8kuVh07O4T3PBgl3kA_vrRir07QNfYx-S6l5oknHFQDtQFWJoT1xYpXmGDq93CRpZgQOdGYVMLiIFvF2L8LYkb9mco6W2gp6-4CORxjMSjpaUFjhN4oTAjOXzHswPQVT361t3dftEuWUyCWSQdOUw195EhYdNJ6dp_EvDnYDTXfl9WX6-JAmXvKQtfS9vzueIs20IFUwbeL6pGmP7r3M_vxr10BVkaKKR3WSM2BuQ0LU5p4sba7_72H-9rAM3U_3JhEtRUkSOuB7Th1xuUacxfp7v7augWWDwSOCDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری عجیب‌وغریب علی فروتن از سکانسی که باعث توقیف کامل برنامه فیتیله‌‌ای‌ ها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/29954" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29953">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTxtxuZHLtjACiDXqOuHZoicg8mIUaOzRc66oOsjoNAfeIYbJBBrIwfy1sdFFpEoSjzYKKV09bNQiNJl7qJrEK0VXsh_8pLz8yQrQTtlD9GPAlHQZrtZzJ1Gh14GDge_BeQ7weGH3KwbD4uUxdBpGjIBn8vZa-9Du7ht-9XNYuTW1cmvXpuzJYWYK-ajbUE2Kv0XSs_tbcXtKCU3d-4N3043Znft-eoFyvQBfGFaor4ONaXzW_AaXY1_yq3BZ7EhmZ1Aw-hNz5DsA3FTdX8Xro0lcqvHlcCaG19YpFWaenCeeut08rYXJeQthvu4CtyfMa0wqLduutNLBURmtaJ6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
❗️
❗️
❗️
💥
چالش بزرگ پیش بینی
🤩
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🌟
از
🤩
🤩
تا
🤩
🤩
🤩
میلیون ریال جایزه برای پیش بینی های درست
📌
فقط کافیه در طول هفته 500هزارتومن واریزی داشته باشین وقبل از شروع مسابقات به
🤩
🤩
سوال پاسخ بدی با حداقل
🤩
پیش بینی درست شانس برنده شدن داری
🙂
🔜
نتایج برندگان حداکثر تا 48ساعت بعد از پایان مسابقات اعلام میشود.
👀
آماده ای شانس خودتو امتخان کنی
❓
🌐
لینک ورود به پین توتو
🤩
🔗
https://pintoto.xyz
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g25
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/29953" target="_blank">📅 18:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29952">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fItsuduR5kNv2AG_4MK-o62XLyRabhk0HIpkIJV7vzY1393KEBlHBq3RYSSarhqC22UufBCbD1nluWcDKcorxG8X1SvHDik7DWLGCFNZhFopKYJyN0uT9B_zNDdQ437OvOEE8yhVG4iXc3zKXk1e_yIcWcNG7dWMeVnnhtuqRDDyb841Wt_VmvRB7EHjzvtTq5IQdYhvAjk7hw5aVvXWnTFt_nNqTN76PiZUFXz1_WPjE6XKqSwk2NZ-0fZ5oLl1WihOxVm4l9oKBuD2Iu3Cc_vVAWTxjoZie_RMmbwuqG6PmPlFRCc8aAYy4Z1mTS44Rog_Y77Ps6to-v2OWFIQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/29952" target="_blank">📅 18:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29951">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8_l9xF2APDNEfU5S8AnTboGA8tqPyZsWxxX5UW9vCXb36oJpZ2sjbQStsNZFof7PdfI5bhKUBHKbKh5FnJmaPXdBtx-qQCIrfgEaXIP6jR44lLW4ImvIh_uwdyG4yiA04Fw1uoYNfbqCVviQrC39sIdzzZ5dY6gO_ubcJxm-zesscG0_ApmB2ic-RRo0c6VJ0hhrqv-Br1X7i74x5_yjj6YRrRMR6essX45UkxRJTNmZ6ONjFOkzLbUFeKTGb36Uwy8rXUkMSVUSQQZWOgmsO6yDcxHFbmYNKUU3oWi27ybqcytmY49zUlU2rrizHMG_vZKy-wbdvfVgf2uR3okAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌سوپرجام اسپانیا
؛ بارسلونا و اتلتیکو روز 13 بهمن‌ساعت 23:30 به مصاف هم میرند. روز بعد همون ساعت رئال باسوسیداد بازی میکنه. برنده این دوبازی مسابقه فینال سوپرکاپ رو برگزار میکنن که روز 17 بهمن ماه ساعت 23:30 برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/29951" target="_blank">📅 18:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29950">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZM6h7Cjsdmn1Q0mGSRn0v1auGUfEzA0TSRxuAjBQ-davnbruCpqVwAb879rmO0TZ8Dk6YEXbXuO0cw49EhmTmv_9F9vcVeKR8x7PlY_mE0WXjvRN83YWHQlHrsDgOq4jcX8fD4lpXnqUlqmqdi89_Bszlrb8lr9_HCA5oQzha7cmQqtdvHDvIDdEwAMwVa1vcUVyUu8IsWR_S0hDV6-GywGv3htPwVLF5jg1UdS9ncl9ROhSYZxo7IUooS0watWfGf-1Rts5xc1L-5rkOSJIEyFEOY2fw7uo-36RtAaPYIiP76pszdlveSjV-jZe0dfmPdF4MtqgKJbFCZDtZqHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌پیگیری‌های‌خودراانجام داده و در تلاشه تا علیرضاجهانبخش رو نیم فصل به این تیم ببره. جهانبخش از اول دی ماه سرباز خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/29950" target="_blank">📅 17:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29949">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UfN7zp2TstFfYhN2B_qZlaT1r2mPOaRQxV7tC_xPXrpgQ1WHWrvBW6yM5kfZr6D4FHgV-UuqdN3U_eYBQv-GZZlCI5QUeLWqBBS3c_ppAgxDZ5PNZ89TYcLMM3qk-TWolDcuEiL3obq5qdUlX27WpZ0kOaMPquuYHcFeOjGt6RezwZk4k4x9ETZWPSC09tQHGzPfQmdtaNHByUdPokmqZV0oz7aom3rFHpmXY30hYtKkHZLebuAnxcbrNyhZVi01FcUBs071rbnhZo9lpur-ZnhEIZnW9eGfYw_hofvZ3SC5-TPv3EbEXgWCUUNU73_B5YE-9p2oYp3sR2OPjPV-hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/29949" target="_blank">📅 17:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29948">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjQH2w6UqlvXWXAaQbrg0zSYS9mb8D47du1FaTGaJnlgxwT7IirPON_r4t_wgLeLC6q26m_GUlxBrU0076Yvz_QVId0R5bUMzzanTcogCVCr1L9oWvPF0Fd4_btLaLQxvfKrnplEwBjDqDeRP1MG_J_MXV8CaG4ykb_AVQU8yI8GVBQPYADZhIV4ZGWg2ncL566W9a6DZLNk3aCdMDbhaEVlQABjPrx2zjRcZ8nwYY4YmN0p2hJlt1QCPGDpEm3m3aoFTc-diTyydfWrQ5KuZ6j775WV1C1Y6HQA9vmDSSYj73XA77lQuNrqXmDhrEtCqy7zv-eVX2KzvXPBYWtDUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام کادرپزشکی باشگاه استقلال؛ حبیب فرعباسی دروازه بان مصدوم آبی‌ ها به دیدار شانزده مهر با تراکتور در هفته هشتم لیگ برتر خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29948" target="_blank">📅 16:41 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29947">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moC9FlXrP6C7oasnBWxInr_zG30hLqB9Ji1_9xm2JC1avbuw-c9-r9V4k2m8o9DDNQ13-uwABxztNqqIjAs6n3LkiVeMytZSxSaPZNnPMGvaZYbnJAuRh_Eb5rUr7ilaEEjGAYbvSr4ZpmUsMTgGQERcOPj9ae-Vbb9Ym7dB2LnfcqV0c_54hMKN8hhuLsNEKNLlovKq3UiK8TVfh3Tk1XLuX8vZEYRElKAXdTpkHyYneKjxYJzC76ClfQT-K5lw0dwoOyX8AvTF5MrnW6t1r3s3IcgFOrO9rEbEPNNY3tRo4ccWr_NA1UU8jltpNsZW6MolxPEkxa0gYamy4L14DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/29947" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29946">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=B_kevBLot8SdC0c_iDyIutFB6W7G14bvTswa7RhdOgNMPcSDCMJ_0YJvxfqpucK2F32zVjZxplb5ITIjUfUaoyfvRtGRrpGebus7cEI-ISfABzDbiThWDZdsGrvH9UJKM4Oz48A9Pp93TvIPKt8C6wn6hG2hGZiLD1iyetXldqJc4XfJXRpyfyTRh8Nw_cz-Y3jio1erVptsec8YWh6Rk6ylGay9CaKN0yPuYL-Hjtom4sDg0Z96wGj9cBGUWZf6qdXQ0a6pbXIvsbImVUfeRJJULgnjg9g4R9Ip8B-d2OQ-GYIb3aDm3eIiK4HUKq1k7UJr4lFBPBKru_n2sxIinqHPx2W8qPzZQrcLHhDnjjh48js6cWqboLf_NuHq7vL32llZGRWezwLRvwoExxf4NAvinJHpei1Z1rZENmpwO0wIODx4GFGRo6geEhP7a2R9YINl9sPwMuGsp4fPBPRdkvmNEZAkQyq6YLMqjZ8zFy1VQm-CPRVlhTyJutvuIAUxslE5-q7LX1yi1JbEsoZW93E8pcyLgMDSqFbSa0OxMKoPm4iME4g5HRMMnTVWD3S59baRA9__zqq3H4VK8puIVM1P5rOvZu1VFw2iRLFUKVlJDUAMK9CbnbJlRRRt_lHsDRj_orAlJMQ_PU2MgN2GkpDJRfRek-4i5mu49uZ-H2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e07abed.mp4?token=B_kevBLot8SdC0c_iDyIutFB6W7G14bvTswa7RhdOgNMPcSDCMJ_0YJvxfqpucK2F32zVjZxplb5ITIjUfUaoyfvRtGRrpGebus7cEI-ISfABzDbiThWDZdsGrvH9UJKM4Oz48A9Pp93TvIPKt8C6wn6hG2hGZiLD1iyetXldqJc4XfJXRpyfyTRh8Nw_cz-Y3jio1erVptsec8YWh6Rk6ylGay9CaKN0yPuYL-Hjtom4sDg0Z96wGj9cBGUWZf6qdXQ0a6pbXIvsbImVUfeRJJULgnjg9g4R9Ip8B-d2OQ-GYIb3aDm3eIiK4HUKq1k7UJr4lFBPBKru_n2sxIinqHPx2W8qPzZQrcLHhDnjjh48js6cWqboLf_NuHq7vL32llZGRWezwLRvwoExxf4NAvinJHpei1Z1rZENmpwO0wIODx4GFGRo6geEhP7a2R9YINl9sPwMuGsp4fPBPRdkvmNEZAkQyq6YLMqjZ8zFy1VQm-CPRVlhTyJutvuIAUxslE5-q7LX1yi1JbEsoZW93E8pcyLgMDSqFbSa0OxMKoPm4iME4g5HRMMnTVWD3S59baRA9__zqq3H4VK8puIVM1P5rOvZu1VFw2iRLFUKVlJDUAMK9CbnbJlRRRt_lHsDRj_orAlJMQ_PU2MgN2GkpDJRfRek-4i5mu49uZ-H2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🔴
#تقویم؛ 8 سال پیش در چنین روزی؛ شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی…</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/29946" target="_blank">📅 16:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29945">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ABSjwSZKJAjkQsi1JLObxcz5DNtrodKS4LLp09DWbrZatyohwtaqh3DTqjmlDo3rg-BRGcQ7-1VJ_mqMymf3ZMHmtrZfVxg0jPh8jlJe-A-EaiyoP9O0rs6pnuyguTPo2t38KoZPs2vyrR-yw6Tu67SPb263DuBDKWcN8nJouEebguJAgfkyzIXtkCiCzzpjHdYFB8fQ3_dnSVRFq6_IMgfDj2iSvD7OgdQrLVcPWi9ZergFyYgyvOkaV_w9RzeCo2ibaSPVsClHo-Dw5BkQeGxyZBYgUXL_YcO9ZBEez0ljl9dtuQXGMKwe-CrWqRdTNjQl6nXGaThXehbv5r3NVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🔴
#تقویم
؛
8 سال پیش در چنین روزی؛
شبی که پرسپولیس، الدحیل را در آزادی شکست داد. 26 شهریور 1397، پرسپولیس‌پس‌از باخت 1-0 در بازی رفت و شکست 1-0 در نیمه اول جدال برگشت، در نیمه دوم سه بار دروازه الدحیل را گشود. سرخ‌ها در مجموع 3-2 پیروزشدند و جشن‌صعود به نیمه‌نهایی لیگ قهرمانان را در آزادی پر از تماشاگر برپا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29945" target="_blank">📅 15:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29944">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=pTDAYzCNb29I6aDfEyg5IgX9KhxoqpqS2Y4_nKLvQyh93Mb80SVQGrJpmq3_AgAXMsDqIifKRc5LUREz0sj39uvu58F4uIyFsP4HVmN3gmGqjLXZViLtSByCGmT1GliUdmxdEZ5qvrXD1VZSa9POGhvgCLoNWYUWUjyhEgSVyw_KRY4N6ne-FFLpWykc2sacf1-cgCwVld4v0kHGNeAoASBIqkSFGiu9Dh1f5FMBmxDVj_geMwhTb4AHuebTI1FxciiCNx1KZVgG30IYwkFjxn4eiDe_odlXMEX74hobOGOV4wkcEFDLnsGuiC2uruqVdDbkGEbHjh-Vrs4YXYahJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27095c80f9.mp4?token=pTDAYzCNb29I6aDfEyg5IgX9KhxoqpqS2Y4_nKLvQyh93Mb80SVQGrJpmq3_AgAXMsDqIifKRc5LUREz0sj39uvu58F4uIyFsP4HVmN3gmGqjLXZViLtSByCGmT1GliUdmxdEZ5qvrXD1VZSa9POGhvgCLoNWYUWUjyhEgSVyw_KRY4N6ne-FFLpWykc2sacf1-cgCwVld4v0kHGNeAoASBIqkSFGiu9Dh1f5FMBmxDVj_geMwhTb4AHuebTI1FxciiCNx1KZVgG30IYwkFjxn4eiDe_odlXMEX74hobOGOV4wkcEFDLnsGuiC2uruqVdDbkGEbHjh-Vrs4YXYahJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی‌ خاطره‌‌انگیز و نوستالژی از سوپرگل‌های تماشایی و برگ‌ریزون کریس رونالدو در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/29944" target="_blank">📅 15:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29943">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRz8RR-Kv_17rbbpYAXVPNQBqXD15-q8BD8GYM4iiiPrjRDW_1wnH-w8RZRKkvy1GswZk_l5QHOflplCfyeZC186CwjE0x4eQIgsus5vRjTi0k4vPx6JEqlgwlgnS5sRfeG05eBGnqu5xpyluYZcoDB56i8IS31U8J6Hx2DoLpnsEWOeHmse-D1hc3lWNZpnahMLNv2R58YrCWoY9SSj0qT3re45BbZhHbvmaJnKotKDjH8NiF_nEunTmfqzCTZel7wjHev8Pvi5RUGvKhfnjD1tm3lDlc58JneePxGvRg9F0v10unX80X8JocXJg66w9LmvdavYMaPuQ9vzb0C25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان‌لیگ‌امروز رسما کارت بازی علی رضا بیرانوند رو برای باشگاه‌ تراکتور باطل کرد و این بازیکن از اول مهر ماه با عقد قرار دادی هیجده ماهه تاپایان‌خدمت‌سربازی به فجر سپاسی خواهد پیوست و درنیم‌فصل به جمع شاگردان خطیبی اضافه خواهد شد. چون پنجره بسته‌ست…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/29943" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29942">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtesPsw7wncsIl5ZXFQuQGy9XwrbxIgOyxybxFMMPukdVsscm35hLwM-BxP0BNhHxBuuJDkV8_5fMgD4L_CevY8uEmUU3f1NeVhdqgyJ8K5iefg3M2b-QSEIdsuX7ygAFP-gsblZBCvQ5Y5KbgD3N40q1cTE3791SRTOW1R7OrEw4pQJuuH8LBuUWprLMlbJNHjGmoCQHjhzCnNh7b5tj-OTUaNGTkFsFhC8-_tRmJdn-CHcwRkfYvnujRzUI9cYSXR-kXRWLOSTjY1JCXogADmsq63_azPX-7FNe-xhGjL453alJv7OhjB8QyA-TqNOYMahfWgagSn8Ggm72KUP1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
از 368 بازیکنی که در یورو 2004 بازی کرده اند 367 نفر بازنشست‌شده‌اند و تنها بازیکنی که هنوز هم پرقدرت ادامه میدهد، کریستیانو رونالدو است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29942" target="_blank">📅 14:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29941">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anA7SZgU6UGk3szxPbgaxJ0rZ8Y_FDmn7IcM-PkIIKFkV-HZCH36vp2jHYBMwikxiCoFNlkL3NMXS7J61KpbBL39Khg10IfOyV_-zUlF55d3jFyJV8y8X5z8kHf3dtLod_ugM6HzLgJSM2dfC5IIt9bgo4ckk2J-w4Pt8bz1s5Bo95SCAKac3O5khLAzFe2UsJ0MF67tHURyR47NITWQLdlgzfXlzLyR6cnmGY7mss9bC8da9ugFbLgliDaEDL9A3eOa_YBA0rGgWSwfoYZJcC1d0v8ivXF9GFShvsrrevWNJ3d2Wr_MK7tccRx0doyPXbhaYlfCPWZQo-IBoyPidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
باشگاه‌پرسپولیس‌بزودی هزینه حق دادرسی که حدود 150 هزار دلاره به CAS پرداخت میکنه و پرونده یاسر آسانی رو به دادگاه عالی ورزش میبره!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29941" target="_blank">📅 13:52 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29940">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUxexSxL6K_DZB_IbhIQESJKoaobQJzOprAHJuhgzgQr00tPwEfzhqWHxZ36DiugcnJ6Ag153KJaqrphMNz-C9iheUSkfUnQwRtLMfzk0xkwf-n5wNJ-OZIUeh8isd2Js_GCfkcnr-5IvJp9trjhHT4IQPTQ4qrHgJfGjeXh7K2fxAF0Gp9ma4LOnStWfvwdGGeSla2ZXGQKIDCtW-XCrmy3TtbiGwIhWpFe1_Q-QZEQQcgFRJA8EVzqo_LZT3nahG7K1jzzp4q40VjalxzODPQ8lBq9m_g1iP2uhUYvAG4j7cHlyZfo56knaOK2yDjT-qSswLEfrW_DZxWqQNrZSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29940" target="_blank">📅 13:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29939">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab4eVEUGklVeCmLa0ajGfVxMNpnYuQQGpbyI6fHmclUVOBvCXh6VNH3OApwohL9V35pnqDwoFEnax-GzTPuBe2IVIVTh8xVJruQSZyMW_od8KIU4xdyZ6KofmxV5LKSiqWxNWAWItXDjpiUsRT_CPF0nGg7Hfe62a_8HywTEddK2-CuoMIrApNhl7sAmhpkyKS-J6XXx3pqruy_-sYbqD_dyECHiWpn4Vpiuj7ObcgqpFAIn7EEO0LG5MYO2Yv60V1AmUYY43QQwxq0UpB9mlzBU8lss5eXzIdUl2NW9CeAIDuL3zrdoJeoXp8WIshDGIvUbOOSu2PLWkYGivPsByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29939" target="_blank">📅 13:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29938">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lzw-UJTiqM23CxT6bZ-eZGdbHTVbeNwK96NPomA8Nlu0EAiPJyHtP24Kk9z71D_F_blesLq5ZtZX5X0tMQGMrTMEyT9TZGhIVZ25v4okJRdZG-jO_tjOcu6nMl7XrhJPtBNIRbOG8XssYOe9ZX9jxubHZ4500H25N03zSGBh625NmINKxRmC5zgivTJ7wTUMrLloRFs08sHphU6LSnN0DGOW-qUaMuZyLhgurRUQf38MSRW9BmxefBW9J2QPPzKjmzVtUGqrpoH_q1-3VocXl2J-Mg0u2GCYRKyP1YTcXRHFtKQzZC2Oo-OdqYvb3d28DPIy8hsJ2FIqSpj2l8lY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29938" target="_blank">📅 13:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29937">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTSxklE7fdWCLAQhor72WUJbTXFpCerDZ9GpFKa5aaG3SX9_Sfo0tKIynn_hQep6b4FkStCD2L1oe-XjKJvDsNeKa4Tnp1og7XwDdJ_z4niJ9aMSajGJyMU-kHTuqeoM2IJgwiXryfGWm6gmSebp4azj4XD9Mm4HpJuMKK1D7XRFxfqS27enUiKelfAJP3UmHZlWUNh2DEi2YgxmEua6MvB3OkwsI_qHcDJCrF_jho5rTkyzIUb7ZB1G5x9BI9lY09kc8psEDMIrL08WhYT9X9zLVmqJZ3kGeDHDHnuNld_qRpFdq4lMchIUJ5o7wKRF9R8hdaQbABG0CIHnYhEvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ کمیته انضباطی سازمان لیگ خطاب به مدیران‌باشگاه‌پرسپولیس: قرارداد یاسر آسانی با باشگاه استقلال قانونی ثبت شده. شکایت خود را به دادگاه عالی ورزش ببرید و در آنجا پیگیری کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29937" target="_blank">📅 12:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29936">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=s44SDMYD9kHx1qBGNXNpKNldB5sBmbyZVA4Mv0k2tLpI6xcPRCnp1nY78hoFU7_yxreiyt1tIPBgeyALGaaBt_l0AU0aZtx4_EkZY6wowBZIemhYwSuQzUyyj8mpsePvilJUMilWz3Fg4CnYL2S8C02k6mpIh22cW_O2GtXuiezkJfVAoKZ-BRZZXxpVeAn94e94UhxFmf9gYKATGQJ6-c8vCxRi0ivnQ-wi6HsqXGnjj-GEqLn4cDOdjnugNWuQ5ZqLQnDUFu9W0uYIWN6USELor8HcbsY0ZMtOncyxRKfIbEnxutTHjL2Tm_NEXxR0JVcBVKYCsLeIj62ftBOupoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0fc3a9a3a.mp4?token=s44SDMYD9kHx1qBGNXNpKNldB5sBmbyZVA4Mv0k2tLpI6xcPRCnp1nY78hoFU7_yxreiyt1tIPBgeyALGaaBt_l0AU0aZtx4_EkZY6wowBZIemhYwSuQzUyyj8mpsePvilJUMilWz3Fg4CnYL2S8C02k6mpIh22cW_O2GtXuiezkJfVAoKZ-BRZZXxpVeAn94e94UhxFmf9gYKATGQJ6-c8vCxRi0ivnQ-wi6HsqXGnjj-GEqLn4cDOdjnugNWuQ5ZqLQnDUFu9W0uYIWN6USELor8HcbsY0ZMtOncyxRKfIbEnxutTHjL2Tm_NEXxR0JVcBVKYCsLeIj62ftBOupoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
صحبت‌های دیوید بکهام مالک باشگاه اینتر میامی درباره لیونل مسی بعد از قهرمانی دیشب: ما هنوز باورمون نمیشه که لیونل مسی رو داریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29936" target="_blank">📅 12:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29935">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJ57LXQAeRCn02co1i4Udvp3hWStqvJUcxdovPiNaHJULsV8HQyrUrHY2GT-13A508UiwXvqImPf90IFZnmNoEg-DxfVJL_1y7UTEe43-HQCvTJgQC382lk5-vjMJO_cYYmmOlDWxdzO81NYeEDOWgFn22XQ0ZVp2Vum32_8DGjEgpBCo-CqQMTmcua2IRX3o4OwJ8hNxpECPtVH-0PPa9biw7i-ilxn3zcbvKbsSSB4jlUBwRTkEhmU9W3iDI7y_c-PvVxkz9JQWN8jK9-xdk1FG55wwwma5shwO_cV0tCZAgmarEj2gqqRO_TMxcneX_h_HE-hi8kfBMxQBbPJag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روبن نوس ستاره‌تیم‌الهلال: کار زشته هواداران التعاون رو هرگزفراموش نمیکنم. اونا ادعای مسلمان بودن میکنند درحالیکه‌به‌کسی که دستش از این دنیا کوتاس رحم نکردند. توصیه‌ من به اونا اینه که دیگر نماز نخونند چون اصلا مورد قبول الله نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/29935" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29934">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qW8X4ZvK4zOpQSHq7zgYvdP8BQW4MGbE4JIV71ceWbF6OIj3rJ-Cm1pBQG4OyspKGlfS117e76RvP1bOzaBV2X7e0HLoQRzjX5XINCOl2xSkIuBfrveGeEuRYl4I9HrrXkHIMvOc4QhjGqaW5d_ClAJ7ntj6-mtZIG672sEsY72IIMO0btj0Xx-CkS3ELT3S7vQAP-kn2C4i3cObu-7LmjQWrt4DHvxcbBwgO6BGloUhpk0KjBomefjK7axK95h6yIgofD5xnTDKcLkWh08s4uzmzsNdpAJgwi7ia1Xi9dSo_FkjzTBDtKOHFv-YlzmFVkXCVBY73xtVNWz3BUXXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29934" target="_blank">📅 11:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29933">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGJryP5bh4B5mQoIyGH_88O43jdRIWx44v9oGs1QNA3iG5ybiNP0yncyOaPGx1N4pWh2JuknJt3dWMTjZj7inJ9X1P40pUqJwIcjX5cvdzBhBx-GmkHTsrfC0jXZy9cNtmYqZuJaKDL6OOofk2kJ0WHNSKQ4lbDLDKSUP0dJ5UP9BvV3dFxYjmUlS35PpKCl9IsG_2cFALbcWbaW5GpJbAs8kmExl3Wb8cGP747s3Ky0oIbwIkRF4O-iQ3x4PKLQWglrgjmq2z4p7xn5ISBOxYcYPZXb8h4cHMpLe1PLQZijuvfGs2-RmDzxgHXZ1NgKGMjnlF5pYs34JVD6nTrWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌بازیکنان لیگ‌برتری دعوت شده به اردوی تیم ملی در فیفادی پیش رو: علیرضا بیرانوند، سید حسین حسینی، سیدپیام‌نیازمند، محمدنادری، احسان حاج‌صفی، شجاع خلیل‌زاده، محمدمهدی‌زارع، عارف آقاسی، سامان فلاح، صالح حردانی، رامین رضاییان، آریا یوسفی، میلاد سورگی، حاجی‌عیدی،…</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29933" target="_blank">📅 11:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29932">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3-6R8QVEVQJUYj3buTDpzEhXGYigmbK88IU94poistC_jxP_ZHy870N5aSw3BP1a1wPSjo4B3VJMQz8KCiloxI7wChbDAgfR1uMYEP1IaaHjlKt6RNFRJOLJJIdi9n5SETS1b3ywIOGjEDymw6-d7gLMW9StATTfsQ6zhHhtY9hZQNi7w5qiaxF1--BR1Gf8dZcoRp0LcJcHiTiJ7rkI86vsP5tU0UKKxYx34OXZ-V5DTa_e_5trZsPcND2X679SdNQE7ZRjK1bLuHhPUaTgLIQxvRUHvSLrYDduURfUOoI3dHey5o2pI2cFwk619oDmzh1FGp0LhKPL9i7qX1CQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی‌ پرشیانا؛ باتاییدیه کادرفنی؛ سردار آزمون مهاجم 31 ساله شباب الاهلی برای جام ملت‌های آسیا 2027 که قراره در دیماه برگزاربشه بار دیگر به جمع شاگردان امیر قلعه نویی دعوت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29932" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29931">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8zlBlCEnSIxM54bSOsKj26W5HB6tHGKRN-cvonl_BAKzZEeUOYkdSbLPAxLGooNijOYhbbhTTgi6GHWhrrfLljTyWHdkXQwgGqyox-i4RBzqOIOn7xkQ-StdZx38pvhAzLi1k3hUelCOj6-gznqKAYDADVdG5zCROMWV8nu57qcS8518xj19BU7h7emYPq6xA9XZa2mU7C98lGJE6M-0JuL9i4IM0KfLkcpaeryHDek6ugZvxFwMApzuAc6Jx150ndTEvLWyYrGHXajj9h5X9YyIqC2KxTavpl74eLHwMxWmb5GZtnIwuOEB3w6DJFURb9iJow5ca9wov_EOc_gNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جی جی گابریل پدیده 15 ساله منچستریونایتد که در دو راهی رئال مادرید و بارسا قرار گرفته تموم بازیکنان تیم‌رئال‌مادرید رو در اینستاگرام فالو کرد تا نشان بدهد علاقمند به پیوستن به باشگاه‌ست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29931" target="_blank">📅 11:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29930">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRl42cct9TLCF0gcBUxH7H35M2y30QocMrHd5gbGNfiSbQjKLp1wwvkQq-lfQA3mfrcNHU0rXlVa1rAv6s7DIM_4SZL0Wtfha2Af4EoSiKnfIWWWY476XuaX0QlQmam38z9JnBt8eIC1EFhxa_wb5-1uKpc17CcgyQ4TDXBEdG_75sPNu3mJUlnzsnIWJ7JZK3nXR2A_5oW5U1YbReCKlWslrjG2JiVT7_ORWbzYjUPMAPeQeWLE14d6aP6nBdSNLmvb0znjxhDGFepQsjn96YSn6ymMxOPJWt2ytyvqfBQ4hsevjaE_4WfmuIlIcNHxw6JOUI9NU0ZW1okyZiF7Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/29930" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29929">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rClCoAifTJPR9Mf8H5jSpl-9MoC2ZKJKS6RPJlw-C9IoneXt0a-fjY7lOXdCxW7hqI5iEpf79ArJuv5uHhl_x762octIkSHLlcw8esjLq7AFlQYOoT8jbYQvQ0OKiV875KwVuHW5Ou06Hf3xJGI8IYdPBLSJBcjqspJkX2sYVvyyWlTFNZ61jfdYLkx4JbXzOpLIbMqr1aNImt3GoVJyUVgYjmeuz19ESoiUTSP7eJP1hoTqxdjZVwAL1p1qiXkGOhE1-EC7J9Qz26Uj6P5Gl-Wcwwn1oSSriqsRMnLG9ZfpLLBW1A0__2DJljkFW8Z8usjL833uLw4o2bukTBcGRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیونل مسی بامداد امروز 49 امین جام خود در کل دوران حرفه‌ایش رو با اینترمیامی بدست آورد. لحظه بالا بردن کاپ قهرمانی توسط لئو مسی همراه با آمار کلی او در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/29929" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29928">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=NXY2Qtl41ROfrMSneaib1GlcUnwn1PTixmFWJjV6U_vtfiWLNWsxnaoclJV8ISz0v7ueEHwG7eTF4RHep22vskC20vVHNMn2qv5L-thNpN6aGB3R3AdC8mgbwwkt3IkiQrh49lryJGpXrxvlVi8i_Pw6j7m6JTAdf6ZNKLyfJGpNPlRB5hPrg6PV0l2mTdViwOL4YEmrDGwXjD8ONvag1AxH-4QT9O0ieaIB0bjkub7LKQgNvwfnhTArVo2s_f13Qr3jw0yJUS8Scc7BNHg3eh3K9Lp6wbviDHcbqqd6ChVkPo8kQBAkzaXLzlMoXYu57mb5FK1A7D3Py1b95irx-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92dd5a0020.mp4?token=NXY2Qtl41ROfrMSneaib1GlcUnwn1PTixmFWJjV6U_vtfiWLNWsxnaoclJV8ISz0v7ueEHwG7eTF4RHep22vskC20vVHNMn2qv5L-thNpN6aGB3R3AdC8mgbwwkt3IkiQrh49lryJGpXrxvlVi8i_Pw6j7m6JTAdf6ZNKLyfJGpNPlRB5hPrg6PV0l2mTdViwOL4YEmrDGwXjD8ONvag1AxH-4QT9O0ieaIB0bjkub7LKQgNvwfnhTArVo2s_f13Qr3jw0yJUS8Scc7BNHg3eh3K9Lp6wbviDHcbqqd6ChVkPo8kQBAkzaXLzlMoXYu57mb5FK1A7D3Py1b95irx-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇹🇷
کاشته‌دیدنی آردا گولر دربازی این هفته رئال مادرید و شباهت‌آن به‌سوپرگل‌اوزیل درفصل 2012
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/29928" target="_blank">📅 10:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29925">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1jhsfQuHUlYY49UM7n_dl2BgY3tnxltDIqMXsJumjwxlcXeMHvTvxfoWVvD9Fv2NT9FdtyY1NIEyUvjHwC27pLxFeVpyRRTGJFNb6VKHXxzFRyEwwMjBHh_TXoev24w_xcyvC8-IFQGIzkSfCY-jwX4dYwCNV0iZsvwN8V6wGU9g0DRof7TSXd_Q-4MpkAB5qji2Dfu8a-PVUoK7Pi44YiOC6zAgltTaSWUcOsvUjT9zp_ei9rwAK7Fg349_L-5MkZx0hZGbpLgRN0oKAHUi8jlO-X-v0luXlEinQKnNNSvN-w0AaD-6iNBYp_GaXmdmSyR_HH31sL0VpTODQSmqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7ZlNyfV0VYLKvGc3m3_6X5vk45ezzWJii7hEK1MNUXi0ecHOpaca2gzh_8BBtSuWyrTCbmiajjI45fHN1CJRvnGidC9CHubcZruhuV1NyZ7sxdFh7uvCkXWNVznelfg4zh3aPiaIJ9Oe0mD_zTiJmytoxweMH6cEPM75PgSM4LmDULjPFcigYgOr1j2RA80u8vzNJJjRDmGu3AieLLq4DZ4jmot5hxsDtiJLnhNZXcAr6XED1Ir_VtKSs-1xDJ83lbvZ6L7EdsI1UJFi7rbeqrucFU8mQmKYhj2o-ZlbAIsBUbcK4tHnhselz-9DL0q54SxurlZfEy_hOzQXSGXZDI0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9d0f762e7.mp4?token=pIjPCikpR3XH96b266_cpiYN2V_2sUiBceQ4rH_zBEOudPVJyV3ye8YDruo97oW6kyjJZ9MOu4feQF042TF4wAS0puAns6jQpoNeOjj0UFIOgRKcThwG2MBQMqJDImTYfmDEpMrmv5Bzm1oSbcOC1P8qLIORDOxXZM6mLioY5H-Vm8X_1K8ikGWpVobkcFkx597X090i-F-OfNyq6RQhTCaQWr0Wf1nSjcTyMqvSRVgcPPdkWTTGm6JgLFsqZDEoWOXh1qzMv1oQJ5XhmXZmwpN8NLBr04NKMMDf6de6th1m9x-o5aWlAtuE1HrZHjJdOvN0SQGfehuBlWR2amQ7ZlNyfV0VYLKvGc3m3_6X5vk45ezzWJii7hEK1MNUXi0ecHOpaca2gzh_8BBtSuWyrTCbmiajjI45fHN1CJRvnGidC9CHubcZruhuV1NyZ7sxdFh7uvCkXWNVznelfg4zh3aPiaIJ9Oe0mD_zTiJmytoxweMH6cEPM75PgSM4LmDULjPFcigYgOr1j2RA80u8vzNJJjRDmGu3AieLLq4DZ4jmot5hxsDtiJLnhNZXcAr6XED1Ir_VtKSs-1xDJ83lbvZ6L7EdsI1UJFi7rbeqrucFU8mQmKYhj2o-ZlbAIsBUbcK4tHnhselz-9DL0q54SxurlZfEy_hOzQXSGXZDI0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌لئومسی دربازی‌بامدادامروز اینترمیامی روی پاس گل دیدنی لوئیز سوارز؛ این 929 امین گل کل‌دوران‌حرفه‌‌ای لیونل مسی در مستطیل سبز بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/29925" target="_blank">📅 10:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29924">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePSVPTzEdSmB-Jc1_d8eRUHS08VEOsSN2gKxyhP_rdassnNVgb_tBqfM8PNOQWRwbk9IMg6JlQj5oaK8ynQTSlkdWm1SAut1JZxZpKGLFy8Y0bx5ghXFpEb1GGP5fh9NEywQQu7j3OMw2ETSu_h_ARVN2aJb7rgGHxVSmIhjWOcMgkr3Jx60BZQ2a-ytTHa-AT9wjyJPnplDTW0_vGBYeFMg31vZ3IAMciEX4a-Cqv-a93C773ccwZksSqNqz_RRbu4cQJxQlQJiKRTFbZSspXbMVNA9dETpQiiAhOMyLhyYVrdGUGDcnmAhOBfBXL9qJazCFsw2mvBvcEHyEmIgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یک‌ایرانی‌مالک‌چلسی‌شد
؛ بااعلام‌باشگاه چلسی، شرکت‌های‌گروه سرمایه‌گذاری Clearlake Capital رسما 87درصدسهام چلسی‌راخریداری‌کردند و به‌این ترتیب بهداد اقبالی تاجر ایرانی مرد اول چلسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29924" target="_blank">📅 09:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29922">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/29922" target="_blank">📅 09:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29921">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‼️
کریم آدیمی ستاره‌جوان بارسا دیروز سومین گل خود را برای آبی‌اناری‌ها به ثمر رساند او در این شش مسابقه‌برای بارسا 3 گل و یک‌پاس‌گل به ثبت رسانده حالا پارتنر آدیمی با یه کامنت به یان دیومانده خرید 140 میلیون یورویی رئال که این فصل اکثرا نیمکت نشین بوده تیکه‌انداخته.…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29921" target="_blank">📅 09:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29920">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29920" target="_blank">📅 01:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29918">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4OucnB1s5tYNz19miA2YEa8D_1s3eKyK0cj4n5qQOoyjpEkVzpdqPZ2IyXYv1_dwb-ylTlXsHyNtHNk3ecwHh9ANByd1E5EZWr_eUpp4RbCCu3OTdvcOpWEyUGM-WUmKEoYdCdd-0OVEI7h8MZRheroe92aKKv6i5ZIlvRtighmkVqGmOCf_nXgoM0Wk0cGzgPbOrd0WoNTuSH8Xh2RdfB4Fw11uAyYR1e_13x8lmnSY3Wi1-IaZDQQo2hzkSWFI_KDufLs1AURgC1TNNGpJGqhRAAzajEhdpZ8wxULNRoeSlTd_WmmOwO-Tx0QKYoA4Xha-QG7aeZQKZzzRpgWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز
؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/29918" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29917">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1thfHlv7FzPt_KH0QPQFfG7AxeWMWLHHywuDiOBRnDS_RqrkBm34UPiCnrSRkCPx67b6E5BJonTLR8cehVq1g6-S4JYYFE09I8hhVu9gQ17nm1t4ED8LEkty4jc27rizDWMwFICtTw8IdqgUS4YTqIVb7mRlCN0ScFmOzv-SqoBC-2NZJBS8DIkT4OW1g0olYuKDEwY0DIx2gi0whw5jI2j-FGLaQbMWhZcUYuj9H6024cZe1SIjNr7Vnyspj0y3EDuEKXRggxkViPw8cxppbYTSVGnEDO3-Nkr1BrFHkbUG-nIXoSctuRoIJEpYceji4EOnXQ4roDB5VY-GykV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازکامبک‌برایتون برابر یاران کریک تا برد هفت‌گله بارسایی‌ها و تثبیت صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29917" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29915">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mB96AG9TsA1qFYhBnPkv7ax-qcxMDCsoejJS59j0apqqnvr4M1OB_cKWLspzHP9WisBuLKtRNJclmD43iYIOStM9qNNYPfXAz0mJ164zctoxAC0oyU7mfKFWh96H_mSx3SowKus2DzdxPHj7p-_4GdPRCYR65etWMZyJFQcA_r4Dd3Scaa2-q5oNt4oN9a0dl9AQei5yVXXJ52leqacnG1aQn8jLgLougss1Ja7aC2dlY9z3nOMBasTXibfbFzzYhXda_9jZwKK-X_by6Rpu9_V72mlkoWhwO8wry0bJZMFGWXab1UfEhOMtGmZf7B_g75BG61s2VTbYALDnbPigqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edqbb0ODooBJkCZZnwRZ4mZfKufDrZdohHEuye0xxsVnlx1MqSi-k8aYFWQN5st37LoMw1gvtz9wCQoFWUtXCMwF4V8I8mMjHPTLZzmCQWs53vrnxwjJ85uGaefSGs8xj24CTysTz6mTSwSaG48vtTY9yYIHA3NRchcg_6f6PbuvqYXGj1zihcXYTwceJeNNKRqQWnA1ivz77m_SplQbfeStRjwyimdzJS3klZ-QWqf1NABtyPV2EQ2eURumUEaNGdiF85t7rG7suqUf0BN1ugJ8alK_RE3mS_rGfNadTC_EBkwCXzmy3t0YajNlRWnNODiO7rGt5GOl1mEnLuWZTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29915" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29914">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELhHKFzxT4MC5W8ASgvIwddzQhIiVYCOjGRYijkBqa5MseymtPVotDKrDLKCH90fQrIZfJmjEBAEAkPLsDl8dSaVKyQqQYT5Ivyvu4mVUxHxuyAC1ml8IcV1B7uEAzeQUQyQDL-xSJqpqEjEh7nvhlkgOzJuOczPZfHK9VbIY-UnNphQMECPtxZnryhCqAjZGbqNx24cmrGuBcu4lUsUhWyLP4lyb0jBYSBnNPuYa7OKImjCxWiPZo3sliiHOq-lwNrf8jLCvZPTDV7Q4uyXuqC8eD-WhgxjdJbHmD91sWsQk0YmxDSsC4I3ryfPyyeAYXT04qeepkLgM6NOjkfmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29914" target="_blank">📅 01:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29913">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv2e6-NWZ6ySH4ZD3hdCuIRPOwOsg2-xISeboE7G-8aakNMq3XQlezJBEvBc5Q2DAZ2DQFzJ_GNkMb24UQ7OqU7aMQq9ohDVwQc4rB2wbNNLsSt22-eFp73j0BgFuWoY5nTlXUYjUbTSUT-dSx7Z0W2HMHKpx2dtBSHKGn64lQKi7EMHP65Kpf1zm9mRysrGHoeh_uVYHwQxXJUDd6WwmZj946Ss-c-3mF6RzKyllJk1e8mtyDmSc1MK4ovBnLnpoqaAK1V2vmpdrYzRz_GWrXtw1AZmqzDptom0LzouDppphMHNOOFl67M9FiITUdw1m3GC3NnBw4sZE6lepoEtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/29913" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29912">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLxQTddycIBl7lKbDdbXX-t5iqzXM_hJCW-ktELwxQBWLicLrO_hotLL95R-X01KeelXNIm5N1cAmoi2R0JpnvElVhxnYB640klio9nv7Eip2bkY70wKMbwATxBE_Z02GQPc5g82_0qyqEQvuKWuCvUgu04whnW7IntnwRVe-wyF98hQbRiYB0IUwWzBDMEG63d4dmjk6snbwwRoNPTkiidkRQkj19Dfda_XV3nfAC5XarHVw8r8-pXxiQeEsrFIU8bmODDkAd3VEY4-6v3ctljLjLzJFMaHWstxGBLVxu5MIDUChKMgN4XM4ePfwyNg1JQdnsZc-RpURp5moev8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/29912" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29909">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nye-_8VWXAOIYrIUyzI99FMtfEPhZYXBtKKJN4VNttoos14yv5xp-MP0qaYkicet5_n8uivMTCs66Bjef81VfKV4glCQshoXhkDW-UzSrwvBldyy7r8bfCXV72RLsFfuWDcqHUT1oaiK0U4piIjcvqDvxgneQK0PPnRjvH3Fb4x3JmkDm-Xxi3pNmtnXFS_Mf92JX6f4Rml-entdjH0Ldhu7yIfAPWk5qaMZO94PGbzuL7OnhmNk_W9wsG3RfacvvpueCs62h2jGnj4CvRwdElHbRkmkp1KZTCHNzK6e2ik-PomFGrbIjFxWg9-LHRUdO8-ynxWIuGCKn5-cO6Ix3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2W4i-KgQofWSaFRsGaa3Gp9ixdpjDxgzz4ZkHtR-8-H-JG41XzY2G_X0CY14a7eQWKNYOljezmdYtrNrJcr8HxbxdJbw2Swd2pgP-Zl2Gw2n3hMgmeDd_lr5TXEX5F8kz1ZA3PgB9SUgpaEVEIElOobJmiYLYw--zsvdfp91ie4U2oDET5TjmBFsVTo6zBljESvd6ikXtnmTpQN0f3uApQ5e1qcwQDHdFMa36kmWd8zyl6NRB4QYiAnbBJ4KoGJqb3cMm3VqgKE_ev3mZynFevQsqfTDRcuWXLyBtqB6nZSQhgcGGY-qIWj5miKxDMss0J2KQcuSvvw9U_-Y01DAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدارمهم‌امشب؛
حذف عجیب و دور از انتظار شیاطین سرخ از جام اتحادیه با طعم کامبک خوردن و شکست میلانِ روبن اموریم‌مقابل‌بنفیکا درفصل‌جدید لیگ اروپا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29909" target="_blank">📅 00:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29908">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVkYo93re6bA_gXhmF8yK5pvmLH4NVYDL4vbeyZQOZMJ9zk_n7FeOVQPNuIvL_pOQdpWembxHLTV0SX7rypWgnpV3CG1ik-ZSQNbnaMl4SjtjHhM6SpEeOAQ4cAWY79NFrE4a4sYf20B2S4yV0xCwUD2db9VGjBRGxI2ipS6fh7PCN3btMf53dfnhmG0PcrcKPBj4aegiTnYsPtbuTI21JIh2GDy5ea4SLWxHKHsoIgoRsGcS2m1Qgx5QudoKaYEuiA7nwtdLqip6wGXfYQOe7wbcmdMJMpy7jd0iDHVRyn1lHOBS7oX7KkaM7sib23wK54fORFzdAKnSKpmF8nT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/29908" target="_blank">📅 00:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29907">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9DWPuikI1E6KuVD3NbnbCY8r5LS8g421DXFJ9-NSVWdFjb4yJvy1yAT3MXfPjpnp95H1Z1jxKpTN7cZZGPsK16gTt3wRo7ViKdTqDk3b7tmY-cMB35MPSGf_I11rfRC6pOiXvYNpJE0wfD__DfqbDF7n0h2FiNnFr5eOyPh5lHDMNlimgYVEYuRRGxlH2pA5SqWYngwrWifLHXY0YcmemkprqUFfDrX5pRjTHWTpNI02SRCvURqALE6A10nkdN9d3wDScg-yzK15Fy-NDpAArEBR7VkbwYEGjNpeDp-2sdtSzn318W2hrWX_RFw0lYdNgmMAbp5FCPfz7IJb98BCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/29907" target="_blank">📅 00:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29906">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgIlKg0lmBAX3q6m9CkxWTXf_DtJIct0lz2z_lBjEoTSwe2XgJq0sv_YY2nAtODiJRRzfduhoqNcbnvlxnCXANiyq6hsxMgfPJkYRVE2tmwmPq7Nxa8HV4HJNA0yXeQMAdX-Iow53aO2R0fi3sLag516bfBAh8gUt-yZ5kbxjuSBXK8zmYc4mrQr088VUaOELCFUskQ5UX45TU5YgEdDKuj_d6lVoof97GREhy5DxqvQoMbRIqkmdsThm0yjOyli8SDf-b36LkPHfk6RBVZQXegBlDU5C_YRyqeej0WeaCX0Gh-hMriLRLNIwo-MQFWhUjLfKlbQK9RVVjzhjApIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/persiana_Soccer/29906" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29905">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=p4ue0PTU_baDy4LJ4W_wxujg7O2yYxRWxt5XZfSn1faoLw7cdmi3-fRmT9g7z1eAEaMgC20gYei0Xb6FXpXUrUZpUX2yJefiSsCsAsziwFwn5bI6JyGbqZSZT4oRF_8-1wj6bkYawCKy-lzhuCbs9TkBoxFC6zRcJNslHYgnLPO6Rr4acFMA19Id7JTShQC-dHDc3Z8XtVl0cUSVEpXs_b8zS9_dv2WT09nrTnVnzURbu3QQd7L3v_JG4yee87yuWnQ15K8Qo4f2sjAgnXaEx11bXXVvOgR0Ml2c8VNmdKrbpydmcm2tPdsQZwRVA3i8WRyhF7_wriTyGYwN-oEllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=p4ue0PTU_baDy4LJ4W_wxujg7O2yYxRWxt5XZfSn1faoLw7cdmi3-fRmT9g7z1eAEaMgC20gYei0Xb6FXpXUrUZpUX2yJefiSsCsAsziwFwn5bI6JyGbqZSZT4oRF_8-1wj6bkYawCKy-lzhuCbs9TkBoxFC6zRcJNslHYgnLPO6Rr4acFMA19Id7JTShQC-dHDc3Z8XtVl0cUSVEpXs_b8zS9_dv2WT09nrTnVnzURbu3QQd7L3v_JG4yee87yuWnQ15K8Qo4f2sjAgnXaEx11bXXVvOgR0Ml2c8VNmdKrbpydmcm2tPdsQZwRVA3i8WRyhF7_wriTyGYwN-oEllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
گل‌فوق‌العاده‌دیدنی ژائو کانسلو مدافع راست بارسلونا در بازی امشب آبی اناری ها برابر سانتاندر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/29905" target="_blank">📅 23:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29904">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=ePymEQK68QpEofVDBTzyBjXwCJw_tXk30qiPkK8IlrBniNpAyW-WBjxEXkzsEYrugy6KQrekon8F7Z5_JomoahdkH2HwVu-mXGLZqh3f5x5-YFzgY5e2hAYhz9LbUIBy7Xt9teIRC5OGz4TwSdJXakBpD0F9cjYZfV7gTfJ1_ToFSQdtCChUmcpOc-h3v7AK6Q_dtXm81SdWPviOhU9XGPhtI-7PdrPNfF4KSf5dntHlDbDoTgmyBQ_wPrC2djggJoKW0vilE1Ozch-q23gd3_KuKB_jKllGoHbSkCpxP01O8NgMMH7jvZjBLG04M2N_Qnzj7icFOrQHJpAVfUDLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=ePymEQK68QpEofVDBTzyBjXwCJw_tXk30qiPkK8IlrBniNpAyW-WBjxEXkzsEYrugy6KQrekon8F7Z5_JomoahdkH2HwVu-mXGLZqh3f5x5-YFzgY5e2hAYhz9LbUIBy7Xt9teIRC5OGz4TwSdJXakBpD0F9cjYZfV7gTfJ1_ToFSQdtCChUmcpOc-h3v7AK6Q_dtXm81SdWPviOhU9XGPhtI-7PdrPNfF4KSf5dntHlDbDoTgmyBQ_wPrC2djggJoKW0vilE1Ozch-q23gd3_KuKB_jKllGoHbSkCpxP01O8NgMMH7jvZjBLG04M2N_Qnzj7icFOrQHJpAVfUDLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لالیگا|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/29904" target="_blank">📅 23:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29903">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyf1O2qFBzmHq_dpN24K8KqivfYy-m_taAmXceBl1wkTyTIz5VcSBrznkpal6pD9Rzy3Dz-ZisSBQzBBudybYRzW4twZ5GXQaqyWjD2S1ej6OwxhqGhPB8sBIUptjxLhhjVy4tKOxkqPH-A2LRrR6Ynmhb4sgFvr8ANbZQIxygPgxqe1zzUi-oF6ZT0V7Zqi3y1l4SpICJdGlpq7eAWKh6W_HP_luoWTrnIKUjd0jOdN0Qphigjwwkmr6RTkdQcksIWK6IzGaZvv8sbMT5qvRDNPcRZzgUYKyF9fhztB_ITjVQXMLoFUnvSeqTth4RwK9ayNK8HPKycpqKATBs5UOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/29903" target="_blank">📅 23:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29902">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-ew5I2PUDaz2Q5OSwhVEt9b9MNNEbTvt-jjcrmPWVy9uwh3faZHLgsR7sWi8R6BK2XLxiSn9wvt_UDkYFl6a8oBpaQKcx0Xtt63T7xzLCkMqKSpUrFrGas_nKzynIacDI8pFDYOi1ShdtvHS1AkP7WP4r7J3CPWC4EyLfd0FI9yK7H1PzV5H_HDyQgzoK7KdegaSQiXdnCKiRtvUuGVHVCNyszbqPo0_m2lt3mbGyOvwT1mId2M67B9pVVUJK37H3qhIGkDtPV-3ekVJH2Nwt6TBUrnkWMCWxLGmvc66NVs6HXDJBPcEVBVd27BWtQv9CG04OTYZva2otDm3BNQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29902" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29901">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-WSftXSD-3ax68YWlphoti_FrsP8SVpC46S7apZlHre09L8DFqrkblSRYRCGppIO9ymnEA4YG8ysteeG1LnNQ9hAodNcvs8rzTgOv_pTSHBVvcUqgYbXeVcucncDEWUnm0DhBbTtq-9n-TxnzVlREA69-eHOAoHDMPChC_rSBM6d8yFZP4P3Als6JZV9IqkeVsrzGPrYqYL1nOZTZdOWWatIEzaSsAsk6rs_OyJi6n9mBsBM2Uw97lL9iVwI_icRFS5XMWLv0W70aOrqdwKt3qnG3-RDfAswYTDs05p0XfhmRgTW735URguckAZrvjM4COIlhUwyNGsFIdMZ4Kf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇫🇷
فلش‌بک‌بزنیم به UCL فصل 2017
؛ که تیم موناکو بادرخشش‌ودبل‌کیلیان‌امباپه 17 ساله بورسیا دورتموند روشکست داد. تک گل دورتموند هم عثمان دمبله ستاره18ساله و فرانسوی زنبورها بثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29901" target="_blank">📅 22:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29900">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k5oF5-QYWawyxZ8fVk9LU62G7UAV7LQxHxbe_W_Vt4I1ibemKIayTqt7eGZie4u4tIWmcMJ-wpby_PYHBxtpGkwx8VGGpsmetEmuD3vSYdn3E-tFCFD1Ij__bkYUWiRJnbz3rxgsUj69QbL-JmJvnlgCCL2qc70iOM4_ld48OnS8B6NvZNYAuAWTfp6jq-wCJDyNtpx1Oj2yTfzTkRFHtJ93YvWBZ8hBZx2MjDE50ta5BBZdG0QGx5W9yhpNLVPgNhjAJmbNcATSfFsHna2CaQgsv_4s-285vQALpgp9cuaxjwz1wUiOBivTTByJpSqrMo6aomrzNoBrJwf-YdyIwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش یان دیومانده خرید جدید رئال مادرید به شعار هواداران الچه که دیشب شعار سر میدادند که رئال کثیف ترین تیمه. اینم از حرکت دیومانده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29900" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29899">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0h_RyoG2RzdZrPsZvLzfXnTmThYc2zMfiJhzMoWG-FeO1ljGqSxQi_zOwqwJlLoBaojOJ0NxTWmqSioE0kBcuQ-cmY-043jmLBWfAfWDoZgG8T2weXZvrSR0MtE0YdAWXFttDP_nUul5jh4hj1mo55ENSLePEpIkWEOrn4n9gJCczbFul_ci3mrLWLUbHoqfA2xkw1X6GrxKYe2Z0KAPkKOgIVAF2WLZwhhmkOWp-aTs4NJh5srS9RhDEoB4Njqgg-o2c8YZhO8CGHXp-ErPeiqsREn8ujlfU6ZAn7mt5CSPHqZkhCukGM4yLRbhRNWokPWSon3Gx6B_4li-ini_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لالیگا
|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29899" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29898">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMEICRjiY2NreKSzlKMEkPOiN-42bJXANySkBFn3OwylX6zguFEVPRJPmpt11pCBkmeum1tBdFySLm_-fd0sN52wE5YcoVJFFsYS_cugwbqPm5AmoENOI471PfFeCNo5unw_GpEBCbhsK_4pcF9ct6zEQJ78iwUQrDTG5_j6rBgMnM4UN8fK1W8wpymY0xM8NK4DO2t8LaoXeBwrG_pddiMHXmOro3rkYcP-wuZnVA_VK60hN1uiEb3BRIP3sqV83_FiNfl4Yz4m5xS52U49a22kGUMTCLExgfrogNgUT9OWgag8fjLM9VS0Mdx7jrU0MXoVEuIWm-koVmT9hQoaCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/29898" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29897">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fszQQl4jpyo1a5PaBKNJnQhJ9L3G1XyBHjMFjeAXO02C6_s6UmSZ0EtZFFE1KXXGIG1aBX5knmoEtfpLqZkwT_h6cAYHdXi6ybNuEerpXbmzL4m6IujnVfFI0OjGOsjBLV8GvYcPKqftUjldby1sDXBsWwfJiGa_YhuoNPxIlj2D-H_AAJkdMqIGS6eXcA37eW00o3dXU7Ys6dOkIaU3j8S6CWwVPFbIEst_ZrCyiA3sigk5zdQRmI_hZfyeAS5SA4jM2WiuytivY9lQCutVZeviJWALJCRQiYQxDCI96mPfpQIpin08hcR2tRLIfU4mXbssIjvaw-smVKKQfO_b4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رونمایی باشگاه پرسپولیس از فرشته کریمی خرید جدید خود؛ کریمی از 18 سالگی تاکنون درتیم‌ملی فوتسال حضور داشت و بعد از خدافظی از این رشته به تیم بانوان فوتبال پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29897" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29895">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk5sgj5NMX35zViDGucr6A663uvyyFWcDJQbnmMctVhbP6pJTZBeHbP4dkWJZrYN84-b4D8Q-le10LpHyvmi-Fxlzw_5inBHBFjEGmUz7LXGT6uz_knDpUyld_Bd6ysPQDP7eJJRjgBQTfjIeHBMg_yaKIEcmzcIuW2JiixAODHSkF1Ks2NZgFAKt2BCSEfkZ70VEjO5uh7PRTg59fE9MoJ-fMFLtskljoslBv4-cxzoMtHRpJB0QQUi8uP29P3a0FlBL93Qfc-E71yEObQt1iM83WQZTaGNNjpHa3wQ2TXs7OMIa17xjFdqViCYH2tAOixonvAJY_c1WfXrBttL8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ یکی‌از مسئولان سازمان لیگ امروز صبح به‌مدیریت‌تراکتور اخطارداده درصورت استفاده ازعلیرضا بیرانوند در بازی با استقلال در هفته هشتم لیگ برتر که روز پنجشنبه 16 مهر ماه برگزار میشود بازی سه‌برصفر به سود آبی‌پوشان میشود. اتفاقی که سال قبل برای سینا خادمپور…</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29895" target="_blank">📅 20:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29894">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkurSlhdORac_mZR1r8op1hzNPg313IhWpJkw5JZz6YynpP2SSNg-p3GQHKzMtxZU4PomeEhelZ2ec6bZ6NNCpT-bYV1wZONi1_CIAxhdgORD-rBUEg7vWKc5bwoCIVmF5xFkub3lYUcNf0d2iOqbSpEuX1lyZ7Lf-rG7nP2Pmpb8n9m-3K8DTBPReMJ5w_mZ3dQrF-dcQN0_qTxka1x64ppAl2TcC9ET7a4oNDLCAAnsOxc4uAkqspxXxrNCnOXVp4cP5Jo6LK7Mvhioule469xgNsDR99eiBTyHK3ETajqkg67mFRfUqYhzgVhCeutuhnSWDul4T2wBxG7J5OtqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه: پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه.…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29894" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29893">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9fTzjejZzJd7u-PEirL2VaPAZ5XSSaIln8LbclBa2G_0oULTnr07_4URB1Z-Kxg473d7nzMJUb7dPTzKvbiYTanCJtmuVIArDCjnJRtBtIsowoId5rJIR92EkKviSUW12etqXmPaIgSBIB4Y2lFXoNuOKSzNU31chlzSdA9TKqi2lPkolNML4Xai2sxPi1r9CPMgCf8LA2feDMrCxFuZjh4SOGPbmJHELJUza8z10GtZbQdp3CdbTlp2qgzhpXre9SKWWjnHHOL5Uf9sU1FehGUm6GjUdcTDgkhKb1BrMVhoR7I0m3rrq-GbWJPdFPL7DVmL1GaIxr0m9M7q9b8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
رئیس‌سابق‌اینترمیلان:
سال2012 خواستم به هرشکلی‌که‌شده لیونل‌مسی رو به این تیم بیارم. به او پیشنهادسالانه 500 میلیون یورو دادم و حتی معاون باشگاه رو هم به اسپانیافرستادم‌که او رو راضی کنه که از بارسا به اینتر بیاد اما لئو حتی نامه‌ای که من براش فرستاده بودم رو باز نکرد و آفر رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29893" target="_blank">📅 20:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29892">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCsg8dlMkzYgmGIcelY3vDO9rlfmTxapZYkL1kQLA2AqGTq5xufKEaC5Zrkzb45TZYz4tSZewvZALEWWO981UdZqlsY94D4Ij2U5_UrKxNbEgF5Wua4cY50oLA2XAf0zRj2B7dS2n_vlTXEUiDjLUX-25F5hLWC8QTI7nBhFP3eqcfyJEGpH2YdMn1Hons7Jck53xVY1ULHnhD3e-2NDZVM6oRqUTDcUuzV2b3vPg9y-Hf64xJ-Q-KWwH6vFOjD9-EdXdL8sBcUkgcSdxCSAiddiYjKggJFiiijDqji24K5ii0LMkY_Z1NpcxQoHQnPaL0HIUUdZ41SiyLXxVuwaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29892" target="_blank">📅 20:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29891">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxdK4-8l3asalAQ0cfx-M4Z6A0se6gGOepPQLRYsWCtYq37rJMewlK0cFr9Y0hw9b9rn1iITEewZcfjMdOcIuev5FT7SFqWcqzaculJxGFbup-OdUDBaT3_NJAI_uig4IxRW1bqYQeohEq15dhB-hD1bh8wisySHNljmtm_pZ7O-Ax0HUQpVBIYkQs5yqSW3DmmIhK67ac642KiFFxKSX5FsTAGSeHkviImXmpBoR4w8bSoXvK6AmDtB2aOtYL-e7BulcFccUWvr9SJqGyZFGDNIch5qj63mvTl27g7HleKa3zr1LN5buhxV0SqI9fmuXxJqKOgIwApBPn0Rgyk1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان: یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم…</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29891" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29890">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTwy47ovOMtjPP9_sw1Fr0jlPl8EiL_AUclXrDegOb3psGIXj3YlsQNBSkduYvhk8hGyQStg8GJYwx4gxymvAhvg965tx_8shjEp63I9td3ggFPq9RVBSPEi7CeSIM4dULA-5JBhZ27rEO3oJzYPhGY4ahOvlOELV4tJZRJnzn_0KrPVx1Ovs-HsUUuwTztPRUj9AFVVTwsybP_3TyuuJ1V0UCQRCUF28I5bd3dfdexh6hvrMdwFF4kDfE77NIKU9oV1cCZxFWKyaMbnWMH2akbLM50jYc63LPtAR3_XbvdXZcs888y1ec1iNT5MJF3I-0avL_nKwkASRkZIEa2bmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
یوونتوس در نقل‌ و انتقالات پیش فصل؛
سه‌مهاجم‌فصل‌گذشته خود را فروخت و سه مهاجم جدید گرفت. مهاجمان سابق‌یووه این فصل روی هم هفت‌گل‌زده‌اند درحالی مهاجمان جدید بیانکونری در این فصل هنوز موفق به گلزنی در سری‌آ نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/29890" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29887">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvPZUakitR-IdYMTbxlSuzypBHepMnIbNu6Sn5wwF_4YCw5O9_UO5zt67DsugSOIbN1RPeD0V-NxMcKLPZr_WW2VrSjdRH_9O3TIM7qe9tnyeFUVqDp_Bs-JuLagPhSEqBDiMwnccOY34WZeXfoC6l_bClNqNTnhEauA87OeJolpcJ4xPBjEY3SUCOxuR1gK-_OBG5suxfjs33xlJ6ye654eKKlus6eK_6D42JbWUhOq3_0pRdb4xKCYzitleA2sPe65L9IbZz83td9OREJKJCge-2JlsJRmd-KlPO5V2a2L9TsZn-BuisdIVXaIGsWe761TbkSwBJHjJyLywNsBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29887" target="_blank">📅 19:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29886">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdpIjg0YtetxU3EQpvx97myi-4-MnyBjo_gP_utJ8PjCA2bYNCJ_FXTramRaJJwLRPtzw0hHJ62mB02gEexuLGMh2RR1qoBF_RsBWIpRJaSGdUf1zpSXWFsM59AfpMwuAG5GcaQqJP_S_k6df7InaAkllN3SK3Hck8VbcAyB7qYrXPWq3XLRUepkQII4J4CMbnL7cJuH8YW2knS4NWLpqATjfJR6JBStghPzcOkZ7m1-yC8jsv6giiW2OQZbrSzhySUt_ZWrbGb89y_gL6KYysiXFMZBFXdNf-TXyzDC4mrsGZ1IglGogopqE9ZOIdjhoL6AaJ86qk8JkKaYiPE0Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29886" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29885">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyL3AdEgDSqkBnE-QT2o1NMGJzJeOMwGFT7Y4m2LPDcqR1faKJKfA2QBU3qIIwO98ynZJw0ZKUdMZ4gE4GEtP_n5N5iTVWlO2C06I7lVbGCm0mgtR-pfJT5XIHIjUuruS3Rty3KZGy2IOUfpz1WWbYvIsIvSYScesU7cjkCEfT5YE0A69eTK5GxpwqQa5-PKD-5Si4DRMmrJe6Av78Hs2wB7CYqWLyOuq-qQ7Nkty9QRU5sHmKcD4wx36AYz1IKPiTedF_valD7Qej9R5FEBmF3SOX671SAxSug3oi81dip5f8L4AFuGtBuaElyKkECErZoUApsyt7kj-iYLkZ_v-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو: این زمستون رو نبین ما هم بهاری داشتیم. افسوس که نامه جوانی‌ام طی شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29885" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29884">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQSm3hIvjDLCN24XZ4DJwvA4K76ZmacVsfTzeuFtYXLjPN758sZj8LEPlR_br-9zTT2Yh4wU9sGjUyirJ47OKhAnfzMbI-YS4-lVQh667PnZKlQtEm3iSU95o8Xb2ffMAoogaTa8zWIZ8kFcOkzaDNYa5oovLWVZkbqXOtSkxLOfrMR9JwsdILdvid249D8cyA8f87eWqFi54BSDvD-8CQbJH2wPxbXOpoQp_mukJBVmlGZtkrmNaX9XxBxwrLYNg1Aq_F0qsehEopsqjSjypA2bwvxqGPvgCfFCSkCnfyo3fCb6sh8cvCz-fqPeqa-VvpcmgZPd-EgDiXKyRwO-og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ازابتدای‌این‌فصل تا کنون 17 موقعیت‌گل‌صدرصدی رو در بازی‌های رئال مادرید از دست داده‌که باعث‌شاکی‌شدن هواداران رئال شده. پرز هفتگی داره 600 هزار دلار به وینی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29884" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29883">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=MnuQmXuuu7A13hkweaIbBUpHAU3s_8dwfiubGyHx6mDnIX9A99d7FjXXdTNyo16uidSMEMaWSrgte3TCaSYTx6g36cj1Ks55CHnUZhQqkDWe6VjdL6HbJqZ_iBIf2aHujA8xESf9rZp3t3SFKa353bvhM2qHX4xKYFAOW9HkDgHhBCruwc5azIAvjdf8weWshNg2azIODj2uGi4LZlpWKwUJw9N0wOpujIVnBJpqAt2N3-PzlHhSYdINMe_k4rhEW68ebB8SEjDyEBg_DdYeqh1hWVCXDF2sGzhaAALuXmObYkVqO4-oQjTmFv0hpHgz911g10RV81TuR4-qNboe1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=MnuQmXuuu7A13hkweaIbBUpHAU3s_8dwfiubGyHx6mDnIX9A99d7FjXXdTNyo16uidSMEMaWSrgte3TCaSYTx6g36cj1Ks55CHnUZhQqkDWe6VjdL6HbJqZ_iBIf2aHujA8xESf9rZp3t3SFKa353bvhM2qHX4xKYFAOW9HkDgHhBCruwc5azIAvjdf8weWshNg2azIODj2uGi4LZlpWKwUJw9N0wOpujIVnBJpqAt2N3-PzlHhSYdINMe_k4rhEW68ebB8SEjDyEBg_DdYeqh1hWVCXDF2sGzhaAALuXmObYkVqO4-oQjTmFv0hpHgz911g10RV81TuR4-qNboe1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29883" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29882">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=JkgI96VgcevdX7kIzjwgtZEAbhzjzRB8J5PIYzqSn1qMYU7gEBDcikLRJaQntAAsGnoX7cUzNhbWnA-oxne8keQQiqRCoQNTlRVTBU5BQnlD-JjcrZYq8cAOysM5dJgG2NbF1FG1k25v5Edh2bZhVlRYIwK4wWjJupO1WPi2wDDpgxVv6kq5QV6Ap-kPXH8dNCr6ILiHiYcwLppjcjgzjJQLN73hL9ED6Dai_f263vAauNOSXF-kszzn6Vwj99F8zN7TTQTJEjGbS3ZurDWytOv_LBLcr0VhvMYbR-I6kCleVebpAGVj0_Yd1ZDphtm1u4JCIF4BQN3tsNIs4jxobg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=JkgI96VgcevdX7kIzjwgtZEAbhzjzRB8J5PIYzqSn1qMYU7gEBDcikLRJaQntAAsGnoX7cUzNhbWnA-oxne8keQQiqRCoQNTlRVTBU5BQnlD-JjcrZYq8cAOysM5dJgG2NbF1FG1k25v5Edh2bZhVlRYIwK4wWjJupO1WPi2wDDpgxVv6kq5QV6Ap-kPXH8dNCr6ILiHiYcwLppjcjgzjJQLN73hL9ED6Dai_f263vAauNOSXF-kszzn6Vwj99F8zN7TTQTJEjGbS3ZurDWytOv_LBLcr0VhvMYbR-I6kCleVebpAGVj0_Yd1ZDphtm1u4JCIF4BQN3tsNIs4jxobg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/29882" target="_blank">📅 17:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29881">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=LNHeOihyX1pWB50v4iJakUHePOzOvetIfdiDxBkJe9c25x0A7f20np4Ew7ae7eHiO5f1Sh5Fc_FK2iuAvQzJcZ-F4AqLOpjX10a9ZKJyNOPtAPYHgEID0oUGurJc6kFIKlrmkC-cfjCjkFBOw-pDgUyTX31HdbjUUTlBbwdZsJErR0w9XSXVcWva9f76tJbOshlJPsOLd6GqIVwg-J3x6EmL8tjJN-Ax2JMjlUnfnyPDI_VI2hEiLkQ8fB5LKNTYANVixi0JPASOMytIGaTZg0BBieh3DQ5oBPyMlLz3JrORPdiDsPXT88NMSNM5HzvoKb-gczzDPVe2JskC6NQIUYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=LNHeOihyX1pWB50v4iJakUHePOzOvetIfdiDxBkJe9c25x0A7f20np4Ew7ae7eHiO5f1Sh5Fc_FK2iuAvQzJcZ-F4AqLOpjX10a9ZKJyNOPtAPYHgEID0oUGurJc6kFIKlrmkC-cfjCjkFBOw-pDgUyTX31HdbjUUTlBbwdZsJErR0w9XSXVcWva9f76tJbOshlJPsOLd6GqIVwg-J3x6EmL8tjJN-Ax2JMjlUnfnyPDI_VI2hEiLkQ8fB5LKNTYANVixi0JPASOMytIGaTZg0BBieh3DQ5oBPyMlLz3JrORPdiDsPXT88NMSNM5HzvoKb-gczzDPVe2JskC6NQIUYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت
؛ علیرضا بیرانوند، داوود نوشی صوفیانی و فرزین گروسیان سه دروازه‌بانی هستند که تا پایان هفته هفتم لیگ برتر موفق به ثبت پاس گل شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29881" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29879">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9fTIl1KyHepZK9vmViuoOUPKjWOJnbDET35n4T1WbR5VFzwImylWHdaa-3BUn-w736g1pe7juo_Nhl_9oUHJ9xOukWA8FvSVdOoC0fx0vCCyi0-vOP8i14r2xmEB83kvB6JxKBcnUh4khLioMtJ8DuLaLo5qxZ93VRFxcFiCq4MdehSeASBVoullgLO2kSHw7XoYZn3rjluVeY6S8uvWIKlu3l6Kwu4jHQpqLDoOVvHZ7JV5WoFDAc54e6XVIWtboPivZwWtjXfbVAfigeTCv5XjMQGM6FmBsBfRAAWNHRVVe2ANyQKHkwP4BMv18amyKqfsP3ytwuomrGbMlNT3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان:
یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم روزی کاری میکنم هرجا رفتی با افتخار بگی زلاتان شاگرد من بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29879" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29878">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DG7FTu_flZ5hA0Pms2dktUGL7cIzQX_vhmx8fUUJ1OBtGteBtQMmAcxsAq79DfpswhIJVUnsPGNTUeoKoH3eihCji3MKhNHKtycb0wV-tm4CZu9hJ6TOr4adwHtKKcFYVYNmYMa-BO6EVcFG2bmFNZAPT5YjEmVbYe7J7OjDyUbMPCjpyV8xFq2b96K6bDJxeYRm3wMzFMTvz9q09COtyq6IgvB_-XF7mHWe9u92scS8Nu30mx_FWkF6-l2otVELWoiPVptWZ7cdBEJQ0M3yU8224b0jzEgLq0-I26CaI4Wu9lVl2nfQTPwe4cnzqpPLpK1WFVGZ2jtXcyTUlg39wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌معاون‌سازمان‌نظام‌وظیفه؛ از بین قایدی، حسینی، قلی زاده و جهانبخش تنها کاپیتان تیم ملی علیرضت جهانبخش معافیت تحصیلی اش به پایان رسیده و باید تکلیف سربازی‌اش رو روشن کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29878" target="_blank">📅 16:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29877">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nSJNATjAfBN_hol8LUHsa50O1mBugfLvBuZ8IGKdiY0Boc1Hl8nUhbrQNNsV5yIPz-hZgFHIgLDxSvntnvlELY7JALVLNrWxLuVnmRa-w-_pxDFdwPYfP-0yflMw9P-eXYCJKHjjw75KTLmL5u5iJeRtUhlPOTI3Mn_8sI36TPgUeRZxqa9p7PT1qZwT3476gwdYLZTXX0x6_7Fn5TOXaA3B9V89q7kL-9Wrn8YGigMyJOdfXvbKekSFLJc0c0xCDVeATt9GF_phL54_PlF_2voIvBQBpfzyuqKvtDRq1Up7cKRQdeltQvNCti-1XdOYqkPsF1sRUafJ_x1ed1hRlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29877" target="_blank">📅 16:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29876">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDUgLgQ3fpXqtfVPy0jol8jBG5A1XV2qFZdjGTc3seJdr29ViY3sie2yOAUPQVUZIHQNwvetxDh4q9wA_trh_iJo5fHFTpKgQTnPKrAVph42ZePlvLx0dI7Ln5V1uzb2H0QNM31BcSCWIaytHSNeS1YDGxeqUHf7gxum0vqDhlBAuCYItt3IFE_V-oqEtfiHWFx7tw65k8TmrSB0geo5V3md2BETpIWN9xPQfVGTeR6m3D-9DMe3mgxOpqRqScUeuBw304RBcGP-iISBGbYv6Kbc4sUsyECDQoVo-x1iPCfsoDgxj78Cw_Q0p1luSWFFp99lOXuG6tr0gozdwXjAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دوتیم‌آرژانتین و پرتغال به مناسبت خدافطی فوق ستاره آرژانتینی تاریخ از دنیای مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29876" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29875">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQNPFYXyQv2c9soCSl0e2YR_fZ84HG6DgITB7OQrh65MKi1sAgOK9QUuIGmqCKDNHKUCPd3u1SpIhuGti-ofr-b4v5pJMbHPUvmmc96cBOhHg0iRSbOM0EkeRmbbbuPn89aCylrY6cLiMgVcCxEHoGz-P8D-cw6Q4CkB2wqQIS3zrKTfTz5T_Jn3hBCiFC-JQboPFKPi-qGXWtwkBipExCFBe_VeQ1d2IVCClxGQ6wQmPFFT19qPYRkIBHKQg8m6F3RpoHMGLivbTeNzmKRyp8T_7VRTyhM9etQGiVI4TqsCcRKBJjSrc-7kHcMul08iU5L-uQd4HvR2qDqc4F6SsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29875" target="_blank">📅 15:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29874">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9tT_JH4-Sa4om-dHHsouJ_j3_zxDR04PUbl6DkwzR2dpeqGPiQWTLhUUwolAtQDtf6pBzOeSmyM-XTV2L9rISDtFYtYHNVKZbfVmlEOHJRwDoKueIj_Dhkq4O_zh_sl_4xKbfqo40MBwzeS453uu0MFnHOLu_ZBSbGuBNW_DxBLqFJ25LSqzXfRuZNFR-8VMEXc5eZB3pQxl_ESqlmbVadknbcMHB9A222KH7cLE7eFC9lBrTE02HEQxQr2-OGdDujQTXXVg-XBEU4SGhUoO-Yc81yKPHit1Xl8cNp4c4EslXBmjxmUUQA6sUJD3sAAWdBVh08z7vGl8yIM3250xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29874" target="_blank">📅 15:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29873">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umtCzGjx9iUvwdFC3Tv7vcMynt4MRnTO3Z9nWomzdp_10Re0TowSuHTyNwGaCYBfjnvDDle4UgRC06zywusM3bp-XozrUVCDVXSnqrU8UWT-SJpp1hZktR-ZiQYg1oJre-Ro07OO-8b_k3DYeuhJreqkDdq0DswTWL7e7ghJb7GTYHBm9es9LibxqrW0YHfCTWGITg6PvzdoupGsrtO6_IytyhPy2N-Yt6PwOnBynq4Jrzt_aVpByeRYVyvc_PsLzTccXW_-i-zRJ-upuWiv-Y7dhyzA4dMA-jnWQEKQ9gPC4GOt4T8rj6F_mxA9Knwpnv-LJl1caEh_BIAePQgiPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29873" target="_blank">📅 15:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29872">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBnGvOSN_524QVlbG8EEJDrvgR0mWsmGe6cayQMTfPKVETwBhsRX_d0AWKHtzyu8jxQYjWS36NgyFzEsE6BzSULNx3up0ElHcZzSBlfdB65qaMRk255Z2f3wtwtIOYCVCAnvv-A45puS_4JCv8TI29vn5W1F_jIPKFkFOx4eogK6CkEFMEhEOtYgirf4fga6cvXiPZ4RZkFZ-aREBYq6qwyj1oI7B1Z08mL1yE5y_UeN0Jrg50LenHtetuYp7bPVmb-5dPJkYtLYVHRiHZjSjjq9l3ndpMcX0dDGC3fv79DzxbX5P6_0Ej0dHnodSvkzo73t0osSsq54BKTCk6HnEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته ششم لالیگا؛ شاگردان خوزه مورینیو دردیداری فوق‌العاده سخت و نفسگیر مقابل تیم قعر نشین الچه با نتیجه سه بر دو پیروز شد و سه امتیاز ارزشمند این دیدار خارج از خونه رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29872" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29871">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNRCxIpU08PVttcwX_r5BOb1SLK_5DvxB7szAqhT5QvnjDwt6LtinW0erf08VgUeZylplp9RlkoDPVSuaTXqNsV6z89rmDbymkAXs-Ge3bnrfd3HRDoOspJdy1653lBrfIfjyKHaLU2fsnQDEdRJZsh0Hdg7dWCBsPSlye60AmJGPx0ggGwQVArLOMcKGP17Igz3GQwEP18XmXSrTbMivZU1CnUBR2_xYiy1ST2wwM9B82nNVq-joAEiUTXjcd_GyDlMK0FcHEz4G4WdBUcLHJ3f9Nb29JV5n70GlFzSW2yTC3xgU8GnL0QUj-Uovs5vARNUI8zZEFqby3tlbrm5Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29871" target="_blank">📅 14:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29870">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29870" target="_blank">📅 13:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29869">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bd8rs9aSXE80OdDo-n7SHLd3M8kHX6Uk9mu9x1VUE61hPXWFnM5Q_-VhihTfAAPJoyF4B2mXziIrkFs9w2x1r-gUoKkyKNjALL38e7R-XFl1h8UoMekfC6Rd-vRa0rWowz2lWduYipsCG2-a7pf6UzEVRZdA5CkqoA0rMZHeDBWjxNKTJZcZxua3vxvj1Kgh2aug-1G-0aucj0ENS3RKCPPJsuXmY-N1CNkBxKhMsWfJowUBQdnwwCTRZZyMJDjojaBewyT3T8QEeUVAnwp16uRuv-4lfnpQ5wp6u5vrEQtcnDm1umhBp10yupOwk9XRVz2QRgj--S5Y5KQpWNpLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
سهراب بختیاری زاده نام دو مربی جدید ایتالیایی و پرتغالی رو به مدیریت تیم استقلال داده تا با یکی از این دو گزینه برای دستیاری او در استقلال به توافق برسند. بختیاری زاده اصرار ویژه‌ای برای جذب دستیار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29869" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29868">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTwtc12u-UsWxwGzSPCAN9axaAsd0rBTQ1Eb86HsYbWLYRBN4Ny_DrIDweZtiXwsN-Xx4dff2o1JmbyoSubkj5dW4Gx4EDtbXr56biPoIOGNchyr5ddFBA3e0Baw1eIF5cyvKigEOamcEEMP2sFeK39W7B0TGb-vYTm_RoSE5z2oRFdiO4hOvnKvbvSXitPg2ntG6qP2xNAiD2YUPL77Gm-byaTplpAaPzleqEvRHQsn9Ddm5u-FglvS90nStH2cWZ5apTHUHFHextmNJQZg7dO2UTtA15v31dbsZOXeRT04RJUfNxZ5ZGzzsDBPsrRHSBQ6wku11AiLdnX8TzK6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد حبیب فرعباسی دروازه‌بان استقلال درفصل جدید در تمام مسابقات: 8 مسابقه، 7 کلین شیت، 19 سیو، میانگین نمره 7.9 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29868" target="_blank">📅 13:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29867">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBu1df0msF2E8y7RIwVAZsfFo_DYW7zyQqLv97m-w4vFi5hW5QhNVbhD90y85q738zkRYdRZSh87tuipfw0pFg-i6Y9YsEfC3GciWD-BREPK_gYEFo-mNwPtLUFuWTy26MTTQZDc894x_dVVT7-lrydyKEwa-za-Yt7eDhC7XaeRKgrTkUy8LaAlOSYJR0qkUhiFeXR_acMSRaD8S8o3gO31r1KnSgPSQ6Z-4ZfH1cbpOcSv-IMENqodgETwqwJALmxj3E36tyLX9fbYoU-pf60tTd_fwsLAGU1eSjcgVnEtdn7BHdfpL0XzsTztWjKyrx9f3KXoqluFZI61MwxVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29867" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29866">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=IK1LUibRwLC8bO1FJVRLuZE24dudfa7JqHhGNqT6dXcVbWu-e33pY2-fjlf8ZE968dpN_JA6pk6bQwcNopJQ4fir0DAo4bPs5PekgfF1li7hHLHl6eXlJWU9N1BlRSxHciDhubQOk7_iau-bgmRJg9hpwvmJn3bXq6o-V3BMVLE0UHcCJz0R3nsqD1lV_GqHTrYyxxSQJbysf-E7uDBjUyLY6C8RGgTjBtStRrky-WWQpQBQRbmmT88dOVQK7_zcoRkW3qlCE-FB45RXAv-1HeoWvmsBuS3OD26s3Xiu9MnJxYZ0bDvbhxk_4rYk9j8lmO08aEatoLWhdwOoxYSqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=IK1LUibRwLC8bO1FJVRLuZE24dudfa7JqHhGNqT6dXcVbWu-e33pY2-fjlf8ZE968dpN_JA6pk6bQwcNopJQ4fir0DAo4bPs5PekgfF1li7hHLHl6eXlJWU9N1BlRSxHciDhubQOk7_iau-bgmRJg9hpwvmJn3bXq6o-V3BMVLE0UHcCJz0R3nsqD1lV_GqHTrYyxxSQJbysf-E7uDBjUyLY6C8RGgTjBtStRrky-WWQpQBQRbmmT88dOVQK7_zcoRkW3qlCE-FB45RXAv-1HeoWvmsBuS3OD26s3Xiu9MnJxYZ0bDvbhxk_4rYk9j8lmO08aEatoLWhdwOoxYSqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29866" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29863">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgQlrBIwwcDBPkMjjYU0evMMTC7xcVozUccuq3CxRspAO66h_tEG9TpjTM7J_STPnVX9wHj0v-Lz_2j_RYOGxTtQMhCDPS7soRCeHKrhVBhNQQ6SWGtUfkzecPKrXJhK0-md2WvrvZDa0oep1sZ88h336MYxQFuKaZL9xSod3wi5t1coYqzyivNE1nl4vRkN7WR-7XKFogkg7WmmVgdUIQ-vbNYGumxvaDs_zsQu8iaFTXLlrVs-ERdDmrZzNpPIJ9F8zeJSHTGacgl-4hQc73M2LEuAdZQQ7_G7g-DLi0YYSkvbLJlvQWLMku77pLN8rnDQkPyfx0exx6771lPxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراکتوری‌هایی که در پایان فصل قرار دادشون به پایان میرسه:
علیرضا بیرانوند، شجاع خلیل زاده، محمد نادری، کریم آذر، دانیال اسماعیلی فر، صادق محرمی، مهدی شیری، اودیل خامربکوف، تیبور هالیلویچ، مهدی حسینی، مهدی ترابی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29863" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29861">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSuQtdJW5qJHu70QacDAN2_f04Qd69wKlvulF8_jcl_dpUFDQN7QyYuxWSWJnYdn6qGCCttCXy98GlslxPe8zoE5a0HPshMf9V3sC52Nr7_uCjZwquq8so--G2OOZzEfGukbEFRtXOHiK1Einl6inA2VREljS4XOBOi3uSuTQIU4_976-2YmOIZrjkjMZqoykBoncgl7Mw7b7RXSaRZ5Tjf9OODVLQhuRVVS3dqa0bbeeumr7sr7OroMVjbHu3pjG2zWQbFd4uVhXKX3Puaej1VQ2H1SaTUKkT6vPQoks7UGfus7GTiiELSDXIqfvD71RSBsOcqRfvtbZ9A9hGJ_3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه:
محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29861" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29860">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYj9pWmNUUazR-9brntKXtKD-hAUYFFYQBQnUijbLBJytJKaIfhyny5XkFGBBPYgj9MrJSDEygiVLSpdBXFAzip_sT1yO0x1u9tMuGXmWgpvaxQOMcsWWVAgQ4ZwRVByRgJ8f7WeOX5c5Q1AeUpsXI-c46MPukcW0fV5y9NTX-DnTOaXDLSwEmJUaJN6haHyTXGJ4xgXTbXqVjtdH8YNPJNeubkapckGfY_3f5hxAsJJqQyDH9NVZoSxEBhOkY4zH6woCacKQ2qL7SEKwDFaNGxQe0K03e8zo09q9oRywenIMP0Wpwm7m2_8XLXZ30k7vDafMFCk2ac6nVnGCZcTUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29860" target="_blank">📅 12:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29858">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toWQTXsehjnmkAz_bp_f6c3bg8sn4FmnboWxr1YcywLe7W1-Xrx5T0kNZEppbPEeYa_WBmVrD1awXP9rO8gAVey7V-LKFavxOKq7JK7eKuS5LXu8nXJM2gTxmiwISE6AiQCX1OkKSNWrGb2EPkveoYG-fA_2QZ3axGjxvDkzLMrnTvoMd8wLuQpv5pvFx8O-mu4ojHhMCtmiLDMQxk4gCAReyqblINJHviU6PJ0j4Gk_Oodu3YBBLnGHUCQCQJKlea1BwA0NpRyeZh8Y63f4SrHVQBwa4LwTGFrOKYHL3yJfa7N05w2cO_hllK0Q0_ALqiCGt_j817qQyIJbR056ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه:
پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه. بقیه‌فعلاحرفی نزدن باهاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29858" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29857">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP7oLSi5PKfa1Aji0l2EPBnHKzYd-3ogWTgLSgH9yvqUkVCR4E1y-hIR53_y8WI-lNHpjUhbCKdwXahHctDm8SRJbr3oHE1Vfmo9bgk2VS-3fuLl0rGcFZnK9lL-3hnLdl-UHLP1MgSXWgq-aHBnG-_8IFpPHXJDC2nmfJd0vNbaSCg10phfYX4NxMOrwowHa9moRKstKEfgZiQZLoVsbUHdWPZVaykIvQwy5k2vNDO5EgPG6BETTLJvxFKoeO2BSK47iQw406qDIhcQSh6XZO1qSZLhmgbuYWKOd4aIMrmhVPfH2awqIWbkUXaJLb3of5ZDP2s2r4ib0ixQHUduPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
فابیان روییز ستاره PSG
: اگه توپ طلا رو براساس‌تعدادجام‌درسال و بازی جوانمردانه میدهند خب‌قطعاهیشکی شایسته‌تر از من پیدا نمیشه. تموم جام‌های‌سال2026 روبردم. تو زمین‌هم‌همیشه سعی کردم آدم‌آرومی‌باشم و بابازیکنان‌حریف درگیر نشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29857" target="_blank">📅 11:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29856">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7IexE4fKUpBOGvw-uL8PVeV4NyWxbUjxMNMfqv58fMiFGqeXWir-7Zx9-ICfs4spjRkhumJNSOMI7ZnFO3L0K89nm7qeYBFf_jHzVwDBUahLh8LdnYChiOA04OulkVcshWFKCZ9IKpyatkWULQWANLBAvTutHiDox4MVVgc8H5pfjqkZ6XLtHMRjdU9hqjwzh7S6jy10ezn4SUpClM9MtOYddtG6RUh2r3JJ6NBniWn4Rfx0-Ob2TFJYLxsOIGzich3UrtZektH7Fb9DoL87uio-29j7FX2Uc475x0TcDmbEDIj_DkyWTAIHqIfopIF0j5GbA9Dt6wAtSHUnwuJ54-4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7IexE4fKUpBOGvw-uL8PVeV4NyWxbUjxMNMfqv58fMiFGqeXWir-7Zx9-ICfs4spjRkhumJNSOMI7ZnFO3L0K89nm7qeYBFf_jHzVwDBUahLh8LdnYChiOA04OulkVcshWFKCZ9IKpyatkWULQWANLBAvTutHiDox4MVVgc8H5pfjqkZ6XLtHMRjdU9hqjwzh7S6jy10ezn4SUpClM9MtOYddtG6RUh2r3JJ6NBniWn4Rfx0-Ob2TFJYLxsOIGzich3UrtZektH7Fb9DoL87uio-29j7FX2Uc475x0TcDmbEDIj_DkyWTAIHqIfopIF0j5GbA9Dt6wAtSHUnwuJ54-4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
⚫️
آنالیزدقیق‌بازی‌استقلالِ‌سهراب بختیاری زاده مقابل تیم السد قطر در هفته اول لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29856" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29855">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUDCBv-CcTWrkS4PgHeqFlU7kzUj0QU7GyQmpeg-wmFbbIn4p8KNPec1XUWap5U0nKdMh1PrqYpk-EBEXPpdOohKNbtNyHA0-mZWF1uj3lzmNm9xw89lHPxXHyZqWonGEATSirAWOE-FArGTE914HFnhQqNGC_7ej5_vBPppNOWvyGYZokDJ0AciOYzvricbpT0dZVXNqqSR2YFHvmUZi1SX5-gVCSsRn8l30X-CGiFNE-K_9sDqn0fJSn-tTPzuslpWzTjIGtKUwJIrSPUZbKkYDi-H99BqjNYsImv9dOFJ_Ktn2j3OmmkVK-BNqx_8SaW5zFAoO_-O7Oi-P2nmMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه اتلتیک: به احتمال زیاد جیجی گابریل ستاره 15 ساله منچستریونایتد طی روزهای آینده با عقدقراردادی10ساله به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29855" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29854">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU70CIbYF-jb5_379IDcPVx76x7_4fKRWCvVIjrbhS-tKBFaaCMsp2JZSJAY1GQOgYxH4XgwAxS9HE8cdHaXyXWIKjePVEBO7PWCq4MPQOuqwwgW8pol-_vyWCteyeeJXhhdEXYISbeACvV0k05zcPJTToOuU0cn-sIJ5F-Z2XSniT494Dhs41VXEt3sQ0OasiS2A2WbzE-JfSKxXOR3rWTBqSeBCei3oIYEskOE4M3reo-FifYmsEaGkhY8_ZWIi_j5krGqzS-7N4G2JYCnTSTEovugcIKRnxkYMGIORWW6nVRR-vgcUpF7V4Yo_mB1rP4m6cdRW5QW4_OZ8tQtB2aE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU70CIbYF-jb5_379IDcPVx76x7_4fKRWCvVIjrbhS-tKBFaaCMsp2JZSJAY1GQOgYxH4XgwAxS9HE8cdHaXyXWIKjePVEBO7PWCq4MPQOuqwwgW8pol-_vyWCteyeeJXhhdEXYISbeACvV0k05zcPJTToOuU0cn-sIJ5F-Z2XSniT494Dhs41VXEt3sQ0OasiS2A2WbzE-JfSKxXOR3rWTBqSeBCei3oIYEskOE4M3reo-FifYmsEaGkhY8_ZWIi_j5krGqzS-7N4G2JYCnTSTEovugcIKRnxkYMGIORWW6nVRR-vgcUpF7V4Yo_mB1rP4m6cdRW5QW4_OZ8tQtB2aE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌دیدارجذاب امروز صبح دو تیم امید ایران و امید امارات در مسابقات آسیا که با برتری سه بر یک ملی پوشان ایرانی به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29854" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29853">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/29853" target="_blank">📅 02:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29852">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=cUKrN_a4zaq34HkhTfNTYyagB48zUosHYpgToWoYD2NQJwfC7rT0G8H7Bun-L8WMD4Tz_Y5JiNzhLT6mjGKWYewrLi8LXeLtG8AqR5nqMf9hbUAhjeqzey53hlt66OyBpkvSKvyvMp270bhlVPASCmdXl2KBe-jqE43JtfReo2OkslZneUH7Kx_p5Lz02VrLKYJZImt9c0kwyM-cjyI4CUGuqJk3djbYknt3cMN6DgatVaalG9v8KNjCvsfwTWxJ7u5mfhL-pcw4p2fvmkt6pK6xxWxrP0pjy0adY9lEOjRyHgakXYNGdy_Q0NwhhLQKB4_FUhNBFvIp_cNH67Y01Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=cUKrN_a4zaq34HkhTfNTYyagB48zUosHYpgToWoYD2NQJwfC7rT0G8H7Bun-L8WMD4Tz_Y5JiNzhLT6mjGKWYewrLi8LXeLtG8AqR5nqMf9hbUAhjeqzey53hlt66OyBpkvSKvyvMp270bhlVPASCmdXl2KBe-jqE43JtfReo2OkslZneUH7Kx_p5Lz02VrLKYJZImt9c0kwyM-cjyI4CUGuqJk3djbYknt3cMN6DgatVaalG9v8KNjCvsfwTWxJ7u5mfhL-pcw4p2fvmkt6pK6xxWxrP0pjy0adY9lEOjRyHgakXYNGdy_Q0NwhhLQKB4_FUhNBFvIp_cNH67Y01Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛ صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/29852" target="_blank">📅 01:59 · 25 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
