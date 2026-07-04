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
<img src="https://cdn4.telesco.pe/file/JIQpRkqx9NoEyOi5Jl0u1L23smQd2f63yAJjQOI7E2VEAQlxNTBHbyTEAfO1_IqwReJGL1NMDUTkq1tMsllVgxZWCrXLglrNa-4cG9gN3A4H9OnlbGo1pIkcZTYbOMkELZmD_GUW0_yd6Tw2GpTfLJ18TvwOTo3H1J3ROlCEE7jY0CszWmQQHEHUTQcY3qDTNvJqgWPUpk6uqIY-0WtLSbYkpdMg3KQg6V9ACp3UWmS7Nt9RV7MNLHdqsdL1kdXnEeKlkIU2qOWA30MwM_fBlzokPHDaWpPz2inAolF060B_SqzudOn5XJRIxsEH8NNLBzBxmUiKzYtZvyqu_DdNUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 360K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 08:31:44</div>
<hr>

<div class="tg-post" id="msg-24914">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Qa7-pBrMB0NcXbcQDBwGBrKkVNsXW9S7rUamf_v3ba95kjxpeEKm3xsSpbhVnTczSv7QsylRFcu77mqmNRGjvfDSr7zwSCQxaOtro336NBq40e9QuX5YPv8BodkynzcPTeEizGOwebtkP0CguqxM1SCcxUjFTKA0uKfAAK3f5mvcvzd9x18yClmLLjvagVFOsfz7sfZNenWBILtGjDAuqatLwtGLBD_juNgkkEI_nOk5sS9VJeJhJxc3U2lR6mUIDANbWlQB2ZyFnRAldy4vez1DelTMnmCcLPe0gyp_3TlieEWkngTL1diCKDgmpcqCt0FTTo2jwwdFf6lpYHSz3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/579197cdd6.mp4?token=Qa7-pBrMB0NcXbcQDBwGBrKkVNsXW9S7rUamf_v3ba95kjxpeEKm3xsSpbhVnTczSv7QsylRFcu77mqmNRGjvfDSr7zwSCQxaOtro336NBq40e9QuX5YPv8BodkynzcPTeEizGOwebtkP0CguqxM1SCcxUjFTKA0uKfAAK3f5mvcvzd9x18yClmLLjvagVFOsfz7sfZNenWBILtGjDAuqatLwtGLBD_juNgkkEI_nOk5sS9VJeJhJxc3U2lR6mUIDANbWlQB2ZyFnRAldy4vez1DelTMnmCcLPe0gyp_3TlieEWkngTL1diCKDgmpcqCt0FTTo2jwwdFf6lpYHSz3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین‌وداغ هادی‌حجازی‌فر سوپر استار سینما و تلویزیون به میثاقی مجری صداوسیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 606 · <a href="https://t.me/persiana_Soccer/24914" target="_blank">📅 08:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24913">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=oliUuWK0lCX5I-DzFMJMggt4ISJGAXnnoJwX0LTa3TeG0F8Cpo8NMFYTG5NBMjxOiwDP4GIMBwtjV6Z762ZxIcU8vRElaX-fu_bldUeSqY9JMEcrKs9IKOhDvKig9a03fJ-dLyiWRQqfNF2phRCKkP0pLjoUeq1bCwZvZ5p1dlUYEnkPKqrhiekLUlaRZbHuqP-NK2h_YgiWgk5vscLb4wtEfB7fPCjjcyxUGoGboAOsdZZt6fGMBaG9m2pEi4FjsGuMtStKoO_d15nQJ5uZWHXW3LOA53MnE7X-ScLVKAPIP4BXHdRcHxgFN1nhxcG1WMk5SV3KRhuf3_vcRnKnZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34a4a83cf.mp4?token=oliUuWK0lCX5I-DzFMJMggt4ISJGAXnnoJwX0LTa3TeG0F8Cpo8NMFYTG5NBMjxOiwDP4GIMBwtjV6Z762ZxIcU8vRElaX-fu_bldUeSqY9JMEcrKs9IKOhDvKig9a03fJ-dLyiWRQqfNF2phRCKkP0pLjoUeq1bCwZvZ5p1dlUYEnkPKqrhiekLUlaRZbHuqP-NK2h_YgiWgk5vscLb4wtEfB7fPCjjcyxUGoGboAOsdZZt6fGMBaG9m2pEi4FjsGuMtStKoO_d15nQJ5uZWHXW3LOA53MnE7X-ScLVKAPIP4BXHdRcHxgFN1nhxcG1WMk5SV3KRhuf3_vcRnKnZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
گل‌های‌دیداردیدنی‌بامداد امروز دوتیم آرژانتین - کیپ ورد درجام‌جهانی؛درسته‌حرفای جادوگر درست درنیومد ولی‌کیپ‌ورد 120 دقیقه بدجور این تیم رو اذیت کردند تصورهمه قبل بازی این بود که آرژانتین همون 90 دقیقه کار حریف رو با 3 4 گل تموم کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/persiana_Soccer/24913" target="_blank">📅 08:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24912">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
👤
خداداد عزیزی: بااسکوچیچ تفاهمنامه امضا کردند اما به یک باره همه چیز عوض شد و مدیران باشگاه پرسپولیس‌درخواست‌های جدیدی داشتند که درنهایت اسکوچیچ اعلام کرد با این شرایط نمی‌آیم.
‼️
دقیقا صبح گفتیم که باشگاه و بانک شهر بشدت دارند سنگ‌اندازی‌میتونن که اسکوچیچ…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/persiana_Soccer/24912" target="_blank">📅 08:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24911">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLjllfsmuXfbcibNoi--GsrxTxLNpP9ioirNhlt_JV8JpBBvbHQr4WGbVzIEH9KhbOv_tOchEIblV9CNGqWI3KTvj_F_yLUHf1pg5sFGD0zpJSLBSwLx6UfVV4GhukRN1UPaxDiFjEbucj_-Z5n8GfpcG-1M9mSwWUw7ldEVS6P4e-jQMeqZEYWURN-tFxpd4TnvvzJJCaqJVYtK8Xg86c4WPWYE_Jyi8DG--t8XkA105Cxp1PrNEyQSl_WbM_jbj1uy5nxzveMFmoFkhPdPzk_7yXWWlewxZYUcdUC_ctLtr0-mTTwkeZtXNFPKXBKNf6TCxlsRXEGzhYaeY-e4zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دریک خواننده‌معروف‌کانادایی - آمریکا رفته پیش‌کریس‌رونالدو و بهش‌گفته‌روی‌قهرمانی این تیم در جام جهانی 5 میلیون یورو شرط بسته است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/persiana_Soccer/24911" target="_blank">📅 07:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24909">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/persiana_Soccer/24909" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24908">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kj-qI4HKsGGxE-fA7yIEyrYqSpOCGWzMI7zYsrjJLFME_FPWRaVRepQrr6EBAptnAlCW9587T1_uTkAdsGItUOTQd7tS-o1zmQThOKVDbSCsBWAGTHmijX66Sh3wA-MH5fje_KAM7q36n-E6ASRR6jkj8zDViEZACOto2JZ0nivWVFmthPdUSfD3TVTVE8z_ErLf72pK8s2fgqH8GPTSyEZ35Ro_5FINHkC0JwQnoykl1RD0RoQElucZoHgo7xyLiWf2FbaQjoBE24WU1yICZN1tWfhCFsl9gyfYgxbARoMkwLRtzuVGXmPII0d1pUgmnOm6Jcl3r7t9MQv6pKrDZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج کامل مسابقات مرحله یک شانزدهم نهایی جام جهانی؛ پیروزی سخت و نفس گیر یاران لیونل مسی مقابل کیپ ورد و صعود به یک هشتم نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/24908" target="_blank">📅 07:38 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24907">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GT5mubd8P7zF3mqZZZoRIKSxzoguTDfb3Y-dSxt9pmgAIzk3Xb7hRxSfuO7ZzHoEHaVkYYtJtQXc-gNwrhRLserWU1b5QR3nu8MzYJHvDKrIK3s3tviyWgTgLfCZ9FL5F3mPZLjiDGjz5HCPVxJ8IEyCWTGdtNPZGG272sidl7DMbKjyVepZOUZGLK2NRTdxgKwSeIIcwgARU9GIohh3U8QARkzScvUvRunQhgi9kat3FjGGWftS4CkgzEsqC3aAyBDv0pz-2vjg9x4KHzH1C3lRqa0FOcGG_inKn70GByx-4ddaUX9TLLEfqyZnNeGW4josBVGO_KqxrAhBsHEpow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی حین بازی آرژانتین
🆚
کیپ ورد لایو گذاشته‌ومیگه‌کار یاران لیونل مسی امشب تمومه و حذف میشن. بازی تا پایان 90 دقیقه یک بر یک در جریان است و بازی رفت وقت‌های اضافی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/persiana_Soccer/24907" target="_blank">📅 07:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmiVKSZd_Kf-a-DDbWxCXSMVeQYDxq_rsdTWR0TQPcK8Q8zTaOndnQ_YGg4W6VwlZASP5QmaEV3z183OinExzdBRsSYNh_sFjVTlbXVhU78w9pvs5p8u8YC72BRmsZix2QQwQfjnEZB7UYCn_AngxBSYPB7VLazTmH7Hv9NMowik_ZXKOY7BS-fCtVhIIzaFUZCpDrMExjJHU-xb7mNgtu29CQLwlJFlWGgnpolSUHdm_snSWejhAIGs7W_nE8OdWUf3PPtd5vZId7JWkXsLeq-i-Ng81YiEHeV0iqkUVc9ac-TsVrM3ZXsWmFzxAfPsvDxpcf85hTYkjGNfED2gRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXlMCQMZ3SS9P2bKTPwajWgxciKFgs1deA2POZVCvvNykoXQ1K2EoPINuhTDzJLKE_MBiZOPVrucAMom0x2onMp4VKcqUu9GNG51AR4RLjy3E57oEPc2yFoCAiMxBjrLqt94IVdLs6pAmO32gW7ZSVSBdFA_GZ7hxNOP3KZAUi7ew0gUI_8w7oUp5NSql689KPLEXlRnrljUlVYUuR2t-mFLy4Am6PNzzPMxXEAKW9m_sFUadDKFdlpbXzhkoaXTI40Z7LcUAB1xyN3CUotYTWrA_PnolaDs_J4SzccLfxSsiMIIFE8btJHf07vs9yKBqaHkKG7q7iF6jSAtV6zl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=Ufgi4GB9k4PjO2ohhy_4K72FFhE4ZfiBaMtTUatuEhQIn_BUdN6-SlRAx86q4-PhvBFRQP_syvEpA36sncAICpZz-vMKQLjBEegG7WxgjS2AqZskyoqIBPbIazpYdsmnK9CeD03AOX55sfiEqclU3sO4iVrKG9CG8SByC40RtPPY8rEvR8TQvX0RTv-LbroK7ICzF9h9mC6_BBfk2Wytfq7g_t7EEP7nboICXy6zW5O08aG1YJD33ODL7U8HshPoU5QV-yZ1-1-MyohOHbHIcC1LtHPV4kZhDpJ48EyJazmIiY1MbQD_ybupylK2G0yXNflLTK4AzfwP5LsgkYh4eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0965bbee9.mp4?token=Ufgi4GB9k4PjO2ohhy_4K72FFhE4ZfiBaMtTUatuEhQIn_BUdN6-SlRAx86q4-PhvBFRQP_syvEpA36sncAICpZz-vMKQLjBEegG7WxgjS2AqZskyoqIBPbIazpYdsmnK9CeD03AOX55sfiEqclU3sO4iVrKG9CG8SByC40RtPPY8rEvR8TQvX0RTv-LbroK7ICzF9h9mC6_BBfk2Wytfq7g_t7EEP7nboICXy6zW5O08aG1YJD33ODL7U8HshPoU5QV-yZ1-1-MyohOHbHIcC1LtHPV4kZhDpJ48EyJazmIiY1MbQD_ybupylK2G0yXNflLTK4AzfwP5LsgkYh4eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛ شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBDsDFkUv-MEcmMZ_VzTas6SosvvyuxtIxp32VP0QIv-biCsq0pWXR9RW9RJWC5BP2WVFT7feLVB1CZwFTLaTvZX-XHdTkRMzegSSDiHLN09k4GO2ORt0G1c-yjEJk3clyyp5fzWo76qPrqGbpQxNodY42ZcL5QD4kYIQIBQkhPaJcQ-E9drSoYjj9A1_vIFW4i5OkJ3-T9wptZgR46srbya8i2PNpb-LL8KnpydY-N4fAV1yCsxZ0AibI35dvVoq1NZOYWGd7dv4Gz9i8XCmrmsk8fvGgoqvyJx_uWjEn43zYMFKoZzrRlruQQpSL8KV9E0HbFdlkoHJ-2GjwlWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ3m8EBCRxGPCPS_OV_Li5DZ96jrXENx9fSZIb7v1VrAk0DOxzoywRJWlmdHJe-NQVIYxqckDEHiriO4ImB1OzsngDclGuFJFVJg8Fkb7Jy34QTWXQMEAL2pwxxM-GohBMs115tOv8DWc1pSKkQk7dBgpsX3coeLwnfTuFdLzLnWg-RMEAaUX4QRnKPcc9JpsR1IXJxyMxsBc73WoAghu0bFXqGug2hv8KJ3CPJh_t8bxgVAPiWoaSbctFrSIQiW8jkZoSvAAwPhm2nd_K_oKYoJiS-AovFnm_pebempJP1Dnu8F2JJad6keNzk0ohIwBYNTSaUaF0cxQFieI18CyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUV4QWK8-GdRfRu2dzDVKXBX-4CpINwBBjWrgKFtVRbPTNTTJcdGmnLSjEgHa7WZhPOablTiey36HQB6Ns8rE9SS0LJtRFLHHMDyiKHHj_mHQJ9kYTg7DRSOj8Wr7n20HakWe5j_5YWUXhZDGqkZkdlWFCa4vmUxizbQPni3umksLzeKNn1hMSUG1RQZcyO_GBK9raXELbA5G4GQg0xSNlF7n2JpPtnN-Uv3pg30tZ7FcM3YabPaM-U4saFjeg9v5FNRQg3cHk51BBgmQQNC-LrLgU6Jo2dWRNuuE_fx0FxcZVfDfWeO8VLVNmoIxif8TSZD6rFqApjzfeHYD7BQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Hgf9fxLNhq0gF66M1clv5oN4ygh3PnPUj6fIHVRxr99ZHsi-O9XUmz6bkArDGVBaq6OlwP7_Brfqxo0_lSdPfFuXrwr5pgyuNSsAlKGZBKUud2DY176sM9xsxDWbEscG6JdlUywSePsuQWcscYyWp2XSJPb8Uae6a6-oTtPoC9Nn_8-WQvp_YI15uoReywQX3kVgbUYf09imd_YTQ_ieT4rE_ij1eLku2MH6z5bZ2dv-aCBkQnDMFIGoP__JMIOQN2hBkuo4Jl9iSz7pUOAvxwhjSjgBMh1mFNea-tMmkGmvrGfff-uMwosV_NeF5F3fv7JBcpErn2lB7nUomyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XbEm1EMMQ08_opBMmiIEI-u27AnO88GTp6F7VhN7XAWF2ttqPa41KYomLUWDQEAs4XkVGDWp3HXVMwCLyAREdTDpSGevGlTMn7UrQHGG8AXhWP3Zal0HI6GhQBxfMVxz1VdyE9KftYMRvxeWC0pK47F7O3-kvtexiLnhyz6HAdsq3BvoIuULNcqF4h5_0Lq43XTnCzWcdycIRtDUuEz7HUMjEib9DgP7GBupTI4vHXB86vuxs9zN-jmP_pn3osUxYnct482NimCyqVxhK4_ZhnieKTvk_sGNx3vAKqVePnaujzmBdWpmP6n4SwkkfOOdUleps2P2GR_WSOCtPdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24897">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/24897" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
با این سایت به راحتی میتونی کل ضرر های جام جهانی رو جبران کنی. بونوس هاش واقعا عالیه
👌🏼
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24897" target="_blank">📅 01:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24896">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lBzoouCLUWk_j2NCqni1KD0RxkVOLsjhVkxYd1pzvGOM0VHtW_m5sTAn7N8q_1OPrtTKw6XdKwh80kY2wBGL5pXubTOwtx_OZkGhEECLjVVskeATTQ7VL2Z6lEyXKYAkDxs25PQPXCXX6AWe4KQB8CH5t8NFu56V2ilte6CpLFZUK9Glwrv7deIAPq2FWISyHogr1mEKsnqE5olrl7MntxgM5ueNEWdQNwfAaFexvnA2vPwH7PoF47StFJIwwLR16LWIVvri5jVaftd_x2jMyRznzI0GpnPK7nJfEN2yE6-yrnvOyq5p3imgKw17iBiNMP3nATBH9LQ2KjBBmONFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
توصیه میکنم بازی های جام جهانی رو فقط توی سایت بت اینجا پیشبینی کنید
🅰️
📌
اینقدرنتایج‌امسال‌عجیب و غیر قابل پیش بینی بوده که ما تصمیم گرفتیم به شما کمک کنیم:
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
a12
@betinjabet</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/persiana_Soccer/24896" target="_blank">📅 01:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c8ce51440.mp4?token=plX_JuxoxyDaHSe0MijBF37xbQ9YJkCbcktYlSieBkruu4scHajgpdhrReuwxF31EV5UnG0GvpIY7wt71tOmOO9UnChSEMHl2vuqzlapRj4Cj2Kg9_bssQHydd3z_1gzAqc4omEhCMlwSrZNtEUs8iCeeKR_WPhlGPeko3eV7ZazxahN6USuqKg7x9hzRi3SNHXXUGpu2wjKAE_htdz-2LIImpYoB97WNVyAAcHLgmNpNvUJGCdjbwUcuQXvJ6BpDTnuNxxmnWMUdbXlYG0_BKG4PxDNEvtSs9JTdBEbjoKl5FkTgOPT646F0jV9fNjUutvJFUniJUcyRFgNd_QuTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌ملی مصر امشب با برتری سخت در ضربات پنالتی مقابل‌استرالیا؛
به‌یک‌هشتم نهایی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SxQ3FrKx2JJJivBogD1S4G8W7qYv4CwuY6A2IOt4TcLoYJa_Ut5eBtEBO3RxAhcgwYe7N8sr2-nHpQuS-lp3vBXGE9WLxJFB21-I5-CLA339BQzScYNu6lT9oaoL1Ha5OYP_dh2VKVztN_QtAN4_Yd6n2YJM4wZMomtcZe9ExcrSR8KA_0_vz8PtyZ1A5BtoS0DmFi8_5noROfI2hqstwEg2RJf0aaK-LJ9VXyO_b8AzR5H0EIe6r9pmXfAxFP_PUqvhaZgp3x_UCtpKXvIc6G66W_cfSeMXNkZ4KC3vDPFeeMp5g4RVAoMGS8Ugmci2BIYZMnFhdLadT09_BPygxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rIxl1cQP_yygWpZoM5XZ-z64Z2dqZKUWzCPD1MVQADkeezR4v_BuDOZ5BoyXy1YrRy4HqqXYqkCV3-MMgUGFspb1sxUabvHhiYfVTBTN58f78gnih406ipPQCCZpkI4wHirefmVqwnMMmGlP8jKa4zAWMMsGnvo_9r29G8rWQlhzWze4q5DCqJFzfkJfPRvBfXZXKLAOV6y5OF3MBj8tnQA2vjK4v4x48NPBiBmUcL-8GmLTN2wRQMp5pzF1fJp7vNbWELOKjFKsdYWHhWzgOj-1Gbocn2uretZVA-DlIhqHZE6ZGhUHMj309Gb-c2h-RagMqFj3cm-aV_8TifxqBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌ شانزدهم جام جهانی؛
شماتیک ترکیب دو تیم آرژانتین
🆚
کیپ ورد؛ ساعت 01:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2OZkRggAtQIXwnH1WaGccO6_G3AElwlq0Jf2zBzaxP0mBm9Q3ruAB2zyoNceM5IHkX67xx0snb9iJFpMXDFKbb1VPxOEcQUo7LyDZQTphJOmr7-TQnO2TJ5Ifg1nOCMVZFVCWwMHsl2hm3x5e6qhp4ms6SMy7skZ3qCnLJIGS4vWGuAuTc1sy6tGk6HyQTAWYGUttY9lR7ZcqCnUq8DrWIYuutsbcirZsYdQRHBowcrrvCZfRA_LXLK7qmVo8O3qCDXTW3ChH_g_RDGbhPQWyK8aUtzxqBjqpGCGImaPUTyVi4wbSigasTwntXeL-L81LL3AjyjLPmVeJ2GAU2LeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGaaE2O5eSUqc61cgNXsuyARlieWXVdUPfvKDETzhgebqZQzj2baLQTYe8gy1vCxWvEic56t64t_jRajmUR6xRnDzRV7AS-Rr0ofIlqaq-S44jtQqRlPJ_csw67IEM6eRnUg6dOXaYVKJh4tM0g01HSThD-K7HL0FxXqmnDAvBfzuvP0BLY__kO4SnLbgX4HPU3u2x9LgHXQldGOPyngOZgsdrsdQg72EA3EpFhAxN_9drEjv6Ba5rogeYgUkuiXAwmfKUkJWLrIuynDQUh8llqmG0c-t_W6M1nsbElpgkB2IDH9Z98T2pnSrkrB0n4WI2-pOI78qmpziG_HDireZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsUElJ4kEmDTovOTQvhYxD41_rLQNv1wiGk_FKfWn59-urN8mi6mnHK7VnzkUHuu66hcbDvJMTpv13B-xOasbTzk19LrbQJ7KSGIIi7QnOxhqAhOL2EyiK0BIiCTj5jiqKQUPyUFdA69zdpwDEx9rNTUtCxs_EoIqarFlRFN0jweEmgSv9yflR8u4eW5DWmmdcIC1qU2BhfmPKoBjvIMBSU0VPlFMLojoWPhRqx14yFv4Azo7nJHxeneCY3cP4jIrAOWgEXwGEwT1mH4_nLgsAgu_J6cXtN45u5-rPXkrxxQerXBQUzOVKdBMeYcKKWXpmbFUeomPph18hJ9watvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO_8rJU3qwUeqycduwFJI1-4oF03sB1krJqGnDakoKHjIYf9OTNPAbaRbedzoo1YkUTls9Sy1SfWyqNhGXbAUEgkI3Mb_Cmblz73Nwnyd1CHgCB5l5Ov1kYI9boOOgA2BoXEs0fM6DdOWeOpc5twGJAfIrKdSgdlDY50Ey5MJkKHlSevXUvWRrmsP-wEdaaD0vQoY5ZyJdmY9_LYS5UWEMItH0y-VFmfj20CYfe2PaxwL8UDdfEzSqXGxOpRoeHFmEojU6dOAXDr99Ayby0Je80kxG3BBbsoeJ_hdaGATLQYqz5Gz_W_GwDNCnj2geWviE3A2D_lDhnOVpPaHyQ8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r48c7rKX2P0D9KML4NLF4PeBd8Ykvxqkompp17-A5s9kmR2N4NM36RXFpaziQI4VU8AdCDaoG9tZT5gptKbpfZ3gETet51Vl8oY2F-VAQr07RYNT-av97h7t88q-1Xop2vLEbpoBQSrJnAgXMtXqHdI2aYtPcneaxd0-8LQ7V75vSBkABVQW7je-A__e_0HWlzn4fDlrjRBAToJH3koUx2JIIrCwj9fWqT2mc0z3PniJAmyYRGhMazc0mO29sRg9HLMID8Mz_csAMRNRUCQPrue4tUthc9X6PdIwU5FpWQ9lrtObKNRPgB5-y4z67Nh8-VbtgrBd9908UZuvbzQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHTwD5F0k3TC5lLObNGIGmLs4oF2SHrbBzmRkywxIsuw6Wq1_rESuGoUn-G46LWs8W2j-qZ_cqZNZDKE-ICrbA1OpTPpkTZmUDljX_UVFuqM0ghn0hPtDXohKg1ToC7GpeFDf097gUE0DWYckSw2eWZZJBZQKeyfKrQDvddzq77SX91Czib747bOrt5femvg3aHux3Tr8UWrq3JyJxBAbmVJhpOzvrryKHX7Qk24Z7tYPC6a51Zd5zK8btHYcqc8PDQHSdveh56jXXBAvCA9wr5vn8CCK-wIv-vcJ7xoNGx-YypTgMNi6Vy2_c6cTxh2h8-2qzKAoTNGS7N9kHKhIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه لازم نیست بین انتخاب‌های تصادفی یا تحلیل‌های زیاد سردرگم بشی…
🎖️
همه‌چیز برات به‌صورت پکیج‌های آماده با ریسک و سود متفاوت آماده شده.
🔝
فقط
پکیج مخصوص خودت
رو انتخاب کن و وارد همون بخش شو.
🏆
ویژه مسابقات جام جهانی فوتبال ۲۰۲۶ | ۱۲ تیر
⸻
🟢
CORE
📊
انتخاب‌های کم‌ریسک و مطمئن
🔗
ورود به پکیج:
https://betegram.com/share/betslip/ZKTRF62467
⸻
🟡
PRO
📊
پیش‌بینی‌های متعادل با سود بهتر
🔗
ورود به پکیج:
https://betegram.com/share/betslip/VGPXN72923
⸻
🔴
ELITE
📊
پیش‌بینی‌های ویژه با بیشترین پتانسیل سود
🔗
ورود به پکیج:
https://betegram.com/share/betslip/DACCB49184</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-D9cQgTTkYv3kUsbiyAag7xF5uxj1ph2pU9D5seGWTqYM-6uO9y_B8rWPXb9lIjFElQyQU_RahdEJ34RW18V1HkuB-ooKLaoL55NASpfFEnYdiZyp6VHIN_LCl6fkww2ILO66UwoAujrWwwzYcrlB-eBAdqSg41ovtmD-X2WdgRFjLvMK-_x16SQF0gik5PUAbgX5TeEqtG_q4KNd8oUI41TGJBsGV0xil7aTYuDb40r24c8-yGntYZ_DHORK77UD-eetdwjH_2WzviOOdpM5QuFU9B2mqmrzk9fnd_aIQ1Oz7u-p2c5KDjONSGhh9Zz2bhGuhNEbgHQoKkT-wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fee6a7d4a2.mp4?token=rN7n9BFrkI5Mcp05D_AcN09g4up1DA2drSSbT6eueeK7Jpq_d1i5q9Ffqwjt5Q6abGNTZV7t043Q2Xvzms-RjxTMdyxYEC1P6wFipr_AxG5B1hGVDzMLqferNy9g7h1p--F20A0Vgwr6TYe0yd_BTiKadCDvxTAN9w74ED0qGZRx4o0vFcUNCwXtTR_CjeFyKB4WY8Nn6loFZcv4zsuiFQfxqMMNJI6YzDXDlhK9NmauMwkb8g9eN9Y7X8q4MIsLRUvrZF8ZXFUQCEc97deq8v_IMGwQE1ozd-FcVhZVZAp7jj8cJ6q5o1F9y_jhfHAu4fdZLTVhYaU8KqnD2s8PeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
بامدادامروز دربازی‌پرتغال-کرواسی‌شوت Cr7 به جایی برخوردکرد که شبکه 3 مجبور به سانسور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFO5eClSUwA3-Eyvjq4pK3-Jjlfrt_M6pHcuzVhBgHSPEESQI9f5FKRCafWZoHDXRuzD_RqbOlJIvLRWj8B5rT5BFB8q3k1YzKdOVTOeTuQfqQXbtM706x7Wa8lhRz9m2OvtkRFRKSH3JnZdo9vKjz5NVI6i9-pwuuhVHAn4XWefz5qHnWgcYMnjf1pZYTyrpT3YrIslzB4lh6a0F4Ok69LAe49q6VEUc2tOuRcRSSbOgOL38tTc44vlRKYYRv_NPjdJpptAoXWyZolLmvvad4KBS-MITBwdAEPLBkrMwoqion7PA3QlRS92oQ8ALi_5rzZaiyXaoOIPy_Qbq6eIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9736fee745.mp4?token=twFo3qcPkTJuCG33snfr-B_5d-NsG7yQ8rdjTpbFSacusQuMeDaGvG8MIOnzWxgnDnSEVy-4X_lZhsr1GetdGBuJa3am1ihMZ-sLU-bHMuWiA4QkBwn2RfUUSYDKegE83Qk3NGq4StWajGSDfAwaPPwaBkjC__vl0c04FBUWrFPCBWgTCY1UATH0K4w53_hV8ObhmLawOSiu1qOVSwgcHfH3dLfiFwsKa6C3CkTw3F1xaHgB45zRn08IfWVKXRI0Xw0oY_ejGyCY9qig5vYdsoCgnw6BZCrlbmrRga1kjEvqTgk3HOc3mVib5EF9bSNuhC2roOWowLqm1jPo7W5PSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9736fee745.mp4?token=twFo3qcPkTJuCG33snfr-B_5d-NsG7yQ8rdjTpbFSacusQuMeDaGvG8MIOnzWxgnDnSEVy-4X_lZhsr1GetdGBuJa3am1ihMZ-sLU-bHMuWiA4QkBwn2RfUUSYDKegE83Qk3NGq4StWajGSDfAwaPPwaBkjC__vl0c04FBUWrFPCBWgTCY1UATH0K4w53_hV8ObhmLawOSiu1qOVSwgcHfH3dLfiFwsKa6C3CkTw3F1xaHgB45zRn08IfWVKXRI0Xw0oY_ejGyCY9qig5vYdsoCgnw6BZCrlbmrRga1kjEvqTgk3HOc3mVib5EF9bSNuhC2roOWowLqm1jPo7W5PSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
وقتی‌قانون‌برای همه حتی لیونل مسی فوق ستاره تیم آرژانتین هم یکسانه؛ فقط خنده‌هاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLL8i8LVVNPFKYZPCNlkS7cfbMdalgA1bx1lIMkHVLLNeHdW-tYdeYaNO3a4ToNVRpBqaW4nyJwq3KsvBjToReLZ8dFLibk__2iAbOACQP5T-WclXBaRR1hJYMPjdMXU3JAGOt7r6No5tv4ytkZ6T9a3fd3Epw4OwTHQNvEfDAPtu-OV_4BWsmwXCxW7n10bjKCDm3HVqcn1DfcKWIDLfvv9s68-DTjX4sQiDxf52wXFTh_Mbzt2uWCrcZYys75cjDfd0SNjKoW-ezT2xR1zqBuySaSIl4MfjLo9lLNABoTK1uXcDswOTYmNyufjg-yz_XKxwPD1ht5woJelauNjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/459003d30a.mp4?token=qLMFYRY5tPIH8kbchTwEtJLXwezjQhuluroqu0f3wI_8i0Y-VaiqqTyc8ECfv2vaXIEppQLReA_DPXrTStlA9rkBD95ZVl9W8QrTBWuTE0tF4Zb2dM_CWQE22dDeu4eQx1c1Hz9cnhMAuBxTlEET9w97hik9WuBAEno8qN2YnG4hpVADrsrbLgrFHsX6BqLTWIO9g0Aty0Aru7Tp74V_FB0W-Ns-pMuTnNkqCMA1yRyIRECG_F2XwtcZmimH3VSQrgNdOzwAUuK2_lpqSKBKSKxNj8L82lZUmn5nNPWmIplSkEaASW3DkLtZBkKSIXNRZpCVRJhL2DOzQuVNQDdyEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/459003d30a.mp4?token=qLMFYRY5tPIH8kbchTwEtJLXwezjQhuluroqu0f3wI_8i0Y-VaiqqTyc8ECfv2vaXIEppQLReA_DPXrTStlA9rkBD95ZVl9W8QrTBWuTE0tF4Zb2dM_CWQE22dDeu4eQx1c1Hz9cnhMAuBxTlEET9w97hik9WuBAEno8qN2YnG4hpVADrsrbLgrFHsX6BqLTWIO9g0Aty0Aru7Tp74V_FB0W-Ns-pMuTnNkqCMA1yRyIRECG_F2XwtcZmimH3VSQrgNdOzwAUuK2_lpqSKBKSKxNj8L82lZUmn5nNPWmIplSkEaASW3DkLtZBkKSIXNRZpCVRJhL2DOzQuVNQDdyEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
طوری که‌‌ تیم‌های حاضر در مرحله 1/16 نهایی دارن بمرحله‌بعدی‌جام‌جهانی 2026 صعود میکنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kctFx9y6vq6jHuQ0F_cBjBd0ijgLbgcA_r51UNNsN3PvvwSK-c7KCD6Oksl_zrkxtujf-GC4ZkJ1hfVuddw9wqmKBtuZcjTWhPCPYXwcgMFp5MmUV0z0y6YjfbBjvsyJWMx10kKTnrW8TsaudWpMhQu8MrONDFVZwYE0gv_l-ccfywQWuQGJ5p-3Fd5Pd9dU-9_sfdTUC876iWcOsKHWq1jFelq-UDTxIy8yU9JVGvc-S6OQYPa2TNYLsrADqUiiBCLOSvVqwvs5sScCihCBJtdWYDirWEcYGssq6vbhWpt90Sw9ZUPYMsDxbOcb1kAkY-aur4KGBB_i8bTLctvl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=SggQ17nQTYE1I7Spyzx9XkAeCRHU2gGteYf02-EpFbjMhU1BfKGKLZmLVc7nHUoVSPk_c61pf78bkcwGXliqwLVEDGc1DMsFVF_t_88IfmPyQw6oB1A7XE1vaXQi-HiscI_JoC6PjFsI_6Tfha3Jye0qRn15YcZS52AKT_5RpXafMaRRoMFLLAC93ixxTc-9vpNT7V5-nZOA56mnxVFn_ZB4pw28EG0TGfftIP48JJtpNKyoG86pXjB314AwkYko2vYrZQW4BlZPA00-whv3aQ-8Pss-mT_nC-3y9I9gIGdItFB2t2MHcXyzkD6PRsINh4LFOWot_WcdgQN_qkzlcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/376f8db7a5.mp4?token=SggQ17nQTYE1I7Spyzx9XkAeCRHU2gGteYf02-EpFbjMhU1BfKGKLZmLVc7nHUoVSPk_c61pf78bkcwGXliqwLVEDGc1DMsFVF_t_88IfmPyQw6oB1A7XE1vaXQi-HiscI_JoC6PjFsI_6Tfha3Jye0qRn15YcZS52AKT_5RpXafMaRRoMFLLAC93ixxTc-9vpNT7V5-nZOA56mnxVFn_ZB4pw28EG0TGfftIP48JJtpNKyoG86pXjB314AwkYko2vYrZQW4BlZPA00-whv3aQ-8Pss-mT_nC-3y9I9gIGdItFB2t2MHcXyzkD6PRsINh4LFOWot_WcdgQN_qkzlcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
​​
وقتی بعد دیدن بازی‌های‌تیم‌ملی نروژ و تشویقی وایکینگی‌شون‌میری‌باشگاه‌وحرکت قایقی رو میزنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97048a0557.mp4?token=DXaW0k50V4AWr5Q4y7rW-8gWFuQd3DJtgH_l8-2XpFWtccVtBIwsI-SlBrqnRfGnlutjbo3PPRDy3ncceSh39cYR4v--IGowh1e58Ms34m2mjIwoyylBwkV_2W0TH1sm3a9Q7jg-6htKsjLxQZzmJmMeeA3yMt8nwNHZ2DHeAEGcyDejyg0YJYk-zmIZ7RHe044q42v465D3jWjoe8LOHdO4WN5YBOMrqTBOGkonMWiEc0JLQkjV245i7OJYyROJu0zbpnmvNjphKwqOghLrd0V9H-GotivZ1DZQ-u1iPMKCnKZPqstu08n8QagFHLuZvdVsadSdyb783CCQkwaK1oH40_rYQUAkRJSTDe33oNyllvTh3o2sx--RKPJLq5_fcz7zbFWomr01kyM6oOpPqI56gW7zg2WCRXvcuj7Vxz6oY7-sPHliL-qPve1u12RKPr8pERIvPe9tkg4vTdPUVaM7z6MjT4bhYNIQ1FuN_5jNehakX_BvDKsHIwGOyW7Hu0AK8PzlRJIK1tbelSnYiGNxAqJ5EoyswKAFgCMzo4dOnTeIb6DCtb1yllpo0Kmy6d6FD-SM9LmBOPr6EjMKNZXKtP-IrAj-2sNyTZ1CnemqwrO1JyCn1IwJzaARedsEF6Y2xgp3H9tpV0roS9tdompILjSCJOckyCzLn82xThw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97048a0557.mp4?token=DXaW0k50V4AWr5Q4y7rW-8gWFuQd3DJtgH_l8-2XpFWtccVtBIwsI-SlBrqnRfGnlutjbo3PPRDy3ncceSh39cYR4v--IGowh1e58Ms34m2mjIwoyylBwkV_2W0TH1sm3a9Q7jg-6htKsjLxQZzmJmMeeA3yMt8nwNHZ2DHeAEGcyDejyg0YJYk-zmIZ7RHe044q42v465D3jWjoe8LOHdO4WN5YBOMrqTBOGkonMWiEc0JLQkjV245i7OJYyROJu0zbpnmvNjphKwqOghLrd0V9H-GotivZ1DZQ-u1iPMKCnKZPqstu08n8QagFHLuZvdVsadSdyb783CCQkwaK1oH40_rYQUAkRJSTDe33oNyllvTh3o2sx--RKPJLq5_fcz7zbFWomr01kyM6oOpPqI56gW7zg2WCRXvcuj7Vxz6oY7-sPHliL-qPve1u12RKPr8pERIvPe9tkg4vTdPUVaM7z6MjT4bhYNIQ1FuN_5jNehakX_BvDKsHIwGOyW7Hu0AK8PzlRJIK1tbelSnYiGNxAqJ5EoyswKAFgCMzo4dOnTeIb6DCtb1yllpo0Kmy6d6FD-SM9LmBOPr6EjMKNZXKtP-IrAj-2sNyTZ1CnemqwrO1JyCn1IwJzaARedsEF6Y2xgp3H9tpV0roS9tdompILjSCJOckyCzLn82xThw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
و بازم‌هواداران تیم مکزیک؛ اونقدر ویدیو‌ها زیاده که باید هایلایت‌کنیم بعضی‌هاشو بذاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a06e45a5e8.mp4?token=JtyMMcQ_3HqP-xvF-AbNlbqrizvh2lF0pZv3swGi57N7B59jED7gsADx0MXGKjK2V4Xz6lox2OQ3-4mB5YrzZ_zXs_LO7w-BGehN97AuwKoQyxmZTAqrTrZ3-Na1fznuZsVxe8Mu_mNZ2oW2dpagYbSY2IpAIHghN-0qmMcGB5uK2fyFB_ggKlhVmeZIgSMXfZW7yrO8Q-g9NxWw5E45_1laoWOZ9N8Np0GIfWLQFZ3wQZiFwOfyom9odFNhtrxQbI1IJRIufCT3B0pl9Pr1MxiBYk5YN1ZfG2R_s4Rh2CJLw27_m5EFpk3Rty2RiGD5N8_cHIl_8aDSWtRZiD4NhZx-dkd6FMoIpJ87G9mpMMJAA-v-Oy5Tv_CfrpctKABWYnbckCqpl9m9A10PmnUpUsgumxuRKFVm_I6a5xV2vAv2SslD4w75W9BFDN8aY4UBJBGOEP1OjnaRvfq7JddyD8sXGrHcfCvp1q3nWMGyNgoNcQTGfMfiMI3H1ccddMmfWheTxCTOI_FKyzEbNJJIEglTMJcEPFbsDi00b_un6gL0SHLHddMpFhNtoRBotZaC1_HMwRyE45yM0iIseUS8IHtChxYd284tljKXeV_Zl2TLn1K2gj-PABcr6FDN3QoWfZqKPl74FrcYSz-cCTwjMImi3pv1bGl_neWdaaDXzeM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
گنگ‌ترین همکاری‌تاریخ سینما؛ حضور غیرمنتظره مسی درتیزرفیلمSpider-Man: Brand New Day
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oodpjJFj2oF3Ny-rBtz1dkwKSBkMj4JZGJ0a2mnBmBZQ_A3I2NKOo8f5qxgBAJ6HH6zyNWS1Rpja1L8-X8NXD2KImBEzrb_7rodM8JfDJ6vzoWmTeqz5LR3sJK90Vi_NX5iRG9ftWl6QCVIRPe9T4sWoRMa_zoM3_zKV_bx2xWw5kWH63GbsAzf0IkplIdBIqx29VjX9k0TY8I3pcOniYRCzdJxmsBYED_YlgeeDNztJOdGClLi_qGkX_fj4yZBFtq45R1ptHC15qwy2pJZrjTKBeEGZWM6uxUbyxaCl0bKyYxjfpdoR-7bFbnPxpgWXEi2acKaZJ2kSpgx-nzqYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=Osqb9Ra6Os9wXshHOsZ_LOiKt2cYXTP5r4-64TEwNJhQVJ7nckd_-SIndUO57GU94TbbHnoYa-k0NakOEgN6KP_wL8HwC2nJhk1yWFMclxDu2lH7hY86GCZX9okfHcGcw6EACZSfi21LB9r0qpdAyroMz1AQiZSfg7Sk5uvL9WF2m9qe_Ptd4yfgLcycf2JT_G5mLern-jqOjZRIEDrGjAewwTwZD2OBAXE7FR_Q9C_QwCZ_JKIFSDSUp24xp1EChlcQ28kgVE89yvZ1UzqDk_s-5_6x5gvKJrnpdvhRJgOYEEFH8uTBfMxKRJK3sxabAxvwSqOTSpYE2dRQLtg3EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0d41c219.mp4?token=Osqb9Ra6Os9wXshHOsZ_LOiKt2cYXTP5r4-64TEwNJhQVJ7nckd_-SIndUO57GU94TbbHnoYa-k0NakOEgN6KP_wL8HwC2nJhk1yWFMclxDu2lH7hY86GCZX9okfHcGcw6EACZSfi21LB9r0qpdAyroMz1AQiZSfg7Sk5uvL9WF2m9qe_Ptd4yfgLcycf2JT_G5mLern-jqOjZRIEDrGjAewwTwZD2OBAXE7FR_Q9C_QwCZ_JKIFSDSUp24xp1EChlcQ28kgVE89yvZ1UzqDk_s-5_6x5gvKJrnpdvhRJgOYEEFH8uTBfMxKRJK3sxabAxvwSqOTSpYE2dRQLtg3EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پدر آقای‌دسابره‌سرمربی‌تیم‌ملی‌کنگو در حین جام فوت شدن و به ایشون خبر ندادن، بعد یهو بعد باخت به‌‌تیم‌انگلیس وسط کنفرانس خبری یه خبرنگار بهش تسلیت میگه و این از همه جا بی‌خبر قفل میکنه که تسلیت چی؟ و با یه حالت شوکه تشکر میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OJgIJxFgbLBSIma_xot0inPvxLdvZnHrLEQ_hIG6mrG2WTzzwC4OgJ4h216Bg01NH4PbkaPU3r6bRB2jBEQ9IZbxfQc4o9b5zUF3vQg-1q-cimWm7VGbMsya1WCgtdwxp8ekohb9NL62SsxfSpX_jE8YO9M_cLt9ufA0bpuuLRKTG0WH7Rl5m--ukqNDRgdIKhZQKJk7idKnbuGtRsNeH_QTz9l0eMTUztnGUlXNafEhF4EzNTUQsqQblBndv7-dti0J_KbV93IfRw3Tjusnez4nFBzVurjzewo5bnvRhb6dly45xrFzGS7_M9J2y-DTHwZxGbVEwYgSUpeNWksG6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8337fefdb.mp4?token=OJgIJxFgbLBSIma_xot0inPvxLdvZnHrLEQ_hIG6mrG2WTzzwC4OgJ4h216Bg01NH4PbkaPU3r6bRB2jBEQ9IZbxfQc4o9b5zUF3vQg-1q-cimWm7VGbMsya1WCgtdwxp8ekohb9NL62SsxfSpX_jE8YO9M_cLt9ufA0bpuuLRKTG0WH7Rl5m--ukqNDRgdIKhZQKJk7idKnbuGtRsNeH_QTz9l0eMTUztnGUlXNafEhF4EzNTUQsqQblBndv7-dti0J_KbV93IfRw3Tjusnez4nFBzVurjzewo5bnvRhb6dly45xrFzGS7_M9J2y-DTHwZxGbVEwYgSUpeNWksG6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=WnOe5Nnp9h6k7ylJpMeh0_jnoq8YsXLFDU7XdtyYcrs57ycVQ4YIcsflHvr-p5T83Msv32hSPp7qv3NwDSDE47Fmw3m01C-VCSzF-ciqdpbnYTlZ319c7AWcSJAyq4d7APzpLwrIFxDrcf7EUGP5dg0KbTYfwZJIwDnDMYfsI9FplxcDd_jU414H9cHfc1335v-NFfVrRUT0DOx0pxP9KDjRHUQVcQ2Cmr7khA_tb4V-_jFnqAHKUkrzGl6yEpSIbJrARHP4d_1fIfadtmqnpAyYFfs-vzsah-U3W6gb2SJNVRWIXJviCG7CJxtxyFNh0ZP5wecxQLVxZDwefQcZ3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=WnOe5Nnp9h6k7ylJpMeh0_jnoq8YsXLFDU7XdtyYcrs57ycVQ4YIcsflHvr-p5T83Msv32hSPp7qv3NwDSDE47Fmw3m01C-VCSzF-ciqdpbnYTlZ319c7AWcSJAyq4d7APzpLwrIFxDrcf7EUGP5dg0KbTYfwZJIwDnDMYfsI9FplxcDd_jU414H9cHfc1335v-NFfVrRUT0DOx0pxP9KDjRHUQVcQ2Cmr7khA_tb4V-_jFnqAHKUkrzGl6yEpSIbJrARHP4d_1fIfadtmqnpAyYFfs-vzsah-U3W6gb2SJNVRWIXJviCG7CJxtxyFNh0ZP5wecxQLVxZDwefQcZ3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liF4h9fx6yY22dvHo_wPr5kj7lKdBPyhcav8hGuoF8crwATIvlb_8f7fUyQe2zWVJi5SmabMbeq1QCsXNIxqvKo0mwpwI0HI_teufEdQHN-Q_PCCnaWX74oXDbXyL4Hy98MHKIRxyQZjeFkQ2oYaoxC01pOs0hcszP9km2ZRfKt1sZZtHB69POY9bthucofipEnbIMGLqs7LpqyKSt9u_gpDJIk1pb-9sU2cBAO-RxOzuIZlUm-swkVBnTpons3iuo7LSRdiYb9Gosn9chQ0HD4PH85nacm3SEVfaLV4eBx5yDDIDrwDauMze_4Y0yn5ZR_oPeXfrIYBW4Jl5zCd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKaG3wp4jIHgoNe8Z0mBdwfhgK1PcMxDBadN4L6nVCJDIC7Cm1ScDRzKJGLOwcZvQbJz1-k3idjSO5PscoOSMRkuIMfTkE0zQdfwBD3-0XjdlLUMMkUsLiWa5VQEjtD8EWTUf8Ds2SQ81rT9ChyF__UsGokf_CXTsM3X8eFPYH4tvZnmgP_dNOdclsiRu4nPT6zbaMfCK9YmCST6YInd2Z8hrvvVlwfpjzvm7H6s_IsyhTkVx526RTNnKKb0Lo56ymMdL_y_n1bZeHZn82vJ-lU1v3iSn3zBUdQlQ5ri9t04xUuiBVxKf7okeOYA1MJZOaDeYeJ_89Cw7vf84zJWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqzCPF8aWY-03XNnh789xl1XcGRBfyD4AWpGvut8ztiR-ljeF6khyG4vz6USQzkAr5mcyW4k05mMfGmnuj9ukf9OOp1kDMlrov_QGJ36uGoDfgAm56zG_ehvPiLECmF2KsYPCwHn3T6b9yC-IIeus4KnM1JG9esVs_bpT686zScutpoEWPjkQt6F8npQO-llbJQ82xIh3FqwciRVIaLnneLXVRAFi5gzw9GGzxmELwf0X6Ve2lprqMjez1svXcuL9LDRsUAVlff5N_TM-oKqsJcrlRS_FBuy7M82TajxdxDejj-O9t7lhOB_hjh95IuZTLh2UeZ2UqNS1SWx41OvOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGWhaHSOEHvMsH_pVifeLqjwOLKJVLbvH7nikxY7nzBPntfjXXWXuiIx9ndLROdjGvehs2NQjdK-H3tCqu-T5FdyKCJ5TYWfttXVxnnvGcdclLDwOrlWbrNJ8A09isqg8ivcKj7nWALB1hpDFAUG4k6Gb74eHYCOGmHu49IRVoI0exy-XT6tfe8AvrquAJIo6gh_-AdHIh9Tm4H0_wWUcSVs-dCRRWQ-hprCjOHbWDhr6xICVQj9VQhpflAjGrCrBHy6C8ff21koj5hHfhKCnyc76sLjn2gAtTbWT_tRiLzcD6nlBQekV8meMPGegMhPTlAm4ExrXYPuHWOOyt8WIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=Z2PtcxqEcOW_y8qDVLx4mcYQMjgHi5FZkGkKHRhOKKePQDEqhXp-Rx0Gs5mmvOY4PIchVw9oiceNkuTyyf_r_-N2Nk94lxpEZFIJU98S3aH-ZzBmZXtGcG49hittwP0G_nsSr3oeEo7p-6BqUiVedFENaz5Kl8-u3_fgFzPuNvt891rq6A30QeiUQU1js09HZJr0PggYEULiJ6Ul-oHaiFvtB64kwsKaIx9mzXRmgg8iQOiIpWWnyXmrK-WIOTi8344CqFWlxzSPn8qk2oYWc-LrCokycdnuBKOfUPpWAKxU6R-hCZdVZaocMZEp98oUUuaMWP_6Yp2da9u0zkt_FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=Z2PtcxqEcOW_y8qDVLx4mcYQMjgHi5FZkGkKHRhOKKePQDEqhXp-Rx0Gs5mmvOY4PIchVw9oiceNkuTyyf_r_-N2Nk94lxpEZFIJU98S3aH-ZzBmZXtGcG49hittwP0G_nsSr3oeEo7p-6BqUiVedFENaz5Kl8-u3_fgFzPuNvt891rq6A30QeiUQU1js09HZJr0PggYEULiJ6Ul-oHaiFvtB64kwsKaIx9mzXRmgg8iQOiIpWWnyXmrK-WIOTi8344CqFWlxzSPn8qk2oYWc-LrCokycdnuBKOfUPpWAKxU6R-hCZdVZaocMZEp98oUUuaMWP_6Yp2da9u0zkt_FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyPhh04NrqK59-ZJ-aQXZyVGwBvsn5bYG0-wrPrml8ZYTVMUNIzL6XL_Vnq69IBMoAR0YvOc_wOVE1QKGexI4fjcg1c2RyRM6SmAahnHPp0a-xMPoq6SM0HcKYcMHl2P8rG5IxiTUQlXnHEZLuMy-6ZwiCUuf1535cIva_I2_yQY8556sronOT1Eni0UpzM-DOMh57y90lAfJFgaKMvZiLIGqCU-1Cql3N546JMeWbRTPXLTw_pCPgz68PFUrgzMbuvImmOJPSVlJunFwhUTecXccrcSf2ajxO8Il-RcO_-ng7rIZvcutGwjIeKg0Gr1NKmbktooD1mEg1XHoFaw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5srLoi52ZDmHApl5Yt3kBq9WDJ5m5Y5E1tZjtkudEBWODTS-FGsDMzIP9K-d-buhrmBarpbbHZF3gQaL2OJiQw1vxn2_9Q-w85-L-FV73g-ev7SOQxfZGrmhOK5TVVU8ivUxS1SPknDp-hW4khZDqMLMa0kLF9kLhOi1zNbqlUANogqhlD2obq1snOS4wONuTegvpbDGpSn82h2-apKSTQRmgH6I6D3OcbBXJMGPGeH4S1w6KHmnTL2ZJu1QE1IXL7xPCIB6AWpcwWcI7cdBZ1-gdhk-CQ5qtRcn46SPgOXFp48aasmpT_ShWtVolPcgF4hZsyzJgFRHd6g7YNK5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7g1UU9aumroqMYfVR3Yf1mobbbeFu1EmYlzXLKNtYwncvEfodNJoUhwKQmgAz3zUhximb9u0QNwoTktCn4qRoJfDZiKvhEv-djT98iEsm3iDmdLpWRQhVG2Pd8kgerodDDwnNg7AaX2cZUS02C6pCGipoNibAGwyFgRYI1HZm62NCKIMztu3TW7KYVMt5SIiYpUfvj0Dc41elTlgsINpRopOPPdKBSf7hRRgc5zdE4naoWxcLa-7bEuI-m_CJ6RMcbtMazr8ZD-GZXO1sq35DKNpM_Qm5aQUxS_JnlO6QcVCzJsDCrbBYGBLjpwYhsw8VD3mlC29Ef1NMDDPlCcig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUNmVl9h-o-XOOqTyurO1dr9iJb5lEQNkN7POD7-zD85KjfDngjzRtGjllL-7-Pb4hdF3WyQdfe5p3vBNWyiEcTZo7DKhZI2x0EHKwKYP0dJJn4BWkJRbrdspW7U6BDD6LEp5G3MPBV6v4F1S3C0sQ49NRUHPE-oIRtAmu-vG9j_NAsbaOKZIy8FQLjI_Vxlw9H6P0n-iqNeJOp_kV2dQt53C5QD04N-lz1TjiC1f5fwjI_foIzTfh1IS2Si8ZZqPdJxJc2eeB1wVwBJE2D15qEy2d1k7h2aykB6aj5oBDGaIYQNU87lTKEg5hpDCP4MJMkJLVmrJ8GjqS8YnYhMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ku81hv-aigeWWNRv_hbPotYcLtACkoOc-EpYaYuUutm5y3fH5xgb45pd3OvHF_eLLvhaIuxEtOV00_iFbMLPhHXdh_1kUisUJgwuDT15Me912fIX4nj5Giz2q-vULE8L-nWUrAQVHIHGNX3FJ7Yf1C6IH8qx-fDXrNRyP9DQ4iPMEk51z1BTqEsZZ6K0TT4VWQEjlItzIEQc8Zhczhd8zhfHTaxs19qRkEKWbCB_0O33s-Su1BF0j3TeEcz2s2U3wDPpU_1744eXRp7TRevT3GDOERimW5wLKt0h08Z9_i57TGVP9BgNFv5ZUrbrCbAN1a8-U9dyf2UqqbXRTWv1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6F2Yr5Kl5iOQtCSH8QOQRh4Y8Xu_HFLLRcOnYrzUXFaXQFPLcNRB1XOSWLyK_pwzWDKnK07ty7pMoKJTqEJBhCYH0f3Tc7Oj_07kq32XElkpdIvL8DaaB-KfeMFVNqOK-UE_5loph2rRLq1m9ifDJV797hN-8GubM8zKwIbHSDId40jRR-Sc9Ru35NYKzDAkxCPjhGuOFRU7SBcAOybgF7JOb4DCJYUEbRWYLMFkXoKYX4dfQvMCfyVrHZBPNj1qlU7iMWUwP-uqtZLVcIzW6lOzSrEy-ac0mwsvtVO_HC-tEuTY7rC73HGylI_oqhz0184q0l02zdbPUJRVZgVEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s-aeaP1lzf9UVUODG2qrIzXZXpHOdenGjxICYCy-wJ41LRuMmZWi9ws_xVJ2EYDA1laj_8CpblUYbyqgmT6mrvdISFwTCmuQWDxdYQsCByhCZsgsmJKMBeADDCxcWBTL9fFCAitSYLzcTyBb5bi-rfI3lHjYThoEWGX_C6WPbq7ZUecbZGkozx3ogSWENVLmtFUtNGwf1xukG-y-e35rPfp-5I25xWl8ivlIAHjGa3EwS9D_qH35nU1N2KPqxGqbyiz8TfWplXNGGS4oivf_mWDnA02asT1pFuEe1cNs6lzdG2D3gm1LRHEMM1vW8ep410aD8eQ-KDMYCVjRTInP5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=s-aeaP1lzf9UVUODG2qrIzXZXpHOdenGjxICYCy-wJ41LRuMmZWi9ws_xVJ2EYDA1laj_8CpblUYbyqgmT6mrvdISFwTCmuQWDxdYQsCByhCZsgsmJKMBeADDCxcWBTL9fFCAitSYLzcTyBb5bi-rfI3lHjYThoEWGX_C6WPbq7ZUecbZGkozx3ogSWENVLmtFUtNGwf1xukG-y-e35rPfp-5I25xWl8ivlIAHjGa3EwS9D_qH35nU1N2KPqxGqbyiz8TfWplXNGGS4oivf_mWDnA02asT1pFuEe1cNs6lzdG2D3gm1LRHEMM1vW8ep410aD8eQ-KDMYCVjRTInP5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=lDg1Idz9JL4jv7tHPDfRXf7ukult7k2uCYrYJrLV_0vL9cTKcKqifx9Ab5BZ5OInCgvLj0IscfIZEcvV-5erKxA1BiWkN3CRYoYet-n4Bxg2Z44XAaZ6uK-QYado-EgYTEBAMPh_DlG7hlCDasGlS3EgjdsjLuPQg3Ht7SMFd2j7wBfWsqdX-Y73aY7y6PIiDb5Gs8JdE5udShGfbNx5t-fnV1jDb2qmYfKyZLNSy_TMcpxprYE34e6YbsVgJn_BxdiKN6jGRQS3hIL2WC5UkNNZDtLeFS01dqEHRQpQpfGELZR7ZwrTjHyXa1wLg71e_WzKrnMttIhQUxfJ4U4RsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e81e75283.mp4?token=lDg1Idz9JL4jv7tHPDfRXf7ukult7k2uCYrYJrLV_0vL9cTKcKqifx9Ab5BZ5OInCgvLj0IscfIZEcvV-5erKxA1BiWkN3CRYoYet-n4Bxg2Z44XAaZ6uK-QYado-EgYTEBAMPh_DlG7hlCDasGlS3EgjdsjLuPQg3Ht7SMFd2j7wBfWsqdX-Y73aY7y6PIiDb5Gs8JdE5udShGfbNx5t-fnV1jDb2qmYfKyZLNSy_TMcpxprYE34e6YbsVgJn_BxdiKN6jGRQS3hIL2WC5UkNNZDtLeFS01dqEHRQpQpfGELZR7ZwrTjHyXa1wLg71e_WzKrnMttIhQUxfJ4U4RsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYd9EkipE1rwltTuQrrv0HgzDkElfkiFIYB9iJWUUz4CPCUtGTE5B8_vGyDFTN6rf3S2CEi7NkmemQOML4zrrQV8HrkKkZ7Q8zBmvDMg3CxdmiYv_sONFevHSCbpjtP0o13b3OAQ9FaMyx9aLsHrJOQqXx17DXpMDIDF4YgjlEZeu_ax_9mQoeiPLTTBdyizqQzZ5ohxgGa0DFFOQNIXJdgSPetxDMSE-LueeFnVhX0vv2eqvXHitQIWWHcNTkQPdoHKVX36hl3cpEI7QuAkmz66UC3JGeVhGTvZhE5ftkuKj3Cu0vbCLXbyYFQXrwzVEkYLXTD_Z1yAsIXb4x_A-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=WIqBqy9CwlsoWnVGmR54ayuPoiFGNu4dBPCWFf4RhIVh_MqSsNd-zPBnVdkVloOAtQ51LChJIsM1qQtOlmnxwCqRjGMmVXNxkG8i5BhGpD-aPZbERrXkhJtTr7XMjdNda63QqZKCiIn4SGgGFhTV7_b7Q2-g0CFxJn3Svtkmd_sqMDhx0TCin3O5uWA7MxMo6OF_wGMvdnxUWjT2jl1FbU9E9YhSG5PDQnY1W1ARiBeEtErGtjVsYBf4NcIBc8987C39uP-AnRulw15ZMkCyLALUbqMs_wTdJOzAlpxoMpfdwjjs1zdHJOwHAg2LcNw0qvKqD7KHNei6OfGO_wLQfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a8e003dd.mp4?token=WIqBqy9CwlsoWnVGmR54ayuPoiFGNu4dBPCWFf4RhIVh_MqSsNd-zPBnVdkVloOAtQ51LChJIsM1qQtOlmnxwCqRjGMmVXNxkG8i5BhGpD-aPZbERrXkhJtTr7XMjdNda63QqZKCiIn4SGgGFhTV7_b7Q2-g0CFxJn3Svtkmd_sqMDhx0TCin3O5uWA7MxMo6OF_wGMvdnxUWjT2jl1FbU9E9YhSG5PDQnY1W1ARiBeEtErGtjVsYBf4NcIBc8987C39uP-AnRulw15ZMkCyLALUbqMs_wTdJOzAlpxoMpfdwjjs1zdHJOwHAg2LcNw0qvKqD7KHNei6OfGO_wLQfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
این‌بخش صحبت های فیروز کریمی هم عالیه؛
میگن الهویی دستیار امیر قلعه‌نویی گفته ما هفت تا پلن داشتیم برای جام جهانی؟ مگه فیلم هندیه اخه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGDkvE_TXrOX_c8QZ9_IyrEO7vjRw5GWmJeLI3KCAGHi50k9200f51shvVxuVy758Z-EWJt3vmkBbtMd6RigrARlPTgyUYSPtVduKuO48g80gMf7TWYkgoV4KGrmmLnOcRCwXc1c7Gk15hJcmHAmrQDovoBHV--JRM07c9lJH1wxmna4y4N8P9qlUQKZzA3l-4KB26HLBbjQWxwr0nAvKNhmWBAsZvjdePC729ASE_n54F2fiDE3AVSspQ2Qt_QdjkjpWlfyUnQxf-g4EAzR9YVRwcEF4wyhzf-tZIe2jydRvEn_liFAngXsfy1Pyta3bpjuf3lKDbxd1TVQQ-5-bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNLnv0IDJ9Ya-YBIjeiLvswHxIyZ-Vst9mvIK3pDIpkJm-Nd9jQ_GMngOZu7UYDjc-J7hb4iT5Q6rjjoqNtWbHlO_4jsSD7YigOiJueEvM-vOiiqp6wuI1AgzayTLie4Det2Liw-U96f6Uak0u1dvqMUSkuk80ma8Jhp5Ax0NQh5tjEEl7FfC5SuGfpzeYfBoAp2kmcMQ03oZXmnYZWVM5rEuXjMhsmFJLAlTIXydvz5pJoZhBsa0BllIBgzA5ErHZtqh4RFzbGfdpROte8_9BI35bbMifuU5reVUWrBwiUNdKV5Opx-9_Dm30vWNwZyXMoS1TfKWojfG0cBd6Wdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S3jtxibO6_WIKpTpVbYBamkqqx6hL7AvIxeEbUf8Mtoah0Oykp6VoEmQZWhfuXiBd3r3zGlkwrMYsDhjCZRorGJZzhTIjrKyBLOeVAAFWvLCDiD0FMh2Js3xPu0Fuak6nHL420eui-8y5y-1kY-OC0GzENU7hHetldN8rAfVTz9UAXD3vKiiG-ou5PD6wSwHU4Qv8vdeLyL-Qgo5WIw-TOhB5hVQCwqtuKNjFrAgidDa82zyg21c9oetN0GAoAg-vovZn8VEwClU65yokHFYjxLv-x3WSzgHjjXS1DIFoXOYrIr4ulKCy7P6X7UsfQ8RKvQHgCSsPZYBG3IGbddyNQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxYfIq0fGNKKvyEgNIK5iEkbUSQOSBf9WBVunpBSrWEMcn0K3wQgMieYDRgoLkGUKISRdtgtz1kbmCbF_mCc8jrYqbYRoJy9ruTxRB5EiEycLDtqHNmxWZW5k4QyWtZvSJ8mfoB9YFn_syOAq6E4v5v9ci5q8BApuFFFhyrQcWoZxWbxztnOGVw4kee1WexTyClfdNvEBLG-c-rtgE349KNKp4QhNIYPKDj5ye_LDn0z76DSccn_U-HRRUOlJC_RFDj408ucKY5PuxQ-QpCUk8Er4JsSpphN6JuSqAom2WqDTWE6bPN7XYD5oVZXT7SSNrtx5Dk_03b5FzIOWrpjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=pkuo6DbFicLiEg1QLnlmRaCZ1gfbv6Dy0wY9Cl35GNDiTZ2ViqbWo2SqHw_LB1Z436zCYdzFKhLDEOjmtvA_h72HCf5OKc0NYuk0UBch7WPVIs7WjKyCM8Iw_nPEbaNeD1Wd-2C7QC9LGXvZTPJS1FxY0JOmGhYPCG7L8v1dN4ViWwe_Wj-vp0ziSuADAbQOn6YU4LI9AHAdLfXkyEZWNkLwwO0X5hnRBHy87yi2CUE5vit_0Zlbs0ovdkHAXYFGxtFUeERkqosIo6WR4uEPvlRvxtPeT2OxNxYUouSxF1weIVkCpRQTLA95BoBXJULRfWJzQPD-NKTXw8DIwYI2QhgvZqIzq_tk0gpzOhziRQFQpATg7LHjktpgu_liE2Bs5kP22_LR71wzDcIXG0S1TLwb9AAU93hEB0kjxTQoy3Iy4HvW65YJASDjbPkar63Ddc5wbGYjK3e_q9Zp5Di8CnkADDVPJXGb7HOMxDWonWT6mj6W4nDOqRrBTpTilJkpCSvpSbREqIUYozFIKT5tZQquIhDX5VmmghJGkK9zqB53cFr0M1EidtnHNSGTBkocAm574-MvOYths_qhGRer8wSYRWeqP_ZpQY-ScM2MvEcUGlnwfOGpkIP6gx6bz4HnddCUCaAdrRzvJQDHI_IHWmorwlv6mQmNlk7bJjWh13g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3224dcb43c.mp4?token=pkuo6DbFicLiEg1QLnlmRaCZ1gfbv6Dy0wY9Cl35GNDiTZ2ViqbWo2SqHw_LB1Z436zCYdzFKhLDEOjmtvA_h72HCf5OKc0NYuk0UBch7WPVIs7WjKyCM8Iw_nPEbaNeD1Wd-2C7QC9LGXvZTPJS1FxY0JOmGhYPCG7L8v1dN4ViWwe_Wj-vp0ziSuADAbQOn6YU4LI9AHAdLfXkyEZWNkLwwO0X5hnRBHy87yi2CUE5vit_0Zlbs0ovdkHAXYFGxtFUeERkqosIo6WR4uEPvlRvxtPeT2OxNxYUouSxF1weIVkCpRQTLA95BoBXJULRfWJzQPD-NKTXw8DIwYI2QhgvZqIzq_tk0gpzOhziRQFQpATg7LHjktpgu_liE2Bs5kP22_LR71wzDcIXG0S1TLwb9AAU93hEB0kjxTQoy3Iy4HvW65YJASDjbPkar63Ddc5wbGYjK3e_q9Zp5Di8CnkADDVPJXGb7HOMxDWonWT6mj6W4nDOqRrBTpTilJkpCSvpSbREqIUYozFIKT5tZQquIhDX5VmmghJGkK9zqB53cFr0M1EidtnHNSGTBkocAm574-MvOYths_qhGRer8wSYRWeqP_ZpQY-ScM2MvEcUGlnwfOGpkIP6gx6bz4HnddCUCaAdrRzvJQDHI_IHWmorwlv6mQmNlk7bJjWh13g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-9mzbzPds2SeTyBgcPrDQVSPrdlPmi1HHSdHH2HEtah9E_amq2ArR2C626eNUSGfEtqAVVOJ_wcMx8BkPncfABbMyISAPWVH7EcwOJvWT8Jfba27z7sg8jpGPIRoxbg7leCQKIRLiasURVYrQe7jkjlUKQzhQhuY3r4qtZolSruLUqzBosU3qhDuRWjOjTCTAICVgb1bbj9lLsWKyQ4s45vHS535yNHHfU9mkBazzgWPp6cM4p8CfFsWpg2cCCE-5anQYtGGpKc_vBKUfC40ox8mn6RhXTWOFT4MXYrms0pe-yuHzFEd4UcnzQtjCKsUARQR5uCCV9OICulsW_7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bjBH0Vhxb7LgpDIAOswuUaThCYFuAMfgqPDnSH5X0qo_zhvNeYx9srrB7FfXyY8RilDPeuXgKJw_Ok55rHdli84S_N8wd9Et3fs1BtzsWD5XCN7BUNM3e2SXOjAoxnfwLUkw1j3Da0sLDqsaQDS8BJuF1mznhiZK17zXAj1Cy0uy89pBwxaNZCzmW4l_KAD1dKDN2ia1mnvAIIfKXfB1k3eyOSfD_gxvPmuegK17UVl_dqed5dUNAiLj3EqzBM8FF51_F0I4IYSgEtJavRgkmUzdBllqTZxMyPpfbfSE0i9tFJAbkylssNSMfXoSzXnQSe50RQRh1TN6cGCSGRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t9aJOKxkyaAE3wfDu9a9BW2q0vbgyiPK28ztl5MbL8V6RPpiKkiIeC-NFJQhl7Ns1L88g4rHO7AJSeudsPL7_bN0-L0i4xRvgL_qqlPdKlcX_JIpspdMy7tqgDqSY3e94_ysUw189froB_maZ1g5udjhvja8p5wNFm6I1uTOK4mfmP7ZEZpqUZdZFyMDJEKu2_PmMDQgXrSnJU0EcJuDtp1aA35W5NRxoUYAlETa4yS0ljrVMJCbfG5zpxqQLUvSl5zkDXhwB1Nwh9XAJMHixihaKwPrgC99gKhbZMor62LqrRXY8UEAKCobDWVsoqUAWoH8A2dGs_tl6hDkT52SMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r6rkPks4BFdjOquAHWiNKnNrCPIEroiVs4S8S9ZExEPJcHLpZKF2w56OROV_o0Nm8Go2nYwSf38KcP5lwrDUwqrDbDW3kleZH__BnJsVmtNAdUoWjVFbP_93v-Rm1BzjxClV_6eoyWKcq4XxXJ1k46sC8Rt19qn_0WlGommr9RiA5kq8uNKFagSjgrruKgF3erCHatL6KZCaLCWm6-aS6FtYesWE9yipUYI2ZfWkC1iAjHXmwoSm_xFm9wXqi9ypODQHYfxPlnTEwRd0iu_dX-GbFDvur8ubGfDta-GKbkL60Z8WQZicRwR1gtHhpxu2WEG1OFLTXzjC3BlEiVfUYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام
‌
جهانی
؛شماتیک ترکیب دو تیم ملی پرتغال
🆚
کرواسی؛ ساعت 02:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oj0YrYcwAk35zDuZJFU0-plmtPdRn4E3x5fCnPnrO8BcVyvDxNyU0WCdjExHHmn73N6UVbdVGhIUC5LPDeWQiV1c3E98451c8w0uTD6utjAioAGyS8ZEHRAWCB0nue-aJxq0lUCDzZ8feWmCwM6sKoOSNUZfsYxXdSgEETtzkoTduu_I8tO8QtcPhtJFnsSNlIdL2ffaHtTUlZutFBQqD0eez8EGMP3DNA0gDSq1omAIPNvMS9BGw7tf52iy_KrFU21zaiYGACnRKp7a6p4UUhk98e3CwlOUFDATk8wqHCqvHjBJsp2G7qV3PWPrWjn_xM_2HAucWgqj9YsUpE7asg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TU688vfIIDumnzdI7RQPHkIuqaZskn72df1sDahAxBLO8lpPOYxbfGnaH3Xe_y1EHB02cvA15ugFUKcCKNxFmYSimIwXjFS8kQ6abeD-QLrmOg7vnrsSAjCwio3xz23EnBRhNsYlHmsOwYcnhpqG4Lcy3pF8u0_w-rD8Ptd8X1M6H8l_bU4fjPR7JQdh2fQ-tG2beBsOzVIRPtngtrLKRjmVLegzd0LjgHJ6fW3piEpX9OY2z_LWb7nn1_N-K0pLeRnL-9zSGZTts9bgNgG6LXsyjdk1gfs818OSRXIegS3I24gNCQZBzCaOg6xiDCP_4hTqKMKSa1ZzdGc0tiinNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1hzHWWR5s2DIGTIweGK7w7A6Aqx5-pWsV-LOaT6jTIzHtB5ylfZ7m3agskEVFLHgJK7DXGz1LuUicA8fizEbPEFP5vbIeBSuy0mqYsfU4OXEFQUJkmeWyA1sJwTT02IaWexJW0_gpag6CPXnwRfZjsc-xOrgl8axplHcEKQwkw24kgVFe6kOTptvrQshqonOAV19OYyJn6WRJxm6u39yJEMJz7h0m979boUd7555KmJVy2wjbJkQ-VglS1LKE_1WBKzGCBIUX-ctISKQxvdL3bTnNW67FEvmuxrG0nCIorl_gprzE3kxFk_nigmm_EB9Jor7S_pXOlYvYzf1yjy0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6a78bfe1.mp4?token=IcD9V6nMMthky_HFcnPlaqHx7EsS3mNLtNjKmRnlU39CFxZZ1_H6VhxNjWUB6fsLUep78YzPSVo8t-mbxiZiKrThs_zbePswaNB6nhzaddfNvIx9sXOKp4alaBSwsPcUmSD994HqpZpM0kj_cfvt96LaYz75QoeRlU5VVtJlfWiVCR5NfT3t5T5N-2T56U7vshEEpMwzGswHHzULBjYq9ziOFdAIvMFj7BE7twGUjJy9cuO2EaAbC3gReJaYEZsWFOZfqNwrUsaVNSud-GlCc0e8939rmYjoAEBFRY8OKBLbLsha2w2GKlZCB9-KiP9ZCrUm-qGYVplYyNIeZKa3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بااعلام‌باشگاه‌تراکتور؛خدادادعزیزی همچنان به فعالیت خود به‌عنوان مدیرتیم ادامه می‌دهد. عزیزی بعداز عدم‌آسیایی شدن پرسپولیس از حضور در این تیم خودداری کرد و قید توافق با سرخ ها رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M0n2L5X_veB1TCd0i1ndSnkmjWnkZhjrzLrHHgYrDWOxADQheiYY5DxcQn2UbnLw9yBt1axWzJqE-JxvLfxb5WemBdn0v-Ry-43ZkcRT2wql09ld0tOZKShnsATICcxqbDM2VzL3a8nmSdra5ppGqMCTUefEo9zsDU2w7gXydsl0lg-NNyuc0C2eG07HyNdAjf64dZbmn4oVYnrbkWNW6-Nz1RT7t0LwAW_ssdDwRNgh6C0NUKCHNxGmlSk-1h1uC6J4ulkq0I3O5PQDjPcKMXnndPeNCxtw-4cEOgQGM2fzriqx31Ajd1xhJ9B26hzcA0Yed0BueDXq9w0QZsZRTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lqt5qd9Z8jrA2FFpRIrZWofYl18bn9SKtytlW2rm_QX-vD3A55BhhosH3EzqNuTACWELMhoFyFq8HT2L4Y_7UmQ38fhuWEGnM4X2wRKOJmAtlXkhcbfk38g_uMfvekIvm5UKVx3H7E5zy_wvIsjj2HMIrRy0iXNxqyyDqjxdOw4EPz1FG5klP_Qk_k4AD7zDFHl48YMNP4pzLWAXhPULY1EWY_U633nu0pnTPgwUnkfPPt7ogTf9b732KTEpKeIR2sLDybJMxeL7Iqbdh4S-X1ONnimToXa7iXP3mM4a-KFWoisJLkWi8hS1hxvf6NRSeIX2CNhsVw3KgTG-T3og0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXnBcJGnelOGdz_nnVwMZqQfChHIv6bnDlQNQlKSFOvvLnm9OeBePQB4bf8RRcd8wgLRPBWq5c138qsAqdLPGu_H89G0jCITfV-svpHjT_xNwqvedkxiYW9DA1Ag-cvzWEUl172Y4ZC8SHGBqt3S747jMe_U75FAis8yZjtofLTD-aS-lMyJZTm4Cbc8E2U14NNkdea5aFGUGhZWK1r_I9TJZ5m0lR7JOEP8ZFdIf5ZDr6jZXiVTc5vDYLujzbJ5TmFxgEGq3VfnUxuh414VxzBs45VIBPYxfuc0c2x1ftkzvy588EbHXeavHWmgFQh2hf2xQHI6rmZItuvqkvL07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3237c767ed.mp4?token=Z1ldoiR5OgQtY4Hp_wBcn6q7QXCCpRwmeKV2aU5z4xlaGog8S61ukfOLKUN99IJDsntCQkkvtf5jg17Zw-eoKzZlf6S7rz_MZyB0rICUz0EqlWcezR-kBAVMdrTAPDruMhhCws4TmapIP372sq6MPjB_JZ5A-DGlSVX5AFv8DAIXzCQS_gZV-lLajQvyZUEkq4sfcsbWAxHNkYn3gr1TKo5VhF4Wyf0TWtEEXmOvdmO25r0XoOHotVpYmsfDfoC3TxKdpbcE2et6EpohLyrKjowyj0PW_ice8ymuVvnozyxky8kuIfa4IqoorOrEeQnR8kqpzedSxEtFEq0UxHDa6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
رونمایی‌از قانونی‌جدید درمستطیل سبز بنام "قانون شجاع" که توسط ابوطالب تصویب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z06_QmEszFFk8lMq1KQYos5_IWCX1Lj59Xh4PSBYNGIWCexZwgK-8S8M6ZPRCQoqIMJvjyEr4w3JBw6KIy6B_rprUQEleBdOjhYfBzwfxVNwhq0NTI161wQ-3hQGTCm7WVQWJe_uC88K6zlmsDJoblU_Qq4WgtWzdfIy3PzlTcqNa0N_kZc9zH1g4LV_q6NE3ZA6LI2m5RA-JKS5YWZyvQlGhJxieL0fM4kj7hyXy5gKADGXXet-IpH6Xp4a0OKi0BTR1VGXAe3VczMYOJHap-j29PA93xq3VymMFwznIiACtRn1TpKNdiJAKAbrOVeFd5tqncqreSiyJ3qq1gjZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cffa11c70b.mp4?token=j7WpER2sDPr58Gh9B4YVNLCSQAy_bYiomDh1G23OEia72h9d_5VYAUP6nSY1vIZHCePJDztSPU-_FaVL9T9rM73oNX56p1LiSERZ0YEdmPvnipaPR0KFtBocdvAkzDdaFFuq9ZTcfba2BzbmqhkjZ0UfKo1314nDAY6KZysJjhSRGtIivkVjjv_LAMYXCd-VZQvtrBQUfAsnfJ6VaFOEaF66dfv15Pu5SXTTtLubCEadRavDlM7iOVoezCrN3TvVo-sAGpV1FwKfCqkWkzZuDmZo7UQ_VwLsd6FCRDZMR84FBd5xxvms7knhGJ1aD33hh11EP-hzxliJ6HxycJr3yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره کریستیانو رونالدو در یورو 2016: از برد مقابل کرواسی خوشحالم، اما چون برادرم لوکا مودریچ گریه می‌کرد، نتوانستم جشن بگیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNSBWRbje_RPJyhy06c0yJi6H0lpWfzBRE3zcvLPofzaWBf3SmhEJt6rTx693V5jtLS3lMiO9eVNLSt5kU_6EzdqcUbzbLeDMvmlvYA3z1zvEB7nj5BTtcMJdVOYumg7SAfI4edvjPsYsF8AbMqBcOvmCwRhL3CNc-LWZx0wbDgLZr01Nx5Y21XlXGg6wA4NMbQXDLMOF_fpJ2ogXvE1Fdajh-2piPWciCwHgt7OVbezatGC4OfS-gnL5_zKK-1YlSGUi-8hFt46ViQjTNKXCEM5MyyjD5M5Dlv3MJKiJimWTVEeZuFsoygU3Qy6g2XA67KUt3uUBjlGI1qF9gRP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC0ARqyvfJB4PMB2sL2Oqh2o4NZkzoi5NrNwCY3KZGZ-FZWH5_D6RCmKVXzLfN2D5k0vVVVHm1G3lOL6MM-6XiEEQh_iRM7bDrbvGfr-oxGZUjbEHjXBdHRmuF1eWI7pRMsrIlkW30EZK8mE64G5kIqlMfF7tCmrtPRlWn3df4m3ep5JwLmIyAYIYgOuL8RfsCNVDmufPi9xaipXuzcXQdHTC2ccfpHlP2haO5n3bkWgSthtEHsNLG7k_DyIOFb3A-01qimuQ3UswhZvaytsa4fMiJMnsJlB7n3uHOQCewBEvAo-3RsnttJheX7nq-26QeWu6cPlQsPrUOoXQGaxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8glo_Jlj5ehxXjsWXcIr_JzM0n5G8_MpWt-4xO7imSEfsEdGXYeP2WIJa7KY-VbdjOnlO37Uvaa3KF9krQYgukRtvEscIPeMKlqkhV-ZXKGvCNw6lxFbU_TKByvRFE-BD5_B6EiU8OzUIfi9EPU6LA1oKe9cEOzlPyFsMb8P3hR-I5Tu5xVxH785ItOCMepRPQDgn73hSoFdkwyKVWiiPYYYoGYkUipcZzER1AcJfBKhZiy8TEl4rR38ditL9x0OciCzUAt0U9ZVC5v1VGtB2c_5Ya5ZEG87zbnEkfKZ4omXJ7UPY3OFucaxf69C0hsfwo_yA42s7PBAt_0YJJ4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3GA83iKiXvmOHDc4w8ZBGc_7LYEClu_TSDV0apCJckypfajuJ3gutaZPB07L6R1f1ox-XztrrW-w8a3vMrU5tJSB5lZSO4-pTGUCw5pBxZPyUkguq1QiMUHI-1zvZpCpQKWg0uF1zhYdAI1aaKHHrinHdv_xXX_xgvbnf5c6SYJiUgE5v74jZke-gYYtrm4Mh2jG7rUvx71aHWANydJrQaLZ7f60gej-iraBOz7qxE9ouZiKBTxiUvXhdJZ_H2hA0C3J28gw9C-4mCEetkW9zC2zgJ9f9vftHHBmJPi742RrKolsQkqXNQlZnNkkPWRK0sS-rOQFPNeRfmEUVaSLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q518TrTUufKMfj0pta4YZHXEbrd6RaxnNqgXHqF35Z7ut0sdcsi9eYtN1l9Tug1xXE4uaevTln7BvLjMMRolp0v9lKushkGuhFOLEUoLBMIQ_-zywMKjfL7frbKkH8hd56aDIbRS0roWyWaDkWeSlrzNxEo9dKrKJnptfk7kSF4uyAeFDOMJSigwLJXk1tTobZnel0dAsQviBMvNhoJGeTqYLmhG9i682WKe7eJuGVf_GD0YOv7M2zbPxOmWkfHorduso-XDhIgOCiLrzc2EtufJ6iH8bKJT9N12uBV9ocVklASxmeST1ORs-ar6YPIB0snHiTFud505WpAwBIF4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0qSFrbxwxLSE0dh_awa97EWf-DQcpfAl93t886hXLLp7a2pD5rxf0IPpCpfMt-0z6Ciy7dvrqifroXG7_U3swViChPxlLOUneBqeuLM3g6SPwOfKGuxpzCiOnwoZD3eJFR8BZGj9biLz1dtEtxtYP5golcbmZYurkPQgBECVRIfkljrGiAjF2QbYM9z0AG3SFUV9uuK6Q79HJ9-DqG16QD8LYANAkqCLFNmzTaWAb_-9qGuvWqVUNrv_KWqdVBp24_BpwmSscqtZmdR-dIRVhjLsTt9BaBpNV9lPXAKGlmtYDVdWZohHWsN9CpDh2csLwQMPY_eyIbQEtb252B_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hObsJXbyGdIvQz8QgZPgGbiMuI1CQOw-4qMHVvPsPuNRBnhn16eX_oW0yks9rxxNvGQ7qQ5J9zl4evwB5FQcu8MfQJzJocYWK5eVkYJidzGTDwYCVegZmBXGZ-QB716PVfb6wXBIzFKTxPl-KqAIlWD9cXNQSy2-sQjPgHeG3sIMgKi8O1J9hJ0UK-DlOwYttEYtIEN9Dv8-Y5o_VzngVOKsViwgqZbnxy1uUsNrIBPyyJYT4BnzQI4uZE9wsMZypIiOP8_pytQGa_KOzfLvezT4EzO8-XzPwmXoaYw5sZWuUCnNJ052TCiAPshlF3WIdrGDYoMCIuhSBNf4KDF3kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLpZ7AhzTLYZ4tw9x_sZL9pzlTox9wdCecrxuQ9BTCH9q5w7fRS_2azdnIRZZ4n3FpG7wd9QQ2LsmS3bRzt2APGXRO_d0X3XPKXgo7UFn3X4xQhS70e44zFXQbvdz1yxnXGb9cLvsr0-JLvYdx6ziP3Z-c_IcQCvaiciMEsQN8khwAbaIh1SNZR0y8c9hRtdg0jsT4EehE6ogjELOdmq7MkfjuP_gkQCXO5pMC6jEKa7VyYGGXDLu2rO5S12L8fDHbFjKC_TV28oDs1mv1IsY1YzfKAcBsX8qfbcQ2WfgfbDP2pOj9ashOu2GBLlHrFwgtbjSByz4VIUtGcWO943VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaabBeJ3-QZU9K6_x1MrwL4rTD8cIkHEaR96-k5QtQVjhHkeD4gXc2DKHaCLTvotzA56D8bOtcIYIfRbYWYq8R55UX9zf9dGQ8AUiqPfv95CNV5DU5PN6SzPW69iiOfiCSfbyxn_x56pp7NB5ole0v6eGmZhaeutEKdLc80RJyKbYWcjXHrjjN7bD54XJLYU6G68kJl80jICV7JuRBGHs9URxcTOO6VRnxeHo1Veo1DV_I98G6H9puWgEkN-g1moQuS9m_qIE79fj2_PJxTlYGGgCAe1ELkrcag3GIVkPkE5xB-aRTF0iPtLqK3fly7yWnt1gNTFUCvdzjmJ4Y95HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhOZwRgAD237k9JB5rB_0ESLFUCzI27U9RnQYBmATS2o-k_igX_4la61mAaoda7z84cg5jU7_JfGk9fqzhTxyChSu6gjHTQy9DskUR4TNlrBeq1wNO9LIyRAOqCAuO2-AVRsISalAfU1rfJXAxy7rwryJc9RWSNM2aczmAIR_hthta9MhqmKHF3Ik9_hizvuen2-XmmlsRKaAF97RUQpIX7D3ZoUKmJwmyrd4MflJYlqiTcmhbD1FOT8-tZ0yLV8_n7MV5GwD9z44-kTp1MtL7mORblapbjw-0bnjHRUc7EqY9vjaVqoQDfn1x3rId8gkWjQDEn4Wg9VN0Gu85fPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTemrAHHIKHE5EhIa_4eSPMwe_PubsbIR_Cy4RDVWcovjTiMv-8UdsMc_SEbiZZpqF_rjrbWDY8BPQOgidSaWUlnsgkUh81d24SVz0MkeoXDYDXwaS9vJGFHWzbvVFJISn3vzV9KutII0k9k5mhloUYP2VppDaJzyXMLXA96XHR-P6eih9sXQ_0iovjxkRND_po8-zuhhttN9dPau0wwxjSi4PW1q50OfGAcQfYH0TNWhVq6cd4c1KuJWcmxAZw--aZLsd25A8PtqLjlBrDotqn7CJwtnWBCmmI0ErbYQLH0aKbDeHkVknuLvKwTRVFL1lskC8LgPMPotNPtjTf94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwkZTIRW4ygRBXJ1pz1jojNSISLwGJFzX_vlxnFNWlIKfdJ32xES-bFqiBIkCGIc76QMVh_pyichN0pq3Z4YZLYQQziNLPgep9NchHnAhpwtZRkno9hifctNXtRUdIUiqqIW5G8ReKwBvHvxZhzeuRcNmYpcXDyd7YM5EH9Cp0GOtjqHdFs81h47c7ygX3HxyoJlTx5VVIWv6GtVN4a7tw3AX1zBVJL-dmwujc-_BF0S3a3o-Shj6ed00sXiTKkwdQCdqr0hZgzF6OpQskHDQxeVh-4jSA3L-c4nraDbglH2l6gxHPhgTdPtDLymIWPxXA7xMxztqwuV1EsasEBhYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9GpTKJa8_gwvSQU18IYI8OGRug6K75SUK3e8h2kAHMFaht7kKKk8pmSW9ZNUOHkXpygHlbzxM8GZbCyK3Ax9nk3zwLwK-iD9hvdhY6vBX8rIwHiOE3Zt7_h42tAYPrpGVznPYCPsyjDT135FW0kY7LsD6iEeRkOidhHIbAuWNqj4iLdpx-H243eC3665fO-U6p5qbPX4Q93kS3lTgk_AwfcQ2dyypg72-ZYwzU7GDNRCj_5VhpV5QUPtX-XbeZGuKn2rMpsjGN_DfgeTl89IYHYz8iu5b83556xMfnJlSBneEqg-4TRnV0dpLjRgWeht_Fbegf9knKRIc35Hy7Vog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2dHhL0pcP4bYdIDtLBZ4SSYqO7hnxbb_Vsv70ZNVv3LCWj07Aiol-gsItXVXfzjb2ssChM600dvkQ84OtyF9VqLgaP1zuKlx7VXmbRY50y-cWpJwJuo18xUw8kKy-fY2DnPWHhc55jS1GVtTY5sqoOi0pyezFx15PePQEPrrirG9bEkH1Iis5h-Nbkwep74yGYJe3psgTN219qiY0A9D58YJAiL2wejBhtwqTUEV88QDW8VPYI8G-shf9unRoFvBWUOQlu66Q0CxxFJK6jmKdCd13R37ceyxWoplfjkvClixnbyMiqI2StxZG84eOMyr1fUxMJru1EM20HFqVqmwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxGvOeIx-1cZTqxiw94QIw_Y5han-VzKNlCJPTqApnLc4qD0HFXGm1IO87_2-bTOvdpaWeBGYsBWMvjCDxL1oGxkgb4TxqofXwM0rFKsmMFo1siVXSxv4JmecNpcN3lw-drsnOH-Lyq6_ik5628RUWxaKMkDNzvybS4RDNNVuteAs3oyyJXhToxj6lVbcXsvNCW8qA1uHTx6Cq_P_s78w_yl_U9o1VzpGxRMU5jow5wOrvf5OALvIfx-9eo-Lzee9shoAXh03opW3hkh4i8ib5wOB4cNfXA74oZZrm9uy8px-jR-0PDWK-Cl_MkH6We7-LADUi89lFbDpVqPP1Rh-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzJHXFaEYovscpsZD2sbWjvOTONsJ9wF1-4txHxUJt4IbjmuX_Op_CYiXpQ7e3YNLdzoCr4dObb38Yy68blEuv0OWI26c-sYanTX3Y3Ksvz4oS-3L9jxb3xDjxiUGehx887fqEpMR8rYh3kcgPn0CUsjEUr0KRcES_Y3A03Zk5rxRx4g7ya2xwOstLB3Se6O12vnoPytAKbb-8_xiQxutu_yhdCDqWJDHjmoHIVl9Cn-ai43z1Uhg5DH3aXsczR9MpGT72zabaI1UWeJbB26MpSOtSRrC5MpeYyxzomAbNCmbIKlAn2BT5neCoYu6PVdadvbP9uVv1Nv9kiP6MVMpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=FiBX1fgb0adpubdg_GsDh1rJlAm3R5bw_q_hHrTBRqsWWGSFczZdBsQv7TjHEs3Ajj-vlllbO4snC8iyvU5z6_51n-qwp1YO-2FJpY1DLXQgMFjMGHFVyVnAKTWtcFJdsTOfYEE-s40FwgvBq-leJA5X3aIP7zdGrQ0nyIsYXHWN99MgNMl8lIlK2Bmn9_9mpSE41AAVojc31hXQQUQjsmaD4G5fdJWPSGj4WN7IoG99hMn-tCD1-rjK0Ass3KeUMaW-m7nfQxJASNYbSr8ghIQOa-JwX5atl0pkkhQtS0G4YF7N_q5uF4ktVBOXytBHuqnNj7sNs9NVOitAmmvNsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=FiBX1fgb0adpubdg_GsDh1rJlAm3R5bw_q_hHrTBRqsWWGSFczZdBsQv7TjHEs3Ajj-vlllbO4snC8iyvU5z6_51n-qwp1YO-2FJpY1DLXQgMFjMGHFVyVnAKTWtcFJdsTOfYEE-s40FwgvBq-leJA5X3aIP7zdGrQ0nyIsYXHWN99MgNMl8lIlK2Bmn9_9mpSE41AAVojc31hXQQUQjsmaD4G5fdJWPSGj4WN7IoG99hMn-tCD1-rjK0Ass3KeUMaW-m7nfQxJASNYbSr8ghIQOa-JwX5atl0pkkhQtS0G4YF7N_q5uF4ktVBOXytBHuqnNj7sNs9NVOitAmmvNsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kaZFomTlDQEYFB2GtOHo65GCEg_lpVtPxua9_55Bf8YsKFzJMLN4RuJZQSEeP1yZL52vfzdQ9J_3W-mZ8D5Z1hqZ1-RIBi0WxScHk19tPGXfvv6rf77GdvbwpgGSqmBW9XrGFLza2fNkNGAy4yf4ol_nBOcxU7gt6jV1BzAIkep1QwVXK6T6RA6ieG_vXgU-xKyUvcmMlbIEdnOhZ4jSKlR0TzE1lC8wYkpCbQ_-QRxubkya2DbiP0LgWJqgG53My6d-Dgepr7tIjfL_j8OjT4p5bJrtgGkDRwMcW_7Re65ul6nyKFoubUIdSw3S6yX-ptfWgqkHsr9U-m6Q86AUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=Xzo-g7WbjOTC_63nZKMYkPQxL1s60OIwrC6F80ftm1nbsLI2QSGEk41ZiO4jxxxMoESpQuPyzilsTOUwixHQnHa_bnXeYu7893mOkoZfdv2udmwV4y_TgUgjREZ4n504a9DNAbcdyY1HhsBkp3K3yS_2MVTojZ8vVRg8dypYW2hXFHLcUTSKl0XyjnDs1_fkz08cUo0vRAwwNSDnBWfgup-tw1qno9_4s_mtqdIOZNp-A_ZFXOKJ9p-XrtrbgvD9tpv4sPMM-C5I-qIOlg3a8fVk_8ISs6HsyDke5_mKBwVhwVqQuhDoJdfw-_xteOxP1PHQwKWQj2WF02zb-3pW1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=Xzo-g7WbjOTC_63nZKMYkPQxL1s60OIwrC6F80ftm1nbsLI2QSGEk41ZiO4jxxxMoESpQuPyzilsTOUwixHQnHa_bnXeYu7893mOkoZfdv2udmwV4y_TgUgjREZ4n504a9DNAbcdyY1HhsBkp3K3yS_2MVTojZ8vVRg8dypYW2hXFHLcUTSKl0XyjnDs1_fkz08cUo0vRAwwNSDnBWfgup-tw1qno9_4s_mtqdIOZNp-A_ZFXOKJ9p-XrtrbgvD9tpv4sPMM-C5I-qIOlg3a8fVk_8ISs6HsyDke5_mKBwVhwVqQuhDoJdfw-_xteOxP1PHQwKWQj2WF02zb-3pW1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si74WRmfULxR0uMrHAgJyUDZzorLFbemR9OFXgeVxFZTeNc50Lers2lWC113ADQiDCHWgagHdTyUtRiuYKE4UxWAHxBCseuPgTqIRW4L27RAHjn25jXuiAXALKebazHR2A1JmejcZ6Bix5pFor8G1JlNbine7GD4xC0LNuoU0o7dPUPp3phRF43gadMwWXL7MnrXICXWTrz8dGpTn243xNfCFPacRa1pcUo03b0xT2GwO3aKqAa5LX8Y4J4nkAFw3EedFOxCfw8eDZP1NGARIkXC-OugJksZb4iBmN8i40HmCRmVKd5T3RG-I8hi_JFyYUV5WMOC-xJfVdDOOsuFSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=QlXT4-U5F4akZpsTQsjqbJUdA1IA5pyHE5mtobkJAdJpyRL_r1h-BQ798gJGrH9JMhsXkpRv3_je13jJ7fV8h4Ym4sh4rxTIBuyLMNrY5L8OGmHuE0vPiDrA23MWVR8cPqFC33c8W9AW9ovyqOYiJmYfHQcUaVi7lIXMN6hJEG_JEBnsdBAvCBskzX5RoyCW_mXmB0VKcVL2-nyxqowsgxKQsdG12pd8PidQ5DDn4p74yaKwA37Uhah1AuL4jiTIabqzTO3WUlPFfMdvL9o0T2YeJugtowOjQr19wNEkFdUi15XnajI_KsaXfP2v7gbI26OdvND37DR8vCQXV-8V8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=QlXT4-U5F4akZpsTQsjqbJUdA1IA5pyHE5mtobkJAdJpyRL_r1h-BQ798gJGrH9JMhsXkpRv3_je13jJ7fV8h4Ym4sh4rxTIBuyLMNrY5L8OGmHuE0vPiDrA23MWVR8cPqFC33c8W9AW9ovyqOYiJmYfHQcUaVi7lIXMN6hJEG_JEBnsdBAvCBskzX5RoyCW_mXmB0VKcVL2-nyxqowsgxKQsdG12pd8PidQ5DDn4p74yaKwA37Uhah1AuL4jiTIabqzTO3WUlPFfMdvL9o0T2YeJugtowOjQr19wNEkFdUi15XnajI_KsaXfP2v7gbI26OdvND37DR8vCQXV-8V8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmrS1amYRYgxGXANVCvBoeY603BCp_5AQiidKgjU5biHaycONFO8o1-Yw1N4bS9cs0v0xFmHmfPxngqSFmLn1L_8HyuSZAxTMfHral_ZjJvYnKM7q_pBrYrh_niuuuSZ7A5Lv_Vw0g4JG5FxRnBFDSVLk_lWlO4bLNbtiscmHvkg0YRvpc-Y62RlqiEC0ukGHrNtvsf_U7ZyN-ZLkuAa1tvoaUNiuqysp5X_ijDba9zIYZ7GpWovxIsCX1ARCC7qGbq6MxHWahwyPVwAAkkZ_IuGmnLaFSyTkV6YtC3K_klLDK9fGQHe8i5R0LaNNdl8wdTb3Ea2f4vL1Ls_Z5eumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVnUa0THapsQ7jYynv6u6Pv0YiZmESa4Tk4uDW_c5Gvu5Lu72fYX2BT4NFw62l2bVq6vkLmnQQqjXpXkkLuQqe1a7V_fj8wD6uHb26escIWYksOaholI9oLwXWipJ8XrQmG8eXnwZJqJMaHEAXrsXcVrIBd8400qBuso_0z0kgvVnECFeyN_0vCDisfwUGwKow4egs2azKIOKJ-LDXoO2jjyu2-2sDld12Km7_LRlhLyNpDOonMyNJsw5RxRyzkSjVyHsJjtpLRlZ8SCtjCo2wpSqvtAecodZbsAoRhKZ_MtobgbXIamaT1C1hwwSay0nj0ZXWyrMdj_lSF_bd3UOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtRtb968q45Hp3BMkvAvLkq-fMc2qMUAKfaRmyRxkjMezUxbRq3-P4JOLquI7DV19Xx1_rjgM0VvvCYal56s30puGzS0WGZjC7vUGWl_fgpNPaBFgnaNGDc28Ia_ODLT-vddgapMrGx4mNgmgIhdZDzw-ffMqkwhp758yKXkvALO5X9-2HklqPAUXMdLsEKIt_FGRYU3qY1QYqUjeNlkSYCPb0kccj8vN0oXM4YaEz7VncNBEbDDUUW8S-Gv3EGm0aDPx2NgnDZuGf0eD1eP1PFTZdY9-PPGnZcgWS4Jt500ok19chIPmU0vkiYU9xlrhCd0tsCMIrDGfaUDTrRJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=jvcM478n2jCuOHqWpU374XynJWlpsoTrnSHRceonuFMkMdzU9ApkdbX6WEAt5xRlCzJrVI44z4TKgRJJPEDSAL4umJLu1LOA-RQopQVIBaBFt4Q--dkVNaLke36ywkSY3QFQ694xDULLBMv27xbbKiUUDjraxPM25pZ7bXIDwD9j9enMWZSQkvjnO9t3OerM_Xn_81X8EeUNkrUncQwm04mGRHCTZM8V9XwsRTa_H6hd3ZCUMvrBb6pM8dJ8zI1rjK7Ke9K171SjnoTcUBCjY_e9YV4M_N4HPj0eVyqGdXIIVkOzQW6SmHAWjGoFk7bnSOf62lAZLyHPtuaUIR1j8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=jvcM478n2jCuOHqWpU374XynJWlpsoTrnSHRceonuFMkMdzU9ApkdbX6WEAt5xRlCzJrVI44z4TKgRJJPEDSAL4umJLu1LOA-RQopQVIBaBFt4Q--dkVNaLke36ywkSY3QFQ694xDULLBMv27xbbKiUUDjraxPM25pZ7bXIDwD9j9enMWZSQkvjnO9t3OerM_Xn_81X8EeUNkrUncQwm04mGRHCTZM8V9XwsRTa_H6hd3ZCUMvrBb6pM8dJ8zI1rjK7Ke9K171SjnoTcUBCjY_e9YV4M_N4HPj0eVyqGdXIIVkOzQW6SmHAWjGoFk7bnSOf62lAZLyHPtuaUIR1j8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
