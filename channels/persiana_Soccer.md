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
<img src="https://cdn4.telesco.pe/file/h8btISsDn1lLBnJInvFEzvG-MizRLxLn-DJYNzR6lCIq1SJ_Gogt9hoksvToT_jpF10XBgH6ZcekQph0q0T6hq5bHDDC_PupLi2N8DlxkBd5gIkBdPgARpBejZJVTFlSgUcib0MEnvPfCNfs1H_qOgKtoxcIckseYIJ6n_H6X8bMLBe-WWeVmbFH9v-8qqmxnOAphMKBMUKvO10JA8x2k9GwJ4u5TYQV8NEe-QiWKY8tK77yusrURvSeh7e-ASoCaIENI4CcP01f9s5NB_A3MpyBwsfyfRcMh3WvuWaCUyb_hxSmpWomh6JqEmlHTVAmTtpLAXvK8GqNPLTRDBvmgw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 310K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-29 21:45:51</div>
<hr>

<div class="tg-post" id="msg-23854">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mui1kahPgwY3GVvLXcYIvrZ-fXifyDICtkmw0pB7WKbVT9gpVif9AJWKyj2VSEumN9fVEj1jIdWccCJqhh2kTOhI2zPS9vRvSnnGRZiqcV70YzUL5FkMyljoH1jB0X2cDS1-VBDJPd0Bh9RA-bmez80dYSbbuVEnXbVRZ6XovhS7mxSvWp1MMkxe1bnwzhm0dJJlO7d8VyVZ7hk8ADVO17ID2RGbxmc4vBK0jc8sAfkPB_MZTnFPamtkaIPzVIR5YH6iuxkMyj9ktshEF-ax3vweL7D0cH1iptgQqw3lTkofRSYyFyKnTl6RU7uWGMtpWgyZZQSqiBm_-nfDHy-mRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wxx4BJjzT7cUNlANntvcHs-PSZTsFI7SlzjhevXFMj-jKspW-Ico8jAa0rAGoMSoTuIu2xO_M7MJX4GZagKxZ5LvOtdcV3R8I1Y9A0ag5QZv-feyILSQvl0C36_5xOeU88uv_YK8qQ5iuG9ogQ117646EUihjbt4Cx79snjZ269DNX3wMYeS6G5Fdg7YWyQqClEgxndsa6Dv-lW-QEa76tcw9IUQ2hHtaikM0C5ssD4bYkR-Lj5RaYS64DkdJT2qMMYjsosKnbDJuGGbu-7vYmrOymKpYhmNYbJc3uWzPhQ46zGPXcPmzyfevKNzA_kroBvkcdJv-EcgOwV_TelnxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دو تیم آمریکا استرالیا؛ ساعت 22:30 از پرشیانا اسپورت؛ هردوتیم‌بازی اولشون رو قاطعانه بردن این مسابقه امشب دیدن داره از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/persiana_Soccer/23854" target="_blank">📅 21:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23853">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-DqgBXJpolvsYQx7ZccW2dvSJebC10ZI0uyVLVTlA2Ci3BEnpmyI9qnBDSQh9jKSQs5B9ypWlW-Dhd2rPI7hGqWKmVBYIyEvIBInqT8X7Ao-TWu8Kw3xDsE_nrXvkH3hNNbiC5n-_sidGt5r0PK14iPI27DoTF9pyoyuSikm5KFwbHO_3XahrfOIh_3t8UO6P6ooKZYWQeyEtp68Ws9-YD-uRojT8xuPwU28D7ZujZ97ublYibq77ZZTwxxuw_roBYCUs3FenRwQoGHBvf3ENXugFx13IkuMOuFfzhWIEWs4MeWOdZ8j1H7vIxYDnZqgIDu3eMAyUQqq0PBuFaKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/23853" target="_blank">📅 21:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23852">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DaHe6dEhd9XP43ZqaA-_FQh-ij281L_J2MJIGMYIJqMR00DXU9hy2PTk5U-BdhSeSoh_Vcbz896Y4Pl57BsuDCHz8X9mRmEy42rjtY57_SimV7gOskfJ1nR-PlFo0CQWH14P3bu2S3oIHjZGE1eFFy9b_HGr9sXfTyBlRi5qMOddp63yTe0yAZgdyRCb1rGFjDch7WYf75_gLdcddN8doPoNx_AlMG3KNPDeJjizxoQeJPsVgvqInUJbgzFS5PVxvSA5p-9MlokLYLgRsIqlJkQk90kjHhL08z8Yb1py1pExTnYWDR4C6FglI_cXaxLssEQrLGQ-sPM5R2K0JxdqMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سعیدعزت‌اللهی‌بازیکن‌ایران‌باثبت‌حداکثر سرعت ۲۶.۴، پنجمین بازیکن کند هفته اول جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/persiana_Soccer/23852" target="_blank">📅 20:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23851">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7648c46620.mp4?token=tvBceG2UkZ4HwOVVCtNETOMfrEVpWIz2o7ICAir2IP59X6tP_XQr9DK_-EFfbICBDUbVtMcGe6bLUtWqzXAzhZgsx6_VnV0Nu11F3DfUL4hJAPklYT9KlTH-LFZe23lMPqIi4-TbECW3zfz3DHO0tweln7uu5LACbhRlw-06Spq49iKzVp4Cfqbv5eoA37fN1zYy2q7hv4HkP8GlgfGEYemRr2n5f66t18skLY9DK5NuvEhjejiRUDk56fV4KAJs5P2XXO3FeWjIGUAE1yrLeqNptec312xUoExnJ7nVyQJ_XDzKuRXddS4Sadun9ctR8ollaJmrAsn-Oosdld53Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7648c46620.mp4?token=tvBceG2UkZ4HwOVVCtNETOMfrEVpWIz2o7ICAir2IP59X6tP_XQr9DK_-EFfbICBDUbVtMcGe6bLUtWqzXAzhZgsx6_VnV0Nu11F3DfUL4hJAPklYT9KlTH-LFZe23lMPqIi4-TbECW3zfz3DHO0tweln7uu5LACbhRlw-06Spq49iKzVp4Cfqbv5eoA37fN1zYy2q7hv4HkP8GlgfGEYemRr2n5f66t18skLY9DK5NuvEhjejiRUDk56fV4KAJs5P2XXO3FeWjIGUAE1yrLeqNptec312xUoExnJ7nVyQJ_XDzKuRXddS4Sadun9ctR8ollaJmrAsn-Oosdld53Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/23851" target="_blank">📅 20:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23850">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kK1PGFvjB7zxQTukSX7YYs98tO30Zjruvpk8nAodE3IRD8GU2TWe9KYMCm9viSTRIX8HIXfO_9cUu-bjbbCg9Z_CE3qAyqsIM6y55QZ5AUmsv2sqmUIUiYJZ_6N61LyBbr8-pOyhU6b1IKHuh1mIdPaZenPLO_gFGmGSLbaToZwCDoE53Jrnw-Wrmn7k5lGIKqwlDErwkhiAoW9TmbR3Q8TBM1Bgx7zWUYG0v8cDHlCmzrhRfl8UMJfHsKzTBRdOdNwroYrfTnq-YzEqrOULJzxPCpQOOjGObFImqUBHcKfLK3txyrunkwd3bvcZGj7AFes3USplbWQHi8jitSdGJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/23850" target="_blank">📅 19:54 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23849">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MciWV93_Xyh9TVnzp3b5UFC5FpjtGSzfmuzE_RrQ2558dQ3zKY9_d795hvO_hDMe2Ysdvkqb1QToT9fJ1_xllOu0cr2LDEm9lEdkuy1iK1c0J9MQoZt4oabccmLc321ZXc5FziK9jl_nqFaR2g3PxKMJ6nc2WWVGCM0XVfKH5Lv_bShIDsFz7czU0trqnpFbA3Z72FFh3dQKpKZzsPxiTUSFbncqd74R5FqDeFAx1XM4--Mgg-Y7TLBZHBlmF1-2fB9mizsoRpUqBbwpUHXCkUuHtumMjblpoEmO92BgO5orzwuV6URbY4UFAncD-iQ1kk3YwgMKKx3bnpC34_SM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد محبی ستاره فوتبال ایران در واکنش به حواشی اخیر: من هیچوقت همچین کاری نکردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/23849" target="_blank">📅 19:35 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23848">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9XSkhRRRUUhda3yunVtVHrjBK2jeeGTz2lwu9XOEHcpu98qL6WASCEyI5u_XBUWEFx4bZ8tPrWjOpDp4Q2lJfe7KL3zpg__cgpfeJEfSiMJDZD766B8DkEruWao2I50D45QfBOqqDOvVNZzax3v-gS9Nmz9O4iE2WgLL8j5ZSybHI8VdySprF-osUJ8rHjVJg6u1DfdhMmg_8rcaTBnY1464h_AzqWGhLkCuU7XR7YECLIfJM8ZZbtYsLi408bqvEBttcO64zc-mJBQeBuGlj52MQgffFVzDEp67EbiT_hmkB-c31rCHMoPFc0jBSbnbaJXu1eCFyumExD2O1Ef-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23848" target="_blank">📅 19:13 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23847">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLvi9H6iEEPgl14X2kKtd_8EKcQGKkdCx9niQf2Vl-xCWCFNolhr0BkB088n5mfAGvZgdeXHuOBt10u9hGWDCyqYH_v63_f8QRRoGYeW2AnHtLtKLOymIimcBmzeKE-L4Flo0hXPRcnfKb1bBCgbsCnYv7dZOcnsXnnGARJkRzBHaz3EyT8qka-BJkq2te9zPuxHbY8xojpsTOr69RlnCpFkSQhe82G7oySiezqO_NkbVXIjKUAQlpz3vFiBmOX7r3vT0_VqCnkTE9NzdBPyZiP368W3qI1_oGfoklcar-ySD_u1ChxS9bhdBpTln0pnZOVxtRrpYXktBEnoVBo8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پدر رامین رضاییان: خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/23847" target="_blank">📅 19:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23845">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0PAFHpnngm7NME1YMMOI59LHVFpPFX9tGJXs6FTwyToil0xXyeKMplUwjTFTRaQpMYOslI5lgpI68cRhK88JNhlEje6piV3QvJ689cheKoi7v6uR7nFVPgZaSjfK6KOzj3Doj0P7wolK-lkRwzIe4A-RBcKsBX8n9EEq0Zvobgfo_SEr1814lzTkiZ106c-VcsMsvntiZMcg7coqCStbUcpRS2niWv2qFv3PkSFX5pB915M458COjX1HyAo0rZpYW90h9gS10Ua8hNK4YTAfhY8dbAKne3_m_08c2UbfQfPdo87GvDzhwp4xhruLxr_SNSPuA3fCbEnEX4bXYCPwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
طبق شنیده‌های پرشیانا؛ علی تاجرنیا رئیس هیات مدیره باشگاه استقلال شب گذشته با مدیریت گل گهر سیرجان برای جذب پوریا شهر آبادی مهاجم بلند قامت و 20 ساله این باشگاه تماس تلفنی داشته و احتمال عقد قرارداد 4 ساله با بازیکن وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/23845" target="_blank">📅 18:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23844">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCvasBVOObox-2No1ETeNiQfz7tWEe3fhGhs999oqJj2dZwDzEz1nN9xOLCg4Xb4wWtARaWMn1ax1fDZxPAwUalfUce92fvJKUnQtlMYPtqaDoEjZgc_lviqgFOD8oMlUg--BYIrV6FqFEcA397NJNDGEPezdJZ13_J1QwGDQYHQ3ssSjZE3ar4bZW3GngWvDyUiYl5DHlcMmpv4PE8m_HCfqWNGvlWlnWF-dJxgUzY7K8nCUdaFQxRqgwOV773eACDJk74PFfB4NesxnFdaLQsycpF8fqWaF6Z-XPckh_dOzLZjuSXk0pxEAaPlT2EX4JG9Pg1umM895RIvl86uwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ باشگاه تراکتور تبریز پیشنهادی دو ساله به ارزش 90 میلیارد تومان به شهریار معانلو مهاجم ملی پوش سابق اتحاد کلبا امارات داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/persiana_Soccer/23844" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23843">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c4MKvVeYTgOxkhAjMSJTyrFTn55WqRmOKN6f8YVVSQ_YMWDVGpj_kzwr1gNoRkUKKL9meK3kSjYWWnQpbH5Tj_LhOE7mWMegP7Wr03ROc805I-QnbQGK8C_xoRZHUc2RVfmz3lfBWpH9LXX_juXodSx1G_hiMGlgn2JyBaUBDK1j6Wrd5H9EccDVnCUR0qZTpMV53XjoX8_bYaamBRDHisOoeqHWX_kPjxbomwDhQF5zl0Sy66yfRhLAJLfTpE9gFhUWxCggAZsq2A4v-XiW9QjmOIkDjPGOPYWwky4Hds2huZJfiM3isGMFB4KHHoym0R6L8MjkqgyOwwM5AJNOJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تعداد فالورهای وزینیا سنگربان40 ساله کیپ ورد در همین سه چهار روز اخیر از تعداد فالور های بوفون اسطوره ایتالیایی تاریخ‌فوتبال بیشتر شد. همینجوری پیش بره یه رکوردهای عجیب و غرب میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/23843" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23842">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sA-al9cdXpdY2-Wh6wRZkglt9Vjq4DXW48IVgU5GV98XPe-aqLi-OTbSy3uscXVha0WtFYdF9X70mki0Yaq0v_cSjZXvGhUixAZJ0j40DLPPgfy0oa7U3KFKwsalmr5dZVVjv7ZNtmfg7PBkJPJ9USZzZoYU4JDcN150nsn32xjyrx1UShOG_yHYmZ9RkBSRm0KNRG0_peuGKxmlzomdlgHDPVTjuGS7N6wm0NzroPhfB-coNvKpw_WafFPgV9zJG2e0VTmXKVl2LEny_KUKQ2jurZCM8APprTXSnCd4_eMcnOk1uVmVZUngpMy4oz8BSm9hMefK3GuFvm1GyULbog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
#امریکا
Vs
#استرالیا
🏆
🔥
⏰
شروع ساعت   20:30
🔥
20% شرط هدیه ویژه شارژ ارزهای دیجیتال
💳
امکان شارژ با درگاه پرداخت
🎲
آپشن های متنوع با ضرایب بالا
🎁
10 درصد فری بت به ازای هر بار شارژ
⭐️
برداشت زیر 15 دقیقه دلاری
🔥
همراه با درگاه‌
#ریالی
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⛔
در صورت فیلتر بودن از طریق VPN غیر از سرور انگلیس ( سرور
🇺🇸
🇩🇪
🇨🇦
🇫🇮
🇹🇷
👇
👇
)
🇪🇺
https://trentivo6402.bar
✅
کانال تلگرامی
#رومابت
29
👇
🔵
@Romabet_official</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/23842" target="_blank">📅 18:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23841">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPnQojm9_6fWOP_GwAHzzIX7ia1sCoy2He6MX-Q77x9EZH02fMWSJhDJFp6jgL7LOKgAKFSNDofb9d9ImgW1_b9cKPRI9r5jSi8G1j4EAoSRxv24nz_eE1Rpyb92uSPM98UXAxt99nteSYv6mu3mmw_1Heo8MbHo7ttqtwL1segDAO4cOULQdmjdG5UrcYtfA-pG_2-9jin7WtjT9rNOxHsPIDPfd8j3lsU_VmU2EqUFxTtLt_sbpfYt2BKkPXFbdMk6YZ4Ijjwcl-RusX1YfcJBOZSWUPwvsk4HXBcVDfvNalsktZ_u8-VH2dCwA1ftkwjWK8YaafmqfNgYYLhz5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شش تا از سنگین‌ترین باخت تیم‌های آسیایی در تاریخ رقابت های جام جهانی؛ کره در صدر جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/23841" target="_blank">📅 18:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23840">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJsti36wZgr_7DXLPKN9lgrz7vWC7OvMSxdpgFNrB1q_AGtlBL9BxzRbVaMihjyBuZsDSxbewfonNWdWA_HlhISt7i2Zg5eJqgNgGMhH-7tl_MTuJyvKDa-L5Uwyt5S6eHKXtBiQrdc3FuciDTcsNiA3yX0KLz0QI046LlG9akrG-uqnzGRTYS_cYlVGiQPh87xVPlFGkrpSMzhiRDAD1b-sEsr2TnDr1bFss-GKLHXk8JeM2NkUrCq8dn0eNNPx6E9FCaoGMmOPd5DN6uNipualHGb9NL__yct4SH4JmlPIYf48KCo1CaGtMF0iVCp1bUnq300BzsQ8OhOM2Rs2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
لیونل مسی به عنوان بهترین بازیکن هجومی دور نخست مرحله گروهی جام جهانی انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/23840" target="_blank">📅 17:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23839">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gfk0MOivTRbLCHvXVHV8BBTBjL6lGBDlvp1uC0_je-c5kh6vQ5ZD6PvjvUWpxrEUvyhTro7j-gJ3aJgcrtZ-9W0IZ1JPjCrp775l21maosoUlOpJSRuxhX49PNNrK2ZEFjhjZnARm-7KT1n3Ge-DM3bgZEHkxOZvi0EFFrF-ewgzI_Sz1SK6MGqLWfush4oySh79u4cCkySZ8_ESVlrLz7L9VjeoAE7uVAsuQWrFxUMojYeZ7Fg7-_VgXTvYal-fBEhIxRiiYrHbD1gue-W_Lwr2MNvSU8IrdrzUG1Orf5WG9xy44HWJvacAgvDLDeeBhPBETdSs8vjqFeN_OycDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات
؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/23839" target="_blank">📅 17:39 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23838">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=XgDiov-Vwrv-q14k3FYDDLaA3Nq3VUAf5TDQMCIWNT1yT_LVkevFIX-hHXVEUOqJgH7rYJf8nT9AXBYngJNhATfi2BeCaNUBmDniyOGT3kWgtPe2CdeFLMdYwwvu20XOXc9tvwPFE4XLgqHFeJLOgxqJx_Nvq514i2PKEZboeJWkZd1-0UqC7KApe4OwjXUD1HAo7Mulga-tZ7uY8xx2HBzm55YtxA_4XQ4u4HIPwBmpezTH9QzFQOHgWJrGCRUdN81W7WwZdb8beNxhyqSVSk28k1CiCyMmMDDIuFqe4tKVnFHTJm9xFqzY0f3nthJk81l7g20pm5b1j7nYorLGmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8fb916202.mp4?token=XgDiov-Vwrv-q14k3FYDDLaA3Nq3VUAf5TDQMCIWNT1yT_LVkevFIX-hHXVEUOqJgH7rYJf8nT9AXBYngJNhATfi2BeCaNUBmDniyOGT3kWgtPe2CdeFLMdYwwvu20XOXc9tvwPFE4XLgqHFeJLOgxqJx_Nvq514i2PKEZboeJWkZd1-0UqC7KApe4OwjXUD1HAo7Mulga-tZ7uY8xx2HBzm55YtxA_4XQ4u4HIPwBmpezTH9QzFQOHgWJrGCRUdN81W7WwZdb8beNxhyqSVSk28k1CiCyMmMDDIuFqe4tKVnFHTJm9xFqzY0f3nthJk81l7g20pm5b1j7nYorLGmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/23838" target="_blank">📅 17:31 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23837">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‼️
اگه‌ایران‌میزبان جام جهانی می‌شد...مگه اینکه با تصاویر ساخته‌شده‌توسط Ai بتونیم همچین چیزایی ببینیم وگرنه که تا حداقل ۲۰ ۳۰ سال دیگه هم قفله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/23837" target="_blank">📅 17:27 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23836">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HF_d9S_bp0M8q5le6Hj9saXiEz3x9g5LwTWasd60ie_ZC4JcvPtGqK-8K__jMcPYGywos_KubooFvj5iRnIZAS2ynpHzAhJW052a9FBfzUoXtwDygOming0GwYoJe-PrZ4UiOR_9QP040PJzJX1VJa6IjoUSGccoJw1va4I2XlV6EtTJEdX5AIl2_1LThTYfnwXDK2QWG2KDCrduhouwlSYRaFdC8dTMqc38mW17_chISth1X9hJavJ1je2Sjw_WhDelnEBZdLnhCJmw43Tg7_gD-aAjwh7bJykp89DWSLhtzwv0uc34yss3nW7RnrD6PDHHMGcJH7xHQU6WcB68kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابوالفضل رزاپور درصورت جدایی میلاد محمدی.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23836" target="_blank">📅 16:58 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23835">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmakQ0Ue3LIAgHGstBbK5cQcuC4QkTjVXC3GRtoWTa72sog_3Ypoa3y4BCliY4-ep574qNh8vNSFbp8Rt7scWsBC4eE8AkU7YrWQkrS-NBTYOZ1XuY6rQDa82NtL3xs76THR_KRptp0bRso6xGqJHIRVt9qc6Ne_qN4ey-oAwxOpxN7ugWf2x80ijwDfvjhx_jR2Hc_wUk1xzYBzHKz9tPHSQBm6ZUOz-eJERTZ67NJm28SiOYzeZQ8CDimqoG770AlnuQ8C7WugIuUnTieIrllwXczWo_bH3f6RGSWkSk5lBmROnUdm7g0K5twYj5h7orGF8i7b4B2NcO1ZO-Gbiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
باشگاه اینترمیلان رقم فروش آلساندرو باستونی مدافع 27 ساله خود را 70 میلیون یورو اعلام کرد. مورینیو بشدت به سبک بازی باستونی علاقمنده و به فلورنتینو پرز گفته لطفا اگه میشه جذبش کن برام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/23835" target="_blank">📅 16:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23834">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uXa_0oZ4z2kmWUUc6T19f3d9hZiPHAp5zcorclj9dvIAt1j2Wwy9k-Hzi5o_soHQ8Ezg-C0v0IUNlpX8Q9zggtXRZw7msMZzfTUugXg9fwM2m9pNYQVXVpjAYujdf-9u2PGsYzZXNnvc2K_iqwlfmdrIUJ2MUsRPX9jp8S8RVJ_6BbeupH_8XOw9KVpkrVAO-YObI_r7QDIyK3FqFIaHq89WfS1Vp6n9CrlRvbBzqNLkiSL1tTfC0j6Cm5NkdJeGVFbRF7hzT3VGr_wABoDa728K_wLkLoCQ-4JPQVJlvuTeMFToqyvnOPM0_7L7BwBj5VSQFrKa0N0dzbL0uhhKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a17a904766.mp4?token=uXa_0oZ4z2kmWUUc6T19f3d9hZiPHAp5zcorclj9dvIAt1j2Wwy9k-Hzi5o_soHQ8Ezg-C0v0IUNlpX8Q9zggtXRZw7msMZzfTUugXg9fwM2m9pNYQVXVpjAYujdf-9u2PGsYzZXNnvc2K_iqwlfmdrIUJ2MUsRPX9jp8S8RVJ_6BbeupH_8XOw9KVpkrVAO-YObI_r7QDIyK3FqFIaHq89WfS1Vp6n9CrlRvbBzqNLkiSL1tTfC0j6Cm5NkdJeGVFbRF7hzT3VGr_wABoDa728K_wLkLoCQ-4JPQVJlvuTeMFToqyvnOPM0_7L7BwBj5VSQFrKa0N0dzbL0uhhKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هوادارای خارجی رونالدو بخاطر مصاحبه ژائو نوس که گفته بود کریس‌رونالدو برای‌ما فرقی با بقیه بازیکنانداره‌وبهترین‌بازیکن‌فصل پیش لیگ عربستان هم فلیکس بوده ریختن تو پیج دوست دخترش:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/23834" target="_blank">📅 16:17 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23833">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OLCncAwV4BzYk3P3-lQhQ-dnRhA6QAZuERUBBMsDDkT-i1spW-EX1ekzDy0iwVw9hzro4CUeLRpRN0N54Y8V9gE0XsrNQb8sk7GWVX17ZPwRsWe0LPCuhwwJkEvlSKEnu2jJZxNZ0M-f5xuZd8acNvSeVaDZ9CdedoTK54h13iy06HFp1CRJtJ9UfPOgwYhBBlHkzSpkO9vcdFgeEGQr0Y8uxwsNFEg1y9x85wD7ufw1zObnjlyBNFqX9XKzplO3onwvB175VvDK4d201lw4oQql_gORlsS3OL8MEhnU0xEQHxBjHQMFQZHt7tLMRtbj1QgF3mxSaUAdE5M6OXZHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛طبق‌گفته‌رسانه‌‌لهستانی؛ قرارداد الهیار با لخ‌ پوزنان سه ساله به ارزش 5.5 میلیون یوروعه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/23833" target="_blank">📅 15:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23832">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zr-z1fdE6MUOoRzBBOZR9yl5tBlqkyZfH-4BqLec-6FmJLGpOJoA2ftAq7zsipKucbRTGWobkv9MKPGLG3GZzM3dTgim4PtJIIqYIdFLxYTsI0msLknV4WoNjJm31AHR0NuQ0pso4L1IgPemGR8ftmO7dW5PUTik6t0rdhHpmeteGnAOHN1nMz-vcHDFK8zBhz4ICwBTqZQY9DlzoqCMjTJb7TlAs585rg0JHwYwly6V38OZRTk--fx0vXTUfkoJ8wKrY0OJKp4W32VAHBwLIr02kMW5HUYC1IgVv632CFyvwzQCOpj24XERpP-aI1baFrf727qy558f81mFoyKVQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/23832" target="_blank">📅 15:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23831">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=mYTkh-Q4XWzX62KnsGMdvSfZihwvUB0RXaFnBFg6XlIo3wb71KAHIN0nA0cNsjYf4frMjLD4j0zlhvqXTFOzCDuFXwHhQmfgLDWWOt6DpuLsAbmq8NOTXTHZXA8uPfnmbsu5YPvLZQ7ijCT4_919rsC-2XtebWCSaaYyDP5RAYt16utvbk8Huk-0jA9TzxsRWwLcIlmc22rcWYpWnUpns1XRBKo8EretC3L8JzBzy8wW6MpvoMKmUil01A5oNyGx2XV3FJVJoPRXm9Q4ociIC0NRQ1yWaSDWuXWay_zE_stsRqHR1IxZWONyPusyiMwPzGqG2dNb8Yo0e7JAEp3w8UBEOp4H5f8PlFfXQlQYSXfBg91E3jQqiVnPzjHLlgEDjlVCla39MFoHWbzQKx5SYlFqhVPDTBpveKUYutWFTBxNSdWmri27KY1gX3qb6VMws8E5uWFzODSTM1iK2iyKC-Zw7pvYFT8WBGZmIuFK5PDPXjrj2QBb5UVUZeoR0hEFWL0Mnw_CI6ia-beDKjm53UA1fBA8lDvTl-Vp4J1TaPFb3gLINEO4MeJUW1oS9n433z6o-wLem2g4UdCFdFshSmi8H3WWPIGtU1fESZrslIkIIoV5fR-SNRiAlhH1AZZLlJI0xCe033XIFTLSykRPdWZPRPqA00ofpB9NX_XnP0s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb2932219.mp4?token=mYTkh-Q4XWzX62KnsGMdvSfZihwvUB0RXaFnBFg6XlIo3wb71KAHIN0nA0cNsjYf4frMjLD4j0zlhvqXTFOzCDuFXwHhQmfgLDWWOt6DpuLsAbmq8NOTXTHZXA8uPfnmbsu5YPvLZQ7ijCT4_919rsC-2XtebWCSaaYyDP5RAYt16utvbk8Huk-0jA9TzxsRWwLcIlmc22rcWYpWnUpns1XRBKo8EretC3L8JzBzy8wW6MpvoMKmUil01A5oNyGx2XV3FJVJoPRXm9Q4ociIC0NRQ1yWaSDWuXWay_zE_stsRqHR1IxZWONyPusyiMwPzGqG2dNb8Yo0e7JAEp3w8UBEOp4H5f8PlFfXQlQYSXfBg91E3jQqiVnPzjHLlgEDjlVCla39MFoHWbzQKx5SYlFqhVPDTBpveKUYutWFTBxNSdWmri27KY1gX3qb6VMws8E5uWFzODSTM1iK2iyKC-Zw7pvYFT8WBGZmIuFK5PDPXjrj2QBb5UVUZeoR0hEFWL0Mnw_CI6ia-beDKjm53UA1fBA8lDvTl-Vp4J1TaPFb3gLINEO4MeJUW1oS9n433z6o-wLem2g4UdCFdFshSmi8H3WWPIGtU1fESZrslIkIIoV5fR-SNRiAlhH1AZZLlJI0xCe033XIFTLSykRPdWZPRPqA00ofpB9NX_XnP0s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
هوادار ایرانی تیم برزیل در جام جهانی 2026.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23831" target="_blank">📅 14:47 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23830">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36feeb0630.mp4?token=YdsxMDbc_QMyMd605aHJHt4IU3yYmFqon6g4bjl_geobu2pa6CFGFuAiQghIRSZpeTlN_GUto6leCFDAj1D7tCQCpuI7cPUxBNzTncN-x69UYPdkKZ4l-3LQQelALy3EoEg346wjTZ4tAwp1SABREYMb_bBC34_h6WTNR0Fg1DAg7MW2UBHF_7OVdCXEgDC3K45vNlu-afMOdvdlqnOjfLvlQM-z3yIqm10JQJdZnfW4_-VzSqQvM-m7SXVF3IKqCyTdK-5qLyEhYP7fl1R3ZZOFRiHL4yQoVpUJKJqeRCc2NmI96qMfgwzjhposcBGq0HB_LLlE3SO7SMgFF4u4hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇦
صحبت‌های الهام‌بخش مارک کارنی نخست‌وزیر کانادا در رختکن این تیم بعدِ پیروزی قاطع ۶ بر ۰ در برابر قطر و سایه مصدومیت شدید اسماعیل کونه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23830" target="_blank">📅 14:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23829">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgIb9tHTz3QXkvt9au0PAx2xWOA_aljJcJi5c5JSbPIpBVyXvH1JOlalrIzoqeEH-Le3r-dk1jRlVRvRC6j6akCgb2wKEwlKC1fDTEQQQfYcNXoVngqM9lvr35gewWnmf70w1uI0KBYE_Jklo5seN-3RWoiPwhm0p17bXRkGSkaFXSXR40oRPBVXVIm9mKpgrz1yf3RX8kao3xPeXEsY2vKoBQ_9N0M8sVNOyCU5bVNMOXzxZHEgRnd94JFhwxguhZ4jTbzed3RhEQtOWf5IT27KzLipJO2VMM6sC8BDnroLRTkZgmPUlCXLFnk1vvXK-AeHikI6APuLkdTsi_5fuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
این ویویو مربوط به سال 1401 عه که محمد محبی به احترام‌مهساامینی‌مچ‌بند مشکی به دستش بسته بود و بعداز گلزنی‌اون رو بوسید و حتی به هم تیمی‌هاش‌گفت‌خوشحالی نکنید. به حواشی چرت و پرت و فتوشاپ‌های یه عده مغز مریض توجه نکنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23829" target="_blank">📅 14:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23827">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1UBilSSEuLydW1x6Rck-aTmX_tdoPuc9XRGkhrA6LS3sJWxKMTEDg46sQ1Rm23h3LCfmpE-H1rSpQ7L23hblsZxl8XVANWaOCfgLw5KZscFNh6ehJNmxEoOaz7Ohm7b2Vmb4S0GmTnf7WQoc94vnAXHUGVfR9RnD6l7i7GVa9WQM9ILQtgPBLG6nr21T9hSTBTHbCKo7hQZ6A9cigoY715T2myq-GG7K_eWLcs4_dmNZ8ITDPwrt9fEN727IbdZ7YuLPBjejp3rBKQoJ1mvde5OJzUiWvxp8snGyNhe8PyEDJS4Agvgn6UsxOcjBBaqMFZc_edaWMVl4_AvePf_ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MWTMRwapRdWCPsKK_H4R5S0KNooaTe-u-TQbStoclmPSp0wh4bS4kJUR7wY_kUp2tomIn0GQnW57WSWgalD4SIDdokQDS0HYQACeNUDg2BFD3pRDgmKvjf5Ce8Y6zY8nZ9lHIvRnLQ0tHXLGzb3Zv1QL31pHmwsJhYW19o-sdUGwic9gt4g21NX9cKky9P1C6Q-ABZae7qR_4KBWQbwDAEd-yDzzomw59ic0LjSrwCLszehH1NR632C3bka89SlV_u8YNRKJauHdyjHmWJnVIRAo2OGvn6Pitb5kXDBSkz1Jv5gDaDkptatA3eVLCE75_fxJvJpDBJVrWjRm_mHFgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
برنامه هفته اول لیگ جزیره در فصل جدید اعلام شد + برنامه‌کامل‌ پنج بازی ابتدایی شش باشگاه بزرگ انگلیس در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23827" target="_blank">📅 14:00 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23826">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQ2AshRo-MLORle_k6VtYUTDB-UILJi2lIrrhMowwjx8Uk8uX5kbt8aYgpWfD7VssbMuyJEYH-ykS4guifg5FTkQxsyce5jy9oLWL15swTmbNsF2vqezjF9w6sbAqtVjkmT4TKwnPmsCRYNY80EJqvA2kiumwcbkht5tnxNvpIMeoSracYVOwEYuIrtCTKJH9V6xHE6ZXnuPAs-uwVA2XbfSpzS41Wx7XPUY8QqAa5xzqng_MqOyaBmVXho_PaY4bV0EeEBKsCEsAYpGww-bBv4E03PNL0ycAHFEj-N-tROlWTkhNRWEbb4JXGwTYuWg-LlUIzARaPGnOV_XufPPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23826" target="_blank">📅 13:53 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23825">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=QYoU8_5cGYH40Jr-A6wTT_YT50__lkWaO6wUKrvc0PIFVf_BYKwA6RP2gbpTWM-NMWlgjlED5aPkM3IxmQdi07vhDLscAEpumwiiPrW78ahq1nHDIPorluxUqJyhPIgzuUFYZVaq72QR2_N8z2XA0_EJ2Xmdrts2auxP_-BKv8zlp4Kv0-oypIn0p-igrbePV5qVJ0aIXJPlhQGnxkdC7NV_dCWlvz1_p3lAtEQ0xBTZWTUgeAAKownds-wqBVOhDK1NW3Esex0eORd4CetHL572gVQbUxBe9BITSfwW5BzPUMsFgeCHHy4bwlWoWaM93ZnzX2xCKYZueH1g0QLl-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fc0b5e928.mp4?token=QYoU8_5cGYH40Jr-A6wTT_YT50__lkWaO6wUKrvc0PIFVf_BYKwA6RP2gbpTWM-NMWlgjlED5aPkM3IxmQdi07vhDLscAEpumwiiPrW78ahq1nHDIPorluxUqJyhPIgzuUFYZVaq72QR2_N8z2XA0_EJ2Xmdrts2auxP_-BKv8zlp4Kv0-oypIn0p-igrbePV5qVJ0aIXJPlhQGnxkdC7NV_dCWlvz1_p3lAtEQ0xBTZWTUgeAAKownds-wqBVOhDK1NW3Esex0eORd4CetHL572gVQbUxBe9BITSfwW5BzPUMsFgeCHHy4bwlWoWaM93ZnzX2xCKYZueH1g0QLl-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحنه‌دلخراش‌ازبازی‌دیشب‌قطر
🆚
کانادا؛
خطا مادیبو بازیکن‌قطری‌ها روی‌کونه‌بازیکن تیم ملی کانادا که موجب شکستگی استخوان پای این بازیکن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23825" target="_blank">📅 13:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23824">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l5Wr-z_kYjYIWDMOPUzK10SV2shHXkDB-Uc3f_eI5UETZmsI9-N5DZh0abIZWFN52EI5nGUqRO2YyV0qQX_5Iy0AnxjAZvBkI34WdREjNX7fb5JOVPfb8n2qd1jfrykJJKS5hypiV3JiL5RmJbFMOJjNf_9lLirr3tbVlwbopxdyhBd9I0PyRV7a9-jA48FP5JYCYQ69zJgTie33FjD6pdqrqLyT1c2qosJByb53w-w1mtvMtnvPuv5cNinJTT_sdLmW22N9kBu1h5SB0ZmaPKL0LkAzN5o1Iae7Sh9t6fFUQFgN1Uvg4qY5ct22wdz5E3eeW7TtSYnMmMMrROKCUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد کامل لیونل مسی
🆚
کریس رونالدو در کل دوران فوتبالی‌شون در مستطیل سبز ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23824" target="_blank">📅 12:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23823">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15564d6447.mp4?token=a9rN6gL8eMXDvnWJBRMgJQBrhnp9smZ8uWsJ1u4ZFgDSMZL_oUsdXwaeom-D02szGhxOZdw3VOuwa7ikxueHnzEz0pPAyliYBzVzAzMBo15ZvoCi1qa2LCTMbFzVDySaTAbw2ZXBiey2L0UJus0zFw7GWURDq_2mmXqMh9lnpe4B9SW4hy_P1SGJLpRAJ5vjTO4ZF18KUQlZi89GrmhR8dioOwgSaf5K_Pb6lnhTimG6F4ULaQwZ2GbPeBAXIFFm2jJ75cSODdTpe-nSQS_jIXDWnr3HmkRAhdvNe5pk4f7XgRuz2xVikoxds38amMPDUyK9IuKz3fwyr5E9m9HiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15564d6447.mp4?token=a9rN6gL8eMXDvnWJBRMgJQBrhnp9smZ8uWsJ1u4ZFgDSMZL_oUsdXwaeom-D02szGhxOZdw3VOuwa7ikxueHnzEz0pPAyliYBzVzAzMBo15ZvoCi1qa2LCTMbFzVDySaTAbw2ZXBiey2L0UJus0zFw7GWURDq_2mmXqMh9lnpe4B9SW4hy_P1SGJLpRAJ5vjTO4ZF18KUQlZi89GrmhR8dioOwgSaf5K_Pb6lnhTimG6F4ULaQwZ2GbPeBAXIFFm2jJ75cSODdTpe-nSQS_jIXDWnr3HmkRAhdvNe5pk4f7XgRuz2xVikoxds38amMPDUyK9IuKz3fwyr5E9m9HiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پدر رامین رضاییان:
خیلی‌ها بخاطر طرز تمرین کردن رامین او رو مورد تمسخر قرار میدادند و حتی ویدیوهاش رو برای من میفرستادند اما او برای جام جهانی برنامه در سر داشت و مزدش رو هم گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23823" target="_blank">📅 12:29 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23822">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTu4Zb6Va0ztmYFh_tvDYAyw_nC3uFFskPNu5OtE0fb8rVV4m-oi4R5dljmTDqx1bl3Dc-H2pCDDeKqbWV175xs9QHWTkqMpA3__olM5xkC1Y2kkd3EcDpw-20pFq-CXhREh_I--gk_NdhjtesY_xAlXXe87tEggH_stCp3JhnaLKjy514rP96Y8A9dex2eqWl77-ILoOWuF7RXPRRzwZHeF5133N3dX770FKyFspGlRg11fDp8_nAj_tLj2XVN_84_SVqUM3Az8WyI6kX_0CiW2ZlklyDcGCU3joTJOTIcGu4URORfGLQpDX2uIlj3K47-CRwCreRT2Dqvqa492wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
قرارداد محمد محبی با باشگاه روستوف روسیه به پایان رسیده و با توجه به اینکه برای تمدید قراردادش‌اقدام‌نشد او بازیکن آزاد بشمار خواهد امد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23822" target="_blank">📅 12:18 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23821">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q11I4z3TQtVprnvbPuT6LHy1i53h5srpdnppq9YS6zRVCkh8LgPFa7YcFYWWuc_xcRY2_N5dExwgeBH5Z9LG7V1IQEbT9AT0DSRkWX-kfpkdRlzjaS_rxHcy0jfWDN2Jum0jGB0MY9L0crXB4xeSt_Pg55LN9d_Oo2ck4eDEc71DSCpF5C0jzxPF_nhB44Zg5RFdUk34lJEAbH-09axm2vSCzRBsz6WRh5ondP9HQdFbl1aI2jKgXAo1rKJ64Bfxo4X1rsUNtUG4yqddN6TnO7E1zF_8DnzXvD-9ovIMHm_4U6226VadHouhCbx95F34X_x4H__zqRtrn250pYbzEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/23821" target="_blank">📅 12:08 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23820">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=WbYpoEXsTEYrqF1DWt9d9nkhPldM1Um86Evzq_EP7B4ve6kv4aS4k7ndd7_ino-KIV6Rliy_wVk0yM264TBq86ByDOEssX0kti0DJdcJHq0OYZ9CUDQpwr7UonaCRgWeVAoEx0ddh1fLHAGQ08tWqz_0Je4RN7A9LrOduXoR1yy3ks-4rQeQsKZ1ClvCHcbAcM0QTSfV7OEnVvO2T6qEtqM3noDNBS7nutxmN1J7fWWmB806a6rdbM29vZgYdci6mJbYuPFVQ5bCRGm2ZUEohjTXjZiQoHrs9K1GQYOZ2jS1dFCuXudV_fZZ0miDWeaD_YfvgZgsyJYVypvarFsEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4aaa4b5d3.mp4?token=WbYpoEXsTEYrqF1DWt9d9nkhPldM1Um86Evzq_EP7B4ve6kv4aS4k7ndd7_ino-KIV6Rliy_wVk0yM264TBq86ByDOEssX0kti0DJdcJHq0OYZ9CUDQpwr7UonaCRgWeVAoEx0ddh1fLHAGQ08tWqz_0Je4RN7A9LrOduXoR1yy3ks-4rQeQsKZ1ClvCHcbAcM0QTSfV7OEnVvO2T6qEtqM3noDNBS7nutxmN1J7fWWmB806a6rdbM29vZgYdci6mJbYuPFVQ5bCRGm2ZUEohjTXjZiQoHrs9K1GQYOZ2jS1dFCuXudV_fZZ0miDWeaD_YfvgZgsyJYVypvarFsEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌حنیف‌عمران‌زاده از نحو خداحافظی اش از دنیای فوتبال:
یه‌شب بابرادر خانومم تو باغ بودیم تصمیم گرفتم از فوتبال خداحافظی کنم به‌خانوم هم گفتم یه‌متن‌بنویس‌بذارم تو پیجم، صبح که از خواب بلند شدم از خداحافظی پشیمون شدم ولی دیگه دیر شده بود همه زیرش نوشته بودن تو ادامه مسیرت موفق باشی منم مجبور شدم خداحافظی کنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23820" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23819">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=FlJlxj-nwmeKxydcH13aDUDRZRXle6fVK_K5CSGcjC5jdmQI9S22Eqm2mFZ70rCoVdzWGqBpNmOZhJ3q-qFtRDV9MwxBMYUFg0zGcjhIYKEUT0gUjOMMu0QGCi5DYSakZf3TKyKheY3ehxJsf71qHyGya7wFX6BE_6mJ5Xti92XyT69SgYmfsyiWuvVmDLmymt5NLHetwg20Qt_-21D6w8DVi17AyfJBtq0LVuOa-ythiKaO7JxQedBa5kaJBFuy6Tmf0A0rFJHRYyUhFinsqjlBVx-EC5aay3URwJoP2RkaaHBPslF7ojbhL0eT7jtnKzxIZkBocEMFxNe2yJcQWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bda6868e35.mp4?token=FlJlxj-nwmeKxydcH13aDUDRZRXle6fVK_K5CSGcjC5jdmQI9S22Eqm2mFZ70rCoVdzWGqBpNmOZhJ3q-qFtRDV9MwxBMYUFg0zGcjhIYKEUT0gUjOMMu0QGCi5DYSakZf3TKyKheY3ehxJsf71qHyGya7wFX6BE_6mJ5Xti92XyT69SgYmfsyiWuvVmDLmymt5NLHetwg20Qt_-21D6w8DVi17AyfJBtq0LVuOa-ythiKaO7JxQedBa5kaJBFuy6Tmf0A0rFJHRYyUhFinsqjlBVx-EC5aay3URwJoP2RkaaHBPslF7ojbhL0eT7jtnKzxIZkBocEMFxNe2yJcQWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرونده‌نقل‌وانتقالات‌تابستانی رئال مادرید با این دوخرید بسته میشه: 220 میلیون یورو برای جذب مایکل اولیسه + 120میلیون‌یورو برای‌جذب انزو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/23819" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23818">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چرا این روزها همه سایت جهانی
MelBet
رو انتخاب میکنن
⁉️
🎁
شارژ هدیه 130 دلاری اولین واریز
🎁
شارژ هدیه 100 دلاری در روز های یکشنبه و چهارشنبه
🎁
و ده ها بانس ارزنده دیگر...
🥇
متنوع ترین آپشن های ورزشی
🖥
پخش زنده مسابقات
🎮
بیش از 80 نوع ورزش مجازی با پخش زنده
⭐
کاملترین کازینو آنلاین
🛡
امنیت فوق العاده بالا
🌐
اسپانسر رسمی جام جهانی
💵
واریز آنی جوایز با بیش از 30 روش شارژ و برداشت،
از جمله کارت بکارت
🎁
کد هدیه 100 دلاری: Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23818" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23817">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZrergXwrwcNhcEWp_0LWq99AwEgXFRYCGsZsQeZEdXAf5BUFRQHejuAn9GlUErDcMUdckXx1x7Dm5wQ_tyU2accMlU84XdGy0ATlSWkatoHIaG7LBkfg2qSBPPjlqDmQe1yN5qYVUl5VeW4XAfSUauiuAe7lpEB3iObru9LlwwpHqX7cTnshwSz5Ta5HiD4LZP6yFdoVUYQsiGVFpU6u0cvDoaD-IUCiE7ULpSVJmXktIsSmI-G3KdWhpjmywdyMu_HWlWZ01DubiwQBHh4UbeGX8agidVH5CHvxHTNUdd-SYjdDsDVtmBynJc4OkZwPSBj9E6c-LN8I8jMbF8rQ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23817" target="_blank">📅 11:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23816">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=srJUr1FTwBwv6LF4AvlOlX1HMqSV73ZcTwHH6K7Tc-wAhr2cYsOsuAIlipuUzWC5-33iZgNmobOjac-uhm_CfP8UGr4UA5VIIWxbj1jlT7KeOWkHJmO11EvgG__5H-jUHoFQM0z47NphS2B9fw6Dcd0TcCnCAb7iw-xkHIZpwVX3hF-GlUiJ9IcP1k1gV6-fOSo5iuLFHgCnUDzv2aapG3pySi2CEiMAlAVM9FTmP1hDQp7H0mZ91jQdI0jztPM8BAfgAMYw4HzCJXTsXIIKLj6_qerSSMv2EPFAEh_0b3hw64KL5oj_mKP7wphIK23od8AdOI3AgkDx-BFFZenYkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ee7c7274d.mp4?token=srJUr1FTwBwv6LF4AvlOlX1HMqSV73ZcTwHH6K7Tc-wAhr2cYsOsuAIlipuUzWC5-33iZgNmobOjac-uhm_CfP8UGr4UA5VIIWxbj1jlT7KeOWkHJmO11EvgG__5H-jUHoFQM0z47NphS2B9fw6Dcd0TcCnCAb7iw-xkHIZpwVX3hF-GlUiJ9IcP1k1gV6-fOSo5iuLFHgCnUDzv2aapG3pySi2CEiMAlAVM9FTmP1hDQp7H0mZ91jQdI0jztPM8BAfgAMYw4HzCJXTsXIIKLj6_qerSSMv2EPFAEh_0b3hw64KL5oj_mKP7wphIK23od8AdOI3AgkDx-BFFZenYkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رونالدو نازاریو اسطوره برزیلی فوتبال جهان:
"به نظرم اگه یه نفر باشه که لیاقت اینو داشته باشه که جلو بزنه و عنوان بهترین گلزن تاریخ جام جهانی رومال خود کند، اون آدم کسی نیست جز لئو مسی؛ مسی بهترین گزینه برای داشتن این جایگاهه."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23816" target="_blank">📅 10:49 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23815">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=HrYJGVgRXo3_FJFLOT273JNq5TGwS_BhWcBPlBoYdBAGT81e2vIXVDt2NbOo2OKpIWs7va1JP0UUllYOhOaNIhC4dNRFKUMC1XgZG4bzKTXLsOqObe6hj48F0ALKdjUVRyfkgrJwdznJdoE9ii7ok3N9WK0iOhyXzAKMkHFZH7y3LbnLeVfWzbxAA7wfVVtdq3ggDrvH0EFEgPdocUNkP5GohA4PGx1xL_n1XGnT2YNZRlenWtQEPIIpYiq2Jfu9Us8up5a5Kx2lVZqRKW9roE2_L4NUHOPSEsSFtxED5wDZYqMsArzpvB_LNz9UkTw8vdGNVZMg3Lj6g7dqPr9NaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8463cba5a3.mp4?token=HrYJGVgRXo3_FJFLOT273JNq5TGwS_BhWcBPlBoYdBAGT81e2vIXVDt2NbOo2OKpIWs7va1JP0UUllYOhOaNIhC4dNRFKUMC1XgZG4bzKTXLsOqObe6hj48F0ALKdjUVRyfkgrJwdznJdoE9ii7ok3N9WK0iOhyXzAKMkHFZH7y3LbnLeVfWzbxAA7wfVVtdq3ggDrvH0EFEgPdocUNkP5GohA4PGx1xL_n1XGnT2YNZRlenWtQEPIIpYiq2Jfu9Us8up5a5Kx2lVZqRKW9roE2_L4NUHOPSEsSFtxED5wDZYqMsArzpvB_LNz9UkTw8vdGNVZMg3Lj6g7dqPr9NaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/23815" target="_blank">📅 10:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23814">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sTIzqSORO49JvEHCuo3jLYq5B_cADwAp9a0tcDmC8NbZ4RSCaerjDH3JNd56Usp7ZAUiOq9a54FnuxvERq--PO-wxwZ1cYjW8_vSWgcoAH4go87IKqDJyy3DFaDCxq3WyFqIMnLkdfdCFgxxk658bhwCp-CG5XUs0zp5uwp-hP4yk_YG2Ho1EXyl9UI78-G7lz4kZ5uD9jXFd72zlsFwVwAK8EJ0RzLPbzEOztMn2e5bqMmoDkmDqBqG8ot7NjF-GNQPWVAKchtGB8QNZgMnugAOPbRsmyCYeK2ySbQ9ucfAqJUjKOgjqlogkdE6aS1-L5HFzrnseUWfs4-lHlESOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعداد فالورهای وزینیا دروازه‌بان تیم کیپ ورد از 50 هزار به 3 میلیون رسید اونم تنها در 5 ساعت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23814" target="_blank">📅 10:26 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23813">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5uNHsS0WwJJw0om5xGfE_7oVNErR92VDXL5Jos5ANIvArnvu9rD05cYgH8MpOfS1YPGMMzIoi5q34gE3oMFRkdUnQ6HQwYpM29CnDMLEjH_hcsaNYS3pukzLsLfAUPCdFQ-S_pNAnFe5SPdaHgG5ZGHKiD8eTwqkJ_N5eZCD6iJRlzq913PryYB3sPm18lju7qfUP3fy7OGRLmm6p8fc5IX-GMioqoUTFocRiCX3gXOPOEwwJzIgfXAwr6qgXH-lhXjzeF9ia3IwbDsjUhNgk1FLeM8rmMMZdNJDk4UNVU4I6azFY4vyMGIV98IQRuF62AaYpFfcXy7x9z1s3p15w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باتوجه به تعداد سوالات زیادی که پرسیدین؛ لازم‌بودبه‌احترام هواداران پرسپولیس بگم که‌اوسمار ویرا لیست بازیکنان مدنظرش رو داده و از بین اسامی 9 بازیکن که به مدیرعامل باشگاه داده 5 تاش رو قطعی میخواد حالا اگه مدیریت علاقه‌ای به همکاری با اوسمار نداشته…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/23813" target="_blank">📅 09:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23812">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">📊
نتیجه دو دیدار بامداد امروز جام جهانی؛ تحقیر سنگین قطری‌ها مقابل کانادا و پیروزی مکزیک مقابل چشم بادامی‌ها در گام دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/23812" target="_blank">📅 09:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23811">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=u4brvZJUT3eNSnypJ-X8nvDvk1zuTRyFXtDypepdYD6uUeN8r9ad6ShJES7xbVVsES8V7nW7OqIBnUS6BKqog-XLhi82bgFpe_xclsjV74kgoWTi9ZV2zloB672SeEt-b_BJTfZAdRxNhJZw-L-OKM9BhrHApIcyyDsu-t81StAm2-jVEMCYiNn4xXHYIZvvjQVBi9Z7eSw4xTPlgzd222PZRg8DkQJywTPLCos35FqbkvqX-mGQ29qhrgyhICZf_xfPi2KKei1JNLTtefDxD5XzIkFEX7MyM1K7uDafYyVGI_XHdcL2RFt3glfi9m-3j4CuUy7liFFjUMEzJAkTuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7641de3fc6.mp4?token=u4brvZJUT3eNSnypJ-X8nvDvk1zuTRyFXtDypepdYD6uUeN8r9ad6ShJES7xbVVsES8V7nW7OqIBnUS6BKqog-XLhi82bgFpe_xclsjV74kgoWTi9ZV2zloB672SeEt-b_BJTfZAdRxNhJZw-L-OKM9BhrHApIcyyDsu-t81StAm2-jVEMCYiNn4xXHYIZvvjQVBi9Z7eSw4xTPlgzd222PZRg8DkQJywTPLCos35FqbkvqX-mGQ29qhrgyhICZf_xfPi2KKei1JNLTtefDxD5XzIkFEX7MyM1K7uDafYyVGI_XHdcL2RFt3glfi9m-3j4CuUy7liFFjUMEzJAkTuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تاکتیک‌امیر رولکس برای‌بازی درهفته‌سوم مقابل مصر؛ صلاح و مرموش روز سختی در انتظارشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23811" target="_blank">📅 09:36 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23809">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FmX5S8EZ3MEix1jfY2D9n9W672Q8T67QvNwpfuHI3iLDaeCd2gI_d9SM7C33DONOh00-bcCpTJkdPXqOj4MCkiU-2CwkhZOL_ZDnfnf117vrTNp2J3yZccg30quLupsiWt293tK1OwohFfxC-iw-NAfYHTKrmFhbKYXEHEaAFJyuca8-E1GUz72OVPwheyeqWe45C9WQc3C2BHTDJ2gA7CYm9dsnjbp84SDpMG8sfuLpBBAcn2plTsEHeqCUILkt0vRZpHYgz1GNduitaVaUE-bAEd10pqtZ27BkaYPFAPZiRa9gq1IITN8_o6PqplvzI55ygJ8mD0Sem74DygH5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WowI950kyyxqsebwbCZgu1B3TwDdlHip6LTLC-T5FuQxA_adZT-p-5ytNW6CMlf8mv8XNEKCXwzsgAndyQhACpYmy_7ceFopy8OQLkpvCDFsOuRsGop7lh50dQAdcNdwH6IOdtFqKatM5zRe8q4pJaYi-QMeHjYJHlG-OC6U0TpCNYHYTFIJXiKlEv6s9pQVUVzRLSoESIaMWatyp4dcNXeyEmuw6-J5OURtx38d638yTY4Q0G1IHHY1DllJOkvTkr6ubxgrVcKk3-E29YHNdFgZr2HNW8fpW_qi-4W8lrRO05jyFAMz9RRL5dlJLSlP6aPhusBZRufCJoxrQZfWIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌ @Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/23809" target="_blank">📅 09:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23808">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRLAiEFwAshMmFC0MucuAVvb6xdqsCM1GbgfdKMIVskn87k00kCfwYB-P9F_ekJ-KGQGK3xI_I9Ow3i1hxbX-0hxv5wc4z6w6KLs8KdXV4AH9oyXWWPo3N3QyAW0pL92Z7p59HqYI9zWn0lJ0uSyRIanijPxNAi3plJbHzTObXYC4MlXzdSeUcR-CeBm2_UOgcLd10A-8T8DVO0PqxjVzBPeVlpxrTGP4a3O2jlYPB2pYl07VXj5YFRosdb2-cMhvlEEcZ_-RnmwpW_4sip18JfEXl-4S5iZIiPSD84Q9UeqaI9Sh5vn9YaOylBpwdwNK9g2gz_AtzoIpe3gAfqSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/23808" target="_blank">📅 02:38 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23807">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=bZboP-ejO3f3T8T-u96bwH1LEqu0NMVY_qLYcpLbUTD9HDE_l9EiyUme8Rfi9n-yEGqi7eAMm4-KYObrS2UqC7fMhNRDfhJYknSlp9d-s-g5L0SvFWx1iDie0I1hueBqbQ9nD0dDFWTaKmRRWd2ufsRtW3sZW7dfsaVyVeMYyEDA75AeWA02Uov67_NX15VcnafDOoT27Tox5SDgk_NbU4ROMAadIEFzp_Lao_Mqdsaeq2-MKheXMF_KBgudzs6XRmhaUp2vKh1E456NsNPcG8z-V8wNFUvc5g2ys0KgGTYdGmfKlfwvTbSwlFOTPfWqbGLXr7ubyqE9Bz3Y9WNBc7_nUelhDYylndgKaQ0c9qR30xu263Tf2Oi3a9a3eA1K9858vR8GvDcHObsGaWeIcE1xv5cvd6nguVzekiMD0wTtl85uYu1Qi6Q2srf7NQnzjWrtGR5c3U7uskA96Ig6q4_v_DcnYRucSsTe_PM2rGdP6alt9pJS7mGOCpFTRr8D_wZYNjXeO6nr8S1PshjiScEYMibSnj6MJtZ4d3_n4f13iqWvxkR7fcq-dVv4h2G_zWSt7SZ72ty4NFBiDPr_EAZ0gw62iC48JRQNjdWYHern_ZUsHls8ec7EOX_KIRymPORLHY9XJXpsjOt4oCHe_gBEXmiGRR0rJGXLOFpdG-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ab6b2cc1e.mp4?token=bZboP-ejO3f3T8T-u96bwH1LEqu0NMVY_qLYcpLbUTD9HDE_l9EiyUme8Rfi9n-yEGqi7eAMm4-KYObrS2UqC7fMhNRDfhJYknSlp9d-s-g5L0SvFWx1iDie0I1hueBqbQ9nD0dDFWTaKmRRWd2ufsRtW3sZW7dfsaVyVeMYyEDA75AeWA02Uov67_NX15VcnafDOoT27Tox5SDgk_NbU4ROMAadIEFzp_Lao_Mqdsaeq2-MKheXMF_KBgudzs6XRmhaUp2vKh1E456NsNPcG8z-V8wNFUvc5g2ys0KgGTYdGmfKlfwvTbSwlFOTPfWqbGLXr7ubyqE9Bz3Y9WNBc7_nUelhDYylndgKaQ0c9qR30xu263Tf2Oi3a9a3eA1K9858vR8GvDcHObsGaWeIcE1xv5cvd6nguVzekiMD0wTtl85uYu1Qi6Q2srf7NQnzjWrtGR5c3U7uskA96Ig6q4_v_DcnYRucSsTe_PM2rGdP6alt9pJS7mGOCpFTRr8D_wZYNjXeO6nr8S1PshjiScEYMibSnj6MJtZ4d3_n4f13iqWvxkR7fcq-dVv4h2G_zWSt7SZ72ty4NFBiDPr_EAZ0gw62iC48JRQNjdWYHern_ZUsHls8ec7EOX_KIRymPORLHY9XJXpsjOt4oCHe_gBEXmiGRR0rJGXLOFpdG-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های‌سنگین حنیف عمران زاده به قیاسی که سانسور شد: امیرحسین پا میشم میام پارت میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/23807" target="_blank">📅 01:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23805">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKlRFfv9GJhD2l79MkUkFI0on1LkxqnKUBo_x-agPcUWzcYbPLjjPov6jnWkGtvkpaqZHbs-ba0iZuRr_mwt0epKLlNWvfzmeG9NCfJ-iOvygJbmrjCGskWS74q4T6GBQHuXHNOwVBmoRn6redimU_pvXaqbcWXUvC_pBhrF7DTp7Zn1WYuVw0ho_lHrdY8Xd_tXNA4SjpMRkFn6E_iIhFs5F9112iJqedt6P3sl3P-cTiy82aS5A-_BIEonTMrWcAPydGfZRZAmCLEzzQZikTj3EBjCLPxbxJJqqvgvX8NtsqTyyB1-NbsKSdd_wTVKkfEC3K80kSJ0X18-ORSFfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از رویارویی کانادایی‌ها با شاگردان لوپتگی تا نبرد آمریکا و استرالیا در سیاتل
🔵
‌
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/23805" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23804">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfLmfretm5e1xxNrBtTm8rVd6WIeIOg7CzAw7uliY418i3UpYFSciiPXjk-EfYyotrvWW6aGHUOBQTR6cp0XdN5sbD-XJzmRayMXZ6Tttd8xXVgM650ushSZm3c4TeJAhTtQ0Yv9eHPC_-_2BbgPCaDxGXyT1MjQHuIjA7RWFFxhk2Ng2OibflGg3pOPYSXXSJjhBq-XEzNksxIx_UBxptWrD9fdbjUxfWFWNB3iCinBrhcHXF384_UW22_tR8DrUmCPhcn7EpWCBMiG9Jx66unH_8T1LaxB_GN1D7k4KQkaVfXRZ1Wr38mEa4IBZrInIorFu_-UlXkz-sleT7ETkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌‌ دیروز؛
برتری کلمبیا با درخشش لوئیز دیاز و پیروزی‌قاطع‌یاران‌ژاکا درجدال با بوسنی
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/23804" target="_blank">📅 01:19 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23802">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=Wy7JfxIGXTPVK3Zr1OXRA-wXIY9qMf3ShY7sOyOp6VTemH5mXEs6PfRyXbLUqMOBLE5n-hQoJhjOjdme1alfoq7KcZ91O21ZS3lsfvrw2TOxr6XR0hqgvkn1d05AXiY_NDyitVWlSPPcIO37BbANOpB51IjDnYvM8nwMAUW1B_3VOFF8hCO0QO8CauUKA540VE3A_8Z11CpWC--pzZemftPQ5qfKzSUOZA8-wmFxe2ByYD9at8adeKwxbnwJEPGx4cuz5ZnnK0uBZ2lRFs_rXlK1AOpap6O7QaPGU78nBcKAqkpZ0pNntxBn7FbUcYqwzljHPFjZ61_hzj9DC9SPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bad87a3f4.mp4?token=Wy7JfxIGXTPVK3Zr1OXRA-wXIY9qMf3ShY7sOyOp6VTemH5mXEs6PfRyXbLUqMOBLE5n-hQoJhjOjdme1alfoq7KcZ91O21ZS3lsfvrw2TOxr6XR0hqgvkn1d05AXiY_NDyitVWlSPPcIO37BbANOpB51IjDnYvM8nwMAUW1B_3VOFF8hCO0QO8CauUKA540VE3A_8Z11CpWC--pzZemftPQ5qfKzSUOZA8-wmFxe2ByYD9at8adeKwxbnwJEPGx4cuz5ZnnK0uBZ2lRFs_rXlK1AOpap6O7QaPGU78nBcKAqkpZ0pNntxBn7FbUcYqwzljHPFjZ61_hzj9DC9SPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آرزوی‌جالب‌خانمی ۱۰۴ ساله که‌تک‌تک جام جهانی‌ ها را دیده؛ برای تماشای لئو مسی، چهره‌ای که خیلی جوان‌پسند نیست! همه را دیدم و مسی بهترین بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23802" target="_blank">📅 01:06 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23801">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23801" target="_blank">📅 00:52 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23799">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTbr-uRUzisg7Ny7U7DBeGslS-l379WrWTKK9AvJjhXa0_ql_k0lzezJUhw2GxLJ1FPV5McO1GHcyk9RMWmbUC3WbQKLYVnJV9Cl5W53W9fNNuz5bDmPSjgmfybOcPK18Wv8DQYICYrM5ARXknVFL3O62mKAqEByumIILaFWzPCKd0R2hLziWQjNYmKOr94pG_cI7DERPefmkYyLBhxghxk8NwKvPWv46-iBPQbwzhbsYDOKMcR4nyb0KSAHbq2KvzGDXpoy7HXYBtM_QuwO_snLyx7PqaEd5CjyuLdfLmb2qafgKVo_R2y0KrQSpaz1hcI4pIkgIGIDaM3ZB-9vbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FZrH4PBZVTZheE-LfFu-C9605YkYquPIWJ2GDt6EP0E3TGdnkLc2Sv1tXkzGQ2irhgURTz9v5BrAByDwfLKSNfyE2foKgyo1x4TFe0m9qssGF_9OCWEcBgs4HrJOIGDC7ZAYtF_70hz3Fc6PYLqoKBbnQ49P6vEm0m1up6-tnFc0vbkDEikOVciCohmKzzauChQTzHY52Y6-WrmJAluSmlBr1REZGy4CzSheXJdJ5itjuSGJNAnnWPRPbo_HxhOoUR1DHStxmotzaLiUztWx3n20Ub-NnoA1-mc9rsxF6vGBbGrK5tDlX9HPpAvs2wPLIiwR0lYLlP5Z9to9SsWNgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دوبازی هفته‌دوم‌جام‌جهانی
؛ تساوی چک و آفریقای جنوبی در گروه یک و اولین برد تیم سوئیس با آتش بازی مقابل یاران ژکو!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23799" target="_blank">📅 00:33 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23798">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTPz9NiO-Fe46-X2xzc7FOCYEpv33TEocpcd51eaqsN1zC4haXZsHnpLl83wh2R9KDtcRlb07J9_rkQp-cd6Yc_NjVkdOD-iuNff3woqpN90WDtXxrNC07J2WGeX_0LPYxdNHvP0RWTnlBzn260DmqrAyDLpdiGpjBArQV7J5dHxx3SZGGE34fhAeip0_lkohtt5ZJrHyPKtlOP9KNZDIZjJG09m9Vy8dMnctIbH2Z0L6mNmtyyJ8FwGZ788cPyA7mIBgomGaTGnjNefnS7f8syMRwz4M32Id-Mi0eWNfFCvqGIikYPNc12poME9lhA37zfte82QFk3atj-jC9EzaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
یادی‌کنیم‌از شبی که ایرانِ مدل کارلوس کی‌روش به این شکل تیم ملی مراکش رو شکست داد. شبی که تموم مردم ایران دوست داشتن ایران در جام جهانی 2018 روسیه موفق شه و از گروهش صعود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23798" target="_blank">📅 00:25 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23797">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my_uwEai0cpmW_MxZ7-D6N2SB4nvYQrf7YL-yPt_A8xjylFJGm5x6AlCRyVbfHO8XRGZ6aUz69IP44AgnRefi9-d87WgM0JypgQ-arJOlVpL3SfOurhYz-AC0XvDH279d4DeaTuicK9JEUpyIL8I0JS1qXdfR1KLHBjapEHbd4p6LnYqceHSxBKVu3QF0fC8KpLJboEcTW7znWf2ATPVJPdCgZqQpSlXz8sgsiwMWQK5IGjGsYFQsXqQj0wi2FyyT-7OF9taoV3Axqw2iRUfSZcYijQGzWF3qkHRnh5BW9o010Nd2kCT6HwI0H27ojzOgxnjp6TCS1VQzly8VHyhYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛سیدحسین حسینی دروازه‌بان 33 ساله سپاهان که پارسال قراردادی دوساله امضا کرد باشگاه به مدیربرنامه‌ هایش اعلام کرده درصورتیکه باشگاهی او رو بخواهد با دریافت 10 میلیارد تومان رضایت‌نامه‌اش رو صادرخواهدکرد. قرارداد حسینی با سپاهان برای فصل جدید 140 میلیارد…</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23797" target="_blank">📅 00:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23796">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zdabmn6ATUsiWqkyqzaNlF211XZqcXNP_Yqlwkwisekw7eOiozntNwHWdUYQFRtERta1hUNcfXkFZlTU9c3iHN0rL_P3-e_ZL1VTmQsUpyzACPDNgqhYf9irQ5pfwSg1cadg00P_0lGI9KbHvWxNifkfJZEC5u5KZK_GVgHfY-fpRHJ1v5Raq8MUzrwKrQS4AX6HtMBo2zwiBO0GkwH54T1NV308UzX4jdZrs3q52c1e8n6VJeBmC71UpePE6Lb5NhxoiMbeBzZWZDCeu338J5uqjcIcQo4uTSoQFVOOGpI1uVR7wErvSM7P3uviMrhlIxT1_BXheST1fwNA4XNQgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
خوزه فلیکس دیاز: بعداز توافق شخصی فلورنتینو پرز با انزو فرناندز؛ کاماوینگا و شوامنی دو گزینه پرز برای جدایی‌از رئال مادریده. شانس جدایی کاماوینگا بیشتراز شوامنی است. درباره فده والورده پرز گفته او فروشی نیس بهش هم فکر کنید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23796" target="_blank">📅 23:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23794">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdKdM9lzMaGwJAuLQOYcrzJUz8DFQ6USKwULNtZ4qW48_zN-CKvFIy-85DQhwMFOW4pAQSNJnvyKGYJJQS-TZx6tnrqtcwSnoOUYgOw-_MlXVGSXvQyMhBhwGYsso02XjHW0NFdq-1LANB9BTCZ7AQSNCtWBEaGsGHm6HdkDPh_8hm85y0KdY_KuMBMeaO6jk-XyiMZao4YteIDCDOWzJyZErPh0KvfLmSKYT9PqF8WVVx5HaAcDjbyNAWtJNAG1YAVPH2tpB-ikDKRi9QHyMnM7p1gohOq-bmof4PiKRRSt5xiMAWVRmaUdE6TUdZGyS-tL89MkSAott0kNvXhXBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2xpxnAUU0_PT-TedBsMwZ6SMPTM4MmcEvIjxxL8Ame8o3kG9C2hOcIyPwDlvvYKByLzaOUX5nLWJKnJgtbQjocz6C2NqBOAlQWwTbV89srYQXkTtdSAOOTf9IG00hUyqvMnUWRAlY_YgyDXmz5gXpFmq1kQzWNvpDbDOokn6XS3RtclU4dUNcn08bAyh95-SNAM56n_IeZQHOD3jLIpzG1_HtD9LLUNOpu8fCp2xNSUwQlOpmc99JBfdVQFuWuH7idZtQeLkF9M53VsBlJgLCnuHGttGDOKrc_xHUs4RvkAgXodAeB_n48uXnQgVgRG29NHRBE7xIGjm4CYYh5DNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
👤
ویدیویی زیبا از شاهکار فوق العاده علیرضا فغانی دربازی‌ شب‌گذشته فرانسه مقابل سنگالی‌ها؛ همین‌عملکرد درخشانش‌دربازی دیشب که دو تصمیم فوق العاده گرفته ممکنه باعث بشه که از همین حالا بعنوان داور فینال جام جهانی انتخاب شده باشه.
‼️
دو تصمیم مهم فغانی این بود:…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/23794" target="_blank">📅 23:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23793">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sun4Nh7oZr_upDR0TDozfOwu9vjOXLe6L7dBkBBTEJHrfYkGEGbeFY75FYomFOB8J8-LhCWg7iWxoGvgDB60xjhl8sHkRUMy9ybj78LIDu-YXT8gx9yFnN1b98sLYPwb-PsAiiVKllC462aRl6-ov_aFm3tA4zdAyBKZHaAZ6z1XGpS0tu6ynO3NomNPKLaKsP6JHrAkpCYgchaNcFAJbC6unT1biDgomwsjlK1kkgUbfWqYKA-RseTMOpv6HPr8nCM0r1HfGSzcIcdZQRmmR-gt-mbZ4OXlTglDbMAAtgAEPQdO9HRac59Q9ncGUldv6pbRs6rKi_ecXFevSqKyIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با جدایی ریکاردو ساپینتو از تیم استقلال؛ رامین رضاییان کاپیتان دوم آبی‌ ها در پایان فصل به جمع بازیکنان‌این‌تیم بازخواهد گشت. رامین رضاییان پیش از رفتن به فولاد قرار داد خود را با استقلال به مدت 1+1 فصل تمدیدکرده‌بود. همچنین وریا غفوری نیز بزودی زود از کادر…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23793" target="_blank">📅 23:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23792">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKuqoQasVS7wIP_VMFo0R4vuhMvMYbw2HycVnVvJQ15iqusfiGDKoF-0M-iv6yAEoJfaNjXPtKLuWaQUedRsZav6i3n5vr6tIv6LQxYXyRcYIjF-SBzUSl6wB9Egkf0ozERVkP7k1Kmr9pEFyqikNGHXHT4gv-IrM0jIAkZGAclHCJvTA-r1i8HGsw9p2U3Hx12arHALV6z6iR4KRC38tdidhTVVu8XkgLEqfoSV0QFnSpNi7vtNHiaXi4nW5uTrDOLImuQtxcEZvr3rbbFyCJ-inL0eO5qcfiDb3OQDO8CtQK5-u-RAMrbj5fyTSRn7OmbLlZ4olxpfd-ip8dCqZ76YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4f7a0d943.mp4?token=Z9iKBpbiv-1UpSs3P-KgrYb2PivjRKPyAuui-E4QlkXmmuGuQaNcAQ0O-UKrWHGhShUou1Ix38ikezkoM2AYLV7OHczIJLXQjP46esBWEKHWtqrYlzLTS8FavpAx5fncmK_ZNubENK4Q-X1kP4hG1gLHlyepF-RcJ8WOiwZLuPFWgxgiHHESsFub8FR7Fo7qxq4moJgqhphq9ywFGTs8uTdIQhLdrtkY6t_UwcETHcKbat8SFG1HnhVK4uWBbEb9dUaTse1ad4q4BoqdCjRJGP3Ko3YIf8-qbAzBbR-Y0RzOUxLlYCUHybp0ny45-Xoc777czIack3rFCjn0-jfKuqoQasVS7wIP_VMFo0R4vuhMvMYbw2HycVnVvJQ15iqusfiGDKoF-0M-iv6yAEoJfaNjXPtKLuWaQUedRsZav6i3n5vr6tIv6LQxYXyRcYIjF-SBzUSl6wB9Egkf0ozERVkP7k1Kmr9pEFyqikNGHXHT4gv-IrM0jIAkZGAclHCJvTA-r1i8HGsw9p2U3Hx12arHALV6z6iR4KRC38tdidhTVVu8XkgLEqfoSV0QFnSpNi7vtNHiaXi4nW5uTrDOLImuQtxcEZvr3rbbFyCJ-inL0eO5qcfiDb3OQDO8CtQK5-u-RAMrbj5fyTSRn7OmbLlZ4olxpfd-ip8dCqZ76YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
خاطره‌بامزه‌حنیف‌عمران‌زاده‌مدافع‌سابق استقلال از کتک خوردن مقابل بی‌آزار تهرانی؛ حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23792" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23791">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TAlFip1YnvJIkaMHKqEtP8Wbv0mq33d-dLO_RQsiO2lVnV7FnokxpQ2RraBCzo1or8N4A6sN8uIx_1fjBw8BzDyjH391m_iYE1Kb6uzIqO5dnm0J25j2w_nm2TerNxFS7Buu2Q4s1vel-BJCD2IhqoYK3sCbJHHEXFxFV1myc8_RUKkA1jx_WGeWe5XhT5eymHBNd_iWYqTzm4JrpYH5RNqmp42GPTAq52z83-NE8CEaPeXwQL7jPYQqROpwpG200IhcsY7SVAWfzufLgzt5IsAH-CvI-s6xfSSOBktlnnwZxf8lJ1XrC5-Kjh_gzknXa34dzwZaxyncq4k6Gm56Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌اخباردریافتی‌رسانه پرشیانا؛ مهدی لیموچی از طریق مدیر برنامه خود به باشگاه پرسپولیس اعلام کرده درصورتیکه رضایت نامه این بازیکن رو از طلایی‌پوشان‌زاینده‌رود بگیرند مشکلی برای عقد قرارداد با سرخپوشان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23791" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23790">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q87IAM5S6L19RZ-BByrEcsoYXFXkf61U4W69smPglrmG-xJNnjfktOshA5H11GF0mn2X8l0EPfuDf-i1V2H9JRLkM-zH3txc9hF_NrcsjZ6o8vjytUjDgsnRhfionuFVH2JvU2UWWG2Hc66DjX-5Azh8bhlA6VWfBPT2PI7uVlN0YgpcGubuV0LNMFFiyL_fhOAevo28vDv3JxDIivLGQe8SXxAGB1AX_o1emIR09nYvwtyF65ysALmZ_P4GX-C_Spm4xpQH7WMLx1qMAQlHvDmznS30McSP5Cv3xaQ4nNx42kFbPSsQRlttnJ_pBVc5IS7ZC0wEvBhfskuUIC-icQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/23790" target="_blank">📅 23:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23789">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/APrRxUWSYEWzFoIxxFVSwK7l1Nt6MLpoEpQjcdmGUI01ePvgrXAaQrS4yJBmNZfXgRDxpx87ZrwC1G5PTDUlMiPdPWcO_mIjrqkcRzyBmuXZf4K4XvhDWlMdvYXm49rz2vZsjewBNO3uYMzhsHXGmmFFUAsLIHxkfVpFUgSsLNn9mk8yIYa6AMospLjATKmS2TPwvyRCGUBMiHlxDv2y2jYWK53vmixzKqu_T42ZxDUqyApfLX-Wk_YWbZCMqyZXrK_IaPdwYV548kqB9vQJDw2oH25o-FsaJdEuayD-3D0AJthHyJmthCFnAdTTFQkRfp_eNbkO7yUPG1mXqvYY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
همانطور که حدود سه هفته پیش خبر از علاقه اوسمارویرا به‌محمدامین حزباوی مدافع میانی سپاهان دادیم ظهرامروز باشگاه پرسپولیس با ارسال نامه‌ای رسما خواستار جذب این مدافع تیم امید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23789" target="_blank">📅 22:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23788">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcYE6nPXrNWWbzx9Bp_za6kfR0BvXcngC60Zf8JIoyNH8P9VWaTHNPUA1mrvJVjBiZfqmNCGuV1y6TwbJo3fyQznksN2zZUvE91_ppxh151tq_sTkRXDFe1Zz2WMJ9zfggv_Dy8MMeYzkbW1mx36SRadW97wOxXh7xDxs0yghbySNC2wHxcRLIl164mUMvoKo1DIPd-1xcYUyC4i2SQo0FXQzqK1H2eyF6QRtYtC0ujRoOYhoISj8QXpNbolMeLAHisKYdYvO3J3ubWSbSnvasqY-ICg1QGyt4VeHo3hnlXXlRf1Alel3bS4UXHammB7fCU6NFts4GHY56gYGgBv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
مزدتموم‌تلاش‌های یک‌سال اخیرش رو گرفت؛ با اعلام از فیفا: رامین رضاییان بازیکن تیم ملی ایران با نمره ۸.۲۳ بعنوان‌خلاق‌ترین بازیکنِ دور نخست مرحله گروهی رقابت های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23788" target="_blank">📅 22:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23787">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XF-ONCwrmdRss21CSDSuJKSP-LXx7hptkCXu23oTMTeRIP0jLHVoUt6oBIYMZYJjgY74KcxsBGu87kLqrM6mu8uSzwQ_duRF8Hxd7ae5tZ0mYsgJgxShxasBar7rSYfrkcwRzNdYjdZ6bDYgMUFwfG8D-B3iDRRHummA3108Duiu7Gx6b6xsgayBFIvhhbY2Zdqs-afG8wdPFJVMSFsE4fbuRHYLOexDZLtcEfIJAYrn_e69dV4GPGA4JfT0QL401DzSNnes5o0SmtVqWcjOs2Bd8CXTjr5a_Negsqr-lSex-2_lN6HMraC2j1wTCUYR5cp5vOjeYSZb0A2hl8TtOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23787" target="_blank">📅 22:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23786">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=blCxmWU6BIENITRgS7McsIJ2eIfAamH6zQsPjM7WAszFdm2ZmB-_Fblr64i6WH2zKATsujxyiQVsuDsQC1lGxfPlsFINE-yCL7azcbVxpWN0SaKbfE8TXGUJmsiWTfv6J4BROJAjvJxHtu7-kgzomwtytrwifgSyLnQv9HIhjfT0uSmsALVOdB0Hy9r7oE923_aTDd8-Z_I_tCGjjbJv4iib5nE-kg0Dxwtte3k0LMKitFbNYyr1i3x1PFWgOGgEEn-I8PEaVfhZJ0hIhv6jFkuBWodunSOh5WxykAMnkCLHWk2Pxn1_oIa38gLnztz4PF_e9CXo1WTlPMRjNJ6WGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef4d39f268.mp4?token=blCxmWU6BIENITRgS7McsIJ2eIfAamH6zQsPjM7WAszFdm2ZmB-_Fblr64i6WH2zKATsujxyiQVsuDsQC1lGxfPlsFINE-yCL7azcbVxpWN0SaKbfE8TXGUJmsiWTfv6J4BROJAjvJxHtu7-kgzomwtytrwifgSyLnQv9HIhjfT0uSmsALVOdB0Hy9r7oE923_aTDd8-Z_I_tCGjjbJv4iib5nE-kg0Dxwtte3k0LMKitFbNYyr1i3x1PFWgOGgEEn-I8PEaVfhZJ0hIhv6jFkuBWodunSOh5WxykAMnkCLHWk2Pxn1_oIa38gLnztz4PF_e9CXo1WTlPMRjNJ6WGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت‌جالب‌ابوطالب از گلر40ساله کیپ‌ورد؛
به تموم دخترایی‌که‌پیجش‌روفالو کردند درجا بک داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23786" target="_blank">📅 21:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23785">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNdaBSFqtNI-qlU3C4xt1qM9I__Qc3DdVWuVLn0CvxWyCzZ-HibpyNjfYobDbpaDwOX9NDqheM5VLW3YN-Yz8MyOzPfvH8vTkEibEu0nh311cLpYOpBKdnQDZ4B3lIfj_ihKgn3aM-JtE6p1jOvTzfhpHugIji4t908ObnnX2wZja2Xv7ZM3agnqzusSXZOd9_R0OXgPvfJIdIZxUxAfLJlu5lGIZCHh-LBSZiROiWqBq7LhtG0FqtjvMDGNubu1sUtV7yj1AonpwpO10hlMDCei2R_n3NO2TzXp1ZlEwWVjQS-lv-PRCIQvyaRuye3te8Nyhwp8X73hUuzdxeUM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بااعلام باشگاه لخ‌ پوزنان؛ اللهیار صیادمنش در تست‌های پزشکی این تیم حاضر شده و در آستانه امضای قرارداد است.  او پس از علی قلی‌زاده دومین ایرانی باشگاه لهستانی لخ‌پوزنان خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23785" target="_blank">📅 21:48 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23784">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFAWAYzzaI9qbFgSb__878M_YdkFKejUeT3BkcwsNllHyXQeMPk6QDbdRxLRhgiDBGPfutaBMGmvbhlKOKB2JrJhVDnaDwbUBxqZlAec81r-_aZzUpbEVKCaomTdls8huDgQ977N6b-p-59zi6Zb2jvcTEZfhzfEVBlUkEx1cZaiRUnl_w78QjgwnDpJ-b9FEjWbjl7UF1sJKih35aD-PTw5x_6R6H-tCj-SYxrrUXqFdcyP8Ka1cuIC9AglgABMQmhhrcW0ipeOz9yJe5dsvmP1XJV_nfw9gKz_gVXRAeS5o6wdWdQlaBsE6VHBOM1DA9g38mYnzR7wRpG6SBqbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#لژیونرها؛ پیروزی ارزشمند 2 بر 1 لخ پوزنان مقابل کرونا کیلچه در لیگ لهستانی با گلزنی قلی زاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23784" target="_blank">📅 21:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23783">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHmii8jk92nxu4TpZo5ZfBXOtqbrRgH_k7YwYIoWGCBl9j0aWNBFXHpu1SPVJK3dz5zGjMG6t1mT7mjsVdL2YhpiF8o1J_6B8q5vEl34STkfq5icietAxRwKzM4eRyBEyt1wDkbzBoztxiJiClC8K3r6xLPJ9DH0veHx9VnGrirTih3oiN5etjuYiyrBWOywd1zV6H4bmt-E8Zi__HfaPlm2q23ZxytSbNNc-Ceblc3G3ABu4o94tEriK8jKmgA7bfHgYWco41GSSsifm28iRplfZpG-33J6HrDrYajSWgzYmhvFBCxWjHstBwIxO4Wv2dh-8oRM3nkBREEOdedXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ارزش‌طلای‌موجود درکاپ‌قهرمانی جام جهانی از سال ١٩٧۴ تاکنون‌تقریبا ٢٩ برابر شده. البته این ارزش دلاریش‌بوده.ارزش‌ریالی‌بیش از ۶٧٠ هزار برابر شده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23783" target="_blank">📅 21:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23782">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ew4CEvTfcmj_RyexCuRM2tccJArbq3M404C0epITomANMNV5x5Pca0n8GXcyvQY80YYViD9K7f8atSk0e2rHeuVrmDfwPa8zJoUlmaryPhg1SrGr5U3YhOD7tZ2eHZB-j-CNiIlo6Epm9L7X96ds6hJNQOauISpOFF9y6wPtwdyymxvP5twz4SmQd0iIAIjpS95npw7RMlV96hWTEGgOJdN1SqoJ9JKELqqNlc-DTTMnuLd-lrvCpVed7YfeNtkF1jqVBGhMDND_wqovhAbLLVCC1CXTPK8xTie4aydR1o__JgiBX2MmlerMtYZyhqraz7mbYWGPEEDDYJGsw8pMWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ جلسه مهم امروز پیمان‌حدادی‌مدیرعامل‌باشگاه پرسپولیس و اوسمار ویرا دقایقی‌قبل به پایان رسید و باتوجه به اینکه مالکان این‌باشگاه با درگان اسکوچیچ به توافق رسیده‌اند به احتمال بسیار زیاد با اوسمار ویرا قطع همکاری خواهند کرد…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/23782" target="_blank">📅 21:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23781">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">⚽️
👤
ویدیوکامل‌ویژه برنامه امشب عادل فردوسی پور برای رقابت های جام جهانی با حضور مازیار زارع سرمربی جوان و موفق باشگاه ملوان انزلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23781" target="_blank">📅 20:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23780">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCw1uDth5i2g2QOi4I4saVS21gkoDf9Ix178wVehW23BI4XVpBuXZoGzPaFVJ414wzgSrBXBVSQrDrOVSe0fHrHTJo-yohGJ9RdlnjPLp1f7ymexMzp9TABNdSHeBEXWZhZ3bNLwhVaJzRYi98fqrBd1sqFz0jwqW3v5bDGHPgzzcXKUf6EKMUh2OxkJlMbmqC6P2b-iAfbjY5VtHt9PTRdcY1x0uuo1AA1AjWnSfkrZRKonzjla8sqsVdjX4i59QRFSkDt0EdRpThpPDbBLKbWLeyz-EgLwMrPkiwApQfjWINHKMi3mFxaNzzU8MzmnSmNRZqJT0acd4Td_STKtpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری #اختصاصی_پرشیانا؛پیرو اخبار روزهای اخیر پرشیانا؛ فیفا روزهای‌آینده پنجره نقل و انتقالات تابستانی‌باشگاه‌استقلال بزودی باز خواهدکرد و آبی‌ها قادر خواهندبود تا بازیکنان مدنظر خود را جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/23780" target="_blank">📅 20:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23779">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESaERtSECeWEkiaFDR2-DV2sbG-PcKuq7Mo-XViN5lQ-C70mzXCNS5yx2KsxxSdoARZEPYHGi6cFR7u8uMlUrw32N-tma2iQQUPXatUpfKjOZE2PmxJOHC14wIsKZjxttASHJt5-rQmM8hgUku08gxuzjSzUMhISLriUxzsfvf02u_DKJFqDULamKU6eg_s-ZABKYhQH0ZQz7vgdYBsW88coZ4SpJxS95gTyar6i1V3vNCG3bvhyyV8gNHXvvlZwIPStrBUxzScanH17AmqrXpoVNnTICEJMGRfpwGhB9pYlnIn9Z4eCLwcDW5sfpqO87THp3d-GV9n7VOtN-5b6xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته‌اول جام جهانی 2026؛ پیروزی ارزشمند و شیرین‌شاگردان توخل مقابل کروات‌ها درگام نخست.
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
4️⃣
-
2️⃣
کرواسی
🇭🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23779" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23778">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwnNjXPCLBLuoB6NFgjqwfyC6Apc06KzaWLhziNOej-GSLZUM2Z8Q0iZW415z9i0zPTZ4EKzfsghI0yHPV__qb6rWdvXDD6jqrgxedffTUIljGDJpv17cpf-bvr7IdOHTm-F157Hyucp4YPHppCb23CWXmzSrnRm5vp3zQaPDPW2wajlehty3B7BgdjJZowCdxUIqWBQZV4ORfHKH3pwszgrgFEKCnbvOhNz29Blw4kFLheEsu0TxrEqb64hk75KddCgHrnIdOhRxEOVHpCNBYGBG35BW3oQ8qXLPV8npSIBkbDvt5M1Q9B02ZzW9Gv6v9O8nbdIp916WaoeT5FhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ ژوزه مورینیو برای‌فصل‌آینده رقابت‌ها مندی و فران گارسیا رو در لیست مازاد رئال مادرید قرار داده و قصد داره که در فصل اینده از ریکاردو کالافیوری ایتالیایی و آلوارو کارراس استفاده کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23778" target="_blank">📅 20:38 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23776">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krgefUomvoJ_76Jc4ZH_5NmJUm8Y-zxewVia9cvp4wC1SUCwkebY_4EkgG8nzerGjG65-LF6kzmwjU_1NxsTRTd_uuCc5VLOJKCcmzVDo88rRJkm7_3H1RNJcVprlczrAPwMu1QZ9zTvMRV_y5HGetX7J--1qGkd1-UVBrXcn1O9-ozuKNG2GJ3Yvg2VuxMpNAwEWBf8zwbrmgo2YYOlbRY5GlNqCzViLnXSqn-AZvAoVe9w6afMXn9ds3iFOj9PckVjLciCFbZa7Vrx3gw3qsSNbsiXAYUAxZTOzF9X_zaHtVDkF5A-B1yzsnwbt-43TlNfQkrdV7MJhMkI54CFJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23776" target="_blank">📅 20:23 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23775">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=MEC-RKkd-QFJc7hOxWBwMicGi68muVmOqyCdJf3wDY5TVyLWOdi7HygYWNajtlZL0Ry4TYZUqJPbnAqEBTlmTzULyXS6GfKhKVI8KpLVJlJw4GDfudaA-cz_g-63l82Xh52yEUkYzHZ6_bLHS0cpULlvx9q2sLzjF4BBUnWuV1uhMYKTlBtKHNF6FV-UD8RBH-OJ2ITfNaQgmCA8yePgTtZU0ai_19xnrgQR65jey5AZWvEXkos-u5EhyAFFFEEDrfuogkocAH63P43K-5_VO9BAPJoIc0wO0wKLz_W6e4HPQzfswyb_hPPjDlfHJpcH-lKMSOdAjTYf28Zcgfiqqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceb72d8ebf.mp4?token=MEC-RKkd-QFJc7hOxWBwMicGi68muVmOqyCdJf3wDY5TVyLWOdi7HygYWNajtlZL0Ry4TYZUqJPbnAqEBTlmTzULyXS6GfKhKVI8KpLVJlJw4GDfudaA-cz_g-63l82Xh52yEUkYzHZ6_bLHS0cpULlvx9q2sLzjF4BBUnWuV1uhMYKTlBtKHNF6FV-UD8RBH-OJ2ITfNaQgmCA8yePgTtZU0ai_19xnrgQR65jey5AZWvEXkos-u5EhyAFFFEEDrfuogkocAH63P43K-5_VO9BAPJoIc0wO0wKLz_W6e4HPQzfswyb_hPPjDlfHJpcH-lKMSOdAjTYf28Zcgfiqqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هنگ‌کردن‌خداداد‌عزیزی‌از رفتار جواد خیابانی؛ از خداداد سوال میپرسه بعد میگه تو نگو تا خودم بگم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23775" target="_blank">📅 19:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23774">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFGCZ-YRRowx7gBpk_o8gaAy2ak0zUqskulJ0EcTue5BrUGEhfRjFXyqYCwGJ0fLpVZo79uyvTmysmEcWQfnZk7FGAZIgbnopMCz5tG1ozOhIAtIt9Z9138KKU6Ri7bumM2BD1WTzfU6pe_5Ux9K47TKt-1AQjZzQQiUU3NSRoTnUiaKJ8JS2dZAZ2QZknJzUH3bSXboWv04VlGcutYAkDTwarBulgh0dJXP_wupk3HJ3N88tmm5-AH7SFVzzQK1uD5lAouLAQlE8XbfS2kRIH8kdvb9NZ_qzRagK03XUajg1muhE0PT9UfZHEh86cT0IJX9iCK8lDIs6MLdF2VXqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23774" target="_blank">📅 19:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23773">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYf8JSBb4Qt2y5LLGLGLv0me-zorA3mjvFsiX16hgNC5WrQb6R9Rjv6LR4AuNkDwRJWEjInkEnp2s6AkJJTYqy-xZmCzwQNr8eBQAlw1-lY7zfeVBBQtMjzu8UNMIVbxz3A0kEjyuUornfxOTxILcu1yBNgLL6iGPFj_soKlBiE0lXuLcSLs1OmTyqD55oRgeTx7g2rKU6CDNds0yV1xENZFnG9NCqu7NTWycQ4PFKusJUQGNgSMgFGAJRdMuvl44tD86mLdHgM5WOchqsR2mC4mipqrvI-i4whP9zNP3UEWdxkySZFe-5lha1bPeRidhnJmStiSDsZ0R-JUEjuPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
با‌اعلام‌باشگاه‌سپاهان‌اصفهان؛ آرش رضاوند و میلاد ذکی پور قراردادشون رو با این باشگاه تمدید کردند اما محمد دانشگر حاضر نشد به باشگاه تخفیف بده و جدا شد. رقم قرارداد دانشگر برای فصل جدید 170 میلیارد تومان ناقابل بود که کم نکرد ازش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23773" target="_blank">📅 19:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23772">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4AlLeCTLVfYr3_vV-J4J4Ggg1xt0O8mqRmFzjrVpfvpvvl64D9ujYDhQIv9SfDqZTvBYE7l6wmYu-SRV6oycxN0Z2zAd_1xPWWaoK_2MTWumKW-NalcduXcIoLfyxxikj5ZQlyi7efK7VpO93GvkjW8It3poHnCelt1u1zKp8R8VCmSfYrYIAZ18UxkAjeduSsPUjSxg4li7mB1sqJsylT7tgRam-u8RDpnRmDdJaw4WimS2oCkTaz7wwbsJd6fXp-bp3iC56zZpSZ2KEjGyPn4wrjmD2msKUD2MxkewaX6bLbEUrXuq0VUzOG-jxtCZzReHhLfq-IS3zIYoMIIQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇧🇷
👤
برخلاف‌ صحبت‌های کادرپزشکی تیم ملی برزیل؛بااعلام‌‌کارلو آنجلوتی؛ نیمار جونیور فوق ستاره سلسائو دیدار حساس برابر مراکش رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23772" target="_blank">📅 18:52 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23771">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOYjG5oXpBQDAfyIqjy_6MQV_WMCHYk_zelKFAJJf7jhELrojPOC4clwoyUlUyaJUr7wqaIXMftkCpatI7tiAG7QBDbGXHKfYS-BUtgcru37QUh8ezs9VdDJFphiBf-XnXqXmX9mB60rJCMMzGuNrugJyTHHnBRMBJogGxXX3mfWB-5dv7shfuHjm24p_KwBFxsCPiQUsatZDr9aQapLyiNbPxHAjsJ3VO3qbFUP_2k2axlC9bPvQ-LeLH76_0yNfv2TpnLVb5vIa-q8a9KG-3EtDBd7xiPf6DDT4hXDfrnyMU34Q0kJrf-nYoToRG4QHDS7XvXyEv-jCz3JF7HtPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: ماتئوس فرناندز ستاره پرتغالی وستهم؛ منچستریونایتد رو به رئال ترجیج داده و به ژوزه مورینیو اعلام کرده که نمیتونه بیاد اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23771" target="_blank">📅 18:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23770">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tb_UirihGGIxG5zkl2rfv9TRZXxc4dF_b5zQgs5Dw-nwb8ehm4YSwRjIwD1GtEMsrKJQjN1iQecBG49m7YItuFQSRmkcTymOQZ1hbKflUsQfZ7CL6eWLlyZ4Ya2FxppEvgdZvZ8F_j1v-kGx_7n7S6GH0GN5oJzlVKX_ry9A_HhTBwJ4byKpGaNFc6vwLbNeXSeX1P6RD7Mvh974313PTUUpqSjvkIdxMFVOIfqw2OfEUTp_fkLXpzthE4I6CTaRMHMIdmwl1Y8DZhfWz7MLQE9ePloy7dwGB7dFprz0ueMAvxxw7KoHShGnoOzUImkXx6Yy4dCoiauVgfbN2gjk5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مارکا درخبری‌فوری: باشگاه رئال‌مادرید میخواد بزودی پیشنهاد220میلیون‌یورویی برای جذب مایکل اولیسه برای بایرن مونیخ بفرسته. با جذب اولیسه و انزو فرناندز پرونده کهکشانی‌ها بسته میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/23770" target="_blank">📅 18:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23769">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSxGj4WxwLJ8b912IJzVQj95-ZtyJWLeMN1RW91JD9ItTJadNgSVTduiSXHbxR36Bi2v3GABzA_Tmwwh1M0H6acXZW1hYCpcqV7pbxboIvJzfYuQP7ydsWwhpCJwfwPzkF97TWcn_dDH5i2ZCj2O8uBQNOffIzKd04AKFa8CS3EXlEktTBmlspuNZ8a469VuECMXpFTxnMXaDKH82odBOooMKlS9CXTG1iDw1xVPvXyn9TVvOW-iYCENqSJeyfFP_UpYa4R5jpfju1IwHiTibwWuEZcqWJvIi1xDW4uimgnZd8kJhUeymR81sAIiX_XDgCFrSs1hKB75dWh89qHScA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#اصلاحیه؛ برنامه هفته‌دوم‌جام‌جهانی 2026؛ بازی ایران
🆚
بلژیک ساعت 22:30 برگزار میشود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23769" target="_blank">📅 18:00 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23768">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=YPS28edeQoD5ULLoaDsluK4sJd0SAyYGbDz5O7W0mmP81yE87mj8FHzHPZkOJHJmGkODwcTS5-T4DLsVSwiMYkuZ9bp4QQtALvj7vFSrA6pTd27zAXuBMjndU9ShWRCWMfM9wCZZMF4B-frl3VrN_RZPvXc5WMuOnRm-W2DPnjuJFcR_5Hk4-gmv_TxLPqCnHomKPiBagcrAIHMjdNe8KwGhxJPEmSRL4CjqkAK-Cw3_8_b4XkC3iIIkJEBdxUWZvHq5zSdS7zdJTCwj9AhzDJQ7TR6rZDwTlqD6Si39bdoG42hdJg3uqYCUQnSPVU2kQW3E4M0USwyEsEmNisUMNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/629abdf2a4.mp4?token=YPS28edeQoD5ULLoaDsluK4sJd0SAyYGbDz5O7W0mmP81yE87mj8FHzHPZkOJHJmGkODwcTS5-T4DLsVSwiMYkuZ9bp4QQtALvj7vFSrA6pTd27zAXuBMjndU9ShWRCWMfM9wCZZMF4B-frl3VrN_RZPvXc5WMuOnRm-W2DPnjuJFcR_5Hk4-gmv_TxLPqCnHomKPiBagcrAIHMjdNe8KwGhxJPEmSRL4CjqkAK-Cw3_8_b4XkC3iIIkJEBdxUWZvHq5zSdS7zdJTCwj9AhzDJQ7TR6rZDwTlqD6Si39bdoG42hdJg3uqYCUQnSPVU2kQW3E4M0USwyEsEmNisUMNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌فتح‌الله‌زاده‌مدیرعامل‌سابق آبی‌ها به میثاقی در گفتگو باپیمان‌یوسفی: مواظب باش بعضیا صندلی نداشتن اومدن صندلی رییس رو صاحب شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23768" target="_blank">📅 17:40 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23767">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqri6gWWno7WlyYPn96d_dhBnTDJtpso117NWW4rKXC3B2_9Kh3cpxDLK4JxaAG66VKQPaNua4guP67OE2CyNJXTQYCpawQLOW2khR5VBLCj6R6b33U8fHbIz_xstvjrsAtMUj3WOv_AP1rKpoiDXzMXbLlBaUetx5KcoTkZ4PjaXpOfbdesUm1tBTjeLiDntc9X53_G_NWA4wXxEq67jIa2YWN6UKExw-kc_9FRQyDjwFgPUaBpMsedQWZXgSkvpWI5952a57pQLqNh4e5IQ88CjB7iUTxigtYBaZjEdao7xyypVTalbfvPXeOwGiQcWkOCvHAwjzbiC5bS70FNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
خوزه‌فلیکس‌دیاز: فلورنتینو پرز رئیس رئال مادرید به مورینیو قول داده بعد از اتمام رقابت های جام‌جهانی 2026 تموم‌تلاشش رو برای جذب مایکل اولیسه فرانسوی از بایرن مونیخ بکار خواهد برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23767" target="_blank">📅 17:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23766">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KtPfKp5sEFLP0ZfwYnL5cNkd6NhLZwuek-KmU3_zhpCB-FGq98-x18iWcRMJkPln7Zkx46BpcrwP7cOUeHOiNXFQfmJvEN76idFfmvwyHZLXmuUXVJoA70jlEGkETn4gyaeY6LuwvgAG_7tNPhA0I44w8qtUsKbuML1Iolf-WXqOe6hqv0SstSkpPc4KRqCFYxVfQuFZZ2DPHkrvWTkMcq2TA_t9Bwu06JHDiHvXXg3D1XfgwGV6O461Ubgo4g2ZhTAA8yuW77v0EE9Cq5Wl5jVnsuiX0HE6nwctFmjUdr-5jzPoYo4IzevmMqvcFs56LOd2jFnvfgHfpB2R01nPiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد چهار بازیکن بارسا و چهار بازیکن رئال در هفته اول رقابت های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23766" target="_blank">📅 17:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23765">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNrRAm0KIFXJ25MsW1MvB7Mt_gvGPf1nCW1TGjP5YSZu7180p3EcvAeRcuNTHrHXIzBOUh3huC7w2G2zXBLW2Tr2isE-zccJ3R_b0jNk4C3A0qTpfOeOS6BwZuM0spMLVb4pVmXyGppbOHJ2dsNGYL-O7nNyjK1nIe2iauCORR7siubrQhYyroRBXRfCqji0_0e_rOfNcCvrg9p1zh3zqWs2bItwOEWLTdHj8vClflCezcetnWxlaP3EKjcxmk5kcZU3LcQCNI6t0jmH8X37ESAuehJ3tz_Sah8pb6bxrz9y3FaqSkyJ8OWybpmueozEGt4GOTjWUH5uq9vbEkh2LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌های‌دوره اول جام‌جهانی ۲۰۲۶ در یک قاب؛ از ارلینگ هالند و لئو مسی تا رامین رضاییان و علوان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23765" target="_blank">📅 17:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23764">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgFWtNCIRmjSs_qvDs-se142KuXitewAhMuM5XjJ0Itt9-WUyHHYAvboCvhGIy8WWg94GuEceS3FVAFXJpzK-LCVmw2DQCI5tUD-3XLyFqccflM6KVoC8wPyDJ4F-4ILG2mTkKgL6_IYwG1gKZxapn6E_rxcwHeHstGPTXtWPjOAo1J3Zm1JYrwTvzTr8D86YX6RxL9TSwgcLV2bQrZl2F6G_mJFLQWcuP0nXnh9-y9C8dKcmyV_1GqVzhiIWerMZdJcywuNFgWZqpZjSkgORwvo7otTqTVhSpTwq3N34PFZxmtE35nX51MGSbCsWrT7_SM-YydqxdUjfxVr6z9MmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
خورخه ژسوس سرمربی‌سابق‌الهلال و النصر بعد از جام جهانی هدایت تیم پرتغال رو بر عهده میگیره. روبرتو مارتینز هم هدایت النصر رو بر عهده میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23764" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23763">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A069xT8WUsjUekbBqsJv8NQlKD2Abd_I54n6_2PZ5XIJwDGHc8D4FGbDRdHwguRl3pd1c2qOMkbC1BTiFqGSS0leN4W1RFdW_Cye6sulcY1lmlKUfG_y23a_NZrLJIhECtIKn5tI0bN6aCuPBITCsZZEgHUz0ukz2lBaDOSZmZddySAs9ELQrBIRNOJ7gN7lx-w_JG1Sg_RJfr9j3CedOmAsWuYmxP1fUbxNWHvellr8QnjSs4HuOkXShuXCZ5COKfUg53v1wXB8oPhCRlOHjPNEX1c_LXGG71FBJdjMJiRx34CCh77PAzOHccvlqsrfBgKhCcQqCtGLBGbCIzHR3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23763" target="_blank">📅 16:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23762">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kasnX5Jr3GNT2GU77Hn3O59PnGFlBoxLpG4yWxelcNqPAHNVZNSXZ4pM6K_bt76Sgt1Ypl6jKmU_jjaJ-zjnsghez2ShEjy3D0optigEr-j7dTxuLbCC4mzsqS-JXvTVSCytBR9pbT4Zqk9dbDMCnDUTOm0sZf6VG0jP6dY1vbyT9a3RMVJVb7KNbURKt7y_NVR1zmiSoRB2_2PRQ3rmxISmStpvthZ1J7oeUxbbwwo7JgXwtpgq-vxXirG4OPGYIGTfB5aOFSheUpOEEEXHEbmELNmKwovLjT8aK_UtlJdJM4voEF7Qg_20OAYBpKFwf3cBRCYsaNyblWeb9jnk6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق اطلاعات به دست آمده پرشیانا؛ باشگاه روبین‌کازان‌روسیه به ایجنت ایرانی که ارتباط خوبی با او دارند اعلام‌کرده برای‌صدور رضایت نامه نظمی گریپشی ستاره آلبانیایی 2 میلیون یورو میخواهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23762" target="_blank">📅 16:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23761">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ataqt395iDt53NX0S6SqSrJhyzPSDzt4N2dwE022kj46rhx0AlXxrFYZG1AFb7FPuPS4M9VVnJ5v_SDZ97yCxhnGjigTMlEX4Yf2rB3hhdudNI5HPztB2P3CjydK7qknx58m72W7uurQ3ZkndN2AClAU7ym6bXOSh181KqHElnDUKVf695QgSjeXIeI0W259nJ2XfENMhdNoQKMm-_Af_PCBOIo49R7Mb-yiKUI7PUATduY-rjuzN3NR3SbipRsCHfgVEryb40-5iooDpYUimWg1NfrYtp_O_pMFwoKWEPHgSxi7RCWeeJoak_8OyswKr8w9rZ0VRLDEUltHXIW1vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه‌کامل دیدارهای هفته دوم رقابت‌های جام جهانی؛ این پست رو فعلا یه جایی سیو کن و بفرس برای رفقات که تایم دقیق مسابقات رو بدونند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/23761" target="_blank">📅 16:10 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23760">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIRVgKW1benkLrmTUo0TwYtdDfBculWRjEca5jCPTpcP3qmRZikzyUVysWxu2s_7mx0iXDU8qhZhbmxMVpchijCvKsl_kOGpC81JIo_ndY8Jz4DIgxd2jGRJLuPaGXSUtdUvhZBsC0BZyLPFC21g1IFDLGOwdcNNk9IexqZ41vkNlqxF8ZVawUD-Vo-tiJ6E35dWGMM666GV3mfOlMKra1L7ZtvYaC1hyzgLJD-XLwc94WFh_hwlXJwhE4pYVr2X5oig1bcb_zpnTjdfpsNpoY4iTuvAYJYB-cJN0gxLytJFePdQnIzQCDRuIb6gC22BEfA3JF-Scwa_UVfcnC3gPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
نشریه ESPN به نقل از مارک کوکوریا مدافع جدید رئال‌مادرید: انزو فرناندز به شدت علاقمند به پیوستن به رئال مادریده و فکر کنم در این تابستون این‌انتقال رسمی میشه و انزو به رئال خواهد آمد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/23760" target="_blank">📅 15:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23759">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSuDfXEugZwTDqZxXiffBFHzF0yN0Y01OqaW_28EUFo4W0k88h3rqfUy2NX4P-4Lw7CEngfuKOx5KPS2CfKXMIg3KWQnOtQseXnCH8aTpIyVdHnFFxmSgTvi4AYg9xwDuIMpcnUxJLfHR2rXypwGiB_xqYjbKcdxMF2NBqJykeCYidAYCy-_jBNl1KgvKZKlUuYwu6_xUSVyp0WQMBn_CxPV5X-k_rhC2oCv52JsT5K5thJYBgKiLhxLIO4JhXyC2JKA6Wb7lJCh-_opxOHMFh0wj_iW3SETTQZN1GTT0G-fawsDPVpPTYlFr9gZzYlppgY4e2HWJjV8NfiRwCZgjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
🇦🇷
#فوری؛ باشگاه‌رئال‌مادرید برای عقد قرار دادی شش ساله با انزو فرناندز ستاره 25 ساله چلسی به توافق کامل رسید و حالا تنها توافق بین دو باشگاه باقی مانده است که این انتقال رسما انجام شود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23759" target="_blank">📅 15:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23758">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=pBZRSyfZeeGd4bDB_0N9ILTonzx4oEV08auXTuuV5ZMmIfmTCzdYGsmJtpWTjdKnkhlhsSbnho40Ltfuu_Ss2qMFA_XhYDsI0GceRdKZ2pkFmFrzsCwAbV0WwnNYMnXBRxkSGCfOLmOl3yn9NyL0WahtB1Nj3Uc2g1PXZJd1P4knl_B_AuA4wwJoKYT7_Gndo6mVgskNlZPFNrk4bxTcv3MZVmJVt2vMtFmJA6w_EkQWobxRBUz9LC2PJ47Gui852fhgWtj-Bgpd6FIoGp5qa6CVIIjO6TIKKpW-rkqunGBTJ80gV5fbdI26nqiwuRIFYGWM2nSyH7I3INlw0jA0pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e3fa7271.mp4?token=pBZRSyfZeeGd4bDB_0N9ILTonzx4oEV08auXTuuV5ZMmIfmTCzdYGsmJtpWTjdKnkhlhsSbnho40Ltfuu_Ss2qMFA_XhYDsI0GceRdKZ2pkFmFrzsCwAbV0WwnNYMnXBRxkSGCfOLmOl3yn9NyL0WahtB1Nj3Uc2g1PXZJd1P4knl_B_AuA4wwJoKYT7_Gndo6mVgskNlZPFNrk4bxTcv3MZVmJVt2vMtFmJA6w_EkQWobxRBUz9LC2PJ47Gui852fhgWtj-Bgpd6FIoGp5qa6CVIIjO6TIKKpW-rkqunGBTJ80gV5fbdI26nqiwuRIFYGWM2nSyH7I3INlw0jA0pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
آندره آ استراماچونی سرمربی سابق اینتر میلان و استقلال درگفتگوبا DAZN ایتالیا از محمد محبی حمایت کرد و اعلام کرد شادی بعد گل او رو پیش‌تر از بسیاری از بازیکنان حرفه‌ای فوتبال دیده‌ و معنی خاصی نداشته و فقط یک شادی بعد گل ساده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/23758" target="_blank">📅 14:44 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23757">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXnY_r_3d2sdreJw-4E8G6ZN2cloXG4o_EuqJMX_yam3VoJULBFL8eUEdpn-RF2MF1HA0NTWUDDEPZq_mTBsxE-6syxXr1C2pmfcqqzVm1SAA-kbn4JApZ1aWJEBCvRKfWxjSeEgUDuEBSf6273Sv8ozCAMKfuwdKw_sbPdzGYYjtFp3-GElK2bcPL7Rxl6FEn0rPK0HYtDZHXoDlkPBVJSsFdUCRJoq-Y0_I8886wvDrxw7h7eVr-rAf018hgsSyI659oS61Yj0iF-v8dNO2IUdDwyN2VCygvTg3lqwjwBcbOd0r2IN7Pr3Li9GkAEDXeic47FoH5gj3VFASRVTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/23757" target="_blank">📅 14:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23756">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDvU4pKrFE6q_Q6DKts5UateWj_zsFpSnQTuY9FBwIVl2mKBnfqfXIi15x6apRa5e5tduS4L58wBqsEp6Na3uggcPR2zHCZPmh9g19UgRDIJ-K1iM63l2ZlyBI2LnF4J3ur2xZekb29vbFi7X1-W44-da9JNsig2qZqJZT-pYE1-gA-RP8_GKMlUCzwCMrJQRgwBDOg3eAvrIpr27c57bvb_TK-h_PccuepIbvoLNlOd1xTip06HTeuxouoqWGPbfo_d5zvsgI1S5vWqCpSCxAclbXz2rphs78HYqpnfBVVvKvaURk50VHkVu6sjgtqu0jEj9bNH6A7AYjCpIzJyaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسماعیل کارتال در گفتگو با TRT SPORT: آماده پذیرفتن هدایت فنرباغچه هستم. مذاکراتی با باشگاه داشته‌ام باید صبر کنیم ببینیم چه پیش خواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/23756" target="_blank">📅 14:13 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23755">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YG969iuTKxOdcBvtREQVzlH5WAfrFjhQK0RAFPka2urf6fBOy8U02iT0jNeZxvNeGvvesCPUGL3EnToRZM9WohSItBwlPIXWo14b_M9mt4QIxDt6pnSeOhdARmzdzsG-Qmph5APphpfuIcODNtKE7ETiRtpjWBeZAFI-Ev-jAkj0xRseSmds6GWhohJ6_z-gJTwQXIXo3bzDaGVpjaxVzryYD6wCDOqJb3RBQBhaTmdjlrK3v3pvsOJILCzH_oNGqiFIXBN00EdGKJm4OaRZZwYDW1MwqjOLC5EeY7Y2gCiWAy9P-LvtReBuCq3_SEuyR-KjnaqR-QUoGwX1_2Nv8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای‌فسخ قرارداد توافقی با اوسمار ویرا برزیلی به توافق‌برسند سریعا با دراگان اسکوچیچ قراردادی دو ساله امضا خواهند کرد.
‼️
مدیریت تیم استقلال در ابتدا مذاکراتی با دراگان اسکوچیچ داشت اما عزم‌ علی‌تاجرنیا برای اوردن این سرمربی کروات صدرصدی…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/23755" target="_blank">📅 14:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23754">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4mw9Sks9tXtraHHyrUVCXjDzpeJ-ZOcL26wW0TEsL0DuomHPqIqOxYHx-zlGxnlAadzu1RhAuVdIjceke65kuVp1Eo2ED5ZkD2AidHy4z1xjnzYJByEz4_M3jO9Yi83zuxaRymn21HOp8cBnI4L5M2K5pYQDv09d0CgUzROjv82mI-y82RZlW5wIm-esfAG7xJNjtbNoAFrmp6NZkeUbOYzjgsZXsvGM63z4PfaYrbEGZnxSvtHsn8GfqETluTkvI_vuU0cocvSIgapl_Htp9u8L3UjOEZ7Oxj-4Fo1x-rnI_YvTXkB9aTKzUPRDOtW3VkDiKD2ANfW_AnjYTc7IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جالبه بدونید مثلث خط حمله بایرن مونیخ در فصل گذشته؛ هر سه تاشون عنوان بهترین بازیکن زمین هفته اول رقابت‌ها رو از آن خود کردند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/23754" target="_blank">📅 13:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23753">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxVHe4cXc-BYASIaboaX8igCjRxglpXp-ePupCEW3SafxcjlynwR7lpyskvhMrt2hDqsAFLu9cIC_pIxsYBhiSu_1gjQQkVYMYnl8H7jobqmJwz6WQowhdOXLWWX95RpAeT-6Opl_lPNXvpRoeeHVrZjlqfrtMYxZRot9Zhy16LA4VatE5rT35UM5e1YIBBcVjVtz-lHV7eqGuc3S36_ltik7VI6nI7l28zh1xJbfrC0gZ2MUO7eUFh_iNxNj5-Qgmi5xKGpy_C1fBxaOvjbTQ7ZHcuCzfogIyytIsJuzEo0nt8YY0TxY4zIYiIkGrOVqPeMzMOyzPieMxAPHOsvcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بانک‌شهر برای دوفصل‌حضور در پرسپولیس آفر 2.2میلیون‌یورویی‌به‌‌دراگان‌ اسکوچیچ داده که مورد قبول سرمربی سابق تیم ملی و باشگاه تراکتور قرار گرفته. حالا تنها مانع راضی کردن اوسمار ویرا برای فسخ قراردادش با سرخپوشان پایتخت است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/23753" target="_blank">📅 13:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23752">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJRnJ3GZqZFXTFbauWdAnwFubL2PSQClCO33r2O_H_X2itWSHF0eMHxwKfefeJeDDFVoBhV6AjsE_i0GOJHMmKWIaXlFQx5Y7BqSG1soHK4_EUX1u5U4Cr0IqOE5VDjla7n6ftV3Jp-MFUJrXjbEozv2DE7mTiDFcS2KXuztI-oRdyi6-_xbxiu55TdwObBHf4ovZMylR9l7cbS4Emb22CxBQCtd4PTgkZm__GRKIBmi04R57p_0i0awAfBJ12WNtb6Rpn8aJGPsa0rTWlETbBzKfwGpd2zPgIhYz4dxYwyh6DA1eDCu1R8B8ndbm7sktpJfj8dRE5Bejl8kV1hIUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
وضعیت عارف آیمن در جدیدترین آپدیت سایت ترانسفر مارکت؛ اعتبار قرار داد فعلی آیمن با باشگاه مالزیایی تاخردادماه سال‌آینده هست. بنظرم می‌ارزه این پنجره جذب‌بشه از فصل بعد ازش استفاده بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/23752" target="_blank">📅 13:19 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23751">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=fPmEqXxlHS8nUr9OiUuzEAx2agRyyVbPprrRMO9vq2xSpWHnp6SKc2qN2w4VCgGbGWqZgETmd-Egga92usk5RPvEMqPhQx-ETlwGscmXkgjIma1V4yPN5NtJLIrfp7cJoFiJdmTZoEQ1Z20GdtF4MNlofxX_pX_DGS0H3LysWkIwSr2EipzHmeDnmuVshfLr4KqH3oMeywkZ0ehgONrzi27sUv0l99v1O2jDC5Svz2jQDPQihPR8Kx5HxYi7Km-RrJj0cpCV8UW4PhkQ7oNqT5NnfKWLO0DGIcbQ_mLC5pf1nVBSL6yegwEwXKk3i-J_CSxtTqYxxvQtvL9u1ZgUJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10541c5fb4.mp4?token=fPmEqXxlHS8nUr9OiUuzEAx2agRyyVbPprrRMO9vq2xSpWHnp6SKc2qN2w4VCgGbGWqZgETmd-Egga92usk5RPvEMqPhQx-ETlwGscmXkgjIma1V4yPN5NtJLIrfp7cJoFiJdmTZoEQ1Z20GdtF4MNlofxX_pX_DGS0H3LysWkIwSr2EipzHmeDnmuVshfLr4KqH3oMeywkZ0ehgONrzi27sUv0l99v1O2jDC5Svz2jQDPQihPR8Kx5HxYi7Km-RrJj0cpCV8UW4PhkQ7oNqT5NnfKWLO0DGIcbQ_mLC5pf1nVBSL6yegwEwXKk3i-J_CSxtTqYxxvQtvL9u1ZgUJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
جذاب‌ترین‌بخش‌های‌گفتگواخیرامیرحسین قیاسی با مرتضی‌پورعلی‌گنجی‌وپیروزقربانی دو مدافع میانی فعلی و سابق پرسپولیس و استقلال؛ عالیه ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23751" target="_blank">📅 12:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23749">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sr7VIvt8Z0fbODUidRyQ_eqMhj5027MWNsDxJiIOJXBg6k7WtVl04u9Y677vk9xIqKJohr7fgO7IW1sQDNeFt09i0CkjMIhUvs29HL-jjALaNXTDSD5qv2nrlc_zWW-lZRwpGs31MDoVU52Zek2r54Hopn021p3XX2eQVNTTkUObOC3FOJN1SrAM2SgU5wiL5MvWAuMr_dk-WF9fZzM-L4DwOVPI8egl2AAwwTyzpiz0nIRcELNbQAUUGhHgev3DUIXLeAd9HhaMiM9mXpMEVNavl2ReITXfqHqAganw-_iN_oPKWAB4AfQ0-y4NwYu2wKoN0NA_XzPp5mV4TXaOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDZaHZ_7sqgo8bCAYN6vXuXyC2O8MLb5ApxNGS5y20wfr3RJlFt3i8wUjeBJ73N-tkLAYQfg5-VGYUH7gFTGK_K_6hQUaEqF_Z6vHv7WCMFNpIZwIvEZN5ByvMzOICRHeD6fcFwu3W0IoKWNoEgwd-Qwmg9UoUEpQ0cZVYTHz4i2Vi5zzA3goz15MuXcjHgqJSN2n0dq7_jSBKtdkPJa_sEPGiZPjK9TdxykB6IADmBfvGAiUiQv51Kspi63U-eL1Gw27LNQ9yU7_Y2ovth1lw63WUKk7B2FejjWtU0wZsm3AGalUkTmZdKVLtih_pMIkJglz1pf8bjHO7EeDnSxPw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
📊
مقایسه عملکرد آنتونیو گوردون
🆚
مارکوس رشفورد درفصل‌گذشته رقابت‌ها؛ باشگاه بارسا بالایی رو جذب کرد اما پایینی رو پس داد به منچستر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/23749" target="_blank">📅 12:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23748">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jd6ETrZiCoty2Egy_CgCfiEjjvwZBT9drTny5tYFSeDlP_QJeoXm7qe1pECP2noDnnFANlYBy1Q6y0LlXNH077xPh6toogsmFzIKWBiUt_pfHDnQfg0LDSh4Sy4y-NCUXut1qfuUJ7xQFuW9ft1qf9Shgb5A_XwHgPVkontrwO7ChIVIDJSjKOIhDp2jof5NsIQAps85euzxyxSFibH3fnSDOH97XWB5_4JMpkdXRjd0soHZA-Ul5nHSZDwAFHsgXDWSndBGEQU53UAWCqFb6ISTspYAt1WB3bS1vYrgyEm-8gnpiBTW11MwmZjS8H2DjNvDCpzjaFHrrdjDtnXvIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رومانو: ابراهیم کوناته و دنزل دامفریس با عقد قرار دادی 4 ساله رسما به رئال مادرید پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23748" target="_blank">📅 12:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23747">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=VYapcqW0UgBsvIGfIX-S_I_PbkjlgNowa24pqej5jpMeHy5jtNaSHuu8r9RL3aDrtPKPNumZIUr6Ft7VX4JG65E0_2dnTtRW-5V5Cr4Xufyap3_Y1ZlbEPSsqVG4tJNFacUHQERjl2Mty2POXcSboCwgwqWqGDFKhpVUStAt_BaD6T6TBkvjRI5C0Q9DuLWIsJQ28Czln2Or9-LsCYqtD0BApDHKC6eGFpIctsUbLe72ZQjNoWzqSA3gPGP6JT7NcauKdmIuI9IVskTcSKnDV9395hvpb2Q65TXNbXAdxG4O-3M-Ze1IugexSVobHgEhoOhmvVuNnG4HFv6ugOJ9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e75ce8522.mp4?token=VYapcqW0UgBsvIGfIX-S_I_PbkjlgNowa24pqej5jpMeHy5jtNaSHuu8r9RL3aDrtPKPNumZIUr6Ft7VX4JG65E0_2dnTtRW-5V5Cr4Xufyap3_Y1ZlbEPSsqVG4tJNFacUHQERjl2Mty2POXcSboCwgwqWqGDFKhpVUStAt_BaD6T6TBkvjRI5C0Q9DuLWIsJQ28Czln2Or9-LsCYqtD0BApDHKC6eGFpIctsUbLe72ZQjNoWzqSA3gPGP6JT7NcauKdmIuI9IVskTcSKnDV9395hvpb2Q65TXNbXAdxG4O-3M-Ze1IugexSVobHgEhoOhmvVuNnG4HFv6ugOJ9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
رونمایی از تنها سرمربی حال حاضر فوتبال جهان که در چند ساله اخیر تونسته ژاپن رو شکست بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/23747" target="_blank">📅 12:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23746">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kabr6RCmcEhSPEciVrBu4qBxBU671QRW-HSkolLF3MpAVxJnVnusYUEOEf8CBz8QO6n-wGNHcPVFKXFUDWPLRuSpqTpyVgD3qPdt7wG8GqETle8sMZCq17v80ee5fyd84R_IQM_MvHX2zTIIoZvIVNSNvPjW9DTyXlTEiXcs6l5Y-tl2DK_9aL6-mnnWPgcHnrH7a9UNBVQBef40WLSJiYKVbXIKHuxdwU_Yn_6R9k5_RVomUir6nj0z31j3-zHidjy0tJ4-HQbAulE1ULkDmJi0YvPK79ZLo5-3Etav8laBIT5ZjIEC1AKamwE_lh6atMsCKzzKjPaondVgvC47Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مسعود پزشکیان رئیس جمهور بعد از امضای توافق‌نامه با آمریکا: به مردم ایران قول میدهم بزودی وضعیت اقتصادی کشور بهتر شود و قیمت‌طلا،خونه و ماشین روز به روز خواهش یابد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/23746" target="_blank">📅 12:18 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
