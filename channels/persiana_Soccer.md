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
<img src="https://cdn4.telesco.pe/file/UmLc1GfMjcWwOnQSCLQa3ob9e2yTwFetjC_h4JjTe0SiNpQjsMgDtXe0r7X8QsnrvqO5u2Mn2QFzt4ZIPxwBmB6wLu9YkrUDk1NuDdYOo_lx3pL2sSECjKTcCYdS2bz8fLrhFzlg2wb6DXc4_Rv4Zokkur8yYSab1KwvkPq7oz348quyy5bl-bQMPXdJlkqbfKpSC8rrhB7P-qcPBN7E3pnTk0VDNSMiLNebmjd9Ga4aQ7GMc8MOS8U1BFfihdkm5UcRM4dbgmEl7PCkPfY_GShkI9VmdKpRyQvRVhu6uNMXPpnTbBbVdzwNuMTGNzF5dvK8pNwxVwsPtvmC9hHp4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 630K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 23:50:17</div>
<hr>

<div class="tg-post" id="msg-27073">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erNI72XVTHua2H7V1QXse6RjWMwv-EkSG7Hpxf1dPT1lbNKPURu902JhKOFwhvll4njT3uMyo_cJOK9gDMh2enDg2vf0g8VweZt_AzAPsswqaAolssu3CBAlPJq75wup8vqp7TnpkDRW1dHCoZiJ3hlNsLhediRCxfsU-wHSLmSgybrpmn37eqjC5Ymk-54l5eQrBTH5HluVc3DI98ehkQ3bJ98H1sgISv2S_rEDd3WJomei7JJFQgdQ_7zVq-ux6LQ18-coi2vCMAXxYabjEG2yt_1WL-0Q7_Oz7jE4DNHyyj8ZFpJVXUMdnvBHWh9FRNQZMET7bwgI2035vPAksg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/27073" target="_blank">📅 23:33 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27072">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzON-oau3bTMOZWbrU_dK-fjiQnx8yuz7quhNOASTS5_Gu-g5a6G0lLaYBVZaz9iHEoF4tN4CueP1tf-ElsbDZy0gvi-29V4IGADggasQwJPx1dzieGh4GRLE7suil4qe5gwztpeT_lmZ9ekFWpofOXyirOqdnDXm1xSGsghssy349_9B1g7QKbJRytR_v1FF61-UyxUeBUgyK2706CAu5z18cv9eB0KLEk7ipFvOzOFlhzvqWLBMDh8ahGx4e0HHYR0xr8wFAoHrk9ma3uevYvUY4yNpQrtq6j1tNUF0_fca4NVHBlatQYLnxAivGnU58OunAyqaYVvkkcCPuPK7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
اسکای‌اسپورت:الساندرو باستونی مدافع 27 ساله تیم ملی ایتالیا درخواست جدایی از اینترمیلان داده و به مدیریت افعی‌ها اعلام کرده با جدایی او و پیوستنش به رئال مادرید دراین‌پنجره موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/27072" target="_blank">📅 23:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27071">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoTAKx3t7eBtnAjm3w9tnES8cZn8YJX4bjp4xDTJ4LdyjEax_8F4-RtypufwS-WZd8jOIgk7PQ1ohx71f7iaC-MA-xhFSzO3bRDlmOA15CJHYKEpxr80Ccgk1cmEdlpi9dO0ErzGPlaX3szQA1bZlep6ytYy6RHkwo9mGgoCOsnJtqLQ1DhchGIlyYc1PTsr-UT9_pZnUAVJVYWBKxWvrOESbgsNTJCmWsC8Km8lAIbytRFTly9Nq49VJ0V5f-rgdgUjosKGk5dCQTS0dZSfKQ62LmWx-2cFKZPiDHBMCvulHrSfrkAtj33kB0w2_3wJSgjW0UIK_o6r130BW8rJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/27071" target="_blank">📅 22:20 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULOflGez0cLn6l479rYSdmkvxbILjq5hepalA7e2oyu-GZRN0fVsjAPOw6GTAVk-Zvz2qGK1Nm-zYooNuz8YtYPRHGRBbTcGI5-3NwMEU10C2eSmd3HQyZcpjUMZQ9MpQ0qJqRjQz7vDLbg5Gwf9SmIyw51gyi-MaCNvKoH3ZAHQUEohgdDl-pkyQkq2S4CEko6wLnKqgxAshwGyS-ughU_d5AgqtVBjknJUmxNKknoHha0YIHA3_M7bR7aXFEIXBAm-gQAXeWcfjPo0bnCFHdqxfBHPrSWoZMFjqvQSKs0A8VMpljysY9ddijadc66m3MyJ6h6UHgHeXCLDavVKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgkiSADV4r5i0-h_k2BeEdEYx_3G2U8i_rgSEMDBb46n_giqbVXpO9aolxivoKk9-kgpwZ1ZU8o0jMaMpa7tDuk3_Ni9UWPQErHhtQWmoLr-TCw4K7uQafO1bqh7WSSwrIVyxeo6BXL305v3BVNQZPTgElEL4ytZDpbjaEwPIpHjf_5GLr_6U_P9LEpuCOVgqmiEhdu9YmF20oS2qyHYy4tCzJWju38YjYt3SN43z_is32NiR7EYI4zqKsQCMfH3DjS6DYBy0c93QdotTp-ZlV8764xn8Z2b6NCYFUVjLoHKqyY_QlMTmAbAmFLjwTrGo4zKNsP5d1og_bndNRtgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=mOa7G0Mbw-ZGGGuR-QSd8sDC4VA8QNuIcPZnvYHFXMO6Eoz9I8jX_-DcLEKd3tbAXyt6vH6snJdvuzmAONLeALf-kaxm0JlO-6S-av2StkhsfeAbWbAa2ZQlZ03J-qHPIwI2JUyq7JIAUQf-P5IY-HTBB5Q-c97DWb_jwhjFEf_avPsE5bVIeNhr5eQ8XcoAQdudSZv0AQEgyKTgs6mAPfyKgOMmOIz31xeX615icsGpus6gi4F3aANz7Ud_Z64xuxU-ZrXgjW8GdfTlsu8WJx3cT3i-ZomsFx9WqT2y8u4OErQOOjq8B_2YZVk_VD0sXay1rZ6LwjSoua89lAjM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97c6b80b0.mp4?token=mOa7G0Mbw-ZGGGuR-QSd8sDC4VA8QNuIcPZnvYHFXMO6Eoz9I8jX_-DcLEKd3tbAXyt6vH6snJdvuzmAONLeALf-kaxm0JlO-6S-av2StkhsfeAbWbAa2ZQlZ03J-qHPIwI2JUyq7JIAUQf-P5IY-HTBB5Q-c97DWb_jwhjFEf_avPsE5bVIeNhr5eQ8XcoAQdudSZv0AQEgyKTgs6mAPfyKgOMmOIz31xeX615icsGpus6gi4F3aANz7Ud_Z64xuxU-ZrXgjW8GdfTlsu8WJx3cT3i-ZomsFx9WqT2y8u4OErQOOjq8B_2YZVk_VD0sXay1rZ6LwjSoua89lAjM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
فصل آینده تو بارسلونا میمونی؟ فران تورِس:
‏من‌قراردادی با بارسلونا دارم، اما در فوتبال نمیتوان پیش‌بینی‌کرد چه‌اتفاقی دقیقا خواهد افتاد. من هم فقط منتظر هستم تا تصمیم درستی بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=AzZefiMMcl5y-dT6H7rB5DybOdUeguHLEyrr69hydlwAUzKxC6UmS7_bmQulh__6HR24GO3KlR_Pubvm6WpmQ-m2HONZEHMK_3XazabgkuWYw3c4Vhh3MXO8gowTWzXVkXkK4fCkfkGe_3VVmrYbfRSVOsL2sppQrhUWAkCIn3L0eBPBP9U-ZQKW-rbV7NymLwJCNYvgdN3nRr6p8JjA_kKzl5ULpvNN8gmMtma_vmD441lTiArC3w_vKOvdhpbsF79KNQcd8u8YlNjFkKeNcqdx9ZC9GzPmTfgOKYB0sChRYcMnAYSxD7T5951GJRgHDB8qGOAjfBhCMmUAoek1sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d787366ec9.mp4?token=AzZefiMMcl5y-dT6H7rB5DybOdUeguHLEyrr69hydlwAUzKxC6UmS7_bmQulh__6HR24GO3KlR_Pubvm6WpmQ-m2HONZEHMK_3XazabgkuWYw3c4Vhh3MXO8gowTWzXVkXkK4fCkfkGe_3VVmrYbfRSVOsL2sppQrhUWAkCIn3L0eBPBP9U-ZQKW-rbV7NymLwJCNYvgdN3nRr6p8JjA_kKzl5ULpvNN8gmMtma_vmD441lTiArC3w_vKOvdhpbsF79KNQcd8u8YlNjFkKeNcqdx9ZC9GzPmTfgOKYB0sChRYcMnAYSxD7T5951GJRgHDB8qGOAjfBhCMmUAoek1sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
دلیل ازدواج کریستیانو مشخص‌شد! حتی قیچی‌ برگردون تماشایی به یووه هم‌به‌پای جورجینا نرسید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdjTfBxWekLRFgS_j_GgPnm5jEE4HkAW9smSQv5lQ38GhXgksMSk-PuGQQCvw443aUu8N7_-o67FO8t4ove3RHeK75_4SMW5nO5OBwNdvBl7s3jZ73crzTFzzKhvCu3NENOqrgE8iLyhJKNFRAzzgwP9IFpskN3w7KkErBwAlbpxbTy2OQDSxAXb1fOh8-ev_FKGv1kzpjgwtE5P6mw26iYRkGVGeP8bypNf2zKKyZCUBflxpdHATJqIgSQ1D7cCsnmAJHDiwuDy_l7vju9dJkMhwjldbDUDEaoirdP5o2cVi2Cdsb0hO5atIaFyDpGtSy4KY1uDLR-ezcWB5dYHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzqoBdFhR1nvTkz6FGlVy-XW06oQjACZCbomLqV-pLr6mRG5Qbfuqt6rYpbroH7JUMBssg1Oc3Gok9KIWi4gwEI-EjPG4nOGzEmjyEvf1BWmt2kfIUg25fvDrMEHt5rL13Iv3YPgFE2xg4AHDkY1jEFSqu72zAXHN5jDUiEw-Bz1mq6S7JoakwRtUTmHVO3liJZe_-EoYf7AJrP6zDI0dFE7TeCUdIskxdQQbnl7SziKLLlHj0hkvhUYKu6hOwbomWnXOWYxrNsxFeBn_YSUKaESFHdRXlQLnANFl5M6FT6OanSxriOjK0RYMBnJV3VXcn8JzaOLzK_W-PCqp07vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKxghC23ZObuItCvSCzs4vkoMocG8Spay0C0ZNAlvcLE5t8hsgheUg8va94i0AHOg24ImipSTIWIjJvV_b9FVSMXH7XjO_PUanXYR4qGzrlDhMMs9dM3f-xsfQR2FZZPVlttNXE1x0uNkRb7ucq0nJ-TZOpZVJeGBLp49mZmuHmtl4xWLVP7TWYFh-9CiSE0z9OdM5XNNh0ierYku54vrPdn8dzm7nmL4jSC-I_b36mGIqtcKs1v6gysnR3noo2uargzqWYqCFVcLKpmZ3B6H8XsgYUH6y6fmByTOeNbOCQjvMEm_yvyI_Ce5MKZ3JLlVwvNwwgfNaSzCMQ9S0bK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXuPCW4nEb-4NpaHEtvJBYdtZYKqs8pic79XyaAnyMjY4FcbOVW6Pzc_1vZXacCB0YhVLZor6DDfOiibJSRxnBBxnNPJ7bXSsJkcJoASAGD4at8Y88abP6zPG_KAKPl56GtKDg2X9HfUxARrk3Hh4spg4qm9keq-rj_YJXBG1YjBdzjzST29mr-wWS1CjETl67qj1vx1QeTqzv8dNOd97Vnibt0QeHX3cSczeugDbsEu0SHF7-OBK9ZYpn_yehXWiVPWMkhcenAukia8tsILFYC6kw3Xq_9q4vUewszoJvYIMNpI9k41VfoLzBSalueesxn6CMXspS98yjNoNX2Iyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=XwcROUPlinLrMhQqfWMQ0s-XQ9tbedO9BYvfKJcTKo1YOjNCMYO-jxHr5wbA_SYLsCIL7A93Q7uJWTaRPhopxAAQ21ZLffoQPEAJGM0DP_L4e9FFwbUJY5Um6flljrAp64MYJhp5_CihogVv-tS17Tf3PgS9vMWXlfcAII8WOf-CPV3zGqwZ9wI61EpbTpWwDHcUWnbekl3Ogcz71dZ8LXn0NHEa6696JA_EO5-JafiywEftEk1q0UCUmmshhmdhSRSNFjHzhWjrLWTqEZRb4hiOOjyUw6ywMGfEjaRZqiTsPVKlxIPr_W1eXAWNAX6oOgnaoVsa-XgmwW2398zTsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab970d5a0.mp4?token=XwcROUPlinLrMhQqfWMQ0s-XQ9tbedO9BYvfKJcTKo1YOjNCMYO-jxHr5wbA_SYLsCIL7A93Q7uJWTaRPhopxAAQ21ZLffoQPEAJGM0DP_L4e9FFwbUJY5Um6flljrAp64MYJhp5_CihogVv-tS17Tf3PgS9vMWXlfcAII8WOf-CPV3zGqwZ9wI61EpbTpWwDHcUWnbekl3Ogcz71dZ8LXn0NHEa6696JA_EO5-JafiywEftEk1q0UCUmmshhmdhSRSNFjHzhWjrLWTqEZRb4hiOOjyUw6ywMGfEjaRZqiTsPVKlxIPr_W1eXAWNAX6oOgnaoVsa-XgmwW2398zTsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو بازی‌بیلیارد تو اینستاگرام 224 میلیون ویو واقعی خورده بود که یه رکورد محسوب میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llYPRa680KfGxKTOGeUyUHSw7Mj2HQUCrsHzQNTSzfS9UEhx08iNoWbRzxHG6uuC1PUvNIYFO-T8r2c_8vxWR1x_pAdy-b9aQJ1YZbz7q1ahw2TL305DntkrJj8X7p_tzKm-GOIxzpTS-gICXqj6Onq87ALcGVj7uFOjBi7smgEb9SQGEqaI9QC0nZhETvvnkVucRzfDtK4BH4P4im7RuqJiiT8bJS3bsvLlWrYaD9vncb7wqP8V6uYwZhRaAAepxSyi8q5OJ5g_YMPLhYuC3QOi1eTCerToDyBLTRG1GCfGzF2NdLAeZ4jpjqgqTf_5Qjltfv4oUvhvjH1GQ11AYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8SZOmAKJ8reiHHB1Fnj_oFG94lK69nQ5-XHdIp3BnKquIVMkk_89LhFrKal-kIVBsgTyouBDwxMDRY_0STa53z9tlGvW9I8Wv5Icd9fCVraLHcYJibegT3UfG2KYbvNouDQkQNU5lk_Y8NrkJi6zU4ajvPOn6dy-KhfCjGxckwKtpt_QEP2SRR7SHWxDGWoRooXQyv3_-Kd-b_R8l0OGko8TtKlLUu_D0an-u1eGv7el14s31JyPr6oT_10cTT2fix3Xlr6PWhhjPKkcEvZwuo47VxUDrb4vGqyq_WuU9LXTjIhWlnMOj2APnPjCenMyV4wI1PASxCVXSyCWr3N-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpRzg9UuHqgChj74rFw0Wr-BO8nXO1tf9L-CCJjJfaDmv1mezDWerBmglSK7Pc5kDt3Utl0FkjOM_GX4EWCIPNmqUM0i-DSWdQ2O2wPeI1QSRrv-9tdfNcLcE0ERkZQb-W4Y4I72Mc_WMcUdfkUTJim_UojmvfLxOvAQtZBUUVANqIYqqojw4DQ807ccN8mLe5RfEURkoRyXaiIh5aDqi9cFLDaIsSBj2Tz2grMOqOmAO_nrZKszFANtzR-uYqGi-eKaDNBZELxpb6G2btesTyVCpC12TB4X7u6e6kQctdspuB0Jrs43qPGr06a4N-t6VvN8pYAMdi5dkN2vsozrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZ4KXjDj5Ta9lYTFMqxU2Z2i3Zoiehz8UTAU84p7g9MX0V-bfXFo1RC0iXyuVLDhqOUjHjDK8PEt0bzQbvU_Axe4SfLWCWjtu8PiXK25sQ3Bqjg8i8xYLBWR-B5cr2bfFCHlYIrt_p_1AA52thswSUUg9qsvFZp2yaFqsK8743i_iNrkBJOrz1D6d8DfX89ZWwKthoNK2O0E8alvx3_nt5wLoamKbzHVwJ2jTj54HMAQD_OuPDCLnUbTATye9u1R5L4xhtbLZ-3DTziaGBWQntyFQkU1OEPBD4EuccqebyM3b9IktMm3Dn01mjUmuiTPHU5WOpyUENATB3h5Ec2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL-EspvObJ7TgWr_5fZqz_3U30FLFzBSpMvsG1XMl8J8c8ndW5jMYZEUOzYeyastXSi3h8s_P_yKe1z06D539PZ2DspW-ySxP4_ldakLEQTpGkj473J3JRUxxlVujwfe1dto4NdtOkA1wuPTEEpsRM3KmuVgFY2cPBASCHu9wolDLahYRkqIJesP548NUvfxUx8r9tbxV0iS-I4hH3h5YnZ4EZtJ5htUTP41yASUDCaR0sLFFahfS2yOeeOXbV4apSMEgUI3nLw6WTTOmZm6auTK2RsTxx-fOa345WpdTetZZofOFEh5Ej_YhGzFmeYOakg5lEb1hiUx5HQoICXKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHHLNcpJAdnY1HyHidUF19JyoXvNe3Vy2tjxEr52OZfWc2JvCMhDLAIA1c3nyIUk3eudFi5SBsytXpB0I5kLbCuSCYsig6w6l4vuQfMKiVpMLD6iB-tun7vq0nuqk8ScLOT0ZpY7ZLJTw4apRn8-oR4hAGGij5Vmc1frS2gUpcd4hlMFtZktCRHMw3hlu6ga-KdyoTAMMxCJDH_OxVj8sNMk-PN-dafE5i9TZc6vMms6ndxW8zxC4tI9q0RPLb9Qxhf9FQYvQ9FLYZv4X2W3HPips5vZUelJVqZ1RmcjeBRIHFBBBPFHG94nlwSDalOnZK4wpmL-VaDpagR1W82b2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKg2UDVdGVF5vQRMhutRBGCFPdMBK0mhKIY6PXVp9rk-dD0sSQfx_MdUbzX8QYZ2s87omyDIDdkdXlbeQFTc2qMMEXEsdR741jg8YGqZDT2dVyKZJQWepi6fbW3VZLZk0eXsKwM7Ldw5F4bfyZglkqU4-cDQ7gguiN0IAtb7Hd4q3_xz-XtZ69tPvkLNqhjIz38xBGxFSBV7QFSWbasEuruMyrvpGHo1slqjcvSBy2JDoUuzLyJAidLxaNe_mAdqy8AzRMGWPICAXhcDJtXRWtsC4rlQLdngljzF8fIDRiJjChyyvkuGDJcNzhFnBCWjFhagox2CwUfWMN3csMQe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2279080601.mp4?token=t5PUSeCDmF0iYF9CT760_4YACJp8f6JTMfmdoCBBytOieVYnvpdPJzeBs-9RUPo9Zg2HO96t5jY3kdCTWrR41jDG3jVfAJ7XQ1pAiZ_LXxXVdmXM7DnhcvwysX08qApE0_LjfywSqp2IYnsMiTy4v2CMAcl2PdHoA_hhiD7twNtom4AXZR9x45lNNjmwTjLjHhn6nJiJxgdquAJtaS6g6MUjJH91mhgMvOXuMIYZk0FBjW1Ef2R9WBZSGHdavmMPTEPtVB1sNDXLQjPN-LYbmas1gmaDT94Zs5d989p7mXggQW-rbDMsSJDdYfR1qoQyBpI79JhUSwSEA2dW5oziKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2279080601.mp4?token=t5PUSeCDmF0iYF9CT760_4YACJp8f6JTMfmdoCBBytOieVYnvpdPJzeBs-9RUPo9Zg2HO96t5jY3kdCTWrR41jDG3jVfAJ7XQ1pAiZ_LXxXVdmXM7DnhcvwysX08qApE0_LjfywSqp2IYnsMiTy4v2CMAcl2PdHoA_hhiD7twNtom4AXZR9x45lNNjmwTjLjHhn6nJiJxgdquAJtaS6g6MUjJH91mhgMvOXuMIYZk0FBjW1Ef2R9WBZSGHdavmMPTEPtVB1sNDXLQjPN-LYbmas1gmaDT94Zs5d989p7mXggQW-rbDMsSJDdYfR1qoQyBpI79JhUSwSEA2dW5oziKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتقادحديث‌میرامینی‌ازشرایط‌سخت‌اقتصادی:
یه‌جوون‌چقدر باید کار کنه تا بتونه یه ماشین بخره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqjreoQOb16SkBrFmFPGc2SxKtkUVQO_ovP8ahDBgqntui4BiGqL2C3KYWaojls9LJkMRULY8rquNAAfQYkZzKPhzFAXAwXrQ5Mz_d2ngbs0W8JvObZ1Livq8ta4_kw0oq-20YDLqLiDx6BcD2w6qQKspX0Pxx7lc1dDUA1q5wF-npOJYbLgGJs3fx19ZyOPd-xf0hUjatPmsjub__gCcbutnkBT3Y8a9o378-HgD7RIbhwah_W_7pQbXRk0gxQdhOpSPaG4Eo6ysymIDAPumgfKrpwOlTaENRNU8f9vFVE5Mqefh_UQxMq80QTkbPMORZWia827BwyAUnhByDv12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idvg1-Z1zyyTKWOOEtZrU895NWbVAKmjnHsIWGTV3lmTdtM1IqKe9X8IuHDuD1Qw8KgO_TYfQy2eTOFTTgdHrDJvV0EXILzVZzm_8miwe6SDkl_4Vq73SbwKSl2mAdMG7VsDdt2FxuMQ9WaWJj6CK_HG6vK78Mq7GJy2lyboujunDd84DTKnNdyZcgNVzMfSFwMyhucCBmEr6PG076oP2UU9M7HWPlJlvyee-ah0PtN3hRfR0VIX3I4nIid-QzLV0CLc1k0yD2D44HQXqHIgXCcSwdF2vvCbDFlOjsUTEeCf6YtrKmHfYObHauCtzg_k9cRj754a1piBOFoZ0-eTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEfJtMeQ9exu3v3cTZvdplbvxWZg6udvmLsbPp2-Zt8XJIRDd-0hic3M_M_WxrfJE3xUefXvdoFeWVmOUhLzsvbUjykJlcbvFkNUCC4RyECvtvm7mjQYhMho-g6HtuY75KLnzAtccbnYI-5nNWkFbZE-_1nJHQeJxeOqrZ7zop39VWdFt8m1tEjyoprlpUYUd8PJDaLw1b-fUjT_ug0eTEgB3-xUCWyPlURyDSowMAcNOfs35r7U38Ysazrak_gbEYezDUPECdWpQiQ0ffvtlYNOACW-ARv31uvOcDePnvnPZkIhs5bFvZ5M6gGuSlq1cxNJqHQVLjNVm4AvFwbYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQOvin7quw4uH60SkxivND_6RdKd3_gOzhXcHN9aioeBU_jH2qvUyvZRC_SJZefI3ujUrqupiUyorVhGhYsz774NUGi5-EhGWobELC9ihGgtQOrR75ywdv1HhQv67eVAPknw0FkinRRqYebE5-z5VkfH5Y0NbMo4LfO7TE7-lAy7lHS2zSI-hNLa-wuwz6uyZPZb4GCB890SeQmhMttuOopaVMmIOwVAK4FMUt-86lDJFCaSy2w4cUSYBbAxnT4qIqKree5ETSap3t3-syQlWPmpIKcTfcNcn1XvI6j26JrpYsxrhTgVhPUuYpJ_PpvQq_rd5XS6Rkje0n1H-UGpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LaVLW0UyovC5p4rbhkd6i4IYcYhCYdeJ7TRLBaieMhmCOMKxnwXHyn3gGFok2J_YE_WVRibKZE4Xmx6giHkRrXW4MNceF_-XC3C5Gf141ST3tHy8iP4SwS8wEkUKlRXYa69Jy-3--FyDIFO4nxhxHuddlt0c0M0z-xVay_ireNBs9JlT2-lgU4g33ucH1KQan5jUXSlkPzyTF7ratVhC0b5syorYMVISnBw7p_4CrFdaKZj6bOIj6F4LHXqsd5pL-sBfl7nNNDXgiU9I1KH9XU4GVVdm4Xc9U9pGCKRZ-H9eatkk-a4XNTkZEYsXTcwyQ-mXxz7gfcsUZ3RWx1mglE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dac122529.mp4?token=V30TSmidXx0tBxH1tD9ONR5nOFrq4Os5bZjPFpVzHtJQmBUrkUDZ_utNDLBouY2H1yorMi5Ia3uelpNS8EVWtV-aH2lxd6ATo2ray8rNCRGn-4sjta7Fxy85x3leguxl-prEC6nkWzTDR4HKwpVQoy658tQuiVY1u6nk3eSAIJy2TkegUKW_qC4Jtl578XIhyAi8xxaLOm9rdIO1hqrkGqRcxu42f_2PhCcVQUcwsOG3w99IdVkp2u1DEh4w7FiPQaADW2aHvA7ttxVr8i1Up4QyxKtytghrOcmfL5BpniajEpvBTKzt-yRKERpwK_gOpzgSMk-0SaRY_wLPnOUK3LaVLW0UyovC5p4rbhkd6i4IYcYhCYdeJ7TRLBaieMhmCOMKxnwXHyn3gGFok2J_YE_WVRibKZE4Xmx6giHkRrXW4MNceF_-XC3C5Gf141ST3tHy8iP4SwS8wEkUKlRXYa69Jy-3--FyDIFO4nxhxHuddlt0c0M0z-xVay_ireNBs9JlT2-lgU4g33ucH1KQan5jUXSlkPzyTF7ratVhC0b5syorYMVISnBw7p_4CrFdaKZj6bOIj6F4LHXqsd5pL-sBfl7nNNDXgiU9I1KH9XU4GVVdm4Xc9U9pGCKRZ-H9eatkk-a4XNTkZEYsXTcwyQ-mXxz7gfcsUZ3RWx1mglE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇷
#تقویم؛ 9 سال پیش در چنین روزی؛ PSG نیمار را با مبلغ 222 میلیون یورو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t37qk-tqgP693Q7NV3kUjUoOEyhgbbzJmnqzu24jbixdCWf0WyJqIsHCSItySi2_rg04RBoC5qKFWGrh2yOqri3_PcOuSqBERTyyjnUZ1lu6QWhVO1ATpDdRoXAtT0sGcVsYBcS725v3F-Ngy03mkgCD6WCszqeanNffHlX-gD7r9NFlPQZFSOxOVPn2rI029Z6Yfi0mkT1VSfrmVsii0Ml0tCjOIor_jPCEPZlvxUyMQtz-dHMeWRMmpVaVNwjSaXvHyYFjndz5Oh_B9_npF36xLTyeUezk2JnUUnUsAxOYBLk8L6IlvxE_aX_oWRCPiZ29WmZd30qxs7vOK3Pqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msPOh1OPKa5UFfsnagmoXwYk2YVxEfSOwMZiChUAH29C8vVMdavSCbsKImF32lzzo7HQxI1dCnrLN2bvtFIJQfyxrcu_EKHJdzETHAzg2p5jL9blOm7Z6apppKrUfUjzKWoWEyYWaRkkIcpKZ2TaZC8FcCRmTR-s77c-IybKEbFpouk4o369MQKtGhL19oHNXs85RBgtGiHZLyq24S3r3uiCEZkIv4mBeq0LZuQx29ULRge_VCyyecyLiEmydoncHZkE5DMIs3s1jhHgg5JaCMvVbY7yIAsDMwS89Yqxe9MW97o2M3IL08YGpj1VM24lfu3UcdNZvIBAgro3cRlCng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27047" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ5s12losXlH-ETyj2GoEj64rTWD0sQ2FtkMu53IVrTNXsKaBPBnBtEbQ6Hev4kIEV5GuTADMcnHU8H2NfMOs_P1DQM0rt9GdKSyLf1EA-5IeOtWjvZ8lIMG2uFr8n2hpGJXNNwTg2gusmJF7pM3EVSyrrGOhpWHwKWMRRmBOsuwjPx0Doj8-lSZ4Fz_R4iRwZk6YSTnYlCEpdImrZ-BWYYPp9UZD8hWmWe0xrUaglBxLIYoJ0sxJW1m3wTcElU9hedplZo3FICBH4_zURxpYdqpsl-M7FQZjUF9oLgQuwOIAA6mye6jHKoFVSj5O3KuzSSJwOO1zmoex5TPVy0WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTi4ky-eEJN-FWprxBMatN7mijtirC4LBjo8mUZbQHnSMyWxFIGAyMjf5RFIojlp-e0mN_Pp2pIdKjTrWZyFXHwxVT9WpYamTXLTRdA8o7g2Y67-dnoBRL_VsFwPBLWbdcpIlNEbX9gcveNATHGndGcg8Mjde02whlMFL2S8CvDVUrKZaCuafWWYaYKvnQaZPPtnp22mrFaMK83iBtc8vIDb42cZX5gndKhWKfGLtHe_-rLkc2OKEm51MAAkUOePhK_QaMW1DvlrATX2CaUV51F4zZ-wzFH2PHjZB2whLXmNZVfzidYXyY5s3hIB0DHDqyQMBMwgiLsU9fY4f8xBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7821302722.mp4?token=EmAFyBx_4ElpgfiN8YatkpGYOwgDQC8ScNx5ebr0w47B8u_6NkoH34n33pb4mOxET8fxJIl_p6tG8IMdF45IvMwJd1WvvHCR3lB5x0r0JnqEmUO9uKaeK73DOgqTrCqN231wZfmUbn1OjtXMiQlnz-kFNwELQI9wGJjfb2MyVt50ZcG5y_5gQT0w6ng_FS9lv0qjy1mPnxgZYNZvc7Qs43AQEjnTWarX6IphDA6Qexjuv4NyA5VTXmULvqhVp4bk6DPQwuIH4MVXC9QnhAaE0Y4oJyyznKUAYMbCrQycGvlmyt9cWIqGH3wBidPazLB37PPwCz9J1A3UQbNnbMehaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7821302722.mp4?token=EmAFyBx_4ElpgfiN8YatkpGYOwgDQC8ScNx5ebr0w47B8u_6NkoH34n33pb4mOxET8fxJIl_p6tG8IMdF45IvMwJd1WvvHCR3lB5x0r0JnqEmUO9uKaeK73DOgqTrCqN231wZfmUbn1OjtXMiQlnz-kFNwELQI9wGJjfb2MyVt50ZcG5y_5gQT0w6ng_FS9lv0qjy1mPnxgZYNZvc7Qs43AQEjnTWarX6IphDA6Qexjuv4NyA5VTXmULvqhVp4bk6DPQwuIH4MVXC9QnhAaE0Y4oJyyznKUAYMbCrQycGvlmyt9cWIqGH3wBidPazLB37PPwCz9J1A3UQbNnbMehaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی‌خاطره‌انگیز از شوتای‌ فوق‌سنگین و برگ ریزون کریس‌رونالدو در دوران‌حضور در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-VH2baEseos4w0Q_nyLH33gaRPyocmxol6clW4ALGmnBOBWzlg5cFCVMwfOM7jzi_DSl2zLvG-tJZGx9agroI0im2XHdteYdSS8KAKOq2P98V5D0R_Y29xkTrN5UJFFSLsMRy-adoS5Yf67bpzdeFCCqHwjMjLGbQ9ooaWOKQpFPrF36-AF2AMd3URHTTWo3h2lDO_RsGALeU6Cgr2vdhhLQpqKxErsbeWLEPyb54Slno50jzn9ephB5iJL3gq96bOIiRJ2C3miX1zxSNtEJtnovPP8U7ko9ro4UECywEJQ_9leNCLFpP06ILiSiTyving9zi7hDvGAE4_TaDLU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQ5OBpHPx7pYSYauVAm7SyyqcrQR12S2FVk5UJdljRJf_FXb1HJ-eWYoFt0WYq8at7aHmbXIfRxEAeVRNnX3ApExP4DPeTME4a1wjTDDLMtX9UMvgUM32h91haDItmwx_TU6vdAaEaM1vdHzehCTQKXdOc8_DlzGpOQdJhi6KpR6NPnv8qqoSqUQ78fL5r3mz0V-sTL7B5KqeZp34q4fCeCeQTfW16zyAnwz6bLetL9lti61WwNmyBKgVJKQlBGLM1WDgC_d3_LrLZKzie4s8Fj5_VOpPJ7cdGatelnJ-VMrf2bMkFbeldbNK18dAs5UPAAymJN-BBGbS_zS4nJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahm5JMMp_dTaKJXmsYQKDa3V1NSPh5fMwRWKM8X0j24b7BITpoXbDwfW9Cjg8klCVv-OrbzZ2QFkRPQL6HY2u-k0AJusCaZcr0LXmkWeJmXRb3UzNyRAvqoxvc-nY0zJDJ4MNJvZ2NeMUrkEUsBmEGfSNXMTsul-XsHuvqvswXHV6vtfkXOjSx6y88s0ojkB_ktzKhI218bVhi6jZ4bFcwK3035afobNggWo-HKIyvamsxr_Mfan0u3rhAhJIp4uJ2ANql1Av7eVlNwYtT4zNRe5mqtj15XRa4gk6F_r17csQCZsJnH_A1u1gV9SOOaksA1Bem9uG4bYm4XYDFiFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWKlj2Q2SNYbehEmjcLUYnrHSgprVuOM1pt2IRf4FXPYFXjZLrIWfJgRAAEVuumICY5DEfo-IPQbsjR_nnj5WME0DR82N-lCdk8i2yjx4LKdzJMcyGFeVJNUP4cH4yyYb5RwLoa3IkqUTbnCtKaEJW3MrS4mshSfN1a-ivd06Un4BSlSTFVkJZHsNFmpc_1dwRB0821ApZCtBi4RBwm92PXyDaI6M9ZEAlLgBF9v0-Quoyk2ePItr5TPYKLysaJ116qPyVGh8qYKsKfx0RVKwZrPWxVpg7kAnDyL-NieIqJjKkjKnoRxeakHKPwVzVy_37XbjSnMR9QNFXCi4w4TLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-rNqPJcouuWsOqSu3e1kTCiWohimJkl7w-0gfnFMujmv76MM0DiSewLNNaGke8riyFSzGbKlotNlkMKZmJAENGvFVQJ1n9u86FNiH8wPrGDDvP-BLcBveNIGRAHoby7zuA6-eyh3PZ5x1-FvoRujEPruipAQXPpC0z71gDJ4MFE-dX7bB9TnR3nVPURkGGOxdPomZh9OhqKSPQTfelD0p_RbXgEatHyQyYpxJL-CW-uucHpzai7DjkAwVFurcUDKljw4tAG0zVOZXvWzj5rdbxEakzCWdYfZL0B51aZ8zHGQAjpEXZLPMb4J47aGnXH5o4tynconpXv9HbydB-lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5EGC-36J6cPMSMH7yz2DedDrR66rKHzDq_NIhRGQl3069m7S5m7N5oe8zhYyYIsh2WeOC6fxr2rTPIgb9eXOCyUz6NK08Ss1JSmJGGqvV2Pa7yJBYEK5SrCu-GgrPerXnCTuHAkahjVKqvTqA6ab4sw6nWeWAAb10GIoqGmeKigVbJVFTuhGWSu36uzQ1qRQT21cB6NcggLe-kr9bUqHzUhcEaJ-amYE4NKKUXhxlkNznNCBg7V4UkZbaN2oeHHfQh-IGR1WuMtPQBfNfQg4qfbhvVIPFRhJsckTTtcf1wxGoapYjCzblpUy4QBSii79PWDY3WtgZy_YU6MJtCTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFA6-I_HHcCFGVn-0kd_wF7_vF2E-YPA_HSp3eLBF1roahFI3Cc_F4oz_6AGf5iuHMRi6hi2073fxYEm04BSBGyp1NrjSbqFA_gVrllktv5VLHUWm20XQEj4HSJsjD8o2xyXKJTVFF464A-BljBBn2zS48VO4KDtQfYax62RFxdZ2HVBbqmGdagzwaN1XeXpfYTljGUKNM1lWtNS5LvB_Is-dq6NjwGXq0BDRVUkoyCJcfyyjgjMG54YRxHq7O32ZmQyQ0SnVHuwizAT-B3o-UwvtZr2NN3E_fOK6BxNCh7I3MmZHVOxIU6Ah0q3ZveJKD6vAuH4y1phExXFZ7g4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvkvtPvLbNxXMvPqOx3nCzzCxgX7xfKnfpdw1sAQGcgX8GNArXh-UU6m-5cfGHL8V5tOzJexwEyqqbUjqFa0F1aTriJ4tINWaa_iXef2LFuU0lxM_R_Uk2VbtMdunPIzNgD_RL2FRrU73vHM0jm1T-dPBiEcs6HGnjjThkwwuvdVFmitSSzqN934nH9gTCihhlAzXVg7SblL-Om3O1P-8m7BwR2vKeBTlsk0aLe3Y4bt2fsVXvf7QcjCcTTd6VghnVFi5nGlVGRrpPE45qPg8iPdIuCccUs5Sm2Sj6BE5nB7O8a3WFeDfLS_yEJVCs8xJi2cQfzRbEUe7h2gmx1JpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f85ecaf4a.mp4?token=bKWBaWbo3hNW9s6r6bWwgTus5ClTEXv1XaZ5N6i4O01t4zH42SdOKe6IVnBa2rCRw7dsvAy6aDUYdHeOiwBczG_aqWBR9eyTZzcL887YXUro55Ee6Czc3Jb77p8XY9yI60Oj3SRM4QLspbCcqVKNgTEcfdASxiAX7MBNoITtdJTiGUYKFm-A_Uhqtb3owX7faV-7FrSzDD8__2u1zXV8SiD4XoH6CY0xcCJh9KMdte8sNu39vB-thCNZ2lFauEYbEYBYxr0w6q5LE7FldyXezp8JKqwv_Yq6hvvcGwRnVdq4QVMo211IDXhl4F5fN8X1XHt6j0g4xtMNn2BsQ-avZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/371eeda394.mp4?token=WVWHg8KdGYsPwmfM5yPVEQPpf3CbDam7soEuel5T0WljmVw-nJzb0LmkuJZOD_HAOM8032ebutGXhCOKtKuCjg5IK9t1SO5uwVJuoNQS7s18nwMrfdUYw6q_6b9qYAFZjTzd2wHiBVcTScNpZS77BMZaZ98c3hRvds35xFhA87e4wEfVkmel1-iVJZ8ApAjJI_2a7ym8mvGRVZUGDxZrrWltpHbyhxREGXGwvJ9W_zvOL6v3fh1zXHUsBkS_LpLnZyc9lNgs8b6YjzgXVzm-VlLeci7PJki4GNgYiWr3iUd_Xhre7eFMB3uYZz3zvR6a1hqhxnzZsB7X5D5xd2u7Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚫️
آرتور ویدال ستاره شیلیایی سابق یوونتوس یکی ازبهترین‌ پنالتی‌ زن‌های تاریخ. ببینید چجوری میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huvTI1lTJ5T0fa5iHuckWZP5AJEIR2hSOPVg1RjkgFJbvG5QxYJO-NokWhKRjtrClIG4YYNiINFVlGofcWDyI75_hJvqfjKTG8yFq3SVt6E70U858U0Xk1LA1n2y8UjZwQIW7W5kRxyMW41LHEC2hfIwNHVwAUHQtvxPpO2r0_gapbEu2u-mLqN2ciU0bsxBCHUEx51F0BGxQWwe1fE6k0HU6FbZfMYGX2ieAk69ZOJDaVzKef6ZgBaPOUF5C7_P2bJq-6hZF8zgqBrFExsTPnLRjWewFlgyUm3RXvgcZESjmLdr1110ZEd9Ee-qb8gjHZnnoZaA1oLM5uj04b0Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e2aeddb1.mp4?token=jHYJZAC_1OxYHmCSWa24VX_2eK1a785YF-_a1bk_HPCPDLCx8QiM8LpII1Y7Lx9NY-1Z6KXvI0h_6geGhbSebHa5bsg867uurO4GwP_omdyrYmmWcAZh1C3VFbYcaJUQcFHR_UxZ9vuvh46g0KKtVQ-WSpKBwDmeZCXot4lUO6AABMaU0XaFZwKbRYZhipFv67qzQnKIJVpMFUOU79QaDMXRu3wHOCk7dTDr3ssz-wI9MulUDJ1i2_2xpLZQwgnF0b9NjIaF7TU0zdMcELOjFUG5W9PjaS1N-U5P5zPrxphCBC9r4c8-PcShUuZl-ts163vEACAL456ABtsNESfOwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vz8DO0TgKcan2DHgiseGoIhtARVj9lbTJua8Ph_JFtuTeq-JLqYM_ru5ovH0Tk2dzaDJCqnQHwRkrnyumMngwYyXP7LyCBg_QVKyiqnIVcvL6hLTnBcJqUQkxfRm-WgIECYy16arS1B3v9W55C54VZ-qgqzue5d7qGw7mlq9acE0kxk8JoTKL_TVmjcksbnEr1-vDDhEA2b3MegQ0rIADqmGSzzEagK56-li0zi9gooPvqaYPaz8oJsM48jV-9_hSvEd1Xv0H4Gbs8I3JPYtrRTKQyk9EnMDIs-kxVvizEa3XW4uD1kOwoIHuEMdl6CuulbrLhbI3FD_qDRv1R02YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T_D6P6ItdC21K1_g1_qGt22CJ-TbJx6sDCrXemCVd2MZd1RmHUZ7v8p048eIRkHO_k2a1HtnbJjvNEuvKqMNi0kvPZXZ8u2R4y3mZWS8y7Qj7Xba0bymCKQkyD0K7iaQbwXXQ1Rn6zByzK3SIc7dkuLlknuDuDCoOJi6Ysj2-McExE_kB7wXuqIj0P75XfzFbr3dS3limo_rTy0hzPGBCQs9IXqEFzJdJi7GcrPvR_6Ve2PO5tdshtHljowmJ9WnVeCN4A4sVlPk-j99drdx-EZNb8PfbTQr64vtY0-TuG5ZjDTqAAoI6-fvobdox73APPP_kFFeJAtNPSYs9HrGcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLMGbHLOgpOSTjP3MzFEpoh1PAgiTdX_xf8aCwqv8NyhpcKyRbs3fxf1Iaw_MGXaQOUmrFF5AyAh9hH1UFD8eQ3YOKHr4BKLhvUj-TdY1b24Ot84EENpeTtj5c5lpD3vg6Ubomx-kNeW23m_dVreP5DGd1gG2pLh6EfSnYdyfl8a1f_jNDkngjwjMQr-aRqYSNrvW9vmf5AcUq06Xt7Q13HStHe-rPmMkQqsesEZOIyUx8EV00gR07Y-hTmrK1_tjcKAviqy4pLFLZ0Rrk8K6U6oqeTMf8f-qdCyMJrKEC53Sc_fcBnqhLVkzxob_fFsIWVzeKpkZLQsS89Eljzwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEOFplG00j6OK0A8WWCAaRwXszXSflfhhpRJBdb_od48N5hzPK74LAke_UUwzMex-0h6Q8kg1t_fEvfgPuoCKHPbJMn9G9EA66smCyvuqH10pqAm5lBjOWo6kemEtALkafdigDYq6UhYa81ZeWJH2t2tRId6DX9wATry2gyP8_vL1GhoIYDOmKnwaYRyOKtG0VDPWd1CJKBdtx6QGLDTEsEqsJz877RrGsrQMb1qDLxIsfsYJ35ao_A9jDZl1B_Sn0uCzRQpYFD7SXkGHCS3Fxo4dVGadleSmAwDoY8w5-Cvu87n4SRuigEtwrcAE4IGIQveV1gbr1cFNd0VKFX5Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MF-4WP8Gqnck_iZobkXChDlcdYbIih0gjitl8hFQAhcv_myaNJlCCvMme7txY6VOsl4JhWnsg2wH1Uryosvc5eQenCu8Z6qfbZh59fjid9A9fly4MweaZXKQ6oNAnyDYiwvBMEe72CkwiGVCCUwwNB55eHTBTBIxfmOgnzHZqkuVzTX5fdA4QcSaqXQbFkhXGmMBvxMpPJhndNXfZbYS2cu8bwyMYzYk0N-EZvBqLxkIUP4AKLRFXEXJf7XUzfpE7rbyT4Yhj8jPACjAKZxDrF-ccCWHHpAmDNpyGrFNqkQMESL4kNHHgTQtSQZ8WTQEeUzZlqGzJEu4iBqHDQ9MkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGj0NiDmLIf0aMdTtx5R0XBV_SsRF-Z2GsUnAX8z6m61Q0uFoJAQOLS4kg-oGJkpuKanuoJG_8VmTpQ1MqZeGnwoT60ABrSKjA_cZuc7Lid4dGSlzU6iav5Ny8Vw7fmPV63cDKOMMd00IF6xD--AnHg8DIHNXZE89c6q1Q8E4sB6ZplBaIoTxKTTbZuPvbnjXQyB-18-8kPDK7VewgE114sBC-okMFwCWaUm4q6OFjp3cCX0FLwd6ZWE4nugOwMT9PyujPMxz9gZ5_nZxFrvUSfdQPrRFjWCn_7q1bleELf_HuNM2hkWt8COXmlzUf4jNKILH1AhdO6fc8NauOj6tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sRf36WfKWbJxFBtR4CKCq70UDcsghnCtxWR5vUmZ9o-ntoUJFSuLBJNvTXbnVZ_NpsKDXz6ESEUzVjHSMzkRemxCHxG5HmQCNacl8f5xDElSjPhGeNLeE28piggjGwBbD44bkX5wMECnhblLYWzxIZdgE7B0sfo_eot5_2h7LQawiXp0aWh2lo-X9GlEm13z9WM1HS3BRQgiaGUuWzCIuPp1qtY6vbQhdXTVn4O0vz1ls2LN6QB1FwhIponTgBv7Y_RYkXsxeIkZ4kdY-R3TSQFQIu3SBAiK_hVD56TpYjztctxNLTiejwQl5sEjUVrBjdjUIIZZKtoQYinvbMXjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo_0aBcu71SUKUVFokZj7Tksewsj0SzmFiOk_w7vyJDDV5xrApv6LV5HlKYUmub9h6MbPpEB2MeQjSswfxmWhXgJdc0ynswZeFx69zI7KwZcPNSvnc-EVObjn2ivdyLbMUlXKh75RgvENTWNPwXTZpQMioJLE8hVhHESZjHaMBqQlsnw3RhSPPeJrVug2eFCAfLVKSpgsvl6XC08aGcM_2qv8fAc6iiCSGk1BSgcp4CGzk-ODV6hE2WGPPSagWl4YzEJ1Or5exYFguqI6MYg2YSV1LpP6kzvjqnP6evTs_7KYWWGWCLtEv0ZAWUsgnIUuJmhB3fIxJPykncz7o3RTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8ryDfsdiHHTm44lnmn_rqccmdEJG6CxSX2Ji0IS01gik6WrQoMQSNvnZPuFUW8R569Nn7ysikz5L-38hGBWtUBWitU31ahRI8zxCWzLQiFHkCapaJz3u6LwEiiie2tC1OPK0GNJdtd_yutxOYAd87xoa7yDsdMjGZvESG6OGUGJZHi4eIWJzDiAZmOJzYg1D4XO53oLu-WKADGCdVVQvbM3fRsgeoSFvlVJ20cBvvMLLAfJvmx4s6gq2-xSj-taLCXHf3THnmRkI3bW_Oc39ie34nKWnEj_lF4ROzlTLsZ7N7lPbFy2sHEftEPGC9AX-As0p0teKZ-kNSROiVKVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxcqwPNnfqYvQl7-k8xQOVR_31mQM6FiZiu3yNSrAicIssDAI1IWAb3NXBG0Esi1za3b6E90PfkE4Yjvj9pt2u3cmx3tk5Ls_a9Bjhc7AWoI4tyJx4nHt3c2pdmJZlv8aCYuhAvhoEZtdThSPWLQcVhWAKP3psIe7KoQJPxLRFBsZ-xHnxD3J2X8ErHM2du1pJCpqZV655qtz0ot23p3VYRZ7uNi48g8fLn09IUqwqQ247AHgf9lpWgPMVp6qbBzTBBORE8fgdXTUyWNtn8pC7X4o5727ZAu8V-_PRcVU2YVjEb0nagqgEC_sCMnYeX5zaftzI48ragF_gjHTiTNeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=D_jh73VMTPCAN60BRdkrwglVpiHCJO9UT1_WBJBU6nT9EfA0XZ5xVDrLwVVFJQsXU5O-bGC19aGndKe21kum0bAgA5zNVK-cvMyTCBMGpW_7Q8HsUG3aM4AclmSMhZ6Wy7aBZrjIXX-daE5bJFKeHjuNPuBLMDCUB515MVrU5_aGAI99FWppGqVeyHJF-DAGrG7fe9cpKNj8IKSDj-V4PdExNgo-jmm60I94HpYDkkJdwnH0ScTOQGv5GlVK5UM4twgQFRYk94240eDFiKX0-Gqueburhb1z2qgR8F6nAyxUNdUZ0ffmicwNM3B2jyCXI3wqJStgy3wbyHQHikvftzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1714deeba5.mp4?token=D_jh73VMTPCAN60BRdkrwglVpiHCJO9UT1_WBJBU6nT9EfA0XZ5xVDrLwVVFJQsXU5O-bGC19aGndKe21kum0bAgA5zNVK-cvMyTCBMGpW_7Q8HsUG3aM4AclmSMhZ6Wy7aBZrjIXX-daE5bJFKeHjuNPuBLMDCUB515MVrU5_aGAI99FWppGqVeyHJF-DAGrG7fe9cpKNj8IKSDj-V4PdExNgo-jmm60I94HpYDkkJdwnH0ScTOQGv5GlVK5UM4twgQFRYk94240eDFiKX0-Gqueburhb1z2qgR8F6nAyxUNdUZ0ffmicwNM3B2jyCXI3wqJStgy3wbyHQHikvftzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZA8gcgqqeQjb6e1B8ah_XW-NxVVptVbrjWyo53QZErmHgOI66vYRaeIFTd2__eI43Sh-7oQNycvT--rSVq2rUJaEZjIyuf-69XKZWvwwrwIKiVS7dv-LTNTpuastNJBPGr_8rX7kHCmsR6WWTtA2IxtdsRUg6zqn8JsV9e61emqsvhIuF7kOXjOVRJEMFLdyKWf6ddEMd7ZW5Lcc_MEF-5G6qSP6dkLmO81j2z9Wg8GNGDO3pmhAKS7_4RxOuQbistuptoc4PWLXsYcVYUptTnFcDJjPfVP8_oftnuXPb95YDHmBBJmX9dxlK7sVMr_VLxjiqtbqBvb6P_Vyxc2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDA_O6d7F7QL32JaAZDCo_X1ShakIWlbVzyvP63OsT0x8aP-kpmPALmkWQRltCVyWxMimUlapSeLKIZKOn_YZrgwb3Kq-iXvKz7pJFhN-3-dQLLz4bmRFOZbKsPHhBYM8pdqcTQMCKQBqN3jx4ZN23Zfn2wZqV_CMNl45CDlkteQusDhahe-zuyU6dlqTZSGDkEfSzNDlJZ8R39UNvLYM0tKEJnIkPdc8_tfjAhtP6odXAMD58r_0ZUz4_6UdVzw2_EtqkL3BY63GDJW86CoIgmDLLknJ92B5Kj4N5h32OzI_hNyTVtIltWAOF15v3vUHYBffcjmNBvHEmbFF17v3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AX7EChPbiFOt9x-wABJJnMOTs7sNKTWZJLgZ0_7kTipPaJ074vqqoFEW_vC_i-SSwqLX9t-tWEie_vem7IY0r5x8XYSvn2GZ5UkV9eD1IwpAVsuUQqQTwTihkn2ZY1dCfcK5724eg3f9h-6m8BgSM8qgvDUTDS7XzVCRyS0fOUle8Q9oCiKrEjVjUhLKPI1WbLw70KK9J-Tb3FBfAJ18zITle-1z_3PezoDO1yLj63t5drSVWt14Dfo0Z_WNHY7GNs6LbSiHCBo0l_pUxSxJeT_k1yFAJGd3HpmrKdjAo3T5RaAjySZ7VaazvdDI-HUJuhNXEnHrwUWUvoK6UR9BMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vk6Ac5EG1RERymK7JfuXWN5WLznPnAy2Ud6hC0xnW1gD96FbMwou3Voc2tNHBkJ1Tnv9rL5neD2vXWioB4EKcz7ZxUKVL-th_woIYqWsedc_qQ225eEYo9Oe_pOl0Si14SlQwjV6Px46f4x_InJLbXWNRS_s6NQsyGGjrcO5DTPo6Z0DcQg9s9e4t6BNY7eKvvmI1K2CpF_V4PUB20gxTqea1WAzDa5ffxkVQvTOixI6GD3f6Rkiv-nmCsdRYDmMDJe2Z4ekVy0hTuDoisZYxb6zSLqxKKkZnFKSH8H_whPtsSa31ILuOdiPjGAHUJ-8kCnIiew1puxXuq03Euqozg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=KtGoUeIwNkZJDNAvNAA28XLXz53FQkQgJNjaxjBbelOR4Qg0Xc8zc4BCMB6s8fSweSJCbCu9lOili9EOCRBATJKuxw13n7BHsd74_GMnVEGFiglNqUihGCdwXo7P4tAH6t5L9oLjAJmss_pMwk3-6HAxG9SpwjQcoTBwKhkdiJrgceQutpSSN5agXhG4bLOwzlktquOQYNCKAfhV7pfgO759wFdcuvVPSYHmhqHalpuhMPjcdv4pG_XZRIR-0UqzvpSg2tJweIv2UxKiaR1gJwueYvpaJJUhcxVMO6xfexnFw3QL60qmfoDicTjRFMGCuiDnsJ-wO6yFnyiNsnUMGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=KtGoUeIwNkZJDNAvNAA28XLXz53FQkQgJNjaxjBbelOR4Qg0Xc8zc4BCMB6s8fSweSJCbCu9lOili9EOCRBATJKuxw13n7BHsd74_GMnVEGFiglNqUihGCdwXo7P4tAH6t5L9oLjAJmss_pMwk3-6HAxG9SpwjQcoTBwKhkdiJrgceQutpSSN5agXhG4bLOwzlktquOQYNCKAfhV7pfgO759wFdcuvVPSYHmhqHalpuhMPjcdv4pG_XZRIR-0UqzvpSg2tJweIv2UxKiaR1gJwueYvpaJJUhcxVMO6xfexnFw3QL60qmfoDicTjRFMGCuiDnsJ-wO6yFnyiNsnUMGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B31oeqBkUdP7BJc9xRmCurZ4fX6ZI2pUw6LbOR_Zlp9LxrGQNaYtEI4VV3KCr8Jh7E7j-Pjo4E-tOsIeViIoDRZyy3oyPyze6cU-Jeqa0jK7Js86SJ_NZ9TcbRy8e-xBH4zVneeI5w7KuRULovLz8YCvxdbX4OZuX-3ENjUS5OabTdCdlr-Zm3osyXES46SAbKrE90Ty4jKrM-feGE924qVKgplIMCbV1h7P-QjAt87znHes1LNfRoSRaH3bZTf9bHvH1LlBDcRh9q9yCxloAH4iLC6wV0k4H5BfcLzkp31ckM9kF1eSOrkkvMVhiCjitpNOR1FUqON63W7fOxCPPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzsFfswxJ9a8po8Etj3intXRqlg1-HCAZaUN7YYLGxA6i88z0AsI4eZCKqZjPU2EGreIxGzQ1rZf-raVD-ozXhfQq6z7LjETdmIsTZbPFD4-USM3u2M5SIl1NxUjPubPn3MFM3HP1cjsEDS5HqVFlMWHYrRyFQklFVFmdS8R7f0d8B-V5LpbQd6IEAvHuucEw7pj_Q_btp0hblbnMP8ngFySGqJGNmA5zo1HHiCTUJv3xmep5_TaRnxU35k3EJKkvsAHG8lyG94M8gOrDAXQuvuna25j6lkEM1zJBzddYtG27bmL1xgpvuEqJnyghe96X-ZXaDuGeq9mhmIEkPG4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0C7E04kMWx1N3ocNnDX86a96ZJM_432nmhajT6iNOVuTQiwuzWT6AgazcbaN2BiTW1cteiNS9IDZMzebUpxXbu_y81B2tFWdOU-D90K4pfHMmyYPScQrq9WYgsow9fhLH48JsEJrexWLupDvQnVcLDVWVZI5vidXjjTBdBzz4fZI3U7nVVnU4USjae4WMZ6mnhrjvsfJrvDaAdqAschDy2nvQxwyLf8asNWNphEIuNh0Vn72LfLgO1RZ-Lm-uVsPQziI9ldq5GjAe-oTAC6kdkbS02_bpE7Rlsac4w_5tLr1lwQOR2xambBr5Fh9cHY4B9k8Z6oDA3HBXIp18WN0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmPGJ3nAXdjc__0Go273veJewXEo4-eaAl4OyL2HJ3o08tEatHnpfpg6LWj2ecmHav3DqFONuVqo7p5zdw0qrBJ9s9XhEg7JSy2cBtbBxOuwhEqBaw7jRnPC42JpemSXXxk8ir0Pglp5hWJnh7U7zINPLTbji7IP04cSCunw9gmsk7pPysO8HYM3Q30KQ9USfqjhVUbIIdkJQIYxxQJ0CSC8BbJ5XCAEdC8rCsGfLKjqoopPP4Le7-EVcThueKVv6gohqR5xBkhCQMxV5XHfQ37uMxtI6ahPA2BIMBTTbeimOdm7cSqC4wnssI9VB1deYlmOy45AMsQHjTBF88sCxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رده‌بندی‌لیگ‌ملتهای والیبال؛ اسلوونی با شکست ژاپن به مقام‌سوم رسید. تیم ملی والیبال اسلوونی با پیروزی برابرژاپن دردیدار رده‌بندی‌لیگ ملت‌ها 2026 به مقام‌سومی و مدال برنز این مسابقات دست یافت تابرای نخستین بار روی سکوی این رقابت‌ها برود.
🏐
ژاپن
1️⃣
-
3️⃣
اسلوونی…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27007" target="_blank">📅 17:34 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27006">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=qIM4c6P2In11TCFGb0f_EIFTuDzmzdYzT2QA16CmX3LVlJvs2-lgIeHHqBK8gRcI0DimARtUmYqBIpdxHVH-uTkSFFC8bJZ4TVWrhJ7-hvVCwxgqMkUH7ogggAN4Auq5Z8IKQMLPIF6ptrzzTwFT6JeB9sqliMbnsDIrjzTfQQNJAG5OBWfZdLWW4fobPxA0OU7umdSzb6s_BHKFYtd41PKdsgUioHcEJDzEuVTm8DjL1jtutKYbfDH0nNUyoTYn7BTckwvqIm-Sdn2bbc6_a2Vv6xP1wYhCp32ezwGJHQvKISbfCzh8TyPLo26SWUTDM_mk8bvtGsNJhs1WPWDVRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=qIM4c6P2In11TCFGb0f_EIFTuDzmzdYzT2QA16CmX3LVlJvs2-lgIeHHqBK8gRcI0DimARtUmYqBIpdxHVH-uTkSFFC8bJZ4TVWrhJ7-hvVCwxgqMkUH7ogggAN4Auq5Z8IKQMLPIF6ptrzzTwFT6JeB9sqliMbnsDIrjzTfQQNJAG5OBWfZdLWW4fobPxA0OU7umdSzb6s_BHKFYtd41PKdsgUioHcEJDzEuVTm8DjL1jtutKYbfDH0nNUyoTYn7BTckwvqIm-Sdn2bbc6_a2Vv6xP1wYhCp32ezwGJHQvKISbfCzh8TyPLo26SWUTDM_mk8bvtGsNJhs1WPWDVRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krW8i1sJM-wQAqhCbp6-w0pGqYS5tlqCsxzxcm7zdAmGfsMio7tfZQVAVowcsAhps9qbjCEf6TcYbddzgw7KVyQzkSBL_o2UVfwjaD7zZx8u6Z6MC_L1ybejoNof0iASyb2nnvvUwcEHZBYJbLZQ0sAEOcGvOf1SAGIVwFc3FeLLH06KkBqy2I2jJIERIhmg6Wd4CCUb3t36TBGQ0Ol7utzKaZDrWu-fVnH9jzmXwn6xPk5OG_GwdcFVVrcGiUkSgO-hVvUPIk6aJnfA8bWi7-jo_bLsNsHEcgFMFfJ7x2bpQMKjkwKtYHZFESdOxr2ujFrdeiW_gr17OFfI_gmppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsUJ0o2RrBCIxvtjzaWJXtiojhgdo4U4BIeygNc-T0RqaVqEirPyTX811Q5k9gen8GA2ZDGYgeAVSGd2FD_jpkwP72KvS_QkJSqQXXlxnRgMxgtBlYOrQFJLoNWHomGII0M8GS3Tb8PfKmA1x4_bc3PTtSgU2tUJJJsqH7k132sOVKEWrCqyOFP7_z4zts18HOkK6qUT22GW3qner0PcYnMSczWi7IfXrGlZ4kfrmYsiu90cJBkQgCb0jVeoQbQmTJVIFhtBVMMRpw6syh5_Ns-hE6fH6pJGeilz6JiRCFLimyTxxAbmFLBB5uob5BfTuDkDVykmAhStgh7InepQkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GP4IRLw6RP-nv3gJnaXrWfAFtnvCnAtYIe71gSWdaFxUplOLq6Zs7-agGV-AfXudVkrG2fFdYFeOAxQ38FQGS2GprX3IvLf5HUnj9Wbr6CjO1GppDT6K6YMr7EUwIV5WClKoTUjjE8Lx_qy5dF2ycGgZGDen16MBpJHuZNqE7Lv__i7JVVEqpS3lEL9hD5_Tce9UVDHNnxB8wzHNtQV6PuYcuBvs-6ie1b4iIiRy_q6u3EKlEAgx0oAVEuM7LzugXQqh9n0AIhEtv2w_6PIakF1Ozc8mTGVuTnlgfootogmZsmAqnHtEHqtVJF7ewBPCGMBpd9UcuvMWJlWGEQed7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZML-JikJIm5F7BFS8sUH9SW0aPFB0XwkyQJJ-gvAcnzIuGAKXwIIBLJ68rP3h7WdP5mgIz1hhq1QwH39PE1D1tTlt_jF2WzMx8V1FXaKLnAMlo3Km1ZHxoZEyc6mz7zz7LfxCF1qmfazrSNThq9qgQpOhZOK2v3ZSAbHSwiJNOFgQIeL9W7cqaZignK_iFlsLASM6RzKqhcQZKvbTWDd1YO2vivMNOibTqDzHfeWjak51Vkvz7oEG8QvFcGvdI3SJWmcRYXSIWz_EichyJsQExWCht6dcZ5thr0vW-ib4ohEoti3cIHgGbqbmiLmQBDMBUFfqv7KCNBjdJhumfGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💰
گران‌قیمت‌ترین بازیکنان در فوتبال زنان
🥇
آلیسیا روسو - آرسنال ۱,۸۰۰,۰۰۰ یورو
🥈
خدیجه شاو - سیتی ۱,۳۰۰,۰۰۰ یورو
🥉
الکسیا پوتیاس - لندن سیتی ۱,۱۵۰,۰۰۰ یورو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/27002" target="_blank">📅 15:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27001">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYZGt0nA1YuCw7hg4YdtI2VHZGdlzlhjg3qTLbG5mJBScf7AhKNIUm4DHzltji7uOJBUgQDZHcGvPjq5wsA1qrtOoutDX80bBIx5uTWual1HrHLwTU3YkD9NhR0iIU4mqdPnjYREr_oEJsql3yJV_qcmgKhD2F7GQqccH6jhoFW9ybywezxcBKFdlXNdYzQiCN47J9IVmCBY_ylzUA-TMV2MkY9BisyMCdUD0UNE_tSVbVrphsRRV2jy-njSfUIP0oZjh9yaBiEfYHve3wjv0ZClr3Bls6myS4t3E_JbOGa7p8U-woIqXrl9XWU2Bon6NU6OmGv_WLrxzjAK8qkr5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLw56tvYEtiwTtp-YyFtNt83DNNR_mIU3RUAu9P_52jj9cb0CJSvmdYXMzrwl1TT3EMSn_tsnH1Cd7GIVgy7yU7_SJiKb757cI5Rpt43bYHqUv9EbAgG_lojQJfFzGIHPbF43PLNE5UmnMHQI9718Wy468grXyP0pKA6KjCjacT3I2GiINenTZtKAr2jDcBiHdU1qBJ11bdn2Zs2dksxsZQB0rQ_yLfH0q1l7bvIfhbHVpsukTqpYcPgDUWIkIJelDBU1noqXrOzk7ThD7HEw88DREjY0HZEGfeJPPhg86zz2ZXNARHPURLv6h-7yQJGb94HcGaptlow9nwyiwlg9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UlqNRJCUjlGYhUrqSXA4EJERJLgp5OJ7qmMSivLuUjuluyUPNLUeNWlHJ-yXC6bocPvTPXVctbqfEoGKdDxHUufpk9bZn0RN1JGYhmYa3x646i3muGWHXaZcjVZ0_g2J6Q7MLDwL_F44q4UWmBBCnP8ZYuMqVWC5QyPbd8vnSMfjh460KSAQsaZ9pjLMfhHWABfgb2VDJFrZUFh0W3es4BxIp_PY4XALglvi823-dX5lrzjud_Dp6qfuZgM4npAoopPGauOa_6VI207zej-8DCbW6WjuhEp31r1_HrNipoISmImiP8wK6wSMlUL1HpxWnmrOWzanXvwjV0B4ha0NVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UY608TLLpizlnmmEoZo8TS1szBDPE_iqIx7tKjmRCTVpB_BbBhc6Je8xXlpym1qfCVshjfDVXIZ5N7D3udNQ2jfDzum5HTUgmEtS6Gxku9D5c_rAn--3RNHvaVMl2Vq-bMZ2xLAlZQfIKiQv9MN1yZy0s5xmuHNGy_0vVEagZ3TcMRgOmK73uhUdM_FCCTOdHhD7pm31ejlhWz4AlScFS-o2vm2FdpvTNqh6Are_a15wSBEzUx4myT2SOMBPghrBzXQMjATBea4lagFXZLEBrM2J4oMcwVDCDSO1565SuFJQbiccW4MU76j4U5-8Kd3mZsj8mdJ4F6WNrXgr66zNFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYc2pqBn92ufkzKVCJdchrldBHJbEfITe4io2_QACVbM9mSNWG81Wb5UdwjINWmZDmklyZ88f2B8v2DQwz9qgZNju3nseIfo4-ZtmuQO6xZoGrPxsbjgg3LHNcHh0FHyC_ZW64CGqLFtHoczqdPBpY7nISPdjHrJbc_C04DQInHMvc1wxlSRjognzcy2uBlv_qrlN-NjWXsbVJA5PcY_uQ5DSm4sLDyHoTeXpGB9r6898_rJAW-AvVrLa6uU-JR6nrGG77UoN0Nzwb9hASMFAWvUMJiRD9qqhRVDN2-eH_HlBl4mZzjOyC_cPZ1KQPD8UVlIm6KUeW9wZN5k6QcJpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRRoWTHYy81q9ghjlAid5qx70smgXsd6b71B6Fnu3ZK6Xp1H8TpwkeuuNLdaELZ1YSOC5NWRSKuO40LuUydmXAsovq61CzIcU1W5nkeZq_gJ9i0T5qLheY-DOFnTG9tE4Ppv5QrBbo-B1DTrNDtvIvuCeE2TKCgHd6g7uz-U2FksdaQueniLRQTXkEBY1uWq5-dpHjxPeRcdCXo6eA0JVLUTxgChVpcR19Hv7rEJ0RDigOXDeIkfH4LUVwrUQ1h1rrBdn9Fe2zMSmKwxSDOsPC1Vtk7EughXKbpbFGqXqDaKBY1tGuBSPfbkp8x3vqzJGPf3psrziEO7xja8zVbFlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=b88-TVk2O-v9pVctrxPU_L-DCwlvIUClZ-tXlFQltVQYYHoqf2OTtzS_AOX2HGZOkZ7qmFw2tIAPrcL_0C3QZvClfZSYTHDOIC387tcNk37C2qlobyeOdOuZdZVpaMX_u23823QqvMkm6rj-WIo5P2eDMA6Kz8p8DKOys4GE-8kaCggvUkte0CBLryhH8Se41fLnAacGe7dPhFt5kb1g3y6mHpQNA3-ppZ0-v6d_7gTRWu3QfVWAbdI7-7eSJumDiy8tXay19UboVMSxXGokKOKuayCXf-dMEMqVHGK8Szq4Ni2RsJWnL32xMMXs8o_ghF5e4cLSvHDvhGmzgWUj7D_Qc6bgZ3zEid0cCUo64OBSLj-jiDOLsRsM7MWT3ItpSjsXXADbEaUKwwCyWuTtwjtTKVGDdaEpn7dbzsHFCJpc-57vpt9eX_8F5vJpK6CkHbdNwv4ClY4oiwm0_qIRbgl_iEBwbdk2oFDptCDcHccGR9DYm8I_eYWb2N61eY9AFeuVi1Co0woAWQpXSBsShiYuZYT23XZXj2ke7McZTzonPNS_3gPJnCcLCZKEHHlU-DEujLVgf8zByMgJ5DClRwMXzPq_ohsd4arRfDC4cRvTvoxzQurI4p3ForGKYoeYZRNoAfNvxNHXPudtq3UvV7-0CPA8DGG3mdLHG9t79oY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=b88-TVk2O-v9pVctrxPU_L-DCwlvIUClZ-tXlFQltVQYYHoqf2OTtzS_AOX2HGZOkZ7qmFw2tIAPrcL_0C3QZvClfZSYTHDOIC387tcNk37C2qlobyeOdOuZdZVpaMX_u23823QqvMkm6rj-WIo5P2eDMA6Kz8p8DKOys4GE-8kaCggvUkte0CBLryhH8Se41fLnAacGe7dPhFt5kb1g3y6mHpQNA3-ppZ0-v6d_7gTRWu3QfVWAbdI7-7eSJumDiy8tXay19UboVMSxXGokKOKuayCXf-dMEMqVHGK8Szq4Ni2RsJWnL32xMMXs8o_ghF5e4cLSvHDvhGmzgWUj7D_Qc6bgZ3zEid0cCUo64OBSLj-jiDOLsRsM7MWT3ItpSjsXXADbEaUKwwCyWuTtwjtTKVGDdaEpn7dbzsHFCJpc-57vpt9eX_8F5vJpK6CkHbdNwv4ClY4oiwm0_qIRbgl_iEBwbdk2oFDptCDcHccGR9DYm8I_eYWb2N61eY9AFeuVi1Co0woAWQpXSBsShiYuZYT23XZXj2ke7McZTzonPNS_3gPJnCcLCZKEHHlU-DEujLVgf8zByMgJ5DClRwMXzPq_ohsd4arRfDC4cRvTvoxzQurI4p3ForGKYoeYZRNoAfNvxNHXPudtq3UvV7-0CPA8DGG3mdLHG9t79oY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=c5PSmUaRv5QNpufvtXo524otK-C_9qFXzjK2eGqWhq_X3Izb1gQnc7RwkdbPpL_QzUw_OmRQH2OjvvdDjX2U4MQNdXzuZD7ft7_vC0dfy6xarnBKK5sesSaoqQ9mp70j-8UgDb_sVyPcRZA9dJ5ICv2sIClcmW8UQDnfVALDaZCJT8aJukc_L-wxkA8EciFaw4OhT4h8ujlGu4LLxTU-t9Thv_BP7Y_70S6qF1QrQRHk_C-SUi8RsPoAGOccN1brLlJN6qGA-pRBk8032oL67YkA4ChDorcho5zQu_DDExVvmHeas8UkT5SiQXoccbmwf0BqP8IUfQoXF4qDMIWOiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=c5PSmUaRv5QNpufvtXo524otK-C_9qFXzjK2eGqWhq_X3Izb1gQnc7RwkdbPpL_QzUw_OmRQH2OjvvdDjX2U4MQNdXzuZD7ft7_vC0dfy6xarnBKK5sesSaoqQ9mp70j-8UgDb_sVyPcRZA9dJ5ICv2sIClcmW8UQDnfVALDaZCJT8aJukc_L-wxkA8EciFaw4OhT4h8ujlGu4LLxTU-t9Thv_BP7Y_70S6qF1QrQRHk_C-SUi8RsPoAGOccN1brLlJN6qGA-pRBk8032oL67YkA4ChDorcho5zQu_DDExVvmHeas8UkT5SiQXoccbmwf0BqP8IUfQoXF4qDMIWOiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOI8GRLqcBcZ991sq7VtuCi5NsgzlLK9ByjRloskxyXLAyjPhcJtTMaatc7FtjragCMoNWUTtOwy1tvdjEf3r1Q32NiEic421fKjAfFbXE2Tuntj1GuTjtsM42D4Iakj1ONCii8yaIM9o2jeoAPvVQxnJT_XK1Edut47ymI740p610cnQvvtxdeEC_F2ZkQTN0boGOlGV5FG0uwwSid_hO_ow73H-uRmFipHqDWLgP-HF8tcLGi3g4aE3XbnrlIPlLI1lRsNbuWWyZVqsFi1v7SCGAyMUWAOzZXTvD-NJ_YanMZ1GZ_Yf48LRY4zQ0v7JX4Hifem4Zvx26VS_ej8KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/svVGfMuE9GkfYWeAemIyUKm79L8Ybdve8rGERIQoBRYmMkUmynLZ66h5Wo23cd-_wfWP-jHvuNcXZeLmY51SuWY9bWLhPULeIeuZSvge-5jo0wPI1aENfQeXEngpIZ0P7tqNHHE0EER3-ruGyxDAy1ljNT6R3xDr_FtJLS4F8itO5TOtN5r-8NuQYz9HRUZZK0KTSG3ubFqcjkIFG-Ipc9vunhCNM7A85XlAYG1_dnZ-VB-J8Ej8eD3aXjMzu9Zfi5SKDgXEdyJ08JXIqgkE8SxRfuniQiBW1HoPfJU4GwVmfwXSb2VQhgcCYSk2THAMQiwfuq_uGrRrtYRHZiWX6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_Usx018XM1qPTMqbr78Gi2g-2XQu2FQ4pzRtgeKcLXr2u71ZJI9gAkbwuZLEV_mj3Rn3mW3d44R4BfLeeXZfiDxgYckNA2dhg71E2awFcjX3UbUAwQKc4uYMC5rXBNLP3Ks5_Cu6P7b1RZzw3ZgWMem-I72aAjEEEpOzYFKNXbNrcnNXjMODKKYykWEey1c_hjgnz8REhoa97cdCO5V3CcDS3_16RXrorUO0ojP_9um-mAW6Sp6zneQLut2Wvh-_5O_KwnJd8oMi6dhX3d8RB9AypuSvzzqUpQU-7dJcL24ZEbCw5N9OZ946UOWiJb7JtJUxbLksrgP-9RH0eqzzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okYh6xRvkds6HGNm_4tzDE6WNWoq_lgMfc6Te3dOiIn76QzJ8jCNf8gQvmLOCF-Tzw8TKNPL6UZroY4B7Y1k-lZ31H39LnIjfdhqBmSCIF2E47-vEhmWsw719q-lLljmnB-2m96WJSPZz5EMUu83rvpuAa1C__dnEH4TFslnO4WvRVWpnqtr11-3bTzk8ny_im1CXOGqt8wDQpf35dI2bkVd9XISUNiUuYVhUqSuSqDA3f6DAgsGZSlA6zdk88gVY93qbYMffGn8ccwiN77aMtBwialBYlnw8EsKwjhvdHstW2rjYxqtyjvRsGqwPeoAQbc2BO3HjLZyVYn-tOMvSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=BX_bRThZsi-yokejcZKdVo4f0Nr4MyQFFaokXKaG8XKlAScZe0SmhnPPR_w7-WyUlf3byOv9gFL2NP5tzbQu4YSE2dOfgyeSyMJfFPLAD5VQAoGO2uwtT2yHhj2qzuIiMeJfbAgBVxmrQOVdHbeSNdXMdoyTPlGx5ZHN-l9ypLrUghWxQYccDU-c_GJkwhtXDSuA4HNh8L24twTqnL7JEssHZ8ilkWtV1TXXdt76IJ0NZ2_7qFpOz-hZ4FBUkZveCauX8MyVb17s1eEIM9w8NlOut1kWDy62XsnQl3N5rKbZ_wT5OULe3ymkIS69ScqjwV7wusmXPEemACryT_AiLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=BX_bRThZsi-yokejcZKdVo4f0Nr4MyQFFaokXKaG8XKlAScZe0SmhnPPR_w7-WyUlf3byOv9gFL2NP5tzbQu4YSE2dOfgyeSyMJfFPLAD5VQAoGO2uwtT2yHhj2qzuIiMeJfbAgBVxmrQOVdHbeSNdXMdoyTPlGx5ZHN-l9ypLrUghWxQYccDU-c_GJkwhtXDSuA4HNh8L24twTqnL7JEssHZ8ilkWtV1TXXdt76IJ0NZ2_7qFpOz-hZ4FBUkZveCauX8MyVb17s1eEIM9w8NlOut1kWDy62XsnQl3N5rKbZ_wT5OULe3ymkIS69ScqjwV7wusmXPEemACryT_AiLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=l-bzinbmQR5iryhIz_VmYC4WDuNFasyWJlXMt7UGwPw-cgf4aoq4tA7e-HsJutRKy-Rh761iSl85qaI5_P3FGr86GSvYemX8Uvso7fX01pA05wkfuxOZLALkivnI3a3ump_qwdyqZlPl6rt5E4DCOyOLi52Ubm2rm2oRd43wpi0KjFNx6_27tR1_JT7wqO1fyA-1EWVrYCoMlZiTXjxQJbEYkFIspiZd-ulLicGVSMP4MnO4bDbCbO9TfrHri5unFkoI_sNHgRFfWxhhFl9FuEoKx2Nbe2WATIXcZguiDvQuFRiKMws6DpTF_ej1iK6MQFZknfBlq5YU13szv_ZxeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=l-bzinbmQR5iryhIz_VmYC4WDuNFasyWJlXMt7UGwPw-cgf4aoq4tA7e-HsJutRKy-Rh761iSl85qaI5_P3FGr86GSvYemX8Uvso7fX01pA05wkfuxOZLALkivnI3a3ump_qwdyqZlPl6rt5E4DCOyOLi52Ubm2rm2oRd43wpi0KjFNx6_27tR1_JT7wqO1fyA-1EWVrYCoMlZiTXjxQJbEYkFIspiZd-ulLicGVSMP4MnO4bDbCbO9TfrHri5unFkoI_sNHgRFfWxhhFl9FuEoKx2Nbe2WATIXcZguiDvQuFRiKMws6DpTF_ej1iK6MQFZknfBlq5YU13szv_ZxeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwV8cVIMgARpX2FUkKOgClhIL6MJkASXO7ex6Ph13jpK8htkrulP2MZADyUTAXW1HOUk0XqLew6b5VPJPPapj1oyjdXsNxYnmcgtfSGRo2TgdGPwRLxj-F-ZgY6-_x8g9ZkpWkrU8uMcPeCSWiZIO6ciSxKcsYmsNdomrQtOj-VnWOgVB1yAViK5rDRiSf4Z_ONAOaZDTAH3EIGy1pa9R2UTo23DtQZ3kEdIZcD6VEqFt8RRiM0nqZIap57LurF15QG-GaJuw05ip6pD4VYxeN6ip5rU99lVyDGQbJKyTokz1tZhTHbLheRy8UZ_BZsJObWn9nZnd2Djxi7zluyRJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkduhCbvtauuMTbxVoByiNUL0ycoY9SIvaFQVOSiRDsa_LAsQyl4BPk-tlotYBE6nJQvtMbwfuzk8tCUUzAufAOEIMQ6Ncg9POHErCAi065f8LAE5MTD4naFaD50_RPis_xlr1MQ4DwKHiQQnCFqhyXS2aZLmQRkCY26o-o06x2DnrYCDfyfRFH9BSRxxKwbUvqRvMqONQnUXVkBbKLqUjrQc_FsbyZGH8z2G2p05qG-WKDl7tHane77Dcl53FCmzp1ASBWgWte_UMmZdxCVRZA8NJRiDUTMeDrXPcaEhZ0UuNo8KSDdgVsJzcy2Ye3soChQWkDCxgAt63RYV6cSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=fKEKd0zaDiTr8lImdp_4QgdEiSaLg1PYrWyroxOfisbCzkh52Yt1ZaTZUl5OjKddBszZY_mZhGNJ1zGdEagY8HTzsmoPYJzIbcIH1PDs4iwJBOkOmwSMuwj_6NfU6l2zxiBMXgTHaqttOaXEe__JWQam3zCkJ8RYAAYrK4QxfuHOG-0cN_Bwtpyx4ZbJh6kJ_Y5jrDiCQiWH8WBKoNKSyGaCFaQ5t2CjaamB7YCMmE6tnQTZQYNlj5LhhG8jIZBHSufsOujykTPSocP-vheObChuGkycyBaJCLobyZVhKlB_rk5v52cXqnjONv0G8G-lTQUu_t1MydWdSGs9MohaNySvLYW3WxWtODGTq7H5AcUAflrIfxnSKE_9cD7BDCHRcsYyc7i2BHNRQ4sR0_VdnOK39U-gTsW01-dP920aGgOXExTYDbV21zWZ4ULW9mDoXqfNLvWt8TBRkIul8tBi-tXjLr4eLNsJc9LEUadhflkx85jnPrLC4C0K8PiLgsk-WNHE-vYCVSgJ52PHtwcC49iSjRRXvSESjNevmUukDQRMEaoEBnQhJcgFkMYSxrt0HUpQTBw2kIZDJ6jiF-X92lY3LXfX1eQ2xekgvvUlBSlk4QYosRBMdpUrdq8P44NV7QSdrOeopdgt0fFALtw_KW6zCN2y_vvb6kE43R1nR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=fKEKd0zaDiTr8lImdp_4QgdEiSaLg1PYrWyroxOfisbCzkh52Yt1ZaTZUl5OjKddBszZY_mZhGNJ1zGdEagY8HTzsmoPYJzIbcIH1PDs4iwJBOkOmwSMuwj_6NfU6l2zxiBMXgTHaqttOaXEe__JWQam3zCkJ8RYAAYrK4QxfuHOG-0cN_Bwtpyx4ZbJh6kJ_Y5jrDiCQiWH8WBKoNKSyGaCFaQ5t2CjaamB7YCMmE6tnQTZQYNlj5LhhG8jIZBHSufsOujykTPSocP-vheObChuGkycyBaJCLobyZVhKlB_rk5v52cXqnjONv0G8G-lTQUu_t1MydWdSGs9MohaNySvLYW3WxWtODGTq7H5AcUAflrIfxnSKE_9cD7BDCHRcsYyc7i2BHNRQ4sR0_VdnOK39U-gTsW01-dP920aGgOXExTYDbV21zWZ4ULW9mDoXqfNLvWt8TBRkIul8tBi-tXjLr4eLNsJc9LEUadhflkx85jnPrLC4C0K8PiLgsk-WNHE-vYCVSgJ52PHtwcC49iSjRRXvSESjNevmUukDQRMEaoEBnQhJcgFkMYSxrt0HUpQTBw2kIZDJ6jiF-X92lY3LXfX1eQ2xekgvvUlBSlk4QYosRBMdpUrdq8P44NV7QSdrOeopdgt0fFALtw_KW6zCN2y_vvb6kE43R1nR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=YaXFgr3wVrYSYLJNPR1Ad6xTnulMbjKlitsmQ2PApnSs2KPuzdzkOWMoQhmfPOq-GMKSApm5A-sktJfs6ZrMfEGCO7DXK87bHjfkZkz8jauSABIno8NPw1srlyWEBSfOi7YCYoaFqtTisbd0Res3vmcU8LD8EJ4Yh9Pvjc6vZ76uThnYkOrq7y-WMHP1HcK1JLaeadRnvcmeaJvhOwBWODdBkrOWUmTTaIgH2V_Q1LjWZToD1dkNVejGoH_x2XYTmasB9odoZmvfcMOdhlpvW5TVpV-B2f2CMiZehUHbkRfG470yHYNxatFwHK8n6j9zPCcDyRSuJPJjkQSEs7UuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=YaXFgr3wVrYSYLJNPR1Ad6xTnulMbjKlitsmQ2PApnSs2KPuzdzkOWMoQhmfPOq-GMKSApm5A-sktJfs6ZrMfEGCO7DXK87bHjfkZkz8jauSABIno8NPw1srlyWEBSfOi7YCYoaFqtTisbd0Res3vmcU8LD8EJ4Yh9Pvjc6vZ76uThnYkOrq7y-WMHP1HcK1JLaeadRnvcmeaJvhOwBWODdBkrOWUmTTaIgH2V_Q1LjWZToD1dkNVejGoH_x2XYTmasB9odoZmvfcMOdhlpvW5TVpV-B2f2CMiZehUHbkRfG470yHYNxatFwHK8n6j9zPCcDyRSuJPJjkQSEs7UuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVwJhAtswTIHMMzMvpJI1Cwo2L8wOnDybHUtONRqiY9i8pHERkiV6CxtisIrc49UDvBS085VM96QzbnwWJHlG2NUGYKGLk8VRI5Axwus2Rrx5PVhKUqDpQNYTmUUbsKVdA3Ac_8UmhY7TUquRPvBX9a-EcCsMn0sVglxJSI1ZbhxrwGHA3rCZKdZIipcZJZOigGbwfkeN2zDevaeYOpBPv9gxR40NWnxob7YNj4BBCmJKeWT8vsT0lHYlkNvYJGG4mRGDlkRaCsgLZMbQFOGtWsGDpNek2RxV9CKkPNDCgPL8dJTOvpxqXVPHt4anu0Z1DlIXLiHk1rE5XfCGy1MNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=RjDb2Ca_nRR3RlclYx21UAmE7AyPtSMG0dPwzznLXyemcMMKWdeFXcaV14d3qyuQQ6qzMMaQvutdM15JYAm-DfC4nUHly87Boo4-JxsqLhkPiRUaaKa0l7MaKqnF27wzpV9VwW1RW0WtNXJQ0xtCPkZU6DdX7i_H2n6MgMlVFL6i4owEyu04DJ_Imgri_LUa6ICvEZtBe7uSbfhNm3QrEJrbA0jhLltuoLQVwDZ5Ds7eTiUEfhjb24laR0T5OBSsJAINHsNQHC5BrGZllc-onKrTKsy5rXlLTzY1zRk0Rltms1SjunsJs10LFC0MTny60lo38LoiCIcrvHpGm6Se7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=RjDb2Ca_nRR3RlclYx21UAmE7AyPtSMG0dPwzznLXyemcMMKWdeFXcaV14d3qyuQQ6qzMMaQvutdM15JYAm-DfC4nUHly87Boo4-JxsqLhkPiRUaaKa0l7MaKqnF27wzpV9VwW1RW0WtNXJQ0xtCPkZU6DdX7i_H2n6MgMlVFL6i4owEyu04DJ_Imgri_LUa6ICvEZtBe7uSbfhNm3QrEJrbA0jhLltuoLQVwDZ5Ds7eTiUEfhjb24laR0T5OBSsJAINHsNQHC5BrGZllc-onKrTKsy5rXlLTzY1zRk0Rltms1SjunsJs10LFC0MTny60lo38LoiCIcrvHpGm6Se7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj1W1Rb_UF8Z63ENXpRAj9kT3Aq-mj5IS5xU7tvFnwPqcZg5rx02q3z8979RCEShTQSKjpWRzQwZ9ZTl_OGC-9g3EcV9xApFe2x6mo7G4EPpDuqINq170Mo78chqPSqDPxPI_IQmwjtRebaEXU-Ci8IvCgm1afKe6FKev6EZevqOh2TBdkQSSA7wSxeU247dbTeicJkhGg_E_wVm3uvikhJY8eFBM3ZtGxNsGGo4SaOm69ZcAxAQnV9gk1mzyQAyABywltU80MumzU1A2ZDLEjkGwW8pO7E7OzBk_ZnbVuEmsg3elvA0BonCj-oIT5WPy9Wb-ILgVuNDhA9LRvHPlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
رکوردداران بیشترین‌تعدادبازی درجام حذفی:
🔴
محمد نوری: ۶ تیم با ۴۷ بازی
🔵
محمود فکری: ۳ تیم با ۴۵ بازی
🔵
مهدی رحمتی:  ۶ تیم با ۴۱ بازی
🔴
مرتضی فنونی‌زاده: ۲ تیم با ۳۹ بازی
⚪️
پژمان نوری: ۵ تیم با ۳۹ بازی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj1MUa8Cu9zN5N3Z37gCD8A52AuIsVTiXkdxXres_DLNHljat1QbtMapE77wAkbF0FY3YQ4BaZ9jqkEWK7ZUrYfMZEaxrNlvDVPPga-6vPuoq8fW9L62tzQ8pX-5lRJpldw6UaZu0OPtTZ_MGjigKQVwaijjIX1rQ3CUC6ywq_ffeuynEI4hKFi6Su_f4UnB3xloVQRa46-vLYtbVLEMnUqA1h0BD7jd9GXrXAl0IEkVm_CErMb3TUvyW5zPAJxgQ0cOaIeQe_Y4QQ4XtamN0qaSprRieOuGqPazvDnKo74HGZsW-SxH9ada-tq0WLsKPMy3JaPihGKXfXUg4CS3FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPd5i9I06PWOlgXsJqNP5Jsmcl-nrq240gx7CkI8AJlawgpHzxptip2prL5R1CcZmyMUBiPNvtGEtYgGq32KkKW7qjqW75lIenbHAAjDnaSalYKhk-ss1rPBkDfq7ce4upbHjuKDNvJ1NYMNC8cH0pbmBsMM4bGEgtgLvEXKV3OORKr5KOfDufDlnYEpkO5saOmU8McvZGUaJG5VhvXCgyaLk96DpA6WYWxByLVqmToiQIV5L-nZu8i8D0iHyk-PoZ95TgDmyLJOFpmlMmzD3OZhCz9QPLOjKZ3uDJtl9oQBFKA2JDW0IFnCGpZb2u7Lc3wFPw1c-JxsCkTFhqrehw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZHkmS6bQ9mtvr2nqlheRmPfEWUxBFqh3iifn1k9nS4gAd3LV8aw09htK3iOR_dSUpAzmA-bjsIQs4URFNX6tW4zN3AQLnmlQNN1ydT5TaLE3X9FbT3zJIUoVVTrZFv7l9Wn3npe7Lcma5njuvAq5fbzbYy_IK2XMZtngZ4-L8z7Ev5jNMierBji31ivOrJctLZcoSTqYPSaU3GyMzNIy8WT_GfgXVd50X1SyMQKCns3c53rwtDBQ1DZf_v2HRudItPYAEwlwcirB66SCf2CmW7nS_L7_r8007MhKCSM7adxnhLzySFFY-cgtPEJ2KR4FgwewNlZcip6PsP377JWvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX5xBb3kGCp7CiqMMW6ktLWMDBCn0D5jpYmZTIC_sDl-8mE1x9wI0Xl1QORdIrlJjk7BVHvQBDSQTuA4NAiZeRmq2V-TA-qvBMFtqSxi5CofAaQmpdYMVZtNQVS8lz9cXX1VZEED0kesAl5uqwocAkOZDHtusMMFlRb2xGRCODyA0nmt4GE05bcV4T1KSS_fJUk-wYGRtgKsyNF8By-5OKRuHbQth4YFmHVu1Kt47ZtE9LzWb9A7li7ztX8XSqrIPFBgcRxhSVIbZFiu0NLRojTfeZArwkvVaF-NSADXSGGX8DDLPCG8Jp5DOCnlbLIQkFPagE7LXddr6SmFEWhpvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJN-3ZQqb5Wqe7YM2PzXQIqHnbwIKIl5XVJixSHM_BiEeV8TsvnnOXA8wUaC6E5Y65bMymWEbO1IJdF6zQtmI0Ap6Z-x4s3jJLCTWV3WW3RKiJ1Gt_-utcliTk0cxPXPt3Mr9POH8-UNyo_2JjOV5f4704V9QKFIV77LrwtRmzltYpzg9Zsnmj_btmsMg09Dkpjcq56tzYVlcyjYu4OUzvPwMTtNDPrfFl7e7rOlJ6OImBzYQqVV_V04zn5yoygoY2WSFfRsgID9K27OOKk0mUM7k5OFEwbaFqimWYyNlzqUc25rYHgxnt_PXQmI_MFvmgmo-aOUHc_Ckqs6jFLoPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEEBxWwD1Smn6OtZP2vwdTyb_2glNwsPZNDwcNDs3UEjEiOPLdT7yyAA5P0aKS2p_mLul80eOUokJyvwSx1lgWihdCSA4rKlhI4USI0KTbdpItzByqgYDhMZ7ARHR2vLpoIaB_ntesIjxLJi-3Av2SoA1oy0iEXDHIXbwka1xhVTjRtnBnq7jYn3D1I99BUgAXcmJFVR936uqc_OOXEyp-Z88hpXT4T9JtrO0H0zbfRG4PMF1817EGSpEuPdYR8shxauODW5X3PHF4LiJUxmE1qzUGW_k93Ulk03MX7PaMrLu3Vf9kNwYyfQVLdkHJjmrYIc0sb2AypZl4gewFc_eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k52ru4C_KT6cl5Fy4XS-7PHUkQejsXuxAAPQ2dktpgq51FtuVz4bMZaM5jTaxbLdjVg72MBCiyXRYZ9gNwL9U2yojF5u7GRfWQkKhaZl92ptuESUgACGk_8ywAlv5A-tXPDw7j0erZZfxTCs_Aan1GmE0AkA4VKz4sFuTiwHoSCO95bAlzweClkA-ayjuzA1Gw4bKrIgOkyVrhNKMC4UdDjOeoMOtF3FB4IoEcTLG8Z4yz8Mo_1Jj6LFvoNLibB4gCcz5TGiDT7VbTNozZRSRlb92wHJPecU9EFF2WXGi8PFHPXR8RYjNvwqwGISMlruNpVbHExm8u8q_Ns4tywo0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CUbM_5vLexdK9FW2CWF2Ww63Bsdu3Xl2iT-eta2wLwmdB_2BCNFp7eSSSll6Fj8NeLu7IjPcdXASSv92x0ZwGavQjFlMeQL0Nzzsr-czCCvu3lNugrbIuYCgf_Fl0v8jPi3CwN6D22HvZDhs1JHoZaEYHb_R2aqniE1xhhJEK7MNHPPn7dPfAKKyzFR0tITzQLS9NnIvtsr1Rc4TD_7gswT1XinYWpw920ry6LAYqng8aybW_ZkAbCO8UhS3U4BWZxmNcSMxiAZ1NCIG9uS4hj7vAqfU8AOuW9ByG1ApKBzB9goPjcuVkY-Pjf2Jl6Y1P59tJTy0sA6gBQba4XFpPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jYZAyup1H5wS9ntM33hn75wsxMcYb0JW4ZMqi6cH5W_Fg3_o8yNFchTuck_o1Vx21Wm9dI1c8R8sIM9LCY5-m5Nkguts4wRKphDm_e9h1peoYL2CbijepsGbuebseNO3qPYN8D-7n3cdycy0QMbIHSbWPlNz4UNxsWoI0kFPVNTCumtriwXsZRKPXzDstniVL-xwuGpr8pjf-X1oicL9deKroWKg_2NPlz9SishUidUwdpaE8JVm2gHNTVRchhGXZeIPWtu_24iqtUe_rUlC2kW7rmpiwA5Mg-RPWZpyQFHjkuJmQIl4H8JNKQaAqpbEuACF5Em77MClk6LBVb_reg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xc1_EC4sdVw8OqRpmhM9h3yXJ364MxZMrSPluOIIMBtcvUR4ACICR6AQmhkqTFOKeHveVaUtJlFTJruDyO3i9pDvQ6CeqW-HWjKFGvvv9Pg045fMGvu_g8xFx_pzA0apTw8d0TKIhag_E_Drs6sSUs-92TPACyuBE7J0erlAIjyx200TRwy2ibM-CEusW6YLLgeqvXWLlGdQMPOaj43Z2CVFzp3Wf_LrQljdaWHwvmEGxjT0A2169dv01JtfQCVwn6TJtwBrB4Y-h53QiQmr6LyAhfF8mr3hozoOdaerTdvLQ703_v8F3l1aZ62o2VkNdTvWOmt0T8C1vxvWlS9eTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pz2SJmocovZOOxnyVPbCaee1LiC9zEADNTjPIcEufdYS7pYgvPY1qn4M9JeUNGnHg75VpleS86KNPYxHWKl7UArjo_DRwvha-Ua0w9o_X52X4Ac1fv4lDekjSquJsJN4Gyq7AIQzb-nhwnz2sUyrvvQVIO5IZpvfp1YYiTS9rFeuvzj0LPU2V8yJKNoYe7A9NEjDh735iX7GEkpMUx3oWw4vRc6XVvZAXJrWV_aFWSH5zJhNs5qN_7kuhCSO-wq42QfGOL9yI4v60GVULyS7RJcYN56nrjL92R0iyq9KogUwwVu_rdDZ0ebBXovYo5MvEC_9SZHC6EZmJw-m78e1MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNlyGkg4vAe7bwGBb5yWLSXAba2jIFqywsPnbj2YBVbff_fsaSj94UKfpSFbgeUFBnpusWRcNiBD97r1hkKxl9m1rpWz4bOImNqoOwb_PhaR8RlP0dzixWx77LlA1u9x8gacbws3NDCTyS10yOoy_EjfkLNj8MhMiW0GMHdXnHoToMcfJcNJbUS50CNvZ3L-kb9zveZJkPVnRivSBbWVKDV3gCMzZbj9Wmeh9r9wcqipS6ufDzJdg1uv_u6neU1M63_UsH5ciidnfS3D7ZDcHaUkSze4K58IOnxEY4U8srG4h75RBTbjI1BxJSln1PFsbmM8GMJD2puKCbc7h8XISQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j4s-9wyAH4M-Wm9Mmj28HZdoHFxa-UTt52phuYVHIFQ2IqAGpEPqDO7KtW5ZPdLOC2rLCYuk2iGOS_Y9wQlnZcbgvmbIhjAIjNPUNPcyt7JLcgnYHzQZk6LGcQDfhmL13W5wZ6oZDD2f9VMCIo3evoHJDGNJLEJfDVaRHjfIXuG5tcO-RlSjmrP_-lj9U9GQ3AP9v31pa-zWQ3I2INDe0J58x4797LM4GB8T55hnFqED3tyWYPJjGRvzxHhr1pfXD15OdFv4bQWdIkacSD4449TqjOpuPfBsWm3-f-qyHQxaJpGFha8Vx_5Mn9hfqmAfvu0m4krmxipF5OABX5rJ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
