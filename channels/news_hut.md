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
<img src="https://cdn4.telesco.pe/file/IyB3zwg63yVXxj-TvHvl4uTXH648JNkwsWEjyWXL4h4iHNuhSh0qhnvbHwmcjly3aLcKHNp5dSm7s35HJ0W2HUnMz0Rn0l3oftAfWieCAPcZ_4az6EDHp5fJVTjEpAJiTZjR7lazRbuoHe9FvfQez7NbH8SzhhkLPYT6pWUKeHGZif7ZY141EQtjTkcB9F6JQFidq0AF7_ig5CPsExUp1i921XuthlOylNMlaNTTiTx2bbD_66qA0e8ZqzM_cKwa5M0HMHGpi8VDMNaijFLR4XN0uXOsaf3fPqnt9L6JND-mafSBJPZoFWKWReBQxXf_kYwpOcbaaTJ7ZRZs6_nxLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 167K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 12:02:17</div>
<hr>

<div class="tg-post" id="msg-68335">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.
کدام پل‌ها مورد حمله قرار گرفتند؟
⏺
پل گریوه؛ مسیر بندرعباس، خمیر، لار
⏺
پل بعد از روستای لاتیدان (کلمتلی)؛ مسیر برگشت بندرعباس، خمیر، لار
⏺
دو پل مسیر کهورستان، لار
⏺
پل نیمه‌کاره؛ محور بندر خمیر، کشار، بندرعباس
⏺
پل روستای مارو شهرستان خمیر
@News_Hut</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/news_hut/68335" target="_blank">📅 11:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hPgzszBeCI3ocUP6ciKFrAVuB112sRQMNhaStdiG8shryZ_RW76qZt85u55sL_n9LHsb823HUipm0W8R4HxbE6rHLwPhlUSNL5zt5KSSQEM4n0q8zPTkM-YLFhjEBPbQKXhs3WmVRdbHppMKUZmgtbbKmzIvGJtyag6D5VUSeUpoP1G2SFr6kOqPCNxC8ItvahhoyslzXjogbrNMfPX5VB_3q7ZzW-QDs0zw59N1mVZpoq-T6S8ME_mW9hJ-rEvN5m6G8xfJ2bJSBD6JJvB0MMIeKJzBXNnKp8KbS6WDEM2F_ZLfv4kjOuv0pkwajtYpJQ63viHiwLIQ4cMYaE-3lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1vY3k_RcNAjZU2JN1sbRlbkLoJwLevqalReK9JQ5pMmSgj4-ITUes5PPgc4TFgQdPTL9KUSR5LCOJ3kZL0mTL_gmBjEwv8VPVakgEAwiXHhAc0w_b-Xnx5XxKSzdlx8RObxiwgx8MGNuvMx2MtbBWuDYeCEvF0MSA4fhP3XbP4qglYCiysTY508KcEEM_b3E4KRmmWLGy0TGvRM3sIv2V6TdToyLJIN2Jm2lgp7_FrxGCzKUl_CYHUcMgAKF9XXYXIL49oNMfDy_emyRlybtDJ1j3fLbx2YOECFOyVZ0xRKGYAXjhDyMXILFQwDjzJTPY7bAU4Q3e00q4Na1_FJ7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
‼️
خورد تو ذوقمون؛ کج سلیقگی کمیته داوران؛ اسلاوکو وینچیچ به‌ عنوان داور فینال و والنزوئلا هم بعنوان داور بازی‌ رده‌ بندی جام انتخاب شد و بهترین داور تورنمنت خط خورد.
ما برای آقای فغانی عزیز اين چهره محبوب ملت‌ ایران آرزوی سلامتی و موفقیت‌روزافزون داریم
❤️
@News_Hut</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/news_hut/68333" target="_blank">📅 11:17 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b51a5dfa4.mp4?token=OCQfHu6v1UjVsZlBGq9SAnDymjqLF9pnQEj_9sSnweUq0ODtNyGUW4fkGgHsREgy2wLrKiUUzBC1pWkN5EaV26Ame-9MCDyorSWbzu1dAnzgP96aLzRwXG7Iwp5adXJ028uc6I9zDHbCdO9zjhA_Hc44u0Y6azqVsR2aHNEmiobb8gZaE-Rq8bYumr0GvD1bRvPV39FAw6ASZJ4tFRVsWi89Du03_5zAPcofel64mIJ-xdg9NPcGYnmhcoSI7gvTJBQJeRMZ06xk_4lgTeF9a3VVacF0yFdB9aHWmDOHfcRbm9nJGB00DP_XNpkp2iB1TaG4Ya9DveEL64flYreWOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
وضعیت پل کهورستان در محور بندرعباس شیراز بعد از حمله دیشب.
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/68332" target="_blank">📅 10:59 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuMyvMH0SSB_MAKNRGXMROldacrxD1MsTAbb77lw9-2UH-Jz9myIWDtaNBRmFvbTDs7poi5vhngeUlQ_yetQ6TiGhX5Hi-h191Sv5qVutEzJiusieqVlUQ1USizLXGfpekeC1XBNr4THYQhDRljRzoZCOtcIrKtT3r_B9OGkGEKirCPm6YNfE6qdiABBCoboshgfZK8O22RCIGzq32Up7kpvtkQFlmvU30JlSsQ5bY9FCttZOpI9e5ELMmXMfGCYTzLp5mzgSIhzZcufrfaQIFmUpQ2TVLQL9ShmfupaDRMWLq3d3oqdVOGguI-tPsRFgpkmsq29eu564dno1mHfbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال استریت ژورنال:
به گفته یک مقام ارشد آمریکایی، ایالات متحده روز پنجشنبه چندین پل را در ایران هدف قرار داد؛ اقدامی که با هدف قطع مسیرهای تدارکاتی به یک شهر بندری و پایگاه دریایی در تنگه هرمز صورت گرفت—مراکزی که ایران از آن‌ها برای حمله به کشتی‌ها و اعمال قدرت استفاده می‌کند.
بر اساس گزارش سازمان صداوسیمای جمهوری اسلامی ایران (IRIB)، در طول شب پنجشنبه چندین حمله به پل‌ها در داخل و اطراف شهر بندری بندرعباس گزارش شد و بزرگراه‌های متصل‌کننده بندرعباس به استان‌های همجوار مسدود اعلام شدند.
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/68331" target="_blank">📅 10:32 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e60e986837.mp4?token=hwM-u1M_tgAx3N9kJfXmevyNUw-4eryXbdr3uBaUQRuA99w8jCuhD_dmo6Be7H37RBdBfv04WGXMRgARDgcCMsik70MRjJepbEskzS_okN_lcnj6UHQYHo7anAIZ7HDDVX4T6nN0cd_sIUEH5M4SxOqSgBDxeW6uL8dc5JNk8uMtN9Dqi2n2Ea7UJBs-gsWoByyarAreTL6WqYy2LmeqDAFtLhPQbNGhiHOZSCrc1F10s_OWOwMlTcHHetIYD2-WPj8tYjvUHEeoKTZprCW551Ht6PBVp7nHDbgZoVoYVMyAo9bmZFKWbdpFA8Js1ZRJRB0XJOVhDcgcuUbDrOqEyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e60e986837.mp4?token=hwM-u1M_tgAx3N9kJfXmevyNUw-4eryXbdr3uBaUQRuA99w8jCuhD_dmo6Be7H37RBdBfv04WGXMRgARDgcCMsik70MRjJepbEskzS_okN_lcnj6UHQYHo7anAIZ7HDDVX4T6nN0cd_sIUEH5M4SxOqSgBDxeW6uL8dc5JNk8uMtN9Dqi2n2Ea7UJBs-gsWoByyarAreTL6WqYy2LmeqDAFtLhPQbNGhiHOZSCrc1F10s_OWOwMlTcHHetIYD2-WPj8tYjvUHEeoKTZprCW551Ht6PBVp7nHDbgZoVoYVMyAo9bmZFKWbdpFA8Js1ZRJRB0XJOVhDcgcuUbDrOqEyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، تیر 1403:
ما غنی‌سازی را بیست درصد کردیم جنگ شد؟ شصت درصد کردیم جنگ شد؟
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/68330" target="_blank">📅 10:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f47f00f211.mp4?token=IhPoOaYUXpRgSRN8spWbhoWVHb0lLtcQixHeLGZwEld_9fFPa34dqc1f-2IJ4YowEBW_cOmFYPW2AZFRqAAmSnoKJ6Hphx4FXldKA3OEvRjeBznfWlsUf69wRf_6PjZSiKJqB2VznAoUAj1v9b6_NHab_JKPkwcWBRdLvuG7HNZVxcrJffjzdGFLzX_C1rW-1dM1gR6FPBOMImoBzvcL63Qt3nFF0onvDf7_mUpqDfHYEwceKwLqwbGT1u8bP8N-GVgQ5DIBBN0VcCf105tyRNslWzauayZIRGyPuFjpT1RdxuwUZv9zstuCFCtEe-PNhdyL_ZI7vLy6jlACcdji2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تصاویر ماهواره‌ای نشان می‌دهند که آثار سوختگی در محل حضور یک سامانه پدافندی پاتریوت آمریکایی در فرودگاه اربیل عراق وجود داشته و احتمالا این سامانه  بالاخره توسط پهپادهای شاهد منهدم شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/68329" target="_blank">📅 09:19 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68328" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SPm_UAYh2Gd1MRgikMhNpExMzyyghabpA8rKv8rKVj2M6BIAdiPeyb4AaPMwVhjBNVVFeiFmqEUMyHK3virBFfmNMFlknWGzmSu6Ufn7mRnX6HAV-m8d2kYUQuImEX0PDaWUs4HjEA3uFNuBei5Hq0eiDRBfBApxidBUpSHvKXpTB1-zLm-9k8APPb0pIpZMrIlZvdGE85bIGFmdG58bpa9kC025WrvIvJLuUqG70t2WdvlrGZCsZsEbw6W0jUWMapaBka3xQFyZsy7Da-dmJwP_jvKLxtCraVulb3WF7X8z4BgPYC7UjAv5bjA7D0EOgW1C5ZJG6i3qqaA_6zpiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68327" target="_blank">📅 03:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
از سایت موشکی جم چندین موشک شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68326" target="_blank">📅 03:08 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bee400515.mp4?token=I-3_bA4tZw3LmCHDitAtBatEZrZxYYdMEsmMHfcobmWxuyFnuEu3nFZXRiZp6Pqs14uFZTT7rEcdJ5gYhvHYh9levga85I-B-dBVa4wPOMDOMTOlby1SmarY77DrkqsarOOPDvMT4eIsK9iELVsYM_Lo8hBuR9X9nwflmt8pBz0fjqLjNtIr6g6J2UBP9lv3w5ATXOjHX7EBVlBUxheu3jlnFmKYn748P-HW2fYU7CpC8ltYt0EXYgvKMsX-41ijEVP2j1cvfelHnqYNAFrvM_NEfreCKTPKuWA2Pc3geNTni3MtySI3_mLys3n3UQWw_tpeBIGPgMTcyZ0Wd-y-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bee400515.mp4?token=I-3_bA4tZw3LmCHDitAtBatEZrZxYYdMEsmMHfcobmWxuyFnuEu3nFZXRiZp6Pqs14uFZTT7rEcdJ5gYhvHYh9levga85I-B-dBVa4wPOMDOMTOlby1SmarY77DrkqsarOOPDvMT4eIsK9iELVsYM_Lo8hBuR9X9nwflmt8pBz0fjqLjNtIr6g6J2UBP9lv3w5ATXOjHX7EBVlBUxheu3jlnFmKYn748P-HW2fYU7CpC8ltYt0EXYgvKMsX-41ijEVP2j1cvfelHnqYNAFrvM_NEfreCKTPKuWA2Pc3geNTni3MtySI3_mLys3n3UQWw_tpeBIGPgMTcyZ0Wd-y-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68325" target="_blank">📅 03:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه پاسداران به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68324" target="_blank">📅 03:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">روز‌ها و هفته‌ی آینده بشدت مهمه، مردم خیلی بیشتر از جنگ ۴۰ روزه ترسیدن، و مسئولین علاوه بر ترس، بشدت سردرگمن، امکان یه قمبل‌قهرمانانه‌ی دیگه وجود داره #hjAly‌</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68323" target="_blank">📅 02:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.  #hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68322" target="_blank">📅 02:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68321">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g53QVvz594KOjZjlDBgVrF5SvZDZpPCG-7XKGcwFq-UF14Y8UZG-Ly6sXguZF_QWGxha8_E4UonkIeyYpkmH26WnNAIcuVfH2E-uGGwTLgqgNl89510MF2bay9tavUbRgUNvV75s05HYuCmJ0OkVwxZipzoyRZ-69ZVfuKhLqcqj-DTc63TE-WhVCJUfvklxWngppK0DLMyh2noHezxhNmjD_RjThaVjrLBB8TvbbGnH3GQs7kcWuUKcr8oP8Xj-KeHFLpuFM673VQLhBJy1Ffbh2EgkfuZXY7Ak5BpaFw2mxJ1gfBhDrzHNkJxex2d9XMFne78JDxAZkdo0N6QhuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر بخوان به جرایز مهم جنوب یعی تنب‌ها، ابوموسی، فارو، سیری و حتی هنگام حمله کنند باید جاده های مواصلاتی بندر لنگه رو قطع کنند؛ امشب زدن پل بندر خمیر به بندرعباس، مهمترین جاده مواصلاتی بندر لنگه رو قطع کرد.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68321" target="_blank">📅 02:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93c5684acf.mp4?token=Rp1DA2SUkQUihrkFHDbVqwmO_rtP0PbEuKKKRZYVs0HJIWWrCkNxIyN8Z_fdYoPHZb_OD4zL7Kk75xT8BQc12UqrUiH4Ny7lIBB5c7TQpQmLcu_qnI_Yul9BRIkBpvibhR7rU8r_F-qr2Q4eTKrcipXVa4Pfnj8jwcu4NUGJyPjzkrz9ByxhiDZlqyo4mQksgYVOjOGo45MQkvVr18874ncXpfI2D9qrVGv8n2PeiH86Ys3KIpVsoV4IntVwPSZcKwjwUthu8UrT3jzIJdRR71zGJm5gdxeMt0yPszJmVBTwTq0LD1eKkDV0ZVc3doYZSSGqlQK2cPP5H6xQ6fKU3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68320" target="_blank">📅 02:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8a3e60cce.mp4?token=XW4OYRDWEIcvDgby5FG0PCYp22hGunylWu6C6JmcfnRZxboMG9jcLT4J23qluMbBi3rf9Cpw8eVzENMzMdbiUOpqgabXeJKKoLeKdTG_kBimy_HnxI9D46G4xxLZZbqRXmct5mkxZV_laz4g1OrfUxdXYWedna397Mi-zJwBb5UudaTldDb7A0C4VqV-1OTLRmt-apW8MfUCdpWQ3AKIMiKt4ezdB49iftIPyzXerxFDrjbXLR7ConQV432rUb9E0GgfW1Vv-km-bXpZvvZ_9wt2x3hatPMe4z8eQnkGE353CbUKxPDI4lUKfUIEr7ch-6Cvhw5UeSnwOlowDFpSmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
حملات موشکی و پهبادی سپاه پاسداران به کویت
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68319" target="_blank">📅 01:51 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
🚨
در حملۀ دقایقی پیش به بوشهر چند فروند موشک آمریکایی به پایگاه هوایی و پایگاه دریایی بوشهر اصابت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68318" target="_blank">📅 01:47 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
فارس:
دقایقی پیش دشمن آمریکایی یک نقطه از بخش ویسیان شهرستان چگنی در استان لرستان را مورد حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68317" target="_blank">📅 01:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed596f3009.mp4?token=IwVrbsOYV7AidQTZ_ovWmsou52Hfj0D2eAcW6f73M-kS6O0hKv879wV_Jcm8zQ9sj-qrs5nkNYb3ZAmYfLzrM0gjVQ39te5YS4Rkcz8D6iHLEsuCZ1CN1f402RtoCqxM4Ny3ShCEYfE7XoK9WgbXGyi2MAqjaKZAl4-85psx66-Ypo2MGCnnreqiGZm801KKWr9WvRV8MEH3OhOoxuawOhpp2glFvSTcbpR0cytt5yzEZHuRYY6Jojn4vU8FZ1MDFDvMBh0XWohSFUFIvJBRqPNqsMEXZHi5DNYWlkfqbzVcwWpNSTTdMYSDV25uZbhJa3Bw9Bw6Ov6Gdg0mpWCCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68316" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68315" target="_blank">📅 01:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68314">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68314" target="_blank">📅 01:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68313">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5f29b590.mp4?token=OePmuX4dWSXmS7BT8CaxiMy7QK5ILANFuk3ZhDu0VKFtH349m859jothFu7G7aRJrJ9m_VOJmraqhduMnhoFCPxdWIhtC0D_buFw5Da5_1WhfRObw_EfqGKVZWkBZUpk2XrgI3BwaHva49ElSjpjSon2c32YAJPeBbTl7Sa8BcdGCjgJS6G-gkkCYyntSaJ3Kx2Rykqr-7SXAFAz3Pk8g9oQnwitZHH0tTzsZep4vNZbvrSu2H0hY_jjQzP8Rafm_w1jp0-gs08aBg2ruYO7Rqlir2BcuutAz7jT58VP3miYfXUOHmV6ykY0y3siZJvdEGnAXe6w9lmYD7qs3QNGjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو وایرال شده از حمله وحشتناک آمریکا به بوشهر
شیشه های ماشین فیلمبردار درجا ترکید!
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/68313" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68312">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d811948267.mp4?token=psNCTgVd6LmQ2mVrbbsyEe8dKcKutWQrSJlz3S15hEZsotlJrBJoyb8DINqELnImz1GK-r4a77dz-oRseAxBliKwJbNs9BpCzx7SoNAwwFFr02GFd_n_L94a-gK0TxSmOJfc-N7abpOW4td_qp4iZY1D4GFbmVjEb_e4UpB82MkVRVdEKe7qxmLJhvxTeAyXxaYUZ3Se59_MKmgnY9xTMQcUIi58VGdhMHN7I8KYp4nSVINp39THDgAS7JNV2HzKOqW5NAuZmb9jfjrF6_x5xJJ6GGWemAhxFbRe0SiOLT7BxD6QM9TtqyZAoWPqTrBzr2RkxelRsLC8uPCgo-qGznq1IPOsVjEKtM_DZa7xP9J_EeFESAdVVi4dmKWO70LiucszqzqVR73GOaN7fKnHZh2kSdA7IaeYFl3Cb9E7OygrhNxonCZ31M3aKpnzAbCImNipL0V4U5pGb4OsFl5nd4sWVPHxO0szdTfcO-3MMJBYGgh1mcCIgqSGCITCa4emfZ8mqsQlw3wx8o_Dhw76KXVkH6qFox8OJYgFxkbvXUZCcPDZmJNi0mXzKulsQzQsH-lEy6pvAHEpy53XzH61fUEIvPilCjbCnfIfKEM477TCoh_ewCf8BPkV0LT4A8sxI0wkYJSWH3JfZ11FdRX0EJJ0hTTaoYlRq6ozmfZRrJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده آمریکا، دقایقی پیش تصاویری از عملیاتی که دیروز بر روی یک نفتکش ایرانی انجام شد، منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68312" target="_blank">📅 01:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68311">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">دیشب که داشتم با دوستای جنوبیم حرف می‌زدم، می‌گفتن حملات بیشتر داره به سمت پادگان و و قرارگاه های نیروی زمینی کشیده می‌شه، حتی دیشب مثل اینکه به پایگاه لشکر ۹۲ زرهی هم حملاتی شده...
امشب هم که خودمون با چشم دیدیم ته حمله به پل‌ها آغاز شده...
حالا سوال همه الان اینه که آیا قراره بهمون حمله زمینی شه؟!
اولاً اینکه ما در جایگاه تحلیلگر نیستیم که به این سوال، جواب دقیقی بدیم، ولی شواهد اولیه داره اینو تایید می‌کنه، اما وقتی کمی عمیق به مسئله نگاه می‌کنیم خیلی موضوع فرا تر از چند تا کلمه‌ست و عملا داریم از یه لشکر حداقل ۱۵۰ هزار نفری حرف می‌زنیم، حمله زمینی به خاک ایران، برای آمریکا بشدت پرریسک و پر از تلفات انسانی خواهد بود، ولی اینکه دارند شرایط رو برای تصرف جزایری مثل خارک فراهم می‌کنند
اون هم به قصد فشار بر جمهوری اسلامی،
یک موضوع دیگه و موضوعی محتمله.
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68311" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68310">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/861fef7828.mp4?token=bls9ncRUJZhEfgBYOdIsggx8twFExkpz2eXDRgYU4TzHxRt8LQEvYovqjhbX7cJIrR8cqDe2s4hwizlZBOOGffPwmSjbpjiuhxxlQQPxMqjr0Np5I36ZUHibTDMGfRJwb4CGbHx6CdHNWQDkMlHr81YKGu6ZFhLk-r5G4NpQrLA2af5iqRyBG1M8bKyQnX8OhYylylNiyuAR4ujXsw51vva0-GyMdMqqm-BTjUCsPQ3OMKfqYJdcfyHz7CVJrhWLJrXVMdIJs5xyMq3n_EjDDZ_VHskDVnYJk0ILQYaKFQmXNjw1g0alkpsZimUdhcTg8NCP4cgbMpX92zHzCDEO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/861fef7828.mp4?token=bls9ncRUJZhEfgBYOdIsggx8twFExkpz2eXDRgYU4TzHxRt8LQEvYovqjhbX7cJIrR8cqDe2s4hwizlZBOOGffPwmSjbpjiuhxxlQQPxMqjr0Np5I36ZUHibTDMGfRJwb4CGbHx6CdHNWQDkMlHr81YKGu6ZFhLk-r5G4NpQrLA2af5iqRyBG1M8bKyQnX8OhYylylNiyuAR4ujXsw51vva0-GyMdMqqm-BTjUCsPQ3OMKfqYJdcfyHz7CVJrhWLJrXVMdIJs5xyMq3n_EjDDZ_VHskDVnYJk0ILQYaKFQmXNjw1g0alkpsZimUdhcTg8NCP4cgbMpX92zHzCDEO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
فرماندهی مرکزی ایالات متحده:
تفنگداران دریایی ایالات متحده از «یگان یازدهم اعزامی تفنگداران دریایی» در تاریخ ۱۶ ژوئیه، عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «وِن یائو» (Wen Yao) در دریای عمان اجرا کردند.
تا به امروز، نیروهای آمریکایی مسیر سه کشتی تجاری را که قصد عبور از سد محاصره را داشتند تغییر داده، یک کشتی را که از دستورات پیروی نکرده بود از کار انداخته و برای اطمینان از رعایت کامل محاصره دریایی جاری ایالات متحده علیه ایران، وارد یک کشتی دیگر شده‌اند.
تنگه هرمز و آب‌های پیرامونی آن همچنان آزاد و باز هستند؛ مگر برای کشتی‌هایی که قصد نقض محاصره آهنین آمریکا را دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68310" target="_blank">📅 01:02 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68309">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68309" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68308">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVBqNEjct0iu3VwvMzsCtGFh2xg7PVaRwx8uPr6gaNa7_WESD2oxc5htInavXmBKPS1NIaaFhWFfzd0-DCA5hE8qf2Ke_BNaqoTMF1fb4IaXK4SATjNhf4I7_ohApw68UfvXq8bzELpBhm3NFtx_EuAqdiKp3DDEOu4P0VWUtdtpcd3ONhcxbajKqp9cvXRYa16LKXGFIfFD6iHhsCUOsXDv48_-Q1WGyvFfYQPnBxndHG4bQMrfmBaSLJUC5G-GVxc4jWa9yFYB6Dw5Yi9LtoTJkV8twdv1NzofRQrcdjGqoOSqe6ow1M-SdxxeN6vaNAzq-R6A_mxD2p3jqVdJtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68308" target="_blank">📅 00:55 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68307">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
دفتر فرماندار هرمزگان اعلام کرد که تا اطلاع بعدی، جاده‌های زیر مسدود خواهند بود:
جاده بندرعباس - خمير - لار به طور کامل مسدود است.
جاده کشار - کاهورستان نیز مسدود است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68307" target="_blank">📅 00:46 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68306">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYABo8Kl6_gfrKak7Ods_Lij3ygi3WkxRvMSaP-p3jWefwwZbb4D3XQL4mpnfuZ-ec65WcEAQqXXNUyEZCST6_-1UDjw5-8umKnHmZ7VZU3Gso98E26sctcM5c1XNeQctBrYWXM9Q6ZgKpqMEAXPujIdq6fmfZiqrsARobO9p_Bgor9czvqnpvVN5N-_DxszdsNKkA_kmSVejdlxSLi1k7CAOcSEgULTTjoExWfngPVg_FNcA4GxZXDr5TZvSTHEO-KNYlr440jRvotONJ1fAplxDJXHh2Mddi_m0Meg3yoLhZbF1RBHrdAAsU7KsfGfjUkxj_4YBRlfPnfRMf-eUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رشیدی کوچی :
⏺
«حمله زمینی به ایران از سمت جنوب رو قطعی میدونم و به نظرم تنها دلیل تأخیرش، گرمای شدید هواست.
به نظرم تمرکز حملات آمریکا روی مناطق جنوبی هم در همین راستاست و ایران هم تا الان با هدف قرار دادن عقبه دشمن در کویت و بحرین، اجازه ایجاد مراکز پشتیبانی رو نداده.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68306" target="_blank">📅 00:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68305">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLI7X-8wy0zlyu_pohhqfqugx_9Qd_QP-PvA6En1exGrN1AK6EXZyjTEYsK8jOuzMhgp3Jn2PsFa6hKjToeMpun7tlWzCuuoGMb2Q5HBCoCmDCEmvZlLBXCxLWAQj-bZ6FDztKK0ZkXRfoJlE2en09tvnev7p8oLD1-Xv_bC0mb0ttHR8j1gffNAQD8EsaIBNScWQoWNOJXOZnys-lEAoujCtaWYoyX57BOEBo6hqQ80R86xdxta6KxL8bUT1i35Yy0JahagKzPFAE0NVFhk3vxhnXaBXaBpkJ1HvpGi5oGmcuPD07y4ufg5V-rOqQ65ANC2LOPOlNn-umQQUfShIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وضعیت پل کهورستان، محور اتصال بندرعباس به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68305" target="_blank">📅 00:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68304">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dX9bB_aVybAN4sjv3AZoAUyMslne_opfgrWk73V0iKqLqD68mIv1IHwlphN8_HvZzpkl5goN_sEMcDB4kNHu79X-Ba1Fye_5rp4egyziTuTEn9oNiCfetmf87QZ1hmcUgKmoIxfsjjxoX_UZl1_ThlvbBmCEAb-QdAmFBY6ORlOt6KKRYG96bbPDEWvfh92j0tmH0DQ32Kx-GIfBYC6aanV5wquwAip5I0lDrafGkoWh3Ry4s1b3yBttE6H6kPU62hwVdgKoTyZNRic81Fn7KXD704DHaDsoMDz2LH3o8XHH7ewI5AkTrId0rfgZCabBV6OGBuz0XX-lyYWQpEnQCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت   @News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68304" target="_blank">📅 00:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68303">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
راه‌آهن بندرعباس مورد اصابت قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68303" target="_blank">📅 00:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68302">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=RXLV5KSMaCceQzIfZoooNoeNPiwmh11sMH-0Y78UbixBacWER8Cq__DFA3h-bREYTovZwdfmKzhBVj0a0jPHx0cE-1mVbUN5cZbG5KbzCnQTN4jeH0HzioczfGc1T8HaFd6mQIndmgvVqnf87K9xPrgr2dXtKqssxFApsW4eBXA_nuhkzoOhpd45JkQLlrnjsjQTjV5T2j9V-hFsAE1mAEY_ntDSRcn2KJUXO-PUVbvS0b5BM5N-jBNXqrGuSo2ZPweOmGyrtGiF-llnybJM7JANgjhCiDnxLtEsFiumBSeP4zc6PrzKkdcjZp93BM5Uj4WfczEEN6rM-xnx50Nrog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5f357e145.mp4?token=RXLV5KSMaCceQzIfZoooNoeNPiwmh11sMH-0Y78UbixBacWER8Cq__DFA3h-bREYTovZwdfmKzhBVj0a0jPHx0cE-1mVbUN5cZbG5KbzCnQTN4jeH0HzioczfGc1T8HaFd6mQIndmgvVqnf87K9xPrgr2dXtKqssxFApsW4eBXA_nuhkzoOhpd45JkQLlrnjsjQTjV5T2j9V-hFsAE1mAEY_ntDSRcn2KJUXO-PUVbvS0b5BM5N-jBNXqrGuSo2ZPweOmGyrtGiF-llnybJM7JANgjhCiDnxLtEsFiumBSeP4zc6PrzKkdcjZp93BM5Uj4WfczEEN6rM-xnx50Nrog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ویدیو دیگر از پل کهورستان
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68302" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68301">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
تسنیم:
آمریکا شروع به زدن زیرساخت ها و پل ها کرده.
اونا به شهرستان بندرخمیر و بخش کهورستان حمله کردن و پل ارتباطی بندرعباس به شیراز که معروف به پل بندرعباس - کهورستان - لار هست رو هدف قرار دادن.برق مناطقی از کهورستان هم قطع شده
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68301" target="_blank">📅 23:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68300">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=Hfn8OINgK9Ax9fhgLRWefnnzsCtCfYBhPCm_MZ7Qg7w2WzcB2KMmB6ZgLy1lBBOe-5wVGFWOB9jEnnPhIt_KYkyyttvpskDj1brd6yEhH47bpUl7Qf7FtqyApZZZgNqpd_sLSo31SifZ229vDZXu02V-SF0OyIcGaChlA3sFn0Rr-rqHxNJ1CHoxys1hny_s0xsuxSdfM-Nln44yjRS2TBeDJQkRuzJf0S-G2kBDkJZcECgxxbYTE3Vdu6k23B8V9ZT2ULaekiAC7Bj7ei4DdD3ylTMAuqwpIBOgJsLs0sblYEMfiGmt53XDoCMuaHS8m_cB1THIZmJhFACwfM91Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e073aa854.mp4?token=Hfn8OINgK9Ax9fhgLRWefnnzsCtCfYBhPCm_MZ7Qg7w2WzcB2KMmB6ZgLy1lBBOe-5wVGFWOB9jEnnPhIt_KYkyyttvpskDj1brd6yEhH47bpUl7Qf7FtqyApZZZgNqpd_sLSo31SifZ229vDZXu02V-SF0OyIcGaChlA3sFn0Rr-rqHxNJ1CHoxys1hny_s0xsuxSdfM-Nln44yjRS2TBeDJQkRuzJf0S-G2kBDkJZcECgxxbYTE3Vdu6k23B8V9ZT2ULaekiAC7Bj7ei4DdD3ylTMAuqwpIBOgJsLs0sblYEMfiGmt53XDoCMuaHS8m_cB1THIZmJhFACwfM91Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
در کهورستان بندرعباس یک پل هدف گرفته شده.
موشک خورد به وسط پل، تانکر سوخت نابود شد، راننده مرد، یک تیکه از پل نیست، کسی این طرفی نیاد...
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68300" target="_blank">📅 23:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68299">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
پل ارتباطی بندرعباس به شیراز و معروف به پل بندرعباس - کهورستان - لار مورد اصابت قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68299" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68298">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=hUQNmgKSWP4YI07ydQQlIrZZII3_HAvZhh7pcmMj1o04YR6MG6ubE8Mdjil4kFFmkHHLPH7UJvJLb07uWUIIpMi4nM16jorG00oHYc6UB1HQ1GhiBh6xTdJHf0-nGwXLtzOlOKJI1EIbzKlnSlpHpS01vgQgZeSK2sZsyxPwMnVjFNfZyZA7f4R4bJOtOe0jvBk6SR-sqh51D38GLPnTqIz2KpPfViQjj6XB4VXJi6OONsnqXH4drg887zBq3lpKd7tX1H3IKXFywjD-wwLNFaLZr0x-0_7aANG-kQDS2PinbMmVHWxO9_q211Ifl3poEtuYSGn-QnZ_Mzj7q063GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a71beb824.mp4?token=hUQNmgKSWP4YI07ydQQlIrZZII3_HAvZhh7pcmMj1o04YR6MG6ubE8Mdjil4kFFmkHHLPH7UJvJLb07uWUIIpMi4nM16jorG00oHYc6UB1HQ1GhiBh6xTdJHf0-nGwXLtzOlOKJI1EIbzKlnSlpHpS01vgQgZeSK2sZsyxPwMnVjFNfZyZA7f4R4bJOtOe0jvBk6SR-sqh51D38GLPnTqIz2KpPfViQjj6XB4VXJi6OONsnqXH4drg887zBq3lpKd7tX1H3IKXFywjD-wwLNFaLZr0x-0_7aANG-kQDS2PinbMmVHWxO9_q211Ifl3poEtuYSGn-QnZ_Mzj7q063GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملهٔ آمریکا به یک پل در بندرعباس.
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68298" target="_blank">📅 23:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68297">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
طبق گزارشات اولیه، یک پل در بندرعباس هدف قرار گرفته است
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68297" target="_blank">📅 23:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68296">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
به گزارش ممبرا ساختمان مخابرات بندرعباس هدف حمله قرار گرفته
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68296" target="_blank">📅 23:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68295">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
حمله به ایرانشهر سیستان و بلوچستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68295" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68294">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bzi3s8Lj-85q_zS5fgUdDfiFW8R50TZDmtAAtxN-SvhZJJnGw_mDZPTKRfG3IDXLSONOdH7IW4NMisHWmxT0oL8gqmDK1qkWC6aC8N5m60Fna4fK1fOSAbb5yK9k3cbK7ucaqe6an9JpKYYxgbGbpjGeufVyj2qGRk47INAgD5r2gYNq7f7Y9n35C7LM9wRco6uAEwDps7VwNiZCDHYj5OyjZh02YMAMSwb93ieALQixABNqjqeS_0tIaqgS0AKgzdWxy-qFnsFscCm0D_iLSHbgvAiORRPek2TYMVEEBJqj5M2NgSdn-WKGjIrHyUSCRG6cTp3uSkarlQyqbnXOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68294" target="_blank">📅 23:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68293">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZXaA74PLv-XRAaM9kDeUubWcGI8oXA1EOjZw824SCYVuehMpJzz2aqHyFF0SSSpfv3DrcYqCCx8LLs2s1kecVDrX74TNm4kJJk73NGl2nS9RQh90ko0YS-utd72mIzVmuGroQgiqWtuwORzId9mH9QQJfviOZ-FP6yKUNYl8eG5zpv6fpGsahQ7VAMR7PifPPdKoHsFSoNHqc6Z8imqE5f9SsNCLFVnICJKDf3mllHF8UySzu77IrE-oJGnijz01AVg8cNvi3s_N_1eIPqG14tT6iqDlk3VJY3XvZgcGIiGxQm-ptx2R-0mhqXXAIXO_dLwJr1Wg02VPrk4nrDhJgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وزارت دفاع کویت:امروز جمهوری اسلامی چندین تاسیسات حیاتیمون رو هدف قرار داد.
از سپیده دم امروز، نیروهای مسلح 32 پهپاد متخاصم را در حریم هوایی کویت شناسایی کرده‌اند؛
این پهپادها رهگیری و با آنها مقابله شده است
این تجاوز شنیع ایران چندین تأسیسات حیاتی در کشور را هدف قرار داد.
علاوه بر این، رهگیری اهداف متخاصم منجر به سقوط آوار در مناطق مسکونی مختلف شد که خسارات مادی به بار آورد، اما خوشبختانه تلفات انسانی نداشت.
نیروهای مسلح بر تعهد مداوم خود به انجام وظایف و تکالیف خود با کارایی و شایستگی، حفظ آمادگی و آمادگی مداوم برای تقویت امنیت ملی و حفظ ایمنی شهروندان و ساکنان تأکید می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68293" target="_blank">📅 23:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68292">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
پنج انفجار مهیب در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68292" target="_blank">📅 23:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68291">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به قشم و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68291" target="_blank">📅 23:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68290">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromS-</strong></div>
<div class="tg-text">داداش ما الان تو کوچه ایم تو اهواز بچه کوچیکا ذوق صدا بمب رو دارن</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68290" target="_blank">📅 22:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68289">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان  @News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68289" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68288">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=Lq4yGS8yAxba7O0qEPsgoq17Q8dqUSdaD6zhASeEVVMeaVDgqnIDs4N8-LM9qOvuuJm1JAbOQqYsBsgep1Gc6TMhiNgOd_9UZLEXiS-bUmHhIjOYqJolgcH8SfC4IpTs39DNkB4HE6k1rnKzA-BhQo9DXgcQUP09UByGixSH6Zn31h7QfEtFJN9X-xTDfGNkw4ciR3U4NM3VGnCe91jvaOtw9zcz35UpyFza8efr3SUuYRt0QunHekAPUIy3sVRmvqCvj02iF68Xwa9yy_FRKBjLB54QWlMxugOLvZG-xLDs7V6y8DM5UjLEcM73jwnpk3HKEcLMXgA7LxdZDBtliw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14dca3521c.mp4?token=Lq4yGS8yAxba7O0qEPsgoq17Q8dqUSdaD6zhASeEVVMeaVDgqnIDs4N8-LM9qOvuuJm1JAbOQqYsBsgep1Gc6TMhiNgOd_9UZLEXiS-bUmHhIjOYqJolgcH8SfC4IpTs39DNkB4HE6k1rnKzA-BhQo9DXgcQUP09UByGixSH6Zn31h7QfEtFJN9X-xTDfGNkw4ciR3U4NM3VGnCe91jvaOtw9zcz35UpyFza8efr3SUuYRt0QunHekAPUIy3sVRmvqCvj02iF68Xwa9yy_FRKBjLB54QWlMxugOLvZG-xLDs7V6y8DM5UjLEcM73jwnpk3HKEcLMXgA7LxdZDBtliw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
شلیک موشک از کویت به خاک ایران
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68288" target="_blank">📅 22:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68287">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
اهواز رو دارن شدید میزنن همچنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68287" target="_blank">📅 22:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68286">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
دو انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68286" target="_blank">📅 22:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68285">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Q6eTV6vBVZ65nuW4JxmipLtvqJIaAcx0ik-23K5igdhWPjdXj476i3MAv4FT8RpuehhQcBcheKicjyerou3A8tWUD5hx52vMAmvm-TYvoFG8IBYpELbIbg4VpC8l_3w_WonQfUGhI04w_s604jLGbcAuOcFo4pEOEQ34woJnzA6OYg1TrXNXpZ6MA9LegipMwnVtP9hRrWabulX9MK0rN2jYO7f2XIRkrh3qyeA9fCejCVyAmIOw9UeTkCnWLAnMjlYwI0J34SCQueS55gXTRiBon_OatQpDd60CHdlklH1KhesPkvKp_sptrwWsU4ACisZJ-idBTGG2Cx0XhyN2Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=Q6eTV6vBVZ65nuW4JxmipLtvqJIaAcx0ik-23K5igdhWPjdXj476i3MAv4FT8RpuehhQcBcheKicjyerou3A8tWUD5hx52vMAmvm-TYvoFG8IBYpELbIbg4VpC8l_3w_WonQfUGhI04w_s604jLGbcAuOcFo4pEOEQ34woJnzA6OYg1TrXNXpZ6MA9LegipMwnVtP9hRrWabulX9MK0rN2jYO7f2XIRkrh3qyeA9fCejCVyAmIOw9UeTkCnWLAnMjlYwI0J34SCQueS55gXTRiBon_OatQpDd60CHdlklH1KhesPkvKp_sptrwWsU4ACisZJ-idBTGG2Cx0XhyN2Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68285" target="_blank">📅 22:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68284">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68284" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68283">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAJz2HklLjER3Ym9-sOnJyL-UdmnCZqP8h1z7BWgEPr-BAxmDn5kFYgNQmRy5FYDkFisy21wRqfs_fSgfdKEHfdz6WqwHv9rU2-niZ9qcPTqcecUsnST7ZZ2ASyLohbl7yUmbn8WxcIYLivW4l0U_z1n9zLaLCUjK6UbHFQXoyvHVvU9KBJpnxYy5LdrOrRWg0_9iGdxvuQ4gWM3P89dOxN8LIS1jRB511-BPx-Hhixzu58iKacYckHkvx_FL0TkB3S4SP3sAOix5iFh4wDVIKNRA5RjbXeJyH4l1AZn4zS4qk6l6djukMOAk4c0rTVKAtl8JGpkeA4ziGYih0ssoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
اگه آنلاین‌شاپ‌ داری این خبر مخصوص خودته!
اگر فروشگاهت تو تلگرام، اینستاگرام یا بقیه‌ی شبکه‌های اجتماعی فعاله، حالا می‌تونی بدون نیاز به سایت درگاه پرداخت اسنپ‌پی را فعال کنی.
✨
امکان خرید ۴ قسطه برای مشتریات
✅
فعال‌سازی در کمتر از یک هفته
✅
افزایش اعتماد مشتری به پرداخت
✅
بدون نگرانی از فیش‌های واریزی نامعتبر
🔥
همین حالا ثبت‌نام کن ‌و درگاه پرداخت اسنپ‌پی رو به فروشگاهت اضافه کن:
👇🏻
https://l.snpy.ir/i1ekm</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/68283" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68282">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=IYIdx4BQsgsCVUwzJVqVEBB3BFPXsi_qqyEvQa8XUQtzzAXsQaRfRVqpsk_oDwviOVQuEhgf7kxmxRLnR6TKCDNbQRG_-VHSLZzeiXcfbdO9DqmNRX0ICvGwyNcOJPJMXBlNxTRzN-0vV-DLq2MV0E7Z4pXv0olkZWyOX6XpVwIkrbtBqMuSzPWzA3lFxdOC_bZWHVfb1WcannWL4L9HQCNUPJNloUyq9wney99L2CK784dKvcMMXybYpMNlYErxEsyY8uxDw-AM-8TSjcd0igXyRV-CAkNXaKA0qQ2bCpAAnP3VFDoF29SNpH6EOQ98cXp3aVXJs42hiMfJBp5KeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c56cad1a2.mp4?token=IYIdx4BQsgsCVUwzJVqVEBB3BFPXsi_qqyEvQa8XUQtzzAXsQaRfRVqpsk_oDwviOVQuEhgf7kxmxRLnR6TKCDNbQRG_-VHSLZzeiXcfbdO9DqmNRX0ICvGwyNcOJPJMXBlNxTRzN-0vV-DLq2MV0E7Z4pXv0olkZWyOX6XpVwIkrbtBqMuSzPWzA3lFxdOC_bZWHVfb1WcannWL4L9HQCNUPJNloUyq9wney99L2CK784dKvcMMXybYpMNlYErxEsyY8uxDw-AM-8TSjcd0igXyRV-CAkNXaKA0qQ2bCpAAnP3VFDoF29SNpH6EOQ98cXp3aVXJs42hiMfJBp5KeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ستون دود در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/68282" target="_blank">📅 22:09 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68281">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLEK9vCHqK4ShsmcbaK1peKUfFJYMpsEaUe4rqia3lRQAs7w5sqVSLS-OisL4_H7CMnRGZZy1WOg53KcdO3GU36L1AJ99LeoEtY7wc_0lYkRiWf9YPB69rLIZe1pZswUQeqES1ZN1DK28qJCqumSa2-DCeAlzdVZzkf1-sKtGKYYOvHjoj4si_G1V5PP9XVZ5XeSCY5DFBuQcsV_1rVU8S9qmlUTEaPOfG2Pa4fCf2JCgAqK-q0S71dGG2nRha4QKzVnJiBpp2gh-W6wx9kmf-Tx87fxbudZFQwQHu-tr4ziv6xnuY58TpSY16x05a-HXoouGNPqkhD1238BhodS7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۲ بعدازظهر به وقت شرقی، نیروهای آمریکایی برای پنجمین شب پیاپی موج جدیدی از حملات را علیه ایران آغاز کردند تا توانمندی‌های نظامی ایران را بیش از پیش تضعیف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68281" target="_blank">📅 22:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68280">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🇺🇸
رسما دور جدیدی از حملات آمریکا به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68280" target="_blank">📅 22:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68279">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68279" target="_blank">📅 22:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68278">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
پنج انفجار در بندرعباس گزارش شده
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68278" target="_blank">📅 21:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68277">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
گزارش های اولیه از انفجار شدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68277" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68276">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=TBOdmdm6EaGkYKFmACjixlUo3QdQK587k4MXxMccfjpDFnZLaDQ9c372yJeHbeSwh4bxKswV_wznilL2JfJFlYo0r4OzvzAqDEgYEpj81KqQJFTOD7L100rOXT4oES9PtCsNxXgeTQ_NmrZF5DkaEaZzKP4ZtwGT1kjb-eOHvzXVECQylR6mH19mzrBlWbt5eKdmqLj08B8fSl8_INfxSDGA6ME9dkormYAAPVhvmw9U4x4uBvxpd-gc8TrbODYyiqmt8CthIhKHfizVtF7NdfOwpBBjnjlNYIUvATtWpHQYbVT695QM-gh6XfL2r078718lHxFVzZI2_UmJ9y2ftQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4cdbbb0c4.mp4?token=TBOdmdm6EaGkYKFmACjixlUo3QdQK587k4MXxMccfjpDFnZLaDQ9c372yJeHbeSwh4bxKswV_wznilL2JfJFlYo0r4OzvzAqDEgYEpj81KqQJFTOD7L100rOXT4oES9PtCsNxXgeTQ_NmrZF5DkaEaZzKP4ZtwGT1kjb-eOHvzXVECQylR6mH19mzrBlWbt5eKdmqLj08B8fSl8_INfxSDGA6ME9dkormYAAPVhvmw9U4x4uBvxpd-gc8TrbODYyiqmt8CthIhKHfizVtF7NdfOwpBBjnjlNYIUvATtWpHQYbVT695QM-gh6XfL2r078718lHxFVzZI2_UmJ9y2ftQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت سخنگوی سفید کاخ سفید:
«ایران همچنان به شدت با ایالات متحده آمریکا در حال گفتگو است و ابراز می‌کند که خواهان توافق با ماست، زیرا آنها از سوی نیروی نظامی ایالات متحده ضربات ویرانگری را متحمل می‌شوند.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68276" target="_blank">📅 21:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68275">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=k6eMS_EX45Zo5GrzKrDHbWs6E20BLc5RMewAZEMuO3oaFXfTP9PMmT307ovlcsLAnQ-2rNk9NKCeY_RhBBSwYHCfyqS1nYmu1y0rFMILlGo7JiKujCgF7W0f3aQFPoKdKCsXQesSfD_CbDfOZgoPeUhRuOO1RBVd16sakRXjtS-hOZ07BOs4npNI99mEnf3kEtbN-xkHvQUzUzzfI9bKjiq_G2YSjW5szBl_dThOi3ShaWfit6Vcr1ybDFfGTea1LiSUwWI0J2QtRePketPHsXekmgUeyr18q-Q4-m9yP-wws15UEd2w39RRhVy5yWc_zjKVchfQSEGCBG7qK5RdjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8bf2cd6a1.mp4?token=k6eMS_EX45Zo5GrzKrDHbWs6E20BLc5RMewAZEMuO3oaFXfTP9PMmT307ovlcsLAnQ-2rNk9NKCeY_RhBBSwYHCfyqS1nYmu1y0rFMILlGo7JiKujCgF7W0f3aQFPoKdKCsXQesSfD_CbDfOZgoPeUhRuOO1RBVd16sakRXjtS-hOZ07BOs4npNI99mEnf3kEtbN-xkHvQUzUzzfI9bKjiq_G2YSjW5szBl_dThOi3ShaWfit6Vcr1ybDFfGTea1LiSUwWI0J2QtRePketPHsXekmgUeyr18q-Q4-m9yP-wws15UEd2w39RRhVy5yWc_zjKVchfQSEGCBG7qK5RdjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز ظهر تو خیابون ولیعصر تهران،یه اتوبوس تندرو بی‌آر‌تی بدون راننده و مسافر به دلایل نامعلومی شروع به حرکت میکنه!
این اتوبوس میوفته تو مسیر سرپایینی و با ۶ موتور سیکلت و ۲ ماشین سواری برخورد میکنه که نهایتا ۶ نفر مصدوم میشن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68275" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68274">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DiJcvylKi3IoYaX5hZ9o5Xva-_3dLTrHnr0fM90J8adTOmxjV7TonIN2FrkCwIKOL7W7A44N7YmMsZ6HFoH6zPtk9q2K9oOiXbcv8zcDjVmHx96_1EsY3PRtrXt2uOXDRRhEa8XDq_bCgEtb_WmrsMahW8iuG4wedMjDx9Q-qbMPffCWeiLLW1oFD_cuH5K_vAL68sAwYHN_iaAX3GOjLQWs2bKlBADA4iOtZRwLMnNjXheaUDlS1mzxIVMiJN7dPx24rxBXtiAZH6_wr9QtqIkiqmyoW0AQT5bQa0UPzyke-v_iyumzVfxcsj-cH2PC477CgeaKmdSWfKc6jsHiWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کپی ترید خودکار
— فارکس و کریپتو
⚡
اجرای آنی
— بدون تاخیر، بدون دردسر
💎
رفرال
— با دعوت دوستان درآمد جداگانه داری
💻
پشتیبانی ۲۴/۷
— همیشه در دسترس
🎞
آموزش شارژ حساب</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68274" target="_blank">📅 21:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68273">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDeOdHjaAdVbwNSnAMENRSTKrquqwyByUu7CxL3wPz4wvCRink6NpAsskK9_PQIEGZEHtOZEXpgw2bjhUWm0fXJHB1LRbIJzcFIC0QnXYkh8UQRDoV2Zo1lCSvA0nqptsMx1zPt6ULTnaMyuamcxEilA5uy3aX45P8z6ZCpv3vqfr1Tgxkj24qxM9TPVDtuSljc2PsL_Vlqi3NIrDw6munw-o-CYZLLWZbS39HWOCnE7I3ck_f9GwhJ6j-7uYKVoB7BF44QZDTlPdwHTAK5GxKmgqjZZnMO9nosWnt09FoA1fsm7HJcHym1xtp9khErxisEciuFBpsls_cI8S7463g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‏شاهزاده رضا پهلوی:
در حالی که جنگ‌افروزان جمهوری اسلامی در تهران و پناهگاه‌های امن خود پنهان شده‌اند، سربازان وظیفه و نیروهای جوان را در پادگان‌هایی بی‌دفاع رها کرده‌اند، بی‌آنکه حتی توان حفاظت از این نیروها را داشته باشند. این رژیم بار دیگر نشان داده است که میان جان فرزندان ایران و بقای خود، همواره بقای خود را انتخاب می‌کند.
جمهوری اسلامی این جنگ را بر ملت ایران تحمیل کرده است و مسئولیت جان همه قربانیان آن، از جمله‌ سربازان در پادگان بمپور، بر عهده همین حکومت است. آرزوی همه ما، صلح، امنیت و آرامش برای تمامی ایرانیان است، اما تا زمانی که این رژیم بر سر کار باشد، نه امنیتی پایدار ممکن است و نه صلحی واقعی.
این رژیم تبهکار بیش از آنکه دل‌نگران امنیت مردم ایران باشد، نگران حفظ حزب‌الله لبنان و دیگر نیروهای نیابتی خود در منطقه است. برای این رژیم، بقای بازوهای تروریستی‌اش از امنیت و جان مردم اهواز، زاهدان، بندرعباس، بوشهر، چابهار و سراسر ایران مهم‌تر است.
خطاب من به سربازان، افسران و همه نیروهای میهن‌دوست است. جان خود را برای بقای جمهوری اسلامی به خطر نیندازید. سوگند شما به ایران است، نه به رژیمی که در لحظه خطر، سرکردگانش می‌گریزند و شما را بی‌پناه رها می‌کنند.
من با خانواده‌های داغدار سربازان وظیفه که در حملات اخیر به مراکز نظامی جمهوری اسلامی جان باختند، عمیقأ هم‌دردی می‌‌کنم، و از خانواده‌های همه سربازان وظیفه می‌خواهم تا آنجا که در توان دارند، اجازه ندهند فرزندانشان در این شرایط خطرناک به خدمت سربازی اعزام شوند. هیچ پدر و مادری نباید فرزند خود را به پادگان‌هایی بفرستد که امروز به جای محل خدمت، به میدان مرگ تبدیل شده‌اند.
این جوانان، فرزندان این سرزمین هستند، نه سپر انسانی جمهوری اسلامی. آنها نباید بهای بقای حکومتی درمانده را با جان خود بپردازند.
هم‌چنین از مردم شریف ایرانشهر و زاهدان که برای اهدای خون و یاری رساندن به سربازان مجروح پادگان بمپور شتافتند، صمیمانه سپاسگزارم. این همبستگی ملی یادآور این حقیقت است که مردم ایران، حتی در سخت‌ترین روزها، فرزندان خود را تنها نمی‌گذارند.
ایران به فرزندانش زنده نیاز دارد، برای ساختن آینده‌ای آزاد، آباد و سربلند
.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68273" target="_blank">📅 20:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68272">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
فارس:
حوالی ساعت های ۱۹ و ۱۹:۲۰ نقاطی در  بندر عباس مورد اصابت پرتابه‌های دشمن قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68272" target="_blank">📅 20:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68270">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=bCacCA5P6IZSTdGVnSG0JHKkl6To_svzKiLl_SaM_Dufm3ZMZc6iL_gHEvJQemqKLu3MEsgSaTci4NGkyztrqlPAKmKxTKxps3j_JJP0tRLBRuLkSiF5s_NmsplJcBtaI0XdAmOLCKOHCr8PvCKlDX0zA0VDa5VVe5gKpY5L6_yfdLIp8s9YKrqC7JvXx3TcC4RAT9sQ83LJC0LDwBPlmDnmT4lmRjSzex8LlA3fmW8Las_C-Gaz1Wg-vTZfoecjTwhqun3GUF-WrMbzYL_Z4oHETV257PYRD1waCVheezQBcDn4IImcgGA4ANC3xgBuvS272I5YzNSR-Yc6HJ8kig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ad056e14.mp4?token=bCacCA5P6IZSTdGVnSG0JHKkl6To_svzKiLl_SaM_Dufm3ZMZc6iL_gHEvJQemqKLu3MEsgSaTci4NGkyztrqlPAKmKxTKxps3j_JJP0tRLBRuLkSiF5s_NmsplJcBtaI0XdAmOLCKOHCr8PvCKlDX0zA0VDa5VVe5gKpY5L6_yfdLIp8s9YKrqC7JvXx3TcC4RAT9sQ83LJC0LDwBPlmDnmT4lmRjSzex8LlA3fmW8Las_C-Gaz1Wg-vTZfoecjTwhqun3GUF-WrMbzYL_Z4oHETV257PYRD1waCVheezQBcDn4IImcgGA4ANC3xgBuvS272I5YzNSR-Yc6HJ8kig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در بهبهان استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68270" target="_blank">📅 19:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68269">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=IlSvd6xDAHM3T0DGEi3N_ZbI5fCclAdC3IBIRDvyvM_RU_nfnIWK50vPagyz3T87oQTnrQcNebI5J3Eu0zEZfCsONy6CR3mThTxrKa30hHDw1seUj8es05ehZWZrInkbL-K94Ag9AA2mPimZKhCeDuXtl4LPyxZ57C7ke9e8vXMxrHLHDyd4snqRxZ7ZBFKUq3tDd_3UHftpFrcgiUm8T9f4X721iUrfhF8aj6p4nycA-dK-x3ymy_j2UTXEZeLBUGiJgTh3gK3j4B53qKncHGNggDF2r5FyJDTZ6aGz5GD2Dk_7jbWxO_qxXsoiJ56A4YoE_Yo5EJscDl38foCm2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32ebc1ab26.mp4?token=IlSvd6xDAHM3T0DGEi3N_ZbI5fCclAdC3IBIRDvyvM_RU_nfnIWK50vPagyz3T87oQTnrQcNebI5J3Eu0zEZfCsONy6CR3mThTxrKa30hHDw1seUj8es05ehZWZrInkbL-K94Ag9AA2mPimZKhCeDuXtl4LPyxZ57C7ke9e8vXMxrHLHDyd4snqRxZ7ZBFKUq3tDd_3UHftpFrcgiUm8T9f4X721iUrfhF8aj6p4nycA-dK-x3ymy_j2UTXEZeLBUGiJgTh3gK3j4B53qKncHGNggDF2r5FyJDTZ6aGz5GD2Dk_7jbWxO_qxXsoiJ56A4YoE_Yo5EJscDl38foCm2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محسن رضایی: مسیری که در ذهن آقامجتبی هست، بهتر از مسیری بود که شورای عالی امنیت‌ ملی رفت.
مجری: چه مسیری بود؟
محسن رضایی: نمی‌دونم، نمیتونم ذهن خونی کنم
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68269" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68268">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhS9eg1_GAGDNguBO8ZYqraduKGYgAdk0A-o6c83as6CWkBATd00_H-Awv4saz55OPG2QN8oBHHQU1lMyqRiXLaJ2zBHaMuBoZSxzQxBqjk6y7CyactXfidLNrKMjw2FfdPA0WitDxdG6iv4kWuLAiAYqYfWAmGL0stjvPdAtP0isD3g2UOGXy-MtGdBakL-rVOCqW8ZwiTJonQ1yPmKyDcrH_bUd6zdK6RltQhVWQbGcuWfw7jOek-nVxn7vUKJQkx8GLUtG727J9J3-c578NW8hkN6YPO_6QS59qZT-jijazmPYNie8GyhViM4YkKuaJmFSUs5GwLpugm_9l7cVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سازگار با تمام اپراتور‌ها
✅
لینک ساب اختصاصی
✅
مناسب برای گیم
💵
20 گیگ — 120 تومان
💵
30 گیگ — 150 تومان
💵
نامحدود — 200 تومان
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn
چنل رضایت مشتری‌ها
⬇️
@kavianivpn</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68268" target="_blank">📅 19:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68267">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETQ_nPH9NKMJ9tbdtdkloXBEtMGjbjU-vZNbcAGUhrose_nJ6VNC2OQuba-tQr7nyqgGuaMXFpLS00tyUIa16jbYvS6f9aupSXNBRWlZt7Ems8dAAv06oL_KJlvOO1WrDEULkNMBvlQpkQu_RBoGJsJEaPOij3XNor-6_TJwZFC7oVVQHz09ZnMxpjWflOO7DvZgaVJ46DG3neSmW5XWhBpRBHRZlSsKa_K8417WWxkMffCAgDF078aUfPsyj8LmBt7nlVgQB-xf18kI6qdKfKrpt6c-IOmMWIU1VDIDh9B_xt3eaJl9IMpZ9NOG7IiKDcSerK5P1yJZ8SIYm-PeEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی به آرایش ناوگان آمریکا در محاصره دریایی ایران؛ هر چهار ناو لینکلن، بوش، باکسر و تریپولی در منطقه حضور دارند
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68267" target="_blank">📅 19:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68266">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06389032d8.mp4?token=JSsOL-UatgdliK_b95Nw5KuNIKuCZ1g15m18knJh2hI3D45fD99tFMkVhRIdVcvYLliESB9E8uJIYh2uxRPeygJk3fmaCyKTL4GTqLtWn1V1_BzI2_YFWWItCZj8JIcpHdQzd8vnsDmRByz1zjUgGfEBzSIXDbVjwFpyWUOvyhveJnFNQ3fTqA-kIe2h15vVT6rLrYVdiodOTnXZkhc8LFFNRfm5HWO0tHVDNfFMyfaFcGDNZYfzosYbK53tk--iLYlkSgK3qGKSa_a7l4QbbPdR5dNEqKTbx4yIs5NGMGPKnEHsfKWMmlkAzuur04DV0crZPqiZOvZZ3zImAdUd0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06389032d8.mp4?token=JSsOL-UatgdliK_b95Nw5KuNIKuCZ1g15m18knJh2hI3D45fD99tFMkVhRIdVcvYLliESB9E8uJIYh2uxRPeygJk3fmaCyKTL4GTqLtWn1V1_BzI2_YFWWItCZj8JIcpHdQzd8vnsDmRByz1zjUgGfEBzSIXDbVjwFpyWUOvyhveJnFNQ3fTqA-kIe2h15vVT6rLrYVdiodOTnXZkhc8LFFNRfm5HWO0tHVDNfFMyfaFcGDNZYfzosYbK53tk--iLYlkSgK3qGKSa_a7l4QbbPdR5dNEqKTbx4yIs5NGMGPKnEHsfKWMmlkAzuur04DV0crZPqiZOvZZ3zImAdUd0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جی‌دی ونس، درباره ایران:
اگر مردم ایران بخواهند قیام کنند و حکومتشان را تغییر دهند، این تصمیم با خودشان است.
اما ما قرار نیست ۱۵۰ هزار نیروی زمینی برای تغییر رژیم اعزام کنیم، مگر اینکه خودِ مردمِ حاضر در میدان بخواهند به چنین نتیجه‌ای برسند.
البته ما در هر صورت قصد اعزام نیرو نداریم، اما پیشنهادِ اعزام نیرو عملاً به این معناست که ارتش آمریکا باید این کار را برای مردم ایران انجام دهد.
ما دیگر دنبال چنین کارهایی نیستیم؛ واقعاً نیستیم
.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68266" target="_blank">📅 18:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68265">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4Tnt5siX6XmljWnwiCF5ZMXFrP2oNoi0Dmj7oZiEmJnzp-W1owkUlumIQy6TBSBjHxz31Hh6JDdRwYxx-WEYrjZkz35H6td-43lHdHFfZfsRjvpRmjHPzqaQhzkYlnZ2WLmlSBpynUenYDfUDD44uaG4iR5Ny6wswsOB10QPSR3_bLZdMmIytmdKZrTXFuTfUPANqKgsstjOqR6xz9BnjN0lCWqsiQHbRMTg8w4gOdWLHwjvJiUNe3GB9bLFoOKWAr3BvJ0HbZpx4iCMOD10naI8426Zgwm9AbrN45shli6RE2HcRLFCH-e5g0BzfDLjouWo_8CeEUYumCEHEIXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
لاشه پهپاد انتحاری آمریکایی FLM-136 LUCAS در نزدیکی بندرعباس
پهپاد LUCAS در واقع همتای آمریکایی پهپاد ایرانی «شاهد-۱۳۶» و یک پهپاد تهاجمی یک‌طرفه (انتحاری) و کم‌هزینه است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68265" target="_blank">📅 17:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68263">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=mTr9c3sixR75I7FlQdH4hibKyA1O_PqnXiF_HwrAgnZTLzc3iMCkdJCk9uK4aEg9w_uxc262FuqjV5ObzN_uiaUlQsI9Db8YQvPQFaWoF3t0JNIHWpXPw7ci8UyeOy7eWqLv9gMiXGAMJP77t8krV-Se6Bfj0lIODLas02f8fz3ZHQXn5l5KEH81B0zGhSPfJZBb4BULso7No4iBPBAt55IIJzmPA9XIGDsGLWAktOpVOK_ewzjRKRRR6wOWFyZbAGOgtxqxbXmQ51_r1ss45NFlCsU_ogQPYmiRm47eVrRHrx1qWs_LJCMBVFtSBe0IoDpEN0f2Chz-L-hDpnRElQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55dfc7018b.mp4?token=mTr9c3sixR75I7FlQdH4hibKyA1O_PqnXiF_HwrAgnZTLzc3iMCkdJCk9uK4aEg9w_uxc262FuqjV5ObzN_uiaUlQsI9Db8YQvPQFaWoF3t0JNIHWpXPw7ci8UyeOy7eWqLv9gMiXGAMJP77t8krV-Se6Bfj0lIODLas02f8fz3ZHQXn5l5KEH81B0zGhSPfJZBb4BULso7No4iBPBAt55IIJzmPA9XIGDsGLWAktOpVOK_ewzjRKRRR6wOWFyZbAGOgtxqxbXmQ51_r1ss45NFlCsU_ogQPYmiRm47eVrRHrx1qWs_LJCMBVFtSBe0IoDpEN0f2Chz-L-hDpnRElQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عموپورنگ هم اینطوری بصورت دردناک برای مادرش گریه کرد:
من دیگه مامان ندارم...
دیگه در باز کنم کی بگه چی اوردی برام؟
💔
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68263" target="_blank">📅 17:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68262">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=Ce65-t49sAzHQVr37abDlENVvJJfW1HR0V82Kt-YgWlGfk6CTCXFpLkBVmI5WuYoWTRwwUVsdlwjOr9atnye2OAGBCKhu-F_OlGfxldXrylusGl6p_DkuUgp6Bfc7ApFwdt58vHBUcOJpFawKcSYr0BTLrZlcb_MqPhx5EG_D0liVMX8ScKXB9YzCs84VhfJ3SykRiKUCTDIq31GTPpZfONODrkTQSsK45A1WuoMEq4yOcAjK4gFwm4bUmixj7LGGSf8kUW-3J_1zN6FT_WHPqPOMilcD5_aE2GBHG5lNxCIDv4QZFkPeks8jZh9jNFph5RGWVleRwOkr70Fu4qg7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c15a1c1db.mp4?token=Ce65-t49sAzHQVr37abDlENVvJJfW1HR0V82Kt-YgWlGfk6CTCXFpLkBVmI5WuYoWTRwwUVsdlwjOr9atnye2OAGBCKhu-F_OlGfxldXrylusGl6p_DkuUgp6Bfc7ApFwdt58vHBUcOJpFawKcSYr0BTLrZlcb_MqPhx5EG_D0liVMX8ScKXB9YzCs84VhfJ3SykRiKUCTDIq31GTPpZfONODrkTQSsK45A1WuoMEq4yOcAjK4gFwm4bUmixj7LGGSf8kUW-3J_1zN6FT_WHPqPOMilcD5_aE2GBHG5lNxCIDv4QZFkPeks8jZh9jNFph5RGWVleRwOkr70Fu4qg7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام:
هواپیماهای جنگنده F-35A متعلق به نیروی هوایی ایالات متحده در حال سوخت‌گیری توسط هواپیمای تانکر KC-135 هستند، در حالی که در حال انجام گشت‌های هوایی بر فراز خاورمیانه می‌باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68262" target="_blank">📅 16:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68261">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOvqkwmlU-BK8yQPBPuoL-YftEJZNtGu1VbWNBy0TX23eserzwv1eJgpdmpH5xRpniC8ZBWA2CYtSsahNWXBAIIObztAo715M0ZRT3QxDVCwgCneJzjP_IlZc0S28GkR5XgnZ1aJYMhvp5p9V1kQL0jBfqj60EwvtuzsFVhYIMrVyX8aZqXdK6dw73G6YAx92nTVvSK61Nxb5v6jzjjRK4W7PcbTXZwGt2rrja9ZzSjcipyWyTq6KrPllcMCa5MqTXSDgTinw1hgdCtlMqN0HaaCcnHBgmWdQRj5zdE7CnMxGPSqAb40vlSP8tuxNw77pJ90a99RXm6L-5je0aKK7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو سال ۱۲۸۷، محمدعلی شاه قاجار مجلس رو بخاطر مخالفتش با ایدئولوژیِ مشروطیت با کمکِ روس‌های حرومی، به توپ بست، و بعد از اون
دوره‌ی دیکتاتوری و استبداد سنگینی
تو ایران شکل گرفت و
آزادی‌خواهان کشته می‌شدند
یک‌سال بعد با اینکه ستارخان تو محاصره شدید بود ولی جبهه هایی شکل گرفت و شمالی‌ها از گیلان و بختیاری‌ها از جنوب به سمت تهران لشکر کشی کردند، و بعد از به‌هم پیوستنشون، سه روز درگیری خیابونی شکل گرفت و در نهایت، روز ۲۵ تیر ۱۲۸۸ محمدعلی شاه به سفارت روسیه فرار کرد و تهران فتح شد
خلاصه که مردم حتی بعد از
یک سرکوب و کشتار سنگین
باز هم ناامید نشدند
و پس از اتحاد اقوام ایرانی
، در
نهایت به خواسته‌شون رسیدند
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68261" target="_blank">📅 16:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68260">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دیشب تو اوج حملات، ترامپ از جمهوری اسلامی بابت آزادکردن یک شهروند آمریکایی که تو سال ۲۰۲۴ بازداشت شده بود، تشکر کرد
خلاصه اگه امشب حمله‌ای نشد یا شدت حملات کم بود دلیلش رو بدونید
#hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68260" target="_blank">📅 16:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68259">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjxoAXEVRTth_OiHx_ak_cNwkDqh-Berrs0y5Vr_85PiEDKOHXWzyrj5u8U9VRhQsYgUqXvyCQuoKwAq_C1LxhVMewWVAvYeu3EXjKsKKb2Ms8trYPSAPC9ikhNKCAlg37eJYFEnM3LvfdRzNtSjN_yE-iHnDI62-XSjSmy6TzFUH6kmnsNJPA3dMqNNELJo8ECVx23d6rNyw5fVG2yullu9TfFLaZzaD9uFh8Q6ddK3Qa2vbyCRF0cvjCIUn3g6ZAnXtwSz1TzHULiHkKNyhVeRpCAHwmjkHkEE7L0HBqk-AXm1ia3zrUEiiwhqh1KeeYS_7ibnvaaGRHktTDeujA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوارنگاره جدید میدان ولیعصر تهران که نوشته «who is D nexT one»و هشتگ لیندسی گراهام هم زیرش قرار داره.
همچنین ‌حروفDT- اول نام دونالد ترامپ رو برجسته نوشتن!
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68259" target="_blank">📅 15:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68258">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">💢
مرد پاکستانی ، عاشق محمدرضاشاه
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68258" target="_blank">📅 15:32 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68257">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KrMEyB67gXX-jJpCHmOZh-O9q-DIP3pn0lOBW3UkDq5A7DLhI-kERNgsNI5AfBwfZVtVKC3cFljQDMQ441I67h7VqTIvR0NeCQx-yDoAeXvqa1g2iG3lLIHwXCIrSecN4R-Tpp72iObl0514LRG9tlU3MbipY0GS_lJui3Y8xjeUWkrEurR8FJPQrHv3ETdOwrMF17Sk5SSWwDXQs5M6cQxtEsi89xS_y3VGb-9WFSxoL_2tiCKteqpoLwa8EPYIJZZEOvBXR_UFZyEC3MAEf54t5ohySzBzpp-_lU5yNKML5haOZTa8GploBazr2IzInAxBIoU43VhkJB1-l31FqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نتانیاهو سفر برنامه‌ریزی‌شده خود به ایالات متحده را به تعویق انداخت؛ این تصمیم پس از آن اتخاذ شد که مراسم خاکسپاری سناتور سابق، لیندزی گراهام، به زمانی دیگر در اواخر ماه جاری موکول گردید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68257" target="_blank">📅 15:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68256">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=jkChujYRcymmfkTe8TEZne_10tI_gQO9w53cEmkOODeg2XXB19dJzSsaakp7LVzr3LIL4Q3vKOfveVP4a6lw3SO93or9ppCzcTkSQY8Kds8ARGUaZzMehzujsLqSdwwkM1buGgj7qrwkz6_thAK4FddBP0DeVffDKYUDxnF28fiB1WtqCbxBS1NDBWTzAA_9bYa77DWYNIIwuUYLVvDx4AS_j65SEUz0T5yrrOnCW-paoXpuS-rPFTdZhzsqiUp3-7_c25RmD719D4r0bVIN73UEl5ydhWiA1qoYeLIp7DctV1_wJv66PdZEC-1wp_4XQnXfKLH48qIu3yxSafCojQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b50f05a056.mp4?token=jkChujYRcymmfkTe8TEZne_10tI_gQO9w53cEmkOODeg2XXB19dJzSsaakp7LVzr3LIL4Q3vKOfveVP4a6lw3SO93or9ppCzcTkSQY8Kds8ARGUaZzMehzujsLqSdwwkM1buGgj7qrwkz6_thAK4FddBP0DeVffDKYUDxnF28fiB1WtqCbxBS1NDBWTzAA_9bYa77DWYNIIwuUYLVvDx4AS_j65SEUz0T5yrrOnCW-paoXpuS-rPFTdZhzsqiUp3-7_c25RmD719D4r0bVIN73UEl5ydhWiA1qoYeLIp7DctV1_wJv66PdZEC-1wp_4XQnXfKLH48qIu3yxSafCojQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مجری‌ها وقتی یارو میگه تشییع خامنه‌ای ۴۰ میلیون نفر حضور داشتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68256" target="_blank">📅 14:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68255">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utvBXffaVuh_nnMgTMXYilX8JVRwVpeHFz2pILRYIgCTnYv-c1oXmTOJb3Saz1DsAho4xc0tpLTZRyrJDYpknubf5BOeE-ipMJsXiMykzUcKmeAYKANIar0Zutym1seOd2iN_-uUhSMh_EhhoTeLcYaSvPTF9vH9pXsosMBlixKwdgzqVcPlbN4rzXu4Fv4pVrTNGOeYxBC_zHXX90xRdj79LvrP6tzguyA26Y9dzvYqGEwx4Tcn9UVsqbHPmXLrPP79B2qyYwRZnwzwpyfBhD9QOEzfeJWLdHhukQmEZYcFKwdK-R0jO7xocmSHiHcRA-H3Vay-0dMINYQ4LsAe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فینال جام جهانی 28 تیر (یکشنبه) ساعت ده و نیم شبه؛
- یازدهمی‌ها فرداش عربی نهایی دارن
- دوازدهمی‌ها هم دو روز بعدش عربی نهایی دارن
بهترین راه اینه که فینال رو با گزارش عربی نگاه کنید
دیگه عذاب وجدان نمی‌گیرید
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68255" target="_blank">📅 13:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68254">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8r-uk8CYeB7K_QgsGFYHsZMz1dUkLFhlqHtc3iedM8Gamc-ZQ8n5si7Cc9bRnuazYxiwrP7jm6J_8e2RAy3HUfAUGNj3zSXdyngbpxsIGZjtrpdlt3J5-s_CDYpo6fyTPODVty8Ybs_Dyy0-Cnli7jIhRExfsIVNDHD47PY33D3ZA47ogHvI1Kv7W8WhF-Tal8WcAfiZDFVFEuUrzBFV_PWwOf6Si60_ml4Cg5kQblTWgbBkymd5QyJ5e2F2SXEL-Xlda6n7rip-0jPDAVXEgMZo-H9iK3XE5vXU2a1cCl7wi7Yui3PJ4uMjJWbROZ57qHCsyk2YDb4RFTkDFZPHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
تسنیم:  کارگاه قیرسازی حرم آتیش گرفته!  @News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/68254" target="_blank">📅 13:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68253">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=qudt9kBNUnI8kxhH7tQXUm1noOxE6mZFy8NOiK5GnfMOUjEwMjkKv4OUx0ymCtcIH83m_m82kClmluYEDI8M_6x1XN-4mlEgOItQXZ7sTB2EJrnivzWExk-cslnunwYlUGiSGltjJdfMpNrJfStJRV-D2T1OnWbpNc9Ow3X6gGZdRvDTRvM_SWlnPTIzvyvBdhAYj--N0gO_rDJLYq9mCg97RrfAYEigv1riPMrIZvAY4U7olMWgK6O3njCzcOMDVHN5XPCwog-Az_eTuoA92Vvr-orQAOUpkpU_zzw668rlMTz_J9R2EFdMd78WbdL76Cg058wPEDuZH8NkAQUMJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34bb460b32.mp4?token=qudt9kBNUnI8kxhH7tQXUm1noOxE6mZFy8NOiK5GnfMOUjEwMjkKv4OUx0ymCtcIH83m_m82kClmluYEDI8M_6x1XN-4mlEgOItQXZ7sTB2EJrnivzWExk-cslnunwYlUGiSGltjJdfMpNrJfStJRV-D2T1OnWbpNc9Ow3X6gGZdRvDTRvM_SWlnPTIzvyvBdhAYj--N0gO_rDJLYq9mCg97RrfAYEigv1riPMrIZvAY4U7olMWgK6O3njCzcOMDVHN5XPCwog-Az_eTuoA92Vvr-orQAOUpkpU_zzw668rlMTz_J9R2EFdMd78WbdL76Cg058wPEDuZH8NkAQUMJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تسنیم:
کارگاه قیرسازی حرم آتیش گرفته!
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68253" target="_blank">📅 12:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68252">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ1LtIkLZLVsvz8bN3LMuMsv5wqDgZoVGjwTDTwhEHP5wpDgeZdjzIh839mEcuYlkQe5Fo9KbAKQIWB3QFD1T-VKV6faBTLpgmepvEPOU2vbt08rSKwUC-cRHXO0XS1WraajNSn9WU70gtu6QObtkAVNsVSrOkD7Fp6DuV8s4vZLnRxJpXVYcx1pfo4lYN485T9t5lTgyuXMg-OXkLzUbKiANVb9avUWTSdjaL3LYZZJ0o6y4gzVgtLLDJq3RlTu3kNOjzbThcx8T6TX4lPiOb44TbMy6tJjIGBmkNSfJLQmrKzhHu6OsODf-Y4_tsmJ_6M1vCt9v65wcY48sRoYFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتش‌سوزی در حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/68252" target="_blank">📅 12:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68251">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/314324694e.mp4?token=aWqqFkLUvTNweGI9NZwZuhraq-L1WwpDRam8cgwOvR0OlR0Odn4dF705b8QOVgGocK9WLQc661rcFQiEq75FgEGOgu7wf4te9cFrG6MP_QTWOH2d9wsX_aESwZRA2p9mNUf6xUUQBw8tzEs5fYl7cinSb6xB51D1dy3T0zZEnwg9XBelSaNdrcbX9W3L-ODsoVUOkkErbfHfACb0tD_pwo9_C4akehSnG1jm53FcRarKEqo28bwGyeUKrmorCK89ey4iMsqvQ5MPfy_eypW4MkBY_d_R3JA4D__bqjyQugF5DLK7OcXPlxniDNHbUYs_old-emfEjjDnkba19m2H4YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/314324694e.mp4?token=aWqqFkLUvTNweGI9NZwZuhraq-L1WwpDRam8cgwOvR0OlR0Odn4dF705b8QOVgGocK9WLQc661rcFQiEq75FgEGOgu7wf4te9cFrG6MP_QTWOH2d9wsX_aESwZRA2p9mNUf6xUUQBw8tzEs5fYl7cinSb6xB51D1dy3T0zZEnwg9XBelSaNdrcbX9W3L-ODsoVUOkkErbfHfACb0tD_pwo9_C4akehSnG1jm53FcRarKEqo28bwGyeUKrmorCK89ey4iMsqvQ5MPfy_eypW4MkBY_d_R3JA4D__bqjyQugF5DLK7OcXPlxniDNHbUYs_old-emfEjjDnkba19m2H4YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام تصاویری از حملات به ایران منتشر کرده است.
این تصاویر شامل برخاستن جنگنده‌های «اف/ای-۱۸ئی سوپر هورنت» نیروی دریایی ایالات متحده از ناو هواپیمابر کلاس نیمیتز «یو‌اس‌اس آبراهام لینکلن» و شلیک موشک‌های کروز «بی‌جی‌ام-۱۰۹ تاماهاوک» از ناوشکن‌های موشک‌انداز کلاس «آرلی برک» است.
اهداف مورد حمله شامل پرتابگرهای متحرک موشک (TEL)، سایت‌های پرتاب پهپاد، هواپیماهایی که پیش‌تر قطعاتشان جدا و از رده خارج شده بودند، و یک دکل مخابراتی بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/68251" target="_blank">📅 12:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68250">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1popxvNOL0NbCYPQoiG7sEmNOnZVrMjDnxBpuv2jAQwz-H8hlFCYzqm0x7ffwF8ps7Uj1PqgL28l5YLC2I_g4nQ6laXtyJ28T4fU2Fa-8n0LRgDRiUyS6ouTnL_MnBMsOyvuWRVfpEUix7WLlxLm54REiWIxvt9Hh8IHYDITOa8_oUqfTGYTHfWasN-lRpOeA_aGjGDYVirTkWqNFAw6A6LI0c1wrFaPSDz-n7Be-e-9pkg6Hh_uOH4wUUUe0vxd2g5rGskw31KGi99BufXdYQiB4np_DczpkBcsOIOedg54XJGZObOQROaTy_2jiEAK4sMzus-4BrW82CeQGtBGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ترامپ:
ایران اجازه داده یک شهروند آمریکایی که در دسامبر ۲۰۲۴ و در دوران ریاست‌جمهوری جو بایدن بازداشت شده بود، از کشور خارج شود.
این زن اکنون در سلامت کامل و شرایطی مناسب خارج از ایران قرار دارد. آمریکا از این اقدام مبتنی بر حسن نیت ایران قدردانی می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68250" target="_blank">📅 11:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68249">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=DMkjtOz-g2OZ3Vb8R_eKcxEa9u6XjYrCSUF2IjU9aDk1Qix66dtZw0Nh-yyfWu4C8ImaT4eQ5ovUJl_0U3yjLpn4jqVNdeSUPK6R_u0oiWpsxVhnU_OhI3wlgrmPNR6A8WRRtVGrq6CcQC3DL8T1VRLjD5CYbsZxJLZ6Y-b-740TAgTjEKJa7-daSpVlr1Ul8brC6kgR0bwDcZ0Iudx5k4VPJ5phHcT_AAWZV3tcGiKryFBGS0btD5YB2As8krtjfroMF1OO41jZNVtY7oTcHxTkfZ2aqDkNQ-9OKDqcv5Nb2L_U50BjIyCmi6lo8YGHfdYxlyEEjSuG1He5HfPGbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bc13721f.mp4?token=DMkjtOz-g2OZ3Vb8R_eKcxEa9u6XjYrCSUF2IjU9aDk1Qix66dtZw0Nh-yyfWu4C8ImaT4eQ5ovUJl_0U3yjLpn4jqVNdeSUPK6R_u0oiWpsxVhnU_OhI3wlgrmPNR6A8WRRtVGrq6CcQC3DL8T1VRLjD5CYbsZxJLZ6Y-b-740TAgTjEKJa7-daSpVlr1Ul8brC6kgR0bwDcZ0Iudx5k4VPJ5phHcT_AAWZV3tcGiKryFBGS0btD5YB2As8krtjfroMF1OO41jZNVtY7oTcHxTkfZ2aqDkNQ-9OKDqcv5Nb2L_U50BjIyCmi6lo8YGHfdYxlyEEjSuG1He5HfPGbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پهباد شاهد در حال رفتن به سمت پایگاه های آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/68249" target="_blank">📅 11:10 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68248">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTlZvfb65LzrvQavflE0_OCY5C_RWpovffYlTCWUBrhPDKncdII0Bn7JLt5VVywrnb3Levrw4RMltmWkW9a9zh37zb6evtg7DRy-xMJeDzJSqyJlcDSc9LSy_fwpDYW4GMXJShyJAKrNuRQTV-jsE6mJLK7uQloOg7p_racMRwkGVnMpXHyXq0LPpilmlO4MLzfembo6ad9deSDdUZaPes8GSJRUx4RTF3RT4PImbWxBd1yxWjHpR9AVrWQAuSTao5TaQHUddjCvCl56Ku7lGaMoObuPXGeDFRAJWnuZ4FQLg1syRP5ASWcxsVfUgRYnanvjT1n2goBkzjiC8P1IRias" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8221101a.mp4?token=KhZo0yPoMkhOG_Ho8mdM0d6iQJETmJwVTjKYq7FGF5u3pq4Yp6Pz7FhKrvR6NyK2tcepNWmkcSviW3vYHqB9zqAP6QaAhAzVx7k-JWVCN2wKE_8PDCfxFMwKFquwWEynRRz4-cLUzLUk2Cms9AcJ9Umsc-ox0OHjEeJmVGC1XY2wKVPImUhY7sGAQSuE7hz4u2ssBYHr2FDhifLmknuJeAGZXsBJoCxpSNB4xFz3e1QLmbP_7YSnHElb8ijy9DC0SEQuPSETOziImIaRhOP6TbmIe1X_qUHX23vCXOEfwr_sDka0htY3RlqSB7MZfu_B9e53_8weSekap2KmuUXDTlZvfb65LzrvQavflE0_OCY5C_RWpovffYlTCWUBrhPDKncdII0Bn7JLt5VVywrnb3Levrw4RMltmWkW9a9zh37zb6evtg7DRy-xMJeDzJSqyJlcDSc9LSy_fwpDYW4GMXJShyJAKrNuRQTV-jsE6mJLK7uQloOg7p_racMRwkGVnMpXHyXq0LPpilmlO4MLzfembo6ad9deSDdUZaPes8GSJRUx4RTF3RT4PImbWxBd1yxWjHpR9AVrWQAuSTao5TaQHUddjCvCl56Ku7lGaMoObuPXGeDFRAJWnuZ4FQLg1syRP5ASWcxsVfUgRYnanvjT1n2goBkzjiC8P1IRias" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو وایرال شده از یک جوون طرفدار حکومت:
من الان شرایط ازدواج ندارم چون نه خونه دارم نه ماشین
بدیهی ترین چیز برای ازدواج اینه حداقل ماشین و خونه داشته باشی اما خب من ندارم و پدرمم پول نداره که بخره
دلیل وضعیت الان بخوام کوتاه توضیح بدم ؛ سخنان حضرت اقا یک طرف ، وضعیتی که مسئولین درست کردن یک طرف
الان ما باید تا30 سالگی بدوویم تا بتونیم یک زندگی متوسط درست کنیم
الان یک میلیارد طوریه ک ما شما با هفت الی هشت سال کار هم نمیتونی بهش برسی و انقدر هم پول کمیه که شما باهاش نمیتونی یک واحد اپارتمان بخری
با این اوضاع 50 شبه کف خیابونم و هیچ ربطی بهم ندارن.
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68248" target="_blank">📅 10:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68247">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⏺
صحبت های روح‌الله زم درباره حلقه نارمک و جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/68247" target="_blank">📅 10:01 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68246">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejrxJpAHWu5N88-377iwEF0xqQUzlwlElLfil7IcO4u9Z_vzSENJ46Y7b_BThibxgk1TCSy4PKI3S_2r-Tm0x-ksS0nvLcFt-Sp9-ic6oA1Cj7G7ls-xprleyZFuWWtfa4NUfl5NoFO93YcezsBx7H6RYLDVbl8fF5pTmjsIdDWX2jTV4aNvi3HBxJWhARKlhnMtbUQ8_X-4L7vInYA-O29ykAR7sPKKTA9qssnco-JKp9OKCJZ-mHAmQ9VjXHtZ8sU4ruFY8qbWwyh1LH3AyzZBpJ_d5s2H-MRMo-bj6aBl1H9sQPg3NJJilIEKGFKgzWStf-3vrH0I2LQUgWZ7WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سی‌ان‌ان به نقل از دو منبع آگاه:
دونالد ترامپ، رییس‌جمهوری آمریکا، در حال بررسی گزینه‌های گسترش عملیات نظامی علیه جمهوری اسلامی است. به گفته این منابع، در نشست سه‌شنبه اتاق وضعیت کاخ سفید، راه‌های تشدید فشار بر حکومت ایران برای کاهش کنترل آن بر تنگه هرمز بررسی شد.
بر اساس این گزارش، ترامپ احتمال عملیات برای تصرف جزیره خارک، مهم‌ترین پایانه صادرات نفت ایران، و حمله به تاسیسات زیرزمینی کوه «پیک‌اکس» که گفته می‌شود با برنامه هسته‌ای جمهوری اسلامی مرتبط است را بررسی می‌کند. با این حال، او گفته است ممکن است عملیات زمینی برای تصرف جزیره خارک را کشور دیگری انجام دهد.
سی‌ان‌ان همچنین گزارش داد جی‌دی ونس، معاون رییس‌جمهوری آمریکا، در گفت‌وگویی تاکید کرده است که جنگ تنها با ابزار نظامی به نتیجه نمی‌رسد و در کنار فشار نظامی، گفت‌وگو برای حل بحران نیز ضروری است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/68246" target="_blank">📅 09:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68245">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/68245" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68244">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pHQ9hI97FVfA4qTZMnjfjq6NQxwAI5mBpb_IYx6FkbKJ4tRAG4CkkgcPEeS5lo-WTFGbAAVxc9fRkhiz2Q0d1k0e4IuVWOikJ97a79N6CfzEDYSYAKfM8AV0YowWYJbUV21A7-EUWPqg67mhzxzLMW4W5DFYDr8fzyToYtU3u_HDQWx7rfe1RuA-9IOT-wFbF-sOJ6sVQuvHgG8bpYp7XptqQBkSjki4eR9lRFyjv-pHWhmv4narHBBzb-D40gks7rPg5lFanU_pGZvZrFKONEv6QODfiDS4Tur4nQzCuKdFp3TuWooZN_Pj0bO4pB1IIPDDKk4hDgdGv5W5dYC3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68244" target="_blank">📅 03:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68243">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=bICn6Lc3h56LiccNFhIEHv0phyZMW3AljMWpAdvkvoUPz6xRuBtHxyZDR5Ef7UYmzSj-9RROmUtbHuaMuFI5E1s5wXDdhGvB0GyKeR495Uo6I5YDyGrgc8OwxfYJYiCoiZC3tQpsPPWsXiC4aoGaZPIxKdJLQ_gxHZ1bkJllVsP3vJcyvitMa109HQCDRAyR2A9m3plyc5O1fZr2kK83givg9UOx2e5ITUk6Z_iG4DfsMo-xMvBfBQ5y10Dys0KZbMjXVsF6jiQUEjMeZ9q1AeeVwf1HlxmXselxRx-hQEq0GU7GgH41kxm6sHik6PAUf2Ix_9ut_a4XHxAVvYVLyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4873db94b.mp4?token=bICn6Lc3h56LiccNFhIEHv0phyZMW3AljMWpAdvkvoUPz6xRuBtHxyZDR5Ef7UYmzSj-9RROmUtbHuaMuFI5E1s5wXDdhGvB0GyKeR495Uo6I5YDyGrgc8OwxfYJYiCoiZC3tQpsPPWsXiC4aoGaZPIxKdJLQ_gxHZ1bkJllVsP3vJcyvitMa109HQCDRAyR2A9m3plyc5O1fZr2kK83givg9UOx2e5ITUk6Z_iG4DfsMo-xMvBfBQ5y10Dys0KZbMjXVsF6jiQUEjMeZ9q1AeeVwf1HlxmXselxRx-hQEq0GU7GgH41kxm6sHik6PAUf2Ix_9ut_a4XHxAVvYVLyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پرتاب‌های متعدد موشک‌های پدافندی پاتریوت به سمت پهپادهای ایرانی:
@News_Hut</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/news_hut/68243" target="_blank">📅 02:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68242">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=fW06qzk5QnAsPjVggcYZfwr40aAWYtz4S3ez_BuKaTCcQ8zSmAYBam3WSmczYiOr6_OmooYHMk9hsyD2MCbVtdejfmgworWKvV-krcj2i9B3TfM9H2bDj6pDzWt9LKZl18p4XDl5tT9UkkxEILjeoIcpE3kF9nQvBDWPP1-3vIf-O-ssp9FrQH1syNSnsnFQLRQMsTUEHdkefjD_i-Z_W2eLKGgfOaTAbS21s3VW0xMiSmeNC0J_3cQpmgiMOiW1DCGs9vePOj5cHKGMCqvORtb94sFdbEMm5CE8KJKnlW0d1gh56kjHlHXnOPoW_DNSpuE9raWBUei4xfb_oiGi6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1519c2ac09.mp4?token=fW06qzk5QnAsPjVggcYZfwr40aAWYtz4S3ez_BuKaTCcQ8zSmAYBam3WSmczYiOr6_OmooYHMk9hsyD2MCbVtdejfmgworWKvV-krcj2i9B3TfM9H2bDj6pDzWt9LKZl18p4XDl5tT9UkkxEILjeoIcpE3kF9nQvBDWPP1-3vIf-O-ssp9FrQH1syNSnsnFQLRQMsTUEHdkefjD_i-Z_W2eLKGgfOaTAbS21s3VW0xMiSmeNC0J_3cQpmgiMOiW1DCGs9vePOj5cHKGMCqvORtb94sFdbEMm5CE8KJKnlW0d1gh56kjHlHXnOPoW_DNSpuE9raWBUei4xfb_oiGi6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن پدافند بحرین در پی حمله موشکی و پهبادی سپاه پاسداران
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/68242" target="_blank">📅 02:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68241">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmJDCtoKKUoOWAmc5uZBQd57Yvx1JEMg_jUfnIiHxGCyNHJD4lwXEv0NWT5lMrPMyd_4spTS8FfnER7BFW2hMyEralELDAs_O0ffA3cjenblNmIf7OK-egwbNTfRZeP7oLtcdW37gB5U8mtx-Q2_OkYy6lKcaubFoXKcdSoNuF-q_onUGQFs9OXtqhvcqmyyLYFFlJA4bD9UL2CAFRHJjPJhB37MNOm12eYlvuyQ8gV9pUbGW7_0v_AzTa-dEJ8Xs_nbq41qo3PvHx4Je_qleXgBBX9pW5GJeCpn0Z3mmyVY-njrM5-PRWzrM-Xt66jV6B3h4MealdF_zDzM7XtbRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/68241" target="_blank">📅 01:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68240">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68240" target="_blank">📅 01:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68239">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=cZ70ANkyaH8kCeEcu7jvqT28UrMd7OWSMPpLerxG4-ArxyBY_GSD5UqZhoteVXpKz9zcaGt7dWdM04zvxiLbDdIsqrTz4NfwnTPF9b7d_hUd7qd-lltoXAAJbKs43UcLlw-Wr8AY4z985CSqwXzvB2sK2us0XK99PC_l64T2hV8yonLDE55U4WWaUvczR-mJBGGKN95bsFL5YEbXko-vmb1GmfX7kIm0xkx0nvv1aFQJ4FihQoZbyzsiQ4aBG0Km1Ece96AzCJoWIkTv_PgurEXTzs1odSxshpsGFlTHFNUAEHlIHcfxeBezfmpCLCk3pEs5GnD8ZH3i19Faat-JNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cd7e59689.mp4?token=cZ70ANkyaH8kCeEcu7jvqT28UrMd7OWSMPpLerxG4-ArxyBY_GSD5UqZhoteVXpKz9zcaGt7dWdM04zvxiLbDdIsqrTz4NfwnTPF9b7d_hUd7qd-lltoXAAJbKs43UcLlw-Wr8AY4z985CSqwXzvB2sK2us0XK99PC_l64T2hV8yonLDE55U4WWaUvczR-mJBGGKN95bsFL5YEbXko-vmb1GmfX7kIm0xkx0nvv1aFQJ4FihQoZbyzsiQ4aBG0Km1Ece96AzCJoWIkTv_PgurEXTzs1odSxshpsGFlTHFNUAEHlIHcfxeBezfmpCLCk3pEs5GnD8ZH3i19Faat-JNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
سنتکام تصاویری از اصابت چندین موشک هلفایر به موتورخانه نفتکش M/T Belma که در خلیج فارس در حال حرکت به سمت جزیره خارگ بود را منتشر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68239" target="_blank">📅 01:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68238">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
بندرعباس بوووم
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/68238" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68237">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrKq1yLULAaek8vXzuHa-9kY2t4eq-lNjCkUNxJFVZHE88a2FfWqtNcZ7G1tBYbJMMggvDk8hoNUUddzeMg0PxLZzy-FBd9waj8NdWMj3AKjKeZ-RRmCS6QvjxxyAjIenWxbabcnyG_x94ALtp4jWNQQU9rSNsErIvN3VysZOQeGomtdCNcoZoJzCYvRFkGyOTLTcnMMuPst0I2ZiUrQ4jaQDSHzqjOtXrsxjBPCPXtyPE-ixOSBf6Trt2XaQCVE9B9chDWMUruBW8nI71efit4jTot5drA2F7hc9wes6YFRrXoP-_WJgyUxWZLB_liaZt35aZKZ6hyCe2aQn3xK5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌  @News_Hut</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/news_hut/68237" target="_blank">📅 01:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68236">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68236" target="_blank">📅 00:56 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68235">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OgdhNXiGYtKsqTG7_kamm58RGjPLBnIPCuxHDCvPl653YC1gzopVipu4wEp5ovRBeCCc_87quzFl9EWePHGzcTEzhPcZG1xSHXa6vCZD2CKrNJRlfDnscihhNiHqQSQfDKoghM2gQVfTzguuo3mYAmn1yjTdLDY154vdtLoero_7MR4Pv6iIPjuBxvLqZC4mVU84vzdegvAg_oKXQGiE_98Ic_s_jinvvKtxrqedcInuZWZhEIPVV9clK4IfqSTwE9IPb-fYkOVhCvOew3HUVtg172Cd3vCcqiWfCnRujqzY0n17yXlixhrzEPeZpzYBjxSgHzZH9UOpgJsOP-1-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی| امشب روح فوتبال ارضا شد
🇦🇷
آرژانتین
😀
😃
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68235" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68234">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">من خودم رئالیم ولی برای مسی باید ایستاده دست زد
😑
#hjAly‌</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/68234" target="_blank">📅 00:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68233">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=vfUB71ULVa9F46ARwmzyOPWrXVQrc-225AYeNwdU6KvymdoILeeD9jGz7Fq8Dn6BaKwugk0CULsrvKuo9y_p8iR1ZgPGd-iqadar5zpu3r6Gin30tOHCM7kpxgFHzTL7ZHEEMEOsL3DT6RWVwoVgkQFWPBJ8XhiJGMM6BCd4ox27ewE-OcIXLKn4azTGsFdvTMSwXU-rvSqO_ANP4SzqngV_lE2ClGFGlfX10chvB_eEmnKk28xtn2ql14NrEcXoz4jwcm75_cQPpu4M4iXDxp90ak8HX9xEPc7Pl3OtBGW2prZKMIsIbdCWmzlVkMD4yFUysPrHC1p6B0YAiQsuFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d327baf32e.mp4?token=vfUB71ULVa9F46ARwmzyOPWrXVQrc-225AYeNwdU6KvymdoILeeD9jGz7Fq8Dn6BaKwugk0CULsrvKuo9y_p8iR1ZgPGd-iqadar5zpu3r6Gin30tOHCM7kpxgFHzTL7ZHEEMEOsL3DT6RWVwoVgkQFWPBJ8XhiJGMM6BCd4ox27ewE-OcIXLKn4azTGsFdvTMSwXU-rvSqO_ANP4SzqngV_lE2ClGFGlfX10chvB_eEmnKk28xtn2ql14NrEcXoz4jwcm75_cQPpu4M4iXDxp90ak8HX9xEPc7Pl3OtBGW2prZKMIsIbdCWmzlVkMD4yFUysPrHC1p6B0YAiQsuFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#hjAly‌</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/68233" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
