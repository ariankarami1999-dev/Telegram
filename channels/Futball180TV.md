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
<img src="https://cdn5.telesco.pe/file/u27T9V7IaRsiPBUvXS96LN-zjhow6FxtK0YToFOB7ecvSRivQpKuilZMyYH3kmczdXmIaoXm3DeLPho1L7LOMhimYGAIAOyuAQADQvA4yTdN14pipRYbXLPwiuqIsFcglK3nI6nGKsUFbqpRoYrXS9SwireRiXO_6Rh5NNyugSq95E3oSmr0HDZ6xTdLzQRi-ypcvPP8967hn-nNoaO-SonX5AAerUV48TfkfT-xEygyK0LN5-yRtRrXNwM4SByULmb91k3NxTQ4n_hjOaFk54sDMecpXa_yvjtlnuhRiBnK2BH4_JyIaNg2wNH-WufhhajrG6DxHxc2kMoILBHgWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 414K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-23 23:22:57</div>
<hr>

<div class="tg-post" id="msg-106503">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ماشاریپوف بجای رزاقی‌نیا وارد زمین شد</div>
<div class="tg-footer">👁️ 7 · <a href="https://t.me/Futball180TV/106503" target="_blank">📅 23:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106502">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حسن‌الهیدوس ۳۶ ساله هنوز برا السد بازی میکنه
😳</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/106502" target="_blank">📅 23:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106501">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حردانی امشب بهترین بازیکن استقلال بوده</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/Futball180TV/106501" target="_blank">📅 23:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106500">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">۱۵ دقیقه تا پایان</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/106500" target="_blank">📅 23:19 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106499">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آب درنگ
😆</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/106499" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106498">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">صداوسیما حداقل با یه دقیقه تاخیر بازیو نشون ملت میده</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/106498" target="_blank">📅 23:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106497">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">استقلال کوووووون آورد</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/106497" target="_blank">📅 23:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106496">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حردانی میگه اگه دعوا شد کادرفنی بریزه وسط زمین
😂
😐</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/106496" target="_blank">📅 23:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106495">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
🚨
🚨
گل السد هندددد شددددد</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/106495" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106494">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">صحنه داره بررسی میشه</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/Futball180TV/106494" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106493">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">السد زدددددد</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/106493" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106492">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">گلگگلگلل</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/Futball180TV/106492" target="_blank">📅 23:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106491">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86d2b781d1.mp4?token=Kap6uIO-8gYIoe5L3a5kcGmU1PaRL8c4JGub0Y06h3j-AvrYtJBwmL91sGwCKkstRhOaFGMw3F2O16Ye1_LEeNdLPHgX9LZeHWsLBiKL7MhNgzM9-HhUutQSnzvpNL0E9N0ycK4i6IEN7oNyycVND08J3CFUtImHHKCTVBYQyVLF7rM2CIb0IbDxBuUDDcIfO9N7nlWoR81Q61N6dyYKfd8PsuMzxqn8eEzPfZB5YhOZGYyJluarNJMwXWy2lRpwhYqi8PB8Evt3_KFnJTrDAcjBXLixC5MaRMOJuz-hyMJUZK-P5h-t0tkwAjh1LtpPcvtfVpkfwzuu1autTq1xXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86d2b781d1.mp4?token=Kap6uIO-8gYIoe5L3a5kcGmU1PaRL8c4JGub0Y06h3j-AvrYtJBwmL91sGwCKkstRhOaFGMw3F2O16Ye1_LEeNdLPHgX9LZeHWsLBiKL7MhNgzM9-HhUutQSnzvpNL0E9N0ycK4i6IEN7oNyycVND08J3CFUtImHHKCTVBYQyVLF7rM2CIb0IbDxBuUDDcIfO9N7nlWoR81Q61N6dyYKfd8PsuMzxqn8eEzPfZB5YhOZGYyJluarNJMwXWy2lRpwhYqi8PB8Evt3_KFnJTrDAcjBXLixC5MaRMOJuz-hyMJUZK-P5h-t0tkwAjh1LtpPcvtfVpkfwzuu1autTq1xXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔥
گل دوم استقلال به السد توسط سحرخیزان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/106491" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106490">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سوپرپاس گل یاسر‌آسانی
😐
😐
😐
😐
🔥</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/106490" target="_blank">📅 22:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106489">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سعید سحرخیزان
😂
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/106489" target="_blank">📅 22:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106488">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دومییییییییییییی</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/106488" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106487">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">استقلاللللللللللللل ایرااااااللن</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/106487" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106486">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اااااللللللله الکبررررررررر</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/106486" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106485">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">گلگلگلگلگگلگلگلگگلگلگل</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/106485" target="_blank">📅 22:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106484">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xw_e8LQ_mOFoTCnoNQBPTG_ZkPL2bUhJ0So4O4kVrZC19MQIHr7lkzbw2zKJv1AKb487cquEu2Uf3PYDrlV5KihcIWvC3ve5O0rciisV6twm0XotVCYqqTPCIwI2ORzB0k7fJ_mKJlT8_zydoI3DhguCMaVvPlS4dx8r0PK1pbcLi8hKC1jgGNDN80gWKunFH33C-MTSnMubp-LR4chmjA-bKOFCvTssrQAPSmVCU9MGBtZ6iFoypik7HU05JZO4jpI7RfO4ZR4pnKRzgDW_m6Vwak0haSjkEU2SXKfI7UrIHBsIMIl-dTMl3_kWCLIu0lLsFS_JpgTc3yeLAkjb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
آمار نیمه‌اول بازی استقلال و السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/Futball180TV/106484" target="_blank">📅 22:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106483">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/323962117f.mp4?token=sJ2psTP0FFOanU4Q7u6D5eCrLv-DEOFyg0oxgB316EJAytS6aZsqQlmMfGZ5mOxHeV8fe-IfgieZ6XA2LpVd1Ei_8Cf629K8gWIBnTmmYaAYRsnJhuPwOU0jBhZxv1x4I_VroIMFpd51mki3fGexUGU3430SHymHsGX0R-yUlq2yTorpDweUXxewScS4FvnpykXd_3OtqgWTFaYC_OasEZR6_jLHjvqy61xH1a3-6Qs_JAI2kqaJL6qTkXR_8wExcRdcQra8US_qfcQnsWi_MEJfB9g4dLxMn1xz5T53yX1CYcBiot-_Q0tiikotwsP_GCMoe6RFYRQPDr-r27V1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/323962117f.mp4?token=sJ2psTP0FFOanU4Q7u6D5eCrLv-DEOFyg0oxgB316EJAytS6aZsqQlmMfGZ5mOxHeV8fe-IfgieZ6XA2LpVd1Ei_8Cf629K8gWIBnTmmYaAYRsnJhuPwOU0jBhZxv1x4I_VroIMFpd51mki3fGexUGU3430SHymHsGX0R-yUlq2yTorpDweUXxewScS4FvnpykXd_3OtqgWTFaYC_OasEZR6_jLHjvqy61xH1a3-6Qs_JAI2kqaJL6qTkXR_8wExcRdcQra8US_qfcQnsWi_MEJfB9g4dLxMn1xz5T53yX1CYcBiot-_Q0tiikotwsP_GCMoe6RFYRQPDr-r27V1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
🇮🇷
درگیری بهروز سلطانی و وحید قلیچ دو پیشکسوت پرسپولیس بر سر علی‌پروین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.2K · <a href="https://t.me/Futball180TV/106483" target="_blank">📅 22:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106480">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76510c3fac.mp4?token=ugHYWThqpgLDcKI6rCwpr1HaMsGCOpDvjXbomRpZu-ghdshUb1daCSI0xUZ984iPmlmCaOHszlSnpEOZ78MYVBw-bCpXu16r7s5dyOtsx2HJJqwU2KDwzUKO1S6sm5L621G7VGsJ6Azq8-r83BbUAIhV8w2yPB_w2l07IfhNoWietm98RPmkSOUD0LD_ANt7vId7aBBZ4hStm-D2BM15lmtn8Kb_wXPW3_16e2fovdwITfBPdwLTXdqV8FTBzNmIbEThovRHMCxD1O5ZaY6Xawdm4EMcut6_E3ii7XiNitgjfQGm7ca_VzqM5-RqNyxlYvSTpRfaxkM6KBL66J3hFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76510c3fac.mp4?token=ugHYWThqpgLDcKI6rCwpr1HaMsGCOpDvjXbomRpZu-ghdshUb1daCSI0xUZ984iPmlmCaOHszlSnpEOZ78MYVBw-bCpXu16r7s5dyOtsx2HJJqwU2KDwzUKO1S6sm5L621G7VGsJ6Azq8-r83BbUAIhV8w2yPB_w2l07IfhNoWietm98RPmkSOUD0LD_ANt7vId7aBBZ4hStm-D2BM15lmtn8Kb_wXPW3_16e2fovdwITfBPdwLTXdqV8FTBzNmIbEThovRHMCxD1O5ZaY6Xawdm4EMcut6_E3ii7XiNitgjfQGm7ca_VzqM5-RqNyxlYvSTpRfaxkM6KBL66J3hFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت رزاقی‌نیا با واکنش دیدنی گلر السد تبدیل به گل نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/Futball180TV/106480" target="_blank">📅 22:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106479">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">استقلال چه ضد حمله‌هایی میزنه
😐
😐
😐</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/Futball180TV/106479" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106478">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/Futball180TV/106478" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106477">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">استقلال بدشانسسسسسسس</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/106477" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106476">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/Futball180TV/106476" target="_blank">📅 22:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106475">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aebefadf88.mp4?token=coIVNsxPjbLNrosMtsxsWa7Ct8eVCefkZKwkEkXwsqElxLaSaI2bQnQDzIK0Vwdvlf08j5a0QDc94xzbQwC6-YIFDEUwk8wfufDpqnWZk-SwVvYJzlRDWCkBh3CQRDJ1MV0gKEvEsKLfBADFd3KvcaN40PRwZQOkDkhYwrkXAZFp50bkYwokmv0SJtV-GRe3DDG3jrMKA64FubSe4Q-AshBq7S0fHp8nN7rR4_OQVFxK9sbhDiFUHp0FPoqP1hzW_fIOG7E4J00o33rwPI9yo2hVFNPeDz3wLJ-q1zoiZvV19A8rl7RjJ9Ai4v3NCQxf6zjpWeewn85SQJ7TlpW2Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aebefadf88.mp4?token=coIVNsxPjbLNrosMtsxsWa7Ct8eVCefkZKwkEkXwsqElxLaSaI2bQnQDzIK0Vwdvlf08j5a0QDc94xzbQwC6-YIFDEUwk8wfufDpqnWZk-SwVvYJzlRDWCkBh3CQRDJ1MV0gKEvEsKLfBADFd3KvcaN40PRwZQOkDkhYwrkXAZFp50bkYwokmv0SJtV-GRe3DDG3jrMKA64FubSe4Q-AshBq7S0fHp8nN7rR4_OQVFxK9sbhDiFUHp0FPoqP1hzW_fIOG7E4J00o33rwPI9yo2hVFNPeDz3wLJ-q1zoiZvV19A8rl7RjJ9Ai4v3NCQxf6zjpWeewn85SQJ7TlpW2Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
استقلال از کووووووون آورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/Futball180TV/106475" target="_blank">📅 22:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106474">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9bbd3ca42.mp4?token=KtfZJReq3vxBFA346RN4tg2Byv96WD6PenQlPnx3P1EY-A7tpKIuXUBw04Au_0Nv5sRTkdokaaYL-svcgHabkuyziVm5f4MA9u-mh7t-zxQGJ9szSXFzNc7scKeUcGhaatAFJhxiq0F3LeV52M4-Xyn95ucq_bAU7nI2NLbrgA4RUUt-apnEBD3Zm5WnzP5hP_J_-6CdWDBRCtTkeaGxMSGAhx3ki26jcZzRj4cP7pDfqlNi37ZJICECHNf7mU-Q-zwW3eiWrOPyMCjrVorYK0MKQuenQuvN1f2OBdxuvTPEe1K5VFPwnX_0y6oON8MQ4fz_7OxaG2HkJ4nQIFnVLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9bbd3ca42.mp4?token=KtfZJReq3vxBFA346RN4tg2Byv96WD6PenQlPnx3P1EY-A7tpKIuXUBw04Au_0Nv5sRTkdokaaYL-svcgHabkuyziVm5f4MA9u-mh7t-zxQGJ9szSXFzNc7scKeUcGhaatAFJhxiq0F3LeV52M4-Xyn95ucq_bAU7nI2NLbrgA4RUUt-apnEBD3Zm5WnzP5hP_J_-6CdWDBRCtTkeaGxMSGAhx3ki26jcZzRj4cP7pDfqlNi37ZJICECHNf7mU-Q-zwW3eiWrOPyMCjrVorYK0MKQuenQuvN1f2OBdxuvTPEe1K5VFPwnX_0y6oON8MQ4fz_7OxaG2HkJ4nQIFnVLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
گلگلگلگگلگلگل اول استقلال توسط یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/106474" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106473">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">استقلالللللللللللل زددددددددد
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/106473" target="_blank">📅 21:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106472">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">😂
😂
😂
😐
🔥</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/106472" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106471">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آسانی زدددددددد</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/Futball180TV/106471" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106470">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گلگلگگلگلگلگگل</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106470" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106469">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH-2f4HYCYczh7ztGh7RJ1Waonolt9qgZD_tzUjlQEyDcBl1LVipLXsnVBbfqHmMGIYHlBID1FE9Xol3S_c_6FtMDVwTQw3wblJUNHD-4bZlPo4hyrq1FWeOgimp3xLbcqe9wl02aMPh2G3X8RZ3etdIGzq20-8oXojuHiON5wGf1TOuW54APy_bPpUKO1wpPrtrjEhHyo1_GFAFGL4bQJXtBM3Adyr3cDi5hLYt2pYjBTs2UifQVn0Yh76-1U9LIJatBHP-SORZC6uGjH4jr7O_iCUf7Ub_cZPliEBAJvRO5-IKrmMzfhYoxr66yPB6M3c4CbRIr6dEnPYqBoHw3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رودری:
🔻
فکر نمی‌کنم ما مدعی اصلی قهرمانی در لیگ قهرمانان باشیم!
🔻
این تیم هنوز باید روی چند چیز کار کنه و خودش رو به سطحی برسونه که بتونه قهرمان بشه.
🔻
فکر می‌کنم بازیکنانی مثل من برای همین هدف به تیم اومدن، چون به نظرم لیگ قهرمانان مسابقه‌ای نیست که همیشه بهترین تیم قهرمان بشه؛ این رقابت، تورنمنتِ لحظه‌هاست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106469" target="_blank">📅 21:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106468">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9jEuyk53AejOjB4zcF4k6Eggd8KSJpQayfH6Sn5tviMBvXybWcFyEbDB_CU09cQGE8bcBOHk2U93J1Su-ANnwRxQE1ajSDSz2uDELMnfvCz_1czfk0HFRm2I6izTTvMbNgnGLlnVKNPc73wWKGiJJ7WgmUK-6yGzALBdbZErQcZAE9Jkn6zBlRwSrqFjOUE1DJgHmSEN1XLVGkFCrlF2BuZejSkjJjpkEPeKFU6-ru8cRatlpzd-IXOxBRYk-vsyaWSX_0FEYD0fko6h3JZ3G4LD7UKz6JGgpBHmZ30Zlj5JyyfcYvEQ9wxiJyeytrtgxrjSGeHtQP9vtXctI0OFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇪
گل اول شباب الاهلی به تراکتور توسط سزار روی پاس سردار آزمون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/106468" target="_blank">📅 21:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106467">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5473152a76.mp4?token=Fm8mducix9Ns1Po3hbCfzgz-PS9ApGIG9ZL7M-Sm_UwN-y3UI2WeFFAFFhus6E15md-XunB5CFKGUCpSsqqeoIfwmOOrNgGF4IesLkprs8iWhu4Y-8SNR4D9sndcIy5GimZBz-Qg4o_cmLFqwOMM1QTLD8XPZN0Hj9YMW6zQj1PdHKe3TSpSNhFLL8w-z6J7q6iXoSmjgjqE-sUmoA9WhhStogGOS73j8IaztD2JazCYVaDqqIBfKxlin3kl5Xxb8gIclkGiHZTXTGNTWhlbsXGzz05FKZT1sFLlmmFuQFE1VR96ETo3VkGrZm2a4V0wukhgJIhhJb18kWBC3TW9Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5473152a76.mp4?token=Fm8mducix9Ns1Po3hbCfzgz-PS9ApGIG9ZL7M-Sm_UwN-y3UI2WeFFAFFhus6E15md-XunB5CFKGUCpSsqqeoIfwmOOrNgGF4IesLkprs8iWhu4Y-8SNR4D9sndcIy5GimZBz-Qg4o_cmLFqwOMM1QTLD8XPZN0Hj9YMW6zQj1PdHKe3TSpSNhFLL8w-z6J7q6iXoSmjgjqE-sUmoA9WhhStogGOS73j8IaztD2JazCYVaDqqIBfKxlin3kl5Xxb8gIclkGiHZTXTGNTWhlbsXGzz05FKZT1sFLlmmFuQFE1VR96ETo3VkGrZm2a4V0wukhgJIhhJb18kWBC3TW9Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شوت فوق‌العاده شیری راهی گل نشددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/106467" target="_blank">📅 21:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106466">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تراکتور تیرررررر زدددددددد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106466" target="_blank">📅 21:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106465">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/106465" target="_blank">📅 21:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106464">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61b23910d.mp4?token=g7nV2srlc1ehYc_y30FqbU1GyuS6pOQeZOanj985ra2OJ6lwQqLj-UqgvN72dH17m_bK7xxYwaZFoK1WMQXaWHj_64LGYWtwfcnYgTvpBwL7SN87TfIT4tcY_PcJ4IUmxEyIhhU5yBH6Zu2tPgTAhUlHHThQt71f7uzQdCOcHr4kvPkQQnh3_FKDrHewA1hybF0Hy-1B3moUVj8EBImX0Wsn2ke9ec-FNfi6ATC4SZE5pzS7fxobaW5rqBJbQxx07Z_KIrbVWBISrJDFMhV0MXonQhspWySAEEmFLABxbCDrbGLfWe0KWWu9h8gZlrE4PxUVb0sQLpsmRSbr3Oky_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61b23910d.mp4?token=g7nV2srlc1ehYc_y30FqbU1GyuS6pOQeZOanj985ra2OJ6lwQqLj-UqgvN72dH17m_bK7xxYwaZFoK1WMQXaWHj_64LGYWtwfcnYgTvpBwL7SN87TfIT4tcY_PcJ4IUmxEyIhhU5yBH6Zu2tPgTAhUlHHThQt71f7uzQdCOcHr4kvPkQQnh3_FKDrHewA1hybF0Hy-1B3moUVj8EBImX0Wsn2ke9ec-FNfi6ATC4SZE5pzS7fxobaW5rqBJbQxx07Z_KIrbVWBISrJDFMhV0MXonQhspWySAEEmFLABxbCDrbGLfWe0KWWu9h8gZlrE4PxUVb0sQLpsmRSbr3Oky_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی دانیال اسماعیلی‌فر از تعویض شدنش
ایرانی جماعت هرجا باشه غیر حرفه‌ای رفتار میکنه
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106464" target="_blank">📅 21:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106463">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX21c7K6ejhCbo13xZmuTFLEA_mbGjrTZg9wZC36lyMJgKxgxXtr0UCUyQBmceUhNWWBcqlMeWgI74ABkdfS797zR2A2rGkY43AAJmvHDnSrarJM34DaZKoH2YfHJ7Ep5iaAQEIPtJ9xR2eFwpfRB-XtoGek0ZL41ZwStimA_jhR8kDOn_qbp_2cZx0zVNXg3uTVw0TR-s2JautwDqZe-ZFBo8RzNPMf_0jgLgzO1Un7hvhKu_STT_0JopIIcx_evdbCeSpbY5tsqBe4nhu2J-fgOueqVZ62IBN3PJknHKSHvJuTxJgAFUNyCIft32GdmkHurdZzzHxqWKNBu97OBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/106463" target="_blank">📅 20:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106462">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e981f8613a.mp4?token=uMxN51QVTAoZsK8iKok-xZ3hINcbsz4lZABVps0WuOqOm2jTW3klVSHB84LrV8ShKhtLQLef6Z6UqsU51K33jflsDMo978ArBMOxRT8c5m8j4a2NsNGHpF2i5YHPhovVeNXUSOTF0oDia8OLqd6EwzN0IQAj4eX1e4TRhFDoE5z1LK5RHoNkScz3oYyvWJ5VqFqFkdUcODRxsn5ST2o3vsm81r6-Nd2g6NIDsrgP51enzoBTqbT-rnBsOFJ7mIziBiZejj6uzZ7kh1I8BT6lX_WFdFtzCvjYPEljBZwZm2QxAwX16mlqC8eSzbH_MIhg1_7Ki9MiHDzbmh-EWPCnag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e981f8613a.mp4?token=uMxN51QVTAoZsK8iKok-xZ3hINcbsz4lZABVps0WuOqOm2jTW3klVSHB84LrV8ShKhtLQLef6Z6UqsU51K33jflsDMo978ArBMOxRT8c5m8j4a2NsNGHpF2i5YHPhovVeNXUSOTF0oDia8OLqd6EwzN0IQAj4eX1e4TRhFDoE5z1LK5RHoNkScz3oYyvWJ5VqFqFkdUcODRxsn5ST2o3vsm81r6-Nd2g6NIDsrgP51enzoBTqbT-rnBsOFJ7mIziBiZejj6uzZ7kh1I8BT6lX_WFdFtzCvjYPEljBZwZm2QxAwX16mlqC8eSzbH_MIhg1_7Ki9MiHDzbmh-EWPCnag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇦🇪
اعتراض و ناراحتی عجیب سردار آزمون به تعویض شدنش مقابل تراکتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/Futball180TV/106462" target="_blank">📅 20:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106461">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co1n_Y95biydmCrdmNHuWDvmyWs4r-HsLQ63rL1Ypd-dZns2LyZyYWah54SyefKcs7ce6iEvEDQkoEeH4-JWhLmVUoYCoHwbw6xRfKoq7cz6CmXeObVvDoKfkf5RlDYUVoMvrm0T_voDMEkRbKo4gfIiyuzKmjq4cpMZN3AK8rbunHxGv4b9gnGiUDIPEiGxqVIdFWNzSopZXId5OmY6zbKkZvUChAnEL2PudZ47dSn3HCEDUoFTOyIemSsW6-Rxo1Hz8aPkH_Fr8B1yty5Yr6aDaQ8f-aU2BTMiVDqCaDuT5tB7bjp7nEEUXg2sBlEO5C7022zy71AJoeOyHkzMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
شماتیک ترکیب استقلال مقابل السد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/106461" target="_blank">📅 20:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba7d85c2c.mp4?token=rG4zpE-kgnwBk5Y67LisFFsa9A-N5BwIUSyorkYH4fN3UBxo3i_dKRAyD4LLMqL9xfxJQAD0hIV0BwzsvWnzsUqyFJGPY0lTBkJzxPZADR7HuQ0TEyelPSKaY6LFRwkOMdSeA0_xxrwz1gaRTjLDYT2Ki6dDW4dHBW_g8U0cX4dTuG-xDQGUPi77TLYvpm2L-ABhb3dVZIA-jlocHS3z_LwCzckEbULNKKb6U_1g3k60UMRNYq_S2IsHdjgUTcfM_pWAKsx3d8E0wsEWZZn6rxm_ovIE_ulOEPTAjIQ8pHiq1wH1Tx0i05_vckvy9TUdpLYDB7HUuMeUlbIzDdBaKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba7d85c2c.mp4?token=rG4zpE-kgnwBk5Y67LisFFsa9A-N5BwIUSyorkYH4fN3UBxo3i_dKRAyD4LLMqL9xfxJQAD0hIV0BwzsvWnzsUqyFJGPY0lTBkJzxPZADR7HuQ0TEyelPSKaY6LFRwkOMdSeA0_xxrwz1gaRTjLDYT2Ki6dDW4dHBW_g8U0cX4dTuG-xDQGUPi77TLYvpm2L-ABhb3dVZIA-jlocHS3z_LwCzckEbULNKKb6U_1g3k60UMRNYq_S2IsHdjgUTcfM_pWAKsx3d8E0wsEWZZn6rxm_ovIE_ulOEPTAjIQ8pHiq1wH1Tx0i05_vckvy9TUdpLYDB7HUuMeUlbIzDdBaKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حضور دو هوادار عراقی استقلال که برای حمایت از این تیم مقابل السد به ورزشگاه آمده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106460" target="_blank">📅 20:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616b69bd7f.mp4?token=Y9CsXXKSBSoTlqWKBtYeIOtI-temldof7UmWF9YFPnx9aNd6ebq9jqHtAYruyh9ZJpiRp9ig_SvBZouPQtL2R36QOKtOsAlNXNOad623Ro-mzCf7UDZZqiagDSetmDM5kwXOi0JHVh1oK5XD5gDf4NWXOqYxQ78v7XJ-Ua6tY3yMxZltR0Tfs-_pIW2tLwCDqjqqx--s5_ZPcwpieuBLYrX_mzhQ4KLVMnqAGHlKqdNWofGIqr46o8EpusTZvWfAWgLOQ0dQMhrJcsviuKaU2ey4Ter1QGqQhN0HKxOXFrksAWu6lGc80MpXWaEkNeRUNWH9VYtM5M1jhpFw2nJyIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616b69bd7f.mp4?token=Y9CsXXKSBSoTlqWKBtYeIOtI-temldof7UmWF9YFPnx9aNd6ebq9jqHtAYruyh9ZJpiRp9ig_SvBZouPQtL2R36QOKtOsAlNXNOad623Ro-mzCf7UDZZqiagDSetmDM5kwXOi0JHVh1oK5XD5gDf4NWXOqYxQ78v7XJ-Ua6tY3yMxZltR0Tfs-_pIW2tLwCDqjqqx--s5_ZPcwpieuBLYrX_mzhQ4KLVMnqAGHlKqdNWofGIqr46o8EpusTZvWfAWgLOQ0dQMhrJcsviuKaU2ey4Ter1QGqQhN0HKxOXFrksAWu6lGc80MpXWaEkNeRUNWH9VYtM5M1jhpFw2nJyIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇦🇪
گل اول شباب الاهلی به تراکتور توسط سزار روی پاس
سردار آزمون
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/106459" target="_blank">📅 19:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106458">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پاس گل از سردار آزمون</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/106458" target="_blank">📅 19:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106457">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">شباب‌الاهلی زد
😐</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/106457" target="_blank">📅 19:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106456">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگلگلگل</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/106456" target="_blank">📅 19:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-t9lBwOSt1ruHK8lNrcG0JVQKa51HJhIvuei3KCD56l43BGkK73EhJmj5Qpi0giP01sN8UMxVG79OCuw0WpYh92LIQ-XQHfunChkdYbJsZoto43WxhJ3TB6_9LviyjbQjvqXx0Gx9EmZbrGtJ-6Zv2sRIBxo3b29F9sxXJDnQQLOuLbanztLa4yJ01mEk1Tq6mvnA_TNtqxLUjmBUOoqySUVJiMfzE0lNh7zDgVVQrAU-JwYFSncaqXkm51zuxKoBlvB9fSEkoNNuErsro4uxTi_XNAiT3IaMr9MKyYbOdgYfgaHLsx3PN64l6vDM-fGrA0xAdw8C2z5RFuag7fsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
ترکیب الاهلی عربستان مقابل پاختاکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/106455" target="_blank">📅 19:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تراکتور یه گل خورده سردار آزمون زد ولی آفساید شد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106454" target="_blank">📅 19:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQwp0EgvlmQTuE81JA1Ziyg5aODtQW_92pQ1PgHAHvq7b1Y3BaaPMvxZZu2_Ed8P5wwz_B6gozGIfUfpSGvNKfUg-Uyo-7Ogff5m3kDTVTca8mA6d_euoH2qZB159i6oYuecHFV8GlBohr_yhvWHgc6f0RAPxYZsWUgifGaCFsUcPLRsf4cBBI8Ud-1f7lXv1Pny1GdYolKiPsdmzSQqJ-fTRBbnCWLdqd9dD0D2cbrKu745ZGtDmtbwUWGPhMLZskgCuDkJvsx20wqDDvgiQ7hFsaLKo_0NLHouyMoeN8budhYvd4EMaKck_vAqzE84_CFGWkHpayy-tqbP_wty_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اسپورت: لیورپول در نقل‌وانتقالات ژانویه برای جذب بالده از بارسلونا تلاش خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/106453" target="_blank">📅 19:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a6dd2ed9.mp4?token=LIIy8rgkF469zwEOq9LG1A2kAAvsLQTDPvT_4mXM4lUAAS1J5i-PeIuD4G2wdfXj0SqD_NPwfH8MPreAZWXtJtUa6lnOTlwTdmYo0Ss0_Zkr36chi2cnuTyzjCu7f07QjMJ6XPpgmhcib8t4XHyettAS90VnpnFJR52r3bMPF_BN1y0VXaVsnVbSkjKwuqzLD2nH9ek-pFL-Z9SbJxoTyn4Mv6rMMMUjUuDn1ZMPqzzkobFoMsenxnuFu8FsmZrAxcvBSIBrayRrL-4anV5Ri2T7tZXBGOs8iCBx2s5BgLMR8P36RYSOfITzPaYOIyTrtFEne_r0koQA-lU8HhSozQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a6dd2ed9.mp4?token=LIIy8rgkF469zwEOq9LG1A2kAAvsLQTDPvT_4mXM4lUAAS1J5i-PeIuD4G2wdfXj0SqD_NPwfH8MPreAZWXtJtUa6lnOTlwTdmYo0Ss0_Zkr36chi2cnuTyzjCu7f07QjMJ6XPpgmhcib8t4XHyettAS90VnpnFJR52r3bMPF_BN1y0VXaVsnVbSkjKwuqzLD2nH9ek-pFL-Z9SbJxoTyn4Mv6rMMMUjUuDn1ZMPqzzkobFoMsenxnuFu8FsmZrAxcvBSIBrayRrL-4anV5Ri2T7tZXBGOs8iCBx2s5BgLMR8P36RYSOfITzPaYOIyTrtFEne_r0koQA-lU8HhSozQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
بعد از انتشار ویدیوهای مربوط به عملیات نجات خلبان جنگنده سرنگون شده در آسمان ایران، این صحبت‌های چند ماه پیش نیکزاد درباره این ماجرا در فضای مجازی دوباره وایرال شده است!
نائب رییس اول مجلس معتقد بود که اصلا خلبانی در کار نیست و آمریکایی‌ها برای بردن اورانیوم‌ها آمده بودند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/106452" target="_blank">📅 19:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106451" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/106451" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106450">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHmVpEeL2orMxRWhe3J8WMilG6rZNXQjlnjuEgPtmZj4wSQe9U1DSnRkbtH6akEpM2CYLHVDONP_uFIlOCRVJgmcKp7Wz36yKaS8tFI9Dn78rIjkr2qn8lEdZHxMxcJc1S2Ami-qIvbIf7GX-KnVW2bMOqyG8Rnj5T-VwKT6LYnyP2z8MevvpjknEVYORZm7enXk11LT3E323jcoGzzDL0Hy-_0Om91D1CRNVo_zgJIwtXuYq9YPCuphLcY-YbUd_5x1QXThZOpsHfOCSeZJcyfVhbChwUWIKQ8Os2zSM0i-ut2Lf8rcSA0PKrQ2byEL4S7C57Rhcw9U1eUpkqTfmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/Futball180TV/106450" target="_blank">📅 19:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106449">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COl9QceX657YD1wRGjXBQCT419j5jNDeDfJnb_0eEblmAUuK8tMpLybYj7lPsZwbrFqw9_9atYAqibUCKnZkUwrGE8eBS9_gYRLXj1CGphMyVU7p6cdLt239ie0JUCOikqXZHoxDaH5Dz0zV0gHaNn0XmsGZqEFzcZgdkxWt6hMYNV_W3kP8vbcH0Ej9MW0s6-Q_-2ybAba1GEBx3yFl4dEJts1klUcjIFuvikUahqIUhvdS_keT3tQK5xtAhNHd5oylXcX5RRYQvmK7L4J4Pn9gFc2lTJQ_xNxpzDDvyrDHqU9_B-h7lpeTdc-X92kw3YTtG7GpxXC11QbTiwMA-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
ترکیب تراکتور مقابل شباب الاهلی امارات
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106449" target="_blank">📅 18:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106448">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22236f4e69.mp4?token=Ga631kyoM_P_JdVpFhKc5Zak54-EhDBFMqtsW8KhjPPCm0jp2Kl9MPAjl0sgKWmFPjQ8H-uN3Laj4fZq4wMAQcXxnXqyWhSKIGDS8ud5eZKoN-z3zrAnkFI-lR13acXCE1Awa-eDljuDj5BAkNx3GavXWFZCoPd0MtfLDHDVjOTM9DjtKOXd_t2LsS6l94cYBChRCe4Yfya6-RTV9laqqBSsGypYGlwkbN6-RrwrphtI32puDQ22jmEh7tIqGc3UU6ozcpmgr_H4TGnwIz2Plh1vvzYOdeID0PzXLl4cnKoFyc7_42dXx_PVMopafRO0dL3mpzO_g8G9ZLIKqWA2qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22236f4e69.mp4?token=Ga631kyoM_P_JdVpFhKc5Zak54-EhDBFMqtsW8KhjPPCm0jp2Kl9MPAjl0sgKWmFPjQ8H-uN3Laj4fZq4wMAQcXxnXqyWhSKIGDS8ud5eZKoN-z3zrAnkFI-lR13acXCE1Awa-eDljuDj5BAkNx3GavXWFZCoPd0MtfLDHDVjOTM9DjtKOXd_t2LsS6l94cYBChRCe4Yfya6-RTV9laqqBSsGypYGlwkbN6-RrwrphtI32puDQ22jmEh7tIqGc3UU6ozcpmgr_H4TGnwIz2Plh1vvzYOdeID0PzXLl4cnKoFyc7_42dXx_PVMopafRO0dL3mpzO_g8G9ZLIKqWA2qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حسین زاهدی جانشین سازمان وظیفه عمومی ناجا: اقای بیرانوند از یکم مهر ماه باید در اختیار یکی از تیم های نظامی قرار بگیرند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/106448" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106446">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2QuxuTTgDFwMimKXwNXwEVFZ8g2F7xCaWmoZzLdeArxeMsX0NA0XIZTMC6kd3VyZXjg4157-UguBeEEy9BTEHZmnlfuG_jJyIOU9rlfJWSNM-5vAGYQ6V6DVGcTRYriF1jT5vnRnIF3aPHcoB4AJFOpEr3aYBSOFmjBQPDkqQkVKj8YtMLW6SW56lvagNqeNw5Sm-ijtOYIZJKTRmb5Xn50AITo4IWk_yYxab-CIs5wTVvNdmCTTa50rHP-ngxyagfA4dodj8SYnHP3NsEhXIckMoE3uYVDvukOd44mZn0Ca_TTW0kVSromuTo5VjGR1cgDkRBBV9nNJHJGbQHlYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XqFqI4943z6WVnYfazbqWQhEddN7ODc0C2AoHnNMLAuoKusIr1EZaPzDG3lGUqVpG0JWXP0x6VyWks0_QxDRWsWkViXJFlvLh0YvUuRKYnzFftHCUiiN7tvMAiX3bwXnTutmyBiZK7yvYMa3Uwlvs7yhhajCol3MyGCIELvLY7lDPut1jftTaFsY16ly0k1R_U69sRwokx7lvpT0ec0U90nmw3Msu9rq_iqwS5sj4PiKx97cMJPRiPaspECowIWecqP3-J2ojUlk2-SdadhHqb2CPXi5LBnLxcf6JIozF8P4MGMG9JvD36MbqK9VLVyVe0oNsg3Wqgm8_5AlhwPfHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
⚠️
صفحه اینستاگرام رستوران «دستپخت بی بی» در تهران، به دلیل انتشار یک استوری با نوشته «هیچی کتلت بی بی نمیشه» به همراه موسیقی متن «بی بی گل» از معین، به اتهام «انتشار محتوای مجرمانه»، با دستور قضایی مسدود شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/106446" target="_blank">📅 17:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106445">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8d5f06714.mp4?token=qUJeDmF4TDiFNY8D5mBxI1r_71Ojjgp-6-EV9Ilz6rsp2fD0GeG6ZSd6ovr9KTTpmD5LYv45uCcsE2ajKdOV6j2oQBehLi4EfIftHD0lUx_9FHIWGaEtryHLqlB2zOsTGOFIds2KLFzNV-2inVgpb9vuWNYzOeO7Vs--UQTjA-0hMIJ65zo41zHcaxYuxceXCt_faZLK6NH-Y7iQ3s2eeFLWWD3rs-QTFp96mEk2IS9lFH_4mrSKHdPxSWp3hHRBlFQN45uOkHH7Nv3mJ0rwLuxpmlfv5ljERXWamUunkYq3GFbsEj92W5rzuhyPjIwz9-puViADR_FQcS9T5XFqNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8d5f06714.mp4?token=qUJeDmF4TDiFNY8D5mBxI1r_71Ojjgp-6-EV9Ilz6rsp2fD0GeG6ZSd6ovr9KTTpmD5LYv45uCcsE2ajKdOV6j2oQBehLi4EfIftHD0lUx_9FHIWGaEtryHLqlB2zOsTGOFIds2KLFzNV-2inVgpb9vuWNYzOeO7Vs--UQTjA-0hMIJ65zo41zHcaxYuxceXCt_faZLK6NH-Y7iQ3s2eeFLWWD3rs-QTFp96mEk2IS9lFH_4mrSKHdPxSWp3hHRBlFQN45uOkHH7Nv3mJ0rwLuxpmlfv5ljERXWamUunkYq3GFbsEj92W5rzuhyPjIwz9-puViADR_FQcS9T5XFqNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
💥
✅
شغل‌سخت و زیبای عکاسی مسابقات ورزشی که همینقدر ظریف و تمیز باید انجام بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106445" target="_blank">📅 17:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6637c3eef7.mp4?token=JNe5FfGdsc3DxPc-Nv8qmKfFd7Jf3WXC9J-VNZ4hrM3xQpqNGhgX7UUZXIBz_Xdruov8F3mrZpWAsw5V7b0adTlUnoxxAYVjRZr7EmrTktWI49FTxJgJgeeI1kwRDWBua4z3ezcdfnvPbp_rBm0eaSbuQuzxhhXZikwgFw-hD4oDPy3x2wEaTc63aL8r2KAawbDDPfqme3vtD-NROAnmdJVhgXQRm2Xd_44QuGV-yYeUv74zUFuVDrgQT_764EnNHWjyF-5X5PkLjAt0mA8AmFnyjC1yQJFR5nKaIHotbFTV2AYpq8rvw15UKqd-eNToBvd0eKIyjQvDLB3K7__CiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6637c3eef7.mp4?token=JNe5FfGdsc3DxPc-Nv8qmKfFd7Jf3WXC9J-VNZ4hrM3xQpqNGhgX7UUZXIBz_Xdruov8F3mrZpWAsw5V7b0adTlUnoxxAYVjRZr7EmrTktWI49FTxJgJgeeI1kwRDWBua4z3ezcdfnvPbp_rBm0eaSbuQuzxhhXZikwgFw-hD4oDPy3x2wEaTc63aL8r2KAawbDDPfqme3vtD-NROAnmdJVhgXQRm2Xd_44QuGV-yYeUv74zUFuVDrgQT_764EnNHWjyF-5X5PkLjAt0mA8AmFnyjC1yQJFR5nKaIHotbFTV2AYpq8rvw15UKqd-eNToBvd0eKIyjQvDLB3K7__CiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستر این فصل هم آبیه.
💀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/106444" target="_blank">📅 16:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/300398c1b7.mp4?token=TSSXdburu4ypTgL8Wo3PRYaGUOxojwGtC4ybN-nIt8HsatMVNWQN2uYbyTJyTrt2K9lilqIGm07voKX1Ph1SvMiycN_2uL1dETqYDqSEtVkdZu-aX1tANOai8s1RJHxE8CCjYcjX9aLEddME0bXMIeQHm5n-NDkfErF1Zr9v3rgixcMVQCrHZeQNwUfqO59KgDQ3XpgEAZg-HXNxD0wk--cmP-li44GQxGBsZJ0MuA4TAvFZMIeK11lY-iyU_44DF6Zd8Hj3kvlFj0iI8J4CHdQGrLQJdx5dpBS1erNMMcv5S24fyEkGCaKh_hqO2O3QjhTLeVhtKDHGmJPezO4big" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/300398c1b7.mp4?token=TSSXdburu4ypTgL8Wo3PRYaGUOxojwGtC4ybN-nIt8HsatMVNWQN2uYbyTJyTrt2K9lilqIGm07voKX1Ph1SvMiycN_2uL1dETqYDqSEtVkdZu-aX1tANOai8s1RJHxE8CCjYcjX9aLEddME0bXMIeQHm5n-NDkfErF1Zr9v3rgixcMVQCrHZeQNwUfqO59KgDQ3XpgEAZg-HXNxD0wk--cmP-li44GQxGBsZJ0MuA4TAvFZMIeK11lY-iyU_44DF6Zd8Hj3kvlFj0iI8J4CHdQGrLQJdx5dpBS1erNMMcv5S24fyEkGCaKh_hqO2O3QjhTLeVhtKDHGmJPezO4big" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇮🇷
وضعیت قرمز نفت؛ آغوش باز آبادان برای بحران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106443" target="_blank">📅 16:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UP2mwUbsdtbUj2IBaSFjgC99PJxs7y4rjLEOnPqaj0E2xN7GO2gUiOyERLCoeQ68zGDFOA0WBT7B5l6Bn0dVZMh9g3RuMc4nXnZG22c8D10Fo9-2k1LY_WzCzKZziar2Sc1nm12ulV9ojJTczuGkOwq91naKYDtm2hk6snWz8kw_-VuDHntQA_dQ8hCCcHSnAQCi7y3aB3lnxhP_GrsNY-LE9OM-dX_LBb2M7mBjYwdfErn62btQiGx7KNzFnR5wfKiaHgcQvRGwHzrnnok9wcYYo_deM56xoC_uS-Am5KGSVC1ko0mmoY7aFgajvm0XCXdaU6al7AHXCi7wbXe-Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
تصویر جالب وایرال شده از رشد عجیب و غریب پسر ریما رامین‌‌فر طی ۵ سال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/106442" target="_blank">📅 16:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8JRBX6IUH7lgvO48uUiHMLIxhE3iArFye47if4iKP9vr1R8KMNCmXB6OFxOf-x_50k-77wY2BmPxPq8A2igkE3a8XuAXYYhAtsjTkFduLqQn3Ey5cx1O92mlcTvrK4ggwhYOOeu35pO53zTGtMKAOJ9cHd497WnFBoygpunhOnfhTVb3zyvlnAlkW2ITFqtHyudaPrUyc4uWaJSCk_obiFJbeVqecBT8fPL1cNyiR0aXyF-wHMzF0C_OzTrKaqZb4RuyOg2dZ3B8HjWLS2XbmLeDUnwlfIvbT7A-tVzyd3OSU4ZqzqUWCkcKe-kMhg5NWBCWpFJrIB8dThyXMpI5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
عملکرد فاجعه‌بار تاتنهام فلک‌زده با هزینه فوق‌العاده زیاد نقل‌وانتقالات در شروع فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/106441" target="_blank">📅 15:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106440">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f4de3a2c.mp4?token=erPePej7VV-cY5w-2NzvJ8BARYes0s9o0iVDU-zbRNCFpkbU0uMzHQaPB2dnrMiA72rz3HmDMcwz94Pi_O8daMYSVQsVBZnyUzd3dZ1_5OQVFq8J8StdZ3wLmrcWRiJb7CJ9bZ5l5WiQIa55sBrZMIJmCd_orSITEYl2lUmpfwpy9u7V3YeifWyOkWK4EzOFzZ61ajI8YV6k-WwkXlhONgbJRnRMGRAGZ9nSdIF8pPnARrnd-tZNFCQqFGVZa28-R1wi4bnBUQUm4Jt6d-dauwCf4d4FBkwYl8OuQZ-Rd1dwN_46qhxoG6JgGhxDxJMcIWc29E1XOqTfluFNDYiKiCuiirwK5whIMtNlNWDc47aFAHnckCnIw_Kb9eyA8jJ_a5lCKUKDkphmXVI3IBj9Sm-HDcdtuoYXu8rjQPoWiMltOdplMruFApL7r0iXRKFpS1o_augW3bokyHxopipnkUQlLjeLaPO7XOKWgl8_DztH6qsp6G0mKeO6EUM_U2gZNoVKTMURr1NXjOzJ9cFIzJ3iE13sBGL8Zz2Q-6B0XWI1GA89LuvNsplx8kHRVExU0zR09XlTU_nkv7DTA81n8DFcXEmJgfnIOCYNUDEKYisTXRcwIRmnYc1-IAVgF5k-rbp3OYcmYEvfIwCZ-b_gVx7GH527R_1wwrP0GTRF1yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f4de3a2c.mp4?token=erPePej7VV-cY5w-2NzvJ8BARYes0s9o0iVDU-zbRNCFpkbU0uMzHQaPB2dnrMiA72rz3HmDMcwz94Pi_O8daMYSVQsVBZnyUzd3dZ1_5OQVFq8J8StdZ3wLmrcWRiJb7CJ9bZ5l5WiQIa55sBrZMIJmCd_orSITEYl2lUmpfwpy9u7V3YeifWyOkWK4EzOFzZ61ajI8YV6k-WwkXlhONgbJRnRMGRAGZ9nSdIF8pPnARrnd-tZNFCQqFGVZa28-R1wi4bnBUQUm4Jt6d-dauwCf4d4FBkwYl8OuQZ-Rd1dwN_46qhxoG6JgGhxDxJMcIWc29E1XOqTfluFNDYiKiCuiirwK5whIMtNlNWDc47aFAHnckCnIw_Kb9eyA8jJ_a5lCKUKDkphmXVI3IBj9Sm-HDcdtuoYXu8rjQPoWiMltOdplMruFApL7r0iXRKFpS1o_augW3bokyHxopipnkUQlLjeLaPO7XOKWgl8_DztH6qsp6G0mKeO6EUM_U2gZNoVKTMURr1NXjOzJ9cFIzJ3iE13sBGL8Zz2Q-6B0XWI1GA89LuvNsplx8kHRVExU0zR09XlTU_nkv7DTA81n8DFcXEmJgfnIOCYNUDEKYisTXRcwIRmnYc1-IAVgF5k-rbp3OYcmYEvfIwCZ-b_gVx7GH527R_1wwrP0GTRF1yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
▶️
ینی این ویدیو حق‌ترین واقعیت درباره زندگی اکثر مردم در دنیاست. از دستش ندید
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/106440" target="_blank">📅 15:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhIQdyb5PpBZD8deNDIe5UiKy1DWBbGa6UoFIO7YRFtN3TilfPxs1NUkQtQFOGW2PaZQSrfeZARre8p0gJYBE8lEF4xsRuCp-9J31b1R5mdmiD5-LIyBqXMcUjqYil-iovd6Q27LxNSwJI30Ucb3hEwvgJ9vwOW-649EITwis8g3RpxbfKiTKcpXvILbqsz8jZBpsKxiGRd_oQ1xwi_GuJdJZb7EXlJVX9_QS4dlCXrdA_fysnR7fVJuHhAYHbsko02wup_auCf3dXb6BZsRh7GajdLCP_lgkA89o6PA3A71LXz_GzoJtCLfy3KvEZ7xrUjQstuZnRa_bDND180gmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
📱
🇮🇷
آرزوی موفقیت رامین‌رضاییان برای استقلال پیش از بازی امشب با السد قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106439" target="_blank">📅 14:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106438">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62958310f6.mp4?token=izt90cVuYfyTYnhpHLDtnMZmmPblGmYACpDaHwsswi54XOnh7UNMFL_YtCyZwnM_MXL5it5LyyiQz4zG5yFn_CsIuSbSw4ZQcrBNvG3UjNeDATp6aOTQD-IY5PwrsFqvEhuXDXOd5X9MzaSraFWs54_eC0crNf10pd-ixHn8UxAkHtV5zbK_3tAdlirBS1ILYeFaf6KfU4Ddd940zUg0Z1Ly1Jv2n73wYy4E9Nn0e7A8V26cF9Cp0CT2S8yqDUva6I1ywmft6G8zJsB0bosz4CWQgxyioBYMvPemcQRtBtslfhCZjHM6kpMQ2Y84PTCTHMYgSvnD06p7FGCOUkT1zlM8nd1e7q7J6A6YzZXbUaGNwvK0i_L5sPnOleaN-YcAq0tacUwx8-367Q-OP62jFEKbdp-wBeARrv2Ilh-SIgvLtIA3yGUmtYFWQV6J7nzS4w_qNsyd7v22QrojBWqBLe8EVbe8vsdiUoTuyRCmNSHbpWz67LnV4H-1c9VEng4muHoAUKG4tDoc7fGecnvJPdKhPb8Qmuca8nuMmP7cRNHrWh1KPLKTa2WVLJlg4ASyxHjcAntbXa6YFwjblqnFFIw64qAqJ85kx-AhhaZ1aLI7z8gySplqpGNL2hXqpLZr8VUfusDcnfM4ZZNsilpHz7GZ2lWfBymIPloPZYRbi8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62958310f6.mp4?token=izt90cVuYfyTYnhpHLDtnMZmmPblGmYACpDaHwsswi54XOnh7UNMFL_YtCyZwnM_MXL5it5LyyiQz4zG5yFn_CsIuSbSw4ZQcrBNvG3UjNeDATp6aOTQD-IY5PwrsFqvEhuXDXOd5X9MzaSraFWs54_eC0crNf10pd-ixHn8UxAkHtV5zbK_3tAdlirBS1ILYeFaf6KfU4Ddd940zUg0Z1Ly1Jv2n73wYy4E9Nn0e7A8V26cF9Cp0CT2S8yqDUva6I1ywmft6G8zJsB0bosz4CWQgxyioBYMvPemcQRtBtslfhCZjHM6kpMQ2Y84PTCTHMYgSvnD06p7FGCOUkT1zlM8nd1e7q7J6A6YzZXbUaGNwvK0i_L5sPnOleaN-YcAq0tacUwx8-367Q-OP62jFEKbdp-wBeARrv2Ilh-SIgvLtIA3yGUmtYFWQV6J7nzS4w_qNsyd7v22QrojBWqBLe8EVbe8vsdiUoTuyRCmNSHbpWz67LnV4H-1c9VEng4muHoAUKG4tDoc7fGecnvJPdKhPb8Qmuca8nuMmP7cRNHrWh1KPLKTa2WVLJlg4ASyxHjcAntbXa6YFwjblqnFFIw64qAqJ85kx-AhhaZ1aLI7z8gySplqpGNL2hXqpLZr8VUfusDcnfM4ZZNsilpHz7GZ2lWfBymIPloPZYRbi8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
سوپرایز دیشب اعضای تیم‌ملی کشتی برای علیرضا دبیر به مناسبت تولدش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106438" target="_blank">📅 14:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106437">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b720c6c51.mp4?token=JGf0uLQCpnvJ10CagbbJ0VPH3c2azPTNbZBn1VwDbdj4T2Y8-C5_g4Ce7Y4HBbc6H0hCebDaS0fYvN-4NSw6ZkFmWIQLyxNK6O_BfzRqxHtblQVD3cUcq3rxs11EQyUbjg4kxi0PGNh1xevePnyTC7eaLXpsEFylk_SmGtFxIBacSzZp5nvEhcENb520tGHGNmudd0anZl6djKDG19X0zsB6PjpRwxb9cWtHHnyAV6XCSKMgkQgm9T9Dvjt60CWg-mTnUPNMkzs_coWynpLvcVyf5cPpxPbWhzoBYDUZI9w5uyrSpt-x0ujoEZAxDLoo86PC7hta-21emgajm2vPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b720c6c51.mp4?token=JGf0uLQCpnvJ10CagbbJ0VPH3c2azPTNbZBn1VwDbdj4T2Y8-C5_g4Ce7Y4HBbc6H0hCebDaS0fYvN-4NSw6ZkFmWIQLyxNK6O_BfzRqxHtblQVD3cUcq3rxs11EQyUbjg4kxi0PGNh1xevePnyTC7eaLXpsEFylk_SmGtFxIBacSzZp5nvEhcENb520tGHGNmudd0anZl6djKDG19X0zsB6PjpRwxb9cWtHHnyAV6XCSKMgkQgm9T9Dvjt60CWg-mTnUPNMkzs_coWynpLvcVyf5cPpxPbWhzoBYDUZI9w5uyrSpt-x0ujoEZAxDLoo86PC7hta-21emgajm2vPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کری‌خونی سمی هالند بعد برد جلو یونایتد
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106437" target="_blank">📅 14:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106436">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbe5d1d200.mp4?token=hgOJlmbh3zXFuHAKelNh4W1XUSxgqQJ1yFqj1qLPa4LuWARqGYg2kloWnSruRH9EPCI_6YiYobbPbz6rsgMHXs_c0yUB5KuXQG_TyGos6681QdPLgsyYJo1JjGRFwEq7dbhExZA2FIGOTlx1nhtJ3HYauDbBEqGhlvalw5Sdd9b8CHY-4_qYWntu0zDZ94I1nGo5DHdgldaqz06-uICsKfF7qKSZeRT7pREwF076Fmr_n9DxQ-1NlGk52r_LnO4AONEyBXkfnXLJJxwqzMGPIjbKdqNbMmMKv3E5JeoqssaMnmIzRNNw2v0ka27cAGQE2GGIa-n21ZKivkW9D0QdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbe5d1d200.mp4?token=hgOJlmbh3zXFuHAKelNh4W1XUSxgqQJ1yFqj1qLPa4LuWARqGYg2kloWnSruRH9EPCI_6YiYobbPbz6rsgMHXs_c0yUB5KuXQG_TyGos6681QdPLgsyYJo1JjGRFwEq7dbhExZA2FIGOTlx1nhtJ3HYauDbBEqGhlvalw5Sdd9b8CHY-4_qYWntu0zDZ94I1nGo5DHdgldaqz06-uICsKfF7qKSZeRT7pREwF076Fmr_n9DxQ-1NlGk52r_LnO4AONEyBXkfnXLJJxwqzMGPIjbKdqNbMmMKv3E5JeoqssaMnmIzRNNw2v0ka27cAGQE2GGIa-n21ZKivkW9D0QdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇮🇷
🇶🇦
آنالیز اکرم‌عفیف ستاره السد پیش از تقابل امشب با استقلال در لیگ‌نخبگان آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106436" target="_blank">📅 14:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106435">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGVNO2WXS2DHTcsOyMhk0CxNjYp4ZodMgI-NE1GYKcMTd93Ro3EQo-6EUS54B2BUpQcqYOpMGXwsACWAllFieI9cFtGTes00W1VNqYr0xM7UXVUbXLg6rpF9rXFumSwNPMnX9fMWAQByFlA5Ct7acv-CD7y2W3ipfndEsvEhDQNJ-B11-bIHSg9eTh0RoPYUjU-fi3mXN4jDNndKhx12EBU53q_oF_arPpY33PS96zX_sE-MuoKir6BsczA57l1f0t1_uvSwqow4rkGdSRxeJARJPPaD77oERv3ZwbsiTjHnHHQa7Z4Xo0JOP5DyjjZZj1axvq46Tx-lFr1ua3noeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👍
👏
سعید سحرخیزان، مهاجم استقلال ١٠ زندانی جرایم نقدی غیرعمدی رو آزاد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/106435" target="_blank">📅 13:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106434">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b9165423.mp4?token=iGeuszgOeDFt8q97Wh1kR1qYqwEv3nDDaSeDESyN5FKZHXd_0YffPZW0XW-vjcb6jFjpRJXJAboshJSy3iRdASp4IC9qPzrtqJE6W_8T0jX0cXTWQzmVR8FLx7MDgDq7M-dItBgmSfZEKArTvjWpVsUS6RQrMEKpQed3qPusbCbCXDeObWLrPdpATGO1vv6cvYqAApvlFl0knaE5D6RWeTpDxc-hIy5Yq_EHbKaxf0skipe-CwgUTx82QYEL6ZfnjG0sVJRfdeviR5UaubnhyjvR2aZFwegPxdMKN1gmuSDPX-lpDL5FFodDbBzEdMNlNpfW5dM3qn3vScGtXnAS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b9165423.mp4?token=iGeuszgOeDFt8q97Wh1kR1qYqwEv3nDDaSeDESyN5FKZHXd_0YffPZW0XW-vjcb6jFjpRJXJAboshJSy3iRdASp4IC9qPzrtqJE6W_8T0jX0cXTWQzmVR8FLx7MDgDq7M-dItBgmSfZEKArTvjWpVsUS6RQrMEKpQed3qPusbCbCXDeObWLrPdpATGO1vv6cvYqAApvlFl0knaE5D6RWeTpDxc-hIy5Yq_EHbKaxf0skipe-CwgUTx82QYEL6ZfnjG0sVJRfdeviR5UaubnhyjvR2aZFwegPxdMKN1gmuSDPX-lpDL5FFodDbBzEdMNlNpfW5dM3qn3vScGtXnAS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
▶️
طنز تلخی که از دورهمی به‌واقعیت پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/106434" target="_blank">📅 13:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106433">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df19a571d9.mp4?token=fQGzQqKLf2U9JnUh3H4An0q3BmGUOTw-ZoxbaaoQlcDS4jk0KuD-iO54qvXPp78OEmGpjEHK5X6PlqMIqz6EtwpRkvVX-B1tR1BQFj9qnPolgBUVTjJN1hUsU3xhkz3levY9GUrusN_c2sUGSR2ftVp-AEvHinUVdM03D24VMEdOYctpWCWVVBP0wyGWLFeiOG8YbQrug-2HeWxrcPq2AOkUC01IJzrhZQROXaqYYehme8X6bMnPAMIyZWg4D4kGOXXiobonFKABIS2Jsvr1DCuLzxjKhgOb79jIPz8xfZkrRE9CvzszXafxBtYohXCsd9-ry2YjLy7ijDe_6JIDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df19a571d9.mp4?token=fQGzQqKLf2U9JnUh3H4An0q3BmGUOTw-ZoxbaaoQlcDS4jk0KuD-iO54qvXPp78OEmGpjEHK5X6PlqMIqz6EtwpRkvVX-B1tR1BQFj9qnPolgBUVTjJN1hUsU3xhkz3levY9GUrusN_c2sUGSR2ftVp-AEvHinUVdM03D24VMEdOYctpWCWVVBP0wyGWLFeiOG8YbQrug-2HeWxrcPq2AOkUC01IJzrhZQROXaqYYehme8X6bMnPAMIyZWg4D4kGOXXiobonFKABIS2Jsvr1DCuLzxjKhgOb79jIPz8xfZkrRE9CvzszXafxBtYohXCsd9-ry2YjLy7ijDe_6JIDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
وضعیت هوادار شیاطین‌سرخ بعد دربی منچستر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106433" target="_blank">📅 13:22 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106432">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEBakQAfCbpdajgg8e1ag7aFp7t5lQIP1yVB9K87DsQjB-B2t_ffkR3VwmqUcDIlbNpfutp1EV_dqFcC2K7REU-_EQsqBZBAYKRJoKQrSePapB0B4GVHxDHsOndEz3xg_pn2tv6EX7Ujjq_O1NRTGGL-6QXVVWscx1-_QhsehSHwxXTGfhIQlXawNDNPWy6BTq6xBzxiBI8z-JBYoyvktP0zJKsM7fXoIuNaedM_7P1fVBBR8-aRTLm9FWoPI49fv6-qFD3-WyTvVI-RykBamWKj2m-t63qGJvTbt6zFYOYctx9GFL7kYavRCGKOqf-GeFMQLYW_-HfNsymSMklEWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
مقایسه عملکرد دیومانده و اوبامیانگ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/106432" target="_blank">📅 13:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106431">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zX62_2cSGX3xBivjrUmQxTjWRrmz6U7v5obVo4OhSyWO1bj64fVy8REv0UVzAE71PeT-pEbG9xMQFZN9Nahv-qu3UCF2m0qTeO4a67DswGI0Pam6s8vK5HJFt6rGh4LmHh1HN8o3LqfbQzMUReDoxffqHsdQY-0ef7FBvJ_2zbUQxRY9rZlGxgddExWejo9PX8BlLjksmGhodddh6XKjeNt4lyHhfmCMJH8S8I0EOkHXBTz66zAe_-bjBBQJg58xeYEjBz28xeQSNUQIoRmReZOfsRGTqnBISbm5jp2f3vfoGrPgErCUl58ZGcrVKU-7tkj50IDkzSbA4wtFj77A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
‼️
🇪🇸
اکانت باشگاه بارسلونا نوشت: فقط وقتی می‌تونی این پست رو لایک کنی که تیمت از ۱۵ امتیاز ممکن، هر ۱۵ امتیاز رو گرفته باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106431" target="_blank">📅 12:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106430">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evSl3N0TpkA-e3zayYUaC6CRSjWKT7kEbZLvSEkQDN91Gnm8PEBXk8YRDbk-239yJQWghqvL-8pGXRESqhJOpO9mJiSONSHhMhyrz6DulC7XW2qBk45NvWweOevtLA0lD6oTrCPeM9XMHQwDfHI9ujzNDHtAPP2b5pBudm23_R7AbzfleyDzb_fRJsV2RFq12pvmBp5uOzfgzJo07Af0SNBbJZLyvs3Cy4oikpOJVGJ9e7Uqv8t4Z_W9yXSWU3HifdBoXH61vrUbYswwfGss1xcbVl0UopfcRWwPLO8gRVU-s5Ql_Z2OBgENMzZlAoH09zB5yPmbRY9Sf5l1wIUQSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🟣
پوستر باشگاه تراکتور ایران برای تقابل امشب با یاران سردار آزمون و عزت‌اللهی در شباب‌الاهلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/106430" target="_blank">📅 12:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106429">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psAsQM_7QIzT8aclukUTqJqVGSALJPuVxLDZD8LXmHi0du0sb0UTHOy3Vm2QoGK54oFEd-dAf_PD82oZzbuxfUmy0uXqtvoSRzZMM2ZD4sEa0K4F7DTp21DpCcUNLIzeVC_xjarDJonNqw3sAR97CTaJLa-dMYS8Yfjqu8zbatIXa2-Sr4wFJtOTTb1H6QRM7tkhJonfAxu8Bopywf681hwoYaD65KHnDOVWTgPkvcNj-UwVW55DkhGuxttSNoiQbhbTY77mqPCaxBXufi8MkSbZtSFuNTSDR4Zf1pEVZQPs-H-Xd4c3i40qJEP4tREbHFrS-NOpt7i3CPiQK3Q8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👤
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/106429" target="_blank">📅 12:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106428">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d890016b.mp4?token=E_Qp6DQLgNtZox4PpM2kXAWDtamZ9quWAaq0BGGJLBTCEitNgsO2TH5hLhfn5oY-ndHa1wkaC3OJLQWWhTzET600yn7J7LmMRqSeQwVvqYHVIwxFMFQJ4wrmXxOL6-o5oO3hmHq8jCqkCmQujkvp9nnI8V9wq2MjJvp3D4jL5HupajMlNvJqzKmZO0NUMY9kNoARHlAphksCrULW9sWJwNDSkU3BtZC1kCCXYcYN6jKgKvPbqKqApG_3n4s3eKUynMUdzyNhB2IMyGsbVkeAKX0EB9S_9zmxFK1tGDhkalECG3uRrB39GfQFbfX_TBBmnMKLuPSdAZxtY7AcR2NEYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d890016b.mp4?token=E_Qp6DQLgNtZox4PpM2kXAWDtamZ9quWAaq0BGGJLBTCEitNgsO2TH5hLhfn5oY-ndHa1wkaC3OJLQWWhTzET600yn7J7LmMRqSeQwVvqYHVIwxFMFQJ4wrmXxOL6-o5oO3hmHq8jCqkCmQujkvp9nnI8V9wq2MjJvp3D4jL5HupajMlNvJqzKmZO0NUMY9kNoARHlAphksCrULW9sWJwNDSkU3BtZC1kCCXYcYN6jKgKvPbqKqApG_3n4s3eKUynMUdzyNhB2IMyGsbVkeAKX0EB9S_9zmxFK1tGDhkalECG3uRrB39GfQFbfX_TBBmnMKLuPSdAZxtY7AcR2NEYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇶🇦
تجمع جمعی از جانفدایان بصره عراق در حمایت از استقلال برای بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/106428" target="_blank">📅 12:27 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106427">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c84cb00cc.mp4?token=pCiVrx38unhcfqTg6EDf4uOD5F1T6U6KvabUZH6q7pkqK0Jrqq3P93paM6iX9-3WuvQc7KpsBN3WOV1y2GgGio0mmaSFjtSZmw7guT9AE0sorBu8-81aVm4S-U7LGdZdzGb41LgVwrNpiOGcSEziU7wwIUE1_7d9Oa0DsV17Mbfy5jgr87UZiqfGJY-IjPJ1AV4paK7WiDqfsFNMWXulBEdpsA6GLouIC7KM_mSQPniMMIbJn8lpEahzXTOZ0P2vdWPIYYD7JX3ibSLCl0CM-6wdZNwzBdsRCYlmytL5G7iRC9xKypMJ4HguYhlLCXCyB7Pzl2Wh5aQhUHMgcrTGsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c84cb00cc.mp4?token=pCiVrx38unhcfqTg6EDf4uOD5F1T6U6KvabUZH6q7pkqK0Jrqq3P93paM6iX9-3WuvQc7KpsBN3WOV1y2GgGio0mmaSFjtSZmw7guT9AE0sorBu8-81aVm4S-U7LGdZdzGb41LgVwrNpiOGcSEziU7wwIUE1_7d9Oa0DsV17Mbfy5jgr87UZiqfGJY-IjPJ1AV4paK7WiDqfsFNMWXulBEdpsA6GLouIC7KM_mSQPniMMIbJn8lpEahzXTOZ0P2vdWPIYYD7JX3ibSLCl0CM-6wdZNwzBdsRCYlmytL5G7iRC9xKypMJ4HguYhlLCXCyB7Pzl2Wh5aQhUHMgcrTGsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
مترو های آمریکا رو‌ مسخره کردیم، اینم وضعیت مترو های خودمون! مردم انقدر درگیر مشکلات خودشونن اصلا اهمیت نمیدن بهش :))
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106427" target="_blank">📅 12:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106426">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCSGlb6Fl5Ck1-2qDxsQHGNmgxh8ceTOrrvDByniSXBzvNyQHxJiILvSMrQLLwAWlcZFLBkKCUsOKnYL3HCjzsve9DTXqw09YKk8k7kCOet6l_RiJYfR77S75qcdimkUeempbu1HE8Ms0U9RJlV83zhyluhp6eyJJR97CqEd7gGNKHbEh98TNdVYwX9veapgdIhhay34SwwzZj9t5slbDxjz7UyPwlB8lQ662IJxpLeg39o67Qxgcbb-OglQH9cdjUy6vGBkAACHZkGSM7KeGBSGRCkfq7w7Dwmg3XYv2k63yu5vaVaR93dLWz1vJraplAdfl01pF9VDbo2IOr5Irg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شکار بزرگ استقلال در کشتی آزاد
🔹
✔️
امیرعلی آذرپیرا دارنده مدال نقره جهان و برنز المپیک و ملی‌پوش ایران در بازی‌های آسیایی ناگویا در وزن ۹۷ کیلوگرم با عقد قراردادی به استقلال اراک پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106426" target="_blank">📅 12:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106425">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106425" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/106425" target="_blank">📅 12:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106424">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKTajb_6bu0foR6UAWCNr8z-qek3sTvVVQpxPIB68mKz-wtl0bDuRtCYuA342Cy5BZd6CfJw1rdJ-tkAm7ycktU7RIV6nxOYr-R8p7ZpMA6d2vYP9jTr_RAsEYr5jXKBR3EKIt7MLa85uCWyVknQP1U4pUsYURWONIcICGHPmSzYv0OVfeUPCIWNohBkyrHia_lTRyEZpuohfUq8e0AVWkTRiflY8U9_rk9uMPMC12FCbrgrgx46JaS2BGFLAIrUSJxryf0_3HxgaNDpjtNFw15ecWV8PErc6i5Cj_jsd-VUVRmlZZ_Xn983M3SFnE24N7VbqQC0vKtZNVTo0eSiWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/106424" target="_blank">📅 12:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106423">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf78496549.mp4?token=sabXrF_ZtbPZN-9KO61zKmJiAWa1iG7z0lI5SCvvAg7xFUxz-3k9WvlbJCjLZwhvUB2tBZYuGQ5d44Z-Nlow1QKjnj5d7VVDMXSuKJ8W4dtdXxdidd2BoSLPraP3hMQb-Ofd6utTfR8orGfb42xaacxp8MBaZc8RKdiUrXWNyxFeqQcV4vSZHOLpHfNga0Yo0Lg0xs-vX69-KTdhcKpLeK7vbmPemtC6XNxp7gxY4OGXSTeh-_oHp-QI3IpebGFnxqOngLV0UoYZVR_pnxx6gk8eAjhz5wQwIrxOaWlqc6PLcdDfBQqu-fdPEsutpCvhD-D7N74hTvQSswRkpZCwcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf78496549.mp4?token=sabXrF_ZtbPZN-9KO61zKmJiAWa1iG7z0lI5SCvvAg7xFUxz-3k9WvlbJCjLZwhvUB2tBZYuGQ5d44Z-Nlow1QKjnj5d7VVDMXSuKJ8W4dtdXxdidd2BoSLPraP3hMQb-Ofd6utTfR8orGfb42xaacxp8MBaZc8RKdiUrXWNyxFeqQcV4vSZHOLpHfNga0Yo0Lg0xs-vX69-KTdhcKpLeK7vbmPemtC6XNxp7gxY4OGXSTeh-_oHp-QI3IpebGFnxqOngLV0UoYZVR_pnxx6gk8eAjhz5wQwIrxOaWlqc6PLcdDfBQqu-fdPEsutpCvhD-D7N74hTvQSswRkpZCwcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇮🇷
🇶🇦
به مناسبت بازی استقلال و السد یادی‌کنیم از شبی که صدای صدهزار نفری و جو فوق سنگین استادیوم آزادی باعث گل‌خوردن السد از استقلال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/106423" target="_blank">📅 11:55 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106422">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYIxSsW4XsxAjNrML9H9ZmoMa3Ts4iFC82heSdTyZ-i5M5S0gA99CT1tSLXlvq98utH_Y8zttaizQjdYArwwTTfQ61D2nOjw9w7WZv8q3e8BrllrxgkXvG0OdxjvilNDDYhw7tzSmt_oNVSSPpOhjEQR9-pVJoxri9nMoo5zlhTL1sHpRa86Fc4lmXXmg6EgOuHVS2OfrPDC0e5F86Lh9lUhfhzHWrdoYZkyb08p1f_pFlFjdey9N2LhgpRrIv7hgtwsHrF3I_Ol60QbPB-TLSWN93zh8Xr7SIPVZ0basO0AUqA1e_otuAv42rky9IWFImKZx_cVPqBXYUJhvBX75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
🟣
پوستر باشگاه استقلال ایران برای بازی با السد قطر با تصویری از حردانی و چشمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106422" target="_blank">📅 11:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106421">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285c0d29ad.mp4?token=WldB7kDhSICilISapep4EXw8cIAAKOmDNvdY943hHlgVzjBIQTUfMbN9qF4_WgpNXJ4-sxoQU7QoKgTNn2vIqvi9vwyIMUBpu6jarXK4QLsUVhYWWLmHfKbR7NvwK-4EhTk30qIzDE6x6hlY9ezeaZK-vHr823zD49vB1KGwDcSRNfPQ9t3tJoDAhGkV8-sXzw-h2lyL3rOaUeOGoTfoRb7i6sHDXgIu8hjPiDTU4nArJgHcm1ETMKXjZCqzWyrG-XPAVoYVgcTuWLEf-ZTN5scGl_kR0O_QjcpLTb_T8W6Jnhms3ISoJEWzZL5jKByhMLVWmiqlYMIGBxZ1kpgA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285c0d29ad.mp4?token=WldB7kDhSICilISapep4EXw8cIAAKOmDNvdY943hHlgVzjBIQTUfMbN9qF4_WgpNXJ4-sxoQU7QoKgTNn2vIqvi9vwyIMUBpu6jarXK4QLsUVhYWWLmHfKbR7NvwK-4EhTk30qIzDE6x6hlY9ezeaZK-vHr823zD49vB1KGwDcSRNfPQ9t3tJoDAhGkV8-sXzw-h2lyL3rOaUeOGoTfoRb7i6sHDXgIu8hjPiDTU4nArJgHcm1ETMKXjZCqzWyrG-XPAVoYVgcTuWLEf-ZTN5scGl_kR0O_QjcpLTb_T8W6Jnhms3ISoJEWzZL5jKByhMLVWmiqlYMIGBxZ1kpgA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
هاشم بیک‌زاده: بعد از بردن کره‌جنوبی در سئول؛ سطل آب یخ را روی سر کیروش ریختم. هیچکس جرأت نداشت اینکار را بکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/106421" target="_blank">📅 11:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106420">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SeT7U_8XqZ9__Eju_gNlJ1GYEWQCTomiBczUASA9c9QECs6eqCUw_4Z9g1VMgXtkaupDir49CFxqD-50Uotg6oXW50gTZP6G5uQIwo05ZGPrzGjQf9SwU32kDLZbqLn0zaiqakUC_RqQg0bxRf0wsHSXyyL9lw8WXMliIrSfH25iseOugz0acDrp12erZxNklAoJtlrTc1YRulJVjNxxeR9s3y6KBZwBqasNg3oILPdRqVTZMOG-kEPsO-ZZS6If2cMAwGqrhUrdQqH5-jwM5PXTZnTPAL0VGxskI1Gvz88e42mEs62uDeNSBNMds23o7apgboRrAozTd2V9fAOtcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
دیدار استقلال و تراکتور در هفته هشتم لیگ‌برتر روز پنجشنبه ۱۶ مهرماه در ورزشگاه تبریز برگزار می‌شود. بزودی برنامه هفته‌های آینده لیگ‌برتر اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/106420" target="_blank">📅 10:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106419">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bbf719687.mp4?token=ivy487hb8xlyF4wEPA5PwWlMR8ukm5dlDFoDR98ZbzM3VZR11YLnzfKJu7OEJvjBpCcy7XAf3ANuslg-6isFNHQDRayrVkRSH7gchd4qBapj3hoHfX60gd_zLJIXS05QagLd3qip5eqv_RpEYzmqOS-HBe25TVY-X5OH8OPe_iXGe4dsJHsqiYwTTRdtZZ7RtSnb0xBWyLbEiM1vxxdzt_w_5-4snMeMm9Ee-bTN4j0wNZZKbAkQ5P6j6QM4YB8Rt-r42rqu0aOprNMd0NVimWM_AdxZ4tAZQvKLidrQvV0NsA5cwDOQGriYiJht6q1YVUzirKM5ZiuCDfO7D8KelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bbf719687.mp4?token=ivy487hb8xlyF4wEPA5PwWlMR8ukm5dlDFoDR98ZbzM3VZR11YLnzfKJu7OEJvjBpCcy7XAf3ANuslg-6isFNHQDRayrVkRSH7gchd4qBapj3hoHfX60gd_zLJIXS05QagLd3qip5eqv_RpEYzmqOS-HBe25TVY-X5OH8OPe_iXGe4dsJHsqiYwTTRdtZZ7RtSnb0xBWyLbEiM1vxxdzt_w_5-4snMeMm9Ee-bTN4j0wNZZKbAkQ5P6j6QM4YB8Rt-r42rqu0aOprNMd0NVimWM_AdxZ4tAZQvKLidrQvV0NsA5cwDOQGriYiJht6q1YVUzirKM5ZiuCDfO7D8KelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
🏆
بالاخره امباپه فاتح توپ‌طلا میشه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106419" target="_blank">📅 10:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106413">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PC9-CuX8DToGItecfPtwqONq79LPkgpzaOEwCW863m5Pa5OUW35pA_eLRf_dfV2xrRMlNoiBPF6x81dP3md3jEQePYK06f2YPScB6KXdtLRl6WCPGXeNtxbYigJUDMa-BraPSkGzcOa4i_FzwXiiQarkUIzBlRSnarzI6xelpyeSox0CCKmA79T_Pcy6v6dUzWbNmMM_gp94C1nsqbyVp2S0QCTmRTgRIoQD4ahnCgvx2rQ5g7SGqhLyDk3Aj059mrt7nlZ-02Po07JxgCCOqIfZ8bCd0fe_dhdJpcUAmAkC0KUBhr-uJDM4n6L6NAh_xcmnyyxVjv2Yw1bqEAJ01w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjJuB3tI42lwR2XkYV3hIFVHAAYSZayucBfGjt5genmYK1AGdUp2FLJG-rdaDhy4EGQGKLfngG7ia0ev8CEMHs6CsFTyMvaU9C2a7XNizdkpsIJAbHHa3TFXAzFd5qZt2CLEmTEaFfk22GDf_N7sg0CDo8M560foioWuI5TgjPnXQvmVpSvAyryohpHAlVmrk9l8cjau70VBT9pAoY-num3KYXmH9-U7UPFePAa0t6rguaTA04Z5pk0F4jMNTL6_ewWvPmHwn8nyvHsMTVu0wcpvveq8VjG4O6UnARZSEnZWcwsljjzN1FPLj9VVtnwqaWnpJ_wKMOwTxyzgCGkycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fov12Zb7fTKWSZCTTrBthYP5pqUoSms7A7EkzG3ZsQDznA1ASsUs6Oswq2PplF1Ao6jO2_Pvr8KBAct6gQdilwJr5vSI7j2RRnNt6m4NN71CjWKtYPBcqlNzrw8sBvCHj5cp5MfkxCxXzYuQaN0nok6SfGjopC-vVgr-hg_hrbLUbOJc7KESEICzjNml6Qhm1N4OEL8VKl-eW012rocTn8oNwW3FkSKh7zjyy1BZtz9zNZutzCTn10tJUYF1ye9l11OjIPEgeBhFQN8hytbpI7-aECKbKOJSLPsSaS35BWgjpVEa4P2-2zkOoMlQsuFdNKr9E2c_UILc7HPs5zDvbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsJN1GpEDJllpRVAZznvqR0AE0g-o9CyczxsFTGjo6xw4Wdt5dCcwJsU7hHNiiY4_RBecu-Ku6qtQJ_oQK_7Bs-xLeycRxoBBwwkNtUl3v1WIT7htxUNYkmApeq56dThJYRFPs1mOm47U2isUETVg7ffguFrcy3wspM9BCgM3CDwzlConb6lXxhSirzKD8zCsuXrG26OrP4mHMLy_Ua-VNV4Wc2tuncLMYkV9eQahzKKkdPvYA_B0mFYs_HGjTDKlfMNO8idENWJ5YkHQ_WvjGJ4UZ0RWPBMOfy-tvkId3I3Ga3C2uBUeelhwWhWK_EM83I0QmslYrWHXDbIh4Horg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UBite2WXBCKeQ3gYdoPv8pRkHbW5iv1dFNwWwis9P0RdM-k43TjKDANMK3pWTB_ule2IpO6yvE32AWELswnR4-Qi4IQ_WiqnwBraFiUXb3vj2sob8FNHNTd0Ywt7QIf8jZ27_GIFwtYCGUd7BlrrBeCMM4BGjRYLF8XK3pOYKjsX1ubyoaoROg_uBwrV9I8lpcZUK68Figi4G4OwfpzWhS_fenkv5lHE-BVuPfELgfkiQrMDrRI_D18PCf3dmgAYhhvuk7qAr4m2W98Yp8dCXmYX-srP6S4U7cWzAoP_2bGWLxRv46XMwdMKGv06cs4b2ZhCxv4YVBsCV3pd9BfTlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZveo2qkk15l0tWIeDu5XlK2r58HiHVETv2enldHB6jTarIl2butjBS9c9VJbn9wW9DogPFgWDZVMOZMvUjlEc1enrU8KwcRHDWePnOa5gsh-TEjX39M1M8S4ZFvbMaSj6qoWSA5XJkRMO1XdTmENq5wi8KVJpzaVcvhSAsKyRzpL9WEkk8o1rwY9giz89PB7uV8ViKLj0bKHrSfzAR2Fko2d8L5KjE8Ke0VbzAL_dfpfypwFurxbW1iGT6Wc_9b6UCBLpqj9L3zQ2BQ20wNf0FhMzC5cOLB59IMsDI5I_SQXKsayPQBuigymssEpjvqhX2okOENu9Rc-RQH5RJERw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
👀
بعد میگن پول تاثیر زیادی نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/106413" target="_blank">📅 10:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106412">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dcc7c68b4.mp4?token=G1av2aHv2KCT5vQ0k11fEyclUo_fQ0JF5LS8gJ10Ha9ihSSVjVRr13Iqo6aEeUDN6UFiOpKUnWpk7g8L6sFWQeG-qKeaDIfOq5SgdQa55VDXE8SLTnyWIkf1gXWqQ2hdRA1a-QbJaWG9N_CKJlwXY5kAk3DzpCDe_EwmZrW0lFRIQfe9S9ZiEmV5sMdh7A7MbiY5ZIEqTDJjb8D5UbqhI_lhBKwmbls-p-HB0_vNCXomDCwvaZeOPKQcTuLWy6mKPfs5Yk4LEmHy2c59lh7cA6HCcORzsTC_uzUWLbXHrHGfJhQhEvrv1lcHCh0F2vDzkp5fDZusV2hSBrgHRFBmpABOFM1xCTcd6ZDzpNcmuxf0UkYsM7kZWY3at1Fsxtmd1MQSQgLU_Np1Sg3pdw8qP8mQkv9I_rE-9FmCirGBn3IM2B9hOnZziPw6blfc_243zIegHpv1__XNKXTSfOd7mKcU9LOGekhdaZUnjCxa1HrUvkN-npKhhDyYDWXjIgXuPzL4aNqYcFzzIaxx2iFX__3SKypSIbmq1v5UpmH-IZfIr_Mt2qDoiQLo_pECzjco5XGhshOMg0k1fUDTpKlQk1_kYb1IIifSKfwBZwi9IQpR7TI-YAKz9ZkXVH0geq23XoEVKFdM8dQZdvI90adhnoYuDUefVOpFZ4YwzqOs3XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dcc7c68b4.mp4?token=G1av2aHv2KCT5vQ0k11fEyclUo_fQ0JF5LS8gJ10Ha9ihSSVjVRr13Iqo6aEeUDN6UFiOpKUnWpk7g8L6sFWQeG-qKeaDIfOq5SgdQa55VDXE8SLTnyWIkf1gXWqQ2hdRA1a-QbJaWG9N_CKJlwXY5kAk3DzpCDe_EwmZrW0lFRIQfe9S9ZiEmV5sMdh7A7MbiY5ZIEqTDJjb8D5UbqhI_lhBKwmbls-p-HB0_vNCXomDCwvaZeOPKQcTuLWy6mKPfs5Yk4LEmHy2c59lh7cA6HCcORzsTC_uzUWLbXHrHGfJhQhEvrv1lcHCh0F2vDzkp5fDZusV2hSBrgHRFBmpABOFM1xCTcd6ZDzpNcmuxf0UkYsM7kZWY3at1Fsxtmd1MQSQgLU_Np1Sg3pdw8qP8mQkv9I_rE-9FmCirGBn3IM2B9hOnZziPw6blfc_243zIegHpv1__XNKXTSfOd7mKcU9LOGekhdaZUnjCxa1HrUvkN-npKhhDyYDWXjIgXuPzL4aNqYcFzzIaxx2iFX__3SKypSIbmq1v5UpmH-IZfIr_Mt2qDoiQLo_pECzjco5XGhshOMg0k1fUDTpKlQk1_kYb1IIifSKfwBZwi9IQpR7TI-YAKz9ZkXVH0geq23XoEVKFdM8dQZdvI90adhnoYuDUefVOpFZ4YwzqOs3XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤡
وقتی هادی‌چوپان میگه هانی‌رامبد رزومه نداره:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106412" target="_blank">📅 09:50 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106411">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5d091739.mp4?token=Bs4CEp3T_SEpd0E3w6xnPIFMBXPiXRqVra43x05cUoV516zrXlndfIqblpXkbmQ3efEQCr18627uM_HW6aUs0bUnw81Vv-KO-pW9uUAry_rRKkiY-1GzxiU5AuIMgrReWQQ8LSmh28AtK-eEX7Bug5ku1GUFnV5wSxJC3WcnQZDsIAUI0dmJidWbnpS9Bw_k0ITax4JvDJzE499Ss9zuDmRZazxEt0gB9TTMB-SmhumW7DJ9k1Mfbsy00HUMIyMdy2WwYcJAN0asz6kSXhzy79rT4Z8ZV01pciBIu4cUdIK0bbtgOK9agEVg6pMDBRIBLUS4W9u88JaSiHUIR3iaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5d091739.mp4?token=Bs4CEp3T_SEpd0E3w6xnPIFMBXPiXRqVra43x05cUoV516zrXlndfIqblpXkbmQ3efEQCr18627uM_HW6aUs0bUnw81Vv-KO-pW9uUAry_rRKkiY-1GzxiU5AuIMgrReWQQ8LSmh28AtK-eEX7Bug5ku1GUFnV5wSxJC3WcnQZDsIAUI0dmJidWbnpS9Bw_k0ITax4JvDJzE499Ss9zuDmRZazxEt0gB9TTMB-SmhumW7DJ9k1Mfbsy00HUMIyMdy2WwYcJAN0asz6kSXhzy79rT4Z8ZV01pciBIu4cUdIK0bbtgOK9agEVg6pMDBRIBLUS4W9u88JaSiHUIR3iaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هالند: خیلی دوست و رفیق صمیمی طرفدار منچستریونایتد دارم و قبل از بازی کلی برام کری خوندن، حالا باید یکم واسشون کری بخونم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/106411" target="_blank">📅 09:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106410">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
🎙
حاشیه عجیب مصاحبه خبرنگاران با اسطوره علی‌دایی درباره صنعت خودرو ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/106410" target="_blank">📅 09:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106409">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514af894b9.mp4?token=bGZ9UU7911-5AUXxC_D_YoFQTIWieFELROo7O7IV81lrD5vDYHWBDWaftf8G5CAmQo3uOEjAGbWY6C55l_179_R65L8mKg7ZLGcrZ18hU122bQHYs5zDx5B7caGqhvLzbtzgLqPBlr9niq02KGJW_eEWotp18G1E9Oy-I9cAD5FHQtC_cFbnhmPMZFhtE-KFuyPnB2LLKQrJ0enmS8QK_5vueSVuoV7ra3LlLLoexvylalBpd9XZz0LXDrKOWaV7XRRkz2RSSr_9sHGCPnbdZlBgoypB4wlJnp0vZVVBZu4rrCH6IrlovPhonLbo0V217pFjLqkHdN2NWw1_deOW-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514af894b9.mp4?token=bGZ9UU7911-5AUXxC_D_YoFQTIWieFELROo7O7IV81lrD5vDYHWBDWaftf8G5CAmQo3uOEjAGbWY6C55l_179_R65L8mKg7ZLGcrZ18hU122bQHYs5zDx5B7caGqhvLzbtzgLqPBlr9niq02KGJW_eEWotp18G1E9Oy-I9cAD5FHQtC_cFbnhmPMZFhtE-KFuyPnB2LLKQrJ0enmS8QK_5vueSVuoV7ra3LlLLoexvylalBpd9XZz0LXDrKOWaV7XRRkz2RSSr_9sHGCPnbdZlBgoypB4wlJnp0vZVVBZu4rrCH6IrlovPhonLbo0V217pFjLqkHdN2NWw1_deOW-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
نتایج ترسناک بارسا همچنان ادامه داره. 100% پیروزی تا اینجای فصل!
👀
☠️
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/106409" target="_blank">📅 08:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106408">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
جزئیات تازه از نجات دو خلبان F-15E آمریکا پس از سقوط در ایران
🔸
برنامه «۶۰ دقیقه» تصاویری تازه و از طبقه‌بندی خارج‌شده منتشر کرده که عملیات نجات دو خدمه جنگنده F-15E آمریکا با نام‌های رمزی «آلفا» و «براوو» را پس از سرنگونی هواپیمایشان بر فراز ایران نشان می‌دهد.
🔸
این دو نفر با فاصله حدود ۵ کیلومتری از یکدیگر در مناطق کوهستانی جنوب اصفهان فرود آمدند. «آلفا» پس از ۸ ساعت، در عملیاتی با مشارکت ۲۱ فروند هواپیمای آمریکایی نجات یافت.
🔸
«براوو» نزدیک به دو روز در خاک ایران باقی ماند و با وجود شکستگی کمر و جراحات ناشی از فرود سخت، خود را از یک مسیر کوهستانی تا ارتفاع حدود ۲۱۰۰ متر عبور داد تا سرانجام نیروهای امدادی آمریکا به او رسیدند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/106408" target="_blank">📅 07:23 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106407">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/106407" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106407" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106406">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWLAzL0g6aSgSBVIsnTZx_FpZmZ_xiX8OFkI_rfT6MNfD5XF_mtBJ3XAe-nrJdY72_3Nkc62TppvDFRGBNBw6rIvc7ziGyU4mzNuoR2DLUqzDwCBR1kg3QFCHRK9t7U9tnPyo-9ep8poJII_JIkfvpE_hyA5KSvZ2y-0JA77Hs1i_qt4IfP9CmtSvn3EF4dd9KxFTrXxwxdklIh-iC5vLVWAQYGWYKYMjigoYGORgLB-x-Z4d8KcoY9JGRn1HTkQcj_rKqvqReNo3EXo2GLYFCxJKOgFX9e_7d8Us7rT0XjbJETjJk_UDo415kztFBP6xLU7_oHGvcglXKaWx-qACA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/106406" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106405">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/106405" target="_blank">📅 01:46 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106404">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔻
🔥
🏆
لامین‌یامال: من و امباپه بهترین بازیکنان دنیا هستیم و توپ‌طلا باید به بهترین‌ها داده بشه. بنظرم فصل‌گذشته عملکرد من گویای همه‌چیز برای انتخاب شدن است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106404" target="_blank">📅 01:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106403">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cSljt1vhpxJTQwbFlj-FhxbmR829XJaerBpfmaKCiZMNM8kdALngqD084kQTQvudrv-3xC-eqFhu7473PY4VYrODGpM_ql-BC5zABMf7uViSlLUt7t6nE4tBAQY0RnjAkm5DBm9Kvh8R-j4VKrj5hpEF1Rct-OmnWz4g8Ei0FUPKgESGto4ssTFA4wK2G8ADx7QcvhMviCxRlEW8890LaGT7_7P_d09LhHrJt6Alpair23jlGdkoyLlxZ3_FmN0D0Vtmc-G-_A20aFoS32cntulNzRx8jTBEXk0AxCo7Qn-FFjBlD32aTOYBN76jH5zJjLCxuoG0ifyCMmn2aqfBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
بالا گرفتن جنگ توپ‌طلا؛ لامین یامال: «فکر می‌کنم امسال به خاطر چیزهایی که به دست آوردم، شایسته توپ طلا هستم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/106403" target="_blank">📅 01:09 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106402">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiAQGDheMZQV2feb-OBJ8zyMJWTQxU0Z78YmDP0snLMowwbXU2ofibcbZt5AL4cCg_nOm0-q88_8puN510D0W4Uv9bQB2yspSHiV0vyzb-RcuqXEu1SHu-24XRHMmzkeifVHE_qRm_3ZOR-zdEt1wK8h-wNraAvBrjq6ZBLHQYGbTu2cFg73nal7qJTynpQR00As_TIJw5XT_ZPuYXzSj1RnSBPt7sBbW6HXE0aJcFuC8l0m9nhvVvYRxh98gqgCHrJnZ6-DZ60E-ulHS6SJAWa7D_gMIkBnTaHTk2k8OHD5qPj-ugWFlZdjOAJA64qyJukxOFi4KtPLdeEPuvzCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
بالا گرفتن جنگ توپ‌طلا؛ لامین یامال: «فکر می‌کنم امسال به خاطر چیزهایی که به دست آوردم، شایسته توپ طلا هستم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/106402" target="_blank">📅 01:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106401">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLy1wnNJ3IFJp3trE7N18JdA2PuF-UtF2ZOt8LOz44zhrTjvZVpX4BQu7-knwaYYjkKGH9Mjogmk8D_PDhPb0rYg0kZ_8OgipEyBbKK-LZg-M_G6afqWNRuraSAQ8IKSCfTA3zCj_fzl1uouGM4wpAJigCq-BCqX5qLGHAo0sENnRwj647vt9iE_sbOe4YQUVc952qTz1MjBk0Pg1hKQ4sDNshz7kBgUUe8vARf_tG3ucaC0vL40NQLT7w-BMNfwFYuClvdq56B_ak-LDk7mO12nqFziuCRqNbORH5lj3T8bSJNf43BGH-u2evIvg8YxQs9dP79nKqHi1fH3gjBUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🧕
بیانیه کمیته داوری انگلیس: "داوران تصمیم گرفتند که هالند در آفساید نبوده و همچنین تشخیص دادند که انزو فرناندز به توپ دست نزده و دخالتی آشکار نداشته است."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106401" target="_blank">📅 00:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106400">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8675062324.mp4?token=BodSuTQoloNH-eh5y-NFCazY1fcxMwRD3lkMTlSaMAlPI30jmqUknUH58RkKfzCuQZTNeLhJQT1VajDB6Rl3pqZOAmft5Jv74-LmXksGImQmrMe48StU0ElQGVGRFmOmYLJeTn70AvorjZbh_wr7gIxjCnrbLsOlYYZVyFYmb4aS_5KcGq1a5DaBhe9RZTeZgv0cU49Pu_L1JnACLs0Y3bBiB0xNJLvAJA-Tf3gGNXNDGlpV73dA2ZXIl50JSPAOs8hVcuZseRmtoJzEywjCVUKlaqLtSzkLfFBQgeMArVz56BdLzCieVfAgol7iewLFscEZidyNEQQM1a9rEQHHfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8675062324.mp4?token=BodSuTQoloNH-eh5y-NFCazY1fcxMwRD3lkMTlSaMAlPI30jmqUknUH58RkKfzCuQZTNeLhJQT1VajDB6Rl3pqZOAmft5Jv74-LmXksGImQmrMe48StU0ElQGVGRFmOmYLJeTn70AvorjZbh_wr7gIxjCnrbLsOlYYZVyFYmb4aS_5KcGq1a5DaBhe9RZTeZgv0cU49Pu_L1JnACLs0Y3bBiB0xNJLvAJA-Tf3gGNXNDGlpV73dA2ZXIl50JSPAOs8hVcuZseRmtoJzEywjCVUKlaqLtSzkLfFBQgeMArVz56BdLzCieVfAgol7iewLFscEZidyNEQQM1a9rEQHHfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇫🇷
🇫🇷
پاری‌سن‌ژرمن با تک‌گل‌ فران‌تورس امشب مقابل برست برنده شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/106400" target="_blank">📅 00:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106399">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9Ueh2lCYr75LljAESLIPr5J0tfmUkCHQJz7T1hrBXOnIDkKcAZyZT_yAmaTF-Oskg5O0v-45X2CAIymAFV-UEWB6I4cf3I9LVs8jpwg-TbTvpmXohGDNvCyGUQ84_JgI9h91yK-5-d_9NDzZ96L8KosdJPRfdXb3QDlbLN8vjbC3k7AqKT60JGfOgRtkkmGY9qbtMRS_FM8oL3OuKVB7jYxtxT2qFi63aWYbCIdTCnISsvaGTvCJQ5m13JZRSKttWDhzxq4Xb_FHJgAF9SsVWwWTHibWhCOqbsoHHSc2p3afCT_3BDmE38oXiD1S7VInCCrarFnQhtal-oB5K6Oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
افشاگری پشم‌ریزون نشریه سان:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔺
شین دافی، بازیکن سابق برایتون، برای یه تماس تصویری پنج ساعته از نصف‌شب تا حدود ۷ صبح، به کلی بلیک، مدل انلی فنز، ۱۱۰۰ پوند داده. بلیک گفته دافی توی این پنج ساعت بهش گفته چطوری لباس بپوشه و لباس زیرهاش چه رنگی باشن. بلیک حدس می‌زنه که دافی می‌خواسته اون شبیه اکسش لباس بپوشه و مثل اون بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/106399" target="_blank">📅 00:03 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106398">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvD-I2rOK9_phnXeJ4KneGNJUpqR29xA11J2Ki8HjOhCOgtl3xAT5gcw6OeI-59kNnnygmBPvcZbGB0tGWZJmMvHJDbwac38kSp9wRVE8z8p87rh9g734n5s7sg2XeK83qF7xhUzzluGLGPBMMkLqnOPWuAluUUUqoNtCuJvsRIUiYF3S1LPzST_6PKRthvp6CA-T88qOQL80RpvuQhreb59y-1Vd58TEJLyJ-bqioBQoT6-33RK0yEHFvURbaoO9I15lYXxqg1aN00uKnhTaWPQb386t0LVIXEWt_cZY3Gh9bZqs7QT_NGqjcm6GZl7_Fi-RMQ5wIgNQE3WG5lGbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
محمدخدابنده‌لو رفیق صمیمی اورونوف
:
🔻
چند روز پیش از اورونوف راجب شایعات جدا شدنش از پرسپولیس و رفتنش به یک تیم دیگه از ایران پرسیدم که با پوزخند بهم گفت که در لیگ‌برتر ایران فقط انتخابش به احترام ۴۰ میلیون هوادار پرسپولیسه و در صورت جدایی در آینده دور، مقصدی خارج از کشور داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/106398" target="_blank">📅 23:53 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106397">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFpRDFB4JAuDg1QBFFcsM0KLx_QpARGthMzNFcSwLK6WRt4Vr8NvgUW8ng_ImQ0pbEyDDtphRGxdKmOW3yveeHfYJ6rIFobLtmpEVqp_RHOik9J_jF8XGOtdzMiL-5XD2s0BOKZK32laEtPp0y-6vpdl5eP7e6HO60Ty9ggqtGmRaUK7xXlzDhfQDDVYtsHkPA10oWXs5UKLgzQG8W2sRODLSvE3_8NphLEquoc3b7Drmlf5-iIM4j_K25D7Md6CcWX2cwxVEC0bLPHUpWIOvohCWLspyYknW0HElHoUUzV4I9MZilxZpWrtTTE2-MSKwpstRLBCf6W2uUTVVcH3eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
⚽️
یحیی‌گل‌محمدی در ادامه روند فوق ضعیف در لیگ‌عراق، مقابل حریفش شکست خورد تا زمزمه اخراج این سرمربی پرافتخار از تیم دهوک هر لحظه به واقعیت نزدیک شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/106397" target="_blank">📅 23:44 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-106396">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCPVuWP1x3OxJSC0YjNlcPEUA09VwnzkVla2RJQAT0QC9nVjaCblhVL6LFIHUoyUVDI9lxTj90Ga1EyuOCsR0gHxmfB3mOFttxjU2L3M-UCiwGi46gwmNtqLI1gTSKPwAz1h1Z7QbCzcJMSRPvSXP3SINXfc4q5WHdYZf86WwRJ7M459vKoVYrhfRjYHgVMr7fCW36igqU6Ak4X9hT9ORqVjw9JzyZ4lPlrzd6UYkx9OnjA2-If8GzUo1zIg7iQlK1niVrjjAbDhOOO53SOcdM1-rNHno5cL7_abnd5Hfd3lgNXUKtzBW4KAhjQPW8wO0oAmkanqC2f4fjw_brNt_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
👤
علیرضا بیرانوند: به عنوان یک سرباز جان بر کف ایران و اسلام، آماده رفتن به خط مقدم و خدمت مقدس سربازی هستم و از اول مهر به هر تیمی که معرفی شوم حضور پیدا خواهم کرد و در زیر این پرچم مقدس به انجام وظیفه خواهم پرداخت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/106396" target="_blank">📅 23:37 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
