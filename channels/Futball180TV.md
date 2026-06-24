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
<img src="https://cdn5.telesco.pe/file/cv7jVK8Vl6vgifbZX9sOzIMHsn3Vr7zsBF3F20X6V7-0eXZ6wJSrZ_f68NCWpXY5SIRg45Er9-IDf04K7DMBUrYf1e4YCEo24aiU6t4kPcFKZ4xR772S-Sh8AMaPvyX8Tq1-DxwUhDTI-yizf2JtIk4eX2BD7ZaCG3R7BXzZjL7aI2ZiSA-M7UIsQsKdkb5A6grdABeHERZiwA2INKYW60qRPShAiaulEMKfb4ms8DiTs9ZC-0oICj1e9rVc6UPUUs6NKy_ZsvInR2Yk5OrQTu7jWbdFl8MnWQMEU0QeFsycjtiOAlDdXfzljTgFNaaVsjOLmlWJk1mKlG1STYgXQA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 708K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 00:37:27</div>
<hr>

<div class="tg-post" id="msg-95718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9jqWNOXaD-T5IbltgO8X-bRRvXLIuUk5AKlun3v06MduLH1VRN-33nTdqDxRu_iiopbuAfd8XOJdp7q8-7kx8OWlwg1dNefY9PEM6rjtEnNHhSPsnuHxfUfL054eurMicGpp4k2H0FKoJA6m48U-viIwoG6uvIKy4xJgY_0rv6Lg0mcXMNxTzsLguCy1dAB9M4vbQYfpdSYNlazxS_SbYuKKA60VwKZcQiSX09WXTsTJqgnXLRH0GCfM-81FRem5Poc6MXOjynQpiG1BKvi0ix1fa1KJnQWyIpktDDHv8LeGWc_zqe5Jb7nsNOSp2_zW1sy49xBIjPo1e8vlN-Qwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
❌
قطر قهرمان آسیا رسما از جام جهانی حذف شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/95718" target="_blank">📅 00:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkD6tMTYA4b_FIJ1VeGtvORgBknkIQeyqawCr-Ny0SdA9Z2ngiEeKr3QmDcD8k-mJLf_OWn-DZ9lJ3Ta5jA5xykD09HMNkkqY1z9dpZmDn_KfCGT-nbakzoejEJOzTm708x4IbfdzLB7xXVCsceMYKAIxg6G-eTYfffp15ReLH7gwiF0TNe8yQKjY5XKshB0lJBBubMpA-MS5pI5AfcVmavVevcDlSHmGfFG-keS80SliDlg2LNjGGM_5875YOij6pVksO8STKWnBE4F_cw8tWomXF1yPzNPIgCCiyWrAxUZk4qBCtIUWFsbxVcmsGiV_Vh51d0jkoPyy1hiqHWzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
تیم هایی که تا الان صعودشون قطعی شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/95717" target="_blank">📅 00:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95716">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پایان بازی؛
🇧🇦
بوسنی
😆
-
😃
قطر
🇶🇦
؛ پایان کار قطر با شکست مقابل بوسنی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/95716" target="_blank">📅 00:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95715">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پایان بازی؛
🇨🇭
سوئیس
😀
-
😃
🇨🇦
کانادا ؛ سه امتیاز و صعود قطعی سوئیسی ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/95715" target="_blank">📅 00:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95714">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پایان ست سوم  فرانسه 2
➖
1 ایران
🇫🇷
25|23|25
🇮🇷
21|25|21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/95714" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95713">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ceb81d53.mp4?token=EWfEU2AeUk_si2cvlutyj8xVy9p4PIa4GQheQbzZo8cdD_bv2RFIdS1FOev6otQEBDy5mKGECF99E19yiKxZrNkT5DIFG2AAPq-9tSiHbE_jLgWnuubnAEYBKkKF2vpxAkUZ_9jKsaYZ_IDMfMqnstngCpQ2sGtkM6aUsIgNy-efILTVfwtJSngqG4gwHeT_dLtZTJ9YTznhjEjwNCUB_3G63hKyVSySjptfT73oGb6D1BdEAC2JRWmd01ZuIKaxSy2e2UTyuvtDRoUreRNRAyNGBjYnwt_gOuprewGVn8smYw_rjJkzGpsz220hRpMcowATkOir9TM9Ei3BMgU7sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ceb81d53.mp4?token=EWfEU2AeUk_si2cvlutyj8xVy9p4PIa4GQheQbzZo8cdD_bv2RFIdS1FOev6otQEBDy5mKGECF99E19yiKxZrNkT5DIFG2AAPq-9tSiHbE_jLgWnuubnAEYBKkKF2vpxAkUZ_9jKsaYZ_IDMfMqnstngCpQ2sGtkM6aUsIgNy-efILTVfwtJSngqG4gwHeT_dLtZTJ9YTznhjEjwNCUB_3G63hKyVSySjptfT73oGb6D1BdEAC2JRWmd01ZuIKaxSy2e2UTyuvtDRoUreRNRAyNGBjYnwt_gOuprewGVn8smYw_rjJkzGpsz220hRpMcowATkOir9TM9Ei3BMgU7sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇦
گل سوم بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/Futball180TV/95713" target="_blank">📅 00:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqh-D5Ij9Q_yscBFCOAGAFVidwsK-xIOpB8ikWBfRGoj84yjif0iytH_Tb79kE3vXd8XdFbwKcasoU5FmIH9z05aBX0l2VyyilsJNsv3f28T-0l4a878TQYaKOyOr8USzvZEvNmCzelOAgMD2YdXV-XAEyKWVvF4AfOVwTRmQ7pH1P6X6eldjNNesiQ7H3O0HC1hOb9QPViVDkjrjroa7ne4DDM1Ac62OpCtAQPcF2Va7-sMOASsiiFbKG_WlKJTZEEvC1BzcMOvnJ5UeAjekFSuZ1OSIpJwHOmSKQaosRB4RWu2-zIcxrcGuzeY3pdJvqjzDs6n1xmMizHKHe2G6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fS_jnkbRgsT6cGstvtpMFuCZQFrYJ8w0e2A_HbiboOHvw9BaAzXtNvtGU2bNcCd4EJDCcAn-zG0Q8UmMGIP3t3uDXOWgbC5KaWV4dberTJ0m-RzaJ97k6iNKahGGSCiifWBq_G7emmlZxlMnuHUafF9-p1yvdQnV776lUf2vL2FsIjHA8zKWt5_0-xQMycgpP2xyXGnawbZbh0PJgd2D-SrFazB_hxsyLX4hDVOSVPdmO8aXuoBR0a8el-8OFbPDrD-bc2TQm35bRdLxPNvRN_ynxakWD75tjzJdEgFyAQXIrA7uiBgBxDpsD3LNLplf41Xf3jLRe7GmQLsqIkfmQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
🇭🇹
ترکیب رسمی مراکش و هائیتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/Futball180TV/95711" target="_blank">📅 00:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95709">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بوسنی گل سوم رو زد</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/95709" target="_blank">📅 00:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95708">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2d46d4a5b.mp4?token=hhsvZnT96Y5LboZuBhHOLMpnw6ABCByBNo2Fp9AS9SbmZGdGxdYV_TRQZmO8MkMDaK0XkUAUZG_BM8_vudgaNNJD5R_7vQilxn_P_UH3WW-uztDlmVdefrqctsIC_ABOw5jGE7y0K1flx9SXbZv4qfqHx6S5gd5Mhrn6r35pJyGiYUCjfaUd3gxRyvkGkoWdg35ueIUidKhZF2p4sFQIJBisopqPNTfHM0z_Hex103tbCgU70JhQnRUI08yXoPsdAa254qkA4-zEqWOyUGX3hyH3j8ik4Gv4V_S7YM5mi34m1wYqW6gQgMr4mdV3Bn03WrQfEgx6OPKxZ98DMsLQqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2d46d4a5b.mp4?token=hhsvZnT96Y5LboZuBhHOLMpnw6ABCByBNo2Fp9AS9SbmZGdGxdYV_TRQZmO8MkMDaK0XkUAUZG_BM8_vudgaNNJD5R_7vQilxn_P_UH3WW-uztDlmVdefrqctsIC_ABOw5jGE7y0K1flx9SXbZv4qfqHx6S5gd5Mhrn6r35pJyGiYUCjfaUd3gxRyvkGkoWdg35ueIUidKhZF2p4sFQIJBisopqPNTfHM0z_Hex103tbCgU70JhQnRUI08yXoPsdAa254qkA4-zEqWOyUGX3hyH3j8ik4Gv4V_S7YM5mi34m1wYqW6gQgMr4mdV3Bn03WrQfEgx6OPKxZ98DMsLQqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
گل اول کانادا به سوئیس توسط دیوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/Futball180TV/95708" target="_blank">📅 00:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95707">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گلللللللللللل کانادااااا</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/Futball180TV/95707" target="_blank">📅 00:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95706">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pdd2JZ_dXzcAYjl62HmZKTEGkQUy_BWPt6HSfSeCrqqSQ511hWTQNPHLFayi09B4Xt7dVuHPqKSGRfTYDgoNVq6FNk9zb0PlOmzKPjJ06C__LWeLk5IBBiuDluFjV0DF5STqlqQXh-fXE1sw0SVLTZETjyvpIiVUy9BLHIsuCLf2SZhxV0B3Rrg1fy64bBaVlWM4xcLwujHT9IMcIg4tE0xoD2YcQ0T7AUrRq0xFFVL-IsB35AYQMIeP-goHOd9fheQY-T9FDxoUG9WT5_jwNnsHL0iAom9BPA0dmcwWBPwvZu1PNkMDz3AGKsw0jShyiBDXsV879HcD5TXfhW1DIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
حضور نیمار در استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/95706" target="_blank">📅 00:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95705">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇧🇷
ترکیب رسمی برزیل؛ نیمار نیمکت
❌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/Futball180TV/95705" target="_blank">📅 00:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95702">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02624180b0.mp4?token=akZaJd-PIqSJjJ8io6R2rWTBSHZDwpp728eotc1fy7N9Rp3oFiqoz3szLHrtQCWHay2QtM0vPdPSaru6YJ76yLhPkZXPqhcanEK7Ze18yCznO_K9pUPzQNYeRa8NNdHVhQAxSjK10S9aXVRQdaRlL1e8iR9oLcjCjUyEcY14TUsMZUkjiDZzj8PMP3CKsP0OxINL4FcAS_-zPPWAdNaklG7gRgQrkPaA3is3lgvjW9nMTpav64JK8V_fbX0ojnzSA17SWOViEc4Ln5PaOf4krc0ZRV8pWzfI0z_YPNOkl3XuxwtI6OhWFea_FrbV5P50KvOZLRA0w8IJbIG13mtQLlaycBXi7-XMm6qmCSaOjXYF4kZOLtFz-1XxNl51ouPCN0aBV-bPsUCOERPSKcH2oz3ze6jT7oxktsHNIjtoC49jnCoxv9qVQT1lVVztEqawJ_rlhfbiJet9P1G0eToPLF-q-aGy8bt4OZt-QYru-XI0hBqU8hMJ1Q3nmCL6L8AhgstUQIS7jGQwU-WcAGY9R0FskHzB7Cx1DsPU0_wCXOVbMe1h26jhKU_bqL--nAYLgi7yzK0aGbvBloIjexzkVGi0QrCqsAhDfKiaPok8CBGYDxPMx7uoam4hvVeQ0A__V_ifBiD_T9EYLInujKGzS3WHt7VzRwk0nvhT849cGvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02624180b0.mp4?token=akZaJd-PIqSJjJ8io6R2rWTBSHZDwpp728eotc1fy7N9Rp3oFiqoz3szLHrtQCWHay2QtM0vPdPSaru6YJ76yLhPkZXPqhcanEK7Ze18yCznO_K9pUPzQNYeRa8NNdHVhQAxSjK10S9aXVRQdaRlL1e8iR9oLcjCjUyEcY14TUsMZUkjiDZzj8PMP3CKsP0OxINL4FcAS_-zPPWAdNaklG7gRgQrkPaA3is3lgvjW9nMTpav64JK8V_fbX0ojnzSA17SWOViEc4Ln5PaOf4krc0ZRV8pWzfI0z_YPNOkl3XuxwtI6OhWFea_FrbV5P50KvOZLRA0w8IJbIG13mtQLlaycBXi7-XMm6qmCSaOjXYF4kZOLtFz-1XxNl51ouPCN0aBV-bPsUCOERPSKcH2oz3ze6jT7oxktsHNIjtoC49jnCoxv9qVQT1lVVztEqawJ_rlhfbiJet9P1G0eToPLF-q-aGy8bt4OZt-QYru-XI0hBqU8hMJ1Q3nmCL6L8AhgstUQIS7jGQwU-WcAGY9R0FskHzB7Cx1DsPU0_wCXOVbMe1h26jhKU_bqL--nAYLgi7yzK0aGbvBloIjexzkVGi0QrCqsAhDfKiaPok8CBGYDxPMx7uoam4hvVeQ0A__V_ifBiD_T9EYLInujKGzS3WHt7VzRwk0nvhT849cGvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل دوم سوئیس به کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/95702" target="_blank">📅 23:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95701">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مانزامبی واسه سوئیس گل زد</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/95701" target="_blank">📅 23:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95700">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پایان ست دوم  فرانسه 1
➖
1 ایران
🇫🇷
25|23
🇮🇷
21|25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95700" target="_blank">📅 23:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95699">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0f2acf61e0.mp4?token=t0YDY_uPO-N9lhEhWq4UdNQozCDEW0QDVEWeFQqeVgsd-n_L1OYji7a0OLISjLzc353Df0kFoq7PIfK5hesX0WfH8XBp-MpqveSgjWNbo_zhyF8OvtyZa-jvwg9ggZo0811Qyq0BTLiqXX6xZkbMtr9JwyNaDjPCsXqNMfrvOnKY4AcHoygu1KYdQd3ubBAiQRxDWwsAih-7sB-0w3-gpzbBrtlxlLu0d19pnb4b6NmeJeRY1PVDfx8HtJBnU4nq55j3IecfINh0cJDbe8z5eL6E-G3NireAYehItGEwNquARwfEJU9Z72ko39yTv00mskSHdJeCGhxJncjELCFe9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0f2acf61e0.mp4?token=t0YDY_uPO-N9lhEhWq4UdNQozCDEW0QDVEWeFQqeVgsd-n_L1OYji7a0OLISjLzc353Df0kFoq7PIfK5hesX0WfH8XBp-MpqveSgjWNbo_zhyF8OvtyZa-jvwg9ggZo0811Qyq0BTLiqXX6xZkbMtr9JwyNaDjPCsXqNMfrvOnKY4AcHoygu1KYdQd3ubBAiQRxDWwsAih-7sB-0w3-gpzbBrtlxlLu0d19pnb4b6NmeJeRY1PVDfx8HtJBnU4nq55j3IecfINh0cJDbe8z5eL6E-G3NireAYehItGEwNquARwfEJU9Z72ko39yTv00mskSHdJeCGhxJncjELCFe9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇭
گل اول سوئیس به کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95699" target="_blank">📅 23:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95698">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سوئیس زد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95698" target="_blank">📅 23:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95697">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95697" target="_blank">📅 23:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95696">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">نیمه دوم بازیها شروع شد</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95696" target="_blank">📅 23:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95695">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdwKX3Met9VxBUfGBR2evkiXgYZN0XeWO-UiA3108ummnITwN12yZ-maidyYU5RlmTA03Pv6nPTS_3re6Ap4bJVXn6Ci63ly1oQFdPkY86cVrutS35qtZZNnaxCClUECNpjqKWmH1jSQlHAK2RrM6uZ-wES5x4bOXk6KuxG74XpNpIsQqxLLwKQtp9YbU5DwP3mynnaaZF64mTpkWK0EzVwYLQELRGxlxn8wXxWP-qiWfgTzAEl3CL7HiUeoTptuqvl5C_twzACWeuXsHawOXlxMQpx78wa-ehMhn7Q3x0nwFAuIdrIq6vEwJ5blenSKyVD6I2hGOOYj09kaOUu97g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قطر پس از بلغارستان (دو گل در سال 1966) و روسیه (2 گل در سال 2018) به سومین تیم تاریخ جام جهانی تبدیل شد که در یک دوره از این مسابقات دو گل به خودی دریافت میکند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95695" target="_blank">📅 23:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95694">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ls-Q6SgWhBKsoPy7UbO3PoqjBFManPUMpW9nHW7jucll-Zm5hQ0co10BCJJa0rbZkjL1EwO_jy1FDPehwTwQ9MK2AhRmSvKQ8hCerM3nexh_zPkBy4csbxj9OZTMQ_betwZwgRUfj8AcgCngb64TYDYkVXT_Y7gabLQR7M4cn_O33Ej1btbcB8dQ3L8sh_V2U9BPv6j--tDv4guvbe_gmh1pjyBPwvmUzKXDd60Jl42L1HbfMF8tpHIMtgeqjo6cS9wUEvCPJr9axawuD2_4kqLBWjp7fN3WXK9on92mM5D7VYaAyCb8Uyv0I_c8tzLsjavF96xmZOqXrO6FbSwdxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل اول بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/95694" target="_blank">📅 23:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95693">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پایان نیمه اول
🇧🇦
بوسنی 2 -
🇶🇦
قطر 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95693" target="_blank">📅 23:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95692">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پایان نیمه اول
🇨🇦
کانادا 0 -
🇨🇭
سوئیس 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/95692" target="_blank">📅 23:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95691">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bd323002a.mp4?token=Uc9htXNa6IyPBINv-TJ0ZebilZf82vkDPrdFew9nrTtAjbU1fIVaJpJ07nchFo1IkpbGZlozz1zZeLIiphgyWWGk5WJpCgdXmjg-ICa3X_XVjCHEqAszdFU6Xw74ajUMP2oufkmMem_f5qpUhaAJpJhpPfyNusz04ZgIhgN3MGY_8QI7MZC4YUa5nTqhxYLgM8yHEA4b_jguBCK6cTE6IOZvJMW4ZaOjsi7sKnXmcLoX1z6YPO1yZKvSlEfBRTzMyfLq0duHDtbfERYicL9C1X1h2XCBn-rQSxYj-D814sVprNcWu75ypQkeI6ZD8fuD3u6S-E-AX0QFUCWXY559rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bd323002a.mp4?token=Uc9htXNa6IyPBINv-TJ0ZebilZf82vkDPrdFew9nrTtAjbU1fIVaJpJ07nchFo1IkpbGZlozz1zZeLIiphgyWWGk5WJpCgdXmjg-ICa3X_XVjCHEqAszdFU6Xw74ajUMP2oufkmMem_f5qpUhaAJpJhpPfyNusz04ZgIhgN3MGY_8QI7MZC4YUa5nTqhxYLgM8yHEA4b_jguBCK6cTE6IOZvJMW4ZaOjsi7sKnXmcLoX1z6YPO1yZKvSlEfBRTzMyfLq0duHDtbfERYicL9C1X1h2XCBn-rQSxYj-D814sVprNcWu75ypQkeI6ZD8fuD3u6S-E-AX0QFUCWXY559rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول قطر به بوسنی توسط الهیدوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/Futball180TV/95691" target="_blank">📅 23:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95690">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قطر اولی رو زدد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/95690" target="_blank">📅 23:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95689">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c442b447e2.mp4?token=sloo2ok2TjHLT8C8JWDsY07EB_tX12R9_IQ_pbeyyq0cbL6F98HiF0sK7sHyxozxztw-niARiL8uhv3bEzBBTPvVW3dw0z2vCBF6OwAWT1K_vkvBo2x0puUGqIMYcs2_zY83QnEvCUeIjYN84pMgYIF_VOkv853AmcTnZh_NrtYWlkirCl_fIgWQlrYlbJMGVwrhAF7X-QVweM7RcY6mfj0D6dGiP_MEpdaL3dBd0MyFlUVIKMuR3WbbwZK7sp-SEo8NhUj59SoJ1lKWbicxZbW6Nu81QAqe__ZbypARG-RGQKxZu5dlGtcDqpt8vXUiclzmL7MW7XSXsqdvneOuRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c442b447e2.mp4?token=sloo2ok2TjHLT8C8JWDsY07EB_tX12R9_IQ_pbeyyq0cbL6F98HiF0sK7sHyxozxztw-niARiL8uhv3bEzBBTPvVW3dw0z2vCBF6OwAWT1K_vkvBo2x0puUGqIMYcs2_zY83QnEvCUeIjYN84pMgYIF_VOkv853AmcTnZh_NrtYWlkirCl_fIgWQlrYlbJMGVwrhAF7X-QVweM7RcY6mfj0D6dGiP_MEpdaL3dBd0MyFlUVIKMuR3WbbwZK7sp-SEo8NhUj59SoJ1lKWbicxZbW6Nu81QAqe__ZbypARG-RGQKxZu5dlGtcDqpt8vXUiclzmL7MW7XSXsqdvneOuRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/95689" target="_blank">📅 23:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95688">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d8b44c8d2.mp4?token=drxtdSux1sHGvQ5m7mHARvL05wvZtGzeALF_Hzd3PHs1Q9fu9jTOjBbU-v1Lnnlu-aTIj7GtM3ftfZ4qTxnMOLrY2mk-9R8d2MM22iQ4e18Hqtv4UnyR_XT_JeX0Zp50a682-XmYoVOxxHfbG3jNV2GlZhRj0UfbWGGKEuoNG8Hu5DxgzpFJoniDtd1TQOCTrXxj4Ozq9eBX6L9IQMB8fLzcEfcDglBDZHVoyYlhqnyijE9ubLHToBT8farE2B2pQEUcI8i7F2xYojs6lTB7qOf7I_GNhaes83kaZYjHorAuSXLiM80WbSq73q68LmBNjenGOlzMpsQVJKldjMR1jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d8b44c8d2.mp4?token=drxtdSux1sHGvQ5m7mHARvL05wvZtGzeALF_Hzd3PHs1Q9fu9jTOjBbU-v1Lnnlu-aTIj7GtM3ftfZ4qTxnMOLrY2mk-9R8d2MM22iQ4e18Hqtv4UnyR_XT_JeX0Zp50a682-XmYoVOxxHfbG3jNV2GlZhRj0UfbWGGKEuoNG8Hu5DxgzpFJoniDtd1TQOCTrXxj4Ozq9eBX6L9IQMB8fLzcEfcDglBDZHVoyYlhqnyijE9ubLHToBT8farE2B2pQEUcI8i7F2xYojs6lTB7qOf7I_GNhaes83kaZYjHorAuSXLiM80WbSq73q68LmBNjenGOlzMpsQVJKldjMR1jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول بوسنی به قطر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/95688" target="_blank">📅 23:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95687">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">لیگ ملت‌های والیبال / پایان ست اول  فرانسه 1
➖
0 ایران
🇫🇷
25
🇮🇷
21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/95687" target="_blank">📅 23:08 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95686">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گلللل بوسنی دومی هم زدد</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/95686" target="_blank">📅 23:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95685">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بوسنی اولی رو زد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/95685" target="_blank">📅 22:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95684">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/95684" target="_blank">📅 22:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95683">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4b0b9366.mp4?token=bnoxWS-eBeW0Io3Sb8bZdrQywnFi5ip63hbwSWR7C3hJBsXR_iJHV4fpEzjI1EXz9_iQ5_PjL3o_4lJb4Cy0U5KnUXYQb-cjhlvfztFwFAcPeCfxlaauGFTwxvZa7juirfSkn0cQaTT_ybxfCtQT1D42ggUsTkvKEIos9Lf1h1QTrqOH3Zt2ppVvoPNBV384qACY8QCAOyyqG462vuNMY-lnRT3hd1RMH7J-zjAJ8L3_5vBbRKkP_-EbT6IXZ3vwpgjVTK4Lm9easXoPpPHUG8ZS19xw_z_CgDe-08KBMJj8J68njKzFtsQNQDp7BmIJUnHvDbmomYZRRiQ_ynVNEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4b0b9366.mp4?token=bnoxWS-eBeW0Io3Sb8bZdrQywnFi5ip63hbwSWR7C3hJBsXR_iJHV4fpEzjI1EXz9_iQ5_PjL3o_4lJb4Cy0U5KnUXYQb-cjhlvfztFwFAcPeCfxlaauGFTwxvZa7juirfSkn0cQaTT_ybxfCtQT1D42ggUsTkvKEIos9Lf1h1QTrqOH3Zt2ppVvoPNBV384qACY8QCAOyyqG462vuNMY-lnRT3hd1RMH7J-zjAJ8L3_5vBbRKkP_-EbT6IXZ3vwpgjVTK4Lm9easXoPpPHUG8ZS19xw_z_CgDe-08KBMJj8J68njKzFtsQNQDp7BmIJUnHvDbmomYZRRiQ_ynVNEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کوکسل بابا امشب عربستان فنه
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/95683" target="_blank">📅 22:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95682">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH0vdUiTYSYQJ_RoCwM0deH7fxxBSwOonaTxCRWNuXJe0oyjwJYeuRp7gzIxHrxZURYQ0LA-GKhAsfz97NUiDFpJZ6WQf6vq_CoUeQ-1zJwQpGF5M6VIcjXSmi3GX4TAYr50oulsl-d_kdswLC9Vgze_jBhVuCaekoM47uRHXixPBLPV1vQOQRTbrqnCcrifz0zYsuGQUG7Eb3Y_tAw7Obfa_YB78y4nmRdj8FAA_I3ULIRtfyRNUYGpPUE9Rtb2Vc9_3y7afcc8H1EPmlSjl2P6YxTfw1rYT1LOHbl6JQ8Xl_SebqN4Tjd5FQezBzI8-o0ZwSPsdkiYbSRszjnkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جان تری و هوادار غنا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/95682" target="_blank">📅 22:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95681">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CeospXER6x3s4GGAxAYD2BR4PaK5a7UZoBb4EnyterMDhoZj8cMWTBbyHsFUg9uo7e0vsnReTEJOZ_m_n5xX5-0bNZJCpEWGM8h9c48mTrGbzPyds6qUrXITpcXMIR0J4AE8xukvQ9HECDBpHZvlKnmve3IfvZDT78fNMzRaGJXocCMqkNXhBMvxqRYhsjhCMOO7PCMeUiaAu4kJI1BcTzYs10ba_pDXmgGFE-ZUuF0Tpap9dPqoRMZEPSR7zjUwPVnwBwSQ4EU8AbnJZRTz1jqPV6ZlKTow7b4BPrc8lsBAgPa6WtykjuYBACM9wSLKUogHLqWb10smsL0R990lHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست رونالدو تو 24 ساعت 25 میلیون لایک گرفت
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/95681" target="_blank">📅 22:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95680">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/95680" target="_blank">📅 22:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95679">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/U1I0FopIAcubPscUHwXBZmK9MdFxfkaR2BWui0RqlV-i-FXG7FNXM-SPK5FGc5WlcA5DF4gcM0nTmM7YyTf9KOYWdPhpaRLBIifiGMe-XjaZB74CO-6My8Ugdya_mwV_5xhgQ7DcjrmqzolfmcaHurBHZR_2vMvgPbvAvk3mJ8yZnBVoyetz1GDNrPhkGTELoBUPBju_J7JhEAAPz3ZKW5PlEhcAWX4qhcU97FvjFTvLqb8LVouvWMSMt-Y6PVPIkyerrQnaidrBglnk5pVZRwoRimzg27Xyk10qjnd9i40jz8Zry4nFl7SZmd4p5lsFl4213vRS6-joMHLRSLlHYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95679" target="_blank">📅 22:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95678">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بازی کانادا - سوئیس و بوسنی- قطر شروع شد.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/95678" target="_blank">📅 22:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95677">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لیگ ملت‌های والیبال / پایان ست اول
فرانسه 1
➖
0 ایران
🇫🇷
25
🇮🇷
21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/95677" target="_blank">📅 22:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95676">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N12iIP1wiQzdwImc1Izs990SxneDXyuSlp3D_kWZ-XAiXMrkyPOIWLVgmqqHbKShc2zvNDp5r8gAmGan24Tn3Ena6M0lTRRykT-VUXrkj-z8tq-CQU2shRWEsvHjqBE8fCspObCoyUCKV5M-GJTDPAZyu1N6_2UfHLhQg8wRyEzTC46thU6l7e46CX-lHrha7Mt9cQ_-pab5ps62T4EdqNQwAaqjeS7vGFq7ZzKd1nt_Jf7eKIptrKHV-RH5o991TOmVixsq1Q2XsLp8eldp4MLIeftmkAq5Y1tq6fJ4s0vadFC3Fg9fXzbmNrRqGXrMwkmAk0HC8wRsJ6ipiiRefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت پای کونه بازیکن کانادا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/95676" target="_blank">📅 22:27 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95675">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgi3E6MIAZnRgOsQHUOGM9wfJF95SglCg2wFj7RFRZY_O6mw2V8JN2RZjXMKDAJHWQyl-w3TupUlRpMiiXUwM7DhQUlf7n84ItUZZUyR0zBZOqQbsYw7hFGjnWkEknZybmd1EEqh7QXGLKliMs5-7JmeJoJTgdtO8Knza94D4VY_UC7qyD0a-UD6-oxK8dw7TJOiz7JRJ4FYG9eSs8bv8IE_hFola_e4nBF4_PBo5Mu9dx6AdvYDGIjEzPK57EhzuCOrtGfjajc6YxeaK73k9TwOrvH24IU5mResn7mml-rKxu08OuKB1L0LMcGiXPFr_pOjO0_4RmB6dkDp3ZMDFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانو آلیشا لمن فوتبالیست معروف با این کاکا سیاه ریخته رو هم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95675" target="_blank">📅 22:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95674">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5w9De60gL-qk2wT0uoYXHdv3Nn8IJImUai6r7YRTAftxXVDSRGOzoRDp6Vpetrsv0lCFN1aMfQHar1_YN_RPeddmmOcgO7rd84lp1wfSLQixc_xXIVG08iLKOzVitjYJ9JzCLXiWPexddbWOZtyY55N12vfKt-D8Eeqy5veORqGc-qB3Nd9Vx3k-Sfd9pyH80jfkDaa0TNY2whg0U75XzmS50sYLBAQ6DwpIK2rZZlnoyxcESf98SpAyY0DhmTXQ-gxAs0XIZriSzjXGE2FiGoHkT-BxJWBW7EN-M8JDIOwobXVnENLUWikRvtgSkUYqq8TzhR2AfhW6lBC1s1VoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مارک کوکوریا:
انزو فرناندز به من بابت پیوستن به رئال مادرید تبریک گفت، امیدوارم اونم خوش شانس باشه و باهم هم‌تیمی بشیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/95674" target="_blank">📅 22:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95672">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bz9aAbJ_K8_vgtwC8EAKTLksFJsqQgjZfgmsG9N3RYzshW6jFBwWoeYrKI0Oc0L19TVKF0tUEej8zz2udP7Rdq-FgPmMpXDXn1OZiwJv92ZcFAD-_6OKk3ZoLw3YtGr7MIPyXtc3Z7nk6FScP9h16ix-YweKQnEbXR4VHAwWv_iBurwNnnKGQnJWW7GAuDYwC7nVkAWwaXw2-cJ9n40MndY-cL19WKxwy3Ka-bEMNK5RL2wr2BNewUYef4M8D2LlXIMqoUitxhkuZZB8LcF47HVw5mywLh_6UHswnLOktL0MB53eldxwNKfit8U5ebK2S_ZNQCUw92O-iCgNREuo9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SJi2Mz54wCnULET-o69zZw70Bd-0z7KxitDh17pXyYpdy-_HtymyL-cqFOh5bOnaCamXZ6MFqdcNRTBDRBvm67zGmxFwou0wrpnuFlIGgpnCHVRWAeGaeJY3bY8WR2q4kbianIpytz3aBmw58Ccy2lwXmoDY0KRc0GtRJ0wjKm_PFyDnn07lwsY2bsaz5mT_fNtf6FfFxoDVmESNgX8DTVQdP_AehSJKNpVNgPrseh5gYi4RkTWAjmOQAP2HP9FNEYBXma2cODsEproRhM-4JY4zRjbRIV5d0ZfxNYmJJwkbScVZ9fEoBN7amZV_YmS-Hm-Jx3ycW85n0kYyA_8lAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من که فن رونالدو شدم شمارو نمی‌دونم
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/95672" target="_blank">📅 22:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95671">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCcpQT4YUGV1DR5FVh47_uF7hNfSQn7W2QxyOeFTtba4ZCR8u9HjkPEMZb9IwMnlw7qOgt3XpCzchOg2LQjQi7V_rHoiKGeC210eqvwO7nS6EAuo7lDZLWTIGx83jkaupbdWcBKSn8pdPRRLM_x7WNsCF6kie0w-zLZCS-QNHLRoaNqywzNIZst7G9kRrREnRrpVXgABucKzliPYk1NMpu5K0YS0yuCiv4Pxfqxc-KTGAnjR3qfwtkg_aLkwC83b0nU7GFqlPmyYn_4geGSCJv3rroc0_MoUD_e-gVNzp3d9WpormuoE_0nhVd5QWeC7OKvYWTjGmcx7Rh8gmjDgTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
فورییییییی از کریستین فالک:
🔵
منچسترسیتی هم به جمع مشتریان مایکل اولیسه اضافه شده و اون رو زیر نظر داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/95671" target="_blank">📅 22:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95670">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff2b449ef1.mp4?token=Y-hTTi7cbirSTa3tedukOvGDWtFOEi5kvAI3Om2BwRmW-gKW85QHWQnyS4av06CRd6iMNkRTAulkzhBy7WoFpM9XyHXTAbltaaqI6TltEzRIeUWzgVZ6RUnGwMu5r7uFwW0-vMD7R1C4EV8xYGRHoFY8jCo9_Wvq9pgMXBIGs-54_EiQqozUlGZuoRFJ-mukWGSb-8sLmpJkVUA46-j32lo3qUbRDX56ViybBgqjiEAPmAqeK426rQMm_ecAcWZOAOqVCAvwtDMSYiG2Zvxw4TngRY9U39CU8ARkdf9EXDTsPiMIrnn7yqLncAWswSXRj0qffK0aNMSTTO1Ei2YOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff2b449ef1.mp4?token=Y-hTTi7cbirSTa3tedukOvGDWtFOEi5kvAI3Om2BwRmW-gKW85QHWQnyS4av06CRd6iMNkRTAulkzhBy7WoFpM9XyHXTAbltaaqI6TltEzRIeUWzgVZ6RUnGwMu5r7uFwW0-vMD7R1C4EV8xYGRHoFY8jCo9_Wvq9pgMXBIGs-54_EiQqozUlGZuoRFJ-mukWGSb-8sLmpJkVUA46-j32lo3qUbRDX56ViybBgqjiEAPmAqeK426rQMm_ecAcWZOAOqVCAvwtDMSYiG2Zvxw4TngRY9U39CU8ARkdf9EXDTsPiMIrnn7yqLncAWswSXRj0qffK0aNMSTTO1Ei2YOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگر آبجو رو بریزی، باید اندریک رو در ترکیب قرار بدی.
آنچلوتی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95670" target="_blank">📅 22:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95669">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUWvIv7u5n1UPG_Y625NJ30sSoX4LqK0iTjNuggaYch4RbGjsc2xTOzJYwOpQQbfkoclQWjGuPFwcPkD5ohjMTXCXRvbMimHN_NMoDvOwRAkmhUuSWkRsWZePA9UtfsOdnyWbP-tD5Dfs4kJA_0BmIvP7Ofi7Ri_hAnfDfuYZtQvjMCUVdfh3KlyAmIYgPjc4Y7G9z1BeI5Z5VFnh-qiWAlJgHnrkq-05X6b1H05J_6Ar74lZ2AUrLGkR27DaNEgTrDL8wKEAL-wTLSMloXRzo1gim40mgusLz72akvqbiL0hqaTzgLR7qV0qtmTYMc_zSftlXTyhDpRKs4HLqx9bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🍰
آنتونلا، همسر مسی، در اینستاگرام:
تولدت مبارک عشق زندگی من، امیدوارم امروز و همیشه خوشحال باشی. ما از قبل هر چیزی که لازم داریم را داریم، چون تو را داریم. بی‌نهایت دوستت دارم.
💙
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95669" target="_blank">📅 21:50 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7OuRpYO4pA8sphiQrzMlrxl2Qv1IT7spm-pr5VaRCH9ViWw40WynUKwnPuvpuVWwpWZ4oUu0XFz9TdzfX36_PkJFCzV3aHx4xNoCWuXmEfQwzcrXyKXCzeHgTJKESkfmc56AvZI6vciU-eWUFGlvO0qqBwn7hdtzJjXQIFw94hTSXrsnJYFuSWjKq_B7--MpcUGyIL_ASXtanGW2nrclpZWaJA-_I5u_GsZxWkqNcS8sFJrHl4obdFBQD-o2hfmXJznyjacKzdacP6sBUrQTbkDlDI91nHXvMEkOkB-2JAT7vIC-otsxeMyig789RM6MonQBrWDWbY3biR48-1-Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GxysGXH77JaNPGeQsRDeGR1Uj_6eU-Na19u81OBs9KrPAXmFdkZWQJ--mBoEgFgLMOGTJ0UdaN4xdQPvkukkYk2WscG2_XzOM0_ETH_X2WjLryJCcatxdRV_fK2IqYpLUhhirrhg6TxUwfRH0eiLrpzbVbFRWg_FMwHPSKdLyu8xt0-jjaU9oalgDM2yLJlKhKI14eXo1RCEG2iKMsAZM3rV8AzodPVei9PcjTA450ZxpTih0b2MhnS47QSUUiE1kB-Kl8ssxNkMPOJmE6-E5KZF4-viSX2_3aSIWRiwS7768YHhGvATKPnLsXoRZP8N3VNPOWJpfgv30ciTawn9qQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
‼️
یک پیشگوی برزیلی ادعا کرده امشب یک بشقاب‌پرنده در جریان بازی برزیل و اسکاتلند در جام جهانی ۲۰۲۶ بالای ورزشگاه هارد راک ظاهر میشه و بازیکنان، داوران و هواداران مقابل دوربین‌های زنده توسط موجودات فضایی ربوده میشن!
🛸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/95667" target="_blank">📅 21:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrVknjEy9fW5zT2RLwk_2mReAL9a7mEDOiwr0_xpUWEawL04C-z8enFjnpznEloiHQ9K8XUuqWL3JMnhLFFmutlGBuQLXJTJKuxq0UQ6aFanhvyY32A8n3P3T5e1s85CK35FNoDeks45bf_bbseJeZP1ogUUdfC_AZ0hPL1IAkQ9QOALyWgkLscqV4PKB3DKeinmzZC9RVP1oTvTRfRDR2Q8Lp2RdRYvIWeswzEbXaH9v5vEvQvu0X2TeG9RAlh5NzvUwqK6M4Egag0NAVQxqLHoisdWRskGmw5gJ4tOw6DG6k2q_Oa8K9RxoB1wxXiFZVTq_2FsPJlEixKTm3HyoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین با پیراهن دوم مقابل اردن بازی خواهد کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/95666" target="_blank">📅 21:15 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bb8c2d239.mp4?token=uHlbDbBDslfwHTY4LA6PmZROL2RZq1FwyjwMCI2NVFSjoRQZIVPKfbkgNeSC_OS7nbN80Xvi0FiVAtrxPGJ7NzMAanhZ4bGpDOsTBikM-yXXFP1cyMq6aSOV3XWy_ROQBi_z91QWuIVD_3_QHnsl3TMjTpcBB3V-Jrlh67abGaT38CAdLwt85Cz7yoSNgqvSmOmpIpjyfM9CbwwOwMm27k3eXcjPuUJgrhaPhZmsOygnXZUQeGDXq7p2WsU_-lIl0lpe3Ta8cn2MYu1Dx60b2pEnNHxgNTJG_9pvwv8WJs_AxNXYRBc0Ac2olfxUb7gL6b7UvtpXwZ3QQGx7-fz8Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bb8c2d239.mp4?token=uHlbDbBDslfwHTY4LA6PmZROL2RZq1FwyjwMCI2NVFSjoRQZIVPKfbkgNeSC_OS7nbN80Xvi0FiVAtrxPGJ7NzMAanhZ4bGpDOsTBikM-yXXFP1cyMq6aSOV3XWy_ROQBi_z91QWuIVD_3_QHnsl3TMjTpcBB3V-Jrlh67abGaT38CAdLwt85Cz7yoSNgqvSmOmpIpjyfM9CbwwOwMm27k3eXcjPuUJgrhaPhZmsOygnXZUQeGDXq7p2WsU_-lIl0lpe3Ta8cn2MYu1Dx60b2pEnNHxgNTJG_9pvwv8WJs_AxNXYRBc0Ac2olfxUb7gL6b7UvtpXwZ3QQGx7-fz8Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جان تری و هوادار غنا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/95665" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95662">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ogv6rXiuFBKkc9gasOKqF0DTSONic95lDkKOp0BcoZwmajiplhaRvaCxaU1lbNKsCQSgc6XJWB32bhcVe_jIISGEK2nK1BbMo_glBkpS4TEKeSOmqZWIsOgjr6qxIT9nxnVTa4gcslivkIpDTcxfJBEWZ870hR1xYdNoF-v3LPQCaxV2l2Nd2PbDLYCDnDpyz28k4WezORkbCWX-1BBmbzSzbrhwvNZowI3HOkBww6obxZg7F8oKQ8pUniiJrWLgZbHg63eZXFE7N5Hje_NGnQs_o3YL0qbMWVLYBz3Fji553CAzODXhQWsmpv0Y7FU2mWlO1EzdrL5RqXojf1GItA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQ2sJ_gMW5tzRImDGM_-ZjFG4gkpnQDECmUsZmEP4WifVpySMTuz0NT4XFRtpKP91GHMh1mbyaJO2D1Z79lwiGZq1nqbcXq1jBKdn79eIDFPdOHNL9BtMuLmWS1n7ohAmGG5PuBlTvgsQ8pry4lkIhWbqIYpVHLS-_4sJug1cHa4WGducg0FsI-YYm6wc8MUUJB8BhN-EnuqEX_x-mV9pnC7hLSPGAwdbLwpQrG-zocA9oXRNrC8JGxw0kCL3I_OVB0w-gTRfnVd8YmV5ylKJOEC6t1y6uxukAqImhYwL69PBFuDrLyiqgEhmpUyrAIpaplFUZGvY3Mt5NVUND739Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇦
🆚
🇨🇭
🗓️
۳ تیر
⏰
۲۲:۳۰
کانادا
🆚
سوییس
📌
صعود مشترک میزبان و سوییس یا یک شگفتی دیگر؟
جایی که هر دو تیم در موقعیت ایده‌آل قرار دارند و این دیدار می‌تواند مسیر صعود گروه را نهایی کند.
⚽
🔥
کانادا، یکی از میزبان‌های این دوره که با عملکردی خوب و کسب ۴ امتیاز از دو بازی قبلی در صدر جدول قرار گرفته و حالا با حمایت هوادارانش به دنبال قطعی کردن صعود است در مقابل سوییس، تیمی منسجم و با ثبات از اروپا که او هم با ۴ امتیاز شرایط مشابهی دارد و در صورت کسب پیروزی در این بازی می‌تواند معادلات صدر را تغییر دهد و حتی به تنهایی صدرنشین شود.
🚀
⚡️
آیا کانادا در خانه صعودش را جشن می‌گیرد؟
یا سوییس با یک برد بزرگ، همه چیز را تغییر می‌دهد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/95662" target="_blank">📅 21:14 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95660">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MZK5CL97yImuj2rYI_ynUyLrWqdYEhe24zFJjl5di-KS70xIsCwiGZyjhiE5dGfkxxM18lzJDA-AUzcGmZVkE8ZP1lRDddzOYsRoFPpQoFRzwyHXxRFA0GP8EcHfP-q_J0_BKw0gcNQoTd1ni50l6DMQb4P03_D_rjkwJyGhN4ZVXp_7xGpDqX3KEP47YmycZ0Azh5M6ZNJEd-TvbdHpEKjZylt9tDfYbtebAW7-udiy_O-kShdskp3kpMiB2PTB2Tw4AWA7mzoT19EJbvvS6pmt9I-ZJBB_r6xbiHQeWKpTKpnmYYsfCB_sIaTPJyjr6i0co2ttCSTQ2mV8-05RRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OPiXIZ7AaBf7JekACsZh7Fv-8NLO1TVGeq4IV21j_IEBp_mTj225nfLYIzsuj4PJgdoB6QL8zVztaV3iCWInpT2kP_4l8h2jZTlI0oNTtuNP3rK-ZgId17NdY1ZSMTe4_L3Uv-CRg-WvKklQYcykGOdbAx3gtk40JRt0owC76HaFcD_jbmVikBCxIqH7wE73IU2rGY1_7dW1kXZAFwe4BiSi7T38yfs2m2j54kEADr0Ff8EL8HAJP2lJNmeMeqTr8MEZbrZMSwi1yed3ORrqyxeqdLf9mT2eJcPRURJKmpwOdXOojXcvm9gxXZN3eA4EQpL_dr40Y7lDLS81B29rEw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇦
🇨🇭
ترکیب رسمی کانادا و سوئیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/95660" target="_blank">📅 21:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/riY-yE4xsXvHocHoNfmIZlVgdl7EXcKUAyDhINflF5zBYketylzRUB-mDE5GumkcDiXXDbeJILycJDE9xjnK47XnFWpY7GPmD2qcsZPvmoZRt0yFUnMm7pI5QcTkksLM-ibI76etYXMt7ZNn73t-XtkZqpuXKeZK064EjkQbsZE3yveWZRsVrYf9CHcaPRB37z4buw5qR8foxDqsg3pWFZb6WC7tsGeco0wc59iEq6JEJjUX_b9YF7Bdp6zJ_jDO7QkEW17OVQHkFziRjmPrSevre24LvxImVJLW_z0z1vIsfl8slzPWiz16RVq6T863W0ilMbuC1FbzN8COVHpvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WnhpP_C9WGWlYsCtaZhaZvQd6U6eqxGlDDblfv7Txn631vkLnls_j8R0N1sbl0hfN1uZr9UZGX0bdUe5fF8GevU-27GY-1ljFtLQoLEwI0Xi8eau7V6p59azQUyFc0-kFBqe2VFkidbBpCKW5jN2RqFAYZkEag6rTMoFLV59flO5m90HgDGt30Z2pQzPKe-asY-SA0cJgEGjg6NKKWN3iDqeWYCaOs233mBxAO4ObLb0vecL02DMQU-5kzfnJfkWKT_8gRs2EBwM83WiSwQtkHK6IVesOKQs4SXofJkan83jZQdxi2N1c8Rxb_TLDyqkSiKDaxKdq5uESocX908qDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
🇧🇦
ترکیب رسمی قطر و بوسنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/95658" target="_blank">📅 21:07 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
#فوووووری
؛ اخبار شنیده شده از اردوی تیم منتخب ایران خبر از بازداشت مهدی‌طارمی و سعید الهویی در فرودگاه شهر سیاتل آمریکا می‌دهند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95657" target="_blank">📅 20:54 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlmY0DE0YcOxvkDD9m91f_9M5pV6lhS4G-RM_JRaWNvVhP_5MWEUC5yZQmg8QGH_-cElOSYKbwqlGdxo1GDj4MhObnKMDV8-ZGicqFESUkXqNM2NtdTwZGCVZ-V_A1l27gOVnSWSIDSItkJvpB8OXdCZcaCLtmGBUyIx6ghLOfZ4mliwlCYtcI4EwcqII2kyIPfzRfT3fwvoiTjGmhiB7QIwOzXttUD-RYPXypdhTTpqz-IdSW9fEcGIgvxWfMjyYa2DU3GHYXMorVamhf8dNAz0QyU6bV9qnHVa3qi5etrdIsg-IkR2r9Be1oPmb-M4fTYgramq6SEsQ7Iv5BrVeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
رومانو:
اتلتیکو آماده است تا مذاکرات را با هر باشگاه دیگری که آلوارز را به جز بارسلونا می خواهد آسان کند.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95656" target="_blank">📅 20:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRYNpnSLsp3RSJEFmf-6vb8cvsEojp8vPLj3IemW8-lYJynD53kFIO1KehjygoOSl0tR5U58ywAs5lbrLGTab-_Vpp-BwtwKOyVYvkV4OADINvesvWBwLLDT7C_ywPEHMCu4qb8pvw1-26QjDjIeRYLDiYqJoppBu0j7s28y2yFddx8BXZ8T1zIEVBbjIWBG3Hri2AvThTf09LJca3gSLjMGHHzH18Gu044-cpbZctCgb9hmo6_N9RMvIl9w2rUvDd8fVYDgu7iFnluZeQVuF6V2c3FbgVj2qzQYo6l6YucsdSUuKu1Ho6dlfELCX23W1A_i_frnt87QBjQ-fnsd-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔻
رومانو:
🔴
خولیان آلوارز از رفتار باشگاه اتلتیکو مادرید با خود ناراضی است زیرا قبلاً به
مدیران اتلتیکو گفته بود که می‌خواهد جدا شود و آنها از این موضوع کاملا آگاه بودند
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95655" target="_blank">📅 20:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddba5ecea3.mp4?token=XwvYeFRt4l3u2Y3cLQn-FjBCtBuS8UeQ-xP1eNJZX-vb2rCwGa-3YSKszLk96cyZupQsV8dkxKvftIXoE2YsSq_H5PGzaxeLoWmlnXhfBCA6xvUnxGPKfPVOYKIpjJqvacQnncKtevt0PCKST_1a2IqKBgi4d93tfsaRHbeGdb92uj8uO1WTqKRp_MU9yKbVtIaBzwXWfh-Azecc7pKG0ozXoZO1r-7eHhj6Vly_97HBX_6POxLIUwRoGs5it4CLXncGEjxK11MG6s_WxPdRcu7LpNxqlBUrlyW77wIKoKJa5ARQ3LKFqdQalbWFzWJYu96oroAHT4wsINGO_wnM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddba5ecea3.mp4?token=XwvYeFRt4l3u2Y3cLQn-FjBCtBuS8UeQ-xP1eNJZX-vb2rCwGa-3YSKszLk96cyZupQsV8dkxKvftIXoE2YsSq_H5PGzaxeLoWmlnXhfBCA6xvUnxGPKfPVOYKIpjJqvacQnncKtevt0PCKST_1a2IqKBgi4d93tfsaRHbeGdb92uj8uO1WTqKRp_MU9yKbVtIaBzwXWfh-Azecc7pKG0ozXoZO1r-7eHhj6Vly_97HBX_6POxLIUwRoGs5it4CLXncGEjxK11MG6s_WxPdRcu7LpNxqlBUrlyW77wIKoKJa5ARQ3LKFqdQalbWFzWJYu96oroAHT4wsINGO_wnM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95654" target="_blank">📅 20:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdIQtAc5WZnkBBRsLV3Vsu3JftZDFOnC9Qkkxtpz1AFkBkYB_MyfQ3LwzgRLrdvT9VxcxTrrA7jutuVr0GAJHBciBfs3s7v3qzTrA9rem86KuWtcexN90MZ2ABtREvMd5FZ1Er81aM7_Gd5rTjLBfE8mYTM_yBqlXZ4eVhEyppadiFaTCNa2DIivclxvgyJm1PzoLUzM6ufRo_RdZcq7Uk74eJFWMQbeQEdATel2NvglnoP3DF2v-pfJyz7p3Gt605ILeQfOQeVjfoXb6vmGgv_rgrBvNrVvUFJ1xfl9PAVMEwZSliU1o7cKbY-iMp9h-jm4Vb9RhYYZx-e6y5Sp1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رتبه‌بندی بهترین بازیکنان در تاثیر‌گذاری در حمله، پاس گل، خلق موقعیت، شوت خطرناک، دریبل‌های موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/95653" target="_blank">📅 20:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pf1wXLQ1pk7_h2H5tPfrhqFncvoVrB6FQ6im7T3LBXptBbAceZBHfnzeb5dLxr4xd0PhN7jcrSnf14dMFHF25D-CT2XNSWswmb3zCBhgDfUBE6_52X6wdv1ejYMYD9uC8x6VjlCSZxHKeHecp-I15KmYmjESX-bxigj8yiMOV7Z6V08byb8JR6wg593sAuWpFSyP122tykafTS6zOQSXWel1xrZ8E5oDsWM5QKFwQpRAVRnz0Oqj7cHsHByuPemg58sofJKgV8mXRIAOjzf0kJanskMsbBkg1eNeuIxn40MpwZTbgU2WsRUZAzK_g1KRVuL5QJ18PBSd79LG-D55rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد ملی زلاتان و هالند تو تیم ملی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/95652" target="_blank">📅 19:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wjn-6KQRpM2M-ZhahxjjmHYVFzvN3TDUxKd-9yDDwhxoyHbez1MfAtsjuwFg9OYrTKuEUDD-sZhIG2mnbMHmzqcfwjNlmFYl1b177A_WQ9mN_RRzGxl0hDYcSL5vhFgYqOa5pEZUfJudaNfke4j7hHBeq5wFiGZPFcrHeuIWCmo14a8b-aLNjaFTteJvjrLyJpuq6bultUXpd-LA-YkcrIqvkPRzqrl3qUJKFMcMMHr1MnYldSYIZWDMxR5EseJoxxhgbPkHwTVewLJEz45ILLRJBBDYaKV2iPp086m7Yct4f-79PaZYeN-H4Y479FIt12ZD1wsORi0f1qojlyKPkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزی ۹۰ میلیون سود از جام جهانی
⚽️
برای پولدار شدن تو ایران چنل زیر فالو کنید
⭐
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
https://t.me/+9ztzXKxhZkJhZTlk
1 دقیقه لینک برمیدارم
❌
❌
❌
سریع بپیوندید
🖱
سایت های شرطبندی به دنبال ترورش هستن ، به عشق مردم داره میگادشون
💀
https://t.me/+9ztzXKxhZkJhZTlk</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95651" target="_blank">📅 19:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHxD6zWSfMWOIWpVd0lJ_fEMeyO72JT49g8r1OE21D59F2iLSZbIxzWsiLrzZH9KxtkNqd4qVr7U1-MfGb9PkdW5232l8UqvG2XUJ7PvsrQzzU3j7TX4NIGbkr7igZZrbUKWvEU8JYIqq5LkPS4M3U0_W2UY5jSzXSBhCjwuVMiCXctdydWfh1WAEURl4TrL1Ljj_6AT4EWyO_BvqYjCuBOJIgSoKh0F9Xp5TRPg5_rTYZ9SwrAORNlWtnXsq4K_FzKIhQhU73Cy2fU-cIyPf6KQJnqZFzsbXn3VW1dc3CFawrCfoWnqWSIU_AnW4c-ys8HYlIfkYPEseHJl5M17ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام عکسو حاجی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95650" target="_blank">📅 19:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/677deda53b.mp4?token=sKz88O7RjZLd1BZVbUiOvuiV4aWHNImBrzHJsDV6RHp5ypnHkgOzZRHoptHNC_0kRjGbre3VYuDuXhok5E72K9BQcpwqqdq8mjSBhYJjghODveDYB4cinH0BR48pARtHvl8PS6r8vEm75SQnWKmyJzL4giUMXACm5urjg9xernolk_tA9P6lmcobJ_e6sLaTyrjhshW55drCjtTmDB1ES5Mxv3AmlgxWldiobP0MEtD4fbLz1dUaYbQpsPDSlb0VGgjhEidCtu96NEUiUU_yv6OY_NPKzgmmAcBDbCv3AcVEyhkZiuhoby1mvXOjl69Ouj_MAmycV4ll7cxlCP5_Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/677deda53b.mp4?token=sKz88O7RjZLd1BZVbUiOvuiV4aWHNImBrzHJsDV6RHp5ypnHkgOzZRHoptHNC_0kRjGbre3VYuDuXhok5E72K9BQcpwqqdq8mjSBhYJjghODveDYB4cinH0BR48pARtHvl8PS6r8vEm75SQnWKmyJzL4giUMXACm5urjg9xernolk_tA9P6lmcobJ_e6sLaTyrjhshW55drCjtTmDB1ES5Mxv3AmlgxWldiobP0MEtD4fbLz1dUaYbQpsPDSlb0VGgjhEidCtu96NEUiUU_yv6OY_NPKzgmmAcBDbCv3AcVEyhkZiuhoby1mvXOjl69Ouj_MAmycV4ll7cxlCP5_Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">2 روز دیگه این شاهکار رو قراره ببینیم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95649" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KV-hqtynlw93nWhnx7Rk0wNSBAM6grK6U6TdN5FQow3skAbN2KR2G4NHKvpOzz3k4zz7eFzGVf031Q41JN5uUnf0Rvl4L9xv-7tKV47WvwqPpZcR4Srxs_vg46UUHYbKq0FdbgD22bH7wkaYzkQl0aYD9g0NI9WBIXHofMPgi8OkLKR8QsMA1RXav1G8jiMbABzruepwYdfWkrTMf_TA45nYBRjnpa3eUV9UXSX-S31O4Udi4MPxjr7Sdx5siACUN-OgVM-JBAOSUR_LcQZlTATbzbWrv36kKACfPj3aWC6iqugeX22DA4TvnuWChpgymMqR57gjlG1UUe90fAoJxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مورینیو:
من انکار نمیکنم که رئال مادرید را دوست دارم و دلیل بازگشتم هم همین است، اما اصلاً نسبت به بارسلونا احساس منفی ندارم.
🔹
من فقط از بازی مقابل آنها لذت میبرم، زیرا در فوتبال از بازی در برابر بهترین ها لذت میبری.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/95648" target="_blank">📅 19:49 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95647">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IervjgGvz9EJbsoAMjO4-uCtw11mByDrAWD2hROVofb_U1PNXhqgmFyyAoNjpvw0Cb9z0-oYQzVRgq1GIjOwHqYgdBSeaQ5cqwv51tCUDXS8xOg01t_TnyKBFW8TsdyYfoiBPuTQM-yNYZM64x_f6iC3GrP0ln1xNvHIgnoeZJuaj2QPrMfXlRgAmsCzdm8hzxpcZkS3ZCVuil8U5N8ZsjMFrGdqgZ0axwownvSDmqItCZIHo1po2uOt9Qxu_ocnNAbbS2SaLIf38bEWXE6LaoKbTavFFgdrW8qIlgOUZjJIMjHYaBo7ijmoZLQCcHkSlCfVGnkPF8FYySVEPMenLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
فوری از فابریزیو رومانو:
گریمالدو با 20 میلیون یورو به اتلتیکو مادرید؛ HERE WE GO !
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/95647" target="_blank">📅 19:43 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95646">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3GtE6vojM5V1itM_fLMZ7G8dPtbgsvWd7yeMEc5BVb-AgdHGViqUh40NawcrVSzFR-oInUmsMvyGEkro9baK5AXcgADjlj8fqsnNM4VheZkaFaZAzD6LcNLqsBGqTk6WAZ1739xOIyEwX1sjrTjYzJSpip1TbPilNQ6GaWKamO62Wjt-R_F14fCk4QvVZQ0coWDzbgrxxSctZ9Q_sKx6Q1kNTeb5na-bBqHaNKvu5qxAps5ZHX4oD6L-4PYkbLNzO0t4FV7-tv31u8OVOH2DaOx08eaX63zmm2SXMFX3hT_WdSMl48Rr7rojRIOIPUSFxLJKMEPGPigQDEfOkDc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی ۳۸ سالگی‌اش را پشت سر گذاشت و وارد ۳۹ سالگی شد. آمار او در ۳۸ سالگی:
⚽️
50 بازی
⚽️
50 گل
🎯
30 پاس گل  مسی در مجموع روی 80 گل در 50 بازی تأثیر مستقیم داشته است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/95646" target="_blank">📅 19:29 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95645">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vyb95vFPIDFgPI71ZQyCnczkhfQBhHEjigwRkrubEPgxgT-VWjkC_cH3RD6oBJC7ekbsmaoxQMKERWSB4eqqGf7PiV8-vH6QFnunAKMU5jmlhlL8GC6QkVSocP1pGrmBlM-t-BaprK1of_Yuxv-T2kP_Dw5TFuuWbgKA_chZomTvjwVzyseNq_h7dIPiEuSjp_FPXijcU6-TsDErg63xH_7TpyBd5JVtWXCxYV33ZF1eNbvnSoxceiq5WgB7cZUL8u-lhI1rq4tU1t3nUpQMtT6JqbkqORsIHJMNXZlDkoo5x_pnYSQyCCEqHdLyl3C0ci1uPjNymKMoZoL7et2jPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رامون آلوارز:
رئال مادرید انتظار دارد در تابستان امسال تیمی حاضر شود که به وینیسیوس جونیور پیشنهاد بدهد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95645" target="_blank">📅 19:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95644">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfmtbhz3izgR8XKpSjRERXfc1XWsM-WQ9rzuLZI6gGU4SeqCLn_H1LCXclJCzRLzZ4R_-Msf4dUs7cO3fTQFG3f9qbS1NGzSpt-Pe1jsAu9I-18GD3AiLoSbfwr8DrzAaXOSdjdwsZVxP_lYDiWm_AaPK6TEBnACvq0eGlPirCyadetC3fM4vmAWquAEwQkV5ksqEZahyCQuRbnKiryLWEBEXwa7LWWayxriJVtza-HdWUtfXWZA0egTTOHgeeN8lHOH7ESL09bQdeHYx2aXFO2WhcMzSr07Ts2rOGJf4e0PUg_lvQDbzIeIMQtpi9HsFH9Rtr57g8X3fDcPOHeo3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
5 رتبه برتر فیفا پس از پایان هفته دوم جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95644" target="_blank">📅 19:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95643">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3u9b-DkyoI3z8V7ylIFzX6Mg3R41TDEj0u4zHF2twIyzkw1s8paMoZPvGdR8VuFY2cdNdonQ7nURmqtv4a9ek1V-ZYSgzWzjcLudteu-vvQJSUcAYJt-3GPl5wVXQo47EnUfnWksPGp0Vzx8DwyDg7IM1j4Dt4vs4ybUk9NtTxX2J2kazyL7ReNhG9kTq-6hsK0xNnPNf9DLJ1DyxwXRaaeHH4EqlV13IKmIOhOZlx7pmgX_nXlCI7xCkeNifd9n-oo9W6EyMhoCXhVEScZEBe1MlFQ9K_enaIPAS6cCwheWcUlRWHPpHgLYg_BxpTqaxAZZQqBM5BtrfCtSSy0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیونل مسی ۳۸ سالگی‌اش را پشت سر گذاشت و وارد ۳۹ سالگی شد. آمار او در ۳۸ سالگی:
⚽️
50 بازی
⚽️
50 گل
🎯
30 پاس گل
مسی در مجموع روی 80 گل در 50 بازی تأثیر مستقیم داشته است.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/95643" target="_blank">📅 18:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95642">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cOwwKOfBT_uwAEVt5aQZY35cOJsgAmnFfACtQHVGAL97f8XzbkVYvKVMATQbH7ExIIap_4PNjejZvisPqE3C9UluG2YgPazlkxL21i3HQnp4hKVOeHDSpHTTWuACTtbAa6r0-3LIkwJTTfN-GSM0ghanE4Gsr4pAbaWT1FvgwJiSI-MWUh_k8pj-sU0g272T5vbza827ehZbsojniL2OvdEw9n0jnM098RzESzvxhXEoaEybOsSP_qE3hi13np48KeOsWKsSn5DmqIHniw4p2UEu58XSnRgBQ05kNgq_Adxe_oaKeQR5OTOZjXJo3dfaXB0Rj1aTKPp7UiSSQAfhWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نانا کواکو بونسام (جادوگر غنایی)
: من، کواکو بونسام، قدرتمندترین جادوگر جهان هستم. هری کین را شکست دادم. دیشب بازی او را دیدید؟ او حتی توپ را هم ندید. چه برسد به اینکه بخواهد گل بزند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95642" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95641">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/95641" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95641" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95640">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=coKxj7yx4F5qIH-q0TL0qDlEOTyrIi6SqCkZfFVKj92u_LowBXK2NskndOKinWtzP3T0gaSPU8W8U7KaZpIOXJpwAScZANQgbz2rcZ2isX97u6N-RoyxAI_H8XDGGGO67C6RM91l2FA7l4pHUo5lIzAHhQac3LupBPCawg6HQjrhoXMC0XoVYHBpftw-z0Wut3Zuc4r2DGBNh_Qax-AahRePzBbesp6NWI8mMYzabIP_GkxJQ-1H7IbgupnP3CN7ZQ6DeRyaV8Bm4vQpTdkuqIHMZgfT4m-ERbphOL-aFnifUsNjxjPY7xJHtD6jbRYPuY4BtIXXGElqgSVz28tItpiBMGgoPTgMvAvpjDNx78V-2pzBpF0oGnBbIGlo68ZJzuFOVAlhuQEpwpbmGeA9JiyRfYXQnS92iQ41PH9yV-8ZPWKmuh6k5TwYzMDzdfkC37RDOeyPNRlEBc5hg-T6umXrzWHiRomaepRuqMiASbVVuLNUIIUHcgj-3JkzwQl8RdlDr9kD8gIJGVvqeg1--2wGZ9bHzd0MWK18B18CPGGONh08CGnArZkuqjgJY8H-V9HtbOUPy51Za1JUHDWg7tvI4e6RzoC_CiPDOmqu5m5lOnXkhhiJgSHPIOyhr0g0S-Yi4wylSsFLT55tIDj3TkUZZMD5BaPU6G4t7cvHwbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=coKxj7yx4F5qIH-q0TL0qDlEOTyrIi6SqCkZfFVKj92u_LowBXK2NskndOKinWtzP3T0gaSPU8W8U7KaZpIOXJpwAScZANQgbz2rcZ2isX97u6N-RoyxAI_H8XDGGGO67C6RM91l2FA7l4pHUo5lIzAHhQac3LupBPCawg6HQjrhoXMC0XoVYHBpftw-z0Wut3Zuc4r2DGBNh_Qax-AahRePzBbesp6NWI8mMYzabIP_GkxJQ-1H7IbgupnP3CN7ZQ6DeRyaV8Bm4vQpTdkuqIHMZgfT4m-ERbphOL-aFnifUsNjxjPY7xJHtD6jbRYPuY4BtIXXGElqgSVz28tItpiBMGgoPTgMvAvpjDNx78V-2pzBpF0oGnBbIGlo68ZJzuFOVAlhuQEpwpbmGeA9JiyRfYXQnS92iQ41PH9yV-8ZPWKmuh6k5TwYzMDzdfkC37RDOeyPNRlEBc5hg-T6umXrzWHiRomaepRuqMiASbVVuLNUIIUHcgj-3JkzwQl8RdlDr9kD8gIJGVvqeg1--2wGZ9bHzd0MWK18B18CPGGONh08CGnArZkuqjgJY8H-V9HtbOUPy51Za1JUHDWg7tvI4e6RzoC_CiPDOmqu5m5lOnXkhhiJgSHPIOyhr0g0S-Yi4wylSsFLT55tIDj3TkUZZMD5BaPU6G4t7cvHwbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/95640" target="_blank">📅 18:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95639">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SaPji9fvB6bclTkdt32OZfvEdxOCqcCcxxy0GsAXOlC4l5no3Z0rHs094D_u5BEm4ExqjAxM0vRKBL998R034CFWQJg3b4jqrvuTXjV7f8zpvRtEyacYZsjJceogoJ5nyTJ3_DRShX4DT2SR7gF6zi-mZehUEtKPlZfAobZKhaBaNBHUvoXFgU3QF0KwHaz1TcEz1X6zrM-Ocy89t1GxNX3IKtAI5TR2OQJy5-VSqRqi5ZoDx_mrJuEiZ8ghM8Y5hOByCpRmoKaqri50Nq38SUN6Zgsp02rX_lYMYkTNaB1ulZYK8NiX21R7j-P2F0-_Tph01VZQFN85F17mrXK9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🔥
فورییییی از کارلو آنچلوتی: نیمار کاملا بهبود یافته و آمادست تا 90 دقیقه برای برزیل بازی کنه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/95639" target="_blank">📅 18:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95638">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51d71eb644.mp4?token=PRfoRL9IaMW_lebkPnrscVIFyeUk1DTLiUP06lySVKD7ie5uBBK4QtnpRogJJtYD79wTXOD-p9OEPxX1w2J4wNheKmRDutz9UZZGGOuP7s0X_-odf64I3O7NcO00FdlZikhx0S-ZNXbeqOkZTUTKhIpzskJSIqNfaipniWOn0KBECaj9iKDVTZJ6CVE04vmCcfwVhn_zMSlnH7fbmkZag3WT-bEIQ2oHTv_FPldjhOD7qXLYtOpqsLSq30p-RiHEmLqR8QS8vL7jnyVw3LAHoYPc5DeXhwSDt3BMQIM3Fl5lUn80CIU-A4XK1NtN26Ge3jDMGGfIl2ZN-H5ioJnfPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51d71eb644.mp4?token=PRfoRL9IaMW_lebkPnrscVIFyeUk1DTLiUP06lySVKD7ie5uBBK4QtnpRogJJtYD79wTXOD-p9OEPxX1w2J4wNheKmRDutz9UZZGGOuP7s0X_-odf64I3O7NcO00FdlZikhx0S-ZNXbeqOkZTUTKhIpzskJSIqNfaipniWOn0KBECaj9iKDVTZJ6CVE04vmCcfwVhn_zMSlnH7fbmkZag3WT-bEIQ2oHTv_FPldjhOD7qXLYtOpqsLSq30p-RiHEmLqR8QS8vL7jnyVw3LAHoYPc5DeXhwSDt3BMQIM3Fl5lUn80CIU-A4XK1NtN26Ge3jDMGGfIl2ZN-H5ioJnfPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
⚠️
حالا این‌وسط بانکا چرا قطعه؟
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/95638" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95637">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/028dc79cec.mp4?token=gCfhYKlxI30-c_hvPQnMyen1Ww3JCSjDqu_LpkIoARpQP1a_0ZCAhCsWRVSdbMwceddyrFoCXYVIpPretwsvTCwydnMf7sjlzYEiHQtYc4yQK5s_832XUWa_79KM3vG9Ljts4V4CUafO4NsYmZT92n-7d1tNWy-gU1bqIKpwTr7ipiC87ii1NINtV2t4Z8A0omaI1pBWx7WBl026EXLx5rsvlxFIwF8Biuhh6QTbIW7U58HElPh_iI5s4BiC3d5WaW0_mx7nTCpNITHz5n9uScLEu1ctnjwtbHulgv4SlS2_jt8Y-xwIe1Vvir8q8fxDKBriY_a6bd1HChuERHXeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/028dc79cec.mp4?token=gCfhYKlxI30-c_hvPQnMyen1Ww3JCSjDqu_LpkIoARpQP1a_0ZCAhCsWRVSdbMwceddyrFoCXYVIpPretwsvTCwydnMf7sjlzYEiHQtYc4yQK5s_832XUWa_79KM3vG9Ljts4V4CUafO4NsYmZT92n-7d1tNWy-gU1bqIKpwTr7ipiC87ii1NINtV2t4Z8A0omaI1pBWx7WBl026EXLx5rsvlxFIwF8Biuhh6QTbIW7U58HElPh_iI5s4BiC3d5WaW0_mx7nTCpNITHz5n9uScLEu1ctnjwtbHulgv4SlS2_jt8Y-xwIe1Vvir8q8fxDKBriY_a6bd1HChuERHXeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هوادار انگلیسی تو بازی دیشب پشماش ریخته از حرکت مردم غنا و فکر میکنه دلیل نبردنشون سحر و جادو بوده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/95637" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95636">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cXPy352SyxT67lJDeX4QpVlf0NxY5adY9WSrHjFQHFKVARNt2qv0y5o-LGMq0kOC3g-Zhs-9iEiIhJ0aGk9qtpJC9S-y06UBdp891ZrmQgOejW_ctpwmnx4CfYr5hZ_6uxsJaghd50tjnaoXujkFnHawScOE-5A9QB1FZ0Tvnle3qrXEFypydAHkCmChUCyIlqTYdTcqLgbmkNcrcneAPxGE8HNkKQhREp4C4kUeUYGc9rpXgVrR4wnNTnKoXH3gWmesocDLcI-4TK84lX2PKQ2lWIEOUxrRoEp-TK2NJ4HziSD2SQqpjy0g99_ap1ukWZuL7Lr5ne5WxHNjObmOOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🔵
متئو مورتو:
🔺
پیشنهاد جدید بارسلونا به اتلتیکو برای خولیان آلوارز با پاداش به ۱۳۰-۱۴۰ میلیون یورو خواهد رسید؛ قراره مذاکرات بین بارسلونا و اتلتیکو مادرید تو این چند روز از سر گرفته بشه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95636" target="_blank">📅 17:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95635">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1224d3d31b.mp4?token=KruNV0Ke_h8CvJsCXmkd28ii3DuZYAq94JlvDDs_mZJ1KaIQYQRHE8jfgCQjCIw0ePx93tfQM1D4oAv0QBXCROV5BRMCQoMIEG-WgG9IFwazlK0MEE71wkdSEibDGcc18Ey0rXeNm_px9Bo4AxnA9uUI2XuLEKSqdi9VRKHs9jbQtBsxhYr3gxBaigQUS_4NIMg5f3hRL7kYiUkIe_cqZ17uLi3CTFfDbMSamqjrx-tgjkN1UnJ1kJumKmyA_-GuGrc8gElYd9BSUV6X82vVN_8KIa1mWPY-Qo5iPwF_dOYXbyFQJvS2kVItq4ferIVOARbrf8uaPgP-9T6qQj1AJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1224d3d31b.mp4?token=KruNV0Ke_h8CvJsCXmkd28ii3DuZYAq94JlvDDs_mZJ1KaIQYQRHE8jfgCQjCIw0ePx93tfQM1D4oAv0QBXCROV5BRMCQoMIEG-WgG9IFwazlK0MEE71wkdSEibDGcc18Ey0rXeNm_px9Bo4AxnA9uUI2XuLEKSqdi9VRKHs9jbQtBsxhYr3gxBaigQUS_4NIMg5f3hRL7kYiUkIe_cqZ17uLi3CTFfDbMSamqjrx-tgjkN1UnJ1kJumKmyA_-GuGrc8gElYd9BSUV6X82vVN_8KIa1mWPY-Qo5iPwF_dOYXbyFQJvS2kVItq4ferIVOARbrf8uaPgP-9T6qQj1AJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
لیونل‌مسی در اولین روز ۳۹ سالگی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95635" target="_blank">📅 17:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95634">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
‼️
هوادار خانم منتخب ایران با پرچم جمهوری‌ اسلامی خطاب به کسایی که پرچم شیر و خورشید دارن: همگی بیاید برید تو کونم
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95634" target="_blank">📅 17:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95633">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYoByDCWKdEcIn_uEsQQ34w6l5GGxqwPZQtLN4qG8ugayuo1ncLWtb2gO_l_Gs_04F_9S25ZQSXewFNog07Gxw9GzEnPt_RZoMEnJtp3SRcsKU_4RkAAKwq86NCvlpvQd4qaD8hhV1UFj41Un9gI2r1Ary49jnZufvgYFAnVNFF0UJU-_dlOSefkU9uTXK4MvL856U9YY0iGpQ9ZYyBoHB24BxuU-Mjs5CXkG5WG3jcrnqDzbWAPfGYjz0_-CULvCMRa9fLcM46PoXXc9gMbQKRFmg8R4Lio76a294_ILNG4GmD7yMH0xzSTCUtGoJVYF_psv2rF9sCxpWpJ2BZ5kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
علیرضا فغانی به عنوان داور دیدار پرتغال و کلمبیا انتخاب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95633" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95632">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b14e7b150.mp4?token=dy132QBnIfrBQEflAGRMUnOLh10Hz_NuJGZFveICfeAXReE5enMgZwUekcZdWQ1d_mplIEfP7jSudOnwneXubrFOc0yS0zA-KGKj4CLHwI_UjU9nrJaLBdW743-NjvV5xycbOvJY1j47eGf5TEf71oVN1fb2G_KyZ1sAuyWmHfv4qHA98o2At4gY2EsQnBFrQ7q3SmNhqY4qwxsKEbCCZzvQ0nMEE4eSvX495L1Mn26u5g9hdOy1v6SpTUQyET6mrS3lLV504vcTZCRqaDMw4rLKIuTDkKXAuT5trCjxB7xK7rOuIvTT1T1ZMCnF5twe3iabwF4yce_GlaxrEqBltg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b14e7b150.mp4?token=dy132QBnIfrBQEflAGRMUnOLh10Hz_NuJGZFveICfeAXReE5enMgZwUekcZdWQ1d_mplIEfP7jSudOnwneXubrFOc0yS0zA-KGKj4CLHwI_UjU9nrJaLBdW743-NjvV5xycbOvJY1j47eGf5TEf71oVN1fb2G_KyZ1sAuyWmHfv4qHA98o2At4gY2EsQnBFrQ7q3SmNhqY4qwxsKEbCCZzvQ0nMEE4eSvX495L1Mn26u5g9hdOy1v6SpTUQyET6mrS3lLV504vcTZCRqaDMw4rLKIuTDkKXAuT5trCjxB7xK7rOuIvTT1T1ZMCnF5twe3iabwF4yce_GlaxrEqBltg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
💥
پای شخصیت‌های وایکینگ‌ها هم به جام‌جهانی باز شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/95632" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95631">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
ترامپ: بازرسان آمریکایی برای بازرسی سایت های هسته ای ایران به آژانس بین المللی انرژی اتمی می پیوندند‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95631" target="_blank">📅 16:09 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95630">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c083e67433.mp4?token=S-lXnlpNFl78pswweDggcx6NvWtitq_YtzWuktF_wsaRgqyyg-jmLqXdQky3msnpwn4Ib0j2DRSI1D9PzpO_W5rh-uAYFix1IIssqUybz9FcHSYFcqOsQRCNfCHaHs5vpbfY9c19sDyI7xW9oUSf-uZjBNHYF9Um3vzHs1pqmdVoxuYkt7OO3HzUGYym3s44BdauaNAkvnKLxuKbC3YkBKlW6PAlU-22FqcUXE5D20kd4UwFlMhwQL88yp-a3CSjZUxN5IqND9k5yMSC4EYz4XBsL_u1fueHC5ZFbf8TY11MxW887xpG2fNynqvcfm0CVfLNGLGyOj_NLQ-KXOrd0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c083e67433.mp4?token=S-lXnlpNFl78pswweDggcx6NvWtitq_YtzWuktF_wsaRgqyyg-jmLqXdQky3msnpwn4Ib0j2DRSI1D9PzpO_W5rh-uAYFix1IIssqUybz9FcHSYFcqOsQRCNfCHaHs5vpbfY9c19sDyI7xW9oUSf-uZjBNHYF9Um3vzHs1pqmdVoxuYkt7OO3HzUGYym3s44BdauaNAkvnKLxuKbC3YkBKlW6PAlU-22FqcUXE5D20kd4UwFlMhwQL88yp-a3CSjZUxN5IqND9k5yMSC4EYz4XBsL_u1fueHC5ZFbf8TY11MxW887xpG2fNynqvcfm0CVfLNGLGyOj_NLQ-KXOrd0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
این ویدیو خداستتتت. خداداد عزیزی مغزش از کسشرای خیابانی هنگ کرده
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/95630" target="_blank">📅 16:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95629">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UvwkO3Zkx5nnM6oubKZ3BjYReoTZQ06owH8nRjRIpDWAuUje94aDjCq2ALIIbUWeb8Db4hMRJ0ApV20CqKiIYTTKEfhg20z7K03Rkvu4WE7lzQoPRD5wqGAUWDSyQCq_PNWEwpmT2X2fTJKmW0CxcaLgMD1wF8jCue1bc8nKpzDYfRC0oIFPLo7rSSYVAq6sy_v67fMg6Lm1VYA5m6WrY3YWAYo13FSYoEVAxst9AoOeF-5h_iXJ6lz3tXs_boq45zzXGHPfqtpFN_6IukXN7mkba5rIiT-rWOYCujx6aBf-ohWRmX8YsL5SN-QyoQW2tYnwSs22t6Oc9GgfDNIPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یان دیومندی بازیکن ساحل عاج در جام جهانی 2026 ، 16 دریبل ثبت کرد که بیش از هر بازیکن دیگری در دو هفته اول بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/95629" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95628">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa4e18637e.mp4?token=Ta-6TwD0Z3XFA5F2oryQK4-fF_KraXRwUtnjHXoN8PcP-X2Y7Kxm0ML-wVB3rIYgpfL36cZpjeMJK3CzuNNFr7i8A1of_hzthZCNDbuA6W7u55-BP67kfYo9ka9s4G7uEsKMrQTPb7-62oSSN9bEsQ_ye3oaOTrL0rAHvRavHvWCo20jmVmMwxtZpMiCiIXRTUVjjtcSmaiwJVD_VYc8ScDElrWdnzGgcVwS7OGKx0tvm_Q4Bo_ff_VEHJ06Rr5-ED3hT7EKbNkRJT_6uWDnKjZmyVoidb4KrCfU9CS-r9yxYOLM79x0FcThcV9DCWmXmYTltBdvrr3Hm-AwBikPRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa4e18637e.mp4?token=Ta-6TwD0Z3XFA5F2oryQK4-fF_KraXRwUtnjHXoN8PcP-X2Y7Kxm0ML-wVB3rIYgpfL36cZpjeMJK3CzuNNFr7i8A1of_hzthZCNDbuA6W7u55-BP67kfYo9ka9s4G7uEsKMrQTPb7-62oSSN9bEsQ_ye3oaOTrL0rAHvRavHvWCo20jmVmMwxtZpMiCiIXRTUVjjtcSmaiwJVD_VYc8ScDElrWdnzGgcVwS7OGKx0tvm_Q4Bo_ff_VEHJ06Rr5-ED3hT7EKbNkRJT_6uWDnKjZmyVoidb4KrCfU9CS-r9yxYOLM79x0FcThcV9DCWmXmYTltBdvrr3Hm-AwBikPRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
جالبترین شادی‌معروف نروژی‌ها تا امروز
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95628" target="_blank">📅 15:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95627">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnEaAO2HsEuLgOWAFlZm7TVWVsn6y5CI8KxV0EUdj9ktWlQdJoIeV0FNzZAVjPU3P82D4ih2oD1QOTnnd2ak7pm4rlp1cwHyfrVGNVehQRIp8Q-73uxPMvmagggdgdC8-16yZYRkFrySuFuO-OBPM2cIwUYNk_NAd7CIbnmSXQek3YEJnL7HUx46f-n1e84uF799jh3yAKtu1-8NdKdQyvgJfTUak-cdWkMXSTkj4b916xYfnbhEWV2p_0r51kREJ1VbXcH35WXTzxMTnYuqPE23DRpL8hClCcJUKPvMfIZpCx3d1bETT08VEU0x27C3ycct02mVJvSuAuW31p635A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
بیشترین تعداد شوت در چارچوب در این جام جهانی توسط این بازیکنا انجام شده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95627" target="_blank">📅 15:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95626">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23666a9bc9.mp4?token=MwZwA2vjEAxxRW1I4Fv06J2cPz18_raYuIIM69M9M9jkMHO6TLVQnnjzZ0Py4WhErpsNpxRcq06NAD3H8kanmFrnzOiNPeoccPyBzW6knTkgSQGJ9uqwQ35uXK6WC2fJ-7ENd_qOWkUTqa8bTlwOy8nvi9Y7-2E-ba5Nsf0IQVmcBxKEcgzS2Qd2el9Yy5Y-RemI-an207hp6qJwQ1zwUqKOEh9I3vea6Pyh9dBBuAvu-d0LQihckuV4r2IN9_ck4L0ncstAGAQ1Cxq0K7p2U-TrjAw2NkpJ-RHfd4XEAjrUFXVfHKZdB4DVpVG7QY3-3-zXn7Slm9l_vlf4NJa1vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23666a9bc9.mp4?token=MwZwA2vjEAxxRW1I4Fv06J2cPz18_raYuIIM69M9M9jkMHO6TLVQnnjzZ0Py4WhErpsNpxRcq06NAD3H8kanmFrnzOiNPeoccPyBzW6knTkgSQGJ9uqwQ35uXK6WC2fJ-7ENd_qOWkUTqa8bTlwOy8nvi9Y7-2E-ba5Nsf0IQVmcBxKEcgzS2Qd2el9Yy5Y-RemI-an207hp6qJwQ1zwUqKOEh9I3vea6Pyh9dBBuAvu-d0LQihckuV4r2IN9_ck4L0ncstAGAQ1Cxq0K7p2U-TrjAw2NkpJ-RHfd4XEAjrUFXVfHKZdB4DVpVG7QY3-3-zXn7Slm9l_vlf4NJa1vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😛
آرژانتینی‌ جماعت وقتی میخواد فوتبال ببینه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95626" target="_blank">📅 15:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95623">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cbxKDvdjefgjz5Pr8N3Od-9dgvGPIEtfLCwjwJUn5t5mMs3wnMi-Yf7Hl2VcKQv3tD-FLFY8e97Ik4M1S4hnQb7mSIqY2bOxYy_ODy3-x_IQlC9nTSjxRrzbOtok-4PAtGZ6-dIeI-1B27LIOSXrBLOKOFhxVTNYsSaChzAKa-aCP_maakmCorPSwMZbuYKYdS9Q4yAz3EJLfDzPJUNYdMmMXeSvee6j0PAgOEduNBqZJPx0CaVBDi5Hg6U-xoycoau4FshG3WKpBePK5Xwoz3q4-SYpQM9LxznQrV4HhsimzX7S_vY9RvXCDYnAiHi96CyCpq8c8dSLoMpIJDCmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rmj3s_czz7Wud4uJqIdVMEGPXPqBVxcbiezd3tU5d2IcMr8xfAbrvdouu-Qc0dTXCklVz6y8inppctcdRKPJeRlO0V25Qj-rsbiOOTocs8TJPS7Z-PWwXpU229djcuxVj8q0cE3uw7ITusE345_jPnlx9CrG8YneJvWl9huey8rmBee4QhkctZz5VztnmqOVg5YAJ3lY9lkVL1o0eNAPsUNDRROz_W8GuqiFE8T1xhTqVQIK5qWZnW4hLU5LJM8oV_R8VNzkndSHrQmINajklw_IWDwYT66hsnwoZJpdIpRn6oV798bGwrquhTK6bVV42iTSMA1KtZ9q82q7fbZs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBHYWjCy1S9IgMY3ynm5v6eh41rKJ335W4UCV3uR87a7dj6wJuiyOl5bwIZl61hIGcE1EuZGX7Mj2fHBHT6fM9CTC6sBRCpjT6m6xYGnvXDhwoKiqKKs3J0o7j7rWll1d_kWePPZy3uhQVM41RfnFOCrQ-jq4V99Tg8S5Yw_nVfpN_93qieC1ZcnAQOxsSa_5cH9cxat_U0t5OTTRFRmJZbZPYpF3hVRZLClXvKjPYlvsd5T7TL_mtUwIL3a99uQZv1gsR59z-powVKkLdMqcswAM2OqRK3thBsWNeAJhzHld1obfiZyJST4H6Ec-pG2fkn5fs9CFW7RzoAfLxThnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇮🇹
12 سال از این ابر شاهکار سوارز گذشت
😆
🔺
فیفا بعد بازی سوارز رو که دو بار دیگم سابقه گاز گرفتن داشت رو 4 ماه از فعالیت‌های فوتبالی محروم کرد.
🎙
مصاحبه کیه‌لینی تو سال 2020: من شیطنتش رو تحسین میکنم. نیازی نیست از من عذرخواهی کند چون من هم داخل زمین فوتبال یک پسر پفیوزم و بهش افتخار میکنم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95623" target="_blank">📅 15:19 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95622">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30a14dc199.mp4?token=etZ-y2msNAh7IV0PwG09FGLVL8_LNqqzKpZos7YX3go41IgKSYOe9OSPsIWv8huygI00ZwCC3bZcYXqauT-pAz4t5m4f-BtatGNm_Bc4hLtOrskqQ9gu6cKWXtqruSMTqvV9NrnMrznsG-_nh3eVXZ3PGdVDEQWhVIKu-nG9Lcv64c-N0MStVQdOWWYyONfAnDrIDDjPZulJd1ZaGzRXagbkWZ9ULLG08ZOwS6xhzd9GuTUr8o1FUl8Ys37viSzNg31MqSxssNB6sDrw2LQgVHqNekAbcniyeXjD8Je8zt3j3d5Rfx63zmokbTcCBSAVnl4id4_tsXGo153v-bWHOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30a14dc199.mp4?token=etZ-y2msNAh7IV0PwG09FGLVL8_LNqqzKpZos7YX3go41IgKSYOe9OSPsIWv8huygI00ZwCC3bZcYXqauT-pAz4t5m4f-BtatGNm_Bc4hLtOrskqQ9gu6cKWXtqruSMTqvV9NrnMrznsG-_nh3eVXZ3PGdVDEQWhVIKu-nG9Lcv64c-N0MStVQdOWWYyONfAnDrIDDjPZulJd1ZaGzRXagbkWZ9ULLG08ZOwS6xhzd9GuTUr8o1FUl8Ys37viSzNg31MqSxssNB6sDrw2LQgVHqNekAbcniyeXjD8Je8zt3j3d5Rfx63zmokbTcCBSAVnl4id4_tsXGo153v-bWHOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
دیشب صداوسیما این نماهنگ رو برای تیم ملی پخش کرده و اینقدر شاهکار بوده که از آرشیو شبکه سه حذفش کردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/95622" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95621">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZbHprvJj319ehSU5kIxDPcMGzjTmPbheFmiAk0qjVpuh-R1CmgtR-WwAlHSNHTwp7QrG9z1kKA8jjnkWhIOKTGBTFyidz0vQJ2lhW8GjS8Rrje7SPadEX9ts4r_9dCrbS1p6OcDYvYZvd6jMqzDwc46VX7hcq0mnWdGbmrmlSMoG7PD5IynacldwLnNOXOJd_MlHN97McHSpWpr60QbU7pQFZorHwOaRu6zZP4tC7zp1yKsPI7WtfzzBUmtU_68Upfry85TKQEV6BISMb7nxmlfTZl4gUvZQFTo39c36uMGDVFj30VS8cdef8PP8sqKDw3syJIGyhUN5DvM9iqSFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
بانوی‌ایرانی حاضر در استادیوم لس‌آنجلس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95621" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95620">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mxHwVwU_fCOzsZjgcfyVl12bVyi8mWL87ZADdsGuVsMAxoIoKsr0hxefeY3eOR4yUHAEu8z3prwd3vMG-fv0GSyp_smPHChAq9_Ry5r3vgZzZaT5bAht7j2QwFb9BmitJNIkbTB53pRcfSboU5OvCJazs0w-o7nKmeFTdxprtsl1TpQkJ-I40pD0pPesp4dVdbwpLyw3e-pZ03ImTGlq4-Gd0y73nz6JNuJb_6G3QwOVYvIZAu5sjIittGyOiMZ-V2QVhs8pduWtu30ENoRVV0Iy_kt1PSRFiTqbPco5mh7vfo0aWclTKiIFMn0qoSH6VnlRKXuHJ_ikVIdGQQYFgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99e258c37c.mp4?token=mxHwVwU_fCOzsZjgcfyVl12bVyi8mWL87ZADdsGuVsMAxoIoKsr0hxefeY3eOR4yUHAEu8z3prwd3vMG-fv0GSyp_smPHChAq9_Ry5r3vgZzZaT5bAht7j2QwFb9BmitJNIkbTB53pRcfSboU5OvCJazs0w-o7nKmeFTdxprtsl1TpQkJ-I40pD0pPesp4dVdbwpLyw3e-pZ03ImTGlq4-Gd0y73nz6JNuJb_6G3QwOVYvIZAu5sjIittGyOiMZ-V2QVhs8pduWtu30ENoRVV0Iy_kt1PSRFiTqbPco5mh7vfo0aWclTKiIFMn0qoSH6VnlRKXuHJ_ikVIdGQQYFgTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: ایرانی‌ها در خارج از کشور خیلی به ما لطف داشتند و جوری ما را تشویق کردند که شاید بشود گفت جو استادیوم لس‌آنجلس از ورزشگاه آزادی هم بهتر بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95620" target="_blank">📅 15:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95618">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFK9x0DqICrpQOZtJ1c4hyssjnuF0GUjFN71nx_CRYbPZjnvLO2u5AO2-Nc4hNnUX38hXzRBCPzhaUtMWZX0juQKya2ZIeXDtej2jrsejtt338i1gyCGc_xUt05KiyXqke_AASyfHCRFCbtw74uBJWAcwkjNmMOoMllJlzSKF8PP1viQJ1re6qUysndFhP3Y0fpLqAVduG6Huff7IL_XeqLgAOgNz87zSAhW58d5vHYvIfhOSQ8WWddl9On86u-TmmwDzmxFHzbKbGCDnfSiK7_Yogxi2zKRJTgN41svkQzHrwbT8aCirzsWtM4k0BCvyHi8KAOaB-C5fkI46eMTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◀️
تیم منتخب هفته دوم مرحله گروهی جام جهانی از نگاه هواسکورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/95618" target="_blank">📅 15:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95617">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a274e0a122.mp4?token=sr67tATcCCIaa67LopO2jijFNr-dT7DrG1_C1ml5DzQFf9cH7Nm-nXrAbMuOZi1JswX6po1vJsOUjMh7wijKhxNTmDAUSzcOEYPCbLwsNNaIwP8dzXyslvrpeJGgoERdfNwtxWLzaUqz0WFf_paWlmHA7bu_cYKe2Bk8J6jjK3o-Zpj_rxODFzAEhjcm5FlU3GhciW76eYX46uEqqVD9bkLxZXi7dEG06QSq0qhnnedYqOXDP2kV-cIyRxAfLfJT2MWOPj7WgBzWlnWHlnAjOghEasIjkKVgRGNGTFqdPWkBvU0PXR2A0gcU0A-eIgn_U3tBi-cbmQaxqiojbCSx7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a274e0a122.mp4?token=sr67tATcCCIaa67LopO2jijFNr-dT7DrG1_C1ml5DzQFf9cH7Nm-nXrAbMuOZi1JswX6po1vJsOUjMh7wijKhxNTmDAUSzcOEYPCbLwsNNaIwP8dzXyslvrpeJGgoERdfNwtxWLzaUqz0WFf_paWlmHA7bu_cYKe2Bk8J6jjK3o-Zpj_rxODFzAEhjcm5FlU3GhciW76eYX46uEqqVD9bkLxZXi7dEG06QSq0qhnnedYqOXDP2kV-cIyRxAfLfJT2MWOPj7WgBzWlnWHlnAjOghEasIjkKVgRGNGTFqdPWkBvU0PXR2A0gcU0A-eIgn_U3tBi-cbmQaxqiojbCSx7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
‼️
خداداد: من خودم چک‌زن هستم ولی میترسم عابدزاده به من چک بزند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95617" target="_blank">📅 14:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95616">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9BbG04fCcPs7xwqeExwLtipz8aoQK5VKCzAcCKwb1ZlYCGJZgPFvXAsumST-Wyou6Bw0BFnFxCgRVJMdU4oWtuYlcliEavBvdy0K3mJB3NOmBIaDLjBUJn8_NmOf3spShvHWGiuhwoAne0cBCCsa9bTJLO9gVozp8Nx9ArQlDempZokPdOJtHsJWMIBUUnrkfhREVaEeVhH_NOzx-PkAqC4fldRzqw8_IVF1zOjBqxAJ1oeYUVli4EjivuYUU3xnsXNt9lyH9vXBzSliVXTIGBgvaUq2VgLy5jZ3V_LT08LC3mHhGK4_wenrPTu-JbZ4ZrG2sHGtMiElrZ_Y7ncOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
خبر پیشنهاد الهلال به دمبله صحت نداره و تیم عربستانی خواستار رافینیا شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/95616" target="_blank">📅 14:33 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95615">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3892238805.mp4?token=OLnKS0phTNxg-1AdAB-TuY0BvoIUD193tZ0oBhwcKnJOLMF5dnovc3L2dxsG6AcC6T1EYm3WlfA9ouQisxNVIjLdrfywEN_f2d2pBPOK_7FwiR21iL2u_Z3ebk8XkqlHjpVBPG_04SzACjp40S5g9iDtFd821DUO7DLe8LXCRrF1MEnqCEkuq0HLu3TsQfYSmCXS8b1WJYTDayHMUF8NoxZGmuNkMc5R0R022Y09hLNwa6865PVbUrcsBgLgSgt-exk-hJdxGNSGsBVSnhFUb0XeJcr2Dh4hWfb72eiQlZfGZA5rZ_1t14O0Eprcygw7yjaTQ51AO5z4HCMDXe1kHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3892238805.mp4?token=OLnKS0phTNxg-1AdAB-TuY0BvoIUD193tZ0oBhwcKnJOLMF5dnovc3L2dxsG6AcC6T1EYm3WlfA9ouQisxNVIjLdrfywEN_f2d2pBPOK_7FwiR21iL2u_Z3ebk8XkqlHjpVBPG_04SzACjp40S5g9iDtFd821DUO7DLe8LXCRrF1MEnqCEkuq0HLu3TsQfYSmCXS8b1WJYTDayHMUF8NoxZGmuNkMc5R0R022Y09hLNwa6865PVbUrcsBgLgSgt-exk-hJdxGNSGsBVSnhFUb0XeJcr2Dh4hWfb72eiQlZfGZA5rZ_1t14O0Eprcygw7yjaTQ51AO5z4HCMDXe1kHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم بنگلادش که بدبخت تر از ما ایرانیا هستن، این روزا تمام فکر و ذکرشون شده مسی
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/95615" target="_blank">📅 14:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95614">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRNDH8IpUKf6Og99R9SeLlUyY9tNXH5urBg1wgahTbXPvb-1mhCo1309mQ571_vywvNRvFoEfrewgU7Gg4CGd35jdZ2U-PZCfIrNl_JY33TluW1fZYNv7BZoLm8LDn8rckBkdd-4ELdp5EQLpOoP5QAJk0zVRVV3I-QdvlXjnMI4X9nThyE3hXl-E7yMvLAq7O_UMp-wtESQ9-5ojs-j0iLvXMH8q5ekXEnXrmKsIURZgJdM7PHz9lRzTWLypnfwmZL0k09L_pgIjMxhRsq0ihLfkzieBXWWaoPkmYGQV_UPaYlW-GW3-6cftalg1kCCpJfs8B39ywx4Kz6ZYsmNjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💋
📊
لیونل مسی پس از پایان هفته دوم بیشترین شوت در چارچوب رو در جام جهانی ثبت کرده ؛ ۸ شوت که ۵ تاش گل شده
‼️
🥶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/95614" target="_blank">📅 14:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95613">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8e892beb9.mp4?token=pKcL8XhfYZYrpqetMWjbnTvXMT1gkGz006CPzOX5dMZ3CTahNDlrpsnJ4dC1nH8PzXnow4Y08rWkF2LXWl0zCRGpJKLsUrgIlHwp7cl8j1Csf8Dfn9u_9r7vnAcoe311Cyi2wp1_HG064QpihHlHMOBoYh0GwuMfYM82ROdAq3JcR2iWQRDhBGQ680hORJD77jNnZp2u_B4ZMPxsrMgwo6p0UJDAcVREOkt5Ep6CbkrpBgMma8faBZObJYu75oLiobByZV_PHhsPEeEj3xg3rUSztOV-IZ130yyPX1FrGKPvJ2T5TufC1gW8Fa8DIV5OOf8UrTxZV7PgaIUQjcYGZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8e892beb9.mp4?token=pKcL8XhfYZYrpqetMWjbnTvXMT1gkGz006CPzOX5dMZ3CTahNDlrpsnJ4dC1nH8PzXnow4Y08rWkF2LXWl0zCRGpJKLsUrgIlHwp7cl8j1Csf8Dfn9u_9r7vnAcoe311Cyi2wp1_HG064QpihHlHMOBoYh0GwuMfYM82ROdAq3JcR2iWQRDhBGQ680hORJD77jNnZp2u_B4ZMPxsrMgwo6p0UJDAcVREOkt5Ep6CbkrpBgMma8faBZObJYu75oLiobByZV_PHhsPEeEj3xg3rUSztOV-IZ130yyPX1FrGKPvJ2T5TufC1gW8Fa8DIV5OOf8UrTxZV7PgaIUQjcYGZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شادی عجیب هوادار آرژانتین بعد گلزنی مسی
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95613" target="_blank">📅 14:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95612">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/013e39db64.mp4?token=PWHUJTOpjSrlT_pXSu85jI1XBT1OkFNfhleB9_NUWmVJxABLW0gh-2vxdFKYblkQuwRmIC1LBABTNJuCkQ26fd4GyzJdheJfE8uXYnbAHNqPBV_XGfE5aWJG94OX7IjeYw-kDCpNHKs0Ju1uF5rt3vE4JNPIxM325-f6WxLRc8okNzss89v3-rQKqmald2dB1GspyC99RrrK5XxzH0fI3-MCDOt_6QnSGUiPQmCn_Yv95K0qvUG-ts5H8QVWcqQ0ybkXobw8WwNET8xA02qKJwBJIsCJU4oLIzqSKp51nCs7qlPpzQcwT4dpjK06Wjk3MF_eh2TukDCcD_3IRbn54Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/013e39db64.mp4?token=PWHUJTOpjSrlT_pXSu85jI1XBT1OkFNfhleB9_NUWmVJxABLW0gh-2vxdFKYblkQuwRmIC1LBABTNJuCkQ26fd4GyzJdheJfE8uXYnbAHNqPBV_XGfE5aWJG94OX7IjeYw-kDCpNHKs0Ju1uF5rt3vE4JNPIxM325-f6WxLRc8okNzss89v3-rQKqmald2dB1GspyC99RrrK5XxzH0fI3-MCDOt_6QnSGUiPQmCn_Yv95K0qvUG-ts5H8QVWcqQ0ybkXobw8WwNET8xA02qKJwBJIsCJU4oLIzqSKp51nCs7qlPpzQcwT4dpjK06Wjk3MF_eh2TukDCcD_3IRbn54Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بلاگرهای کف‌خیابونای جام‌جهانی رو می‌بینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/95612" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gef3VwsZJyjTRS8LmsNrvtHDFgmbJsNo8UZtVJzYd990I-VR4FJhm0hO-D0QPZdgxVhgzangtmssRIn_RoNMeCqD7gng_2VzbSqDpP7aI0YQATZsnzbi5u-ElkrG-Ccp_njTjEZKpmxduODKSvOGSSW3i08hhU7zgjvQwxqWKTDyRNPjZI6H06H8B5iHln6fEMf6GDO986qWvNEKn4ZKXyKgKx-DyvRDVIHismG3Wqv_7rKzCUqrthhaYHIpqh1Hucwe-R1IpCjQeooZGse7lsf5C2EUNXBxKCsyejhxCn9CBg23u3ZiDOepMa_7dyugjMZ-uteOghcP1qMTdJiJBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
آیا میخوای چند سال دیگر به بازی ادامه بدی؟
🎙
لیونل مسی: "بله، بله... مدتی ادامه خواهم داد، تا زمانی که بتوانم کمک کنم، احساس وضعیت بدنی خوبی داشته باشم و به هم‌تیمی‌هایم کمک کنم... به بازی ادامه خواهم داد."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/95611" target="_blank">📅 13:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95610">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbB5t5bvUxUtZPzzU-BuqyOh_H3e5GtYmwZWr9mhFfSsIDa5NYDYPBOiboqm8PUUYfHTNnc7dsMJXHQhqVV5IHGDSqiYeUhUBL5arwa2y9P1GR-18VN2xpAIMrTFbTOQx7rGeSYwQ5p0DQaxRCufpnZl6UPHneMoEEEG6D0ZbflOTox-gUSE1rY77CZySLdOobQrgfF5Je6bupgXc-dN0HMnYl15M-tL2aa6Sj0pcMoD-Pv_V4QJqg7ypu0UxVM_yu0j34OaWXd_YUKXDJV9gq71AoHvB9r_RB_4cSJPM6exKYZTFPCwrUvTsaBJFh_Vkiv9Zxb9pFVm1E-wL8ecYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
ماریو کورتیگانا:
مورینیو دوست دارد باشگاه رئال یک مهاجم نوک کلاسیک شبیه خوسلو جذب کند، اما این موضوع فعلا اولویت اصلی نیست و برای عملی شدنش، حداقل یک بازیکن باید از تیم جدا شود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/95610" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95609">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgivY98dYHu1aP4qO9WvICXDPSXjV3I-8J0bEYWD2QXqmtCe7u2ilpFgDtpfo4uunS7Ritz-JeRA1i1aFbcyPhki7HWgHMKLyG4lcOtoiJS_fCjONKxF-mAHbvf8owXRwpG0cMkQgjm4HwF0hFmwCSvDBF6DFGS9IcA0MX3LZhDn8QKNDUUSvAhNysaSForwzNb_DCDdek_eVHTe4cJhpwcNi2NkZhLN1RZyyOW6H-aEwYkARHaM6YDqBElh3SOGW2kDc-lyakG0hGWV2WrYpf7aijeN0NdpCwKapWYUyjcA1jdVgJM4XZ05_T0Gy1RRtuGNf6f3M0N7GpY5rkrp0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">7 بازی آخر مسی تو جام‌جهانی
👀
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95609" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95608">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97d2bcd8ab.mp4?token=BeWL7FsQDwb39M-4BLqEyhP8HEEZVIaLirm-qj5aPnwwvkucudC9n9od4BouFPT2lHz56ef84YR123Ol8MgEdoplBQWizkOfa6qKKDwmXsNmplb4wuenjzkxLa6jHTG_HidWXxiwpA0AxmV9oMvsVIZ1I5bV0shXOwjbuwArJEmAVdb7J2n6iqlgrGrOq4s_09Jzosfx1xmqUNxzeseALojwTj3eItRg1Oi3y-A2drGyWb8lq4s1nWe8Obk6XKf8dc-O4Z-jxZwR6VvUVFfD_j8h16x6oYOpJMiUb0yQQkTVIjSLpSjlHD7_exm6C2UQJfCXL6gKNF2Cv84d_ZWjSkMkPJ9pOqMQEVh1iw7m7_QxTMEAWYLwNpZP8_i2hkLDQ0JIc4zsFTWMrrcgIsPUq7tO0LFZsKm7R4ZsR0eontF_TBiFFAcoVPHOw_tqHCOKOSqDYsx5xNR6NuNEwABrNjsYY9FeLpCUa0XuOb602BgaqqjkgVRYo-KzT1N_Ledf64iKNrF4S__z7HbTMrjuH838ZXFx4AMpssgIHcI_G9T6-2e6Scax9-uXpRI4ZnMoSHGR6SnP6od1OXzMUZJ-f_o_L27_S9gOGe-gJu4_uVWnWPGPZ2c1xHIHBRNAlgx87Js2X2adywu-7DVjE1XaxsVI5aEMliqL1dwMXBV2ojs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل‌زاده: علیرضا بیرانوند وسیله بود و دست خدا بود که اجازه نداد شوت بازیکن بلژیک گل شود/ در حق بیرانوند خیلی نامهربانی کردند و حالا کل دنیا در خصوص بیرانوند صحبت می‌کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/95608" target="_blank">📅 13:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95607">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYeUJCdcdHT0W_5ukCJPB42aIJYfnJRymqZKJzaX1J8hC0QrtDSxxsP5RA2emUPTAxxDJmueSDQTdHi9tOlEyjx30TxH4Fq2iNDgzYcZaEjKnvS2ksYzTbst0zU0Gs_4_GS8HS6hwUlJaXtBoh8WGt0Q4bnd-oylW5TV564RrLEaVOJD7FVF7nZaaflUqva6GoMGbQRBzU-hzKzKsvBfQ5Jsr-coLCiVFpBJtLuvNMRuF2d8r0RAcrhqx3fE1tZcwrRxpKGZckxXtXdqmJrz5oxII9_4l1kkG1pnql2np-PJ-3wBA0UOWiEtA8Vzkfz5cVc0bu6fIUwwOA0PFoXomA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇦🇷
زوج آرژانتینی با یه بچه تو شکم اینجوری رفتن اسطورشون رو تشویق کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/95607" target="_blank">📅 13:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95606">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5b5dc5848.mp4?token=Cm28Cf7m_0AlW1m9HbAg6i_VjyQWLU5fb9pQu404ygraB7uDSzVbww6Tbopymo8p0JBm1YdwgBMDY6r22tTkzehxpaDb2tBr-3f3bvj1LtYnJd655TGsk5a3INhFRkiyCmFXoTtq1pZoXDdzIzh_zRd1CblCpOjCutZwp4uFJgWs75rcHtZUKjZnR65pwAtEXSfZ6V6GZhTG3Z4g5uhyb5Vpwod_xxK-j7g32NylrynpREmdO9Q-QLOuc-WV6gAG4-fWyb16GequGZr-9DjzzWeHSQu9hRA8ZKDXRxV0lu7f1PrcLFvCInOx0Qo9cCVgWwZhvdihDT1-CP6dpsPFw5hO5tPqqQySpsy8oFm5UEwwGFqqLNV__zsEB6qdAaMlb-pX8bmeOCZSB3fmlLTx_k_Jv_5Mh9EU11MW5bogXLAYrACszfjr67LQaLtkLI-4svD_aAaTKMeabxzScWjLE-xjl7n9gCxLsljJ50L6Ko51vv_crZ2L1gcfKUUbYsH46OuhjrG46g25N7mPXSR5skTXRXBbEsBGZKAjV-iJrn8l3qNuFN5QxcXyDcLve1bDRZK2jdNxZ0E9SzD2IzvXmYazGk0_Ko3BZgzb_rXQTZCmuFtuZ-Bik-xBcRjX4Qi5P-g8Wy-zWKVrcjQ46jAia7OsAtaf1mkGRXNXCmJj5Nc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یامال شاهکاره
😂
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/95606" target="_blank">📅 13:10 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
