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
<img src="https://cdn4.telesco.pe/file/UVE4kDOR6uh7OvvoDUfGIXEaULS_ae5vGc8mSAzYrelbWk1gt4_Lc4dK_Rr_yDCzocEo25LoQyOLjVAyU1R35VACJl6sb49IaOqOPRmvPtjufM001mHfI4nK3wWTiflKjiaoGUNTZ-sVu5ACHdu2zJGmuB0w6Du8iZLx7Pr79RTH5lxF9y6BMNvDQIio6Fok9ztIyK4CygvczkAORQVu7jQ-vToGBQcbPCuJdLrFFkeXGu98o74J3R-RNXoTaAuEulT9JcrkIomqPTiVADI7p5KjSJstfgF9lzQNvi4Ain8vB2HrVO7Yd-hS5UOXTyr8aqVynL-fiCHC5jrWiE0Zsw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 425K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-25492">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c6aec402.mp4?token=OxS5pln_9WuVipuUEKlr8uI_lJaRgPz45eQkwylKSYvXRzvaOIzbhhYWQfXzAJCteq5T3k0mMuD0raItEi5AdBMB_fgoYy1RxCF4ftSTF7leK319AYh7na4r5CpIuJ1ThN_AOc0bpuoSHMpbRcuGSRG0ppgECP4nB0CUQJmRC_v9AWLG2jW0rqy-hkBxWMocjbxuDAbry_Wgqm_VayiRSLNeKIuMNxuOcg8MAxDUXDw6WJI-X1mGkFYdTgwUFxhVGTb9iHACdQtRk_htzK7tRTLVDxH-dUPOoxbpQgnoWsGc6mqQQxYaps3zZTB-uZMwVlaoVYfFghIWihk7g2FWaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/25492" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25490">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T_j_kptCKXSiPEEGiIf5YYdSrSnqmgR13RFH5h2gyLTCXUV78C28v1erYj1vvq-QEQ_JOGqj71vgSZ7B28jtDsAEwE5p50TZIT5J7fqpxVCIs7MPH4mepvn56wgGWIYMQXIC5iowtfn97kND4YJ26ETiKY58IKJZ3jxUM0JRxRw8rwHyWcSzArpVb4WMC1qIoC4RADcgo_MPj6jqYaQVxE87OeVryBs4ShzDOLhTLEhSdBsgRS4hiG9-eioKecf29_fPp26uMQIK06jMnjJA2o5FbDdMViyYD-8Un_LAAitP0YaS_EkG34ycfbGDV7EsgbOVH0Z-gKvbUQVkCiqiog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1-RgkumQMhyONcM4YamG7DcL5gQbQjD5kcV35QWp3m6MuAi5FkonpYilB6f9mxlN14ZDW9RRqf7XQu5ewJ1XLnZksHPTkrPCXYAzyr_DE3XMQlVQ49LmjJEPkS9ISADPb_tcS_XA5xIxEkcC5hv0GtmpXEvsN5Q0zn2pjgupG9nf8SeLTItCI9ajovyKGepjwZLM0StTleW-Ce-bCCtEjulnEL9mBssQxt63BiK3LriP-egxYbr5HHkS68-QH7ZzoCNJWYdvBdZtNW2rMkD_DXH1ZIrAERL6dYZoAmX1dNLmfGZh9hrgSxFjXAmmyNoN0qZXZmPR4WHnh_DiB88jQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی؛ صعود سخت و نفس گیر یاران‌لئو مسی به‌نیمه‌نهایی با برتری مقابل سوئیس10نفره؛آلبی‌سلسته‌حریف سه شیرها شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/25490" target="_blank">📅 07:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25489">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iipIDfJor0R5Jk99q0-b8TRx6xpnuPY8G5BIO9_qDTsJpS-XtMaRJFJy-sfaYgxh0DkZTixX8-aqlARPMIR-ZDe4GWWoX3C-HaAhYfAC6N4-1X_RP6Ob5G9rjrPx0WuMRUVDn7RMRcSIvtEwjo5mHWjqLaNk2ya-Ci944aceD3B-K4227NqOc0jKqYJFImBq_61FLlSUMQGl_SjzR-LvghBsDC8uyUGADvVmLVYJzCMGcfaABWjmAmkDCrsV10o1rRQ_Y3jyeixiklcIHqa0hgLTIHAJ5I4-qiX4B_uB0hECISF1NbexT1lbxNAM94SLBkzWMpIGZagBx5hkIdvFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک چهارم نهایی جام جهانی 2026؛ صعود شیرین سه شیرها به نیمه نهایی جام با درخشش و دبل جود بلنیگهام؛ یاران هالند از جام کنار رفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/25489" target="_blank">📅 07:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25488">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQMZ3R5UQaH0wfKfqi4f16GdHEIb28jVFdJQJ7vhmDkvhnktN1VFHWpmgfEiQmuydj7fay2FSg2jvhH8cjCCWx1CXETtG8TyXOaoQ-IqaJO0xKPGT2B8WIi07yyYxpii0zyLlmWJp044nguWa6_PS_YaRWKqp6P_FufrI4xJ8OMNcQSbSFxXQnhvmXPGRaJLQQjsqFfHl6-KOrVVt5rsG8dn_FSqcDaDVsgo2T7CcZRH0P2_Y2ca1HX_YWSsGr3kjhvQzcPjFaRrqeQD2oRE4fts0vpXfydsZipupD_DbJfXuA4HHcKvA1Sx5CSIhYqDCK3_-Rgyt6-nUf3D2tXkAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/25488" target="_blank">📅 06:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25487">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv8eXNPDwZnyd9cVwcWY3iMaKXOrqiAPfa6ugB42c81GX_8riL8UTr2LW-euuIWnLM81BDiwa23dbCKu3PjvB1q6DD2iZ3ilSMzNLtY9qammof2DlS-K0SyC23RTRADgo0r0AivI69ihrJ2qFPwj00mwLmIPETX8fa1ybHzgvgVWA_FUH_Nej-RqBEBS4nZxY6Uh6jGTpdv5Y-zHczY2mRJFGGzFQL_ih_wv9iG-QtD5hnIuTUs41JnnbSHMqEbUnCXRiEYP1ToX-G77NT5EeRmX7Fr975WJnwNtAFuZUlqbWY_2e5LCT0v_tMBSvX2n83F5oy1OI0Y2zmebSIa0Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوست‌دختر بلینگهام: امیدوارم‌امشب انگلیس با گلزنی جودبلینگهام نروژ روشکست دهد و راهی نیمه نهایی شود. بلینگهام رو بیشتر از خودم دوست دارم. هرزمان رابطه بخواهد با کمال میل همراهی میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/25487" target="_blank">📅 06:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25486">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EcR6_mOgBqhmIbQicjw1J6gb8yD6_gpOstgH-R4PTvYY094kvb2PiMrh3Qi1zbLUxFF_E-Fssrk8PBC7fxZ3FkLy77teYRYIW8LIM_q60vhVTy49_2k29bnuwdd8ni7frxYV-iRCNrpPjT-nX9wu3192X21NnoNZdnvCcj6ikypz49azy7tTr-q7amkCDdnMrGgHL7O7k-nyz4aaLnlbq2tkmAQ-Hmjh5HJjBg0DMGckJEOu8i8BYCHFUAYso0zmt_pLmClII-bTOVePh19316-rzJciX35d8v4eyKAR_IG_mvfBgPBHUqejUqpsTLM_stajbh3VXbCxaXRa1HicCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش‌چیشد که به این روز افتادی؟
چیبگم اون شب جای‌درس‌خوندن‌نشستم‌بازی آرژانتین-سوییس دیدم.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/25486" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25485">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67aef1f61d.mp4?token=v4FSpkFmIDmJloFBBWI-DfWb1b4OiycuwJJNzWI1SH0DawPexdcXNQzapOxIl_GqwqHKGHrsbvjKu6wmdOqZe08iup7inWYfkYB7VK7ETRjV-DAhnhR6F0MExt_Jusv3ZJzvCJLpQ9Iut-vZ5ayCDjmfkmd-QuWVY_ZmWhtv1xBibAWuYpaFjmcO8lF20JI1f0_7QekNHS83pKmtHO4uHl_3QDnE0mznWs5-2JktOBoYoyDo2XiPn7T9zMZumao6BXcYv-u7tijRrdKtbPdfWMobFp6vAW2VCLE1-BY_MivBG8Oh_Es8yeLS_52z-huAUIVv78zrSqPvYoyNwVbRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
واکنش‌جالب ابوطالب‌حسینی از رابطه سرد بازیکنان تیم ملی پرتغال با کریس رونالدو در پایان دیدار مقابل اسپانیا و حذف از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/25485" target="_blank">📅 00:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25484">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSw_7ia6wdoDUhipFnvN1dGrNxu1MOJYnOfG97df1_-fYciq-KKpVtSMirLWANvpzGLmQvOhGHVd0bu05FAlEUh8lhsl4qgUlGF5QdvJzRT8OS59y6yhrFP0ryKKyLAssKBiTKF0EuGtTYaNEXsLpv5zmog6e1po9sFH5RFNCQjTNGI8PkTuRVAaGBHLl51P-MavYLrdpuxvesetdpyOd_JkhfioT863cuVGsYebf0Nzn_y2f5c-igV0mDlbEJkl4df5si5zmokNoT7d3SS7tHR3P4udBcGVtH1bX7dfliFe2DTz2fe-5bWocjm-yJSA4QMuAGcSCoVdGJWEcmg5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25484" target="_blank">📅 00:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25483">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyau-GVGPPYT5zwCd9GpQN-Wzq1AWT-pJ7f2Ypt7xqSOT8-S6nUunn_N6MgipbR_2vv0Qjdl9v-0YcZujCyglkrQIiPr7uRhtYNyY7z3Z0a-BKe00msi1svcqQjGtV1y7c42GZSENiEJsv2AX36Fgdd6K82bx956Vuk_VU9jhjRZJlz2jUmOtwwWIukMgiiJ_YIRDpECbPzbnM1WTEzhKqc5PgdKmf9lddXHATxVLhIuELYoCAp5PGsHQPv0wgbV1K3MTfFYct-0zDu0gjggDEj8nq8i6NMKIFFGVbjToAJC4IQYvlEK3p9JKh7xfUxaet36rCiuiChyY7fzPZ4zRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/25483" target="_blank">📅 00:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25482">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTMYrb5y2vmy0VPc7GxHXFkC0s5uBUENqAMif7uLEME7gkQFcYOXQ25d-gec5rfFZFhOsvTmT4FyY9S3fhZGxN38cIlfb4nyLKzD-EQbub8dPMt83z569JGoTTz96EwNJ7ypcJrhBB9ZDYScypyw1NIvfSU6AZ83W7-6yKaEd8UdkMcOCzW4mjDx-yIDF9OpXgY2fNDpvT4OFMGGU_SauANIi8bXlxAdsbexvmYWbPGSLuy4BE2DCy1ZcJU60xdL1wHxIvtoxeiirVwEeYtj01jS4Ni5NcWxaQL3K1bLvrkquYMrDjNpQ2vzMb8bliM-K-pT87wAZsAwyikUHzr5AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/25482" target="_blank">📅 00:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25481">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvgjxT3aZR030Mx6fJoAKp3iz5PIP7jedz26VjyBWINBGEiIREO4nOfzSmgBv9iD2n7FJhrIly-ZhitD3Un0KuPVIK-NKIemucz6yXSELLStqNwSENsALnlIPIHmBvj0N7fjEGW9niuTaz7sKsuROcmm8Ifvf-5z1jZl0JLnijVESFsM4wufGXdTV1l-kMLapqvqHZ1cneybmCZWsRrlI4W86bC25C0EpSueVFKT9junY18tbm5XnIyk5Qkcbf06BnYOxTbX97prXCr54idCEDCb0Fj8VVo5eSmurwaEZqA6BZPzeuY-QutJXYs__8En2IHbLVFYJ3FrMFjXsspfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ آنتونیو آدان،عارف‌غلامی،آرمین‌سهرابیان، محمد رضا آزادی چهار بازیکنی هستندکه سهراب بختیاری‌زاده به مدیریت باشگاه استقلال اعلام‌کرده درصورتیکه حتی پنجره نقل و انتقالاتی آبی‌ها باز نشود باز هم نیازی به حضور این‌ها ندارد.…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25481" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25479">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LQk1jGRnlsm-gNW9PUUQakEjOhdFUIDNISjrJgL8jAwC3qmAcKs0188ZnDJ2mlx6OZaLXLxHkijDna7YjW-4AJ2fEWQT69tVgeTIR_uw0OLXzMnACRDgxFCl9zGTPyIhz7JeBoT0ZnUGf3Yf4E-XLK30foKKFAhzfn_ux-cgkf9PxszqtU6yX9gOLrk6UFbwRa3lDUZndDY6vn9I7IdtCaMWM9IgnZIABAAH_B_CB1lsFKX2LGAkAliegH_ajBQTgFUeciQ4zgof2xn1i7iJOuywAG2brDovnr1bIsLBHtZy3dvFjOBovvIvDStxr9z4-ZhNIB39x7UfBonfsMvJXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ieh8r97hnYKrRgz43i9Hdz5hraqt66RPjK1T3fnXugxntPCAc23WDWj2gik2G9-DumbFrHbxeK0Ex82SyZMp4RKD__Qbifavwnv7UfBtuwXcjxTEFjXsgxcV9OL3nCVJD36ttENDBRQJsmSERyjij0Eq8ZsEd3Le7Q6zXHO2Ie2A2oZZsXtAfhwgwnlJXKXYB_M0XZf5xVtRikjiya84Q6hyo0AAI9kBqzigvcFUJuEcXgFCT9wGOkwtgE3fQtUQ_G5KRmRQdW-JqCF15KnejFiTHkQEHsPRS6PVNP3SMpA79lBi-IL2bUm8pHSEwxRADlMA3Yk5zQD1w234AAmwBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نشریه سان: درفاصله چند ساعت تا شروع دیدار انگلیس برابر نروژ دریک‌چهارم‌نهایی‌جام جهانی، جود بلینگهام دوس دخترش رو به اردوی تیم ملی آورده و باهاش رابطه برقرار کرده تا سرحال وارد زمین شود. توخل قبلا این اجازه رو به‌تمام‌شاگردانش داده بود و گفته بود نباید به…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25479" target="_blank">📅 23:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25478">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHZiwdDkVBa6hFMh2GkrWND4wi05SNV0YPALq9sAPRHOup6drqcKykqh23yGLwCz_RFKZNtXyi96cxEcnY4DZ6tpfwPGLy4BpOsxqa-d6X9fRHPy2J0rwGRgP_zxiytS98ofeWcW8Y2IoNMb8cKuz6P3_aJ_7I5T1GYumTY4YcFleg-WZKQRQXkSHuxM2USxw0R9diZf7N1Ia4joGmDXPhqJA9_QVrUDpRUAmQmHF5LsyoRMnzcF8_Oh_j9UAG_RDTP_hPVqwVoHJhHHZphw7lFRYE8SfxFq0c3hVhzW95Pr-R3GWynrnaVHklo6-rNZ2iN5qPg59g4ozQ3PUsnPtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق اخبار دریافتی رسانه پرشیانا؛ میلاد سرلک در حال مذاکره با باشگاه فولاد خوزستان تا درصورت توافق مالی بین طرفین به این تیم اهوازی بپیوندد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/25478" target="_blank">📅 23:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25477">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eSFibhxK1DfNTy7oeZWx_t7esT9G4V3UFHNiXApyuOXyTulG91Ud1E_kTk7_UgfLKK-mgn4QsMuDrd4iXEmzCl4tmXj2N0rISBwND2FQhCvRiAIYS1cBTX3DypU5rgxFguswNkzBVuujx7JazysQXtTeryGWEMLiYkE_iGhm-UvfHhg33_pHRHuH9OF6NkPLXY5bVL-PbRKbhPz15QhYcvn0-n4r5dZEncVzbBIN-TIm5jgBwTiZLK4f-bRRmrj78qxchAkFaGaTMW5AdN4CLv3FMM4MswYV1f0nuaBRG3eVNB0RQ0U2PBvUAJnXdwBJf-K2PKPn8icVoQ-3wvn_VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
👤
وحید امیری کاپیتان‌سابق‌تیم پرسپولیس به‌مدیریت.این‌باشگاه اعلام کرده‌که درصورت تاییدیه کادر فنی سرخ پوشان علاقمند است که یک فصل در پرسپولیس بازی کند و در پایان فصل از دنیای فوتبال خداحافظی کند و به کادر فنی سرخ ها اضافه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25477" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25476">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rac2itQruu8G_Bdos62hFBt1F3iFHTr5kCYFF2CB8AePqed3EOmnYKJ2UjnPqqkKLN7XIJsESFIZG8BGmu1tlsiwnfc0JCsaqTjlo3UL9CgPVONj7YrbDp1mjNn0XUtRLBHTKGOnetahF1hw1la7gBPXY72bGoG6EguMPX49Gq1hF-7WiAWO2cAdbZvkA5hLRs6-u5dYG-F5B3AYwiQvNoLKSCzigUHauq3Kmd7__RJvPjw4N15bA1xWQISDdG8Pi3Mm6z-igTjy6gY3m-m43Vs-vZ7uTN5a_XCWucWCx-iJofeHeb_GbB91Tea5vJ6CV89ix6N_Q4zKXBjiDsbWBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#تکمیلی؛ روبرتو مانچینی برای‌عقدقرارداد چهار ساله با تیم ملی ایتالیا با فدراسیون فوتبال این کشور به‌توافق نهایی رسید و انتظار میره به زودی پوستر رونمایی از او نیز منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25476" target="_blank">📅 22:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25475">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=A8RBY0wgcwYZZtSb52extsIBF2kq5bUBjaTEFMv9yspE39YQNs69NcuxzSvjhCRcTjlnowHmvDlFEbjqUgqLk_A4EaSgraSBArY_mJe_ClPZIyg8QuMRqbp5gHxJhk6QvOaIP3MSzumP9Jl2HCzEEcDMfLYzxcKQGGQaDh_myx2zhRMqXbY1iVsm_va-aKCU01iyX773z_4FSkzQF4inQv45t6S-C2ihIbj6qymuUEgjya8DFvarxZTYxisjtS1_Q-1jzTqCnwS4TB9SIPNrRBECGIgEkUfZydX0s5xSUrUQLu-BB_ZlZSBgL4A-1YNCj24hQTdcCzVcJzkjYbMypg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d020345f8.mp4?token=A8RBY0wgcwYZZtSb52extsIBF2kq5bUBjaTEFMv9yspE39YQNs69NcuxzSvjhCRcTjlnowHmvDlFEbjqUgqLk_A4EaSgraSBArY_mJe_ClPZIyg8QuMRqbp5gHxJhk6QvOaIP3MSzumP9Jl2HCzEEcDMfLYzxcKQGGQaDh_myx2zhRMqXbY1iVsm_va-aKCU01iyX773z_4FSkzQF4inQv45t6S-C2ihIbj6qymuUEgjya8DFvarxZTYxisjtS1_Q-1jzTqCnwS4TB9SIPNrRBECGIgEkUfZydX0s5xSUrUQLu-BB_ZlZSBgL4A-1YNCj24hQTdcCzVcJzkjYbMypg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
روزی‌فهمیدم مسی هیچوقت‌تسلیم نمیشه که بعد دعوت به این برنامه‌ازمجریای حشریش جون سالم به در برد. لعنتی‌ها ببینید چه گیری بهش داده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25475" target="_blank">📅 22:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25474">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDOUBhMRhEQiEUYEuw3-AtBwcH-K_96V551TXnipRJf6NurUO6V66VvoS1xu3fTIaQpYy0buPauNZjqmcrqtgBKX8QcUMlvZZ2yiXYnXZh5BgzEC-3o2GrooZJe9Cak9uYidk2vNX4Kn6Kus_VADk1Dh6PScuhkgiQZrNLrnqC5ZU2V0Z5XBw0bKA59VsJjZ-K7mitq1NHGJE5LIz2909ENWz0D_AFR_eZA43Xg7lAt_5gy4k6e3sTv7WOwSTOLIEIVxaut8__GedmSnxal4JOwkRNDSwipcbfumoCreT-eE8X0mkfO3Z7F-XP0A75miRIvKlnNiTcXUpGocE9cd5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط پیمان حدادی مدیر عامل سرخ‌ها درباره وضعیت علیپور و محمدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25474" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25473">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=hoqKhNRnr5jRd2YXs9sLSAFoBym3tntowWt1L2lq12mfyNiw2gtecC9jG2PjPn44ZIkz0OopYP2qkOIcj545OtuKKHzGtgKKxWil52gHD8MPtNtgzFbkEYD3kKV-mlcgVKbncNlB1XoQzmv0BtUCX_5h4W5FnrJ5EYeu4x_DWlvIXwF0PWtF6ZCa5t7fq8A5U0QmnvZzD-Tv-xlRxrpHI-rJKtySPk40NgytFy9KfkampXSww_QeLOOd-DLP0BzoxNhh1Zs4mMJMGJo9vhkgoj7GuNeBtn-ivAwqz4iyFu_de2jD4b8FGLtA_WEBvfFipaXPioiOBxjhwlPuml8vYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec99dbc8ec.mp4?token=hoqKhNRnr5jRd2YXs9sLSAFoBym3tntowWt1L2lq12mfyNiw2gtecC9jG2PjPn44ZIkz0OopYP2qkOIcj545OtuKKHzGtgKKxWil52gHD8MPtNtgzFbkEYD3kKV-mlcgVKbncNlB1XoQzmv0BtUCX_5h4W5FnrJ5EYeu4x_DWlvIXwF0PWtF6ZCa5t7fq8A5U0QmnvZzD-Tv-xlRxrpHI-rJKtySPk40NgytFy9KfkampXSww_QeLOOd-DLP0BzoxNhh1Zs4mMJMGJo9vhkgoj7GuNeBtn-ivAwqz4iyFu_de2jD4b8FGLtA_WEBvfFipaXPioiOBxjhwlPuml8vYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
صحبت‌های‌ندیم‌امیری‌بازیکن‌افغانستانی تیم ملی آلمان در رقابت های جام جهانی 2026؛ این بازیکن از دو تیم آرسنال و چلسی آفر دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25473" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25472">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeIwvvZIKDQn3HXe2KB0nyaF-JHojZz9NuJ88o9zMqM-vJpYY6TJzBCJLRTtLh2s4pQDsT_M4H3vI2Mz3BDz10KVKTuTTvXceXrPGR5wj_5wCz2lafNkDxj9u7GvlD5dRwPk2WEb69d9Z6MHPhwedJbtSWRdKsHZ7nIEDT0uJ3VMbSj9EpfCQVIWW47f6gnFjKa2Oex50i-ttKkG0sTGwbLos_o4XILV9mnszkvrEYzN4RR6y9ZUvr88x6DpwpeOLd3A4z0XMysZ18hBU2OyxmDGweg4GvCBf1LAXZEot9eRea4dhS46yhW6tm7H2VpG7hAFSNGjmEa8wK1QC-pvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
قدرت پیش‌بینی‌ات رو ثابت کن!
⚽
🔥
دو مسابقه جذاب:
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🇳🇴
نروژ
🆚
انگلستان
🏴
🎁
500 دلار فری‌بت
بین تمام کاربرانی که نتایج را به‌درستی پیش‌بینی کنند،
مطابق قوانین سایت
تقسیم می‌شود.
🤖
پیش‌بینی خودت رو از طریق ربات تلگرام ثبت کن:
👉
https://t.me/betegram_bot?start=p6_r4EF37DCE
⏳
فقط تا قبل از شروع مسابقات فرصت داری!
موفق باشی!
🍀
⚽</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25472" target="_blank">📅 22:24 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25471">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2t8uD1vQ1slxmhdwC1fgc_Xsgl9g_sCOajMhTDSrXAIifv1ySE6UhPA6MvX5gk-LiZ8b1Ry1LSu-wEqrvmTz-9iB4YRmVFu2LjwBUcDCxQj19qkcuJcLQvvkL0QSsHcYPcwXXI9PaYaU7kMkpLeov_k0HHJgvNb7mG51GUhWWAHhXnzA2JvU6wfN0NE99K29-S7P5hnySNC7H4RaLrCKnF4WEsvkthDMqfw7vq68So3aQKvsDVmJiTv-Vl0u7Y2D89yUlExtod9YFNy2wYijMjYHC4QLR5-4AVIEVSZnfuq5iwqIl49hWM6XQXY66-3zFXpPt8VO06pBCok6YN0lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
#تکمیلی؛ اگه جدول رده بندی رقابت های لیگ آزادگان همینجوری‌پیش بره؛ نساجی و مس شهر بابک مستقیم راهی لیگ‌برتر خواهند شد و تیم صنعت نفت در یک دیدار پلی‌آف به مصاف مس رفسنجانه میره و برنده اون مسابقه نیز به لیگ برتر راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25471" target="_blank">📅 22:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25470">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C91RQJHsBe5o-4_lPfQFPpBg8Vva4hYDwm2aTRcr93qJV53LdHLWbQxSx-h6FYVe6VxApfkOA8TJVYCA3ynexUJmkxh8oxWonDNuk_Vqlgq9vwpOz1DesRUwwrUWKdCGSnqDIAn2h9lKy-fdJL75zOp_wjWqs5Z2w1l2T50nqQQzSfRajVlyQk7U7PNsyCoti4CzsYMsp9EWlcpHgopMIM6vfOUmXEF9rIzwa4oCi-k3xKO0_33SFZgXfqk8kWXzl9MQUfJe5CKRSu83SfHzfJ1OdU_o7qeGpaee1iXscrGBzK0G_G7mjrBFw8ofL5rpDpyuekQxMGzlWSP6a52mMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جالبه بدونید بازی‌هایی که تو این جام به ضربات پنالتی کشیده شدن در نهایت تیمی که پنالتی دوم رو زده برده که این‌فکت هم درنوع خودش جالبه واقعا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25470" target="_blank">📅 21:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25468">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fe85cec8f.mp4?token=jAHr_vbbcRe0R-bQ9TB4D9lq-lVItaPv3X4siBRijnrvapzPJHiijROlmoB6nY6kKyX1qTTKVnzhx0DJQZAKuLTV47PSSjcmKlfGrv96sX44N6RkmbTE_P6e-vE7ZMghKiz3-skqP5gBWNlTLophcM1nPTiAedaXFRzNqQ9dDp_l-Kb1Cm2ZVa121HbfnQXBQjJP3FW1ui3c03tmfobkYdhVLdmPHrstWIFYOKxVOb5iuT3GBC96__L40qcBXUwh7am88QCps4qDecpnePNuw55G9ZDQ9otZ00sUgOy7MBIVDeSsrwgJLHaE6iBNFuePVTVdURAyjrw3EqNnzNm-KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه‌پرسپولیس که دوهفته پیش با ایجنت علی علیپور به توافق شفاهی رسیده بود حالا 72 ساعت به‌این‌مهاجم 30 ساله فرصت‌داده که برای تمدید قراردادش به ساختمان‌باشگاه برود در غیر این صورت قید او رو خواهند زد. درباره میلاد محمدی او تمام توافقات لازم رو…</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25468" target="_blank">📅 21:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25467">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3FdtNyarYvNaim0QAkpa-Bi5YXq_6ZW3OpnKTJgBoXdKMPjX0Wrx1orowB6815RmOR5L-b-bHLJlOZaHIBx9DTkDqZ5qijdCz_mUSlShV1SKS9urdpOAJmP8MMMW8hkOeE_AboDkskEXrdQwoP2JD2pYcgqsrK7dd0ME7RAr74LC4l3bIxDsfS1TXcGHudGcK0zs6BgK78sR36F1m1q7vPcw7mhHUlA0W8VB-L3CRlDsWl7PcBXJ87TgsvAVMKs_zCtQsadEwFEfyrZhi7bP-M-FKABmIAvPPGkA_VYyW3X8rTF44S7etekIT4vhljzGeX7BKlebgiex2w91xV4dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25467" target="_blank">📅 21:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25466">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIhco7KVl0Dmj-kO-xFH5pPZWHbVZFcLvUXAr5098R3XSsuJBHy5nGkhi-kaw_cE9YSDZte1-yptG-LOa367uw0S9Y8-XsEF2VlX3xloSwg_0Xt1INveKh4bVeh6A5vfDhtz-N767597CxEvFmfcIhUj0uAUisgblhtk8gTKnLTpy80pJv-sCplncvhlRtOTrIqqocvvcBJPWUgwpx8FVch4_2R5xaZrAgcEMeuyFBlLT6GdF-iHbdHC87srylIJPmUGBVgmJ_IXWwIshwig8qdOe_u0wi5BjNGLmk6TWk9mCep-_LRVwGCGNufJHlyEgmeP0eunqQJq5oOcIJSuxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق پیگیری‌های پرشیانا از ایجنت منیر الحدادی؛ خبری‌که رسانه‌های‌آفریقایی مبنی بر توافق اوبا یک‌تیم‌مراکشی منتشر کردند کذب محض است. این بازیکن اواسط هفته آینده به تهران برمیگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25466" target="_blank">📅 21:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25465">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9_kdq6oQwjluySRo-8XvHvw5SFfgyqVLMFMuS9ey6bzQWmJV-3-KiunCB2xfDqdtHF7laucEQkNxVRPDUdL7P8e5QsV68IriZCrCtfRq00liVXMb02Tl6C7GeWLZsnAbmrgMbF5uQNnKOB-UUF0jVlf-TxR724Dgs4hmc4zfcHO4M5hbii9KtwPszbXIJAMWl8rSztBdvbZyPAF61qpz4s7aWRA1t8sLJip8G6gVi6G0zngw_mGeGVITaqPMyLnILtrMQUzLrTUB-O9KnyHcXxLV63fWmHevNJ2NezFoWCt_SexwAjTJ-C1rKof2FKeETAC-kOOYcyIoMIYBRZ8og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
توماس توخل سرمربی تیم ملی انگلیس روش جالبی‌برای‌انگیزه‌دادن‌به‌بازیکنان تیمش در جام جهانی کشف‌کرده که چون یخورده 18+ عه تو کانال دوم‌راجبش‌گفتیم. حالا فهمیدم بلینگهام چرا یهو اوج گرفت. بعدجالبه بدونید 10 گل از 11 گل انگلیس در بازیای اخیر توسط هری…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25465" target="_blank">📅 20:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25464">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mL4YcqFGqTQaVvTOTwBhkZWPC0uGGlx0PUYttkgcJD802BtWl3dH9NqO9BahPOXdPdcfLAK1IEw1qAmM_uQ9RBXDSDzaSNyROtFbVoDYwHg13QeAHeVuWT2cdziVG2hEYI_V3nkFy9u3CBAbhq_Senur94gcJR9PQuXuit8qDYXPd9rTioS11-LqmCZvxNHMABG3qPGlPcaeOcggIzQCfxhXq9vp-RmOrWV5RXj6juWDnWqOsgTVP6n67h1Hmi0LYJhYagCFlm2o9Ud1bBoxlRxmkcVJbhkHGjpYF2yglieXfUmyGTn97V00eUGLsX89p-DRz0xs3rv2c9ZSUSC4mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعداز موافقت مهدی‌تارتار سرمربی جدبد تیم پرسپولیس؛کریم‌باقری بزودی‌به کادرفنی سرخپوشان اضافه خواهد شد و قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25464" target="_blank">📅 20:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25463">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi47YcMEfx9WVCWILr95XknuCeVKvQblM9aqe2g6QHL8HjhhYCzVlEDzF8ldM3FZkpZ2Q5W2TpvIkAGyUX97J4BWEelEt24UkFiOFo-UaS810fi94FYfUorq3aoANkRgwJNO5yvssW8HfYRk7NAYrAPn1t-xiOtqlxenVxm-VSK8oeyK2FHRC1y6_BqptRh-Jo1NprPel9C5kXd7Cunad4YjwD-ap5g3JzUpOS1rTvfc6C2wyWUawpnLZls38MS4GRV0Hku_n1bD1_HEF0C9SSV7a9f-AWkZMzxoaSR2gyajLxsONiurp3gI62fVWffzmMgQ14s0T9QKUOU23WrbBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌اخباردریافتی‌رسانه پرشیانا؛ امیر هوشنگ سعادتی ایجنت معروف فوتبال ایران با مالک باشگاه تراکتور آشتی کرد و در اولین اقدام قصد داره هادی حبیبی نژاد که روز گذشته در باشگاه سپاهان جلسه داشت و توافق نیز حاصل شد رو به تبریز ببره. اگه این اتفاق رسما بیفته یکی…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25463" target="_blank">📅 20:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25462">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMM4A8ONKAoDMD5h0WqBO7xjFCUSPehl6L3gR_bUSKbEmuGV-whIsCN-Q4Ya_q7wFc9iLjDzyATefskcUiu91_t3RIzi3RpxaoQjWLDH-p2aC09AXN3cxQKidsqlM7x3hk6r5qNljdVmJ7KmyqqVNfZNA82Wg_Kmo3mdQEjgeGmB8EKusNxUWyTTheikmxheaHXCLx8tPgoe7glIooyRGqD8SDLINc9TAoXr-hcqXBxD3vcL6SebgIKsJZu7cIPbdXrTyw8kLSGyk-P2tSrQLKuwDKlTB5y8NY3drHcju-3l_kuEjpLA54e-eAnc4xrOLssztf3YXbyJefYTKaXsHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25462" target="_blank">📅 20:21 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25460">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BroDk_LRpNNxwiF6vyDnzf8Iw82G5FD4H5VAQBWpThPfKWKAa825s6AVqFHoFgohbJOm5WWs_RRjYQHAxr_Xwg4CZjpNBpNdllVZtdb9DH1GraFz1DiIdkoX5pxC8PffjLt0OQM8BIfZANjoHnkUgWTvgYPNdTF6MCcm6_pHyKizrt8nYYd3aCp547fNFJfP4JfVwSz2huRRI3oGHcCtdyR79FFkGaWrQXcAfkZZebGxc9OQrduC2zftziJ0Zc3dAcxGHK5ZPGUa-YQSqrAVCM56CXymwKUe10O0Z_gJelgpSSnCn8giCHiOzZ7F4m6tFNOBBd3_S4O26UinlJ1IYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25460" target="_blank">📅 19:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25459">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxjXcRbaGBuAcA4C4Dgf7wHAbomN3MN8uIeH27Co7j1agxLykCOI_m2INOeKSsdDx3jJ70ev4tJoo7Lsuy2AbcK7F562JZ9P69tGvUjpOjI0lPRpmDsG4ewS3dHAuIwVw9jMfM5RrZMgMMFs-chQH25eD0UV4M4aJRGcRfnsJajo6qdVj4xh3_fToGsEBhS0BNOdwV1wLHNZOc7Ut819pue5Td6LNswwp47V5rCAIQ0iIKr7o27UhfgsEODomN3loZchTvHc1ROrg3o6ABxBdSkxgLIU7BovYRFY9_3G2F9ALqAWJEF6shUxhpbhs6EJ7bk62PqmB2d33WAYQvj2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تقویم
؛ 12سال‌پیش‌درچنین‌روزی؛
بارسلونا با پرداخت تنها75میلیون‌یورو لوییز سوارز فوق ستاره خط حمله لیورپول رو بخدمت گرفت. آمار سوارز در بارسا: 283 بازی، 195 گل‌زده،113پاس‌گل، 13 جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25459" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25458">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25458" target="_blank">📅 19:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25457">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=lroPmLAoWXG13MTImIATpAguhD5i4Tn3XUfSLna-phbo8e3lSBekRlHmO5ivEz_cF6WWIfp4GTi2QTK48Ba3LS1tPVrl-ZuCedFvwrs-BnU_D7Gpv74sp5aKfKTCzA0U3LBbfaASa_61yQZ2FoDFXDlLG0WeSkeFla0CojCRNIB3SIh_LuEn9prWZ2u7D7EwDwLKTNSFn4wd63wnb1IinBUeKqTdGhUzsM1d3v0pwxO1yf608xKvkK_USnmlHd5REvYzMmXmQpT9dwI9xW0c4K2HnDFPUyemTWG2pDAz1kWpCxCHc97YmbMjNNVcq3uyiJMXjIVzjhhls10r1BmHtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e046936a8.mp4?token=lroPmLAoWXG13MTImIATpAguhD5i4Tn3XUfSLna-phbo8e3lSBekRlHmO5ivEz_cF6WWIfp4GTi2QTK48Ba3LS1tPVrl-ZuCedFvwrs-BnU_D7Gpv74sp5aKfKTCzA0U3LBbfaASa_61yQZ2FoDFXDlLG0WeSkeFla0CojCRNIB3SIh_LuEn9prWZ2u7D7EwDwLKTNSFn4wd63wnb1IinBUeKqTdGhUzsM1d3v0pwxO1yf608xKvkK_USnmlHd5REvYzMmXmQpT9dwI9xW0c4K2HnDFPUyemTWG2pDAz1kWpCxCHc97YmbMjNNVcq3uyiJMXjIVzjhhls10r1BmHtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لقب جالب لوکاکو از زبان فیروز کریمی؛
جالبه بدونید که برای ایشان به‌خاطر شرکت تو برنامه جام جهانی شبکه جم‌ تی‌وی پرونده قضایی تشکیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/25457" target="_blank">📅 19:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25456">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4aL4KftYmYd6TG0jz8fAczn6NBZqIGX-bUp9F0VUY3edDyp_aLsAj1xzMWb8hKNcd8IU5pomysSAB1zOXkPzqhg2la-lx76UcWhHglIwUhQV7QvipxugiO59k5K_YOgc_0OSpfFfRjYLPeQgAh3seXXQuLV4bVDwcu7lrLYUDuPT8RaXffEzdrEyRk67l58KBidrVbUdp56jWqWN94r8fd39NKt-IF7vJSPjJDos8FY0sn123mGpzWE6iU4St2jwIRGGh0WIicGrpkzSK1jwsfg9xlVRb1hLk3E5yDYCd-w_o8KyVjZADJJZn8LzdCS-Ev-vrxK1i-VRktGnvbF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25456" target="_blank">📅 19:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25455">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5h91ST3pc43bTWcKDJsgLS27kmTi9wbngZMRpE6P7u_72KfrVY7WjsfJL_CKGop4KmnIP6d3LGMNxUI3tsQZESmWnD5KnRXITCfRjq0Md_0IXHMRvMo3TSmA_8C86DmjZDALWsiybAUavRpWFe3NV2gMBy31Pzfdlw5sHq9k5Pvopg21FV2lfkJdi5Ao42BZjkS5Nb770_uvsID7b0o3fVXpw-SnoTIxKsii65d1gAYKLrNRM438chn9XzfnSfWYJ2tSgAoYD8JR9AtSNpHeCDmFeQ3KdRN5a-zD7r6okrajGx2F5CnuYYXRktgXH6v4r3jwx9AluWfbyWyHa4Y1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
کریم بنزما اسطوره رئال مادرید: به کیلیان امباپه گفتم الان‌بهترین‌زمان‌ممکن برای انتقام گرفتن ازاسپانیاست. به‌هیچ‌عنوان نباید این فرصت طلایی رو از دست داد. اسپانیا برتر  از فرانسه نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/25455" target="_blank">📅 18:27 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25454">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‼️
خاطره فیروز کریمی از حموم عمومی در برنامه دیشب ویژه برنامه جام جهانی شبکه جم اسپورت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25454" target="_blank">📅 18:01 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25453">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8mIg9gVQCTw6PbB3YmdiLcNRiEd-hpUt3KqcnYlVlJpV6aGLxPulRF4SRG8aGw2gStHbxcC76VphCxGg7seFs0wJyul1Cannq_9u2tP2L1BU1lcBnHtkw_AANtD1oJHPUp3HNQn6NWGtbib5ckODP4oZzJXAvz6EFGm4NFwf3_FKJ4FnpvjcIdHvfdJCk1f13DLBlHD1njgU0BL2uIXPSAuDAxevtHPA68gEdzuhkKTPMWpJfkTpYq-roXznYLMmZooaL1sl0quL_LXFuCPcbTNgmTVas3AWA3OkCCOEvgu_KtPZ5CQSx_0s9UyoqNYOgWcDWSuGaQTrw_LwFlaBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال به مدیربرنامه های یاسر آسانی اطلاع داده قصد داره که قبل از شروع فصل جدید لیگ قرارداد ستاره 30 ساله آبی‌ها رو تا سال 2030 تمدید کنه.
❌
آسانی آمادگی خود را برای انجام مذاکرات برای تمدید قرارداد بلند مدت خود به ایجنتش…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25453" target="_blank">📅 17:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25452">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upV1-GovYcUxAsA-MqOnI6ICDWgsDHaNhH_HO3l_kGwOqVSgmF80vxP7kEvqfw9Jpe3a3abtuS3_JB7HlwW6cMyvq_UQHcodihnQx8pF-TZVKVbapAW8kvzLYoieCQ5cT9aKywhw6DyF79SOpDbGkQtBnxAFpr8nVDMKUtt22l-JynjuwglJoAK0DCSPgG0F6sS7999zlh9AMOgF9VCE24UFh1zghV4HktdNVRBKumT9ZmJX6hk52LaCz8e-2uGvGElpsPIEc_nO0z_PmJ5lxt7SnsBa4QW1F3D13PfrE6GJpb2lxHN2fCoBd6JTZ_QCWFk0RQaThUcY7yU7VWafRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25452" target="_blank">📅 17:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25451">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zzhdk8VNqLtMwY65DarwxXSPstJTJ0jAoT4Jmb65jS312RZO-8x6uHCTwcERB3-SNL8Mn-H65rAXuQmacuDtDL8VA1Q953P4OzWjWq-KHg8fqE7eaVkRRRS44ew7V2qtp1WOskzco4RGZIoCD9MsCYN9uwKW8HbxtJvxFMurKm8Ed3_Hex523rBpY25DA2-E6PJEvu4E3xONCK1yB9hDYw0VyQIbZt6s35p3mU7ATMVDyDEDXXL7f_vXXjkXtD4J0nX4yS3YR0__dPM6gXAUed5NS6eZoVTPrApj2vf1jZ3v-6_8-VqXUbJhYVOIOj8HG6Ly-rquwAXU-fWn5M5siQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
علیرضا بیرانوند دروازه‌بان ملی پوش تراکتور: اگر در تیم پرسپولیس میماندم شک نداشتم یه روزی مدیریت با من هم مثل وحید امیری رفتار می‌کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25451" target="_blank">📅 17:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25450">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROOItZ8VNtR9-cyqZjhwjf6RW_hN5Pw3DPWmgMykZLaoyrLgCOJhWsP39dY6b2tEQobJxoJiAFrlcsO4nxm5MBUJe5Xy5D3v-WZQ7IX_UDiB4_T0rpEbZMZSsu_E30_GaZV23OlOVpHacSiOVkAsBzgkkbZVt7dlG0VnE_QJqQTe5cBT_lGtqZBBQUNjM_xodm94SiXtEzwB2DrNfOjIG-hppu06zit7X-TlO6m_b-1nFXO5FuFRay3fXhTXnSAXrIFsCTN-SHKwmFhUE6q7CeOC-0O3SzM2nFWnsc7Ie4Dq39Tsu4_zjhDpL9O051fdPK-2K7Fq0CYs6VwFk6CBkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25450" target="_blank">📅 17:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25449">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1I0Pqww0Hm0PhXTRE1fPOP7aZYvYT5dt9eW1fp40-wnZ56RMwpNayRSdQDDeUcpkYJIuWKHHFg6UwA0dnUYwzbpNIWLgQXRXh79i4LzJXn9rA252F_SG4J3M6dVvrb9XdAB_vyzOQo7napvKr7Ze7Iir02Zd0vkUlbj5MbeCmq0c2mpahzYPEF28Mb8QkH0T6XmRQr-ZFtiYmckEDVJA4odqtcK4SfHjmTNhPsY9jpmL-vWsW04oCXnbFuYc79kZNPkDBptHy9GWx9MTuxklx8ZUe1Sa5w18Bg6mPZTxqxQ1szA0N2TpDdJ6qjI79dgiFxGhJXXUvhn-ye484LYPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال
؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/persiana_Soccer/25449" target="_blank">📅 16:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25448">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqLkfvZ24CUCWnOW_2HmPpmXWh8fba5NH8y-Qdwg2OqDjcVVHzOwkss0yOqhlPEUxOw1n5an9P7qPlInYa_neoXPlUPjgE-L4G0QqsWVgdCytB7AfY9IbOtlvGgKwYkbefNNt7nUg8SB41Un6y5NT_rxGDnnJI5GHuYeYd5l-wn6WzXY8O-hnoPiAuQp9ofPrXTkC0cDs-2BWUxwYpg45bT_2XJPwWJ_DHiT7V66cUdn3iOB954QM2eH2ZFq5fVhbx3OFqR2q1rvt8exHMAXmpZeD523cPqMqCSfSp02O4vA-V9Y6KqQ5v9nH_zPF_2yNAa4Z3HqDLjHxs54jPa62Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#اختصاصی‌پرشیانا
#فوری
؛ باشگاه گل‌ گهر بدرخواست سیدمهدی‌رحمتی خواستار جذب ضرغام سعداوی مدافع‌میانی 20 ساله تیم استقلال شد که با مخالفت کادرفنی آبی پوشان این انتقال انجام نشد؛ بختیاری‌زاده به سعداوی گفته به.سبک بازیش اعتقاد داره و در فصل جدید بیشتر بهش بازی خواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/25448" target="_blank">📅 16:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25447">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6mqtNOra06Uto_MAKzyCGtrfbw5p-l0DOFTnLhzK8ndrgrR6Tw9Vfmi3CaIEoeA_UtYkhZ2b6xnfHL2UVmj5dEPIEWiOahiUbLJX2DZuzvYagbfR6yaOnFzlmPfb1pzqfpzRtp8dyVK_IUBKKr_RK4IGC3cl_SwN20QZ5mdZ4kWcAm5QPsDqDvYgZqOLzYqhbuy3rUoQHqKf37hngKgW5V4KmvNWD0GegxfvMfVbF8UTrnwu2K51vBRGFGPIZjaNQBDm-BQs61EDYRgR5ZaX2yufN8wKSV_PpmO1NfjhRJqwwK9d0uNQjj3sv2yx1gnmdTyTDE0SQ2Ffw9RvQI-rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25447" target="_blank">📅 16:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25446">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C55c3IF2RDhkV1PUQ8s5jzt-1XyXnGyVXBTSu1EU5jXi0nc0d4pZsmzh50oilBMlh147tLpwjRVjbjLm6kmG2EHxTFNHou7d078zkNU87rsyUVCsW0Z6bHGQT6NreKO8d0W9qXyCDmoa0FWdfUCsE5U0Y6_KV0FcFOgsPevSUANbv6pK7NIenS8ja9MO4SyXOXfFKeOs5mbuSHQfpymfkyZddQ11-0us_VkOE5ik3qOCfaYokTTY9QZTH47AMtdewKdm5MRKMUEFD2LbRtZ31FfqoUu-VBEYst-lwagPzsFOfnuxil8AcavGykz-e-bBfPFLdkek0brUO6vyU5DkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛ باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/25446" target="_blank">📅 16:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25445">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEpXa5bUlCCb4nbfx567_Zf-QLZprLOtMmkqpY79XqIhAnPpGzbSjbp7RONN_YKsjwpWUmetKiPrtedE39UgwPxNb-mUdCmRTPox7sRZUxEB-lCh4muwdyjZesphi-Tp2siXyElaqLtSN3HltQwu9FOnyLSgTYjdajcYjMSMyE6U26iHKZXnN7q-LeCTdb08m3PfJgR4mNYh7KT1F-4XebPcBxCjGlfjcQJVwitw-MR7JfpYlqNJNZkgG6u7yO46V29ZhxV7oY8R2o7Fu3kt1hsQHyIApZabg6KTQyPV6jLKP2IIFsBEiINgCqbCVpC487f87bE4rq2MgBpkQ3jjSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های پرشیانا؛ باشگاه الشمال با ارسال ایمیلی به باشگاه پرسپولیس خواستار جذب اوستون اورونوف ستاره 25 ساله ملی پوش سرخپوشان شد. این تیم قطری اعلام کرده حاضر است تا 3.5 میلیون دلار برای‌جذب اورونوف به‌پرسپولیس پرداخت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/persiana_Soccer/25445" target="_blank">📅 16:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25444">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bY914PJcVrJjxl7sk2HAaRDrRx6SJrG1Tql790bLFzuDIlMIX5VQ-fM6WQdR63AR_eO5hKmPVLD_ts3jtGSzxtq17c-RR5Z6XZjx929M75MLBb8j5xzvtxwrF8SE6StxlxzTp9B34T4LN2SueVojYlQIeZz3nngccNYYgNZsCKaMWPeo4408j2AKkXFEk8ySHnXNl3St003UXgDupfB496Lrj2sEWO-1_LMCIMtycGH8GgqpgoyTjILGgbvIQuYrVhEvR6c5fIUNuxVMmzg3zdnsuvpK8IAA_P8YdX8SeMLYn9KfQIhCag-isc_jcAjEg1kM0VNFS5zfTQzE1jKQBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/persiana_Soccer/25444" target="_blank">📅 16:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25443">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfjwE-N2RZcX-bgtvj58yiNFD_GkHsoUYu-cQipPlKGPAROeM-W1pu3YwBPaS--rXkcZXNdvKUN1GDu2u0jXlK5J6lhTXEo-lI6sAsCPsu0YMhzQ_1XEaq3wzNjn7UnsHjOC0ZCWiMCbz4MlB20at7yOjJLhBlpIo88JaUMva4MKHtA9WGpCcBt3Ho18a4ge7Nd_x-jWCsBz8lAfwrweD4mwzqvX3LP1ue3xoTusLVZODaSoEk3PpGfrNENvRoBOofR8MbmSEJmJtSQJJhWLijlC8Fbp8jVFnukaA9UD6b-76s2392p5G6gEn3QwR8uZkEoe8wLxA2MR7BKVdBAoKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ کسری طاهری و نماینده‌اش‌به‌باشگاه پرسپولیس قول داده‌اند که ظرف72ساعت آینده برای‌انجام مذاکرات نهایی و عقد قرارداد راهی ساختمان باشگاه شوند.
🔴
مدیریت‌پرسپولیس‌نیز قراره بزودی مبلغ رضایت نامه طاهری رو به روبین کازان روسیه…</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/persiana_Soccer/25443" target="_blank">📅 16:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25442">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRmV-qr3v6KpaQ6xikZ5plGSKl_DPayBaYemdJYr_A2a25g2L4gAl3NGR5oxzSKJHrDt0MXxlobjVb2n1ecFf-RhgkFbvR52JYxBz3KBFBUMOS6DaL0nmJ2NAzuAK4xJ_NvRNAXEoSVN5rC2u5SyE7CyVx_9VzeAyT7PhAnEER_oWYpr69lsYbQ5ZFOu1xvhWjglwxXa6Q7OGAE76u6ekOxEpVzrAzgS6Kq_8nx3ZoBf1VOmOULUI51fC6agWW-7Lz6fdIx0vyIizZ7IWD8PYD_hV_7HRTt-mBuNB7e7x8ODdONDGwOFU3xhIImsxBOKInjWXf8OJWXLj4s8h-kNIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛
رضا شکاری بعد از دوجلسه تمرین با تیم پرسپولیس در لیست مازاد مهدی تارتار قرار گرفت و به مدیریت باشگاه اعلام کرده قرارداد این بازیکن رو فسخ کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/persiana_Soccer/25442" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25441">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8ad7a6bb4.mp4?token=KVCQxjLXR-tT5V1hHcag3dNri6BJ5LLH--Y8kr9iUnq_ydjoXhWUfoWjlSUQnmxck85dZGLzNzorlLu5jRLDngU8nsOHbEwOP0YPvr7tUAF8vJn1cwMjfvIQP6rWQoaW9qcfeLwhmp0Wwk0HJABBWBax_-PovEMxh8wet8Z70DAFMwrDQ7vi3oEzWDqbs7ErhqI47IsiUR4wHAzlcoeHhDifE4NV5cKjBW_8ejkiXfPf_mgziF9MU1kXpt-VpsMTqWwNRacGl542lZ0WGqHVMSSY-AmeTheWA-9l6mjCmQVO0w0bf-ESKsXaLN1eqsnot7PvZQU2WnmJHu0fqdj1yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
خواسته‌تموم‌پسرای‌فوتبالی؛ روزی‌بخوان ازدواج کنند و بچه‌داربشن، بچشون‌حتماباید اینجوری باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25441" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25440">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NUab6Ik6aRm0yJytAGSL6i2oELL2h3-9v16Lx120ZAYPvCF6yUmw30VLRpwE3KIF3c_uJuDL7W12FOloZzNNr_X1M9BXvSGLRrJ3Sn8t2e54riR9CnZiiYYS1vH-OWTgKt2FSrHyeLd7Y72SlYWuFD4eSeRuyysEi1PmSvR3zFNSfrz2V_QwVGqvU6OI5iRT2uT4Mtq5O1wnp0QwtwWTFV3nti69hvt36sF929wxlRpXi9gT0v-HMEE01o64yYnentPiq2vtOgTuI2J_tZDvF-O5MO5y2P3uqzLDl-iBhDCSp7M5viD-Atb26igv6Pqy9zWE_BaA2HtRiV5P0bNpoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/25440" target="_blank">📅 15:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25439">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLUnNuJoGURChpClKN_HIMfed74KEyUidG9POEbW9BA_VIrscEYckxHj8o5cdZPOeCzPBLo3MhzOy4vYdR1SZJ9cZkSJISKeoYW0RN1_TX35WOUu3kmJq_0Xu11vKUdL0lJBRtlv0QfNo59LXx5BeAqWry8vsFQfsMlK_F45I23h9AH9AvLQiAJ6r9LcjgWJdhzzPw6-QwoHAnxQA9rRiuqwbNuq20jaALiwpCIkRplfYGkAptRdB8wAgzc5pTpZT8WudrpQmoQl1uklgvfUB9vQrSvEOzHr5KT2IUlqppWZW4FExXDNEri8Gi6Xlqien4GMi6fPfi3INXibHXDv5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
گردنبند جالب‌ دوس‌دختر لامین‌یامال ستاره اسپانیایی بارسلونا که اسم او و شماره پیراهن‌ های این ستاره از ابتدا تاکنون هک شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/25439" target="_blank">📅 15:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25438">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CO5A18j8rfADBa1BWT3A5ZmXYJoxomH6aZ_pOAqSLZgX3iN6hT3XhhsqItMuNTcHLMItPKU3EPfxuPPXkzhX8n5hk4pMNiigJfRtkleuVD2Nm2T-P82Yo4dOJiWmMFq2LBJsFs5mc4leE4divEsMGH09Nwb-_VvmUUSDmXHAwfBf5ema77XUJmkSW8O63kFpBvEBoDfTIcTkdA1ejpMKNg2d1ACubR8bSqwtmV7GDFf4XVfR1ydPLIR2f5hGd8gisAqdaq0NZRNzt1fbna2vdVz49KMWCP46L6SihKzNF3l3DIswrMr9k-7FJGup0D4OofPW4qPVULpJPsT0uHi3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌هوادارمکزیکی درصفحه‌اش افشاکرد در شب بازی پرتغال
🆚
اسپانیا؛ یکی از ستاره‌های پرتغال که درلیگ جزیزه بازی میکنه بهش پیشنهاد رابطه داده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/25438" target="_blank">📅 15:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25437">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqv-dzezk_tWIvNsCXuYRG0l_-4dhCCJ9BRyp87X7kBerVufOLtGca21b-pODdWy1ESwCRtczM2AuaErP2OawEg2o4WQMuOT2kgJrhXjdQEh0wQiT9FKKSDvjMzIXtubGGGs4l6C-HbDnInJHt6VFsbIV9bIVL9LKzRXEy7f4obfIsPbHL_SeM1VclBbYPxvk0oFJao9se0WSHf_19Kl51zpwg9UnBZNPePUedzWXhMUz-T8QxPL8RTm6h3Md968zGYt59B19eIox7mi5HxuBQeXpDVFz-LCTcrPru40ZenWIEYKUfMwdWP0pwlBXuKaSPWampl4XjWEgRp16cAXbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
نشریه موندو
: باشگاه الهلال عربستان آماده ست که‌برای‌جذب رافینیا دیاز پیشنهادی 80 میلیون یورویی به بارسلونا بدهد و دستمزد فعلی رافینیا در بارسلونا رو در الهلال چهار برابر افزایش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/25437" target="_blank">📅 15:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25435">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f54inTBcv-DE2RVAjlawduCK_L-flEQEdRbsJvNlzKTiy_nzwIIoejf5uyDC8kyTyWzTFV1f_sj_3EABsnTmK5EOJgfQAxtwoORI07B8IjdyXktvmW6RKT0-g2YRtfzbcmcuL6r7o7lGNYyOq1kwQN_eoWhc7KvJVDCPOg9awUvHkJFyawV8c_S7p7W-rz9g-AWq9JXbepLomGTm-u42XKEYn8ocxLBM-3Lx7eMrQeE3wbrgmujCkV55AHdaB9xt3ADESVH8ZjTeknmxpoG_GKDaBGyFJNDL2JV7jKDKZdCsPjSbIy99rzfCNiotMLE4gjIKVxMt2gd1nQmUeq6Tpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pKtWNnzkUA_TFJL2IWgA3xqs1rcoNMpZ1a-Wku4GYHQaJ7DPJJzTXlG8rCGkkNvuEBEOJ9YoQLFnWIVHspOz-02fj2BCbGMnB7wVOrK-qEfJJ_2g9WTUIz1TBLWhdSSCpYttYE2cmQlJztisHMGjIyraDpuvK40Aw_MzYgQ_F5qn-j9osEt8_3CzNVdzWqXmZWaSNq03r7rA5DO8nfnOQmEey4bP9dR0iYtF5Q4FPWBgrKR4zRjPe6YGyABNMl1p0Nop11C8SvuVFB0E6RAwlYsO0Nro2MrZbzRfQElNVOk5O3OLSh-VlzLFIt-1JNvm5929GbYv0Co-pUczZ52lKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇪🇸
جالبه بدونید دوست دختر لامین یامال قبل شروع بازی امشب گفته‌بودکه اسپانیا دو بر یک تیم بلژیک رو میبره و راهی‌نیمه‌نهایی جام جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25435" target="_blank">📅 14:56 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25434">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=rxTa_S4Sm5fKYS62RCZHFZjphdQDZxSDfzcIxkFqmrpb9zi86EjZScVBlUIygQ7TrknDu2c2wfujaN5GllPl_odx6P3DpO0o1b5mwtWzO04dk_fIpY2U5AzCclq1zg9khsyB7HBr_BuEL8isoyhONyBu3m-IPUaO-6rMIueOeJgfz2zNABz0uBInucWYGCfZWqGgVIS30MUEMene8cAqpo1r_19-7zy4dwbjdu6HfoUfGZ2ELkklykmJyesepNsdXkcY7CGEGoFZmFcIl9LoiRG8EqHAtWDOH1neSABVh4lTJvgC-NZVVLsfkRml3rbjZT8Xuk0Fej66bgIvd1i2kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56676ff59b.mp4?token=rxTa_S4Sm5fKYS62RCZHFZjphdQDZxSDfzcIxkFqmrpb9zi86EjZScVBlUIygQ7TrknDu2c2wfujaN5GllPl_odx6P3DpO0o1b5mwtWzO04dk_fIpY2U5AzCclq1zg9khsyB7HBr_BuEL8isoyhONyBu3m-IPUaO-6rMIueOeJgfz2zNABz0uBInucWYGCfZWqGgVIS30MUEMene8cAqpo1r_19-7zy4dwbjdu6HfoUfGZ2ELkklykmJyesepNsdXkcY7CGEGoFZmFcIl9LoiRG8EqHAtWDOH1neSABVh4lTJvgC-NZVVLsfkRml3rbjZT8Xuk0Fej66bgIvd1i2kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
آندرس اسکوبار مدافع سابق‌تیم‌ملی کلمبیا بعد از این گل به‌خودی که درجام‌جهانی 1994 به خودشون زد توسط افراد ناشناس به ضرب 12 گلوله کشته شد و پس از 32 از این حادثه بسیار تلخ، قاتل وی در یک رستوران هدف‌گلوله قرارگرفت و براحتی کشته شد.
🔵
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25434" target="_blank">📅 14:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25433">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0-rD24HYCRaUQ0jMGs2jDzRYH2E3QndCADVwUvYvm-vx3Eoqou2w44ycTX-aqeZcTxgnL2m_6Qu_XjHXvpt_D5lfsn3JsAjt3w_QU_2I7UY5hwvBpnVvcgEEMs89VuOibVx68gunNdYVzkEXYPYCZQKO-1UMxYu1hgCvppCTYTYwEd94dTSyawxFnJVv6pY9TzHDGIcdF7RoLBBhZ48Bnd0SXfLbnu9UunrtkrYo1zNUH3tJiBrZDtnctbMUri3bEK1DN4OXi19ff7dfchHY09q6HSNKbrJu3dKA0OG4lIawA2XUIavFnVIU8UscrSYpACVGF3ZB1hzbZNvAgjp_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
امید عالیشاه کاپیتان پرسپولیس ظرف 24 ساعت آینده با حضور در ساختمان باشگاه و دریافت 50میلیاردتومان‌قراردادش رو رسمافسخ خواهد کرد وبعد از سال‌ها حضور در این تیم جدا خواهد شد.
🟡
🟠
گفتنی‌ست‌دو‌باشگاه‌فولادخوزستان و سپاهان اصفهان در روزهای‌اخیرمذاکرانی‌با عالیشاه…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25433" target="_blank">📅 14:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25431">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDQDYFbNPWUDf1ucEvqTkM79SSHNOvp14RyBwrJi2OrTX7KwXWy9Jsoc4nhODyuyX9pPxIAz-JUr-6_GONAh6N1Ag8ElxF0wchl3ltyvwz80qYBu2ZFVUH7hASVIpyxTImZkrJHj6Q_jsJl2vqbz2w9d6AOW1QcC4kuxm1j4PtJjhYRMWanAnJaRGIx51z9rlavQNVpavCnjd4WTD2rIX2ppLhlcQsyfIsq_LrEG6_V_eIujOCKZJDboSu3tKN33dJlYpN4YfRajZnwue9MYYA25ZkWbAU8BoQAQVy0SK5Zr1HSFgI5LO0oEOSpstNINV4iJjFp9gT8clfmBSvmcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/25431" target="_blank">📅 14:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25430">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdGiSAUH8trRjwyu5Y5LmgKuClXCqKSYoqddiujCHtbv-7jWzVNOVVH60dockgHvI9s7qxnNpmMtYmpxrbqZAtj4cueRwSP1BWXRz1YQYiyicERab52_6nyUN6IGQOoqyuDJN_u2IiIta5wNO_RTAxnQNba8xR1xmouihFPLayzdO-umX5H78Eg2A8q4pLHGYUumkDTkVTPPDnbHB5laX_3-WOSn_wDzU_9CdUSgzsKIR8kNBik4ROqS1GrWn9DoqOG31bGEye3WnuM_b6sBYW2rIXMaa4HMPmL_yU9bB0Js64kFUyeOFbTpenV5GY29kp45S6bfyKHIsJkurVwiEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛مدیرعامل باشگاه پرسپولیس قصد داره که ظرف روزهای آینده با امید عالیشاه کاپیتان 34 ساله سرخ پوشان جلسه برگزار کنه تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25430" target="_blank">📅 13:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25429">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2ZOhL6YYT_x2W29GDaRMtO4l3uBDKCPRzX4f20JCp7gfKVwmwosEsikd-ll1xHNEA3dPkFX0l5qA9e8vFsroF7e9tQ7cKjf-SCB1D4h2EGmQioR6g8_m7OonK5w8JUj2TpWC5bfvvGkRY2fkE3BG_STFxg1WlUJU3oZVRwD7BH-WIuJ8x0hDS3xbRMhIJ2UeP8DT69DOr0A-RG96LngPFAXO1M_9ku6T9KR-6i2CYRcvTUBxkm66iICetF58hAp47YECeRNrnpe5DXT6IHvLqxwaygA4Mk6PSXBfdYZUl51ilz7MUkcOpy3Ys8v_uuXlVxrPQbo8ONo9mNkWCOCGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال بعد از محمد خلیفه؛با بهرام گودرزی مدافع‌ چپ 20 ساله باشگاه آلومینیوم‌اراک برای عقد قراردادی چهار ساله به توافق کامل رسیده و بعد از باز شدن پنجره نقل و انتقالات آبی‌ها بلافاصله از او رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25429" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25428">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XC9_4IN4VMp6-CDtoCyTSqGJgNsApjL6ZoctTopmjmXX2b0KQHPSOUG_czf695eBSPQlHUV4_GGCFxv_gWC69pqu8ikivm4p9CccRjTHIz1Zwcuzd1Q2G1Tttf9Ba-aX-kCWtF4ITpd4dJcHMM4lspW1ZOCqUSx0ROpCrnytVDbmEcAs5qQRVpR1237uI6E1YeHU_7bMoQUYk8I5WieabHuV5sQiXtKDktXb60sngGPYB86A4aaSGMXPqtxcjYDnlRCvERHd5dSiP3b0aXgXR6lkVfz605895meU5p3CzXJRtw5Gq-OH6rfMO8gVRNw2ILV7rfHTmp9RkV_vgcjzzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25428" target="_blank">📅 13:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25427">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5HiM7h7CWVqlLJzweLp3bhyzFrXupPc7EONvkglpvibwLIoHPeX6M69G3b71G3ktSWXhVpnyylBvXCclZHFZKIMaG51kDpWYWCvpIMAgitvdgJmBvsCcSU9rTAhAuSG0YukDc097ePFjRnCGG__DXip67hPCPELcLoVo3QkK7DRfWwraq3FaOrX566oVypByJd9hP8PgA6r4Q_eWMJ8UxarwEzy35NIdDQaqo6MKFzPfBHASutTNafnqXrsRs0zC8cRWiAGvZfP5ssJDQQTP_94f7TMgia_91rRB-gy7BNslCzEuJbW_paMa8oBHZ5phDg5WVBGnF0uvuoS4bzDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌ شنیده‌ های‌ رسانه‌ پرشیانا؛
باشگاه گل گهر بدرخواست سید مهدی رحمتی با مجتبی فخریان وینگرجوان پرسپولیس وارد مذاکره‌شده تا درصورت توافق نهایی این بازیکن راهی سیرجان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25427" target="_blank">📅 12:33 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25426">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kGHx9k4cdf7DOZfHAX4jRdOtj2NnhRK2Mv0lE9WV7xGR-G3txk6SEmna0EjwA2XBRJpk49-Y4Z02mV_Cb37MBk35rVorgMQ3LG2NhiybECteKMdER_TVPEu3FNazw2mDusognDj2BJJ5rQeE5gdGxnamPGKX5GkcHluyofqyjikgHX2AszgMnNqjOKPyl8qgOVlqYHcG8Elgd5JrDyss9ZRyd4eD6w08voBRMFoaWRhV5E4igQO-yacM6nbiAu_Sl1bjp7ZJULQIL1BSvZMU7XB2MXaZQTY7w2i7IH4a3-EWtkFzMLQQgmx1BjdR4Qqz_gJE_RclfUcMRlghIFU1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25426" target="_blank">📅 12:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25425">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06676f902.mp4?token=iEFu1aPzs5PK5tdfyKQM7aVqgK3KVuxbNwfJEsc5lhUCbxN_MHrTPy6-4ivIqc5r9sdw7rtJk5eaBWBSvGQ-m2-IeVTr7x2tCrQGRqkTnCjirgWBzkh-Ko7wnssZi_aMGpr6BTATnZ6X2W1esPGVSZUtiKFVFFdWQLpErDL20ERfSayhdr-yvsEfjyRqlomszCqDxT8FWSxrfsNUjqhxlArl4N62vvDVEmcMdJBmykjKbRBuW-ZOQOS4dtaT5JqJlIrbWbN6XUiregPFpjX0lXhP-fHteXpq0XZtUnPK3i7Wuoz6yQmxvZ0d7aBLBHrHYUp6LK399p4hwyzF-L5nSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06676f902.mp4?token=iEFu1aPzs5PK5tdfyKQM7aVqgK3KVuxbNwfJEsc5lhUCbxN_MHrTPy6-4ivIqc5r9sdw7rtJk5eaBWBSvGQ-m2-IeVTr7x2tCrQGRqkTnCjirgWBzkh-Ko7wnssZi_aMGpr6BTATnZ6X2W1esPGVSZUtiKFVFFdWQLpErDL20ERfSayhdr-yvsEfjyRqlomszCqDxT8FWSxrfsNUjqhxlArl4N62vvDVEmcMdJBmykjKbRBuW-ZOQOS4dtaT5JqJlIrbWbN6XUiregPFpjX0lXhP-fHteXpq0XZtUnPK3i7Wuoz6yQmxvZ0d7aBLBHrHYUp6LK399p4hwyzF-L5nSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌باشگاه‌رئال‌مادرید به این شکل از کیت اول این تیم در فصل جدید رقابت‌ها رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25425" target="_blank">📅 11:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25424">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kDl801VQtxi8pMlJWmHuyyesPcMlYVd9jXw4iMJWBN6MUwSF7eVtOmmRPVYoC4paIDioaX7tdnqPLsW8Uz-Yqg4gJDYBTbDj_bjItNX-GPqFbKeTafresqSby5tfX35X0iLGshtgYzhEJiPqsFNUGs6m5H3TFD0xNlrOuDq2cRKGqBzAiZ8kzmAi4kf-MtJN_f5S9c2PVdA2Uyk-1Vh3-BXAeKALIAEd6rirAdSOzsWplKiWGJh_IasjHcm2Sb3w1zB0yP0fL6dtphhKP8BsNYyHayVT6AzoLnRkl7goMQZSLtV7npvvIc8kTliqcQ0QGhVOkQspe72CofUYKXba7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/892129455f.mp4?token=YySyWcvf7n_-x_pNOZG6glHicji2tnOoOIh-7yLFyADJflf3F2_JD_-9IN4Z21g0DkFOAHUE54TId3-Nh7JT10PBXHRgqjXbHoWQw2B2jB7Sq5gd9ba-4-KibaJBOD7cuwnyE1pezBM6DcT6B2GGRGu5BKAwpAyrxxAnwWzDGc_P0LGNBPTh9D-7HGzDrPCkMk0dCoh9WqgQx_lGVHed9d43235Xdu6k5JE1YIOrVwBw5G8-41mw6H-B6PvVfLHOWx28CJsopJtlbaguy1-c6UDvjIiLx3i-aqd5qlfRHXmh1vQQe-TYC2F9bNRHkd7afr3yBgM6MkTkazdhvqXw6kDl801VQtxi8pMlJWmHuyyesPcMlYVd9jXw4iMJWBN6MUwSF7eVtOmmRPVYoC4paIDioaX7tdnqPLsW8Uz-Yqg4gJDYBTbDj_bjItNX-GPqFbKeTafresqSby5tfX35X0iLGshtgYzhEJiPqsFNUGs6m5H3TFD0xNlrOuDq2cRKGqBzAiZ8kzmAi4kf-MtJN_f5S9c2PVdA2Uyk-1Vh3-BXAeKALIAEd6rirAdSOzsWplKiWGJh_IasjHcm2Sb3w1zB0yP0fL6dtphhKP8BsNYyHayVT6AzoLnRkl7goMQZSLtV7npvvIc8kTliqcQ0QGhVOkQspe72CofUYKXba7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های‌تامل‌برانگیز امیر مهدی ژوله در ویژه برنامه دو سال گذشته عادل خان برای یورو 2024
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25424" target="_blank">📅 11:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25423">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RwSGOe_fVWnyGLhBfgNyZUQXwh9MTFT0g0a3_VRdK_5SpBfmE3hphYF-BoLDFdH0QQAp8qEAQdy_EEO3mq7LHVK4Kt3DQHbX7F5fkCPbCOtwfRSR81gwLOi56JvVeqKqariT2iCi62z7zmUlsLWmam_3ht8mut1pisXQhW3qBCmjrr1xPNNMaI3fmPgSK43fL1Uhng8AptlOHPuGQYyFQDgRdFIlBvOrC4ptQqSz71vhYBpFx00B7oim3e9bSzHfkO-zWdQYlV72q8nk8UV01q4P-1E4wFaXVGmA7x5NP0-y33qURcOGKzhYaTuQr7qXeiNG2NaDoJ70vV6ngGXUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25423" target="_blank">📅 11:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25422">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKoUFM_V8_dhDkOYc4o3-5tbu5GutwwmVZbAMl5eg04XQEaZt8tvHEOULR3ZQronMX4S5Zrgv4VBaNzS1zhQJZjwN86KSNiyIKYmj3xNFf5au2NHeDY9XuYtPLOI18GDcUKRpMCmpvSCSxHlaZoeDVJbym0c3wB8DbhRAPhymBxwBVZte0hb0ik7oROam5GDwYfBKGVC5W7BwRmIK9Txgtf55N9mQk5Zh534Az11q6o1eYdhXpTvBtfWjgn2jatPynoins5bJjRAnMQMiUuwQrLZbb3Ez_Ltu5sLnc7DcHKiFjHxye800Jtwrj-jC_N4QDJqoNPJ4IarOGXhYMGC3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب صداوسیما از تقلید از ویژه برنامه عادل؛ ناینگولان بازیکن سابق رم و بلژیک رو آورده باهاش مصاحبه می‌کنه بعد ناینگولان نمیدونه اینجا ایرانه همش از کلمه‌هاه‌فاکینگ، اوه شت استفاده میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25422" target="_blank">📅 11:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25420">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=O5Jy4pN0o5s_avt9MoRMZv4JRnCVAWM46O_fVx3oB7spEON5ZJl4EmmiPKPVmirxd73lwMITaejO2Z1Sm7v0oNIXytSDe7mPCndySOp6vLAPoBJDLDTcJepzv8mpSZfJgypEvzsOmTn-C2vdjeGRFjPAUjDbVibxhC3kprGRwP2e-tcNw_0rBlW01PA1nEKXdB3a4mraUC5Hnjd_OZTmOzvICGKnUA3TK3jjM-p3RwiD_cffJkh05x1jiOgIHTJJNq6--XONmJPdN14y40QxIAvnFZe51JDOsBqbW0hDK5e82JZg2roZEMP6dDgb475oZmTt-kZ1S_HddipEOGCIvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cfc077d3a.mp4?token=O5Jy4pN0o5s_avt9MoRMZv4JRnCVAWM46O_fVx3oB7spEON5ZJl4EmmiPKPVmirxd73lwMITaejO2Z1Sm7v0oNIXytSDe7mPCndySOp6vLAPoBJDLDTcJepzv8mpSZfJgypEvzsOmTn-C2vdjeGRFjPAUjDbVibxhC3kprGRwP2e-tcNw_0rBlW01PA1nEKXdB3a4mraUC5Hnjd_OZTmOzvICGKnUA3TK3jjM-p3RwiD_cffJkh05x1jiOgIHTJJNq6--XONmJPdN14y40QxIAvnFZe51JDOsBqbW0hDK5e82JZg2roZEMP6dDgb475oZmTt-kZ1S_HddipEOGCIvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
روز سه‌شنبه هفته‌پیش‌رو اسپانیا
🆚
فرانسه دردیداری‌فوق‌العاده‌حساس و مهم نیمه نهایی رقابت های جام جهانی 2026 رو برگزار خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25420" target="_blank">📅 10:47 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25419">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrRtj607TDt4YesISBX-SGLGWPCxXbNoOYJYuD6O4kce24GDw05HEozNrCPLIqvnooNhONSCd7kyanuEneE7U03ybECtVSxXajkxGGpEi_zo2JAsqLzrWfiGTjE0LLCPD48IpLIyNOGbO5GAcHhhOkMV-MRLoq-AWo5SOc9SRp8gLZsswaWk5fq56X4CszZRJwna5p_4L0MN8UCRTU7Bw5DqMfPs4cvpEOKCAJdzXifuC0pTc3TtE1mL0cx_13LwhTSDjYYNCwgeVAH9hzMrNRtQA_68vPqJ1mCkGS-sRbsKRXAgyRioJG0CyoTsZnBoy9Y8suxBhH6dWbDHOq0UNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
#تکمیلی؛دیمارتزیو خبرنگار ایتالیایی: فران تورس ستاره اسپانیایی بارسلونا برای عقد قراردادی پنج ساله با پاری‌سن‌ژرمن به توافق شخصی رسیده است و تنها توافق با باشگاه بارسا باقی مونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25419" target="_blank">📅 10:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25418">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHV75fEvq_MyWfta2WFZdQ0rtWbYZTs9XgkB1oL0JeApbV3bUbXjuYDZbUTupwLX_43Yt1AcLL7Olx0CtZcpyD-WdzxTJFho_4Yml8BMFP78QFpxPgJHTIiD5RT1vdNFJD_ezHmRali9xzL7Z1PJs73d53-kpKakiKNWbs3fA5nxm8CXz6HI7GxysFQPVvO3xfnyRoJlMcm7jDLmvAs_U0ULyUhuDBnr0e-mDcM-uiE3AGwcYL3GzjmNN3C8rctpq8KMQgaTXpQV_UuY0JHswxhzT94grMUxkisZ5QxRLGyklvAtt7eRKWl_fX9gc0zswfTmpEn-9-MUSnhUusfJNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25418" target="_blank">📅 10:23 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25417">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf45NXtldv2kKj2emmlukGXDavQ2lUu8eQ192VwTUnrSBTKydpxDdl7lqNk-D0GwIUB0LFIO7XtgGV4tihDnnL4dsvdujju039If5Yh6tTD4vDGS1NvfFhOgWD9q6hr8DlIYcQ734Cq5zlsdell8hNBPrk4rhC3uKFMHCAWsIM3srbaWFgFAoVb4e9x3gn8QWY7OJavk40bXcZdbSuSyH_EHZ0g0RXT65L3ZjYBkgX6I9eJooCR5RbA0JBZu4x8SN0ZU0LIS1DsOtAmIL8nsKQtENeubU6lYYaiaqCxFnqm56YJPQ758yn4RSYUpJeMUAslfL7d62jMBQ-lvSgL15STQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1ea0d3f69.mp4?token=i3L8Gle6lKWXB1Qsf-Voh2-pCmvY7rwb4r5N6yfkGcOSvdfR3lL5YkAKsBSdJ0lC2CJ3sKWuxa67fUzap_GK0k1dw950mkO1DTMhyMN6HbLbjJP73LA9w88g4fwnu-LA8i2ji9uFbK2kc6VqQKLiMKvxG7V9bvPajxcUF3YZZUlI-84vXKQRZM__74NT2Q6SVJLCEM02DWA_cM67sSaQjO08SOs_7w12HJROVcnq8ulcJKoJbQo1w0-yobTTJfq6XOhPYkBAwqXhGaDxlJRxKeAsNIpIcHebBqn9y9t87fvMOB8FU7mQXM6hDb4aujL4qOlcUT2A_uBRreiXtXKf45NXtldv2kKj2emmlukGXDavQ2lUu8eQ192VwTUnrSBTKydpxDdl7lqNk-D0GwIUB0LFIO7XtgGV4tihDnnL4dsvdujju039If5Yh6tTD4vDGS1NvfFhOgWD9q6hr8DlIYcQ734Cq5zlsdell8hNBPrk4rhC3uKFMHCAWsIM3srbaWFgFAoVb4e9x3gn8QWY7OJavk40bXcZdbSuSyH_EHZ0g0RXT65L3ZjYBkgX6I9eJooCR5RbA0JBZu4x8SN0ZU0LIS1DsOtAmIL8nsKQtENeubU6lYYaiaqCxFnqm56YJPQ758yn4RSYUpJeMUAslfL7d62jMBQ-lvSgL15STQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های‌تامل‌برانگیز این داداشمون راجب حذف تیم‌ملی‌پرتغال از جام جهانی؛ عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25417" target="_blank">📅 10:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25416">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJVyJY45QJXM8oBfF0bq1WFahEv0wqCjgN-Pk3a0jVadoHRZueXNJLVnXaV-Jw-LkL0ih2m3UfC9U9xMRwxClrjn2sLyfrJME9pxoT_4-ID0o2uTiCP3HNwijWwl7OnkTGBLjmMxvkSL5cIgw0P_yI0fuRM5fKsXdeGo2cWdXjgEaU4yk9qs8mJEdr4l0ouVS3W2sxNh5YECSC_46faDEhb5XZ0rFOTgcdHUdvfjYzYuuf6SrsCvlkSjhJyGT-hw_TaB_ZjxOGAPeQNo0ogBt5HE4gGang7FVHtAO2Ze4QnopO1jW4KLuNHI2KRx5AvLGrv9e7rSmbspgpt28EEiHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
👤
کریم باقری مربی تیم پرسپولیس: بالاخره وحید هاشمیان هم رفتنی شد اما این رفتاری که با او شد در شان و شخصیت باشگاه پرسپولیس نبود. بهتر بود در دیدارباتراکتورهم هاشمیان میموند و با شروع فیفادی سرمربی جدید میومد. الان وضعیت نیمکت تیم برای بازی با تراکتور مشخص…</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25416" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25415">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQqn3JGn_8JyNAAMa9ysTckgSEOqo6mpMAxbNhglBmN-QkR-NDhk5LqvgkFfkbEPd4RLM9-YoBivv0OH1jZkh6FuAjz2qaVGBn79FAo6k19IJ-yuOqQEXyYCrIpQZ7M7DRiQqswunqgs46eTDt8UMcgEs895MYJfv7yQ1Xj-8F7gUpHQ84sz23Bv0MYpJDs6UNeLv4gOOtDCtLyjC0C6plmliaEgS1LP7lS0mp3HVkRy3ZxMcLGJjYDFdLFw0QhLDCZeErW16vtN_VFhnNcw0asDKj-XYDBgv18tDxTEG2CeYjPWaMe-fX4x49qmuzjOhPqraiA0xac11WOyzVcsSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت
:
سال‌ها بعداز این جام جهانی مثل 2006 کلی کلیپ میسازن که‌چطوری‌این‌همه ستاره با هم تو یه جام بودند. تنها مشکل این جام ساعت بازیا بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25415" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25414">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLxtvjgk_8DOQwOamOyh3SIGp4_RFxlwinpRD0t_zvx9pIhAogBc8IXqUuqKfF1UbrASzd5U4ThpZbQek89fLvZAXi3pzHdpKFug8O3tis69Dlz9SuZtkobR2YvTy-Azg4Kfrg3nxjO05Q776Nezw4GhYj3C6wYXf5gMG0jk25emv3PDJgOQKidJKWt1r1qOpS1C0vGE5PL-WdpRcFF0WvruH2dNPbQ8c-PFI7lWowMzYfvaqZM9P5zhHkjuKs3d9mx_KnstPqBrqCRtLPJeGY9BpOUCtv7GQeEj5neiBzVbz4KQGh1dVhW0E4nesSVrsJI6O7s336cjIYarVfLVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
بدون‌ریسک‌جذاب‌ترین‌مسابقه‌ی UFC را با بیمه ی 100% ی وینرو مسابقات مهم را پیشبینی کنید.
🥊
بازگشت مک گرگور به قفس
🥊
مسابقه جذاب UFC
🥊
مگ گروگر
🇮🇪
✖️
🇺🇸
هالوی
⏰
ساعت 06:00
✅
1میلیون‌تومان‌روی‌برد کانر مک گروگر پیشبینی ثبت کنید در صورت پیشبینی درست 2.5 میلیون تومان برنده شوید ، در صورت پیش بینی اشتباه کل مبلیغ را از وینرو هدیه بگیرید.
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🛍
پیش‌بینی به ضرایب بالا
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
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
🔊
همین الان وارد شو و فرصت را از دست نده!
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25414" target="_blank">📅 09:48 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25413">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URfZ0f7Y-kcyDY5hrqX173GH1ui_rZT_dZk0vPH-JPwzvQG8e3A8ihYBrR-PJXJole_7hmtB8UtZabf5Q4PX5xc79-gccLDqzneAiXlff_3l2FrS3WU0u4opMnE__g1Ws6VFGKcw2WAG157BeTZ_K4Ebc8JbNp-xyJgsaRd1947_RzXVyfyhAIlEr4Ad8aO_PfH4BBrhsKIz2lt270bhKGICyXqKd0U4oyrGgSSYj2KNeOmNDn8nWG4r0z0ppq8JBQCiVf-IEmRJomSccHNVm3t39mRrzrYBkmyIPmT7wRvh9-ajFMpQr6RqN74YPg1PIpkqBp7YINNDQel_QcMYCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ 5 سال پیش در‌چنین‌روزی
؛ ایتالیا مدل روبرتو مانچینی دست بکار بزرگی زد و قهرمان یورو شد. آتزوری بعد از مانچینی دیگه روز خوش ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25413" target="_blank">📅 09:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25412">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=Tr6HXKRC_thcnTpm1XKqlyq4MGzR7V53SB3lyN5GMCDT5wIdUQkyV_79dJqMSjLJQDB9hs9W6gNav-grYsPuy0aFhZnPkqa6RGz3MaopR2TxqNqfgCwLd1bVe5740r-KQSUmiwOwKSe-SlNPIRo36hdiEacr0r97eOq5rzXp7dx1bPrUf9YPBprarucmiSgI6uurWnPoTPbX76chrpwtzTxfB3jV-kkqiNX1QR0TGOrx8U-NM8YBPqxcL9FAoEC1FI6nXgyN2w8e61WJ6V1SFKlEPFIHy2owqrhqntZWo6rLOXC_CtdESkgr_hMrtw8lBzDYlv5DYr7AYnsTa22ZSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e28eceac9.mp4?token=Tr6HXKRC_thcnTpm1XKqlyq4MGzR7V53SB3lyN5GMCDT5wIdUQkyV_79dJqMSjLJQDB9hs9W6gNav-grYsPuy0aFhZnPkqa6RGz3MaopR2TxqNqfgCwLd1bVe5740r-KQSUmiwOwKSe-SlNPIRo36hdiEacr0r97eOq5rzXp7dx1bPrUf9YPBprarucmiSgI6uurWnPoTPbX76chrpwtzTxfB3jV-kkqiNX1QR0TGOrx8U-NM8YBPqxcL9FAoEC1FI6nXgyN2w8e61WJ6V1SFKlEPFIHy2owqrhqntZWo6rLOXC_CtdESkgr_hMrtw8lBzDYlv5DYr7AYnsTa22ZSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آدرس خونه و محل سکونت بعضی از بازیکنان مطرح‌فوتبال‌ایران؛ هرکدوم از اینایی که گفته خونه‌ هاشون کمتر از متری 500 میلیون تومان نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25412" target="_blank">📅 08:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25411">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=HD1MDhNicZKci2pDP8vochop1hK_zScj4UC3sdm2pohAuF2UYlE96URF1T4rgrxN4bgEgRjCpw-QFUhnkaupjRWrUKJucRgkC3XcBqfatBVDiJJ_9HU3Ay0k4KNtx09AirHA2aFMyRkG1HE0YSuotjUwJOcLZC20oHwqkXMqRPKASTy5n2CdAOc2rDvfa3xhhvm46uT2Qd5LZxKgzr3PVSMmdgnGW-9WQ_3ZbixKg0TKj-J7YC1rfYr9E8_DhIKUIKOUI1Ns0XM9O_foOr57d07tQq3oF4IJ9fwQfW1cbrCptKCRNNs8KMKASEtLRtJ5Xkru9Sgww4gessM0WIApIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b56368b61.mp4?token=HD1MDhNicZKci2pDP8vochop1hK_zScj4UC3sdm2pohAuF2UYlE96URF1T4rgrxN4bgEgRjCpw-QFUhnkaupjRWrUKJucRgkC3XcBqfatBVDiJJ_9HU3Ay0k4KNtx09AirHA2aFMyRkG1HE0YSuotjUwJOcLZC20oHwqkXMqRPKASTy5n2CdAOc2rDvfa3xhhvm46uT2Qd5LZxKgzr3PVSMmdgnGW-9WQ_3ZbixKg0TKj-J7YC1rfYr9E8_DhIKUIKOUI1Ns0XM9O_foOr57d07tQq3oF4IJ9fwQfW1cbrCptKCRNNs8KMKASEtLRtJ5Xkru9Sgww4gessM0WIApIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
دابسمش‌بسیارجذاب‌ازگفتگو اخیر جواد خیابانی و خداداد عزیزی در ویژه برنامه جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25411" target="_blank">📅 08:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25410">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sORTzXzb5crpPcJUI2s4mD8NXTnnTsHnovz7Sm6oWnABQ5ymnWJ2cuXiAp7SKveenqkCQZtw7LNl-Tn2U3ugGvcRvlloOXSBVVBPDdVQ0yNkxVJlzRD7BhyATsUmvu4jwIc_JDf6kyYb-ezxO1IVMZBHpLKFzOr7WZz7Kt3zrfkBuAs0uLbytSaHPVYG0X2N98CV0qkbwC9U_TCTGC3ZSb3Uj3adZTeHEPJbPaU89iugWgkoZFsZ-4HTYH8h4ob4_BwMWMaSclVQj00AygqxxxfQDIP55WK0IgWJvN1hSn3fPhLQFKRucSHOIMMp9AFgDYuHCuCCvNWwtNWd4ZHpkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25410" target="_blank">📅 03:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25409">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omsWlJYhwv6HlOFssg3c3IS4xjLjltrfEADOfjD7ulAskk2dY5sTNz9WPi4Iq-x7mFGzph-RZPYRVK5TkSOwEcF_G8RwB8H3nCrHTgLCm22MuwdFG0gFmT9fPc5BdWhH26W2whAjB3u8QNzTHWVMM6jPOF17BIDpvWMg1N-RrbT-ZV3PYriJReNPCAb_E9T_oi07OkiZU3Q0eEnLGeJqCp7Hcs8rRvldkWjzoXk16qJkx8hO4hV7YOpM8Ip6m3UDwVgR3GvUNsaIw8KchuhiXgG19YJFOyKdOSvJoNvKrkNW97cZYQq6C4HBhzHdn_FXSSAZdZU6_sZritaHGjErXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#نقل‌وانتقالات|نشریه آاس اسپانیا: بردلی بارکولا ستاره تیم ملی فرانسه تصمیم نهایی‌ اش رو برای پیوستن به بارسا گرفته و درصورتیکه لاپورتا با ناصرالخلیفی به‌توافق برسد این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/25409" target="_blank">📅 02:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25407">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=p3HqYtbNOH42Cqhbi9covFZOtw6anrgZLu55QK4taHg8dw-5p3l9WYvPfqFbdfQ8Y3n1xHlwHIi37-NncKPBeBRz0nrSVTXKHXuNyxyukijAH8oBwA4ORug6ye80sg2lavNr_9wSgAXNWtxHfcyGT6OI9WOCUoSe5tkLTlAwqbiGS-LfrgOC3lGBmDPehyYM03YiNhXpO--l_Zuvv0LPyTUrbgfKSJN1jl5rJaICKZ7OU7-2rL9gGmYabst6GX5KFBWwekFVl5PXLGRlmiMA5rHDGoZwMMj0bu9fAWks3DkMp6RR-81ExWyfI-niHq4YJ6vSEyt8DgnfCdRlWvyuww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4014cc1ec6.mp4?token=p3HqYtbNOH42Cqhbi9covFZOtw6anrgZLu55QK4taHg8dw-5p3l9WYvPfqFbdfQ8Y3n1xHlwHIi37-NncKPBeBRz0nrSVTXKHXuNyxyukijAH8oBwA4ORug6ye80sg2lavNr_9wSgAXNWtxHfcyGT6OI9WOCUoSe5tkLTlAwqbiGS-LfrgOC3lGBmDPehyYM03YiNhXpO--l_Zuvv0LPyTUrbgfKSJN1jl5rJaICKZ7OU7-2rL9gGmYabst6GX5KFBWwekFVl5PXLGRlmiMA5rHDGoZwMMj0bu9fAWks3DkMp6RR-81ExWyfI-niHq4YJ6vSEyt8DgnfCdRlWvyuww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25407" target="_blank">📅 01:38 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25406">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm-LUJPp9nNeFFLVEjwp4N4FiQeiX30otB9hMNa8NgIthMsggRdLoHin14njn1-jPzoEwg1XVBxGUSKsaBAN-LfsfyhI_OhxQnwUySfFYwmP8f0VRTmwun-5OllN3So_vWpK9-06WZOu9r8V7Je9KITkTvtZbcmJycEo-LXQ9_GHvH8_fKcH_pc5EAN63YGBd1qT_96Vi91oJBKO3-YSJu97Bqc-gIywcWb2FgwoDi9Sh4UG6Ez1kxXGEx6OzrBsRJXG_zUpZ6NV3_EIcYpUBVbM2el588TcPxm2Ld7Dol44p2_wDN9U-XDWYqErQGt11kixv6P9K_I2FLbYGMdQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
ارلینگ هالند روزانه 6 وعده‌غذا میخوره و حدود 6000 کالری مصرف‌میکنه معادل 24 چیزبرگر. هالند عمدتاً به‌مرغ،پاستا، استیک، ماهی، سبزیجات و عسل علاقه داره و بیشتر آب مینوشه و ازتمام خوراکی‌‌های شکردار اجتناب می‌کنه. جاشوا کینگ هم تیمی سابق هالند گفت اون مثل یه…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/25406" target="_blank">📅 01:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25405">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHS-9Cjd4XlDi02tLru8bivCnKzy2hpABPZiTDRx3OtkUmnvIBeOW_HJ4-VF66fXwQzxcNrqnCmkz9vf3njHMCy2tTLvA0yE8wxIRW9ajwwO3umuk-yZextRrfihJb55OKbBs0xir79cWjVqbmEwGy-uSXq3-CxXuiPz4zhLBdrOVRqs_E_wnM_hoh8bNjZTXuZ4fPgCxRUU6tlJ_iADR0-TGut150_xhx7ESseuB1nFmhhbOF5Kt73uznB7uTcwm1aQgtxVURegjkXoGY1fItBK66HbidkiGbFOWXs78I4Z4Zs7qJm-IWGf5qRYXcjeyc7wRB9aEoo5B5Fl2gmrcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ دانیال ایری مدافع 21 ساله نساجی به دوستان نزدیک خود گفته با باشگاه پرسپولیس برای‌عقد قراردادی چهار ساله به توافق شخصی رسیده و اگه فردا مدیران این باشگاه بتوانند رضایت نامه‌اش رو از نساجی دریافت کنند قراردادش رو با سرخپوشان امضا خواهد…</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25405" target="_blank">📅 01:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25404">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICcTVS1FMmlRjZ1FssI-ZZk3Xpfrx2-RedKRPm2Xcyfz2I9QzYKGy1NdLsWugm66V4hTFsTNdwZq8EYQuwx2DNkcpM4BwA3I1QS0GlEEXCJEvUE76wRZLsgVp-KKZbgdElZT9E5YJgkAKS2mekSfpGV7WOPds7YtzuBYAdlRrhCy-LIeGoE-QqMDB5pdI4zIJmMxZu7wWnx5LRxD7bpwjWenuQ_qQYdI2eKQJsi78REIW9dpRWPBlBxJT_Gfd6GU-pu6wSAzRuI-FMXHZ8ZVbDKkfhoRCb1L8AFAtMm3jffI8QniciaxWH2DwzKW_LFosTA2yzcsR2mbzcEtYscI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌بامداد‌فردا؛
از نبرد انگلیس مقابل وایکینگ‌ها تا جدال مسی و یارانش با سوئیس
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/25404" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25403">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgURsCZygzKaLSgq3OODIT14KxO3uviwk5mS40wuy7zja-vPqiKSXcGiGfZtxa4ALe1KadKdNQ_h9Amrlph2nA-04lgWM07vGEgszcRPQc1B96nm6O0o01JVrDIh_Yn5egmjSuf8GNJc12ZQtihej4-Eg3hxTU5OE46ogYaiWX8oOLMvPJdGHJXjYq5ShvZavy6SFYxVmgJjNIKfieMlDsciWJnpj5Wjuj9_dY3wKCZqXtxpHKMCNnswuttZTaFOTgyHT6gfZaZWxYRAbjT3lxzvhEIrM96Rv2zw0EB5b8-Fsq5p4fZYh92buxyScV_-RilqkUxV_PB6yXRdSGrM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دیدار‌ دیروز؛
سومین صعود تاریخ لاروخا به‌نیمه‌نهایی جام‌جهانی با گلزنی مجدد میکل مرینو
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25403" target="_blank">📅 01:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25401">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIFyZa-1kRsHE5GNMKyj3gVdCiDhFhv1stKWlnb7cGqU8TXKoBW7CWFu1vVDHTHV67OvGKu7_FZPgYduSE1eRPy_N3JVXV_0emU-iK4gdZ73jZOVAiTlSNevVD8zWwLupltWLljJcBqz-iQ6ZLC9TcE4VOVQ5UqDgELnvUK1QdzZA2v3jCJAj5HAxdiB2bD_RjQ9_1lYJijsLLYZMQCaD5B3lMpPHIHz9dSjim0IcDowuzQiThTg2gxDp9nG7fRdtpFnyVPRsOuPXK69nMMi3kIpGMaojazSPuL1CYOboEbUJA7KeFjtB1WmTzwu-P8VCryRKcDrXwxCSh0s2Lu9cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/25401" target="_blank">📅 00:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25400">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pggF432vNYGAPRVDCGJKHMGZlptBL5g3kiMSzYhiqGQLodQDfASQOdFEf1cDjtI_MgSk7rScFpVDicGJp4ytsFb8RbhmE9hUZ510HngVdksVRhnqiEi5u7IBrmt1pnlMyjTa34CBmJu-mQ5RjhVRslb9b8giie_6FXnPBLmuIqaT0HwH5l0vMl9ktoUVCEnFRa58f0wl53d4DCshuF3yPg-rIV0W05uS4lvp6n9M5RFVBXTVTmrci1nGiIjfo8iMrQyKZvGmGpyru_SX5MuSt2cisjvNOK7yifw4SoDbERljLStkur9N5D0atqAv1EI88WwKngiXUzmMhTkSK1HWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌چهارم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دو تیم اسپانیا
🆚
بلژیک؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25400" target="_blank">📅 00:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25399">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJg5-w-hKZYx30paejfXNkmcNoiMWN_EFWEMNl3dRn9Aq2VxDwcjNDOjAx0c0VjrgNwLO3GVwD0TCE3qA_9tqClKrA3UFJVYNrbJXgGvUuUVB8UN-v-qVFWXyD6yDRT5qhgukp8FlNBjR9xYvzaNhGWVMXKRxLpE2D2UiUsSKjL-JUudsvUG5H_NrBeEwlI-uR1AcGifSu9SJ7Pt-E2qcnPOtDoWj0PSLsoddQ4MazpueC8x-hY-5lYizMgcF4NFY0IaRAktpx4oI4o6Nn4LAk79Y0BIRHGAg9_nP2HWm7HPxOL6W8GaJcrB8HffcIJfb78RqIfgqCf9Oq_LhIvmQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛ صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/25399" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25398">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSaD2YkPoqxmIrGrjQpzqNmJe-SYTM9rfOQllaSMUizgPWtHoINe7ZnxUeFG8ikJOSN8AzjCvQaX6ee1vVruLnTHqilEwQdVMctZbr0-Jo53Ua90J8mifr8iYLjtlZLchrLRGwqUJuSIeLUu2LWo4KSW-mlF8rqaKZ3ZQLOBRIUjCVLMtGYa44Nfd-cZ3RV0JWUIiE8oktNnZWJmj7ZOYi5Ot6THL7p_eys8qU5AuEGn4PRY9LhnM_Gw0E-E4uza8Kk9SmKwDHeHJDIIK7oQEiPQ-g6LRL23_RlOhjf5gK6hAU3YcFZqGXzP4LJCmO7UcLkjQOpJB4n-pxAlteFtVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک چهارم نهایی جام جهانی؛
صعود لاروخا به نیمه نهایی‌جام بابرتری مقابل بلژیکی‌ها؛ مصدومیت تلخ‌ودردناک کورتوآ کار دست‌بلژیکی‌هاداد؛مرینو باز هم گل پیروزی بخش ماتادورها رو به ثمر رساند.
🇪🇸
اسپانیا
2️⃣
-
1️⃣
بلژیک
🇧🇪
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25398" target="_blank">📅 00:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25397">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlQr_v8BajpwcJSlXt1PCGyeHPPPKecZn9MOysnksdJklXq8ku9fp_GMMaYa91za513yW-GTBpoacAchM0y128Ky4nbjcN11li2bkRIgi-oCvA9U_aeKUp5mKe1Q9032EMS12S5H-1O_5kBXj5eGK_ouBJOFI9109yHj2U0VWa-dgSq4CPceWX5ms2HbgHkk98ejlBmNGT_NebkKjtJ8jRZJiJ-PUdFjg0aBoted2fQNwF7ClKacSvgLoXtCGm9U5R8opgQ7RpQ4z_mdciAjI2MBVqui53Itpkhxsp9ftbad_oHc8oea8igVKpFZFlRNOy97WH2uezHpCe5kITvZFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
#تکمیلی؛ مهدی‌ترابی درزمستان‌برای تمدید قرار دادش با تراکتور به توافق رسید اما هرگز قراردادش درسازمان‌لیگ‌ثبت‌نشد و با اتمام قرارداد دو ساله‌اش باتراکتور در حال حاضر بازیکن آزاد بشمار می‌آید و هیچ مشکلی برای عقدقرارداد با پرسپولیس ندارند.
‼️
باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25397" target="_blank">📅 00:17 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25396">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmk1Co-16RvXdVmx0FwWm6cMqXCAeQ0yJbcuufuMQBvOcumyCzfbjbjRPQJq690jx0axlXr82UVOrnik33ID00_qhZtMnmIesytyYcDqkjSAZQaqSuI3Lsu_SubJmY930AhtOo9uLAt0MpinsTO1TWisUwU_8RJe6d46A-hT586n_fWIYg7ySTdgCdzBjKwgrh_QuQonkNZHES7ktiDXGvf2BLpIkhlcQp95KKATJtIvuexEegr6zRZjHLkphNXl0t6WWMbYLxuMIUYrH5qWzHysFHrFncGn5balqqlxs6jr_WwEwcF7u7nDcn3He0VpsDBIbwQLaF3r9eYZtwcnMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ نماینده علی علیپور امشب با حدادی برای تمدید قرارداد دو ساله این بازیکن ملی پوش به توافقات خوبی رسیده و به احتمال فراوان بعد از بازگشت به ایران با حضور در ساختمان باشگاه قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/25396" target="_blank">📅 00:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25395">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUn-sdt458QQE4rTQEnQKaA4o5KzWI_rc9wW7_YZXa1s0UCEZeWZb_gl21WaSOivdk4Hr0qj_LEDJZozRDIGEmnTKH9rkhTNV8Tfq4decnDHvBsCiHq67sCZCeewD2Jdrg8fP_stwJMce6AFf8bVRbDqqf6diH9cUdEhIFg0INdZEZch1jFH9gqOyd6TkEMNWoNg4BkbPyYuEMmRJY0OLRb0g1RsOi2J4RB0g93_4U-_meobStyUHiblhXr0Kgo36Ptso76ZFkMeUyT0J1hskQc2QVxGkJwf0dm0476CVbWBocCMQ989YL-lPbldWVzaZ9yK1UHuSraamc27PhfqHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه پرشیانا؛ دیدیه اندونگ آمادگی خود رابرای‌تمدیدقراردادش به مدت دو فصل اعلام کرده است و درصورت موافق سهراب بختیاری زاده این بازیکن گابنیایی بزودی به تهران خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/persiana_Soccer/25395" target="_blank">📅 00:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25394">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1ALFcnJMhk5VSOJ2Ow01O9prMFBUJrSu3Qks6kEcf8aohy0ZUXeyvdhfAHWcKrPw0arTShuMfiEfJCVBUsxtlbEMbU99AogrPP0kae95hMQfmwFkZ9jXdBW4zi7mHn-OEMVdZu_1CESNaLPuWUNnKKJPROUmzdTsa2Mokfld23TGnVo7H-2nS__mTX2LQePaHukSwwgjuOv3AInOaZE7p94AoGk9pYLPIv1bJoihgDxQ72_Z_vvT8xIEawVI3LZ56f7C013R20pIBsPn9fHP_glF2-l4cH72zX6jB7mHo7awVE6fdR3ZprEhDd2t7UsUoHswfmMoUwHErLUDU1AXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ فردا ساعت 11 صبح جلسه‌مهمی‌بین‌مدیران دو باشگاه پرسپولیس و نساجی برسررقم رضایت نامه 550 هزاردلاری دانیال ایری برگزار خواهدشد و درصورت‌توافق‌کامل ایری با قراردادی چهار ساله به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/persiana_Soccer/25394" target="_blank">📅 23:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJOnoMxjmFF9IGJkSZYzCCsip1QJm8bmWChjS5txXcAzsJ56uf2V8nTQea0JPdfZPSwMCvYFJK3pDHFzXvptE5FYdJIejrUON0W_f02X5b8VnLWj-iKCBqCDJJuhsFsv65wdjs5O6HQDenen8E8r93Mxg1EU-3E37x22QgX24vYjit97TYTRQZHRnNYhH_b9y97KCzDP4JzeAhoeoULEVV02xpYWbl1hvC8Iy9cZruXZzlVY9eCQ8k6nqI3I1T-xDzw1erqAOjeZ71IO6qsZDHkP9rVUrqnWuExHOtTGkInBRpgUTWSC-EbLFKr1a08icyg5S96aWuHsOV-QsWLyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ebFH2Xl7xXY1o2MwmztPsGYlCBLRlUjDBzaXKFTfaBPYECHt988A9LA1HSuddbkPbUYvCnPpKhI1qF9vZEp-J9EilkYcKZqQ-BMNS5kOxu0PJ6cE_WV0A5XcIT-Xb3MLcfNhxBL7k1jWqK9oCkK3LZMcPpib6ea019AM2rUbqWAdQGWUORImso0wFU1RmtEAXAUjKK9u3llya6N7qA9lpS_i4jPY1kelgXoqI0E0RI4rn6Ej6HhzHl3ZAHTAnldP446H5QshmZlHpocRgc8TJyInT6YjUhFQVLIINL_Dca8oWthH6jUuQ5ypbyOTfbYhgLYyL_bKzT-SfN5ELTEPcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌چهارم‌ نهایی رقابت‌های جام‌جهانی 2026؛ برد شیرین و ارزشمند خروس‌ها مقابل یاران اشرف حکیمی و صعود شیرین به مرحله نهایی رقابت‌ها. اسپانیا
🆚
بلژیک حریف خروس‌ها در نیمه‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/25392" target="_blank">📅 23:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRvzwLuiIMoN8CCA5yXZXdpaRY2NlddxkKeeLXVitD-5s4xzBf0oWtu61rMT2FQFnXFVVuoi0_nlRi7Qyju34ZcELGlzVL8ZbkIGX-xuv7cxzh35mLW0GhV7-F2NKPT9QluwyFgierDk6n_5ZjBCCIxAJzSpLd3Lr4cwYh3RBek5ceL5uzBPPlWdtpkkvqJh_TcVpc_2UeS1cWln6iMDFO49dxH75lyhK7AzDts_MvhxoqA4d9AwJ8x5kQVga1KQb5uMChu0MGn5ZBepjiEp3D6P6IxjiysnuSpcjtpvQtiGxR5-6V47rY-sCw-A6r2JQbtgqeSxorSyq4X0wZ_7Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/25391" target="_blank">📅 22:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBiaegE4IsS22d_LkfzhqS0VBZynUfLT74ajNQlOXh5CuSwx2pxaXA8zgQ94_QjdFiivicnjrA5tHBq-KIa-_eOaEMzoEerFpGhRhz1Oic9Vk-VSIbZkHiZwoAyHrXF2z7rkAyU86j7o5ET_IdyGf2k5PSNPKayvxgsut8mONo2spX-rUlvNDkCwe_w_B4kms4jlTcpZUV5cbV2EHit2PhgVT2X5oAj9uxL8loX1cjIetK1lxCXj5cdEryvvWpHbHOF4m_5hYYuqgDRB0rSsvWiJDeUbfSfLn7ebhbfMJPi-ebBB5nhgu3GFmIet_Beqy9OIsQvYdfqQISIrhyr6Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا؛ باشگاه پرسپولیس آمادگی‌خود را برای‌پرداخت رضایت نامه 600 هزار دلاری پوریا لطیفی فر اعلام کرده است و درصورت موافقت‌گلگهر این انتقال بزودی انجام خواهد شد.
‼️
فرهان جعفری، مهدی‌مهدوی، دانیال ایری، مهدی ترابی و محمد قربانی اهداف اصلی سرخ ها…</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/persiana_Soccer/25390" target="_blank">📅 22:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9FVTiKevV0op6KjTea1o_S-JjdkQNVZbyOdSljDfH5UGKE61bfuLD8tJgaTqaJXJOwXaFgHeJp-drMHbdjeIOrruHhK1ObOr8wylgYlJarSp2v8TfQmy12T9y5I5Eb7Rh8vwmHP3_41RvdFaJR4acNPJTnfuPpWPoGp03y9Gaxszy1Q4y6OKeBKfn25qnWzrvRU0BD3snTN8c50-GaLZDfPZj5RDcaAief23YQgCUohaiThvvg_7Nvrt7z9JzTETgALXjwIuKZa5mwQnpqQWaURw8040Zfe2H4YiZ4_5mSIRUi6f-PnqNz7B7P2qov_k450HJ757mh72qIDSlUFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/persiana_Soccer/25389" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TPwO7vLaZWp-jA97_W7JvkyvMQfcKJbhNGnkbsPzVdnXa4CVLsoFaebFtu-2vebaV3acCNwq0lyD7rwDvbe75LKbHIwbny6Ktz9E-nQcf_KrjSwwT3rZl1kD8mXJXxt9aNdoGmB_flk8Y0tD0tw_nvmYPfj6W54yZthusSyfVn8vLWa8u0wSyt8zOFBzhMmD-akPEgXgb1v6xWM6pyPXJ02vONJSB5dAt4K_MrDGWKiNg9WuLlQR6vcH6okyCo0SJdphCOEvwv6QH_whbJbZxiYWVEF8ctczEmZEcBd_1a0ZqoZKO6KuDTgpc5lRa4losV3fLk2bnQl98Q44xb6DQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه گل گهرسیرجان رقم رضایت نامه پوریا لطیفی فر ستاره 22ساله این تیم رو 600 هزار دلار اعلام کرده است. کادرفنی باشگاه پرسپولیس تهران به شدت به دنبال جذب این ستاره جوان باشگاه سیرجانی هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/persiana_Soccer/25388" target="_blank">📅 21:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/avMU6Hu2LastcI3WWxcnL83_EKPSE8BKmzH05lDsw--L9EOxAWAzbG5VbrTpeTf30IAhcHPdxERTseeiy-ByY3Xd-xYX8VFoQTK4pttnCI21Q9NdE8IvmPOMESnCu4W0jVLUGzneuxilGzb0ZSrBj50OYhvkmoLm76pLfwRGc9cByKXCBGNEkk3PjIdmmAcEMKak3bDY4ghVvu_lqLVJze19q_OAYthh8s0IeYgYYSzRMdI262fqiMMoQB6XkNmORJmg-amT2X2mCSb-nBlpUOmWqJSAdMUPQG5HtQnvYYuLaUd04Zf0IP7YXFOqZJIAz1SLB8j0w1vGGEi0Ix-e7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
تایید شد...با اعلام رومانو؛ کریم آدیمی ستاره دورتموند با عقد قراردادی 5 ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/persiana_Soccer/25387" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25385">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhQ4tS8bzieAm5tc8M-LUW7FlsUM_KssopmVRsr0Py649PbL3htKAfdvokJUShkEpbKPTdzZU8spA5KEQ5YyMKSOpeYTcpHr-mwRdiKrWhKOmATN8nL_eGpiYsPb8w6VkX1uahNvngJEC7lJJC60MVutaNxixsx2q4_I2lRKXeYjuefsoTZOZ48uzqIqPefxPdT4Jmjj5Z24jv0qQANATon8AzsrbWE5dPZF_h537GyIj6a1SRqz3iacoqtvuxpZa1zRPPiHhdtaEn-cc3oUR22KUN7PA6DX8zL_jiat7hpyW_9xJDGJKJQKFuM1eC_SxzgsHExOeAplegr7uLn-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F1kRM7vRvnzwi4fNWyEsNX1QseHn6Fz4k374iMJrOFTFZ9S01AEQwhzpxFuvKKpQpZNnjja1lkzVcAvWw3yNaenOz4Hx1PW9Fc0zqyjzdThltrqx_WweiZBliVYNk6V5ojzN_b5NJcQzV03RIJZTAeqJezIjVpCQ8NVMeR9E-vzNl-z3GlcV7TbeS13WsGaXEDsybvGADWslxja1RkTe_VvTggV2oS6Xu1-XyxFT9c8RskbMXvVWSZL_6E650kjKnodyxgf0ePGo5qkC3cDuwHn4LdQZlXYAzR7az_qYRZCtOAElxnpOv4EwTp7jihXPgRxhgflrIfx5LzpNNe03Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
برنامه کامل و دقیق مسابقات مرحله یک چهارم نهایی رقابت های جام جهانی 2026 آمریکا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/persiana_Soccer/25385" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25384">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLLVJlrr5pxCg6daayMeaPKRq6nCgnvgxxkiD37shwab6jrIolZXODtuOaw9J47d0-lq7y-7ImgeXkQdFyoc_TIP3bRlf74m3HX7UL-6kGZ4Dcf90b4Mbbv0KNkIIoU8SkA0G7A37qsnpuRi_RhRsq3hGs3Ws2W5VbvV09cUS-oqWEkFAXtWMv1kAlYm07CyaymgIoRCg5YJSWWlBiwxU6d6wnmSGTM8in1YFD_GWeHs538Yo-4hkIA9kkz45SYs0TyICdeY3G22yS9ZCatB9L0reiaC-BrlZYaELdaQzX6FSzLcr65njaPnQ6_9rq7kkc_pzJ-6Ly-7pZG5eaU9sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رقم قرارداد ابوالفصل جلالی سال اولش 55 میلیاردتومان‌ثبت‌شده‌است و سال دوم 70 میلیارد تومان بدون آپشن. در ازای هر 5 پاس گل 10 میلیارد تومان به رقم قرارداد او اصافه خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/persiana_Soccer/25384" target="_blank">📅 21:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25383">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e53vqYFZ9dtsBzTEIsG9b5pxcfo2J3s3zo6iR4gvJfumUz_P9MUZPIOE9aUx5Hyk-UqYGu91XQ56O3wAHahJ-2eIKZ1fWqRiDcnoWX-W2qr7HuntQ93OOuZtxuLEJyYLNmweijSFarV3BQNwKr1CHeX03uJncSDZ-yDSY42kHhyhs8nbphhlYAj8KK0KcJKsg3fE0uIXWXPpfZ8m5M7sVI_FKCWqqVzYt0YLj9Osg09EyKZ3Bu_VqjyYcdSi7ZYSTMxQ7TvzEoAE5C-mRBGIggdPgOROrKITjZ5KOucmvG1k3DnZFmRT-ZiiGjy_tIQsCYmRdOx3D59pWFT6o45zew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
#تکمیلی؛ رامین رضاییان ستاره فوتبال ایران یک پیشنهاد دیگر از المریانیزدریافت کرده. درصورتی که با یکی از این باشگاه‌ها به توافق برسد با پرداخت 200 هزار دلار به باشگاه‌استقلال قراردادش روباآبی‌ها فسخ خواهد کرد و راهی لالیگا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25383" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25382">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ra1pbnlYivCG2ErjVxXJxVZLY69pUDSPB8nbArHKG9okYpCurVqEsQuufh1ucjTStJ_PPhiYfEmCXPEa-8fdfDHEe2qlQB68AO99CAVPzrvRluhbV0PlsdQdHeeZcfoHGfmdI0_43e9X0VOc1KX_r6QH3hvoQ1pWdf9Kf_XJPuXfO7zCwTrVPGiMxFqt7vKaDfzPeXpScwaePHjNhIFvnx5SN7k8Fsxj8LBnL5sPXCqWANz1zhbH3JV6wU7Ep-PsukqR4shabH4LuCPlDgLopXwOxQlPhYQ0RCtGq0-XuTIaUqL4Y5065bKJr2wGfRWvBWJ095UhoB5LSzOnG7BH0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇮🇷
#فوری #اختصاصی_پرشیانا؛ انتقال بزرگ درانتطار فوق‌ستاره شایسته ایران در جام جهانی؟
‼️
باشگاه اوساسونا به واسطه رابطه نزدیک مدیران این باشگاه باچندتا ازستاره‌های‌سابق فوتبال ایران به رامین رضاییان اعلام کرده‌اند میتونه تستی چند روز در تمرینات این‌تیم شرکت…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25382" target="_blank">📅 20:58 · 19 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
