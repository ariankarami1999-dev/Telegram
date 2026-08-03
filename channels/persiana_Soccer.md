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
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 22:13:24</div>
<hr>

<div class="tg-post" id="msg-27070">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ULOflGez0cLn6l479rYSdmkvxbILjq5hepalA7e2oyu-GZRN0fVsjAPOw6GTAVk-Zvz2qGK1Nm-zYooNuz8YtYPRHGRBbTcGI5-3NwMEU10C2eSmd3HQyZcpjUMZQ9MpQ0qJqRjQz7vDLbg5Gwf9SmIyw51gyi-MaCNvKoH3ZAHQUEohgdDl-pkyQkq2S4CEko6wLnKqgxAshwGyS-ughU_d5AgqtVBjknJUmxNKknoHha0YIHA3_M7bR7aXFEIXBAm-gQAXeWcfjPo0bnCFHdqxfBHPrSWoZMFjqvQSKs0A8VMpljysY9ddijadc66m3MyJ6h6UHgHeXCLDavVKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فوری؛ دونالد ترامپ: این آخرین فرصت ایران برای امضای یک توافقنامه خوب است. امروز یا فردا می‌فهمید که چی میگذره. قراره به زودی و به یشکل دیگه، مذاکرات پیش بره. کار خییییلی پیچیده‌ای هم نیست. قراره فرداتنگه هرمز رو کامل باز کنیم. بعدش هم در مورد ظرفیت هسته‌ای…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/persiana_Soccer/27070" target="_blank">📅 22:07 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27069">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgkiSADV4r5i0-h_k2BeEdEYx_3G2U8i_rgSEMDBb46n_giqbVXpO9aolxivoKk9-kgpwZ1ZU8o0jMaMpa7tDuk3_Ni9UWPQErHhtQWmoLr-TCw4K7uQafO1bqh7WSSwrIVyxeo6BXL305v3BVNQZPTgElEL4ytZDpbjaEwPIpHjf_5GLr_6U_P9LEpuCOVgqmiEhdu9YmF20oS2qyHYy4tCzJWju38YjYt3SN43z_is32NiR7EYI4zqKsQCMfH3DjS6DYBy0c93QdotTp-ZlV8764xn8Z2b6NCYFUVjLoHKqyY_QlMTmAbAmFLjwTrGo4zKNsP5d1og_bndNRtgJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/persiana_Soccer/27069" target="_blank">📅 21:38 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27068">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/27068" target="_blank">📅 21:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27067">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/27067" target="_blank">📅 20:41 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27066">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KdjTfBxWekLRFgS_j_GgPnm5jEE4HkAW9smSQv5lQ38GhXgksMSk-PuGQQCvw443aUu8N7_-o67FO8t4ove3RHeK75_4SMW5nO5OBwNdvBl7s3jZ73crzTFzzKhvCu3NENOqrgE8iLyhJKNFRAzzgwP9IFpskN3w7KkErBwAlbpxbTy2OQDSxAXb1fOh8-ev_FKGv1kzpjgwtE5P6mw26iYRkGVGeP8bypNf2zKKyZCUBflxpdHATJqIgSQ1D7cCsnmAJHDiwuDy_l7vju9dJkMhwjldbDUDEaoirdP5o2cVi2Cdsb0hO5atIaFyDpGtSy4KY1uDLR-ezcWB5dYHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛
یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/27066" target="_blank">📅 20:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27065">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SzqoBdFhR1nvTkz6FGlVy-XW06oQjACZCbomLqV-pLr6mRG5Qbfuqt6rYpbroH7JUMBssg1Oc3Gok9KIWi4gwEI-EjPG4nOGzEmjyEvf1BWmt2kfIUg25fvDrMEHt5rL13Iv3YPgFE2xg4AHDkY1jEFSqu72zAXHN5jDUiEw-Bz1mq6S7JoakwRtUTmHVO3liJZe_-EoYf7AJrP6zDI0dFE7TeCUdIskxdQQbnl7SziKLLlHj0hkvhUYKu6hOwbomWnXOWYxrNsxFeBn_YSUKaESFHdRXlQLnANFl5M6FT6OanSxriOjK0RYMBnJV3VXcn8JzaOLzK_W-PCqp07vyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق‌اخباردریافتی‌پرشیانا؛بعداز عدم توافق با مدیران سپاهان و فولاد؛ امید عالیشاه عصر امروز با مدیران باشگاه ذوب اهن جلسه داشت و برای عقد قراردادی دو ساله با گاندوها به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27065" target="_blank">📅 20:19 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27064">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKxghC23ZObuItCvSCzs4vkoMocG8Spay0C0ZNAlvcLE5t8hsgheUg8va94i0AHOg24ImipSTIWIjJvV_b9FVSMXH7XjO_PUanXYR4qGzrlDhMMs9dM3f-xsfQR2FZZPVlttNXE1x0uNkRb7ucq0nJ-TZOpZVJeGBLp49mZmuHmtl4xWLVP7TWYFh-9CiSE0z9OdM5XNNh0ierYku54vrPdn8dzm7nmL4jSC-I_b36mGIqtcKs1v6gysnR3noo2uargzqWYqCFVcLKpmZ3B6H8XsgYUH6y6fmByTOeNbOCQjvMEm_yvyI_Ce5MKZ3JLlVwvNwwgfNaSzCMQ9S0bK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید خبر اختصاصی‌پرشیانا بعنوان اولین رسانه؛ اولیه هدیه ارزشمند سعادتی به زنوزی؛ هادی حبیبی نژاد ستاره فصل گذشته چادرملو با عقد قرار دادی 2 ساله‌رسما به باشگاه تراکتور تبریز پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/27064" target="_blank">📅 20:01 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27063">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXuPCW4nEb-4NpaHEtvJBYdtZYKqs8pic79XyaAnyMjY4FcbOVW6Pzc_1vZXacCB0YhVLZor6DDfOiibJSRxnBBxnNPJ7bXSsJkcJoASAGD4at8Y88abP6zPG_KAKPl56GtKDg2X9HfUxARrk3Hh4spg4qm9keq-rj_YJXBG1YjBdzjzST29mr-wWS1CjETl67qj1vx1QeTqzv8dNOd97Vnibt0QeHX3cSczeugDbsEu0SHF7-OBK9ZYpn_yehXWiVPWMkhcenAukia8tsILFYC6kw3Xq_9q4vUewszoJvYIMNpI9k41VfoLzBSalueesxn6CMXspS98yjNoNX2Iyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/27063" target="_blank">📅 19:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27062">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/27062" target="_blank">📅 19:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27061">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llYPRa680KfGxKTOGeUyUHSw7Mj2HQUCrsHzQNTSzfS9UEhx08iNoWbRzxHG6uuC1PUvNIYFO-T8r2c_8vxWR1x_pAdy-b9aQJ1YZbz7q1ahw2TL305DntkrJj8X7p_tzKm-GOIxzpTS-gICXqj6Onq87ALcGVj7uFOjBi7smgEb9SQGEqaI9QC0nZhETvvnkVucRzfDtK4BH4P4im7RuqJiiT8bJS3bsvLlWrYaD9vncb7wqP8V6uYwZhRaAAepxSyi8q5OJ5g_YMPLhYuC3QOi1eTCerToDyBLTRG1GCfGzF2NdLAeZ4jpjqgqTf_5Qjltfv4oUvhvjH1GQ11AYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/27061" target="_blank">📅 18:53 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27060">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8SZOmAKJ8reiHHB1Fnj_oFG94lK69nQ5-XHdIp3BnKquIVMkk_89LhFrKal-kIVBsgTyouBDwxMDRY_0STa53z9tlGvW9I8Wv5Icd9fCVraLHcYJibegT3UfG2KYbvNouDQkQNU5lk_Y8NrkJi6zU4ajvPOn6dy-KhfCjGxckwKtpt_QEP2SRR7SHWxDGWoRooXQyv3_-Kd-b_R8l0OGko8TtKlLUu_D0an-u1eGv7el14s31JyPr6oT_10cTT2fix3Xlr6PWhhjPKkcEvZwuo47VxUDrb4vGqyq_WuU9LXTjIhWlnMOj2APnPjCenMyV4wI1PASxCVXSyCWr3N-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
#تکمیلی؛ نگاهی به کارنامه لیونل مسی در دوران حضورش در پاری سن ژرمن در تمام رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/27060" target="_blank">📅 18:22 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27059">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tpRzg9UuHqgChj74rFw0Wr-BO8nXO1tf9L-CCJjJfaDmv1mezDWerBmglSK7Pc5kDt3Utl0FkjOM_GX4EWCIPNmqUM0i-DSWdQ2O2wPeI1QSRrv-9tdfNcLcE0ERkZQb-W4Y4I72Mc_WMcUdfkUTJim_UojmvfLxOvAQtZBUUVANqIYqqojw4DQ807ccN8mLe5RfEURkoRyXaiIh5aDqi9cFLDaIsSBj2Tz2grMOqOmAO_nrZKszFANtzR-uYqGi-eKaDNBZELxpb6G2btesTyVCpC12TB4X7u6e6kQctdspuB0Jrs43qPGr06a4N-t6VvN8pYAMdi5dkN2vsozrlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛بااعلام‌فیفا؛ دیدیه‌اندونگ هیچ مشکلی برای عقد قرار داد با تیم استقلال ندارد و این بازیکن بزودی قراردادش رو با آبی‌ها تمدید خواهد کرد و از هفته اول رقابت‌ها در خدمت این تیم خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/27059" target="_blank">📅 17:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HVZ4KXjDj5Ta9lYTFMqxU2Z2i3Zoiehz8UTAU84p7g9MX0V-bfXFo1RC0iXyuVLDhqOUjHjDK8PEt0bzQbvU_Axe4SfLWCWjtu8PiXK25sQ3Bqjg8i8xYLBWR-B5cr2bfFCHlYIrt_p_1AA52thswSUUg9qsvFZp2yaFqsK8743i_iNrkBJOrz1D6d8DfX89ZWwKthoNK2O0E8alvx3_nt5wLoamKbzHVwJ2jTj54HMAQD_OuPDCLnUbTATye9u1R5L4xhtbLZ-3DTziaGBWQntyFQkU1OEPBD4EuccqebyM3b9IktMm3Dn01mjUmuiTPHU5WOpyUENATB3h5Ec2UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
هانده ارچل: من از بین تیم های اروپایی طرفدار منچستریونایتد هستم. علاقه من به یونایتد به زمانی برمیگرده که کریس رونالدو در آن حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/27058" target="_blank">📅 17:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qL-EspvObJ7TgWr_5fZqz_3U30FLFzBSpMvsG1XMl8J8c8ndW5jMYZEUOzYeyastXSi3h8s_P_yKe1z06D539PZ2DspW-ySxP4_ldakLEQTpGkj473J3JRUxxlVujwfe1dto4NdtOkA1wuPTEEpsRM3KmuVgFY2cPBASCHu9wolDLahYRkqIJesP548NUvfxUx8r9tbxV0iS-I4hH3h5YnZ4EZtJ5htUTP41yASUDCaR0sLFFahfS2yOeeOXbV4apSMEgUI3nLw6WTTOmZm6auTK2RsTxx-fOa345WpdTetZZofOFEh5Ej_YhGzFmeYOakg5lEb1hiUx5HQoICXKsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
نام مهدی طارمی کاپیتان تیم ملی از لیست اروپایی المپیاکوس یونان خارج شد تا این بازیکن در آستانه جدایی از این تیم یونانی قرار گرفته باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/27057" target="_blank">📅 16:36 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHHLNcpJAdnY1HyHidUF19JyoXvNe3Vy2tjxEr52OZfWc2JvCMhDLAIA1c3nyIUk3eudFi5SBsytXpB0I5kLbCuSCYsig6w6l4vuQfMKiVpMLD6iB-tun7vq0nuqk8ScLOT0ZpY7ZLJTw4apRn8-oR4hAGGij5Vmc1frS2gUpcd4hlMFtZktCRHMw3hlu6ga-KdyoTAMMxCJDH_OxVj8sNMk-PN-dafE5i9TZc6vMms6ndxW8zxC4tI9q0RPLb9Qxhf9FQYvQ9FLYZv4X2W3HPips5vZUelJVqZ1RmcjeBRIHFBBBPFHG94nlwSDalOnZK4wpmL-VaDpagR1W82b2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27056" target="_blank">📅 16:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKg2UDVdGVF5vQRMhutRBGCFPdMBK0mhKIY6PXVp9rk-dD0sSQfx_MdUbzX8QYZ2s87omyDIDdkdXlbeQFTc2qMMEXEsdR741jg8YGqZDT2dVyKZJQWepi6fbW3VZLZk0eXsKwM7Ldw5F4bfyZglkqU4-cDQ7gguiN0IAtb7Hd4q3_xz-XtZ69tPvkLNqhjIz38xBGxFSBV7QFSWbasEuruMyrvpGHo1slqjcvSBy2JDoUuzLyJAidLxaNe_mAdqy8AzRMGWPICAXhcDJtXRWtsC4rlQLdngljzF8fIDRiJjChyyvkuGDJcNzhFnBCWjFhagox2CwUfWMN3csMQe5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔴
یکی‌ازمسئولان‌باشگاه‌ملوان‌انزلی در گفتگو با پرشیانا مذاکرات و توافق باباشگاه پرسپولیس بر سر انتقال فرهان جعفری به این تیم رو تایید کرد و گفت تنها مانع این انتقال مدت باقی مانده خدمت سربازی اوست. درصورتی که فرهان جعفری بتواند کسری از خدمت بگیرد این انتقال…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/27055" target="_blank">📅 15:54 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27054">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/27054" target="_blank">📅 15:40 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqjreoQOb16SkBrFmFPGc2SxKtkUVQO_ovP8ahDBgqntui4BiGqL2C3KYWaojls9LJkMRULY8rquNAAfQYkZzKPhzFAXAwXrQ5Mz_d2ngbs0W8JvObZ1Livq8ta4_kw0oq-20YDLqLiDx6BcD2w6qQKspX0Pxx7lc1dDUA1q5wF-npOJYbLgGJs3fx19ZyOPd-xf0hUjatPmsjub__gCcbutnkBT3Y8a9o378-HgD7RIbhwah_W_7pQbXRk0gxQdhOpSPaG4Eo6ysymIDAPumgfKrpwOlTaENRNU8f9vFVE5Mqefh_UQxMq80QTkbPMORZWia827BwyAUnhByDv12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27053" target="_blank">📅 14:56 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27052">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idvg1-Z1zyyTKWOOEtZrU895NWbVAKmjnHsIWGTV3lmTdtM1IqKe9X8IuHDuD1Qw8KgO_TYfQy2eTOFTTgdHrDJvV0EXILzVZzm_8miwe6SDkl_4Vq73SbwKSl2mAdMG7VsDdt2FxuMQ9WaWJj6CK_HG6vK78Mq7GJy2lyboujunDd84DTKnNdyZcgNVzMfSFwMyhucCBmEr6PG076oP2UU9M7HWPlJlvyee-ah0PtN3hRfR0VIX3I4nIid-QzLV0CLc1k0yD2D44HQXqHIgXCcSwdF2vvCbDFlOjsUTEeCf6YtrKmHfYObHauCtzg_k9cRj754a1piBOFoZ0-eTPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
احمد گوهری دروازه‌بان‌سابق‌پرسپولیس‌با باشگاه صنعت نفت آبادان به توافق نهایی رسیده و بزودی با عقد قراردادی یک ساله راهی این تیم میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27052" target="_blank">📅 14:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27051">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kEfJtMeQ9exu3v3cTZvdplbvxWZg6udvmLsbPp2-Zt8XJIRDd-0hic3M_M_WxrfJE3xUefXvdoFeWVmOUhLzsvbUjykJlcbvFkNUCC4RyECvtvm7mjQYhMho-g6HtuY75KLnzAtccbnYI-5nNWkFbZE-_1nJHQeJxeOqrZ7zop39VWdFt8m1tEjyoprlpUYUd8PJDaLw1b-fUjT_ug0eTEgB3-xUCWyPlURyDSowMAcNOfs35r7U38Ysazrak_gbEYezDUPECdWpQiQ0ffvtlYNOACW-ARv31uvOcDePnvnPZkIhs5bFvZ5M6gGuSlq1cxNJqHQVLjNVm4AvFwbYIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/27051" target="_blank">📅 14:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27050">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQOvin7quw4uH60SkxivND_6RdKd3_gOzhXcHN9aioeBU_jH2qvUyvZRC_SJZefI3ujUrqupiUyorVhGhYsz774NUGi5-EhGWobELC9ihGgtQOrR75ywdv1HhQv67eVAPknw0FkinRRqYebE5-z5VkfH5Y0NbMo4LfO7TE7-lAy7lHS2zSI-hNLa-wuwz6uyZPZb4GCB890SeQmhMttuOopaVMmIOwVAK4FMUt-86lDJFCaSy2w4cUSYBbAxnT4qIqKree5ETSap3t3-syQlWPmpIKcTfcNcn1XvI6j26JrpYsxrhTgVhPUuYpJ_PpvQq_rd5XS6Rkje0n1H-UGpAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ جلسه پیمان حدادی با مدیریت فولاد خوزستان به صورت ویدیو کال و حوالی ظهر برگزار خواهد شد. حدادی امشب به تارتار قول داده تا پایان هفته پرونده‌نقل‌وانتقالات‌رو با جذب 3 بازیکن ببندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/27050" target="_blank">📅 13:29 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27049">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27049" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27048">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t37qk-tqgP693Q7NV3kUjUoOEyhgbbzJmnqzu24jbixdCWf0WyJqIsHCSItySi2_rg04RBoC5qKFWGrh2yOqri3_PcOuSqBERTyyjnUZ1lu6QWhVO1ATpDdRoXAtT0sGcVsYBcS725v3F-Ngy03mkgCD6WCszqeanNffHlX-gD7r9NFlPQZFSOxOVPn2rI029Z6Yfi0mkT1VSfrmVsii0Ml0tCjOIor_jPCEPZlvxUyMQtz-dHMeWRMmpVaVNwjSaXvHyYFjndz5Oh_B9_npF36xLTyeUezk2JnUUnUsAxOYBLk8L6IlvxE_aX_oWRCPiZ29WmZd30qxs7vOK3Pqdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
باارزش‌ترین بازیکنان بر اساس سال تولد از سال 1985 تا سال 2008 با نظر سایت ترنسفرمارکت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27048" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27047">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27047" target="_blank">📅 13:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27046">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQ5s12losXlH-ETyj2GoEj64rTWD0sQ2FtkMu53IVrTNXsKaBPBnBtEbQ6Hev4kIEV5GuTADMcnHU8H2NfMOs_P1DQM0rt9GdKSyLf1EA-5IeOtWjvZ8lIMG2uFr8n2hpGJXNNwTg2gusmJF7pM3EVSyrrGOhpWHwKWMRRmBOsuwjPx0Doj8-lSZ4Fz_R4iRwZk6YSTnYlCEpdImrZ-BWYYPp9UZD8hWmWe0xrUaglBxLIYoJ0sxJW1m3wTcElU9hedplZo3FICBH4_zURxpYdqpsl-M7FQZjUF9oLgQuwOIAA6mye6jHKoFVSj5O3KuzSSJwOO1zmoex5TPVy0WYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛دیدیه اندونگ بزودی با حضور درساختمان باشگاه استقلال قرار داد جدید خود را به‌مدت دوفصل امضا خواهد کرد. تمام توافقات لازم بین اندونگ و باشگاه انجام شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27046" target="_blank">📅 12:52 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27045">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dTi4ky-eEJN-FWprxBMatN7mijtirC4LBjo8mUZbQHnSMyWxFIGAyMjf5RFIojlp-e0mN_Pp2pIdKjTrWZyFXHwxVT9WpYamTXLTRdA8o7g2Y67-dnoBRL_VsFwPBLWbdcpIlNEbX9gcveNATHGndGcg8Mjde02whlMFL2S8CvDVUrKZaCuafWWYaYKvnQaZPPtnp22mrFaMK83iBtc8vIDb42cZX5gndKhWKfGLtHe_-rLkc2OKEm51MAAkUOePhK_QaMW1DvlrATX2CaUV51F4zZ-wzFH2PHjZB2whLXmNZVfzidYXyY5s3hIB0DHDqyQMBMwgiLsU9fY4f8xBvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ فسخ قرارداد یاسر آسانی با باشگاه استقلال در فیفا و سازمان لیگ ثبت نشده است و درواقع‌فسخ او یک‌نوتیس ساده به باشگاه استقلال بوده و با بازگشت‌ او به‌جمع‌آبی‌ها او هیییچ مشکلی برای همراهی تیمش از ابتدای شروع فصل جدید رقابت های لیگ برتر…</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27045" target="_blank">📅 12:39 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27044">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27044" target="_blank">📅 12:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27043">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-VH2baEseos4w0Q_nyLH33gaRPyocmxol6clW4ALGmnBOBWzlg5cFCVMwfOM7jzi_DSl2zLvG-tJZGx9agroI0im2XHdteYdSS8KAKOq2P98V5D0R_Y29xkTrN5UJFFSLsMRy-adoS5Yf67bpzdeFCCqHwjMjLGbQ9ooaWOKQpFPrF36-AF2AMd3URHTTWo3h2lDO_RsGALeU6Cgr2vdhhLQpqKxErsbeWLEPyb54Slno50jzn9ephB5iJL3gq96bOIiRJ2C3miX1zxSNtEJtnovPP8U7ko9ro4UECywEJQ_9leNCLFpP06ILiSiTyving9zi7hDvGAE4_TaDLU8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ویدیویی‌از تکنیک ناب‌وفوق‌العاده تماشایی نیمار جونیور در دوران حضورش در بارسلونا؛ حیف صد و حیف که به اون چیزی که لایقش بود نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/27043" target="_blank">📅 12:04 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27042">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwQ5OBpHPx7pYSYauVAm7SyyqcrQR12S2FVk5UJdljRJf_FXb1HJ-eWYoFt0WYq8at7aHmbXIfRxEAeVRNnX3ApExP4DPeTME4a1wjTDDLMtX9UMvgUM32h91haDItmwx_TU6vdAaEaM1vdHzehCTQKXdOc8_DlzGpOQdJhi6KpR6NPnv8qqoSqUQ78fL5r3mz0V-sTL7B5KqeZp34q4fCeCeQTfW16zyAnwz6bLetL9lti61WwNmyBKgVJKQlBGLM1WDgC_d3_LrLZKzie4s8Fj5_VOpPJ7cdGatelnJ-VMrf2bMkFbeldbNK18dAs5UPAAymJN-BBGbS_zS4nJBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟢
💰
#تکمیلی؛ بعداز موافقت مهدی گودرزی با درخواست سیدمهدی رحمتی برای پیوستن به گل گهر سیرجان؛ مدیریت این باشگاه 80 میلیارد تومان بابت رضایت نامه گودرزی به تیم خیبر خرم آباد پرداخت خواهد کرد و بزودی این انتقال رسمی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27042" target="_blank">📅 11:15 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27041">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahm5JMMp_dTaKJXmsYQKDa3V1NSPh5fMwRWKM8X0j24b7BITpoXbDwfW9Cjg8klCVv-OrbzZ2QFkRPQL6HY2u-k0AJusCaZcr0LXmkWeJmXRb3UzNyRAvqoxvc-nY0zJDJ4MNJvZ2NeMUrkEUsBmEGfSNXMTsul-XsHuvqvswXHV6vtfkXOjSx6y88s0ojkB_ktzKhI218bVhi6jZ4bFcwK3035afobNggWo-HKIyvamsxr_Mfan0u3rhAhJIp4uJ2ANql1Av7eVlNwYtT4zNRe5mqtj15XRa4gk6F_r17csQCZsJnH_A1u1gV9SOOaksA1Bem9uG4bYm4XYDFiFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهارت‌هایی که توی ۲۰۲۶ درآمدشون میترکونه!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27041" target="_blank">📅 11:02 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27040">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OWKlj2Q2SNYbehEmjcLUYnrHSgprVuOM1pt2IRf4FXPYFXjZLrIWfJgRAAEVuumICY5DEfo-IPQbsjR_nnj5WME0DR82N-lCdk8i2yjx4LKdzJMcyGFeVJNUP4cH4yyYb5RwLoa3IkqUTbnCtKaEJW3MrS4mshSfN1a-ivd06Un4BSlSTFVkJZHsNFmpc_1dwRB0821ApZCtBi4RBwm92PXyDaI6M9ZEAlLgBF9v0-Quoyk2ePItr5TPYKLysaJ116qPyVGh8qYKsKfx0RVKwZrPWxVpg7kAnDyL-NieIqJjKkjKnoRxeakHKPwVzVy_37XbjSnMR9QNFXCi4w4TLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
عملکرد فوق العاده لیونل مسی فوق ستاره آرژانتینی‌فوتبال‌جهان در دوران‌حضورش درتیم پاری سن ژرمن: 75 مسابقه، 32 گل زده، 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/27040" target="_blank">📅 10:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27039">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-rNqPJcouuWsOqSu3e1kTCiWohimJkl7w-0gfnFMujmv76MM0DiSewLNNaGke8riyFSzGbKlotNlkMKZmJAENGvFVQJ1n9u86FNiH8wPrGDDvP-BLcBveNIGRAHoby7zuA6-eyh3PZ5x1-FvoRujEPruipAQXPpC0z71gDJ4MFE-dX7bB9TnR3nVPURkGGOxdPomZh9OhqKSPQTfelD0p_RbXgEatHyQyYpxJL-CW-uucHpzai7DjkAwVFurcUDKljw4tAG0zVOZXvWzj5rdbxEakzCWdYfZL0B51aZ8zHGQAjpEXZLPMb4J47aGnXH5o4tynconpXv9HbydB-lew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27039" target="_blank">📅 10:34 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27037">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5EGC-36J6cPMSMH7yz2DedDrR66rKHzDq_NIhRGQl3069m7S5m7N5oe8zhYyYIsh2WeOC6fxr2rTPIgb9eXOCyUz6NK08Ss1JSmJGGqvV2Pa7yJBYEK5SrCu-GgrPerXnCTuHAkahjVKqvTqA6ab4sw6nWeWAAb10GIoqGmeKigVbJVFTuhGWSu36uzQ1qRQT21cB6NcggLe-kr9bUqHzUhcEaJ-amYE4NKKUXhxlkNznNCBg7V4UkZbaN2oeHHfQh-IGR1WuMtPQBfNfQg4qfbhvVIPFRhJsckTTtcf1wxGoapYjCzblpUy4QBSii79PWDY3WtgZy_YU6MJtCTMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هانده ارچل بازیگر معروف ترکیه‌ای که گفته درفصل‌جدید رقابت‌ها طرفدار منچستریونایتده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27037" target="_blank">📅 10:21 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27036">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFA6-I_HHcCFGVn-0kd_wF7_vF2E-YPA_HSp3eLBF1roahFI3Cc_F4oz_6AGf5iuHMRi6hi2073fxYEm04BSBGyp1NrjSbqFA_gVrllktv5VLHUWm20XQEj4HSJsjD8o2xyXKJTVFF464A-BljBBn2zS48VO4KDtQfYax62RFxdZ2HVBbqmGdagzwaN1XeXpfYTljGUKNM1lWtNS5LvB_Is-dq6NjwGXq0BDRVUkoyCJcfyyjgjMG54YRxHq7O32ZmQyQ0SnVHuwizAT-B3o-UwvtZr2NN3E_fOK6BxNCh7I3MmZHVOxIU6Ah0q3ZveJKD6vAuH4y1phExXFZ7g4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27036" target="_blank">📅 09:51 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27035">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PvkvtPvLbNxXMvPqOx3nCzzCxgX7xfKnfpdw1sAQGcgX8GNArXh-UU6m-5cfGHL8V5tOzJexwEyqqbUjqFa0F1aTriJ4tINWaa_iXef2LFuU0lxM_R_Uk2VbtMdunPIzNgD_RL2FRrU73vHM0jm1T-dPBiEcs6HGnjjThkwwuvdVFmitSSzqN934nH9gTCihhlAzXVg7SblL-Om3O1P-8m7BwR2vKeBTlsk0aLe3Y4bt2fsVXvf7QcjCcTTd6VghnVFi5nGlVGRrpPE45qPg8iPdIuCccUs5Sm2Sj6BE5nB7O8a3WFeDfLS_yEJVCs8xJi2cQfzRbEUe7h2gmx1JpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27035" target="_blank">📅 09:46 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27034">
<div class="tg-post-header">📌 پیام #65</div>
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
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27034" target="_blank">📅 09:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27033">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27033" target="_blank">📅 09:16 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27032">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huvTI1lTJ5T0fa5iHuckWZP5AJEIR2hSOPVg1RjkgFJbvG5QxYJO-NokWhKRjtrClIG4YYNiINFVlGofcWDyI75_hJvqfjKTG8yFq3SVt6E70U858U0Xk1LA1n2y8UjZwQIW7W5kRxyMW41LHEC2hfIwNHVwAUHQtvxPpO2r0_gapbEu2u-mLqN2ciU0bsxBCHUEx51F0BGxQWwe1fE6k0HU6FbZfMYGX2ieAk69ZOJDaVzKef6ZgBaPOUF5C7_P2bJq-6hZF8zgqBrFExsTPnLRjWewFlgyUm3RXvgcZESjmLdr1110ZEd9Ee-qb8gjHZnnoZaA1oLM5uj04b0Flg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
درخشش‌ادامه‌دار سوارز در میامی و شکست عجیب شاگردان ایرائولا مقابل لیدز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27032" target="_blank">📅 02:03 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27031">
<div class="tg-post-header">📌 پیام #62</div>
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
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27031" target="_blank">📅 01:24 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27030">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODVKBsvp33LVPzlWNvBejbR28J0kJvnIb8nfSCVfLG8t4f3NgIb220AQ2zEE6N3JeUfS9jlv469b-ZUemeHA2-L1aGA78SjxxlAnfJInAoRrwruJkVwLzWMZEhJE796jYjHMWAZJIIeqIVqId47i89N94u9xX0cOVXalckTg2qqiQOSzR9qlOq5bTiq9AeGeOlYTt26aX8rCWcK2hIg7arpCi00L9MspHiOZwnWg1TqwVYXdMukK_CVfRa_RoKF7IsjAohPhzghyY03lAfWq7dwLPpGmL2y7k_iSMbo1pJCxmINRK9zgZam4485xVWmNAUJ5wZ_wXYM_G0-lwEzVdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
آمادگی فوق‌العاده لوئیز سوارز در 39 سالگی؛ تو بازی بامدادامروز اینترمیامی‌این‌گل خوشگل رو بثمر رسوند. کاسمیرو هم‌که‌گفته‌بود اومدن‌اینترمیامی که به مسی برای بردن جام‌های بیشتر کمک کنم تو اولین بازی اش برای این تیم در دقیقه 34 گل بخودی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27030" target="_blank">📅 01:09 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27029">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMXV3VYGb73K0vFtmL5Pf57-jq0226FVbi76ZNbTMaWQlcWkIDYzixccL_rdZw6NU350YjmWNUg-xA6Q0Vle2f5X5JTRRYmhKYDsfIgCvVylemSA9OnhYSxHkWLBvqnEGnlanVjkc9HH7k7wCAGG2CzH5i_idOpExpon9Sv5lJ--HzhqMslkkARaIgLqKtOrKbzDizAw6bFNw0tnLLYwp5oQODygrL_sxXmM11tA0eb0aRs6I9wkbbObl52auCWGsJ1m2xQdRA8j9saRNLARdB8UCf6NeaPwUdwlERgtoYuwaR1V3YXWUo7qmUTDdAUTszH9FBAQCXGZIS0nPbqX7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/27029" target="_blank">📅 00:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27028">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJo9enwt4zy58rIfDVqfnXv3kl7voNMgPrEsI2ERojZtXbn3__8m3DSrF4UOpYszAh3yBo1goNI0Uq1xZXD8md_5vwzitfS6b-Mvt2ljkIR7_ecJV0NuWGRHot9DtBTKyzmFI5ADPswA6LaydP-4m1B9QJFQjh4Hw5nJrnpcqHTEfYbXBHudv9jvALFKWMq_IcPXQ3p5oqdgQcHMgkLX3sLs3drSes4dqI8lBG_gNHGOdZC4vMFuL-YrnYZW2Y9iTaVGFJ7Oo-rgl15YqDnDD2Rz8d3tfZ_DHXwLGQYYxVxVelVVaTb2_lJo6R5Gf3noUuD-a76IaK1wHCpLcRYE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27028" target="_blank">📅 00:26 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27026">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0AKEHVxaRhZK1UUZdxNVs9PBb5MRaz-cujCXOlLZ4c_PttON8vJHaZ0nwyaUyan4rAe7eEg7L4nopTAAqrpEnbGzIhtPHgZK2h8bTykdurj6j-Yz0HyGLJHTYfCGQBUR68aESYpYhpQtDFGDVkfOw7aCga-qKRW19QXpv5Ut-DULw2c-Qux6vFcj1zMD9CvFN50DNwj1Id5TAtD8RkMVp2bn_XGaDo3b4lMxbKvixP2v1gfRu-SZQpRALdf7OISaLWEZTPAoBW4S5UxTjHbHyPpMbqPPxSzngnrfG3Kqss7qc1gybwZ2a_6xeku9nsmDpPkYhZ1FsEv2tGGu8mJ2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
شروع‌رویایی‌پرسپولیس‌ِ تارتار در پیش فصل؛ پنج مسابقه، پنج‌پیروزی، پنج کلین‌شیت؛ امروز هم باشش گل تیم ترکیه‌ای ارزروم رو شکست دادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27026" target="_blank">📅 00:00 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27025">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mes7OGWkTAMIN169w8KBJG_sh4houu5KyWO7pexV3zsVnD25Dhtm_IotW8iiNWpBT-4ci8TUT0x1g-mrrjC__v9fmFdmesykSow9GL3X3xlXXjZWLmip43UUJBN8MjHplBVJ-TfKTIkUF8QU5GRNWaGLOk6v6X_cGymsngeBkWgeFhtnD-Io7dmWt-QhwYqcEa4B0pERhR6JlT00tu4c5vmDmZ7kRcMJ0lJWEBO3Ow6O3dCxDHkXmk7iOvMunjuQQFFKdpQ34GNsXLL3vtzZaxcNwiezEfcvx4VGIojzfFYcuHRwU8FUalyJuFC1i0y9Mj-G-HSqZfdwjZQTjnYz-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
الهلال برای جذب رایان، استعداد ۱۹ ساله برزیلی باشگاه بورنموث و تیم‌ملی‌برزیل آماده آغاز مذاکرات شده و این انتقال را بعنوان جانشین احتمالی مالکوم دنبال‌میکند. رایان جوان یکی‌از استعدادهای آینده‌دار فوتبال برزیل به شمار میرود و درسال ۲۰۲۶ باانتقالی به ارزش ۳۵ میلیون یورو راهی تیم بورنموث شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27025" target="_blank">📅 23:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27024">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrNzNh6bV3tJJcOW60H0j7U9q01LECRyOK85_LUZ1WU8MLoOCotjh1GKdtMu3MQaA2zzWTm9IUkiFHtPblVy-XbdLH6mJTGjSYy_69HDkKVtMSuOdulPw0N_s7v-BMaNeak9AxQ68UB9Lqeh4ZvIgHF0FG3BwzFFHmBZ5JHWOKUNTEuwCl9SBCue9vkw8yLsgEXKTETkuuYSCEIwyEc-i8_t-zt8tlj-phr8wDv0v2nE8ZD7rq5X2uqEt-PP0EBuYncR20XtuF5wvHSmrLIfwWbiSFQ-ng9TfvCbqUQX56QJLkVdgXiV8BDnCStPvn-r98N4Dq81b7_FsS3RQc8jIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛ پیمان‌حدادی‌مدیرعامل‌پرسپولیس فردا بامدیریت باشگاه فولاد خوزستان جلسه خواهد داشت تا آخرین تلاش‌های خود را برای متقاعد کردن فولادی‌ها برای‌فروش ابوالفضل رزاق پور ستاره چپ پای این تیم به کار ببرد. گزینه دوم امیر جعفریه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27024" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27023">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGo9NwkkDziBUxWOOigOqedvpCTetYt1SPhSLAi7Sy1d_OtDEOB-_xLA6OFmq-aufafP6ig8wfIcGzKC5SqKU8M6DH0Xm_yIAdPK2mhIjMuDv_q5e4TeXD5gUXhkQDFrwzosk5tmhxfvBOyjmny0iqMmTpQUi4pybpkWT5LWDnYsxtJHrG5Uy-nQ0NurlY3tnQOlDIG8J5y8QkCLZk3k4mLaBefhw7gKpDBLA97lNABzhcuwYOBe0YYP6xB7lv5ztVdrpsw4Bukc4c_b23BsX3FYmPXqV2VNmcK6gZgdX4gjvbaTGQMFyvHmEQKMYgporijzk6X7xfOSHl32Ni4WPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ حمید مطهری به مدیریت باشگاه فولاد خوزستان اعلام با هییچ رقمی ابوالفضل رزاق پور رو به پرسپولیس نخواهد داد. مدیریت فولاد به پرسپولیسی‌هااعلام‌کرده بود اگه‌مطهری اوکی بدهد این‌بازیکن رو با دریافت 80 میلیارد بهتون میدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27023" target="_blank">📅 22:53 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27022">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMMKvOvdjzx80lvPNdW8CVDcDMz1ELu288W9WSclaAoTxdWoVe6H-sMn_FU77sjpGJVPmjeFffflNY1dno2gWSGYVedX5L-qKke_d7x6_Yii0JbH2sVIplGomTBR2iibL8NCb7oNEzfkMLUmDN6RQEJQl0sz0neWy2utXW_yga5tpR_6zotFanGoKTFBR2F1XSZBCjMFw8rkcF9KW6o-Aqw_yBakY6zBgtxp_eNbv465tkX3T2S9G8Q1LmFaZ2zOErVNSCm6DolBTIy_Y9MnkEKh3f2Oze9cc0SnuIu-sXlQV3EpnN6hvVQxto2labNI7wtNlGBje67Zap1p6TlNNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دادگاه‌عالی‌ورزش "CAS" روز سه‌شنبه پیش رورای نهایی‌خود را درخصوص‌پنجره نقل و انتقالاتی باشگاه استقلال خواهد داد. اگر رای مثبت باشد فیفا پنجره رو بازمیکنه. اگرهم رای منفی باشد این پنجره نیزبسته خواهد ماند و با شروع نقل و انتقالات نیم فصل پنجره آبی‌ها توسط…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/27022" target="_blank">📅 22:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27021">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeW-Un5NLT8YjVcH6CByz_AaIJmsvaw31-7b8nK2I7L_C4Nlpo7Sx2cg7clkM-o1rqPAn0EzioEQHF0kja-mWmUljuRa2oyE63sGnjtaneqgQo3uGlFFK6BDN9uYeOk4Hv1XHFNoxndTx7YWJzcZhAJHbEJI4vnTjipMIxuS2jdYlTjc7OC9IJnqZ85uBH9fu-21gm5JTiXWycQsW0kY7AxNwV0I51H9AVjrFl_vsn84In79iRjkXxnRtxsk2j08iEeiwhettN1l4XMVqN3QCsY7kciI53RctF9qLSUecxeIPQ0X0eEXu1ZrefBFISJybqFmd9X-Xcs3gbJ-J-Zqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
این‌روزهااینستاگرام رو باز میکنی، همه نفری یدونه‌مجلس‌عروسی‌واسه‌رونالدو و جورجینا گرفتن؛ ولی این یکی واقعا تمیز و زیبا بود. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27021" target="_blank">📅 22:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27020">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umeNvsoJHst8N0pwYWwn9lLUlKTuCKMojyEhiyTOZ13D31Zj93IUagKwpgJkquIDYaV7i5o72dlZVyCui3SvNAVy9n40yX_Cam7n4mbestK2L-33wKL-t0fsOllutoncGQAwbEWLZp02LUa7xJOcXZiUQI8GmouiLx9wvd0P1aU0tKqRmni5q1Lt2TugFwnTPfgd0FAljxfxU4xcKK3NyRzr2kptIn7gD-j46tHx-alrXQtZouKu5G3etu8SXoPQBf7LOMnlBW6fEQMcVY_gTZGSF1JxQxR04pcUiVB_tUf1AV4eWTx6DeLuAFKQXgovo1Dq1-k0mtqrSpcdYY9rhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27020" target="_blank">📅 21:42 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27019">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/persiana_Soccer/27019" target="_blank">📅 21:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27018">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtiNPW2BsPx8Ui5i9sgJdrNBYe72h1fKcjH7Ldlv8sNrmyWUc-k_v1Y-VAWN_TJ_RFypo1qECU3FVA3dlzT_8Q5r-redj9cPH4KvwZt9yl6C0pzwcpX6qYDJqWlqRa4GfT-e54TicILc7JtOb9mrEtShN3ErVKbkDjiYncMg4lPSUBeFeX5QIiouVocUsLDCHSwVkW88OXYbTQpUGpffXsPUukW_ChZNO1vt2jPNaDCBukcPpsYXN_90lv1ivDnv241NKnyIkjUml2dtvhKPiU4IgtAxP1WEC7RKbdaHnNhko8pN3StXXM4oW6cFTkcXhwVcoJtGnZJ7C4dA3oDYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه گل گهرسیرجان‌رقم‌رضایت‌نامه امیرجعفری مدافع چپ 24ساله‌این‌باشگاه رو 70 میلیارد تومان اعلام کرده است. مهدی تارتار بشدت دنبال جذب این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/27018" target="_blank">📅 20:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HmCzvxFWuT2EqrN467NnXwxy7Bt1TG9PUdWt96SJkV4mGXTXao4fBWF-2gSJk-eQZQBk0SsRNkQQ38Bwb-Pe6Pp20KwozdSGXFUpjSFKV4pc4OSNrOF2KJP8VQLXKPokse5V5gsxeareun4bEZhsN-oyXNPNHKLPx8LiYvFlyS9snk-TeF2uKxu4gGDl0S9zkas5bK4qsEa_jtUp1CmJGris3L7wNpBFNtU2vfIBAkJdFB7XUftc3OGYn8WrxQnh0T2INHfb5w7nf6HyRBGtt511H84Krf-IhxK6NmsO_8iyCvifdiNR3-flgPuIs7dqNS6XyRiep5b94LUZOLqaMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق صحبتی که با یکی از نزدیکان محمد جواد حسین‌نژاد داشتیم این‌بازیکن‌هم‌آمادگی خود را برای بازگشت به لیگ برتر اعلام کرده و به احتمال فراوان راهی یکی از دوتیم پرسپولیس یا استقلال میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27016" target="_blank">📅 20:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aY-mCYHiPHl1CpWafyQk0CBFtCrfoM4Ah7gm7ethH9yvhG9ottQa5sIKLK11uYsydBPSgrKicOh67pNyIed04iy36qqm2jKHFClCg00jQDcsoDu0Df-2qm8PNCsRkKXcwRcY6_fXMqoJc9t7cm9YgIlIj1eaS8yrsh0YnrREX7mvRatBwB0fA39ei0VWDTep2Dnn5V5dYy07x2y0l_F98I1t5As2_Jin0JvK-lNLXw-Qn-9StM7xGSQTq2fwktj5s_2_1MEer_F4TvXo5ZewPmUCcQ2jyRkSYME0zg195VCkFjSsCeMWWE9GQ2tmbAgTiXAMzwuVQSUihy9FWLCyew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو درحال‌آماده‌سازی مراسم ازدواج با جورجینا رودریگز برای هفته آینده در مادیرا است. این‌دونفر در کلیسای جامع فونچال رسما ازدواج خواهند کرد و سپس جشن‌ها برای مراسم پذیرایی بسیار خفن به هتل پنج‌ ستاره و لوکس ساوی پالاس منتقل می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27015" target="_blank">📅 20:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgRbl2z8DOXI2JdB6psnmJYX64hTyzonXhc28nHyuDeuuanNLfMhGQfwgaVu106bdIJHx53YnMBmIVW6SiaI3t5-PEUs9SHVOf_iZ1yl5XyEl89_XcBzBCpXLdnKjU8ZxuIhyGIevO0rNsNIwSpQMPiFGrEN3pVngHuZdXflVTPa1o8kC7xLbFS_pryXtSwxMbPKoP3Mn7C4XnPvABxzmOM6a0oztGrSWRhE3FW-RPYpotIViZ7J1JXiQxl9UJfwu-s4FZ3ZHvj45lVe6Z3Tw5GD6GJuVQrm3wao6lHXOi3SPd-Vu_OS9nvvzfhudgqs-0jza4v9u6_tIYwOecqdiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27014" target="_blank">📅 19:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27012">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=ZsbmFHM1enduYPmhIKuxS4caG9HVx2WdSJICKX4QoAtdoGSCanAqzVkTI4Zu4sBxT_0GEe1m533OG43u60lB_J04H79fXJhIr3yT74jHJpxbkD_Af7LdkOgcX9sneSjB046xe-6QnXGi6u9S2lgJbbbPGfKb9Jwk46eJLo6mL4qeh3YZ_b-4CiC6ZK1F781wf5MKusR0zjC2m9Pf2hzT7dukYoMCSkDlLGztnE0muR2aoUaLS2hjWyYZP4Qt_J-g-6VUJiHIfWh4kiBu6qvGcwSlJBaxfidP2HKI2UFyKV5NnfK5gZAbe_G1fThZDnXrMuctIx_9P8VwuIwyHji5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5f5546ea.mp4?token=ZsbmFHM1enduYPmhIKuxS4caG9HVx2WdSJICKX4QoAtdoGSCanAqzVkTI4Zu4sBxT_0GEe1m533OG43u60lB_J04H79fXJhIr3yT74jHJpxbkD_Af7LdkOgcX9sneSjB046xe-6QnXGi6u9S2lgJbbbPGfKb9Jwk46eJLo6mL4qeh3YZ_b-4CiC6ZK1F781wf5MKusR0zjC2m9Pf2hzT7dukYoMCSkDlLGztnE0muR2aoUaLS2hjWyYZP4Qt_J-g-6VUJiHIfWh4kiBu6qvGcwSlJBaxfidP2HKI2UFyKV5NnfK5gZAbe_G1fThZDnXrMuctIx_9P8VwuIwyHji5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عشق و حال مهدی قایدی ستاره ملی پوش النصر امارات با پسر کوچولوش میلانِ عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27012" target="_blank">📅 19:40 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27011">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAInEPyOdHvlzrVNJLW5xLnvlYcVQzxbigLeAeTMUBiswDGLZEdhal7hOA3qSOSH_ZGhDChYMKOVjirDTKyNhjgtsLpefsR6Y713z1Gwxy_uoH1SOtD4uKX8Vv1UopuahAlxui45kFuMa2nJpuhvupGmfRd2gUfyRa5Lmk062pnGI6t32zb-q_KvMO6DIyZAxxddh9qmCWRsDK-DQeGKVhL2SPhtHWAk833Dzbu5JNT19rplawEA_ahF7TEppgt9HiYdRa7zurcRHWy8qAgWlVXpmYzkdxl5vxQ9_vp8Z6IeKZMZAXXZpL74tXNxqc4cEaK9mxjwOJTQKiN8XfpGgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ ایجنت مهدی لیموچی ستاره 26 ساله سپاهان امروز باردیگربه‌پیمان‌حدادی اعلام کرده این بازیکن اماده‌عقدقرارداد باباشگاه پرسپولیس است و درصورتیکه‌سرخپوشان بتوانند رضایت نامه او رو از طلایی پوشان بگیرند لیموچی سرخپوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/27011" target="_blank">📅 19:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27010">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n29RJCQmVX5OMCMa1MNaPHTuxaXLwhI50EKFO4kBm2zH9OJzU-ktxIGC4d7HSH3OtCPIYsISIswhZpnGP3j-96QXRdVdd-Ug0K3RGtIRaPoCC_iTvMUXNi5LLL2PeTP8iQpIB2pwhGr0_geliQWF828xtb5mdT5naxV4eeIlab2bMG4n1aN3eBPh16tG-2nXeJHMFIqiczlR1Ev7jZ8hDd5M_8iVUfBkckR6Lfw8ITYsfAmKdL_CxQc4G7qB_BC1VycmcxRMXlKvqCjrWMh42SRjcQFiNe2ZkZGGnwD72D4DOUxJBJ55bY1OlMpHvPObajXS4hc06fj4L20Z8t66YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مریم ایراندوست سرمربی‌ سابق‌تیم‌بانوان ملوان عصر امروز با قرار دادی دو ساله سرمربی تیم بانوان استقلال‌شد حالا زهرا قنبری کاپیتان تیم پرسپولیس به مریم ایران دوست بابت سرمربی شدن تیم بانوان استقلال تبریک گفته و گفته خوش برگشتید انشالله فصل خوبی در باشگاه استقلال…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27010" target="_blank">📅 18:43 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tILFXP0vtXu_FWEIdQxgC4-Izkq3AJXN2o53ryIABu5o8FmM2y0ZeIcEy2kV_2FuxBOr9NBG8bQg62vXe2HgCJyCCCv_JDENIqlQIBzDWJ8DCBi3ecq1Jo4Gp0JN82d6XGRpf2KvUsUyVuDnQpKpVdYoVzBRFfZ47mxxZfC6yeYlqIhgvIKH73CtiKQ-jfGgYRcuc9-rPwWfIIb0LBoL45nHh5YUuJqrKDovpJ6QO7dwGuXHxR3vejnui_kJ4wIghqo1VRBMzJKcy4EKVFrcDjhLPno8w4ECcs2bf0YX8AzpScwRf5TKXgdZ9rUE6HwBebI_aN-Bif-fKBOr94eM9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ترکیب‌پرسپولیس برای دیدار دوستانه امروز ارزروم اسپور؛شاگردان‌تارتار فردا به‌تهران برمیگردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27009" target="_blank">📅 18:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✅
در فینال مسابقات لیگ ملت‌های والیبال لهستان تویه‌بازی‌سخت و نفسگیر موفق شد آمریکا رو 3_2 شکست بده و مجددا قهرمان این رقابت‌ها بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27008" target="_blank">📅 17:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27007">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swzTB6xRWqExzi7An8hjyfKZ25M52Mdnj1ib9w4cr1OwH6R_sHy68KNAOEv9Wn8vjUJTxvxcSXLqYQpswwtxpr6x7UlcgukFCUbbZDr62KazwVeFp2kBUFPq599vxQi4RLre4E3HNLXDIRN9WH-aBHvm1Lq8wXHpPY76mtPKdN7na5Z7AB8yNawQLgY_0jBwnSlbaVoesVIAMLKsynRSNMpyZ4G0OfSNa8hW_3ZRhIrgNm7JEu4RI9P0hzJQ5edNRKYe7dM75ULN9lk_YIZoPcTOQgPCimegt8xS9vU8Gpv4LkzMJGJGuYjcb-b7aeP3Fh50nwFQAiaxEHTnkQ6Smw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=AzSmC5IhPyEIl8JJa1VFQw3IP9YV7QpmPIOJehLUQ2Db5qMMbgtonmPjhSpcwdk-HFkbmkYDpfBAPT6QXwRVI_DGBBUODrfQKIku5jMI9f7mgTAjoc5jOXXAIUPKvpBci3E_K8eQe_4IievAgUjDJlvVqwBK3idcn3f7LYf3OxijSbYoII2EwxPjA-kfUuvE2zZnd43tWUvZHbBoZETLhbjCXR65FUAbUIVmttSK5muFdzYFbUXuD91PgTyCFIBktj5GteihGySFYhv5mzBGgO85rzD8J1PiuaG25bUXe23b4oq9I1EmhsPNvswP1wYpNorCUBOZj9qIstSJOoV3dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a40435b41c.mp4?token=AzSmC5IhPyEIl8JJa1VFQw3IP9YV7QpmPIOJehLUQ2Db5qMMbgtonmPjhSpcwdk-HFkbmkYDpfBAPT6QXwRVI_DGBBUODrfQKIku5jMI9f7mgTAjoc5jOXXAIUPKvpBci3E_K8eQe_4IievAgUjDJlvVqwBK3idcn3f7LYf3OxijSbYoII2EwxPjA-kfUuvE2zZnd43tWUvZHbBoZETLhbjCXR65FUAbUIVmttSK5muFdzYFbUXuD91PgTyCFIBktj5GteihGySFYhv5mzBGgO85rzD8J1PiuaG25bUXe23b4oq9I1EmhsPNvswP1wYpNorCUBOZj9qIstSJOoV3dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27006" target="_blank">📅 17:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMrEPKoLxyriBAOfmYLYZFpRDRLT-iZGXA-UeRmWeTZwb85kd0ZRTY2KKrj35H8-TjS3nvea_idk9rQxSNU3ceRu2VjhmG66_gjKMkw8LIREKuPggqCaZg1KffhgTYS2ouipF_7vDyKNyIGsqQYlk9lWof6GVkBoRCXeLyGXxsqtb4ri0lpYBrW8OQo0fT1ylncYIZRCWLeWl7igc9w2EvhoeQJtO542UgLylpnw2NFYeliCNSVqs_RRb3kCqwoWdoqD9ydM7E9ePcl82vvpHLHmUNAkpu27ZbeXfK-v1iY6umNS_mO2x9c6OzrJsEB0U9_Osy3i_vu4ir-fKp42OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27005" target="_blank">📅 17:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhLjn9pgb_XKtFh7NawWM1Sy3qU7tnoS9eubLFFZWruSdqX48Rv-XDRRMgTWNNT4h9lt6YZrfjezGc5SQnLBzKSK-4v9Ykhqx1F9HtBCm2HSx6Yi61by3UlIv7A4GD7U0MqL7TXrlQ1stf5V1nBY2l-X5aOid8Yz3e_XG6Yw-N82qW7SDsl8p6zmI_RDbx8JpvVCt6-pyzoOM8zxjkf-R4Y4uiCAowcOJlfpH1MrOc82HOTS_Q1vrirZYD01kjbUCIYhJPN71O-I27oegKV6kJikolcZdPiAvAMJ2845r-7vGCsJGjHbny-HJ571of9WZhlyQtW9193MbQwgp5l6nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔹
👤
طبق‌شنیده‌های رسانه پرشیانا؛ با دستور مسعود پزشکیان؛ مجوزفعالیت فرهاد مجیدی در لیگ برتر صادر شده و حالا به‌خودِ مجیدی بستگی دارد به رقابت‌های لیگ‌برتر فوتبال ایران بازگردد یا که خیر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27004" target="_blank">📅 17:00 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27003">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNLsQfC9lzwFB5Ar7Y-zUpT4mvQNJenSNIDJYVr0COyvcPPXt_3rpd7V5AMsHTy9H_9H1N4dPMxGtAQWAr2L5aD3qr44wJ-d4pEBT-rI24dQXvqv10IqOvD54nc8hCW9fyHbUegQDuIKChBKZ0Odjca75yGICajn7rN5q8QS4U0TV-aLq3dCUwGy9D2Ng6upWwq4MpVAT0DpA5VQ06J-ljKmL5ELnwy1Yxe3agBhXRj7gv0QrJ5XKnJ9smOK1W_Q10hDWP6d-mWq4y20JbCuIdtr7ngtCVRNl1o9zUkXNpirzwTKBwWhM8Dwk59c2Z66OvlPEDrI05wbKSTQ2H-XiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ سید مهدی رحمتی سرمربی‌گلگهر ساعتی قبل در تماس با مهدی گودرزی شاگرد سابق خود در خیبر به او اعلام کرده که پنجره باشگاه استقلال باز نخواهد شد و قید عقد قرارداد با استقلال رو بزند و راهی تیم گل گهر شود.
‼️
رحمتی پیش‌تر نیز مانع حضور…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27003" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27002">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIeSK1foHo7Ipt0lfk4tozLpi-CUcn7GyufIXILI5AGeazZpEYAAje1wXOtA32M8ewt06YA8q_Xzcu8J7ovA2QyfvaTdWJqbonZ2l4hcI8BSkoe5ppPSXjyGl4H6v2r4vp91mlkt_TgyPMM6CmQoRly9Ej1Hu4fDMMLjbYhsJupH2a0Ipvn3UTylcbGoW89Y5A7lPOoz958Tkw5LHifWSiVF1wzwZRYnti2KogvFA2YqEUAtPkib7v99e0tTad-VhzEeTU9v5h1E7u9tKrt9EYN6E91mpAsJlbmI--a7GEpJALwbj6XBREaSY0SRQ9V3lSE6kMun62M2Yj3_vzgr7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwXefP5K8INN_BEw9lk1zpY2CqPxcoFLWF4UyVwDHav07TZ41a4uryEDTjFGndZNzNjSIksskWDypmkHfHYW40dMrkJTOzP7sIqCgBeqAeqUnCC54DGfx06LlMRnjwT42PTRx-pGQCq9CR_bm13Y0F36pqQpD6YMUn-CZqux9JUahFCWvZpheG7wqcukLl4xuW2mLlHSZvzu5FHSfhxKeIDj3aicMLwDrvgGJ2IbS-ohevsVk5UuuQZBR9H2-BbhbPnx_4bAEB5Gc3aRFyZr1Jgy6Gf5iaMJWN98lgaJN0xxAB9NDSnRzt3TydJD28kenUcCTmaELm87un67mXcxlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27001" target="_blank">📅 14:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHLsjFBwaxW2HtNmFLRsEWKwB_LjRIifNlxPKHLga7rgsUTMaX-dafTUY4F7333FiSoqliDpj7DBspcz88iguYNJ_6RYz_civhZMDRgJXCSwR-pyT5cmL34cIOgBrsQ0ADpaskfDC_u8caK7xkF5NGpAP0nMCcnE3dYJ89Hr_upgyRy1ksle80j05UQNld5UHfH9JmqeClluSQPuLUAVlxrnBCQsQ4KW3wAN8WQE0pfj0jtfuNIx0p5FjsnZcG6RDZd115zYLRsEHBSxOeD5av8xNnJg9rD8DA8pR5lPx1r7UejbQyUJesDwru1A-XcnrH_TCYHpHlFJ9kgtRGIQPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27000" target="_blank">📅 14:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eTOBoVm-Ng-rpmCpof_eaDwZtGrg4nOsFU8tMtHm7Y5O2DlUyop8jRRZLRtC7DpbsVIjSrLZs9NTqxqdWvtREKed_PPqUD8hmbiQIWw8Y2sOYqsc3clgprY8zDdS3VANN7g4ySqzBIFGdBeENA5GUGs_ajU2nQyepDPlLYW84t8Zxr0a7l59sYN8i9D7jRVDTE2wOVp6OLVtyJr6o6WOvxD94AZRFboVfSIMZVaTF6vWRufkPQ6Y1ujhlPnoOhWcYEp4bv6WBrha96-HV8Wrt8pcl-9X2XBwnWqZHGZYboDA2IQaQZX2GOqww3V-SlzsIG_796tDNN-f2Wup3fYyqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nowhxpj9M1kKgU1yoJF6psuwSkIk2jgbnKprSS-aUEg9IL_0MrAXUO8kBmCp-xxKO-LfEuxK7Ev-J_DN-X9GFjmUhH-b9P6KIUz88fQH4OCJPyq_P0bNGqdtMvWO6CFE-ldwLqlOsALLC1AENKinvylhC9EiMwjCawPYQLHzaTBlea6RVdRWCRIRovZrpiesz3grcjSvupV_tTmL2-7V4z0I5ABEx9b3Bs0Ak5ZPMI_FnbgNiyRqCBw42dy3dW0vvQ4haS10Qur1GTsZgQf0dew7bFIzFQ6UR40ykQgYsWogbDKM7AqaJl0D7KxMp61WyMGfh7kQ2YG45KT_N6dMyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👤
کریس رونالدو و جورجینا میخوان‌؛ مراسم عروسی خود را بعد از مسابقات جام جهانی در جزایر مادیرا در شمال اقیانوس اطلس بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26998" target="_blank">📅 14:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdfrlNs2B-Izkk1n1Xz4Vdx19vs9-FhJ4-XG9FD7zPFioB7O5PA0gQhRkRPC8K3BlAvzfro0qowI2DKBYkSrrFXOO7ZQyVHjOlbLH1uKPHv189xxtfo4o-f9jX1P0MQhj4urib_cQr8fTfxLkt5DRpUCXEgFcC4nBA2WbeKxcafHFPGKr9aPdgvtHEMPZgpDWdgrKXpg8Ec7eleQmh6nesAIqGpOUIT7xM2Q97SpZx8T4J0gR5rCVxitkCFg1nvR0sYa6gBuHdaif8Ao0es9cnfjaruwYNo2iRL4l4aNvQJnY513tv7k9xM8NYVBUA4oPZFRniAlqeNut36EWODC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اینم از توضیحات کوکوریا: خیلیا بخاطر مدل موهام منو مسخره میکنن اما دلیل بلند بودن موهام پسرمه که اوتیسم داره، این تنها راهیه که میتونه باباشو از بین بازیکنای دیگه تشخیص بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26997" target="_blank">📅 13:57 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26996">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bj7FK6FEAmw3fp6BSOYL5X58U-lBkWE_3jFEW3Aff6ayp0zF6ESzwIkC_sDNJL1LF6O-GOowj2kN_DlN3PgbLKLuS5ITgeq9X45LEycQkbYXzNpBh7mDKx7pFqtoV9ujlebx0sqK9y0FY2tn7afwGa9LpvZJ0h712Ee3kzHQ9lK2-M07TryIFjo4a4see31gxKMfJoT83p3vnrFfhVPs2U3ui_2ih9CuWUzsFYF7JlLoh7_a04JYvNsak6GIbyg1ac-QoMCn76000W4AsEJvFItB4GPru3ZNh3W_sqz5I7eO66SZkVLvoTYGrSk0M5kSD1LZFsD7UpnpHcbek73j9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس‌نیشیموتو بازیکن تیم‌ملی‌والیبال ژاپن که باعث خنده خود او شد؛ یه لحظه تعادلش رو از دست داد. بازی فینال هم ساعت 15:00 شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26996" target="_blank">📅 13:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26995">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=D6q2UAO0UvCl3rymebab4nspvp1qikn6xEFMMYbCeD-7t5vLTLZMsE0IhOd9RiHlkAFdRGOv88sZ56Wh-FXNXVxRYcWjqTbjkKv6GeXAbL6n4q6sswOq8E4oFL77WK4xfVvDFGp9hUvlJe4vwNeUPKMldkOTsrSlIL2_c-eTRBeNBOHuo00qRLjQRMHjHjcZbMottupy8d8k8PKSafz4bDeRuib46PlboFMKf7pMgVi-k3bVaVNhUpcT8drXnuY-sHUI6gCSf4wAE2vy2s157Lv81ff39AJbyLIRtIhywf5udI1tjczhJr_A-U-zOHoetaOBqAiL3D9uuoG82PdSI7LmuQTHmKhScae_Zle6aMyAyNvrQ4r0rIfjCFsXc_Rq9gBOmnL3lZegwfI6SjElK9dw8zTpfYPWkQ1uZmFrNSOqBogyZW7gPUqBxfGGmQZ1b_WLTzBpKk4M4PG2uWxEEZVUUHU-fCbvCN9PXvLpb7nM_YGR-iLQx0OTPxJeRwEvQr3u7tgdHQdHNN0yCLb0cppwInCuxu4mOFnzkF4Jktx_OeJdSVTTNxdGUhgJlc4l1AvjbuCmHIYaIzSmb9GUiwE45qjC-jwgWV1cv8c9qe1j31wE57EHEnFVZqZlRQcOLhV6ncA9fW2LJPao9ut3ugcbRZRQNeYQ3jQo5UGr28Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71a95e55dc.mp4?token=D6q2UAO0UvCl3rymebab4nspvp1qikn6xEFMMYbCeD-7t5vLTLZMsE0IhOd9RiHlkAFdRGOv88sZ56Wh-FXNXVxRYcWjqTbjkKv6GeXAbL6n4q6sswOq8E4oFL77WK4xfVvDFGp9hUvlJe4vwNeUPKMldkOTsrSlIL2_c-eTRBeNBOHuo00qRLjQRMHjHjcZbMottupy8d8k8PKSafz4bDeRuib46PlboFMKf7pMgVi-k3bVaVNhUpcT8drXnuY-sHUI6gCSf4wAE2vy2s157Lv81ff39AJbyLIRtIhywf5udI1tjczhJr_A-U-zOHoetaOBqAiL3D9uuoG82PdSI7LmuQTHmKhScae_Zle6aMyAyNvrQ4r0rIfjCFsXc_Rq9gBOmnL3lZegwfI6SjElK9dw8zTpfYPWkQ1uZmFrNSOqBogyZW7gPUqBxfGGmQZ1b_WLTzBpKk4M4PG2uWxEEZVUUHU-fCbvCN9PXvLpb7nM_YGR-iLQx0OTPxJeRwEvQr3u7tgdHQdHNN0yCLb0cppwInCuxu4mOFnzkF4Jktx_OeJdSVTTNxdGUhgJlc4l1AvjbuCmHIYaIzSmb9GUiwE45qjC-jwgWV1cv8c9qe1j31wE57EHEnFVZqZlRQcOLhV6ncA9fW2LJPao9ut3ugcbRZRQNeYQ3jQo5UGr28Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
۱۲ سال پیش در چنین روزی
؛ منچستر یونایتد و رئال‌مادرید درمیشیگان به مصاف‌هم رفتند که ۱۰۹,۳۱۸ تماشاگرشاهد این بازی بودند. این‌بازی هم چنان رکورددار بیشترین تماشاگر در طول تاریخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26995" target="_blank">📅 13:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26994">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=roEzvS7vBGZiKhf_JTM06qKtm4Iv74FjYnxgKcXi1C6ZKV6R6GnRnJFpm-T-Gy4blSBWtoO7YdoCVoq3tcEqS2MJtzw4Rlr_feyUWmZCmxwkpMNPsSXIpExf7UvWFXTRDNni2BUycHgImCbBD1uqftQUtYi0VSlw0u0tgEvXPk_b2RE1ybBj_h-6fBl5zB4gKCxMlk5B5f51EsRzsVGs_uqHT5SJIFGV0wQz2H6FL_Q2k1T30L-QL5Fy_X3zvxRMI6kGTP8rishVhy4cBJ76SnXM8L4G-JU6IesTu8eRscNZarSyek3B6_y_2yqYa4lCHZKNWCuZuFBP9xc4QCIOsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3f4f0e8.mp4?token=roEzvS7vBGZiKhf_JTM06qKtm4Iv74FjYnxgKcXi1C6ZKV6R6GnRnJFpm-T-Gy4blSBWtoO7YdoCVoq3tcEqS2MJtzw4Rlr_feyUWmZCmxwkpMNPsSXIpExf7UvWFXTRDNni2BUycHgImCbBD1uqftQUtYi0VSlw0u0tgEvXPk_b2RE1ybBj_h-6fBl5zB4gKCxMlk5B5f51EsRzsVGs_uqHT5SJIFGV0wQz2H6FL_Q2k1T30L-QL5Fy_X3zvxRMI6kGTP8rishVhy4cBJ76SnXM8L4G-JU6IesTu8eRscNZarSyek3B6_y_2yqYa4lCHZKNWCuZuFBP9xc4QCIOsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
رسانه‌های‌ مراکشی: منیر الحدادی تاکنون دو آفر باشگاه‌های مراکشی، دو آفر باشگاه‌ های برزیلی و یک آفر باشگاه‌ های قطری رو به‌ دلیل پایین بودن رقم قرار دادش رد کرده است. بالاترین دستمزد رو باشگاه استقلال ایران به او میداد که فعلا راضی به بازگشت به ایران به…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26994" target="_blank">📅 13:07 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26993">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kbe-gDEPA53gtZnI8xIfHHR_xn3Fj84CP_62Ujk-S39QsFu-iyNNlir20zGN6H2QJZi3yUHNjMrQlQ-NmiRMxN8rn8bsKxqPj6n-CUnMvQdcs6V0tm07gx5-4_tQhlO-C8LceNbjzgTlzaUH0CSqSZhKk2TmGkWR4BylprJXcJE72bH7dWfsKvEYurf0VdTdlkjcd2feAZl3DbiIMtCzMGrWNX_wa6yE7jC2inQDrliDYhmgUcrI84Aj4Box38-5F5BVK6sq8WYeYm2fNxaqvURcN-xSaTwYY3XIPBBPkk_Qx0PeXfGJR-VCE7EvpTAv30j6tQSwl9BHDHA68NUZzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
دوران اسپانسرهای شرط‌بندی روی سینه پیراهن‌ های لیگ برتر انگلیس به پایان رسید. از فصل جدید، تیم‌های لیگ‌برتردیگر اجازه ندارند لوگوی شرکت‌های شرط‌ بندی را روی جلوی پیراهن مسابقه درج کنند. این‌قانون‌فقط شامل اسپانسرهای روی سینه است و سایر همکاری‌های تجاری همچنان مجاز خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26993" target="_blank">📅 12:54 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26992">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMM4pou33TfUZ3_uPGmaTjSOD_G2-ssAsvCfujpe0k6mDJPjJbdZrSc5QTM1nTWRLYLy71qCk4E9PYISwa7dOgHee6bdU-5y_WSdKk24BtiDGvhgZjrLx160-Lyg__-hYttYxB9CBb3WsVwUIuuH-qqCNy8IOLoRBrmve3Y7z4_0WC3nqBM9GXVXMVHPCtp1SAVbmfrtRg_fwF980NNd1DzC5h2gyOmjURYUGX_EvybR9AAxtF1aOXOdzvU82Cvme8ZiqnPBIunj66pRqAcZuvFHqHRY3vlVM1oR4lTtwn3Pmf7Fz_FLWNxzmbSb9KUvwJ88FKKWvbN_G8q5-xx6iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔵
#تکمیلی؛بااعلام‌رسانه‌های اسپانیایی؛ فران تورس بزودی قراردادش رو با بارسا فسخ خواهد کرد و با عقد قراردادی چهار ساله راهی PSG میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26992" target="_blank">📅 12:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26991">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_Usx018XM1qPTMqbr78Gi2g-2XQu2FQ4pzRtgeKcLXr2u71ZJI9gAkbwuZLEV_mj3Rn3mW3d44R4BfLeeXZfiDxgYckNA2dhg71E2awFcjX3UbUAwQKc4uYMC5rXBNLP3Ks5_Cu6P7b1RZzw3ZgWMem-I72aAjEEEpOzYFKNXbNrcnNXjMODKKYykWEey1c_hjgnz8REhoa97cdCO5V3CcDS3_16RXrorUO0ojP_9um-mAW6Sp6zneQLut2Wvh-_5O_KwnJd8oMi6dhX3d8RB9AypuSvzzqUpQU-7dJcL24ZEbCw5N9OZ946UOWiJb7JtJUxbLksrgP-9RH0eqzzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ ماخاچ‌قلعه دو روز به جواد حسین نژاد فرصت داده‌ که‌پاسخ‌نهایی خود رو نسبت به آفر باشگاه‌پرسپولیس‌بدهد. ظرف 48 ساعت آینده تکلیف فوق ستاره فوتبال ایران مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26991" target="_blank">📅 12:21 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26990">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU14nQ6W4Bc8d4UpvSVpMwcads5PuMGJyL6ape85EfU1hPnkwGo4heqYEl_a03Y0oefpBp3hF-RETA1s8B8v9vNOa9pIbWwRE3yAyN6W2L-N9t6DcTnHNwgEeCxFCYShV5hwpU682Ap5vZB4DkhVEpKRqZa4bqpSkqUNCKFZKTp3RjQTaDFxy34tA5GWN5w5-kfqfbG-1cDrmXLwIluFsw3BpMSb1Ly4ugDw65ymu2MrS6vnCttiCQZmD-0GMAp2RiHnbFzUWcLAxhfVNY79g-NEYbmuH_MIXGu_S4d5ArD5so0sORaHxEJOOt6OokMqAGA18nxsJXWPazvYKMuMwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیج بارسا اومده صحنه سجده حمزه عبدالکریم بعد گلش‌رو استوری کرده و دقیقا تو همون استوری تبلیغات یه‌برند مشروبات الکلی رو هم انجام داده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26990" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26989">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f58235729a.mp4?token=FeBLSmVThMEnMarz_gRUvYzkB4QvMhPepQ19lbGiaD2F69om2QjxTKkKRrR8LGS7Q1e608Ohs7vJcmgfjNex1Y-CsCdKH1M9qZg2LUzXSv9TuO7JLe5goRsWrw0sypvH99GfvkH-xJsRyVaVT7N4tcn53UHxhAR_pEPzSj2wib_evFJ8yA0bLX8BBjV9iJIQJqE13CjJI1a92th0bD6tELTP_0_3S0ttTN0qUcv6JgU9lx0mx6VwcyfI1CttkkHJVmRGBxlQ55ulqfe6MACuvfGb7Z6KxSXbe17IsgNW_ivYNANwKZsltSBQ73vEgcg4fGGh4m1zBtFxhHuqcuRmdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f58235729a.mp4?token=FeBLSmVThMEnMarz_gRUvYzkB4QvMhPepQ19lbGiaD2F69om2QjxTKkKRrR8LGS7Q1e608Ohs7vJcmgfjNex1Y-CsCdKH1M9qZg2LUzXSv9TuO7JLe5goRsWrw0sypvH99GfvkH-xJsRyVaVT7N4tcn53UHxhAR_pEPzSj2wib_evFJ8yA0bLX8BBjV9iJIQJqE13CjJI1a92th0bD6tELTP_0_3S0ttTN0qUcv6JgU9lx0mx6VwcyfI1CttkkHJVmRGBxlQ55ulqfe6MACuvfGb7Z6KxSXbe17IsgNW_ivYNANwKZsltSBQ73vEgcg4fGGh4m1zBtFxhHuqcuRmdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مهدی‌تارتارسرمربی‌پرسپولیس باردیگر در تماس تلفنی به مدیریت باشگاه اعلام کرده نیازی به حضور تیوی بیفوما و دنیل گرا ندارد و این دو بازیکن رو در لیست مازاد سرخ‌ها قرار داده. اورونوف، سرگیف و باکیچ 3 خارجیکه تارتار سبک‌بازیشون رو پذیرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26989" target="_blank">📅 12:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26987">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/436452afaf.mp4?token=aBcG7vKo3N8qHlqyXEtIGzz10bZAPC93vnL_dKOshr1y0kVxJJiRVPoQLE8gUQSJCE5sPOdGBryInyG1v0L4S53ICLU-ZzfiU-YZGcrRNKEZpcuYxpZKSj4uF7uiZrTUjmbx81Pqq7dM-mINccogO0w5joVVDkn-Fkgy7TYDw9fUy71C7oj_4v5TpwwI6a1igvkrFzAdAO_Mk1hzfMjvKl8CMXOLEw__T5GO1zdFdaZyuJ1D3Jogqd_3jN9jIdpytJ9Qz6ItmaFWYYVivkzM6MNn_V8M7FkbVGkltFCpiuNYazM-x7JYmf1zphbz-O_n9FW53ZyNYrnLvfbybZpfPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/436452afaf.mp4?token=aBcG7vKo3N8qHlqyXEtIGzz10bZAPC93vnL_dKOshr1y0kVxJJiRVPoQLE8gUQSJCE5sPOdGBryInyG1v0L4S53ICLU-ZzfiU-YZGcrRNKEZpcuYxpZKSj4uF7uiZrTUjmbx81Pqq7dM-mINccogO0w5joVVDkn-Fkgy7TYDw9fUy71C7oj_4v5TpwwI6a1igvkrFzAdAO_Mk1hzfMjvKl8CMXOLEw__T5GO1zdFdaZyuJ1D3Jogqd_3jN9jIdpytJ9Qz6ItmaFWYYVivkzM6MNn_V8M7FkbVGkltFCpiuNYazM-x7JYmf1zphbz-O_n9FW53ZyNYrnLvfbybZpfPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏐
برنامه بازی فینال و رده بندی لیگ ملتای والیبال؛ فردا ساعت 15:00 مسابقه فینال برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26987" target="_blank">📅 11:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26986">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs4OxRQZfQoiu-RWVycCJ1qtAYBO-mphfap84lNOHXSxdawifwzBIDDRMJ6NUu2DpTHmkGOQdQdL1JMZlpRKFBibxzYwwT1pHG5lj3OPdauJY77KBL7sC5Hyg4RjhUU5bp6MJYw97gh9urr6wHpUQe3jF-WwuGhHUwEyQBLGXLQbp9PWuYb4k8wdykTu_ajRjIFMKOwe45hQAouZR3YfUk5r9gh2KBT-XiTtqY9tS3UcOxldZDUr8MFCkmSnf-xKejHAwZ_ygqNoK53nALphi848gVTBGCwBDEeCJleaP2qlJc-tSvoHcybWSXmHkU0_xxMJczc-7JOSdex_q29nUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوری از دیوید اورنشتاین: وینیسیوس در حال تصمیم‌گیری برای خروج‌رایگان در ۲۰۲۷ یا پیوستن به آرسنال درهمین‌تابستان است. آرسنال تمام منابع مالی رافراهم کرده و بازیکن به این ایده علاقه نشان داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26986" target="_blank">📅 11:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26985">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqwQ3yBnPeA72bVsahYop_wweGg-mvSWbo-tiXrSGpk0v8mD91qIMq7U4irLHZVyYJZ8CcZ2O6wA7vHrCm-7Zyj8VdkrJDXVMuOa1urpi-QDM5CW1h4pZOWNd9pqVC4ppqSPRvtX0YDbtSvaP_efIkMXFZ3cdrS3aecQ6d1CNEnBkA9aw9zO-6RbcVtfxHbdfYv4yk4xmEpOmn5-ePHsQvkW3-aaQ9qOlkcTrooF8d7mOPr33pTJiL0X2m2o0AoVGp7CWxcDzsfgyi0-7b_uWRy6ej8W5n7BX6f4hKxWhoo5hEV9zSA_ci65pJl2CfHL2zDp-cjf5mAN3IJRIZTOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیر برنامه‌ های داکنز نازون: قرارداد نازون با‌تیم‌استقلال درفیفا فسخ‌نشده و باشگاه بخواهد این بازیکن به تمرینات تیم استقلال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26985" target="_blank">📅 11:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26984">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12920f454e.mp4?token=f0fjYR8hOp5LANJlnVDAXbhuFCklWzGwRH8b61kVMMd1ZmVLsjV2VaJcyI-7nDoiNy2V1a5jwBcfylLMMPlk4tCmG_mNh0PJmNGsf0Hd7cOzbQdsOmFEpugI232kXa7dUKnj5I1amtiX0N7nOOIZ7_cl_KMQqsv_QaIgFLveyV1YM6g-9TJ_mluGv4PJbwAe1tF7MTOxgmlkAc_-mlKpyxVAFOB150EKiWyclm5APIEjdDQTS3uPWowERH8TA_gUcSiG7EiY5a9-LubOBJDpCWs832qn1uILX0vkQK_fv0fzYW3Gao_Bc7BmKAzpIs16X0QbGt1otPAARlGCTGg2Nyo2DcJzksBUj1OTkYLeW9SWlxjP8k0XSekWvBQwnK2y_fZ9zxJQBfyY3aUMlIzLkENBFmao9CGTSJg3pwwte--2-H850w6WS5Q35KKCsmc98utZmzDdysT_vqqXcLWQRXQ2ijRoIppYmcxrtU1rQssXK-lxwptf_t5kyx4WnflMpWtl-S3CogRIfLSOHYM5lSq9Hr_e2qBeDuuYsW9SYucOPKDFolVP6o7WRTLKsnocD_XOagrPbO2GGWBFbdThS-EM6PjtQm8DnnPZ6MmRD_ZvulJpkUYRTJJQeJ-mfKOKwxtJKOVGlFr6PxQmia0RmAVtZag-lyHd3DpcvNeopJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12920f454e.mp4?token=f0fjYR8hOp5LANJlnVDAXbhuFCklWzGwRH8b61kVMMd1ZmVLsjV2VaJcyI-7nDoiNy2V1a5jwBcfylLMMPlk4tCmG_mNh0PJmNGsf0Hd7cOzbQdsOmFEpugI232kXa7dUKnj5I1amtiX0N7nOOIZ7_cl_KMQqsv_QaIgFLveyV1YM6g-9TJ_mluGv4PJbwAe1tF7MTOxgmlkAc_-mlKpyxVAFOB150EKiWyclm5APIEjdDQTS3uPWowERH8TA_gUcSiG7EiY5a9-LubOBJDpCWs832qn1uILX0vkQK_fv0fzYW3Gao_Bc7BmKAzpIs16X0QbGt1otPAARlGCTGg2Nyo2DcJzksBUj1OTkYLeW9SWlxjP8k0XSekWvBQwnK2y_fZ9zxJQBfyY3aUMlIzLkENBFmao9CGTSJg3pwwte--2-H850w6WS5Q35KKCsmc98utZmzDdysT_vqqXcLWQRXQ2ijRoIppYmcxrtU1rQssXK-lxwptf_t5kyx4WnflMpWtl-S3CogRIfLSOHYM5lSq9Hr_e2qBeDuuYsW9SYucOPKDFolVP6o7WRTLKsnocD_XOagrPbO2GGWBFbdThS-EM6PjtQm8DnnPZ6MmRD_ZvulJpkUYRTJJQeJ-mfKOKwxtJKOVGlFr6PxQmia0RmAVtZag-lyHd3DpcvNeopJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇱
دبل دیدنی لواندوفسکی مهاجم 37 ساله جدید شیکاگو فایر دربازی بامداد امروز این تیم در MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26984" target="_blank">📅 11:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26983">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=ArX1mBOkwz45xq9SqGkxTRRyb3Q84RkNmjncRIyrYzJbkyrPUc8ELGksyNcItKUmgYRMVmTa2e2k0WI9YbR58GMwKyVBz2loxBuxM794dc5257pseSsQScJcgK8bJVVoes7VIDWkM2h0WOzo8A3k3XuSrxlGNDtPUiBREOxyIevCJE6Um78CkSMlHyKE1kEhgEvL0LHB4RiH24JDic2BHovAkDmPf3LsZw5ozLQIEP6XayeDI5QBZoVjCaMnqX9gJP9vG8DCe8oUY36WRRCabdctqQ6jWEzPkGDz9f97lY2tqpQGA79dHnZGUxTjfa1HWV9Fe-G5ZcPVkNv8q88CKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6fdd524d5.mp4?token=ArX1mBOkwz45xq9SqGkxTRRyb3Q84RkNmjncRIyrYzJbkyrPUc8ELGksyNcItKUmgYRMVmTa2e2k0WI9YbR58GMwKyVBz2loxBuxM794dc5257pseSsQScJcgK8bJVVoes7VIDWkM2h0WOzo8A3k3XuSrxlGNDtPUiBREOxyIevCJE6Um78CkSMlHyKE1kEhgEvL0LHB4RiH24JDic2BHovAkDmPf3LsZw5ozLQIEP6XayeDI5QBZoVjCaMnqX9gJP9vG8DCe8oUY36WRRCabdctqQ6jWEzPkGDz9f97lY2tqpQGA79dHnZGUxTjfa1HWV9Fe-G5ZcPVkNv8q88CKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاسمیرو بعد از پیوستن به اینترمیامی: اومدم به لیونل مسی کمک کنم که جام‌های بیشتری رو برنده بشه؛ برادر در بازی اولش برای این تیم امریکایی:  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26983" target="_blank">📅 10:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26982">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jP9iRXO2IEwZtLCswAz2WxoiLuzsBzUfesQSgeECiPJXKeNbNAxdDLAFYCAEIkjXZXNsEiYUcZ_rzDz-ruVQaaAClNs7mz-4NKxeAmPZUVJQSGFHhQgfOSWdtkDsA1lNr4XhCNGE9H_8PrhBWSa9Cj6etf2Wio51eAcl4_fkgJ7yIO3Bxv3z4el0Yv1E833eWyVItesjIZ807M2L9WAkLugrzjk8b2vmG5JnuEyYpdyecEGevTsveunzdZr0BgxKx53FyQ-y0R_Mdh0q6xTMAOqI6XOBKRSoZzDPgH5F5ZaTqrYs28UoJtlt5eBtI1NycU5R0uOfntaQTvQmiELxEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
شایدباورتون‌نشه ولی‌این‌دراز فقط ۱۸ سالشه!
‼️
«جونگکوچ ماچ» بسکتبالیست اهل استرالیا با ۲۲۹ سانتی‌‌متر قد، درحال حاضر بلند قد ترین جوان دنیاست و عکس‌هاش‌این‌روزها حسابی‌وایرال شده. حالا بخش جالب ماجرا اینجاست که پزشکان گفتن ممکنه از اینی که هست بلندتر هم بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26982" target="_blank">📅 10:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26981">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=uSwjwFoRb0IYy4c2ekExRJscC-uruz67PIBsgRsfUKrPo9ICPmjhsNg2gVeCkarMvfQ0-lACcSxPNwYLQskAKDqw6-O5WV1jQYiFxzQ7Urin1nyO825SHViY9vDaw_s2kQlnLzwrVB0ADEzWNIMT4e16xFP68d2bsXoQcc4BHy93w_4kKCjB7jZq7jKARvnDaVMv0IemtSs95qWdNn5zUruUGAnZ3PGI9nsBetRXY5QYNio1mHPeEj_wrUBOFzKb_8wSfFPOZjNJ-UWc9OOY9QBO5BHQBEUxDbttHhgbLcE3ei1ZVms9mki64iTUWXNyoOGE2gJLpGEDvxxfVbUJcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffde0543e.mp4?token=uSwjwFoRb0IYy4c2ekExRJscC-uruz67PIBsgRsfUKrPo9ICPmjhsNg2gVeCkarMvfQ0-lACcSxPNwYLQskAKDqw6-O5WV1jQYiFxzQ7Urin1nyO825SHViY9vDaw_s2kQlnLzwrVB0ADEzWNIMT4e16xFP68d2bsXoQcc4BHy93w_4kKCjB7jZq7jKARvnDaVMv0IemtSs95qWdNn5zUruUGAnZ3PGI9nsBetRXY5QYNio1mHPeEj_wrUBOFzKb_8wSfFPOZjNJ-UWc9OOY9QBO5BHQBEUxDbttHhgbLcE3ei1ZVms9mki64iTUWXNyoOGE2gJLpGEDvxxfVbUJcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
محمد نوری کاپیتان سابق پرسپولیس ملقب به جمله معروف و تاریخی "هرگز نرسییییدن بهتر از دیر رسیدن است" با عقد قراردادی یک ساله بعنوان سرمربی جدید صنعت نفت آبادان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26981" target="_blank">📅 10:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26980">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7BVjKac0MPtVvYkkYkQV-iLyPgaiSQV5ssabjAD5Sgo8GOycQsoa8wn3sO1mjoDW_Zt3ffkuN4nQxAwYoribc1N2UG4vezYP7E810NYtKhNcPWO9PA1J5BpieSRjA50Be8Kr0cL5fYsegDUKeh3zIBRdFogDdioyPkvUPVeEcvSwXLy-80_Ltt1jn9hmOlaUsFKd5PzAlbdaT_dZrbhXm18IXY64O-WJYRL7vA_PSOXFSkk3ISR4QLRh_YMJHaPAlJv50BQdI4u0Qoa_ib-nz7UEvhHoZ7TKj0PVdmALAD7NXCyq1wSlzgcepipzkeP3IrrIp6VoYrqBatKVaz74g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26980" target="_blank">📅 10:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26979">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH2rbR06tWH66IAFGGgUyvAX2JP57-HNGHdCgrKJxk4fUIa62rr8bKITRgLjIxXa7LatEUa4mE8o8NWHe-R3tWmSsknRBWuowd1cprzpVcyEw6W8H3r_q2QZavl2cszHMk6emVMFEYgVqxWyrMC490n8JmXE9XZRGdSiJyEwyR2BrRwsCgSvPr1iYuskC9g9lJRI6nfEN6cIYNHmv3Rhwtxdvv9fqlndSAghGP-PfiI3--7TYmRI3MQFA_aFZbHZf0SCmeAv4zGr7oeE7mwzVIFAXxY9hobhFTI-nao8ut4K3lR96orSozjGmYymNDJ4f0rpJ5NwH_SMRtOoHa7rIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تمام‌برنامه‌های‌هوش‌مصنوعی مناسب برای تولید محتوا در اینستاگرام؛ یه جایی ذخیرش کن به کارت میاد. برای دوستانتون هم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26979" target="_blank">📅 02:16 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26978">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN_1uVIvGM-iv8aoyztLlNt3-75C1bb0ZOEF6nrGpi1mHImuGIwXoMS8eRjAE2GOyx32f53bmiOcr0Mwq_zFaVCHlbT8131IeP76ZCv1a5dBhlCgsmXF1_CNF979PkcTpjKY4iv5qpyq2fE5t0GLNee6RdcTjUS4T9ihkr3VwXiup1yhzcvG2YZuQuOPLs47LPDHQMwxEQ2QzfTJAT306-O8tjLOXEzwACJTp04OYdO7-soa6JKgAmpCjXZ7z-fREIur_3ey3KyluLq3s_6pOADWTlMC5Lqkfgx3tqMQk4gQp18gIJGuxgO0Ol4UY4vETflTmnRx4ejP_-TgWfOpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه دپورتیوو مونیسیپال پرو که به خاطر بدهی های سنگین در آستانه ورشکستگی بوده و به لیگ آماتورکشور پرو فرستاده‌شده‌بود در یک حرکت خلاقانه کیت خودش رو به ۱۰۰۰ قسمت تقسیم کرد و هر قطعه بین ۲۵ تا ۱۵۰ دلار برای گرفتن اسپانسرینگ به حراج گذاشت. جالبه بدونید تمام شرکت‌ها محلی و حتی هوادارصاحب‌کسب و کار به طور خودجوش اسپانسرشده و باشگاه‌رو ازورشکستگی نجات دادند وقراره این باشگاه به لیگ برتر پرو برگردانده شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26978" target="_blank">📅 02:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26976">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEuXhT6z2KtrHlGP7sPoG0nE8x5UJLxXrHxAgHsAYHw_DVnQQhuJL76y7VXCkL_O0hv-DuO2j7NS_3GWGtC5GH00emSWHlouP7UxLMdqIXCaHd9FwgOTVQrWL8kK7_IeccpxeCrno9Dd8OOlb8Bb0qKV-gdLHXGGJZ6dU5YPIP5zlQPkNGf8q97fi7YFW8443TpCBfo9HeixrXNEH-gLje8VNMD-pJtrbZJHUw6iB-c0WYd82V0vL2yWZZILX8PrEkpXGsYZ8fQz6L1UWDAi0DJV4n3WDeexEofsU1Usw4NXFOKoRrqKSfcPP7l0QXi8wWRVD-xmziuNvaWWlHLESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
بازی‌ میامی‌ برای بازگشت به صدر و دوئل‌لیورپول‌ولیدز در اردوی پیش‌ فصل!
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26976" target="_blank">📅 01:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26975">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MuwfdJG4YwFH96SoOQQnq49q7N-I2AZc5jak8QPCJE-wJ4SAYqBqeG8Ax2hg0wvv4bR3CX2aYsaWsJmiN2bY_D_ijDLTGyQwhZgGyNdmk0I2leafh6V-PGmhBFA-EGjQ91Jx6uNCdexsc-J3gj-ELcXp5Mdia5gMGUW4MrtLnNUFZn1XhRfMn2W5jv7Pj6Ff6PQ0FMvKPwedgyKV7yVWY8_Hd5cedg4U1Mp1JiJBlStDYuUeF8lmQOTAqRNfKuo09qqUAMiy-nx1rfkf2r0pL5ZS888W11ZvwoVqBAFYONJQ9DcMXZmQ8O63Tzd47qUJ2CiMVHsH3S3yhWF5rpwFGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برتری لخ‌پوزنان با سوپر گل صیادمنش تا توقف رئالی‌ها برابر یاران دخیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26975" target="_blank">📅 01:24 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26974">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WdFnPYtDjBXiFMP809OskJr9k8owyfoKyITSVBFrieScp53fm5aUGjcrKI2_FcufzWwsH9ZJwrklBh90KkTt2QXSszThvandP6HAgHrgLkIQ50FGVrot2W4d9pThN5dXM52j8K_gXOBrOVGICvqPUsx86_iZO30-H8pqRkD_hmZwM_4H7gBJKWTm6t6V5tCtaZsRAmJHKZOnyqqaxacypSKNobPNWxmALaSJdISsS5mt27TTIeyQbB7unilfS-VBcGUXkJIREk669KjM3K8EZRjWtf1rz-pSC8lB_moNRn3ac8Bpx-0srRtFqMABcMhhdz8wFyKzqeQhy__DI4xZOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26974" target="_blank">📅 01:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26973">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYqGMVIteFlPanmD0vKgvgJ-TXDXxsbfLNHW0WHBQtgCXXUJVVY9NfVZ2n88HPnFTRPKKOwstOHdXarxmGI3rBacmainpnSWwHJ_CUzcjBEU4DTdLBldKo_Sng-GXgeojeOFhauY1j2Ix0zhixdBHncYnd5T3CbK0shdSrW4SI3DFOKasgsz0ApP9h7LVZN71oKLVXO6eRP7BQdJRIwq9k9NjZ_QCGMVsjxVHpQN3N6MvkhVy56FzJPz6DOooKJ4_cSof3O1NegI6VW9O_hpSLDFg4dT33WRzpE_1olFSCFBPrfdqnMgVSZnA3nsvsJxxnj6dI7O7rcIiO7mtg8SoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون مهاجم سابق استقلال: دوست داشتم درتیم‌استقلال بمانم امامدیریت هیچ علاقه‌‌‌ای نشون نداده. بارها گفتم برام بلیط بگیرید تا بیام اما باشگاه هیچ پاسخی به درخواست‌های من نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/26973" target="_blank">📅 00:35 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26972">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WL5cLG_bLPcoeNaL20JeE_ADECVbcMcD77h7a1xuxUMRuMBV4l4T9jSjVUSuSqNyi88eioZk6dFSll_C59tfX2_SWTvySjgCX05CWkWXTIL6RV695i3LI61yo8KVEIjJBZFYsu4NJb32jMx31CtbXyhcu4ThDrAAFjiXfZjJ1repL3keQrtqwKC43CZ0CkRr6rTN2ASEu7zEqip6phDF9kqSu9iLw1m_06sQ8dzHPXJWMmOkvOF8QBywqMofDI5o47OIABFPWZk4vB7exadLLMPembDoef15WqR7Xvmge28Eq9FFt-JaZcyK4TaobTOX2BNDx08vUhIoAeLsp6wltQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محسن بنگر کاپیتان سابق پرسپولیس در کنار دخترخانمش؛ دخترخانوم بنگر دانشجوی رشته دندان پزشکی دانشگاه روسیه هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26972" target="_blank">📅 00:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26970">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MkDbxDe54zx5I-K_HlxRZ9SKZQ6_W-mghUAKhPxGZBqwSogCduXX5dpEsSPnGh4jRX4oNmX660e7RbUzBf1Pqp2GtUAcRRkv62Pcf3nhoA15VpAT-99Co_CAM-8wCO4GoL1jVeEakEMGJabByOJHeh9-HbtzTAvP9q_NjX_lHpQ6RYAIda6zp2RG-819_xN8pk4z7keb5xtkwHSed7CR3DYjw4BdxemKqGArvTmjrVmTQ6tqfnELYxMdYXeQEh4AsbB6kBmG6X5YiZOLEURVfA4wwJDVwVgVtb_SSofKnrPRzRtpn_Ol7zU6MgdaoQb4E07efQFfxljezZ4vl6fJMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ital5TOsDxduPjxGmmLGcOa-RYTveXa38kM-5FgLSFgl5TbtJHQvbPZBmPfKcnj-kjbzYuf1PGADECaJ6Nk1PouBTrxYmaLL-GpAW1g9Ch9mPE6L6vpzRODGXRXQNFzONf2uCxsMliM2wLbTCIL9qaahlKSJiVNNhi1zhNTNVbY9Igc2LIurUOGPtOfoZct0st2jPTg1LkQZP_VqUPm7upe07K-aFYpl3A43Vs36_X_bzJVpgn88MsM62YnNiNLugrrCfiJVV9WMF4kqlzqXWEtLL1bkY8azRUt0y_Ejcjq1uLWXch5MO31cItI0rl1u5DK5ibS-YoN-rv1vLvG34g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
دریابنگر دخترخانم 20 ساله محسن بنگر: از بین بازیکنان ایرانی سبک بازی محمد جواد حسین نژاد رو بیشتر از بقیه بازیکنان حال حاضر میپسندم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/persiana_Soccer/26970" target="_blank">📅 23:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26969">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWdGrLVMmIJrr2agskzN5WwebVpGlMteaDLCJxiXQiSt4ut74Fu1HvjWIyDJ9ZrTcdII-B4lWJOVRKIDXxjbpm1VWeYItY2IIwvFZOm-_oyrJYf9rX1sb-pKhnnqMfhzKQUPSFV2MqaWRWVTlik2GDGEoFAAPDMBqMqn-434aL-j6XRiT93HhnW33MGm2xGZ828W8hd0w5xWmCYPNY9c3ogPt86vb-SnmDVUNNquaTvllR-QeY6UaBmSbm_BVn7Q9V2HphfDXMxrWmnZxXxG0mQWYZzHb1bthsyt7tUHNhe_n3MWqnk1GBnywO1ozr-i3T--DzEtqnzJ7UhqMoWT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...با اعلام مدیربرنامه‌های داکنز نازون؛ این بازیکن قراردادش رو با باشگاه استقلال فسخ کرد و‌به‌شکل رسمی از جمع آبی پوشان پایتخت جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26969" target="_blank">📅 23:36 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26968">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaZsNORPHoCmI7Zb0snu3WPOs7RTlnVC1vOf_Z00FYaHJsy8iCCM8DXtf_AX5jJ4nM3kozjcxER1udceUwasJrgVtUbr_cqbf6bwPZ7Kt5MLC_O_c5QflEjtOC2ssT6UCiOHqn6SDBWqOsiDY4mV1SSobulXNTtYUfW3DjrbDKh2_jxpe79HnatHa7SsSx7vAfg3juVAPbk5NbrcjLo7q613CNADiT3AZusaQzTVIjuZLWsXHhkGH1nix8GhwayypQ3AdK60jqAR_-BQt3vPiHZFmAd_fxkL87HBsdv2tuURKMXQTkFI_mKzz1o_QdvU3YaNQGOHstyrWdoz-cdANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق شنیده‌های ما از باشگاه پرسپولیس؛ علیرضا اشرف مدیررسانه‌ای سابق‌پرسپولیس‌بار دیگر به کادرمدیریتی‌سرخپوشان پایتخت بازخواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26968" target="_blank">📅 23:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26967">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ssx0dH2ThkoEW4hlMfkYOZ_kOWd_drOT3KAAz8L7raHkrxzcX3e3sC-BnEXmwkdA4FLXJCkc1V7nyxyT21eQo7cdKsc7ScM0wCX66zBeFXnXyk02gtIuVUZgdYqfMoF5ptzuFpmQHLitUfN1uCGg4UNYpHoffQTD5uW3uz86AFCQ7TlQzXmBQ3ce0ZZn-y5acgQIwRD_OoOTSCVK0mSegz9-dtoB6mDB1YAOHShfgQU76iqwRhJg0F2Ch88pnNztcZQ8wq4arZT7B_WCblD5_Ew7F4sMsRKF3esUZcF7bsknU8GQrJddmO4f9gAJfYNYL2HUeRt4SowBFGeLVuOeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/persiana_Soccer/26967" target="_blank">📅 22:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26966">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIhQNPQ8AhNlGCWH6u04iK2laEut9i5U03cMi9BhTZR71J1jm7oHIzFKL6cyFdV0l3V0uMeqrKMBqJmIYXs2chxn28EWNV4G33YBM0rG6afSqmO4r8UqOMg_dlcuJcyoQxqaHWS5GsdRH6E-JLMb7K-cXVMXM3prdkv_9hLwtuQVfr33023Mz0rmU_0ZZoOJuwc_7x_fsleOqNFpjOoj7wOG0jDJ93ajH2miAagxEvVlhuYfxQtZPqf31H4VZ-wfMK4U26_vK5cJaxuSIco9kfl6WhyB8XFVq30jTeuTrHkaLEtREL5ijf47oPMx4EDHnt6_1oiefkiFOP3_eDJFsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف‌شایعات‌مطرح‌شده؛ باشگاه استقلال تابه امروز هیچ مذاکره‌ ای با آنتونیو آدان دروازه‌ بان سابق خود نداشته و برنامه ای برای جذب او تا نیم فصل در صورت بسته ماندن پنجره آبی‌‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/26966" target="_blank">📅 22:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26965">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgPk1AP9vVRyOevOLxmXgTEmhJCdprgTpCMZSEKNaZZOySgQH-H4JvVfk-PzP9ZsfGDu1UQ-2nJKf9yvAT3LQW9bBs40GFyTKAyf7Akd-j6J4CxEBZavGh_TgjDaEXJFNZTIRsHdHJilTuH7HvoYrq7J-M6ePwwxAg5Gq1HK5L_H_5ZlPxyMrdDhCWYJNHwMobEdj1NQFaQhOSr8wjP1kxSrwXA3bmacU338W2VPLcd5Q_8izPVE6e0BfBI6GUgh7D_3isa2aewq1RhpmpziMO-Ebag379gyANBRSOI9Ls3v4Ih_n41fzXrxWiQLgF44m0zT4mCzFv9stHqcpW4Kww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
تایید شد...زهرا خواجوی دروازه‌بان تیم ملی بانوان ایران و سابق باشگاه گل گهر با عقد قرارداد تا پایان فصل به‌تیم‌بانوان پرسپولیس پیوست. همچنین زهرا قنبری مهاجم تیم ملی نیز سرخپوش شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26965" target="_blank">📅 21:56 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26964">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9YLF9vMbLFFuD8B-m9iDiWKk6uoE5Hm8qxSgJ0KtirpRy0hTNw-94AvtLNXyv9vtdraRnrXSEvbTGn-xFeSbAKkyHGIIv8E_kLNkgoAeu9eWrPR9AupRgeMeojx2P2wVHkDyYAk-XT5ix7AKePfEW_s_9JMKafXSpE2SdmaBhRfKgrDyX8pejijyS-Dh1ZfSSHfFvINcKysP0-AEsBo9n82O8VXR2iEJ0v9ZQB1dk_y0rPly0jMh241Fh-TcLEgt3vdaxJG_GxsTENsutpCDu2XxdDYFL3KOKQ_V6LfJtTbE_tiwnLW1NFoPCdKzuSjb-2TBH4rgCdMiH2TJXkVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدید
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26964" target="_blank">📅 21:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26963">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHRJ3CW0TSRj67wur7Vpl1IZ2ypKpkb07EbieOTxR8HJ2exLhUqtiQpJYhB1f09yXKcl8z0l74wu1tntBq4lDe-VPdVb9TCFqbmVdWi2Zjf7WDNZq8QW15SyNLo3H0oX9XRMY8rsgweD86bL8BFozRi8HuX_rqOE2dOePYa-ywQlu9k-TmT8q8GY1gTOOM5QmuRkdUpx91EdZ2ry71suz8SbHreK_X-waTc5vHRZwMvbVQ-US_urogK2RKdFlj3GociS4t3h0qZTokGy3i9vXWeIxyrdwXO8HCF0z2UJZUpvSQpfqIWsy1mKJfBJGlWL7WVkUlfkjjBVAkyRh6K5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه 3 بازی دوستانه‌امروز رقابت‌های باشگاهی؛ پیروزی اینترمیلان و دورتموند و شکست چلسی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/persiana_Soccer/26963" target="_blank">📅 21:31 · 10 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
