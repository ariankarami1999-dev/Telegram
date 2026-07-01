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
<img src="https://cdn4.telesco.pe/file/tZ1CiN2Qtmi1p-7tx9iFkCrLSN0ZyybLcO1J49ho7ZJHIdzNTU-X7cZBlxC8xryoYRAQBxRm3I0QZTQ_f4zXJnZKE8KyFe--_12N13iVYz49FGHAMbBh9n63JfvePFo_MdSMWZFhWZS_5nc5p8pCnzPAhDz20zJyhv_RKapKNTDPc-z2Ahb7EkLHaO5DIhchLR6kDkZl9kq73MXUnGOewshSZER5N5_1rwIA4B9YBdijpDB19nbcoAOiIRaX73WORcUGYPX5WqqSU0PX-HCO3QfwiQQ0eYMvtL9_1zKz7kmkDjSSdoImkDHfS_vGfCfQcJTCEZXRfxFTTRJxIo2oBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 355K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z46iLgyDfubLh61UGJFX4MvZTALScrsF-JS6Z__d4g73TNDpzivcH-FxKqcl7E3EgZBWw3M_lDZ7JyCY8ALXAd7okLhXJnt0INxRiO2Dzf4Tbm40Q1BYBOJ8q_HXZIV4IJcwhMwV-tJNWaw7KQUJVmvlkL9PMiv-zCVIQRWx4UW2R5MujcE3e-XP008Bw2RL8_9njrzSd9NyWdzBoAACBrLM7Q6xuxngeTWrxCKagffJtXbXbM0NMUaX9vH8fNqD8e3QdQA1Wr6NK_lYe_SiiIBDH8X4II_SSSaPrvZAzlkzzt57P-VKs7Y_-qlY9Yrerf_epDSCfv5GgzEIzhW2AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_NRjHhyeueiwmdJCNgOrRnoy-eiQko1aQ5zeprmfq6dA1Cw6IY8KbTd8A0iamH0VTBlbGEPuXNrD5p_vzUbpe-2FZtCHzTsi2JauP6jlYae-kX0qa0UCaGJzCzn1YSmsB80ugmJ_Z5YGoW69Ov_R9QDAx5SCLnQZ43FN1_WREglfWynr8TUlsg9fS0a0Ffu1rhaSQPN6CbDtBGyNDv2-LrX04CRb2luvMCq7If_qhSAjSFTJGDZQwTN_6VBoWTk9vVm3LHL8ONaGIneSsfBEC1n9NxHiR2olPCkIqzFX4HZn7CLKiOhBOiWUUS-qKp_a0t9DE2xMb9J1z51GTC_iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=sGB6aaVs9gZNjZyg_DF5PBDnQi9PyOk3fNk1IBH67EaGlBnuXA99gLQNbUzscC_p-pBm-oyX9_z0i3AEvy8WblfDiyuKfNLGzg-N4KwQ4nQDn-UrcP-ZQ4_czUmrak2BQEAHKvcWjFxi8zAIMLmnf8gwrABO9BK1zhnQxcMOGaXAiu6nDl4lelbK4B5bKmrOCym6Iah7_sGrilqyr7MXMD82pVXrOrX9ELqIzdfqgLNXaYZD5V0ZSDiidhM0whC2VXkMt5xuEmClvnbzIkDaMHTO2sAvHsxPeAji41-UETzSHL73gczw0khD9lf9AYTaxEMn4v4f45-I3doGdE52iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=sGB6aaVs9gZNjZyg_DF5PBDnQi9PyOk3fNk1IBH67EaGlBnuXA99gLQNbUzscC_p-pBm-oyX9_z0i3AEvy8WblfDiyuKfNLGzg-N4KwQ4nQDn-UrcP-ZQ4_czUmrak2BQEAHKvcWjFxi8zAIMLmnf8gwrABO9BK1zhnQxcMOGaXAiu6nDl4lelbK4B5bKmrOCym6Iah7_sGrilqyr7MXMD82pVXrOrX9ELqIzdfqgLNXaYZD5V0ZSDiidhM0whC2VXkMt5xuEmClvnbzIkDaMHTO2sAvHsxPeAji41-UETzSHL73gczw0khD9lf9AYTaxEMn4v4f45-I3doGdE52iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=sKo9RXdtSU1PJAXKD-a18j2PUyjy6r1Tx0Y0TEteOcecrsjjLPf715shImjr_1W1O1aj5Lpel-kiBs8cO2snU2dQEF9T-HRsz9ln9ey2K5oWa7V4larNu_SuSa_7zK-MqJhE4JRzRKh6pJuZwO3Y3aYE0XRlQNX8jeqowimgFIedjtYlXn-DzIOIMtbF3FLHZpjpBaepL78RlnglGS6cW0-ZhmjCOKFSvpwUuBjM--o6IFYdgGE0LgNQO9SckuFoEJB_8K2rGbsfDhFnqpZASuwyTvwvZh76SiO6aaHOKatfax4YI6O-izcFvh2GLJQQmDMiwddIfHEIxAJ3jI2-5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=sKo9RXdtSU1PJAXKD-a18j2PUyjy6r1Tx0Y0TEteOcecrsjjLPf715shImjr_1W1O1aj5Lpel-kiBs8cO2snU2dQEF9T-HRsz9ln9ey2K5oWa7V4larNu_SuSa_7zK-MqJhE4JRzRKh6pJuZwO3Y3aYE0XRlQNX8jeqowimgFIedjtYlXn-DzIOIMtbF3FLHZpjpBaepL78RlnglGS6cW0-ZhmjCOKFSvpwUuBjM--o6IFYdgGE0LgNQO9SckuFoEJB_8K2rGbsfDhFnqpZASuwyTvwvZh76SiO6aaHOKatfax4YI6O-izcFvh2GLJQQmDMiwddIfHEIxAJ3jI2-5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24734">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myOLGEiF7A9ziOEttpZLJ3Al0jx7iyiETdy3sIPhJEYWEw9Y-FBLSAzA_o0sdlxvWnMRSHFI_Wxf0VOmaTcgA3jVEPt_yZkP4fa0IcIpoaL0EIZjhsbmKp8i8VJn_XF-j2JyjIfClOUEXjAVs30LSmRyzgcFA42wnuVm4Ot_CedDPnIZmnMTcIMRLUVhf_gsLUVwhsC_r-lNax6pceQQP4eFLBNs9uBAqW95oA30rGhwvyukdTJbOn826Xsx45G93YHQxH0AqXDieqWI1ZsNfykGHE-csT6UgMDoLfT8YipoUBKpeXTq2bci3CGVwyEE7OTUQObuhRPHsDiIMDZFMA.jpg" alt="photo" loading="lazy"/></div>
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
r10
@betinjabet</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/24734" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcb_Lqvr5YtQjEDErz4S6vQSuIuZEs3RgakOC_u3kA6UK0i3uoLV8Vv5y3F9aA883V1nAjRUK48zvbn_qRWvIM21evfNJaAVd8UbdxVtKNsvBUMF-4UDxABd1n-87W-ORDRRomNy7X2Tm4UvqHI9r_bmHBqGd7Pfs6jkTQVprSCylOF7DZY36KCkQByZfaFTTlH2AHPEKG3c-OHLvIJ1r0O3kfZ8le8Qmsso5tBqw9ZMZ0NuntCse-u63PHq78FUteIkYLx5eday3fKzsDPc4Wh_teTlwfmAUTPzWIuSgbzHKP7zCpYum_gyZQ-2hN1sgHvvaUIUsWCrHykTid2VSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=g45jWN2Q8QV9ezA7ar65aja5cMsCoySYGyvlbwLEUJPLYR3wDwlbNWWlAkIpfdDlW5uArBgeWYaWHPipHrVPlE2BgrgTu7JZDpsle8Q6vE8Z1F6LExtusD5HDO0JV7nBCkl86d0jjtzSXv9VTuWRqOtFXXhhh_Qo1EJJAgpdxIruAbVu_yQf8GnW8Xc0YdYHFIT9aRcPoZs6zED3r77vO0GMG05c-D94HKh2JNaHIgUW9wwWPl2ioQCkkLzQJJshfDjX8bkrAA0FY8zQC-8bpYhbK3ICs1qyq1hJ8Yo67Hj0vqz7O4AYM_IE-0upcGVuFyvKeQauU6thfy-Lk04_Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=g45jWN2Q8QV9ezA7ar65aja5cMsCoySYGyvlbwLEUJPLYR3wDwlbNWWlAkIpfdDlW5uArBgeWYaWHPipHrVPlE2BgrgTu7JZDpsle8Q6vE8Z1F6LExtusD5HDO0JV7nBCkl86d0jjtzSXv9VTuWRqOtFXXhhh_Qo1EJJAgpdxIruAbVu_yQf8GnW8Xc0YdYHFIT9aRcPoZs6zED3r77vO0GMG05c-D94HKh2JNaHIgUW9wwWPl2ioQCkkLzQJJshfDjX8bkrAA0FY8zQC-8bpYhbK3ICs1qyq1hJ8Yo67Hj0vqz7O4AYM_IE-0upcGVuFyvKeQauU6thfy-Lk04_Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=JG4n5pb3ckofMgw0fBbW8uBmJVwUdPXvSUcxDvssKP7Ioa_xVQa9KhAGfVTM1PU2sswFIIZgZM7DH6HnIcLojbJ5O3IRk4M3jKF7ZGR2Yd3aIAtvwUxdBHqXZbx2Xebf9i0xgj1cVucKTutFvXIsZdAtqjSLiT3Hdj-S-SXLIGJZdrEm2LD2XyaK-xzzErjS7ydMavpVxqJ9GetqvYhTkcy8o2spYvZf-WNji_tsArKD1wihFNQwQP_rqqKtW2zIhYJKTJApofz33D7uJh7KB5g8U2KdYwL4lsKDoGjtO-ShRS0i6kWYh7t4MiSQoY-8Us2uE6GHqUMq-y3ff67RlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=JG4n5pb3ckofMgw0fBbW8uBmJVwUdPXvSUcxDvssKP7Ioa_xVQa9KhAGfVTM1PU2sswFIIZgZM7DH6HnIcLojbJ5O3IRk4M3jKF7ZGR2Yd3aIAtvwUxdBHqXZbx2Xebf9i0xgj1cVucKTutFvXIsZdAtqjSLiT3Hdj-S-SXLIGJZdrEm2LD2XyaK-xzzErjS7ydMavpVxqJ9GetqvYhTkcy8o2spYvZf-WNji_tsArKD1wihFNQwQP_rqqKtW2zIhYJKTJApofz33D7uJh7KB5g8U2KdYwL4lsKDoGjtO-ShRS0i6kWYh7t4MiSQoY-8Us2uE6GHqUMq-y3ff67RlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcQcL_4DS9u9aiSM4J_7Phq_05vIWQ5fzDGBLIaNKyiChEoSOeY5Ov0WHuZxFXyItKKtlNDp-D01det1oiOo89bCr4BTDKX_BIHb9jIIlooBwYtpVCzxHX9D9gXLJ_Vc4pzRJ3tiRfbLl9PZY7Cwm8RO-X2Rc401jrNyzflv2yCqzOMH0AQpua5d50E0q3vb28rzXWa3Suba_7c-LjdvR0NkK9DRQ22E6Uf8_RUuE0sTk0MN5cL07OSG7vjM_pnpXpP4Zub-CtxIF51HC6Q_-7cSCE_i5uvxBuD23Zj_xV10498q1obY1og4b8ewPqZC9-liA-SW9CQLJnS5zK1zlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6Mn3CtNQeb9hgydjDkcaJR_13o3gOrxvvJmCALpjD_9AIKRu4AIBiRIxpZ-Vk3ViKgxyZycIdOFjFxrc3wGM_7SqQ2RGAw51ktKHYIwp1Vaqw3SeHpbxIvuU4-uFWQFOIbxd-XBHLVkX16cbjyfZwNvPDsp64RNgpV2QQTUU-PUyQW5BbBOtzfA7YLP8cGKyqLdrgIaQMJFzp_3qD_Qg-naBhK1UsOjvVSykPznkXrja4lQj-c6f1K6PgYMH0FZ8zU6Ze4LxbSmMNwp3UD1p6_mbqltoQR2oVTXWmiz4rPyyTNZodh39cBEySSV_7gdUxKfMf0j4a6ahd8JZEyJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVXVeCxvedXByY4b_Jm_HB0fOPoIF13YuJbBbWgOZoCqGmExFmGPR6oD2LXGjwPY87pyfPYzoqJrW7J6V1jy4Nq2nFANxp9I8n5fMh6gyYZscSNMe3dV7NmeBhf5sBGxiHjN3eSwdi_XSfHxIhd09dq_0L7eCENpt0s7gwNvWnlYOkHC3c-H7FFUKKJVEU5t9JkdgLgvziIJKzYsyt0ruRNwyKG_RifS0I5V2kWLLMACwbAB9WmGgtzrlrUz50ztCKQvg3Nl-EU2crOyBArxp-whAs2ukhmDB6w2ISN31k-uHWuVH2BzuI302dauEFAnAYPbFHaNJmOZ-lSyZ6c5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jDJ64XNucJR7hbbtnovGq1X5IC8tYi_PXPAH9YUQsrBJhrU_001T8ZJENlL2jtQi43kpu6sLjJnTmTY5ecTLgomEb0WaZljsdNFYvad8BpnUos9H3ht4g0OzC0cDyKwF8itxGfLuOj3eWbikvEW_di8s3df1DyH5AhyKz6BscfPlPIEFAyfS-0uT-0DQegp1oKh-FFuT9A2McbNAOmIhPXXYob5eIbz6Vdb73lYKQIjLF7dWaCql4-2K5onwXw3NhQRPXLZ67LJVAPtU9ZHgI3ug0XPWm_k5oWeW7WWpEKlrK_4v4Ljed_CTv8lpRZImXH8rsCTHf0huZXYntsCaWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Z4YC0N_mmC2E1dhNdwbMUZ_v562acDuB1lCIu47igwPpuTnOE-dlS6ciFz3m2u5eeL_nbznj4SxlfQMU9KOUw16uBIvU8IPgd-JatR1Q9l9FEGOHHfEEq1Hb_sIQEwNLIP5jZuEYpLhN5bn-9j-ja9SonaAi-43TuNonpSpJ2FF0qfprdnaiZK_8-RE0A4xsjy48XQ2P9V-7DNPRU7QcruQi4X2CLJdjbD9gYMFrNh3eG81NoRf6XQzkcTUhPKGbB5g8USlJMdIA87me6fiDSZLUefm2TRhbwRCvDpkeKQn9KG50UYcOdXoflOBwYTHiDXUVVfNI--dfC9Gs7q8-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=Z4YC0N_mmC2E1dhNdwbMUZ_v562acDuB1lCIu47igwPpuTnOE-dlS6ciFz3m2u5eeL_nbznj4SxlfQMU9KOUw16uBIvU8IPgd-JatR1Q9l9FEGOHHfEEq1Hb_sIQEwNLIP5jZuEYpLhN5bn-9j-ja9SonaAi-43TuNonpSpJ2FF0qfprdnaiZK_8-RE0A4xsjy48XQ2P9V-7DNPRU7QcruQi4X2CLJdjbD9gYMFrNh3eG81NoRf6XQzkcTUhPKGbB5g8USlJMdIA87me6fiDSZLUefm2TRhbwRCvDpkeKQn9KG50UYcOdXoflOBwYTHiDXUVVfNI--dfC9Gs7q8-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J47ma4SayyIgs0CJU4EPRtiTL696VwtJ0OV0vQsIspt6b4hFL_qNcu9SInmmaQnDQpcBIAscLXYAjMOhBTr142WtLUc60XybUjXaYwps4jaXCef3X8ADTzeQAIK1TX3jrAcEv8CmI_FZ0wKRu9q1DBzfmlDLz29ya2-8gyxOUAa3d3F5ow3qxL-SWhIWC7NH3rrtSaXhyNuRsROP1I1C5ZEwevvXBdYPhsce-Xe-5f47jZqmvez52ZhJin8_eFIKJSMg_MGxpEXsuWPhdbChERP1tBg6175uXUxLIbbEl-nKhfg352HN4d6QZUO5AW_2leJ9OSUeT17d1LbE6qHsMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=gQuUR2qHeybos2CQbL8_0-yD9N4LR-qfAqIhbsTJyQ7-5529tfTcW9i2h3Ys93D6bD0SVLfbXyTYMqxidw-Wuool9ZIf-AO716RhkqTinI_L69YqNDLZ3SI3pTGIUF6aQyfwWf8v-MG58EpO1HgwGu4s8UKTGnTdXIfQ7Xew1b-p33wOZp6IVaHl0VzOjHnVVdKRPGqysnaCony_W_j87GpYBxE_OnYI0zfGygke7Ig6K0bOCthbz9PrtACmNfiyBrGn4cLzIde2POTnC69iyFOFliUuWJSS79dUzecb-aGx6uPhAdqMrK6Ksx-Migeg72OlQcPw8X7ek1Rpw9xtdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=gQuUR2qHeybos2CQbL8_0-yD9N4LR-qfAqIhbsTJyQ7-5529tfTcW9i2h3Ys93D6bD0SVLfbXyTYMqxidw-Wuool9ZIf-AO716RhkqTinI_L69YqNDLZ3SI3pTGIUF6aQyfwWf8v-MG58EpO1HgwGu4s8UKTGnTdXIfQ7Xew1b-p33wOZp6IVaHl0VzOjHnVVdKRPGqysnaCony_W_j87GpYBxE_OnYI0zfGygke7Ig6K0bOCthbz9PrtACmNfiyBrGn4cLzIde2POTnC69iyFOFliUuWJSS79dUzecb-aGx6uPhAdqMrK6Ksx-Migeg72OlQcPw8X7ek1Rpw9xtdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7qVUJN9x4VxDEz6m4UAJoVe910SFityoIpZ75jgu_hpx4tnlD_xKXYgEr9hqmgrMWFZCtcMN26G13ehTsWN3Tlukd7Q5vr9U9U2yVCEVO7u2z4QWEXAjSvHCvUVOby8R4eA5OXPgir0WBmtwm0vhop8L8Rnl9YGFJ92_pYgIG37oHkuhc6zJyoMrwyOk47X221IAlsHL9RlCc6SmXMlgqf7et_IugGfCNCqCKBB03zW1Yp8i50AE4I-lTOeknNHy-eG7smyfGC7uDZBmIR-apSYI_DG9btzL_B415KekDwmc9VCppVYhW1nZE4iXzzNE0I2yZBm7JPrgoSFNJcYPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy-LFKMmbRcgtom0n1S_IeeeQf-63VjIoCrI6drR7EZdahbJZdZRIS49bUcLvNdGtB35GyaWEt6c0mnibV230gkmxo6FanAkiPBgnWPqank-hIXcNBUKz0JWxjV_gYw5mWQEw_42RPq2xTYAIkTweUdCC1uXkNueQTLqvBv7Kz1VLVb39Jru568XLY-TBvH1nPNMUajtMYxRw_PimXSVJvuRgtLpgHRIjUtvlxN7Yj31OfLBz67MtxcQyfAD1EQTG-3ZK9Pch2BXTAsg8U-UWiCwoYeWZ_xgFx1DuxQY_z8-U_8k7LsngdRTKvkiap39mifRA9UKSSTejzZWbRMT5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df_E89dgBGGFrYZOu_H3fZHynYsq6JzF9hZsXnHZ6ayuw8f4ujHd9LtnTsXSR7YUWCflrELcS5JkGwlEVPVKJmYbMNfwARano_lz4OPSq4_x7SH6bJSUwawX74IhDOl83hXJrKeCigsoNBghAJJA_cC79CqgJ6iareii_GNszNZ3oJKBLMG39NSAhoECr6_Vw_4YepEWi9ETMuv9C8jwYUAXbRpzaU414ZG7-vafWedHMwOzmJvDvGvRMYUbhLcmFTlGwe5vsogi1RUfvo_WfR38zYuLCPGyinoKTaBk-gDXoWMnvQmN7A_HImu4AFpeYSGt4D8isToxbXOUT8ze3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ_xPAHE_4nwqeF_tXWDFSGoIP2JPUWZJWXkuPhjv6Fb9jpaAQBoMRIjBqfU_Mwve93hZGH9iJnYG25-te4jVXcgBY2lqYO6RejGcI8pXjheJUdku4veUm8YNIyqr6AWgrs7csGU-p6T9EP2cShJTFwSnUYjWyJfX7DaSQ-2xpY9Kd0LEReUBpyeNCZiUiOjdQZrUNp2Qk7aLzHdZCXOC9n9csgaOuhy_y8rqcuWqRqZWMyg4F6r94oa7o7TyIUYFUKe7OQDwocoD52WbreEv7X3F53vShuxGtnRco1lwgoac8gkcOktcpuX3ChAzGg9nEjDILRDgqkHpy3E9M5ghA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOZ_D1udFyesgBEYScwQN4m3RXKOV2Mma6Vutm6uga3d2W7Eyhhbm48aAbGJp3MvafO0P4Zty0gHNK9aorCPOdUVYuDh095ELzE1S6POC4LDeu0R1fQPOjjF3sW2C3JYLbrMDpfTSvvMMgZzh9R-X1wZ1rRmppxkUtgDvawqzEv-tM-k8X7mEy7X3RF668iLWroS0KklFKq5HQDwpwADMNwAGmMw7RMpv8pzRQ8owLrW8py0V5bBcEv76Yawy3AdYWngPPl7Lq8tAAVgGcTgY2SS_9WroT-0UKtijLoeSozl7P3oxyW8HWm9fyKtb6qKIAgOT25wB5qsPjIBJNkT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9YgkOrtOtxaK6lEIS7-eX7RCSStLrcKEiU_wwmR0MBm1Zwjov1jhh5rlPReIw9xmk1x9Ucxx-JAk6zYnqGcB75MbpuVwZc7jO3xBy8NSJFVkPKePYbfM0jcOIDqvctaoQABiVujrF7hgFMi2tH2YMsmJXx3S98YdzV3tn0PbJ_sMubix6ofrX_ScS9vWCfxy7PlwHDnwEIJi-zZzGE93bnuon2Wo0zi8AI7YAMxyeSTmDuA0IzOBPv_bQcJcS43RTdUchM_8XmAeJdLFJzLMQ4RX9de5dtD3hhy_9KVPECV7vKLuKQb436NPrdaw5reSbmhihnV2GGt_O95fGlVZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLUlMjjFP-jaqC2mZf_JkuWGl2JdANXZbsEoqk6aeTO3-N16OVOnij0EdgGn0U7PGPtsQwpMsha_Dk-Aj5CXcq2zFkwKG-MAO5G39H4Ypp_JaetuKfhwco9b2mjf0QOu7pM1-iang-6j1xqoQVPi8CHWt9pNmeLfWBXSjywy6DUTgsvh0omcKYVSdX-FSB5VaBp-G-WB9i1cBvjISvtIDPryICwLlAuI-IbCSLOZbP2QSHA1H5VKNseOmXe4G8QcznaIQDNrLnReQM_BmSZORdV0uGHqlC7jZihD4eGMWfOT-Xwslzj_-Pu5DG3j-Obl_kJZZyUbXoD-dTvhIoWAqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GhqLMqkgu5rXeTUCFu7ZrF9iKLw6Iep7G5Y_UpI2b64WV9E5_uDYfgzy6A2nKjZpJpLVXM61c-YELNu-rZVS3Xgwh5lil9RrFVchzv6ijOD_A7CCEjkZeZjcqI1iUmLzyLr37rtVe2xG2eaFGX_dc7xd09jCHazAJPuR1walSGpWndsaS56HBCMCSW1pSU0Jn2JUyEpkN3qwttBvtJ0IiA-bFey1O21vVVtLY4Uh2RqLgCAx2IN1g6PNbJT8XdYhjiftkuNUeQwShTdJbgi3dgae81rywX12Ltr7G2DvnekhysFdSXIck6B206vYFoIsZOTtJ-mKcgWGQ12Pg0Awbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g219ldTcho1iMJ7KwQ-ouyl04AMLIDPk9EF3cqpTc9nQsLR4N4lS9oFdhOwEXAfboAwV6HDed6uhqxwQWIPTheU55LHJgpkspA48g06KUZLUa9n32O8iRkaMecwp91uO2tXBzSBLmOe9x9179hIIoU2SbmwfKtkbxpgzqrHipGGuYMI-PqegpFE_DWlLJ2GAJKTujAS31ne7h4eysWLB6cKP8GXQ1wWEgluB7mi_UKVI3PhbcAuT7K1cBLeS4xoEuxAC8MwbmYvqR2JhymTgYy7Ab70pRRDXwZ87sCnlMuklIuALt6RlfnnZglu0Bk3FNbSBmVj3tQP8dVgSrvw7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAN2dRqX_T1ywOxzPhoY3pvwy8VECJrbcHDiXBE_vNdP1NqDiRKF-MnkAZBcjG9GXn1U09DvjBUvuQhtX-25GnwaLBQU6Z70xOfpsFiy5EBvgIMfsSRkC8BX07yIt_MhFZmKW1ClyqVWoy1uUjeYTJAoo6U6Z7zAXqr5YmvAm28YT35nTqXjtN5Mc5sjzlyLoEK72ko7lL78Dv61MwwtPjtZDixXsjJ4TWs2_CoQVojr3fvtZIYXXikMwGo7JtP3pPpcI9EdnbvBtrlt3HfQUeVQGS8tKtwdNDC78JGgr2PnfMrW5ZgDhVt1oeAiZSjmmx-iD4ROX9L0ox5iCx5cFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Am1hd1bno0NTAnTmYjQYN-kj1MI00CRpsI4hRpqkmBgQneUVAo2C9__hE3LhTgi5ERmHZVcVHFBhQ3mlFgpDZ5nS9WpsKSM6FT17D-JNWKVWrsxlGWDYWvoVVD7SUDrYycTSoC60HwSmcX_hsu-qABGLDu8u47qdufsYmgjxgGBlTSdVUUEyOFlHaidZ2O_INOR7ZIumMpNlZVWxrHfsnTyF6lNb3_Lzy45pQ-ipu99KYjRbbwkU7L6d8fum9V5-2BGWoEX2xDSESYH69DLd3QcUhcnDVTIoEM6hZ0Gd0hW1TtLfii7yEKIgxSQyLDUoMYV470U92UpMcHMGCptSlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRlWk8iUpP6eygsDaKtg3C54FCB_IA-ctz8D7sX6Hp-NCnfkoUfzx2ottN2S01Tg4NoS27kFUyax0jPimRtX2vVI1iOKSLMIRgnBWMM_IzDXi4s16aFeUeHEGCEgBoggs_E7tO7_3LgLo8Vj2GFFBX22vUyqRDHdpvKui5oNiQXXSyRWCdoYEqt2UoPxJZP556Z1FYkMuYf1-wqReXuBDtIMXKUH70qQOQZ8FY1iPIMesvL_mtzqISVoW3cyA9KfBkls_-3aZ8bCHYGHAl76QwxWqj04VzGP1Frut1YsI0qAOZPh_j2cu2tJzQYoz__K1sjOMseTl6b8ml9lKts2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aSgg5ma3FyAO-P_HBlP9krMgT3mZXMtqKxvyUd54y-6dZYDdznTWwYscjQ6JgPElWyMQjHDS8WzhVNXhI2Uyib_nHnWaWBfVJWOkzRyLdJcSQWyXJbx_iQZwcyS-Gja4968U9O7_k8_Gj1YxjQCun8CQADuhwOoQiEHlvEtgcNgttsg7dhKyP7kFQIUio4BV8vVzYwpAvpSPROTlPifek6PubpBAkn1OfVL8qhvg-wVpxTiYg9AftXZh_pFjuH1pbtcVWzLnCXW-7nhfy0A68WHIH1xr2HZQc_cPP-msc6ZNbH_4Sr12SS7acBualmo3z8hT94n2aiDhgKgrUn_b-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇽
🆚
🇻🇪
🗓️
۱۰ تیر
⏰
۰۴:۳۰
مکزیک
🆚
ونزوئلا
صعود مکزیک یا شگفتی ونزوئلا؟
⚽
🔥
مکزیکِ به عنوان یکی از میزبانها این رقابتها برای ادامه مسیر به میدان می‌آید، اما ونزوئلا با انگیزه ادامه شگفتی‌هایش به دنبال حذف یکی از میزبانان است.
👀
⚡️
میزبان صعود می‌کند یا شگفتی در این جام ادامه دارد؟
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24705" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l72QGXBFAT8LyYTGhMv09d6CPjCLboA0cdbwQtiIE2tGaHunsyuOc23gPDovpdgIFZ35CBcecgButZYyynDXgs_xSQN4yRP71zOc--WgKBxjRWSo9Os75aKh0QkvrLA9MkXwS92y3OzhLke5-rXDCrN9-TS-skRlowq6OfAA10tDDlj_6WPdb1B7cob3Tzs0Zcq7bIXpti8X6vYA6GvrPLwsGPEUA17LmCLfCa7A-7aka4zC51-s5S-6y710RBFo3kI13Ivx7MDFHX61Dua9Yialekrgn_rToHaWYfBPa-zrST_npQY7ULX6IjCt4-C6qCTIrvqZOL8OqpfJ1UN2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gf6fhvMWhnFjqCJCBSxMWt-_7OLr7wQW7Mi0tmEWdgitafyVW4cmszHt9-am-QPbYDrN8Ayc9RYwbbGsYf0tm9ZJOe6QBf6YXEHfJH59oNhgaV3Z8t9IaBg8DtXv-BAFzamrsn7JzEOD2xCcD6xYoNQpbdd3_n3g9a5umyzn0PP3ovKm3pD6SbcQyG5nPkxH65VKgTPiYxJF6fD9-4tKIr75bW95nWJ7YSdKxbPy93zDBh6pTMUL33Xi8uVtuLxxkHdHSnyCtE5nyFbBlv6bsaIjQrRXd6OrZdhpTyXMUwSFfrC4TqlnkZ3nNDoLg18oKxbT3IRoehm4fnNxEzzQ3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b_YJPQRrA-GrB1y82zhpUEyONgyb41zkIsHOLZKZZY2BboiPtgLUCkPTfZYgpl-lIBn_bEy0hfTMgDvCrn3T9lqxrvQB6S1urP8w4XM-wjx-P1PKzSkkzq0637iFTSBKOTEVytURA-aB0EllVMDSpniAGPJNc2ZMO-duo3Mzy2JGHvungTlOVQ7IYZpz1F0jOeqaEjWrSCkWzAV6eFL7QBOtPL82JskKqXClHOciQC7QBwCLSACZCuoPkCDQzkoCD0Qyxruvk18Ad6FParQe-QU6yA3akYaSamLYN7JDvQVSSXSRw1UwDZTHv2TgeuLYj9TvhKhNNGZYh1oVa5W03A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmXRMxelvpgjKrTdX6LVHBySeld0GzS1kg1S_eXkDTbcCwDPBwLr_lkw672NObLsXmZKYv0GtJSTMGboTGbQkMYwvPOc-KrBlPw6XaNRffDlQz5IQF3EK51FvsU3BhAbygG-08WT2C4J2sVEdcqGvqwpIlviFJ4tX1nRXzqjBlgf3awzR9fkFiJowK_38-ReUsJARPqXAF9eyxEm5cqlu8JerlU9mkhuwyNutNhq4KCwJm83Dk1dQdukexV6kqy4zFy_jAPAlWF054DwSN_Q7FhACgNWkrSsVltbaZmUp73pqW4hrwenHPHDsINsDt1YxwCB5lnjYH6e5AWpoL9C2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24700">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUcsd9c87cCaC7QyqaIsHPVFeTG2pwsL0VooS4cCoD9nRZjUCpfzQDQnzDwr6ANEBCh6vXeTAzT81oVaKQ5_1LiI-AFttL_tIF9OT5MZLf4fqo8HpqxsyIw7l15Yn_UGxngHgWFRuGGMOv3YPL-AHRaAZ9pcP91whhG-0poOKq6G5pMG4zu0s894I0Kl7wB5cfP2CYiL5MpI7QDYs1YDDOEwmPvZO3CUWv_xxGPr1qmj6_y_OGXjJ9lgjgXxGWqaN6ePWipzJ4Y6fEljUNKomLmnmGfLep5wcxmfvWck9TuGH1fjoo6NfD6Sd8rwbM_l7Y9DGef9dJbhnv8Qm3-5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇴
سوپرگل‌دیدنی نروژی‌ها در بازی امشب مقابل ساحل عاج در یک شانردهم نهایی؛ چه کاتی برداشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24700" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24699">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVpWp-6nsgnU1E1tvNMEwy-HBxMt2i2ZbqMnSFjD_wLKi2D_h3oeHSLE0yvVwxgS3Ej3Jk1j2NV0qTVRseKJGI6E-Xp6a846ZN4LhI8eo1mdszZVw2XfDtsJvTV6yhuV8zAJEiQqmmDO9pP-9Fuz38dIvPWCjhIgEilqCTi-qL8ejW962OTAXirlP9Hr-O8CQzrJqLpt2BdGjU_BdUvNEPPZvwedGGug6a_eVREUFpLEvqEC1aBdJD6hJkbfgF7T3J6gGXy0h5jTc_vMDn7RwVb6bc6xQiIZyuV7FL_KEEHO5RRGKufSs4R23Er6fHcSwltCb07ZhEWQbuiJ-_9Qrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24699" target="_blank">📅 22:05 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24698">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dl7u3j8neNL51xVs-YHB6Hq9LwCpnDG9k1BSXGxSCmhTz59RcHvO-LGLFGBHvwOsnODS0giCF1VyAQv2AydLOk7XPVusE1G1Bmj9PjELYLZaLwzm57Qf_EQVGlaVD3bLWlH5nDjGl7TVYvinIptygx4YSf-V4i8YserDUyzYuo6JJoo5kDpcYz2T26CGURIIZYB8cck2hNh6I0aQBx9Nh2m7OJy6gnlVBBZK2MaHaDOKgho2zs8NRtWzHw1KlDGe4tGgnNn7BSNg81xFWeRDGDppUViCbsM895BKhvmsSYiMmNF_F-eIB8PkADp8g-E39XU_85MZPLJaeiQ6AXV3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خداداد عزیزی در ویژه برنامه امشب جام جهانی اعلام کرد بنا به دلایلی پیوستنش به تیم پرسپولیس منتفی شده و فصل بعد نیز در تراکتور خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/24698" target="_blank">📅 22:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24697">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=a68wgjtn1ep21xnEUVFNwQZqYAC7MkM2UlDocYbxply0HwPiF7GhLJgMd1HfmbmCPsAz9Wz01-QiYTjFXjgepe_j1woPl3AhG77AXmVZXSVDsDewoYzgC4UjR8etkbfVSN0ALjY_GS2k8SBFrUdSMT2ysbHrnM4vJ0ydkpD83tU8HUqJrzLkMD00Z97WFD5t8azPrUmbUBrkwtCub519WaAcWUwwbkZurpBxf1wbxD-mMKJHbF2iaENhQzNFK-t75Agf6P28KZul9YbJ5ChHc-eSOzAn-rDrL9WPKIr0eU1MzbWATaDqS5Zk6tkVqN9xTc3TLionstdlPgbhDb0DoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b011e22cad.mp4?token=a68wgjtn1ep21xnEUVFNwQZqYAC7MkM2UlDocYbxply0HwPiF7GhLJgMd1HfmbmCPsAz9Wz01-QiYTjFXjgepe_j1woPl3AhG77AXmVZXSVDsDewoYzgC4UjR8etkbfVSN0ALjY_GS2k8SBFrUdSMT2ysbHrnM4vJ0ydkpD83tU8HUqJrzLkMD00Z97WFD5t8azPrUmbUBrkwtCub519WaAcWUwwbkZurpBxf1wbxD-mMKJHbF2iaENhQzNFK-t75Agf6P28KZul9YbJ5ChHc-eSOzAn-rDrL9WPKIr0eU1MzbWATaDqS5Zk6tkVqN9xTc3TLionstdlPgbhDb0DoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اون‌بازیکن‌تیم‌ملی‌هائیتی‌که‌کارش‌هندونه کاشتن و فروختنه، وقتی میفهمه من رو کلین شیت مراکش بت زدم: این چه سوپرگل برگ ریزونی بود که زدن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/24697" target="_blank">📅 21:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24696">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQ74oYbMrCTXzk4SY4anMKtGszxVtXH8h0Kg9_SQX_s7b7QqCldlmaR1uPhcGKl79HXJTi7iSiHWtFBJbcPke9ar9brm0D9IAqRyVbJ8NmJXIL9BSmIuS8G19NJ_uGB2Q9lqst_nRn7C7quPGGlAc7tAZs2YDnvsehlnGa1wcIdyG3UFSKkpFwtbOa_rur38cIErxvJGFGkeAICCnIRHTcEgIO_hIMbaolXDC1u1FSg9gscisG2ylJArF4HNsC3bAJTDsp8F40ukThnvdb_iyEz1EIfM5BY522fUlhryEln7nm7DxtKJoKEJ0afzZ4m0BEtyU-6Ox_Wm45ZOltroUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
لامین‌یامال:
شانس تیم‌ملی اسپانیا برای قهرمانی درجام‌جهانی‌بسیار بیشتر از بقیه تیم هاست. فرانسه بسیار ضعیف‌شده و تیمی نیست که بخواد ما روتهدیدکنه. هرچند بازی دیگه با اونا داشته باشیم باز هم با اختلاف میبریمشون؛ ضمن این‌که تو عکسه هم خبرنگاره سرشوخی رو با سپهر حیدری هم بازی کرد‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/24696" target="_blank">📅 21:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24695">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=OQFQrjbblSMw3Q8l4wx7LwXEGOeM_lYf1BF0ECGfDmAd91RtvMFF2deK41QfdDdEoiUljkoJw4kn649ha2vN_Sa0P1r11MvgymCh890JthlU0__Afawi9vYxKizhBZe8vGz5ouICjzC_wcbgtncut5q3Hs46Fbzori02rscYBi9eaPO-oB83cAlhd4J9pLVnbmKxxo5L_CEEhCZpcGyeHcjuGogGHbiUpwPVRaG4xWxAaATJlLOdec32G_DNW35ZODtZ-VB_HrZMn-zMFt8BkJkPKrqlYnnptxse1emVBR_lKFEPtx2N4pmAG45AZN4WHfr-jHonnro123STc57RtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9726fa772b.mp4?token=OQFQrjbblSMw3Q8l4wx7LwXEGOeM_lYf1BF0ECGfDmAd91RtvMFF2deK41QfdDdEoiUljkoJw4kn649ha2vN_Sa0P1r11MvgymCh890JthlU0__Afawi9vYxKizhBZe8vGz5ouICjzC_wcbgtncut5q3Hs46Fbzori02rscYBi9eaPO-oB83cAlhd4J9pLVnbmKxxo5L_CEEhCZpcGyeHcjuGogGHbiUpwPVRaG4xWxAaATJlLOdec32G_DNW35ZODtZ-VB_HrZMn-zMFt8BkJkPKrqlYnnptxse1emVBR_lKFEPtx2N4pmAG45AZN4WHfr-jHonnro123STc57RtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛ از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24695" target="_blank">📅 21:17 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=OjhgEAdlQQ3NRL0Rkegk6o0Ig6HLg3haFheV1seYoeIqSvLh_6rLCzuVCn33PipXOL9iV61hZV9CgWG3appluUAw9IDuGmzQNs0yT5igNDWo9tYETk4DDp3pNfMZ_iB1ciTnAcDkJqWhYN4E91idJjIhlw1d7bFDAe-CL2P_y2QZo_xo3-QbjAKbrkxuk9Gqf8VbUE5A8k8LxrDkAARHsPb8dRW3StrB-EVfX3rwQy3OGTr2RWBk6L4ngHCQstxdHiq-lTcSDukJyP--TIo3z9V5AIq6mr2aQIi0aza2LCm6kyA7xwoceztg_SlShdczoOuhynlpkVXtBscL9M1nmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a72b5a564e.mp4?token=OjhgEAdlQQ3NRL0Rkegk6o0Ig6HLg3haFheV1seYoeIqSvLh_6rLCzuVCn33PipXOL9iV61hZV9CgWG3appluUAw9IDuGmzQNs0yT5igNDWo9tYETk4DDp3pNfMZ_iB1ciTnAcDkJqWhYN4E91idJjIhlw1d7bFDAe-CL2P_y2QZo_xo3-QbjAKbrkxuk9Gqf8VbUE5A8k8LxrDkAARHsPb8dRW3StrB-EVfX3rwQy3OGTr2RWBk6L4ngHCQstxdHiq-lTcSDukJyP--TIo3z9V5AIq6mr2aQIi0aza2LCm6kyA7xwoceztg_SlShdczoOuhynlpkVXtBscL9M1nmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
👤
باشگاه پرسپولیس در اقدامی عجیب در روزهای گذشته با خداداد عزیزی سرپرست فصل قبل تراکتورصحبت‌‌های‌‌مفصلی  داشته‌اند و قصد دارند که او رو برای فصل بعنوان بعنوان سرپرست جدید سرخ ها انتخاب کنند. فعلا قراردادی امضانشده اما احتمال اینکه عزیزی به پرسپولیس بیاید…</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/24694" target="_blank">📅 20:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24693">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZA3qbCO9vTnnAOmtT7VY6lx_Cxgx7GdlCZEBag8RvMekURraC00xj8Zri2wMbu4AIfUjtKIKeTSl0Go8qaNZ-dJ5OyNzs6h5cbIDEv6BUWJQGwZlQMPAW5xGIS1O3zmHlKGz6-XFExHFhGK3dKzfGLaoXWhkeSGmghxn389eJbiz55rXzTrO1EFo_WcqDGcwo7MC-3YN5ckzl92UGNjhpDbClyKi4R4S9tkjmUDYMzZwoYJvoKvtfoDY9_dR9GSprVCQdV7XlT0PE704-U3dGpa5epG1g7tacgfs1qYm_llk5pbp7FUd5Xo5YH0BzVRmwL1VbT-OdZQ-XJVkwXp8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
همانطور که پیش‌تر خبر دادیم؛ یاسر آسانی ستاره آلبانیایی استقلال بامدادفردا وارد تهران خواهد شد و در تمرینات آبی پوشان پایتخت شرکت خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24693" target="_blank">📅 20:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nolI1gE8UQn4bIp-2wGyVkADvPujbsNqQA4vw0xx7q5ObulR3ym8EPiHZrMJisaK8E24_jCHiwKPYnec4MvZ0jhzFMIrvKr0QVuvM3CD2NffwPYljy9SDQZbSNm2X5dHJ5Gd-B9HCHiujMlNCl7IHvn-ymJK3tGnkKbHulbELhE4gbTv0QzI_zxbHRxI_RGHVECYWgD8BBN7GVKzM7cxTwlH2gHv5nZo2gDWX1Nx9VXoyLnkyi5RjqmBodDiEO1MXfY3LffVvl6UjIAurlQQQqiBw0D2X6-054O8RoZ0mFbo0FVIuyH2OkeQFYyZan0IA8geqX7gEnt9rbRuG16wkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فلورین‌پلتنبرگ: سران‌منچستریونایتد با ماتئوس فرناندز برای عقد قراردادی پنج ساله به توافق کامل رسیده و حالا توافق با وستهم باقی مونده است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24692" target="_blank">📅 20:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXjx-Mpe9ad8bCWNz8ikYVqqHIqVh5BlYvG1XTwE0XlDUY60zBJK42NeKOR72QRwSOZ_QS3kLTPw0OAqN3QdbrMZU10gpIKrEEIf-NxDYdr5QBNV9gfYrlSSUfwg0678EIGMu2fhlu2NDDFQUh6JYdeOZnNWhFk1KOZu9rRqUcggOkPVMkx1QlmdD66LNWyYad7N6qNQ5QMTVhQq9OFuxsfKtkgifXJGTCTtIu0r604uXsDPcEy0L81fLN8mvYhNpJ198hx5zg9FA759YWjCW6fGqxR81tHm2GpO7pnXSZ7zMF-rjxRJrhH8OFZ77ocXCM2iEqdhkCQ_s-dH3_CS-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/24691" target="_blank">📅 19:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9zp33CC_TmlunC73d8qPdDERcz6wWWrfLcMBZGj4XtNr9LBnwi2utMZpT9R8yjXK6qT_YSg6DuX5LDAsbZ25Kbtl_WQfXPis3ZzOjH8Tn8YtnAVpFVAS6KvJa9ZVi7qHnmV5OVTE41qaafxpLVKvWRkx0VtaDtCyniTj0RTAYticrv0Gs6jx7Ko_v3DxcaPLDr0WikcIAdUXHWT3wrvQrIzt9xz7PYD-2yFyJpiQSwH_kjx6e5hcaV_hcZZ9g7PZVWLiI_Gp3w9AAqEhdeP-1KVQGMrYaIpy1SHJfHJSgJbMAaOdKH1kZQ_lUCmhz3lHOZfqCpI-XT3etErTJtZjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛باشگاه پرسپولیس و بانک شهر مبلغ توافق شده به اوسمار ویرا و کادرش روفراهم کرده و فرداصبح قراره‌این‌مبلغ به حساب او واریز کنه و رسما پوستر برکناری‌اش رو منتشر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/24690" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24689">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeGlOZ3RDZv2bFx-HWO1-xdO6KbcL7pu15mlwBwUWiBfdQsWEMXoMcxyLiRjg9l-V7P43MFLKreKUlNuG2WwpAuuMf5WfmnLeqc-0BRw1NhI7PgISOvE7oyyPj0lzsrxn8dmjYJcAQdXhlCGoLa2FaQQVHbRrZk6fS7_2FS5fKRodplGuBfEDZ8tjb7r_1_CijUESiCwGGgNZ5W4otPfAMYDH0LYHc0LOD3MTZ4ymHNcVFFN21NeJcqbVbCpZ60iDQNokidrS64u5su3cngmdt16JN7_ClT1w132Z28k-qndsvI0N5KtLHKx_pfp0xHVjPHoSmrYFvO2UlBjJT54qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
ضربات پنالتی دیدار امشب آلمان
🆚
پاراگوئه در مرحله یک شانردهم نهایی رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/24689" target="_blank">📅 19:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24686">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=LA4G7IPgkwE7LhwYf9cB0ybTHgVYIDT8QevZAizmqFnoTeEjs8wxzO0xRuvS3wiuTcnGtJTNK3tWkoGvbdL8BNNIdpb1vMlf1XxxDPeil3CS5wQSS3VRSOucVg1aR8UodCDTDMFhfd29NqZt30CDtxdKW4zhZ1H5jWPOTBIwpXxBhQi6sSbLWeVEpFrCg5Yytdbw6IXqybj677f1Pn1Yr20e5fmzeSUgfnhi2IsldeQEmn4dUE21VfrmXhOxbFQnMGf3aJxN8zQbWrcOjQtdruGT9GxJ5MKTYWGq1YdaHLxttV2liZNr965QmpOe50wyzB3R5CeBFQKon07JIC26iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85e47b5880.mp4?token=LA4G7IPgkwE7LhwYf9cB0ybTHgVYIDT8QevZAizmqFnoTeEjs8wxzO0xRuvS3wiuTcnGtJTNK3tWkoGvbdL8BNNIdpb1vMlf1XxxDPeil3CS5wQSS3VRSOucVg1aR8UodCDTDMFhfd29NqZt30CDtxdKW4zhZ1H5jWPOTBIwpXxBhQi6sSbLWeVEpFrCg5Yytdbw6IXqybj677f1Pn1Yr20e5fmzeSUgfnhi2IsldeQEmn4dUE21VfrmXhOxbFQnMGf3aJxN8zQbWrcOjQtdruGT9GxJ5MKTYWGq1YdaHLxttV2liZNr965QmpOe50wyzB3R5CeBFQKon07JIC26iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سبک خاص و جذاب پنالتی گرفتن یاسین بونو که قبلا هم دیده بودیمش؛ پنالتی امروز صبح هلند رو به صورت عادی شیرجه میبست عمرا میگرفتش ولی اینطوری راحت سیوش کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24686" target="_blank">📅 18:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24685">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=oy_IJnjtAWeXacCtsK9qfE2aiPdnkf0sCKANZ8SJf8zZxs1iDH6MJ84Oo0my7pf_2mewsw3dQBqdBKcWrMMZ4ZcIghiVwF7J4hN9rqUi8lqHGh1GTxTlpct8romaQtQJTIs3EQUmPPZFFJMLOmnvM9iyxuaESe8UTG3Zt4LeyO2AanflRDxn0W3iSveG_dBPXXdi_1jaLmEvh6PEV-8vVuexm4viVORc2-JZJFRXYpaVqexqJZjgjz4pjKVqQiurXk48U_T7d5kMPUKo2DZJgdMouvF3BnMnvE-24vDoLEBxMECE00mBUuigfhaNaBN0hSFn8P1Rf5juDHL-L-Vs7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85d949fba.mp4?token=oy_IJnjtAWeXacCtsK9qfE2aiPdnkf0sCKANZ8SJf8zZxs1iDH6MJ84Oo0my7pf_2mewsw3dQBqdBKcWrMMZ4ZcIghiVwF7J4hN9rqUi8lqHGh1GTxTlpct8romaQtQJTIs3EQUmPPZFFJMLOmnvM9iyxuaESe8UTG3Zt4LeyO2AanflRDxn0W3iSveG_dBPXXdi_1jaLmEvh6PEV-8vVuexm4viVORc2-JZJFRXYpaVqexqJZjgjz4pjKVqQiurXk48U_T7d5kMPUKo2DZJgdMouvF3BnMnvE-24vDoLEBxMECE00mBUuigfhaNaBN0hSFn8P1Rf5juDHL-L-Vs7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
تیم‌ملی‌آلمان همینجا حذف شد، نه مقابل تیم ملی پاراگوئه؛ اصلا بعداین‌دیگه نتونستن درست بازی کنند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24685" target="_blank">📅 18:11 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24684">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezE2_5xxpdl5JeEE6ymNGgpNm9XCwh_k66StIPoAnqXekUf4AwVeUxeOWxD0A0wsX1g_HnxrPXmAIEP9MkphuyyuwOK6cebTr7jv7D_DZt3XXxBawnPiMONtSHNGrSB4wULbxTxR9wbV43bEvAbid6bbmCjyvhPORjacRJq3IIrM-78ahfoLhzuDnadqMwsuu7y2KoJ2-Wve2qj7CHzdR4MDBCrtxaA3iuNH7ofmNdmdh5UIQJnAD-mBjxZ0i4cyEkRTVsq9vVVP-2CGAly_3D9SIXMTL4FNrpZq77WuiBPQph9_dltv4GN9kOpQFfipVlQqe3YIXda_jqM1aVouPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
جادوگر تیم ملی غنا: در طالع و سرنوشت کریستیانو رونالدو نوشته‌شده‌که امسال قهرمان جام جهانی 2026 خواهد شد. سخت و دراماتیک است اماپرتعال بشکل باور نکردنی قهرمان خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24684" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8rVjYOY-ZcndHIxWHd-cc3my8mlXaggJhb_C7V0PlaahA6q5wT1fxKPdwxEo44N824wBFhvGCosTozlPLLwWtqTmuHMsytFvvadD8AA8I-pO1vV7WFOc3G4EbGWaxhwJ026nZNCHZYB3KTvkj1_eTS_X9rYLLtjTvpvx_Kc2YBXI8l7F2NrAB-h7sgrrr9F1tG8Yyko7HhsUe4Abc9VPxAccN6h9SAwV3WDUSWfhwMEXBmQxqZv_I4Yq2a5X13lPP649QKAWEK9EtnBwJ5kqk6mMco_zCqc1knqrDhGRmd53vIiRF4wDGioffLd_pn8xaT4Zb1d8CcYmEehPm4sXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: باتوجه به علاقه اینترمیلان به نیکو پاز؛ فلورنتینو پرز میخواد او رو با الساندرو باستونی مدافع 27 ساله این باشگاه معاوضه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24683" target="_blank">📅 17:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIW845NDWsAbw36XYFAWyw9urs_B8OmHU1624sPXj91mb4SyLdnKk08F7P38o3uIASlbXhgf1Xk_0eRa8c4Fkm8EglOs_mPMBbbGgImJaaFZFKxgwdGF-AFtM3DiK6mANZweGmULX_ZHTAxP5FtVrR_Nibt8acvC_ArIvkO0nTJNuOo6JzFKGqDe635jLeOxNE5HLVuVnxZMNsrvt-bcUUqTz1vX7OBGd88rGwhJcS5kbqfLTIcSRRbTGnJ-09sz47EM0BcxlAvSzFtICx64ANGbk6o_W36XliIEmy8WJisxzLIFfmrU7xyOpkL6PFzJfTEKWCK96G-K1tFeWHkkxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24682" target="_blank">📅 17:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=VEGjyxH7TkBItTvuRxTjxN5F833vkm4_lhA2eCzo2l1IbgJi5_m_i2KQmYx9MXyDbZik3oyCSaLkuvaTIZqFwL4ZHF83vtdlw6vx14eM6OU5FYaUdYwo4yVHhoewzb7dvOVV0TlbfODbCXxSR3cRfbZleI4cDAYVC3EyFHgVNV9GkQvtgNhrEhas48s-4mmWB17tjpzJXJGD7eI0FjZsu8jrJfmuu6UtMQMA-6DgdXogOXznWWO8zCC3B32-tSqF8v4KoPBjrn3ZKQEJA4tPteQulZOhvqDZtKcbzYyce0jQ3i_upfHlwKp5YTRr-qnCos9e7552I40czG9xefFNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b6727cd80.mp4?token=VEGjyxH7TkBItTvuRxTjxN5F833vkm4_lhA2eCzo2l1IbgJi5_m_i2KQmYx9MXyDbZik3oyCSaLkuvaTIZqFwL4ZHF83vtdlw6vx14eM6OU5FYaUdYwo4yVHhoewzb7dvOVV0TlbfODbCXxSR3cRfbZleI4cDAYVC3EyFHgVNV9GkQvtgNhrEhas48s-4mmWB17tjpzJXJGD7eI0FjZsu8jrJfmuu6UtMQMA-6DgdXogOXznWWO8zCC3B32-tSqF8v4KoPBjrn3ZKQEJA4tPteQulZOhvqDZtKcbzYyce0jQ3i_upfHlwKp5YTRr-qnCos9e7552I40czG9xefFNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇩🇪
#تکمیلی؛ بعد از حذف آلمان از جام جهانی؛ مانوئل نویر گلر 40 ساله ژرمن‌ها رسما اعلام کرد که از بازی های ملی خداحافظی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24681" target="_blank">📅 17:25 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ePucBtQXuZD-ceEUJAXdeII648EJIP-JN2MJL_aL5Vy-Pir_WWjtZiUai7GivSooWQ3MuP5UarJV3-dhgF0HqdYwbKOxJm_8Bw8HQ2zi0l-zQxQ59dD-FLmtDRe6ssCE_5Z0pzEmwyu5andWeO5DaumBDjlTl6RegfZyzea3dMSrf5jOSlbDyVsJFfNVuO-oq1ogjOUjzcf-K4V0-oYL-7MvLycFw-QbmiRirjXD26HA8lo7x6PrsFj1jvlvV2OV0Nh_Zm66T1EkiAhwswNfTY1a-OxVro4PYbraczGh_nz_1-Moh13iXKEKAi5e1W-55YW-pAVTVozkxcF7gzpz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مسیر به‌ظاهرآسون تیم‌ملی آرژانتین و لیونل مسی برای رسیدن به فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24680" target="_blank">📅 17:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24679">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFetOAE1zbC32DVIFsdBr4BtgF4tLJJGEMJ_xysm4cwA5QC-WQ84hIoYpNAQGqpVl4p4rP9xzJADVbklBJLPQ7AoqFdUJbw3WFzpvxN2tXLToU-I_hZD0Txr8hclCqqnSndYKIy7JM0a5y6Xk0RAQCuwe7us8wUm3E_1cF8bF3KX_nekX6G5o5j-OBy5YYoYX1-dewUQ9Ebk15OAQZyBkFYN2Y_qYQ0EiBtfk2NGT7IAHv0hvbH4JCXz_cO6-65pLJE-YjYDc3MRAeXyNPyUYzWNxzpYykBMb0jdDL10yY36zZ1ZRcWPtObcc2vBUMx74k9j9KgDBuwGJSmkn3e7XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24679" target="_blank">📅 16:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24678">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRIjbz3FiWAWWGmRQPjH0RLiaK0MrOE_91pM7UJe54BMtOeoKXygOgbag6sGJO8yxEX3gqjIiLqkFCAaZgrtTGjLaaapwP0fgdqiXKFa3h4V6WB42R1yOeVujZtnny5bpaYJJep-gc4KH0Dx0J0X4rIYWE32on72AA44T-znzx0tYbiX57fXY2MovFx18I_4u2jLe4z9PEPUw1BzB4GnA7L3jJVPLJNrDiGPDRrmfAvrwkvYUmOwh55DigbLlXPsKL3Z0FHmhtiLhQoV2Ft6a2xwVQoToX3M5h2ucKhZEOzERSofgfxG52bsWKIJ6uokHj_uq_RHrRsV-_7yKXtEXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24678" target="_blank">📅 16:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24677">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJMM9rzCBw_N8rNkHFTWuv8TMGSzki9fsrQTOCa3dbueWcUNuZvzsaWI6UVyzsG2B8K6T8RUHhKGobua9LYz_JhJfiLL1jqv6HmIFxXZ7t54UwbESZbt9ZphL-_aTJJR6XP1ElrNp3_s7FfqrS4_y3qi2C7QnoeobkEqXS9RMMwVr_OF7BsVb2SzZnKBIxj2H_M061wo1IM79EiKuSztmbIBkdep-VTTyMLerK1_OytAJygkxHWPFuO4XIGTv3VoDD4Vy32mELtcN6mqJicqpotZwFBFcU-L-1sxKXupfjwPZ6JluEe87prppPxCkxu1JkSRjAoX7wHlP4dyxvt4uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
شش بازی بین آمریکای جنوبی و اروپا در جام جهانی 2026: 5 برد یا صعود تیمهای آمریکای جنوبی. 1برد تیمهای اروپایی. فوتبال اروپا این دوره بد ریده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24677" target="_blank">📅 15:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24676">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFp4xC3A0Q0JlpLU-OeyhkDYhDPkIc26On-eLZ2f3dRY64-JR16ISo5EBiz4kr_h3LE4dt_bkVjlq3e6Dwlv9YRw53YJPm0wPICIZTCfRz62srkqchZPr1Og7EiyPDNaA6Qk5mOLenSgWGHdVzZkusPx1YbO3XLPE6Xw1JE1C-GxyZmqsoECZu3X1NBOuxjxLMISH0rNWlq_JM8nr-mrldBgJtZATx6WBDMNwKehRM1dXvoOfyB49O0kp9mVPFvu4tgJo0z-5un48c4m4FudBz30fQk3SdcFTHLx-kHVwEjZY5biAMMsRCCjen6Vrf1NKvzgUQb88HjpvswvIVcjlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/24676" target="_blank">📅 15:22 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24675">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHUUlcd9cfDJxB7ZncTCwFY1eIlAOyG_rUCi12yCjADvMVNdh5krTuRUwMKLrL7TjoUbb8yXZY8jNPIHB0GP0LqZIpPXYsvBo_5_aqvK3WAcIKknLKvxTlhlD717nY4lBgl3vBP_lVvOLLS7rZ66kcjiklJI4scEkqfNSp5auFJwemJGj7OTgROFzNrwVWQLAOSQBPW4KTrb5sFQuWVw2jtC0DfEsJ94_Frchz6rjOf50arXA_ToJim6uRpXYdK29Os5oDzoo63rDqH9osqL7q2B3CfVCKPeG4lb_V_7mH2IKlR8l72PI0F9Dq01GuQPZlKoxDX6HsCaL5V_VRMb9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24675" target="_blank">📅 14:24 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24674">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HnH8D6IfB0l0BHduy2oYvCftsAnTqMfz8Rb5vA4yjltZ2YUL7gqsOLVNbhU-2i-79TabtFob2ljGNL8imK5VuB5GYAnHQXNKx5UOSQDPyke33ff0d2wTkIWd760M2LDYWmnxo9zs7e0xZWnOHTgt32Ce5UnWd_gFf5X5__joqt9407hV4QPiujOhhbPSOCa99rBn18RUdEab4eXItrxDdUjPrEVvseI17FnjcZkSCWffNtzfZb-frkAGgY2LDqJFBHgQkCe01GhMhsOMGBJmerdDb2gdaPBwwFY1W4qipqBROF1-3hNgwN9bwAfxV4Cm1kfvJKhydFIIflhe5LsTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه تراکتور در روزهای گذشته علاوه بر تمدید قرار داد دانیال اسماعیلی‌ فر؛ قرارداد خلیل زاده به مدت یک‌ فصل و قرار داد محمد نادری رو به مدت دو فصل با پرشورها تمدید کرده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24674" target="_blank">📅 14:12 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSkLlVr4ScUqOovGiE1cc_JS1lOixUDKPg-9TPDHSBO26sIa5xaKss8SlzME5M-lgO_3mMKCSl85juloofezY0HIViGjsLFBYI9-W3v7qPDj_8qkWj0z9MijMwtHM3vU8ryQ-gCIgHlYbh86JlsD0vlcSRmtGoF5fjnJPX1KUAuALTIh8JWiG0O3yVLpKtPrRWIWSHpX3O4XlxZfN-bwZIfd-4H1lCTvcqFXVq6ZaoPzGpFXkVA4lkdAcuOxPbNUu4oPfWqUJGxpu8y_SrvXcb9PPGhOXPhJ6o1Zp5n4hlzgKA6VM02w-zxDYBQCu98ajgi1tr0KS3GNS9KfI2hWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌استقلال باید مبلغ 150 هزار دلار نیز به حساب جوئل کوجو بابت فسخ قراردادش واریز کنه تا پرونده این بازیکن به فیفا کشیده نشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24673" target="_blank">📅 14:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24672">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82624c7740.mp4?token=DI0--DZFgMNA-hiF-GN0HpWaYv62LZgBcvUBICJmDNXKOJIJG6SQE6J5kYl-3_PAPw7XDsXizS1ImEZ2H9JyDfVqcilQz-8pt4YFf0Irj83cCXjSI-8gqUH63OZVsEJlYQoEdFMqTAoRJ_9J7sHfyT0eDuF5AbLZGShwymNA5FGtbgbtE3OTWYFNr17hG8pacGotU5Z83ANMisChPC5c1Mo8hbwHeKLMg-YlxGCB8PM37h00Tw33bS4gmNdSUWGZaKx1u7qYX056KwE6V1iL11CQs9vqiEDbxsQv301UdnwkocaDt7hJ_8XzFm2kWSRYpTPThAnBEqgGo2KScmYoEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82624c7740.mp4?token=DI0--DZFgMNA-hiF-GN0HpWaYv62LZgBcvUBICJmDNXKOJIJG6SQE6J5kYl-3_PAPw7XDsXizS1ImEZ2H9JyDfVqcilQz-8pt4YFf0Irj83cCXjSI-8gqUH63OZVsEJlYQoEdFMqTAoRJ_9J7sHfyT0eDuF5AbLZGShwymNA5FGtbgbtE3OTWYFNr17hG8pacGotU5Z83ANMisChPC5c1Mo8hbwHeKLMg-YlxGCB8PM37h00Tw33bS4gmNdSUWGZaKx1u7qYX056KwE6V1iL11CQs9vqiEDbxsQv301UdnwkocaDt7hJ_8XzFm2kWSRYpTPThAnBEqgGo2KScmYoEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
میثاقی ژاپنی که بعنوان بهترین تیم اسیا اونم نه مقابل هرتیمی مثل‌نیوزیلند و مصر، بلکه مقابل برزیل پرافتخار ترین تیم جام‌ جهانی حذف شد رو مسخره میکنه؛ جوری میگه منتظر 2050 باشین اینا میخوان قهرمان‌جهان‌بشن انگارخودمون‌خیلی‌وضعمون خوبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24672" target="_blank">📅 13:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM4vHX8Qsg8XzeyO71iCLGp0NQFPobHR0EHagLq_kw_UXPy0gsXH5Cq-21jf9FJI9D5058bmzajNoEZZcsbyyynAYT8-RFtUrlhVCK10Eii7aiiwCindeS0f2aHhdiKHI-wfi-aGHd8XdKSqInURLMl_Cv3zN7NyA1ds59BORiXCTlqA4qLjTy7Ie96E_uya725NEBJG2XWrZE43-ucyNrzmVQ8KRArmpds8CTiksR0gtmWoqyslifvSvw9Nb3uwFLq3O4-UNhU2-_M8oNv6WOqdtGDZD8KwVLSFCVEVey3ZHlZioCQ1dL3t0zhPFeArTVQ-Yo4J77oTjsfi3LxH9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛ گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24671" target="_blank">📅 13:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNTILIebTU69YhDhmyOmfjt38BUgSkMHdeR7s-d2dhCVTyYU3aIWhrNABQbStmdAS33ENktCPgpZCTGgVtuy9c3Ts6NZq0SBvzSqhVCNq-i2gA_wKU3LgYl21prUYKbawKJDkFOrYsW237sxJLsabdgNp7WXrJhU9j4DU4KHeoWUeJ54b8t9-okZoaeODTu38r_BTd3p3TeBgaddV-jRFMBgdpRDHof3dk1sA4sEarU4PtEOV3-mqidJIqbo8Qkd8tTtR76Okl5jLDNNEbwWEH2j6Dn3Htl7SeWU30CfJaVqiEmyWvDuPGVodc4kxy7ia5AAOIJihK-o77eRX036kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24670" target="_blank">📅 12:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24669">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68e8477068.mp4?token=Y8fL9Nib3PgEDDe6FGWsub9EtUdvp0-1qoo_-UDIFqCdnqhd6YZNeNZKt6NWEmSSxmpAgio6uUUOVfW6ugdqACZxr6-dNovh2qySlxF_7f8UXvhBo8VHSVC7zO6Ng8euHRI7kc8OayTvP7C_Vd8wejKlxxPPOX-Na954iAEKMgQEh6_2X2XG_zZz3bFcElF_ra-35TYskqLGS1Mt27m4KjCAK6rqpV6XNYM3SbC3nqHnIq3o3jFgKeajbvmYN9mRLkZRaONfHpHPGRZ3MPMxKqWDVrj1pZQb_ejhW-_MLQcT6YWOzV7w9Lqhu240VwFmLeWeBC_pWFag3IHuBvILow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68e8477068.mp4?token=Y8fL9Nib3PgEDDe6FGWsub9EtUdvp0-1qoo_-UDIFqCdnqhd6YZNeNZKt6NWEmSSxmpAgio6uUUOVfW6ugdqACZxr6-dNovh2qySlxF_7f8UXvhBo8VHSVC7zO6Ng8euHRI7kc8OayTvP7C_Vd8wejKlxxPPOX-Na954iAEKMgQEh6_2X2XG_zZz3bFcElF_ra-35TYskqLGS1Mt27m4KjCAK6rqpV6XNYM3SbC3nqHnIq3o3jFgKeajbvmYN9mRLkZRaONfHpHPGRZ3MPMxKqWDVrj1pZQb_ejhW-_MLQcT6YWOzV7w9Lqhu240VwFmLeWeBC_pWFag3IHuBvILow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
یان سومر دروازه‌بان37ساله سوئیسی‌ تیم اینتر میلان بعد از چند فصل حضور در این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24669" target="_blank">📅 12:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24668">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=uEz4_HtmPkoZEngdarXI7dIWUYV19cl-2UDTBPJ_ZL_lalgbvxkxKLmiI3Htkf_R0db4vRgFxS4S1ABHdeGfSPnCmkQ4iTxokIM3B0OGtpk4h2-pHFJETtRdVX_0K2OdJ9fz8zEmdrjKhpiS6GOwPAweAYUIOZqV6mEC4-gkt41fJ8-9_c0nhMvFDv8p6EngrRiBLlNYpJTah5aOu_yzQOdGGELuymqE3P1LW-NNz3j7ywSptb94oU0QqO5I5Jb4XxbJojSdv3nY9B3DaiP7FLuw5KSMcV_WuUVjtRyOl-9TdeToM666Me3TMVpP0W_DIaTYwekuZFbqviNy0Ix86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/786ffe7041.mp4?token=uEz4_HtmPkoZEngdarXI7dIWUYV19cl-2UDTBPJ_ZL_lalgbvxkxKLmiI3Htkf_R0db4vRgFxS4S1ABHdeGfSPnCmkQ4iTxokIM3B0OGtpk4h2-pHFJETtRdVX_0K2OdJ9fz8zEmdrjKhpiS6GOwPAweAYUIOZqV6mEC4-gkt41fJ8-9_c0nhMvFDv8p6EngrRiBLlNYpJTah5aOu_yzQOdGGELuymqE3P1LW-NNz3j7ywSptb94oU0QqO5I5Jb4XxbJojSdv3nY9B3DaiP7FLuw5KSMcV_WuUVjtRyOl-9TdeToM666Me3TMVpP0W_DIaTYwekuZFbqviNy0Ix86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
جادوگر غنایی درگفتگو با ESPN گفته شک ندارم که آرژانتین باتموم‌ ستاره‌هاش مقابل کیپ ورد غافل‌گیرمیشه و خیلی‌زود از جام 2026 کنار میره!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24668" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24667">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=X3KsqFrYIo9fVKOh6cT3Az2NfkX8jPqyxnOBysyY3PpNWF48LdLnbB_pb2s_F4-s7cnkcA_4CIH8q4VyF4jy7IyEBTcho05GpCaPjV_R0qNpIyFv5wKo3sKGUHAAmLmdJN153HWopjZESnec1AnN78JWt7IWcVZ_duqzT7b5qm0NcjnkZLGsVlLBKLs4Wpge_B53Q_wPUeHDUd4xVFN1J_b0KxANT95mbN1Jp9PJ_AABxa1wlRimuPx5PGblUdRMCjn56_1iXA6-9eYycN5-Oyr9CnF7BA2_UETetSFL0YCrxwd58unH3bVph13T-o30NA-_VrOUGLBv-LmLwU8U5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d5676f715.mp4?token=X3KsqFrYIo9fVKOh6cT3Az2NfkX8jPqyxnOBysyY3PpNWF48LdLnbB_pb2s_F4-s7cnkcA_4CIH8q4VyF4jy7IyEBTcho05GpCaPjV_R0qNpIyFv5wKo3sKGUHAAmLmdJN153HWopjZESnec1AnN78JWt7IWcVZ_duqzT7b5qm0NcjnkZLGsVlLBKLs4Wpge_B53Q_wPUeHDUd4xVFN1J_b0KxANT95mbN1Jp9PJ_AABxa1wlRimuPx5PGblUdRMCjn56_1iXA6-9eYycN5-Oyr9CnF7BA2_UETetSFL0YCrxwd58unH3bVph13T-o30NA-_VrOUGLBv-LmLwU8U5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صداگذاری‌باورنکردنی جوادخیابانی مجری ویژه برنامه جام جهانی روی آرناتوویچ و خداداد عزیزی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24667" target="_blank">📅 11:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24666">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJGo7SDqaICzaj6BRPpDkzTdo0fobIsISw_2GIOXDiG53zq1bs61zTW_GbMdCSXJD-0g67PUUQau7lO8agEhhskdEYnT2oiBWLCSyVF2UB_8BIDm99hWqka1zOBFOeIK99Q6jpuNALqRkI1rYX3Tx_38htMMjC3T93pITdQQa0BvoL7eojA-yzCx1xxduWGCa3kEByPuwWav8fk7lkJFjqsQIbV8lfZAuBGnz80QRnaPqBpj-RL8ERwem-IvdlsynyhgeTe-ca2FlD374nwlRDxd_dzLe3mQJ9NjpGhzXqPj1q94xxjNCWRwJP9gec3m5kIFVKTffdznfr51E0_u_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا؛
به احتمال فراوان باشگاه استاندارد لیژ قرارداد دنیس اکرت مهاجم 28 ساله خود را فسخ خواهد کرد و این مهاجم ایرانی الاصل احتمالا به لیگ برتر ایران خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24666" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24665">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7GIVaHIwP9d79BBhfpHRr8XnOSmbsp7D0xi5HKhGAJWnfIeF53wzgqNzsnBym9gt1mNhF58fTZGO0vw36zuu23NOCA4fjIPyO4eK8H-1nYwlna4hjeD5bN_3nixdhLAGICVwBxBDh29aDxYWEHBLUkagyR6U6wVXi_rCffUG9YIaFOWwqzdcrZVB959USNH1U9uFzaTdj_GWGZ1JYnzlppZbh8OtavmhfiS5_ue6B2ME3VEZkQa8bwai49oi0HDZl2U2j8CqUB5KQ2rKs0r0sRK9h9i4pS6b9nvw8DE1Z-8e_nyWawY4EZywVoZ-sAO48jkcUagO3A6l-eFGPFL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانزدهم نهایی جام جهانی 2026؛ صعود ارزشمند و شیرین کانادا به یک‌هشتم نهایی رقابت‌ها باپیروزی دیر هنگام و سخت مقابل آفریقای جنوبی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24665" target="_blank">📅 11:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24663">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbZ4bajx4xCRzfQIErxohIgMy_nJexCW1waS1es7ILQY_Fnkk7d3DA4oneX0k7WM8s6AXl21FOHpD-sHSzrub2dbL2sepq7HX3xuAbU9x6mSl2OBGyZtCCNPaZoRVMEi1MUYGYA6JOudT6sqWx9qte8aL8g2KYldi3zvy42JEn2M9TsDAp-57y_ZMm_XXa2WODmNiYo03E0nLPEu4Hllg1rci--fhb9fThnxzzmhHSkJXlCkcuwwSM1jrjcbI80WfkmZSgOzO14wJp-BgyTsVdAG7DF12DGG9wg3tPyzuMRr4qTo5nj2brx9YlIRTYsV4GcIdMJjbPWuXbhQpnYe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس درتلاشه امروز برای دراگان اسکوچیچ بلیط‌تهیه‌کنه و این سرمربی کروات ظرف 48 ساعت‌آینده با دستیارانش وارد تهران شود.
‼️
بعد از رونمایی‌ از سنگ‌ اندازی این مدت بازیکن کهنه‌کارباندباز سرخپوشان‌پایتخت خواهیم گفت. این بازیکن از وقتی فهمید…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24663" target="_blank">📅 10:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24661">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d6647db.mp4?token=REvlAMeBlklj82DVDlWT11WZUCyv-C8EM_ILyoiXr6BxpOIF2-V6rUeNIPr2rQmjWNK5aXE9ScANOjGh3LrlVf27Dwzzyl9K7n6cFXcSDQ0qbMfW0T3vO5PsonOtsd5vGk5awdnD3K7MnphOvfalLS_tpQbBb0bRgHen0UawmFJjVdt0Phq_zI0hc9tiCKwSkrX2jLcO4zM87ueAbqnpvYpoAy5rccxDG8qXWP6OM5Q25dPD6CnocVtnzyCtKw7RVd5ODCtw3IxnrviW7ag_mx5s79eTP18YRKXIJ-S2ipRcDrzLPa8iDVA0w-bwHVpxEjLX1XNXwFn5jj-H4eCp9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d6647db.mp4?token=REvlAMeBlklj82DVDlWT11WZUCyv-C8EM_ILyoiXr6BxpOIF2-V6rUeNIPr2rQmjWNK5aXE9ScANOjGh3LrlVf27Dwzzyl9K7n6cFXcSDQ0qbMfW0T3vO5PsonOtsd5vGk5awdnD3K7MnphOvfalLS_tpQbBb0bRgHen0UawmFJjVdt0Phq_zI0hc9tiCKwSkrX2jLcO4zM87ueAbqnpvYpoAy5rccxDG8qXWP6OM5Q25dPD6CnocVtnzyCtKw7RVd5ODCtw3IxnrviW7ag_mx5s79eTP18YRKXIJ-S2ipRcDrzLPa8iDVA0w-bwHVpxEjLX1XNXwFn5jj-H4eCp9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
صحبت‌ها و عذرخواهی هاجیمه موریاسو پس از حذف ژاپن مقابل برزیل بدون بهونه اوردن و گیر دادن به زمین و زمان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24661" target="_blank">📅 09:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24660">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYT94psv9YOwgpqDixXClqQ1aRPGwXcnUen0daK2Xar7Rz_kfoZJhTt_nTV_P3ONKYrlEFXjSWnz8uK5481sdG_psvuSFF_w4j2nh148U80b3UxCIJiSPxKZrlxLDtduLZgfxQHMor_UqZsgoPb1Powa3PCGwsSw3wJdFBIJp_V2rur9iEAj4ZKvwuR4xAJ8ezfLPSkbVBxgPBYyvjINmYuwTYAWaHRJDqedS-ryf1lMeqJK0uR8IdR-jobrxe2j_9ics-KHFyiWFeDCSQhagC2jy3Mv8Ru608mincIYZctYtPPlTgpIOyYsbzaFuQ8QESZMkSmdoi3uuoh1odLsIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سه‌فینال‌آینده‌جام‌جهانی فوتبال در این ورزشگاه ها برگزار خواهد شد؛ کدام ورزشگاه باشکوه‌تره؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24660" target="_blank">📅 09:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24659">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24659" target="_blank">📅 08:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d--AlyY1PKyhhonGUbxhfEzqX4oS28BMsEzCN3lYjlSd4xuMQK6DkSNbgjGRMo5yx9UbIHK8qQBq2Um7nWX7PIOM6uJ9YqZsajlzSoaA3JF0Nt2c0vqPFFtr5rQVfljpXbLyQfz8hDp9ueE_tcLSTNewV9857AYtFGjwxBreXhohxmHZIXVMBev8CTW7VaifV9jWyiEdfZdXiMCfj6VbfNVUKrlCoX3cHvAF-mgAF2qgFu0tXEuh6anNiYMez32M6bo4TN8FbuawriBWlJjdC7dGs_3jfIfcitKwvHPWKneiX4-3DEBgLdonj9BuN11Fs3yHnz5XBys80i19KxIjDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی؛  حذف تلخ و زود هنگام لاله‌ های‌ نارنجی‌ برابر یاران اشرف حکیمی در مراکش در ضربات پنالتی؛ مراکش در دیداری سخت و نفس گیر راهی مرحله بعدی رقابت‌های جام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24658" target="_blank">📅 08:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uD4YzDLOCbq-V8Dsbx38CZCfbnxBWCq8p4aqv0AsPnbEbZ8geJoBpzy1rlxQYHeqDeAdsgxiEdKlBrDNoVPfi60eLBfs0v5qGHqymQ60mwiLPF1P2MoKMSWoSvsDa-CGZ6tiFoArOiuh1eb50dWpxT7DJWe_mImI6zZQC85pgP1lqY7R96CVVmpl3F2EVVGRwAQdD9Nt7V6Xuya-igNSaFxeAH8W4K26BOkfYSo7PWnxlZc4WIss6QeNn_R2Eb5U4mnCMS6sBaW2dhCJTILjEB2Nj1POgbeMEIjjsOr2HWC9b-ykU5hSmPh3mEEW1TTxeWIrRp6MonKxgr5fLUqP6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی بعد از صعود برزیل و پاراگوئه به مرحله یک هشتم نهایی جام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24657" target="_blank">📅 08:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24656">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V8xsVs4O3zYVr-t6j5VqIxLVX_TPhZ_pdXKZrN2B3vOyNSvEdDq3EVLNLTcDS6qOId1TVf34dCNhghdnUU0dfs0fOBmNS_2s91q7ur6rPW_I9YIiixuLHO0gHuh2ehuZkDHewjTHozF6ik8g9MpHrWOtL3nKivNbRabtNAkFJLGijK6zWKMhvw4aeILqlw2aXYQjBZe2O2axnegMPo8yZk4NgQXnget_gnVGMfIrbUViac-QgKP6nAe4pUvHmIH4Bv34f9yi-AkdzWouja3-0GzmX2xxSydLtKab6zcrFFj8ZqfHP0mOHMB2y93VzEkJ5liA4_9CYHR22u8y5Mc8lV_4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56f71a194a.mp4?token=v7RqjOxzervAeWLnt9eUD-PS_cE_dmDTD3KdlRC2R4ma5Cduv5QKBtKeuEfR_L3DaExluuCPYswXCBjU3BrRB874nlBpwoePb0XMtj0XC_TVMxCwbXlZ-49WUTXAuUNgeScTGOjkPikP4UGKtGBP-Evb1HwvBU3U5xMOYHzT2M6c0Lo-kxEGExzuiemGZY4dxVbRElMMWJUeC1gGk1eCXerwyed1Y-X6L-fJeblDdsjLWGh45nvn2gCS0q_jMru-vgoHXBp0IWIxdnZy_AfofX49-9uUZNLnj_jvKQJIIM6bvG9YYTf7yZcdkHnORLEThZtQ46ddWq_QnWL_hY3V8xsVs4O3zYVr-t6j5VqIxLVX_TPhZ_pdXKZrN2B3vOyNSvEdDq3EVLNLTcDS6qOId1TVf34dCNhghdnUU0dfs0fOBmNS_2s91q7ur6rPW_I9YIiixuLHO0gHuh2ehuZkDHewjTHozF6ik8g9MpHrWOtL3nKivNbRabtNAkFJLGijK6zWKMhvw4aeILqlw2aXYQjBZe2O2axnegMPo8yZk4NgQXnget_gnVGMfIrbUViac-QgKP6nAe4pUvHmIH4Bv34f9yi-AkdzWouja3-0GzmX2xxSydLtKab6zcrFFj8ZqfHP0mOHMB2y93VzEkJ5liA4_9CYHR22u8y5Mc8lV_4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24656" target="_blank">📅 03:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24655">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=mpMbIWE-2nNAztH5k9mEFsLmR5DVbIsiH3LJPPekiW2M4qZPx5ybhbCR09qsMSNMxWjaWfAGrZRVsZQG3lUWS5A_GfeJRYsd3_YSnTsCRRIsSRdxdw_gfOp7MKBQTYFsFw4ZW6dP7tx8L6bJbf06S4609YBwfn8R1a_wcVa7GKYxOP_Ydek0NVoxXlQgoATd0Uo6DUhD5auEFJEkIg_4wejyFV6C9D6lMqWMXitYNUDAOfUlZrf3jWz6U0x0xlJMWXwglxnNHE3R_fRotpCirXPaUGd6zO9CFxdOKNbH7fS5EwkEU7_svTwp5aVjRVH5qjMPZLiJc_RWhLAzQBDQYaEwFedZ9W1fWkSntCI4Ybc2X_VWQQMGQdhcIPNLq3hJY7_xmf1tzLlxGBtchTDr1Wh0WpSCGSovrfDWPiQqMnvIyrsdDoVzpaMepqdmHfGfGQSUVgW8T91euV8s8eAbNpYaU8B-6P_tgiKkj_dEkrymU0jxpisjJ-OV5Lt9ls96aIGfbmBmLBLRStzJ3rSVkPZAqoAW-6qfgJO89AjIacIvhjDfEUGHASU029nPkBwio467F3NutzBPIwwys44hZr1ECv3ovmVGgnQZKPma2u2vodMKFwfM8ko0Ximo0BGWDQOR02drOZXbdT-4--0joX2XulE3Lw-kch-gGUKvIuk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14530aa1d.mp4?token=mpMbIWE-2nNAztH5k9mEFsLmR5DVbIsiH3LJPPekiW2M4qZPx5ybhbCR09qsMSNMxWjaWfAGrZRVsZQG3lUWS5A_GfeJRYsd3_YSnTsCRRIsSRdxdw_gfOp7MKBQTYFsFw4ZW6dP7tx8L6bJbf06S4609YBwfn8R1a_wcVa7GKYxOP_Ydek0NVoxXlQgoATd0Uo6DUhD5auEFJEkIg_4wejyFV6C9D6lMqWMXitYNUDAOfUlZrf3jWz6U0x0xlJMWXwglxnNHE3R_fRotpCirXPaUGd6zO9CFxdOKNbH7fS5EwkEU7_svTwp5aVjRVH5qjMPZLiJc_RWhLAzQBDQYaEwFedZ9W1fWkSntCI4Ybc2X_VWQQMGQdhcIPNLq3hJY7_xmf1tzLlxGBtchTDr1Wh0WpSCGSovrfDWPiQqMnvIyrsdDoVzpaMepqdmHfGfGQSUVgW8T91euV8s8eAbNpYaU8B-6P_tgiKkj_dEkrymU0jxpisjJ-OV5Lt9ls96aIGfbmBmLBLRStzJ3rSVkPZAqoAW-6qfgJO89AjIacIvhjDfEUGHASU029nPkBwio467F3NutzBPIwwys44hZr1ECv3ovmVGgnQZKPma2u2vodMKFwfM8ko0Ximo0BGWDQOR02drOZXbdT-4--0joX2XulE3Lw-kch-gGUKvIuk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24655" target="_blank">📅 03:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24654">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b74cUPP3v_YVTqgX5s3gGOn-iKsoBSdNsFU8boP1RKVpJV2-BYSS-loCsWQhW_XRGnHvp2DC9CMtdMc_Z3cXBLrm7Dze6hdeEa_8DFHvVAOLpwQ9L3KBskKN5lYhqXyjeik4pU931oG-zMYcMJK8oMTmb8J0JZteDPhIWTXLcoyd-XO_-HSrx7YL2DnFD8ckIBQ8b6kxg2nr98q-FLgdJV8BQTr3_58ICT0Zg0Q8Qz-oTsQ-xeMcxeHEWH2ebhBESABH36E7yomi6Ll2tKWeoeZrHGe4D0QHXOFilMzHjz485fHP2dFH9vS615sxYTB5WI5hBlal4e_9bZZ3gfY2mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24654" target="_blank">📅 03:31 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24653">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=qGKoT_mOjJ8zQ39p9N1Eb5z6ZgXpY81eI8eSInUjEEOMfO4cmQRkQueXF7CDcuOK1BB4YIM67OE0CjjdzyzGsPPrkyIa92UxQDhJLuLYfN6kQckcXUcNr1pWwzZU3KgkJRoWVZQY5Vp88szLqmWOYbMtNmUkjvpOMFo439L9lAwZ24ZaGnRTSRkbYPLbrAM3OZOhxgPlUQbrcl5_a2ruIGEqXS_CqbJvHyzazKe8EQ9fupxOPeJaiMORP8g_yph84JbX7waeU2UtAmDF67vFeFr9GKEW6N7I5goYopWYtWenoPLP9vaZFgI1pga9iCoUemYa0ZBR5KPikLRsaREloQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef2bb58ba6.mp4?token=qGKoT_mOjJ8zQ39p9N1Eb5z6ZgXpY81eI8eSInUjEEOMfO4cmQRkQueXF7CDcuOK1BB4YIM67OE0CjjdzyzGsPPrkyIa92UxQDhJLuLYfN6kQckcXUcNr1pWwzZU3KgkJRoWVZQY5Vp88szLqmWOYbMtNmUkjvpOMFo439L9lAwZ24ZaGnRTSRkbYPLbrAM3OZOhxgPlUQbrcl5_a2ruIGEqXS_CqbJvHyzazKe8EQ9fupxOPeJaiMORP8g_yph84JbX7waeU2UtAmDF67vFeFr9GKEW6N7I5goYopWYtWenoPLP9vaZFgI1pga9iCoUemYa0ZBR5KPikLRsaREloQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هالک‌ایرانی‌درگفتگوباابوطالب‌حسینی:
شمشیر خوردم و مانع کشته شدن یه بنده خدایی شدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24653" target="_blank">📅 03:19 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24652">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4Wa3cTw8WEb55RHLVGec4nYdlY7K_ezRBaCaY2cThT4EnZqkespGATTfXrVl35g5n7pHMpnsZK2gMKQyovP5JqGpWbIL7RHr3FTPc_1ltAECrdM0yCi9ndf6Jhao06ZmMvVgMZ8c6XIFzumlGxTztj-I7Cap5h7_ApOJFfZabT-ZiSfTbL31sr_GzHU-b-TNcbWK5F2dIHQx5OJF56uQy0dBZgFewxO3g73khC4ngQyGDUimdrEsDwMVu_WeRGPoF2XSoBBggz2rxyCDKGWBWED0bwA6QwgurLlMAgX0aP4pTff_dXjKKWc8JOyF6KDcOrRq1JBnJIKNKGdwViVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛‌شگفتی کامل شد؛ صعود تاریخی پاراگوئه به‌یک‌هشتم‌نهایی جام جهانی باپیروزی ارزشمند مقابل ژرمن‌ها در ضربات پنالتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24652" target="_blank">📅 03:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htlbusx7EqCj8-ywoaHYQV7IoSxwd7bOlIvqhsz_WNEsRvM9GmW70z4Q2pQ3xcPAWCSQzKUdpDXON42y4CGy6w1lUKr18uPP6t4NadthDBI51VAsvh48jnwT6-2wysbuiEBhTnTganI8QF5-wfu73N7f0d2lLJeQRM1psDhVxe2P-5VV2Pm2AC-SwU4wydgPVZ6Y0ssOlIFKwk1aaXMvRweoPTksnfLrdx_1JodIg_baQlr1CDoL2gJVfjD5SZjwSeuH7Q92Tt9DoLb092Q57OfESO2s-glVEtN_X2w6UWTx3TVnQhVrXHLBlFQHLE-oaRgC-YOcr4RCstHcKm46Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آلمان‌امشب‌از پاراگوئه‌گل‌خورد؛ آخرین کلین‌شیت نویر و آلمان توجام‌جهانی‌برمیگرده به فینال 2014:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24651" target="_blank">📅 02:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24650">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=Suskf9FIOlS_WeGcI3E5XNZjNtsyzhc7EUML0rmw8ToX1Zm8ABvRHS-QHW947Hr7nOJpJuHRyrDhCfqm13Lf1GkB4bvBLxE1JmusD5s4IiuFb8oxVJH4VNEei_ghemROiK5liRGxdgrDYgWEFuY4hxPhOuC4FK9bQntCv39EU_l97RaQWc8Wv5zgAH936rOlx7pW6rpmnt5X55mLZXfxWYevLAYgOI691o3jmvXYlXS2ek8AsBuZx4plcVGP4prSd_ZCj1bQxRT7U_8d-DDx2WW862zBmgu3BW3MqMq2YOILrLYqTZlMkTwzZbaaNufL5Ct8lAm1a0l4HmT4RPezCZYd0VHAmutJq5rryXmwIPdCjc2IxREKq8-oN9apdukm1VtGC5JNqKntRhXmHeh5mFlG0qCzYtVc_fru58Sk_DxC90oabpG6EwjlPsAx_frBGpmwuw66CsZnn0S-_TTM_TcN3Jxs2XKAUE-pbI8bc4xSuTuMltYaL6yJiAys58LH6ODtndgJz-taJ_vvclDPh_nPzHIV2Oakx4iIDmYNgrxNthmPLYYGOZRXU16URhNCmf8G4hInTuhL_rTcSH6LnD6Ye7oaO-FKRwadjYbefmtwKiWU5IDHxPZdbHQNKrut39AI1clsxSypjFJtXrRGFjRK4dyUgrzRSrqOHs1R3B8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8d0fcfa32.mp4?token=Suskf9FIOlS_WeGcI3E5XNZjNtsyzhc7EUML0rmw8ToX1Zm8ABvRHS-QHW947Hr7nOJpJuHRyrDhCfqm13Lf1GkB4bvBLxE1JmusD5s4IiuFb8oxVJH4VNEei_ghemROiK5liRGxdgrDYgWEFuY4hxPhOuC4FK9bQntCv39EU_l97RaQWc8Wv5zgAH936rOlx7pW6rpmnt5X55mLZXfxWYevLAYgOI691o3jmvXYlXS2ek8AsBuZx4plcVGP4prSd_ZCj1bQxRT7U_8d-DDx2WW862zBmgu3BW3MqMq2YOILrLYqTZlMkTwzZbaaNufL5Ct8lAm1a0l4HmT4RPezCZYd0VHAmutJq5rryXmwIPdCjc2IxREKq8-oN9apdukm1VtGC5JNqKntRhXmHeh5mFlG0qCzYtVc_fru58Sk_DxC90oabpG6EwjlPsAx_frBGpmwuw66CsZnn0S-_TTM_TcN3Jxs2XKAUE-pbI8bc4xSuTuMltYaL6yJiAys58LH6ODtndgJz-taJ_vvclDPh_nPzHIV2Oakx4iIDmYNgrxNthmPLYYGOZRXU16URhNCmf8G4hInTuhL_rTcSH6LnD6Ye7oaO-FKRwadjYbefmtwKiWU5IDHxPZdbHQNKrut39AI1clsxSypjFJtXrRGFjRK4dyUgrzRSrqOHs1R3B8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
صحبت های عادل فردوسی پور در تعریف و تمجیداز رامین‌رضاییان‌ ستاره36ساله فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24650" target="_blank">📅 02:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24648">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=u_84Yk-gbYr1cccsdlEtqI_tSQByzZKyCmDmkN8rkE21kI_SZt_GuFQbzIfv4dGhL88Lsl6IklKLCHj3l1XQMA8VlVHxqKmCtqchC7O8yBHuFyPWXxvUo9u1mJxahPUK0EAmNbwiops4CLeJNFtGhSj-YbJj65W8h4yg9W2m1zgQFhTG0Y8V9YYzMUe_8ncsHPTyHFyOJKfX_MXqW-6Nai-UiEo-r6w3B_MkhJWU6R4v5L31ysn7RKENXTpOIPfL1-u_TRzDnPKqd_cakT3ZgUEYJ8bVd8l_9E87VWlLjYH2NvApXD0MN88ecLuq11eV76H7vwvy3CepHHiSQqkF5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ff3a278b0.mp4?token=u_84Yk-gbYr1cccsdlEtqI_tSQByzZKyCmDmkN8rkE21kI_SZt_GuFQbzIfv4dGhL88Lsl6IklKLCHj3l1XQMA8VlVHxqKmCtqchC7O8yBHuFyPWXxvUo9u1mJxahPUK0EAmNbwiops4CLeJNFtGhSj-YbJj65W8h4yg9W2m1zgQFhTG0Y8V9YYzMUe_8ncsHPTyHFyOJKfX_MXqW-6Nai-UiEo-r6w3B_MkhJWU6R4v5L31ysn7RKENXTpOIPfL1-u_TRzDnPKqd_cakT3ZgUEYJ8bVd8l_9E87VWlLjYH2NvApXD0MN88ecLuq11eV76H7vwvy3CepHHiSQqkF5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
اینطوری که پیش میره مکزیک سال بعد یه افزایش جمعیت چشم گیر رو خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24648" target="_blank">📅 02:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24647">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPH-ah_z7cVGaUzRL6BO6a_UnxZf-p7vXWssgrU78rmJdyInBj1VtTpCcKXvJ6T-xrNQQRLxfZDyoPoP6tNn7ny-0Nt4nFFmL7-uE0yNxx0gcZpAKAczLbkfEHpmbzelt8AnzLx_maYstRZvYojKqfr6KCFZasih7GSyIXzqSO5ZhZ2x9H-hu5I5YXpWeRtiqZ459RK6E68x-2Ts4I-Cm16pc3lQDR8QfeM6uyMKlXKqxZsHvgcPeYwKqwYqVQP9qMYuDD6StnlNAfWpEk9fhE3tdEt5C6GRNNBQbmtDSmHNorX_u-fyQJeEakAp-o9WzZJcxfX46JXnNWw2LF2_vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جواد آقایی‌پور مهاجم‌سپاهان:مردم عزیز اگه تو رشت هستید و نیاز به کمک ضروری دارید به من پیام بدید، کاری از دستم بر بیاد براتون انجام میدم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24647" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24646">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‼️
بازیکنان چادرملو به لیدری رضا میرزایی وینگر این‌تیم سرود قهرمانی این تیم تو آسیا رو خوندند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24646" target="_blank">📅 02:10 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24644">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3SS3rjLtgsJi25KRJhIWQSynZgGDJnUS9OJbqA9jQkW3nxHv50VVpFYIyEbvSVHcJxPuG56zvHKtClUP4B_Q8YtjUBWj8VWXa4_zCyFWgm9IyzjspTX_PqiQhXhinG-S3Vwge-7eszotOn2e97ecB_GaqDR4BHXH-9bcuLN6e9rFv_YE9eSiz7gZLW4KEeyBxmKaVYYcWRTCyV3JQorakkxJNOI9xXsT-j3HKmE_2ABKwK1mDHujGo2YK_AavHU8jvvPFBDvIKPX2DNK2L5rEsHNyGQYv08PpdmFV6v2K4SMTxENiqpi0GyzssaiPoNoR119iE1kZ6Drn6vUQS1tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
#فکت؛ علیرضا بیرانوند تو جام جهانی 2026 :1 کلین شیت نویر تو جام جهانی 2026 :‌ 0 کلین شیت
‼️
تعداد کلین‌شیت درسه‌جام‌جهانی اخیر: بیرانوند دو کلین شیت داشته. مانویل نویر - 0 کلین شیت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24644" target="_blank">📅 01:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24643">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndjwXrF0l4iyfjWiVzbtSDWi8o8ToTYO4005CIOBBtWbUMK1Aa-U6tAam4Koqqunp1qWhQc_S_8l6iaw6hVLJYoSSoatozZd0HxlvVla1AP3puUh6YMfenE5gl1p-C9lkHN106hDTivkc8MhgfoeSgwt_x-ilpoyE6d8PoIm8mHBwI1fhNYLroEmLRqVIuVHEmXj8oNQ72qe44acM0G2QBHrizDka-RQZSAsoqAzCHjDBdEHAbmg2ehtK301edH6jujlHUJxFqdG6TilKdf1uGsPdU-G3jmqg_0ow_raSVKkgZ-0CcYr1j0PmzEDzj6BDPNa76JkgQSNeSKnXou1xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24643" target="_blank">📅 00:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24642">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsZoZAGIB7qsO1ryUoXWWJbHzczBWEPHWfhQdPw8B_JGkkaDOL5PLNcL9DGA09fnNeVXTcSxEtq08Wr3UtntJJDOEHRq3EkrYzeU09-QtlJ4wM60EV2JhNjbYDt-DpeKHYUOFkQglhUKTjC-ZOfVxdsxut_sVmxYobpSld53YE3W9qbMmsYnSmllP21PFlTTlhcNyLnK5UD8Rg4n5wTyYs9lr_CbfYfDN689idQGhkHDPX4CwaxFq0-Y7nBea775u7REKCEpBiSvb5tBVCtq8yqk5PX9pKmV7mMnyDqBAQmk4Qv-j15I2oi9BzwyZE2Q2elscHVnE27CWK4P2z3Emw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🤩
جادوگرغنایی: تیم ملی آرژانتین با تمام ستاره هایش مقابل کیپ‌ورد غافل گیر خواهد شد و باشکست در این مسابقه از جام جهانی کنار میرود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24642" target="_blank">📅 00:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24641">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO_IFC0A0UJwwb_COiaxFiH0ZcXRpL6ESMWqyjL__eH11K-KqcgX5SkIF22fM6SaAgmkI7lVlnfVr7Ac2RTB4BvJEqNybwywoEr70DJrK0cM7ckHPUOd1Uk4X-bat2vqt4QLKL4UCWP3T60KAPL8jWFWW3TDYDHZ1JZKmCXvERlB-ya7hzIESwcJ3HbsAEhDsT0GhP4jrXfwGY_UaCHHOMEOr0URMnq-kEeVgYPI7jnEACdE1jHsnHcX4pufMkqQuaCU18rk6lv4fr-sZMCX3wjPhwliW_ENB4LrUFnDPBNJYLBCL77qvtioUdV3bo8IEyhK-efjzZwbtViVUKZvzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق پیگیری‌های رسانه پرشیانا؛ بخش رسانه‌ای باشگاه پرسپولیس پوستر خداحافظی از اوسمار ویرا روآماده کرده و بعد از تسویه با او منتشر خواهد شد.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24641" target="_blank">📅 23:48 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24640">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=nV22I8_tuQp2n9FmJz1gxIkf8A8xSJR6thR-fGj0SdQcjN5J1WsYCEcDqQitEbp-KOQjDHWdN1xlYZzvnwb1Z5Nl6YXu6L14MHjR4GIoCYr0UpPNkNtzxAR7ZNleBd5zunnqmK7nMmA96DqlwRCPdCTRgE74a8lvqgnS8GkrniO07UioOYpWgBCmT6QhLwyVtELnVlvv9xcBChy-7GT6r8eSxx0YoAyL0DAf96Y14jztopUBpXUuWPSDO99e1awtRePYe8E42QAWBfMbWiJffYioCZNKUoM3oJLPQvDUdMTsj0fzyl07_nd8kDReCTcZluj9G6CFJRM7SZ4Stgi-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09c7fb1ae.mp4?token=nV22I8_tuQp2n9FmJz1gxIkf8A8xSJR6thR-fGj0SdQcjN5J1WsYCEcDqQitEbp-KOQjDHWdN1xlYZzvnwb1Z5Nl6YXu6L14MHjR4GIoCYr0UpPNkNtzxAR7ZNleBd5zunnqmK7nMmA96DqlwRCPdCTRgE74a8lvqgnS8GkrniO07UioOYpWgBCmT6QhLwyVtELnVlvv9xcBChy-7GT6r8eSxx0YoAyL0DAf96Y14jztopUBpXUuWPSDO99e1awtRePYe8E42QAWBfMbWiJffYioCZNKUoM3oJLPQvDUdMTsj0fzyl07_nd8kDReCTcZluj9G6CFJRM7SZ4Stgi-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24640" target="_blank">📅 23:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24639">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1DHjxTbxWRRT1Gj1_01UUwpJ0SFA13Ej_a79zuv6ob0il9Ko-GQNgVaQxgCXxA7FIh742G_-VpDFD94WazgQ6v6xzxacO2epoZkkoHd2LqvgRZG42GwAdDrbA_Brhdy7-fThHdteuooAYljdAALkUhWlBJRmoQ_bFm9ZgDlZYZ-1LPJEsGjykeZoPnvLVmKcG9T5jFYXGUKDjKjUZ8elWHd61QjtdsHxOplG4jBpaFjMKwAzWB0_f6zz-NfKckOA-_9lN_At92pRpg5VTN7i9YtlcoBwGskJ3m4RGFojP_5t9aupsyzgdaOyhDL3Kh6SKLdsc_7NSirnrTSXYkGGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
سرمربی ژاپن بعد از کامبک خوردن مقابل برزیل: بنطرم خدا با من هم سر ناسازگاری داره. این عدالت نیست. ایناهمش‌آزمایش الهیه. خدا داره منو میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24639" target="_blank">📅 23:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24638">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZllbxzJw9la-Yns5yxM9KmBE-z2YFZDXdubuYoiahMCaU_uquB5BYhlY6oMPfmnQZ4RDvJ-_XMH_lc1mn8TSGi-i8aWJQwiZTY1idZRRWfK7HYQnyuimXl6wYK6VuQ5tXyzihA3FilFyDgb38r4-jwVb09LxkJbprbk2BdW9eCoWpp6EFg89S-tVR0u9-A9lrngbzOtaOHUkVKgpFkxy3F7ZK146HJWfmBuyGaIeVogn-WXrrW8uUBAKIv_83Iy-otyudmCy1_ngYuNRLZjB8xOoriStjotmXzBLxbk5FaGNtHuxmsM2Zs0VfpTQupOsuAGDEwTXvGI5c1a4xMT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم‌نهایی‌جام‌جهانی؛صعود دراماتیک و نفس‌گیر شاگردان کارلتو با برتری مقابل تیم شایسته ژاپن؛ سلسائو بالاخره سامورائی‌ها رو شکست داد و منتظر نتیجه دیدار ساحل عاج و نروژ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24638" target="_blank">📅 23:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZtoFsfPWRcoFG-M8x9Vys6JupPq-wXW1_MqfO5V-yGFvkmmQmtKaxSO6DyUp6qugT9Z07r-bdEoE9FwLUCjTG3YRI77C6I-BugRydcOc8EXDsEDOYKjTJDaxIJ68jRBjYksUS24G5Mdq18pDmNxdXE1uaukAndwQS0xTz3rlqkpxM1HJ3cd-LRr7thktnfAgoEoGddqi2ISeJrgnCmRpuDDn6urCtuJsIEwjDv72mtBBRrjtHfva2MpgfY0zbWJtkTdtnhY1NsFv5yXJDskT8v7_V5Spv--Ka6lOmRQSIUfgByqkPbNMvrU8cml84AnDtwcwSVAdo--B-gg3xoRKxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ فردا؛
از مصاف مانشافت برابر پاراگوئه تا نبرد تماشایی هلند vs مراکش و جدال حساس یاران هالند مقابل ساحل عاج
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24636" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-R0Q8jAFxSoONP--oKoigutYFHcpJSTLxv3GXHrj1x8xcM8dBBLX9v_4uBo8en3X5E3JdJxxnJjAPNCgrxGs-8K7KKMWEPDucV8GswYaQH5fuybDbrgW8fwYKsvLjph2TZK-pgGFxvMAarlt4uuz8LJmorr8NuBuE4sCT4y_hmjJi_qGdrmd0Zk68XmDGFVH9_aWU6MyeUdfGC0DfTHHS12V4-PS9g3b0QXGqE91vPidjKLw-LQTeGbzhVRWkqjKCXed3Ekail4QxMILE_mnOsfA71he3cNUBlYn2MQFdCISuGFKWxkU8W6M1Tse8NdkgTVwcOv56CJOO0iOjJAHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنهابازی‌مهم‌امروز؛
گذر شاگردان آنجلوتی از سد سامورایی‌ها با گل نجات‌بخش مارتینلی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24635" target="_blank">📅 23:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItgnVMNQj4LaNCYEy7Y171ZUnORDYwlyGZdLQLpqW75hoT69oPvV71K041M2-HXBTa0PZ64E9n4gH1mfweRK7QEYT9EDIMgpPu7rPvLKwuef6BId4q0YvdyvwL0dw8U1KrXOo0XG8R8Gf7dH23oDjjmJ3ZiuhsLzwishX3QHIDaeV_I3K6JdaLjlTu9GQOQ3mrdxpEZ9kZn0gDuLIlpy45O-fbI6QcHbB4a-laFNFPPVunWCoDZkR8NHiTISamNfJ70BS1Z3xVjY1Mz8J53mH7A3Z1kEwThcvmuL3jMBDtSUQl86cYfVKWhtoJeFdR4QxBYsRLYU5r_2O8inZ3dztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M3lCx7zoQIxnHnFWMB2ZZgk-lvFfe6eLNz8DSdLYR_MEcYdbt-_eZQno3ropDnercSBpLMCQ2GlpKA90aQgBt3_zp5BbK9PL2alviulA8TBgnxIdw7hl7_YwYXpk6Us4QUKbof-_YjpKIHADAb_J3wLP6XARfSy38mhW8Fc54cxkIIyz_RKSaP-c9eanG59kEMQAjEeb0Nq8KGXpuMr9rC6FcXB0gcud6z-lHgfqh4HolKdeQCgCIolYIqVCXo8yIWkJqUfxOoBHf2mFpsXDz1US31Yxzdb1kX7cil9JESYLPUJMBI370Rdrxf4CxR9oa6JBiKZN1AP8_3dwTRlAOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=QRTyklqJvsl4gwdMcm5Iez2y68E7HdqwkCcIe7PmsfT_Yh2JMGZGpoCUWRFF4fdhsS-Cxipw5h4cGjWyGQ66MtmUwgjNQT1-yFcxRawTdvXw-O1qqMCPDBSWGcKfRrmetxawoC_6Nyh81meUuL_EZsNHTnVOiEI2wUELeU8yE-2velgrJpccZMMdfvAI2uGCLyprs8VXZ_ZqL13Y6CEz3HHNhYfLLBf3-w_4Q8EFbyOfCyP6a-cQGAisosDYx20URP0RXFEQUunbXungpx6tCrJPEB5KJ1jdN5Sk_BIulF6YJXsjsNOYXp6TI2Pv3bmrq8_4yIcQwNbLfWf3VdfT8JIARBi8y5aE8cAP0nW4HPi2wDfrRlIWRYo80vE1EXA3cFvdv3OQTbeUabyqUfU9WBOD9Wypa84cdAjAOZi5Q8_w705iOrDBnZ8YjCn6lq-soOFahVX4SK4vxVxPSrZ2JHnwFoBbSn_SA0RKbSyY8U45mpiUxvNh-ifMd5Hj2HFCBicHOnYRVT1-imN4iA9FPDaL6F_ZIhngG8VwmzW4uy21vJVNL5m3LGWC9nF9wskBH-jMA27TTGlhch6AKYgCGQ95RTdxYYh4ImUkUO6WHGhlJIBu9U62nhU1H7GH5eGJTq6j_JMUev1II01zTusnUMfZ5yRlvygcybFiyCMrSS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=QRTyklqJvsl4gwdMcm5Iez2y68E7HdqwkCcIe7PmsfT_Yh2JMGZGpoCUWRFF4fdhsS-Cxipw5h4cGjWyGQ66MtmUwgjNQT1-yFcxRawTdvXw-O1qqMCPDBSWGcKfRrmetxawoC_6Nyh81meUuL_EZsNHTnVOiEI2wUELeU8yE-2velgrJpccZMMdfvAI2uGCLyprs8VXZ_ZqL13Y6CEz3HHNhYfLLBf3-w_4Q8EFbyOfCyP6a-cQGAisosDYx20URP0RXFEQUunbXungpx6tCrJPEB5KJ1jdN5Sk_BIulF6YJXsjsNOYXp6TI2Pv3bmrq8_4yIcQwNbLfWf3VdfT8JIARBi8y5aE8cAP0nW4HPi2wDfrRlIWRYo80vE1EXA3cFvdv3OQTbeUabyqUfU9WBOD9Wypa84cdAjAOZi5Q8_w705iOrDBnZ8YjCn6lq-soOFahVX4SK4vxVxPSrZ2JHnwFoBbSn_SA0RKbSyY8U45mpiUxvNh-ifMd5Hj2HFCBicHOnYRVT1-imN4iA9FPDaL6F_ZIhngG8VwmzW4uy21vJVNL5m3LGWC9nF9wskBH-jMA27TTGlhch6AKYgCGQ95RTdxYYh4ImUkUO6WHGhlJIBu9U62nhU1H7GH5eGJTq6j_JMUev1II01zTusnUMfZ5yRlvygcybFiyCMrSS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLvdmBBdp9_HS9s_9KZQBhjaoPLgB6Ed8Vit_y5Yn0TbqXBRwY9LD5mAlHoa03umOUNgfbSBmwR9PcugW6ehiiSE19M6PmrTyOo3h3M3g54e0x0h1gbHEZSYQn9W0d5ioPjGpvaHbXUshu6bxHtLXNV4kd0-F-dNfAHEEq9dhf0KI20OW2fEe5NHGD_IqPKs6lNea-oNaukoQrhAwGYLp2UsVRMMHz-ybqCmDmnSlOkTrubG4i02LC2FG_8OIPxGyc99ZiHNbfLfpL-njR8NRYFvupr_dPFwnfnPgcCTW3pBdB8OOHLe2ylHEGm-TS8HrDf4cgdsLVi2Ri9kE14Oug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=iuj9CJUNK55l5ecc9yrse6YhqnRpw48C7FrGymwKoU-yasXMbzNj8cQymtiBHhSDGPt0sELgWS4gShLlC6iJjnCi8wUZ7vlZrb07t8XTA36EEHR6dn93cfV7FB99OyIqxQGegv9ewewrzEfy7BRmMV0OdRdoywx6UqRkxmVPbs679dOfrmVm1w2jHdynB0NQQJtIHvQ0IF301w6GUNPJUksi_ku3TtEMEaxrMALgyw8Z-EO74-w20fiHHHSZmHi8qpiO5YoNc9bdFF0JgQtMvAc_ptetua1X-ZaswFCdCUfBF-xSAHDubyDRdTU3febh51YdYwUmWeTAkzlS9KPSHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=iuj9CJUNK55l5ecc9yrse6YhqnRpw48C7FrGymwKoU-yasXMbzNj8cQymtiBHhSDGPt0sELgWS4gShLlC6iJjnCi8wUZ7vlZrb07t8XTA36EEHR6dn93cfV7FB99OyIqxQGegv9ewewrzEfy7BRmMV0OdRdoywx6UqRkxmVPbs679dOfrmVm1w2jHdynB0NQQJtIHvQ0IF301w6GUNPJUksi_ku3TtEMEaxrMALgyw8Z-EO74-w20fiHHHSZmHi8qpiO5YoNc9bdFF0JgQtMvAc_ptetua1X-ZaswFCdCUfBF-xSAHDubyDRdTU3febh51YdYwUmWeTAkzlS9KPSHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=nHUiDeBwILYEJmH6gMQR9tt9f8vXAMO8QbjWNUj7uyz-edzolwpORHt_UObEyNkfILNbWBesTTbLR5XKvfyf33UZEUmFhuCAgc_9JzUhAXM-JW4Sn00jS621kbP0xQMWN53zEhAJRVM41l6WnNWsAP5HNW08KZfBVyzU6dq3pjlg99vbom2qUEmvotuKvwrmzAxzeUT0h3G0zfY-OJOTLbXesHtF91cNltD5Uj0OcVH907v_XcvtNHYhC_0lKieLowGfJCU3hof5RQXQP35QcpiNpp-3Mz_DgA6nV6qF0M6UvdRlw3P0EW3SdYf0ie9wS-RJDwXOe_RTGCCX0VOcWSxCH53pK8F2IEDkqrrl5n2QIp5WK4jpEJcRLwZBkIMoSF4p0wFP1wdaJQOY_hYBCu3rkqRk2ekJVD0hoP0DCYiYeIOSBwBrJWyGCXPugsc4lLXkIpspqxzNX2HXDO3ozphSMuauSSrQaB-tDZOnM0NcrNUyZdHXBE39aqB0iQJX3bcJDB8r-RH9_UywbmhsAfg_CET4p90OTOEufg4iZK9JMSxq6rAtSGHgiYWlHaK0rZNXU_O91RDqtOGCGMflf4F-wfB6gPRU6534ad1QSYph8jnitU5cAOCjrQ4boRpx4pC2THxvOdaPu6-1zT5QnpEm6XR2scxfi7a666JLh6s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=nHUiDeBwILYEJmH6gMQR9tt9f8vXAMO8QbjWNUj7uyz-edzolwpORHt_UObEyNkfILNbWBesTTbLR5XKvfyf33UZEUmFhuCAgc_9JzUhAXM-JW4Sn00jS621kbP0xQMWN53zEhAJRVM41l6WnNWsAP5HNW08KZfBVyzU6dq3pjlg99vbom2qUEmvotuKvwrmzAxzeUT0h3G0zfY-OJOTLbXesHtF91cNltD5Uj0OcVH907v_XcvtNHYhC_0lKieLowGfJCU3hof5RQXQP35QcpiNpp-3Mz_DgA6nV6qF0M6UvdRlw3P0EW3SdYf0ie9wS-RJDwXOe_RTGCCX0VOcWSxCH53pK8F2IEDkqrrl5n2QIp5WK4jpEJcRLwZBkIMoSF4p0wFP1wdaJQOY_hYBCu3rkqRk2ekJVD0hoP0DCYiYeIOSBwBrJWyGCXPugsc4lLXkIpspqxzNX2HXDO3ozphSMuauSSrQaB-tDZOnM0NcrNUyZdHXBE39aqB0iQJX3bcJDB8r-RH9_UywbmhsAfg_CET4p90OTOEufg4iZK9JMSxq6rAtSGHgiYWlHaK0rZNXU_O91RDqtOGCGMflf4F-wfB6gPRU6534ad1QSYph8jnitU5cAOCjrQ4boRpx4pC2THxvOdaPu6-1zT5QnpEm6XR2scxfi7a666JLh6s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcR_2RSmoR9DCkQDIB_qaiakxLoCVDVAvhQiY83hhrFO8B4wTmQ6RYznCurIxV_yt0QbM1GoUMp2EcZzsMKRyxMirxnLCnB1hezQwDu7Qj8UAST6G01nZeuJ0GqViLaMnfO2O1dx9OWvBCFa9AbJw1_0fUkbdkLGRSNbgLe8BgxzbM5Ce-yAUNFCxT5jqbm594TW-SPjay_pocoAcjmlayN9s86JBmCcOQbnPJxjHjb1KuVBz_Y6SisyvsuQK19hHio-TlGkdI4ay8jUzlEJ1_aXxFdansrFB1YoeWs4tUuX_oEDfcKT88o0J-O8y2fDnRDG-49M0TdtkpEUnXl88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=Up7UUkBfBmsIzGXxSjWqzjRoeNBONEG3V8QJoEbTWQEOFTPphFu5qYPWQkW3vHH4vYe6TRLCP_wRSMRuIJKrkGqvgLWxgBD_xcYcrAzwqdzA5Q7AAC2QLSaZ8cNLPyBJ6P9LTcQdO0fNs9LA8ACReA8r-_dNY7mk1aaVj_3-LzkFb8kijH7hMveAfpUYEGhL3v3QsnO6KLFhPt3ujd5HpgTOQEWiyMsu5Dcp_IwKV_KxfuJL_TpqyyZWULqduAKCLGSUW4-hDVgfilYfizC3ImvHwblntrtqfE2W7kjz__dUnELlIBr3mV_E1S2TF2IkjNKShINMWIxr_1945xUduLlIsEiLP82vs0_nHeMXpuJsfb5cMI-6EJSneBVjgxt_MUUINh06IZLMdGMArH4970PmXW0-s5qk4EO0fBoSvGEGGcwnZ-jFWAle1iGy5VmnpjZXugHwS-uOTE_uMat17cjv4a7SvhmJkH_RfbTOSEyO076OuT3bc8qCR-nEGCXmZeCWd-TfD47pOvEko54uTRcJq6_Pi1aCM1AXn_KFic4EQIIqR2fGzsHfF4JmVgaqBpchPCxbEpgpPX_azY96gp5T9D-uRiNC4tricevgn3yT3bfPesn6XgnHdP-M-dplVHZaZZ04rYr9ssVC3dirmpAYSqTXWwovb9N9N6ABjTU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=Up7UUkBfBmsIzGXxSjWqzjRoeNBONEG3V8QJoEbTWQEOFTPphFu5qYPWQkW3vHH4vYe6TRLCP_wRSMRuIJKrkGqvgLWxgBD_xcYcrAzwqdzA5Q7AAC2QLSaZ8cNLPyBJ6P9LTcQdO0fNs9LA8ACReA8r-_dNY7mk1aaVj_3-LzkFb8kijH7hMveAfpUYEGhL3v3QsnO6KLFhPt3ujd5HpgTOQEWiyMsu5Dcp_IwKV_KxfuJL_TpqyyZWULqduAKCLGSUW4-hDVgfilYfizC3ImvHwblntrtqfE2W7kjz__dUnELlIBr3mV_E1S2TF2IkjNKShINMWIxr_1945xUduLlIsEiLP82vs0_nHeMXpuJsfb5cMI-6EJSneBVjgxt_MUUINh06IZLMdGMArH4970PmXW0-s5qk4EO0fBoSvGEGGcwnZ-jFWAle1iGy5VmnpjZXugHwS-uOTE_uMat17cjv4a7SvhmJkH_RfbTOSEyO076OuT3bc8qCR-nEGCXmZeCWd-TfD47pOvEko54uTRcJq6_Pi1aCM1AXn_KFic4EQIIqR2fGzsHfF4JmVgaqBpchPCxbEpgpPX_azY96gp5T9D-uRiNC4tricevgn3yT3bfPesn6XgnHdP-M-dplVHZaZZ04rYr9ssVC3dirmpAYSqTXWwovb9N9N6ABjTU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LkRUMj2H81oCZghmO7kEEBsb_hjrhulV1ZfA0B-ypTQAE-G4AbToYFF5jflQEMRXCra4S0GoUi6fyP4Q4P500A3iw4PA9IkKRlmg4UYF03184UgeXmnTz9UIhcCsPN3kaoiRHsGZtb9VgiSJgCDJ-mQQHCBrbYwtiuUE7Yb2liMw2X-tsmPpEuu1UoSptbDE76nJhltUzTm-2PvSnAMrl6kM3N-qy9RJ-tcHKs_EBrgUA1geAbBQEkh-g_nNh-WyAOArRseqHBj1fWdRPCW6UECyG1J5_PbzNp8cQUxs1vtVoOi6DysKMh6K5Ipe8RSwMNbv9DZgiEU_-EZhnyeHWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
