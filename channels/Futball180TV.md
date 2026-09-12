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
<img src="https://cdn5.telesco.pe/file/s8SpB_CmshFs-nxdSTGTlUtibTgEGp6YFOcJpmP1o4qdKfImRNTy7T3IgbK1GHtfZxil2oCx34oWUnNhUsJzYD-SxEMdyTmh2Vjqseoy29tjsXtDRMA3aYjQiAXa6ctKkEn5jaKUThwZQ0lzYlZktxVyZoGOCaQ49NJq4fSrRfv8HIXtDZxvkmoRdtWmw0c4iHYjFZDCRcar0IVwZAc3Ak_llMIk6gMTKk3UR4c5KWFug2S8yUFO5-eiBzawdDNVtWhDusO27vReKX_ztbfhEyHzeoaWLTUk4DyopGmjds5SQoSCgKUOn1FNI4GDWryX9ixllNN3aH2oZVV9iIomDA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 416K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-21 23:00:44</div>
<hr>

<div class="tg-post" id="msg-106306">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=LppqXmVlAxUgh1z0gMHNxaxYsuFKtFP8TMnhraLBUH_G5myz3Im4NBfM0UdtBGWFxZM0Foy0S4F9vA201X7XCYAHlWi-96M2Rk9wXa7WgP3Iy8bDOeeaSVOfov48HvSwF_YQSfxSvzp4fH0AxwEMefMcJMk4AkZ-sYHdw7w8hqCf7XM4GiROVcU8OYRHcPRaF1FyGYYwxumeYm1C453Bf9svKpcNpYSmrNu2ay4UmekBAsCfPVnlhVP7Xu991_AvbwzgakCbIGeNJOGZ_od7ZCUBWTqACGGPuR-g1MCZSLr57_OlZhC08_h84BVmG-SfBnihUfkJhI7xGT2YX3oqdg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2689afdf46.mp4?token=LppqXmVlAxUgh1z0gMHNxaxYsuFKtFP8TMnhraLBUH_G5myz3Im4NBfM0UdtBGWFxZM0Foy0S4F9vA201X7XCYAHlWi-96M2Rk9wXa7WgP3Iy8bDOeeaSVOfov48HvSwF_YQSfxSvzp4fH0AxwEMefMcJMk4AkZ-sYHdw7w8hqCf7XM4GiROVcU8OYRHcPRaF1FyGYYwxumeYm1C453Bf9svKpcNpYSmrNu2ay4UmekBAsCfPVnlhVP7Xu991_AvbwzgakCbIGeNJOGZ_od7ZCUBWTqACGGPuR-g1MCZSLr57_OlZhC08_h84BVmG-SfBnihUfkJhI7xGT2YX3oqdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پنالتی امشب اسطوره توپ‌طلا امباپه
😍
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/Futball180TV/106306" target="_blank">📅 22:51 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106305">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ریال امشب حشریههههههههه
😍
😍
😍
🔥</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/Futball180TV/106305" target="_blank">📅 22:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106304">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کاررررررااااااااس زددددددددد
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/106304" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106303">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گلگلگلگلگگلگلگلگل دوم رئال‌مادرید</div>
<div class="tg-footer">👁️ 2.75K · <a href="https://t.me/Futball180TV/106303" target="_blank">📅 22:49 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106302">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9x1sACUpSGZ4qqngw9dAPtCj4MFhOmlsCnOO96viR5E8OHf7NFCn8H62mrJKBnF3SpWPx8QKbLYWJGwEWhZVMf2jJwz3RrlKx-AEQXDwNgqgOwjFkhFwVpDsNH9a0nYfVzOgcx0UVO8PdgzT9-CW1fY5k2fooThp-48mq1_ZgE-FZhF-czZCkoOUIMNAoTeRROgN10ITgT_sKX6tYlK7OfdDBh14HTQgPgK3yV4QAqf3A8BiaOAtwz7Sc3kig7D_pf0WWsZbLhT8bkElKV3JgKxxSx9bp7A7hIcToLLUrcDF-TTv202p1kVO2yYHyk_ONEiN5JPTgQmismdy8L1Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده واقعی توپ‌طلا
🔥
🔥
🔥
🔥
🏆</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/106302" target="_blank">📅 22:47 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106301">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رئال‌مادرید زددددددد کیلیان‌امباپه
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/Futball180TV/106301" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106300">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گلگلگلگلگگلگلگلگلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 3.42K · <a href="https://t.me/Futball180TV/106300" target="_blank">📅 22:46 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106299">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">پنالتی برای رئال‌مادرید</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/106299" target="_blank">📅 22:45 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106298">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTSbbV5KFDvWNQarFKZVo2NOQ6ewZCTYdI3otUZIgOBMA_eV8Ft5wo_Gv9UvcMnlhVtRGTWpUVTLjXpTFIcLvBhvaa8-UNxWnkSqg88SbmbyNe6kRQ1YqOSvnzpbhVqDnFJFZE67sPbuEp7LrCZCi6t2RnR_m_CKjBtZdyfIndT8EJBnclbR57MBv4ip_9wBKFTxOK8psCeqgXF2nH7wUCUyKweU1bcb3BvUtzUIs8bnSfQV6stbk4vGazP9y0JH8Wsj7IfWqukD8pj2BV7WaGsfYeHSCK2a0BnXhuCK8E52M8-jHYWKdH3K-JjExqM5Q0vxptou270dmk0k7HL3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
شماتیک ترکیب رئال‌مادرید مقابل رایووایکانو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/Futball180TV/106298" target="_blank">📅 22:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106297">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
یادی‌کنیم از فینال سوپرکاپ جذاب اسپانیا در سال ۲۰۲۵ در قلب عربستان شهر ریاض!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/Futball180TV/106297" target="_blank">📅 21:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106296">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mBo172705bT2zbV0Sj3F0KKht0mre5b3H_I_9HrGxMff-qh45L5GCMDQA1h_kzQyeYJIIZ9DyVGttkE6RXORYWUu7fG5kkVtdoriE8tVbiwZHzpnvHxuOVfdi9IP25rFRvcoHheZK0N3e6iSgfBEsBHbtQZyz36FQut_g7lRoJe52rTIdRBVAYuVVDttXDbfCrYiUantaILz50d50_k88UflA9emDiuDvBE0F1PubWHDiz8MZ4Xb9qUowB3IjYzhcC7EFVxIWzHCuBh2M7x4lIbRI_xqBEWEUjh7Y-jN2irorCQme3SQAzGbz5zTHN9KIxTgB3Hgxxua2DQEXaqBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇶🇦
پوستر السد برا بازی مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106296" target="_blank">📅 20:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106295">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOz2XwwmDJ3RUsTlnoJA0sFDpuSwjCpne0vR7WALwLZ7f4_J3H6mvt-rDbF7a9N9BuJP0zzIYr7AxD1IPn7CIyMNoE3-bkPy_-o_0z758IP63hMj1MfnV9zrOlB786PoL4AlA85Co94dp9zcNo_1JhQk6mvbBRBkjtq-gyJtV0hp2i_e1qATNpNZ1sSCO-_j_qBYpfB5CFMcM49kS_-Qm4ns0RIQqKnkkzz8X7lC0Q6vT-4s_YWPQQ9bBTUq66MIQAzDkz7IGeaMVgMO0wp5fMMxvuPMWK_NMgVPwJX5EoLmt_3amb7MCOhQy5WSos3D9FPdlLt9MmAaFqOelFPI0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
😱
قیمت PS5 Pro در ایران به حدود ۳۰۰ میلیون تومان رسید
🔻
قیمت کنسول PS5 Pro در بازار ایران به حدود ۳۰۰ میلیون تومان رسیده؛ در حالی که این کنسول هنگام عرضه در ایران حدود ۷۵ میلیون تومان قیمت داشت.
🔻
یعنی قیمت PS5 Pro در مدت نه‌چندان طولانی تقریباً ۴ برابر شده و حدود ۲۲۵ میلیون تومان افزایش یافته است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106295" target="_blank">📅 20:30 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106294">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReveQs77sKCxVIKZ3fpffNtNJNlu53is-4qP1c_wymw6R8gKmY3eubVAocIu275wk9Ie9BWqHG5aMuTVd1vI02Hp4W75vecp4NPQEjoBdGqUwvZjXFP-HwADNDO4zYfob67irFioBy-uaBos2ntYKLWoGaMY1jDWG9WXIwf332YC58yFxcgELqX1W-MwhU7c02CX6E6nbeZA8xowGskgwgGlJKbMA6xIZhlw7V0Vrs1DwQjF7aOxup6aK9sxWnc_5yD1uGw3o7kLuGy1HgY9MM7Ecc9GztvyCbVzXI5zwsrEqxHTz0YqyFUrZob-IQphfu2Cj7Xpzip1yfyJbc4HzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب النصر مقابل الخلیج با حضور GOAT
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/106294" target="_blank">📅 20:16 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106293">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMUmauHOnW9KsuTduB6N_khWFkDVx8OMEpLcT-V69UiaDaGoEI1FRMLJC_bV8zhfl2vjU8g1NTKmnAuMwo4qbw2ZPaAjfvSwwf5K60WA7ILThBa6kUrBME2a0Pzt2ED49xu3CcOr1104LxNv-gLOYzmoD8sgweEGie0glwVIaV28pymOWFOX4-Al_v1_-1TpiuAsl0EJEZngVxePtoJbRRQGJdBke9sHyhmHU36fBrqSAc0wpDuWqvjgQmrEO-bB1USuUou8x7TqWVoK-x3hUO4Vw5Hak--zsc93ne4jrvfoBdBPrRLcjEiKV1Jc8PP4H2Lr5JrDrT5rH-q_OaZtSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
استقلالی خبر جدید براتون اومد؛ مارسلو بروزوویچ از النصر به السد پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106293" target="_blank">📅 20:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106292">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✅
▶️
صحبت‌های‌جالب یک‌بانوی ایرانی شاغل در آکادمی باشگاه چارلتون انگلیس که بسیار شنیدنی و جذابه. حتما ببینید از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106292" target="_blank">📅 20:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106291">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/045726ccbe.mp4?token=BTfYLBLNZZ3nzqTmxR7M5KeBrIL6zjJcCs2NhDkInU4-_8wDLjD6AnaalIwUEV6HmIbqzWfBd0D9kd48kJLEe1CWNVZI-lGClirusRIG61XhpM8m5tyoAFXSY3gGSbTcoExecpW5vAPwtiYJUUgF4Cp1bOsD8_YhJf_PcGB6tfvoSJSeg3c2_2kVpAJ1VWqStWL6UvnDTnikYWw4rHbQSYJYZMpqpPnocfDijBm7mf2R-DSepvds99PgrpH6D8gQ3tKuxgShyb2To_l7Q8O41QKo-o4TLnBtw-cmQin7G36uS8Lj_barmWgAFrunilSk7tzNwxmSPafOzH9gGEe-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔵
گلزنی گابریل‌مارتینلی در بازی امشب الهلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106291" target="_blank">📅 19:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106290">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMAjTQC1cmkn4DC5eoeKRDFfYLy2o7vkCwSOYV9P7TeSPnpuh_yH8zHnok8FWhpr2-Z0Yypn-dmGbVD7u7fKTVrrYZZTLT9SR_tCkwdzYoT87f0NC1sAk4Gcc6di8BZ6Wcy1zs4GBQPqjwwsrqDKscrc0kH66TsnsjLO_mM3g8GXCi3jbS0YCzZ2naFL0ipwIut3r1HcZacvKSiijreXz7tV6Yzc3D4ofCswVtfou9IbX4sCxh0mjVCLoK42oPg-SxWvLlNLd5Fgvt0UXSaKjuOrXR5RSfAkOw7eFWks4zzoYX06Nvvuq8CCksSpzrphopBqyEtr-N3TjaH8eh9zEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست بارسلونا برای دیدار فرداشب مقابل لوانته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/106290" target="_blank">📅 19:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106289">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106289" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106288">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iSyi0BYqJr-o5XSkc0q2A4fk_K6e7zhdA6dtKtjnPC_klnrUK13FxKlZ8_N_Pt8T6sDhSFEfiBtjgOKdXdyb7yYQyGHoNfwKV08NQ762vOxA72wGwLewMBht45v3lnWWCyLhcvmnNipdO8tmjcwk4L4VilKU-yCSQaCW7vs1g3xkVZeFnl0MUxGgx4rKLdy0ayVWsqTwSDXHjBoLCFY7XzBfRWQX8XVwsdCwJlrNfPoeIjsQbMg-HIlWalbe3reZ3ltnFfG0KIqgyeR5b4J_2XdvSQ9Ouy8eMzPcSHtKtPLXQQyY5dsFq8iBLwdfr5vY_vH9cM_xS72SY-lU3MXHiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
میلان
🆚
لاتزیو
⚽️
را در
TrexBet
پیش‌بینی کنید.
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
میلان: ۳ برد، ۱ تساوی و ۱ شکست و ۹ گل زده
⚽️
لاتزیو: ۴ برد، ۱ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/106288" target="_blank">📅 19:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106287">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41e5692356.mp4?token=AFzTt0uq5r5N_10CAnhZPCTqHMUxq2Ay6_XJwUItAll0HrsgDd_rWj-MKZXYzAwk5Avuc35mAme0siR_WB4DxEm5Izg_nLGiWkZkPLfX08j_3bKeifN9tvOqhBOsQWtWizHTtB5oFbTlqtAQlOo_JEhQhrHQEvIdVGmhCbAH3IigG5pR_ws8PcwpkDaf8wqNw7715PSJPh42t4hDa0AgOD3VFfRr40u8CJyJ48hKNo5v9NfJTphe-zlfuQ5BsxrzcNU1TLvoCEpBtfWkYziD6uAHQ9OOZMdUwQ0xnWQwPgJg6cwbpEAKreR4jCg320ostk1wnkI8t8xLmZMPuNc8XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
تفاوت صحبت‌های چوپان قبل و بعد جدایی از هانی‌رامبد! نمک نشناس هم که هست ظاهرا!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/106287" target="_blank">📅 19:32 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106286">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gt2ObcPcNbvoBiVjsNnx7-CMPSp3XFPPve-x6pIvnWuU_Gxi1ibvrsw0N9ORmXC21PsMyNlpAaZR1FrN_m4z3Ka3IA3OrlUNT0LULDaVgRJGO6fVs250l8d-0rQGBm4fbaqT9pgSPu8xoTELF8XwOYVXvG2sl_p0Scx0LrvG9-FNrAjfcyVmgONrF4esknjoY-bZYON3zJSnLFBOxuueu6i5weOBT0vSvmGaoI_jSH5KWqbZ_iAqLHkY5pi3T4rLJjssjCQnc1Exo54FDBRPWrG5acPkMy7yxna0RVBen_dvdjf200mfMJKQ9-F2inH6T4T14w6paZXjUf7Hes2_Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
جدول بهترین‌گلزنان تاریخ لیگ‌قهرمانان اروپا؛ هالند و امباپه با همین فرمون پیش برن به راحتی رکورد رونالدو و مسی رو میزنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/106286" target="_blank">📅 19:04 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106285">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90c64420bb.mp4?token=OYJmeJ2HPSb5aefobaE1Z0VKEIlNQYVzcO5-NnUwOa8R3GDk-8_XQmGY_2NpS0q_7HPLzdIiZvl6kEV_Xo484TRJEo57JgcCAKfadp2j-81vSTzrMoWYfhnqQ8Ovkx7asfN0sUBAyZbYaO4C3ZgburoMLuXnHtydGCLUGAcb-4Yg4oPgcH5V9MdNUQ4A2Ssfwd0F9TePSVbnQS1sra7pKPK-39lCXW2H9t5MUfbxZ9jxg2a4bLbTgH7qKJeHHfQN1t7Rm-Ju95IQiYUliYN-Iha1R5Fk16gJetQtPge6rSUmwPoOE5GTUOtndlLOMO1vdQN1jqmbooxoygIp4GQbjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
🥲
دردسر‌های کیلیان امباپه هنگام دیدن سکانس‌های فیلم زیدش اکسپوزیتو :)))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106285" target="_blank">📅 18:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106284">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/833fb28b6e.mp4?token=NpE7eJ2DmY052v2JTsFFfYHjIKd9gCNsGNMq45mSu6Cgw0FqRB4fSx50i4p1ciCcijGKUdz2dlB-jwpJ-Bsq5vTK10NiXD7O1GWjAYfGw6sX9mgd1RpffJAFOQky81284FRinH5DWJjx3EeTAvSnJYOXBvFJclfz-2h41bJPWnnAXR9i3qZdOFBKiV2cUbMyoecp34WhvZDn1sZ6itzuRRpfhQLPxsDkJmDSM1O_IQIwdtj8s2Qqz3PcNEUc_BEWVb7L77EFBP46nx3NeGfjZVhz5JWTg7crM6QZAFyXED8uT1IAGfiQ9t1VatwzP6qjawVhSkZte3U1HXza6j-BGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💔
ریدمان دیشب داور اسپانیایی بازی لیگ عربستان که بجای کارت زرد اشتباه کارت قرمز نشون داد
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/106284" target="_blank">📅 17:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106283">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9242df0ef5.mp4?token=c0MpQQP4OptSRX9aFwJkYzd3WvutngxANuvaxIOchhEenwvr87L0dW4zm0MJm9i3EFCJ6zxunUfguNoN0cjy2mMhLqzMquD7lTEBEmd4MPGCVJKvr_YjCVQg1ieFacNyts_yGg29karF68IwhXE50iesplFh3LaPycrC-wao3Rf0kRZIbFxzdHPCuIxD4cIk1Adg9q_jF2ARqVxUWo7ZjBOhxDojjSx3tG93-9zRZ7sRQ7IwYaMKZ1pX3c0jYcXC73iRvCrC22YpXqgR8W9X6iMOV3LITTa-IBEGbJgJe7ugTCZ9jVy6gHzeSsT4hVS7UUN0v9fThZPxhx8Bw4RwhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
افشاگری جنجالی محمد سيانكى: برخی تیم‌ها در سفره خانه هاى تهران بازيكن جابجا ميکنن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106283" target="_blank">📅 17:20 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106282">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iM1Bvv3HZKf9s4skskgwM2Eh5vmnTB7pberyOuFWejmNvMMHfG0TQdFXQniMrpNzlp9DJbX6NSNfyiIZpD9x6ZGkhExqxLBDBEH_DMc2i91_sdZpf7R6-ms0_6SQMVOL9gcWr-FbayNUGHipPm1rwyMOfbNZNVHTnjtMAtzYzrQrtGZ2AsuMB0RDt8HHKbeszpu2Ops2JuNvcYlwR37ZglXtiymmSf1UHl1wYAps9UmTjEr7MD8o9W-GTIsNHKt4Z0joEUbCQ8OFFoXAEDeMY8idswQpBU8cE7h7So86FaOl2wTHvuk4SLVwT4X6YBNyDU2suzeDBx2xnSZuttkbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
🔥
🇪🇺
عملکرد تیم‌های انگلیسی در هفته‌اول UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106282" target="_blank">📅 16:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106281">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=C32jIRSNGbzE7dkPygxVXuLsb9L_GE1ixIH_UD4rCP2z8eoQ5UxTqAwCrMgYpwQ5vG-KAan7S9297IyKWfpV84EzefTFbWSeA5S86IhEIbFj_-DW-69qWQbGqHrylS0Q_ekI5ssRwBwMUGGi_Cq2kEk1PGdFkgo5z_SWbGoUhlGHctKU1P05jJMWxLE_kaXWGUpEL2x274YpKInOK_1a3d9l8rXvNVMkI68tpuE4ot22WEw84k2Ma2gXLyI_iZZpJgW42GD7Ky2-7FnSbpcF06Ry2TEtQan31fENfCfUEsMyM-P0KuVAYTmBFIKwhgK--t6omCAJPy6Akv4mBAB4OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc8b60637a.mp4?token=C32jIRSNGbzE7dkPygxVXuLsb9L_GE1ixIH_UD4rCP2z8eoQ5UxTqAwCrMgYpwQ5vG-KAan7S9297IyKWfpV84EzefTFbWSeA5S86IhEIbFj_-DW-69qWQbGqHrylS0Q_ekI5ssRwBwMUGGi_Cq2kEk1PGdFkgo5z_SWbGoUhlGHctKU1P05jJMWxLE_kaXWGUpEL2x274YpKInOK_1a3d9l8rXvNVMkI68tpuE4ot22WEw84k2Ma2gXLyI_iZZpJgW42GD7Ky2-7FnSbpcF06Ry2TEtQan31fENfCfUEsMyM-P0KuVAYTmBFIKwhgK--t6omCAJPy6Akv4mBAB4OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولی تو تاریخ لیگ‌برتر ایران هیچ‌شادی گلی مثل این نبوده و نخواهد اومد
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106281" target="_blank">📅 16:31 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106280">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=I8lc3rFASqQ5IUBZUTbAIqjM1EYjGMGALHXBQnHCkDmsbaKS0IOOIRjn5CEtMx2WMUnsM2su-aXXo5tBgesLimUbOksPimybxg2d0QTojmjKBW1D0Qffg8ZXI_KsAHvwPv4RxOuFtuc4-MNMS0-N_uN0ydhlrA7So9DXrJGzK2tYmBkMHhcX2jApam6cEbyuslAVDeq3YYk85rJ_p5tYN7neBigTL3_xzKA9_8DzIFvT47sy3zN3skzCIz85V4mEUzLiKib29Tr6UE22fXvF7Rwfy1hP-0lz7_Bm6n31a_-zMgJf9y8dPgaP-xi1Q0qU_Yosge0p1DqC3QPaoUj15w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5318ea7807.mp4?token=I8lc3rFASqQ5IUBZUTbAIqjM1EYjGMGALHXBQnHCkDmsbaKS0IOOIRjn5CEtMx2WMUnsM2su-aXXo5tBgesLimUbOksPimybxg2d0QTojmjKBW1D0Qffg8ZXI_KsAHvwPv4RxOuFtuc4-MNMS0-N_uN0ydhlrA7So9DXrJGzK2tYmBkMHhcX2jApam6cEbyuslAVDeq3YYk85rJ_p5tYN7neBigTL3_xzKA9_8DzIFvT47sy3zN3skzCIz85V4mEUzLiKib29Tr6UE22fXvF7Rwfy1hP-0lz7_Bm6n31a_-zMgJf9y8dPgaP-xi1Q0qU_Yosge0p1DqC3QPaoUj15w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥶
باریک‌ترین خودرو جهان با عرض ۵۰ سانتی‌متر ثبت گینس شد! وزن خودرو ۲۶۴ کیلو هست و حداکثر سرعتش ۱۵ کیلومتر بر ساعت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106280" target="_blank">📅 16:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106279">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=lwR-M-2h0OBNO6BvP4hqRpvMx-K4dyS4li2_FTKZXDA4rP69ZbBO2C5NTjzmKt6VLVGeKw_gkm8s03HYXghH3wQhOrU09OlUcJJ5rXaQlOPVtrkmamWZyz51q2yhmMMEaQl6reqm6xIUq6gO_PECfFO2QHVvq7m9y2Qx_9uSYjXxzkjM0M4_YIppmloXFiyBvipRhqJf44_3pKr0J7xa1YVc-qM4KFrP9MPUSA3xTaLBC9Zc5UeE2e49_hVS7xn2kjSRA-2-ql1xr-p7mTKXGW3cj7TCXvQ0p9QYBXQFOJIFpllYwipc5rVRe9BX4Wk52I574FwyFIamgff-79MYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76c27ec481.mp4?token=lwR-M-2h0OBNO6BvP4hqRpvMx-K4dyS4li2_FTKZXDA4rP69ZbBO2C5NTjzmKt6VLVGeKw_gkm8s03HYXghH3wQhOrU09OlUcJJ5rXaQlOPVtrkmamWZyz51q2yhmMMEaQl6reqm6xIUq6gO_PECfFO2QHVvq7m9y2Qx_9uSYjXxzkjM0M4_YIppmloXFiyBvipRhqJf44_3pKr0J7xa1YVc-qM4KFrP9MPUSA3xTaLBC9Zc5UeE2e49_hVS7xn2kjSRA-2-ql1xr-p7mTKXGW3cj7TCXvQ0p9QYBXQFOJIFpllYwipc5rVRe9BX4Wk52I574FwyFIamgff-79MYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚫
🎙
هادی چوپان درباره کلیپ رقصی که در دی ماه از او در صداوسیما منتشر شده، توضیح داد این برنامه دو ماه پیش از اتفاقات دی‌ماه ضبط شده و ارتباطی با حوادث آن روزها ندارد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106279" target="_blank">📅 15:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106278">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f692d60102.mp4?token=v9S7HksaqP4IbkizNXG4cJp4PFyI28n9P4gGsCoONHUNw_FeeVeaePkXgT9JwdNVJyRut4Xz0yku_V3_ZPN6QuME4bFfZbMV27PvdtilbzgmVYFwhZUyQFllzHYKJlBRi15v33xp9gD8fS8bZPrwIo72dn9IgJdM7fEsBOSr7WeeKE4Gz0115ovhtuQLrNHtYFRbxiChoqWNDmHWimAH62EU1jFv_mVgscK2f1M1jUfDppj7mXsBhoo2B7YUnX-Pv61ToaSLEbxswD6XfwrtTOLtAHcUlL_TbPWaIjGeUufn8MepQCdWy9oceyWJoUCAYTLpq_94EP1WA8Y_Ez-OUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f692d60102.mp4?token=v9S7HksaqP4IbkizNXG4cJp4PFyI28n9P4gGsCoONHUNw_FeeVeaePkXgT9JwdNVJyRut4Xz0yku_V3_ZPN6QuME4bFfZbMV27PvdtilbzgmVYFwhZUyQFllzHYKJlBRi15v33xp9gD8fS8bZPrwIo72dn9IgJdM7fEsBOSr7WeeKE4Gz0115ovhtuQLrNHtYFRbxiChoqWNDmHWimAH62EU1jFv_mVgscK2f1M1jUfDppj7mXsBhoo2B7YUnX-Pv61ToaSLEbxswD6XfwrtTOLtAHcUlL_TbPWaIjGeUufn8MepQCdWy9oceyWJoUCAYTLpq_94EP1WA8Y_Ez-OUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
✅
تو این شرایط اگر از اینترنت زیاد استفاده میکنین برای مدیریت هزینه‌های خرید بسته، این ترفند راه خوبیه. برای دوستانتون هم بفرستید
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106278" target="_blank">📅 15:15 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106277">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=PwFbODS4N48IHuz9wOOcwXh_VaYRQk9ABDLo-lmlAECtToYpFjygoL75J-2CncaYI53JlyeScCAn3rgcm6jgH0N78_ihpvt_OlbMZLAsY73WuAWn_uxI0grFqqvW9DS2OYOv1hCnntpm3zA8Xtd-oMIOmNaUTz7X-tlNhr5QWyxKEN2fxvfmyh7Mflh-6SMtV0LQOrPlgQ7ebb64u9lJW_nl7me8JSaXycGH5ngs7CbyMVMu0M_hfrwsHvNCb-NVM8rVwPHeLZ8MoFUEMSx6EvbqnxPU-lKN_cO_0K2k-1Uwy7DJKAxlTtzD6lgBu1FA0jCJ7jB3HX43Lf5XtfbG9IisgzfCu5pKq7wK7U4ykuYcLY4_PXUMo51bObHhGhm-A8XjCCPjawABAPiKhTbH3NNuiJ3v8Tw2VZp83mqG1IKWBGrSbt7tPpG5NcgWlr8ESYac0dOKazNdYb5Kd8T5SNRU_Vcfknr7r3Q0hEWQGjJfj1I-DGwwhF9KyEmSrm9LOyBvSckYtkvvwjlqLKuDbci-1wDhPtPynT7_HGCTs3DvpvMIUBntHTz_BSzdocePZeRo-WisVhKrY0NS9IxLE5TMmfuqYGOpXlbER6lb-Vy6V3VieXJvS1gW3oa5L4lKbM9DTQZ5-fB0Dmi7sxX7TMti9ZG5uNmIgzwP6FPgChY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb9d15a53b.mp4?token=PwFbODS4N48IHuz9wOOcwXh_VaYRQk9ABDLo-lmlAECtToYpFjygoL75J-2CncaYI53JlyeScCAn3rgcm6jgH0N78_ihpvt_OlbMZLAsY73WuAWn_uxI0grFqqvW9DS2OYOv1hCnntpm3zA8Xtd-oMIOmNaUTz7X-tlNhr5QWyxKEN2fxvfmyh7Mflh-6SMtV0LQOrPlgQ7ebb64u9lJW_nl7me8JSaXycGH5ngs7CbyMVMu0M_hfrwsHvNCb-NVM8rVwPHeLZ8MoFUEMSx6EvbqnxPU-lKN_cO_0K2k-1Uwy7DJKAxlTtzD6lgBu1FA0jCJ7jB3HX43Lf5XtfbG9IisgzfCu5pKq7wK7U4ykuYcLY4_PXUMo51bObHhGhm-A8XjCCPjawABAPiKhTbH3NNuiJ3v8Tw2VZp83mqG1IKWBGrSbt7tPpG5NcgWlr8ESYac0dOKazNdYb5Kd8T5SNRU_Vcfknr7r3Q0hEWQGjJfj1I-DGwwhF9KyEmSrm9LOyBvSckYtkvvwjlqLKuDbci-1wDhPtPynT7_HGCTs3DvpvMIUBntHTz_BSzdocePZeRo-WisVhKrY0NS9IxLE5TMmfuqYGOpXlbER6lb-Vy6V3VieXJvS1gW3oa5L4lKbM9DTQZ5-fB0Dmi7sxX7TMti9ZG5uNmIgzwP6FPgChY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
داش‌علیرضا منصوریان درحال یاد دادن ترفند سرمربیگری به اسطوره سندروم‌داون استاد علیرضا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106277" target="_blank">📅 14:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106276">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aa2c3aa1e.mp4?token=tmfodG9LIKfSl4s8ZgOtrqlphyRANXAaXPxxkfMqgz68c0rO2Aln7TTxxKUkTVL3gz5FIS4kfeSrL25sX53wUWDkIqJxtvM0aO3jXTnb6aDAfmgTQaTnAP2EV5stt5Af8ibGI2MGVUT22z5-gRr_eEpyAG2kpzH8Wl77w9u5GU1_CCY6MuEXEN3t-6cPiU5S_5Rhjpskk0UNyMrszYuUBxfFU2tLU1P1nq8ut-tqxtXarkSIcVeaC6KHpsl0VPA8rOnQ08TgyMEeoqVqH_Cd67pRaB4aFPziBySO_zKYbUerGzjOOzL4xPvshdjJshE30-dZqBQVxxU_53MaoxkU6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
دلیل جدایی هانی رامبد از هادی چوپان: اون مثل برادر بزرگترم بود ولی یه زمانی از من خواست پشت جمهوری اسلامی نباشم که من قبول نکردم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106276" target="_blank">📅 14:25 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106275">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkdtYwK23yGjgok9GeJpU2rYRHV0U8ZERIeiQKsS6OpPLZII4kAFXfRg9fgGBipBMK_DxBYnvJ9zsuOor3A_SxW1MNUWLbyyOTJd3peKBHg-sG78eLGShfgrAyfuRmFrluCi2AFg9Je-EloejLMhJxQs67UMSWvn8RcxWbtel27sO1ek1PoBQs2Egx8ySCG0rn78GaFk7rAJ-0p16a7bedqPsuzYi49zDJ8HHjpjSubQkCsUCQqJKJ4eAmwIr6VNVt4xYNze2hs45i73dlWHA4A55Rz46rzdx47wzx_tc1M_el6D8vTi-2Ck63oApL74eybPzEo3QuDyRZ6OqPxrWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات لواندوفسکی و دی‌پائول که درگیری‌شان در هفته‌اخیر جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/106275" target="_blank">📅 14:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106274">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4SuPig6yK8t3LszTfZMWGmiQ8bO-Ac0Qxh9ycVwPjGVb1QvHIGjgkqME4cgSDfbWTRBa2Gsd8owFQ6NZ9QLoDZNQ1dVLek3_k6Zay1Y8qG8aVGYkGdlnfBNEqpNQF5fOmz0206Aje6G1oqkTVQRtxmEGhi5-kqI-2e31sVEEys2sn5f02Obxjz4kk5UDMm31mzMJmPBUFTpWkYs8lN5NRv3wiIYxzzcvjGt2rNY4KJGXgdGs2Y3xaoTNiAIaENSaIhAiUU827cxzMnFnhSdymNB1VGkXhBjgPAIC-upq7KYLd0754cK5U_Jz13eGqLjzQrqWe3piQ_J6wMo1K_JOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
درخواست تاجرنیا از هواداران عراقی برای حمایت از استقلال در بازی مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/106274" target="_blank">📅 13:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106273">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bcc13d5f9.mp4?token=SovcbNbqfFUlyQMJrAypRhWb8q9FEGQfaA7PwvTL9-BbP2Zydhfgerc-aT3FsNKlpbT1oC4XVNOiW3lOL3HbMt_yxksueMQGaMUZzUZjX87kF5BgGVZd7r6siO18uf-PbVSpcO6KuHoQviwCD8xOVADBSwA3mslvuXv5xCk5R0TM_numMssSaCIsJS262FYlZY6s18_C3AMCPaAkulP2LrOpNM01vJaFjLW9Pah_Go9i4xPmlwurKO7tZjJV-xkc1BpdsjaN0Hccx-jZgzEutxoeAuRtUpeg1bbVryJSLQjbO_89cj4FJWerbF1MV0JXdfsqUzBqebwZf2yYsWy_34WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
محمود فکری: سهراب بختیاری‌زاده از دست صالح حردانی حالش بد شده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106273" target="_blank">📅 13:10 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106272">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFpeiqMFsZn1Q6zKBcKGqV_HpdP4St75VNstKAP77OsGYuIW2a3eRf4xGILiCT5OvdArEM4gU2O574zyDx9kHom3J-LD8_FHMcfPwGlgoPm9sn8L22vvHvlHWw5r3jq8BhyItKu-Tx38qK6Z1tpMQgtWjChiofYV1CXmnNUamDGU1hRBjUDPBUVb2JxhjOGMUxVeyPlmDthmeJgms763A_8dFR7ltMIN4xRfbL0Ligly3qWMRb8RrI5Plx_3o2SDTuwNhC6sIpkJF4LMCobuMgtXUKnSyVeTaMk0lud6BiOmimmRnUT7ANdnBpOzopPTqVaX94cY8XUh0cQ_KbBgpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
🏆
کیلیان‌امباپه: اگر عدالتی وجود داشته باشه بدون‌شک توپ‌طلا امسال باید به من برسه. درسته جام باشگاهی نبردم اما در جام‌جهانی تاریخ‌سازی کردم و این جایزه هم برای عناوین فردی هست نه صرفا تیمی. پس مطمئن باشید به خودم رای خواهم داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106272" target="_blank">📅 12:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106271">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_LYZMWXQOJ0mTG_13JQDUpK4DXOS_NZsV7I1fKY8cWViyD0jqitdmQwRSP_Zw_g8ygLtIh0KHBUe9d5-d5zS7ngncV1Dhisihm_5M4FNQNR_fTu4sAG8ZUlhKhjMbkOWGzU7Je-GWEkU2vMneN-Q80wUjwpj_bLXit1-ysCf-bbNyt1Bb66smnW24t0rb4s6bhfSvOY-71M_NYi7xAfpt9KR0EIogCAxmjZbUgjepZe0iLpkzCoGtVM5NjuBhyySO7sPA63wIodNCqaGzWbuxCgPYYsU2Ar716-5n5VqRRvckTkMs7L7s-9dtrpTk84lQP_XudrtS9v9eIDNUPj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
با رایزنی صورت گرفته مشکل پرواز استقلال به بصره حل شد و کاروان آبی‌ها تا ساعاتی دیگر عازم این شهر میشوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106271" target="_blank">📅 12:19 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106270">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92b41d0adb.mp4?token=M6E0zArPVsU7a5AMoyZu1VCfzdeoWFRloHyP8NM7POUYWtgD4FDbOXtRKkEjmjfI-OE0MoC1vdQrc6GHgBwJw-ZMHGO54b_2TV6b5KoliwQH-ZkxBIw-NFJ0eKCCn7rJcCEV1SBZLZdS5sFvW60Lc_fOEkhFl73835eFzi6JLYP36VeWSl8fc5nyKzXiy1vlFlUcamtkaMRb3B5s3qnXxyXoWSPtz8BSkZ-wvosP7WVcXv0L549Y4dLAGy1B6g0nIHXeec4QrnITgm_njUYclG-foA2eloE3l27hVK9S-AhsVObk5aXDDW6cixYiVH8wWJ_b3L5K3eSZbOC0jbGRVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
پاسخ جواد نکونام به سرمربی پرسپولیس!
جواد نکونام سرمربی تیم تراکتور در پاسخ به صحبتهای مهدی تارتار در کنفرانس مطبوعاتی پس از بازی با استقلال خوزستان صحبت کرد و گفت که «آنها از آب گل آلود ماهی گرفتند!» تارتار هفته گذشته خواستار برخورد شدید با خداداد عزیزی شده بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106270" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106269">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106269" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106269" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106268">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVUqGpsYK3zxLRfP0wqJspvY_pcf7Ud_RmUNzlYVA_cXHky69Mt-WFuNROfUpROEya4e0HsD2vXL4Lqp_arG6-agbDBmSuC3mvCcAZajVv1K2srYPn8WldU-VAtrk2iSn9WQ7fhVABElX6rGoDdYgVccfsK1UnUJE6ZsG_UVigE_37lszFLWzjmZTw02PNF20qYyaoIn4Gjhl5aELBrblr2fzWG42kGQwfsAwLTMgiJhogk2v2iRZ7Jjn8kwViNa9OyLKGByHVOCZY0csIWSwRe6oFXCvToqgDggiPhlsDT1OHAHlwNos98eSEDztRTub9qchrQ-RVJ9hJV0RN1xtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت‌بین‌المللی
TrexBet
پیش ‌بینی کنید.
چلسی
🆚
لیدز یونایتد
فولام
🆚
لیورپول
اورتون
🆚
تاتنهام
ساندرلند
🆚
آرسنال
رایو وایکانو
🆚
رئال مادرید
میلان
🆚
لاتزیو
کالیاری
🆚
آتالانتا
پادربورن
🆚
دورتموند
🦖
🦖
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب برای بازی‌های امروز
🦖
واریز آسان و امن از طریق کارت به کارت و ارز های دیجیتال
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/106268" target="_blank">📅 12:08 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106267">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/106267" target="_blank">📅 11:59 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106266">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=eSU2raGGBXmp4JM7UizmkqUK_yNwoA_mF1hshvktUpo0MdWJZYgK2n7L248xJGg4n2STfdeaxBf23mtJzl-v4h7x5mhihCw807VHhXed_frdParEh6x5AMxySpREFssqPma4AC8Ok-aDqZSIgUS5ul796UXTEDRaAFuMSHY5wyr7paF9JMO8ihZZEOdyQudvWg-V9ADNxRHssMx7t4txBHv4o9FdC5mjQZX_WQhG6IUChFZ8XC3VNNm75GfZ0mgdQ70vw7TAnNeOEZaVp_jl7Z2Hu19uumYx4rDuhPofF36d0WLWRwxAhKLHnBprG-P6VDRy6QEMHnkEFUIWlGKeyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d37095ed52.mp4?token=eSU2raGGBXmp4JM7UizmkqUK_yNwoA_mF1hshvktUpo0MdWJZYgK2n7L248xJGg4n2STfdeaxBf23mtJzl-v4h7x5mhihCw807VHhXed_frdParEh6x5AMxySpREFssqPma4AC8Ok-aDqZSIgUS5ul796UXTEDRaAFuMSHY5wyr7paF9JMO8ihZZEOdyQudvWg-V9ADNxRHssMx7t4txBHv4o9FdC5mjQZX_WQhG6IUChFZ8XC3VNNm75GfZ0mgdQ70vw7TAnNeOEZaVp_jl7Z2Hu19uumYx4rDuhPofF36d0WLWRwxAhKLHnBprG-P6VDRy6QEMHnkEFUIWlGKeyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚠️
بختیاری نویسنده و کارشناس اقتصادی: چند سال قبل من رو به سمینار دعوت میکردم تا اقتصاد رو با انیمیشن به رئیسی یاد بدم؛ گفتند ۳ دقیقه بیشتر نشه چون ذهنش می‌پره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106266" target="_blank">📅 11:55 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106265">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=KKtk7BK7bGkDg8gEwyBgWZ-8cQeI9wV4Pzk9yEgzc1qX_Ok7-pmypnaoxPyqJobDjk4d4noXsgNriWSC1AZ6e9XL04sHVJR0VTjsNwPKf1wKrCpaqYqxteD7mxmOa-0lgZ8_6y4LvkuqmzCOel_tsDsZ-6bA-85V1GlwwkF71YVO5Gho0_Bn14K01NYf8y8z7NS4LDIXxJVHDC0ucKArcPDqQQgV9c7Pj3-o7apypZ7Im4TVNCyPesKfz3_y17c2zPTRRywvdCYEwdxl52yge4l4AZ-L8mQpdXiUPxozfjqjSWdQphZLPULQKK6xcfDzBfD9jgXy9isGDe7j4MTG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe7ae3e84.mp4?token=KKtk7BK7bGkDg8gEwyBgWZ-8cQeI9wV4Pzk9yEgzc1qX_Ok7-pmypnaoxPyqJobDjk4d4noXsgNriWSC1AZ6e9XL04sHVJR0VTjsNwPKf1wKrCpaqYqxteD7mxmOa-0lgZ8_6y4LvkuqmzCOel_tsDsZ-6bA-85V1GlwwkF71YVO5Gho0_Bn14K01NYf8y8z7NS4LDIXxJVHDC0ucKArcPDqQQgV9c7Pj3-o7apypZ7Im4TVNCyPesKfz3_y17c2zPTRRywvdCYEwdxl52yge4l4AZ-L8mQpdXiUPxozfjqjSWdQphZLPULQKK6xcfDzBfD9jgXy9isGDe7j4MTG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
🇪🇺
🇪🇸
کارشناس چمپیونزلیگ: امسال نوبت بارساست که قهرمان این مسابقات بشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106265" target="_blank">📅 11:34 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106264">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=eKITosdEVTqIYJl16CkRV_vwrNkgNZUd3Apt5DCF46ahlyykrE_sgMPBCxrM-tTvozLFceUYI48C10ym57n-ZDlcFvVmAF0s2-ePrQXVwWBF-JcH-bn8qd_pksDumM33A9qjbbnLzxalh8I_xT6JTFFXfmwTcsaht-fo3aI0o64z_HAQHD3BDaJZIruBpiRP069SzLvSW8Io8Qe7ysBOOHGTJbw5RKP1zarZcb3mjclYVWlUq7b6ZCzhHndiK0rY2w9BSqJiw_OVhxoS9noKy4RQJ_dM96EwELRroTVrBQmyIQxvN1Kt81BAN4fJ-VafCoeNKWcLROgeXafcTzlwxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecba46a4ad.mp4?token=eKITosdEVTqIYJl16CkRV_vwrNkgNZUd3Apt5DCF46ahlyykrE_sgMPBCxrM-tTvozLFceUYI48C10ym57n-ZDlcFvVmAF0s2-ePrQXVwWBF-JcH-bn8qd_pksDumM33A9qjbbnLzxalh8I_xT6JTFFXfmwTcsaht-fo3aI0o64z_HAQHD3BDaJZIruBpiRP069SzLvSW8Io8Qe7ysBOOHGTJbw5RKP1zarZcb3mjclYVWlUq7b6ZCzhHndiK0rY2w9BSqJiw_OVhxoS9noKy4RQJ_dM96EwELRroTVrBQmyIQxvN1Kt81BAN4fJ-VafCoeNKWcLROgeXafcTzlwxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هیچوقت این دوراهی سخت فراموش نمیشه
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106264" target="_blank">📅 11:05 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106263">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=Uok2e6H0OzN_JIpGAKMfiGIQ_8ftFEfbMgLhkJuyeTuKNBGANJ4ID0L18ulRjvklsHfM38WTK--ydZty16KRlZYM1vY51dWu4oTBGnD5KAl5mYQMQU57NTWaPksPDPa4ogUK_TLD3HIObyfdteNJlPG5UTq4BsRxljAUg6VBt9OaIAUUmQNZVdlSxwXqwoaKMYOz3-YA18ZUCgFlFPaBmAYIL8owPI5XeAhEoT6BjUNg8-Ryz7a63WpnXlHedmRYBqOCLWE9AzQ24oouBPY29PDvQj66OZP2ByqeCWoeGKtv3zZFlNLtbRUEote3lzQtbaGypMPYY94eVQaEAxZBAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84d171b8e1.mp4?token=Uok2e6H0OzN_JIpGAKMfiGIQ_8ftFEfbMgLhkJuyeTuKNBGANJ4ID0L18ulRjvklsHfM38WTK--ydZty16KRlZYM1vY51dWu4oTBGnD5KAl5mYQMQU57NTWaPksPDPa4ogUK_TLD3HIObyfdteNJlPG5UTq4BsRxljAUg6VBt9OaIAUUmQNZVdlSxwXqwoaKMYOz3-YA18ZUCgFlFPaBmAYIL8owPI5XeAhEoT6BjUNg8-Ryz7a63WpnXlHedmRYBqOCLWE9AzQ24oouBPY29PDvQj66OZP2ByqeCWoeGKtv3zZFlNLtbRUEote3lzQtbaGypMPYY94eVQaEAxZBAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اعتراف جیمی کرگر به اشتباهش درباره لیساندرو مارتینز مدافع منچستریونایتد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/106263" target="_blank">📅 10:40 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106262">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=KHLy3JFmHYYZWf4Uj8A9_pz3HDWpeb8a_v2oUwzqGgEVd5GosXGBFMZM2DNFvbH5Jv7YUoRHMFWQMckKpJimTSPt5D2gUA70_pnDM-xeQUfvjX7jxBZf5fZs6MJ4i40JYYca8DcRbT5JMd9nz8lSaSJmo4XWL1EHd6FnpFO6PY-V1dSOVJona4BYdL9V9bm0Lk7yNsRAbhdue7pcricnx49pYDJOz29DqFcb-FQbJMOJYlzV8_1kseVctwAM8IfrE1G2zOBEBl2L5B9AUi7dOWnsyKXhZKcBanf667P6nTvhphOv_sMAnjkm2d40KlfQQex73OhrjNwJilgVmyGxkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d19807ddf.mp4?token=KHLy3JFmHYYZWf4Uj8A9_pz3HDWpeb8a_v2oUwzqGgEVd5GosXGBFMZM2DNFvbH5Jv7YUoRHMFWQMckKpJimTSPt5D2gUA70_pnDM-xeQUfvjX7jxBZf5fZs6MJ4i40JYYca8DcRbT5JMd9nz8lSaSJmo4XWL1EHd6FnpFO6PY-V1dSOVJona4BYdL9V9bm0Lk7yNsRAbhdue7pcricnx49pYDJOz29DqFcb-FQbJMOJYlzV8_1kseVctwAM8IfrE1G2zOBEBl2L5B9AUi7dOWnsyKXhZKcBanf667P6nTvhphOv_sMAnjkm2d40KlfQQex73OhrjNwJilgVmyGxkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🙂
جدیدا تو صداوسیما دیدن که مخاطب زیادی ندارن دیگه خیلی احساس راحتی میکنن
🎙
مهمون شبکه دو: زیر کونشون میزاشتن
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/106262" target="_blank">📅 10:18 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106261">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
⭕️
🇮🇷
درحالی‌که مدیر سازمان فوتبال استقلال دیشب گفته بود که اعضای این تیم امروز ساعت ۱۴ تهران را به‌مقصد بصره ترک می‌کنند، فرودگاه بین‌المللی این شهر تمام پروازهای با مبدأ و به‌مقصد ایران را تا اطلاع ثانوی تعلیق کرد
‼️
‼️
‼️
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106261" target="_blank">📅 10:00 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106260">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31134b7828.mp4?token=Fq8dcJYsfwKiFGVgCKxHoAtL-W3NmwxuMVyuUtVfRAp-MarHXIMpFcL8E8XBLXqtv_-her0DlPz3YLPEXRO0JdphHnPsFwZIxyQH4o65w070gdKwZNhqwwr2pDc1AJ_OI0TaY5yFIxX9CUOieoLtQ1OxtPKA9S5OiLqsPYdtzXAqBuNOT6UclIayoNca9ox6xpWnJ_alZtiVshq036euu-V0SOFkYyYzDCJfeYFgCQR1HCBP9yUTvkB768DYyW3ep98KmLlOVLMoD8ZnO7w-zrvrxAWZtliWd9wRlU8y73Krb3p1AlDfsTBCo-dTN7U6glnJkgiX9PP9Hzb1Pb3R-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31134b7828.mp4?token=Fq8dcJYsfwKiFGVgCKxHoAtL-W3NmwxuMVyuUtVfRAp-MarHXIMpFcL8E8XBLXqtv_-her0DlPz3YLPEXRO0JdphHnPsFwZIxyQH4o65w070gdKwZNhqwwr2pDc1AJ_OI0TaY5yFIxX9CUOieoLtQ1OxtPKA9S5OiLqsPYdtzXAqBuNOT6UclIayoNca9ox6xpWnJ_alZtiVshq036euu-V0SOFkYyYzDCJfeYFgCQR1HCBP9yUTvkB768DYyW3ep98KmLlOVLMoD8ZnO7w-zrvrxAWZtliWd9wRlU8y73Krb3p1AlDfsTBCo-dTN7U6glnJkgiX9PP9Hzb1Pb3R-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇮🇹
اولین‌حضور کومو دوست‌داشتنی در UCL
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/106260" target="_blank">📅 09:50 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106259">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=XO30ZmgWnoESPotfxuMlQUjbGE0nD6DxlY1B4zKD2CapZA2SuhHZFPLIv7lJakpLqbiAmxGotasQCSmjHXGgAQkA-6L687PDSTLrcCKT2MC8z40WJ5-0Ng5-_dAQ0uMKPjgdpPVtDo5hYpUtNbHsxpxTHF8oSmPgznpge0Bh1jQ_h3xBq0eyakKqTtFbhajdSaGwKMy56wrElrHnUXyO3zO48S6SAb6iBBVQb7AfXxJ7XuEsjy2tihCbA4Ef1YjMrOsKC5AQ_omiQDG8iT9S7JrdhQdOMg5utriMOP2QpMgYIWMS5_PD3nnlKwSgByN2Qda5VcA8u54Hj1Ru9-tpPDoUkV4cyPVuvR9WCnCql6Sxn3otoo8B_Pvu56KHIpImzDqVwvcJCztTH3B4pU4vAtdPZse5fjgcEQL0vlu3tj-D58NzSer6Z-e3TSwAYHqIPnF6e1OlBitZgUKc-6wvZYnIU5Xrn4Wpm17PDwyy51_YtdYnestBM67KSpMefmnaiGXVsEY3nOTV25CmOee4GsinGgSwFze0R77oI5X_YMP62IPWbPDAHMZFP2SucYIwo1db_i8I7wnnxolPyP_HnPzFKPvUtxkE8xKnqTFytl7D0TK4vnyuu3YQCmP7OEAMusOmrdc1fgm8U843DSV37Uc9eEvBHDBvycUUeRzadPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0128cf1a.mp4?token=XO30ZmgWnoESPotfxuMlQUjbGE0nD6DxlY1B4zKD2CapZA2SuhHZFPLIv7lJakpLqbiAmxGotasQCSmjHXGgAQkA-6L687PDSTLrcCKT2MC8z40WJ5-0Ng5-_dAQ0uMKPjgdpPVtDo5hYpUtNbHsxpxTHF8oSmPgznpge0Bh1jQ_h3xBq0eyakKqTtFbhajdSaGwKMy56wrElrHnUXyO3zO48S6SAb6iBBVQb7AfXxJ7XuEsjy2tihCbA4Ef1YjMrOsKC5AQ_omiQDG8iT9S7JrdhQdOMg5utriMOP2QpMgYIWMS5_PD3nnlKwSgByN2Qda5VcA8u54Hj1Ru9-tpPDoUkV4cyPVuvR9WCnCql6Sxn3otoo8B_Pvu56KHIpImzDqVwvcJCztTH3B4pU4vAtdPZse5fjgcEQL0vlu3tj-D58NzSer6Z-e3TSwAYHqIPnF6e1OlBitZgUKc-6wvZYnIU5Xrn4Wpm17PDwyy51_YtdYnestBM67KSpMefmnaiGXVsEY3nOTV25CmOee4GsinGgSwFze0R77oI5X_YMP62IPWbPDAHMZFP2SucYIwo1db_i8I7wnnxolPyP_HnPzFKPvUtxkE8xKnqTFytl7D0TK4vnyuu3YQCmP7OEAMusOmrdc1fgm8U843DSV37Uc9eEvBHDBvycUUeRzadPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇩🇪
عملکرد درخشان اولیسه مقابل بودگلیمت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106259" target="_blank">📅 09:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106258">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=Or28nh3MmCTLvES-kdNcfSmK8wEZMHNiG2Dhrt-NDwLcwROcpPBcausjWukr0yukTOLmuUmccp4v1Kn-DIG_56NYZdspUv8NMGDJQnnR2bMBbePZwOEItQw2F3n5n2Ovu0SCg4gWQp4uH7UEhGny2BPSW08NIyqkHZ25qgG2u4fMPo53s_5iEdUfdyspvFtLYNkkZRyc5-LF5mz1QwvvyoC0Cw4wzWVz2OzhkrD27Rp1nXE-Y85kjOlBh4Vi7V5BOqxw_tDmJp-kcZXPk87ooan5SWa3-G5NPa-P-hbNHsL7Tj2WeUSQ62RQ-_-dAD4O3ol0duEPy9kvTOg4q3KmPm4iDVLsB-K9kUbmEbHPAsECDKK00hlt8l0fzhH2MJyR3WuT46QkUW36ec_ZSwWnOaW8b9u8CA-wj6DP-K2pS0PhwegHRls26H_Ia6u3n--CpaOCD9JadsJaW1owew4iexnIAycCbA0H8S4wYjKYkqa3agNV0CM-SnXLzILPUH1DgnhSBSsFyZddbjwUbWiZ3zu_fGadPuUUI1GkyE0cnZHr9AqYVj_pfJuFWHbHCnX3ZKOY1FVK_FcI5qzB5Y5c8Xn_ppbeBtNxbeAWcpADnaXK3CAESKmRqGT8nVujyL-tpZD7Uy5Q-35YEMQH9NwRsgdkoZxNCRUVFAYF04gm7bs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a312ae120.mp4?token=Or28nh3MmCTLvES-kdNcfSmK8wEZMHNiG2Dhrt-NDwLcwROcpPBcausjWukr0yukTOLmuUmccp4v1Kn-DIG_56NYZdspUv8NMGDJQnnR2bMBbePZwOEItQw2F3n5n2Ovu0SCg4gWQp4uH7UEhGny2BPSW08NIyqkHZ25qgG2u4fMPo53s_5iEdUfdyspvFtLYNkkZRyc5-LF5mz1QwvvyoC0Cw4wzWVz2OzhkrD27Rp1nXE-Y85kjOlBh4Vi7V5BOqxw_tDmJp-kcZXPk87ooan5SWa3-G5NPa-P-hbNHsL7Tj2WeUSQ62RQ-_-dAD4O3ol0duEPy9kvTOg4q3KmPm4iDVLsB-K9kUbmEbHPAsECDKK00hlt8l0fzhH2MJyR3WuT46QkUW36ec_ZSwWnOaW8b9u8CA-wj6DP-K2pS0PhwegHRls26H_Ia6u3n--CpaOCD9JadsJaW1owew4iexnIAycCbA0H8S4wYjKYkqa3agNV0CM-SnXLzILPUH1DgnhSBSsFyZddbjwUbWiZ3zu_fGadPuUUI1GkyE0cnZHr9AqYVj_pfJuFWHbHCnX3ZKOY1FVK_FcI5qzB5Y5c8Xn_ppbeBtNxbeAWcpADnaXK3CAESKmRqGT8nVujyL-tpZD7Uy5Q-35YEMQH9NwRsgdkoZxNCRUVFAYF04gm7bs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
داستان جالب منیجر ایرانی مسعود اوزیل؛ مهدی کیا: پدر مسعود اوزیل باعث پایان فوتبالش شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/106258" target="_blank">📅 09:03 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106257">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106257" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106256">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r498LVChHQR6-qWIbadPFqrgpxPyySIGRBUp4vxqBXyyvxtNCdvV-N2_o2fmPgtC9EJs40xW3AGOMGeHA2KuQ9ASBNpdX4hJgMMkEJjgTN1QgPEdiX-ek-TzMHVrRpU5Y6XKecrHy-IKTYx6v0DwVO_hFfVgfJUC_e4NFGKWldyhM10kYz7qFgFVbV98qM9yuNXdNa2SI_PB_3xzd_h86389_0aBDUlJ-c-yXRBwAfJ-G-3s-GMZmWb6V-RQNb_9uYZYu8wXI18Dmt0Qy32lOwDSRbpc2OnWhgOYOKIU-uteA5tJUu7mnC9217bo8pSkFV5oa4G9QX4UGE1nAtIHyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106256" target="_blank">📅 01:36 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106255">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/106255" target="_blank">📅 01:35 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106254">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qIMwJ-CH7VBkUbh-6V5jHXg-4UuD8WaK1fcR2k-55e_9hIMBWkuvS0z3EpmhgULFubu58p7YAhuLNVpI3HN9K9-Eh2vMPfZh4zv17xZMt1uWezfr1l9dASHQn5ATy4CfP1hOeeKXmkhUoZKbHQCT58A3Do8DAYbsoxkzDzUjr1-O6OAE3gYgoUoh0oJkCwgrpzsbo4oc56cJ93XD2TbP34Ba2jgfhfaeSCUSa3XlGMVvz7JQEM81Z9PgNtiyhiRpAMGbSKI8QRYz81zbNjtvHblM2XYEttCE6BcIJxA3tuaOUO6NufngIm71J8BreUIfwM7fXdsUNm6d7DI_ssDT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
✅
🚨
کیلیان‌امباپه:
🔻
من سال‌هاست که خودم را بهترین بازیکن جهان می‌دانم اما اگر در مراسمی توپ‌طلا به مسی یا رونالدو می‌رسید، اصلا ناراحت نمی‌شدم چون می‌دانستم آنها چه بازیکنانی هستند. اما درباره سایر بازیکنان و کسب جوایز کمی تعجب میکردم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106254" target="_blank">📅 01:27 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106253">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taELzJesG_KrGKoTDvjY2iKLN0jIsnNIEB4BLt0Vd80ZS_6SCFaS653Sz-HBaGUA8zVzhL8mWARrBWsZl7prVQFXvvtoMdeh7ReTqpNw67xZwO_xPtw-5KiRcDGSqW-gX_EMMM7xA-bNmXb4qTTLMFOYDbm_uKYn0db_QczX7Vl7Q7Z4PFpsDZ7giD0Hl3fUcwA62b5GPTom2cpHw5YhaaUpkN1EL-_tXiu1JooFErqIUs3ggwJrwZTHCpve4ZbCyJl_k_-H3JW9IM6Kw3dHLANJyEug6hwR_4AJr4T67sh8GfyUJQ8NZAGJNkqplg1vyWeiMWCkp-yof8fuSwyMcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:  اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106253" target="_blank">📅 01:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106252">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEPYdnRygmPb_SI9vHd-JIlkUmzwTJGqtIix38C4T_lsi66LKunBF_9ox9ltVffcD6RsQW50aL2cIqkfXNVqfUmoPGp3hneURK9dta2pKdn0VYcl0dnuTPic-j1aRt2-FLaP7ba71DktEH-4lB_RJyrwqHeD7YFFKL5LYe_Sf7wrcJVG9VAhDQKpYoHFFOrmTSTYKhC-aoU4UyAzRr-oGvQAMAZvQkk46furFnHFGSAOFVNYwZw0YLcTMjCc6cjJZhO0sbnVacgQ9iICoIupVgS8Th_0sOhU3nBzUmAIk8UJHwQjvb_5qJDMqj8Rsw-xEhABwIFoiloBNbH6XxhV5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
آیا فکر می‌کنید می‌توانید مانند لیونل مسی تا سن 39 سالگی بازی کنید؟
🚨
🎙
کیلیان امباپه:
اگر لازم باشد، تا صد سال هم بازی می‌کنم! (می‌خندد).
🔻
آیا کیفیت من هم به همین اندازه خواهد بود؟ این به هوش بستگی دارد: اینکه بدانید چه زمانی دیگر نمی‌توانید ادامه دهید.
🔻
او نیازی به فکر کردن در این مورد ندارد، چون هنوز می‌تواند این کار را انجام دهد. ضمن اینکه، مسی خودش یک بازیکن فوق‌العاده‌ خاص است.
🔻
من خودم را یک بازیکن متفاوت می‌دانم. اما او هم یک بازیکن متفاوت، در بین نسل‌های مختلف بازیکنان است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106252" target="_blank">📅 01:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106251">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeqWccB6qdRvLayVOPK-LzrGxBxO2A4wtZcsx4RF4-3ajiUYJHZo2QiGh788Qd9OyQdpfNYKj85VRSvgo1ZRq7cuWHxc12bK5Sj1gkb3-_FVPGEhYEV5uZ8X8zRbvwOf-tPUWddwy4xK7Yz4_Nu8430Pg2SoTUbO7sWHOKx-uIg_jwLc2tVPB1jThospgBNiq7TUWo_STOM5E5TPK-gBF3iE7D6BfHXNlI0h1c23SyKi_bgsN9XOu55_FdnaIH90SiWkpXIoIwOpEoOGQypxqye6BGDqqu7JUbezDCHQUIUdgaTjj4nQo1pBZMcXCJ6DPjgjrN4TZCbEeLJ8TFN3RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😆
📱
استوری ابوطالب‌حسینی: ما نبودیم دیگه تو فوتبال حاشیه نبود و همه پاها موازی بود دیگه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106251" target="_blank">📅 00:37 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106250">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=Z8ZwANF5II1N7RFk8HZZhLSX6y4wR8Kf5w7yxzsJ6PZxpi2sILwBH975_gnSelV33NSa37k5hPhxUlfQ7bYFDtn2acLJrYzxFk-B63jiiF4tixehNcf2jcKvooKnB5g4WF2t0RaqzCcHtkLQH1_u_r9bAyIfp26eHe3yT36Y5kzi6fCJUk98WNYJ3Rpw4h9ej5KyLnCPi9r_JMmF3UxtyAFtnIoszpUTFB0J92yZSc6iDR9qa_J_Tl-Lv0T7xb1W98SBs1QgkfZymrlunOO-LdVIYZ_ZnDOO282pP5rDUikAO7F8XKzcLGYqCuPOw82XkA5Iv-ZzZdNexu0hjam6hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b4f3dd673.mp4?token=Z8ZwANF5II1N7RFk8HZZhLSX6y4wR8Kf5w7yxzsJ6PZxpi2sILwBH975_gnSelV33NSa37k5hPhxUlfQ7bYFDtn2acLJrYzxFk-B63jiiF4tixehNcf2jcKvooKnB5g4WF2t0RaqzCcHtkLQH1_u_r9bAyIfp26eHe3yT36Y5kzi6fCJUk98WNYJ3Rpw4h9ej5KyLnCPi9r_JMmF3UxtyAFtnIoszpUTFB0J92yZSc6iDR9qa_J_Tl-Lv0T7xb1W98SBs1QgkfZymrlunOO-LdVIYZ_ZnDOO282pP5rDUikAO7F8XKzcLGYqCuPOw82XkA5Iv-ZzZdNexu0hjam6hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز بازی استقلال و پیکان توسط تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106250" target="_blank">📅 00:22 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106249">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ki6c9qgAj0H2rpDsdJEHeXPxgEbNjYmf93wwkSsCKbtmbOZbIwMczr9WwwDhQuOfW-e_cCxzJEDXFH46CW82v1_iYadEWmRLpkwob89I2q1NJM7nPVIVJCUbCJ512B2P8sJT-drjtCpIvjDCqPslp2QZTp4l7wOQZJJl3ABfZ3wGZuSzLMaUGG7feCeYMWE-VDG-zRBqr8s6zfqIStLUKfDIddLw7Mn880pLL_9PMTL1s8PXGrEwzVvVqJiRNK1YR1EupmD4HFhfMQp-lzeqqkRKqVm_mpEcGjc0NNdriVeXOZBrL1T9izMLwxfsnCf1dCWwFJ0AJm0dultlX8guvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106249" target="_blank">📅 23:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106248">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjGstazaXoKp5Y-d9tc0GDxTpNDFlEXT3CIQ0W5NjcY95UvLkJLytOQq33JHcCVSCFymW4rE-0THox46N3w7qYe2RsIl82OHnL6UqiUqmmUFEzyMaMcP37eP9JkqVqW3sT4mxm7LTLV2v1JaaU_VVSXkJGxW95vRYSTMZwalFz6e-u41PS-bRQTAjqXWLZEbOxA17JUFgt75qCfKBK9ZLWnZ15VTgiMZQ_Ms3kUgdZzX9uE5tkkYs47YEg2Btgh8Ru5gVNNDPxN7gT4ym9Jw7FHcx1z3-i3qELtAm1SrKnrZRVyZ9rBov2Ls2gBO86bd6Ao4AB7UtHhGClFq4dd0Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106248" target="_blank">📅 23:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106247">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63b0b11397.mp4?token=fEDKzYoL8GrkjGh8NUnVUTrO0ZyF-0j15v99M-wJC9D0vMG6gXopDlbcFC48IO73XGVg81sqBNBGcghfZ27jPRmsJayutJie1JGN1Cju5yRercxS6NWVJ7XKmWw5EPbFyiIzmWIUQbheZM814T-aRNTSIYW3J3ZTUCi342cFeCl4UVuSPCJOdP02Fv3neBVPKrkUPW1N6pAl6Mqr3nfWPcWKUW2mzrYutgnYChS4T9-IorrM8Ov3bfcFttDgmfwquDUNaiHsT8BBpM0Fbr_JbgRmnfkMf8dvUTC-oA1tEoS0Wo63RbX1eKDoB44er3hu8uPSFxOemZ9O8IJrH4zONwagBmkBpaAgWEUoDhal_7A1HWbz5I4IrZxHNihuuiPuPdItH3gVWJy8V44ShMG09hnM5ppoCAUT64a4Y2f6lxfFy1xI0EZ0_19vifJWrXTf93PA-HKobB91DBalqyp9QZwsnIsbBCK0H6aVxcKDgAhvflDRhooig6V0fLj5FmZdA2awzi5jvMbMBwcmyo_MtdgPS8Xq6gecADT5ZmUCqpO1OnYxTJTSJK-poxsoef8Ewr1UOjyZiAoW7_yU_Zob-WjtZB8jj8rmpZDWLO07JSd1l3t_LecH2HryJyDru_gAQXnIIT2cjVZPhwR0_BgSwp-yer39U3CFtiIBSgRdw6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کنایه‌های تند وحید هاشمیان به حدادی:
🔻
حداقل درویش از مدیریت الان مرام بیشتری داشت و به نظرم برکنار شد چون من را برکنار نکرد. چطور برای اوسمار این چنین مراسم بدرقه ای انجام دادید ولی با من این گونه برخورد شد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106247" target="_blank">📅 23:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106246">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa1d2ea919.mp4?token=dhrOo1Z86rrTK9Trs_jZ8JUJEOrO0L5KWLfLAqUpbFirOWmDnRqPURi6g9c41Dx2WmA3Hxl4fPAb26lfMvige6Qjcd-NZD0xjQjfUIadT1K2cFettPNrVh1LmBC8l44UE3tf8qGd1a9yNEC9X1r7wl6GG_6IZrXGyfAK8m3wq394Oj0reCFjFEyzu8U88FJNnnlyzbBZTmgBgHQ5WkJpuJivdXqNDU8eW1nMTYfOAWeQ7ZSOcrofuoPlsxmDfkOeYecAOHXDJJezMoxmq1QdZIz6BxmkXxJj1X3JHkEQtO4gKMQ2wz_Ui_i6O3BuwVkbdOsNjG9Kmx6PExwq9sE1Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
محمد تقوی، درباره پیروزی استقلال برابر پیکان در هفته هفتم لیگ برتر گفت: «استقلال نمایش خوبی در این بازی نداشت اما باید این بازی را می‌برد. خط دفاعی استقلال آشفته است و با این شرایط در بازی‌های آسیایی مشکل بزرگی خواهند داشت.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/106246" target="_blank">📅 23:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106245">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=BRpeiL3-zrpwMGAo92VFKwfBdSZ4phZcs2_LEEDN1s0JjsuM1SW8rrZvNC_95W6h6IblauA6DcDfdbv2pdwNv6OnnoAaIl-nqj3lwLPPzebcm7FACURYpEWGDXg1lndy3jib1dlozCX0W_hGW0tCQJ8gOh_kgfb39xW2ZKgr2Gw7IC_jpZB6Ws8-pWSDu_BKVIF5Hc5Zts_UMtWCwImxZa1Ib7TmLpvx8GLJIXQVZ9QEA4l_g1VMiXwxF6nhIOgrLTxEIcu-HaUP0PBjJ4s8YdfPoQ-M8mH4ehtAqE5qlC2w5GT3ZwhXze9pJe5cszuv8raWvAqKsf6sR3uVzW3wXS1URrB-v82gz6-Ruh0_JkFS_zJPXyK92wePeUzyPYZLZrnkktkyhxu96knEB0lVCZu-iDdmuLIHEiBRhfKM53Pm2p3DYmTzyb9qrDQFVm4VRuHNsIMxXTMmYRrAdCcbmZSOK6x9iADPZV04ny_I8nZMgz2ksQzNlUXLJPxMV33LteidU0AVYMi4Wcrzgo6eUED6GbQWd0TXEi-ntq5TEKje4b2QaqU-vedch5sZ27PtiRm8YuLV_zDaRkiuzOhlgX4X5tw34irlvd8PV2gRs3J96gWC-MQ1HP2NNnxNFY0X5nQBhR_bxVn88lB5c58g6y89k3PNGd53eu57X9NTCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657c84dea6.mp4?token=BRpeiL3-zrpwMGAo92VFKwfBdSZ4phZcs2_LEEDN1s0JjsuM1SW8rrZvNC_95W6h6IblauA6DcDfdbv2pdwNv6OnnoAaIl-nqj3lwLPPzebcm7FACURYpEWGDXg1lndy3jib1dlozCX0W_hGW0tCQJ8gOh_kgfb39xW2ZKgr2Gw7IC_jpZB6Ws8-pWSDu_BKVIF5Hc5Zts_UMtWCwImxZa1Ib7TmLpvx8GLJIXQVZ9QEA4l_g1VMiXwxF6nhIOgrLTxEIcu-HaUP0PBjJ4s8YdfPoQ-M8mH4ehtAqE5qlC2w5GT3ZwhXze9pJe5cszuv8raWvAqKsf6sR3uVzW3wXS1URrB-v82gz6-Ruh0_JkFS_zJPXyK92wePeUzyPYZLZrnkktkyhxu96knEB0lVCZu-iDdmuLIHEiBRhfKM53Pm2p3DYmTzyb9qrDQFVm4VRuHNsIMxXTMmYRrAdCcbmZSOK6x9iADPZV04ny_I8nZMgz2ksQzNlUXLJPxMV33LteidU0AVYMi4Wcrzgo6eUED6GbQWd0TXEi-ntq5TEKje4b2QaqU-vedch5sZ27PtiRm8YuLV_zDaRkiuzOhlgX4X5tw34irlvd8PV2gRs3J96gWC-MQ1HP2NNnxNFY0X5nQBhR_bxVn88lB5c58g6y89k3PNGd53eu57X9NTCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇶🇦
کامنت‌ هواداران پرسپولیس زیر پست‌های السد: قرارداد آسانی غیرقانونی است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/106245" target="_blank">📅 22:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106244">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=CxpS9aBvpVx5Rq6_xSMgIwllspyQVHhw4WjREXOhyGNGR__jlSva_8VCguOxO3yQ5z1Nl5861x5_goNXtZ97g59najykwyX97Indy_XPVIfGwlW6cEZsMOkGYOWIf5gs5w_4lF8jcp9CejJMkxaQ88y8VtjG59BphORhpxOpt-btEMd-iBZ54GdqQvYvqY7zqRRhhNq1Os7Fj8_J8sjNPJQYI-OKWO3C1SJTiYR8qnr2rNu2whCUNMA-39ZLtfyvxecJfaSFaOE7cf7tjbQauqPVWbxQ0YgtjjLVNVXNao5E8z7cEoBBh-kHIT_hfr8_BPySI4UcZxJOmRd3NHjbcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9444ed9ae1.mp4?token=CxpS9aBvpVx5Rq6_xSMgIwllspyQVHhw4WjREXOhyGNGR__jlSva_8VCguOxO3yQ5z1Nl5861x5_goNXtZ97g59najykwyX97Indy_XPVIfGwlW6cEZsMOkGYOWIf5gs5w_4lF8jcp9CejJMkxaQ88y8VtjG59BphORhpxOpt-btEMd-iBZ54GdqQvYvqY7zqRRhhNq1Os7Fj8_J8sjNPJQYI-OKWO3C1SJTiYR8qnr2rNu2whCUNMA-39ZLtfyvxecJfaSFaOE7cf7tjbQauqPVWbxQ0YgtjjLVNVXNao5E8z7cEoBBh-kHIT_hfr8_BPySI4UcZxJOmRd3NHjbcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سعید فتاحی رئیس سازمان فوتبال استقلال: به غیر از خلیفه و گودرزی در نیم فصل هربازیکنی سهراب بختیاری زاده بخواهد باشگاه استقلال جذب خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106244" target="_blank">📅 22:46 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106243">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=vh-5zYWB4cXzETlo7Cevrzo8pUHSb6KEXHGFmKKJ_6LyMupAhEMYHW22NRLcfjJvY5tc-hiXGb4XauHP-wAriGTbeZt2pkJk9kY9csfy6YPGmK0ogm4eopIrcAaTkKNR5c30UDCBw2iA_4a_OmZCqzPwaNcBIY4EfOipQt8boGNC41WHAllqLD-yILG3UvlyD-YmsaalA4AO8uuxEM_e_CUE5YSmCMWe58tWC7NODVWk_iTC_cFKTUDj66QzGEade55nIFsmkBek5c8gqfFoiKbuaRR5DllcEZNk-3bCg7oZIEbu68qZBVcz0qZjRMvUFkSkUIFLZd12Snz7NelVqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dab1b117ec.mp4?token=vh-5zYWB4cXzETlo7Cevrzo8pUHSb6KEXHGFmKKJ_6LyMupAhEMYHW22NRLcfjJvY5tc-hiXGb4XauHP-wAriGTbeZt2pkJk9kY9csfy6YPGmK0ogm4eopIrcAaTkKNR5c30UDCBw2iA_4a_OmZCqzPwaNcBIY4EfOipQt8boGNC41WHAllqLD-yILG3UvlyD-YmsaalA4AO8uuxEM_e_CUE5YSmCMWe58tWC7NODVWk_iTC_cFKTUDj66QzGEade55nIFsmkBek5c8gqfFoiKbuaRR5DllcEZNk-3bCg7oZIEbu68qZBVcz0qZjRMvUFkSkUIFLZd12Snz7NelVqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
🎙
نادر محمدی منجنیق: به صورت اتفاقی این نوع پرتاب رو یاد گرفتم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/106243" target="_blank">📅 22:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106242">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
با اعلام باشگاه استقلال، مشکل مصدومیت یاسر‌آسانی جدی نیست و این بازیکن برای بازی روز دوشنبه مقابل السد در دسترس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/106242" target="_blank">📅 22:24 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106241">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=jYSxwaZQOlEs0ChdnZ8rfCGpt9ebJ3a9G5Xy2L53Rns-pevZtkflk_N_21Kj6lXKX6mofKz2zg1Vc0RohRv689sVFczp0Jsi8xWg3Brt_CohFav0n2R1B_OeB7TDFULUgvh-Cq2aRTyxbEkVgUz158Qzuz_6j7hNtMZFPQ60EfL_WQVvT-Jah0oMYlnBsXUJBjQmAHfofZ5ORHJgid3haPSEgt6pVHKiUHvw8nJ7KwWO1K-0jgcgfoxS02GZo9ye2mkg_0mqqQEamrsVJHdtz74fxodotoThWSIMFZl5y64SUmQukpOGxeWcpLk6eKQaZeqE1dXazexT7DZYSwD40gBvPN3DtCmgScm4UeARFxlc-vycW30KPDGRAQzYdfl-H6z_LY5uEJQ2hefCi2h97fTl9Ssoii06cvUzxM4VXaul-dwRSIScXkGufuM8NnO_NslC8lJhLB1EXm6tg4DdoiwSa8jlRqmzwZofxUwKLuvCz4kiPj7AevMVvJS6FRd2Zcdgv7U_uFUV92onOObwZIAA96um8DpI4xfAZw19VdbVr4TBFRB8sfFtiGihoXFRzMr13bDgJWg4Ain0ulVOXcFIapGEQL_-L_yB7qQxhI54lOXjNO4SdVofwU6T_K3ejkRYibVO5hTMY2QKKQ6419LVZL-fFhBLrD5JwBqKfIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e3e40e30b.mp4?token=jYSxwaZQOlEs0ChdnZ8rfCGpt9ebJ3a9G5Xy2L53Rns-pevZtkflk_N_21Kj6lXKX6mofKz2zg1Vc0RohRv689sVFczp0Jsi8xWg3Brt_CohFav0n2R1B_OeB7TDFULUgvh-Cq2aRTyxbEkVgUz158Qzuz_6j7hNtMZFPQ60EfL_WQVvT-Jah0oMYlnBsXUJBjQmAHfofZ5ORHJgid3haPSEgt6pVHKiUHvw8nJ7KwWO1K-0jgcgfoxS02GZo9ye2mkg_0mqqQEamrsVJHdtz74fxodotoThWSIMFZl5y64SUmQukpOGxeWcpLk6eKQaZeqE1dXazexT7DZYSwD40gBvPN3DtCmgScm4UeARFxlc-vycW30KPDGRAQzYdfl-H6z_LY5uEJQ2hefCi2h97fTl9Ssoii06cvUzxM4VXaul-dwRSIScXkGufuM8NnO_NslC8lJhLB1EXm6tg4DdoiwSa8jlRqmzwZofxUwKLuvCz4kiPj7AevMVvJS6FRd2Zcdgv7U_uFUV92onOObwZIAA96um8DpI4xfAZw19VdbVr4TBFRB8sfFtiGihoXFRzMr13bDgJWg4Ain0ulVOXcFIapGEQL_-L_yB7qQxhI54lOXjNO4SdVofwU6T_K3ejkRYibVO5hTMY2QKKQ6419LVZL-fFhBLrD5JwBqKfIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
✅
🇺🇲
بررسی حادثه ۱۱ سپتامبر از این زاویه؛ برای دوستانی که اطلاعات کمی دارن دیدنش توصیه میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/106241" target="_blank">📅 22:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106240">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=RdxGaFifigSklmFm3Mub0hL6EkIMyRETB7yWmU-tJqLsRtKyNFo0Oy9GCNPxlnbpIcuaYQu2xd_fkxNxt83EwaE3v2pqsV-3VeSxy0bviNTsJwoZXrHMfUk1w9caBAbaXg1yIkZujVp-7Yf98HDMVnDKKJZ7xxGvaszSuFMsS69BXcbSY0xPj5meu0gFtlFP9Mmx4vbteHJx-_gzZEdZDoodFqDjLtr0iXd2WooOrYtC0OBWjZ68XaeZ02TtOFBT1dWeVHsUByRy_Sj9C0o9oMxH_pJf6y7Wk3JbOGMRqj2cum1Shs4x7k9PyQHlLBz5GmDoH_kAvkNlXF0wijiR7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16ebf2050a.mp4?token=RdxGaFifigSklmFm3Mub0hL6EkIMyRETB7yWmU-tJqLsRtKyNFo0Oy9GCNPxlnbpIcuaYQu2xd_fkxNxt83EwaE3v2pqsV-3VeSxy0bviNTsJwoZXrHMfUk1w9caBAbaXg1yIkZujVp-7Yf98HDMVnDKKJZ7xxGvaszSuFMsS69BXcbSY0xPj5meu0gFtlFP9Mmx4vbteHJx-_gzZEdZDoodFqDjLtr0iXd2WooOrYtC0OBWjZ68XaeZ02TtOFBT1dWeVHsUByRy_Sj9C0o9oMxH_pJf6y7Wk3JbOGMRqj2cum1Shs4x7k9PyQHlLBz5GmDoH_kAvkNlXF0wijiR7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس: چرا می خواهند ترمز پرسپولیس را بکشند؟ چرا می خواهند حق پرسپولیس را بخورند واقعا این شائبه برانگیز است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/106240" target="_blank">📅 22:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106239">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=FZuv2kvB6PjLkLiZm9eXgRl2J2Y8mzJnE1cs_6mSQSZOOmDzaqoqD_tTlfmP2q6rs0lS9YAaJFplohvXjF1vXFZCCiQyMiPBrkjpF6V97BathDXKs0HRzGxGzFnlnXh7hofhW0jejj9RF_YQUzAp78U2vtA60-eaWo1RJVd0sfCxlgQmIhafINDfGVjlz5l-v5acChL1LxVElONwr2J9M-9jTJLevNmm3vFfVxWbHdYtIaRa8vTBv6B6i3rOFYOEKHK7hvYFVYLfNGa1fx4LAMYLU8RojSfje5jV5jM0k-ZK9l6f9yZdwjDTabLJeEEOMtQPEm_p5eCDwU6rT2pG5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/febf5e7a8e.mp4?token=FZuv2kvB6PjLkLiZm9eXgRl2J2Y8mzJnE1cs_6mSQSZOOmDzaqoqD_tTlfmP2q6rs0lS9YAaJFplohvXjF1vXFZCCiQyMiPBrkjpF6V97BathDXKs0HRzGxGzFnlnXh7hofhW0jejj9RF_YQUzAp78U2vtA60-eaWo1RJVd0sfCxlgQmIhafINDfGVjlz5l-v5acChL1LxVElONwr2J9M-9jTJLevNmm3vFfVxWbHdYtIaRa8vTBv6B6i3rOFYOEKHK7hvYFVYLfNGa1fx4LAMYLU8RojSfje5jV5jM0k-ZK9l6f9yZdwjDTabLJeEEOMtQPEm_p5eCDwU6rT2pG5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
محسن خلیلی مدیر پرسپولیس:  2 تیم ( استقلال و تراکتور) با تیم ملی امید همکاری نکردند و بازیکن ندادند چرا کمیته انضباطی با آنها برخورد نکرد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/106239" target="_blank">📅 21:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106238">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a557a62450.mp4?token=hrg4tR6n6zG331GCbsH7cyUYqCydinkJj65JGcriD7htJnb-ZshMlVNiMn9vf8yYdc6vWWSYj0lLIpcSVb0z-5nxPIqkdG-6Ph6eHuBOlSYVuLeBFjLIfBueGkZYB7obAmTLnfmY9B-Rk45fNSJF4zdXZcS7XpogJFImFEnfi4E9UE_HiHeEgo6cZNKvweFdSpNqFj7auLzslnCNEETHCspF8UjSZV_94wso546nHf6hhhwyWXh-1UA_y485bc6IStcvelAAB2jCu1MFFZ4vUdcSjIaHWS4wXwFbIRgdb1npfOjiNI9q6TpeRKhTN67mIc_ybJg32UeKP1etGBVYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a557a62450.mp4?token=hrg4tR6n6zG331GCbsH7cyUYqCydinkJj65JGcriD7htJnb-ZshMlVNiMn9vf8yYdc6vWWSYj0lLIpcSVb0z-5nxPIqkdG-6Ph6eHuBOlSYVuLeBFjLIfBueGkZYB7obAmTLnfmY9B-Rk45fNSJF4zdXZcS7XpogJFImFEnfi4E9UE_HiHeEgo6cZNKvweFdSpNqFj7auLzslnCNEETHCspF8UjSZV_94wso546nHf6hhhwyWXh-1UA_y485bc6IStcvelAAB2jCu1MFFZ4vUdcSjIaHWS4wXwFbIRgdb1npfOjiNI9q6TpeRKhTN67mIc_ybJg32UeKP1etGBVYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینیم دیشب در لیگ قهرمانان چه خبر بوده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/106238" target="_blank">📅 21:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106237">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQxreP3tQQs1nn6-12aOpKhgHSgjtNc3nKSXF2jvUe98qGH83mH7Irg2FOGHiqnmQMhiozLDP_v3e4Rvtc0y1nf_AMoYvujsaNvAww1apNUvOE7tZ9mTqG8EBGZ_71GP-oNS29gKVqCXHJhQExmzA8upFCC0uMlzXQxOnjFMqTJhF4C6rqug3-cGQGhgDcxWW0TC7Y_w7qWRP_YxMQq7aVyJ8W1fTi24P0d6s9crqov5LPrJ3wOnRvjlDDx66E708c7RK0iMBDT2S7uaZt4-7BLT__HnUwwD5QJnKIFCWZB2jVFHHl7wXqffOVt3ZcUOUZK9VGY_GtRmAs0uvOOqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇮🇹
🇪🇸
سسک فابرگاس، سرمربی کومو:
🔻
«بارسلونا ترسناک شده. سطحی که تیم در حال حاضر داره واقعا ترسناکه. بازی دیشب رو دیدم. فاینورد تیم خیلی خوبیه، ولی بارسلونا کاری می‌کنه که حریف ضعیف به نظر برسه، چون در هر لحظه راه‌حل پیدا می‌کنن.»
🔻
«می‌تونی مقابلشون نفر به نفر دفاع کنی؛ همون‌طور که فاینورد سعی کرد این کار رو مقابل رودری یا پدری انجام بده، اما بارسا از هر نقطه‌ای راه‌حل پیدا می‌کنه. فرقی نمی‌کنه چه بازیکنی وارد زمین بشه؛ سطح تیم همچنان خیلی بالاست.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106237" target="_blank">📅 21:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106236">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/525ed46310.mp4?token=bP90rvtY9iDFT6sF84Lqmfolq2bb-0Vxzk1_1O3WpPm-CfdKHn54bdPKcxOH_PTeDMz2Z2QSOd5aHF5t32qmHVWlvVo9L01_O1pN5PL-t7FITB7IH8V8zGsiF7rRgP73Fx9mgbtpcP0R7iudvzNJT50doPUdzQdOWKl3NX_fHgJ71gtKEAi8DA_MD16N2aytcbfJevGxBvVY-OK2pzYt3WMvEl8qygex3zG6N9CCGLZuWOUbtyNgaCFW4pNZTEgxM8xsgv3iBBvd117AVRiHWZp7jMDIOdWKkFH3VxO97S0w-9Ox2o8nUJbLdehqiq5qGM_H-gLxBOW8OMz2A49b-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/525ed46310.mp4?token=bP90rvtY9iDFT6sF84Lqmfolq2bb-0Vxzk1_1O3WpPm-CfdKHn54bdPKcxOH_PTeDMz2Z2QSOd5aHF5t32qmHVWlvVo9L01_O1pN5PL-t7FITB7IH8V8zGsiF7rRgP73Fx9mgbtpcP0R7iudvzNJT50doPUdzQdOWKl3NX_fHgJ71gtKEAi8DA_MD16N2aytcbfJevGxBvVY-OK2pzYt3WMvEl8qygex3zG6N9CCGLZuWOUbtyNgaCFW4pNZTEgxM8xsgv3iBBvd117AVRiHWZp7jMDIOdWKkFH3VxO97S0w-9Ox2o8nUJbLdehqiq5qGM_H-gLxBOW8OMz2A49b-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😳
😳
😳
اینارو از کجا پیدا می‌کنن
😂
- کارشناس صداوسیما می‌گوید ذخایر طلای بانک مرکزی ایران ۵۰۰ میلیون تن است!
یک ۵۰۰ میلیون تن و یک ۸۰۰ میلیون تن دیگه هم گفت تازه
😂
حالا جالبه بدونید که کل طلای کشف شده توسط بشر در طول تاریخ ۲۲۲ هزار تن بوده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106236" target="_blank">📅 20:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106235">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=j-sHJQTr_efOmBXVVdJ2FuCHMkEhtQpWRy8nY9e58L0lCrc6PV_UddKytrbXgQBl5rLEejXUSsvqhoA5HHjwqjQTPAsL7PZ5K92tPevHSz9NOh70HEsx3l4ktJQUMiEEPD5KI34S-7xbCDTnXjw1lKZp8-BbkZZsZs2bv6FWnYwi-77YF2mlRLYTA0mn-nZBUHn9RXBxpaGM7UuVNLiSokuIZttIrLCC5o3Vda2WNFyoPXhOCG6DMfR3PCvCykOlfVTG8x9mJ1Wynixx8zwgDZNUPqdiKb-1LoCjt2a_TiBVmVgIX0eKMCuDwA8dkosQtmGnqnntsbjZfYOZJF3tsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e059f4f8a8.mp4?token=j-sHJQTr_efOmBXVVdJ2FuCHMkEhtQpWRy8nY9e58L0lCrc6PV_UddKytrbXgQBl5rLEejXUSsvqhoA5HHjwqjQTPAsL7PZ5K92tPevHSz9NOh70HEsx3l4ktJQUMiEEPD5KI34S-7xbCDTnXjw1lKZp8-BbkZZsZs2bv6FWnYwi-77YF2mlRLYTA0mn-nZBUHn9RXBxpaGM7UuVNLiSokuIZttIrLCC5o3Vda2WNFyoPXhOCG6DMfR3PCvCykOlfVTG8x9mJ1Wynixx8zwgDZNUPqdiKb-1LoCjt2a_TiBVmVgIX0eKMCuDwA8dkosQtmGnqnntsbjZfYOZJF3tsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
فراز کمالوند سرمربی خیبر: الان که پرسپولیسی‌ها مخالف هستند 3 ماه پیش هم که پرسپولیس اصرار داشت تورنمنت 3 جانبه برگزار شود همه مخالف بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/106235" target="_blank">📅 20:07 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106234">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6dYFF8_dwICEj3-HGvSWCGsK61F7SoqlY0IgiEhnAqf1XwrYAqZxXA5Pm3QaAOd34ddkOaJG66sIwwooRL0qSeH1lBfGzOjVRFFBzn3asgs_n_LXoJLhCC-406bLzMOiuAJaTBmeWkM_kznPq2_7eg99h81teICxon3szmkWOCpFG9tyYIBbyweh2NDGuRp5f1yhSsdfZa9R7CTntHeQ62ltvAul7Qkv2me1MCcJpBomdDsFDrCAFp3PaEPTjGpLS2YYdj41CqP5DY-DK9h2NEn92kDWug4zQJt4VFinmqtNXjWoqiS3ofI_y7qs4R2xoE51WQkEq-566IjM2mLog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسین‌ماهینی عزیز و همسرش
✅
🔥
👍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/106234" target="_blank">📅 20:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106233">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=n18ofzj-4cckQApSdENXMO-64JEIyPzVhJD4oH4hPpO8cZPzGS-hfizhFEdqKKYO6hn2479OpawL4cnAhJj8UAayEi5Xuni8TWfzQQ-hd1y_kGnnoXX2ngCnnZunvMfLcb4e7uQbNSvzYvdLoAVgSsHgp4SWT6J__akZ1w3RiZrbsQfvm3IAkp5KgZ99RFTbC3q3NHyWykRReVzOgES5ZlZZDZubqeaTKxW6ZDtv_Rgw6Kaaqncc1z4Xs0kv-2-qbX7Qj438pvK3IHtrqxAI4RqG3inbpZzIlmaf3LqRn0QvRm1eN_F4iQviIO7rVQgyGfnGrtQYoeGRvP0dJyCRBpKJj0t4yVI1FkIyLeqpJvyRCMe5OwkMCh9W1s6flr0srxTln0QWRVNuu0MZeiTEMJjGxoyMCMGPAIDlxI0Ar2QnrPalxmXu_mvIpGsh8x6lFY1RTNNIhuf6ovgxGiXwKFsziRJaVpVJ2cMPmY7YfSIzqWNIR0W6RkvdqAa97YlW0vmc6Wmvvph6om9X88GPdF6bWiBEgxrRp5oq-7_gtlV0ARBS5Nl7JQZ3O8G7JwyFlDZn5JnIRMe-qpRyEDW1ypMmFvto1SBIdUVfEcv37dQc65fhpDPCq5NXm3HKimTT9rHJO15xSH5EjVBzoJ0UcIQVEowiB-1V1QQXMjJ7t24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d8215d3c.mp4?token=n18ofzj-4cckQApSdENXMO-64JEIyPzVhJD4oH4hPpO8cZPzGS-hfizhFEdqKKYO6hn2479OpawL4cnAhJj8UAayEi5Xuni8TWfzQQ-hd1y_kGnnoXX2ngCnnZunvMfLcb4e7uQbNSvzYvdLoAVgSsHgp4SWT6J__akZ1w3RiZrbsQfvm3IAkp5KgZ99RFTbC3q3NHyWykRReVzOgES5ZlZZDZubqeaTKxW6ZDtv_Rgw6Kaaqncc1z4Xs0kv-2-qbX7Qj438pvK3IHtrqxAI4RqG3inbpZzIlmaf3LqRn0QvRm1eN_F4iQviIO7rVQgyGfnGrtQYoeGRvP0dJyCRBpKJj0t4yVI1FkIyLeqpJvyRCMe5OwkMCh9W1s6flr0srxTln0QWRVNuu0MZeiTEMJjGxoyMCMGPAIDlxI0Ar2QnrPalxmXu_mvIpGsh8x6lFY1RTNNIhuf6ovgxGiXwKFsziRJaVpVJ2cMPmY7YfSIzqWNIR0W6RkvdqAa97YlW0vmc6Wmvvph6om9X88GPdF6bWiBEgxrRp5oq-7_gtlV0ARBS5Nl7JQZ3O8G7JwyFlDZn5JnIRMe-qpRyEDW1ypMmFvto1SBIdUVfEcv37dQc65fhpDPCq5NXm3HKimTT9rHJO15xSH5EjVBzoJ0UcIQVEowiB-1V1QQXMjJ7t24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
آشتی جالب هواداران نساجی با مجتبی حسینی سرمربی تیمشون بعد از فحاشی اخیر به وی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/106233" target="_blank">📅 19:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106232">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dG7nkUU1MTSgzzEMzSXeCOtkA50NbKlNNVF0h76mDRhU5mc0lbt0gIBcW9trx1ZeyorAMqZFMrX7qlavpmDOr2ee5f2AO1Z_qJNlqL9ozTjjWf_IYI7O9eEanbaQkZFGj7kClth9UdIdv-ykeJ-YYyGQOzUGJB0cayUCZeqHM64UYMudOkN2BZpnkYRC79LHHfqSTTjpvjHf43ZZDVPKUwbcKEM1vEQ-APHExTl4yRGo_EXOKWe94NXAIYL4WgiVjl5In-Dw8PrV84_FUCrCU4RyC0TzjMgVexxv0ZYFGrQO6UoLeG5PyBrRSMDCI4i3ysuzP3T59LWgUIODaMKDBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🇮🇷
طبق پیش‌بینی‌ها، یکی از پربارش‌ترین پاییزها برای ایران در راه است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/106232" target="_blank">📅 19:16 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106231">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=N-mJBwjTCLSe1elgMQWGp1kwSgwBVpumzlJHjDQ68qhYtRKJvG4MKl9Hl-vznzpUwKtumlnnZmktKbKyRxVDtyhShrbttVB_JiwdbEV2_KlplEOd0UP_vfjX2TZFwl8CokwCuQ3Y_Q7ZLBhSOx8whboOgEMdq2q-NsjFcM1bawYRnrUUhYnpML8nI7mjTVu820TiSNq6Tqj3lTsjfpJVK5DP7_TsJxBHG8u3tkxrRzIJ8kq2IrdP30UiQWjkxIzg-05CNGVedA6fimJAt-etICVUnqE3L6m-23EIBKMn7jDj3tzm3KwIakEtm3Tyyd7_H4UskOkMf3oj6pJxfdq-gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be84e2f3d7.mp4?token=N-mJBwjTCLSe1elgMQWGp1kwSgwBVpumzlJHjDQ68qhYtRKJvG4MKl9Hl-vznzpUwKtumlnnZmktKbKyRxVDtyhShrbttVB_JiwdbEV2_KlplEOd0UP_vfjX2TZFwl8CokwCuQ3Y_Q7ZLBhSOx8whboOgEMdq2q-NsjFcM1bawYRnrUUhYnpML8nI7mjTVu820TiSNq6Tqj3lTsjfpJVK5DP7_TsJxBHG8u3tkxrRzIJ8kq2IrdP30UiQWjkxIzg-05CNGVedA6fimJAt-etICVUnqE3L6m-23EIBKMn7jDj3tzm3KwIakEtm3Tyyd7_H4UskOkMf3oj6pJxfdq-gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
به مناسبت سالروز واقعه ۱۱ سپتامبر یادی کنیم از همدردی مردم شریف ایران با آمریکایی‌ها؛ این درحالیه که کشورهایی نظیر عراق جشن و سرور به پا کرده بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106231" target="_blank">📅 19:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106230">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbVv6lQ3mn8nnsQqTD_VZQ-JIgGEK0CVLpcADGNd5-J1iJMl2ec252Pv3-Pbq9ccMQa0hRqNcfKHcbI2nob13olDm0UY54jp6tF-yco7g56PZC66Ili_Ga7YYvSPIqtA5wolwwZovgPdBrTkSc28roIUMM9Ar18NceKHvjcK4ET0Tfb4DEnxXslKSGmJPajnp-kseishbGdVntexBo4hpDNILQXwbt5zV10-YLCXl5XlKc7wFBXjsgGW3t_7DE_2Ybn-JoLqhOnL4CzlLirBCKUafIqlVVyoXl1crOcAUJTHieLprtitNcrqbtGUnBaJqeRXkxb1Dqf7CvGqyIN7yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
👋
گئورگی گولسیانی مدافع سابق پرسپولیس ‌و سپاهان از فوتبال خداحافظی کرد. گولسیانی زننده گل قهرمانی پرسپولیس در لیگ بیست‌وسوم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106230" target="_blank">📅 19:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106229">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNY1Zu12PEL0oXa3U2qt-ywPFA0vVehkNjZRfKeSWcbr7630Pz6GVj207XpQuS0YIKXX59EydzGb3-AtnD1oRCGP3IlBrMLwjxs4QxBAbYtpPlCVulxz-TEv-U5rrnNUVDWay1z8CM1eRL1QTg7TK2qb1ELtPShfLihm8RTFGwBXrK5cFvh6LYoaiy9I2teU-Fi9bBpX42IHbi0TeTZbEpwOHzrsrn2IEqJV0Boar3FKFT6nG4n7dD-C04BXrcAfru2BfVNjkdYaOl8hUfg2RYW8uhJoXdX0zFhpTodgtVjyg6FiP7nDXoAX-Dx_-y5JgmFyUdlwQJ0yH-54LT0ogQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🔥
🔥
🔥
اکتبر خونین که در پیش‌داریم!
🗓
🇪🇸
🇫🇷
20 اکتبر/بارسلونا - پاری‌سن‌ژرمن
🗓
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
21اکتبر/آرسنال - بایرن‌مونیخ
🗓
🇪🇸
🇪🇸
25اکتبر/بارسلونا - رئال‌مادرید
🗓
🏆
26 اکتبر/اعلام رسمی برنده توپ‌طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106229" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106228">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106228" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/106228" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106227">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQlAcTF-2WC5RnNpAvAP-Jm91xi3cSl_uGfIVGEeNGP-6mRFIGs1ufXvyZCsFKevU_up92F3vMfj_x5sF-Z_i6ewWH7qyk8BNkGOg5knNkGLPsIUXQlxpCwizBXz6wIzG65DswHoOjfnx6eCcmXBwQ8_L-nIp6-fvz1AblXO0eTRqd_xQxeadILg6mAzMSo_55NNqBYmAZFvjaDoSID4Epj5qerM_asRGxmFjuDwbuAivsxgIYPElFDMYMal8nDN3DEHFzGGfCYm2DSyfxDsl9ERIKqthgSXjUXdaG94rXl7iBfE0-CreTfJSgqrlG4gL_N3zNcBK2j-hr0G4R-HjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106227" target="_blank">📅 18:43 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106226">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S25csdP_-KeaDw8JzTU1Lvxi5-cb63IzSJA3Sbx7aFSd63DX9BqZO5w-n7NNlEIwTf_-kb2tp7xD_6SypvrnwqWixaKBx7m0jjxliHtJGj-nrG4AT5c67746lhSbwwUDzjj_Rh_EkchYdZGsIzVxhcj0zYbg_MgLaF2Bx9NWyaJI04w8F8dwcmeUGTaQm9iIdFFG01mVMBD0GiQ4vb9AFnSIxr6fP_Z6Sy0VDsE_KqTnLYhQjjyp1ePcDR8XrzaQJbRTDDKXTj0vIp3Ip3RkNladTsWLL8xHWoxtvMIhoeiRtSEbPPqGQefT4j2H9tEhY1wxGwIHrqug8qUo8Zk4bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇪🇺
تیم‌منتخب هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106226" target="_blank">📅 18:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106225">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=HSgfNz8MD5Mjw7Cbc4ETyKHUa-4-RdXV0d0e8CoCE4lTqdomZSWygcFuz4pXU6GBDsIg8AA7BTu2UUz4GJAThQiktrUXHojeDr15MSCMiiJ6VoHEIYDMsNk67JKGaeS4-9oZJqj_9YPUZOfXFjGWG6tCMkA-h3OAd2We8JAlozj7hvH9yB96sVXtyQs4rt7tmZuY9WcXIG7dLQzn-XdgoNUCzupl5W80TxTyVdQzdPHokrLN697ofn2frPw-W4wFcBrI7fPnSlN7mXIlPMolJGdEE5EGzCfnJOEys3OTNocFU2teAbnJbVbSlM5L77FeixpDtcUGwq9LbSemvBWmQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1c6bb479.mp4?token=HSgfNz8MD5Mjw7Cbc4ETyKHUa-4-RdXV0d0e8CoCE4lTqdomZSWygcFuz4pXU6GBDsIg8AA7BTu2UUz4GJAThQiktrUXHojeDr15MSCMiiJ6VoHEIYDMsNk67JKGaeS4-9oZJqj_9YPUZOfXFjGWG6tCMkA-h3OAd2We8JAlozj7hvH9yB96sVXtyQs4rt7tmZuY9WcXIG7dLQzn-XdgoNUCzupl5W80TxTyVdQzdPHokrLN697ofn2frPw-W4wFcBrI7fPnSlN7mXIlPMolJGdEE5EGzCfnJOEys3OTNocFU2teAbnJbVbSlM5L77FeixpDtcUGwq9LbSemvBWmQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
پخش‌صدای بانو هایده در مراسم هفته‌مد در نیویورک آمریکا؛ روحش شاد اسطوره
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/106225" target="_blank">📅 18:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106224">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=FytpDzL-nea63TzHrjABIDnbc59Ofyk6HzfU2SeKa-zKvblw2Zo_y-TIipWivXNliFaQCs3hkwjVDZT0cs4XeJ7chFdRGSQG5BhP0sV6YnjfdTHG44qtFMnsahpmrQWoEr-m4nnrCyzNfhuj6Bia56guv9gEPKndOJtZ7tXJy44JvWFDd_H7FiPzjIqnwFvxagJGynhxG3x0po0Z-p6xtjJ_Dgodkd6SbuiSD_lLjy0jhvkwgJFAd-PdsvH2e8cMq_boteET0G4b5PupXlwgq09u0V5bsQVkJQzPAg8Mbc-ixmJNoQ6LhxmAi7SHp5HofnMmyglnp0BlCmgUu41Q1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8904bfcc25.mp4?token=FytpDzL-nea63TzHrjABIDnbc59Ofyk6HzfU2SeKa-zKvblw2Zo_y-TIipWivXNliFaQCs3hkwjVDZT0cs4XeJ7chFdRGSQG5BhP0sV6YnjfdTHG44qtFMnsahpmrQWoEr-m4nnrCyzNfhuj6Bia56guv9gEPKndOJtZ7tXJy44JvWFDd_H7FiPzjIqnwFvxagJGynhxG3x0po0Z-p6xtjJ_Dgodkd6SbuiSD_lLjy0jhvkwgJFAd-PdsvH2e8cMq_boteET0G4b5PupXlwgq09u0V5bsQVkJQzPAg8Mbc-ixmJNoQ6LhxmAi7SHp5HofnMmyglnp0BlCmgUu41Q1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🇪🇺
برخی از اتفاقات هفته‌اول لیگ‌قهرمانان اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/106224" target="_blank">📅 17:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106223">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=qGITXHK40P6MRdYwDhvprKN-nspLrW1oYdK_zvr7xDjHdUlz3hwbAVS-Z965Uo3jsCwFjBLNM2-pB00jWn7w3FmOvYw5OYrC_k1FpftS93tpiDUo_u5sx29Mhcnna4Bja_9nJ37-fezQE7uRrJ0Epgd_EuazFsUrXub4IFUU98v8abY5f-OHhlrFF9VwmEFXZM0eSl-CBnRrcp4BPydlvzApje4OnKOx5C2zotawYa6G3Rdll-W2hJh2aHCvzH0nOLkULMrsB1HOKVHD0oAkeVii0TVB_mkFTHnUNbAZhve50r-BgrWnVcj4JSGVGDJR0508MoxwagjG40-sU32rOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3be86e9eb1.mp4?token=qGITXHK40P6MRdYwDhvprKN-nspLrW1oYdK_zvr7xDjHdUlz3hwbAVS-Z965Uo3jsCwFjBLNM2-pB00jWn7w3FmOvYw5OYrC_k1FpftS93tpiDUo_u5sx29Mhcnna4Bja_9nJ37-fezQE7uRrJ0Epgd_EuazFsUrXub4IFUU98v8abY5f-OHhlrFF9VwmEFXZM0eSl-CBnRrcp4BPydlvzApje4OnKOx5C2zotawYa6G3Rdll-W2hJh2aHCvzH0nOLkULMrsB1HOKVHD0oAkeVii0TVB_mkFTHnUNbAZhve50r-BgrWnVcj4JSGVGDJR0508MoxwagjG40-sU32rOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراسم تشیع جنازه بابای مسی با علی‌آقا دایی
😂
🚫
با صدای کم‌گوش بدید فقط
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106223" target="_blank">📅 17:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106222">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhWCIzCX3vcbjZWTK9oq0aMiqSBO9wtmvRuQbfD9vHdOYj73Q3WZRelc64-cje6eNEOlR8JX8E7EgRA2Daco5X2ZkQHY-EN_3XK3IAra7Mqd4yWS1jCxGyQ9zZHB2LsvQ_Lak4Np7t3J1UdIIgnVT563vMWDmvlEyPB_B1lB26iDbmH1fNtnInILG857YkfyOfMWrm3meokmMOzyn0X-zDBKCwa9ARnY75WqAUJ1-2baVv4f3qWogppGimXUp--jkh42Wzu5SktYLlGA26e94pUEyVEyLYs5AMBapE_ZDnbSBb26uXq5Iyv-vpqOcGVDjL7YQ9R82NxkeTLxEXmTbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
واکنش علی تاجرنیا به بخشیده شدن صالح‌حردانی توسط بختیاری‌زاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/106222" target="_blank">📅 17:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106221">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=gZ61r0-2tr2H4LkhqJ9au3Iu0Syo2Pd9DK9NIBSDr28mEWbPckYJLGIXS4dXKsQ8Jt3DojYOmR2nMwc0rwzHfUg7oIRT43ZjcSxgx9vnGc7Db4OCZgBtdI01wsXpktTuUc7xTpEln4CBAipEc6M6M2QOC7bygt-guNvydUd7z6WVJNxLC_CbGJ-OZ0LXHSL2fNjQ9NNLY9u_xfu7Yry2eRnBTZ5OBP7JWzePVCs7Rh1rrhSrErLr3Ueenn0Wrbq2z-9651XfpC8WnEzX_pcEM7MmRykTyaREKRF7r2wZrXToODo5io20z39CeswnrCICDM9A59-W7zjlMvPfUKOFY1r7NIGEYJcRQa9JSVIwmIS9mr7-iNwxR-R55z1xkXd-v5jtd0b_bVcMRoJM8LLvoigOOkGLe_euRWEs9tMH7NdeBqp7-zoi4KhWNdsjiuZdujquVQyDTrZ9p_UAEl01Xk2TWKOQIvuAxHg9D-ObC1Hly7hq8rb_3iSVGI24JpmZvwmr8eFaPo4fqKjB8Ojlbc64Hu-RmdhFOt1-YDzjSEMdWfYmynYiT_egzlPoMgIUQ4q9yPpJ2lZMcrvTm1t4ghoSlZT0NCn8NgD2J3uBiAVdsyDDLqmgdK7HGSxIO6sdzZS3Y-rJ0IOpkt2DjmZ22RNy84e4DF0wVeeqULW1-Vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d24125c19.mp4?token=gZ61r0-2tr2H4LkhqJ9au3Iu0Syo2Pd9DK9NIBSDr28mEWbPckYJLGIXS4dXKsQ8Jt3DojYOmR2nMwc0rwzHfUg7oIRT43ZjcSxgx9vnGc7Db4OCZgBtdI01wsXpktTuUc7xTpEln4CBAipEc6M6M2QOC7bygt-guNvydUd7z6WVJNxLC_CbGJ-OZ0LXHSL2fNjQ9NNLY9u_xfu7Yry2eRnBTZ5OBP7JWzePVCs7Rh1rrhSrErLr3Ueenn0Wrbq2z-9651XfpC8WnEzX_pcEM7MmRykTyaREKRF7r2wZrXToODo5io20z39CeswnrCICDM9A59-W7zjlMvPfUKOFY1r7NIGEYJcRQa9JSVIwmIS9mr7-iNwxR-R55z1xkXd-v5jtd0b_bVcMRoJM8LLvoigOOkGLe_euRWEs9tMH7NdeBqp7-zoi4KhWNdsjiuZdujquVQyDTrZ9p_UAEl01Xk2TWKOQIvuAxHg9D-ObC1Hly7hq8rb_3iSVGI24JpmZvwmr8eFaPo4fqKjB8Ojlbc64Hu-RmdhFOt1-YDzjSEMdWfYmynYiT_egzlPoMgIUQ4q9yPpJ2lZMcrvTm1t4ghoSlZT0NCn8NgD2J3uBiAVdsyDDLqmgdK7HGSxIO6sdzZS3Y-rJ0IOpkt2DjmZ22RNy84e4DF0wVeeqULW1-Vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇪🇸
یک‌دقیقه با کورتوا بهترین گلر فعلی اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106221" target="_blank">📅 16:55 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106220">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=eo8LEHvgf_P3NloMLusgBSszZ62JJ51qTKEw9UKwDl5P_H7a--uswt33mL0UvicieGExeGHdU647Dzdk2h35_htXPM7SApUncoQaRnmwLvlVdLPymIM6ZQmnkMXRVXPqF4URXlB0-DE3q4VvONrkL1tFtKYmgngtOBwiCtvktRISl0Ux6OxHh1pDPqH5PICHtmG1ijd6Jsbo3kpzU7xcYaqf12O7096K0ByMr1GS10Gs70KXJcWMpiz53_l5KeacASQl-aBPFTj5Uz-5S8dveNKXGpmqHgRNClS5M_e7RUBhiAJOm0OkGILElOVi8z2mzc-dCSHeUt9oqKhXnriwH6P7rZw0bp_Sc3JmdEX22B7beIkKjmrvyyTcdaXVrRRBCTfSVm8BlRxd_1p-sH2Bo3H8gy_9HEQ6cnRJqI6SibyPJg2_Mwx9-MGmu3-ADkv0290g3AkgcdW23F6h6voL2ef8NNlBxOsYMgJl2kHLz7tqoKlPVhz01x4FX6xUDErHJUodxy8DriDsyWkO9VsP2mCrFL92FqOeWMrEe84w9Yf2h70MXNhjHJKLtaYASGhog4jN0-JQ0sETwhrkYYBzneBxFiLtwTXmN6fezUPRRcOSfZ-nrrxsH44lu9DlcvsmMBh3eaGsX7IY4dqlHT08Icutl_x2PWTIAHQiSwfqOHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0df98090f.mp4?token=eo8LEHvgf_P3NloMLusgBSszZ62JJ51qTKEw9UKwDl5P_H7a--uswt33mL0UvicieGExeGHdU647Dzdk2h35_htXPM7SApUncoQaRnmwLvlVdLPymIM6ZQmnkMXRVXPqF4URXlB0-DE3q4VvONrkL1tFtKYmgngtOBwiCtvktRISl0Ux6OxHh1pDPqH5PICHtmG1ijd6Jsbo3kpzU7xcYaqf12O7096K0ByMr1GS10Gs70KXJcWMpiz53_l5KeacASQl-aBPFTj5Uz-5S8dveNKXGpmqHgRNClS5M_e7RUBhiAJOm0OkGILElOVi8z2mzc-dCSHeUt9oqKhXnriwH6P7rZw0bp_Sc3JmdEX22B7beIkKjmrvyyTcdaXVrRRBCTfSVm8BlRxd_1p-sH2Bo3H8gy_9HEQ6cnRJqI6SibyPJg2_Mwx9-MGmu3-ADkv0290g3AkgcdW23F6h6voL2ef8NNlBxOsYMgJl2kHLz7tqoKlPVhz01x4FX6xUDErHJUodxy8DriDsyWkO9VsP2mCrFL92FqOeWMrEe84w9Yf2h70MXNhjHJKLtaYASGhog4jN0-JQ0sETwhrkYYBzneBxFiLtwTXmN6fezUPRRcOSfZ-nrrxsH44lu9DlcvsmMBh3eaGsX7IY4dqlHT08Icutl_x2PWTIAHQiSwfqOHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
واکنش مجتبی‌پوربخش و علیرضا مرزبان به تصویر تلخ دستفروشی یک‌دختر خردسال در استادیوم اراک!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/106220" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106219">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fdir6fSgxvxnJCVU86hG3ZtH3INxjK80hLfgo4McPe9Ue1YCaVJgvZzDRbqJ7H8dD2fzs7Qr8MronLLM3AShWZsjtfpBP1-mt07SRdIb9s55BF_yYoh93wYqV8w__LHyX2ShvYT7fhq58dN96V8AEKJ-WbDxvBJXmBdky8FQ092qY1hCBXUEvGquoZq9RGq7WFsFqAaoBB6IBDESHH_RYOgkcET3rU6fxOh6UVUDmwbRaliv9pA5b5IjWuvTh7hpeAZ3FOu-CrPw6gq3Y0NzACPFJxgwYwO7-UHukeWt_9y7YWgyUh5ykc_3u8Ygq7M5K-qu1e-X3s1uO2RZ4dDAyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
‼️
📊
🏆
سوفا اسکور: مقایسه میانگین نمره رافینیا با نامزدهای توپ طلا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106219" target="_blank">📅 16:05 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106218">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DwaOdHxjhU9wS2cYZBg6Axj12ubsv0pmixpMNbovgi7uqxU3zJYnJ9Us_GXHUu89VyxuqsEGyIJ7YKexvLCHprXURa_AdJwb2o5lPZ9VGmPrp-3uFw0jWesyg_MNZ5okjY_iUjKjDPYVXbJatqB8mfSAVfTGi-eYkZbAyzle6RXXbiggkkaaw8yy7G0bfbYq-1tvIMoTgyNrWpO62Y-ifrER0FoRhtninWC0KDPteWYOskJgpemr41ktMMkEomEs9HQnyGYql_uJS_F00LP8blEUbBi_Hqj2HlMREjpfr-BVtJrr_x_I-mG_6W4QifLQZzfI5QJb5NJhZOeVJgWHuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🤯
امار و ارقام لامین یامال در کریرش
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106218" target="_blank">📅 15:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106217">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=gsdAkRq0wXglrqrWmiWP2sfYW9UbcQYPOHtG6GsZZgJHuV_3KXaOl7CPvkHwEnax_xA9z95RobMYZZMCagmN02tMCjwEIndVw_v-9sVd0I5Vx0NFCfLqxlaAanaNdqkfMc2lREcjESg-tgDNe2VXiww383DJVHjqvl1wYigpufMrfiIGIVltghQttLZ-AJoB5VctEspkL62SlSfWnGOSsgMJUBFJAkYKVyRgcZbSKLeW06FwLgBZ122B8KWDRAG1ZChri7fboG79US9nRYIqO8XLALJ0KEM1-gsayeW5tJyQGlpMOa5Jw_FFxbOT0Y9zVqXYhPS1QRCtTjavvCkMIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88e638c5ef.mp4?token=gsdAkRq0wXglrqrWmiWP2sfYW9UbcQYPOHtG6GsZZgJHuV_3KXaOl7CPvkHwEnax_xA9z95RobMYZZMCagmN02tMCjwEIndVw_v-9sVd0I5Vx0NFCfLqxlaAanaNdqkfMc2lREcjESg-tgDNe2VXiww383DJVHjqvl1wYigpufMrfiIGIVltghQttLZ-AJoB5VctEspkL62SlSfWnGOSsgMJUBFJAkYKVyRgcZbSKLeW06FwLgBZ122B8KWDRAG1ZChri7fboG79US9nRYIqO8XLALJ0KEM1-gsayeW5tJyQGlpMOa5Jw_FFxbOT0Y9zVqXYhPS1QRCtTjavvCkMIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
از مالیدن روی آنتن‌زنده و صحبت از قناعت تا عروسی سوپرلاکچری سامان گوران مجری صداوسیما
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/106217" target="_blank">📅 15:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106216">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=GcJRmyVu3WTZsqd_pIJxxHoJwupAe5-ULZIdWcmZyhkIHY5A-S16MLXAVMlNNKqzTDCvof5uzZxu9c8yd69Inh_KWKONthiuQadO3IAXkbrvXabobZuKeeFOAOQTH6Jle728U5tbuzgleDRlwQDiUJjAzVaoj_8Cx3X07W_pc0qHmQrj6Vn-aRsVH6cuItkBiRJcVUZzjLtuy9uc3VXuipMX8mgv-AAX8bcMjUGmXtof1B0Xef6E3pErPsk6WeRVLLvpZzpv_5EvNz3qDzcryWZtToJGGtuqeU9fH1iOs62xV3iLAOaPmZboL2qXwE1ZtqQjql0L04Q4oQDADgXkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/225d461ea8.mp4?token=GcJRmyVu3WTZsqd_pIJxxHoJwupAe5-ULZIdWcmZyhkIHY5A-S16MLXAVMlNNKqzTDCvof5uzZxu9c8yd69Inh_KWKONthiuQadO3IAXkbrvXabobZuKeeFOAOQTH6Jle728U5tbuzgleDRlwQDiUJjAzVaoj_8Cx3X07W_pc0qHmQrj6Vn-aRsVH6cuItkBiRJcVUZzjLtuy9uc3VXuipMX8mgv-AAX8bcMjUGmXtof1B0Xef6E3pErPsk6WeRVLLvpZzpv_5EvNz3qDzcryWZtToJGGtuqeU9fH1iOs62xV3iLAOaPmZboL2qXwE1ZtqQjql0L04Q4oQDADgXkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
▶️
حس‌واقعی هنر در ایام‌قبل از انقلاب با حضور ستارگانی نظیر بانو گوگوش...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/106216" target="_blank">📅 14:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106215">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Phxb1dVFW1jHYpc6W3u-gFuagB4fg7eJWRkVTwfQcB0xodxA48Fw2zb9bc1CNQvXLBSx-AHgUKWVe1WQuDn8Xw0mnRXoHRVBrTtcO1YIHvMcGyWW4aVo-A8JlRAhO9eTRCXCVReZiiRTicCYdbvxmJ9F_uXtwOYtLwHjKpN-altemzQ4DXEWCi-gUzaWEplxy30-jz2akdDsvhxoIX8DXAxMpkSm2WqRQcAyrTKP1s0en2tb7RUqrVO9SlpE_CkwkNZ0jOUWiSYXUojoub6X0dqe9dpSs99EO85sUlUhk5JUyONGzj_NUYCD1alu5q7WbSm_gDbuMm2N4Vwnw6mxjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
💥
🇪🇸
عملکرد فوق‌العاده رافینیا از شروع‌فصل:
🇪🇸
الچه
⚽️
⚽️
🔴
🇪🇸
بیلبائو
⚽️
🇪🇸
رایووایکانو
⚽️
⚽️
🇪🇸
والنسیا
⚽️
🇳🇱
فاینورد
⚽️
⚽️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106215" target="_blank">📅 14:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106214">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=QcrwuAQPwCy_h_zYVtG2v89nNYgv25veUQ18V9JhoBux64fAOA02Lj3K5l-cWN2zaEKnMFUgXKPFJVQc5CTYWlPAIPjwV2VxSp9vbSywyJts4k56N55X6IqNPDPEFeivKzERIYnjjGW85OcIDPLj16nA-eMmHccy-wEap2EPiu-BX0joseHOKHshdzumiRnTaRlQ9BTvKoaHql4NPKbQtiJOmmATHSfoNasuOoFtgjF7TacS3uDIjnGhNcBserMwSiritWwqf8qxB2deR7PwNfWawmXRSCYH9EqbGBjjDC_fEFXBb4ZC20qWf4MDhsIuT4srrnaJxgUNEdYbjP7lbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e2cd36180.mp4?token=QcrwuAQPwCy_h_zYVtG2v89nNYgv25veUQ18V9JhoBux64fAOA02Lj3K5l-cWN2zaEKnMFUgXKPFJVQc5CTYWlPAIPjwV2VxSp9vbSywyJts4k56N55X6IqNPDPEFeivKzERIYnjjGW85OcIDPLj16nA-eMmHccy-wEap2EPiu-BX0joseHOKHshdzumiRnTaRlQ9BTvKoaHql4NPKbQtiJOmmATHSfoNasuOoFtgjF7TacS3uDIjnGhNcBserMwSiritWwqf8qxB2deR7PwNfWawmXRSCYH9EqbGBjjDC_fEFXBb4ZC20qWf4MDhsIuT4srrnaJxgUNEdYbjP7lbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فرمین یا بلینگام؟‌ کی بهتره؟
👀
⁉️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/106214" target="_blank">📅 14:01 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106213">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kpp7Vl9delx3_HelpprzBfj1n15zBk_GlKTSGnOnyYRCJP9t2O05lcFNy9htBeWji9xsBv6h-px0q2xh7xNC7URzhNPSlaFfsfRlBZDZfUkoMzXLJO5hP0o3FTGfPaU4qPS_hVH-PXPgSqp-OnrdjCBq5Wr00_h75XaKqha35QjJ9fEeghfJuegzuh5Z_7eCrmFx0Uf0Kzt19f8N-bPC73QahYzB3rbAn0EifC1Oe44ea1XnYWke7BC8vV-m0WoxcVLJotXpol5-o07NKFs05MpADRjqkEEmOO13KXZOwK272TxioPzxPkdxkxH2Vi0yCp9Mu25dBTtj8mtDPV53sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد درخشان مورگان راجرز در چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106213" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106212">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=byR-r-vFA2R6U0tkAigEpTQfufHAbi5bhjwsJnR_bcvrbiN85n43xc0j3BRlwqJV30bJMDzWdeYaXDusv2yvgSmWR9EmfvgjtieFF8_Ocgpoq-donMmbhk8qNjLqHCFH-ZYheBMwj3rHejMF6O-HYEqiaPQR4xt1eNybxvwSWuB5kKMSJPZWmdKD8c8u_avnTPH_LZGkfAkT6g5VIVHMk0ZgbztDV5ewnUNioabCYaHMxnQjgbZOC4et5a_rYZ1866MDmLT8vDcrTRqvtJt1Nj4H21ExmySKTLYekPcihdbpMMgnK2GcxxcK6P3g6e9tQR4AK7ewfx1RnAd8cIn5qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4258e2b29.mp4?token=byR-r-vFA2R6U0tkAigEpTQfufHAbi5bhjwsJnR_bcvrbiN85n43xc0j3BRlwqJV30bJMDzWdeYaXDusv2yvgSmWR9EmfvgjtieFF8_Ocgpoq-donMmbhk8qNjLqHCFH-ZYheBMwj3rHejMF6O-HYEqiaPQR4xt1eNybxvwSWuB5kKMSJPZWmdKD8c8u_avnTPH_LZGkfAkT6g5VIVHMk0ZgbztDV5ewnUNioabCYaHMxnQjgbZOC4et5a_rYZ1866MDmLT8vDcrTRqvtJt1Nj4H21ExmySKTLYekPcihdbpMMgnK2GcxxcK6P3g6e9tQR4AK7ewfx1RnAd8cIn5qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
ویدیوی وایرال شده از تجمعات شبانه:
«تو تاریکی می‌شینیم، ذلت نمی‌پذیریم
بنزین رو کم میگیریم، ذلت نمی‌پذیریم
دلاری گوشت میگیریم، ذلت نمی‌پذیریم
مهریه کم میگیریم، ذلت نمی پذیریم»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/106212" target="_blank">📅 13:10 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106211">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=OnPHhXJui7aeGcxuOXH6FPVhSlFMVvVtzcop_H0LDArHsIO7Y-DMR-y_mg9K5kPUKuT3FmL-cpx5GtUYIXoKyonq_GqX2orV1XJq_LbPbFLm51D3MlYFhmR7FNw63YQrKoGEXbiZTKAP6CH55zVFghSVstW3X1h3qW4Yi27vKzaCSMwevPXMgcnzz3kexqr5vMVEfKpDKwJRF1OcWlbyrTfrRptJIi1tLGR7K5xlJdaQV85UN182sxOen3J7k56WkxFlmDquZ0urtP5o7FDKnAHQSRrtQetxReHb136H_2UO5QuydmMrYKlycqOtMZj8BDdyx-fepbfDCS2JXN9pTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62e4095a95.mp4?token=OnPHhXJui7aeGcxuOXH6FPVhSlFMVvVtzcop_H0LDArHsIO7Y-DMR-y_mg9K5kPUKuT3FmL-cpx5GtUYIXoKyonq_GqX2orV1XJq_LbPbFLm51D3MlYFhmR7FNw63YQrKoGEXbiZTKAP6CH55zVFghSVstW3X1h3qW4Yi27vKzaCSMwevPXMgcnzz3kexqr5vMVEfKpDKwJRF1OcWlbyrTfrRptJIi1tLGR7K5xlJdaQV85UN182sxOen3J7k56WkxFlmDquZ0urtP5o7FDKnAHQSRrtQetxReHb136H_2UO5QuydmMrYKlycqOtMZj8BDdyx-fepbfDCS2JXN9pTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🙂
🇮🇷
نحوه برخورد شجاع خلیل‌زاده با مدافعان تراکتور: حمال‌های بی‌خاصیت
❗️
❗️
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106211" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106210">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106210" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/106210" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106209">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdAGnFDHO7dLb-Sh4eErj833hg7EpbMyAq0-I1_LEir3t2tmYXT7zWeq2EKRiINrBIm562bPHTj9Vi-yyFM2eZAz-UeeR93syia2PIFJARvk8qrL207__Oizv7xhDick6nofOPX5hWCYP1eAZmb-PPRw03mZ8RACyw9rqoveMjy1Fs14k0wQIVsabI475hgL6HI0X07s2e3obx5T1wrK6HzixR6IeaXau8U92tCuhrPO03fa_aY7RoTTgpMZYo3znSAYtTXBsVucZtxpKox8Mdu4mxoWHtDUtabL7roYWK2tX1TbbZXky7gnQ22QFjU_SupLl3rlEhVGCjxL0GGWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/106209" target="_blank">📅 12:44 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106207">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👀
🎙
🇹🇷
اسماعیل کارتال: بمولا از ۵ تا بازی اخیر تنها یکی باختم اونم جلو بشیکتاش بوده. تو پلی‌آف اروپا هم لیون رو بردم و به مرحله گروهی رسیدیم. نمیدونم مردم دیگه از یه سرمربی چی میخوان. دهنم سرویس شده و قصد استعفا دارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/106207" target="_blank">📅 12:38 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106206">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46400b9012.mp4?token=e0eIJxY6p7jB7jPpbN4eEgPtx8zxYOHRUvEtJxCtogSFA9BysbbGIbbcEuLT7AgOcZ78L6oadN30w7pHZIT0PLvQ4unGDsPxdnYCXNSg1lLRNhN88-6QY4AelaOuPfLEuAytO27UfXJdgdAj0UEbrI1XHtUEvHMK5TigGlMVdNaNDvusc60isEASR-EsFi0SrQkMiZLZYv5_nE0CqNPT1IwvoBDCT_Mhd2m-CJ0zU400rHpuD10HRe7iAHTdqum5P7Yjf73thdiKPJCEFHbNtFS1Bp0sjPyBbE-5Xe50ENgVh-jFjJOfA-A3SffTM3vPh4Wo--kMtrlSJ5BO6fhw9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46400b9012.mp4?token=e0eIJxY6p7jB7jPpbN4eEgPtx8zxYOHRUvEtJxCtogSFA9BysbbGIbbcEuLT7AgOcZ78L6oadN30w7pHZIT0PLvQ4unGDsPxdnYCXNSg1lLRNhN88-6QY4AelaOuPfLEuAytO27UfXJdgdAj0UEbrI1XHtUEvHMK5TigGlMVdNaNDvusc60isEASR-EsFi0SrQkMiZLZYv5_nE0CqNPT1IwvoBDCT_Mhd2m-CJ0zU400rHpuD10HRe7iAHTdqum5P7Yjf73thdiKPJCEFHbNtFS1Bp0sjPyBbE-5Xe50ENgVh-jFjJOfA-A3SffTM3vPh4Wo--kMtrlSJ5BO6fhw9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
محسن افشانی: اون شورت و کرستی که استوری کردم برای خریدن آبروی یک بازیکن فوتبال بود!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/106206" target="_blank">📅 12:19 · 20 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
