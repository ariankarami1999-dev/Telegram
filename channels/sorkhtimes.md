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
<img src="https://cdn4.telesco.pe/file/Kct_bWr6bykHBygcjDHUMRQEj27Rhf0q548toW-pVlLwFTc5BIeGRfdPRfw-4ZFWxi8nqN4NWrRj2wjydoBBWl6UDHts2mnyxxEtV2OY4GS62ncw9LsoubH-w-T1LlUprFFf6obJbxga73hqg6pEhhTNU00CIDqnv5NoEbh7Ph0oBsT2PWficvlV6qHug8oNr0QNBbL9p91DOaHjyeX5etkS1vw8Ht0AkNdWWYZ0iirf0QXEWpCZ6pbU9UGaJO_WS-RmMEEOcAP8gea_7ljWokjLWaC64c-_leSOg4SKS8t9OOGtC2INTf9Pfx0enX64Xu_LbEnN8QYi9ZOq6uXLSw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 16:41:30</div>
<hr>

<div class="tg-post" id="msg-141433">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce91480d30.mp4?token=snQWI2ZYBjf_3UzV5Y-YSIe1vmVqtzv3y-LAfxYuw9Ypqh_-XrZzoZ4I_kL82RBNyQRbqSuxibYJlVeEwNJMxUCCmVqV9hs2E3Xam5rqUjeH9cWdkM5aKBw5KgsbrXscZjchLL7M3PTMQuVk15uKUFuJpu5yBgz1ylD6kkbgXcgbNCezsJlz0h4NFowi0qMtayMekyhf14MkKVrAIYf0YYpD0ye-JcMR4CsXe16s4FFgFeV9ICwI3P_PWZC7jAm0LPGa35SSzEHIU928yn-b_6pciYXxaCD2zBRgsFny84exBlGLzonVpD3xlf1TJPVZnrZdJqQZa_lTqDj1afmJBnCZP8EXMRjs8X34bNwm79AmsOs6n57s21GsZWDRAzAU6726Ma4sqa6aKWFmDD7pFYziZcGrfjOyj1sAtonFsAZoFwHXWDg_Y0yI3O2UKrhL0EAV__vcaLw8vfuEcbmALya8JM7QqxkPclgeIzlrB1gtGnw2n67NjAO8ZvvbGTsdcgUEA6B_Y2hu6KBDeOjvLDkjXrI_hi_da3vSUy6S1saD8JK8hDOXEJFJ7mC174NSBkmOufm2i1L1-PvUW3y42ayw2GOnpyvlVw6tgxJ_W7qnWc6D8KfLqe8GDJUr13eIFg7ZGya2_GytXK6eMpU-wVdqHJ2zgieVhQpjJJTolSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce91480d30.mp4?token=snQWI2ZYBjf_3UzV5Y-YSIe1vmVqtzv3y-LAfxYuw9Ypqh_-XrZzoZ4I_kL82RBNyQRbqSuxibYJlVeEwNJMxUCCmVqV9hs2E3Xam5rqUjeH9cWdkM5aKBw5KgsbrXscZjchLL7M3PTMQuVk15uKUFuJpu5yBgz1ylD6kkbgXcgbNCezsJlz0h4NFowi0qMtayMekyhf14MkKVrAIYf0YYpD0ye-JcMR4CsXe16s4FFgFeV9ICwI3P_PWZC7jAm0LPGa35SSzEHIU928yn-b_6pciYXxaCD2zBRgsFny84exBlGLzonVpD3xlf1TJPVZnrZdJqQZa_lTqDj1afmJBnCZP8EXMRjs8X34bNwm79AmsOs6n57s21GsZWDRAzAU6726Ma4sqa6aKWFmDD7pFYziZcGrfjOyj1sAtonFsAZoFwHXWDg_Y0yI3O2UKrhL0EAV__vcaLw8vfuEcbmALya8JM7QqxkPclgeIzlrB1gtGnw2n67NjAO8ZvvbGTsdcgUEA6B_Y2hu6KBDeOjvLDkjXrI_hi_da3vSUy6S1saD8JK8hDOXEJFJ7mC174NSBkmOufm2i1L1-PvUW3y42ayw2GOnpyvlVw6tgxJ_W7qnWc6D8KfLqe8GDJUr13eIFg7ZGya2_GytXK6eMpU-wVdqHJ2zgieVhQpjJJTolSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
ترمیم تورهای دروازه ورزشگاه تختی خرم‌آباد پیش از شروع بازی!!!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/SorkhTimes/141433" target="_blank">📅 15:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141432">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=H7USHX6PeZYjOT79s_onVvTFJzDAZ8TskWSrCGt6UpGeP9b-28_ytjauRpidCbo7O3gkQm2Q-GP-P1T58Bh2XX70Kk5BNwENpKkV9lvZn7MIR3hoHDvNZUa22VUHJHfR1ka8qVKmwH8VySR3Qf76x6cBiEFI5pwnWnesjPzWqIuULi__WcSsTX-g9GmoRglJbJrYS8Vlj9QXmNZI2kFuN6tPX4Qik1ap7gJq5iaUQmihGAo7wKBjfmL_KmIfrGEB04wvXCxQ-DvHbCqJNvpgYvyekggDEnX7MXqiX9tmFW9OqS2EDBc-UY833hqYDTjP22w9Cny4p4LL_2y43yxgxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/995cae6ace.mp4?token=H7USHX6PeZYjOT79s_onVvTFJzDAZ8TskWSrCGt6UpGeP9b-28_ytjauRpidCbo7O3gkQm2Q-GP-P1T58Bh2XX70Kk5BNwENpKkV9lvZn7MIR3hoHDvNZUa22VUHJHfR1ka8qVKmwH8VySR3Qf76x6cBiEFI5pwnWnesjPzWqIuULi__WcSsTX-g9GmoRglJbJrYS8Vlj9QXmNZI2kFuN6tPX4Qik1ap7gJq5iaUQmihGAo7wKBjfmL_KmIfrGEB04wvXCxQ-DvHbCqJNvpgYvyekggDEnX7MXqiX9tmFW9OqS2EDBc-UY833hqYDTjP22w9Cny4p4LL_2y43yxgxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
هوادار خیبر: اینجا اصلا پرسپولیسی نداریم؛ بیرانوند بچه سوم را بیاورد و معاف شود
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/SorkhTimes/141432" target="_blank">📅 15:46 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141431">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
محمدحسین میثاقی:
🚨
روز گذشته بیرانوند با مدیران تیم فوتبال نیروی زمینی تهران صحت کرده است که از اول آبان به این تیم برود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/SorkhTimes/141431" target="_blank">📅 15:45 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141430">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b71aafa3.mp4?token=FB2kkHmgfA_YXJjm27xffsxslJHGN2xOK6NlBAOoOxXHfhnF0x0-Jgg3Vr-7YhI01EAJvMkL02eWu78IzgtVwIqaXfpTrJQg-a5UbsBqpvxzsBINHN_GNDPywn8_s3oPO7vCl0lBgyJlgIuMnZUHBtRDhGF1eVv0tohugy8mDMXR_vLWi8bJzvzf9ypky5qYeAQIqZZo7btdXM2fKPz7I0IN2X0tgK9m3MT8mJv6CrrGQa_w2iav3p6JJI7hAXxTaZV1aD3LIxfuCDrpVo1eP0trjKyCfJvrCnFulXdlgXkR6o8mTB3w6eknMmyeH4Cdicq0xjzfMM6RzmAXe0OFZmPtJrmtPbfSqyUyk5u3zhHWlnYsCQMuia6ncGSzqQ_cUDukKNSrpp-h09_aciUwHkOaPxF72kxsBkEtCkkCr00l6-xReaoxgQrYV-hGOF72CevjDszeLOV4dSZTndG5yd75a2KTekMV6trHAEWMKEJLCvsVrzw48itvZw2SpzK9JuumoF1QmKBI5waZbIkXhekUJs5fmtURSYVgwoPLJBN9uB_FFHtikOKOYGsDkXtAGEOem-F7bh3GRPYMpcizKldMhBbWG9wsNpGbxtibCu-til0u2W2C3zZmiSPLNxE4Q1RLEhRAIhbhmBwagNJ2GpPqKaBHhhO5XuxfjViuvIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b71aafa3.mp4?token=FB2kkHmgfA_YXJjm27xffsxslJHGN2xOK6NlBAOoOxXHfhnF0x0-Jgg3Vr-7YhI01EAJvMkL02eWu78IzgtVwIqaXfpTrJQg-a5UbsBqpvxzsBINHN_GNDPywn8_s3oPO7vCl0lBgyJlgIuMnZUHBtRDhGF1eVv0tohugy8mDMXR_vLWi8bJzvzf9ypky5qYeAQIqZZo7btdXM2fKPz7I0IN2X0tgK9m3MT8mJv6CrrGQa_w2iav3p6JJI7hAXxTaZV1aD3LIxfuCDrpVo1eP0trjKyCfJvrCnFulXdlgXkR6o8mTB3w6eknMmyeH4Cdicq0xjzfMM6RzmAXe0OFZmPtJrmtPbfSqyUyk5u3zhHWlnYsCQMuia6ncGSzqQ_cUDukKNSrpp-h09_aciUwHkOaPxF72kxsBkEtCkkCr00l6-xReaoxgQrYV-hGOF72CevjDszeLOV4dSZTndG5yd75a2KTekMV6trHAEWMKEJLCvsVrzw48itvZw2SpzK9JuumoF1QmKBI5waZbIkXhekUJs5fmtURSYVgwoPLJBN9uB_FFHtikOKOYGsDkXtAGEOem-F7bh3GRPYMpcizKldMhBbWG9wsNpGbxtibCu-til0u2W2C3zZmiSPLNxE4Q1RLEhRAIhbhmBwagNJ2GpPqKaBHhhO5XuxfjViuvIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏟
⚪️
🟥
آخرین وضعیت ورزشگاه تختی خرم آباد در آستانه بازی خیبر و پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/141430" target="_blank">📅 14:58 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141429">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
🔴
🎙
پیمان حدادی: از اول فصل تیم گرفتیم هر یک از تیم‌های فوتبال پرسپولیس گل بزنه، یک زندانی آزاد کنیم و تا الان ۴۳ زندانی رو آزاد کردیم.   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/141429" target="_blank">📅 14:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141428">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
ترامپ درباره ایران: ما باید این موضوع را به پایان برسانیم، و این فقط به این بستگی دارد که ما می‌خواهیم این کار را به چه روشی انجام دهیم: روشی دوستانه یا روشی که آنقدرها هم دوستانه نیست.
❌
شما خیلی زود متوجه خواهید شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/SorkhTimes/141428" target="_blank">📅 14:48 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141427">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SorkhTimes/141427" target="_blank">📅 14:23 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141426">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">💥
💥
سید جلال حسینی دستیار امیر قلعه‌نویی در تیم ملی شد و قراره در جام ملتهای آسیا قلعه نویی رو همراهی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/SorkhTimes/141426" target="_blank">📅 14:22 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141425">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtzbCk1ueMzRRA2Z9yPHE5LaEhEJRzLGzQMMYUHH_0uh0lTJQyy4Z8_oN-3jStE0xP4XE93WmLBH_cGIrSGk8mMaVbuIEk6wj6V1BHqE-8_GTO4oz3UbBAbJOpOSOJPxYnhnoLGaxFE5c2SKucZKNkp-0VtkzWPf4-kX8JZmYvhhsZKmxSlgYNpIAZW5gfEfHXtl0TazQeiCQYzHUyFF77g75Jy3CZA_b7kSbwCmFw-oHBegeNf5WVwMFnSumS_GlHFgxmsSOZ_0ZXG2zwBEgXv_RMk2InKidztNuZ76iXBzNkpPvDxw6nbvgOWS59Kjr9R2saErlHwbzTXL8UybSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
نبرد غول‌ها در اتحاد؛ سیتی و پاریس برای سلطه بر اروپا!
🔥
⚡️
[
منچسترسیتی
🔵
🆚
🔵
پاری‌سن‌ژرمن
]
⚽️
[ نکات کلیدی و مهم ]:
👇
1⃣
.
نبرد مالکیت توپ:
سیتی با پاس‌کاری سریع و پرس از جلو به‌دنبال کنترل ریتم بازی است؛ پاریس روی انتقال سریع حساب می‌کند.
2⃣
.
فضاهای پشت دفاع:
سرعت مهاجمان پاریس می‌تواند خط دفاع سیتی را در ضدحملات به دردسر بیندازد.
3⃣
.
نبرد خط میانی:
تیمی که توپ‌های دوم و دوئل‌های میانه زمین را بیشتر ببرد، شانس بیشتری برای کنترل مسابقه دارد.
4⃣
.
موقعیت‌سازی و گلزنی:
کیفیت ضربات آخر و استفاده از فرصت‌های داخل محوطه، عامل تعیین‌کننده نتیجه خواهد بود.
5⃣
.
سناریوی بازی:
با توجه به سبک هجومی دو تیم، گلزنی برای هردو تیم محتمل است.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 3.26K · <a href="https://t.me/SorkhTimes/141425" target="_blank">📅 13:28 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141424">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/SorkhTimes/141424" target="_blank">📅 12:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141423">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
محسن خلیلی، سرپرست پرسپولیس:
❌
یاسر آسانی؟ باشگاه تمام مسائل را از صفر تا صد پیگیری می کند. داخل کشور به نتیجه نرسیم صددرصد در دادگاه عالی ورزش دنبال می کنیم. ما نگفتیم این پرونده پایان یافته است. مندیت آسانی به پرسپولیس؟ بله او مندیت را داشت اما زمان همه…</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/SorkhTimes/141423" target="_blank">📅 10:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141422">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PsI6FUy-u9CNgJv2iMP-bPVJmY1S9TE3eUqv5LrjTtyDrCf4YIx7HVI4ndNHtD3OwsQvRYMyJq-NcBoPYE2MAr3CCsLCBHkPC8PiYcyMA3OXtK_I7nPez2ScCqW3wcZf-lu7DaEp8K3KGAij0M0749OS3nvhGjL7l25H9KvAb4lizpYYUqdC6KMDjBDEukmpTrGnTzmtL95XtNZkJ7Y-eLi_l96ufwVr4CPMQ2aQ31wYiNl8hDyORZj_CryeUYbXjTogpy3k7B9wiSXWNEvF_ecN70NlPPTrofDAcyff5BFJbr1ACGl3NSY5rTYHaO8IRwY4X7KxznCTFrWDfKRyIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ورزش‌سه: دنیل‌گرا به مرز آمادگی رسیده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/SorkhTimes/141422" target="_blank">📅 10:42 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141421">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
🚨
حمله تند امیر قلعه‌نویی به عادل فردوسی‌پور: قرارداد من رو گفتی، درآمد خودت را هم بگو. بگو اسپانسرات به کجا وصل هستن. بگو در جام‌جهانی چقدر پول در آوردی. تو فقط ابزاری. هر وقت بخوان میزارنت داخل کمد، هر وقت بخوان میارنت بیرون.   «سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/141421" target="_blank">📅 09:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141420">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/141420" target="_blank">📅 09:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141419">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🤩
✅
معوقه هفته‌هفتم لیگ‌برتر فوتبال
🤩
پرسپولیس
🆚
خیبر خرم‌آباد
🇮🇷
🗓
تاریخ چهارشنبه ۲۲ مهر
⏰
ساعت ۱۷
🏟
میزبان خرم‌آباد  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/141419" target="_blank">📅 09:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WihoNsy5GidSOYSi0iSwSbFnx-s_sp91KT4w4qOTQrvoKzPyIaKnkB4GLixNOyaMjsZElWM2plV9--m-8ZCya_VtoRzqdlG-1QL0WGw7dv2pGBZNIxZv84b1zLPoC0_5ue1VxRKy6iUR1hXgbAoGQ4qGZ54lv83COr9X7I-C2Le6Nvz6KaDs-1xFY2MboN5z06Rro_OvCwuJddz8SgHN6vYU426jcPD8p2HJXdzqfmZyy3AI6XdLGImj7U2LQKOtMvhtNrH6O47yi8v3XwX1zyzGDXBo3shMzDO7LvXpUVBD9TQZlXMSRlSaNyiMqB9-QcHFMu1rvCWRPt46njdxkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب، لیگ قهرمانان اروپا در اوج هیجان؛ از نبرد سیتی و پاریس تا جدال تاریخی رم و رئال، یک شب تمام‌عیار برای عاشقان فوتبال!
🔥
⚽️
نبرد سیتی و پی‌اس‌جی، تقابل سرعت هجومی و کنترل میانه میدانه؛ جایی که کوچک‌ترین اشتباه دفاعی می‌تونه تعیین‌کننده باشه. رئال مقابل رم از برتری تجربه و کیفیت فردی برخورداره، درحالی‌که لیورپول با وجود غیبت چند مهره مهم، شانس بیشتری برابر لاسک داره. دورتموند هم روی کاغذ برتره، اما ضدحملات بودوگلیمت می‌تونه معادلات بازی رو تغییر بده.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی بازیای فرداشب همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/141418" target="_blank">📅 01:17 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SRlvL49XNuRq71emfmVNMz9MM8AWOwSfVUZov4IqoQCdZe2e1l474z1V_2czjeLhxYnkBtAI2g5329nCSN2FUfAriqREdBAmp8sdX6RncjwpjWyiMFX57k4f5WBbZPlqTwuxLS2EipjcONYgQZ9G4MKEPMO4UPQ7gzJJ_YCmJ2pOlPU0Hbgp0h6cKfkQ6fy21gHTV4H-dXjIxg73aqIDnzNz4pLYzoXl5cS5ERRrqIMkHKhkuxb2pixXT2cmL8IHVO3NA5C7A8BvoURmVator0lg8vtX0ZMJYTniJTLWJWNbRZhQLMZfg3wwO3iTxFW0KcEhegXJlCD4Dln9kcmFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مقایسه نیکمت پرسپولیس و کیسه در دوران محرومیت
❌
کیسه بجز ترکیب اصلی فقط حدود یک همت قرارداد بازیکنان ذخیرشه ، این وسط هم دو سه تا جوان هم گذاشتن روی نیمکت که مثلا ما هم اره...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/141417" target="_blank">📅 00:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHGWy09yAOkoLQHJEFehOc5sExIJKhNY5X7S3ptl9Jbp1Xs164pw40zbR1M9m6Nrz9jv3Mkq8H1QWQt260BFNr7GV2LFRSpSanYMXK2f-dzIwYNFNEhEZEQ4yaCpe02ay5RnGpuAK_--w6dr2qVryiU2ZOcImJSZ9ZJHQyzKRuEhKbEkivjWqyo2h0ulTmCZsy00Q0XiK70mfQ9xI82n3M2ahthrhvn0btiopy8cbv5fzgtwwV38s6Grk3fTWiIUWPlWGjmtP3hiXyhMm96zAS8M7rsWVFEZzu2qnSK1g3zgtkeiEcdruo9uWO_-AUnUT59cod0S9R7zVMaW2DATLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کریستیانو رونالدو : من کامل‌ترین بازیکن تاریخ فوتبالم! اگه کسی مسی، پله یا مارادونا رو ترجیح می‌ده، این دیگه سلیقه شخصیشه و منم بهش احترام می‌ذارم. اما اینکه یکی بگه کریستیانو رونالدو بازیکن کاملی نیست، یه دروغ محضه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SorkhTimes/141416" target="_blank">📅 00:33 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsxKW0NaqxgGa5Esitz5NfJ14U-arXb2fxSpSmjj1fLWGSG_nyxOD3_ZfQTGMR5iXfONdgvU6njDYY3DkOvOfKdqn_Ffk7Lz9TyswgqBWxTVpJl6cvP0rM-J3xW4EvkE664Kp6wQXApbbmMwoOqnwnS4N2z7ROQr9xoB5R6ceeQ1rKW1R1lHTP6kTPYwOPpaSAVfCnRUlcBINg8e4tJj8FNq_eHM-884UwgGJkc1fyVow7acveeu5adyubs8b6tsH-4IBWxGP_K5QrlBwXGEVYZVv73_DiEhfMT5gbjoQwR3c_P_7-eYdqI3wFPr-BUXfGd69oxXw6RonEYvkEZ5hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
سعیدی: هیچ‌ نمونه مثبت یا حتی مشکوک در لیگ برتر فوتبال نداریم
📘
دکتر رضا سعیدی قائم‌مقام ستاد ملی مبارزه با دوپینگ ایران، وضعیت کنترل و مبارزه با دوپینگ در فوتبال ایران داشت تاکید کرد: در این فصل از رقابت‌های لیگ برتر و لیگ آزادگان هیچ نمونه دوپینگ مثبت یا مشکوکی نداشته‌ایم. باید اعلام کنم به طور کلی در ۲-۳ فصل اخیر هیچ‌نمونه دوپینگی در لیگ برتر و لیگ آزادگان مثبت اعلام نشده است
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/141415" target="_blank">📅 00:16 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/141414" target="_blank">📅 23:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141413">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9243295073.mp4?token=VPvMtKOt4Y6h_HXX-D7QQ4n44KLf9b3IF362HMtpCB9XziZWizGlmiF2Y94NSfNLCxq6pMQtLyicVoI-E7c-KiBZLQC4yeDtgOACKdSk6EGIcdQBKbjBudOdBlvgcV7Ml_yvKsvTiUgkqMftrAlQfV2fQjqHhfTt067eqOtRU5oL-2wGdnCdNLcTOZIhVtNJvwWmZxhjJPMJEWtejCfZfTx_PwuYABshkdfaORtUBy_lT7rszkYVsCX_dlghdGIUsyQLNpk-QQPkq2ULqJrY5vcs9iz4PGaH-_rLGiBmAWVSCQetJur-CTwI0lCqhXiKXSqxkMWNTQAb1un-IRor9YutPFZKu0EVHdESFhdeTDLH_mIC2dNhh5sRPG_Cv4oe9czaR-c6DYGRaKUBSAcmrrxRI3FRQ_W-ogCK7PMPq2yQ8Gr-cctxeXiugbye98Bjt6o18Epu8iB-REJ1dR5RqYsfXK9AyrMshEa6BwuIhnn-K4_ENk7cZw-5c69xY8pjBMJwfp_99KLQLmGOFHaJO_7DL4pcgYQzWEZ4PXLz0nlX6pbIw5imtZESp2yUrhNFcptXzOFkEQkHufq2gB_FjFY1F6lFpQ0dMxutez_N_4bOcjC2vfhVpkWIlR4oG0HJIj3GUQdbUWEmqVUyQf0LNksNqAlDlfTDF2p6O8055iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9243295073.mp4?token=VPvMtKOt4Y6h_HXX-D7QQ4n44KLf9b3IF362HMtpCB9XziZWizGlmiF2Y94NSfNLCxq6pMQtLyicVoI-E7c-KiBZLQC4yeDtgOACKdSk6EGIcdQBKbjBudOdBlvgcV7Ml_yvKsvTiUgkqMftrAlQfV2fQjqHhfTt067eqOtRU5oL-2wGdnCdNLcTOZIhVtNJvwWmZxhjJPMJEWtejCfZfTx_PwuYABshkdfaORtUBy_lT7rszkYVsCX_dlghdGIUsyQLNpk-QQPkq2ULqJrY5vcs9iz4PGaH-_rLGiBmAWVSCQetJur-CTwI0lCqhXiKXSqxkMWNTQAb1un-IRor9YutPFZKu0EVHdESFhdeTDLH_mIC2dNhh5sRPG_Cv4oe9czaR-c6DYGRaKUBSAcmrrxRI3FRQ_W-ogCK7PMPq2yQ8Gr-cctxeXiugbye98Bjt6o18Epu8iB-REJ1dR5RqYsfXK9AyrMshEa6BwuIhnn-K4_ENk7cZw-5c69xY8pjBMJwfp_99KLQLmGOFHaJO_7DL4pcgYQzWEZ4PXLz0nlX6pbIw5imtZESp2yUrhNFcptXzOFkEQkHufq2gB_FjFY1F6lFpQ0dMxutez_N_4bOcjC2vfhVpkWIlR4oG0HJIj3GUQdbUWEmqVUyQf0LNksNqAlDlfTDF2p6O8055iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
فراز کمالوند: پرسپولیس آماده‌ترین تیم لیگ است؛ شناخت کافی از پرسپولیس داریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SorkhTimes/141413" target="_blank">📅 22:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141412">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
دبل سردار آزمون جلوی الاتحاد توی ۱۶ دقیقه ابتدایی روی پاس غندی پور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141412" target="_blank">📅 22:17 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141411">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
ترکیب پرسپولیس مقابل خیبر از دید ورزش سه
📊
سیستم 442
⏺
پیام نیازمند
⏺
مجید عیدی
⏺
مهدی زارع
⏺
حسین ابرقویی
⏺
مهدی تیکدری
⏺
پویا پورعلی
⏺
محمد خدابنده‌لو
⏺
محمدمهدی محبی
⏺
اوستون اورونوف
⏺
علی علیپور
⏺
ایگور سرگیف
🗣
نظرررتون؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SorkhTimes/141411" target="_blank">📅 22:12 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141410">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه
🔻
کمیته انضباطی فدراسیون فوتبال با درخواست باشگاه گل‌گهر سیرجان برای تعلیق دو جلسه باقی‌مانده محرومیت امید عالیشاه موافقت کرد.
🔻
کمیته انضباطی پس از بررسی درخواست باشگاه، با توجه به سپری‌شدن دو جلسه از محرومیت…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SorkhTimes/141410" target="_blank">📅 22:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141409">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🔴
از تهران تا خرم‌آباد با کاروان پرسپولیس
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/141409" target="_blank">📅 22:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141408">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❌
❌
❌
محسن بنگر : امید عالیشاه اهل فحاشی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/141408" target="_blank">📅 22:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141407">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785f027d31.mp4?token=YtbtKYWW4gMTWXXmBUrKMnnGtSsLMfwDRea3ScxLxQUq8R0H5rh1i9R7LfSsOgxxkyJRjlKHpPdVWJ3cO3uRSq9JDXV43LRQRiFqi7UpPIBCTf2ZYTXjHKfTBdlR94BZHEtR20S-TxqFTXllku0W6RLQiIG9C-UgcBHw7apb6DqrFkfnG9AGWl0IyN4S2k_NymsmVQBatj_UTbZtscm1HVFr6Y1U6Z1rmCjR3k_IJPy7YFiVIbG9hPK8HU_C40k8l5pTyWm5ISMKQLgI4ve4btFX-LUIEm7Oslvrr0cr7WkAPELudpaHygjxuBLrnSblpELRN8OrJeMeU24C9iRhCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785f027d31.mp4?token=YtbtKYWW4gMTWXXmBUrKMnnGtSsLMfwDRea3ScxLxQUq8R0H5rh1i9R7LfSsOgxxkyJRjlKHpPdVWJ3cO3uRSq9JDXV43LRQRiFqi7UpPIBCTf2ZYTXjHKfTBdlR94BZHEtR20S-TxqFTXllku0W6RLQiIG9C-UgcBHw7apb6DqrFkfnG9AGWl0IyN4S2k_NymsmVQBatj_UTbZtscm1HVFr6Y1U6Z1rmCjR3k_IJPy7YFiVIbG9hPK8HU_C40k8l5pTyWm5ISMKQLgI4ve4btFX-LUIEm7Oslvrr0cr7WkAPELudpaHygjxuBLrnSblpELRN8OrJeMeU24C9iRhCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
وحید امیری بازیکن سابق پرسپولیس پس از ۷۰۳ روز موفق به گلزنی در لیگ‌برتر اینبار با پیراهن فولاد خوزستان شد
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/141407" target="_blank">📅 21:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141406">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwxe7fujb_96-HHskN5lmNnXqdY2GlxzGSTnpEuNXP8Sscj-HnFtEIlmNXg-IWXTqA81noXY4uT-cDSrtsYbdxWRRhuOXyLWti6AdqArDpnK0bcaK73N_K_2ql1ZEiLIGezw44FHio32m6xcmVoCBE2IGHOlpXBGhdd0f7L-VGJlNjy15Lr078rjOxoVLK2elTxebA8yf2coM_w4v-BWogJGl2rCr60NaYLUFvDHmr0e2P1OxQfSqqnYd_YTuORnjD6g9nOc1woG5pI6ZMLYqdgqR0D26YbD6EuzpGKN5Zy0zQq23BbQEaLh24Lu4v0adwz59svk2mzRUyUmDsV9wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تارتار به نشست خبری بازی با خیبر نرسید.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/141406" target="_blank">📅 21:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141405">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAaL58gbDsf3Y-_pgJ58BHuW1yPExw84L84K4xVneuJs8S5S67AdO6HMaed3i5Rwz1CL8HXOgwFn7HF4M4CErbF5r4ASmqE18LXeoIyB0z4lqXoYEcsSPh36KpzbO3HnNOdJ8nK-DhO5FkLSGG5PmcyECCZ85vKFK-GJMpVx2kKdMy1WPM1dJcHYrQ6Tu55LyrqvInBFLkO4l_u43hM9IMKRS46fEtgZkXBba2s0ezmpXYepxLK0hf9DoP8Rp-s1q12XdSBNSVtLt-ayQmW7Ce7AX8_vuPF-7xfBc3H4iLmgb8zKghCHV0GjobROx1nI7hJj6SlO618lUA4PJAxPTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
جهنم استانبول در انتظار غول کاتالان!
🔥
[
گالاتاسرای
🟠
🆚
🔵
بارسلونا
]
⚽️
از نظر آماری، بارسلونا در ۵ بازی اخیرش در لیگ قهرمانان و لالیگا ۵ برد داشته و در مجموع ۲۴ گل زده؛ گالاتاسرای هم در شروع اروپایی‌اش ۳ - ۱ به اسپورتینگ باخته است. بارسا در ۱۰ تقابل قبلی دو تیم، ۶ برد مقابل یک برد گالاتاسرای دارد؛ با این حال، فشار هواداران در استانبول می‌تواند بازی را پیچیده کند.
سناریوی محتمل: برد شاگردان هانسی‌فلیک.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/141405" target="_blank">📅 21:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141404">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
🚨
مهدی تارتار: از فدراسیون می‌خوام که جام‌حذفی رو برگزار کنه و مام حاضریم فقط با جوانان مون بازی کنیم.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SorkhTimes/141404" target="_blank">📅 19:56 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141403">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=mf8N_TBxxElGlK90q5seKusK7DkvXwSkbdhmJrss_9gWFLsx06T61RxlJ2s2SsKco5agy_YX8DdCeVsF0E1fI1xJMGbL2v3Uu3f60awLG0Y35uTQIwE15zKcLMlHu_W3Dpz9nDuypk_0c4P_1jsBlUfuM3Rk2SOlV4NaW2DPfefgvRDDUawYWKZC222rXLAUkmDYSBK771Til4qPfUHwkHaCEX3PwpN0SY7pglmoSLSc5dWQL9WC5XBtXaltCpLv7-RwYlXGiokrIoF1moRewr5nhvq2HzjoQXZtIzmBiO44J-GiEVSTttK4i4LmRrgavbM83eH5QM-1pz0CnMJD5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f8f94fff6.mp4?token=mf8N_TBxxElGlK90q5seKusK7DkvXwSkbdhmJrss_9gWFLsx06T61RxlJ2s2SsKco5agy_YX8DdCeVsF0E1fI1xJMGbL2v3Uu3f60awLG0Y35uTQIwE15zKcLMlHu_W3Dpz9nDuypk_0c4P_1jsBlUfuM3Rk2SOlV4NaW2DPfefgvRDDUawYWKZC222rXLAUkmDYSBK771Til4qPfUHwkHaCEX3PwpN0SY7pglmoSLSc5dWQL9WC5XBtXaltCpLv7-RwYlXGiokrIoF1moRewr5nhvq2HzjoQXZtIzmBiO44J-GiEVSTttK4i4LmRrgavbM83eH5QM-1pz0CnMJD5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
وضعیت درب محل اقامت باشگاه پرسپولیس هنگام رسیدن تیم پرسپولیس در خرم آباد با حضور هواداران خیبری
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/141403" target="_blank">📅 19:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141402">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
تارتار : بچه هامون دارن به تناوب بازی میکنن، دست یه مربیم اونقدر باز نیست که بتونه 15 تا بازیکن رو بذاره تو ترکیب، انصافا استون هم تو تمرینات داره تلاش میکنه، من دارم میبینم همین قدری که تیوی بیفوما داره تلاش میکنه استون هم تلاش میکنه ولی به هر حال گوی سبقت…</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141402" target="_blank">📅 19:51 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141401">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNDW7hx8OOS_N9Q2p1QkkOOiFDwU_x4-JclWQE3q7mrG-B0sGKUFV7Q1N1DJ-1pk7_74kC2sP5ZOYV-FpMq_3lgdD6q-I1YPx9ilSeMudxPvylDmou7ULRh1NThCpqklR1YGoDalg-dudFh15Ctt80UPUDipAKllGuPbG1Dei8TlDKUDNYRBW_IIXTGGRNM1rexIdKQaG8DaqJsOs0hSipbJTKiyiD-cS_pewfKRrOSjnGtGuSJsQLYJEebMT8stCm_tDxniZvGy_YUoFAdqyq6ZguW6o94eaLbXgucFlWFT9mwDtQWERlsQEiz3SSj9Ohrege_6UhRNGK15nxJM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☑️
جدول لیگ پس از پایان ۳ بازی معوقه هفته هفتم
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SorkhTimes/141401" target="_blank">📅 19:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141400">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
بیفوما در آستانه دیدار مقابل خیبر دچار سرماخوردگی شده  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.68K · <a href="https://t.me/SorkhTimes/141400" target="_blank">📅 17:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141399">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
شایعات : بیفوما با برخورد با یکی از بازیکن های جوان پرسپولیس مصدوم شد و بازی فردا رو از دست داد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/SorkhTimes/141399" target="_blank">📅 16:47 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141398">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/141398" target="_blank">📅 16:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141397">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">✔️
✔️
✔️
منهای ورزش :همراه اول تو جدیدترین شاهکارش، سقف مصرف بسته اینترنت ۷ روزه «نامحدود» شبانه رو از ۱۰۰ گیگ رسونده به ۲۰ گیگ!
✔️
اینترنت نامحدود تو ایران = ۲۰ گیگابایت!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.87K · <a href="https://t.me/SorkhTimes/141397" target="_blank">📅 16:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141396">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma2uxQm1VUP80cx2PaOV8JdHdFECKGBcZyYFlZVtXryPkGu3YIBYcjDU3N5-THe2TtBO9lBROV6UfI-pTWQ6czRD5Slv_zTt_kVDQaPR2ubNx5Pkz8KpnM-viInUYY_U3jV7AGdbyzhj0GVmJf7-r5-g9TMrSeWNC9OXm2xCl6csaAj34_iF4CnurLi3DmUZ8aYGYB_oCZ3DFrQBvJ5zg2nDp8NBhybs65d-NC6FszHdif4ng2mHfH4XX_cM29JdjpyNJXBqRB5KywKaF_EuQqw63_yW6d-JG9dwDSKS24Kg2IgSNh2C-5rm93BASIl7KyKxcOSUZdaeFyTGRWpTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مهدی عبدی در دیدار فردا در ترکیب خیبر مقابل پرسپولیس حضور خواهد داشت/ورزش‌سه
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141396" target="_blank">📅 16:32 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141395">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک…</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141395" target="_blank">📅 15:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141394">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVdxs-XOtS5gVYIGA6uQnHBgnwBVZxtHZrKVFJTDz9bc-Tko56sULIOb1mlepS_fTqb1rduFnbWBi0Mt3mC5vgNplF5zeHgIgDKck9N2NSlqBh81ANe_yZWXH_suM3onldyCBCvwKvA2Xqked2cCUD8-NWB_O-0QDVyvs6E2exzJv6PKfiUarc99efIEV1A7o-su5rXD8l9t00bodbneLQoVghPEq13VoY8RMy68RxWud7f4USGinwalUj0-97bXceUjIKp0aGRoU3dBT6oCR3eED64pGjlNdiVNxXf8ii75MPwUDrGjfE1Za45-OJrFeZXqnOK14k9ieU3AxwKIcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دانیال ایری به تمرینات پرسپولیس برگشت.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/SorkhTimes/141394" target="_blank">📅 15:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141393">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
حسین کنعانی در صورتی که فردا بتونه در تمرینات گروهی شرکت کنه مقابل خیبر بازی خواهد کرد اما اگه انفرادی تمرین کنه به بازی روز چهارشنبه نخواهد رسید
✍️
خبرگزاری فارس  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/141393" target="_blank">📅 15:41 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141392">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFYH760ZUFzvhfnRhBUtciveN44O5_KK72NtqfrH72B5c3G5r102QoRtpjWfSa9DQ_kmYly1dhb9JMfUT3X52P4g6uiL4IZivEml-HrzYOJdiEJHzFnEkkenOksM0oMXcM2j7toibNU8F_mK8-AJJs9_WOLqyDlaGWpMA2UsOa25twXYHaeHmMjRIJrYYYW4In2Sm56Q7ou8DSUfFGdmRMAVQ42KFUFqkYPai3JcifmdYSS154qE3H78j7yoxYnVOs87w6YzScHUAQ55mmexNst_HZYo29s67zsiwNutOk-nVX57T_sB8Isv8JXT3wirgAT_-I9Vb2V9LoMexTMWqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
برنامه چهار دیدار معوقه هفته هفتم لیگ برتر
❌
پرسپولیس در دیدار معوقه هفته هفتم از ساعت ۱۷ روز چهارشنبه به مصاف خیبر خواهد رفت. پرسپولیس درصورت برد مقابل خیبر، با 19 امتیاز بالاتر از استقلال و تراکتور صدرنشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141392" target="_blank">📅 15:39 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141391">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
رسیدگی به پرونده محرومیت بیرانوند اول آبان در CAS
❌
❌
دادگاه عالی ورزش اول آبان‌ماه با حضور نمایندگان حقوقی علیرضا بیرانوند، پرسپولیس و فدراسیون فوتبال، دفاعیات طرفین درباره حکم محرومیت چهارماهه این دروازه‌بان را بررسی می‌کند. امکان حضور آنلاین نیز برای…</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SorkhTimes/141391" target="_blank">📅 14:37 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141390">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
به ادعای خبرگزاری هفت ورزشی مهدی تیکدری از بازی کردن در‌دفاع چپ ناراضی است.
✍️
هفت ورزشی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141390" target="_blank">📅 11:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141389">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=WXyw-Awy0zN0EdYiKC9pVeMjjl2hajvxV9NcWE8dPM6sU6-de_xdJeQEso2UQP3f5gaVal2wRExO6zD91p-c2KQsroUTGAzKGPYkTToNEyt8fW0CTSyu3dm2eLN6Puo9yFgPDQuibrrVkxHqkd18UYbX27tjkbGnK8DY0e9vTJIok0D0YYwCr20kK2udz5A4ICYyrW_9A34ojBaIREGoLUD95a-haVtKzVTdTPTQ5MNsylmJg4m0Z_5ULnua0Tm6JZkVQ6oRKgyUKiof0CZ6d_BCek5t-Lu5o7X9sL2K7uEG8ZRsaoNdap40oY1fKkT36vzi646OKDqubdh92WDDGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb1d8d44f8.mp4?token=WXyw-Awy0zN0EdYiKC9pVeMjjl2hajvxV9NcWE8dPM6sU6-de_xdJeQEso2UQP3f5gaVal2wRExO6zD91p-c2KQsroUTGAzKGPYkTToNEyt8fW0CTSyu3dm2eLN6Puo9yFgPDQuibrrVkxHqkd18UYbX27tjkbGnK8DY0e9vTJIok0D0YYwCr20kK2udz5A4ICYyrW_9A34ojBaIREGoLUD95a-haVtKzVTdTPTQ5MNsylmJg4m0Z_5ULnua0Tm6JZkVQ6oRKgyUKiof0CZ6d_BCek5t-Lu5o7X9sL2K7uEG8ZRsaoNdap40oY1fKkT36vzi646OKDqubdh92WDDGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کلیدواژه همیشگی مصاحبه‌های بیرو
درصد، دلار، ماشین، میلیارد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/SorkhTimes/141389" target="_blank">📅 10:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141388">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141388" target="_blank">📅 10:27 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141387">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-ftmmykfyNH8Mlcmy-PO79grvSjrOetezcXKxiQIz9iV_EG66rC-Ypzqr--Ney8tGRHE561ws4j38Ar236bNV8E0QKf130GWX9xoYz3mzQfi9V_rkDWDA1XoYCXAa9zA4GgZPaTb4mbSUNxod08nrMjwsXDoxDxM4hsUluGe3sUMBg6r8pfqJDpGKo9bgzkjP4CpIwnSJ2HQoM0K6xvCIbEOKKIz6kys7WvFmx8ZuCkQJx3WKVBNi9Srg_yxHOJMhEYpZgD4sblRUFTGsRUzopV1zVG2QKW7oneHggkwQFtLEPrANvRajIBeJrCXwomv23d6dUJxFrRhu5sduPNxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📘
⭕️
همین یک‌ قاب از تلویزیون و دوخطِ پشت‌سر میثاقی که نوشته « با اثر فوری فسخ کرده است» کافیه برای حقانیت شاکیان و غیرقانونی بودن این آلبانیایی شارلاتان. همین یک صحنه بسه و دیگر هیچ‌!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/141387" target="_blank">📅 10:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141386">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
افشاگری میثاقی از نامه وکیل آسانی و فسخ قرارداد با استقلال در تاریخ 14 جولای!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/141386" target="_blank">📅 09:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141385">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🎙
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
◽️
عدم حضور در لیگ‌های معتبر؟ بازیکنانی که در امارات هستند با اسناد نشان می دهیم نسبت به بازی با مصر 25 درصد افت داشتند
◽️
تغییر در همکاران؟ نه چرا باید تغییر کنند؟/ در جلسه هیات رئیسه من 10 دقیقه توضیح دادم و یکی یک سوال نکرد .من گفتم توضیح فنی و گزارش را دادم و اگر کاری نیست برویم چون قرار بود تصمیم گیری کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/141385" target="_blank">📅 09:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🎥
امیر قلعه نویی، سرمربی تیم ملی فوتبال:
🚨
ماجرای بیرانوند و وساطت برای او در بحث سربازی؟ به هیچ عنوان، وقتی قانونی هست باید یکسان برای همه باشد
❌
بیرانوند باید شرایط قانونی سربازی را انجام دهد
❌
او تمرکز لازم را در این چند وقت نداشته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/141384" target="_blank">📅 09:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141383">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65a8965627.mp4?token=Y6wLbxxl4k6XPqSyLaIEggxxFRaFwDMII0JmIfR6dFLgTDtV4KeIn4oZ6j7KJClV9i4FvmwxUgIyyJx4mbJPwM6nR0YBKaU5BZkuOV63l9q9mzjRXqj3KeYDvTVlaWtXY1GCUCFKQDbapOwGAOp4xA1A5ZUG5sn2i-Zyhcx4ukzOFzZPt4uxA5u_WtLPysokKla4W3DHV1E79hcNjDlaqo4_6afDX9--tRh1RgoTPwIcYoq8-Y2eSpwDlQHXWr8aXAMoTnVOoY_qdUksDYsQmtp7G-YDEYW6Zx1KRZ7LHAWBN7S1inLWfp1DSbWlbbpyHpe-7RpeeFRkkcwSqXrnlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65a8965627.mp4?token=Y6wLbxxl4k6XPqSyLaIEggxxFRaFwDMII0JmIfR6dFLgTDtV4KeIn4oZ6j7KJClV9i4FvmwxUgIyyJx4mbJPwM6nR0YBKaU5BZkuOV63l9q9mzjRXqj3KeYDvTVlaWtXY1GCUCFKQDbapOwGAOp4xA1A5ZUG5sn2i-Zyhcx4ukzOFzZPt4uxA5u_WtLPysokKla4W3DHV1E79hcNjDlaqo4_6afDX9--tRh1RgoTPwIcYoq8-Y2eSpwDlQHXWr8aXAMoTnVOoY_qdUksDYsQmtp7G-YDEYW6Zx1KRZ7LHAWBN7S1inLWfp1DSbWlbbpyHpe-7RpeeFRkkcwSqXrnlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
امیر قلعه‌نویی: کنعانی زادگان و علیپور؟ کاش تیم پزشکی بود و می گفتند که آنها مصدوم بودند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SorkhTimes/141383" target="_blank">📅 09:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141382">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=SCBRZCEcEXosIwh1hWogYdNoYlmYgaKr9BqP97NWkRzO93i4tWtCIQbFxL5N5p7lMmUEM1_qf5wlFV59N3qCd_gGXQQC_Nih1sz9HcjOrbWaypQZ92ROh0XVhIPCTrfPNsgsVif3WcZ5D9mLnHo8eRibFZIKkkbh9cAdimfrwIR20m41zauUBOKEt-bVYaGxXK8C5wqjgdhBTTkBPTZngg62jrVMYGL8tHgMoiPJNmH9Hb9fADaajdJambd9pgaZ1iEOdfNmf-uM_9KdR2rSJjlPrX9eL-a9b_M5-7ETbFv1OTq1_wmZEigj23Z4rHU7YcNzUx2jZ5soH1U1kP1QrYT-l08NR_IzButGTFnKaHHCUe-xdCyJn0sY3XFAcXXIExjrMpfG9h1RFkJF053u8A1o6XakKwlNyYFRbZ563zl7Ff2MdsbBGDcS2lTQbsFHI0nftm_umYvt6V8fxaMPuli5JPGadVcgz8vnH3ClDhUsOI3yKu6UW-5mlFr58CuK6C3c7k-ZwwFL8qpZ8SKsv0CXlei1bD539dZDGK6mHlUKekrTkSDrVy2FiHx0J-IDs5I4Fn0-2nKwSrcA2Ctk4iBtFR-mqlVLq8RsdX9gGD28ReqVNBjWzmjbeUXmmXaS3YCu6UFE0tj-evTV9yH70WtjYJuuJ_maIOrkSaYNh08" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e06a6489f2.mp4?token=SCBRZCEcEXosIwh1hWogYdNoYlmYgaKr9BqP97NWkRzO93i4tWtCIQbFxL5N5p7lMmUEM1_qf5wlFV59N3qCd_gGXQQC_Nih1sz9HcjOrbWaypQZ92ROh0XVhIPCTrfPNsgsVif3WcZ5D9mLnHo8eRibFZIKkkbh9cAdimfrwIR20m41zauUBOKEt-bVYaGxXK8C5wqjgdhBTTkBPTZngg62jrVMYGL8tHgMoiPJNmH9Hb9fADaajdJambd9pgaZ1iEOdfNmf-uM_9KdR2rSJjlPrX9eL-a9b_M5-7ETbFv1OTq1_wmZEigj23Z4rHU7YcNzUx2jZ5soH1U1kP1QrYT-l08NR_IzButGTFnKaHHCUe-xdCyJn0sY3XFAcXXIExjrMpfG9h1RFkJF053u8A1o6XakKwlNyYFRbZ563zl7Ff2MdsbBGDcS2lTQbsFHI0nftm_umYvt6V8fxaMPuli5JPGadVcgz8vnH3ClDhUsOI3yKu6UW-5mlFr58CuK6C3c7k-ZwwFL8qpZ8SKsv0CXlei1bD539dZDGK6mHlUKekrTkSDrVy2FiHx0J-IDs5I4Fn0-2nKwSrcA2Ctk4iBtFR-mqlVLq8RsdX9gGD28ReqVNBjWzmjbeUXmmXaS3YCu6UFE0tj-evTV9yH70WtjYJuuJ_maIOrkSaYNh08" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه‌نویی: در پست خدابنده‌لو، عزت‌اللهی، قربانی، حاجی‌عیدی و نورافکن را داریم و به همین دلیل دعوت نشد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/141382" target="_blank">📅 09:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_de64zrJXorZTkyaIXicV5qUK7x44jyrFX351tDwZ3L95GU2BJgZSR-lJbz6BOQflaG1qoR8fVenqdrPKMI3yU1PvlcnNKPn5tVUT-NFKQ06tP5ra0ujDPhjtQdrr-DE9QGfJReYCHDDa1S4JuO9FIKVKj0E-JHtOrC5vqtoMBH-GQO1016buFffY6EF_Lwj8nKp2imBPek8zE8Vqf9-FlIqteAImUF7SXBwQE2tJjg86KNYGPY698ZFMqDJoTyGoDjE1__OSVAkKc4rNUM-ugJD9FyMLHqzpCC2L4C4IiFtLnLMeSdfTFfYiiWpXT4AdSEdrgeTss5K2YiRcGpgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
به رئیست بگو خر خودتی…دستتون رو شده؛۳۰ مهر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/141381" target="_blank">📅 08:25 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZeenoEisiMMM-AasXprxqUXmvErWGwUlIhshX8sva-gLAZTlfNrxMtPy4ic-7BISCfGchwQ4Oh4L_ykb_v5amYjLF9r4TgcR288WXSxVbAepXzU52rpyx29214zJuhdTYijh16oxfVefUSdA0pBnPiaC1E6uvWltO1rfxr844jtt_krNdJGxwIjZJsNWq8e_rAD90zzbc3M6B4kRYLeZ7TU5sYGQKuqZC0SLh_Tkr5mRiy-nbzuCN69Hn4pK_HptNWs6pLQpEERi6-WNv6HbC8dcj_8s5ES2CP5ID9dyvSM_gGGx0Valadg55UMVM_US_aAt2tRs3E0Q7ksF0i7Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فرداشب اروپا در تب‌وتاب شب‌های سرنوشت‌ساز؛ جایی که غفلت، تاوانی به قیمت امتیاز دارد!
🔥
⚽️
فرداشب آرسنال با ضریب ۱.۲۱ و اینتر با ضریب ۱.۲۳ از نگاه ضرایب، مدعیان اصلی پیروزی هستن؛ بارسلونا هم با ضریب ۱.۲۶ شانس بالایی مقابل گالاتاسرای دارد. تقابل اتلتیکو مادرید و منچستریونایتد با ضرایب ۱.۹۱ و ۳.۶۴، از جذاب‌ترین بازی‌های فرداشبه؛ درحالیکه ویارئال و ناپولی با ضرایب نزدیک‌تر، رقابتی متعادل‌تر رو نشون می‌دهد. دیدار لانس و اسپورتینگ هم اختلاف ضرایب چندان زیاد ندارند و همین موضوع، این مسابقه رو به یکی از دیدارهای قابل‌توجه کنداکتور تبدیل خواهد کرد.
📌
مسابقات را فقط تماشا نکن؛ همین حالا وارد مینی‌اپ وینکوبت شو و با اولین شارژ خود و دریافت ۱۰٪ بونوس ویژه این دیدار‌هارو رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141380" target="_blank">📅 01:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141379">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/141379" target="_blank">📅 01:01 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141378">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">⭕️
⭕️
⭕️
هومن هدایتی مشاور حقوقی ورزشی:
⭕️
استقلال تخلف کرده و باید منتظر حکم سنگین باشه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SorkhTimes/141378" target="_blank">📅 00:59 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141377">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
با توجه به مصدومیت حسین کنعانی و دانیال ایری، زوج خط دفاعی پرسپولیس برابر صنعت نفت آبادان، محمدمهدی زارع و حسین ابرقویی هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141377" target="_blank">📅 00:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
آسانی که مصدوم بود و جای رزاقی نیا اومد تو زمین ...خود آسانی مصدوم شد و از بازی خارج شد
😎
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/141376" target="_blank">📅 23:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141375">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3890159133.mp4?token=ncHPsc9WOJD6750cVn8bf_81tFKO3wvE6P8k48aXc5YRr0sJzTMrXSd8qFEEWUCf2xQdxYqWfPA8N9iqm9dIEQKgmy3RY8m9WmzaeMIcTfOxrXb5mf43_5CPtPcPkrp5GxaORBQQEGPV66O19E5ehv_7C2YU_FUnxpk41UwW0Xy5ufXtDruU8_fNmpgqk0i9LWjWzvRM-CT_HlsBHF62PfhopDN916IRu3GjTLuXagtDk1uF5mQbR4TLdiy-gnWkLXEn8ReThhqG_A3usB3wwS8QKhHA_etlmHuYUZynxKRuqpb1FtHk6WZR5mS-0JigTaAoHvZSYWYejk4wQLeCsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3890159133.mp4?token=ncHPsc9WOJD6750cVn8bf_81tFKO3wvE6P8k48aXc5YRr0sJzTMrXSd8qFEEWUCf2xQdxYqWfPA8N9iqm9dIEQKgmy3RY8m9WmzaeMIcTfOxrXb5mf43_5CPtPcPkrp5GxaORBQQEGPV66O19E5ehv_7C2YU_FUnxpk41UwW0Xy5ufXtDruU8_fNmpgqk0i9LWjWzvRM-CT_HlsBHF62PfhopDN916IRu3GjTLuXagtDk1uF5mQbR4TLdiy-gnWkLXEn8ReThhqG_A3usB3wwS8QKhHA_etlmHuYUZynxKRuqpb1FtHk6WZR5mS-0JigTaAoHvZSYWYejk4wQLeCsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
🔥
گل شماره ۹۸۱ اسطوره رونالدو
❌
پ.ن فقط 19 گل فاصله تا آمار عجیب و غریب 1000 گل مانده
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/141375" target="_blank">📅 23:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141374">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">✖️
✖️
سیدحسین شریفی به عنوان مدیر صدور مجوز باشگاه پرسپولیس منصوب شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/141374" target="_blank">📅 23:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141373">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8WOAt3giGga4rtepGJDUNLDPnsX4ikOYlOpSpsZtazdzVnU9wEKliqEDcRgd0WPYiYKeiqOgcrmE-sNqIfQVPgw5sboalWGjg_jDn4oef2tF5zmQY8D8y4LXALt1Mov-AeNkBilryXhFxTHSPKBcun9p-QZl-cFeDXfOlm5Rc62mtmYFwPiclit5QxCtFOAt5Gep1mJ6C3TqBI6xNoyHFepthWtTF8W3DTveUIO1WDkcOuANTttz8GHgdMP8iEhJ4UnWA4QsFAVWJ5zFtIZKKNKGKpIqZSKTyOc1Tw0yxyscimxnqx9jNmomKUWlO14Eqwan5_BE_Qg3uRFHNcsaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
زوج خط حمله مقابل خیبر
🤝
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141373" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141372">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h96KnzrEhoAgJ_W9gN6RkGm6aRH_WG21hjy1y_T9Hn7lwXanT5sK5NXtYBAMM2xntTHiYpd2SVTzTDLYhc0PtkhxDKFMmrtl1lgYB5o3WRsMZZUKtQVFqXSUl01wJDJtac1nLSC_GITqn_gff1y3ystFyi5Tm1Y9lMZZpilSv8AohFEzGLTol4o7uCO8h7k957fwj0heTjEI0HZQd5sL6ofBxRZcQ7lfS9x0K2xeJRVs8Zi-9b21uTaHwUDTTCeUcPUg_idAbnbNMnlZPCOXVnSr7QP08stxghZqtMdQlZIkNko2lSOHDPhKIQbBVFtXaeqtiK5JHYYjzH13eZ0j1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
احمد کونِ دروازه‌بانه الغرافه واقعا اسمش برازندشه
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/141372" target="_blank">📅 23:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141371">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/SorkhTimes/141371" target="_blank">📅 23:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141370">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
الغرافه گل مساوی و به موقع به کیسه زد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141370" target="_blank">📅 23:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141369">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
لعنت به این آسانی ...ده دقیقه اس اومده تو ..گل کیسه رو زد .با ی شوت دیدنی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141369" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141368">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141368" target="_blank">📅 22:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141367">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cn4dcb3SqHHw4h2px-KXU7hDN4aFKQcpa0iqvbJUyicuwlXAbnOb6Y4QJKJxQLtMa05sn91u9sapqwY2Ut9EC46kh-ftjOEcfV7cP68R2rSJGPe8J1um6PSBoQCkvzqyWuWZsxI4CXmW9Hxb09Q2CVbJKI1Qn1m57ldkiFRuR3OG0tl0_VhL6b9HGCYSiA9ZSRs6b9LPL5n9kqJNb1dzTHMsLGrD2CX09dmDYk4_BqAths5dOzH01oX8k2ZtO95FLgz6Dlw2owZ8z64pWzaxQKSns407bJ6wTjW8HQZGyySJmMbZWdZGiuPP_9FHHhJv07ZbgVfEb_DnOEGHDM_alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پویا اسمی مقابل خیبر هم دقایقی بازی خواهد کرد/
فوتبالی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141367" target="_blank">📅 22:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141366">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
فوری/حوثی ها تهدید کردن اگه بازی النصر برگزار بشه ورزشگاه رو میزنن
❌
بزودی تمام ستارگان فوتبال از عربستان خارج میشوند
❌
العربیه:
❌
❌
نیرو های امنیتی بخاطر حمله حوثی ها سریعا رونالدو رو از ورزشگاه خارج و به یک جای امن منتقل کردن
🎗️
«سرخ تایمز» دریچه…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141366" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141365">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔵
💙
🔥
نماهای دیدنی از سوپرشوت یاسر‌آسانی روی گل اول کیسه به الغرافه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/141365" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141364">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
احتمالا بازی های تیم های بزرگ عربستانی هم مثل ایران به خاطر شرایط جنگی شرایط میزبانی و دیگه ندارع و تیم های عربی هم میزبانی خودش و باید به کشورهای ثالث ببره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/141364" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141363">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
بازی کیسه و الغرافه هم شروع شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141363" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141362">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/141362" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141361">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21384b098a.mp4?token=gwKwVU2ZGzr1DRDd769zUG7D479vsXehXYJOeiOljSEJPChT40TFob7D-CA0ZKQORXdcRBwFD6Eyp-vAcdlZWwgio-tfOpfIMcp3Ldhv-DIUauzO95y2FIpTA3OLXU8VhYZ3o0X5SVxXilQt0zSEPVANe1hssfEY7bNAg0cUWyyXm2oPbxnf6Wpjd2k0ifQw2ciuh-fCegOOAIdmTgptcpHre1GkUbbbLbBQGv6VD6lVsRS1hYx7S8kcNERkcORkGMcJgZIJNwO3bSmuIZptYt0ahIB4tf-3C1xtkRStKNOCilUa3B6iB6nXNDolCVXqAtq_4VHheCXguE2Rd-QmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21384b098a.mp4?token=gwKwVU2ZGzr1DRDd769zUG7D479vsXehXYJOeiOljSEJPChT40TFob7D-CA0ZKQORXdcRBwFD6Eyp-vAcdlZWwgio-tfOpfIMcp3Ldhv-DIUauzO95y2FIpTA3OLXU8VhYZ3o0X5SVxXilQt0zSEPVANe1hssfEY7bNAg0cUWyyXm2oPbxnf6Wpjd2k0ifQw2ciuh-fCegOOAIdmTgptcpHre1GkUbbbLbBQGv6VD6lVsRS1hYx7S8kcNERkcORkGMcJgZIJNwO3bSmuIZptYt0ahIB4tf-3C1xtkRStKNOCilUa3B6iB6nXNDolCVXqAtq_4VHheCXguE2Rd-QmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‏بازی النصر عربستان و نفتچی ازبکستان به دلیل حمله حوثی ها به ریاض متوقف شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141361" target="_blank">📅 22:21 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
واقعا ی بازی خواب آور و بی روح و سرد و مسخره ...بازی صفر صفر تمام شد ...
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/141360" target="_blank">📅 21:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141359">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
پایان نیمه اول |
🏆
هفته دوم لیگ نخبگان آسیا
🎙
تراکتور
0⃣
🆚
0⃣
الشمال
🇶🇦
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/141359" target="_blank">📅 21:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141358">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🚨
حجت کریمی شلنگ رو گرفت رو بیرانوند
😂
❌
❌
حجت کریمی: بیرانوند سال گذشته 100 درصد قراردادش رو دریافت کرده، در حالی که طبق مصوبه سازمان لیگ تراکتور می‌تونست 70 درصد قراردادها رو پرداخت کنه. امسال هم بیرانوند 35 درصد گرفته، در حالی که بقیه بازیکنا 8 درصد دریافت…</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/141358" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141357">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p69EHubEBQUZ-js8ECycKa7Rq4jnhE5k6YWG1Vt8jLRgDH5f3pZ_4pwCN63WiKQ6eTEZWZMByJyOdbZMqOa2V925h3328b-qoPm1rJCZI8k8xtn7wO_ufVrgWRQyurwIzNZnCN6tSwJt-b3-j8IC2493GHLPxYpVH4qwQM7TZhEMdyxcNEvv8mfdbJVR_JimJmKcOJwpjjZKK7qR0rWtnv2yO2ZvJv2Ee2N744VPr7KK46uWm9bMx0fuG7ZgpoU2i0Sj_ey-_fb0902Tf_dmf9-wQ3jEnMsFG72Ap78APwJjKwzDHtRTiJSYww5O7mh_pLlHciqdpM116DOIiBCuLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
تصاویری از تمرین امروز تیم پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/141357" target="_blank">📅 21:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141356">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
سرعت، برگ برنده پرسپولیس تارتار
🚨
فرمول تارتار، ضدحمله‌های سریع و برق‌آساست؛ پرسپولیس با چند پاس سریع از دفاع به حمله می‌رسد و حریف را غافلگیر می‌کند. البته تیم‌هایی که دفاع فشرده داشته باشن، می‌تواند این تاکتیک را سخت‌تر کند
🎗️
«سرخ تایمز» دریچه ای تازه…</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/141356" target="_blank">📅 20:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141355">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
فوری؛ کد سربازی علیرضا بیرانوند فقط برای فجر  صادر شده و راهی این تیم می‌شود. او به دلیل تأهل و داشتن دو فرزند کسری خدمت خواهد خورد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SorkhTimes/141355" target="_blank">📅 20:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141354">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=MxnnHvtjh6r11fpcRc3Ufj0TfEsOSW2qroSQ_Sw2wbkE21S8VuNhVfwjL3LOOkt7kSTQbe1eKYJR8F_g5DAaCETRzn63IoKpUueMtV-TJLMPu99XSz7VSpqttdCdcxt7qgHOu6FO4yGUjDg_FjO53vaNWY9QschtMg_SwMh9bcjgE8MXbD9oBrh_QQSNc0uWNXimiSip7R2k-EI_dC7ZXYVyh3TrauBNs7kvv_TANF_DAwNl7VeAofLqI7XDbofS-7br5fOD2pP-HpQF1C--hH5GLnIN9TVvhoiqpboElGS_wzLt8vZ9zBmTm20tkVmO3qBsZSoxRW3b_GPY0VGKZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f780d2f1fd.mp4?token=MxnnHvtjh6r11fpcRc3Ufj0TfEsOSW2qroSQ_Sw2wbkE21S8VuNhVfwjL3LOOkt7kSTQbe1eKYJR8F_g5DAaCETRzn63IoKpUueMtV-TJLMPu99XSz7VSpqttdCdcxt7qgHOu6FO4yGUjDg_FjO53vaNWY9QschtMg_SwMh9bcjgE8MXbD9oBrh_QQSNc0uWNXimiSip7R2k-EI_dC7ZXYVyh3TrauBNs7kvv_TANF_DAwNl7VeAofLqI7XDbofS-7br5fOD2pP-HpQF1C--hH5GLnIN9TVvhoiqpboElGS_wzLt8vZ9zBmTm20tkVmO3qBsZSoxRW3b_GPY0VGKZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
پیمان حدادی، مدیرعامل باشگاه پرسپولیس، به مناسبت روز دختر در محل تمرین تیم فوتبال بانوان حضور یافت و با اهدای گل و هدیه به اعضای تیم، این روز را به دختران پرسپولیس تبریک گفت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/141354" target="_blank">📅 20:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
بغداد بونجاح و ریاض محرز، دو ستاره الشمال در بازی امشب که شروع شده مقابل تراکتور غایب هستند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SorkhTimes/141353" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141352">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQhggCTAvmxs3BpzIU_Hnl_UADC7obuoRJwx-QM3moEPHkrymDjpr5ijPOTZmJx3R5Q3rxLCkJhf0FLN2Ie_Reo2GuYUoe5y5j1HslvSbcZFXsjn2k4LM_8tYMjt-7aWmVkiv4DOS8mT4jnAwYNxUju2nqKNa7of5uNqdpHofxHrkLHU-hiXof7LEF5K4hGd4tCStFPkJkVbyeJ7GzPNfTA4hgF2NGue7OXkPg9aamietH2KVTEzm77B3-dQerLLBgaFIin14LV6qUo3L8ANAD5buCJCy3EiclAQafOxhVSP4STHOk9g9eNmci0NUhXaZ936ctwCMmWj0HQzPaauZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
Al Gharafa
🆚
🔵
Esteghlal
⏰
Tonight 21:45
🏟
Thani Bin Jassim
🟣
الغرافه در ۸ بازی این فصل ۱۷ گل دریافت کرده؛ نقطه‌ضعفی که استقلال می‌تواند با حملات سریع از آن استفاده کند. استقلال با روند بدون شکست در ۹ بازی اخیر و برد ۳–۰ مقابل السد، از ثبات دفاعی و اعتمادبه‌نفس خوبی برخوردار است. با توجه به ضعف دفاعی الغرافه، گل‌زنی استقلال دور از انتظار نیست.
🎁
بونوس ویژه اولین شارژ:
فقط با ثبت یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و سپس به موجودی اصلی حسابت اضافه کنی.
🔗
همین حالا وارد مینی‌اپ رسمی وینکوبت شو و فرصت رو از دست نده و این دیدار جذاب رو پیش‌بینی کن:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/141352" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141351">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✔️
✔️
علی پروین: فوتبال این روزهای پرسپولیس من را یاد دهه ۶۰ می‌اندازد، این تیم قهرمان خواهد شد؛  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/141351" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141350">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
| ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/141350" target="_blank">📅 19:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141349">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">✖️
✖️
✖️
✖️
با توجه به درخشش مهدی تیکدری در پست دفاع چپ، پرسپولیس احتمالا بازیکنی در این پست جذب نمیکنه/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/141349" target="_blank">📅 19:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141348">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🟣
تراکتور در مسیر قدرت‌نمایی؛ الشمال آماده غافلگیری!
🔥
⚡️
[ تراکتور
🔴
🆚
🔴
الشمال ]
⚽️
تراکتور با وجود شکست در بازی نخست آسیایی، در ۹ بازی اخیرش ۵ برد و ۲ مساوی داشته و از نظر دفاعی آمار قابل‌قبولی ثبت کرده است. الشمال با میانگین ۲.۲۲ گل زده در هر بازی، خط…</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/141348" target="_blank">📅 19:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141347">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری از آنا
🔹
باکیچ به دلایل فنی از لیست پرسپولیس کنار گذاشته شده و مصدومیتش کذب محضه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/141347" target="_blank">📅 19:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141346">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V30Xu9egivkVn9NDyl6Cg80QQM4MrttqM8APCYXIs0FA9QHSlsTWD98Y99E3grrZk8Y8Jf7zokabqEsSIYO_dfKANJj0zqvyzJ5VBpHkunkMBtpBgE4TuitQ5_5Kh_VMyaP6yUFCf2jEjxyY_n1EM3tOBxVzEKr6RQzZKVbI-m7HApSqvJp_0G4_3E18a4S76Yk_OswQMUNyHgVi2jhWFhe-3Bl0JR4LQMT8gUZ_cVmFc7opDa1vCbl3fBYyKWgSDVvd40XkNyWymC55rTvZD-dwkfFTDpernIWW_RB03lU_OOJAcBEEUrQtC1dfICo4f19Y4rh1jfnNt5RbDmPuqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گویا یحیی گل‌محمدی در یک قدمی سرمربیگری تیم ملی امید قرار گرفته است. فقط کاش یحیای عزیز حواسش باشد همه بازیکنان این تیم باید زیر 23 سال باشند. این دیگر اجباری است!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141346" target="_blank">📅 19:28 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141345">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss_LeNRhlpQAVo4uhCmCI5BgoBETdxe0mCQzkLTsfL8QkbpYsTARb-UF3vtQ5HaSl4tTPGB5QAgmwsGQ0P7zGbf8nEvyXp_rX_mk-3EponIQMh1mYSpW1H4UmtWNctJz3DtLdis_LDkCOTa6Ft1CdZF6aHA-8Bzz9xr9xyhQAiIPXWAz7eHxLT-BFJo9gYe4vqHuOYjGWVr1advnDmHxW3cpHFQj7_njyCVOdvBe440b77bQQDVPv9o8yc4W0yJodCS7mFxhdbix5DTjOl4dGuALfL3l60kJv5uOJfUs6sAXdtmLcSG9J5b4luP8-6hiIY-qjAUpSoeVl662MrAO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇮🇷
مهدی‌تارتار به مدیران پرسپولیس اعلام کرده که اورونوف غیرقابل فروش است و این بازیکن باید در تیم بماند. تارتار معتقد است که با وجود سن و سال بیفوما، حضور اورونوف جوان در ترکیب تیم ضروری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SorkhTimes/141345" target="_blank">📅 19:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PoMHXC3k6l3D3-SqB9PGbiSl8IqaDod1nf0_IhEnj06FzGe6wFn8fmKOQr2ASwopMWZA67QtpsWvPeo_y5zY9j0NMEUV8iiCK2vTwFQpBCJMflOncXMemCIx5fh-HTmkXvOT3_tq9KuKe3KRS1FOGCJ_0QVUMjiU6RSue3c3WTTpoHTwgY4vPjFLMP364c6YX-48kQot1UUbEwjNL1Tml1L18mY2EMwetVKO2SneYzT8vHyXlXFy7FjbONgYh6B8pqslcU_73JvCVTFIJVN4abx2r28ISgpziPqSQFPvwZTYRduuwatXGVin_AMP1R_KwpYhvj_NqTVIwIK-yliXGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🆔
⭕️
⭕️
|
ورزش‌سه:
🔴
❤️
پیمان حدادی در پرسپولیس ماندگار خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SorkhTimes/141344" target="_blank">📅 16:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141343">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
⭕️
⭕️
⭕️
ویدئویی که کاملا توضیح میده چطور یاسر آسانی واقعا فسخ کرده و پرسپولیس باید دنبال حقش باشه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141343" target="_blank">📅 16:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141342">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
رد درخواست پزشکی بیرانوند  اول آبان؛ اعزام به خدمت سربازی
🚨
🚨
ماجرای سربازی علیرضا بیرانوند سرانجام به پایان خود رسید و این دروازه‌بان باید چند روز دیگر عازم خدمت شود. دو درخواست پزشکی بیرانوند در این زمینه مورد بررسی قرار گرفت و‌ هر دو رد شد.
🚨
🚨
آسیب…</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SorkhTimes/141342" target="_blank">📅 15:34 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🚨
خسته نباشی آقای تارتار
🚨
🚨
🚨
با وجود انتقادهای ابتدای فصل، تارتار تونسته پرسپولیس رو به شرایط خوبی برسونه؛ از اعتماد به جوون ۱۷ ساله‌ای مثل پویا اسمی تا احیای بیفوما و خدابنده‌لو و مدیریت شرایط اورونوف. حالا سرخ‌ها با یک بازی کمتر، فقط یک امتیاز با صدر…</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/141341" target="_blank">📅 14:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141340">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⭕️
⭕️
⭕️
⭕️
قضیه پرونده آسیب کتف، پرونده اعصاب و روان و خالکوبی بیرانوند در کمیسیون پزشکی پذیرفته نشد و به صورت قطعی از اول آبان سرباز محسوب میشود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/SorkhTimes/141340" target="_blank">📅 14:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141339">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔄
🔄
هوشنگ نصیرزاده: پرسپولیس با شکایت از آسانی به CAS وقت خود را تلف می‌کند هیچ سندی علیه آسانی وجود ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SorkhTimes/141339" target="_blank">📅 14:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141338">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❌
❌
❌
اول آبان؛ زمان برگزاری دادگاه پرسپولیس و بیرانوند در CAS
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/141338" target="_blank">📅 14:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLT6S3sz8CNvwiTMXo7pZuH0wRHOiiUwRWe7R16QZ0No7_-Xz2GKkqRj-zTa74DrtOMAdqzl2yk8tbJaWnRbgZFFS0b-n0xOcdbQKYcX9dOU9EPVWVKHmP2fE4oD4zHP-Uy9AC5uDjeuywvcwPHyAcKcFOGX89htJKdki4xZCYXeavACb-fXRsv3iYl8yGCdDcOWQKIXBdcEVAKteIkQQoLG8SYE2ubG8SsPt6RSVZ2wslCbI0oy7z5v-73fyF5SaWOH_IJOpM5qInDZwuRa3PxCiKsPLh1B5Qv9VjBoBfIG46mIvxCiTrMYy0CTygjj5sVOnpWchLF9Jw9dEE2u8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
استقلال در دوحه؛ جدال آبی‌ها با الغرافه برای یک شب سرنوشت‌ساز!
🔥
⚡️
[
الغرافه
🟡
🆚
🔵
استقلال
]
⚽️
الغرافه در ۵ بازی اخیر ۸ گل زده اما ۱۲ گل دریافت کرده؛ استقلال با ثبت ۶ گل زده و فقط ۲ گل خورده، آمار دفاعی بهتری دارد. استقلال در ۴ بازی خارج از خانه فصل، هنوز شکست نخورده و فقط یک گل دریافت کرده؛ نکته‌ای مهم مقابل خط حمله الغرافه.
سناریوی محتمل: بازی نزدیک و کم‌گل با برتری نسبی استقلال در فاز دفاعی؛ الغرافه با استفاده از میزبانی فشار می‌آورد، اما استقلال روی ضدحملات شانس گل‌زنی دارد.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو با بونوس ویژه ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/141337" target="_blank">📅 14:07 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
بیرانوند به کمیسیون پزشکی رفت؛ در انتظار اعلام وضعیت نهایی
🖍
علیرضا بیرانوند، دروازه‌بان تراکتور، روز گذشته در نخستین جلسه کمیسیون پزشکی در تبریز حاضر شد.
🖍
بیرانوند که به دلیل خالکوبی به کمیسیون پزشکی اعصاب و روان نظام پزشکی ارجاع شده، همچنین برای بررسی…</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SorkhTimes/141336" target="_blank">📅 12:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141335">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
باشگاه تراکتور به صورت رسمی به علیرضا بیرانوند اعلام کرده حق حضور در تمرینات بزرگسالان را هم ندارد و باید به تمرینات تیم امید برود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/141335" target="_blank">📅 12:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-141334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8bNUk5vinVQqwYo2p0XjuwKG4H9Jh4H85tyZneFe2Z0ABPUPyzVxFT9drcLYkU4RAxRQ6ngDX_pnwMTmVDYHRPgLRh5nwhUG4E35LDiz_hYTnrA5tZASRrQ_yYGq5kfe0TZZCrh1epso55_avw5u3wzN_dRJKnF_u5zsAr5mrsE97m5iQjhlPFNKr_4sucDWUIy2r9WE5uuqWW3B3E-UHRq-mw1OYNVLJbTibyT4Z1ypAS5Y4XdEskhMOvIAY0HpR7mmTDRUwJGTecPdMEQoKdW4HrR4ra-pUVdAsJ9EIY0a13euSVT2GgbsKiSf4267dLk9MM8Sk1saRR6p2IJ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پوریا لطیفی فر در بازی با نفت نتواست عملکرد خوبی داشته باشد و مقابل خیبر نیمکت نشین خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/141334" target="_blank">📅 11:52 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
