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
<img src="https://cdn4.telesco.pe/file/gF2A3lKwkaisNQhpP8hTq1fpplwJXLaZw-Fcv2GG6qOMrov4rvWb9o_Cbk4OGVomY_RL3OrgIx6DsqGlOOvT_vsyzVfRk0Jg_QDNG7RfKZZzTeTnH48X6QHN44a4Wt3SE238iKinUvP6HbeV4IuOUQqaBPcnc3vL0CEhY-4hfjSVwRpopcwmjkgo5qeuP237ikeas8PH-wnA-c9KyGmZkY5HG7qUtwtCv2ePWudgX2Cnw7-QCgoeKs7SesHJnp8I2QBr6JW25APCZvvMdeQg7UYdFwDBPY9TiVkAATqCIagdh9vQcQXiIf2HAOpj5kbmBlR2_ZdnynX_76yFPuv-rg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-26 12:10:17</div>
<hr>

<div class="tg-post" id="msg-442526">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYNUuy4NExvGKLJNdpFUnUBDLjvL6-pwbln-ro7zQMqHnYkRkAG6ZX-FaZx2c09V70fi3cSFCSSQWs12O-lUoHNGaKuGATfrgSxW3_G4dFFts92zi2O0v_Z9Hjar8IAV79GyqsEVk7LXs28TGbUj5cLeiS8wpxAulrlFShxcOnd-uH1KOGFMsU3RAwPC9Eely8wtfozG_qug90aotwJdGy2Y1MiE3UTrN2V29mK-yv_O5IpZKM0Mb74r3DmibUlx6PzvBBr1tvdoLDekqpsg22Jm4VoTeZPDGEDhYc05YSSVlAzoa_TAm3aOusFWNM6HKMDa1465TNSWR1f3cDxlOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم آمد و افق خونین نزدیک شد
🔹
سال ۶۱ هجری قمری چند هفته از خروج امام حسین بن علی از مکه می‌گذشت. کاروانی که از مدینه راه افتاده بود، اکنون در سرزمین عراق پیش می‌رفت؛ سرزمینی که هزاران نامه از آن رسیده و نویسندگانش از امام خواسته بودند به کوفه بیاید و رهبری آنان را برعهده بگیرد.
🔹
اما در همان روزها خبرهای نگران‌کننده‌ای نیز به کاروان می‌رسید. فرستادگان کوفه یکی پس از دیگری از تغییر اوضاع خبر می‌دادند. عبیدالله بن زیاد با شدت عمل وارد شهر شده بود و بسیاری از همان کسانی که نامه نوشته بودند، یا سکوت کرده بودند یا به اجبار با یزید همراه شده بودند.
🔹
چند روز پیش از آغاز محرم، خبر شهادت مسلم بن عقیل به امام رسیده بود. کاروان در مسیر عراق حرکت می‌کرد و از سوی نیروهای یزید زیر نظر بود. فرمانده‌ای به‌نام «حر بن یزید ریاحی» مأمور شده بود راه را بر امام ببندد و اجازه ندهد کاروان به کوفه وارد شود یا به منطقه‌ای امن بازگردد.
🔹
فضای کاروان با روزهای قبل تفاوت کرده بود. نشانه‌ها حکایت از آن داشت که رویارویی بزرگی در پیش است. امام بارها در طول مسیر به همراهان یادآوری می‌کرد که اوضاع تغییر کرده و هرکس مایل است می‌تواند بازگردد.
🔹
کاروان در این روزها تحت مراقبت کامل نیروهای حر حرکت می‌کرد و عملاً اختیار انتخاب مسیر از آنان گرفته شده بود.
🔹
محرم آغاز شده بود؛ ماهی که حرام و زمان پرهیز از جنگ به شمار می‌رفت. اما این‌بار حوادث به سمتی می‌رفت که قرار بود در همین ماه، یکی از مهم‌ترین و تلخ‌ترین رخدادهای تاریخ اسلام رقم بخورد.
🔹
کاروان هنوز به کربلا نرسیده بود؛ اما سایهٔ کربلا بر سر همه افتاده بود.
@Farsna
-
#روایت_کربلا</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/farsna/442526" target="_blank">📅 12:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442525">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">هرگونه حملهٔ نظامی رژیم صهیونیستی به لبنان یا ادامهٔ اشغال سرزمین‌های لبنان نقض یادداشت تفاهم است.</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/farsna/442525" target="_blank">📅 11:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442524">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-OWZNWRFmY0i8uN83rc9VInfXUQqPKRAOzTUclV0qLJCp6x68Hms7U0hS16EMJ8YuDot8kmpeIe-A2uMmKJLQCrygOxxijhrU2TFSDooKNOCHM0mKKLhn8mlTfeNKh2eY87evOmOgxXvQdRBmobE-U5sBKXniWkf-gTUYTd0tUyerIrBndMxYsFifB3EiAaPK20k4sOce9MlYQfHjSgHAPlMxiXq05N79k1PILE0ubkozlBCTWTQCSI5r9YjomeeB6zBtoGYFxwQ1DJ8w3YfIuGsS4nAywlYoGqECYM4dhvm3qMoDxQL_1HPW47v6M1mhhQFExbpMDx_IkytNU6vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
حماقت ترامپ
🔹
کاریکاتور جدید کمال شرف، کاریکاتوریست یمنی
@Farsna</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/442524" target="_blank">📅 11:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442523">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qjJKvtFLAvANvE62K9-AKSHsP4aDr0I5KTMAAa08AiMKor4gY1P8BldYadxBntsKGCVgvXLqfG86fP7Xt2oeWEXhOtU8gE8fjwRhvx8Ch3SW4M4VUfms-BKeAIhavwadmovRTr5SmJGr4AAZNNhMHm0b5qm_jrv_frCVUmqL2dCNOIKy9pAcC_B7G2ZHcAmlzc1-IgZVXGSC7M5nBGLcWYBi-fRuNhmugrGBznLQg-pXgifvU-vJjpkw3ct8OJG9FdGoJUmoIe3mVYTS7vqINwxgoDo11TXZyE1JeHEKA37tSbQEcqkEtc-XwJxfUcAVEiU4CGWpewG5mAyA8U560Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر ارتباطات: تمهیدات ارتباطی برای پوشش مراسم تشییع درحال اجراست
🔹
پایداری ارتباطات در مراسم تشییع رهبر شهید انقلاب از موضوعات مهم است تا این رویداد به‌خوبی در سطح جهانی منعکس شود.
🔹
کمک به صداوسیما برای پوشش زندهٔ مراسم و تأمین زیرساخت‌های فیبر نوری در تهران، قم و خراسان رضوی در دستور کار قرار دارد.
🔹
اپراتورهای تلفن همراه برای افزایش ظرفیت شبکه آمادگی کامل دارند و تمهیدات لازم برای ارائهٔ خدمات ارتباطی در زمان برگزاری مراسم پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/farsna/442523" target="_blank">📅 11:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442522">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=Dcm5dCLMV3cjvzCyNOkzw89ej8KeT3bM_AZOgqltUgi74G72fu5qrwhu_tfdF0sa8TtxiXb84DnwvgoFgLadOvQmV0-PWtxtFJDqY-4QOV--bWDig1MkVdDDbL127iSB8GemJaPIPYHPurgnEIkqCsPmPCCw33npfvLlQFAWjPkpYXutc9REbQFrLNCTGtH4gdUV_rUu1bG1TNSgL4-AwpwlibNqq6hWKzCe7Y8hTBqMcKVeLc9GbZ2CRK4_s9rvLnGCtad2r-Nus2AFqG80s8ESVbCw3qEA0RUX9A6c2kTYKYSrIYUwgI7vWURHZZvcLSo03NG8qL2SSVii4NBwv6HCYU0Z_NwatNwGy3w4tKPJYZSVtlwZrs6FI6KeBkQbnuT3P_3OcsKyikVl4rJT-_-GhoEDmYruF8yh4RgZC9-Z4UnmeLe6DK3LOGYK1fWHOguRn-8DMGeF0uGeLDtVe6LjYGTMozw3v7F6SZZQOk_-mjlMtKdFybo-vyrPjdRQ-Ja_z6h-YL604oi0zBAkaRKXibM-8wQ6xKcwJmjXh4cHzJoeT830v7yXNCPI8jhjsAbJqHKmo948zYdpO5Cug5Bv8KFCF91tPCoNifWmR1f5lMTJPgms500m6oG9PKSYZ3xMQK_qO3yGKZ7VWPgur19UUWxBFbmBCsJhz5NQL8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec0210a91.mp4?token=Dcm5dCLMV3cjvzCyNOkzw89ej8KeT3bM_AZOgqltUgi74G72fu5qrwhu_tfdF0sa8TtxiXb84DnwvgoFgLadOvQmV0-PWtxtFJDqY-4QOV--bWDig1MkVdDDbL127iSB8GemJaPIPYHPurgnEIkqCsPmPCCw33npfvLlQFAWjPkpYXutc9REbQFrLNCTGtH4gdUV_rUu1bG1TNSgL4-AwpwlibNqq6hWKzCe7Y8hTBqMcKVeLc9GbZ2CRK4_s9rvLnGCtad2r-Nus2AFqG80s8ESVbCw3qEA0RUX9A6c2kTYKYSrIYUwgI7vWURHZZvcLSo03NG8qL2SSVii4NBwv6HCYU0Z_NwatNwGy3w4tKPJYZSVtlwZrs6FI6KeBkQbnuT3P_3OcsKyikVl4rJT-_-GhoEDmYruF8yh4RgZC9-Z4UnmeLe6DK3LOGYK1fWHOguRn-8DMGeF0uGeLDtVe6LjYGTMozw3v7F6SZZQOk_-mjlMtKdFybo-vyrPjdRQ-Ja_z6h-YL604oi0zBAkaRKXibM-8wQ6xKcwJmjXh4cHzJoeT830v7yXNCPI8jhjsAbJqHKmo948zYdpO5Cug5Bv8KFCF91tPCoNifWmR1f5lMTJPgms500m6oG9PKSYZ3xMQK_qO3yGKZ7VWPgur19UUWxBFbmBCsJhz5NQL8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر زیبایی از یادبود شهدای میناب در رختکن تیم ملی
@Farsna</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/442522" target="_blank">📅 11:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442521">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dda22ccf1d.mp4?token=ByzGOlo1BubCAbfyISVIA8YyJoorJHvXSmvfcJds5f8DZ5AOK48vQbVPRFQwor08-q3UcIvXH7PdaLCfPIKLQyyXuAm5599hDYA3AlIPXn4uE4A9ZwYQfY5ajXm9r0GIwwwnSKhL4l3dsj9Bz5qGTDTetKVRZUrFSjl-Xar3IRYus5WM_wqulCaB8G2R9jckdIyZbtDxjxi1n2xTiy0E4Bp5ELabb74J06I2gbWr04G_Zdox2K_spJD7aOo4efgFvdEKlDtCqPeP130gDIg1Vp5AQcNquBx-2jvfaXV6EsH7CcsEPkqDbOQyIqi1XVwRa_XQOl7QvxHGy75PGngF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dda22ccf1d.mp4?token=ByzGOlo1BubCAbfyISVIA8YyJoorJHvXSmvfcJds5f8DZ5AOK48vQbVPRFQwor08-q3UcIvXH7PdaLCfPIKLQyyXuAm5599hDYA3AlIPXn4uE4A9ZwYQfY5ajXm9r0GIwwwnSKhL4l3dsj9Bz5qGTDTetKVRZUrFSjl-Xar3IRYus5WM_wqulCaB8G2R9jckdIyZbtDxjxi1n2xTiy0E4Bp5ELabb74J06I2gbWr04G_Zdox2K_spJD7aOo4efgFvdEKlDtCqPeP130gDIg1Vp5AQcNquBx-2jvfaXV6EsH7CcsEPkqDbOQyIqi1XVwRa_XQOl7QvxHGy75PGngF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: جمعه پس‌از امضای تفاهم، مذاکرات آغاز خواهد شد
🔹
در مرحلهٔ اول مذاکرات دربارهٔ خاتمهٔ جنگ، محاصرهٔ دریایی، تنگهٔ هرمز و آزادسازی وجوه مسدودشدهٔ ایران تفاهم شد و در توافق نهایی دربارهٔ موضوع هسته‌ای و لغو تحریم‌ها تصمیم‌گیری خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/farsna/442521" target="_blank">📅 11:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442520">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce85b3d54d.mp4?token=Adyzi4qPDymqdFf8_VoMJeGqYazYX--hU_ElaYyL10xi5d6Dk1e3Iobl3hAR0uMbR2rFcACJ0zQf6pA-M4DCtoostm4FON9fQF4OgjOC-zORaWCr58N4R2LqcsGZhkvt6i9BIucqdjlQG-8oKhSk1oXez6DH_WKFzBgVob_iV-_sQih0FZQvc4fEwnUtCbXFXBI_5pohqJ0tqv8Dfjz--zz45-d1jUaxjCwNj42ntPpHkca4z1PiwLmqegeXEGlGbbSWSoJLmX90w4foY7LhUO9NIJQF7QU62G2aB6whnuk5pJ8g1V4bVogcLar7u8_51t8WdkBs9P_mk1UpM9du3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce85b3d54d.mp4?token=Adyzi4qPDymqdFf8_VoMJeGqYazYX--hU_ElaYyL10xi5d6Dk1e3Iobl3hAR0uMbR2rFcACJ0zQf6pA-M4DCtoostm4FON9fQF4OgjOC-zORaWCr58N4R2LqcsGZhkvt6i9BIucqdjlQG-8oKhSk1oXez6DH_WKFzBgVob_iV-_sQih0FZQvc4fEwnUtCbXFXBI_5pohqJ0tqv8Dfjz--zz45-d1jUaxjCwNj42ntPpHkca4z1PiwLmqegeXEGlGbbSWSoJLmX90w4foY7LhUO9NIJQF7QU62G2aB6whnuk5pJ8g1V4bVogcLar7u8_51t8WdkBs9P_mk1UpM9du3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: متن تفاهم با ایران بعد از جمعه منتشر می‌شود
🔹
این سند بسیار محکم و تأثیرگذاری است. مثل سند زمان اوباما نیست که یک سند افتضاح بود. این یک متن بسیار قوی است و من می‌خواهم که انتشار پیدا کند. بنابراین احتمالاً خیلی زود این اتفاق می‌افتد. @Farsna</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/442520" target="_blank">📅 10:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442513">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ICKNZyYD8kkQBrH4zl3Az_fnuBg7qD6fYIncaVdgKyzrNj26nycS7UdAE7QSbUbX-jbGrPtuEuVEIB_ih--p44SnPbDecMgUiLBKYlEftqbJ5HTLOFI-5y57NuN4DN-98K6wlJR1x9mJ_-PX4NuzvO-tyKRG0x1NEXG025LQ6Xt9DOT_loyrcPbnbwVjmc0gdVpgcM6KgdJmxZV_okCWgBcs2xxUtU_WcE2Y-P8MS_Rsn0MTgEawo8d-CrpSaxmCHP4NcDSccopv0Mxxf2sJSjiB4ZLQceRpUs_HNeNthmJ8ogufKZt0jRnnZWhSOf6QFeFWpxKbY6-Dpx9Sgz5fCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YXn-6p4ffdGdtjR1FZh4pAEi5_E5B0B4Jd4DMF20P1QLSiZSh-Pdb3b3JWCS64jlDjAuUxiso-ayjMlRajd0r010LJIjEiZuc4Kli8DCbQSC79VlrjvlYacpmOFgmCG7YPJt1uveg4wlPxIdeqW51QIxTfX2AreolICkzo52_LoQWiY4o60HPJDo4QX-nAUfGV-E-suaeMSgCkqerW_fmaP4Gbyv7pqvIrtk2XJ3x4QvpE3F5i7A4KW7y97-WIuyvXMPAvR3bf_mhq_fzTLyuoMW5T9XUqZsTc-0VVsiTlt_yJBU1W5htyony9Et7Gc6oPh7HIlGfZku6Owssq1o8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBYRg3tRxtv7-96_els1lgKPUHz-b0DuA8oiPbft54mYzp_Yo7SNCMuKDCWvemRVLM5lYCW7MFgvT4ORERHz8paDX_Tzc3lsg6nCmMKYISG2rvuJ-ZbxeFOKn46ZUn5Xmn_Y-TGDL3FSxnJDHI3OK-exE6-cZYziqdBrcVy43q_Har9eFXsCBEab2S7uxs3vpCrg9ESYdpi5NMtyWXs4b84OB98I2zxU3KDw2xhhT3mnE-Q6520SH1PNPjCb5b0o8paPQ-zeRrWNJb8TMH3_GzIP5-G_OWZ3eTzmpXdzbIHLZ-Rm8y5Lfx9IWAGbwRp0voN8RvZGSweSSM9VEV2rNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6IrpiLd7TqvlfqMvUqLfJBzXUnHo-pTkBV7Oi2q5GQF0U8McJ-GhOrZ7LYovcd9Ae71I12cDRX_Ds3ELRxHfbpQNXvj0GNe2epmT-JJt-dQI2CszQw0MGq3-ponqlZFUJfoeN2gkFi0OglSAeb4UoO-3oUdFj93O6CBrml37hIqMS_SZHhfolTCoINKaOubLJrqEq_7BMKR1XJGbvuyQHkzxF68tOOrc2u9oTagIBlUFVB4JSTwjjU03iuf4eFmBkKgpT9REfJi_V73qAcUdwguq6-xWqTpW5BnskSYF-uQxR7qtObZ4yWfwGheN73By9wP-Y1S3DuwbQx1He45kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOfbYYGt9Vl2_eJYH4nEPXMIfXl1CxUAKl_ofi8V3rYaui5K174vyj5HscLlr_Dsx4c4lFc6QqnsAaKwjVKOnFoUjLuht-0ACFx_nJu0v4DIgxpExlxGUVZJuVqP_NRfOr5zheNv2lcLK-EI4CD4uWvqXIWEYeBF9T5Ng54tT8MsnOHQeoL2ku2f9zuhycfBxklr62oyXFVetD59fZPJ2ORlNUdLc4_4wbkU1RieUp_CV7F5DvZUGVOLSxBIp6An7IHAr8hztbjqhFF4V7hUe6A5VM7Jf2KwoNBUxEX_QxdTZavbhozynmOxKJxACxekKNc2uBG1j8pITwIOG-Yt7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VS6VtIYsZT3IHBdU_FomRQebwrva5vKnG1F-UFswH16WLeXJtU2ZpIgX-KuIBs3ablpFUF0BeUE1Kls8Q608X82Y7tbkcpPo6uUFMpRCEAUsJ6sHfP-ej_KkACdngUaQkpzczB4nop35rBRgABiVrmYLAOfH4bREIae32Ze4GpngVJD4DdPg3IykHLziGk6zlLiMm-111_5bwhQcjwPa5U5WsmpsZw2Rqpu_c83wglvVIxwIOjkOU22-aSAthJ59Y-tonqWkyn7qsMW87n1Se-VhQRVc7QNKL5LtAAzRlW0r7Wsva7n-ntOcfGJr6zbEbxz8MhR7gQGxqr6flMGSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOAsH5_9anK2xUdfNo7KUcSdL7o7ybbU47BYflsnEpnS0mTvqWDC849IVsamcGSjsMhYRhwQ_7PtNYQ04_dIYR6EXYmCUOpmS8NaXMFbg0hDVoar8mL-s79J_0-nx08tsetevaPo47oOrfj10Ot6QJZo-3sZXYHEejHssszOeX3OCLPeDQ-F6Ja91hJf88SckmUGD2Ww1YqkZLB3DNafEHhn-fhkmipuUGKaYPYAR6S8wq3hw_zLFdw3OkNPmY5p-x-1yPPsNz-xWyO9lfJq2XLKzbHNba9graeXIHdCx0aQrLceBlK0bRr2crVM8YfX9ZiF1sUaU4xIEWWT1xTxlA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
خلاصۀ بازی ایران و نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/442513" target="_blank">📅 10:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442512">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O4pzZoMOxGbN17s-KrY1zcz5lOuILwhrO8882VlU4frhvFI65m36LoMrQpcO4S_IAo1wjnAMgxw4tRutzdcdvtG9EWIwK5SglrC-ztsnWwhcboIMhp1wnFYHtbou77uLWNZTunxJmhDH4sHJKEj1-XP-DizE2rrLBBgwm6TD_hOT_wTf__lW85vUt0Xz0Sr65LEsLP3ucuoVmx3Jxnbgg7skdzwYLO3Nd3AZ9svmrVnO2-35RANYmz5Ux0Cyb_4xauzTKIz2zGkLrkIgmedccuO0d1rLx6wYtIcS5crCxIK1m9v-DeQGex5ah2tFGYDujyZfTOPTfd3w-PzLuXIE3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل ارتش: هرگونه خطای دشمن با خشم انباشته مواجه می‌شود
🔹
دشمن در جنگ رمضان و جنگ ۱۲ روزه به‌دنبال تسلیم ایران، نابودی جمهوری اسلامی و حتی تغییر نقشۀ کشور بود، اما هیچ‌یک از این اهداف محقق نشد و در نهایت خود به‌دنبال آتش‌بس رفت.
🔹
برآورد دشمن از مردم ایران اشتباه بود؛ ملت ایران با حضور در صحنه نشان دادند در دفاع از کشور، اعتقادات و نظام اسلامی ایستاده‌اند و بخش مهمی از این نبرد را مدیریت کردند.
🔹
اگر دشمن اشتباهی بکند با یک خشم انباشته مواجه خواهد شد که کار دشمن را بسیار بسیار سخت خواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/442512" target="_blank">📅 10:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442511">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSjcTDspoWViuUgj6TWX-sBh4SMHubSTecHK3ugMYeissoKu3QgbZabg1_Nr8BzkMJ3sq8ZDPwaWrQtJtpJsj05dSwXypANlbQaHaApMMSuu1k5EyJ9qoT22EQcr_uH3maTVjv0WF4XoqddJ-rYGYNQboF2EF6Mqrq86QwtEhHTfF9-ZDq8lhEeXEx5XjfZQZZlzWJqG9RTVvK94nO_0I1mEbG5Bp_a7yVXLhuvf58Af4kY-lYWvZFv-Ut9ajsRLAjf3KsA71_Fg8lfr0g0AhjDbtQyHyfrVUfgswEL-Giq3A1HipLfg6QBSXqc8y3Bg4nPGFVPBxgKqKjRGFoO9eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چمران: ایجاد منطقه آزاد در تهران به تسهیل ترخیص کالا کمک می‌کند
🔹
رئیس شورای شهر تهران در واکنش به مطرح شدن ایدهٔ ایجاد منطقهٔ آزاد در تهران گفت: چنین اقدامی می‌تواند در تسهیل ترخیص کالا مؤثر باشد. برای نمونه، در صورت ایجاد این منطقه اتوبوس‌هایی که در گمرک بندرعباس متوقف مانده در تهران ترخیص می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/442511" target="_blank">📅 10:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442510">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر…</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/442510" target="_blank">📅 10:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442509">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQTXJMvA0Sxkfr0nMu__lSr5xMSInmJFj40P3y0AarINq4U7JJeT424jvI1HOnNhGAZgGLsOAjvLnQ5ZrQDy90eX0yYxlAArnQMUqa7Gt-Fo1kTfco6meez8l7-oXdBbqApP-kgMY3Xpf2d1nwZT8KVE6Khhqh1GpWxkIvYoyP98OwA_JdaI3pSFHYJcKysc1D_XpIOK8MHFWJiBQ6vI0fUpBfKdEw1lpVtFLe_klOOAbgDV90LvoXX1a6zC2uZIZLqsNN17GaUUiaWNKJ6wojLS-XZZPuWJb4nPwDBqSBYx2LJzHztG2DhBJfdvsWXrLZ06r5EN5LwAHCaa_uF6Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر دوباره برای طارمی و الهویی در فرودگاه لس‌آنجلس
🔹
کاروان تیم ملی فوتبال ایران پس از دیدار مقابل نیوزیلند درحال بازگشت به تیخوانا است، اما روند خروج مهدی طارمی و سعید الهویی از فرودگاه لس‌آنجلس مانند پرواز رفت با تأخیر غیرموجه همراه شده است.
🔹
درحال‌حاضر تمامی اعضای تیم ملی در هواپیما حضور دارند، اما این ۲ عضو تیم ملی همچنان در مراحل نهایی خروج از فرودگاه قرار دارند و تلاش‌ها برای رفع این مشکل ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/442509" target="_blank">📅 10:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442508">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INAJsOKgaoZBxmqPt9KdDnVWnI5XxoSB0Ot7iFx2dnKAmEi2IKspmaO5HbNerhQWOzU6RtqJxXeMxVzVxGqS2Vai9JJsZu8ZMoDrq9bYGUZzHZ_s1RAhivopIoKa2qA8svm3ZQMXzWdm52EOgjv1LO3GVM4OQEFmBxKW2sx8-8kgL6yino42TXdGQ6Q1hmYItAYolIz8LXTYyNX4p7XhV9l57aFY0S__vQcr0qEmHeiKMoehUpSvuqSpDFmD5cE8Ab_IvUwPt_nsnkiXMvnoeX4iHbsFBu6axFDhV3NJ8MSeFYETqQZTZEojWBwH_Dk3WryCMmHUayB4CkwCarw56w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سهراب گزینهٔ اول استقلال
🗣
براساس پیگیری خبرنگار فارس، درحال حاضر سهراب بختیاری‌زاده گزینه اصلی سرمربیگری استقلال در لیگ ۲۶ است.
🗣
قرار است شنبه هفته آینده کمیته فنی جلسه‌ای را با حضور تاجرنیا برگزار کند.  @Sportfars - Link</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/442508" target="_blank">📅 09:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442507">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">احتمال شنیدن صدای انفجار در جنوب اصفهان
🔹
سپاه اصفهان: به‌دلیل انجام انفجارهای کنترل‌شده تا ساعت ۱۴ امروز، احتمال شنیدن صدای انفجار در صفه، بهارستان و اطراف آن وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/442507" target="_blank">📅 09:39 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442506">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZ8QkNh8MqONc-OoxmkkaRbcJm3a2H9FSRTeqoSme710QFI68qt_OXZV3rBtxJMEEQLRbRPgypHI3OQyRIL3GjIhXN0s-CTZUXQ82U9mQMs2sXBFvSEiwItLLK1wECTF_F2RwzOxCDjRKCpnsgF-AluGeavw_Zi5QnnyckW4EqO3-5svsgvgqtAp7kAUDfTm7bO43nHXFOloQSs0E6InwfpwdWsEzot0FYXlf3QJEIkRUs_9w9WUgIFianCZabPqd6x_7i43u_EMJJfdz1NaQBrBgwENttLpkYJp1Na3yjnPoHnVqJa-eXJOXkAY8Zd2ElsVUc-F9xH-X7nHoobGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک افسر پلیس حین مقابله با قاچاق
🔹
ستوان‌دوم عرفان شکوری از کارکنان انتظامی تالش در جریان دستگیری متهم به قاچاق کالا که دارای چندین فقره سابقهٔ شرارت نیز بود، به شهادت رسید؛ طبق اعلام پلیس مازندران، متهم دستگیر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/442506" target="_blank">📅 09:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442505">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxtCGAFWNW_U6DCzKXVv1q4JQXI32EaZSmiQDsIREGcMVX2R38QbcYiScgNka710plYWHFO19jUyd0kgJYxXsQ4bYZP7hMzppIa6Fn-bWru80WspRua2ICsnNRnzxwmxIeubBc6fjojC0aLdq-IgZL4s2tuwGDV7BtEdAzKSbfCApKMVpcXZajTvfyUHGaHFNqbj1Hgjwopw8wrupPjXamallClojFhRq8X3L6Ki-M_6lNEiFMl3a_z3TM0P4vAlFER9PHjz9SV6xh_z-UGJpyb9orpQJ4yhN-NZT5tz16dCdGzD_0Fdf_O0gP_ArR9aIKqFduR9-su2w_w62JO4_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سند منطقهٔ آزاد مهران صادر شد
🔹
سازمان ثبت اسناد کشور: سند مالکیت منطقهٔ آزاد تجاری-صنعتی مهران، به‌وسعت ۷ هزار هکتار و در قالب ۷ پلاک اصلی صادر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/farsna/442505" target="_blank">📅 09:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442504">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ejZYAAks7Q7r26zBCzAIfwAxWlKRsfPOJ7jmvUEwb0BCNqIpShQXx3hsXYgA2PaxKC7DnCCtPpZMRbfk9jdtBDfPOT-E95MetmANpWCVFunY8u7Za3jhu-x4Iu_1D5eQjLy8ofPLtx10o64yhlzCUDAyAbxAzxncLlrC9NfETnRlek6lOVDsGe6XyvX4HJ4g-WQiq6EwAelItfUAn_WgVSOYreiGx5NPwKZKCr40S5ghTwe4d7DuA07vYEd1znZaSeOtrR04Z3U2Yz6QN7AiaqUmRmkEWh_4CMaB_hoNI4P15heYMFGrAqCGvPMDjZOkD5Qv-7JgK2ARnYYECSLVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس ۵ میلیونی شد
🔹
شاخص کل بورس در آغاز معاملات امروز با عبور از مرز ۵ میلیون واحد رکورد تاریخی جدیدی را ثبت کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/442504" target="_blank">📅 09:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442503">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🎥
زاکانی: ۱۴ بند تفاهم با نظریهٔ تفسیری مذاکره‌کنندگان و امضای آنان به‌عنوان یک سند در نظام اسلامی است و اعضای شورای‌عالی امنیت ملی به آن رای داده‌اند.  @Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/442503" target="_blank">📅 09:13 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442502">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1areXz022BwyywlA5zzTXQmWCugD_rzPlB6kGu7t5DutKMlQKlrMPwEBzo8JWYEq3EYHqDmuIJ6fP5Bekz-VLkn7SibRZ7niKGlQHBIfBZ9d95zRjX_HfWImN1NwsEuXITp8kwuIedbcq-GFLvuQOep-J8EXENYu-SnRqogOVvAVzMGzt7vbbY4V9AvsFXmYMWWflYYd9sfzGiqvpbCWkj8fHUiN40xRwDwYqFnFi07aWzYhViAyVesH8ixUVhGdzlq91S7zBCHB8n8qX7YFgMhFp_d3V5xa074OR_1uh_gh_uYbk39unpRT2ZESS5qkyqEZ3CvBzrJ_WQl1HvTDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌙
ستاد استهلال دفتر رهبر انقلاب: امروز اول ماه محرم‌ است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442502" target="_blank">📅 08:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442501">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0379533dc4.mp4?token=Zk_w1Y_M_pwGTBGG-rZd2lONvpeCtfqOOvOt25IPKcB66rE9DRRXqRLzX40tz2Ah3sjVc6af3XtHcVNm0mrjk-abD3dmY2A-_j5lwVXSkym7mrxjZrPdaqdRX0kwtyctMMydBtMEWFpUtEaBXVGfq7utUHgHxzgqfhGORWdLtAYzjWBkoapqg_H1q9tPVVcNE8BtmE7WQ00pvlIkX34mFjoOshS5HJyHlPu4eu-ZI-4i2cQKuJRnhwxDN5tQtgF69OqnnmepVKWl94PWDcILtU75AzJCS2hrANN1exzB1iUKu3HDoCdJBId7Y6Me8vuORNtxQ2RrR3z99cKEVOVjQmpA3_lyCL3BpaWsDJhRTZyqPm7U_tLG0p-Uk1kIxW-xSwmXQmw4K9nD94uKLo_DN21j2sjb796aDZmww_vBq41mE_5o0ajqVWV34V8mlPExBLRoSxkRp5BUzBW-yQdFYq_U_ALK7j7lUttSW1r-rHIox-0Gg4KmxFnu3XTrqd78qXMjuZ5ANKFpCBbBcIY02UvHqJcBk_bvn6wSa4ckgRLLFim1JF2wo2JFJ4niYRc-Q2UZFx94d7wDnkg986TwllEiaVipHACatSaUEe3xMhFjPfysQD4hEN4VpH91zbXejEAE23GMfhcKP9OJLg6FyxqM70kV0jZ-FERIZBGJfjo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0379533dc4.mp4?token=Zk_w1Y_M_pwGTBGG-rZd2lONvpeCtfqOOvOt25IPKcB66rE9DRRXqRLzX40tz2Ah3sjVc6af3XtHcVNm0mrjk-abD3dmY2A-_j5lwVXSkym7mrxjZrPdaqdRX0kwtyctMMydBtMEWFpUtEaBXVGfq7utUHgHxzgqfhGORWdLtAYzjWBkoapqg_H1q9tPVVcNE8BtmE7WQ00pvlIkX34mFjoOshS5HJyHlPu4eu-ZI-4i2cQKuJRnhwxDN5tQtgF69OqnnmepVKWl94PWDcILtU75AzJCS2hrANN1exzB1iUKu3HDoCdJBId7Y6Me8vuORNtxQ2RrR3z99cKEVOVjQmpA3_lyCL3BpaWsDJhRTZyqPm7U_tLG0p-Uk1kIxW-xSwmXQmw4K9nD94uKLo_DN21j2sjb796aDZmww_vBq41mE_5o0ajqVWV34V8mlPExBLRoSxkRp5BUzBW-yQdFYq_U_ALK7j7lUttSW1r-rHIox-0Gg4KmxFnu3XTrqd78qXMjuZ5ANKFpCBbBcIY02UvHqJcBk_bvn6wSa4ckgRLLFim1JF2wo2JFJ4niYRc-Q2UZFx94d7wDnkg986TwllEiaVipHACatSaUEe3xMhFjPfysQD4hEN4VpH91zbXejEAE23GMfhcKP9OJLg6FyxqM70kV0jZ-FERIZBGJfjo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بازی خوبی کردیم اما از نتیجه راضی نیستم؛ شانس برد داشتیم.
🔹
باید زودتر می‌آمدیم که اجازه ندادند. سازگاری ما هنوز کامل نشده است.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442501" target="_blank">📅 08:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442500">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">همتی به مسکو رفت
🔹
رئیس بانک مرکزی در رأس هیئتی با هدف توسعۀ روابط پولی و بانکی میان ایران و روسیه، صبح امروز عازم مسکو شد.
🔹
این سفر در راستای گسترش همکاری‌های مالی و تقویت تعاملات بانکی میان دو کشور انجام می‌شود و قرار است طی آن، طرفین دربارۀ راهکارهای تسهیل مبادلات پولی، تقویت همکاری میان بانک‌های مرکزی و ایجاد سازوکارهای جدید برای افزایش حجم مبادلات اقتصادی گفت‌وگو کنند.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442500" target="_blank">📅 08:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442499">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/508119118f.mp4?token=EDwtN7snBHwGXCLXl60hbDWhh1gFyGJzDcqGxGtD9CdqXp59TSEoEb3Bhl2_ImHwgImKm7z3RMXIiu7Y8YcP1PiHP-Fx83cXxNzCpBQF4gC8zbif-tjHSZjG_y7pnBIL-J-2LIVoF1DRQsd90c9tcF15iSCMOzbSGe7jW6_pgrWHQj9Uq12_PtO-rymQz5xgbmdY09d4wrDg31yxEKJvpxYgXjXJt-5PowyBEu6uYHU9xM6Upsv44OPQ2mk2Qqb6Kp8HPpyId5dV0EjRNdIPaU_hPLEJZ2RblW6efsXkU7H7g3Hx019rb_8Un3K_W4Bl4MGV6tVAzH6t8pOQJNit2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/508119118f.mp4?token=EDwtN7snBHwGXCLXl60hbDWhh1gFyGJzDcqGxGtD9CdqXp59TSEoEb3Bhl2_ImHwgImKm7z3RMXIiu7Y8YcP1PiHP-Fx83cXxNzCpBQF4gC8zbif-tjHSZjG_y7pnBIL-J-2LIVoF1DRQsd90c9tcF15iSCMOzbSGe7jW6_pgrWHQj9Uq12_PtO-rymQz5xgbmdY09d4wrDg31yxEKJvpxYgXjXJt-5PowyBEu6uYHU9xM6Upsv44OPQ2mk2Qqb6Kp8HPpyId5dV0EjRNdIPaU_hPLEJZ2RblW6efsXkU7H7g3Hx019rb_8Un3K_W4Bl4MGV6tVAzH6t8pOQJNit2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت زنانی که پای آرمان‌هایشان ایستاده‌اند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/442499" target="_blank">📅 07:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442498">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kg4AxkHEiPouEDSP5wQ4S2RZFbW27iv0JTv9wwipmyK1_9mLSiVbCbMYW6v0YFIsUKasZel8tvTiWf8rKIftZYii_gabtI4gCfkrcp2moybd1lcIHsc2QehKKYejBOl6xY-e_4Cszx2kOKsrsTziiXuseMijDXlauwyniILXZULwQxyuCgrqobK2S7ggFAixFvChwTlsQ1o44_lvWa4X0_XSI55n8yKOpwZcb4Zw39xfMsh7lA7JdJVVD9jLJs8miH8nC_hxCZk4Lu8OtzWDBHiib_MLBGHF7ki9diUxRkGBBtBBEdXFzflyUAKapntKBN9rEhrc0C5ixhnmnW2ogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغوش باز «شیرین‌سو» برای ۲۰۰ پرندۀ مسافر
🔹
تالاب شیرین‌سو در شهرستان کبودرآهنگ به‌دنبال بارش‌های زمستان و بهار دوباره آبگیری شد و جان تازه‌ای گرفت.
🔹
به لطف باران، بیش از ۲۰۰ پرندۀ مهاجر آبزی و کنارآبزی به این تالاب ۴۳ هکتاری بازگشته‌اند. حضور این پرندگان نشان‌دهنده بهبود شرایط زیست‌محیطی و افزایش ظرفیت زیستی این زیستگاه طبیعی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442498" target="_blank">📅 07:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442497">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44f9ddb167.mp4?token=bHv-UDRBSzED6o3_s-iNYH-VDbrtEqIAqKRI_z0uNyCED6wco4kxN7VHfXlB7cM8f-9Bn29C6phNRTMWt9KDFCwFy3TP_SBBImYie_Jm33GionXNNEk7UmMhO7mA2Son07UU4bq6GdMAN24qBRguI5JZDSMgG1VoiJ9wsrRqdZkfSBY07a_MIbzSOWyE5hdrYPTgXLWRD_hXAPAOLjigTxCmqkNQvGQmlFC-5hNahJihYcsu74VEIxemBc8H8SIcXzIN1Rbkh9jHC0TCFJMNxDImdPPIdkYStFbNWHgaNn_O3dCh0Es8Pu7Q0x7oWbcU6dQLXJgjrC-935DL7GpzFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44f9ddb167.mp4?token=bHv-UDRBSzED6o3_s-iNYH-VDbrtEqIAqKRI_z0uNyCED6wco4kxN7VHfXlB7cM8f-9Bn29C6phNRTMWt9KDFCwFy3TP_SBBImYie_Jm33GionXNNEk7UmMhO7mA2Son07UU4bq6GdMAN24qBRguI5JZDSMgG1VoiJ9wsrRqdZkfSBY07a_MIbzSOWyE5hdrYPTgXLWRD_hXAPAOLjigTxCmqkNQvGQmlFC-5hNahJihYcsu74VEIxemBc8H8SIcXzIN1Rbkh9jHC0TCFJMNxDImdPPIdkYStFbNWHgaNn_O3dCh0Es8Pu7Q0x7oWbcU6dQLXJgjrC-935DL7GpzFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442497" target="_blank">📅 07:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442496">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abq_CVJZaP8WB-lmCNZuzZM1tmJDd1vOT35GcVTrw8_pDaPru5GaXN3pohy4f2hV79499SZ83PrCvX-uf0t9158IeUEV0ybb7iI9WPf1lzG5ac1IR_ll33jnkUgAe5J6gkUif5dofNIZHmcC8yDPJOE0n9Z__puT4SaLrkFcondS91ypC_QoWHfPU91szltjbnoHC4yAXllcLHY94mqOy6gXwxP2iKz1oWD6RYyLb_inMgyocA69zXTifnkNAqDTSwvmWurCIk3_mimUORzyC2-UGlyYO53I_wvKb-Fs-jjCkiuAmqXIuMMWwSukPIB0UWH7PmKT2zcB-OVYhleYtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس داوری فارس: داور در اعلام خطای مهاجم ایران اشتباه کرد
🔹
حیدر سلمانی: در دقیقۀ ۶۷، داور به اشتباه خطای مهاجم ایران را روی دروازه‌بان نیوزلند اعلام کرد؛ دروازه‌بان با مدافع خودشان برخورد داشت.
🔗
شرح کامل تحلیل قضاوت داور بازی ایران و نیوزیلند را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442496" target="_blank">📅 07:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442495">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">تساوی یوزهای ایرانی در برابر نیوزیلند
⚽️
ایران ۲ - ۲ نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442495" target="_blank">📅 07:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442494">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/627745dd75.mp4?token=np4l7tA7odNnuQ1YJj4UrQtbwwwkqdp62UsJLRvlymxinMlpqQfKxXVJvle1OCh0lzvcOR_zdxWYQkonHgahGRRWU_N2g_9iW7B_zu4kRHtv7od1hr0sQ6-rqeopo6AgB0M7Sr_Jn6dqOVOflLLURUjiHRHGBBnZBq6liwVsoBtZqSRbRKjFVcpzEz01UMa1YuoXvND8WLIb3wkEKCKDzJ_fhDibOJPXI0f3SIEaQEDEWKeU9fdYWjYn3KrUuODwiJacCy8zs1Cw4PuK-Rka8L3azEnmZFoPTkA2Zq81Rg131oPq5OPri9oIkOXbxCkcQgkDSI0qEDb8fNDEVz--UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/627745dd75.mp4?token=np4l7tA7odNnuQ1YJj4UrQtbwwwkqdp62UsJLRvlymxinMlpqQfKxXVJvle1OCh0lzvcOR_zdxWYQkonHgahGRRWU_N2g_9iW7B_zu4kRHtv7od1hr0sQ6-rqeopo6AgB0M7Sr_Jn6dqOVOflLLURUjiHRHGBBnZBq6liwVsoBtZqSRbRKjFVcpzEz01UMa1YuoXvND8WLIb3wkEKCKDzJ_fhDibOJPXI0f3SIEaQEDEWKeU9fdYWjYn3KrUuODwiJacCy8zs1Cw4PuK-Rka8L3azEnmZFoPTkA2Zq81Rg131oPq5OPri9oIkOXbxCkcQgkDSI0qEDb8fNDEVz--UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قلعه‌نویی: بازی خوبی کردیم اما از نتیجه راضی نیستم؛ شانس برد داشتیم.
🔹
باید زودتر می‌آمدیم که اجازه ندادند. سازگاری ما هنوز کامل نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442494" target="_blank">📅 07:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442493">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4244f3cf92.mp4?token=ZfvNR4Bg2TRJYi4_yoAFCYUGR19E94LkwPKf8pEyDMtD6jfr3KCvgS4b2zrCJcXjkEa032X7ry6mcrBBZbGpRUzLy7VhdD8gG8Q-LPzgipKVbAf2H_xEGGc4ly61BhwFDtINvxkks-zfnwFC_2IESEx31WiVmhjHK2calSgcQngyhBhMp8-88wHQ41kZ89oEBURkQmE0Sjb04wLKTds9y-AjUGlXsvUiZdPjn0bnh-N_JrVEj-RwgSJxSvg7hlL58Bnr6hHTRP4l-Qd-R8SdrUl63DT_E8bWk5Trqg5PEqlG1U5kpgQjPLnOJcJA83FzdE2Egx5DMOa9-ZoQWm06GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4244f3cf92.mp4?token=ZfvNR4Bg2TRJYi4_yoAFCYUGR19E94LkwPKf8pEyDMtD6jfr3KCvgS4b2zrCJcXjkEa032X7ry6mcrBBZbGpRUzLy7VhdD8gG8Q-LPzgipKVbAf2H_xEGGc4ly61BhwFDtINvxkks-zfnwFC_2IESEx31WiVmhjHK2calSgcQngyhBhMp8-88wHQ41kZ89oEBURkQmE0Sjb04wLKTds9y-AjUGlXsvUiZdPjn0bnh-N_JrVEj-RwgSJxSvg7hlL58Bnr6hHTRP4l-Qd-R8SdrUl63DT_E8bWk5Trqg5PEqlG1U5kpgQjPLnOJcJA83FzdE2Egx5DMOa9-ZoQWm06GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
رامین رضاییان: بازی را خوب شروع کردیم اما گل غافلگیرکننده‌ای خوردیم.
🔹
بلژیک هم مساوی کرده، مطمئنم تا روز آخر می‌جنگیم و می‌توانیم نتیجۀ خوب بگیریم.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442493" target="_blank">📅 06:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442492">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPgksAJvSnMn5acZu2-3ALmfueW1juPbCrrs3fqNveWlsbEtMqbkmeV4naIcMa5aOAOI878FrFPTAY5B4dcaRCJX_KHAK72KLAedqih_EJn1yl_Vqe2rUfHx3njqcovGmZFsIOC3XvABesy6RCrL3PsMHsY-flobD-ybzrxx9NCbYvrNE4JxIV0hjKZtHyBrwlRD91yt3mBDuCUrNEo4jDYi6m-LGo4edUredfcNTR1kqLb1i2Ajf0eqhfARuXxCL7GNDdkAD-z9iCSfzJQ1a59FtzlMSkTVZylHfqWoDAP5QoqoSDSooCpa1rE3pp9Xyx-4YJ4BMUiuHa9ltjDO1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گروه ایران در جام‌جهانی ۲۰۲۶؛ همه برابر
@Farsna</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/442492" target="_blank">📅 06:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442491">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKh3jByCPnLrhfcRy5wpqWRW_mwK0ddIfV0s4vucyZOp2n7m9WVXx9H4re38pIkmkq98UbDd7_0gabGjFEL7hsSbF71mGsM8R0Nx04wXKUYigtUJj-tm0XTEFC-ucE2kc6fMfMQe6njD5Zfnb6DK6o9pXvvKGtAjsGCVUqqfltNXrczcyl8HUbka8TWPiOlsaHiGaJKPq_2guPbL1CsIorRrPJPElBe6d_ueVvxK27zxghK1mY-0xfhyW5MxN5XOZia4zSXrHwHL69nvZC4oAhn4Rsn8_KIiQHNAZva53sl7Q8SpsW4ILF9K8x6JE079j5tdUgZhq5qyVNjkbbot8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی یوزهای ایرانی در برابر نیوزیلند
⚽️
ایران ۲ - ۲ نیوزیلند  @Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/442491" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442490">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn5t6_p_Lz5HiyArQXVJ_F9g3whQxiHfzIQCUhpsT6ipLmSkX7Kah879zm0DhF-BWhYT1W9s60QAVm--PbpVe6LwiCvlgY8lYnrHjRV-juYsmGGACnp0Zm4TYYMBuKff8vJUyFePz0XIsamgjdeUy9j2wn4tPVF46MvlpkUrsij_2HkbbLB5Hf0e-HLSW1viCw7bsSMTE1plq8fJZv7no0zCf0psOfPSa7Ft5wXfrYJyECGiU6ISnYyIEBjrKDcdqnZudwv_RQ5xdfk4mA5Mc2JIHX0NBjdMF27MyVkbJQ6biVXCAn1ME6gQIKwq91KDjNo7tLozQlxdujeV6SCbYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی یوزهای ایرانی در برابر نیوزیلند
⚽️
ایران ۲ - ۲ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/442490" target="_blank">📅 06:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442489">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb3f718a25.mp4?token=cXifyl9nIT9CIlnGtglfRukCnkO4Z2OVvFYH14QE8uv5XTvIuLvFkfUdNzTlREWzNGIkDnf_ST3bwcKoGVXA85gQ8a0MbEX3Y6Hrmj2K1kTqib95HC-Vc7mUtj7CdJXlHpcpGoidiGAGZ7P4gvAPDQx0UGFCxYqItGqxGBWBmcNqyp0vdvNM9B2XsO8jL4PIGuDE6sP3n5YaiM3t8h_HmrLuRKYsnf8P9Xm7X2_yKocN1vugoNpcGh3JECTkonoloyuGtxImkVKt68hatbNqb_myi3L6-TvPTz8ZujqbUbq5dlnpxkgu1rNpKAm4EryU-U5BfzslhAwdIlairXaUiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb3f718a25.mp4?token=cXifyl9nIT9CIlnGtglfRukCnkO4Z2OVvFYH14QE8uv5XTvIuLvFkfUdNzTlREWzNGIkDnf_ST3bwcKoGVXA85gQ8a0MbEX3Y6Hrmj2K1kTqib95HC-Vc7mUtj7CdJXlHpcpGoidiGAGZ7P4gvAPDQx0UGFCxYqItGqxGBWBmcNqyp0vdvNM9B2XsO8jL4PIGuDE6sP3n5YaiM3t8h_HmrLuRKYsnf8P9Xm7X2_yKocN1vugoNpcGh3JECTkonoloyuGtxImkVKt68hatbNqb_myi3L6-TvPTz8ZujqbUbq5dlnpxkgu1rNpKAm4EryU-U5BfzslhAwdIlairXaUiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت عجیب نعمتی در موقعیت گلزنی
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/442489" target="_blank">📅 06:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442485">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EoWlvk2IoRmucjhwBKO_BJiFUBdIA8eXUK1MmmDyGJOkeenc05FyeKOjiJFX5cXBTnP3WYBPjIgnL81QQhSXw-0W5qrCU3b3Cmr7zDgWHkvDcbCqPXAe8JOBWH2NEhTbTkS1LUcE5r0hKDkwH1f9_9y-nAewzKIapBDXPgfLd7i0C5o7ilhj-2xluAhlDVGUuhoSKWqcy00i6cipH2SsybsMpPNQHBeLlSdJNpcEegAM8SE_pdsj-xcvCL4trBn0Tbf4bjPSZGv-H267O_WukXomrPJGzMk2mIBRINVMLse9r8HxIm4WaiMgkkGRA10TQcIdB8z_7QrgdUdy1J2R_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3hm9bqnUP47nwtVrxeIQp1pCJrRdQ57COBnanyP--JPDLFwgmUopy2Sr-s-PXUacCziQ16al66QwcUdciI9fNSQdTSQx0OL1nCxvolazalxraGCvfTVRd3lnF2s-nCVPctVkWOAaIqrLQGwBue1ziufuFR0VjoYnD57uExO80WzlbxONv7qKmyku19tOFKJjvEzsMLi06KBCpyjxrLezIArDndu9F4P-Aev95U8fAEnqDz6aR0g0aIcD05Dim3AauCzmiTGyDMah2vmJZFCG0NnGV_VyD8kTuFWB5h92mW_YXh281qJCLdsJX87xsxslrMHS0BJXNJ1_LuVvtF_qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k4NPRWyn27vgWBfE6n5XOoT38yd608J3EmsKBOOtJhV0Ucfpkl0syCxGgs9NTK9OeBtBUQdqJ6duvIxAQmvlXnegmktKoTgZYufrxHsLwhtNM4fvdCdcQJ_pJ3nDWi6CMBKwIxrJ7BQ97Uf2GM_NNzi3R7zKjy1I6v5CAoUW_EKpoSxbZQjT5msWT59r_qbiTEpOmvM4GQTb__ed2i_lPu_cb0r-BZm4rElYmNOKC3wDklJLWeP0IRWGuaiPLgzhKdnsEccZjfkFwdAuaui_GbRATph7XgHCQbm3pXdVOFhRO6_qB6mcUpjjbx13VHdN9P-nO3HYOv5Sdb89RgwHOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dUpELcDtckjhmTX2S4M8anltbYk8v2uPWXB5go_DLP0fNTs5H1kKUF834YMYJ0rmt5gwRk1-FTrk60pUisEYUoqc3Cko2I1BB4rFOFPHn6ZdAF74J638mePOG15j_1ETWvv1muVSRy3i5xQ9rXmHU_7SaDfs5bVb0HK3H-4nEgetcXqMvn2Jp7PVBknxhNSg--9hP9DRnmc8inxiA6UJANmFqaZURZlE1a_pa53lbdXS611c5Ad5kQWdOtBdtdpKX54Gi4Jyi3HSvj8L69ScV_6lX_e8faExFgaqprJc_VrLIiTqzC45-8k6f4fWgtFIlfX8Fx7KzeRfi4ECHanHgA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل دوم ایران در دقیقۀ ۶۳ توسط محمد محبی
⚽️
ایران ۲ - نیوزیلند ۲ @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442485" target="_blank">📅 06:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442484">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">⚽️
امیرحسین حسین‌زاده به‌جای مهدی طارمی وارد زمین شد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442484" target="_blank">📅 06:19 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442482">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚽️
احسان حاج‌صفی به‌جای سامان قدوس وارد زمین شد
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/442482" target="_blank">📅 06:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442481">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c76ef17530.mp4?token=riFytAakrY5g0pVzeN7PoHLt46U1a2p61pBzyqMF45HwVJnZgEVt2avtT7UNBLb09Nh58copwvi6NxHZtbQgWktCKWCI0gT5QSdxB2ZV9RG_UKa-MACKb3xctJgKot7QOS3k8vhdDo1WAM-caeRTNBSzWY_oz7GG1qaq1zY30rIFA2OGynwU9AlTWxkO99a2MpmEhoVLA7SZYajnn5Q0Xnw_L6u63gnsgyD94_OblqMDNl-sOMIrQW7FVikxwPL1oFt8ECCc9UZMRXXSlQbEjeZ7oMvzFDQkgQNj8mzjuaOQKj73TtIQsWw_oi9B2xwaDvjxcRZuDJoFBZFMZvZqvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c76ef17530.mp4?token=riFytAakrY5g0pVzeN7PoHLt46U1a2p61pBzyqMF45HwVJnZgEVt2avtT7UNBLb09Nh58copwvi6NxHZtbQgWktCKWCI0gT5QSdxB2ZV9RG_UKa-MACKb3xctJgKot7QOS3k8vhdDo1WAM-caeRTNBSzWY_oz7GG1qaq1zY30rIFA2OGynwU9AlTWxkO99a2MpmEhoVLA7SZYajnn5Q0Xnw_L6u63gnsgyD94_OblqMDNl-sOMIrQW7FVikxwPL1oFt8ECCc9UZMRXXSlQbEjeZ7oMvzFDQkgQNj8mzjuaOQKj73TtIQsWw_oi9B2xwaDvjxcRZuDJoFBZFMZvZqvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم ایران در دقیقۀ ۶۳ توسط محمد محبی
⚽️
ایران ۲ - نیوزیلند ۲
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442481" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442480">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3VAuSBL5_KrBMl1HL6YHIHW9qbCqRjLIQoWVedq6XN5BjK7UJmqQjt_xFQo_DoXTY0yBnO_nRNbLLOTZn9IfG2JAvI37njeQ-hrlaGot3UoP0eF97bfBgH2guct4ywt1JuFzIBEGu-_poGE7KaA8rN7u1LkEWBCwyKg6stKA8A0GkukQee8paoawjTaXCR8qCcgsn4txSscnVXc4qWRn2C49vBJg5a3sp6a0sqWwh4qH4fDOnQfzQUxzQARnrsePEKnZp3QnUS6BhSHrdfuZdhocOfRvYikkXurUMyrd6zLp7Pobk2qgjCgLw6E-ubnO32pkxezojqsR6qhq8Kizg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
میناب ۱۶۸ روی سکوهای ورزشگاه
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442480" target="_blank">📅 05:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442479">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0ff7336c5.mp4?token=YGuAR3EeRUvWOK8Ze_tgAfeLSFESQTt3BQxPGa7JifjD0QBJ2Bozn4CMHaz9_9QPzboJzDuV70zFQ99d6FngrLstmwP4Ef4YPuFNX9AP7f4PPZx0T8HFiIAScVDULYXfL_M8yCuoZWmrEdvx7dZMoVC8Yt0YWL-0z73aqwfZhj3ju9tcQODclWR4oay4lmdnX3-niS_OVOhlHFIUm1Y4OzX7fm3FjK3G-vxKilO4tnGKTUFxnpbrmLlM3npcGFLOeoYqzDFkzUuFiAfPuPTag3VctByUyrREE_wGlcq5JUFSgNiQB1rwZcBDf8Rc2mbJbFg4oY1AH6XjmroVKEX8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0ff7336c5.mp4?token=YGuAR3EeRUvWOK8Ze_tgAfeLSFESQTt3BQxPGa7JifjD0QBJ2Bozn4CMHaz9_9QPzboJzDuV70zFQ99d6FngrLstmwP4Ef4YPuFNX9AP7f4PPZx0T8HFiIAScVDULYXfL_M8yCuoZWmrEdvx7dZMoVC8Yt0YWL-0z73aqwfZhj3ju9tcQODclWR4oay4lmdnX3-niS_OVOhlHFIUm1Y4OzX7fm3FjK3G-vxKilO4tnGKTUFxnpbrmLlM3npcGFLOeoYqzDFkzUuFiAfPuPTag3VctByUyrREE_wGlcq5JUFSgNiQB1rwZcBDf8Rc2mbJbFg4oY1AH6XjmroVKEX8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم برای نیوزیلند در دقیقۀ ۵۴
⚽️
ایران ۱ - نیوزیلند ۲
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442479" target="_blank">📅 05:55 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442478">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc7c11d9c7.mp4?token=irX3OLXiBWleH4riAt29SosG95S7kbhqlpjCmjPytqhWtp7hziyU1Yt4zwg5sXDO4wX-jlSFYky581vy4jJlZumRM-qEooVNqs-pEK31J1PLNha8rCmuKrZasFcoEZKdOAsoft8o1R3PGIrzW3jDPEFvQ_DOdsFikNRnxCKXJazhTKu4fh7BzApjBa36YXpZGVb_2Is1rSI09QiokQrRV-HlxdOSWOI7A-whzPQFRrhmMy46AScTbQsldd8ce4XUh24u9nT4a3ECgFGtMHjYkMxpNBtVgW__KE4J5GNd2mU8SP9sZd18JkXvVJeG75aPuJryfYswpdjWDEH4SfkAgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc7c11d9c7.mp4?token=irX3OLXiBWleH4riAt29SosG95S7kbhqlpjCmjPytqhWtp7hziyU1Yt4zwg5sXDO4wX-jlSFYky581vy4jJlZumRM-qEooVNqs-pEK31J1PLNha8rCmuKrZasFcoEZKdOAsoft8o1R3PGIrzW3jDPEFvQ_DOdsFikNRnxCKXJazhTKu4fh7BzApjBa36YXpZGVb_2Is1rSI09QiokQrRV-HlxdOSWOI7A-whzPQFRrhmMy46AScTbQsldd8ce4XUh24u9nT4a3ECgFGtMHjYkMxpNBtVgW__KE4J5GNd2mU8SP9sZd18JkXvVJeG75aPuJryfYswpdjWDEH4SfkAgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربۀ مغانلو از بالای دروازه به بیرون رفت  @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/442478" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442477">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ad3fbf9d9.mp4?token=jExerjtZmHMPDdqsKqJyWF8P5aYKKiy8QrlRG2pzILAgL88O6UVc3PBQNTKSZ6nfdojWC0FnJssKJHKMUZDoxg_RRe3UuX-6zxsvbbGAZVYWBPqL90aHo-XrMeikBC9X-8qowWNxOfyA2vruy8ZcnXyTZRwI6Z0q4bIgP7Ds_hfwmqMcaMqTesiLM-j6TeRFoLcN6TBPQraUpAyjdPxn4VtebqF9GynYyd5Z0VHlD9xlS7Pz29DWYxVL8Oi8iLtjGi602hrmgfNO2RYMFwjb0PQK8_Djm8Az79JRhcz0CkdHcKHKir3WTMpUj2eJCs-D6fA87X82LY5vqqgTf6gg-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ad3fbf9d9.mp4?token=jExerjtZmHMPDdqsKqJyWF8P5aYKKiy8QrlRG2pzILAgL88O6UVc3PBQNTKSZ6nfdojWC0FnJssKJHKMUZDoxg_RRe3UuX-6zxsvbbGAZVYWBPqL90aHo-XrMeikBC9X-8qowWNxOfyA2vruy8ZcnXyTZRwI6Z0q4bIgP7Ds_hfwmqMcaMqTesiLM-j6TeRFoLcN6TBPQraUpAyjdPxn4VtebqF9GynYyd5Z0VHlD9xlS7Pz29DWYxVL8Oi8iLtjGi602hrmgfNO2RYMFwjb0PQK8_Djm8Az79JRhcz0CkdHcKHKir3WTMpUj2eJCs-D6fA87X82LY5vqqgTf6gg-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ضربۀ مغانلو از بالای دروازه به بیرون رفت
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442477" target="_blank">📅 05:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442476">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9a562a209.mp4?token=rh6_t6P9NzKlziumCo8zQbyoHgGBssN9uGt3ZSckvmeU7uBClmJ-zNMK30Df2vsy3ILnSFnKnvrHmaQPce8OEG78mf2WRUkW9tlIX4dc0WiBe9pv51EfDxcO0H01ONxWPGtZjTFbAmdTwuH6gyrnbgmwnU7cNwvUV82GdV3luKulZCkn-I_erqXriRLDItpOnPkp5g7oavcbBecsSb0UFWKcbu8ImoifBaSUvtHpCHDc2-y7uEUlaYTl0ftCd0ZYJdUYBvVF1U6GXriWjUcEBSeoAzqD53dQmFPTZ_kAIIYCH67Du_ja7uDTghYg-o7-Wxr6OMFFKJYm_DqxIJxg8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9a562a209.mp4?token=rh6_t6P9NzKlziumCo8zQbyoHgGBssN9uGt3ZSckvmeU7uBClmJ-zNMK30Df2vsy3ILnSFnKnvrHmaQPce8OEG78mf2WRUkW9tlIX4dc0WiBe9pv51EfDxcO0H01ONxWPGtZjTFbAmdTwuH6gyrnbgmwnU7cNwvUV82GdV3luKulZCkn-I_erqXriRLDItpOnPkp5g7oavcbBecsSb0UFWKcbu8ImoifBaSUvtHpCHDc2-y7uEUlaYTl0ftCd0ZYJdUYBvVF1U6GXriWjUcEBSeoAzqD53dQmFPTZ_kAIIYCH67Du_ja7uDTghYg-o7-Wxr6OMFFKJYm_DqxIJxg8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در شروع نیمۀدوم، مهدی قایدی جای آریا یوسفی را گرفت
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442476" target="_blank">📅 05:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442475">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/719b90c3d6.mp4?token=HoYkh8t8IT1WQND7XG8f1lbI66CMG7F_KL2undE9QfPon4PDWhKxF9K3pb0UGdcubHAmz0xZQUVl3GLCoGs9cizwXSHaydYgoGBx6ZjViKL3sgbGxABjtp0yg_kXRHTAmKAeGqExq3UhZ2hKcv2541VTSW-rsNp154qUEIrYA71ca8qmf5bEl2kSg_00qvlHOzRdjQSBFw0a8-0P2Qx637YL8WLvub4VyMxYqBifodahnpWvJD6xAlJiIbJXwb-zG68maNx5gq8_89MD_ujNjQb8m_0uo3JgVtOvsT7pocsjszTZCPP6cDpPNltE38Apb9E_Z53gQTWwoQbbEEovFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/719b90c3d6.mp4?token=HoYkh8t8IT1WQND7XG8f1lbI66CMG7F_KL2undE9QfPon4PDWhKxF9K3pb0UGdcubHAmz0xZQUVl3GLCoGs9cizwXSHaydYgoGBx6ZjViKL3sgbGxABjtp0yg_kXRHTAmKAeGqExq3UhZ2hKcv2541VTSW-rsNp154qUEIrYA71ca8qmf5bEl2kSg_00qvlHOzRdjQSBFw0a8-0P2Qx637YL8WLvub4VyMxYqBifodahnpWvJD6xAlJiIbJXwb-zG68maNx5gq8_89MD_ujNjQb8m_0uo3JgVtOvsT7pocsjszTZCPP6cDpPNltE38Apb9E_Z53gQTWwoQbbEEovFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد ایران ایران هواداران در ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442475" target="_blank">📅 05:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442474">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4bf7284b1.mp4?token=a6h6oDDkcG7pLj6RvOQBF_s2mYH96Lvvfwi3am7KK3L0x5enp6rC6-_5znYMgS2LbOUkKwYr2ZjysmqNI9n8mDR6Y1ivWKU6bXMosohVWAqpfdFnpPHSbWXsvWUdYt1PiD_EpEpGJCLfHzeseufN8DKsxzd_cXXLRS7RpYlcHDOKWRFvYkPEdbKdNzniyQUNq9_vCDAXtQ4xki3d03dTWkFPnScmVFahItMVJbe_5zDTYFNG8B0MZddgj_fysOVM-ZG1tWfrZ0GcD5hB5M35Gy8dVkbnLC_OB6NZFkY_qSj1EJoz5ldRkJdV6KIP2iT_LqhGfY9eDQBD2G4UWLp4NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4bf7284b1.mp4?token=a6h6oDDkcG7pLj6RvOQBF_s2mYH96Lvvfwi3am7KK3L0x5enp6rC6-_5znYMgS2LbOUkKwYr2ZjysmqNI9n8mDR6Y1ivWKU6bXMosohVWAqpfdFnpPHSbWXsvWUdYt1PiD_EpEpGJCLfHzeseufN8DKsxzd_cXXLRS7RpYlcHDOKWRFvYkPEdbKdNzniyQUNq9_vCDAXtQ4xki3d03dTWkFPnScmVFahItMVJbe_5zDTYFNG8B0MZddgj_fysOVM-ZG1tWfrZ0GcD5hB5M35Gy8dVkbnLC_OB6NZFkY_qSj1EJoz5ldRkJdV6KIP2iT_LqhGfY9eDQBD2G4UWLp4NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصویر شهید مدرسۀ میناب در دستان تماشاگر ایرانی
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442474" target="_blank">📅 05:35 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442473">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c43df35bb.mp4?token=Ui3xir67tH9ElokdLQ_z3gF9UXzJ-4EE0VmJsuk1TgA5O7ZYomzD2hECvQHSoRi_MjyxXfcxXqwANEptjhPlWz1JaCTMEg8Zb6IvRpINryUgIj84FzHluopo9-bYAIWN9fUfR9sG3SC-Xk_VACp6vKzzmGZB9EyLhxEyl3oQ6u-N1ouX2d9LWGJznvy4MqcJFDH5dSrw5W8CqjxzPw1SeXdZCcrnZ_aJTS-So1hWNRzQEJtNVo7mBLcyJMnZZDU8Z_bevJ1OaNgIsxZt05WsjcrPUyq245Vnwtn97FqqR8MFXZbv-YLk7pHEn_SgQU8EWYILB1P5izLTB9BS2tm8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c43df35bb.mp4?token=Ui3xir67tH9ElokdLQ_z3gF9UXzJ-4EE0VmJsuk1TgA5O7ZYomzD2hECvQHSoRi_MjyxXfcxXqwANEptjhPlWz1JaCTMEg8Zb6IvRpINryUgIj84FzHluopo9-bYAIWN9fUfR9sG3SC-Xk_VACp6vKzzmGZB9EyLhxEyl3oQ6u-N1ouX2d9LWGJznvy4MqcJFDH5dSrw5W8CqjxzPw1SeXdZCcrnZ_aJTS-So1hWNRzQEJtNVo7mBLcyJMnZZDU8Z_bevJ1OaNgIsxZt05WsjcrPUyq245Vnwtn97FqqR8MFXZbv-YLk7pHEn_SgQU8EWYILB1P5izLTB9BS2tm8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
گل دوم ایران در دقیقۀ ۵+۴۵ که آفساید اعلام شد
.
⚽️
پایان نیمۀ اول؛ ایران ۱ - ۱ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/442473" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442467">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-WbOIwGQIWaZYYCnu85YBoGIxey75J-poSmi2l7goEfFLRUfpF8nhNl64A2RU0AmdLFfd3z-HK5a1lSVTZBjkQqRiXlv0D_xF1lbkNxIVV6T73fUv2HZr53gTkCcpc-ZFDF_2hDNm8CekMTG7QxY9tUfF67kMJ5uk1nsgtPw5I23GC5h7S3lz8nefFFjvTXTcWYCATOWvuhKVS_PyEie23cnADteqeeeKwxvoy2A5GkLsBVg5GhXb5kw0Ug5wBe-1gbImGOwN27vWEt2GEYFxhVl0tQtEp6h6o0cxOl-CKVUazIJByfuzL9w9NI4_6Sg8qgznio5kwEWv6fHG9bww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V04P-N6MzLbz4wP3wG2F9j83KCTJk3CIKVZcjDqK_7BKhNldwg3B8x_pWIVQmT-n8-bGHST-FijE8yGTvF4MV_37swB8g-8KeZp9yXtdPysjXtuZRp_bItnSGZ-8xWWjhc_mwqvibZc1eVhZQbomPKMGD2hVJslRVrjcD0GHyPZK5QBkQV6x7MT97mf2cfbc4usM7_R9M8RR0kC7MORyCgPEYCZIMYaP5b_dYrP5DrAavF9BXCXQKKXNf_YMb-d-Q41tKNYkbH1eC4yvd9VWo1xptTOU7jzTUAlXSz8kF_Z_jdSvDmQaVujYs2xu3we0jjDPkaGz0JaUbSOJTIi4EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KymhPAoW1jlHPakU_LCtIih9_ogUCm0-pxkwmZe4drZx_kOOQZFnHOQrCQHXCP078X6C-56h701FNEXbrA25mz1CZ6zM-YV-lgpne1pS5Bwvo6C8uKjwOOqWHQRlsPdjA8duoMrIE3TurO1rnsxMjXi_Idu995PgBvx7C-Mk3PI1XwxVkUQAHmznrS5bZatdfZz7vtujmqM1rF-3iEG9j_tcOhalSl7KkK-eIehHnxpz3_W87TD0JXWo1G2tvNKz6nG_Bbo1Fl1hODzwwFdItgKoN22W5Ne7rlUK5rHf3yel_K7feJXyc5MSMuV1OuxxoBw4-lFM16N0PBoK-6tf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iECFVrTV69lgZiuizYI9HoqFGDiRvMi-LE0lucqWHuDk0Ao_lrgwFkkgd7Wk8a3hA3Sr2CCawOt-ZIY-_WIDGRHKe4ZdMCI2eDCn1R3XYmmiE4N6fI6SH3EAIfJkYoZY7BXdIatlrhAyn6TFqvF6I-V84hXpjKRaVgAggvcdUgIOoz3yrJ0aOstZzTnJmw9thyU1xjmaivMJt1QLVDAn55QyWUB_NQznFTDa1XCNpAnjFycW_NRyadPivTuay262dabbw923EPEKUs7r16wMgdW_t_rjFjtWu9aUp08SWLgbuSyrO8UKwTvzS44Sw4jUxXer6DBhTqxPAdi4igJi6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PwNwMfbv8IUmtDFmevxYLaO623Etrx6wc6KGre6IhsSqzcps2-Wh7WQEAJ2KCjWZobGDLSL6FgcB3cG1SBLRldC-LXPH3WGu_671MzkdZTMoRjFKC1o6EMZytiDQujJzVa4_VtRU_VTUfVwIKUkS_zBBXyKST1e0SbS8ib7wSsOc4hB5UH7NHHBUPb78gHlf9UPP1iyr0_Dok1g9QTefR4HLIYat2bfZasSsO4wRqwymXIRZeJnIgYuGdl1NmD0zxXaklGw22_2AbZAgwK-Iu8MIZkhBMVytExx95es4sBb95xWwrvl8CRy7LYvYHQ_ofWGUGBAAQKFpjsFCO7PAOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuiKcH3cleppzlMfiMIyqEr5ckHq1F-dhzogwj5uZtlSoCZFDUH3-yvW2rqZdcn2LA4UPxmdzV2yu4i8JXOAW1jrDYQP8w-TBnnAJ5nopz55HwGZrcn1BflQEQFD2Y1anG-lahs35dW5XH-Xrug8gd7CytHwtgzHB2oy7-nO3ymgijwCEHnOANeDTwqUBFsrIHG6q0HdnzivlRzkLNDNn1mEHruhi5dKw03RiGkKiLNXGuPMWuWAcDAMIRasoQIY2zqgg5_IOee4oVsKLZitQvBUfGLp08feyX2bAySZwC-yQltKcehfEB3__R4EpIbmf4rjpiMeKCd95rjHUZiSUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
شادی بازیکنان تیم ملی پس از گل اول ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/442467" target="_blank">📅 05:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442466">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ccac3f33.mp4?token=tcj-6MSn7qtPyq7AxQbXQQvrto50iGEmWmNHy7yphm77LmGfhnMd1TxOQThpyLxb5nwSfYO-loqc03qMIjHLzWwnJXUb0jAnAA123indM38V2fj7qm4bKnu5R31NYr4DcQUXYyz01CSDxRpnoLS5A7JI-xpMDrVtpplOwYhX8iNcrE24t8JPM3kfp9koAMxPjUqp5vKpQDLU_3BkBD1N8k0D8sYet2NoHQeZStxbw-3gBKxOwScr7xAfxBDIEqwvuedDKSWQIhtzmxID0DOzg-SYOwcJzsHSfKhf3NbNkDiucsyxPr04A3bKIfUcAFFyFYCyzyPBYVLBXQ7iA9qaRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ccac3f33.mp4?token=tcj-6MSn7qtPyq7AxQbXQQvrto50iGEmWmNHy7yphm77LmGfhnMd1TxOQThpyLxb5nwSfYO-loqc03qMIjHLzWwnJXUb0jAnAA123indM38V2fj7qm4bKnu5R31NYr4DcQUXYyz01CSDxRpnoLS5A7JI-xpMDrVtpplOwYhX8iNcrE24t8JPM3kfp9koAMxPjUqp5vKpQDLU_3BkBD1N8k0D8sYet2NoHQeZStxbw-3gBKxOwScr7xAfxBDIEqwvuedDKSWQIhtzmxID0DOzg-SYOwcJzsHSfKhf3NbNkDiucsyxPr04A3bKIfUcAFFyFYCyzyPBYVLBXQ7iA9qaRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران توسط رامین رضاییان در دقیقۀ ۳۲
⚽️
ایران ۱ - ۱ نیوزیلند   @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442466" target="_blank">📅 05:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442464">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3f08a530a.mp4?token=N97s_iv0HMM7GeUS0Had91wpASzJtqHufHRi34Xre_uhKVbvAFoohhEaV-KxYiohmqAjamQL8Od9b0AbhkhfrLKZSGOkfGgqCpeDXRUFbfOIwmod6UsO86koZfdAfHBJ6Su37CtIxRRHoUEVjHo7A2MMQVr43WC4b6lgFl4WEhumPLI2xvtE2JI5Mg8CXJRGL77OvOS_UTtvhPFcic32QN3JbVhHQQhoy5XQhcCGoDvOnyxto5agZumA_UT6KMm34CuunKEok459Sf8KYOSjX4ecmJjQMxNfdYzA-FuUQvqSMK4lKksFUawBAJnh4X592THKvsUbB_7shbZGi7kjlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3f08a530a.mp4?token=N97s_iv0HMM7GeUS0Had91wpASzJtqHufHRi34Xre_uhKVbvAFoohhEaV-KxYiohmqAjamQL8Od9b0AbhkhfrLKZSGOkfGgqCpeDXRUFbfOIwmod6UsO86koZfdAfHBJ6Su37CtIxRRHoUEVjHo7A2MMQVr43WC4b6lgFl4WEhumPLI2xvtE2JI5Mg8CXJRGL77OvOS_UTtvhPFcic32QN3JbVhHQQhoy5XQhcCGoDvOnyxto5agZumA_UT6KMm34CuunKEok459Sf8KYOSjX4ecmJjQMxNfdYzA-FuUQvqSMK4lKksFUawBAJnh4X592THKvsUbB_7shbZGi7kjlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول ایران توسط رامین رضاییان در دقیقۀ ۳۲
⚽️
ایران ۱ - ۱ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442464" target="_blank">📅 05:08 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442463">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8c3438698.mp4?token=ZSZ1DpKxkDw1raJV7ww911KjESzA2ldACwE6YOwWwmCW6x-nNjHpPAJM4RmNSFQDXehujmkbmCnXv7rWwCq8j1i_YjtvvYaF4j_U7_djIo_w3r6zgRLfv_qgNwEroyb_2aykRePI-GtSE4RugMByA32T9bIz2n21ptdQgH7PdkkJnLr1Jt2yI4TCtFHoFHCtgpBXh9PQSw69ZOYApq4JKaenYGgk1Trx8Ioxy6HBGOGQoov3nWRL8fa7aspM5tx58UhP36YyQxgHow1HhK0H6pMFkpMqrBlH0rHH7qL8MiW7vTMUog93Xo1NxYfBOCRqEdB9LafWskpH2So_rL9SxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8c3438698.mp4?token=ZSZ1DpKxkDw1raJV7ww911KjESzA2ldACwE6YOwWwmCW6x-nNjHpPAJM4RmNSFQDXehujmkbmCnXv7rWwCq8j1i_YjtvvYaF4j_U7_djIo_w3r6zgRLfv_qgNwEroyb_2aykRePI-GtSE4RugMByA32T9bIz2n21ptdQgH7PdkkJnLr1Jt2yI4TCtFHoFHCtgpBXh9PQSw69ZOYApq4JKaenYGgk1Trx8Ioxy6HBGOGQoov3nWRL8fa7aspM5tx58UhP36YyQxgHow1HhK0H6pMFkpMqrBlH0rHH7qL8MiW7vTMUog93Xo1NxYfBOCRqEdB9LafWskpH2So_rL9SxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صحنۀ برخورد مدافع نیوزیلندی با مغانلو، که داور دستور به ادامه بازی داد
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442463" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442461">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/259f717fd2.mp4?token=YNHTYyVNpikkUZHdhPeONsxgHSsOaZ2x4cOmzWqE6JZ1tKWTNfFeNxcN_iLXcsMpa-OhMsyMAZLB4Bh9xQRc316OtGmjiPRitUooyW3hLKqbzAGyhk701XF6-nQaYq-nAyiuevUsO3DpgJoG1Yyur33k4yTO2Gr_uOOn2GDwXq1my3nCzWlOFld2Gl8UWr0F8Kk_gGS01OWTogyZ84rbygX0Pmy3pQ3IKBzTii9_0BY6q8ZQOQGWqOQkqaT3434M6Zmu0150qYxXfCFAzCqHs9n96P2Sxg2FvpRFyX10O7cSIgkp8-E93OgjUL1wRdy3ezXeiIB0lbbsX_41JKTxwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/259f717fd2.mp4?token=YNHTYyVNpikkUZHdhPeONsxgHSsOaZ2x4cOmzWqE6JZ1tKWTNfFeNxcN_iLXcsMpa-OhMsyMAZLB4Bh9xQRc316OtGmjiPRitUooyW3hLKqbzAGyhk701XF6-nQaYq-nAyiuevUsO3DpgJoG1Yyur33k4yTO2Gr_uOOn2GDwXq1my3nCzWlOFld2Gl8UWr0F8Kk_gGS01OWTogyZ84rbygX0Pmy3pQ3IKBzTii9_0BY6q8ZQOQGWqOQkqaT3434M6Zmu0150qYxXfCFAzCqHs9n96P2Sxg2FvpRFyX10O7cSIgkp8-E93OgjUL1wRdy3ezXeiIB0lbbsX_41JKTxwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوت طارمی به تیر دروازهٔ نیوزیلند خورد و گل نشد
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/442461" target="_blank">📅 04:59 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442459">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cc9656da9.mp4?token=cA8rh1UZTqyu6eJVyJBR4DerDXPgbymDfXtj9FqSanry9JesEaDOtTZhSUEplu8C9yA6f87_4jULmhhSnhpBWL6ADWcZ6MRL3hduI8F8ahzRLgRFHq31w3pGJ1l6AeB5DqcXQFy-x9X5BTraz66X6SnUXPdsnaiZOtoba6HXK4pEUdO8zgwr0JDXNEvDIPKk1uFpLCNlGu10M4q1naWCnMYcsb-xHiBsFUhjsysDjGGL7gsEsLE1MVghtFxX9KPDGT_M5c6smJuvQPMgA6yhWlr0oE91Ef638zSfOmTgSPar3aLsns7nZOEe98Oyw-Zv7Y9p7b3UGzTCKL2f3LHzCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cc9656da9.mp4?token=cA8rh1UZTqyu6eJVyJBR4DerDXPgbymDfXtj9FqSanry9JesEaDOtTZhSUEplu8C9yA6f87_4jULmhhSnhpBWL6ADWcZ6MRL3hduI8F8ahzRLgRFHq31w3pGJ1l6AeB5DqcXQFy-x9X5BTraz66X6SnUXPdsnaiZOtoba6HXK4pEUdO8zgwr0JDXNEvDIPKk1uFpLCNlGu10M4q1naWCnMYcsb-xHiBsFUhjsysDjGGL7gsEsLE1MVghtFxX9KPDGT_M5c6smJuvQPMgA6yhWlr0oE91Ef638zSfOmTgSPar3aLsns7nZOEe98Oyw-Zv7Y9p7b3UGzTCKL2f3LHzCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیرانوند ضربۀ بازیکن نیوزیلند را در دو ضرب مهار کرد
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/442459" target="_blank">📅 04:57 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442458">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba11b250.mp4?token=V31Q6wDp7_nUoO-5WOkdEhlMIi5mCBTkXbHYjShRGsuxJp4MSZCcPKJ_D5pNrSaXzgof6XEKzqEzW0IJwEHKMGYzZ5QbkgKpkfwnaTF5QJaBCD8i2Qsj1hd-YvQ5RHGVxXL2rC0_Xq4ZV-xEAwjpIfga4rv4_CLKmBAgufMjuh_jI22YPUorjGWe4ami4TbJtTfzY9_u2kdcVpfWMb-I4SgH_zlqoS3svn7VCZ3JLNr9EkZ8zVA7e9AuuoHGtN62YGBtco1_l4H8ALmWdlUpWjliHSsUrMnZ9tLREe0wT1Z6579fMptMpkGVZgJn6S_7QEtLPIk49vSaEiZadi6ySA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba11b250.mp4?token=V31Q6wDp7_nUoO-5WOkdEhlMIi5mCBTkXbHYjShRGsuxJp4MSZCcPKJ_D5pNrSaXzgof6XEKzqEzW0IJwEHKMGYzZ5QbkgKpkfwnaTF5QJaBCD8i2Qsj1hd-YvQ5RHGVxXL2rC0_Xq4ZV-xEAwjpIfga4rv4_CLKmBAgufMjuh_jI22YPUorjGWe4ami4TbJtTfzY9_u2kdcVpfWMb-I4SgH_zlqoS3svn7VCZ3JLNr9EkZ8zVA7e9AuuoHGtN62YGBtco1_l4H8ALmWdlUpWjliHSsUrMnZ9tLREe0wT1Z6579fMptMpkGVZgJn6S_7QEtLPIk49vSaEiZadi6ySA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تکل عالی مغانلو مانع گلزنی وود شد
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/442458" target="_blank">📅 04:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442457">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/666ec3016b.mp4?token=fimf8DTCKZdzmm_zXC_SHiAMXmq6in1VEhDnz9ZFYm7UhlE3I7_MdG1SRIkpE_tvRvWU3gThUJ_hlehyJ33BdtHDjNtRdvPs1RHl9lF7N4NmrJwIh65tidbupRxsQIaBHu0gIRdKLie1wpVR7n5A3ycPmuT6tra0wuHbhOlccvMkMRZOo2SDF-BuHB-78hzXCUtfgoHOCL34gC0uzrUG_7fC57XO36TJJoUVUIkkiVpN7M8DubX6wswUdG-1Rs9VepQCUX0z3uGleIGJZBIkdJz1i_d_ZwrSJVoB01q3vPCy8082NNREk7Tac1GiyaHlSYtgOWcgwhgjrQAOa0hdmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/666ec3016b.mp4?token=fimf8DTCKZdzmm_zXC_SHiAMXmq6in1VEhDnz9ZFYm7UhlE3I7_MdG1SRIkpE_tvRvWU3gThUJ_hlehyJ33BdtHDjNtRdvPs1RHl9lF7N4NmrJwIh65tidbupRxsQIaBHu0gIRdKLie1wpVR7n5A3ycPmuT6tra0wuHbhOlccvMkMRZOo2SDF-BuHB-78hzXCUtfgoHOCL34gC0uzrUG_7fC57XO36TJJoUVUIkkiVpN7M8DubX6wswUdG-1Rs9VepQCUX0z3uGleIGJZBIkdJz1i_d_ZwrSJVoB01q3vPCy8082NNREk7Tac1GiyaHlSYtgOWcgwhgjrQAOa0hdmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول نیوزیلند به ایران در دقیقهٔ ۷
⚽️
ایران ۰ - ۱ نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/442457" target="_blank">📅 04:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442456">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d8601fda.mp4?token=gw93yHaU7h_tfmRegjZLjO7XnIWR04Skx1LJ1aB7n99oOXwEj657d-VYY9CiG1QYprzjRowTkk3a-NcjTLfwEFqLmn9jH7RfFmrkmSuBckf4GxWkU9ypsg_bLZLKWz9HEmA6AV9SmGmAKHoAD7XDWrdeJ64ptTzSbwz_WN5BeqBEsbBvA85cDECkSQR7lJ4cZbyPqngRTY-S5fytgrMrrnzC84WZ-aVPNb5XNJvalKno59R9YqvAryOUR0-ZQOyC2kkIFBak3GoZ7uo6FrEtF2lAao2pL-ffltlo0uqdB3q1X_LyMPbelE9uqNnMXcO4GJdxAhQLjiHXAPNUxxF70BnwLTDV8pUQtv9NF_NpARilDYvKJXG19M3p7wiZIGasrmvb8JlC_NRvSkxnhLb7D7mtN_nY5jijv2U_zfM6AEVPgBnk87SAt5Z6iUE8Lbkmq1CBU7sSrhl4PB-e8MIFkxBIG45iEXfraoY72nALgkMd2wm6VL1nyfRgVYi7L1jk-QeJjInNC8TtLKf2CxwoHaIZD344bE-pVBhea8UDHyomqGOwePB-DNXShRhiWuohNLV3g7NQzVhgWeIv4AcsNAAam6k5RCzV3VdD72KjRMnzwuXDrfkemJi_SBSg75A_3F_kyG9C6GlDdZwSkWRawY5-xaa2ndfD3hjO6MOA8aM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d8601fda.mp4?token=gw93yHaU7h_tfmRegjZLjO7XnIWR04Skx1LJ1aB7n99oOXwEj657d-VYY9CiG1QYprzjRowTkk3a-NcjTLfwEFqLmn9jH7RfFmrkmSuBckf4GxWkU9ypsg_bLZLKWz9HEmA6AV9SmGmAKHoAD7XDWrdeJ64ptTzSbwz_WN5BeqBEsbBvA85cDECkSQR7lJ4cZbyPqngRTY-S5fytgrMrrnzC84WZ-aVPNb5XNJvalKno59R9YqvAryOUR0-ZQOyC2kkIFBak3GoZ7uo6FrEtF2lAao2pL-ffltlo0uqdB3q1X_LyMPbelE9uqNnMXcO4GJdxAhQLjiHXAPNUxxF70BnwLTDV8pUQtv9NF_NpARilDYvKJXG19M3p7wiZIGasrmvb8JlC_NRvSkxnhLb7D7mtN_nY5jijv2U_zfM6AEVPgBnk87SAt5Z6iUE8Lbkmq1CBU7sSrhl4PB-e8MIFkxBIG45iEXfraoY72nALgkMd2wm6VL1nyfRgVYi7L1jk-QeJjInNC8TtLKf2CxwoHaIZD344bE-pVBhea8UDHyomqGOwePB-DNXShRhiWuohNLV3g7NQzVhgWeIv4AcsNAAam6k5RCzV3VdD72KjRMnzwuXDrfkemJi_SBSg75A_3F_kyG9C6GlDdZwSkWRawY5-xaa2ndfD3hjO6MOA8aM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمایت خانوادۀ شهدای میناب از تیم ملی فوتبال
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/442456" target="_blank">📅 04:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442455">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VlLqyxvET5P6MinwPbUkTX2x78WqWXp9aVFH1jC7P-vTo760CrmlLx-Moeep7qlCLIm6mhB18hxaC3MAoi3iHL-L4iZJkDPVadHznQ4tvX9lTJ429h3bdvlnO2-onUS1_hRn0lykh-2qOQ2M7Gz6j1TC67LdVAVz1zIuiZZFnn8Ro3Xx96JOfkCdmTKM24vft-RLlTjNqZ27IhLeLv7_eNo5pql01CsQzjGQ_kTU72mtHRxIKT2C9aG-qnkR2RYPPFyLE0SS3_SlnCaeQVehE4CQWEqJ9vsmkGk0Le-iuGvZfaHY3qJTv_CXEBMSRrUvP--cYN_HzXqcXI5C5IhzFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
عکس تیمی ایران پیش از شروع مسابقه
@Farsna</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/442455" target="_blank">📅 04:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442454">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d6d9fa8a.mp4?token=CBJUpkxv3A-WyJ8pT34tKeDiJOlvrykhnetkO0wuAw6Wl3LHIpLx2fWjpC7P_ljIg9EKg7TWrKmmYxWj14AdlvwiEpo67mYfbMdEZkK9rYgE8IW2zoBERUDlyFnKfkfV3NY50CbhsGcoY4CjxZcwcVm3Lh3WGp0egbqa5vw2fODpck9UW9RRVfObQxaxL5iR0PBICWzvXUZ63yU6ftKtis17g_zdDsY7-IVw_cfKGXE85t0Rci8sPYQ85wKVwbJ3ZuqfKaUFTgDiFuSFZQ5w-CHi1WMwvAguHr2SyqjY56VriroaIBcfDi5jes7o6WhGFrNCZ34N8c3MB3BbQrEmdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d6d9fa8a.mp4?token=CBJUpkxv3A-WyJ8pT34tKeDiJOlvrykhnetkO0wuAw6Wl3LHIpLx2fWjpC7P_ljIg9EKg7TWrKmmYxWj14AdlvwiEpo67mYfbMdEZkK9rYgE8IW2zoBERUDlyFnKfkfV3NY50CbhsGcoY4CjxZcwcVm3Lh3WGp0egbqa5vw2fODpck9UW9RRVfObQxaxL5iR0PBICWzvXUZ63yU6ftKtis17g_zdDsY7-IVw_cfKGXE85t0Rci8sPYQ85wKVwbJ3ZuqfKaUFTgDiFuSFZQ5w-CHi1WMwvAguHr2SyqjY56VriroaIBcfDi5jes7o6WhGFrNCZ34N8c3MB3BbQrEmdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همخوانی سربازان ایران
🇮🇷
پخش سرود ایران در ورزشگاه سوفای لس‌آنجلس
@Sportfars</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/farsna/442454" target="_blank">📅 04:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442453">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🎥
ورود بازیکنان تیم‌ملی ایران به زمین
@Farsna</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/farsna/442453" target="_blank">📅 04:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442452">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3133c8fd.mp4?token=UdAJQQNE3iq3m7YZlGuzi4gpDncTQLLGobOtQpFKq7lMieK8bVA4CN1wRBnAxnIxQHXFZHsOoeK_uGvowVWUZ-q_w5tNynRqhahuLTqSq6FbmgmGgne32eadHi41lKVUIWsbnmZa4I-Q5AQ1gfkExxlg_UWDN3_6Yzxz2LFqImo_o7_1L_I-0RoyDAOofGGnBk8cdXJfkFr5yC67I6qz2erR8b0zWqlV3qjh0hOGMUqmvRkrMOOMMiT0FTb5zTgRQRN7LqjsrXdliTo6xHfWevpeYC9HyM6gYym0s72jRRkY-YK4cQ7k7CEfPV7fYp6jwXQc3divZMHXXXzhWmjLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3133c8fd.mp4?token=UdAJQQNE3iq3m7YZlGuzi4gpDncTQLLGobOtQpFKq7lMieK8bVA4CN1wRBnAxnIxQHXFZHsOoeK_uGvowVWUZ-q_w5tNynRqhahuLTqSq6FbmgmGgne32eadHi41lKVUIWsbnmZa4I-Q5AQ1gfkExxlg_UWDN3_6Yzxz2LFqImo_o7_1L_I-0RoyDAOofGGnBk8cdXJfkFr5yC67I6qz2erR8b0zWqlV3qjh0hOGMUqmvRkrMOOMMiT0FTb5zTgRQRN7LqjsrXdliTo6xHfWevpeYC9HyM6gYym0s72jRRkY-YK4cQ7k7CEfPV7fYp6jwXQc3divZMHXXXzhWmjLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پرچم بزرگ ایران در ورزشگاه لس‌آنجلس باز شد
@Sportfars</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/442452" target="_blank">📅 04:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442451">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50bb88373f.mp4?token=jKyAcwwzACdCd6L9CXFVPfwnAli_LU25eURAfbYj1bjl6Z1iP1n1E5vPmvzO6SZC_L2O8e62baNmm83YWQmT1rpjWAEN7KG7Q-XRzAIN5SbYSGl2fkhl6QiEAx9uT52AYcWDKgFtErV46TnHYNcCvPEdttIKrfwtvGnl5CivkSw8nq0ugpuGUkO8sRlqzQ3kNFpRlMrup48Phkj-lMxkQceqrAtAz3_rVn3X69UJcl7UNbxvkxYVp9g8wUXOFthb09Q0LAdW5dd5Dy3dxf-6dm_nx5HaYNoAY2tWqH19TPglREwflWB57IZrwcso2Z8Uth_6DYPBtD6NE9bJf2Or73BmOMWf76M4xI7mNlt5P1S2SwNzveVsPmCc5IYGeRhSq2ftKo_qCVvBLExjChQsjhMzd0tGKUJaooXZ4PYg73-pvyJq2b1HnJ7wxd1gJeHannZurUwB-1A8k4Z6vsWT9GYKUTRtMDIBWZknQueoE_Hg5C3ctDcz2NpmIyshgiPMpJ9_Y4fx-JMVuenKdtqHFVyGjEOjuHgaBHaflOT03TltWxgMH4y1bcCuYGSugNI9DLtJBldSPZjXp3SEq69HDQuatnMZrDEoz3Upzw-Nt2_YrrdnTMjvCTgl3idVkRqZUuBnPf4DpILd85jGDnQ4lTnVyAfh-KMp7yKrnRzIP_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50bb88373f.mp4?token=jKyAcwwzACdCd6L9CXFVPfwnAli_LU25eURAfbYj1bjl6Z1iP1n1E5vPmvzO6SZC_L2O8e62baNmm83YWQmT1rpjWAEN7KG7Q-XRzAIN5SbYSGl2fkhl6QiEAx9uT52AYcWDKgFtErV46TnHYNcCvPEdttIKrfwtvGnl5CivkSw8nq0ugpuGUkO8sRlqzQ3kNFpRlMrup48Phkj-lMxkQceqrAtAz3_rVn3X69UJcl7UNbxvkxYVp9g8wUXOFthb09Q0LAdW5dd5Dy3dxf-6dm_nx5HaYNoAY2tWqH19TPglREwflWB57IZrwcso2Z8Uth_6DYPBtD6NE9bJf2Or73BmOMWf76M4xI7mNlt5P1S2SwNzveVsPmCc5IYGeRhSq2ftKo_qCVvBLExjChQsjhMzd0tGKUJaooXZ4PYg73-pvyJq2b1HnJ7wxd1gJeHannZurUwB-1A8k4Z6vsWT9GYKUTRtMDIBWZknQueoE_Hg5C3ctDcz2NpmIyshgiPMpJ9_Y4fx-JMVuenKdtqHFVyGjEOjuHgaBHaflOT03TltWxgMH4y1bcCuYGSugNI9DLtJBldSPZjXp3SEq69HDQuatnMZrDEoz3Upzw-Nt2_YrrdnTMjvCTgl3idVkRqZUuBnPf4DpILd85jGDnQ4lTnVyAfh-KMp7yKrnRzIP_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معرفی ١١ بازیکن تیم‌ملی فوتبال در ورزشگاه سوفای
@Farsna</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/442451" target="_blank">📅 04:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442450">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfc9fa056.mp4?token=ux20k2RtSJkXcUYL2TKInyeQXClCLPrqwMD0856a1IFtzlXPFDdf50Ua-ddzxcINhgSs61slPby3_nIS0d19wK1yq7ETy-hiQJEC7x_y01yQtGt2Kt8yfodrUMe0jsfeElhYkju0ZV1RJPODk9DRPD1_GVqjyxpuhfVstaXOAsIBmtOswRfEqwsWk6vCvwgFY2GO_KjgLf2pY8ibh8VcOZmBuIx-qI8OCOkoebX2Gg7X-Vr8a1_I-M0datyXr81yPHIIJ4pPpNAOnI1uZY7eAvgMVflnLXrNtGjcS5AoLB9d1JgdD5X8xeTBED1XyScF8SY4iyuwGjLl-DqdFqI76w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfc9fa056.mp4?token=ux20k2RtSJkXcUYL2TKInyeQXClCLPrqwMD0856a1IFtzlXPFDdf50Ua-ddzxcINhgSs61slPby3_nIS0d19wK1yq7ETy-hiQJEC7x_y01yQtGt2Kt8yfodrUMe0jsfeElhYkju0ZV1RJPODk9DRPD1_GVqjyxpuhfVstaXOAsIBmtOswRfEqwsWk6vCvwgFY2GO_KjgLf2pY8ibh8VcOZmBuIx-qI8OCOkoebX2Gg7X-Vr8a1_I-M0datyXr81yPHIIJ4pPpNAOnI1uZY7eAvgMVflnLXrNtGjcS5AoLB9d1JgdD5X8xeTBED1XyScF8SY4iyuwGjLl-DqdFqI76w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صدای پرواز همای در سوفای پیچید؛ پخش آهنگ تیم‌ملی در ورزشگاه
@Farsna</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/442450" target="_blank">📅 04:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442449">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYKQoF2fKNj3F4TdrUi3xtd8mws_u66NR6HE-qZFNBhYpcBSgyV97-QkC5mlrphx5tmK7lYt-4Q1Tfv5xIpNLTEuKwpLCdhW2EJv0dbwOmIF28WHBmiQkO5f9TUIp85e9wHZLlYf6Kice8Raez0AZJkqtYGPMU1X0Lsh-Adxo_n4qXSW7FinNI8wjlZqOUDfN6VhS_4idZajCZQt5PGfGVWSUc9AEOyn2cS3XIRn5SquKi_jfHR8606eyc_1F-0ci88dSU4f4ofyvHNsZH71JwqmLwHiGk6-FWnWZLbpjbiurAjE3DkscbxyPV7shuhBu0uXRDIwlHVm083qSmWabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قلعه‌نویی: شرایط تیمی بسیار خوبی داریم؛ با تمام انرژی برای مردم بازی می‌کنیم
🔹
سرمربی تیم‌ملی در گفت‌وگو با فیفا: بازیکنان باتجربه‌ای داریم که برخی از آن‌ها دو تا چهار دوره تجربۀ حضور در جام‌جهانی دارند. مطمئنم با تمام انرژی برای مردم بازی می‌کنند.
🔹
نتیجه دست خداست اما با وجود تمام مشکلات مانند ویزا و کمبود وقت برای سازگاری، شرایط تیمی خیلی خوبی داریم و بچه‌ها مصمم هستند یک بازی خوب و پرانرژی با اجرای فرامین تاکتیکی انجام دهند.
@Farsna</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/442449" target="_blank">📅 04:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442448">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BItQt2laliadojVDl7rOawmx69A6Ia-ulNOxBGFHPv7ufUTS_01zJjeoybbsoyWaKEvuC39MftHCybsJstS3lhbG24wTjk9FvldVYErbznHENQX3Q7EgvfQhxtZVSTJxcJc4K3fcMTq0k7OdRdTLYSqZv16bX8BGUl1Q6oAa5pPDcrDt2G6Zp9R19JOqgqyMhYyU_weaenFS-T-Hghx6TW0mecmANbad2OeDzq_uQfTFMfmKowhwGQq8QrgqHUPkoZ0vreSniAGiEKWLZV2XfU_nqpVqzVAD74xcXmpqkBqZZFyZMcWLD0aa5fjHvyq2AF2TI2tQ2w2_4KKqjaIPIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌فروش بلیت قطار‌های مسافری تیرماه از چهارشنبه ۲۷ خرداد آغاز می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/442448" target="_blank">📅 03:58 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442447">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030daf485.mp4?token=LAugZIMlPmfIwTohJCI1aOXiHbxD6X-Jqi2EpcNeu23Momr7g-HK2dqpeN7G2kQio0IJXSvxCn_qjXUsG8wqkLoclx7aJ6nEM5vfR0appJAFdxyTsZd7o7Nxxh_sTSHCVyueImeWVy5rU73wvfmNkZHLrge_ZFDFonqom5-2JJC4s3p__4kSFX4V5yL2RXVepyK1t03xPbmjoxPb7A8346vKUrDUrAhq4M3qSdS8EEQIlucKB7x8Z8F2NswGEdvmgUuhwVrgZTktqHJnJgpT2NVmCqFZ3rlTISduy6lEzlXC8jkcdVMjuD9MqNK0TAog7DccYlNRCtIqy1BHi_J0JnwCuz1LqYS8wQZZyrSvL1g4833lZhZkY_PaeJObj-9RcUmCST2GEkycbJfpG7ARoPkCH2UPwf3QkCt2I0WNPklAsZkx8Qr2efsi0_2v7JrwqGQzQlhKi864jcQck2YM3ZF_pZpeZmZyuwJdmyHHGH-qavjtNZ5zpdcGFIvnFawcsgnTB655sYuGMbpJTQRXBuzxHVz5TbauEdZCt5HOtiuTVALBJ6-ntCJA9AzBRp-rkqKi9U_MBdqgqqvBcUvRyb6t8Jy-bDwuGALHFIAWfgLGZsPbEuxinA_PRpEPrEHWIf5mA1ZCfeBdXb2lmy6k9l7hjiZVD6iYEJytPeLu1zM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030daf485.mp4?token=LAugZIMlPmfIwTohJCI1aOXiHbxD6X-Jqi2EpcNeu23Momr7g-HK2dqpeN7G2kQio0IJXSvxCn_qjXUsG8wqkLoclx7aJ6nEM5vfR0appJAFdxyTsZd7o7Nxxh_sTSHCVyueImeWVy5rU73wvfmNkZHLrge_ZFDFonqom5-2JJC4s3p__4kSFX4V5yL2RXVepyK1t03xPbmjoxPb7A8346vKUrDUrAhq4M3qSdS8EEQIlucKB7x8Z8F2NswGEdvmgUuhwVrgZTktqHJnJgpT2NVmCqFZ3rlTISduy6lEzlXC8jkcdVMjuD9MqNK0TAog7DccYlNRCtIqy1BHi_J0JnwCuz1LqYS8wQZZyrSvL1g4833lZhZkY_PaeJObj-9RcUmCST2GEkycbJfpG7ARoPkCH2UPwf3QkCt2I0WNPklAsZkx8Qr2efsi0_2v7JrwqGQzQlhKi864jcQck2YM3ZF_pZpeZmZyuwJdmyHHGH-qavjtNZ5zpdcGFIvnFawcsgnTB655sYuGMbpJTQRXBuzxHVz5TbauEdZCt5HOtiuTVALBJ6-ntCJA9AzBRp-rkqKi9U_MBdqgqqvBcUvRyb6t8Jy-bDwuGALHFIAWfgLGZsPbEuxinA_PRpEPrEHWIf5mA1ZCfeBdXb2lmy6k9l7hjiZVD6iYEJytPeLu1zM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بازیکنان ایران در حال گرم‌کردن هستند
@Sportfars</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/442447" target="_blank">📅 03:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442446">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639510f858.mp4?token=BGAEi3c1sEnCV2rZQzetBH9siB1WrmW6xzbfWXro1VE99EgFq3zbMOdt9z1t2w0C6jI9cnROnb1FwRWjbzc-FBgW7OXKLfCOkaIl3gQf8HIb3zKliiinwwQTg0L8IAUlV10Lsk5bWSc0BGQsS4Dbld-2mUrswS8TWz6KN516RqO02J45HjFl-pU3BIZgaJoHR8zZhWtVAmRLoIoZUFsriaNwEWewodWlM8mOR08CpydNsSsbFBRg8DHxHNPTRf4hsR2d9gsbMw24KxkwIAwRAP7kK2wWUEsv1nIOX2ja1NBk5hzPjMC-MlkoifYusNdNAkzff6627pqYMxQtNkhRlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639510f858.mp4?token=BGAEi3c1sEnCV2rZQzetBH9siB1WrmW6xzbfWXro1VE99EgFq3zbMOdt9z1t2w0C6jI9cnROnb1FwRWjbzc-FBgW7OXKLfCOkaIl3gQf8HIb3zKliiinwwQTg0L8IAUlV10Lsk5bWSc0BGQsS4Dbld-2mUrswS8TWz6KN516RqO02J45HjFl-pU3BIZgaJoHR8zZhWtVAmRLoIoZUFsriaNwEWewodWlM8mOR08CpydNsSsbFBRg8DHxHNPTRf4hsR2d9gsbMw24KxkwIAwRAP7kK2wWUEsv1nIOX2ja1NBk5hzPjMC-MlkoifYusNdNAkzff6627pqYMxQtNkhRlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از ورزشگاه سوفای لس‌آنجلس، یک‌ساعت مانده به آغاز بازی تیم‌ملی
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/442446" target="_blank">📅 03:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442445">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbE5wqVV5LZqnOC_oayuYP9KQA1ez4FanzbTNEOEy06a0v6x12R8-YNZ8lxwAOIlXkki9Qm652OjhYl5nhCBQyY8X4mKIxkRKBZWAfI7SxDcDBT5Qy8Huoy4UObOgUuvo5j3NzUsX5YYAck0imnGnCci4Fy539myItQ5LEu4y-Fshs7n_JMMxLGic4SE-zw98kYofcyQJQ1N0PRNZ6njv2DdznQ7EatH2uRWQ_PZR_1xFb9EKu5Ps9sAZw-ncbH9NFvl_N01GKlPHHuYQKEq1TOIG1VPX3F64Tn3zwIb1SJWWvqRRKwbI1uF4YwNpEd9URpmpL06DqOHjJxDyGUmyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان در آخرین دقایق برد را از دست داد
⚽️
اروگوئه ۱ - ۱ عربستان
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/442445" target="_blank">📅 03:36 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442444">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07a6002605.mp4?token=GmoNxtOylis6pPmnHqP_s0XAwEqNBg78Wi6RZmz7_-3cm2-7_GDeuoESvRd49gFLjj3-fYfVQ_lgOInAJnB-bdbpWLOgqCPqyAzLKU6dfWSbTGQJtMZEXnkyhVTKMMkVdlkFsFLQMpQi2OvEbwNQWACscrBOn_iiMr8SBQP0jFR-LxHMHOt9uj6G8w8jqiDAtROIY7tazA7S0BrfS00Xgf-Sv_QnMlc-7SdXN9MWKnkgednO4SMrllmNUmPwOYkRVsMmgrKvtdSkGLirIXmghW7rsS5W9qvcBKxilI0GJdcQ3IzKKm9P_hR4o3BMvs1AlzEnQQ9IjfKruiP9zeXQUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07a6002605.mp4?token=GmoNxtOylis6pPmnHqP_s0XAwEqNBg78Wi6RZmz7_-3cm2-7_GDeuoESvRd49gFLjj3-fYfVQ_lgOInAJnB-bdbpWLOgqCPqyAzLKU6dfWSbTGQJtMZEXnkyhVTKMMkVdlkFsFLQMpQi2OvEbwNQWACscrBOn_iiMr8SBQP0jFR-LxHMHOt9uj6G8w8jqiDAtROIY7tazA7S0BrfS00Xgf-Sv_QnMlc-7SdXN9MWKnkgednO4SMrllmNUmPwOYkRVsMmgrKvtdSkGLirIXmghW7rsS5W9qvcBKxilI0GJdcQ3IzKKm9P_hR4o3BMvs1AlzEnQQ9IjfKruiP9zeXQUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد «ایران، ایران» در ورودی ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/farsna/442444" target="_blank">📅 03:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442443">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTgSPZdRHxa0sO9XRNuNaqQA5CG5WUkUGcApwsp1p1F2_QKkZ_0_2Tgu2TKfrAh1ZDTW5l-navuR8J-kxvUwC7RxqnYfpRL6AaLWll2_rzhwVWM_iUAeoTcvLa4vqvWba7KHWSl3XrQYv9nPR01Q4h6UzFlVJeuV9PwSof2CdyY8KVbvUJg591ElIQ45UQUFf46I_etnw2F0JX7YdP8TDwacTgSwB8YcCy57SNyOvzfxwfBXNm2UtyZz8xpCCyt5Ni1Baw67i5WMW-2jm3gy7PC5kjiYqLDZBEvqG5Fl0teVEyrlyBCGCbZ7V3FbaFv0fjr0Q4BfJLJpXPjByrmBWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم‌ملی ایران مقابل نیوزیلند
⚽️
ساعت ۰۴:۳۰ @Sportfars</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/442443" target="_blank">📅 03:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442442">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">📷
هوادار ایرانی با تصویری از رهبر شهید انقلاب، آمادۀ حضور در ورزشگاه سوفای
@Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/442442" target="_blank">📅 03:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442435">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MGfh5-3nbEX9kym8mqEBOBpVCQ8MTl0KFxmM5VFXn8o1-uADFUNDyqr-9HpC0obTq-FRi1IFGYqhhgDFCXFjKIyb_1W8QP6jSQDgt-9FDBodfmsawsQIU66enCxt2keuZrFr5_p0YWtaji_eEpphpXdWCfzgJRxmNiFgIbiSKqqbEEbCCbFKOlBdpwbo2eCYWNkq6omOtiE2a_llt8R002NJIzW756pjkoYvZB_cZ-d9clHlq5aabdAl4mgqw5XV8D9U_BvL0He_spECUoZibIEvYZazxo9x4eJlzeeObYPGPVOQWtUzaoVylqrYPcnyPdoRZsKVYlJnb9rtNyS4wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bUMoYfz1GP3vheExhfcWJjp9BJ5T5w4KPZAruAHIwZ8Q-8AKVO8EUlj7-2SO3TuTLbMW2f6WwuRgwEoDF6XGCx5dhxsUms_Cu39tK_6-k-1CIo6t0iENRa-rg7yQMWtxTxgLptjS_LljnVI9MkNbVLb98aX9H7BcMpj8cXQbSfeWcMJvDS2g5_a_kOvS86Twvj2r_qy2VElhUK-bpHyBd4DY_pvt0fKbalghA6ZBK2sbW-KYmsPrMDYIkTEe30Faeltcs2Z4O3UpiFDDF5yEa2Mu7pQs4_ekJF7TeH6QEgAfxu1c949NbPl2IlpSER8fGvFqKgSN4N_FE5wawDY7HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FolUm2-7527ScYEsZhyPXOSywM-mcNlcGYvnz-jKgrUppY2irRLdqxHdsGTP43m_HaorZIUonn0qS38iKOFhhLWX1RSqZ8dp94Y7t8FG0oTB-XSmWYRMeQdUVoCGlnZsn7Q9hGGdwmbm11XYhTsEwK58XM6z8iLI4V-XDYBPKsl8lHR94DPe4tSj4bc-ZhUlxoR8c-H6tcy7iKQPMc1bjX9y3ctAu5jxJ_mH7Lk1JtFEYGdxkZK4zmGLmS7p7dCtd84IKtiS-ZgtE0lgMTJ3589UiHxBD9oMMXzA_iXM6zsDrqDKvQkD53pN7Ew5mWVuVQiBcKv7EPVOLE-Lt7KDSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jPaVBmxaxW4hGNb3QVEexyHKCTJVIGHqhRI7miqyX8GSgF3-7kE77TogrwdrhIUflIz7fsKwtWJL5BDFzfmsZMYfx_kaYYp0HNl9SOusCNC6qqMBB4I7PobaV5yWvoMmuZGO2N52eC0kj6rk7ixEChvcguErCNdyXdq7sgzlwkKFD7AoytBfMlsVsieGQE5hGTIwt2fRFYFB7CCoF6Hokls0AzBuaA7UzzP5taZizwkZ4ELjXq9q8HoPQTW0SVhuyT-T0uEK_MLdSKK67V21Gkdl_bcz6DCGRZWufdixtn5GG6Fi7qZ9ZRvr8tkM5a1LfSHCb32MQd3LIjTBOPduoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NzzQBGz41dnuW45puLm3gE-jStdvBlo-5d6cNVE3jeHlJ5ViCyoytQcGgWSVIi-j-OOCSV5a2ZRS7qKZmaj4w6R3K1UZJH7QTlyux7lSRAMXPWbbNxmZB7OrX90e3mw0_AWF71PXNiVnWigHgj2bK2-G4BE-_tXiikRb7BwN4xwv2nXZZJmkKOraPs6IFp7lYZkJ00gWlZmhjck6OskRZD-yi39B-l-2FrNw0SHaP4buCFPIg0_SG5sJxEFv3SbP4796b8Pf5mOfDwqxet4C5FnXK01W0gn26W-vMc_1ffWbZOiiFCbQyEkivXqIU0w8-WDQMZUFOnxOux_Pw8ZrnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCFPl6LoouhYg3SRXkPJRgHWQDqlx9MkLBQopabGCpcX1RLjSGMoZiOO53UNjTTxrGKxk035pAQ1naZqiG0biFeq4t-x65mbUWraXlE3JkDkRCxZqZhqNHbwlSHYx0s1EYrL3M1zfpLwykq6zpHif8OsyyDHUsJkFw9Rr3dxovJzFkdB-iqIVgKperWzyk5gcNmwY4F6VI5jJnfLYrS46-xGEorRXCGH6h6_Rhdqk4Ducjkl5D0AxuI5XGZyJWLYkp0AXdapeGOKZlZT2UqRQCrmV_NmZhh7LQonrJIjWo-rdWMdWhm2Jwx1DTkOhZh0qIswFpdKGk9hcBCeO54vwg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
اعضای تیم‌ملی در ورزشگاه سوفای لس‌آنجلس
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/442435" target="_blank">📅 03:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442434">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5coHJS81oJJB4DsLV5rSl9lXhzxP6_dE4WgBO38vGRHrqvgRdWNcdzgZhx8dmffTxl3OiZWWQLh04JUQavLcjohLhMX2RqTZTb1gAgrw7wB_hA09yH9G3H_HBa_2RYkNYZMBePxZvow81Van_F8T0MyEqIZV8iIpe57TCFYUonC4GWbXJnjKN_DmJWNfcfT7qCsonpYmqR0p86WMk-86BOtUJK9LZQx5Zp3FPcYFMcUIbB9yLVS1iq7PpWQibgVWbwg278pAEyMaRL6FIBPc72BZF_shGXHNM-9tb9GQtZQNg9y3EJC0m9JXUxQjD0wJ_HfS_str0sYabZgp1uxLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب تیم‌ملی ایران مقابل نیوزیلند
⚽️
ساعت ۰۴:۳۰
@Sportfars</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/442434" target="_blank">📅 03:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442433">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9388295890.mp4?token=MxxdVKHc9EzZv5tDOT15-A_T_0RrX1fwcj-MSn0heBdSUphgCQTq2EzSNtVFDZOsdqh-BegVZjjXoCDkqZwrxhCJ9TF11eA6lRHtyZbxSQJqHJxRVL8hWhUxjgkANZ64J7s7XMdxgdj0laUIrK6vl59V45JC6tr1nMReM4995eSHyfNcqR6vDpTcGVd-lNYjUyv3Kvc9-FYhblxseeqKYRGHVAvT1aqF2zha08lmYXCShzyPh5KSlR0ZJjKe4COz8_bWUrWgC4Og-UQYT53EiiSvD5HToOxnX50n2Cd4L8GoRQjBZtxXfQ9pk72CPdM3w9zW7R7TZG-qKZh9761wXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9388295890.mp4?token=MxxdVKHc9EzZv5tDOT15-A_T_0RrX1fwcj-MSn0heBdSUphgCQTq2EzSNtVFDZOsdqh-BegVZjjXoCDkqZwrxhCJ9TF11eA6lRHtyZbxSQJqHJxRVL8hWhUxjgkANZ64J7s7XMdxgdj0laUIrK6vl59V45JC6tr1nMReM4995eSHyfNcqR6vDpTcGVd-lNYjUyv3Kvc9-FYhblxseeqKYRGHVAvT1aqF2zha08lmYXCShzyPh5KSlR0ZJjKe4COz8_bWUrWgC4Og-UQYT53EiiSvD5HToOxnX50n2Cd4L8GoRQjBZtxXfQ9pk72CPdM3w9zW7R7TZG-qKZh9761wXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اتوبوس «ایران» با بدرقۀ هواداران تیم ملی، عازم ورزشگاه سوفای شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/442433" target="_blank">📅 03:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442432">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e1ec016a2.mp4?token=KAk_jqt6VKWUGzw7VrXY_IQvXUqcYIazyvm-wsoyqsR1E5E2Pjqcjnaofna_0vNIZS1hnEJ1J-y79xKjtsQwiyx3T6vXHVXVF6sVd9W5slwuut9IDEwi-eUAv2LE8e0oibpobXy3GrR-1PLIgxIJyfMQi6T3sYGd0EY5NQSk9rAWyjHouQMQmK7cy5Dw2J5lavPTOHDuhUa36hHgY781Dj4P5aE1-AT48UQwd_spMm7pN7-0C9nbHMQOBKrydDx3I9oR9azhIHBuUr_ndM1KS0jFTUP9wghPDRLzOK043f0SDe8J_sjtX5jwwTle_yWwkQx-Rr4vx9j42Lay5ydp3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e1ec016a2.mp4?token=KAk_jqt6VKWUGzw7VrXY_IQvXUqcYIazyvm-wsoyqsR1E5E2Pjqcjnaofna_0vNIZS1hnEJ1J-y79xKjtsQwiyx3T6vXHVXVF6sVd9W5slwuut9IDEwi-eUAv2LE8e0oibpobXy3GrR-1PLIgxIJyfMQi6T3sYGd0EY5NQSk9rAWyjHouQMQmK7cy5Dw2J5lavPTOHDuhUa36hHgY781Dj4P5aE1-AT48UQwd_spMm7pN7-0C9nbHMQOBKrydDx3I9oR9azhIHBuUr_ndM1KS0jFTUP9wghPDRLzOK043f0SDe8J_sjtX5jwwTle_yWwkQx-Rr4vx9j42Lay5ydp3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
العویس بازهم دروازۀ عربستان را نجات داد.
@Farsna</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/442432" target="_blank">📅 02:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442431">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b74d4133ed.mp4?token=SkcyoEyhT3JA9GKVV10UJazegUwAUVrG2OeT8aPUWOhcyC2pyeyxSpbFZzu77hNyAwYEKBVHSHp3NVn3bMtodXo2RpeNE-0Wc8Nq8qw0k7lwYXdC_RZX1URxr50rxdbIJP4ozAdJfCxkHGFxQEugSCLBU_49VoHVr5U_APj1jIUVworGLQzYYz7cf3CY4vCEGAg4UtkhBf9TW8bHrKeIQZXWqpwq4ZTNGQk5gpDRgvbx9U5STz5pVJfFd57wM9XSP2t_sDFuhosgClRBldnKIT-hrMHDxBkowAQ2w751JWKG2YMfCcINjKoSODK7ixeUGrR9okqsKNfV2Iq3Kol2yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b74d4133ed.mp4?token=SkcyoEyhT3JA9GKVV10UJazegUwAUVrG2OeT8aPUWOhcyC2pyeyxSpbFZzu77hNyAwYEKBVHSHp3NVn3bMtodXo2RpeNE-0Wc8Nq8qw0k7lwYXdC_RZX1URxr50rxdbIJP4ozAdJfCxkHGFxQEugSCLBU_49VoHVr5U_APj1jIUVworGLQzYYz7cf3CY4vCEGAg4UtkhBf9TW8bHrKeIQZXWqpwq4ZTNGQk5gpDRgvbx9U5STz5pVJfFd57wM9XSP2t_sDFuhosgClRBldnKIT-hrMHDxBkowAQ2w751JWKG2YMfCcINjKoSODK7ixeUGrR9okqsKNfV2Iq3Kol2yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم کرمانشاه از میزان اعتماد خود به وعدۀ آمریکایی‌ها، و حمایت‌شان از نیروهای‌مسلح می‌گویند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/442431" target="_blank">📅 02:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442430">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60882735c8.mp4?token=WQUnKM0oSP3-gCbSADrFcmX8GRykLVA7aqhk6QXMq24Wp8kMT2wrXteG-r2uHi2wmxbfPzHlUFSaYDxUkGfKK0jnyYZmprJ7kBoDDXSVhxycOZyMak4ky8QcU13ayc-BbQFJjfkQvCgAJnnzMgAE0Om5SBg6_WR5irX8D_T772FpkoLHNjREPWKUX1momRZHClEv-qsGw8cIAEldVZ9e9Z24f3ZILoTh0f6VeWaAkq7POjQhB7Eyr9VvfRYAzrxdXYZOmZqC9B3NW_Uc_js3NcdI6knbEYBY7Dp9C2yObSux8dxOqoeGf1jCaxTNfbE1SAYQ8wKiAD9mmniXf51ieA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60882735c8.mp4?token=WQUnKM0oSP3-gCbSADrFcmX8GRykLVA7aqhk6QXMq24Wp8kMT2wrXteG-r2uHi2wmxbfPzHlUFSaYDxUkGfKK0jnyYZmprJ7kBoDDXSVhxycOZyMak4ky8QcU13ayc-BbQFJjfkQvCgAJnnzMgAE0Om5SBg6_WR5irX8D_T772FpkoLHNjREPWKUX1momRZHClEv-qsGw8cIAEldVZ9e9Z24f3ZILoTh0f6VeWaAkq7POjQhB7Eyr9VvfRYAzrxdXYZOmZqC9B3NW_Uc_js3NcdI6knbEYBY7Dp9C2yObSux8dxOqoeGf1jCaxTNfbE1SAYQ8wKiAD9mmniXf51ieA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل اول عربستان به اروگوئه توسط عبدالله الامری، در دقیقۀ چهل‌ویک
⚽️
عربستان ۱ - اروگوئه ۰
@Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/442430" target="_blank">📅 02:22 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442428">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b108c8df8.mp4?token=goCDVT5-FHhqs8lWS84HeH6dW8y6966a3KlJAkWWAO9GQFiRGSPlJ_U7tmzW63qNmWjeGzMQZnJkZeeeuC5kaN34qO0IdXTIrLbCkd8vEB4lksdQMdqLQjVfOY80gFON0_zEqZTExfDW-U790NQIO1xHQoYx8teugw2Fi-Sc-3JD9WO5a6RXY0uhPx1VMlBGoMKj-zn5AOWCO0JkE9W7HAJZPu8wcOSQkYJRX6oEGx4kDHCAMwg6uuU9eTJ0536AjWymQ1SSrQPM80hqBLVgK3zyRa5gFiALywmWxftEAOYmGGmOQKA1XCnlZTOvQrlyL9nP2IEuTlHAudsQ9pP5yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b108c8df8.mp4?token=goCDVT5-FHhqs8lWS84HeH6dW8y6966a3KlJAkWWAO9GQFiRGSPlJ_U7tmzW63qNmWjeGzMQZnJkZeeeuC5kaN34qO0IdXTIrLbCkd8vEB4lksdQMdqLQjVfOY80gFON0_zEqZTExfDW-U790NQIO1xHQoYx8teugw2Fi-Sc-3JD9WO5a6RXY0uhPx1VMlBGoMKj-zn5AOWCO0JkE9W7HAJZPu8wcOSQkYJRX6oEGx4kDHCAMwg6uuU9eTJ0536AjWymQ1SSrQPM80hqBLVgK3zyRa5gFiALywmWxftEAOYmGGmOQKA1XCnlZTOvQrlyL9nP2IEuTlHAudsQ9pP5yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از بی‌-۵۲ آمریکایی هیچ چیز باقی نماند
🔹
بمب‌افکن راهبردی B-52 آمریکا دقایقی پس از برخاستن از پایگاه هوایی ادواردز در کالیفرنیا سقوط کرد.
🔹
تصاویر منتشرشده از محل حادثه نشان می‌دهد این بمب‌افکن پس از سقوط به‌شدت منهدم شده و تقریباً چیزی از آن باقی نمانده…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442428" target="_blank">📅 02:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MuJRbSwoUR4jiKbRBqLtxEcdYs5AjVYPKiv_555stuEGc1MRAChxwAsLxdAc8_XEAFuj__BqoGxf5yrJdgcW3tkDs35a_yDm6ur8f2BkaxQv1DVs8TXWKcInsKlsOxq7uCMp5siwaYNbpW8DvoXYZ37mp05pVaB_FJ_rXxPzj4Y0MyIrh5UZr7cqvdGJOcFwshZab4F3aOvLHH0Psky4Aa1xTRP0oaDyXIKRteVUT-uu_I6iWSpzHEiSYzFiC9y2vSnxATV1jVAyF81ZGw_wJO0Fu3y-kBU97LPyCxPOZfy04tGIF1b_l4K3gGRXlP85edX_BCaRiSPhAuysdtzZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gn-HiXIAF3sMLJLj2aS5dqhynUvKYpEgcHqIo7st0QyfZpTeztFHmCLFfcmyfnUBrnoQGnvlz3i1i-romhCPU2RLAk3OppMtvenpKCLYN7uTuwx8eTgRb3HEnoOBSG5EUJpoaUt-O6fSX8VeukrbXiHPP0ueP0hJ1Zr6jSnWJrTiulWQhgeNvySH_55Vzx88VbmTo4yolMF-r4XP_qYrkKesTsaKdhNqsV6KvOZ9dpvTSpriHGW6eyQjjqFca0POepBfVqq-166HETh7xWmAvrfxWOaZbQCChhH_sM0Pl25gkbjNXhHORGCH4s3fDRatS2KN_l-IAGhcCGnz31JRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZOorv3m7qHn3NIaoyq3DJG2Nm3qnCnoZv4NzTb8vstP4GpjRZmLBFGrHKXTam-KtR8yhlohkKf37XVZEL6tf1ITdwx6BfIY-jeRy_PAdS9z9CnN2-DKFCV8Cf7nqnU7EXZ-Bud1DzrUuRTYI0XjoKjGeHwgJ37qMTFR7KovuIvWDQWHtK1dc4QeFb5bXVcl4vmCI8u_a9KPYQIAh5PkU6nCB0T0QQG7a0DouPrziSCyfKIo2uFGChFLlitErLPYJOdeFdvIxWmttiEl-DRDx8x7oPr4HhXvSgHnMy4B6pyPGDlHT9lVc39kzdKRslT2TwnKcIg3shP5ZedzkvWh-7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I7cFf3Eu81sjYyazqGlte-lebtyHVpcZ-3pdwkHdPhj92epS2nLVhw0vvU_3wLJOP85O-LqvOkD20iLuRyF4chXgP6IyFwVkOUfB0gnO86kOJNJXRZV9B4ZEfZH8DU5oDDpL1svpf_nVS3SbQlgt60ZTP0JHmkB8uNhA8rbPp-c2Pua5gi6fIGdZPsQ2x8kWZ5T2zm-XbkhR8TlZxKtYm9yRbh7IQWelyejupcckILnO-pebmZQS4ikjjU8cujeypH0EsajSl1zkziP0hO9al38Xd6iNOTzqFiigsXUbYT8pPmT6YwKI0I2XgikCLoF_Yew3WHS3U6L434DVDmrqPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lXZeuyoo4UfC9jHDLnZLSXn7EVThCzFnwDPxxkL48qIuLLOHcx3dF6j8pBZv851lJDG53OBsQ4B5aoBFCS-XXiuoB-VGUQkgTt6Y31M3L7u3UJc3hVLinpzG7xQwjXVvTXGb4t1MlDJD1Sc9FLSSlwnW9kvEAoYvlH7DdhUq9F9usXTb02Eht8LbSAuH5xsnatzWrBYsbWgnq8XmoHUB6mqmUqRMOOuc6-nhDf8hha0_6YoAzr8v-ZNAJnriLb9XhkmoIRgJYVV27J5hVPZgw4BXMxiEa7F3sC43byb4wNkH62RQKhHD5JMNVm34ci-3hECqSFKNyw0Q0Vxs80kNBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j7dCon2VJbwhxQuZTLaNajsAj9RO9z7TngjRlKjIaLAhCLHSdutfw4l_CN7jf3JTJzK7rO3Bo309JlPU6mfM8S6MzESF4jLAOPBGPwwCBHPOpAwAD8VWbjrLWggkMco9xdnRXc-CqOPssE84n0Wub4FVS55vez89OtVDSxnvC71TCzL7rgvq5e2_b9cUJ1rX4k0a2EV1s5V5fbNxIwjrrPvlH0e4y-eoOCummWetm8f-R5Cg3p0zpMbEz48Sg-7l1mbJf18Kdggi5PRVQBr2RM3GhqBaolmWr0mJFNIHDhhC5lr7lwijTzcacrbs484MCriRs45QjOy_aVIa28uE-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NPg4ygaXvfoWARmzA3lNuJXZBokjCPhQGpSbQhFQirsUOseacXr9Gy7KXdTCVPUL7Tun-P1CCjUi7ZWIRK_sauZv7Qpzc1CIsVuW2eUMTE0rcMq5nCMOTPGu8TMBjkmSYxavYRN8KSIn8yJWbRgxn-qjJpdVSigdip64A0j6H2agTUxOtrKRA_4qDH2h8cDxP2BSc8eD1xQxFGvMn3gUNnr927MlzFTC_lbsAUZG4jhqbozkzaOMp_bBR3PiUMKG4B3N9LQKQj8uVpPctB5CZ81AuVgG7aANLMpw3Pxj3bD7CPO_hpMtiWy12otjm-9VxntomlEAen9lze7ni3vrGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/asb3mIZjrfeJGvBapWLGwWYdVZ49i0R0pxhXsFvZ2jHPRb2UjTrt3bSxy99oBPn87vt-42qtaemrX-X764LckSQLHRPDM7pGD6lIQSN83GQyMMqMy7ZPPTqGYooEhiOXXQ3UtQuAlDYQhDVB_AKndTXJokT87ie8DsIy3X5CcqTwG1awdSc41jrf4nxCAD9e1uAWox8Dn9BQKnuB0PgRYFagrYoKB45pblcPEeNL8-pODlsMxulu4capnGAYfhh3cgcJU-19-0SyszwNK1fxaezkQQqCcf0dnm8SJBlwxipezX1iGCwIfze5WkbyCEK0saVh5ym-SGuARfFblCsqvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حسینیۀ اعظم زنجان سیاه‌پوش محرم شد
عکاس:
عرفان تقی‌بیگلو
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/442420" target="_blank">📅 02:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">پخش مسابقۀ ایران-نیوزلند در سینماهای تهران منتفی شد؟
🔹
در فاصلۀ چند ساعت مانده تا آغاز بازی تیم‌ملی فوتبال کشورمان مقابل نیوزلند در جام‌جهانی ۲۰۲۶، به‌نظر می‌رسد که باید پخش این مسابقه را در سالن‌های سینمای پایتخت، منتفی دانست.
🔹
کسب اطلاع فارس نشان می‌دهد که دفتر نظارت بر عرضه‌ونمایش فیلم با ارسال نامه‌ای به پلیس اماکن، درخواست کرده تا آن‌دسته از سینماهای پایتخت که شرایط پخش مسابقات جام‌جهانی ۲۰۲۶ را دارند، به این دفتر معرفی شوند اما تا این لحظه پاسخی دریافت نشده است.
🔹
از سوی دیگر، با توجه به استقرار تعداد قابل توجهی از سینماهای پایتخت در مجتمع‌های تجاری یا مراکز خرید، راه‌اندازی آنها در ساعت ۴ بامداد نزد سینماداران چندان آسان و مقرون‌به‌صرفه‌ نیست و مدیران سینماهای پایتخت، رغبتی برای پخش بازی‌ ایران و نیوزلند از خود نشان نداده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442419" target="_blank">📅 01:30 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gqOhuN5iNQUKXxd_6gC-Tgydh2UNfQ_xpODLa4udDfFQmtEifTfoFmwMi2t1C5GCfuMD99OFdg4pH6-iOSMn0kNxnng1wM0ok3cRPiDGUAJUMGxo_eos-8jwUY3UmGfs03zVU_WXJN_vqQOcWs_2kEZ2jl1WuPHBJT9ZVQPwhKKMUPqOl9zZVKAm7p_OMwYYCqdeYQO3EviBTa18v17KTlEdAUIPgvQEyjMZWGJ_nWiAd5lBRH_K77iUlwZBKtvqVfdrTmsUvLbC3vQy5uOHrfzBe-RI-vZMCWCYV4g0jobzYX7dYdQD1mwSko1sls_9YcMKUW6vdJgawg8uMkDUwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
امسال قلب‌های ما حسینیۀ شماست
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/442418" target="_blank">📅 01:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ed854ebc.mp4?token=h1Rd3STa7uXHeg4K6baSO1k1Iy9LnMU0gBJvilDROZX8Hh9Wnuihu8BQc_yLRT_69CaOPBRyrrp_YeJFqXE7yiIpoWDA1A0znK2wvBOveRliQ4N-N6EEu8LXjFfIqYB4bkKBClBPYgWU5fCW-VjCjiEW70NjMij4FU6Z7GEfU-jTEcj8OieytRvx62A4QWYCdFb1GyCIAquVMe4gjAiDM58oKH9Rt58B-Ub_NueAhN5AGWJgfvmhAK-BnlUbA_sYGPX34513IM2OxyaodSYYnL2tq4Rm411mEHXOIq6hAG8NYwmStZlSNEGUutczJqHtSk3whFZ0y6LNazzFvg_18A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ed854ebc.mp4?token=h1Rd3STa7uXHeg4K6baSO1k1Iy9LnMU0gBJvilDROZX8Hh9Wnuihu8BQc_yLRT_69CaOPBRyrrp_YeJFqXE7yiIpoWDA1A0znK2wvBOveRliQ4N-N6EEu8LXjFfIqYB4bkKBClBPYgWU5fCW-VjCjiEW70NjMij4FU6Z7GEfU-jTEcj8OieytRvx62A4QWYCdFb1GyCIAquVMe4gjAiDM58oKH9Rt58B-Ub_NueAhN5AGWJgfvmhAK-BnlUbA_sYGPX34513IM2OxyaodSYYnL2tq4Rm411mEHXOIq6hAG8NYwmStZlSNEGUutczJqHtSk3whFZ0y6LNazzFvg_18A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نمایی از استادیوم سوفای در لس‌آنجلس، محل برگزاری بازی ایران-نیوزیلند
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442417" target="_blank">📅 01:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🎥
حاج اکبر مولایی پیرغلام اهل‌بیت(ع) درگذشت
🔹
وی در سال‌های اخیر در هیئات پرمخاطب تهران به‌عنوان پیش‌منبرخوان برای اهل‌بیت(ع) نفس می‌زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/442416" target="_blank">📅 01:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🎥
خلاصۀ دیدار مصر و بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/442415" target="_blank">📅 00:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442411">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVPtufc-gLtnwl0nsByFmsISLPdR2P2F0-1MW_5CRJd9SDLyqpxpvsLYz0p6qiB36BBLHy1Sam1qGm4L8l5ddt_gishLQ2JUI78H-vyxmokk51kGyP3a2r7U03j7zA2psadVyq1CH9vwRXO0KNTuvKUroSux657zD3EJfJifLWDARvJ3axfJ44hkjMkyBP63pL68l2eLS1MHItGIhPKZMu1zSr7sviYdCUCweFW4G1ZvzGzXFQ7Hd8CXDT2ZQCcKCuvtAj9hWFUNKSC8kvgD4jXlAQa60gtITu5dvFg7YeKW9LutsfQrcZ01eY0fb9e5RAj5EzbipfZv-tfJHTQu7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjLHTAGu8o4PG4mDDmYMHzg__SC4EjVjVrYWjVaIlVOp3r6qM_zcanUNTK-JsYTGvFK1awTlaGjs7YoDkFuWXMIDfOXwKWoJnIG_rK-Zi9CmNKb8WYCAiFewP6vaRPxAKVsww4LPEaUxSU_lPeL7DtGBvRCMdad-c-mGscvk0xhn4eH57iS6o9OQzm4hNbH9hKb04muD842B9v3JhvbYjUzM8wXRayIf_cuOJPjbhoS1txH2QHCu599OEYLAoInHtHW3rSPl1mRClzVc-eboK6KP6pGGJiDa9aVjfOc_zxU_kx7e4y4nDRNwAwQfI10n6Nddmr-jv4d-BtIn0jOJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NX6EOBxABgtYuWLcKz6B6dG20I46KWmHtuAEtb_atA6ZfqiFyvuelHDRgUxlblgHHsxUxpQxJ6k_FtzE8eq4Vdfw_Q6V5abFyfHaftCOfekUqsDfGX2VRwNDgUhubp2zLz-y6g4jF9xIAoSgIYLkqumEg0ASRvdxce0hu6Lvqsi5SXYNgCDtOIiudlA4kIsafACyig_M9EOM7ZT3iA0MfQxRIHhRMV1rB51ooPZfLJ30xz2MqYnaRqdthDyTB8_G_S4mPI_q6xngyuRVrwKKH1t361sWAYpqKlfsnkQRrkqc0V6rNBLJob57iU0_VGYXYD1ur_9SJGa-ZJcbMwY_iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MgOdSxZGc3sAy0GZERLprI9YjPMeVCoG18hyOMUJ_QzqNmDFmTqQ5qv7R7oFpEB33uhqZlDK0whCHYvfYspiiyOe1rwOTQJd43m07dba0EBCLdmCJaDRTs6dayKWs_lt61flwxuz6uZfJGvgeOd5mXzYyvfdZkIFAN9kR3M9B2GNCnHoxeuOez6_34NPThUozEqH5rHkCxWUctsdxkoPRBbiPsiKHqP-Ld12ilN_cnB1jAbQaqs5yVZ3vjcNzExEN_W-87nABMyT41jZ4qAPpYuypsEgAnErCQucGO0Bj31Rz9wGmBD2E-WCXyqgEOMgFC6c7k0lmabqXo2SprNtYQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | سه‌شنبه ۲۶ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/442411" target="_blank">📅 00:44 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442401">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rg5U-arzMZSWrn28Z6x2qanTSpNKUPhbANvrqKzpPKsqGUiPC3fXMWq6RHdLu2X9rCvqvVFZq1Nw6NokMiwx-hy6yl7B1nwBGiT2wBec8Jm3QcIceykL1j7h45i686HO7yKh-9SPWeM-V-ow_5I0zTLFgnA-VbkwnHSB_uDUhePTI1CpcUjQ2DP6uFxxe0O7gXIUjlY8AYMuSFvNspZl5F1D5FqSKgmiLM___h94GBCwGPP1lXdpAkNMZe1h3K6chWhqyqDto3i4wfWLigR-TgguMYGxxc1VGPAdLZycVB4gptB-a13tfS5uSRhEtT1iu_FTEMZJlFT_i3peor5hpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XZ1HwB7y4BTovZsMXGRi8-TSMzvEloezPqFobI8eqmZwKKbF3WB2eQ9OEqteUoUkDAz0b9QmC4R9iPreFsYvPT4eE7LZHlNgTkvjc1GHW7BnA_aj_ikpnVdkC5imgsyYgTBYYVmI9J_gPbw5a4OdTfomzg96RU9sr5icemWEzIywjl_K6GzgqjQxLYLTA5WrYKxoLccH213hA4o09QP3kgMZUZftoTuFaKMH1b4pruAGrkqzWbOVxcjorHkq7K3QVAaFRPbweQUmO8FmJ56-aSSoHBkfeh-hnBxM32MpmATquphakgtu19Fv7PZ0aySWtZgUcsotd-JGW-HJN3QNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzgpv5cbgOKNwuORrBa98fXQqjbsz6cIEgRvxgEr_EalarlLCgTw0S32Gu1lv6hJrSmlQAOFYONXwqFBJFIZ0XmmmsZsG4ACl1nFO256SGaZpVTtI3HICbUzd35_4eFAz_2xdMu2KczKDRYelOv58gfLKjlibIckc8QjzK2E8qeUizle14NoTwaDh3Bj4MTQi-VN6q5iSsqcO02GjHcTrfXwK_BSd3uYXTVDhsO2jsLue1eXUSMNQkcGlxVb26M_yxkUaiMT2TCAlGFMHzGWeKCdYvt1tUiwAfYpVFY-sQOHJjP6AizbbvM9nJoOPSUj8xudC3DrnQYNKzAzdD4GmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bikBLWQQll9jMMSvsjIn35HwWwFmMs70je7NZZJsq-k_oYhQ5Ttnaanh4o5avFiTOZberlcePqd559MPMYouIFIQngeklFrZhn-Af-3RO7PptitTf5pf_Y1u1oKgBgO0PVGhGtJsYiM2xjXYglR7fSKvP3LwatG7jhm8Dh7HYNE1Pph1dd9ze270dNcXTytWOD23pMv0GvZFTFaJVkrVe9EnbHt54orbOGbTfOcfbhDCNbPYOSLmwjJEwtgrVDS955WI3encwrAvB2N2196CZ1raaJd1nMIs7DeSYtH1xmDeB4S19T6QldTS8C6djLBoAy8SXVqxtOmLoYS6csq73g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmJTa3C7FQq9Parz1tGZr6chDzii7V-kRV3fMiYb9Gm9BfU5X73sVlRc1E7vYeUgZPEkWs8JaTFG4gHxP0fYxma2VXLb82grU6sJfC1JAaTsOOEOJLoz9pCXGjti0ZS1Ggt2EzsUqFbCuXH4G4J7kUX5RWw4sinh9MApRva7kyoaFlS835c-FcLsbWB4W76njcvFPPm9iS-1Kpze9Bvpa53qNNIJZOIslPX8FanplwseM3E6A-tT59dfo9gyh_4Jf5c0vO7oXce0tzPoJ4FERNZMZDvrZ4PK1yuYFxEtqVaNXa-CkYwFCMzjWOhmPXj0nLHJEsIsmE-amowtxak4NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ne6HKYVO-ElA8jv04QhN1Yic3m-0DybR7TFv6fDH3_RkJVuu9fhMhYD3M6-GbynGyz2NeQxDJdjFLeRpS5dblxPA5MWvEUKx3S9XQNCmBNf3fMNFOLyU784v6Jxt4r9qOA6j15yBEfJLZPyBe1RH5g2oMGuYFIt2xTYOc8Z8Xsk3No29WxrG8xeDQHIQQ5J6N5YwIWPidAyoscYA15HPAaIUHSnQ60RHR8sjigrgVJXNSWmKs-Bnp4YC-HOHJelAyw08K99QYbFXLKwqR0Ag1q-aX4_Fc48slxMX0UjWNqeUNoN__d7cpZp2QOA-Iq_2uRjLVN8_N3mGGqK9O2aFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHyCCByubG80RNnVWodEdvAvEe94GK5zwjxGeaCYxBpwYzAj_l_oom9k3INanoG-PvTHrK4XcC8IBQ1kf4krRAkKH8MHmwQKHJM42YYLfm3uV9vf55XYhCDIp-mCyuZKWBQAUv2g5PFNYRWG1tB4lBhB2FtpcyM6RcN60K85AO7xXOqJ_KIvGKcyR0IczuvrxiRe6tPSk76_Znsp_LLRg-LinMgjfPHgXCq7jq91qLJGRvf0lj25jHstbGTF1PReTegySfYmQLKc_AJoizb8Q7oPnySCcK81x59NX_nWIBsi7MyNgV2NXWTgOLajUinX8p3efhiZTr8vyr6uSXW0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BgveZ8qjYH054Jm3kv5n-gDAZqxx9UPBFD7YmqQKi1ngrch_AMYDUpvUnaT4AjzWXjq48X-IAsKpSZTiL5lYPGS4Dn6Qv7gFcu6PqQ2OUtqffZH2CMPXqkGS8ggtUhwIrpxA25Hs0uFC6c9KVoFkyVPDDGu05saCkIvRIpji3h3JptApxVQRmS9AnwrWISbdiKSk_5nNfMW5dXRDX1vlrwIvePKOh_Io8biS5gZTRczCQYXfKqREwshZs2s2TMHQJcRldaluTJK0icuQV8MyTl8q_TGrNUeuWyTRT1NtwykFKL__eHpiX4K6peaRcWU5P0LaQevTcCQA37rTtZy3bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksX6L1_lzDSnZl-BOb_fS-LQSmcCbCGR8v6tAXRWDNxIrbwqeyJRKBNII5qfRXzs3xfonzAv_ZZ9QKf0qG5637h6LrZHPE6ZJ3KSjkeqzSFuZmcLcbXAyjd3rPemDOGs4Rm6LU0eBHOJRsD0uxQAfWq4KGowz4wHT-sVmqrVETwfx7sRUK-Lq5VQwJtFvEg6SKYl1DFj_Fqq5WYPPDBSXCAS4yIfBOQtDxKWyv9TEA-RXwo97MZLzGjEOPuFvlcZg_DvxHF4F_a7-tVdq2_ce4sVEIPGlb3HiwuFoleHfqCJbG5bIgLosTCipQ-zr60jIxrv6K73lX8nNUcBXMtj4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N-_S3LQ0ptvazdGj4E6xtBj-KvrA4qNr1M50lMM1z1Iu-RyUIsuPuJZ0gZbMGe-2S1u4C2lwZHZdCJ4qAQFtTR-7dYachpsAJD9JJHulLUkO8I6_9cj9esHmzpxnW81DFjDXrx6zpYp15neH2uie77EaZc-FaZMOZilS2nBBZZ8vCyBfyc3t9Aa49p4jkI5jl2ic4uu7OcsGunqje9-0jLQ25CUx7oYziysd7Cjlh53RW2LOQ21J0-okbN58kIB6IHO0Rt-WKdYJHo3M4cJUweE8rrQeE_dGSu1h5Rwi6A3-JbMqJ1vR2Pgt0xrzp7PVD3q7x0LZ_dJgJXIRdasvBQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/442401" target="_blank">📅 00:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442400">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G47oHqLrtMCeHhZ8_8ESn9L3wNLu4yO-3AY_sTvp22CRScGzLemRWjwFLqMk5Q1Y0gz8A3ERoj_7_l3H7RbmYhk0OdbqejWZMSp_PKTb2pdvkLzBjqTA3jiH5_s6oCZSUP1tk73d0gtjRpYAu3gPegMTsB-GM44czeLN7Z2bkZcbxL_x5EwSpFA3zvh3AD0l_Sf146tqc63rF6LJfd0x5A4p7iicyh0siYqNrorqm9MIb4TzHJ1mB8ZACCyZWArAPnm0QCzm4ztlZC6FIPzM4qIgBpAzWfOie9ja1xj97SNP_baGy0R3PmLucaB-tRA5YLaGa46o9S8_QHeVBiSyfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تساوی مصر و بلژیک؛ نتیجه‌ای که به سود ایران شد
⚽️
مصر ۱ - ۱ بلژیک
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/442400" target="_blank">📅 00:31 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442399">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5187626b6.mp4?token=Rlc6-fGDtHXDE77yTsP-O6kNuWJHGJT6r5Qde3Hy7XuaAH9_5ivB4p9OdsuZUyQ9Ao3_QWygyW6IxjC6v1b3p5Ije9znswgcRe5vcWQrb4H0RlIW20cg2dq76m6tl3t3w2ujR_f43xfkvN2Di05qCi_4rlAbm7Hhk0JupVNxgulWKj66KkP7GKblo1cbD86BNCMomONY008FXoPfJgev9QELpBHrPhn93-DrIGXq-lNvOEhsZvehl7SKtky4FO9slltlvN4mecw8BgcB3oJQp-j3IW04Vcbkz1Y4c82SQad3HyiRIPCdWlnwqgC95t2L9CQQLDdoh1d9kXkNLhkxAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5187626b6.mp4?token=Rlc6-fGDtHXDE77yTsP-O6kNuWJHGJT6r5Qde3Hy7XuaAH9_5ivB4p9OdsuZUyQ9Ao3_QWygyW6IxjC6v1b3p5Ije9znswgcRe5vcWQrb4H0RlIW20cg2dq76m6tl3t3w2ujR_f43xfkvN2Di05qCi_4rlAbm7Hhk0JupVNxgulWKj66KkP7GKblo1cbD86BNCMomONY008FXoPfJgev9QELpBHrPhn93-DrIGXq-lNvOEhsZvehl7SKtky4FO9slltlvN4mecw8BgcB3oJQp-j3IW04Vcbkz1Y4c82SQad3HyiRIPCdWlnwqgC95t2L9CQQLDdoh1d9kXkNLhkxAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دو مهار متوالی تماشایی توسط مصطفی شوبیر، گلر مصر که مانع گل دوم بلژیک شد
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/442399" target="_blank">📅 00:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442398">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱</div>
</div>
<a href="https://t.me/farsna/442398" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
#روایت_شب
|
مرگ معاويه، به‌ خلافت‌ رسيدن يزيد و خروج امام حسين(ع) از مدينه
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/442398" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442397">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🎥
سردار قاآنی: باب‌المندب مثل موم در دستان مقاومت است
🔹
باب‌المندب فقط یکی از نقاط استراتژیک در دست مقاومت است و جاهای دیگر هم هستند که اگر لازم باشد فعال می‌شوند. @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/442397" target="_blank">📅 00:15 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442396">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پایان محاصرۀ دریایی آمریکا، با عبور کشتی‌های ایرانی
🔹
دقایقی پیش چند کشتی ایرانی نسبت به تردد بدون مشکل از خط محاصره اقدام کردند.
🔹
طبق اطلاعات ناوبری کشتی، یک نفتکش ایرانی VLCC از آب‌های آزاد به‌سمت بنادر ایران در حرکت است و از منطقۀ محاصره گذشته، همچنین یک کشتی حامل نهاده‌های دامی‌ نیز با گذر از منطقۀ محاصره به‌سمت کشور در حرکت است.
🔹
یک نفتکش پر از نفت ایرانی نیز با عبور از دریای عمان و خط محاصره به‌سمت مقصد صادراتی خود حرکت کرده است.
🔸
روز گذشته، ترامپ در پی پذیرش شروط ایران به‌منظور توافق آتش‌بس، دستور لغو محاصرۀ دریایی را اعلام کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farsna/442396" target="_blank">📅 00:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442395">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1558868203.mp4?token=ms3PPCb2JetOgtIHUIWfU7PQHEarFCOEB-J3wd_6SUSZFbkmi2Wq8HjJEXs95BCUjzYphQrK1nOjbmN83ZsL_mexMvdpXwwJYQvas-JO1vOPJ_EF9nu_2Umf_9dMI-WCzsRRpMRa1FfW--vZwx-a_QuWYUWISOQ_ZghVmnCIAtX0OQ6onGO7ttdWydAez70F_2lWgg-u0f_Ty5xiFZx1vCXtxKgtl3SwwlzgTzBDh6SdU0qzsN_mvm4MfsFSklKmAQHz4n-fPc-YMIWE_4X2K5es_iFooDysHh44CDDNZWbfJF74v1S-TiNkZHAR29HEWfBg8STmFDum4WmKhisSO1nS9Foql1DYOZeRX9ApYsIj0_p7pqtu3HY-ZXW41OGgTRxgPjD7-gX-K3lDW_65sdcJqE9YkOjtkkINQq-9_6ayIOg3hno75XfM3SDPKn2uH5a-i-LBWgSwltgtM3JUz00dea5GfVtG9kyg-JaypxzTgd9Ld_BKkGwWQS6f9WbxOmKyxEspFFsmNVvfooiGIy8qDflSMejCr8EqluKWX09qyuaNZ2WLpPxZnHvEo44GCIbg0zh67I5K-jKXW0VWcFbQD7MtXrz9aLUXRcQmUJBC2KDr2D-Q-qIkE--PT4FOYvYs5EmVjvQ7V48UEQ9YEx1-SvVxpe6aTx8agpFrAnk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1558868203.mp4?token=ms3PPCb2JetOgtIHUIWfU7PQHEarFCOEB-J3wd_6SUSZFbkmi2Wq8HjJEXs95BCUjzYphQrK1nOjbmN83ZsL_mexMvdpXwwJYQvas-JO1vOPJ_EF9nu_2Umf_9dMI-WCzsRRpMRa1FfW--vZwx-a_QuWYUWISOQ_ZghVmnCIAtX0OQ6onGO7ttdWydAez70F_2lWgg-u0f_Ty5xiFZx1vCXtxKgtl3SwwlzgTzBDh6SdU0qzsN_mvm4MfsFSklKmAQHz4n-fPc-YMIWE_4X2K5es_iFooDysHh44CDDNZWbfJF74v1S-TiNkZHAR29HEWfBg8STmFDum4WmKhisSO1nS9Foql1DYOZeRX9ApYsIj0_p7pqtu3HY-ZXW41OGgTRxgPjD7-gX-K3lDW_65sdcJqE9YkOjtkkINQq-9_6ayIOg3hno75XfM3SDPKn2uH5a-i-LBWgSwltgtM3JUz00dea5GfVtG9kyg-JaypxzTgd9Ld_BKkGwWQS6f9WbxOmKyxEspFFsmNVvfooiGIy8qDflSMejCr8EqluKWX09qyuaNZ2WLpPxZnHvEo44GCIbg0zh67I5K-jKXW0VWcFbQD7MtXrz9aLUXRcQmUJBC2KDr2D-Q-qIkE--PT4FOYvYs5EmVjvQ7V48UEQ9YEx1-SvVxpe6aTx8agpFrAnk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سردار قاآنی: هیئت مذاکره‌کننده ایران به محض تجاوز رژیم صهیونی به لبنان با اقتدار با دشمن و واسطه‌ها برخورد کرد. @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442395" target="_blank">📅 00:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442394">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🎥
سردار قاآنی: بدون اینکه ایران یک کلمه درخواستی داشته باشد، نیروهای مقاومت در جنگ اخیر با ایران همراهی کردند
🔹
تمام برادران ما در مقاومت از مدت‌ها قبل همه‌شان می‌گفتند در نبرد با آمریکا ما باید پیش‌قدم باشیم و نگذاریم به ایران آسیبی برید. @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/442394" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442393">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🎥
سردار قاآنی: بدون اینکه ایران یک کلمه درخواستی داشته باشد، نیروهای مقاومت در جنگ اخیر با ایران همراهی کردند
🔹
تمام برادران ما در مقاومت از مدت‌ها قبل همه‌شان می‌گفتند در نبرد با آمریکا ما باید پیش‌قدم باشیم و نگذاریم به ایران آسیبی برید.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/442393" target="_blank">📅 23:46 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442392">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac486f2dd.mp4?token=gxXzQf25oep3IYzZ0RqaFBXypWVCgLey0N7TGxbfassxQ9D_RJvV8ovh4iTTcxJ7oe1dmEiT1abYDupXX9WKWhGH6djzBQx6YDNLMA8Gs6UDF5cWVmaNfuFTnxJe3QL0YSL8vszjRmNDT-Xtd3TpXTEfy8BqCjLDPNXfv5eGeDRNE1ope_yC1fBmGc8o-_PJGp2Z6HQxfLrqTglJgE5kcKiK-HHF-p6_kR-2tpvarwzB9OuEwW_OSGZAi-lhnEL3zNjgdCk_hU3h57oGA4xrZ59nYwCUNcyTnFvHpE19l2qUX6AuXp38t_-Lu83GhrZpf8ItEPAGc20E_ZeIRJEA8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac486f2dd.mp4?token=gxXzQf25oep3IYzZ0RqaFBXypWVCgLey0N7TGxbfassxQ9D_RJvV8ovh4iTTcxJ7oe1dmEiT1abYDupXX9WKWhGH6djzBQx6YDNLMA8Gs6UDF5cWVmaNfuFTnxJe3QL0YSL8vszjRmNDT-Xtd3TpXTEfy8BqCjLDPNXfv5eGeDRNE1ope_yC1fBmGc8o-_PJGp2Z6HQxfLrqTglJgE5kcKiK-HHF-p6_kR-2tpvarwzB9OuEwW_OSGZAi-lhnEL3zNjgdCk_hU3h57oGA4xrZ59nYwCUNcyTnFvHpE19l2qUX6AuXp38t_-Lu83GhrZpf8ItEPAGc20E_ZeIRJEA8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پس خون رهبر شهید چه می‌شود؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/442392" target="_blank">📅 23:31 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442391">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e5d07062e.mp4?token=NLHdqfNJ-FL8UpiCH7-FALjbf4opOE8II_nTso35LJbNOcJ6iVqKrwYWosksl_plk8brwLMr3qAZhimC5gDYao0IFkvYLNfIPQ4gCNPOD6raDsQGKqQS3jXIR2P_Rvx0mXgapYI92GEll9cm-OTs9SFs5AfZmZ7dtBz1D7Bh3ZCAnL7cLfbkWuQAv3wIK71Ackuu2xp75zL0inckWbKb_7sqh-8JW0OcZkCev-URP-kgj2i9MoG0CUIeDekEaDndI8b_3GMhwJT0woRyV7DfjIP8iDgWFO3rUaLQc8IEEbaDooKDTvCsV3Se10pzyoU0qjMn5u-RtMLStbMyh_h1Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e5d07062e.mp4?token=NLHdqfNJ-FL8UpiCH7-FALjbf4opOE8II_nTso35LJbNOcJ6iVqKrwYWosksl_plk8brwLMr3qAZhimC5gDYao0IFkvYLNfIPQ4gCNPOD6raDsQGKqQS3jXIR2P_Rvx0mXgapYI92GEll9cm-OTs9SFs5AfZmZ7dtBz1D7Bh3ZCAnL7cLfbkWuQAv3wIK71Ackuu2xp75zL0inckWbKb_7sqh-8JW0OcZkCev-URP-kgj2i9MoG0CUIeDekEaDndI8b_3GMhwJT0woRyV7DfjIP8iDgWFO3rUaLQc8IEEbaDooKDTvCsV3Se10pzyoU0qjMn5u-RtMLStbMyh_h1Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ما در میانهٔ جنگیم و به‌هیچ‌وجه کسی نباید فکر کند که جنگ تمام شده؛ جنگ یک توقفی دارد و آمریکا و اسرائیل دنبال تکمیل بانک اطلاعاتی‌ خود و مهیاکردن دیگر آورده‌هایشان هستند.  @Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/442391" target="_blank">📅 23:30 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442390">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abc7b4f64.mp4?token=OubwiZd3yWjK37Ui7rRheg1VGT0kRDHti7gSn9RJWJQKvZeyoPq8MrVbVeDRJQUFQFvcU3dZRH_X_CWOBsKBtZRyRhkL6fQkgyhH-HfiwUoAPcFFYKgMBXqzeZq0aWAu_yXg4wV1ku1vSx1mY5vVjaieRdVhWvXbPoYtzalqxDzab56G7iPPy9qO-JmqpfktfAc5PqCXC5Xfqf6Wb7Hitp5kwt9_txF_TLRaovO0yjTo34-M-3XI-JSHqHIpToEMKHWHrps6RCjTI4NAduWTd6JBhPXsfG4c9919FRX_0MG37J5FBGiHCANJ2CwvtdUPT7wnikxhcLJxd7CGydKwHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abc7b4f64.mp4?token=OubwiZd3yWjK37Ui7rRheg1VGT0kRDHti7gSn9RJWJQKvZeyoPq8MrVbVeDRJQUFQFvcU3dZRH_X_CWOBsKBtZRyRhkL6fQkgyhH-HfiwUoAPcFFYKgMBXqzeZq0aWAu_yXg4wV1ku1vSx1mY5vVjaieRdVhWvXbPoYtzalqxDzab56G7iPPy9qO-JmqpfktfAc5PqCXC5Xfqf6Wb7Hitp5kwt9_txF_TLRaovO0yjTo34-M-3XI-JSHqHIpToEMKHWHrps6RCjTI4NAduWTd6JBhPXsfG4c9919FRX_0MG37J5FBGiHCANJ2CwvtdUPT7wnikxhcLJxd7CGydKwHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب‌افکن B-52 آمریکا سقوط کرد
🔹
منابع خبری بین‌المللی گزارش داده‌اند یک فروند هواپیمای بمب‌افکن B-52  متعلق به نیروی هوایی آمریکا به فاصله کوتاهی بعد از برخاستن از پایگاه هوایی «ادواردز» سقوط کرده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/442390" target="_blank">📅 23:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442389">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🎥
زاکانی: اتهام‌زنی به مردم در خیابان و مذاکره‌کنندگان خیلی بد است
🔹
سطح امتیازگیری ما در مذاکرهٔ فعلی «میانه رو به بالا» است. @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/442389" target="_blank">📅 23:21 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442388">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4IeR67hz869a-9bqoOTFC4OBf1sEaAkrcl2nBBWcK5dpDCcBOWmmVERngqI400W5dwC0QMvIOWKtoue5Q3tqTBNCZDnoggTkMxjplimfw3nK8GsgxzY6suPsa6ERD9wblmGw08VbI2eHc0ERIDGs7M3sJbDDONszv-hBnrOl5Ge-YwfYfoybLQX-PerpJKaCiQpWCQZ0_sGYn8ODu4X4LeBIDMHh-RiDTAGuvxzI5pybHaUw9lgp286ITpJc7a1adn-kfpufAspQDVGq1deLVj4xeT1U-hPcowWOFz8O0wrhwzcKODTVLIOwsxWkuPZshj40048iDhaxngQO6Cn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقشه ترامپ برای تکرار سناریوی اوباما در یادداشت تفاهم
🔹
اظهارات دونالد ترامپ و مقام‌های دولت او نشان می‌دهد مقام‌های کاخ سفید به دنبال زمینه‌چینی برای نقض عهد در اجرای یادداشت تفاهم حاصل‌شده با ایران هستند.
🔹
در ساعت‌های گذشته ترامپ و معاونش جی دی ونس و همچنین یک مقام ناشناس آمریکایی اظهاراتی درباره تفاهم‌نامه مطرح کرده‌اند که خطوط روایی کاملاً مشترکی را دنبال می‌کند.
🔹
محور کلی سخنان این مقام‌ها را دو موضوع تشکیل می‌دهد: نخست اینکه ذیل یادداشت تفاهم حاصل‌شده منعی برای برخورداری ایران از امتیازاتی نظیر رفع تحریم یا تشکیل صندوق بازسازی وجود ندارد اما دوم اینکه، این امتیازات تنها در صورتی حاصل خواهند شد که ایران به گونه خاصی رفتار کند.
🔹
این الگو البته چندان ناآشنا نیست و مشابه همان رفتاری است که مقام‌های دولت «باراک اوباما»، رئیس‌جمهور اسبق آمریکا بلافاصله بعد از حصول توافق هسته‌ای برجام در پیش گرفتند.
🔸
ادامه این گزارش را
در اینجا
بخوانید
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/442388" target="_blank">📅 23:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442387">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cdaff8d552.mp4?token=PTxrntes3px_pW8_1ZGt7nAU3qQUCC2ajS2hO8U_Tw05Ms2lBjf9BaBh7NhPAtcl2K7ErE58PHzvL9YwALeyKZnYMMK4RywBS6Nt6uI9Ci2n4CJ2egEcx_aWzYS7xOc3kFr3hwDnTX1_Q1z4sHkzCgRHZN41DlQ5BK0HfpMNSlaGLvf2YioNmg3ji4d2JPh1WHbqeqt36aAnEZ_ggaVHNkNoyYdI6NhoGe-Ng071PpW01LMU0qmFjMofa6KjwDfVH6V5zcYl7RjNlzICTxb8i97MiPZk9gCXZG5dWtZ4uP_WWJgpuZwF9ta6ZUAkOY2IwXlbNEbjLK5SqjxRB9qTsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cdaff8d552.mp4?token=PTxrntes3px_pW8_1ZGt7nAU3qQUCC2ajS2hO8U_Tw05Ms2lBjf9BaBh7NhPAtcl2K7ErE58PHzvL9YwALeyKZnYMMK4RywBS6Nt6uI9Ci2n4CJ2egEcx_aWzYS7xOc3kFr3hwDnTX1_Q1z4sHkzCgRHZN41DlQ5BK0HfpMNSlaGLvf2YioNmg3ji4d2JPh1WHbqeqt36aAnEZ_ggaVHNkNoyYdI6NhoGe-Ng071PpW01LMU0qmFjMofa6KjwDfVH6V5zcYl7RjNlzICTxb8i97MiPZk9gCXZG5dWtZ4uP_WWJgpuZwF9ta6ZUAkOY2IwXlbNEbjLK5SqjxRB9qTsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: ما نباید فقط با آمریکا مذاکره کنیم؛ باید با چین و روسیه و کشورهای دیگر هم مذاکره داشته باشیم و نقش خودمان را در جهان آینده ترسیم کنیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/442387" target="_blank">📅 23:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442386">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h28I0nJt02vOtat_ud9xzfIdulD1u0Y2QUwfXHh-T1na8UD6ldSsjn-AML8enKh41S1Aa7pbFbYoxpoVyEYsuzEx0QvnnNOMuRnLzS9KOpYboKJxlhuI7fMhLQN4h1hKswFUTBWtHofpjdKLzgUrlqGJSdJ9aqTRoAfHiDldpxH73WletKqfRdZ7IJbdc9YZquBm49KVc5mAtgMtzBGpTwW8JIY8s2mHeNi_6mbA9-mNMoKbD2kk62pIFSweDhuZdQM3mL7SKhTYEaCUOjL3KvXr_uw9VzkJK7M-cA-gZLfkkPEie_c515ghtPhgo64XfuH4IxhEnTDYCV5Uosqurg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری از شهید سپهبد باقری در دیدار با رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/442386" target="_blank">📅 23:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442385">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77a39f0be2.mp4?token=TJYbS3-csafN2S-rh8QCEUbgKKg-ncKww8RoKrMQmBMWKtMa2XKKHxq85pl4vbBRuiaiLpY-83uy6egPQA4EZZT3MNjy9urajL-UtAb4CZ3UCRquw6IC3-RAktCXS202LF2tVbrXAjEtNsZjfEBKOdRIRxzN9dhRmv5bSiVD8T2ShDb4F2-y7EcBjwnOWHKb8UJPi8qq5psMCyNU3DqfNXorm_5DL-4Tu2mJRNt-DekAG7XqOrBvH-3MWI9S_clgLmV1YpRRzezKTWK9zHF7Vokya-a62YowIepkXejZu3S1bivP3iXgBmYJQDOMaPdDkBCzODncFstEmMoMmBKL1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77a39f0be2.mp4?token=TJYbS3-csafN2S-rh8QCEUbgKKg-ncKww8RoKrMQmBMWKtMa2XKKHxq85pl4vbBRuiaiLpY-83uy6egPQA4EZZT3MNjy9urajL-UtAb4CZ3UCRquw6IC3-RAktCXS202LF2tVbrXAjEtNsZjfEBKOdRIRxzN9dhRmv5bSiVD8T2ShDb4F2-y7EcBjwnOWHKb8UJPi8qq5psMCyNU3DqfNXorm_5DL-4Tu2mJRNt-DekAG7XqOrBvH-3MWI9S_clgLmV1YpRRzezKTWK9zHF7Vokya-a62YowIepkXejZu3S1bivP3iXgBmYJQDOMaPdDkBCzODncFstEmMoMmBKL1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد!
🔹
روس‌ها به ایران گفته‌اند باور نمی‌کردیم شما اینقدر قابلیت داشته باشید. @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442385" target="_blank">📅 23:11 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442384">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88a1ced860.mp4?token=m1teiXsWXecKv_x4qHbCW1czeKczvMlJTKvEhk_kdYJBXDXA2BOWiaPp-z71ZCfrXkITWEXmpeTWww-snIBLxhceI6pzlpcShdzMii0DK5TIfm5mtFKfFzjZ2qqbY7EzVtnV029HioeW6A9g4pEsyQMaP328C90xTEwQ0zuxSiEAtr8GAmxL-iGzKFb7ibrCHWfXLKI16jAPUmWw1UrkhNeIr2YTU2IofQX1oX72MgbTfrouXFeivw4hxtCaH0no--AqoivnGaRlvPCdYpkhWYI8SKXqvBs8-So37qULUnx-MmFTAzbBjG6H_TwKd_RxF_FH-XL4xOfZDPe01BtHiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88a1ced860.mp4?token=m1teiXsWXecKv_x4qHbCW1czeKczvMlJTKvEhk_kdYJBXDXA2BOWiaPp-z71ZCfrXkITWEXmpeTWww-snIBLxhceI6pzlpcShdzMii0DK5TIfm5mtFKfFzjZ2qqbY7EzVtnV029HioeW6A9g4pEsyQMaP328C90xTEwQ0zuxSiEAtr8GAmxL-iGzKFb7ibrCHWfXLKI16jAPUmWw1UrkhNeIr2YTU2IofQX1oX72MgbTfrouXFeivw4hxtCaH0no--AqoivnGaRlvPCdYpkhWYI8SKXqvBs8-So37qULUnx-MmFTAzbBjG6H_TwKd_RxF_FH-XL4xOfZDPe01BtHiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مشهد در ۱۰۷ شب حضور مردمی سیاه‌پوش سیدالشهدا(ع) شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/442384" target="_blank">📅 23:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-442383">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7342d0d8c1.mp4?token=GiwqK0DN5I0edfPGnqP1PWjk60HNpeJtORiQ17aCdezUk1Z3WDoQ-a6a27ozkDwv4aKdOJi156n5hSFPtg1Nj_f0oQ5BbZ4kljT4d-0sF3FoBdj-wnyAFBOP0FilR0ZJ07tvY2iQ58EavRm5899yhBjKh8_3Dt5xOgHNlK12BPkPGFVDkihHIXfmEFpNeluOSV6fkYCz3fSw29Xy5veD8KCeCBy7hQJj30cITgAGceRuIUQ_MxLvtJmxAEILYa0vCpN8DeC5wbUT8RH5JMfSkQu1dnkZgt3SZjdUKNVrh1Jn3IPcW0rE66KK-do_eQ-ee85e9es8nVa31IrSMze6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7342d0d8c1.mp4?token=GiwqK0DN5I0edfPGnqP1PWjk60HNpeJtORiQ17aCdezUk1Z3WDoQ-a6a27ozkDwv4aKdOJi156n5hSFPtg1Nj_f0oQ5BbZ4kljT4d-0sF3FoBdj-wnyAFBOP0FilR0ZJ07tvY2iQ58EavRm5899yhBjKh8_3Dt5xOgHNlK12BPkPGFVDkihHIXfmEFpNeluOSV6fkYCz3fSw29Xy5veD8KCeCBy7hQJj30cITgAGceRuIUQ_MxLvtJmxAEILYa0vCpN8DeC5wbUT8RH5JMfSkQu1dnkZgt3SZjdUKNVrh1Jn3IPcW0rE66KK-do_eQ-ee85e9es8nVa31IrSMze6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زاکانی: پوتین گفته بود که نیروهای نظامی روسیه به من گفته بودند که ایران نهایتاً یک هفته می‌تواند تنگهٔ هرمز را بسته نگه‌دارد!
🔹
روس‌ها به ایران گفته‌اند باور نمی‌کردیم شما اینقدر قابلیت داشته باشید.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/442383" target="_blank">📅 22:58 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
