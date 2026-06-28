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
<img src="https://cdn4.telesco.pe/file/VnP8xr8Ny-QGA0GhN77_Sw9J7tY65fzCyMcbaReYguqvlv6v2eS0cpF8UU-zcm-Uvv1D4OjsTZy5ZQ0ZqwQgK1VhcRHhoayr045z7oEMSPdjZFieyZCoKUswco_2W7C4CT958u5h-ZqRkiCvAirHEVNNcLDmQMGJIgVgZmCaRcvuMTdruilEarUF6IYGL4aftOlBIgrlBg3kn8CHOjLLl1fDSmGUejK0i1o1bMGRkm3-itWurDYEBDS1ebRf2d_7Nhaz77w21kpQFDERAwwws50qWKM-wLI8yJjIVG6Or5fpKPVOu9dS4Wog0_PJ8P6mjGEKW2txnuYAfP8TSpkIvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 931K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 00:22:11</div>
<hr>

<div class="tg-post" id="msg-130778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=hZTRtTmBPcnv6_jZO8aptUQ0GQc-62kVdpJtbJCMkyIJcM1tDDxzSJqKgHQ7UM6JcDWH8bCtcRdxrA1Xy-G9w6KQzWErMFpvVL6TCTg7_mf8p7XRWGOlVkAxauRY56GBtnjxemRjoIYTkcr1QCR5CEXMhd0_jQd1qmokmmX9-cl2mN1jj2Gi0fGALePYdmxwyQKf0qAZ99PtYMbKn-EUKAaz8SMg2Y_Wp_D2C_xEuhIQGYxM_EVyRjb1PSm4l9Gj_N_S_QrlXAtA6bunRSLvhKpGP_MYHbjii3MFfx80TQePrkpkGBPa_9KpdPV8rtHVuKKkuvsPyYKd04O635EZBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c35ef3b087.mp4?token=hZTRtTmBPcnv6_jZO8aptUQ0GQc-62kVdpJtbJCMkyIJcM1tDDxzSJqKgHQ7UM6JcDWH8bCtcRdxrA1Xy-G9w6KQzWErMFpvVL6TCTg7_mf8p7XRWGOlVkAxauRY56GBtnjxemRjoIYTkcr1QCR5CEXMhd0_jQd1qmokmmX9-cl2mN1jj2Gi0fGALePYdmxwyQKf0qAZ99PtYMbKn-EUKAaz8SMg2Y_Wp_D2C_xEuhIQGYxM_EVyRjb1PSm4l9Gj_N_S_QrlXAtA6bunRSLvhKpGP_MYHbjii3MFfx80TQePrkpkGBPa_9KpdPV8rtHVuKKkuvsPyYKd04O635EZBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سیل فراوان تجهیزات سنتکام به منطقه
این ویدیو که ۲۰ هزار برابر سریعتر شده؛ خلاصه‌ای از فعالیت سنگین ترابری هوایی آمریکا طی ۷
روز
اخیر در منطقه است که به شدت مهمات جابجا میکنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 15 · <a href="https://t.me/alonews/130778" target="_blank">📅 00:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
تصاویر رهگیری موشک‌در شمال اردن
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/alonews/130777" target="_blank">📅 00:17 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس: مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کردند که حملات را متوقف کرده و این هفته ملاقات کنند.
🔴
یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/130776" target="_blank">📅 00:11 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eef835b390.mp4?token=qGrgD6x3s_WixpRv2DiIReSb-g3Fx6MrmtAFvSyI18zq95o6uQjAwPSOeeACWLlbC6U9QqtdwI-WH_7apRnc1MAMwwk1Ys4fTQxlubQuwSq8jA7vDeM0ktiZiIhteesB9V3vntVNt4Bu0--_GQI6e_ZqmtilRtnlNH4y-kYuXfwfBjTd3Vce6l_ZoCEKZrLbkc2-WxyGDCIyPxHcCo6ugOV9G09NAo6wxNpKfJ27GTEil7lRg6MlcmDm5lXx7nOVKefl8pnwaOyxmUjbOGiXKCzTkFfTITPRqdiB8CMnwSg_S-4nQoD5V5ZnePctVH2tWWCgueXZBNxmJaQkEzghbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eef835b390.mp4?token=qGrgD6x3s_WixpRv2DiIReSb-g3Fx6MrmtAFvSyI18zq95o6uQjAwPSOeeACWLlbC6U9QqtdwI-WH_7apRnc1MAMwwk1Ys4fTQxlubQuwSq8jA7vDeM0ktiZiIhteesB9V3vntVNt4Bu0--_GQI6e_ZqmtilRtnlNH4y-kYuXfwfBjTd3Vce6l_ZoCEKZrLbkc2-WxyGDCIyPxHcCo6ugOV9G09NAo6wxNpKfJ27GTEil7lRg6MlcmDm5lXx7nOVKefl8pnwaOyxmUjbOGiXKCzTkFfTITPRqdiB8CMnwSg_S-4nQoD5V5ZnePctVH2tWWCgueXZBNxmJaQkEzghbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کلیپ لبنانی‌ها تو ۲۴ساعت اخیر تو اینستاگرام عربی بالای ۱۰میلیون لایک خورده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/130775" target="_blank">📅 00:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=lIYYe6HVdZeH-gcCrUj0SDTdFKXl9kSEARz9C7Vqco8TrZEVPBwW_54zHhWSPrmGVkzJvVpk-c2MOUK05HATsHaOkFCFUvOJpEqkZ4Ysn1eMNMC_DpmVA685kQT7Gg0AUNjV8JfoUsL_6g2aoquTT_eRk0zlc2BMEBhtJmptKf6VzCpSuSvt05-HK-LmLvTO2KdwTLdx0fTaxRhiBb726GGqrMVgl2QIMujkW5TwGOmwgTgFrulrvK6X0OUDFTGMhfi2T7buQjTt111n5oyfrnugjWuEPHHA1wkz4unKFJ4vN8aR6yzaVSFNiWhmU-4tzvwq9QVPCbsP-A98lrJswg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=lIYYe6HVdZeH-gcCrUj0SDTdFKXl9kSEARz9C7Vqco8TrZEVPBwW_54zHhWSPrmGVkzJvVpk-c2MOUK05HATsHaOkFCFUvOJpEqkZ4Ysn1eMNMC_DpmVA685kQT7Gg0AUNjV8JfoUsL_6g2aoquTT_eRk0zlc2BMEBhtJmptKf6VzCpSuSvt05-HK-LmLvTO2KdwTLdx0fTaxRhiBb726GGqrMVgl2QIMujkW5TwGOmwgTgFrulrvK6X0OUDFTGMhfi2T7buQjTt111n5oyfrnugjWuEPHHA1wkz4unKFJ4vN8aR6yzaVSFNiWhmU-4tzvwq9QVPCbsP-A98lrJswg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/130774" target="_blank">📅 00:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130772">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7lWAWzUzaTmxaV6uhX1kF5ahbojgG8CtASzOUU7g5c_sfxfU19l-qsXVNNs_a_s6G0PIat-rUAoz1LbEcfr_reLFXrFIH4cr-7k6zeVHI3nOB03QUS8cvEGvcR_NyYgPHPDkuVlnSExyTsseFo1IVT79wHqtKZ4f7D9O43ISQpVx41qvXOP4Igoob_JgURzHaxQXQihlkLR71oy95aKbUl_c-OjldJkC2AVxeZ5XW9zHRrGkSvjDdrYH6YBdu7fkD75LWouDe1m38Ys6oFM7QD0NMj6mLPqZA43m24xWjiPGhZRhMXwiYFHbYnW_ViWOfWFhhhHYQiZ0-RHQyTAVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید خبرنگار آکسیوس: مقامات آمریکایی به من گفتند که ایالات متحده و ایران توافق کردند که حملات را متوقف کرده و این هفته ملاقات کنند.
🔴
یک منبع آگاه از مذاکرات گفت که قرار بود مذاکرات سه‌شنبه در ابتدا در سوئیس برای رسیدگی به برنامه هسته‌ای ایران برگزار شود. تشدید تنش‌ها آنها را به مکان دیگری منتقل کرد و دوباره بر تنگه هرمز متمرکز شد.
🔴
به گفته یک مقام آمریکایی و یک منبع آگاه، انتظار می‌رود نیک استوارت، که ریاست تیم فنی ایالات متحده را بر عهده دارد، در این مذاکرات شرکت کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/130772" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130771">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚀
اگه واسه کانالت دنبال
ممبر، سین، ری‌اکشن اتوماتیک و حتی کامنت با هوش مصنوعی
می‌گردی ارزون‌ترین ربات
کلیکو
هستش
قیمت‌ها عالیه:
سین کایی ۵۰۰
ری‌اکشن کایی ۲۵۰۰
ممبر از کایی ۵۰.۰۰۰
⚡
تحویل سریع
💰
قیمت تضمینی
🤖
ثبت سفارش خودکار
👤
پشتیبانی 24 ساعته
لینک ربات
👇
👇
✅
@ClickooBot
🤖
✅
@ClickooBot
🤖</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/alonews/130771" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130770">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه:
روسیه منتظر ورود مذاکره‌کنندگان آمریکایی پس از اتمام «فاز داغ» رویدادهای مربوط به ایران است.
🔴
لوکاشنکو به خاطر اظهارات تند زلنسکی دچار وحشت نشده است
او با آرامش و تعادل بسیار به این موضوع نزدیک می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/130770" target="_blank">📅 23:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130769">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZO6OV7xO_hsluD77g2AInU99-hZ5IKxQ6Degc3YJ3Kl0cX5AC6Z_rd0X-AXY1RLMhWp6iJp5RtFlzQWrSQldiQ-OqIj6AXhx9js_KbmUHwI4uiIBR0-LlXxEW5UJ0PYDuC_FVsDWXobsyYuHtp-Keq_1vni0ECfbS46QPez0naP9_XSqRw17RXGG8HRQ2-kIZSfdj9wdmB5YZm7pnbzoSz3Y2WFt19DEnDlGWFgzZGFO5yxfzw18eMIj8Cjmt3QNr2w-fi7NKeq76BRp3KXx-p8vAsIzkSSKhth9tVylfxoVEyFM59wV5GVT8iCu0pqxSPCdM-YkgZqiPvBV2E-_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اسرائیل در حال گلوله‌باران توپخانه‌ای و حملات هوایی به منطقه عابدین در جنوب سوریه است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/130769" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130768">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ارتش اسرائیل امشب عملیات تخریب گسترده‌ای را علیه «زیرساخت‌های زیرزمینی حزب‌الله» در شهر مجدل زون در جنوب لبنان انجام خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/130768" target="_blank">📅 23:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130767">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pA-uHsRRj1rIZt3YEFaSPB_6mg-LfCJbAlL963_GbMAEzCcK4_KTpGJCEbYVc0UGoX4kKSHaNj-3FF6o2ZVwHha-PXy3pLx159txTqgxTLoghsGb-inBzEvV8tk2PwKpwnUCYsMb8iYtzs4oHdqOYJ0tV2fjGhlYfYFmfNC8__huX-bNr7aqbXByOJpjJN6M5vFCEsF7qf9J0DsCA0xWJqNCRNguGnI33pNmMopeQuXaBwsCua_Bw-MJH10e3UJqatfg4bW1snHj4u2naK9_8pqA5rk1lE80rmr7R8VJQxMRjKNj7xUefa1sGfVG8H4gZV6PPHa-XI8T_PXjGFt4ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویر رهگیری موشک‌در شمال اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/130767" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130766">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ارتش دفاعی اسرائیل امشب تخریب گسترده‌ای از «زیرساخت‌های زیرزمینی حزب‌الله» در شهر مجدل زون، جنوب لبنان، انجام خواهد داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/130766" target="_blank">📅 23:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130765">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🔴
میساکی باز هم توهین کرد: کسایی که برای خوشحالی گل شجاع کلیپ می‌سازن همون جای خالین @AloSport</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/130765" target="_blank">📅 23:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130764">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
یک مقام ارشد آمریکایی به الجزیره:
کانال‌های رفع تنش با ایران همچنان برقرار و فعال هستند
🔴
گفت‌وگوها با ایران لغو نشده است
🔴
مذاکرات فنی برای اجرای تفاهم‌نامه با ایران همچنان طبق برنامه قرار است در روزهای آینده برگزار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/130764" target="_blank">📅 23:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130763">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803cd79e57.mp4?token=swamobLQV94Mbv43gKBj8sAK9KrDfmrS_eynQcm9wXEKfTnEaPmO4bcTr0cprLWIBjB9xQcBuhRqyNUYMntM4YLqR7UEEpb_pYCioPNFMYC6JIY0IdaVsBPElXiOPJZ368PZMlB_-4pFX0wyiVz0jJi61MFStfTQMt262S_sl3ojhljyiIWcaFVPEKUiRcBYOTfuoQBwreP_stUNTuSjrpbQLhe9q6rmIt2SWDhLldRgRpxssRQXkn-83m2Pcye9djh8z4d0GmK2elBLhKeeHlMYWTXrSxouhScHwN_Bm--6m8tWPEccGZsygmt7JsxGffHISBNeAKa_OwUJ2RI-Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803cd79e57.mp4?token=swamobLQV94Mbv43gKBj8sAK9KrDfmrS_eynQcm9wXEKfTnEaPmO4bcTr0cprLWIBjB9xQcBuhRqyNUYMntM4YLqR7UEEpb_pYCioPNFMYC6JIY0IdaVsBPElXiOPJZ368PZMlB_-4pFX0wyiVz0jJi61MFStfTQMt262S_sl3ojhljyiIWcaFVPEKUiRcBYOTfuoQBwreP_stUNTuSjrpbQLhe9q6rmIt2SWDhLldRgRpxssRQXkn-83m2Pcye9djh8z4d0GmK2elBLhKeeHlMYWTXrSxouhScHwN_Bm--6m8tWPEccGZsygmt7JsxGffHISBNeAKa_OwUJ2RI-Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صحنه‌هایی از میفدون، جنوب لبنان، پس از یک حمله هوایی اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/130763" target="_blank">📅 23:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130762">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40133fcdb1.mp4?token=enzBc4UZjjp-1FHuOKUyAHXf-eXi8WtHt5avwGId9EXmFwP_WP7U8buk3pfM3tDmD9ZVcV9QyUa-SfV4K1G-_YckFFoDsE0QDgNyIdST96Pbab2TswBqHA7rL4iX3WP1uqRH2PSZQOnW5KVDrgusNQmR5IFKL9b3RHZex62oYcoa6ls8qULAGCGu6v2Ykq2Ln0hcOHhEHKBtsEW_sHH4iqhZDQSzvKJrcSy6nWpe4H6-5gGCY819_VHrQ8QujOArs1hQRE6A-jYL9q_omh7j_k6qk9Fsu-bDusowWSk4sXdcKCBecf3Lqv8qQsGpxD9qRMx7smJt2S7QS8Ts4oglN3cfOUi8YVriR5llU5ZmRLDTuAEM3pKrgXemNWyJDS1_-cK0nn2DrSDFQ87lOND2O3O_-Peh9mGjNE_pv4j3z3jJHz-wwUOTYsb5Au-NzkJeVckYzdoPeO42tNfUuauq8PvvnGWYSUmFL-N3CvAttycPuqHrNRVyFT7mLoc2Ze3P_qP1qhGxrzAZubkIF1b8g3GWMv78T55ck5d3VU8vGgn9gBgmi6j3lcmk-oMTszNdEVbDgkqSliC8SPnblEV-NzM1YjZA1IKv7QVsuGH5NenElentEyEmaXEqISI3OEglWU-jAi62jQZ2o9Tei6BUdAHgvi0MNqX7PfKmbvf8G7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40133fcdb1.mp4?token=enzBc4UZjjp-1FHuOKUyAHXf-eXi8WtHt5avwGId9EXmFwP_WP7U8buk3pfM3tDmD9ZVcV9QyUa-SfV4K1G-_YckFFoDsE0QDgNyIdST96Pbab2TswBqHA7rL4iX3WP1uqRH2PSZQOnW5KVDrgusNQmR5IFKL9b3RHZex62oYcoa6ls8qULAGCGu6v2Ykq2Ln0hcOHhEHKBtsEW_sHH4iqhZDQSzvKJrcSy6nWpe4H6-5gGCY819_VHrQ8QujOArs1hQRE6A-jYL9q_omh7j_k6qk9Fsu-bDusowWSk4sXdcKCBecf3Lqv8qQsGpxD9qRMx7smJt2S7QS8Ts4oglN3cfOUi8YVriR5llU5ZmRLDTuAEM3pKrgXemNWyJDS1_-cK0nn2DrSDFQ87lOND2O3O_-Peh9mGjNE_pv4j3z3jJHz-wwUOTYsb5Au-NzkJeVckYzdoPeO42tNfUuauq8PvvnGWYSUmFL-N3CvAttycPuqHrNRVyFT7mLoc2Ze3P_qP1qhGxrzAZubkIF1b8g3GWMv78T55ck5d3VU8vGgn9gBgmi6j3lcmk-oMTszNdEVbDgkqSliC8SPnblEV-NzM1YjZA1IKv7QVsuGH5NenElentEyEmaXEqISI3OEglWU-jAi62jQZ2o9Tei6BUdAHgvi0MNqX7PfKmbvf8G7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین: ایده ممنوعیت کامل صادرات سوخت دیزل در حال بررسی است
🔴
اوکراین چند هفته‌ای است که به صورت سازماندهی شده به مخازن سوخت روسیه حمله می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/130762" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130761">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8RNRIDI_MxKEHFvyGdqT7SXE0A8McWG9OBl-MwNbO-w_3M4xH1HyYSR_lpOokxuPze36bSs91YQIe32V6zMmEX8Tq0m3V_AS9W9drRiggA4YPaPDEI1eJ4fslik-eLgmTiNGUn48AGmQUGBYbOt6pgNbZUouOteJjN9kAeMdO805TvyVDMsIDw0HTYdiuiT09nYbFXnk1P0vhRhMvq6YGBJ1pckEdVh0SJoIGs-zDxKoZXYlOAEFHAzPaMfBaX6rGMcLAXlZ-Lc6ZTYM0EsoLqNmKWmlhYfsdCyFpJVoCMbaaXzygDFGy5eaLzTDoiMuE5lOY_iyBJ2atmNmHy2Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندی پیش حملات هوایی اسرائیل به میفادون و نبطیه الفوقه در جنوب لبنان انجام شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/130761" target="_blank">📅 23:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130760">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
آتش زدن نمادین متن تفاهم نامه توسط یک مداح تندرو و جنگ طلب
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/130760" target="_blank">📅 23:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130759">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
فضائلی، عضو دفتر حفظ و نشر آثار آیت الله خامنه ای: امروز قرار بود مذاکرات فنی برگزار شود که ایران آن را لغو کرد و شرکت نکرد که دلیل این امر درگیری‌های این چند شب گذشته بود و دلیل دیگر این است که منتظر اجرای برخی شروط هستند که مثلا امکان برداشت پول‌های بلوکه شده است یا خیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/130759" target="_blank">📅 23:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130758">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فوری / نایا به نقل از رسانه های سعودی:
رهگیری موشک ها بر فراز شمال اردن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/130758" target="_blank">📅 23:13 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130757">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
طبق اخبار و تحولات موجود، بزودی جنگ آغاز خواهد شد مگر اینکه اتفاق دیگری بیوفتد
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/130757" target="_blank">📅 23:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130756">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
منابع خبری از حمله هوایی جنگنده‌های اسرائیلی به شهرک «میفدون» واقع در جنوب لبنان خبر دادند.
🔴
تاکنون جزئیات بیشتری درباره تلفات یا خسارات احتمالی این حمله هنوز منتشر نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/130756" target="_blank">📅 23:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130755">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیویورک‌تایمز: مذاکرات لغو نشده است/ روزنامه آمریکایی به نقل از یک مقام بلندپایهٔ آمریکایی مدعی شد که مذاکرات فنی با ایران در خصوص چگونگی اجرای تفاهم‌نامه، کماکان برای روزهای آینده برنامه‌ریزی شده است. وی با اشاره به تبادلات آتش اخیر میان ایران و آمریکا تصریح کرد که هیچ گفت‌وگویی لغو نشده و ارتباطات همچنان برقرار است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/130755" target="_blank">📅 22:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130754">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پوتین: نیازهای سوخت کریمه برآورده خواهد شد و در حال حاضر چند روز ذخیره سوخت در آنجا وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130754" target="_blank">📅 22:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130753">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پوتین: حمله‌ها به زیرساخت‌های انرژی روسیه باعث ایجاد مشکلات می‌شوند — این واضح است.
🔴
کمبودی که از حملات نیروهای مسلح اوکراین به زیرساخت‌های انرژی روسیه ناشی می‌شود، وجود دارد، اما حیاتی نیست.
🔴
تمام تأسیسات انرژی آسیب‌دیده در روسیه به سرعت در حال بازسازی هستند و همه چیز با حاشیه ایمنی بزرگ در حال کار است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130753" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130752">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4fcf308f.mp4?token=LM4k3KAcSPJASVAIMhALLeitKbrx_Wyg1t8eUb3hjwUL5RuIHBNGMhgryok5yPQ4-Dpo8vcuKRL6KFBWuXQTbu8DzVp77DSTTanik-suGLCdNcJMRw03HvZtRCHib-cnDv6pXHvwvOwlzbQG4CPC4N6L5GNK7xo2m7J_aeZPomFREJZskShRjeJRLo79m-qzi70rHgDhGB3JLnQu43ASPl39Ne-n1Jkrq_4rYPw7SgnKTcXZq67enUK4pQLgEU9gSUwBguiU39O9fHcdckmmg5Fb6KbhxoAC4tnV-ndBlZbD9Z2BU4DO_Ow07bEgf-dua8hRRpSIi1uNHFuYaV2pPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4fcf308f.mp4?token=LM4k3KAcSPJASVAIMhALLeitKbrx_Wyg1t8eUb3hjwUL5RuIHBNGMhgryok5yPQ4-Dpo8vcuKRL6KFBWuXQTbu8DzVp77DSTTanik-suGLCdNcJMRw03HvZtRCHib-cnDv6pXHvwvOwlzbQG4CPC4N6L5GNK7xo2m7J_aeZPomFREJZskShRjeJRLo79m-qzi70rHgDhGB3JLnQu43ASPl39Ne-n1Jkrq_4rYPw7SgnKTcXZq67enUK4pQLgEU9gSUwBguiU39O9fHcdckmmg5Fb6KbhxoAC4tnV-ndBlZbD9Z2BU4DO_Ow07bEgf-dua8hRRpSIi1uNHFuYaV2pPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ولی ما میدونیم چرا!</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130752" target="_blank">📅 22:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130751">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
یک مقام ارشد دولت ترامپ امروز به رسانه‌ها اعلام کرد که مذاکرات میان آمریکا و ایران که قرار است آخر هفته جاری در سوئیس برگزار شود، همچنان طبق برنامه انجام خواهد شد.
🔴
این اظهارات، گزارش پیشین روزنامه وال‌استریت ژورنال را رد می‌کند؛ گزارشی که مدعی شده بود این مذاکرات به دلیل دور جدید حملات متقابل ایران و آمریکا در منطقه خلیج فارس به تعویق افتاده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130751" target="_blank">📅 22:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130750">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6cf47261a.mp4?token=AuFOgc0cSyQIE1TbFSLhNglql2-M6CwLDH9vKZz1oAdxrkbiXoyt0_PZ1AsCxGlHyoorIQALW2wSTf83JiWBTX_KZRPrYGfczAq0JAIwzhflaemRNx0trTDBTmZeGjJ0ZjFTvAp9Mx9SgaqZdm_TQ5qZyRfy9DUY9QXFx8qLzDnLKcsIW3BafO1VPvNwFw6sGrp5xkX_x0VCUNlU_TkYWe5_ZknfxHeeg118kKesvYlQlrsb2scPaj9QAZ76NT1ZpyzQL76ef_msOCD4BQkf3wbG9tk2ipCd6yu1puNIYvFQQ61s4ein11Q2Iu42NPyCJO2gnG-msYF0IW3WSpmX9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6cf47261a.mp4?token=AuFOgc0cSyQIE1TbFSLhNglql2-M6CwLDH9vKZz1oAdxrkbiXoyt0_PZ1AsCxGlHyoorIQALW2wSTf83JiWBTX_KZRPrYGfczAq0JAIwzhflaemRNx0trTDBTmZeGjJ0ZjFTvAp9Mx9SgaqZdm_TQ5qZyRfy9DUY9QXFx8qLzDnLKcsIW3BafO1VPvNwFw6sGrp5xkX_x0VCUNlU_TkYWe5_ZknfxHeeg118kKesvYlQlrsb2scPaj9QAZ76NT1ZpyzQL76ef_msOCD4BQkf3wbG9tk2ipCd6yu1puNIYvFQQ61s4ein11Q2Iu42NPyCJO2gnG-msYF0IW3WSpmX9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل:
اگر ایران فکر کنه ترامپ قراره در برابر ادامه حمله به کشتی‌های بین‌المللی دست روی دست بزاره، کاملاً در اشتباهه؛ چون همین چند شب اخیر نشون داد که این کارها رو بی‌پاسخ نمی‌ذاره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130750" target="_blank">📅 22:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130749">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آکسیوس: آتش‌بس شکننده ایران و آمریکا در معرض فروپاشی قرار گرفته است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130749" target="_blank">📅 22:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130748">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uci_js3Zcur-GSveni2A-1LyaDuCW82lI5iLc5JqJYQ8Id_UMl48uNhreekC0Gen2ZB_YoJIScoKLcRfG7J3dD_Zm0GB07h_drMRZn5lDx7oPv0dZCHsyiy3kG_eddyzUi94BDUvaIrumBLAYCCTfes2FFLGoTMVtGrCdT0ZFvDOUq6PjcVtzZnL-T1uPtn5F3J5ipHCIUl6hkFcfreweOBXyL4zq2VlcMFTdjZ43rPnd8bbVd1umQAL9NIxUY7rtnUDtcHcPcfjaJSbm1TEqKBteklRGXlgixQK6xgGJPPJrigMz3mY5AJQ5KRZmAKXjZznZvMH0XL_dnMOq8juxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوسان قیمت تتر در ۲۴ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/130748" target="_blank">📅 22:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130747">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96c68e7570.mp4?token=IP6XvOEOQioNN7LFm0oRBtnXD8drjhdbrAEBlCIACzX6DVKI2v5Es2XdnieaX7QJh8I3uwP5SLExamprOGZgor31IMdum9FyXCPnIMXhVDn-ov8YCaMgvCPvQiiDwhcy6cpATP4bpFkKNv40RNUEyMnc1q0N_4Lv5Oh12efdTQ2W2Zd-VwHiW_eCPFviv7EmX7hN9mD8byGGf8itpsbAiULD1dTRhwPSXC0qY5UsrDgctjEyXrP4PUuxEyN-rP1oaSh2XdjLwOjedBkucwoFLMGeSL05oJoPZ5gc81bKWJr-MlBTHHqcktU1OI9JoFXxQy8oLxijRiCOnZcm67CjQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96c68e7570.mp4?token=IP6XvOEOQioNN7LFm0oRBtnXD8drjhdbrAEBlCIACzX6DVKI2v5Es2XdnieaX7QJh8I3uwP5SLExamprOGZgor31IMdum9FyXCPnIMXhVDn-ov8YCaMgvCPvQiiDwhcy6cpATP4bpFkKNv40RNUEyMnc1q0N_4Lv5Oh12efdTQ2W2Zd-VwHiW_eCPFviv7EmX7hN9mD8byGGf8itpsbAiULD1dTRhwPSXC0qY5UsrDgctjEyXrP4PUuxEyN-rP1oaSh2XdjLwOjedBkucwoFLMGeSL05oJoPZ5gc81bKWJr-MlBTHHqcktU1OI9JoFXxQy8oLxijRiCOnZcm67CjQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه نفر GTA6 رو پیش خرید و دانلود کرده، این به کنار، 175 گیگ رو تو فاکینگ 10 ثانیهههههه دانلود کرد
😐
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130747" target="_blank">📅 22:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130746">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🔴
یکی نیست به طرفدارهای تیم جمهوری اسلامی و رسانه‌های همیشه‌طلبکارش بگه حالا که افتادین تو فاز «تبانی شد که تیم‌مون صعود نکنه»، اول یه نگاه به خودتون بندازین.
🟠
تیمی که سرنوشتش رو می‌ذاره دست نتیجه بقیه، حق نداره بعدش برای دنیا مظلوم‌نمایی کنه. اگر عرضه داشتین، تو زمین کار رو تموم می‌کردین، نه اینکه بعد از حذف شدن دنبال سناریو و توطئه بگردین.
🤔
به بدترین شکل حذف شدین چون دعا یک ملت باهاتون نبود.</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/130746" target="_blank">📅 22:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130745">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/s3a8-BTr77fBFJ0RJim1sfNfMzuU1mRLzGJdmVVnr1zRskt_oEHffJSRiwGQYNgKjpshW0o30nYJLMLGowBnktuUUq_fAeMUPuJRo0yQ9SVgz8ZLyVDkfiwVOsrXLFBXT9WYSnP6tZZjA30LgDGiX9FQqsZ3rqmqPhwXs4sR8SwTkxDIbJuYgLV8x7uKfab0hsCSFvVFanXgysvwTv8I6wGp9kcv_99L3lucvBKIcOHzc_Udf1jDZRFWCAITh1FwkIr5jLksKINFd5wxWYua5asjFl0LAkviLlBcIyL4dzx2ay0X5B4e0ltNvphy4SJYjqBcz2adnAVLVs2jmWCykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدول بیشترین شانس قهرمانی در جام جهانی ۲۰۲۶
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/130745" target="_blank">📅 22:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130744">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
والانیوز عبری:
اسرائیل در حال آماده شدن برای احتمال حمله مستقیم ایران است، پس از امضای توافق لبنان و اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/130744" target="_blank">📅 22:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130743">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63c51b823e.mp4?token=KF9ZLbuQyy5I_hPK5c6T845jxHamvigKSBevyaEoGTWhUYxhZCLTVnxb18RpRfLDzCbBhdyJIC-zSwwF-NZ4jurRCYw9piCC7BKba-VvGFttAoIiJ9TfBewPeddc4QC1vjMjd6KATLsouDg5DpfqZtjN9NoFG5CyDKi1eRA7O0tdQnfsfYfaNAOOBix9B_utv-qIVIEdF9--8xm2VjQ8tcOL_iDU2tzbs0WbmRMX7bsEq8fFzRjLGv_p6lz6GuKYqJMCUcXFjE_YLFfzokSvlp6PHuNBluKEYB2RknCZEbhfMaElwxtVhYHcFUgI9i3ydIYu3hkzxSR9g2JT-cvlEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63c51b823e.mp4?token=KF9ZLbuQyy5I_hPK5c6T845jxHamvigKSBevyaEoGTWhUYxhZCLTVnxb18RpRfLDzCbBhdyJIC-zSwwF-NZ4jurRCYw9piCC7BKba-VvGFttAoIiJ9TfBewPeddc4QC1vjMjd6KATLsouDg5DpfqZtjN9NoFG5CyDKi1eRA7O0tdQnfsfYfaNAOOBix9B_utv-qIVIEdF9--8xm2VjQ8tcOL_iDU2tzbs0WbmRMX7bsEq8fFzRjLGv_p6lz6GuKYqJMCUcXFjE_YLFfzokSvlp6PHuNBluKEYB2RknCZEbhfMaElwxtVhYHcFUgI9i3ydIYu3hkzxSR9g2JT-cvlEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلم‌ پهپادی از خسارات گسترده‌ در لا گوئیرا در ونزوئلا پس از ۲ زلزله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130743" target="_blank">📅 22:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130742">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668abf668f.mp4?token=v_IcREru13eEpKFNLc5hV48Cxnb6NrrbRUWIcnn4-Jb7338sQC1-zR6qBWUOSikagmPI37TrycqeyamjRXVODPV02Ayv6Gm8athQbc-AF_GCJzb1w9AHv3Y_sL1gxMvcXRBoOmgp2Z5YHGL-XJyEt3ANc2044d2dLzczfog5ixLtcn4VynihbADjjq5eyfeycaqlTPeyOozuJ0STsd_VDKSUkA_lofwVXhiw7nPXf92HvqO-mVoMXog4FAh3uJD6FF31WUeCYd7NDbUHnn8vohaDngd6LQOsxLX4SRW-izaeKe6kG7PR4Rl7JJN3q5GCoqN0-f6jlTjW27q3qUdK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668abf668f.mp4?token=v_IcREru13eEpKFNLc5hV48Cxnb6NrrbRUWIcnn4-Jb7338sQC1-zR6qBWUOSikagmPI37TrycqeyamjRXVODPV02Ayv6Gm8athQbc-AF_GCJzb1w9AHv3Y_sL1gxMvcXRBoOmgp2Z5YHGL-XJyEt3ANc2044d2dLzczfog5ixLtcn4VynihbADjjq5eyfeycaqlTPeyOozuJ0STsd_VDKSUkA_lofwVXhiw7nPXf92HvqO-mVoMXog4FAh3uJD6FF31WUeCYd7NDbUHnn8vohaDngd6LQOsxLX4SRW-izaeKe6kG7PR4Rl7JJN3q5GCoqN0-f6jlTjW27q3qUdK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤴
تو این روزهای فوتبالی یادی کنیم از  افتتاحیه استادیوم «آریامهر»
🤔
اون زمان کشور های حاشیه با شتر اینور اونور میرفتن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130742" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130741">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcTHJyjjVCCGrkm9ZwrWctyPMNEzQg8Xhx67jJts6_IA3uJUolOLGifS2U_IIQmRXUNh1m7shPAA6BddiJzssJIQ8_TigKnPxmX1O7HjHIByc2jt3Gbz7En_KoqgvMdSjvydm95YwxxdWg6Ew3__1F-jXcZpF2XUnNZe5er0DYe5SGzvJmDaXZgNBFEVjIJE-a3mUNzzp-VijJ9lr2NxWjve2DL3OynQhulEDZK2paEScY88SabyA51e-fDeTpbG3vss-ZAlNuROUjsuFVAWCh_aDnIeGqLH9D8y8jfRy0MS02MwkmvyU3edqz9nf1u0HizM5xR22nsnJHRMxLsq9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت و عملیات پر شدت هوایی بر فراز منطقه خلیج فارس
🔴
از آواکس آمریکایی تا تعداد قابل توجهی سوخت رسان و جنگنده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/130741" target="_blank">📅 21:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130740">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
منابع عبری : افزایش حالت آماده‌باش در اسرائیل به دلیل نگرانی از پرتاب موشک از ایران به سمت اسرائیل
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/130740" target="_blank">📅 21:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130739">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qo7hEY4SmAP2ZFFFSs1367L-qLPYW1eiNBROJFBpvhRrehOjIasSMvGI1V21AFwpCZMKRyp3KFk37reAcdvKdct40oCY6ARShZZwMhXVhxymo13u5JoFaR0KaKIZyWhyBervPI25fwF0ET4-YalTc8lTibTKIxrhJNu-Detb5rvZZGX1F5k_pHa64nztf6Ip3RhJBjqUlGMNUP1mXFz-s5o7_QGF0KUdgYbYSwcgBdnVUYl7czaQdYJxinUHJVWUzmQ_jMZTO7qZzCk79TgUIzqeCIgrlD04X4M-jeGthEhu6i40bVBwGym92omofDwB6tj68pUu3lhuadeBM6cVWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس :
آتش‌بس بین ایران و آمریکا می‌تواند نابود شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/130739" target="_blank">📅 21:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130738">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908ea40def.mp4?token=fdbZZuZJoxc9I2uvMfxAbUFbOG7rD20Hi-YvcBUPhn80lGSGU_Rle7SfayCtryuTDjduzEaiPDk9-Pw591p_PVRVVMhEbpZH0-c7GFrVp_-WcCetb6DTAjswxKMNjbyCAZYy4q1os-ACQFkklw3OeQd-qaX3wh8iVPmlfoPbDNo5qXdH-AR0zWLbJNKgGDoT8i1PaZeSXITYdzhgqkEfKpG4c4zbNyTzNSl10b9Us07q5St9YdHb32eJgDyGCjWuiMAFau56KxxE3sqfTDcUCMeRHPvYGHMpTpdJH5mnnVfhhGYknzPygVosWfrq2jECtJaPi1YM2ncNTyO1mDaNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908ea40def.mp4?token=fdbZZuZJoxc9I2uvMfxAbUFbOG7rD20Hi-YvcBUPhn80lGSGU_Rle7SfayCtryuTDjduzEaiPDk9-Pw591p_PVRVVMhEbpZH0-c7GFrVp_-WcCetb6DTAjswxKMNjbyCAZYy4q1os-ACQFkklw3OeQd-qaX3wh8iVPmlfoPbDNo5qXdH-AR0zWLbJNKgGDoT8i1PaZeSXITYdzhgqkEfKpG4c4zbNyTzNSl10b9Us07q5St9YdHb32eJgDyGCjWuiMAFau56KxxE3sqfTDcUCMeRHPvYGHMpTpdJH5mnnVfhhGYknzPygVosWfrq2jECtJaPi1YM2ncNTyO1mDaNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میساکی باز هم توهین کرد: کسایی که برای خوشحالی گل شجاع کلیپ می‌سازن همون جای خالین
@AloSport</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130738" target="_blank">📅 21:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130737">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">حذف شدن تو یه مسابقه میتونه طبیعی باشه اما زجرکش شدن قبل حذف یعنی اینبار اسلحه دست خدا بوده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130737" target="_blank">📅 21:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130736">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دنیس راس فرستاده ویژه آمریکا برای خاورمیانه در دولت‌های جورج بوش پدر و بیل کلینتون: ایران در تلاش است «مدیریت» تنگه را به اجرا بگذارد. تنها دستاورد ملموس تفاهم‌نامه، بازگشایی تنگه بود که در ازای آن ما محاصره را لغو کردیم و به ایران اجازه دادیم نفتش را به دلار بفروشد.
🔴
می‌توانیم به تبادل نظامی ضربه در برابر ضربه ادامه دهیم یا محاصره را دوباره برقرار کنیم. گزینه دوم را انتخاب کنید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130736" target="_blank">📅 21:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130735">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
منابع دیپلماتیک به روزنامه الجدید لبنان گفتند ایران چارچوب توافق اسرائیل و لبنان را به رسمیت نمی‌شناسد و می‌خواهد اسرائیل را مجبور به عقب‌نشینی کامل کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130735" target="_blank">📅 21:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130734">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: دولت لبنان از واشنگتن خواست که پیوست امنیتی مخفی را در چارچوب توافق با «اسرائیل» منتشر نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130734" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130733">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1janjqzfmAn0ahy2cO31dLXUd6EH0YfTmNhUVgECiyeD0MXWU-bcQ2o4rDsqplfR_hrEVmnLndqSVaG7cCe7qfJ8K9bNbi5maalGz6Vc-ZKznX7WjpLY9WAeINYwT8umb3bJA0rM2N1wcy-T3eVfoN-Kpp_xIVpn11vj9wCx_PMCrSAbe_j1gyMnJScKYhfHiLa9tATy1d9zTzqRriM9kmkQoTsbGhx4tjIKv-6VNZSF52vCu9vU55GA3-zsPm5SoFPJrhjb_hY6s-XfvK0625uIMgro9qpqQ9Uv8Enr-43F9eBV0Ob2JElh5YiU-OEzwXhIt2K-_vBlOrkwx6C8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت کشور قطر اعلام کرد تیم‌های جستجوی دریایی پس از عدم بازگشت یک کشتی در زمان مقرر در این آخر هفته، آن را پیدا کردند و تأیید کردند که یک شهروند قطری پس از اصابت ترکش از «عملیات نظامی» در منطقه کشته شده است
🔴
یک ساکن عرب که در کشتی بود زخمی شده و در وضعیت پایدار به بیمارستان منتقل شده است
🔴
مقامات تحقیقات در مورد این حادثه را آغاز کرده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130733" target="_blank">📅 21:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130732">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
ایران هر شب حداقل شش پهپاد به سمت کشتی‌های تجاری در تنگه هرمز پرتاب می‌کند که برخی از این پهپادها توسط ارتش آمریکا رهگیری شده‌اند، طبق گزارش i24NEWS.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130732" target="_blank">📅 21:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130731">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
بلومبرگ: تلاش دولت ترامپ برای لغو دهه‌ها تحریم، به‌عنوان بخشی از توافق برای پایان دادن به جنگ با ایران، شرایط سردرگم‌کننده‌ای برای دولت‌ها، بانک‌ها و سایر شرکت‌ها ایجاد کرده است، زیرا آنها با ترکیبی در حال تغییر از مجوزهای جدید و محدودیت‌های قدیمی دست و پنجه نرم می‌کنند.
🔴
پس از انقلاب ۱۳۵۷، ایران به دلیل برنامه هسته‌ای و حمایت از متحدان منطقه‌ای، به یکی از تحریم‌شده‌ترین کشورهای جهان تبدیل شد. اما کاخ سفید اکنون در حال طراحی یک تغییر موضع شگفت‌انگیز، به‌عنوان بخشی از توافقی گسترده‌تر برای باز کردن تنگه هرمز، کاهش قیمت‌های جهانی انرژی و پایان دادن به جنگ نامحبوب خود است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130731" target="_blank">📅 20:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130730">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
خبرگزاری فارس: ایران در دوران گذار به نظم جدید جهانی، چاره‌ای جز ساخت بمب اتم نداره تا گزینه نظامی علیه کشور از روی میز برداشته بشه.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130730" target="_blank">📅 20:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130729">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cdad75e45.mp4?token=QY6GFZGrrtYne78x-GTwbw070ar899iE80mV4yeZd48gtz9oFSIEd7ZDAhozIrnPmSgdK6I9-K42RPvJ5h61venqsTUpmWh6zDF2Sq0Ty7x1m9OXd4u2MYBjBiF8qMyoTBDZAeu5W4gnfK9bGYX1iCacQh9SOR90rP8YrtagN54XQxpWlft-jJukv40WOUcFtJpL0WlEATUf81uAfl5zRBQf7nojYseRuxoplZiyonNokRdVS3P2lNYuYfRcBeKsSZh6QxzeUTgpal5Kbtvm5ADjUuUSySwkFHSiQioTBvFw9wfyNsYzUIYbeh-WkpzxWwHOVp80M6q56jRP-xK3GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cdad75e45.mp4?token=QY6GFZGrrtYne78x-GTwbw070ar899iE80mV4yeZd48gtz9oFSIEd7ZDAhozIrnPmSgdK6I9-K42RPvJ5h61venqsTUpmWh6zDF2Sq0Ty7x1m9OXd4u2MYBjBiF8qMyoTBDZAeu5W4gnfK9bGYX1iCacQh9SOR90rP8YrtagN54XQxpWlft-jJukv40WOUcFtJpL0WlEATUf81uAfl5zRBQf7nojYseRuxoplZiyonNokRdVS3P2lNYuYfRcBeKsSZh6QxzeUTgpal5Kbtvm5ADjUuUSySwkFHSiQioTBvFw9wfyNsYzUIYbeh-WkpzxWwHOVp80M6q56jRP-xK3GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی گسترده هتل «پلازا» در اربیل عراق
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130729" target="_blank">📅 20:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130728">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزارت امور خارجه انگلیس با موضع گیری در خصوص حملات اخیر به بحرین و کویت، خواستار اجرای تفاهمنامه ایران و آمریکا شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130728" target="_blank">📅 20:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130727">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری/ سفیر آمریکا در سازمان ملل:
صبر ترامپ درحال تمام شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/130727" target="_blank">📅 20:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130726">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
گزارش ها از وقوع درگیری میان ارتش اسرائیل و ساکنان منطقه حوض یرموک در استان درعا سوریه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130726" target="_blank">📅 20:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130725">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
حمله پهپادی اسرائیل به جنوب لبنان
🔴
منابع خبری از حمله یک پهپاد متعلق به ارتش اسرائیل به اطراف شهرک فرون در شهر بنت‌جبیل در جنوب لبنان خبر دادند.
🔴
جزئیات بیشتری درباره خسارات یا تلفات احتمالی منتشر نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/130725" target="_blank">📅 20:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130724">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
اکسیوس: در جریان مذاکرات هفته گذشته در سوئیس، هیئت آمریکایی به ریاست ونس با ایران توافق کرد یک «خط اضطراری» میان آمریکا و ایران، برای هماهنگی ترافیک در تنگه برقرار شود.
🔴
تا روز شنبه، این «خط اضطراری» هنوز راه‌اندازی نشده بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130724" target="_blank">📅 20:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130723">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
پوتین: روسیه شروع به استفاده از ذخایر سوخت کرده است، اما ذخایر بنزین در سطح سال گذشته باقی مانده‌اند.
🔴
ستاد دولت درباره وضعیت سوخت به‌صورت شبانه‌روزی کار می‌کند
🔴
در پمپ‌بنزین‌ها صف وجود دارد و انواع لازم بنزین همیشه در دسترس نیست
🔴
لازم است پیامدهای حملات کی‌یف به حداقل برسد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130723" target="_blank">📅 20:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130722">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqkGNJL9jdcRYtQss50PXoTA1vn3CGmXg-J5q8wLD1KmAXfgHERdDpLiY7d2SMx_Bvm8mP_9K-Uhpzzedc3pAQDEQ4Mlqvmee87pcuuKE_HPt5oyEXaCgXc1L9qKIpQ6Ir2LVdq9wPuxejL5DiKSq95_LbQDJRXJIsGJWDQMDmplWi7c-Qqh_AbUF_9skIyCLRB0E-lRST9p1JhLL1vk9ibXXEztZ-AEAQVcuB3-8B9Mx_xv6aoewLhDb5N9mbDW0PUR049LixFyIw0YHzAy8eoeVROH9WWPUyChpFsj0665uQaUQldPFGiwSbSlkHB3OewfxCENbuh4wHvR1jkqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال اعلام کرد مذاکرات هفته جاری در سوئیس به علت درگیری‌های جدید لغو شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130722" target="_blank">📅 20:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130721">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلوبانک مجدد قطع شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130721" target="_blank">📅 20:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130720">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
۸ فروند هواپیمای سوخترسان آمریکایی هم‌اکنون بر فراز خلیج فارس و تنگه هرمز در حال پرواز هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130720" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130719">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d5aba3744.mp4?token=b4HqJzqigmsiwz2HMbBCQ6T2JJaMyI550sPsl3ZuuPNDgd8F8zcD-taF6yxqcwYOqaik2bBnKk_-ZJm1tJ_aLYxB0ENA_2179AQ9e9IxpOl96iMOXuy9e3J74HVkBhrW07WXKAzx4XFbu-EP4h_aKqxBWBts46z7SHzytsADc_ObmlPoK8l9sJeToefuSAe3-6EL1Qe9uuDEoaGAYhGLqvfN1-EHDVO_PNf2lql2rjEVVWHB6-UbPNY0GTvKXGHbODhbh-I4Td8Pemp55KbrhKiJ3HnbtYKicUQHbCY8VMo5gDIsvkQ1CsQxyCWZ7Uh-PD3DNvpZfpADsxj-6fKjRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d5aba3744.mp4?token=b4HqJzqigmsiwz2HMbBCQ6T2JJaMyI550sPsl3ZuuPNDgd8F8zcD-taF6yxqcwYOqaik2bBnKk_-ZJm1tJ_aLYxB0ENA_2179AQ9e9IxpOl96iMOXuy9e3J74HVkBhrW07WXKAzx4XFbu-EP4h_aKqxBWBts46z7SHzytsADc_ObmlPoK8l9sJeToefuSAe3-6EL1Qe9uuDEoaGAYhGLqvfN1-EHDVO_PNf2lql2rjEVVWHB6-UbPNY0GTvKXGHbODhbh-I4Td8Pemp55KbrhKiJ3HnbtYKicUQHbCY8VMo5gDIsvkQ1CsQxyCWZ7Uh-PD3DNvpZfpADsxj-6fKjRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرمربی کره استعفا داد
ساعاتی بعد از حذف تیم ملی کره جنوبی از جام جهانی، هونگ میونگ-بو، سرمربی تیم ملی، با برگزاری نشستی خبری ضمن عذرخواهی از مردم کره، از سمت خود کناره گیری کرد.
@AloSport</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130719" target="_blank">📅 20:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130718">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
جهت رزرو تبلیغات در الونیوز به اینجا مراجعه کنید
⬇️
https://t.me/ads_alonews
https://t.me/ads_alonews</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130718" target="_blank">📅 20:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130717">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از منابع:
گفتگوهای برنامه‌ریزی‌شده ایران و آمریکا در این هفته، تعلیق شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130717" target="_blank">📅 19:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130716">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ADY-o78D0bwJR6gU6c9RDauw-gCJR16g5OdFeG6B9lMz3EN_CCNzRcuTnfBT8IoRZRfO2Sl5vpj4oI5qf5MBB1fNwizaIpYJndpLiy8RbEfP9XrSEprtXmGPnQd9l-noHGy07gVGaaNqDY4muaoBUMTwvhbmGN_lCzqR2efqM2AJgCXykyCSZPZWYpMvrlAxjEQqs5C0RxyDafOIqGz56oScC3AHWd_IsFH3frdRmW8GwifcmeRQcR2kpFYmBIc9dGcLPK6wrSdxuQ8vE7m7LR2hSfXoMIJMoIdZQuXBGzjWEgiRfgZJnHCS2XuoIwGNJyhOd1r4JLhwrVlyPG1gAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
هنوز بقایایی از محور ایرانی وجود دارد که باید با آن‌ها برخورد شود، چالش‌های امنیتی سنگینی وجود دارد و همچنین فرصت‌های تاریخی برای صلح در منطقه — در لبنان و جاهای دیگر — وجود دارد.
برای شکست تهدیدها و بهره‌برداری از فرصت‌ها، ابتدا باید در درون خودمان صلح برقرار کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130716" target="_blank">📅 19:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130715">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntcMLFStfQSqDlv1XNfHOdK8HQXGaMx0gNHNx6N6NyiATyify3r8_QUZLIqM05dR23hiLcKtkoi4saQJ5chbH1GXrhH9knBdGd9aQWQi5qQkxRBahu02KULW60Ia5b_uDB4ntgHI8izfBaYz1LZ8Eok_z-EbEwjjMlUkeZ33331uOXAn4_eKGXRxMsgbcRngI-v_h05SMBoAtaNd5E2lCcDYg5xWvtwXMR_QzljdsEWgIpRezVlSxhlxvGM27PDb5ZAaM8LiTuRqdFyF68w_UGRCVCCgRH81uN8tZhXLVG3L1pkLGdGwm1VzpvKj3-La7kVwZPKcaa3M0kChoCBC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو:
اسرائیل به یک دولت ملی گسترده نیاز دارد — و این دولتی است که من تشکیل خواهم داد.
در این زمان، پس از سال‌ها آزمایش‌های سخت، مواجهه با دشمنان از خارج و چالش‌های بزرگ داخلی، دولت اسرائیل به دولتی نیاز دارد که اکثریت مردم را حول یک مسیر واضح، مسئولانه و ملی متحد کند.
قصد من تشکیل یک دولت ملی گسترده است، دولتی که بر اساس گسترده‌ترین اجماع ممکن در مسائل مرکزی که آینده ما را برای نسل‌ها تعیین خواهد کرد، تکیه خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130715" target="_blank">📅 19:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130714">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نتانیاهو:
ما اظهارات ترکیه را نادیده نخواهیم گرفت و آنها را به اطلاع دوستان آمریکایی خود خواهیم رساند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130714" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130713">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
آغاز پروازهای تهران-دبی-تهران از فردا
🔴
مدیرعامل شرکت شهر فرودگاهی امام خمینی از فعال شدن مجدد مسیر هوایی تهران-دبی-تهران و انجام پروازها در این مسیر از فردا (دوشنبه) خبر داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130713" target="_blank">📅 19:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130712">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9z50wv0Ok9IDca0vbja5udnxGaVhaV-HR4KnxVTL4jTudYclDs8jbwsY9HsH8-clyYI38VDnVHSQ8v7xcf7MFJJGr8sKpyAtftzoZbUs3_wOccm0XPlkTMbotn0855B2ve_UJB4BOC8GKvLpb8dhNzd42dNmWb4diIFlYDRzpLyM-VgitDxyftG7MUtLykfNsQNZs9Pd8Tc8bw3aXg7D70U9AjPyagmMrFWidGJNxctWM8rrNMH6gNLSEnJaEXUHezI_CKlXGOi3KxZcxFHwKU6XBNEKJ-awxTAJG0JJe7UyUhP70vw4Vj9CAea4Ffb7Q2XOE52Kr4m4Kwrsm42Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از لاشه یک فروند لانچر منهدم شده دو فروندی کروز ( طلائیه ) سپاه توسط آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/130712" target="_blank">📅 19:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130711">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/884efd1550.mp4?token=K7oF19vNPonyVE20qPh_8YOUTH5SO3ZswmS-2nsSJWSn5tdrdb_IcjhJhy86gi6WZfjgtinLCTYs9LYGaZg9Pl6l6m6UfcZxkg_JkRfQOWOH0_4ARfYWf394ihXgWgwelqPt8CCV3lYmaYk4LNDnGzc1Jkl-rJmh87kCQbuT1B6cTYtKj4ZdvzOsvlG0suSXDSDkiwWvm_yS9TxFRgXzA5MyncM729Q470k3QJcgqM8dZg8uJygsFeS2cqVAsgyI-LBmZ_s1JqRN_7Wq5yRczeNZHAT_4QnM32HCievburAo7LGjlc02kxcR7Dg7F3662lj-BMlfrp4XVAypgigXAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/884efd1550.mp4?token=K7oF19vNPonyVE20qPh_8YOUTH5SO3ZswmS-2nsSJWSn5tdrdb_IcjhJhy86gi6WZfjgtinLCTYs9LYGaZg9Pl6l6m6UfcZxkg_JkRfQOWOH0_4ARfYWf394ihXgWgwelqPt8CCV3lYmaYk4LNDnGzc1Jkl-rJmh87kCQbuT1B6cTYtKj4ZdvzOsvlG0suSXDSDkiwWvm_yS9TxFRgXzA5MyncM729Q470k3QJcgqM8dZg8uJygsFeS2cqVAsgyI-LBmZ_s1JqRN_7Wq5yRczeNZHAT_4QnM32HCievburAo7LGjlc02kxcR7Dg7F3662lj-BMlfrp4XVAypgigXAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سنتکام فیلمی از یک جنگنده F/A-18E سوپر هورنت نیروی دریایی آمریکا در خدمت اسکادران جنگنده ضربتی ۱۳۱ را منتشر کرده است که از ناو هواپیمابر کلاس نیمیتز USS Abraham Lincoln در دریای عرب برای انجام پرواز برخاسته و همچنین یک F/A-18 سوپر هورنت که روی همان ناو فرود می‌آید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/130711" target="_blank">📅 18:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130710">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e87a537482.mp4?token=pPKol_qlNxDF_fbh9HV4UcSmuRa-xnMjo_9sT4NHUrJiB8lCmW3tPQX8uPCAnRP5ljLyyVBJTB-COCvX7oJpEMDXQD3vldHW7SKNIfbOuYb_z709HQPCTQIJ2sWNmeg9r17wQqL6xDCDYQriC2NbBBUtZcseo144YG3o8TroqNkgVlQZiJzq0YqhKsQiLbqPQbwRKrv6UYy6RWmdX10AQ4-8QMCofibjXR9humuq_EPBwOMI7AN9T6rfdCHslhkwB6uSt3ftdIBghGk57tuvk-lx1FtCRORAU-dqACVbx8mlogoLwNYkwM4v6Wz-MNj1ZLml0xxiNj4k757tc8mK-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e87a537482.mp4?token=pPKol_qlNxDF_fbh9HV4UcSmuRa-xnMjo_9sT4NHUrJiB8lCmW3tPQX8uPCAnRP5ljLyyVBJTB-COCvX7oJpEMDXQD3vldHW7SKNIfbOuYb_z709HQPCTQIJ2sWNmeg9r17wQqL6xDCDYQriC2NbBBUtZcseo144YG3o8TroqNkgVlQZiJzq0YqhKsQiLbqPQbwRKrv6UYy6RWmdX10AQ4-8QMCofibjXR9humuq_EPBwOMI7AN9T6rfdCHslhkwB6uSt3ftdIBghGk57tuvk-lx1FtCRORAU-dqACVbx8mlogoLwNYkwM4v6Wz-MNj1ZLml0xxiNj4k757tc8mK-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Newcastel core...
@AloSport</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130710" target="_blank">📅 18:20 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130709">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل:
در توافقنامه هیچ جدول زمانی برای خروج وجود ندارد و هیچ چیزی اسرائیل را به آن ملزم نمی‌کند.
🔴
در واقع این یک توافقنامه بسیار خوب است، اما حزب‌الله از این بابت عصبانی شده است.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/130709" target="_blank">📅 17:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130708">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5affae2222.mp4?token=VLzKnNRHhyX6HDdugxRx7hPY6iBYttuEQ6Tpd7uwOjAWCVTclXD6AarkQ5nHmL0vz2LKEQlWOAxunf6ansg1R5J30JYJG60_jFLO6hn5nRxTD62RYOrxPInroxjMB4tZbyXhvG4Gj3cZPl1g7ZDMTeTDf3Yeb4aXaZPfyddEAb3dFDNNJbih9unkyPOukgqY7T6xlvYn1gys9w0BJaiuaH5wiSwdP9uBX6cj4gpruETD9Em04K9BNzW5vFk7IOJwALa_rIoVjMY0geUpPVK-JYrdmWcgQcqZwTJwtO_gZrYUJfYtrR7QjcpJGdal0zlLPFljqapmH-ngKetTLEl9UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5affae2222.mp4?token=VLzKnNRHhyX6HDdugxRx7hPY6iBYttuEQ6Tpd7uwOjAWCVTclXD6AarkQ5nHmL0vz2LKEQlWOAxunf6ansg1R5J30JYJG60_jFLO6hn5nRxTD62RYOrxPInroxjMB4tZbyXhvG4Gj3cZPl1g7ZDMTeTDf3Yeb4aXaZPfyddEAb3dFDNNJbih9unkyPOukgqY7T6xlvYn1gys9w0BJaiuaH5wiSwdP9uBX6cj4gpruETD9Em04K9BNzW5vFk7IOJwALa_rIoVjMY0geUpPVK-JYrdmWcgQcqZwTJwtO_gZrYUJfYtrR7QjcpJGdal0zlLPFljqapmH-ngKetTLEl9UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی مردم غزه از ناکامی ایران و صعود مصر به مرحله بعد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/130708" target="_blank">📅 17:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130707">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">پیروزی شیرین ملی‌پوشان والیبال مقابل کوبا
ایران ۳ - ۱ کوبا
🇨🇺
۲۲| ۲۱| ۲۵|۲۸
🇮🇷
۲۵|۲۵|۲۰|۳۰
@AloSport</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/130707" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130706">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
دادستان مازندران: بی حجابی در سطح استان به بیشترین حد خودش رسیده و دخترا عریان میان بیرون!
🔴
از مسئولین مربوطه درخواست دارم اشد مجازات رو برای دخترانی که خلاف موازین اسلامی رفتار میکنن در نظر بگیرن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/alonews/130706" target="_blank">📅 17:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130705">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
نماینده آمریکا در سازمان ملل:
تحرکات ما در صورت لزوم ادامه خواهد یافت تا زیرساخت‌های مورد استفاده ایران برای کنترل هرمز را از بین ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/130705" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130704">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/130704" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130703">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: اگر ایران گمان کند ترامپ در برابر حملات به کشتیرانی و پایگاه‌های ما دست روی دست خواهد گذاشت، در اشتباه است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/130703" target="_blank">📅 16:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130702">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ET8iOwctgecFkKNEtJxkPriKxCoVsMOkg2UBAAmSWnskjhfdhMD1v4dRTUAZMXQeUfCJ7NMKYLbnNFGaEc6EM1esIXq_tFXEiQNULoWLidt8R2Fk1rhEGrNdZmB7F3mYBRJcD_m-lFvxWRUtHkAPemO65TbqR3q_KGQ51LAh-c-BQ8mpJaxDHpG0DoU-5R3CsdrzWK9Egt95SwN5ZXBsZ7wvEj_1Nxd5svAcW1hH8GG0dA1ByNyibKpqy6Z-uGGPwOL0hrqmMzxk0yQICMAe73MyZvsvCROQuH0_T-N699zcb_SvpisC0j6rUlJuF6ZVSkV0pszGdZeIAvY3zbt4_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خداداد عزیزی:
قلعه نویی با پارتی بازی و رانت سرمربی شد و این نتیجه افتضاح پیش اومده، سرمربی‌های ایران هنیشه با پول خوری و رانت و رابطه انتخاب میشن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/130702" target="_blank">📅 16:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130701">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
ممکن است ترامپ به زودی دامنه جنگ را تشدید کند و تفاهم نامه با ایران را پاره کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/130701" target="_blank">📅 16:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130700">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
زمان شروع امتحانات پایان ترم دانشجویان دانشگاه تهران از روز پنجشنبه ۱۱ تیرماه به روز شنبه، ۲۰ این ماه موکول شد
🔴
پایان امتحانات پایان ترم دانشجویان دانشگاه تهران نیز از روز یکشنبه ۲۹ تیرماه به روز شنبه سوم مردادماه به تعویق افتاد و همچنین روز دوشنبه پنجم مردادماه  پایان امتحانات دروس عمومی می‌باشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/130700" target="_blank">📅 16:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130699">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mwq6bsiBpN1JNpBPPLA9x_VEISmxO9I9gvBt0tOjrh4KiUv5fPXaIasrCuOU0fNGlvURUaX2IMICRxdLqRQ5EvYZhsP7ZLnMLKTQi_AkRLXlN24X5SqLoc6-TduFLqAuSTyyfKJYkAiV23Ca9Hi8vyJ4PsL9J90_KvcADkXmuZHErLNidNCt-DrtQct2pTdwT0sQQDZga9W5nQIafX33bgTjYMKETVjjmczN4CyMfJwogWgYDg3xQtjqnG3-X0Oqv-IG_O95M8wMEqEqVVcJIKvueVJQruPiKyuW98TjGO0aRAatKBDuYcpSvAdKAPw9gBC6IYn28kfH8baZs6THMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده اولین کشوری است که در یک روز هم میزبان تیم جام جهانی فیفا بوده و هم کشور آن تیم را بمباران کرده است.
🔴
ایران دیروز در سیاتل با مصر بازی کرد و بعداً در همان روز، ایالات متحده به جنوب ایران حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/130699" target="_blank">📅 16:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130698">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqC9OGrdCVGKc4Ztht5259zpjbR_FKui4KuLvcacr0eHZWPumsjKUQ_g-pSeWEnIIUJV4gvoViSXseumVC88Mdh-5NPhfY41XM5ZdXruDM7i6G5ZU56e2jdj9Ru_VRY1wkWeaOWHCnLF4ZMNSJCZa3wxi7BdGlEbpkbOiMKHxV_j14ZTuMLEyV-GDxPz5QOSEOKs8EcVtcyxYhG9-USP8Te_ZvBYusY0jY1OUTfK6G8-DqPySBrkTGWPx-LOQPvfR46cqfkD-iW21GS32QUylxtyEdGXlp2lFVZvFou3JHQTbjDkZX7j_qdM_XwWFMJKCcuU0naayKerOyk-0d5jjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: مسی دیدنی است؛ او تنها بازیکنی است که می‌توانی بگویی بهتر از پله است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130698" target="_blank">📅 16:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130697">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U1_7FkYEeDr7YsYJsxB6a8T9Vczn8_XpKALb6qaHAT5eF9yfNrGn5szSXGrFtVZNqPdgEHYfldrk75X5zUVSO4RUGHMU-a6DP2qEe5K1lrUdcQ5WLSG8_S5twwcdc_JBGKKBrR0e47lUzXsRwMSjARNYYyDFlfLtqT8XjlRwhOB4-jWesJVIxVyKLVsZFUy1beyEDbTLv6SAFdwb5sR-DJUXTdwu2aTyFShA_hGGAkFwVwhEnCMISeOi314Df_3106wI-rn7nwGScC90zpJfiJrERT8Sw5sqqVO3PJov_uRlbmupC-Eiyadclb0O55PwNZc8ELeKrn9_XI268ejaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاتز ، وزیر دفاع اسرائیل:  فرماندهان و سربازان ارتش به طور قاطعانه به عملیات در لبنان ادامه خواهند داد تا تهدیدها را از بین ببرند و برای تضمین امنیت ساکنان شمال تلاش کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/130697" target="_blank">📅 16:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130696">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
فایننشال تایمز: میانجی‌ها در حال انجام گفت‌وگو با ایران و آمریکا هستند تا تنش‌ها را کاهش دهند
🔴
فایننشال تایمز به نقل از یک دیپلمات گزارش داد که میانجی‌ها در حال انجام گفت‌وگو با طرف‌های درگیر [ایران و آمریکا] هستند تا تلاش کنند تنش‌ها را کاهش دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/130696" target="_blank">📅 16:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130695">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
وزیر ارتباطات: اظهاراتی که اختلالات در خدمات بانک‌ها را به اتصال اینترنت بین‌الملل مرتبط می‌دانند، غیر حرفه‌ای محسوب می‌شود/ عمده خدمات حوزه بانکی اصلا در خارج از کشور در دسترس نیستند که با باز شدن اینترنت، برای آن‌ها اتفاقی بیفتد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130695" target="_blank">📅 16:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130694">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e18ef9d64.mp4?token=CoMkG7P93E1dRvrFmQotiZap7hajlCePxqwoOAWXyF8d9e9yhIQJ785yecTn5XYOW0aEo3VrgA-6QfxPSgLTDUXByG_U5h31-eZ_6FWs8HfvGoKfiCF6rS6NCMSPEgJSz_lymNAY5uVSyE889AfYqSGVvIMuiajObFT0vajyLlWxwkBCs78oNDzOr25erGDuzX4jPiGRQCV9T7VJrchSALmFAXh3CRPAB606ryRL6uUFZ1QOXlMcI4LwriQ6ux_afEDF0BrcvQkr0oWdUi03Tfo2PBezlIRzKRneljFUpWabxDkTpVNg4qGJPM4MvwQIReOaYsKEePeuDjuWZa0a3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e18ef9d64.mp4?token=CoMkG7P93E1dRvrFmQotiZap7hajlCePxqwoOAWXyF8d9e9yhIQJ785yecTn5XYOW0aEo3VrgA-6QfxPSgLTDUXByG_U5h31-eZ_6FWs8HfvGoKfiCF6rS6NCMSPEgJSz_lymNAY5uVSyE889AfYqSGVvIMuiajObFT0vajyLlWxwkBCs78oNDzOr25erGDuzX4jPiGRQCV9T7VJrchSALmFAXh3CRPAB606ryRL6uUFZ1QOXlMcI4LwriQ6ux_afEDF0BrcvQkr0oWdUi03Tfo2PBezlIRzKRneljFUpWabxDkTpVNg4qGJPM4MvwQIReOaYsKEePeuDjuWZa0a3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
39 سال پیش در چنین روزی، رژیم بعث عراق با استفاده از انواع سلاح‌های شیمیایی، مناطقی از سردشت در آذربایجان‌غربی را بمباران کرد
🔴
یکی از غم‌بارترین و تاریک‌ترین صفحات تاریخ معاصر در این روز رقم خورد؛ رویدادی که با وجود فریاد مظلومیت مردم این شهر، از سوی جهان شنیده نشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/alonews/130694" target="_blank">📅 16:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130693">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
قیمت هر گرم طلای ۱۸ عیار به ۱۷ میلیون و ۷۱ هزار و ۵۰۰ تومان و سکه امامی به ۱۷۲ میلیون و ۵۰۰ هزار تومان رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130693" target="_blank">📅 15:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130692">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
انفجار بمب‌های عمل‌نکرده در محدوده فرودگاه شیراز از امروز به مدت یک هفته آغاز شد؛ احتمال شنیدن صدای انفجار وجود دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130692" target="_blank">📅 15:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130691">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
مقامات بهداشتی فرانسه می‌گویند از ۲۴ ژوئن تاکنون حدود ۱۰۰۰ مرگ اضافی در طول موج گرمای بی‌سابقه‌ای که در غرب اروپا رخ داده، ثبت شده است.
🔴
افراد ۶۵ سال به بالا ۸۵٪ از مرگ‌های اضافی را تشکیل می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/130691" target="_blank">📅 15:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130690">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dr47g5U78KCVPSJ8TBFTtb44rLB2_eEXzAzTczvCYKDXyIDw6XQ6JstYbHXlrJZ8vv1_7AVElzRQgdeOBmirj9whwr0Fx94NjVTHUJZCKdQDd1QHkeHyOoOrhj2PCA8zpW5uV7P_DmZCjq7kPQOCq3JSCMzx8TGJJg50mhi7C0Lp6_JNftZpjnAHjDdnr_JWWicIzZWz2pzAJa__4YPti0LTbHkdkciw-qnqHi-EH4CG17TpFfnjwZGqVLSTygDJDAj8VIs18ndkuG9lwdX9yMvMsr7lE3JRTZuimZoGBmMgRXMWcS9a1fq-hN6w--HOehOL-rEngxKbr4ZHsu9P7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تردد خودروهای پلاک مناطق آزاد کیش و قشم در هرمزگان به‌صورت رسمی آغاز شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/130690" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130689">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVR1IsNjzF5Qbkm1nlpisoQiznwf4JeRGidARCGeQqDi5bi3H0kp52WwVApqxSdiHprgikF-Sv6VvgbMU3D80QuNuV9JaxemQbVZUyzwOZjTZb32qq0gA5vOyN2QrUFfDZBx_d13irMrUyMzD7labZflVaQxmYdicYF0AKYRYtquJ1USwyjKG5JaJ0YtbuyHyVqkSL2ajeaV2dUnITgH7Y_bWA_l7F5oCjez4AnfHUDev5ly3fC_6cR7gz4tASB8e8g47xcnk_4KxykOrUIUgzNIdq5GhKLy9uTZMhQ7uhFkwuYeOYCnHQc6bjHsqw-NPTHcklq1-Dc5VFmc9MnsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو هر کشور چند روز باید کار کنی تا بتونی بازی GTA ۶ رو بخری؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/130689" target="_blank">📅 15:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130688">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
داعش ساحل فیلمی منتشر کرده است که حمله ۱۷ ژوئن به پایگاه نظامی ایناتس در نیجر را نشان می‌دهد و سلاح‌ها، مهمات، خودروها و تجهیزات نظامی منهدم شده به‌دست آمده را به تصویر می‌کشد.
🔴
این ویدئو همچنین پیامی از یک تروریست داعش خطاب به «برادران در زندان‌های شیعه عراق» دارد که از آن‌ها می‌خواهد در برابر آزمایش‌هایشان استوار بمانند، در حالی که یک شورشی دیگر قول می‌دهد کمپین گروه را از ساحل تا بغداد، مکه و قدس ادامه دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/130688" target="_blank">📅 15:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130687">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
گزارش ها سقوط یک بالگرد متعلق به شرکت آرامکوی عربستان سعودی در رأس تنوره و کشته شدن ۱۴ نفر.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/130687" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130685">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed75e27c84.mp4?token=UHHaiiadnxYEAE5qGcy2_EhVkA8WTxXKiNMSbjXeBEqwVzDmMe8dhoXsWypGeJqf-KWBkzfUR0_FYNsqelA7vlJBlUewzZIRzlZtzR88BaiiZVSIqugiK_mD0a2UxGwoF009SwEhRaa2VQpJYwwkJLEAfQxI0JzAhfEYFYQ4VZCxVXaIKWS1Q-PmTxT6UThDmh1_AHUIDGEgziVrrUJ9d2ulBjcCvBAYJl5XpkzrhzBK0FZVwnGd0Eu1NjGNDMoz94tnZomnWmlLxMRGZaj6EP_wCKDAcz12E81iwQ_43Mrn18Z90XzUkpYmnGo5rUGizxVkWS5y6KnYd0cxJYFynzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed75e27c84.mp4?token=UHHaiiadnxYEAE5qGcy2_EhVkA8WTxXKiNMSbjXeBEqwVzDmMe8dhoXsWypGeJqf-KWBkzfUR0_FYNsqelA7vlJBlUewzZIRzlZtzR88BaiiZVSIqugiK_mD0a2UxGwoF009SwEhRaa2VQpJYwwkJLEAfQxI0JzAhfEYFYQ4VZCxVXaIKWS1Q-PmTxT6UThDmh1_AHUIDGEgziVrrUJ9d2ulBjcCvBAYJl5XpkzrhzBK0FZVwnGd0Eu1NjGNDMoz94tnZomnWmlLxMRGZaj6EP_wCKDAcz12E81iwQ_43Mrn18Z90XzUkpYmnGo5rUGizxVkWS5y6KnYd0cxJYFynzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نیروهای جستجو و نجات ایالات متحده دیروز مادر و نوزاد نه ماهه‌اش را از یک ساختمان فرو ریخته در ونزوئلا نجات دادند.
🔴
هر دو تنها با جراحات جزئی فرار کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/130685" target="_blank">📅 15:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130684">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
یک کارشناس حوزه آب با اشاره به وضعیت منابع آبی کشور اعلام کرد ۹ استان از جمله خراسان‌ها، کرمان، یزد، اصفهان و سیستان‌وبلوچستان در آستانه تنش شدید آبی قرار دارند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130684" target="_blank">📅 15:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130683">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6IRqrQmyD5Exq8Pe2F8E5Sn82rSXkc0JwHAse21745YrkoefE7qGheihmWcoUzRrZvJ-sK2MjcTzShSoIZhA5AaYm6hzQxcRw6pnhzahYYMQhKlLNY96agBjpjCTUl627k2yGotMj5WbDe0UXXo3hoCG4MIO3sbgoapo0HvQf6vembbMhBso8xp8Wzt77XrYAKLtgLt9MJzAmsgD_QJHvQvUNEVVJBMDUTZAsT6_qxo7QrxRqwx6svKtFJC3FvjkF7NW9miyAARY2nz72B9lg9zxbSXXANEQNIiJvhzrvFFLG7Ug4Prrzlef29JO2ph_k4CxAgRMeVt3JB02KN3ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/130683" target="_blank">📅 15:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130682">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
الجزیره به نقل از صدا سیما: امن‌ترین گذرگاه برای کشتی‌هایی که وارد خلیج فارس می‌شوند، جنوب جزیره هرمز و برای کشتی‌هایی که از آن خارج می‌شوند، جنوب جزیره لارک است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/130682" target="_blank">📅 15:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130681">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
شرافت یعنی آقای مرزبان
🔴
خدای ما مردم با خدای طرفداران جمهوری اسلامی فرق داره</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130681" target="_blank">📅 14:53 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130680">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
واکنش سخنگوی قوه قضائیه به تهدید رئیس‌جمهور توسط یک مداح: این یک اقدام مجرمانه بوده و قابلیت پیگیری دارد
🔴
دستگاه قضا‌ حتماً به وظیفه قانونی خود عمل خواهد کرد
🔴
شرایط وحدت را حفظ کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/alonews/130680" target="_blank">📅 14:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130679">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
وزارت خارجه قطر: باید از پیامدهای حملات غیرموجه برای منطقه جلوگیری شود و مسیر گفت‌وگو، دیپلماسی و کاهش تنش ادامه یابد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130679" target="_blank">📅 14:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130678">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
گزارش صداوسیما از جزئیات حملات نظامی بامداد امروز آمریکا به قشم و سیریک
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/130678" target="_blank">📅 14:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130677">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxiUQoXP3GmzZFu1wfWmQqv-bvALUjJK3iHIHPP3A4bB31ermDzJuMwIh0j3VkVKopPfkdil7GbhTfW5rBOnzINTZKkQVd1nXci6GfimVVtFwrdLaYep1rotbWxz_MZtVS22Erp9mo5J99qbMJOde2lDtOSWEXyP6Y2CNsZXFBr1iP8Gr8bp1BTE_ghvA9irdeClwOa0rvUAWEjG3Sj96NwW1RpR1vu2_ULOkzCEnPaNV_0Fc4CGYJNau-Ujw0TmGIpLDb6q73FOyTGUpCEV1wQD32r0V6fVTjbOV7WK7IsQ__lV2pzPEY3loJKR1uk62i_sYqMz6iTsFwLSM0cPQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی با نخست وزیر عراق دیدار کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/130677" target="_blank">📅 14:47 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
