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
<img src="https://cdn4.telesco.pe/file/q9EIGojXLT9w_yuw8Z0tEd2Be5zZ-5HPVIRK3qw0QwN5E-3Gc2k_9SjktQQQa1ZaJGoHe5iHzMeyMuv_f9IcNCLdwaiRTH-7Mnk5gpQXIjsDvw9965zEqlv_VRKUyhp_YBwP-FfeFOi6xSo-TSMSl7W0vCpFPPGHHTq4A38jwL7q7w0zEGuNvKm9uN-jlbiK3dUtYhi-u9MN82zNJZ5T3xIYp6N-goh8Rd9YgCysC8z4PkpmfCF9rnmUUP9mEx1H1JKYdmoc7ySIUKhn9Z4rG1sgPSnDXN2yNytohB7jFFNivM0NGgZIKJhhEjh58T30pT3N6UWLTSkSOxk1q0rnKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 472K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 09:11:44</div>
<hr>

<div class="tg-post" id="msg-30164">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7M3M7C57H9xdgTd-kgpj1BCQ7EroBt6J9QdLWNvyJe_W723x1MNx-MoRcO_HTnCzodEaYBwoB8aw-gg_FJsKVoqiW7vQGJZIQU9bgVriW0pSXAFmwIQrYPFrTmcKiS5AImI_SvOctMNVT9nsO5hwCI5LkazP7oF1oxRacL0fT1TW0NhQYXWECAaZcSAzUddNHxcg-4W7AWkSIUH7qgjrqD5AHeJCfmH0b5YrAJRn_fXCoD_slPV3ozJG9K-hS31dnvAGJLWXBTl7o-2RdgD7HfXwZmA5C5TlELp5zR9v1SRWOqje-0fLZHKmcIKfXbtGPf-8DHPySCD4OX6sJ4HFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/30164" target="_blank">📅 00:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30163">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEqTi9ezswWxzn7n8DI43dgWjvfggOnBJlOmcgVFBONZbw6R85zhYUGEF64v3QSwgXB-iyAi17ld7KEuljOn3LyzS2jMR2RKR7On_R7IaaEgdZhy_DLGTE-MgU8tlayp7AH2GdvO1GRtYBQl1h3BEFGaj9oSoNkyP3fAhc4aiPf6zHPJC7DgzBkaZYGLnCxkxxkHxsS3Pb1RTWhE44R6sy3KARXefvq1Cpx13V6CULTMXpMgGGBt3OgDIWWzyvDbJs9frS14mS_ajvtJIAQVRqegFmZkYfERgWQmEbirU1FjUAYopPao_vz58JthhaWuvL9cG9klPP8dfp14tE6qGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
الریاضیه‌عربستان:جدایی‌کریستیانو رونالدو از النصر در ژانویه قطعی شده. رونالدو قصد داره به فوتبال اروپا و لیگ جزیره برگرده مگر اینکه باشگاه الهلال پیشنهادی نجومی و سنگین به CR7 بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/persiana_Soccer/30163" target="_blank">📅 00:44 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVnXDskv8rCVbzvRYCBO8ylQAw3Jjw0D_Eiy96fkVWKD5QGg6GV3chxg9hOTuFzesaWjwC3R44Ztn4LStvcSe6q0gOAKP4tDwCiN9U1nbEKa5imKy_2y0m48bqJSoNY7IvFLAUZv2XGUFvgANHoX_1X62yvOfvo40-u3240yw94h_FPIIusTpmc7Sg9RR-8WD4VnAUf7hHeAhANzrmn6uVW8dLVVXj9bphbjLt1_V-6j_raGxDKCJjwHCXqS2xVC81jyRhVvBwqZPAbPGloLwgHWXKAjW5EWmf55KjGAM8zZ3gKBisDOxT4aNMW4zbIRa8d0ShAx_pBaWayKMgP4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها ‌‌‌‌‌‌‌دیدار مهم امروز
؛ جدال خانگی لیونل مسی و یارانش باسن‌دیگو پیش‌از آغازفیفادی و بازی‌های ملی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/30161" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30160">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHMgq-6Ujtz02jQZKXAgR3XhnYAvUy4cK8RqKvf8VT4UxMoxRsDxmtfufE69tU0znUT2JwNBHGUpPVGMoBGnScKxuOzhr_apMeg-F2vGvzMh47a2tIF03fJp_swHcrRArCCs5P76MovbjLVV_-UTFhZcUJZ3b9Kfx7QJKkW6CQ6ehFw8iQ7y-ZGQeI2KGytC9fQA7B2M1JtRRPmqYAfLxZkXWWHnhO6sNGtHhhTJb2l6gA4CQsSs2YFzm_mJJjfQmx8hS-1aOUw6aqk47J7NZGnAEwEJnTFxukz2BQQ4e3f5FejFFZna3wwjUUK4LYKTLl40VBOIitMc4mO4asOMhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌بزرگ‌ال‌چولو در دربی مادرید و برد اقتصادی لیورپولی‌ها با تک‌گل ایساک!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/30160" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30159">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnjE4g4qoWtg1FVYVYJUdzF811rugqVp5EsYqnKbE0uq-KKDyj8uURMCHS1m2xHGeRCZ17NxsmkcqPVnj9uOIzJXDEYPR01mNA6XlO1LVHfRXCVDvnudMG098k98p60sUAjVZ9GW2q1GS5DQCgj20EE7dOvooRd90u9OGvey3t9_wLvz-5sm3cGZBvl9cH3B7pV55I59Cx1BlXWAvuOhf19xP_s1SFVqn1MPv8G1DNRDg_2IIRadvA51mfNdp-C4f3XujiozkN6VQbdUiLHSHsf0bZ0MBRQ91_b8zUk2dLgOf7bdcKPhhcWdfrWIEylyg2qvi0rvbrrRF_mkvYhQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎁
🤩
🤩
🤩
کش‌بک هفتگی در یک‌بت
⚡️
یک هفته بازی کن، کش‌بک بگیر و هفته بعد دوباره برگرد.
💱
هر هفته بخشی از پیش‌بینی‌های ناموفق خود را به‌صورت کش‌بک دریافت کنید و دوباره شانس خود را امتحان کنید.
🆓
برای دریافت کش‌بک، کافی است درخواست خود را از طریق پشتیبانی 24 ساعته یک‌بت ثبت کنید.
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
P29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/30159" target="_blank">📅 00:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30158">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/30158" target="_blank">📅 00:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30157">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba92349391.mp4?token=U6Zz3xZdjI3RK267m8CbyR_28SytkeVwg-itaPZYt_ovzs-2mfecJ1xoEycpyVeN9U4JRHzzgf02AeQdU2AGawo0c_UF_y3EwOptWgVJqa9RyhiiMzexX-XU3vIFG7KjEv4_Uv_rH_hwFcUilUiihUQ9loD-uUpzkrJdG_V20jUHrhGOPsxlgPp1-gDZV9eHaWs8lxYt20IFeq3BDfVSj41Fg7FvQ01U9awli9NQvVo5jvaMj2e8qYo_ZQ4CA5iNL9zKYx7GaxxS9FpXQDhuPerDu1PvOgVPQyLZGMXbylJKwFIx6IthzA5vTNrHR-AI4YLFHCFNB3wtd1OjCwwVQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba92349391.mp4?token=U6Zz3xZdjI3RK267m8CbyR_28SytkeVwg-itaPZYt_ovzs-2mfecJ1xoEycpyVeN9U4JRHzzgf02AeQdU2AGawo0c_UF_y3EwOptWgVJqa9RyhiiMzexX-XU3vIFG7KjEv4_Uv_rH_hwFcUilUiihUQ9loD-uUpzkrJdG_V20jUHrhGOPsxlgPp1-gDZV9eHaWs8lxYt20IFeq3BDfVSj41Fg7FvQ01U9awli9NQvVo5jvaMj2e8qYo_ZQ4CA5iNL9zKYx7GaxxS9FpXQDhuPerDu1PvOgVPQyLZGMXbylJKwFIx6IthzA5vTNrHR-AI4YLFHCFNB3wtd1OjCwwVQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
میلانِ اموریم در دیداری خانگی با سه گل از سد تیم‌لچه گذشت. میلان با این برد یازده امتیازی‌شد و در رتبه پنجم جدول ایستاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/30157" target="_blank">📅 00:18 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30156">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUdk1L5vXFZNBfSohAC0YaZR70vaKirVdieDHbwU_C5GBrDRpt_gAaYEjO3f897uaxPRJClbJp77wi1onqkGBExHap2TZgi2vGqK5S5aCoDp7SrmWTmWZuB3pJv4pdYJ6sUkVpeV_LmWlDTbB2A0G0fCM75oivONkPL-WAB4SkzBMqISKM8Fhq23vd0zbSeo8t-QS7TQ9P9_KhAmkmxRKyrgA0lL_QpwrQaXYBiZhuqE3GZswUlEpHCyLRKxpwG0QEh6zxsyF0rDqVrBAqrp-6kR4OZqMDHhqqb6Jp4MwxgrRay5rsdsnuevvTU_uG0RXjrlSuM7_68XGIT2eQGlIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇦🇷
کریستین رومرو با سران اتلتیکو مادرید برای عقد قراردادی چهار ساله با این باشگاه به توافق کامل رسید. رومرو در دوهفته‌گذشته پیشنهادات دو باشگاه آرسنال و بارسلونا رو رد کرده و گفته بود به سیمئونه قول داده بعد از جام‌جهانی‌راهی اتلتیکومادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/30156" target="_blank">📅 23:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30154">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bj00u9Sj0ZHcz5i4MJ3K9ibKlev9YqlLSE1O2yLGjzodC546zMhzC7NInWFyxOHBccvTKfJIIlMB6G83r76CQLJrakfr2E4HasAbL12AjdvLVvkNZXlsfp-gGk-EHJ1rzWTkHfdLoCi5aApmggVRXHVG0QTkl7MT55_06QGdo9HAvXpIO3OwzSXjlUhMCNRLLA3N6bh_M_9GyCPjeYOIvKdJLyG2IAHSl28trNva18Vt2rCHWN4d-x2ao15c6ARviXhdcDch14fUOPyJb28x_-StuENmYUMNS6kr_UkV2pW7oMO0RCraGs3xwMtpsLZcy40pb7r6emptiAuF71Qftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LIuBA31P2tVENnMR9WRBdmiibk2q1lb2ZIN19oHtOWUl2d-Yt0Ev0SXB88zT_PhapY5c2CYFTwnRQjpvdOJwQLHfrnLi4v-A1iHWisEmmGYelDvWUov9I5gJrqHoaJoCkeOloYfoUKoYujWDmiz3-Ra0B1XvNW1YajxvgscYAqJsqkMr2IAsFroZu4_e_NKNcLgMTeKrnzDEsEiQKZDSbcek5YdGb7SQBo0R3bwGG2xVq0Ne5vrhEIRdd9aN2P56toT9VFx_WZhCPCDEA8a3GNPTl8yi9pcU6bga8KibEsavEx6fD5Aqnt4Csq5qkT6VVyHzfmPEmdbzlkGjVpvKcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد رافینیا و یامال درفصل جاری همراه با عملکرد کلی رافینیا در بارسا؛ بازیکنیکه بعد از ژاوی داشتن میفروختنس فلیک احیاش کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30154" target="_blank">📅 23:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy72Z8jXsstZEgt90oZva5vQptdzOq7vaw7K-X0WdpyZ2o2-k0i-atDo1fF26b_nb0L4kZiuDyZyCLqeYvCh8lz41TBiN40Inx4lzO8EFJJNEv7TqRzNMcRHaddVgKGhEbPrWWI1WAQuhkMnYza1vgxIA3PkJ5fKf_stSgS1awPz18BY6acj56JPpPhJq3cgK9gysbXg4rAgyPilk-g_f3biQo-WObgIJVWgIFWvEvborVmObHVdMLorLdAU8_LQAIwWHP_J25vzz1WojROr6mUvS0Xan2_ISPAfk_vfo6wVcC0Hj4poCt0nEyc3LnvP4_enVcCFDNa32QNIuUpmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
مصاحبه‌‌شدیدالحن خوزه مورینیو علیه داور بازی امروز مقابل اتلتیکو مادرید که از نگاه سرمربی پرتغالی رئال‌مادریدعامل‌اصلی شکست تیمش بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/30153" target="_blank">📅 23:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDSerppMspNOY7WG-pzTicwqc33PpyLPeM7lpueKmgqcFe2wHs2BrmjOs7HYDhL-6iLy2ToCoAIzBeSHXFDD03WjHvpUAubPVbw3pr7sQKrGICWlQy21P1DqAMQlwjW1rVjAuVrY9weS7zzbZ8HGKlo7FcNlf2XtyRd2yC8EMjOsLkEFsbo0iz2xVTFuOMTMrRW7wAkDQpwXMdW2z-kfOr_fhegSsPdG2j720ei6DRCAo7dY93CEMAeqcFo1cBI0TKQailZYLLVWdrgD7PbGtcStowI3rzUn290AexHBIwmPw0PI2xMIoScpaoupuFwgUa0wEkfgOwiX5-15g3JEKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
به بهانه آغاز فصل جدید رقابتهای لیگ نخبگان آسیا
؛ نگاهی‌بندازیم‌به‌تموم‌قهرمانان و نایب قهرمانان باشگاه های ایرانی در رقابتهای لیگ قهرمانان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/30152" target="_blank">📅 23:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
👤
طبق‌شنیده‌های رسانه پرشیانا؛ کادر فنی تیم ملی با اللهیار صیادمنش برای حضور در جمع شاگردان امیرقلعه‌نویی برای مسابقات جام ملت‌های آسیا تماس گرفته و این ستاره 24 ساله که عملکرد درخشانی در اروپا داشته احتمالا به تیم ملی دعوت خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30151" target="_blank">📅 22:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXsMMot-DGehqk3Brdn6aL4ZycrUwc3qDstxswVkfvS1HZ52WItGr_1H8MQkdKWDO3aW0Mgo6gm7g2_fuFyS6O_Z2ydTTv3oO6iL1Ihd2ezsLZESHFDBvj2kXGHk8pDDVI0NAEeY08i0pMNpjVKaH2Iis71D4SOXyt9dtjAsMI-ed4R8DjgwSVs2-OgnA7PMcHqxL7VrP9p9_3f9lBRzSswpXBqiTF93UKuD0kdhXXfdEpmDAHXx2GwI2_oL1wJB7lilKrUKPBQJQT_STaLYiG2ZBzS_efd6BXSXeBW4h-JeMjNq-GFgSCrnsI-OpB95HC2LtbcvzvIyFztVFH3IRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبرنگار رسمی باشگاه فنرباغچه: بزرگ‌ ترین آرزویم این‌است که کریس رونالدو قبل از خداحافظی از دنیای فوتبال یک فصل برای فنرباغچه بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30150" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VCxaZk4rwQsCqCLrF_ZseuHuschmXggGi50IEC2o8ZmtrhvRhrcOn9aakvmk61PpjOWaVgPme51vy0Wl6WrQYhsDfBlIDELu2jB4HTUBY-52Sr3Y7mH_aBL0sE5ksdskIUFr0CPQ-pFmr2b4goCL0qPUODxch1-ZyyFjVSONQUma8uPkBulfYENcprF-gJ__0AStRDOQ_0LPvWUDr9DUSmSqKWoXCBvhJbasGVbLZFlcEpZx93beY8VG94UDxmf5fW-DiZtTC1mFWNnFgYcxWaFir9uWBGhtYose7rTvrzwoxKGsvREVPHHAkhAqfXb75c6-FQvGLn6uiR3CC4mIOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فده وارده کاپیتان‌رئال‌مادرید به دلیل مصدومیت 3 هفته دور از میادین خواهدبود و احتمال داره دیدار الکلاسیکو که سه آبان برگزار میشه از دست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30149" target="_blank">📅 21:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">⚽️
⚪️
شبکه رسمی رئال مادرید به شدت از عملکرد داوری دیدار امشب با اتلتیکو مادرید شاکیه و گفته سران‌باشگاه دارن برسی میکنن که لیگ کنار بکشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30147" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgVSI9iV2ehoyJYrni7PTDjICY4Ghc7Rp0tElBhavYvGsO1sYXRBs1uMg0Ozs-IfCpK02T-l34oVe90twkDal8OGnpVr1gd9i2xZzJcFcwXacp2qR3Pagb2BvM_jWvq7jlUqjUVE1GIV3R5N2nO-4USMq9AJ2LI-xdiJBtxqbefvigPPCafZOyTjIdoWL-YANWUBUy0TytxenfxIpVTdOcezfaxO8cnJokez2P_DGWLh5Qlc3AL4E0_gTEZCNg7FUMj7htNeY0V5ItOELlWMaNUNK5E3hvVSkeN1zlfc5J7u2HPfNk2Rb8rYFiA5o3HgLG1xULtOKVDSG82iYqJn0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
آندریاس کریستنسن مدافع‌میانی‌بارسا به دلیل مصدومیت دربازی‌شب‌گذشته مقابل سویا، شش هفته دور از میادین‌خواهدبود و به احتمال فردا دیدار سوم آبان مقابل رئال مادرید رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30146" target="_blank">📅 21:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eeae99a.mp4?token=aaAn6iO77BmfaVKChCQW8anXQ7zSeeyeBBei995o4NqiDsf_LYIJ2rBGebefiVG0iSuTBxr1loZAoSGXmiewufFU0j0OPvI4yUUuR-sOlM3nVWEYTzdzUxqYgp_IA_sU_3sa9nxRwG3yDc8oBhZGzWBsMT2DSdMZ3dhXs0gvJBurNC4UpYfYDSXf_BSY-MAYXwr-nbB82sF9VEfWdiDbMYx1MwAFjEo41cJ3SGhFdPppoJK33l53pXkfE5nZxA8Ovlg2lhyYimBE0XVXxRk4F_n4nzHJquOdNcdbr-05xVTgbITRzECcSdrmITsxg0QPsIfSQoB24bJczHtb8vWnfHe2PZY7nj4cMsmhTSD7Gmcpq88Prf9MUGUC2aX_PvMLdxEVJG08EXcOeReWMYqAy6PCuBn4vXy3Vww6VqRy5SAGeho8VdG8meNbVsuENL5wfV9zQIxiGknKN5_4eAPGXrD9EdwQsPQ1aOC5C8P47SrO0szvl7Fh0_DkdSAtFoLisSeG6SIDJSyH2HnRvQobp8zIffyYvVSz8JPVlzC4GJ5vfOV2i-oUQ-pYEyhWvbWhXB3Jbos81zQ_9sxF3rDNYFPMkCLUFiyJtB4i6kivneP7XwPH0eBKoSI364rDZRI1cRGtHtoRY939bMvZAsVFZmNeYh9Yy8_8BOVrQN7nJAU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛ ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30145" target="_blank">📅 20:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b6c09bf.mp4?token=n5-dbit72MmO1skr41V33iIXJIxzPapCEZ_FECQryy-KL-EOKeNRjkorlvaouP3v-1G-orOWws4CqATLU46SNN259Z4-T8yq9YC9zHpMaEzaYEq8WX5qGj8_9-kcJj6ATn-vIgmfzLUechnjTElKRFmjKH6tExl3dj2PkYq5IhrfXxOD4_E9DCO_DJD1zq8SlfGZ7UGJrKgI3KAldh1LzeogQxv7PrxcawFGfzqK7fFyn7yWLMdjSl1IWYJhLYIXfhKWgoKv-RuUOaWnBkBdAcqdnWDKlZE481KBo4G11e5e4m0V7qnRAmUW9xTGvQtzNCbokr_HuyFem1n6MrkA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نامزدجایزه‌پوشکاش سال؛
ضربه قیچی برگردان فوق‌‌العاده و تماشایی‌از میگل بورخا، مهاجم تیم کلاب آمریکا مقابل تیم گوادالاخارا؛ چی زد!!!! حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30144" target="_blank">📅 20:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2be5ebfb1.mp4?token=dgREOh5aCVjdPbfsWkuL8Ag-0f1K401KVU7cD6gjZhjasBIxvzm_c9WFO_Y8enc36-v2w9DNdoIQLQQVK8DGKUfbpowjeGPFC1WRU7d-mQXkYQFpWqK75hABreyx_ZobJI6UgrwiK5V36KjAKhjlrzJ6MdVxJL6Mhb8vYLGPfSwKVVI9KTEu03IYeYkLEs8EogIE6JLf7cqdFBhiTpvLooCbjDZEz_maSvd8YKlkvPRt4vtpEmy-5A31uf7EnvKbWI3eZ9i-F-CLkgvNeJhEJ63zZJUvtqMpM-ccpcm4PbzrANXlpd31d2SZBwPD8iETpxwQA6MS8c6TOdL7v9WIpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30143" target="_blank">📅 20:08 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30142">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNAfUKVMClgwz-NrmPurcK4Pv9NaPjqqj6GomkLhptxS47kMdNlZDuJWkwZhnz9nYVG4bAJSNuIrZLvESOrocpRwmKi5NpcDHqtJgEqv8HVCPv2mGwW4YEihiQMVW4icCKVlrCH05ypkrb7TXTMuy6I1t32ZQIJIiyRL1DrPoPltVXvd7XeHfOtsAdp8XsRYKB8U73A_yT_1FSm0-3RqCHA79EK_YaajKlxi0_7jBOPYox6DXzkyQOtzpb6dxqxdar12HLzB8minV4jibSMuUh1RmSvDbp18LIY9HsJL3tYVG05p4qVxH_WjIJ6s5c5G1otiqJY5PyQW9hz1U_WjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته هفتم لالیگا|دومین شکست فصل شاگردان آقای خاص این‌بارمقابل اتلتیکو مادرید؛ اختلاف رئال مادرید باصدرجدول به شش‌امتیاز رسید. بارسا مدل هانسی فلیک قهرمان زود هنگام این فصل؟!
🔴
اتلتیکو مادرید
2️⃣
-
1️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30142" target="_blank">📅 19:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30141">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zra0COy4NtdjDjemUCRDPOE-ppKOTYz3Wq7IpIWXubzasN-ZgET7AwGBeaJxTijDZTqGtT2L2LxpGeYqUE8pPePDMlPbxgSF3gaM4wRNS0kGuEy-NiuNx6dTscKj3akcKXalWgW4VPXco9fKkGCS8jcN21NSPrKm1VEIrWMyKnPOeOR_ZXwx_EGDn7fGimwbOahG1tRz7XrP_Wjr7NO2pF9uwuTrYOvxgj9G6TJrkFKxsOkz4gnBaBXN97Qec9N95MjpqPMnDvnM5TQi7Npit_ekc67dCiMb1nmF0kriewbrEmrZFhQa3nwE37-pN-X2CvhYdQC7Gi9VnBtPy0Y98g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک ترکیب دوتیم رئال مادرید
🆚
اتلتیکو؛ ساعت 17:45 از پرشیانا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30141" target="_blank">📅 19:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30140">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb7yOaVtm4dU8rTwTcDFQDQAugg5d2AgegFfZ0ZmWP9d9wLBkLFrAUqJ46AoIB7SJkkl_s74nu0ZsFcYJhpkUyalkAMIVWZQM9TkXCKe_nID7hxJTYPTGqxA6uYUrIlmoZgtnopTphvpcNo1crNS9Yt_ZFjhBLWmeVN5-QkL1H6FjBZBmd2kUWF8oLyUEX4X3F4DFI0ObtIBFZ7WspM67YoS8RE4pT6ONTz5nf532qhYRFf_9xbK3YR1muyIpi2-6IlKeG2zP3I3RAcKvYyWs7Yr5EUFumnQsoAopy97qEeBZy9oksi4FQebLlQurBT6lexpNy3KlCLzzi_1ZjSGFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه کاشیوا ریسول درروزهای اخیر پیشنهادی دو ساله به ارزش 4.5 میلیون دلار به یاسر آسانی ستاره‌آلبانیایی‌استقلال داده بود که این بازیکن بعد از مشورت با مدیر برنامه‌ های خود این آفر رو رد کرده و آمادگی کامل خود را برای تمدید قراردادش با باشگاه استقلال…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/30140" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30139">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=ptRvoMGPTqOFMlgccbnI0Tj5TPSmiteiPFn97079uSKbaAjrK5LjUMPbqU_66QbvU6BSu5grnwf9qlhtwHaWbCVU5sUBR8QsqgqEuV-KkEgMpaLrLd7AULZqIt6mTCERCjxupw7BFy9VKG34JgifWufBOcVpRHdE-k3YcOALcgR9dntE2Lxaxtw1r8fH5UlY1lbh6WFHgK_oFF9yCKSgFCP6hDSKOZpBbhJRBbOVFpKPXBsM0BEDZ-ThxUeh0gvPs0QalF5BagerkdsiYw6xV7M6DREIvSxiCvfrYt0-ghDXD_BwtbXM9G27WAZy7jObpq1W7myxk7kV-TfFQbSqHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f4a8d8c8.mp4?token=ptRvoMGPTqOFMlgccbnI0Tj5TPSmiteiPFn97079uSKbaAjrK5LjUMPbqU_66QbvU6BSu5grnwf9qlhtwHaWbCVU5sUBR8QsqgqEuV-KkEgMpaLrLd7AULZqIt6mTCERCjxupw7BFy9VKG34JgifWufBOcVpRHdE-k3YcOALcgR9dntE2Lxaxtw1r8fH5UlY1lbh6WFHgK_oFF9yCKSgFCP6hDSKOZpBbhJRBbOVFpKPXBsM0BEDZ-ThxUeh0gvPs0QalF5BagerkdsiYw6xV7M6DREIvSxiCvfrYt0-ghDXD_BwtbXM9G27WAZy7jObpq1W7myxk7kV-TfFQbSqHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاطرات سمی امیرحسین قیاسی از مصاحبه با علیرضابیرانوند و جواد خیابانی؛ بدترین مصاحبه کل عمرم رو با علیرضا بیرانوند گلر تیم ملی داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30139" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30138">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnTexIUVTPiSw3wz7bYYNWTbvGZD3Py9FVbXQvgjzQOfMVptx2DtZUMQiKKs86sTNejCt_SeyWNfZUYhSXrd9k-8d2SV6-veudj2VgX5PMEztGcOlA0rrz7R82FKStAEXN1gLpwVQZFWFq5r3K8fr6QxvjOdpVbKZUPizIvyh0mBfj-p8uuJxA9-Acp_NIUJFXHggKXDG3c8PrWIKKyUOGlWmqEM8msv5UywfOP7sI-OruAgpKorjN7pqfOUJnFzvVCzQK26z8wfSZn8buZgF-It-y13cj1_1JekKSmdSO0guM8in5y1dbae2GxEFUJD9Wb5aWa_nKOcgFZuz67XQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30138" target="_blank">📅 19:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEL4LAZXRrCjCQLbqmIYvsOZJtdasP9HzJJJNS4CNg7lIdXfiCFoK_hTl4qGs8JmunB61h66u1oKcuoolOo5Ks--GbV1rMBKko-iHeAlSoThSBf9XuNIOgR4Iojldfg189suE8QqDFcTlslzcywm8ESEjHaIdcohBEfvN7gcFkHSPQdjeoytQzLEb-L_xUMFsiUgUlW-5ghlyTv52GOH40ctd63LvAZ6T_ZnSNA1zW2Yz8o-a0NZVRLfKeaIfThnRQofla87jTbNA_erdBmSfVRRGfECBOyr-es_60UjXkfILqkCHppd2wahZjDmLRZiBqz2YlbSxPRRPCKmsaydtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30137" target="_blank">📅 19:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwnWh6Gb37zcO6na9WV5h-f5UUQ5rzsqAHqdjfWZ-XT1pHz_MP3ZwiDTCOp4jYEFVOYN0Q_muZNTHaPh31z-j3SGQeFTEvebPsmyv4VoWA5JvHvCfa2VALYf6wHrxaOfxZSDTogXdovJS9goJmNFETp15GBjr0ZGIPpblIQrngPEk3hfry8MyqCeAk1cCUDOpJG73eu0VbfHziFpvlAxqlIksvmckgkmEiM_c9GwdJJm19hgB6JIY-ZX6qvoNaZd4xd3ftk8LpdUi9gj7g_FOUwUEsJNouEa9_iiaZhrWJ2BWz9od6cjyVO668mxO25Zf0b8tCofnU1J6ULFEAGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌ های رسانه پرشیانا از نزدیکان اوستون اورونوف؛ برخلاف ادعای رسانه‌ های ازبکی باشگاه تراکتور تبریز هیچ گونه مذاکره‌ای با اوستون اورونوف ستاره‌ازبکستانی‌سرخپوشان نداشته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30136" target="_blank">📅 19:21 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30134">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=JVT-DnZbut2-vfbURkCkK9E5Jvi2vAH1x8_bzBgTak6FYOJJllrJGC7lf54XttY4kLk6MlQvSp_YFeeENFzpAfHlqzzb7r5ikwEj58KWV-BuCG1XHHN_V7_pBuEEoxXYqhR0xMlCdpzvtuHPxiL-FnXoQ1FFkx99Uszz-osCUj57fKvhaSTNbW50s1gq9oZ9lyhle9lr05kQqFrtiFDYKj5c5q-w1JoR0fTN68UqQqI2pFBwyCGhp3kdWfORUVMyva-4_DcezgWfRTVgKZEVoXRHfFkaoOzAnJ1fJovb0bpLlZWoGP4OKnQKsDSOAZWHHw8D4hhD1N4Hr0OQfyGhzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb0177e91.mp4?token=JVT-DnZbut2-vfbURkCkK9E5Jvi2vAH1x8_bzBgTak6FYOJJllrJGC7lf54XttY4kLk6MlQvSp_YFeeENFzpAfHlqzzb7r5ikwEj58KWV-BuCG1XHHN_V7_pBuEEoxXYqhR0xMlCdpzvtuHPxiL-FnXoQ1FFkx99Uszz-osCUj57fKvhaSTNbW50s1gq9oZ9lyhle9lr05kQqFrtiFDYKj5c5q-w1JoR0fTN68UqQqI2pFBwyCGhp3kdWfORUVMyva-4_DcezgWfRTVgKZEVoXRHfFkaoOzAnJ1fJovb0bpLlZWoGP4OKnQKsDSOAZWHHw8D4hhD1N4Hr0OQfyGhzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌پنجم‌لیگ‌جزیره؛
پیروزی خفیف لک لک‌ ها در دیداری خارج از خانه و آتش بازی تماشایی سیتیزن ها در اتحاد با درخشش انزو فرناندز. گل‌های این دو مسابقه رو حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30134" target="_blank">📅 18:42 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30133">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsFcFEjuHl4GIxgr9jVz1zwtOT9HzoeQOpft3Td8etSxeWm7hZP0yf3VLuff5rYUnwD6IJfeGNREgyqIHov3fhxpk6yw2r0G4MGgdkEUf5kyObbdJ9ThsHcZqUoTf0zRkrRoFFqYQZuqNS3UzEmsx7nJaBJk7hD2SJXd8lYcM1KRkR10MxzN_spJQUl4T2cbODb0RTcOSDlKSmPr06h25kHotz86gvSJZ9Qa8MVBxrQtWpJXPG_POxUfXQvMMe9Wth_eVUW82xDQB-TGWbuBu0jPvw15Y27CSqMHfzRsLi-ySUMX02yK30GAq7EgZ8XFipkwEWIaIuQmvti8EKvFvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رفتاریکه‌مایکل‌اولیسه بااونیکی خبرنگاره داشت این بنده خدا هم ترسید اولیسه اومد تو میسکدزون ازش پرسید گفت اجازه میدی که بغلت کنم؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30133" target="_blank">📅 18:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30132">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kXKn31iUyLiNzhjwVJQqiW20XZWIt1HvuTmzUg59DaIoLgbZJFuzSzNTJWgfyrJ46zr5eOcrBRkoxNWjBblIykBzlSdNm_HYfvODL_xzNAZyUOA8J372IDm-V2Ko9iVHa4DVH5We3JnXje-Wj5MLDTdOpJZOcfIz_hqyp7jx8Mzr-3pUxmpO0XLy3yBS6hKuhyuBv6ESgYdSoGNzTK65Wnety3qfK9sEy7h_bBdFlTB25Bsi2WIi2bEyMw7GjvGRRonwgRYryBgoO9h8awJumKtj2fQhFfp5ytBEoEKdtijlwAG6KRLcZTrVVliYjhuRsWKVicY1Cxe9i_A2-1g7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
پارتنر لامین‌یامال:همه‌شواهدنشان میدهد که یامال شایسته‌ترین‌بازیکن‌برای گرفتن توپ طلا 2026 هست. اگه عدالت برقرار باشد یامال برنده توپ طلا خواهد شد او اسپانیا رو قهرمان جام جهانی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30132" target="_blank">📅 17:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=fGhmUrxAXeK3cEb4NsTb-br2Ckz1V3ixFlu-YPItlieNEeyOU7mHTSQYzgOukmGHtkH8TTmqgd8Mu_qbhQ0MTLcGhhvvdg3wfNEKypcpeBiKSLNito35fOG7WTmbp_n5UmV6rI_HxsXP0O1GlN4z01BDqKf_6zMAAIKneU1S6wrXaQhNA6_FESrCr35Xd7V-2T8KJbvnSI9xqdp2hJHoh2hPjeBKQBom4LjmUg91mEP2lXQjPMnRzYO9KExM3KcfgPc4erhL6MTeKpk-D_0NbgGtAwvooZ3Ct6UEpMKTZck7NOhAs4jctYx2RRxP4h1fh7TLtbKI4pqaXQ3Ytx29ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=fGhmUrxAXeK3cEb4NsTb-br2Ckz1V3ixFlu-YPItlieNEeyOU7mHTSQYzgOukmGHtkH8TTmqgd8Mu_qbhQ0MTLcGhhvvdg3wfNEKypcpeBiKSLNito35fOG7WTmbp_n5UmV6rI_HxsXP0O1GlN4z01BDqKf_6zMAAIKneU1S6wrXaQhNA6_FESrCr35Xd7V-2T8KJbvnSI9xqdp2hJHoh2hPjeBKQBom4LjmUg91mEP2lXQjPMnRzYO9KExM3KcfgPc4erhL6MTeKpk-D_0NbgGtAwvooZ3Ct6UEpMKTZck7NOhAs4jctYx2RRxP4h1fh7TLtbKI4pqaXQ3Ytx29ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=HZ8gnCkMtMZF2-ifMkJ9ub3yv4wESjWLPgROBWjunDbJE3m0xxPKruJ-jmLWiDl3w75nHaZEzKHw0_IWyxd0MeHKQvA4lo8mmsUHUiwRoZVLk616xP4pBzxmhwcewvLUj-N1edia86Mb4wuvYlVw4hSJcWGt30b58PYD-P75y0imEtYubCDGSsJcBjwkmJI5r4BR90Zak8HUL_jLHTjkSRXfSSFWQ7BgU2d_wxlP_ea1r_4BiSBUEUDdzGrIcns5OcqDKl5ngxHioG-klWliGJevhdGY2K81T8vNtsjlUM_iYVFXg4Zh5ylhzjHD4wAi7WrrhifM0mzM_b1aYJO9Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=HZ8gnCkMtMZF2-ifMkJ9ub3yv4wESjWLPgROBWjunDbJE3m0xxPKruJ-jmLWiDl3w75nHaZEzKHw0_IWyxd0MeHKQvA4lo8mmsUHUiwRoZVLk616xP4pBzxmhwcewvLUj-N1edia86Mb4wuvYlVw4hSJcWGt30b58PYD-P75y0imEtYubCDGSsJcBjwkmJI5r4BR90Zak8HUL_jLHTjkSRXfSSFWQ7BgU2d_wxlP_ea1r_4BiSBUEUDdzGrIcns5OcqDKl5ngxHioG-klWliGJevhdGY2K81T8vNtsjlUM_iYVFXg4Zh5ylhzjHD4wAi7WrrhifM0mzM_b1aYJO9Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8xV_2g2kV19NZOBk3Y9w-qXpajAx4o9W4dW4gb1i7qnb2gxO_KqKzOB4pTdAIvtCIlv6TJFpHGcOWnw714r8dEWU8JeoNqF8xXIPeG-Mp1WcVfKvDLlcXUkn9mA5IfHZq0r9zLBYwW7_2Ef2JSYSE6z1alo4zYGfxIGETMG8bL9ybR2JHNBjYg_whQe2w990gm43OFZdZmh80m7EwqwVpXX3fMcZM5Q2k472xNdw0eEwDlhF4AW51wIQjqAUH0Ops35NUpW6vR8NxxtRZnXZwF_h30jFDJKAQUEWeegSv4BDZTZjI4wrW2glAUS5pLGeo1zBBm_jPRo-RXAQjKRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsIBT9s6pfIZE17JGfyKMN8RpI8XkBDYiLT0yGEAZ2FlMnD2DMUslSQOQPfA2knMVw2eKp1dqm9KDaNvrIL3SIOk44NWySiD4GNMsy0xCwoDu2XTQxMdCrDmzSqfUMIBZEhu7ct5fv4p-N0ee9NYpFk8TAa9MBHf9gZQX_H4vW_b2wntcXw2QM2RIt0lOOe-4A5mZUya8ThodStPJe18LKflDcfaKp9lGXR3qt2csA1AD1R_GLxJ-1v2W7-uvh_Ui1BdK-MQXW3sCj7D0oydmpLjTHTlNnKGAAJ9kw_IdCaFUCXNC8c8H7dojdRdQ_hgcGp8R-SneaDFqeBou2srTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6_FpapALdvVM4ghWOtmwK_gSLqZbnB59WWHcVQXly7Tbp8w9KflokRN29nKRHmNpchLw3-PXrGSiQ6OpExTMP-1GVUUC0IcIcm9QGjchdR5bB4us3zleI4ytoNIXYrrysphyMixpjd2g843g5OTDUsqxiPUlQ66DeKo-eyAFx9pvmHll1VGzgV4vXY4099vTrz_vQ9FOYM43Bp-R1j2tTXqo0nn6djFf7IjRagpHPf9JvYuKoSMnmomYJLy3KIqQgszaZj-oGxDSxsWnfXi6Jt5nh1gfL8J9MSBxy4kQ-U6lU3sBLiezCS8FSRBrF0Fp2mapPUWXEPLAvNfx0Vbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTJ5sBfvalcmj9_safd0IEP8ugMRNhZ-dSYHGncmJPUDzahD58_wjBNkFGa0nZ7Ib4RCHb-iL5-1v-60EOuXLXbP1WoxdLuOvDqPf59BS-JABDooaDc0UhcFD3X702dDjG1cWAY7dfI0U-1ps_dTcbhMzYk22_rkOcRxReYrlIYCDtTwOaXPFPT4FCl-1l20Ziw1RX_f71hrjqqnIIvVumXUVdg523tCIUHOMbkXy_JbLW6jO5k3QRE8xzPuE0GaY6Ki6LF1BtcSN00-TFNqiZW33Fey_-IetFerWRwzdcjcpdy-O--lZTjMtvwCQe5Xl4Q1UQnvPfguA_Oe12LYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJhv3DXz2gZlndqaJgHhgUn4q4aSwduyjJeVnSnt0OEdASgzULKSluOatgMhQcTMGG4R9if8OtXnbCtGw5u0Qc-sgWPGAu4n6eZyTng6yuzimQl3kotKmThms1cF7SyYrrIJe7KcgmHDueS_5kUj8MgUzsPe1-InINFnNQ-fRTzLAqfIoLwzGSFDP3VmW9S6AHtwll-fcmfEGgY2XWaQWGT7kQwT2fLQaJ-aylMveRShse9aqNURZ5MDB8BhDnfR37a20-8Cupx8jNI0u44fNvB1Z8dfV_GGOdBvivUxsUqFsJCs42Mxa_rTlsjt9GP6wneSLUtCRXOQ5OaiPI-ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FIrgEqSWPVNW0bLCZTmDBw1Edmk9fW47FjZCmnAvEPc065K9wgzR_UBuncTKGsy0u5RxrhLHreSHmXBon3cwtMGsn33L0G4edha6HAHuS-sDHTakdcbKbN0W7l8nXe-WM9NW1Bynl6iYxCDB8NSBZR1OJnuBpqWTE1e6QrSI3bVh2DAK_A7EaUcVt4TJPGJQX-HAriHlGFEnTk9FGseH-uV8msK4uwwxNTUM8QH5Or49qVVCEpFgJn8fabX03p0dx83HVukEvNg8m7tUU03RHxFRR7snd5wCfQAnKH0ED4SPD6Eg4V-iCrrqO7WROe0ST131RQrJysrqW5Rp8-qBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kNIdAhHAQGjisAr4roNmNjo5f9ZKlj-wIqXQ9JMpHrZj4iRTGjN1ggTynBy56RadYpI81hM9fiAAzB2LCrLTAkTuy0S0DaV5qspbQ7SV-n3y-u2kpsee4JNvPeFHcuWwE_B-KNoQjEH16oxlcmn9J4JGJM3GvBtQpMhEK23tM_OffCiQDo-O8qmJSZ2kBwImhJ7SoXEQz-y4RmqhmZvfOFCfqytimUBvAjAMj7Z9kN9XMNUh5DHYnh6XmXhPG5_VjM6WNz9-bI7DP0gRh9pk9dv1rfvIhcGRYmZ_5rzhrpdfwGQkwjaduFwyf1Au6FjvBMo_pD5OuOK8b0YBOwa89Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mg455Z9VIWKIDWKnWt8kcWnXc0bRrRUeWLKkz-5YBwDPmhL_H8xap0EwiHLTJIEqJskeNEoeZG7Yf-yGA5S3IfqOtJZ7YyOgUZsSN4wYnLfzVHRVArU34klh_Kkvifl2m_6yHoNmc4pg6XMn-HWvc6EwpraSdi37ExH_4iTFGiW38BuR93otEgra51GOjaMruWmhWYC4enIK-6KLy6uEXQ2SWOz4lE59WEpVIyTdl4vncaR0q-0VdiYqnptaJoPg0oGMy1WGuG5g6mbOqcX4GISZCzCYS9gHrlPwwFaiDnapynWtoTskBwbw0h0NVMVjLB2yZ-SVQM5Jcxkxm5Jx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=oqf_Vl47m5tBBnWpFQgd2PcjYMbxw2Q5gazeh2zXp2HST8vdTQE-aP9JWpqTQq_ay_PJx5rbuqJTikOM3UcXL05U__oHiUSQkft1wnhtiN5n9Ht50fsrVVLwhp_2o3tHvHuVpV8WWTN-hjZhOeDKCccsRfM_Hg8K6OBRmke_S0g4ZZx6gX7UW4XSPjBs4msoJz8yJq0xt4lD1yVI4HIJrfZp_Fv7tjAFltlUEsCSu5l_kIKNVb52rzv3lJ4H3YAimpM5qlnizZ5bM1-LedAcNVas7J9Gyof81aXuiUQ5zcD6fdfrLdnBpIUNJLTabOYI50fjN1b6coWuQ7A9Tc2Qfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=oqf_Vl47m5tBBnWpFQgd2PcjYMbxw2Q5gazeh2zXp2HST8vdTQE-aP9JWpqTQq_ay_PJx5rbuqJTikOM3UcXL05U__oHiUSQkft1wnhtiN5n9Ht50fsrVVLwhp_2o3tHvHuVpV8WWTN-hjZhOeDKCccsRfM_Hg8K6OBRmke_S0g4ZZx6gX7UW4XSPjBs4msoJz8yJq0xt4lD1yVI4HIJrfZp_Fv7tjAFltlUEsCSu5l_kIKNVb52rzv3lJ4H3YAimpM5qlnizZ5bM1-LedAcNVas7J9Gyof81aXuiUQ5zcD6fdfrLdnBpIUNJLTabOYI50fjN1b6coWuQ7A9Tc2Qfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1BT1JL0ensCzV5crp5kyEAOH3-UveiAllM7fPNRrVYnWMACTeH1x0dax2LspO2Nu7fhmAcmoQ_UqRMb7Z76LfyLb_dNV8wFRmuTBk8vZODRqXvEicnLJ8b74C4qJnQE1xhu4GsKkMez-w0DNGAc9LTK4OC_YTdWuMoQh3oyC4UIVS_4W7h_xiQXoi_HT8lvAJ_GKG7Cv6075Zu2Q4Ts_mCJ5GKSX38o4XfAswkwFZtP_0VsKVnO_pmHGCO8D_WP7Quh_d1Uq35qwgeX69H8pj1UvYTrYwTYf6lN6F1cimj9aJrCWDxD_k1olk1InKI9c0uE9EfaSu1S7HYetuabxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FF6B5dx6tRrbElUGp-DZjyML8TVUNt3WCcghiTU1z3MOPGRB9vbsNm8S5FRg7rfseg2gw-26AqP1IKNIU-xwr2hL9ywc_ZeJe1CGPy6wS625lLMoRJNjNZ-L2E_xScrybyL2wq--AJ_VgQOeeQ-G-6jW-ntGBTZa_KcG5rPoh0vQ5I0FUyqXJqMQnO6n6evJTdHmYkftEgXOgVInhPEPvYb4OMv6ngrNZoxDXzbEBmQ_8mLM5rKfQhXL2EBPk_yJBrk532JlCWyGmNzxY1rfprmkf4UuouflYyMXkgOBcHYUSuhIrX_CFq6t222KTldId1Aq5LbC7fnhwdkDcPfLrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VePK8Bwk6nci8rGCuAVW8xLemTqr_Q3mg0xtM_56lm5McLV6wniBX_dy1EuJUuppfeKMqZ1-qXR2wPNY3VedOTD-T4UJKxkF5tnHFJ2rjq6uE9vgxlYegBo-Goy1d1DXnnhsNjXlEoPlhVTDN6hawCfbcT7XoXfOoqi4uag1rDLenhdex-JuCUjtfxFAlOU8zaXMcO-6kMTmuSHsgI3ufEd71hJCTT0KVew86DEtxvWRA_Z3UXDYt_yZbAdvKc2eBGEHQw0tn0W17OZMmsG4_lLNwFSnI5SIhz5-PxLYQb6WVFSTPDOatomuNGoK6Kb_2zbgCdMKjnszdFrtHLBBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMoxtOuFP2-c_QcaNwQzRksVlktBJz1snpH0wQuHD-OEvNXq0u48o-X8k9QV-EUnyml-XwwLStHjPF0dvL9YEc3vB3pDI7_tB2UckHj9ibrxNFuS5nFPIZtCegYuYiMVlENON50fZ4_VVakysCwgRC7qL96aNnTbwquzI5z5VYSUkIbHDFay43HV8O-YTBWddSl3OWDxKGTog3SWzp3_kZEpAn5zM4LUa5f2BwSWtLtah18V0kSBazzb2YSyvAk45pVbMTjUJ9wlOzgpxpIBC9Pay68jG4s-zg2SWDqVDbZmN9n9hZueTRy9Bh6qSieNaZg6zBmv5RXGk0EyOJ-UNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCVsVrcjTpZIEgIV7Dw4SbeyeXIgynf8UFyWvcOyyD8groxXqgIpXPdwpY91Tk2LNjfhekFekbzFEeeJaO9NA4dVyK3Wh91yK1NOtsTJPQmbkj_mB3WmKbZAXu3rtgy8iM26oD3sY4VADjED2-LLTC_Ov7erbsInjcfkoRtGGNnG8tzvGZI6lPR7Z2zno-_85ctLBh9kPhX6sQjTUPmTZobIJgTyJsUGp1h7Jjfq_bn8gpgDaecEnUDx0Lumyvv9tq_DF8Zc3N-3LitatizeiHAR4Noj7SLgSpwgBQyXIwvHakXsGD8LETBMfwxPirChre_Utw8MDikdAVXih88MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnRFg0LR5a6F9ZNmSi_x_ZuFlxN4bwnxcE0bkZ7NIN_vJVvIEUDqphJx4S_Jp8khwd_5GfTCJqJk9qe5TlBYmXcrr6-RckQi6xrxe8dBam_i1HIxTL0G4ZAYogbBjRNSp6aA7UhVhSIu3PzVvIVuc4d4EZhCpSx72eRmIaH0ZY9kNq1jt0KXeSfn4r7CrJKy4AvqQQ5xcRH8l43crdjseO59PLMUJn3jYIdWFC4KdZ8a1K3YzAucs6KKI2ybyRYfWoczqsy53Uu29-BvYPtUk_QvoY7Pv7ONNHJ7pO69294nzGP-7JALx_Bmvr22cKzk-aA9iDOjojgDhqG7hCPNpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnMbVfUm5IaC_sb5je2UHA8VeYB-1TFVze3l0p8gzIDEs-gxlx9mHIfG0ibC1-wFiMqsIjKu75A2Mf8x85Jq2IKT9WTVkRWseSMp-p6JURc2C_sIxVpzsUkjRrlmWTVcwfT8cZgjpikJXgtT0YRIKcalzrXCnHoawobhzDR0gil41SOpW1srB_vUWwZP96w-s2N9_FJB3gWa_DMLUUNEJ-jXfomeSxEXrO3rJY7WBmRRHe-gV_38scXTRVbNg4WOKIVbqjEqVeJacpJgpdSkPMcRexBpXwDLlFMYWzfQmztrSyLzJY_I7YZKcZIRHMA_EhveAyXE-pdmi_CjitunHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPgBOpaxFPSDi73cfgR3PiNR962bxugv7aEGToKmJW1LtvBavFSgWGiM3BIynZuf9KcPHamPNLngdGnaq3Uh_k6sawQSzvau1PL3wSH4MiL_vsFhO24zkbC9DrsKWuz7eOpaIyLrtTAdW697UJI0nbzWdMGKpK7c9SPy1FEK-9O5tymiDxmTvNzRMd1XHGKWCnBKgwU2nWEbEQpvpcbOuOG49ITGw_oSvSaTA9mAUR9pT4f5kwIA4oB-nfhK8Q6mKMzrsH3H57iraHz1p0DfnWCZWL6Vqbopyy3kBkPsCY9EOv55LYsftnvedHBvD98EyZxKKrwbxXxdj38olsqkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLK5QnupFyZSNVUqLdg9sEwsHHxiS-JwqoRw0DKpV6ib6uxu52s5NwUvELnSt8_cfuvy6TDekU9vKgcavMt5ZfX-jfNdKvxv11burmROUst_4-D2AEUnm8ukaMD_DumBoAowLemDvaHSsrzS22PMZbanum9I9uWwJj_rUVhapLqsEv5AdlT_G9wGUCIzRzAJipTAAe9ickfb1xUMM7-07-QihJRqaLlxumseivKjhy9Y6kWImyHGROxju6iXJ3kh76aXKb60auuHg9itD4VotWFMmljuczE-yjcKY2gAgxNBzluKw0dD-XOiECyBV5fssx9QlOojX1AeqCl7U8Jfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlwsaxS_1SzKFkTxzaatLm_-sTkBaATDCOcVUPcc0tgRmz_ohzioNpTfCAue4rswZ4gXb64wmw8wvP_RyA0uE7XUW1vXOF5WEe6s6I2g_UOxG5ErfY6W1M8Ua-b81hyqr2oiSAhvFyFZMR46-Aox9XqFrmFmbH28NLDbZOHSCRb0Gn9nDZcDHflpafYwX7IhKylVgVxOzNkY30pjj8uAvlrfFD0bQYSnZe42AY4xO1IK_eyx025jr8yLml2isoQ2areo79NsI4OqnQz5A1q9KZUXKWqcflfbpDlKFK4xO-JRYFYi4GSt1HIGz1Sp2wgnRHTWvbS6YJhOL-d9ivcWUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_ojgclrqUvrixrdKOA1z7lyG_z_dZzlJk-POM6PMxroovXH5xYMBKVpEwgBOr9YUy3w79FMW4EiEtVJkOQtzeONjccSEL3EAbISIPcFCD3-FL_crafHKXB9Wzpb--OxvP8igty-yb-8UrL0U8K7sWTZr92HLR-c1NW4urIkkjVDq1gdwjXHii766LGk9bl7_ZdMvRd_01Yo6xFIdWwKKC_yRi4spOemtG93ztFf8O-EYcRpw_V9uJflohqIDho1Md0Dshrgm_6Uh3OvrwV6k0Vr-JurhM4rO1U-P5abp5GqxwTsy6p587ZHgSGk8C_d3A2X6DGa-eJ6K__PM2Lc5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZhQCWv7cI5GNX5l8Q-pCAo74e3xqCQy6h3hgX-GS3zH9nCB5dyEA_6BjZ8sioG5xNtFIoiXCus5CT7EIVuhY9i0Qm45f4fFR6hrJwmWzKR1PYYmZkwyFYqJLVwPljLxWH0Ccdo5O2rtKZ9sUF7SyN6_skf5CpvsPznx89pNoF8y6jD63F8ea3wDCT-SQEnqSyZnuBegLTih0WhXB0pHDKS_ihcMB9W6EnpvMfu6KMAcdnn0_dHlW3fMydL8okVlK6TzzG9NqmMrUMW_xNwvsYIK3mOfTExuZbTuRyXGfvmUUbPXvczqmxTVq3pjDH0FrTK3-lFTd5RAOWUhhrrnrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjunW6JHoFQXwVnk-tTUTCT6NX9vhcPjZFfvDgpNfgslGgd6qu2GWJ9T0-iYrmNEzdv_ZW-8X0JpGxo2zOFiLLSeamk1rjYQ-IraC1RYsNUhJfMWuSP4nJitaFSnBZC8ZQoFFUzDYbi4_5bYRHXsuqmVe9BWPGnONbQziIyHAUe-FRBqHFn-IoBSEr2HzfqiaunmchF0PHH0dnN-tzbF0kBaSmgdgd31xSSSokN30wJGT5Xb6DX45WweHozzQB14afVqDpcJFn9VHaJ-s1hh7YniREQae6YreFRgLcRUlMyl2k0aZNcH-WBKGriePZXx1nXzVk-PQWT-CcHoCNflHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5OlfeP1Yl7oZhp8y1oVatY8DpeSGXctpLi6J3JH-mLoIgOIwB3-hI6mudGjPY462opnhMm6tM4IRCehr_g2yB-f7LyDX201-otjna8IhRlNpuvnR3V2IKJHZHn0Wtk8zBJiO4ZZfD68UjoXZffO-wmiM-HnHnkl-WWdsYjmqsUCtd9k6N6ELYsEg2Zyf-xH6b6X3JG4bn2Djyw0AcGTisqZh5N_poWyad1TOi19MFeYyS_twzS-bChaIYDFiFj5vnwS_TtgDH4pTPZwo9wDBJnAXrKw9sIERXfCHf82BkLrVIXjourmAOrA8o9cS5TItHYO_6zaO1JCl6zOyJu2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1rgtYnkGMh6Xz1kcTHoDhSgODqqRVUT1bZ-1QO84NiLa4skowvQ79rzDyRI8Ao9Fr_-moTEJ9mQ57PP-kBMW37z55wCNzMUN7KoPx3-llD7gpA5oaSCYgixZQAL-w4tjZ8s3ejgXC3IFap5YplMmf3m3fYhonhhJI615QP5yIPtL05RputZmIcExNtQazYCo4sy7lRgRHLJAXFjQP30M4Zj2r1KbbKwhU3fFenJpXsXqAr1V52-qLwMTJPAB-2oS9gGlwl6gOqeQzgkebh0mqgxTpTnRYFq7RK4BAxM6erlCFjRdGQRKB-d2i4IT6Sxk9wqpSf6eXy4tcKnZHn9Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oKB5EPGE0mSWIvpbT_3yVjZ_5oJTuqW-ou7XT9q2aJ5bd1chfBV7PU7UowMe-jHNsWgSuPpmERIjyi1B8pd7ZrheybKYDloVTR6rMa-eAE-WIAmknrEiP49VACWaG0eutUwpftdl_goo0tAUbOi9JlhaveBe_YvW6DCE2FhiSvXtKetab6xGJbUNnRLjeFbnTFmSpR_0-OGnoVXw0s3xyg4X_bLIRNaQxNNsKpPm1sS0A3IDiHE4Ke-ZmxUh4OJwF34yFqyFkb1qRxfLoaYdLy5wS4SDmqMIV9Ov391OFEl_cWUgHhHo5cElXSO-fXTPP1tmRUq5gS28mzadTh7WVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7hg6Ar_lVnaGQCKPCBAV03jw0h039sBKzghO9ApcNju6gbdC8L9k5EyQ8gf-fLrGrHJhvzQi9K4RqxVeObL5jbz6BzwUuBXb16cNPIwgAg49EXJlSHLDt09mxtqa-QZAqOa0CkRI6k5CxRqIIil04aRhbHonLiDnxF7hNsUWmFUquCk5EIrW_yvaKpd0zo3xwrryffo6sY8eCgcNq2wBaFOL0jAtk-o93S6V7TE3_IXo0HHCORTcrKWM9UHn3UC4F7oJofWYD4Q4BLeqz5Ulijdb4pUvqf5Wy5eK4ypbAf4nV_yIdqo5GYT5zZLvFhHue6z2ZzJqd_Z4HNFZ4YUdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xqwz4zWvBIzLdkOuF4GckSMDprzbBrMbI1ngu0BkAkY5dPm2a7n4_1Iy87FSngujwHiwcgpdk0yl73SFtoNyW_y9X7aHn8x4AtkYdtmqb1bK2FynEITowa4F5WyH1MUikCC5jTwg_YwGtOYQvS_mGIBVus1xH4SgYX94Hd_sZnkvxVLCzzHFi2xC4K6fG7Rj--89CHNx42tcSNyaHJif6fKl2si9tUeEHd73GqCwyq6TQZSpzwprrfZNKM6aZEQF_2fATK6Ni_wg3jWhvD3Rl67LAHP_kKWlRg9Cjl-mp_OnSrK8nnf2zg4OO1ZItrbEu6Ode8MgivgGI6yKPO7q8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C203F5VO-p_3tua2o9GbgY-bbn4_RlonwbT2vXWKrlRc4_FvQ4e1SNcOeYHYmFfvjDAPfuY6LDUv8SN1jTYybGg7zYJoMukw0qH8QOHn0vYONcdc30e_U5ekM_m9Obf_rSK3ojJhgC6iqcJo-2glLL1VYNm3pTb6IekbWRt_4AzHumlrdkkcYMxpio3Fbb8OAK9vsX6QWu6BYe41-Von9DZCtSnqDPd5yyKnDxZJlWIh_d6TYQk3rh5Lc3jaGv3_eHqeKu2b0-fKLatiDDQ1PuBYrSjLK1mHvd11vRZUGo7FugfoTQxrCQ5igCSvzpbG6bC5-uI5K8CzcQoKsYMeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxpn2ad0JKp5rjDUs7rwyf6d8zjFElhMzkkhYIU1XjSpmdlO921rkJTmOaZ4wA89BtDiDlL0-4ZTm7uI9MxamesDAzWm_rPaPoo90BC7hjSfeaYBAJqU9y38uqZW73QdHOyR9ndxrdB4Zp6UqcC24DKlQ0_m3oDQrdDrDINhAuKWyrrJk7sQd9cO25fZ9YtyJ3aBgCrBw9lUffLBvyK06WfkdaKinoOVqyDowZAbnjeFdEY4O1FhZq--xfOQAn55Ks_8oU8Tt3XY5NVaZMhnpBYgHxOfT8upKGmfa0URJndikyfFkmjjOqidAo1FE0_GAprPP3JLPGAIVg54TWtxWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YavETOwIWJbv787BKcAfkVbtQ1MYDrngaPK2iZk1q9MfxS-P96ubND02byqyEG2RFRocLsReXfWlqYWEsYkJyZNRaYyLu71mqlv1VI5wuuapj5zoKF-KPmUuw2Fsf5PEE6SrPlRCOxnu4oIz1qKY1vwylf4tFaTSjJecxLppVmRrPdkO-G5-KKCzvRdbINq-GPG4k1fBsfwJ5xXr1vQzhVvXH8dFFLzt6ZwmUFUfKWshr36wE0gn5DzoASMGE1iZE5KJpggz06p0WZQs1IcBk6w12VgjkpYKEUSa_N1gJMnMMCn5Hb7DuPFL-kRaj7J69XtIQXHan_HH10tOfc1FpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j31g7TV-4KUHH1HbpHNM1PRdCRRCZHWsUT4XATaciSJoMoHLjds7UGCFUmS4-gk8lqy-MdsGarbtVtDzLiONPiFPFijqK5z3iL2aTBvNNlGNzCxqVKlFGe1UMQOcXsYppmO31xI4_1ssTH4YbG8j3KN7g-EK7a6BU5RooKs_UwfB60gfI_zIFodsQl0KQ_bjMzwVtvW6ByeentEdgm4gjklGO_yv6il-BFJsPGDVrpIguJaD4QOXC3gxIYh0iWhjkkYImPXJo4pfm4MzOYOenGE3JsrZ5qTuxseKQRRtjFrParP-8A4h-earf6O4nnLAab1eVrPfyMjxHB_xI_9z_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRpllZ4ChsPw_lQGf7KbRU4lW4vXTxAdvsoQiiolQlJxVTrMJauPxtfNPmfSKhr_V0J_ATfZj7R0nrIFEF9Xb0MJZPX5iCBgm8fiRODvNveo0ulGvKS7NQOT5yi82kcVU6OvF3s9WJGDC40qgsu5-FvbhU01AlzOYV6Lyffb3xLpd0tY2Cp8BXcdLV81GpxLaIj9opBXkoNzXmixd8_52T_f-M9lABHdVxYZmY2f5bgurUNGp5V5ynSkbQum60VdS-d3Wrx47ZT52B2Ng9ARoQ0s5UixFs5fet2M8pTiZ7e8lib2sURo6Z4uOjtab7TsxIcPGnGvQ-9wSGiH-YI3_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUDfGldIeDDlwbYTJcMPrcd1PRIPTCkxeJO6EpkLGRda1eY0RyG3C_VCt6zQrXgFMavju4fHggtN22c7BCx_WlYpYmB4b4kHP7PU5yeksAt22n_izWpRwZWWwEwEwlwq2dIIC-IpVi32_5HVRo-MqgDcYl9z_feOUhJy5FO79WVni9QbpVketDNWDdGSrw1-5N6x8LjHW8FKU1vPvelcuEucyXvx9BM5ApLvJ-CzPwmazVqqvWsG1w0pARCoveArtZzFl1yD8zT2reo2B74jcHuq5181TPQgKfnhgmsvgkG9OSUj5mkPh9t3VR6MzaOsjh4KjuFidvKiXXQoX-G8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9O5fsnbTmzfjNI8QlAradjnXGM1_gRQ8-VmQMjenGTp7i-NePmY5ul4E2cdKuJld6EaGJ9G4eJm2dKkONMzzzRc1i9B7Dua0RHYuR8-1DChyNmmZ-BUlKnUGsFSB2SyzBJZ3I8Y64oEE_MqFwtwB2KcUFHoPPttgZBL6kkDL52fHPGhBmdeLhr-HQEqAXtKVmJl9yW_w0EkoF164ZuB-mn_1wWLitsFNW_-FcahxX6ilPUIBW07s4HAxH7G2u4WHeqJdMzUyL7xMPXhiRY0dNdENKJMsbEaL5se7xCWBRSIU8I43k9eIr3-M0PblN-ETpiOOny7sblxfSWXMlxjhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30087">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hI_UWxylCIfUGfnSPDuuxgZ_Jxlz3IYhDKce5gdb-qei86a_6ETPDTM78QJpUCO64hjDd_I9efuZ6WiIBfge9Q_PEZPAEpQFymgJ8EODxhhefWg23xsZeIzeGLmfJ8XLMhybb1D2cxIwhyRvqB_2LeLQi8v42uk2XtgmTnI5vh5cKofobWvdfmkmJpuVOLMeKuAmqn_JGYZdlsCMw9p_8HMhL-giN_wcKNVIyidz3rYGZ6mRMovNzy4Ng7MI85QX3YD6jwP0HEKe2ImYUxCPZT3YYzZjstVF4JyvLe7EEFXx44Uxo9pcrXSw1H6YqihTgmaBFl51ficFkvfiFAm2kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30087" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30086">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOsUZZgL8a8khEviPbKmPC1NdiIbFebudmhVKecJlx_kMjcKoxZahSB1swt2vIzWhfv0vppyxFlYiIgRWKDfe0cL_9CYH_nFDmLC8frZk-3GtbDzcEhLcVNx_3U-DZkEd9RCrT4ARl7r30l8bZ4qOTB5jh-O_cGEIbYMNzAfGjfdB0TROVCSWfgiwIoIIBx0BIU9afFc0hVHySoi5Vr9BqVkfjEBRw8VzyDDdH_gDrb1SGBp1PhbxM9QsgWrPcdIWdSSUM1r0zqUepnAB2OJNMAA5-73x7atvv0tSWWurYuVdAMWGentney0-hDcRR9O8IQS0jODxnNlgvEn6GFVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30086" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30085">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c9-iLZnpGEL7FC8GinRAqRiyTBd7vjbatEGPYMUnWJ-F-SG-Hgo2vX_khFWYEFjj2L8H2rXp32Xrxs0aLVfsMelo_FsAqn6bObyjh5opwDNdQAZGVRk8UWpwzwudo6wLygE22U4cp-8KjqoP2lfLvpdVJbP3k9UXif2XtVJdyORWvi8K2YD_72rdxwQ9X7oLZs8IEtNLptjiBIjRPpw4RzHCqU4S4O5ODT3WJTXcJfGOy6yVu8e7jdpn-eWliWQD32RnQ7sIR26gVgKp_mVy6xMCJcXPfvhWybhXMkZhFddiIi2n4Eo8tSiWhYFmXUS7d_0MriFd4DiZnfPDbJrG_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
دومین گل مهدی طارمی با پیراهن الوصل؛ درحالی الوصل امشب دردیداری خانگی دو بر صفر از العین پر قدرت عقب بود مهدی طارمی به این شکل از روی نقطه پنالتی گل اول تیمش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/30085" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUNw2jC6xRjEDYxMY2NPjvjzJ8I_0_oqEz-E1vS5DXrmXuQfqrW6xEJ3KrrKWiDChkL81igDfQaOlJYjjg-l_I60ClkuUWsIK1WQbzji4Cbv9Ko7VIG5FDnpLm6usy193MIj-PerdC8gon2cTzyDETQUN6cLRTXsRRr0hMEbgfhX0-1o3_3BKs3sA2oFLPLso8AdmnvTgAcsElIXhtNgG5e6kLkbzbl4V6613NXAM--psN9zHdwxGLSgxK7zmnrWxwvs0b1c4hGxp-6LCof_puCbSQw8K1kg16FzjndDjySAr-PpVIbifcAmwFZ-qBdlja-gN21aFY5mx8LLLfYq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZ18NEa0lYKT73MgW7OvbyJcfXT8beVkVmr2ViUa8JIxlxHITjBWaMaDraGpguy6R4tVL8fjdYIMjkHVnKfn0BrXt5XMZ8fiZja0X5er8uMPAdLII1medJa-7gmb9s0dmUsuQ854dhgBPKt5s5gST13kUe9Zc0QHMWdRlNNNeC2SCDfw2ziK5M0sNp00pbyt8A9Pf_2xX4-0VvhcCshbSgG5yHdRTSBMhGI0sUSiBg5IhtpXqpFeVMUIm7j3vty5maquRtrOn_Q_RqAaSx4iQjV0BEe-tuRVCcQGyTN3aw-nuIrcl2kev7vvdO3520XAk03ZcgIbuQJBHUvqoUZZIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMuLGEu6nb3klcW3u1aU-itp-8z8o_YrmLp5MbUdet5jmCsrnC8TalFAvRqBUTynUPIitiVTOq6FXiEqBoAKhm4IaDi7eBW9AWmzQKm0fWzkSsTZe4PigC2fB_XvnLsVcxbm85FmKx_L3v9gij5T0z6sbhXtZxixBpFEZ4fl1Xo9qXwPKTxss6lPgDfR3qRX95ydyLu83AXAjAsHIyjMuyOSXTaKpneG4zcAIFNb8tUU8PiUSG7Fc0HMB6dRbBMRwswQ_O6Y-7e9miBUCCEpb-ExJhSNF0mszh8k2cFYHQy1291Z4TKmXsALDB7EvTYCaHNYbvJLULWd5sJR8sxsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7LqqpurcUFCacvb9iXBDNz0-nGyhl2Do0IcfDtXosHexIxT9blmRA2ujSC_ScPiqaffiRo-UmrGeswvfMMac3-8s8SpSPGS1rcGsQF3p_lVlE2KCUOWWx2h_7Vgl5TNpe79Hn0UMDh9hh6nd7WWC8yDVwQpdyg4fkp5HpcQHASQxj6C4GX47yR6Ymavhx3mosnpvm5kxvrVYlHvOd0X4Y2N80WoioQQQ2kncTryxhOX10DC7hkgamCMhvxJp21oB22C-raXcL91-Kg0EZkCpAOI8iObryjwxc5o87eqjBCC48orGp3FdLWzCTeuP3NMS5iqLonvGLzuGnyNGqiJ5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=lqI67-WsKzH5_P5Qmf0oPUiquR28edWQmatGpA3m313EuE-7-e8Cb9VOo-ryyzeonasRXy0Mf2PNvowHtw6HNXt_V6MbiXcZ552yaG5dgimsR1ej2g7uxOTj80x_xUeUawvE1WACR31ZR4xdzX6WCnKo4c_A8xSk7HzktN4HyltMRqk76CxuHrG-nsc7XRgAFrJDzCo3uNtAOPu2xs99LtTreGv-OhodH63ZUUdHrFbo-PHLEQ_jPyBy-25eaznQmg0fvp5n-xG3cojMdE2KowSy2Xyqkw_GLRrdxOMpeOCgsexJutDCWrxdlgwIDn_xbUvf3USt3T7gzyeYtv-rBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=lqI67-WsKzH5_P5Qmf0oPUiquR28edWQmatGpA3m313EuE-7-e8Cb9VOo-ryyzeonasRXy0Mf2PNvowHtw6HNXt_V6MbiXcZ552yaG5dgimsR1ej2g7uxOTj80x_xUeUawvE1WACR31ZR4xdzX6WCnKo4c_A8xSk7HzktN4HyltMRqk76CxuHrG-nsc7XRgAFrJDzCo3uNtAOPu2xs99LtTreGv-OhodH63ZUUdHrFbo-PHLEQ_jPyBy-25eaznQmg0fvp5n-xG3cojMdE2KowSy2Xyqkw_GLRrdxOMpeOCgsexJutDCWrxdlgwIDn_xbUvf3USt3T7gzyeYtv-rBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFBjjBbv3Yc_gftKBuGXIbO3ZNUW_4No-Rn8EFN5ULIe__tKwW4scemvbFX2X3XMkBmmvSPxSShQyCQ7P3CztCAmrUPw4jkOZpB_j2YVy0FvEID0p7mBR62vP3lHz2hpxZQ68VmsieJ5r6Lt5mPEqg_1ZY5kv8ESwYEoG634GRLMkVakZ7XL1sPz98a6lRtQ9IrXH3xowSiCApwgAWsD6e-Tibabjsypdt71nRsBEPRe958k9JUZdz9WP4vWAOgsVdJHO_nJ1Dyw4xuCghHVtd_r4TTWw170l7Q__DN_dzvwJ4cWIWKUJbYyM2JXrOmZ9th3f-yVXrEPStP9oRqftg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BskDjZ_Kp66kRR9Ee1_3LcOsFYH0-ibe10EYBggu0D5UIMY_4uqH20MqvEeR0koOiprDvuH8wJWFYNh8qAH6Oyxhj-WNDPAbXGbKH0DJ2Q-PweBbwruBMEcrykE_WFXWjGfh38iR0a_mhJ5pC2j4qN4N5iH2yAh_gjSAAtdU4IHv5GB0yUsPGfiikMPnCtZwW3j6tc7zrwzEYJjHPpwdmudeYqrvpfZ1t7iDUXp5znptBZWW0839w_N_16us0VdyvURdoxY4xYHTO-zXQP8rsUUv6NDodd2h4kQn0ZAyeKDm6ZGk_sFOhI1QiKK5-KltPIXkyqq8ZRtrHVPiD_7A6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tz6Y7BcwH8gT21JXUncqyXnCZMmFVim1-O1gSbRVU5GV0iZxoFrDPK4Kn1EfpzOw0L0_d_qGKbRW_cTCW2xrGlykK59sHn61HJZPA0g3p9gyJNNuRZjWgbCuTStTRIbhlvNCcqBg9EWQ8hbagLDM7UJ7bjV7zUN63cRUzj2tUtn1wMv-TOTfT8n4NdAQXkSoyC8Nhuvs-l2ZTUp_1IHA3attpfVvLcaOt53UaOzQu58EUfCfG3sSiqRjEOOWldg32Y1L2GiB7UoLqaEXB0dAXpu93Yhx_amqCYog7-dXd-2jLYhnAoyezXY2Ts5Q79Q0-EOyeDPkPcRsUxddWHhdKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FlT7cuChYvt_1V-toW0wsr74CqwyoA7YUwb8BsD-Q0VAGUD83i5_s1lLo-I-gbonrLK41tnwOcGRJ6rKMptHCz655shBZH3Jl-CzSvkgQinQgFdBuXCdYCk_roQUCSF4zMwbGM5OBfjkLxxfgEofCYqM3toVnspU2i4zc6jUJu6SKDgAzZUE7qfPw5ihI1rZYnCTTWDa25Oi2H8UYH19lMwP12rg-NVtw7KkB1embPNJ4oEVsGhGoV8lTu7mOwmgj9CDcXvCs_WoOj_-JO8NEaJtQ_boYMtoqQBBaMF9q96TrtlOzVhIHsKX-WGhXESwkm8rFRSzKjGV2aAdvPexsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=qPGbF93tHpVuF0sJmibzWoGMzhnV8LSQgfUVoRKAy5A6q3vpIjIdn3WnGcswWx3CHAKWlDGCGXhHqmGaRXQsgwaCpTDggxfwhDGnSWVouXFuq1dJUF4Y7jZese9ssJt0pmcqZr_LxR-e8KIHvtmmouulqEBN4piyw0g9yTVaFgUQy8EyBnBP79FtD5t2iDq9jtlhbgvwLkIAm7FUf2iDuTLbyQmuuIyUw-CBDNznAhVkiGX7nw0RbhNlmIjpD8K0HSH96ojTGvfGvTToW-2PRJ4PC6O3HkGbizU92cTa2_65AC5YBymWgDkfaPA0PY2xhb7eoaTycongZpC0QdHayg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=qPGbF93tHpVuF0sJmibzWoGMzhnV8LSQgfUVoRKAy5A6q3vpIjIdn3WnGcswWx3CHAKWlDGCGXhHqmGaRXQsgwaCpTDggxfwhDGnSWVouXFuq1dJUF4Y7jZese9ssJt0pmcqZr_LxR-e8KIHvtmmouulqEBN4piyw0g9yTVaFgUQy8EyBnBP79FtD5t2iDq9jtlhbgvwLkIAm7FUf2iDuTLbyQmuuIyUw-CBDNznAhVkiGX7nw0RbhNlmIjpD8K0HSH96ojTGvfGvTToW-2PRJ4PC6O3HkGbizU92cTa2_65AC5YBymWgDkfaPA0PY2xhb7eoaTycongZpC0QdHayg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMsubAwL8jVRU54Oi_6DxQ1x7u-Z7mTDjlGZQD6Vrh0yi79JIQsftgVCiLCPAhdKG_dvAkoLRJDWrgDT5dGu6tt-UjZpJWPo9JGMGSz8ZKeg0hgQ-QLeBX4yyK2wgWAXXlWKLjiMhUyxi2ffF8wchL-3JJdKCC_4S2AayXb5YqXJDu6IWDbh5JlL5sUWF4NJGzXnKrVvhFxNyazHuzV8rHOSW6N68ypZg2yzS5oVY7mfeqqqdmRQH6s_VlRDFBYf_avbu_-Azewu4dIOQEQiktVE_Bh6MvAuMsUK_uHVgpxhKfDEjB7pEB_VPo9g7XS0Iu15RFuuBzTVAS76Z3SJMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=Zx_BrBpgrQYTfYw6a0aY_dKpNImrrFV6ASd1l-ZGehG-MLin6dn8KuNeSp6aWtZD6GuO-lhl5w70m_3C12iS_488Tqd22_qYlhQpKcIgY0q0FmjY30UyCNcF_af2scwlbfKJ_tstE4bXpNuLC9kWGgn37bWjtrNFexxec2dbQp4A7EBqIgmWmDG6V6287mkvwWq0gCYOv9o50LkrwfOpjKZwBpk3y_1QJ58SfqcHr-36KTN6wELClOTS-TEt79z05TemXQ7TwJevF50OxLLK9HDginpz6ZEuz-1NCFJgn0KiIdHphV-yXxeCmGjKt71OzXF9o4USWa1OKF4KFyu04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=Zx_BrBpgrQYTfYw6a0aY_dKpNImrrFV6ASd1l-ZGehG-MLin6dn8KuNeSp6aWtZD6GuO-lhl5w70m_3C12iS_488Tqd22_qYlhQpKcIgY0q0FmjY30UyCNcF_af2scwlbfKJ_tstE4bXpNuLC9kWGgn37bWjtrNFexxec2dbQp4A7EBqIgmWmDG6V6287mkvwWq0gCYOv9o50LkrwfOpjKZwBpk3y_1QJ58SfqcHr-36KTN6wELClOTS-TEt79z05TemXQ7TwJevF50OxLLK9HDginpz6ZEuz-1NCFJgn0KiIdHphV-yXxeCmGjKt71OzXF9o4USWa1OKF4KFyu04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1-dkDT4MZirgZWNXOQmONxAegneRs3NE-GKmVQ3xfyJk8w4pb80B-8CXilGJw4MyH8A8GPxL2WQqGd56xl2QbF-sLFO9qrUFAgmIg3SXTkh0sna3vFjaG2TbOc93DvUTYzh6NzxHdlx4duNu0MzaYGxmGWqrfQJcdvkyrw0f-7hyoaTkCFqLKuARLIf52NvXPsXgKJQnPw6fnP7dGHUv6dNcuRvjanlyI93Sc6--KjJVYDUlv9jKqzrcI1uVM8FFwRwTA6nIa9SpeL_w6ar7CyNfHd_XhPShgu1gaD97X7e1kJyLT7-TL-kA4FAgO5WE-VykLGhH96QNwXXSwvYrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPDry7oI9hYfdgdjYRLUb2Eg0cbgG3YhXL60cMF1vOKhozsTH13wWuNNydk43n_J7dJmhGgi2iCXPFlfrYOGmjeuE0NHsG8VyXEm20Oc0ZoWoX7P8Wd9GSvmHt7RXTXR_-Fl2OqKVK6GjOc5n_-lIYIcaZXKgiA3AE3pRbVmu99eg-mXT04enxUMarxneuCzWr5uq5z45OkbI9GPi1vJgBAvaWGUdTO2fH4K1GYv_8EBhne-9h-nGkSBUpkQFSTBrxp1MpiOfzjQTiJ7Fcry-hJcPz1LtXqA6Mgn2Up9kGyOhsyFGV1FKk6IhxPE431FXmoVXV_s5ZOy7Qr2JP4_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmiAizrbDDQ3V2Cpwqy4tQ3S9h7lzhgC7YTzBjJ6WjCE9YBkfohxzatWnfUcJiOgV66z4zhadUe0i-1u-P9gEo6Hh074wrqxmNZUtw3O7vRCHH8QI83W5KV0acNW84PsMNGK5HD9hVeiuKCQNmY_pLuCd_fMz4OT4PX73nFFhK-ib16QcTa8ryJMZPBGi-PmCoxaHB4y_ROdXQ6YCFBpOaQ-z1WMEOPY3g3N1Nj3QLGXXpBWu-lTVjREWW3IIwYveTM93yV4tNlAZoxmRPNJ84hbQs2uZSbu4eGS8nF1HybLeV6yV5OTc3Rfc8hetfYy-LZL4hAwlnqsEwmCmHVeMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=AjXpE6dHnQl-QpwIMvGzAzfFlFxr5VpeIXTcWQ-NEkyTQID4u0WrHACXq7ZB6zDL2E9ab0N0Ed2wAEs-CztHPtbGtPOcETCL69rMEi4js_7RvFC90Ed6fjepmGGYp-dmwYmLfepOcJVYRtvINBLMKdBJzvSVsQpIAzFueq7NcR78xTUz4gXglFwHP-SIbK1mKtwSdo9Fgx8TNMjC_-RKDOOE3rU-RmqtmuG9mrXXHpymg2XKfrTaVqG_z9nafNiJX0dRE9sQlapYd2NCNpl7_HKl-76opwaEMJrCGab6puyQ9PbeHrOikyKT2jxQRqnwNAUoNnA48gMnNQvjIZOt0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=AjXpE6dHnQl-QpwIMvGzAzfFlFxr5VpeIXTcWQ-NEkyTQID4u0WrHACXq7ZB6zDL2E9ab0N0Ed2wAEs-CztHPtbGtPOcETCL69rMEi4js_7RvFC90Ed6fjepmGGYp-dmwYmLfepOcJVYRtvINBLMKdBJzvSVsQpIAzFueq7NcR78xTUz4gXglFwHP-SIbK1mKtwSdo9Fgx8TNMjC_-RKDOOE3rU-RmqtmuG9mrXXHpymg2XKfrTaVqG_z9nafNiJX0dRE9sQlapYd2NCNpl7_HKl-76opwaEMJrCGab6puyQ9PbeHrOikyKT2jxQRqnwNAUoNnA48gMnNQvjIZOt0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dh7bjJoCza0ou_P-dXp9nvFnMMBDJJPDq6g2zG5jIzMkpF6YLSOcq_TcT8VN5WLCQlpe31OEr5G7XC_hcyQWM0468jI-eo4M-0iZyH72xInhIEyK7tEbhKL133aH3IvjI6lomSzlN5Gm-jIRaIMCtYs9neFaLBPJ9SsY6rCP85pzNyX76ZQXk-qWv9Qd0Dm_CupFg7fq8P2FKFMKfEMbUMFQ6vnuUAlAFysSzZnkavLo_rE3oMWI9vknjfp0-zgfeLs7WS5UEjhkBybtYQ1LnCC42ipHf3D-rSYETMUef3NxWy52O01FWTprYxyV33OJtzDx1YYSamT3ClI-JKkEMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMdSy2NknUKxk7B21b32K-9MJ3dP7Wsd8l8IfM3COUdiFmdPtXN-jMa3Xh-h0J6ygGYVMfXqsqwUyxqUmLKz8rF8sJMNlrCFXrlm7JKXPssJdDK3fZJk9kbFDnk2TLbmo834typ8c74rIuPVWHV1QnXyzq17yvK0CyWL2ppSr9OjZbmHZ3EOmcePApW-4p44I15yMaVx1448t5cq-v_jxAHHI2F_7Rvt1HfbGT3EESXDsT8d0uyWTCNSxBqH5k08gWJmbQyMti0Ti9BBu8w1qZR51R3TUiPxOZn4SjTHfIg20fXJqshaKVaVmMA2g0EjDeX6s7ElfaPIB_9VBkmc-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i_DyNG67KY-11AiqzbbQZnYsJiPx7ss-Q2Um2CYSJJAr1c-DRf6He98o2-OlxVnDyEk2Xq2WLedHhqcJXaGsq8VeQXOCv-KfZwFAOcyQaxOy3gIDGQhIiaWfZwOIm87OuCKDhjRBjYZES3EIKt1RVZYsh0BIX9ERbIVwMwe9cdFeWKD7tJYafyAEbl7Pu11ozdg6dS2VwfRdvYcHINVtfO7G5aYXzzsX2bJtEtyDfbMt_iogqRXdlY58lAZ7RN_6ljF3GIAIeOXQCh87pXxB35ayPI4cRpfEGjh5-HHEj-G-OZSaEv4llrxpLFenwAZ3QKl2XemyeF3yOlo6VgoLrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/am6CfccBkPEG0E5wbx1GMZK7bTh6-3NP1SJKWj5xLeflScLL8BvIhJofRkgKnPvBzrDLs-A5RfszbVsZGgjSEarsWuUZwfKWmfRJ8DRBGH3ZeFCbuyoQxCnjPeyC906IZwYAo_yNoDUe93mBX-EEEFJfit0XljHLya_apsXSreabus5-3yHhUtCzAjniLvV33zCtYkpvLps2fZCWcgtr53LLrEQtj4zlDPLJGUnhHo78BqbmqvQLuTIHB55OtB0iwP3DjTM0Mp1yjB4uE_xyXg8ZoXVXrOJHNUHsnREHzb6M3uFwGgGvcH1clcwN-me4isMl9ZMbEKaQ7aKJXO9LVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=E-XCTsSoBzQ3Ln5PmWrCUvRl4fCcHUe3d0DJ2hnhwah90jJWBfgChI-lNyt_GddiRlKV6XO9H482qzebmBIyO614N-pvr9p9GVAlSFwConDoHhXMKed5o1ycMVr_nrzEjrPKJEiSnxEemP5EaTegPWalyKzSiXp0qZScIOOAX6hMdlUxwgtwGsr6S8m5sRJyqIvGSlne8w5oUy8GtXQqp36gvuXBDB61GBWI59Ls59puytVQqpUwdr5bpzY8zQphXCefcaNtFLSjmfzsGH8cQOx7qi8WkwFw06hVhmexspptDCIkB9Qqr8Qu3Alt_vepPUH6hjVZb3pfZ-y48IjaRpRh4ohh4QTZMaPXz4lltpS9_F-UAO9yH_bq_ipT2SoGTJhoougE2Tw1bY3SQoxbmHnZWGSbfZd8VWm9Jyc1LMnqWY84duvPcHN1wlqJbEf7I3s3GGrnUz8XQeT7AQ3AwHuAZWZ4bmWfpdgZv5yjLpgrP7N2XQ9HiBQ7_6JBw-V7JBgU4YLrWA0jS-GxrpNwRByOcIjH7seg7s-iWD2lR83j2cpYeTeTKeKDC0vfaEGwmWi5494nijxJiZSB5NYjO5r-nizcjlTX9HOXMxbp6L7-dbFUKwGdOIGi5TQGxlSKaGIk26TiaX0qR6GeEiaDHWhRj-0n6gBjeT_dDRO1OAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=E-XCTsSoBzQ3Ln5PmWrCUvRl4fCcHUe3d0DJ2hnhwah90jJWBfgChI-lNyt_GddiRlKV6XO9H482qzebmBIyO614N-pvr9p9GVAlSFwConDoHhXMKed5o1ycMVr_nrzEjrPKJEiSnxEemP5EaTegPWalyKzSiXp0qZScIOOAX6hMdlUxwgtwGsr6S8m5sRJyqIvGSlne8w5oUy8GtXQqp36gvuXBDB61GBWI59Ls59puytVQqpUwdr5bpzY8zQphXCefcaNtFLSjmfzsGH8cQOx7qi8WkwFw06hVhmexspptDCIkB9Qqr8Qu3Alt_vepPUH6hjVZb3pfZ-y48IjaRpRh4ohh4QTZMaPXz4lltpS9_F-UAO9yH_bq_ipT2SoGTJhoougE2Tw1bY3SQoxbmHnZWGSbfZd8VWm9Jyc1LMnqWY84duvPcHN1wlqJbEf7I3s3GGrnUz8XQeT7AQ3AwHuAZWZ4bmWfpdgZv5yjLpgrP7N2XQ9HiBQ7_6JBw-V7JBgU4YLrWA0jS-GxrpNwRByOcIjH7seg7s-iWD2lR83j2cpYeTeTKeKDC0vfaEGwmWi5494nijxJiZSB5NYjO5r-nizcjlTX9HOXMxbp6L7-dbFUKwGdOIGi5TQGxlSKaGIk26TiaX0qR6GeEiaDHWhRj-0n6gBjeT_dDRO1OAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjjo2U-T5OZuafyB_T1lj7PPgqvX-6K47Nk3l0rRDWDVVOoOhZ9hMgyyJzceHfKUvJp-fiYZoG5sOzJGivUSOp0sPmLvmgFxnq2_JgIINbANLXgif66CX6AH8BGSw_SIVrOxNu2wqEXgw_62JcaPGGpj3Nwxd9azC0VKEOodr_3K_qnGzhaWuxSucvVpFjC_Z25Kv2YVeFv9gojOmpjeAe7w2KKhZOPKdnLTNlDYNy3Vb2rqqdIrl1bZCwtOD3Uu_qKyXQ-lWR7HvSoVoutm4zJVwFG8zbj2H-SszwtW8CBlb19zlj7wLlrR296RaxyzIq30gEULCF3YQxY-dfgqcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l6uyrPW0icZAKv26IFm0HjYxuRS-NC0YRJ1vz5dUxGXagD-lZckgYiqZtYwiEJ81IZpaJD6egcvPKyqDvz24wyqF1ud-yC2Bc7QVvNaSv9FsXEgsozsnCbrKSKUecPTefnFhdejmJG03NZgymio5NS6IJI2HDimT3akgiEpsKbX-YMP0Ug052ZEO6U1n6IAZXHs4fFVfevRsC6IQMxCkCoBu4nyVQMiVIvXLuFFOK1oaVtPDe45Ur-VbkFGUrDXcrVNhX2U2k-Zj68YRkdLWjp-Z9UbMhoswwONxFqNg0pJoNyQO_XgIc_nTpp311kc5AdDlH_RpsP33qpI44HqvFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMPtGDJ2-p424wdsqzPkXfOCpLO1EZoj_KH5DsJBYHXfmr9nxAm9ezCXAJ4KpF4NvH6a9RaKwimqcfBC8-ebO-G5mJd2y9LI0zN6ddrnon8QKDsuwZ3Ikz_i5Brapfmf2KGIelsepmlpwuIyhGCIW1TGdv9kDa8ws4SVoyUqs4EFD9lYYDv7UVIzNmnFzQHQTBS47mIzhwodhRgoRgUHQOZTMaw7rIiRocFux6V9Vy_T2QNHIdXy9h7JHff-PfcEis6ldw-hDjhkguRC2m0dSy_6tcZUZ_87xPxzBHNsk2keki0VgsDKDgz5ut4C3rWUhMDD_uv-2ysReqlKtrsX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tzz5Tz3QpoPGskRucQDlClolcdJkTRWR2gs6BikZRa42Echb1jwwe1SqZC5kNomNPCd_kkJw8cXvi77JHhFsTcBkFX9JhDv20cA9SxwTXbL6D5t6ufyIMKsaq9NvefuRxXDifS_PZz7A9l3HKSSbnVi1Eq_XHv5uNbN6vDpXPKvinEsbnkHFV-dOVo_KTie8CJiEPCy1HPJ7dgSL20gv6UcESzHAbWMhYYscS7QJPL0Iw3xtSGd1cdDVDnnrwMh8G5mdA4PIpCwSS145r4aJdpg_h8YR1tiUnv9WYvyXdGNrLX3S8nU3Bn1auyikUcTdhGGig9IqODbNZ3ACjOitUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/su6asu9XfUS90V7EUrSH6PPk7mD8JysLSW-DlleoCHVst6PIY57VjQGFOV4qavq17sNGg3pvs19NLxztUWYHUnsx-Il3ylV_6W_e0CHzMTshy47AOSE8-Y9NtayHqS9qBQn2x-kojEza8aTHWE8pLASVWFd2yF4GpTocmfwUTEfA1R8F0yqDHDCFiLlmJOlP5ZKwmKFqwwGfLMGoVFo28PtVg3jk3MswrqVUPxEwWNkX0sLPI-vhk_HkWGJBqZ46O3C7jXRhphFmqbkTEhquhcLPCQj0HzZLfjXATs7ljQAe5WfcCUeX0LDqSsPq2ERPoUSynL4EkY8TqV72NG82MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K4jefzURIj7GGpFuN4Zp7GeW0cmPEBA9nfhpobMuimpCnvimLbUdKcsp9PIsaww-iJlFWNKuc0KKV2Ppibq4gHuIZ6SrsYBH9WW690vZfZCTlRwFvgFVv_KBMbnppDQfv9bEnYzrkCpJimMOHRVH6tomQHZ603UuURA5oJBT3KJNcSBO0fXPlNFOSDlbuqOMvM5z0BNdtiN0mossZtdc2hLHrNW2uIB_XQIiAaYVfK_SoK1OEs0jA1WsO2zWV4Juh9cRW4qSycj-cRastbF0-QBmNQ0UOYXcGiy8vZVjodqzzLIOFNCAAwHRAR_hxSdQt9WSJgocbtFrr_2xPmJwQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFEOe72NUKjGDOMATo4YQFPwDkZFzYYnSMqY7INHpeXRt6mvUWCCtNFdZUnM1aSLzacBWUrbi0FYlL-j_0NzdWpBrvVW9gv4o_LNK2GK5SMuVhE5mNuTx8SExVK8lziuzcqY29rhEnrNG_9xvXQQGwvWSNPncybc-txukGO4mJ9XFewj3ub-pWNEvbIx7mcEJUZOFn5TpeO61NusClV0IU52yItj31HslFPW5Nr3Cya8tIOih51g2lFm6XJEUYS0mk7-U9BPYiYnRtcPv5vFu-6TpaJA3w7YOhbYKYlKeZlssa9miK2dUg2VgfEZSiyAIhaBuKyFGOluvn09JRapFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
