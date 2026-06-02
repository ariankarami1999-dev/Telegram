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
<img src="https://cdn4.telesco.pe/file/KGLweOkIemECS-0TQp20LXRBnaiAcZU23X-6SZkxkslwiU_Tfjw3StoDzbRdHcHxxGueun7KLrT2Y-HFVp8m0edc8-HcZpPzu53UYWooddtKyhTJ3i0uL9zG4pQ6t7Ina2OaAszvdklbqHYAqzfOD_EsuXzgAyBEghe-6WFPDX4eteoW_TQXs--w8F3ZCTo27diQoGm1W4-5cykpbcxZVZw-5UuFUFB8MntJeKWzQloj-zKV9Q7M3eHygbW4XrZ3-gMpeTq-vdHkgY8Su9h0RGvfRhW1dVBRdf8w25cPNEsurX3k3UcVlBmfr0zC3zPFbhMp5UdLsUl6-n88HVVsoQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 285K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 21:30:46</div>
<hr>

<div class="tg-post" id="msg-13281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b925d659.mp4?token=UZ_a4h0v53g5DG73ZUvPP00chJ0XkI7AicPOHWiMmUxy7-8GiSEww4uzPNB_xI2f7cd_Hr2B3Yp2Ix6jpHWCRjFYjlaOvtqqynyZKfP89ijVIRjMhHaaUyFfi15Qj3R_r_S_hI6Hxuk9YjUUmxC281NvxKmRZ_0L-ShAdGiJH-Rg9dMT-MLwZnUBUB875JV72xG3pjJZaX_42ZGq3uQNbn1vdH9nkbgWnNaEvSRkk9K5fVNZDSaAxOwF3HMjkYSYoGcC2Ktz1qpAKuO45iF55u2T6NTWiy9nrn4Z2d022zHBPDkb9bBCSZ3_3thrP6rrkYMf86AnRdfCyzBCdpC1Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b925d659.mp4?token=UZ_a4h0v53g5DG73ZUvPP00chJ0XkI7AicPOHWiMmUxy7-8GiSEww4uzPNB_xI2f7cd_Hr2B3Yp2Ix6jpHWCRjFYjlaOvtqqynyZKfP89ijVIRjMhHaaUyFfi15Qj3R_r_S_hI6Hxuk9YjUUmxC281NvxKmRZ_0L-ShAdGiJH-Rg9dMT-MLwZnUBUB875JV72xG3pjJZaX_42ZGq3uQNbn1vdH9nkbgWnNaEvSRkk9K5fVNZDSaAxOwF3HMjkYSYoGcC2Ktz1qpAKuO45iF55u2T6NTWiy9nrn4Z2d022zHBPDkb9bBCSZ3_3thrP6rrkYMf86AnRdfCyzBCdpC1Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو: «موساد همچنان در خط مقدم نیزه در نبرد ما علیه تجاوز ایران باقی خواهد ماند.
ما اجازه نخواهیم داد رژیم ایران چرخ تاریخ را به عقب برگرداند. ما اجازه نخواهیم داد به سلاح هسته‌ای دست پیدا کند. ما اجازه نخواهیم داد موجودیت ما را تهدید کند.
این رژیم محکوم به زوال که پایانش فرا خواهد رسید و ما به رسیدن آن به این سرنوشت کمک خواهیم کرد.
این رژیم دیگر باز نخواهد گشت تا ما را با بمب‌های هسته‌ای و هزاران موشک بالستیک مرگبار تهدید کند.
این دستور من است و این مأموریت شماست، رومن.»
@withyashar</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/withyashar/13281" target="_blank">📅 21:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13280">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ربطی نداره ناو لینکلن ، بوش و ناو آبی خاکی‌ تریپلی و کلی‌ ناوشکن هستند و کافیه!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/withyashar/13280" target="_blank">📅 20:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13279">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ادعای شبکه ۱۲ اسرائیل : دستور تخلیه ضاحیه جنوبی بخشی از هماهنگی نتانیاهو و ترامپ برای فشار به ایران تو مذاکرات بوده و نه برای حمله مستقیم به ضاحیه
@withyashar</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/withyashar/13279" target="_blank">📅 20:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13278">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYPB2Nc-NtZm8vgXz1Q63X7IqQhF8fTiOpkxBcsjEcRnQ0oOR_50uBK4lQdn2FibUvUjOi8koHkD-NSMN87UNv0F2dYlfa5DS6do55iPBbqQZZCbWIrbaa1jJfkNvlezRN6ivIeWito24RRz3IukhNiLCmJIqWOufFaKpC4iqJ4l-R-Ezs3gH-f-AASmfqcLV9tJejMni39WeDHY7EiBJSTGvhAHwEmPkQqq1wtCVUJZcsXd2mVRMWjCwgc-M6mHJaCJgOebDSdFK9tIDK3MF4oJ3oGNNsBeZsCDf7nRmUQhFPHDEkUDKI9BIs-9Pqy7vIpqGyEvepkPDGP2uL5OzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث :«گزارش‌های فیک‌نیوز که می‌گویند جمهوری اسلامی ایران و ایالات متحده آمریکا چند روز است با هم صحبت نمی‌کنند، کاملاً نادرست و اشتباه است.
گفت‌وگوها میان ما به‌صورت پیوسته ادامه داشته است؛ از جمله چهار روز پیش، سه روز پیش، دو روز پیش، یک روز پیش و امروز.
این گفت‌وگوها به کجا می‌رسد، کسی نمی‌داند؛ اما همان‌طور که به ایران گفتم: “وقت آن رسیده، به هر شکل ممکن، به یک توافق برسید. شما ۴۷ سال است که این کار را ادامه داده‌اید و دیگر نمی‌توان اجازه داد ادامه پیدا کند!”
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/withyashar/13278" target="_blank">📅 20:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13277">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b6ab4e43.mp4?token=Jl2-boGcldtZvA24avJ2JcoL4CmMqJvN_H4LE9a8dB4dRBROvckkCiGAeH51oGZq5VQIVl97cPwSSCTUuL1hK7HrX68nb7nbsUn1elFOZhLSe6Z8zG5OJ7X6Z02FbRDY2VoqA5MRX7aLxTNuwi2AcCh2bdaBJe_Cgkm5xEeRqoguALdkrZFQol4PuA8_ZIJQddwibn7Tc5HZRatq_xoNrX6vsn9CETTICuPw8fnpDJGSdVXSr3T9gKlqAjSL2F7UR9FxWggUH3FZa6eGXKlh-AJUo8uu2zbV-gWr2j6kbN4N0e5W1CjaQqlMjBOf0eon6BAkGmfSdZpaK-dAvGu7xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b6ab4e43.mp4?token=Jl2-boGcldtZvA24avJ2JcoL4CmMqJvN_H4LE9a8dB4dRBROvckkCiGAeH51oGZq5VQIVl97cPwSSCTUuL1hK7HrX68nb7nbsUn1elFOZhLSe6Z8zG5OJ7X6Z02FbRDY2VoqA5MRX7aLxTNuwi2AcCh2bdaBJe_Cgkm5xEeRqoguALdkrZFQol4PuA8_ZIJQddwibn7Tc5HZRatq_xoNrX6vsn9CETTICuPw8fnpDJGSdVXSr3T9gKlqAjSL2F7UR9FxWggUH3FZa6eGXKlh-AJUo8uu2zbV-gWr2j6kbN4N0e5W1CjaQqlMjBOf0eon6BAkGmfSdZpaK-dAvGu7xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو ادعای مسلح کردن مخالفین حکومت ایران توسط دولت آمریکا را رد کرد
:
«من از هیچ برنامه‌ای برای مسلح کردن غیرنظامیان در ایران برای سرنگونی دولتشان آگاه نیستم.
منظورم این است که ممکن است کشورهای دیگری این کار را انجام دهند، یا گروه‌های دیگری این کار را انجام دهند، اما مطمئناً دولت ایالات متحده این کار را نمی‌کند.»
@withyashar</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/withyashar/13277" target="_blank">📅 20:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13276">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الان کجاست احمدی نژاد</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/withyashar/13276" target="_blank">📅 20:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13275">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGYM</strong></div>
<div class="tg-text">الان کجاست احمدی نژاد</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/withyashar/13275" target="_blank">📅 20:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13274">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmkfW6y4FsrUgeEwKbbs-cwuRkTNFviVckGdWo5d2SW4yY9QSzgTHOrXVSEy0rIBqFZLk4iDDYYURk2OFfsAOopyt2HA2sD5AB9R7Y2Hm52So9KLwcA3XgBzIsvDvT9PwZBvgOTRaNNT1bbhrku_QK2II7H8MgGlxmnWYHtgEILJFZLeHJhgSI1X1BaCefxaswH2kjzrtneaohy7LwhQV0RVEX80WYetxJjxVAjusc6qoQYudTuyfbBp3EstGjaumEq1SWqTS6nJNzx6ACxY76VGdA_aoZRKG0H6BrPW0db8vWkzeSKALiOCCUY6apzWRq1F8XhHpf_Xm6c16U6oew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ال احمدی نژاد السیسی
🥴
پس بگو این مدت برای چی انقدر ‌رفت بوتاکس کرد و به خودش رسید، قیافه درست کرد.
@withyashar</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/withyashar/13274" target="_blank">📅 20:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13273">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f41232db.mp4?token=JkJsdK8ZPrcUCO1meZ8bpMn2IlKm-8uMgXi6o4WwCHHBq3jaItY_1rf1CuNYjvx9xot0HHI02-kGtubDiDgORoNpP5QQOmxGGyPomoTllp7M2L4OfOnfs3VasXYwFfYuoCUsn87GMOX-SaftUwfVsBMjsYe80tnb1Cd1JzjiUaEPzT4RKHdyjid5iy4tD1eTJwBu9i7jCdhQ40mkhqo_qXFYfrU18jzAW1m9a37s5dicT2sOCHIf4Qfkap6xaOtVaolxvc3XFN7s3E7aBHVYe__TWYg-bxE_fFl-wKhtx1ujo2xPWEjUAd88OxuMqTa8AWP4HsG1nWsSnW92eEK8ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f41232db.mp4?token=JkJsdK8ZPrcUCO1meZ8bpMn2IlKm-8uMgXi6o4WwCHHBq3jaItY_1rf1CuNYjvx9xot0HHI02-kGtubDiDgORoNpP5QQOmxGGyPomoTllp7M2L4OfOnfs3VasXYwFfYuoCUsn87GMOX-SaftUwfVsBMjsYe80tnb1Cd1JzjiUaEPzT4RKHdyjid5iy4tD1eTJwBu9i7jCdhQ40mkhqo_qXFYfrU18jzAW1m9a37s5dicT2sOCHIf4Qfkap6xaOtVaolxvc3XFN7s3E7aBHVYe__TWYg-bxE_fFl-wKhtx1ujo2xPWEjUAd88OxuMqTa8AWP4HsG1nWsSnW92eEK8ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت های
تامر هایمن
رئیس سابق
سازمان اطلاعات نظامی اسرائیل (AMAN):
عملیات سری ترامپ و کردها و احمدی‌نژاد !
@withyashar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/withyashar/13273" target="_blank">📅 19:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دایرکتاتون انقدر ماه بود که الان میرم اتاق جنگ
💻</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/withyashar/13272" target="_blank">📅 18:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13271">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e0a60d360.mp4?token=Bhut3vGH6_Mdjwl7M7C38GjB2_4LDE0521hpILZdhjXXplTLdtutn697noGH64fSpKWAs38BLBuGnpDIeDoW4Y-caKNMozIhc0MvfxfLpNq12B9cfidO-Q9SRQpjjkLiWwZVNJ1pM8QXHSnyPLPgAWYdPVRDk5-7z_jDGk-epqcIFb-cDaCxeA6yhM0YTw_tfWeaRLGTOwYYb7cMqiu37BaDFb0OvTzMDpjFVeLnKCxDlZzSOzaGGB8z8dVySR8cKAQQRv7GkNml6Kn9QbKrpQQT7g95MiSPfOl6Xe0wcLnT_5LKf7X2isp1mu7e4Ia5Rqlbvt0-Mkt98_D9gTCxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e0a60d360.mp4?token=Bhut3vGH6_Mdjwl7M7C38GjB2_4LDE0521hpILZdhjXXplTLdtutn697noGH64fSpKWAs38BLBuGnpDIeDoW4Y-caKNMozIhc0MvfxfLpNq12B9cfidO-Q9SRQpjjkLiWwZVNJ1pM8QXHSnyPLPgAWYdPVRDk5-7z_jDGk-epqcIFb-cDaCxeA6yhM0YTw_tfWeaRLGTOwYYb7cMqiu37BaDFb0OvTzMDpjFVeLnKCxDlZzSOzaGGB8z8dVySR8cKAQQRv7GkNml6Kn9QbKrpQQT7g95MiSPfOl6Xe0wcLnT_5LKf7X2isp1mu7e4Ia5Rqlbvt0-Mkt98_D9gTCxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران:
«ما در حال مذاکره هستیم و می‌گویم مذاکره، چون مذاکره با ایران شبیه مذاکره با سوئیس نیست، درست است؟ کاملاً متفاوت است. متأسفانه این مذاکرات نیازمند استفاده از واسطه‌هاست.
اما اکنون با چشم‌اندازی روبه‌رو هستیم که ممکن است امروز، فردا یا هفته آینده به نتیجه برسد؛ اینکه برای نخستین بار، دست‌کم تا جایی که من به خاطر دارم، ایران پذیرفته است درباره بخش‌هایی از برنامه هسته‌ای خود مذاکره کند؛ موضوعاتی که تنها یک ماه پیش، یا حتی یک سال پیش، نه‌تنها حاضر به مذاکره درباره آن‌ها نبود، بلکه اساساً از مطرح کردنشان نیز خودداری می‌کرد.»
@withyashar</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/withyashar/13271" target="_blank">📅 18:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13270">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وزیر امور خارجه آمریکا , روبیو : در حال حاضر نیروی دریایی ایران وجود ندارد، بلکه گروهی از قایق‌های تندرو حامل رگبار هستند.
اگر ایران بر بستن تنگه‌ها اصرار کند، ما آنها را برایشان خواهیم بست، و این کاری است که ما از طریق محاصره مؤثر انجام داده‌ایم.
امیدواریم با ایران به توافقی برسیم که منجر به بازگشایی تنگه‌ها شود.
@withyashar</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/withyashar/13270" target="_blank">📅 18:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13268">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یک منبع آگاه : خلبان هواپیمای اف-۱۵ آمریکایی که در طول جنگ بر فراز ایران سرنگون شد، همان خلبانی است که هواپیمایش بر فراز کویت در اثر اشتباه پدافند کویت نیز سقوط کرده بود
@withyashar</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/withyashar/13268" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13267">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ربطی نداره ناو لینکلن ، بوش و ناو آبی خاکی‌ تریپلی و کلی‌ ناوشکن هستند و کافیه!</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/withyashar/13267" target="_blank">📅 17:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13266">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAli Hb</strong></div>
<div class="tg-text">سلام ی سوال
اگر امریکا میخواد جنگ کنه چرا پس ناو جرالد فورد و باکسر برگردوند؟
این خودش نشونه این نیست که جنگی درکار نیست</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/13266" target="_blank">📅 17:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13265">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صبح بخیر من دقیقا ۲ هفته پیش دیدم و گفتم برگشت ! تازه رسانه ها فهمیدن در این پست مستند شده !
https://www.instagram.com/reel/DYiHl04xutP/?igsh=MWZhNHllczYzNGtvaA==</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/13265" target="_blank">📅 17:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13264">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromkiarash</strong></div>
<div class="tg-text">تروخدا بگو ناو باکسر میگن برگشته دروغه؟</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/withyashar/13264" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13263">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یک منبع آگاه به فارس: درحال حاضر تبادل پیامی با آمریکا انجام نمی‌شود
تبادل پیام بین ایران و آمریکا برای آنچه دست‌یابی به یادداشت تفاهم اولیه بین تهران و واشنگتن خوانده می‌شود، دست‌کم چند روز است که متوقف شده.  درحالی‌که دیشب ترامپ مدعی شده بود که گفت‌وگوها با ایران با سرعت بالایی در جریان است، این منبع آگاه تصریح کرد که آخرین پیام جمهوری به فارس اسلامی ایران به واشنگتن، پیامی آشکار در خصوص لبنان بود که بازتاب گستردۀ بین‌المللی یافت.
@withyashar</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/withyashar/13263" target="_blank">📅 17:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee6b42048d.mp4?token=cHMM3CXyjXAk2Bq_e1RKvEA235iFs6LfyuK42IuYCAs_ieSrH6E3YkKkRdJdu_Iq286NcTcINRqBRAC8g64iXkYv-RYifZWIAdBkIhoiwKCMUDm18SnJpISARq31KaQyXdjkCVG-Udz0kBuInBfatGCKj60OdJG2--Yu_kgPM57UEQRmSVUmjXu3ueJEOzGKrQSC4ysqDdMs4tFMwal3_jzo1__uPyOx7yiY9SJZFxYDGtxJxmSNofmtss8oV85lDSHPYACGIP1VYG6Rt23jc1FkizJy0U0x9W7STuTfK6N85oQv98eFv9W-6oNF5M8zeFtnocaZGWjiq8C4EPQYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee6b42048d.mp4?token=cHMM3CXyjXAk2Bq_e1RKvEA235iFs6LfyuK42IuYCAs_ieSrH6E3YkKkRdJdu_Iq286NcTcINRqBRAC8g64iXkYv-RYifZWIAdBkIhoiwKCMUDm18SnJpISARq31KaQyXdjkCVG-Udz0kBuInBfatGCKj60OdJG2--Yu_kgPM57UEQRmSVUmjXu3ueJEOzGKrQSC4ysqDdMs4tFMwal3_jzo1__uPyOx7yiY9SJZFxYDGtxJxmSNofmtss8oV85lDSHPYACGIP1VYG6Rt23jc1FkizJy0U0x9W7STuTfK6N85oQv98eFv9W-6oNF5M8zeFtnocaZGWjiq8C4EPQYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آهنگ تابستون کوتاه ورژن عرزشی
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/13262" target="_blank">📅 16:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">واشنگتن‌پست: مذاکرات ایران و آمریکا در بن‌بست است
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/13261" target="_blank">📅 15:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک افسر ارشد ایرانی به CBS گفت که جنگ تازه با آمریکا به نظر «اجتناب‌ناپذیر» می‌آید چون اسرائیل و حزب‌الله به درگیری ادامه می‌دهند
@withyashar</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/withyashar/13260" target="_blank">📅 15:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">جناب شاهزاده رضا پهلوی گرامی،   پدر ، این پیام، جمع‌بندی دیدگاه‌ها و پیشنهادهای گروهی از ایرانیان داخل و خارج کشور با هدف تقویت انسجام ملی و ایجاد مسیر عملی برای دوران پیش از گذار است.  عناوین چکیده از هزاران پیغام مردمی به‌صورت خلاصه:  * ضرورت ایجاد ساختار…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/13259" target="_blank">📅 15:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جان بولتون :
ایران باور دارد که می‌تواند از ترامپ بیشتر دوام بیاورد، یعنی صبرش بیشتر از اوست
، چون ترامپ شدیدا نیاز دارد که قیمت نفت را پایین بیاورد.
وقتی کسی سه بار بگوید «برایم مهم نیست»، شاید یعنی واقعاً برایش مهم است.
اگر ترامپ نگران نبود، با نتانیاهو تماس نمی‌گرفت تا در لبنان آتش‌بس برقرار کند.
@withyashar</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/withyashar/13258" target="_blank">📅 15:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چرا کامنت فقط 3k لایک خورده؟از کانال 280 هزار نفری انتظار بیشتری هست بخدا،به بچه ها بگو یه تکونی بخورن یه خودی نشون بدیم</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/13257" target="_blank">📅 14:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSohrab</strong></div>
<div class="tg-text">چرا کامنت فقط 3k لایک خورده؟از کانال 280 هزار نفری انتظار بیشتری هست بخدا،به بچه ها بگو یه تکونی بخورن یه خودی نشون بدیم</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/withyashar/13256" target="_blank">📅 14:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شبکه اجتماعی لینکدین رفع فیلتر شد
شبکه اجتماعی لینکدین پس از بازگشایی تدریجی اینترنت بین‌الملل، بدون نیاز به فیلترشکن در دسترس کاربران ایرانی قرار گرفت.
صفحه من در لینکدین هم داشته باشید :
https://linkedin.com/in/seyed-yashar-tavakolian-a26a61188</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/13255" target="_blank">📅 14:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وال استریت ژورنال: ایالات متحده بیش از پیش رویکرد بی‌طرفانه عمان در قبال تهران را خصمانه تلقی می‌کند و این کشور را تحت فشار قرار داده است تا با انتخاب یک طرف، روابط دیپلماتیک خود با ایران را قطع کند.
@withyashar</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/13254" target="_blank">📅 14:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/13253" target="_blank">📅 14:16 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">زیر پست صفحه دوم شاهزاده رضا پهلوی و بانو نور پهلوی کامنت مورد نظر را گذاشتم. نیاز به همیاری شما داریم برای این مرحله از فراخوان. لطفاً کارهای اداری را انجام دهید، طبق برنامه.  https://www.instagram.com/reel/DZFAJOWRays/?igsh=NmVldnV2aW1jaHE3</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/withyashar/13252" target="_blank">📅 14:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13251">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/withyashar/13251" target="_blank">📅 13:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برادر … کامنتت پیدا نمیکنم راهی نداره سریع بشه پیداش کرد من چون فالوت ندارم اینستا اگه راهی هست تو چنل بگو</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/withyashar/13250" target="_blank">📅 13:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from<>CNA<></strong></div>
<div class="tg-text">برادر …
کامنتت پیدا نمیکنم
راهی نداره سریع بشه پیداش کرد من چون فالوت ندارم اینستا
اگه راهی هست تو چنل بگو</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/13249" target="_blank">📅 13:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ایسنا: اپراتورها پول کسانی که اینترنت پرو خریدند را پس نمی‌دهند و فقط می‌شود اینترنت پرو را به اینترنت عادی تغییر داد
@withyashar</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/13248" target="_blank">📅 13:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">جناب شاهزاده رضا پهلوی گرامی،   پدر ، این پیام، جمع‌بندی دیدگاه‌ها و پیشنهادهای گروهی از ایرانیان داخل و خارج کشور با هدف تقویت انسجام ملی و ایجاد مسیر عملی برای دوران پیش از گذار است.  عناوین چکیده از هزاران پیغام مردمی به‌صورت خلاصه:  * ضرورت ایجاد ساختار…</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/withyashar/13247" target="_blank">📅 13:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">رئیس سابق موساد در مراسم خداحافظی:
اردوغان ترامپ را متقاعد کرد که عملیات نظامی به رهبری کردها را که قرار بود اولین گام در یک طرح گسترده تر علیه رژیم ایران باشد، لغو کند.
@withyashar</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/13246" target="_blank">📅 13:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو: تا زمانی که ما هستیم، نه ایران و نه «همسایگان» آن به سلاح هسته‌ای دست نخواهند یافت.
@withyashar</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/13245" target="_blank">📅 13:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ائتلاف «اوپک پلاس» در حال برنامه‌ریزی برای افزایش تولید نفت در ماه ژوئیه است.
@withyashar</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/withyashar/13244" target="_blank">📅 12:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13243">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اتاق جنگ با یاشار : دیوید بارنئا، رئیس پیشین موساد، پس از پایان دوره پنج‌ساله خود در ژوئن ۲۰۲۶ سمتش را ترک کرد و استعفا نداد.
پس از او،
رومان گوفمن
، سرلشکر ارتش اسرائیل و دبیر نظامی پیشین نتانیاهو، به ریاست موساد منصوب شد. او از نزدیکان نتانیاهو محسوب می‌شود و در دوره جنگ ایران و اسرائیل در حلقه تصمیم‌گیری‌های امنیتی حضور داشته است. گوفمن برخلاف بسیاری از رؤسای پیشین موساد، سابقه طولانی در این سازمان ندارد و بیشتر از بدنه ارتش به این سمت رسیده است. برخی گزارش‌ها می‌گویند انتخاب او پس از ناکامی برآوردهای اطلاعاتی قبلی درباره امکان سقوط سریع حکومت ایران انجام شد و ممکن است نشانه‌ای از تغییر روش باشد، نه تغییر هدف.
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/13243" target="_blank">📅 12:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13242">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76b8efdf64.mp4?token=HwBnsDQ-eIM1z8FITMA2BgVph3JPK3Ia-JE65hAhyB6lGWj83hPsy8dGj_t66kXNDdUy-pmtZuViqKeBk_X0eV30_WIu7PYU2-MfUFsLyWZft5b97VkU74efKF2E2EnaJC6SyDdUHdM9Uzjg-HCJqT2cdHO7K5cCqqhGwZvG-5OBWQlKOdhlTW_WO-FSyMlQmEp6AvtSy75LntPy7qnpeOJoz38yz-LTYMiWUXAZl_zxNI6hRFWulChuKTu8sr3tWkjxicqxGbxZe8v0vopdKDdKxURZQhHdMiDqs_lD0jiG3o3kI90u0P5m_cL4rmWq8oki24YrKvXVHgkSZmsOTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76b8efdf64.mp4?token=HwBnsDQ-eIM1z8FITMA2BgVph3JPK3Ia-JE65hAhyB6lGWj83hPsy8dGj_t66kXNDdUy-pmtZuViqKeBk_X0eV30_WIu7PYU2-MfUFsLyWZft5b97VkU74efKF2E2EnaJC6SyDdUHdM9Uzjg-HCJqT2cdHO7K5cCqqhGwZvG-5OBWQlKOdhlTW_WO-FSyMlQmEp6AvtSy75LntPy7qnpeOJoz38yz-LTYMiWUXAZl_zxNI6hRFWulChuKTu8sr3tWkjxicqxGbxZe8v0vopdKDdKxURZQhHdMiDqs_lD0jiG3o3kI90u0P5m_cL4rmWq8oki24YrKvXVHgkSZmsOTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دموکرات‌ها نیروی نیابتی ایران هستند !
برایان مست، نماینده جمهوری‌خواه کنگره
:
"تهدید شماره دو ما، جدا از سپاه پاسداران، دموکرات‌های مجلس نمایندگان هستند. آنها دومین نیروی نیابتی بزرگ ایران هستند!"
@withyashar</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/withyashar/13242" target="_blank">📅 11:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13241">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">روابط عمومی۳پا صاحب‌ الزمان استان اصفهان : احتمال شنیده شدن صدای انفجار کنترل شده در محدوده جنوب اصفهان ، بهارستان و اطراف وجود دارد.
این انفجارات امروز سه شنبه ۱۲ خرداد ماه از ساعت ۱۰ صبح تا ۱۸ بعدازظهر انجام می شود و جای هیچ نگرانی برای مردم عزیز نخواهد بود.
@withyashar</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13241" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سخنگوی ۳پا : برای تمامی سناریوهای احتمالی آمادگی داریم
@withyashar</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/withyashar/13240" target="_blank">📅 11:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c22e4a8d1.mp4?token=Cs7_79D4IJdlZygJWInWe5subpIYFaUJkWJtw59qQf8rriA8i8aeG6cYaTn2uvqIZDgNTL50F3AR-ufOoeSffsJLg-7KumpL1bN2LegjuMfHWkY3CH0T0pdLBIj-HLRRypd2olA5h31bUFeAXAijEE5v82ztEZ1SFsS55wFSLBlPd6XNW5oMzEOPFGUaZ4A3N9p8rDYm5SqA7bzYNkoLwaSFUwYDEpQpRzdQpGx1hf4QUomn7ERn3g4aRRAGzujkg-qQpRmjuMozCi5TinuQT7IGYQS4Qhg0HqW67XIgo8BTZCteJ7isJMHFpXpGt-JEMXQoX8vtGOX-dNZDQFtI2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c22e4a8d1.mp4?token=Cs7_79D4IJdlZygJWInWe5subpIYFaUJkWJtw59qQf8rriA8i8aeG6cYaTn2uvqIZDgNTL50F3AR-ufOoeSffsJLg-7KumpL1bN2LegjuMfHWkY3CH0T0pdLBIj-HLRRypd2olA5h31bUFeAXAijEE5v82ztEZ1SFsS55wFSLBlPd6XNW5oMzEOPFGUaZ4A3N9p8rDYm5SqA7bzYNkoLwaSFUwYDEpQpRzdQpGx1hf4QUomn7ERn3g4aRRAGzujkg-qQpRmjuMozCi5TinuQT7IGYQS4Qhg0HqW67XIgo8BTZCteJ7isJMHFpXpGt-JEMXQoX8vtGOX-dNZDQFtI2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏رئیس موساد بارنیا در مراسم خداحافظی و تحویل پست در حرف آخرش : «تغییر رژیم در ایران یک هدف ممکن و دست‌یافتنی است.»
‏او در مراسم خداحافظی‌اش تاکید کرد که سرنگونی جمهوری اسلامی ماموریتی عملی است که به عزم و اراده نیاز دارد و باید در صدر اولویت‌ها بماند.
‏پیام کاملاً روشن است: تضعیف این رژیم تروریستی کافی نیست. تهدید بلندمدت خاورمیانه تنها زمانی تمام میشود که رژیمی که تامین‌کننده پول، سلاح و هدایت تروریسم در منطقه است، برای همیشه سرنگون شود. ⁦
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13239" target="_blank">📅 10:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/withyashar/13238" target="_blank">📅 10:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13236">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مدیرکل آژانس بین‌المللی انرژی اتمی:
انتقال ذخایر اورانیوم غنی‌شده ایران به خارج از کشور کاری «دشوار است اما غیرممکن نیست».
چنین عملیاتی آسان نیست، چراکه (این ماده) به شکل گاز است، بسیار آلاینده است و عملیات ساده‌ای نیست
@withyashar</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/13236" target="_blank">📅 10:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13235">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری «مهر» به نقل از یک منبع آگاه درباره روند مذاکرات با آمریکا نوشت «متن نهایی همچنان در حال گفت‌وگو در تهران است و هنوز پاسخی ارسال نشده است.»
@withyashar</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/withyashar/13235" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13234">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">وال استریت ژورنال به نقل از منابع : ترامپ نمی‌خواهد قطع رابطه علنی با نتانیاهو رخ دهد
@withyashat</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/withyashar/13234" target="_blank">📅 09:47 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMat</strong></div>
<div class="tg-text">داداش خیلی ساده بخام بهت بگم اگر من تو شرایط تو بودم هرگز همچین مسعولیتی رو قبول نمی‌کردم...
چون شما هرکاری هم بکنی ازت ایراد میگیرن در هر صورت ‌
خیلی باید مرام معرفت و دل بزرگی داشته باشی که بیای همچین کاری بکنی
باعث افتخاری
👌</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/13233" target="_blank">📅 09:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from💎masih💎</strong></div>
<div class="tg-text">سلام یاشار داداشم من به عنوان یک ایرانی و هم وطن بهت افتخار میکنم واقعا الان خیلیا ناامید شدنو هیچکار نمیکنن حتی اونایی که تند تند استوری میذاشتن الان فقط از زندگی خودشون میذارن واقعا اگه این انقلاب شکل‌ بگیره شاهزاده بزرگمون بیاد همه ی ایرانیا مدیون تو هستن
❤️
😘
خیلی دلم میخواد این متنو بذاری چنل و در کل بهت جوری افتخار میکنم که تو زندگیم به هیچکس حتی خودم اینجوری افتخار نکردم
💪
❤️</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/withyashar/13232" target="_blank">📅 09:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الجزيرة: حمله اسرائیل به شهر الغندوریه در منطقه بنت جبیل در جنوب لبنان.
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/13231" target="_blank">📅 09:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/13230" target="_blank">📅 09:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 78K · <a href="https://t.me/withyashar/13229" target="_blank">📅 09:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">پست شد اینستاگرام سر‌ساعت  https://www.instagram.com/p/DZDi1pCEfvI/?igsh=MWN3ZWNhdWxqbmk0OA==  لطفاً این پست را استوری کنید و برای تمام افراد مرتبط با شاهزاده رضا پهلوی و شخص خود ایشان و تمامی پیجهای ایشان ارسال کنید.</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/withyashar/13228" target="_blank">📅 09:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4rkP2jYxGOEdwrgeQqpDcmjb80qD4bs5kJQowWL4Iwcb5ZdVXsXwUIyTujr-uO7Yc1qNXmVmo6CvZrHcARidHMpLmkOAmkqAqnw9Am7uOZt5DmeSbsJEUIN2WZmDDFaiZejUBbhoyKXNE7sDa4YdvZueFmcKtME8VXr-9F0cpJdnIE4OtV8DVaI4oONeu_fA5003CYgip73uPTeWcGN4AwXHVTaJwCyaGuMTOUgkZBopm0WZ3chv2qrcS_4tndUsjoIaAVT_4DDS4t1oaerp27yBxfAvTNz7AqbK5tS9BX0HizB-d3VLTQBO_rzXHr3N0FYwQsW0bDeZpOwla_nJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/withyashar/13227" target="_blank">📅 09:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ در تروث : اگر ایران تسلیم شود، بپذیرد که نیروی دریایی‌اش از بین رفته و در کف دریا آرمیده است، و نیروی هوایی‌اش دیگر همراه ما نیست، و اگر تمام ارتش آن از تهران خارج شود در حالی که سلاح‌ها را زمین گذاشته و دست‌ها را بالا برده‌اند و هر کدام فریاد می‌زنند…</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/withyashar/13226" target="_blank">📅 08:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13225">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">https://t.me/boost/withyashar
بوست دار میریزه ۳۸۰ تا دیگه لازم داره. لطفاً این پیام رو برای تمام دوستانتون که تلگرام پرمیوم(تیک) دارن بفرستین و ازشون خواهش کنین که چنل رو بوست کنن
❤️‍🩹
چیزی‌ تا ایموجی آزاد بشه
🤰
🫃🏻</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/withyashar/13225" target="_blank">📅 02:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13224">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13473aa0cd.mp4?token=FXfyoKr28wUFAfHw_n8AkWY4ZgxbCYWO_gf6-gON7YkOydb4be7HStbptxLjMqqCOd-B5nU-W2dF0T-uoUt_Eg3G068u3RkLMJfD_oApX21v92myc4V02pxG14wIkUFU8LmNQLxK1syFGCP1IZfeq9l-Y68F-Bb2yqWihDEpXqEYF2T3Pu7aZqHxw7tY_sWNxJ2VB9mcOaQidGnsvOkBRFG1cLxI0oo59-TuQjsBE3ettkqVqWOw_a3ZawMv87hlU1HC6hWda-hh4w6BTY0tqbcDvwCy8XJqhMcTVO9c_u2mqlrD2eRe8RfgKGa3ktLASHhdwzFwRdjHxT8TMEhzByOXG4HYekgJ4Y66ETrKQCom9zb8l-G1wumtKuzxSxa1JotnP7RyE5is75syRb5NvvyBnrWmQanx60J8q3_1BY-u_2FHH_kjzKsA8mc1e5pOv6c2kxXxnQf_WnjRfddM2VW3zzE25Lmg8EadaXSifHrNAc54R-qozyrc3L03GxaNrA0ma2I1DUxkBC31-wMr9JLX99mIm__cEwdQDW2CJWgcXd7GNZrx-ra0Oy5qBQcS33bWWnkpFnZy6a-bGaLfoqw6XQQqu3LSOT6tS9bv6AkMsaLslucFqkadgJv8d5HP7ij0ofDjUkG9n_YfiFQUkJ5nOy_7WF0TDZPfvTqqbdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13473aa0cd.mp4?token=FXfyoKr28wUFAfHw_n8AkWY4ZgxbCYWO_gf6-gON7YkOydb4be7HStbptxLjMqqCOd-B5nU-W2dF0T-uoUt_Eg3G068u3RkLMJfD_oApX21v92myc4V02pxG14wIkUFU8LmNQLxK1syFGCP1IZfeq9l-Y68F-Bb2yqWihDEpXqEYF2T3Pu7aZqHxw7tY_sWNxJ2VB9mcOaQidGnsvOkBRFG1cLxI0oo59-TuQjsBE3ettkqVqWOw_a3ZawMv87hlU1HC6hWda-hh4w6BTY0tqbcDvwCy8XJqhMcTVO9c_u2mqlrD2eRe8RfgKGa3ktLASHhdwzFwRdjHxT8TMEhzByOXG4HYekgJ4Y66ETrKQCom9zb8l-G1wumtKuzxSxa1JotnP7RyE5is75syRb5NvvyBnrWmQanx60J8q3_1BY-u_2FHH_kjzKsA8mc1e5pOv6c2kxXxnQf_WnjRfddM2VW3zzE25Lmg8EadaXSifHrNAc54R-qozyrc3L03GxaNrA0ma2I1DUxkBC31-wMr9JLX99mIm__cEwdQDW2CJWgcXd7GNZrx-ra0Oy5qBQcS33bWWnkpFnZy6a-bGaLfoqw6XQQqu3LSOT6tS9bv6AkMsaLslucFqkadgJv8d5HP7ij0ofDjUkG9n_YfiFQUkJ5nOy_7WF0TDZPfvTqqbdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم شهر…
@withyashar</div>
<div class="tg-footer">👁️ 90.7K · <a href="https://t.me/withyashar/13224" target="_blank">📅 01:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13223">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ادعای آکسیوس: درگیری نتانیاهو و ترامپ بالا گرفت
ترامپ امروز در تماس تلفنی با نتانیاهو عصبانی شد:
"تو کاملاً دیوانه‌ای. اگر من نبودم، الان تو زندان بودی.
من دارم از تو محافظت می‌کنم.
الان همه از تو متنفرند. همه به خاطر این موضوع از اسرائیل متنفرند. تو چه غلطی داری می‌کنی؟"
@withyashar</div>
<div class="tg-footer">👁️ 90.1K · <a href="https://t.me/withyashar/13223" target="_blank">📅 01:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13222">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هگست وزیر جنگ آمریکا: آماده‌ایم به جنگ برگردیم
@withyashar</div>
<div class="tg-footer">👁️ 88.7K · <a href="https://t.me/withyashar/13222" target="_blank">📅 01:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13220">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpHy2opczmZWPn5lxlexrBLbVP3_hUdEL7ULgDi2c8mMvICfRMUxkranaJ18o-4vCnanajXuzw9gxrH3MzAtq1an4D4SzbKalIhHN6_cT8Y1818Wj7cfjMcdtlpEFyD0xarxQDml-Ucv-ibV43X52ryMhipHo64S8Bn4uiWb46B-MiJOgkc_rTUHPiFSErk9KH0t3yzlqcNhbsGeuq4rFiQVVbEQvpGXrOToOVO_g6lsrR5ivcKc67Ad-svXQWtu9DcocoO3uJtHyN3m_GtSVFyKt5J-3Fg9Zi_OJ6EGSL0Ncuo__8C3YlfqqWrJyryX3LKa6vO2_Pv3ATCPQ9-p2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : «من امروز با بیبی نتانیاهو گفت‌وگو کردم و از او خواستم وارد یک یورش گسترده به بیروت، لبنان نشود. او نیروهایش را متوقف کرد و بازگرداند. از تو ممنونم بیبی!
همچنین با نمایندگان رهبران حزب‌الله گفت‌وگو کردم و آنها موافقت کردند که تیراندازی به سمت اسرائیل و نیروهایش را متوقف کنند. به همین ترتیب، اسرائیل نیز موافقت کرد که به آنها شلیک نکند.
باید دید این وضعیت چه‌قدر دوام می‌آورد, امیدواریم برای همیشه باقی بماند!
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 89.9K · <a href="https://t.me/withyashar/13220" target="_blank">📅 01:20 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13219">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ به ABC: با اسرائیل و حزب‌الله گفت‌وگو کردم و به آنها گفتم که دیگر بس است.
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر بگیرم.
کار ساده‌ای نیست. شما درباره یک کشور واقعاً بزرگ صحبت می‌کنید، آنها یک کشور بسیار بزرگ هستند که می‌خواهد توافق کند. خصومت فوق‌العاده‌ای وجود دارد، واقعاً.
او ادامه داد: «بنابراین این کار برای آنها آسان نیست. در واقع از منظر ما هم آسان نیست. اما ما داریم آنچه را که نیاز داریم به دست می‌آوریم.»
مردم ایران مرا دوست دارند زیرا رژیم را عوض کردم
@withyashar</div>
<div class="tg-footer">👁️ 83.7K · <a href="https://t.me/withyashar/13219" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13218">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ به ای‌بی‌سی نیوز:
احتمال داره طی یک هفته آینده با ایران به توافق برسیم، همه چیز خیلی خوب پیش میره؛ توافق صلح با ایران میتونه حتی بهتر از یک پیروزی نظامی باشه.
@withyashar</div>
<div class="tg-footer">👁️ 82.3K · <a href="https://t.me/withyashar/13218" target="_blank">📅 01:10 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13217">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qR8mQFJ9v1qqUFjMNjWu5HzCKSSK1_yIBeN5sF-ZxzALiud3kMYwgB_euYFIYhnbzAJhhK9bgtoPKlXgZ0g_g8PMSDpK4QmsGx8dKlNF6Jn9wBFfijYWt57CqRyXyyXzrNKN8tSUFBToH85ZUgdUVovg_4-Qkd03dfv6Og-2wuWgFUJlMTwO-1ZJp6ICJEerzZKYnkOYAV68OBFkkDGcG7gxxPwmuewss-Oi2qcY5LSJOuPjFaiCnwwqXAEQAaq-7_KS5Xwtpt1CyUd-tbV7cnuKOSqz83o-wEauMMWzaV2jjof68SyUIyYZwYYcSn98V5K-JnuoL4QcHceWsQXNEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید کاخ سفید: به ترامپ اعتماد کنید. فقط بنشینید و آرام باشید، در نهایت همه‌چیز خوب پیش خواهد رفت همیشه همین‌طور بوده است!
رئیس‌جمهور دونالد جی. ترامپ
@withyashar</div>
<div class="tg-footer">👁️ 84.8K · <a href="https://t.me/withyashar/13217" target="_blank">📅 01:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13216">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">WarRoom with YASHAR
pinned «
پست شد اینستاگرام سر‌ساعت  https://www.instagram.com/p/DZDi1pCEfvI/?igsh=MWN3ZWNhdWxqbmk0OA==  لطفاً این پست را استوری کنید و برای تمام افراد مرتبط با شاهزاده رضا پهلوی و شخص خود ایشان و تمامی پیجهای ایشان ارسال کنید.
»</div>
<div class="tg-footer"><a href="https://t.me/withyashar/13216" target="_blank">📅 00:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13215">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شروط حزب الله برای آتش بس:
آتش بس فراگیر در تمامی مناطق لبنان
عقب نشینی کامل ارتش اسرائیل از جنوب لبنان
عدم تجاوز به خاک کشور
در غیر اینصورت حزب الله اعلام کرده توافقی در کار نیست.
@withyashar</div>
<div class="tg-footer">👁️ 83.6K · <a href="https://t.me/withyashar/13215" target="_blank">📅 00:52 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13214">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 83.5K · <a href="https://t.me/withyashar/13214" target="_blank">📅 00:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13213">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">قالیباف در تماس تلفنی با همتای لبنانی:
مصمم هستیم در سراسر لبنان آتش بس برقرار کنیم. در دو روز گذشته به طور جدی به دنبال توقف حملات اسرائیل بودیم. اگر جنایات اسرائیل در لبنان ادامه پیدا کنه، مذاکرات رو متوقف می‌کنیم و در مقابل آن می‌ایستیم.
@withyashar</div>
<div class="tg-footer">👁️ 84.9K · <a href="https://t.me/withyashar/13213" target="_blank">📅 00:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13212">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">محمد رضا شاه پهلوی چرا اونجوری شد ؟ مگه مردم چیزیشون کم بود ؟ نه ! چون بیشتر ما حسودیم چشم دیدن همو نداریم ! حالا اینو تو کل تاریخ هم بری ‌میبینی ! تو یه شهر کوچیک میبینی ! میبینی که همون دوستاتن که میفروشنت ! اگه مهارجت کرده باشی میبینی که فقط خودی بهت میزنه !
😞
و این داستان ادامه دارد…</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/withyashar/13212" target="_blank">📅 00:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13211">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromshery</strong></div>
<div class="tg-text">داداش مثل اینکه کون خیلیارو سوزوندی دارن جر میدن خودشونو</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13211" target="_blank">📅 00:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13210">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هم اکنون شلیک موشک از سمت حزب الله به شمال اسرائیل
@withyashar</div>
<div class="tg-footer">👁️ 87.1K · <a href="https://t.me/withyashar/13210" target="_blank">📅 00:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13209">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نتانیاهو :موضع ما در حمله به بیروت تغییری نکرده است.
@withyashar</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/13209" target="_blank">📅 00:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13208">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">حزب‌الله پیشنهاد آتش‌بس جزئی را رد کرد
@withyashar</div>
<div class="tg-footer">👁️ 88.5K · <a href="https://t.me/withyashar/13208" target="_blank">📅 00:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13207">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">نیروی دریایی ۳پا کشتی «msc. sariska» با مالکیت  امریکایی اسرائیلی را هدف قرار داد.
@withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13207" target="_blank">📅 00:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13206">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">@withyashar
مسیر ما</div>
<div class="tg-footer">👁️ 87K · <a href="https://t.me/withyashar/13206" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13205">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-footer">👁️ 86.4K · <a href="https://t.me/withyashar/13205" target="_blank">📅 23:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13204">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این قدم اول هست و ما پشیمون نمیشیم
😃
نیازی ندیدم تمام پلن ها یک جا انجام بشه در نتیجه از همین شروع کردم ، من به تقدیر خودم و مردمم ایمام دارم</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13204" target="_blank">📅 23:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13203">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">دوست گرافیستی که قرار‌ بود اوکی کنه آفلاین بود و در نتیجه اینم خودم با ای آی دقایق پایانی درست کردم که دقیقه ای رأس ۱۱:۱۱ آنتایم حاظر و پست شد ، میدونم و ببخشید</div>
<div class="tg-footer">👁️ 85K · <a href="https://t.me/withyashar/13203" target="_blank">📅 23:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13202">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐴𝑚𝑖𝑟</strong></div>
<div class="tg-text">فونت پست یجوریه بنظرم
یچیز دیگ بهتر نیس بزاری؟</div>
<div class="tg-footer">👁️ 83.4K · <a href="https://t.me/withyashar/13202" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13201">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">درود در عکس آخر  کاش بجای  جناب آقای یاشار توکلیان  می‌نوشتید  اینجانب یاشار توکلیان را .... کمی گرم تر بود  البته نظر بنده بود یاشار جار  باز نظر شما محترم است
❤️
ممنون از زحماتتون</div>
<div class="tg-footer">👁️ 82.4K · <a href="https://t.me/withyashar/13201" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13200">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA.r</strong></div>
<div class="tg-text">درود در عکس آخر
کاش بجای
جناب آقای یاشار توکلیان
می‌نوشتید
اینجانب یاشار توکلیان را ....
کمی گرم تر بود
البته نظر بنده بود یاشار جار
باز نظر شما محترم است
❤️
ممنون از زحماتتون</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/13200" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13199">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ac18e165f.mp4?token=dIG9PUM_yM81iLn8C_w550E4MZYSr2rt5JD7tuDosHgvQ9NghTRlrb40EHxULDEaaEZp0MDL00zxbh7CypNSjPJk2OJhUOrytGVPNIumKv1PCuptjaYI2uiW143ETaA3hlBzTPt8YYfu9quJUanclHOgjmrPjDwwXp-rVYTT33Iu8UhAVnPogpE_frkQzDH6q8CLOrDW_-s-evc3BpkbPB0BC53-3m2a6ERNct5Mn2e1Oz4lN44-ojWVYIUcUf6eBg-IadrLgrNV6aN9uGJLU8m9ps6aawk7S_JsXs5LEQHMqYWyj8pCCjKo_2sJP4BTKzkLq_kpzjVwPBJsoQyEvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ac18e165f.mp4?token=dIG9PUM_yM81iLn8C_w550E4MZYSr2rt5JD7tuDosHgvQ9NghTRlrb40EHxULDEaaEZp0MDL00zxbh7CypNSjPJk2OJhUOrytGVPNIumKv1PCuptjaYI2uiW143ETaA3hlBzTPt8YYfu9quJUanclHOgjmrPjDwwXp-rVYTT33Iu8UhAVnPogpE_frkQzDH6q8CLOrDW_-s-evc3BpkbPB0BC53-3m2a6ERNct5Mn2e1Oz4lN44-ojWVYIUcUf6eBg-IadrLgrNV6aN9uGJLU8m9ps6aawk7S_JsXs5LEQHMqYWyj8pCCjKo_2sJP4BTKzkLq_kpzjVwPBJsoQyEvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/withyashar/13199" target="_blank">📅 23:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13198" target="_blank">📅 23:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای…</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13197" target="_blank">📅 23:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13196">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/withyashar/13196" target="_blank">📅 23:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13195">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پست شد اینستاگرام سر‌ساعت
https://www.instagram.com/p/DZDi1pCEfvI/?igsh=MWN3ZWNhdWxqbmk0OA==
لطفاً این پست را استوری کنید و برای تمام افراد مرتبط با شاهزاده رضا پهلوی و شخص خود ایشان و تمامی پیجهای ایشان ارسال کنید.</div>
<div class="tg-footer">👁️ 84.3K · <a href="https://t.me/withyashar/13195" target="_blank">📅 23:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13194">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98c544c644.mp4?token=k9yH2OqMPqXNDno5XIgTorGKhkLcYgeY-Ce4Q3NHqASUX0AjeYSBYpWYkKXbQHKPC-Q-0Prx-VIs5xDTDKQ7aJpiqFNu1qb2ds7zHVr42lGJ1C2ZQDJtmUDF5--OFM_1s9RrQ33e1dnIqoyQ_XwRuFJs5As7A_N3uEbZFy0tP-Eg4WXc4xDbaOOKLfP1L4y-RlF-y8rQU2OVv5ojQivW60xHhqkn7G2M6r903r2J4Aco5xJdc52qAnlNc5UbC8b11QdcUJb_aq84nAgUbAilrQ-x0KtjUkjFKU5VnzNtDFqJFFmsGQlAmApQSa14_n33MzBGl6Tmy-GhLcTT4kGXziTuJ7Ei6boJBikE52uRMifUVKFKdK_5PTJ4lQkTqO4KWjkY_5yexgWjCjKVveZvbFZ-j0XMoDPcKj4y5Rcufpa6knTlbO0V-K_mSq0jXO2sx3FYDoTF4V_7K-AOX235X7WRVEePwEUl34aPq_VW3erJ2h9eCdW5W0wF3EBlxxbTuy290O47gdmZ3ya_3LbWrGesMqzW_8yDt1pKS2d3Y_CjJzjf7IK2fpgdwNLpQt955kWnDZHo2QZe48Odpf9r2NoLl0rdh_ZOWG0Pxi4CmerSrTlsPH1bvSGU4VdHMyQ0-K7B0TNhEftbd3DLbjivjdpxt38Wtofdz8sWAcAu2jk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98c544c644.mp4?token=k9yH2OqMPqXNDno5XIgTorGKhkLcYgeY-Ce4Q3NHqASUX0AjeYSBYpWYkKXbQHKPC-Q-0Prx-VIs5xDTDKQ7aJpiqFNu1qb2ds7zHVr42lGJ1C2ZQDJtmUDF5--OFM_1s9RrQ33e1dnIqoyQ_XwRuFJs5As7A_N3uEbZFy0tP-Eg4WXc4xDbaOOKLfP1L4y-RlF-y8rQU2OVv5ojQivW60xHhqkn7G2M6r903r2J4Aco5xJdc52qAnlNc5UbC8b11QdcUJb_aq84nAgUbAilrQ-x0KtjUkjFKU5VnzNtDFqJFFmsGQlAmApQSa14_n33MzBGl6Tmy-GhLcTT4kGXziTuJ7Ei6boJBikE52uRMifUVKFKdK_5PTJ4lQkTqO4KWjkY_5yexgWjCjKVveZvbFZ-j0XMoDPcKj4y5Rcufpa6knTlbO0V-K_mSq0jXO2sx3FYDoTF4V_7K-AOX235X7WRVEePwEUl34aPq_VW3erJ2h9eCdW5W0wF3EBlxxbTuy290O47gdmZ3ya_3LbWrGesMqzW_8yDt1pKS2d3Y_CjJzjf7IK2fpgdwNLpQt955kWnDZHo2QZe48Odpf9r2NoLl0rdh_ZOWG0Pxi4CmerSrTlsPH1bvSGU4VdHMyQ0-K7B0TNhEftbd3DLbjivjdpxt38Wtofdz8sWAcAu2jk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : بو های مشکوک ، انبوه هوا پیما های آمریکایی در جنوب ایران و ورود به حریم هوایی
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/13194" target="_blank">📅 22:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم @withyashar</div>
<div class="tg-footer">👁️ 83.8K · <a href="https://t.me/withyashar/13193" target="_blank">📅 22:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13191">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیدبان اتاق جنگ : الان ازسمت کرج موشک شلیک شد  @withyashar</div>
<div class="tg-footer">👁️ 87.9K · <a href="https://t.me/withyashar/13191" target="_blank">📅 22:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13190">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">وزیر جنگ اسرائیل: در لبنان آتش‌بس نداریم
@withyashar</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/13190" target="_blank">📅 22:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13189">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حملات اسرائیل به منطقه صور ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13189" target="_blank">📅 22:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13188">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">پدافند تهران فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/13188" target="_blank">📅 22:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13187">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">همانطور که از هفته پیش وعده داده بودم حدود یک ساعت دیگر ما متنی را برای شاهزاده رضا پهلوی ارسال می کنیم. همبستگی شما در این فراخوان باعث می شود صدای ما شنیده تر شود و ارتباطی بهتری بین ما و شاهزاده شکل بگیرد. ممنون از همراهی و کمک شما. تا می توانید به دوستان خود بگویید و آنها را آماده کنید.</div>
<div class="tg-footer">👁️ 88.4K · <a href="https://t.me/withyashar/13187" target="_blank">📅 22:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13186">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">وزیر بن‌گویر: آقای نخست‌وزیر،
شما گفتید که یک نخست‌وزیر قدرتمند در صورت امکان به رئیس‌جمهور آمریکا «بله» می‌گوید و در صورت ضرورت «نه».
اکنون زمان آن است که به دوست ما، رئیس‌جمهور ترامپ، «نه» گفته شود.
اکنون زمان آن است که آنچه لازم و ضروری است انجام شود: حمله به حزب‌الله، آزاد گذاشتن دست رزمندگان ما و بازگرداندن امنیت به شمال.
@withyashar</div>
<div class="tg-footer">👁️ 88.6K · <a href="https://t.me/withyashar/13186" target="_blank">📅 21:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13185">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c93913316d.mp4?token=jzSVUVa5Xyt8V0jpbfx45oZYAIhlLGB2M9p-MCEGkoA5bsk_kmQKmV_lz01Y22Wi6ZCrZ4ZpWwZdRmX3OoOxnHq8Tkh-Wi7JRf87V-aOX4vPJkXaHufnCOJFwt9ThcaSTU4ooIJI1_HnZ24Y77vKcrOTHn7vmJvpklzMLuty7n4t7eh0-MxdF1l7SZSnKKZMyZ2uCAzNFeQkLHlOGP3wc80oEMDi7kA7R1plIBITXYheWQnfxmezeoHhaijtM_Tw6qVVfZFaFM1Iis5qXziQ5F_dOTkwUs_wZeuFQNDb4OmGXAk8c7SpLbuoKAfqOwcJ2ga-KzESrR6TDNkK4C0bOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c93913316d.mp4?token=jzSVUVa5Xyt8V0jpbfx45oZYAIhlLGB2M9p-MCEGkoA5bsk_kmQKmV_lz01Y22Wi6ZCrZ4ZpWwZdRmX3OoOxnHq8Tkh-Wi7JRf87V-aOX4vPJkXaHufnCOJFwt9ThcaSTU4ooIJI1_HnZ24Y77vKcrOTHn7vmJvpklzMLuty7n4t7eh0-MxdF1l7SZSnKKZMyZ2uCAzNFeQkLHlOGP3wc80oEMDi7kA7R1plIBITXYheWQnfxmezeoHhaijtM_Tw6qVVfZFaFM1Iis5qXziQ5F_dOTkwUs_wZeuFQNDb4OmGXAk8c7SpLbuoKAfqOwcJ2ga-KzESrR6TDNkK4C0bOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیدبان اتاق جنگ : الان ازسمت کرج موشک شلیک شد
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/13185" target="_blank">📅 21:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13184">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">۲ حمله هوایی اسرائیل به شهر نبطیه الفوقا در جنوب لبنان انجام شد.
@withyashar</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/withyashar/13184" target="_blank">📅 21:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13183">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfdw9UsncfXgtAL7o3mvs2n6a1hdXECsDSMUvW3xbWGGY5uBYCONxhjQO9pYriXkIwEXRolxneOuiJXUbQNeDKPHVXOmiNkzmUqUnYkD-KhtC3yoTAioOurYrWw1WU7BtAUd4MPLZ6jJsKEPOeQaeYGeLw_nmZil4_0L92ZVXg-ii4pR93zNKMElfwVyIPp5AiRrQKEhW9hvdxh8t-0TwXfGLUV077daCtoBI24QSjNfmGHwVeZ6qvsKXiDY65M0xFvTFY_jTfzndJ4tZ8Cf1IXNe6uyImx5xw4vuIkjNoqf69fz8CG00Dgk5WTfPPEd6Bf0MAi13GIGxXzXX0Snvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: مذاکرات با سرعت بالایی با جمهوری اسلامی ایران ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 85.8K · <a href="https://t.me/withyashar/13183" target="_blank">📅 21:17 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13182">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شلیک راکت/پهپاد توسط حزب‌الله
@withyashar</div>
<div class="tg-footer">👁️ 85.5K · <a href="https://t.me/withyashar/13182" target="_blank">📅 21:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13181">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pc2-jYuz6VpHDRWUgqqlMXxEjwfzSrJDcbrnAFEyNXyp1m7HNd8O8U17XwlUvIXwNOyRnpSkWPxu2Opuo43OMPhdJaPDhs5Vfkrq3rhi_nTuC55ci_vpHbmtu1HiDhGEz689KK-J8hMkAbhRtZ4H8gkmiJBfp6sgOLgpf7IOob5g9UScxgvvscz3SToucvByR01OsuiiInSaJGvsIqV0BEDuQJtz8UyQoG4HV2srGMUenYJRUhg1r7_OkRYlnF5OgLpVLezXgAa3ivIdnkoQ0GpwApEFxvFL9ed8Nqs4mS2BnzcIFY0SxMP5N2etvibSz5y_u6xi-7j5n68tipqmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«من تماس بسیار سازنده‌ای با بی‌بی نتانیاهو، نخست‌وزیر اسرائیل داشتم؛ هیچ نیروی نظامی به بیروت نخواهد رفت و تمام نیروهایی که در راه بودند نیز پیش از این بازگردانده شده‌اند. به همین ترتیب، از طریق نمایندگان بلندپایه، گفتگوهای بسیار خوبی با حزب‌الله داشتم و آن‌ها موافقت کردند که تمامی تیراندازی‌ها (درگیری‌ها) متوقف شود؛ به این صورت که اسرائیل به آن‌ها حمله نخواهد کرد و آن‌ها نیز به اسرائیل حمله نمی‌کنند.
رئیس‌جمهور دونالد جی. ترامپ»
@withyashar</div>
<div class="tg-footer">👁️ 88.8K · <a href="https://t.me/withyashar/13181" target="_blank">📅 21:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13180">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرنگار اسرائیلی :
یک منبع بسیار موثق از فرودگاه بن‌گوریون به من گفت: اتفاقاتی که داره تو فرودگاه می‌افته دیوانه‌کننده‌ست. تو این ۳۵ سالی که اینجا کار می‌کنم، تا حالا چنین چیزی ندیده بودم. ارتش آمریکا حداقل شش ماه زودتر از برنامه زمان‌بندی‌شده وارد اینجا شده. اونا قراره در هفته‌های آینده هزاران پرواز مسافربری رو لغو کنن؛ تمام مسیرها و تمام مقصدها رو.
تنها جایی که براتون می‌مونه تا بتونید یه کم از این اوضاع خارج بشید و نفس راحت بکشید، یه پایگاه بزرگه؛ پایگاهی که می‌تونید برای مدت طولانی توش بمونید.
آماده باشید.
@withyashar</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/withyashar/13180" target="_blank">📅 21:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13179">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رویترز به نقل از دو منبع اسرائیلی: اسرائیل منتظر تایید نهایی ترامپ برای هرگونه عملیاتی در حومه جنوبی بیروت است.
@withyashar</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/withyashar/13179" target="_blank">📅 20:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13178">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۲ عبری: تماس تلفنی ترامپ و نتانیاهو بیش از یک ساعت است که ادامه دارد
@withyashar</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/withyashar/13178" target="_blank">📅 20:55 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
