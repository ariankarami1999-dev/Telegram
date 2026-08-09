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
<img src="https://cdn5.telesco.pe/file/f-ZuP7v9L5eFSA1PNWBNWqWJ87aHBVEYlWO3b7UceFXyNu6wJkHD-VX9kRVK3bsg43xufk3ueMXdex-4oiAlWzspCFqX9AUXS7kNXI5VgY5PKp2EJo9sJo7YLfpAhdS3xpZ7gyUdql7ZKWowrQLLKhO-FvVAlE9JrUkMn6Kzj7rs_y3W5i9kk-PtER-EBj1xjo0xBfrac0ZxWlDxaoCQmnOzkh79pUAMZ6S6jqFw3zRTUn03DYWU3Q_y9ZNO30yknkBb53t7JYKgTJpDCqugZn1yG4iN_6rlhQpFckxGPzH6CpJLzaPBrbFJMbUbvOvwmUoZj8JVtAbSAdVvd_1w2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 483K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-18 10:09:32</div>
<hr>

<div class="tg-post" id="msg-103141">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP28gQaDdZiev5HO50MyBfHI9GghEJu3Cwf4-XBzS65c5sKSBu8-V4wvxAi3E5uixg1hPj3TUQvm4vzT8Ldtj-tmhgnfM_A4RCo7Of24Yze56jHBwFD3IZDivuJvOLeeag93D-BymXVN5tVZ1cwS3eJvMNZKBTudYuxof72mBlXcdO1L0QQ9mdNjmspsDOxfKvQdYgqSBIJtwie-0HOzhiLfim1YoBf35GQAksR4VmjmF4lRYnL-xb-_V3MKsA2_n2OV8IW_3S11FAenW6tTOt9mywG9OGEP6zUzG5mmqk5Z0t6QCqguSLhj5TOcRu_QgLBU6-8ls4VoNQxeP3CnLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فابریزیو رومانو: رونالد آرائوخو امروز راهی مرسی‌ساید میشه تا تست‌های پزشکی خودشو با لیورپول انجام بده.
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 147 · <a href="https://t.me/Futball180TV/103141" target="_blank">📅 10:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103140">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ox7Rps37cCzTTzmB2HGxj4z0jDRr38sg6gT9MiTYkoorA-TeyUrDzcuP0Gs4jeAbh60s-lhkgPXKWRFkQibO5EJEzcsRfeJzts8EDyoeLW1HEzS0vIlS7VsHV8zoulMXbee2pntmpfPmfAJIWXmzd09wrEbGwoDflF2eW9DH3ULLhY4THy_nnwdK0Odfe70Ddg3ztNsaOeSGD5sHkVEmqm449H7XjkGEyDhiBB2r7iOZ7oMpN5kCLc97ZBo3Tx0rldSJSTMtgDA7B2FXDbAYzo-LUow_Cy9oBOVBGSrr7NN9SPCjNEQ-MPGDc-z4lML6nThvnAabec4T95kcRmPhRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
آموریم با میلان هنوز تو بازی‌های پیش‌فصل هیچ بردی نداشته! حریف بعدی میلان منچستره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.92K · <a href="https://t.me/Futball180TV/103140" target="_blank">📅 09:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103139">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رقص معروف لامین‌یامال سوژه عروسی‌ها شده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/Futball180TV/103139" target="_blank">📅 09:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVGkKNoHEtUcY7434a3uQsnWmv2FR4XjFxO7cp1e143CJchwQk-FUINNo153fszsQjEAKDdQsStAZiXdRFbZw__nPRaCl4ouCrP_Z2AxLpv-16rZiaDEiz5e5ATiWv-xckM4uOjeN64xchU-tdEe4d5CePtOeXDkgOTMXnXpv5cN5fHdw3TfK2Z5vjTJnM1trb1s269kjv8pANHiOU430hPJUiZwaY5J_-m4A-9eimz7bAkgbV16jO8hfdK-dsB_wBiWSUv_tE5A2xiBA3Qj3Z9AAZz0gJtjxa4eAwWe547chM3RPurG0GJSMTQylmEwBTWMV1lFaHdGja_jCGsCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🔴
#فوووووری
؛ جواد نکونام به عنوان سرمربی جدید تراکتور انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/Futball180TV/103138" target="_blank">📅 09:29 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103137">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5Oen7LUFCimZFCchF2ZGr4845jbDI04ZIyDxsftFMUDe8s0FbzEfWFUU6m1IYe0yCGMHm3lBZ2MXYX-U1OAST2z_10QLMnHt6ns333BI0VRR0Tudq968On0IX5AQPJ6BPU4vQaY9XsYxyFpScsOEGVJV-hObJsiDKnJIfjGdjozMBf3G2Al48rTPtUF-XPl0nvnXG6BWfuqSstVpDDy7BhH7J6aV5cH9kut7qtGrq_lVbO7WI-UB0lMEqVFsMolM2WlQplOoiQ2obRlsYuHd2QYhto_Net5CNsGxMW5TxqvSVlp6O6prfsaDsmeilXoTr9lrJykc76dfA-Jk5HBFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💥
هرگز فراموش نکنید که لوئیس سوارز چگونه فصل ۲۰۱۵/۱۶ را با شگفت‌انگیزترین شکل به پایان رساند
🤯
🔥
⚽
⚽
⚽
⚽
🅰️
🅰️
🅰️
vs Deportivo de La Coruña
⚽
⚽
⚽
⚽
vs Sporting Gijon
⚽️
⚽
vs Real Betis
⚽
⚽
🅰️
vs Espanyol
⚽
⚽
⚽
vs Granada
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/Futball180TV/103137" target="_blank">📅 09:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103136">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/730562ee98.mp4?token=jgYzSq5qegvyJiMTHUKBeSKF9lll-8lZixd5G7TgukDyQjaViHYwHbEV7Qruvss6PJj_UkNTiZD8w0WljMswhuVtBDJAq-_bT0EIL5u5-Cg9zeyLEgqKSL2dCknuSsBLggPEmo7Ybz1VXF6HmwlNKwvkeTl0SE_x_vQsH1nxtwMJ4NASXjgnq5ZPIvLebJt1h64_0Mp6POEaI1j6WfaUUjAbQRyX9ffNXn0aJ_JPnC5pWRPNpfTaRpr5am-11u_ATuvXblt-5koKm26huHPZMRsrIRFEaFWcQml07CRkxC-4RTwC12a-XUUlqZgQ9WwH1TyVascrIpFaZ9WlIW_oRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/730562ee98.mp4?token=jgYzSq5qegvyJiMTHUKBeSKF9lll-8lZixd5G7TgukDyQjaViHYwHbEV7Qruvss6PJj_UkNTiZD8w0WljMswhuVtBDJAq-_bT0EIL5u5-Cg9zeyLEgqKSL2dCknuSsBLggPEmo7Ybz1VXF6HmwlNKwvkeTl0SE_x_vQsH1nxtwMJ4NASXjgnq5ZPIvLebJt1h64_0Mp6POEaI1j6WfaUUjAbQRyX9ffNXn0aJ_JPnC5pWRPNpfTaRpr5am-11u_ATuvXblt-5koKm26huHPZMRsrIRFEaFWcQml07CRkxC-4RTwC12a-XUUlqZgQ9WwH1TyVascrIpFaZ9WlIW_oRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نوشاد عالمیان یه سبک زندگیه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/Futball180TV/103136" target="_blank">📅 09:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103135">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZAc_7gm6-hMBPYaMaUPkXAE1buAeiOqBpCWiOjiqwiunCRcOgaWvIllZ5Dq95qosA0vOv2Q_UnwZNSzmL5jos-jd7vf-eDiLp6R7EnxzZgNwpqp7nfi9xsAfmx7gL9udPGX4zpU_Q4W_Ht_STOPhWJY9iSSprws66v8Umv6auKrCYh1UzfuQu1UB3uTtHj-R9jBqZFaeoMSE7IObkLCE3GlGhSnk-hDK6tj-YV3NXcjV2lEQHQFMMrqPuBKyWjg1Lo9YAbrKBdgtvJEZLBUVD-yuqYpdZos_qctcE5OqwDpLLmdS_CEvCEPNBTXY_mLBT9UUbL_qXC0QCcBXd3BoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چهره مسی هنگام ورود به روزاریو
😞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/103135" target="_blank">📅 07:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103134">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ENQ0NbyMzHitjQ1a4WbU783EDtP9-m_vNQeWFB2Ld-Z_JL-ZfD1KSYTMLj3ope3tAnhBkX8ArEl9_S0RW_6PcWgfVmcT97atqyObzn2gogncFfvuPXkfjWbAbF--L438TXq7DFLC25sYt_FOTou8JSykye0NRaCfMbHAqJdKJMo0azCM2ngs0gyaKLKjT6tTHs8eDa9E2CMDz-ftIAV818o4FagyHiqyJAWqhMZTSRhpdsfLb9MejNg6JzICPt0U5Ea2zL3gEghUqbYGqrDMriuIbdjU7N7hH679R0s7ngMnf7Zlx9Eg5zX0z2R_OhX9gx9RCJBJzJ14O7o-dJc_Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee87aed7d0.mp4?token=ENQ0NbyMzHitjQ1a4WbU783EDtP9-m_vNQeWFB2Ld-Z_JL-ZfD1KSYTMLj3ope3tAnhBkX8ArEl9_S0RW_6PcWgfVmcT97atqyObzn2gogncFfvuPXkfjWbAbF--L438TXq7DFLC25sYt_FOTou8JSykye0NRaCfMbHAqJdKJMo0azCM2ngs0gyaKLKjT6tTHs8eDa9E2CMDz-ftIAV818o4FagyHiqyJAWqhMZTSRhpdsfLb9MejNg6JzICPt0U5Ea2zL3gEghUqbYGqrDMriuIbdjU7N7hH679R0s7ngMnf7Zlx9Eg5zX0z2R_OhX9gx9RCJBJzJ14O7o-dJc_Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رودریگو دی پائول، گل خودشو با پوشیدن پیراهن مسی جشن گرفت. لئو مسی به دلیل فوت پدرش، خورخه مسی، در این مسابقه حضور نداشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/103134" target="_blank">📅 07:06 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103133">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0UUOS1E1MYciPBifaJ32Idk0haLWi0_joOl5uvQ2SHGltr3G0JOxkEfO2O2EAqHb4HJm7h1o0Y3RcGLlnubqNcGIMhcPu3IgBVtin9lOS8Cpc8wFWNlMRBDg9_1_QM3KUqlOdXuR-q7EabYgbHqb7zvkASvITHyx2O1Oq5gmEDq0xqVRLQ1vgmwPqD7TwB2kbq1NePdKsdYaAWLfEaelVioE1UkUwMsQw8px9Z0MwuRjQsl0qmq2NXsJXHbT_a_6r8tUiZineXE_6MHpIOX6HhPL2Us4l5ztESSiei2AsXW_lN23_TEVhPoXJpbVzZU2z0IZOAcX5eKDfxTlSfyFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اینستاگرامی لامین‌یامال
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103133" target="_blank">📅 01:17 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103132">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=pdmqY2M6Yv5gvxMHdN0lm8DkGULgDrH1SZfhBHfoF8bqOhx7KGZghIbHq0QHho21QZXLz5DWAmn_YHJBtwlVlaby-uReHTDm9QPQ-auAHidXHPujbFyLUsWiFFsVOcSOvx5vBkO5rrjV-YHLf8eHR0TKGTfZ1tjTibgUNDPXJ1_9mNn0AkW7P4XEW9XU0vpecuJ_UqJCr43vlIQ16nu_w8p-cYzZ16bOH4ZezSnEwOnhUYJ6BJi2m1Thc2ilMAFFG3i7vmAliXzQZIGx8--dvMDel1woOjQD2plusPkMOEfxT_rIZaLzUTLoW7jxesPlB309nKTIZvvm7URDbCjqNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d3ae9a81.mp4?token=pdmqY2M6Yv5gvxMHdN0lm8DkGULgDrH1SZfhBHfoF8bqOhx7KGZghIbHq0QHho21QZXLz5DWAmn_YHJBtwlVlaby-uReHTDm9QPQ-auAHidXHPujbFyLUsWiFFsVOcSOvx5vBkO5rrjV-YHLf8eHR0TKGTfZ1tjTibgUNDPXJ1_9mNn0AkW7P4XEW9XU0vpecuJ_UqJCr43vlIQ16nu_w8p-cYzZ16bOH4ZezSnEwOnhUYJ6BJi2m1Thc2ilMAFFG3i7vmAliXzQZIGx8--dvMDel1woOjQD2plusPkMOEfxT_rIZaLzUTLoW7jxesPlB309nKTIZvvm7URDbCjqNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
یه اصفهانی که قرار بوده برقشون ۵ عصر قطع بشه و نشده،‌ زنگ میزنه اداره برق یادآوری کنه که در ادامه این اتفاق فوق پاره‌کننده میفته
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/103132" target="_blank">📅 01:01 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103131">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKfxT6vV-GmHWLjZferjKrjyFYbFcBYMHW-PFeNDovxyrvbJ4bNfQJv-vCCw71cVuV3mg76LQqf0kCBMj4jjoJxh1p3PCCyAcrtuBbzuWPS1u3E-x9f0AjB8ubaje-fg_5v0aZnmI6VyM4VVMpWTKreJEFGoLichUgZIk_OfMLCE8BeHnOna8ASgF5mamj9ANOVZWZVED5K4G5KUWAUl-QBrLaZe3-GGqs_xs5GmVHRtnE--0Xpy6Fi4o2A2D05pi1HKnY6zGEE2jgwcQGQ5U5T1ASseqOOk__GhSBuzVk3oUj3vsepTzF4p25S4oCvcSfMVRbXKRmE12HCuGrrCJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیو فیس و این حرفا.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103131" target="_blank">📅 00:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103130">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWZnRL3gox-ROlMyeLHPwXtTKPopugNRAejdQ3Dy9Lr12lLoXbHFCyNBZvWdtSmsqxO2H_FbJBL0hisSpmUD5bkYO5Dl6RBXGdruLisDfJHMwDSy3DMvz44ZaA0w2SXYrDinSnBUXkYfSeyLHe2JLHnsvA5voWK46CPlQTeW8KvEgOhAmcFNnVPJHwoo1cMNWHFAx6Y_2gfgAwv7TJqRj5pYrkTnhhF6oL0G2nCpNRfnO8XxRbOPovpIYv0cVk2GfEcRNZSodzI2BT24RWcvVzTFUbTCe1n3-x5T07lde8-IIrao6NbgnCrcPhY4Yn0C0OxtAd8QlmJ1Q8yVj4FJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🥶
🥶
👀
فلیک‌حسابی کلش کیریه که اولین جام فصلشو از دست داده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/103130" target="_blank">📅 00:40 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103129">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=HO9hgcCm84JMSPiVPBDQ3fbb_bHPRCo_H7gaZtagnq3yZdrMDhwMHJdRHLkuvG64rbAzM8tZMrZwFlpnxeOz_uqEFPZsP9vzCGKNSJN4Ae1mqEKvE5SeTOO7Q_B6wlm6I5--9H5u3zVytyDShD4cA8I0inQNSkuFAtEj4m_AbwaQHNT2Z1Kn7arEoDDWMZ08Ej2YhfVjfiT1xKV759_Ypdwgzy-lXT60DOtSaKJmVvcWwcdDA1ieOfvneUwEl_2TUvInGl-cLtRzkhg7S0DcGTGZzQ-zgzObZPOE0_EVNGgw10b4oF0O5j8PpljSevxOLf6YUGi1sTidpNnX6UXW2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da2c1528c.mp4?token=HO9hgcCm84JMSPiVPBDQ3fbb_bHPRCo_H7gaZtagnq3yZdrMDhwMHJdRHLkuvG64rbAzM8tZMrZwFlpnxeOz_uqEFPZsP9vzCGKNSJN4Ae1mqEKvE5SeTOO7Q_B6wlm6I5--9H5u3zVytyDShD4cA8I0inQNSkuFAtEj4m_AbwaQHNT2Z1Kn7arEoDDWMZ08Ej2YhfVjfiT1xKV759_Ypdwgzy-lXT60DOtSaKJmVvcWwcdDA1ieOfvneUwEl_2TUvInGl-cLtRzkhg7S0DcGTGZzQ-zgzObZPOE0_EVNGgw10b4oF0O5j8PpljSevxOLf6YUGi1sTidpNnX6UXW2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇹
تک‌گل تیم اودینزه به بارسلونا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/103129" target="_blank">📅 00:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103128">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
📊
🙂
جدول تورنمنت سه‌جانبه اودینزه، بارسلونا و ناتینگهام فارست؛ دیدار فینال لحظاتی دیگه بین بارسا و اودینزه آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103128" target="_blank">📅 00:35 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103127">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=Qsg7Ngu8wwHhnypeypTFBL1zR8ZaSf6vIcp847NiBg0fDka93UyiVo7S-FBpWO9fLLNJgnc7AwZ2ceA6J9cLxNQwJbUNX-By-rEqXHbxKO733DSTvmyyoI2SWhnn-DbBy_jmAzjzXv_kwSbmfGNk6g6vIWeIDxcKtok6rNtKGLpzm4VqXbbBI_zenoInovcBA_o5tcaiubAu-L8CGJJzWV1H1mlpCcQiqvtauFNPir0j-mK3EAaDd-JPdT05JhIg7k5kMADlUdnMz_i5BYDh7Vni_ZWVuqLnvzKC62jjfF44lmnw944BsM3cOS15P4hMM9eo_M5q8stoIexY_s00_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/019d8fa87d.mp4?token=Qsg7Ngu8wwHhnypeypTFBL1zR8ZaSf6vIcp847NiBg0fDka93UyiVo7S-FBpWO9fLLNJgnc7AwZ2ceA6J9cLxNQwJbUNX-By-rEqXHbxKO733DSTvmyyoI2SWhnn-DbBy_jmAzjzXv_kwSbmfGNk6g6vIWeIDxcKtok6rNtKGLpzm4VqXbbBI_zenoInovcBA_o5tcaiubAu-L8CGJJzWV1H1mlpCcQiqvtauFNPir0j-mK3EAaDd-JPdT05JhIg7k5kMADlUdnMz_i5BYDh7Vni_ZWVuqLnvzKC62jjfF44lmnw944BsM3cOS15P4hMM9eo_M5q8stoIexY_s00_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویری از مراسم ختم خورخه‌مسی
🥸
😔
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/103127" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103126">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app-release.apk</div>
  <div class="tg-doc-extra">4.5 MB</div>
</div>
<a href="https://t.me/Futball180TV/103126" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎲
همین امشب با اولین شارژ
🤩
🤩
🤩
درصد شارژ بیشتر بگیر
همین الان شانست رو با موجودی اضافی امتحان کن حتما بزنده میشی
👌
👇🏻
👇🏻
🌐
Telegram
🎲
🌐
winro.io
🎲</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103126" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103125">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v1AKdJGc0pPAgxiHR3UlapDs2wtgzn0VnEG2K1oHNQ4d3SYt21wcBLUc_nLJJV0_4Th2l9yvaQHfg1_5zJi_-VYI7XMlWCS5pwuFjkopw5j2j3DV7OWiN3UQ5jupkAs6FPNLCdUNI5GkEm0gGQf982gd6fTdhcVv2yvE4s-uz7yqjgcEU60WrfOkFiVKo_ohTXu8HDclDrQyjdAv7AiDpoJdbFDHfckdaei1kU0EoSpF4kHvKo4sIGAOlfsRy8zt9XVa4EInnXXNW0nUx-sgWvAkAPWaFhATpiqlEH7ff-j08HPUoCzeo1agoAl4J2cM9iNgDuZ4fz3j8OsIO3YCPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑️
۲/۵ میلیون شارژ کن ۱۰ میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای هر واریز در وینرو به ترتیب 300 ، 150 ، 75 درصد بیشتر شارژ شوید
.
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن
⚡️
🎲
ثبت نام آسان و سریع کلیک کنید
✅
پخش زنده‌ی تمام مسابقات
کلیک کنید
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا a17
🌟
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103125" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tuujFo94t6cgMEjgR5xHUw_DBUcS6sa14d9M4hYEwRWvu_ViW9pMqMo89U8j_hA1sQ2xzSXvkoqVlAJlbvCgIcJFizd6LDWbsq4XqiSq0MbK6e1M8fLoJaeZRAn_I6v9KfLa09yDv8KCFQvJlGjKdrmVRoB6snWOuGYRvg-21AiTNwvaLtH4H_JsCQdSXkXQi8tS3SCZwmS20Tfq0ulnWFyaQhxB-cX-X_aFXZgOBRCdMDQQ208tzMLYlCS0dCw4ipyuAHkYf-oCGgCidlEhvQnL5_rn9qOh7v80af9UozkQBTP0V2Nd3xth96NfTapuH01dbaPE6rbXPLYEHk0KIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=IA9lKw8vpZzB0F-b1wWMYPJOQlnqfJnDHsWhyJHtC-tSmlK7qQ0aiQtiMy5GdWg9WlHzGepjKQ4bImFcDUP52RZJTJI_jdBQ21710h2TQvOgbxFVSSLge5RUz__zAb6_Eo6rv8l1PuLXFzkfcwVPvC19Lu17yY4IJt-glnKr8YjdPj8fdUV7_6MqC8LUP9VvOF0I8CIESsqnv-ywxTpO-QocPpdKRbphpeu3lhikQFm6Tx2VibbpK1iy9zaAxmG-v2wP3pDReZ0v301sBqlha9_M6-BOQ3VNA3J3XUAnsRmWP7GcPQrfZQqkUlsRc5Ax3F2gaLv1VphMM13DvRqG5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5e8a9ce1b.mp4?token=IA9lKw8vpZzB0F-b1wWMYPJOQlnqfJnDHsWhyJHtC-tSmlK7qQ0aiQtiMy5GdWg9WlHzGepjKQ4bImFcDUP52RZJTJI_jdBQ21710h2TQvOgbxFVSSLge5RUz__zAb6_Eo6rv8l1PuLXFzkfcwVPvC19Lu17yY4IJt-glnKr8YjdPj8fdUV7_6MqC8LUP9VvOF0I8CIESsqnv-ywxTpO-QocPpdKRbphpeu3lhikQFm6Tx2VibbpK1iy9zaAxmG-v2wP3pDReZ0v301sBqlha9_M6-BOQ3VNA3J3XUAnsRmWP7GcPQrfZQqkUlsRc5Ax3F2gaLv1VphMM13DvRqG5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمیدرضا رجب زاده یکی از مداح های حکومتی بوده که چند هفته پیش به قتل می‌رسه، حالا یه کانال تلگرامی مدعی شده اونا این قتل رو انجام دادن دلیلشون هم اینه بوده که این مداح تو دی‌ماه جز نیرو های سرکوبگر بوده و به سمت مردم تیر می‌زده
ویدیوی قتل که قلبشو از سینش در میارن و رو صورتش خودارضایی می‌کنند رو هم منتشر کردند و بعد برای خونوادش فرستادن؛ چند ساعت پیش هم اعلام شد که قاتلین دستگیر شدند
🔞
مشاهده‌ی ویدیوی اول
⚠️
⚠️
مشاهده‌ی ویدیوی دوم
🔞
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103123" target="_blank">📅 00:18 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kt_Mitho2r0THUMulHSFsQOtp1Jic9U8FHcQ9L1kAX2cNAiwSjzgPXhR9fG5gUF9FapxAjT4CnG7EFuHvLwryCaHlual2eTW0XFNwrx6mYRs6_6v5a4-ugfTGQNS6X4gJYRqyNj_iG1uG_SyXCkt9rJDE9wrinZRgR-Jc_WyHZIBLpriGZ5Kl5K_Oanp8YQrj6Ju2meIseGODktBRLHcmMwljBbIOdeRX4d6QFveDg4YGu3ZvH3PAu03edLoPnAS8WWOW8kTpLopb4ug6iNnyHPP_JrHmd2IVx5XkDhEGKq-j8XZNfbHtbJ3vChYXVwEs9ZIExECoT8Sx6t_lyf0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعطیلات رشفورد که حسابی داره بهش خوش میگذره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/103122" target="_blank">📅 00:00 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103120">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2YvYN_1p2-niMloYFXvlws16qSQHAoiCkn4-uthTwFuD6mUJw-wCDlFYm_vbsNnewgMhCCs5x18sMUMStg24AUNxZWRrj35d9IhD7rFEaB_46PWj0rsrWDyQrpMMfnvv89K7Dpx-79c-XJ6_jrUQ0gcaSqP7uhtopHGcYYPfXRKZtZDAxD3IGRi69NnaVrpwJycQugEFsMR362_gjk-b7ZtVON5IVgvjHJgcP1QxKTQuhtZYCepl-5JD_2oSWl1XniLs-Eh79Cet56WAt-ci9jl1_ZEMybpwILYvR_RGpdoJ2Nxf9EU89kwfYdSKjwbHcK6W6wGOPxqLOq9BwzAsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-72relM17ZHmremCcAtNymIH3IVXJqjQSAJDSl7EconPnyTFoiJEHaIYVEAoUs8HcuAgAW_2ucUFWGUqkrY9OecP5wopHnEQ0UWNXyHXx32WpdzemxyasxWom2t_KS_zG69GI52_6ANwD2rOOAOfiHyEezFyUVNGpdaOglkx2nwZmEN3eYn5apBrGF4fuWTLacE38ENDOcyWqruvk4O_KAAzsmiRA64jZR9Hvg7vDRYZlLVbhdIh4t03EO0jnb0d0kI-gDaidxzMiaURPAxkEFoLyzs2pgDaJb_K89qX1RHV7RxHM-Nfn70G01NrqakqJBJHdWspe1xfW4g2c4X3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
گفته می‌شود فران تورس تحت فشار دوست‌دخترش برای پیوستن به پاری‌سن‌ژرمن متقاعد شده است. پاری‌سن‌ژرمن پیشنهاد رسمی خود را ارائه کرده و حالا همه‌چیز به پاسخ بارسلونا بستگی دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103120" target="_blank">📅 23:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103119">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/feOIBCy8kwFzvyOd8ocYA9ILLjP3mxxKBN6rSfe4uZnd6AIDqc4pdfpVH1dsZ4wHKEm8KgkD4N4yWU5I7YsgK-nLEzZ_aYzfhvJImZz9URqoNIELcXrwjmSxb_PuSnthlXh8_ijxVTO_FbyRcdlQpq1V5VxWYmfMphCZYdes3SUJ6w8lo-KCGXWlai3PYQ_NvP-0VfIzt6Ai4rpUdHvYBcA36A0qfDcjx1QhGy9PWTu3bc7sJKaTW_gRLMk4DpiM6RsO2iYFtJcnXgRI1RxQyWbEwIcb5b_DSsNNx_SYrvFxQuoOnB9uqzMYD6_plCrL7p18jY1hkpilFitNkGpEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🙂
جدول تورنمنت سه‌جانبه اودینزه، بارسلونا و ناتینگهام فارست؛ دیدار فینال لحظاتی دیگه بین بارسا و اودینزه آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103119" target="_blank">📅 23:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103118">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAKjY-IUDpaOh-87XU-AuFdIrhWtchsx6v8NPiytERH1E0EvytbbSpydYqyTvbOrqXHhnf2J2jaaxGEeGPMENQLzZ1jiSGbRxyCR8Ik245OI_Un3Dce4yGoAdFe1WoNtQIJQpWwQf40B4BymoShuV2epkoNhrQF2I040lxi7-jrSdfQcch92RVz4oDB60PFvWpOUclFqClI-CJUZmmReArML-f_EiIyVSY8DkDng7IlUC9u1PzwxbmLktWZve1DFasRuTjZYsd5SebLM9w1H2b7tj5qbW7rSF9qf6m3xdZoCquax5YLRRz1ifJSitk9TD2W4hP86lsdy1FV74OYTKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تسلیت مارادونا برای مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103118" target="_blank">📅 23:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103117">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq5XOoMwGkARI6ULhSgw04SSXGl92cUQNBTWVwWqSLIBna6wsUvHu5OdQs1Aaeb5JJK1si003rVAe518aFYkb9ORk0VPLwszlXrsZXGeG3tfHR6seAqTkrL6h8iNEQ_HTufy7x5TTGqeKwli7yew83rYOz9Qv-aEPKqWVUPOmSNvpfj751ukmphYn-WYgZVF1GxS2qdSy-b8e7VDak7_tyZalwzZdKO1_2MXEdXIbMGc5J0Dx0UfbyLLIkpV9G-hMDXNz732NeEUGUroJNorMZso0elBZiGTQZKSc2_3cBNrDNaS7pi8N-D4pT3_IYgDMvTVesCrm-_zwsZLVOPvhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
پدری هم بالاخره بلوند کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/103117" target="_blank">📅 23:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103115">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWmEyBZgK2TYe6SrCiWTqhFu-EP4_Z7yE37NnhVCthHyBS76zJ7tIeh1b-dtPhG7Ynp4EG2hcAMGzm1DzV8OPGKtsOAENFLdIMBdovhSgGGhyjaTyCLQpGV8ZYhkzVMT5aiS8UQu7Pk84YoK-3k3awLI3YzRODjaDHD2vWZKfU0oRnNSWx8NsQh4_G_0V11S_c-Abq3brozf4XT732fXjfA8tA6eMsHAvZpvaApU7Zw6CG_o10jQfz3ZkCQDngOg3bR2iGCMbU-Vv1OtZ9IVPye_HZmTRRuI_31PqeqW1dkMCSx3qIHuAPWRR5DJSX1t0ypnRpBwhdFvPRM2gDdr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hE7YkY82rHHNhLAf2RFtcUaLVS6ZJmGZczMIBWtowFNje_B9tQ975bkiSFjXNa8PS1dPNu4n50LOSwPq8cOu5IpDx5qOSy5ZplLfXiLikmmtogOTp7R81wUVph12FSUrYh-w6-JGVFV4N8lzpXVN353_Jsf5sDdA9S7o8QzwgC258s8g3yP79QMVnxWVcsDLoeK6-U6a4n4OP7EjjKkuAWXxF9C7rL7x_Bw69o_Rf0slvysXWkASqYf-5iqkA43XRdOq5I7x-BKUwiJichMKUBfNYUJzDh2igGR_qNUi0lKLeYC7yznKAhesWZ48YPZZtYGsc5lggOEvyJz4Ar8fxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری جدید بانو جورجینا از کمالاتش
🍑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103115" target="_blank">📅 23:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103114">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TiNjDEiXCjI5m98rQ2MJLVge5Rl7ttEloXHTx4rGdzNa3s9KhbtHlZSfkPwbOfAYDQjs6ptUXKz7OmgwxzdPGV0FS3WNa8fCKGd-SwjT0N2IyV5gTewhD3rvNNd5xJVePVH_kQ9i198RcgCkrEhGaRumheByYfUAupve2qTT5imspGDpL1x2EmQub0v99QIqQ-VJP7X3J8CyPFT_8_w2gOrnN-oeLZJH0QmUdguI6r-2qhGe9UFzg4ImxWhARQWdwhqX6vPhQlSd5fQmEJrqEJ3VVu9c7WA_eEtP84ADGCZSZ6LhD56k5tb5_nx4fCjVP9OwJ27-epusKoL_C9d9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
این کشورها به‌صورت رسمی حمایت خودشونو از جیانی اینفانتینو برای ادامه ریاست بر فیفا اعلام کردن:
🇦🇷
آرژانتین -
🇲🇦
مراکش -
🇶🇦
قطر
🇨🇩
جمهوری دموکراتیک کنگو -
🇲🇽
مکزیک
🇩🇯
جیبوتی -
🇦🇪
امارات متحده عربی
🇲🇷
موریتانی -
🇰🇼
کویت -
🇳🇪
نیجر
🇱🇰
سری‌لانکا -
🇮🇩
اندونزی -
🇱🇧
لبنان
🇧🇹
بوتان -
🇲🇳
مغولستان -
🇵🇭
فیلیپین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/103114" target="_blank">📅 22:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103112">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sOGDuUc4jDi9Y_hRF2EDBwF6uWWrIia351VzmXsfrjqkUH3SF-os7Pvg1F-MGkoK3_vBHJyWnSvleCWY_MmhJ2caYGrxTI-Iyu2bbZahX2Ds_AlBb5--pwGVM1RzrdrtTsKESEI_dt4ZL8J0YGYi8xcdiQ_zL5J2HDIo0-vSue3rLoFj1n1pe-P5AGb3EnxlCQwoP4xWIN7AAkowvoH74yxC-8bMJBwUEYMc-WZbZKhvfOZxP7YS9W5ZqCz6IvwWi8TtLUlCcCHbSLHsSfvyUIg6rMXPQ7F-Da7l1kI-UuzqurjnH6cLjWDAdSbjGjUxZsm5njGqYgiYJEN7BQD7QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgfFN21WxGQTvUqO5tiyHwANZf54rpztwvU4qnQpcFWC0iSvUQELD52hFUYAs7DXs-E66IvhYuvw2SwSSgfxJMB1Zxjx-yEiMU1rqUl-irIxgL5qzsP1oCjWYVY1OiWkTawb61rMdC60GFTA7CN9C_wpQ71GJvvtTVdoPj-Zq7yCMZSb1Q3SM4mI5NNrcdXElXE61nagHp4t0Bsco3yWr1kmkCw8YUIVKSfYiU4oH4LxnvDWoGJW5OtRaDGJzqT6g9juPYpJbEJi06zFxT4RxfjyPP7W0jH2zqiSyCt3XYMMhEJnFzZw5qkRaKxhEfbAmfEPTNzmSFpPTuVdP_VJfw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
مدافع وردربرمن، عبدو کریم کولیبالی، در آلمان با صحنه عجیبی روبه‌رو شد؛ سارقان هر چهار چرخ خودرواش را دزدیدند.
🎙
او با انتشار استوری در اسنپ‌چت نوشت: من فقط می‌خواستم برم تمرین.!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/103112" target="_blank">📅 22:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103111">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjMH7-Lra4_-7dFE8-sGWhai9nyiF56Er8t01fJZCjyNHaWWt7a0Gj02Rl_cvqXqPvVQCDUtlF6wylZZmGodoVKdqCPLCCUEeID-prA3vbTsIqJuI61kxlysuJo07HJYFwWfkLbg6TxSyAwZFnR8FINzBOnyK_crSfxScwbYJ9lBF0VM0EeAG4Z87SrOztqvficN93paknQOQki90BAuskIDXevyv6pMmwDb0Bm-4YRw0rged0I7laXkRzHBuNs14Q5I89Rza3CpSVZvetyi7-ttcLu076be8NAaDSMkQsuLPjNzfThhVLwe_ApcReOPbEa1oTdengz5mlJSRS0-3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رودری در یک تورنمنت حذفی، تعدادی از بزرگ‌ترین ستاره‌های فوتبال را مقابل هم قرار داد و انتخاب‌هایش این بود:
رونی یا اوسیمن؟ رونی
بنزما یا کین؟ بنزما
کریستیانو یا لواندوفسکی؟ کریستیانو
زلاتان یا آنری؟ آنری
وینیسیوس یا هالند؟ هالند
امباپه یا اتوئو؟ امباپه
رشفورد یا لائوتارو؟ رشفورد
مسی یا صلاح؟ مسی
رونی یا بنزما؟ بنزما
کریستیانو یا آنری؟ کریستیانو
امباپه یا هالند؟ هالند
مسی یا رشفورد؟ مسی
کریستیانو یا بنزما؟ کریستیانو
مسی یا هالند؟ مسی
کریستیانو یا مسی؟ مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/103111" target="_blank">📅 21:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103110">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ayF4SNIcVdPsCWvDOb8h2pUDZr0e1Q3dOPAePH4PD5MLDtGZiKqOxKKA8c-ldz8UHEOIR5XK5Gj0C0QIsvvKlfZrbBrMWBzEme0DUOgRmCgErsV3cfkVNQgJ09eGCk6gk2uD478ETrc9o7rybHS39Gzz4-MNE6z7R2rv0E-IA2ySPY8Zr3-4T0_OtFvFn13uEYyHJ_NtKdSwHb_O1pAiCxuHhRzbn6pGy5-YbJSoQObshfFw5gCqaN1iZ_QhkQz_Ec0MOAvvwbl9FzkP-or_JuqgyUZw0wxoazcbTAxOgP57azsZqj5peoJGtms0ne-rzmRI8cqv2gZ5SpDr0KOJgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔴
گری نویل :
🔻
من عاشق بازی در آنفیلد بودم، ۹۰ دقیقه شنیدن توهین بخاطر ظاهرم، عمدتاً از طرف پسرایی که شبیه سیاهی لشکر فیلم سیاره میمون‌ها بودند. یادم می‌آید یکبار یک پسربچه تپل فریاد زد "گری بابام میگه تو یه جقی هستی"
🔻
منم بهش گفتم "من ۸ تا مدال قهرمانی لیگ برتر دارم، تو غیر از دیابت چی داری بشکه مادرجنده؟". او غرق در اشک شد و سرش را پایین انداخت. رقابت یعنی همین کری‌های دوستانه و صمیمی
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/103110" target="_blank">📅 21:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103109">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mY9A3w33E6u_4C3WMt8N59sNNUbzmvtuoOHtbakwWr4ASeaAOuqpyCsIQaodeghJws60UaejMyGWku-LpdkmfB0qD_936t53YRzV5TpxRZ32uaH5KtYUNerbu3fjMtAnDYA4TdN7ZOyxOnESAtM8QNBHpijMu6P_05r-hsRl2WmzUVDCl3xFptZ6FgT9Rk0ajbEnNayvkYm7AKqJ9gNtd8Zlq7-kfpFNz72chLospvKvVQeQgCeNjBqtRM9p26bMiKLKa8yRKZjKYjgbqiqipBVyYu0ugUeVEhkiCpIf0lMpMGmXGtb8Mmci51CANn2gDuvZWAn-IlSiP7ZVpavvWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترکیب رسمی بارسلونا برای دیدار مقابل ناتینگهام فارست
این مسابقه فقط یک نیمه طول میکشد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/103109" target="_blank">📅 21:28 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103108">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfgKIai1XcIP-XV5s0rZj_P0GTOZGCfLcLQCKSqPRAOdTdJLwWUY8QBERAMSS_-7nyQWrdm_lRbizEt_vHyDlB3tNrH0txOVLSmoZLv_wZdqyE9ogjnn4xTZBCR1fSDDHkPCZbNC7bMkir03YN2_9o-z7fZqsy7ojjt174EM4T_JGJ-8ZTb67w3ovbj_Wq0QCXLkV6WkLp5sd-kbWVDFqvQEdsLuWQfwwsj0cEmk8uj7Sd8hsvYgKWIFzMpSBgGYl2P0VpbohdY80s3TZXQbaeWD3E2QI0RsZzvuodnVi17sR6QjyFwgx0n6ljVNq0BaSmjVzlk7spBFmjCKM_jfEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم از فصل اول حضور نیمار تو لوشامپیونه فرانسه؛ شاهزاده تو اون فصل تونست با نمره 8.90 با اختلاف زیاد بهترین بازیکن لیگ فرانسه بشه
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103108" target="_blank">📅 21:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103107">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YeCe6DIdMPCCBH3tN2W3RmIL8SWN_FbPUnN4lY8z8dsXC4fWJMAmWA-c59wWXmWQoHK9piPs-38Tgys6LOKXP4Omq2ctgZq8Rq_3JfOfzXNY0ZdB6vkcWRb70ix8XjZl8lGTD9Fsuu3rRCsAPi1DKND3c6J5p8quRKGB4Qj6O7RkIObfyxkDqVhvVIr2qNvsIiTubKsnxGsff3TNVmi7iujlFssJMTjzTBQECd4Lqa7aOSdbFhaeA6PhkhzzELOulKxVFISWtHsZLUPb3c5Rw2An-7nEnY7h01FWV3phy3Jl6u73-mU3XSdyakXFJx_tKPosyiWcrOMlDi-T-DVHZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
بیانیه باشگاه رئال مادرید برای درگذشت پدر مسی
🔺
رئال مادرید ، رئیس آن و هیئت مدیره آن با تأسف عمیق درگذشت خورخه مسی، پدر لئو مسی را اعلام میکند، باشگاه ما میخواهد همدردی خود را با لئو، خانواده او و تمام عزیزانش ابراز کند، امیدواریم آرام در آرامش استراحت کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103107" target="_blank">📅 21:16 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bMmkNAkoukfEmcuAV1L07GoFWXl6JiY-aG5ySbU-IZu3d2wb5_2NXSVZ3wCY7PIv4DTiYcdCUgQGLwmzGoWEdHZrEIdrrSmv5_ogDjIRVQ42sIuBVHOSMlBcuUveljrgq5tNVNtjVA9WzcV259KfjEFb7s6qqsgu-RVW4A9ECcFUcXecohqV97VmTyFQS6th-FnXYNuwQBUyXCkd48m2o0NvYw88Zv9cxjz2JJU6dzWhqer4UNin2FhJsVIjnOBx4RN3UdQRcyyq4sYlpyB-e1NrLgmJLTDTLqsF8MoY-LSSWWVn5gl4AlmdLXMM9ODRZLRbjcs239FArt-fzUFV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bapgamg_t2ZWtUtDJWr7JRXzR-22pDL4-I2TXWo-XxX61X_lZLZN_y5Qgt8w9bJ37Sl2RFTpw0R75OUID8RupduMKNIVXgXAsSyc9E8CDu6vE3cwLlnYRS4UthRpvuDIqKOZwo7PPy2sAQgnRmOdvcnKq_fKrAz5wg1EYzRMzT-A4GpZxFESoCW-v2f4MrTzun7Pq_Rfv2Vjqr8mdxIitvClm8Fke0DzWqnZfC2uBi6hzH70U-XkyuWoNmbXGZxeR4ACWPRpwA-8kaO-_m_qynA6m1_wn1gqc5y5WPL9EOiLgMKR2DnY-E1n-JowCNwvMJbCl0XDg-9M6YwPSNlmCQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آلپر ییلماز برای گل روی ایشون کل پیشنهادای خوب اروپاییشو رد کرده و میخواد تو گالاتاسرای بمونه
😛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/103105" target="_blank">📅 21:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103104">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113b1e4e1a.mp4?token=ZZ06FwU7Unb5EUex_HgHXXT09NHA-XWUheULSuOn-txvIFVpgh-QXD1hTEFE4_ntra3BUzzCsh9mvleO4UbzS2PctgFGWilO13Vut0DRl0uwMcnfGlKsQU4s_fTH5UbaRvHLLJWZbCSitmfiYY-x0zpZZs9TD-CVbMOm3iAS5eyftx7sCPbpgX5-zEV6E5R-sb3XsRsrZ8cZvu8lCWoe0w_MF8MGbxIcbiMQX6jftnlhdsvNNiIMN7ZfTIFzP8r1ZqMkdyKh4eKkOZu2IPGmdd8t_dpbeoX6yRolkZaDNHTT-bm6S2okbqMS0GcZjAShtwl3vRVT6Xw7ufac8DHWbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113b1e4e1a.mp4?token=ZZ06FwU7Unb5EUex_HgHXXT09NHA-XWUheULSuOn-txvIFVpgh-QXD1hTEFE4_ntra3BUzzCsh9mvleO4UbzS2PctgFGWilO13Vut0DRl0uwMcnfGlKsQU4s_fTH5UbaRvHLLJWZbCSitmfiYY-x0zpZZs9TD-CVbMOm3iAS5eyftx7sCPbpgX5-zEV6E5R-sb3XsRsrZ8cZvu8lCWoe0w_MF8MGbxIcbiMQX6jftnlhdsvNNiIMN7ZfTIFzP8r1ZqMkdyKh4eKkOZu2IPGmdd8t_dpbeoX6yRolkZaDNHTT-bm6S2okbqMS0GcZjAShtwl3vRVT6Xw7ufac8DHWbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپرایز نقل‌وانتقالات تابستانی
🔥
🔥
🔥
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103104" target="_blank">📅 20:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/molWLx52PgZozurBlOfDqWT5H6zB38EWxTM9H3amehrqRlguf65U0ByX8-sG8PXJ_NG3NhFKvL_OtBXoGfN5SegqmeH3oeF6x6w-pN2Ngxod2RDfsfjx8lj7K-V-2NCx-uxRQKUGGmuZ_zAz2HhzyIYbvWEnEkSfhOtTb1PJO4oIOW0S7PXabg3FTTeJtJ_CEsEUN7hcv6xjckXSNBGFuPhCnvEW_BZZ-MVV8GzJFlVVot9YI5La69qetQZuka9vnxS7_HGndutukSDpS22uZ2rxla8GXFRNaqQobC0K5PSufj6H6grCCofs2aRJX0_DzuADXqbnPazSBUZEEvGkLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fdd1aafd8.mp4?token=tul1g33QF8-9tk2Hk9jCuXq8nVrL59LlLt_FtrZ6RTRNnVKoK4nVoFdO_HstSyAaAhxsXJ7tOxcacT51_NTmjwYHJ_rYNeTTLJBDJKOPbgJZHQck9OtClj1buUngF7x-vl2aTJTBnA4JQU8NyOhikD9TKQsLZVsWfyZ1b1Cupsle9H7iyD3IgfRk_2j-1Ub2aU6-Z0gujE0ZQrpwJDwyQsVSXjRbGT7d-zv7SBE2RvYM0SdwYST_UYvCJomSp_DyEMyZZeXcaeSKGDQpyfvlJuWifefBAVmKpsNR2FmBhjzjYRnB4VotFIJy0WdBjUkk5hdhnY3Iq7VESrOxWyxmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fdd1aafd8.mp4?token=tul1g33QF8-9tk2Hk9jCuXq8nVrL59LlLt_FtrZ6RTRNnVKoK4nVoFdO_HstSyAaAhxsXJ7tOxcacT51_NTmjwYHJ_rYNeTTLJBDJKOPbgJZHQck9OtClj1buUngF7x-vl2aTJTBnA4JQU8NyOhikD9TKQsLZVsWfyZ1b1Cupsle9H7iyD3IgfRk_2j-1Ub2aU6-Z0gujE0ZQrpwJDwyQsVSXjRbGT7d-zv7SBE2RvYM0SdwYST_UYvCJomSp_DyEMyZZeXcaeSKGDQpyfvlJuWifefBAVmKpsNR2FmBhjzjYRnB4VotFIJy0WdBjUkk5hdhnY3Iq7VESrOxWyxmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز رسانه ها یه خبری دادن که کریس و جورجی قراره توی کلیسایی تو مجمع‌الجزایر مادیرای پرتغال مراسم عروسیشون رو برگزار کردن و سریع کلی آدم رفتن اونجا و جمع شدن؛ و کامنتی که رونالدو زیر اون پست گذاشته:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/103102" target="_blank">📅 20:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QG8ndyzE_2N-sEiGQBDawNYPiy76Jwr4ZQHzfV-rZBFj9z6ySxcrwAIBZt_XDxiLXwy6GCdDbJKkVeiHEL24pa9rnDbLO5zbcz-Uvuw-fMyip_SBeYs09AFbEMbCJ38OYJoWPG6gpxa6V6Tg_uOYbfjnCxUCAV5RpC887eJN-1B6CUYSF1XTvnfEtXqVJLKukV1oMHFizfr6XsXbr1C1YB6oCmdhRpkurR1sqedOQwHrTux4SIxaCMJuGzEnZqeF_vg2VPj-SrgMIzLxlJHJRcIg6K790EHrp_QGTpy5gfOW4Z3ctLDAAE7zTSGHCJlH6Q670hqdKmB2pUIuHRNBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🔴
کوروش اژدهاکش هافبک ۱۹ ساله آلومینیوم با قراردادی ۵ ساله به پرسپولیس پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103101" target="_blank">📅 20:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQmwyQaIWLe8QGK-GogX4tMjS3ZUanlVUi_s3abcifKqYB4epQNS5l5ElupCVki0xhlMkuS5DeOKCJTfYPvXStbPS0J1vxTN67Cow7vGW39ntN2ArsfZAKjhAchmKR8DuZ1dI_xJOqgUlfx1frNYOqmeZtoMmPqYOOfvaN8WoGO8p1WoINI_eY78AXyFNdDiuOCDGLmzG8jmgO5mFF0stsOdMIb7bq-FA8GzZiVQHVS-3_8-y1YfqMPQI5M_yW2eDklfXf9V57LPpx6j9p_DhkGeH3ZnrCJp3x4vsUpvEids0O9wYoYI1U1XKFQOR9hNXlzAsHd7Ah4kXGOSXh01sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
#فوووووری
از رومانو: همه‌چیز طبق برنامه داره پیش‌میره و رودری بزودی بازیکن بارساست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103100" target="_blank">📅 20:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63a86fcf1a.mp4?token=F_zws_IZpu2lPO39xufIhuGvmgaGM07fqKcX_r6M5vvmHncFOXChiLYkJ3MsPA2diWqCqo1NeHkhRSynQT4Dlp4qiyJY7xMq_eVmePfdqHdFKnmo2T9zdjXnIRcEx-cpkmjZiA1ufbtSNiYDDCeFIfWm2XWu-PDzaNHNAl6ERpNG4WNV_YFCzacyDU5p0xmVUNpPKlcQEahUDdfmqCfakTbl0WorCWyW-7rrXHL_i8f4p0RYB_aWW1oUX3OZ94p8Dkbb_38xhMNa4HteGl77kvwIIVzXZtaT0-T4TzYOt4z6pxtKLQEJ7xsHgs61-m5CRBM7i7XW-B_DbRgxUipg2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63a86fcf1a.mp4?token=F_zws_IZpu2lPO39xufIhuGvmgaGM07fqKcX_r6M5vvmHncFOXChiLYkJ3MsPA2diWqCqo1NeHkhRSynQT4Dlp4qiyJY7xMq_eVmePfdqHdFKnmo2T9zdjXnIRcEx-cpkmjZiA1ufbtSNiYDDCeFIfWm2XWu-PDzaNHNAl6ERpNG4WNV_YFCzacyDU5p0xmVUNpPKlcQEahUDdfmqCfakTbl0WorCWyW-7rrXHL_i8f4p0RYB_aWW1oUX3OZ94p8Dkbb_38xhMNa4HteGl77kvwIIVzXZtaT0-T4TzYOt4z6pxtKLQEJ7xsHgs61-m5CRBM7i7XW-B_DbRgxUipg2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمیرم برا مظلومیت لیورپولیا که قراره این یار مستقیم هالند باشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103099" target="_blank">📅 20:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd45b921ef.mp4?token=abG85qj0pbKCga7t6sf_5ikdRNLoJl8rcrj81Cl7NJr94Faq_Od0bIM6HMKXcBug9-xNSqmxPhX61ZG9QvtmPWFyj4wClugEYQsbFuHwV-hZZEJYZX1JFMiR5vI9iiEuyHM5M6JcC3a11ebfijZa3_oLAO1MVY0iXAcD9LLTJFHf-IqWu7nphxoLjdS8-SwFYLmQC-B1puFKG6_VtIMoaynQ9hAqA8osimhIxeED0Mj6Isav2S8EQ1u3XUY2C7BrLlNnpHDdjmglvXcjAEforJPZHGyDoqe7_Beq20tzNGiw1Zx5fHziu7CjqWSEAZDp1ItKKTBqdQE6S-5WQcvnAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd45b921ef.mp4?token=abG85qj0pbKCga7t6sf_5ikdRNLoJl8rcrj81Cl7NJr94Faq_Od0bIM6HMKXcBug9-xNSqmxPhX61ZG9QvtmPWFyj4wClugEYQsbFuHwV-hZZEJYZX1JFMiR5vI9iiEuyHM5M6JcC3a11ebfijZa3_oLAO1MVY0iXAcD9LLTJFHf-IqWu7nphxoLjdS8-SwFYLmQC-B1puFKG6_VtIMoaynQ9hAqA8osimhIxeED0Mj6Isav2S8EQ1u3XUY2C7BrLlNnpHDdjmglvXcjAEforJPZHGyDoqe7_Beq20tzNGiw1Zx5fHziu7CjqWSEAZDp1ItKKTBqdQE6S-5WQcvnAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روحت در آرامش خورخه مسی.
🖤
🕊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/103098" target="_blank">📅 20:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=fysqqQ3VwXiDnFIU9pSSbIaz7YQyAGlkn8JMwKfhoTMKcE7jRr8oDVi2he8G2qM6Nvk-qqP4uVnTslOd5twvv5EDDH2Mwta5AZEoaBh3SOTfZFBQMBDZDs0JerhbYuVNht-__NXJO0Y1Wj3M42HIA10cdzImiMhQZnLtLpvsj9Gr0OcYwLWzV4ck745pL2l5oOT-yqJN50eMy6xZhDmGTiMLdLodUmROYOzKigiKgTS3hihzj9V5fHjFkv-umitkDeI40HlnmtRza-F9K6dIxvz0es3fXp5twkA7_r9mPny6FZ9z19bA879vsPiQvQYnB1gm01mu34Fw-h3jWNGGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beec0f3cef.mp4?token=fysqqQ3VwXiDnFIU9pSSbIaz7YQyAGlkn8JMwKfhoTMKcE7jRr8oDVi2he8G2qM6Nvk-qqP4uVnTslOd5twvv5EDDH2Mwta5AZEoaBh3SOTfZFBQMBDZDs0JerhbYuVNht-__NXJO0Y1Wj3M42HIA10cdzImiMhQZnLtLpvsj9Gr0OcYwLWzV4ck745pL2l5oOT-yqJN50eMy6xZhDmGTiMLdLodUmROYOzKigiKgTS3hihzj9V5fHjFkv-umitkDeI40HlnmtRza-F9K6dIxvz0es3fXp5twkA7_r9mPny6FZ9z19bA879vsPiQvQYnB1gm01mu34Fw-h3jWNGGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
نیکی نیکول دوست دختر سابق یامال:
یامال ازم سو استفاده کرد با اینکه من دوسش داشتم بهم تکست داد و گفت هیچ وقت واقعا دوسم نداشته و فقط دنبال سرگرمی بوده، من کل شب رو بخاطر این پیام گریه کردم. اون خیلی دل منو شکوند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103097" target="_blank">📅 19:51 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKqfVj4ANBaqfUKqinrXxWQLssw8T0mTGHIAcm7EnUy7GqnKS1Pv5daHurKODAfGCdXvRb_2BIF_-tSGK73A80mjGgN7zauOX-XaLUqkAu4kBMtJwfB1JzBhuxBoj2kC7oYy9TUJgeKyX6IIiMurv5B2XWDjTFb6I8Zxc87xtyoRS6fcMg0CkDTGITBSzDwJfQJir2YHE_j6iDjExiVgBOvEDvUcGx-V2mVqtVPR2S_Et7paCvKyGJJa8BWa_ONwuzDKVz0OHPc2Y-hAKNOgNwcCx3_PI4H0vp89uH_z2nmuGdgavr8J4WIGNTdHZ81aEDCTw5g2hlw0V4EXw8qtiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولی جدی از اون نسل طلایی آژاکس که نیمه‌نهایی به تاتنهام باخت هیچ کدومشون بازیکن درست حسابی نشدن تقریباً
دلیخت، ون‌د‌بیک، زیاش، نرس، تادیچ و اونانا
دی یونگ یکم توشون خوب بود که همیشه مصدومه؛ جالبه همشون هم سود مالی خوبی دادن به آژاکس...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/103096" target="_blank">📅 19:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103095">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=P8ILGAJlFC4hivnl5o2dCWNDj2kRTl2WOdrGEwChhcHUHt8fz04aWEoWS9CRTmiRKIxkSTVyOfMwi2Lorf8R0nRrMrwUsZE6Nd_3sFikzf06HEqhpR_RTqRC5aIxuhMYQnPcrUQK9D7dL6iP9-lfDfvxl45vWLySCvHwa0O9F9EguOrcXWmbR9U_DD2C4FW3qaTOzEg_nkl8ayUTVq4SDtdQmG3zSnBEIRnI7vp7Y181Q0ZmCF9khgDy2UAKu_Ftb_ZItGF-Bi89VuBlTojdeiQDiOlMNIHiBOSy6CPLzbhhf8Yy1rpkRX4B1GW6HJt76rRj7L-wdrhwTPBl6dupXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa788f17f3.mp4?token=P8ILGAJlFC4hivnl5o2dCWNDj2kRTl2WOdrGEwChhcHUHt8fz04aWEoWS9CRTmiRKIxkSTVyOfMwi2Lorf8R0nRrMrwUsZE6Nd_3sFikzf06HEqhpR_RTqRC5aIxuhMYQnPcrUQK9D7dL6iP9-lfDfvxl45vWLySCvHwa0O9F9EguOrcXWmbR9U_DD2C4FW3qaTOzEg_nkl8ayUTVq4SDtdQmG3zSnBEIRnI7vp7Y181Q0ZmCF9khgDy2UAKu_Ftb_ZItGF-Bi89VuBlTojdeiQDiOlMNIHiBOSy6CPLzbhhf8Yy1rpkRX4B1GW6HJt76rRj7L-wdrhwTPBl6dupXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدیو منتشر شده از عروسی رونالدو و خانمی
😃
😃
😃
😃
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103095" target="_blank">📅 19:26 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbzQxgEdB6TNZEOSspf51l86zSTDwnrM_PafFkGUOe4P9JneXXmmg-Gr4bZ8Yp4oxqYv4vttP9oC-VA12tw7NzewJVGpjAttoZ9qA3uf57nj_ttByj4v6Dw3dgBMqp3jBClU5uJe8ZJbZYcuNoGq5yyFVt-fR2WXfSC8_9GqoNm0NP0spZjahR5sX8VmMd_IheIkUHRKejbybNv5RcI9QuhX6U85FKzQpXFE8uQ3-lrnwyLXENZyUUO2mj8q109BlRIK1ON-deixPPtWkJUeoNt39rUHkpQigcm-sGlsCrJhWrMJHdmHiVzZBeRv40q2vOOcwWMymNBb22ZjKRZhgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VQ4PYnNuuLJoIbm-5eL9QQN5MDi1Xzepvt6Rc-jnQZ76-ls6nM2cQT2KBQefe9GVHp2OLT9Lc3AaMs9toXydNmtc55ERdaDNxjVCsahXVtlGsByn7xR9175zppHIF417eL3VA-niQXG54H8LXuW7gI6cbhvPuzMT09KIf0B4hghYnEDxbC-iLdwhk_2LAfcwXcg6hde1rVUnT8KIu8E1NIvNPNBg3p5-TUcivXxJAH2nlXywhXPn8ogz5nNreFteRqYEDQM7KfcYBqWwPAEAarai3YLnRV7Hu3duBic4AnztXUOmD1bDYm-LtGC-a4b5osEHFpsBiAEV9pMGZUd5cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_rlLTYsGLxuo73QtKBahFs41JkAG8ncLhssULu_8UdSPS6LvkVIV3qzwaGj3pDDDpbI_J31WexiLrQwxM5SdHNDZ94pAde1LqqpWFMSB78w670J3oVxdhYTA-ioiX8997J9kq7nzMyXNxEIRaLC-0zllKfnBj2U-Lpy_TPyeae3PSfiE1aG2Ns2nhec-LqK20lX2WkXFXUK5f3HGyuyMXEI2NG_qmNNWyL5qlegHaF40ZR-ojv3x2lB3Xqoyjaoq8gjyabO57uJZ_eQDENdBxQJkHVx4r4p2ynlwCRgKDuZx7_bTBnlgN3jXPYGVdgVLU4A8yjxHS2HXj55Rr9iXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
✅
👕
کیت سوم فصل جدید بارسلونا که قراره ۱۲ اگوست رونمایی بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103092" target="_blank">📅 19:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mwo0f2i0hlVjf-JxMNMTL-JFhDeJFgFcl6lTome4wmuOBExRB4jzD7p1Qb26E1irrXKGBgf-C41nk4msTYL1e244Foqyxd0v1aQN021RtnddTM-qDb8GhKxNbHMOY47CqjWmkT9NM55enwhS8-tS_YuEG_41HUubqbFFEoWOx2CjDdzzj-7-Mf528euCLI-0aRWQsQfoS-43oUfbEPCugNDzwyeqh2aEoF697EHmVdXmbtGlmr-m9nIUVpIkj8mFOSBtDu4PJ1M67Hue8Ujh_a0Gb7ZeRVyvOTFxlOmoYnu7bAgceEiXk5N7e9WJx9N8CIZz7pfm7wZ16t6RsBJPrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟥
🟩
پرسپولیس در دیداری تدارکاتی برابر آلومینیوم اراک به تساوی یک بر یک رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103091" target="_blank">📅 19:21 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUDQ2T_6W1jFY_9QR6KFwNwkefKwEmO4zcu1WLFB6yD-nG4yfzsOoKO2CDW0D5gm0oyOa6pQyrOFmlLcQEE0Vm-fjv41cPkC0uH0luwLUP7BONN08p7mMgFuddi1HhT8WUuG8wVf5Pp8sTEatwRT-Ji-OCPZrW5-cEkYbIXajzbwU9aVoSryun1rnWK8wAX6_NErWuGb6rOezBRS_v_4TRMouVh6sGsQCzvWXnVmk6xJJUOMZvDFkme5tcYKqAjGfJFBjPatn3FQNldEQIALSuTWLOBHJv1p54nbFzZQ7CUiN-YnLys_4pC9jYuOG1aa8qKIqoruuHwSkk5QkVxUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ترکیب رئال‌مادرید مقابل واروش‌مجارستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/103090" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103089">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی
بونوس هاش واقعا عالیه
👌🏼
بدون قیدوشرط
❌
با هر 1 میلیون شارژ ،
🤩
🤩
🤩
هزارتومان شارژ اضافی بگیر
🅰️
❌
❌
طرح شارژ رایگان فقط تا پایان مرداد ماه</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/103089" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103088">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3KI4oUhX_76qvd4L2ILFGJ5lukPfjI2TKMdlqfO730iy2rAQX4wYJxLLztw1JPmBUjupdr7NE_Ufi0e4abtxzIFfZg8cH9H0FuViRaydP-4ME-H4Dlct2Yhp9stNV3_-2ReKEmM47OgyUmd-JiCmz0htE6PJOlsSQ9mJSV9KwWU8BxyxGRVvtR0AzjtvDnzujLxG2YnHeFoPWICe3dx8tXRrHyS2RohsaiA3FPEl0B1_F5hYvHCD9J4mHLcp3iDNxsbmoGKX4Z-E_lxSfWWTvTuNvEWZqo_WswFhlcZ2L_7iO_cyfMn3D5xT_vqZg1XpYiZOaWuwEW2s73iHSumGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛍
#اتلتیکو
Vs
#منچستر_سیتی
💰
🛍
#لیورپول
Vs
#موناکو
💰
زمان: یکشنبه ساعت ۱۴
🚨
تجربه پیشبینی مطمئن با
🤩
🤩
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🤩
🤩
درصد برگشت وجه در  صورت باخت:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
g17
@betinjabet</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/103088" target="_blank">📅 19:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103087">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUsEusdQpWm5QZi1INYneSRcTuT6V5Ck-55Fx6Uk_AE83oxwLu5nbNTx-LKJctpH7efYib-8dBDebpUEfx38vlElBy2guAbvubGHF4zpatLDm7zHmTXvHQyxyJQjJ82ryrlU8dgO-ioL9noi-d_9ZklvGwWAN7Jwa1iiDwQoMRwCaAeg048rsirRh6KxRkmP2cTZpvrS0SGD8RMpU3A9h_R6pBuUF5cNmBwdJg4CCDvAju8sZiTvgPyenNbX6xMEtC4nf2ZatoYuxg6Wrs2RzYs9eZvA8-GQmIYHQs9abtzzqxaYYiKqTm9b8ATRAA_Pb1iPgfksqH_JtcX0S2rBJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نتایج چلسی با ژابی آلونسو تو‌ پیش فصل:
- برد جلوی میلان
- باخت جلوی یوونتوس
- باخت جلوی تاتنهام
- برد جلوی سیدنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/103087" target="_blank">📅 19:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103086">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47158534d6.mp4?token=l3uA4oTKrCpnM9Op3Dmn1FHgot7iapUKUdN-ZHtoYcOT597pZXC-GpcxYsxuDoso_Zhr9Cu6dm_aeke57Y87ynrQ3KoxjX6-9g3ZAFcsp_MSB-6syVecL8W0TjlY2lGNFpVzZ2uC2GZ9jatbFhqhuslzfUmmzMXR0zj-pzRArqkhY4h28z4SC-1AH0xAbJQGVxBk6Y7oazf7S34dpUoVDGhwq3RjCznqPGp7wzUShRM-gwcfgkhwQh1e3_bz5XtSmYloFxIKGDuVL9XTBKTjD8sYWFKdkL9enGBNhRCgxUXv6_Lxzg8OGPSbLtrmc9sAVaUeVCOl6HKH_SctY5JtNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47158534d6.mp4?token=l3uA4oTKrCpnM9Op3Dmn1FHgot7iapUKUdN-ZHtoYcOT597pZXC-GpcxYsxuDoso_Zhr9Cu6dm_aeke57Y87ynrQ3KoxjX6-9g3ZAFcsp_MSB-6syVecL8W0TjlY2lGNFpVzZ2uC2GZ9jatbFhqhuslzfUmmzMXR0zj-pzRArqkhY4h28z4SC-1AH0xAbJQGVxBk6Y7oazf7S34dpUoVDGhwq3RjCznqPGp7wzUShRM-gwcfgkhwQh1e3_bz5XtSmYloFxIKGDuVL9XTBKTjD8sYWFKdkL9enGBNhRCgxUXv6_Lxzg8OGPSbLtrmc9sAVaUeVCOl6HKH_SctY5JtNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ادای احترام به مسعود ذات پرور تو مسابقات اورال کاسپین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/103086" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103085">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DpIZpGVITsZWTnCd_t_WxUHAZEl38ddjO0c-SXPjXxHZ-qCw2OHVEobMxDBNXU965cZW5rvC2DW9XaYYSfPHyGfchCkcvE86rf1g0TtrIauKO7ZwkCcDMBKF06E-JGQNxMjEi4kDoFWvg5DNy4TbVPk_kx0kVwKCFRUrUA9D2QxjokaOgwvGJWKmYdgt-0y4NGDdcDdMTUD2Hv1RMt9DtS49Qnnt_uct3WV7Y1LWlRA_TemEIf1uNJerzdeSWpwhPPODATQlDYiW8fPuPHR3WpXtgPMdbeY-bF05WPD5ZSMtyoKhcRdl15shi94PrW_Q1EKMedBH_0xbHSM7lRKLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/103085" target="_blank">📅 19:10 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103084">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5956080028.mp4?token=I9V2O7naV7Z3IcFdYiFoysitsVqtKgsv2eEulG0m-q2J1jWzxTBAlEKUuhdA_hTikt_4obn9SvEg7Y7Q5KoZHNa88hWXXVkuk7CQ8B4QFrLVk03MrgeYg89rORezGzkcBVaz4B_0YOmvj9sB6TTNPsmsE_NkHGMoe7Y5A_fgXcbMU3vqvMpQwNX7z8AeYUNLjB5wa7-qvrm1-ub0_wLBf8Ugtjdey-UFYi9B38KAi7-p_yhnMT6CFU3Wspq0StqUJieCxsiR7Cui9r6JcVrtMeKatZt2q9HiR0VitVJS07QFQmxWBaXOQsig4GFJLAHubm9sRoF1DaZzzc1_uLcMBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5956080028.mp4?token=I9V2O7naV7Z3IcFdYiFoysitsVqtKgsv2eEulG0m-q2J1jWzxTBAlEKUuhdA_hTikt_4obn9SvEg7Y7Q5KoZHNa88hWXXVkuk7CQ8B4QFrLVk03MrgeYg89rORezGzkcBVaz4B_0YOmvj9sB6TTNPsmsE_NkHGMoe7Y5A_fgXcbMU3vqvMpQwNX7z8AeYUNLjB5wa7-qvrm1-ub0_wLBf8Ugtjdey-UFYi9B38KAi7-p_yhnMT6CFU3Wspq0StqUJieCxsiR7Cui9r6JcVrtMeKatZt2q9HiR0VitVJS07QFQmxWBaXOQsig4GFJLAHubm9sRoF1DaZzzc1_uLcMBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
رونالدو وقتی از سماور خودشو میبینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/103084" target="_blank">📅 19:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103083">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">▶️
داستان عجیب و غم انگیز از ناصر حجازی
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/103083" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103082">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_avQYh7CjdN9cnEMWZaDdimXTGLtFQebIBrLwJYG2iDyYXMOtugGeeWnH9xdPSsFVtsswWPRZsCXxRMs_Rqz7MOr41camV2AjCYGr1HBuw-Q88SEFv0izNcMeHvm1gRjTIklzaLbMiM9UUNdPAwG3xyPKlZsX_naBmlVof07ntY-_Dmwsr-c96FlHh-tmRANFo_iee4YqIPoURwr0h5hD9NOv_MLzQOvrqvCtpwEXYAYQrAVP-_tbTxsXeGHpzxK0sFsiAt2RbC1G28n9Dmic13kvkBRCu5onbdH9iLWoci_foEpzHUnR-vod5WCRY0EmeA13xN_BUHjTQsxs_MrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بالاخره موتور چلسی روشن شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/103082" target="_blank">📅 18:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103081">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S0Kv5iWBUJzDzuYxetbndrgpDBpR8YAxH2wJtZafHwDozaumzHAOk_7mZExJO8Xyn5YE8JDgxXtX3eAPPDbuafESEGwRbSnnGbBymE8HO4eDI1wkpLbYTXqq5nXCHGIsQ9P1Do6g6G-NgY2tVXO2RWdAxoXQz-1K7nFhqGFpRjjQ5wBBBZyh4TCOEkuVeb6Q0sDE3tZnLO9Q0eME7jarfpHPzGWvJnetkshcjC8ky_92JejiO6Ct4EXRyuNkgVwROi4BL-VPIYuEkidDG6h8vLTakPFPXuNE5GiGY_QAA8Gsr5TrWrw5Z6DeHjxNxd00TboKpNi02ne7Q8xl5D_CdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ایشون برایان ماجو مهاجم ۱۹۳ سانتی‌متری جدید استون‌ویلاست که لوکزامبورگیه و متولد لندن.
‏پشماتون بریزه که متولد ۱۲ ژانویه ۲۰۰۹ هستش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103081" target="_blank">📅 18:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jG3F3QTHvITPuj3jT0m01CohNki6jArYywoE1_Qr8DrBdoGfjKmsNkGVaIQvrmbvThr1z925YbSHoUepenQURIZVhYhw1yRgfYErYIUw4ddBaGQv6QftYXRIiJwfymKwsoGcYPsU821A_ZeDZ7HTs4eLYd7l-fbt5RMRJX_3iuUjtZsq2mVrug4IJzo3IEIX_cRiz9bsAe1bUsl6BAcPoADNDAdwepVbKjEBbhy11zlzQGXHD0m4lFlEe1QZj9lp7UIgZT-dSR1PncPx4umUL5FvCVbBvAhAWAasJ48xepTCfjVjykQ_7jv5JYDr64P8IpT4Ee7ygAxZh4GULvEoWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y4sYYZhivTHo775TlxKXq9mHhJCIJXaRUAQxPchukGUsX10r6uvrhm4X06oHzHYZKUwyKDsvOwAc4Se7a3S48TqsUBmY8_dQSM4M0lLq8zSLC0wpDtKp7K4aP4I_yhKBsVcaleqgyMGcu54OmO6EHNN-f2GPLnL5l6xTiypM14F1_xTn_MB2zJAUArlwBuJG6ozNlFZhf4lz73bf1fPkY_PGpWyufKcMh5GVf7fD6MI-VzV3xQZ_hEKObqG9OamOro2CvGu4iIekqeHXw4JuwGampDt34yPbUvwx5U1IowCVBVpSxEA_L5ihYO03g7jwFTXpoOcae4doZ2AlJihA-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">8 آگوست تلخ ترین روز تقویمی لیونل مسی بوده..
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/103079" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
از ال‌موندو: زوبیمندی ستاره آرسنال یکی از گزینه‌های پیشنهاد شده به رئال‌مادرید پس از عدم‌موفقیت در جذب رودری است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/103078" target="_blank">📅 18:04 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d44f31c73c.mp4?token=JqltQz-_Hbdc3gNNsXdSiPURqDccbOSGcwl3Y05I5IfmEuIU5RCVcMJDN3-wH89VZzJWMBk4kvC_lRwz3YLDPtTEou1PB2-QqYiZ6Ha45eYNXkjcBS0wE_YXZtcHHZPFtqjuZYGvzmy5ePuwKXJ4X4L92Pyzgt1vEPRE8WgKLQ-yDugyrPOpE9XPO-CQiTbvthS9xeAJKyhf5la0XXfQR8qfW2QNkhaIbikilGa--aj9XKn_UI2DsNJTsIuUQwf_KTjzrcbBcJ0XjSeoC8MyipZHP_EshDok_nqwml390lXCQl1C2-UeLyaPN8OXnNSWRRAbyC_OP8Re-AoszLxOyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d44f31c73c.mp4?token=JqltQz-_Hbdc3gNNsXdSiPURqDccbOSGcwl3Y05I5IfmEuIU5RCVcMJDN3-wH89VZzJWMBk4kvC_lRwz3YLDPtTEou1PB2-QqYiZ6Ha45eYNXkjcBS0wE_YXZtcHHZPFtqjuZYGvzmy5ePuwKXJ4X4L92Pyzgt1vEPRE8WgKLQ-yDugyrPOpE9XPO-CQiTbvthS9xeAJKyhf5la0XXfQR8qfW2QNkhaIbikilGa--aj9XKn_UI2DsNJTsIuUQwf_KTjzrcbBcJ0XjSeoC8MyipZHP_EshDok_nqwml390lXCQl1C2-UeLyaPN8OXnNSWRRAbyC_OP8Re-AoszLxOyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
ویدیو وایرال شده از مصاحبه چهار سال پیش رامین رضاییان در برنامه فوتبال‌برتر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/103077" target="_blank">📅 17:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b851903a5.mp4?token=vGaDj2Zi8Kpqfb14xmohK9dM9bPt3vEwoLNXLViefUJCDRSI0r1mWF4KIJYVOzySgQSc3nNLgTgYDF_qZbe_Q1F_CzJfA9HeUOEJMeVLzTywLzR-hSqdxxl6yRQH6tyGNXFLscg341oZpXPtve2TDMs4DtoOiyMvYwbLAM3qA5ixs0n5x5oYNwJ8-5eA6LJ3vqiyeGFRfGSAR1OXXXjXKlztAswy6UxdCoDYhASk41LbJ-kiWpmfECNG5aR0C48T3CdQs2XnN6zRDw9kg6Xk_eCZw-5HZw95CmWYy0UT7IX1Qmd7OSEYUFusjZtPxlndlLYv6J-paTr9e9d8377DTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b851903a5.mp4?token=vGaDj2Zi8Kpqfb14xmohK9dM9bPt3vEwoLNXLViefUJCDRSI0r1mWF4KIJYVOzySgQSc3nNLgTgYDF_qZbe_Q1F_CzJfA9HeUOEJMeVLzTywLzR-hSqdxxl6yRQH6tyGNXFLscg341oZpXPtve2TDMs4DtoOiyMvYwbLAM3qA5ixs0n5x5oYNwJ8-5eA6LJ3vqiyeGFRfGSAR1OXXXjXKlztAswy6UxdCoDYhASk41LbJ-kiWpmfECNG5aR0C48T3CdQs2XnN6zRDw9kg6Xk_eCZw-5HZw95CmWYy0UT7IX1Qmd7OSEYUFusjZtPxlndlLYv6J-paTr9e9d8377DTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
🔥
آهنگ خاطره انگیز:
Savoir Adore - Dreamers / PES 2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/103076" target="_blank">📅 17:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsuj25SzA-uSfBwdVcSAe0rfp1g-hJSS-ckQbQvRxXdIsGbLE4zW402Vvwl_vpQeUPW0S-ZFG6gcLNNwIIHkLkzXGo1XQzPg8DTqwqQBIoe9YgHXaojai-eMcPNLKDLNJQaDsamH3qv7SeVv4e4mT3-I1QcDIz7pg1Za_YCMyUxV_0oH2cIT670ujWME0bzKye1nIJzaYUxhIXgLAQtgkllnuqfx2PkEWpmC_zNydtxxE0egg-BMG9vED66qNynGBRuyz7XmPPrnXHYsd_MoRaZyZENe4QFgxF_MygqfM0P4dUs2kj1-aYdlNwdjgW4Ns5c48nAM2zb7qqdYBH0Ihga1tc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d1230c317.mp4?token=QhFI4tCRXlG9Esh8185-9bbThqG7w51qh8V3AP7kzCjNzDN0rIJmrwCEA0Lhr2rmcAPJ6Nv7tkyuRME0lSUYW4MXxc4G8J9_sLi3pyAyZQWF5wE-joOd3EHPRHJRHW9HPLWKPL1z_mq-VYdZ8bvqh8XuadRNrBhxMiVGSykK-rzCDvKsEJrLQPQLAzFcNGaLSQX_Di61DiuyU2Vy407cwK_sKhDiYvbHjClvkFbImgd9s5ndBJ7CdhOhSQXa8LtRpBRvrp39QIsPI9BdL7uGKgMxT7UfFzrqV2rt2u1Rtnbdl4nLFjqqFVVdOIh_ILMffFatm1A0eYVd9VWU2vsuj25SzA-uSfBwdVcSAe0rfp1g-hJSS-ckQbQvRxXdIsGbLE4zW402Vvwl_vpQeUPW0S-ZFG6gcLNNwIIHkLkzXGo1XQzPg8DTqwqQBIoe9YgHXaojai-eMcPNLKDLNJQaDsamH3qv7SeVv4e4mT3-I1QcDIz7pg1Za_YCMyUxV_0oH2cIT670ujWME0bzKye1nIJzaYUxhIXgLAQtgkllnuqfx2PkEWpmC_zNydtxxE0egg-BMG9vED66qNynGBRuyz7XmPPrnXHYsd_MoRaZyZENe4QFgxF_MygqfM0P4dUs2kj1-aYdlNwdjgW4Ns5c48nAM2zb7qqdYBH0Ihga1tc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
تمرینات میلان 2002/03
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/103075" target="_blank">📅 16:55 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5i7t0fjUxPE9LtIi-fP_EObH1Z12caCKFAaI1xY1FHObBh7BS9s610el7AGrjvvkdU1xHBC66usqxf1iJPPG8ggsi4MQE3FhY8XQS2vNBl8dT7jLdV3OxSH8FXt6I45CmTy90Gwt-bsqPmJGWThHWXQ5GZ91wfgF3C4-e6jg0HZLQ5UPbz2RT4A5l-ulJCsLaqlx5LfZWV1_iJmSzNlXih2z_dlE7a69MSPVlrbGisFNFCB82Ca4N44Xo5bJn5os1_6fPCMW5CTNxpvcA7kUNo2MYBOs1Vm22Wz1jhpXyd5bQCQ8buC3pu2QaeOBVOhgqntGCKVPYzbjksmO1Fs4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فورییییییی از ویکتور ناوارو: بارسلونا در حال بررسی شرایط جذب لاپورت به جای آرائوخو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/103074" target="_blank">📅 16:46 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=MdoZCPuFxWcuN7iU62ctahZTQhAotkVtuLyGrJI9bcP5SPipwMeegni4VbOXY80S8MsQEJZqcNKCfQFd5f1fHwpTT4yaf29xTjovhf8FO28IMqpa2VDUdr_wtprM7AvqYy7FkTqyQ7OfiseoTFC0ifZSHdsGMwtovlGOfMbaWNIC_7M8dRHFb0a4CkDa5Ne3W5OtdDZvE1iYjbD933fnYhJ-qpTd5bXyNwEEshGw_XPqh10WUiNPn4RICVwiV3upyWReI-a6kQ0yn2SSuD8ox8D0kHW9HyM5hcz9zm8dY4t4Vpxe7GN-Psvkru_HvXijwoKNA9RoCMsfjTZK05lcbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8cc1a076c.mp4?token=MdoZCPuFxWcuN7iU62ctahZTQhAotkVtuLyGrJI9bcP5SPipwMeegni4VbOXY80S8MsQEJZqcNKCfQFd5f1fHwpTT4yaf29xTjovhf8FO28IMqpa2VDUdr_wtprM7AvqYy7FkTqyQ7OfiseoTFC0ifZSHdsGMwtovlGOfMbaWNIC_7M8dRHFb0a4CkDa5Ne3W5OtdDZvE1iYjbD933fnYhJ-qpTd5bXyNwEEshGw_XPqh10WUiNPn4RICVwiV3upyWReI-a6kQ0yn2SSuD8ox8D0kHW9HyM5hcz9zm8dY4t4Vpxe7GN-Psvkru_HvXijwoKNA9RoCMsfjTZK05lcbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت عجیب بهروز رهبری‌فرد از قمه‌کشی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/103073" target="_blank">📅 16:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=ExwFDH2G1eg4o2IbQ8eE0V96T6mD2BCWUFaEOgjodrd2VLomrVfdZX8-12v6JBrzVqRwNoS4Swfnknk6skucUpqlMUJJUYdR7XLpG0mJ4NIhYGCQlXq5Fxi2Z3zEQj-9BODWp_uV16g2AF88_6OO1KXyKJFHJL1_8BhN6Gg1esxX-FDytNPVWHFCc7k_gnaolQ1VJg-zrb78NvDzr9ltUcn6_XAwMEuVQ9u4dB_z0L75WXL6o8KpBW5d194-HVyLDDQsp1OK-0GMYIhwYR9qtmFE61pPYDSL_AsSaB5fbOQtvBphyQhAk-Liq1wD6hLY8dIg2hX_UkM32ZC3Sm8nSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e632b28ac1.mp4?token=ExwFDH2G1eg4o2IbQ8eE0V96T6mD2BCWUFaEOgjodrd2VLomrVfdZX8-12v6JBrzVqRwNoS4Swfnknk6skucUpqlMUJJUYdR7XLpG0mJ4NIhYGCQlXq5Fxi2Z3zEQj-9BODWp_uV16g2AF88_6OO1KXyKJFHJL1_8BhN6Gg1esxX-FDytNPVWHFCc7k_gnaolQ1VJg-zrb78NvDzr9ltUcn6_XAwMEuVQ9u4dB_z0L75WXL6o8KpBW5d194-HVyLDDQsp1OK-0GMYIhwYR9qtmFE61pPYDSL_AsSaB5fbOQtvBphyQhAk-Liq1wD6hLY8dIg2hX_UkM32ZC3Sm8nSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
این کلیپ رو چندبار ببینید و برای آدمایی که تو طبیعت همه چیز رو می‌کَنن و میخورن بفرستید تا بدونن یه قارچ چقدر راحت می‌تونه آدم بکشه! اونم مرگ با درد زیاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103072" target="_blank">📅 16:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103071">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=Sr1-A0_RCzzQdTRwaYtA0BvheH0H06lRwhAoV1MV5bTaxDVUx7xgxyXk8JApnWWBW5gP0i0PAu2MU6M0Hf3Eja0Qqzj8jM3pxwxqG3o4tN4FqEgkbXaq__f5D1LgAZjXSHW33tanQZDR78_4hGHShh4uAIe6nt1pxf-RKEnDtq9lMcVj2FFDoNU-g5F79mn5dB38aEuQpyfIoA71tbtJdqH0f6PQwSl8xOziny6gZdVU2tgSlRa5JzqLFnpw1ar7cywquVt_fGedFjPZF8lb1L8RL_BWHlInJsmgAfuVJatbrsJF18f_jccLjqRxFl19sW-o-pOA2LvfbqFmp77bBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf9b4001ac.mp4?token=Sr1-A0_RCzzQdTRwaYtA0BvheH0H06lRwhAoV1MV5bTaxDVUx7xgxyXk8JApnWWBW5gP0i0PAu2MU6M0Hf3Eja0Qqzj8jM3pxwxqG3o4tN4FqEgkbXaq__f5D1LgAZjXSHW33tanQZDR78_4hGHShh4uAIe6nt1pxf-RKEnDtq9lMcVj2FFDoNU-g5F79mn5dB38aEuQpyfIoA71tbtJdqH0f6PQwSl8xOziny6gZdVU2tgSlRa5JzqLFnpw1ar7cywquVt_fGedFjPZF8lb1L8RL_BWHlInJsmgAfuVJatbrsJF18f_jccLjqRxFl19sW-o-pOA2LvfbqFmp77bBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
روایت‌جالب‌پپ‌از معرفی نیمار به بازیکنان بارسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103071" target="_blank">📅 15:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103070">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be22201896.mp4?token=t2I2jOIsvAva-Bvr65iDtmyh12j743Mf8nm3GJTRlMyqUO2WcZOLZNtnzqbK8fjPxhelobz2YO7RMxuepham7j2qafvALnVnpjjbP2rOwCGxbb5pwFG5aKqkPqychJh0ZlgbcEKieVU-cn92sZ0TDk8EIjTY2P0XInsNja_UWQyi-K82WvXqd1v7lMuCEPcgTelaS1yr4GQC5GwOcokWzrB98qlWWANyuygRBF8qYIqLJyQndvctrevqHpDwecoR0tIEtzGTwXCJFQRLvwqY2UWQuTgKUDq-Ro--Kc3RZYOSZLvQDnG1cmGyvZYpVBbRE8fHdhKhH4P2TiOx4lMCJDAgNOcCVKXL_DtvHptczIyxrxxhnxgqz1AxJzrB_t-6WHaa-_9jGIiOTtvxjSUGi2E_0-GuoHASLqOy99HXs_JxXlzHC8xho0nkrSOHEl8w8j6C1Cc4sj8T_9kBxpadWN23JvCu5wrJ1HBRvktTjs9QvuTUd5shqYzIgkVWg0OF5TbuZZtVHsqJt_FLBLhKOq5CKNKx59tuznPSvV4kBU8QGqe3DofvEGjljIGp_pMfGo6dNk6ZsDhjzZKVvd2YQlMEku93srq8PZ4WaJjBCJjjvobR5kSDF5OdsVOU2v0fAHp4cIBZxbHHaln5-J6ClW3cqllFYDQo36ZEcB0IuFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be22201896.mp4?token=t2I2jOIsvAva-Bvr65iDtmyh12j743Mf8nm3GJTRlMyqUO2WcZOLZNtnzqbK8fjPxhelobz2YO7RMxuepham7j2qafvALnVnpjjbP2rOwCGxbb5pwFG5aKqkPqychJh0ZlgbcEKieVU-cn92sZ0TDk8EIjTY2P0XInsNja_UWQyi-K82WvXqd1v7lMuCEPcgTelaS1yr4GQC5GwOcokWzrB98qlWWANyuygRBF8qYIqLJyQndvctrevqHpDwecoR0tIEtzGTwXCJFQRLvwqY2UWQuTgKUDq-Ro--Kc3RZYOSZLvQDnG1cmGyvZYpVBbRE8fHdhKhH4P2TiOx4lMCJDAgNOcCVKXL_DtvHptczIyxrxxhnxgqz1AxJzrB_t-6WHaa-_9jGIiOTtvxjSUGi2E_0-GuoHASLqOy99HXs_JxXlzHC8xho0nkrSOHEl8w8j6C1Cc4sj8T_9kBxpadWN23JvCu5wrJ1HBRvktTjs9QvuTUd5shqYzIgkVWg0OF5TbuZZtVHsqJt_FLBLhKOq5CKNKx59tuznPSvV4kBU8QGqe3DofvEGjljIGp_pMfGo6dNk6ZsDhjzZKVvd2YQlMEku93srq8PZ4WaJjBCJjjvobR5kSDF5OdsVOU2v0fAHp4cIBZxbHHaln5-J6ClW3cqllFYDQo36ZEcB0IuFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👍
روایت احساسی خوزه از ساعات پس از فینال UCL و قهرمانی با اینتر و تصمیم برای سرمربیگری رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/103070" target="_blank">📅 15:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103069">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=fOt1LAzhtzKYWoK5vkS-Rw3jiRbcNQYqW0mAzSI_s_XZlJVUqfDPkolH60Z89bkn6XHV1nbhumE8fuY7fBy2eUGU8juGjKILrOJ6tT9hhn94lNfSEDbcyLhczij30dEE9OwMi_MOfNSR8iOTuxUU5fujVOEq0QDKC7Ri65OVFkJSyZH4IJs5i9p0VV_zkCz7A6zMKArpSF4TssjEQHCvLcRTP3viExziIcyq9L_2bYffAr0-4ZBEfxdIIf-2d9uHf1qdFs88Haw3pIEyYvp-9BUrThN0GGluAJRfWpfh8uLtkBkCaJ9-knle2V9zpks4VAfJQn_hr9r10d8qFJVymA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/772fba48c6.mp4?token=fOt1LAzhtzKYWoK5vkS-Rw3jiRbcNQYqW0mAzSI_s_XZlJVUqfDPkolH60Z89bkn6XHV1nbhumE8fuY7fBy2eUGU8juGjKILrOJ6tT9hhn94lNfSEDbcyLhczij30dEE9OwMi_MOfNSR8iOTuxUU5fujVOEq0QDKC7Ri65OVFkJSyZH4IJs5i9p0VV_zkCz7A6zMKArpSF4TssjEQHCvLcRTP3viExziIcyq9L_2bYffAr0-4ZBEfxdIIf-2d9uHf1qdFs88Haw3pIEyYvp-9BUrThN0GGluAJRfWpfh8uLtkBkCaJ9-knle2V9zpks4VAfJQn_hr9r10d8qFJVymA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فکر کنید چقدرضربه محکم بود که یارو با این هیکل پهن شد کف زمین
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/103069" target="_blank">📅 14:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103068">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmXQL6se3NEukU3Fb7st_GDBLR86_zsNqod_x8mVKRmuxglCMZF2n8C1pZaOX6V2TFjPh2DGu8Qd4Nrg00sG_kMrdUXcFbReiQg8rbbW9nlM29D94oX_2L9lxknJmLXiPeXEOwDsAfBHzq8XCYM4ItPpI3MrXXwSX_rVjwvWH1NZ9HXecg1A8GIZ15bWGPrbQTXf-KJ1h8cMq_ZCH9XtwHgaUvpPmdHzevVSIy6ZUdwRVw_SWx0I7q1tACc0_4x5vo-0EWU0KPqbmKfyThsH3ByL12aw1WRM13DQU3D1-rQROV1T8L_YUXeKSjg0e_u0VH3U-lWUebJZp1NYWGEyJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
نگاهی به آمار گلزنی لئو مسی در بارسا به مناسبت پنجمین سالروز خداحافظی او از جمع کاتالان‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103068" target="_blank">📅 14:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103067">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcCIJbIgW4KmPtu3ojVGK96r_8wwqMEEbyiaHkwnAVwnjZoNGKdDyX0ovArZHdHebMjDG9HmAtZNmePhiqfMG9NROXb33bvTI_kC3UAb5CJ_JkH9I4LGtADvOcWvA7GFKd_4hKGYYdnzLBvAUhQYQNW2QtNE2TUux3nAXMytuaNtApayhTN-i8ff_ktQqG_gJc6t3WctIGb459xbdGPX4VSEOcuL-pySV1qnqbp9qWEAuiXiGp4CFjDqUJtw5jDIHiSmXQueVhdFQdN0OXk7UweGetyOPXd4SHw5234TKI1vsp2wkE7TV2eiTfkY12BbLnxEyRDPVjC6CUy2QltTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خورخه مسی، پدر لیونل مسی درگذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/103067" target="_blank">📅 14:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=l--T2GIfXSPCZfcizOIJH9JRvg7sQixRza0Ees5Q_b65yPIZcLUIiG2vvFdutafgl9OXMUNQJyJoNaoJ4DF_ML-ijTw1ZvQrnhIl-hWYYfBXI4SWv99PEumkPcfuMLmcibxANC6CdrOTN31PIo6CofNs9MB7LlPTRnJ6xLOty5U9vz1G6uCs90VuAuOTjOy2sMiDVHIm-cy3iDNTWlhyy_q8CJ1mJ-lSg0HjSCtsqesFdX2FTw3Nod4x-XzHtSgKxZxUVL1bsEvEkfS1uUju0i21RGzL5pXTgV6IJVNVydSR_ZT3W6RTr31K6NF8xSqpwBxu8V4CdV8uwQ8gl5aESg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bc67d9626.mp4?token=l--T2GIfXSPCZfcizOIJH9JRvg7sQixRza0Ees5Q_b65yPIZcLUIiG2vvFdutafgl9OXMUNQJyJoNaoJ4DF_ML-ijTw1ZvQrnhIl-hWYYfBXI4SWv99PEumkPcfuMLmcibxANC6CdrOTN31PIo6CofNs9MB7LlPTRnJ6xLOty5U9vz1G6uCs90VuAuOTjOy2sMiDVHIm-cy3iDNTWlhyy_q8CJ1mJ-lSg0HjSCtsqesFdX2FTw3Nod4x-XzHtSgKxZxUVL1bsEvEkfS1uUju0i21RGzL5pXTgV6IJVNVydSR_ZT3W6RTr31K6NF8xSqpwBxu8V4CdV8uwQ8gl5aESg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😢
سطح‌تمرینات تیم‌های باشگاهی آفریقا رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103066" target="_blank">📅 14:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DhP_SA-6wZvR6M1otmOBzueWHbP8cHKtvAr8gePhWc1iR08rh-myDLETh8bTjLjrvcVv62XxOg9CqdYBR7k525QmqtBQ1eEJcvD-_oM5BzUyy4Q1mL1Y25Tt9iJd7qz-kJH96WLbyfSlOPF4wIIyariCjHsTMkwlemmRMUL83KwHyzOfLvYEopjwJXf-woxZjjlb7WcR2xoegKPohRrVNG7FQvn__zCKo4ak7ED61ouz00qkVpaTPeDyM89mzJU7gvJzQwgA_2PhzMulRfspjtFvTcfEOGbKVXJFq6IvA6BqWaW-gNiyMj2sgnd1MoQVC2FWFaWbOq1pTPGH531CBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇪🇸
🇹🇷
علی‌ناجی خبرنگار ترکیه‌ای: پیشنهاد ۱۲۰ میلیون یورویی اتلتیکومادرید برای جذب ویکتور اوسیمن توسط گالاتاسرای رد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103065" target="_blank">📅 13:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103064">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/103064" target="_blank">📅 13:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103063">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=Rxjri4SIfz0h1EMLz1pwuyO5pbaFAkxdYZDPvRhcsG7N9xxOz_eEcg43lNvCtu2E_9S_mTA970PULXRnc6NCz4k6e-fwq0rPr5N5xPAk53raU8vMTyNpx5sF6PbcwnI0m9BHCgb9T0pSD6hYEY4AdYzPnqE0uy8VBblYFf8jg1U3rDNxUSaOyEDg_smfwFchZVfXY1MIKVwwWVPHFOiWy66FxaM79gmWZTB2In80T5BNx6UqeJib-qtFl-GxguO42xPYvlP2lgT47OnRK4dgmKxStLwE_4RRXf8nZGKhmNGkwkfmUxCNzt2ZvcsTv5Y53lhrhxMtFVhgEEicWylP1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e15d33bd4.mp4?token=Rxjri4SIfz0h1EMLz1pwuyO5pbaFAkxdYZDPvRhcsG7N9xxOz_eEcg43lNvCtu2E_9S_mTA970PULXRnc6NCz4k6e-fwq0rPr5N5xPAk53raU8vMTyNpx5sF6PbcwnI0m9BHCgb9T0pSD6hYEY4AdYzPnqE0uy8VBblYFf8jg1U3rDNxUSaOyEDg_smfwFchZVfXY1MIKVwwWVPHFOiWy66FxaM79gmWZTB2In80T5BNx6UqeJib-qtFl-GxguO42xPYvlP2lgT47OnRK4dgmKxStLwE_4RRXf8nZGKhmNGkwkfmUxCNzt2ZvcsTv5Y53lhrhxMtFVhgEEicWylP1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😃
یامال این‌روزها تو کلمبیا نقش دیجی‌ بازی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103063" target="_blank">📅 13:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103062">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDKmJFAIHqReYH6iMdRFvmp5VtmsVcLplRk9jFxCJprW4a1IzyoLNdIPiOp8IbLNefQzJiB773tvDc4Yw1DBjbrYl41c28cPtkquiw8px7UW1rhzJIqmzk6XnsB1DBH_KLqf4H47rIKN_irUQhb5nJLw0PWj56SYpuOApgZ-Nk6BLtOy-qiMJ9Rz6Ao5AUuWsKUNI_9QdyW1WyLUGnSeTSNPcD7D5rBvjl1znrI9p4S_c3qQbIHAktNb6pOm4p0CoR3ESkBa5VlTEkk3GXct4fPHcCZsIDsBd2Xq9Y_7HdHZCQRqAzH8EskyZspXR6NyEyjEbmJ9pfiOAAfLFLdZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📰
افشاگری‌عجیب فرهیختگان: موسی جنپو فصل‌گذشته به ازای هرماه حدود ۱۴۰ هزار یورو از استقلال دستمزد می‌گرفته که در تیم جدیدش در یونان این رقم به ۲۰ هزار یورو در ماه میرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/103062" target="_blank">📅 13:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103061">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iPmSS-iK1q41szkhuA0ODsDd8_uJTLwe5M0XQDqz0qZd1gZjJz1_RWsxTZEOEuB_3YMZlz1rAy-8aPZLVH9eQzu2YVnvxdqoUhHMWysMMH65s_aigCGNvn1xJ9YwYDMUvi56sBwfF9hekmYm19gFULdfPFGrb1Zc9QC4SFrqZHMvta6emhUC1GH67-pLB7Ae-5XVRwFUw37QGy9XCDy30qX2SG9yCgCka__qlZ31HmHuWn1fc77NEfQlPU9OjBJHUeCIFDKdMw9v2BXnBk77W7X0kHLpGR0d4SoWyENq0ec_BzpySo9EJ2E8NnE4ztIKStDkXiekelcDAjJ1H3Bkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
🤯
#فوووووری
و پشم‌ریزون از مارکا: توطئه‌ای برای ترور لیونل مسی در جریان جام جهانی فاش شده
😐
🇺🇸
طبق گزارش پلیس آمریکا، لیونل مسی بازیکنی بوده که در طول جام جهانی ۲۰۲۶ بیشترین تهدیدها علیه او مطرح شده؛ از جمله یک تهدید ادعایی درباره حمله انتحاری.
❗️
پیش از دیدار آرژانتین مقابل اردن در مرحله گروهی، ظاهرا فردی با فرودگاه دالاس تماس گرفته و تهدید کرده که به همراه دو نفر دیگر، با سلاح و مواد منفجره دست‌ساز وارد ورزشگاه خواهد شد و مشخصا مسی را هدف قرار خواهد داد.
⚠️
تهدیدهای مشابهی پیش از دیدار آرژانتین مقابل مصر در مرحله یک‌هشتم نهایی نیز مطرح شد. پلیس همچنین یک تهدید بمب‌گذاری جداگانه دریافت کرد که در آن ادعا شده بود مواد منفجره داخل سطل‌های زباله ورزشگاه کار گذاشته شده است. نیروهای امنیتی با کمک سگ‌های مواد منفجره ورزشگاه را جست‌وجو کردند، اما هیچ بمبی پیدا نشد و مشخص شد این تهدید نیز کاذب بوده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/103061" target="_blank">📅 12:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNSRvwjAHxKcShsDUApb3DZF03GaFYSNumSIrkJHHty01Fb2gbZ1ZWY__naBSMg7SJXL59HNUEy3mW1kXCCmOyYUnzxiBieAsr4VeIbk4Gk5NXB6ueV4gj--aitsK7RM7gOdFx0GwpwF7mMS2O3tHzzKd9esSM64qwJoLpn5o6-3DuKVWjlFFwqZE_XHVnDOB87-vanCTDcQrKc-2vThRhkkvY8ZdBoeJUqIUak26rCc6LCRsjR0LvTg_uepdsBuZ4rLFa_spPFoR5EBK5wF8C9Gi-1Nnl8fjLgaMPjC4hMCKm4_qZGL0OraxpVAtprzGOb1xjHEX5zwZ6BAs_rsPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
از لوئیس روخو :
✅
فران تورس پاریس سن‌ژرمن را انتخاب کرد
🔼
مدیر برنامه‌های او این تصمیم را به اطلاع باشگاه بارسلونا رسانده
🤝
هم‌اکنون مذاکرات میان دو باشگاه در جریان بوده و تا نهایی شدن توافق فاصله‌ای باقی نمانده
💸
پاریس سن‌ژرمن مبلغی در حدود ۵۰ میلیون یورو پرداخت خواهد کرد
🇫🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/103059" target="_blank">📅 12:32 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pU_aoUenKQAp-koAq7CZhshJknqWmh1K53fnlZ7zXgTTYH6RcmksHWwowNc4X6W-5O6T9ZxWILlzZtph8DKzxfCQE3zwFvdaDE9Df3jA0c4sJT8ZNCn_gi7hHn5zNFAB9XiKKsvUgkx4H6cCGDdP4Kx9W7XB0HIJWllp-DbgorIpRynJHhAyk9LLKIncWq04Sy4H0kKoAlOyNYBmHSccCbHdIckMyi6dj7GONpJwNVF_I1YWEjYOBcEd9HXjOGHqLlJgSkWRy8lgySCR2mPv2OhNoaFj-Mw0zKll6Y2avs0lBRF4tNOiu8wRG--rSScfJEu-wf9tvRAoBYwq5QQobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری
دیه‌گو سیمئونه :
🔻
وضعیت کاملاً روشنه. باشگاه تصمیمی گرفته که میگل آنخل اون رو خیلی خوب توضیح داده. از نظر ورزشی ما از داشتن بازیکنی مثل جولیان بسیار خرسندیم و بهش کمک می‌کنیم تا به رشد و پیشرفت خودش ادامه بده.
🔻
قبلاً هم شرایط مشابهی رو تجربه کردیم و دیدیم که چه اتفاقی برای گریزمان افتاد. از نظر ورزشی هیچ راه دیگه‌ای جز ادامه کار نمی‌بینم؛ این وظیفه‌ایه که نقشمون به ما دیکته می‌کنه و تمام تلاشمون رو می‌کنیم تا مثل دو سال گذشته بهش کمک کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/103058" target="_blank">📅 12:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCIFRoxnjyRycF4DHGmn90YIliMBx3hGpylHuTOVygQJB2MMn7VLhjmIN5fHVyrigINYhDUKKF3EAx-ulEFsTVDc5rSB6765-fX2CUyvz_ZCvCNsLlTNvJ2igKGl_o1807MF-_X-gl71nrSyITWy0W1QTgpoXziEBSEJ-7IxKsXbeZPcJqTyc8xUNUooxdF7c4MR6e6u1ZA5sJjURVNInQCYl1YVhCNcCLos8rsfxOQP2IaKW-ReT2wmas7clnzzbN-LmE4LQdzORfbGUI1TMCqFCr__1oqcsqH8fnGjtzuvyu0Q6bd4oKt5avsW2BsVMwJMVIRG0QdYXpGLzsKRcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماتئو مورتو:
الهلال برای جذب کاسادو با بارسلونا تماس گرفت.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/103057" target="_blank">📅 12:08 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trbSM0LsKvQVygQuU8D5uv6sksdN5uOINwwwbexb84vSH8TD4R0XVjX6WG7qqW9sPjl4pIwzePwAEHe7DHZsY8PWgIInRFQnJBGWWJDtZhduiUbu35jLE4j6-j_T2mp2DFd1lkgDH1BGdiBBS9jfVu75Tj17mJ6Wn34oPwn6k0yTllBQdjXPfTi_XgeC2Np0jP3LIt94TdmCd_dsO4GxBjz2Uld05JnfTzIfjp215dcrVEzEn3-geICgvjXTbFv5miatCGxgkfvpTQ0PpORY-Jw9GYvrwO7SVvs5reHK-I2ZQVBivXltUDye-ET_1APaa1jCXd9Ls7rZvv-cy7cVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇫🇷
لیست PSG برای بازی با منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/103056" target="_blank">📅 11:53 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgV5gkUHy7b2-aRgUY7O1WHxtuzBLy5bBqbPESGwYx4jS0farjQxitBWa_2yw_8KJayjnwYVXiVwKIN8kczpLKEiWQnj2AADcF1-V_q9y9x8_s4Nzl1ebkA4cAmMvf8WtDTOWXEfJsspbHZCRdLv1xdci9RddB0ZwMMH_KsmhpC4UO84STTcFf8-7b8v53mOLghAXhdSKpD219gZ5WUqJeWB6ecn696eTAlE2QGvBVDabRIuGpYVfmERHVnk-FUQnP7h-N_8hrUp37BwXwpJZydvXDyTBwGWiFWsj9Izh1M6XRayM89u5h4Gc3aPSKRJSxhe4mTVezVdw9YwEIhG3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇪🇸
بارسلونا روز ۱۶ آگوست در سومین بازی دوستانه پیش‌فصل به مصاف بازل سوئیس میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/103055" target="_blank">📅 11:41 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103054">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ff922b433.mp4?token=viJh8LbH-kxGbfGJ8-OHBNsuIfZjqISzAb7gdED9EYwnAO4nOZEKiB5-DTFf3uEcrKk3RhK9ByYAj0FcGmSAOf3r0_yfXDyoIgaAVjO0_bdNs9jW-cRZ4Dk-Q6WJ-Cue3q0itJjJ8qvMYbCduuxjwBUCadLK1Y6IsnwE5366fOcwO26eqWJwW6nCkDcKFCQR44kzvia6Xs9msHlcbm7WMJksv1TP_Xaw_d7ErFWWF8X7jXcRE1bZ88Pj5vysSu9GKYoPJNplg5qWTdc5iRtftO1wox4gJjKPEduEOTY7hGZQxTYkYcm8wxnB_gpcLlHKVBvhRZy1ZpBoYo7CBker2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ff922b433.mp4?token=viJh8LbH-kxGbfGJ8-OHBNsuIfZjqISzAb7gdED9EYwnAO4nOZEKiB5-DTFf3uEcrKk3RhK9ByYAj0FcGmSAOf3r0_yfXDyoIgaAVjO0_bdNs9jW-cRZ4Dk-Q6WJ-Cue3q0itJjJ8qvMYbCduuxjwBUCadLK1Y6IsnwE5366fOcwO26eqWJwW6nCkDcKFCQR44kzvia6Xs9msHlcbm7WMJksv1TP_Xaw_d7ErFWWF8X7jXcRE1bZ88Pj5vysSu9GKYoPJNplg5qWTdc5iRtftO1wox4gJjKPEduEOTY7hGZQxTYkYcm8wxnB_gpcLlHKVBvhRZy1ZpBoYo7CBker2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواداران ترابوزان‌اسپور ترکیه درحال یادگیری زبان عربی بعد حضور محمد صلاح در تیمشون
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/103054" target="_blank">📅 11:33 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103053">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0d7174722.mp4?token=fWKbCIU7d0vTpKKQjP5WirpHBeVexBN3g7lD5np78VWcDeQGltiLfhbzTLB0yvDAhex8iBLvncmsrIyjJekLJnDtlJFI0o-WpdZFl6HEX88hozL-1hWDy-1xe7O5EEc6SKxVmlGuf2SgjDA3sVeoDNrrJEziMkZh5CDrcVeOSUgE2gpnTl6sDd7OOEsZgdOm4geDf_Ki3kPcbdEHSYYI22mrNPa28jDJpeKl7QJ_jaR5ZUk97UwBdLq0fX5sHsyQdsD8RGr_rGKa_7jUkp_AAuSD05g5WhJjGZZWDa6flKFH_c9zCPF8NtZRss22343aBjoxSbdmRkkp2LoQgumiLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0d7174722.mp4?token=fWKbCIU7d0vTpKKQjP5WirpHBeVexBN3g7lD5np78VWcDeQGltiLfhbzTLB0yvDAhex8iBLvncmsrIyjJekLJnDtlJFI0o-WpdZFl6HEX88hozL-1hWDy-1xe7O5EEc6SKxVmlGuf2SgjDA3sVeoDNrrJEziMkZh5CDrcVeOSUgE2gpnTl6sDd7OOEsZgdOm4geDf_Ki3kPcbdEHSYYI22mrNPa28jDJpeKl7QJ_jaR5ZUk97UwBdLq0fX5sHsyQdsD8RGr_rGKa_7jUkp_AAuSD05g5WhJjGZZWDa6flKFH_c9zCPF8NtZRss22343aBjoxSbdmRkkp2LoQgumiLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
از عجایب مملکت؛ امام جمعه ماکو رو بردن که سالن آرایش زنونه رو افتتاح کنه
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/103053" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/Futball180TV/103052" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/103052" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=E95VDFrHxQI3Z9pZCriAtqOgn86sTmc9M3laec1Ml_6UJkFqxwb5ZDMNftRucd2uNksWEO4Td9JlNfIJlhMP9saRJjtyJ8Jjo6Rwhte2pHD-s0uB69lNZaYSNGTHiK6T9yf2GOM5b7MKvbqP3_THbpO7c5mmN8LKIDJ0_HgdinqEepS7JSTOBl6qM1uDbjOGcpZkNSjXgkZMmSkypN9KsxOD3Csf_iB59xHV_ZlivlIo8VEk3JlTwBwednRtKf7wauq9gDQcxz3C-OOmbC3voKSdyxaV1rgD-1NuzoFgTOHG69WdYtV5ARC5AHBmWa38DcbngrqUJ5KZOI_AjlMheg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7f1c8ee4.mp4?token=E95VDFrHxQI3Z9pZCriAtqOgn86sTmc9M3laec1Ml_6UJkFqxwb5ZDMNftRucd2uNksWEO4Td9JlNfIJlhMP9saRJjtyJ8Jjo6Rwhte2pHD-s0uB69lNZaYSNGTHiK6T9yf2GOM5b7MKvbqP3_THbpO7c5mmN8LKIDJ0_HgdinqEepS7JSTOBl6qM1uDbjOGcpZkNSjXgkZMmSkypN9KsxOD3Csf_iB59xHV_ZlivlIo8VEk3JlTwBwednRtKf7wauq9gDQcxz3C-OOmbC3voKSdyxaV1rgD-1NuzoFgTOHG69WdYtV5ARC5AHBmWa38DcbngrqUJ5KZOI_AjlMheg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
اگر
#تندو
تیز هستی اینو ببین
💵
💰
✊
این بازی فقط سرعت عمل بالا میخواد
😍
🟢
ویدیو
#آموزش
بازی AVI رو براتون گذاشتم خیلی راحت با سرعت عمل بالا بدون ریسک کلی پول دراورد به همراه
🤩
🤩
% شارژ اضافی
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r17
@betinjabet</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/103051" target="_blank">📅 11:13 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f294785d1.mp4?token=O7nLSf_VFZLgyYCQFV4iCpHirDnWUNs-8cX-_qSMGHe8KfiTwUYFs1-OnJYZtb7EBQqy5AvGZjFR2FawXJ22wTtVZ48AxkaxJvZfo4RW3tJnm75hj-re0yy_nyPllH51KwbZ9ku1nD-O8GsPfywbiR1E3RgK3Q7TRJbl1oHPpKFgou-Vls9OY5sZ-w4Jbbue6m2r8c4DJN6CAZ3IhZfNAcGCP7_lulJ4rVsbUPOY789fUNKJr8sbEaRlvAve6NxCc-6XLh1Xrg5FG3T-VR7gqjtqDN7Mb_B5NTOEnxS2e-0_NGfr2YSDdzvimu0OLgGwVU7HiXshWcKx4_eox0otP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f294785d1.mp4?token=O7nLSf_VFZLgyYCQFV4iCpHirDnWUNs-8cX-_qSMGHe8KfiTwUYFs1-OnJYZtb7EBQqy5AvGZjFR2FawXJ22wTtVZ48AxkaxJvZfo4RW3tJnm75hj-re0yy_nyPllH51KwbZ9ku1nD-O8GsPfywbiR1E3RgK3Q7TRJbl1oHPpKFgou-Vls9OY5sZ-w4Jbbue6m2r8c4DJN6CAZ3IhZfNAcGCP7_lulJ4rVsbUPOY789fUNKJr8sbEaRlvAve6NxCc-6XLh1Xrg5FG3T-VR7gqjtqDN7Mb_B5NTOEnxS2e-0_NGfr2YSDdzvimu0OLgGwVU7HiXshWcKx4_eox0otP4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚽️
مثلث‌رویایی کریستال‌پالاس با حضور ازه، اولیسه و ماتتا که شکار تیم‌های بزرگ شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/103050" target="_blank">📅 11:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsB5b_fsz5ZdGgMfopNmEzNX426bDOFQ3ch3MJXR4OB-CKeXe1YCP6FKFS_coyeO2FHH8l-C0t7wNVXZouD5sKteQKu0vdRU5tq7HkNBI1VRCe6nnZWne1DQcmTB5_hcndoOrGX3Cm1OajN9fS2D_wTsPlGaDKfdozW_s4j2pcMCVuDweXGmPSxchZUnvnF1SvhDspNN5SIjsI9xX34Q_Zuyg6TVczxQP4y12RFu0stIudFQUIWECflVRQUTLJAyphBByMaVwT7mqMiy_-aWKk27qQytdOxpLJ6Iif79ZkF4OE4UdiNZ7uj-jSBVy-kEoSoYQxFPtgvM7Cri0a6j1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
تلگراف:
اینفانتینو که متاهله و 4 تا بچه هم داره در زمان تصدی پست دبیرکلی اتحادیه یوفا با یه زن کارمند یوفا ریختن رو هم و باهم رابطه داشتن! اینفانتینو هزینه‌های زندگی این زن رو پرداخت میکرده و کلی پول خرجش کرده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103049" target="_blank">📅 10:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3239f9b4b3.mp4?token=XZttmbKz32nPTBzBpm8ZhKQRSi1zy2mX1X1OV6uZAFqNE4qJ_pRE8MzN0tISX_8CvTp7WnGk5txpMauOxez2s4BQx_Vn_pzyIaFYQnI7ipW_ca82EAYYttI7o7FltI33mEzIMOYydj58LGpdu7_a10CV8hprHWVNY83_hcLslbOhlVKPXLB7CW5DgqrDDaVWKo20UWtk7fkcIw19dNO5Yw7hCnstEaciUbkfRsXMQmPQVFdN15msNb9ZCeZG3bnhOFzYclOWMkOiAlTDoiI3T0Bk_nOlPN37yaL2f7dPXiSuzcIe-wz2rp405ICvrcxB1LzZidJcJVg9btLVU5Y4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3239f9b4b3.mp4?token=XZttmbKz32nPTBzBpm8ZhKQRSi1zy2mX1X1OV6uZAFqNE4qJ_pRE8MzN0tISX_8CvTp7WnGk5txpMauOxez2s4BQx_Vn_pzyIaFYQnI7ipW_ca82EAYYttI7o7FltI33mEzIMOYydj58LGpdu7_a10CV8hprHWVNY83_hcLslbOhlVKPXLB7CW5DgqrDDaVWKo20UWtk7fkcIw19dNO5Yw7hCnstEaciUbkfRsXMQmPQVFdN15msNb9ZCeZG3bnhOFzYclOWMkOiAlTDoiI3T0Bk_nOlPN37yaL2f7dPXiSuzcIe-wz2rp405ICvrcxB1LzZidJcJVg9btLVU5Y4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه تعطیلی باشگاه و واکنش صاحب باشگاه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/103048" target="_blank">📅 10:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103047">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🙂
👀
واکنش جالب پادکستر هوادار محمد صلاح به انتقال او و پیوستن به ترابوزان اسپور
😄
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/103047" target="_blank">📅 10:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563a2467b.mp4?token=VnffEh1Cdag5yGg-eHoEIEI5ecGVXhHfEc-IJwv3kEu5r4kLTAohcUfyey4794xmwtuchXu-0SGlYpLp-kOekwgCXwouc28dhUc_jf_W3XdW9mYsebjq18WNpk_Wz5PZzYJBUG1DGCMPVPoUqUkMtF1CIfXSYEN6b-gxSnLr-3-LO0c9IoIW9sQDq118FTNZPhn3V4K2EXTS9dt-dlHIN1FnFLsHwZ5zcVu-HiU0uzPDkqTdkpK09wPx1L-QmWaB3zl6uTktUqbq85NzvbuDkKtZAHkoCbhRNb6ZqHSeLc3Ho94CK6G6gFg24SubRAVpulylutsPe4qb0AFsg0uVBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563a2467b.mp4?token=VnffEh1Cdag5yGg-eHoEIEI5ecGVXhHfEc-IJwv3kEu5r4kLTAohcUfyey4794xmwtuchXu-0SGlYpLp-kOekwgCXwouc28dhUc_jf_W3XdW9mYsebjq18WNpk_Wz5PZzYJBUG1DGCMPVPoUqUkMtF1CIfXSYEN6b-gxSnLr-3-LO0c9IoIW9sQDq118FTNZPhn3V4K2EXTS9dt-dlHIN1FnFLsHwZ5zcVu-HiU0uzPDkqTdkpK09wPx1L-QmWaB3zl6uTktUqbq85NzvbuDkKtZAHkoCbhRNb6ZqHSeLc3Ho94CK6G6gFg24SubRAVpulylutsPe4qb0AFsg0uVBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
هنوز فصل‌شروع نشده لوئیز دیاز گلای سکسی خودشو برا بایرن‌مونیخ شروع کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/103046" target="_blank">📅 09:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103045">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/114a435ca1.mp4?token=Bt97L2KwpkXqgZMaPbPjgYTXaTWM_KoR2bkbzJM46SpPD4I_Uov8QDx_xd5UpTqp3VAw_5DIIJB26miINyp54W12-RZypbTleNtEsMrIyNIuYxKFhR2rn6TGv5RIdE_gteQcoQii683HDXk4XvzXjYxo6e4z6ji15iJtD5-aQFuafPZ_W_C-AaEZ68z5RhNddXHOg7na7pOfam9D-5Q8wTUSkE_P6rZ_Sum_MOvH2VfdnQSUbW-820MW6dpYph6rhx7y4ExHknEdL0XWSuFH6oJxk5XuMxqxuQ_c1acMaCjOExyGJI3Dq0XDZx_wpaqwTMYUuHRfEw0Pk02-a_mDrk66DStWNaaoI96rK3KLd1pEaWdcpspgDd5MXhHXlUI6djlgIBZAIk3-ivTjNrc26gYH11cPJVAhwIdyv2S2AnswmvYRGJqV3zvm5ug9HDdyHjZL18XYb0BL1max4mznmNXdFPB5A1lDBp6GNS66Qgu8Y-PnV-ac4pUplLz96s3o34dBIeMdwJ3VGN4aBJzwyfcsE4YnqabmqpeekCyBzF42E17v9CDLKWYoUPRqFSOAFfVCUT7YROzFJIUme5BHxOjyvchM0VESGOSsowknvC9c6Yf5g_vI7auOMfaAwifcqvMiN7awIgqUrJQJEgf28EgipbyP-0z9x9CZebNsw3c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/114a435ca1.mp4?token=Bt97L2KwpkXqgZMaPbPjgYTXaTWM_KoR2bkbzJM46SpPD4I_Uov8QDx_xd5UpTqp3VAw_5DIIJB26miINyp54W12-RZypbTleNtEsMrIyNIuYxKFhR2rn6TGv5RIdE_gteQcoQii683HDXk4XvzXjYxo6e4z6ji15iJtD5-aQFuafPZ_W_C-AaEZ68z5RhNddXHOg7na7pOfam9D-5Q8wTUSkE_P6rZ_Sum_MOvH2VfdnQSUbW-820MW6dpYph6rhx7y4ExHknEdL0XWSuFH6oJxk5XuMxqxuQ_c1acMaCjOExyGJI3Dq0XDZx_wpaqwTMYUuHRfEw0Pk02-a_mDrk66DStWNaaoI96rK3KLd1pEaWdcpspgDd5MXhHXlUI6djlgIBZAIk3-ivTjNrc26gYH11cPJVAhwIdyv2S2AnswmvYRGJqV3zvm5ug9HDdyHjZL18XYb0BL1max4mznmNXdFPB5A1lDBp6GNS66Qgu8Y-PnV-ac4pUplLz96s3o34dBIeMdwJ3VGN4aBJzwyfcsE4YnqabmqpeekCyBzF42E17v9CDLKWYoUPRqFSOAFfVCUT7YROzFJIUme5BHxOjyvchM0VESGOSsowknvC9c6Yf5g_vI7auOMfaAwifcqvMiN7awIgqUrJQJEgf28EgipbyP-0z9x9CZebNsw3c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📱
✅
استوری وریا غفوری: تقدیم به همه جان های عزیزی که برایِ ایران فدا شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/103045" target="_blank">📅 09:20 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103044">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbaa91a27.mp4?token=ql5x1OPy0F3Kc-62yCjKcm2jzl3XASzybItLEXmdx1JTITVUqBTEz6Awwmo8wrWrW7Yuxkyl-n6FQf8ou58qbPwU852Zkf-6bnLiIMBvZkk_OHEWaZLzf-uLoZSNONrhSBmceAZ8q9jqOUnS-CLveChqL1sN_H87Ax9Go82QzgBo_1HtY4CaJV8kAZnMgMLXYCs-QLoXzlgCc5oB7x3lsA2QublXVOWyiYydxzVd7DEN8okT28g0VfMn72xTAa-_Fxc9Asc3Ah4N93vE3pNrNUBm56aNIJVZRHPnnd7SCrKcrQPtk6gW1zjLzj2elb-YKcupr3-OnN3U_I7-zXYu3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbaa91a27.mp4?token=ql5x1OPy0F3Kc-62yCjKcm2jzl3XASzybItLEXmdx1JTITVUqBTEz6Awwmo8wrWrW7Yuxkyl-n6FQf8ou58qbPwU852Zkf-6bnLiIMBvZkk_OHEWaZLzf-uLoZSNONrhSBmceAZ8q9jqOUnS-CLveChqL1sN_H87Ax9Go82QzgBo_1HtY4CaJV8kAZnMgMLXYCs-QLoXzlgCc5oB7x3lsA2QublXVOWyiYydxzVd7DEN8okT28g0VfMn72xTAa-_Fxc9Asc3Ah4N93vE3pNrNUBm56aNIJVZRHPnnd7SCrKcrQPtk6gW1zjLzj2elb-YKcupr3-OnN3U_I7-zXYu3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✅
رودری که بارها مقابل مسی و کریستیانو بازی کرده، بدون تردید لئو را بهترین بازیکن تاریخ می‌داند.
🔺
او می‌گوید تفاوت اصلی این بود که کریستیانو در محوطه جریمه مرگبار بود، اما مسی در هر نقطه‌ای از زمین می‌توانست بازی را تغییر دهد؛ تا جایی که فقط با رسیدن توپ به او، حس خطر به همه منتقل می‌شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/103044" target="_blank">📅 09:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103043">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/103043" target="_blank">📅 02:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103042">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=vDHzj6ImXqb2BBjDUavvf24NSCVifsgoZzUrLTqeETPMoH461dGGs7TSXzW45sx9RUycxLbgNvmpTjaFgqR1Boa6YXhpEFXwsiEYSraPus9GhdLrsyFS88kYVc8pOZbgs_dGsEkIOaGo9RmUASKIk4D_7OGjd8Eb9LywpFhvkZRNFFZf2VlW70WZECHpX8yX0NkZou8yVyqPWwFdz1q7KVO8Pfe9kp5yKtukDaL8ucB_dKytSz2HBnt9sVXNgkbUcmqKOVGc1Kmtwe-QlNXj_csAfbwLbstPXc9Z-gRD-zoaoyTDVsepOt8ff4cxQmp7Jh_eK3ZoP4w1WqQbxFiqOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b5ff304.mp4?token=vDHzj6ImXqb2BBjDUavvf24NSCVifsgoZzUrLTqeETPMoH461dGGs7TSXzW45sx9RUycxLbgNvmpTjaFgqR1Boa6YXhpEFXwsiEYSraPus9GhdLrsyFS88kYVc8pOZbgs_dGsEkIOaGo9RmUASKIk4D_7OGjd8Eb9LywpFhvkZRNFFZf2VlW70WZECHpX8yX0NkZou8yVyqPWwFdz1q7KVO8Pfe9kp5yKtukDaL8ucB_dKytSz2HBnt9sVXNgkbUcmqKOVGc1Kmtwe-QlNXj_csAfbwLbstPXc9Z-gRD-zoaoyTDVsepOt8ff4cxQmp7Jh_eK3ZoP4w1WqQbxFiqOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
❗️
ریدم حاجی اینجارو داشته باشید
🔻
حسین کلهر مجری سابق صداوسیما مصاحبه کرده گفته که یه شب تو خونه حشری شده بعد زنگ زده وزارت اطلاعات که براش یه پرستو بفرستن تا چنتا اعتراف داشته باشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/103042" target="_blank">📅 01:49 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103041">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4bekxgYOQZQNbegFwdQGrvWvwrdaBI9TBcc0NC-eJpU4532_jGCud66XuzwcV1G8MDYK70Em8YCvszkRxn-d426TaLvpzgprF2tGqn9XgdSv6R5SbkYEQOMGgiwEyJBt9h4reSUgSLeC2-TC9nxMgKddWCHKWCpuXt5KUY1hzoQfOPNDu9LgchvD5yWK0-WpsJrNBW5C04IkXPKxeH7-QVYU8w6w6dcsfWpHPmI84Ym6Gm7lCwgJ6gXW_sD1jc05vd05-Uo3ADW_n-1AuOaSwLOYJfPdrrqEKGEHIbPgRdAPG-5d8g9Zv3nkWZMAPXi5ZtX7X6hxP_J5JAwszLE2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
🇪🇸
بنظر فصل‌آینده عقب زمین بارسا قراره حسابی تیمشونو شوهر بده؛ مگه اینکه دکو کنار این سه نفر یه مدافع باتجربه اضافه کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/103041" target="_blank">📅 01:38 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbzqJGzgzPbwrppWXlub2HPanGEYbXBxYQtBQNaeK_LJLVNBCAPokB8UuZ-L2cDL9fpI3JvbIi11yNKOTCQ9PFkADQQOCmTTSkuzBYF97_cMiwLhrvLehZlu4cjPr6qorMEzRJxKq99EgPPAtmAI3dcFcGYGbzG3TuyZ5raNR0nbiJupeg8F0tQLfZlDe9zqo3LZrw38btkL3CmPn8BGgVYor5iiXCGfGzxeTABWmpW9vVWStahJvFRNhd-Jtm8fxYdq3OxWDwg56BHDKj0Tnnmcc3SVBHzfWMMLOOml-bfD8JDZn3frVXnP_k4RirfGFUBAPHAtFwDI9xhgVEP1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
⚽️
لیورپول تمام حقوق آرائوخو رو پرداخت میکنه. همچنین بند خرید اختیاری داره و با پایان فصل‌آینده در صورت نیاز قابلیت فعال‌سازی داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/103040" target="_blank">📅 01:31 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/103039" target="_blank">📅 01:22 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC6PB1838rXkwrvlnEkMl9uwCrnFVNeYaOMPEjqVitv6TJNXiELGIbfM9c3UIDEGVAr2ad_v7425i1r8bui-kZzm8ENW_US4VrbbqlsT2Be71VWy8t-BXIn4mi0tZ2qcokj4cV48qDBNx96QMfnPQ3YPfKi24a6JY21dMy4CFG9j2_4cc12RDcXxUaF_0UshfSGF44F3lMcpqB1i9Bd0a9Yf0LV_3QB4XP3MvsVq_Zl4YAK_-nzOhSgLvEgrukulXOEYwPvDZ8ZDV38y77qkkR1OfMwX7s3BGux6cpm7roxQyVI-O7e5VOk7qz8GFYfMo3AOKMhli8GzWXSg7sS1FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚠️
🇪🇸
بگایی‌هایی که اسطوره آرائوخو در سالیان اخیر برای بارسلونا به همراه خودش داشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/103038" target="_blank">📅 01:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOHHvRj6GQzyn8dEHJsMMGmpKoA_UDi0g4eYLUc5eWucymLxesRlkRLmmeqO23wOjV6LoFNiitHQMANbkP35mFcyyPU_AkbtES7xTqZFIc9eUDl8dAm4YzWMpsyTY_LG083YiTHS4kXhwqah1anqqVBqMPsaAEx3LWy21-VjgMIQ8n2Lq8wJ7Q0b4bKovKKF4PdmBnypSjEkvOHlibR4Aivjhd9IzgdcJaQX4B68oarNkX36kQQcmDRbtaozmSVdh7XchP5QtGUwelWXG2kLLiWw8UNL4NeRdEDO3vjAkSVjkgsPlaJmxdFW3mgQeeZnk-IRb0lkxdc6xCgHeMbNJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🔥
🥶
اینجوری که بوش میاد دکو میخواد یه مدافع وسط بگیره؛ کوتی رومرو یا لاپورت؟ خواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/103037" target="_blank">📅 01:11 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103034">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOfJY03DNsQtoe9XyPfnX-_6b27jrBOX3JGHX3-KM5Ys16N45ztd6gNuOZxOBBtTK3H7uCof3HOSG6It0zJ28HmkIf2FZP2BfBsA7s4N7aVmJDbIBbJIuEt9mNKiSJuQLfalvAewgTlRSRjLJztKPgpVtbnWehgIZBFoP0tmWNB3y8N-bVQMlP90I5GNAvLb9XL0uZJxfxItJb9VVgW91OP8AX5vwbHOK09TjIVWXVRFSxScXk6xjC1wcAPU7yeBD0jg1JToDBBJ-EakHe_uu83DhsVLmV9dUBDMWjit7V_qev6g5qB09VojZljw5We7IqwnCDxKfjouy9xGPBcy5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🤯
مهاجمای پریمیرلیگ خایه کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/103034" target="_blank">📅 01:05 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103033">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tyQ5GqvI57qRytTABZfVK-st_-3yM2M5xxMSikNhhLWX59BtGTgHTtxt16nGiuUOTaoG3Q94R1p9A4FgrfRSPnIfK8MLSYbXHNY4jIirwEwJx_SsWfOMGNNxS1eV-3c0Gd5wLFlXr1taXOA2NDjJ7pBikzz0pHM1qFnAWEl0LQoIGpqHLlbBRwR3-SnEc1SPYA-ISNW09C6SylpCoT7A4I5bu1OBVnd2k67bI0gLH-r-PLSvDB2JN0tnkupmPGp1HtPoXNsErW0DfQdHl4imuPd-2JctJLg5Qw3pA9_5FkxiN3W4Qq7HSJBlUrF3psYoOz4EfudQB680wmyHs4i1iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🤣
🤣
🤣
دکووووووو بیشرف داره چیکار میکنه تو نقل‌وانتقالات امسال با بارسااااا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/103033" target="_blank">📅 01:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103032">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/103032" target="_blank">📅 01:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103031">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGXZqx_At4TCn_pZHYSQ3RizPGoIvVuMpV-qBU2ejIFWACgA4y_gAGRJ5E7ZhbwKGRtDSLP1wu66iifvsHUDH9wmKyQsmwVLba5qReV5uGsBCMYBL_zz7dmnoCeOyGOdRQGO6cXD8_ZVxGYaqK85HldVddKDkHYkZfL103TpdIabxeT2Vq-YX1K-DFJYlEO0XUC5wF-MQnd8CtEfDOyMPgniIF9ZDQSCqwIrcQ3rrz9C7IlK5Bha5Aah1gDhS_0lambZ9WVUmIyOhJ4qqoO58D8z3Wx29WHnx91yS1r5D2LnYxrwBXcZFYFCemdZGTgu50V63UvQRRyigQpWSaIuCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🗞
🤯
🤯
🤯
🤯
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
#فوووووری
و برگ ریزون از رومانو:
🔻
رونالد آرائوخو مدافع بارسلونا با عقد قراردادی به تیم فوتبال لیورپول پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/103031" target="_blank">📅 00:57 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-103030">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
متئو مورتو: باشگاه استون‌ویلا درحال مذاکره فشرده با اتلتیکومادرید برای جذب متئو روجری است و احتمالا تا ساعات‌آتی این معامله نهایی می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/103030" target="_blank">📅 00:49 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
