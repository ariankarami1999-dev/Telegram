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
<img src="https://cdn4.telesco.pe/file/CuxB3qD4xcgHGfh9il3yleb8r4qprPRdstAxFEKMFU6nUIdMaduQ_P0BOXdBsSUbhVjoxD7z28pMcZdibA4r8DkDVDqD_rLxBhk414aooVXjYx5n9ZyPtZnwI8pOwfn1qVmii215wahAXn3W23EExHrEFsxycs4E1fOyllr8u0K9zi-FhTULhZYXm2i9Z5ifN0gFVuPxPUeol_9gJYj9223brwghBx3Pis2a7nkOagIPAiNPlt4bTvB1S-4vG91zQnnSMucfiv6G8072OO7TrLQh7y_nop16VRj-ZzzYAx5hhexaU_5ICgclpHYKvJY1fT1FeVbENIxWd6dojW7GLw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 948K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
<hr>

<div class="tg-post" id="msg-147938">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/147938" target="_blank">📅 21:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147937">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
بر اساس گزارش شبکه خبری ای‌بی‌سی، سام آلتمن، مدیرعامل اوپن ‌اِی آی، و جنسن هوانگ، مدیرعامل انویدیا، قصد دارند هفته آینده در یک شام رسمی با اهمیت بالا در کاخ سفید در کنار شی جین‌پینگ، رئیس‌جمهور چین، حضور یابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/147937" target="_blank">📅 21:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147936">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما به دلیل حمایت از دولت ایران، پلتفرم معاملاتی ارزهای دیجیتال بیت‌بانک را تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147936" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147935">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
وزارت امور خارجه ایالات متحده فروش احتمالی ۴۸ فروند جنگنده F-35 لایتنینگ ۲ به ارزش ۲۴.۳ میلیارد دلار به عربستان سعودی را تأیید کرده است که نخستین خرید این هواپیمای پیشرفته توسط این پادشاهی محسوب می‌شود.
🔴
این بسته شامل ۴۸ فروند F-35، ۴۹ موتور پرات اند ویتنی، تجهیزات ارتباطات، قطعات یدکی و حمایت‌های اضافی است.
🔴
وزارت امور خارجه به صورت رسمی کنگره را از پیشنهاد این فروش مطلع کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/147935" target="_blank">📅 21:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147934">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران: «صحبت‌های ترامپ درباره حمله به ایران، به اعتقاد من تلاشی برای زمینه‌سازی جهت مذاکره با ایران است؛ چرا که این موضع‌گیری‌ها بلافاصله پس از سفر عراقچی به پکن مطرح شد. همچنین تماس تلفنی میان وزرای خارجه چین و آمریکا نشان می‌دهد که چین در حال سنجش تمایل ایران و واشینگتن نسبت به هرگونه اقدام چین برای حل‌وفصل اختلافات میان آن‌هاست، و ایران نیز در جستجوی کسی است که تضمین‌های لازم را ارائه دهد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/147934" target="_blank">📅 21:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147933">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0vblWBb9mKSuCVsNJpNVLpOVSoghTc4Ws3twTTvGLFsC0fUL_3HcTP1M5gj6B4IhITh31xlu6XSs8ri1qPKSKoLg48Y52j7A-n3h7VHzm1CseLzQUN5lFp38TTS7uqo1_viJQAHLNPB9CFxJURYWtthqNdhCgdof0TcrVSfWww05yZr4OT3NaisoUHhEBhd3MKl8h2u1iBvWpNfnqAJl9EUGUD3Yj53vS-TiUoJQrM3KaKSBztVWboZ_jzUQPMI3UN-sV62rH06qa6vLmVRal78ucuhH2ie1ZVbK1VAvptmIxE7_FtMSqExmCng-M66WXLrtog6zcwXcDhYjztTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ درباره لهستان: اخبار عالی! به لیدرهایی جسورانه از سوی دوست من، کارول ناوورکی، رئیس‌جمهور لهستان، پیشرفت‌های چشمگیری در جهت ایجاد پایگاه ارتش ایالات متحده در لهستان حاصل شده است.
🔴
اگر این اتفاق بیفتد، مکان آن به‌زودی اعلام خواهد شد. این یک گام تاریخی برای اتحاد بزرگ ایالات متحده/لهستان ما خواهد بود. از توجه شما به این موضوع سپاسگزارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/147933" target="_blank">📅 21:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147932">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fh9I2fD2Y337GWuMzfBrWGxkR-JOfUwLufvOMsfqPsefa0dvcF7NhwpfbThz98_ziZhs9Lsv5MWqTWcraqouJSB2KCNzEhqFQLTJE_ffZFTfAVMXuh28pl0dwAxl1wNNzvNq7qY0v1b9daP7jA_z3GcGjRs4VwTZmp-rxG-xr7xfQMVAYq25dvq8kpNGh2Nox6kPKnmnxBuZo5vDSZ183hmNJuHvng7EBedlPoIJCKXx3mjtSYOyigvNfypDVZvNEL5bvLRrReQjo-MqeoChUxco1_LRA04OLktjDVDQUN9_EsJWqk6JLL-Wbdq3zu_oZoCfpTm4NewFoTjTahQF3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba25b1275.mp4?token=fh9I2fD2Y337GWuMzfBrWGxkR-JOfUwLufvOMsfqPsefa0dvcF7NhwpfbThz98_ziZhs9Lsv5MWqTWcraqouJSB2KCNzEhqFQLTJE_ffZFTfAVMXuh28pl0dwAxl1wNNzvNq7qY0v1b9daP7jA_z3GcGjRs4VwTZmp-rxG-xr7xfQMVAYq25dvq8kpNGh2Nox6kPKnmnxBuZo5vDSZ183hmNJuHvng7EBedlPoIJCKXx3mjtSYOyigvNfypDVZvNEL5bvLRrReQjo-MqeoChUxco1_LRA04OLktjDVDQUN9_EsJWqk6JLL-Wbdq3zu_oZoCfpTm4NewFoTjTahQF3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فارس: کالابرگ ۳۰۰هزار زیاد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147932" target="_blank">📅 21:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147930">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMwUfgCjxlsS0SU329S-pPX61Mc198UxXbfmGeVp9DIFrb6J2EOGypbayhItf6XM81jV18ecewraAVduQSvCteYV5xlBSE5tGb_wjLkOHDKxrQiUfBNrlrxHcsvu8FF9LB3laP3-3yQJoznXUfFpkQasdS0m7KUwhIcg0Po_b2M52OZcMi7uCMBPoWbTQzY3Rj7BOLJNnbPyP3C3JfbYd6hiE07tFWe61s3c-xT-Ri7S9X41-YkolfY3XUH2YsJupVAetUgs-E2Ur347kucrjiQve6WSVQLTOlG-oaZbUnkpyyaxkSVA5sEfgjKNK10Uq6XX_pW-X3DIdlz0rNtQ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=IaKdsoPjdkXgtfOLi1ZFLbht7bDexp7M7pnpmBv2yROe7xTqYUk0OvnkRdM-sDuy897Rm09iRKdA6rKDylfBuLdgLT7fJPN4oaNv2GQ8ltYoCDqvwGMqbkagGdKVNG6tS8s5t0OtBhHGCP0QpOywa2xCm7eN0mX7Ot8Wv2wzAIcaO243z61SK4WLRpdU1p_ndCwkM5Pt-nf6SW__ClxcPDVdiUFfyyLHZ1JOvgmIkzgucTh4QZbpoDNtfzm90RtlRknUex46VhOVvaYe4p3p0FDuVVtKIkLODqALEpYp4VUq3y64ylPNpabAvLYKluHoITGpcyRSsIOvpmL50tNugg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef55f0b0ff.mp4?token=IaKdsoPjdkXgtfOLi1ZFLbht7bDexp7M7pnpmBv2yROe7xTqYUk0OvnkRdM-sDuy897Rm09iRKdA6rKDylfBuLdgLT7fJPN4oaNv2GQ8ltYoCDqvwGMqbkagGdKVNG6tS8s5t0OtBhHGCP0QpOywa2xCm7eN0mX7Ot8Wv2wzAIcaO243z61SK4WLRpdU1p_ndCwkM5Pt-nf6SW__ClxcPDVdiUFfyyLHZ1JOvgmIkzgucTh4QZbpoDNtfzm90RtlRknUex46VhOVvaYe4p3p0FDuVVtKIkLODqALEpYp4VUq3y64ylPNpabAvLYKluHoITGpcyRSsIOvpmL50tNugg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات سنگین اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/147930" target="_blank">📅 21:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147929">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
تا ماه بعد وضعیت طلا چجوریه؟</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/147929" target="_blank">📅 21:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147928">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
آکسیوس: ترامپ دستور داد سطح نیروهای فعلی در خاورمیانه تا پایان سال برای احتمال از سرگیری درگیری‌ها حفظ شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/147928" target="_blank">📅 21:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147927">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وزیر دفاع پاکستان، خواجه آصف:
حتی اگر هیچ توافق‌نامه‌ای وجود نداشته باشد، اگر عربستان حمله شود — به‌ویژه مکان‌های مقدس ما — ما به موجب یک توافق ابدی موظف به محافظت از آن‌ها هستیم.
🔴
خانه خدا و مدینه منوره — محافظت از آن‌ها وظیفه دینی ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/147927" target="_blank">📅 20:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147926">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=d3ykdmfyLoZxrsybuGGB2rE1w-SGZRssnMIf8mJCTqJtp_05v3kExMbh2SUPxMy8A0TCBXJ2rLYYzl7phSxLK2feo2XvzKDLd23Vczy8SAZkl98QA8FBL-4fCrVmxJGnuVHRgYVaZx9HjiJh8bvBCLOVD89bRQQkA8Hmbl6yN6LYRC1eoVonA_h4a6VA_PQlHiiavXkc4WVf7WE4psGdEoeTJKmw_d8kPfEGmEYHP30KIUIoVl8AbravNIUSu8LSLEPZIQ2ijlVkfqNuzqe2sOe7Xu7UGac0gsSLXdufJ9o_8CF-HOazZ7mluT1h2UiHkN-zznAMLhZgifZDp2_EhBQsRAJKreovaRLJ2JpRuuoCjcr8tmySYGIg7eDa8lz1wNI4rvR5UmoZIOp6xNHXFmEG7HrNg8Hb83kDm05VSAj0Zey8mZazOtSaG14havz7qS_Nee25LsIa79GOhsOjo1iMbiC89yQmSNrki7cV3aJTiWyDDN3omcE4MgH0xNy_LhAx1mTnj6EKelkP8W45gL2jogLuWbbFH6tiOiujnNtXxqZZr3-bm3vgBillXH-vD2rTCN6qMlvt66RG3uTn25TfbNuDCniKWLm6vGx8OntRNHtyIIovkaHujJnSERUSHfeC5hjqbggXCK_80HakEKiWvGgbjFiPsLaZKK3GYF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb984ea71a.mp4?token=d3ykdmfyLoZxrsybuGGB2rE1w-SGZRssnMIf8mJCTqJtp_05v3kExMbh2SUPxMy8A0TCBXJ2rLYYzl7phSxLK2feo2XvzKDLd23Vczy8SAZkl98QA8FBL-4fCrVmxJGnuVHRgYVaZx9HjiJh8bvBCLOVD89bRQQkA8Hmbl6yN6LYRC1eoVonA_h4a6VA_PQlHiiavXkc4WVf7WE4psGdEoeTJKmw_d8kPfEGmEYHP30KIUIoVl8AbravNIUSu8LSLEPZIQ2ijlVkfqNuzqe2sOe7Xu7UGac0gsSLXdufJ9o_8CF-HOazZ7mluT1h2UiHkN-zznAMLhZgifZDp2_EhBQsRAJKreovaRLJ2JpRuuoCjcr8tmySYGIg7eDa8lz1wNI4rvR5UmoZIOp6xNHXFmEG7HrNg8Hb83kDm05VSAj0Zey8mZazOtSaG14havz7qS_Nee25LsIa79GOhsOjo1iMbiC89yQmSNrki7cV3aJTiWyDDN3omcE4MgH0xNy_LhAx1mTnj6EKelkP8W45gL2jogLuWbbFH6tiOiujnNtXxqZZr3-bm3vgBillXH-vD2rTCN6qMlvt66RG3uTn25TfbNuDCniKWLm6vGx8OntRNHtyIIovkaHujJnSERUSHfeC5hjqbggXCK_80HakEKiWvGgbjFiPsLaZKK3GYF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس ستاد مشترک ارتش آمریکا:دشمنان ما در حال یادگیری از جنگ‌های ما و به چالش کشیدن برتری‌های ما هستند
🔴
دشمنان ما ممکن است از نظر جغرافیایی پراکنده و دور از هم باشند، اما به شکلی فزاینده با یکدیگر در ارتباط هستند.
🔴
آن‌ها فناوری، اطلاعات، تسلیحات و حمایت‌ های اقتصادی را با هم به اشتراک می‌گذارند.
🔴
آن‌ها میدان‌های نبرد گذشته و کنونی ما را مطالعه می‌کنند، به سرعت خود را با شرایط تطبیق می‌دهند و در پی یافتن راه‌های جدیدی برای به چالش کشیدن برتری‌های ما هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/147926" target="_blank">📅 20:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147925">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها در تماس مستقیم با ما هستن و همچنان خواهان دستیابی به توافقن
🔴
می‌خواهم از جلسه عمومی سازمان ملل (هفته بعد) استفاده کنم تا مستقیماً از متحدان منطقه‌ای درباره گام‌های بعدی جنگ بشنوم
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/147925" target="_blank">📅 20:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147924">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/147924" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147923">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
فوری/ ترامپ: به جایی که باید درباره ازسرگیری حملات گسترده به ایران تصمیم بگیرم، نزدیک هستم
🔴
هر اتفاقی ممکن است بیفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/alonews/147923" target="_blank">📅 20:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147922">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / دونالد ترامپ: قرار است تصمیم مهمی در مورد ایران بگیرم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/147922" target="_blank">📅 20:31 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147921">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=QnEMG5eG6ZvR0UZOArOTpoWC89q6KQJgYdwYjHUskW1y9o9eic-D8U__SB372bOxpbff-qtVkakHGaGTuAHITKRN-NDYzbCZeahPXpfvad4K5ftgAtBzwy1-v1P1YpbQTZk8oxJYGeG0gIMzOZPpJrOEJpVUSiNcoB-mpkT9WFgb0e_8bsCqmhM8BEL02doyStatJby-uj0g-aUa10H1wps_ZspvC4-jqRVv74d-HdCoDCT5GtlOMA9qEtfpkQH8Bfv1qW0GI3pttSqIOMriIsYo4N7j7HA0uwfdgXUIwI6mPuOcX_HZtdrdqyQWCxdkpuQ4-AElLEshq_INe3YQ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed64f0a840.mp4?token=QnEMG5eG6ZvR0UZOArOTpoWC89q6KQJgYdwYjHUskW1y9o9eic-D8U__SB372bOxpbff-qtVkakHGaGTuAHITKRN-NDYzbCZeahPXpfvad4K5ftgAtBzwy1-v1P1YpbQTZk8oxJYGeG0gIMzOZPpJrOEJpVUSiNcoB-mpkT9WFgb0e_8bsCqmhM8BEL02doyStatJby-uj0g-aUa10H1wps_ZspvC4-jqRVv74d-HdCoDCT5GtlOMA9qEtfpkQH8Bfv1qW0GI3pttSqIOMriIsYo4N7j7HA0uwfdgXUIwI6mPuOcX_HZtdrdqyQWCxdkpuQ4-AElLEshq_INe3YQ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نمایش بمب‌های سنگرشکن برای تهدید ایران در گزارش خبرنگار فاکس‌نیوز
🔴
خبرنگار فاکس نیوز: آنچه الان می‌بینید، یک بمب سنگرشکن GBU-31 ویکتور ۴ است. ما در یکی از انبارهای مهمات ناو هواپیمابر جورج واشنگتن هستیم و همان‌طور که می‌بینید، انواع مختلفی از تسلیحات در اینجا وجود دارد؛ از جمله موشک‌ها و بمب‌های گوناگون
🔴
در انتهای این بخش هم انواع دیگری از بمب‌ها را می‌بینید. این‌ها بمب‌های ۲٬۰۰۰ پوندی هستند. باز هم تأکید می‌کنم، تمام این تسلیحات در صورتی مورد استفاده قرار خواهند گرفت که رئیس‌جمهور دستور حملات بیشتری علیه حکومت ایران صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/147921" target="_blank">📅 20:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147920">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9225e42d16.mp4?token=WIY5qzE10K2g7iPWyou9WnFwdhM5qyweRZAZBwxRvfqjXAHifZ4KLtFJSYsCo2hrYRm1s9CyDInKne2RWyCMmIif6zL8MCZdl2Nmx4jT0ophcvDdWckNOaFJDn7h6wXXRgc4p22P0AXs9m1edH7d66gKdImuvITCNJJ_oeOA9Xiw2HVnCHDF0kVcCJtaOJjgcIibZaXLUV5yPx8gkTyHBo5jQg-dPKKlQb2CWd87Ax6UUzGQDREOE7uQ1HRny89KTtEdR0gPVgbX2Ks-XPPnFeDm2tezD0sua95CHs7PD_9spIxiL-yn0l9WaR6YAHk6ywoTVOvNhI7TzRZL1Q51hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9225e42d16.mp4?token=WIY5qzE10K2g7iPWyou9WnFwdhM5qyweRZAZBwxRvfqjXAHifZ4KLtFJSYsCo2hrYRm1s9CyDInKne2RWyCMmIif6zL8MCZdl2Nmx4jT0ophcvDdWckNOaFJDn7h6wXXRgc4p22P0AXs9m1edH7d66gKdImuvITCNJJ_oeOA9Xiw2HVnCHDF0kVcCJtaOJjgcIibZaXLUV5yPx8gkTyHBo5jQg-dPKKlQb2CWd87Ax6UUzGQDREOE7uQ1HRny89KTtEdR0gPVgbX2Ks-XPPnFeDm2tezD0sua95CHs7PD_9spIxiL-yn0l9WaR6YAHk6ywoTVOvNhI7TzRZL1Q51hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اسرائیل و یونان یک مانور دریایی مشترک برگزار کردند که شامل تبادل خدمه و آموزش برای سناریوهای مختلف مانند «موقعیت‌های اضطراری» بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/147920" target="_blank">📅 20:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147919">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16578a4b94.mp4?token=NvwuO87D8TS2_MqQXULfJFpdboEZtVAobK9cJqcggfZVA-EK5HVXZQT-MQIwKKOyAlVpFLf62H_7tBO-VyakYH6195sydauFQeqaVJMQ1chVScPOcJF1SR5waV3LqhmfeAajGjYFABH8aIxB9bmYEQnrz-PIQMQGWfGAmrkCGoCln2BPtRzjqvXjKptV9D1xKWpTNI5XrYs7LM4QF7vfYkgasR6KiYFw95ncrJDaJ4gxCYcTgiD_0SPDwDCW066zHms1h2JgB-QawxZoucCTLB2zEc6upeSk1gRpX7hN4yzeotjBLaNJfv2X0h52B3I1VDx7CKVw_Oufi5DsAa00lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16578a4b94.mp4?token=NvwuO87D8TS2_MqQXULfJFpdboEZtVAobK9cJqcggfZVA-EK5HVXZQT-MQIwKKOyAlVpFLf62H_7tBO-VyakYH6195sydauFQeqaVJMQ1chVScPOcJF1SR5waV3LqhmfeAajGjYFABH8aIxB9bmYEQnrz-PIQMQGWfGAmrkCGoCln2BPtRzjqvXjKptV9D1xKWpTNI5XrYs7LM4QF7vfYkgasR6KiYFw95ncrJDaJ4gxCYcTgiD_0SPDwDCW066zHms1h2JgB-QawxZoucCTLB2zEc6upeSk1gRpX7hN4yzeotjBLaNJfv2X0h52B3I1VDx7CKVw_Oufi5DsAa00lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: من خیلی باهوشم
🔴
رئیس‌جمهور آمریکا گفت: من آدمی با سطح هوش بسیار بالایی هستم اما در نهایت من فروتن هم هستم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/147919" target="_blank">📅 19:58 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147918">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy4dhSIJ4xXk6iBthVoFsjGck4TmKZJ2gbXGiQfOZVN_1uABX-1ZAfptDpwosmXykpubEDupKx9CtXoT_AJe6-ubGYUEZdoU-zRue5YSLvO8H9USfu7xSTthsXqr37v1kkBMPamIUn8q5VJKq8xcpJmUktMRTnpubZc-w0YLOg873SR7BIak_Qia7pL-2sJGFjyO9SEI-0FQ5JoNk8KIkwWyVVqGbGeG9-70erCtrBa-vb4OcYW_a6Qn1jnnrLZ3clu7LkRTf_rLTM0GMmJVOdGfM4Mfbq8HupclFz1KrBp5wmqA9P863Cp_pNrapwO0LT2-TM13EYf7kMfh8H9xpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محبی، سخنگوی سپاه خطاب به آمریکا :
شما روایت هالیوودی می‌سازید اما ما لاشه جنگندتون رو با فرغون جابجا می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/147918" target="_blank">📅 19:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147917">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سفیر آلمان به وزارت امور خارجه احضار شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/147917" target="_blank">📅 19:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147916">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SPyjcWgtyQMdVW7SyUmpJ165aetIzYb6Y-E97bh6GxQksT5pa2-pAnDJtHEw1aFIoecRD7uI8jGJoM5HbaJhfM56yGNaspZ8RTei8btTxqHHfCKpMFs8G6jryptREnVPUow9RvNaJymQ3pdnUqNtrGYi8YTGiO_uyRotOLq0iRg54FA5i0Zk5Tr9at2IsBe40CkQcMZQNILCy_MMCiv3G8P5q2hzBSL4X5XgVpw5JhslrRVnCmzLKP_HBy6CSmvzzntjww7v3b2J_CJrfUasyMVyO3M2mYRN3XYuMCN9V36NtPH3AAU4RfUwYwIutg8u_ou57OFrH6RY2EGWgvPRrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروی دریایی بریتانیا اعلام کرد گزارشی درباره وقوع یک حادثه در فاصله ۷۵ مایل دریایی شرق عدن در یمن دریافت کرده است.
🔴
بر اساس این گزارش، یک قایق اقدام به تعقیب یک نفتکش کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/147916" target="_blank">📅 19:46 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147915">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c065e013.mp4?token=VdKmtRgGvDzq9NE-hUsd21exWToBfayd2FZ0gyhCuaydJHXLK9KXchI3g_wUTU7QtFkalH4b0YbEPAH07p6o7ysXxfWl8udokXH3M_c5I9JybJqKfFcpkmrv2GaUsJn6dLUirna04ORmLQbgf_L5ZkgdWXFxkuiN_DQPVfFg_aSaw1LnOpRLl_NZmuPt7MdPQeuY_WL3yv7tcSpA69eg5NbNPUf3gn4NjXRqRGXX4mlOLtX2XHLbew-KB0wDP9ZJw5j_S6bXqDKPq_KXYYRA3i8ptCyl7pfXsuiptHCu2O0eQhUe4LKCAzr6WGga1c_V3kCzOAXvXAfmKRhcVD_uboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c065e013.mp4?token=VdKmtRgGvDzq9NE-hUsd21exWToBfayd2FZ0gyhCuaydJHXLK9KXchI3g_wUTU7QtFkalH4b0YbEPAH07p6o7ysXxfWl8udokXH3M_c5I9JybJqKfFcpkmrv2GaUsJn6dLUirna04ORmLQbgf_L5ZkgdWXFxkuiN_DQPVfFg_aSaw1LnOpRLl_NZmuPt7MdPQeuY_WL3yv7tcSpA69eg5NbNPUf3gn4NjXRqRGXX4mlOLtX2XHLbew-KB0wDP9ZJw5j_S6bXqDKPq_KXYYRA3i8ptCyl7pfXsuiptHCu2O0eQhUe4LKCAzr6WGga1c_V3kCzOAXvXAfmKRhcVD_uboWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده روسیه در شورای امنیت: عدم اجازه ورود رییس سازمان انرژی اتمی ایران و معاون اول رییس جمهور ایران به شورای حکام، نقض آشکار  قواعد بین المللی است
🔴
در سال 2025 تمامی قطعنامه های اسنپ‌بک ملغی شدند و دیگر امکان بازگشت به مکانیزم ماشه وجود ندارد.
🔴
از آمریکا و بقیه کشور های حاضر شورا می‌خواهیم دیگر تقابل با ایران را ادامه ندهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/147915" target="_blank">📅 19:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147914">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147914" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147913">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/igHlqLuvPXGhGVNVD42RUVSW76XHtf0CkDvkWYC5_Ed068ySzmrppDOuNu8paoDV6m1C00xAgWEOYS6XKt9oYwRP_C2W7VWAcHVjOc9FGO5N-iNiQ0I3d70pQEzaagaVk8uR3i5gku6e8xpypVSpwnI0pS5fPDLUKPPlow_1_UsU3MfaRoaT9akKK27FX0AG7FGmITaVkwNpwjfrDc-C6kLSxqR3AZPpPGrfMDOlySYGapdTRiUy-HIKWILrPb49qH2LTdyQWkxhfhsKGzQaTFZl3sL8Cn_qVBGuvdpdhEZGOekHmzRHBesG3xdmbcT0Aeq5RG-j1QHOU_udn8_gpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۹ جنگنده F-16 دیگر آمریکا دقایقی پیش از اروپا راهی خاورمیانه شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147913" target="_blank">📅 19:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d68625bb.mp4?token=Eom5oYkkns7YyaPlWpiT_NvpxyNRtXosMvMtgBnBb5UgGN_Q5swjxc7pzZNwDw4LkDR4aPagHwsaceDEJaJRWkDBuTU71WXs0dXeXD4Y8aBY7suWuuH9AgBju3gKGsUJH63DUDtF0DQWXVaT0V56TUKeLIWMAFohZtwHcC7L1CbI-bjePCiJx0sdaLx7Zw1ol3eh4KZ_JDC4nZKOjHT4KPtNtVsS85GYiqvBekNT3OylC7Yva0MG4JWk_31eC6dzwToXDg_NtgQVOi6Q5siC0g116xhIDbG9O8wh4tv4Iby_vBj1lmpT2ol-sfnu2sMAOn2YV3NAYsO7OcairadWFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d68625bb.mp4?token=Eom5oYkkns7YyaPlWpiT_NvpxyNRtXosMvMtgBnBb5UgGN_Q5swjxc7pzZNwDw4LkDR4aPagHwsaceDEJaJRWkDBuTU71WXs0dXeXD4Y8aBY7suWuuH9AgBju3gKGsUJH63DUDtF0DQWXVaT0V56TUKeLIWMAFohZtwHcC7L1CbI-bjePCiJx0sdaLx7Zw1ol3eh4KZ_JDC4nZKOjHT4KPtNtVsS85GYiqvBekNT3OylC7Yva0MG4JWk_31eC6dzwToXDg_NtgQVOi6Q5siC0g116xhIDbG9O8wh4tv4Iby_vBj1lmpT2ol-sfnu2sMAOn2YV3NAYsO7OcairadWFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای جدید نشان می دهد انصارالله در حال تقویت مواضع زمینی و سنگربندی در کوه های اطراف تنگه باب المندب  برای دفاع در برابر ضدحمله احتمالی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147912" target="_blank">📅 19:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) روز پنجشنبه ۲۶ شهریور، اعلام کرد که ارتش آمریکا در راستای اجرای محاصره دریایی و تضمین رعایت قوانین، تاکنون در مجموع به ۱۰۴ کشتی که در تلاش برای نقض این محاصره بودند، دستور تغییر مسیر داده است.
🔴
سخنگوی سنتکام روز گذشته با تاکید بر اینکه خطوط کشتیرانی اصلی در تنگه هرمز پس از پایان عملیات مین‌روبی همچنان باز و امن هستند، این محاصره دریایی را «آهنین» و کاملا موثر توصیف کرد.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/147911" target="_blank">📅 19:23 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98b6b9d143.mp4?token=MMmfBQjLdMF9OjVBAHK5hYioTVZlinijYMZXVCfGxykKLrDTIexP88Vqy-wwjuefzC0FJEMy25kP_Ad_b6yBcULxDa3Rq-YYXcddv5KJx0K0wvD-xTh1tdWWZJwz9wYg4wMqMbEpwX3iOsMfqa6sOMqTjTsDuFOYkpjtE224tSDjd3Lpl5nhjn7tzcRvOzlZZ9Epn15e_HIvz8fYhsdeRJFHH0Qpb3wy-Xp8UOk0H3V2bhmtFZ_khh-akMpr_TI9M5OV2bLX1Vr38aKRExx04t6Yax0_NQOaHaLwp3kRVAuH02bE_kWVUOoPoaYUntHMbeT0Eu7ZwCqHl01J7eBY3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98b6b9d143.mp4?token=MMmfBQjLdMF9OjVBAHK5hYioTVZlinijYMZXVCfGxykKLrDTIexP88Vqy-wwjuefzC0FJEMy25kP_Ad_b6yBcULxDa3Rq-YYXcddv5KJx0K0wvD-xTh1tdWWZJwz9wYg4wMqMbEpwX3iOsMfqa6sOMqTjTsDuFOYkpjtE224tSDjd3Lpl5nhjn7tzcRvOzlZZ9Epn15e_HIvz8fYhsdeRJFHH0Qpb3wy-Xp8UOk0H3V2bhmtFZ_khh-akMpr_TI9M5OV2bLX1Vr38aKRExx04t6Yax0_NQOaHaLwp3kRVAuH02bE_kWVUOoPoaYUntHMbeT0Eu7ZwCqHl01J7eBY3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از وقوع بهمن عظیمی که گروهی از کوهنوردان را در ارتفاعات قفقاز مابین روسیه و گرجستان گرفتار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/147910" target="_blank">📅 19:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoqZmIlcgALiEHr6eveMizyMXOPZnobZqsB8ZTekMt1yrnsf-dbL7rcm0i-Vo9Yan1hnWk4F-XbqVX5m-vS7tQXkoUvi39MKqFLnX15q4ALQj0D3Pn58Heaz2mvAY9q5vYkwBRt43BuWnBZO_4gvFwOZAhPTxJLvw4csTxwRjQjKvNy2Ch6kh161Gevhsz0NbjJ5_jznMF3rBcGLQKSdiD31YMA-KloLRtYwIKmaUMbSD013ia37FQfS-7n3tV9TS7gAW5J1j8jmXkIFIG_u0xylSQVe5vrjbIqL23a6AqUagLhzu_vtH7EyNQdXZ4wtmOg7uWbpGPjshrEvF-GkJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هیئت حقیقت یاب سازمان ملل:
آمریکا در حمله به میناب و لامرد مرتکب جنایت جنگی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/147909" target="_blank">📅 19:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
هشداری فوری جامعه «باستان‌شناسی» خطاب به رییس‌جمهور: تخت جمشید را فوری نجات دهید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/147908" target="_blank">📅 19:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7c82a08a4a.mp4?token=lYn2939tLmPqersVxi2Jx7KDdwQKftniEiuh18mdGvvv6NCGf-sMPDu6BK8I2MOf8TnyIEmOpoY7ACtuiBAT3pxvIvP_7_F7XFfgIPllev46EdzilKyaT1kXjGgiiT_wit8Fgh_vfkVJj_T5_NdB16S3hSOoMtl0zWRpYdqEIA9am-41dT8KPft9NVdo_ET6gJubq-NQg4e9a19ALNrDbJF5l55DBkWnuCUqiTLNbdbz2q4SPsteJYuSzQcm9FxoOmnXIIwYDDAS0NiRKjOYWB6CU9zIxryXhDnuGkcgYuLWL8PT5V0egIw7TXCLUErNYozOE2ugYhWO5QIyCx0ruolUCFRZicbaoUG7xoYub4hjPJAr28cQhXqgHrlySRy8XciU0cW7pmJQmHkmgIF2EfbkiKiomFTbq1IMfB8od5jaCuuoQnhp9O5SXaJuW1WdhAUyMnQ63xRBbwf6THfiUpSODOgNp9hMfIkt1H-eJeW-HurMQgJ4BFO4lGHBEcAFDnr17OcfUX_Lq1Vl-uryZuWxVjaDyjHaF_bBuCwAftW3WWogwk_SINghyZSRST5goPhi47vW1T0a8VE6uiL6NPFWSnm7UoI6FszD3fcngmqWsK5YEL8NBljpJ-B-4Qnwyj5b0aeIb6G_7_Ubc_p6mjP8Ldbx4xydKinn31NydIM" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7c82a08a4a.mp4?token=lYn2939tLmPqersVxi2Jx7KDdwQKftniEiuh18mdGvvv6NCGf-sMPDu6BK8I2MOf8TnyIEmOpoY7ACtuiBAT3pxvIvP_7_F7XFfgIPllev46EdzilKyaT1kXjGgiiT_wit8Fgh_vfkVJj_T5_NdB16S3hSOoMtl0zWRpYdqEIA9am-41dT8KPft9NVdo_ET6gJubq-NQg4e9a19ALNrDbJF5l55DBkWnuCUqiTLNbdbz2q4SPsteJYuSzQcm9FxoOmnXIIwYDDAS0NiRKjOYWB6CU9zIxryXhDnuGkcgYuLWL8PT5V0egIw7TXCLUErNYozOE2ugYhWO5QIyCx0ruolUCFRZicbaoUG7xoYub4hjPJAr28cQhXqgHrlySRy8XciU0cW7pmJQmHkmgIF2EfbkiKiomFTbq1IMfB8od5jaCuuoQnhp9O5SXaJuW1WdhAUyMnQ63xRBbwf6THfiUpSODOgNp9hMfIkt1H-eJeW-HurMQgJ4BFO4lGHBEcAFDnr17OcfUX_Lq1Vl-uryZuWxVjaDyjHaF_bBuCwAftW3WWogwk_SINghyZSRST5goPhi47vW1T0a8VE6uiL6NPFWSnm7UoI6FszD3fcngmqWsK5YEL8NBljpJ-B-4Qnwyj5b0aeIb6G_7_Ubc_p6mjP8Ldbx4xydKinn31NydIM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حیف و میل گازوئیل توسط قاچاقچیان در منطقه مرزی سیستان و بلوچستان!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/147907" target="_blank">📅 19:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53768ce3a2.mp4?token=R9Gc4e-Lfcf_zcGMhOZrDf_J0-2inKvFjnn1f6kv2vC4Eri5XBkpTLcizsCX7j3kgw2NVT81Vfe1p1Wo8Klv5dyf8hCWMPNdIrGwjau3CkCm2e5RJSL0ifsVDA2zjEnGlT1yv-bCqsP8Qx_2Up-A2udlaDIa0xUatM9UxfPdfNyK4opJSK7Bpg_CvRxZNgFOrRq6rCWHFMjMpcQPomXoXpzYwQZSfayWRv66ncu31i81xI8kEowXmSJbjLSIQ2UAD8JWFYgX6d6wsL082h8DXhET2-p-zpSK7mvo0NXUYLoZUa-LbDHz7J-AdkWvrVDZAbmaJEYGLHan7fbmBR3TpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53768ce3a2.mp4?token=R9Gc4e-Lfcf_zcGMhOZrDf_J0-2inKvFjnn1f6kv2vC4Eri5XBkpTLcizsCX7j3kgw2NVT81Vfe1p1Wo8Klv5dyf8hCWMPNdIrGwjau3CkCm2e5RJSL0ifsVDA2zjEnGlT1yv-bCqsP8Qx_2Up-A2udlaDIa0xUatM9UxfPdfNyK4opJSK7Bpg_CvRxZNgFOrRq6rCWHFMjMpcQPomXoXpzYwQZSfayWRv66ncu31i81xI8kEowXmSJbjLSIQ2UAD8JWFYgX6d6wsL082h8DXhET2-p-zpSK7mvo0NXUYLoZUa-LbDHz7J-AdkWvrVDZAbmaJEYGLHan7fbmBR3TpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گروه حوثی‌ها (انصارالله) یک پهپاد سعودی را در آسمان استان دمار در یمن سرنگون کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/147906" target="_blank">📅 18:54 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147905">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClgfSRNsCn84rfPGpzUb_mLHC3lwB9B-PrAHzNEk1rPtwnSciiEci23dzcMj4FMY2_DK0EQaHHRTZ70jCw3RRQfenrb6LdbbTqDiVKCnK_cjNpnMpulxSQQOkW_N_W-thd1e-Kdfo6da1obRhrFvaaTi290aSrFURJ0MZVRNNNNvizUhlFnZ2ANnYx6WUrIWEj5JtFl_HFP8Z8JJOrDirt29UMWUVh2JWVgmgnL40g3dJ7UsxLgZTG7C39f5IPJFVNaWR_cIRZn4V4CIvQv-OvWKpHBGFrJ3Nmy3U4Yu7eqmGNvk0PtRn5dAf88IqpkLzqiF5fRe6Sz4fy_FxufZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حرف حق پسر رئیس جمهور:
ملت جانفدا شبیه یمن، یارانه نقدی‌شان قطع بشه و از برق سراسری استفاده نکنند و هزینه زندگی‌شان را نصف کنند و به سفر نروند و از هیچ خودروی استفاده نکنند
🔴
نمی شود از یک طرف به خاطر اقتصاد ناله می‌کنید و از طرف دیگه میگید بزن توی دهان فلانی و فلانی
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147905" target="_blank">📅 18:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147904">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
عراقچی: از ابتکارات رئیس‌جمهور چین استقبال می‌کنیم
🔴
این ابتکارات در مقایسه با دیدگاه‌های غربی، با درک درست‌تری ارائه شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/147904" target="_blank">📅 18:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147903">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
الجزیره: روسیه و چین با استفاده از حق وتو در شورای امنیت، پیش‌نویس قطعنامه پیشنهادی آمریکا برای تمدید مأموریت تیم کمیته تحریم‌های ایران را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147903" target="_blank">📅 18:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147902">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در محدوده تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147902" target="_blank">📅 18:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147901">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
رو دلار و طلا سرمایه گذاری کردید؟
آره
✔️
نه
❌</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147901" target="_blank">📅 18:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147900">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ذوالقدر: تا به زیر کشیدن ترامپ و نتانیاهو، تنگهٔ هرمز رو نخواهیم گشود
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/147900" target="_blank">📅 18:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147899">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
الجزیره: روسیه و چین با استفاده از حق وتو در شورای امنیت، پیش‌نویس قطعنامه پیشنهادی آمریکا برای تمدید مأموریت تیم کمیته تحریم‌های ایران را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/147899" target="_blank">📅 18:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0940fba80b.mp4?token=YXDVvNqEM1hla7qIvS8vHQu84sKTB7_ue_9pdzWiMq9zz3t0Y6kesKPjJQU9mEi5gc1wHn8skUCXggOH716QXBEi43AGNH9pKsTH_z6D3m2jbmAo9hflSqy0sSn_k9dzSieK3ypkJBOuIRMZR3AsLuxZ4IEWtEXoYOHX7fn9oGC6p23bBm96BhovRN99aKXCXBCXApZ4p9KZ7-si8lr5OoBprxFmoKzRlUJNZ0zVawzgjFAxKkcJXhAqfmFG9N6f4KRZHnbhwoABb6z2y9YLAZcC-_cFzS423kH3UngJNsFp5mlduMs7RfDb0l_sb_UWktq6dsJn043Dr-JicIFteBelHShkqT2eHuJvOAJjbLCo0V0843o4L_XFu7_JAlzKvX6LL6V4S-GDL6p9R3kwzBB0RZSYA1g68PxAydW0Ak4vZcAd3VY4skrs0AyoJKoj20W_6c-8bbLvHhPw1Iv61a59_C1PoJhQ60mLjaGzcDyFC21ISW3wYaJoIgXOWRH-JlXmoyx7ZjuZ7sAdYstmqOUcvkksl7MJZ9dTOK0gvtMFb6FcN8XTX3NWOHiV-_5NMdJCtn10Q6TJFjPPrGk9Wh4FSmJbKl56AHco5ERta6h9bX2YK_fsEwVEVhi1zDq0KOV_7KrZ0UqmM3gJXZRVGNB31-wIHCeHQqEoVsNNamE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0940fba80b.mp4?token=YXDVvNqEM1hla7qIvS8vHQu84sKTB7_ue_9pdzWiMq9zz3t0Y6kesKPjJQU9mEi5gc1wHn8skUCXggOH716QXBEi43AGNH9pKsTH_z6D3m2jbmAo9hflSqy0sSn_k9dzSieK3ypkJBOuIRMZR3AsLuxZ4IEWtEXoYOHX7fn9oGC6p23bBm96BhovRN99aKXCXBCXApZ4p9KZ7-si8lr5OoBprxFmoKzRlUJNZ0zVawzgjFAxKkcJXhAqfmFG9N6f4KRZHnbhwoABb6z2y9YLAZcC-_cFzS423kH3UngJNsFp5mlduMs7RfDb0l_sb_UWktq6dsJn043Dr-JicIFteBelHShkqT2eHuJvOAJjbLCo0V0843o4L_XFu7_JAlzKvX6LL6V4S-GDL6p9R3kwzBB0RZSYA1g68PxAydW0Ak4vZcAd3VY4skrs0AyoJKoj20W_6c-8bbLvHhPw1Iv61a59_C1PoJhQ60mLjaGzcDyFC21ISW3wYaJoIgXOWRH-JlXmoyx7ZjuZ7sAdYstmqOUcvkksl7MJZ9dTOK0gvtMFb6FcN8XTX3NWOHiV-_5NMdJCtn10Q6TJFjPPrGk9Wh4FSmJbKl56AHco5ERta6h9bX2YK_fsEwVEVhi1zDq0KOV_7KrZ0UqmM3gJXZRVGNB31-wIHCeHQqEoVsNNamE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سه تن از نیروهای امنیتی سوریه در جریان عملیاتی که علیه منزل فردی مظنون به عضویت در گروه داعش در شهر الصمین، واقع در منطقه درعا در جنوب سوریه، انجام شد، کشته شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147898" target="_blank">📅 18:08 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3WTCAa8sNm1z8mZajqzvOm8702yU2uNOwBnvlsFq9aNTdUfFZFLOVwdSEMxfmSuDLQwsVB6zW_CBTUYbRfvBzJPMS98VFGooCBQ-lAJ2cV8p5xC2td3_k6gJLjb7LI37oYXBZmaEgBNjAu7Z2pLNCkHYeb5GKQYdUb5HKPHGjTVyqarC353vupB9ZdMgG5g3vrbQl_W5fepAvYHZQ-KISZO-J84A8BDaRFKD3FUSlGnGffQP5yqQkYTwVJSWBsWlVP-DyN1rOitM0aJq4ZaJNIecPMxMwqK-y2JqsfD7dfHK89OGn3JlD4Jm7_cwKWufpKCjwjcgoivJWikpC7n6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ولایتمدار: روحانی و برجام ما را ذلیل کردند؛ خدا ذلیلشان کند! حالا با اقتدار مذاکره می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/147897" target="_blank">📅 18:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2SsEuk_Ba293ashT2RqIa6Ola2TvX5TXi_u8iFZWlOuC_aDdxAKEJlswB_OwruSGFh89N-VHdAcmQ2_cYKhlKjfFEsLIAeFRKmwISBuKDiE15ghWrBj3CVrxmjnr-aKlWcCWpF0YC9_Y-fQRma3BPJabVlgDoJ9zV3KKDSk7W7secGXsLEY4K7q_ZOioM25FlgAjQlDhoPUtRNco0VZZgyNg-PRgZpGXOc1OTKN4pstQ4BPRHDVr6Vjc8JAIRaiDf4fUxjAd2SIXd_fEEcCKaMqTtx1j4WrChoH8PVOwDySdJso69egtbAUbJyXDqtSQmECadpTjJRtOvPKQRT6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جذاب ترین رهبران جهان با حضور رئیس‌جمهور پزشکیان تو رتبه ۱۱ام
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/147896" target="_blank">📅 17:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmz0m1MIkDsnVMT83ES5kHE7bynbXUHkUzBa2jsv-F8YPXH9RXgkh9IjqejATM7ule1zQSw0FKZsIL7dhhg4S7k0f48CYLvo1V395D8sYrbSghHW2GuAnoJt9o8saVTMVC8x-mR5_4trLkE-4WcmB1LPpFe255cCQChom5A-GmDrYMHs9Aie-ePYYDEV781fM9j1lP72BDwrm-k_OLmQ10btp_RLLXMx_6-ryxi8gPZLvaAfIHCjePcnj1xn0FxGovIJP202uLQ3aytqzCX1KkVMFm8izLsX31WefXV1ewYC-iVpT9Dalz80dYKUfsHZvefGi0_gpXRjddQT5-ekjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت به ۱۰۲ دلار کاهش یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/147895" target="_blank">📅 17:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
گویا کارت‌های سوخت جایگاه‌ها به‌ تدریج جمع‌آوری خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/147894" target="_blank">📅 17:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
المیادین به نقل از یک منبع آگاه: ریاض از عمان درخواست کرده است که از انصارالله بخواهد یک آتش‌بس دو هفته‌ای برقرار کنند که طی آن، گفتگو برای بررسی راه‌حل ها صورت گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/147893" target="_blank">📅 16:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147892">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نتانیاهو:
تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است، تضعیف شده، نظام ایران را سرنگون خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/147892" target="_blank">📅 16:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147891">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
سپاه: پهپاد زدیم
🕺
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147891" target="_blank">📅 16:21 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147890">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16117ba246.mp4?token=J4mGKn3HV35c2g_ADg2Exxja3iU8Ztr0GcbNWCnvy-usxUCpWWIrgSMOE2gK0ZOCLI1YEUC8VsASgqGAuxZb45vM7R5P_VT37F2fG0QNpertOWnGocww-oCOPi_pUHfU4LlZoy4kFe0DWtiBwkkuvTpDIRDhMngaQ3Rw6-2JmdkjqD2tSiqFdZly_CLPi3tIrXhFsMM-rdgXWmAujxPdWeE5cvLz1FEeSMpIoMJ_vLlm0GOlst9wTiC_8Cp6iC7iKleglAaNbIqcJkny0EQWNllmT7G_6fA_A8YH7Q_OFf9d_nCwJbVJ5UOJej8zPdPLqpSyTmlFaS5tHGJwOmhO7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16117ba246.mp4?token=J4mGKn3HV35c2g_ADg2Exxja3iU8Ztr0GcbNWCnvy-usxUCpWWIrgSMOE2gK0ZOCLI1YEUC8VsASgqGAuxZb45vM7R5P_VT37F2fG0QNpertOWnGocww-oCOPi_pUHfU4LlZoy4kFe0DWtiBwkkuvTpDIRDhMngaQ3Rw6-2JmdkjqD2tSiqFdZly_CLPi3tIrXhFsMM-rdgXWmAujxPdWeE5cvLz1FEeSMpIoMJ_vLlm0GOlst9wTiC_8Cp6iC7iKleglAaNbIqcJkny0EQWNllmT7G_6fA_A8YH7Q_OFf9d_nCwJbVJ5UOJej8zPdPLqpSyTmlFaS5tHGJwOmhO7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر کانادا: هیچ‌کس برای ما تعیین تکلیف نمی‌کند
🔴
مارک کارنی، نخست‌وزیر کانادا، با تأکید بر استقلال این کشور گفت: کانادایی‌ها متحد هستند؛ هیچ‌کس قرار نیست به ما بگوید به چه زبانی صحبت کنیم.
🔴
هیچ‌کس نمی‌تواند فرهنگ ما را تعیین کند یا به ما دیکته کند که در عرصه بین‌المللی با چه کشورهایی توافق و همکاری داشته باشیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147890" target="_blank">📅 16:19 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147889">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obUYkxMwW3HN4xpT3Z83MJ4qSKrY4BXsKRMbJkpNtxpgghZTt2yIqGYI4BjHVaZt_tz5b_kXpj2nUn613-Rc81JhDrcNqkLdluo0fhjJ_7eLOi2rZFt303UNXCco4RPETy1EelxonlkNXBaBFPPcaPCezpUh6R2YSZCzDlkOB7bidTxemSHOvR-PzWIYEpcOp888gUsPzYFLJZvphkllUR3ImaYhlO4wp2qPh3kSNHLXOJUbjet64_pOqwgvjQ4wuPqeYSCyvdFQG5aoP2BsBUoWBupX7Nv9_twr7Yvl3EpUf1u1ZFYcDLl97pFR-9F5Uc_FU1Fvovqr3V6FIfUDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پس از به صدا درآمدن آژیر خطر و شلیک موشک‌های دفاعی، آتش‌سوزی بزرگی در یک شهرک نزدیک به مرز لبنان رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/147889" target="_blank">📅 16:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147888">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
رویترز: شرکت پهپادسازی آمریکایی «پاوراس» خبر داده یادداشت‌ تفاهمی با ارتش پاکستان امضا کرده که شامل یک سفارش اولیه در حوزه پهپاد می‌شود
🔴
این شرکت قرار است با یک شرکت سهامی عام ادغام شود که تحت حمایت دو تن از پسران ترامپ قرار دارد
🔴
مدیرعامل «پاوراس» می‌گوید بخش دفاعی خصوصی پاکستان «در حال ظهور، اما هنوز نابالغ» است و این باعث می‌شود شرکت‌های آمریکایی سریع‌تر حرکت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/147888" target="_blank">📅 16:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147887">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1F2Ilns_3UYOgUsWsopCsCFELR3bD4gvgpE-SZHf0AxZ0_Ybs08E6M2yeFwTxFBkccZVDnMEqzbC2d6PGzf-ztlQ0WvVcidTxU3v01CUSTSFTsGq8IAAd8PlvpjlyqUwoHY6kQ7NbNKvKwYE3fN4zsUSzREHSALW56-KuFaneDbn_giz7xDIn-zPI6Y9qe5CSNxyHP4TuH1tJVFBFF7kBiv43XwwLYmshsj9Z14eKvlehUe-DJ-u3GBkYooUPw6aJ295QM9roteb_xQcEFjrYh1smZtw1ci78o_9lwa-Cb-AzhsLJ8xU6Hd3DouzPbVOwPtrbU2YvBexhD_HqkCog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت آیفون ۱۸ پرو تو کشورهای مختلف چقدر خواهد بود؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/147887" target="_blank">📅 16:05 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147886">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I-BNqljuCJFz43024-wUGwbEgPjExxX-0JH86p9NMxffN41Kfaa_yfUZ5WSetK_ejPVXe2XKOOyESOQWJpqzEEdr5g-Sd7aSinfjIGUpAYI-jENihQuk_VUfXgQw1HNhIDkb5XGc4YO1hp9R208GoAfE0yl2jf64sXVykG8FVIKjYpunYcZGfu8p8WpwbTaBA0uL2NloMbw_d72XyBXsdCCCeBk5elLObk10l0Qp_P-uCFS74zcZODYY1dbWZawWOgDZCb2zWf6wyTu6zVGVGrJPXwEkSJG9dUgMUVdSXJTFNP-bjW6QdL9HVsZnufdX1TYesYt-BXO8zOY1zAH2Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعتی قبل جسد پنج زن و مرد که گفته می‌شود قربانی یک قتل عام خانوادگی شده بودند، در بلوار سیمون بولیوار تهران کشف شد.
🔴
اجساد این افراد در گور دسته جمعی درون یک چاه عمیق دفن شده بود
🔴
عامل این جنایت دستگیر شده و پرونده برای رسیدگی قضایی در اختیار مراجع مربوط…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/147886" target="_blank">📅 15:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147885">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این تاریخ بیت کوین میاد رو 200هزار دلار
از این تاریخ پرواز میکنه تا 200هزارتا
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/147885" target="_blank">📅 15:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147884">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m1qthQ0axTS4-eD0e5ul_LFseBB83lk6hP_bilz8xlnPHsyE1F1T3afLG9F8kuKZozZDEQ98ttSsFZjFl9I5NPT4rmmb0044fRDPxNU5ZnM6v5WGMigWyRVA79HKJxA7YcQaG_i-AFYKOKKYAjUROHdXXZG4Q5R9kBymV-VEQCNxTOWf0RM8R-a5u-G2jRyt0wA2ffkqEyLgxCPlwy4wFEBHYsHLC4FLGNS-lAeCfRB4SOpzx4yMqLHpczYP3r_Rpf8XK_7lQx1jX1VmwWWLHUlQdcZM77PEKjb5tIQCy6QtS4B-ywet79eydLWYVO2Rbs-OGc0zHanc1dDs51bjaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت: 103 دلار
🔴
امروز نفت برنت 2 درصد کاهش قیمت داشته و به 103 دلار رسیده است.
🔴
قیمت نفت آمریکا هم به 100 دلار کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/alonews/147884" target="_blank">📅 15:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147883">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
سپاه: رهگیری و انهدام پنجاه و سومین پهپاد MQ-۹ ارتش امریکا در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/147883" target="_blank">📅 15:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147882">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: جنگ با ایران و سایر گروه های شبه نظامی ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/147882" target="_blank">📅 15:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147881">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96265f0275.mp4?token=Zzs2UYwFITkG0dy8FxkbA_1f83029ES9XzNtmB6_VJY4c_-sl4DEX1jYF8XrXLruQwH135dl20NRdFn4r0kwlQCCmcyDXZU6vgmWiETz4yX2bFhkC1HKIklQl9d81jHDPfnij-8pKMwcmboKKRQYf3n1AzsDadhrG3IqOgQxdg-lIn6ZMLFVqu4ovoAuVoywoEhQ197K_tinkIpAtQ5BvOTeOMuxYhkyvXocmDh87THf_dRXeza6R-AAPu_SC71ZPk6d6eXIIdhP__khCnEhvMf_MgJymDGErtu5cBfQkE7NqPLWeAlg0KGtcpCouWEyTQXSaxdwm60LMF_nhqxlew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96265f0275.mp4?token=Zzs2UYwFITkG0dy8FxkbA_1f83029ES9XzNtmB6_VJY4c_-sl4DEX1jYF8XrXLruQwH135dl20NRdFn4r0kwlQCCmcyDXZU6vgmWiETz4yX2bFhkC1HKIklQl9d81jHDPfnij-8pKMwcmboKKRQYf3n1AzsDadhrG3IqOgQxdg-lIn6ZMLFVqu4ovoAuVoywoEhQ197K_tinkIpAtQ5BvOTeOMuxYhkyvXocmDh87THf_dRXeza6R-AAPu_SC71ZPk6d6eXIIdhP__khCnEhvMf_MgJymDGErtu5cBfQkE7NqPLWeAlg0KGtcpCouWEyTQXSaxdwm60LMF_nhqxlew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: تمایل ایران و نیروهای نیابتی‌اش برای نابودی دولت اسرائیل از بین نرفته است؛ فقط تضعیف شده است
🔴
توانایی آن‌ها برای عملی کردن این هدف، اساساً به‌شدت آسیب دیده است. ما وظیفه خود را انجام داده‌ایم، اما هنوز کارهای بیشتری برای تکمیل باقی مانده و آن‌ها را تکمیل خواهیم کرد.
🔴
ما حماس را از بین خواهیم برد. همچنین ابتدا رژیم ایران را شکست خواهیم داد. آن را سرنگون خواهیم کرد؛ سقوط خواهد کرد. با حزب‌الله نیز مقابله خواهیم کرد و آن هم سقوط خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/147881" target="_blank">📅 15:33 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147879">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jQtpHgWulwTzhFohS2vwrYd0dJuapwjajid_iJTTOWD2j9QCWN2gztsk6pS8kwmG-OVZEfLbY_fbBpVfSu-rca8uEiMYTCNpJYMkMc_LGUWExI8dB52Zy_l1w5a4ZY9dLO2kHfwZ6W0_JdMli2XIoQqMiS2YgLhjI6waMPAFfLWDSpe89KhrCf4GUCq9kaN2ZjgK1or8FyUIUZ3028PwQHFwKkfOH5bMRouQeA8190lVEgYqT7Fy3HECRKp7DCVnRgcLKLPgBxd138onylqcRFib3mbbgzvJ-18dUg4hxIZpMC0-ebwXFXLHFMtjBXwlvIycDGehAv6RQKfxyjBp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/auTJzssrBaw47hvV93YG2DOTcFf1RsXyUNX_WskEfNDeb_dZtkg89MjB3adYxsShzY60iLbiZERVOj-HzAvjX1c7-mpF9_-d1D2rCgE__wqwB4TpNRyOEuPrHVCx8JFF6D9pjvw_1FoRO_8v8GZVSawnBUDkNmfzVDSi57dVT6-WOzQFNIyo3szDUIvNcIFq7T3M16_bnRFLTli8PA32zgHcrFCMI7-2sNYzWxy7CVNYD-RGOJfhmGRJveAhXPep0PWC70O_eJ9Q6f-47xQyrbIsI4jUS_iq2n1dsJXBLjTGSkzC08EOy-Ox-_MToMrh4rP6uV6q-YEVDu8HQjPxiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
فعال شدن پدافند در شمال کرانه باختری
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/alonews/147879" target="_blank">📅 15:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147878">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VeTbUBES8pUamB1RA_Tncd_VkzZFTQp8_5dK1qOM_mIUWZTZoinMZM7FWFEE3GZrc8hHmASX50irPrzLkniA9eKofMqbLwM-IGBEWDo7EK1AeQyaUEDRyJcI3gfaoCUuf_0iEtPiMxA4WrBEJlC5tRPfB3ubIG1HAeXkA3bZRvxx4Tvm4UQYt668zY8r-I36DRNzMpboTeLThltm1awuckPzrImlGhw7qFgvzvjEqOp6THUb-13obac65F14wYuHjc3H-eDcM7VQQxFKdPDVGmjJBYiiLOaCgnueaY87U7QtdcIKy02deVisarO4O7Ch4iP-pH-aGYZJsJ5aVMaVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سعید آجورلو، عضو کمیته رسانه‌ای مذاکرات: آمریکا برای کاهش فشار از مذاکره مجدد می‌گوید. سخن ایران مشخص است؛ به هفت شرط مورد نظر تهران عمل کنند تا تفاهم عمان- ایران درباره تنگه اجرایی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/147878" target="_blank">📅 15:26 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147877">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NknBXN01aa45IWqlQ6Gd_XHDhy46FsQOMygA9KWxzRXPU4BhA8Ozv5bC3lZvc8AtHbfz3VxLxO6tQcrszziPAifycrJygd2n6Zoh-DGIweHynoysswuZyqi6Ri-a0QnPp-K5YULdGfO8f2zx0Xyn-AXpYPACNPfNcu3C3X-Gt1zyV1nhxKDzAZQzoiT8eBcgauNfrU3SbAe-46M6XDItC4iD_TogxMCR_ibx-M6y7O-n7YBRKzBcazZf11JOg0sl575kGZGfLiPehbipqzQPLZCxIUTUiaY-swlpC468j848x_Ga--1r4C76BJaRAAsVz89bCgtq5IglZ5nOSJznAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش ها از نفوذ پهپاد و فعالیت پدافند در شمال اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/147877" target="_blank">📅 15:16 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147876">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
آناتولی:
عاصم منیر از ایران خواسته تا انصارالله یمن را متقاعد کند که به تأسیسات انرژی عربستان حمله نکند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/147876" target="_blank">📅 15:02 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147875">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
تسنیم: ممکنه خاموشی‌ها توی زمستون ادامه داشته باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/147875" target="_blank">📅 14:50 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147874">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دلار 227,000تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/alonews/147874" target="_blank">📅 14:29 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147873">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSGq2JoQ0J0ya_OSF9b96fhMwlD8Bb_urQYlNL8Sx9Pi0J42uH5Ch5QdicEHn4Ayb9AmbEtkkXg8LzkingpSNn-ILA4JN7MdCrfEf6vbE_Tj6PN3Xuesm15lrhBIFozIZbHHuU82LSRWY5G2hZ_ZtA7RSzuLLRaYE0okFUpo3HztrVrGtiwNmhjoC4lpaGFZF0ez3g0qjfbG9W2DjiNmlW3fWkx78zbw58wvoXXTN1y2kBA0NixBd-07fySmsqSgwNeJTonBWseEzil_OkYXI_8vE8ZScMsoDQyeE5FKOo5QqTtLTMIfhhz9_gHdl-f7DUhJqc4K_8qTlMuGN4KYGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای سوخت‌رسان سعودی از جده به سمت مرز یمن به پرواز در می‌آید تا پیش از بمباران یمن، به جنگنده‌های این کشور سوخت‌رسانی کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/147873" target="_blank">📅 14:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147872">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcydIVLIe2bUAg2hLtmmy6SWb831WbqRQd70AdSiHjNF_IA2vayTJMk85pCunG1JHjIgdJuAJ0upmgUZ5b2-njaMySNC3145zfXGGpjMlKJA2D7nLfRsz_YmXIxWWffTiXEdlCnNe0lfuSLwQ5Zg7GoG16MNsEMtWPn45xPUqKxT5l6Qy8vYIPIRRvL8wLEcok3Ok5rQI1WKAVLtH4A0pC7lUKyANbZ62KdaGnaCoQsjuxJNNKiJIsNbilqT6V3Y9OT7xBChaSTqpcUZ1-JkvVQ5ILxu9KNtJkdP5QA9EbtTDqi7-UyBTy2z1JUbcLJ1NtxC9g6zc_L4w6T15-j-XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز - توقیف تویوتا متخلف با راننده ۱۱ ساله در یزد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147872" target="_blank">📅 14:07 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147871">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
کرملین: تصویب لایحه تحریم‌های شدید آمریکا، تلاش‌ها برای دستیابی به راه‌حل مسالمت‌آمیز برای درگیری‌های اوکراین را پیچیده خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147871" target="_blank">📅 14:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147870">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ترامپ: اگر‌ کانادا بخواهد به اروپا نزدیک شود و اروپا به او کمک کند، اروپا هم تحریم خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/147870" target="_blank">📅 13:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147869">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUf-szsgAZExIkGmQJQpzymUBXg-SfNYsRhikEyusxos42xEx-aTRG-BXWhCjf8t8EgA0DrTLXDW25QM2dku32pgz9DknjDqTVsJrTFp09WGkTf0zzCN0tfa5oXP698LePo8vte4Sg_Guh10XKJGop7BjAmxpL7g7q1Scfnp3QceSwkDurTyQiG7nAAG6V1ooCseLGtgbnwzZZloOpZKIJWR3ADzd2zKhpf4U_Keg3djFxb9ki-RILIcn7t-weuVxGCzgoSa7m4UObp3dmwVSdZ8CxQ0gzpKvGW_k8BqUBjDNcelwnwAeNYW5jb8qb6m8LtMVPOHUy_WqvsTbiXDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۱۰ فروند جنگنده اف ۱۶ آمریکا به همراه تعدادی هواپیمای سوخت رسان، صبح امروز از پایگاه لاژیس در پرتغال به سمت خاورمیانه اعزام شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/147869" target="_blank">📅 13:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147868">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
ارتش روسیه ویدیویی از هدف قرار دادن 1 قطار اوکراینی در استان دنیپروپتروفسک و 3 قطار دیگر در بندر یوژنی استان اودسا توسط نسخه هدایت شونده پهپاد گران 4 منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/147868" target="_blank">📅 13:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147867">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
رسانه The Nation: ترامپ علاقه خود را به جنگ با ایران از دست داده، اما جنگ همچنان به او علاقه‌مند است
🔴
اردوکشی او به ایران یک شکست تمام‌ عیار سیاستی بوده که اعتبار دیپلماتیک و نظامی آمریکا را تکه پاره کرده
🔴
جنگ برای ایالات متحده بسیار بدتر از آن چیزی پیش می‌رود که قابل تصور بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/147867" target="_blank">📅 13:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147865">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
اتفاق وحشتناک برای طلا
‼️
‼️
👇
👇
👇
👇
https://t.me/+cs85WnZxgpM1NjRk
https://t.me/+cs85WnZxgpM1NjRk</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/147865" target="_blank">📅 13:25 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147864">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
گاردین: عربستان سعودی از مصر، بریتانیا و پاکستان خواسته است به صورت فوری به جنگ با حوثی ها بپیوندند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/147864" target="_blank">📅 13:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147863">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">‏
👈
صرافی کوینکس رسماً اعلام ورشکستگی کرد تا پنج روز دیگر زمان دارید دارایی های خود را از این صرافی خارج کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/147863" target="_blank">📅 13:18 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147862">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db56a3dd02.mp4?token=FZDFacGoj0qn3a7P6rQRUanVLfIXPfMqdQ7uBwEOf0O9Ng8ttB-kW4mo4CAJgbPQ23WFcicfYK_OOyfLy8ODUVEDntgSPVGCb5DSwmHnIOyx-d-yQh1Zf-haFCZKSYQZmpTCtUBGC1kR-tqZjpryE-xq0zV1IwqRy9LNX8SKFG0HMkmitvHnH_sSATSgJLwsXWc6AlNhVsYuCLkEsqe69ah-MAhRcWpmfhR0o4_u_Y7VFvefHwwZXpz78BNd5pdikU7fNTJEfuXGuQNSoeLE3W9XfttivdXskbQ7G2qnSZFF6EZjsENsRr5zp2BPDevfYcXklwbOo-9QAkI_fetqeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db56a3dd02.mp4?token=FZDFacGoj0qn3a7P6rQRUanVLfIXPfMqdQ7uBwEOf0O9Ng8ttB-kW4mo4CAJgbPQ23WFcicfYK_OOyfLy8ODUVEDntgSPVGCb5DSwmHnIOyx-d-yQh1Zf-haFCZKSYQZmpTCtUBGC1kR-tqZjpryE-xq0zV1IwqRy9LNX8SKFG0HMkmitvHnH_sSATSgJLwsXWc6AlNhVsYuCLkEsqe69ah-MAhRcWpmfhR0o4_u_Y7VFvefHwwZXpz78BNd5pdikU7fNTJEfuXGuQNSoeLE3W9XfttivdXskbQ7G2qnSZFF6EZjsENsRr5zp2BPDevfYcXklwbOo-9QAkI_fetqeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
درگیری شدید در جنوب سوریه و کشته شدن ۳ نیروی امنیتی
🔴
الاخباریه: درگیری‌ها بین نیروهای امنیتی سوریه و یک گروه مسلح در شهر «صنمین» در حومه شمالی استان درعا، بامداد امروز پنجشنبه آغاز شد و گزارش‌هایی از تلفات مخابره شده است.
🔴
شبکه خبری العربیه گزارش داد سه نفر از نیروهای امنیت داخلی سوریه در درگیری با افراد تحت تعقیب در صنمین، کشته شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/147862" target="_blank">📅 13:03 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147861">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ درباره اروپا: چرا باید بار مسئولیت این همه کشور در اروپا را به دوش بکشیم؟ ما بار مسئولیت کشورهای اروپایی را به دوش می‌کشیم
🔴
تنها کاری که باید انجام دهیم این است که بگوییم: می‌دانید؟ ما دیگر با شما تجارت نمی‌کنیم.
🔴
ما دیگر به هیچ چیز از آنها نیازی نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/147861" target="_blank">📅 12:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147860">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
پولیتیکو: پیشنهاد اورزولا فون در لاین برای تبدیل کانادا به نخستین «عضو وابسته» اتحادیه اروپا، پایتخت‌های اروپایی را غافلگیر کرده است.
🔴
دیپلمات‌ها می‌گویند این ایده پیش از طرح، با کشورهای عضو مشورت نشده و هنوز تعریف مشخصی از جایگاه «عضو وابسته» وجود ندارد.
🔴
کانادا نیز با احتیاط به این پیشنهاد واکنش نشان داده و مقام‌های این کشور گفته‌اند تمرکز آنها بر تعمیق همکاری‌ها است، نه جایگاه پیشنهادی جدید.
🔴
مارک کارنی، نخست‌وزیر کانادا، قرار است امروز در پارلمان اروپا سخنرانی کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/alonews/147860" target="_blank">📅 12:39 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147858">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
پکن: چین تحت فشار آمریکا همکاری‌هایش با سایر کشورها را تغییر نمی‌دهد
🔴
وزارت خارجه چین اعلام کرد: همکاری‌های تجاری و اقتصادی پکن با سایر کشورها بر پایه برابری و منافع متقابل است و تحت تأثیر مداخله یا فشار طرف‌های ثالث قرار نمی‌گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/147858" target="_blank">📅 12:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147857">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
الجزیره: شمار کشتی‌های عبوری از تنگه هرمز در روز گذشته به ۳ فروند کاهش یافت
🔴
داده‌های اولیه ردیابی شناورها که امروز پنجشنبه منتشر شد، نشان می‌دهد شمار کشتی‌های باری عبورکننده از تنگه هرمز در روز گذشته (چهارشنبه) به تنها ۳ فروند کاهش یافته است؛ رقمی که نسبت به ۱۲ فروند در روز پیش از آن و بسیار کمتر از میانگین ۱۰ روزه (حدود ۱۷ فروند) است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/147857" target="_blank">📅 12:24 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147856">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445b3dec5a.mp4?token=kLbho2QcR4jBj2B4kJ2Wb9fjbd76bi5jQXbfq1zrdHS0A6AM_NIFfz-NRwprSd_--Fy1kf2mSIcMYOhvn_UCSMBTukwnn1CxcAAp9Eg16TB-HLdqG6KGOS78wj486P3ahZTlsNsuOryOCA-FF2bPegNN5JpWHz41AvGb5aETexC5zdX38bNI8P7GE7UTkeeX5fMRWu8r_6Wqn0bF97zgxR_YvDej9M6tj-j0QKiUCXcO2bDYD4MMtIWBVNBl7ZT6fOKNUN9sP3zCy2Qe6pn9KlxGg9v6Md5YWl_9UwmrchS_Sp-cxDIzscOqSaYpVX6iRoBSKseaOZb7n3TzctvpXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445b3dec5a.mp4?token=kLbho2QcR4jBj2B4kJ2Wb9fjbd76bi5jQXbfq1zrdHS0A6AM_NIFfz-NRwprSd_--Fy1kf2mSIcMYOhvn_UCSMBTukwnn1CxcAAp9Eg16TB-HLdqG6KGOS78wj486P3ahZTlsNsuOryOCA-FF2bPegNN5JpWHz41AvGb5aETexC5zdX38bNI8P7GE7UTkeeX5fMRWu8r_6Wqn0bF97zgxR_YvDej9M6tj-j0QKiUCXcO2bDYD4MMtIWBVNBl7ZT6fOKNUN9sP3zCy2Qe6pn9KlxGg9v6Md5YWl_9UwmrchS_Sp-cxDIzscOqSaYpVX6iRoBSKseaOZb7n3TzctvpXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرادویسی، تحلیلگر اینترنشنال :
بر اساس این 3 تا خبری که تو این هفته منتشر شده، بنظرم آمریکا داره خودشو برای یه حمله نظامی بزرگ به ایران آماده میکنه :
🔴
حرف ترامپ که گفت شاید قبل از انتخابات یا بعدش، کار رو با ایران تموم کنم.
🔴
صحبتای ونس که گفت شاید تو یک یا دو ماه آینده، درگیری با ایران وارد فاز جدید بشه.
🔴
جلسه بردکوپر، با فرماندهان نظامی اسرائیل و کشورهای مختلف.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/147856" target="_blank">📅 12:13 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147855">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به نظرتون کدوم بیشتر رشد میکنه؟</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/147855" target="_blank">📅 12:09 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147854">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
پهپادهای اسرائیلی در ارتفاع بسیار پایین بر فراز منطقه بقاع شرقی و رشته‌کوه‌های شرقی لبنان در حال پرواز هستند.
🔴
پرواز پهپادها بر فراز روستاهای سرعین التحتا، سرعین الفوقا، نبی شیت، صفری، الخریبه، جنتا، یحفوُفا و الشعرا گزارش شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/147854" target="_blank">📅 12:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147853">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjmssKPnFhRrJfhTohR5zfi3tIEI-d7_V_ONm0S_3-YlaXI7qq_fYct7VaOqOQ5kbGInaKUxas2QrpmizPu6AEr0S5ao1ae45EXEd0Hpetg8Q_GTfRGq9XBVZNaB5Mc_W0cg8j6ggJyIW-SPfCeu_1UngE7hYb00Tstwtn5Ilgi4T8fyiDsfuzIuYEopWW92bnfPz1lhyhHKJnz207UvwZ-Y0zddIaWF0NflM0vRIvcNdudQW2KLFS60aDmYk4BUL3X5ESdjIBUYQ0mld09ZPcwiSPypDrRbAd2JA6foBz8iVYqfaiHtVLaYk-8y2tH-ebO3o_v5p7f7WSQukNH1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از حملات هوایی عربستان سعودی به مواضع حوثی‌های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/147853" target="_blank">📅 11:57 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147852">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
عربستان سعودی در ادامه حملات خود به حوثی های یمن، صبح امروز مناطقی از شمال و جنوب این کشور را هدف حملات هوایی خود قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/147852" target="_blank">📅 11:47 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147851">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLyXQIhZBmNwZwQzrMA4nDpkxG6NVHuj0nsApAvdnw22j8TnXShrun7vo_DhqgHlCci3fXKsXbEIlaCESYBeYcuXP6XQqE8zkSRCh95S_f766fJYGm6F_5MrACwn1ertI9T1EHq-a7NLhJqHqQleMDgR08FNN05MXOu277vbocu8jL6uGMJW1_kkhkz1jh9CTKcmhCbq062SK2Q8uA2ZQPhuC4HMM5Ljy3yHeZNKp4W46PsIViuv6IsRJqj0-yODiT8Zm3cFGBjAXT7NFXBiy5IeNgVyKN5FoMSCvRa8W6cPoAy0vc9CRlagRWgKN0QIJvWL7nYSGBkqmgWNwEduhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه‌نویی: اونایی که به من حمله میکنن مشکلشون من نیستم بلکه تیم ملی عزیزمونه، اونایی که حمله میکنن یه مشت وطن فروش خائن هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/147851" target="_blank">📅 11:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147850">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بیت کوین منفجر میشه
‼️
‼️
‼️
اگه توام نمیدونی بخری یا نه حتما ببین
👇
https://t.me/+4jOgodAq96dmYzY0
https://t.me/+4jOgodAq96dmYzY0</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/147850" target="_blank">📅 11:42 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOoX_mqM3nTjgTmWwmK4O7ToHe6JlQWq0V_W2zLIcQymLg2mHsbT3ESFcikoI-eFbe-npy2BSRd8RrXTCbVDcsG1Gn60BvQlNZNMkdW9EMAUBzlMgHroUX_fSFkZKxqa0QgapEYL2GjuHfh1SMXtr-PfHGwiTkzzIP3SKFtu-kgP0XEfyDAf3LcacAQFSgA87dB4BCZJOHFzysy_yUaHanI6Q6lmYEbA7Wg1vSwqBOUQphIvuGZawg4Om0epTKF8r9_ae9Pb_jge7Q7BhU1dRHoeU0SjH30cMXeIxdV5Czv6c_ZO7FDzrbo8FFyfPUahKk0rImjtg_gHXjSwTfl8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cPKYIpx4BejUkHNfb9rYh4XSZ4xEUSdsQcvhKR_TVr65QuF_Qmsnnq2fAhl0_5D17RarHchHgnx7XBDtC5xYMcnrjLY1Mv10E31DMSaoQfdW--zBn4UsvnyPgr6ngAUtZGe0ohiRoYScrkCuae3R0MNCxT-IFArTC2ncR6xM_Q3UlYpjAsJf9IxzJ6kC_wWH_mfu9YTV8tthUve72Nqc9DX_ZcxCVn_mIh-3-Bq6J-mRZomsQcDkEsXA9NFVZMbxKDEx0pnFElSc4aFEWwI7PxXXTOFxc7dSLjkwe-tz4mElpxRvffogLDjqpG6BJ5vC7EtUF8TjsGrxAsYiuUPguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hd9fHKq7UcuR3uKZq4RPCiXB9FwhbZDzdKjlA_350jytNRR7hzmHMrxkXRZ66z_yQiEqsVQU4jad4W2szHZK3itqDhshiFrrRsrwNGrKGzv8Y6bwbLsA91R-q3giADtbP3b1bD7I_z19frkLpmAESQG-RuvxzU5TAPHQQuJRqYzMJ7dbx94l1FUtALk1ni2Dr95nPAbKThnCuqiNrrms1bd-1lpMzSeIPIb9ZrMhivC0ddV-7t7Y2NNaSrNm6af0pLSv6iUg0dxo0BK5WAa_9Jxp2ld10XcW-VPHo4Mmcojo47K-uIf1iceLgPGU4Ixwy9YJV89aLitsmEBTA5HSBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
هواپیمای هشدار زودهنگام آواکس E-3 آمریکایی پس از حدود هفت ماه مأموریت جنگی از خاورمیانه خارج شد
🔴
هرچند برخی، تغییر شکل انتهای این هواپیما را به برخورد پرتابهٔ پدافندی نسبت می‌دهند، اما دلیل اصلی این تغییر شکل، فرسودگی ناشی از مأموریت سنگین و به‌کارگیری مداوم آن است.
🔴
فرسودگی و استهلاک تجهیزات، بخش پنهان این جنگ بیهوده برای ارتش آمریکاست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/147847" target="_blank">📅 11:40 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147846">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMsSWmb--K62ZeIKGydoUq6NtjUaGIf7PNZvRK_uVA68V8ZQ0xlP2sU2z4S-oRF7tr5xGSFp6FXoFyfNsFjbbh5GOeJOQNdKgqEceq_tZ5uquRBfwBVZ-w2irZ2hO0xwzVrnBax4RpwY6Z34CN31ysn9LJLtWagOsI5Jk5G1mhbBWvse1G5kEJvxLH7oF0ucgIjdryZwl8oCGRBsKRQ7ecwbmAKqHeheBkBoz7_f5zR7Mwd1iOsYcK8Wr0d-0kPq6fMqurMsEZmCOkLwrL5I5OFUAB_szPFFqf04Vv57uOdL09R0es9gQd9POZMUPGTvhBS1TjsXwPb6kbtSgXDVAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال‌استریت ژورنال: آمریکا در حمله اخیر ایران به اردن، در برابر حدود ۲۰ موشک بالستیک، ۶۰ تا ۷۰ موشک پاتریوت و بیش از ۱۲ موشک تاد شلیک کرد.
‏
🔴
‌برخی موشک‌های ایرانی از سامانه‌های دفاعی عبور کرده و به هواپیماهای آمریکایی در پایگاه موفق‌السلطی آسیب زده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/147846" target="_blank">📅 11:37 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147845">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
الجزیره: گزارش‌های مربوط به اینکه عربستان نفت خود را از طریق عمان عرضه می‌کند، قیمت نفت را کاهش داد
🔴
نرخ هر بشکه نفت با ۱.۲ درصد سقوط، به ۱۰۴.۵۹ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/147845" target="_blank">📅 11:27 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147844">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
ساعتی قبل جسد پنج زن و مرد که گفته می‌شود قربانی یک قتل عام خانوادگی شده بودند، در بلوار سیمون بولیوار تهران کشف شد.
🔴
اجساد این افراد در گور دسته جمعی درون یک چاه عمیق دفن شده بود
🔴
عامل این جنایت دستگیر شده و پرونده برای رسیدگی قضایی در اختیار مراجع مربوط قرار گرفته است.
🔴
جزئیات بیشتر از کشف اجساد پنج زن و مرد در تهران
🔴
اجساد کشف شده مربوط به یک مادر، دو دختر و یک پسر خانواده می باشد
🔴
سال گذشته دو برادر خانواده که پس از سرقت طلاهای میلیاردی به پلیس مراجعه کرده بودند مورد ظن کارآگاهان قرار می گیرند
🔴
در ادامه تحقیقات، دو مرد به قتل پنج عضو خانواده اعتراف کردند و انگیزه خود را دست یافتن به ارثیه عنوان کردند.
🔴
آنها پس از قتل، چاهی حدود ۲۰ متر حفر کرده و اجساد را که داخل گونی قرار داده بودند، در آن دفن کرده بودند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/147844" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147843">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
رویترز: بحران اقتصادی ایران، مهاجران افغانستانی را به بازگشت به کشورشان واداشته است
🔴
افزایش شدید قیمت‌ها و کاهش ارزش ریال باعث شده پس‌انداز بسیاری از مهاجران افغانستانی در ایران از بین برود و درصدی از آن‌ها تصمیم بگیرند به کشورشان بازگردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/147843" target="_blank">📅 11:04 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147842">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0b6c3f846.mp4?token=Dmp9zftpWZ-gytgdvCLeHmLqJ56vK8jLOE-2rwIw11K5mlba8QnGX2r_S3_CmPgMuIbaHkauVKrrfF-tDOeOiErIaqDUslgnLOJVDC_fWNYeSZyrp9dgHmqBM-bChomG0YxGdWSbGWqMlDntidLyRiQJeyn7ngkmp_6x1lYjjMdsz5D6ICsWaBb1aumcejq0o799dQ1McvmuCk5DtNltX-ebmSZIbUz1LO0p4b81rz8Gt1bNK0GjwozK7u88ohNPypuZ3S2cEaZequr7zL6xt8cp7Bnds1bwspPUQXsBhyQImEx3vW1XmrtTbsK61gMz812nsVJHvQskl81Wcst3RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0b6c3f846.mp4?token=Dmp9zftpWZ-gytgdvCLeHmLqJ56vK8jLOE-2rwIw11K5mlba8QnGX2r_S3_CmPgMuIbaHkauVKrrfF-tDOeOiErIaqDUslgnLOJVDC_fWNYeSZyrp9dgHmqBM-bChomG0YxGdWSbGWqMlDntidLyRiQJeyn7ngkmp_6x1lYjjMdsz5D6ICsWaBb1aumcejq0o799dQ1McvmuCk5DtNltX-ebmSZIbUz1LO0p4b81rz8Gt1bNK0GjwozK7u88ohNPypuZ3S2cEaZequr7zL6xt8cp7Bnds1bwspPUQXsBhyQImEx3vW1XmrtTbsK61gMz812nsVJHvQskl81Wcst3RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عضو مجمع تشخیص مصلحت نظام: دیگر جنگ جدی نخواهیم داشت؛ یعنی دیگر تهران و اصفهان بمباران نمی‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/147842" target="_blank">📅 11:00 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147841">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ژاپن در واکنش به احتمال نقض حریم هوایی این کشور، در روز ۱۵ سپتامبر جنگنده‌های خود را بر فراز دریای ژاپن و دریای چین شرقی به پرواز درآورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/147841" target="_blank">📅 10:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147840">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQzLpsJau-KFUd5Absh36NyYlamJysshuzTnuy6v7j_jNfSkNTt_VafPQmdB9RpmUHz9URTIkKz61Vqrn2CKBCpj_I6Ercvlq7JXXLvp1noXdcZePiI7fS-K3kXgkI8dcI-ABrLh8bhOamWhz7l0jEcwcTgYBvD1B-SqQP_1EWpmoaWGHWWz93uhD1StNfOC1HVNigzCR02DYsxrc2PEwV68e4aqvyXswJ5ZoJsVogCwwV7QxOqJXOIgGipeBPOjQZzYYNUKj3aJmUMPOBZu_SHX6zJTuVFlcJy7J42rahX8g_BV-sYV30lLtMM3CJ5RrBR3I5MpWfc0NuhY_YxT0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زکریایی، کارشناس حکومتی: امام علی تا آخرین لحظه بخاطر حکومت مخالفینش رو کشت، تو حکومتش هم فساد زیاد بود
🔴
حفظ جمهوری اسلامی از جون امامان هم واجبتره چون حکومت الهیه
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/147840" target="_blank">📅 10:49 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/957feeea93.mp4?token=ITiHc3MqH_kCqfp5dT9dkkVlDxFs00my_ZXC-dm7d2b9jbWiyBDKdIOs5H3BAKXFC_rx9Dwe-T3W6tn5LUbQFfjac1dpQ9_m9XUOoucd9y1HWYl638F-IHECk1XOqtaAiq6uiPMA-Cm_JYzqZq2RyBqQ4BsbHpLThaXorpkBHzK3gxau9BQEKgEn3i4DTDjCw0TMjJ48v5BBTC0ZLZDYiTtqgBZhZJRffwpnfugL0ponTDkYA76JWERDSZEGmZpSCHhU5vl6iNRRuzIHOEULEzuo5iv0I2_kTY2NHL2oWpWM02GsM3-vqs6TPXgndoR1q2dCT34DScp8VFjw75nIhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/957feeea93.mp4?token=ITiHc3MqH_kCqfp5dT9dkkVlDxFs00my_ZXC-dm7d2b9jbWiyBDKdIOs5H3BAKXFC_rx9Dwe-T3W6tn5LUbQFfjac1dpQ9_m9XUOoucd9y1HWYl638F-IHECk1XOqtaAiq6uiPMA-Cm_JYzqZq2RyBqQ4BsbHpLThaXorpkBHzK3gxau9BQEKgEn3i4DTDjCw0TMjJ48v5BBTC0ZLZDYiTtqgBZhZJRffwpnfugL0ponTDkYA76JWERDSZEGmZpSCHhU5vl6iNRRuzIHOEULEzuo5iv0I2_kTY2NHL2oWpWM02GsM3-vqs6TPXgndoR1q2dCT34DScp8VFjw75nIhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله به یکی از بزرگ‌ترین پالایشگاه‌های روسیه
🔴
پالایشگاه نفت «اسلاونفت-یانوس» در شهر یاروسلاول هدف حمله پهپادی قرار گرفت؛ تاسیساتی که از نظر ظرفیت پالایش، جزو پنج پالایشگاه بزرگ روسیه است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/147839" target="_blank">📅 10:48 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147838">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=uhcbM4j6Frc9K5muSVgNsmsWnvzvYiszt6b01Hb247co0aveCZnfij5cqzIdaPsk9pU18j--iitjedJSjdNEViHd_8TeM8FIznS6p7b9pJWwRxgjHFJMvhaQ2BZabMGD0ipHex6ZJDb56A4jyiInbWadePwk0vE_TcEvdC0PFhp5uNKcNi-kt2OVwc7gLCtt2E1TWt6VePQ4p6Ndelab2_iYbwirFj0FDTcvWsV533QQCEltDyALu2yp1MFyxAKNIV5oS4Vaj1ksRQPR65qvGEAMGnhzqpuXqT3sU1V2lVmNngXI17kZzNoJPM8gbCwOsIOpIlZhu27LLp_1-HS3Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=uhcbM4j6Frc9K5muSVgNsmsWnvzvYiszt6b01Hb247co0aveCZnfij5cqzIdaPsk9pU18j--iitjedJSjdNEViHd_8TeM8FIznS6p7b9pJWwRxgjHFJMvhaQ2BZabMGD0ipHex6ZJDb56A4jyiInbWadePwk0vE_TcEvdC0PFhp5uNKcNi-kt2OVwc7gLCtt2E1TWt6VePQ4p6Ndelab2_iYbwirFj0FDTcvWsV533QQCEltDyALu2yp1MFyxAKNIV5oS4Vaj1ksRQPR65qvGEAMGnhzqpuXqT3sU1V2lVmNngXI17kZzNoJPM8gbCwOsIOpIlZhu27LLp_1-HS3Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عارف: از مردم عذرخواهی می‌کنیم شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/147838" target="_blank">📅 10:44 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147837">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: جنگ روسیه و اوکراین به‌زودی تمام می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/147837" target="_blank">📅 10:38 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147836">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این استوری یکی از اعضای کادر درمان در مورد زگیل تناسلی(HPV) هست که میگه: زگیل تناسلی به قدری تو کشور بین جوونا زیاد شده که وزارت بهداشت دستور داده فقط تایپ های خطرناک رو گزارش کنیم و بقیه رو منفی گزارش بدیم.  [@AloTweet]|</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/147836" target="_blank">📅 10:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147835">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad31b0089.mp4?token=QuTrSpoxzU49N5ECoZV_CQpeZc1FDIPIqERpt4rP7E0oJos6ShOJzI8Tgjtly_cvESr9xtzDmPMFnRsfEpxj7sLBnyCQsuS9tBvrlLaGh5n0ei9VMExbieUGye1slNaBNweRUojOC72h3ZyQfmbSgt_bbgxSUCMu1e91OZo08Pz4bnrXcJG1zCiGe6BzQasJvtoqvjm21a-opKNywwM6Fnd1AB48896mg-2hni3jUFh7tdgHI8XvctfHLNVvacu7VhS4xLWuyggCub83IFPgEIDsnGR99AwAGY-0F_ZWbm4_ix2t4LFNOeWKPHce6lWKZEMc-j-_V1YcliOWRaadRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad31b0089.mp4?token=QuTrSpoxzU49N5ECoZV_CQpeZc1FDIPIqERpt4rP7E0oJos6ShOJzI8Tgjtly_cvESr9xtzDmPMFnRsfEpxj7sLBnyCQsuS9tBvrlLaGh5n0ei9VMExbieUGye1slNaBNweRUojOC72h3ZyQfmbSgt_bbgxSUCMu1e91OZo08Pz4bnrXcJG1zCiGe6BzQasJvtoqvjm21a-opKNywwM6Fnd1AB48896mg-2hni3jUFh7tdgHI8XvctfHLNVvacu7VhS4xLWuyggCub83IFPgEIDsnGR99AwAGY-0F_ZWbm4_ix2t4LFNOeWKPHce6lWKZEMc-j-_V1YcliOWRaadRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کنگره آمریکا تا پس از انتخابات میان‌دوره‌ای در ماه نوامبر تعطیل شده و چند هفته فعالیت خود را لغو کرده است؛ همچنین رأی‌گیری برنامه‌ریزی‌شده درباره استیضاح پیت هگست، وزیر جنگ آمریکا به تعویق افتاده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/alonews/147835" target="_blank">📅 10:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712b365b48.mp4?token=hCWhDPgYZtkp8FXmlA3-kJnBwUl5x6e3lzmncLAYHFZSKapEG5QxHrBIrks7sGLasfJ8Z3d9LCun1eJB5Po2GphOJzXVYWzq1gBANxNH08XzTtsWGDg2nOZgqha_bmHpqPFfIzHGv36LzFVdDTQZgof1CLZmOGYhcQvPN3_GpskhB0-_LC3LXBq8_n5-cSV_NFovpCpJoeqWACsW-AEB9HMst5yC8GNc0MHTO0jJ7Poa6v4vY5sY-Mvi7jWiIoWEcqYcBYE3FqfNA_qcj31fxLivuQE3SZptwbvrjV7Syj0RW_IBsS0aF3FSJSBtfoYoJ-zH9DAGgzQOqQljrW5KlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712b365b48.mp4?token=hCWhDPgYZtkp8FXmlA3-kJnBwUl5x6e3lzmncLAYHFZSKapEG5QxHrBIrks7sGLasfJ8Z3d9LCun1eJB5Po2GphOJzXVYWzq1gBANxNH08XzTtsWGDg2nOZgqha_bmHpqPFfIzHGv36LzFVdDTQZgof1CLZmOGYhcQvPN3_GpskhB0-_LC3LXBq8_n5-cSV_NFovpCpJoeqWACsW-AEB9HMst5yC8GNc0MHTO0jJ7Poa6v4vY5sY-Mvi7jWiIoWEcqYcBYE3FqfNA_qcj31fxLivuQE3SZptwbvrjV7Syj0RW_IBsS0aF3FSJSBtfoYoJ-zH9DAGgzQOqQljrW5KlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرماندهی جنوبی آمریکا (SOUTHCOM)
:
نیروهای «کارگروه مشترک نیمکره غربی» روز چهارشنبه یک
ایستگاه سوخت‌رسان شناور
در شرق اقیانوس آرام را رهگیری کردند که به گفته آمریکا، از عملیات قاچاق مواد مخدر دریایی پشتیبانی می‌کرد.
🔴
اطلاعات SOUTHCOM این شناور را به سازمان
«
لوس چونروس
»
مرتبط دانسته است.
🔴
نیروهای آمریکایی خدمه شناور را از آن خارج کرده و به مقام‌های اکوادور تحویل دادند و سپس شناور را غرق کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/147834" target="_blank">📅 10:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-147830">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fsc1srI1yynlabiHftT6Wdr6WT0IvuWk1aozh8cw6XVd9PiPw5zZ8sC1zOgsxPhpfRAQ3k5odzYF4GHeeL43pS5ujd2F8BBP5HLZWaLsxlpQd4lfNybWgoVSA232Ulb0zoXLOJ51-_BjcSVbHlKZmZvAgz4VZarKEjUbSzlq_HdKu-zDNOf9w_AAXOGx8XdBkGUgVsycqclrLIuojAvu6kV3Y7juwAdLd-fbgQemeAhgiWBbnYCLd5t_wWDMjANRmc0hna0l7C7uEehA_oy3sB1R0v9gbIrgk49CSxh3GJ8R1HiCIH8wFy49M3CmGOXCYGtwWMzyBk_PAk9wwRAfaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QXqUdVoFkrP3J4boqxS-uVw-4zjKje60a53dStA-RjTbvn5VN1E2c4fjnX0HMIM3PPjUS1fEzb9LnreErcrlgeu2pyUtkL9q9uISJGNp2TopeqRhKwRdCAYxsmRxMojmnyxLOZVQnZ2gpNj5wgDOKxpzm26ArInETOlJ0ZdciVTHvhbdvBSxMzXknTjdpA8ySRBzaPvShLCE_i7uniYHsYXeO8X_NVSivS5nSaKQHb14KmzUYjZB0XoMXQ31O18k5Dwu_XRwVN9YOnVkhVEzj_ctEoLGegkn-NL6Xpdbi25S1BI77Xf0PMnB33QwBlv_soN_eH1A67NiCb8uSBuKPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asEitixFveQEzMBWoJliea_N6SFnhg8kqyWIOcaNyNY-ytmhkk7x3t-cs6dsXLrsPI8qdCMphMmhHYVA0U4dZi35LwIuHDRN3JvAtQtd5FrpvwIhXirTE_IJu3gT28FQSSxNlg-fmwxWZrJyL2Dcn6SEW-GrwHU_zFMjWxSFy37iqEb09OEMkqGUWawFxi6YsEQ1jwyy2_Lblr28XbAZXRNlQqlK8TgkzJR86uCbeWF9qiQyhwPHoKw9pOqEZr0qeJEbhBsfbQ2MrESpcFMZkuH65_-owzX4LffgsDAp-R01PMDbtnRzdrQYx6-H9bgFhmgqZxgxfZWHI8poGUW6Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rKn-ZMIGd51UTLZophbPsOsILDhmkXnEW1APGilG_RzNoeK7ig6ZoBEYiyJdMFccLVINYiGCoqBfeXxwzTv-Q4LydURmxp5xfURExzKB8e5cRDZUxYZ65C40dV1gk5BJh3vkRZr2MdSOARXhZmQvz3KWYIoPltg81UocHdeOXUtC7tyf70twTdVPIna_KBRSKNNmgGhS_VpsVIYRKQSBl0FqSFJWKTzx8Kntezw6AshL1iyvLZ1Cl-Qt5N1wOCOV6JmAoDscri0Ki2iNFRvrYqG4Ii797xf77VPee8vjkbh_cQKYJfPD-iwmKWMtHxgUgtVQ2rYVoOfAfMqOCmCiAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خسارت وارده در کیف بر اثر حملات موشکی/پهپادی بامداد امروز روس‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/147830" target="_blank">📅 10:23 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
