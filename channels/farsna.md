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
<img src="https://cdn4.telesco.pe/file/hbooY9dfmkyLpEOMui0V-GmznAQ-wIBT-ZaKHTpn812B_UlRaK5cfoiHvUQSdPnoZy1iyB_c7Zato7jeo-axPVZWcpZjY0HSRQr0HTxzDiQXpmFZU0PSAK-EIAXA6EwZC4xqHRi7zDIuC77G57uWAxec9VCaZZOGH59-JmUrz0thtzJ9qoDbtswma5QIyCYWR7cTJ-2bM45KGtMMuJxwhMcYtgL4JtGx6tIoKT9ITkHKsrWhEdXuLaVznIRWzjFRSkcj5GM7NbDbDJGxNtZmr7cdofDoHsFz_b1LhLQ9DrmhA5YgYzSuxjkGDrZV8mXnggXmopXKBYMsti_cTzNrSg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 10:05:14</div>
<hr>

<div class="tg-post" id="msg-438411">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFPvDGBizfrWbqcvfIHKN8MAcvIewCilZvocN6QDSAV5oEqkfzs7gJGkLiCc3t3VmUks_V7nO7Z5ZWm7MJNDoP0dVQQlfdPB7R75J8IeWivHZWB8NV72wAqh8dir2xaqAq4H7hfiRoJaF5-pGqlorQWsJ_rb7uOeTfRB_W5Y6YSGzE79ElLL8PtRs40fvf-TsCILIB0-EnGIu-ECPuZgFKJEjYpx66odiHNXRRxWGB2c6oF_r_L9HQ2IW57hCmcms8-3JIJHDbJHdZ8OWoMs3l-bvj5t4-wD3DysrjIqS8fky97UP8uE2VK2nEThzpjlz1Krk94fZqukeOcEUjBxzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: شهید شیرازی تجسم امانت و ولایت‌مداری بود
🔹
فرمانده قرارگاه مرکزی خاتم‌الانبیا با حضور در منزل شهید شیرازی، فروتنی، تواضع و اخلاق حسنه را از ویژگی‌های برجسته آن شهید برشمرد.
@Farsna</div>
<div class="tg-footer">👁️ 768 · <a href="https://t.me/farsna/438411" target="_blank">📅 10:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438410">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8405a51a28.mp4?token=YCt4G2JaypC9rI-KfrLlEyZ4XlI_uwc_wZV2ITWl7cBiJUHbN6DU5iQEVNup4a7V3Vu_YmoNz37Uo73ODwHpW4KGppaUJsZm7hDKBsDRPkTjg-wmwGSUdl_cvxi2GbXL4RFINE2lcaveqEnKdiMcPsKw4ADXfJDoyb0sVk0yiK51lwx6RCmB0_4x7pj-UeFALVG1kJqUhVgSENjgyziPwL558gVNpOqcPbY0po3mndhViCWrfCqQop_cU9ucpz17-hsa4eDzQkWtJXWecFUT9pz49swaNK7ymYxkjac9iyo7VnJZikHuONE064dQWAm9i7sf00ktf6XWdFj9MHbicA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8405a51a28.mp4?token=YCt4G2JaypC9rI-KfrLlEyZ4XlI_uwc_wZV2ITWl7cBiJUHbN6DU5iQEVNup4a7V3Vu_YmoNz37Uo73ODwHpW4KGppaUJsZm7hDKBsDRPkTjg-wmwGSUdl_cvxi2GbXL4RFINE2lcaveqEnKdiMcPsKw4ADXfJDoyb0sVk0yiK51lwx6RCmB0_4x7pj-UeFALVG1kJqUhVgSENjgyziPwL558gVNpOqcPbY0po3mndhViCWrfCqQop_cU9ucpz17-hsa4eDzQkWtJXWecFUT9pz49swaNK7ymYxkjac9iyo7VnJZikHuONE064dQWAm9i7sf00ktf6XWdFj9MHbicA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فواد ایزدی: ایران نه غزه است نه لبنان
🔹
کارشناس مسائل آمریکا و بین الملل: پیشنهادم به مسئولان این است، من اگر جای آنها بودم اعلام می‌کردم که هرباری که از این به بعد به ایران حمله شود تنگۀ هرمز یک ماه بیشتر بسته می‌ماند.
🔹
اگر با این نوع حملات به‌صورت جدی برخورد نشود تهدیدها ادامه دارد.
🔹
ما به آمریکا امتیاز نمی‌دهیم ایران نه غزه است نه لبنان.
@Farsna</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/farsna/438410" target="_blank">📅 09:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438409">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91b67c9b9a.mp4?token=m39xial_m58wAciVIuxH02kOYIZV_oduDXYH_0pBaCFxEpm72kfBYC9QTVBngbrzesjfEIO3N8PCpBaM8MJMP4FgAUIpkzqbMW1Vnj4bHKPu_sPM7w4Mg8rl75JH5UONaY4YE558yNIVHNLu_oJs_ImxtcO1dXDlCAtgDv9ruF8WV9crYXfv95Tyvli3akedIx6xX65yKD39mbnr_ZSh7qE5yDLpF4vg18U31a6lWc0OGaw55UTglTuxDGWXOQ49MH3JLdYxtQdQIE-3ibolGRLtE3HzuGjljdjh4-TQUjv8Rui5qIqOg2mcq1PbIOpS6GOfVWlWpNCsIv56F5oelg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91b67c9b9a.mp4?token=m39xial_m58wAciVIuxH02kOYIZV_oduDXYH_0pBaCFxEpm72kfBYC9QTVBngbrzesjfEIO3N8PCpBaM8MJMP4FgAUIpkzqbMW1Vnj4bHKPu_sPM7w4Mg8rl75JH5UONaY4YE558yNIVHNLu_oJs_ImxtcO1dXDlCAtgDv9ruF8WV9crYXfv95Tyvli3akedIx6xX65yKD39mbnr_ZSh7qE5yDLpF4vg18U31a6lWc0OGaw55UTglTuxDGWXOQ49MH3JLdYxtQdQIE-3ibolGRLtE3HzuGjljdjh4-TQUjv8Rui5qIqOg2mcq1PbIOpS6GOfVWlWpNCsIv56F5oelg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاری کویتی در محضر قرآن رسوا شد
🔹
قطعهٔ «عاشت یدا ایران» با صدای یونس شاهمرادی قاری ممتاز ایرانی، در پاسخ به آهنگی علیه کشورمان که مشاری العفاسی قاری مشهور جهان عرب خوانده بود، منتشر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/farsna/438409" target="_blank">📅 09:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438408">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eTy_PRZ8PzOoE5PpgkqM_RATtWceoS9ME9x90C2WZOs6l4w7nX4J7oBmNLCB_yBuJ4UPyy7Fwm0EkvubfekhuR1LvOjSUb4-Ey0kVZZRRaBeCW_px7aGc41Z_Loh1oX4WiSsFVFBwHnlV2cVyW2GCCpb5A1xqcWrrlI_QOPwVE18FyrslbmbHgQCtjjaVYblqyZ1BTha4xcjU1vEkC5EGz3Q3BSDCBr0_DTTUPbcPOkqLWE9qgFicsOuKOj0N0MwlWshjmd6v_k7HYaOA2e55QklZVyx5nedlOt7Wk-NOr1STeaVUarx0hBTPUOVY9-wcmD-Ki14mZt9m_uDvkRX6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شباهت به ترامپ، بوفالوی بنگلادشی را نجات داد
🔹
یک گاومیش آلبینوی نادر در بنگلادش که به‌دلیل موهای طلایی و خاصش به «دونالد ترامپ» معروف شده، پس از مداخلهٔ لحظۀ آخری دولت، از قربانی شدن در عید قربان نجات یافت.
🔹
این حیوان ۷۰۰ کیلویی برای ذبح فروخته شده بود اما مقام‌ها بعد از پدیده شدن آن به‌دلیل شباهت مذکور، با ذکر نگرانی‌های امنیتی مانع این اقدام شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/438408" target="_blank">📅 09:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438407">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخط رهبری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/350d4094b6.mp4?token=rZegTYq268IqKw9pWIBzV-V07pG426KdCHPscfCLl4VKY8JvmGBTbQhNG-wHRCBiqCDQxXspG0bh2bwlmchNKAxjoOMQOPYMfpHkKuz2Lt60u0y50FE9hH2JGndCSFX4MRxzrGr3oXDnYO8kZC2Nz5n6rbQ2OVOnS-x4Rc925Isavr50ITK7XWfjnj-HkseSLGp5PESmwfitsi6SN8B5Q971onzbvPNhNXrAoOXRdvBS0FUcL7Ddqvp3iVf5977rW9-zLYZr0C1A3sMwTaiWwYus2Lc0UMgdt58V-ekASUxz9042liUlaEE2uzW0s_iyigZsQRTE3LjMv9eHm27MNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/350d4094b6.mp4?token=rZegTYq268IqKw9pWIBzV-V07pG426KdCHPscfCLl4VKY8JvmGBTbQhNG-wHRCBiqCDQxXspG0bh2bwlmchNKAxjoOMQOPYMfpHkKuz2Lt60u0y50FE9hH2JGndCSFX4MRxzrGr3oXDnYO8kZC2Nz5n6rbQ2OVOnS-x4Rc925Isavr50ITK7XWfjnj-HkseSLGp5PESmwfitsi6SN8B5Q971onzbvPNhNXrAoOXRdvBS0FUcL7Ddqvp3iVf5977rW9-zLYZr0C1A3sMwTaiWwYus2Lc0UMgdt58V-ekASUxz9042liUlaEE2uzW0s_iyigZsQRTE3LjMv9eHm27MNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گُلی که خانم
ضعیف‌الحجاب به آقا هدیه داد!
@rahbari_plus</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/438407" target="_blank">📅 08:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438405">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f4b20d15d.mp4?token=g5lTDMRklXXlAEhKx2BneA7voSNtReNou1p47MXnxP9HQ2rdsi0ebFmREEb5YQ-eIK-eJbRFYwRkOoQJXQtsmtrNmYScQy03a8gUIwnSBGs2aogi0rpdnJ8BXH8wwvtoes7WjESN8fir4evk_oEWVWtKi0Ao4I2MVlZTBGUGKsekexi__zpc0-TjyVRV0aE09zSudCupYiS-BFbblIVFRTzM2RwUnKPPvPowe1SBxE79mDWBr8QR0nHyZAS2lSZ9k67Q0FtM9VnNkMwrILtpZg78R4u2nPkqf9zgkDUKhcGf_ahuaH9C_uRVwdsdh898_sSYgMkzUjko5H_UzasrTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f4b20d15d.mp4?token=g5lTDMRklXXlAEhKx2BneA7voSNtReNou1p47MXnxP9HQ2rdsi0ebFmREEb5YQ-eIK-eJbRFYwRkOoQJXQtsmtrNmYScQy03a8gUIwnSBGs2aogi0rpdnJ8BXH8wwvtoes7WjESN8fir4evk_oEWVWtKi0Ao4I2MVlZTBGUGKsekexi__zpc0-TjyVRV0aE09zSudCupYiS-BFbblIVFRTzM2RwUnKPPvPowe1SBxE79mDWBr8QR0nHyZAS2lSZ9k67Q0FtM9VnNkMwrILtpZg78R4u2nPkqf9zgkDUKhcGf_ahuaH9C_uRVwdsdh898_sSYgMkzUjko5H_UzasrTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی: امروز و فردا در کل کشور دما افزایش خواهد یافت.
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/438405" target="_blank">📅 08:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">نهاد مدیریت آبراه خلیج‌فارس، در فهرست سیاه آمریکا
🔹
در ادامۀ دشمنی و مواضع ضدایرانی آمریکایی‌ها، دولت ترامپ از تحریم سازمان تازه تأسیس «نهاد مدیریت آبراه خلیج‌فارس» خبر داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/438404" target="_blank">📅 07:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438403">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
سپاه یک پایگاه هوایی آمریکایی را هدف قرار داد
🔹
سپاه پاسداران: به‌دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه‌ای در حاشیۀ فرودگاه بندرعباس با پرتابه‌های هوایی، پایگاه هوایی آمریکایی به عنوان مبدأ تجاوز، در ساعت ۴:۵۰ دقیقه هدف قرار گرفت.
🔹
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع‌تر خواهد بود و مسئولیت و عواقب آن با متجاوز است.
و ماالنصر الا من عندالله العزیز الحکیم.
روابط‌عمومی سپاه پاسداران انقلاب اسلامی
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/438403" target="_blank">📅 06:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438402">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ماجرای درگیری شب گذشته در شرق هرمزگان؛ تبادل آتش بین ایران و آمریکا
🔹
منابع خبری به خبرگزاری فارس گفتند که صداهای انفجار بامداد گذشته در شرق هرمزگان و حوالی تنگۀ هرمز در نتیجۀ تبادل آتش بین نیروهای مسلح جمهوری‌اسلامی ایران و نیروهای آمریکایی، و فعال شدن پدافند رخ داده است.
🔹
براساس این گزارش، چند فروند شناور آمریکایی تلاش داشتند بدون هماهنگی قبلی از تنگۀ هرمز عبور کنند که با واکنش به موقع و قاطع نیروهای دریایی ایران مواجه شدند. ایران پیش از این هشدار داده بود که هرگونه عبور از این آبراه استراتژیک منوط به هماهنگی با مقامات ایرانی است. این شناورها پس مواجهه با نیروهای ایران، ناگزیر به عقب نشینی و بازگشت شدند.
🔹
در پی این اقدام آمریکایی‌ها به سمت یک پایگاه نظامی شلیک کردند و در اطلاعیه‌ای رسماً به تجاوز به خاک کشورمان اعتراف کردند. با این حال، ارتش آمریکا بلافاصله اعلام کرد که این تبادل آتش را نقض آتش‌بس جاری نمی‌داند.
🔸
گفتنی است تا لحظۀ تنظیم این خبر، جزییات دقیقی از میزان خسارات احتمالی از سوی منابع رسمی اعلام نشده است.
🔹
در دو روز گذشته در پی ماجراجویی های ارتش امریکا، درگیری‌های پراکنده‌ای در آب‌های خلیج فارس گزارش شده بود.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/438402" target="_blank">📅 06:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438401">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuyspg2NMW2T2L6M_UuyvuWCzRW76czSJpcGlml5AzBBW9m9L-ETXXbYuyroPecNK-cf_RemMRWSvvh8tz_qJrp5JIeXIyT4N07sFIqhb7Mh_lRnVT1ooolZK7LHuk0YmEgAV-hpADY6oEaZss49w_YZF5qS-v2vyJYwvPEu684p9Cy9w5-5FwvqRPlmiuT-y5-JcB8CLUgaTO09Zv7VgZKi91ZbX-XFMPl_0xS0bkZ1qSG2Euwhf4pXrQz7nRS-mDWB-pr5SMPwSzxS2LxLAXlfzGNs5fcTHKlIsoTFtrYOG9gqCL3jojQ9wGDed_rKcGi3bD03AyeTaE-461Dfqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان بازداشت برای وثیقه، با سامانۀ جدید قیمت‌گذاری برخط
🔹
قوۀقضاییه: با راه‌اندازی سامانۀ جامع وثیقه، دیگر نیازی به ارجاع پروندۀ وثیقه به کارشناسی و بازداشت متهم نیست، و قیمت‌گذاری وثیقه به‌صورت برخط انجام شده تا در صورت کفایت، پس از توقیف سیستمی، فرد بلافاصله به منزل بازگردد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/438401" target="_blank">📅 05:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438399">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بیمۀ کامل معلمان مدارس غیردولتی اجباری شد
🔹
محمودزاده، معاون وزیر آموزش‌وپرورش: با پیگیری‌های سه‌ساله در مجلس، مصوب شد که معلمان مدارس غیردولتی باید به‌صورت سی‌ساعته و با بیمۀ کامل در ۱۲ ماه سال تحت‌پوشش قرار بگیرند.
🔹
عدم رعایت این قانون تخلف محسوب می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/438399" target="_blank">📅 04:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438394">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm4HjlrXyEPW8Z4HG99ZI5vRQjaqpsKf8KeZAG4l_GKlbyXzAb9HzTIVWD98VrW9IFTVRUPaCtMicTXeqs_bzx8vUnNXCug4uQJAPYWp8eaSpLeATmyjEwLOesHD4bF6mU-l7Afsjb34T76aQT3OJJ2RMUYsFKeYdo7N2_WSTrRxducQOGBP2Ywn3yQkm3j7kumd9CmfwUEgyUuC5OjB4_5g0NsasgS5IDKrdCZBmMemPMFYzDour6orogvvAaJxJi7irgytovS2QIUqHSh1qlmzSmwomTK7SeGL6yvlAgZTKvxjqEiYYi8ErNlr56YOpDguyDVtWQrBSDc5jCpP5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lj3kqKv_FJnSSTiz0pUaKNDK4LXgURVzHMXDiqgETso0rhD-0mCDErXrSwoNLYMK3XL6k36BjWGjlOpnCOL1HyCPjtsqs0raQ2hCXIb9WUepi8b4lU2pLxQR7KrKGq-BmJS8xxzU7f9K02OHBbF6nHya6XnkHUOSR9GJcuu_YSjKeVi1XbBJYGTNFHvytRjVPUBx_KW6eg8ZL7OS3ES04T_yvlWMGyL9CYyF9J8GAb0HIpUw3mosP0cQbDWLLobK4mg3bTP0EdSg-0eb7AbMJIqCAph72IyE0EpcJHUONa2MwUlhmm2Opr246EbES4leD8CQVo6hNodLhg_N0VShmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rbY6pNF8VRyXMuNwWuCBQz8_29x0_hhLAv2m1VmrZlY8cV4wp36-PorWo-CmyKNE18NQQCC4bP9Fqf1eXl4ZfJCi2FBICYvhXAKB1nHVza3Iog4UYTcFNcvRlVzTg7EtdHHHScha1V6-LcRG_Y7cL3OflH7rax5kyjyhi7CtEe7uJMnU9csq0fln37uth_CXS6_udZF6GuGQUHQZrZT-gE4_hMyd_lDW3qNOUFdaRfXKmzKMp_iMcW9dxhGxdahcNdXCAQvSRDh1gDGhgXuqMzZNEObQAFCj9yldn1v3zkbxz36Oz65tpyDov4g_UG38fnIx9TJzg4uYW38fTxplcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ptx16LX6AXYqW4F9TNLfhd_AVecDCXniNadXGKMkAgpzgKlvv0JrB8bdmG5H6d_tdR8utDs3FLXDkgguF0WS_KnhoRqsZ1hYAeDjairGHA68dz7TTCum66OlR1FM2BftLFpnrIabIetYm0GG88uGhibaB2u065hiH1hbMIo-6XPdDSFyei1Y-hfgoVOHEdidCP3ByuHfWeX-q45-uHLd57RuKwEd-flC9JlORfMI_MUMyss086IF4xuvBzPq9wWSy0A0cHDZu3OgpeDWOsKs0X8kxWoPekt9imqK5sLLfwFWsy9arh5N_6ZodFUFxDOguL9iT4o3JuiMaLgrvkOo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bye6yJJp5FjJGmjdsGHCGeTB72m9oLacBws_T7zW7ByBNjH5G1l9suKIBjvbsSn1KVYFVjubY4u6L4aQj5QwgE_UAnI9KIaFXeXAzLsdmLIXPX3FyjWXPDbFtI7Xk-noHPJ8e3tQhG4tl7t22S2J-bclm8a-r4DddNkn4w08hXbkSlsXMtvTW5r7bGtxsRRKvWK7ofUC6Tz2FUkrZ5k08GYqcgDg3kSU_58K9wnamwawpHpS328wBCnyWVERG5MHy2kafmSPA5FVb08v4rQxLkNmeYb38NjX2ggCw84nsIlC3RYWvVCVEMeUY_o8GGo8ZPH_kq6mIrXOujBsY_dz7Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسیر ۳۷ کیلومتری تندرستی در منطقۀ ۲۲ تهران افتتاح شد
عکاس:‌
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/438394" target="_blank">📅 03:43 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438393">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jBfbJbYvBbhJS5rXriMSwdw29dxlZ1IlKlRlQeTjO8otLnpUqRdLECv2r4xdR7UHptD2MDUciSqKvlmRNwRGTGfCUbGTxSu33t2NLijYjNvDGGgyv2lbsztzXk110O-0asEZpoh8HfHgdVDklZjE8LereCy1muVbEpccdKeSnWcw0HY2A8ItqTIZEqe100Ah6C1M0TmQ6eAdEoAJ1dhVMhNT3ldeNAQN788HEW75cCUmCg038WCUFpYqBtHBS-uZF3nrxW9hr3UN-vM48K3FBLOwXP0wBPzFdKRwPrN0e4tPHyP8Mmr6ywd2u3rZ8hDw2IWpgQQ89busMvdpxsH48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیّران در سال گذشته ۱۲هزار زندانی آزاد کردند
🔹
ستاد دیۀ کشور: در سال گذشته ۱۲ هزار و ۶۹۷ زندانی مالی غیرعمد با مجموع بدهی ۴۷ هزار میلیارد تومان آزاد شده‌اند.
🔸
هم‌اکنون حدود ۲۱ هزار و ۶۷۸ نفر در انتظار حمایت خیرین هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/438393" target="_blank">📅 03:17 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438392">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
🔸
طی ۴…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/438392" target="_blank">📅 02:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438391">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">صدور احکام جدید بازنشستگان تامین‌اجتماعی، از هفتۀ آینده
🔹
تأمین اجتماعی: صدور احکام جدید بازنشستگان از هفتۀ آینده به‌صورت رسمی آغاز، و احتمالا تا ۱۵ خرداد به پایان خواهد رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/438391" target="_blank">📅 02:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438390">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
شنیده‌شدن صدای ۳ انفجار از شرق بندرعباس
🔹
حوالی ساعت ۱:۳۰ بامداد صدای ۳ انفجار از شرق شهر بندرعباس شنیده شد.
🔹
هنوز محل دقیق و منشأ این صداها مشخص نیست و پیگیری‌ها برای مشخص شدن آن ادامه دارد.
🔹
همزمان برای دقایقی پدافند شهر بندرعباس نیز فعال شد.
🔸
طی ۴ روز اخیر نیروهای مسلح کشورمان یک پهپاد آر کیو ۹ و یک پهپاد اوربیتر‌ دشمن آمریکایی صهیونی را در منطقۀ هرمزگان منهدم و همچنین سامانه‌های پدافندی نیز یک اف ۳۵ و یک پهپاد آر کیو ۴ را نیز رهگیری کردند.
📝
اخبار تکمیلی متعاقبا منتشر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farsna/438390" target="_blank">📅 02:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438389">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🎥
شب هشتاد‌وهشتم خروش جان‌فدایان ایران در قزوین
@Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/438389" target="_blank">📅 01:50 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438387">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1180119de.mp4?token=VW1kG_7Xr8O5Gpk3eZYYlejyto6ukiL2idg4y0ZBMq8Gf2mYCR7rBo8Dg8Bhy3coq7_rNflwvYnF4EPdfTGWaiEfmRt_8GGFA340cdudJyAMy6KUxRA-1-TY1QqNQop6RtrniBEPWit6KGvE1ohsw_ggvIwlsEqtEGHfLob7tkFIvhrC1pg9DST3A71orAYWI0WGP-Sey99hqLaOHrmFbQIqx6WmbUIz8DHKfIUe8ZBFuq7Tl_vXAMnaqzO7GuOAeTXE8eFTc-8CNW520XvZFqkvoCa88Qtw-t4pG1zW83xW6sJ8mHVUqV2x90riyKFrPLxh8tR2_EjdBvZTeXvNEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1180119de.mp4?token=VW1kG_7Xr8O5Gpk3eZYYlejyto6ukiL2idg4y0ZBMq8Gf2mYCR7rBo8Dg8Bhy3coq7_rNflwvYnF4EPdfTGWaiEfmRt_8GGFA340cdudJyAMy6KUxRA-1-TY1QqNQop6RtrniBEPWit6KGvE1ohsw_ggvIwlsEqtEGHfLob7tkFIvhrC1pg9DST3A71orAYWI0WGP-Sey99hqLaOHrmFbQIqx6WmbUIz8DHKfIUe8ZBFuq7Tl_vXAMnaqzO7GuOAeTXE8eFTc-8CNW520XvZFqkvoCa88Qtw-t4pG1zW83xW6sJ8mHVUqV2x90riyKFrPLxh8tR2_EjdBvZTeXvNEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات رژیم‌صهیونیستی به شهر «صور» در جنوب لبنان
@Farsna</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/438387" target="_blank">📅 01:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438383">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
شهادت فرمانده ارشد کتائب القسام تایید شد
🔹
جنبش مقاومت اسلامی حماس رسما شهادت «محمد عوده» را تایید و لحظاتی پیش، طی بیانیه‌ای اعلام کرد: در سوگ شهید قسامی، فرمانده بزرگ مجاهد محمد عوده (ابوعمرو) که استوار و سرافراز در میدان‌های جهاد به فیض شهادت نائل آمد،…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/438383" target="_blank">📅 01:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438382">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeZI7IdwfNJNXEMyZKNNIxOOg-XQdJBR0beQR7hMB-Eol4eDzJV502iWvAh5WOj0UfS22ineAASehc0wIlpfDkiwBwiG6h6tR69fL4piSZ8_apBpkDxD6ctLgTXs5PoWpbbwyqnO_mmb1f3oPAHblLEegviD0r4EyHTMJSryx1ppSyXZvozNARPm_vm5MjyxLerVkd1jN5Q1iOn9SsD6ljxUNG5fNBpCdlqb8sabqIxBGncVyjQhUcqmdg1eTQrtG_rXjx5-8Fvl0-vOYXj9Qz16tGLKT0MsO7YHaehP8vCW6eErpwulnBdkaRvX9c69vt91CFvFjjb4NaQ0M1Ft6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعلاً خبری از خط‌زدن مصدومان از تیم‌ملی نیست
🔹
رسانۀ تیم‌ملی ادعای برخی رسانه‌ها مبنی بر خط‌خوردن هادی حبیبی‌نژاد به دلیل مصدومیت را رد کرد.
🔹
رسانۀ تیم‌ملی دربارۀ این گمانه‌زنی‌ها نوشت: کادر فنی تیم‌ملی مطابق با زمان‌بندی و مقررات اعلام‌شده از سوی فیفا، تا آخرین‌مهلت قانونی برای بررسی شرایط بازیکنان، ارزیابی‌های پزشکی و فنی و درنهایت انتخاب فهرست نهایی ۲۶ نفرۀ تیم‌ملی فرصت خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/438382" target="_blank">📅 00:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438381">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvEr55GalstLgDGtbihdkaaAJat3ZN_h48Tl69ocgiVTjnTnoHa1xvXCcpFURvNbZHHDr1AZr_HDhSKvmGj-PgMrFC1f1ZpN72RFm-163muwt16xIyJhnppocSHGb-ssakiHlKGpalzMvfn48DCmTiK6F-tf_uBmtNS8zz74p_HiM1qJPRHJ_wPiAI2uxsxYKEsV4zg8FFtgWqOj7_6gnnv1VjTlG02FCd49sJzZBsxVC73qZRfZf70W9CHAa9dmyxl7ouazSV4moUJy7wdnjrXRpLmaiIVslWIleuZXunmjDnb8kcgcMqClgqq7Og6c9v9rTbcfZemRRwf91JphGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روند پرداخت خسارت خودروهای آسیب‌دیدۀ جنگ سرعت گرفت
🔹
بیمۀ مرکزی: تاکنون خسارت بیش‌از ۶۶ درصد موارد ارزیابی‌شده، به‌طور کامل پرداخت شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438381" target="_blank">📅 00:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438380">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYKRRypSbrJGlimsULL5iEsGmcRYJ6sN3CAgmSYsGitHQMeOF9RXy2KqBqHDuBjDYjrCkAWBZ9WWKdmfK2Etwp_lpwZAmAWsDAEIM3xQDgejg8GZ4-TLks2OMHg3ZfpOIKCFoKtlIYD4Udb1ekbXXBxyuPDMiWZ0vnsdumeAQYol48Rb3XxUxyD2KThJKhTk_N739DyxUBJZ_wFErO6_zVwqF07Av8nrWNrVDmOOwWQHoNKfzGj3Nh2D3dM0yTZasb_cnIs5LSBEiPXq-bhEWq3snIC9ncl7rDtAEcP164R045SwBxuJ2ZVCxFvw0WiBcog_3uXrRIEQKqTRGFFVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دزدی اثر انگشت از عکس‌های سلفی
🔹
کارشناسان امنیت سایبری هشدار داده‌اند که هوش مصنوعی می‌تواند امکان استخراج اثر انگشت از سلفی‌های معمولی را فراهم کند.
🔹
براساس این گزارش عکس‌های با وضوح بالا که در آن انگشتان در فاصله کم‌تر از ۱/۵ متر از دوربین قرار دارند، ممکن است جزئیات کافی برای بازسازی اثر انگشت را در اختیار مهاجمان قرار دهند.
🔹
در سال ۲۰۲۱ نیز پژوهشگران نشان دادند که تنها با یک تصویر از اثر انگشت، نرم‌افزار ویرایش تصویر، چاپگر لیزری و چسب چوب می‌توان نمونه‌ای جعلی برای فریب برخی سامانه‌ها ایجاد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438380" target="_blank">📅 00:14 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438379">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVimRDScxu_nRF7sRfULDznYXT-LRspR_nJIhIT9lz-Pg-HzX4xMkMSIdPMlYp7ENxw1lm2MIqvcipaYpEw0tmyGThFdI_NDku7Bu4W1nD16Sf4w3qwub3MYsY55LnKKni9HWNKNRU3XODpTsdctauCMrhEj0Z9Xa7716xvjfJl_V9NA8GF_XGfvF33GUR8SV6xYhdwAlJ-4YcCJrz0Tit-JZ8Yf5xzMdlewUaHumdYDU-SLrKHFcjdzKNy75DJSkxLXkRxErNh3tiZhpXECfAllwb33sEMwsoN5XX_gTfK0Pov3ysT8nCsCNKu1SkoNvwCB8BZwp84omONbmnEqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یخ ابهر و سلطانیه
🔹
روزی شخصی ساده‌لوح نزد مولانا عضدالدین آمد و سؤال کرد: «یا مولانا! یخِ ابهر سردتر است یا یخِ سلطانیه؟»
(ابهر و سلطانیه ۲ شهر نزدیک‌به‌هم در زنجان هستند).
🔹
عضدالدین که از بیهودگی و سردی این پرسش شگفت‌زده شده بود، بی‌درنگ پاسخ داد: «سؤالِ تو از هردو سردتر است!»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438379" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438378">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🎥
تجمع هشتادوهشتم مردم آستانۀ اشرفیه این‌گونه بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/438378" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438377">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/271065f03f.mp4?token=TfPs_9W-8yPP_rYOdaBILk6iki-JAYLXfGvsE06oAFpjEyGjE_DHauquGVgVKzJHbs0NjqM2sXC-2pkUtFw17QSQFZlJMhZA27QtvW0SOh-flfPhuj5p5xJG1qF_uQWowUNio24yNObkyxv4mpebSDAM0bsPdvE4Fnr6L4uCUisfc49tio0bEsj40PiYkmKZ7vAuDDHEV5iU3algOW2vgkLvxUINYwDKKeFHQIkQKsDZ98vtPhJTF7a5neSYYQ9WFJ5VjZta5SLbe9Dpu-nEFW4LnicaCgRZXN7T7Q2XSUbTA3aRe4P24g1cn4inMDjsC9ZTpysRIJl4JRiuGpdR5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/271065f03f.mp4?token=TfPs_9W-8yPP_rYOdaBILk6iki-JAYLXfGvsE06oAFpjEyGjE_DHauquGVgVKzJHbs0NjqM2sXC-2pkUtFw17QSQFZlJMhZA27QtvW0SOh-flfPhuj5p5xJG1qF_uQWowUNio24yNObkyxv4mpebSDAM0bsPdvE4Fnr6L4uCUisfc49tio0bEsj40PiYkmKZ7vAuDDHEV5iU3algOW2vgkLvxUINYwDKKeFHQIkQKsDZ98vtPhJTF7a5neSYYQ9WFJ5VjZta5SLbe9Dpu-nEFW4LnicaCgRZXN7T7Q2XSUbTA3aRe4P24g1cn4inMDjsC9ZTpysRIJl4JRiuGpdR5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تجمع مسلحانه مردم در هرمزگان
🔹
مردم شهرستان رودان هرمزگان امشب سلاح به دست در تجمعات دفاع از میهن حضور یافتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438377" target="_blank">📅 23:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438376">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🎥
تجمع پرشور مردم کاشمر در موج ۸۸
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438376" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438375">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">عضو تیم رسانه‌ای هیئت مذاکراتی ایران: سفر قالیباف به قطر درباره آزادسازی ۱۲ میلیارد دلار از اموال بلوکه‌شده، موفقیت‌آمیز بود
🔹
سعید آجرلو: براساس پیشرفت‌های فنی که در قطر رخ داد، قرار است بلافاصله پس از تایید تفاهم میان ایران و آمریکا بخشی از دارایی‌های بلوکه‌شده ایران به‌صورت غیرقابل برگشت در دسترس بانک مرکزی قرار گیرد.
🔹
در بطن تفاهم ۱۴ ماده‌ای چند اقدام ملموس و عینی گنجانده شده که برخی از آن‌‌ها این موارد است:
🔹
در دسترس قرار گرفتن اموال بلوکه‌شده.
🔹
معافیت تحریم‌های نفتی، پتروشیمی و مشتقات آن.
🔹
رفع محاصره دریایی.
🔹
اگر این اقدامات توسط آمریکا انجام شود ما وارد مرحله دوم خواهیم شد و در غیر این صورت اساسا اعتمادی برای ورود به گام‌های بعدی نیست.
@Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/438375" target="_blank">📅 23:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438374">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5501a453.mp4?token=oxfbyk60D0CTQrv7vGugor3ySExOV6IQ19vt3nqb1HVlWq5Ew-ElAu_WAW1aZ91Y0Q8ARbYyDNN77o1m4RSBD6OhairNMJ22d62KWxRBdbVOSwzz_95jwEI93s1o6lIP-_TdmPtzQQByMyDtg1iWlOe8UBxBnKaI9HkwZnA9j53FkG1sHUem3Z930y1X_AkrRHt9lWUvi0aqWxBH2QBXTW6SL8tPiGnYFcaaT5ONJdKmV4QOlnVb0Wt_pBHa2Nk0KkbZjG11Bt_XGCju8Tnao5ypghxovQjxcx0RF0cqdOrgnfP3Dhl_c0dp4zYLz9NnVmmd6Y3vvtKpW3oOcQjYHEAku110m1K878e3U3f3tN9UPhaNRLP0UlS5KPk-V2mBG-xhfaVkTYp4k51O9t9DBoEZkNOQRyY2amvFBb3Vl8hOZhgYcb1VP3LOiTE8na8_3pB078WViP0QMxMPal6d2_6KWUVmH_xc75ct2tSG4RhvhxdTv2VXfVEbSK8-lGtMiIDhxul4YLIGIrbn8twVWGsMzSbwHL5U0gOXhpXNNy_xPSGSLirS-YoG-RPpfk_VlgqTfclHxoEZ-ZV48iO8Qw1tkh-FCDJQ3ZRqr75jqQkCag7Lna8GY-B3Wpqug7LD7Q5LCJLn5iDN2wFmDdIlkdHKRAbVKXBRP9chMFPgjnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5501a453.mp4?token=oxfbyk60D0CTQrv7vGugor3ySExOV6IQ19vt3nqb1HVlWq5Ew-ElAu_WAW1aZ91Y0Q8ARbYyDNN77o1m4RSBD6OhairNMJ22d62KWxRBdbVOSwzz_95jwEI93s1o6lIP-_TdmPtzQQByMyDtg1iWlOe8UBxBnKaI9HkwZnA9j53FkG1sHUem3Z930y1X_AkrRHt9lWUvi0aqWxBH2QBXTW6SL8tPiGnYFcaaT5ONJdKmV4QOlnVb0Wt_pBHa2Nk0KkbZjG11Bt_XGCju8Tnao5ypghxovQjxcx0RF0cqdOrgnfP3Dhl_c0dp4zYLz9NnVmmd6Y3vvtKpW3oOcQjYHEAku110m1K878e3U3f3tN9UPhaNRLP0UlS5KPk-V2mBG-xhfaVkTYp4k51O9t9DBoEZkNOQRyY2amvFBb3Vl8hOZhgYcb1VP3LOiTE8na8_3pB078WViP0QMxMPal6d2_6KWUVmH_xc75ct2tSG4RhvhxdTv2VXfVEbSK8-lGtMiIDhxul4YLIGIrbn8twVWGsMzSbwHL5U0gOXhpXNNy_xPSGSLirS-YoG-RPpfk_VlgqTfclHxoEZ-ZV48iO8Qw1tkh-FCDJQ3ZRqr75jqQkCag7Lna8GY-B3Wpqug7LD7Q5LCJLn5iDN2wFmDdIlkdHKRAbVKXBRP9chMFPgjnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم نور مازندران در موج ۸۸ تجمعات ملی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438374" target="_blank">📅 23:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438373">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPxADsO9Pi3uTn4RcOZw6RKXu1nzl-lUMSbGUVMG0zhNk3n01UnhkZhwEal7CMtVufXhf4iqiivELHs4Jna_h2-tEIinB_FO8HciAfA5jlZL0Vnsff46U0Q3J6Q2r7JMGVQSuq3CBkAybInUn3ITHwI6OdarPoJnlrUm5EaGQANcRM1Uvr8GczYcPhI8WxfWQ6wZXIJn6Zh_M14udw6E17mEPA37tSzYquZ901WBuIBV3-e62E0wVFaT-9_y4c2AUFYqZRX2U-3bPnZw6asTpGlkXluOIrQxjSurpJtQX0xb-4wDCezxAHaxC88vxvNhclHIScKeOBODTTTggZTB0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سعودی‌ها از ترس جنگ خانه نمی‌خرند
🔹
گزارش پلتفرم «انترپرایز ایام» نشان می‌دهد پس‌از آغاز جنگ علیه ایران و درگیر شدن عربستان در آن، ‌‌ حجم معاملات مسکن در کل عربستان ۵۳ درصد و در ریاض ۸۳ درصد کاهش یافته است.
🔹
گزارش‌‌ها تخمین زده که بروز تنش‌های نظامی، هزینه روانی اضافی ایجاد می‌کند و  خانواده‌ها را به تعلل و به تعویق انداختن تعهدات مالی وادار می‌سازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438373" target="_blank">📅 23:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438372">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fad9f09d9.mp4?token=AxUr1FgLFe2FeYFi0fNPUIqRMOOPMPG2zMNwQiQ6fk6VWmw4iKgPlGW-2bjz8x8X4YkbGktGNOuFXPT0vaVL1_eGMxyYPBJjJO42_2CI_absaN5pQsWVXHZ8ZU-IdPBxbsW4VnASKoHbdEurYnYlfbKlntWRFZrCZebLY7j8lh2lpPOFRkcjuaBdIl3VPNf2Doe4t15-wQPEMpYW9QXB0smvEepzj6KvV1Y55NjMEdwWWzBxo-fNPJRODzoHPTK1pXT0n8qgqtTME3lvMVggKlEwR5wshqwqLzp9TVVccKAnzqM1S0UBRtAyY5ARwUzjEYgtJ6vqP09z5gAZkf1sag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fad9f09d9.mp4?token=AxUr1FgLFe2FeYFi0fNPUIqRMOOPMPG2zMNwQiQ6fk6VWmw4iKgPlGW-2bjz8x8X4YkbGktGNOuFXPT0vaVL1_eGMxyYPBJjJO42_2CI_absaN5pQsWVXHZ8ZU-IdPBxbsW4VnASKoHbdEurYnYlfbKlntWRFZrCZebLY7j8lh2lpPOFRkcjuaBdIl3VPNf2Doe4t15-wQPEMpYW9QXB0smvEepzj6KvV1Y55NjMEdwWWzBxo-fNPJRODzoHPTK1pXT0n8qgqtTME3lvMVggKlEwR5wshqwqLzp9TVVccKAnzqM1S0UBRtAyY5ARwUzjEYgtJ6vqP09z5gAZkf1sag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کودکان ایرانی به قرارهای شبانه در تجمعات کف خیابان عادت کرده‌اند!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438372" target="_blank">📅 22:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438371">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d15d5b129.mp4?token=GCasLifVb3NeQsy578BTik1wbeZg2zWVZ8q6E-e6laGEdcKu6a7J8NmQNm4QMoxOrwaE3J534ifpHmkDgpDU2m71lsURpKqZgkClMtFsUJ0GT-ORhScCle-IPCPmZgKk88fFXzTxE6_58_YHc_Ckfs6vPH39bjdBQCDp4ptwDhQxGJ5yI4Gb6BaKtoK-sFsfCc2b-sEMu8zdfG_5MxA_DkaLrHkyGOQvgNrITJ7TEx4-Pfd7n2Uql7upy_8xllkSeum7NS7e-KHKLMM_syCjkr0jLjxY6w89kH9ERqA3uedWI2eKIy-agvFs8RxyKaMy6w29rE6qEMXYqFqNP7gtiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d15d5b129.mp4?token=GCasLifVb3NeQsy578BTik1wbeZg2zWVZ8q6E-e6laGEdcKu6a7J8NmQNm4QMoxOrwaE3J534ifpHmkDgpDU2m71lsURpKqZgkClMtFsUJ0GT-ORhScCle-IPCPmZgKk88fFXzTxE6_58_YHc_Ckfs6vPH39bjdBQCDp4ptwDhQxGJ5yI4Gb6BaKtoK-sFsfCc2b-sEMu8zdfG_5MxA_DkaLrHkyGOQvgNrITJ7TEx4-Pfd7n2Uql7upy_8xllkSeum7NS7e-KHKLMM_syCjkr0jLjxY6w89kH9ERqA3uedWI2eKIy-agvFs8RxyKaMy6w29rE6qEMXYqFqNP7gtiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تراکم جمعیت در اجتماع مردم گناباد خراسان رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/438371" target="_blank">📅 22:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438370">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1u4nbIlIpFVa0ccyXlcAEZe36-EeKMD0memFJXwm5mCcuGOZ-IloBAMiQUrtpTS6zHB7uNcUiMyOlVy6122-rVKW7YAXvkPx6U6v1WALdw9Exnl0HVKxRVVvfZyO26hUtz9GYAMo21cW9H4m1W_zmhR23fxYDOzYTYx8UqvH6N16AyTRs9j5lkFKwZt1d1ctOUpuTKiKiefBT8-p-sZ3MDhjSIaeaHsjpFAxs4hlIKlvHzhQXK_jCxGVha7i8LsmpTkq-FiQScODCrkn7KOU3l-MR-XcBjotd8VCYGcVs7RDIPSbix4eaYFEhPsEIcX7NmP6t5XN9I1s0Gfe6OImQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز مطالعات آمریکا: بازیابی ذخایر تسلیحات آمریکایی حداقل ۳ سال زمان می‌برد
🔹
مرکز مطالعات راهبردی و بین‌المللی آمریکا امروز در گزارشی نوشته: پیمانکاران نظامی ایالات‌متحده دست‌کم به ۳ سال زمان نیاز دارند تا ۳ دسته ذخایر تسلیحاتی که در جنگ با ایران استفاده شده‌اند را جایگزین کنند.
🔹
این ۳ تسلیحات راهبردی موشک‌های کروز تام‌هاک، موشک‌های رهگیر پاتریوت و موشک‌های پدافندی تاد هستند.
🔹
با این شرایط نیروهای آمریکایی درصورت بروز درگیری احتمالی در آینده با چین، با کمبود شدید قدرت آتش مواجه خواهند شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/438370" target="_blank">📅 22:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438369">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🎥
لاشه موشک آمریکایی در اجتماع نیشابور
🔹
این موشک در جریان جنگ رمضان در نیشابور عمل نکرده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438369" target="_blank">📅 22:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438368">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77acb69f2c.mp4?token=H8PoI_xrjaPCGJ8hUw1nMV5964YswrxL5YQbFPtF5730kt7QDMtinEPlomDJ4BdO8vNZN-WhjwmnTqjTh9nsI2JylUekpsLjqOLdkqsv_WM22wkCYN_Y2-GZAskTCwHuaABwePUDRV4SGUPI4gRAVBMU1DEMY15mJ9LBFLllQtOvCWu5SDgw3QEKkRD9NYJr3vjMAbfWT1OB4JC6ebNbnS3VWlKIgWAUb5LwV-bdvIrbe4w0DUEGGHNqaS7_Q8lEu9f17-jYExiOYyQlLhwmI0VLudFwtb5SanHeDeET4JeJB-Pzh1wt7LNg2b5yw-8O84jQmU1dI4ZZ0LV5iO6hEBceFtcGNVcJyVVs9gk4Pk9ldtp7CCF5ZrBMVuENEjw0srbzMn2GUv6H9BlccRPvaK_iEDau1mXGVdVlvTNJHO3gIpqKbF85ibfjifzcxpNpPk4XA9RGH7Wpagug6CREJLaDue5enzbXBn3L3JaQtpYkMlo_ercKDFgKKajpSTBDOkD2qvSn-XE3U_OTBmwF0CLVDA-PdgsKW81wtmuLc5ljt1TiPP5TRt0I2j-B5gs_p4sqss_uGv1pNfw9OJh-0d2xBTWEA_bteVoYXiGXj3YQeE6meN-ZRZmymOzt_fGG4Jf9LOdUt9mxUR2MtWHmH40LM-yXho8gBnSuvLIkT_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77acb69f2c.mp4?token=H8PoI_xrjaPCGJ8hUw1nMV5964YswrxL5YQbFPtF5730kt7QDMtinEPlomDJ4BdO8vNZN-WhjwmnTqjTh9nsI2JylUekpsLjqOLdkqsv_WM22wkCYN_Y2-GZAskTCwHuaABwePUDRV4SGUPI4gRAVBMU1DEMY15mJ9LBFLllQtOvCWu5SDgw3QEKkRD9NYJr3vjMAbfWT1OB4JC6ebNbnS3VWlKIgWAUb5LwV-bdvIrbe4w0DUEGGHNqaS7_Q8lEu9f17-jYExiOYyQlLhwmI0VLudFwtb5SanHeDeET4JeJB-Pzh1wt7LNg2b5yw-8O84jQmU1dI4ZZ0LV5iO6hEBceFtcGNVcJyVVs9gk4Pk9ldtp7CCF5ZrBMVuENEjw0srbzMn2GUv6H9BlccRPvaK_iEDau1mXGVdVlvTNJHO3gIpqKbF85ibfjifzcxpNpPk4XA9RGH7Wpagug6CREJLaDue5enzbXBn3L3JaQtpYkMlo_ercKDFgKKajpSTBDOkD2qvSn-XE3U_OTBmwF0CLVDA-PdgsKW81wtmuLc5ljt1TiPP5TRt0I2j-B5gs_p4sqss_uGv1pNfw9OJh-0d2xBTWEA_bteVoYXiGXj3YQeE6meN-ZRZmymOzt_fGG4Jf9LOdUt9mxUR2MtWHmH40LM-yXho8gBnSuvLIkT_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرم بهمئی کهگلویه‌وبویراحمد از تداوم حضور در خیابان می‌گویند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438368" target="_blank">📅 22:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438367">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">وعده وزیر نیرو برای پرداخت وام به دارندگان پنل‌های خورشیدی
🔹
وزیر نیرو: تسهیلاتی برای استفاده از برق خورشیدی در بانک ها درنظر گرفته شده که با معرفی وزارت نیرو، بانک‌ها تسهلات را به افراد پرداخت می‌کنند.
🔹
همچنین اگر مردم با نصب پنل خورشیدی تا ۱۰ درصد صرفه‌جویی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438367" target="_blank">📅 21:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438366">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f83bb7216c.mp4?token=gGEtxNmhEGDKUYQ2Oc-0CkXT-KIolPu-C_oO_pTjrPLxfzAkEhFvsPB9526qO1WsPx2osjC3CvaZ6OndCrBU5wqQ3AC9uXLwdmlv0gktWAxIxoyfVKWQ2KBpnuTIFVME4V1ETVUW2aATBu4Vrwu5BmOUATrzyft4gsxAuh7EEpwst_-Ldet29KhHItD7dVnTT2QyN-aagm-pYj_wxV7ZkJkO6V3iOGbUDmRzfbP5h75C2vy2SRTuJ60b03Yyj-6WcdzCPRBKtqQzzbfcPw6pofDXuOWA_WqoK2hvdwe0a4fd7ylSM60DkpC1emu_rF8HhsWQKd_d400ug6to-e9o2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f83bb7216c.mp4?token=gGEtxNmhEGDKUYQ2Oc-0CkXT-KIolPu-C_oO_pTjrPLxfzAkEhFvsPB9526qO1WsPx2osjC3CvaZ6OndCrBU5wqQ3AC9uXLwdmlv0gktWAxIxoyfVKWQ2KBpnuTIFVME4V1ETVUW2aATBu4Vrwu5BmOUATrzyft4gsxAuh7EEpwst_-Ldet29KhHItD7dVnTT2QyN-aagm-pYj_wxV7ZkJkO6V3iOGbUDmRzfbP5h75C2vy2SRTuJ60b03Yyj-6WcdzCPRBKtqQzzbfcPw6pofDXuOWA_WqoK2hvdwe0a4fd7ylSM60DkpC1emu_rF8HhsWQKd_d400ug6to-e9o2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هشتادوهشتمین شب ایستادگی مردم ایران در میدان خیابان هم فرا رسید
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/438366" target="_blank">📅 21:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438365">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🎥
ویدیویی از عملیات هماهنگ حزب‌الله در جلوگیری از ورود لشکر صهیونیست‌ها به شهر حداثای لبنان
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/438365" target="_blank">📅 21:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438364">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWg07jghq8Fgpx9urVxLDV8rQ7ScgapuSFXjReevtSl4-xIGiVjK7KeNYNLroQ5xg-Dn9pcGEs0iCMUgSDzUi99vsMT8kckQ2DukD_kVWuWAabOeuXNswoegS0WDNBwVm_UiBJNxCPOzE__75c8swV5aE-DTxDaakB8e3621a6boWMrf4q7zBgS251tYTwqUgIOeqYdFJ1oM_-Snszs59OsM3waSJpanTAcalPbjcJptcZsaES-hiafut-kuT3YLEYP6mZBq-LxlAo78sGKam7pQMrwkPMw86sPwTu3oq5CTsDDvfeqh0XrqIti8tUNw2TZBcpVS0OcsAcZLB7foBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
ترامپ عمان را تهدید کرد
🔹
ترامپ گفت: «تنگه‌ها به روی همه باز خواهند بود و تحت کنترل هیچ کسی نخواهند بود. ما آنها را تحت نظارت خواهیم گرفت.»
🔹
او در ادامه گفت: «عمان هم مثل همه رفتار خواهد کرد یا اینکه ما منفجرشان خواهیم کرد.»  @FarsNewsInt</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/438364" target="_blank">📅 21:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438363">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d124275e76.mp4?token=fL7OntDp-Z2nosXL7GsKCNUO1Ehl1G6tc6R2x15ifKVt59DDVYGJM6Wp-wgPj6z-ij76S4qtJH_7Eqs2nic-kMxleQPMQpAKYo3Avatui6isjRsBGG1DilnRc9gWsWlscW5m0-9Y29imlNdActvkM-Dfl4ZMo5jI5lZgT0ny1wlUdY28G4YAZezmPUwyyln2WyoBvvNjAGwWqBl6UvDAyGutlVsFeiuC5gQvbOgzrpx4cG9Gi1lLE30QX2LIUZTXStpqg_JEituX8x0h5RtjqLF4X8agVIwyrlODMcSPBtd-8Y4Jt48P7Sm4_7OvMeWSvXeEDrs6JD0ylPrphsgf3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d124275e76.mp4?token=fL7OntDp-Z2nosXL7GsKCNUO1Ehl1G6tc6R2x15ifKVt59DDVYGJM6Wp-wgPj6z-ij76S4qtJH_7Eqs2nic-kMxleQPMQpAKYo3Avatui6isjRsBGG1DilnRc9gWsWlscW5m0-9Y29imlNdActvkM-Dfl4ZMo5jI5lZgT0ny1wlUdY28G4YAZezmPUwyyln2WyoBvvNjAGwWqBl6UvDAyGutlVsFeiuC5gQvbOgzrpx4cG9Gi1lLE30QX2LIUZTXStpqg_JEituX8x0h5RtjqLF4X8agVIwyrlODMcSPBtd-8Y4Jt48P7Sm4_7OvMeWSvXeEDrs6JD0ylPrphsgf3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ عمان را تهدید کرد
🔹
ترامپ گفت: «تنگه‌ها به روی همه باز خواهند بود و تحت کنترل هیچ کسی نخواهند بود. ما آنها را تحت نظارت خواهیم گرفت.»
🔹
او در ادامه گفت: «عمان هم مثل همه رفتار خواهد کرد یا اینکه ما منفجرشان خواهیم کرد.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/438363" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438362">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8583938fe.mp4?token=IAPB9fraLQiQwmd3vwO27LGbChSSchc1s-uG2A9mnh1yZ7HhWe0C1rikLpzDNtIkj1hb-z_uLAYP87ztlHyvAlaVshaRUQY_5MJIJXvf-2TzYNTfirvGg1XJcvvJPZfRrdpg_3JUjvDxrIlD-uPJKaHQ4AQGUpdl1VSHK9rxo9SHOrFB0WDSibph3wxRC-r44_hOu_ObXGhEV5ZonhuqJWIhIAlWdh0DSB31IRfqS8Ws9KT2OL9qvibyjOHQVQ7mXQGSabrpOXYhjh1ddD6_-vGA0OWRsbLDr99ehvOlLNTZCuTULCq-HDyUjXqQK-TmzzNIb0OK4a4rlZriIsKVYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8583938fe.mp4?token=IAPB9fraLQiQwmd3vwO27LGbChSSchc1s-uG2A9mnh1yZ7HhWe0C1rikLpzDNtIkj1hb-z_uLAYP87ztlHyvAlaVshaRUQY_5MJIJXvf-2TzYNTfirvGg1XJcvvJPZfRrdpg_3JUjvDxrIlD-uPJKaHQ4AQGUpdl1VSHK9rxo9SHOrFB0WDSibph3wxRC-r44_hOu_ObXGhEV5ZonhuqJWIhIAlWdh0DSB31IRfqS8Ws9KT2OL9qvibyjOHQVQ7mXQGSabrpOXYhjh1ddD6_-vGA0OWRsbLDr99ehvOlLNTZCuTULCq-HDyUjXqQK-TmzzNIb0OK4a4rlZriIsKVYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماینده ولی‌فقیه در سپاه: در طول جنگ می‌توانستیم اقدامات سنگین‌تری علیه آمریکا در منطقه انجام دهیم اما چون مردم خاورمیانه آسیب می‌دیدند رهبری موافقت نکردند. @Farsna</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/438362" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438361">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3117b79c.mp4?token=NIUbz8868eflD071tWkcsFbE_8VFKrjIJrz3qKEFlvj4w5Jwv41-bQ55t5MNLFK5YKdh-qeO0qylbD4nNEzcepFI6AjguxK6W0j3NuZf7yD2rhCYJ1sqEhhN-ob8KbUtasraGOUU979MYQEU0RkeZ9BB9goMH_enHUYFWacWx_-zG4nlPh5t_NbmvapHdSxxL5-esc3Bwg4asL793D2H9y_Dtm4S37UWn1iFTEuncA6Ws93-UJRyWtyd98SMWSPrUGrHq8O2tgfeOdHBrrGxzCEhjpzZL7J_A9lM584h5hHuUsWc_34gIy3Et2CZWwk-Z1Lyoo67gqx7HPJi_IRVJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3117b79c.mp4?token=NIUbz8868eflD071tWkcsFbE_8VFKrjIJrz3qKEFlvj4w5Jwv41-bQ55t5MNLFK5YKdh-qeO0qylbD4nNEzcepFI6AjguxK6W0j3NuZf7yD2rhCYJ1sqEhhN-ob8KbUtasraGOUU979MYQEU0RkeZ9BB9goMH_enHUYFWacWx_-zG4nlPh5t_NbmvapHdSxxL5-esc3Bwg4asL793D2H9y_Dtm4S37UWn1iFTEuncA6Ws93-UJRyWtyd98SMWSPrUGrHq8O2tgfeOdHBrrGxzCEhjpzZL7J_A9lM584h5hHuUsWc_34gIy3Et2CZWwk-Z1Lyoo67gqx7HPJi_IRVJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده ولی‌فقیه در سپاه: نقشه دشمن این است که ما را مقابل هم بگذارد
🔹
هم کسانی که مذاکره نمی‌پسندند و هم کسانی که مذاکره را یک مبارزه می‌دانند بدانند که دشمن می‌خواهد ما را درگیر مسائل داخلی کند.
🔹
اختلاف‌نظر همیشه وجود دارد اما وقتی فرمانده بالادستی یک فرمانده…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/438361" target="_blank">📅 20:50 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438360">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0848db393.mp4?token=nSvPbmOmrEHqRUHmMebRL3rIhAWkkuGmcBrWKZuk1xTyvxS8l-uDbfOI6YsyCi0bomDGie5WPHTB6iqvghAG6sj0t_ehhYPyvk1wl5bn4BgIXK0WFKIuKWMYYQQ0gbbFrS5Xp8cA9gSKtvnMuKc4cpdZJO8mEnzyr9r0KpIFGovtr8or66qw-b_98JFV7YoGnCFgNlP7VYdemvgFBzPFZCEDyq2qvRX8mDJMR25VSxgr0X8Yh0LP6A77dVlBg-S6TTeGTh5e-mRiaCFmly8DggZSjPOhF9QPoSuQBuXIydhWlNgNw_44bPyVGmM16nyvAa_yTo1iRN8jUdKeu-FPcyr3pH0ybXAd-fZYgc3BX2Fo5NnA6iuEQFAy1xq70cTykUJ85l4uSfTBUViEyA2DoU6EdGnaAEudz6p83_m5Wzr0Ximb-gp61ZIf6J-pDur6uIbdN_SSnV0LhCUvU-Z4fllZOQuQjDDF63Lhj-zuTeV1dv8nDNU94iR3u_LM_IrCxL9XCr-Psmix_omT_YwSDQDrje3hXozaBCheucQ8GI1QuSBPWilvsem1hEkhvYtB0pXD-LpzcTze8eyw2bN1WiA665l_loxp58dX7mO7nzOvZdMZ9nf3vgwD5v-lhjBc3_oosLlhbybR43P-6kVMzf_GM3rshAt66cGbe6mFPmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0848db393.mp4?token=nSvPbmOmrEHqRUHmMebRL3rIhAWkkuGmcBrWKZuk1xTyvxS8l-uDbfOI6YsyCi0bomDGie5WPHTB6iqvghAG6sj0t_ehhYPyvk1wl5bn4BgIXK0WFKIuKWMYYQQ0gbbFrS5Xp8cA9gSKtvnMuKc4cpdZJO8mEnzyr9r0KpIFGovtr8or66qw-b_98JFV7YoGnCFgNlP7VYdemvgFBzPFZCEDyq2qvRX8mDJMR25VSxgr0X8Yh0LP6A77dVlBg-S6TTeGTh5e-mRiaCFmly8DggZSjPOhF9QPoSuQBuXIydhWlNgNw_44bPyVGmM16nyvAa_yTo1iRN8jUdKeu-FPcyr3pH0ybXAd-fZYgc3BX2Fo5NnA6iuEQFAy1xq70cTykUJ85l4uSfTBUViEyA2DoU6EdGnaAEudz6p83_m5Wzr0Ximb-gp61ZIf6J-pDur6uIbdN_SSnV0LhCUvU-Z4fllZOQuQjDDF63Lhj-zuTeV1dv8nDNU94iR3u_LM_IrCxL9XCr-Psmix_omT_YwSDQDrje3hXozaBCheucQ8GI1QuSBPWilvsem1hEkhvYtB0pXD-LpzcTze8eyw2bN1WiA665l_loxp58dX7mO7nzOvZdMZ9nf3vgwD5v-lhjBc3_oosLlhbybR43P-6kVMzf_GM3rshAt66cGbe6mFPmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده ولی‌فقیه در سپاه: نقشه دشمن این است که ما را مقابل هم بگذارد
🔹
هم کسانی که مذاکره نمی‌پسندند و هم کسانی که مذاکره را یک مبارزه می‌دانند بدانند که دشمن می‌خواهد ما را درگیر مسائل داخلی کند.
🔹
اختلاف‌نظر همیشه وجود دارد اما وقتی فرمانده بالادستی یک فرمانده واحد است همه از او فرمان می‌برند.
@Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438360" target="_blank">📅 20:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438359">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ادعای رویترز: پزشکیان با نخست‌وزیر پاکستان تماس گرفت
🔹
خبرگزاری انگلیسی رویترز به نقل از یک منبع در دفتر شهباز شریف، نخست‌وزیر پاکستان مدعی شده که او امروز تماسی از مسعود پزشکیان، رئیس‌جمهور ایران داشت.
🔹
مطابق این ادعا، شهباز شریف ابراز امیدواری کرد توافق میان واشنگتن و تهران به زودی تکمیل شود.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/438359" target="_blank">📅 20:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438358">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4501e83e61.mp4?token=pDKsO7f31Y-V4IbVxWOV1XFta-g9zXsklehvv3EPWcW6ZYIEwE8mub-RdelkFwamqBeiM_5CWBhMGP2gNLPzpUKBuSlHu6m4GT6NaNX37NhxE1vzlxfJUUeSafE5wmsbT4HCsQJxyKqtzNR5iFlQrMSFadOEr6HDh-wjUn4YVjvbJrc3WsaYm7uCQx4oJ5WuxpITXoPM9v_fJiFf1mTaDEAn3gDYI9sTsaZApmFS0QTNYDXNBmF5HDLR8-IsDrk9ofVL8sc0hQsgjF4AwS7wvjBBL4e2550hFYEYKueN0DX9WmZaOrCYbZyXD9UMEuxVAr_iXnBrsz0KQuDR2e1cPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4501e83e61.mp4?token=pDKsO7f31Y-V4IbVxWOV1XFta-g9zXsklehvv3EPWcW6ZYIEwE8mub-RdelkFwamqBeiM_5CWBhMGP2gNLPzpUKBuSlHu6m4GT6NaNX37NhxE1vzlxfJUUeSafE5wmsbT4HCsQJxyKqtzNR5iFlQrMSFadOEr6HDh-wjUn4YVjvbJrc3WsaYm7uCQx4oJ5WuxpITXoPM9v_fJiFf1mTaDEAn3gDYI9sTsaZApmFS0QTNYDXNBmF5HDLR8-IsDrk9ofVL8sc0hQsgjF4AwS7wvjBBL4e2550hFYEYKueN0DX9WmZaOrCYbZyXD9UMEuxVAr_iXnBrsz0KQuDR2e1cPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: ما به نفت نیاز نداریم؛ ما به تنگه‌ها نیاز نداریم؛ ما به هیچ چیز نیاز نداریم.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/438358" target="_blank">📅 20:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438351">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/clBIAS8IYlTJGxZzomMoU8cqR1t1R6tWkm0sChcGphq5MRwUSCtIJbYtfKGB3r05raZi-OBs8S5YU1Lej2sqSpkZVR2rAWWiGWiD-4G9NikWFPpjW2zMl2LDEVDmmlI742r3_gjjbYGbbiRu7JUAF8C2SQ8-aUxj1SnSmf22_hy2j5nB5rZ3Brd7EhYiXGBVdzLhcAsJWOnSW210XNKTjQrzFTM6Lf_lfqvLMzWplM5PzHfkIsl4xnikMrBV9_5XfMyrme_qS9fD8UP44_eDhIFeo6YhqaEgFSf4nJHahqBo4WBKh02Jmr3RYx54zhKoz_gPdSHRoi8ZXmD0ckWfwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O1ZN08h5pGxR8bS_22IzawHu7_kEDR23gpgLudr8PfTypJ1D3h09eFK3zEX8R192dpXT7Iv9I2uk6YH9kbL_4_zy-ez541whE_PS4Lags7W8PEN6OaV1Ce-LtAOrJfzIKU4ZG2OeJe6vXuo2qDaVOpPYHJNw603QRmLXjxaRe9qLcy_d8dp8ZoetA-k2yjcWbWFM1PSKA6lAPw5NTqWvYsiGNmcgGcoXvBqoa_q6qVPMJi5QLyV-UHQzzinWnbczJpySe0N3ie5vr_MMlsXb5Pxk-p2-_Wvyzr_kIXB0TYb11EOCcerAEEYabWq40kZEhOdZ_1tLHnVaw0bNHICi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sJMtEwbam7qUrcPxwdufTxGGiFk4UPrwFkFNNVpBN3k5Abo65TwxYwuoCKXb2nv-WHDV21QoGSj1yuDn-OqLWS8IRJjhhYFENhrYYD9KbJdrucpZWjObHFfakS9fJ9HJ4LllhBboIFV8FGdsqVPORAg_O7kWD-WaOazx4rTIll1cEG2Gtu8lSSyCkKprms_mHWpyLshFahOF5nNjfflaIZDuHCkxD9UYkXnLoZNBCmiLDNmBLahCMjbnmJGyUY9Tppt15ad6MmQkoJVHiwiDc7gisAkkEjpzZLikU1Ma8q2peGfyB3Jd-iEbRnr2zZCZDw8KZI_TlTXHVCjffM6yCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uwc7Jey_7g3VbubhdfXakw7c2v0LbpXBOkwjzE9tOH0oQwKSDdR3DdULQBA96sMqMdhOXU2tSqSSS7mE-vpsErPn9M7R7z0NpzQC6UMg-3ImxEjUKTKbA19U_2wI-jlEZ9Cl5u6gstMaVMMI5e-S2Tgb7ESYL4smZAmSTQH6pggFh6fJEDn98Wz26JsT-SNbOXhZHs_vyyybh50uc8IUmyqWloVyPMvIQi8dIGyMmg_wuk7F8AxLW3ysGb05saRg4BIpiwxgXMx9PHcAW8iOBNaxrPr7rQqm-1fdiOzqlkCbz7Z_cKiJXw0xmBQguU_ydtm6SUpe0_7PlkIaADZOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/anjqkTR6SibJiP_0ejfaxvyJ6luuKssjxJF-YBQ03buqJJ0GwTPH9hTW2ZGKW403ZysIK_qLmaBBPPvWHdO4c_J7n7bQx_ado2ZUId1kfVSGN1DlljhimCmrOP6I_hoHS9ZUeZuR4iMS1-_9tzPGg6HhAO6d7LVBkb0r0bNBLmjur5gODnZ2wQybzRtyx9dYB7qeTKkQrulCMecucNLMxJHmOh5Gn9g1cHvZ16ezlwMJRHwodwRM_YlXJt_lBGjj4VGKH7S5IFNCIAQvouR4wMA2ciy-kOVyJFNNJzo-xJdHFAnbicc7W_YU54IpbxvLbmBUxKPGYCbBXketsadiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mWD89FnbdbrOA9VeX880zFKEZHegc5iJzcuQZQAPJrpwd3Le0wtqsYBF7OyGioYn5FB3ynZQrj7rsO4VO0JU-_5QVXaHSMGw_j_JEKnZkT7O35abEpHa_9MFk8USzNBXVZtl4qx5Me_1Duu5s8DfVa_crg0eqRY5kvYogwKV8iIHNb0hAyPyGQ7sLLUyf4GS0v9Y0GxhZUZ1OfyLVpTDLP2xB-Uaaol4fgXM3UpdodG6clxa5D2dSsmLhH770UkcqmQwMEiGdvbPwbfUY8LWMLl4ckx3FXIhRG90oRCKDTrFijpLzbTgSfRvneXszBKNK7Qdy57-0GqWml27BsJC6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l_68ouEqfu4OuW2zEp0iHSoxV2Oja7tcQM1p8JmNp8xcR3aZvCqdPYxjPYQ7JsE_RvlubRk5FLO8EcQAIFBeoUML9Ov7WDWxCqQHcxB2RpKWxOl2v9LyMA-Ar7OalgTuTGV0mVE6QZ5KyI7mfk07q--EbdQdKfYXYTgtI4w_XXlftyAe7tN2-J68xJ9HdSPW9p4WU4D0brwNQhRHEJFhAAAA93-UHRaL2RXhP33LKYa6jCnzMAx0vflXW8Hj-cBNi2-cOGgEa4GvXyEROZCmd3jBRlHWNMAjLotUXqT9VWxyrDdJQEErrVLFlwth9jDyvbbXt0LpTVFRNBO5jF2TvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز عید قربان در اردبیل
عکاس:
حسین حسین‌زاده
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/438351" target="_blank">📅 20:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438350">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHRcPsDyvzMwup4-FKk3KvBAtPs1Mlz57s9gM52c6DsCxWsMZsOQ-bltLZRz1HrHItkJdLlo4z4T2SLmnrP_mLruxI27fQbRwTgzUc7IvAn2DJkXVLKtt4W6h-eYEekTpZZHdF6fdsKx-3WaHdryir1I8b6Q_FGQ8qJe4JD7kl4F8rom9cCosufYsP0ZxPcb3sg2htwjKcwWpE9ZzRQR-uSsfViFw4uxWlkJVsVjX0zRNJV5BKPmXFe6NFBnBOI5gpkjxpgIZf_KFBbw6NuaDI71BiXUiV4M1cnjw9Ud_J_-7954FvKZcFsTV4NVXmERkiPdL1NUTwamnh2VK9e68w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تحریم‌ها در ازای واگذاری اورانیوم رفع نخواهد شد
🔹
دونالد ترامپ، رئیس‌جمهور ایالات متحده، در گفتگو با شبکه تلویزیونی پی‌بی‌اس گفته که ایران در قبال تحویل دادن اورانیوم با غنی‌سازی بالای خود، هیچ‌گونه تخفیف یا لغو تحریم‌هایی دریافت نخواهد کرد.
🔹
وی گفت:…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/438350" target="_blank">📅 19:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438349">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbxZHNsUOnm-FiJF3zsdlFHFIleMNU1O8TsFhxd4GZa4TWvqvBZfWlgKzQTz4cmi908sKYYnNBzsFM4mkj_Wa_wFDVh87KhQizhza6ZWHKgndsn6TKZmTtvo6EAV5GlJj-h_fu4fghlUrxWXhnIosVzstSxw3Yoo3omUlfmNPS9FM5TYgAo7kMriuzNtjRhvOzoMgjjlSAfRsji7hS7YYIY2hgFs-FhW5NadWOGCVASOwSEpIcYFpwQqN9HiG8v3030Eljo_xFJgBdLD3DkeyB8zmizUG9WVU9y-GX6Bvrg1cD_Lau45AMJDnffiGEddjwGsT2nZGfBBimfaicmTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: تحریم‌ها در ازای واگذاری اورانیوم رفع نخواهد شد
🔹
دونالد ترامپ، رئیس‌جمهور ایالات متحده، در گفتگو با شبکه تلویزیونی
پی‌بی‌اس
گفته که ایران در قبال تحویل دادن اورانیوم با غنی‌سازی بالای خود، هیچ‌گونه تخفیف یا لغو تحریم‌هایی دریافت نخواهد کرد.
🔹
وی گفت: «آن‌ها اورانیوم با غنی‌سازی بالای خود را واگذار خواهند کرد، اما نه در ازای لغو تحریم‌ها؛ خیر، به هیچ وجه این‌طور نخواهد بود.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438349" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438348">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFSlGkbpiuC7wPyhGM0NqJTskuQ1NKPGrwzSQn_j8_B2gfxMoICjTQSM6DAceDncmRrZU_pn7Qh9XTTZtlie2R6lVuI4Q4B7h07lcZUL3PWzdeYS7Zm9pFwdAGnc_PfahssI-Kg9H0lNqDxm2YqKIWO43znDsQ2VUBtXGCdstavlXHRrDIiWnqRphCEbUxGys7yYyJpMJS7168wsAOXfkkXLpnx6zeS09ogvoK1gR_h84DKQ0HpWAl3MFv1ZzNMN1-3_D9HFa7b_AF2FhovDJMqQexTrXNsA7iCUr8z9BXVQxWyzv03bmPnVMVlbUUJI5APP7QJIjj9KMwW0gLcunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نشریه تلگراف: ایران فقط درصورتی با آمریکا توافق امضا می‌کند که ۲۴ میلیارد دلار اموال بلوکه‌شده‌اش آزاد شود.
🔹
ایران گفته نیمی از این مبلغ، یعنی ۱۲ میلیارد دلار، باید بلافاصله پس از اعلام تفاهم اولیه در اختیار ایران قرار گیرد.
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438348" target="_blank">📅 19:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438347">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
احتمال اعلام یک‌طرفهٔ نهایی‌شدن توافق توسط ترامپ برای فشار به ایران
🔹
منابع آگاه می‌گویند دونالد ترامپ، رئیس‌جمهور آمریکا، احتمال دارد در ساعات آینده به‌صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است.
🔹
این اقدام از سوی ترامپ با هدف اعمال فشار و القای توافق به افکار عمومی، پیش از رفع کامل اختلافات، ارزیابی می‌شود.
🔹
بااین حال، یک عضو تیم مذاکره‌کنندهٔ ایرانی در گفت‌وگو با فارس تأکید کرده که هنوز برخی موارد حل‌نشده باقی مانده و تا زمانی که همهٔ موضوعات مدنظر ایران حل نشود، هیچ توافقی در کار نخواهد بود.
🔹
به گفتهٔ این منبع، ایران درصورت رفع کامل این موارد، رسماً نتیجه را اعلام خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/438347" target="_blank">📅 19:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438346">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
حزب الله: در ساعات گذشته ۱ تانک مرکاوا، ۱ نفربر نمر و ۴ مرکز تجمع سربازان متجاوز اسرائیلی در جنوب لبنان را هدف قرار دادیم.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438346" target="_blank">📅 18:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438345">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a455f364f7.mp4?token=AERuQO1RtghvyxfSKS-0rS2EOBJzwo93A83b1eqFy5Wl3dRZy_UmuvtZiH4V_3jbqCbhgwIbC8deQ6lWMOWbZGaMTXuofLl7vT1CUvnLfHVJdvi5HyLDtVzgjStngGeISsWvOGPzLKZ-YuNyoPZiJOKerzMP-4zN6ikiatFvaPNgjdMNUDzHFsQgHm_H8KxLZicYXHENbEmBokJ0HzuLzhTPiRHhFbng7oZPS9yZ0MM_VERfx2JGasl6CsYNABilazfBSbnLQZoZnYhZLfQATlX8bGZP88UXJa6oLvtEtof5fnzR_wE2j_qxTRNkFiPbEwYMhtGhSDLExPU8puKjZwQ2XZ1dgfuQGHAZ2k7ajFVzdmJEiFQ_dvyhf_cOKCugMEoMQij_yRgoUq8sAgTtDv7stsW6Wqg_UPHZT8xIUNRBrzhWNozl6UjDA91duX4hkQhxtRZSsMpQc63yDfDZaJU92sTITfnEryzRgUnpbLtpVLCwbMKCY8dZSnuucvmBn-ZDIJHcwEySxDiK9FLk_imcSCpJ4bYhOhcQ97hX0h3e6Rd0svCSPFPT5sfGzxRtzkgafkdv03_d4V7vMmPdXKz4J_8Vh_L_DTPtp3qbcESNFLbhWdP27ntuepqiUn1PYfLsHIsUYyKSSJywBX90BhMDGzbf8QhXEH1upLXNQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a455f364f7.mp4?token=AERuQO1RtghvyxfSKS-0rS2EOBJzwo93A83b1eqFy5Wl3dRZy_UmuvtZiH4V_3jbqCbhgwIbC8deQ6lWMOWbZGaMTXuofLl7vT1CUvnLfHVJdvi5HyLDtVzgjStngGeISsWvOGPzLKZ-YuNyoPZiJOKerzMP-4zN6ikiatFvaPNgjdMNUDzHFsQgHm_H8KxLZicYXHENbEmBokJ0HzuLzhTPiRHhFbng7oZPS9yZ0MM_VERfx2JGasl6CsYNABilazfBSbnLQZoZnYhZLfQATlX8bGZP88UXJa6oLvtEtof5fnzR_wE2j_qxTRNkFiPbEwYMhtGhSDLExPU8puKjZwQ2XZ1dgfuQGHAZ2k7ajFVzdmJEiFQ_dvyhf_cOKCugMEoMQij_yRgoUq8sAgTtDv7stsW6Wqg_UPHZT8xIUNRBrzhWNozl6UjDA91duX4hkQhxtRZSsMpQc63yDfDZaJU92sTITfnEryzRgUnpbLtpVLCwbMKCY8dZSnuucvmBn-ZDIJHcwEySxDiK9FLk_imcSCpJ4bYhOhcQ97hX0h3e6Rd0svCSPFPT5sfGzxRtzkgafkdv03_d4V7vMmPdXKz4J_8Vh_L_DTPtp3qbcESNFLbhWdP27ntuepqiUn1PYfLsHIsUYyKSSJywBX90BhMDGzbf8QhXEH1upLXNQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وعده وزیر نیرو برای پرداخت وام به دارندگان پنل‌های خورشیدی
🔹
وزیر نیرو: تسهیلاتی برای استفاده از برق خورشیدی در بانک ها درنظر گرفته شده که با معرفی وزارت نیرو، بانک‌ها تسهلات را به افراد پرداخت می‌کنند.
🔹
همچنین اگر مردم با نصب پنل خورشیدی تا ۱۰ درصد صرفه‌جویی در مصرف داشته باشند از ۲۰ تا ۳۰ درصد به آن‌ها تخفیف داده می‌شود که خود نوعی تسهیلات است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/438345" target="_blank">📅 18:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438344">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9O0t_6aNmzlQuqGXCduwYNUzvCZPU0zXBCj7DGDA0IXSu87tAQwLnMdFpmD2NLgk1EpaE18D3XNiLYGtyQsjaaGWU4Yue9I5xkrc49dvMsH5NPkrYgqSIsLX4KSg6kPwuC3rP8dRQCR1wR0pW1eNm7Z1Khr1xHaMrULAZnkZgyfAwRbdVAk7IB8BANlVzhJzMVRiRwnzL2vCPp_5-q3HisjJ-ZanhGjCjl-Gsd7fZmbfIg_obcEfx3nrAUK0LV5npiq5_8AzAtyiwCdFPETU_43a7easMHPtkFpS9DxAQb7ieeSFiiQVHsxK8u4b_SKb3mzpfztcKX48Vdz_e1v1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدیدترین نظرسنجی از مردم ایران دربارهٔ مذاکرات
🔹
پژوهشكدهٔ مطالعات و تحقيقات دانشگاه جامع انقلاب اسلامی، در یک نظرسنجی‌ از مردم درمورد مذاکره با آمریکا پرسیده است.
نتایج این نظرسنجی به‌شرح زیر است:‌
🔸
کاملا مخالف: ۲۶/۳ درصد
🔸
مخالف: ۲۲/۱ درصد
🔸
متوسط(نه مخالف و نه موافق): ۱۲/۹ درصد
🔸
موافق: ۲۴/۶ درصد
🔸
کاملا موافق: ۱۱/۷ درصد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/438344" target="_blank">📅 18:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438343">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مهار آتش‌سوزی در فرودگاه امام خمینی
🔹
مدیرعامل شهر فرودگاهی امام خمینی(ره): ساعتی قبل طبقه سوم ساختمان اداری گمرک فرودگاه دچار حریق شد؛ باحضور نیروهای آتش‌نشانی هم‌اکنون آتش‌سوزی اطفا شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/438343" target="_blank">📅 17:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438336">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SHaDNqGCd7sjBb-oZEvrmuLR7VAXpaxMZxuaHmzGz0FkdYTQ6BxzZNwwbnwGbAy7B7zZEZQzWqe_-MucGQNMvZDY7kQPKX43xQom5KQiK2eMO1GiNWS-yMiLumGOigV5Dbp07siOfWC0YwFAPBhdHltYGyeZoTUZD-PpR-k6EE3H1d2IErxFclODfWZKMx8rqcXFsvQdfREsm_zKTA7r_Aqk-b9in2EIhDlpsJ3c2ft7x--3-NdceCi-SmZIvNCOidPUy4gF1N013_FRDkw7XSLDKphSpVcywmRW_PAIykVVi_uDTG5PGij33KGON07HttlEtnLNmf5kuJ4qEWG10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqYlM8mASXVOXSlhCd568rM7EuscYJsjmAhVBE_G-Dk0Q80aqlQ2wPSQXH_iiN9VH4xsjQuW0qade8T036PtCCpU0ZuKOcQA88mhkyvSHnpbEPLnu3vYpEEU1WcrzbA_vUA_7CPAXs97MiBuCjF1ewU2Mo_IKXWTFOQoiB7u570sCSq8tWp0OIKXNCPN3fOV5yzPfRqgf5TU1fuhOGlqpN_z1MJyhEM02eSwcSblQtfAtacWewLJVTFZ22ulG-P9zt_so174LTwQB7BU16BtCrnNObQS3npUxu0SZ1yI7HGmN9BgzSkldAZ5lEV_K0HJppIA-XzrwKvUVUmYP3iFFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wen8nngyzAhrXSXP7BsAcndg25i7V4PGx7EBfam9orERM462L9V-cxyQOsyD5VNDoci73ZE3gpT2tbZ3kaJPJDXeYpUo3kLGK6H25AjHeSR-gYcBT83UNEZVQU_3gHTVQyNMZBJwDPIirSinsus7RE1ZdUoRrNcQaeblzabxCbzZUiOFX-CmC0AUDXNRNubu-m7mJjKMafOCbVTMGzBcorYxsOKlCbXh1yNvVNFp3jqkwb25_g3tS_U_x-hUh5iChOx4LSkH0XZ_Gf1S2SK5HiOmLQ2h_50VYWSJAdtegFdncsiVV9MwoJjDZrKjM9yatNTAYNhQ4YtXYQZU-v_nSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JH2tD6_ks_GSH-yfSf8p1rQMslqOlO1x9hBguSkPyhEL-CIYq3GFhtGh_ZpBqkfq8TX0xmTswVD4ak9f0-IDW6ybdK3cae0yzdp77qDDzJu1ybn5gNYlpMmqgzEyeM9VTBQhr54nXWgj2ug_3Kff03TA1x67_VGNtVr25duPHvlCE7RMtHn8v1juJobouUc5FqQX0dLCu3sNaCgtUU2vZvYPKpsos9r75gPl7feDFA7oseehDVkufF8fzAMPCmQAxVXbSQW83wLSfBMz8keV-UMojlY_-pZjkEOG8h4ViLsK2RqTGPcFp8Ym8C1NYH3xq3GMgSPTd1nkOF1Y-vSSRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LTATaPerdj6hz6_eG642OGr2AaYN17B1dXraZyH9qn9IZy9Hv9k_KjDQAXrd7i8kWMMvs19xKu-xJG4Tnj8Ycl5rsT5dUngNN8cono8_6RCpyjjt7SgkFZpJeO-RjbQg-fT8MMq3N81pciPgz8cRpxjabekNTQU-y4asjFJ9kZDBrHboS9ZjXdx3eG6Wh0RbZ8XCKZ3XNAi339KUfRkw0Ab8MVMllq8UsUIW8HROX2eWcK1fkC-F_Rgv1-dmyQvrajgSEcll5kLoKZ0FhnPnG8eW4hWDn3Nk0WfgUE2O0gGHal14L1j30jC96yOtgmyErQLFiRk6yx3h0GSlSis_OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ldvguRAhlhudX8kdZO2FODO_bDMytTGfh2OLSbBv306IHk01Fm2O_xnL7e_lKwt5ENv5_dnEQA5A2Mnn49MZAYeYodXt7hJT_trTuUsGhDDaycLwkkIzzxUBS7RtRfLSKxkwwU7pNiItft7Q1zv5SOH4aARgV4r8sCI-7e3CVjZK0P9zFPPjsfEBRiE-cU8Z2zrtnhovkx4mJeJIfJA64cvfWuCSylc3jOj6BVF3ODp10mn0-LCa6Tdo4e_B7oLFIYJtBD4bARLugqCwRsJAf0sLzw-5E23GfAOvhiohqPRLImbiAEROy8PSBok7O1eoSBHY20Eef-s02INQf3njuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-X0TT1pHLbawOtzddaOVSvW6SVvwdF-vbbUOj_M5EmAWRXVsZXch7ndigCMxJ1EqU1J2t_EEAEZO3tRYpeEG3hehUNfeGPsRMWkpZEi8gCCJElMw7fbnBO7025miaB84702UteeF9ELHS_EIK_6lbIiC1OaerEdIRTPctLosQmE9lWFQMcmukUKWrR8gZ0o33kQMESd-AdtgA4WDsGMiKgSeQL6u-daEJbwILy02QOScJOhEqq9QieQ_rRb7WcR71noLiH_vGJ0h1sshOtUt940PEtY8QIsbNy65fwkIFnA6t7S0HUKsVd6VGiAo7i4h1gyLIAPivOtLyrAeP4x8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نماز عید قربان در حرم امام رضا(ع)
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/438336" target="_blank">📅 17:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438335">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4db406e91.mp4?token=aCrFWSJzMMkg3_QrqbON_WP4kMWID3IJdlTbtlR5KOhA6WwNQrZcEeyTGAH6ODwyqAa1jwiDUsCrJ3psou6adKGaPV3jCijrrH93y6y4QCz4yFO1ebMGjCbko2-5zv5nv0JQPmaEJsBmApUThh-I2CtrTE0aDcnTNrtQtmzwbm7LS-jplfAIOP5yvW6NN4HxaExh7vKy7iGV3-N4jtyGvF4VwIkcncWNIDPccUT-JpytkVDelC5XKzsuzY923xmK225HQyLTOWmseRKXPQp7Ttoo1f1joIOt5uebnyRiu7qjdQgoxdSX5Z9lcuO5e0gqFy2F43rYivfnXX5hWm02ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4db406e91.mp4?token=aCrFWSJzMMkg3_QrqbON_WP4kMWID3IJdlTbtlR5KOhA6WwNQrZcEeyTGAH6ODwyqAa1jwiDUsCrJ3psou6adKGaPV3jCijrrH93y6y4QCz4yFO1ebMGjCbko2-5zv5nv0JQPmaEJsBmApUThh-I2CtrTE0aDcnTNrtQtmzwbm7LS-jplfAIOP5yvW6NN4HxaExh7vKy7iGV3-N4jtyGvF4VwIkcncWNIDPccUT-JpytkVDelC5XKzsuzY923xmK225HQyLTOWmseRKXPQp7Ttoo1f1joIOt5uebnyRiu7qjdQgoxdSX5Z9lcuO5e0gqFy2F43rYivfnXX5hWm02ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز تخلیه شهر بزرگ صور در پی هشدار ارتش صهیونیستی
🔹
پس از هشدار تخلیه از سوی ارتش رژیم صهیونیستی برای ساکنان شهر بندری صور، ده‌ها هزار نفر شروع به حرکت به سمت مناطق شمالی کرده‌اند.
🔸
شهر صور طبق سرشماری سال ۲۰۱۸ بیش از ۱۶۰ هزار نفر جمعیت دارد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438335" target="_blank">📅 17:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438334">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بازگشت خطوط لولۀ پتروشیمی‌ها به ظرفیت تولید قبل از جنگ
🔹
آواربرداری، تعمیر و ساخت بخش‌های آسیب‌دیده واحدهای پتروشیمی به پایان رسیده و اکنون تمامی پتروشیمی‌ها می‌توانند با ظرفیت قبل از جنگ تولید داشته باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/farsna/438334" target="_blank">📅 17:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438333">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8HAqinqwt6_cQzXbHlsO1fC0oYNKKBOSiUiV_X_PnpIG8CFztnYtJ-UD5RaO7uLgJ7Dx10cd9h8Sy5C3IT3ryW3ju6-iXtAqAdC_BQhKTn3bFzmM3nWisJB0pPhdyE1ccgoiN2OWd_kM-sx5bTNTX7WwlAq_xuRZ7jdHQt3QvmWa5J3LP9StMB21wCEEBg0mynHtpAOsG_iTqLdyImb3L-67zZ5CxWBc-ZgclumT4EA-CQMPvnZW_4ahknUvwwclbLfj0o7PkPp7-51vrgiF84dko7QWw_MmnqxSKJKeuqvVg3ipAfJTIp1JFnrxS6hm45Q-LuJLEJ4lZ_YGrBETA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سقوط ۱.۴۴ تریلیون یوآنی بازار سهام چین
🔹
کمیسیون نظارت بر اوراق بهادار چین امروز اقدامات تنبیهی علیه کارگزاری‌هایی که یک تریلیون دلار پول غیرمجاز از این کشور خارج کرده بودند، اجرایی کرد.
🔹
با این اقدام بازار سهام این کشور ۱.۴۴ تریلیون یوآن از ارزش خود را از دست داد.
🔹
۸ ادارهٔ دولتی جداگانه به‌طور همزمان بیانیهٔ مشترکی در حمایت از این اقدام تنبیهی صادر کردند.
🔹
این یک تصمیم هماهنگ در سطح دولت چین بوده که در بالاترین سطوح این دولت تصویب شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/438333" target="_blank">📅 17:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438332">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کشته و زخمی‌شدن ۸ نظامی اسرائیلی در جنوب لبنان
🔹
رسانه‌های عبری از کشته‌شدن یک نظامی اسرائیلی و زخمی‌شدن ۷ تن دیگر در جریان عملیات پهپادی امروز حزب‌الله در جنوب لبنان خبر دادند.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438332" target="_blank">📅 16:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438331">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833385620.mp4?token=n8D47rm_O1udGeqRQoLBhrirSLRMGx25eVi9TMd4dKA7CEdPyKPrMNoKEAK8-Xqb1_vW1rJ7NrurYWqaJDLm2k3xlygz7pYCZlVWsD3pw5qhfnnX2cIfnXw27uQbez3rMXUdGePhw4ZkTWPFIG_JcRqG5oHNDhX6hODgYWGYeSN1BO9_B73um8ZzDEtFd_CYE3Ydkf40K1c9DlBOsQARBCv3Os-PJZSVGt1UtrxlZ7xptHK3-RsvudqXbusrgQEnK7O28BmNQ_aXVmFpnqPN24wKQbHHYzfALmTgCAT3VmVslDISwqrqaIV4a_E7Z-K3MojKuDj6Tqxbcqm49z6h3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833385620.mp4?token=n8D47rm_O1udGeqRQoLBhrirSLRMGx25eVi9TMd4dKA7CEdPyKPrMNoKEAK8-Xqb1_vW1rJ7NrurYWqaJDLm2k3xlygz7pYCZlVWsD3pw5qhfnnX2cIfnXw27uQbez3rMXUdGePhw4ZkTWPFIG_JcRqG5oHNDhX6hODgYWGYeSN1BO9_B73um8ZzDEtFd_CYE3Ydkf40K1c9DlBOsQARBCv3Os-PJZSVGt1UtrxlZ7xptHK3-RsvudqXbusrgQEnK7O28BmNQ_aXVmFpnqPN24wKQbHHYzfALmTgCAT3VmVslDISwqrqaIV4a_E7Z-K3MojKuDj6Tqxbcqm49z6h3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مذاکره‌کنندهٔ ارشد پیشین آمریکا در برجام: ترامپ با یک جنگ اشتباه تنگهٔ هرمز را به‌روی خود بست
🔹
شرمن: این جنگ نه‌تنها هیچ مشکل هسته‌ای را حل نکرده، بلکه تنگهٔ هرمز را که پیش از این باز بود، به یک بحران تازه برای آمریکا تبدیل کرده است.
🔹
قبل از اینکه رئیس‌جمهور این جنگ انتخابی و نادرست را پیش ببرد، تنگهٔ هرمز باز بود؛ آزادی کشتیرانی برقرار بود.
🔹
اما حالا خود او مجبور است تمام وقتش را صرف این کند که بفهمد چطور همین تنگه را باز کند و محاصره‌ای را که خودش ایجاد کرده، بشکند.
🔹
حتی وقتی این مأموریت انجام شود، حداقل ۲ تا ۳ ماه طول می‌کشد تا قیمت بنزین پایین بیاید؛ آن هم در شرایطی که هنوز مذاکرات هسته‌ای واقعاً شروع نشده و هیچ سازوکاری برای راستی‌آزمایی یا پایش توافق، از جمله پایان محاصرهٔ تنگهٔ هرمز وجود ندارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/438331" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438330">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dArlIblQ71qZe9_0EuIvTTXIxY-GRqVInqMu7RDKoqSdVFkjvP0ffAGGHDT96hc1zvzTBzZtqICRodcUn75nZwRjcf71maBFhLix9xnCdTtjkp6E9WPnzmmH31Bv1SUqRLHm0uBqN3OEDoOyymrXL0OSJ5c5mTwQgxTQX9ZdZ4mon20VRxY-Bc9fsMguMxH_2_XP5djRZRTVGPCTWf-2TcVpWqcZdWPUAGkqDyjJAAfBODZ3lFtw9hi_eQR5PjfEmc22D0Ug_eXKQoXaAH1yT-Tkl-XTQUtDDL5vA6kOgWkjnLs0__D6wRPELs4MLAQuew8SBDvc0xlJfUkLLg47dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتدی الصدر دستور انحلال سرایا السلام را صادر کرد
🔹
رهبر جریان صدر عراق، امروز دستور انحلال کامل «سرایا السلام» و «پیوستن آن به دولت و مسئول کل تشکیلات نظامی» خبر داد.
🔹
سيد مقتدی الصدر با انتشار بیانیه‌ای خطاب به نیروهای خود اعلام کرد: «به دلیل مصلحت عمومی کشور و برای جلوگیری از خطراتی که کشور را تهدید می‌کند، بر خود لازم دانستیم که اعلام کنیم: سرایا السلام به طور کامل از جریان شیعه ملی جدا شده و به طور کامل به دولت و مسئول کل تشکیلات نظامی می‌پیوندد».
🔹
وی در ادامه تأکید کرد که بخش‌های غیرنظامی وابسته به سرایا السلام باید به «البنیان المرصوص» بپیوندند، بدون اینکه هیچ مقر، اسلحه، لباس، نشانی یا هر چیز دیگری داشته باشند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/438330" target="_blank">📅 16:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438329">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZE1DY36yyYMQMzCZamy09XBAQzlo0ZqlBQplEufkafsUcVNUCi_om7njgAJSm3MrH8W4PBRYzSJtJvtwl1pBPQzR6lG5Nk3n9TfNeiMKj9bDEUupj8tq0YG_5ZTIHR3KUSHTbfImJ9wfCdmsdKF63P8EN92uznWDog1Pk2YL4IZtla4Rcy54l7Qcw7OIQKLJkOjn0IIRmMJorjH8nVWjxlx82Wj4JPudebEbJmNwclbzkg_Rhu4KjnJndLGqojHL9FL57UTkcMtV68fxHfkk5F-lCEUh590umotKpo1DCFj9zdCquPf93zHYov5GmddENL-55NUnZnFWofzIkda5mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز هم در خالی‌کردن ذخایر راهبردی آمریکا رکورد زد
🔹
جدیدترین آمار نشان می‌دهد که دومین رکورد بی‌سابقهٔ آزادسازی ذخایر نفت راهبردی نفت آمریکا (SPR) در تاریخ اتفاق افتاده است.
🔹
هفتهٔ گذشته هم آمارها فاش کرده بودند که بزرگ‌ترین آزادسازی ذخایر راهبردی در تاریخ این کشور انجام شده است؛ در آن زمان هم ۹.۹ میلیون بشکه از این ذخایر کم شده بود.
🔹
حالا آمارها نشان می‌دهد که ۹.۱ میلیون بشکهٔ دیگر از این ذخایر کم شده و سطح آنها به کمترین میزان در ۴۳ سال گذشته رسیده است.
🔹
ذخایر راهبردی آمریکا با هدف کنترل بحران‌های نفتی ایجاد شده و از زمانی ‌که جو بایدن برای کنترل بازار در زمان جنگ اوکراین از آن برداشت کرد، واشنگتن هنوز نتوانسته این ذخایر را به سطح قابل اطمینان برساند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/438329" target="_blank">📅 16:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438328">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CV2pgoa8L8iB4amJuO2QMeqOijeOALWFHtA-9gi9RAR3Y0LbyRqzKXAIJFNgJ-hiNW_ccYqavk-uLk0HppcGwj74e_2DEpchopCgD8-KvKePNOqz8WzcxxmS52yVAzKrwoZbWrzVy83OJsDl80MLSR8u7HJx_QteqIYusrfdCQAs072845Teg2PvZ3Ai9FpreMSQnA9zomYrC8BGS0hJVSHX7Sdc7EU_xubzIznVCXNO14oo-H9uN-Ux3q1E0QohPNFDcyZI-G-e1GSQP6ZeHbK_CUNnoQIhbS6qCgyMzA1l17oclKCKJ-orHlOwSaJmqrjxfO9DbYWQ_uOpRcDFBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الزام صنایع به تامین حداقل ۴ درصد برق خود از انرژی‌های تجدیدپذیر
🔹
معاون برق و انرژی وزیر نیرو: مشترکان خانگی برق که نسبت به دورهٔ مشابه قبل ۱۰ درصد زیر الگوی تعریف‌شدهٔ وزارت نیرو برق مصرف کنند، تا ۳۰ درصد قبض آنها کاهش پیدا می‌کند.
🔹
همچنین مشترکان برق اگر نیروگاه ۵ کیلوواتی خورشیدی نصب کنند ۲۰ درصد از قبض آنها کاهش پیدا می‌کند و اگر تجهیزات ذخیره‌سازی هم نصب کنند تا ۳۰ درصد از پول پرداختی قبض آنها کم می‌شود.
🔹
در سال جاری بر اساس قانون بهره‌وری تولید، صنایع مکلف شدند حداقل ۴ درصد از برق مورد نیاز خود را از طریق انرژی خورشیدی تامین کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.73K · <a href="https://t.me/farsna/438328" target="_blank">📅 16:04 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438327">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzmcCqWGA9dOblFQcG232lVSHcMLVzv46_E_4pSTLnd7qTIY3Qaxzog_tkb1bWtI5ZBk7vn3xEjipuQj5FWEbRU_MyQix4jDo7xu-2ZbIE5Kc78yYhPL8dIdU6TB_RxzX_oyDyTV33E2fj7dqpll3tWDQruMNN1ETMHV_UwxZsPgrZr9EKqgBTGnsxiBZGcbHc3AXie7KRKQAopzveQH6sOXdwj6mDD0F_W-jDx97kTdvUZPRFBuvIu4A7dQdj_8cdx0HyyR_2nCL39lbcJOLGdhbuEtetOIkyJ5kcTpe3osdTX88HofqSGvreClOTfp-mZaxpbFL3HcmWj3zohxAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی وزش ‌باد و گردوخاک در تهران
🔹
هواشناسی تهران: امروز در برخی ساعات، وزش ‌باد شدید و گردوخاک به‌ویژه در نیمۀ جنوبی و غربی استان پیش‌بینی می‌شود.
🔹
این شرایط تا جمعه شب نیز در برخی مناطق ادامه دارد و در ارتفاعات استان احتمال رگبار و رعدوبرق پراکنده وجود خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/438327" target="_blank">📅 15:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438326">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18422de433.mp4?token=YgtuGwekCVZmNlLa_uj3myRI-o55ryP9UOTnIFePmmS4vk9OjV7iFSRIsFNQBZCuj7b-Izt8pZmMCh1Z-YdwrYxDeABm7V00j6ERsFRE5UCdkBSWxHhrLQb0b8jrgjtTEI96AO0rrDeZeP8JyXN2Uah96UnhisLy-BjyaGZ33kUmE0Rrp0urKHeSca5j6SShrPPtwUFXlR-LuA6YySTs6uo_arvF5EIH0CfGWhXDxipG0DgZawy1YDQ8O6JXzS1ZKH-MNpQg8dikE_aMsLnz4UNIKUGVUxefW2CmazO_ifUn515ZFRNLbrzzJXh7SqxnFJNKIUhJrF4Dp4Z0s2nCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18422de433.mp4?token=YgtuGwekCVZmNlLa_uj3myRI-o55ryP9UOTnIFePmmS4vk9OjV7iFSRIsFNQBZCuj7b-Izt8pZmMCh1Z-YdwrYxDeABm7V00j6ERsFRE5UCdkBSWxHhrLQb0b8jrgjtTEI96AO0rrDeZeP8JyXN2Uah96UnhisLy-BjyaGZ33kUmE0Rrp0urKHeSca5j6SShrPPtwUFXlR-LuA6YySTs6uo_arvF5EIH0CfGWhXDxipG0DgZawy1YDQ8O6JXzS1ZKH-MNpQg8dikE_aMsLnz4UNIKUGVUxefW2CmazO_ifUn515ZFRNLbrzzJXh7SqxnFJNKIUhJrF4Dp4Z0s2nCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پهپاد حزب‌الله یک گنبد آهنین رژیم صهیونی را صید کرد
@Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/438326" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438325">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IBvRa9T-aBHto9i78p8gl9FbC-wrjsLECERlqvvB0P2kpefFoItGTLGS_JM_eBgDBn7J-3VcxDTeK5F6xeNwuXDkyr0k2P6O0HBHE-OKZPxkkjfmIQ6KjMJFoeXBOpjC8VvqaYLcLzGeBUkhEApq8UbhnUg07cbFwIw6xrzS6x07a0bTXvPsDRnVFyCaaheLfTTIk7lfbP37ecP9DoqdV-EKtEkxYKOb_tR_t8Hguw7wGH9gJX1gcsIM_HMC5QZB3y8eNg1dFwSTVIbqwb5REy-D-3OvjUW5zZJHsvTR76rew4-mJ6AE2danwPt76kLuCJu3FYyqd0UHyQg_4vgxGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وعدهٔ جدید وزیر جهاد برای تسویهٔ مطالبات گندم‌کاران
🔹
وزیر جهاد کشاورزی با اشاره به تحویل حدود ۲ میلیون تن گندم به سیلوهای دولتی از ابتدای فصل برداشت، ابراز امیدواری کرد که سازمان هدفمندی یارانه‌ها در روزهای آینده روند تسویهٔ حساب‌ها را آغاز کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/438325" target="_blank">📅 15:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438324">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ae0b9d8f.mp4?token=ofxOtEln4bSFxBAMyyUQx6R8ijSRGjssPDTCksZLPCfeFNtILvIh6rn8s7C0hku-eCoZx0OaEmpe_Wq2V_YOe8zAAZ6JG-okGsSyjMAdmQFuv-inqskRi2vLctZcFTlTLLKZ-bAUtamGkt-WKEo4abcY_BJQT5p8mX4vdGfWTLq-yVCJWXqPJJrXyw20MW9te7s7ul_1LL6lW7RWuOeGog1nrr6AvvXv7TdhAfSq2HkIlymI0D_Z2FEV7zSTt4XTkOCjRHhBfaI4rUr6qdaBJbOiD7ZFGb9PXkBHRUY4N5KD3qSLMqUhqCmU3u7F4sH45Rf6eNj-abeGv0eyFjdBWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ae0b9d8f.mp4?token=ofxOtEln4bSFxBAMyyUQx6R8ijSRGjssPDTCksZLPCfeFNtILvIh6rn8s7C0hku-eCoZx0OaEmpe_Wq2V_YOe8zAAZ6JG-okGsSyjMAdmQFuv-inqskRi2vLctZcFTlTLLKZ-bAUtamGkt-WKEo4abcY_BJQT5p8mX4vdGfWTLq-yVCJWXqPJJrXyw20MW9te7s7ul_1LL6lW7RWuOeGog1nrr6AvvXv7TdhAfSq2HkIlymI0D_Z2FEV7zSTt4XTkOCjRHhBfaI4rUr6qdaBJbOiD7ZFGb9PXkBHRUY4N5KD3qSLMqUhqCmU3u7F4sH45Rf6eNj-abeGv0eyFjdBWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روزنامه‌نگار فرانسوی: موقعیت ایالات متحده در برابر تمام متحدان اروپایی و آسیایی‌اش متزلزل شده است
🔹
پس از جنگ اخیر یک حس آسیب‌پذیری نسبت به ایالات متحده ایجاد شده که وضعیتی نوظهور و بی‌سابقه است؛ جهان تازه پی برد که قدرت بازدارندگی ایران تا چه حد واقعی است.
@Farsna</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/438324" target="_blank">📅 15:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438323">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9d2be9fc.mp4?token=l96YsUjJ_ZlTl5F-UaLYiMMK-t2KZdywVMc2L7JPkjAIrYm1Z5SN_vBEZpCYZYnluOVxuDsF1_QTGncb0kU3smQp0sg8UoiYtlOjKMAvWJ-Q4LRhlFnDCLIGoSeGIrJjPdj_BYPZa2ImQjiWbm0kle2cwUBiO-wO1NtB_MuoXajX2KNrmYplecNfwXQWVCsQLc3thGBgRCHmMIBSODYwSUmNIluzjlMGqEsLpbgN4nOkLUmvaduHjC09ph2MAhoVBdUEn_O5dLokDw1e_DbayZUUG-6_sLN3oIGjDqAEss_kELf6FIHo0OgOdOdOxen4D190Hcx5NV7wNtPUurE0wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9d2be9fc.mp4?token=l96YsUjJ_ZlTl5F-UaLYiMMK-t2KZdywVMc2L7JPkjAIrYm1Z5SN_vBEZpCYZYnluOVxuDsF1_QTGncb0kU3smQp0sg8UoiYtlOjKMAvWJ-Q4LRhlFnDCLIGoSeGIrJjPdj_BYPZa2ImQjiWbm0kle2cwUBiO-wO1NtB_MuoXajX2KNrmYplecNfwXQWVCsQLc3thGBgRCHmMIBSODYwSUmNIluzjlMGqEsLpbgN4nOkLUmvaduHjC09ph2MAhoVBdUEn_O5dLokDw1e_DbayZUUG-6_sLN3oIGjDqAEss_kELf6FIHo0OgOdOdOxen4D190Hcx5NV7wNtPUurE0wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
نیروی دریایی سپاه: کنترل هوشمند تنگهٔ هرمز با اقتدار درحال انجام است و هرگونه تجاوز با ضربات کوبنده پاسخ داده خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438323" target="_blank">📅 14:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438322">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e3296af9.mp4?token=tJuPAoyvc5LvhLEkpXV_35nLiihxcop4B9M3MQnR2CaQWXVazujh86XbV85UFXGaFXHVUqlTucZNrpl7H77WcUyW2vskiUYVTJ4wQ6od4w-YH32jx-BE_tYSJ-mxX-GeuIfIXnCEVVeJmlz-IaEacKrqJeXAoX8Dx6sg4KiLyKgX2T6TalGRUXiY9YLNye8jiK3sCbs4axMre753V3EXqKemmaLzMwWDz_kdTFoV5fYRwdGJhb5-_Dbk9g5V3xTiubTcfb-dovstM9zCeOUOmc_0Jy9dpZRZWyjva4_d4GVxI5ekv6hHuj6ZKPrzjcAGX-M1UKBGABGwyGPpf41HVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e3296af9.mp4?token=tJuPAoyvc5LvhLEkpXV_35nLiihxcop4B9M3MQnR2CaQWXVazujh86XbV85UFXGaFXHVUqlTucZNrpl7H77WcUyW2vskiUYVTJ4wQ6od4w-YH32jx-BE_tYSJ-mxX-GeuIfIXnCEVVeJmlz-IaEacKrqJeXAoX8Dx6sg4KiLyKgX2T6TalGRUXiY9YLNye8jiK3sCbs4axMre753V3EXqKemmaLzMwWDz_kdTFoV5fYRwdGJhb5-_Dbk9g5V3xTiubTcfb-dovstM9zCeOUOmc_0Jy9dpZRZWyjva4_d4GVxI5ekv6hHuj6ZKPrzjcAGX-M1UKBGABGwyGPpf41HVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: جنگ اصلی در میدان اقتصاد است
🔹
رئیس‌جمهور در نشست با اعضای اتاق بازرگانی تهران: هرکاری از دست ما بر بیاید انجام می‌دهیم و آماده‌ایم تا تسهیلات را اصلاح کنیم و کمک کنیم شما مبارزه کنید؛ چون اگر شما شکست بخورید مملکت شکست می‌خورد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/438322" target="_blank">📅 14:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438321">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdec731a71.mp4?token=qLvXYB23oO8CNmh7OYZZ1YmAY4fl00S_GoBXizaGUZcY3RbW_Uz9swlDBM6LiOGzn70OzHspUBsuVEvb6GBMUCcz_4PqUhJqbX5T_JicOjOMvFZUNI3n3twXKrAuecVf1LVxx9zbvlx5YOlxFCRG3EfMq-iu1i8jls5ks5VMGW0_uRFlfZIA_STAXkW6CSNnDnQYltZphbs37KTae3RfChSfeCvPKl8bmX8fjyzOpz3EfEiOzeoWhweGtUhvtB7SsWBk_Ff4AWod_1Y097iUYxom1GIfboPptV9f_Bhb0eNV9glFgPVcI4wQ-8qQ5I0L7xZerfZ_aZDBDVlFvtNw54DQCE8COyrcRxHukobg12iIh9_d2J3ohzWpDmqPMDDXtbt6x1rvcEhi5C2lV5qOS4CQ5Y3ZL8T-7apsfDEPvvyv2hXi3MEu0YJKDiaGBejJTu13N6MBYaLlmQg3pWuuFj6uu4JaXSt83ikU5-uzvXeBbJ9mXMwJqUAs--c5l15bf8PuyGVqjs_qoQr64mmYh-hesvq4Gpp0qy4Ho0vZzXe0Kqgdi1dgEx9Uee8yC1oN5IHFyoGJ2Y7HxRY4nQW9b4jLVEm07fB9LkYI2hfvfGltABECSIkRCxHqu8S_MR2vZZpJHu83qsAZS05CeItFgK8r-bJln1eVjbdrZGwioIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdec731a71.mp4?token=qLvXYB23oO8CNmh7OYZZ1YmAY4fl00S_GoBXizaGUZcY3RbW_Uz9swlDBM6LiOGzn70OzHspUBsuVEvb6GBMUCcz_4PqUhJqbX5T_JicOjOMvFZUNI3n3twXKrAuecVf1LVxx9zbvlx5YOlxFCRG3EfMq-iu1i8jls5ks5VMGW0_uRFlfZIA_STAXkW6CSNnDnQYltZphbs37KTae3RfChSfeCvPKl8bmX8fjyzOpz3EfEiOzeoWhweGtUhvtB7SsWBk_Ff4AWod_1Y097iUYxom1GIfboPptV9f_Bhb0eNV9glFgPVcI4wQ-8qQ5I0L7xZerfZ_aZDBDVlFvtNw54DQCE8COyrcRxHukobg12iIh9_d2J3ohzWpDmqPMDDXtbt6x1rvcEhi5C2lV5qOS4CQ5Y3ZL8T-7apsfDEPvvyv2hXi3MEu0YJKDiaGBejJTu13N6MBYaLlmQg3pWuuFj6uu4JaXSt83ikU5-uzvXeBbJ9mXMwJqUAs--c5l15bf8PuyGVqjs_qoQr64mmYh-hesvq4Gpp0qy4Ho0vZzXe0Kqgdi1dgEx9Uee8yC1oN5IHFyoGJ2Y7HxRY4nQW9b4jLVEm07fB9LkYI2hfvfGltABECSIkRCxHqu8S_MR2vZZpJHu83qsAZS05CeItFgK8r-bJln1eVjbdrZGwioIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تردد بیش از ۲۲ هزار زائر کربلا از مرز مهران
🔹
مدیرکل حمل‌ونقل جاده‌ای ایلام: در ۲۴ ساعت گذشته، ۲۲ هزار و ۷۱۲ مسافر و زائر از پایانۀ مرزی مهران تردد کردند؛ تردد زائران بدون مشکل درحال انجام است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438321" target="_blank">📅 14:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438319">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a82e25df.mp4?token=Xp6w2Z9dHmDos2qMDOx-lXjIyjMRWptZJpvFrahlMX-fkKYkzSlaZ-_UIfAgXvUbSu1Ar1gBd8CZUKsLBnLZg4NU0J6ERNq3WNNt0tbWJ1wJmgoH8KM_vy8i45HsPaJ_pGaJlnqUPhHcXfPF4PC8atfy5lAGo9UrqMtrFQOi_0q_Se9PvOwd9Z7H1WPed-yOp9TvlXxq7Faj0LlbCXUxBvY0yY-sM4gILKH2eBecNTHB8ybWT4qi3mElM-5VObPjVnbD7j0owWojw2tbHL2jyk9K4eazNIW0ab3tEPBXRwa9Ayj9TU1xEFcRvGzFLYWbn5tmF4yU70FgGJBhYHMQ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a82e25df.mp4?token=Xp6w2Z9dHmDos2qMDOx-lXjIyjMRWptZJpvFrahlMX-fkKYkzSlaZ-_UIfAgXvUbSu1Ar1gBd8CZUKsLBnLZg4NU0J6ERNq3WNNt0tbWJ1wJmgoH8KM_vy8i45HsPaJ_pGaJlnqUPhHcXfPF4PC8atfy5lAGo9UrqMtrFQOi_0q_Se9PvOwd9Z7H1WPed-yOp9TvlXxq7Faj0LlbCXUxBvY0yY-sM4gILKH2eBecNTHB8ybWT4qi3mElM-5VObPjVnbD7j0owWojw2tbHL2jyk9K4eazNIW0ab3tEPBXRwa9Ayj9TU1xEFcRvGzFLYWbn5tmF4yU70FgGJBhYHMQ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس یادبود شهدای خانوادهٔ قائد شهید و رهبر معظم انقلاب
◾️
شهید زهرا حداد عادل
◾️
شهید سیده بشری حسینی خامنه‌ای
◾️
شهید مصباح‌الهدی باقری
◾️
شهید زهرا محمدی گلپایگانی
🔹
پنجشنبه و جمعه ۷ و ۸ خرداد؛ از ساعت ۱۶ تا ۱۸
🔹
مصلای حرم حضرت عبدالعظیم حسنی(ع)  @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/438319" target="_blank">📅 14:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438318">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LIf4ddhPYt2Oe74-diBLiy-dAz4vzYjvSBuey6NM2WoHt5q93zgQlr_tGKr0olUwJXpL9E8oiLMncobqNTt1oCsjDsFbGJEl_1YCtJZkQy2QN5nTzOp1-Q8j2Hi0HNSdcHVNEI8_TYVdQGaATBJuzq-CyHHpFewdWq943BBIzAL4IM7eryFwwh7GP_NKrI3B1XdBk_-WgAdPckFG4F6e-eSuQJiuhKx5qet9jTy2oOw2P4LTUvjraFPFCDtg1B8GGmd4WsfXTkKnEpBK_t3V9hw_pun8V8GzHxBumLiKyiysCPoLvsTtmth1JYBNpasFu2EwMnCKLoT7bVQ0WrE5Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پای پزشکیان به سهمیۀ آسیایی باز شد
🔸
سه‌شنبه شب خبری مبنی‌بر ارسال نامه از سوی پرسپولیس به رئیس‌جمهور برای دستور و دخالت در مورد انتخاب سهمیۀ آسیایی منتشر شد.
🔹
امروز سرپرست مدیرعاملی استقلال در شبکۀ ایکس نوشت: ‌عدالت یعنی سطح دسترسی به قدرت سیاسی، تعیین‌کننده…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438318" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438317">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیروهای صهیونیستی هدف موشک‌های حزب‌الله شدند
🔹
حزب‌الله: در مقابله با پیشروی ارتش دشمن اسرائیلی به‌سمت شهر زوطر شرقی، آن‌ها را در مسیر رودخانه در شهر زوطر شرقی با شلیک موشک‌ها، گلوله‌های توپخانه و موشک‌های سنگین هدف قرار دادیم.
🔹
نظامیان دشمن پس از مقابلهٔ…</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/438317" target="_blank">📅 14:01 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438316">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px6-czso35Hbxlvw4wvDtQpcTHDqNzKbscBjN3nA-HgRZEWlXdl2G-lg14YaKYRjpo7FuTr84UHRfgwd4S3oNbi8-guaQc7jwR15SkQ5_gVjfQ9cxEEGBjK8MREGd6yhWH1J8Bv71hVizSCupRRuk3WLQtKOBfhT__VGXokSyH9p2Y_r3siB53gxoUf05w3GP07-TXxJfrnonQf0LejQ5N_VVeRF4v1Xx1rgtOWsQzLuA46YeYrq5TuDRtPiRiKFSPZlRmX4cOAG5qLMDZpVYqb-1ndRG6PooZMDm4fCw9D54RxIrUgRP5xoZBW4-eKbcT1tHHaEd2zr_oalSiqfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۳۰ هزار لیتر سوخت قاچاق در لرستان
🔹
پلیس لرستان: مأموران انتظامی پل‌دختر از یک کامیون تانکردار، ۳۰ هزار لیتر گازوئیل قاچاق کشف کردند.
🔹
خودروی حامل سوخت توقیف و متهم برای طی مراحل قانونی به مراجع قضایی معرفی شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/438316" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438315">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fcb5a5bf.mp4?token=LT0ENTowFMPS9ynkm99TJBhFcVdYE-o_mUQXAFPlRc9G9hiKqDf_aNFJYGw0cc1YZCeuveR3hgchiH9_AIEU3voFhiVz7DEge6arvkJ5-KwWsImPC7UDQSVDzja6YdCGtHAXdiKCUBQKdQGQsOYMuK69QHoHq_z6AJuWZ3-qGrzfPjaCuoYsBorw7Cg-zFylYJuXBLc0-b_ZalmcxLNARcMxYTtg5DRZkB13TuDGC5SXsq9aPUeoRFBZ_7NZ9fv7FrnhPsH-9pkrXHL8k-yT4sY07ij_m1GXL_zOlsQNPd_p8F2e2O2fZqUAfS8E0lVqloUFallW_KqJ8egBn_WGYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fcb5a5bf.mp4?token=LT0ENTowFMPS9ynkm99TJBhFcVdYE-o_mUQXAFPlRc9G9hiKqDf_aNFJYGw0cc1YZCeuveR3hgchiH9_AIEU3voFhiVz7DEge6arvkJ5-KwWsImPC7UDQSVDzja6YdCGtHAXdiKCUBQKdQGQsOYMuK69QHoHq_z6AJuWZ3-qGrzfPjaCuoYsBorw7Cg-zFylYJuXBLc0-b_ZalmcxLNARcMxYTtg5DRZkB13TuDGC5SXsq9aPUeoRFBZ_7NZ9fv7FrnhPsH-9pkrXHL8k-yT4sY07ij_m1GXL_zOlsQNPd_p8F2e2O2fZqUAfS8E0lVqloUFallW_KqJ8egBn_WGYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا رسانه‌های ضدایرانی دچار سردرگمی و بی‌برنامگی شدند؟
@Farsna
-
link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438315" target="_blank">📅 13:46 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438314">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFEh-oMcKqB7d99fsP8gdk90moAYpAzs3Z-htn-iEJdVOCX1ICyEO2K0yxujxQBPjlVObLWaOrD_HI6digIZB0HFlv_X9h9hUs1TKnTI7RjdZ5Frcq8hYpeGSaigsFoI6SmBdryOLhUIskK2QkssTzLteRubodFFuSxtS6PHs3DdUkmuuXT5GaLti4ls0qS5CTCOlcU2OAOV9cX4uLVa0bdygD7PU26e4f87dsYjz3cMC9PfrvUKQjO64yvXzsQjGNqk5paRFngBDQWVMVG9Pb9sZo737FRubF7AJ40tDn6bghjZC0YYr4A0ncKisKHmWcAJQlFQjrjZiGQxBEWKiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان نقشه‌برداری کشور: دریای خزر کم‌آب شده است
🔹
دریای خزر به‌ویژه در ناحیهٔ شمال آن با کمبود آب مواجه شده و پهنه‌های خشکی در شمال، شرق و غرب خزر مشاهده می‌شود.
🔹
خوشبختانه ایران در جنوب خزر و در عمیق‌ترین بخش آن قرار دارد و عقب‌نشینی آب هنوز به ایران نرسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/438314" target="_blank">📅 13:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438313">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">وزارت اطلاعات: دشمن پس از شکست در جنگ نظامی، جنگ ترکیبی را تشدید می‌کند
🔹
از ابتدای پیروزی انقلاب تاکنون، ۳ جنگ تحمیلی و چندین کودتای نافرجام به سرکردگی رژیم صهیونیستی و با همراهی آمریکا، انگلیس و برخی کشورهای عربی، علیه ایران طراحی شده که همگی ناکام مانده است.
🔹
با وجود شهادت رهبر، وزیر اطلاعات و جمعی از فرماندهان ارشد، کشور همچنان پایدار و استوار مانده و نیروهای اطلاعاتی ضربات مهلکی به رژیم صهیونیستی وارد کرده‌اند.
🔹
دشمن شکست‌خورده در میدان نظامی، اکنون تمرکز خود را بر جنگ نرم، جنگ شناختی و تحریکات اجتماعی با محوریت فشار اقتصادی، اختلافات قومی و مذهبی، ترور، خرابکاری، قاچاق سلاح و استارلینک، حملات سایبری و فعالیت رسانه‌های معاند معطوف کرده است.
🔹
هرگونه اغتشاش، جاسوسی، ارتباط با رسانه‌های تروریستی و اقدامات تجزیه‌طلبانه با قاطعیت پیگرد قانونی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/438313" target="_blank">📅 13:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438312">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/607552d2f1.mp4?token=Vg0uGiJHdduuGuZ_QOy0O23GBEvYIJ593nihOy1btroolBwyESXTsZCUNCBvB53qQCGzu_gQ2ql1gvRTKhehLGh71hB2EP0dEezK1uePbLo386TdNlaw-x0VF4s-g6bo1QO5nH54LQxOnQEgVgaCUy7el48aCYI8IfRwGKtX-pWASLCp1QiINirYYxreOSxijtiz4wpEsvqbdEzyRzi7T_7Awx-FyzSc_3sVQQY8INMd8qTMGdJI3BFhMfw-BMfLVZ4QP8Gy2brCjCcDdux2nJxNq6A63LXxjwdNBcmce92eXQfgA7OsNgCDmNuuBTGcJ1I0JoL1V_3vIDyR3GFBKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/607552d2f1.mp4?token=Vg0uGiJHdduuGuZ_QOy0O23GBEvYIJ593nihOy1btroolBwyESXTsZCUNCBvB53qQCGzu_gQ2ql1gvRTKhehLGh71hB2EP0dEezK1uePbLo386TdNlaw-x0VF4s-g6bo1QO5nH54LQxOnQEgVgaCUy7el48aCYI8IfRwGKtX-pWASLCp1QiINirYYxreOSxijtiz4wpEsvqbdEzyRzi7T_7Awx-FyzSc_3sVQQY8INMd8qTMGdJI3BFhMfw-BMfLVZ4QP8Gy2brCjCcDdux2nJxNq6A63LXxjwdNBcmce92eXQfgA7OsNgCDmNuuBTGcJ1I0JoL1V_3vIDyR3GFBKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاطرهٔ فرزند شهید تنگسیری از روزهای منتهی به شهادت پدرش
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/438312" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438311">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_MBxzCdpTz8pxsJoQA96U3ioahp2v41a18jzFAAG7_8IeJyJbJR-FnnDyGoZURC6I-ykuo6axdfLjqd6hZe_yr7-ThkflWa_oHGvt2orLx2i3zub4Jl5xjt9vUvnQAbiHqF47Fkmr8A7Z6hZb8Gku47gV3nuVHr3yqZsEx2M7cRMOv2hBTlJaQ17B1wXIHuEByh1kTqYmjkh_f1H9w56SWCKKlfkfT8QjPW_BcalV8fhNiovJ5IKxKtjXGrOSoW5E8Asw_5_nv9AB3x5U3dSE5FHQb6Ju3DFpcMTjWHSqN432E3sBKLP3lOLtbTXMFWbmB2Ryo09TgT9Pfg8zK15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شهادت فرمانده ارشد کتائب القسام تایید شد
🔹
جنبش مقاومت اسلامی حماس رسما شهادت «محمد عوده» را تایید و لحظاتی پیش، طی بیانیه‌ای اعلام کرد: در سوگ شهید قسامی، فرمانده بزرگ مجاهد محمد عوده (ابوعمرو) که استوار و سرافراز در میدان‌های جهاد به فیض شهادت نائل آمد، نشسته‌ایم.
🔹
شهدای این حمله پنج نفر اعلام شدند. محمد عوده، معروف به ابوعمرو، همسر او، ام‌عمرو و یاسر، یحیی و جمیله فرزندان آنها.
🔹
محمد عوده از فرماندهان ارشد کتائب القسام بود که از او به عنوان مرد در سایه نام برده می‌شد و پس از شهادت عزالدین حداد، فرمانده کل کتائب القسام، از بالاترین فرماندهان این کتائب به شمار می‌رفت.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/438311" target="_blank">📅 13:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438310">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78120c8ea1.mp4?token=jzJo13eYVeZkAxqaxErtFF_SVxJFxPbuVbcddo7zof6DSLx5f6kyNfyvJf_lpNuCdfuLlfiI_-kCb1cx7eQUUDypXMsDyM6n5n0sqJVVJ62WJp19WUTq0umz2PDrcvf5ir6j62EsnolRC81kJD_RDSu-vNJtWgmqXWora43KWJb5M0PLqYKubuSZAxluba7D5viio1JravWV6HoI8jkDQdjb4t87RGQRqsI8Hcjcpftay40lD_tu4vTkFccPlk6XAG997OyuSlgG7NJL9F8qHnxvGvl2xqd6ItQ83YmFykEcqHyr5gmHepf4KSi1lE0l00ZXS3jLALLV_xHu-AGxiF0fkeKo5OdTNxAfnyzMUA1jA-xEBAPJd78w-j4DX68hcZtIXtvVJREk0Cq8NzWntSQyugTDUMhlwney-4AzRfUWAVgFhcRN3ZA3JDXoks0Cm5TshW_K81wKQ-z8WCR9UZisspPNwqb1hcT7usIt3fUnqsyB3imAgRRdsXes-ciJU_f_Tpqw2IeVlZ8y8gcs9ZTRITiXo7lp_tbe1qwzdlroCMk37n4uTyecy0G8fjDM-RFKg2wlB4kdaDEdicqvNxfI9lTBhA455bGnnsUY0aJ89B_3MuSpsNaMuAGcyZUI0zF9rQmPmVONHw5XbXc4YWBUna3MA-cvtjtfAKs4oKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78120c8ea1.mp4?token=jzJo13eYVeZkAxqaxErtFF_SVxJFxPbuVbcddo7zof6DSLx5f6kyNfyvJf_lpNuCdfuLlfiI_-kCb1cx7eQUUDypXMsDyM6n5n0sqJVVJ62WJp19WUTq0umz2PDrcvf5ir6j62EsnolRC81kJD_RDSu-vNJtWgmqXWora43KWJb5M0PLqYKubuSZAxluba7D5viio1JravWV6HoI8jkDQdjb4t87RGQRqsI8Hcjcpftay40lD_tu4vTkFccPlk6XAG997OyuSlgG7NJL9F8qHnxvGvl2xqd6ItQ83YmFykEcqHyr5gmHepf4KSi1lE0l00ZXS3jLALLV_xHu-AGxiF0fkeKo5OdTNxAfnyzMUA1jA-xEBAPJd78w-j4DX68hcZtIXtvVJREk0Cq8NzWntSQyugTDUMhlwney-4AzRfUWAVgFhcRN3ZA3JDXoks0Cm5TshW_K81wKQ-z8WCR9UZisspPNwqb1hcT7usIt3fUnqsyB3imAgRRdsXes-ciJU_f_Tpqw2IeVlZ8y8gcs9ZTRITiXo7lp_tbe1qwzdlroCMk37n4uTyecy0G8fjDM-RFKg2wlB4kdaDEdicqvNxfI9lTBhA455bGnnsUY0aJ89B_3MuSpsNaMuAGcyZUI0zF9rQmPmVONHw5XbXc4YWBUna3MA-cvtjtfAKs4oKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک مصاحبهٔ متفاوت با همراهی یک گوسفند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/farsna/438310" target="_blank">📅 12:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438309">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY7HupVFETRicJg7D_cXIrcF9fAP6PwScPWiOC2SGTEWotMs13OzjpLudU0i4bODO_K-5r8DHjpZ7XPFq9j7gegvV1anjEZotFe6h5RGN-P8haiEHyRIe26zub9a5Ybr25L-37W8O6w4sSH2X9Lx7oeAW9Abc6qVtb_JOHoU__6wntJsCSLI3JuCQZpBestOD7bvT3lDjib72R6CvpV5q84NVBaO_isTaLJbloPCtgQnn4vsv6ao7WxGTOlqxsXqZTWlxkzSHfS6jNWXvkdKD0YRQ6vovaNSM_1Z-nZU3n4O61f-Sc63hspvAUSm_TlyLjse9pPr5NHQY7GrKrTt1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کندوان به‌سمت شمال یک‌طرفه است
🔹
پلیس‌راه مازندران: جادهٔ کندوان در مسیر شمال یک‌طرفه شده است؛ این محدودیت تا زمان تخلیهٔ بار ترافیکی ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/farsna/438309" target="_blank">📅 12:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438308">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">نیروهای صهیونیستی هدف موشک‌های حزب‌الله شدند
🔹
حزب‌الله: در مقابله با پیشروی ارتش دشمن اسرائیلی به‌سمت شهر زوطر شرقی، آن‌ها را در مسیر رودخانه در شهر زوطر شرقی با شلیک موشک‌ها، گلوله‌های توپخانه و موشک‌های سنگین هدف قرار دادیم.
🔹
نظامیان دشمن پس از مقابلهٔ مجاهدان با آن‌ها مجبور به عقب‌نشینی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/438308" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438307">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YkF2WLKxcd-u0ekqTKmMdUHAPKwemJ88KyMEPC10ieP0miXITJjTA_1uzXm7z8kJ8nvWdTf-SRgI0KNwSgjbW6rF7Fuq-d7TTxGEezM_NDOoshNGFwTsUfHl0Vf3vtmVTbQqo6XYaBLAsLnW6nR8IPTZM8fC6I2u8YtxYbnaBxo7oHpofYckyH9rN71jj29BJ0AavMwK-Cscemd5JKpcGjjB-pzG1wu4TDJu5sKXqAE-i0kUFG78Pgt0nE61L4ukIDiD2aZn0AjYue-Jm48BGnui5EAse8vBULfaZPPEnK6E5Hkg6e3xPuEt9pYpgH0Qf8qTRmcnd88F73clt-YzKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقدیر رهبر انقلاب اسلامی از میدان‌داری مردم سیستان‌وبلوچستان
🔹
هیئتی ویژه از سوی حضرت آیت‌الله سیدمجتبی خامنه‌ای، رهبر معظم انقلاب، به عنوان نخستین مقصد استانی برای قدردانی از ایستادگی و حضور حماسی مردم سیستان‌و بلوچستان در دوران «جنگ تحمیلی سوم» به این استان…</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/438307" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438306">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTCTM6myT6BIsfizM1oRX3CHlFsLZM8NSY304eZJmEun5YeYC1pQ44F4cGgtbghSdmfGc920b32c5IAKgZiT43q1zJ3czEqZdzN8G68OP4E3oVHXIWLli1udBQyhPoB7ENnx5Nvlk8JNaDfW_N7k5kTiqnm_4uSxbVwD8SIKdXX90aXKSfhf9WN9VKjFD8i9rRLrjEQhiKNWKI8HA_vGxliGFGfJGS4UsW70eBJrQxB1L5CHFQtb3sOtihaNfQwyA7Y2jKifuJPXHs4jMQDO0fiOiF8X0mGdYu3j-m6zHKoGTU7cTfuusN4yv5zO_93sk83YQ4LQp_kIi2TwPn0k5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی باقری: موضوع ذخایر اورانیوم در دستور کار مذاکرات نیست
🔹
معاون سیاست خارجی و امنیت بین الملل دبیرخانه شورای عالی امنیت ملی ایران علی باقری که امروز برای شرکت در در چهاردهمین کنفرانس بین‌المللی مقامات بلندپایه امنیتی به روسیه سفر کرده، در حاشیه این نشست و در پاسخ به سؤالی درباره سرنوشت ذخایر اورانیوم غنی‌سازی‌شده ایران، به‌صراحت گفت: «این موضوع در دستور کار مذاکرات نیست.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/438306" target="_blank">📅 12:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438305">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e09b5124.mp4?token=t5vSxOUgxt3FOFo-MkouFgVFnHrKrzDdLAyU2lqTa0hVuAMA5rJ1DXFIxkgjL4_2dUi-AVRo1wM6x_cKviAvWNNnyJnDtIpIiQvJmrw1Z97jAg77wz9QXVTPqx8eggD0QH2YnUbbwiLWgJAuw0oo4ZBWOpL9Kq2vo_0v-YfhNluVTrWfBCf1MkDFCNGTGEqJFyni81NV3LPNtRHrK6Q7zxqNhj0xAJUbaSFioiZqDzL_buIsJL5swrnSJ1YBZERNNO5GPODN2Pm74xK2dfiV438KYgTK-KN-mmpZypYMkW_OsUJWuA6EtWyAPnNNTbdAcS4Cpj6yy3WXNwZiK4DTCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e09b5124.mp4?token=t5vSxOUgxt3FOFo-MkouFgVFnHrKrzDdLAyU2lqTa0hVuAMA5rJ1DXFIxkgjL4_2dUi-AVRo1wM6x_cKviAvWNNnyJnDtIpIiQvJmrw1Z97jAg77wz9QXVTPqx8eggD0QH2YnUbbwiLWgJAuw0oo4ZBWOpL9Kq2vo_0v-YfhNluVTrWfBCf1MkDFCNGTGEqJFyni81NV3LPNtRHrK6Q7zxqNhj0xAJUbaSFioiZqDzL_buIsJL5swrnSJ1YBZERNNO5GPODN2Pm74xK2dfiV438KYgTK-KN-mmpZypYMkW_OsUJWuA6EtWyAPnNNTbdAcS4Cpj6yy3WXNwZiK4DTCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آرزوی اردوغان در روز عید سعید قربان
🔹
رئیس‌جمهور ترکیه: من معتقدم که نتانیاهوی مستبد انشاء‌الله به‌زودی درسی را که شایستۀ آن است، از مسلمانان جهان، خواهد آموخت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/farsna/438305" target="_blank">📅 12:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438304">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4ScGSCsaUPocpXgvt5EjP3AHaAJKNWu0tiBRlHA3gZJd3NSwlYhwmVcOKCRMLOOF3dt5JPHYF-QBIZEnZxU7DTeDejTEl5xAypjwyC-P7GeoO1H3FheITRLFw0Rc6qWYDmQZN4AAyOlpYXzlyo0OTX8boyyeas0AVEWYAnwetqsvdVp409BWrsGf4RDat8xu7JMprCwrZ-xuwilm8vEyU6RycbcjezGC9KCIiNgG1AoakVtmoMwVA8X7qFfs6LwyJ1dl91c3jQzw75r-TiZLMoBsviiLpfY3_E8q1C6kBOIBr2ytzx2dQcJe60p7XlVcHFHy1Uq6On8FZtWtj9a6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تردد بیش از ۲۲ هزار زائر کربلا از مرز مهران
🔹
مدیرکل حمل‌ونقل جاده‌ای ایلام: در ۲۴ ساعت گذشته، ۲۲ هزار و ۷۱۲ مسافر و زائر از پایانۀ مرزی مهران تردد کردند؛ تردد زائران بدون مشکل درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/438304" target="_blank">📅 12:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438303">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbnC4d_F5ZbW6YrxMhV_nEe_5X0tE6KqfJ-_0xfXzdclkIQPyqiVKJCt4-dndmhyR4ORzz6H92Blh45610CX8GxRnHY-9CEYJqWAqyMI4sbqLF6bQqKK2HzDZq7DTqf-jZis6SMavF64jvP7A6tkpLJkFUFCq5217wAMsBqlXhcMwtUioHCSoB6lirthhEMJTj0GVtq4dwlR9zl46wBLnS2lL5e84TpSwl7VGqFL7OaWNtiN_GjwCctPHfI7G0WLVQSNAJFaoQSBHjY0tyAyPPTSgyrNWeBaGtTSSUSLpA7nkmm53u-HVezzFqqbKbkUnjhJcV7on0KnWEsQiCCa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجری فاکس‌نیوز: ترامپ به توافق با ایران نیاز دارد
🔹
تارلوف: دونالد ترامپ، بیشتر از یک توافق هسته‌ای به یک توافق برای انتخابات میان‌دوره‌ای نیاز دارد و هر اتفاقی هم که در چند روز آینده بیافتد، باید در همین چارچوب درک کرد.
🔹
دقیقاً به همین دلیل است که او در آستانهٔ آن است که برای حفظ آبروی خود، پول هنگفتی به ایران بدهد؛ آن هم درحالی‌که محبوبیت ترامپ مثل همیشه در پایین‌ترین حد خودش است.
🔹
قیمت بنزین ۴ دلار و ۵۰ سنت شده و کشاورزان ما برای تهیهٔ کود شیمیایی التماس می‌کنند.
🔹
کاملاً روشن است که ایران دیگر تهدیدهای ترامپ را باور نمی‌کند. توییت‌های زیادی زده شده و از زیر کار در رفتن‌های زیادی صورت گرفته است.
🔹
این افتضاحی است که این رئیس‌جمهور نمی‌تواند از آن خلاص شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/438303" target="_blank">📅 11:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438302">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg_cpoNx2iNQTDMhy1HTrIu3q8S6HdaFR1X5z2O7QnBLZjHAf9fjuwP-EEZjrqyFeQMIbshmO-ZM8Utkho4Q8JCipgQzlKZLhMorcj7zmrT37gQA9FURUTzgaBF-ReowIOWWV7lgWBvI2Klj5LfCIq38fOi2DNjisXGf6T-tl9fgbABa6H0ScrZGehhBNnfmvDwEngO1Zi38NYk32nDsFzGZO8TPNfSqH4hiUwcz-n67FKcvMeHFtvxQ2MUj3bGMMurgpdqxxBUCHIqcSLMlAm6nTLpF4bGLMZTLMojJ-93B-TGGBzZsmsxr0fr19dC7bmsdtIhu54mDTNJgStSBHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مشاور رهبر انقلاب در امور بین‌الملل: ضامن عینی بقای توافق، تنگهٔ هرمز است
🔹
تاریخ گواهی می‌دهد، همهٔ مهاجمانی که با سودای سلطه آمدند، از اسکندر تا چنگیز و ترامپ، همگی در هاضمهٔ تمدن غنی ایران هضم شدند.
🔹
«ملت بودن» اصالتی تمدنی و ریشه‌دار است نه کالایی که با دلار نفتی بتوان خرید و یا اجاره کرد.
🔹
خط قرمز ایران روشن است؛ این بار کاغذها و امضاها تضمین نیستند؛ ضامن عینی بقای توافق، تنگهٔ هرمز است. جغرافیا دروغ نمی‌گوید و قاضیِ نهاییِ عهدنامه روی کاغذ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/438302" target="_blank">📅 11:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438301">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec7f32233.mp4?token=GjgBoYHOrHMDj3k7TdosU5HdQQBbe5XnJNe09dnkyJ8WT2oJfUtkDeCRNntnOCJr-tqiN_zaN8Mw2roN-HDEseasG8mOt5ryDOz_umk_K6DR4hzIuc0_RgXHRmmQuew29ecKYR0fSBPx_wBmty73g-Uh4YLbUp_c2Zg1TP6qvkXIzVx4EunLTEJppWnFsX_dOi9UlsvOlZFrYHYtROLS524RVPmouf2XYXHRTBTNUFuGW7y_MrpU5inK9dWXeOMErcWNNtj_gkHY6Tmn7mEEv0X0DjnPapXL48Vd4Y1Rxs5raJ3aHHdRmdOaa2nHzkQLSHOPnGPyP8S-Ossmux22JFTQy_iNaEuw2doeirHkLo1Xcs5NqxPUR6W5lsBB5iaRNk-P_1kkJNgUS09iPZlexjgv8p182l2L1nYdl-chaLk5HRX1WytMjkUIccugylXlojS2A3Y8AmgfAdKo017lZoHlEoGfc56Z6DGWeAvmOgV5QUf-oxnAJ8GkWkcixpuHvb__UTVgrKeRylcXUu9TOrFgUeq-5ns4yR8wlOlFE9k6fdu9CvHlvqaMlAXFcY5pKdbXkP1ESf_Ho_fdQB6mEeRLtcYu8AMPH5lQq3wkRdlRlFa1cRYgRcjkgxUowTsqdrtuPZsMS-6Eh7vF6MS9hkDN8y_yXyOB2SQamOVdZYk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec7f32233.mp4?token=GjgBoYHOrHMDj3k7TdosU5HdQQBbe5XnJNe09dnkyJ8WT2oJfUtkDeCRNntnOCJr-tqiN_zaN8Mw2roN-HDEseasG8mOt5ryDOz_umk_K6DR4hzIuc0_RgXHRmmQuew29ecKYR0fSBPx_wBmty73g-Uh4YLbUp_c2Zg1TP6qvkXIzVx4EunLTEJppWnFsX_dOi9UlsvOlZFrYHYtROLS524RVPmouf2XYXHRTBTNUFuGW7y_MrpU5inK9dWXeOMErcWNNtj_gkHY6Tmn7mEEv0X0DjnPapXL48Vd4Y1Rxs5raJ3aHHdRmdOaa2nHzkQLSHOPnGPyP8S-Ossmux22JFTQy_iNaEuw2doeirHkLo1Xcs5NqxPUR6W5lsBB5iaRNk-P_1kkJNgUS09iPZlexjgv8p182l2L1nYdl-chaLk5HRX1WytMjkUIccugylXlojS2A3Y8AmgfAdKo017lZoHlEoGfc56Z6DGWeAvmOgV5QUf-oxnAJ8GkWkcixpuHvb__UTVgrKeRylcXUu9TOrFgUeq-5ns4yR8wlOlFE9k6fdu9CvHlvqaMlAXFcY5pKdbXkP1ESf_Ho_fdQB6mEeRLtcYu8AMPH5lQq3wkRdlRlFa1cRYgRcjkgxUowTsqdrtuPZsMS-6Eh7vF6MS9hkDN8y_yXyOB2SQamOVdZYk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان نقشه‌برداری: برای نام خلیج‌فارس اسناد ۵ هزار ساله وجود دارد
🔹
واژهٔ جعلی که کشورهای حاشیۀ خلیج‌فارس ایجاد کرده‌اند به سال ۱۹۶۰ بر می‌گردد.
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/438301" target="_blank">📅 11:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438300">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8ed8c99fd.mp4?token=hCXw8vM2Pu4vL5URni7xWDy2NEvWN3AnfpAzBWT3GJsLQqnzAEM9yWH10oq2K04iaWWZXpfGtEGFTHfCcfZrQrd1gf7TeigIEy_SW10aAAt4l24EohM0Q721yzDraZoPiRChT6CwTmhudwja01hrtc_6crnb7vfBO6hUoiANyYMtAvOphNI4x5l09tG_Cr2aJHbXr02_6a1dKSKCAFdQyhJk-oSK0KQIT69h8DfkpWu4jUQOXOpqvFTxo8inHbjdMZGHeCZP21LgTiPAL0ZGUuIpnI0_bkG_Kzva1CV2CTggJsjPZCbVryJFSbJ-PZYT6Tb1WLCpMoJG7NPq_dka-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8ed8c99fd.mp4?token=hCXw8vM2Pu4vL5URni7xWDy2NEvWN3AnfpAzBWT3GJsLQqnzAEM9yWH10oq2K04iaWWZXpfGtEGFTHfCcfZrQrd1gf7TeigIEy_SW10aAAt4l24EohM0Q721yzDraZoPiRChT6CwTmhudwja01hrtc_6crnb7vfBO6hUoiANyYMtAvOphNI4x5l09tG_Cr2aJHbXr02_6a1dKSKCAFdQyhJk-oSK0KQIT69h8DfkpWu4jUQOXOpqvFTxo8inHbjdMZGHeCZP21LgTiPAL0ZGUuIpnI0_bkG_Kzva1CV2CTggJsjPZCbVryJFSbJ-PZYT6Tb1WLCpMoJG7NPq_dka-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازداشت جاسوس اوکراینی در مسکو
🔹
ماموران امنیتی فدرال روسیه امروز مردی را که مظنون به جاسوسی و ارائهٔ اطلاعات مربوط به تأسیسات وزارت دفاع روسیه به اوکراین بود، در منطقهٔ ریازان مسکو دستگیر کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/438300" target="_blank">📅 11:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438299">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
خاطره شنیدنی از حضور رهبر شهید انقلاب در خانه خانواده شهید آشوری
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/438299" target="_blank">📅 11:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438298">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b86d6fa10.mp4?token=UkfHf6UO0_Lih5e02rldq5eXge7ZyURA9O5t9fjKNNsjyTLbYsGcP43Wtgh8QCGMue35zATZDOJFzC4nLq4-3ZJ9Oh50GZtduQVGmwRN6UXZTwOMcAOhA6Xo93prX0ynG4z1o5idW8ainldlKfI6VcRkJfT-IKVn76uu7yLjmNRJ4VbTHeRA7L2ElW5zP9KXP3xfGqAXgipnUNVnw8iKdf75wk7JJEHTJP9ZM90sqDX8WzKtC92jShPJGIADI7QuqAg2TQuVAlhdecKH_-79-uLv7FlDc9ERgGtU1F8RQoEQESqjfAQdxZEA_5zYR_wBcwZTL_jZo_Jr4_ivMg1csQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b86d6fa10.mp4?token=UkfHf6UO0_Lih5e02rldq5eXge7ZyURA9O5t9fjKNNsjyTLbYsGcP43Wtgh8QCGMue35zATZDOJFzC4nLq4-3ZJ9Oh50GZtduQVGmwRN6UXZTwOMcAOhA6Xo93prX0ynG4z1o5idW8ainldlKfI6VcRkJfT-IKVn76uu7yLjmNRJ4VbTHeRA7L2ElW5zP9KXP3xfGqAXgipnUNVnw8iKdf75wk7JJEHTJP9ZM90sqDX8WzKtC92jShPJGIADI7QuqAg2TQuVAlhdecKH_-79-uLv7FlDc9ERgGtU1F8RQoEQESqjfAQdxZEA_5zYR_wBcwZTL_jZo_Jr4_ivMg1csQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ دیوان عدالت اداری دستور توقف مصوبهٔ ایجاد ستاد فضای مجازی را صادر کرد
🔹
دیوان عدالت اداری اعلام کرد: در پی طرح شکایاتی دربارهٔ ابطال «سند ایجاد ستاد ویژه ساماندهی و راهبری فضای مجازی کشور» هیئت تخصصی صنایع و بازرگانی دیوان عدالت اداری با احراز ضرورت و فوریت…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/438298" target="_blank">📅 10:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438297">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G05GMvbSvGPqIkKSF2uciIi8lQzOF0gRx2PncfB6KVw-CKXYc9Z96iswiry1Ps5EO0X1t1N764KmsLXIXvUOvUPAvU3wS3BvDSkNN0IcRppzHfArWS6GwR5czPk5gtqgPw69ko2SNIKMFyejWSYv0NTtcCcjD4SE5AcKqs2NL4P8i4hty7iX65h1q18MwWABezDFM_VremA_pwDMkx3rdt9qed7tpIvhSPw7QQweL4LvhtMSsix5zD1hw6SddpTp0DZ-JLAad9PzjQP8PaejPTiQTH0GkdoWHX_A1jXJuxsM0AG-L3AlV6TEA9Hx1d3JjMPuklkVe8kMu5l5g2uLKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل از نگاه کاربران بزرگ‌ترین تهدید علیه آزادی در آمریکا
🔹
«توماس مَسی» نماینده جمهوری‌خواه کنگره آمریکا، روز گذشته در یک نظرسنجی در فضای مجازی از کاربران پرسید: «بزرگ‌ترین تهدید علیه آزادی در آمریکا چیست؟»
🔹
بر اساس نتایج منتشرشده، ۸۵.۹ درصد از بیش از ۳۲ هزار شرکت‌کننده در این نظرسنجی، گزینه «اسرائیل» را به‌عنوان بزرگ‌ترین تهدید علیه آزادی در آمریکا انتخاب کردند.
🔹
این نماینده کنگره در ماه‌های اخیر بارها با جنگ آمریکا و اسرائیل علیه ایران و حمایت بی‌قیدوشرط واشنگتن از تل‌آویو مخالفت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/438297" target="_blank">📅 10:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438296">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf046f0904.mp4?token=Q_usPW4wRkhTU0GkcIXeU5nSVdpyYQszX32bfkn3R49xDnvCe8cF-zWcFQiLq1wkXuIlbUiQ9WFmpMhVvf8JRS0F-QHiL61U-eSrZx3d7fKQaEtrYOKNBFmEIdsQuMFIOntpNF3uWtfNnm68dSIlF0lWhgdEpXJ_W82WYvTn3J1ZZBtBS-AqPqV4dsP2vtwncavcqBNfbyzJ0aINBuru7Jqm8uoKNcOxazDFHjCrj7uGYo7UHxF8f3ze7kwZF-btuHr4aJRAGH9nS2PuPnxW1lg4R8WDhh7rtZdxPoQmyXTBHbU_Bm-elUKdkOLrFyk--OGdj969I1FM3yJrXHUVWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf046f0904.mp4?token=Q_usPW4wRkhTU0GkcIXeU5nSVdpyYQszX32bfkn3R49xDnvCe8cF-zWcFQiLq1wkXuIlbUiQ9WFmpMhVvf8JRS0F-QHiL61U-eSrZx3d7fKQaEtrYOKNBFmEIdsQuMFIOntpNF3uWtfNnm68dSIlF0lWhgdEpXJ_W82WYvTn3J1ZZBtBS-AqPqV4dsP2vtwncavcqBNfbyzJ0aINBuru7Jqm8uoKNcOxazDFHjCrj7uGYo7UHxF8f3ze7kwZF-btuHr4aJRAGH9nS2PuPnxW1lg4R8WDhh7rtZdxPoQmyXTBHbU_Bm-elUKdkOLrFyk--OGdj969I1FM3yJrXHUVWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
یک کشته در حمله جدید آمریکا به قایق در اقیانوس آرام
🔹
در حمله‌ نظامی جدید ایالات متحده به یک قایق در شرق اقیانوس آرام که واشنگتن مدعی است حامل مواد مخدر بوده است، یک نفر جان خود را از دست داد.
🔹
طبق گزارش خبرگزاری آسوشیتدپرس، فرماندهی جنوبی آمریکا (سنتکام) با انتشار ویدئویی در شبکه‌های اجتماعی، لحظه انفجار قایقی را که با سرعت در حال حرکت بود، به نمایش گذاشت. در این ویدئو، قایق ناگهان در میان شعله‌های آتش فرو می‌رود.
🔹
سنتکام در بیانیه‌ای اعلام کرد که «بلافاصله به گارد ساحلی آمریکا اطلاع داده شد تا سامانه جستجو و نجات را برای بازماندگان فعال کند.» با این حال، دو سرنشین دیگر این قایق جان سالم به در بردند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/438296" target="_blank">📅 10:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438295">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565ab109bd.mp4?token=o8TxwVDhFWuKUBDpay_mo40liuz7Sofe46RGgW3l2qrDc4YtkyZElRSxC9DapUuIEisJiJEdyBpL-KxV8wGn1pmg0X40g66_0iIETpN63JfMkUJpY-xSwVqRmw0YojE8D-BEMgAMj5Qw9ndlKUwjZ-ggr6aP2lDdgOXfhIEi7oaXfHfHxmb-_PRVR4kVXkDad5wUIPoSrSXKAhO8vEZP3Nh5nK6HiCjwOrQt6Np5FBldHEjYK9SNRMhmlNJYANdep9C6iL41Vnu6ahGjWfpSnr1bxSgPAafke83plIkVeE2torDAdFF4KXhZeykGddXzR6DdDkeCqWLcRpWXf66tuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565ab109bd.mp4?token=o8TxwVDhFWuKUBDpay_mo40liuz7Sofe46RGgW3l2qrDc4YtkyZElRSxC9DapUuIEisJiJEdyBpL-KxV8wGn1pmg0X40g66_0iIETpN63JfMkUJpY-xSwVqRmw0YojE8D-BEMgAMj5Qw9ndlKUwjZ-ggr6aP2lDdgOXfhIEi7oaXfHfHxmb-_PRVR4kVXkDad5wUIPoSrSXKAhO8vEZP3Nh5nK6HiCjwOrQt6Np5FBldHEjYK9SNRMhmlNJYANdep9C6iL41Vnu6ahGjWfpSnr1bxSgPAafke83plIkVeE2torDAdFF4KXhZeykGddXzR6DdDkeCqWLcRpWXf66tuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ باشکوه نماز عید قربان در میدان السرایا شهر غزه
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/438295" target="_blank">📅 09:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438294">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03b5f96a2b.mp4?token=VFlyfefhHc9nCRjgrBFloCCSWjNQSFcsfxbflJ0WZ58NQGV2rFhfpl2XO4y8qv26NqKio_z2s10tEVsetugpRlPmb8UbwPNg-C9ms2-1EFdFo5BLP6E0_g0pPk9N8Fpctj3IwX9AEzXKmvWrE0GdSewMpzaaSsP7QIskb7KPqwK1xeMp8msyHkc_4uIoIgPJLsWj800zjjp-dFGhV5gcjrqncW-bCKJbBd7iXn6oz6qqPlQQM7YGjxTDJcuxONwbwQfc_90fLP2ph36SSJ4vXLSgOQGFkDL5ztjgb1W-5RQoIKDkSF2ryDIQvWwIssXFkPAUz2c83sLLjAjZuxL8jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03b5f96a2b.mp4?token=VFlyfefhHc9nCRjgrBFloCCSWjNQSFcsfxbflJ0WZ58NQGV2rFhfpl2XO4y8qv26NqKio_z2s10tEVsetugpRlPmb8UbwPNg-C9ms2-1EFdFo5BLP6E0_g0pPk9N8Fpctj3IwX9AEzXKmvWrE0GdSewMpzaaSsP7QIskb7KPqwK1xeMp8msyHkc_4uIoIgPJLsWj800zjjp-dFGhV5gcjrqncW-bCKJbBd7iXn6oz6qqPlQQM7YGjxTDJcuxONwbwQfc_90fLP2ph36SSJ4vXLSgOQGFkDL5ztjgb1W-5RQoIKDkSF2ryDIQvWwIssXFkPAUz2c83sLLjAjZuxL8jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجاج به شیطان سنگ زدند
🔹
پس از حضور زائران در عرفات و بیتوته در مشعر، امروز هم‌زمان با روز عیدقربان با حضور در سرزمین منا راهی رمی جمرات شدند تا به شیطان نمادین سنگ بزنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/438294" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438293">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4264a298.mp4?token=JLkV1mqlZkdEO3NY2dtKF-fGBXtOfiCki2_W9qDOdEWEqVMDFF0k5N4o5RnuPS5Qj57dXNGw9nGIyt7uIUCDwLxeO51bX1h3KbrBzPoQKg7pBBH-zMJ8i5e6VEtUoG-qPtO5PTcIhKZFGH9ReSuTkGzRuJ7X4zXL1b5E_-BQiFS0mFOJ0RbbSxlIK1cMYC9KD0i0imu4GJsFNKgT8hRCJijSC8I2nDYaq4WpvdLl-4_NtYnRE3QnK9RoYIXSf9Qb0HXYOJvamVZf-O1NR43HtFhBc6482pMLxQeMnGnDpMuMXNaCsbCzGovNENR22qu3k2mSd1CzfcKA7BkVcH3iaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4264a298.mp4?token=JLkV1mqlZkdEO3NY2dtKF-fGBXtOfiCki2_W9qDOdEWEqVMDFF0k5N4o5RnuPS5Qj57dXNGw9nGIyt7uIUCDwLxeO51bX1h3KbrBzPoQKg7pBBH-zMJ8i5e6VEtUoG-qPtO5PTcIhKZFGH9ReSuTkGzRuJ7X4zXL1b5E_-BQiFS0mFOJ0RbbSxlIK1cMYC9KD0i0imu4GJsFNKgT8hRCJijSC8I2nDYaq4WpvdLl-4_NtYnRE3QnK9RoYIXSf9Qb0HXYOJvamVZf-O1NR43HtFhBc6482pMLxQeMnGnDpMuMXNaCsbCzGovNENR22qu3k2mSd1CzfcKA7BkVcH3iaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نماز عید قربان در بین‌الحرمین برگزار شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/farsna/438293" target="_blank">📅 09:35 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438292">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b0f6c0ec7.mp4?token=hHRddmeMPctvBMXFZo4AHpgk89Kc9BlqqY7rA1OSN7gFDr0CwcPvBbS078VYhuEgfcp839JkshOGb7ZEI8-vI0ECQfQt3T7i0RzweAEIXnYcoFN8U8UhWBjkaGOcG7tMD9j8mksRTaxU9eiUT-wvoO4Y_G_fcwcwqtMB9g7SgDFxu_K2GmOuPUyFgdLHeOOxZywhLRZjXTquZFl5Of0JoVVttYx-7YJzBWbqhRPM77dGCJ7BJA5FnSYpmvwVagZWuXDX4dsbasnwWzCoRlLdAis_Y2Yhs0xwGN0eW1yxma48BQYZ862nmdgfRxqPqJ-mDq-KpzToK3R0wT6mooyYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b0f6c0ec7.mp4?token=hHRddmeMPctvBMXFZo4AHpgk89Kc9BlqqY7rA1OSN7gFDr0CwcPvBbS078VYhuEgfcp839JkshOGb7ZEI8-vI0ECQfQt3T7i0RzweAEIXnYcoFN8U8UhWBjkaGOcG7tMD9j8mksRTaxU9eiUT-wvoO4Y_G_fcwcwqtMB9g7SgDFxu_K2GmOuPUyFgdLHeOOxZywhLRZjXTquZFl5Of0JoVVttYx-7YJzBWbqhRPM77dGCJ7BJA5FnSYpmvwVagZWuXDX4dsbasnwWzCoRlLdAis_Y2Yhs0xwGN0eW1yxma48BQYZ862nmdgfRxqPqJ-mDq-KpzToK3R0wT6mooyYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ اسرائیل به غزه هنگام جشن‌های عید قربان
🔹
به گزارش راشاتودی، حملهٔ هوایی ارتش رژیم صهیونیستی، یک ساختمان مسکونی در غرب غزه را در بحبوحهٔ جشن‌های عید قربان تخریب کرد.
🔹
به گزارش آناتولی، حملات اسرائیل در آستانهٔ عید قربان منجر به شهادت دست کم ۹ فلسطینی شده است.
🔹
این حملات یک ساختمان مسکونی شامل مغازه‌ها، سقف یک ساختمان مسکونی دیگر در شلوغ‌ترین منطقهٔ تجاری شهر غزه، یک وسیلهٔ نقلیهٔ غیرنظامی و تجمع غیرنظامیان در مرکز و جنوب غزه را هدف قرار داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/438292" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438291">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در اصفهان
🔹
سپاه اصفهان: به‌دلیل انفجارهای کنترل‌شده تا ساعت ۱۲ در محدودهٔ شرق، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/farsna/438291" target="_blank">📅 09:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438290">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5oN8l0tkh88KsRX2xMiCX_v4of0SAnj3gVeguZUsE72iKm4DUGMfy4hM46hQU7lV__MT7m_RVIyYhIC9PbHJ-cV544HOtam9ruBad63UE7zxrXWG5b0_Po09TCBcxOr4EqG6sAQvr5coQh2cga2feLwNv4BP4kp3znxQ78XcqwUm4G0CIDD2z3OHCpcUiNMxBdpR5ebzB14wBxmENtnkDvPl7UJSNXxa9bfHJCC2KuDU07HC0gGv6MKs_cbofRRA15OQinlLa6KVbbuWQ__r47sIsLyl3Gw3kIRShn9r8BycoAR64OfZMbtLgG1kMwCZTLVSUC52oYfWj3m01ueHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
اقامهٔ نماز عید قربان در تهران به امامت آیت‌الله خاتمی  @Farsna</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/farsna/438290" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-438289">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a2b18b16.mp4?token=JlxsolhslzA-kbCzigESap3sPOugbyI76Wm9O5wldpxWHiit-93b607kF-LMvexexyc2ujk0_u1LFFue_-asU5CMcpBdUeXCE6pKcrJHxuFQdZkC3Xyz-38FFlSY37F1mHnZ_XFhyqBx276tEjd_19zW7dwhzwYbUMAz6hqeFxBFHBO-0jovW5bQJQM2fsPCNhzK6p5EHHd-zFEkSK_y1c4MSUb2bvORvNInBKH3rrTWsglhn03WcX2Vyq1iHEFKKjZrmHMdjWgOWLB5nPdxxb2OXTM6o5qLEzvXMx1LRST3lL_aoo4NXh8vX81N9KTX5u3bMiTiNQAYTRU3d4Cg_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a2b18b16.mp4?token=JlxsolhslzA-kbCzigESap3sPOugbyI76Wm9O5wldpxWHiit-93b607kF-LMvexexyc2ujk0_u1LFFue_-asU5CMcpBdUeXCE6pKcrJHxuFQdZkC3Xyz-38FFlSY37F1mHnZ_XFhyqBx276tEjd_19zW7dwhzwYbUMAz6hqeFxBFHBO-0jovW5bQJQM2fsPCNhzK6p5EHHd-zFEkSK_y1c4MSUb2bvORvNInBKH3rrTWsglhn03WcX2Vyq1iHEFKKjZrmHMdjWgOWLB5nPdxxb2OXTM6o5qLEzvXMx1LRST3lL_aoo4NXh8vX81N9KTX5u3bMiTiNQAYTRU3d4Cg_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامهٔ نماز عید قربان در حرم مطهر رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/438289" target="_blank">📅 09:00 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
