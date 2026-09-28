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
<img src="https://cdn5.telesco.pe/file/OwJvX0qkJAvfvhOpb0ew87cBa_4SpIi7yaCzriPcO5SkFfk6SZHC35N-sDdMzOSL9jHRlUpDmNcOuzRJqR1OlkfwJAOLP1MWuHnZ4MFXaefMMtkaZb7DacrdIXWEwbRUIXc9QJjiMCD7_GKHl3UHpf9gaXK7HNGdgn3t2zbg9UNxghPAP7exxPKrSjhPdwuqcpavWtY5Ga5_5TmqLVnnIbKaN3GjGXc1SccYV_bHQcWg8uz0xVXNBr-HeIXy2-n2-yQ44KOkf5q6GBwEszimiuBWA7wK-C0qY6xR-JppcjzByVN1DQ9ZgQFeXWuvJ50A-WofYWdSUSmgk0xT6nfOdw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 398K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-107411">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=cMC86RhMq4Dal-KN10t-1p7MKhnvDfZrxu5eFvBHtOFod9GI6Ky1QyxZTMJbDcxgt0zVN-jJyT6_xo1ZOfu6afnmidrYz6ycyH6q04mSWjtf3DQma03cFWWXLt1965yzbpIchOduOL2kwpqw6gBUEegOZksCnlqglGxxk1VA4-ZkcZAEEHdqLoWHyXIBJ14kAnJ47RlD3I8bYiuSUbMzLvGWhgAThwIZypNkQjqc0JxqirGukIKJh17rfSot7kNs8Sbb0yWvOBAL2w_xf0YofjpdVPaaQQB8-nXE7nJOZlYO8pvH3k9vx41mVyqhPrykM6cd4TOvVrKYQtcmCeZp1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2bfc79cd9.mp4?token=cMC86RhMq4Dal-KN10t-1p7MKhnvDfZrxu5eFvBHtOFod9GI6Ky1QyxZTMJbDcxgt0zVN-jJyT6_xo1ZOfu6afnmidrYz6ycyH6q04mSWjtf3DQma03cFWWXLt1965yzbpIchOduOL2kwpqw6gBUEegOZksCnlqglGxxk1VA4-ZkcZAEEHdqLoWHyXIBJ14kAnJ47RlD3I8bYiuSUbMzLvGWhgAThwIZypNkQjqc0JxqirGukIKJh17rfSot7kNs8Sbb0yWvOBAL2w_xf0YofjpdVPaaQQB8-nXE7nJOZlYO8pvH3k9vx41mVyqhPrykM6cd4TOvVrKYQtcmCeZp1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی پرویز برومند در جوانی ادای جلال طالبی رو در میاورد؛ عجب تقلید سمی بود
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/Futball180TV/107411" target="_blank">📅 12:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107409">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RlBZLuJ33Nyc7o-BnNiRCBMXynB_6XcOFGsjwAG55bCJA0MEsdoiWX33qL_xiVJOO1P6Yg9VC9jvmIAUmlsiDTXIPqjcjkGRnGeP-WBE9IcgYlIwFgl6OCub20z94ehvN8lgddwWTfS7SKgANMR4CcmFQrDf5ga1RveqDMAV1itE6u6EJ1nts6ifxEGLVflKWkGxCFh12BTOFR3fXhyIml8BCmRnHz2BsNvmcUDlQ-cbYU8zxK-AT4L-5E0hC0yQZfHdfygVFCWAIM3Li_WvUnPStBQ9b1OXXNwozhhQWBoUMlcqbrPF5qVt511W8Ax2ZVyqO_fM5b1b5kPHGXkDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
بیژن مرتضوی به ایران بازگشت
بیژن مرتضوی، خواننده و آهنگساز، دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/Futball180TV/107409" target="_blank">📅 11:51 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107408">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=MXlHK2s41V1VqKD4mZx2YLJxXf9O60CU6lb2zg8duPiP4OTxFy3ywD_X0X9Iooo0Ukqh4cKbLFFIcOVfRmT-Nh76QejXCNfL3ohVpM5qgmKHU0uJrcaPs3mlAYHDD195F2R5MGH8W4RZjHewRjymrKkAjOB1BXOiAFkhalY3HL5W2D97aJKJtfOGyfL_ykcL_gG-2cCETKdDYAYE-twqyQJfyM8Em1Q4a7BR6yZArsoQAOCo7SzNGo3AuoYoY8oiMbzHxxBWPX-Sy-OYZIRCB9nkMbhj5XQquBbsWLwHJUXNjF1Zh-uC2njA2QnoJiWTGH95gNMGTTZhM6ISk4trYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573c62a08a.mp4?token=MXlHK2s41V1VqKD4mZx2YLJxXf9O60CU6lb2zg8duPiP4OTxFy3ywD_X0X9Iooo0Ukqh4cKbLFFIcOVfRmT-Nh76QejXCNfL3ohVpM5qgmKHU0uJrcaPs3mlAYHDD195F2R5MGH8W4RZjHewRjymrKkAjOB1BXOiAFkhalY3HL5W2D97aJKJtfOGyfL_ykcL_gG-2cCETKdDYAYE-twqyQJfyM8Em1Q4a7BR6yZArsoQAOCo7SzNGo3AuoYoY8oiMbzHxxBWPX-Sy-OYZIRCB9nkMbhj5XQquBbsWLwHJUXNjF1Zh-uC2njA2QnoJiWTGH95gNMGTTZhM6ISk4trYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚔️
درگیری شدید بازیکنان در بازی دو تیم عراق و کویت در تورنمنت جعلی خلیج‌عربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/107408" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107407">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Zr_OsJLL-UbV5C7vx-LZSs46BR3E0W-xzCG9RZdmLEjb-h_CEJNxBjrqa29uiwujQKCvOP6XigXT0KqZL4S9zuXYkyW1iBQwL_Pw249uhniPU5pmUTxb1M1WzMpocMb5GLFr5U5Wgv4PwAqXcmM1-6vZ77CSTFNxdJNU11dOkEE_m5mtwGc_PGm1-mwVW1pkhMtYSXe6E7s9IF8g6I5gjUTkedyPOu_vWjrbWYY2ghEJwa3sygoq72o2O_HMk1mdG99lG-eUkOkowYKPqEjG-N9frPry1LOYvKNx7uyhhbe3VD3HTjEwADvJ8JDkjl_NpLLveNCpxfyuhVe7rYOR1V0usGOucDnaT2bowzM6cnioxug9VpvYwFpfy2TsyBGRC3wUFB28fix8mXPUonhxvYzp4q-d10zIMM89od4UAPfF7VZPS5rnS4Brzhr7Sfj61Ef5TX6G05AtJA7x8NaoB-8fK_0PVkkJNoUmd1SSgvUfNJaB_bHufSEHbiBMS8Yw8tdi0zCzZWlRwYuleNq5lgNX-cyeo0pK8nNq0lhk8_NKnO8Fe4_UTJfmFv0O2FSN5pXs86tQCWdAFaP5ehuAa23RGK_mhp1V3FsFdiXGa5cnRFX5dJY2J_H-ovGakr6BD-3ZSfIIu_uXAGAb-pyeNHGlsG5qwTNCynKAi8EgI6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2719da70df.mp4?token=Zr_OsJLL-UbV5C7vx-LZSs46BR3E0W-xzCG9RZdmLEjb-h_CEJNxBjrqa29uiwujQKCvOP6XigXT0KqZL4S9zuXYkyW1iBQwL_Pw249uhniPU5pmUTxb1M1WzMpocMb5GLFr5U5Wgv4PwAqXcmM1-6vZ77CSTFNxdJNU11dOkEE_m5mtwGc_PGm1-mwVW1pkhMtYSXe6E7s9IF8g6I5gjUTkedyPOu_vWjrbWYY2ghEJwa3sygoq72o2O_HMk1mdG99lG-eUkOkowYKPqEjG-N9frPry1LOYvKNx7uyhhbe3VD3HTjEwADvJ8JDkjl_NpLLveNCpxfyuhVe7rYOR1V0usGOucDnaT2bowzM6cnioxug9VpvYwFpfy2TsyBGRC3wUFB28fix8mXPUonhxvYzp4q-d10zIMM89od4UAPfF7VZPS5rnS4Brzhr7Sfj61Ef5TX6G05AtJA7x8NaoB-8fK_0PVkkJNoUmd1SSgvUfNJaB_bHufSEHbiBMS8Yw8tdi0zCzZWlRwYuleNq5lgNX-cyeo0pK8nNq0lhk8_NKnO8Fe4_UTJfmFv0O2FSN5pXs86tQCWdAFaP5ehuAa23RGK_mhp1V3FsFdiXGa5cnRFX5dJY2J_H-ovGakr6BD-3ZSfIIu_uXAGAb-pyeNHGlsG5qwTNCynKAi8EgI6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
خاطره حنیف عمران‌زاده بازیکن سابق استقلال: هر بار گوسفندان را می‌شمردم، یکی اضافه می‌آمد؛ متوجه شدم خودم را هم دارم با آنها حساب می‌کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/Futball180TV/107407" target="_blank">📅 11:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107406">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=qnPCtBEoMxwmkPxDBgUw2mxih4RG2AK-qLpAtmXX9MQUIlphlngHprKb_LNSrxNFDVIXoluy1oeYaOZXPLsEdOPCyzSSuxzZTRB2kjg5DAEdkiu-RbWLvLrnslaiO-eb3ugMaEO_wZpYBAjwyIcwRGJmoMqrsgef8GKu0xpMjLJnfLiO2I1rYQuK3xxKEvvdEvXjDcQC7fTCuHaZ1IgLEp-aSkku5sPzznokLKSg-BWI4c_9rvRMFtikzsZFUQFC1nL3aoOXQ_OUTifGmM3gwRQkRnr19Vy1gyLzZLQByjmM88h48dPQ9F5kz2diq2zzycbtuGoh2jT6u995T0Srp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/818f1ea358.mp4?token=qnPCtBEoMxwmkPxDBgUw2mxih4RG2AK-qLpAtmXX9MQUIlphlngHprKb_LNSrxNFDVIXoluy1oeYaOZXPLsEdOPCyzSSuxzZTRB2kjg5DAEdkiu-RbWLvLrnslaiO-eb3ugMaEO_wZpYBAjwyIcwRGJmoMqrsgef8GKu0xpMjLJnfLiO2I1rYQuK3xxKEvvdEvXjDcQC7fTCuHaZ1IgLEp-aSkku5sPzznokLKSg-BWI4c_9rvRMFtikzsZFUQFC1nL3aoOXQ_OUTifGmM3gwRQkRnr19Vy1gyLzZLQByjmM88h48dPQ9F5kz2diq2zzycbtuGoh2jT6u995T0Srp4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
با لابی‌های علیرضا دبیر،‌ معافیت بیرانوند همین‌ شکل یک‌ماه یک‌ماه جلو‌ خواهد رفت!!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/Futball180TV/107406" target="_blank">📅 10:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107405">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPahkRxKy8pKk-paRdhGIapWt-uy6TDmXOvhouebIQwAS8pNI4wvPJCdtuhVVFaOQcJ5lEIKoLwx4UHc0DpuoEbJojTwW3R_0TSsX2p6cxUh-m8FU8tbslIkZs_2Gnh4IkY_RJhMpTGgd9qYmTChkSiEYwJZCVPgbOY5cVJxVeAk0iEIjyUdUlyVO6am9wY3bk7Cm_vvQ3_slCQK0qRHcSDiBpOj4Yb1lpF3N2WXVrTyixv5p0oTUzFGjD8RIzOpT9YDGuZjvPWWDdaJO5PIhhQwSwOg0sUBkMys5CGDbjcq6lmre-pFkkhFJvEQmKo5IqgVLcwYuTBGLUkjgptWR2jAI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe4bcfcae.mp4?token=saIdb19OwbH2_hxP5nff8hvftdaAq9fqSDibBXV_U6etZrNpzPJJreXEvEbEbHddSwR8PEnonW2bxhfLxl90RiJywBR6_L4VMdjwcba_0-Qw4JpQGddKNDQTZCKMoHXFS0HETJeeh2nP68gX0IPYXe2-zLMaKmadyGk_QW5_TkYTxAxHy6EJzAApsOX4cn1UHT0lOp48Uu5fOl23sKFpBjiOlp-gk7TxPvBrTfGvmwZJSkaUvr4-z7jYSqrUT1dnXpTlsQPqU_nIg484Xn_hyuKqZqhtVyOrzZjouI1UqNQgVfRgiPVOwUFDhTzft_UEXtt9achUudAg_6mwzxwPahkRxKy8pKk-paRdhGIapWt-uy6TDmXOvhouebIQwAS8pNI4wvPJCdtuhVVFaOQcJ5lEIKoLwx4UHc0DpuoEbJojTwW3R_0TSsX2p6cxUh-m8FU8tbslIkZs_2Gnh4IkY_RJhMpTGgd9qYmTChkSiEYwJZCVPgbOY5cVJxVeAk0iEIjyUdUlyVO6am9wY3bk7Cm_vvQ3_slCQK0qRHcSDiBpOj4Yb1lpF3N2WXVrTyixv5p0oTUzFGjD8RIzOpT9YDGuZjvPWWDdaJO5PIhhQwSwOg0sUBkMys5CGDbjcq6lmre-pFkkhFJvEQmKo5IqgVLcwYuTBGLUkjgptWR2jAI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
❌
آنالیز فنی از تیم‌قلعه‌نویی که مشخصا چیزی به اسم‌فوتبال بازی کردن بلد نیستن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/Futball180TV/107405" target="_blank">📅 10:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107404">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=aa1m5p8q_h3HKuMVKxo5mqsRhAfFRcV2jFl8Jgw9_9q4A8XCrk2a7q1xj-bAqwStWLEn29kSlVxYWkGBRtofs_UnX5cDVVI8n7tpgdWVXTxUxtLqmHbYH0paZkDpMv6wNt7qRbZYgpRUpcOx5AklyBY-QZzIRBWGwvJ8_niYBJl1yzjXI95zaYCpTvFq4ejTih2gffxCe9TOsOYFTHzy0-AJISjYHbOmZWZXH01TTY2niu8YF7hr1fmFnPq816SnjksJB8Sy-mOD1rEAfDDArxT3uBlJg9P8m0844af0Md7d3xvXdz_kTinjq1ofWtQyUh3GsamaPbFVV1GgBnxyhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e340f6f2fc.mp4?token=aa1m5p8q_h3HKuMVKxo5mqsRhAfFRcV2jFl8Jgw9_9q4A8XCrk2a7q1xj-bAqwStWLEn29kSlVxYWkGBRtofs_UnX5cDVVI8n7tpgdWVXTxUxtLqmHbYH0paZkDpMv6wNt7qRbZYgpRUpcOx5AklyBY-QZzIRBWGwvJ8_niYBJl1yzjXI95zaYCpTvFq4ejTih2gffxCe9TOsOYFTHzy0-AJISjYHbOmZWZXH01TTY2niu8YF7hr1fmFnPq816SnjksJB8Sy-mOD1rEAfDDArxT3uBlJg9P8m0844af0Md7d3xvXdz_kTinjq1ofWtQyUh3GsamaPbFVV1GgBnxyhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🎙
مرور صحبت‌های ژوزه مورینیو در ۲۰ آذر ۱۴۰۳ درباره اتهامات منچسترسیتی و پپ گواردیولا⁣
⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/107404" target="_blank">📅 09:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107403">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jScwkw3igrmQCQwZ4QZG1DDvn4mD3Jq8zvV6bicmAYDHi_rLUDGE8qQ_5DbHeNre3jIjjveHzdi4E9pWrIRT-ANNFPibvUbhokfIqsMLcwDvocLWhfh11pKzB0nlFtruzaEdUvSEf_2nkO_9Fw7zA7ipgcinJySqq3_tMmX0JkJpSymIYNfYQP2aZKpjHKhB4VwSssTTF5TleUFlKLOL5KQlh0r7cJ4X4doG4XdPIo8SmN6V83A_rhRFvV6Beigs553ISKHM-7mwLYhVZlMI1u4YWJApRKGhRbXKKvZnVUA-NRwXrrp3CSR-9wgS5aENESH_v48BoNatr1U1znvjWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
علی‌تاجرنیا خطاب به هواداران استقلال: جواب پرسپولیسی‌هارو ندید چون مکتب استقلال بر پایه احترام و اخلاق است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/Futball180TV/107403" target="_blank">📅 09:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107402">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UO5SynNRraco1bP8ZTIJ7Q4uFtJ6G2Z0LeVBASM_CoNkYk0pJp5yChheqSWLUdedrSaGR0xcZ66ePeyBlgTij7lEYYqOoJK32ZZ3qLbM7ZkWLXDpkwqCUAzhPRrLmz_jNyY3GdqJcKLrY0TaL7d_cuSrYJJLCdpLCiB2TEL3VPaAdXWh4svxcraphdkYhMU9kEtkDbynwX9dAfpX1ZQoJWuYvJChDuKd5rkdGq-00h93GXQCEjLK869FiXNc-OxfpWubWour1b-Q22zJrzwXrGbIvfJYwh5iOupF85xQ6i9yQx_4GR-Ah2THd3VbOIkjo3yYKZC84Q_oRVu5tkd27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
۱۳ سال ناکامی‌مطلق امیر قلعه‌نویی در ایران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/Futball180TV/107402" target="_blank">📅 09:25 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107401">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=JXcSc5DnNcUvvh6dES1wILIOFMN6HS9izw9jYimATtguG3bvvtCeAdCDgqTPCUFeorCzCYhYayjynkZpSOwaP8vvvJ3BGudWTq9zh0CELIcr2OPmKhBczPsWHikva8sVg-MzVAEV0Oq-J4VuLffdvwdh0gME5YW6QuL0hkDB1o1W0t1Ke0LYwaNrOHnQIwNDlV5zP3vE73Bg_I-CYG_wNuZAgfhPKRXSQK3Az1aB34FYBG0lxP3Rtb9RlsUfWJEIKq0rsYhOyKtiHzKoXBMOj7nnKDXoHFBFQmo3ZQQpEC1u502e_svPfe3Bp5LBLtZPiWxRyYa45PJNT238oj9qyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f1638a09e.mp4?token=JXcSc5DnNcUvvh6dES1wILIOFMN6HS9izw9jYimATtguG3bvvtCeAdCDgqTPCUFeorCzCYhYayjynkZpSOwaP8vvvJ3BGudWTq9zh0CELIcr2OPmKhBczPsWHikva8sVg-MzVAEV0Oq-J4VuLffdvwdh0gME5YW6QuL0hkDB1o1W0t1Ke0LYwaNrOHnQIwNDlV5zP3vE73Bg_I-CYG_wNuZAgfhPKRXSQK3Az1aB34FYBG0lxP3Rtb9RlsUfWJEIKq0rsYhOyKtiHzKoXBMOj7nnKDXoHFBFQmo3ZQQpEC1u502e_svPfe3Bp5LBLtZPiWxRyYa45PJNT238oj9qyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
❌
مصاحبه جالب بازیکن خاتون‌بم پس از گلزنی و برتری مقابل استقلال در لیگ‌برتر بانوان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/Futball180TV/107401" target="_blank">📅 09:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107400">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=T9mlXy7njtc-PASddGK6b2j5fg0qqg8TvoM2zaQ2VepVqu0OT9R6Ius0A91NVwRIdo5SnK0KMqgNW89p1nX_5HoRw_Q47gg0VcgojmfDpE3a_eTyp4ep9vk9BfWRaUheO94rEXPGUptzPg15mFAErI0ZdQgijlfAmo9qqWu0IwJiFsCpsXWHSqEB83KlKqXf8pOGtRq2LgS-rWHl5EnDFSlmye2M6WtEmp83H8CC74qK5bPFJPZKyk20mPHn1TQNrFBoNxkwLcEsohtdhqA-LO1ljlEg-K68T703TGPjgwgOWDoAr1cIkfAvdKu6r7-xgsu2tKaYx-3ySxjR0GI1Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c65f44125.mp4?token=T9mlXy7njtc-PASddGK6b2j5fg0qqg8TvoM2zaQ2VepVqu0OT9R6Ius0A91NVwRIdo5SnK0KMqgNW89p1nX_5HoRw_Q47gg0VcgojmfDpE3a_eTyp4ep9vk9BfWRaUheO94rEXPGUptzPg15mFAErI0ZdQgijlfAmo9qqWu0IwJiFsCpsXWHSqEB83KlKqXf8pOGtRq2LgS-rWHl5EnDFSlmye2M6WtEmp83H8CC74qK5bPFJPZKyk20mPHn1TQNrFBoNxkwLcEsohtdhqA-LO1ljlEg-K68T703TGPjgwgOWDoAr1cIkfAvdKu6r7-xgsu2tKaYx-3ySxjR0GI1Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🟣
سوپرگل لیونل‌مسی از روی ضربه‌کاشته در بازی بامداد امروز اینترمیامی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107400" target="_blank">📅 07:12 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107399">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107399" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107399" target="_blank">📅 01:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107398">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BpXnuN7e1aa-L0mgoGJzOS8f_ywAfA5k1RdX6zo5xz3R-QqopkdCmRhfbOoCL6bn_a4IhW41_zoDVHaBrlHEyfY9jCKvy_bZfZBp4fFKSUoq5DlO4G0tvlDEUNt-cGOcGs8eY5nyMQc1Jzm5PFaihX9dB-p589Wmf3DrTX5AEoapI1CZgoUFMyovys5Zk8oc3AIN5XEkVSyPzyy3Xj1joR-tsb9CVYFdMrDTxAczXxQxtNeIlkT9pwiB9y8SKOzU120WIVpJuh0Y0QNmLRQFZypIX8uD6WtNIkcpATh5hFpwVtpibXqiYPbbXExod9FGrSzERAzNOf_yYgzZDvfZUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107398" target="_blank">📅 01:19 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107397">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PrJpQ3EYBONlB34etvyi6weYyD63D7smtW4mR8Iy_sGqSQaBwrPeOKgzASeyUwCez6Ku6Rx22a_IAZPJ6UTWDHibVL2YTLb-aBnhMrHoyuI0C8g0wNFkcpZ3DzvdbShAFyPH6JXWq8hsG2OSY_Xt0EdrwGlF6jMJUZFrwGGRvOR45_ZI6RqnkOckYFLRgHgqVwZaHU6ja7eFL-EWlJGpjgzXQx5lkYleKiug2BRHg_p2C2HvTSC9yAHn349te2H2M6CcNiqEFFoTB9b2a9kEBDoiW9lChMmZ_lJ_ayERY47_gGrfRZVIGDu1_y_KPdIoZbWUPO5pO7ptiS2lnrmjGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
ژرژ ژسوس در مورد نيمکت‌نشینی رونالدو
او می‌توانست در این بازی بازی کند و مشکلی نداشت، اما احساس کردم به بازیکنی با ویژگی‌های متفاوت در این مسابقه نیاز داشتیم. این به این معنی نیست که او از برنامه‌های ما خارج شده است؛ ما قطعاً به او تکیه می‌کنیم و ممکن است در بازی‌های آینده نقش بزرگ‌تری ایفا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107397" target="_blank">📅 00:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107396">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tlaow4RKJrqmB-Vn0FpB42XA_K8_yR1ifU50MWIEAtzKv3fregoiog15pzpXJmaDWZt_EJKBYfJe5rwLWB7R74xgk1i2hpplPkhcrD7tbtE0CqH0EayhiEYnMQ2ya9Al9L0h1aS5Al1EZjxqIKDAsQ6aMJePh-0vZIJ3XWrfBEHt37s_74KCwAdlyGq69KP8dx_tab7SFDoiYZXAtSZnUSMIjyTw8qazz6RD5iy0lfK4c0VMeMSG86KSdRb_yKVZMnE39mCiBKFw6YOrFuLBw-RjbC9Ymipoim4APCsi8erKZZ-M1E_a3vjgdyojuUeQs2U8RntLcSLPUaSgVRR83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
❌
آلمان تحت رهبری یورگن کلوب:
❌
تساوی مقابل هلند در اولین بازی.
❌
شکست مقابل یونان در دومین بازی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107396" target="_blank">📅 00:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107395">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-VdZHYeB1GeiD0ydW-z0yN3yju86BcmGNT5CZrhFeaDPs7Mbyvf14J_bZ_z29418Q1Wf1EAd9XjgPlml-0Ci8-Mrwm7XNhnCDjY8wcRcmnytu4RQfAP7z5poo1pJjVSnFvHpYB2lt0YhxsGmBunPsNlkZjscquoSiNpW5hKDoq_yKAfj3c6ONNRs085gzwZDICTWPBz_pYOHvr4zqfbXh93Lt-3lXVcMmSv251Nf0E9UdN2bpcrx_ASO4kRZPv96pPiZNREGbwmkvwsvEJgvUlWvElvrBYWK1OGWnIY3RB80IXFuDpYSDM4wsPONKhkQ0dzlFKJ1v8XthPjpiiwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🔥
ارلینگ هالاند، [65] گل در [57] بازی با تیم ملی نروژ.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107395" target="_blank">📅 00:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107394">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HQFGuzUwcGPrhIgQ-EOUM4E5m6ONoVtAd0O568mdXfe2h_O0jn7psxI32xqsVWHbhZiLQMv2wjEQh1xs5HSUHbTf5Qr9cbO_T0WBqaw4V6iFmZGWUJQsSrdNdLf0HkZoixSFzU6dzseTOXtBU-hmeoYYrHcb7P5rOAa7H57oU_JC03MTAOcSPwhLZXIvYPtSyRprUJZB8AiivelgpHcSnpSla-lFpNJQ667JaowUnrPOxQecNQ2iiLQYCGgTGsFZ5gYgEeFT1H8NqVA9_vIWU9yk6nBKCgrakH9Sdnq_wKGgLjbkZfmYdmbmwjuRsfgYPmTu2Dbuk09s7mgBjk3s5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107394" target="_blank">📅 23:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107393">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lt_VBf1TCj_PljqQTOBgs9KOQ6-SvePMAwVe5f277wAYoU3CFJGmSBk3CbEeYOvEgIjImaSBCqHXcvABJCHLy81OElp3Z7vXkoexZ8jJ959AZ5y7_OY-YVWLr_zlJqzfFV9dQsxt8WzcUwzW-FztlObigKZIBtt1Kfg4BBCBgBw2afrJgwejtMZlTBuGled9B8h2KwS9_aZNghOx_KR5BWi2PKORE7dyTCMa-uOH6mc2AR_8ysYuP-o3tH_U_HvUW5w6HIlg3eYdcOyiYpQsOAJQDGIhDM7pv83TLlOZwslIVZX02ZQQMqdz5IgaJTYi6XP-xDz-mLbFXY0B5dsThQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107393" target="_blank">📅 22:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107392">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/arug7IbFiFOiMSxgk2Yea6QWVKTpfOg80q-QKA52aQdZ-a26OgSZ2yiFQ2suBedKAYJiH96W6NyLzpAuq5CRUjlNk7J7pFdyjy8chMh6mTQFgiZoumZsyU6SyjGjXrbox15thPXDwekr9lRtiBzdKSlClVMXArM_svPREBozeljY4JvXZdLqy-mZ-duKfaHnKAXzl6odyts2PHEWY7rXSXoh6i3hPwELYtE4LU9IGDQfqxhSaVIsnluCYasYYPPDV8AvbJpCe--5nHGGlhlN5n1MuVGZjJGe94NtJwxr8Q2ROwVUa4RhuT2ldCN8FE1jWH_VigoxYbLj1M2edE8b4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
امیرمهدی علوی سخنگوی فدراسیون فوتبال: من نمی‌دانم چه کسی به علی‌تاجرنیا گفته که جام قهرمانی را به استقلال می‌دهیم. هیچ‌ بحثی در این زمینه شکل نگرفته و صحبت‌های مدیر استقلال برای نمایش است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107392" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107391">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8aLanV-w6ordvVmL2dKOLbRikHbs6KJlsxNGnPq7Nd28eIXFFXM9ZQ6aCjbqFLC43yGrwhUNta33HJ2OqVU8_I-fuho9wIqsXQKKLZK7DxMJ8icVVBCl-BiosW1QGiilwCZUVY7PYOCF3mqqftY8yD3pw2eZ80FzFzG7ZJHJfaboRZYZXqrmql9B3Fz8hAyy65baxKle1jZLohct_cP9Uy-_G26T9TTzzrREKmVx8AoN7fS31J9p9cVXHc8Vv7Q4V6_n0rRHXF4FYWibZjh9BtH3zzG40XC1OgM00S6UUcRLU2sjF8ab10doJOxoL7DeInK_pHX2avQDxrdGVW4eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
کنایه معاون فرهنگی استقلال به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107391" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107390">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ImDK21RBbe_wCAoF_WntuLLCvYsDWCnvW1uV6s-BsA1hy3vtq9sWa3eRdZIX2nQfG3NQ9TKvn-9a7t97cwSlaW27bFii2VeaKsU4w29UNfDUxOTAnNfJ1omSrMVdqXiqRVFOr0yxf7c-uFfVc8C-eJc0WGbspgiD846JX3uHErONjqsxaItXh1sUy6x7kSojUullL1Qba996ftpcE3Ds2w7B28EMi06I7mirU9aocR7DAiPLP4n4xeceBkB85kSsm6Wc4QjZOFmaTR-WR38zZsqdi6srTIClS_0r0lCVD5_7g60PWrMatwZ2uNC7ROw0rbMTcUJJ139MU8sTFPhGog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
رونالدو روی نیمکت پرتغال مقابل نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107390" target="_blank">📅 21:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107389">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=qFsTgEBh6LHN0GoQFc8BK18_fwBVSSDghE_qDCg74NKOkfcn5TAoeRKHgk--6kcZPOrX2gDnNfRxqt0DptI4_nag_kmPZiDj9JAYuTnR3dUtWOIjEduMs1Bl1U7torv8YZKp49PXNqL1Lbon7wp8djo0HtQlIq7-jjVU4CA4OjgNKpNsQpShwEUYVwO8eCZFIj88rxDuc80tDrD6bjZJi9kTRV3ohGd22H7BqoxrhF5M-mwB4Z31OqczQHK2cHGFdupAULwhh267LMlUpgff8hFCRGebnwQewOj1CdRKl7xGY01OC7rw7nnFJ_3bsJDciW7zx3HkTFC268koURnrmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2062dc3d8.mp4?token=qFsTgEBh6LHN0GoQFc8BK18_fwBVSSDghE_qDCg74NKOkfcn5TAoeRKHgk--6kcZPOrX2gDnNfRxqt0DptI4_nag_kmPZiDj9JAYuTnR3dUtWOIjEduMs1Bl1U7torv8YZKp49PXNqL1Lbon7wp8djo0HtQlIq7-jjVU4CA4OjgNKpNsQpShwEUYVwO8eCZFIj88rxDuc80tDrD6bjZJi9kTRV3ohGd22H7BqoxrhF5M-mwB4Z31OqczQHK2cHGFdupAULwhh267LMlUpgff8hFCRGebnwQewOj1CdRKl7xGY01OC7rw7nnFJ_3bsJDciW7zx3HkTFC268koURnrmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقاد شدید مجتبی جباری از داریوش شجاعیان!
مجتبی جباری، سرمربی جزیره قشم، بعد از تساوی برابر فرد البرز، به انتقاد از رفتار داریوش شجاعیان که در دقایق پایانی بازی در نقش یک مربی به جباری مشاوره می داد، پرداخت و مدعی شد هیچ بازیکنی حق ندارد در کار فنی دخالت کند. جباری همچنین خاطرنشان کرد حتما با شجاعیان برخورد می کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107389" target="_blank">📅 21:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107388">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dki54LLhNgsGEBkfbczU6qqE3X_aY-GeuEkelfErAVrz8q1CIZl55Q3815n27mCN-9L4aLdl5DKIKxt-fEw0h6wV0wytKSnXxeYQiFkxcHC2PZy-3Fdinu1rmJo4rIgUVItr75hp911HzQJzBDP1h4CXrAZgLVa9PlFaRQT9KoBF8BMs17D2MycRliTzZ_u2rLZfuccGcoAWY_RgcnhK8UI9qfcCtbAEUfjhP8IdWCh2uKz-3a0DCDK1w1OUcnRtmUjgZMNR7misP233b5xtBpBsKFlrGPlLeK9xkl4_5cnhSsud6Dt6gYri_9m63RUu-x0b098WkpSnGPbgB3FFAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
🔴
استوری تتلو گونه‌ای رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107388" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107387">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaCZ7ChLAo0GJuJ4luyxCQNJrIq5CvMY39svKDyCWBZY8STwyys9xDtSHSV29TZkEqkT4QcvsgyIKu-s5tSNOi1owqQrLBSyoCbQOGKOcMRMRbct5FukvyzpEu70ncER3k6eExiXAdPbSMSrwFW-NYk_bllnrqQcF2nTmzLf91AurmITDHqCFq8SBvb3ZtCvUmyAERq5wkejZPuovzDMfTtARfJ5-zvpbk2iVq0n3XTtwkyjDBaksnFDeHTBFN6tjSHBrubqFk559HZXBuiWkIS-1qiIpOfbAN2WquUJA6UIEGNb8FFK8tDe-fOhTd_HLYx-yyth6KS5lSJmAk0ugQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
صحبت‌های تند زنوزی علیه سرخابی‌ها؛ جام در منیریه زیاد است با هزینه من یکی را بخرند!
🔻
تا جایی که ما به خاطر میاریم، جام قهرمانی رو در زمین به دست میارن و نتایج مسابقات باید تعیین‌کننده سرنوشت تیم‌ها باشه و شایسته‌ترین گروه جام رو بالای سر ببره اما متاسفانه چند سالیه رویه جدیدی در فوتبال حاکم شده و بعضی تیما دوست دارن بدون مسابقه جام ببرن و حتی فاتح مهم‌ترین عنوان ورزشی در طول یک سال بشن. جالب اینکه درباره عدالت هم صحبت می‌کنن اما در روز روشن چنین ادعایی رو به زبان میارن.
🔻
یک باشگاه میاد به زور و با زیرفشار گذاشتن فدراسیون و لابی کردن، باعث و بانی برگزاری یک تورنمنت سه جانبه میشه و دیگری میگه جام رو به ما بدید! معلومه چکار دارید می‌کنید؟ البته من دلیل این تلاش رو می‌دونم. هزینه‌های بسیار گزاف و چند همتی و خارج از قاعده‌ای انجام شده که برای توجیه آن‌ها باید هرطور شده یک جام بیاوریم حتی اگه تیم‌های شایسته‌تری وجود داشته باشن!
🔻
به هرحال در خیابان منیریه در شکل های مختلف و در سایزهای مختلف زیاده. اگه دوست دارن می‌تونن حتی با هزینه من برای خودشون جام بگیرن و روی پوسترشون بزنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107387" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107386">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=rIA56L5J2tSdrVf7DhdRVsw_2Lymr05kTmPJz45UbCMl78TwZvdQt3CDxs11gWYt9THB0iP0sQHeC0zkRsQiuFs1Ph6dZnKNNG_cv_6iUFJxx7vyJfmZW2tnvI_ExuWOcA80oOgfZwH0vSS4EnomQU9FjFgY6PdKLTuLTHzvSeB7n_VBAtBcoxlW_FJ5hxgNSc2ERSz660QvdSI0QxJQGFCm4u574QVBFR0hCAzWvS6b2RYPMItWfQ9p97xCaein_pinumQ7UsEs_CALKLqfwmrf6HxQotXkMr9tPF21P12pKcW3QYnt1hOi7L9I1zwVFP0K9yCLAHOg698Xj-6iXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbc500f316.mp4?token=rIA56L5J2tSdrVf7DhdRVsw_2Lymr05kTmPJz45UbCMl78TwZvdQt3CDxs11gWYt9THB0iP0sQHeC0zkRsQiuFs1Ph6dZnKNNG_cv_6iUFJxx7vyJfmZW2tnvI_ExuWOcA80oOgfZwH0vSS4EnomQU9FjFgY6PdKLTuLTHzvSeB7n_VBAtBcoxlW_FJ5hxgNSc2ERSz660QvdSI0QxJQGFCm4u574QVBFR0hCAzWvS6b2RYPMItWfQ9p97xCaein_pinumQ7UsEs_CALKLqfwmrf6HxQotXkMr9tPF21P12pKcW3QYnt1hOi7L9I1zwVFP0K9yCLAHOg698Xj-6iXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتباه وحشتناک ووزینیا بهترین گلر جام جهانی مقابل مالی در لیگ ملت ‌های آفریقا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107386" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107385">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=iJQzNaaVNWWOYZd5V0RQVNSkT31GS_jghZl3JIRIaZASYl2sK9PiL7s1KIsRuCTOKKx4v0WjlVLktr--CMluc298m5u8r3sgIhdqW4a6mAceZu410pAsd7GLbZbG0iYB6v0FyRBCfYOQH0hSI7lwFPSafSRfIMbX7fDmq7rhuoy3-EmHKREfpO2xDz92kWR8Rh5W2vHXgObbVI9KQF1yO_vEhVWcFhd6aCmU8hfDpuCLHv5bAThwsjsHmUF3dX_rI46HAzm_cmX4E42xVRiRYY8Pz0r6yfXYsM3UpMhmoJsGfxe_d2RVv5PdCbFNa_q0yJxWJ_UWVtdGh1eSjQILVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ce2bef5a1.mp4?token=iJQzNaaVNWWOYZd5V0RQVNSkT31GS_jghZl3JIRIaZASYl2sK9PiL7s1KIsRuCTOKKx4v0WjlVLktr--CMluc298m5u8r3sgIhdqW4a6mAceZu410pAsd7GLbZbG0iYB6v0FyRBCfYOQH0hSI7lwFPSafSRfIMbX7fDmq7rhuoy3-EmHKREfpO2xDz92kWR8Rh5W2vHXgObbVI9KQF1yO_vEhVWcFhd6aCmU8hfDpuCLHv5bAThwsjsHmUF3dX_rI46HAzm_cmX4E42xVRiRYY8Pz0r6yfXYsM3UpMhmoJsGfxe_d2RVv5PdCbFNa_q0yJxWJ_UWVtdGh1eSjQILVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی برنامه نداره ...
وقتی حمید استیلی میخواست برای فرهاد مجیدی
در تیم ملی امید دستیار ایرانی بگیره ولی مورد قبولش
قرار نگرفت ، در ادامه به مجیدی میگن چطور مربی ایرانی
برنامه نداره ؟ امیر قلعه نویی رو براش مثال زدن اونم گفت
که اصلا قلعه نویی برنامه ای نداره
حالا برگردیم به مصاحبه کاناوارو سرمربی ازبکستان !
که گفت تاکتیک ایران فقط ضربه آزاد و کرنر هست
چرا قلعه نویی باید ماندگار باشه ؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107385" target="_blank">📅 20:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107384">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=c8KkTjpJTswy9PXhuBN8AN4S5SxvYpwO1tQcSE5TzCuzKhfTGyAnmMSN2kTFGSTqGhI3a0aU1r1kUeuEXdp5h8bFboo907JdMauy2tsoHAJKpPwedr2X40Msew4ZfQZ6k8TPuRLXbQfSyrceFBi3xOvx7bkc_7DnwHh9R3S1ULc2JVFuun_JJesPAFox4xBin2ddVLLUJadgOAR0NRtuFs47RikaU__6oIvSSAGU1x-wZW7rDy1BEkk9muN2ysNYmUWeTmFMdgGg9aHOIz91ZQVR2O-VZETrPlwarw7YmKtDWc66rMdJYFVrkIK5rWRbDjTxF4FzoVTb7Cf_vouf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbd8f68cc2.mp4?token=c8KkTjpJTswy9PXhuBN8AN4S5SxvYpwO1tQcSE5TzCuzKhfTGyAnmMSN2kTFGSTqGhI3a0aU1r1kUeuEXdp5h8bFboo907JdMauy2tsoHAJKpPwedr2X40Msew4ZfQZ6k8TPuRLXbQfSyrceFBi3xOvx7bkc_7DnwHh9R3S1ULc2JVFuun_JJesPAFox4xBin2ddVLLUJadgOAR0NRtuFs47RikaU__6oIvSSAGU1x-wZW7rDy1BEkk9muN2ysNYmUWeTmFMdgGg9aHOIz91ZQVR2O-VZETrPlwarw7YmKtDWc66rMdJYFVrkIK5rWRbDjTxF4FzoVTb7Cf_vouf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
وزیر خزانه‌داری آمریکا: اقتصاد ایران تا دو هفته دیگه نابود می‌شه
چون اونا فقط ۱۵ میلیون بشکه نفت روی آب دارن و بعد از انتقالشون به چین، هیچ‌چیزی براشون نمی‌مونه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107384" target="_blank">📅 19:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107383">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=jz19gJahTw1aWQ11AFNy458SCPwOVa_Ekt_c_VE_Bc6TAFvYFqqS6elXtZCNykx9WIDzYvO0zcVZJdTMOfa9PQ-EJa6dv0TrWOxCdAO2zjHNEyTLJucw1Q6ZJR3ZGgKMS4YtuKKmWx0V-6eXvvqW08EhJ46PVI9CztMdcBCiZmPO_BzImlIYWXLkKxJG2P-maf7_NDA3DzbfW2RCP6e2wnCnvuY3vdyNXR9qccZFBUO3JCCfbGSpilr2ayQiUf9umoVwIigCauE1MFQPdi9TgBBAZLWemVcC_5AO7rJYSPFJq5MCeQpTBzmXd2ZWmpSZmPOwNIMG0G9hsMplVyVZLjZuXdRhjZugX5qQ81PQJMAsy8r-9Mkufy5C0XusQMk0DA0LC7EwzQx-X8m7UW-3gH3ST0j9Ywjl8zLZzQ8MpTuef87PvSLt0VBFQXBC1avUPeLGwYK4dReWmoAPb2E1PFED6Ar093ujBOk1LcRmhrw_Af-N88VpGRcy__cPb-3yTbWYpPQkqV67p-RDiBzSXYPPS5SBJgi1gHuVVdlCctGD-LU01YeODlC2wW3m8tMJk9WNosc169No7TPaiR8BYJznUWwrV9DmSZn_pwBxe5X1fz48nEJJRPcLyKAXKXfBPatoJT-jH0MKqKAvnLluOS46jThZGApbnNivznuPbWc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8f6084ad3.mp4?token=jz19gJahTw1aWQ11AFNy458SCPwOVa_Ekt_c_VE_Bc6TAFvYFqqS6elXtZCNykx9WIDzYvO0zcVZJdTMOfa9PQ-EJa6dv0TrWOxCdAO2zjHNEyTLJucw1Q6ZJR3ZGgKMS4YtuKKmWx0V-6eXvvqW08EhJ46PVI9CztMdcBCiZmPO_BzImlIYWXLkKxJG2P-maf7_NDA3DzbfW2RCP6e2wnCnvuY3vdyNXR9qccZFBUO3JCCfbGSpilr2ayQiUf9umoVwIigCauE1MFQPdi9TgBBAZLWemVcC_5AO7rJYSPFJq5MCeQpTBzmXd2ZWmpSZmPOwNIMG0G9hsMplVyVZLjZuXdRhjZugX5qQ81PQJMAsy8r-9Mkufy5C0XusQMk0DA0LC7EwzQx-X8m7UW-3gH3ST0j9Ywjl8zLZzQ8MpTuef87PvSLt0VBFQXBC1avUPeLGwYK4dReWmoAPb2E1PFED6Ar093ujBOk1LcRmhrw_Af-N88VpGRcy__cPb-3yTbWYpPQkqV67p-RDiBzSXYPPS5SBJgi1gHuVVdlCctGD-LU01YeODlC2wW3m8tMJk9WNosc169No7TPaiR8BYJznUWwrV9DmSZn_pwBxe5X1fz48nEJJRPcLyKAXKXfBPatoJT-jH0MKqKAvnLluOS46jThZGApbnNivznuPbWc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🎙
تقلید صدای باحال از گزارشگران مراکز استان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107383" target="_blank">📅 19:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107382">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/464a64d711.mp4?token=Z8Iphd5etdqb6qU_HrF2hN5nTxxnAtjR4Ts3t9SX24GqXPllRKx8JHgRSVsJhg0lAc7TKEUwxeppWohdM0dXoBlEPLaAnqdi2FyVlmM6lDe_I90lpDUqbMB944tsxtRSAHUpbFt2G-DlNev6wMdMlo9GJpfFT_BZY8BRQQB9j7Ezxj_HzdJiBk1eTPCPfYN-jzN02Tn-wi28yxtyAKekyPUwsJcW9sDr0OOYz2-hafrsinxoodumZKudXkvMwEFdx0ntJvMky5vQL7Oeb8C283vZ7rGSC0YCS1aKknPvz0IfQnZTFKaS3FL21ai5HoSFeLX1dgE0AuOI_smZJb4sBnkaag1j6ETMuYhrmn41_81bgQeyrItcOq8pxYRjP45GJb_35UtBfi0aZ5Ox8ffxNvzKhxwZCFK8klHvUWpFPepXGyPwzy5xZUI2e4FChvMlRFO3dv1UnsBpm2ihhEOT1GkHMoH4yEt-qEO7oHanlmpU9JZ5YdYDfY3EXEzsj-tf7RuKffotHbERrlgSATgBoaH3uj3a_78t5XnjHlFJsg2HnSZx6UJ1f2w26uJTN6eGLQWC3UbKncJdoYPMpp1l_es6EYULjspPuNn85kXPJmA70jg3N6C646HxUXxtvvPZ_S6XLpvHe8HBXJf__-DHAL-be9TTwbDTiIno-A6TxJU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/464a64d711.mp4?token=Z8Iphd5etdqb6qU_HrF2hN5nTxxnAtjR4Ts3t9SX24GqXPllRKx8JHgRSVsJhg0lAc7TKEUwxeppWohdM0dXoBlEPLaAnqdi2FyVlmM6lDe_I90lpDUqbMB944tsxtRSAHUpbFt2G-DlNev6wMdMlo9GJpfFT_BZY8BRQQB9j7Ezxj_HzdJiBk1eTPCPfYN-jzN02Tn-wi28yxtyAKekyPUwsJcW9sDr0OOYz2-hafrsinxoodumZKudXkvMwEFdx0ntJvMky5vQL7Oeb8C283vZ7rGSC0YCS1aKknPvz0IfQnZTFKaS3FL21ai5HoSFeLX1dgE0AuOI_smZJb4sBnkaag1j6ETMuYhrmn41_81bgQeyrItcOq8pxYRjP45GJb_35UtBfi0aZ5Ox8ffxNvzKhxwZCFK8klHvUWpFPepXGyPwzy5xZUI2e4FChvMlRFO3dv1UnsBpm2ihhEOT1GkHMoH4yEt-qEO7oHanlmpU9JZ5YdYDfY3EXEzsj-tf7RuKffotHbERrlgSATgBoaH3uj3a_78t5XnjHlFJsg2HnSZx6UJ1f2w26uJTN6eGLQWC3UbKncJdoYPMpp1l_es6EYULjspPuNn85kXPJmA70jg3N6C646HxUXxtvvPZ_S6XLpvHe8HBXJf__-DHAL-be9TTwbDTiIno-A6TxJU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
⚪️
⚽️
چرا تیم امید همیشه ناکام است؟ این ۱۴۰ ثانیه از فرهاد مجیدی را گوش کنید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107382" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107381">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107381" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107380">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/h1C5bR3fa4-wv_NT6_ZJvxSQYVJPc2M5td2QbWFtH7BdciJEPqmj0ncPGP-gKHIJ9ctgxgnqpqurJ8Ie3n6a8GFd01RvD4mLYKAdXYKiXn-N0ED3Mq1rqCmFpIuTVSzse8Q9CVcE6WnHQ7gEReBeT1GI5Gi-1v7yKJNdFWb0zBy1XyQ0bViF_ddSW1oGFkpRkcpy6q7JBRHxwAsl3MkBqp1Wewpsgkp27DJhO4I8mNbSYsfMdeoCU7dj55Mqqdq0_MCRJnZ8_0oEkzlA0GyIhF0Yvpfz8o5NCvsJQ7SZigbjYVNvvhM9hXZ0r14Mc-vEXlp2A3qbALgxdJBTeDGlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107380" target="_blank">📅 18:51 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107379">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36187cd975.mp4?token=BdKyDJTEpfHt0NYp36L4N1PIk63pwH6K6FL1VYZ6QobZV_0r9gEm1VwN8XTJ35ZkZxpmoMD47s54MuGI5Tj3ydBTUsi1Y1ZKCOWCBbHa2wR610xygSFFv7Ws2_j5geMilGeK4Q6-lBwPwHpUoT2Ztu4MFJJRerJbCXf2LNbrItl_dMPMai2UKC6fZQFEg3cdxbpW2yzvFZvFKGXoIqrhzU8KzXeg7RSEh_HoRmobK6VhI3F1MlNFiZoSzYEJjRmg9_4UYQMchaLSIv60ZkrKyUpyTX744SjLpR49wYrC1DEgUPlU8cmtRvFw8cnjhq9TEvj1V_3ohwIMGecUj4PaHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36187cd975.mp4?token=BdKyDJTEpfHt0NYp36L4N1PIk63pwH6K6FL1VYZ6QobZV_0r9gEm1VwN8XTJ35ZkZxpmoMD47s54MuGI5Tj3ydBTUsi1Y1ZKCOWCBbHa2wR610xygSFFv7Ws2_j5geMilGeK4Q6-lBwPwHpUoT2Ztu4MFJJRerJbCXf2LNbrItl_dMPMai2UKC6fZQFEg3cdxbpW2yzvFZvFKGXoIqrhzU8KzXeg7RSEh_HoRmobK6VhI3F1MlNFiZoSzYEJjRmg9_4UYQMchaLSIv60ZkrKyUpyTX744SjLpR49wYrC1DEgUPlU8cmtRvFw8cnjhq9TEvj1V_3ohwIMGecUj4PaHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
محکومیت ۴۰۰ هزار دلاری استقلال در پرونده کاریله؛ آیا تاجرنیا طبق وعده ای که قبلا روی آنتن زنده تلویزیون داده بود، مطبش را برای پرداخت این جریمه می‌فروشد؟ آیا دیگر اعضای وقت هیات مدیره، طبق گفته تاجرنیا از جیبشان این خسارت تقریبا ۹۳ میلیارد تومانی را می‌پردازند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107379" target="_blank">📅 18:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107378">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=RFNGde9Qa6eMcy2gfcIGBSFncvwpMeKf0F_3_FKYzP-rL4ZiDPGGcnA3DZ_ODx61r6q-7RYC9B1u4ulglZINuOMoY8fWkJe6Ys4Bx3DCJzIDw2XZKd3b_hPLswqg6kpVPjcS--fmM-wwC9GXpsT4aDNkVPoVb-rDNziqXuea8o54Nx-W6u62XcYqxn28ue5Em6u1WJnqr7tuq2WgHS-BkDli0EJQxPD6yRLkZacPdALPsl5f-aq5mtYZ1znal_c9j7fc6CEmpMmLlPX3ze5_rEghe6qGvBRVnpmrXdMCc7eOapKcjrTtRYCpp97-7k3w8r4cZMo6tCJ2s8jpah-T-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ea1431c1f.mp4?token=RFNGde9Qa6eMcy2gfcIGBSFncvwpMeKf0F_3_FKYzP-rL4ZiDPGGcnA3DZ_ODx61r6q-7RYC9B1u4ulglZINuOMoY8fWkJe6Ys4Bx3DCJzIDw2XZKd3b_hPLswqg6kpVPjcS--fmM-wwC9GXpsT4aDNkVPoVb-rDNziqXuea8o54Nx-W6u62XcYqxn28ue5Em6u1WJnqr7tuq2WgHS-BkDli0EJQxPD6yRLkZacPdALPsl5f-aq5mtYZ1znal_c9j7fc6CEmpMmLlPX3ze5_rEghe6qGvBRVnpmrXdMCc7eOapKcjrTtRYCpp97-7k3w8r4cZMo6tCJ2s8jpah-T-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
درگیری شدید سوبوسلای و بازیکنان حریف در بازی اخیر مجارستان مقابل اوکراین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107378" target="_blank">📅 18:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107377">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=EN8mY1K_g4kA-0r1hJmvrdZtT9VCFk-dmjC1x8NjYrgbH2IMKQkIEN649roDtOupc_8Gxt6T_CUKtEbM9WFZiPMCFb_uEQthEX329aws71Mrlwrci2AinJROtPNlhvPSPeiLrSu3rXinIEovyhU97k6fsIreghicu3BLRwj2WyoEh4-_7k3ukLh27ERO9dITZLIN_FG19fHHlUF5abOPrBVnZWMJP3UN9eXdXEPWvy6sBFVdYdqxq6Nmdw1RSEYOyyEM3Athoe0gCo_faA4S2Ue0JixXTuIItqQmKrSrQdONJe6IHft1HngH1K8QX4Ge3t7A_kNsQGyZRQSjgkUyVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49852d72a.mp4?token=EN8mY1K_g4kA-0r1hJmvrdZtT9VCFk-dmjC1x8NjYrgbH2IMKQkIEN649roDtOupc_8Gxt6T_CUKtEbM9WFZiPMCFb_uEQthEX329aws71Mrlwrci2AinJROtPNlhvPSPeiLrSu3rXinIEovyhU97k6fsIreghicu3BLRwj2WyoEh4-_7k3ukLh27ERO9dITZLIN_FG19fHHlUF5abOPrBVnZWMJP3UN9eXdXEPWvy6sBFVdYdqxq6Nmdw1RSEYOyyEM3Athoe0gCo_faA4S2Ue0JixXTuIItqQmKrSrQdONJe6IHft1HngH1K8QX4Ge3t7A_kNsQGyZRQSjgkUyVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
گریه‌های آرش‌افشین بازیکن سابق استقلال: نتونستم پول خوبی از فوتبال در بیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107377" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107376">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=P_SwknzcaxoGAz0tliHy12cau9jv1O0en6bdH5PDTw4dISk0ouJqSIZXXNwWUgzZZ7frxzQrGqXD0a__kjM6zzx9TNXZLwUBrXj2_sqzA19t1Y6rrHK9pxlngnAxaMVqZBk5GU7wncvKoWHvc1BEDWRT2NKvHS2MfVFpUb6IedDuDFZi8ZzgaXRXxuG0A20eBkLZaTT0KHzkCnOK-NgMkhjiHmTCosdTcqOqrYPyFnoQxZyiObUXYzwH9sLvUBrofwNYd-OMwcLiUbgcB20V6CTRh6ozLe9FZJeSB_hZpKd-2Ds_XMBEBtdhDHdKxS2mEp7mHzSxJl5xRlLem3qupA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d81597ceff.mp4?token=P_SwknzcaxoGAz0tliHy12cau9jv1O0en6bdH5PDTw4dISk0ouJqSIZXXNwWUgzZZ7frxzQrGqXD0a__kjM6zzx9TNXZLwUBrXj2_sqzA19t1Y6rrHK9pxlngnAxaMVqZBk5GU7wncvKoWHvc1BEDWRT2NKvHS2MfVFpUb6IedDuDFZi8ZzgaXRXxuG0A20eBkLZaTT0KHzkCnOK-NgMkhjiHmTCosdTcqOqrYPyFnoQxZyiObUXYzwH9sLvUBrofwNYd-OMwcLiUbgcB20V6CTRh6ozLe9FZJeSB_hZpKd-2Ds_XMBEBtdhDHdKxS2mEp7mHzSxJl5xRlLem3qupA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚪️
⚽️
افشاگری حجت‌کریمی عضو هیئت رئیسه فدراسیون: قلعه‌نویی قرارداد ۴ ساله می‌خواست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107376" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107375">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=k762ipX5iUAETAmAHeh-zQB-RCl8ZngCE7daZCMapBLU6eT_32QKolJLgvlIUABjSaZ5F0heMt6-5LnHLGzKQv5ekttT6cvWb1NId951xcHNeII95KzpfsjV7Z1LBih_fJF0_tPSNf5cxt0Km3vFrEynJyHX-JwS4WTccie1AZ0HJ4qGPDqA_gB0B_bBZ9QlvsdsMgb7brcb--71n1qYei_RtPHdxENbyXMRI_8Mmd1JtxyPlYrM2wAUsEdwjLi9faOl7sebD0j2Gty7TAAc--8LRi1JDagQcWpS1_MHCZ2UFI57fNHdv0-jhcr1cGErICnVwSuj6veAfMuOVeNStg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30882bf1b3.mp4?token=k762ipX5iUAETAmAHeh-zQB-RCl8ZngCE7daZCMapBLU6eT_32QKolJLgvlIUABjSaZ5F0heMt6-5LnHLGzKQv5ekttT6cvWb1NId951xcHNeII95KzpfsjV7Z1LBih_fJF0_tPSNf5cxt0Km3vFrEynJyHX-JwS4WTccie1AZ0HJ4qGPDqA_gB0B_bBZ9QlvsdsMgb7brcb--71n1qYei_RtPHdxENbyXMRI_8Mmd1JtxyPlYrM2wAUsEdwjLi9faOl7sebD0j2Gty7TAAc--8LRi1JDagQcWpS1_MHCZ2UFI57fNHdv0-jhcr1cGErICnVwSuj6veAfMuOVeNStg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نبرد دو هیولا از دو نسل! امشب در اسلوی نروژ.
🔥
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107375" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107374">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119aac7582.mp4?token=M6ZGrSzvOlIcxN4nUDyYFM0YcsryLV7-3Ac93ECVggz-ZMKvj_8HRkw8W7E5KU0I5ecmg-zpwyJxzhqIYexrXJK8gn2yo0h0df3Ji-LssVyOvbzm-LMbkZGpwkFTB29FSv3TsixCoslbgGdJwmc-yj4kPlMsgcyGQRcsSDPsFnH5XC6bGKc6KO5FEbw1E7v5sMoSrO_DP9-CAJAvnACbDRFKeWwqL2KK-rZ77WomndkaIYQ2FG8I9t4UanpEuoSeCVMg6oH5qfdp1VR8xscXsqirKBfv0CP-VN0JIUoa4fgqhELLScJsxZxihRAJztLbPiq5Q4OPvAp1_8GO0Qa4xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119aac7582.mp4?token=M6ZGrSzvOlIcxN4nUDyYFM0YcsryLV7-3Ac93ECVggz-ZMKvj_8HRkw8W7E5KU0I5ecmg-zpwyJxzhqIYexrXJK8gn2yo0h0df3Ji-LssVyOvbzm-LMbkZGpwkFTB29FSv3TsixCoslbgGdJwmc-yj4kPlMsgcyGQRcsSDPsFnH5XC6bGKc6KO5FEbw1E7v5sMoSrO_DP9-CAJAvnACbDRFKeWwqL2KK-rZ77WomndkaIYQ2FG8I9t4UanpEuoSeCVMg6oH5qfdp1VR8xscXsqirKBfv0CP-VN0JIUoa4fgqhELLScJsxZxihRAJztLbPiq5Q4OPvAp1_8GO0Qa4xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دو بازی، دو گزارش، یک تفاوت عجیب!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107374" target="_blank">📅 16:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107373">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM6PyoJ2mv1SHLrDgAR8C_vDhVJ68oeAWeuToFDIWWPe7Mutk2SQE1-sVlVZx83tm8mTOsI3zyW0gGlcdThJ8u5LS9KZtBN29Okp0SxalW2J7kTP5WZoxhp24Sz7Xu2e_wm4ARJGneJAhgwrX-TB5HwfCuvOjnxTWv37354CmrJ7HEPlFON5r7eLsvpGCyO-I65wGA_FYRbGiHc7EReAVyf9JxwkA-82dQjGMoWkGxk4Wzg455vrJSmXoBeVuJkvEoUinK9ruGKk9UFzJVoXP8PIwl_v81p5DsFJTLkD_kuUbfqwMi2hIr7TjVqvcZ2ZV6kBBkLMCcEtMu7GgqItIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گاتزتا | روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتا قرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی هم یه قرارداد با الجزیره امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو!
هردوی این باشگاه ها متعلق به شیخ منصوره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107373" target="_blank">📅 15:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107372">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=b1jSAwk6-rTlVZmsEl9XcQ0ZvF1zBsc36OC34PreewmfQzqwqChT8PUQuG8gKhNUhjiuqwXQ54K1BHX8buBwKahAMNa_nQVznfO0jAr2ibLvjKJTCbI3blhuqQsINzfJPOlheXn9_TVurzV-gBQXWmBAkqq3EBGJyRfdAeSRHaJHdmLZnbzeiz4eORVrMmUWkPC1NMIaGnxtpHblMedZW1wjsUKBEOTJobhcNaaTDbo56i3EYmkBxYTEaZmm5C2gqJSuAb4XyFaaysxHCqj_dBF14EV5dn8Qa5_XOts0Rtb9OJ_CbgQfbrBMB34ibaaLjiYle6I4KXTzJ2higXfk4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a4c9c45d7.mp4?token=b1jSAwk6-rTlVZmsEl9XcQ0ZvF1zBsc36OC34PreewmfQzqwqChT8PUQuG8gKhNUhjiuqwXQ54K1BHX8buBwKahAMNa_nQVznfO0jAr2ibLvjKJTCbI3blhuqQsINzfJPOlheXn9_TVurzV-gBQXWmBAkqq3EBGJyRfdAeSRHaJHdmLZnbzeiz4eORVrMmUWkPC1NMIaGnxtpHblMedZW1wjsUKBEOTJobhcNaaTDbo56i3EYmkBxYTEaZmm5C2gqJSuAb4XyFaaysxHCqj_dBF14EV5dn8Qa5_XOts0Rtb9OJ_CbgQfbrBMB34ibaaLjiYle6I4KXTzJ2higXfk4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🏆
یامال: این توپ طلای ما رو بدید بریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107372" target="_blank">📅 15:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107371">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=h_mHWRIoydC3sPX83Ibexth-3EIL3mXQrm6KHU4limDe7F9gtGY9hhf5e86h-QvhmaWkkH5bWIzbJWu9mI_RAZSdoKL4Ki5Wjs2_6h7g4Ocn1zNydW33Agh9CuPavAcfN2d4zA0OOyveDH-F8Cj0lq6i21Ug8xXNkFViCjQg-w5HSIqb0ioNpPjMy_LWo_LaW6KSt6byuLXcKXFvIJ6yK5FfboPS-E5wovzdrYbDHg7SAShTAs6NhzKJ1kWHKgdLyTy68lrBlt1Bfkf_oiWvP7943fXy7fWQOL15JTFNcuE0BIWzUNAPGsCoXMGjcl-YdjexOLag11NEygvI9lM33Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8c98790b5.mp4?token=h_mHWRIoydC3sPX83Ibexth-3EIL3mXQrm6KHU4limDe7F9gtGY9hhf5e86h-QvhmaWkkH5bWIzbJWu9mI_RAZSdoKL4Ki5Wjs2_6h7g4Ocn1zNydW33Agh9CuPavAcfN2d4zA0OOyveDH-F8Cj0lq6i21Ug8xXNkFViCjQg-w5HSIqb0ioNpPjMy_LWo_LaW6KSt6byuLXcKXFvIJ6yK5FfboPS-E5wovzdrYbDHg7SAShTAs6NhzKJ1kWHKgdLyTy68lrBlt1Bfkf_oiWvP7943fXy7fWQOL15JTFNcuE0BIWzUNAPGsCoXMGjcl-YdjexOLag11NEygvI9lM33Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پنالتی که هری‌کین در تقابل مستقیم با یامال از دست داد تا سرنوشت بازی دیشب تغییر کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107371" target="_blank">📅 14:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107370">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb8643-yIqhfBp4XVH7VBg6a3sTf9vRIN2yC7YGLBWUDij7r4LlfjZKhC6KZabbaFOQKJMw7lvgxnujhvRy0iatABhKeFbBpcFt42_xSf4xfg9YfgWdHn951LACP-06rOhffBJ3YvK_2MsknlfFMFGXHuT9cVfE9iOTSaexdM7KqIMifkQ5lhiJdBZ-jG7zRWXHif7S23Z4yhVvzCQHfBj6WnloR73LgKNd4bA6nB0nX6Cc57fh1xqM3LKekEyXa3O_bDp8qjotMJqnTOy1otoev1x-5jEm5VLgSDPb5N6LHY3zlwa41vmuE-VqREvmsbSuHno9ip2kdAIaB2_Zyug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پریشب نبرد منتخب آفریقا و منتخب ترکیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107370" target="_blank">📅 14:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107369">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VV5fbwxYe7tf0MX0ARYpEAsrxixBC8nlTQ5jFWvGEu_8g6PF5l_F1ndwLhi6pq089FEuXuhdIB1czylaMz0mDOCwcpY9bY_8kzbU515ASj0ykds_9Hupg7xzExDAqlnkLyWJajSA6xXlcSNbITp4Bya4R-AYMFApC5rtETmEg-_JydFG_la684rMeVCQFv9bELO6dthY3B5rmMAUDIvBcXFsezTqP7ybleNXzYj0gGNh-Vx0JwTPpVFo_bQkO-4tU16WK1jIlqEKh0_9v3QGOk7tNdM05cMFX8Y-97Kl_UgxZjLoObxFHK-FffqQMgfeMHB5WSa3KJ10NXaQooIowA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇪🇸
برخی رسانه‌های اسپانیایی گفتن که اگه سیتی محکوم بشه،‌ ممکنه هالند درخواست جدایی بده و با توجه به نیاز بارسا به مهاجم نوک، این بازیکن گزینه اول کاتالان‌ها میشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107369" target="_blank">📅 14:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107368">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t96aphotdODBeZi4G1AawWYpO82yMGMdr0tnrMHsKgt-aTGeppaCV1kJ0cVzA7PzikFw2Ue7TF9N1AS-UusGYxWAnzOL50NMhHcuXwiKzq9HD0py-H03AUI0tDtFP4LMW5hwapD_w7QJccTLqNeEjzyBoqhCK7PRbVVGdLkmFdBbeffQd_2VtFFmA5krRpiuH-9nAfRHbBf77xZ9SW-rhQ1sRCrBsedPqAVoU37hiUIvcmCeOls18be7gsNTsTAqsbbgEio5UGobwhRTCKZkh6MzuDLlEL9odD4UnnwMNARZh3aPRzDbd8J6__H805ZXhKcSfMtEHNjtMMd-HdQxgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇧🇷
نتایج ضعیف برزیل آنجلوتی در مقایسه با سرمربی اسبق سلسائو در بازی‌های دوستانه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107368" target="_blank">📅 13:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107367">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEV_tQ3CBnn2R-0bIK_fB0FYIfZ8abBGLiIHtOmDLlIpRU18KjMJRWltNhkKdpKNelEXXH0D38sgd7ZnNcIDR8FQJl22IfxFOSodhxFT-K64QcuQ4HoIsoZtFBIQ4eCTe4Wvu_zqp-h8z7dpUQngDAQ9Seq8Pys68j0a-0Ey3EX64xlQGOlJlEFCh3rI7oq08HCiyIGTiSqVYKTVwrZto_maFRCVG3PAh3zAvTQK8pLYdSLyOX5kIuotiYL2IKXTOROaR67mqmur0_s9OLjMbgNCT0AcF1Ffdo1EuZ9Ql_9IBIyZ5VrA7agOQ97uDR53jy44nlzOUhKb1exHnkLoQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
‼️
اعتراض تند عضو هیئت مدیره پرسپولیس به شایعه قهرمانی فصل‌گذشته استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107367" target="_blank">📅 13:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107366">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=bx1xaaF_otYvodMMD6g63INiLc2_2y8gQCLgCDzOeZGRCefdaDllzK-OW3niMUXGzohey0cS0XywOATV2hVdK2tXM_0IkdqGh0u-guZug5ei7uK8Sny9kSNRlXb3Gj-Zx8GuftRMZNEvdKwqjJmBsM_X8C48k99Zp-kYwfPlMJpRrwZ-j4bGrzQ9Yqa2bqzU5sZw9BdJovj-5ICvNF7hV_K2JiuV6Ajdy-Wukt7LfH5vwPZAft3x4rHnPuMZaZX8R7zvwr-ro2caCwmCTY2j3pTOMhMjm-wnZb-JhkGaz5Dp2SVuU8gnqSyASt3ysMnZ2MrQUgMvlotUUXtQGOlTQUn6MPD6ljX3pEmGQ-1K4HYH_hQ40N0KcUguFbA8ZrTSxAoLjLBChyGUZw-1SIWiHVJM6--27rZJi_ZIsgz0flipe0CHQtk1GX-m8yt7wMlVwh_GygYEv-BzvWKxk82d9dcPUWKYdIFTRS5cL9-pLQ8Oczc4p43iq_poDNZ-xJehpOvcXjfWqHqg8UTn8vAWdaMqszCm9iK55-hbg3ZAjGGkyoP61ZqiPePdn-kwVdWEeOLypWKczhrxJdZfRWD83JiJTE_FHpYZHS88PcNeEqk7fjkgbu5VTOf2M8sNXRjeJqQ53yXg07JPSu4of9KauJBFl20FrY_r8DGzPSXkKog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39d99adabc.mp4?token=bx1xaaF_otYvodMMD6g63INiLc2_2y8gQCLgCDzOeZGRCefdaDllzK-OW3niMUXGzohey0cS0XywOATV2hVdK2tXM_0IkdqGh0u-guZug5ei7uK8Sny9kSNRlXb3Gj-Zx8GuftRMZNEvdKwqjJmBsM_X8C48k99Zp-kYwfPlMJpRrwZ-j4bGrzQ9Yqa2bqzU5sZw9BdJovj-5ICvNF7hV_K2JiuV6Ajdy-Wukt7LfH5vwPZAft3x4rHnPuMZaZX8R7zvwr-ro2caCwmCTY2j3pTOMhMjm-wnZb-JhkGaz5Dp2SVuU8gnqSyASt3ysMnZ2MrQUgMvlotUUXtQGOlTQUn6MPD6ljX3pEmGQ-1K4HYH_hQ40N0KcUguFbA8ZrTSxAoLjLBChyGUZw-1SIWiHVJM6--27rZJi_ZIsgz0flipe0CHQtk1GX-m8yt7wMlVwh_GygYEv-BzvWKxk82d9dcPUWKYdIFTRS5cL9-pLQ8Oczc4p43iq_poDNZ-xJehpOvcXjfWqHqg8UTn8vAWdaMqszCm9iK55-hbg3ZAjGGkyoP61ZqiPePdn-kwVdWEeOLypWKczhrxJdZfRWD83JiJTE_FHpYZHS88PcNeEqk7fjkgbu5VTOf2M8sNXRjeJqQ53yXg07JPSu4of9KauJBFl20FrY_r8DGzPSXkKog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
على تاجرنيا مدیرعامل استقلال: بیرانوند برای آمدن به استقلال پیام فرستاده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107366" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107365">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1582f31111.mp4?token=j6j4Gz4Q8I2qcYuIT5TEfxZqWoLEqJBj6UdgxLEDDowuRv8IqCSQCFRYG-MQzeOUi3nqnuWx8fUAGhBj1fgjeYYw-unk4z-LJEITJdGAAkseUJ6nYO5LSEnsBbX1VPA2GPY1bloJ9fIxolbp-eOYKVkfndnZ9wSUk9umGHhLydgJx6V_3jmzBBnZnquQADdD-tJpf_HI0dLdCh5k4T3aRLyoVfZQUiJqPBFpQieRCOvhFO-dZL1sTyTaqGq4DzNUGLtX3bnh_7X7scmCByLAxRtUsEfKWjy4QfupB72VOYIEr9Ol0e4SnceNgQ4EPS9U8nwjSQ-HiqiWeogkNjTmHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1582f31111.mp4?token=j6j4Gz4Q8I2qcYuIT5TEfxZqWoLEqJBj6UdgxLEDDowuRv8IqCSQCFRYG-MQzeOUi3nqnuWx8fUAGhBj1fgjeYYw-unk4z-LJEITJdGAAkseUJ6nYO5LSEnsBbX1VPA2GPY1bloJ9fIxolbp-eOYKVkfndnZ9wSUk9umGHhLydgJx6V_3jmzBBnZnquQADdD-tJpf_HI0dLdCh5k4T3aRLyoVfZQUiJqPBFpQieRCOvhFO-dZL1sTyTaqGq4DzNUGLtX3bnh_7X7scmCByLAxRtUsEfKWjy4QfupB72VOYIEr9Ol0e4SnceNgQ4EPS9U8nwjSQ-HiqiWeogkNjTmHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری‌که بازیکنان آلمان از یورگن‌کلوپ حساب میبرن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107365" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107364">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=lI8CEPYgmy82pC0nCZPr2S2rbVUZCEvXmeEJPngXOG8yYdpP-ab0nf1kqTgE-XxF3hDrzN6A9wIS50YDj0oc3CUd7g72OF8VQcRkP6KVu26vPW7DiCUYRnn2aSbnzdTrQ3tqh51TSxHtDJUFm9AxtGOhv7mlgz7wpbxvQNG9Azs27Zh74g7VqynnmwRaEEkNhlXY8pkQX4Cldj12B-QjSfJjaKxMiJbmSLqSy84p6CVlM2mFtjK-G4tY7oq9oUTsCQ-axV2An3KhfrTXJMMROzDAvqkXeTPi_l9_stfFjoXkznNJmbx05wbALypME2I1SWd7OnyHGCZ2eLWLJ77T8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a8b1d7243.mp4?token=lI8CEPYgmy82pC0nCZPr2S2rbVUZCEvXmeEJPngXOG8yYdpP-ab0nf1kqTgE-XxF3hDrzN6A9wIS50YDj0oc3CUd7g72OF8VQcRkP6KVu26vPW7DiCUYRnn2aSbnzdTrQ3tqh51TSxHtDJUFm9AxtGOhv7mlgz7wpbxvQNG9Azs27Zh74g7VqynnmwRaEEkNhlXY8pkQX4Cldj12B-QjSfJjaKxMiJbmSLqSy84p6CVlM2mFtjK-G4tY7oq9oUTsCQ-axV2An3KhfrTXJMMROzDAvqkXeTPi_l9_stfFjoXkznNJmbx05wbALypME2I1SWd7OnyHGCZ2eLWLJ77T8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
❌
تاجرنیا: در پرونده توهین دسته‌جمعی هواداران پرسپولیس می‌خواستیم به دادگاه CAS شکایت کنیم که شخص آقای مهدی تاج به من زنگ زد و گفت از پرسپولیس شکایت نکن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107364" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107363">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107363" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107363" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107362">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqW52kDmRft19Wy9AqCDeDHZ7EJYQP_zT85BRBJZzrf0krIGiIVvTHLnBP-zL7cePuWjB4Wow88rjdDB_2NG6puP9Qwik3LE43spEjPwC9S1k1RmU02EosnXQD4HEhdKR4G8tal0f3BjdRxIzpe2Sn_qv3e4VCRsy8-2oODIUdt-mRLoVMyKo3XzXTJz_PtbwW24KyREQT9T2sR5COKhSKPy_qA6FjCaQxd5M8sVr7cpy1fSyOmPGAgj8Kj8kPIm6OydPS_x563MQNqhK9aI4dQyrBUuIju1H2_KSJit9aumPCryfbDJn9X3GtHPPGYi8TUzPYuS8k0ZXeUTyqpVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
پرتغال
🆚
نروژ
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۸ گل زده
نروژ: ۳ برد، ۲ شکست و ۹ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107362" target="_blank">📅 12:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107361">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMoPIe6NEIEou_klYpcr4M-GfgSFScwa3vs5StsTb0aHsRUQOQpu3tw4ix6LrHxNXO1tYWNLfqCv8dKPdykGkv8fC7dS5DgLVLQD1HFU-okrs-VYnoMFSY4a-B6uESdP9IurGrZEiMw_MFDIKtiose8yEaEt5Oz9NZMn3PFSAxX029-is4SJ2dDQCaRUHbCnGznyFK3Mw0MaSd2oDm8rNXVQ1ZD185j5PxGGqWrjylaGLdrAjnUMgisBkWQ1UvfWG_N5nIYZSAg8ThDZwZ00mjbg2mMyYnn8-4EpFfTGLkoySpNm-pt1EriosyxgKXeH8uYf5KLPmUtoYjLH0G57l2Bo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6292835767.mp4?token=PbboC04g31qrPokSefmMgz6qCt4COT57V_IBJkU7kCWVpZ6VN61oaLOY4nDBvjigeucM3fqE1-tVPBeKjgSxBhP92gyHW_DaN9DpO9XFOsCA9jcyEODQ64uvVvJ3koJwuNHjSj7S_6rFGEiQ6hJhYZYnn8GDYXtcnz8JMxXHZKs9StMMJVIvBkNeh2qy9nBar9PWNUta5Q_C8jSN4dXsSrT5Y2UfO28bBSUB2MW6IdrcGGvpMA2wD5oc9Zq4FJ3RrfpThp5SE1bQ0rlVyf2BDOK99q2lZ5mQfGb2zAM0r1rU8rQVhQDjGd1V551fUSbQmCoSA3_0nhGojADqtv6AMoPIe6NEIEou_klYpcr4M-GfgSFScwa3vs5StsTb0aHsRUQOQpu3tw4ix6LrHxNXO1tYWNLfqCv8dKPdykGkv8fC7dS5DgLVLQD1HFU-okrs-VYnoMFSY4a-B6uESdP9IurGrZEiMw_MFDIKtiose8yEaEt5Oz9NZMn3PFSAxX029-is4SJ2dDQCaRUHbCnGznyFK3Mw0MaSd2oDm8rNXVQ1ZD185j5PxGGqWrjylaGLdrAjnUMgisBkWQ1UvfWG_N5nIYZSAg8ThDZwZ00mjbg2mMyYnn8-4EpFfTGLkoySpNm-pt1EriosyxgKXeH8uYf5KLPmUtoYjLH0G57l2Bo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
سوپرگل‌های زده شده با ضربه‌سر رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107361" target="_blank">📅 11:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107360">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pl4MWtgbhiVv9SET0rQpTydzzZLynBhXJoTujrjWYglb98YK8SsU4E57ybau1wm7qK9RoEwMYt1KGtNODmB3qpEaQKTZdMNvpexe4a-9rrxxWMAtpc1jrbKgBaWuQm4QVigy6Ri9YQmlqAu-c4Qd867oWHtauFKhVpO5XXzsHsWIK6T2pJayeicyxkJkrYF5L-QzXH3sKnCSe0CikXpeSTMbGCs4X8gPMhnzRD1B160beL-9mCPjQmtCLfPX6Rg6n3_GlBqF2rz6yOs8NjCzTqDbclu49T2Iqed4ytOYeHIN_Hcu0lwsdyLPvnOyIDrKAdL57VZANEJmpAutmmeJog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107360" target="_blank">📅 11:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107359">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dCVgfw-MjT68V5yCOulgVxD3E1NX4JXH4KZtHqJ0TjBF2jxpw4zQsgIaPWg1r3lY1G6F7gwuwnMIm7u6NFZEkgSdK6IKA9v-KTZTQyS5y8pU10EhFHgidJf5kuy6jjovfOXktDv7nGKcdYWkhDN7I3UHTGs_EwRhg8zXwerBNc_vU2AWYvfEkxo80HPG2J5dRP5bYReiL2d5qOCOjp7tjiRnybu_5Ow9y2aWXp2Bn2_uV5kzOrzNzvEYlnYx7yczyDEW4e_AnXzC5Mie3Etaxg89nqMw903pTzNo853xXKqIJtRdl8Yp9p6GRdwF2HKAL9L5ERn87BIHzo3PH7YVig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
لیست محبوبان و مغضوبان امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107359" target="_blank">📅 11:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107358">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/184858d60e.mp4?token=NmJD8Y8ZzoCnlOsNN21N-qYJgbVNAwfJ0InsNVUFp6ycrwBG0_hHZjExOTT0Z6xDsMp1lANyXTb5PoFqUbkv-Z0wi9vEgy9NgeBYjyrvqIfiYZfj78j_jNaP0e-S6uxkhKujYlu8m9swcak9HTD52jzDanmGHkzhXopNtKscv0-d3Ucu8Sy-Wo0ZSIw3dFfUPTcDHqR5OKv71AdsjMG0IffbFZddnWb-P8i0Uk_spcIVoPasQXoiX-DgMf7fi2VYHLTdiB50bjgBjGzoqIbtwNQ_oYXfQ5pN6ORiJluXBW2HKEvNkU30cgLDZoK9Oa8qTRnwdS104y9i5FMNMYj16oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/184858d60e.mp4?token=NmJD8Y8ZzoCnlOsNN21N-qYJgbVNAwfJ0InsNVUFp6ycrwBG0_hHZjExOTT0Z6xDsMp1lANyXTb5PoFqUbkv-Z0wi9vEgy9NgeBYjyrvqIfiYZfj78j_jNaP0e-S6uxkhKujYlu8m9swcak9HTD52jzDanmGHkzhXopNtKscv0-d3Ucu8Sy-Wo0ZSIw3dFfUPTcDHqR5OKv71AdsjMG0IffbFZddnWb-P8i0Uk_spcIVoPasQXoiX-DgMf7fi2VYHLTdiB50bjgBjGzoqIbtwNQ_oYXfQ5pN6ORiJluXBW2HKEvNkU30cgLDZoK9Oa8qTRnwdS104y9i5FMNMYj16oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
به‌مناسبت عملکرد قلعه‌نویی یادی کنیم از این افشاگری تاریخی محمد مایلی‌کهن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107358" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107357">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=ewrL2-NlZfm2yuKkm7_4LQQ5MlBgOceP1VSeQJ7ZbNYBvass5_GfBbkCwc2nP1V_BWkdbZAGaWz6VaPEZWnuKFYM6sfp9Yb7jFX_qqeyteQw5dYhZfjQIs3sLnBb9FwMTnqabITj5zzKdw-ohPRchgAuCk2o5SBLclwfVCL5xC5s1BIoAcho9lgjbu0pFMLa1HIMi-Uwgmlav0swR0JDFbN3arCishRBBf3KaSoQ_9QjE6X1xishxu6x6QeojLOvtHz_r7ZlCCHjt2GC-TR7gQP51CONxgOTflQSA5mnbkKH5l2Z8tT_vJpN0mCstFpJPyo82i8X8Bc_aBNr9t00vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f1db9d0d.mp4?token=ewrL2-NlZfm2yuKkm7_4LQQ5MlBgOceP1VSeQJ7ZbNYBvass5_GfBbkCwc2nP1V_BWkdbZAGaWz6VaPEZWnuKFYM6sfp9Yb7jFX_qqeyteQw5dYhZfjQIs3sLnBb9FwMTnqabITj5zzKdw-ohPRchgAuCk2o5SBLclwfVCL5xC5s1BIoAcho9lgjbu0pFMLa1HIMi-Uwgmlav0swR0JDFbN3arCishRBBf3KaSoQ_9QjE6X1xishxu6x6QeojLOvtHz_r7ZlCCHjt2GC-TR7gQP51CONxgOTflQSA5mnbkKH5l2Z8tT_vJpN0mCstFpJPyo82i8X8Bc_aBNr9t00vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❗️
سوپرگل‌های بازیکنان ایرانی در تاریخ به چلسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107357" target="_blank">📅 10:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107356">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=JBSZNCWLYsfkaQiPJJKUKXqXIRZ5Ooo9ZMdBA9_IG0UVlcS4O8pHvyoT5ulM8vKJgjXNs0TnhDvAjUucNclaf3KsscP33f00uTEgmmIo9rYJtqGj0Xjz8fFSdvdXfIDaB7MMMu5ywQs1gzGx0N8idyGKJR-ocVZQL4lw0c-LZlx78YrEx0LUb4CCSGVUTX7b5LtrGncCclqEOtUt46QSHvkB_pO00v1umHpUt-FX0qpwNbwD_4h8abWlSqE-zhT2wSHNUeVcyzb1YtjPeA_7YLNkHYll2C6P4PsMqbCGAzFhbxVMwXHDtk-jUhVCZCM770pnWYa3XsRz2CtRK5StXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805925ad6b.mp4?token=JBSZNCWLYsfkaQiPJJKUKXqXIRZ5Ooo9ZMdBA9_IG0UVlcS4O8pHvyoT5ulM8vKJgjXNs0TnhDvAjUucNclaf3KsscP33f00uTEgmmIo9rYJtqGj0Xjz8fFSdvdXfIDaB7MMMu5ywQs1gzGx0N8idyGKJR-ocVZQL4lw0c-LZlx78YrEx0LUb4CCSGVUTX7b5LtrGncCclqEOtUt46QSHvkB_pO00v1umHpUt-FX0qpwNbwD_4h8abWlSqE-zhT2wSHNUeVcyzb1YtjPeA_7YLNkHYll2C6P4PsMqbCGAzFhbxVMwXHDtk-jUhVCZCM770pnWYa3XsRz2CtRK5StXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
سکانس‌جالب و وایرال شده از مرد سه‌هزارچهره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107356" target="_blank">📅 10:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107355">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‼️
⚔️
برخی از لحظات خشونت دیگو کاستا ستاره سابق چلسی و اتلتیکومادرید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107355" target="_blank">📅 09:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107354">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAxuE0J8hflKNjxrwFoxEHKtIgHjM6Pem8IoNtY1jGkCOVk8QYMH_LHGx45_9RNL9Djsf6l8ymcRocEect_G7Rk2HfrZh50qVZkxtKUz6snjRsegSFUBZRDXORb-1-SNmoFlJcGlh6UiSZf7JCFmNne8QlwEcF_IwXHkzpBj-F8VmQxfUPqw43RV2YISNDjCx84Q65TYoKF_fHjvcJHdyxSxZIpIWhpAYaEVZRrdAJzCOubMJ7Onm2xT1z5Y1u5WUZ2DVLcIk20cfmGLtmh4yiu64SGb4ow9CKnWBfxp40Qn5Sl_IOzsBzHlRs1WAndHe5e0iysjzS2OG981GLSbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
ضعیف‌ترین عملکرد‌های تاریخ رونالدو در‌ پرتغال که بازی مقابل ولز در جایگاه دوم قرار گرفت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107354" target="_blank">📅 09:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107353">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=s18-4Ptr5fwfjPst0pgUPIkGhrfFxFAZlvBqDv8OEWeCIotl7hEMSbhsEHfa0rjNg5b6S2LtIH2aDCjbo4mw6u76LE8SDYGD5O4kLYPDDAUs2T-ipSEyHtI_hMPc9OgzuQ00QCmU8yObet_b5aTl3QeU3BBFxrbh2bGkDhvlRaWBORRbcsXpQt-VJdnaUIAnL2a5VjC7cciFCbmBHngjhpR9d053E3-ge8iP9XemrR6fswCIs5rqIWBsXkA0o8XdcFKejDclOt5KlJ9rd9KDRGxFKpC1tnwjwQwHgSDqMo5qxv8mEI6IynLp-HWl8g6aQWV-WuypkvYscyWzh1KOBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bc355e5eb.mp4?token=s18-4Ptr5fwfjPst0pgUPIkGhrfFxFAZlvBqDv8OEWeCIotl7hEMSbhsEHfa0rjNg5b6S2LtIH2aDCjbo4mw6u76LE8SDYGD5O4kLYPDDAUs2T-ipSEyHtI_hMPc9OgzuQ00QCmU8yObet_b5aTl3QeU3BBFxrbh2bGkDhvlRaWBORRbcsXpQt-VJdnaUIAnL2a5VjC7cciFCbmBHngjhpR9d053E3-ge8iP9XemrR6fswCIs5rqIWBsXkA0o8XdcFKejDclOt5KlJ9rd9KDRGxFKpC1tnwjwQwHgSDqMo5qxv8mEI6IynLp-HWl8g6aQWV-WuypkvYscyWzh1KOBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
آیت نوری مدافع سیتیزن‌ها تو بازی الجزایر مقابل زامبیا از دستور کادر فنی برای گرم کردن خودداری کرده و به همین خاطر از اردوی تیم ملی الجزایر اخراج شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107353" target="_blank">📅 09:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107352">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=AReElOlcICsYaCmRZgAVqpLyha0FSgNJVgUDoh8ZZyNY_FOOG_D5TzhV2SgQjAlh2Jn4N0eGSydGjqhGZDa3s4VGp7gPrLAljkBB7YZ0ccA88XwWtOq9jbCncwWXGhRXgxuJbyK2F1uiNrifvqjKJvdf3h1Sq39c0t-svIfUpMciHqfWG3KUFHl2dD-ZgTZQ7N4-Te31moHHgUdL23-aZmHS8Iu0CtP4J2d5x5mrAemvtMvLBhMRnWFAP2Mby6zHSbfOhAEaIZaDmVEKqchXfQTS4RejoHbA8wN7Av8--VDTdLDiLVIzPTek5u2VSSYqsdGdpH7qdyScEJo0eK9PHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e5fa478dc.mp4?token=AReElOlcICsYaCmRZgAVqpLyha0FSgNJVgUDoh8ZZyNY_FOOG_D5TzhV2SgQjAlh2Jn4N0eGSydGjqhGZDa3s4VGp7gPrLAljkBB7YZ0ccA88XwWtOq9jbCncwWXGhRXgxuJbyK2F1uiNrifvqjKJvdf3h1Sq39c0t-svIfUpMciHqfWG3KUFHl2dD-ZgTZQ7N4-Te31moHHgUdL23-aZmHS8Iu0CtP4J2d5x5mrAemvtMvLBhMRnWFAP2Mby6zHSbfOhAEaIZaDmVEKqchXfQTS4RejoHbA8wN7Av8--VDTdLDiLVIzPTek5u2VSSYqsdGdpH7qdyScEJo0eK9PHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
حجت کریمی: قطعا انتخاب سردار آزمون در ایران، تراکتور است. به هیچ عنوان دنبال جذب اوستون اورونوف نیستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107352" target="_blank">📅 08:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107349">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yn5yYQGBcq-OU7b1_i1sizJYdTFd1c71kYmWXshzmMsNGplIQ5hF-xhIbyZUYvtIQLzrOi0OPj90Jm93nnOK_22MPqXHjR1b6kNsDNMvynBLF4HwyYnDT_IaH5R7BOofueEfpNGbZeyQvDe9SlzFq_z0Clx1LwtZBTXpRYo_DwqvuZidxagYxcD3FFtcIO4KbzW05xbmlcrZkwiayPI3Pc1YpuJ6uPtXJ8XkwRkMSqrSThIV08S7Xa8rRoIxS8LuKdSBGpTgz5L3Fl3NNYYnyoOBABf4X3A2X-ZoGpeTT3XHOn6GE8VnrhkrpqFKYSRDwVWtyhlYkilvwhXP73Id2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گوگل رسما ایرانیا رو تحریم کرد و از این به بعد مردم ایران دیگه نمیتونن حساب جدید جیمیل بسازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107349" target="_blank">📅 00:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107348">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4ckYsbw2WyWoW-nHHiOKQ8ZARRjeLD55CEdaMyA8gpGTsx3wkZ8fgIwBKKtMQM20ZLJnFX9zJNynaCzIGKlg4lao5aii_hkdyF4rJxv5GGd-e8la6xEA_YmmRuvDGjN79D7rlNFfYfgL78sDqmTnVrTnoKwXPstt_YJ7fhLcqRWfYoCl8hLS09_1IqzFS9xy3gIeSTIkxnn3H_tTU5Xas04iTnI0MdFssuRiTPMCAOk6acwLDpvfyZ7fpl6pNJluDX5hwXrBEsgAmvNoK9F6NFGzRs8stUOc52Kf929peZEZ_XpbGrgAeSr0MJZrXA3HwTQZf4hkXQaI5BkxXl5bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
🇪🇸
فابیان رویز تا به امروز هیچ بازی‌ای را با پیراهن تیم ملی اسپانیا نباخته است:
‏
🔻
51 بازی؛ 36 برد‏؛ 15 تساوی؛ 0 باخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107348" target="_blank">📅 00:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107347">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107347" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107346">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhFcU3OwIfukihP1gYXGzCcwhZjKMVqZzxYj04t54gPNG-ifsUoGa69oWd0uYJaXemoIOf7r09vi9AuM7jh50lR6AGimE3osCpqN2GkWRfjIEL0mrVo_ab2nuP9LTFNp0RHmqL4kLcn1in-HaUrjGHQ9w7l8r7vsFrI_BAGRQwvfkp9P10nJZ_NV04TGQ-p2JM-ylnBPOrI9oHsWxrFHWbxmQXfi9DQOqvJ3UFi39DgffgvkQ2UO3bUL_OCfsYp0m1TabruiITnNaGt_kuurK9ajhoajk2yUR5FgMtytpXUSINpEK8PVBjP8Ado6yJAEDmdOy3dfjmROxyn9Jb-qFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
📊
طولانی‌ترین روند عدم شکست در تاریخ تیم‌های ملی:
‏42 مسابقه —
🇲🇦
مراکش [2023 و 2026]
‏39 مسابقه —
🇪🇸
اسپانیا [2024 و ادامه دارد]
😳
🔥
‏37 مسابقه —
🇮🇹
ایتالیا [2018 و 2021]
‏36 مسابقه —
🇦🇷
آرژانتین [2019 و 2022]
‏35 مسابقه —
🇩🇿
الجزایر [2018 و 2021]
‏35 مسابقه —
🇪🇸
اسپانیا [2007 و 2009].
‏35 مسابقه —
🇧🇷
برزیل [1993 و 1996].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107346" target="_blank">📅 00:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107345">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dwDC_bDjb2imwyJPuo9sL3SAyhvoCSSyusbeLyLO-o_loYZYdpBJs2E6Wgm_5egK6ykCyNu7ToedVStWJsyB08nXFB5hT9YiyPIjKto9V9j1CbRcssNCoVtvFT1Df3kfB57uwT8lZKa8oY3mA8TF_V-BhslQktU0PyUTkAwgKXjUhauhWFcIbEru8EP47W6tr5tv7bPNp1FNmj_C-augfBj_karpdjhd_cmr6pY_zCPGuI3Jg4hfP3iGfFxJazq4IklRz940a60XHDIr7MhYHSLAphVXBDVwZs_Cssu_9AdchrypAGVQyaBXx6T9ErZ5AOZCRieASjhkLmhpBWTCwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
🇭🇷
کرواسی در شب درخشش لوکا مودریچ ۴۱ ساله مقابل جمهوری چک به برتری رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107345" target="_blank">📅 00:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107344">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QydXyGVzykIZT2UBrYT78cuCqUvwDtfUkJ8P81Rre7EIh2RlWpszV8sggaKcXe_4XNdRmZ9ioNjh5ZCzeYZTgQSX15p1JOq7JJWThDybZDN4rKW82r36SHhfOY2zbAH0wCDGSsFKNyaVOsSVGPz8BW20dOLuqTYqWiyQVnIwUDLt98jgepigEJaKM5XGlfA3MGYRCmxjei4XaAwWIUzDmONPqd0VLzsgYqHHAhqBB04ZchuGVYvQL0m6LyhGoNzhEdw74aN1FLAokwn69T-XfowEG1ej8BNgcBcvtRW3doz_2fpcwm_SKbX7goRZVcfVTA7nz2FTGEvySG_5lxqmhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇺
لیگ‌ملت‌های اروپا؛ قهرمان جهان در لندن انگلیس را از پا در آورد؛ یامال بازهم ارزش خودش را در زمین نشان داد!
🇪🇸
اسپانیا
3️⃣
-
2️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107344" target="_blank">📅 00:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107343">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=F-5OufYh3seaMXU6QsuXqbDV2oCyHhk_0OzPpvboK4F0lfqwfk9kt-b_QPnV97QrabR9KDwzmgcymEmJh2egEmVK9L0EfUxklXfIrGOcpoG8KEaJdhizDJizQgSHI6KB_LDLRhALgkWaIvmti9ZBhKLF5IJGpYpzu9rWSVXxtMOvp_C-ivn757hnDFEM4Na9cU4G0XlQbmuF4slzxuhJT0G116V81lPOsdlpxb76nIoJHM9AK-QbmVSbgJNWbuLmaRLox8bqiaz9beAHUzf0MJyPz1Lw6YUBj1wDhGo7hFIf13Y_dFMXQBqORekQRPwgGp-ZmfZo930suzK3jyRvJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/494ff796bb.mp4?token=F-5OufYh3seaMXU6QsuXqbDV2oCyHhk_0OzPpvboK4F0lfqwfk9kt-b_QPnV97QrabR9KDwzmgcymEmJh2egEmVK9L0EfUxklXfIrGOcpoG8KEaJdhizDJizQgSHI6KB_LDLRhALgkWaIvmti9ZBhKLF5IJGpYpzu9rWSVXxtMOvp_C-ivn757hnDFEM4Na9cU4G0XlQbmuF4slzxuhJT0G116V81lPOsdlpxb76nIoJHM9AK-QbmVSbgJNWbuLmaRLox8bqiaz9beAHUzf0MJyPz1Lw6YUBj1wDhGo7hFIf13Y_dFMXQBqORekQRPwgGp-ZmfZo930suzK3jyRvJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌سوم اسپانیا به انگلیس توسط اویارزابال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107343" target="_blank">📅 23:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107342">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">اویارزابالللللل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107342" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107341">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گلگلگلگلگلگ سوم اسپانیا</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107341" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107340">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=DhyFmvRYipv16bY1ciNQW62sK1skXW7L2LnEw3LYvtWhWUXnfw_0Rbvdb10HYh0aiclH2N7qYrUQ4MbwkzJ7Y9iGcRsEwEub8ahb24WvcI9TAaHXcEOFEzoq1cvqm-6ZIUrzCesjKMtxTi6iFXVmvogmMxiIvenZeDMuw5B8sEdkHiORhY88YOrD7zNY5xrnDJcDdbDijsljz3aemBv9sA4QFaECKUcpHGUHwMpiy0n5AQxojuTxh57YuCMlbPJoNFie9L4thvoh_nKkwNZpUtPXrDi1nQS-UuGJvWF9H8kIOgg5GMYGSyfzzRSKaQUqiLuGfLgyRaYG6tHBrbfxIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a0a10c6d7.mp4?token=DhyFmvRYipv16bY1ciNQW62sK1skXW7L2LnEw3LYvtWhWUXnfw_0Rbvdb10HYh0aiclH2N7qYrUQ4MbwkzJ7Y9iGcRsEwEub8ahb24WvcI9TAaHXcEOFEzoq1cvqm-6ZIUrzCesjKMtxTi6iFXVmvogmMxiIvenZeDMuw5B8sEdkHiORhY88YOrD7zNY5xrnDJcDdbDijsljz3aemBv9sA4QFaECKUcpHGUHwMpiy0n5AQxojuTxh57YuCMlbPJoNFie9L4thvoh_nKkwNZpUtPXrDi1nQS-UuGJvWF9H8kIOgg5GMYGSyfzzRSKaQUqiLuGfLgyRaYG6tHBrbfxIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌تساوی اسپانیا توسط الکس بائنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107340" target="_blank">📅 23:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107339">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=ImVsaf5VPJ2TebB9kAqrE2iTNzdiqWF2n-W1zMJJGHyJpR5Kd4zbUkDq_cUi7m7rp54NcVfzONqDu-x3PUFrHyhSKiWoIsx31UNCGV2UJ9pfZtsOigSEf0lv7DTV6EZetbN4-UqgS0QOcO6IHq3btZRisc3cFh6rjW6e-8PdeXDMdmelWV35fuZKOHSUfBlhwbIvpgyZGuo3hsUHTMVBYFyZQwOQht2vEK9dqtwZPSNLHicJc_ZDEjPrxxt27ALpvqVS7zgnIPuf2NwMjY2sMM7Natn4JCVDTcsh6bGBGCLfJW8dRuaT_dLiB6qdfFpAgRpACRuRxTt4kt-nUoXFhg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ed28ae0d69.mp4?token=ImVsaf5VPJ2TebB9kAqrE2iTNzdiqWF2n-W1zMJJGHyJpR5Kd4zbUkDq_cUi7m7rp54NcVfzONqDu-x3PUFrHyhSKiWoIsx31UNCGV2UJ9pfZtsOigSEf0lv7DTV6EZetbN4-UqgS0QOcO6IHq3btZRisc3cFh6rjW6e-8PdeXDMdmelWV35fuZKOHSUfBlhwbIvpgyZGuo3hsUHTMVBYFyZQwOQht2vEK9dqtwZPSNLHicJc_ZDEjPrxxt27ALpvqVS7zgnIPuf2NwMjY2sMM7Natn4JCVDTcsh6bGBGCLfJW8dRuaT_dLiB6qdfFpAgRpACRuRxTt4kt-nUoXFhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به اسپانیا با گل بخودی کوکوریا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107339" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107338">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=m4DDfrwY40V4mBIF9SAcj4ufp3Je6KEx-wbFYR3tDvoh-WX04bOU5On3xFHeS6f0Xef8yaDMxXuMx-bizsgwCDlmnC6UnHs1Nn81fUiNCMW7-tZbnh-kwd_4moU58VLO0FwY9x0ja-XGiP8XZD5d4-3yd_OKKxhetoXM0U83ZPvV_fhysxEXmnzPqiN3C8lAfEz_mnF-qxd3fykHPR50hlR8QA-QveLwZe0n3wXPPMSAWpuPD89-YKHidAeh9fr6ehY2jGN_QN6ZWu_hQ6rRgH5lR_9WmET4wD7tI7r38v0NMwouv_JhrT_D6jKQhtmEDk70mZKoiWYBJ3wrKs2Oog" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8bcae065f2.mp4?token=m4DDfrwY40V4mBIF9SAcj4ufp3Je6KEx-wbFYR3tDvoh-WX04bOU5On3xFHeS6f0Xef8yaDMxXuMx-bizsgwCDlmnC6UnHs1Nn81fUiNCMW7-tZbnh-kwd_4moU58VLO0FwY9x0ja-XGiP8XZD5d4-3yd_OKKxhetoXM0U83ZPvV_fhysxEXmnzPqiN3C8lAfEz_mnF-qxd3fykHPR50hlR8QA-QveLwZe0n3wXPPMSAWpuPD89-YKHidAeh9fr6ehY2jGN_QN6ZWu_hQ6rRgH5lR_9WmET4wD7tI7r38v0NMwouv_JhrT_D6jKQhtmEDk70mZKoiWYBJ3wrKs2Oog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول انگلیس به اسپانیا توسط گوردون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107338" target="_blank">📅 23:39 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107337">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🇮🇷
⭕️
علی تاجرنیا: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا می‌گویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107337" target="_blank">📅 22:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107336">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=lTJ9Z_ifbFKJP_0-JU9lz7BCKYZloJP2gYRSc31cuDhfvVtCfCLrflUVCVtJXwfIw5IF-kgdQW-lP0EwWnUNoh3r8l02-23ikqTfbNvQkwXOJoZQwCRbW72OyggHjDvrwuGfDTvU8QCyT7dJVhuGniDrPRTU6AYHc34jiDAuxQa8RAoLotH_Gnpzg-Ni_W0nuggvI3ZLd7DKugVNdinyiIWuagXZQ0JZI3ZZWpc49RoSoS-r_S_o5dkvPtvy3beI8dP2ZSNUYHCtLgn40b_kBUeH5JQ-VPmJT5DSstPpjOB6J9Cge-yZj7IPqF2eqJPI6KLpOoGXD0GVbBOyR67mEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c757a44e62.mp4?token=lTJ9Z_ifbFKJP_0-JU9lz7BCKYZloJP2gYRSc31cuDhfvVtCfCLrflUVCVtJXwfIw5IF-kgdQW-lP0EwWnUNoh3r8l02-23ikqTfbNvQkwXOJoZQwCRbW72OyggHjDvrwuGfDTvU8QCyT7dJVhuGniDrPRTU6AYHc34jiDAuxQa8RAoLotH_Gnpzg-Ni_W0nuggvI3ZLd7DKugVNdinyiIWuagXZQ0JZI3ZZWpc49RoSoS-r_S_o5dkvPtvy3beI8dP2ZSNUYHCtLgn40b_kBUeH5JQ-VPmJT5DSstPpjOB6J9Cge-yZj7IPqF2eqJPI6KLpOoGXD0GVbBOyR67mEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل‌اول اسپانیا به انگلیس توسط لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107336" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107335">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اسپانیا ییککککککککک</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107335" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107334">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">لامین‌یامال زددددددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107334" target="_blank">📅 22:22 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107333">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107333" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107332">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXZnFTzROBVzBxPNVGdeDUeUrfVS87nwQSQCWRxVbvV-oIS73ito-zz149H_E6Pwnb8GwIa8vsSEMkvUF9NCu0Yd5jCU8CBpjnVslRELyQtb5IoO-vwzjPibIQBpn5j90WH33uj0Q-kqF4HjGkfwHTXSK1hcVjekW3FiuA5KZaEBKE4FfacqAZaDfbQkkhA8y8aaGEZYFqDEIlJfpZlaTR2MEEw3kfTg4pQzyIB8S9_BNeqCNcr1y-M_wMClO2BYOnlutEooZo-K2d62OhFp1EZqSYh6E-9TxjkpF5dVRcrjTyKVabJxJDfBlN_ZHDZuADbYeqw2GY1UY5kAfJYpxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107332" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107331">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇮🇷
تاجرنیا مدیرعامل استقلال: همه چیز برای اهدای جام استقلال تا قبل از بازی بعدی آماده هست و صراحتا میگویم به من این قول را دادند که این اتفاق بیفتد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107331" target="_blank">📅 21:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107330">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-410DfRxFs73Cf-mua5m2w8vcLHSB8PRl6CUW1Kz0l81bfvQ3NevTfjPWsOyx9LiAMWyl0c0SbGXO_rrB6V4jY_LmAkp6yI1hJJVNexRgbl3aIy6wn7LYgAwIRj7Qa2VA_pyxXLOlgmskrS7NKzDBIB46eFSZNSEobv8xqInbtPaqvGsFZVpeyjVQGOJxRphCPHVTbnt60sdmpwdDm3TwUIFBjHZGZAgOdzBtpaUjCeeuNmfeZLAKDYQ6Q2PDGXKdqBeMG-4-5VIvzT6DhnnVQFm5tkSq0QMVIY619lKsLNyH__v5yyS51mfCh_NO0_wfp55-b44JNJjHzPYwr0jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/107330" target="_blank">📅 21:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107329">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jny2-6-2HnNxpDVRbX98MykqtAUdOXf2zHZQ1VgHua6pNkNtp8gpMoy6y676omo8KWpDdbcordcOhG0AYRzIW1LKdf52kX_C6n7zw1apIRvTqkxykQusg7F9fTDaa6hhowjBuqPTEF-Xh9M_Wm6GAAhAKzmpG-dueRCPGVl1siJ7cz0yAcvttqG-wJeTQ_IbBYhg2XID98qxKnZYphX0hJrEFjxfEYPdpGeT2PCzhfTjOfoZ7XnRfJuwpzNHUZ5Cww2hKpZcOHxlotHGFdYlJa4BKY87c_1bqGAcpq7dUF1lZya52DN4hnkRvlmEI7tvtLWkAgXp3RY-qS9BMo1-GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آمار تقابل‌های بین انگلیس و اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107329" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107328">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GC9A4ggbYQ921QVzZMYSMJVIPQA9F58oTrHub5LDDin64wuo9kh2oXaqK8a75w6qohD8C8iW2DyTmZTpFhD1m05tYm2f7_tLWa6mM6Zm5zFZfvIok8TeIevJp0CYWisa6TIqMoTsgIp8nkE1TU33cyUdASEhRurRiUkxsE9jzNb046BD98HBrskP6r2lBYynyqbscm5uMD3F1ajcfztRofWL4X3i7TZzGVkE7HN1VSzmgnUJJR3vpzkitXawYHROKzl9UOA6-_EGhjtNYDTQFIq86JwmIB6d7-FWK1rrkYKWBm6imwBkFy9zmDx6jpHM2gMUF6SHn39fGlq4JdY69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
✔️
شماتیک ترکیب اسپانیا مقابل انگلیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107328" target="_blank">📅 20:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107327">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=cduxEXHlJylVlIwE-8i2n7BEikCahdYnzhizhjIVgFo2LEvMtS51TrZ2pdp18JBifnjpUyU8Ig9APMHa0ugSZaWTw-YlX4DneEnw_7aI5zViAYiyBLeK1gHwmcj3iH0BtCu-HICavBQyXQ6RDRFpSZ6Nm9tY6GuNhxSUiVGKqzwPT6IIADkuiq4QVTadxnbvHeLp2qA50F6MtTnG79VOM8Akid7lDv2PMjEAr4oH7OtmIE87x2kjJ9hmZNL4RG2-6oHLykFrxPACMblUUVuB5SXkzoZ2n5yOgJkrMjs79CxnXgUzcA8Nk4DvlEgQ5ijhMrYRvflhZ7KpuH7426BRmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/591cd9489f.mp4?token=cduxEXHlJylVlIwE-8i2n7BEikCahdYnzhizhjIVgFo2LEvMtS51TrZ2pdp18JBifnjpUyU8Ig9APMHa0ugSZaWTw-YlX4DneEnw_7aI5zViAYiyBLeK1gHwmcj3iH0BtCu-HICavBQyXQ6RDRFpSZ6Nm9tY6GuNhxSUiVGKqzwPT6IIADkuiq4QVTadxnbvHeLp2qA50F6MtTnG79VOM8Akid7lDv2PMjEAr4oH7OtmIE87x2kjJ9hmZNL4RG2-6oHLykFrxPACMblUUVuB5SXkzoZ2n5yOgJkrMjs79CxnXgUzcA8Nk4DvlEgQ5ijhMrYRvflhZ7KpuH7426BRmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
✔️
توصیه عادل به بچه های کنکوری
😮
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107327" target="_blank">📅 20:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_MZudWJ3R_ImOuFn4woD3Yb_oDLignsDY6HAlDjIQnj1u7ehTKYGd1LvKONwexfarVQMiNCjfbC8XYtRPH7B57jIi_NnC3naMfaSJ1kFyT9I-QJqOlDZOxYVqIz6SxutydYU6CI0mreCMwJ1Dqu5uVsfIRyPvjFgbuFdibhddtllczxl6_yafWvu-AR2Jqv4h0MLDTPqBaku8HL3olRi2x_ASjgnWbCnEf42EhaoOQRO4Y05EHhemCdkdmtBJtaYvVEhY-MqgfS-Okgj0ulgjhQmPEhXBPVEiJ9eAMOmhYCOkT9fqkx1HKLyAceg2VPpWqwLWUsB7470-j4QP-FQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
👤
علیرضا دبیر: چطور مهدی مهدوی‌کیا با یک گل به آمریکا از سربازی معاف می‌شود؟ حالا هم علیرضا بیرانوند بخاطر مهار پنالتی رونالدو باید از خدمت سربازی معاف شود و هرکاری از دستم بر بیاید برایش انجام خواهد داد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107324" target="_blank">📅 20:49 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=HZ_YEhoj4RrLOBM4KaUBpb81mJzp45lDJg0FL06ERzJh6iBwgSs3xR9wwO95BGx4qpgshK9IGxs-d-1_D9h01XCZPDxShziEA9jrg9iyyA00T3mi42geVZKT0Sm1_C0zZYbqn_UXesuSHapb-XQLatCL2wC5RC04M8_SjQWl9mPUcBAOv-5uSagjPkUfuCb8bi5czVQTgctQO9mx6Yc1dT2mfkxL_N_iSyihG_-Bq53PffTEU0MJhhe3tJj40WW6jaNfq7brsMlbrUqzHi_K2CzZVIb1_jY8JQTVGNHlDLvh0nI99ldMshYwhB6SFLlirrZRlRYHJp1W1E2FDtxLyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc1ed24863.mp4?token=HZ_YEhoj4RrLOBM4KaUBpb81mJzp45lDJg0FL06ERzJh6iBwgSs3xR9wwO95BGx4qpgshK9IGxs-d-1_D9h01XCZPDxShziEA9jrg9iyyA00T3mi42geVZKT0Sm1_C0zZYbqn_UXesuSHapb-XQLatCL2wC5RC04M8_SjQWl9mPUcBAOv-5uSagjPkUfuCb8bi5czVQTgctQO9mx6Yc1dT2mfkxL_N_iSyihG_-Bq53PffTEU0MJhhe3tJj40WW6jaNfq7brsMlbrUqzHi_K2CzZVIb1_jY8JQTVGNHlDLvh0nI99ldMshYwhB6SFLlirrZRlRYHJp1W1E2FDtxLyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
عصبانیت‌شدید یاسرجلالی آنالیزور فوتبال از وضعیت وخیم تیم‌ملی با قلعه‌نویی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107323" target="_blank">📅 20:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
🇪🇸
بعد از تست‌های پزشکی مشخص شد که کیلیان‌امباپه حدود دو هفته از میادین دور خواهد بود و مشکل خاصی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107322" target="_blank">📅 20:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=DO7_SllJ1gc7A7PEtqrULufFeOTAIbb1n3-BlmTIHT5r1RbQ4Jbv8sdyb8ajmczszZqcqHvK4axE0txMzPabHm-PwhB6da3TTHCDyaQQbO_i9S83lE1DFxTZcZBlcQPU8_W99ob1EYaAWtC1vGUXeKeP00dPh2muntpdg_Ao8Gt82kPT6YmJbNhr6XLGEYoENQ3Y_Cxci9VYeQj2y6FsO4gI46Cer-yP-o103PAGfDJqcFu6mX05DgplpeN0aKROP7g9qUx7qb2HQ-A3c41Av6_VD-09vxpbc08FTFoaTZSUQ8AI8CqVfaitqnYY36gLDAzNyfUidmdnlvT8A9kWqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6fa8be9960.mp4?token=DO7_SllJ1gc7A7PEtqrULufFeOTAIbb1n3-BlmTIHT5r1RbQ4Jbv8sdyb8ajmczszZqcqHvK4axE0txMzPabHm-PwhB6da3TTHCDyaQQbO_i9S83lE1DFxTZcZBlcQPU8_W99ob1EYaAWtC1vGUXeKeP00dPh2muntpdg_Ao8Gt82kPT6YmJbNhr6XLGEYoENQ3Y_Cxci9VYeQj2y6FsO4gI46Cer-yP-o103PAGfDJqcFu6mX05DgplpeN0aKROP7g9qUx7qb2HQ-A3c41Av6_VD-09vxpbc08FTFoaTZSUQ8AI8CqVfaitqnYY36gLDAzNyfUidmdnlvT8A9kWqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🙂
تو مسابقات کبدی بانوان در ناگویا، کاپیتان ایران حریف رو گرفت عین گوسفند پرت کرد اونور :))
بعدش خودشم زد تو سرش بابت حرکتش
😂
😭
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107321" target="_blank">📅 20:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=pvANh51r-U8zCwaTruwL5I8cu6ecJl1s8XLqP1mz4L8N964v7bfd93Rr5whKqrD4c7KXxBRCUDv8DzGzv75OCgnuW26BJdOy6v4TOoiSkeuvWgWuWZeI-1rQVKM1IkGPgxwPLHxNI8VqaFcI4RAFrYB3kYC-bWr5N_WbG76xxJZm4lG6Mop7sSX9qN5bVL9zRb7pxIv7a8AEWw8q5FNrca8KNjEWOaG9HNiXCg_fTKdK5EEJNy9qo4SBPsGxV6KYk5KkslPRl1DPuOVU_HUX40oQMI-6CIrsrHA7poMseYqX7aMx-_rmg7f1qV2r08d88Ox0mwXPWnOBgSJ7212fPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95b7a70c4b.mp4?token=pvANh51r-U8zCwaTruwL5I8cu6ecJl1s8XLqP1mz4L8N964v7bfd93Rr5whKqrD4c7KXxBRCUDv8DzGzv75OCgnuW26BJdOy6v4TOoiSkeuvWgWuWZeI-1rQVKM1IkGPgxwPLHxNI8VqaFcI4RAFrYB3kYC-bWr5N_WbG76xxJZm4lG6Mop7sSX9qN5bVL9zRb7pxIv7a8AEWw8q5FNrca8KNjEWOaG9HNiXCg_fTKdK5EEJNy9qo4SBPsGxV6KYk5KkslPRl1DPuOVU_HUX40oQMI-6CIrsrHA7poMseYqX7aMx-_rmg7f1qV2r08d88Ox0mwXPWnOBgSJ7212fPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🎙
حمید مطهری سرمربی فولاد خوزستان: دوست دارم یاسر آسانی بازیکن من باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107320" target="_blank">📅 19:47 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107319">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=lvy18X8svJZzYHoVBav6evkiTyKNZuYpz4Xgt7cEe1LK8uHK_qyihbQEHT8Qm_Fi3M4LeId-i_Sm2ZqXG3ep0ZWJpCv-E1IWyRcLFMVQyycDPRKCWm1qKejv5foiKvWGoI6bXEQfuoxSO5wzsPhvrEcn23IjWMpUnv9gWxW5QJGxkLPnVQQshj-5O9EuR9pAuh7OdTMGz7DyQ9QUydqHkpU3vSm5lGKUOEitlUstdR7FbH9qePTzr5k02nVmXnToWybx0tdjoxctp6imh3vuxJQsNwoMFiasv1NTXecOT6bRFc_P33hzwMlyw-we7IdAgYR1PGiHTpsHpA_fXKW1Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b399b2bcc.mp4?token=lvy18X8svJZzYHoVBav6evkiTyKNZuYpz4Xgt7cEe1LK8uHK_qyihbQEHT8Qm_Fi3M4LeId-i_Sm2ZqXG3ep0ZWJpCv-E1IWyRcLFMVQyycDPRKCWm1qKejv5foiKvWGoI6bXEQfuoxSO5wzsPhvrEcn23IjWMpUnv9gWxW5QJGxkLPnVQQshj-5O9EuR9pAuh7OdTMGz7DyQ9QUydqHkpU3vSm5lGKUOEitlUstdR7FbH9qePTzr5k02nVmXnToWybx0tdjoxctp6imh3vuxJQsNwoMFiasv1NTXecOT6bRFc_P33hzwMlyw-we7IdAgYR1PGiHTpsHpA_fXKW1Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇧🇷
عصبانیت رافینیا بدلیل عملکرد ضعیف وینیسیوس در بازی مقابل استرالیا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107319" target="_blank">📅 19:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107318">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEUq8b0Fg1o5P2ErHyandtIt3t4zgUOU9FiE4ymWah-SJD0-SZrOMyK_HMnnyBMZmgp76nbiaE1kDDdgoaAfrzfSyU_gE5iORVsVw5Ut3VZeXnwOoD_uu7dMySF0PBveOp3FWfZZ9lImbUEWNUf32Wv0BIYkOvncC3KgrS-vdhxFMJI6Yj6nQ9rOxBzqFyigSUA4lcJVzt4J57cYn7yj2nWH9mtatI-jmW6rdSrhx2p-hAiqunibbcvLYrs0gcEuIZ0XdNkpFlLmFWo8MtsZ66n3RsDfd0m9z0JSIejTpegJE9Dl6J4w-DznWWqw7LjLo8CG5GM5LwmAdekWI_-mog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
پیام‌تبریک مالک باشگاه استقلال به مناسبت سالگرد تاسیس آبی‌پوشان پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107318" target="_blank">📅 19:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107317">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMNWQX-ndtYYL19vpfubYeQHlBwIuM_aqR1JWR3HOSMoaoOrCnCxQh1yFLW-8zxb4jTRhKKi78PAEGb94uKs6TMx9fFhtm8pXHtzjcglRMNR8fWAaIDqrOopqnUEcZhuIIAkt1JPaZ6gvNYpVpDk3X6_QwNWGNZ9cZI-xYgp8r_MimvkeJEEch1zIQanewSqpqUnvJWO6Nv_ZuYkX01NU9VrHz6H-zpkcgNiLIPcwFJMUw58CH_7tzx1KnUhhOsKhgdbCvCiRJMMFZNe-RxZH99y_F0rEmxCoDlp4f2hzfYTtEAjFF__S4_N94TwsbOeKpnu26HReVGFp1b6-ba00A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
چند روز پیش موقع آغاز سال تحصیلی تو تهران، تو یه مهدکودک مربی از بچه ها پرسید شغل باباتون چیه یه پسر ۶ ساله برای اینکه جلوی بقیه بچه ها لاتی پر کنه بلند شد گفت بابام سرقت می‌کنه تو خونمون اسلحه ام داریم
🔻
مربی میره به پلیس میگه پلیس میریزه تو خونه این پسر بچه میبینه چندین اسلحه تو خونه دارن و پدر این بچه، رئیس یک باند سرقت مسلحانه از منازل مسکونیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107317" target="_blank">📅 19:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107316">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgxtGhdeKv00AgbiKN1fiYcaITRdjYf6ERA7OqXFAY3RAiWdCA2sEGaI37Urb4rrTngIeqEgP6bpzcyZMj21_7qCpk8_8nVBvTL5ozSKmi52RJCFTjSFtWMJ0gAYcTE5_nvtzhkHclUYSj0mhP3unHWh5u432H36y4Eov_rwGu5rcwMZvPq13xmW0m-3YYGdy-FRxcfqNjU4wG4yNr88dbmxtXWUTGXwXmVqb8IVyh4EA4uO4E2WhDS8QqN5-H1mesfOILbNl0qYT43FcqPhizmuuJ2UgQ3mr1KIy-lEhgJI_3ZvyWubTAYio5784XeYfDi2i1BY6ampSWzU0yx1rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
تیم منتخب انگلیس و اسپانیا از دید هو اسکورد به بهانه بازی حساس و دیدنی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107316" target="_blank">📅 18:40 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107313">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=Ft1aEjwX3OZ8RnUAQMx_4G5IRXKLlUxW2ovhyJfR6gmYWPyxp7PVBYYpWiGBVU94lrBg8IO6elNtbm0CJy4fABjqt1Qg8VA89Z0Vqjydj4FkzK-1mJ6vhgzUA_FL_1BOM5u1nCQMEFMipwdhcgQXd-m642vDI3JpslOlvKbc8Ehk6UkcRYc5hyIud-j3z8iSA9xudTjuRvY3gK-wsDoYrV7405bU0YYi6Zldl1FDxMrk0c3cBvcdk5krwXfoHF9iyu8aa4LOZoT7emrq1m4Ae635k8eT11H-xQyPuj4fH3GPXzhUZf4EO1htT0Ot7JtseJcEHlpWcZ86VweIO63gSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a50b6c2404.mp4?token=Ft1aEjwX3OZ8RnUAQMx_4G5IRXKLlUxW2ovhyJfR6gmYWPyxp7PVBYYpWiGBVU94lrBg8IO6elNtbm0CJy4fABjqt1Qg8VA89Z0Vqjydj4FkzK-1mJ6vhgzUA_FL_1BOM5u1nCQMEFMipwdhcgQXd-m642vDI3JpslOlvKbc8Ehk6UkcRYc5hyIud-j3z8iSA9xudTjuRvY3gK-wsDoYrV7405bU0YYi6Zldl1FDxMrk0c3cBvcdk5krwXfoHF9iyu8aa4LOZoT7emrq1m4Ae635k8eT11H-xQyPuj4fH3GPXzhUZf4EO1htT0Ot7JtseJcEHlpWcZ86VweIO63gSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
گزارش جالب توجه گزارشگر مهمترین مسابقه هفته دوم لیگ زنان بین استقلال و خاتون‌بم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107313" target="_blank">📅 18:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107312">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRgsCBSFaWdsshz3CMXtV9EDDTg54wZ5mjEiJxn4mJWSvlJbNLS7unPndS2Ry3yFzzwuwfjtsFEMzSOi5nOQuFITFcedX1WwTITg8FSuzLNKpOhkvAnbZFQ9KtiO4-rQdJb-XGJXqzEvY2N8tuaUAIdRokFjsCoTM2CeczpiYqVHWsuPMIJrPAZO9CH4bE6DnNYc9hmfY8QDEJFQwA3443g-hkn9kEjUwJ74u3ARV08p65xnizmQkNNxvtb7KOvUiFxCAChQZ00Ohvzb9sGAMo40jWRlNcWGCekDz2WTZBLxAQ8JsOsKk3UBBtzjl1YGV9k-3CLpJkHotgWi3S38yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رودری ستاره سابق سیتیزن‌ها: آنچه ما در این سال‌ها انجام دادیم قابل سلب کردن نیست. قدرت و سیطره تاریخی سیتی در لیگ‌‌برتر هرگز با رای دادگاه از بین نخواهد رفت و قهرمانی‌هایی که کسب کردیم در عین شایستگی بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107312" target="_blank">📅 18:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107311">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1OvXlIXuzXCApagN4tPzUiImWOt0Vvmld6ZTfz8XQsV40_BLgUJus9BDgLfdkt9mPmOtRnoCCVz90wy0vVoc-WxieOf7DG_XWNrYor-0gqBe7Ql_hemH4vw3uOcpspw2YV2iIWYgntxCbmXmJAhUIjuQ0Xm9-cTA-3efbZ0ovhjQOb19rRMCZciIdr254JvaIpfKa1vkE837DDDr51O9GxvVeumnSiffrG_XDmq4CpA6wraHQpYkFj_Y5yJE-3btz3K4vFszssfCXMxRCtZg701O3nkMJXZ8kq4Pn031MI44YzG_EAx7udcraotXF6YeztRXPgkN191s7yHo_an8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👀
لامین یامال ستاره بارسلونا:
🔻
من برای پول فوتبال بازی نمی‌کنم، چون دوستش دارم بازی می‌کنم!
🔻
بازیکنانی که وسواس گل زدن یا پاس گل دادن دارن از بازی لذت نمی‌برن.
🔻
من برای خوشگذرونی بازی می‌کنم؛ برای دریبل زدن، برای بازی با یک یا دو ضربه، برای اینکه به هم‌تیمی‌ای که هنوز گلی نزده کمک کنم تا گل بزنه؛ من برای شادی بازی می‌کنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107311" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107310">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
⭕️
⭕️
🇺🇸
ترامپ: پیشنهاد ۷ بندی ایران را رد کرده و اصلا مورد پسندم نیست
🔻
ایران خواهان توافق است و من هم از توافق خوشم می‌آید، اما این پیشنهاد غیرقابل قبول است. ایران خواهان بازگشایی فوری تنگه هرمز است زیرا متحمل خسارات سنگینی شده است. من هر توافقی را که بر اساس آن ایران بخواهد فوراً تجارت را از سر بگیرد، رد می‌کنم زیرا متحمل ضررهای بزرگی می‌شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/107310" target="_blank">📅 17:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107309">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB2WoENNcA8Kafn5hUVacSM8j6HmzIOTyOd_-tQl3rzREo16SF0N-CLWiFNAHAaYk4W9sNiWQbIP3GAmdeaakVHilSuL6g8QjqMNd6XJAqAk6-vKxojOuoWVhNPp5bQKMOqQlQ5swasyU9YTn5qiCcXwEZXZLDGvDwKshAZFUu3COUob1C0P_KpH7nPuMGxbw39j615Nzn6LXxBSceUx_hChWBskzPSWky0Prm-oxWtXG67sAAVkl4GIJD1iIp_rKBGb2lXB_id0qcyrsk6ruYAC1rCSsUMhuLQpSKjtL7YNDVPE7HmVNf94ckMy6ShXs0qKGfFBrdauWwUHz9HYRwxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712da7f0e0.mp4?token=HCsIC5Pln8fQukKF42XkmaWALARqN1_LnNl45XvBuxFcA6K_ycSAtj3bEEvNLMta4oLp7b35kiWdvMQN3gDGMgEhhWfYhythwmpc4unD1BAM6xY9J-WmU7WLE5lArOSFtLwUAvmSOSl03xV9u39ifV-6yNd47PtiEVqN_O9gkuABBO_P0W1ben9y2tn8GBWcnnS8tPbqggCZo-ft2RSqH-8PemVe5jfUfJ_WRSKt_rE2qz8AbZ3voM-x47qMtfbKt2wyLEwqBx0ju76_EWj5WeJYJSYvV0g3wmNoBounUQ0-ZTnMWohJodrRFOXxyiWIktAjdJWiaMgoumcYWR1YB2WoENNcA8Kafn5hUVacSM8j6HmzIOTyOd_-tQl3rzREo16SF0N-CLWiFNAHAaYk4W9sNiWQbIP3GAmdeaakVHilSuL6g8QjqMNd6XJAqAk6-vKxojOuoWVhNPp5bQKMOqQlQ5swasyU9YTn5qiCcXwEZXZLDGvDwKshAZFUu3COUob1C0P_KpH7nPuMGxbw39j615Nzn6LXxBSceUx_hChWBskzPSWky0Prm-oxWtXG67sAAVkl4GIJD1iIp_rKBGb2lXB_id0qcyrsk6ruYAC1rCSsUMhuLQpSKjtL7YNDVPE7HmVNf94ckMy6ShXs0qKGfFBrdauWwUHz9HYRwxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از روزی که رونالدو نتونست مثل قبل بدوه و هتریک کنه، موتور تیم ملی پرتغال از کار افتاد!⁣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107309" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107308">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=gH3a5U4FYB9GFsFpGT4KEQzITdWF9GlziKGSMeE6M7iYEcOKaiF2XEHJwJNqkK9S-AHHeUHV692moGkOuJUk8NLHx3j56s9--aaOHVZ9CSOlUiQ1iACGsfJ7muTncluFGpqdhdDtfHQfybH9JBnVdzVQRY2S4WClq991pHpqwFfcppDL37rjWjlN8gXPkxnkkMgAGh-xCcdTFHBFvDD_ZEl-qm08D9TfQSknyu1L_SgHN_6qfRNuLMbOE66WF_afIgmTFDS4Wa8ukxosPOymK5CvnYr6GDqx0cNBrXEP6h6huDPTKKb5wBp5BOqNd4sb6FeNaTP-Uz_WoyqmIWbN9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5c5606552.mp4?token=gH3a5U4FYB9GFsFpGT4KEQzITdWF9GlziKGSMeE6M7iYEcOKaiF2XEHJwJNqkK9S-AHHeUHV692moGkOuJUk8NLHx3j56s9--aaOHVZ9CSOlUiQ1iACGsfJ7muTncluFGpqdhdDtfHQfybH9JBnVdzVQRY2S4WClq991pHpqwFfcppDL37rjWjlN8gXPkxnkkMgAGh-xCcdTFHBFvDD_ZEl-qm08D9TfQSknyu1L_SgHN_6qfRNuLMbOE66WF_afIgmTFDS4Wa8ukxosPOymK5CvnYr6GDqx0cNBrXEP6h6huDPTKKb5wBp5BOqNd4sb6FeNaTP-Uz_WoyqmIWbN9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ابراهیم‌شکوری دستیار حسین‌عبدی بعد حذف از آسیا، از ژاپن برای خودش آیفون ۱۸ آورده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107308" target="_blank">📅 16:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107307">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/275c393efd.mp4?token=DsVOfLItW5AfO0jg_9eZUDjIgfgpCrnb-SCEXhAalaBhe62sbAewh2r8zOVlQ08jgRWl7F0WuYJPtnI3lkeLxIVkmdh9CxcK9UAp4wuCvufdwDLWVMvD2QptT6hnJn1T_XgqHVDbKl_y39tTMvbpPDBSO1TKpIsBH0JDQSp9p6cwQQqunzJs0cUSPWIjDV8RfLC2nvZasZYXEP3BCiBjppGF5H6nXcIinaFn7HBQmzM_nNqfMoPxI1ZU6-2o3oZnlDXKRomox9MSmt53jswfxlpoWBvBu8-U-Tr5MIP5uqjelgQkDej_S6x3HrNyWWXDUjjznZBQxortUjwBHxfSMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/275c393efd.mp4?token=DsVOfLItW5AfO0jg_9eZUDjIgfgpCrnb-SCEXhAalaBhe62sbAewh2r8zOVlQ08jgRWl7F0WuYJPtnI3lkeLxIVkmdh9CxcK9UAp4wuCvufdwDLWVMvD2QptT6hnJn1T_XgqHVDbKl_y39tTMvbpPDBSO1TKpIsBH0JDQSp9p6cwQQqunzJs0cUSPWIjDV8RfLC2nvZasZYXEP3BCiBjppGF5H6nXcIinaFn7HBQmzM_nNqfMoPxI1ZU6-2o3oZnlDXKRomox9MSmt53jswfxlpoWBvBu8-U-Tr5MIP5uqjelgQkDej_S6x3HrNyWWXDUjjznZBQxortUjwBHxfSMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
❌
آنجلوتی بازهم به رافینیا استراحت نداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107307" target="_blank">📅 16:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107306">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am7TSiYkbnXixSCv75orruOVICJuMnCwzmIPP5BJg4q68t-WPiaus5cyS7szlrddOpItxLdmnK8eN2PJxuBuq0i_RptZd08KIDkdnbqQsUYGM4-A4O9iXkSiS2Z2D1Li5oISnkTgZ5i4RphDMTrZaPmsf8eqS0tYY8rPJfadOVU88qhhJ99dWd-zY122KM3zfrAK1UTT6NfBJiiqHA8xO-EUwoSJLXMvitgiS56prql68rTv84k0Uh51ReX796PtxKYmVy-OREoC2hRVNKwv3UVKeSg6ZN84yWm_WDF5Za26zCclFe9KqZVghMcYPv2PkAWRsdB1Xlx4sISOqWe_eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
🇮🇪
چند بازیکن تیم‌ملی ایرلند از بازی مقابل اسرائیل انصراف دادن و گفتن که مقابل این کشور بازی نمیکنن. در صورتی که این اعتصاب گسترده‌تر بشه و ایرلند وارد زمین نشه، اسرائیل برنده بازی معرفی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107306" target="_blank">📅 16:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107305">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=Jhv-BreI7EAxVX1AZSXH7AiiZmGbgJyjSNr6l5M52DiKRCkXJn0GgBkyLvK6Bte4F6zGLlk7QzbVNWUQhokqGfgz9n1E53WD7evnt5fGv4VHhzWJIVw-5iETHWQruaQ87S4x51GQrfjtr9nm6e2njqaN5DafUyWzcVjl6qrABVU9CLJQBahQvdODS14g9ZRzZFFIACJ6oZ3zjYlSd_HvHxZ2QJMRA1c9t8sLax_iann34AfgKKQ5puM00DDO2FP4dMkKumcD0rBzDB1AovgHWGrOvt2gbaS5-WOMos4Dg9TiNfxVns7AhJg7bVAXRFsLYeIwwrNSWOWL4doDr4mW9BKDawsFc134oAI6VIXEqk4rTmTMTRxTrp4rNrBRV9eqfbkPmU6sZX8QC9hLUeDGymNdi-ibQUp_rjRWIpnlWB53MiSMCCfhLldvunTeL1vHrWebAhz-mQ8FfNrSEuV0RfPMLeM6PnUpHVTE2IsOPRCzOB1PInHiuofgDFYcA0U12KncXyVgpbmEUee41P5RupxWH7NhzSZvkaAPakRFngvnKy0ew6h_o4X_0QRB2s1N5fZScMuSK9Y3O46vc3pbKlT08z1si_-vEf8PNXznAaUFGlqsAfs-G2ltWcm9NsZpIe2B6EXLYPTUKfWpVMNFrQlu-LVhp4k2HHzhG5JGl4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b29264e5e2.mp4?token=Jhv-BreI7EAxVX1AZSXH7AiiZmGbgJyjSNr6l5M52DiKRCkXJn0GgBkyLvK6Bte4F6zGLlk7QzbVNWUQhokqGfgz9n1E53WD7evnt5fGv4VHhzWJIVw-5iETHWQruaQ87S4x51GQrfjtr9nm6e2njqaN5DafUyWzcVjl6qrABVU9CLJQBahQvdODS14g9ZRzZFFIACJ6oZ3zjYlSd_HvHxZ2QJMRA1c9t8sLax_iann34AfgKKQ5puM00DDO2FP4dMkKumcD0rBzDB1AovgHWGrOvt2gbaS5-WOMos4Dg9TiNfxVns7AhJg7bVAXRFsLYeIwwrNSWOWL4doDr4mW9BKDawsFc134oAI6VIXEqk4rTmTMTRxTrp4rNrBRV9eqfbkPmU6sZX8QC9hLUeDGymNdi-ibQUp_rjRWIpnlWB53MiSMCCfhLldvunTeL1vHrWebAhz-mQ8FfNrSEuV0RfPMLeM6PnUpHVTE2IsOPRCzOB1PInHiuofgDFYcA0U12KncXyVgpbmEUee41P5RupxWH7NhzSZvkaAPakRFngvnKy0ew6h_o4X_0QRB2s1N5fZScMuSK9Y3O46vc3pbKlT08z1si_-vEf8PNXznAaUFGlqsAfs-G2ltWcm9NsZpIe2B6EXLYPTUKfWpVMNFrQlu-LVhp4k2HHzhG5JGl4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
ادعای جنجالی کریمی: خودسرانه برای بیرانوند دفترچه پست کردند؛ در تلاش‌ برای معافیت پزشکی او هستیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107305" target="_blank">📅 15:53 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
