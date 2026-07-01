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
<img src="https://cdn5.telesco.pe/file/UFXmewFz6qrOO05Si9vO9AO3mISN0q_I0dmegawcwKTzy9aAvSWmv5q3vjGfA_LLgIC2zWexCbKYs5FuPSTigErLQMe8oRqSulMXqJ_elp58EN-cPU5syjIh2zre6QfLWAwcBSQdyWHddcsOIGJcekg4YKT_LWaWSOGRW87HbuLJJLLUJIKft0Yq0n7uhl0UNIMhcvbvJt2YSYXXFzlWq7lzP_XcChLJfE6ZYz81Eq0la7TI2-0_OLH9r5QPtAoss23lJ2zKyA14MhqnxOD77R1zHi4wNROZ5ATH1Qw583JRGwYZz0-HnBxg5sShLqwg7JWNh_fUJLFyj20wh3jj5w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 664K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 00:15:32</div>
<hr>

<div class="tg-post" id="msg-97465">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bopFgr9pGbgtu6Qh6HEI3pLzBPa_s-U7_Fj2FXI53cQEt5JYxtWVe2nYMqwWZtoBpEzB-bDwrcdytp5yWJlt1UboZqH77mfU1i9scQH8pnnHiiNh8bkg5tQrmvYuBoPdviqgBR2FbFcVZ_z5ZWVgXpnjNf-4mMkSGHUKaMmd08lOkH_iBQJnJeXAjTP2UbwM_erENZUri7puHAj6EimvdLiSNBmj0a_lDVxeNH58OUVgs-0uVx6Vk8AYPYeWP33IAX9zvtdz1sOsmPIueRjaETHIauqwAU5d-owFVzfsnvRAENFKUwkWfb8VCaAqyyxCrymh9mirjQd3UPw7gkpaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ci4mbYO3UMrgCvgjJeB-sD5QnF0xeYB5mmD6OP04oK2g61TaJ0L13V1rSQnxbn_PmRG-9quPfaj6iMqtWmprmD5wirbvr0h8YTVM-qrq0MTGO5lIpo5fVCzZKkU1jZ2gY8fMWo7La2s0EsA07TcrM6iPHkvTYysfcf8FmZa6ADNvtKcYStQnoVkIH4m4UQr9oN4-l3dyyptPp2RXuxshhLxvqCFFmXsBTbYR0I39OVr_KHFMWdaa8Nl7TmbXxVkUnCvp8Un2PH1FPISVSvmvrEbo1EsQkEAcoy4QPwp9IgKVdHIyuljfoX-0R_04kyCxgVDWSal77Qt8Cin4K9E9WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P8DJ5OO6HuERq_0ad-0y0QRPef_7bBXqqBfw9z5N5AvBHRcRMVdiNJqJzWAa_K3z_GFxravXC8RWUsgPoJxUt33vVMzbitfYcL00cWYPlXql9R4VepY6mkPIJd5oerN5pfzU9HQihIfhJpQnWssvy-KmhKz9T1CiARzFvyoL2gPUAi5NZbiJH90175VzNR6B_0lHrGjh3B7uIyluBmJRn9a18QR-mSBJw-aeFtmGWHFs6t3Rztrxtksxyxk6JohQTJrDjnYR3Vsif7HBwnZqzO4FMvR1DuHM4UBIn9ua-u8siTzEqSCNyMR-x4AoeNRgZKJD5ovzYlK8kHvsx88THA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جیمی جامپ های بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/Futball180TV/97465" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97464">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OR4LS9hKb6u0BfOcrgDrFW22jiJQiEJ0-zID10Bg7GjtyjCMfAri0ekikYdccsolTaUFFGd7ec9YQIKkh57ALtPBXultufXceDYL5RKg7HZnwzAzbkGFT3pvEBk3aoHeTVIabtPo64aNVRQRKOHa6X3JOnRFJ0hh55h8DAQI9bu17bRE-gagc3QgbhdPO5OZrYmo1eb9kz21EPHuphYbvwCwlGqSW5ONySnyN3qshH1TQJ_h3YOPqOIpqxXUJsvHM3BDdvIt2gF0ZjDIRecox9TG5fheaHuJVd_aedIZkLpQBcmCa3ESD9YiHqKGsuhdSTo3NShExLJki4GjYaemMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری متئو مورتو: بعد پیوستن تونالی به تاتنهام، کاماوینگا هدف منچسترسیتی شده و احتمالا مذاکرات بزودی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/97464" target="_blank">📅 00:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97463">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
متئو مورتو: بعد پیوستن تونالی به تاتنهام، کاماوینگا هدف منچسترسیتی شده و احتمالا مذاکرات بزودی آغاز میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/Futball180TV/97463" target="_blank">📅 00:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97462">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گل اول سنگال به بلژیک توسط دیارا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/97462" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97461">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">چه کصشریه این بلژیک دیگه</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/97461" target="_blank">📅 23:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97460">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گللللل سنگال زددد</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/Futball180TV/97460" target="_blank">📅 23:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97459">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFSdOixjcETLAGGnBHNdyWxQI_AGotsMozT5vniJYpK5pSVZpObQnJpJpG0vQpKRg2AF6CaTBoStmf66XCnaAH-IgxCgSGBP06-FPMUMVwWUhVPLx9FJqtLmcHuOFxMdIFIF8ijkQZ2EpE5bzPKsLv7CU1F0j3XdN_zt6NtPiPoXZK3jtS_uLb9vs746zBIz8ud-H3ig6YkT9g6b2iKlq7kdaoeVsVjzZJ7zTrsB3yl03RymS_8DJjy5MtrmJpr6EibMC3bE72lxx080g1WLxiii7Zjqp52QVQ3K_atxpLLteatHAcXaaGTc19EPGV7leLFIdhBxBKAsohdRq6M_Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از شروع فوق‌العاده امباپه تو جام جهانی، هوادارای رئال یه طومار با عنوان «کیلیان، ما رو ببخش» ساختن که بیش از ۱۱ هزار نفرم امضاش کردن
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/97459" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97458">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a16ec06f22.mp4?token=lABwlCKkcIDxgA7-Tlv37AXWZM8E8WCc7jKzsZMDaz5ru0XNBHJQeiRtr5ipSXBUaX7j1R-sDP2VFy2F5zl2LjChdB8ePvgaMcYPh9HfYDHUKqSb04KQpgfzQg0xjqOtPmxs53ADUUmGlupjR3CfrI2MDgg8vqMTLSt3ZhpZ30Kpg9pX30NUF-1Hjr2FmB8N2DN2U4wxQwJzRzDtB9-vMW0gJLjwE_bOdwVWMfnB2w6cVysQwOXCOuqt2RVzMgJfYJWEnV1qJPgVPd6IHXBaQDV8nNmgQ2RX-e3r_33gEK-cvnMHvs3cMwt4UDlDqEypMws6fyjccPfhVp5k42kjx5mDh_tW9YVoJiItl13ojJdd5j6VcikcWBDGA7hrrYw_QWk00EdU1zCzP2fUrRYwb1mwzpufg9nI0prKovqFAnvibaIdYxX0bA1T2vswMl_E6KodBVBnTxR6ZpmETD-qLIq3-l2o3pyt3btXD9EjsDye6fi4e0JDrGB9Z_NVcIqLXtHpR3vz_fWMtuERU9nzbJiFfnzwarcjibmQ4qkDO0o9b4ahS1Kug_IHyR_biZdI5YN70PTr8bpnfrSlq8AVg4Rdb_jgJpdqdyuZUUdTtq9cZVD9njA5LNlqK-lDnACyXAifqarorIedprYPGLPL2EllH1QsC5ndtEKCv7dC_M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a16ec06f22.mp4?token=lABwlCKkcIDxgA7-Tlv37AXWZM8E8WCc7jKzsZMDaz5ru0XNBHJQeiRtr5ipSXBUaX7j1R-sDP2VFy2F5zl2LjChdB8ePvgaMcYPh9HfYDHUKqSb04KQpgfzQg0xjqOtPmxs53ADUUmGlupjR3CfrI2MDgg8vqMTLSt3ZhpZ30Kpg9pX30NUF-1Hjr2FmB8N2DN2U4wxQwJzRzDtB9-vMW0gJLjwE_bOdwVWMfnB2w6cVysQwOXCOuqt2RVzMgJfYJWEnV1qJPgVPd6IHXBaQDV8nNmgQ2RX-e3r_33gEK-cvnMHvs3cMwt4UDlDqEypMws6fyjccPfhVp5k42kjx5mDh_tW9YVoJiItl13ojJdd5j6VcikcWBDGA7hrrYw_QWk00EdU1zCzP2fUrRYwb1mwzpufg9nI0prKovqFAnvibaIdYxX0bA1T2vswMl_E6KodBVBnTxR6ZpmETD-qLIq3-l2o3pyt3btXD9EjsDye6fi4e0JDrGB9Z_NVcIqLXtHpR3vz_fWMtuERU9nzbJiFfnzwarcjibmQ4qkDO0o9b4ahS1Kug_IHyR_biZdI5YN70PTr8bpnfrSlq8AVg4Rdb_jgJpdqdyuZUUdTtq9cZVD9njA5LNlqK-lDnACyXAifqarorIedprYPGLPL2EllH1QsC5ndtEKCv7dC_M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🟡
اخباری سرمربی چادرملو: هر انتخابی غیر از چادرملو برای آسیا، حتما همراه با مفسده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/Futball180TV/97458" target="_blank">📅 23:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97457">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
‼️
🇮🇷
صحبتهای عجیب ممبینی دبیرکل فدراسیون فوتبال: در حال مکاتبه هستیم تا AFC برنده تورنمنت سه جانبه را به عنوان نماینده ایران قبول کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97457" target="_blank">📅 23:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97456">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
‼️
🇮🇷
حمله شدید بابایی، مدیرعامل چادرملو به ارکان فدراسیون فوتبال: اگر گل‌گهر به آسیا برود، حق مردم یزد ضایع می‌شود. حضور 40-50 روزه ممبینی کنار تیم ملی چه فایده‌ای داشت؟‌ اگر یک آرایشگر کنار تیم بود در آراستگی بازیکنان نقش داشت؛ او مگر شومن است؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97456" target="_blank">📅 23:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97455">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
فدراسیون فوتبال پنج‌ستاره ایران ظاهرا حدود یکماه قبل اسم تیم گل‌گهر رو به عنوان نماینده آسیا داده و این تورنمنت سهمیه که برگزار شده فقط برای ساکت کردن پرسپولیس بوده و فکر میکردن قرار نیست براشون دردسر بشه اما حالا با قهرمانی چادرملو توش موندن که ببینن چیکار کنن و AFC قبول نکرده گل‌گهر رو حذف کنه و چادرملو جایگزین بشه
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/97455" target="_blank">📅 23:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97454">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شروع بازی حساس بلژیک - سنگال
🔥
🔥</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/Futball180TV/97454" target="_blank">📅 23:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97453">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzU-SInwI8nLhzFpX_338KCg-vI0LHVzteyOuCPkErB4kBXxGXbw0Md227DelH0ZgFlJiY_GkzD1xGcy3_kelh4XAQ218s08mRnRAomMqO4DF6O70_JSEfKr8NLh0PDgsGzY0B2aQ1WDbUJ_wlXwHGZUDAFHeX7D13EYNqwRz0tMK8GKXWkZnywAQWl2xQo4txKbo3vxxXQi8OT9zNpWQiBw2kMp-tW1WgoMnGqgmHS9hc37gh0fiWOwiWSzntv6G5qlGnCxZiW65SWTLSj6i23xgkp4iuiyMLH25bYLxeCgF6nSa7msySd6NAD3mSv_n4as2rAvQDTXfc-ZzBc2sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇪🇸
#فوووووری
؛ لکیپ فرانسه: میسون گرونوود انگلیسی هدف اتلتیکومادرید قرار گرفته و مذاکره نهایی با این بازیکن برای جانشینی احتمالی خولیان آلوارز آغاز شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/97453" target="_blank">📅 23:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97452">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmtiF4_rCp7SV4KWbZfCHhherKEnBD1s7Z8uVkiD4op13CWOKsEmuGsa2Ord7JJs9atbV3LYvaehCHeanRSd_vns0JmX9nEyb7QwZYblCY_qm_aBSCMmtfaWoxfMSQEa8Hsj1fwjqw_pjRWytecqnmZouj0n4Vi_2f09wRckjhBvB2KM3bsaiuYm5NMSOpwfIppGaSWuCwOXItNofCGKsXhWboAgeEkr0KaFKd4bAC3ZVJp3dhs6FTvcRNGZIQx1FUbCcaxx9MFdgAc3rCIC9Ule0DK3twalEKl5rkbN9qU9Pq1_nueCAxFuSFx4369txcK-LZwNdD2FS7Sg8MGkyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
توخل درباره هری کین و امباپه
و مسی و ستارگان بزرگی که گل می‌زنند
: آنها همه مثل کوسه‌ها هستند... بوی خون را حس می‌کنند، سپس حمله می‌کنند و گل می‌زنند. آنها جلوی دروازه قاتل هستند.»
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/97452" target="_blank">📅 23:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee1b4fa7.mp4?token=barbeL7DTjRmlXyR-71T7aAgAorbTCOWH7kkqA-suIYjwcoP3UPszSIG6Ir5zN2gr2JvDroEmnHj5XC_OpwRRG9SB9tWMxhrPqvhsax4YdIkMkA44Bo_hatIEY_ddP52TyfyZIxEzljp_j8i_o35YDSTgpRzhHDmc3U_wV-09N9_DiJITUjHcI9P4hSaoPxX9G7m32mka8w_WY4j4QyouecAWYlCqRRsQ64RhbCg93UIHFIx93aexCjRirN31wl_wNgf8PvQEu6n_bDBvBij3djA3hrxIdv3wNFKwbnMc4YU-tuZ0gBZUq0s9wmUqHmXAW61dVF_a07C57TQ0r9leg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee1b4fa7.mp4?token=barbeL7DTjRmlXyR-71T7aAgAorbTCOWH7kkqA-suIYjwcoP3UPszSIG6Ir5zN2gr2JvDroEmnHj5XC_OpwRRG9SB9tWMxhrPqvhsax4YdIkMkA44Bo_hatIEY_ddP52TyfyZIxEzljp_j8i_o35YDSTgpRzhHDmc3U_wV-09N9_DiJITUjHcI9P4hSaoPxX9G7m32mka8w_WY4j4QyouecAWYlCqRRsQ64RhbCg93UIHFIx93aexCjRirN31wl_wNgf8PvQEu6n_bDBvBij3djA3hrxIdv3wNFKwbnMc4YU-tuZ0gBZUq0s9wmUqHmXAW61dVF_a07C57TQ0r9leg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
Senegal vs Belgium l
🇧🇪
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/97451" target="_blank">📅 23:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58bc4ce63b.mp4?token=hLEq4lUTPITProcruJmC4MFA-jXL0h4qmUxKgvpUZcZ-Iy2raVOZtk2-VHb9pRhrKF2zilAGJSoHIyoc-YgmIMTB7f5FCc5m3i8xy1ujSIUa5FO7W5oLW_2eaYB7IDMCgaBIzXa-qoWYeLoJbP1HOUGWky1nfV4oim7nt4U3oq04OQokjuuttah65tLVO7H8eBygxmk2W_-X6vg0dtPorTqKT6yjD80ix-FGg4HSQykiN-7KO8Edtg112XbEoMnLce7U-U9IybvXaVB3UMLMt6vwu1nBStFXX45HUc6tpqepitVDu0YxaVxTUOII_aanE_7YmUyXHXnZvj3lK-rJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58bc4ce63b.mp4?token=hLEq4lUTPITProcruJmC4MFA-jXL0h4qmUxKgvpUZcZ-Iy2raVOZtk2-VHb9pRhrKF2zilAGJSoHIyoc-YgmIMTB7f5FCc5m3i8xy1ujSIUa5FO7W5oLW_2eaYB7IDMCgaBIzXa-qoWYeLoJbP1HOUGWky1nfV4oim7nt4U3oq04OQokjuuttah65tLVO7H8eBygxmk2W_-X6vg0dtPorTqKT6yjD80ix-FGg4HSQykiN-7KO8Edtg112XbEoMnLce7U-U9IybvXaVB3UMLMt6vwu1nBStFXX45HUc6tpqepitVDu0YxaVxTUOII_aanE_7YmUyXHXnZvj3lK-rJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ارلینگ هالند 26 سالشه
‏هری کین 32 سالشه
‏کیلیان امباپه قراره 28 ساله بشه
‏لیونل مسی در 25 سالگی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/97450" target="_blank">📅 22:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97449">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxdmcfPo1qRYeRGaebOJX_FEm20SFNK_zsqKWG-VW2Inp7dlKB7-Z9SkX-PShSGcKlqPs_9lVpurg_UI5QPXxZJN7Vg2GD2fF9RLIZ2LfTufIBYPrlMpmUIq2m0QrTMIyfyNeXOn5yDgfgnyCX9GO75MlWxYweNCIR7nqJ-gejHSBDLDQjk2KmVey-KY7xZx81oV2zfVsjBsHwcrJgxXHtAUkrrOlymBDeiAlNOYPBD8nVmtcMK_DKuBjeBGaeo1l4jFnxZAJ-n63OKaU_C-2F_RJsqhQX95jTEi--JG_fJ6kK6bgisO_2PzTB_RmtrCX4fa58JBBqdNEpPpTbByEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرانک کسیه رسما از الاهلی عربستان جدا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97449" target="_blank">📅 22:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jNlN7KR1hT65z1F4XIb6lpqUKwl-ZSzZKNkGqntUMhJX0JYl-972Ze46TJVSiBYH5QLKAEphpJWFtz4pEJCQlOKIMgYcR0MXc4wdHt2K-P-6Va9yctOBzk75founnHg0sbWLaOtUGOpd-mOoVI4ByJ_WgMBh-4XjxNB3HXvUzRND5kXbT5UbCJRSB_fYf7TSOHIOxthU3WDRAWrZEbyq_J1o8Sf7R9Rhusgrt5fTGESpGt5HRitp6e98J9mHDtibxxYrjXSts-ulxiSG0cF-U_PP1IeI114NQtiCuW_wHDI8oLjioAESezqPY-9R6IrqYyvfVebNRWRpv-3pTAn_QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
خط هافبک تاتنهام برای فصل آینده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97448" target="_blank">📅 22:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🇩🇪
#فووووووری؛ قرارداد ناگلمزمن با آلمان بزودی توافقی فسخ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97447" target="_blank">📅 22:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97445">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/KHcLAZIABikBDTSVHRF5fePgFYfglLqd1TjSEs88EM8xM2lIwnJVUyJ3WRHlDqaBvZmvME89-nogAWeNvAJwLB9yDKijDiY3W70bgTraHwKHfpBTbtShDGfrcsiCTsU0Fm4RDaHcJk6vBw2U0KPcdEp870Li7mGf5d8bcvJ30QgAjqd-71w-8Glt8J2FVVOxxUbZ2pQG1gJ4doVxRxvfnhvdqWLxhXMD2eAU6XTrALuUxTfDfMvEhY_-vOVPArnPXm858dH4rKIpnkR0TEOlFzGUYn_gVOAvhbICMpt6-Vczz9GA1UWDivcFK-R8mQnH3iO7AH7plaxZVvOBpMik5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V4qyVfu5V2Ji_2TTIlThUAVz7V6xvW-8_rZ2PQpUt-Kz7vCvGK7oGJoC-_BFcrhA-ZoQBixAj813xBfJ2B8UrY2pFlgUZ-NrNb4mN3cGs8MxrERyN4XlE0dwpambVsiHNWEIJ8C8p4nUoIfZxmFlzemeCtbugGBojdpxs4o9VujS18X3jONeM2H2vJarqKJJBY0og1XaoIaUAlghUtktSKF4ojMBqb4hN4boZhsatPx8VqjYvhlyq-gmOhvzJRiBQsla-i4nqI60U9gkoJ07RvVrSDTCXIYOO5Z5Hs-WoGnSzjcWg2roWY3V_o1h55frWkr5SVOhmJ14xqLIFY1t6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🏆
🇧🇪
🇸🇳
ترکیب بلژیک و سنگال؛ 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97445" target="_blank">📅 22:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97444">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oT0KV_0dI9tetyrvTYC0X-C8B3a18WKs3NCSfGOk-MRWYutkeySyly0PyN6VLMsci5_qMjr0D5-cdYBPw6eWTZ4fWfal1ibLDdv6zMRgye9MR2f6hJAcNymRAZqfslpQOYMs9tnAkqxH9eXeH-pPYck8ZkxFD0SEMprFca8mjivvjqUbMIyHL2ADNvOF6RDvhvHdrJJsfZDCWEosy42c-I-LNJgGEXUEDf1J19kB9ObEWWXT6cpHmvYNnICpx2daT3drk0X9hbDrl7pzGZ50VNCATknX3ppnkxCmTFVqxQps32ZH4XWp7AbDcbcNX640FMfvdX7XWqD0kp8SGMve3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇩🇪
#فووووووری
؛ قرارداد ناگلمزمن با آلمان بزودی توافقی فسخ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97444" target="_blank">📅 22:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97443">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddt7qnrIC9tLO-Q-V_BG1kC-5-ybfj5Vf4vhNlI2AFreTzVGEp3tSrFsVfJCEDRQRdM3ibAIV8rfXNesOjgEoBhG-FaBvzvIxLTDwCN3luJiZBz1-6Cv25o5GZGksWCWy0PM2Rmy0LZSLn1hSIZ8S-sxBLWt74RpLQ4LWciqvOu8TL6rYAsVCn6gguFIg88oOCXAMrWoe1fliPZaeNlf7aU-7tNXaJCrmAMYLvSCx-ZpIR4jL2o_iCNeLq6oJUdTPDJOFRTTWQRA94CGhC9i2L23RPbXaABpNlATWiuBvMPt9Az6wxhAyc-fdUCa9YcW6UKVuxwcSzUESZ86dKmKZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇩🇪
گزارش Bild آلمان درباره وضعیت مایکل اولیسه برای بایرن مونیخ کمی نگران‌کننده شده است.
- شایعاتی درباره این بازیکن فرانسوی وجود دارد که گفته می‌شود نزدیکانش معتقدند او می‌داند که می‌تواند با بایرن مونیخ قهرمان لیگ شود، اما او این کار را قبلاً انجام داده و اکنون جام داخلی را هم دارد.
- اما قهرمانی در لیگ قهرمانان اروپا شاید کمی سخت‌تر با بایرن مونیخ باشد.
- شایعاتی وجود دارد که او می‌خواهد به باشگاه دیگری برود و رئال مادرید باشگاهی است که باید به پیوستن به آن رویا داشته باشد. اولیسه زیاد صحبت نمی‌کند، بنابراین نمی‌توان صحت این شایعات را تأیید کرد.
- با این حال، گفته می‌شود کسانی که درباره او صحبت می‌کنند بسیار به او نزدیک هستند. این ممکن است برای بایرن مشکل‌ساز شود، زیرا همه می‌دانند بازیکنان ناراضی بازیکنان خوبی نیستند. انتظار ندارم این بازیکن ملی‌پوش فرانسوی در آینده نزدیک قرارداد جدیدی با بایرن امضا کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97443" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97442">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ HERE WE GO
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97442" target="_blank">📅 22:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97441">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDRXknPG4Zsgdav7Ebh34sGTRFZ52biN-7wDpnCRwazTx1aPLwCzxzeX7NwziU4jfDpXziwK36DLtjVR3pxfqj5W1a313badhYO374LhmNOX0dHILViZ4ZGlj5GA4J_QLP_hdWh9VowX5Bsu3fHQTckezi1EG5SqB2KrYtqBeQDDFBT8zyFz4KMOG4QizKSGpQv86JPyeM4L7EAhMW3-3hc8Ydwlebysz2Cv9CUjfb_ukL-rb2W2f3DKaLQ4f3qa1p6tyOfltCpHOGZ7-a6912rM0QOeUvWjtQCfdabIpgH3YAkhA0KssnvFuRd5PPkgREZuSzGE3t7R9KpXNBh53Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
برترین گلزنان تاریخ تیم ملی انگلیس در مراحل حذفی جام جهانی:
⚽️
۶ گل — گری لینکر
⚽️
۵ گل — هری کین
🆕
🔥
⚽️
۴ گل — جف هرست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97441" target="_blank">📅 22:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97440">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Su_DTFhGhQJZCAeRjPxv9CjrAGhTuWiTKKutK3xUDwjAjfLUyITxZgTeMSKHJdvVEbAzWLiIzf51xtJ3MnwXk_gp6HQcwe9HKCttQy_FLhxSQyoPyo1oOyDIeWjqze4bIWJrLUsu1JnkLpJtw7tEjrj1NigVbVnMHDf71TLlNeulWnzVKGBbeqkMrNi6-L8RIhI4i-XEZj1HH17zySxQgApuAv8FodkGA8-i9IXstPvkDnUCUR53tWUK2NQHPBknzHzuOnbX-Nm0cO6kmTqBHnI6HSyQOvHswXxhSd1EU8yvTF65Q5Q0LigjSlk_FYnS_1dlJTYRszfWgtqQnwVoXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97440" target="_blank">📅 22:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97439">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv7YespFt7KXboy_WBKS1h7fYf3GvhE8MI-KSLN6HO-i8RXhhGxEUqGLBi5pGqBtbashEpnD9yy_DAx4MnzlnWUgMUkHbM8DBm5lmsbeZagfVZMoKo-07JJpdcxJhk7qFt3EmU86XP7__dWmh_QDGFgLXK79eJ5agpwAFrtvOEop7ugRtm_mG89aXanq8-wacVJlMgZak6EtbuPKtTTbs8DfLHBzueTH2xUjjS4fKsLOX_qD5sr9rcIyJyM6U5ikkmZchnoByvyZuRXF5HrdKxnHrMF-rxRWouRvk_rWgcZpRINb7U3kVJ7S9DfeZ3jhj2Kj7UHXdqpSZCgGMU7vdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیکتاتور هری‌کین
❌
کاپیتان هری‌کین
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97439" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97438">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5s2TGI1U_SM80m2t-noP3W7vuvT_PjCYhxfZq64DlqbB9escx5yyHDrpE9LD_Ren_IDhDUAsIAXXEgs8hKUVdcdGGo2OMUxFk5JiAk1e1tkMPmlHWpp2Myr0S-eBuq8L0gfRT0buLb_HAoY_oM91TMnS_FHHo7T-OoESeD6-FN92FNM2P7bwi-mZ_gekFM7jTpqQ9MdDYSRZcCGrF8z1x3P8MeGZ8LaVbh94ni5Czg3aYHSrF63BXRiIZIH2NgQdtHMDpdMbEDlKYrEnaS6vG8OpDPytb9AFAD5U-b2sXYg8KBAHAt-BD5wgaCKKhBNtSlTEy158CECiwLiWxH7sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
🎙
اشلی کول:
هری
کین بهترین مهاجم در تاریخ فوتبال انگلیس است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97438" target="_blank">📅 22:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97437">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5-Af8vimrR260e2C6AW5FIPYUwGWoiBsWPTOGWxtv78VYicT56L5ukonbFL_QZ5roSvFhDjph80FHy7wmdFIQa0zlX_8D7uZ3goqzHCfiwjLshsaqbnFUIVTGs-8QKNHBZcpqd0w-sDeCv23inadzAsMQ7pJVzqvKzBan-G9un9Arai402e8GIrgC5xC7GoFxTlW3KZzdrMQXV6Ftoly5_sWNUsM77CIO3wnNwSUCRs245RWuymSqahMuZkk2Hi-5ZNM9_tCPes_Tq62KGHZiSOYv4QbCFJzvUMyPRY17VvDhvAv0pORLhoGg1eUdgV5a5r9J-rRY1luw9FObWgrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
آپدیت نمودار مرحله حذفی جام جهانی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97437" target="_blank">📅 21:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97436">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/brhKWbBkCeaH5EWw-M5M7i3HODrSJbW5YxC3A5T3yQx4Irc2-m6TbcYCvP358zSnU3F-ocKopV1OWik9z67ftFdw5kP1x2gfkLx7YILGf5Ra54Sat9iME3qLnJYWOL28Gr5ZynLRXosW9DP1eyA4SrBzLy_wR3q0bp34A_NVuo5NtrmJal58yLjfHWt8WYYzloof_FhrWs9Pk2_DJb1KRfqUm0Vt9irhOOcqzi4CHTmFb1MLeh5uWcbUcoGm2qiNv-XTv5TsKY1tgikrqTyWFN1ht9QWpAElSV1iWW0t7gpHp74ZRNSpji2Vd4hDaiLIeTURYX6fM3PPISQynXaWAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار هری کین در جام جهانی ها:
15 بازی
13 گل
3 پاس گل
بهترین گلزن تاریخ انگلیس در جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97436" target="_blank">📅 21:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97435">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEo4d4BM2RYRDp744hmkWuTck_4v554VTfO6RobjTbv7Q9EuwGRaNeN8pFptNNsGMqSwtOiikOCJxiibUQCu8a7BskUAY-kbKdNJ_eLIpZk7AsMpgxiOIu34rkBbIze-R80884WcDXUqgkbRMBH7F3mMHm4Zkj4NXVQh72s8HSPVtMLItwj1DRdD3aYZDA2SWB-0aufgMUSmxCafsau_oAKYVjuKlOVoM3YnlcZC7FJKBdL4hvaHmyJOSkb8BU_IEQkqr2GC997JZli-83ClEuPCgdmA1Z7OXNAkanxTuDZWZB5eSoFZ26QSlWCXZccWQR9ltNCamtTXYYfEGwhHgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
⚽️
جدول بهترین گلزنان جام که شاهزاده هری هم وارد رقابت با بقیه ستاره‌ها شده.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/97435" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97433">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yeww7JOOemsI498xVMiubgaa6tDpvncV3oFP2OQ2dzkDRyP0OwNaBNp6HOZYhtqaIdKaFVNeVYlkC5WC7H3njUmWHzKTd-y-WFGcm_s2Bk4BP66Y0fBoe6NNehcmeAf2aV-xmOQUC06mDhH4KVrqj4CHRclDDRKFNXIS1UvxHqoFRhXHBgrtQXRYTa79uHuUUshqG3a8qaEpJMbcS2oVvwGI_9MxiOvoL_ViKqJu6jgFyn8pMUhZJLi1ETp6kRI3cAhFCuD-0gY_DIhYR1KtxiKzuokPOcArBfFhWllsqES5GhYG7OmsIARti87mJQawDhwSnBF38IjOQe_QSLrclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nFnSvTX9_PE5wQCAZd6znltTYhVAqM_FVbjHOcmdqQQ_0n2ZVFALNicozQr-mzWFftiSPrfLTnK8km2VmZMRd9YqYEB7X_L_A81gehMW3mVSeByJ9kkC8esL__0DW3whyOHBHJIU_8VNIEyyXwruxde8uMfTRqEi_vw_xVvTxswi4KiNAV2Pdz6ib7mhIFzQMtdGVsOzMHT952ralCbWj5XGz5w1wk8xAIekovHjGIMJsyvveEpzhYmsm2HZSALHjES9zOPmXMhi2lybuSIdSGVsYd7fwJupwq93dOKQxYzZttWbYgAet5RavgDsS99m51xzrWk0Sre7KFMw44PRPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
🆚
🇧🇦
🗓️
۱۱ تیر
⏰
۰۳:۳۰
آمریکا
🆚
بوسنی و هرزگوین
📌
میزبان در مسیر صعود یا فرصت طلایی بوسنی؟
آمریکا با حمایت هوادارانش برای ادامه مسیر وارد میدان می‌شود، اما بوسنی به دنبال غافلگیری است.
👀
⚡️
آمریکا میزبان صعود می‌کند یا بوسنی معادلات را تغییر می‌دهد؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/97433" target="_blank">📅 21:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fw5sk_A_8GrcIi5KhyLHGpq076d6cG1VDcOmhjdcBeJpy4ySKNv2D8ILkmL_A3-LFhDdUnAlIO8wvEamZxkhUz2sD19MQW-25eeaRiN2Vywg6AnqKRBvkJLVHhtiwFSymmb2q7-BN1sAhM5bq5IfWkRwbsgFAku9iwkPY4c56Sl3AmAoBgzN2UHgB_2WrBs-8ES3ieyfoOQQET8bkqJ65nMZIrYBBphg7VJv-cyKJuP-i98pTI9UYuS_VxT2-y7Qtj6_Xp-RCKGHRoeF3RCmMPfOKtxmFLNboCiV0PzmA2otNY_DtgF6o7_dzLyDuDe9trqD4gdUFs66ZCEyUX9u5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کاپیتان هری کین پس از پیروزی:
‏
🔺
امروز جشن میگیریم اما تمرکزمان روی فردای پیش رو است.
🔥
🏴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/97431" target="_blank">📅 21:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-ArUew_jh1p5pK-yYR1iulFTTPUBdzCe0eXEPckPbu88ZrglUuIC4z3FDIjLyJ3gA_CsW3Z0rU4MSIxnusfO6KWY2wQ7aP7_poXswew-GaSs3VO2FHNWSH06gYW0lupKxrg0EzBq02vZX-WgqtQxLVMPyKbpr5xLcayq63QutKWmXOh0zdh-DCLPloTdotBrlpZG71G0nC_yHdlIxOAmXKqb0YKcrmtLtnkpOXr8h04E7kTEHlSbiGzrfOsxRwXeq3l43s37SpWyxnruSeOEIdRRheoBL794b3AinHviN5NKk1g66KynJxUmxHjyv0kMdXaCffLnsXAnG_9QxH8vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴
آنتونی گوردون اولین بازیکنیه که به عنوان بازیکن ذخیره در یک بازی حذفی در کل تاریخ جام جهانی دو پاس گل داده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97430" target="_blank">📅 21:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btEc2_hG684xFtV8mczCDzLAaldyK4PvJh63mGZhw2yc6vQ7p4r5SsoKHuAyUXutTaUQhiS37zSaNbPg8TIy7FWwzAgp6k7GkXMGkprAdxWawwUBEWg0tOWai6QU9QlkzJoRQnye2NvEn3UzqK5wPi8hWB4UksvM0DrYlORVb5l6WSouuVQUVy8lKInVB4mZcd3_XBxKJeSrE08uMWWcESbpxzJjVwU6oEfMmYOMtIxFy8u78mNPfPP9FdHAFbvpDomXXAKfIXaInY54AYDz429cThBvJWiknUMgXQ1akQDo6KoWNGcqmdO2pdMEQRvnSHsaUSvIH6X0Y64Lp6ZBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلستان هرگز در یک بازی حذفی جام جهانی مقابل هیچ تیم آفریقایی شکست نخورده است:
◉ انگلستان ۳-۲ کامرون (۱۹۹۰)
◉ انگلستان ۳-۰ سنگال (۲۰۲۲)
◉ انگلستان ۲-۱ جمهوری دموکراتیک کنگو (۲۰۲۶)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/97429" target="_blank">📅 21:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHwZgMVClLUvISUp1hN341ay084x9tX5kr6dTkk7TKrYQJ7SMcfzzM0YipLZ4jagkuL8c8M40_-KGKzc8_9hvd4PxU7YiyiEq1BNm90-PPIp8tGuMG8zBRz4uy7X9JcPWCBrSeeQHLA6LGtUlm23qq1JxW1JnKc6x6RG6ZwO59V7b2Ilw8t0DnASt8OQ994qD2VM0p2ixa28g6BVx_xlTaQmfaPg-lQZorMXI_F97JC3y_DHugtdxG_C3IZcuUrVWsUUckIqEE1kRrSTBYDv-k2a8gLGFvWKLB5LSWfEFzvGIk5I8aAiSDaARoxkiFC9EiUccyECh1uBX1W0-7Zu0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤖
هری کین رکورد خود را به عنوان بهترین گلزن تاریخ تیم ملی انگلستان در جام جهانی بهبود بخشید (۱۳ گل)!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97428" target="_blank">📅 21:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9FSenmsAtUASLFe2st2BIXFVb-dY2202rRUZm-e5eQ2VyFWNeCUnXovdC-V6UZkojE-LA-cHBT2NEb70YfdXZdgVj5vBekr-nuEvxJiAFbRMyeTwXkM034BeEigO9x-2b2sLTa9hRE8Y7_NPXVI8BqtiIuZ0N1EVfMSGxF_AUubWHMaAE0utIz0XfLdj6GSNZ-e7_5xCThy9lj7kHRpbtvwbt3tjvIjM9z5jLMtLy27xgzEONOXQ1HAIXhsea_Oz-oFoy95bNpWBAWwgpksv0S5Mh9ZcQpRhw2pV7wGK66OsykTa4NYrI_xWUdbH8P8lFb8gZkKlf7nObyA_KIDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/97427" target="_blank">📅 21:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp6k9fmDt27CeTeZstNFK5tnbQdEMSvdxcLdFmdesLPjXqr5hqon8sEeZXmq_oUj8GwlV7ZgzKh62jUR-gVmGWclkX4O7idkjIY-aoytN4Y-9hmaAIzgXiuhtCAeOEvG5CXxHQBI60epuVTZDn3-p5fJixAAugrpmNCvytONThq6TOigqjiQ-8csN0gl5gcXC4pXIqMiUysCi90aJEJGHzBJ3sFPePTJMM8Am40aJm78EaoVoURR1i0v4iQFdGrE9M4dtqQofIez1jmkDMdn7qYi2NSoXadWd2Yrs4PT-dPNGmp2lc54LV6Wx46W6efQD_d0EydA2VJncgDPD7_SNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی؛ انگلیس
😀
-
😃
کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/97426" target="_blank">📅 21:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxyPuefDw8bUTcPU83lVWo0PBMEjDrXEk_mMfMEgxWAThwEWuUgY8KN76PGCqG7avq5ObIpw9X_M7ForzjxkjDwXdLPJzw3pvV12Iftka5G4Gexkrt-pCBbwJVP8_eNuIUHCf-KqXIE3mNSDfRslbbu5x9qR9cUCwavsDgfXYOwODGGF5XL5P3lQiK6QxUXnY9MtRlf03C8Z3RwF_1RwAuyzdl_rRUFmkY8Slf6k_1fxgQwoqCZlfNOYlrNj4SbckDqO91tn6P4qJ63cTQdgmo9ugm-stloF5W7b706DfCn2YJ79nQHiEQR49d7lV9fLzWvPqHg6vBDURGshuoqJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوردون بازیکن جدید بارسا امشب دو تا پاس گل داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97425" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/97424" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/exnSfqvCw4JBthE6JkwFjvW1-IHzK5biuA8jCnt_qSvLwoXFU8U3Dp-gi3vz5nitzTBw6rKTkC-3JMyDg6Z6NN9eHLBbpzZkAPF6CbUdQrD_cMf4PTo5C31TZMTZXRu8ksgZ7CVd-_M9kUq5Gbb6Mf-bnOWbERtTDFCbQG0c4ws0a2yPpfms53ehC2LBdozARmBntUpX90Ln8mSJkOn20uZBIPuyMySYpOe145T4QdWNVW852xCsosOp2E3Vt_oAZUrMAZCOCHSmuoNho1MST6GTBUh0_sALTsAuLqpANAziClybbRbROwuoSsAide_CYnY8M66R3DTiAhmvXtgF_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/97423" target="_blank">📅 21:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">۶ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97422" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5faa5495c9.mp4?token=O-4t6A6oPBi5QW6cD4BC1tpzdPPV3d3gonNPr1_BTrFQwyg1UeOEty6Qprd7IT2wU6JfSp5T-YMP7vheBVGfBwSdeuvUokNVqX_e9J5iga-RzwES8aKGMYkyHvFB76TRH20uf8eZA_FgCm_cz1JI_9wLDifBUV06pqHKZ-zQSUmVNaxWNw5pbf67OXXq8AkicwqpoAd003yKIPdpcFOoTpJq0TT3Nl8B8Q34Xn-IZzpksezu2MIS0Ow0WvCfMl9644mPlSh3tsw_W92WUMePMsM3ENGsi-h1kehKjWu9vyF8r5i50MxmPW3IuO98SbPhVXSlrobwxHiwyGlpd5an53HyV3t2l9m-QSewiauIrRE7ZlADhgHlZI2AlkNmlA9fT_l23H4tV22eTa9Ye-nC8WZJzjdssqBNJC5jurb22bceVQvo-R7NeiwXXoK83HjfGH2TRPCQXbB5XVEOdbei0_klJpo76WBN8EEnPCXTsjPEVVLAnJ_bhJYl93fid3aTCz8F1VXwVnAz6C4EUy2bwa-rUvjw3K1E20Vev57_L1Jh71ce5nUkiAHhflwxdVaEdPljAaW98XDjpr5_nM1PnsOsdyNVAC9PxJ9AK_G0e6SIw4xBWlWCv_299wj9qQt96Qb9gNiOvufOX90tFWtTCY6lE3JJu3mpQK2wLmXq1UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5faa5495c9.mp4?token=O-4t6A6oPBi5QW6cD4BC1tpzdPPV3d3gonNPr1_BTrFQwyg1UeOEty6Qprd7IT2wU6JfSp5T-YMP7vheBVGfBwSdeuvUokNVqX_e9J5iga-RzwES8aKGMYkyHvFB76TRH20uf8eZA_FgCm_cz1JI_9wLDifBUV06pqHKZ-zQSUmVNaxWNw5pbf67OXXq8AkicwqpoAd003yKIPdpcFOoTpJq0TT3Nl8B8Q34Xn-IZzpksezu2MIS0Ow0WvCfMl9644mPlSh3tsw_W92WUMePMsM3ENGsi-h1kehKjWu9vyF8r5i50MxmPW3IuO98SbPhVXSlrobwxHiwyGlpd5an53HyV3t2l9m-QSewiauIrRE7ZlADhgHlZI2AlkNmlA9fT_l23H4tV22eTa9Ye-nC8WZJzjdssqBNJC5jurb22bceVQvo-R7NeiwXXoK83HjfGH2TRPCQXbB5XVEOdbei0_klJpo76WBN8EEnPCXTsjPEVVLAnJ_bhJYl93fid3aTCz8F1VXwVnAz6C4EUy2bwa-rUvjw3K1E20Vev57_L1Jh71ce5nUkiAHhflwxdVaEdPljAaW98XDjpr5_nM1PnsOsdyNVAC9PxJ9AK_G0e6SIw4xBWlWCv_299wj9qQt96Qb9gNiOvufOX90tFWtTCY6lE3JJu3mpQK2wLmXq1UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌دوم انگلیس به کنگو توسط هری‌کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97421" target="_blank">📅 21:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97420" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دوممممممم انگلیسسسسسس</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97419" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97418">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هررررری کینننننن</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/97418" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97417">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگلگگلگلگل</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/97417" target="_blank">📅 21:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97416">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5851711fa4.mp4?token=aRUB1Fs7jWofzpxI3VP96KLGV-CEox4j9JQ6WSvUT21jQ0mjQP3hLkgLpnRRlXaOvS4pNtf0XiFBqQZBL8AIlJ5cM8ITpDFa6_cL2_XFwQzAu00GdpEIR9LU1ioRjnZLnRlxX_LWNSqFn0vqb9T3yP4FCsmfzC550ufpmVx57L79uMj3N_GDsrDxvrARcBfpYWbGuAVTRbXpTqf4X3jnxtesrsIu-4SAsOT1usOiUWKpQqV-8h1xl5dQzmoxnISUvbLnrcz-QBcWsGN4NX5NhsqnyIXGma2fscRMYUkHRo5DqVZ18WSmCDtRazn2XHfYEKYSMyuy4CFa2IhIrKgjpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5851711fa4.mp4?token=aRUB1Fs7jWofzpxI3VP96KLGV-CEox4j9JQ6WSvUT21jQ0mjQP3hLkgLpnRRlXaOvS4pNtf0XiFBqQZBL8AIlJ5cM8ITpDFa6_cL2_XFwQzAu00GdpEIR9LU1ioRjnZLnRlxX_LWNSqFn0vqb9T3yP4FCsmfzC550ufpmVx57L79uMj3N_GDsrDxvrARcBfpYWbGuAVTRbXpTqf4X3jnxtesrsIu-4SAsOT1usOiUWKpQqV-8h1xl5dQzmoxnISUvbLnrcz-QBcWsGN4NX5NhsqnyIXGma2fscRMYUkHRo5DqVZ18WSmCDtRazn2XHfYEKYSMyuy4CFa2IhIrKgjpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول انگلیس به کنگو توسط کین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/97416" target="_blank">📅 21:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97415">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شاهزاده هری کیننننن</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97415" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97414">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">انگلیسسسسس</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97414" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97413">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گللللللللل</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97413" target="_blank">📅 21:07 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97412">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYzcinkafQy2Pbxtcdnt3NbkeGAQpDJ_GCUjzIzIsDiun7GtXRie03y727Jia3zr0lOZwZi68rKOrJid3YroeFolY4YoSxjuEbZUOmjldBohtMZHcBPpD-Uk_NyUyOlq-aT-aX66LuJpj86n_TVh8vkqIMLnld8zqr5CpeEryCHT-lqmsgsW8nE7NjFVMQBhb83HcHgYlzDBK3Tw362O6bKEhPuJXxAQ227VJydknIor091SfK90WNww3MKNLX8Ed74dv__D6GkA1ayzKtS_18DSBaElbz5w9LKq2v5L2v3DPAgq_MBA8yfCOPtO3FkYrITJ0K8t8v88jIyiQmA7sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇩
گل‌اول کنگو به انگلیس در دقیقه ۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97412" target="_blank">📅 21:06 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97411">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">انگلیس فعلا نتونسته کاری بکنهه</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/97411" target="_blank">📅 21:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97410">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97410" target="_blank">📅 20:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97409">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITAMWR1SuEUquQIqrHSzTVjJG6ZSwSA8yN54iAJdMRr4cNLF4izNT724QPrkJ5T328JHRecB_kMIIea1Y9qTBQoYwKpHDl9RU5v-LEnf5iNyWCLltc723npTX_SEtPuHHeSGRC2-EHZknE_bHSn2pMK2qidiqCK1gZmb8vNTrEmeC0VW5qVDAdDMGl2Fi__0cB1IkSRYFPvEamaGoQ54DKAU5YfbSN2ZA5LEX89bQ2AY4YdTyndhXfKDZS-P82RwLjyg_gBgYP_HSzz_vHw0RuIj4VGFbekwgWR1Yn9eb1L4tR-fFaV6oLw1BuwsqrZfaihKFhVtvR6iP5UhQO6IUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقطه ای که گلر کنگو باهاش سیو کرد
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97409" target="_blank">📅 20:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97408">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممم مصاحبه فیروز کریمیو:
😆
😆
😆
😆
فیروز کریمی روی آنتن زنده: قلعه نویی ۵ سانت و ۱۰ سانت را تحمل کرد، دیگه ۳۰ سانت را کجایش بگذارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97408" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97407">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🏆
پایان نیمه‌اول با برتری یک‌گله کنگو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/97407" target="_blank">📅 20:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97406">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">گلرررررر کنگووووو بازم گرفتتتتتت</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97406" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97405">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/97405" target="_blank">📅 20:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97404">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=IDx2Ud5NDJO-nKHfwbExV8sCoidfbznJQqKbsPGXHhd1linFbtMhet-s7t_ZjRk50CD6gwNnYHOgfHoqNiBK4rkObQYHfndTeVTuP2-ADhYYBICspFiFFEyqzlWIgxd9r5rxpndTsKA0azOGrLEQo3agB70oUF8BX3PHDXcMYK82hHc9cxcOh8c8oX1c9hxNcNoI5xo7oU8oX8MuLXfDF5BgVTv0BwQ7z0M-F0yXgn4nEbRj6NcTkbwPccoC2DqVwY5f_wWTKSwJQOlRr72kjW00HjMaNeDwYJ5PN-VqbIRYKojqeI8RhIa2XcpR7gOxDTXvduR-0SlCiaADU9q3ng" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/80f7520ba9.mp4?token=IDx2Ud5NDJO-nKHfwbExV8sCoidfbznJQqKbsPGXHhd1linFbtMhet-s7t_ZjRk50CD6gwNnYHOgfHoqNiBK4rkObQYHfndTeVTuP2-ADhYYBICspFiFFEyqzlWIgxd9r5rxpndTsKA0azOGrLEQo3agB70oUF8BX3PHDXcMYK82hHc9cxcOh8c8oX1c9hxNcNoI5xo7oU8oX8MuLXfDF5BgVTv0BwQ7z0M-F0yXgn4nEbRj6NcTkbwPccoC2DqVwY5f_wWTKSwJQOlRr72kjW00HjMaNeDwYJ5PN-VqbIRYKojqeI8RhIa2XcpR7gOxDTXvduR-0SlCiaADU9q3ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
پشماممممم مصاحبه فیروز کریمیو
:
😆
😆
😆
😆
فیروز کریمی روی آنتن زنده: قلعه نویی ۵ سانت و ۱۰ سانت را تحمل کرد، دیگه ۳۰ سانت را کجایش بگذارد؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97404" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97403">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گلرررررر کنگووووو چی گرفتتتتتتت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97403" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97402">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">چی گلگلگلگگلگلگلگل نشددددددد</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97402" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97401">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97401" target="_blank">📅 20:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97400">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">رشفووووورد ریددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97400" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTYbcRo-MlTFeKE7aLDOu8xPB74dRMw3gkQUFheOfzwkWrb5yJ0h3OLZRCHffr-A-ijHGAcmU5QFU--ArNLJxGNhBPmw9XNk41pIbAIMJWPtKMJEVY9P3cdvChQ2wMQYvxuzQ68Yk8XeSiXvwuq_WdgLRuZVR9hs4bXVaVIi0LFSqIZISfHcDcu1Nze_mMoOE_b3NVjjkK62LrF5pD1LEGk7nZW-DVBia59EPJVUVMCEp8-t4mxABEz9szinWDarjQCAN3ByHX0n3wIYCJdKM3nv7HIcTN6i9zOVIcmFt08iV-zo7hwTQy_DrFgpFime4X-N0lEeMv-LWnqkoiSnsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
👍
بوووووود یا نبوووووود
👎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97399" target="_blank">📅 20:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نگرفتتتتتت</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97398" target="_blank">📅 20:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خیلی مشکوکهههههه</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/97397" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97396">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">داور تمارض هری‌کین گرفتتتت</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97396" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پنالتی نشددددد</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97395" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">انگلیس داره گاییده میشههههه
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97394" target="_blank">📅 20:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97393">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">کنگوووووو زدد تیررررررر</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97393" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">پشماممممممم</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97392" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97391" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WpWOFkzC-mYl9jkVn1r4dI6BlAL7OB-K4e3XGGSZuXN2q9plDYtVFSshbNLEtsSAhe6e80gcK17aoTTpn0agMmkgV7YrDb5COJvafr9SDuWTQrVuXeJsNP3Qj3PJWYGYBCD9EqxyyCN-Ud9rzo4De6Gvq2uFiUxExCDSvTI4i1cSET9bDPuF1n2hYBMhQY3x3p15unhZLrTQby6xqS2W7lslGYOtfxUEjGL-NcogA3O-_QZLKt7Y_w3C7RGWTI7UECjKbOc5oGr34vSfpcYGRqouqqXqUKDZfRAXDXr4XeB5eMlZ9OrWzBKd4h8a8XceT_V6fRvNUPlsF2zngq4Dhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
رشفورد اینجوری ریدددددددد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97390" target="_blank">📅 20:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">کنگو خیلی کیری سخته
پرتغال هم اذیت شد جلو اینا</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/97389" target="_blank">📅 20:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97388">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چه تووپپپی از رو خط در آوردن کنگو</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/97388" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پشمامممممم</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/97387" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">کارت زرد برای بلینگام</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/97386" target="_blank">📅 19:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97385">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این که کنگوئه اینجوری حرامبال میزنه حرامبال کیروش دیگه دیدن داره.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/97385" target="_blank">📅 19:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrWouK0N7EXM3Zh0w-bQKcehZVCZU2NQ4h8s69Xq1Uyj7xj-uvGhq73XekaWHeneXVc5JX_RN2C30cM9hnynFQ6dJQfB88gBV1lJPJ9NlEEgvyKqWgVuWMICC-12Wse7daxGSJDNt7rLqkStNVckIf0HHImJEYSgRClXpgc9lDK-8U1Joged-AhYDEX_4Axk5uaOFtJSQVTo8zX4GbC8-M1ci7_p4jYzhKqlInh0xETcCYs7-mBvwkktCllbnwfj3wuiW4_heHBcls5qvhORJUnm34_foeeahNkV0_VCRBo86Ys3LMMvy1jgJYgqBnVE0SPNWJgsK5ajrk4aKhgQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار به روایت تصویر:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/97384" target="_blank">📅 19:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/8df51f9cca.mp4?token=R52-2GPbOiiBc7vq0HZZokXbghbDr4H-IGq6jjbXWsSX1z-NvuWS0Lu-nCtoUwX7Gyw_mJbXsLrvJcQ95MJyRqj2e2cNP3xjpn5otka5HA9AD1R3s36AHWXVgW0wBVuEu-WrDbaOu6-nUHa64IC6MucQOPct-1H7lpnc_YKauPG4Enut_vPzZljWNYLIQePhO9WKL0sxU7DdvAFKRMidlV3TaLQRWnTvvfyythGj9kuIwxuGhkuf3ualX6WBpw2Ct7vMQP7ada7Bu5RSGCP1256XMgfpniTj-Se-V3kj3W3H5UywM4v-w7wCeuwaFLkOSZrx9fRXI411i_amvtZ50ws1rOG0axaL18RimcVCTX6cOFE_VxdwTh3vMVzw1cQIFT8rUBA5sGoTxCtgoTZ1G8gfOVZq06vZU3F_fMqPq0BaOuf2reb_m4EIPjrBKJqkSJ84e9Bkl8at5YHnSKHdo_UdDTYqmGzi0k8WDl-lFRHImLUfGE4u-hhtA23LTOTtZerE_a3uZf1RtnTGCcxIIPKuxsAgrdkEQfj5W25XVcQIJi2tMNKQVh6mIR9wQ1mSpBd18XkuMJ4_mYmmMuzBj5v_flyl9-fLCNcahhnH2qdZ-vtRkt68X2tYoC4YRnfhVasS71hzXlxtIypK3Q68ZwRrIhHi57JDPiaOrif65sE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/8df51f9cca.mp4?token=R52-2GPbOiiBc7vq0HZZokXbghbDr4H-IGq6jjbXWsSX1z-NvuWS0Lu-nCtoUwX7Gyw_mJbXsLrvJcQ95MJyRqj2e2cNP3xjpn5otka5HA9AD1R3s36AHWXVgW0wBVuEu-WrDbaOu6-nUHa64IC6MucQOPct-1H7lpnc_YKauPG4Enut_vPzZljWNYLIQePhO9WKL0sxU7DdvAFKRMidlV3TaLQRWnTvvfyythGj9kuIwxuGhkuf3ualX6WBpw2Ct7vMQP7ada7Bu5RSGCP1256XMgfpniTj-Se-V3kj3W3H5UywM4v-w7wCeuwaFLkOSZrx9fRXI411i_amvtZ50ws1rOG0axaL18RimcVCTX6cOFE_VxdwTh3vMVzw1cQIFT8rUBA5sGoTxCtgoTZ1G8gfOVZq06vZU3F_fMqPq0BaOuf2reb_m4EIPjrBKJqkSJ84e9Bkl8at5YHnSKHdo_UdDTYqmGzi0k8WDl-lFRHImLUfGE4u-hhtA23LTOTtZerE_a3uZf1RtnTGCcxIIPKuxsAgrdkEQfj5W25XVcQIJi2tMNKQVh6mIR9wQ1mSpBd18XkuMJ4_mYmmMuzBj5v_flyl9-fLCNcahhnH2qdZ-vtRkt68X2tYoC4YRnfhVasS71hzXlxtIypK3Q68ZwRrIhHi57JDPiaOrif65sE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇨🇩
گل‌اول کنگو به انگلیس در دقیقه ۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97383" target="_blank">📅 19:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97382">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">چه گلییییبییییی پشمامممممم</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97382" target="_blank">📅 19:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97381">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پشمامممممممم</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/97381" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97380">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">کنگووووووووووو زددددددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/97380" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">گلگلگلگگلگلگلگ</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97379" target="_blank">📅 19:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97378">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏆
🇨🇩
آغاز بازی کنگو و انگلیس</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/97378" target="_blank">📅 19:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97377">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBLaZ5QFZF1Nu9Vr70jNhOZ0vfoGmJcPV-lbGFxJNts_gZVygqwoocah1UlJZKy1AyR5l4ppstU2UCPRqabLksNSgFhr2LcxnY2CB9IeFtmrekyJMV5a0TdYryoKA-XhTAX4ZMyOomIG0yFj1fD6detdM6AermuxQt1_2xNvjXCGmNYYraXePcFYgaJZed4RZYr1wjeW7hvqJlSLAx9DXauX4GBBPvZjxmisyQB251B0UgRCILojrhYBclOHhrUwBQV1_Hf7IGu4jT6Vteeo4EZ7XHkYntp4T1p4Lt_FqoTxY8SDAdAIpZXXU_oRrOu37NNrE8C55BPuC5yq1IRPBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسماعیل سایباری رسما تا سال 2031 به بایرن مونیخ پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/97377" target="_blank">📅 19:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97376">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84477c6b89.mp4?token=j4ov24JTOopRex2IdPJwEq0_Crj0mRRc8U0xIgJ9WKdtqeWG2y1bTpO8PC9Nh5_L1tsbTgx1Q2axHJr8vy0guhtCDCf6VX6zJke10RAYUsNKgZ_7t4nHxHjXwW9VM6hsaxIuBaA1JkvU6J6eQBev1GsLVmIdOE8q0YsTOy9vSmz36mSOiSjC6Ye1iZCUSsNtswFvJS78olr6Q1a1yFJOa6xzFYufGOCdabW_yIYwjC5dqNcU5hShTCISsOutF6nvTV07hrQig6J9AmFzKSXV8WlL4lXsgNWkb1kC0NiHgKO7-37mRrzKabu-uJSWHyrgzBTp-aB9ciFrOZGcsso_AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84477c6b89.mp4?token=j4ov24JTOopRex2IdPJwEq0_Crj0mRRc8U0xIgJ9WKdtqeWG2y1bTpO8PC9Nh5_L1tsbTgx1Q2axHJr8vy0guhtCDCf6VX6zJke10RAYUsNKgZ_7t4nHxHjXwW9VM6hsaxIuBaA1JkvU6J6eQBev1GsLVmIdOE8q0YsTOy9vSmz36mSOiSjC6Ye1iZCUSsNtswFvJS78olr6Q1a1yFJOa6xzFYufGOCdabW_yIYwjC5dqNcU5hShTCISsOutF6nvTV07hrQig6J9AmFzKSXV8WlL4lXsgNWkb1kC0NiHgKO7-37mRrzKabu-uJSWHyrgzBTp-aB9ciFrOZGcsso_AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇫🇷
تیری‌آنری: حرکت دیشب دشان موقع تعویض امباپه نهایت بازیکن‌سالاری بود و اگه باعث ایجاد دودستگی در تیم بشه مقصرش صدردصد سرمربی هست که به بازیکن فاز دیکتاتور میده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/97376" target="_blank">📅 19:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97375">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd23d495ee.mp4?token=aasjTBubGK8Nt20tFZyqJrOubJD1Q5G8ZkA3inean-ldMwU9FR-YbzB6r-FTEX6SQf6wWPtCuxvW93pfcQ2felLWX5BZGdIZqWl0XSiksUuLa1nD5mtsA558_pIbcxHR6jAcoBSSYoKyu3dKgwBFn4JliUQnAwKn8gfxAsAit31rlnMU8UvZOubALko_93mm8NLQ1Cko0vJCFXnu8iwHthp19ESUs7D52C7juJRrZEuIzBJQplSWkdFmerebnTDa-wk5ESyvV-CViSrHt-HpAYcAk59Wp8PvRV-qmyKHpEL71a0mK9wN1s71DkHMal9fxNEemrM1BVLDJZxTZRWf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd23d495ee.mp4?token=aasjTBubGK8Nt20tFZyqJrOubJD1Q5G8ZkA3inean-ldMwU9FR-YbzB6r-FTEX6SQf6wWPtCuxvW93pfcQ2felLWX5BZGdIZqWl0XSiksUuLa1nD5mtsA558_pIbcxHR6jAcoBSSYoKyu3dKgwBFn4JliUQnAwKn8gfxAsAit31rlnMU8UvZOubALko_93mm8NLQ1Cko0vJCFXnu8iwHthp19ESUs7D52C7juJRrZEuIzBJQplSWkdFmerebnTDa-wk5ESyvV-CViSrHt-HpAYcAk59Wp8PvRV-qmyKHpEL71a0mK9wN1s71DkHMal9fxNEemrM1BVLDJZxTZRWf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
صحبت‌های عجیب محسن‌مسلمان از ازدواج ناموفق و دادن مهریه کلان در سال ۱۳۹۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/97375" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97374">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NE3Q8E6KXf3ZBP7FoQz1ebENoA0PcIgFRGIX5vciqf6_TZyZrL54iuClMLBBE1aljsoFprJAQ85sUYKg2Tm4-sO6r0OsUThwnRbhJFA_rNfznSUvzc5n2-VijL-Fe5OCtD9D0lcmZgJF2VcnKAiQkCqZ5WCGO5MlhUTZo9gYQsn5ookjl6gvKXRSX5lHtmihc6JrTRh0P4l5YjqeRfXdDXJaDGJAteYGHNcaEtmBR7bfU6ZV01WD5_ojZ9ZoLmazSTtTX2XkBYX6qpcTw9irS90PBnxc47RHLLua_GC6QOmYZEqHKnbtmfQtPz-4GmPPOjaZPCZGgGAp6R7oqPHmzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده تام‌الاختیار مدیرعامل باشگاه چادرملو اردکان:
اجازه نخواهیم داد حق باشگاه و مردم اردکان ضایع شود
به گزارش روابط عمومی باشگاه چادرملو اردکان، امیر سیدین نماینده تام‌الاختیار مدیرعامل گروه معدنی و صنعتی چادرملو در باشگاه، شایعه معرفی تیمی غیر از چادرملو اردکان به عنوان نماینده سوم ایران در آسیا را یک شوخی بی‌معنی خواند.
سیدین افزود: مگر می‌شود فدراسیون اصرار بر برگزاری تورنمنت سه جانبه داشته باشد، ما را مجبور کند که بدون تمرین وارد مسابقات شویم، چند بازیکن مصدوم روی دستمان بگذارد و در نهایت بگوید این تورنمنت بی‌معنی بوده و تیم دیگری قبل از همه این ماجراها به AFC معرفی شده است؟
سیدین ضمن تاکید بر دفاع از حقوق مردم اردکان و استان یزد، افزود: مطمئن باشید ما زیربار چنین ظلمی نخواهیم رفت و نه تنها از مراجع قانونی داخلی و بین‌المللی پیگیری خواهیم کرد که در مورد ادامه حضورمان در لیگ فوتبال هم ممکن است تجدیدنظر کنیم.
سیدین در پایان تاکید کرد: مردم ایران، چنین اتفاقی را به عنوان نمونه‌ای بارز از بی‌کفایتی مسئولان فوتبال کشور به خاطر خواهند سپرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/97374" target="_blank">📅 18:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97373">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAjUNyEOCSERkAAzSkVfVlnoj2ke9pr8N_nn49FER30P7LEuqKcTWo-jUBNSSMnMZOBC6Ltp-lGyWzN-6x6AjsvxFOIo2bOMvY63WzxuWV0uC-gxBmdY2ccAmM5iGXfxQaN__bGeBXd8xJWx1ALg3a1nbmfefEFD89jCTaWvIS96IPaxHakmT5ZsWeE3ZajQlCbQtS_S_1jYyTEfSId7ENgcwMDEDHxwjGUKFHrZ2UQ17_rs70RDvWmXdHGxWNEwPQvwJmWX2wUFTSjHFrOhSP2IwutV1KcqGHEtv1SbwF0fOc2vPXkm57MwFdDicttO2G96nSNh8EN6pUqZcyaNiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
آپدیت بهترین گلزنان تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/97373" target="_blank">📅 18:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97372">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlxH1IDAsHQlD2yBD1mQMnDQdjVXimhoAVn71q4xLDMXs5DGTG05oIz8r2oEFe5EvRLYexhMxMAie_37Y-G37fh00EkHZLnypph4TOVKxtYjH8I1OAoxCnwGi1ItDYlt6L19kvJ9mdCYA051z_KFEo0YXGb9t1eK76kzEyaNHpGUEVGJmxwN4i9a9-4eEl0azv-im1Vm0VUba1FWAMpXIeQ_-JEnsP5kjCmfVnQKkfx_dCUTU2muO8BPWIVtQgZnuWWuLYCaNycWFq3A2p0dQgzMxsHuPI7X4K-KtlrSKnrTgbJ7hRZxfiy9sIpPuApLGSXHnPBAn-KHA_isdtMGaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
قلعه نویی در بدو ورود به فرودگاه:
دستاوردهای زیادی داشتیم و الان همه دنیا درباره درخشش تیم ما صحبت میکنن. گل شجاع صحیح بود حقمونو خوردن، با آمریکا جانانه جنگیدیم ما عملکردمون عالی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/97372" target="_blank">📅 18:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97371">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oScTPRhSd_1HA8BADmtI8qT8uDBeyBQmzV39rc8azf5IQWH5xDbK78Zw7btWU-QmP7A_1Nx_a4-NFAZMScuqRX4Ph0LSXbdWbe4_EOlaqht-NfPS_gGdC1K1fM89xtM4ujbWA7X1kpI6B_Mr7WWULC1CoZ05BfFffSeY8vaWcYMDIl1I8DUxJic_6l7mcBnkbFF-MoqjKno1vxulBJ_bI_0MwQ_y-dcWduh5iEwaLQTd1eKWQ8MYfqSrI0vTjUdIzSWzHgJ8WRvvd9gJBW_Bk34pOlX-_4BaHsSwERZEMzepKimGwgrDHo8FhivN800i6c7LSyLmRYmIDriysGLWWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
مایکل اولیسه فقط 1 پاس گل تا رسیدن به رکورد طولانی مدت پله برای بیشترین پاس گل در یک دوره جام جهانی فاصله داره. و این درحالیه که ما هنوز حتی به مرحله یک هشتم نهایی هم نرسیدیم.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/97371" target="_blank">📅 18:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97370">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35fd6c28be.mp4?token=uixEZAM4jGyfu71S07Z_infGLLvvwxv1KqiVXuFvNnrp2d5EkNmVOOy0iYR6utQ40zHNJ1VrufBthlACnWlBZ5q74ql9FqFRtIPiP7tQRqsi8itU9bj8pjsRc_GdjdyKOGZT2Rznt8lpMTNNfi3yM_a7VvqaChTkVTG_KmechP-ZiJR98uJmQlm5d6ZCavhW1Jx0MV0_xPNudP25QNHmImHzskfmLn_JZFXSmbhFOAiDQ22ZOltz2vIA9qBCZY2vdelrAPuxOjyoAUndMXvpQ8FtY0MMBT3HKIgabqQSUFlBJxCfbqtOsRMhvswv_o1C7mOBQus884_Wj_GY2sYFOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35fd6c28be.mp4?token=uixEZAM4jGyfu71S07Z_infGLLvvwxv1KqiVXuFvNnrp2d5EkNmVOOy0iYR6utQ40zHNJ1VrufBthlACnWlBZ5q74ql9FqFRtIPiP7tQRqsi8itU9bj8pjsRc_GdjdyKOGZT2Rznt8lpMTNNfi3yM_a7VvqaChTkVTG_KmechP-ZiJR98uJmQlm5d6ZCavhW1Jx0MV0_xPNudP25QNHmImHzskfmLn_JZFXSmbhFOAiDQ22ZOltz2vIA9qBCZY2vdelrAPuxOjyoAUndMXvpQ8FtY0MMBT3HKIgabqQSUFlBJxCfbqtOsRMhvswv_o1C7mOBQus884_Wj_GY2sYFOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
🇳🇴
سوپرسیو گلر نروژ در بازی دیشب از این زاویه که واقعا فوق‌العاده بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/97370" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97368">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sR5HYXq7BZHrBtDYwLuUMBi2pDd-ck1l1jU-zfbNAyMqHFRc2igwit0IoPJOBESNDAfZRsTNlXnjsYJ90QyP_tGsbIo-Fc_xVL1wsqgXl-N1OC0H6vufxIy8TpPwKrs8kubyDoccdiLLuQwOTC83LMsMIRGzcbBOeth6oiuPEPt0ldSOY5CDWncjcJziu11iUYUak48MtX0Cna0aEueqDWd47ZCKPeNKtDqXZ_WXE_raJvvim3l9RmET220W377uf6nYiZK5Ionoqxpg5kPkd5bnS9XSm4FGDPXPtAchvkgq6zKnjcd0GainW85f_5LdjvVmvBgZt1ZRfOOzTuYLUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HBgtgtx6N3zBrnATcFS0nXk6i3w7TkuQw1vm0qaTrjgq-0KuGTe97gyPUvpzlm5DXTOrgpsRBWsfJi3Z5G18ISm52YxbRzrrsqKTa-OMJVrwQM59V2dT4vgdhxYw5fEbLQpnqGYjHiyTHPISUPHl0KguXqmksmfl87QdhUbFgc_ojMR1TclE0RGAKXLwYNplUEk_7pxrYEkjWzlOa1syA93aOf4Fx7tPTv-ESm77JJksvMWcGMVjPbwkp6SWqfuUJb_qtAFadKBFfekMhWp2d5ATUNuRd3jQuMm7GE9qGxDdKXmHJvDvxwC6_Dy5EPXGBHCfrPDbmZCM1OwdYJBJ8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇨🇩
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس و کنگو؛ ساعت 19:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/97368" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97367">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/97367" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97364">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d8b32dc.mp4?token=q9Gz0WtK5QVdsP33dX6HqKfYWwp8QmolfP4IFsY-ZUBbjIpw16O7A7uYndUeq0E3pPxaDNhiCW0gdE-HkWv7K4tIF2UHXY0OpMyNv4T7fWX-HcpFdIHHQ9L7rGlnp_3Q8kBUEaasbnUInFos5GG9Wfw-ujfwkCnnx0sN619vpqocCxqDfuURyZep4vJGX0Y4MzzK2V14YXEuwedX9_OMin3vQzfjof-w2qOfFEdgREglngw9KU5InW5kfm3PjckkpMbYs1EcInVgRSEYS4L5ZnkaEkIEDOhcwEXKCKXV3_IqkpenwSmPitGIYCPfvYhMukY8dN9WtDyb49Tm4A7rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d8b32dc.mp4?token=q9Gz0WtK5QVdsP33dX6HqKfYWwp8QmolfP4IFsY-ZUBbjIpw16O7A7uYndUeq0E3pPxaDNhiCW0gdE-HkWv7K4tIF2UHXY0OpMyNv4T7fWX-HcpFdIHHQ9L7rGlnp_3Q8kBUEaasbnUInFos5GG9Wfw-ujfwkCnnx0sN619vpqocCxqDfuURyZep4vJGX0Y4MzzK2V14YXEuwedX9_OMin3vQzfjof-w2qOfFEdgREglngw9KU5InW5kfm3PjckkpMbYs1EcInVgRSEYS4L5ZnkaEkIEDOhcwEXKCKXV3_IqkpenwSmPitGIYCPfvYhMukY8dN9WtDyb49Tm4A7rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇫🇷
ویدیو وایرال شده بعد بازی دیشب فرانسه که رایان‌چرکی اینجوری سرمربی تیم دشان رو دایورت میکنه و از دستش عصبیه. دشان هم هرچی از در خایه‌مالی وارد میشه جوابی نمیگیره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/97364" target="_blank">📅 17:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97363">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnhQagkc2Oy0D9d_SbpqyRUYlpVOetZBMmkiyFRuSVrTwG6TUKXkfho1zDfA9foeaA05kF97uenc2hujHFn9zpRmzULxb5rz9mJq-n-iaxEkXRWvyCXkkPfZEpnRjltwl4xxh0pI2wZI8TVTgWf-2J07lUFNF_C5pjBtRXmGVkDZk_j1kCTcY-feiuWPtVjRYXSVVugOWAnasPvPEbtWYI6rteYxtYlAMFNaUzf1-lC0QWv8M1EKpBCkTgAO7yujVgg3mOFyycrANW8yQROMZc6vUXc7JP2y6qhNTl0dRBQn3I4azencMWzH1Ih-JuVcm2ATEfbAdYfO-eGP9o1VzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇽
دیشب بعد از پیروزی مکزیک مقابل اکوادور و صعود این تیم، 1 میلیون نفر میریزن کف خیابون و جشن میگیرن که در اثر ازدحام جمعیت 3 نفر بر اثر خفگی میمیرن.
💔
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/97363" target="_blank">📅 17:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97362">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ggloygx2QmfQvKQKkzMGli025P4WQnlHgGTiLWDB2Hm8seyEtDBP2tjB-PiYM8fyB2KUYwZMPk5r4dLCt0d-OkeO-O7y9UjgZMb-8roIoSVfeU8RA8_LGwwK9sdYGScKwhj1DiYJRZcQS68am5orbq7rBGfu4a_IC9-dqgSaveuATr9WwzFcmqTxt-KqDl5StucB94_DfV0qpwwBbRWo7ftFWtS0V13x7mHMv_GviP2PaQsxTHtTwJepe-gql1wbaa7CBeRNNTMFnF7Q_Lvz1s8DJxGkGbDFgCWoLcj6Y_kwxIEXXdF67LvmabcKJS4UVZeM9LVEnDokb-uHnRZYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ ساندرو تونالی با رد پیشنهاد هنگفت منچسترسیتی در آستانه عقد قرارداد با تاتنهام قرار دارد و بزودی رسمی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/97362" target="_blank">📅 17:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97361">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=fUmoZpWiYozOqK87gFrUUievYovwXcEaNkUwVSy4q3PmcPSwip9qqDFcshD2-MeF8yxnXOAf8o-iJZHpMgBvdse_QoSB9qKssp_LXc8jZBTj4KECuzz9h4zBf9S-FO49gdYodZ1vyUeiB4gOsGsCKY-7gCynh5T1U4Gkz_JBjH60Ro1HS990s83B2CuXpjpLAdNLjhWHTDuM2zz1bM7T_ogJJwrdQ8QsuouOelDoZWtPnDeIe85xxvy2UBkmj5FNUgfg9ObcYstk12_70854lBYd6p6U2AMXY6Jx-49yeHolsVD3DoxKNnAMizqcqWpx-oSUawOQ4z4IoREiOYRZGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ddb483137.mp4?token=fUmoZpWiYozOqK87gFrUUievYovwXcEaNkUwVSy4q3PmcPSwip9qqDFcshD2-MeF8yxnXOAf8o-iJZHpMgBvdse_QoSB9qKssp_LXc8jZBTj4KECuzz9h4zBf9S-FO49gdYodZ1vyUeiB4gOsGsCKY-7gCynh5T1U4Gkz_JBjH60Ro1HS990s83B2CuXpjpLAdNLjhWHTDuM2zz1bM7T_ogJJwrdQ8QsuouOelDoZWtPnDeIe85xxvy2UBkmj5FNUgfg9ObcYstk12_70854lBYd6p6U2AMXY6Jx-49yeHolsVD3DoxKNnAMizqcqWpx-oSUawOQ4z4IoREiOYRZGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
😐
دخترای کم‌سن‌وسال با دسته‌گل رفتن استقبال رامین‌رضاییان تو فرودگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/97361" target="_blank">📅 17:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-97360">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hoJqMhBLvEh1ZxAhHVo8PX-6ugAGYHINNFDj4t78ZRIRbJiL1-BvEdQpAAoBIO7JMyPENbEzA8vUpf0vqRKZfnfgds8CAgsh0-GLEj_28dgUW4fmLeUL1rI_GtAk-LlMfkOxkyube7Nn0OHbkAINpHvX--o1QoGUyDqL9vfeWUeVNfwOxGN6Hu0S9CXq1P_wlE0lrdiPAbIpFoJzKv2Xh4CE-eS93QJqyEfro1CZ60tPNS-aMzoUfDRRGQZbXlf8HBE4viZcy39fHBIJoQp63Ml0s-e_nUKGhefYr-Z7ACiTw68b4cK9qIRoLpVzfqr2X88u-vVXVS8aeJVcGWoclQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
#فوری #اختصاصی_فوتبال‌180   باشگاه پرسپولیس به ریاست مدیریت بانک شهر پس از شکست مقابل چادرملو حکم اخراج اوسمار را صادر کرد و بزودی این خبر توسط رسانه رسمی این باشگاه اعلام خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/97360" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
