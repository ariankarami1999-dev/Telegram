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
<img src="https://cdn5.telesco.pe/file/ivbu0n7Mv2Z2_IZAh8tCO5vklJlEE4Qea1X0sbNWNonKbrj9isiFTxI0r9wWiERXpllwaKh2VQEWLorklr4ueynXoJTRFpNTLSE200IjryBWCz6I2F6MBuQtj_8_ITaG8t0RPPWAg8gPr-1aWJkKwv4lxIPyI592-WC4Jm5dkWwtNNMW3ec_eE0NGZFw4ZcozN2NnSFu7QUHEXCDX1KE88EvdhU48K4RyUMv46QUjOQ1MOGl-5bJJKnegqEI8qTnhvzdoIrPYUcTxcsfg990i0Fqcb3V5CzFzMr4QSDaJTtIdBlCBbrHibV9AjbIWpbUOp7fjjilvmgMRS6haJG7NQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 388K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 05:04:34</div>
<hr>

<div class="tg-post" id="msg-108153">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108153" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/108153" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108152">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXn0gG-Q6XNyo4EHgflH35smJWQgvz_gNng1G_6SvkhWyCZIweOO2rTqM1U46xMcy91P1u7gkupAvJLJjFB5M4Kwap-pOJDksXx_BfyXgVIsA1C_n9iC37-1B51XxhPG5SZYki3vMVim4JClQxQfjIvElbaqIcmGKE5PHGRBfa7r1zqavIbgyj8EnJ9xCJrVIT8arCdPVFzuhaWhSXtHGeD9xbyn0xIH8y-dq1wF4NWl9bl3wRO69hKsgf3NLN85usuKNbd3jGNdfFx_R5izCpzqG4Aag8uwYfMM3KMGOXaJJG7W_HTnT0ZkgXTSBtRMmsh1IpShv3j_tMMCvuI-CQ.jpg" alt="photo" loading="lazy"/></div>
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
واریز اول: ۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم: ۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم: ۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم: ۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/Futball180TV/108152" target="_blank">📅 01:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108151">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCy6U4IO_c8lb6U3AuuCjgxg3Ijj9YgXIgpYt5ww2iBDljJCwEuCZp_eTsOuKGxhVUsvu591XM_RzJRHV4tmr2qLGKapeEaf0uiDic_HWagu8VlDSIkzdL9hbT-jn-Qt8KhcLEnXkmfoAY_12W0f2Npn3J2MP0NFEq3HJGXBSvIm6J3FByYQc5Cru3gZGdtAJxVU1iBZkHyGKt_sZJWVFaXkOw7iEzj5VVcKVxD1wbECLi4utqidR7R-67NL74L_OFagcNq7JKyq4u8DWx15WU8R7TtUQ4MdNb189wkfW4xUx6sFAVcTTJjP_jYc9JiU96Z39Gqw1UScyH53BCTMZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇶🇦
نتایج ۷ بازی اخیر الغرافه حریف استقلال؛ 5 باخت - 1 مساوی - 1 برد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.2K · <a href="https://t.me/Futball180TV/108151" target="_blank">📅 00:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108150">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=vCWhK4fRxaayTLotMvO0Q6HETBwVWv8wk-3bzRqzQD_VtyfLhuyOo1x_vF-GFyCEDSZsQANx6JGjyBG__nnoTkuNwFskDYcoV4Ge9OTbq-x6K0UrB7Yzx3lHmplIrF2IUmIVjFPlqmAw-YlqVl-WRhxjsGeAID_SZZVz_rEm8tPXpIgl2g8dtJN8noLvZfypcG5POlfG5MHfaTt2Mzq99fvA_7a0W6zDiQB5USZdMyzODVTBdPVr3v5B804sqqM6xh2RoABc5FVpe48I1AqFFdEtW64hkNNnQvtlN-t9HhgrBmyH1IohjwyR_NT_HdqQvmkAbVd3g2-5JBYix6RVUFQFQsOcRCq-eflO__1Gnd8LAwlISMzNZ8FUxoyVIYlO1A2JZ0sAeb3Ygs5TxMgFtvnjLszG5yyIp6J1-BCshKtsBBmowFiML34uTkZbPzzqXSN55Ai4Ikmmw9fpsHB9eRc7QMWJHIL4-0t7HFqJzeZ9y-eE1htxePcM5v41joXiV8ZJqCHcLPMzAjz0CkabSCp4lg5pjNfERtDbwhRpuI12gPntrNhWVe2wLzj94bY4JTGAER4thvDJk0MC7qq80fPR3qLNcZSeR6p3cxMVKZ_Q9aXDVLeHdUo21b2Ygao3najlKd7AkAjU6A1JIDRhn-_jwFME2B67iHpJzbdrN-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa5d1caab6.mp4?token=vCWhK4fRxaayTLotMvO0Q6HETBwVWv8wk-3bzRqzQD_VtyfLhuyOo1x_vF-GFyCEDSZsQANx6JGjyBG__nnoTkuNwFskDYcoV4Ge9OTbq-x6K0UrB7Yzx3lHmplIrF2IUmIVjFPlqmAw-YlqVl-WRhxjsGeAID_SZZVz_rEm8tPXpIgl2g8dtJN8noLvZfypcG5POlfG5MHfaTt2Mzq99fvA_7a0W6zDiQB5USZdMyzODVTBdPVr3v5B804sqqM6xh2RoABc5FVpe48I1AqFFdEtW64hkNNnQvtlN-t9HhgrBmyH1IohjwyR_NT_HdqQvmkAbVd3g2-5JBYix6RVUFQFQsOcRCq-eflO__1Gnd8LAwlISMzNZ8FUxoyVIYlO1A2JZ0sAeb3Ygs5TxMgFtvnjLszG5yyIp6J1-BCshKtsBBmowFiML34uTkZbPzzqXSN55Ai4Ikmmw9fpsHB9eRc7QMWJHIL4-0t7HFqJzeZ9y-eE1htxePcM5v41joXiV8ZJqCHcLPMzAjz0CkabSCp4lg5pjNfERtDbwhRpuI12gPntrNhWVe2wLzj94bY4JTGAER4thvDJk0MC7qq80fPR3qLNcZSeR6p3cxMVKZ_Q9aXDVLeHdUo21b2Ygao3najlKd7AkAjU6A1JIDRhn-_jwFME2B67iHpJzbdrN-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
مارک‌کلاتنبرگ کارشناس داوری: هیچ پنالتی روی یاسر‌آسانی اتفاق نیفتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.08K · <a href="https://t.me/Futball180TV/108150" target="_blank">📅 00:18 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108149">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/108149" target="_blank">📅 23:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108148">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNfLNrh36DlQhHm4s-ZefhO5rkaFv1nlglUYM3TzF3UPml7e3Uv2gH9jor-n5pE4fjr0gKkcAZ0urH6wZGVxeRVaa82Lf_lzhAW3IPAheMvUDwaQ3SFZplrc751MGBw66ZIYmp7j_T6u6gsUd6h_8-mlGnLMdImdS9CNBNi_-EkVA-x5Kp6VSNG6n1uTMd8nNLlcZeqj6v5ZFQuf-P93olkkKosKa0CoxVB4uHpsrZXXs8aTqnreSM8R9j2cvkCsDUHh6TvbCe2DLQE9oCj5aU0UJ1c6YnNus9rrlIKOiNwbqvvJKD4bVk5503_mloHpYaDjAjBTprBmpoYl6_96hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
اسکای اسپورت؛ مایکل اولیسه تنها در صورتی از بایرن جدا میشه که به رئال بره. اگر مادرید پیشنهاد جدی ارائه نده، او احتمالاً با بایرن قراردادش رو تمدید خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/108148" target="_blank">📅 23:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108147">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StX6d2NrQ-tMoH2JJ8heXyXcKEPPk_S7IMknwQbf8XggarCVucksTHsroaQq3EAlZNj5zlpdY1ISBOD9pUjJoTJToNoNQkenB0i9dAELyIFxbogscZJr60W8zjKzw7qExER5VjMgFxY4kiTtKD-0nFH2aC-hQMghS_KLmEh9K7GhLWLwSE_oJKpA-kxSfuLLc2ZeGppqulkDnx2fXis5pRvu0l7kE7TdATY57T53TY3cKHm0kj5QIhiZyhzKA6iP8K4_uSqAFrdusfWO62Xn9t6pTX40Y0jJRN3asidwiDE_Our1-0-njqgDoE3EFBUcI6s1vlWbclJMwJnu2jZv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108147" target="_blank">📅 23:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108146">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYh_BliwMFUortAUWJXvVVDHy7KTwYe6lRxX4XIkfFknveS_Bou656imT7oE4GbnFeq9ytXbAWgBmBVL96MTMqmO29vME6PBimsoS4JPZaPUoKQoJYtkHHEZib_s4xzpQ3uDfPgSEejeeDHoi1t33mFGtEnxwb9yjA__W5XNR0yfRttVS-HRqIpnxiWh5nkmPmU1CXePG0cD-NQfG86e7b4505X84rDSk7w1RlQnP6CUw5Qpm3h3Ayb6xBVNddI47kmrLSzHgIVbTgJPJPFYSWixY3UzlOp6s8R3jpEoz-D3I2KMX2movbNA_VUK0Aux9y2HI0B2CeMzoERBLT4fvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
کنایه خداداد عزیزی به بیرانوند: اجازه هیچ حاشیه‌سازی را نخواهیم داد و از زنوزی بابت انضباط مالی قدردانی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108146" target="_blank">📅 23:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108145">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=voBwjB9dDkfElbYqP13V_dCaDu1wlMnMWvi9qJ_qg5v8mXlSAR1r4Ai0kTHeo9fQ02gXrTvUau90o_Y2TBaPXLfCXsB78MJcyMA_SFV6toL62P1vBoi-tI0BO_0BgXkoCzMlVnLYLay1KyMdQyyBZlBP0LeklcNn2_0mhk7ilN_TZVDsHom-VeV0iVCdL_cYw1UpcIZSw7oBYGaOG_P5yadm9FiJyNbzORCGqcSsU_8RUhTl34ubgyIQNwn3VCxqYxKYAjdOqLo1bWF9TRnWgsXzLnoMERvFP0IEulnaQ2O8MtjA2WROO_DymcDmQmvkeB6KKOS3bHuKvPhuWAFEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109c5cc92a.mp4?token=voBwjB9dDkfElbYqP13V_dCaDu1wlMnMWvi9qJ_qg5v8mXlSAR1r4Ai0kTHeo9fQ02gXrTvUau90o_Y2TBaPXLfCXsB78MJcyMA_SFV6toL62P1vBoi-tI0BO_0BgXkoCzMlVnLYLay1KyMdQyyBZlBP0LeklcNn2_0mhk7ilN_TZVDsHom-VeV0iVCdL_cYw1UpcIZSw7oBYGaOG_P5yadm9FiJyNbzORCGqcSsU_8RUhTl34ubgyIQNwn3VCxqYxKYAjdOqLo1bWF9TRnWgsXzLnoMERvFP0IEulnaQ2O8MtjA2WROO_DymcDmQmvkeB6KKOS3bHuKvPhuWAFEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
در اتفاقی جالب و زیبا جایگاه هواداران استقلال در ورزشگاه یادگار امام به صورت مختلط درآمد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108145" target="_blank">📅 23:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108144">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOOTh_EHlVrMPI-pwjQnqJYlewVpPYxJx9yXNFLoWygbUnx_fn9exHomk0jjtSpyDPm2Y2gC-8czR-XExssbs2Dyy-leDcBosr28Hf3ipa-aZaprpacCBdrdzeKhbMo4dvIJMSevM57Ie603emLp4q-HmverCwOfBQfptVGxvsd2AsxiKrVe_6k4lZ9DS_bmVqJhAN44Q8mAJF_7NF2UF5qV-gjAOOV4Xod9AMyg32m8JlcJZa17jbYmd8whvrFvN3VSgfPbCLb7S8OYU5bzVyb4S02cl4BS0VYOi2Vvo-NQm0nHeWBOu_a9X7dvCNVhb6YdWuIGBHRhmYDlGx049A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
مورینیو در پاسخ به سوال درباره رابطه‌اش با داوران: فکر نمی‌کنم مشکل از من باشد. فکر می‌کنم مشکل، بدشانسی و حضور در باشگاه‌های خاص در مقاطع زمانی خاص بوده است. من در اوج دوران نگریرا به رئال مادرید آمدم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108144" target="_blank">📅 23:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108143">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCDcw_gmiZ4511SA5QjpkfWx32N-3XR6z1HvnMuI-fJJgBnxzUjGbxFeTs-7lG_H9T1qyVVLQG9K20Mk7GnYMFCjOWvE2Rk6jeqCuzXLo15vS7V8JPtvC9HMSLWlmad5hf0JonVD98gnyJ1WWjDpEPfoQNEfvo1EL-dpLYPIXRJRN6V790fIxWaBpDwM4Q06VDY4HigluY5DNLytzdAxgM51L5OL9UcJMYjH1Ts95lmmJQfvUt_zq6N4_MT4dAA7GJ8auWdtkcN2J8LJtzb1PZRBjydbIcbVLVeH_yGWWn7eSj9CS5Hkl6oEwAliX8n8ojdrl9-rkGDwyd8YCkLa3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108143" target="_blank">📅 22:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108142">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFIQYDzIjBtCkk1LXEVPXaiX13FzHT8mVcbv4-2egYzrO1OUUYHgTYbxtB6M9Bq2LDomZjGjO25I1zFYLifAGn9DPOkQo2K-D4a4zvXViS0GtMnP8hzf2UKQsOWAereAFjJis4q1GuCPIAZgRKfpqckSKtMiGt7jInTWj_j_-4HI_1teYdHyRb_cDqdcWgXj3IQe9EcjSh7d5sgmC7cLeMUp_LD5NqVqOkj6-wnKGQz4eKABxZudv8mMH_ExJZe9gdUWqAVLM7gPyriZfzfW4V6-taGxoSh8CorqOMGgtaj0v9swPILtP_wRhpZ6F_6GJIRrcc8fuevr8EGTSYNg8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
قرارداد ژاوی اسپارت ستاره جوان بارسلونا با این تیم تا سال ۲۰۳۰ تمدید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108142" target="_blank">📅 21:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108141">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PRy2hksU5RDEdrqEMKXBXlrV_9GUPgK9iuoIBjPofjlqfDmsbWSNgi4Al8Kft4Na84y_XWC85ezYzgKGcWzV71IDrpz-ajBuSXC9l1MJHNs2f4NdhU5NPCJ-gyVL7f-n0RdeDXNlDB44829v8XW2vfLWrDIeqziAjQEhsDK_GDVq1zDVmGqMO2vaaJpk2b6t4BBQ34Zi0Re2AAKb2Sa7iKIYpkHKwfpPvHLMdDHxLFHajB8FEOO65_oNzDpjaFPDlKHzkWm58ZtK3hst0hcnrD81ooT6t7TWykzSofobaJHfVW2nXSmMyaV7PXMXrl4OnbMK2t3jyj3_tiE0icASPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108141" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108140">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQi44-ojU8-fT9A81ZiRSXxKVnTyWQRDyFObiNG3FA_IpcT0o3ZBBfGgPmSJtt48_jlMnO8tB4EfO5Tox8wLqqN1QvM7QW88-JQZ5oWq3cSZrSvx1xrHUOxuVQBXwGw5zJzV_pzd4wwrz4h_pJFbGNLP29KVKiPklJ0AsmORYzOfmGBJpMFPEBxKjbIYbfKaJF9oKd5A296bYlrqTBSrfqfLpom-8leBeQvRViOA8-40rwTC6nviaJWiQ2Ooq1dU9yi9yWaBXMnlUhUUoJwY1Hu8MelC5nwrljdwtfyvQ80_si1skdEFTivH7hncRdzLcRoRmH_O-DjL61s8X-7NLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108140" target="_blank">📅 21:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108139">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14105f8264.mp4?token=M1i-MI31BDy387z7zLRdPjFTxSNxe5u8DgmmZZjVLqT1hX-3hrzTlQA_E60Xt-8UbKG1g2Su-w0_swUW4Bi_7D-nhneY-XaEf0TA1l5D-J130UYJRUBvz2ouQOtGeb5_PM0Fgil8_yALocgrtNQkgDae1YR5pigOphLKe44doi_o8VAPkt9fOq6Bxwwwx-CkKZ319xPrqnsWd3ndIePv4ZiFa_C0-oasnjfa9j17cXgwsI32UlD5gvyIql9QtR9c9AtN0F8Fx1BSuftiximLXOWutgYlOHuLIkkiwzknJpP_8r2jCN-HXASeIOFEKW-ZO9xJKtH6qJReS3w4_5ujrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14105f8264.mp4?token=M1i-MI31BDy387z7zLRdPjFTxSNxe5u8DgmmZZjVLqT1hX-3hrzTlQA_E60Xt-8UbKG1g2Su-w0_swUW4Bi_7D-nhneY-XaEf0TA1l5D-J130UYJRUBvz2ouQOtGeb5_PM0Fgil8_yALocgrtNQkgDae1YR5pigOphLKe44doi_o8VAPkt9fOq6Bxwwwx-CkKZ319xPrqnsWd3ndIePv4ZiFa_C0-oasnjfa9j17cXgwsI32UlD5gvyIql9QtR9c9AtN0F8Fx1BSuftiximLXOWutgYlOHuLIkkiwzknJpP_8r2jCN-HXASeIOFEKW-ZO9xJKtH6qJReS3w4_5ujrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با کنایه به حجت کریمی!
🔴
درخواست بیرانوند از مالک تراکتور: به فکر تیم باش
🔴
به داد بچه‌ها برسید؛ 7% گرفتند
🔴
آقای مدیرعامل به جای پریدن به دیگران مسائل را حل کن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108139" target="_blank">📅 21:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108138">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMlZ3-yicbqXs4Hbkz_gk9mfYHKY-lmTmcsXE93dzuRpq5fItvr2xVAY_ZFJjVh7DZYrKajMD3gcHD4ZT-WZhpxYKtG3k0QhRTIA3cyYJFKHWEFMWLxhMZd2aVnPcVIq9CAYWt9BE3yq7D_v6mL-A1QdqIcRaDQxyKRSQz9Jz7Mo6uV7zhz6O9KOpMMMpNL_n8ED0iotl65N71j-uXUr-1r7fpSVQtIB6bJVcnYj-e6IG1OnsO_0c_UhkCk2cEsggk28Vb8crCTlpDSglSwsuQLKJODGGlAyeDhP4EMVXiJllXTj4LprGPDyklh7w4EVYcgX2UVOMjq9I11NCyfjJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇮🇷
پایان‌بازی؛ گلباران شیرازی‌ها در اصفهان؛ نویدکیا پرگل به استقبال بازی بعدی رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108138" target="_blank">📅 21:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108137">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/846f23996a.mp4?token=qAZYU-n4QCLN9p3MucUAG4s1UZNNdQvNYNjQ7424WR54ld6CXBl6gAfodyxBxucinBZR8YsV-o6Qtz0MpYsOWqFri8mcXppOfPKNzFu2u0j2QdbOC0S3M3D5M8qH8nPVddc5YFTFVWMpCa5apK7BVrvK7SLbwHUqY6f-zSt8CGHGUUVPvD4276TKnoW_IzCbly1F8etyQJ4ynlfSkKcc5zeCgmOEwlyzPE-QInk2Y8k7s93Lx5UTMLlLk--NxpbqI7-JLeMxGwrSBy0AYp4QFCx7fpCH5aFT5arIgx1VE5S-OxCjtkxEVzm34LhywciSHm8R1lhDaglqL1If40m81Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/846f23996a.mp4?token=qAZYU-n4QCLN9p3MucUAG4s1UZNNdQvNYNjQ7424WR54ld6CXBl6gAfodyxBxucinBZR8YsV-o6Qtz0MpYsOWqFri8mcXppOfPKNzFu2u0j2QdbOC0S3M3D5M8qH8nPVddc5YFTFVWMpCa5apK7BVrvK7SLbwHUqY6f-zSt8CGHGUUVPvD4276TKnoW_IzCbly1F8etyQJ4ynlfSkKcc5zeCgmOEwlyzPE-QInk2Y8k7s93Lx5UTMLlLk--NxpbqI7-JLeMxGwrSBy0AYp4QFCx7fpCH5aFT5arIgx1VE5S-OxCjtkxEVzm34LhywciSHm8R1lhDaglqL1If40m81Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
⭕️
بیرانوند: استقلال تیم بزرگیه. فصل بعد بازیکن آزادم و یه تصمیم خیلی بزرگ میگیرم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108137" target="_blank">📅 21:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108136">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31d21db945.mp4?token=EQfuptldg6s7SnbKJRR8-pW0O2AQWJZNO2bB92cykFN7STvusKURW4luwsjn7ScIa2YChQZbX6I084owwgz0SYsWpWxAZAEPdx9WQ6gieKRTkCUUqroDuhJ7uHJOzzyUo49SuIQB4ym7Pt6tzrmUTxAHTAdf7T32Uxici9bVW6CTTBPcK0AmXNY6ntCaNTKwe7FMsdGLxTJCnNCgX9Qhy8AQYGWWNVMwZqpP0nkuZwEDYEy6C0jGKTDSztN4Jv-NR-9Z3EgCWHgh1BcOgXmF-Isz_f_1HRDpAlAqmfRgjTjMNjPHMrFMRWY92eRauxRzyp9WKLVWzhBM8_ar17xPXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31d21db945.mp4?token=EQfuptldg6s7SnbKJRR8-pW0O2AQWJZNO2bB92cykFN7STvusKURW4luwsjn7ScIa2YChQZbX6I084owwgz0SYsWpWxAZAEPdx9WQ6gieKRTkCUUqroDuhJ7uHJOzzyUo49SuIQB4ym7Pt6tzrmUTxAHTAdf7T32Uxici9bVW6CTTBPcK0AmXNY6ntCaNTKwe7FMsdGLxTJCnNCgX9Qhy8AQYGWWNVMwZqpP0nkuZwEDYEy6C0jGKTDSztN4Jv-NR-9Z3EgCWHgh1BcOgXmF-Isz_f_1HRDpAlAqmfRgjTjMNjPHMrFMRWY92eRauxRzyp9WKLVWzhBM8_ar17xPXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
‼️
🇮🇷
واکنش نکونام به مقایسه خودش و اسکوچیچ از نظر هواداران تراکتور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/108136" target="_blank">📅 20:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108135">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Jokar8RcXo-MGmAEn1MKMKmycqNbCYJ6c1VVR0fc15rpwP6P-wn5CRnssGwt2Crm0zR6q49GatBqNSqi_6uzJs6ZBiKmKwDMhD02uyOOkBor0qTJC8fPMreYF_tNYnodWfuFZYQeQwAnH0pzVaxHmePYiUuURC86FBSOSXuF0DFu1GuS9ce12cpBRQqpOamsv3pjueA3chs9F3xcsdyg_Ivuq9IyQOSoyvEM6iaayUjJ7ToeiGQKL3SpP76uvbvuT33JcKMGT_NRKYU-MJLUTfT0p-mKjN-S94lB2Q0M84AyEthiePj-FA9RelvZJwgFKNfzWQGvE8uLsii0t7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/108135" target="_blank">📅 20:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108134">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=vkM9-un5eegeUwn_Nvtb-KfNB2lhkiZ6ebdic8FpcVt3moRvnxpfeMa6jZotGXOqiEZOOWbMOJavil123ZgRLuQc-4-igS9CHultLe7iFNUXBZPVKRBV3r5rfsS2GZtcLvPsR4LKKfvBYHvEcnlK6YmZBM-iHlr6DekUfFIJPjZ7J8I-k9qHu_DEVZupmMH1HN9tXT3einoKssao6Me_wCnh3J4CkW6miyYrKhCvOZEiTYBxlcF82K2ZLbLg6CGm-SMrEksLK7OY7oAMbq42GaMMH6m9eruJSQVyexGDBY28rYd0io3NhC0d_fUOV1yaQyHXiJlLinMDN-XFBN8PnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03a8cc7873.mp4?token=vkM9-un5eegeUwn_Nvtb-KfNB2lhkiZ6ebdic8FpcVt3moRvnxpfeMa6jZotGXOqiEZOOWbMOJavil123ZgRLuQc-4-igS9CHultLe7iFNUXBZPVKRBV3r5rfsS2GZtcLvPsR4LKKfvBYHvEcnlK6YmZBM-iHlr6DekUfFIJPjZ7J8I-k9qHu_DEVZupmMH1HN9tXT3einoKssao6Me_wCnh3J4CkW6miyYrKhCvOZEiTYBxlcF82K2ZLbLg6CGm-SMrEksLK7OY7oAMbq42GaMMH6m9eruJSQVyexGDBY28rYd0io3NhC0d_fUOV1yaQyHXiJlLinMDN-XFBN8PnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌ششم سپاهان به فجرسپاسی توسط شفیع‌دوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108134" target="_blank">📅 20:39 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108133">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=fUIfSM_nTiT-9jpkkIFqzkD5WeUvKsu4lDpykx28QMPpgqw4mfm0tkkysAl1U6FYir28p-oaS5d-gOqv7b9udaB4qBxdrG_4StdWFaco97UEauo7l43i-v1OdsxpWTb7ex1Z1efXziBhj6AiHJN4kzTq3lq24Qzqu-s0NCR5h-YmzAvraEz29BLy3BmkiZZGgANGplZiV_rLyDdAqmxPw1XgdGTKw3uZmIywDGozxDKgW7s_-6w2gd3BrVU8DErgtRt327DwouSnWGfW74Ds1jcktq1z7py6Gl4BW5dywTbMdOHVDYrXG7N7-Za-CPVAyQ-Boh-xPoLTnetehtnR9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded4443f3f.mp4?token=fUIfSM_nTiT-9jpkkIFqzkD5WeUvKsu4lDpykx28QMPpgqw4mfm0tkkysAl1U6FYir28p-oaS5d-gOqv7b9udaB4qBxdrG_4StdWFaco97UEauo7l43i-v1OdsxpWTb7ex1Z1efXziBhj6AiHJN4kzTq3lq24Qzqu-s0NCR5h-YmzAvraEz29BLy3BmkiZZGgANGplZiV_rLyDdAqmxPw1XgdGTKw3uZmIywDGozxDKgW7s_-6w2gd3BrVU8DErgtRt327DwouSnWGfW74Ds1jcktq1z7py6Gl4BW5dywTbMdOHVDYrXG7N7-Za-CPVAyQ-Boh-xPoLTnetehtnR9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌کاشته مس‌شهربابک مقابل فولاد خوزستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108133" target="_blank">📅 20:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108132">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
📊
🇮🇷
جدول لیگ‌برتر پس از تساوی امروز استقلال و تراکتور؛ پرسپولیس در صورت برتری در دو بازی پیش‌رو خودش به صدر جدول خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/108132" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108131">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92cf998598.mp4?token=eN9nBbJalRy6eLbmFuji08G7Da3ze9d2mbYCVUrR1y3I9SBv11Ox-xmxfUMv9vA4dWW3shAjtAzLh8JijTr6guYl-yU2s7zrK3LpLQnHMv3okj27se6-4R_C09gWnT2u5SJXW3RoLeO6c2nz_6n0_vusUU3eOluGAvfeCd4BKxe-kgJPqtwQxftV_Vs70-_N-XhyCoVgj7nI3vCxWyD_BuzAWsUfcsdOPGgw3iwRdYk0k8NO69bHD76QLhO4po3Y4xOD0pzCqV2GLA3em1_8B4ii8LqKBsr72qIjxFD4YVG07LkeP2Azzp0FS4_17SNpE5DQZaQehbZyRDgEwG3NZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92cf998598.mp4?token=eN9nBbJalRy6eLbmFuji08G7Da3ze9d2mbYCVUrR1y3I9SBv11Ox-xmxfUMv9vA4dWW3shAjtAzLh8JijTr6guYl-yU2s7zrK3LpLQnHMv3okj27se6-4R_C09gWnT2u5SJXW3RoLeO6c2nz_6n0_vusUU3eOluGAvfeCd4BKxe-kgJPqtwQxftV_Vs70-_N-XhyCoVgj7nI3vCxWyD_BuzAWsUfcsdOPGgw3iwRdYk0k8NO69bHD76QLhO4po3Y4xOD0pzCqV2GLA3em1_8B4ii8LqKBsr72qIjxFD4YVG07LkeP2Azzp0FS4_17SNpE5DQZaQehbZyRDgEwG3NZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
💙
سعید فتاحی رئیس سازمان فوتبال باشگاه استقلال: پیشنهاد داده ایم تیم‌هایی که جزو 8 تیم برتر جام حذفی در سال گذشته بودند امسال جام حذفی را برگزار کنند. پیشنهاد خوبی هم هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108131" target="_blank">📅 20:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108130">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=nhGwToA4VNX6_p2_PDiGG-kB31uIYrt_gRKbL7CW4c37zUHzlLo59zTAYk-UK_1IOCjt7oTzWBQrvSyq-kltYqllHVMzXI_1ontmbMdmxHlxikqQbLy5UVtmThHsSpN0FivbTqqfO3IeP31QSlfwMY6K6dU-6nri1Ixk3P5dY8GRzMvQz4ROWjzlGr6SLIXJoHpRJHmVTB86VKwvckscmpF1SYeZgXAZGeOnMOI4KzJXCDxqi15gqjDmmpk9Xzw5yUaxGlo2NzbkjutNIdZ1XqH_FiOQf7xRJt15VpJ1sXmdOvWq-HBoFT6LzHi87okT8ERyqJmJm0y7EfORcCW-Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/251e2a3878.mp4?token=nhGwToA4VNX6_p2_PDiGG-kB31uIYrt_gRKbL7CW4c37zUHzlLo59zTAYk-UK_1IOCjt7oTzWBQrvSyq-kltYqllHVMzXI_1ontmbMdmxHlxikqQbLy5UVtmThHsSpN0FivbTqqfO3IeP31QSlfwMY6K6dU-6nri1Ixk3P5dY8GRzMvQz4ROWjzlGr6SLIXJoHpRJHmVTB86VKwvckscmpF1SYeZgXAZGeOnMOI4KzJXCDxqi15gqjDmmpk9Xzw5yUaxGlo2NzbkjutNIdZ1XqH_FiOQf7xRJt15VpJ1sXmdOvWq-HBoFT6LzHi87okT8ERyqJmJm0y7EfORcCW-Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل‌پنجم سپاهان به فجرسپاسی توسط لیموچی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108130" target="_blank">📅 20:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108129">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f44126980.mp4?token=MkFnYZKkRu55sylH7a0GTpDLVjeII-4eUPZgV7oGidEKsJ_JIb8h_Aj2ILbKP99CDNVt1Mh99iWT3TwAd9jf7dd-TKHFU9xoO_HmGpOfDtAHLCL0j0avlzv132TiKO-vY0QzUvrLSuwLqPVpb-HBVypr2PLq2j_CWPWD24quWB0QbuMFTKX3YyUUvRXyPrdUGVSNGjDMMMVwIGxmEwao0jMLDEOcKwPNRZiheqfG1BiNUn5aBWAOe8cR_WOTLJbaa8qtV01q5P9nhJUv6aQpUfAvJYfE5VuvxmCEO23nd0wjTT0T1_ZXs9kOhWuDHX0Z4YY030vEkHDdyN7gbFe8L2Zb1gj23zXeJW0kWGE-H9Isy86ZifshDD2I5SgIwGppYc_J-DoGisgFoky18VQa0Nd8Uz0MDDVhJ5c06j1HFsfd3ljVY4uUWAjOU0ry_VAqChzQ8KKA5IZ74-ioohRYXHgKRN11OnfAeFLJDvPLGecd9p_aJLU3jwgoFkuBsFqjhlPv2njZO-kw7OC5xaI87B0LsMQ37MuAkSaNlzT6-SPLPE29fBTX-4MDXY7lfH5cQXUwFUzzp3ktuPAfrR2UpmdfYHK3YjjH8c6Gm0rdGms6wZsmYorNn4wkPU-AX_txJHXk8uWT0H5CfJapepCBgx9XaAJd-_Zl8_l1HEK5fRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f44126980.mp4?token=MkFnYZKkRu55sylH7a0GTpDLVjeII-4eUPZgV7oGidEKsJ_JIb8h_Aj2ILbKP99CDNVt1Mh99iWT3TwAd9jf7dd-TKHFU9xoO_HmGpOfDtAHLCL0j0avlzv132TiKO-vY0QzUvrLSuwLqPVpb-HBVypr2PLq2j_CWPWD24quWB0QbuMFTKX3YyUUvRXyPrdUGVSNGjDMMMVwIGxmEwao0jMLDEOcKwPNRZiheqfG1BiNUn5aBWAOe8cR_WOTLJbaa8qtV01q5P9nhJUv6aQpUfAvJYfE5VuvxmCEO23nd0wjTT0T1_ZXs9kOhWuDHX0Z4YY030vEkHDdyN7gbFe8L2Zb1gj23zXeJW0kWGE-H9Isy86ZifshDD2I5SgIwGppYc_J-DoGisgFoky18VQa0Nd8Uz0MDDVhJ5c06j1HFsfd3ljVY4uUWAjOU0ry_VAqChzQ8KKA5IZ74-ioohRYXHgKRN11OnfAeFLJDvPLGecd9p_aJLU3jwgoFkuBsFqjhlPv2njZO-kw7OC5xaI87B0LsMQ37MuAkSaNlzT6-SPLPE29fBTX-4MDXY7lfH5cQXUwFUzzp3ktuPAfrR2UpmdfYHK3YjjH8c6Gm0rdGms6wZsmYorNn4wkPU-AX_txJHXk8uWT0H5CfJapepCBgx9XaAJd-_Zl8_l1HEK5fRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🇮🇷
سوپرگل امیرحسین جولانی بازیکن فولاد خوزستان از وسط زمین به مس‌شهربابک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108129" target="_blank">📅 20:17 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108128">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic85fY3yffouKx68HrDHmgayBCI8o3LRZSUamOzxkaHyZAqz78Bi9nfoUcnV-Nuj_HYuoerKdjU3blUZ5JP9qB15j-K9_esKZfV7TyC00ovOm9JBEegsEo4GXlN2-VyRak4ZwFd35GrqBmcPR0g3CbaxRC6JzsQ8xrKL0rywVlNTi2_tqkzkY30JaeQicRTfmw35WBe0dcVCLEed7m8eh4J6Yao8FSJirIGOH2okcGeN-H9hqLawpbnGFk98bVmeIc_daX2GYoBipcQ4vgdf0lHUlrqADsfcVI2-JOVbeDfSK3beZlkVAYvjPXSac9TgDRPh7zZvLXRGpcDibDdzkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108128" target="_blank">📅 20:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108127">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36afca847.mp4?token=lpOIEGwPE4EJFp5U5eWozXTRN67bta_U14z7juJh0W-TdVhk48Ez1zl7UqePCMhsZeQimrNxm9iHVViKndKLQOTsaqY2Qi9rviRoFJtXWX_2gu0OAABto4LT9SA4eSCbBhhHvmrDKyUjnhU_zwBDCzbX5R8NBY_WAlFdNPfbQmPWaC94wPtI5OCkrSkmZfJiBYxlDkP_NVx70HykgMHmbPD1P15JPOYDdI-Ff4QqF2lTUYgebgk0EEqZsv1BnGJFxfc04K9Dwy6trtK6-TwQA8oAh_aisIX9eJLG4mc-tyhvp_WlwIySld4oM_fhUO8W5nLQWpsuhJknOnQGbMg9xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36afca847.mp4?token=lpOIEGwPE4EJFp5U5eWozXTRN67bta_U14z7juJh0W-TdVhk48Ez1zl7UqePCMhsZeQimrNxm9iHVViKndKLQOTsaqY2Qi9rviRoFJtXWX_2gu0OAABto4LT9SA4eSCbBhhHvmrDKyUjnhU_zwBDCzbX5R8NBY_WAlFdNPfbQmPWaC94wPtI5OCkrSkmZfJiBYxlDkP_NVx70HykgMHmbPD1P15JPOYDdI-Ff4QqF2lTUYgebgk0EEqZsv1BnGJFxfc04K9Dwy6trtK6-TwQA8oAh_aisIX9eJLG4mc-tyhvp_WlwIySld4oM_fhUO8W5nLQWpsuhJknOnQGbMg9xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گل چهارم سپاهان به فجرسپاسی
آریا یوسفی در دقیقه 54 دبل کرد و گل چهارم سپاهان را به ثمر رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108127" target="_blank">📅 20:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108126">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=P2ALipjIwGSSRNEJpDedwnMGGftER1JqXcs0swhkSKzWBIhVIS9RnXUP9wqrIZz6CWW8qg4OLKYrojSEFpSUKz_y-GOXQyyVViRQrUzt6qYN9tOH7KTDfn_qo_IPB7iTZ9qykFrVBxGwxrv9ZYvoXa9YZdC-k74MTPseSGayCrOvCnBWHh5ezj3gzTx9D8vuapIU-X3z9tjiDSu9PEe-ZDk9u8pGaO4zIg4ibgmILtsidGQVMQ2j3kAbCNAAgPOATx2igjwOZ8IS9wC7dw_SBCbF2RroJ0Lp6QhpRQyxQ0B-q4yJ_xEl1AW9sR9xiEbAnyIwMCGum9I379G3lk04hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb8c7cf69.mp4?token=P2ALipjIwGSSRNEJpDedwnMGGftER1JqXcs0swhkSKzWBIhVIS9RnXUP9wqrIZz6CWW8qg4OLKYrojSEFpSUKz_y-GOXQyyVViRQrUzt6qYN9tOH7KTDfn_qo_IPB7iTZ9qykFrVBxGwxrv9ZYvoXa9YZdC-k74MTPseSGayCrOvCnBWHh5ezj3gzTx9D8vuapIU-X3z9tjiDSu9PEe-ZDk9u8pGaO4zIg4ibgmILtsidGQVMQ2j3kAbCNAAgPOATx2igjwOZ8IS9wC7dw_SBCbF2RroJ0Lp6QhpRQyxQ0B-q4yJ_xEl1AW9sR9xiEbAnyIwMCGum9I379G3lk04hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل سوم سپاهان | احسان حاج‌صفی '47
سپاهان 3 - فجر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108126" target="_blank">📅 19:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108125">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=XeYco3vDgOGvqABL8XmoNgCAnh1BQpvunWwXtm0dn8ehpyP2KPrqBBC3aNd79mSYsIOxIsHPNklEKee7UbcCveYl2P1FCLH9LoBzGvwdr9PnkdeuMzURXgtyZaP15jNms9TUjlCB_WUgsHj0aKzMF0X6SCXmmejsrvITIOdeG8N8wnseIa9knV-aYp_feZ9MO1gOGEZuWYyIAvaWjG5FY2SKE_yFK80Ws5U4yx7d-kBp5hbtWcsRUEtHQpLoVDb4agO4pOOUgH8elOxQo9hSRIgKs6uneQCcglqxGluO7FtKIF7Tty6hI3XEprkcQRbRrRD4OuzgbA1YE0Xb2oohxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da3e24c2e3.mp4?token=XeYco3vDgOGvqABL8XmoNgCAnh1BQpvunWwXtm0dn8ehpyP2KPrqBBC3aNd79mSYsIOxIsHPNklEKee7UbcCveYl2P1FCLH9LoBzGvwdr9PnkdeuMzURXgtyZaP15jNms9TUjlCB_WUgsHj0aKzMF0X6SCXmmejsrvITIOdeG8N8wnseIa9knV-aYp_feZ9MO1gOGEZuWYyIAvaWjG5FY2SKE_yFK80Ws5U4yx7d-kBp5hbtWcsRUEtHQpLoVDb4agO4pOOUgH8elOxQo9hSRIgKs6uneQCcglqxGluO7FtKIF7Tty6hI3XEprkcQRbRrRD4OuzgbA1YE0Xb2oohxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری‌زاده : یاسر آسانی بازیکن تاثیرگذاری است/ بازیکنان تعویضی تلاش خود را کردند.
🔵
کادر پزشکی تلاش می‌کنند تا او را به الغرافه برسانند.
🔵
امیدوارم مصدومیت او جدی نباشد ولی احساس می‌کنم کارمان یک مقدار سخت است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108125" target="_blank">📅 19:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108124">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=lhArvIoUtzGpr3B2uQaegpTzqveJ5mJNub3BD-iP89tMi_G2Gnob23VvpSt4tLw7cIqKiHpKnMUZTd-9i0__KjXbNlaIhXdnLVRG7FjPgUTOL-3nyCQX33c-pt8BkyIBHIV1Jrwl3jPdxheIKIQQjYPVWKD-vE1_JCnPx1irXPVSffznM16AkNDbvPK6Wus5H9PKBNAKPnGhKhiysJz4MouT38ELKyRZlrEDJINmdAlUKkbfHuUIXWVlQWQIjhgZMF44XXGpR_V4i2syqHUkmulKdyGMaHCcETW5ETL19jiPlqvRegIlkrEoYXQCnp7qFrG8eW2Lbv-YVN4aODqMFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dbd7f5f47.mp4?token=lhArvIoUtzGpr3B2uQaegpTzqveJ5mJNub3BD-iP89tMi_G2Gnob23VvpSt4tLw7cIqKiHpKnMUZTd-9i0__KjXbNlaIhXdnLVRG7FjPgUTOL-3nyCQX33c-pt8BkyIBHIV1Jrwl3jPdxheIKIQQjYPVWKD-vE1_JCnPx1irXPVSffznM16AkNDbvPK6Wus5H9PKBNAKPnGhKhiysJz4MouT38ELKyRZlrEDJINmdAlUKkbfHuUIXWVlQWQIjhgZMF44XXGpR_V4i2syqHUkmulKdyGMaHCcETW5ETL19jiPlqvRegIlkrEoYXQCnp7qFrG8eW2Lbv-YVN4aODqMFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🟡
گل دوم سپاهان | احسان حاج‌صفی '38
سپاهان 2 - فجر 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108124" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108123">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=QCyBQzB2pRNfu4zk3Xut_chJtdUoqqYLmhWQruFECv8T--ZE_z1duspfbEDVgn0GSk_BsXSNt8PX2liy-Gzdj21sjylMp7v3mqQb8VrpMcsfPxLYI35XWtWuxaZmpNveGhY3CUwYPCkH-3Ao6CuXtOL3f-gHGnrqoo5CrGYy_supESP5YMWszZPJ6qmyEMgwmfqmKTi880LBwW0cFM4HH4XTs0ckAv_au-HxO_BbyVvKxr-gxRtTuCErQt6o5m4YQnm9be-JK0KATafqaivAWwoKYWMqt3YfeuuDfRcCliPKucRLOOlJoMaLX_JB1cTy-Dd-8YbGSA87MvBRyi2fRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd8faa668d.mp4?token=QCyBQzB2pRNfu4zk3Xut_chJtdUoqqYLmhWQruFECv8T--ZE_z1duspfbEDVgn0GSk_BsXSNt8PX2liy-Gzdj21sjylMp7v3mqQb8VrpMcsfPxLYI35XWtWuxaZmpNveGhY3CUwYPCkH-3Ao6CuXtOL3f-gHGnrqoo5CrGYy_supESP5YMWszZPJ6qmyEMgwmfqmKTi880LBwW0cFM4HH4XTs0ckAv_au-HxO_BbyVvKxr-gxRtTuCErQt6o5m4YQnm9be-JK0KATafqaivAWwoKYWMqt3YfeuuDfRcCliPKucRLOOlJoMaLX_JB1cTy-Dd-8YbGSA87MvBRyi2fRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108123" target="_blank">📅 19:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108122">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=nG0n2imOKNkg0oTH4SB_sVNJT6sBXsKeEZYjxtQ0QwMEVG3a4zk-HwjdPu8nFQaSR0aS2D1XXyKW67eEpSN45IbSVPWuGQ86A7xr5Vqih-dNUhmdpArbGIdfaIM-7akLgioPgauuNxHReSSJr1hUeaYAD9Tahsus2w7xmtUm4AMyaHNiUSspWwKOTm5FZqFizWhNBU3g-FH_rstjwh0scKCCoPHqw-sdzPhLavALFF94L6mh5hZYp53zaMcXhXc62VfQpHI8_0fnXRAQ8K-Kmn0mHA1jYlJ8N60LqFWzlFGCAD67NVupcq7qq2MuFx3JZyI483htI-fWitqjM0GCew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f54d246b.mp4?token=nG0n2imOKNkg0oTH4SB_sVNJT6sBXsKeEZYjxtQ0QwMEVG3a4zk-HwjdPu8nFQaSR0aS2D1XXyKW67eEpSN45IbSVPWuGQ86A7xr5Vqih-dNUhmdpArbGIdfaIM-7akLgioPgauuNxHReSSJr1hUeaYAD9Tahsus2w7xmtUm4AMyaHNiUSspWwKOTm5FZqFizWhNBU3g-FH_rstjwh0scKCCoPHqw-sdzPhLavALFF94L6mh5hZYp53zaMcXhXc62VfQpHI8_0fnXRAQ8K-Kmn0mHA1jYlJ8N60LqFWzlFGCAD67NVupcq7qq2MuFx3JZyI483htI-fWitqjM0GCew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
شجاع خلیل زاده بعد از پایان بازی با عصبانیت بخاطر تصمیمات داور، راهی رختکن شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/108122" target="_blank">📅 19:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108121">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=UYYBBkngOJ7jqOweW86lUweKqt1AJD-Aq9P7UOHfgiwtsjl1HJLjdq8vdTEd1ZxdGemenC9bvELk-Z_A-IXmZRMSLDKte4e7C301IsuC6zICGWrQdATJlxnNq99cBR7HbBiNdwCExEOGJpKkXYN-Df_z_5Pxs7BTYXPE8pCP3vpnsi0KduNCIgn6XkARra7N2mQ5pmcob6DICsP2DxyKWBkkS60u3ibSDmC3rjuf1fSSOsokRB2L3tDQrvfy4y81rjYpBmCcJIxw-kqZhQoQY-vccG0kf7BMiEyNPVn3NV0DN4khMS4ITSeiaNZ5bus6xqX7Ewgxbk9Gf5nzqxTglw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/238e05c12f.mp4?token=UYYBBkngOJ7jqOweW86lUweKqt1AJD-Aq9P7UOHfgiwtsjl1HJLjdq8vdTEd1ZxdGemenC9bvELk-Z_A-IXmZRMSLDKte4e7C301IsuC6zICGWrQdATJlxnNq99cBR7HbBiNdwCExEOGJpKkXYN-Df_z_5Pxs7BTYXPE8pCP3vpnsi0KduNCIgn6XkARra7N2mQ5pmcob6DICsP2DxyKWBkkS60u3ibSDmC3rjuf1fSSOsokRB2L3tDQrvfy4y81rjYpBmCcJIxw-kqZhQoQY-vccG0kf7BMiEyNPVn3NV0DN4khMS4ITSeiaNZ5bus6xqX7Ewgxbk9Gf5nzqxTglw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
گل‌اول سپاهان به فجرسپاسی توسط آریا یوسفی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108121" target="_blank">📅 19:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108120">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmF2xXTRuN8Lb08kyGNVVmwFdhUbGqD9MsDv3EQyp3OuV64o59HiYK2WXFZFDPliRfRbIKRILb3hEbbxtU5cgWwzNijnsMJTfKF2VUZ3dFXv70Bj3XUFG6kntJ9q56tKDV8-67DKeh0-TrJ7HWpYNti99QE9fuBnDSiC4bih2UpAgGuT5tPmWH-lUctCZv3RVjchBn4BY1tRPTKZZj0AcHjCM5mgx8o8sGbdYzpW5pLxXpG_Bo4KJCJnpqIEQj6CBtEwUYhumgmxPvbuF-aRLCbzzQANhIInamDmrnj7B1o3TPORctDURFeyVOdzvlLAygo2zqI50jRJyfT4fKrCsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🚑
🇮🇷
براساس گزارشات از رختکن استقلال، مصدومیت یاسر‌آسانی جدی است و احتمالا حداقل یکماه از میادین دور خواهد بود. باید تا انجام معاینات پزشکی و نتایج آن منتظر بمانیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108120" target="_blank">📅 19:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108119">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTJ0Xp-HevS_NeJyh0scpWAFUkCp2EySRB9U3HBBUTsZYjkJHZUs7ue5RKAEwWeTvc49RNkArnU1Xn5NgdPbMeu_1d4RZGG0L12A0xRIerdKc5XOwezeQeXF7C4kNYP_S46HusKOUCpzoXEhGIxIdTjg_K6z4tGnlPSfWMJuZnjUsrL-dv79B3mO6tIlNAXBJfN3hJKy5iEXHLqxMZvGiWk6crugJ8WqLnMBvSX9uewGiW6zXXH2Y5BCYTNeORP8Zvd_8DWZueJpmKOQJpdcw4igpf3JvsSz1wxu51p4-ZzanIm46hMooWNpFk_RgQYX1LiaKDcKIaRJOZgVR9BLTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108119" target="_blank">📅 19:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GxiepUfJgcyiC0k5K8Gbidcry3RBeqZzmfrhyVzzebVHQFODFISFgHQS-YoKZi_vswEJL3k33GkY4kHYyZzSiZNwgKb3G19CeYwRCOLQGmhuVaHZdzn9zilGIP2QnX_TIoXrJbmMCse5IdtA6StHZbwzsGm12V90vhWPofeDXinYiwonnLV4_z3vADacKbyswgkPO9ZTUwkl2sqZe3t0KHpZO8ddQ8qo9Jb6iRzT52qdN2eXv1JfuKxP9b83x6mfiV8yjAmS6XFa1WNmciwGQAVjkwTOeqrDPVdwYB8mVXhYPlITObR_2dmovao3KBkdPh5KxZSmkXskIjNpeVJzWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
هفته‌هشتم لیگ‌برتر؛ تساوی در جدال بزرگ هفته؛ استقلال با مصدومیت آسانی راهی قطر می‌شود
🇮🇷
استقلال
1️⃣
-
1️⃣
تراکتور
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108118" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=aCF03mBwG8zDMgOUtB26I1zmADSbuIWU3mt2d7ntB2A9Nw9LRfnkVlxNwF_BSPxl_iAyM2DyhWHnBnxcG5ZKIuDNdE20geQ6Q76qVjkVMTp1HeN3NfQpmv-s7lR5HdH-viv6w_2aOXUxAxUO3MrNTQzazJxzow7PsCZf-ickPKZQIzui6l02ElofIKVmeNVcVv3xrJuP3X6cEhZ-Z-r8r2aEdln8IHctRKM4Bd9m1W12zV-nJ6ZxbYtVLPSnGE8s6ekXUXyTUYtDXUdl_J-wBeonAOpVyj5AT12_tinzezqdtCiUCMBaPQo95jQT6HTMJqbQsxtl1u5RgETLuCLO1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52b9315c21.mp4?token=aCF03mBwG8zDMgOUtB26I1zmADSbuIWU3mt2d7ntB2A9Nw9LRfnkVlxNwF_BSPxl_iAyM2DyhWHnBnxcG5ZKIuDNdE20geQ6Q76qVjkVMTp1HeN3NfQpmv-s7lR5HdH-viv6w_2aOXUxAxUO3MrNTQzazJxzow7PsCZf-ickPKZQIzui6l02ElofIKVmeNVcVv3xrJuP3X6cEhZ-Z-r8r2aEdln8IHctRKM4Bd9m1W12zV-nJ6ZxbYtVLPSnGE8s6ekXUXyTUYtDXUdl_J-wBeonAOpVyj5AT12_tinzezqdtCiUCMBaPQo95jQT6HTMJqbQsxtl1u5RgETLuCLO1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال توسط حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108117" target="_blank">📅 18:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سید مهدی حسینی</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/108116" target="_blank">📅 18:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تراکتوروور زددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108115" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108114">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/108114" target="_blank">📅 18:35 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108113">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=UpfpocweJejpdB-TdSvepfuSzG1fiOl7NdSWTFDUlbMiZU8h4Oq3bYN-DjEusonToZB72OzLYip9xRRRnTl40suWuhDlwCJCbvYjoJh1DL6lgF37KB2kFGXi2uTPLgFJxhdoghAFan3oqeeG9MlCPCxBaI_aXgVASjXR6flIISr4KKZQG21dmO84Lb0Oz-77CxJaj5WW9qXvJ-ZWSVa03-ekzKlK9n61fsq5UGyUq59etfrgt5z2jynJkM7SZAENSWdLSe1xSL2WmMw6F9jwAYSqQMy9A6V6OSXQg-4Vyuil3usY0w6agGIjSvWOlM4wvCAnVSkqezAUEq9ZgQOwGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d3b589fa0.mp4?token=UpfpocweJejpdB-TdSvepfuSzG1fiOl7NdSWTFDUlbMiZU8h4Oq3bYN-DjEusonToZB72OzLYip9xRRRnTl40suWuhDlwCJCbvYjoJh1DL6lgF37KB2kFGXi2uTPLgFJxhdoghAFan3oqeeG9MlCPCxBaI_aXgVASjXR6flIISr4KKZQG21dmO84Lb0Oz-77CxJaj5WW9qXvJ-ZWSVa03-ekzKlK9n61fsq5UGyUq59etfrgt5z2jynJkM7SZAENSWdLSe1xSL2WmMw6F9jwAYSqQMy9A6V6OSXQg-4Vyuil3usY0w6agGIjSvWOlM4wvCAnVSkqezAUEq9ZgQOwGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
داور بعد از بازبینی VAR گل تراکتور را به دلیل خطای هند  بازیکن تراکتور رد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/108113" target="_blank">📅 18:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108112">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/108112" target="_blank">📅 18:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108111">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
احتمالا خطای هند بازیکن تراکتور</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108111" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108110">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">صحنه داره وار بررسی میشه</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/108110" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108109">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726254fc85.mp4?token=K6l_mHlhtPHEaTzYrMA-ubD7bO69NUqgLRbCCStziOT3hq1J9F0-FlE6jI6ID8ajjlN-47Px2EfgWaRuevnD4JZTtssaTxgSEUm6KqbZqo38h-4P6W0meKJHAB9XNjvehWCluOJYyvYHsEZ4LZJrOyMGn7Xmv9t2-3dwjhIUCCe5Scd5cRKIaXYelMeIAXh3brvKYB-fubDp4rCpTJ72dRIofnmrOK1JskSH7ToTXlZd-H_uUYFsbXSHqo4kRIsA6FhVRgw6dzrccmHtq6Bz12EcCCk3Z3VpQ3pFaIRISPFAkoUIQWJQKt_gadmZBH8VWvLyyT7SMbJtxeZ2q_JgjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726254fc85.mp4?token=K6l_mHlhtPHEaTzYrMA-ubD7bO69NUqgLRbCCStziOT3hq1J9F0-FlE6jI6ID8ajjlN-47Px2EfgWaRuevnD4JZTtssaTxgSEUm6KqbZqo38h-4P6W0meKJHAB9XNjvehWCluOJYyvYHsEZ4LZJrOyMGn7Xmv9t2-3dwjhIUCCe5Scd5cRKIaXYelMeIAXh3brvKYB-fubDp4rCpTJ72dRIofnmrOK1JskSH7ToTXlZd-H_uUYFsbXSHqo4kRIsA6FhVRgw6dzrccmHtq6Bz12EcCCk3Z3VpQ3pFaIRISPFAkoUIQWJQKt_gadmZBH8VWvLyyT7SMbJtxeZ2q_JgjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❤️
گل اول تراکتور به استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108109" target="_blank">📅 18:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108108">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تیبوووووور هالیلووویچ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108108" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108107">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">تراکتورووووو زددددد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108107" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108106">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108106" target="_blank">📅 18:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108105">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همچنان استقلال از کووووون میاره</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108105" target="_blank">📅 18:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108104">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">استقلال از کوووون آورددددد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/108104" target="_blank">📅 18:23 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108103">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppyk0v_gHL4fc8HcSebOR6D5tOhqmfQdUE5eKyZ9LeI8O8AYGfTwRlImiz2DzqTn1e0Lgt80LfL-JhIeiCRPvE4a2sf_4zWQlThlziiDFIaNeN3dkp42X3Vkjt19NfmcNmOILrXW7dqMONyHXP4nBNEqC-nc3EtNwj4JQS1109iudtD3H375fs0DilNTonDCgSmAcgUfR-Gb6arqWLetiKWL20Yj5QGPKZXRN5vGIs-GF6X1Msz7kRoiuYAaVxht83TBNIUpm6cWCbV0xiRnLi0hoJ1sdmhvecoxI1oThHmK2fJmPuFNJjLVJqoPxE5dcRUrEhtua-oQ2ZJv-Q3Wrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ترکیب تیم فوتبال فولاد مبارکه سپاهان برای تقابل با فجر شهید سپاسی⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108103" target="_blank">📅 18:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108102">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRloVY5XxMlTMY_dfOd2KPtJFY_MB_QFYMQbTsgjfPpCpBrQ_lhOWEP6Ny7_xLMgimnOdRgJKhun4qeMm2VQls7QebGn-8SUm5ykZGMj-fFobm6f3M7mgqWGFhkmIjA3B55rQNP0mRuXCdV55KGvhyXPZwCbHj7ZuiiQJYK9T7z4rHopX31vlA--k2ueYaIY1Uf9C7JITM-jIjGg6Uwvta9aiz-2CjbPOXSeuPUWPcpeir0yGWDz4D3fDj_BVV78uiFkFBRqzRN_DZ6vUo1DxKt54qqHvsvGWgvGWl7KxmFuuFXXsO-M9jNqKJV8J9605sZf5Efnz5TtQg8T2JP-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📲
استوری منیر الحدادی درحال تماشای بازی استقلال و تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/108102" target="_blank">📅 18:11 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108101">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=VBETB44oAT5oyV9LP7yDN55dFhM31pZW3Ni0f8rlLSo3HwmTdCG63tv1V4aUjpcc3vBFK61wbExFATaZ__4A3Sh1mjyn_wqHAox4INGYci7desodWQOliYPRJ78_LJwFTpRBtU0mHJdOHa6ccLkUW6018fmTbXGDM8SWnhuCzu_7hlh7QGuFrqNSCBaRsRoFtVFPeU3YeJMVfbT5w3eQdq9jxDGtF9ko5d35QPGwNo7lIJ0PKXNP26OcjIa7vH2hwmMMJhp30HzbuYDL0A2BDeATvHux7ZAyFdr1KY_qjKkV4Tl43qM5s4X8e6-LssypdOlradkhi0DAZTGEb6oCVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a57047d91.mp4?token=VBETB44oAT5oyV9LP7yDN55dFhM31pZW3Ni0f8rlLSo3HwmTdCG63tv1V4aUjpcc3vBFK61wbExFATaZ__4A3Sh1mjyn_wqHAox4INGYci7desodWQOliYPRJ78_LJwFTpRBtU0mHJdOHa6ccLkUW6018fmTbXGDM8SWnhuCzu_7hlh7QGuFrqNSCBaRsRoFtVFPeU3YeJMVfbT5w3eQdq9jxDGtF9ko5d35QPGwNo7lIJ0PKXNP26OcjIa7vH2hwmMMJhp30HzbuYDL0A2BDeATvHux7ZAyFdr1KY_qjKkV4Tl43qM5s4X8e6-LssypdOlradkhi0DAZTGEb6oCVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشک‌های یاسر‌آسانی هنگام تعویض از زمین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108101" target="_blank">📅 18:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108100">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
⭕️
یاسر‌آسانی در پایان نیمه‌اول و پس از سوت پایان بازی بدلیل مصدومیت روی زمین افتاد. باید دید در نیمه‌دوم تعویض می‌شود یا خیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108100" target="_blank">📅 18:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108099">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⭕️
یاسر‌آسانی در پایان نیمه‌اول و پس از سوت پایان بازی بدلیل مصدومیت روی زمین افتاد. باید دید در نیمه‌دوم تعویض می‌شود یا خیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/108099" target="_blank">📅 17:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108098">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab3fc2522.mp4?token=c90q1NRLOpALEBuItp5hbhjiMgsfRWCLCTsm-6OBaixmFPLYOKRkwLfahLofdTye4TgjUmU8sdrh-iMlWhtLtqR4PhumYDKa3VTS9n2UKsAJjLcxkjaovgXdyYwxB1_7jQlf2Rx4wan3LxB9YDTuR_zkydtMP08W4T1b_FcWyLs397VSpqFJkzmvUrMX2nxABm9Z04RDRs_0Nbe8PGbspOQvtuicelrPd7UaBHwTARwg38811JZvFRAlZLYBQAzMug4GqvNYg3q13EClq0kyv7Q11OI_MeC-duvdX6a0QLAi_V3WVqVwa-wOG98V6gp0LzcbxbAJ_x4CjyEa6MK9vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab3fc2522.mp4?token=c90q1NRLOpALEBuItp5hbhjiMgsfRWCLCTsm-6OBaixmFPLYOKRkwLfahLofdTye4TgjUmU8sdrh-iMlWhtLtqR4PhumYDKa3VTS9n2UKsAJjLcxkjaovgXdyYwxB1_7jQlf2Rx4wan3LxB9YDTuR_zkydtMP08W4T1b_FcWyLs397VSpqFJkzmvUrMX2nxABm9Z04RDRs_0Nbe8PGbspOQvtuicelrPd7UaBHwTARwg38811JZvFRAlZLYBQAzMug4GqvNYg3q13EClq0kyv7Q11OI_MeC-duvdX6a0QLAi_V3WVqVwa-wOG98V6gp0LzcbxbAJ_x4CjyEa6MK9vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
نوید مظفری، کارشناس داوری: در دقیقه ۴۱ بازیکن تراکتور هیچ خطایی روی بازیکن استقلال انجام نداد، جاگیری، زاویه دید و تشخصی داور عالی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/108098" target="_blank">📅 17:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108097">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/827ca52e8f.mp4?token=OQYV-p3zgQJ3Tw-RqAAIj_g-ZLFxiEI4FFmu-drohDTc9QGvYULIRhXe0BEz25qOGqP_29pGwFIFx5JWjTGEK5An2qF6ofJUmJMGvl_XvtKQYT64dZ_DeMQYrl2sQkfT3L74N4PKntYo549P2MUb2OKs0AzeNOlfD7fENBpmoz7N4Vboz9UyTPhZgjyQTeCypk8KqYwh1QycDwiypWy4medDmWRqQgbne0k9JdWqJZYCRgsLL1c-j0bI6PrenPAww_wX-nKWDYUFlJQzingDK6oSEwS2i8VKszPwzBgjw5uz1MtSmjcAGAZ_CMuOSsGgqWX2Lu0BFTrvUFCBYiL2uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/827ca52e8f.mp4?token=OQYV-p3zgQJ3Tw-RqAAIj_g-ZLFxiEI4FFmu-drohDTc9QGvYULIRhXe0BEz25qOGqP_29pGwFIFx5JWjTGEK5An2qF6ofJUmJMGvl_XvtKQYT64dZ_DeMQYrl2sQkfT3L74N4PKntYo549P2MUb2OKs0AzeNOlfD7fENBpmoz7N4Vboz9UyTPhZgjyQTeCypk8KqYwh1QycDwiypWy4medDmWRqQgbne0k9JdWqJZYCRgsLL1c-j0bI6PrenPAww_wX-nKWDYUFlJQzingDK6oSEwS2i8VKszPwzBgjw5uz1MtSmjcAGAZ_CMuOSsGgqWX2Lu0BFTrvUFCBYiL2uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
موقعیتی که یاسر آسانی به این شکل از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108097" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108096">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
صحنه مشکوک به پنالتی برای استقلال</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108096" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108095">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/108095" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108095" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108094">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYURxcUFkMhA89NErbkClaCpO1fV9j4LXfc6Z2WogcF7-jtxihbm5b5Sy98dIfM7D-Yp0tjH2BqOrOjJDVHoqUf_6K4HSuBbMcexYHVv4G93MTuu0G8IiavoBgLBjTIKmh7BYGmapiVZZvxWAN7KW80CO1z1VAR6vzDKW_ShWkPKlAkvyMrIvO-JHAFoZWyDdMEpNxZ7PMdvHpB2-VTg6glEA3WevEgdPojoF0AnLG0dcf1GmEkK16heIeLJaJz5rkNQf1dRAQDhkxFOdp6BI3MfpV6nFCbgyj-Iegyi71_Fn3F54oFZOyNVmNrKtjitqOtAzADurGMBGTGHpaJfDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/108094" target="_blank">📅 17:42 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108093">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c9b37ccf7.mp4?token=exeVjZpmw5cYbzOMjYiUL6F-Mt1MjdrVuRWC6dLxApCW5HCT0gQYCp55R8rVzT1sxwJ-8f_NwK-Q9PI_AS1Gu2gMNiSCwG8ZAImUMdZ3gcTYWnEDx5y-zl9r-qwrwwmrh46h4hY0eer-t3f1MU9RmKEPGYkmWpndBELmuk9EHUDntzeOC4yjNroMHS1SEz0GageHpPQbJGSqzsX58RVq3Hpn8Gh8uAjT_LbrhkFPLP5ahYOLPpWbharA1xgD0H2n47RLP_hje13KCpESMI2rDyi2UwgW1vUliqXlEvxt9zkUc4-q1NhB8_vGmKaX28S49C5Dr9dQw1pzUALiyJaRqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c9b37ccf7.mp4?token=exeVjZpmw5cYbzOMjYiUL6F-Mt1MjdrVuRWC6dLxApCW5HCT0gQYCp55R8rVzT1sxwJ-8f_NwK-Q9PI_AS1Gu2gMNiSCwG8ZAImUMdZ3gcTYWnEDx5y-zl9r-qwrwwmrh46h4hY0eer-t3f1MU9RmKEPGYkmWpndBELmuk9EHUDntzeOC4yjNroMHS1SEz0GageHpPQbJGSqzsX58RVq3Hpn8Gh8uAjT_LbrhkFPLP5ahYOLPpWbharA1xgD0H2n47RLP_hje13KCpESMI2rDyi2UwgW1vUliqXlEvxt9zkUc4-q1NhB8_vGmKaX28S49C5Dr9dQw1pzUALiyJaRqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رقص آذری سعید سحرخیزان که باعث فحاشی شدید هواداران تراکتور تبریز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108093" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108092">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2859c6f67.mp4?token=gA1QAUvfC9o4Ni3iEW_BwUjCjSgQVn-dOD1gcLpalZCkdLtZYaEb9CXaOZv3eeBCoXupBfTn7ebHE_mOcpTNEERlzeFXlHIwDUQ11Jbs4Vzt1POH16tb__GTXOAeAoS8XMyGlQjdUxWUOhJPl8bxO3iHT69yvs0FR2iBe2aK3MEdDwM_gNs3Vpqhr5H9jsNRW7fzlQ0ZOvyWAqKkSiOJctkELkMU-7VO0O7xsbk5qdnttv-emSIcVeEHTWASbqEg3fAG6c7XhWmDddAHdegRB2fSQovsMeR4mK7CJplV6zFNb1bOGxArhJMg47zWpFZwh5yr9J0xwpcFotkuznkKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2859c6f67.mp4?token=gA1QAUvfC9o4Ni3iEW_BwUjCjSgQVn-dOD1gcLpalZCkdLtZYaEb9CXaOZv3eeBCoXupBfTn7ebHE_mOcpTNEERlzeFXlHIwDUQ11Jbs4Vzt1POH16tb__GTXOAeAoS8XMyGlQjdUxWUOhJPl8bxO3iHT69yvs0FR2iBe2aK3MEdDwM_gNs3Vpqhr5H9jsNRW7fzlQ0ZOvyWAqKkSiOJctkELkMU-7VO0O7xsbk5qdnttv-emSIcVeEHTWASbqEg3fAG6c7XhWmDddAHdegRB2fSQovsMeR4mK7CJplV6zFNb1bOGxArhJMg47zWpFZwh5yr9J0xwpcFotkuznkKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚽️
⚽️
پرتاب بطری به سمت بازیکنان استقلال بعد از گل اول این تیم به تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108092" target="_blank">📅 17:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108091">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c35a7666d.mp4?token=Zzvfo3g5nlkS56Yt4loKsfL8NEOapyCy2WhDRXkVNs-l_7w2qi2XEsbdwCXdbtYz3lzFJ35Xz-r2VCKOU8gy9PLonr6ahufyGG8872C-jGTGXZMXa2mSkxD7YHB_WPCuj9pv59P144viA3STBiB5GRhRr7Fj-JLEzI1Dx1bpLvs5qF8gKMy5eRqINBov2r1hvhZ9N6tSWxSG-pT8nAWNi9glFpSv13mk9bjZTkbLQZh4TuoY4gsozuu6XSjB2IKF9oUEWzKVS_XKyLtWpWc7Geh-UoS3_wHuV5g5RR_SI0MpRrWt3ijIQsnfeASpqNJiBQEWZQEJ6yYOFcNtUoZMvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c35a7666d.mp4?token=Zzvfo3g5nlkS56Yt4loKsfL8NEOapyCy2WhDRXkVNs-l_7w2qi2XEsbdwCXdbtYz3lzFJ35Xz-r2VCKOU8gy9PLonr6ahufyGG8872C-jGTGXZMXa2mSkxD7YHB_WPCuj9pv59P144viA3STBiB5GRhRr7Fj-JLEzI1Dx1bpLvs5qF8gKMy5eRqINBov2r1hvhZ9N6tSWxSG-pT8nAWNi9glFpSv13mk9bjZTkbLQZh4TuoY4gsozuu6XSjB2IKF9oUEWzKVS_XKyLtWpWc7Geh-UoS3_wHuV5g5RR_SI0MpRrWt3ijIQsnfeASpqNJiBQEWZQEJ6yYOFcNtUoZMvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💙
گل اول استقلال به تراکتور توسط سعید سحرخیزان
28
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108091" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108090">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اوه اوه هواداران تراکتور رو تحریک کرد
😐
😂</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108090" target="_blank">📅 17:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108089">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سعید سحرخیزان</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108089" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108088">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">استقلال زددددد</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/108088" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108087">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">گلگلگگلگللگل</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108087" target="_blank">📅 17:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108086">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
‼️
✅
تایید خبر اختصاصی فوتبال‌180؛
🔴
شکایت بابت مجوز کار بازیکنان! نامه باشگاه تراکتور به پلیس مهاجرت و گذرنامه آذربایجان شرقی درباره بازیکنان خارجی استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/108086" target="_blank">📅 17:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108085">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2316aee10.mp4?token=qpL5KFzAMuUgKEyG9ovlkyH1LbohWQskPBR1oWZpfL0aKjTzZ8FSKHrzomVcFb1iHtTszRd3-hjn_k0kFGTJNadyDx5qXPFpsb6LNktqfkg9FTMAEdnGK_nzDyK_rSSgCN-KtPXO30ATTkUeL9pZkuVDFJttqxfWkpZa8t7pb5bP9Fluxeqrzh5_EplCVQdgESM_Jkr9PrU-wyiTlmstnwtVLLWksSxttjIeIqQmZ8p2NpjzOA0DMPzy41YigE11y-hxBOT9YFHd3KZ7IEhGmMStojCKPi0WazdoN4SkTEazzMDK5LPSDBPinucXDd3CUER2LjHUhpHsxS5yhvoC4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2316aee10.mp4?token=qpL5KFzAMuUgKEyG9ovlkyH1LbohWQskPBR1oWZpfL0aKjTzZ8FSKHrzomVcFb1iHtTszRd3-hjn_k0kFGTJNadyDx5qXPFpsb6LNktqfkg9FTMAEdnGK_nzDyK_rSSgCN-KtPXO30ATTkUeL9pZkuVDFJttqxfWkpZa8t7pb5bP9Fluxeqrzh5_EplCVQdgESM_Jkr9PrU-wyiTlmstnwtVLLWksSxttjIeIqQmZ8p2NpjzOA0DMPzy41YigE11y-hxBOT9YFHd3KZ7IEhGmMStojCKPi0WazdoN4SkTEazzMDK5LPSDBPinucXDd3CUER2LjHUhpHsxS5yhvoC4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
🇮🇷
🇮🇷
کری‌خوانی تراکتوری‌ها برای استقلالی‌ها با پرچم‌های قهرمانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108085" target="_blank">📅 16:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108084">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a1e614300.mp4?token=GUTjQ05U3RFM7g47MBpC1X1ViIDWNjP2-_sS6oKjI2SIxB4GtoWHa0E3tcHA0hPvDe_8NN3CueN0CLn8nyg4wGXt1-U_1CNWrTpj3RSMVwee1g89YoPdRnXNep69G_j1daAKr6cEI10rbEnDw8q6HqsWn8sU7tHsoqGJUsewHm_XAjl3o5fmzUv0jnuTPq2OmaseTBVD-OVFMAaw1xyuCpaFeIwk2V_U9paXHhL4oDclrES6jBlY7zLD_Ps70gglXWoj6wt3yYJE45WYUVCPpEhQP_MwTK_2yxOsrepFiV5XCsC9zhcTnYfAKvGgUQakshml3fJbR4-PUOj4mBnsM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a1e614300.mp4?token=GUTjQ05U3RFM7g47MBpC1X1ViIDWNjP2-_sS6oKjI2SIxB4GtoWHa0E3tcHA0hPvDe_8NN3CueN0CLn8nyg4wGXt1-U_1CNWrTpj3RSMVwee1g89YoPdRnXNep69G_j1daAKr6cEI10rbEnDw8q6HqsWn8sU7tHsoqGJUsewHm_XAjl3o5fmzUv0jnuTPq2OmaseTBVD-OVFMAaw1xyuCpaFeIwk2V_U9paXHhL4oDclrES6jBlY7zLD_Ps70gglXWoj6wt3yYJE45WYUVCPpEhQP_MwTK_2yxOsrepFiV5XCsC9zhcTnYfAKvGgUQakshml3fJbR4-PUOj4mBnsM4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
رقص و همخوانی هوادار استقلالی با آهنگ معروف تراکتوری ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108084" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108083">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ca421470.mp4?token=ryaM3ZRljslYX1hu21jwWvE62Dxj17cGLNLQTn2GXgDQ59YjPsFSCA3_KEFXCBfzcgoS5DXq7qKwgtuKiyTnWSWFCE7Jy3lf4tp18M0Sn5THreIH_4VbmTMUABgHPxsXSTsU_qlwH-u64M-MLem8NSxyVrXP5sWLb6kQ-lj6nAyrdQcOvBmVbniOdDjp3al4hdHk3LbEE8TPid0HsYvRq15ODgwmsL_8DH4c4ncbyZDMarwSBHSN7sxdWZ3kPzpi_xsrkVMmdJ8cJAo-2u4Lh1pbaP3JDdRzTucAapYewcIHT1WsTrZMTw1gTBSf1ospFCBZIohBqF9otpA8jUkAKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ca421470.mp4?token=ryaM3ZRljslYX1hu21jwWvE62Dxj17cGLNLQTn2GXgDQ59YjPsFSCA3_KEFXCBfzcgoS5DXq7qKwgtuKiyTnWSWFCE7Jy3lf4tp18M0Sn5THreIH_4VbmTMUABgHPxsXSTsU_qlwH-u64M-MLem8NSxyVrXP5sWLb6kQ-lj6nAyrdQcOvBmVbniOdDjp3al4hdHk3LbEE8TPid0HsYvRq15ODgwmsL_8DH4c4ncbyZDMarwSBHSN7sxdWZ3kPzpi_xsrkVMmdJ8cJAo-2u4Lh1pbaP3JDdRzTucAapYewcIHT1WsTrZMTw1gTBSf1ospFCBZIohBqF9otpA8jUkAKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇮🇷
اتفاق عجیب برای فرعباسی؛
خون‌دماغ شدن دروازه‌بان استقلال در حین گرم‌کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108083" target="_blank">📅 16:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108082">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
هوادار تراکتور: استقلالی‌ها و پرسپولیسی‌ها می‌ترسند به تبریز بیایند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108082" target="_blank">📅 16:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108081">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWQL_5UKDM8Onj5Yv6d6SBr4MUyjnBgEu6X93ms7htH7QREi0dSKoS94ed594lb7nqcgPTyOrOIMDvf_4104-Fvb99mrffKjZXHx4_o0iyYa6bXOFYdldlOYGdkZEPS7RuoM8b2JGeo8wlIeQ2sVoGLOP6vtgrSkbn2cUS_i2HOqicLepyE6YeCV3f4EyIPXH7-tq-t6G48GqLE9d2OFKwQ7iylwfNzV-J_BkDnJocr3Km1LoI_oRkoviq-z-HOnq3CkDAEZB1GuJ1zbPC06kb02evui9IIhveF2SLBDQc5HyjBsGarq0KqCNGQ1Z7CigLeHXiR2ZXCfg111-HdbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/108081" target="_blank">📅 16:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108080">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a925bd26b4.mp4?token=RExHxw3oxdI0xL-DUmrFb0Vk_1TVtlQlPrNaLtV7eUDRWMaJ2Z1CF3XJ02kmk-CDior5M4FL7tUsPUnXhsJBgMzC_kprFPEC55glUMOcdrkbn6PvRg8teBfGvabZSlt1fuFm8PWMExCsVoBykv3KhH0sOUMNv9MHapFgPQl0aYxm0qZnpjTg3RXeUjpeht5ZZ9s0uFCKV9mcZbEUDhsK99Vc2_bKOptzvC4sGTkqSK1CTWbfJq5AHTbNgTylaa3IzpPwsC6_olmb08QuwmtUe-TqfGt6_ELh5hxdTZl0KdnRyYjLPG-sI1mbco3tSJmWO7JaQ3szuIcXJYF98Zz12Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a925bd26b4.mp4?token=RExHxw3oxdI0xL-DUmrFb0Vk_1TVtlQlPrNaLtV7eUDRWMaJ2Z1CF3XJ02kmk-CDior5M4FL7tUsPUnXhsJBgMzC_kprFPEC55glUMOcdrkbn6PvRg8teBfGvabZSlt1fuFm8PWMExCsVoBykv3KhH0sOUMNv9MHapFgPQl0aYxm0qZnpjTg3RXeUjpeht5ZZ9s0uFCKV9mcZbEUDhsK99Vc2_bKOptzvC4sGTkqSK1CTWbfJq5AHTbNgTylaa3IzpPwsC6_olmb08QuwmtUe-TqfGt6_ELh5hxdTZl0KdnRyYjLPG-sI1mbco3tSJmWO7JaQ3szuIcXJYF98Zz12Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
مشکل جدی قیاسی در تلفظ رولز رویس
گلزار: چقد فخر فروشی به مردم ندارم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108080" target="_blank">📅 16:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108079">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE3_34Q67IHwKF7qpDcfAEMFcUfsr1e6O5A5nkHcUiW9nmD8goM1yMy-EKSB5n_wh16nohQgt8HSCbvPao-ucBgzjWjCZx3uwZ5bv-OhOfuBLNi43-wnDbsqWIEofDqAuwhiUqsNBsCg3Zpgu_ieu7jSLmPzDFQUDzNZkpXCpo92g7vr2GK4zG6EBy2G-nDCT4mwS-lE1byfgGWK72E6vP3WmNLqdFWQG3zUrTaw8uImoHmjqxl00ePOHtSyIT1AtZBhYdWqVvGufHEcbCioFxZt6MBuGuFO8hnKP_mC4FT68hFqUTqZ95rigNLfW0JFTMNzRDW9MvDYuZsbx3rLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب استقلال در مصاف مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108079" target="_blank">📅 16:01 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRJr8LEavij7XzhlnlU4bCppkLqkW3zBLA3cJ29qUkU-THxFyNZZbd8e2xQEJTmY3Xs3J3fXojyiQTIA2TLmK4pO3Gky5IprZHT4ML4X-KSAEvrLLjIf9PUqD7d3O8ANAQpUjwLOwho4RJWRVizPJsr8xd0Fr2aop-L6PHL5OTCWx3rtYaU189eq6ud2PSA7KQsu2HZCqaZvR760LkWfizY1esFaX9OLoP_N-qoVX27ti4Mjxk3WSP6bFVV1H9QM1Qwj07lk5TDbmcyt1MSJFyTkrOT68jmF5Oa7BJSKIUXdEGAK7ER6fzh4wmHYcTLSVZ3AbaZCPFbvIpgkNXWEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب استقلال در مصاف مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/108078" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ea53f.mp4?token=MJoynWZ7pB8KlPLdB7LZnlCs-lqodoQrN7bOKVPZEcPqwmS6ZZ_znM_aMwh9M_DRM184C0tM06c8Qg0KlBZs43m1MEAF-pPdcPJaYj81Khzotr-_pU-_Rb422uMZJ_F4etY2kldoFv7T_NX-xwfDjDhYfBkVLHctDr5m0dPUc8pYgeP9tExm_ZdqzNLNlRNpRXaVbinWDlpr1UVH8MlBDtZc-h1zCHp8YMf8ApCNgXqWda2spkHvRdV_LeqqBA0xbYQkbX75wkgJDXJfvNSOdWxrJ485w2likJgbcBLs8CfsOgNQYnMTosYzdbPol0xE3xnuY4Re_W04DRFYfI9jpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ea53f.mp4?token=MJoynWZ7pB8KlPLdB7LZnlCs-lqodoQrN7bOKVPZEcPqwmS6ZZ_znM_aMwh9M_DRM184C0tM06c8Qg0KlBZs43m1MEAF-pPdcPJaYj81Khzotr-_pU-_Rb422uMZJ_F4etY2kldoFv7T_NX-xwfDjDhYfBkVLHctDr5m0dPUc8pYgeP9tExm_ZdqzNLNlRNpRXaVbinWDlpr1UVH8MlBDtZc-h1zCHp8YMf8ApCNgXqWda2spkHvRdV_LeqqBA0xbYQkbX75wkgJDXJfvNSOdWxrJ485w2likJgbcBLs8CfsOgNQYnMTosYzdbPol0xE3xnuY4Re_W04DRFYfI9jpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
❤️
هوادار تراکتور: بعضی تیم هایی که در لیگ نخبگان نیستند، از تلویزیون بازی تراکتور را در آسیا تماشا می‌ کنند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/108077" target="_blank">📅 15:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sDY62hnTJ-kblXmgSb5T4xIfFja_1FArjcyP1Yaqoewq-U4NXfjFciMHiYgk4LssNk2zehgkJTljoQ3TWysLils9aLE11oGJWfQmB84OPSiK8kcYgIjNZjC7RxjMWf73t2s1zRq7zA0Z3P3LTm90oHiLOpSoqojYlV1OnhF5xCyD-W0kpUX06YE8A2-mtp0TgXPpbRsTrkC9SfOqhzSWEuGZiMpxGZN_NNcoVNlZAqryFcbzg2ZzkdG1crzd0cPrttWyHQy49v_wxMObSHc4e9bDZN_oAOZGQKMkD7cagyEYnH4UtQS0apw1-RSXWmt7tDIIxzpIjot0MVb4GGDRfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب تراکتور مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108076" target="_blank">📅 15:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ec3521bc4.mp4?token=DB7Y0QpEgFJCqhDVnPYKMyEARpf929gJDYauRFMkNUpl1UF34rkgPtFniPmOn10wSv8auf5Fr80hwPcsnqU798migpwLs3kM7qw04rSCdCFPpF0MNhYrOPxzcpWvISJbGfi0TDiaqgNHbKTdCXjENDogUrbSd1oBlf9xW62FXRAKekr9Xhr2MhFTeA7rmMroBT1WN3DBtAXp-fl-dz25XA7ZhWDIF1Djik4rFb8fWGYoBiqe8UiXobF6s3fC0gyOLd2Pjw6M32szI4gyzDKTIWZ5ysDJCfWKnkvFFpxtvaWDyclT-pQSUCWQGXVvdaO6rbheRJ4QMf-dLZfjfnlchWUrkOqPKtZDFLK0VW9JFQuStdtSxCx6zoZ425flSHYXmDradauO9i6eHOP1M9WPSUshMYVEhE1pIZmaUPPkBkK490uJUmA5HCKOO2jj0uapyoIof0dtFmkb39CVbktuIiDgR-HPlYEQyqWCDYsxKQqQ8Gxz3B_tffcR5jVHXgObbC8vCzIBaCpV66gnfa8cdPUYUvwdc_ksfmocyrF66e9or-6rEyopLQG0aA1MeSmf9rABMsgDhotEtdTMP_3-cBWth6SZvfxJV0X_hwvvUN0Op-DQLpedCBJobKtTpbDek40mykBuTzRvLbmd_Tog1_GbXibdIf-k-5Ak9oEs9e4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ec3521bc4.mp4?token=DB7Y0QpEgFJCqhDVnPYKMyEARpf929gJDYauRFMkNUpl1UF34rkgPtFniPmOn10wSv8auf5Fr80hwPcsnqU798migpwLs3kM7qw04rSCdCFPpF0MNhYrOPxzcpWvISJbGfi0TDiaqgNHbKTdCXjENDogUrbSd1oBlf9xW62FXRAKekr9Xhr2MhFTeA7rmMroBT1WN3DBtAXp-fl-dz25XA7ZhWDIF1Djik4rFb8fWGYoBiqe8UiXobF6s3fC0gyOLd2Pjw6M32szI4gyzDKTIWZ5ysDJCfWKnkvFFpxtvaWDyclT-pQSUCWQGXVvdaO6rbheRJ4QMf-dLZfjfnlchWUrkOqPKtZDFLK0VW9JFQuStdtSxCx6zoZ425flSHYXmDradauO9i6eHOP1M9WPSUshMYVEhE1pIZmaUPPkBkK490uJUmA5HCKOO2jj0uapyoIof0dtFmkb39CVbktuIiDgR-HPlYEQyqWCDYsxKQqQ8Gxz3B_tffcR5jVHXgObbC8vCzIBaCpV66gnfa8cdPUYUvwdc_ksfmocyrF66e9or-6rEyopLQG0aA1MeSmf9rABMsgDhotEtdTMP_3-cBWth6SZvfxJV0X_hwvvUN0Op-DQLpedCBJobKtTpbDek40mykBuTzRvLbmd_Tog1_GbXibdIf-k-5Ak9oEs9e4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
کنایه‌های ژوله به سرماخوردگی عجیب رحمان‌رضایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/108075" target="_blank">📅 15:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/322ce18fa5.mp4?token=KlHp9Syrnqmr6fTVsp6wlVvjK8DdGoPL-930b6Qg-8AaH3GsiiTxtmeLGZfYFkp-7qEeI5y22XZBJmGkpGki84sw1oKdepm6A71It00QLohl4NashNq1CeHUyHwWU5xbkUu3BbRpcd0bdghqP2pD2iPNnz74WbkV-FHveDFfYy4d52pJIbyNiYqBSwjaS94_hqZ66TTsRRkJpgD6-6rxnMCU3V21OXUmPobTjwu9zwjW2DXbRbP3GDTgm1GRrDV-vaYc1IwmvPHIrn5eus5uwEVH3BM_oySSBNrO4Dcq_P1LyIv2AtkcfnPo01qFTKQ13tnKGnMJ6NJG7E4IzBZE1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/322ce18fa5.mp4?token=KlHp9Syrnqmr6fTVsp6wlVvjK8DdGoPL-930b6Qg-8AaH3GsiiTxtmeLGZfYFkp-7qEeI5y22XZBJmGkpGki84sw1oKdepm6A71It00QLohl4NashNq1CeHUyHwWU5xbkUu3BbRpcd0bdghqP2pD2iPNnz74WbkV-FHveDFfYy4d52pJIbyNiYqBSwjaS94_hqZ66TTsRRkJpgD6-6rxnMCU3V21OXUmPobTjwu9zwjW2DXbRbP3GDTgm1GRrDV-vaYc1IwmvPHIrn5eus5uwEVH3BM_oySSBNrO4Dcq_P1LyIv2AtkcfnPo01qFTKQ13tnKGnMJ6NJG7E4IzBZE1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
👤
هوادار تراکتور: عادل فردوسی پور دشمن خونی ماست و همیشه تیم‌مان را تحقیر می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108074" target="_blank">📅 15:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28665d2567.mp4?token=G7r1JjyopvsJFOv0DjzlN2cOxKzs59TKMCE87l4Q2YEWw_zxap6_7w4MaNZ_RtEHOnE9ICWNYDBpwsemlB1R83EpvKxtH-XjW13FT_I3Hp8AGMvy9DW5LM09GD9kuVRoFp_z8DKVq8ahukPX3NpvbVgpA5FggKrBd9YoGug8KMHvSGpx-TNAtYk48b27m8VDbglrVC3PJiBtY3ZpmG-rDncA_X6IiAnSfUKlGY2dM4WOqbZLnHARe5oqd7VLjBoSMfC7CTRq5ZXQoxtklSLxllxBmIfOaF-s94LpLElJSggdXTf1PGZY1LE-tZBFUbEap2vyzKoRfUR56pfHXPC_SGSOeX8uEW7LSAcOUHsdShEDAsJVKvO2fBw78H6-ntveT4I5u7iYAJRM19ClWv3dXlPpoH7Bl1tlicpRXCmUn8GKjHX9WSXI463Y6TNenHdUnXm-JyYhd2jUdCtqfSFXNKo77iirMCo-Ea_rJ9bQo7tO4EJg2ajT-2c3SMg-RAvqu3cHiefWMFG5AKYeY2KKR6KAX3KixxCXcx1GHAeYaSwWkP9BYKXdhAQzzYh6jSDSWP5Pqpi0ZmNJFOqhPeJsvEGAb9-2M-azAGFaGCGatlY6T0WXbkNprjPsS0UfzrKpXQ2Qf6POokuyIOv711lyE0Eu4pTK8psr5FAAhFM_vGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28665d2567.mp4?token=G7r1JjyopvsJFOv0DjzlN2cOxKzs59TKMCE87l4Q2YEWw_zxap6_7w4MaNZ_RtEHOnE9ICWNYDBpwsemlB1R83EpvKxtH-XjW13FT_I3Hp8AGMvy9DW5LM09GD9kuVRoFp_z8DKVq8ahukPX3NpvbVgpA5FggKrBd9YoGug8KMHvSGpx-TNAtYk48b27m8VDbglrVC3PJiBtY3ZpmG-rDncA_X6IiAnSfUKlGY2dM4WOqbZLnHARe5oqd7VLjBoSMfC7CTRq5ZXQoxtklSLxllxBmIfOaF-s94LpLElJSggdXTf1PGZY1LE-tZBFUbEap2vyzKoRfUR56pfHXPC_SGSOeX8uEW7LSAcOUHsdShEDAsJVKvO2fBw78H6-ntveT4I5u7iYAJRM19ClWv3dXlPpoH7Bl1tlicpRXCmUn8GKjHX9WSXI463Y6TNenHdUnXm-JyYhd2jUdCtqfSFXNKo77iirMCo-Ea_rJ9bQo7tO4EJg2ajT-2c3SMg-RAvqu3cHiefWMFG5AKYeY2KKR6KAX3KixxCXcx1GHAeYaSwWkP9BYKXdhAQzzYh6jSDSWP5Pqpi0ZmNJFOqhPeJsvEGAb9-2M-azAGFaGCGatlY6T0WXbkNprjPsS0UfzrKpXQ2Qf6POokuyIOv711lyE0Eu4pTK8psr5FAAhFM_vGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🔴
مهدی تارتار، سرمربی پرسپولیس:
جام حذفی را می توانیم بدون ملی پوشان برگزار کنیم به جایش از جوان ها استفاده کنیم. مگر یک بار قشقایی پرسپولیس را حذف نکرد؟ چه اشکالی دارد که جام‌حذفی برگزار شود؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/108073" target="_blank">📅 15:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
#اختصاصی_فوتبال‌180 #فوری
❌
مدیران پرسپولیس صبح امروز با حجت‌ کریمی مدیرعامل تراکتور تماس گرفته و اعلام داشته‌اند که اگر در بازی امروز مقابل استقلال موفق به برتری نشدند، می‌توانند با همکاری و تعامل با استناد به این نامه(صحت یا عدم صحت آن مورد تأیید رسانه‌ما…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/108072" target="_blank">📅 14:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78b4e1c6b0.mp4?token=vRfvsa1oWf244IAFjMONZT59VGGPLt_sTXipOMIAMvXhVym1W1EHmgohrKDpL6aHyP4bmYQinLtAP3V9BoyXK3Px-8mE-NPHqxZOmdgIU2R5WE9AMgMma4d84FkQ1ZGI6nz8rEwaGrSuzkC4lpVelRL2ESGhrPEXOLYZq9cnjIoVTsv7f2KNV8qGHRTv-wGI1PAXZ4106yXSTAFdHWwvnDMLGMe_8OgdaWhRMC-OLdpU1Grtbe785pgRCDPJTY2QRjBwf9cDfguCVI63AVgzrN-7egt_VqsnhIcQbkl_GaEuVQ3Sp0X90M3GjwEZkkZfYjuWemEK69ei_593TDztnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78b4e1c6b0.mp4?token=vRfvsa1oWf244IAFjMONZT59VGGPLt_sTXipOMIAMvXhVym1W1EHmgohrKDpL6aHyP4bmYQinLtAP3V9BoyXK3Px-8mE-NPHqxZOmdgIU2R5WE9AMgMma4d84FkQ1ZGI6nz8rEwaGrSuzkC4lpVelRL2ESGhrPEXOLYZq9cnjIoVTsv7f2KNV8qGHRTv-wGI1PAXZ4106yXSTAFdHWwvnDMLGMe_8OgdaWhRMC-OLdpU1Grtbe785pgRCDPJTY2QRjBwf9cDfguCVI63AVgzrN-7egt_VqsnhIcQbkl_GaEuVQ3Sp0X90M3GjwEZkkZfYjuWemEK69ei_593TDztnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
🇮🇷
هوادار تراکتور: استقلال و پرسپولیس در تبریز کلا ۱۰ نفر هوادار دارند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108071" target="_blank">📅 14:56 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd3638bac.mp4?token=ojvXC7SD1JoQOePB6FllJZzmg7TJmES9BCIWYDa9tXAus-6Hc8Blv7kHdH46SvvrhNx2XmTgKqBx6c_Ow2gfgA-hfMvHkmaps7CD7es1HDB7OU29AcZEcyx37DQ4ob8nNBQ2aft4dEUW0olMjgCgym_wpV8ENJ3LpC6vGcfgmdwJMjSh7GoQPWevS4mg8HLKJ5xUHW7rH0dN-E-F-V7nMMkTAOELIoYK2HwiZRHACF_zALfXzR-Jr-XjtU08R4WwfWYBZzSakL0hRD9yIABaHrDJ9D1JbtO99IpFzVF0K3K2ugmJAv8QRR8PLYSnVi_GpyedyNQ5WjlsnVVOM-pzzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd3638bac.mp4?token=ojvXC7SD1JoQOePB6FllJZzmg7TJmES9BCIWYDa9tXAus-6Hc8Blv7kHdH46SvvrhNx2XmTgKqBx6c_Ow2gfgA-hfMvHkmaps7CD7es1HDB7OU29AcZEcyx37DQ4ob8nNBQ2aft4dEUW0olMjgCgym_wpV8ENJ3LpC6vGcfgmdwJMjSh7GoQPWevS4mg8HLKJ5xUHW7rH0dN-E-F-V7nMMkTAOELIoYK2HwiZRHACF_zALfXzR-Jr-XjtU08R4WwfWYBZzSakL0hRD9yIABaHrDJ9D1JbtO99IpFzVF0K3K2ugmJAv8QRR8PLYSnVi_GpyedyNQ5WjlsnVVOM-pzzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
❌
🇮🇷
🇮🇷
هوادار تراکتور تبریز: ما مثل استقلال تهران گدایی جام نمی‌کنیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/108070" target="_blank">📅 14:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ایجنت یاسر‌آسانی: اسناد منتشر شده در دقایق‌اخیر که با ادعای مدارک فسخ آسانی با استقلال است، کاملا فیک و ساخته هوش‌مصنوعی است و اعتباری برای هیچ نهاد حقوقی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/108069" target="_blank">📅 14:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHQOoZLnWGu0CKPfniNwlN_ksKR5p55OKz2lm01awt_ReSMaJH7xDPhd2GR-Sguua9h33jNNTJdA73Qr7NYgaCU2JOTg23PRDfxo8H5ANA_GgbV0wbgU4bgSI00h5ugH_pW3PKlfIoInvRHcI6m3mzgT7tnfO4xGLyz5J6XnaEWo0Rq5_6v_rvNc0ahP5gxYPZqqVmD_L1xECTNV6lpB8Kh-Bz8RxtTuMMSd_bD8_ueQ9Qwl65nhkdLhpwMLfMcd29a7Kt9u06QS9u2m8cRo_YozBwdgE-T2h9-CssFq_wCPB4HhCXq9f3AMGs02ujBWJFVJ5BiI51gEZFxMkkioxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
ایجنت یاسر‌آسانی: اسناد منتشر شده در دقایق‌اخیر که با ادعای مدارک فسخ آسانی با استقلال است، کاملا فیک و ساخته هوش‌مصنوعی است و اعتباری برای هیچ نهاد حقوقی ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/108068" target="_blank">📅 14:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMzsnA1hNaia06Kkf9fEduGLbfPTcnpTZ7Up8dpv6bQ9b6wIGWgSRL5YEtDG2iMu_7KGwM0xYvYmWWJeMRmshttLr4ka4auQLn396E0oXkNpd2_8Qp1IYenHBdxjqL_aDsaSmwh-_LxLp_KQPLL_9NsdJ6EBGbhoythANb9o0b0GYm6hf5PVe7zKQXjQxFtJYDt6sRiGEYdqrHA4W85Gzo_zBvCSRdKJron-HByanTEvsxXM6VGhmuZL5kvSOwIj9DDJ6sjDnKCT8kWwjaR75tsyePFDZ0hDcDNsi1yZl2h8U4LsBuFmVH70HmRby25uwGZueCYFGhbGGfttFCGDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
‼️
روزنامه‌SER: در روزهای اخیر درگیری میان چند بازیکن در رختکن رئال‌مادرید شکل گرفته و مورینیو کنترل رختکن را مشابه فصل قبل و دوران آربلوآ از دست داده است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/108067" target="_blank">📅 14:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">💥
🔥
خانم دوناجان وایلد، در سن 61 سالگی، رکورد جهانی طولانی‌ترین مدت نگه‌داشتن حالت پلانک (تمرین شکم) را برای زنان با ثبت زمانی 5 ساعت، به نام خود ثبت کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/108066" target="_blank">📅 14:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a13616851.mp4?token=EBtCQlcvwSPuVBYwo0gSXs97QXevWBs8G4t7OON7P5FvG-D5nz3SDoL05ZT7rpo4eVPu0biaQdE0z6ksTV75NMq132F8bUAt2KqykLROv9ZaYLw5HzXkMYR314qrB2xC_X6htTnM9p9wx_EGkx0roTJDs4tpFZMsv3Tr-zn0HrBE8lEVwYVivTmoL8ZUIqemnEHnphblQ2RykGeemcGW8psz_7tKPz_AZyuSoUBN6ZTwuRdrlU6xo4_WOTfAWb3En8LL2G8Tudg-VfymHLUh5BammSU5lkwVdaE8or7TBoR7aTuBx6sLW581kQgPxeZrBRBDUukYjMlxU3qOtQ19OQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a13616851.mp4?token=EBtCQlcvwSPuVBYwo0gSXs97QXevWBs8G4t7OON7P5FvG-D5nz3SDoL05ZT7rpo4eVPu0biaQdE0z6ksTV75NMq132F8bUAt2KqykLROv9ZaYLw5HzXkMYR314qrB2xC_X6htTnM9p9wx_EGkx0roTJDs4tpFZMsv3Tr-zn0HrBE8lEVwYVivTmoL8ZUIqemnEHnphblQ2RykGeemcGW8psz_7tKPz_AZyuSoUBN6ZTwuRdrlU6xo4_WOTfAWb3En8LL2G8Tudg-VfymHLUh5BammSU5lkwVdaE8or7TBoR7aTuBx6sLW581kQgPxeZrBRBDUukYjMlxU3qOtQ19OQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
خلاصه حواستون باشه موقع خرید آیفون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/108065" target="_blank">📅 14:04 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-QaM5XZN-3ER6I4y1F3MI__reVWf5h9kbH8o2JqL0Kqh-k_EP5hhW04CIZ04zV2tHQwPdfcaIc-jDpSiBvH0XVMxFANE7BAx90BQOIJ2X6Vjh_jPU_yRbLDd9kJ9CAWA5CZ2okYnQhJDBnYwpYISKlYFQRBSyzqOCWt5P9P_kj0CpTYu1-9IcSbWLUCycSiI0ZOoshqw3IbCpgs03S3Y1Jgt-1jT-s84gJB8E2FHzsLmSawF-wllTxWKYv0Rt5gwtOvh-16XJlDaEtRhYVaAy9yCvsRP9zkvXYlV8CiyLr-1rA83RihxQEdSHEhzfCW0gvM3XUtKf8sfxAO8UpdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رافینیا در فاصله دو روز تا بازی ختافه در تمرینات امروز تیم بارسلونا غایب بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/108064" target="_blank">📅 13:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108063">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a9ae65408.mp4?token=J48WuV4NB6hc3j5m6HKSc622ZdyIMhDOrOfm7oHuruIgNMkn2MgfKq1SST0eItjctzcjXKbwRwH9s9u7HaE7OQTS9VYOM1gDNGHRN0aRSLrd9PImI9Taj9ODOkTXX-SXRS2PEo3giPCFoTLsfzsBvGtW-XyWqvymn4oNXahqXSmDdnegO4I3qtO_HxENyAw2DdCk8AX6-MlHnHrgTvv2_KDJtkkzn2-BQd_c6E5Ef_6J8fAdo5e3tfg4e20Pz9-0yX1C-CQBdhS1xZVV__Qdk2qfYYm3PVx4aTjsgEsRbfmj-wCyOZT7hn8UPQk5tD6dwxrp6TuW42xw4Wyo-TJQxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a9ae65408.mp4?token=J48WuV4NB6hc3j5m6HKSc622ZdyIMhDOrOfm7oHuruIgNMkn2MgfKq1SST0eItjctzcjXKbwRwH9s9u7HaE7OQTS9VYOM1gDNGHRN0aRSLrd9PImI9Taj9ODOkTXX-SXRS2PEo3giPCFoTLsfzsBvGtW-XyWqvymn4oNXahqXSmDdnegO4I3qtO_HxENyAw2DdCk8AX6-MlHnHrgTvv2_KDJtkkzn2-BQd_c6E5Ef_6J8fAdo5e3tfg4e20Pz9-0yX1C-CQBdhS1xZVV__Qdk2qfYYm3PVx4aTjsgEsRbfmj-wCyOZT7hn8UPQk5tD6dwxrp6TuW42xw4Wyo-TJQxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
تئوری کشته شدن وینیسیوس صحت داره؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/108063" target="_blank">📅 13:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108062">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4T7I7MXgPsg_99BVsMsNZywulfAY16dj5VROf04XhfbSIz855TYPKcGxMn7xe3M4xv0Mis26bTma_mLgPv4nthCiZiq5PAVKqcxu9H12kxaznvopBR-hYOEMX4XtQ5KmCycgITCS07pQUsa7k5IWsh6_wIPmQomO-LnJMfH-GAOluJTZvwfRdsMQrP64AzKMftEooshqmzPkGDJGboh-3cFaB4NMUxhhGz2rbHwW9wHi3Outb379exxaFlurMC-5X3sjY8-dbvXciG6VF9PkFp_wol_bn5HK1n09pU-IY7HQ_3doHJi8t6KqE6_uyzWcdWO2AwIKdtcQ3TMN_T3eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتیجه بازی بعدی رو می‌دونی؟
👀
تو
آی‌اسپورت
بازی رو ببین، پیش‌بینی کن، امتیاز بگیر و برای جایزه رقابت کن!
🎁
🔥
👇
همین حالا پیش‌بینی کن
همین حالا پیش بینی کن</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108062" target="_blank">📅 13:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108060">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBLSddeCMlFepxU9Ybq36XepqFkqPnh-gnrT10-xdRVq5y0LQxmcIkXPI50IUPXdSEFdlLIVxuX1i02hjIikmZelgfvB2doBSGu8fBF7RI8D8RJqSrOitTrtMy9n9OSrwjZX3PJrWf1meVkYvA1Ufaxs_acaXw0Q0jdoACBmzFbZV4zXUXSZZlKhGhH0qQL8sQVuq-4NPtD1YPfttQDzjr7G2g03fRFEJUpaVUMnu244_JKyCeLrHzQkzqW9TWqsironAcIshgqYZiAlbxXUwEEb1LnkbChQZXHTF5-HQWbcrovYjcaGoO095rxcS_m0XUCiLxGZybfxBXn1uIYepA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا در مسیر جاودانگی، از برزیل تا کرواسی
؛ لاروخا رکورد باورنکردنی ۴۲ بازی متوالی بدون شکست را به ثبت رسانده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/108060" target="_blank">📅 13:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108059">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1507fa12f.mp4?token=O10CyoShyIKBh-uTDmdNrYyq67ZFU7lKNpgLobugGA6ZZP0v3X3gbYXgnN_q7Q7MueKBB29OEcUbygWGZFr426t3scWBXcGIu7FZX1nKJXhNkoH1V2JRoahb1967jVKy6v3xU50fTRFHIPDMXUQi01Gr-r8vI-zbc8PkSO6duSw9tuuscm3OLLTzdRsuScWoNFpdE3exgVdHV0UX3f5sjbVEqcGdrqDtDhDI-A7WHrkrchng1XsNIF9a5baQdXpD5rfg69kVOMA4rjqSIXrLpgunXHyR3RT3BHZfCP6-a3rmztwbGXhfZQAipXaYu6lR9sbdI9tzFeGNvQ5GM2rnSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1507fa12f.mp4?token=O10CyoShyIKBh-uTDmdNrYyq67ZFU7lKNpgLobugGA6ZZP0v3X3gbYXgnN_q7Q7MueKBB29OEcUbygWGZFr426t3scWBXcGIu7FZX1nKJXhNkoH1V2JRoahb1967jVKy6v3xU50fTRFHIPDMXUQi01Gr-r8vI-zbc8PkSO6duSw9tuuscm3OLLTzdRsuScWoNFpdE3exgVdHV0UX3f5sjbVEqcGdrqDtDhDI-A7WHrkrchng1XsNIF9a5baQdXpD5rfg69kVOMA4rjqSIXrLpgunXHyR3RT3BHZfCP6-a3rmztwbGXhfZQAipXaYu6lR9sbdI9tzFeGNvQ5GM2rnSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
محرم نویدکیا سرمربی سپاهان: هواداران و شرایط اقتصادی را درک می‌کنم و این که من به عنوان سرمربی از آن‌ها بخواهم با این قیمت دلار و گرانی به ورزشگاه‌ها بیایند خیلی جالب نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/108059" target="_blank">📅 12:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108058">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e684a43eea.mp4?token=QzDAGnxvsfVEEplS36E0FOfaSB9TBdv--tsTDN6wq8IM6z5UYfd3hLeyb1QBt5G7uzof0xHh38MoHk7xBxbOfAoCuGiCbDYMWUzjirS0R1gfhkcSio3VaP-Z2P2t-Hy2ogsISeRdLjA6LOxRq_jB3rFFDE8ejdUy14BWZkxKS3JZkoXYGcxcdqgyLUMmK0i6Eaxn5Jghf6cYENc3BhL8RX3pmY1tR4bNLdqNwaMErtrkNki26R9pV6f_v7u7X3Ynsz75FgVkw5ljWQebN-jiUqECUS2ulh8PF63cOJ9_9khz-SMknFdt_Jqw4kA95taLQrbKrbK3Qhe07YP-Pc-UmF1vJImFyx2UpR29MccclgNUst9-KaJt6Msry6QvvFgZg7Ldh_X7liqxkkrj6SAJRKQOoHaKTeDPxLZdgook2o_DPpQ4gRCn3VgJTR1FD1qZ_yCf3SZmyJA1t7GRWXwBtifHter1p-uqOd5vLybwwksZTX9y0jkqhLUK9c19ftve3z8k-xS3mt4gSyaYIWP2bmNbccWIDz3R1gD28P6Q1qN1mQmJAKhvv1V71hK1x05JKe3XMvAtVG7MsCo7GjN5f6_4K7fL26iaRZvndhOcwebeFors70BcE7cVxjRWB5AqCT_A65osG__c6VL9Y7VC9a6duWdaVeo4Ud7Hz8u7FAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e684a43eea.mp4?token=QzDAGnxvsfVEEplS36E0FOfaSB9TBdv--tsTDN6wq8IM6z5UYfd3hLeyb1QBt5G7uzof0xHh38MoHk7xBxbOfAoCuGiCbDYMWUzjirS0R1gfhkcSio3VaP-Z2P2t-Hy2ogsISeRdLjA6LOxRq_jB3rFFDE8ejdUy14BWZkxKS3JZkoXYGcxcdqgyLUMmK0i6Eaxn5Jghf6cYENc3BhL8RX3pmY1tR4bNLdqNwaMErtrkNki26R9pV6f_v7u7X3Ynsz75FgVkw5ljWQebN-jiUqECUS2ulh8PF63cOJ9_9khz-SMknFdt_Jqw4kA95taLQrbKrbK3Qhe07YP-Pc-UmF1vJImFyx2UpR29MccclgNUst9-KaJt6Msry6QvvFgZg7Ldh_X7liqxkkrj6SAJRKQOoHaKTeDPxLZdgook2o_DPpQ4gRCn3VgJTR1FD1qZ_yCf3SZmyJA1t7GRWXwBtifHter1p-uqOd5vLybwwksZTX9y0jkqhLUK9c19ftve3z8k-xS3mt4gSyaYIWP2bmNbccWIDz3R1gD28P6Q1qN1mQmJAKhvv1V71hK1x05JKe3XMvAtVG7MsCo7GjN5f6_4K7fL26iaRZvndhOcwebeFors70BcE7cVxjRWB5AqCT_A65osG__c6VL9Y7VC9a6duWdaVeo4Ud7Hz8u7FAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫣
نورافشانی فوق‌العاده ورزشگاه مونومنتال آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/108058" target="_blank">📅 12:20 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108057">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c30835c72.mp4?token=HEMAtKYVy_Mcgx6F6BpDKLbPlCm4adTVrnN3dzmjFe1IxtZTLKpMz5z9-mBxlhT_U8DtYLkDD4tKQPyM7sdmmxO8Z4RsaVJIPTH6mi642sgagrx279XruiM8XNpF1A-qpL2oj38kxmjqpUcU4kx0xfwpNkxaJ_SbKzHWZf-OYOjhymUbDkFYNNhiKbafMIDgZBvZ4j6k7e2ZeXv2uYn7qJrN7kWJGVuTtK4qiS6DJ5T3VIuzI0Zm6VZPdmgpx-e8gg5Uf-6AqSfjod7hiW8B7_yBOfyyoaBO3BTLizrs2EwUONHjHyFs7AYYiS9W0W2OkG-aQlPk77lbpz03XRu0xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c30835c72.mp4?token=HEMAtKYVy_Mcgx6F6BpDKLbPlCm4adTVrnN3dzmjFe1IxtZTLKpMz5z9-mBxlhT_U8DtYLkDD4tKQPyM7sdmmxO8Z4RsaVJIPTH6mi642sgagrx279XruiM8XNpF1A-qpL2oj38kxmjqpUcU4kx0xfwpNkxaJ_SbKzHWZf-OYOjhymUbDkFYNNhiKbafMIDgZBvZ4j6k7e2ZeXv2uYn7qJrN7kWJGVuTtK4qiS6DJ5T3VIuzI0Zm6VZPdmgpx-e8gg5Uf-6AqSfjod7hiW8B7_yBOfyyoaBO3BTLizrs2EwUONHjHyFs7AYYiS9W0W2OkG-aQlPk77lbpz03XRu0xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐐
🔥
🔥
پایان یک افسانه ...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/108057" target="_blank">📅 11:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6399207329.mp4?token=gRbeTdSsFWjymIR6SS9AS5iJVcp7U5GbX26qr13X6gkWq2uGu0BtQc5IvW2ZjhKRaP1Q9YUO7ipBPvgwWyT-HrkoJvaDWds4B-Eu9bQNvBllKq4hulcwyUGoy2jumQYm4BvTHq-gyLzeNeJhqdJ3FF7jxvLM9LFZmwpkPX9VdUekqt0r38i496pGSWkwRvy2WRBKCKejXQHcWTIijIxU9_EyTWys2ePnDvPJgKCHKRDuWn2OLQOhjr0_5RZTIKc-iynNsIbEVyAiGUx2vSTqFvoexAipqe7iQfwmMCqE_nxoo9LoWMjc8Haxziw_wJqRCIHkbDWPxnUis2sQTfOQSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6399207329.mp4?token=gRbeTdSsFWjymIR6SS9AS5iJVcp7U5GbX26qr13X6gkWq2uGu0BtQc5IvW2ZjhKRaP1Q9YUO7ipBPvgwWyT-HrkoJvaDWds4B-Eu9bQNvBllKq4hulcwyUGoy2jumQYm4BvTHq-gyLzeNeJhqdJ3FF7jxvLM9LFZmwpkPX9VdUekqt0r38i496pGSWkwRvy2WRBKCKejXQHcWTIijIxU9_EyTWys2ePnDvPJgKCHKRDuWn2OLQOhjr0_5RZTIKc-iynNsIbEVyAiGUx2vSTqFvoexAipqe7iQfwmMCqE_nxoo9LoWMjc8Haxziw_wJqRCIHkbDWPxnUis2sQTfOQSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
زیدان محبوب‌ترین فرد در فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108056" target="_blank">📅 11:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e37d8d2b4.mp4?token=PFnbRwig7Bv8Zn24baKCxqzdcwc-QPlsWgBiDaevsq_7BwaH6Vioi4Tfpfs_mEZSzMN3yDVYPon7-IPksDqwJ3f5vR5oH7Oh-mK73D5UUA11wlS6mSWFKTCU4ZsvqKrbJZVTfwGDyrcfD5WJ1zNlXzr9s-RcQzDiM4ftsrimvYSqFdqVdRvQZdw1xPFFxS3HQeLHk0-Ys6_B87dvtQc0TjtNcSNpaGu7ni0VB4E7ggX5JK6ax7yYKjLKHys_iK-dYY_42V6C4jHA4zNB1ZGSOeN_S_HRcEiVPPlw7aERZNZVlXUj3BnHklyAFdR461ts88pX-wOAenY4QnDBjSN-QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e37d8d2b4.mp4?token=PFnbRwig7Bv8Zn24baKCxqzdcwc-QPlsWgBiDaevsq_7BwaH6Vioi4Tfpfs_mEZSzMN3yDVYPon7-IPksDqwJ3f5vR5oH7Oh-mK73D5UUA11wlS6mSWFKTCU4ZsvqKrbJZVTfwGDyrcfD5WJ1zNlXzr9s-RcQzDiM4ftsrimvYSqFdqVdRvQZdw1xPFFxS3HQeLHk0-Ys6_B87dvtQc0TjtNcSNpaGu7ni0VB4E7ggX5JK6ax7yYKjLKHys_iK-dYY_42V6C4jHA4zNB1ZGSOeN_S_HRcEiVPPlw7aERZNZVlXUj3BnHklyAFdR461ts88pX-wOAenY4QnDBjSN-QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
آقا جمشید حسابی سوژه هوش‌مصنوعی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/108055" target="_blank">📅 11:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
🙂
ماجرای لقب حمید بلان از زبان حمید مطهری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/108054" target="_blank">📅 11:05 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-108053">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/880aca12e8.mp4?token=Bb0MlNktUa5GipElZZddEZtmXqYJUJSrfAXzpJf4Ffz2mHUNfoMVNeIam0-XB5gF3G2-peprCJRKRpYQj7XYjn-17L1QXFDqacDpV8Cs4hDZNpGqDT5xb7AubkCMxQgsOaVCwl3aTrcNwm2FIiiZ-cztJTQKXiRkgEJWl3XyKqwuu9_g7F9Q2IMZ43Zog7amFPCa0aKTD99bgHwgkHIVe2MqDe6DS_rxh8mIuQ0xnUemYa7KLrhjeRCypIAP7ZRg3SsVTfYnUPIOgu_aVhbL61ffGsYi0DWcuiDQZZvsfq46TYIBvOSWmJde5pUgdfkmbg44BNVKKtUc9NIaqj5IXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/880aca12e8.mp4?token=Bb0MlNktUa5GipElZZddEZtmXqYJUJSrfAXzpJf4Ffz2mHUNfoMVNeIam0-XB5gF3G2-peprCJRKRpYQj7XYjn-17L1QXFDqacDpV8Cs4hDZNpGqDT5xb7AubkCMxQgsOaVCwl3aTrcNwm2FIiiZ-cztJTQKXiRkgEJWl3XyKqwuu9_g7F9Q2IMZ43Zog7amFPCa0aKTD99bgHwgkHIVe2MqDe6DS_rxh8mIuQ0xnUemYa7KLrhjeRCypIAP7ZRg3SsVTfYnUPIOgu_aVhbL61ffGsYi0DWcuiDQZZvsfq46TYIBvOSWmJde5pUgdfkmbg44BNVKKtUc9NIaqj5IXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
دلیل نتیجه نگرفتن تیم امیرخان مشخص شد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/108053" target="_blank">📅 10:52 · 16 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
