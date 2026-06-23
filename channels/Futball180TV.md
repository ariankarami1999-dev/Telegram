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
<img src="https://cdn5.telesco.pe/file/fKriYYvzTOiAeuufOsxubZX_fSB5eZK6sDHlveIFM3P0s3lutitTCmQbMztfOeGuuY8NM9VLh834NtwtuEaTCpofk_3CiMoG2MCQLDBdtoZ9anvYiZoAGueW9bhfia6EUZYZkqWrhT1pyrJiLe_LNK7OPUpdEM8teBgmz3BdSPI4QfjIQTuQMwPkXUoyJJ2_xTI31cmCErv1-lJ2uDX39YyhiYjb3gVbHYim-ZLMQsctTiekOJZAMlwV4X8IwwT3VO5PrYKmMvzkTfLpYvfyETOKNjtBenZsQctk6XUF0s_SeqQS4rz9S4537G58MF8_-apzpI2dqMUHNul-THt2tQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 727K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 11:54:03</div>
<hr>

<div class="tg-post" id="msg-95406">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10eab0b9.mp4?token=Dqsv_Yf860c4lSi1FTwr4ZMPbEKFJ-jl0OuS9ZSm2k-GGYIDbf3nuxrQK9pSRiLsq2FHNted-5pFcGmZQshUlDHrC4WU4UQtruebR4_PiwIfDwH4l2ysDVhVHz10_HIuSZ7G_y9LKElG5nlOtzzET7mk7FeiWS5SbT0nrlqLOpczgI5vanj5Td9CHfafPUxLTWNsoVDfIymJVc38VGDkM1dhyHyES-Y8oGVEsyZ1Dcrd2Jfcj0tBeOrcxwWtpDww5y9x9VfQG4iyFtKTmPIl0Y3gy8H5ATvABRlbGVlfnR3bGESLZIc4sD3P8TOutgJ3sF3NwGKg__5slQnJN9b0eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10eab0b9.mp4?token=Dqsv_Yf860c4lSi1FTwr4ZMPbEKFJ-jl0OuS9ZSm2k-GGYIDbf3nuxrQK9pSRiLsq2FHNted-5pFcGmZQshUlDHrC4WU4UQtruebR4_PiwIfDwH4l2ysDVhVHz10_HIuSZ7G_y9LKElG5nlOtzzET7mk7FeiWS5SbT0nrlqLOpczgI5vanj5Td9CHfafPUxLTWNsoVDfIymJVc38VGDkM1dhyHyES-Y8oGVEsyZ1Dcrd2Jfcj0tBeOrcxwWtpDww5y9x9VfQG4iyFtKTmPIl0Y3gy8H5ATvABRlbGVlfnR3bGESLZIc4sD3P8TOutgJ3sF3NwGKg__5slQnJN9b0eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
هوادار مصری رو می‌بینید که بعد برد جلو نیوزیلند شورتو میکشه پایین
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/Futball180TV/95406" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95405">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad3c34fdff.mp4?token=Sv9yu1w6oDVu5T_JiSGr_3egBCELqDj00hWylPfIvkuIFkqT4ceV8p2YKyY0yFERLvZNqQGUBiN3zdWViBveYkXHMeNKHIsfr-VCwj_VRs18AEkAFVMv_5wzxvEnZ4KhgqZx0qRM_dLPdSycs814zc9SRSyuTIWpmiKJYBar0rizQGzRz5f7mHGDqvYrOIyd-TpA75Pe9AGLtLHuUjd4leE6-vnUMqwG0bvlBfoICvbeZJgVON8FZ2qCx_cAtvL4UqE5-rnzGvwnGMQUx_bkYHYKWt5KgAywYQvAWTsgRsMCFM1j5dzrwbJjUIfdOVJjCqyhpp7UNlUfmPTg9g-kpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad3c34fdff.mp4?token=Sv9yu1w6oDVu5T_JiSGr_3egBCELqDj00hWylPfIvkuIFkqT4ceV8p2YKyY0yFERLvZNqQGUBiN3zdWViBveYkXHMeNKHIsfr-VCwj_VRs18AEkAFVMv_5wzxvEnZ4KhgqZx0qRM_dLPdSycs814zc9SRSyuTIWpmiKJYBar0rizQGzRz5f7mHGDqvYrOIyd-TpA75Pe9AGLtLHuUjd4leE6-vnUMqwG0bvlBfoICvbeZJgVON8FZ2qCx_cAtvL4UqE5-rnzGvwnGMQUx_bkYHYKWt5KgAywYQvAWTsgRsMCFM1j5dzrwbJjUIfdOVJjCqyhpp7UNlUfmPTg9g-kpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
پشماممممم چرا بخاطر یه پرچم اینجوری بدبختو پهن زمین کرددد
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/Futball180TV/95405" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95404">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dde90ba169.mp4?token=GXR7l21KJwHSPdoNLaHOaTeFUdXl5-phjRO3ORKhsetaYXfqN87uEjGybCr5jfbccwzFlj_WPcPhJC79BvxcmctsI1tagTTsxLf5n7gm-vukhXcTvPGI_1glimsDOn512Jr0F4X5oIJww1aQPPKaT2CMtK9KEwB9YpW-dJsoPD1nSw58uVRueodEwYtMIDyblCMgvTKm6s5z1fTRqzZmkU5yRXgE1RafKZYBUSNegQDBj-Bm0SZjmEGKwweZIcwLXl8hNwqZ4NKWZ_sZWHa_-Ci42wN2EoYP6wm-nq5o5w0sqUuYJ3yYnywUEIqI2Xze6qQBudReJnae8Ahzqp3xHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dde90ba169.mp4?token=GXR7l21KJwHSPdoNLaHOaTeFUdXl5-phjRO3ORKhsetaYXfqN87uEjGybCr5jfbccwzFlj_WPcPhJC79BvxcmctsI1tagTTsxLf5n7gm-vukhXcTvPGI_1glimsDOn512Jr0F4X5oIJww1aQPPKaT2CMtK9KEwB9YpW-dJsoPD1nSw58uVRueodEwYtMIDyblCMgvTKm6s5z1fTRqzZmkU5yRXgE1RafKZYBUSNegQDBj-Bm0SZjmEGKwweZIcwLXl8hNwqZ4NKWZ_sZWHa_-Ci42wN2EoYP6wm-nq5o5w0sqUuYJ3yYnywUEIqI2Xze6qQBudReJnae8Ahzqp3xHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از این زاویه ندیده بودم عالیی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/95404" target="_blank">📅 11:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95403">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fd135cd6d.mp4?token=BH7xWUOuH6O_z6jL-r0h7RzfiY_OCfRJ4v9FU_82p33bnDhlpmzPucP_ImLAG1zzw9oSWH0t-X4rS_yKtrJNvbwQ4F6ojsglrqBUoQvnpa8nu5zrgBjyffWmVfzITBOUofrypuSDMrkkvxOOFh-qlFlh3zYYtFcVfmbkRh1Of-x6P0ueIBeVsux6WFIhl9bWfOn30HfnHnFqlaXECtZ4-6sGCSTsEFC_h-Tb_zJatpE-qWkdKxZoXhv8xsvRZzA-Y1LI93-NkQ-qKPNkFz_RMUH-Xo8tDK7eBQTdb-BaKW880xA3sWDUja32eDRPaRjYz5-EreAQ8M2YKjdj-8hYSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fd135cd6d.mp4?token=BH7xWUOuH6O_z6jL-r0h7RzfiY_OCfRJ4v9FU_82p33bnDhlpmzPucP_ImLAG1zzw9oSWH0t-X4rS_yKtrJNvbwQ4F6ojsglrqBUoQvnpa8nu5zrgBjyffWmVfzITBOUofrypuSDMrkkvxOOFh-qlFlh3zYYtFcVfmbkRh1Of-x6P0ueIBeVsux6WFIhl9bWfOn30HfnHnFqlaXECtZ4-6sGCSTsEFC_h-Tb_zJatpE-qWkdKxZoXhv8xsvRZzA-Y1LI93-NkQ-qKPNkFz_RMUH-Xo8tDK7eBQTdb-BaKW880xA3sWDUja32eDRPaRjYz5-EreAQ8M2YKjdj-8hYSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تقدیر جالب قلعه‌نویی از بیرانوند در بازی بلژیک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95403" target="_blank">📅 10:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95402">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2281627e22.mp4?token=RqIhewILbn4lvMFdddKEDX8XgrlNbZ057ukcxR4EvSMTajmoQXhnrbylvOZjJMCSIb2EhnKzgaL4xsiyjsBG2m9IfnJYv5cadLNWfLtnPKPdhRRXX8vuVF_I6KV_a1JAyi-JsQ-zHOT7qRsB6JiR2iKeBXv-vKzJblzrF4OdphL16UBWImu5QXqqRXarDH8YOzYpduH_dupdYh9a4omPMLyvoUpFW-D6h1J74MVJguC8qJQQVJxXUVdhdKffkqbzcfBhMwMsw0C9sZzl_hBcVzH8lKv2XNZs8Rbhvzmxv9Ex8GH0AqmPfJ77A8sTosMER4Wxb4ht7tLVmFDlBbvflg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2281627e22.mp4?token=RqIhewILbn4lvMFdddKEDX8XgrlNbZ057ukcxR4EvSMTajmoQXhnrbylvOZjJMCSIb2EhnKzgaL4xsiyjsBG2m9IfnJYv5cadLNWfLtnPKPdhRRXX8vuVF_I6KV_a1JAyi-JsQ-zHOT7qRsB6JiR2iKeBXv-vKzJblzrF4OdphL16UBWImu5QXqqRXarDH8YOzYpduH_dupdYh9a4omPMLyvoUpFW-D6h1J74MVJguC8qJQQVJxXUVdhdKffkqbzcfBhMwMsw0C9sZzl_hBcVzH8lKv2XNZs8Rbhvzmxv9Ex8GH0AqmPfJ77A8sTosMER4Wxb4ht7tLVmFDlBbvflg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🙂
چالش هوادار ایرانی تیم‌منتخب قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/95402" target="_blank">📅 10:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95401">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/612c544153.mp4?token=A0-9acO33ie8OiTzjRRKtRg3feiMW9w067VwhHBFUdlGLHOnN70mD4hS4L2GHGSZ8xM-JtE0qQQAB8nh8ABbTOOW2WE2lNHKg5v_1zYhI8LhE1DTK_DJ2DZaj89a4zv1TL7JlLybqO_6ynOv6tCu6LkQsH6Sr3DJqwxxDPzfZKRCeeb7NllH_iI06V7owYrvAlXaZQMkVdqJvx8ux-j8P0H9xelfZ8Ygb0B9vc-C5vgea1hEUa7U3XiU_LrtoEd2AppyHwMZH06_r_gqxCjkg759XZe0UJDr2pCNH1NAxNZBVdjAnc6_mXMjtixtZRs9zgKNqxt1AeIbLTFALgl3Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/612c544153.mp4?token=A0-9acO33ie8OiTzjRRKtRg3feiMW9w067VwhHBFUdlGLHOnN70mD4hS4L2GHGSZ8xM-JtE0qQQAB8nh8ABbTOOW2WE2lNHKg5v_1zYhI8LhE1DTK_DJ2DZaj89a4zv1TL7JlLybqO_6ynOv6tCu6LkQsH6Sr3DJqwxxDPzfZKRCeeb7NllH_iI06V7owYrvAlXaZQMkVdqJvx8ux-j8P0H9xelfZ8Ygb0B9vc-C5vgea1hEUa7U3XiU_LrtoEd2AppyHwMZH06_r_gqxCjkg759XZe0UJDr2pCNH1NAxNZBVdjAnc6_mXMjtixtZRs9zgKNqxt1AeIbLTFALgl3Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
پادشاه اردن امروز در ورزشگاه شاهد حذف کشورش از جام‌جهانی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/95401" target="_blank">📅 10:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95400">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e962c1522.mp4?token=AL4tsnoCZPe9Mof6-QPhHbR63JTeJEUKkji_XxjfSJl-9THs6AdqCCX55Eyq9D27gg8wT8QqQGJr9QoEgmVbo9dP9b-TiCegY9fLXyQ3qaIpAFoJfngr4Q_vSG28tODUGrRvo0xSC-oDYCXuBD4QH9RYrd7zHRiY38NLMCWjgOWpD0lIUlxTj0i0M4RcxI1lav-QVGqMr9MnFoyNUrWLZprQbFpgFh2tbQFNINvoOZb_yw8ke2NooVt0iR9WK5LBc8GSRpsbUpSSRkfEQstr7KIeSUjkY3SSP-G23IbrS90vIpHr2KTYLUW5iEVfvUiJzHkPhj_CI7xcqZgpp1lYbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e962c1522.mp4?token=AL4tsnoCZPe9Mof6-QPhHbR63JTeJEUKkji_XxjfSJl-9THs6AdqCCX55Eyq9D27gg8wT8QqQGJr9QoEgmVbo9dP9b-TiCegY9fLXyQ3qaIpAFoJfngr4Q_vSG28tODUGrRvo0xSC-oDYCXuBD4QH9RYrd7zHRiY38NLMCWjgOWpD0lIUlxTj0i0M4RcxI1lav-QVGqMr9MnFoyNUrWLZprQbFpgFh2tbQFNINvoOZb_yw8ke2NooVt0iR9WK5LBc8GSRpsbUpSSRkfEQstr7KIeSUjkY3SSP-G23IbrS90vIpHr2KTYLUW5iEVfvUiJzHkPhj_CI7xcqZgpp1lYbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🏆
🇪🇬
هواداران سوپر مصری در بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/95400" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95399">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
❌
🤩
#فوری #اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95399" target="_blank">📅 09:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95398">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b71ff2a0f.mp4?token=tBRw8HHmYbw2J8Eh1KlKYUl9kICFtu_izTEbfKiKRUJxXCQytOtts8RXHjLS6AL8YZDNETDb1YVCEeZQCsc0ghuPq-E5TEdR-8p030KOQwD79dugS9awCWdaQUYQnjwzJ2QC91ZNIsKkK6gNJnI3Giwo-khJABSrtyfPh4jzd72CgTRI5RBNeku-L-3MiTPpK-jgRNKje8honGssfOX47niKLRflLiiyxR4E26a94rYnzr1ensV-KRe5y5Zn2gsoPu05KcEMz-xsB0JY-DgqRl_LWRn9xH-lsFflUA7CgyJcgCh9Zb9G5yAB1lp75AP2qaxPvkriMDo2CTn8wuYNzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b71ff2a0f.mp4?token=tBRw8HHmYbw2J8Eh1KlKYUl9kICFtu_izTEbfKiKRUJxXCQytOtts8RXHjLS6AL8YZDNETDb1YVCEeZQCsc0ghuPq-E5TEdR-8p030KOQwD79dugS9awCWdaQUYQnjwzJ2QC91ZNIsKkK6gNJnI3Giwo-khJABSrtyfPh4jzd72CgTRI5RBNeku-L-3MiTPpK-jgRNKje8honGssfOX47niKLRflLiiyxR4E26a94rYnzr1ensV-KRe5y5Zn2gsoPu05KcEMz-xsB0JY-DgqRl_LWRn9xH-lsFflUA7CgyJcgCh9Zb9G5yAB1lp75AP2qaxPvkriMDo2CTn8wuYNzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بررسی کیفیت تیم‌های آفریقایی با کاوه رضایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95398" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95397">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dee4859e05.mp4?token=oja8wzEtq23AwOZw3Wf-hDHFDXOobBtyOFR3iOEbbu0P_qeLaEqjsjkR0y8oaiN7gL86FOAOy6ZTO6ktNBw5OKElOTFk8IHZAxV66hwflytUTLaAK7hhwzNh8nOBgLNYIR3UGH4xLM5ssz1e64M-ZCy2t-gT5RBvsC0Rw0sFFMn8N2Xu5BjgWHsqDiiMrySrE8M7z35KWhT5cSSX3OagmKsNItGMzm8DV6l3bd5zpAxumWl_7OnG5oCRw9EKfnqMElHB29o-MVoF-MXvgQtTZh09geUf9RKV7DAExFnWzPLxQKzqKy0rQC6LhnLV0yBAToZA9nTGgFp90lYpA0k4iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dee4859e05.mp4?token=oja8wzEtq23AwOZw3Wf-hDHFDXOobBtyOFR3iOEbbu0P_qeLaEqjsjkR0y8oaiN7gL86FOAOy6ZTO6ktNBw5OKElOTFk8IHZAxV66hwflytUTLaAK7hhwzNh8nOBgLNYIR3UGH4xLM5ssz1e64M-ZCy2t-gT5RBvsC0Rw0sFFMn8N2Xu5BjgWHsqDiiMrySrE8M7z35KWhT5cSSX3OagmKsNItGMzm8DV6l3bd5zpAxumWl_7OnG5oCRw9EKfnqMElHB29o-MVoF-MXvgQtTZh09geUf9RKV7DAExFnWzPLxQKzqKy0rQC6LhnLV0yBAToZA9nTGgFp90lYpA0k4iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
طارمی تو رختکن قبل بازی بلژیک دقیقا چیزی که می‌خواستن اجرا کنن رو توضیح داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95397" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95396">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aca2671.mp4?token=PFS-k0vOy1VVaBD5XvICXWVk2Pj5lg0GBu0sAG_mHnoySyI-oDaZIvzSInsyKYQep9a8UtSIlNPbt4mK9Yn8yVmiNRVIwKIN0KEIIAS3mWJD-RRb2Lyekh_ptg3lAfkMm8zHWOPU46aPq3FoynrgDVi0fxecA5MRGZcxrobB6eWMbuZ2jN5drWscdP-5x9LHkarI5uMxw9oPEsfxUbkH7zI5PWS5Whv8hObiLPZnNOsbsy5N-2qFvSH0-_3GVI-pWmtOv4kRHS9vdG0GH_7WyRKtjIgnhRBJ3Npe741uJwjNXTyLsooM0PRFyTybfL0ETbftwjUfkGXEfQcAZdynOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aca2671.mp4?token=PFS-k0vOy1VVaBD5XvICXWVk2Pj5lg0GBu0sAG_mHnoySyI-oDaZIvzSInsyKYQep9a8UtSIlNPbt4mK9Yn8yVmiNRVIwKIN0KEIIAS3mWJD-RRb2Lyekh_ptg3lAfkMm8zHWOPU46aPq3FoynrgDVi0fxecA5MRGZcxrobB6eWMbuZ2jN5drWscdP-5x9LHkarI5uMxw9oPEsfxUbkH7zI5PWS5Whv8hObiLPZnNOsbsy5N-2qFvSH0-_3GVI-pWmtOv4kRHS9vdG0GH_7WyRKtjIgnhRBJ3Npe741uJwjNXTyLsooM0PRFyTybfL0ETbftwjUfkGXEfQcAZdynOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🇳🇴
احتمالا پس از موج مکزیکی و تشویق ایسلندی باید شاهد رواج شادی نروژی‌ها باشیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95396" target="_blank">📅 09:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95395">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOpYbSQuB_AzefRNLF2OB19DvCSLVcwj04vqwT5XmxqNf4A40DceMS8F1XHXMJ7KjePtj_2jvXiuBgZWPL0lBSBdHk5D_qYPsYYhDyOwgKyzgaA2ACaGII5ZR0i_S6yyvbMFT1H-dHJnJoH2cVWy6G31g67AGcrGGMC6PUxrCadI7gS87zKdyd4uZuMzYwzDS9boctUrWlY3FuV3hbB-9vrvJlroiACe4IWjKCsliZh0areJr_BZaSlkFpDfXXnbtdV4OjMn27IZI0wNcIMkKCDg-lmc06UPu37dGAwI2DTrwAe4nhL39xxQzGxEbNq58QnB68D8FRA2qWRR6dvssw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇯🇴
تیم‌ملی اردن از جام‌جهانی حذف شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95395" target="_blank">📅 08:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95394">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇩🇿
گل‌دوم الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95394" target="_blank">📅 08:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95393">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8863fc015f.mp4?token=p9n0kCRlpGX11jPAXdH89fpGYLR1eLtnYVzRKBiAGYOyYxSPCTyBBQ0LULcM6hzM1WhabBAPr2tCin0gcgZWwPUvhJDCsbaaRg-FR8htZ5Ahdqbn56ArGOnO_etH2b7mc4d6qUVsEUnqmStawFx0Xrmv0R20Qj3cvVBcykaIoX1HvqoBvNqzdu8CokprbWWUDtMQAtASmCPahfR60RFm5o8M1MJY0xsdwsUeAkhoWO9bo0LJZ5yPFJlnEVJcdKQo0PSXoszNX3jMUDph8P8Ad0mXuMNKW3xqhFdgPCmhh6nhU2OWrfXqh6RWGJknIiAfPlOhMJTf4Q6aatAzavfB9g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8863fc015f.mp4?token=p9n0kCRlpGX11jPAXdH89fpGYLR1eLtnYVzRKBiAGYOyYxSPCTyBBQ0LULcM6hzM1WhabBAPr2tCin0gcgZWwPUvhJDCsbaaRg-FR8htZ5Ahdqbn56ArGOnO_etH2b7mc4d6qUVsEUnqmStawFx0Xrmv0R20Qj3cvVBcykaIoX1HvqoBvNqzdu8CokprbWWUDtMQAtASmCPahfR60RFm5o8M1MJY0xsdwsUeAkhoWO9bo0LJZ5yPFJlnEVJcdKQo0PSXoszNX3jMUDph8P8Ad0mXuMNKW3xqhFdgPCmhh6nhU2OWrfXqh6RWGJknIiAfPlOhMJTf4Q6aatAzavfB9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇿
گل‌دوم الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95393" target="_blank">📅 08:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95392">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">الجزایر کامبک زددددد</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95392" target="_blank">📅 08:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95391">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=grjCt9uib7QbnpEVK4uGFHLt3XVPdEkk9eWLM_osBZ0CQU-G2M9xnA1KFMNcE3XrqdWkyTlPfHgFmXe5sRvglckUhyBj_s2kJ0RJnUjcPmMPuRt9ntuSIPwrbSXczOdzrllNEqzGopGPIs4QKM1R-lDQYIDgOyOcWTjmcosDTCkvt5SN4184uHQfhyWqe-Awt7CgZbHWrpLxS4gMlyD49e0K5uOrVdxvns_pemFZONPG630rwzG2uBwhPQf3n0GPor9_Z3_yhxj40J1lrOgyPndra1upuNdgOodIene04x-sWdfLOP6sub9PXGEGw2Ns8qeKbF2uGLsEZ3MVWkdyNw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dc4496f0cd.mp4?token=grjCt9uib7QbnpEVK4uGFHLt3XVPdEkk9eWLM_osBZ0CQU-G2M9xnA1KFMNcE3XrqdWkyTlPfHgFmXe5sRvglckUhyBj_s2kJ0RJnUjcPmMPuRt9ntuSIPwrbSXczOdzrllNEqzGopGPIs4QKM1R-lDQYIDgOyOcWTjmcosDTCkvt5SN4184uHQfhyWqe-Awt7CgZbHWrpLxS4gMlyD49e0K5uOrVdxvns_pemFZONPG630rwzG2uBwhPQf3n0GPor9_Z3_yhxj40J1lrOgyPndra1upuNdgOodIene04x-sWdfLOP6sub9PXGEGw2Ns8qeKbF2uGLsEZ3MVWkdyNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇿
گل‌تساوی الجزایر به اردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/95391" target="_blank">📅 08:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95390">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گلگلگل اول الجزایر به اردنننن</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95390" target="_blank">📅 08:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95388">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V4yUs2vdCnb51qvNBOZ3na6cxnx_Frk-VE-IAJsXeyFUl5gC6tREZew4t1FkVNZbEMvwOiWbEmxfyP-47eHLg2ddCpduPX24v0YWLgOGIyV9siWSQHAEoyCsAjguTH9LH0p5deIDPjSWKBFys1VI3qNqh-vkhjZQ2rTb5i-cVjhFu5hMzq7mE_o9usF10oEYHQXrCM4zlBp-yLtWBLLOGpzV2WJjGtxF2bR6vjDA6Zi0qDjmEP8LRDqd2rEvkK-4GSAFGu58tEPhJQYJQmt25F8xt-u0AlROKN8yimxNSdV978UY46hesHNSzluGhSCcgbsqCnEIW0mnEPH-GO44Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/muf41K1WJcDJQcsOGFBiQNPXSVGLFntKiVrvP1W-0PnhMVOcWKgXHO4mIhn_fkNIqZykFQ3z7q-pMzjxcBZbwaYxNz0u3KjCDyDwu_1eYoandxkfqibmLVAMg8qAkbthU_gK9uq6zF3demr5ZnETvbdape5PwTcV4sYPHPfr5gb4mwKjjJZtAroosiQPA8KmzQ5B-ryQmf5eT8oQ1ewiE81kaNebiD1EM1Kw6bkZk96mXOs_tFWyWr1rHlCTfUQnpMetB8GPgwb1FCIMUze47mOR-sRExbzB8_zvNF07CZpnoQHMQqG7J9f7nhHraW0jUH-psclTBTYfYmdb49Mnkg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
کارلو آنچلوتی: یک بازیکن هست که من او را خطرناک‌تر از کریستیانو رونالدو می‌دانم.
رونالدویی که در آخرین بازی‌اش گل نزده است
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95388" target="_blank">📅 07:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95387">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/09b400e516.mp4?token=uQuX_f-aEnVkLw72gPol6WV_28xckRvgK6BYR6Ht4AYq9RuX_33bb1wMhxhD2LnHOH9trIpFdl51nTmMfdqydFVAJcHq5etIWy3qUb9GnGcAxQgBJXPKIoLA0VeJY6CNubTHqaapeIctVtCxkWC633x0zquNpDUszlCKsnPca1_FjXqj-Sw6G8OOAJwdeI1PMRfUGe1tKw8X-c-Nhvhe6AyI07pKl2ovE0v_mYt6XEL5gH47I_MftVBCLjXVzPVA4Yr7L9OiFEGLXUvkr35U-MJdbx9sXem7ICGTPoL44e0Gzmya5kmg1QAXSm7ub_oZx4uBqnHk6IPBgmCAXz482w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/09b400e516.mp4?token=uQuX_f-aEnVkLw72gPol6WV_28xckRvgK6BYR6Ht4AYq9RuX_33bb1wMhxhD2LnHOH9trIpFdl51nTmMfdqydFVAJcHq5etIWy3qUb9GnGcAxQgBJXPKIoLA0VeJY6CNubTHqaapeIctVtCxkWC633x0zquNpDUszlCKsnPca1_FjXqj-Sw6G8OOAJwdeI1PMRfUGe1tKw8X-c-Nhvhe6AyI07pKl2ovE0v_mYt6XEL5gH47I_MftVBCLjXVzPVA4Yr7L9OiFEGLXUvkr35U-MJdbx9sXem7ICGTPoL44e0Gzmya5kmg1QAXSm7ub_oZx4uBqnHk6IPBgmCAXz482w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل‌اول اردن توسط محمود الرشدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95387" target="_blank">📅 07:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95386">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گللللللل اول اردن</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95386" target="_blank">📅 07:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95385">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شروع بازی اردن - الجزایر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95385" target="_blank">📅 06:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95384">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/069fb238ab.mp4?token=ifr98j7zbAtDeQ06fbPe_JCdpkal6wE_-A4WNevwQVY8vRVZf5VtgI7OQa4EQ5UXJoeSygI-BOngbvNIyzFqEYqQUumht3GVNLzMamHrA9_1K_WwV77qfm2eSWGwcXoFMzkWYiw2bIvdMELBkslhrNEHU0bDFH8-IH5wCCjUJkhPg9GC7gScR1TLXcHx8B-EgM_x1jKbuoc4pkcc_Li9FzIRTXTYtdGJNpm0H2dJb36ljyMKgCvZDCGKD1OXNSvJVq2ddtKysQFe4qBmfJ4R8bd6KRkBToBpEpBTojXXp9jmxTKkejlbEl9oeqW6MEcwPw-lm_2k1l_HWepLT23roQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتخاب سختتتت بین تماشای فوتبال و ..؟
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/95384" target="_blank">📅 06:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95383">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUOpiaKbMqLLkvv2tUK58eXXZrLOoGPXknCsBYFAwGiCW4Sq2R3ouI2PnsKsWAYItgw8TZpIVMmruA0fjVS7RVkdgS3o-b6urE0Xo9w9fb3HACxuR4-LeaH12MruhpdWdgOdbNX3CFCTlQBZC6qxKzR27_ooHTxlbnU7IhYnEopm2MF_vpIMKEEqHueY-GQ0o7z87nzeEomTQWYRiDfkuH0skd8EbpSYd9iBGHuigeLTV79TfDOXMHeBOT5p5REmfY7wU8bUCCh6lugFQJsSi1oQqU1gH1TT--jMwUmV75ci7hTjqbO5c00Bv8yd9-ocdlFK6wBRcsTqpsp4nIzaEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی نروژم اینجوری بعد بردشون احساسی شد و از خانومی لب گرفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95383" target="_blank">📅 06:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95382">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFA-NNbe-A109Rox3oMBuD8LE9IicTlumUeDueiXI9b-VSYkdkWymLi_hQVklYU_nzXY73mJiGHd5JNADSdK4WOXX6BS5ZV281M8cjLwova08y4IykPX6y4sVJ_eLfeuYoQuWgbQMaVqCk0-zNfHewXj7EflV-RDjSBbabs12QjCFeh21Yq2efpxA5ngv7SSOtvxDjWosycY3tvn7ko0EVIbU976L_BaCCmbmm_0YsXTvsKw-hxO2WIxvmB1KtxQJSqHBgFQLrCpNkC_u5a5nS94RlllJPxtA0cykAsmfqr97uRld7UP7JuyFcdDngmtKb4kS9bXHBeVHlOFv8KJEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تقابلی که در صورت دوم‌شدن نروژ و پرتغال در گروهشون قراره ببینیم
😬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95382" target="_blank">📅 05:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95381">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxp9ll8uOIYi0R8ELAwQZr-aVTX86jQyKXN6l2G2vWrISK3geNTgkFxrJDg-i0tDiTPaaeuMtAuht23lbUymAodPBfZDKyHmfpkp-q1qH5o9QfqBnsOxpAynkgLmA6KXOVWUb6ZDpRh4Z9-_RNtrssu_P0074RkgQu8Q6hq3j1dchLoAiSbcVFXHwO-zeTylb5gaH-_0c0HGWye2NGdXgaTFgPQnM3Yq9fUDl2eyPCk-tgLAS9yxsDXg-sQLTbZEosaWOU2amqH8HxVVPqRHh_1y6CnNpa1ohJngzzWgqtitL6-qtZMQCDesZ430epzBX-CUUIeAt5eVh8oNObSZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
در جام‌جهانی ۲۰۱۴ و ۲۰۱۸، بهترین گلزن جام‌جهانی تنها شش گل به ثمر رساند درحالیکه بعد از گذشت تنها دو بازی در جام‌جهانی فعلی هر یک از این سه نفر حداقل چهار گل زدن
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95381" target="_blank">📅 05:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95380">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f7d89f979.mp4?token=T5mKIBR_QvCriTe0l2UvT8hbdy3XZnnebzha4pPqxVZABzQZmkRwsJkXuLH0qFt4HsV87kCC9G4ccIJ2GLfN5ReYgXb7xwOVXnuEPf51oteoeJ_wRo4Q8HUKTKofIuZ2SMz6vS0CLncICIArgopjSjW4sLPRgfY4FWhg-j_41PRXcfoxUHJaxc5kwio8aRgTgKFfumhjIiz9OEm1Un5MtYLGKWj4ZGWUWawFDwPxN6KeiBjV6qnCzZVspXMtPe16BC9iN-XdRlNlKJE3rpsDL5JXmbefcyGwpK7MWFresIW0LakKH1Tsk9_BN85Bga04XP693_feDrRXD8rdsOLISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشماممممم از جو پشم ریزونی که بازیکنا و هوادارای نروژ بعد بازی رقم زدن
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95380" target="_blank">📅 05:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95379">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjIJtEXx2gEktVbDv_l0d3CiB4O3nqpvkg1uE69sC2r_eCTHh0jSLhJ117GjB5EW7Q5ShAfUUh2epKimnGgNmy9KnS1zOoPLAbeYht5LWbwezzmuK31B0-iHFiDP23Kz7FkskQaR1qWKAh5vUjWDd_zeiFli4dD5q_04Zv06xA3uH-aV_fQiMygb7vuRWJpJli_vnWBRSnPPm3nRh88Mb28WFmvEMWsAdXbcsz8Qy66XMK6-xwHMOCdjtwRGvIyzMmYqreb2zTOGf6siORCN7NNrFgh9ZytdSmjdD8CWp3gaHyMbNdtJnArP2trVYErsAYj9eFWIj0X_MxoOQYR5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇳🇴
ارلینگ هالند در کریر فوتبالی خودش:
⚽️
‏• ۴۱۶ بازی
⚽️
‏• ۳۵۶ گل
🔥
‏• ۶۶ پاس گل
‏۴۲۲ مشارکت در گلزنی در ۴۱۶ بازی!
😒
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95379" target="_blank">📅 05:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95378">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmbiYlDLYi8WOjcf_StzJzLoKx3CocOBc_0YPVB2xyWY8FI6p3NUkqpXzcFfLg3BfMQZ9mpopL_CXdoa6_FeNekwNY_c8-0n5-9iFEruUSJRUc1IyzCo1UaL-nDAYI0vtCLeAALZeOr9uLijGPNn2CUmLNK_yXENqYnvxiEfAvgmsiJf4ODxWcLCrIlBqA1ha-A-g2juSNh7D7qfXpCliup__sOkq2IIhqKHi6iIlAGM8vtpOY_RROKI6QrjPdUHTXJ5nFpDofH9EQRIhTWFx55OZgqbWD8RrJr9AhdT65nKP1R9lyI232PlkfASELEav93vj-J-NbWtXjz9dJ3X6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه L جام‌جهانی پس از پایان هفته دوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95378" target="_blank">📅 05:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95377">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVLTZkn0C_3ITka7r1id2--AAtbwVcgpqqdPVRdgilKCgAeua3s0RuJz7wsq_9lttjhzKYmMWNHilAjL2klEryC7hsATbgXr3FX0iFNq3p5Fp4HR88pnjDyIWFiw2_16Y316RNbPq6x3F16w_nBi_ZweBp9SscaplZTK28fSDt6qp_trRKx__XWGGZAy_v3iyuoj3qBp934BQrZ2Gsg9Ys7svi7oSaBymWa5BWpuRxQwQrWC24mqdHqh0bOoWLARFxQN0D6SKhL4VandzniYwNfr4izrfVhjbXblDf1ibM0dFyHvIq74AVqKSSSw6VtkNJPQNdmEZJzH1ro-e2Gg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | صعود وایکینگ‌ها با دبل بچه‌غول
🇳🇴
نروژ 3 -
🇸🇳
سنگال 2
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95377" target="_blank">📅 05:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95376">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=rr8O0-8piGOMdKSdR4NW1Hu6PR0QDz5XEzBKE9N_Ke893xbC3dlNM3jdNCLFJ6iY5FBCjB2FjD4jtofym28ZFHu3cDmpMdPkn9KCllf8auwZ71SXhQrEODO1Qnq9KtE1F4_ndhcdhv0_IE9a75dWJ5Tyt0T6DORjSmBKRmBrS6sz5KNjuxe28Lpbp7iLMpuuD9934CuVc8AkRyzImRvP4kEMwtYM8wB1VvcnQFu8cK8atdVII7vkblvhwyoqZAR69qHdvUR2Rk8-l0N-QjcV0ED39-MCkzG8s1SyjoddsX2r7f-F8AYsbNBZ8aHI33hngYYfx23vJL72rOfhiAyCpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/03c1e0c349.mp4?token=rr8O0-8piGOMdKSdR4NW1Hu6PR0QDz5XEzBKE9N_Ke893xbC3dlNM3jdNCLFJ6iY5FBCjB2FjD4jtofym28ZFHu3cDmpMdPkn9KCllf8auwZ71SXhQrEODO1Qnq9KtE1F4_ndhcdhv0_IE9a75dWJ5Tyt0T6DORjSmBKRmBrS6sz5KNjuxe28Lpbp7iLMpuuD9934CuVc8AkRyzImRvP4kEMwtYM8wB1VvcnQFu8cK8atdVII7vkblvhwyoqZAR69qHdvUR2Rk8-l0N-QjcV0ED39-MCkzG8s1SyjoddsX2r7f-F8AYsbNBZ8aHI33hngYYfx23vJL72rOfhiAyCpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
دبلللللللل سار مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95376" target="_blank">📅 05:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95375">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سنگال دومیییییییی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/95375" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95374">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلللللللللللللل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/95374" target="_blank">📅 05:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95372">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7Z6OxFFgqKFKx1dUKqON6igcKKI5WyznuY1Ow9FYbiUpw54FojBnEHRMcX3Cl9RoPsTIxD6waWMgNp-vLmb_nz_UHzGE36xmiKjHOhObEixW-NIGKJc9Sqn16vj-98LEaaUvEQF6326Pe8yxkpHsSdUwhtcF2HK0CcDUrDqoreMHcrp9y3d8wK0xT0Q7z6vNzFsIFn4ZxgxHAgAz-EoDr_KyHBDDCWJVRb7VhpfhnbOkOCzk6kpzMKlZU1BgskCV6pB7MzVmmzKlz-ymKUt-aPCMjf5SAo4P-GRuyo0_uX0Z2EawgBcLH56PYroaY3cL17ltowbXcB0Y-FBvOOljg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I0ZKyMW0FJZd9TC1vifUZAu2zemXcBQJEjoAVqBc2SdOCVNEDK_Y03CapyAqf4bSzLaQDM86qs4U7YlAtl5xbgKUq7VBjbSmjqLpmWh3uXHGSqVcF9HHokMykeehxnh-fjT4rLpg0IqQwsxtEtb3bYEBmJ9TkTW8YkUbn9wslZxwJR98Aedhil9QJwl7cdtV4ZI3v7MdxVah1mfr0U_mMgP8nKpQsgFE50FyLw0opGb5HFjsFx696GMACAeaVUJN-2yznNVYy0Woc_37gyYQ-7ZnXNYwOoAa7DdD0aU7Sv1QU4myvB1Wf0P-TmqBvuFFOb41AtxRta6u781UC1cpuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇩🇿
🇯🇴
ترکیب اردن
⚽️
الجزایر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95372" target="_blank">📅 05:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95370">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGNTfIeY4eQaySzu6rFJq1hXpITTWia1YnAN9X716pe2VOd0nhk55ADmAR6l3Ygv-RSGAki0WwL4klqSIqN81O1rEfv-nP_quraEGwfrYPq1WspxWSUL51cifpm7v1D86Qqx6RyTmSP6nyzhcK6pkVRXaCgpDARMi0aBurjo4GP2AaVaE51spEhmXHFFP7g4QB-oz1RDTSR6v77ksbl8ZLcAB7xbDSmZvkfLdO98Zzxaitr7Md5jVhkvbgzP6aEI_L453z1sx9iNhnButayEbqJZoS95prD2J5V-R_FMMuH2ZFvblIyEAeXfQGnR-ZMHlXzxAbm9VnW5O_xSc9O0Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qes1e062iINPGX4m72OWqmDKAxmKnM4QyeaA1TW0jrz12pTrc0VVek1OGX9MhtwkFYXq2MLk4nezpYrJxdCM09Pm1kgIz15ZlOVojyBbpZ16T5Y1ent67exgkBpc3CBB_HGnZzG5eRdymmjMWjJx4XpIU9k9BwH_M8FFKsW1qL8cdyHIk_UH3FJtaKVhCajUkmjnSxUetCGaOBIGSMzuITCiMHekTK98kDBEPoe1JAJCOTYIb2plzrYrbDbtYKzuyoS1pbmR9iYCyd_Ie1BX47qQ1PAZKVvjCXgZZTiInhbDM9m9ZOPkghmVcPeDqNM0EgwEWbw6jHVyYROhudq2dA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Haaland x Ødegaard
🇳🇴
💎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/95370" target="_blank">📅 05:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95369">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDVf4UP5lvu-0wKpPaZvasMmRGA0XcvFy0_PqA3xsTFY-ODr_mdK2ImU-PDPV3EGdBJRN1MIJwEYyaIWVN7Jjn__0Cfp4OMLtvYh4Kk3E1zQwnkncJo6NIN1VQ_2YgEdJ5esG-cUFIN35sLWXRJuS4kdSLMStcf3XPDNMnE51ZWFHTjqJdO8fDdiJdP-mGOhDxb7wF4pRmtfJpWSVOWoX80-mAt843i1qQBQqjgunNILZxfwWs6dq5ILz2L5UosIxP1uk-z7qizDttwOpQakCOih-gkOCaEByoO3KG3JPLXz5wpZEVI3pAUNjZ2mIDokpIhSYuaDfH4qOccJ0yKRCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وسط بحثاتون راجب مسی و امباپه این وایکینگ نروژی خیلی سوسکی تعداد گلاشو به 4 رسوند.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95369" target="_blank">📅 04:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95368">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مندی گلر سنگال مصدوم شد و دیا به جاش اومد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95368" target="_blank">📅 04:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95367">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SwKpyB1vGCLSc678Uht2_kGE5vIFsCzyPrOqhBmeZg9fXpGRKNN0nwFOMT5ItKDzbmAoYAtY1I4pEHowV7131skL_BuDzGyqzs-ksBi_J65dcZefpZ_n1bSMAvMEyML16LUiop-D9MGi9SYj7zvh-vqLMnfGzyKlCNpT53XV1o1df2R05mxfF9fizqIxZw_l5KJb32LL75hPzNxxfkU7UK37ciOFLThdnEnDnU1-YocNwqgm51MsfB2hWHQSozryZPY9RjbvSl1U4As4p_jrDZTvE6kqZHFDWMvd2HHAta9D2UXLXPKe4j5HQ7CsFq3Qvb6II79H_zJ-SQFpb5nqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار پشم ریزون ارلینگ هالند در تیم‌ملی نروژ
❤️
🔺
ارلینگ هالند به بهترین گلزن تاریخ تیم‌ملی نروژ در جام جهانی تبدیل شد و در 2 بازی برای تیم ملی نروژ در جام‌جهانی 4 گل زده
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95367" target="_blank">📅 04:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95366">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=p3-SQFNIWwpGKdPuHtylsH-BpdcxSL1grsX5Oy2swHXwrl5BzAbt-Enr3I3FKlkjrLB8IvF8xQqA4itHXNZzapM1Zgw-Zlq2qiLWaX6PmW9H_e32twIinwF3EvxnCFfS2ijLQShHTPeW6Cy-JUR5ABIYYbvEX6BSoK8GN-s6VLrdtQDO8c7lKDnDB_9RewAAiWpkKRDD8CaXPA2CUR4qx4-zy-s6JVKzea-bznKt1tohi7jrWFFO884z7TjyadNdMaWfnLBR9iZQnL067yh34X_GLcxTplYQpJUh9Y-eMnSBLS1lteG1jziIn29C-_JCY40cFZ2oH_Tvgu2dcFAfWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90bf733ce2.mp4?token=p3-SQFNIWwpGKdPuHtylsH-BpdcxSL1grsX5Oy2swHXwrl5BzAbt-Enr3I3FKlkjrLB8IvF8xQqA4itHXNZzapM1Zgw-Zlq2qiLWaX6PmW9H_e32twIinwF3EvxnCFfS2ijLQShHTPeW6Cy-JUR5ABIYYbvEX6BSoK8GN-s6VLrdtQDO8c7lKDnDB_9RewAAiWpkKRDD8CaXPA2CUR4qx4-zy-s6JVKzea-bznKt1tohi7jrWFFO884z7TjyadNdMaWfnLBR9iZQnL067yh34X_GLcxTplYQpJUh9Y-eMnSBLS1lteG1jziIn29C-_JCY40cFZ2oH_Tvgu2dcFAfWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
دبل بچه غول مقابل سنگال
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95366" target="_blank">📅 04:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95365">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عجب شب سوپری شده امشب</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95365" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95364">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دبلللللل هالند
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95364" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d459d53d.mp4?token=oZSSxLKgRKc53kweVdKTP2Kgx3ywMsHDpTzLBkJKKD8hSjvUumNGROejSNm2lhKCFAtkiLt-M8YrTzeVhHdeGAHRRlQMOuremVcmKIZjvw46O3Z5MkKjefiydvf8uRK5-qn3BF8moIqjGjzqXn7-52fWhX4OdSVULtjyhoT1PsewsqBz1ErvKe9UFupyW0f-Pt1CYvYcs3-Ezemrz_ejb81QP_tPvoSbi6f3UHdvjjVcKY9r9yG2JPhqX_9ajUxIHKjfijQbra_OiVkQwx8o3sa0rbPkFWVCw8kF7RuWplLA_MDrU-2PdeszaRlC1hJ2IpWAxMc3gbWtNkVydYtf-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95362" target="_blank">📅 04:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC5sWPTRKF297Brdlmif8N317sr72mOhyrnEhvEmiQPQn2FC-C-t0A6SMjMBYmcaTFlStKb7K1_GbX3GQp_4Zm160O5C28ea43sVaoBwyeseJhUKssP1zsbaYtjCpb30p8zQ8ezEkob2xEJNtfKG5GdDM6ocpGNR9pLYLzD2ZDkQiA4c-QGFW5RiNpM5cc0rvuAd1_RQIRtRgJt7doo2-tYLznzJpG0TaGA6a7Jnh9EPAeanCEbHyIVfHig61udPkAaoqN0wYybB4FCMhgzDOU1FAryu0vC_FHlL6QyGJzjreiy6CZs0AsjXWe0NwYxDmrF7hUaKpJ5CLg3hEUcgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امباپه با جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95361" target="_blank">📅 04:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4D5CV7Ms67j5VK2s6iyFmzn-Oq1AFNrh76F0lGA_6kLQxFoxrbE5RIuzGDVjLjzw8pyvUDAulTUROoF7BViV9F8so8VgmKGw1edNM4EqI87TZWJmcTBw4jpCX7fIKt3_XNhPJRJ_D3jb8FLq8JIfQAah9O0YMGIge7rZ7NN-2WCkHXf8kcpYQqQh_PAaV4-qTZz779VfdcZTHA984AJ2Z3qvCzQJOaJDL-MPGRSh8tPxkHAgQQsPme-rV2Of1FZtLDvts01_gsNe6vvWxIFU_z_CCAH4yDkmkswpaLw853EKOOQP6SoGE3kllvnUFiFHIxHi3iNBmXc1sk4TAiULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
مثلث توقف ناپذیر فرانسه مقابل عراق:
🔺
امباپه: 2 گل
🔺
دمبله: 1 گل + 1 پاس گل
🔺
اولیسه: 2 پاس گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95360" target="_blank">📅 04:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TR24P_blXKb7NvwFckwn9UmOB3h3RePc_5mMWxgzJ4ucDoz0l1IMBYC9TVFEhvHkliyyqIrrNvFedBZG9Q7LiLeXDfehVIpEIQvuoShaYSnWD-9cSuC24DOJadkIq7Y3G2Zsb1Hk0Y4EFaHPDJxhz208rlthG4NhyW2hOcI-fBoKpIiWYG82g3SMYs6nbCvXcEA3kCTDpVIzsT3Lzkqw3KUskNibl7sIRZ5UtkjeUBQTmJb5ZeTWuWSy1_9F84-urSCf6utYiFEFd69fIESE5joVXyRZqaWf6U15swpvIVzbHFekCgAD9IlDGO_Fkoxd9yg-eFOT_MuYtxCoWgqkBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیمهای صعود کننده به دور حذفی جام‌جهانی آپدیت شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95359" target="_blank">📅 04:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=jbcfqusXaqnkCiR39oinQ_O3xzHraTUapdbo885jJ6iITd6UumEMr-uHPADXz7Ls9eTsHeqi-mf_kP7U_rrND95ZqlTT32VkOdXluTPwDGOnQzX2Qt0ill_yLt0f5Iq6s8-LFsoW84g772dCk6KxBbfR1beggSIlhYYRO6snD7YrpkkuyBlz_AAIoSvGlcwOxYoLcA6TywMs5awynwFPoPbguVl8vozafxdmk8_Lm06N9NivHm3B3tCFS8A_QZHK9QxmpS-3FASflGSkgVV7Rtbds9BKMJnrpQymZJUvDDPklCSjBkGoj3Mvdr6eaffWJacn8WBzi0A9291SKn0dTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48292dcba2.mp4?token=jbcfqusXaqnkCiR39oinQ_O3xzHraTUapdbo885jJ6iITd6UumEMr-uHPADXz7Ls9eTsHeqi-mf_kP7U_rrND95ZqlTT32VkOdXluTPwDGOnQzX2Qt0ill_yLt0f5Iq6s8-LFsoW84g772dCk6KxBbfR1beggSIlhYYRO6snD7YrpkkuyBlz_AAIoSvGlcwOxYoLcA6TywMs5awynwFPoPbguVl8vozafxdmk8_Lm06N9NivHm3B3tCFS8A_QZHK9QxmpS-3FASflGSkgVV7Rtbds9BKMJnrpQymZJUvDDPklCSjBkGoj3Mvdr6eaffWJacn8WBzi0A9291SKn0dTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به سنگال توسط پترسن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95358" target="_blank">📅 04:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnB_-2J-QXQrl8c3bcDxasSe3neDHD9Fb2ICEIy-SZSp2NBg2WsX1q-pFJbm-mIureIcYIhMr6Wsn5XPfsuDsNKymqA56H9UX__yQ9ma-pLGF_hx_JWCgVqG-q-XXb663T-Y4rUx9HBMkbZtvTKPN1zWCcRjE5AShM2kg0EwZ1pPE1nXhz7PaQ8OK9vqAMkGoyACzdj2ekrfGNIug7Vbd-78T54cvheNzmSelNd9XJc0I17kxUUXwbXM3BTUUYpsVrfWl0E7-mBvSbTGeSEqeDcHu1ivDQWsAudpwDzsUgzT3DKBXwx7Ls5rF5o0YgOCfs9-E1pqPqy3DuRGa5YYgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | جوابیه سریع و خشن به مسی؛ صاعقه‌‌ی اصلی امباپه بود
🇫🇷
فرانسه 3 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95357" target="_blank">📅 04:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eflgykEgXm4Iy4pQTLzDlyOgmiKSrBoVp-0mq0keL9c6rhG-JsSPIA0-rIETYVjyVA_d1yJxd_AAJi63Z1rtaOCyS7OApGDot-wb7BdqAOi6OrYgPKSKOPEOxbqY_xfkDk0RSmOtU4jO_lBgHRUYFWOhMXkaPXCgQ9ftisx0ffkFPPL2NzYc26DJ5ODIeK_y6BDNlzLnxK2QjkAp9-QnYZ7DYZlsEgoAqHlgjtdKFteaOeJD-q5q77-emotVmM1B7bqmaYIfT2fbE4r6Km44yWKB9gRNst8e1cHsLg8QoOn40WiEZGv-TGEJ8Hs3yPMeMuiujgpY9KH6nvIFXtZXqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از ابتدای فصل ۲۰۲۵/۲۶، اولیسه در بازی‌های باشگاهی و ملی ۳۰ پاس گل داده است
‼️
بیشتر از هر بازیکن دیگری در پنج لیگ معتبر اروپایی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95356" target="_blank">📅 04:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95355">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=uj7f-jWUQpnkpPhYiOC_gPsGDLhEY1hHO-USsxctIreK3qh1z8QwOL1_LjhhUEh6X6yQgsqoMBUqhGsQFAtHapqI8JtESfPu8KqVFE6XqTKsxl2KZsN-xYDJrqzGl5HX_UvYXlSDDvcOjSoH09Lbe-SogJatG7BBnjCz_6dzudEVi_vZQBDJFcm0_kgSRCvRLUSd6w74Uys3bPbYcNzvy-4dvs_NCsBMQobZM0-R4MjgEcWUmCpHEWoYTPFCLW9xmUzIudMIkpamzn7LsODtxvvb-JIPfKb43Sf5cV8NrLrfm4nCLhKZCpRtR-YaaRMNF9PrelKiZYOqAChulUHnGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184c9dec10.mp4?token=uj7f-jWUQpnkpPhYiOC_gPsGDLhEY1hHO-USsxctIreK3qh1z8QwOL1_LjhhUEh6X6yQgsqoMBUqhGsQFAtHapqI8JtESfPu8KqVFE6XqTKsxl2KZsN-xYDJrqzGl5HX_UvYXlSDDvcOjSoH09Lbe-SogJatG7BBnjCz_6dzudEVi_vZQBDJFcm0_kgSRCvRLUSd6w74Uys3bPbYcNzvy-4dvs_NCsBMQobZM0-R4MjgEcWUmCpHEWoYTPFCLW9xmUzIudMIkpamzn7LsODtxvvb-JIPfKb43Sf5cV8NrLrfm4nCLhKZCpRtR-YaaRMNF9PrelKiZYOqAChulUHnGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دمبوز هم به عراق رحم نکرد و اینجوری بهشون تقه زد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95355" target="_blank">📅 04:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95354">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=ce6899G-9qMwCWcUxEwzE8gDh1DEUrJnwgw1yPE6lbuR__QwpAiz29uyCdS_CReo56OsxRgEuCSFayfpj9lKQ1bVsfP6rirVJ7Bv4Muztsj6gKQCTX7XfB2SXOFdsapN_DGq7bPIYB7Vj07MbGB_6p8UxJEaz_67vnU0K_FYAL6Buuvng0or3jKeqyBGXkqFZqZrh-rkCGw9a5nxZosVWNuZYQCT_zMnmfXYChqoF-0RwPYNp78wpav-ZJRFGpnWZNbLlbaSpC8jDzTT3Sf9jOFAUwE9-r3sd1QmA4oft1vKDjQB_jHKCgE8aejM6BDxz9g9-vk0wqqL0UhMz16ZVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac3e060451.mp4?token=ce6899G-9qMwCWcUxEwzE8gDh1DEUrJnwgw1yPE6lbuR__QwpAiz29uyCdS_CReo56OsxRgEuCSFayfpj9lKQ1bVsfP6rirVJ7Bv4Muztsj6gKQCTX7XfB2SXOFdsapN_DGq7bPIYB7Vj07MbGB_6p8UxJEaz_67vnU0K_FYAL6Buuvng0or3jKeqyBGXkqFZqZrh-rkCGw9a5nxZosVWNuZYQCT_zMnmfXYChqoF-0RwPYNp78wpav-ZJRFGpnWZNbLlbaSpC8jDzTT3Sf9jOFAUwE9-r3sd1QmA4oft1vKDjQB_jHKCgE8aejM6BDxz9g9-vk0wqqL0UhMz16ZVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
دبل امباپه مقابل عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/95354" target="_blank">📅 04:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95353">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95353" target="_blank">📅 02:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95352">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYhbLsnH17llybIqbkZ8Rusfexf0my10OtLt8j3luK4MkKeIjwYwKmM2PvILDnKe-RQsclAkAtEsbXNGEuNHlqm0n4LTydi_TasuRHlcMDGHPWktyzg_JzorE3zevApbBgTrlZkHeRRUfn35tg32frfIBrQrcJdMjMj8yS2h7yiVWAWyyT3EK_LKrZM3Y71BZ14sMMzDTl3TK0UptWuxhtu-kwr202RwOB90kWhrFM717UIQSdcfvJPnFMT9bLAqISXaZNIOtCQrYFR2FP7p0_6PmOu9mNUiuhzvjuHLAFPyDkIuvr4TIjm9XLfFkgwDAcAPkAud9rFLS2JPcjC17Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
با اعلام داور ، بازی ساعت 3:20 شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95352" target="_blank">📅 02:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95351">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRyH_wPDFpiHZwIw1AfRvHc8KKWPHz68mSbQTk2Hfve0m11fJGuoDUZ2bC3DO7yotFm7L_FJYfXKRlqsyu0znq3fbfahLCxxImvb28XE3hdFghoRiXv63NiOlzW9PkAmuCS9kO2dnrXhWi5v6ZFPpdLU_CUzkziNkFxkyKpJ8lY_LKz8VA-ZktRimzupd1yZwqNVAGxle9jAodTlb-ommYdoGRtBB8viBGD8izd9w-_OycJqVcC1RPQNoOm9ChKAz0wZrYVX7JcDnMr6CSXP1syNAqz3YdSFY8waXj7RI_qCfLpbq0MWuwAGXFkMIsxo0q_UlcoMzI_sdoN5wMXPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رونالدو :
خدای من مسی 38 سالشه ؟ من از اون کوچیکتر بودم از فوتبال خداحافظی کردم و وزنم رسید به 120 کیلو، بیاییم اعتراف کنیم که لئو بهترین بازیکن تاریخ فوتباله، همه باید اعتراف کنن، غرور رو بزارید کنار و این جمله رو به زبون بیارید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95351" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95350">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🏆
#فووووووری
؛ با اعلام فیفا، ادامه بازی عراق و فرانسه ساعت ۰۳:۲۰ به وقت ایران آغاز می‌شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95350" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95349">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95349" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95348">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ctAt1WCgsVnh4VSaKAspZbCxUhZD0dolwJ0ukBsy437I_MQGm-MDhwIvYICVu2erUTY2QFbxJDmLoRMp-KK5oUiFR6eoPPrxH0ucLa1XOGukSGfblPbd4S0fyfJdKTVULc8glVd5dnVvtOnz2TS182-m_2m3FWTfdywvhlV8RzYi7Ri87ZhV-z0fjaRegOMXqla1-5Fmk2is29CSI2UDV4rE0fc9mgMt_0b0QpTlXHdv0qs-IpuQ1elCPmwFas1ZrVn9KIZo6NmeqIrzW220m7W0Wq4xjfXcVBDkieTKKF_SLHYFEjGU2dKtD_RzjWk9JKo029djpeqAPXgKzhNL3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/95348" target="_blank">📅 02:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95346">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
#فوووووری؛ به گزارش منابع خبری، احتمال لغو بازی و موکول شدن به فردا زیاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/95346" target="_blank">📅 02:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95345">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0yaVG_t1DTCfB5PZlV6Ex7gAXcxAs_NPLJVYOskn1HPwdfSPZ_S0-QZM0GFMIB2EdB70VC5OZydZ2FvyV_izRYFl7VQZSRjsLEFZu_CUwVLEN1Yj6aVhm4sEH-cMdwU8IBk9owZmcYNrjo_LP1cyMeCa25NlT-OFRiSUsc-etJLHWXnBYINH7-qSKl5F2tVaOwrnQ6T55Zu7E13YKr8wZgQdhr4snXuf1ijpi8vvayDYOjiwg8yXB2qF-W2rTCNhbVdYmoVGg754vfWjehogqTb6lVFu--No6KcE9B8vx6VB0htsPIBIMgGSmYYWzBfHT3UVpOf0suskJlYhzBQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🔴
سوزاندن پیراهن آلوارز توسط هواداران اتلتیکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95345" target="_blank">📅 02:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95344">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lak6y67zGF4zX7ATjLDdznKy47o41kpD4uK4zkpQ5Zed6BP7lna7j01IsBGL0SuIvwBKHz1BT8Y6VE20vrOoLjet19uzxTDImkcLV-Y8VDvo7SvBALvZI5-wbHlMzRFrDS3cOiVr8EaE9ltGEdHWQlrMTg8C-efTI64CC90kSyqSr63vZBe4LTtNcany_M0l9ZnJFKwV5_U79HW4gtTB88-bShHfwn1we66kF-oobp37zt6FsnESyq-b8lTrAe7CsBKQpzhbEeoPBAxFpM84s-9ZkYzOjPnYeMTLG1gq7Yyn7dQpJB35B40PIyPCrvl67qMUanflqZqLUT2XfHyOIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
🇪🇸
❌
تمرینات دقایقی‌پیش اسپانیا بدلیل شرایط جوی بد لغو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95344" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95343">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
تو بازی سنگال - نروژ هم بارون میباره اما فعلا شدید نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95343" target="_blank">📅 02:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95342">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95342" target="_blank">📅 02:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95341">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
دوباره صاعقه تو ورزشگاه رخ داده و بازی تاخیر خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/95341" target="_blank">📅 02:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95340">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SisQWufFCdmIpXn4I7t29j0yO3dEDXuLe5g120p0a_uV5agQb9Uilwnw3MyjLlLbJkN37-rMKDUlR_kChsiFrpq5AkwoxbAajfAecItc6mEmYKprY603z6LYQ_yh0E_eY5YcMUfyV1Al7KeHQaMm7t8nOTeGPUgZ1XU2izrPkErTWWlIuqIhKwx87gJpbA_IrYieFSaJ2AtiWEe_fDfoNvr4IWNGAYuJ7eUsuHAHMbRNe6gwvCHl6qGwgBXZ2XsF9gYAOn8hgs-dPzeH4tGTPPzYQxAx94960pFSz7Wcg48pfZTHfMUE59z5LUDTtEAy_elzrVnr4KV7_MNmad9Y7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95340" target="_blank">📅 02:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95339">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
لکیپ : بازی حداقل با 50 دقیقه تاخیر شروع میشه، حدودا ساعت دو نیم به وقت ایران بازی شروع میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95339" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95338">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/95338" target="_blank">📅 02:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95337">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtumAJUI1bjU2h_MZejlAYtN9Zvrku4q2RcBULM7SsVqETSRY2nYCO8OWpKhxs7UIi_nifZEfICxGAurDiYqwCdckMpnQwb_VD6qEIgk-GcQUsJQe_1WiUPUPHfQpZcip9Workugf_OYBpfY-lcKP6EujD6uUAoEMNJ5GnAAuyyIT0xJDKwBZlX5qsS5kup1n0ib4J_N41d9nnq6FXg4cgEZ4xCxry1L9N9I7wKA4pDhENJ2YHD3wksYntDkdVlVTPIyPtg7yrUzkiG70lLjRHvIscNlJF43z7IMp_GgEJ3sOCW8CCvgaMGhHE0I4rX8DJutGNbFIxUuviAN47oFVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری
؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95337" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95336">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozN05IENRrV6LFrkzgTHkPEtLWAlfa-dN3P9YoBrdDtAPH3I7iFSs_yxBQZwktQtRFjntYugcfco1XkxgMwHEz0k_KVNOKZRQ7fsuOabof3tloaWG2tRlo7AQQGcqKMJ1q8XIZ26cGE30bfYL82KItrsPfw_1k5YAKCN6vWy52i2Db_N-3W25JIdBzLiR7_0sK5_CB5AqugNa3wUDqDmt4C0DV4ZJfRkxYDaQLBeorkjS4-KOKjWSTgviSChWtJWthxJuRliJG6IBSOgYwvaeEfnvzvaZZtnuEXsjw3kClGF4h9mDpbwfbq2qR9fTLmT34VWftFMy_QjC3TmUDvN6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چیپس پنیرو تو استادیومای آمریکا میدن 8 دلار
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95336" target="_blank">📅 02:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95335">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید با ارائه لایحه‌ای از بارسلونا بدلیل اغوای بازیکن تحت قرارداد به فیفا شکایت کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95335" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95334">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9Qq_QghUjucVKlEVLA7YaUfRjVARe08ViZ76ROPO6ES5HhV7lobi8UEfGolD5KWlpVvM6Zswx5q7TpKQ0ujX00ltUc6sYSkhrHLVibYBgXVOZjp8W0koVgT1jPaMOhisgYygehPaGNOFQ_Q1JtxKYeBEYm3yaXrQMPaTvqRng-6ZMJHEgU7e6YgU1oSSZN0cibVjll_x_E3Z5CEsPv7OgtKKBzn5WZ7HMwOcuYTqNQE1pox9QaqjHoZ76hC2p_DVg3srAexrogK28W8LdlpMn70s0yMu0b0Q9A7eJaxPjbqnjIFxnnaHxhyytGeXsgNaA5BtwG3VElSNss6D6Ekug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇳
ترکیب سنگال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95334" target="_blank">📅 02:06 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95333">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95333" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95332">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/95332" target="_blank">📅 01:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95331">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sNxMJ0FkBnABzsfVDi70HKVPkTZ3gN5DTLu_ei2ViDTcmeUimStnOmTXLtAT78peAfSj5b5Eo5-3wqRajaNKzyGFs6iN8u6F8SjTq3foqH-zRJXFsRTc-xqW1Y_QbC7aTY8Z-WR5DYlcTwbO5pmAc0vCunoFaYtF1BKf8RCNUxV6KaUfNLZY4uoiuhuYKyjZir6E73QXPjO6U1b21VMxjJD2WTfwavxG3AyBdMg0TB_7dVfmmUcTFYbDVyov7uvLRy_1ZOOpdkN1t2FCLpHHdQeUR9nbJWM6tD2gZ--eDNZfogoEIGHPjqM2vg3WDK8vwXzdxI5HvGND34TNkcjN1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرشیو وار:
پنالتی فرانسه در نیمه اول سوخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/95331" target="_blank">📅 01:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95330">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPWrUHFK2bbkQio5lnxrrfPeNHOSiQEDjIxQHlSXJQ-m3Elr1OjsHufbGW07sZu0t-jjCCH_BA4o6JsucezAJdxSe_eIK8hBKxcr3A_doELw2gfCKNb06iY9uhNHyRhwWn3PlsjVoIXIfy7rl7-LG2_zZUfw7JzcHEwfJ0cgvlWTNm1TOQnehSJGxO22FHc7wZMkgUw89FRNl3aFaodz-JnKk62xWhGd7YR4u8x47QxBrXzz_HsPjGYJLKV3xGg5LnZzKN8V2mtfM2rk0YrJPcfyp1C6_26_i8ZH3Msb4xAECaTLNhHZc8x_79Q5gzUmUyK6IoIVC45cIIJgQuRxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووری
؛ باشگاه بارسلونا طی روزهای آینده پیشنهاد جدید ۱۲۰ میلیون یورویی را به اتلتیکومادرید ارائه می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95330" target="_blank">📅 01:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95329">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzCavSTsraTh23b8uiqBalQ9_VbA1wxP9iwMu4LIQ729KEig0_bKDkTJkvFf7i4MaWk7AzcpP4OCus6jqgBBUZBI-CnEfYI28U3KSoWzigYKQBIOMeIGKE7rkXS31ODyKZL2DkcNFqI5xDtjleyFBlKk3SSDqP0E_TUcN6JKC30i22qTZWLWgY-xuWat-HWC59SLJgBcH_8UIIbtRMkHgzKXPxXLDb5v5u36HvjD4pqxCop7YtJTpCPm_nQDg4QLxDiK2CSqgA2Rcq_5mtOITMRrT3a-d_2Xm9wsRr-hjG16msrgMkZ1o1pYAGXlP8KOUTDyq76GKNymbOBFDz0X_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
نیمه‌دوم بازی عراق و فرانسه حداقل با ۱۵ دقیقه تاخیر آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95329" target="_blank">📅 01:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95328">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🔥
🔥
🗞
#فوووووری از رومانو: بارسلونا با آلوارز به توافق شخصی رسیده و اتلتیکو از الان مجبور به مذاکره میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95328" target="_blank">📅 01:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95327">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">پایان نیمه اول
🇫🇷
فرانسه 1 -
🇮🇶
عراق 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/95327" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95326">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-emnCdOh2KV6oSlXoVSgjpRSqZwlVZTN0cc_PorS11Sum0hgiUYWQ7r9Sog4IVsWHa01XbLd-EO1G785RVvTHIt9bc3oQ41DtKBKXzZJRSe9V7Vgws7tXFfu66oM4hy8eRSHZLn7BTgtM-K0LqQwJBVupmxbWglv2ddBOoBb5PBx3AS-cAS-J_7EYg3FUi9n_0YO0yr-P7JQt6JjmLGMnEz5jtV-qGgAlH7CQvV9XjqGzUTz0w2GHLy1yrd4GDOLLadN06JwmunQUGWqqiAJWg7AM-fp5dRXgQqfWyD8NLlNMG8wiiXtdlliuDRL8idcSvNiqxUjem5LxByd1idnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارون تو ورزشگاه شدت گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/95326" target="_blank">📅 01:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95325">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIMfvt2wpyDZwjz42dtzKWp1Gzt9oJqdDYVRLz5bEhx_Pb2cfZMSdVMn10Pf3P7HX4Xhs3Q0KEfDnSiRK16VF0KPf7NuO2MY0i9lkVqrJ679vdKCF-so_7UfWVQy3mkZk0PktkKCb87AWvT27KSrQ9opCuk2nodxv71L6myr3-ZOaKaEdtaFuGLnhYGhIcO4tq-Gu9PYAaKWExehIFgLvV7V4Ik5MQuDjYQ0TLzJvhU136GLZwKzoXG90OzhS_2K2X9eergD1QqCLZxoI7PuY2fGlMLAgycK-bg2OzDTgvMKIl5Iq3gGF0cIjGNYTfoJb4lTOLINE434PkMQ2R8_cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکل فوق‌العاده مدافع عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/95325" target="_blank">📅 01:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95324">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوووووری؛ اتلتیکومادرید از خولیان آلوارز به شدت شاکی شده و احتمال داره جریمه سنگینی برای این بازیکن در نظر بگیره. آلوارز اصلا قصدی برای حضور در فصل بعد در مادرید نداره و فقط و فقط میخواد همبازی لامین‌یامال بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95324" target="_blank">📅 01:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95323">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfugJ7RJTX0kftH3CVTb_9zy19rBGVNZ_z3ZInX9e9ip1gWFr4T9acVIRL1ovVmmWgh1vIVdop6fx0UXCXVq_qBbZH8gwxqPUUIwwObIi7A8HFqi7DnI9fPg2HGi3LwT0uyVCcdNnd_eIjFoyOjE3z2AY7sQSc7W62qG8rueIsjz3YztIo4NMp6BfkzdcFSOiBDEK4kj3dVky_B2hxkeOW3U_Pa7Ehvq9lavTczostOwxL98qWSxWVpp3pRlMS4vR6ew5xs6tjhuL_kFhwwR-F8O6imj7rHW6cNJK8xFDGE2CSSmaNTr3qElLTRuxWeul0J71g_5FK1RYlL23b5UQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کیلیان امباپه به جوان‌ترین بازیکن تاریخ جام جهانی تبدیل شد که به ۱۵ گل زده رسیده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95323" target="_blank">📅 01:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95322">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FZW_zIRGadGKJeLVXVyre3Z1Ew8jpkJqWt-0STeC0ZKtdO2FfMyZXD-fdvyD1Wa2u2y86n0iSG9KByAM602QL0ccD4WL436EML9r5SxzWJTwjSMYDCBrQ_m-fFTj7UC-UkCxqlWOQ-0p_PB6DZ3Ua6-hUlh4MxTp0LkqKeckIinxtkpzuR-tlXgs1nilY5JUF-FHBFKeQMtpb3b-8LVaGcjfc36L6KuTtJrZCrVV2oCssp4sfzzGjIlDYZfzBjpld0T1EKp-P2lhSZIhppOilB9MG9xmDH2WjSF2uiO-0tL3PviTGwoNVpDK4t4cVqnCTStI824yVuXgi7vVtPsWHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیلیان امباپه گلش رو به پدرش که توی جایگاه تماشاگرا بود تقدیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/95322" target="_blank">📅 01:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95321">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=TqazLeGnjko2pwz6A8JnbGp1yL4UsThleyz0umyQd7ratyyqroluV63kh86O27RPBg4Y1p2-1FDp9ikPKjRP904hem8ieoiAlqsn60FIHFpgXEpp9yDeJOjyac8-_rNiYDJVOCh9BIV0t21Hy1p8ugjbrA99et8tJZlCHp_k3a2RnB1XJ7RuByZudhTUaX7GdLdfrD_DXPNS__Z9SbqQ7WZZ_caTRPKu_LytQVe01U_PimI4wBrWdS5YkwSsFq3hLfu697xFQJ0EJIC2rfJzujhZ3wGxb3hiYSA5M3NzUzj2B9RVTwbYlFxyK3wccTS2fCS_ZQiiQ_lmGt8niZ_xME6PA0x5oBglsW_4aGIOPMIru1yujF8l3VX1pNvxfjr6Dyuch1hzXo8EWFBjIwLeA4lrUymUhjhRf-XFDAjYz80jThFBz6EjaN9NiE5UeI36L14zNU0iRQHGaLMGZ0kNsjd8X7v6dsh0cks0cAf8qLlO-dC6zAOIpqYyE5-Yzm0eJaVog-mxvRdvdr1pS_E7JtDUzYVIrApnTKGflwsoiZ7BaV1XbE53dPnqHzYgmJJYV5fr-4f1sDDL_VsXQfPn1QnCAuVQIRT8eVYsG3_nQjAbNjGkz0kE6bQlahtjoFMvxhqIWf90uzec9HTJ0gM-mAz3DhGRIuXWPo9lcjdOoNo" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a9ad943b75.mp4?token=TqazLeGnjko2pwz6A8JnbGp1yL4UsThleyz0umyQd7ratyyqroluV63kh86O27RPBg4Y1p2-1FDp9ikPKjRP904hem8ieoiAlqsn60FIHFpgXEpp9yDeJOjyac8-_rNiYDJVOCh9BIV0t21Hy1p8ugjbrA99et8tJZlCHp_k3a2RnB1XJ7RuByZudhTUaX7GdLdfrD_DXPNS__Z9SbqQ7WZZ_caTRPKu_LytQVe01U_PimI4wBrWdS5YkwSsFq3hLfu697xFQJ0EJIC2rfJzujhZ3wGxb3hiYSA5M3NzUzj2B9RVTwbYlFxyK3wccTS2fCS_ZQiiQ_lmGt8niZ_xME6PA0x5oBglsW_4aGIOPMIru1yujF8l3VX1pNvxfjr6Dyuch1hzXo8EWFBjIwLeA4lrUymUhjhRf-XFDAjYz80jThFBz6EjaN9NiE5UeI36L14zNU0iRQHGaLMGZ0kNsjd8X7v6dsh0cks0cAf8qLlO-dC6zAOIpqYyE5-Yzm0eJaVog-mxvRdvdr1pS_E7JtDUzYVIrApnTKGflwsoiZ7BaV1XbE53dPnqHzYgmJJYV5fr-4f1sDDL_VsXQfPn1QnCAuVQIRT8eVYsG3_nQjAbNjGkz0kE6bQlahtjoFMvxhqIWf90uzec9HTJ0gM-mAz3DhGRIuXWPo9lcjdOoNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول فرانسه به عراق توسط امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95321" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95320">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دیکتاتور چی زد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95320" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95319">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">امباپه اولی رو زددد</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/95319" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95318">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گللللل</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/95318" target="_blank">📅 00:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95317">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVIIyxXqGuDpU-CFGeOwivc4TOd2jY56_tyrjZKglFfR6Gv2veE_bIxWvyy2lDTDNCQj3A4b5Phq1dpUh0QayzWUsbHngRto4ysCt5htqfA2RDbk0y-Wd4HF278k05NBbJzbVC4t9aC6s7MlKz99nYAZZ-BLy09rNVDNSnbMyfn8WeW2NvNR7WyDYr5XJ0Y0W7nDJdaX6VMYeUf-ewSmFp3MkU0z5pKses4Hzo6VKvGel3WWVLO23Ezo1PVLWaAQJt4hduf3Cbk8__-xQDuXdQqeC_3PvjWbGnqJStGvWKcEWfHr8TPL9ZaBVApFbXhLMvYEEw97fCHUzObdusElpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فووووووری خولیان آلوارز: من می‌خواهم رویایم را محقق کنم. با افرادی که باید در باشگاه صحبت می‌کردم صحبت کردم. بهترین چیز برای آینده‌ام رفتن به تیم دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/95317" target="_blank">📅 00:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95316">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYUoYU2XMHk8zxyBHbAFLdWWNs_FAjL32-O4BnIA0NqmYVTMx_20jxCHQkx7L5PpVuIFTKhVjh3twCIwkXq3LjDJ_JHL6yj663qeFZLeLnP--6yj4nGwLFnK9tY2O0JWXD87hDYYmDhLiXP5JWSTsaAZqT-cYQ3UwZFM-eifsQnY83ocbYFMyntDrA4qlPit9Nu5ZMAy-1VBYXthWJLcl6Utynfcx30JPSntz-OXDjs-LC8ut7V4AM1rOb8VIN089OdShVuPxXJtYz_eJN0OwVt2T3_Nyt09-lINgkWwtQ4cAijrSy0cVhW3QDRqFHTxyV9BglIJ7JYdrVBuFmTpHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگار خیلیم به کارل تو تعطیلات بد نگذشته
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95316" target="_blank">📅 00:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95315">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Xx3jwmnVIpzLT6eVtkN1NHOz7Ya-F7moIeVh_jLgv26NZo-U7ynfXB05Uzf2iPwDftldkgLtqav-c3nx9c1rpaZfM6gPytIHDYv16cwLyXWJ2zaUNE8O6J1WbpQ5G9BlaG7sZJuJQbP2oTuG6pszj-UxHQMtOPGVBjpXfLBtuWimuRceZ6We2lG1MKZWSoudkeDj9Wbg5e5I3HFOnPNhKLneTf-chNhdgE0sWuunsL4wm1MXY0jUxFS2-YQoO5TlTlZQ9JIcQIXnFBszFCD5SMJF9q3jydtPq9OV7g3d_cKl-n9vBopCbBGJgsDhjVom9QhpfDgDLY_zjTCh53IWSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔞
🚨
🔹
اوه اوه
🔹
🚨
🔞
🇦🇷
⚽️
🔞
بابا بنازم طرفدارای آرژانتین واسه مسی سنگ تموم گذاشتن ؛ دختره بعد گل امشب مسی تو ورزشگاه جوگیر میشه و
ممه
هاشو میندازه بیرون
😋
😍
⚠️
🔞
🤤
برای تماشای ویدیو روی لینک زیر کلیک کنید
👇
👇
👇
🖥
🔞
https://t.me/FoootyHub_Bot?start=qcipRV72
💯
🔞</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95315" target="_blank">📅 00:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95312">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
فووووووری خولیان آلوارز:
من می‌خواهم رویایم را محقق کنم. با افرادی که باید در باشگاه صحبت می‌کردم صحبت کردم. بهترین چیز برای آینده‌ام رفتن به تیم دیگری است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95312" target="_blank">📅 00:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بریم واسه بازی فرانسه و عراق</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/95311" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Isfqd5iqmd7jVi6mn8e2kp6TcpCl2pm_GmEyE6pv26NPDn29ryYpasQpNRtWhrkV8Zvqw-n4GN51pV3YMENTUORyLM6SYH-WQOO8JdaQZShkYC4VJnXWomUZElhzytT5p7QU9B1Eo_hTfFrlUIOkpIRTmyDIzUbodjzN0bPDZukWvW3TzTIjwfHzzsfbAiF1uKHwwRbO-vREqBQGFpy4wRhjBBPvbSg-K8fN9uVRRmFlpj19KBF3kuDWGZUWk6Hu9ZDYjmFXmdVPDJ5ej5fw0r_BkFzVWHfJXKOaPysx2C0h_gph-es8mPbh4gAYHQyWjhD4zlbwt-6IrcOO3V06WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
⚽️
تفکیک گل‌های لیونل مسی به کشورهای مختلف در جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/95310" target="_blank">📅 00:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f8VKCAtTCcoR_Qf_BrjhnXOPqyE024q29X-0uHqy7b5WAJjfdoGpACJsHkhY5IQZOC3CIpLjUhAoRNGuuSdt-gSBbjbZsnV0TzWlb_58MGlFBpVpLFapLCy8eQphS2CWMCbcU83FU7ENv0NpsG3BNEuyKAcQ4etxsgEEly-5Qdbs1wRNdeZYMt6xBPIqWdNrzAUhhO0LnwHUm_RlT5vErQ57bNqsRb2WagFiOnF9kP2hDzJyaw5Njt2cxN1ovX4TKSKPtRHWpr0eFrOis97B_7wgEMLiOr1jimE3RcK5cBU1LubiTzXxP8hLD5Ix_L3ka0mnPe-vw_HeLe5n_PeDcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آلوارز :
مسی رو با کلمات نمیشه توصیف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95309" target="_blank">📅 00:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODWEpAuKAwMEsvD37QdKMl2OCWOlUckK8oraEyVylbHI69uJEfgf1f42THNsgLfRZso8jR-au1zVjhF9pD3NtyoA2psH_oqX81ov9gR2RRdmR3ZwpKdcg6BBotvXOHVJJ_ONxpHXm0ggTYCUbSRM2y9-Mhdy7bR1eSah_Q9i6cDhAm956bM5CC4YHJu5gxhXaogHXCV225KNbxOFtAvp7VtCGoN3Dmt7JrDuh0hQsIZqQq8gIF8MXCYABmKXy1fvFwFlMXNFKQDye8eoOMnyZlekH28CiLauroIAotxA2c4JOCKXPbt8dRkA69mv6jX6d16Ww-Dnfx6-5iC4XS_uHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امشب به تنهایی شرف عراقو میبره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95308" target="_blank">📅 23:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_Ha6xjuZIKEz-YLx1bd-i3YLCIxcae0tz87Fz-1gff9lmpgIbqm1goOPVpi6YAmbicLIY7NQAcKNzGgGy1wba011yZ5k5Nb202OWror4SqDB_jCHwn_hPyaEhnfIwuzSwpsVHeE1MAD8JzZRQC944CtZGwDt90ok-yW7s1ASSLfULz5IrcoEz8HngY4rpp4mn3WtvW31tkrVWLRxaSxPY0gIPFvMuP5CluNUU3TBQt8UrjxGYybM6eENIqh7y5ip7xhCtq7DS3xjjbWLBaRn5XHS1z9lM6vFe5peVZpa3A7dk7tg-vFHLT8RtVad4aGpPEP3YRv9x9UXg1UzjXB4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورگن کلوپ: ما هرگز بازیکنی مثل مسی را دوباره نخواهیم دید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/95307" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a6777a2d2b.mp4?token=SoelsgU2mBadB2yjT5ldOVO3zLZK37zdBsdrv1plmL0pmtUS3brKPQ4E5EqHt2O4YrPt_CDYlyMM2kEiPV1R1tMIhFdLNsUOBrSjqPN0pqd43xfv4AS39kCatALCySNUB5GmS3v871daEki9EF7vJj44zQrrXGe4FUN0r4FPSomG-HN3dX9OMIROdvsq4ttAq9xlIibwaECOEcX6QTSkFngwZspqlQyMxdAOxafWt4FDIwWuXJ3ptzPtYwkr174DOlp0YzhzhQn7vQT_KC85JsM2k4ZDksxzp1Mw5OzzJBgiKZ_Bv_uE1z-EEVC9gL7JcACmZI4JlNe4FAHQLBl4Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a6777a2d2b.mp4?token=SoelsgU2mBadB2yjT5ldOVO3zLZK37zdBsdrv1plmL0pmtUS3brKPQ4E5EqHt2O4YrPt_CDYlyMM2kEiPV1R1tMIhFdLNsUOBrSjqPN0pqd43xfv4AS39kCatALCySNUB5GmS3v871daEki9EF7vJj44zQrrXGe4FUN0r4FPSomG-HN3dX9OMIROdvsq4ttAq9xlIibwaECOEcX6QTSkFngwZspqlQyMxdAOxafWt4FDIwWuXJ3ptzPtYwkr174DOlp0YzhzhQn7vQT_KC85JsM2k4ZDksxzp1Mw5OzzJBgiKZ_Bv_uE1z-EEVC9gL7JcACmZI4JlNe4FAHQLBl4Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: بازیکنان تیم ملی می‌گویند موهایت را نبند چون شبیه یارهای جومونگ شدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/95306" target="_blank">📅 23:53 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb3ab2e493.mp4?token=T7wBMPACmeu9D6gi_Pxbk4A9KtWH68PrJWKVwUDVFI6PI2dSlx_5QHD_5YNtwktSRyS0Kzc3LcnoDlKWhuQo9DEnFZ3eE-aRyRZMZbP25CMUy-Cl50UZQVbqheMZl_nP8iG-BdPrO2dVbnEwaTdPYCDgXnFeFlpmaUFEVS8nWb4WWrZdv-BDZlaLCADFHzOOcbbY8AEONtNWJZSdv4YZr6sUmWUafyUzOU19ll1Qib5o5-UtxQrrHizJFatUi-rLD1CccrQsCYicA5y-TGXaK8s4ziHp-8M5P968zdPM-TywCwKoOt57PskVs0HZghl_Ry1nrdz0RlxaM6jCdSxjAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb3ab2e493.mp4?token=T7wBMPACmeu9D6gi_Pxbk4A9KtWH68PrJWKVwUDVFI6PI2dSlx_5QHD_5YNtwktSRyS0Kzc3LcnoDlKWhuQo9DEnFZ3eE-aRyRZMZbP25CMUy-Cl50UZQVbqheMZl_nP8iG-BdPrO2dVbnEwaTdPYCDgXnFeFlpmaUFEVS8nWb4WWrZdv-BDZlaLCADFHzOOcbbY8AEONtNWJZSdv4YZr6sUmWUafyUzOU19ll1Qib5o5-UtxQrrHizJFatUi-rLD1CccrQsCYicA5y-TGXaK8s4ziHp-8M5P968zdPM-TywCwKoOt57PskVs0HZghl_Ry1nrdz0RlxaM6jCdSxjAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارزش دانلود به شدت بالا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/95305" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
ترامپ: پولی که آزاد می‌شود برای خرید غذا استفاده خواهد شد و این غذا به طور انحصاری از طریق آمریکا و از کشاورزان ما خریداری خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/95304" target="_blank">📅 23:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b7d3caa97.mp4?token=HgFifMyfd_V9eaRh5w_y4jq9YKxWryQwE8FoLLIsTBFQDlnubjOJKMM8mhd6ApTf2L1YqC-sI9CGe1aTCJ3qkEnn-siHhDsEIQlEpRfxQKMgCfeeKSjWmcpVhHuP16kXsqXmX12ZSEfPx_p87464j3RZv0F3L9lCGut4x6BWJczOAeyXZW8a8zHlOQ2vJi4t-BZzX76zMZMKaH8Ggcua83Mc_7Jlg7SvPisbbTP2S6CsLeMSbnuJvaMbQml4xV09R5PxVpdm7Z743QZoxdVrAI6dKaPPj60HoyQ1EDcEdAkThFVvSHvksQsATrzOYd-D3Wd3J2llm8c5D8N0XxWuVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b7d3caa97.mp4?token=HgFifMyfd_V9eaRh5w_y4jq9YKxWryQwE8FoLLIsTBFQDlnubjOJKMM8mhd6ApTf2L1YqC-sI9CGe1aTCJ3qkEnn-siHhDsEIQlEpRfxQKMgCfeeKSjWmcpVhHuP16kXsqXmX12ZSEfPx_p87464j3RZv0F3L9lCGut4x6BWJczOAeyXZW8a8zHlOQ2vJi4t-BZzX76zMZMKaH8Ggcua83Mc_7Jlg7SvPisbbTP2S6CsLeMSbnuJvaMbQml4xV09R5PxVpdm7Z743QZoxdVrAI6dKaPPj60HoyQ1EDcEdAkThFVvSHvksQsATrzOYd-D3Wd3J2llm8c5D8N0XxWuVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معیار دخترای مکزیک
پول، قد، تحصیلات، استایل، بدن و...
❌
کره ای
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95303" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=SWeh6tPLZPTw_opuFG97lZ08TKvYsnSqn6qhGPIdH7toiCpP35aG8Qas5YJKT5DMxcrI1WGepmPQvFVT4StKDI6H1DE2XHcJz9zkkcyWOoGQf1NHwomXd2NvC-ImkAdtdrequh21fJBwD0n0dSSVQcmQkjaXKmSSKfTZnJQ4MPITKKbxE3JoAYOoEwdEgGyZ-MJRbvW6-bms2M_MSLv7R5WIySp8nAKVyYH1IJ9LK3_4HYOjfSRxvJBLFGKff9PNpeYtHHi1q7E8nvUkqia8l8he22vsSoDmpLma2blkZ-smTFm-YQcME-bFC1yj78zpDwbvCVX2e3aCI2AW8d_ewA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d02fae5a3c.mp4?token=SWeh6tPLZPTw_opuFG97lZ08TKvYsnSqn6qhGPIdH7toiCpP35aG8Qas5YJKT5DMxcrI1WGepmPQvFVT4StKDI6H1DE2XHcJz9zkkcyWOoGQf1NHwomXd2NvC-ImkAdtdrequh21fJBwD0n0dSSVQcmQkjaXKmSSKfTZnJQ4MPITKKbxE3JoAYOoEwdEgGyZ-MJRbvW6-bms2M_MSLv7R5WIySp8nAKVyYH1IJ9LK3_4HYOjfSRxvJBLFGKff9PNpeYtHHi1q7E8nvUkqia8l8he22vsSoDmpLma2blkZ-smTFm-YQcME-bFC1yj78zpDwbvCVX2e3aCI2AW8d_ewA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا بیرانوند: مردم ما ۴ ماه سخت را سپری کردند و همه تلاش خود را کردیم تا دل آن‌ها را شاد کنیم و شرمنده آن‌ها نشویم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95302" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhk6COFRMguG3r5lV1W4nSZj6PEjdd9H3IWTg5U_Q7aqFNOPVcQvhEoISOydBJcisVglJHYp6bAYizkqXpZ6V80Nr0I5-XPnqDm0EPd9HAMujv6A_HvXlyJsoewJxM2mtKJTKp6iO_u1HpsMacNkKnFAGRpfe5vhSbJOQ2MTbfyImhBPNB6VDf1YcDSPs_BdDCzqGkxenyujfhgWxfxjl_MrZKwlKswOL0lmXZENkkVokyH2BRgWsDQgO77L4tKkpN7FfXy--cOoLx6eZF4JzMYqpq5BV7EyRM4pbDNVISNIoL75Y8z5HsI5nrCcDMwid-DbE7fJVHpdOggp3jln3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
لئو مسی با جایزه بهترین بازیکن زمین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95301" target="_blank">📅 23:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Do0Bk_ARUtUXDtE_EyEsK4yMiF0J--JO6Pb8M6wABgT4iJRoEj1U5jg5QZwI4aQmUo-HPtfAQBr0R7_ystQWgmMFNJjoeXV3WemwB4sZ1b2LSceQX8z3d9O3_ClGOf6XBdoZ30vAx5LNHvl4FCkPyEnAfctyEhs0SyK4iQGug124B7Y_ai3qWaVOJIfns7Ty5nO99746MMjbYKmZPzG-1LAAfoivGdfCIzXynM6W8WDFDFa-MKyCXIjD_KEbwpHPo3A96l0JSQ_8X2Ba4egr0nK7watAY7atVoUcIWB_lZ2SXwlgk0s4L0ht2lbYbBSkYcvQYUaoFVqVXmWhoPe1Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیونل مسی در 4 بازی اخیر خود در جام جهانی 8 گل به ثمر رسانده است که با کریستیانو رونالدو در 23 بازی برابری می کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95300" target="_blank">📅 23:26 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
