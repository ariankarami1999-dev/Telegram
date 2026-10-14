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
<img src="https://cdn4.telesco.pe/file/Ppy3EHLeWhiRw0rxmolyCmCjQ8N-XykUMzUd-YWpq1hWFjvhnzKgoUEyT87hPRAKIN4cEe3_c_P0yiGdLCo6BCObs-xiI9xpHwB_FU8-z2cHb9VLWEJTHnndvED2aS3BbXwDMJy-SOr53xmW_oDzl5l7vhw3uN0IaQFnxMKcrWLNs2jNzUDQJZKqE5BBRWYrZWD1jA42HU4NRM2T_XaqB_APMoHG7LKuAKixq5BC8rYJ60HlE7dfX72t1Uc0RiMpnpQ3kk7u0_7xhFiwN7XpVHqudriRde93O5Sjph_qzr0JO9lYlUuZwJXwZ9crREuSHNq8R7HREQnsy_fn6J9Kvg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-152656">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
بیانیه دولت عراق: زیدی، حمله به فرودگاه بین‌المللی خالد در رياض و هرگونه حمله به غیرنظامیان و تاسیسات مدنی را محکوم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/152656" target="_blank">📅 16:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152654">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Sngx_hlYQqCJjzE7JN9gMwlR7_yQERX5-MTeX-DsshwCe1c_Z8SHPAXHVXIem5xwh58o6ecsSTjRIi_sb4lpCjJmcZRctbvc7AXmoZcjAIhDAoSMQgNVF5l1STuViaH_abX1M2IkN8n0oJaRVeSUF9meyQ4FeKXkWcaOAOtyQciS_GEkpXG9toXFNlWPUBUaD9lWlRf0RGEGxjoscFYlVTfyE_uj9zL5Bz6ay_hSEnSVW7Tm-B0w92C-oVVylwfHWFy7Fij8bHHmgsn1U4nEd5EZRUN93FsQHsoYxYr0U0rzoSN3rijxQU0ORFmvIOMuuCKucqW1kfulIxgtkvr8Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jrTf_f9pg3WsxxJ6Ju99GbbaE_PlCcGIBKV1MC61uJXg9mvplJcov-KB7uaf2oWNRR73nid7Fv1EWXafUjPqoxqVQM6fHauBYt1o8a77NN0Mcqw8BZLOUIuR2OihfOiZvdkdG42ZcEFnnRnzmAzduDNFE2YIgcEGGRJ-LnqhY1pETLl7VMQ9nU0ae4VniRvSXt_khzZADIg7mPNIptIG0wbXbT83nNFywOGKHsXOcxH91389K2rL3i29yYy5mCS7B8k2y_QIWac42J46T4r_ohnxyk11TwXRbNnCYxXNeWt-DokvK4GHc619LriGDEasZs5Fop_ny8DYF1cLJaCubQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر بسیار عجیب خبرگزاری مهر و ایرنا از ناو هواپیمابری که درحال قاچاق خودرو به داخل کشور است
✅
@AloNews</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/152654" target="_blank">📅 16:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152653">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
زلنسکی: روسیه شب گذشته با ۳۹ موشک بالستیک و بیش از ۱۲۰ پهپاد تهاجمی، به طور مشخص زیرساخت‌های انرژی ما را که شامل آتش‌بس می‌شد، هدف قرار داد
🔴
مسکو اظهارات ترامپ را قدرتمند و بازدارنده نمی‌داند
🔴
از رئیس‌جمهور آمریکا می‌خواهیم تحریم‌های شدیدی علیه روسیه اعمال کند
🔴
هیچ کشوری در جهان نباید در برابر بازیگری دیوانه مانند روسیه، تنها گذاشته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/152653" target="_blank">📅 16:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152652">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4482fcb60.mp4?token=JD70Bo_s_a8yI9eNdw5U1_j6S7ptop-em21tHiUMR3_7kL03-Z11ZBEhjwP5eIzyK3bTC2gh-7DKz56GYSvuXX3Guikg-H1ZhFaVuXWh24SCyA--sAyHeY6_lcXuwvqXs6u-1-wDPl7-BYHpL7mhaV2YN1rmWJnOkGDzwOOScz0yypQU3dbGLoWT0EY2ltJJO00PLxyR4mrqJ3AguyIHDMjeXbFVGLQ0Q7C5nD17A2muyP5WMXi5EOe-8w69TB7TTdofFqZbQNkfkii-GGqx3rY1EtHl-aAcjjRmlDGwF21AuekDVdPPacJz1jk-ALOgJTikEttTtFfljwewayJV3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4482fcb60.mp4?token=JD70Bo_s_a8yI9eNdw5U1_j6S7ptop-em21tHiUMR3_7kL03-Z11ZBEhjwP5eIzyK3bTC2gh-7DKz56GYSvuXX3Guikg-H1ZhFaVuXWh24SCyA--sAyHeY6_lcXuwvqXs6u-1-wDPl7-BYHpL7mhaV2YN1rmWJnOkGDzwOOScz0yypQU3dbGLoWT0EY2ltJJO00PLxyR4mrqJ3AguyIHDMjeXbFVGLQ0Q7C5nD17A2muyP5WMXi5EOe-8w69TB7TTdofFqZbQNkfkii-GGqx3rY1EtHl-aAcjjRmlDGwF21AuekDVdPPacJz1jk-ALOgJTikEttTtFfljwewayJV3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: شاید بتوانیم یک کشور فلسطینی در اوگاندا تشکیل دهیم. آیا این می‌تواند راه‌حلی برای تمام این مشکلات باشد؟
🔴
نتانیاهو با خنده: «پیشنهاد شما به‌طور جدی بررسی خواهد شد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/152652" target="_blank">📅 16:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152651">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/959217c881.mp4?token=e23E2kZVJBmRBEtFYhfI1z-FZ9YfmPPIm8_Uwe-Cb6tNbBIAVj9xu5rbrx1g05BspkCp7lgTJ6a_cNPKp7bfD6QQni2FyYEl5xXp1b1USNnIN-hZx246smHganGAnYCIwnolKYSpcREt2m4yvYUybgoFXTXiBbL9IHkIIinxz4WJ1gpsDEL3WqcGIIMILqsP6BZx1hB4ZdhlwKGk08UPW0N36ylUKXlgescRY82-VOYuZ3FWdoFfZRi0lUEMvuh0_FGbcB5zbRbPI8J6jelllLf_5k-W34t8PJHwQpsaTN-406Qz-UWntnwrdeNpql9sENmz5-f__MATZhYahLsNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/959217c881.mp4?token=e23E2kZVJBmRBEtFYhfI1z-FZ9YfmPPIm8_Uwe-Cb6tNbBIAVj9xu5rbrx1g05BspkCp7lgTJ6a_cNPKp7bfD6QQni2FyYEl5xXp1b1USNnIN-hZx246smHganGAnYCIwnolKYSpcREt2m4yvYUybgoFXTXiBbL9IHkIIinxz4WJ1gpsDEL3WqcGIIMILqsP6BZx1hB4ZdhlwKGk08UPW0N36ylUKXlgescRY82-VOYuZ3FWdoFfZRi0lUEMvuh0_FGbcB5zbRbPI8J6jelllLf_5k-W34t8PJHwQpsaTN-406Qz-UWntnwrdeNpql9sENmz5-f__MATZhYahLsNfYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجروح حملهٔ صبح امروز به لنج صیادی سیریک: درحال صید میگو مورد اصابت قرار گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/152651" target="_blank">📅 16:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152650">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIJL8kBsUIiZdN7zEmeVc_n4DhzaVQvq0H013pqI_GxFjKw1vNNhnbIJgAr3TeE7NEtjZ4URzeTQfpy5P7KEtEV2hVtXgUANAbF-F5PINkQhXkY3rLZ64_fGdllxrXGo5mCBKMps1KEyo8JJMWFtiqMaIJZana3DwVpZdQKBbfF9GLTz9wmocbp-kCW1_NyXc0kF2y2m_7UtHnYR99BueM41wGhJxFOBCGhDUmV8E56PSUag7SgElGYP_k53quVZhvwy_3wHT_Gy0zuo_rv_nLV42xT8EPLuyPjC_5aW2iNIXjde2M_V_r8D9PaYfOYiTdzPSGFm_cThEUYj8ol1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: اکتشاف گسترده نفت، گاز و مواد معدنی در گرینلند آغاز می‌شود
🔴
دونالد ترامپ در شبکه تروث سوشال نوشت: «اکتشاف گسترده نفت، گاز و مواد معدنی قرار است در گرینلند زیبای ما آغاز شود!
🔴
کارشناسانی می‌گویند ذخایر نفتی که به‌راحتی قابل استخراج‌اند، از ذخایر تقریباً هر منطقه دیگری در جهان بیشتر است.
مهم‌تر از آن، گرینلند از نظر امنیتی و دفاعی، هم برای آمریکا و هم برای اروپا، موقعیتی بی‌نظیر دارد
🔴
هر حمله احتمالی آینده به آمریکا باید از مسیر گرینلند عبور کند؛ جایی که سامانه‌های دفاعی ما می‌توانند پهپادها، موشک‌ها و حتی سلاح‌هایی را که هنوز اختراع نشده‌اند، رهگیری و منهدم کنند.
🔴
گرینلند از نظر زمان هشدار، موقعیت جغرافیایی و میدان دید، شرایطی فراهم می‌کند که در هیچ جای دیگری از جهان وجود ندارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/152650" target="_blank">📅 16:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152649">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
خبرنگار الجزیره گزارش داد که نیروهای ارتش اسرائیل در حال پیشروی در غرب روستای صیدا در منطقه جولان در حومه قنیطره در جنوب غربی سوریه هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/152649" target="_blank">📅 16:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152648">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
بر اساس ردیابی اطلاعاتی منبع باز، بیش از 19 میلیون بشکه نفت خام روز دوشنبه تحت اسکورت ایالات متحده از تنگه هرمز عبور کرد. حملات ایران به کشتیرانی در طول روز ادامه داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/152648" target="_blank">📅 15:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152647">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rkyv7d1_nG4gm-I6hNflq8_obhZcNaAFa0zS9fmrhnEIsq4Q59m3qtNWOmLkqIlc6mmhzXztueJsPM2AlCAazHZTuV_t10BZbaX-_hcB9HcRXXR4S8e9ZEi-jut-NzqASZvuJtZCbk9BKpNprbREivGnZJCswNTfB7bqNUANEYTF8dwhuaTxfBvvu2qp539_DRDlxLw7BDYq_dTtIU0ixNFXFNwD0bBDP3RTZgkVz5fRi6msVRZjeBqeIwr1HIuZQcgEMIL8nzUewWx5rh6Lbb1TxMB6ZTcZm_WFmj7wCrL9IrcTMQUwGqN2UL06TjgMefhtIJi5jUCOGblLkNTCbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a4914da11.mp4?token=rkyv7d1_nG4gm-I6hNflq8_obhZcNaAFa0zS9fmrhnEIsq4Q59m3qtNWOmLkqIlc6mmhzXztueJsPM2AlCAazHZTuV_t10BZbaX-_hcB9HcRXXR4S8e9ZEi-jut-NzqASZvuJtZCbk9BKpNprbREivGnZJCswNTfB7bqNUANEYTF8dwhuaTxfBvvu2qp539_DRDlxLw7BDYq_dTtIU0ixNFXFNwD0bBDP3RTZgkVz5fRi6msVRZjeBqeIwr1HIuZQcgEMIL8nzUewWx5rh6Lbb1TxMB6ZTcZm_WFmj7wCrL9IrcTMQUwGqN2UL06TjgMefhtIJi5jUCOGblLkNTCbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواپیمای مشاهده‌شده در نظرآباد آموزشی بود
🔴
درپی مشاهدهٔ یک هواپیما در آسمان نظرآباد البرز، مشخص شد این پرنده از نوع آموزشی فوق‌سبک و متعلق به فرودگاه پیام کرج بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/152647" target="_blank">📅 15:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152646">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
مرشایمر، نظریه‌پرداز روابط بین‌الملل:
این احتمال وجود دارد که عربستان و امارات، آمریکا را برای حمله به ایران تشویق کرده باشند؛ زیرا تصور می‌کردند می‌توان ضربه‌ای «ناک‌اوت‌کننده» به تهران وارد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/152646" target="_blank">📅 15:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152645">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ac89bffc3.mp4?token=XQN8WMkNtkNmTuXVkzY4ePPjX7eX98H_Li8Evi-021t6PpocnRW5fYjJ_pg6W0NnvK8wedxVy_YDKWTobbIxD6ZKrNt6fmLLuVHZU-XYixOO6A2U99Ge__rUwcQLT6r6SaPDoch_iK1MMWMSPIgMOK7aYRgsYpeNihGSN0f9h4KmbvIh4R8zYgUE0OGDpvs4wcJIDLEMRj_TgL8roxDdpX5CwejjNxaRATiHfbaUUnA6Sy13y-8ubjmxLbKB-jum48GTCc5my1WjBNaUKLGjURFQUKnY7GvngZeDMp8N9r-1fIL_Cm4aVnjjCo-L3CxHJTS7cpnrHsKrHRTd3XxEJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ac89bffc3.mp4?token=XQN8WMkNtkNmTuXVkzY4ePPjX7eX98H_Li8Evi-021t6PpocnRW5fYjJ_pg6W0NnvK8wedxVy_YDKWTobbIxD6ZKrNt6fmLLuVHZU-XYixOO6A2U99Ge__rUwcQLT6r6SaPDoch_iK1MMWMSPIgMOK7aYRgsYpeNihGSN0f9h4KmbvIh4R8zYgUE0OGDpvs4wcJIDLEMRj_TgL8roxDdpX5CwejjNxaRATiHfbaUUnA6Sy13y-8ubjmxLbKB-jum48GTCc5my1WjBNaUKLGjURFQUKnY7GvngZeDMp8N9r-1fIL_Cm4aVnjjCo-L3CxHJTS7cpnrHsKrHRTd3XxEJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وای‌نت: انفجار و آتش‌سوزی در کارخانه اینتل در جنوب اسرائیل
🔴
در پی انفجار و آتش‌سوزی در کارخانه اینتل در جنوب اسرائیل، سه نفر زخمی شدند.
🔴
همچنین گزارش‌هایی درباره نشت مواد خطرناک منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/152645" target="_blank">📅 15:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152644">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGPMSVeRC_2ZWTeB20A3W9_WbCavcU1ytvxR4fMSYHujQhJSncVZYhkyZ3Z0Zfa9Y1KHv6AmKJkMqKbGow1VpstDHPo3nPAfwMez4O9Y14nkwzs0VdQCVPzWNgblqjjm7XDW2ajt6Kyv7Ia-aixDET2ThtNUtvajclmRULDB0YWW8qfUpk3ZdyUDYDRw8aBDSeFazxbdcM8D6blQTFAJwJvukz0yJjv7lvK8T1LvxbiMLnSYAY9ja4Kw-JRZxovp4DK_h92qpN9Fz_rEHdmegGXyo1ZwLBpytP9VcJUIolBC-aJrHKhyqvapA3OXKSchTTh3zS87VDHc0ypzkZZ-tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۳ هواپیمای ترابری نظامی آمریکایی، بریتانیایی و ایتالیایی به سمت خاورمیانه در حرکت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/152644" target="_blank">📅 15:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152643">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL0AXsby4XFvtpqe0HauIVITekOwApxEDxyj23FyeLz7Goe0riRYr7elg8TjbITEp_ZffmCq7iHRL_MveCCc9cr3FCopldI8jHdhT_7f_S2zUWUFWhLNK7Awr5BjkRQlGRGMxApyJoSO__x879xfviU-1G9WTs6za9FGjLb7gBYJzVYVyA-jUECudt7oUCy0xUEpUcH9CwIEym1ADuJhxO1U8RFstKT3RjLBCEt-j3AnNYD2HS9kNuInj8QDmvSOCZn3EnZxDuMQW2VnPxb3eXsioyigNNhR22bYIv6rLNUxqbdYukD2flXrSJya6J_8UDiJ6bUUG1fxv2WytsHlLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان: وضعیت صادرات و واردات کشور و فروش نفت عالی است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/alonews/152643" target="_blank">📅 15:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152641">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VznUNT8PU-mQxHpOh_KhyRNC7m7qGgSLyndV5YDJtQkGreCtdfI2Z5Rr1RlyVIFM1X7MxnDSqeVE9YvJmPV8bUeUxcSHTLz_iSBzOWaedYVMwkef3gp3iqMfNp4WqZVCbk-3ANbcJHOmnjQqsZB4EDCntQuQR9ydptDtEq9oW43FQDYPBN7khZG5duXZ62VSaCCMVzqmUIXLv5qsmxmT6i0R0Xx8yvZwffkd34QosqpMNwqwtscijmtw-n7fWjv9XQcLu0IoukmKcUAIYjqaxyHCaW5UwTBnwD6l_oC5Qq0FGWnpHEZHBXyg9me2H4F3tcTZPpfbYUvsAk53coV13w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XGqAxShGndIsKyn-k8thWhhJaxzWrh5wvGYSyQbbBdBvTz-jnSJ5CaduMOvUl5pFSEr6TPAwt-dKn0Ex5xOqk1Fnrs-gp002LyH_KySn9TZJV2uNou9S17Kw48ekGixzUFlrPoJ9xLNKRcTRdk1ohJiz8w5KEzcdMWKzG-zXZ5YkS_79vCPfmH_XaK242SJIpT3mqa0RIcAitZRwWfS_EPW8Hj5yKTIUutZhRlvaTHvjrns_AQYh9GkKJ5x4jOI-ob6IVqQJ_4knDIF2Puw9WlQdW-I9_75P0-FEmItg5hDwtoaAnMzEo8kUr8hjeb-lOYmgbFlxkM8QwKPe6oYqAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر دیگر از لحظهٔ برخورد کشتی کانتینربر با مین در مسیر تنگهٔ هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/152641" target="_blank">📅 15:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152640">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ در حال بررسی قطع اشتراک‌گذاری اطلاعات اطلاعاتی با اوکراین است.
🔴
یک مقام دولت آمریکا به رسانه سمافور گفت: «ترامپ واقعاً عصبانی است؛ ممکن است دستور این کار را صادر کند.»
🔴
این موضوع در کاخ سفید در حال بررسی است، اما جان رتکلیف، رئیس سیا، با آن مخالفت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/152640" target="_blank">📅 15:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152639">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کاتز وزیر جنگ اسرائیل : اگر حزب‌الله به ایران در حمله به اسرائیل بپیوندد، ضربه سختی دریافت خواهد کرد و زمین‌های بیشتری را در جنوب لبنان، به ویژه در مناطق النبطیه و لیطانی، از دست خواهد داد.
🔴
این مناطق به بخش پایدار امنیتی اسرائیل تبدیل خواهند شد. به ارتش اسرائیل دستور داده شده است تا برای یک عملیات زمینی آماده‌سازی شود
🔴
همچنین، محله الضاحیه در بیروت تخلیه خواهد شد و زیرساخت‌های آن تخریب خواهد شد. بیش از یک میلیون نفر از شیعیان به آوارگان داخلی در لبنان تبدیل خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/152639" target="_blank">📅 14:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZCR0nmBNpH9WrCPlrcnhmC6hXB9jOTOXKfbJSBVzT5vdZDs5jpw2PY22uSk0q4jNMGPC9tRuE7iw3L3S_t9bf5gZx8bMRuYndZ0u3LXnpnEGMgc4u4KK3dFAppSPW2GdR_XUPttka7r3Fu3dockyxGj5KGPtNXZavccrxr7TifR9s73vGyUZqfTkK8k6ewuxXJsM6RUHiBZNB5yx7x75C6_BZ5dXGZCwAgQy7wj5IGX_ZXSmvFRT6nooTSEh0-C025ZkqPC7meSjmsi5siY2qW2qy1x4gjqL0IMX6G85_aGQZJ2d7tjBbaog_jUoI4HDpH_KMkNoncqwudCVjQ5aow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dgHGu5aS_agIrtuY2EAXIuvp-_C8pnmjJ5oY84GzfjKdGGhQ1Et-AJcXnxBcOeouz83J4GzEOeJ46NtiO3GneqMXR0EzrSokiL2J5TtZYBC7wk6SfSkotLnqvzcU1qvKzfqdByJuYZ52AAItk7mz7_erPUHTBBPpdSRNePm_fdQ3Mp1gMfzDj48Xm9idon9Z4SVrhCT_Ly5qSzJgS9-8BhpGhD1tl8LMNiG9ThaT-N5NUeYvu9ZkqUxrC-btp5CgImY08PRN5rQLYCVyqqjnymhEbZtEfr-jv4vD25aQ4GA9aB3X6UjZPMp_jnJ46vlm7QUDyHZotBf4t0XV61Zngw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سامانه‌های پدافند هوایی فلاخن داوود در شمال اسرائیل مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/152637" target="_blank">📅 14:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
رویترز: مقر شرکت آرامکو در ظهران در حمله روز گذشته خسارات شدیدی دید و آتش به چندین طبقه سرایت کرد. به کارکنان دستور داده شد از خانه کار کنند و پس از این حمله، بخشی از فعالیت‌های شرکت به دفاتر آن در خارج از کشور منتقل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/152636" target="_blank">📅 14:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
هاشمی، وزیر ارتباطات: در شورای‌عالی فضای مجازی مصوبه‌ای ۳۲ بندی را برای رفع فیلتر سکوها تصویب کرده‌ایم که باید اجرای آن پیگیری شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/152635" target="_blank">📅 14:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152634">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
آمیخای اشتاین، خبرنگار i24NEWS :  نتانیاهو، اعلام کرد که در مقطع کنونی و در آستانه انتخابات، با انجام حمله پیش‌دستانه علیه ایران مخالف است
🔴
نتانیاهو گفت: «از نظر من، اکنون زمان مناسبی برای ما نیست. من در تمام طول زندگی‌ام، همواره ملاحظات امنیتی را بالاتر از هر چیز دیگری قرار داده‌ام.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152634" target="_blank">📅 14:19 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152633">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی انگلیس: یک فروند کشتی کانتینربرهنگام عبور از تنگه هرمز هدف اصابت یک پرتابه ناشناس قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/152633" target="_blank">📅 14:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152632">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
ممکن است ۱۰۰ هکتار زمین را برای دو یا پنج سال در اختیار افغانستان قرار دهیم تا کالاهای خود را از طریق ایران ترانزیت کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/152632" target="_blank">📅 14:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152631">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نتانیاهو: نیروهای نیابتی ایران قصد دارند در روزهای آینده به اسرائیل حمله کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/alonews/152631" target="_blank">📅 14:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152630">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQMUu9wQJSpvkkt25Tvro-R4yJp7iiAG6O3iJ-FdKeNGjknVS0OI8mmUb1adrilmVzdsqaDLOENaG4G3l3z8MwhFKsILatFUhWDowpwi-hok6EkNGD952J8oTqMgKPET-txAnjhQUPda2J1BGloPKD33A7ZeUQWM3tEN8upGN1FZFEGjelK66eItZG0o9myMpXzbz7as5-2BnJ3T9R5vtzig1g9MZMD-kEFwYcZpgvfsj4ChkJPEQ0DIEvjqao8msySZqgBGDhud674XX5GQ0W3wDkFqL_104abUqbku2anuK1SdXFqCpvOnDCqiHBCUqalRntEmZoToCzhE_r2Zbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آیت الله خاتمی: مسئله فلسطین به ما مربوط نیست و خودشون باید مشکلشون حل کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/152630" target="_blank">📅 13:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152629">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0ZMCWT966E9epN-WWMDfPa41tt6Xiy_eK4Q2pdF56ayZRkoSoha-LVjjhQB4FQdGJG2XRBeSgxElc2dres9R4tiW4TteEEEMrXuwUO31MneNzEdQpHWlGGxZIZc7oj0b_CzLaTpI03l4cUM4uUlxvLJtnVY2i-kYQB8WCUd3KJZmMg3LUfdJN3yZFBTuqHMpSgaD4AmLwaIRlB_HWPheJu3OZQyhxUan2zVb5n2YRmHXP7ujVE5O-zL896maVLwjPBMaeKSfgDeKaw46lsXKp2RKl8YFL-qtjJlGX5a5eHzfD4BaNEoLBJM6oaFn-GnppXnJvykGfAFiJHzKP8_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پلاکاردی عجیب در تجمعات شبانه برای رسایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/152629" target="_blank">📅 13:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152628">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/duA-X9L63n9w-DNYLzDO3xm66SQcJh6mFhYGfsPX4TDIYmea2hmYKjHYfqrqGNAO_9P7mJbxU9rQJBj-qQ2hlzrgcdKH5z_HAxQKiPfLrk5QCI1y0YRzmavBP5ngzzSFKkW33ZaALMDbMFiTput4FYZam-E6H973RLzWwcctorWcQ0bIfzlodmcw8hAbzc8N7C_92mVOCwKkYuEy6VMFQcOkXd3aVfcbCe038YzkR4Nl1YYVq8aDtWe8ZGIig2IOmWEW5-dUzSTMvi9GzFlMicoYJul_bXbosTYUsYiEdz6z5J2zD6d5pRHFDfuyx4fYDjuD06eW6_xuz3xYRZm1DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر عراق وارد ریاض شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/152628" target="_blank">📅 13:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152627">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
برخی رسانه‌ها از شنیده شدن صدای انفجار در استان سلیمانیه در شمال عراق خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/152627" target="_blank">📅 13:39 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152626">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
وزارت خارجه روسیه: تاکنون هیچ درخواستی برای میانجیگری جهت حل و فصل مناقشه میان عربستان سعودی و حوثی‌ها دریافت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/152626" target="_blank">📅 13:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152625">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فایننشال تایمز: محدودیت استارلینک عملیات اوکراین در خط مقدم را مختل کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/152625" target="_blank">📅 13:29 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152624">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
سخنگوی سپاه: ایران آماده است تا به هرگونه تجاوز مجدد، با قدرتی بیش از هر زمان دیگری پاسخ دهد و این‌بار، پیامدهای آن برای آمریکا بسیار دردناک‌تر خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/alonews/152624" target="_blank">📅 13:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152623">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
مسئول بسیج خواهران شهرستان مهرستان در حمله مسلحانه کشته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152623" target="_blank">📅 13:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152622">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/PKrolojmBac4UPPfcX4K5J9WicOisgxGjRD0kl_ozUNzM79tvlrZt3S5Hz3HSCFn0zxxVi1jbLIf3_q4Afuu0h0y7cgJIknzNUYYdf-cNItREpzK1D-PoLTmJA-sZEJbLFh5DaetYqlvZeP_JyvLXaBTSt2Haz_D_ysHvJxr0uJp-f12TW-XtiJjTiIE95wR2AdOYiC5h-1AqvScubVtUONQbDFqzTXG-FiBTfikHSIKovo2wtIvw5I1hzxBechGggAfu7eAFtMPeCTIRxqxDIMlSAvfsVxhnMs5hrG3dMrWNCE7fHWS6Hzq9wnGtsiuCJHHKwcSM8nsBEfhm1dZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سپاه اعلام کرد یک کشتی باری متخلف با ۲۵۰۰ کانتینر هنگام عبور  تنگه به مین برخورد کرده و در جنوب تنگه هرمز غرق شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152622" target="_blank">📅 13:02 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152621">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPG3B4hkMcoR1fh-KWDeuIJQFAcztRenhdxxWC24O3C3FdnX-iWNR4hgXevEJ5W0ry2Mfv7gWdWbXBXZ2UJeqEQrsA2RKK_LjkWPPB2OpJTn5mbWL6I8j8X1hCBbml8FKql2wNVY19pZQjFAo6Zjg0nvvII-hAfwzt2S-qG7hebkg4lPVbYrR_GUBcp-8sx4kea-dzUdDp4JAd5Tc1-kHVDEgjF0ZlcUp5m3czreh3njhEpiW9_euH7VbQb3Mn4jvwkaP2nBFaCH-7Ix47J602hWb86HAO_ulvD4FadQ2XIe3uxsttNPYXnnVbl6frRySh2uUZe2K8JKv1d62cDS4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت عجیب کارخانه برای ارزان‌ترین خودرو؛ پراید وانت یک میلیارد و دویست میلیون تومان!
🔴
قیمت جدید سایپا ۱۵۱ بادلاین پاششی با احتساب هزینه های جانبی ویژه مهر ماه  به شرح زیر است:
🔴
پراید وانت با کفی پاششی:  میلیارد تومان
🔴
قیمت قبل: ۹۴۷ میلیون تومان
🔴
میزان افزایش قیمت: ۲۶۵ میلیون تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152621" target="_blank">📅 12:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152620">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
خبرگزاری مهر : ترور یکی از مسئولان بسیج وابسته به سپاه در سیستان و بلوچستان‌.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/152620" target="_blank">📅 12:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152619">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
هشدار امیر قطر به شهروندان این کشور: باید برای بدترین سناریوهای ممکن آماده باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/152619" target="_blank">📅 12:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152617">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
هیمتی:  فروپاشی اقتصاد ایران توهمی بیش نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152617" target="_blank">📅 12:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152616">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزیر خارجه پاکستان در دیدار با همتای عمانی: خواهان حمل و نقل آزادانه در تنگه هرمز و باب‌المندب هستیم
🔴
به نقش آفرینی برای کمک به صلح در منطقه ادامه می‌دهیم
🔴
لزوم خویشتن‌داری همه طرف‌ها در منطقه و بازگشت به دیپلماسی
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/152616" target="_blank">📅 12:24 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152615">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فایننشال تایمز به نقل از داده‌های کشتیرانی و منابع: کشتی‌ها در تنگه هرمز با شدیدترین حملات از زمان آغاز جنگ روبه‌رو شده‌اند؛ وضعیتی که مالکان را به تجدیدنظر برای حمل محموله‌ها واداشته
🔴
ممکن است ایران در حال توسعه توانمندی‌های موشکی ضد کشتی خود باشد
🔴
در دو هفته، ۲۴ کشتی هدف حملات ایران قرار گرفتند
🔴
صادرات نفت از تنگه به شدت کاهش یافته
🔴
برخی کشتی‌ها به سمت بنادر آمریکا در خلیج مکزیک حرکت کرده‌اند تا در منطقه‌ای امن‌تر محموله بارگیری کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152615" target="_blank">📅 12:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152614">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SnPTljafarhfDGVhqtahL1klZTIdyCzAz_qMtoyov0dG962V0LRWYH2UHObzjv_sfcumYf4hYwtanz5E_tZCUoYm-sws4k5zj3OVFOzmv_Yz8msCfZoyt-4Js2j-kYh8IYSNK2dEa1HdEnBI59cgNKDytA5oQDsqPudL7HBinjjWpICreyeArMyCN1hsJF3ChKlxuapkLmFwZHFvGtiDzZpxy03kPvjz1UEgjx2axYG4Z0cDb_DrJgaX60Bg3h4noWJpPBYsSx0E1qhUaT5v3d-qot8AAX2WMUjQum11oEmRblSn1Xt5Cw3RZcTlwqkGEfEiVy6RnfkgHlaSZRBLeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خاله نرگس، مجری برنامه کودک: میدونی چرا به ما میگن ارزشی؟
🔴
چون ما با ارزشیم و مخالفانمون بی ارزش!
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/152614" target="_blank">📅 12:11 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152613">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
بدر البوسعیدی، وزیر خارجه عمان، اعلام کرد نهایی شدن توافق با تهران درباره تنگه هرمز به نتایج مذاکرات آمریکا و ایران بستگی دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152613" target="_blank">📅 11:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152612">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRk3-9cv2EnfIb7xrV_JFnWbgDJORYjV9dV4qexInrIsoIhBXxNtdGQdz6bZSxqy2AJo7njwQrFOvuCN1lUifHKCXWqsI5PMABdgoJGoYJzzU54NUx1esbT4G7JshShXgfod38BklyRIbpwvkAbSqSX3bzXq7jcui7doFqxwUWqU4wffrBou9Bs37TMyOeAmJJvY7F3V4D2m0XNz_Jclpt_0Nr9byC_0sqEtq9B-SrBCHIp8ztLAx4sKLZnveJy_UapIFqI1WaogZAerqiVTP6DuoN-12YJFYy1DNpLDczhP59_zYAjThkWusN2ncMvzZ_rGnLFNNB8e4Y12FnVDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: باید مشکلمون با آمریکا حل بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152612" target="_blank">📅 11:47 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152611">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
آماده‌باش اسرائیل برای احتمال حمله غافلگیرانه تهران
🔴
رسانه‌های اسرائیلی فاش کردند که در پی افزایش نگرانی‌ها از تجدید تقابل نظامی احتمالی با ایران و احتمال اقدام پیش‌دستانه تهران برای غافلگیری تل‌آویو و وارد کردن ضربه نخست، سطح آماده‌باش در بدنه امنیتی اسرائیل به بالاترین حد خود رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152611" target="_blank">📅 11:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152608">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihY6z1iir3Xi4_ZA_kPXSrNPjChZQ5M8B8UHtEe7BR9p7PzNdmtGh9BJdDTfTPvO_Y9FgqlZQVVTP3usWReVrNdUg7w6pSSfP7YemPf4MGzm1Kh7bojUAa0hAmwiuhN69lQA6K9jYjFr9e8F30-EQVOPi7IlK_k87TR2IcYIZJKBWDdv0hQCTrhl2rJqWORJYIZ2uGQMf_C-CVsQHBX9vvkuzPg7mysI_dHxDVV95LX4Vmrn5i44niieIJwM0heKlZj3mhm2SrHDRbmy4m85v2jl23c0eOFGuVYTQoLrX5haQKexikvjxtsHs76SWG7wwoQ9x6JFmCQuAGWx3Bp8yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPmRQTu-Z6KxV98w9P4PhFVKo9IAnNW1bDrRD4tt8caFB_j5B58KZB9q0f2t5tFubHlx5H8_xhclBzT1kN7m4mWkks95_NJH_lRITeI8oURiARGeJB-OftD8GUhiqaWjIBZgajsEFFXXAiaXkkCDy-fqgjNu7M8WoFrGo8T59q2B86Mk0C5RhcJdNJJ2__oEdi5jjhLpwIkG6HYJppkjyGaRS_XYmUj4x03gCb3cAsLL2Dn8eWXEVC09iFhGeXIDr4RyET5LMV48gNENGlecz13579muhNBOuJrfRTKPhmu2uv1hnWezR91ZKdPZgn-_xfgMCtm7EiRWmD7PZmXXXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=nP8CP0wVNK8HjbHucBYrLfW60TYy1f1q95nT0H4G7HVu3R76sfkkU5OpvHPO-3A-6inlaiLZqrWwSK8xBXs6tN4dvKbeG2BNt4lNC73cEr9sERKJMc7oEVHPxYj5JvnJC_7jEdKGf3b8LZKa4tighAdrexHP_1aUoUrzs_errkDxyRZTZxD6NeMyHK3C2dYGQhk_QQAXveZDcSXrvjPqYoi511RYIOzLGokaJhJtqmutWldBzrJ-8RkI_DqPN4Mk4sdkczgfuRzSvCOzj_-1XIIDacilR6Z3ANFWYrNyiJeZ_jSLNMjikUSyeSiQOwE4j_McfTnCAb8R2hNwAIJ16A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd22e2bf5b.mp4?token=nP8CP0wVNK8HjbHucBYrLfW60TYy1f1q95nT0H4G7HVu3R76sfkkU5OpvHPO-3A-6inlaiLZqrWwSK8xBXs6tN4dvKbeG2BNt4lNC73cEr9sERKJMc7oEVHPxYj5JvnJC_7jEdKGf3b8LZKa4tighAdrexHP_1aUoUrzs_errkDxyRZTZxD6NeMyHK3C2dYGQhk_QQAXveZDcSXrvjPqYoi511RYIOzLGokaJhJtqmutWldBzrJ-8RkI_DqPN4Mk4sdkczgfuRzSvCOzj_-1XIIDacilR6Z3ANFWYrNyiJeZ_jSLNMjikUSyeSiQOwE4j_McfTnCAb8R2hNwAIJ16A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از کشتی کانتینری هدف قرارگرفته در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152608" target="_blank">📅 11:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152604">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
واتیکان : پاپ لئو چهاردهم به سرطان ریه مبتلا شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/152604" target="_blank">📅 11:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152603">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e813e99f5.mp4?token=UZiiakJ4HHQhJRreJ84-YiK430mXlRXt_HGrJvjtC96UD9bY6AlXq9rp2bvshTarliBzYmMmObINXOE5sEVTyfcCp-fY9ej5BnKUxzmTITB6DZEeKzcaAvO45gCX-stB7wsZIriUxDGdJ7QAtrPfbIkoDf7QQDG40H8SEHbyzj97m5WSorJCKpNTa7nVh9vmr2Nfe1KPOEhI8jsmq26hokqgflWUjZUMMG4wcQNHi5dkSSe5sSZX5liSsbt-kXRdekj9-zIrCJnuzT-kII303xyUbX8CmdfN6PT7K5b8_qTwTDHqNI3HfzoVx2wmSkc52zVPZb-cMeG5nfDQV7cCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e813e99f5.mp4?token=UZiiakJ4HHQhJRreJ84-YiK430mXlRXt_HGrJvjtC96UD9bY6AlXq9rp2bvshTarliBzYmMmObINXOE5sEVTyfcCp-fY9ej5BnKUxzmTITB6DZEeKzcaAvO45gCX-stB7wsZIriUxDGdJ7QAtrPfbIkoDf7QQDG40H8SEHbyzj97m5WSorJCKpNTa7nVh9vmr2Nfe1KPOEhI8jsmq26hokqgflWUjZUMMG4wcQNHi5dkSSe5sSZX5liSsbt-kXRdekj9-zIrCJnuzT-kII303xyUbX8CmdfN6PT7K5b8_qTwTDHqNI3HfzoVx2wmSkc52zVPZb-cMeG5nfDQV7cCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم دود برخاسته از تاسیسات آرامکو در شهر جبیل در شرق عربستان طی حمله حوثی های یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/152603" target="_blank">📅 11:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152602">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
استانداری هرمزگان: تاکنون موردی از فوت سرنشینان لنج صیادی که صبح امروز مورد حملهٔ پهپاد ناشناس قرار گرفت، گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/152602" target="_blank">📅 11:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152601">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❗️
هر لحظه احتمال جنگ و قطعی اینترنت هست
🔼
اگه میخوای همیشه وصل باشی میتونی از بات زیر یه سرویس تهیه کنی
👇
@VOXNET_BOT
@VOXNET_BOT
مورد اعتماد
✔️</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152601" target="_blank">📅 11:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152600">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2a0bfc52.mp4?token=bOdOhzY-jph3iCcEI9fU_optqxCO3dQEptcft7uUAWD4blK27cqpei7APoFUHoEho3q4qzGhlGbaLvmoknknK9qcVn5Cub9CuBUi7IEjXijEKYqRWkSNnRjZIkk4aLdf5DEXrgfxyFabGa9osbPcZrbdA61uoo0NW8mUy-Se_77gj9K9QhWA96uzKYT6RMoTy4gym1ziWK2ScRYsMavZdLPpnGKGwVBWncEIodTvApMCqu2DodJQAr9TAIOzpY3K83-di7D8MwjNf2KpQbsdw60haLmpHwuodZVo7IGxiq_ti2YPZZ3Ti-2Sk5JlkdnIK7S50u6MIKNR2jRpjhkdNJ5kJpA7_UqNHGBga74SSzpbMh_xsDgA7SrsAPfTvDQK2Fiy6gr4j6CTvTGixyX5k8VAdGV6XNlmZ37q2Jlro_sV1Kj-WiKcQk9U2-SE5YDO4OFTAIAM5K5_Z86LK7TCw7FmMzFx4xOqHjwyr3FUQwZ5nSAxSKaWRe42H3TRvZGBjlvOEwqMH39Yx82RwOrOQ3oty8_oU2-RpwCdz0if7cJy0d-C5C-26M5ypJvrOrnD64rRwIcnTd4SZHaJlnBdBiFr-2uYiyAXqvX61G_ZsRS2LHYgpxJrMatUXYvPucS44Hd4mQdW3T1LGwdnZyFUoKH7sm-dIET_UmeMGdkorc0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2a0bfc52.mp4?token=bOdOhzY-jph3iCcEI9fU_optqxCO3dQEptcft7uUAWD4blK27cqpei7APoFUHoEho3q4qzGhlGbaLvmoknknK9qcVn5Cub9CuBUi7IEjXijEKYqRWkSNnRjZIkk4aLdf5DEXrgfxyFabGa9osbPcZrbdA61uoo0NW8mUy-Se_77gj9K9QhWA96uzKYT6RMoTy4gym1ziWK2ScRYsMavZdLPpnGKGwVBWncEIodTvApMCqu2DodJQAr9TAIOzpY3K83-di7D8MwjNf2KpQbsdw60haLmpHwuodZVo7IGxiq_ti2YPZZ3Ti-2Sk5JlkdnIK7S50u6MIKNR2jRpjhkdNJ5kJpA7_UqNHGBga74SSzpbMh_xsDgA7SrsAPfTvDQK2Fiy6gr4j6CTvTGixyX5k8VAdGV6XNlmZ37q2Jlro_sV1Kj-WiKcQk9U2-SE5YDO4OFTAIAM5K5_Z86LK7TCw7FmMzFx4xOqHjwyr3FUQwZ5nSAxSKaWRe42H3TRvZGBjlvOEwqMH39Yx82RwOrOQ3oty8_oU2-RpwCdz0if7cJy0d-C5C-26M5ypJvrOrnD64rRwIcnTd4SZHaJlnBdBiFr-2uYiyAXqvX61G_ZsRS2LHYgpxJrMatUXYvPucS44Hd4mQdW3T1LGwdnZyFUoKH7sm-dIET_UmeMGdkorc0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خاتمی: مسئله فلسطین رو خود فلسطینی‌ها باید حل کنن و ما نباید به جای اونا دخالت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/152600" target="_blank">📅 11:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152599">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ ویدیوی سه‌هفته پیش رو بازنشر کرد: «مردم بزرگ و سربلند ایران، لحظه آزادی شما فرارسیده است».
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152599" target="_blank">📅 11:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152598">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
اکسیوس به نقل از مقام اسرائیلی: نتانیاهو گفته ترامپ بحث درباره احتمال حمله به ایران پیش از انتخابات را مطرح کرده، نه او
🔴
بر اساس این روایت، ترامپ از نتانیاهو پرسیده «آیا اسرائیل در این حمله مشارکت خواهد کرد یا خیر؟»
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152598" target="_blank">📅 10:55 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152597">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">⭕️
فوری/صابرین :حمله آمریکا علیه قایق‌های ماهیگیری ایرانی در نزدیکی سیریک، در جنوب ایران.
🌎
@ForioNews</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/152597" target="_blank">📅 10:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152596">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
نتانیاهو: ما اسرائیل را به قدرتمندترین قدرت در خاورمیانه و یکی از قدرتمندترین قدرت‌های جهان تبدیل کرده‌ایم
🔴
آنچه در کرانه باختری رخ داده یک معجزه است. یک معجزه.
🔴
آنچه قرار بود به یک دولت فلسطینی تبدیل شود، امروز به آن تبدیل نخواهد شد.
🔴
این اتفاق نخواهد…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152596" target="_blank">📅 10:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152595">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
روسیه شب گذشته و ۲۴ ساعت بعد از اعلام آتش بس ترامپ با موشک‌های بالستیک به تأسیسات انرژی CHPP-4 در کی‌یف، پایتخت اوکراین، حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152595" target="_blank">📅 10:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152594">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نتانیاهو: ما اسرائیل را به قدرتمندترین قدرت در خاورمیانه و یکی از قدرتمندترین قدرت‌های جهان تبدیل کرده‌ایم
🔴
آنچه در کرانه باختری رخ داده یک معجزه است. یک معجزه.
🔴
آنچه قرار بود به یک دولت فلسطینی تبدیل شود، امروز به آن تبدیل نخواهد شد.
🔴
این اتفاق نخواهد افتاد زیرا ما اجازه نخواهیم داد.
🔴
تقریباً هیچ کشوری در خاورمیانه وجود ندارد که از ما کمک نخواهد.
🔴
و شما را شگفت‌زده می‌کنم: تقریباً هیچ کشور غربی وجود ندارد که از ما کمک نخواهد
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/152594" target="_blank">📅 10:34 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152593">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55840225a.mp4?token=PvdvvZjpm-AsXIkXsMto85VUSmnE3o5mSss3iTnXVuqGcsEZPzGYbP56bLko9VwPkWLNFeHtCplmbCtKoOXN3EhsNG2rdNS_AjvQjT4Qsp52Z_ecrBN-b3tEYY6dNaKItofUTJnoStYM2TyQlI9TN3g7APTQsKeGAh0M_4C-TUt2b0wzPvHLC0J5_t5qXqwlW0m2Yk8w2ZoO5qUodGy9ZCMXgIz63CxG8Wi267Co3KGa6EckvH3D5KWCM4N36nqWb7fRD8jc3sNO15G-Hlago-_MNHPbsonTB9uh48mPBJxicPvuLZVjvak3AQG2lCiLFaDaTK9WdvZpJ9cxt6iqTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55840225a.mp4?token=PvdvvZjpm-AsXIkXsMto85VUSmnE3o5mSss3iTnXVuqGcsEZPzGYbP56bLko9VwPkWLNFeHtCplmbCtKoOXN3EhsNG2rdNS_AjvQjT4Qsp52Z_ecrBN-b3tEYY6dNaKItofUTJnoStYM2TyQlI9TN3g7APTQsKeGAh0M_4C-TUt2b0wzPvHLC0J5_t5qXqwlW0m2Yk8w2ZoO5qUodGy9ZCMXgIz63CxG8Wi267Co3KGa6EckvH3D5KWCM4N36nqWb7fRD8jc3sNO15G-Hlago-_MNHPbsonTB9uh48mPBJxicPvuLZVjvak3AQG2lCiLFaDaTK9WdvZpJ9cxt6iqTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش ترامپ به اعتراض حین سخنرانی اش: اوه به نظر می‌رسه با یک بچهٔ لوس طرفیم! نیروهای انتظامی حسابی حالش رو جا آوردند؛حالا باید با گریه به خونه برگرده و بره پیش پدر و مادرش که به من رای دادن!
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152593" target="_blank">📅 10:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152591">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf60973ff7.mp4?token=T37KdQdmPPCclZ843Q7KZC9P2BV_0lpI9DB_KX8E7Cxjo30ec9kLx9CcwI7i4LpfpGn4pvR6Cjz8OjWolOviJow6apXs_r0Mgc2zdBtMl3UfwDQWmkRppfeTDA_PAWQfUdP0WkObU1jR92bLAYXT2vm6GyNo2LlBUcHKFfbzzGmvWoBJNiiYCLZ2g9aIPjCl4yPmjfYbI98Lb8rRwpxO7PF8bbfp41Fz5ARVfJp3CxMzHzWRlyuoXx7HK-25vrx_vsmah0W5KHv0WzgDPsHTZrKchwDxuoHC2nRfxOhnsK-2lOkmZ_jqT1BbRR03ttDtlTJY8rayRTsNeTPG4Sxp6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf60973ff7.mp4?token=T37KdQdmPPCclZ843Q7KZC9P2BV_0lpI9DB_KX8E7Cxjo30ec9kLx9CcwI7i4LpfpGn4pvR6Cjz8OjWolOviJow6apXs_r0Mgc2zdBtMl3UfwDQWmkRppfeTDA_PAWQfUdP0WkObU1jR92bLAYXT2vm6GyNo2LlBUcHKFfbzzGmvWoBJNiiYCLZ2g9aIPjCl4yPmjfYbI98Lb8rRwpxO7PF8bbfp41Fz5ARVfJp3CxMzHzWRlyuoXx7HK-25vrx_vsmah0W5KHv0WzgDPsHTZrKchwDxuoHC2nRfxOhnsK-2lOkmZ_jqT1BbRR03ttDtlTJY8rayRTsNeTPG4Sxp6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">️️️
👈
اعلام وضعیت قرمز در شیلی به دلیل طوفان و رعد و برق
🔴
طوفانی همراه با تگرگ و بادهای شدید، برق نزدیک ۴۰ هزار نفر را در استان سانتیاگو شیلی قطع کرد.
🔴
سازمان هواشناسی شیلی به دلیل این طوفان و رعد و برق شدید، وضعیت قرمز اعلام کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152591" target="_blank">📅 10:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152590">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
هم اکنون هدف قرار گرفتن یک پالایشگاه نفت متعلق به شرکت آرامکو در شهر جده عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152590" target="_blank">📅 10:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152589">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=Vi8q74PNUMhF1eWspBfSdyyMhltidei4hCrK65vkxnhENba__HDBtkWTLkUfXSYFubaSZf8w6W-9YoHZRrDSEtZFNYhqLo8L8z1rs_ysG_zK348LREkoUBVYwWutUg1wIdn_GXqp-C9OywAYCfwBlgVsa0az7meI2qhzKND-Q26J5JArhf4E4qs3EQTO-ZuJjavdBPJqZGl9JjKVyG2YgNfgQf5a1XMIYZ5wTwAxLEZOevTKkyHXZT3gGVgi1ZuFLZ3-9oK5Q-tSfUznrpfhRvm4nGvUh_IbuqkDxpRAiVWjKK-TS_Vs2BW-nK7wNYv6uBdpamHolqgdn1oV3LU1xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8ff56bcd.mp4?token=Vi8q74PNUMhF1eWspBfSdyyMhltidei4hCrK65vkxnhENba__HDBtkWTLkUfXSYFubaSZf8w6W-9YoHZRrDSEtZFNYhqLo8L8z1rs_ysG_zK348LREkoUBVYwWutUg1wIdn_GXqp-C9OywAYCfwBlgVsa0az7meI2qhzKND-Q26J5JArhf4E4qs3EQTO-ZuJjavdBPJqZGl9JjKVyG2YgNfgQf5a1XMIYZ5wTwAxLEZOevTKkyHXZT3gGVgi1ZuFLZ3-9oK5Q-tSfUznrpfhRvm4nGvUh_IbuqkDxpRAiVWjKK-TS_Vs2BW-nK7wNYv6uBdpamHolqgdn1oV3LU1xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو نخست‌وزیر اسرائیل: حالا، این یک رژیم دیوانه‌وار جمهوری اسلامی است. تا زمانی که بر سرپا بماند، تلاش خواهد کرد تا بازسازی شود.
🔴
تلاش خواهد کرد برنامه هسته‌ای خود را دوباره احیا کند. تلاش خواهد کرد تا دوباره ما را ویران کند، حزب‌الله را بازسازی کند و حماس را بازسازی کند.
🔴
برای ویرانی این کل دستگاه، ما باید این رژیم را سرنگون کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/152589" target="_blank">📅 10:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152588">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
قتل خونین کارمند فروشگاه هفت در تهران؛ خواستگار جواب رد را تاب نیاورد!
🔴
دختر جوانی که کارمند فروشگاه زنجیره‌ای هفت در محله دولت‌آباد تهران بود، مقابل دوربین‌های مداربسته یک بانک با ضربات چاقو به قتل رسید.
🔴
بررسی دوربین‌ها نشان داد خواستگار سابق دختر پس از مشاجره، با وارد کردن چند ضربه چاقو او را به قتل رسانده و فرار کرده است.
🔴
متهم که چندین بار با جواب منفی دختر روبه‌رو شده بود، پس از فرار به چابهار توسط کارآگاهان پلیس آگاهی دستگیر شد و به قتل اعتراف کرد.
🔴
تحقیقات درباره انگیزه دقیق این جنایت ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152588" target="_blank">📅 09:53 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152587">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
هم اکنون هدف قرار گرفتن یک پالایشگاه نفت متعلق به شرکت آرامکو در شهر جده عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152587" target="_blank">📅 09:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152586">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وال استریت ژورنال: انصارالله با استفاده از قطعات وارداتی از چین، در حال ساخت موشک‌های بالستیک میان‌برد پیشرفته است
🔴
این گروه قطعات تخصصی جهت ساخت نسخه‌ای از موشک ایرانی «خیبرشکن» را وارد کرده
🔴
شرکت‌های چینی به بزرگ‌ترین منبع تأمین محموله‌های رهگیری‌ شده‌ برای انصارالله تبدیل شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/152586" target="_blank">📅 09:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152585">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
عربستان: زخمی شدن ۴ نفر در ریاض بر اثر بقایای موشک‌های رهگیری شده توسط پدافند هوایی
🔴
خسارات مادی جزئی به ۱۵ خانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152585" target="_blank">📅 09:32 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152584">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b835bc2e1c.mp4?token=Loev6bo23iTipPj-bIpyT-AI6HPM-ROd80NiKmwoAtV7k9-K2azG-q4b7kLLoe63nfZ4oQKQELZ-APuJuBGjxcDloMHRbwGocZRJ6yujFUBn1Kb6mscbeAx_40l-JJeMCn9EEfJ2CRE7KnvxNVKc3_ZbqiNLiwftLAE9blOgdvlqZBh8PL7QBGf7r0FIHxg8ps2l-XZN18p7l27Opi5EQiLj-fpv4ioSkeXT4gMZLbG76yzrv-DWIrzalbjOBdLD50Ld455xf9NauIRX9mEOaRqv8AcuXMXVeTSHNEyAUmbcUe5YAccbfgIQd0qHAAoXFE3aPu_qsi4uXzU6cYm8VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b835bc2e1c.mp4?token=Loev6bo23iTipPj-bIpyT-AI6HPM-ROd80NiKmwoAtV7k9-K2azG-q4b7kLLoe63nfZ4oQKQELZ-APuJuBGjxcDloMHRbwGocZRJ6yujFUBn1Kb6mscbeAx_40l-JJeMCn9EEfJ2CRE7KnvxNVKc3_ZbqiNLiwftLAE9blOgdvlqZBh8PL7QBGf7r0FIHxg8ps2l-XZN18p7l27Opi5EQiLj-fpv4ioSkeXT4gMZLbG76yzrv-DWIrzalbjOBdLD50Ld455xf9NauIRX9mEOaRqv8AcuXMXVeTSHNEyAUmbcUe5YAccbfgIQd0qHAAoXFE3aPu_qsi4uXzU6cYm8VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل ناگهانی در منطقه گورخا، نپال، خانه‌ها و پل‌ها را با خود برده است
🔴
پنج نفر مفقود شده‌اند، در حالی که صدها نفر به سلامت نجات یافته‌اند. عملیات نجات و بشردوستانه ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152584" target="_blank">📅 09:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152583">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
بلومبرگ: مقر شرکت نفتی آرامکو عربستان در حملات موشکی انصارالله هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/152583" target="_blank">📅 09:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5VZwIQKuvqjx822UrgLE4yy807D5RU8RDASpHLdSEsb_30p41tx872YYf5zPOOm3n2U4CLpxlh-fAWT-eoykNmk2wwIY0VjE7jmffEzXfGeYpnHl5UQkN0-_-vw4RpyifbJj_SGQJqYqFK4fceEE60YUVUDoe64GAwZJhGNMQ36PuXrR4gqjOUPMSMj4hL23APIHg3LFOjTO6mtnhEeVUJoWSE0E-wOrhl3QZsOZKbcKFfiU-oogqCbV2znFlhW3s7eoxMRh3ltyRgSu_nnZty4ZkFcIn4x7pmKmpJmCzWh2kTPp6LynhEJP3OEFX10Z5lrp5CKi52w6V7ikzMCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازداشت مهندس سعودی در شرکت سازنده چت جی پی تی به اتهام جاسوسی
🔴
پلیس فدرال آمریکا یک مهندس ۳۵ ساله سعودی به نام «عبدالرحمن الفوزان» را به اتهام نصب دستگاه مخفی ضبط صدا در یکی از اتاق‌های جلسات محرمانه شرکت اوپن‌ای‌آی، سازنده چت‌جی‌پی‌تی، بازداشت کرد.
🔴
بر اساس اسناد دادگاه، این دستگاه برای ضبط احتمالی گفت‌وگوهای محرمانه مدیران درباره فناوری، برنامه‌های تجاری و تحقیقات این شرکت نصب شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/152582" target="_blank">📅 09:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152581">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
سید محمد خاتمی: نظم موجود جهانی، نظم ظالمانه‌ای است، اما باید آن را به عنوان یک واقعیت ببینیم و برای تأمین منافع خودمان، در درون این نظم فعالیت کنیم
🔴
اینطور نیست که بگوییم راه نجات ما، پذیرش نظم لیبرال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/152581" target="_blank">📅 09:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JXOXx8gKxNVmOm9Ttrc9i_C47M1Qp2MCpiMSycOnHQIgYDpyNmeUCb4HM2nIy1eDQjqtp8gYeq84Pi7MQ9x-h4xFCib9wxlHLTCOTzcdk_w2YvKB_XNa3UxujL8LqFS_ms8-xk5tHeLOkY_C6YeX1mSkGzB63GjK41Rkbb9HY39yYkcmBw1tDDMz6hs0h7rQU2x--vvF8Zw58XaXqczlWTxPwR4P6LO6zUVMns2OPbpwDfrgkfrfSkDL35sA0jzVTOdZma30VKQttYTxDGpgaP7ZyRokd1pxylPItmnAvexCm4oDZOG4b0pq5EGXUUEvgR30YTYhp3hc6RNKdStz3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eiEhqJGk6e2jWKrYgERjMtOhl6MLSjHIX4uT8H0hW-CkSl_17uEhppihn-11zQplVS7QOk0v8KUHlQJNo1z-DVS_ywidqf1__TQhizOfiz0VbxX4LIb8NJGs5Cl27wO3GN-nj_sOmYYPlKf-N-NFdhJZNWNcf1OVNvyzHtDHm-_23Zd4qo4qC0OFU01wvNCuMCF3_rIySmh2kg2dLLWTNGqNEBZtLMhDE1vFS4agVTdCEvrpBSp_XXukPfrLDk2SQEvBGQ4V795K5_4mo83pHHjiY_HNCOaYtVLYh7eLY5-qNbpcUsTPA2_G0eaAEBKgmlV4P7u_2iBUYRSFRs60AQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ساعاتی پیش؛ منابع عربی مدعی شدند: یک پل هوایی نظامی گسترده از سوی آمریکا به مقصد خاورمیانه برای انتقال نیروها و تجهیزات تقویتی نظامی به منطقه برقرار شد
🔴
طی ۲۴ ساعت گذشته، ۱۰۵ فروند هواپیمای نظامی در منطقه رصد شده‌اند که شامل موارد زیر هستند:
🔴
۱۰ فروند هواپیمای ترابری نظامی از خارج منطقه وارد شده‌اند:
🔴
۳ فروند فرانسوی
🔴
۳ فروند آمریکایی
🔴
۲ فروند بریتانیایی
🔴
یک فروند عراقی
🔴
یک فروند کویتی
🔴
همچنین تحرکات هوایی زیر ثبت شده است: ۸ فروند هواپیمای ترابری نظامی منطقه‌ای
🔴
۴۵ فروند هواپیمای سوخت‌رسان
🔴
۷ فروند هواپیمای جاسوسی
🔴
۳۴ فروند هواپیمای ترابری نظامی
که در داخل منطقه جابه‌جا شده‌اند
🔴
یک فروند بالگرد نظامی
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/152579" target="_blank">📅 09:09 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61fc96e515.mp4?token=aXtbPWtIN4XqAMQMBamyTE3ymegQ523k0hemdw9eDnYWnwolnIPSccz-kAbPJZ2vyLu6r5Nx0dA8MQ9q7D5jAvc69Gwjw2bAkQVfunKZncEAx03VKxUnfR9rHWIpqvH5eafPP5e5u2HScB-9UhDLGPL6GGlovGTr2m3cAJF09Pxiy0MNMgQRLdd5efT-J3RLNXLujAwlkeMc8iuMkISKDp0Lv-wOR89K-tlPuslEjN8lxbSExm5RmiL28ZW84xADtkqZYA5YWOhM4HBxsvvwS6QLGYqH9qrOrniPDLnY6gXWqD2lkSlU_h1c4F_Is-ioCVG26YVbw_TV0bEyFYMfBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61fc96e515.mp4?token=aXtbPWtIN4XqAMQMBamyTE3ymegQ523k0hemdw9eDnYWnwolnIPSccz-kAbPJZ2vyLu6r5Nx0dA8MQ9q7D5jAvc69Gwjw2bAkQVfunKZncEAx03VKxUnfR9rHWIpqvH5eafPP5e5u2HScB-9UhDLGPL6GGlovGTr2m3cAJF09Pxiy0MNMgQRLdd5efT-J3RLNXLujAwlkeMc8iuMkISKDp0Lv-wOR89K-tlPuslEjN8lxbSExm5RmiL28ZW84xADtkqZYA5YWOhM4HBxsvvwS6QLGYqH9qrOrniPDLnY6gXWqD2lkSlU_h1c4F_Is-ioCVG26YVbw_TV0bEyFYMfBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش عجیب ترامپ به ماجرای کشته شدن یک فرد در پارک‌وحش یورک‌شر انگلیس توسط ببر
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152578" target="_blank">📅 09:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152577">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF1rebonpB8xCN9NPKa1Qd7WvEGIhbapo1zFdttUGQ7rBxFuEkgr81MstrIQvVWMX-O5KmEEwtRhdwqaBzRW1vaK23pog4Px3673MqawCIz5-d0xtPyKde2VSYRFAJp_xSuqpYN7u1L5bs6h663tMTosx8HMYRtRryaY1Nz00E5UoZOymB0EvD5JU1umxVdWvKam2PcXZzjo6oJY82CzLZT3MS73xVbk_1mvNP5PJpmErPLMDPZFelwRuTwafpKqEP9IKJ1XYA8lQ2sjV7hLzI7bWUrKNh43OR2m2ExrpoLd_PBeh6fCJJkq7pRj1mmdWqL-1KVq3eZzF3aw3xAbLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رهبر کره شمالی موشک بالستیک قاره‌پیما با قابلیت رسیدن به خاک آمریکا را به نمایش گذاشت
‏
🔴
رهبر کره شمالی، از موزه صنایع دفاعی این کشور بازدید کرد که در آن یک موشک بالستیک قاره‌پیما با توانایی رسیدن به خاک آمریکا به نمایش گذاشته شده بود.
‏
🔴
رویدادی که یک روز بعد از آن رخ داد دونالد ترامپ، رئیس‌جمهور آمریکا، از احتمال دیدار با رهبر کره شمالی در سفر برنامه‌ریزی‌شده خود به آسیا خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/152577" target="_blank">📅 08:56 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152576">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPHiu08T5b5A6VnDIhpgskZRKc4dFhGua97vgsHq5EAayiP5JYoCHX05ty3l3_eqpFd5GnaP3TCnd3mJwIWHEFutCLNHgIIiT5RmZ022CDktw2QHy2xnVv-El5wEbZuYy3HCesPZ2tF9HNOM9i3MGA6ZFVliWgSu7yeHUZ84NAZNrmy4_zbnuiQUv4NoAbDImfHv_6dDNLnnlxf7It_GcvpAgZD1GskxMokWdSfLNg22JFidyqY7_AAJ0xjLZoD75fofR5ZxUJQtbVWOvHnCUK3creE9Q2m5N4U97itdAKiLKQkH5RbnLAeAYSVH8SsIUIBTzbodNcFRO-iOQN6-mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه شهروند آمریکایی دو تا رسید خرید از فاصله ۲۴ سال رو کنار هم گذاشته و میگه قیمت اجناس تو این مدت ۳ برابر شده؛ داریم بدبخت می‌شیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/152576" target="_blank">📅 08:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152575">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
ترامپ: احتمالاً با پایان جنگ، قیمت‌ها به‌شدت کاهش پیدا خواهد کرد و قیمت نفت نیز به‌زودی پایین خواهد آمد.
🔴
ایران در صدر فهرست حامیان تروریسم قرار دارد
🔴
تنگه هرمز باز است
🔴
ما تنگه هرمز را باز کردیم و اکنون این تنگه باز است
🔴
در حال حاضر حتی بیشتر از زمانی که تنگه پیش‌تر باز بود، نفت از آن عبور می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/152575" target="_blank">📅 08:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152574">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae5ed8552.mp4?token=IbJFkeov09aSEOau3_SkL9iYxg_ijz6i_8ETwKdns7yL1Z8hYvOTOKUeI85EXZbhh4CfApk6KWG9P920btgRniQeuGZ-tH75qkzTeAAzBhV62wPi7rljl_OYoF4ih9fQzmsEaKyhrFEz94MTaDgl1yklOSsuNxmptIfB37Pw4xx0A8kSGxTQjZ-fSBgMqYEO8NjB29jNtyaCFhOTVndg20KU0vlDy05E_a4oURTjOiTojSYEe7HdbV4EDFeh98s8huPSmrLOTmy2EUHcGDR-2Eg2J5tOVv36LLK24KOoaDDtmFa9dGhIvbRf3Bx40-TovJgnf4zlMTTJeSnrlM2kRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae5ed8552.mp4?token=IbJFkeov09aSEOau3_SkL9iYxg_ijz6i_8ETwKdns7yL1Z8hYvOTOKUeI85EXZbhh4CfApk6KWG9P920btgRniQeuGZ-tH75qkzTeAAzBhV62wPi7rljl_OYoF4ih9fQzmsEaKyhrFEz94MTaDgl1yklOSsuNxmptIfB37Pw4xx0A8kSGxTQjZ-fSBgMqYEO8NjB29jNtyaCFhOTVndg20KU0vlDy05E_a4oURTjOiTojSYEe7HdbV4EDFeh98s8huPSmrLOTmy2EUHcGDR-2Eg2J5tOVv36LLK24KOoaDDtmFa9dGhIvbRf3Bx40-TovJgnf4zlMTTJeSnrlM2kRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها منتظرند؛ ما درس سختی به آن‌ها خواهیم داد، چرا که صبر ما در برابرشان به پایان رسیده است
🔴
ما درس سختی به ایران خواهیم داد؛ صبر ما در قبال آن‌ها به سر آمده است.
🔴
دولت اوباما میلیاردها دلار به ایران داد؛ در حالی که باید مانع از دستیابی آن‌ها به سلاح هسته‌ای می‌شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/152574" target="_blank">📅 08:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152573">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfa4581b6c.mp4?token=IpWS_xcrZwvBCUH-c-ANnw7-lAPZr1yZTAdEln0R4KwM6bKqfldLTV1pV6WMoKGGv3Imh5yX_HNsUD5BWkAQvlMA5TY3hXAJkxkD4B-rJAWnMUUrFjtmxBnUY098QssKEtkAENBLrFjScYq5GaRCKTPISG6g2A8T5zSlrx4asIjctH8Qg78DF-DP6kVCdHQEHoZLdlyx58BeB2jln0UcVbSSkF30J-ceXzY2mRCmLjvizmF4_MTOITeVXFJir6Awu_a8KC0-wtYEaAwqM9iO7pIUFiZIBDPCcbRI3hcRymtPCWfLJyOP9iA3YubqWCEWNUnFX74gSUYa17gKOQzycw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfa4581b6c.mp4?token=IpWS_xcrZwvBCUH-c-ANnw7-lAPZr1yZTAdEln0R4KwM6bKqfldLTV1pV6WMoKGGv3Imh5yX_HNsUD5BWkAQvlMA5TY3hXAJkxkD4B-rJAWnMUUrFjtmxBnUY098QssKEtkAENBLrFjScYq5GaRCKTPISG6g2A8T5zSlrx4asIjctH8Qg78DF-DP6kVCdHQEHoZLdlyx58BeB2jln0UcVbSSkF30J-ceXzY2mRCmLjvizmF4_MTOITeVXFJir6Awu_a8KC0-wtYEaAwqM9iO7pIUFiZIBDPCcbRI3hcRymtPCWfLJyOP9iA3YubqWCEWNUnFX74gSUYa17gKOQzycw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: صبر کنید تا ببینید ما با ایران چه کار خواهیم کرد
🔴
ما کار بزرگی انجام خواهیم داد. صبر کنید تا ببینید... ما دیگر تحمل این وضعیت را نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/152573" target="_blank">📅 08:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152572">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
به کارکنان شرکت نفت آرامکو عربستان دستور داده شده است امور اداری خود را به صورت دورکاری و از خانه انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/152572" target="_blank">📅 08:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152571">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
فقط 13 روز تا انتخابات اسرائیل و 20 روز تا انتخابات میان دوره ای آمریکا باقی مونده
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/152571" target="_blank">📅 07:40 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152570">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d9062d93.mp4?token=DOj5nKuFvGEa09N72uYUAGrh2NaiDEBAHAHiw096ozmuQYoDplDnB751OuhxNXuB5113D1858Rrc6AXzsPZv3K5O9uAs7AtzbbSxcEzncJ4OXQiDZYpp1A_XU9JnWr1FzTQDzIZv-oAWowyb7bwXLzB9EbVPWiYgO7UW5MDA3vmRdXEB0RFb11Z0kBobH858TEtgcjWdTJf35WUQ6Wj_sP07En7Rf_EilgLJt03fX90cWzRttGSWZBUCkZTMkq7s7E8VIC07LxtlEhFHgHvv2ywzGSsOVD59Wboe33uQJW8UI99YLH3e3VAYADgaFL5nwfjlPFBLY52mjeQYGCthEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d9062d93.mp4?token=DOj5nKuFvGEa09N72uYUAGrh2NaiDEBAHAHiw096ozmuQYoDplDnB751OuhxNXuB5113D1858Rrc6AXzsPZv3K5O9uAs7AtzbbSxcEzncJ4OXQiDZYpp1A_XU9JnWr1FzTQDzIZv-oAWowyb7bwXLzB9EbVPWiYgO7UW5MDA3vmRdXEB0RFb11Z0kBobH858TEtgcjWdTJf35WUQ6Wj_sP07En7Rf_EilgLJt03fX90cWzRttGSWZBUCkZTMkq7s7E8VIC07LxtlEhFHgHvv2ywzGSsOVD59Wboe33uQJW8UI99YLH3e3VAYADgaFL5nwfjlPFBLY52mjeQYGCthEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عبدالملکی، وزیر کار رئیسی: مردم میگن یادش بخیر دوره رئیسی چقدر خوب بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/alonews/152570" target="_blank">📅 07:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152569">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bb5c55db.mp4?token=WURxLuA0SbY3ZEVhzqfhTNKKbYH1rTh4KGJY2CBwPbGhe1vY5zgIO0UR51q0SQBnCqHQRfztCCsZimp9JsuvtE7VBymQ6_32sQGx_eTQMvyogWn3CgUAaU6wwomqWa10Vw5-YzidB-5i-2AYb2iFCQ5SxUBHuw5H3lu5CGtK3Sa5sXV3PSUfMRQNzSGrFl8zWCnD_u7uDbl9fgP3LhJmLPS3xjMvapJJtzaoaKeGy6FZJetpiWjzMDYVlR7C4RiTNdUv47bKryzRG5dCzTlhnvUrmMxkkQE8DRmzyj735ycYEReKe2XDr72Y-fAxoIKxVOo9tb0Merb9JBmijxrOji180ordYwf2ojVvwNp-_Yg7KbUuqG-xw8k0Y1PCA_3XCVgY1XRamMjmWMNVYgBqLTET66ecm96TI0kXDj4hspg3MsA4M91iNjKOlVyQyWrIq20_Y5sbID1TEXcHOKeFVN5889yWmE9FCFyGR9bvpbHbdV3ygQJ5VYM0raTlB1KI4OUYiQg9LIVGkRsq8OrQmjB4Jpq_Lq_VQHgrOgooy2RybdOQR-6jTjrKbzv9MMGy9xDvwqHQ9NgXHc6oqoF7qYWHhsiNb9dNoYKIJvn_kJBYD0G9yPG0Ol9W46jqXw4QuB-8OMIU_yBG27ZlQDfOP9H72pXqrtk7uoVWBX7ZB-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bb5c55db.mp4?token=WURxLuA0SbY3ZEVhzqfhTNKKbYH1rTh4KGJY2CBwPbGhe1vY5zgIO0UR51q0SQBnCqHQRfztCCsZimp9JsuvtE7VBymQ6_32sQGx_eTQMvyogWn3CgUAaU6wwomqWa10Vw5-YzidB-5i-2AYb2iFCQ5SxUBHuw5H3lu5CGtK3Sa5sXV3PSUfMRQNzSGrFl8zWCnD_u7uDbl9fgP3LhJmLPS3xjMvapJJtzaoaKeGy6FZJetpiWjzMDYVlR7C4RiTNdUv47bKryzRG5dCzTlhnvUrmMxkkQE8DRmzyj735ycYEReKe2XDr72Y-fAxoIKxVOo9tb0Merb9JBmijxrOji180ordYwf2ojVvwNp-_Yg7KbUuqG-xw8k0Y1PCA_3XCVgY1XRamMjmWMNVYgBqLTET66ecm96TI0kXDj4hspg3MsA4M91iNjKOlVyQyWrIq20_Y5sbID1TEXcHOKeFVN5889yWmE9FCFyGR9bvpbHbdV3ygQJ5VYM0raTlB1KI4OUYiQg9LIVGkRsq8OrQmjB4Jpq_Lq_VQHgrOgooy2RybdOQR-6jTjrKbzv9MMGy9xDvwqHQ9NgXHc6oqoF7qYWHhsiNb9dNoYKIJvn_kJBYD0G9yPG0Ol9W46jqXw4QuB-8OMIU_yBG27ZlQDfOP9H72pXqrtk7uoVWBX7ZB-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک جنگجوی برزیلی که در ارتش اوکراین خدمت می‌کند، لحظه اصابت پهپاد روسی «گران-۵» (Geran-5) به هتل محل اقامتش در خارکیف را ضبط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/152569" target="_blank">📅 07:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152568">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسرویس ابری ProNet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UzkwUNNo8MzFDPNpQGvUKzegIfGh-r8pX6pFKsAchOPl3xpKfBcVvRbjeFr7P3rz2cOTKY7O5NBNSFMm6lroIjYxSDODhly6rORvGRpGNZkN_WsLGuAfDLTOYE51qqln8OvBrGPTxxOXyAMyZAJ9GmExE3wDvEHEuSWwH4tUvkUVLi4sSSZ55jYfs_uHqhGkns4ZwNiuKs0-Z4_6NYUkXztKPa8AjYEtYpeLLr-EYrFPcX7gyBYFNsJUa-turRLAC-J5U9cOWmgyY1yCJcZKh66THZyeVv5sh5V2IuSpo4yvk_TO7cQr-IG9jr4yLhdWhtBnHmsIf998yA65H6i7Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین فیلترشکن پرداخت به ازای مصرف ایران
🌎
پرلوکیشن‌ترین سرویس ایران
🌎
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🔴
دسترسی 75 سرور با خرید یک اشتراک
🔵
قوی‌ترین تیم پشتیبانی 24 ساعته
🔴
مناسب برای تمامی اپراتورها
🔵
سرورهای ترافیک نیم‌بها
🔴
سرورهای ویژه زمان اختلال و محدودیت
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دریافت مستقیم اکانت تست
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
🟢
مینی اپ حرفه‌ای مدیریت اکانت‌ها
🟢
اشتراک فیلیمو فیلم‌نت رایگان
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/152568" target="_blank">📅 01:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152567">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
گویا بخاطر تسویه دیر به دیر دولت با فروشندگان، خیلی از فروشگاه‌ها دیگه کالابرگ ارائه نمیدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/152567" target="_blank">📅 01:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152566">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3e211b84.mp4?token=S09s7F-LjFKlzNRqN8kswAKcCHZqL4lq-UHhWIj20gl0RJTPcsem-i0woOK4yW5pmXscVL5U53q5Fvsx3LDc77MfkLS31jTknYqYnAOC3BzqYQfZhnYH2QS-Wd9iLuhjqVlJsNjOYzESYHnlub28edC7OTrI3SS2lvi58U6HlDR86CPayYKgU1gWz-JiOpNRxKP4BXl-hBrzZnAPvZITNeR3YiVB3nyAtmseLHxRF0oafoBM1wPjssNQuiv3eB8NjAJRdp9hjhyL_lRU4fSLSJfMHWMvyNUm_ly5yCLyXMb2xhAWDBo2vx1_Di9_kxr5LfFOwLLdlTFN6sfMvnLL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3e211b84.mp4?token=S09s7F-LjFKlzNRqN8kswAKcCHZqL4lq-UHhWIj20gl0RJTPcsem-i0woOK4yW5pmXscVL5U53q5Fvsx3LDc77MfkLS31jTknYqYnAOC3BzqYQfZhnYH2QS-Wd9iLuhjqVlJsNjOYzESYHnlub28edC7OTrI3SS2lvi58U6HlDR86CPayYKgU1gWz-JiOpNRxKP4BXl-hBrzZnAPvZITNeR3YiVB3nyAtmseLHxRF0oafoBM1wPjssNQuiv3eB8NjAJRdp9hjhyL_lRU4fSLSJfMHWMvyNUm_ly5yCLyXMb2xhAWDBo2vx1_Di9_kxr5LfFOwLLdlTFN6sfMvnLL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسن روحانی بالأخره دادگاهی شد
🔴
امشب تو یکی از تجمعات شبانه، سه نفر از حاضرین نقشِ "قاضی، دادستان و حسن روحانی" رو بازی کردن و اینجوری حسن روحانیِ الکی رو وسط خیابون محاکمه کردن.
#توهم
#تریاک
#کصخول
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/152566" target="_blank">📅 01:27 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152564">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZyc2EHQCs8VDRfCwF368V2T8P6R8OacdILVAJ_QHNFAlxCDTKfajosisOyyup_kDYGRb76s2lJnWIi_s9Ts78qvKqY09ncitRYHKOhVWnI3CRYUwRPjWf1Q0-b3TuQFsHLRf_QkiAqCHwt_9jOpyfm9A0wn0gFdwk8yz6npOvCF8Q3yLJCQPtPv1SeW3hG70_OQW0z8PZep8BVBJwybcAfSMAwTQ-hT0AbEp2EwgO716kOZjFUcmVk-PaMJB6Wn6Y1tr5S5rTCjL7vtFdM-vwH33x_GKlpjU7j2hidQn34_36GaQDUWGQDG16lkzinvwfd8QjnRIIttwEICl8d08A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی:حاضرم تمام افتخاراتم رو بدم اما ۱دقیقه جای ملت مبعوث شده تو خیابون باشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/152564" target="_blank">📅 01:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152563">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/152563" target="_blank">📅 01:15 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152562">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
گزارش‌ها از افزایش پروازهای ترابری به اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/152562" target="_blank">📅 01:06 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152561">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-X6akOu5V3uBMDEZObfBgoW_0aPgUB-ZxGaw0eDfC42U4YysPthTvM1AahaUsUiThjfzhVR-jfH9KAL-2oLbVFhmlGi4YWnH5Uo7YITaLX8hZWY5OrJ0xJA83HmgvWO8b5zz7wSaVXqST5UrZAzUvWsEibcB4ybX1PgT3dlePgrHSDLd5PVFMojZ9bt9wt_eaeytAU9fl3l-jbOJoLyeDmo0NXyIo-rOt-qmncXyiLIMTGeVccDS34ja5xB4PNRkI_vs6HiGZ15LOTLWkdLBQIKTCs7rQVRNiNZjVoj971GwuxSMv4m9m5XQdGX7rbpEkKuEu-tMRR4Eyrb_KAG8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازگشت ناوگروه ضربت جرج بوش به دریای عرب
🔴
بر اساس گزارش منتشرشده از سوی USNI News، ناوگروه ضربت شماره ۱۰ نیروی دریایی آمریکا، به فرماندهی ناو هواپیمابر «یو‌اس‌اس جرج بوش» (CVN-77)، پس از توقف در تایلند به دریای عرب بازگشته است.
🔴
این تحولات در حالی گزارش می‌شود که پیش‌تر نیز خبرهایی درباره حضور ناو هواپیمابر جرج واشینگتن و حرکت احتمالی ناو تئودور روزولت به سمت منطقه منتشر شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/152561" target="_blank">📅 01:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152560">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q80XWH4sVChrVF7kHGbVK9s4IYc7XQY43FEMs3S8fsHn775KI3W3AheFl9hcfhJe333hMFQZgUxXqXPXzIdgv99kp9kxuYvz591R5fnJF9JlRDDeoP6gEM8eEelWgjEJwehTS1-0NnlnhwZjMvjO_GPVq4EjRNUyNe0lUyCHKTfL3CwUD5yGKqpaMNbhKxVX9DfNIZaGmEYKpGVQEj9wmgzvnZug0AZVVaS7H8ANoQaPg2RNYaXTwYArCxdjZPETXhi5zIBPjI_U4Dgp6PU1gf9FsYFFWF3i4kCOAlq4hfxp8I2s5WzXD47L9-TxlPBtP431jZWCiulS39FK9NrJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۲۲ مهرماه تولد ۸۸سالگی فرح پهلوی، همسر محمدرضا شاه و ملکه اسبق ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/alonews/152560" target="_blank">📅 00:52 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152559">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-plMo4uXJJpdZmGhIcdv-xb80z-HILxkvoaAxUrZN2uJkr_VAsIc6fCt86J8q7zv9tJ91WTMbGpRhy9s-g9uuYfAwewDGQ68AVx43C3ZjsAk4zBBGaWGYsfUKLNEdhM12RE8AUqVVHjf8H8vfOEOV2RCck8om3YLddG03kW-k00GHHjaZA9JpuHkD4oYsX9zpGL6td7dTQICioOSpiUlmvF985RCT46pKhjw9xNcKDbrdUk7Q65m6g1Z-WXGL_DgpLi_vwx22yBNlUSO_crTDQRiJb8WYPoVCB753rWWliPslOxqxPcdqmOc3g-HYl2xgTLkKOTnXIs1nqMt9NA8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید:
در جلسات اخیر با سران امنیتی و اطلاعاتی، نتانیاهو ادعا کرد که این ترامپ بود، نه او، که بحث درباره احتمال حمله به ایران پیش از انتخابات را آغاز کرد
بر اساس این روایت، ترامپ از نتانیاهو پرسید که آیا اسرائیل به آن ملحق خواهد شد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/152559" target="_blank">📅 00:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152558">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfzEGEXiOH-he1s4Q_TQIOyJqeNOCAC52WT_vXqqaZOCxtv4UDM0wa9p3q9Rao4LpmLnhBBUIwmpkt8304r2P76BXEULwKAaEigdTrZBbQ6Z-eGCKwbo27B5JD-GNnQBaVpCV3kcL5Iu6gJKbSUh6yL_SpsXYXc823DvIXwdPKwU7VFTjjwtJyHznVV-RfeYWxqXZ0SW0xgoushtmqWCnLf93MINmUnRMGK-DzE25j4-FwgcDRg1AadIuHYg2egCPhcOHfUv9TqHm77qn0-uMZeMZ7RJaam_BlQKOxbPiUwPkmKI5snx4uiDOg-gDLJ9lYerlgu197aLv1dEaUE3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع آمریکایی:
هگست شدیدا به دنبال حمله به ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/152558" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152557">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fT3I-KgVyvr9LaO2eGBRBiFGe5KleoCHT2q58857D9BI9_6dhtuiR_ucQD6C2eyDyvyve10QIu6qR3WyMNsjDD_e82VcCve75VFYbmkQITtB9A7gL9IFHNeeNK376lQ8CUu4AuY0dzP5-hQ0okKIHrg1KOt_VeLo6RS8tJuubqjkgBem8qZ61GoXgMJ_CZy5fSPABZTBCEUUloSzknJNKDQd6JpXQUqZaSBUuKAHOcYY8gd7NBOiFH-axKRlueykdHGFJlzCXC1wtgyV4XYhLeoYdXSuslXxHrtzAMfHyGDIpBuGH3AKFGlVlnZl6q1rf89wbxvfXSLF_SAnhXd8sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در روزهای اخیر، شاهد فعالیت‌های نظامی غیرمعمولی از سوی نیروی هوایی اسرائیل بر فراز سوریه و عراق هستیم که یادآورِ وقایعِ پیش از ۹ اسفند ۱۴۰۴ و حمله مشترک آمریکا/اسرائیل است؛ امشب هم دقایقی پیش و برای سومین روز متوالی ساکنان کرانه باختری و منطقه گلیل/الجلیل از فعالیت شدید جنگنده‌ها اسرائیلی خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/152557" target="_blank">📅 00:26 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152556">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
شبکه ۱۴ اسرائیل:
فعالیت‌های اتمی در ایران رصد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/152556" target="_blank">📅 00:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152555">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">⭕️
فوووووووری/لیبرمن: جنگ ویرانگر طی ۷۲ساعت آتی آغاز خواهد شد
🌎
@ForioNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/152555" target="_blank">📅 00:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152554">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=FXVw_xmnXDVzI21axvgPTKuDZFwKTyer-w5fCqg9kPrSCu35ZQ8UXQ0IPEY2f1dOu7BC9NL1lLwGvHzA_ciKKmXn_QA-B7FsTCdIiLrph4t7-f-BVHaLx3uxsA1sd27ybH0X9w3McEHM9BsXQC9HVvozhYsQNVIDRFehhQ9JDdA9MzfmQ260CI-_-J6ad1UI79LzFtWsqIeloUt2kS4HAdJRypUpmVudvDfWVbppViooDavMDZ0P_BefnQUvs2KHlAOclB9vWLtmz9RbenHfeiRC2T_cHVEZZokAvTc8NMDa5i_VzYsj0SHVXKeb_xD6oL0Gcen-AvWr9G5P2XsvCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de41df8bac.mp4?token=FXVw_xmnXDVzI21axvgPTKuDZFwKTyer-w5fCqg9kPrSCu35ZQ8UXQ0IPEY2f1dOu7BC9NL1lLwGvHzA_ciKKmXn_QA-B7FsTCdIiLrph4t7-f-BVHaLx3uxsA1sd27ybH0X9w3McEHM9BsXQC9HVvozhYsQNVIDRFehhQ9JDdA9MzfmQ260CI-_-J6ad1UI79LzFtWsqIeloUt2kS4HAdJRypUpmVudvDfWVbppViooDavMDZ0P_BefnQUvs2KHlAOclB9vWLtmz9RbenHfeiRC2T_cHVEZZokAvTc8NMDa5i_VzYsj0SHVXKeb_xD6oL0Gcen-AvWr9G5P2XsvCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ابوالفضل ظهره‌وند، نماینده مجلس: پیش بینی میکنم ظرف یک هفته تا ده روز آینده جنگ از سر گرفته شود
🔴
نتانیاهو بدون جنگ باید به زندان برود، برای همین چه با ترامپ و چه بدون ترامپ، جنگ را شروع میکند!
🔴
برای زدن زیرساخت‌های ایران ۳ روز برنامه ریختن، با این‌کار نتانیاهو انتخابات را به تأخیر میندازه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/alonews/152554" target="_blank">📅 00:12 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152553">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITOQ--UnimtIWuUF5fQVUaSsyxkVjuLZs-tKpDkyr2lELX6RieQRNr1Ry02g6P_AAKS8zAsZNHpa4y1PLAe09rlMnVmmZX_LSQL6Nmw5gyFvR_hJV_ICaQ0gwTmbT8BCMRYRangyt52AK6JmxcoqCEmo4PqZksvn60BcuLEc1LOeKz79KtJYoy5DMtnWn1OzyQM9cq2XVtV5GFZYAkFT259bElCqZQMvFuYWKB1p0pOQMGzccWozEOqr6ysA5Qwh_iiGERKeAN2p0usXKwscsNoG6Ku0I9gCOwT9FBwO9Lcq_ZN53qu-RgpkrWI6CPO4vzOeeQmhZZ945ZT0YYFrpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آغاز استفاده صداوسیما از نام «دریای کاسپین» برای دریای خزر
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/152553" target="_blank">📅 00:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152552">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / گاردین: گزارش هایی وجود دارد مبنی بر اینکه ایران فعالیت‌های غنی‌سازی اورانیوم را از سر گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/152552" target="_blank">📅 00:01 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152551">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
یک مقام کاخ سفید به الجزیره: اطلاعات مربوط به احتمال حمله آمریکا به ایران پیش از انتخابات میان‌دوره‌ای صحت ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/152551" target="_blank">📅 00:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152550">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HqVocZK8HaxU8BXBFqccCCKsV7d5-JgZWfTdnbYxrS6yU0RimHoRNUmteNp0idKjF_KUi2cuks7rsHL5z3tFoXHrHvvZCzoENErEQll_W_jKXEnZ6cy5IuPr89lKLQg_z7IeTJN6a7jiMyqEGW0lwscnjqtDTQi7VJKY1t07rCvmX_uZnBN-ZgKxNDWCm2i8fWaZUa8z_Z09H03WVYTI7JJpBbIf1WgC20-er8NsspIW2dqeJMRH6iTO4k87ROHIifMAWDxD8BNq_Cl5t5IMCjL1JV10EH3WMg0zTDFWGppolj8Az-wHRPk8FWvo22YgMtsU0Wc3G6JWUiUnc_iTMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توی دزفول چند تا دزد 6 تا بز اصیل افسانه‌ای ایرانی رو از باغ وحش دزدیدن. این بزها خیلی نادر هستن و قیمت بسیار بالایی دارن دزدا‌ رو دستگیر کردن گفتن یکیش نیست دزدا هم اعتراف کردن و گفتن یکیشو کباب کردیم و خوردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/alonews/152550" target="_blank">📅 23:34 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152549">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرگزاری رویترز، به نقل از یک منبع آگاه، گزارش داد که ساختمان مرکزی شرکت نفتی سعودی آرامکو در شهر ذهران، امشب مورد اصابت قرار گرفته است. این منبع افزود که هنوز مشخص نیست آیا ساختمان مستقیماً مورد اصابت قرار گرفته است یا اینکه خسارت ناشی از سقوط آوار بوده است.
🔴
به کارمندان شرکت آرامکو دستور داده شده بود که روز چهارشنبه از خانه کار کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/152549" target="_blank">📅 23:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152548">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
لحظاتی پیش سازمان عملیات تجارت دریایی بریتانیا از حمله موشکی ایران به یک کشتی باری در تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.6K · <a href="https://t.me/alonews/152548" target="_blank">📅 23:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152547">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gxCUWUuc5xBhgjn2BBQNUDHV3hcPqgykdEgwiS_lqD4zCcAjlEdBBETLfAYF-xaDMoSe42sGDfXRJ6ICwmpPXjXg3NieBopAkWgq-gGzGrimPdUC_477psXGotS-ilEwL8iNV7Qptyon9ttAAdTmTajJFDbMibvzV8ypVUDQaEsXDilO3ZdJ5bJ0YpCOvJhYmE3I6bIrF_sZg3EhR1SyFUA-w_BR7ZZHa_oNKVSZfKZVLiDsk0yQNJKx61u1t-rZmpA60U5jrazJi2tcPKk6a7L_P-F1goJ0VyE6nVf98Y79FUp3NUnm2CteoXH217xeRcLDOQpTCSa-aMREDPaxlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
منابع عربی مدعی شدند دفتر مرکزی آرامکو در ظهران در آتش سوخت
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.6K · <a href="https://t.me/alonews/152547" target="_blank">📅 23:14 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152546">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‏
👈
دفتر نتانیاهو، اخباری را که نتانیاهو ترامپ را برای حمله به ایران قبل از انتخابات تحت فشار قرار داده، تکذیب کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/152546" target="_blank">📅 23:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-152545">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVlqcf45Cd52ljXQfWovxp8D5x2KiMWbrPNw_dv6XzVYKwxaPGuqCSXgbjs7IRXigOJhtR6qJQYiI0q9a3a2nMwztGhRcdiTlgw2dkmYXJWDSUytt0XQL9ssQX2z4aATNj5aMGMdev3KQ0zq0EEXvHZq3eO3iahGquPntMkOPT42mD63q8KB8OW_NOh4gsB-z8gjScRCYBUCLLHiQBKp63O35ObxFt2F0ic5dU9NzVEooOp9QIhmLH6TMXTqjpMYqkRDRdL3ZoIRh54SE8rAplHrJB89QwYmrBt5e6YbUsJ8StOeBvfpvMV3CUar3sa8yAKiAmkAwmgcbtrWo049cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
طبق گزارشات دولت آذربایجان بعد از ممنوعیت حجاب تو مدارس، این بار تصمیم به بستن فوری مساجد در سراسر کشور گرفته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/152545" target="_blank">📅 23:04 · 21 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
