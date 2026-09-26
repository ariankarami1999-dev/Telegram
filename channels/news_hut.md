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
<img src="https://cdn4.telesco.pe/file/RpR4JaSYs9wpQevFJYM07SrhxWbVTgyz9Pks-vcD1ZtZ2oBWduVIE93noecc2TFTDqTTB3h7-TdqKAh1LKEV1UAZixMSVklVZooeAZGrzv7N159Ikz12A7kmv79mIBJwgLTrCs_rSz0_76VHtR-P9TJb6uDcHqnchhGcqwsKtgm_pOMtN0txu_rbucEIP6wZIUpalWi29K14lOlVQt5VnGOD-L9Zvt1dqIKCNSFM-i0kF-eXPaN-q0-ts-zD7ZhaSq0qGlRvAeKwCt42VwTw7-I0gM20yvVBgtyjYmJptHKQRXF28kCmLMg518CpslA8pPkldvJkobjZcVBdbRq1Nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-04 20:48:23</div>
<hr>

<div class="tg-post" id="msg-72323">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9470296462.mp4?token=hIEF-9kjoJY6vwqLOpI3jgfiuGKgsvX4Mv5EHdnlLoKVT4yrltJsBHzHDOu1vlvx-QiSMJddrB9olJqroUEtmCPbgiJBOE00IPt3juCetOaja4Q0WTR5brjeNq39frCCyxNs-wADDP2_HCmIDzgs-cXUN3aeeMn_nn_WENUvXPCoaX0UrhwQ18bhP4bO3OW_vM9TVgjSIWb1r2DhayclpSlqf0V4_gkOoSvlnGRG9EBNpQKpH08BamrI-eZzM7qy5guvJB4UkdQZlfANwtkVKAFfftaMTxFMBJPyHkZB7n0tzzoofJwXDoqP1L4aSMgt76dFZdxJr7QVT8kp1fQESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9470296462.mp4?token=hIEF-9kjoJY6vwqLOpI3jgfiuGKgsvX4Mv5EHdnlLoKVT4yrltJsBHzHDOu1vlvx-QiSMJddrB9olJqroUEtmCPbgiJBOE00IPt3juCetOaja4Q0WTR5brjeNq39frCCyxNs-wADDP2_HCmIDzgs-cXUN3aeeMn_nn_WENUvXPCoaX0UrhwQ18bhP4bO3OW_vM9TVgjSIWb1r2DhayclpSlqf0V4_gkOoSvlnGRG9EBNpQKpH08BamrI-eZzM7qy5guvJB4UkdQZlfANwtkVKAFfftaMTxFMBJPyHkZB7n0tzzoofJwXDoqP1L4aSMgt76dFZdxJr7QVT8kp1fQESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تجمع عده‌ای در فرودگاه مهرآباد و شعار علیه پزشکیان و عراقچی
@News_Hut</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/news_hut/72323" target="_blank">📅 20:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72322">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=gsZVspe5EndsxTpJrI8-i55S4Zzz19_iMRoGs7WDCCkfP5xJ4nuCMooWIKGdGBGNLYR8Bbw7uE5kArscbv59Job1_GGWTO-PLjN7eryufY7xtYZLAkWnyLw_9fANdRfYvsjwp5kibQaRwDhUXRMXpRsYDcgB0PS5oKTdAr3LMryej38y0l_ubY3SkYfshUYjxlpPKG7jvD00DQDCe04fVjDQheg-b6B0IA-a3SLB_3cTCrXHk-VdARwbftQRtD_ZX-hdzK1oUZ7Vaf3b9Ms9BA4gxQVZVFI0JwJ1o_rsuafgjkrfD7zpUleynl1YrKnxCbcUGBTVkx6IjhxWTBvR2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f33229cec0.mp4?token=gsZVspe5EndsxTpJrI8-i55S4Zzz19_iMRoGs7WDCCkfP5xJ4nuCMooWIKGdGBGNLYR8Bbw7uE5kArscbv59Job1_GGWTO-PLjN7eryufY7xtYZLAkWnyLw_9fANdRfYvsjwp5kibQaRwDhUXRMXpRsYDcgB0PS5oKTdAr3LMryej38y0l_ubY3SkYfshUYjxlpPKG7jvD00DQDCe04fVjDQheg-b6B0IA-a3SLB_3cTCrXHk-VdARwbftQRtD_ZX-hdzK1oUZ7Vaf3b9Ms9BA4gxQVZVFI0JwJ1o_rsuafgjkrfD7zpUleynl1YrKnxCbcUGBTVkx6IjhxWTBvR2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ از پاسخ دادن به سوال خبرنگار درباره زمان آغاز جنگ خودداری کرد.
خبرنگار:
آیا پس از انتخابات میان‌دوره‌ای به ایران حمله خواهید کرد؟
ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که در آن بلافاصله تنگه را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/news_hut/72322" target="_blank">📅 19:28 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72321">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1e0c-XkPse7477ILIgTQOwTA3NF6LKsbPXH8O7D3kcLkFIvGCHTNfgOUl1VeaHvnceqvzV1S449tqGj-PiAZXTjDQEUH1J5l_O0uI4PUCyacpu65LREyj4q-D1QwM5KzZScF4jBxRbEq0NGIysBhbZwFuWKC13N3tdqo1tfn5iMKh9bDdfjcYd09j0RQmbPV9GSwXmNuaxrCMzguWsv4nhfgScWIscmfZjSImtbMzfbUnRNgFgIqynHkpdCtdimPj5MrxFrkbe7BeYfFliIDeW5qzc0mbOXCJf4sntZfrxZ34HHYdzitnrf6aODqIloWVrv6fz_pantaD4yO0Ne8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک هواپیمای ترابری نظامی آمریکایی(C-40 Clipper) که بر پایه Boeing 737-700C ساخته شده و عمدتاً در اختیار نیروی دریایی آمریکا (US Navy) است در بحرین فرود آمد. مأموریت اصلی آن جابه‌جایی پرسنل و محموله‌های لجستیکی است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/news_hut/72321" target="_blank">📅 19:16 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72320">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/72320" target="_blank">📅 19:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72319">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=mRdyusL5xwtgPK53CmkCFpB-PE7p-Wtm7npYQdJH_nYbIoFEQ4p5C0x7GBFEMRXm37qzx3Y6P_qE9vYbPptjpmJDQnv8vOF9li2eW5LDRW9aBbjQG6j9TgVRWpvNTzTvVBekZC942D6KwvhdEH_ytyw3pE2t1t_i_0LeWopTAuc-wpBx_eZRO9uFRX7XDF_agMOC_ShPgBWKPop9H_eiHI3dBDc3cWUlu7e1VWJGIy5KZ-isakyCXZS4OEpNlXGCMtewc2U_mozeumkdHGX99ncjjYCtUMe1Hm3lsUBm1nAArtkSNcGNi-ggRu0MSgLawh9X4ROjt9qat-Y9oXXl_w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2074b2f37f.mp4?token=mRdyusL5xwtgPK53CmkCFpB-PE7p-Wtm7npYQdJH_nYbIoFEQ4p5C0x7GBFEMRXm37qzx3Y6P_qE9vYbPptjpmJDQnv8vOF9li2eW5LDRW9aBbjQG6j9TgVRWpvNTzTvVBekZC942D6KwvhdEH_ytyw3pE2t1t_i_0LeWopTAuc-wpBx_eZRO9uFRX7XDF_agMOC_ShPgBWKPop9H_eiHI3dBDc3cWUlu7e1VWJGIy5KZ-isakyCXZS4OEpNlXGCMtewc2U_mozeumkdHGX99ncjjYCtUMe1Hm3lsUBm1nAArtkSNcGNi-ggRu0MSgLawh9X4ROjt9qat-Y9oXXl_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانوی گاثی که دریک براش هاپ هاپ کرد:
غذای مورد علاقه‌ام کباب کوبیده‌اس! بابای من ایرانیه و عاشق انواع کبابم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/news_hut/72319" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72318">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72318" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/news_hut/72318" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72317">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGloWVWGdSxmSgflBrKpShA5pOTuC-Xz9M0Y_UrMSCKa7Q1xGtGaXj18IpdYTUkiJUttzmU8BJQ1woowb-7auLBg5b0njGtEmYtpDVX4CNXGTXnbHtZ4mqHgfNJSAEBO3SNDhI6EbGI-MsI6iHGV_j4eOAbLprg5yCOLDWrulxjsin5wtBaRE0dkzCgr9sSt-Ls9fHWeB_zkRmD40qLEgDaTPZYMXt7X-0_J6NG4xDYOB41ND-Q8CKFaKVIzeevzziUavMeRruxly_eSY3ubt4UaILR-sMjMxW7yzFYRa8cjr83uninykWKPtjPhZ1LYlJ-yT97QTgxDbXSl43doxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/news_hut/72317" target="_blank">📅 18:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72316">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=RE1VoGZ34L9ujgsA2PIZIKF6DwDHCloV2A6-q8s_rPFbhczbiX1clDF4WQ_quHWDVARgty1m6pi6xeslbSdYeIbFik2xUCAYCm3VsJI2AQq4NFd959GJS5VgvE-9KUeRnI7RZaCf9YC-8XyTbPRrVFpma2ybLJZFT8OCAclmT8h9l5X19x3YFZ4KkrRfGvd7B2eP-xsIpqa2U0gL5iAkweRVmE-7ObpJS3pdS4CaBA6aKVgeWQ_3QU4B1-QIjVIoiEx-JAYlMOeZOPCHH_anJec0lhD6SQfNu1V1WKym1JlqBOMGpZ4p5_eyuTkhoHSBrnNrrb9Hlgqi321Aol1Z4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20a8e0532e.mp4?token=RE1VoGZ34L9ujgsA2PIZIKF6DwDHCloV2A6-q8s_rPFbhczbiX1clDF4WQ_quHWDVARgty1m6pi6xeslbSdYeIbFik2xUCAYCm3VsJI2AQq4NFd959GJS5VgvE-9KUeRnI7RZaCf9YC-8XyTbPRrVFpma2ybLJZFT8OCAclmT8h9l5X19x3YFZ4KkrRfGvd7B2eP-xsIpqa2U0gL5iAkweRVmE-7ObpJS3pdS4CaBA6aKVgeWQ_3QU4B1-QIjVIoiEx-JAYlMOeZOPCHH_anJec0lhD6SQfNu1V1WKym1JlqBOMGpZ4p5_eyuTkhoHSBrnNrrb9Hlgqi321Aol1Z4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مراد ویسی:
بعید میدونم مجتبی خامنه‌ای بیاد بیرون؛ بنظرم مجتبی خامنه‌ای تنها رهبریه که توی تونل رهبر شده،
توی تونل رهبریشو طی میکنه
و توی تونل رهبریش به پایان میرسه.
@News_Hut</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/news_hut/72316" target="_blank">📅 18:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-jOgj9ch_9NrEwR7udi1ig68g9DGWNXB1CJkgh0Pgv2hj5wye5S_lNEfWiBaJKTTDnBPTIYDl7I1wRdn5k2fFUpV74Gxmo_IhJ9xpI-RvxCW1HcKSL7tK1ddRlWrI2p9K_7F0uJA6KP70JZpYRtmx0NZUASW9xHiyXi_aqJUmch1XeGUhH_gLETKr9fx-4CEoXa6Th7e2qWErXXYlVT8B7bQgYEbEjtY4_1Q1yMvaWL5f8kThVH3rbEQ0sYHfr4JG4LVMhb_2xhSaKQFq5awHq4VQHvCzeR-T1wFpQB0OZEdJJQgnOqk9klEKO9-gTfjeurc5P9t5Yrk-nlt3cL67WY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9475808af6.mp4?token=HWEw7sn3Ie43Df9jaR3fLtu881zyPBOMu7zxY29_8yfM8rymnpyqX2e0fPyrEeADfFWBtcgsvqNLdEyOwyXXRHwsfXhJzOLr08RUiN0cqJjOa2uQqM84rLuDr9aX2HrswFPYWuygKb5d00W6nSmiqrTc6HcMbhOSDN811wm7HRgMpn5y5yEOzIKlMTZAFcfgsXtlk-jeSJNYLT77GFb9iZpkiJqKu0Z-DdYPoZa6Bi4-LWV9KgFvMDeMFMteMK6nM4UdMqeQwRfOsYO3aRzfu5qW68gsbfSxSGFFrthtGCKc35RYW6jjzS52kzn8acgwF40xUfRCpJPC5Kv8bBhC-jOgj9ch_9NrEwR7udi1ig68g9DGWNXB1CJkgh0Pgv2hj5wye5S_lNEfWiBaJKTTDnBPTIYDl7I1wRdn5k2fFUpV74Gxmo_IhJ9xpI-RvxCW1HcKSL7tK1ddRlWrI2p9K_7F0uJA6KP70JZpYRtmx0NZUASW9xHiyXi_aqJUmch1XeGUhH_gLETKr9fx-4CEoXa6Th7e2qWErXXYlVT8B7bQgYEbEjtY4_1Q1yMvaWL5f8kThVH3rbEQ0sYHfr4JG4LVMhb_2xhSaKQFq5awHq4VQHvCzeR-T1wFpQB0OZEdJJQgnOqk9klEKO9-gTfjeurc5P9t5Yrk-nlt3cL67WY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
کاری که آن‌ها می‌خواهند انجام دهند، باز کردن فوری تنگه هرمز است. می‌دانید چرا؟ چون دارند از پا درمی‌آیند. می‌دانید چرا دارند از پا درمی‌آیند؟ چون هیچ پولی عایدشان نمی‌شود.
آن‌ها درآمدشان را از طریق تنگه هرمز به دست می‌آورند؛ بنابراین با این کار، عملاً علیه منافع خودشان عمل کردند.
آن‌ها گفتند: «بیایید تنگه را ببندیم و برای دنیا مشکل ایجاد کنیم.» اما من وارد عمل شدم و ما بزرگ‌ترین محاصره تاریخ نظامی را برقرار کردیم؛ یک دیوار فولادی.
و حالا چه شده؟ آن‌ها دیگر پولی ندارند، چون می‌خواستند تنگه را ببندند.
و من گفتم: «بسیار خب. ما آن را به روی شما می‌بندیم، اما بقیه می‌توانند از آن استفاده کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/72315" target="_blank">📅 17:38 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8FpzGyrKwNP0JxhP75J87GcwM9tLG9j7CUjK8YfoYTyhtVHOa-eanZj-MVXCyfiDQwBLrEy4VmATNiY2CEzRDIDeyVWQwdGx-87CSONIDPzfuEjpXAZYsx2JypedDQwVRXf_gF8CJYsGtu_6v6x7y0f2k8BwqvuFk99LhJYHMC7r9ihyLFydeicYtl-sFTYTc1Tsqr5_K5HUBXXL-mRywrqaoYZsSleTkEsh9_yiyUe9-fzT6g1B1dh_YbDjhys15fcHLW7Nag6KTTRoEWVsz-uifeLSyD2JKmNiusOt5ugAB15Og92qJiQ-NLGUX5eYJ3r8atSailD0AJPVJZL6dBAKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6488dcc10a.mp4?token=EJV5-w6c7DdSxzPSsT0H5tBnBTBieP2UjN7sPYCSqm62GkrtRP2-MBjdzFKioUnLaDHu5N8Bxp-ijV1SxJRCo77gwgaoQYawgEA4eYTbKTjA5XlVXlMzZJvYiXLzGqHGBqQT3aHcnU10IEhD2jDshBoHSP7HVz4eVKyOlOkCTnPfuNhvIyNf9sVAoMB1_F2ZoqtakQIO-pE3TpRV8WyYjNNQf855AVCEUkEcBQGNtaoccnbDL3iTVpPA4rVQY9u-y110U_dZWPtx1A2ZeBAvIGO6DMMCerkh9cu8kqaVr6FgBdhsG-NqLcGyyKKe2VTTXAFoGpmNtP0Wn_O3zh8FpzGyrKwNP0JxhP75J87GcwM9tLG9j7CUjK8YfoYTyhtVHOa-eanZj-MVXCyfiDQwBLrEy4VmATNiY2CEzRDIDeyVWQwdGx-87CSONIDPzfuEjpXAZYsx2JypedDQwVRXf_gF8CJYsGtu_6v6x7y0f2k8BwqvuFk99LhJYHMC7r9ihyLFydeicYtl-sFTYTc1Tsqr5_K5HUBXXL-mRywrqaoYZsSleTkEsh9_yiyUe9-fzT6g1B1dh_YbDjhys15fcHLW7Nag6KTTRoEWVsz-uifeLSyD2JKmNiusOt5ugAB15Og92qJiQ-NLGUX5eYJ3r8atSailD0AJPVJZL6dBAKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ:
من توافق آن‌ها را رد می‌کنم. آن‌ها می‌خواهند توافقی کنند که طی آن فوراً تنگه هرمز را باز کنند، چون دارند به‌شدت متحمل شکست می‌شوند.
می‌دانید، شما این موضوع را در «اخبار جعلی» نمی‌خوانید یا نمی‌بینید؛ اما ما داریم با قدرت تمام پیروز می‌شویم.
ما کنترل کامل تنگه هرمز را در اختیار داریم. حجم عظیمی از نفت از تنگه هرمز عبور می‌کند؛ همین دیشب، ۲۹ کشتی از آنجا عبور کردند.
آن‌ها خواهان توافق هستند و به نظر من این اشکالی ندارد. من هم از توافق کردن استقبال می‌کنم، اما آن توافق [مدنظر آن‌ها] قابل‌قبول نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/news_hut/72314" target="_blank">📅 17:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72313">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=X4AtZJ1IbPmGHnR2ghnKrM_pdudBKYs9SbD1WA7D7IoAGGW1dPz3T9vJMctY0sJwzR7z13Bw7PO20t14cyN4WRPQwuWOISLSJ13sXTd7ARBhBlvXouHenY8WubkP_o4dwb7QqeYOVSbMzxnPxQgjmezR3zHNIn8Axq8CdgX-rm3UYujAzXK8p7M0MfzYmXXt3awCB_H01Ieq0cB4jQpfGJTJ1Ael8Mv8X6nsYX4896ngkO_vDKkrVjSAgS9w_zVSaQc8qjwkgygPuV6DjrA6JzJQyxjSp6omQm1E8zQjUKpN11sd3KJkgJSy4q6KA_bkUxiR7xGol_Jhg7w6POnYAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5297b02f7.mp4?token=X4AtZJ1IbPmGHnR2ghnKrM_pdudBKYs9SbD1WA7D7IoAGGW1dPz3T9vJMctY0sJwzR7z13Bw7PO20t14cyN4WRPQwuWOISLSJ13sXTd7ARBhBlvXouHenY8WubkP_o4dwb7QqeYOVSbMzxnPxQgjmezR3zHNIn8Axq8CdgX-rm3UYujAzXK8p7M0MfzYmXXt3awCB_H01Ieq0cB4jQpfGJTJ1Ael8Mv8X6nsYX4896ngkO_vDKkrVjSAgS9w_zVSaQc8qjwkgygPuV6DjrA6JzJQyxjSp6omQm1E8zQjUKpN11sd3KJkgJSy4q6KA_bkUxiR7xGol_Jhg7w6POnYAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره طرح هفت ماده ای ارائه شده توسط ایران:
آن‌ها پیشنهادی ارائه کردند، اما من آن را رد کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/72313" target="_blank">📅 17:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDlpGfEKIqyDCRJKU4cta6BtQwNPZACPICgoop0yQ9mYxcwcHhcXNxWm7vF3uIhOOjY6zzG1e39bQEEuwFdBqkCnXvEf-ZVxET4BMfDAWQ7YArwfTZ_1SCdKCaTTMTmBruq2h5KoZhMeyq0IP3pA1-AQq1pBI2r05zQ4vNxG89jBMoYOFcswwx-VkHP8TPncOZc3brMmJJgdk0AGNEariUGCWGqIU3ZN1owCtYGiPNyAMXWNeYI0aEVHe5Hlz827SxtwugHkYrHa6XMRHVpA5YnPhAZf6RX9cvBqVQFCDWJvwN3UociftbcfqFkr9v8UiNLxEmBDuuDckCvHrjIS6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ایران نمی‌تواند سلاح هسته‌ای داشته باشد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/72312" target="_blank">📅 17:09 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72311">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=d0D8Cd6jt5W_fz4xO_g_1MgZufIVsvDYjloHsNK-ql5RizvhzPsf4etkoaFPhCj8G41dxQJhTFwM-HXUN9qspJW6USeoEDfsP1p4oiwamIsjFXG4l-OXn56o9rRTAEDU2tSRVNe-VkOjyzgNOsoY023B3voB9iUHx0EfUGE5k3HGWYCbdpy8MRPH4LL3_CTONzMXW0n8LnjXLxlvI1JXr3EoxQB15RXenOwWSNadrYTExskxYXGAkFm2A84WY6Ye9mMB8dyIWCMvdBoJCRL9zh81lq8IFkKKaytPazMv_5HsAYj5IoLWYWR4IvMg3LNcpfZelSQL4l1fviq0IosJmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b70e110ec.mp4?token=d0D8Cd6jt5W_fz4xO_g_1MgZufIVsvDYjloHsNK-ql5RizvhzPsf4etkoaFPhCj8G41dxQJhTFwM-HXUN9qspJW6USeoEDfsP1p4oiwamIsjFXG4l-OXn56o9rRTAEDU2tSRVNe-VkOjyzgNOsoY023B3voB9iUHx0EfUGE5k3HGWYCbdpy8MRPH4LL3_CTONzMXW0n8LnjXLxlvI1JXr3EoxQB15RXenOwWSNadrYTExskxYXGAkFm2A84WY6Ye9mMB8dyIWCMvdBoJCRL9zh81lq8IFkKKaytPazMv_5HsAYj5IoLWYWR4IvMg3LNcpfZelSQL4l1fviq0IosJmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه عرزشی داره فخر میفروشه نسبت به بنزین مفتی که میگیره در حالی که بقیه مردم ایران و دنیا باید گرون تر بخرن
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/72311" target="_blank">📅 17:04 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72310">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/204024e85e.mp4?token=Vvo4s-oyajtR3ct6RhPNal-cKvbQnV82P_3IkznF_cF_hAoJEabwnJ7qYwQ1-mmajItlusFqp5igxvdgwIUG-j7LyG5xJWlEHGurn0CNJCEjCnAOfbJnf9SZy0IXbGlrYe-yIpTwDWrqwEaUE4akrmQ3FrpJBHtp3TRBfv7TMpVNGe7DL95Ca99bKJrNLdKMwgy7ELl8Rx4C8wMAyS4CnlITt-BXy1KFMHi1UnJHKRdenMmEMuPHxL1upLMCl-p9TIYoR3BB2YkYZ3-4D_tZq62RchfBvTFnXjZT_ApdOJUX9oNsn_IYlzwuFfQaLIi3QsdsaXeOLfV276_RuKzWug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/204024e85e.mp4?token=Vvo4s-oyajtR3ct6RhPNal-cKvbQnV82P_3IkznF_cF_hAoJEabwnJ7qYwQ1-mmajItlusFqp5igxvdgwIUG-j7LyG5xJWlEHGurn0CNJCEjCnAOfbJnf9SZy0IXbGlrYe-yIpTwDWrqwEaUE4akrmQ3FrpJBHtp3TRBfv7TMpVNGe7DL95Ca99bKJrNLdKMwgy7ELl8Rx4C8wMAyS4CnlITt-BXy1KFMHi1UnJHKRdenMmEMuPHxL1upLMCl-p9TIYoR3BB2YkYZ3-4D_tZq62RchfBvTFnXjZT_ApdOJUX9oNsn_IYlzwuFfQaLIi3QsdsaXeOLfV276_RuKzWug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه تعداد هم وطن به مناسبت شروع سال تحصیلی لوازم تحریر جدید گرفتن پخش کردن بین بچه های محلشون
@News_Hut</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/news_hut/72310" target="_blank">📅 16:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72309">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11382bd536.mp4?token=t5V9aoNG_gIfvolETmh6lCCCOunW1p6Y3IgDZORBP6OxZnZiT9TnfbFj9CU4DCZpHLx2G2KEGsXOTFfkYLTSjQL1QjY0NgiUXcWd9CvD8SfcB2JVaP58iZs21ldirm9MxHRAH20tM9YiQjh1bjdrGpQbK5_vMTVkCZaxTRCDGUXua7Y1kij6qGS3g8R42RSCtBLcq9rdrTXtMyXl6OpasTMjXgPOKiUQqm3NTaW9VWDEKwmttQ8NAE6Fzk0vHQKsp5e6vs9-ymOX4fExBQ-3YDqUa9MgI9vUIKuzXMpm6_sRE0n0YcpuFN3lrUswnFbn_N5HLcJJj7IBqPl3zp3Na442QAZvo497VNblR_jIHvV487NDl99UIiWUF0jH7j7g2yTXRnBKmTiop9E7PapikEo92v_6zDWQ1yv9QfleF09Utb495gL2d92z5-kPTrqLJFqoyiL1yaEjSnVtkMVqEVWXn5u93XYolEelrtungnQh6WRNmVjHut4I1G6v5hesyNYZO_x2K0vkiJlgxvz3qIGnUacvoNXPekMsQ_adAAAESu2fdwHMKl3AA29IR1ifqP78_0XueMO-STJBjQmV3bB8a1ZjOuoQ0dXTtLPCwNWdrb7m874Rs2GzmYCatXfqTU1AgksQSdMRb5Vp2Xh7LZaCh8prmlKGfwMiA0wfaYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11382bd536.mp4?token=t5V9aoNG_gIfvolETmh6lCCCOunW1p6Y3IgDZORBP6OxZnZiT9TnfbFj9CU4DCZpHLx2G2KEGsXOTFfkYLTSjQL1QjY0NgiUXcWd9CvD8SfcB2JVaP58iZs21ldirm9MxHRAH20tM9YiQjh1bjdrGpQbK5_vMTVkCZaxTRCDGUXua7Y1kij6qGS3g8R42RSCtBLcq9rdrTXtMyXl6OpasTMjXgPOKiUQqm3NTaW9VWDEKwmttQ8NAE6Fzk0vHQKsp5e6vs9-ymOX4fExBQ-3YDqUa9MgI9vUIKuzXMpm6_sRE0n0YcpuFN3lrUswnFbn_N5HLcJJj7IBqPl3zp3Na442QAZvo497VNblR_jIHvV487NDl99UIiWUF0jH7j7g2yTXRnBKmTiop9E7PapikEo92v_6zDWQ1yv9QfleF09Utb495gL2d92z5-kPTrqLJFqoyiL1yaEjSnVtkMVqEVWXn5u93XYolEelrtungnQh6WRNmVjHut4I1G6v5hesyNYZO_x2K0vkiJlgxvz3qIGnUacvoNXPekMsQ_adAAAESu2fdwHMKl3AA29IR1ifqP78_0XueMO-STJBjQmV3bB8a1ZjOuoQ0dXTtLPCwNWdrb7m874Rs2GzmYCatXfqTU1AgksQSdMRb5Vp2Xh7LZaCh8prmlKGfwMiA0wfaYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مقایسه ارزش برگ‌های اسکناس با یک برگ دستمال‌کاغذیِ دورانداختنی
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/72309" target="_blank">📅 16:05 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72308">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=A801Jabc1P6Zl19kBHfzzKlSS9flU3Y4B-p_q5B5cWGxu2fQ-WWF9AUcCdRL7CCzvW58_yytmEpHdB6nkfgzRlkmmkPVM7yISsAkdTya3nPvhtBkJlL29pf885zRkRfdTeRCGkwKK7p_I2sfv4K_11FI6itnwh_ICfVM0xvhhbjuViT5GfsxQOGVCDPeOJVtqOZ_GExBlAre9zOlJ0PFXmcTUTJ4Az7HqQnchvGSy3ZqcbE9OQ2BzwiZ397l06WP6nyCW5nPbW8JfdNwlAPUPF3whQ4cnGws723AY52VP5lF2vzwVTRN1eJ6Sr9U2k6kbjVyVnN8DvTlis4idtugDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d50ab7df03.mp4?token=A801Jabc1P6Zl19kBHfzzKlSS9flU3Y4B-p_q5B5cWGxu2fQ-WWF9AUcCdRL7CCzvW58_yytmEpHdB6nkfgzRlkmmkPVM7yISsAkdTya3nPvhtBkJlL29pf885zRkRfdTeRCGkwKK7p_I2sfv4K_11FI6itnwh_ICfVM0xvhhbjuViT5GfsxQOGVCDPeOJVtqOZ_GExBlAre9zOlJ0PFXmcTUTJ4Az7HqQnchvGSy3ZqcbE9OQ2BzwiZ397l06WP6nyCW5nPbW8JfdNwlAPUPF3whQ4cnGws723AY52VP5lF2vzwVTRN1eJ6Sr9U2k6kbjVyVnN8DvTlis4idtugDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضخامت رنگ کوییک اسباب بازی از تولیدی کارخونه بیشتره !
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72308" target="_blank">📅 15:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72306">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QaU522qNNNk5a9j6N1NAh_vXpmB-KoMJgtCvVbLk8uR36sgFLys0-Sa7H9-faw65YQTfOuk1tuPOH_tdriqVW0roEdgXOFAQnIgBZHibfYWUkSY2C-74UYzoYLXRdIHjE-3jkllquYU8KTNiF-565VWud_EceoyQ3yZH0QpcOvk9HkhbDmUhKLN3lu5sXQpPQj3xv5FhboikuriIneyknBPZ1ikTaJ879FGgWl3taBNywi8mkMD2P-M1ayaD0MwNtf2-FmuV55wXNgO_Nu-pN_PGIBNV3yhr4AqtYFNGDBHzJh0_V96n7jFuiFONJhpgRUR2Mh3yFKq0gD2VwvANWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=quOp5QVTlcA5maHnx6qmOYusSZwnozIcww6yJS8t4NSanR3Oyox1ChynlFuehkliBapZEZ4gJtQJY7LH_PDYnFwB-bLB6XQ0vDEeRcK053jWNAc7JI9OfCOwMwPduRfvi35QkM8WGKh-PpVZNGodXXNrPkddizL6_boXs79Bf4RpeME0eKuotHMIpZhkeZ588OviRy4l4KoiniR_ZgNiyVk1w2TZ_KLw6ExUeTEyzPYo8i7hGGrUrmg1xbPI4hGFUmOIarMBCTvz0okBT4DZgQhn355lzoewDTRS3buonQqvaGmpxaUjrVfQkI2Qq4Tflc2Do0Enk6492k2o1DgbaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d7c1c9217.mp4?token=quOp5QVTlcA5maHnx6qmOYusSZwnozIcww6yJS8t4NSanR3Oyox1ChynlFuehkliBapZEZ4gJtQJY7LH_PDYnFwB-bLB6XQ0vDEeRcK053jWNAc7JI9OfCOwMwPduRfvi35QkM8WGKh-PpVZNGodXXNrPkddizL6_boXs79Bf4RpeME0eKuotHMIpZhkeZ588OviRy4l4KoiniR_ZgNiyVk1w2TZ_KLw6ExUeTEyzPYo8i7hGGrUrmg1xbPI4hGFUmOIarMBCTvz0okBT4DZgQhn355lzoewDTRS3buonQqvaGmpxaUjrVfQkI2Qq4Tflc2Do0Enk6492k2o1DgbaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
ما زندانیان آمریکایی را آزاد کردیم اما آمریکا زیر قولش زد و پول‌های ما را آزاد نکرد
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/72306" target="_blank">📅 14:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72305">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اثر جدید ابی به یاد جان‌باختگان ۱۸ و ۱۹ دی
از او بگو به دنیا..
از او که قصه ای داشت او جشنِ زندگی بود..
سروی که قد برافراشت از اُجرتِ گلوله ..
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/72305" target="_blank">📅 14:27 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72304">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=V-zIkx5N1xwLob8DtmuEDx6rJIL2qJ-i0o-DCb4kZumUCRXGc6OBQ1m0eHEFGg9gFXSVR6ur2ZW9PSa_OBmnYlIRWD7CEG5QHQeOqDByacgZgbI3_a8v271i62wpRVpkLeQXnninP0muvJS5E-4bblm6vZbNe8xavyrbwij_NQb5s0JeQoyemFf05SdMS7gL5Tup7qi0QzCqVTHADbJULrj7i4_SrkY3UNXKgriG88t3SJD2vby7FaUbsa4MvfMh_-gIlJnzogTA0Eq0eXUFL53d21-TXmOBRiw6r8xGg_E8Lbv2-s7Tv05iqIqNfD1YUF-78YtG0AWyXGUxk-7YFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a59d978fb2.mp4?token=V-zIkx5N1xwLob8DtmuEDx6rJIL2qJ-i0o-DCb4kZumUCRXGc6OBQ1m0eHEFGg9gFXSVR6ur2ZW9PSa_OBmnYlIRWD7CEG5QHQeOqDByacgZgbI3_a8v271i62wpRVpkLeQXnninP0muvJS5E-4bblm6vZbNe8xavyrbwij_NQb5s0JeQoyemFf05SdMS7gL5Tup7qi0QzCqVTHADbJULrj7i4_SrkY3UNXKgriG88t3SJD2vby7FaUbsa4MvfMh_-gIlJnzogTA0Eq0eXUFL53d21-TXmOBRiw6r8xGg_E8Lbv2-s7Tv05iqIqNfD1YUF-78YtG0AWyXGUxk-7YFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ در پلتفرم ایکس منتشر کرده:
در این ویدیو تصاویری از انهدام یک لانچر سپاه دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72304" target="_blank">📅 13:53 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72303">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گزارش های تایید نشده از انفجار در نزدیکی جزیره خارگ/همچنین صدای انفجارهایی از سمت تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72303" target="_blank">📅 13:32 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72302">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc192b406.mp4?token=CfWvZJacwPP3BtdEyi64ZHQeiQwDaRxYCQuOspAAqaimXFjgIYlUfNRzx5__g328HdyasHhVfT9xYB1fkOYyk9zXlhPtwByR9rHzFeU932UrW4q7TeC4yTk2rFRCtvm_Y1zmaYdK4lMVfl_pbWt6GldjXFgC0NZgHqEYAryBmzcVriX-zTgRrYpUmKrEhFPhRpVh6p1p1s6xu2wuUXRSkdwbc01mEst6em-s1n4tZ41c2zBi6RLeErIoUF98K-t6XoOkB-zK_mBVdvo7wq78GOIY2oa1WR-jo7hUay8r_cOh7zTp3OF-m7kJNWApDLUm2PvhHlXCKIR-Pn2EZOU9qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc192b406.mp4?token=CfWvZJacwPP3BtdEyi64ZHQeiQwDaRxYCQuOspAAqaimXFjgIYlUfNRzx5__g328HdyasHhVfT9xYB1fkOYyk9zXlhPtwByR9rHzFeU932UrW4q7TeC4yTk2rFRCtvm_Y1zmaYdK4lMVfl_pbWt6GldjXFgC0NZgHqEYAryBmzcVriX-zTgRrYpUmKrEhFPhRpVh6p1p1s6xu2wuUXRSkdwbc01mEst6em-s1n4tZ41c2zBi6RLeErIoUF98K-t6XoOkB-zK_mBVdvo7wq78GOIY2oa1WR-jo7hUay8r_cOh7zTp3OF-m7kJNWApDLUm2PvhHlXCKIR-Pn2EZOU9qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی خراتیان کارشناس صداوسیما از نامه ای محرمانه که چند روز بعد از اعتراضات ۱۸و۱۹ دی از طرف جمهوری اسلامی برای دونالد ترامپ فرستاده شد می‌گوید :
ما از طریق سوئیسی‌ها، حدود دو سه روز بعد از حوادث ۱۸ و ۱۹ دی، نامه‌ای محرمانه برای ترامپ فرستادیم.
نامه به تقریر رهبر شهید بود و فکر می‌کنم آقای پزشکیان هم آن را امضا کرده بود.
متن نامه چند محور داشت و لحن آن بسیار جدی بود. در این نامه به ترامپ هشدار داده شده بود که اگر جنگ را آغاز کند، شرایط مثل گذشته نخواهد بود و ایران درخواست آتش‌بس را نخواهد پذیرفت.
تأکید شده بود که جنگ را به منطقه خواهیم کشاند، به پایگاه‌های آمریکا حملات بی‌سابقه خواهیم کرد، به نفت رحم نخواهیم کرد، مسیرهای انرژی را خواهیم بست و چه جنگ باشد و چه نباشد، به اسرائیل حمله خواهیم کرد.
رهبر شهید نیز در یکی از آخرین سخنرانی‌هایش تأکید کرده بود که این جنگ قطعاً به یک جنگ منطقه‌ای تبدیل خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72302" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72301">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72301" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/72301" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72300">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeJpz5aknrGc-wJ7yLxhaub6hFMUO1D6hU2UhBDxQdn0G0mGDIm9yYNdbcF1TeiNG_R4-fu_Ywa2XIF5Vw57In4rHNivTu6K7Sh2C2WkeS6NI1L8InbXCdtDpCxXiZAc_0p5h3Gn7DMpQcG2q_m-DqSKBAlJbDg-Czj8YVfDgKo9bPWY149_xTJ4aaF9qdo7Sk44EboWrIYZxl0t5xWnHJulkYMy_xavQJ_BwZkxi4NfRz5Vf9ejC6OFzuyDfVEx99_b0yHBw7q_ZUZijE6TjAXhdSJV8HffgukyyLRr8Sqt0SIuidLUig2C_VyQTYZ9ynCKFFw81s2G_I1Gj7D5aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز اسپانیا
🆚
انگلیس را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
اسپانیا: ۵ برد و ۹ گل زده
انگلیس: ۴ برد، ۱ شکست و ۱۴ گل زده
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/72300" target="_blank">📅 13:20 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72297">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iBlqXgLXwDG04YMzvhTKsL8cDMzhjLQ-5piGxVNX0jAxWzhdVmQdHJlQoPEGh6r5mE-quXGWY3yxKD3HxYy5NRz86OIDobUl-pnjJq0jIOgAsZSW2vbQ1DwH7JwUkQ1CXEwR89-ietuFmXcgoUhVWIRbU61n-eKVW3oseGTFeKvjkxXReCfsniocQnz586luYP-L7fhsdB6r_o6KA4MzdIAy0zl3RckuL_LqnZfWWytnDUAvD-Jwlzox4S_XG4B8mhcOFbkYNvotN7qBkClwuq0AGLS0HI_CcnDpRtMdysbb6HnloI5Z4v5qauykP49HPmYMTZX_kDbzXFA46pPhDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M592XQDsZoZZp4UKAGTgF59kFjVRoIVgEiq0kX8rK44Am67e4nkMNvmKi0wW8m0SGDiw7kUC69XoAqOu5zIHmKg3v0zrFwfm0eaoYS-5nKXVKAUvjaFh2Wfc-cBKGQKz9VGedByjtW8jbofY3jZjYbReK9EEcJgk72ejSpqkqKv8rXiSeEr3DiFjLi38k-vQb91DNW4O6d6qxykueG5tlEPgzPnD39E46pKAFeOZOOiUePfY00JUgWXX9fkoRnLZV6MCNtspEd_QOD9UkE6MP7DdUHen3kG4ijDcCV7pTjY5OeInzy-YaUPJr_TqHHVTfhXLlfOtOdmTVG-xl94fSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/exM4j0XS6wSrE442JzuVierrkPncziNc5puuwLvTviKQLkIZPf0EDN8PDVMHIW7CDBzsdqfe2TNdtY43rrg_2w6DHiKiRMY0zNzdmRfHSk-Ld9ljXSM1PJB4K1LwPf3iEo-Bv-bk-vKoqttueVLpz5pJ6MKB87VpzQ7KCNzxB9Tk8XXcIgLxoVaggaNTQRVJukOOtBaykOM3ekpc7q5evx35z2eUuOZwzL96Qpg0u5ANtyGj3PlqAkxQoHZjPA6eSB-QkSlK5n2wo0ZK3Dl6xS1qElcFQMYlj62kAZLXB4iwCAQIRBxIbIhAMFqpZqmHFdSiwvNJLjOkLH-a9Q-jZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سیرک جان فدایان ادامه دارد
ترامپ توسط جان فدایان دستگیر شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/72297" target="_blank">📅 12:59 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72296">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=q4MFZK6iVISTiyyZ4_fPbwoEqRDfqJxrkFMjs2y37q_DWxAvM-Y0kEKyd1roFbNqSugCEobz1FpKFyYlX2PQAsfkUJumoGzGNKw4EFQ0qxj_xirsNmcSv0KhJwgTahGDUPAFa6Byjl7lQBqo5F2yqK59ecIiy7Z9NPNmcyoclkmlhxWhZno8t9RAMZVkcNTQK59ASg-r4myt1PRJ2iEBKW54UfM7wMMsDLDVPV2TBCDTQPTaAgb5cgUJ6wnM5nf_Wjy4Q2MmKN7Jvap2IDJ9zbfVLw0W8607Ax49tT4pIhhvZ4vpL3AfRezr-ryeJ8wSHT0Woq9XRElLiiCV0CSXcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/748f1ed77f.mp4?token=q4MFZK6iVISTiyyZ4_fPbwoEqRDfqJxrkFMjs2y37q_DWxAvM-Y0kEKyd1roFbNqSugCEobz1FpKFyYlX2PQAsfkUJumoGzGNKw4EFQ0qxj_xirsNmcSv0KhJwgTahGDUPAFa6Byjl7lQBqo5F2yqK59ecIiy7Z9NPNmcyoclkmlhxWhZno8t9RAMZVkcNTQK59ASg-r4myt1PRJ2iEBKW54UfM7wMMsDLDVPV2TBCDTQPTaAgb5cgUJ6wnM5nf_Wjy4Q2MmKN7Jvap2IDJ9zbfVLw0W8607Ax49tT4pIhhvZ4vpL3AfRezr-ryeJ8wSHT0Woq9XRElLiiCV0CSXcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکر کارلسون گفت که پس از تلاش برای متقاعد کردن دونالد ترامپ جهت پرهیز از جنگ با ایران، او به وی چنین پاسخ داد:
«بله، حق با توست؛ اما در نهایت همه ما می‌میریم، پس [این موضوع] اهمیتی ندارد.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72296" target="_blank">📅 11:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72295">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=ool9ZYF5TdhFoAxc_xTiqv6_E5Finwlr3T_mX2zDHYwOy2zu3dP9RWsnsjBYn8dpzo2CtXOwDQDev7VSQg3G2AeVIfZ937IsIbZHD1KDnpZxOOrp0FK5q1pGJjS29JHWwnx3ZDc232UmU_IS_qvgwpVNzD-ULf-FnCHCO2LNuNOeSbNKIy18fKvqt288pqkGWWUesL-PqNqZG9Sm5p7VSDWYRApQ9-_JAOTMN6kFoP2sJ5RoPPkIBKF9JweLt-X-psz5eaDJJG1y6ZffNp1q6lgd1A-B4IBqDUmtVaLNEenVVX-ueHLCx81sYKLbf1L4Lbzv8oF_blnGxydkDAHWMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47aef3d95c.mp4?token=ool9ZYF5TdhFoAxc_xTiqv6_E5Finwlr3T_mX2zDHYwOy2zu3dP9RWsnsjBYn8dpzo2CtXOwDQDev7VSQg3G2AeVIfZ937IsIbZHD1KDnpZxOOrp0FK5q1pGJjS29JHWwnx3ZDc232UmU_IS_qvgwpVNzD-ULf-FnCHCO2LNuNOeSbNKIy18fKvqt288pqkGWWUesL-PqNqZG9Sm5p7VSDWYRApQ9-_JAOTMN6kFoP2sJ5RoPPkIBKF9JweLt-X-psz5eaDJJG1y6ZffNp1q6lgd1A-B4IBqDUmtVaLNEenVVX-ueHLCx81sYKLbf1L4Lbzv8oF_blnGxydkDAHWMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان درباره مجتبی خامنه‌ای:
مجتبی خامنه‌ای هیچ‌گونه مشکل یا چالش جسمانی خاص و مداومی ندارد.
در آخرین دیداری که بیش از هفت ساعت طول کشید، البته ما عادت نداشتیم که آن‌قدر طولانی‌مدت در حالت نشسته بمانیم.
ما زاویه و وضعیت نشستن خود را تغییر می‌دادیم، پاها را روی هم می‌انداختیم و کارهایی از این قبیل؛ اما قطعاً او از سلامت کافی برخوردار بود که بتواند پس از آن ساعات طولانی در آن وضعیت، بایستد.
از منظر پزشکی، او کاملاً سالم است. این را از زبان من به عنوان یک پزشک بشنوید و بپذیرید: او هیچ مشکلی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72295" target="_blank">📅 11:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72294">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=fNQ-BStKTluemc4d0cR7sbfIccF6GWvhyS0e2l6BROl8qwIYkrGxjT5xGBFXzMreu_OMOCZPYzMHv_zEgTu1tdAhX_nq_p2KIHYwaEs-s_VOihENa6QH8YyuN5-9-cdBtCYjLMsHrpM2nKfQMehkNMVgxUBAg5YfwJZ-4cqR_dIN_2O_bg_6GYach2HWc6XCF0jY4Szix98AUzuQsUTzF_f6RuQWnbQzA9b7VJJ9y2oEvOl7h3xeN5nDWf-xOgdjjNoqTrQkNqX8B_tAl5zMguLVH5v2dysmb0l4op9INDrJgn55ifu2MF9YaeRqOCaBnZCT56hm5scmC0wQ2jG-Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d63e3933a.mp4?token=fNQ-BStKTluemc4d0cR7sbfIccF6GWvhyS0e2l6BROl8qwIYkrGxjT5xGBFXzMreu_OMOCZPYzMHv_zEgTu1tdAhX_nq_p2KIHYwaEs-s_VOihENa6QH8YyuN5-9-cdBtCYjLMsHrpM2nKfQMehkNMVgxUBAg5YfwJZ-4cqR_dIN_2O_bg_6GYach2HWc6XCF0jY4Szix98AUzuQsUTzF_f6RuQWnbQzA9b7VJJ9y2oEvOl7h3xeN5nDWf-xOgdjjNoqTrQkNqX8B_tAl5zMguLVH5v2dysmb0l4op9INDrJgn55ifu2MF9YaeRqOCaBnZCT56hm5scmC0wQ2jG-Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا ایران بعد از امضای تفاهم‌نامه با آمریکا سه کشتی را زد و تنگه هرمز را بست؟
اینجا احمدی‌مقدم در حال توضیح دادن یکی از دلایل آن است:
نود میلیون بشکه نفت‌مان از محاصره خارج شد اما خریداری نشد.
چون ناگهان نفت زیادی عرضه شده بود، مشتری‌ها با قیمت‌های پایین می‌خواستند بخرند.
با بسته شدن تنگه، همان را با قیمت بالا فروختیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72294" target="_blank">📅 10:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72293">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMVwwwaLfgy6IRWGwKHD58jCW2ysJJ6yYtXeZxyI39lObZtmrIuZKZvn86xGi3vA8nkwUcoYnlLX8y3z_uXgZd1Vs0cDLe58b_MYG3P7fSlen64vWA1X9ztN4M930W535Yi7-JCHPuN750XL1nhMMP4wkpGrilPz-30cozA9jhnNi8FdW5pRoKitcB4rU2B8_XCTRsOBPAFCRg3sduO3xurAcKdVgEbPLli2VMxAWuG-ijwWbwOKvHi4RUda9V1Y1L8lYa5tpn7kJPMfJnT5JSCZoCFYsXsi3OqCXlrfneQ7oLHtYwWjNvi-lDW6DE_OkdEaD4TrLjlr9oVkaA3j0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وال‌استریت ژورنال:
به گفته مقامات آمریکایی، ترامپ پیشنهاد ایران برای برقراری آتش‌بس هفت‌روزه را رد کرده و اعلام داشته است که انتظار دارد پس از انتخابات میان‌دوره‌ای ماه نوامبر، بمباران ایران از سر گرفته شود.
پیشنهاد ایران شامل بازگشایی تنگه هرمز و ازسرگیری مذاکرات هسته‌ای در ازای لغو محاصره بنادر ایران و کاهش فشارهای اقتصادی از سوی آمریکا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72293" target="_blank">📅 10:35 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72292">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=OoMtEWyvkkZ43W7Vji3CWIh6eETg1wMmblg52xDPGRtRrP4XxVgfRrezwGCbr3KQ71_SK1E_YPlWHYNul1IkYoFsBGwi3F0WgPlaG2Hs7loiiCQhmM_xxTp3wP1Wtw-mcY57j1VT8yVRiEagCDeut7GCNrQz6uY0bds6FRDWUcdUdrV_0nDA_0VUv9XqIXI9ENc6kB5BEF2YisqLKqxsPlL6gwoQ67jC-gEfzeC7tX2cpg8xKFHYkNQEtZ9MnAxDNCQL-OKJvydG9meRZ282o9P6XoWxWTclyln-xmfslF0bPzCjqBfBgOu9Gh5sUECdhjtjdfxMTHfZgRXbH44g-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2ed2f431b.mp4?token=OoMtEWyvkkZ43W7Vji3CWIh6eETg1wMmblg52xDPGRtRrP4XxVgfRrezwGCbr3KQ71_SK1E_YPlWHYNul1IkYoFsBGwi3F0WgPlaG2Hs7loiiCQhmM_xxTp3wP1Wtw-mcY57j1VT8yVRiEagCDeut7GCNrQz6uY0bds6FRDWUcdUdrV_0nDA_0VUv9XqIXI9ENc6kB5BEF2YisqLKqxsPlL6gwoQ67jC-gEfzeC7tX2cpg8xKFHYkNQEtZ9MnAxDNCQL-OKJvydG9meRZ282o9P6XoWxWTclyln-xmfslF0bPzCjqBfBgOu9Gh5sUECdhjtjdfxMTHfZgRXbH44g-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رامبد جوان :
سانسورچی‌های صداوسیما واقعا مریض جنسی هستن
طوری که با سیبیل خانم تحریک میشدن. میگفتن سیبیل فلان مرد زنانه‌ست و تحریک کنندست.
یادمه توی یه سکانس یکی از بازیگرا میگفت «بیا بشین اینجا». میگفتن اگه یکی فقط صدا رو بشنوه ممکنه از «بشین اینجا» برداشت بدی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72292" target="_blank">📅 10:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72291">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=IXUQHbNSCxY7lxqd4-V-F_kPvS-4YR7y-7EsVKjNVzmIh69Nru5SNNNjNnG-SP_y1x1F_3JE-xB5Be4Aqqpetx72m_fyzmDM5Gnd4sckYWVbMJvraGL8ubysfQu8LYFljAbllKtgP4qRZphgFthGS1mZDhjphxvnkJXo-P-i8QaWJuh4KZGe5n_mi7-b-sZsHedeRp5hCNoqXLuADMK3oJ8mUZhx9zykA_06sBPZb5HnKRUQR5ziI4Y9XST55bELPFdpqR_CgGPNiSeh_ZVb4Kpbiz3wVT695HilBu33yBbLdKOFaXnDkSK7t_CE6y6h1_qanfaY_yOE3MJMafB63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2932ca5f.mp4?token=IXUQHbNSCxY7lxqd4-V-F_kPvS-4YR7y-7EsVKjNVzmIh69Nru5SNNNjNnG-SP_y1x1F_3JE-xB5Be4Aqqpetx72m_fyzmDM5Gnd4sckYWVbMJvraGL8ubysfQu8LYFljAbllKtgP4qRZphgFthGS1mZDhjphxvnkJXo-P-i8QaWJuh4KZGe5n_mi7-b-sZsHedeRp5hCNoqXLuADMK3oJ8mUZhx9zykA_06sBPZb5HnKRUQR5ziI4Y9XST55bELPFdpqR_CgGPNiSeh_ZVb4Kpbiz3wVT695HilBu33yBbLdKOFaXnDkSK7t_CE6y6h1_qanfaY_yOE3MJMafB63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:  @News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/72291" target="_blank">📅 09:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72290">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7db87608.mp4?token=dfA3_3w2oFliD53VnIVvRwoyPUO6GTCQAEn8g7GmpAtM4KSniOl-Hs9a--g6wdoMW77GCszOZiBSBlT6QKlrXEv9aaeImvqIZzaLrGIyi7Fd7eiFcdrovDikq1kZp4PIpMG_zPgb8pKYoAslawlj8I5Lnk25GQ2BB4k4kygVGh62bcZ0KJCunEd1wxVGekUYQx6ZUB7Hj7yyM7iSrw4QsP4ZrwyYHg8GrmNKZ3NngTTCAFJGQq0YCybfmpBOsIkcsqJNrw2iaU_sCgSeO99RXZPVXqHjIwRjqsdyaXyZBFS8_3ZUazMIObL0W6Br5k4w4hBWw84EfYcfwkZKf44Dwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7db87608.mp4?token=dfA3_3w2oFliD53VnIVvRwoyPUO6GTCQAEn8g7GmpAtM4KSniOl-Hs9a--g6wdoMW77GCszOZiBSBlT6QKlrXEv9aaeImvqIZzaLrGIyi7Fd7eiFcdrovDikq1kZp4PIpMG_zPgb8pKYoAslawlj8I5Lnk25GQ2BB4k4kygVGh62bcZ0KJCunEd1wxVGekUYQx6ZUB7Hj7yyM7iSrw4QsP4ZrwyYHg8GrmNKZ3NngTTCAFJGQq0YCybfmpBOsIkcsqJNrw2iaU_sCgSeO99RXZPVXqHjIwRjqsdyaXyZBFS8_3ZUazMIObL0W6Br5k4w4hBWw84EfYcfwkZKf44Dwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احسان کاظمیون فعال اینستاگرامی، یک هفته با یک پیج فیک دخترانه با پیمان اکبری، مجری سپاهی صداوسیما توی تله انداخته!
آخرش هم باهاش تماس تصویری می‌گیره و پیمان وقتی می‌بینه طرف پسره، خشکش می‌زنه
پیمان اکبری همون مجری حکومتی بود که بابت اعدام ها از اژه‌ای تشکر کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72290" target="_blank">📅 09:01 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72289">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72289" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBe
t
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72289" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72288">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-9MH0AtzBdScDv-jn_UQm9QGyhNIuXQ2gMYIYd9KgdhRjFQ1e3EOlRdKSU3Sm3grD3nqoXN1aIrrKzcuJZCVQZUCpGQYvT8vXpGkBP4-mdURauSVgDGuYxXEpWVph2JCXZ1apkbirk7B-Qle6EuIw-Hpfr6uyIrGNVwppxo-bODMgT4oCr3P6i4T9fCo5T8aH8_1QGNc1kQcn29hN5rVELcRZMpKGLgwO_GxtRMxz87O1wrA7C5W_jwDVg5sBkGa_aELgElpCsvDvQdU0W5lN43QabhSbk8HIPIt_1Qb7q8603SaoZjATYB7dy4aRXvaD7GeJl0I3clGMVaoT9JDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
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
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72288" target="_blank">📅 01:46 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72287">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Peu0lwctsQotAiI9QSZSpSns6HdTr1VFuaYDUNeiO1U7QcKX327jmmNdr4Y7ynJKGFoYpJZgiP2GMySFWM5DHEURL_U8P68Z1BS3x8dxkO1Yfyj494E3pjMfgRIlrkKxAC76Rl45BwT-FqlUAgtymEurJ8Gz3Jalbp3rRbuhoQFk0cBaj6oBAptUFOumngcHwHF0goBTpa80tvbuUyStR27LBuptuU5KVemmKteLPezsjxEi-b_AlCbpJ7w_69vzFrfkgY4Bmgn-06oap-U1M1KifITiZvnpDZVo7ZTi7dlg77zhEv1mi1SHI7NUGJtMbVN9y72slWQqMf9ftMUwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه توی ریاضیات و بخش توابع مشکل داشتین؛
این عکس به بهترین شکل تابع f(f(x)) رو نشون میده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72287" target="_blank">📅 01:15 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72286">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:   طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه. در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه. توپ در زمین آمریکاست.  @News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72286" target="_blank">📅 00:34 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72285">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=nxrdOz2uppmfe9Ewm-P-jgRG2zcqUxuzf3yMAh0wxhoggz4FyjrHaH-APkdywRSf3XlVLSk8tuycxXTcaJiHrKWKm-lFLDKB-fvj5KXI4HC8Xri1b0u-SLyjlkQZ2Nxo_L87N6qSGMT5_BJSa_D1EMu7RBSv0cKmQCwB7S3-9ANIVHbFhB7ggNf9DDdqS-Qx6gRz88yD311kdW8MyWDmRGaCSAo4TCm9BKtt4P-y7j9HIVHg3KduKTCitz0d9mEP-M6JBnM57yeZ5bwmxLohilGUa3h4CcDAPV4MCv6YQ2qFOcEin7SMBeq5QyI_q0FO35MIuU5YP1mzalf4zFaxgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbcfd0ec.mp4?token=nxrdOz2uppmfe9Ewm-P-jgRG2zcqUxuzf3yMAh0wxhoggz4FyjrHaH-APkdywRSf3XlVLSk8tuycxXTcaJiHrKWKm-lFLDKB-fvj5KXI4HC8Xri1b0u-SLyjlkQZ2Nxo_L87N6qSGMT5_BJSa_D1EMu7RBSv0cKmQCwB7S3-9ANIVHbFhB7ggNf9DDdqS-Qx6gRz88yD311kdW8MyWDmRGaCSAo4TCm9BKtt4P-y7j9HIVHg3KduKTCitz0d9mEP-M6JBnM57yeZ5bwmxLohilGUa3h4CcDAPV4MCv6YQ2qFOcEin7SMBeq5QyI_q0FO35MIuU5YP1mzalf4zFaxgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های عباس عراقچی در نیویورک:
طرح هفت روزه به طرف آمریکایی ارائه شده و اگه بپذیره شرایط رو از همین فردا شروع میشه.
در روز ششم تنگه هرمز باز میشه و روز هفتم هم گفتگو ها برای رسیدن به توافق نهایی آغاز میشه.
توپ در زمین آمریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72285" target="_blank">📅 00:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72284">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=Suyg3Vj8un1TdN5nNyAwzHFy6lu4R8osdv2kVFfpIuGguGokskOsyhBswbF37CSRRulxsf6O9PAfYNNWPr2Ov1OyB4-lBLjYjLQzeAUi4SwhMGEBct-ov_xzGFoBb0Oc7z83qSTDoz6t-T3DhBnFxYw0DqBCYekVYwIfUq3ge2ALna-EOwsy4c_DQKSKKYgLcT8d3HCHVOfqv1tcG33pHEjLPKd53RNz6hMgVhhmnZm3GyoAU8V016yyJcqw1cTYHsUsdPhj1REPBk6UIaGknyAzKPC_mYGhwgsLI1AMjr_lGkZAuhEYmOZn67eoIKXTC9T9c84K9jjIDjamKvIDaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55143aaecc.mp4?token=Suyg3Vj8un1TdN5nNyAwzHFy6lu4R8osdv2kVFfpIuGguGokskOsyhBswbF37CSRRulxsf6O9PAfYNNWPr2Ov1OyB4-lBLjYjLQzeAUi4SwhMGEBct-ov_xzGFoBb0Oc7z83qSTDoz6t-T3DhBnFxYw0DqBCYekVYwIfUq3ge2ALna-EOwsy4c_DQKSKKYgLcT8d3HCHVOfqv1tcG33pHEjLPKd53RNz6hMgVhhmnZm3GyoAU8V016yyJcqw1cTYHsUsdPhj1REPBk6UIaGknyAzKPC_mYGhwgsLI1AMjr_lGkZAuhEYmOZn67eoIKXTC9T9c84K9jjIDjamKvIDaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن جدید «بی-۲۱ رایدر» (B-21 Raider) ایالات متحده، پرواز آزمایشی خود را بر فراز کالیفرنیا انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72284" target="_blank">📅 23:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72283">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">خبرگزاری فارس به نقل از یک منبع آگاه ایرانی، گزارش‌های «اکسیوس» و «الجزیره» درباره دور جدید مذاکرات ایران و آمریکا را تکذیب کرد و مدعی شد که هدف اصلی این گزارش‌ها، تأثیرگذاری بر قیمت نفت و ایجاد ثبات در بازارهاست.
این منبع همچنین ادعای الجزیره مبنی بر اعزام کارشناسان فنی ایران به نیویورک برای شرکت در مذاکرات را رد و این گزارش‌ها را نادرست توصیف کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72283" target="_blank">📅 22:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72282">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eda15604.mp4?token=pAQFUAncovJtR-jNVHt-RCRwV1C9xKi7_7UHYK3pbHxpcWHH1nUoQpuEyqpeNTRjw0XCcSC2YbIshY3ZOLHj2NwLPZU3urfkRlfmCfXFa_bemFsEKvYMtDt0id6au6aVCKbKI9eFK-_2L0UIJ4zswcecHAwVHA7ByhB5i7Psar92iFiOFVSepo2IJLW3RyXL_zT9KzaMKmlIzkNGfWin2O9DbH3jwCjUMgOZjy_Suat3DdLVV0RX1a4G6O2LttvN8mqD5bbz5xUDaSn3nzCZa_ZFA7FVRpx1-LZ1w8UjtZpNv-4-wmTSXHt5eftZyKq_zkgx6zWcoeNttjHk_CazUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eda15604.mp4?token=pAQFUAncovJtR-jNVHt-RCRwV1C9xKi7_7UHYK3pbHxpcWHH1nUoQpuEyqpeNTRjw0XCcSC2YbIshY3ZOLHj2NwLPZU3urfkRlfmCfXFa_bemFsEKvYMtDt0id6au6aVCKbKI9eFK-_2L0UIJ4zswcecHAwVHA7ByhB5i7Psar92iFiOFVSepo2IJLW3RyXL_zT9KzaMKmlIzkNGfWin2O9DbH3jwCjUMgOZjy_Suat3DdLVV0RX1a4G6O2LttvN8mqD5bbz5xUDaSn3nzCZa_ZFA7FVRpx1-LZ1w8UjtZpNv-4-wmTSXHt5eftZyKq_zkgx6zWcoeNttjHk_CazUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید براتون سوال باشه چرا به یه جمع دخترونه میگن خانوادگی ولی به یه جمع پسرونه میگن مجردی:
دیروز ، رامسر به سمت جواهرده
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72282" target="_blank">📅 22:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72281">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=JzgXr13hXrd2xT4WC2uuAQfKvtN_adk6AqvsW2f4s4atiow7Im4g3sgNuntJ2_uE7w4VVRDbhPXd5FHt0gM9ebuR8iscZjN7RXr6z3-OsKP-ddBjbphtARvAhYBENImzVzO8EZcUEEaQ3x3GYeRj8GmoPMRONUWkncgPnqZJYHKoNTtmfSlCesQmy0Mb7JmwwFxJAH9fxHX_sVgk3tR2WiVPi3pVWUkVotZxKe_4qoMAcpvYmaXUIpnkD9JC5NYH271lHSDJaSzDOL_AGwi6fcFSR6wE0TyU8PVGDCjHcXlyofndZS7dMgb1op6NDXuQa8NQKr6sW6XlxD0_rxiSLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2600d0ba66.mp4?token=JzgXr13hXrd2xT4WC2uuAQfKvtN_adk6AqvsW2f4s4atiow7Im4g3sgNuntJ2_uE7w4VVRDbhPXd5FHt0gM9ebuR8iscZjN7RXr6z3-OsKP-ddBjbphtARvAhYBENImzVzO8EZcUEEaQ3x3GYeRj8GmoPMRONUWkncgPnqZJYHKoNTtmfSlCesQmy0Mb7JmwwFxJAH9fxHX_sVgk3tR2WiVPi3pVWUkVotZxKe_4qoMAcpvYmaXUIpnkD9JC5NYH271lHSDJaSzDOL_AGwi6fcFSR6wE0TyU8PVGDCjHcXlyofndZS7dMgb1op6NDXuQa8NQKr6sW6XlxD0_rxiSLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روسیه در حال اتخاذ تدابیری برای محافظت از پالایشگاه‌های نفت در برابر پهپادهای اوکراینی است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72281" target="_blank">📅 21:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72280">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یک مقام ارشد ایرانی به رویترز:
ایران حتی در صورت پذیرش پیشنهاد تهران برای بازگشایی تنگه هرمز از سوی آمریکا، هیچ‌گونه امتیازی در حوزه هسته‌ای نخواهد داد.
تنگه هرمز تا زمانی که شروط ایران برآورده نشود، بسته خواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72280" target="_blank">📅 20:56 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72279">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=DHZsYbbAGeVu3oqiC5T6VG8KIqLbNsiyshlOAA7dyYp-GhFPPDXgguMQzzu9UU-zkj8rE50760RwDJmZiEd5FW0zd-hKukL7VTzXZAsrz1h_MjBdD3aSm0LwHW21tTjJNGBbnRrqAgfYJ0X4Pi55hG2hpumgs-gKFnloE8Gv82MPdF9KVlDmublB-wr8eSsJcZgqSGAOoxVEmgyJhrK_rFbAGgSpdS3OaOt61NmozWk-IJl5ucigYwnleMcSXfjYRmeFxdRW3PtIN-1jlk-vsnO2_BdUO8OjBEHJLTDP2cIWS5SkDTKHMDLKhd0cXoFy76JFHmoGifyNvFTLKXFXGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb62dc836.mp4?token=DHZsYbbAGeVu3oqiC5T6VG8KIqLbNsiyshlOAA7dyYp-GhFPPDXgguMQzzu9UU-zkj8rE50760RwDJmZiEd5FW0zd-hKukL7VTzXZAsrz1h_MjBdD3aSm0LwHW21tTjJNGBbnRrqAgfYJ0X4Pi55hG2hpumgs-gKFnloE8Gv82MPdF9KVlDmublB-wr8eSsJcZgqSGAOoxVEmgyJhrK_rFbAGgSpdS3OaOt61NmozWk-IJl5ucigYwnleMcSXfjYRmeFxdRW3PtIN-1jlk-vsnO2_BdUO8OjBEHJLTDP2cIWS5SkDTKHMDLKhd0cXoFy76JFHmoGifyNvFTLKXFXGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بی‌بی نتانیاهو یه شوخی برا میلی رئیس جمهور آرژانتین کرد و اونم یهو زد زیر خنده
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72279" target="_blank">📅 20:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72278">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=Hr_-LyEevIH7Ox2_cRvRmb-yWLfcTrnO9olW4vU9PwHOnFXgUCGVFpep9gmoWaBCGKid1DMMuHPbi4AfRDo4ksTdBai_BnvnuL6NWXbgJsMXbmR6PFMi4zOkDkMp5p3dpkdGHWDSfmvVkgLeguZfjkCMLXHOKgw6xtSs2THgff6kXW5yEH625D5IduX7sBWUqrXmxo0EyAoDGyjRiLSgZDjlT1FtmHB4KCtm9Np5J-N0Wq1LccJ0_UhIdw2ypksFievggdycXhiLz99OVuzBBEXC51MreKp9UZ5CyBieFMWoHoSf40MwbjfA1jJ2gnNnKgw9MMngWhbnzbFrdJKHfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6656758c.mp4?token=Hr_-LyEevIH7Ox2_cRvRmb-yWLfcTrnO9olW4vU9PwHOnFXgUCGVFpep9gmoWaBCGKid1DMMuHPbi4AfRDo4ksTdBai_BnvnuL6NWXbgJsMXbmR6PFMi4zOkDkMp5p3dpkdGHWDSfmvVkgLeguZfjkCMLXHOKgw6xtSs2THgff6kXW5yEH625D5IduX7sBWUqrXmxo0EyAoDGyjRiLSgZDjlT1FtmHB4KCtm9Np5J-N0Wq1LccJ0_UhIdw2ypksFievggdycXhiLz99OVuzBBEXC51MreKp9UZ5CyBieFMWoHoSf40MwbjfA1jJ2gnNnKgw9MMngWhbnzbFrdJKHfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روزهای ۲۴ و ۲۵ سپتامبر (دیروز و امروز)، افزایش فعالیت‌های ترابری ایالات متحده در ارتباط با خاورمیانه مشاهده شد که شامل هواپیماهای ترابری و پشتیبانی آمریکا—مانند مدل‌های C-17، C-5M، C-130 و KC-135می‌شد...
تدارکاتی در جریان است!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72278" target="_blank">📅 19:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72277">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=Tpv1o5xJOjtYUH8ND3GscNVMfVDhqG41KXCq3xLe6RssGOLVf52j-IoWVppSp_Bd3Xz-T_pifxE5-uz4GlYpTAT51sbifQALGlF_EyW-DNkD18vp4Y2yMRhXsUibUQj8qsRdgsc_TKwX3WcCLv3OFKVjKssXyPA6Yejq1P0KfZnRhneKUvcw-KdFBUr2lI7S7-bBy8lyvn9NNU36dANrqGJQP9YfQVP5IZHq6cUsOYEc2y39WLF4IInnUQ6wuuX27qipLzo-bSp3_8YdBLT3TbPUJqnJzIu2L7-K1fH73LHEceT8J8QgBa6vTWjtOOmbEoq1BCzlKiqNp6CH-tINYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332f3ab7c2.mp4?token=Tpv1o5xJOjtYUH8ND3GscNVMfVDhqG41KXCq3xLe6RssGOLVf52j-IoWVppSp_Bd3Xz-T_pifxE5-uz4GlYpTAT51sbifQALGlF_EyW-DNkD18vp4Y2yMRhXsUibUQj8qsRdgsc_TKwX3WcCLv3OFKVjKssXyPA6Yejq1P0KfZnRhneKUvcw-KdFBUr2lI7S7-bBy8lyvn9NNU36dANrqGJQP9YfQVP5IZHq6cUsOYEc2y39WLF4IInnUQ6wuuX27qipLzo-bSp3_8YdBLT3TbPUJqnJzIu2L7-K1fH73LHEceT8J8QgBa6vTWjtOOmbEoq1BCzlKiqNp6CH-tINYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ به شی رئیس جمهور چین میگه عکس روی دیوارو ببین؛
ما خیلی برات احترام قائلیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72277" target="_blank">📅 18:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72276">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=UxYwSvhnBiB3T7Kax7bCDRJIrCjFPX3rs1QfBev0-I-ySrBsvzgsplf7AQIk-lz-SnmiIr1gqpS9fggfyHRb1Yzo6St9byUjxiIfKM7BxrgK6TDPl3z9Bue--vv_pz4IwVWKR5SEiHJoQwNZHp-nWuFcJgW7vXIGj82A-qRTKwmV4CWWG-pd_v-LZiS7FH4STv_lNT4i9ig8pNLI5DFK-ZRdAnByZJFWqTS0eHXmc9ZeZmqw7YaFJkQIIesp4R68K7Kc8VhspFBCfXvgbjOHmgOGPSKX3O5XrtOjitFg-Uu0gUQO08rnH3So1o2gCopXmgR70lN7SfE9HYN4GjlV_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f168bb0c29.mp4?token=UxYwSvhnBiB3T7Kax7bCDRJIrCjFPX3rs1QfBev0-I-ySrBsvzgsplf7AQIk-lz-SnmiIr1gqpS9fggfyHRb1Yzo6St9byUjxiIfKM7BxrgK6TDPl3z9Bue--vv_pz4IwVWKR5SEiHJoQwNZHp-nWuFcJgW7vXIGj82A-qRTKwmV4CWWG-pd_v-LZiS7FH4STv_lNT4i9ig8pNLI5DFK-ZRdAnByZJFWqTS0eHXmc9ZeZmqw7YaFJkQIIesp4R68K7Kc8VhspFBCfXvgbjOHmgOGPSKX3O5XrtOjitFg-Uu0gUQO08rnH3So1o2gCopXmgR70lN7SfE9HYN4GjlV_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده با این شرح:
مردی در مشهد با انداختن 100 میلیون از امام رضا شفای همسرش رو طلب کرد ولی همسرش شفا نگرفت و درگذشت و اونم برگشت تا 100 میلیون رو پس بگیره
😑
😑
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/72276" target="_blank">📅 18:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72275">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72275" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72275" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72274">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLdPaw_48Wmot_vx-0RUdkRAVwn250b9eriwe9dRcfaCL096LMLr5lN1Lmu4MGQ55WnGUSKUkytwi07a-1j__iU0mbLnv8WNHRaePqhfHPtcOG4xAvzKOrOIcjvCahRZF0R6PFcYEV0Iv1iPimOIy9vf_zr3HHM5937DD0kpu_n12YbC7at9iNErOikYomd58TVqWV06zegrgbqYH-IN8oEjGLuFYLnr81jOpxP4e92E9IOs0vlXAo4aR7cNCXxbEaIuKwrv8J7SvNbqq17UHiBHSy1QHcGMW9iMgULzOh37gwMkav4bkOVoXLSpSDkqjpaqgHcworWEsmHxYtLB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72274" target="_blank">📅 18:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72273">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=kKMyku3vILOzrLSgVQIPI_R6r6R46xFIGeMFkzK6tpiA5VymmBwgS2teSwiGbsHZ_xht92zmxQCOpV00QeCRKBNcfJfYunsPqii4OOqCETRHKh0KBqTGNxhPjiemfG6yZXbuJ4ZOzwNKsFdQMgthHxoKCFZ112wQIWfuSMHYUikvvK1ZO8MhMGbk9N0TZHykU2wl360a2v0bB3ev7nmYDVRvNQyXSiR37NhuRxEhSZxOKwpXPVF9nhVxJmiBAEdAqSogREem1p5LiTCum_OEuL65tFR9pYg5IrcOkvFaYFFshTqsaqEYyKIexghr_z_mFmkWyw9ei93T2Vv9cJlITw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9246e73cb.mp4?token=kKMyku3vILOzrLSgVQIPI_R6r6R46xFIGeMFkzK6tpiA5VymmBwgS2teSwiGbsHZ_xht92zmxQCOpV00QeCRKBNcfJfYunsPqii4OOqCETRHKh0KBqTGNxhPjiemfG6yZXbuJ4ZOzwNKsFdQMgthHxoKCFZ112wQIWfuSMHYUikvvK1ZO8MhMGbk9N0TZHykU2wl360a2v0bB3ev7nmYDVRvNQyXSiR37NhuRxEhSZxOKwpXPVF9nhVxJmiBAEdAqSogREem1p5LiTCum_OEuL65tFR9pYg5IrcOkvFaYFFshTqsaqEYyKIexghr_z_mFmkWyw9ei93T2Vv9cJlITw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی گسترده در یک کشتی حامل خودرو با پرچم یونان در شمال جزیره میکونوس
این کشتی ۲۹سرنشین و نزدیک به۲۰۰دستگاه کامیون و خودرو داشت
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72273" target="_blank">📅 17:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72272">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=JQkc7_wrhulndmc-hQgRcuJYAC1ZpYkGQ3FyCkGxJ97uF8LYP1hoVBn9JDTmSfpPqL96i0F6Elzw1d67Z6wAujC-U8nUBsgAB-hP6oxaP85CTOglCjb-M8oLtJaH-84b5l003euOo-5Ha9xLOErWRsE4dCameR_FZuSwNMu0N_xHqhbu1NsppJBp0kQd8xjjUUd5B_zCuf4yks1ywRDkeYOhIv9COYdmQS20MvOL-1y-J1v5xiWlsqkETWF4K-voe2Q6VrgGNbFgWC7HHmRAUnpESx1_xfE0UgZHNOz7M1A4Hc_NRzZIth5ZUF93GJQZ3Aoqkz196-rYs7WCMKwcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9af590b4.mp4?token=JQkc7_wrhulndmc-hQgRcuJYAC1ZpYkGQ3FyCkGxJ97uF8LYP1hoVBn9JDTmSfpPqL96i0F6Elzw1d67Z6wAujC-U8nUBsgAB-hP6oxaP85CTOglCjb-M8oLtJaH-84b5l003euOo-5Ha9xLOErWRsE4dCameR_FZuSwNMu0N_xHqhbu1NsppJBp0kQd8xjjUUd5B_zCuf4yks1ywRDkeYOhIv9COYdmQS20MvOL-1y-J1v5xiWlsqkETWF4K-voe2Q6VrgGNbFgWC7HHmRAUnpESx1_xfE0UgZHNOz7M1A4Hc_NRzZIth5ZUF93GJQZ3Aoqkz196-rYs7WCMKwcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیئت اسرائیلی در سازمان ملل اسامی کشور هایی رو که حین سخنرانی بنیامین نتانیاهو سالن رو ترک کردن یادداشت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72272" target="_blank">📅 17:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72271">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=NbRxk9NlDgi8AwvJYpwGbUrx2bedXKYVww1hobGRl-MQ4nDslL9gccjVB0sSGoWQCm8wh4iCG5WWK3IOPzenoQVt6vlThGQxp4Nddz4pZSgkN-GXYLHypvxMpJ82gRnwZGORXv38VkuP4CKv2S1sPT_VY6O_p-Dk_0ygKXDNKvRV03aPTGhYoIXmvs87u7rJkweuI-BQw9WLGCLywA9_p5kV4w2gfAs0yypkfq_vQgmXFf1SNvJcEJOBJpfmfxag8MG7z26MDs2s1HjvgdvTcEMoSKH0MuxoY9-jj5bERmStAI0bNRcGPPQp0EgWcRV4ULogFSvNwdtGX-szWKw6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327c73b8a8.mp4?token=NbRxk9NlDgi8AwvJYpwGbUrx2bedXKYVww1hobGRl-MQ4nDslL9gccjVB0sSGoWQCm8wh4iCG5WWK3IOPzenoQVt6vlThGQxp4Nddz4pZSgkN-GXYLHypvxMpJ82gRnwZGORXv38VkuP4CKv2S1sPT_VY6O_p-Dk_0ygKXDNKvRV03aPTGhYoIXmvs87u7rJkweuI-BQw9WLGCLywA9_p5kV4w2gfAs0yypkfq_vQgmXFf1SNvJcEJOBJpfmfxag8MG7z26MDs2s1HjvgdvTcEMoSKH0MuxoY9-jj5bERmStAI0bNRcGPPQp0EgWcRV4ULogFSvNwdtGX-szWKw6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پزشک کودکان : امروز تو تهران ی دختربچه ی ۴ ساله ی بسیار زیبارو آوردن پیشمون با خون ریزی شدید واژن، معاینش کردیم و کاملا مشخص بود بهش
تجاوز
شده، از پدرش پرسیدیم میگه با واژن افتاده رو جاروبرقی درصورتی که دروغ میگفت و مادر بچه وقتی رفته بود بیرون این کودکو با پدر کودک و دوست پدرکودک تنها گذاشته بود...
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72271" target="_blank">📅 16:32 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72268">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4pZXrfJ1ovcWt1EhtdsA4sviR00N4zBASv6jWONTfpQ1TCoivtSEP_97YCmD0H4rafdhkQKJEm8ej4g4xsNv9wawMvsGGD1HqO51R6ZB4lGu17LeXzsAUHMfega6rCdbyXSDiAoQ6GdlcPzZ1yCsYvgx6z1yltQwkaF_WLHy_6FztNOfM_7q6ywhAUjheSouI0SW7nAcdJM0IkOxMfe2C8JWuP14Kc88KsbtBAZqLA8zpNBuBIIOXU994VJK3-Zo2XchC_VX5ea2MVt2ipU8QvaWOqHrOUQEKe6f5PUqLp3dSEnk5wWKI_QDQgGwKBxQtQu3Z0Icey90oyxDBIenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=fcDUjJupK5jOlxSffGA4dgdA3QZAcFwdHPP8IlOLYy0kO5cYYfh0IrfJglunfB8dN04QOkcaWNobIX0KVCNmocqfZZ2I3sYrbxAABwMQyPZPkzKksR6gFuyVggIBK5E_qM_8eg-dg8MFr1GS0iS8qZvxtMtKq4FwylxmekdC_Af913HsHFVcMPj3ZTVs17J0DXCMhy4hm285bjIcZEkAk5Gb2-xOKG_mLatKN1A0oXkHE9pDxN-Kxyq-QzlIrEEdZh6p67PAdlOf_9IcJ2Q9JdZ8DyFRu7XVQfgasuy__i7Zme-E-FtQcBgzrlyRbcoivli6eCTJmSGQcYNruTsUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c33b2c3d47.mp4?token=fcDUjJupK5jOlxSffGA4dgdA3QZAcFwdHPP8IlOLYy0kO5cYYfh0IrfJglunfB8dN04QOkcaWNobIX0KVCNmocqfZZ2I3sYrbxAABwMQyPZPkzKksR6gFuyVggIBK5E_qM_8eg-dg8MFr1GS0iS8qZvxtMtKq4FwylxmekdC_Af913HsHFVcMPj3ZTVs17J0DXCMhy4hm285bjIcZEkAk5Gb2-xOKG_mLatKN1A0oXkHE9pDxN-Kxyq-QzlIrEEdZh6p67PAdlOf_9IcJ2Q9JdZ8DyFRu7XVQfgasuy__i7Zme-E-FtQcBgzrlyRbcoivli6eCTJmSGQcYNruTsUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپادهای اوکراینی به چندین تأسیسات صنعتی در روسیه، از جمله پالایشگاه نفت «پرم»، کارخانه «ایسکرا» در اولیانوفسک و تأسیسات «وورونژ‌سینتزکااوچوک» در وورونژ، حمله کردند.
پالایشگاه پرم که یکی از بزرگ‌ترین پالایشگاه‌های روسیه است، در پی این حمله دچار آتش‌سوزی در واحد فرآوری «AVT-5» شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/72268" target="_blank">📅 16:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72267">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ارتش اسرائیل اعلام کرد که یک موشک رهگیر به سمت یک «هدف هوایی مشکوک» که بر فراز جنوب لبنان (منطقه فعالیت نیروهای اسرائیلی) شناسایی شده بود، شلیک کرده است.
ارتش در حال بررسی این حادثه است. هیچ‌گونه آژیر هشداری در شمال اسرائیل به صدا درنیامد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72267" target="_blank">📅 15:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72266">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=NJ8P6sY_hAYZ1oxNVGSWeJqhVjluM3XfkkhAJRfdNz8TK5pUADT96pVrkY5Wii42-HvLtu37xKjtp0kukBzVipwsSi9znwsjC8cW7bZLvU4kvppiTSeWKqvmVSqvMP3xR2Zhs4ZzSd6rcDBh-pHVeOtGLFkbv8gHUo0g-OPbtTRvHXPvmlgHfY03nC3pF9HwVvS6aD_dDW3hvitvDTbkz7d4h4547W8ErPjZ5E8jWuYjR30JRAkhD50jDZt4sRu6jRFA6XX5G01sHpJiKHMxTLfWH_fLij6FcNTiIMNoOR--EatPU6IU2S1Rl72xY_YtKggYSfagD6XxjHhcK1muug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a4505de81.mp4?token=NJ8P6sY_hAYZ1oxNVGSWeJqhVjluM3XfkkhAJRfdNz8TK5pUADT96pVrkY5Wii42-HvLtu37xKjtp0kukBzVipwsSi9znwsjC8cW7bZLvU4kvppiTSeWKqvmVSqvMP3xR2Zhs4ZzSd6rcDBh-pHVeOtGLFkbv8gHUo0g-OPbtTRvHXPvmlgHfY03nC3pF9HwVvS6aD_dDW3hvitvDTbkz7d4h4547W8ErPjZ5E8jWuYjR30JRAkhD50jDZt4sRu6jRFA6XX5G01sHpJiKHMxTLfWH_fLij6FcNTiIMNoOR--EatPU6IU2S1Rl72xY_YtKggYSfagD6XxjHhcK1muug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار از پزشکیان پرسید که میخواید بمب اتم بسازید یا نه اونم میگه نهههه نههه اصلا،
بعد بهش میگه اگه بمب اتم نمیخواید چرا اورانیوم رو بردید زیر زمین ۶۰ درصد غنی کردید؟
گفت اونو که میخوایم رقیقش کنیم! یعنی غلیظ کردید که رقیق کنید؟! بمب نمیخواید بسازید؟!
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72266" target="_blank">📅 15:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72265">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPWUD4ADGtBmClvH4A0Nws15FOQmiMcO6ieLlQB2WzC0unNP_nTZa8akngk6VLnJB_VdZTE_vD4LRd_Cvqbztx0n4CnK4CtnWbJSxnWYD6joKkQNGPuXk69B4yyfrkGf8JnJyq6QsA4jKzHBjstPqb_kRxu7mIvX-snQQqva-J5k9596DymSY-4PEGxTaQ2gDUGYTxmTNLTVeXHFrcpzLCFiwdRkm8FOj-ATEWN_Js-Cg1PeZhFhOulU2Y6iXSRzZpg41cZh85CgiF2Kfxcb8MAcLdp2_ax36g-oqLjlu2AEyDu1I2qt1yjkcUrNkZFc2mP33OG3P2b0VNvGJYgWzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران طرح جدید ۷ روزه‌ای را برای پایان دادن به جنگ پیشنهاد می‌کند؛
به نقل از نیویورک تایمز و به واسطه وزیر امور خارجه ایران:
• توقف کامل تمامی خصومت‌ها، از جمله در لبنان
• آزادسازی بیش از ۱۲ میلیارد دلار از دارایی‌های مسدودشده ایران توسط ایالات متحده
• لغو تحریم‌های نفتی
• پایان محاصره دریایی توسط ایالات متحده
• روز هفتم: بازگشایی تنگه هرمز
• آغاز فوری مذاکرات هسته‌ای
عباس عراقچی، وزیر امور خارجه، این چارچوب را علناً تأیید کرد اما جزئیات تمام شرایط را بیان نکرد و اظهار داشت که این طرح تا حد زیادی مشابه توافق ماه ژوئن است.
نکته مهم اینکه او نگفته است که عبور از تنگه هرمز برای همیشه رایگان خواهد بود؛ در چارچوب توافق ماه ژوئن، امکان عبور رایگان برای مدت ۶۰ روز پیش‌بینی شده بود تا در این فاصله درباره نحوه مدیریت آتی آن مذاکره شود.
ایران اعلام کرده است که آمادگی دارد این طرح را حتی پیش از موافقت واشنگتن اجرایی کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72265" target="_blank">📅 14:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72264">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=NtyEuynRDb4o6HxcUokB5WDYigGxfgukV9gJ6vTSEhWsHose5O-Au9wqrBcql_43hp46iZSSyRl04A6USW8pC9g6snqzRFnwTndDqZEsnaNJgVK2tC2PZaJ-e_pRvAvA3IyszOJMCwV0GpLCWez3RJz3CnThns9QjwKYe_-svVdY45X27vimIcmn-OIHyLt1nWrF95SHTWHaZiH4Y4pENs9PFBWswKwQdQ9dKj0Z81gURyJhOs49sbA1MZDnvjLjnPrdYs7mE3sjUz0ggGLiQL7UFLHSNpOe3YGFxmxVtE0x3ouYVAl9lAFzXmESzYBPPIuKTPT49UYDYI9ILr4Z9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48620cfb1b.mp4?token=NtyEuynRDb4o6HxcUokB5WDYigGxfgukV9gJ6vTSEhWsHose5O-Au9wqrBcql_43hp46iZSSyRl04A6USW8pC9g6snqzRFnwTndDqZEsnaNJgVK2tC2PZaJ-e_pRvAvA3IyszOJMCwV0GpLCWez3RJz3CnThns9QjwKYe_-svVdY45X27vimIcmn-OIHyLt1nWrF95SHTWHaZiH4Y4pENs9PFBWswKwQdQ9dKj0Z81gURyJhOs49sbA1MZDnvjLjnPrdYs7mE3sjUz0ggGLiQL7UFLHSNpOe3YGFxmxVtE0x3ouYVAl9lAFzXmESzYBPPIuKTPT49UYDYI9ILr4Z9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: بزدلا صیکشونو بزنن تا شروع کنم #hjAly‌</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72264" target="_blank">📅 14:12 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72263">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وال استریت ژورنال:کشورهای حاشیه خلیج فارس در مورد تلاش‌ها برای از سرگیری مذاکرات ایالات متحده و ایران اختلاف نظر دارند.
عربستان سعودی و امارات متحده عربی از دولت ترامپ می‌خواهند که فشار اقتصادی و تحریم‌ها علیه تهران را حفظ کند، در حالی که قطر برای مذاکره، از جمله پیشنهاد توقف هفت روزه درگیری‌ها برای بازگشایی تنگه هرمز، تلاش می‌کند.
عربستان سعودی با اشاره به حملات به کشتیرانی خلیج فارس و اقدامات حوثی‌ها در یمن، استدلال می‌کند که ایران باید قبل از هرگونه توافقی با فشار بیشتری روبرو شود.
قطر و عمان از بازگشایی مرحله‌ای تنگه هرمز و یک راه حل دیپلماتیک حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72263" target="_blank">📅 13:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72259">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/M3DyDh9OBI7cAWK2rpmPqe4FIWinB9xYT2bigco0Pq7wfXpnR732eWiLTshYMH-dRtrnm3qcJIBLEQNaa1YzhLrpPCAmOCpQzl_f_abFB36IC75Ev76aX_zgENUAPUCFELXCtxUF4DAZY_-ptTJWeOz_c3zBuxfK8qZNWomA9cMC34b_G4pz5CIYs1yyDqSKI2Ni2OeDZYkGNEpALFB6P-oM63yTwr9dUwJt32_Sf18LrWiOSq4ahwQN8m-wxnPpDqXQxzpuQ-Hjg69M5Pm5nIbZm7P5grWEmVvZOFl3u9HpDxgy7VcM41djBAAF9JSH2h4G8aaSflBurkWyu_4WWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gmqolyDFKP1LSJoD2YpYW7vMgA2jfSVaBFzZZl_3OHdqcQ1HMKpWU1aCv3ZSY14xUTv5HszYIjVNQ03CPBmkUYhq-mKWEjIA5m5z21nxXcRG_BMQyBtNjdXVqz23m4YfEzWFMQ34ALEx0brHLR8L70Hzue9cTQqaWu_PHk_p1gMnAlHPs-rJGgbP-0Zvqfrm5cS-kqf_Cmy5yoBXiI4R0Vs2M_YQS8hcKeyxhoNsjPLvaXmzV8TC0E0tc6V8GtmnaKykUISzedc3z11QxY5xnmcC9QXO5uMgebEaHSDQpjB3SvswK38yu-44YmfKfS5nOHaGCuTScZ8aNi1_tVEqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/I3tJeE7dFBz03BgqXrNHbQrYx8L42_owRBb_GrM9FNK8KrAV0xRrMLJf8fm9fwSVgrm0joOg2vvlTKyvl_62RKbr2_xfVLbmF5rN3J-Jqo-COBA-rUQyYiSoMQYBTSFmETq2Rs8EpjiMYVhhn5eCk7HVQeq-fpMZEXB8o3IyrDl6vPp6OOEwuxkxR8OigC4T7LirNZjeWXFanOVYp5uQajA73cavBvLJ2uKVTwpBUouQNmCpFss43UeVLOKD_vERZl9sCSDW7V9vCAQMJkMWMUe139I74QpA1R9Cgu3SvaTqMVCDxeiOcdD3vE7qMWKAURJCXXGUpQ14VSkp9t5Kog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/iysLIBExSkL6mQR_gBDbu64XDhObOIRt2nFK4V7CvduR7huFmigdhDIAD-k6pfrA0uQMgARe8MeKmiea_KO1iArHCadjLGj_sejSLuUZ1CSvuWb2jVFCxQst5ezvsZbj8t-6BnsOUOMIP__bsQKaQwmWSGZcUQhMx6LJWbqWQ8icF0qt_855Fa2FxI3pgZ_3qSjrhxZ0G4taJ5LqOLBfmNEk9dfACO2Dyw-XZwPQufCyrgr6jHRellhwXWFnwiKeMaOWhDQIk-IfsD9HQtxXVI6cmMpL_rnZvCUnr-_zFthbwLzyknKLIOTEEZpOE4C-JSW6gmuauG7nAEk7e966AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گوگولی ترین دانش‌آموز امسال معرفی شد
این دختر کوچولو به اسم
گندم
لقب کوچولو و کیوت‌ترین دانش آموز امسال رو از طرف مردم کسب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72259" target="_blank">📅 12:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72258">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72258" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72258" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72257">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkvE7BHXzIrP2t0DNaS5b1A8tqBM4MK-FegQwp7tgeNkZ4c3fl8vKv7zAqvE9wszCPn1V4BOt9906zRB8LDfmudoKlZy2p3D9B7zb7IywD9NnBw29FH628W6WvkrvPbeIHj3cQbgVa7IY3p5rGL-4h-k8Qxa-i1SWkj9h3RcyvFsUeQykOOHsd0-QEwoE00Kgg3bRaoaQ_RKZhfGea-NGIuF-a0q17H9iMsXgecCL_xDA_WzDeVUeIUIazmafhPcSW5CTKAOpuKFq4r8d3DNjPWJ57vaI8ImR8n_AXHbeA_7mFAKIhTMjS3OBBrrmfB2fGjAliozGzHbp3RFIb3EyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72257" target="_blank">📅 12:58 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-d2haQXKzPTh60Isz5jA2cTU4HDgtfQ4Z07DtC_KKyxs-exmHK-1yolXvio3efXpg9ta02NNc9hxmYQ0m7aSVWQGPj8BxJS2j3Je55T06FaXopTsSYWGj9b_2BvhskiQaUIPlEm9O8yLDdPQPROD6qsddV1UA7acuZi3Ier5o9SRt11H0TtQtMuA2pkl-OUkCkFZ2nu3VwrNU3sYIiZmcIVAGOSpGjcom5ZUbGZZCAWx7wGigJaWXQEi20qIqQmyWsO5BvA_lyLpgSmfh-5_FUWLFBMg5Xhu2Xes5iSK788g3U-rw6ydypjC9RLY3t0-8Jn87x67dwUsR9spYNUzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویترز:
مذاکره‌کنندگان در حال بررسی توافقی مرحله‌ای هستند که بر اساس آن، تهران در ازای کاهش محاصره اقتصادی ایران توسط واشنگتن، تنگه هرمز را بازگشایی خواهد کرد.
این مذاکرات با مانعی بزرگ روبروست، زیرا هر دو طرف خواهان حفظ اهرم فشار خود هستند: ایالات متحده کنترل فشار ناشی از تحریم‌ها را در دست دارد و ایران کنترل دسترسی به یکی از مسیرهای حیاتی انرژی جهان را.
ممکن است ایران در ازای دریافت امتیازات اقتصادی، از درخواست خود برای دریافت حق ترانزیت صرف‌نظر کند، اما همچنان خواهان حفظ کنترل اجرایی بر این تنگه است. کشورهای حوزه خلیج فارس با هرگونه ترتیبی که به ایران اجازه دهد از تنگه هرمز به عنوان اهرم فشار استفاده کند، مخالف هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72256" target="_blank">📅 12:13 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72254">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQBUYYKMJFn6FQ2iCfbC9OOK6k7L-3H6ZPzWISRDMe1kcsCdz3ZxjSTG2ONMZoqHkNHlqQ19oP1zttQmDzb1aCbe6FbxHMTZL-Ikbm8R1HXdRM0mTSOLNBNwMrZuorL2764lBGLSaU09flhk82sJEwz3b3y75jpwlmXu2n8VS-FZQybzPk1kK_5mvTa3Ztpdo1j9iBR9LftuDUjqR1AqjwmsfAi3k8d1G9GwE1Tkl7Ergp0sBKb7RpiA3Dff2U0caE-mAzEzMT_j8iF0kLUEI4qknGEVw2FWhQoGrzrr3EfhBVj-1u9IaCDMreeZcSqx_o8bUDiXQfY4PAZqXGuBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=rriyW6RO7sZNAuHvYpoTUgTWD_Pi8S6z6fDxJKu_DHgYIfAFb7yOXz4akJA253UWLr2W0mcBxJkmCzKuAjLRYiEHOWn2qFtywjPBB4FMNJKRzx5k2UIag2zKtqqLju7cqvHCJtkGafkgQ1NdhsC201gEEumfO9_jPOJq5GVsqrFrfOVEUPLFRixGiUujdXOoRMMPi8zYEFABaQEMI0Kf1QnPyVbNir9UVE3voMx5XIAxHUF3sCsqpFtVmBvM10nmR-zcyRsIdFPtVKtgXxUNQ6BWOkcH3sI7fVD-1ruukquwLy6twhtyoM3mbaX0s6jQMwQ6uoUnSugyvQYkyiaVUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b32e956f.mp4?token=rriyW6RO7sZNAuHvYpoTUgTWD_Pi8S6z6fDxJKu_DHgYIfAFb7yOXz4akJA253UWLr2W0mcBxJkmCzKuAjLRYiEHOWn2qFtywjPBB4FMNJKRzx5k2UIag2zKtqqLju7cqvHCJtkGafkgQ1NdhsC201gEEumfO9_jPOJq5GVsqrFrfOVEUPLFRixGiUujdXOoRMMPi8zYEFABaQEMI0Kf1QnPyVbNir9UVE3voMx5XIAxHUF3sCsqpFtVmBvM10nmR-zcyRsIdFPtVKtgXxUNQ6BWOkcH3sI7fVD-1ruukquwLy6twhtyoM3mbaX0s6jQMwQ6uoUnSugyvQYkyiaVUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نایا:مقام‌های فرودگاه مانع سوار شدن مسافران به پرواز شرکت هواپیمایی معراج ایران از نجف به مشهد شدند. این هواپیما بدون مسافر در حال بازگشت است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72254" target="_blank">📅 11:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72253">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=g_Q9jpIzJ1lu5aloiYzqu8y0cU7zf94vaEfwIe1fClQxR0Ct9iMZsmbKquzeNRmI4JAXc7f4Ae5JD-yZVK8ks9ERaRIliVyCp7LkZilARbN6qaHJrDvptL_PeYHD2r4XhREvTxTAsGagektltKXldIJ1WbRhWi3nysvH0CkD6jNYwjBfdH-L1WC3OIGbN4tnCTJtVxchlYgFju9YLonEBw78XkI80rAUuAIryiEXg4kTHwfdCT2bRTRe4AGLdfBTQgrdxAdMpmgSE1LGE1dnjNFlihr13x4QiUJGJX4hhtS1sDYCvHkfn_15Xi9Jl-18zjhDRCQF0Np9OE6ZL7oWtZEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0cef4a4e.mp4?token=g_Q9jpIzJ1lu5aloiYzqu8y0cU7zf94vaEfwIe1fClQxR0Ct9iMZsmbKquzeNRmI4JAXc7f4Ae5JD-yZVK8ks9ERaRIliVyCp7LkZilARbN6qaHJrDvptL_PeYHD2r4XhREvTxTAsGagektltKXldIJ1WbRhWi3nysvH0CkD6jNYwjBfdH-L1WC3OIGbN4tnCTJtVxchlYgFju9YLonEBw78XkI80rAUuAIryiEXg4kTHwfdCT2bRTRe4AGLdfBTQgrdxAdMpmgSE1LGE1dnjNFlihr13x4QiUJGJX4hhtS1sDYCvHkfn_15Xi9Jl-18zjhDRCQF0Np9OE6ZL7oWtZEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های یکی از خبرنگارای رسانه های فارسی خارج از کشور با معاون عراقچی، کاظم غریب آبادی:
خبرنگار:
ترامپ‌ گفته میخواد جمهوری اسلامی رو نابود کنه ولی هنوز به توافق فرصت داده، فکر میکنید چقدر فرصت دارید؟
غریب آبادی:
ما با رسانه های فارسی زبان خارج از کشور که موافق مردم کشورشون نیستن مصاحبه نمیکنیم
خبرنگار:
ولی با ⁦CNN⁩ رسانه ی آمریکایی که رهبرتونو کشته مصاحبه میکنید
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72253" target="_blank">📅 10:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72252">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=Vvek21-L9cPYVirQAGU-dXXTghYXhn92Vp-5ZS5a9VOPX83AMmT4Wfkv_2UthxjUg9eOEW3VO-0o6kPkNz2dAQsmYOH4XEQhpJFlKfAJq3p1aZyKpPHYaPDHSKwkuK0bpnwlgC_BbaLPAJsy7IAl5Xe5D05anzx0oWbHeAO-HEWYecdRvrsv-k_H8y7KZ4yhBjaHJMpBlVsNLWrNm1ChpG8XIkwqkeHZuIyVwJISZTmBNN82cY9vEuALw9Qf6Ct33Ki6XHcwaFQUj0NUy0AoxhkB-XjxF-_gy5uehJqSPd6fbxfDvAAt1m5ZG0owXkBFWyeclx_1TSNrtQ4-EOhhiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69869e4eaa.mp4?token=Vvek21-L9cPYVirQAGU-dXXTghYXhn92Vp-5ZS5a9VOPX83AMmT4Wfkv_2UthxjUg9eOEW3VO-0o6kPkNz2dAQsmYOH4XEQhpJFlKfAJq3p1aZyKpPHYaPDHSKwkuK0bpnwlgC_BbaLPAJsy7IAl5Xe5D05anzx0oWbHeAO-HEWYecdRvrsv-k_H8y7KZ4yhBjaHJMpBlVsNLWrNm1ChpG8XIkwqkeHZuIyVwJISZTmBNN82cY9vEuALw9Qf6Ct33Ki6XHcwaFQUj0NUy0AoxhkB-XjxF-_gy5uehJqSPd6fbxfDvAAt1m5ZG0owXkBFWyeclx_1TSNrtQ4-EOhhiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس سنا با ۵۰ رأی مخالف در برابر ۴۹ رأی موافق، قطعنامه‌ای را که هدف آن محدود کردن اختیارات جنگی ترامپ در قبال ایران بود، رد کرد.
چهار جمهوری‌خواه — شامل سوزان کالینز، لیزا مورکوفسکی، رند پال و تام تیلیس — در حمایت از این قطعنامه با دموکرات‌ها همراه شدند، در حالی که جان فترمن تنها دموکراتی بود که با آن مخالفت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72252" target="_blank">📅 10:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72251">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWg5FxhSJAQ08kJXxJgyCS1aKfnP77cwL6zlK59FG6V213EGb6Pivo9lr1nBaKo0gVuTt0w5UGMephvHYcNuJswq4CzDnioLOuU-voR9rDlGvVfieJn5EyZtQpjybIUjQyYBD5hmmD9q17_ksvMU8hz89fv8SavBEySbbnQ7JCX79ZJ_oVw5xVgKZYoW1nhci5G4_nMGjtfZqX60Nceyk8yzSEkM8pUi63GP-2UGSsLOrEClxtaoL8mVfU0nSXEijOnY9eKdKf7EdWzme9ibXHGdeHuaVKivlRqXptNH12obnFfcRwALnBSZuZCyAyE9OKmispkk9ucU7ldCFUq57Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ان‌بی‌سی‌ نیوز:
مسعود پزشکیان، رئیس‌جمهور ایران، اظهار داشت که تهران خواهان احیای توافق آتش‌بس خود با ایالات متحده پیش از انتخابات میان‌دوره‌ای ماه نوامبر است.
پزشکیان گفت: «ما نمی‌خواهیم کار به انتخابات میان‌دوره‌ای بکشد. ما خواهان آن هستیم که آمریکایی‌ها پیش از انتخابات میان‌دوره‌ای به تفاهم‌نامه بازگردند.»
پزشکیان همچنین اعلام کرد که ایران برای بازرسی از تأسیسات هسته‌ای خود «آمادگی دارد» و هرگونه تلاش برای ترور ترامپ یا خانواده‌اش را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72251" target="_blank">📅 09:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ویدیوی کامل سخنرانی بنیامین نتانیاهو نخست وزیر اسرائیل در مجمع عمومی سازمان ملل به زیرنویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72250" target="_blank">📅 09:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=cYjTfyfKcOHOBisCx_YAS0Fs75GNqJENpfELtdkKZOIqMV2mZAxADFyYR3OwY4zDUwbSTkQBEoquR4I9g2XiTQ9udv8RGpCl70fxOBN6YxeWbSJCS_qalSxinF_ScV1Nz7FPnEDido4ky3VSI2Aw5JFHw-m2yiQQas6nu8vNdYhAPAxvHA-jlrGCw0avp6Svc8PUZH8hJtAwKSh6RIiwIGwkqrOOJ6RN4LPASFptem2cVCNn692UtcMXNkelNPHIWEa6XAqq1tHJKm0kkS4bhIhEmxPnYLmnAKDuTirdXtG0m5_D9fgsXUzWEoIPgFehl_6lg3pURDVLF61cWCDOWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae3b513eed.mp4?token=cYjTfyfKcOHOBisCx_YAS0Fs75GNqJENpfELtdkKZOIqMV2mZAxADFyYR3OwY4zDUwbSTkQBEoquR4I9g2XiTQ9udv8RGpCl70fxOBN6YxeWbSJCS_qalSxinF_ScV1Nz7FPnEDido4ky3VSI2Aw5JFHw-m2yiQQas6nu8vNdYhAPAxvHA-jlrGCw0avp6Svc8PUZH8hJtAwKSh6RIiwIGwkqrOOJ6RN4LPASFptem2cVCNn692UtcMXNkelNPHIWEa6XAqq1tHJKm0kkS4bhIhEmxPnYLmnAKDuTirdXtG0m5_D9fgsXUzWEoIPgFehl_6lg3pURDVLF61cWCDOWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: جناب نخست وزیر پیامتون برای مردم ایران چیه؟؟
بی‌بی نتانیاهو: ما با شما هستیم نا امید نشید
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72249" target="_blank">📅 08:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">با این جوابایی که پزشکیان به خبرنگار داد باید منتظر موج جدیدی از حملات طرفداران افراطی جمهوری اسلامی و تندرو ها به پزشکیان و دارو‌دستش باشیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72248" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پزشکیان:
- انصارالله مسئول اقدامات خود است و از ما دستور نمی‌گیرد.
- ما اورانیوم غنی‌شده ۶۰ درصد را در چارچوب قوانین بین‌المللی و پیمان منع گسترش سلاح‌های هسته‌ای (NPT) واگذار خواهیم کرد.
- ما به تمامی تعهدات خود ذیل پیمان منع گسترش سلاح‌های هسته‌ای پایبند خواهیم بود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72247" target="_blank">📅 07:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=uvdjkFYV99ES09LqVUDR8UFuGDA6j1u_LhwFsmnrXNJOj-ttQdtjJ1dJkMsANjg7GXIdqFQNqb5y9cNQguTCQKsMmdjuGkxRBgFdLsfcfx7-RGojnGhANib3HEwoZK7Fcp99Vcjtr9X2PvTvSVlQFoToxhgKZxx4Hyo8pzgXj2Z5oJnbpZ5gyAQp8okB9auNb5sBl-d8Zn_egwGQtQ0-M_J6klX8vAIwXE_zN165PSHp3QRFUz0AZujQSt49tjdr3vKNOax5OiTKs6kJNSxwtCaf2-wQdGOdPva8PI714FanyJBI3oGhWHjvwTrQVQYfZ38E5SyoXP8gKHc5nSQDAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efefaab11b.mp4?token=uvdjkFYV99ES09LqVUDR8UFuGDA6j1u_LhwFsmnrXNJOj-ttQdtjJ1dJkMsANjg7GXIdqFQNqb5y9cNQguTCQKsMmdjuGkxRBgFdLsfcfx7-RGojnGhANib3HEwoZK7Fcp99Vcjtr9X2PvTvSVlQFoToxhgKZxx4Hyo8pzgXj2Z5oJnbpZ5gyAQp8okB9auNb5sBl-d8Zn_egwGQtQ0-M_J6klX8vAIwXE_zN165PSHp3QRFUz0AZujQSt49tjdr3vKNOax5OiTKs6kJNSxwtCaf2-wQdGOdPva8PI714FanyJBI3oGhWHjvwTrQVQYfZ38E5SyoXP8gKHc5nSQDAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری فاکس‌نیوز:
آژانس بین‌المللی انرژی اتمی می‌گوید شما ۴۴۰ کیلوگرم اورانیوم غنی‌شده تا سطح ۶۰ درصد در اختیار دارید. این اورانیوم کجاست؟
پزشکیان:
آمریکا مدام می‌گوید ما همه‌چیز را نابود کرده‌ایم. خب، این ادعا یا درست است یا نادرست؛ کدام‌یک است؟
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72246" target="_blank">📅 07:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV1nw2Z8SRcoo3G0nDtra5Hdr_36_F53oVWLzhVUfsSzfUKSf1VnNhl9_Kti0LYKjqy3FKfGZv_7kySeWrfd6o9wcHzd3hZDIBe-9dA5HO-PfPZUlrn8i7ljJaVEgDPRCgEQyJstCZWP4Vlp3MWbWms-gL1GANmVCWi8VDXOQphgJAcJ4h4YxbSd7YflfXIK5RzQuRG3pvZb2H755mAWPGodOitr_6fEUdnWT4HP38SLrc1xeRKCYO6JvkawFA474n67KKy5MGxQCAIZaMJHmmpCWo6JkL11d1lWrHr6p3I-Bw6ltVgAiM-UlHPmC_d829DeFQCED5jKfXij3SVuGAaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d65dc0d7.mp4?token=bjCzm3P5wYeFND59TYaDXY9iRJuXXn-yYK2UStsdd05SPO3sJZ0y-PMOtW5STYpPkwtDr51LKleLJqgXgT5aTbypVi1GT2uCg5rnck6I1lUsNuBNhmrYgH6kxv1afVQcEsSc45kMDZI08ZE0Votr6lhnleDs5o89ztHuPdhbu0HAGWQtSr1q4kisIpBEzKvp6PvI9dGEPVtirVYIA4sRWQf6AwfkdvlRF_HkYD5YJ-yi1fGCj8rgnOTDtL7VSitiOhxwQeYtg8xZEACzNfh0xUcXsaHzk_ILj1UVKsgqKTYq6jAqrq46AyX4NWEwQlAtAqYhpqPvlQHsVST4_HVZV1nw2Z8SRcoo3G0nDtra5Hdr_36_F53oVWLzhVUfsSzfUKSf1VnNhl9_Kti0LYKjqy3FKfGZv_7kySeWrfd6o9wcHzd3hZDIBe-9dA5HO-PfPZUlrn8i7ljJaVEgDPRCgEQyJstCZWP4Vlp3MWbWms-gL1GANmVCWi8VDXOQphgJAcJ4h4YxbSd7YflfXIK5RzQuRG3pvZb2H755mAWPGodOitr_6fEUdnWT4HP38SLrc1xeRKCYO6JvkawFA474n67KKy5MGxQCAIZaMJHmmpCWo6JkL11d1lWrHr6p3I-Bw6ltVgAiM-UlHPmC_d829DeFQCED5jKfXij3SVuGAaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
خودِ آقای ترامپ اعلام کرد که آمریکا این افراد را تجهیز و مسلح کرده بود تا حکومت ایران را سرنگون کند.
اطرافیان نتانیاهو اعلام کرده بودند که نیروهایی از استان‌های کردستان و بلوچستان به مراکز کلان‌شهری نفوذ خواهند کرد تا حکومت را ساقط کنند.
آن‌ها تصور می‌کردند که این ماجرا سه روزه تمام می‌شود و حکومت سقوط می‌کند؛ اما حکومت استوار ماند و منسجم‌تر و متحدتر شد.
حتی کسانی که به دلایل گوناگون در برابر حکومت ایران ایستاده و با ما مخالف بودند، اکنون از ایران حمایت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72245" target="_blank">📅 07:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=ULNpnIdz7GjKGHUSpUt8sqyWctybk15rxpaW2ZEm6hhIyq5NBfj6wiutAf8O4NEWfUeBKPoVhUrDb9F3lu_3lGtPXgDprIO2aLkflvjpXyNrbyXiXXu2jinm1qaIYahZSHHWK6qzrVC84m9HjXCgarqe0gxMR6HzeuRr8eUEvEFPKb_9rxIfsfi9U5qBMwNdvoCAT4APuFEM3a35JI-SkisIhX1Xu2xnpUF9mwR7_JZgXzIKzirIPWA1tHU6Nerb6OmLAOvagpQoXWVV8E3CztbdMTwL8q7cOVu5_fVyZPAR_0ngfsbmcMk-Bnkx1XVM6TmU7YCLi4YZbO-O0pvEHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c4f14c5fa.mp4?token=ULNpnIdz7GjKGHUSpUt8sqyWctybk15rxpaW2ZEm6hhIyq5NBfj6wiutAf8O4NEWfUeBKPoVhUrDb9F3lu_3lGtPXgDprIO2aLkflvjpXyNrbyXiXXu2jinm1qaIYahZSHHWK6qzrVC84m9HjXCgarqe0gxMR6HzeuRr8eUEvEFPKb_9rxIfsfi9U5qBMwNdvoCAT4APuFEM3a35JI-SkisIhX1Xu2xnpUF9mwR7_JZgXzIKzirIPWA1tHU6Nerb6OmLAOvagpQoXWVV8E3CztbdMTwL8q7cOVu5_fVyZPAR_0ngfsbmcMk-Bnkx1XVM6TmU7YCLi4YZbO-O0pvEHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما هرگز به مردم خودمان حمله نمی‌کنیم.
برت بایر (از شبکه فاکس):
اما شما این کار را کردید.
پزشکیان:
نه، نه. چه کسی علیه ما اقدامات تروریستی انجام داد؟ چه کسی مدارس ما را هدف قرار داد؟
بایر:
متوجه هستم، اما در روزهای ۸ و ۹ ژانویه، قطعاً نیروهای امنیتی شما شهروندان ایرانی را کشتند.
پزشکیان:
خیر اصلا اینگونه نبود.آنها تروریست هایی بودند که توسط آمریکا و موساد و کرد‌ها مسلح شده بودند.ما به مردم عادی آسیبی نزدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72244" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=Jyw1N3qIKl5EmE6-HRNGJwg7nBaGtDF4ZgHJLegbT94YkfYOqaqSz_wO35C-jawZBBs5gevsGt3_zkmC96miEdUhXEeEumsrc2tWnTMWjZVwoxhUr7qUnQ9rrPzK9HlTOjXRHZSB3yWE6m-paw-6eXYvM1bmJ4q_AHe4eZV0QXOdty2TLbRjPcpuFvRQGu0032oDrhawvhQhz6Qnmt4zUB8s3KoitaPRBCyIiNbA-yak80NgVeo_U12xg2cmmSA-4sLYuUv54NNgLhJT7K2RAaFQxtDfcXYe2BesXNFcnkAAvzJ8wAcAPqPkOI-aW87bzAP1YjoVullOht9EUILvoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b2094964f.mp4?token=Jyw1N3qIKl5EmE6-HRNGJwg7nBaGtDF4ZgHJLegbT94YkfYOqaqSz_wO35C-jawZBBs5gevsGt3_zkmC96miEdUhXEeEumsrc2tWnTMWjZVwoxhUr7qUnQ9rrPzK9HlTOjXRHZSB3yWE6m-paw-6eXYvM1bmJ4q_AHe4eZV0QXOdty2TLbRjPcpuFvRQGu0032oDrhawvhQhz6Qnmt4zUB8s3KoitaPRBCyIiNbA-yak80NgVeo_U12xg2cmmSA-4sLYuUv54NNgLhJT7K2RAaFQxtDfcXYe2BesXNFcnkAAvzJ8wAcAPqPkOI-aW87bzAP1YjoVullOht9EUILvoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
رئیس‌جمهور آمریکا اعلام کرد که ما تروریست هستیم.
اما در واقعیت، همه به‌راحتی می‌توانند تشخیص دهند که ما قربانی و هدف تروریسم بوده‌ایم؛ با این حال آن‌ها می‌گویند: «نه، ما چنین کاری نکردیم.»
آن‌ها حقیقتی آشکار را انکار می‌کنند، اما در عین حال ما را به چنین اقداماتی متهم می‌سازند.
ما خواهان زندگی در صلح و آرامش در منطقه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/72243" target="_blank">📅 07:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=huuiLSI6Y8_hfC-8j37A4LQv213Uc8l78skobQLpqKbo5frtiYuPRzVaPFxOiCn2AkSwfnBPqbK0qIN3Od9VKAji4wxe2BOcsqRKKoEgLPMsJOVFQsnvujuD6Dv_G0ZFAQAXMKdbCEZk21427Ep364VzcnCcHd0UX5LCvW-PByd1SVzmSos625qj47CZHAeW4shurqE9tET9D1pGiObyRe5752KUhlkf7efKPwlVk2nbYfV5zvt9WJivIyztdtN2n1Oa0hweLuFX-SPPbisw2lN0AeBjQP0WWOh4GGjmo_jksiTP6UEy9rPuJnwpyCPUD_VmJ1MlL60PBHL5DuUwvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb427a69c.mp4?token=huuiLSI6Y8_hfC-8j37A4LQv213Uc8l78skobQLpqKbo5frtiYuPRzVaPFxOiCn2AkSwfnBPqbK0qIN3Od9VKAji4wxe2BOcsqRKKoEgLPMsJOVFQsnvujuD6Dv_G0ZFAQAXMKdbCEZk21427Ep364VzcnCcHd0UX5LCvW-PByd1SVzmSos625qj47CZHAeW4shurqE9tET9D1pGiObyRe5752KUhlkf7efKPwlVk2nbYfV5zvt9WJivIyztdtN2n1Oa0hweLuFX-SPPbisw2lN0AeBjQP0WWOh4GGjmo_jksiTP6UEy9rPuJnwpyCPUD_VmJ1MlL60PBHL5DuUwvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان:
ما تا آخرین لحظه به مقاومت ادامه خواهیم داد.
بله، قطعاً مشکلات اقتصادی داریم؛ اما برای بقا، از هر سختی‌ای عبور خواهیم کرد و ایستادگی خواهیم نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72242" target="_blank">📅 07:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=t0Y9q17oj563tT-u8vxKGky1tI8wpOjUrsVQ1tOSKab4Rn-mEDBAat3EdDSpZFqiKWqUcpJEKkMKfmB0uXxs4q1-urN1SOQRI4j4njc09Ixe75owdvLc30lYfJrzosFoyFwMvpDX4YYDxKMRC5JggfFxug8kfsWQvbYUFDxMOQq5JyUtxwkcNnkCqNdA8XVd4Eaz6T_lV1Vngzx8nYhX9-ii_3lpGqjQ66zFAOoTpM4Jz1ONqg-fVW0QU_FIlanx5kfkZmcDqB4b5PB3KAZNVyuyaYMcjN6GE_JCQMWZ8He5Yv5Q2wxYaXp4SkeNpkM2Ir4ZNJKxQ0YPm_6Oo_b7DbxeGctrkG5c18Cy5DRajDqAr720jnm-HHMCy4k_b2iKUUTSr4LWM_-oszR4cBBTUWNGoVj4ez8O-QRXbc51IL4xKrqRi8jg-8jJ3cO3wEjDhG0dpu_mzLZjbPyYFBQB1gFjpJWf5rnzFU9Ga-mHoqgu7ygZS3AwkD3Ekf9e6il32yPNtr6fY900mMg1AbkiSu9IbU1eE4GghECNnTCQOxI6lR79WTuZTJc0bDZWsSNAQhpiC0Ixwgzwi-2E3-9_-Bg9o6rdKEJMEaDE32_iBIoMHniiF910SP3cafDxSizH5ajebEihU0bpyxKmX78Y-j5Zn3K8jsOd1-KGS1h9iXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9fa81c1c3.mp4?token=t0Y9q17oj563tT-u8vxKGky1tI8wpOjUrsVQ1tOSKab4Rn-mEDBAat3EdDSpZFqiKWqUcpJEKkMKfmB0uXxs4q1-urN1SOQRI4j4njc09Ixe75owdvLc30lYfJrzosFoyFwMvpDX4YYDxKMRC5JggfFxug8kfsWQvbYUFDxMOQq5JyUtxwkcNnkCqNdA8XVd4Eaz6T_lV1Vngzx8nYhX9-ii_3lpGqjQ66zFAOoTpM4Jz1ONqg-fVW0QU_FIlanx5kfkZmcDqB4b5PB3KAZNVyuyaYMcjN6GE_JCQMWZ8He5Yv5Q2wxYaXp4SkeNpkM2Ir4ZNJKxQ0YPm_6Oo_b7DbxeGctrkG5c18Cy5DRajDqAr720jnm-HHMCy4k_b2iKUUTSr4LWM_-oszR4cBBTUWNGoVj4ez8O-QRXbc51IL4xKrqRi8jg-8jJ3cO3wEjDhG0dpu_mzLZjbPyYFBQB1gFjpJWf5rnzFU9Ga-mHoqgu7ygZS3AwkD3Ekf9e6il32yPNtr6fY900mMg1AbkiSu9IbU1eE4GghECNnTCQOxI6lR79WTuZTJc0bDZWsSNAQhpiC0Ixwgzwi-2E3-9_-Bg9o6rdKEJMEaDE32_iBIoMHniiF910SP3cafDxSizH5ajebEihU0bpyxKmX78Y-j5Zn3K8jsOd1-KGS1h9iXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ترامپ مدام می‌گفت «می‌خواهم برای مردم ایران هدیه‌ای بیاورم»، اما هدیه‌ای که آن‌ها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
آنچه آن‌ها واقعاً به دنبال آن هستند، دامن زدن به وقایعی در کشور است که زمینه را برای فروپاشی نظام، جامعه و دولت فراهم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/72241" target="_blank">📅 07:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=r_-EhIeV2_oxR1W9PofSF1xHX6W_8eBxy0sbGZi2SCEAj8qn4cTOKzijoqZYmKAvLZPNnJkWrsKRuzkeB9F4V9y_E0UnOusG9yD5jFQtIN7FmhgC_wdv6j1IvFaYN_upGbjvC0VD1lEfMzOCA5y8SkSaNwsqZ13kHrWABRgFhcBsulAsJr_CaUeySkStys2G9W9_cjHTOD-pAsmDX4aKaS_6_rPeVwEkJl-Lr_hwJGLJu1BqEviUisADIWWIaYpJX64IMVCnSz848F3rzbpVyGG4QRh9inexNFmbjbVSWeE0hrdgH2fG9Q9owjVhcMTxAaCDzrps1u1f8DwgwqMI3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b006ce96b.mp4?token=r_-EhIeV2_oxR1W9PofSF1xHX6W_8eBxy0sbGZi2SCEAj8qn4cTOKzijoqZYmKAvLZPNnJkWrsKRuzkeB9F4V9y_E0UnOusG9yD5jFQtIN7FmhgC_wdv6j1IvFaYN_upGbjvC0VD1lEfMzOCA5y8SkSaNwsqZ13kHrWABRgFhcBsulAsJr_CaUeySkStys2G9W9_cjHTOD-pAsmDX4aKaS_6_rPeVwEkJl-Lr_hwJGLJu1BqEviUisADIWWIaYpJX64IMVCnSz848F3rzbpVyGG4QRh9inexNFmbjbVSWeE0hrdgH2fG9Q9owjVhcMTxAaCDzrps1u1f8DwgwqMI3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
اگر دولت فعلی آمریکا بخواهد در چارچوب حقوق بین‌الملل به توافق برسد، بسیار خب.
اگر نه، چه پیش از انتخابات باشد و چه پس از آن، برای ما چه تفاوتی دارد؟
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/72240" target="_blank">📅 07:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=N8kCmjnhNTW9X0DGY18Pgl3z1EKmxw0ubMMaaeLRuQk53b2Fall7Tu94QTOagS4Duuh_Esy0q_Bu1D--n60Qu1HjvaTGupcgkuQFTPM4YHNBJ2ihOyQZ3ySefg9nC1D1U-KXyGFHeioRnYn6Djtm5eKsKWNy0hqFbi8-3ML2eUKgwNoCO0AyZzpbLZSg61PfnkeqLd_EY13IWLPnFeLaJDwT37fQtNI5skWKr_kb32eDfac43ghAILlIm1UStIyWdzd0vMjOIlzNpT9rW0wKac40gWcpnXCcVy3hj3DEdWEI9iFbWdVOW61Nrf-64GYmaG8L4gfSmf3Ly5pQ_X_qIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d17a7864a.mp4?token=N8kCmjnhNTW9X0DGY18Pgl3z1EKmxw0ubMMaaeLRuQk53b2Fall7Tu94QTOagS4Duuh_Esy0q_Bu1D--n60Qu1HjvaTGupcgkuQFTPM4YHNBJ2ihOyQZ3ySefg9nC1D1U-KXyGFHeioRnYn6Djtm5eKsKWNy0hqFbi8-3ML2eUKgwNoCO0AyZzpbLZSg61PfnkeqLd_EY13IWLPnFeLaJDwT37fQtNI5skWKr_kb32eDfac43ghAILlIm1UStIyWdzd0vMjOIlzNpT9rW0wKac40gWcpnXCcVy3hj3DEdWEI9iFbWdVOW61Nrf-64GYmaG8L4gfSmf3Ly5pQ_X_qIYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان، رئیس‌جمهور ایران:
ما هرگز به دنبال جنگ نبوده‌ایم و نیستیم. من عمیقاً معتقدم که انسان‌ها نباید موجب مرگ انسان دیگری شوند.
قرار است ما موجودات برگزیده خلقت باشیم. وقتی می‌توانیم مسائل را از طریق گفتگو حل‌وفصل کنیم، نباید به کشتن یکدیگر متوسل شویم.
اما با اقداماتی که اسرائیل انجام داده، آن‌ها این جنگ را به ما تحمیل کرده‌اند.
با این حال، ما خواهان ادامه آن نیستیم. این آمریکاست که باید تصمیم بگیرد آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72239" target="_blank">📅 07:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f631e90489.mp4?token=tsLURlsSgytKG3wiXNF3UanqtU7yrKHtvU7vi4QozDbROhQynnj8rq2IhFwqIIX0tkChnCXRgbuVZxXe-5foIMZdaczcslID3Ge6zZcrZmE_SyweC9lhoWifLMTLx2EOxdHAdQMADEtmOYx2HqMwUgFdVQnLXCWHckgoJGWh0gFr7-tgB8YFsfH35OEcfK5kDACs5tsvLERps8MGKBx57Tw20C-6FlR8yUGpwE4a532KwZu5X05bUi_JCSANsdv5h0EiDzfDNGgmIBp0uP21ntMAtDgPTYNKFy00dnNfeoYbAx2cq2WkWcv41fhEGjcbPq2N1Az9bdTuV6cA9i6wDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f631e90489.mp4?token=tsLURlsSgytKG3wiXNF3UanqtU7yrKHtvU7vi4QozDbROhQynnj8rq2IhFwqIIX0tkChnCXRgbuVZxXe-5foIMZdaczcslID3Ge6zZcrZmE_SyweC9lhoWifLMTLx2EOxdHAdQMADEtmOYx2HqMwUgFdVQnLXCWHckgoJGWh0gFr7-tgB8YFsfH35OEcfK5kDACs5tsvLERps8MGKBx57Tw20C-6FlR8yUGpwE4a532KwZu5X05bUi_JCSANsdv5h0EiDzfDNGgmIBp0uP21ntMAtDgPTYNKFy00dnNfeoYbAx2cq2WkWcv41fhEGjcbPq2N1Az9bdTuV6cA9i6wDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان:
یکی از مشکلاتی که با آن مواجه هستیم، مسدود بودن منابع مالی ما در چین است.
ما حتی نمی‌توانیم پول خود را از کشوری که به آن کالا صادر کرده‌ایم خارج کنیم، چه برسد به اینکه بخواهیم از آن وجوه برای پرداخت به طرفی دیگر در گوشه‌ای دیگر از جهان استفاده کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/72238" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=Gqies3Q0kgRVjSryvi3vO3CG0FjvIvl4_bFFj5WZ66Em9S4lWp9U8F8c1mdKsQ5ycoYAVoT3B-HoTZVR8FNGVsY4CMIS49H1ejWj_wX7psUqwt6TqMVY4adD3mmo1-K1Q39YWdp7-TSmzanQHwT8YmH7p4deOwrvP5PWtEY55tAxrO1xDe0pyTqXMuI94ACWYpZBsYMrGw34bAlyIxZy7ablDLby8JGuBESLguqpUZbMr0Fl4-2k2JC1KXeXzy68FK-GSdlH-QitDV71xqidRjrrgQoV9YPMlKss-5ecbs_fIaDwdW0rjMH7xv38nlfVjl3IUJeFsL83HAp1iGX4-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4c8deae6.mp4?token=Gqies3Q0kgRVjSryvi3vO3CG0FjvIvl4_bFFj5WZ66Em9S4lWp9U8F8c1mdKsQ5ycoYAVoT3B-HoTZVR8FNGVsY4CMIS49H1ejWj_wX7psUqwt6TqMVY4adD3mmo1-K1Q39YWdp7-TSmzanQHwT8YmH7p4deOwrvP5PWtEY55tAxrO1xDe0pyTqXMuI94ACWYpZBsYMrGw34bAlyIxZy7ablDLby8JGuBESLguqpUZbMr0Fl4-2k2JC1KXeXzy68FK-GSdlH-QitDV71xqidRjrrgQoV9YPMlKss-5ecbs_fIaDwdW0rjMH7xv38nlfVjl3IUJeFsL83HAp1iGX4-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسعود پزشکیان در گفتگو با خبرنگار فاکس‌نیوز:
هر کس بخواهد اعتراض کند، کاملاً حق انجام این کار را دارد.
ما با بسیاری از این کارشناسان گفتگو کرده‌ایم. اما تبدیل اعتراضات به ابزاری برای تقابل (مسلح کردن معترضان)، مقوله‌ای کاملاً متفاوت است.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72237" target="_blank">📅 07:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72236" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72236" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/asd1x6QGRXmh9hXVQmZ5VVjtn9NEuHpGyuH6uTyW3AWoQrfuYyUdwfNDgvJWurCZTgDCyDS8WlYpU15Gu2wiRG6VYBGuIHWzgzViPMqAK62c-UjsiJHJk2wRaRr_D_vJxJ9gPUJg5WvCvRxhTwIoikO6I6g7djXgQZD32dFZriuxTJUmyap7SjdDKAZvrOE9SzLiNngOiCmzHbMy_qkuainku9IWIt7BnYGK6cgv8r56M8G5334_XuBQmWgkdWvwW-GIqF7eVrgFOQNcIxqZqMpks_DIt16MFzfZvdT6BIeab_Q9liA85HJ2UGwjhxCVzg2x9JMO5GRP8Of31PzXHQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72235" target="_blank">📅 01:48 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25201994ac.mp4?token=foXEeasIV7yny35lq9DPivZMFlACXL8Ik0vWVisSNW5HpcDpYoN834_lBPU-bP3xDN9xsVv8cjAWzevrLrcbrrNU5Kf_8NHplvSnk6SZDi-ScmVzUnd_UYdpcDj2UXzBF8YRrxE-T3GfWHzt7ckX6WnwHgITK964yNE0bmLPxCKBL4YpFzkF-I3YVInklEt9YX0JMNbp_MIlpKeKmlXXR_i2ZsEZpCmUcfTv2Sr4n8IuJdY1kQQB6otJ-4ZIhRsY4XpYh8977CcbCUNqw5TJ-8hyxazkJpYZFzx3VmUqyNAeH0-u_nnYwseLpsRTD60ukTS8j_QIVKHEq6bFOIPeVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25201994ac.mp4?token=foXEeasIV7yny35lq9DPivZMFlACXL8Ik0vWVisSNW5HpcDpYoN834_lBPU-bP3xDN9xsVv8cjAWzevrLrcbrrNU5Kf_8NHplvSnk6SZDi-ScmVzUnd_UYdpcDj2UXzBF8YRrxE-T3GfWHzt7ckX6WnwHgITK964yNE0bmLPxCKBL4YpFzkF-I3YVInklEt9YX0JMNbp_MIlpKeKmlXXR_i2ZsEZpCmUcfTv2Sr4n8IuJdY1kQQB6otJ-4ZIhRsY4XpYh8977CcbCUNqw5TJ-8hyxazkJpYZFzx3VmUqyNAeH0-u_nnYwseLpsRTD60ukTS8j_QIVKHEq6bFOIPeVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
‼️
🇮🇷
🇮🇱
🌟
نماینده اسرائیل در سازمان ملل دستگاه «استارلینک» را به نماینده اعزامی تهران داد و درباره «کمک به مردم ایران برای سرنوشت و آزادی با این دستگاه» صحبت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72234" target="_blank">📅 01:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=RlLCby2aNWOxsdHhSvXOR22-mzz0EYlDoKrxbyZTt5PsWdZxEtDNtHOX5IRzVaGu1nVHfqbb809yxU_ovSIVBZd3lQQEpo2KHPgh2CmCRZqQiTZWDJW4mlnxsSyZ23JJJp9xK64cstDIM4-LEB1Y9rHi-5RG2x1wJrVxnRsf9vKEIids9OCnkWK8lbuG8F4qSjQMYkhlEvG_WpUykihxQMjA_8wA4n3jicWp5EPlhycez3xDzkfRLOk94mnZn_wEbCfpcityEr-nahi_OA3wHfsOIOsPxqmxxBiIp5DVJwYOnsV6M5HgdXRLd9ka2xb2_T1odgblD9rLtcV-eiBWlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7bed5269.mp4?token=RlLCby2aNWOxsdHhSvXOR22-mzz0EYlDoKrxbyZTt5PsWdZxEtDNtHOX5IRzVaGu1nVHfqbb809yxU_ovSIVBZd3lQQEpo2KHPgh2CmCRZqQiTZWDJW4mlnxsSyZ23JJJp9xK64cstDIM4-LEB1Y9rHi-5RG2x1wJrVxnRsf9vKEIids9OCnkWK8lbuG8F4qSjQMYkhlEvG_WpUykihxQMjA_8wA4n3jicWp5EPlhycez3xDzkfRLOk94mnZn_wEbCfpcityEr-nahi_OA3wHfsOIOsPxqmxxBiIp5DVJwYOnsV6M5HgdXRLd9ka2xb2_T1odgblD9rLtcV-eiBWlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستربین ۷۱ ساله شد و جشن تولدشو با صدای بانو هایده جشن گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72233" target="_blank">📅 00:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=lO3UK1dlV5ALkMcbUYiho_N2grhY7KbSx9EVEqUweq9sandSLPF1_8-Rnf5bm-oCrrMw1hxshHfxSh7hpiBqwxn9sGBqBXaq7IV1SQOTW5enJP_6bGPpFBtt00BDbjqyojqBrR0YI4BkMJHXkCxaVgB-_9Bt-NVqpglk414ZGqCzmRLVhgvli7kiKFL-AxV1Fc5tTFQIbIyu_p6S49_4omsw5oZ16FvMltsqXTehPuu4TuVpFGpLUP63gZISbhvOBhkZOAv3I7ksYaxi33TzzCRiazM4qjU88zzsxM3SsRmTq8Vp3V6oSSoecoW1YtONnFMUFQDXzlyZ3RfpCnCvRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cef647d91c.mp4?token=lO3UK1dlV5ALkMcbUYiho_N2grhY7KbSx9EVEqUweq9sandSLPF1_8-Rnf5bm-oCrrMw1hxshHfxSh7hpiBqwxn9sGBqBXaq7IV1SQOTW5enJP_6bGPpFBtt00BDbjqyojqBrR0YI4BkMJHXkCxaVgB-_9Bt-NVqpglk414ZGqCzmRLVhgvli7kiKFL-AxV1Fc5tTFQIbIyu_p6S49_4omsw5oZ16FvMltsqXTehPuu4TuVpFGpLUP63gZISbhvOBhkZOAv3I7ksYaxi33TzzCRiazM4qjU88zzsxM3SsRmTq8Vp3V6oSSoecoW1YtONnFMUFQDXzlyZ3RfpCnCvRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش جالب رئیس جمهور چین  به اقدام ترامپ برای جاگزین کردن عکس بایدن با «خودکار»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72230" target="_blank">📅 00:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=q7cPxoBMGqcuw5ln-dxlhpaOsbI6o4Ozf9TYSg-a0YcQMavaFptsFcCtuHybftyBX-jq5birCmgDh-JpLx6y-2sqsuvtt9UpPu7Gi9NlrSPOkKqDXg6uhsrMtykWG3iWaZdpbS3lwESns7xfAuWyJufg560o4UGUnwpk4UUnek5wOqJWsKVmby7OQu06YUzZSURcAFmB-1C-P2d8oMVOB4ITFzrPkKDuw70jzYHrcf5jqFF38LlCkceAZghJKKHlJJfze0GRrW_sO_8_-IoSy0VbGPzu4AjkDBNtGxfoZvOCDtKs27wkVPvg-5ZWnIFPioV-TR56gXJYoIk7MKXGjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd32fc6ad7.mp4?token=q7cPxoBMGqcuw5ln-dxlhpaOsbI6o4Ozf9TYSg-a0YcQMavaFptsFcCtuHybftyBX-jq5birCmgDh-JpLx6y-2sqsuvtt9UpPu7Gi9NlrSPOkKqDXg6uhsrMtykWG3iWaZdpbS3lwESns7xfAuWyJufg560o4UGUnwpk4UUnek5wOqJWsKVmby7OQu06YUzZSURcAFmB-1C-P2d8oMVOB4ITFzrPkKDuw70jzYHrcf5jqFF38LlCkceAZghJKKHlJJfze0GRrW_sO_8_-IoSy0VbGPzu4AjkDBNtGxfoZvOCDtKs27wkVPvg-5ZWnIFPioV-TR56gXJYoIk7MKXGjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با این تحرکات لجستیکی و نظامی آمریکا باید توافق رو قطعی بدونیم
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72229" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">عجب دنیاییه، پزشکیان رفت سازمان ملل از مردم غزه حمایت کرد، نتانیاهو هم رفت از مردم ایران حمایت کرد
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/72228" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
می‌خواهم از شما بخواهم که با دقت به حرف‌های من گوش دهید. روزی خواهد رسید، و ممکن است این روز خیلی دور نباشد، که مردم ایران آزاد خواهند شد.
این رژیم خبیث، به دلیل دروغ‌هایش، فسادش و ظلمش، سقوط خواهد کرد. این رژیم ستمگر فرو خواهد پاشید و همه ما در آن روز جشن خواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72227" target="_blank">📅 22:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72226">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
این یک دستگاه ارتباطی استارلینک است که به مردم اجازه می‌دهد به حقیقت دسترسی داشته باشند، آزادی اندیشه و آزادی بیان را تجربه کنند.
به همین دلیل است که رژیم ایران میلیاردها دلار برای سانسور اینترنت هزینه می‌کند.
آقای رئیس جمهور، من این دستگاه را پیش شما می‌گذارم تا بتوانید آن را به هیئت ایرانی بدهید.
بنابراین، وقتی آنها ناگزیر به ترک کشور شدند، آنها نیز می‌توانند آزادانه داستان خود را در رسانه‌های اجتماعی بیان کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/72226" target="_blank">📅 22:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72224">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">نتانیاهو: خدا باماست
سخنرانی تموم شد
#hjAly‌</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72224" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72223">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">نتانیاهو: روز آزادی مردم ایران رو باهم جشن می‌گیریم
#hjAly‌</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72223" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72222">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">نتانیاهو: یه روزی که خیلی دیر نیست، مردم ایران آزاد می‌شن
🔥
#hjAly‌</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/72222" target="_blank">📅 22:11 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72221">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">نتانیاهو: نیروی مردم ایران، آخوند رو شکست می‌ده
#hjAly‌</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72221" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72220">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: شما مدافعان قلابی حقوق بشرین
#hjAly‌</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72220" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72219">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نتانیاهو خطاب به کسایی که سالن رو ترک کردن: وقتی آخوندا هزاران معترض رو کشتن شماها کجاها بودین؟
#hjAly‌</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/72219" target="_blank">📅 22:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72218">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: آخوندا می‌ترسن که مردمشون استارلینک داشته باشن
#hjAly‌</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72218" target="_blank">📅 22:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72217">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=Nf5bu3mCo1Qe0R6JVoi4NMCzTREVD40k15YCdnw78JRZ6lyljIa5fqhO58qD-ci0oIm7CFMgH6F-8x5br57PnyPx4n_mCN0_NMwXrhhaTk8K9NhVGANUMdzAvuBuEIUPACMYBDcqOBjpD1owGSPJ_RKZHK2sftZJrEM08_7QZChBRljCDjqZDRLstS_63pBuHKyUn7mXyXwscfVRGtoCLZIFjAR-QWbM9H2-PY8-MKxHxMsKZQw6QzEsFShH9mxAlWpyU82AXc2kvs5Dx9kn6AuULCGr1r-rS7UjJwR7hAh8bGT5A8sM7bbfw5ugc6vokWtn8ZJqPmvuPEk6K5Vfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d451a336d.mp4?token=Nf5bu3mCo1Qe0R6JVoi4NMCzTREVD40k15YCdnw78JRZ6lyljIa5fqhO58qD-ci0oIm7CFMgH6F-8x5br57PnyPx4n_mCN0_NMwXrhhaTk8K9NhVGANUMdzAvuBuEIUPACMYBDcqOBjpD1owGSPJ_RKZHK2sftZJrEM08_7QZChBRljCDjqZDRLstS_63pBuHKyUn7mXyXwscfVRGtoCLZIFjAR-QWbM9H2-PY8-MKxHxMsKZQw6QzEsFShH9mxAlWpyU82AXc2kvs5Dx9kn6AuULCGr1r-rS7UjJwR7hAh8bGT5A8sM7bbfw5ugc6vokWtn8ZJqPmvuPEk6K5Vfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
اخلاقی‌ترین ارتش جهان؛ ارتش اسرائیل (IDF).»
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/72217" target="_blank">📅 22:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72216">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">نتانیاهو: هرگز نسل‌کشی نکردیم
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72216" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72215">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">نتانیاهو: آقای ممدانی تلاش کردی من نیام نیویورک، دیدی کیر شدی؟
#hjAly‌</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72215" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72214">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نتانیاهو: کیرم تو ممدانی و زنش و دوستاش
#hjAly‌</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72214" target="_blank">📅 22:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72213">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">نتانیاهو: ما کلی واکسن و غذا به مردم غزه دادیم
#hjAly‌</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72213" target="_blank">📅 22:00 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72212">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نتانیاهو: اردوغانِ جاکش، تو هیچوقت حاکم قدس نمی‌شی
#hjAly‌</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72212" target="_blank">📅 21:59 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
