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
<img src="https://cdn5.telesco.pe/file/Nc-cII8i0XDz84v1XFyEo6I0MXz71hzZ91No93OOe6vtbiucK4t4Cnmjvc7yPVp6ph0b-u1hoKU2vDMGSzw-2Z9nbyNZp08M4Cyqpn2-WV3jB73Pl64FhbSqNn_AUvLi0wqAQFOdl9KhCeNXJD-F0SgPRdaWtpK32KDbWzSr2gw6_l6-sy0iVmcNmlTkpIoWw9SpE_Bo4L8P5Y8PGcGwV4qNmxiNG-sC12QvjqU498LZYEUjXI26vkU9JE8UpbvyxdCRng5dCh-X4G3Gihott-bMgqQWMdIxFut2UeYlEknT0LMPZLsioFs8AT0SoCW42nCcZkod2-I-NEd13LcPXQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 675K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
<hr>

<div class="tg-post" id="msg-97176">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf-BXq-SWDGPbTORJzjgxeKusDAhdeloeJI2W8EFFCPifXq0F7KZLdxHUjnGRzptkgYun1LTkmhpDzOE8eEQpdThvGMZxnPvDc3CJhxDItz7kcAXVntC1R7WCQbQeSWygNN6i4qode_0t1SFi1zwyP8Yk_8PSGOCpWbSH-pHnMH7Bsd4cPlUiG31GAbBOw9lqZTX65IXhuQaWT6jZAMdbJ8AgkRiKMpwzjY7rJaR_BLlKVYKy_S0N2aGlMtTWWqUXMiU9ISruaQHa2G-fCPBPzfCRr8q7QrNzrEodNggPTw6zJLb7phUSF--OA2xS6HdaQJgm0FFebeVJOCLGYmTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خستم کردی بادوم زمینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/97176" target="_blank">📅 20:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97175">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شروع بازی نروژ و ساحل عاج</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/97175" target="_blank">📅 20:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97174">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ خداداد عزیزی اعلام کرد که داستان حضورش در پرسپولیس منتفی شده و با تراکتور ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/Futball180TV/97174" target="_blank">📅 20:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97173">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔵
#اختصاصی_فوتبال‌180
#فوری
🔵
باشگاه استقلال با چندین ستاره‌جوان لیگ‌برتری به توافق نهایی رسیده اما تا باز شدن پنجره نقل‌وانتقالات آبی‌پوشان، هیچ امضای قرارداد رسمی صورت نخواهد گرفت. هرچند شانس بازشدن پنجره استقلال کم است اما پیگیری‌های وکلای خارجی این باشگاه ادامه دارد. در صورت موفق نشدن آبی‌ها، قرارداد برخی از بازیکنان فعلی که قرار بود جدا شوند، فورا تمدید خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/Futball180TV/97173" target="_blank">📅 20:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97172">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhgwH8TzyXlcsvE5DYPr-PToevqX2eDJzEbo9RpLLq-v2NOvZh_VGRTXyvnZ_C44FOqYtujwTvX84__mLGFrzhJT8RTt_sNOF9iHrFrLTxXF2WkyfKJRIaM299QXjBm7jqdDaE26TcHvBQjzUp_ixLA538H3A6Aqp7V1BqWgVXfeCNrblEY_07JiREfQUVl8cqyG88yu7Gl_kRymI0GP6T3ThgYHFf9LhuXMtVbeSqTuW2zKcAsm26tvPl87XmwdM3gn6dqABcddfrh1oebcrgPbz4Ag0EI94EpKylblYA7jvGJrwNn6UgoMffKJG01XSZ0cRjTMYOIAWuGE9siC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین: متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/Futball180TV/97172" target="_blank">📅 20:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97171">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IP_NvxfRNm9z1eVRXwSpOKUDdpIAvoFMl-6QuWTL6959-r5Asoskk6pCB5VT4HUeNVk2jSBCOwfdRvM_LRx1eyG-aMNpk-iHd56Ptjc9egmEC72vhltBtbwR4iyp8pD2DE6q-tUNmPi0oEsPo7DQoKa3xQH3MYzJ3aqF8fedPmOHkC63cIuHBqVlKr3-W22bhEc2WXKAanw9nKyaw9ptd0yqyJf10FkSg8qrv9ToxkxovWEvx9ON1FucNgRz-Br4be0tr66c0GzQLvWy9UJjRLwnC-E80f_4T9WZYOZg_WG4Mh4-vMqQm1idEONnCHYfUt-fDLKNMlRueFSLV6K_Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری-دیوید اورنشتین:
متئوس فرناندز با 85 میلیون پوند در آستانه پیوستن به تاتنهام قرار داره و این تیم رقابت برای جذب این بازیکنو از منچستریونایتد و سایر تیم‌ها برد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/Futball180TV/97171" target="_blank">📅 20:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97170">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F5dOxiT2IMpiXQp2bnBefDbpcVhenh5M_vFlYHKJuz5_Q5XHg_p75geK47M4mdP_EvGKJVuRP8EnX_xJFlbaXO0miz_y7aN5-R9CuhvCCfqgmHabcUOZ6jGUwkh0JwcUuqJ3qmIqC75C5EQO3SOu_ZVnwPdHXP95iBhRR89XBu0Y_GAnjtjSmOJqcN0E6ad0oL9djQGlSy0KDDtMLXsjdR2nmoZpZmucFSJhNGni-Wb6qdjfvq_GZF4P2qJj-J598RpDmqY5l5maFJ34FhUhSCECOAwgfA4Eo9cZpXNcVAc3WSlzpX8iGE-0Vn5P8H0RUPGaMZ6Uuyb3ydzTrZgzhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
اسکای‌اسپورت: فدراسیون فوتبال آلمان درحال بررسی ارائه پیشنهاد به یورگن‌کلوپ برای جانشینی ناگلزمن است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/97170" target="_blank">📅 19:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97169">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYtCFxkNBg3by8gBv634rfmcLH_m6O_MFKsaVjEIiVLmfLD4n9ji5eNRkfDS1naTwYVDOd6xgVR_xNSf6PAfITM7IpKuXj7hafpHopaUCybroVdoUDw9Z7sNa8FT7g3KcCFRnXlJp5-_2RhqJoCaEJQVovfdgSB0dxUfK-bs-uU7CzpiqkEF2y5aoWHIE0DCNneAifdwwZAey1-68PjlspLPrpuYo3jMwEOcQpqejkkMP3DMOwwn2hzDeHacTT31Lthyf1i-igaTbbwIsLmjBw3Ien25s9qI2M_hojsAZ6gHmCBO2RF3F2Yk2_4QUn-ma0OyKuLGkeoNEFt8oG1WwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین وینگرها در جام جهانی تاکنون:
🇧🇷
8.29 - وینیسیوس جونیور
🇳🇱
7.85 - کودی جاکپو
🇧🇪
7.84 - لیاندرو تروسارد
🇨🇮
7.71 - یان دیوماندی
🇫🇷
7.67 - مایکل اولیسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/97169" target="_blank">📅 19:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97168">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=ENXrPmbsMvejbszH2UQAln9S81oP9hbSKWo2pzpWDmBeIJnvrVL4OSLOUhdMbGDk8XNvP1PEzUSAQObQMKZ2lnv_UTPTuZRZs8OfuHvbqIFNmchP9UySdQw_Lq7PdQat5g17diknunhyb3lVgVD4xxLdvD0heY-G5ZsRnL0PHorCC0mJt-2eotfiXrGdLingQSV3rSjHw8_MJTVgTIb9xFj7TM1lfdwE4eQIFm-1yaCJbujMx6vs2cYW3fFcpSboyKMyH6loaf205ajrkw6kZpfY2SQSGccPIzfSiQZOhuavY7wlJ5o69dbLmD7t4z6rA15vRKhnp64Ofd_tXkPmbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e36513eaa.mp4?token=ENXrPmbsMvejbszH2UQAln9S81oP9hbSKWo2pzpWDmBeIJnvrVL4OSLOUhdMbGDk8XNvP1PEzUSAQObQMKZ2lnv_UTPTuZRZs8OfuHvbqIFNmchP9UySdQw_Lq7PdQat5g17diknunhyb3lVgVD4xxLdvD0heY-G5ZsRnL0PHorCC0mJt-2eotfiXrGdLingQSV3rSjHw8_MJTVgTIb9xFj7TM1lfdwE4eQIFm-1yaCJbujMx6vs2cYW3fFcpSboyKMyH6loaf205ajrkw6kZpfY2SQSGccPIzfSiQZOhuavY7wlJ5o69dbLmD7t4z6rA15vRKhnp64Ofd_tXkPmbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇵🇾
خوشحالی پاراگوئه‌ای‌ها از صعود به ⅛نهایی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/Futball180TV/97168" target="_blank">📅 19:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97167">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grfBEd1FRVsqmKdqA0oEftW1kIZH1Q1xZ7E1f2A05BqpsSDskwvfHFaZBTg3ExnjPqOURVF1Aa3OMpPdrmE-Vyk7hpS5OfeUEeFFgzCfKdKQdjT0_OLz6mxmZmERb4x-enz8ONcfYcOGivfLGitcK5TyWKrs0aap1TSPZoVQ_AXwG9a-By-iq5tC4e74rBbmPNjy9k-dvk62LyKDYBUkKwMCyzbqFWSYBwdafeNvGsbb-jcXnjmly_TyDngrXz_ov2aOkHHXxjSRlju1opj-WOWojLxBtkEKac4UX4SeVTdVsH56feGpMMApgOqq9Q86o-tUaQnNlxTlPi7EGb-6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
جاشوا کیمیش دو بار از گورتزکا خواست که پنالتی ششمو بزنه. پاسخ
نه
بود. بعد او از والدمار آنتون، ناتان براون و مالک چاو خواست. هیچکدوم قبول نکردن. تنها کسی که پا پیش گذاشت جاناتان تاه بود...کسی که هرگز در یک مسابقه رسمی پنالتی نزده بود.
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/97167" target="_blank">📅 19:09 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97165">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvg5bh5o4XgXGHHl-t-iTtAmFQ7PhipamVaLN3dQWvpiN1y5HeLbZ5R1Ow2ANYPpD9sHEGqPlbbickXxTn9JFENWfrlBtFOXhF-HRAuy3Mas1XVTxpE7LHZ_CR-nNwEziMH-muy5MA_ifiec5YX388oxmbSmDxQWEZGec8a1P_skyBacJ9Wt2FwurdBhnqukgUossqRVCDjI_r1zIvmtUC8BjczyYnOsVisH0Bovtxs_PmEbMh8xsWy1wS3f3kdtSbMQVhue1iRpFbXiuayaoZJKVa45y5giS1_WFIIFDG0W_06Rj7UzMGlvtboWVhW3uR4hcbMkcwvR9JJMhzyRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lk5cGivFVkb4JWkrdK4eXYeK-HzDKtiCdQJT5rMS4CoGopIOH13_zRBAp2djnPDkyN2uAF-Bme6rLS7G0AYdfwxXwkDCqLWYDO4-ysET6cZNMkyObCTkN9Qr-RwKZiA8v45RYikOnAQrPgkhfk-z0HC0G3_X7FT3OvDc_qgtHh3_49Kz9TgGVkkafCTFP5LblkbWZE9ZphtaV5aYZLrLciofxSMIPsltJrFdlcGLsfph0yoCDRr0VT79oDd2TuVUI_mzzMICgtR4WUU-WsGwGwCdZNHFs2uyIoOwo7QaEfF5YezKfouORPb9ztOwxgSQYz-4WTgfj1d86HUceZ2lmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇮
🇳🇴
ترکیب رسمی ساحل عاج و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/97165" target="_blank">📅 19:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97164">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">⁉️
ستارگان جام جهانی کفش خود از کجا تهیه می‌کنند؟
🏆
جام جهانی یک تجارت میلیارد دلاری است. آدیداس چگونه با تولید کفش‌های دست‌ساز فوتبال، سهم بزرگی از این بازار را در اختیار دارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/97164" target="_blank">📅 19:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97163">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-9XJmAd8BQvjYvBXDEhn_O5F5lUgrhN1RUtsL-_FiiJLFh72qDsO9XJ0Jso-jBaDdqEZq40ZVghHtH6bczCAk73xzMahVw7mX2HQePjALC0AtxRcUgX3-r5jxXFYeIvkVywXsgPxK6001coXltd_bd26ItPcDaziMjsM5TnNzaJP9izxP_8kgAKvAj_yUSgvMhLrOOBRm4NYf2iVe4WRl4JVcHwQol5P47TIom7u6YwzFQnKVFlDwCkYwLScHmnFQG_AAyZlHYm8Ew57ATOnwiZKkB5VH4ZXKJ5MUJ5A5l3rgqjr3K19R_aCVAneqTfXI35wGTSvLiAaba1CNmBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ترکیب اصلی PSG بعد از اینکه یان دیومانده رو جذب کنن واقعا پشم ریزونه
😐
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/97163" target="_blank">📅 18:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97162">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMUYFOw4KPTT8Yf8RVt9hDTy9sIYPuzaqBDiaRlay392g6_FCpeDWyP9-iK0PKY8MbSknOKLK-rPt-CBzs9sZRVZKtIz9zUk95Ay8gc7e6Rqp-1wpz2bKCYO_dMkBNx2tFy7QW_t9TTVDX26d6J-EPD57A-7eLv71JqzzG2lzJwXX6OpGAaM3pbgyK1Sqevr2ogWk5zXwye7azbFNqo8hVzpHStyyleDIO0Za88156IqtowE_h6YEK7mJLqLgN77TzSLwH_ONuezKBYdiNIt1gvUyXnJT96lst20-OWi9aLj3NNB2vQuF8pse2Kim1uEyOhJHpDIBHA76OlCMN1XBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇫🇷
#فووووری
و
#رسمیییییی
؛ با اعلام باشگاه بارسلونا، آنسو فاتی با عقد قراردادی دائمی به مبلغ ۱۱ میلیون یورو راهی موناکو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97162" target="_blank">📅 18:36 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97161">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/erF3-LiHJ36KyBnMHlt-ECso37k5UpN4E2mJRUSFgYqsSDgYlDGIBrMrQrVPPkLmpAb5XnTXW9g3Ungu1pySn1cj0ufuUzRN8qKb3g_bxZR0Uuv0mgPj54Qf93Ajmv9TjSxEIF4DUW1Tfv5Se5RonKqJ14COTL2RuCdkPmYxqIG0VeeijSgqNqsrgT9iLzYfZ7VRQ5O-wfWh-OJ-iW_AKRFB4TLxnkIOi-M7JIlMj2K2djePapLcW-nC0AOCyQbwkmVpWXbvevc7KbWN1VxCQLtkJ-r5_6daEPTVzn-74KXAicRQqBzJOSZLuCaTvS91bTMrLYqDZmwYFwZF5oV_0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فووووووری
؛ با اعلام منابع خبری اسپانیا، باستونی ستاره اینتر در آستانه عقد قرارداد با رئال‌مادرید به مبلغ ۶۰ میلیون یورو است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97161" target="_blank">📅 18:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97160">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GO0kFbOL052jYPnrwIcMFmNcMk8s3C8Rw6WhlzDrqe15gJ1xY42Ug98Cee6bklDM7Yhn3WaeaDuU-YEQGQibrIp03n5EPn7a31X7Gb3rSVB62DGv5vHcC8yXxC4SSGfrZcafhi4u1UPSe6NcQIpkxW2wVQ3sPL8Q2H1qVO-aJQ5Xa417Ij5DvESAn3qXcvZMAK3SVZwav87DqYmACNbH2dX7nIaF2xaOT57-V_D7Aqad1UUbrYwGFJeB4iSCye-p8kFZbFwkVaYJu8j61TXErhCXY3OGfXKZ_7tX3uYyhE-ztAyvxKnUAmWx7EyosuIjCM16pq5KySiL_o0MO9Pckg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جای خالی ژائو پدرو شدیداً توی ترکیب برزیل حس میشه؛ آنچلوتی به خاطر دعوت نیمار مجبور شد ستاره‌ی این روزهای چلسی رو از لیست خط بزنه و حالا توی تورنومنت مهمی مثل جام جهانی یه مهاجم شش دنگ نداشته باشه.
درست بود وقتی مهاجم نداری نیماری که تو سه سال گذشته ۹۰ درصد بازی‌هارو به خاطر مصدومیت از دست داده رو دعوت کنی ولی ژائو پدرو با اون آمار فوق العاده رو نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97160" target="_blank">📅 18:33 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97159">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=kDOOTl8_jHUXesZsmrhnLFfjos67x-CSWjalA3o8wgH8QLKz_vU8xokcMU3JgFUW1vIg4fx6r0Gpv0jeY2qlwZYdKtdn8TCa4DkhkegvPKY_7jpSMJavecKDx0OwRcNpe0qVkFe1U8GPwlmglYHZKAZpa75-gBso8K5bXJU2wW67avKZfjFfsydsH_urc7g7nZ900lzrwmQm94ACATDaPRFFphG4FqTKEvx7LR62hWKj_gTV_o4TJJB5sdHH4p-U3iHyZQgtJPNAHZyWTVOY-wIwOTuf7DoiIppW1ryf0Br7EwsbLr2wzQ7xqjTAX7lK2r-P1nCZbvQrtEGsb6TYEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9ef52a64.mp4?token=kDOOTl8_jHUXesZsmrhnLFfjos67x-CSWjalA3o8wgH8QLKz_vU8xokcMU3JgFUW1vIg4fx6r0Gpv0jeY2qlwZYdKtdn8TCa4DkhkegvPKY_7jpSMJavecKDx0OwRcNpe0qVkFe1U8GPwlmglYHZKAZpa75-gBso8K5bXJU2wW67avKZfjFfsydsH_urc7g7nZ900lzrwmQm94ACATDaPRFFphG4FqTKEvx7LR62hWKj_gTV_o4TJJB5sdHH4p-U3iHyZQgtJPNAHZyWTVOY-wIwOTuf7DoiIppW1ryf0Br7EwsbLr2wzQ7xqjTAX7lK2r-P1nCZbvQrtEGsb6TYEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
پشماتون بریزه؛ سر صحنه آخر پنالتی دیشب پاراگوئه یهو تلویزیون قطع شد نزدیک بود نصف جمعیت سکته بزنن
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97159" target="_blank">📅 18:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97158">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=Z--8mK1N8zk_TP7E8LJuV9kz2sEqNlEGk0TETx1bgetyZAa2w3zZsRjfZ_GfUboeWDN00vrFuDpAiL2qentDHwJD9Wic0s3hWEeG1dQ3UetjvdE61hLDST7gQ5gjIphFdbxNfDF9H5gwx54MiPDgcQr5RvraUIG0sVf3Yccl-Q4y0ktTESJ9edMBHFd9Wa6FXLX9YlaQ4T9hEdmrssrF7nJGPTQbBgd4Cf4zZeV5xUuSDx39d0jeDE2gR-SN7KIzEr74TCH3eCT5v09U1kjVdFcndB0liCzGcN8jF1x7ByTWOZ85fOAbaEOvTI7Snc-AxDTj1RUHOigM5HdbsFADww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9b9bbd43.mp4?token=Z--8mK1N8zk_TP7E8LJuV9kz2sEqNlEGk0TETx1bgetyZAa2w3zZsRjfZ_GfUboeWDN00vrFuDpAiL2qentDHwJD9Wic0s3hWEeG1dQ3UetjvdE61hLDST7gQ5gjIphFdbxNfDF9H5gwx54MiPDgcQr5RvraUIG0sVf3Yccl-Q4y0ktTESJ9edMBHFd9Wa6FXLX9YlaQ4T9hEdmrssrF7nJGPTQbBgd4Cf4zZeV5xUuSDx39d0jeDE2gR-SN7KIzEr74TCH3eCT5v09U1kjVdFcndB0liCzGcN8jF1x7ByTWOZ85fOAbaEOvTI7Snc-AxDTj1RUHOigM5HdbsFADww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد باخت ژاپن جلوی برزیل، اسپید رفت که یه هوادار ژاپنیو دلداری بده که طرف هی داد میزد "مسی، مسی" اسپیدم کلش کیری شد و گفت خفه شو مادرجنده
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97158" target="_blank">📅 18:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97152">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d_jpV-Oj2rIfwDy81uPHJCwzzaIdYSiaF2V78BaZvAK4lQPS2m-IcpFgSrgsLuLg7WVVtIMQ8OChsNeZn0LAOqY-oyad6c_JICNY9YyMYOjosYWjVnLwi2cjxCEOEd1Atkke8WjVuxRfBLuqI8cxCPrL3Mm4Y5RW4mKzlf_Vsp1HmYKi-Xq-KLJf6vGu2fovQk5JtiKCaAmKyUaWoycXZoHO-ORJdZyQiAhu3kh7Zg1lktoIXTZjZ888ZiZBRI9l-V9LUYF02SUlmwY31Tjf3YoxkQKQhxWO0S8y-NVdqvz849ed1aJzknrAH5DnEa948Pk575qenvpFvIfboHT1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xr7mDNhh5tU9MrH9aptILSx45JoyfoEuRIfSiWUkMBNKnv6sVwLMv4rYw3k0tgRA27yZWA3U4aOorvG-eLVZ-w5gXxTyyjf0DZJIc1q4GoRYj43kJbOc-41ANb8HYFHHqyDbFPPzLpdTfwq3X9EhWLvocYgQ8kQ0c7UcFMV9oLKGE7mS0dXN8Y4FCz-Z-QUlhMHK2kmih5RZBhi14DIRNIGXyWhRqF4wYjJrzj8Fty9yAu13d99JYENF3tsCz65Rc3npcujyIdWy6AhVPX2iqfHBSbw1exgjqzc1mGdswPKrKcDqiFO4hH378IhHzk3G-NmroGxjwYSiXOqbM8b_Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/et4vyubH4Scfsze-GX_R_OVEeDy0vaw1fEU4APsnFXezwXfr957FkNpG_K-WGAJEcWrIj8hUzs4G5vdqcGnOFqpDVUmlqNO3P5RQiBLqWVHeZEurUpjmBjFCVXDg8M8TmUKD3Xj-NRc5rnqt_ndwhC8oqCH6kc6wDG_oqU9_d46pR8e_n7eoPv9CLs5iweKGmgn5hNRQ5zniGlmsXO8BqFdCRDaOd02Aub3YJzOfbW2ELaPL1pMfJakZTxTC6tkoea9mMeFeX8SnEPxjhYmrehAK8e9ERUYsHwCt8PVDg67D4TatNEoQb72_6rOIpPDVZR1pvu48JEB8uNUMsd5SYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffk-j_2WMb54LPvzQ5MVK21bRhntXjK83J8kv3tk4WL_HlZQGLdJoOnuq2GVgTgzP6xYOjt5bWVAE2vDGZLVsmpQd0qEVtR7ii2XySB18ikx3tn--jJtePyldZ275VxqcCJ8AwadmOzNBB8nVsgpuDA3H9Egm_i5-Fn1P3Tfb_JmJtIASZUeM6QUYmZrfd7xQm2Mi5OmnR-Inz2-hgRp3VwhID3bE5WisKPbLtWcihoT4ukDk0M1PuL8E6VGc7etVEyW7U8T5pZ5Vhbm85hTQpm5czLwVr5G3SaZ6LxSG5Cwo9PlVGrfeuX1K2OJDLZip-NnLrqQ8Ggm3POlWoZFtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JrCbZ_nUnuzgc492HhxgBrcH4JIqSMkPxLJ8DiJWsp7MZPo4JnHgMqQeS_R30BapSiCEM0YZgBSZd0vnkEurmdtPSDPWvkxywkesCGD67cpjDF0PBRw-2rv7jNHvle4NuxJ94TJASEPqUH7zaW4-8_9C8GHClzkHcxC6mNs8v8RJ761Qaw29gQ0nvkuwmNV6730yDhnJIm0zjNN89IrbXwd-7bAg9HOdq_uQ9KpMEAt6sMCNt-B8Edwc_3eV0uLmCgse3fb04Mg6pQhtlqgcUlSPcRSjn3Eth7lDY7r1ZOr5Z9DTVMLsyWxz0dBpakjHx343_WpV2QYgBa8bhxXi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PJOeSzlHYJwiZHjtHIfmWLyS6fuBwG5BezaaU2NmMboqwR_Exstds4stCpsSOF5sbmrV2L6VVG3PRaSKPt70kHTgR3EShIthkTelzOwKHD61Ala9w_0wi2XviA0HfoFUgc6F6F8GOB_aREGx0cYnd9qmglQinYOQZSjYzkPtm6FNpyGH_N4DRx7tObwaxXBYbIIvXYxpz7DsOnvqKgsjghws34SeHGwnKLFd77T3gowXOQMDIEszO4MLcRbZOL7N_uprApi2ZIZFO7X6Yl7IA1v2Yp9yrh_vOdbcRgp9xoPf8rtGtzlkKhRXA45KVbF3BYXJtgLnmIIY77MQ5b0vhg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
فضای‌امنیتی فوق‌العاده در استادیوم‌های مسابقات این دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/97152" target="_blank">📅 18:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97145">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hd1P5st4TeRDZxSFwZqjFistvV2rw1joUqyoN4JYtzg4vSM_KmiKe-EfvjMvcmQpxVp-jSVPFzJu_A5oFfB1DszK1DOkw9BRwDRTC4UVt6H-o-ceJdzI55iqLbqMqjUngG6IX0TmsTqx--fjl5cqD71dVaL7niqqDx3FVz6qdCpHCCBJhRxwn-XYUczJv_fO3GlwZ-xFTvPtw5I6DNYypoWjZp6yNKuPd7rUkn507R0jntz_HWVnh8GUrYVh1az51xYFi9kwx1fdVtarBBx73gx_QhiigTyBggx4FLr09kqDYc5se1e6evmdfZ3d56_723AR9k34-KY2qpJDaXTZig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAikrWcrtrM_z29MaXtb7iKxNMQyJeHwY8wWvEtK5c3W3fKBRehxQs9HkUg6o-CPVNajWsIipeqTHUBEBUYxEiYwrwm94YpeslGvV5Lj478WPO8-M1g6uu65BCiezmSqyKE_AGYNOuTw8iIlBLmdfz8v4pDAdP8OnOT9qYbj-99hHMJLmFCD92-lBhJiIOWP1nXko_CjsBJSaK3qXPLQcR1Q5iOP9O2GIGUQPcmIiqUyNaJbSxSU3wGWbcOIKdajVz0cm3mLvQtcpNWI6zaY5OXGqt-Zy37Mt6b54bHR1RCHDUN1MoucmQssty3GI3cgTxG8xx50rsryhAMwb5TKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jjcUdfBvg4hwo6xz47bdMaEqZLz146mbhbvreg4cCgVUNfz2sS8SwnffohVFjCTpwaQhXtQGUyIHlss4Z3QQE2ROQoIhwIxJwhmn5uNLWm9ymYImylsVC4y0cf8rrW5SC0qskM7mD18q-REhQWf0tahaaibUQ3CCjCeph2vkQSilOTwfFP8HxeZ0u3D2hj7poQiwfXf3CWSv3OPBd6gAV4aBMIrY6OGQLqxTw_YBNrJ4j0QojhmInLlYhbCx-9698ip76UCrkefVYSNkCKVWljQdYt1YeAVj-c5e8AXcD5L9uyqJ-SxuBcRlLLWzmsi0vg56jxEsPLZPTQpDLG8WRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZsCG14gT-cr2-1qXtbel5I8RUmwRqHUloRZcXlcLeSEiLiRazGQoGRWaB2jCTI2XgEKlD2qESzYE0S8Sz6dRyxfXZC0DxDQ7vIXlE5v-HdYOHAzRWKSc-xqLLu_nNRF8Woj0GuORGUR5zCmdOlhV2EJvRqOTC1lLmdljCA1bsiuBBmWJbf6nBCph6FBPFgo2iVyeIoikR79zFHfpthqWG-HUggN8IyU-HjaO8mGhwLGpJDpAIF92hQHfo5HF6PyjbJLoUiQgbNJa7niQBCJbFGa2HDIK3HxjOyF13gV-KmNRogRDLYwlTufSCJR8bkH8nBPWyE23VgqZVM24NBwcxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U9-WVK_Cqh2vfGtRoNeutZx-26UVn78gn7m6oKywvWYYwX_HeXCxq1qQQlQb6p8R722FPa61ejsy14OxAJogIp-CA9IgyDz6Ev3NOiAN_ue4c8xwenL7b1QFv3DF7zs2HQw6cARuUyjGJ6jVtT1SBkRy4gfgRAxI4O2RSkHk_EWcN7WVkQF6be8E8JKLWV3oDoN7EnBorXTZF_hzIL5RPew0esg9_pn0ZKjpmRmPXhNMNrXHMplGleFxFuc8zDKLXKsUxPGaCgIv-cjBqfZoZC4AIIg8f0nkIyhKDJkKzzm5ywpjdd_C-zb7KbzHH0g5cV1K_PaV4S9zdfHjZF9bRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/api1yG50cffQvSM8KvIRh8cPPywIlgTcpYvoI1Yz6cLlRl0j3ShpWI8Qyp9TCQNnZeMi9SrkOpOkpxZC5nSLRPkkPKbuKYmxfLvT3o2lhcfgoQTNq4GRrDNSay17kky6FFMgCxTBs11tr0CwcGg1tzLyS6mUC5cdIuczq99T4iVXFwIPDbPTVmJAez2hm1g4qdLxpxI_yiNfpRWA_uSKPxsFR0bR8lIwE0Wem_PzhC33uMs_v71axgUcmdQz-xGgTLPo01S_p4b2yFWuzD4o_vUzBxUjX9sCs1bU7XmkL9c5tqoKNJnvStYYjrDDoy7stWuH2xF56AFVgjk0E9Usdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WO3GA46_JNqh6kO0sh5zeXoWIa5l-I0VdR2GXLIoDpRkkHE-6zWscCfS94ocoT_E505ME_oSotIYbkyBUMG3DUZVf6DUfoAOg4AiU0oPw_8_5qB1phYMz_EO_8FFJpXk9LmwFiGEw7MFraE9f8XLXolG74i6bRT-j3OF6tmCEpNHZXhb_RgnOlv257Y2g1-IFMybk1ABTVEbbnevfSGjpRaikMAV8lpqFy6FmMkw8CXR3FlwMFIzToCbaS_FwqNqdAndeSxvwHoo_2w-nk-77pJx60yOaYbYmJUypT0x1niTLURGtKZkRi3ax0_Ch3rQDn7ujMrJiYTaFaoomxhMlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
همسر ریاض‌محرز در ورزشگاه‌های جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97145" target="_blank">📅 17:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97144">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRgfTSxYVMPQGOkBXVm2b6SIK1_vcoMLIHMRJYqrmmtMunsr0Cfx3CTNe6_ic7VuMUD0oOpmFYGrVjkNkiVaRHAC5cj56BmFfH88ncR5mSVJAQZIDQA79Us0kNkoE2NZf0BZp4lwgXcDM4mvSbJzX48J0SQQTg7A90FFM6-b2PD8fAp1FaUfa0ow1p6pA0DWB7VHj-MPpCEEqZMDQuEfsWlGm6HARMqE-nG9Rjt-Xi4UMEPV7b2e64UzRhpnwEVRPt45lwMuMpRk4J3d4NnJQxPCpJFOASKB9wnmoxGC58NNxTVecGtOsFrt1jVMAgMIH0-tO4Ii1O2X4nU5UxOqTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
✔️
فوری و رسمی؛
گونزالو راموس به میلان پیوست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97144" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97143">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEEOATv53qeVl9LsocCFne0yfUaeucyr3r7lttOMwwxfhw6k41-IS3ZdiCEj5lYG6iuQbu2PL4fE8w8v-E-4n-i2I0TJFmhKd400NpTY7RbR65eYdl6CcR8QLd7iU0ALcmi4mTo3iAermeL51A4Hxs60VHYQ5TtPvWRxVopmjqtUl9QS8XKOyyRZ-Te6EwTbAZe2CEvR7QM4AOwARZlhmTikIBTZt6-6Bb-pR02mmWBbCYa5r4zBj1I1xhuGdvlFXyBLN0ZdiJmXRig8U2XKsSaNI2qp37_iPobJ66dVLvXhhgNywOLXKnC9gn3LEQ-oHI_HCu8LhVhGz99PbEfvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🏆
رتبه‌بندی نامزدهای برنده توپ طلا تا ژوئن ۲۰۲۶ از نگاه‌ وبسایت Goal :
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین.
👑
🏴
🇫🇷
دمبله
🇫🇷
اولیسه
🇫🇷
امباپه
🇪🇸
یامال
🇦🇷
لیونل‌مسی
🇬🇪
کوراتسخیلیا
🇳🇴
هالند
🇵🇹
ویتینیا
🇨🇴
لوئیس دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97143" target="_blank">📅 17:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97142">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rincd8t88bdniycA-fXI1fRf0fWfGox5vqV6FYZx_QQKWyHCTXYdUBeT15YlD_WNQFozddDBGQW-M8SaT7rNlYUemFuoClXlNJ24t7zjTfO2hw_0Kn6O4dFoe-Tov221NcgUvkFv2t0XnzjRQ6kWByolXDlIFqV_Vp9M2erG6yuhgtoOPMfswMJLP-6uKp0QcIZVbslKCJadQqIDS2N1fMmMLzGNpDVgnnLM2YHH19-tTVWrS7panpTNwDlRCdXhJhDmBhB53cxgejnoyt8_60oXKUjw2BztvAEybaDS_TT-7DdwxRZzLzdX6UhTYhj0rTCVc4w-C98odIul-EPafg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
❌
فوری؛ فابریزیو رومانو:
فعلا هیچ پیشرفت یا مذاکره جدیدی بین رئال مادرید و چلسی بر سر جذب انزو فرناندز وجود ندارد. انزو مورد توجه رئال است، اما در حال حاضر جزو اولویت‌های باشگاه نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97142" target="_blank">📅 17:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97141">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=RSJ7UnpvMhINm--NzE9e8M69VJNT7WrpBBM1ock6jL5XOg8FWVnAEbBDuoR2XqHdK6Zb2jLXA58y-2syLNmMRX1FYUM4Mf2vCoam_ND3LLjTDw4cIopT0ocovQC2gGLqVywKJywu4IloY1M1rzpjlDSw2Noo6DQg0sPcE79uhx-2sbkuP9wLqk8YIGBc1qK4XmltJvdvRmP485BCfGS1vnHgASfAX0mq9DnUcC12oD2TpZFjJHUARpDlnbF7ySssaseRA7NFkQXaPU5TJlRD9o-35cBRoaqUV_HX3p-GDVjCNUuurXvCZ3eWG2U_b92fuA2iBa62jf2O6S3U-tOGvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1401efae7.mp4?token=RSJ7UnpvMhINm--NzE9e8M69VJNT7WrpBBM1ock6jL5XOg8FWVnAEbBDuoR2XqHdK6Zb2jLXA58y-2syLNmMRX1FYUM4Mf2vCoam_ND3LLjTDw4cIopT0ocovQC2gGLqVywKJywu4IloY1M1rzpjlDSw2Noo6DQg0sPcE79uhx-2sbkuP9wLqk8YIGBc1qK4XmltJvdvRmP485BCfGS1vnHgASfAX0mq9DnUcC12oD2TpZFjJHUARpDlnbF7ySssaseRA7NFkQXaPU5TJlRD9o-35cBRoaqUV_HX3p-GDVjCNUuurXvCZ3eWG2U_b92fuA2iBa62jf2O6S3U-tOGvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
اسطوره‌های‌بیشمار در حین‌بازی برزیل و‌ ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97141" target="_blank">📅 17:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97137">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UPeOHIeHAoY1tvWyutHxduO7QS4MAZDfhnzq61TqLtGyvU9iSVWgJ2uprgYoHXCZd0OxRMN1XDOmFoh_-VozUASP7JeEGHFwAUbD199FfSebvhrPZberHy1cJbjYuxDEk2Rj_xYQNLYADw339q6ZHOLW8EXhkpr-GvHOvXjsoqAN-lXGnp2KdWXlYfvPsYCHiCPw1nzD2rHL9t12Gd45RgY_zTSKNhU5LjCv5NeZB4Of-7Jz0H_03MM_990WKsqFvY0BJdKagwWudFeUarD0by-TkYlW8AAkQOmXewK0N46Vk355oYNsrnelkQyG7UyeVy45KwlVzXWQXtHz7wPZRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOp7k142i_tZP0ayLa-mkuYsI60PNrA6dDJB_Jygganfs1nahKKBeMS_t2i2jROHSsCZjGOFO59aeR6jKpdjnhqC5SLISVF3ZJi-kfvCTynKZV4Hbhw1iyb2cryOqBDDcvxwxF-V8MGWp3QkeuMqq7QAn0CqWnMx-YGoAvPaL1X-gqLFycXxpM6syM7wvgd91w1I81LaZpckL3Oy_ohfCmJoKSfqsfIlo83YUggVbaUIdfzYq6Y7g4MkNgo22IQEa6CT8vnKNRVdvPUlyJtvhH6WqhIwrnJceQMF0NFinNog7DuQ5FzxmpFX1svjlA3Tl8t6ofEd5kew_9yKjWuC5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dMIdtgkgvQzBfll-CcMPTb5wNOoe_HNh2uXM4OE6zahAtnP4G4DTNpSgOzMnyFx7fJ3eufPy_xtgQw_vUpKqruIL128BgDunG6pBYUUS_ttcMoFh8DDoQkU0nYQw13G7oOscTXgmxOzw1bCt0QEewLVN_hOU57ZIGnzRLE2ozESHDyFWOmNH_ftn8aWysudMbgOeNj-04MrBV8jxHlaiAFNMSfVzie9bZCKc-RaxMxlUwUxt7_ut4dYSxceZo1GI9UPF3Cogv6O9bC62zWtEl2JoFCsymIYbt28kdOzUUBJW7GwllAnhcld6H_Vn5QtJFHnTvaWfxejSjSKQGlb3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMWP4gzYsztZ_0TBF45OV7Qn-WWlt435ddBVjwABPd8IWz9JcVFoLBPiSXG6pE4jA2DZHAH3tGeDizbxZcQ2snFaGO1mcUvM5lsa6qPYvQx-8f-dvOazFHDvB0uKY7H-433CKv0i6cbuAoy8rEa4J6lFWre5gNQYwXg1sqQ4t6K7nCyXgbm8D9jfa-jsYLctuexb5xibbp6fLLppcp7Hztzu6tzzbf5ny1jvrS81qTGjEGTev04w_n6AoCmdOGOJOStcpo0BprO-yUcobsKu1Iwo1zfOfux1sXuU04RAJKadV2k3Q9r6i30EGiXpX2MxNZRZH7pt65APqGT94U0KvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
بانو میروسلاوا مونته‌مایور مجری شبکه TNT اسپورت جام جهانی هستن
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97137" target="_blank">📅 17:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97136">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">😛
یکی دوتا منبع خبری آمریکایی صبحی گزارش داده بودن که جان‌سینا و زن ایرانیش قراره دو هفته دیگه بیان شیراز برا یه پروژه تبليغاتی. ایشالا که خیره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97136" target="_blank">📅 17:08 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97134">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdHuTSvhtsckY9Cu0mhXQvHyGUtG3XTYzWBCZnaSBzk0ozncT_-vcryeh5Lbb1a3BswrSpoioQRJcNE7n49wexxJla2tt1dywG8iDLRx3k6JFZaTLlPJ3MZLFK3kQPIg-pA3cjvTbOPKgHk0aOAUiacee2k2hDzIOU95MaDJ7G4cnKTtWFJVw-mMOwtzJEtM5df8hx1k70XvNKRESGBjjWpRosKCy2sqo9FHf3LJL70kyMh3TmcxVa-kQ31rzisaiDVx1r421H3WRH2STnuH_G22NwYAA-6Qahwq_w1Ugoqw6GwoAzh7Q6N1F7hjrGrlWme0F1kiONVMLmNiSZgyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pklekeEi4EXM2-XhVb_TLRR4-z9Cn0u1w44dE8TWI5JDmfTjzxj-N-8VFQYZdawUyUJPl1xsiPTs8m8cU6NtjBJ74c0L25zE0MPh8VzYQPNWtPF-ctdpEJ3fh8pT0dSCO1DTM2FPfmzCeZOnL_O07z-vogVKjxSIBjtMUWWsyEhvt6iqE8QoZBtnFD82ABtPATTd44SraCEg56_mHm3FvczAkBRaoJ8maPHJagMlNQJEJ4YEoAd7wxnyyAVO5N0VIGdqE2Qnh_9igLYlF9xGG99RWMqw565pbQg4xEf2SwgABklfVt20bT0Tb8aZpDzvczQUEOfGiaFRlbfgUKTQhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ظاهر جدید جان سینا
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97134" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97133">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=EzSdB-YJXWCmKf_fCF3gfOoSGMX0sr4Q4QIxypz7Gik1_FjBrQ0o8C1ABaCjnFsZaYg-kLjKcJT0ZJuXzB7MVmHy-PRsXIB9pvHAR7AGDT_xIY-0j-kgIWYr45LiZsf-AQjAn0NrChB3Bat1q28gsEab2XsBRQPJTPhggWoxRq4PJWfW9DVCK5_KNc7YjE8b7PpCesHXsmk9nrIwRVO21VaNV07kfhseK085XM40P_aIpxXZaNlVlPMC_FQ_a3AuBlhDlHpLwGj5dWAqByZ7wIQ8TUc67myI9mutA8Txifav3Lr6LDWzUHm5lRI_bgGOF1l9rgxhSqofI5qGWTWFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43c88f5b44.mp4?token=EzSdB-YJXWCmKf_fCF3gfOoSGMX0sr4Q4QIxypz7Gik1_FjBrQ0o8C1ABaCjnFsZaYg-kLjKcJT0ZJuXzB7MVmHy-PRsXIB9pvHAR7AGDT_xIY-0j-kgIWYr45LiZsf-AQjAn0NrChB3Bat1q28gsEab2XsBRQPJTPhggWoxRq4PJWfW9DVCK5_KNc7YjE8b7PpCesHXsmk9nrIwRVO21VaNV07kfhseK085XM40P_aIpxXZaNlVlPMC_FQ_a3AuBlhDlHpLwGj5dWAqByZ7wIQ8TUc67myI9mutA8Txifav3Lr6LDWzUHm5lRI_bgGOF1l9rgxhSqofI5qGWTWFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
واکنش آنجلوتی به گل‌ لحظات‌آخر مارتینلی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97133" target="_blank">📅 17:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97132">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXBOGMYzEmfU4-O8t9ZJ0qFTgCWp17xvTmveRGfxhKS3hVyUSSrmvVS7ZoR392gFXdaDK39zeHNJ4ezJnDP6MDmE9rs9TT4Lu5QV2QGAAfQ1xwRV-Qhnf19oLITL-jFpn64bpdfnhyAUelOGGlMBUSTuden7ZG186oFWWw_kc_9T9fpTe_pJB4hmHjwqGRw97PMo9JjNaSX7If4tW1TeONuaQnpy-6TzTfyOkQJrWXm1RsiS-G3A0OBE-Dz6qJ3m5tAuY-uAOSQBcyFGjvCjiy-OBLkGKV4_h4wVJF7ZpWGLTXW_tgzLeUaxZLo4vpKSjiRU5I-epM6T0tlwRpZYkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇾
طبق رده‌بندی فیفا، پیروزی پاراگوئه مقابل آلمان چهارمین شگفتی بزرگ تاریخ جام جهانی محسوب می‌شود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97132" target="_blank">📅 16:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97131">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
‼️
🇮🇷
#اختصاصی_فوتبال‌180
؛
🔴
چند تن از مسئولان رده‌بالای کشوری فردا هنگام بازگشت کاروان تیم‌منتخب ایران به تهران، با حضور در فرودگاه از اعضای تیم بابت نتایج درخشان و حذف از جام‌جهانی تقدیر خواهند کرد. از خبرنگاران رسانه‌های مختلف هم برای حضور در مراسم دعوت شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/97131" target="_blank">📅 16:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97130">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=hyjxDZqtyvgLTvHQ35PqZprWj3qK4mY42BA6MdR6p-__HEg1IqVCpI72yMQl_kTPYi8UGpnHu2JgAqE1NXY1eXyV8EVijCiLQJgUFMV3-oIMfjF21Fxgb2CI8itPbI4uHr6N5xejSEkpFsDUhikpsS3z0Rz2Dddit3mNyEIx29Y1oXxQl6pK62spFKCbRDN5deF5HaHwzANf-jLZ8QkSUxeAk5m7_iOH3YdYkQVYLu_Xsf67HRV19ZAr43gntzfTJbCzTsHZDLrBoqfXl7ZJSaIyBweqMVj707j9WM2774Kouy5MUYVZ2TcVUz9D_0lq0yXPiYL5UalELQC1oZi5uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffa3275ad1.mp4?token=hyjxDZqtyvgLTvHQ35PqZprWj3qK4mY42BA6MdR6p-__HEg1IqVCpI72yMQl_kTPYi8UGpnHu2JgAqE1NXY1eXyV8EVijCiLQJgUFMV3-oIMfjF21Fxgb2CI8itPbI4uHr6N5xejSEkpFsDUhikpsS3z0Rz2Dddit3mNyEIx29Y1oXxQl6pK62spFKCbRDN5deF5HaHwzANf-jLZ8QkSUxeAk5m7_iOH3YdYkQVYLu_Xsf67HRV19ZAr43gntzfTJbCzTsHZDLrBoqfXl7ZJSaIyBweqMVj707j9WM2774Kouy5MUYVZ2TcVUz9D_0lq0yXPiYL5UalELQC1oZi5uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😏
شادی دو‌خانم برزیلی روی سکوهای استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97130" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97129">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0faDPpaIB-WenUn28L-QmewBMzxm1lg6BuFhB1cjzv_C0On8cW45eNvqAHNs4gocJ61IwJXBuDeAS2T8jctfC2wKa268o_lvonKpGKeMuo7Ast0-SrELpoZoO5E3UnDSC_893HlbxwGHtmJF6ots4BkOVy_odwLgt4aaT-scIStasA_KBIzi_3kIJX6b9HlbcJsjkg9liEa2d1t_Vcuq9Usof6ht4ADnCq7e9-WaG7dXS_vHDXkkoIT8jFWzOlp2Ri_g0V-r7V7z4y9aImzTkpvZO3V33TQas6033OyJVBPCU-Ox3WdBvhSEGlmDM_IxRS4LIQ3B2vQHaV4-iMpzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">8 سال پیش تو چنین روزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97129" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97128">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/97128" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97128" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97127">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=F3uWugtR1kWkDj_xAtpNMRyuWBo5ywRZtwldwFoKnDlbR6wmOzAST5LJuBj7zn_VJ9bqkQbI-GT4fGD0mJy9GnPgQJd7B3YS4FyyFMBvRktyJqe_RqU6YGOtm1Av5H95_qWwIhHCLaMZghByBTWBzCBqChazZ9Lau1QuzAK9R5SZBFGZS1lcCz419durQGN_h1vZ2JzY2qftaiWv8dVJHAw5j-TGQYNvjKj57mqAH1upeiFwWC_0nwQRwB955YRTl7b7_hGfTwA2uMlZTpQivYj6Qa-NKpKQKmsp5nKr6n6MkExoafNMiBIArxXCTg3yWSYHlBEUolT68uO5ZkoaOg3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=F3uWugtR1kWkDj_xAtpNMRyuWBo5ywRZtwldwFoKnDlbR6wmOzAST5LJuBj7zn_VJ9bqkQbI-GT4fGD0mJy9GnPgQJd7B3YS4FyyFMBvRktyJqe_RqU6YGOtm1Av5H95_qWwIhHCLaMZghByBTWBzCBqChazZ9Lau1QuzAK9R5SZBFGZS1lcCz419durQGN_h1vZ2JzY2qftaiWv8dVJHAw5j-TGQYNvjKj57mqAH1upeiFwWC_0nwQRwB955YRTl7b7_hGfTwA2uMlZTpQivYj6Qa-NKpKQKmsp5nKr6n6MkExoafNMiBIArxXCTg3yWSYHlBEUolT68uO5ZkoaOg3Y-Ua_tbMktpmTzpmxvQeAWFYV_9SooEGJt-Avpq1B3O1WESnDf9LiCUdyjLuk4aUjhnrJwIjw73L7gLg983uaPcdVNzBdTA79STwk_XPiFeyUmWnHzz4gSQIz19bkDCyqMNR9k_W0O-ELTJO7w3qIxe9eNwI2_47RKuoHmkpHexpxqDWdPkFVbBM2XK0qa0qu1caprqa7lDBoOPSamycymwPv4zLfzNbwecdyKawve2CIgVwtJo0ej3SRXyhTmEQLjn6bJMKflOQmM7juvcpyUQ7bZDBiUO9It7fqQxj4eI_N1Xe9t2zhsSvXSXX10WwKNsTxJ4fuA25kQsPIah0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/97127" target="_blank">📅 16:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97126">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZhkz3FVi4QDfl-WXeosYuTy2EbpWjBJI7fnJsbf8YEWHyKncoqKq0g-yZg36LlTwZTqoPKypuEkVfdvHVxOxrkrUXL4D5E74BpGqBgGV24qKJS9Qe8aeGegIE_gI36hnN90QRx0O2GNbHKilJlFHS0tsyL4bxo_UqbVim9_Wp-YrOubPprzPaZQ15vwRt_jWdUF2AlItMoA3EUlOL2sYGhAGUproLPJFGwtY3yQTDMydSWzwfBV9dwElXd_FkQANRUXUGCuTjOARvPKihkffn3Hxuk4Y9SHqlkaWSSpkk7V24O1k1dfW7zlEsdqTWT7ihvTY6ocu-R2rmWSTuMd0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
مسیر احتمالی فرانسه در مرحله حذفی جام جهانی
:
🇸🇪
مرحله یک‌شانزدهم نهایی: سوئد (قطعی)
🇵🇾
مرحله یک‌هشتم نهایی: پاراگوئه (قطعی)
🇲🇦
یک‌چهارم نهایی: مراکش
🇵🇹
🇪🇸
نیمه نهایی: پرتغال یا اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/97126" target="_blank">📅 16:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97125">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37f012c953.mp4?token=unqhgqQvlII2BEJNhHZk3uPpvdWodrV9w2BoCGZsbekv0Kl7xMitPHk7lEN0ZbDCLAlpO4RGwKDBPL2Nxcwf7YA5MVc2bDsclE1MlSnOg79TgD3pj5vENbWDLsRmbv5i9k371cgeR0w3hYVnQH0j-a_nBSqpjg4g8th7Jkc5Xbf85WkAP6vj893-7n6ozjUcITPvNf4m7aOY6-KN4MsfdcakzgXR6m7Ggsqg_IRcpFzk0fol6c7ogn0xzKkc5azZKPw5lA7OkAXOJtktB9sBPF98jyiUm6Vr91NxlVUCOBpR1YnoNOyNnMnC_VIenGfKyMjvxesR3NNtDLKjaRjj5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37f012c953.mp4?token=unqhgqQvlII2BEJNhHZk3uPpvdWodrV9w2BoCGZsbekv0Kl7xMitPHk7lEN0ZbDCLAlpO4RGwKDBPL2Nxcwf7YA5MVc2bDsclE1MlSnOg79TgD3pj5vENbWDLsRmbv5i9k371cgeR0w3hYVnQH0j-a_nBSqpjg4g8th7Jkc5Xbf85WkAP6vj893-7n6ozjUcITPvNf4m7aOY6-KN4MsfdcakzgXR6m7Ggsqg_IRcpFzk0fol6c7ogn0xzKkc5azZKPw5lA7OkAXOJtktB9sBPF98jyiUm6Vr91NxlVUCOBpR1YnoNOyNnMnC_VIenGfKyMjvxesR3NNtDLKjaRjj5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇧🇷
مراحل آماده‌شدن همسر‌نیمار برای بازی ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/97125" target="_blank">📅 16:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97124">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVacDt5WMNMzxwcvsUWx3f5Z6s_Ivh55aAGwVnHoQxnXQAtcAPAsnUiQMbNOpiW4A1yly8N3AF0xCugdrIm0xL1k7xuowMqMnoOOy7-moiUOD1T-TCwdkfYE-IYp6_Kox1GVH3LBBj1BPDkDfhy2jHkzBE6ibFF2wNhdi97RLlm1uy5bSb3On6pSYUrj5JNhDMiZhMoim1tHQGDXKiy79XpM6ZCsTBCjzzLM_sLLMWNbIWKsEP9aXviOPjqhj67cMsC3zsQsI-0R6toxdwR0G6ESZ_L8GikSWS7rLDJXqh36Y8ldpBZtaXUT7g0n6mk5hCb4jX9OPi-csS_9IQP-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالد کومان از سرمربیگری هلند استعفا داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97124" target="_blank">📅 16:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97123">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=Ik2QOLavaFdEL6Y7UgyAt0vHIU1AbiejeZmlKRk3NbSHWmi5RCJ8UVyqiaPXqzKh32VxHhFPts-bNcC69dlm4juBWcAf-kUWXrxrhu4FXIfMToTLD1PzagbtGMXe8p9J-RhYPEUNM_7FNM_hiFQ5Cjw8UNEA520BdWXlgd8gnUlUq7RRot-o_qKhezSDZcJAd7FVvZJcitl_GpYEz4fNMQ9JD975Moc8xo_8dXJCOxf7mm4gAXVWnBGK52rbKKWKsqADQTeyYP1zOzSnCB1tCpPdmFBTqvlWLf8oaPfnJJBX4zCGgpjiDnkycT4Vq6swZNooWRTqTj4ukGmqTwdULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a9b21708c.mp4?token=Ik2QOLavaFdEL6Y7UgyAt0vHIU1AbiejeZmlKRk3NbSHWmi5RCJ8UVyqiaPXqzKh32VxHhFPts-bNcC69dlm4juBWcAf-kUWXrxrhu4FXIfMToTLD1PzagbtGMXe8p9J-RhYPEUNM_7FNM_hiFQ5Cjw8UNEA520BdWXlgd8gnUlUq7RRot-o_qKhezSDZcJAd7FVvZJcitl_GpYEz4fNMQ9JD975Moc8xo_8dXJCOxf7mm4gAXVWnBGK52rbKKWKsqADQTeyYP1zOzSnCB1tCpPdmFBTqvlWLf8oaPfnJJBX4zCGgpjiDnkycT4Vq6swZNooWRTqTj4ukGmqTwdULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مردم مشکل دارن: نه مردم فلان کشور وضعشون بدتره
❗️
جامعه توش جُرم زیاد شده: نه فلان کشور بیشتر مجرم داره
‼️
مردم شاد نیستن: نه توی این کشور مردم غمگین ترن.
❗️
اینم از فوتبال ما مینویسیم اینجور فوتبال بازی کردن قشنگ نیست بدون بی ادبی ...جوابی که میدن: فلان کشور بدتر بود. یه عده ام که متعصب الکی بدو بیراهاشو به ما میگن..
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/97123" target="_blank">📅 16:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97122">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">💥
🇧🇷
شادی‌طرفداران بنگلادشی پس از صعود دراماتیک برزیل به مرحله ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97122" target="_blank">📅 15:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97121">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=XojwCf6exu6Vs3PR7Ft31R98DDCv1zBpyXmyuEEcBxK2FGFwwAnYA7pk58mBmIU-U3Efrc_j7sDJz3mmamb0X31D0fuZyEmx_ZIebi-UrVX6AcyOrBtuB7wImyzKF-z9ZNCAtr0N5lOxzYRT79MhHMm6yR0JifnDG64mPQb-2tcZbkVApDVga9nuhD9Y0TCvGvmuWK1BBN68IaAGaWKj3Z5F0W2NopEthiR9WXWWI3dyik8fOVdwF0_dA4Q-e0hFwP8TW3k2ZZ1lmXsszHm0l9nCP7s-T3w0DCiWZPQy6W2n-69sEytARN6yOw3-Nd1AvB1SRWIZIzBYnHEp39u9Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa918da02.mp4?token=XojwCf6exu6Vs3PR7Ft31R98DDCv1zBpyXmyuEEcBxK2FGFwwAnYA7pk58mBmIU-U3Efrc_j7sDJz3mmamb0X31D0fuZyEmx_ZIebi-UrVX6AcyOrBtuB7wImyzKF-z9ZNCAtr0N5lOxzYRT79MhHMm6yR0JifnDG64mPQb-2tcZbkVApDVga9nuhD9Y0TCvGvmuWK1BBN68IaAGaWKj3Z5F0W2NopEthiR9WXWWI3dyik8fOVdwF0_dA4Q-e0hFwP8TW3k2ZZ1lmXsszHm0l9nCP7s-T3w0DCiWZPQy6W2n-69sEytARN6yOw3-Nd1AvB1SRWIZIzBYnHEp39u9Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
❗️
اقدام جالب نیمار در بازی دیشب بعد از ورود یک خانم جیمی‌جامپ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/97121" target="_blank">📅 15:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97120">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a4sGGoTLFEzdvltjZ8zWj8c_S6R5aWbUpwS9-vB_l9RXCKuuWcN0RGNA5wWTm79aTilkM0BRB5mejuLHOBr8tzUY2BVIGh3vo5LzM_JcdD5a-txhEdgXp6upJDNZqUN7KwfPnDfaS8_sGQq8VqBCzwsJMj-c46Mwn8WlECc-Y3HW8XzcYqgOap6l2XuYDK9Ue-vEuCP9ob9tcm505MVEhXXbKWnyt7PLfgGrNvY0xOSgyqMmVtHSB882pm-vuok5RpIMMklJ3DHQJoGVTDwL77HDuS1ZzkS73_5OPHRm90etW8lE-wTW6g2XL-bLE0YoxdVr38410oN_1VuAHO4ZQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🗞
#فوووووری
- کوپه:
😂
فرلان مندی پس از اینکه یکی از سگ‌هایش یک پسر ۱۷ ساله را گاز گرفت و به دو سگ دیگر حمله کرد، به دادگاه احضار شده است
❗️
دادستانی خواستار محکومیت مندی به شش ماه زندان، جریمه و غرامتی تا ۲۲۵۰۰ یورو بابت آسیب‌های جسمی و روانی و دوره درمان است!
🚨
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/97120" target="_blank">📅 15:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97119">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnbpVjb3HRZBDKDYJ2oZdTjQxYxfAAVfoS_xDzbvRRNQef9ZaSiMWLtHJc2KBM9BiP3kHaxEjjRKBYcSq_Sh4dlAHaXHEARIrWFgORgVkMqN-1blm8IvX-pv-rX69xAR0rw37XxIUmGhJ5qqlYTqgIZ7JmnIlLS9fETVD04MYCcbOx8L3HACCf2esIfvDdPogwDkMSLD-QFsQzEpUWIPJN8zIBdcZgMxqdqyjrjZRTrSev5ASkclIQRsfChIj5AWc7giQXEvWgjIWAFoKCqXA6_hHMiJmbhOcJoNi1qN4VRtxKfSw8oaH-rf_Hdy3S_tb_zCALZSV6Y66F1VTu65Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
حواشی‌جذاب مسابقات انگلیس در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97119" target="_blank">📅 15:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97118">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=p2QcimXWHxMjwFe_kGSVGmH3vh3hjK68QHV20mhZugyoiiprjOlO7D7e5Ph1nZu-g_AmSCcYTawYTtFt3Fd5xcC_uKvO3lJRsKSZQ7c9rILNtgDC4GNC1Hb63CB-68wUTMPPPaAlgBP3SEcRUfxEzvKzLgx0BhFATls7oMfBNAz-10Y3hE_U--idDk5Rxg6gSbobY0o00gZdT6zk8XRJ4bso6-vs5ZOTElWt7l-Wcgj5hMGoMV52W3yqia2mOMX2C_HvL6sHykK3IgKsUoRIpb8yp0SDUOyGX1z2qd_fsiV4e44qKJkNk6xRFoYIcJrYtqj4Rt_QLyh7pXkw1LCbaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96ccfc4b2a.mp4?token=p2QcimXWHxMjwFe_kGSVGmH3vh3hjK68QHV20mhZugyoiiprjOlO7D7e5Ph1nZu-g_AmSCcYTawYTtFt3Fd5xcC_uKvO3lJRsKSZQ7c9rILNtgDC4GNC1Hb63CB-68wUTMPPPaAlgBP3SEcRUfxEzvKzLgx0BhFATls7oMfBNAz-10Y3hE_U--idDk5Rxg6gSbobY0o00gZdT6zk8XRJ4bso6-vs5ZOTElWt7l-Wcgj5hMGoMV52W3yqia2mOMX2C_HvL6sHykK3IgKsUoRIpb8yp0SDUOyGX1z2qd_fsiV4e44qKJkNk6xRFoYIcJrYtqj4Rt_QLyh7pXkw1LCbaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
طرز برخورد صحیح ماموران امنیتی استادیوم های آمریکا با هواداران بی‌انضباط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97118" target="_blank">📅 14:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97117">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=Pokq_4cIdnWfEmfIGlSfGbLG1utTSHdNzOz58pPF43rSZCzR0-j0vEju_j64iREEdNcyADK5pikEES-DOBH9KoyhzpYLQKUxOCh9phWxE2qCXud1abCR-T0PH_-f9C_iPKpuHbz_HyfO1c2uzPUyo6dlI7ElczkkOmxLdbjC23xqqlpxySebTZnDxQ5TUlRkLnCDbxmwBxaqA75pUIRrpPnTKrMuMOBk4p7D4uY-5_nRG7jUnv2Ft-8AqxciMgI8Nd1GjF1VAKaGQsy2VjOUAbIKny3fq9gdqhw1VCP61Qs5nX3ktshh3tR6dQR8Lx8zHr8FNr2v1r2brno5B4TtyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d804cfa856.mp4?token=Pokq_4cIdnWfEmfIGlSfGbLG1utTSHdNzOz58pPF43rSZCzR0-j0vEju_j64iREEdNcyADK5pikEES-DOBH9KoyhzpYLQKUxOCh9phWxE2qCXud1abCR-T0PH_-f9C_iPKpuHbz_HyfO1c2uzPUyo6dlI7ElczkkOmxLdbjC23xqqlpxySebTZnDxQ5TUlRkLnCDbxmwBxaqA75pUIRrpPnTKrMuMOBk4p7D4uY-5_nRG7jUnv2Ft-8AqxciMgI8Nd1GjF1VAKaGQsy2VjOUAbIKny3fq9gdqhw1VCP61Qs5nX3ktshh3tR6dQR8Lx8zHr8FNr2v1r2brno5B4TtyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇯🇵
انیمیشن حمید‌سحری از بازی ژاپن و برزیل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97117" target="_blank">📅 14:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97116">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJKOVZUY-pUgsJRmqGQev-pYY0itSQIB0ag0E_WNKThK7A50Zqe0xRZCHzyasj0-QNXyIxLB9x6O87v-v5KqWEQjIgJblwqJN4015K0OwKb2sww2aROG6UZCGJ1BTlvBn9KJS_6LcqIWkoCkqF_3i1Ae4hTHzB7P4Ag_aYWbMtW6LDOaSKvEArHHCg0Ru5j6dMMZkUhbgWplFF5Q7awNA83hRXH8Kb15m_6QoL2CwEP9y9vG1I_FhR6ebgLgZ_tBl7v0Zd8Bu8Ge6pUoOL_wXI1ydp1tiiNSd-yPtUFV8mzbyVVy1Kdtx3cl7SaCD_IKPOGJMHRzSu3AuUq34H69mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کوکوریا :
ترجیح میدم کچل بشم تا یه تتو از لوگوی بارسلونا داشته باشم، من حاضرم برای وینی و امباپه فداکاری کنم تا همه چی رو برنده شیم، تمام کارهای کثیف داخل زمین رو انجام میدم و فقط هدفم اینه به پیروزی برسیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97116" target="_blank">📅 14:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97115">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=nWoj62XGprtp0z5wzuT-VJxNa8z0746453ALtDZQei0AlfRpUuYh8k4zcdy2gWKh9mjqpHL6WqPDhDl-0CmKIHlYdmKFDfy9rU2GBiXbvyoeYel6NP7KGjIRU0mvDoDg175Y_MPrn2G8Tc2AILarYgMQi_WFWvFgJQ-gHZfx3DSkJocFVGE-t69ppV-XFk2WsTebiH3T1hmzC9jFs9WBMnqNBtjsycnKO82KmwXsF56vN6ZXeNgBr-EnhFGpVQKifeucG6F8dhewGnSUfOGir1s3nQl44v77V2opNcAISJDF-KY7F0ogD4iwOkqDDDugL_eC18PYq4ISxD73ILolQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3a0c56dab.mp4?token=nWoj62XGprtp0z5wzuT-VJxNa8z0746453ALtDZQei0AlfRpUuYh8k4zcdy2gWKh9mjqpHL6WqPDhDl-0CmKIHlYdmKFDfy9rU2GBiXbvyoeYel6NP7KGjIRU0mvDoDg175Y_MPrn2G8Tc2AILarYgMQi_WFWvFgJQ-gHZfx3DSkJocFVGE-t69ppV-XFk2WsTebiH3T1hmzC9jFs9WBMnqNBtjsycnKO82KmwXsF56vN6ZXeNgBr-EnhFGpVQKifeucG6F8dhewGnSUfOGir1s3nQl44v77V2opNcAISJDF-KY7F0ogD4iwOkqDDDugL_eC18PYq4ISxD73ILolQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوشحالی شدید میثاقی از حذف تیم‌ملی ژاپن از جام‌جهانی؛ چشم دیدن پیشرفت فوتبال کشورهای دیگه رو ندارن تا به مردم اینجوری نشون بدن که تیم قلعه‌نویی عالی بوده
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97115" target="_blank">📅 14:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97114">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=G9yXknsW1vR-e5WaI0ncl5HZHJ8jS1fx4uvVQV21tYieJIDVIIpT2VlGGs4aOjXXnOHCmcfQuobYaX98so4X-PSv1eLWgnY7fkLHfNiXbZ7mS19HyhzzgQjn4duynkTpVbzE_2ILB-h8DCh7qK-Gypq6z_lfcxwp92L6DEbRwFlXYJCWXroWyaxCQJeX0FQsvEANasnpO1rAn4hFfFJpp4h-x-lP4ULju2vGXmmgRG4ZR8bLEyTdCpA2Q7we1hY9imegMVFWABAcD3PjNe-rrF6rfDXuOUr87jOkvc-zK7tj-9uhmKBZBRBgKI3t65ElCByRXbVYUWxJSiWKg-xqZYGAj4Wbq5H7LyLFpjQvfLQPrdtjyPh8TeAcvDKfhg4l6_kqRpWW2PtBs0JeQFxVJ0elWq2_lCLRK7XThN6-z3rTg9-KLjtbEiu5Q1cNEzTInAfRopl-NR-MpWge-69J3kgVTpFGipofiRp9K-qVVbO1135PRgxgMutoA1rgA5U-R7mHywQ4Z3PTAF8vvND2QAsZDJ5ntwMslEoOtWtuAcek3FVf1NDKTUp6mGAJiQk6d8gJ1a2uCRMde09kqbVK5eivP0iH6Ril8hkncfxceQ7RH2WtOAKlwW4jAps0QZs_7tpBK8cNH-72akQ5O5NisVTovb0Xe5Ckc8hyj0YTjPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53f3cc7f42.mp4?token=G9yXknsW1vR-e5WaI0ncl5HZHJ8jS1fx4uvVQV21tYieJIDVIIpT2VlGGs4aOjXXnOHCmcfQuobYaX98so4X-PSv1eLWgnY7fkLHfNiXbZ7mS19HyhzzgQjn4duynkTpVbzE_2ILB-h8DCh7qK-Gypq6z_lfcxwp92L6DEbRwFlXYJCWXroWyaxCQJeX0FQsvEANasnpO1rAn4hFfFJpp4h-x-lP4ULju2vGXmmgRG4ZR8bLEyTdCpA2Q7we1hY9imegMVFWABAcD3PjNe-rrF6rfDXuOUr87jOkvc-zK7tj-9uhmKBZBRBgKI3t65ElCByRXbVYUWxJSiWKg-xqZYGAj4Wbq5H7LyLFpjQvfLQPrdtjyPh8TeAcvDKfhg4l6_kqRpWW2PtBs0JeQFxVJ0elWq2_lCLRK7XThN6-z3rTg9-KLjtbEiu5Q1cNEzTInAfRopl-NR-MpWge-69J3kgVTpFGipofiRp9K-qVVbO1135PRgxgMutoA1rgA5U-R7mHywQ4Z3PTAF8vvND2QAsZDJ5ntwMslEoOtWtuAcek3FVf1NDKTUp6mGAJiQk6d8gJ1a2uCRMde09kqbVK5eivP0iH6Ril8hkncfxceQ7RH2WtOAKlwW4jAps0QZs_7tpBK8cNH-72akQ5O5NisVTovb0Xe5Ckc8hyj0YTjPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇩🇪
آقای‌ناگلزمن خدا ازت نگذره که دختران سرزمین ایران رو اینجوری ناراحت کردی
😔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97114" target="_blank">📅 13:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97113">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ef2e2b2ce.mp4?token=bI_jrMv4c-7MiV5X1Hv8sRqIv4Kn-bBcJ29h2iGw25QguvFrHQqSNhdxyO8GM_a1zILEjHWLRhdkhIR6X7sDToAxklm0KJgyuGICS_nz_uuTR9j5Ht975sdF8mocuyJaFBA6gEEEOsFLg7W9hlzgAAsfQFhDyRV_9lbt7ki17_f6EXIm3fkri0Dr3rZjXu0TZqcEsjrpssat9J82ObJ04d3PyswjIuwR5Rt-DqJJcMwSPR8p2cbGPFk9ICZUMyOhQIXKOJN4D39D1WDz71W1tUgdBimMyEA9lpdJswTicSscYjt9SiASorOiuTR2Pr8_JetUCXphR_XA44lQGmI5eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
🌏
پست‌سمی پیج‌چادرملو بعد کسب سهمیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/97113" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97112">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_2MgLXZOh5kfxPkHGWi4GhtWw-f30Sp-RLBQDzM2rTC_DBTB8UAjGShm5M5KT5zsRoYDm2VPKErVRkC7-I37_wpv4Z0KdnvKbw5RJDchoI04oGW90V6SAruQMKDGkGIGf0fj8Fj_TAiu94XHeyOQ-_zcgT6yU4IZYlcA1PRjdI0AOi8DREliyfH-tYxKJsowcNS5mYnVfmLO4teiDdQxj5XGkL5LU83Un0-hAQPbdU7MaaFNghpyawzT4eHX4DXUyXbQ1nFCv4YnaQJHHtAsqd9Cv7wg4ZdmW41xviVcT8_psHwrESMjv5lJXSP5w9jmriQtSPUJl5ze-xyaNN0sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
#فوووووری
از رومانو: قرارداد کاسمیرو با اینتر میامی سه‌ساله هست و بزودی رسمی میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97112" target="_blank">📅 13:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97111">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGVufUpOoH5LMNlbpHdI6N2f644l4FnnnJzCFNXUCps-UxUnkKVX2Am6fEFtXAWpyc5qqfI2CJTvxbSxo92ayG07ZVTziaB09fXZCWwVY31JkXgoKRBwKhqj2MLjr9-24jcFfRNEgTXokMmhb9O8BtvxHtQ6W9b8spgcTeAiBtiOs1IvQfqyM9jZ_sBEjiooMoabY3ev_ZbdJpDT30HhtJVjBfFSWR3_2ycgmRBS86Qkv9J3YYTpK8zmxDiHwVM_RG7R30qFv3wrFXnUtJtW7vAIsgPATy-EQoc9pJaykPV2oCVnAcK5oE13LI9GBzC343G63KubVDRaOk3GnooZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متئو دارمیان هم از اینتر جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/97111" target="_blank">📅 13:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IW6T4wLM9IMQ8Sc6KfelUjRkblGuMVSwI0dP3p2bvkqIAFBhEAgkB0Rf1hLRHK3-tNHXmVWG9wRwxCv2kjg-HK_wU36RYSeMdw_AaHyPh5RDUBMCP76GH_UlTef-1g9MJ4h6jfJD2pB-tPd3MYWUOOoOzScDRxeyhDNNeikqKRQqGdUoBGODuSeA1iOkCOth24uwneepvrkRm1X749oTqbgf-tMqn9uWR5wPk-_ywaa5DGM6T8TMf1XZwbSjeGoL1_T70MGWvmM3JwdS2fpemQRBeX9rSR7GrYPZ5vUx1z2Fi_OdZ9rEXYuiRHv0jnpTshh4zavjHQKYUkfX_UpRzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XeiCGQLTFO6YebwEM0k2ml9EmLvCebj6xOoyZEfp5XuLAUd1JN66g7oCmU8Km2YlAyAekdCqzKFc3az2AjTHSqKqbpQzPEX5GFBTODO1H-fN3OdHmkA_YtSvGQE7nc3Xh9ssdcJKVa1P8io58Dj4pvSzOzfZGAt-FDoKzmqzOHtvcWj6c2PDrZmllXhShM6BkC2Pcw7NSR-Sxt2psSniyg0ZBPLXRs3EQFR603NoP7SlVP08Tr-84Pr0M6KRa_OmWwfwj8tOM7SmtaM2kXMWBNNrPe6sbaTW7S61WmLsIopHgtKpnZNIocfmBgoyzpPobeWrpnDmudCGZqT3RwKcWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rceCIGijiept6VJ1SBtwBdepUFGJHB3ovv73qSNV3xZonkQgWCjcYWvVlueGgfFY3BrUUi-QWg1vZc0UtMFzy3qV0-_WTHPEpEpKJHU-2InPdehtkLRgLjmTgxj_caI-Nikg1QTE1YK-3D72FqL0oIvul6sk3CiYDbJTz1c342_qlZE3AP76W3Fkp8X68wO6PkiixmiF_iTZMS21KD_yX3wTuE7Zu_yGFzSVl5EdzKF8SMcdm4xWkEPPEi2o3iVU_weaC09NvBQvVYp2raHty-5kPAly0XYqRWWtCdlY2J779-2_BTDEKLUIxjx_6GLh7lPOkd1eaxd-n13g1okLBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdTClanJLKeyJr7Yd0uG706M9JaB_g_KbvyVqiRPcQGMJYorLJ0Wc5-dLp2WIZHpAIFF61xITDhERTSmYzzop2THx35nJosTMghNs2E-crkOIhDKu6JScQOdifWLfLDpgmHI2aBMJB10XJ2XdhKQy5gbxY0aZRGYsOcsNI-9mOk6IVxQgY0YrY9ILBg21dRNCIl6upbiKFV7RW_G2c28dXxF3rfjYkQZrT4p9aF6UZhf2ANT2V7JuR0ueBpoR1SPputa1uxss7ETqGLR5YYbvKuOD9x1V9lB04Z1MAMBI77s8pIvw7kTkQCMkavIZlrPm5r_YF2vkHA8946YJVvk3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
تصاویر جدید اللهیار صیادمنش و همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97107" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97103">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K06_zGipt46nSPuCWO0r-KquJ8HhZeKeD66sMZxYiYnsw2K3_6TCWGOFEj_IbwzwNeHyCiVhUI5d6qtJgjrcQ00lNCyN7AcOmolPICWyMFV3SNAejkt4r-AIwQKQHccvCyEvejcwQq1K_gZWDc5he-MB4gb5f4L0DLDWXkcxQzHWoxfo20sVU-N_3TzbFXRGfVuPVasCXU8W_N_MfakMwsKC8EoSnTE1iSP13VX_p5yppS5i5edjGc5FR3uJNTuVmGo-P5i0VyItufjt-ZRrw_TEOu44h6mDNAhZc5qrgNJ1DwUus9R9yzbfIk8Wx4cQGzUUmgt4h15daCSmRg90MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puFsiGDWkWybREdcy96SBqAaHhRSLvBCfHIDCRhLVqlWYPW5govauAeu7h9Z91vgPJReTUTr4jcaoOlBfGuuXuNviht4vWmMA5YldjUEadu2AUtRqGYsC60Xnixn4lGp0Lca9xOgy0NaETGEBgQW1NJFFWlgbytc0qVEO7-79yuPJbaf0pQg3TdmfIo9J-28pCXF-3NlYgDT6W5w_ZzX4ik-wyry7NsVpZRjBi14i8R1iXqGrPZ-1DZLl9cH26WuB6BNHZlVezYReeb1BHnPtVO1etor7M33i-D22oOOi4vb2vU7jr-FEa0eyoUVSsRBww_Mc5PQVDTEQsr8CsxGNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qCZcHAoy-9wC3EQQi9zMb-4SIpD5befDbT0qxvpowF9LjRdUt1Gob5r1owQOm_VKH47e6TgwNZe-wTRkaiNjsRfalszAcAwCmoATBHZUX5gUBrxnGjQ9jOXUh7Xo-zBHjbxgmFWfxxnKqfEy8AFuQ95NfEltKB8aPNBc7LaCZfhS5iEdovWU_jd155fcRG4QqzWX5h-LpxJti4f5iJg3WYEEnFK8bpkN02vxMeqIWX57nk4LYRcvwiBT-VinHUm-DpEGbnJVuWnN_Iksu8ewzq7FGF1cSMoq5ROK8K0T3Vn5MBPjczJE03D8dNzwmtmHmz2tICxdST9yMaGxrGsbgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qze_jRWZ6NUWE-HLFAQyQPlS9zG13X0XCZaoMjBHzNlRkia4McGG49ZjfpKGjnViTQJblkF7kLy3dxG9NEWM5q-B-mJfk7TGpCRx5UBaIok8G_WzlL1j0RQkds7S_WBPqSLejODImgVP3kM2yjQyFS15AX-ELJJLUJllULo816OmbDvQRWc87qEnWv1tYaAAafX3sa9B9z9oxwKuuMqKzcHU5o730QbCACw7lPhThAuqRO7Mb4NbHkGTOyelQr4nhoqTaKMuRNAyvWW_nGUnidKudNdRYqPV4lbvZKfBp-HKtBl6Z3nqg9_2q-_50rMV_RmzsxRH6xTobCrl2b2Kig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
هوادار پرتغالی در بازی اخیر با کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/97103" target="_blank">📅 13:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97102">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSrAuO-KRfs-IjtZi6ZsAmXxzroseFsJ1e_aIV5YyqJIHojZtWN-vpFu9pN7yMPAQ9nonjtjEYtY2yeWLDYB80IiNrsr12EUxtNgklxjOEgkd8kU5rO3HRQ1sWD1PE4Y1VbVaqWUSshfIH8dwxgxmpDRUs0KSSno9h8CsrkzsbiVvBAOObrikKQBOhI7njDRuKccJ3hm2MtOx6ZCtTeizG3eUNlkc968Eu9RxojmCSO9eKptvcgwh5_N42X19PwSl4a_QqGEeyi7lQj8iqA-WtII3P1SKb09XEwxcxIUGOZ-TK1Q_aZ9Lj7HN13hkA5AyP9hngxS0Dd2D3qRMo2Mpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
باشگاه اینتر اعلام کرد که آچربی مدافع این تیم و کابوس بارسایی‌ها از تیمشان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97102" target="_blank">📅 12:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97101">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=felZ8-_fehw3PV4i9vfaqOdTvC4WAGoL_yFFu41IOt2KO6Mt_7bs6NpojcTmYk71zP1lZr2NmSxo-2KIX106-0LKIkx8rQIA9yzSRubBX1-cGFKfgIuqH_n7DFvy2UhP0ste_jQL3mjCBdBWc_FBFz6gbUn7NWe08wUGR0wwwRgwtvsSlLFVfPSJwDi0MZRTzn4jun7fHxHD-Ta89-0VNqo-Coy-GL7Zy1W8WDGXfWDX7jd2Svxem9WkCz1YuIXOp_qxWro8uvOjqTY-vWHovKqiAOTSD_PUTblLErhLCXy2AncAXZR4sdMGokLVWgWDoqLx_2j6zsJZxrWQK5PIsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b3d094a9.mp4?token=felZ8-_fehw3PV4i9vfaqOdTvC4WAGoL_yFFu41IOt2KO6Mt_7bs6NpojcTmYk71zP1lZr2NmSxo-2KIX106-0LKIkx8rQIA9yzSRubBX1-cGFKfgIuqH_n7DFvy2UhP0ste_jQL3mjCBdBWc_FBFz6gbUn7NWe08wUGR0wwwRgwtvsSlLFVfPSJwDi0MZRTzn4jun7fHxHD-Ta89-0VNqo-Coy-GL7Zy1W8WDGXfWDX7jd2Svxem9WkCz1YuIXOp_qxWro8uvOjqTY-vWHovKqiAOTSD_PUTblLErhLCXy2AncAXZR4sdMGokLVWgWDoqLx_2j6zsJZxrWQK5PIsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
وقتی شجاع خلیل‌زاده سوژه ابوطالب شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97101" target="_blank">📅 12:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97100">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g0wY8auWo9b6o6LUEhXaMIBay0MfEmL3XFEYMwtnL4w_-iy1hG3xthbnNaHAFQ1WVAFObnMy07uCQmK09CGWavMTr91l4GIVGpBVG5bE5mMYcMb_Z1Cci_H_fx27z6bCtWO4NxQeeiV6JX2BQu68WSw-8OlgdrhhVu49NpQ0PjBOdXcDvRNb3Jo9jAyv1PVg06hKaRwlWzTn2ML5XoToTJq15RHJgTq7__6zJsVzhg9wnLxKxVYsLfJuFXtLdJFM1O1RCVnbfxv2GsbUIsMOiUu4B-5f1GmJmKrmSyTp3PxCz8GeuDt7ihEDEQ2eODy35pkBedQiGBKVJHK6Rw3fEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🗓
🏆
در چنین روزی ۲۴ سال پیش، برزیل برای پنجمین بار تاج پادشاهی جهان را بر سر گذاشت و فصل جدیدی از افتخارات سامبا رقم خورد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97100" target="_blank">📅 12:28 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97099">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197441ec59.mp4?token=TnbwpCps-YowXT7zNYFyDzTpHktNh6rO_BIqGind6_pEbnJJaTfydyOWQEOWvZETqBLEryXsn5ynsmFIUAIZSx6x5ku_TAOy2ZV3WzL1L8Q6qFpXogugwfJ7upqzTjbp0N8nFYAQnEqxHPTsZ6DDj-r_ohEQy6V5MUxadV1PnAnp4YXl3lyTWpqLuIcxravam2hsUlR21bRLRNOVvOW8FVsMn_dxUHGKluxve19YWdBXKofzSltXEia1LhfwL2C3Gh0il53MiXh6zooYJA6lWkTWcJWkEU9fBe90L3_CmRyurn_TVOvExa5ptaAd5ZZ7RzO0N-HkEZcqsTZGssvFnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197441ec59.mp4?token=TnbwpCps-YowXT7zNYFyDzTpHktNh6rO_BIqGind6_pEbnJJaTfydyOWQEOWvZETqBLEryXsn5ynsmFIUAIZSx6x5ku_TAOy2ZV3WzL1L8Q6qFpXogugwfJ7upqzTjbp0N8nFYAQnEqxHPTsZ6DDj-r_ohEQy6V5MUxadV1PnAnp4YXl3lyTWpqLuIcxravam2hsUlR21bRLRNOVvOW8FVsMn_dxUHGKluxve19YWdBXKofzSltXEia1LhfwL2C3Gh0il53MiXh6zooYJA6lWkTWcJWkEU9fBe90L3_CmRyurn_TVOvExa5ptaAd5ZZ7RzO0N-HkEZcqsTZGssvFnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
💥
شادی هواداران ایرانی طرفدار برزیل از صعود به مرحله یک‌هشتم نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/97099" target="_blank">📅 12:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97098">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c36135326.mp4?token=RASWHjScyH1Snw-DfwvM0HLLfqZs43cT4ITnAG90opX_V0v-mNIo5LoSwNiCHaA4rgobUjGBbFepjC8qmCe14-FUfzy4geyAtqwDR5X8ykfhRiEJj70S3PT80s-SnkYLMqIC0PeMcdsm7gFBmUgNuRgLTYAMHwzk9EBg0DYj-OwYXu-mD2fDC8ygsycn3Fyh4M9YLQBMPVEl8MFoegAOMnfdS0Sk2uNHrD5DGREwgAiAfiRAAnoiraMDlyvB8hlLhsS54u7WGxzFDnHyhkK6ARlA2wGTcYYX76jINy1GugUEk7AfQG9mGWb0IY_M2CAX4aK6SEnJ_LfxTeeu_mfGNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c36135326.mp4?token=RASWHjScyH1Snw-DfwvM0HLLfqZs43cT4ITnAG90opX_V0v-mNIo5LoSwNiCHaA4rgobUjGBbFepjC8qmCe14-FUfzy4geyAtqwDR5X8ykfhRiEJj70S3PT80s-SnkYLMqIC0PeMcdsm7gFBmUgNuRgLTYAMHwzk9EBg0DYj-OwYXu-mD2fDC8ygsycn3Fyh4M9YLQBMPVEl8MFoegAOMnfdS0Sk2uNHrD5DGREwgAiAfiRAAnoiraMDlyvB8hlLhsS54u7WGxzFDnHyhkK6ARlA2wGTcYYX76jINy1GugUEk7AfQG9mGWb0IY_M2CAX4aK6SEnJ_LfxTeeu_mfGNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
کسخل ‌بازی هوادار ژاپنی تو بازی دیشب
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97098" target="_blank">📅 12:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97097">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IwYejcf7RyEEQw3Mes6KhiERCitueXiKMYiqgIIATi9GJzlzmrdTqLbMvHWqFTmfBu8bSQaZGofoAML7S46IeVFG4mvw4G5Q-C25dikpGMSGypONyghSQB8BvkY5flIQqnarzZAQvIBp22q0iAOq-NDoGfgOd73qK2AmcDVahSAVE6l_H3olIjNsFjybYXvf3-DT8iG13RyTM3j4PBKFjowaKNd-edbT9Ch64w5JkYOv-agSWtztSniadB27kHji7tsLTpqKSWHsac4K5oF6DzsVAr2AFbaN5V3IxZHKmynYvvRv8xENRFkkOt1zNjcxwEoeTGmAr4eg9ElMOzFCQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/97097" target="_blank">📅 12:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97096">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRf-SWBTGZYVRF91r0mQkHJjoKbxgblHYRQO27R8mcAeo90rPveKuDdIWaITADJq_ZP1CYwuhCSAWqCNbVYFnH8mLARMoGVyGJwz0pAwAhLxgiUuEg5u8x1wp-b2RZ035PP4WaWq8su4a5ZRQgvCyzlsMAtTmcS7_c0y453zTgxi00bPfumXl95FVFMhj70TXz7eI6VoiYkMKht-OZhZDJQAEN985OGVys3ISKPTIxlSPHORpYgZSKCuS9tYHpeY9jdzfeZEJFIxgy629-ZH2iRYmEO5h1x5JYrW_sUt9X1GNI_FjZt8YAVKzbMNylzwnN2xEnGcz6ZqflU5tImw8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
🇳🇱
رونالد کومان سرمربی هلند درباره ضربات پنالتی دیدار با مراکش
:
"
من سعی می‌کردم تیم را بر اساس تفکر درباره اینکه چه کسی می‌تواند پنالتی بزند تغییر دهم. دی یونگ را از دست دادم، خاکپو را از دست دادم و سپس سعی کردم بازیکنان واجد شرایط را قرار دهم. موفق نشدند، به من چه ربطی دارد و چه کار میتوانم انجام دهم؟"
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/97096" target="_blank">📅 12:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97093">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NtgrFbbn_0ZrLEwX0Q8y_v2SHN6RnL7kLImawKFzoExPIa7WXq_alP3RfCCLMHPS9Y2jdqC-DRsMS7wchV9y8aLsi4hJJZ0GqsHStx3kkEEr6p-lvGVh55kMOPZlc4sxuxXsqMfWKocxYHJrhKZUxKJHbbDgpwaaMPyrYHljEv5M33LuHjKOrf9-62g6_9l10XQRiO83aGFJgLP2wSQs96lQ78CrnaEcnYbXIJjA-MJrgU5-ou1d2A6i8rRqT79AWVNNUtI-0-JYWhVa9RNRO8ZkLZudLnVLGbnpYxq0mA_STUbNKMIkCP0xxm_qO6gjx1N_YZtbiDoHYC8cLqC6oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jhUX9VpuFfHjl6wDHHgxuyVxDlyx5-QxEsg9ywpQklzOQvG1q5V0-7qRq3PoQYxf-VS-jX_k-vq6wlAZh0ZVkKpXSQdvFfsx-nMrXG345cBCypy0Cv5oceH0HDoNM0tP21G7oaP6O94HFKmWCNfGpOSb0ZnVMPezqd02JUDV1-yzeGzeMfarl-4ps3-PJgzW5cEmkw2NDdaEymlAcVzzflH3W0RFK8sYz-yMtUvscOzl271qAx1MSDxH6uid8DzD6ZBinHvqibV3n-y8L41BcJs8spWTgP9zM94wzG5sXYeUkQE5iqVUo5ZGv22RiesJ_PxcfLU2p2oy9War7274pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DT6p5ENwZCYtwm2XEKIYspmadH2p_KIyaEzTprZ7DJJLl9idU4kJ57ivLskpwAn0yp2BAIj5XDk5xuEdBJo7a450r2UPr0PVkudBBZZ1PObnerzj9h0sHKwFdvI3BVmGlCuhgjz-eL7VJk4tO0ZuOfF3VmOTEqgCzu8w4UTDjQygvtS05pI0ETHYsyAGzOsN4vDQQFOoPi-e-HqeZn_z684xdBjWvgfPGhyw44_yjuOhtUjFF_yAECnwRHzCLQywhIi5tRP-7tvf2czTnW0MZD9PCQ7ncU45FTP9Dq2kkJs-p-NoTt-eq4TpszLx9Q53VJ9GkRUk0I6_sFB40hDEPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇷
همسر اندریک در بازی دیشب با ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/97093" target="_blank">📅 11:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97092">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">▶️
🤩
حس‌‌وحال دیدنی رختکن تیم‌فوتبال چادرملو اردکان بعد از صعود به آسیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/97092" target="_blank">📅 11:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97091">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vpaiq1GHRN-irFRQ9Dg15DIZVDqmi-eFOtRQQHX63ANv4f26HX8y6O1xHQnEu1ClKw3wJf9VtmcVLN3rk0NYR9RHWslF9-eZvIid2KEBTX6CS8fDgXbsMqYOmRbNd5B5r5W26_sxOxCa8aXKYpJHWdopQcX1JVEeJyxgGhIKlcWu2vbJRODIA5e0KOgfGbsBQdSJJDdk0TPdZm36YjigSD_A2Z-rO2CO9mVRB3DMOym4RK2SJRihzrbr3kWO6tZ2LUDz3fzGhwoKYlahSdCMW91h60IfEkX11TUrsja1LkmWJ8DyIcayx4LXzQpZcwHkQlAQYWuQyw9M9fENPLkGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اینترمیلان از جدایی یان سومر دروازه بان خود از این تیم خبر داد.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97091" target="_blank">📅 11:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97086">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-mWJmt4zyfEasJ3FdGSMVfqLFI9Dspw2pYORJZLiC-a7MHAiqv50AN3N9-ckN6E8MuIzset78xDeX7XdVYEx9vIKuTizeUZ9sNVxUUv6h8yvlrpQO9iuVow0E-TrCRIdIBZaFe5R1aQDveR-PEGN0B2h94KeOdqQavEfT4dmVMIhfY7pO0fTlpDLBdMz9xpR1zLkXF9gKG6MlvYNYAwiC07HJ00MmTAsThXFap1Gj5Cg1_MqFObeO4yn8dIkfOWlK9VJFBdZqM6OHNZHv_iDVOgHmTPDhoXaaBREU3OtDsaa4IcTlDzN_-4BWwSKtKT9YonU7O11B7Jj72A5FeZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mgyIcOziKaC7CjCnEwWM1PYWdrUS90Eon9CSYSYN9HhJapPxWYFnlB92nm8r0NmybjAp7_Z1l8pHcJnpMWfhpRShK2-cBDW9YBuOBezQthsNrbxXcQ69kG4F5omp7CW-k4HaQWsdpYpbLVqCRk1SoWyy08HzJBQsQMkm3-xidaF-1IEg1rifMQ2lDSQhpR-uTK6u9df1_JhG8uR0X-cVy2ZTDpEfA85t0EV-PU83jFl8FEYROSQ0ZB9YJACLQmd_X2qKpfvD1d-njChn38NdZk8u5GVLb9m0s_9NlLLZviRXcOshsTA73InsddE9XIN8iKmivOi6wZRhhUGe4I3rjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pe9U_M2QhQxQCOhiylykmffUChiY7g2CqVoo9FDgTs8_2XctDYSp0Bn_i4nn4iqqZn75Mzw1i--AjmoSBa27djuMY-qnBTDwGHfAxwnYLh96Hb--NiAsX0HQdIYeVZrC66oAHekvF-8szJAVdZToY6oOGTCeBEHRtjPjKfRLtakyoLotUd1e3yKoiAcUPw0F8rDOC6A-uFMZ4rZ4j37TLRuFZytUfU1TJcg6Eb9tybfIMV8otn8UWoupnI1c0F7qivm34cKaybJ6XjVzkG0FnYZDFRAxR8-NYattaBsVcmREGVRpJbqI0fg5a2czoxFeVlCU2MUtmJpBRptBE0i45g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAeGYeJC13Z6E9iWrqI9u0JBC6APQ2U8PcG6ta5pbhRhyqRboY1fzKe_trQB7HPTSc7RZY1tamSDENV7DCGQQ6IGkRS2-HKUFyDe-hUf5VnHVfR6q7WZHp0JQzZvvxEtLhdnyS1lPR0TO68kFv1ttatVMFQDHoJmc-m6xQWQBHArOI2467c3zvln88O7kWKrlOrqUv0GHzxeNt_BlmBKzy5ptze-suRt0aMN-HLlwcsBc6yAkd2qDrG3aNZkqHdTM3T_UI_P2qecsm0ZXsb9O_bRQhcXvXWX6tb_6HTIwg0938Uq-o3qxvO6Dh3ySR6--hINZeFJhy6yiEggz98LLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXplPmyJFrHH7Z-sEQbZ79itZxvxFQn_xzN7LFkRUo3d7eyV-jwgL5_2Sfsn4Jl31FpW0PIq_y7eyGdrnVsaIpEIvzDEykGxGEtJwVKISP3s-h-iTYfsIT-QmjchhDVeCrvrFTr1PAB9jygCm8RCkwV4yS4ycjsD_pnLIiIdwuVF7KJTHghhjkNu5iuxooLzSmMBkNPxbJa6yIe89mOMAiuXpQUTVHD4s8Vn1RPkZKE6Q8EMpIZBekfHv1ZVTNY2aB87YMLTue0thVHNQKHpBtMn_EEkRGiAE_AOBFJEm5rWuMPyZBUUfu7-qGr_hUquMFmq1h2qGuXDdqCBGIzlKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر رونالدو نازاریو در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97086" target="_blank">📅 11:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97085">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=d04Q2CiLVfzLpHwPhz_dkGHBWvHcsqW1dN4EsnFOU9uZeXvrG4ahU3MAMy3mvOx-p3PaMHffh8pKsDS-V6mVeghth4cgYntIfysNYKjYvFQEnLK2ZOAdk1l5ykTKNage5DfN-VR-pYwe_2xo1-g856UZ9DY0c-NUFX_QfmiMWlb_PG17FnXQ3Uf5XbtfgQuKN2parF1hlWE7iXfJfaonVcONJdpK7mgAurYeRgPHCs-tfEH95OLhqPsf7wCaF_dGxI8EPUxFYU2x-Qsx0VXFlVGFef6fLRFubCJmGSeNsNMe7skFXSk_Xj4cjgpfBXmza0LcJ1n3uRHRhTi-zaJjVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdbeb523d8.mp4?token=d04Q2CiLVfzLpHwPhz_dkGHBWvHcsqW1dN4EsnFOU9uZeXvrG4ahU3MAMy3mvOx-p3PaMHffh8pKsDS-V6mVeghth4cgYntIfysNYKjYvFQEnLK2ZOAdk1l5ykTKNage5DfN-VR-pYwe_2xo1-g856UZ9DY0c-NUFX_QfmiMWlb_PG17FnXQ3Uf5XbtfgQuKN2parF1hlWE7iXfJfaonVcONJdpK7mgAurYeRgPHCs-tfEH95OLhqPsf7wCaF_dGxI8EPUxFYU2x-Qsx0VXFlVGFef6fLRFubCJmGSeNsNMe7skFXSk_Xj4cjgpfBXmza0LcJ1n3uRHRhTi-zaJjVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
هالند تو اردوی نروژ داشت غذا می‌خورد یهو‌ تو آینه خودشو دید رید به خودش
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/97085" target="_blank">📅 11:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97084">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=fzQ1pxwFABkk_oPX9k6ebUuQIeiBTOkMCOe0Ir8hl85XgXjH7a8dc7uSoQ0FhUWIQQUzKVGbrqzmWN5TSI_LCg-Yl_ZTDfEW4dnRN2f-EBKv-rDm_acnMOurAxdX33R2iO7k3Yw5BD3I-GvuUzngWnrHDN1zxb0FVh6s5sMyw9E7KLW4Q9En4Sw6MfUyYVef8BHgG61FgD2cJIQu5KstOHF8BVTPJ8BpouvrIBa3nEeTVJmECEXVsQGUT26RcTKweDIkmg8uEeUPR6_T-r1TW0dwJWnCJwQaHTdA7juDPQZjPCVsV6XWJf5sXoNPY2nw6hGlec0go3fzKl0ISY9XSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65d2830ba3.mp4?token=fzQ1pxwFABkk_oPX9k6ebUuQIeiBTOkMCOe0Ir8hl85XgXjH7a8dc7uSoQ0FhUWIQQUzKVGbrqzmWN5TSI_LCg-Yl_ZTDfEW4dnRN2f-EBKv-rDm_acnMOurAxdX33R2iO7k3Yw5BD3I-GvuUzngWnrHDN1zxb0FVh6s5sMyw9E7KLW4Q9En4Sw6MfUyYVef8BHgG61FgD2cJIQu5KstOHF8BVTPJ8BpouvrIBa3nEeTVJmECEXVsQGUT26RcTKweDIkmg8uEeUPR6_T-r1TW0dwJWnCJwQaHTdA7juDPQZjPCVsV6XWJf5sXoNPY2nw6hGlec0go3fzKl0ISY9XSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
▶️
🇲🇦
خوشحالی سرمربی مراکش و خانواده‌ش بعد بازی و شکست دادن هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/97084" target="_blank">📅 11:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97083">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=FJ7QVDO4n5KuSkbGhnA5nee3RDR8sEAhUYJyFF3xbds0UFYxWd9DCjvvCPj9xvWbrsc1lc7XASRgXyDVErQ7U41pdDDvA7Lj9iFlg6s-S8AxCliJ5upZyW73nY5bk0e1dS6q-Ie3YNohGYEBWZkvK0ccayjLmIWL9OzAXtfBroZOia-HVuCheEjNj9G6tmEdMUjdjj1IRZMWx4WRwooHuuqWiY1fIMVHsv3qxUK_iM4315zZGHhI866U3P3JE0TV2fNWdRBrvedAXLUgs2D2GCv9AskRHOop700e0NH66i3o-Glx9ki87EYo6TN8Ycx57b2KBkW-oJ3aAXkWeURqag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cd2ed3762.mp4?token=FJ7QVDO4n5KuSkbGhnA5nee3RDR8sEAhUYJyFF3xbds0UFYxWd9DCjvvCPj9xvWbrsc1lc7XASRgXyDVErQ7U41pdDDvA7Lj9iFlg6s-S8AxCliJ5upZyW73nY5bk0e1dS6q-Ie3YNohGYEBWZkvK0ccayjLmIWL9OzAXtfBroZOia-HVuCheEjNj9G6tmEdMUjdjj1IRZMWx4WRwooHuuqWiY1fIMVHsv3qxUK_iM4315zZGHhI866U3P3JE0TV2fNWdRBrvedAXLUgs2D2GCv9AskRHOop700e0NH66i3o-Glx9ki87EYo6TN8Ycx57b2KBkW-oJ3aAXkWeURqag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇩🇪
🇵🇾
خلاصه‌بازی دیشب پاراگوئه و آلمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/97083" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97082">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YOfZLp5zEUsrZWOyVWhLvTb3SwqtCZtONmUAWZxnRg3vn3h8DbLYULknA2_SdpI_MigFvxPC41QHC5-0fOEIYq31c0fRaqNiepBdTW9ZfGIpjMkLZq4AdqHl00VmPRg930nTpIryjOQi3a8SG7rR3X08Ll_RLWrZgZrbW0vkzd9aqa5EFtTf5AuRz8KaUrjjaBQCyUkRjetujY7FgYYrozXgDmV2FNhyoXBLAcPIIoOt5XjcPdKsup6lkgofSsM9mYwl9q4HiBuGzkW-qEgUDWYYddGtnP4TWn9nljdNo3aYjz4XfImMJ32OSrsu4N3YQcEDXOqdtrbYqz76ZBTctg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
عملکرد تیم‌های آمریکای جنوبی در مقابل اروپا تا این لحظه در جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/97082" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97081">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-text">ریا و دورویی برخی مرزها را درنوردیده و حد و مرزی نمیشناسد.
واقعا با چه رویی میخواهند در مراسم تشییع پیکر رهبر معظم انقلاب شرکت کنند و در چشم ملت بنگرند؟!
https://t.me/hashiyeh_news24</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/97081" target="_blank">📅 11:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97080">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=h8z46SuXU-MIN28kevccbHqcyL-jT46hZAPNAl424wx0Dtj99RccHMIcR9nds536vQiN-HDfL-Dib4qW-wBB-HNHo6otjJOlcU0Yq61Tl9mzz4v5CmP0_4vMMHmV5sPgrP_eoCEYUBl4eUwoxiLD_Wb0-yW-XzPw0pHd2W24wXIOqOcDImzOeEQFBZjRJU2uBm5O0fm4d-eGRNdWcatnqvYA4IJ0v9YFx1KorUg1dT5ks1YbQ71P_QLVTWH1q1B8bYi0-sNp7XbATWLvvPA6l5xi7H6sLq6YuzpKdzh-mu6cg1qvBygtajpCa9Hk3B1T6__Lv3iFpRko97TS_du8146tK_mmXUA_zWeXK1A7CM2K7Y7sgWJIlFK8HtVh74bsOejouAM4cOMW9NzAhxbf5SqYPnAfcjZO2-WhEfT0ptGvE2iZGqtO9fy0uNE5Q_lOTW1h0sd6gy-qsZVWszl-IuyI7yfi9WMNvtq9hTMy1ebh5ZjXR9Y4_ncokRBwazb0m8xApeqrUgpLka4pkyPrFJeUkxhurGmCri2iQF6MZdoVJVzsBAyDX-_hW5MfIMwhTZK4SL0zrFCZqA6A15CikDKGAVK3TymJNSjgRzDu2_6NKlRHUYeqHc3grcu8nCPS793wrYGuE7u0hKYvcZqHQXMQOIahWN8p194yUEdSu_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c92c81a09.mp4?token=h8z46SuXU-MIN28kevccbHqcyL-jT46hZAPNAl424wx0Dtj99RccHMIcR9nds536vQiN-HDfL-Dib4qW-wBB-HNHo6otjJOlcU0Yq61Tl9mzz4v5CmP0_4vMMHmV5sPgrP_eoCEYUBl4eUwoxiLD_Wb0-yW-XzPw0pHd2W24wXIOqOcDImzOeEQFBZjRJU2uBm5O0fm4d-eGRNdWcatnqvYA4IJ0v9YFx1KorUg1dT5ks1YbQ71P_QLVTWH1q1B8bYi0-sNp7XbATWLvvPA6l5xi7H6sLq6YuzpKdzh-mu6cg1qvBygtajpCa9Hk3B1T6__Lv3iFpRko97TS_du8146tK_mmXUA_zWeXK1A7CM2K7Y7sgWJIlFK8HtVh74bsOejouAM4cOMW9NzAhxbf5SqYPnAfcjZO2-WhEfT0ptGvE2iZGqtO9fy0uNE5Q_lOTW1h0sd6gy-qsZVWszl-IuyI7yfi9WMNvtq9hTMy1ebh5ZjXR9Y4_ncokRBwazb0m8xApeqrUgpLka4pkyPrFJeUkxhurGmCri2iQF6MZdoVJVzsBAyDX-_hW5MfIMwhTZK4SL0zrFCZqA6A15CikDKGAVK3TymJNSjgRzDu2_6NKlRHUYeqHc3grcu8nCPS793wrYGuE7u0hKYvcZqHQXMQOIahWN8p194yUEdSu_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
وقتی سجاد غریبی کسخل با ابوطالب‌حسینی فیس تو فیس میشه؛ سطح برنامه رو فقط
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/97080" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97079">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFLuNdTXp0bnV57uyKw4LUEKxpJMTbzmjCclyUGsijIl76naq-hFjWmBjN3eXAzM459xViyXpUA6_AVXl8Olnx2krYiPn6gBaKwTPC460YJLXfJH9ktQRRPWBTq6ceJrcZJqKOFhLhbMHVmrLc1WZ6JP1g4BQJSW5YITJBTEWoQviA9SDhhbYTbqgvFci3_Fr4ZrALE34kxJ2bQxd-LbPRWKbSBYqkl0twoulmBCW-Y7VTRnwlwE-4S8JKZe3F5x8TJJn6FljFAGUJcNTIbA5yerF7OjboQjmSZgyFViq6BUMeCmRAaFjEvVCw2GFy80KY1fIsKeF_k79aiRPs3yWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
#فوووووری
#اختصاصی_فوتبال‌180
🔴
با تصمیم نهادهای امنیتی و توصیه به ارکان فدراسیون فوتبال، امیر قلعه‌نویی با توجه به فعالیت‌های اخیر در دو سه ماه گذشته، روی نیمکت تیم‌ملی برای جام ملت‌های آسیا خواهد بود و خبری از تغییر سرمربی نیست. این موضوع پس از حذف ایران از جام‌جهانی از طریق مهدی‌تاج به قلعه‌نویی اعلام شده تا خیال این سرمربی از محکم بودن جایگاهش راحت شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97079" target="_blank">📅 10:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97078">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=oW86RlNqRSra5D_jGAR31ePWUc8HtM53IYhixXM1z8HRQO5UbTUDoaw3DU-MbNIhwUZHdrkUONABVoPQj3VRr5Zm9B9nPJsTPz0PuL4Sl35lXRLymDkNEYu5kKzBZMM35qlfymtndKBxbCmDMAOTShKrhhbHt2XFsyCFHP0YdS2y6bB5rPGm48tcrSN7G7i3WqOmYVEAE2_1mS6F04rBsrfpUmqBNK1wqZJ4E_In0Km8bj-hwTpprr-W5HbSmei13YbnUI4uYgn9mSyj69XKOjPKUQMgp7HKeYmz4jsnB2oynp9Q7IMRang-oIe0XUuCT5DXTVbGPcg3uv1V4vixAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22b45db9c9.mp4?token=oW86RlNqRSra5D_jGAR31ePWUc8HtM53IYhixXM1z8HRQO5UbTUDoaw3DU-MbNIhwUZHdrkUONABVoPQj3VRr5Zm9B9nPJsTPz0PuL4Sl35lXRLymDkNEYu5kKzBZMM35qlfymtndKBxbCmDMAOTShKrhhbHt2XFsyCFHP0YdS2y6bB5rPGm48tcrSN7G7i3WqOmYVEAE2_1mS6F04rBsrfpUmqBNK1wqZJ4E_In0Km8bj-hwTpprr-W5HbSmei13YbnUI4uYgn9mSyj69XKOjPKUQMgp7HKeYmz4jsnB2oynp9Q7IMRang-oIe0XUuCT5DXTVbGPcg3uv1V4vixAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
💥
🇧🇷
گزارش فوق‌العاده گزارشگر برزیلی روی صحنه گل مارتینلی مقابل ژاپن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/97078" target="_blank">📅 10:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97077">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcqQr-lim67pn1PHSWATffEYi2JSVCZhlE_K2jSSXNTQOw1hw_0XuC7DYm6sBfZxzyf3xLmHbyUKa4sZKXk9cuibJYmQ_pMCT0L0MA34YZhX2ub_42Un81I5ou3ozvE7y4aqGduR2JyJp7K8hYQWkVSw8Qn-tAE883IsG6XapJ21auLsMpYwwvV3-fsG72YooUolPW-dL9A0Mkio8hsK_GTlxY6pbw7OmMoMwXm9r9FOtuHT5QHHAR4491v9nHhneFEMTChIeIwjjLEOhaXuZv4uF13l-9YixIc-ZIU7Z8Ddq8ivdbkC3rAA_WBTRh5PVtiG9FhEmnZxZrCZwTZtjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
📊
🇦🇷
جزئیات عملکرد لیونل‌مسی در ده بازی اخیر مسابقات جام‌جهانی قطر و ۲۰۲۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/97077" target="_blank">📅 10:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97076">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1P8IihgZaEYha0pukduX5_ZQlKVnrH5jJg0hZB58oN0GiXC5ud_b_zWf6zJC69UUv2ZFoXQuzHarBIPkKT5xNPybEa3XVySMDE6bBPBVeUd84KCbqnPDDi3d6IogvKtczf2GaIBpjYQ3XGKp4iXWdMplLeGPWvBNDQdjGaXULJwl4DielSLIfFv6IKvqmWWTW4_u9xd_l-3_EzLxEsNG0rUzS1XepCVCYMOhtwNj6PawzTFAINKWNIWnGc7sJLvwKaxa36bNJoqbiSgHfTyVWxaT4sXP2vPDqhjHhCrtU29L3tc_h51rTQwl2SWKlN1OPNYnD0pv9ydxTV2Nj1DHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
پاریسن ژرمن معتقد است بردلی بارکولا را باید با قیمتی بالاتر از 116 میلیون پوند بفروشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97076" target="_blank">📅 10:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97075">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead284c858.mp4?token=DeR_HzsrVFIMj4p4jGCK42gjd2rozZD2LrOVS7Tg2NbMsqGbIhaI77h2Koshy4spKg9V0XLU8AU-Q8vfaxioGEFtPcGt7jFRRKF9YS9teC2rmH5pQK0cxiEE15UZrH-8G189Fe874wkvTYJNMIIUKiszQxB25Nxcc0BtXcN44LiJJOeQMNtNepvhIS8PYxDUjApoPL894pXZ5jCbxhTjIc9BPVTJ67S4I9BGC1CPD4B3kNE-In65_iM90C2hARC26wKMbOGKWfw60J9WJ3L3tblyPijDsxK4ViiNKZ16k6SVg3ejC_UDEz72mPCyDNKE4kfAVtAmymLbSUL_jBfTYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead284c858.mp4?token=DeR_HzsrVFIMj4p4jGCK42gjd2rozZD2LrOVS7Tg2NbMsqGbIhaI77h2Koshy4spKg9V0XLU8AU-Q8vfaxioGEFtPcGt7jFRRKF9YS9teC2rmH5pQK0cxiEE15UZrH-8G189Fe874wkvTYJNMIIUKiszQxB25Nxcc0BtXcN44LiJJOeQMNtNepvhIS8PYxDUjApoPL894pXZ5jCbxhTjIc9BPVTJ67S4I9BGC1CPD4B3kNE-In65_iM90C2hARC26wKMbOGKWfw60J9WJ3L3tblyPijDsxK4ViiNKZ16k6SVg3ejC_UDEz72mPCyDNKE4kfAVtAmymLbSUL_jBfTYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
وقتی میری میوه بخری فروشنده قلعه‌نویی هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97075" target="_blank">📅 10:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97074">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
▶️
🇺🇾
روایتی از مارچلو بیلسا سرمربی عجیب و خاص تیم‌ملی فوتبال اروگوئه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/97074" target="_blank">📅 10:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97073">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=KkcxTNOasD7HMnlN9wQuDTrwmzdWUl46vglbfnvrjOWngVm6joJk4BsSe7XLooHoa7zgpfWoVZlcP3hlh0XOh692kg7B5RyQ4nkLkat7J_q0bCPDn68J7oKJXFY7EXOrzP0oiNhEkOBhn7N5z0pxRURTSjkq8stOwCIykVM4U7KaT98HJubou5AVpEVkIA_0dhkx-dA4RhJSSbZe5cHDdw5fL0bkkbMz5o5AZlM52TjR1U-9d-WJP1IC91zR3v6B26S010hudZ5tuySZs-QciIzZEllBLkbqh8O2LYjUlOpRRla05ltrtCtuqxSE56K0oSAwvYM4Gvq29pLFe96aXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77d79899dc.mp4?token=KkcxTNOasD7HMnlN9wQuDTrwmzdWUl46vglbfnvrjOWngVm6joJk4BsSe7XLooHoa7zgpfWoVZlcP3hlh0XOh692kg7B5RyQ4nkLkat7J_q0bCPDn68J7oKJXFY7EXOrzP0oiNhEkOBhn7N5z0pxRURTSjkq8stOwCIykVM4U7KaT98HJubou5AVpEVkIA_0dhkx-dA4RhJSSbZe5cHDdw5fL0bkkbMz5o5AZlM52TjR1U-9d-WJP1IC91zR3v6B26S010hudZ5tuySZs-QciIzZEllBLkbqh8O2LYjUlOpRRla05ltrtCtuqxSE56K0oSAwvYM4Gvq29pLFe96aXTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عصبانیت عجیب وحید قلیچ از خداداد عزیزی؛ حسابی کلش کیریه سر صبحی
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/97073" target="_blank">📅 09:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97072">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=Qd-d_AEndnyJ4FhNMPW7hAgQlhH0v606YdzqWgHoOHIqFIwSlSFrlch2QeCCW_ATfXVGVRbRcJ1BPOEPQR60sd_qrktz7NMugstW4709bNL92AtnLRJ5kWqnCsJ-Y6XLzSP6cRGE22z4fQ04BKgriw97-GJDTsEMg73GGR38ihVclXRWI1xIj4Fu28ipuMLRhMTiXRQHXvqiAsrjjG-SnqqQZdEdqtPJgLFYHFLsVlx3wbuGRq5JeUIyqpt-se4UVQEitXlxCsfTb8cKbOH8AfqtKs-mqNQx3OyM93AGml41Vwrpoitigy6HWYS2AINm-pK5uT5S9GFQZybf78Vqgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d90dfc72.mp4?token=Qd-d_AEndnyJ4FhNMPW7hAgQlhH0v606YdzqWgHoOHIqFIwSlSFrlch2QeCCW_ATfXVGVRbRcJ1BPOEPQR60sd_qrktz7NMugstW4709bNL92AtnLRJ5kWqnCsJ-Y6XLzSP6cRGE22z4fQ04BKgriw97-GJDTsEMg73GGR38ihVclXRWI1xIj4Fu28ipuMLRhMTiXRQHXvqiAsrjjG-SnqqQZdEdqtPJgLFYHFLsVlx3wbuGRq5JeUIyqpt-se4UVQEitXlxCsfTb8cKbOH8AfqtKs-mqNQx3OyM93AGml41Vwrpoitigy6HWYS2AINm-pK5uT5S9GFQZybf78Vqgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
سید حمید حسینی سخنگوی اتحادیه صادرکنندگان نفت، گاز و پتروشیمی:
با توجه به شرایط فعلی، احتمال دارد مدارس و دانشگاه‌ها امسال نیز بخشی از هفته را به‌صورت مجازی برگزار شوند و فقط یک یا دو روز برای رفع اشکال و حضور دانش‌آموزان و دانشجویان به‌صورت حضوری باشد. هدف از این سیاست، کاهش ترافیک، مدیریت مصرف و کنترل شرایط موجود است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/97072" target="_blank">📅 09:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97071">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=NcmS-EqA_HVq2ivGQsL5XqYFDdw5m5TUGIYXmOeR_QqGun8YoOM5W4Kqig926IqbO-0gKT8Vbx_Srx9s9-x3Yi_QtV9Z1IuF-t76AZPVv7LgJ2Fkq9Owc5HVgbmb_KS17pHtI7IV6MdDJkCTi9LsPCS7us0-KWx18DW_71AtacKkyu88iI7ng-WavrwwUUQGV-aZ7TJ1NHx3VZIpX2QyJig1kUSXWu85tNLq1MO-DwPKRUvN9Vzto1fw-1GymPYxbAjaaGxq_RvXV8yh04nQEfS1yZPVreeXYtlDDEzZxJkEQlb4N-H1MztFsESIGX_bOIVs0m2PJ1UkU5zGaQrlZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b23fa1a74.mp4?token=NcmS-EqA_HVq2ivGQsL5XqYFDdw5m5TUGIYXmOeR_QqGun8YoOM5W4Kqig926IqbO-0gKT8Vbx_Srx9s9-x3Yi_QtV9Z1IuF-t76AZPVv7LgJ2Fkq9Owc5HVgbmb_KS17pHtI7IV6MdDJkCTi9LsPCS7us0-KWx18DW_71AtacKkyu88iI7ng-WavrwwUUQGV-aZ7TJ1NHx3VZIpX2QyJig1kUSXWu85tNLq1MO-DwPKRUvN9Vzto1fw-1GymPYxbAjaaGxq_RvXV8yh04nQEfS1yZPVreeXYtlDDEzZxJkEQlb4N-H1MztFsESIGX_bOIVs0m2PJ1UkU5zGaQrlZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🤣
وقتی زودتر از تلویزیون نوتفیکیشن گل دریافت میکنی ولی کونت میخاره نمیتونی سکوت کنی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/97071" target="_blank">📅 09:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97070">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWtn8OSeUx9GH-yRspjzPOvVtD7_FuUinqCa0AbnQwjpvcYlBYIvdNSDr2n26P3kQjtqSKgMaIE3z_ijNhXSYr0oivROt1YTtbu1vzQupT_kPPiGNqnSr7Jlgvf5ciF74cltCVMxb2TCiWcGAzTjmw9C0rL5bOknYbJF44nPoxkJ8Y5MGeImpjq3w0cnsaa0yUKbrXEr3r6Q-9CVy8v7Fz9F1xqn60p1IdXMYHbgeh1-4OnESJQh3Vu7nhLu8AU71MJePqQdHx51jl1sDswH8oxQRPha4CEftOB8wOMm8Wt6EkaKnK8P0MX65KrcJ07dpVgIXHv42HCHZNISKFRSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بوسه‌نیمار و همسرش در بازی دیشب
😘
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/97070" target="_blank">📅 09:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97069">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=bDXT2wCJ3_nIUcCyHGHWjF01mx21yFKktlUaVEFhEb1fogn_6oW2D3VkqVUj47mH3o5nmh55J6FzZ7pW8Gq-J6ZpCH7ecsmHGWQ7xZNRJxceqHUcNbAb2jxb7LDNs991pkW4rzcuP3EZPK5D6DJMfDXebucX3T_GPpPU9WfCi1UCSS7wvQwX6FEYc4tOikmJaM9oJjX6U0tZXxP54sE-ICdrszLGawnSIKS5I2ws_kc5-c7kDoKA1m4Vh17kQIeGNrQXKQGC3qJmEjaPojrpshW2ENZMpHEhwDk9UWYyp0gri5i-P-hSXw05SE034QHb_OseTg5ZxzigsDMFdwrhTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de3e24176e.mp4?token=bDXT2wCJ3_nIUcCyHGHWjF01mx21yFKktlUaVEFhEb1fogn_6oW2D3VkqVUj47mH3o5nmh55J6FzZ7pW8Gq-J6ZpCH7ecsmHGWQ7xZNRJxceqHUcNbAb2jxb7LDNs991pkW4rzcuP3EZPK5D6DJMfDXebucX3T_GPpPU9WfCi1UCSS7wvQwX6FEYc4tOikmJaM9oJjX6U0tZXxP54sE-ICdrszLGawnSIKS5I2ws_kc5-c7kDoKA1m4Vh17kQIeGNrQXKQGC3qJmEjaPojrpshW2ENZMpHEhwDk9UWYyp0gri5i-P-hSXw05SE034QHb_OseTg5ZxzigsDMFdwrhTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇳🇴
ماموران امنیتی فرودگاه دالاس این‌شکلی به  استقبال تیم‌ملی نروژ رفتند
😂
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/97069" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97068">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk5BH5NqjLgDgmz4mN9lhKvYmV95H1JTiWCAJY49Go-5sV-3TH7IeUSRlwVuslH481XoSZrIf-zXk1ZQ6zFtBU3dBOjqM2fYmpCxznlhZhvmn5lW3IqhIQCuBWf51pHb1NfhOHgrEbFJZQyDxoNztDJTOsq1FOZaBYlHvI0QplqtAMIJSgx4YZpUHJX10O_a3lb4NlmwGESjq1u4i7XylfS5khX2-pibLcnSZw-GRc2yRWkUKZqs0zeyqkHzAOmZvL0dyYpbVC2mr95WCrYMn3rxM6WM1Moa4NYpldfrXP7WsgAc_LsCk_qVU2j7vsT2adSHVVk9YVwriImSIuL5BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
یواخیم کلمنت، ریاضی‌دانی که سه قهرمان آخر جام جهانی رو درست پیش‌بینی کرده بود، معتقده که هلند قهرمان جام جهانی ۲۰۲۶ می‌شه
⁉️
⏮️
مدل پیش‌بینی اون همه‌چیز رو در نظر می‌گیره؛ از جمعیت و تولید ناخالص داخلی (GDP) گرفته تا رنکینگ فیفا و فرهنگ فوتبالی کشورها.…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/Futball180TV/97068" target="_blank">📅 08:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97067">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHpVFRgsu7cjAO0Kx3ictPjs6G7XdH0XLSdruWsSG3aOrJyUfyc-yDaDdGwWJQWpDYx5R9Ln6rfMpIOmkJ5r4mZgdR7HE20-dA7X2RBGb7T2-M9043Nd_G7Y1ly3Q4k3dAS2ANAdwDXn4WjAP9Oc-WCqIPLbThOPONs3iQVV_18dLIrgZ_hl7fbIM2oNISaPkoIWAcK1SnCHXSMSg_GeCIlyAjlp3jx4qzeOB6di1m7VMHFAqf9ulkLz1NgW9x6LfP_ytzbsSB1vLi8APnqgXL_RFClzvsmZlrowkfdEi2bErf4y3MgPJHvzemVVkPNng20P6XT8Hdfad4Kn3XJ0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇲🇦
اشرف حکیمی [
🇲🇦
] :" بسیاری فکر می‌کردند که این فقط خوش‌شانس در سال ۲۰۲۲ بود ولی ما نشان دادیم که قدرت جدید  فوتبال جهان هستیم"
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/97067" target="_blank">📅 08:07 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97066">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw_Ypk2HRp8JOS03do4CZjuEASiu5Ao4okBpOhfCEBCe7zR9EankofARgHGWD5H6-cGwMQgedK-gE-mfs63MVz6-xzsXrw0kE8xaluYx7VRwMGRb1k5_X1399zD8IJaOtTNnyPwBo3ITFYYsqZ6nSaKYTC78eRNVYIWSfGE_f0CNU5FvMjtJHvo7mvLBaoEEZ8C0ZXCoInujbXIjFVFlh-iTwISTj3rmqSdYETSd1P8hI_4uIzpQgcbfszQKiFQtDQueC4Md32YRQEbpFHItDX0fR5BNcsh815G4pFNL-xJ1ytlb-eAVf0aZq5wvwTgY1UdcLAEJXnid-YufuhGZBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇳🇱
🇲🇦
آمار بازی حذفی هلند و مراکش
🤯
🤯
از 878 تا پاس مراکش 800 تا صحیح بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/97066" target="_blank">📅 07:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97065">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2EOAfYftj_rQ62_SMk10KVOArgcj6EGPIq7-Qapq5tSraRYvlF4CdUTkJbtITOT5LRGLwG1cAxlsmeO8TqZPT0JihRTJRFv_nF5gS8pmA29s8tda7vHDoEQJPIQ1f8TwInmZ4ZDJwdMgKkDzm7vObINhp_IVMUsfg_pB9Oq7IBqJc0IjqPA07zhcY6iZap2VuO9vRCiPzc4u4jybvu_Ko1dyPq92PIwZa2_mYFYkBhhmdfAh-bGO2TPKvgPFEYQ4zLNcdWtkAZpVAz5Ha2J4RLEp39_WCkU2LBINNqQx76g0nSu0OtB5GkbHpMGq07PZSOl0oj7u4-nefC_EeXKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
🇪🇸
🏆
بازیکنان حذف‌شده رئال‌مادرید از جام بعد نفرین‌کردن توسط ژوزه‌مورینیو
❌
🇹🇷
گولر
❌
🇺🇾
والورده
❌
🇩🇪
رودیگر
❌
🇳🇱
دومفريس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/97065" target="_blank">📅 07:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97064">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y80oReQrjF9ngQvS6uRD33TY8JTAsLwYCYJ2_yY5x964Ju9QplngI0u0L1WjUwpkI2cUCUOXIFWtq7o6qjZMpmBLbNw-qznytB9iX1PddTNvnW93iE0myme9lP2VNj8JDX60u2em49iOXaA4qVePfSW87hqaQRFZx-dYv_AcIY_9tkPO4pvM14GW9YdDwUoR33XLRypVDL-I6-Op4dfowFTgdOQAr3gJj3j68PYrSanMrkZwQvhHw7J1NZyDiSp1Qor_WnWk5j-3SVR4ayOAd0cl6xOQFAUIEp5uEBeRhXVYJ5GnGczFk8XRdY48QMFUIl_jDIM5ImZBizxLidYCVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
تیم ملی هلند از جام جهانی ۲۰۰۶ تاکنون هیچ مسابقه‌ای را در زمان قانونی (۹۰ دقیقه) نبرده است!
• از آن زمان تاکنون ۲۳ بازی انجام داده و در زمان قانونی هیچ باختی نداشته است و یک رشته ۲۳ بازی بدون شکست را ثبت کرده است.
🇳🇱
🤯
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/97064" target="_blank">📅 07:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97063">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AM3knxewGXjuI792uns-lxOZ02Jo7EFYrMFjRDCDIPEzz_Xg4taivYPvHhLlSIeU4K5i1DsTnLi8_vYIJhRFacQZDtWYpQSN505LBK18Xj8W6gqQZqAZnik_upqJIDRVtoTK3FHQ_DbnSa4XZfU01iHXvrGJsS4JgclnO3EwBRMhHZ5V6x2Lr5h9J8txDuDDMkLwrKPwxmUFjlJNoOfa3Qb5TvF6fzral30K3rQvjhtuNQkvBKHLNuuF-eEsJCet5NuCwJBMQvtsybnjQq28WEznkwewtiCyZdh2X18OoHch-BaYu5zvKRu-_QBld6IhoWfqlF0vnj-QO7tT_QPCzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97063" target="_blank">📅 07:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97062">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/QMcGnvdFQx13XuOtVu31LYhHiDSj6zBB8DkbeRRR0TtImOIutA4DvBSKEJsH6JZb4CCdqMzOQ2OA6jA-GqIJ6CkpCoxiiEIQxnbxHSf1PD3R8_5HVayythN_EaLzSGpv-SSlt61WZ7OGiLcie3c1YzxzrNWt77tyWcqvsfB9m4xzvAK9bPL3t-xDgkVtcoch-no9Dyo8piWiyrKtv1dASMJMzf3qAizYhXTHlnDB1jIf628x4IQx5gHVxL3BqkuywUPBm9uz3RPbSO54vN8V5tr-3T-IU7-ZG2DfRZZoRXXetkIViYQwvI2Hf84Oh3OzFR6uwXWT1zsGsIvC63xSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
👀
یاسین بونو، دروازه‌بان تاریخی مراکش، اولین دروازه‌بان عرب است که در تاریخ جام جهانی به سه ضربه پنالتی پاسخ داده است
🧤
🇪🇸
در سال ۲۰۲۲ دو ضربه پنالتی مقابل اسپانیا را مهار کرد
✅
.
🧤
🇳🇱
در سال ۲۰۲۶ یک ضربه پنالتی مقابل هلند را مهار کرد
✅
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97062" target="_blank">📅 07:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97061">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oi_gzMYicN9ri_howSLLL70JIqwDlp7oMmArdIy5qOgiEbo5-7wlS-hyj0OegSoySTgibJyQ3qoH9P1JMgXYBHt4n31-TG5B-v2AElbN39v4TJjVgwQ0bZjAEU4EZ8PNd8JWm7fahSVCDfyb2l8Hafl7hVDpXmrqcAPlcvOWXNsFf23lEdiROKTspEzjCsgmFPJaY5jzZcRssJ3B_F4dy9nivOw5eviHjkgN3oyg1j6muj8a2t3ZncmCFuD6RW-RahPT1jRbJ26cSkE0PkBRGIS9oE4UELrWJ1lRlhPX6Y4tShhLuWwmeZngvRCQb00jC6V22eYbb2QH8X7OV2GF2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇲🇦
تیم ملی مراکش به شکست‌ناپذیری‌های متوالی خود تا ۳۳ بازی ادامه می‌دهد
✅
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/97061" target="_blank">📅 07:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97060">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ9ZLtWMK8sKmmv2kypePX9T3C5D53AfnlnqYNzw44EwTp9mE_6HTmcNXoGHtFjoUNQOmbP2WwC0y9lSPjG5K31jvlrgG5ygUraYTkOU4yx16HirQf4BNOH_48sw9s2ob0mPpBFF-7F8XDYjHiBNLTKW3poNIXfeASZ7htkV3rVmvq-82EHdN4kGjJQP8X-ARGkgXc6QfxS46TItU4w5PmDefJnfUdQGABy5V6RMPXFpfOB8uiMzKGMmL93j92EQoCFVDpKPXswsUI1jE6vIBfQ8hjKQCxaHgfrVBUP67KSSYpVX7EtEeLG2Prsk9LYoAZzl2gRv3wjGOYFt8y9FgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مراکشی که تو جام جهانی 2018 از ایران شکست خورده بود تو جام‌جهانی 2022 و 2026 تونسته اسپانیا، هلند و پرتغال رو حذف کنه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97060" target="_blank">📅 07:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97059">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDBVf7x5TLYMHtT8Eus-J4cQzULaTjL3nzyWLStZsW1tPue9xQFPJdXCIWtKeldmpVzhUwiBH6Wb1HhOAaeyQ_gi-803Ll1DujB_agJd3BsVZazKJFAK2liOxDJZFrgpQq7wWXlmSWIY4Gq_7dlGjBRucq8dNd-12cWP8-mXWBIBJgpOBnYMI3KwDVUci48S630btcsAPrOZ28ZgjwM6qtD8SRCNbfRYni_3eREwXGLwYAR0MKs9Fbhi9gTEzzguXuX4vRfwsRIvChSci3rpf32XkQTRrZ1OS72ez6fsCwcrq3yHq5WjQrKRvidTtzN8E0yzJCJc8Rd7p3owOc0RQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار حذفی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97059" target="_blank">📅 07:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97058">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lskCrTLwnMi0fGRZkw4yJcPK7CnS6IM9i7WkFZfO6mepudzEMrU2UNFG0S6NTd7iX6yq1wbRXAuUzd6Z4A3uEsZad-cokqoAdFxyoid1H_rP0rWIOpwkXP906fw9352RJqAJWPXADVhl3t1R5CCSdzJSsHr9YGI0w9e8LBKZkPZvLZ2tBgBcRxhTzZ1jaOdDofUytEgKBfTO4o2IqNgyGEAaACOwFvqGhP80xAuJn8cwhasXJHgjFBXsz1OgBxuEYrFgAmnxmPAt6ZBl-tmW1ZfcIO48sa7MMKHDWhmY-S4TDB-aAOxn-2rAjVK9kWPmr4k9H1wQCFv9O02HV67ZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
#رسمیییییی
؛ مراکش با حذف هلند راهی مرحله یک‌هشتم نهایی جام‌جهانی شد
.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/97058" target="_blank">📅 07:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97057">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">گللللللللللل و تمام</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/97057" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97056">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مراکش بزنه تمومه</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/97056" target="_blank">📅 07:23 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97055">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بونو اینم گرفتتتتتتت</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/Futball180TV/97055" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97054">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">پنالتی پنجم هلند</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/97054" target="_blank">📅 07:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97053">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چه خبره امروز</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/97053" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97052">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اشرف حکیمیم خراب کرد
😐</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/97052" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97051">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">آقای کومان ریدی با تعویضات</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/97051" target="_blank">📅 07:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97050">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تیمبر پنالتی هلندو ریددددد</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/97050" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97049">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">همه چیز مساویه</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/97049" target="_blank">📅 07:20 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
