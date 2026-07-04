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
<p>@persiana_Soccer • 👥 361K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 04:34:58</div>
<hr>

<div class="tg-post" id="msg-24906">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmiVKSZd_Kf-a-DDbWxCXSMVeQYDxq_rsdTWR0TQPcK8Q8zTaOndnQ_YGg4W6VwlZASP5QmaEV3z183OinExzdBRsSYNh_sFjVTlbXVhU78w9pvs5p8u8YC72BRmsZix2QQwQfjnEZB7UYCn_AngxBSYPB7VLazTmH7Hv9NMowik_ZXKOY7BS-fCtVhIIzaFUZCpDrMExjJHU-xb7mNgtu29CQLwlJFlWGgnpolSUHdm_snSWejhAIGs7W_nE8OdWUf3PPtd5vZId7JWkXsLeq-i-Ng81YiEHeV0iqkUVc9ac-TsVrM3ZXsWmFzxAfPsvDxpcf85hTYkjGNfED2gRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/persiana_Soccer/24906" target="_blank">📅 03:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24905">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXlMCQMZ3SS9P2bKTPwajWgxciKFgs1deA2POZVCvvNykoXQ1K2EoPINuhTDzJLKE_MBiZOPVrucAMom0x2onMp4VKcqUu9GNG51AR4RLjy3E57oEPc2yFoCAiMxBjrLqt94IVdLs6pAmO32gW7ZSVSBdFA_GZ7hxNOP3KZAUi7ew0gUI_8w7oUp5NSql689KPLEXlRnrljUlVYUuR2t-mFLy4Am6PNzzPMxXEAKW9m_sFUadDKFdlpbXzhkoaXTI40Z7LcUAB1xyN3CUotYTWrA_PnolaDs_J4SzccLfxSsiMIIFE8btJHf07vs9yKBqaHkKG7q7iF6jSAtV6zl7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
گلزنی‌لیونل‌مسی دربازی امشب آرژانتین
🆚
کیپ ورد در یک شانزدهم نهایی جام جهانی؛ این 20 امین گل لئو در تاریخ رقابت‌های جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/persiana_Soccer/24905" target="_blank">📅 02:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24904">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/persiana_Soccer/24904" target="_blank">📅 02:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24903">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBDsDFkUv-MEcmMZ_VzTas6SosvvyuxtIxp32VP0QIv-biCsq0pWXR9RW9RJWC5BP2WVFT7feLVB1CZwFTLaTvZX-XHdTkRMzegSSDiHLN09k4GO2ORt0G1c-yjEJk3clyyp5fzWo76qPrqGbpQxNodY42ZcL5QD4kYIQIBQkhPaJcQ-E9drSoYjj9A1_vIFW4i5OkJ3-T9wptZgR46srbya8i2PNpb-LL8KnpydY-N4fAV1yCsxZ0AibI35dvVoq1NZOYWGd7dv4Gz9i8XCmrmsk8fvGgoqvyJx_uWjEn43zYMFKoZzrRlruQQpSL8KV9E0HbFdlkoHJ-2GjwlWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/persiana_Soccer/24903" target="_blank">📅 01:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24901">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQ3m8EBCRxGPCPS_OV_Li5DZ96jrXENx9fSZIb7v1VrAk0DOxzoywRJWlmdHJe-NQVIYxqckDEHiriO4ImB1OzsngDclGuFJFVJg8Fkb7Jy34QTWXQMEAL2pwxxM-GohBMs115tOv8DWc1pSKkQk7dBgpsX3coeLwnfTuFdLzLnWg-RMEAaUX4QRnKPcc9JpsR1IXJxyMxsBc73WoAghu0bFXqGug2hv8KJ3CPJh_t8bxgVAPiWoaSbctFrSIQiW8jkZoSvAAwPhm2nd_K_oKYoJiS-AovFnm_pebempJP1Dnu8F2JJad6keNzk0ohIwBYNTSaUaF0cxQFieI18CyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/persiana_Soccer/24901" target="_blank">📅 01:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24900">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUV4QWK8-GdRfRu2dzDVKXBX-4CpINwBBjWrgKFtVRbPTNTTJcdGmnLSjEgHa7WZhPOablTiey36HQB6Ns8rE9SS0LJtRFLHHMDyiKHHj_mHQJ9kYTg7DRSOj8Wr7n20HakWe5j_5YWUXhZDGqkZkdlWFCa4vmUxizbQPni3umksLzeKNn1hMSUG1RQZcyO_GBK9raXELbA5G4GQg0xSNlF7n2JpPtnN-Uv3pg30tZ7FcM3YabPaM-U4saFjeg9v5FNRQg3cHk51BBgmQQNC-LrLgU6Jo2dWRNuuE_fx0FxcZVfDfWeO8VLVNmoIxif8TSZD6rFqApjzfeHYD7BQKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/24900" target="_blank">📅 01:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24899">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5Hgf9fxLNhq0gF66M1clv5oN4ygh3PnPUj6fIHVRxr99ZHsi-O9XUmz6bkArDGVBaq6OlwP7_Brfqxo0_lSdPfFuXrwr5pgyuNSsAlKGZBKUud2DY176sM9xsxDWbEscG6JdlUywSePsuQWcscYyWp2XSJPb8Uae6a6-oTtPoC9Nn_8-WQvp_YI15uoReywQX3kVgbUYf09imd_YTQ_ieT4rE_ij1eLku2MH6z5bZ2dv-aCBkQnDMFIGoP__JMIOQN2hBkuo4Jl9iSz7pUOAvxwhjSjgBMh1mFNea-tMmkGmvrGfff-uMwosV_NeF5F3fv7JBcpErn2lB7nUomyxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌کامل دیدارها‌ی‌‌ امروز؛
جدال یاران لیونل مسی مقابل پدیده جام‌جهانی 2026 و بلافاصله آغاز بازی‌های حساس دور یک‌هشتم نهایی از امشب
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/24899" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24898">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7XbEm1EMMQ08_opBMmiIEI-u27AnO88GTp6F7VhN7XAWF2ttqPa41KYomLUWDQEAs4XkVGDWp3HXVMwCLyAREdTDpSGevGlTMn7UrQHGG8AXhWP3Zal0HI6GhQBxfMVxz1VdyE9KftYMRvxeWC0pK47F7O3-kvtexiLnhyz6HAdsq3BvoIuULNcqF4h5_0Lq43XTnCzWcdycIRtDUuEz7HUMjEib9DgP7GBupTI4vHXB86vuxs9zN-jmP_pn3osUxYnct482NimCyqVxhK4_ZhnieKTvk_sGNx3vAKqVePnaujzmBdWpmP6n4SwkkfOOdUleps2P2GR_WSOCtPdog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از برد دراماتیک پرتغالی‌‌ها درجدال برابر کرواسی تا راهیابی یاران ژاکا و محمد صلاح به دور بعد رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/24898" target="_blank">📅 01:08 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24897">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/24897" target="_blank">📅 01:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24896">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/24896" target="_blank">📅 01:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24895">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktggsuQgkEiBQ-rJE9fUv5Kw_ZjsmNeujV1cZrRGdIh9_fTDSiBLcfTHD6Z0_WSZJkTBTWK4qqVcDNY2S1Ffh658naHXz8qV5-Vxca2WKGRasrKHwDzbB3WEDPA_skub7kLuD-nPlonCflSSDONa9dOpvgG49jSp22ooDuShE_OQKQ8jWAW46Xp68qaEOqF82pRM5uCC30ApW77lJ5lMCXPWcNULFYMiQIPf2DtuES79eBjaGCQ4iOn2Kz9NSYizNgrYYoyNNg_2Szq1p_DvMCcIHh0eD32j3OSWpdHCC_bIdhVwhNIraU4kaHYEsgzIYFYnZGUn8FyrChSqietp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ دراگان اسکوچیچ حتی لیست ورودی و خروجی خود را آماده کرده و به نماینده و ایجنت ایرانی خود داده تا بلافاصله بعد از رونمایی بعنوان سرمربی فعالیت خود را در پرسپولیس اغاز کند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/24895" target="_blank">📅 00:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24894">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/24894" target="_blank">📅 00:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24892">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/24892" target="_blank">📅 00:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24891">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2OZkRggAtQIXwnH1WaGccO6_G3AElwlq0Jf2zBzaxP0mBm9Q3ruAB2zyoNceM5IHkX67xx0snb9iJFpMXDFKbb1VPxOEcQUo7LyDZQTphJOmr7-TQnO2TJ5Ifg1nOCMVZFVCWwMHsl2hm3x5e6qhp4ms6SMy7skZ3qCnLJIGS4vWGuAuTc1sy6tGk6HyQTAWYGUttY9lR7ZcqCnUq8DrWIYuutsbcirZsYdQRHBowcrrvCZfRA_LXLK7qmVo8O3qCDXTW3ChH_g_RDGbhPQWyK8aUtzxqBjqpGCGImaPUTyVi4wbSigasTwntXeL-L81LL3AjyjLPmVeJ2GAU2LeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هواداد تیم اسپانیا در جام جهانی 2026؛ لاروخا در یک هشتم به مصاف یاران کریس رونالدو میره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24891" target="_blank">📅 00:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pGaaE2O5eSUqc61cgNXsuyARlieWXVdUPfvKDETzhgebqZQzj2baLQTYe8gy1vCxWvEic56t64t_jRajmUR6xRnDzRV7AS-Rr0ofIlqaq-S44jtQqRlPJ_csw67IEM6eRnUg6dOXaYVKJh4tM0g01HSThD-K7HL0FxXqmnDAvBfzuvP0BLY__kO4SnLbgX4HPU3u2x9LgHXQldGOPyngOZgsdrsdQg72EA3EpFhAxN_9drEjv6Ba5rogeYgUkuiXAwmfKUkJWLrIuynDQUh8llqmG0c-t_W6M1nsbElpgkB2IDH9Z98T2pnSrkrB0n4WI2-pOI78qmpziG_HDireZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/24890" target="_blank">📅 23:59 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsUElJ4kEmDTovOTQvhYxD41_rLQNv1wiGk_FKfWn59-urN8mi6mnHK7VnzkUHuu66hcbDvJMTpv13B-xOasbTzk19LrbQJ7KSGIIi7QnOxhqAhOL2EyiK0BIiCTj5jiqKQUPyUFdA69zdpwDEx9rNTUtCxs_EoIqarFlRFN0jweEmgSv9yflR8u4eW5DWmmdcIC1qU2BhfmPKoBjvIMBSU0VPlFMLojoWPhRqx14yFv4Azo7nJHxeneCY3cP4jIrAOWgEXwGEwT1mH4_nLgsAgu_J6cXtN45u5-rPXkrxxQerXBQUzOVKdBMeYcKKWXpmbFUeomPph18hJ9watvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ نماینده رسمی دراگان اسکوچیچ در تماس با مدیریت باشگاه پرسپولیس اعلام‌کرده که تا 48 ساعت به این باشگاه فرصت‌میدهند تامشکل اسکوچیچ رو برطرف کنند و این سرمربی کروات همراه کادرش به ایران بیاید.  درصورتی پیش پرداختی توسط باشگاه به این…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24889" target="_blank">📅 23:40 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO_8rJU3qwUeqycduwFJI1-4oF03sB1krJqGnDakoKHjIYf9OTNPAbaRbedzoo1YkUTls9Sy1SfWyqNhGXbAUEgkI3Mb_Cmblz73Nwnyd1CHgCB5l5Ov1kYI9boOOgA2BoXEs0fM6DdOWeOpc5twGJAfIrKdSgdlDY50Ey5MJkKHlSevXUvWRrmsP-wEdaaD0vQoY5ZyJdmY9_LYS5UWEMItH0y-VFmfj20CYfe2PaxwL8UDdfEzSqXGxOpRoeHFmEojU6dOAXDr99Ayby0Je80kxG3BBbsoeJ_hdaGATLQYqz5Gz_W_GwDNCnj2geWviE3A2D_lDhnOVpPaHyQ8Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24888" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24887">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r48c7rKX2P0D9KML4NLF4PeBd8Ykvxqkompp17-A5s9kmR2N4NM36RXFpaziQI4VU8AdCDaoG9tZT5gptKbpfZ3gETet51Vl8oY2F-VAQr07RYNT-av97h7t88q-1Xop2vLEbpoBQSrJnAgXMtXqHdI2aYtPcneaxd0-8LQ7V75vSBkABVQW7je-A__e_0HWlzn4fDlrjRBAToJH3koUx2JIIrCwj9fWqT2mc0z3PniJAmyYRGhMazc0mO29sRg9HLMID8Mz_csAMRNRUCQPrue4tUthc9X6PdIwU5FpWQ9lrtObKNRPgB5-y4z67Nh8-VbtgrBd9908UZuvbzQ9bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24887" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24886">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/24886" target="_blank">📅 23:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24885">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_-D9cQgTTkYv3kUsbiyAag7xF5uxj1ph2pU9D5seGWTqYM-6uO9y_B8rWPXb9lIjFElQyQU_RahdEJ34RW18V1HkuB-ooKLaoL55NASpfFEnYdiZyp6VHIN_LCl6fkww2ILO66UwoAujrWwwzYcrlB-eBAdqSg41ovtmD-X2WdgRFjLvMK-_x16SQF0gik5PUAbgX5TeEqtG_q4KNd8oUI41TGJBsGV0xil7aTYuDb40r24c8-yGntYZ_DHORK77UD-eetdwjH_2WzviOOdpM5QuFU9B2mqmrzk9fnd_aIQ1Oz7u-p2c5KDjONSGhh9Zz2bhGuhNEbgHQoKkT-wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق آخرین اخبار دریافتی‌رسانه پرشیانا؛ وکیل ایتالیایی باشگاه استقلال عصرامروز با ارسال ایمیلی به باشگاه باردیگر اعلام کرده که ظرف دو هفته آینده پنجره آبی ها قطعاباز خواهد شد. وکیل آبی‌ها در این حد از بازشدن پنجره‌مطمئن‌است که به تاجرنیا اعلام کرده اگه پنجره‌بازنشود…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24885" target="_blank">📅 22:54 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24884">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBWr_Tiw8MWnk1ZRGpCYIimhAm472eTGswDYhBWyv35b4OWBXCklfaivUvp944RjGcTSPP91hqAH31N4c4G0Z4ytQN2tWeJdkRCiMR5GMTdkMwZ2ytJZMNO6UBJgOkJRsMknS2JFqRflKhYOoNhBaJzH1iQQFmiaM9Lk1E7HGNxoWr2ptd8HgqJof51_50QPpeMmrvZKnCI39Cq8qZG7oieGHtxeBi5edwGE4z0-8z5u4x1hkigZSlPAt7ifWbGt06ulycyAjUBXJ7F-w25w89-2xwrUGweQI2AnleXfEekc4mxsH6iY_wgM_Wkvuq1JB9Pwv42U2u25CkzLwditMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24884" target="_blank">📅 22:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24883">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24883" target="_blank">📅 21:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24882">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFO5eClSUwA3-Eyvjq4pK3-Jjlfrt_M6pHcuzVhBgHSPEESQI9f5FKRCafWZoHDXRuzD_RqbOlJIvLRWj8B5rT5BFB8q3k1YzKdOVTOeTuQfqQXbtM706x7Wa8lhRz9m2OvtkRFRKSH3JnZdo9vKjz5NVI6i9-pwuuhVHAn4XWefz5qHnWgcYMnjf1pZYTyrpT3YrIslzB4lh6a0F4Ok69LAe49q6VEUc2tOuRcRSSbOgOL38tTc44vlRKYYRv_NPjdJpptAoXWyZolLmvvad4KBS-MITBwdAEPLBkrMwoqion7PA3QlRS92oQ8ALi_5rzZaiyXaoOIPy_Qbq6eIYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
رودریگو دی پائول:
یه بار لئومسی دیر به تمرین آرژانتین اومد و من‌بعدش به‌لیونل اسکالونی التماس کردم که مارو بخاطر زود اومدن به تمرین تنبیه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24882" target="_blank">📅 21:15 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24881">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfPi4YxYvfEC9SrGLjRyrx06jCWgJTHrjoxHerPd20QLMFdJvAkgpqMpH6WXOiJ0uyONMzQsiZBid60AwyEsFRF6KZ_58c1Ba5BGeO5HBuM7mLV5Ase_W7QgyI2mEmTmznLDlcrxXupba43aRGjglyoOckgQabMswOQJUboucg8xV_VGGBb3INcAyUWkSzEkQQDjDM81zQcIdOI4D_QpQCC-a9Xusk9xcX1JHj7nA8luR2wM5dBwEop-d2hFGVrsjM7FVbDZ2XtIEr1eRtm0klKt3k-T0Wb3Ch8G5EpZi0U4fnlHWBODGn-LVeDbD4_r7CYcL2TDuc-6I3JM8ZfbzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
علیرضا فغانی داور دیدار انگلیس و مکزیک شد. به‌امیدموفقیت آقاعلی عزیز در این مسابقه حساس. ایشالا خبر سوت زدن بازی فینال هم منتشر بشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24881" target="_blank">📅 20:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24880">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FW3DUoUvCITgEOfWTmZHsMUvGRgSvZlOOwgxI37Hk2PaiGPjRoXH97MPQXfFekyxjD7UO2q-hhewAxinYRAf_5XeHkHgoxhYmwPanaKP1dox_mCQ709zt_nDQaPPwKzhSBjPDihTiDfGidn6ucsAXuTukfDBSulf9-D2e01-S9tICd2542imY1Xp4U2HUwdK22d09dcenrjS1oBVCP-Ya3MfYsO0eVWvxPIgvHzZaEfghwUhnKLEZrBBuYTbscuZxSXB8qV1J_c1uRLGVXYaW5AJrnVkX32eUkobH5TOC2SGfggTgLekU52r7yJO14eELZK3hjwZVhuNVDlcwA8VoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپهر حیدری رسما اعلام کرد از ملکه پاکدامنش جدا شده و دیگه رابطه ای بین این دو نفر نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24880" target="_blank">📅 20:25 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24879">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24879" target="_blank">📅 20:17 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24878">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLL8i8LVVNPFKYZPCNlkS7cfbMdalgA1bx1lIMkHVLLNeHdW-tYdeYaNO3a4ToNVRpBqaW4nyJwq3KsvBjToReLZ8dFLibk__2iAbOACQP5T-WclXBaRR1hJYMPjdMXU3JAGOt7r6No5tv4ytkZ6T9a3fd3Epw4OwTHQNvEfDAPtu-OV_4BWsmwXCxW7n10bjKCDm3HVqcn1DfcKWIDLfvv9s68-DTjX4sQiDxf52wXFTh_Mbzt2uWCrcZYys75cjDfd0SNjKoW-ezT2xR1zqBuySaSIl4MfjLo9lLNABoTK1uXcDswOTYmNyufjg-yz_XKxwPD1ht5woJelauNjyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی پرشیانا
؛ کاوه رضایی ساعتی پیش با حضور در ساختمان باشگاه سپاهان قرارداد خود را به مدت یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24878" target="_blank">📅 19:46 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24877">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24877" target="_blank">📅 19:18 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24876">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kctFx9y6vq6jHuQ0F_cBjBd0ijgLbgcA_r51UNNsN3PvvwSK-c7KCD6Oksl_zrkxtujf-GC4ZkJ1hfVuddw9wqmKBtuZcjTWhPCPYXwcgMFp5MmUV0z0y6YjfbBjvsyJWMx10kKTnrW8TsaudWpMhQu8MrONDFVZwYE0gv_l-ccfywQWuQGJ5p-3Fd5Pd9dU-9_sfdTUC876iWcOsKHWq1jFelq-UDTxIy8yU9JVGvc-S6OQYPa2TNYLsrADqUiiBCLOSvVqwvs5sScCihCBJtdWYDirWEcYGssq6vbhWpt90Sw9ZUPYMsDxbOcb1kAkY-aur4KGBB_i8bTLctvl_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24876" target="_blank">📅 18:37 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24875">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24875" target="_blank">📅 18:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24873">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24873" target="_blank">📅 17:50 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24872">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24872" target="_blank">📅 17:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24871">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oodpjJFj2oF3Ny-rBtz1dkwKSBkMj4JZGJ0a2mnBmBZQ_A3I2NKOo8f5qxgBAJ6HH6zyNWS1Rpja1L8-X8NXD2KImBEzrb_7rodM8JfDJ6vzoWmTeqz5LR3sJK90Vi_NX5iRG9ftWl6QCVIRPe9T4sWoRMa_zoM3_zKV_bx2xWw5kWH63GbsAzf0IkplIdBIqx29VjX9k0TY8I3pcOniYRCzdJxmsBYED_YlgeeDNztJOdGClLi_qGkX_fj4yZBFtq45R1ptHC15qwy2pJZrjTKBeEGZWM6uxUbyxaCl0bKyYxjfpdoR-7bFbnPxpgWXEi2acKaZJ2kSpgx-nzqYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
🤩
رسانه اسپورت: دیگو سیمئونه سرمربی اتلتیکو به‌سران‌ باشگاه گفته بزور نمیشه یه بازیکن رو راضی‌به‌موندن‌کرد.150 میلیون‌یورو ازبارسا بگیرید و آلوارز رو بهشون بفروشید یه مهاجم بهتر پیدا میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24871" target="_blank">📅 17:16 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24870">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24870" target="_blank">📅 16:45 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24869">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24869" target="_blank">📅 16:30 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24866">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=qFnFvU_0qGIn5b6pUZDvzWwuZ_SrUOsC4d8R_i0UQtwwUQZAeZqjoyKLKuBxbK5TRJ_f7zGhhFBvOlrcCIPmzq2QnbvR-cFpL_6vBxxeFVJMufIqpw_idpDVjCbkzv5EsoyczRrLPy44eRsHmOcMnJOjYaFGoLh0h1DOEyZMidVRETZhkdqv8wPDGwJPr8Et2a_sc0NK5HSULs4EkhgkTfUS-afwWRv6T6TR29YmcvAG4oXaYCngbzjb_dAJ9T55mQoWgTOhZnKoWOzTtnjqSaTJ8FSdY6R38HYxOpS1FHkeS6zS29csaAULkzxpdZcuhzr6QEFZD4FeQxjjMtwjyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8659ae843a.mp4?token=qFnFvU_0qGIn5b6pUZDvzWwuZ_SrUOsC4d8R_i0UQtwwUQZAeZqjoyKLKuBxbK5TRJ_f7zGhhFBvOlrcCIPmzq2QnbvR-cFpL_6vBxxeFVJMufIqpw_idpDVjCbkzv5EsoyczRrLPy44eRsHmOcMnJOjYaFGoLh0h1DOEyZMidVRETZhkdqv8wPDGwJPr8Et2a_sc0NK5HSULs4EkhgkTfUS-afwWRv6T6TR29YmcvAG4oXaYCngbzjb_dAJ9T55mQoWgTOhZnKoWOzTtnjqSaTJ8FSdY6R38HYxOpS1FHkeS6zS29csaAULkzxpdZcuhzr6QEFZD4FeQxjjMtwjyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
ارلینگ‌ هالند ستاره 25 ساله نروژی باشگاه منچسترسیتی اگه درکشور‌های‌مختلف بدنیا میومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24866" target="_blank">📅 16:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24865">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/liF4h9fx6yY22dvHo_wPr5kj7lKdBPyhcav8hGuoF8crwATIvlb_8f7fUyQe2zWVJi5SmabMbeq1QCsXNIxqvKo0mwpwI0HI_teufEdQHN-Q_PCCnaWX74oXDbXyL4Hy98MHKIRxyQZjeFkQ2oYaoxC01pOs0hcszP9km2ZRfKt1sZZtHB69POY9bthucofipEnbIMGLqs7LpqyKSt9u_gpDJIk1pb-9sU2cBAO-RxOzuIZlUm-swkVBnTpons3iuo7LSRdiYb9Gosn9chQ0HD4PH85nacm3SEVfaLV4eBx5yDDIDrwDauMze_4Y0yn5ZR_oPeXfrIYBW4Jl5zCd9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: خواهرم‌ گفته این‌آخر خطه و خداحافظی میکنم بعدجام؟ دیگه تصمیمای عجولانه و بی‌هدف نمیگیرم. بعداً تصمیم می‌گیرم، نه الآن.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24865" target="_blank">📅 15:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24864">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKaG3wp4jIHgoNe8Z0mBdwfhgK1PcMxDBadN4L6nVCJDIC7Cm1ScDRzKJGLOwcZvQbJz1-k3idjSO5PscoOSMRkuIMfTkE0zQdfwBD3-0XjdlLUMMkUsLiWa5VQEjtD8EWTUf8Ds2SQ81rT9ChyF__UsGokf_CXTsM3X8eFPYH4tvZnmgP_dNOdclsiRu4nPT6zbaMfCK9YmCST6YInd2Z8hrvvVlwfpjzvm7H6s_IsyhTkVx526RTNnKKb0Lo56ymMdL_y_n1bZeHZn82vJ-lU1v3iSn3zBUdQlQ5ri9t04xUuiBVxKf7okeOYA1MJZOaDeYeJ_89Cw7vf84zJWRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
محمد خلیفه گلرآلومینیوم‌اراک: باشگاه استقلال باآلومینیوم به توافق نهایی نرسیده. الویتم حضور در لیگ برتره و دوس دارم که در تیم بزرگی بازی کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24864" target="_blank">📅 15:39 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24863">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlW6IB_7ySm__lSYswXypryYC7mzpOVUU6H9Y3K8tu4ZBwRT_G8Kqm1v6OB9FtCtgpIJMPvrSCn7qusDVIPhZagk0lWr6js6TXC4xYw0TBdV-wqzfIy02WyyRaTdZtZCHhyKtYujVKI2x2US80QWgUFmsFhdXTkxa7WFM-t-Lx4-RtcbqQf7rnfrx3SEe2by69YEQYpJ2fRNr-Od_DS-zq4EX26z7qiikZQrCvuUn6HbxVRzxPi263FLCpG3TnpAhVQBknNA2ZXOnrUBvycI7XCy0Qbg8GnxVJe5sN_DX5rGcDB2aTo2prf_BFhaPFh23-c9SDzl7YP8Za2-CZxQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛باشگاه استقلال دراین‌پنجره نقل و انتقالاتی بین‌علیرضا بیرانوند و محمد خلیفه یکی رو قطعی جذب خواهد کرد. با توجه به توافقات صورت گرفته بین‌ابی‌ها و مدیران الومینیوم ممکنه که محمد خلیفه بزودی قراردادی پنج‌ساله با استقلال امضا کند اما یک فصل قرضی در…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24863" target="_blank">📅 15:13 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24862">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHduZ07EsXMH3c_rzFibHXTYw585b3mgj8TUKEAYx1waD8gYr6Cyy8F6QeReSBLZprKcnl09Gx7T6pztj0m41K7FDFo-mYWZlJA6ECAFvc-6mdza9bW74eHxLSy4ch-jMLU05V1R2IIYqHs-sZzQCSINco6-YVD2PPpSUWTlacCdRVPf8xXCiKuCJQRYqtb5xMlqc3rp2U4KpNnbM-kSN2fLFW9ZxawYEEK14_Ki3AZl0IaJ3QCfoSwU_LasrPDW_d9niKPHb3DsUZXaYYACdsUnVBii4W03w8PQ1rdlNPBZ2AP7yXWqrE2Dr3MKM62o1c4tI5ieqVHzEJVM1x4_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دو تصویر متفاوت از کریستیانو رونالدو در دوسن 21 سالگی و 41 سالگی تعداد گل‌های CR7 در کل دوران حرفه‌‌ای خود به 976 رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24862" target="_blank">📅 14:48 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24861">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhvUGUReSA2Icn4DCwdAKCHRn2JsEe5B6NVuoO8tlLwRP-unpp1MGDivSHFtjDz0W7-9UF-aE5g_gDx7987CPuGHhs2tjJiIYUCutuNmBtzhPw5DU7CxZNxj-2HvmQX3QbDugmrnR4EHjhh1Z3BwTloy8RsxL2L9lmAkDCTLLtio9nrh0E6Finj9tupOsies2uHOfGaWOzqUr2tCDOpi0HBj9y6B0Sy9LHxwLIGhzHDeOl7d0YTrFIwdUvenqyz8wdaZRc8jSb3AuEA87rZO2aNXzmxMvEEgiK1JhkA9sFKdz1L363kGUOoOQT4Mxcz6B_5JqtIflafgvbpNKPR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
🇩🇪
#نقل‌وانتقالات
|
مارک آندره تراشتگن با عقد قراردادی‌قرضی‌تاسال ۲۰۲۷ راهی‌آژاکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24861" target="_blank">📅 14:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24859">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fGWhaHSOEHvMsH_pVifeLqjwOLKJVLbvH7nikxY7nzBPntfjXXWXuiIx9ndLROdjGvehs2NQjdK-H3tCqu-T5FdyKCJ5TYWfttXVxnnvGcdclLDwOrlWbrNJ8A09isqg8ivcKj7nWALB1hpDFAUG4k6Gb74eHYCOGmHu49IRVoI0exy-XT6tfe8AvrquAJIo6gh_-AdHIh9Tm4H0_wWUcSVs-dCRRWQ-hprCjOHbWDhr6xICVQj9VQhpflAjGrCrBHy6C8ff21koj5hHfhKCnyc76sLjn2gAtTbWT_tRiLzcD6nlBQekV8meMPGegMhPTlAm4ExrXYPuHWOOyt8WIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a322be112.mp4?token=pNtjnTkdVPWWWdTUtA_ICRx4bvPIM1JkVwgnuMPzTfewOtv6Q9jFp2AQIPGbcq2hntOGRHWwS7xhUowAHp2P-4gd5VKsC4um9MsY1YHarZR2ZKzNOl5nnRw9BL_8N34cq4jkN5ieXNmJh9KJtIfm7xmW4lgQTWhFUo3sSIKnj95b4USx_Gfv-gSM_WQZYxVYfqP9p3sCBXGTsEZnZHbJ0DVrW5ju1NviyCmZ0nyrOqLhXSu67BLdwE6uVPuFe1gWgTRV6O5QEzPDJZrQ_0d923i0J38YnA3AkMmX0l6V7KyMmH1CGDbFQT2_N_S1HjPUdqchbqN85vme4jlOru43HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a322be112.mp4?token=pNtjnTkdVPWWWdTUtA_ICRx4bvPIM1JkVwgnuMPzTfewOtv6Q9jFp2AQIPGbcq2hntOGRHWwS7xhUowAHp2P-4gd5VKsC4um9MsY1YHarZR2ZKzNOl5nnRw9BL_8N34cq4jkN5ieXNmJh9KJtIfm7xmW4lgQTWhFUo3sSIKnj95b4USx_Gfv-gSM_WQZYxVYfqP9p3sCBXGTsEZnZHbJ0DVrW5ju1NviyCmZ0nyrOqLhXSu67BLdwE6uVPuFe1gWgTRV6O5QEzPDJZrQ_0d923i0J38YnA3AkMmX0l6V7KyMmH1CGDbFQT2_N_S1HjPUdqchbqN85vme4jlOru43HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
دربین‌تماشاگران‌بازی‌ اسپانیا
🆚
اتریش؛ کلی ستاره بود؛ از فوتبالیست گرفته تا بازیگر سینما و خواننده، اون عکس هم خانم روزالیا هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24859" target="_blank">📅 14:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24858">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyPhh04NrqK59-ZJ-aQXZyVGwBvsn5bYG0-wrPrml8ZYTVMUNIzL6XL_Vnq69IBMoAR0YvOc_wOVE1QKGexI4fjcg1c2RyRM6SmAahnHPp0a-xMPoq6SM0HcKYcMHl2P8rG5IxiTUQlXnHEZLuMy-6ZwiCUuf1535cIva_I2_yQY8556sronOT1Eni0UpzM-DOMh57y90lAfJFgaKMvZiLIGqCU-1Cql3N546JMeWbRTPXLTw_pCPgz68PFUrgzMbuvImmOJPSVlJunFwhUTecXccrcSf2ajxO8Il-RcO_-ng7rIZvcutGwjIeKg0Gr1NKmbktooD1mEg1XHoFaw3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این هوادار مکزیک گفته اگه این تیم انگلیس رو شکست بده به50خانواده‌مکزیکی کمک مالی میکنه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24858" target="_blank">📅 13:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24857">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5srLoi52ZDmHApl5Yt3kBq9WDJ5m5Y5E1tZjtkudEBWODTS-FGsDMzIP9K-d-buhrmBarpbbHZF3gQaL2OJiQw1vxn2_9Q-w85-L-FV73g-ev7SOQxfZGrmhOK5TVVU8ivUxS1SPknDp-hW4khZDqMLMa0kLF9kLhOi1zNbqlUANogqhlD2obq1snOS4wONuTegvpbDGpSn82h2-apKSTQRmgH6I6D3OcbBXJMGPGeH4S1w6KHmnTL2ZJu1QE1IXL7xPCIB6AWpcwWcI7cdBZ1-gdhk-CQ5qtRcn46SPgOXFp48aasmpT_ShWtVolPcgF4hZsyzJgFRHd6g7YNK5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطور که در روزهای اخیر بارها گفتیم؛ دراگان اسکوچیچ سرمربی سابق تراکتور پیش نویس قرارداد خودرا باپرسپولیس‌امضا کرد اما اومدن او به ایران منوط به پیش پرداختی ازسوی بانک شهر است که بارها گفتیم یکی از اعضای هیات مدیره بانک شهر مخالف جذب اسکوچیچ بااون‌شروط…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24857" target="_blank">📅 13:10 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24856">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noEL5qDxdDFTTbMCcP0-6n5bQgfaYGHJeuvCcaWjTAf5rl_E0Pc_73MhG95PqqUT0FFy8VdSFP-4cILSbHGur1cFjhCIwRI-uNZo6kRbNOnozfquteC6aIQiYYPsnqkZAWwGNDJFDYDBZIwi_fHKo6Y4XPU_ZaCWGD98wl9pPR_0oDMZ_GLw4euXTjZuUuLR53FxZsmcUw_3tf6Z1AmgY7GA0vfB5NQIJer1NTfbQKZObQiNHi5ywewbktuxxGQ_7symK7-YVEyfCL5zEU_DkGbvRKzy8csM60u7vY8R8gH1lLRFVhSwQLYBDbLhL644A70pD91UzdhT4CaztW_jRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق شنیده‌‌های پرشیانا؛ باشگاه تراکتور بامدیربرنامه‌های محمد دانشگر وارد مذاکره شده تا در صورت توافق مالی با این بازیکن قرار داد امضا کند. دانشگر در کنار مذاکرات باسایر باشگاه‌ها درتلاشه که با قراردادی خفن به استقلال برگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24856" target="_blank">📅 12:20 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24855">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUNmVl9h-o-XOOqTyurO1dr9iJb5lEQNkN7POD7-zD85KjfDngjzRtGjllL-7-Pb4hdF3WyQdfe5p3vBNWyiEcTZo7DKhZI2x0EHKwKYP0dJJn4BWkJRbrdspW7U6BDD6LEp5G3MPBV6v4F1S3C0sQ49NRUHPE-oIRtAmu-vG9j_NAsbaOKZIy8FQLjI_Vxlw9H6P0n-iqNeJOp_kV2dQt53C5QD04N-lz1TjiC1f5fwjI_foIzTfh1IS2Si8ZZqPdJxJc2eeB1wVwBJE2D15qEy2d1k7h2aykB6aj5oBDGaIYQNU87lTKEg5hpDCP4MJMkJLVmrJ8GjqS8YnYhMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24855" target="_blank">📅 11:44 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24853">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ku81hv-aigeWWNRv_hbPotYcLtACkoOc-EpYaYuUutm5y3fH5xgb45pd3OvHF_eLLvhaIuxEtOV00_iFbMLPhHXdh_1kUisUJgwuDT15Me912fIX4nj5Giz2q-vULE8L-nWUrAQVHIHGNX3FJ7Yf1C6IH8qx-fDXrNRyP9DQ4iPMEk51z1BTqEsZZ6K0TT4VWQEjlItzIEQc8Zhczhd8zhfHTaxs19qRkEKWbCB_0O33s-Su1BF0j3TeEcz2s2U3wDPpU_1744eXRp7TRevT3GDOERimW5wLKt0h08Z9_i57TGVP9BgNFv5ZUrbrCbAN1a8-U9dyf2UqqbXRTWv1rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6F2Yr5Kl5iOQtCSH8QOQRh4Y8Xu_HFLLRcOnYrzUXFaXQFPLcNRB1XOSWLyK_pwzWDKnK07ty7pMoKJTqEJBhCYH0f3Tc7Oj_07kq32XElkpdIvL8DaaB-KfeMFVNqOK-UE_5loph2rRLq1m9ifDJV797hN-8GubM8zKwIbHSDId40jRR-Sc9Ru35NYKzDAkxCPjhGuOFRU7SBcAOybgF7JOb4DCJYUEbRWYLMFkXoKYX4dfQvMCfyVrHZBPNj1qlU7iMWUwP-uqtZLVcIzW6lOzSrEy-ac0mwsvtVO_HC-tEuTY7rC73HGylI_oqhz0184q0l02zdbPUJRVZgVEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇵🇹
به‌یـاد ژوتا عزیز؛ دیشب پرتغال درحالی که یک‌بر صفر از تیم‌ملی‌کرواسی عقب بود. کامبک زد و با گل های رونالدو و راموس تونست به مرحله بعدی بره. رونالدو هم به منظور سالگرد ژوتا  پیراهنش رو پوشید. تا خوشحالیش رو با اون شریک بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24853" target="_blank">📅 11:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24852">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=sYY1QXSePKSJjWpAkWF-8sjhPkQowE8e3Sy29DtKnqyum_JjsN7uS5RiNjuLq_wsvbI51s07Ae_b8eEyNGcJeRFmRvlQ3a9uu6-nuEhGGpFYN27I_Lxu4AGh13dNFBeV-XgJvMs-Vvj7VB9Hj7ccAGlx4xJYJSk0RU0ncnmDzaT1y7ECRC3zsKwHUoduciTs4xHV3mf6Qlef4657kxDi_FwYNW8U5n2IWjxtSRyOgzgpHKaagTcPgi6oKfro0GvS33UIOADTj5U-gHRKiq5F_7EGkHFVNYJJUzl9S8w756KPNhZx2xPX6bBlvurwB3jZTpD1CymfcrgG1EYW3gIwRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f468b62e.mp4?token=sYY1QXSePKSJjWpAkWF-8sjhPkQowE8e3Sy29DtKnqyum_JjsN7uS5RiNjuLq_wsvbI51s07Ae_b8eEyNGcJeRFmRvlQ3a9uu6-nuEhGGpFYN27I_Lxu4AGh13dNFBeV-XgJvMs-Vvj7VB9Hj7ccAGlx4xJYJSk0RU0ncnmDzaT1y7ECRC3zsKwHUoduciTs4xHV3mf6Qlef4657kxDi_FwYNW8U5n2IWjxtSRyOgzgpHKaagTcPgi6oKfro0GvS33UIOADTj5U-gHRKiq5F_7EGkHFVNYJJUzl9S8w756KPNhZx2xPX6bBlvurwB3jZTpD1CymfcrgG1EYW3gIwRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
از دو شهروند بلژیکی پرسیدن که حاضر بودین به جای زندگی در بلژیک در ایران زندگی میکردین؛ خودتون پاسخشون رو ببینید‌. چقدر تلخ بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/24852" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24851">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24851" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24850">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs4jFJ_ZErYrQOMwKpIBtpgbXmZufxu7PCPOYmU6aybsky7A1jq4KecSRln0ea1YSpE-_nadHO7OJmz4-_CJ1crZzo9nGdoTrmyDfRphLlFHtMlbFPsFC6x7B8pyN1RUjjBYFxa3s-92puJTufl70B85wGtHY4Q8NQi_WoiBBmQSLqSOldgMYK8s-yZZiwwoPcC4A_NkdAUiXpEuhBJrHaFAdiph_idx1dfG1J1qrgfNdyLPXoX2P36fGXSxz0sSV1Ef8hMNy904_nrj_IQXH0-AEjobhzJwkJ8JSi7De-fZZoqr1Qsh_cg_JYRONf6CXg0mPf_SsrBvmJmg3ZsY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r12
@betinjabet</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24850" target="_blank">📅 10:42 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24849">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYedbC2_pYbFamWQRAVTHVoNRPsLahP-WIZAtgcemhELuTsiYXOuCO8yULGDRl6p3kk7laJUduYErIDUAQCdfzu29O7T_2-RcflimAW9RSUqEURL11hEsCp9gOwoSokV0_LnYuApRO-xss8MRy2YFH5vGg4zfp_VxWegbvbliu-fQlYga8D20TKClS8azzvn08gAz9BbQwltQJW4fmcRLeHPYx6LC0UFuaX0sAV_okEu0lHNjkM6yJ6hQpde5q8ASafZJq1ea9Hbbou0EgQr9ixih27kPBbb4zNTPaj290j_1P34EAOnvCubWpRgS8_UtjHuDxklgyKhIWcISmbvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
اگه سنگ اندازی های عضو هیات مدیره بانک شهر تموم‌شه باشگاه‌پرسپولیس‌از اسکوچیچ رونمایی میکنه. پیش‌پرداختی باید پرداخت شود تا اسکوچیچ وارد ایران شود. امروز پرداخت شه فردا میاد. پیش نویس امضا شده اما شرطش واریز پیش پرداختیه‌.
‼️
دلیل مخالفت اون عضو اینه که…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24849" target="_blank">📅 09:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24848">
<div class="tg-post-header">📌 پیام #49</div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24848" target="_blank">📅 09:35 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24847">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jF79qHdAC9gCGmiHqr_qOxO33nsd-KLL1pqo5un2oLJZhrdURSo9Q-aHlmBRWwOhJjNMp68LMLIV6J9pQ00p_DRVt1EVTTFCQWrQBsyCh5Xjqr2bPy46L7cLL_L-uuObZ80dp7KVdjwtz8KGnKKgv0nHJOpPBvdNf2WRDiVRl2gBn62sM0xejPsWIcCwvMWWfAdRtJcCCMPfhJofjQwqzj25tUGmgZw4jHYKJ859W8CW2Rfe5aZl7CZ1dKm3LTj57SEQAm3cvdoxYn7xtgfJ_Qa-lg6ZQRW8hvNcRERc0GsStw3_tO86kMmh5cXxmOYq05GVpuKyZVVdYtCnoyJKmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت: کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24847" target="_blank">📅 09:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24846">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUSdhh3JDaeDpY7rR33BKpl-TYwME5byAhgmVP4_6toUeZLf1rJ1furMrE9DApEcO2BLFgXc0d-wJRLtjSirTxme9Z2fktPg37-n45QC-Z-26XQIVa8Qgc--Bizx5HsKseLR09WMjs3UJJJivosRAK_GH1S8xytAD1Kau2AT_RSElBqdZxL73Pf2lcilZIO1tngl42rpMs00-zNCPzT8Nqbt1KI2sQEvf87COUUREh1zRXdh1MSqywhg9NUQdAFn0XbVyyY7DSprohwmhd-pqDV3RZrpgUgvXEIU7PWSuot62LXfbJKDEuRtuErAGTywnKDBBYXIx-EUw54uf9s6qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24846" target="_blank">📅 09:01 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24844">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uNLnv0IDJ9Ya-YBIjeiLvswHxIyZ-Vst9mvIK3pDIpkJm-Nd9jQ_GMngOZu7UYDjc-J7hb4iT5Q6rjjoqNtWbHlO_4jsSD7YigOiJueEvM-vOiiqp6wuI1AgzayTLie4Det2Liw-U96f6Uak0u1dvqMUSkuk80ma8Jhp5Ax0NQh5tjEEl7FfC5SuGfpzeYfBoAp2kmcMQ03oZXmnYZWVM5rEuXjMhsmFJLAlTIXydvz5pJoZhBsa0BllIBgzA5ErHZtqh4RFzbGfdpROte8_9BI35bbMifuU5reVUWrBwiUNdKV5Opx-9_Dm30vWNwZyXMoS1TfKWojfG0cBd6Wdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHrN-ByOOMucga0yvi4RizIHpUtPCAalBoGh7sb3X5P10jaHL5pO6ss8S9xIoHyWXa7dT1UT9jb4_TcpMrHIISnZ6_b21DdGDMFuT5JvT-xGtkoawgFgn4BMyLpRcMK94t4vdj0hSTV0ckSAhYQtTuOFfRXeCDsOyE9f2Y55ZPaiS3O4woZ9JEclvR4twvRY8e8UGYLM7RY6Rq3PXz_flCXzOfpRujk3NiU4BBlk2JkNQ8yFvPWhkD8oCTakEaEkLlEYYluSX1EigEvNlxNdfhjd4f2E6_lXjnvc9JfAyhFdGOcOQGETgVFlLwv5HUbGiDpBM_AYimz_fIDqlkNjXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇵🇹
گل‌های دیدار تماشایی و مهیج بامداد امروز دو تیم پرتغال
🆚
کرواسی در جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24844" target="_blank">📅 08:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24843">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bxYfIq0fGNKKvyEgNIK5iEkbUSQOSBf9WBVunpBSrWEMcn0K3wQgMieYDRgoLkGUKISRdtgtz1kbmCbF_mCc8jrYqbYRoJy9ruTxRB5EiEycLDtqHNmxWZW5k4QyWtZvSJ8mfoB9YFn_syOAq6E4v5v9ci5q8BApuFFFhyrQcWoZxWbxztnOGVw4kee1WexTyClfdNvEBLG-c-rtgE349KNKp4QhNIYPKDj5ye_LDn0z76DSccn_U-HRRUOlJC_RFDj408ucKY5PuxQ-QpCUk8Er4JsSpphN6JuSqAom2WqDTWE6bPN7XYD5oVZXT7SSNrtx5Dk_03b5FzIOWrpjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی؛ پیروزی شیرین و ارزشمند پرتغال‌مقابل یاران لوکا مودریچ با درخشش فوق ستاره پرتغالی فوتبال جهان؛ یاران رونالدو حریف اسپانیا در مرحله یک هشتم شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24843" target="_blank">📅 08:34 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24842">
<div class="tg-post-header">📌 پیام #44</div>
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
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24842" target="_blank">📅 08:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24841">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-9mzbzPds2SeTyBgcPrDQVSPrdlPmi1HHSdHH2HEtah9E_amq2ArR2C626eNUSGfEtqAVVOJ_wcMx8BkPncfABbMyISAPWVH7EcwOJvWT8Jfba27z7sg8jpGPIRoxbg7leCQKIRLiasURVYrQe7jkjlUKQzhQhuY3r4qtZolSruLUqzBosU3qhDuRWjOjTCTAICVgb1bbj9lLsWKyQ4s45vHS535yNHHfU9mkBazzgWPp6cM4p8CfFsWpg2cCCE-5anQYtGGpKc_vBKUfC40ox8mn6RhXTWOFT4MXYrms0pe-yuHzFEd4UcnzQtjCKsUARQR5uCCV9OICulsW_7jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
تیم‌ملی‌اسپانیا بابرتری ارزشمند سه بر صفر اتریش رو شکست داد و به مرحله یک هشتم نهایی جام حذفی راه پید کرد؛ حریف بعدی لاروخا از بین یاران کریس رونالدو و یاران مودریچ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24841" target="_blank">📅 08:29 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24839">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0bjBH0Vhxb7LgpDIAOswuUaThCYFuAMfgqPDnSH5X0qo_zhvNeYx9srrB7FfXyY8RilDPeuXgKJw_Ok55rHdli84S_N8wd9Et3fs1BtzsWD5XCN7BUNM3e2SXOjAoxnfwLUkw1j3Da0sLDqsaQDS8BJuF1mznhiZK17zXAj1Cy0uy89pBwxaNZCzmW4l_KAD1dKDN2ia1mnvAIIfKXfB1k3eyOSfD_gxvPmuegK17UVl_dqed5dUNAiLj3EqzBM8FF51_F0I4IYSgEtJavRgkmUzdBllqTZxMyPpfbfSE0i9tFJAbkylssNSMfXoSzXnQSe50RQRh1TN6cGCSGRlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24839" target="_blank">📅 01:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24837">
<div class="tg-post-header">📌 پیام #41</div>
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
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24837" target="_blank">📅 01:12 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24836">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sX6-OgMRFMMG1r1K4jnWeZO5OY0WEjNXB4q5KUEtOXsNX9JHS-4o9J6EpxKrhDH0kJkjD7fH5CsiHymGWbnUGVW_oWeXkger2PLr1OPMmDyMhpkrjl0Sw565kLbSliZ71NmxNdFP7HI1zfvWYLJVM4kNLAX87SiTynrs1-_2wzUaEo1umpiOxVq6cMBJGgy2EQB1RQv4BFACfUD_z9xVwOtAcexDEIRIdwwwEzgeEYrruU6Qv8yqyR8_K9vOjBkzG3c-vw3rbtg7gceLY8ot1f71pqpQe8D2HJSTVfnUXktASuR6ATvrgmrnDVDFjWqzqf4DF0W4akHiJyBDXG0jEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسول‌خطیبی درگفتگو باعادل: قلب محمدرضا زنوزی روتیغ‌بزنن روش‌نوشته رسول خطیبی
🙄
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/24836" target="_blank">📅 01:05 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24835">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJWH79Ys3tbhX8ZQndVzORRXe4DPXjJSIKfoHAl_Fx5dUhHUEt8AWUjzWiLaFR7wfNqIYz8PvSOIZ3flP4gfAELDZupzcy-OcR5NeR9cDdqV0N2pgzNxISFbqBhXlpd9nYleOlIYUCFlH69yOXTQ4XUkdIuS7WTO8EdF57k5IbzX78zFrrzERR4RA1T9dMLPe6hUSCk-sf_39_24t0-3XivpRtGO5bhFqHJe1qyWZhsIGU_6OQwh6LM-vGcphD0NCcG2DXS53ULMVzCyDMqWwibWz6pw9o0RFPviGplbTRzkBEkVIg4OChsAZrQu-XUbRuj01H2BcA19hVhHyj_mWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد فوق‌العاده حساس و تماشایی یاران رونالدو
🆚
مودریچ در تورنتو
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24835" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24834">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDEAnU_9gpLsHDcOmhT67uJIYIrTKnQ1k1vYBwRiWOha4h-1OPx0k4HPS01l27ggA0_F7ttPqQvOrLmc7f-2cP9D3ExJ6Jpxg8cTE7Z_qbZ0enRoOwWfWyChURR5Etkqa5W-ArxenQJ4DRIxnekeQMrkXAOf78SrQiokv5YjKF3O4340d0XK0fIZaJChgi_bwj-GKdOHAl4fO5jxo2GzDBkgfM9ls9niAz1gwWGA5yCrF1TszD46rWX2_m28cc9NWHGkLAJdoBFNvj4S1uJb3t2XXKxX-UqhptQ6SaCg5WOQ-aI5jv7uqeKkJprMJ51t6JSU-dj36j2jY_kWF-8sjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدارهای‌دیروز؛
صعودمورد انتظار آمریکا و اسپانیا به مرحله یک‌هشتم‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24834" target="_blank">📅 01:02 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24831">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24831" target="_blank">📅 00:49 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24830">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdPq4URryJXpedqlt3Afr6PMkUoaA2O0PLQAoZCs9CprBJQOvXD-tZ0bgkGNM6UjjfDMFc-JouvCiiFlhaaq5ie2aLGZN3C0wjCzcZeQEwmu-JV3yb2HsXUxCaLYhiP0I3SeDgX_AgjjsJxE9Yjix8IOBqqAIdlH7-w8tSw0UD3zrz5lj7hmeilMafV_Bb_gC-iDyoMHvAOQ8sdF9c1KWD37kYcKgn82T7M01ydIg2ZanzqZqRwiac8PUcgaDLv6SyyYaodTCldoT2kZaakQwehCK-9cJwzicZPNfoGwEJWCTq1-ZnVaOdCmy4Gw4EGCb7w-XQEhB21anssyGDbiNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی رقابت‌های جام جهانی بعد از پیروزی سه گله اسپانیا مقابل اتریش. بین پرتغال و کرواسی یکیشون حریف بعدی لاروخاعه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24830" target="_blank">📅 00:33 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24829">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lqt5qd9Z8jrA2FFpRIrZWofYl18bn9SKtytlW2rm_QX-vD3A55BhhosH3EzqNuTACWELMhoFyFq8HT2L4Y_7UmQ38fhuWEGnM4X2wRKOJmAtlXkhcbfk38g_uMfvekIvm5UKVx3H7E5zy_wvIsjj2HMIrRy0iXNxqyyDqjxdOw4EPz1FG5klP_Qk_k4AD7zDFHl48YMNP4pzLWAXhPULY1EWY_U633nu0pnTPgwUnkfPPt7ogTf9b732KTEpKeIR2sLDybJMxeL7Iqbdh4S-X1ONnimToXa7iXP3mM4a-KFWoisJLkWi8hS1hxvf6NRSeIX2CNhsVw3KgTG-T3og0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درمراسم استقبال از کاروان تیم قلعه نویی؛ تو جمعیت و شلوغی گویا علی نعمتی یه لحظه غفلت کرده گوشی آیفون 17 پرومکسش رو دزدیدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24829" target="_blank">📅 00:19 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24828">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXnBcJGnelOGdz_nnVwMZqQfChHIv6bnDlQNQlKSFOvvLnm9OeBePQB4bf8RRcd8wgLRPBWq5c138qsAqdLPGu_H89G0jCITfV-svpHjT_xNwqvedkxiYW9DA1Ag-cvzWEUl172Y4ZC8SHGBqt3S747jMe_U75FAis8yZjtofLTD-aS-lMyJZTm4Cbc8E2U14NNkdea5aFGUGhZWK1r_I9TJZ5m0lR7JOEP8ZFdIf5ZDr6jZXiVTc5vDYLujzbJ5TmFxgEGq3VfnUxuh414VxzBs45VIBPYxfuc0c2x1ftkzvy588EbHXeavHWmgFQh2hf2xQHI6rmZItuvqkvL07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24828" target="_blank">📅 00:09 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24827">
<div class="tg-post-header">📌 پیام #33</div>
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
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24827" target="_blank">📅 23:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24826">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z06_QmEszFFk8lMq1KQYos5_IWCX1Lj59Xh4PSBYNGIWCexZwgK-8S8M6ZPRCQoqIMJvjyEr4w3JBw6KIy6B_rprUQEleBdOjhYfBzwfxVNwhq0NTI161wQ-3hQGTCm7WVQWJe_uC88K6zlmsDJoblU_Qq4WgtWzdfIy3PzlTcqNa0N_kZc9zH1g4LV_q6NE3ZA6LI2m5RA-JKS5YWZyvQlGhJxieL0fM4kj7hyXy5gKADGXXet-IpH6Xp4a0OKi0BTR1VGXAe3VczMYOJHap-j29PA93xq3VymMFwznIiACtRn1TpKNdiJAKAbrOVeFd5tqncqreSiyJ3qq1gjZDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
رسانه Smashi Sports مصری خیلی جدی اومده گفته ژاوی روایران‌میخوادجایگزین ژنرال کنه‌.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24826" target="_blank">📅 23:11 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24825">
<div class="tg-post-header">📌 پیام #31</div>
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
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24825" target="_blank">📅 23:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24824">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNSBWRbje_RPJyhy06c0yJi6H0lpWfzBRE3zcvLPofzaWBf3SmhEJt6rTx693V5jtLS3lMiO9eVNLSt5kU_6EzdqcUbzbLeDMvmlvYA3z1zvEB7nj5BTtcMJdVOYumg7SAfI4edvjPsYsF8AbMqBcOvmCwRhL3CNc-LWZx0wbDgLZr01Nx5Y21XlXGg6wA4NMbQXDLMOF_fpJ2ogXvE1Fdajh-2piPWciCwHgt7OVbezatGC4OfS-gnL5_zKK-1YlSGUi-8hFt46ViQjTNKXCEM5MyyjD5M5Dlv3MJKiJimWTVEeZuFsoygU3Qy6g2XA67KUt3uUBjlGI1qF9gRP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24824" target="_blank">📅 22:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24823">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YC0ARqyvfJB4PMB2sL2Oqh2o4NZkzoi5NrNwCY3KZGZ-FZWH5_D6RCmKVXzLfN2D5k0vVVVHm1G3lOL6MM-6XiEEQh_iRM7bDrbvGfr-oxGZUjbEHjXBdHRmuF1eWI7pRMsrIlkW30EZK8mE64G5kIqlMfF7tCmrtPRlWn3df4m3ep5JwLmIyAYIYgOuL8RfsCNVDmufPi9xaipXuzcXQdHTC2ccfpHlP2haO5n3bkWgSthtEHsNLG7k_DyIOFb3A-01qimuQ3UswhZvaytsa4fMiJMnsJlB7n3uHOQCewBEvAo-3RsnttJheX7nq-26QeWu6cPlQsPrUOoXQGaxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24823" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24822">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8glo_Jlj5ehxXjsWXcIr_JzM0n5G8_MpWt-4xO7imSEfsEdGXYeP2WIJa7KY-VbdjOnlO37Uvaa3KF9krQYgukRtvEscIPeMKlqkhV-ZXKGvCNw6lxFbU_TKByvRFE-BD5_B6EiU8OzUIfi9EPU6LA1oKe9cEOzlPyFsMb8P3hR-I5Tu5xVxH785ItOCMepRPQDgn73hSoFdkwyKVWiiPYYYoGYkUipcZzER1AcJfBKhZiy8TEl4rR38ditL9x0OciCzUAt0U9ZVC5v1VGtB2c_5Ya5ZEG87zbnEkfKZ4omXJ7UPY3OFucaxf69C0hsfwo_yA42s7PBAt_0YJJ4ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24822" target="_blank">📅 22:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24820">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pS0afjMHnduAkOmxKtqo0kve1jqDO-BG2-ZmKnc1kKaibF-9NvFqz9X7fRE8vAc3dQbzJtlecg2nPndSr4Rs8HtE7zj_6RSzF-agVUgo8XDAwf_MLZEM1ckiGeNVV1zh-T4eqoLzbYzJmNAVERcZB3tjPyiaLzp01mtokXkT8CyTZ_FNiUxZ8hhmT4HaUYJB9skuRxSyCwQSVHFTHODyz7vSAF0YgUIOZwlZe3rXjXtDho0AfQOCybW3_Xrre0UaNFpdNWltm17IiG3C8pgUvsAHCvyZStRm1ysaT5pXoXvfo_1LFlixX7dDSBKjJB9OoeNipmqSiXYK6mlnF7NOhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا 72 ساعت به‌باشگاه تراکتور فرصت داده تابه آفر مالی‌اوپاسخ بدهد. اگه‌پاسخ مثبت باشه ویرا بزودی بار دیگر به لیگ‌ایران بازخواهدگشت. همانطور که دیشب گفتیم قرارداد او با پرسپولیس فسخ شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24820" target="_blank">📅 22:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q518TrTUufKMfj0pta4YZHXEbrd6RaxnNqgXHqF35Z7ut0sdcsi9eYtN1l9Tug1xXE4uaevTln7BvLjMMRolp0v9lKushkGuhFOLEUoLBMIQ_-zywMKjfL7frbKkH8hd56aDIbRS0roWyWaDkWeSlrzNxEo9dKrKJnptfk7kSF4uyAeFDOMJSigwLJXk1tTobZnel0dAsQviBMvNhoJGeTqYLmhG9i682WKe7eJuGVf_GD0YOv7M2zbPxOmWkfHorduso-XDhIgOCiLrzc2EtufJ6iH8bKJT9N12uBV9ocVklASxmeST1ORs-ar6YPIB0snHiTFud505WpAwBIF4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
حجت کریمی مدیرعامل سابق استقلال امروز به عنوان مدیرعامل جدید باشگاه تراکتور منصوب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24819" target="_blank">📅 22:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9Jp32TaqmWdbwrijC-6Thj4GCw5tMu4nk-47hYsfZHzu9D1rqAV5jzNacuvLqZzAzQyEUAPBu4uKMqz71PE076XuW7QT8xLBEADoowMaErP44gDUf85Cl8tyqGf5OFo1zbEYKbJ94iWf59LbIeLmclnkkolMwaOlhw1c3s9dFPN_wH8rLZGhgFaGUop6ntnE026BhiG36QjXT4_i46cTbISsOxpC0Y1wtyn5dWNgfiO0pxKsfSF8iAYgQlC_G4IcCeGxP-IbpM2HXbD4ZwWJ9vnRvweNuDR2XGjJxdoSAS07oB606KUVcqxrgl17nIadgTulAe-Ken6ytROG-uFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugKGOLMpIOASD7hWUHHRrbnCzqCOlkfJ5MSn4Ql6Ew7iSNT1eJuAJ84jkxNv6wLKi0aNxvse91FsyEr9rW9zyMDPG-zQLoLp1qwXbCX6G3WCM5msfmuwR-lmaDkaL656N__rgISYSKgqgHrsCVBv7CoselNlWaCSvV8OSYAbtXoc7FiEI8gdh6r7STjhJYSoAX8NR2Q9qHNmoI-Zz4KKwF44Hgm-8y0FLLMCtrbEUdBco7gju7UCYYI0rIEDHZNO7l25Xn-3Uzrlp5WUMQr1BLTcLXGGaaPMYW9uO-IF6WDelfzx_hVfLId3TaN9R6getWntJYCLg6DZm42HUJ59Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLpZ7AhzTLYZ4tw9x_sZL9pzlTox9wdCecrxuQ9BTCH9q5w7fRS_2azdnIRZZ4n3FpG7wd9QQ2LsmS3bRzt2APGXRO_d0X3XPKXgo7UFn3X4xQhS70e44zFXQbvdz1yxnXGb9cLvsr0-JLvYdx6ziP3Z-c_IcQCvaiciMEsQN8khwAbaIh1SNZR0y8c9hRtdg0jsT4EehE6ogjELOdmq7MkfjuP_gkQCXO5pMC6jEKa7VyYGGXDLu2rO5S12L8fDHbFjKC_TV28oDs1mv1IsY1YzfKAcBsX8qfbcQ2WfgfbDP2pOj9ashOu2GBLlHrFwgtbjSByz4VIUtGcWO943VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YaabBeJ3-QZU9K6_x1MrwL4rTD8cIkHEaR96-k5QtQVjhHkeD4gXc2DKHaCLTvotzA56D8bOtcIYIfRbYWYq8R55UX9zf9dGQ8AUiqPfv95CNV5DU5PN6SzPW69iiOfiCSfbyxn_x56pp7NB5ole0v6eGmZhaeutEKdLc80RJyKbYWcjXHrjjN7bD54XJLYU6G68kJl80jICV7JuRBGHs9URxcTOO6VRnxeHo1Veo1DV_I98G6H9puWgEkN-g1moQuS9m_qIE79fj2_PJxTlYGGgCAe1ELkrcag3GIVkPkE5xB-aRTF0iPtLqK3fly7yWnt1gNTFUCvdzjmJ4Y95HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhOZwRgAD237k9JB5rB_0ESLFUCzI27U9RnQYBmATS2o-k_igX_4la61mAaoda7z84cg5jU7_JfGk9fqzhTxyChSu6gjHTQy9DskUR4TNlrBeq1wNO9LIyRAOqCAuO2-AVRsISalAfU1rfJXAxy7rwryJc9RWSNM2aczmAIR_hthta9MhqmKHF3Ik9_hizvuen2-XmmlsRKaAF97RUQpIX7D3ZoUKmJwmyrd4MflJYlqiTcmhbD1FOT8-tZ0yLV8_n7MV5GwD9z44-kTp1MtL7mORblapbjw-0bnjHRUc7EqY9vjaVqoQDfn1x3rId8gkWjQDEn4Wg9VN0Gu85fPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTemrAHHIKHE5EhIa_4eSPMwe_PubsbIR_Cy4RDVWcovjTiMv-8UdsMc_SEbiZZpqF_rjrbWDY8BPQOgidSaWUlnsgkUh81d24SVz0MkeoXDYDXwaS9vJGFHWzbvVFJISn3vzV9KutII0k9k5mhloUYP2VppDaJzyXMLXA96XHR-P6eih9sXQ_0iovjxkRND_po8-zuhhttN9dPau0wwxjSi4PW1q50OfGAcQfYH0TNWhVq6cd4c1KuJWcmxAZw--aZLsd25A8PtqLjlBrDotqn7CJwtnWBCmmI0ErbYQLH0aKbDeHkVknuLvKwTRVFL1lskC8LgPMPotNPtjTf94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xs9zxVbQxOsUNxJvH1yMxKyW_LiJSF3Ts_RXdyPdF2znjiduQQlhG3MzlDu4FAOJly6ZtfFkgZBIQIHEeDqsczE8o3arQd8y3fG7Wig6PRuD6SFr903bp0Nn70x89_F8w6PTHJRjY-U6gR0uooaPLAX_1oNumwU2GpuSPNiDWb2Bbfjrizu1-UGYlozXTQWaHcPOe5zEneFZ7pRNTg7dJHfw5AMiI1yQO_QYeqFcpmelZwm_zjY5Z4fQMUTKVq4QdRf38KSNz8efHJC6iNfOjuJUMVSyrWwBnbxd50SZVSkM2rMVm_PsUK3EYaF05tHfNurI_mxBw8cHRGqQEk9tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o9GpTKJa8_gwvSQU18IYI8OGRug6K75SUK3e8h2kAHMFaht7kKKk8pmSW9ZNUOHkXpygHlbzxM8GZbCyK3Ax9nk3zwLwK-iD9hvdhY6vBX8rIwHiOE3Zt7_h42tAYPrpGVznPYCPsyjDT135FW0kY7LsD6iEeRkOidhHIbAuWNqj4iLdpx-H243eC3665fO-U6p5qbPX4Q93kS3lTgk_AwfcQ2dyypg72-ZYwzU7GDNRCj_5VhpV5QUPtX-XbeZGuKn2rMpsjGN_DfgeTl89IYHYz8iu5b83556xMfnJlSBneEqg-4TRnV0dpLjRgWeht_Fbegf9knKRIc35Hy7Vog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXtB3G9SlvXDS5zoAjgKNvvl-qgW_eSRoRFfd0fAdBmhqAyrbAwgbiuUlzyMT2jZJ311wOoujYYXhWqN5-AlqOu4kkfXUpOq68pIfkCx4dfTQxURNgs7204poxh4aJyL8m-VnJZENFztTrq7gyUNiblt2wmSs50z6Ul-YO8ZBWOeXBXYmEDNaIUfnstWf_SbG5NpxBPZTMXB2YDa0g6Zn_7m-qmUtn27A9tnQXlv0tdruJFwGSuGyeB6EIdvCOdh9XKLkLH4GrSoSJ9nuo8m6jegvwebgGn1DMCkV6KHei08cIsfj0JarQSqYXhrsUo_FIhmOvdEKBLzTAdv9bW33w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bu8uAuzncWc-0Nql7SG84ICpuBwS0cSjqfCufE4DRcDNByiruRlljouDOylK8eP2E6Hksm_dIKSnNwsvUuonQne658XUIZqsBC1jZOX0I6UIM409508hxUR2ZcxxBlvpNQZ4U3nJxRQsGOhi66PlDvcmKbXqRhmKHoxI9WSYkhHs9cZgf9QviDtlp4YIAOZj1Ooa0wEvq2UqwDGEICXacMpq30IQ0fzEQvSq6-Zc0MYIlxM2LLOADrWsWrC4B2cJ7A-rww9NlJ_16ejQpPEO8GZzxH_txOH_u5XBKdkJp7pbILs_yx-uubc_SyDz4PsMDb4x7bgHQN0p90339rAAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qzJHXFaEYovscpsZD2sbWjvOTONsJ9wF1-4txHxUJt4IbjmuX_Op_CYiXpQ7e3YNLdzoCr4dObb38Yy68blEuv0OWI26c-sYanTX3Y3Ksvz4oS-3L9jxb3xDjxiUGehx887fqEpMR8rYh3kcgPn0CUsjEUr0KRcES_Y3A03Zk5rxRx4g7ya2xwOstLB3Se6O12vnoPytAKbb-8_xiQxutu_yhdCDqWJDHjmoHIVl9Cn-ai43z1Uhg5DH3aXsczR9MpGT72zabaI1UWeJbB26MpSOtSRrC5MpeYyxzomAbNCmbIKlAn2BT5neCoYu6PVdadvbP9uVv1Nv9kiP6MVMpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=Mz7PL_CFxGLbk2SYBfmWyQNLDkRAOZjmErAMm4ErKFjdbX8zipgxLFdbEGan76EsneYd4ObETK3lyw3mvKZB8jco_sYQg5uPa27880daUuMsElV_ZHNOd-XkC7Ro8l4WqixpFjFziM80JYJlcQ5k4MQUx5RORW8MTMn-tv5SYfj7V6Fih4TtSFsRGldedddPv7t4lf6uI_vubMyDa7vpEVDQY1AsexlYGu3mp9OEcsy2fl2G-HxVhl1lAmI3Wm2BRhY9gwweXGaq8BlD6IB_1a41X5EyM9GHMxWwpXfDV507RteR3H4g6w-EB3G7JxUKPhd_UNBKu6_MQmx5y4wmMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=Mz7PL_CFxGLbk2SYBfmWyQNLDkRAOZjmErAMm4ErKFjdbX8zipgxLFdbEGan76EsneYd4ObETK3lyw3mvKZB8jco_sYQg5uPa27880daUuMsElV_ZHNOd-XkC7Ro8l4WqixpFjFziM80JYJlcQ5k4MQUx5RORW8MTMn-tv5SYfj7V6Fih4TtSFsRGldedddPv7t4lf6uI_vubMyDa7vpEVDQY1AsexlYGu3mp9OEcsy2fl2G-HxVhl1lAmI3Wm2BRhY9gwweXGaq8BlD6IB_1a41X5EyM9GHMxWwpXfDV507RteR3H4g6w-EB3G7JxUKPhd_UNBKu6_MQmx5y4wmMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQNa0HdLtA6u4onmoZpjuUSFOpxviVitp79fC8pfg35jSqMweKmHCYkshUCSLnmtq9QUOOcDPQ6AYeAcXidlPhHwxQHQqBJhHIsdmLFh5TWSXl_Se1S42mdJ0r3EQpOsUDopSDWbPTHPCYyGgUJSvpVhfmd8UyTaL4WXgiB1iIUrvVzF5F3fuxpF89Ioi94g6Okhp8Ej-R3IdH9Ke3dtSY79aZNVeXIehXI7QpGbsTDtjS89lJ8mtqoYtXjYiG9V4Y8Kg3fGmhNmcEiOaQ72DCjXoTs1Yo1gCjJT__N5rVAPBsGznoIIOidfv_5aROCsTdMaawGbv1erlf3tGKExVQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=vz89Xc0HpGqqVLG-0pWT5QIJCznhFYiq0atJ5VZqV-aj1vmvwnUCLu1Y3wdYfV9GDf-Fi4h9Jo5KSIpAFGEffZEh1_eQ9faM105fXqpghkrxZRUZGTjJiTCOrvrY7FIFFNW4yVGPbuIcF8dLKgVhjYwvysA_b73C-e-4p8RRo9ePIATKaUfga1eyuCENuLgOqZNSCRVtQh8TWroUPCV8D6sYtdCaNO_Hm2G1nQjGnISmh7dVIAdeG2cg5o0CxBbcSzQ9ph7Wa5sww4c2oNAC_k9ikMU1zDdIWT-11_6u4E-CpN6-U7sK8mvU7IyVG8pJ4I4339lVW5kT7fN0bcoJ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=vz89Xc0HpGqqVLG-0pWT5QIJCznhFYiq0atJ5VZqV-aj1vmvwnUCLu1Y3wdYfV9GDf-Fi4h9Jo5KSIpAFGEffZEh1_eQ9faM105fXqpghkrxZRUZGTjJiTCOrvrY7FIFFNW4yVGPbuIcF8dLKgVhjYwvysA_b73C-e-4p8RRo9ePIATKaUfga1eyuCENuLgOqZNSCRVtQh8TWroUPCV8D6sYtdCaNO_Hm2G1nQjGnISmh7dVIAdeG2cg5o0CxBbcSzQ9ph7Wa5sww4c2oNAC_k9ikMU1zDdIWT-11_6u4E-CpN6-U7sK8mvU7IyVG8pJ4I4339lVW5kT7fN0bcoJ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hG4cEacC0zID19_iQY8rJ-veWDyJDUoAaxGRKxB8Trm0Kkj5Bf6cQlOFxUigEDkg1-gyTCMMpWmmxnSERZilErzT3sXYy-o17eNPJzAY3mtUEJMiRXEHr0S0V2euqHaNdNfYR4vhc8yNc7qaKegDB0cfKK0Be-CduqEtbeseY3CY17BjL7QQzX8TfxZJZgCy41qrbMQp0pSp0EzsYcrcikzgJbRXADoXdZKbOQWDUCytkE7HVy3UYlzGwvR0rhPPq9SDmyIPVK1AFRmLMxfI7buN0E49PW6krtEZDB28qfRABbl-ACt3BYqCI-vxKfNhG_v00NtQDiC_t2ePgUl3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #11</div>
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
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nmrS1amYRYgxGXANVCvBoeY603BCp_5AQiidKgjU5biHaycONFO8o1-Yw1N4bS9cs0v0xFmHmfPxngqSFmLn1L_8HyuSZAxTMfHral_ZjJvYnKM7q_pBrYrh_niuuuSZ7A5Lv_Vw0g4JG5FxRnBFDSVLk_lWlO4bLNbtiscmHvkg0YRvpc-Y62RlqiEC0ukGHrNtvsf_U7ZyN-ZLkuAa1tvoaUNiuqysp5X_ijDba9zIYZ7GpWovxIsCX1ARCC7qGbq6MxHWahwyPVwAAkkZ_IuGmnLaFSyTkV6YtC3K_klLDK9fGQHe8i5R0LaNNdl8wdTb3Ea2f4vL1Ls_Z5eumg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F7ZrW9NLBc5gAK3krbvY-1Udy3dcC1EcVvjI46oMYVPgXVUvZkycgxCkr8vuKxync0d2TVK6lV86TnFAo6YzHkQ8BW3CUBnlLwE-rhBunaJQRpiZ5cjyeaXnef5edEL6LCR36RN9MYLZzq9wKTKgPEfI003csxgzUOloWj7wtUwPMqliiuP_SW9JMsGN2cn58tX2F2bqaGqO6KIEOjsDxXgWsz7GAcvRKBm1JjDbnAWoyqZIl9ZfJviwXsZ9JV85aEq02TMgyu247ZoTKEZF3AoxsO2AGGjbvbLA8M8D7uVlfXl3OjJai4t9UaKI8EjuIcAroREgmNA0PcdmZFgQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nu8a0hxeyFRknhnvuLUdX9g_FSmiLTKsLPDKCl0RJH6ygqOCA4ZL_feou8GUoXiqlTZ6UmRoi16JLH95O8LljPW9mYuumley4__PxuKuceQScyAULau0GStoDGb0HIwCZ6EgrFvFiJWKLPo6R6CFwrNnp3hAE-ljGEI2BcuIiL2TAL4kk6WyGIlmELQiYUXdCjXz1YYywpW5n5X5R__nf9_n-O4ijSkAnh2R4e2gMeRRaexrpzvwiDlHO_egCBbmDexeZE-K9Ts1AFa3Y48GEUlg63ujhPkbyqcGapb6Znsg1UtqWK9qyMpxXkO_sfhYiguBOySNrwNW_CoCJM9X5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=b_EeiO4PaOCkb27xDzfF-6Mu1DWzHkXi6XK_Uoi7CCIpAY5a8F-O1z-vHyqLjgmFYDBrvV0Qhd_-ne9qby50Wz4Vb4B65LKv4ln0xSIQiyf_pSkEtS3Uvy1fbmsTsj2V2uzEJJRM7BMfdEd_Ee3bYRVV5zo0MCAsbTUbLNBOpJC3kaf0SzefdViuI_kScpL0RIxqlgbNgKXOAxdzrO1ALVKIA-ndd6R6SMOchvK7zj0Z9THb956Q_a4et5DK78Yr4m5pk5ZtyANmB5WVkE35KwNf_0I8knBAKaZrYEYL1HX_A6yNUn2we192as_--fEtY9Qdp7yrY4YmYcD_ZMLrCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=b_EeiO4PaOCkb27xDzfF-6Mu1DWzHkXi6XK_Uoi7CCIpAY5a8F-O1z-vHyqLjgmFYDBrvV0Qhd_-ne9qby50Wz4Vb4B65LKv4ln0xSIQiyf_pSkEtS3Uvy1fbmsTsj2V2uzEJJRM7BMfdEd_Ee3bYRVV5zo0MCAsbTUbLNBOpJC3kaf0SzefdViuI_kScpL0RIxqlgbNgKXOAxdzrO1ALVKIA-ndd6R6SMOchvK7zj0Z9THb956Q_a4et5DK78Yr4m5pk5ZtyANmB5WVkE35KwNf_0I8knBAKaZrYEYL1HX_A6yNUn2we192as_--fEtY9Qdp7yrY4YmYcD_ZMLrCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDCAd-g9VLecmzF3XbzjipCmTZe3MvBELmcgRmj_W0DGM9NoV2hy108ofmb0hOU98TMLXsBnMXBoPhVhv1tFjiRyN-ojacnCOt9f_gfltip9HG5i1WpPUz3ULWlVnMjRHf1hv59a_QEk7xyCz_WJ0sIK7wqP1hMNKjQQkV02eH1VCbMnNyf4MsLYAomwscU8nf5sHXAt2gvdgGJvO-tsLnQaeNAYUegYw8NcQfiwmPdH41pBZrj4z8lPSO9dh1bP5rBsLIghCsSvM_bBNyHD0eWGAVkQExjHW0ljJoxwFaa_NcU6bTdRSkLcQ-1IF4O57SUGvOsQ48D-bZga7Fg8_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bN65JuSBnuxLZM6DYkNNQ6V5cZuk0cAT3q7RSlWF7xc9YQ46bwtZNWkuW7PI1FIqQO1CKIcJEcsvTZBsVqKuTLPuD3UfO09fQOUzLVwGjwKtZyhXvBFo8ZLSEXtoIWj9RaI64O2GNGQsFbvr8gvaqzu2UcuJB3LwhuFdJ2wy-xu4ZJ03dEUOgaS72iPuxCCnEKRhrz8eeqVEda8VXiBc0SIUsCe5XT-TZ5YRji-yTKiEO8W77WKamb_w3pER3PxG8fz0MI8md43l4LhG8j-unevVm6I3CMgZ9ZkCnxz-VTcsyZ1nCV5GDZzwvTdySuatrdxgYx3OY_i1MafaFZgwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeKQJ93v6M08_3jpoLwwNI4qiJ3N1usA8aCkNteLBKqcqOOyuGIyp39_JdApcJrB9gfAEXwPsrrH9_9F54M0VwkzVacIPZu7PtWMoYGF5JRyQ4mid4zM5Z239f1PTxWE7di4pH74Bm3z_WovzpckUIFKLPzoKbX3xKQCTeSaZ_A94jL-FnkQzUhTC1usaI3V7Fm9O2WNkpgUhW_F9cjBk5JWdLOTY4WTurLI1UyUcVUkFanqJScuYi0SgJthI7OnOWD94kaDv5gA_d7G0Sg2wBj0uEjaoEs6KODbaD3BkK6deva2iuMSfO0djYTZAfueNpf0Jfm9Yp10gNuGvfGxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PM6veUEq7q9uSefrwfOLGYUY6g-yyEnztNZsAJRuE_GFesPujx-fj7mRy5IGaR3S64uBKbLcORqByawlhoSYEmGDYhbnKUBfsplS6U7DQE4xZ6I8m2V3bJie37BH94PZERy2BeBui7SQzq759Uyje6KZUXCEygEGx2neOVhCRWenDmfXTXtsyFETY5OpN9XfK5iunvIe8tr0hzLAfT9qQY09sK5nXy35nsGQsn1hlBx5VPVa3EqbLjFqPsZEpTYECTRdF--4a69tMr7PDcxvUQuBYo6JtuTj6-L4VgOA4OFUqCRfpgWqKbkjysG1i1yfSrFYwL0YiOaHTDA1SRGlxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCL3iKasnufl_3vwuG5i0LcYqZDecVMz12uk-3jVl_8q02p-aG4llm5lkPhWd0cUHV2glhSW1fcTGc2t_59JsdXXGHvChlKMO3whR08UG8MgwkDPDZEgZxMJ7yrRUCqeLmlzEDIXdlaJlkXE3CznnXHHochCV5XfMGr5EOgOLGxotbXuP-g6fJNQ39fN8r_pvwfz6vhM3XOfAzYX41XaO8bn55CYuAOp0iwmKjyoFdnHRz9INrLQjW6o0Vw2whB1RZC_3I5QD1yjIhdIZVdxSR9O5sv70AQ0GAaRGrGSzCQsutgcCArO2ox7609AOB8Q6HZw-QdVqD0a5Z0nbVyfFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn0xNucQk8ZYHEswUkSNz7ZHu8qCO2JzPd4y0XF-XCW7tEAv44ahZnnfYuoAZCQtQA9BQlqDSD783hp3Q_jxeCXGd7wp3xtJix9khbRAWRp2KaJ8aZ2RcSIPPcyZTjY3iLKfptkCi-OPW9f2g7LKqHEnUwR0wGwdfeFzArkUnWdIaVcCG_9or-L8N_4BIpFbAi5uIU-Zs0Nem8wpwgHqzVDZxWwrI2mobh8ZQCFUVnAOjvndF7m5_-8wzEAtaonluxQ3aDu1hCUngjMkmk44jrXUQKGJlied2VxiA7Lr0PH2Rb_vHFCZjJQSqBAbSKNAqhY5KADcYRKgRnM_XXjoVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
