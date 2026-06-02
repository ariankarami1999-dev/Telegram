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
<img src="https://cdn4.telesco.pe/file/t2Z1z7nFdM4fUk6T1Wk7NpnGNKS-tEdOzv09Swy0GdclncylkJMzHgG83Rfe4vRZ5kKKHkxgle-Q8MDcXVK5191Id0hnFkTdpfYafrorHYBtTD-d65I8KfSkxMGpvvVxV0cGkJTOk-IVoJrCM_qQ-c_u_Zw5-u4m67W0r1APqPv3sd3xIOkxUE7KJZjx4G3nI09ABzqXYd2NtpkegbGptUU9WGPaNG2ox60si29OOAYexZPFW4-FtAf6QnoK_Tre8V21C5WhQ1m1AGuALiBlJ-2qU3y040FAMwm3TpI4YmivqWQ-2HZHQ_jDhMsYJ8QvYMhe0BUuPQsjuNx1WJRSWQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 03:37:39</div>
<hr>

<div class="tg-post" id="msg-132623">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=BX0--y8GIbOrS51Y50tAPU0iRkO6CR_AYxbOAYy34pUKNTXAZi0WCIpWZZNTCgqlEpse_7p8ppt9LHFdxVqWxKLvXYUyOXQM1KRIcymwXFg9KDxc_DVY86cdd67QfZYfFOSMO9L8910kb_VgaQTVKPb2AXpUetIZyU-1D5RmIGiUG7XP8UC1VqxvMpyp6Pr0ZuC17R2aZzaMUUr-W5nvd_Y0DEJsDitrM9YzaHBXiXsJlmOKCRj-Mk9qEpGTffi_CI7dT7M0jVbS2F24CJhxh4CblFcyqxGK8RakLS8_MQIilXSNYAAcuWMtFm77Dhkj1rTAPrPO079E2Q7vwKu3Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=BX0--y8GIbOrS51Y50tAPU0iRkO6CR_AYxbOAYy34pUKNTXAZi0WCIpWZZNTCgqlEpse_7p8ppt9LHFdxVqWxKLvXYUyOXQM1KRIcymwXFg9KDxc_DVY86cdd67QfZYfFOSMO9L8910kb_VgaQTVKPb2AXpUetIZyU-1D5RmIGiUG7XP8UC1VqxvMpyp6Pr0ZuC17R2aZzaMUUr-W5nvd_Y0DEJsDitrM9YzaHBXiXsJlmOKCRj-Mk9qEpGTffi_CI7dT7M0jVbS2F24CJhxh4CblFcyqxGK8RakLS8_MQIilXSNYAAcuWMtFm77Dhkj1rTAPrPO079E2Q7vwKu3Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 751 · <a href="https://t.me/SorkhTimes/132623" target="_blank">📅 01:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132622">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت
بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/SorkhTimes/132622" target="_blank">📅 00:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132621">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔴
برنامه های تیم ملی تا شروع جام جهانی از زبان تاج
🔴
بخش دوم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/132621" target="_blank">📅 00:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132620">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">✅
فدراسیون فوتبال: در صورت تمایل امیرحسین محمودی رو جهت حفظ روحیه بر خودمون میبریم مکزیک
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.66K · <a href="https://t.me/SorkhTimes/132620" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132619">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a044344.mp4?token=baIdN7uDARGxSopbV4-xvKRM448siDxunmz_-9zGMFQ3jTZfTOzWYKk5IW-YL28OEHLgp_PV__RoYUn6CMebw_98HDR1uTMJxuCwFV8XFyBrZk376FY-Ci8z-7JUne5qCP3dw70b1rC2V27AmHtEFzPAlezgRbX6OEoD6GZJ_txJzLZSSpeoZiFfnETKf1edJH_yhK1LLYiyaB8FZw3eVxgWEmqsOy0cBqyVH_npjjL6SaLh4gTcTyCnd7hO3Is814EAVgss6osGURKBO3FMVIGUUqcLtTEmtJ2srJO1MdB_0xqfZBxr9U1ItXWUPp-Ln3i0IIPS_enCQcFqnmVJ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a044344.mp4?token=baIdN7uDARGxSopbV4-xvKRM448siDxunmz_-9zGMFQ3jTZfTOzWYKk5IW-YL28OEHLgp_PV__RoYUn6CMebw_98HDR1uTMJxuCwFV8XFyBrZk376FY-Ci8z-7JUne5qCP3dw70b1rC2V27AmHtEFzPAlezgRbX6OEoD6GZJ_txJzLZSSpeoZiFfnETKf1edJH_yhK1LLYiyaB8FZw3eVxgWEmqsOy0cBqyVH_npjjL6SaLh4gTcTyCnd7hO3Is814EAVgss6osGURKBO3FMVIGUUqcLtTEmtJ2srJO1MdB_0xqfZBxr9U1ItXWUPp-Ln3i0IIPS_enCQcFqnmVJ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/SorkhTimes/132619" target="_blank">📅 00:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132618">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=IAqJnbjtzq1Z-mr0QvP7HrhwyVMPdBI7EWZ5Pzq8F1lY-UOyvLEunT2cWitFNWkDdqXUjBLKSNv2gWFJUjkUtmPWVbxUZYImUbXRq1VLREimAQeUpUoNHLNv-phKkh0Jy83gafklUubJ0PtPKGslIjbxo9GuXMDgrHhoaxbk-NpyhsvMAHFbpvN5CabwXsZYqOlJgg_PhSlJyoqnUwJDDMSzk6GTyuhDwLImhA4PN2EyrXEjVaQxpkP7A36IC6KsZxYpIPCDDBp8rdnJtiMdyRSK9oZsJTKKd3xO6oNM9SjsCKKUJAishV0aMvTvWrL6ISjum1fH67kC_AABvfBFBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2531fbac09.mp4?token=IAqJnbjtzq1Z-mr0QvP7HrhwyVMPdBI7EWZ5Pzq8F1lY-UOyvLEunT2cWitFNWkDdqXUjBLKSNv2gWFJUjkUtmPWVbxUZYImUbXRq1VLREimAQeUpUoNHLNv-phKkh0Jy83gafklUubJ0PtPKGslIjbxo9GuXMDgrHhoaxbk-NpyhsvMAHFbpvN5CabwXsZYqOlJgg_PhSlJyoqnUwJDDMSzk6GTyuhDwLImhA4PN2EyrXEjVaQxpkP7A36IC6KsZxYpIPCDDBp8rdnJtiMdyRSK9oZsJTKKd3xO6oNM9SjsCKKUJAishV0aMvTvWrL6ISjum1fH67kC_AABvfBFBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
با اعلام تاج امیرحسین محمودی و مابقی خط خورده ها راهی جام جهانی میشن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/SorkhTimes/132618" target="_blank">📅 00:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132616">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=i6_yqIXY0yqPWtR2Kzf0tKCwb8TlA7Uh96z3GOiYqxDNpUkijBfxNcQae8r2IJh432raKT2niz4igeW3cfjKessDbsYl9VZbRTKF5JMo2lO_-oMLB86PACmRBn-66NqNwaS33P1n9Aj_FmMQ0x9HvmoXyDLJuAUXeAIBbENZhalMtRedAdQpQcCVAuzRKWxdVX4sCUyGllcN4uT-nsRfJIRw44MF7gqFVtcAbXlbFTRhBqBIdWAybGUtB60X6royZn9dho-1KRm656wG9Ay2jlxXCiJO5ep8KSY7te20hD22QzXNQW2uqlHKnR9y5rzOBmqyhp_dgRLekKkZ8Weyjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988a98ef48.mp4?token=i6_yqIXY0yqPWtR2Kzf0tKCwb8TlA7Uh96z3GOiYqxDNpUkijBfxNcQae8r2IJh432raKT2niz4igeW3cfjKessDbsYl9VZbRTKF5JMo2lO_-oMLB86PACmRBn-66NqNwaS33P1n9Aj_FmMQ0x9HvmoXyDLJuAUXeAIBbENZhalMtRedAdQpQcCVAuzRKWxdVX4sCUyGllcN4uT-nsRfJIRw44MF7gqFVtcAbXlbFTRhBqBIdWAybGUtB60X6royZn9dho-1KRm656wG9Ay2jlxXCiJO5ep8KSY7te20hD22QzXNQW2uqlHKnR9y5rzOBmqyhp_dgRLekKkZ8Weyjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.76K · <a href="https://t.me/SorkhTimes/132616" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SorkhTimes/132615" target="_blank">📅 00:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/132614" target="_blank">📅 00:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40e411950a.mp4?token=naYCNpqz1aE7oSBpgwDwjp9xafk8NLlB9xGedT8vEWJxUJonoQgdPPD7eNuFuMOkOn8ceWxDiurtM6CFVb1NphkuZiad3Z3Ysqa4Lxdd9NTi4cdrXe4IyzLNWjqQJn5zrea_lE989mUSk3KFX2L-Cgmi3adRGnFSOXgBRADJR9FthN-OHETNbksibsjuFmIm-RAgv6E1ojgu_vru1cetm-hFqjNc_AyrZfZSWNM_IU0N5synTRanxW6Ox2mZg7OaOIh-bcDvdG9QMXNmaeYk7WLWE-DvR0h7Zurb4_QAklOkt0mGu3KcckfyoNLG4TgJz5w-DdneVyJfVswwR1nHhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40e411950a.mp4?token=naYCNpqz1aE7oSBpgwDwjp9xafk8NLlB9xGedT8vEWJxUJonoQgdPPD7eNuFuMOkOn8ceWxDiurtM6CFVb1NphkuZiad3Z3Ysqa4Lxdd9NTi4cdrXe4IyzLNWjqQJn5zrea_lE989mUSk3KFX2L-Cgmi3adRGnFSOXgBRADJR9FthN-OHETNbksibsjuFmIm-RAgv6E1ojgu_vru1cetm-hFqjNc_AyrZfZSWNM_IU0N5synTRanxW6Ox2mZg7OaOIh-bcDvdG9QMXNmaeYk7WLWE-DvR0h7Zurb4_QAklOkt0mGu3KcckfyoNLG4TgJz5w-DdneVyJfVswwR1nHhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مسن‌ترین تیم‌های حاضر در جام‌جهانی؛ ایران در رتبه سوم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/SorkhTimes/132613" target="_blank">📅 23:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
حدادی مدیرعامل باشگاه پرسپولیس: سروش رفیعی همچنان بازیکن تیم پرسپولیس است و با شروع تمرینات باید در تمرین حضور داشته باشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/132612" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:   «مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم! — دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/SorkhTimes/132611" target="_blank">📅 23:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndXdwoA_VR_fCg_EFuCNByfSMa1-_i68FIjeyK8BFwQGfMjhrWb5TfMcWy8yB-oiDAu8Z0pOeC1c6FIl15XF_y6cPTYXpu8FqxCzHaOO3uumHeBx9rRngm5wH4x1hs0JJsZzke3TllcdKyY5HHg4LUX879H--ardpWDwhTwm0vxCB69y2SK_mE1kLri0rIcdM3BiSc4ESaELQvevdtXZBkyjEwLNJo5F2K3hvTGCCBegIJ0Cyzv8J1eDZz35RI9K_81WTQODkW9CfnZbi_RjjRwmRVeWHYmsSrCihpAiviQT_isqE_-TYXKTw9OzKih6QqO0vFzoK2JwO8s6tWc3NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟥
بانک شهر طی اطلاعیه‌ای از تاسیس نئوبانک جدیدش به نام (رد بانک) خبر داد که تمامی منافع این بانک متعلق به پرسپولیس خواهد بود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.84K · <a href="https://t.me/SorkhTimes/132610" target="_blank">📅 22:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6LElCC9wjknDCRssu24HjqkOuXJzOJfk_mgQK1vVjxMYdPH9becoyMtMK9TH5-Cw-qpgs4SoNxzYXsQCFJ12YdB1IafWjcXD4xhjUsTZyCO2KgirthpN7yxiFdV5ZVGUnxDdOE98rrYvAbLOLw8CHqEKbiza-om9dXGpbM2sYoi2kEqd5oYnbBhPG-A26-mTfGD1W7e_1YNJOXIKS7rnDNlmHFvqjxanmWrcagUVpuVBsshv6hkfUbYNsqnSym-wzCuVpRYU7LX-dD-ayJd02rlDans-sAslwaRXMdNsy_DwX4DaGMI4Abtom5TpbhO-K9BXe2jVovd91WJFoswZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«مذاکرات با جمهوری اسلامی ایران با سرعت زیادی داره ادامه پیدا می‌کنه. از توجه شما به این موضوع ممنونم!
— دونالد جی. ترامپ»
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/SorkhTimes/132609" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SorkhTimes/132608" target="_blank">📅 22:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132606">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">✅
هوشنگ نصیرزاده، وکیل بیرانوند در دادگاه CAS: چه قبل و چه بعد از جام جهانی هیچ چیزی بیرانوند را تهدید نمی‌کند. اغوایی توسط تراکتور انجام نشده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132606" target="_blank">📅 21:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132605">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن…</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SorkhTimes/132605" target="_blank">📅 21:10 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TQ2KMDhSyh4WRL9yAKCioA16r8LLI4V9SOgGWkRflG9OEEWw_YmQONEkDvqNMsI2E1SB35F_FZvIrcd2wY1_Ad5AOtcp-ZlC0191p-MQWYv7wKBv2xYOz3gzpW6EaPG51pcIK56K8A3meQnKGyQhJMuA5LUrHK0D-9SS-1jblmJpMHJfkHgQpW_VdITwxYsBY2-cwxA35h0lap5HJX_ZwSIZDLJ-YRPh7TMBdx3Y0Kki9_WNrBxl43o0sBUdpiN5wcv5POZdUBTBXm8tsTdRIVjByRKnZzLepYmajFrfAcGuQ0U1yU2Lm8RR5tMTvAMkI3APSo_VI3R4K-GNdtZhNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
ترامپ: من یک تماس بسیار سازنده با نخست‌وزیر بی‌بی نتانیاهو، از اسرائیل، داشتم و هیچ نیرویی به بیروت اعزام نخواهد شد، و هر نیرویی که در راه بود، قبلاً بازگردانده شده. همچنین، از طریق نمایندگان بلندپایه، تماس بسیار خوبی با حزب‌الله داشتم و آنها موافقت کردن که تمام تیراندازی‌ها متوقف بشه؛ اسرائیل به آنها حمله نخواهد کرد و آنها هم به اسرائیل حمله نخواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/132604" target="_blank">📅 21:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">❌
ایسنا: احتمال برکناری محسن خلیلی از پرسپولیس وجود دارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/132603" target="_blank">📅 21:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SorkhTimes/132602" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes ‌</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/SorkhTimes/132601" target="_blank">📅 21:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
از جدول ناتمام تا شهرهایی که آماده میزبانی در آسیا نیستند
‼️
چرا میزبانی این دوره از تیم‌ها در قاره کهن امسال برای فوتبال ایران مهم است؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/132600" target="_blank">📅 20:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8Ze23KPqN3TbbEldt210u0AwRpd15Z1N49l0bCbdHDcYJrF4_hTciUr4mzChTPtHZ_Jsz6dxCH-84MfS65RdaeMX2fKmje9sypBOwuDOT0jVeT3Gf23va_JqMf28BuBnbO7bFOQd6e-G8lncG16hhgQdx1EkqVPohN5YjiR7rFAp8-96YcvkV3AFJLQsG2G4tVSOiyAH7hF5uuEPZFmVD_ikDjYujUFgRjlEhhXmhC_ZJ1kO-BIBk5AjIqGVfrQ9iYVdtVXOFtq7vLItjxtC63J2kZ5_sXUZKGYIRrg9OEfUGbGztXYbjA6IOC_qQdKzVpQtAZtzr3m6vYQlxmh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SorkhTimes/132599" target="_blank">📅 20:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
محسن خلیلی: باشگاه پرسپولیس حق دارد از حق و حقوق خود به هر طریقی دفاع کند
◻️
متأسفانه در روزهای اخیر شاهد آن هستیم که برخی افراد از طریق مصاحبه‌های رسانه‌ای و به صورت غیررسمی درباره نمایندگان ایران در مسابقات آسیایی اظهارنظر می‌کنند. این درحالی است که طبق…</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SorkhTimes/132598" target="_blank">📅 20:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132596">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚩
ترامپ: فقط ۲ چیز از ایران میخوام، تنگه رو باز کنن و بمب اتم نسازن، بعد ما میریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SorkhTimes/132596" target="_blank">📅 20:34 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132595">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnvyNSQUl3Ay6S_qStVU9gM2kvRG73slYI3zNX0ImWGOf8vXJ7sbOahqMFgV2hFwWHJ3VTKWMTGm3oIaea8i3RZH66Ou4eeKiJkOoeZWMxIzLyrUM2TxvZRTb67qi4Qf3HHeEyVJRxjobr1eJSS7u2uveLKXEK4yX0NNj4pGfOflQB8Q-MJ29VuLqWQCN6OCv0DK0A3qDkl1yCyHltfiwcJynyLtdFhULNS7K5YnbIPfmDuQtNPORCG0ZkMlpkxaXC9dvKWgbN26QRgXG35BOw3-n9H46UGWYu9aHu_XYiYFuzR4jkcxCbZTm1cMmk4v_2jMszoanDEw01nCiIUpmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇪
آندرس اینیستا با قراردادی 2 ساله سرمربی گلف یونایتد امارات شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/SorkhTimes/132595" target="_blank">📅 19:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132594">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=utKI_tm0AblVrERMmJ2CAB2LYjt8H2PFdgt_qt8kNQ6OVVInBmc77n8mbl5F1lvEeFXh20AJjkzdF0DCNLDVCbR38OMdKvENxD9lcXTiy0pJHCejIm8EOg5W3qwTWTcBBZ7gnBuCzVOVX2hZxIWQaMfeYSa71Sv0Y7j75LWZvuxGbApIUPg3_DoTcJWOidKllN2dnBnRpUXe1IvbeTcBkrSAJ245DbjxlM2WNAhhU3Iy8A3tPy75kWrmbvqakiN8JivTlvOR47vuj6c5ZZZ-h6QhYayfBfnasjMxvlOjADBdX1G5OzkKE68u1twkjWj6SlsAiRRc_537xM_zQVyGUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32a1bce686.mp4?token=utKI_tm0AblVrERMmJ2CAB2LYjt8H2PFdgt_qt8kNQ6OVVInBmc77n8mbl5F1lvEeFXh20AJjkzdF0DCNLDVCbR38OMdKvENxD9lcXTiy0pJHCejIm8EOg5W3qwTWTcBBZ7gnBuCzVOVX2hZxIWQaMfeYSa71Sv0Y7j75LWZvuxGbApIUPg3_DoTcJWOidKllN2dnBnRpUXe1IvbeTcBkrSAJ245DbjxlM2WNAhhU3Iy8A3tPy75kWrmbvqakiN8JivTlvOR47vuj6c5ZZZ-h6QhYayfBfnasjMxvlOjADBdX1G5OzkKE68u1twkjWj6SlsAiRRc_537xM_zQVyGUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دو سال پیش
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.4K · <a href="https://t.me/SorkhTimes/132594" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132593">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132593" target="_blank">📅 18:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132592">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
مهدی لیموچی با ارسال درخواست رسمی به باشگاه سپاهان، خواهان فسخ قراردادش با این تیم شد.///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/SorkhTimes/132592" target="_blank">📅 18:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132591">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SorkhTimes/132591" target="_blank">📅 16:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132590">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
خلیفه، نورافکن، محمودی، حبیبی‌نژاد و طاهری خط خوردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/SorkhTimes/132590" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132588" target="_blank">📅 16:42 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/SorkhTimes/132587" target="_blank">📅 15:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132586" target="_blank">📅 15:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siyFw70xJIZjGSjmTLo3R3YDws6mHSsP6lTjw7Z5VObNo1Mx0p6YEXND9_hIwgdvYSwpJ8zp5AMoVhwSe0aoCOjBb8UqnhYOUIGEQO07pQLny49USftAWD8UNg7SHMvlX8TxFCVRw9toIEkapkiowecjv9UdllctDeIY6GaFSOJjhFzZHeY6GeofRI7rlhzv9Fw12dHIG1fbdGo36bNT77q623vAABSGWguIZQyXt6TI98GRY5bEUOGdZpIZsx53v6qSRFybLaobBhwrviUE2PKHSTdWVaJ4jxoSkqoHAnrE2tTZfS7JCNslENmjba9dN1JGgti5CAhfQuo-Mri7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
لیست تیم ملی در جام جهانی 2026 مشخص شد؛ محمودی خط خورد!
◽️
نمایندگان پرسپولیس در تیم ملی: نیازمند، محمدی، کنعانی و علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SorkhTimes/132585" target="_blank">📅 15:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOkpeuJv84Hu3ae3qDLuqjZ9MKkTa6ZpFfQWPO4Iq7_0lisXkqqQY8qeB1RVTyAGzuh2A47ybFJfmZ9LOYatJmZwYg-tB2galagCFkCJmnhyqP4AoYMlmXW0M_1UcoHMkte1TfG6OplFVHnzfaXa9Vk8R6MyWcgbvrKhwQA8CyzDyQt4XX2bvp7xm5I_2GjyFd3weRrCRH8Uacnl6oh4LxAgxgHJDUrC4WynJkn7VO4TATys234XRyF9RCPgq5vCcZS0WOIsOAXCOz8prpeeyvzPFaY405BIVoYEaMy4iZRHS5OWMtFWNGafS5NFHjgHdB4ppzCeUuHri6caFaApZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مراسم معارفه مصطفی میر ابوالحسنی به عنوان مدیر جدید حراست باشگاه پرسپولیس با حضور پیمان حدادی، برگزار شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/SorkhTimes/132584" target="_blank">📅 14:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPdFmF23ulezpbOO9XPgaPJm02OupdKgtMBfyWtKhJxruozZV2jjVdPc_bOAZE7VgBP7qsnSiJ0mzJyeVa9hEjZtFBDLM4XUOifTngDmmyOteH6kkur-MtTB-63ud8RTFyMxhmBf54cLQajrPSacV1NilGcOsjdJxWWOq5NhqKFKlT56aQCgQ9hBGUuI-OBaB1E6glPi5YaxLCjMLJ-3AQwX353as8v3KU5PUxSk3Gz-ucfhOMtHOheAmrbcwBVhvdUFISC69wxjBvi258PtBfq5CcldV-7WK9Emg_riA5cUoadtL46e4Ob5FgjvfF5atyExseZiI7gOwCwZjyjMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/132583" target="_blank">📅 14:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/SorkhTimes/132582" target="_blank">📅 14:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: افشین پیروانی قرار بود به یک کشور دیگر برود نه آمریکا/ او برای رفتن به سفر از من اجازه نگرفت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132581" target="_blank">📅 14:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
فووووووووری
🚨
شانس پرسپولیس برای آسیایی شدن زیاد شده و ممکنه با تبصره ماده پرسپولیس راهی آسیا بشه/فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.65K · <a href="https://t.me/SorkhTimes/132580" target="_blank">📅 14:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAPUd_o7JnjE-66lf41VR-BlrmHjDXf0D9yZIiiej_NX9gGyJXN9SEo56NFbS1l7u9VDvoWab1GEOwwxnyAEeDb_GwJgpW7b4HuK-40UxrD08sCnE3qjUkiKPVFg1_1nM9IOdZbkIAAaXKAJCxS75uXyA2jkoSkLeyckjIVW_WE17vbGq6UMoqN40Hc7p9yooDwettUwFAsR-4xdcW_XM10KrK9diuXqX3nsLZoTQfoUJEOxMWPu-qbzFdiD3J2FWgN_dCPd2lVWc5iz6n-_JabftfSfsE1ixW0Iu7vapT1ToXdxFoGHY4kicjPxGqG1RSVB01hWKeTNYTHpu_-GDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💭
تقویم مسابقات جام جهانی ۲۰۲۶ در ماه ژوئن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SorkhTimes/132578" target="_blank">📅 13:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132576">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NY8y5myia-llZFePlrUDZ0B0xbRf9ROCWGIimXGi4_J2zmfko9Mmf5d0wqPSjtSuYyALJ7ErD38BbW4wtfpgSi2kSr8mU5W0Tv5pFjVNdtTR8WARQEp12JfNne6ua-j8P7QXbep6GUXDu_HlACFnjSxhp7LdU6alAcUs7uleUKMRjgVMbHXibw0KHbbkqMOKFq2bfAW4hEJImcOyR7XEiCJhwGJKHl9M7y28ZrQglE7ZXstJ9pv1M4xwFLqmIAVSYAgFvhJgB34AT7_99iG2zamz1F03bibieEajorvFjICEjpudV9Uy1X8AT95PKUEnbPGocgZe7TR6hqh9LT5Etw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سه سال پیش توی همچین روزهایی؛ پرسپولیس قهرمان لیگ برتر شده بود
💔
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132576" target="_blank">📅 12:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132575">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yh_ov4jX40i7JMdeATHXxi0nc1TKhAeV8zbBTGbkQ7XeB1Vdi-MS8B2mCQtCVKymlR8M-yOLoswTB1r1tiF8jjxcJnkKfJSa5F5DVivXtOARtJF5p2DF0-sI4FVoghFpW9hsm5IDu1JiuOal9b9XIlItWvFI48YNwrlik0DbqBtJrq6KJCmPTkp_9U6UxZJmfX0mDG9xnWEg2rKct-TYonwajQtvKd-VmUxfenZi5tMdG3fs81P2JxdA5tkOrlmSXrTmY7HDhpUjYa2hie8yoRGVu52kQOzykR9JROAvNTAnE4gjJ9jiAWPJn3liCodxzONIhjAruroz1lT8zUt86w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇷
❌
۲ پرسپولیسی در آستانه خط خوردن از تیم ملی
⏺
شنیده می‌شود حضور پیام نیازمند، محمد حسین کنعانی‌زادگان و میلاد محمدی در لیست نهایی تیم ملی برای حضور در جام جهانی قطعی شده اما این احتمال وجود دارد که از بین علی علیپور یا امیرحسین محمودی یک یا دو نفر از لیست نهایی تیم ملی خط بخورند.
✍
خبرگزاری فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132575" target="_blank">📅 11:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132574">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwhKVBxWjMev00foFMVNZCCtViWDIz6wLQ6z_yht7qgeXvbq1vl_4DfhPA4L1EfM4d0w52Mnemt0dB5-Kwt3y0dPHwbY2uSEQzG5lXPRy5-1FyvUvvF3n_7s0NIX7bN1TrzhbHx5OriSXWLQOUHHS4eRrssKjpavyhUU_qGif_RHvh82Tm0Duqc9P6dMB9P1OiIWdvQ0fKRfYMOd2UX6xGKPxDbqQpHDEAqcqwGbXDH5XGK0PTrqsRlhh25Bri4Ek8q7mj92gzLBfLExjPPF01ROzJtTGYiDi84Ivwc3dbbntM6-7_BeMmIlw6dA-qiYzIt2LLcPxzWvpytaUedxxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست خرید اوسمار به نقل از فوتبالی:
🔴
اوسمار برای هر پست ۳ تا گزینه معرفی کرده و حتی اولویت‌بندی هم کرده
✅
دفاع راست
✅
دفاع میانی
✅
هافبک
✅
دفاع چپ
✅
مهاجم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
‌</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132574" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132573">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
ایرنا: مدیران باشگاه تراکتور با مرتضی پورعلی‌گنجی، مدافع پرسپولیس، برای انتقال تماس گرفته‌اند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132573" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132572">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/SorkhTimes/132572" target="_blank">📅 09:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132571">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjdphfJHpO-m4jdxWc8c8kPAoCV2S1yoGGwLvFDwVsxiNU9jVLyAxKYB6AdoIhEWVsBLRcAzwglr3095_xTLoWV3PLzrS2igIid5XDmfrvua_O0JataARaVhkdYiKQXrA2Jv0jmZp4p7CvgrwhHj4fm-9LMRTQznUJjZx7M1wJ2oJemF7xcapPXiuwW9kpi0EIZV7nCJjwXOriD011tJNbpITZxw8Q31y1HOcOr679N18V7wwoGOQVkXTz33ENC7BL03o6j9Hika7eCGLHuUiu-u0Gnfdmh3qLILA5kmM8fhNsqvWPGWLutBnSBTdGzdSIZtwhTtBfzrXs7lTrukWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
‼️
هواداران پرسپولیس حواسشان باشد؛
🔺
برخی ایجنت‌های نزدیک به اوسمار در هفته‌های اخیر فعالیت رسانه‌ای خود را افزایش داده‌اند و گفته می‌شود با استفاده از بعضی کانال‌های تلگرامی در تلاش هستند فضای باشگاه را تحت تأثیر قرار دهند و زمینه را برای جذب بازیکنان مدنظر خود فراهم کنند.
🔺
بر اساس برخی شنیده‌ها، این جریان رسانه‌ای از همین حالا کلید خورده و هدف آن ایجاد فشار روی مدیریت باشگاه در آستانه تصمیمات مهم نقل‌وانتقالاتی است. به همین دلیل احتمال می‌رود در روزها و هفته‌های آینده شاهد افزایش شایعات، اخبار جهت‌دار و حاشیه‌سازی‌های مختلف پیرامون پرسپولیس باشیم.
🔺
هواداران باید با دقت بیشتری اخبار نقل‌وانتقالات را دنبال کنند و هر خبر یا شایعه‌ای را بدون بررسی منبع و اعتبار آن نپذیرند؛ چرا که در چنین مقاطعی معمولاً منافع برخی واسطه‌ها و ایجنت‌ها با منافع باشگاه و هواداران همسو نیست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132571" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132570">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
🚨
سپاه پاسداران انقلاب اسلامی دقایقی پیش به کویت حمله موشکی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SorkhTimes/132570" target="_blank">📅 09:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132569">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
به تیم ملی جمهوری اسلامی واسه جام جهانی قراره ویزای ساعتی بدن یعنی واسه هر بازی چند ساعت ویزا میدن بیان بازی کنن بعد سریع باید برگردن مکزیک تازه این ویزا فقط برای بازیکنان و کادر فنی صادر میشه نه افراد دیگه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132569" target="_blank">📅 09:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132568">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qc6twq0ci9SWbTE_OAUTW9jmiRg8f4gAkIm9d1F_rqd3ligiQAnT3XmJa0nZPRYXm4hFN5AhtaxFFGNzrmPIc-jHQ6z0oeP4b-cWsnbDtzPi4yyJqArBPnbpBUrcCMjG_J-oZAbR7rOHScc8tyfcakFCVVLeQsT596NuTq-XVvuXL3nWrH6cOoS_EjNmcov4bEFGEAC25eLvVJh-hxwZolbhpbcwijFFSaTuX-g55Z0_-Ni-Qp3Di159zhVCTbyL1rA8f2F7tLdVZw88KgjFvtmuvKBo3AKg2REQMWvo9iRGqwQ-v6RlJB1vfEW8TN6wjkr0BO5Kxxsgg-7-aJMnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
مسابقات گرنداسلم رولان‌گاروس رو با بالاترین ضرایب در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132568" target="_blank">📅 01:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132567">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">❗️
بین‌گلگهر و پرسپولیس؛ احتمال زیاد پرسپولیس راهی لیگ دو آسیا خواهد شد. اگه اتفاق خاصی رخ ندهد! گل گهر رضایت نسبی خود را اعلام کرده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132567" target="_blank">📅 01:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132566">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QYkOTbkL84s2LAaOt8Y-iruxQwcjlJSAwyGEUTUm7l8XOg4sGwzkmkIFQuJOaWIzl4RGqcZ9In-wtejmUQQk28u7qkSK7KSY5bQSo5S2zFwTw_1otpYbM110PtSXNWeUuYAj2_CkxMCMkujGOuSfNILp6nFiBi1waPdod1NkWxTeQTC9L5kS4x4NYjlN1XxqujKEzP0hAZoGay68SjyyvvxrvR8arRIkv_IaTQd7cyybRd4fZWGLDGJxRlQtRk2JrhEC_t26liTweDDxIg5T3ItUnpl-JkVzf19ITM8ZZ2NG5A-h8u5VgCi1jIfEMSyG0D-l8rOaP7dpa1XuaS_vcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
یه سایت هوش مصنوعی اومده تیم های صعود کننده به مرحله بعدی جام جهانی رو معرفی کرده که تو اینا ایران تو گروه خودش دوم میشه و بالاتر از مصر به دور حذفی صعود می‌کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/132566" target="_blank">📅 01:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132565">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⛔️
پلیس مکزیک گفته بازیکن های تیم ملی بعداز ساعت ۸ شب بیرون نرن چون ممکنه لولو بخورتشون..
😂
🤧
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SorkhTimes/132565" target="_blank">📅 00:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132564">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">⚪️
مهدی تاج:
فدراسیون فوتبال دارد تلاش میکند که سپاهان از آسیا کنار نرود و اگر سپاهان نتواند پنجره‌اش را باز کند طبق روال جدول لیگ نماینده ایران به آسیا معرفی میشود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SorkhTimes/132564" target="_blank">📅 00:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132561">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">✅
شنیده ها :مدیران باشگاه پرسپولیس با مدیران‌دوتیم چادرملو اردکان و گل گهر سیرجان تماس‌ گرفته‌اند تا رضایت این دو باشگاه رو برای رفتن سرخپوشان به آسیا بدست بیاورند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SorkhTimes/132561" target="_blank">📅 23:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">❗️
لیست مازاد فعلی پرسپولیس به ادعای تسنیم:
🚨
سروش، پورعلی‌گنجی، سرلک، بیفوما و گرا
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/132560" target="_blank">📅 22:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SorkhTimes/132559" target="_blank">📅 22:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‼️
امید فهمی مهاجم جوان سابق پرسپولیس به پیکان پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/132558" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🔴
خبرگزاری فوتبالی: استقلال داره لابی میکنه که قهرمان لیگ اعلام شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/132557" target="_blank">📅 21:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132556" target="_blank">📅 21:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132554">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
اگه تمام نماینده های پرسپولیس در لیست تیم ملی برای جام جهانی باشند چقدر پول گیر پرسپولیس میاد
⁉️
🔴
نماینده های پرسپولیس : اورونوف - سرگیف - نیازمند - کنعانی - ابرقویی - محمدی - علیپور - محمودی
🔴
یکسری از رسانه میگن که الکسی گندوز هم اگه بره جام جهانی پاداش…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SorkhTimes/132554" target="_blank">📅 20:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132553">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
ادعای نیمکت نیوز : مهدی لیموچی امروز درخواست فسخ با سپاهان رو داد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/132553" target="_blank">📅 20:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132552">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132552" target="_blank">📅 20:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132551">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uxk_VB5sB_fYdRcNKQ66R1mtu5uIuIRJ6Xi4oApjDMN3evuynUbXUctMFEJaclrtzXLndM7bsmWW638Zq1ZOnoT9z1UkLQiyAFCKA_r318LfmPOYehPMliIV26MTGLV8eY5wbZ35UC2Zz7Ar_KdDBaZ9dCB6pK9ZkT8wzuuxYoyIsCH-5nUpxRp8QnX6_0Y-9NUZCXaTDrWQ33z2kuzTVJnscjrP7NoOI6NGqgPqgtq9UYPZpjshga5k0ZyNReOQbjmKJ7mXiYf3JEAeDznl9PO4_tnouJ15ioFyBRb5rskqxgLReDv0WVQT5RCXfV690IIVg5n5WDB_6n0hPdpKmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
خب سپاهان که مجوز نگرفت. گل‌گهر هم بازی اضافی‌ش حذف میشه و چادرملو هم فاکتورهای لازم برای مجوز AFC رو نداره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132551" target="_blank">📅 20:50 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132550">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2Qm9fkmfBL7Ln1B1a6UxkAfH4HEor2lcUPZkr-B-1zzIgTMSdrNCnGMEnQphE7xXasbc_2yWBmXh6gBephll7il_QHXFiiXdDFFLh1PBCFDYAiJbIlmXEm8tC0oT5Agr9zQ9--pClzb6N1Q4-RDdAqGKgjZzXATdWwmUutqEkrrfsn53DNK46oFrHyroKODXTIG_VMifSr6kJrHrILtjPzM6CNxw08DGtCzFHz4k4GjuYZTAgn493tNcfAlIMRvDId3i5QUoDtWkousILhuk7uK_llX1yC2aD4YcPskOemiS2xmUb9vE_gD_pmwtFusBrEbn1XWZmlbMdkdMhviGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توییت پزشکیان بعد از خبر اعلام استعفای آن توسط اینترنشنال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132550" target="_blank">📅 20:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132549">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🟡
سپاهان حذف شد
▫️
گل‌گهر یک بازی اضافه داره
🔸
چادرملو از بازیکن غیرمجاز استفاده کرده
🔴
پرسپولیس برای ۳ امتیاز بازی با ملوان شکایت کرده
⁉️
باید دیگه چه تصمیمی گرفته میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132549" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">✅
طبق جدول لیگ برتر؛ گل‌گهر با یک بازی بیشتر ۳۶ امتیاز دارد و رده چهارم است. چادرملو و پرسپولیس هر کدام ۲۲ بازی انجام داده‌اند و ۳۵ و ۳۴ امتیاز گرفته‌اند. در صورت معرفی گل‌گهر، قطعا هر دو باشگاه اعتراض خواهند کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132548" target="_blank">📅 20:44 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcwO6MwR6xioOZXOETEM05_jCAUSzp8BZe1YfzXgAANG6VtVHS5cwkcP4FHYeuYiBsw04mWGcBhuY959VmnyBNVQrCglPQpqoRqKEWVnrM-Qek8g-4hk-tuMPvN1S6bsknAyzzstaY0J_fPmj5NtOgKisD_b0X0pr_dHNMQgg0FSjn86ZzUici2CgYTdv0QgdWNJAuy778yQULh42yxl92LQEMmQZSP2w2E8D0KnlSMCtiCZEXvEZ6atleHbm-Ac7bLB64MyWOolDtdouE7hq7Z7fEwyYlikh7vqvrcQ04VtWjYuBwz2Iy6OER8HnI2r78Xj-XRVBvrlxFc82XsLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/SorkhTimes/132547" target="_blank">📅 20:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔴
خروجی های پرسپولیس تا به این لحظه :
🔺
سروش رفیعی
🔺
میلاد محمدی
🔺
مرتضی پورعلی گنجی
🔺
دنیل گرا
🔺
تیوی بیفوما
🔺
امید عالیشاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/132546" target="_blank">📅 19:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
گل گهر، چادرملو و پرسپولیس به ترتیب به علت حضور در رتبه های چهارم، پنجم و ششم در صورت کسی مجوز حرفه‌ای جایگزین سپاهان در لیگ قهرمانان آسیا سطح دو خواهند شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132544" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132543">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف…</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/SorkhTimes/132543" target="_blank">📅 19:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132542">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف شود.
◻️
به این ترتیب حالا  یکی از تیم های گل گهر، چادرملو و  پرسپولیس طبق مدارکی که به ای افرسی ارسال کردند شانس حضور به جای سپاهان را دارند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/SorkhTimes/132542" target="_blank">📅 18:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpLTtLFUvrckJlmCet78irwP921QGkdZSZH0c-CqTnpi2kzzcUSUq7VPWE5KasMv98JI7zwHNQqmHEkC7pYJq7xfWqAx72tKUyT4WhdSel6RGJg0gzhisR9dIVkBWeVT5kcFI0F4SPuV-yD3rcpb1OpT1rTUr9LsD9b1lR2LAzK4HnH0jDQF8frWV7FunF0Ea4sPf0NLDSyrqKq9RW8FzFvbXrfCD0u_6VzHJgD0TNKWIHEpsEJ-OHplr8B0uMf7oUSTK-6P3tm3amEGY9GopJTNK4EKfD_H4vZ9zn0YU-yNwF755jUFRweqK7kZsURKviXos0qNqS6gcAuDhSK-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سهیل صحرایی، مدافع جوان و آینده دار پرسپولیس، دیروز ۲۳ ساله شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132541" target="_blank">📅 18:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132539">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
خبرگزاری تسنیم:
◻️
باشگاه پرسپولیس به دنبال جذب چند بازیکن جوان و ملی است تا میانگین سنی این تیم را برای فصل آینده به طور چشم‌گیری کاهش دهد.
◻️
بازیکنانی مانند سروش رفیعی، مرتضی پورعلی‌گنجی، میلاد سرلک، تیوی بیفوما و دنیل گرا از جمله بازیکنانی هستند که به احتمال زیاد فصل آینده در جمع سرخپوشان حضور نخواهند داشت.
◻️
مدیریت پرسپولیس از طریق چند واسطه پیام‌هایی را نیز به چند بازیکن جوان و لژیونر ارسال کرده تا شرایط آن‌ها را برای جذب بررسی کند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SorkhTimes/132539" target="_blank">📅 17:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132538">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">❗️
🗣
حمید درخشان:
🔺
در حق پرسپولیس اجحاف شد؛ در ۸ بازی باقی مانده هر اتفاقی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/SorkhTimes/132538" target="_blank">📅 17:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132537">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5B5COTfuhgiNQD7NZy30i3HzHhuQYRZ28Myl6jXRtD59dqKJXZA7nGicyziO5mOWougc7e8d7w4IDuCm3fLR6p3svzXUC5V3BLZFVFtisauM8uoB9p3ds8JChZNmYzYWECDegA4Z0M6PrLsU71XacEtfhX2rxbZeeGVExkVcrKXtYWD2T0us4WZaelJXHJ57sUmesed7xZ8nXSqcYkMEjVd12EKgL6Cr5Xx-OEDN1rY2jnMiXJI00hUZuqoXxwLPHKD7FiTfi-1a4oFa98Ad-GhbZQYz1A8nJLSlUlQGj5hwp2VoZWOure7XNLNcuLAHkTn66ldL-pdRNLRc8DmnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
قول بزرگ وکیل علیرضا بیرانوند به تاجرنیا رئیس هیات مدیره باشگاه استقلال: پنجره باشگاه‌ تون باز شود بیرو بعد از جام‌جهانی با تیم استقلال سه ساله خواهد بست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132537" target="_blank">📅 17:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132536">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">❌
خوردبین: تیمی که در ایران مجوز نگرفته چرا به آسیا معرفی می شود؟
🔻
آرزو به دل ماندیم متولیان فوتبال یک بار تصمیمی درست بگیرند. آقایان بگویند این تصمیم را با چه معیاری گرفتند. یک مثال بزنند در کجای دنیا با لیگی که ۹ هفته از آن مانده تیمی را برای حضور در سطح…</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/SorkhTimes/132536" target="_blank">📅 16:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132535">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">✅
ترامپ: بهتر بود اصلاً وارد ماجرای ایران نمی شدیم!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.77K · <a href="https://t.me/SorkhTimes/132535" target="_blank">📅 16:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132534">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔴
فوری؛ با اعلام دبیر سازمان لیگ، ادامه مسابقات لیگ برتر برگزار نخواهد شد و نمایندگان آسیایی ایران بر اساس جدول فعلی تعیین می‌شوند. به این ترتیب پرسپولیس سهمیه آسیایی نخواهد گرفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132534" target="_blank">📅 16:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132533">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GNJjNVsfJl_2vXyLj0qxPpS7S9G9NmGy9yBiq3sTIyX3RsnIP-wyOBd5HLM8RQyYKzhvYyGYUShua2L95kxnXYchyW0ACe0hrTlYSiAuQtAM25KdqZ0dDumax9eq1Lizeq8GpNzIY30bvWRA5ysXfi2p5z_Kl5kv9gWEn9IZXJPTUZ_oOJUV9oEkPtVLApLgiL2ZyXhUFgo0bMZwZulFOsyakJ8aJkH-Vs6GNcSJ6bUw1BXb4IOeWfYPuJ08xlYuW_QOPPVBOqk75ujVYpbu6pTnd7T55u17FeBu1DrwQdIJEa0nNeLJc4HpJ5oT_ccMxptPGmn4eNP3G-K1mVjQEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
مایل به تمایل…!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/SorkhTimes/132533" target="_blank">📅 16:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132531">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CL77qP0j2Oy3abMMZJ9E2Lr3HiVpeiiTamYWQMJ3GOT_2YKP-ue6DW9sMS0oBgl11KK5MLvEt5hgDNgipWErKlya9vnF8bk3FUrd-u_s_NTOa-79DpDC1cV7dt5BUoAQVDDPSucdJePW2YOvoJGY56_SUuUC4hVglYUeb3ykBBY9GRp9ry4_W6luJcu39IVnJfOtzUqPTG8urn_Exrpd6jSQa_HVnW4iY_PCl-3_tmdMNOKJwLhLhxEihPN8xPOeVT2S5LZmQvbFiw2VfNjrX4wZqyhfDDQkBJCitabOgRU5ipXJI_192zJC2ULHQ2Od1CftbO-Iog4aPniB9n2eSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دسترسی دیتاسنتر همراه اول به اینترنت برقرار شد
🔴
اولین نشانه بازگشت اینترنت به دیتاسنتر ها  باید منتظر باشیم و وضعیت بقیه دیتاسنتر ها رو هم ببینیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/SorkhTimes/132531" target="_blank">📅 15:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132530">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
اوسمار به باشگاه پرسپولیس گفته واسه فصل بعد بازیکن خارجی می‌خواد و از باشگاه خواسته اگه جذب خارجی ممکن نیست، زودتر بهش بگن تا گزینه لژیونر معرفی کنه
👀
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SorkhTimes/132530" target="_blank">📅 15:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132529">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=SeXY4KScMq5vHOrSTd4RiYT2fm5R4Ge8_FXFuQZoROt53CNNilq4lhUROIIV0ZWfgaguIi857GaFcWSEGCdON_8z1fFwG5X2JFXc1nADASFvryDLB36zIYUqxiYZGsPEH8PF_f9_ap_bozE1XiCWuq0LapKl8UfJDi5j-pE9RUqGWH6giPjwi5WJ9R_Udr54pTxRkjFqEFxJqwU2CEUEla03KeYQzgSaIqjhGHnzIvht6XVFw4xL_1Gzjsb0mC5IXdF6uanEkbq_qtJBCxpb48p-4tCH8IDPuVcJD-aThChHUZenaGL24PC16ha9pVmQC_5jSOcZX0Lgdch8rQKXhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=SeXY4KScMq5vHOrSTd4RiYT2fm5R4Ge8_FXFuQZoROt53CNNilq4lhUROIIV0ZWfgaguIi857GaFcWSEGCdON_8z1fFwG5X2JFXc1nADASFvryDLB36zIYUqxiYZGsPEH8PF_f9_ap_bozE1XiCWuq0LapKl8UfJDi5j-pE9RUqGWH6giPjwi5WJ9R_Udr54pTxRkjFqEFxJqwU2CEUEla03KeYQzgSaIqjhGHnzIvht6XVFw4xL_1Gzjsb0mC5IXdF6uanEkbq_qtJBCxpb48p-4tCH8IDPuVcJD-aThChHUZenaGL24PC16ha9pVmQC_5jSOcZX0Lgdch8rQKXhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎ اگه این روزا سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132529" target="_blank">📅 14:39 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132528">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
مدیرعامل آروان کلاد: از نظر فنی همینطوری که میشه توی یه لحظه اینترنت رو قطع کرد؛ همینطوری میشه تو یه لحظه هم وصلش کرد. زمانبر بودن بهبود وضعیت اینترنت از نظر فنی فقط بهانه ست. وضعیت اینترنت در حال حاضر بسیار ناپایدار و ضعیفه و اصلا به شرایط قبل از جنگ برنگشته.…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132528" target="_blank">📅 13:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132527">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
قـلعـه نـویی امروز لیست اسامی ۵ نفری که قراره خط بخورن رو میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/132527" target="_blank">📅 12:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132526">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❗️
امیر قلعه‌نویی:
👍
دو سه شبه که از بس به فکر چیدن لیست تیم ملی هستم، نخوابیدم. راستش رو بخواهید، هر چه تا امروز خواستم نشده، ولی خداروشکر. من به این تیم ملی امیدوارم، هرچند مشکلاتمان خیلی خیلی زیاد است.
👍
این روزها برای انتخاب نفرات واقعاً روزهای سختی است.…</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/SorkhTimes/132526" target="_blank">📅 12:55 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132525">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس شایعات منتشر شده در صفحات مجازی صحت ندارد و مارکو باکیچ فصل آینده در پرسپولیس توپ خواهد زد؛ و بند مشروط قرارداد باکیچ فعال شده است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/SorkhTimes/132525" target="_blank">📅 12:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132520">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❌
ترامپ: ایران باید قبول کنه هیچ‌وقت سلاح هسته‌ای نخواهد داشت
🔴
تنگه هرمز باید فوری باز بشه و عبور کشتی‌ها بدون هیچ محدودیتی انجام بشه. هر نوع مین دریایی هم باید کامل جمع‌آوری یا نابود بشه
🔴
کشتی‌هایی که به خاطر محاصره متوقف شدن می‌تونن برگردن به مسیرشون و…</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SorkhTimes/132520" target="_blank">📅 10:52 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132519">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
سپاهان به بازیکناش اعلام کرده فصل آینده با کمبود بودجه روبه‌روئه و احتمال فروش چند ستاره این تیم بالاست؛
🔴
پرسپولیس و استقلال هم می‌خوان از این فرصت استفاده کنن و برای جذب بازیکنای کلیدی سپاهان وارد عمل بشن...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/132519" target="_blank">📅 10:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132518">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✅
زمزمه هایی شنیده می‌شود که امیر قلعه‌نویی پس از جام جهانی از تیم ملی جدا خواهد شد و یحیی گل‌محمدی گزینه اصلی جانشینی او است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/132518" target="_blank">📅 10:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132516">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">✅
سهراب بختیاری‌زاده از وقتی فهمیده استقلال بدنبال سرمربی جدیده شاکی شده و میخواد استعفا بده !
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132516" target="_blank">📅 10:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132515">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
عضو هیئت رئیسه فدراسیون فوتبال: تصمیم فدراسیون بر ادامه لیگ است/ منتظر رای استیناف درباره سپاهان هستیم
◻️
رحمان سالاری عضو هیات رئیسه فدراسیون فوتبال، در خصوص تصمیم اعلام شده توسط سازمان لیگ:
◻️
اینکه لیگ تمام شده اشتباه محض است.
فدراسیون فوتبال به دنبال این است که لیگ را ادامه دهد حتی اگر لیگ هم تمام شود ما قطعا قهرمان را اعلام نمی‌کنیم.
◻️
براساس مصوبه سازمان لیگ و با موافقت فدراسیون فوتبال
ما ۶ تیم اول را به آسیا معرفی می‌کنیم و براساس دریافت مجوز بهترین تصمیم را می‌گیریم
اما با این حال اگر تیمی موفق به دریافت این مجوز نشود، تیم بعدی جدول که شرایط لازم برای حضور در آسیا را داشته باشد، می‌تواند جایگزین شود.
◻️
ما به دنبال این هستیم که بهترین تصمیمات را بگیریم که حق تیمی ضایع نشود.
در خصوص تیم سپاهان منتظر نتیجه کمیته استیناف هستیم و بعد از نتیجه این کمیته باید منتظر نتیجه AFC بمانیم که ببینم این موضوع قرار است چطور پیش برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/SorkhTimes/132515" target="_blank">📅 10:14 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132513">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q_MfjphfRjOsCv_w7nZCEiafN_b3CEd0-kV5sK7I1HFCv51uIVrUu2oHMMAtjK4fJldglap2zzYSomPpkrm7quwE3EdZNLTvFfY0pIDzQp6tQyIALDVxMmt4Kg6Krug2V8ywXSF_ZvAPg3aVnNxqznC7xofkewQKfM_pS_qHbA0gkmsnKwLBAgZ3QTYqYY1FHRTirPoROvgIyy5J7v3CQ4iSsF9C_etHpmYg8tPbyHevXRL9C8xneZ4QjwmQVaUAmdKlt5TfapxbXji2qs404L5YVwxoQt_t_H4x1uajj--_ffaCj9JN9gQ6vHzdeNoe4gI9u6E4kO_-4NDTLmYulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⛔️
ورزش سه: حرکت غیر ورزشی تاج
‼️
🔴
در جلسه کمیته استیناف برای بررسی مجوز حرفه ای باشگاه سپاهان، اعضا دو بار (صبح و بعدازظهر) به این نتیجه رسیدن که اعتراض این باشگاه رد شده و مجوز حرفه ای صادر نمیشه
◻️
اما مهدی تاج، رئیس فدراسیون فوتبال، با اصرار و فشار شخصی خواستار صدور مجوز شده
دلیل اصرار تاج، قول دریافت 250 میلیارد تومانی از کارخانه فولاد مبارکه اصفهان برای تیم ملی هست در نهایت، کمیته استیناف همچنان مخالفه و پرونده معلق مونده
👀
‼️
🔥
رئیس کمیته صدور مجوز تهدید به استعفا کرده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132513" target="_blank">📅 09:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132512">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🔴
قهرمانی دراماتیک پرسپولیس تو فصل ۸۱-۸۰ رو ببینید
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/SorkhTimes/132512" target="_blank">📅 09:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132511">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس هنوز باشگاه وارد نقل و انتقالات نشده و منتظر اوسمار هستند!
♦️
لیموچی و هر اسمی که به گوشتون خورده در حال حاضر هیچکدوم شون صحت ندارن و تا این لحظه باشگاه هیچ مذاکره ای با گزینه…</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SorkhTimes/132511" target="_blank">📅 09:30 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132510">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
محسن خلیلی: باشگاه پرسپولیس حق دارد از حق و حقوق خود به هر طریقی دفاع کند
◻️
متأسفانه در روزهای اخیر شاهد آن هستیم که برخی افراد از طریق مصاحبه‌های رسانه‌ای و به صورت غیررسمی درباره نمایندگان ایران در مسابقات آسیایی اظهارنظر می‌کنند. این درحالی است که طبق بخشنامه AFC، فدراسیون فوتبال ایران برای معرفی نماینده های ایران به آسیا تا روز 9 تیر فرصت دارد و باشگاه پرسپولیس حق قانونی خود می داند که فدراسیون تا آن زمان برای انتخاب و معرفی نماینده های ایران صبر کند. چنین رویه‌ای و اقدامات این چنینی به هیچ وجه حرفه‌ای نیست و می‌تواند باعث ایجاد ابهام و سوءبرداشت در افکار عمومی و میان باشگاه‌ها شود.
◻️
اعلام رسمی نمایندگان فوتبال ایران در رقابت‌های آسیایی، باید از مجاری رسمی و مکتوب انجام شود. طرح این موضوعات در قالب مصاحبه‌های شخصی، نه تنها کمکی به شفافیت نمی‌کند، بلکه می‌تواند موجب بروز حواشی غیرضروری شود. باشگاه پرسپولیس حق خود می‌داند که موضوع مطرح‌شده را از مسیرهای قانونی و حقوقی پیگیری کند تا از حقوق و منافع این باشگاه به طور کامل صیانت شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132510" target="_blank">📅 09:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132508">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwWF50tXiwOq65hB66ky2u6rzOJWWRrIwSq5LA612Y1Q_mcINQ_B-bTGBPBCa1jF_74fVFtGtyBFuhDkQdnYY500OXOqk6GacAPcxLcDEb6vgAY1NITplQn7pqvbhkqB-UBwvCVojnd9S8NGd3b43NiSxGfgbcriBLJtjXyLrLspB1l0MSXwdN-jyGCjw6y7tXisoQ5l0bY1Djr05qrNOzqwoaWBh5UYHzGPP0Kqp1MdAQYZ29-laHiLFQelMTqoeVeTkh1eObkGFwzmXpmjK4ZwnHhcHfBKlYQymHdVDsNcGzKYNiWwheERXD1ftZbMy64rL3hno8kKrEDCWNpAfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
گردونه شانس رایگان وینکوبت فعال شد!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/SorkhTimes/132508" target="_blank">📅 00:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132507">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
در پی فشارهای تاج بر کمیته حرفه‌ای سازی برای تایید مجوز سپاهان، مصطفی زارعی مسؤول این کمیته تهدید به استعفا کرد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132507" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132506">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
کمالوند سرمربی خیبر شد!  پ.ن و. احتمالا پنگوین (مهدی رحمتی )سرمربی کیسه میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132506" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132505">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ErfU6XP0KafcIY14CVl50twCIjktd5aszLh_wD0SZVI5DxGzaLHJ1jJMZNhyarUlSOZnAAAJCpSdBNjHDWkB6GgjEJFYF3ThA-YufRFs2wCNGJpfUrZzwOgipD2NPCX1vEAijHdQ2zqIu31V1YIkp5StoTLEPCecw1DmpA35IKAXm318Dd4W-KnyEBI2_b_MOi7lks3sgLVddNaUqLt7opvc09swOSUGurWQS3c1BMFyjWcY4bpnCwpJFqRpBKcWCPv078ozBZnWa4oF82-F0W6bBkBgbF8cmUrADllGe7XF9to3sUwJ_oTRuQZrElu4jCR-gap8J9iDzcg1ff9uTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00937b1a6d.mp4?token=ErfU6XP0KafcIY14CVl50twCIjktd5aszLh_wD0SZVI5DxGzaLHJ1jJMZNhyarUlSOZnAAAJCpSdBNjHDWkB6GgjEJFYF3ThA-YufRFs2wCNGJpfUrZzwOgipD2NPCX1vEAijHdQ2zqIu31V1YIkp5StoTLEPCecw1DmpA35IKAXm318Dd4W-KnyEBI2_b_MOi7lks3sgLVddNaUqLt7opvc09swOSUGurWQS3c1BMFyjWcY4bpnCwpJFqRpBKcWCPv078ozBZnWa4oF82-F0W6bBkBgbF8cmUrADllGe7XF9to3sUwJ_oTRuQZrElu4jCR-gap8J9iDzcg1ff9uTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های امشب عادل فردوسی‌پور در آپارات اسپورت بعد از مدت ها برای گزارش بازی فینال
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SorkhTimes/132505" target="_blank">📅 00:04 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
