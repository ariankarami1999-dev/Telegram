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
<img src="https://cdn5.telesco.pe/file/QcDJAgCY8Hj73dMOAKhWYEG4ikGZHtW7sI6SI-zwEbnYlLk3-8p-8RK-SEWM5bU4ZjAJfMiWaQmVB6EMHiGwFgL3w6_KjIalXkXvxE0q66tdAWvO4cjZw7cdAUu-y4wcPvtUYcLBiJKfxcmAquJmaYzRzGoxZkgeGr67P-V3lbckc5HmYmsTQt6YB6mJMPj6OXnumkpFfwOfpYOEJRyvbxZf80cU7AeQa6VRvu_LQjrzpVhDRiZNYYjmmctHAeUUxzZA7hEgMD_vXEjsTwopjgjmq9OV8KLv45Pb3X0ptc3w8RrifMNRe1CtE2RG-748uZMdZVdz7OcpydqtjOYLYA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 426K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 14:49:11</div>
<hr>

<div class="tg-post" id="msg-105585">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rFRSmgIquJ7Sd0W9eaL2SD3mnMzAiswkXvxtROQFe4REmSBmOkQUBnGgjTdwLs3_gJOuVtePXYaANs3wbs06sxbsB-keAV4dYFKBGnAiZEBl0tn2Kbt7y4Gg4_v6As0SZx347sF50HVrn2lDIore5ZDJKW3yAyK4jc2ZjXN2lLeJ7voveMGyRDgHJj1uucfv4BeOOJuy1hTR1LVD3sVOKMjwjNmzRln4CMpMC0zl6lWT9qS4S56EQcrgWDSIH6MG79GVTknrZhh7OR5XkE8i97hlMVi6NHsr0cs4LjwUpju2SAJrEHwCA18Y2kZPoRJx8k8MDhRNAeLnEQ-403NDTr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b748609641.mp4?token=RzunL_DpN2NHsZfjNwDcmWO40VKtB7nNEzxdG90go2s3bV0kBxlmMV9SXikhNokzXxPuRi23u2flZVL9xkGDem9GGrNm3wtOmIGk5hv5rSBbG_a1la30pCrz67SAZXFjjyRCz8OFBtlSZjbpbV6y3RRXtCd_aj1Zgndg-bpAVYN0gVRjNoHQcIp1OUfCuNLt26yBfBT_-fd9W0z8e3-0YPi_iH3Av9KRbPavIYE3te7mlkm5Pvv1NHGH1fJ21P0Wdo-s9na4uvk1AThoO-MVmakLE1PttiIdswmix_iyFu63nAN7nNXoRFcRn4ZZsIAr5NDuL8x7Yzq3enPR1Cz3rFRSmgIquJ7Sd0W9eaL2SD3mnMzAiswkXvxtROQFe4REmSBmOkQUBnGgjTdwLs3_gJOuVtePXYaANs3wbs06sxbsB-keAV4dYFKBGnAiZEBl0tn2Kbt7y4Gg4_v6As0SZx347sF50HVrn2lDIore5ZDJKW3yAyK4jc2ZjXN2lLeJ7voveMGyRDgHJj1uucfv4BeOOJuy1hTR1LVD3sVOKMjwjNmzRln4CMpMC0zl6lWT9qS4S56EQcrgWDSIH6MG79GVTknrZhh7OR5XkE8i97hlMVi6NHsr0cs4LjwUpju2SAJrEHwCA18Y2kZPoRJx8k8MDhRNAeLnEQ-403NDTr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⛔️
🇮🇷
🇮🇷
لب‌خوانی صحبت‌ها در صحنه جنجالی داربی؛ کنعانی‌زادگان درخواست احترام گذاشتن داشت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/105585" target="_blank">📅 14:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105584">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBXr5MzcQ-rMSLaBRWOoLqgDCFJ2023n4sR6QHxYFr0EglPxK382JWOSAXv-5qxHJiI2qLIndV0T-vWaJRoVLSZn0_elzEJc2AScW7jBCNxQqQQTugTNNBscapSXiDzXLI6XN8zxWTmloejzTP208CVeoL5c19Vp-sKheIJRSVWPLSMI7pexXL7Nlp6niJhZ39HfNEmpLsX_NNFWW1prOjZRI7GPM-sHRdMpA8o0WcQlGT1KgIe8Iuwf9r_f87idGFcJMOuTc6nLYuvxoavohdyXzRP99OSEQZKesQ7OujVuo67EtPguleKGhNf3--4dSf_mVOesi2HkVnCSqPbatw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇮🇷
💸
هلدینگ‌خلیج‌فارس مالک باشگاه استقلال اعلام کرد که در ۱۲ ماهه منتهی به ۳۱ خرداد ۱۴۰۵ موفق به کسب سود خالص بیش 187 هزار میلیارد تومانی شده است که در مقایسه با مدت مشابه سال گذشته حدود پنجاه درصد افزایش داشته!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/Futball180TV/105584" target="_blank">📅 14:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105583">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=tcj4eQClqwMhleEz-JHKbq2Sbm8juaigR2a8IaM4er8RmsyIwvP3ii_MVYcy5a98PPkCsV8zTwKwJM7jn86uHKih0cPMgd0LeuvUt5Utsi498DaoOvnv8BAiYEOxRespLK0faRtu2gc3mL1OLpZwpogKZ4ALmPPoMhVwJPjACy2aULNML1k4WdmAxbCItZTVsUEUAEArJzkmXVUCww-4aGrjtzmC4RI7GiimsfapCCizltr-lZdbaGLkefKRPyV68X1kLvOf1aLFy6OlBIgU9omIm3qWlLXeDZ0VvtM7fuhdSZUYYfTO4OJDos29KVMSS6MIvlMUKsMmA1Lpp_hEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf4edadd1d.mp4?token=tcj4eQClqwMhleEz-JHKbq2Sbm8juaigR2a8IaM4er8RmsyIwvP3ii_MVYcy5a98PPkCsV8zTwKwJM7jn86uHKih0cPMgd0LeuvUt5Utsi498DaoOvnv8BAiYEOxRespLK0faRtu2gc3mL1OLpZwpogKZ4ALmPPoMhVwJPjACy2aULNML1k4WdmAxbCItZTVsUEUAEArJzkmXVUCww-4aGrjtzmC4RI7GiimsfapCCizltr-lZdbaGLkefKRPyV68X1kLvOf1aLFy6OlBIgU9omIm3qWlLXeDZ0VvtM7fuhdSZUYYfTO4OJDos29KVMSS6MIvlMUKsMmA1Lpp_hEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇪🇸
🇪🇸
آیا پنالتی امباپه باید تکرار میشد؟⁣
📹
تحلیل صحنه پنالتی توسط روزنامه مارکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/Futball180TV/105583" target="_blank">📅 14:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105582">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71a26a715.mp4?token=PN2LSFoSPtSoGSEfkJLqjiYrHMTPUtzFphcUgFPL-zlEehMSRRanJdOyS84eQ_l5_aIdj95YjG1we07WjB2KNcnrSn_tzzcKikpp4YcrLs-cBcDjQxwJ2L2KlTiZJuB2MQ0J7cwbyBLEHaNf9i7k-c0gYGXKetHRHyyRmbmMNE3tsX-RS6c7H94Pu3S8cZpTgk4jX8BrocsbMiVd5rZWFPzUGwoVqduJVOwIRKLXU1HXz00GthckqwWbadWPYb0MzXPJih4vu91ElmfhB-qYa8CrhSgi0AEq4GIQ6qjLwA8FqGGLMTZrs5EEXW6mrG3m5nBuzEDmJdAUi5H-fTgIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😁
😁
😁
😁
وضعیت دیشب فوتبالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/Futball180TV/105582" target="_blank">📅 13:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105581">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0lp9RZHNx7iigFUHeo-jv6jj_nRfh_GQHINCesrrAcJiJKMWXnQcUX9lLGqZlIKXWGyQ-1h12NgssAANW4BUNSd-Cu7bmxwYhB_WHxV9N81MU9UaUVUqB_LJ5Pyck1q8dqnRFYFkDnSjsw-HdXhyCd1UOm63lFR50HIAByGnrB4UFoxUf0A_fboGX7vvOIwOp1XbUqP8MpKtOAu5mSsJnzAYaByOv17t8J-uEcUR_38aypVCAhEIrc5BggpNp8WiQFYvUj3bmp2iP9jLOoxQcOf41MJSzMCAzrPGtPtLiktIjPjGrtjxKDJOnJOs14OK9Y27OSnty2V4WEIvcryeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
20 تیم برتر جهان، رتبه‌بندی شده بر اساس ارزش‌های بازار، طبق داده‌های سایت ترانسفرمارکت
💸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/Futball180TV/105581" target="_blank">📅 13:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105580">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/105580" target="_blank">📅 13:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105579">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
⭕️
⭕️
🇮🇷
براساس گزارش برخی منابع خبری، سهراب بختیاری‌زاده به تاجرنیا اعلام کرده که زمینه فسخ قرارداد با صالح‌حردانی را فراهم کند و دیگر قصدی برای استفاده از این بازیکن در تیمش ندارد! به عبارتی از این لحظه استقلالی‌ها باید از بین سهراب و حردانی یکی را انتخاب…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/105579" target="_blank">📅 12:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105578">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
‼️
🇮🇷
سهراب بختیاری‌زاده درخواست برخی از پیشکسوتان و بازیکنان استقلال برای بخشیدن صالح‌حردانی را رد کرد و نام این بازیکن را برای بازی فردا مقابل آلومینیوم اراک خط زد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105578" target="_blank">📅 12:47 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105577">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb7600cfd5.mp4?token=iomDK0C62Bied5CjaZXz-6ucYN_cxmVlVkuj_O-t3t4mjL4brCKh2USwQeTMBLYifxKAiycp0mEInDGM4lAExEZA33BNPzkpS6Cfdaaai5mEOcm78lCIrk2EiOBCYOLOR1X84BWfdBnwp5388tmPalbjqJxDKpzw18DEpcC2GzFdSR63rlyXHxzSJTZAGTnrdR87fL3FK0r6kjYB-mePLKoy88HH77vPwtunm1AfLJiNgwXB_T_oS5TOARRN6KLHshLWp6n06ZmF3oWDmsnUCaMIxSGC-pKWYym86G3o289rBFt_u9_ksL0TkqIB65L5kusVdYPSW5xMCU7t21pBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
وضعیت دخترای حشری تایلندی بعد دیدن پرسنل ناو هواپیمابر آبراهام لینکلن در پاتایا برای تعطیلات!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105577" target="_blank">📅 12:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105576">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🇪🇸
لامین‌یامال در آخرین تمرین بارسا پیش از بازی با والنسیا بدلایل نامشخص غایبه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105576" target="_blank">📅 11:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105575">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mzGAwe8e5Wj81rEIEBpig6-oBzW90Y2JGiR22z7oDbkDINKI4dZm12_BOSK-3eeQsreTA4hCNo6o2D6icZ3vTEM8m6RwkyML-qbKJNgOhgObzKLGtAFim4ijkNHDXHnr32OF7fcK-R8v6hagDM8okbF9gc3gfWkZ3r7Oy1F8I2wCW6mGc7BMPuNZf030VeQMDg10jXqJL6UCiYRdi9MLDAPnUXrnGPZhX1d_eOpF5HgCcDcUKmkVhqi0gddHY96eJJnqtbLPtw-1mIPROjYatdnIpQFda-ne-JJd3jSrC3zdiXRdb7nnhO3Mbxe2dxnxzJvWwYnhSgkbqffKsWM2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج رئال‌مادرید در ورزشگاه بتیس از سال ۲۰۲۱
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/105575" target="_blank">📅 11:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105574">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c140b1799.mp4?token=SfVHXH0YDFrYQul9w6avorAO3PLiW7saWU69LefzDSZWEzgzoaUD7oWeg1vuu7fhB_fHTUSVFO-E-WK2pT4DXQfgS91OU5J3w9JnyQdAOJb11_OlbQ9qWiCxAtD0eYKAF9yo6yVz1a0CIVvSxM1AfZJ---QglyBqIBH_s-qifdVQCJv3SfokK9deN9ixOEGWI3n7NmYAyX2dIv58vIbFMB_57renhHfpCle63s7CGd7gbbh3AlSJ247Gp6TlJ4cO30d1tduBycFkmAWO9Vow371w_V6EpijMv1JmuuloJz9SjWrGJ7ISg6LUXpdI23HQ8kEDOzYri_gMvbI8FwGAWZ4awUdGoDM_9m3-ay-b4uxOAy7v0dNDumt_rCsUJSwyuxTPOd0u1FPKak3b69GZaxtxTxTx0qMdXFhaEEEpShzureR5jo6Ma45rs4nHRoSq1go5bgV-LbOZlXOTi1VUo2sbAZSYWcTlqlQbLNH8oz5Xl3oovL2Y3S3032UKbdobb_qZZUdHzNmqP_2La1X1Y9-_J90D4hLr1DqN7hAoVxrvkwJMkezm5Lu_vV2o2uYetS8YhlR4rn4_bTc4ZMdOGXcAJ_9sJe4aBT9BZsKISlcUe0e4KYNinuB219sHZZAJ1C1GmJ0to5E1ZM7VkD8kjHjpxy7kBI7hqIFYACr-Dm8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🔥
🏴󠁧󠁢󠁥󠁮󠁧󠁿
زوج فوق‌العاده پشم‌ریزون ازه و اولیسه در تیم کریستال‌پالاس دو سال پیش رو ببینید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105574" target="_blank">📅 11:29 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105573">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105573" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/Futball180TV/105573" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105572">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pv95tEwzBbN7QUBZXQQ87VW7IFRhACc5SumPmGfmwL75Qm6iIhTgCXFU4ReVUrLWZ9Z-Otj4h4XwEjKM3gzDgAU1NcYqTr7Je_Yyac7dDd38CfEXwXGcIFWg2Vlntj2A0_TenrQRjit5UhMHRu22vSTH_s19jyYfNOZacckOa5G4mKQUtogQTeT1I_35czPi-Xb-cdPtX7_ntnQE4-Kd1JPk81HnC8rSQcDWWjPuRoiIUdbbjkkrBV5WNVvvQwgH3ZVJRbrnCqcGkcn9foYP0VB6IsfIdDZgtmH9LMwNzoKXd8JzwqY6GxUxZpdHbnJcwlaz5zIhB95NBqiJT7X2pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
بورنموث
🆚
نیوکاسل
کاونتری
🆚
منچستر سیتی
تاتنهام
🆚
ناتینگهام فارست
اتلتیکو مادرید
🆚
اتلتیکو بیلبائو
ناپولی
🆚
اینتر
آتالانتا
🆚
رم
دورتموند
🆚
هوفنهایم
بایرن مونیخ
🆚
شالکه
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
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/Futball180TV/105572" target="_blank">📅 11:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105571">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c6aac1de.mp4?token=i-NVTaJ36HxGioJzToEn4TpGI2OGjT5RijLJC5_3RL6sc7XppcGI1TGTiH59NRfmLyPtrQk4R2dEDiWAEwQMS1yJg-EZ839xEMpKofJfP1hM-re9TLZrHEFLfKDhhx-pJ1iRac9TrrO9OsLCvBqA2X-hRQhxnJjoVOVYLeJVRJUUOq5GLhOw_Qo04JVm0dAuC8zT-5y-6AzYxmioiNPs1RN67DmGVKEWhd5vGaigSc74oh7vPbiPfsI1lizrajnEqt95ZOlqfJVJEwOEW4IhWH_CX0MRkh02orBAovqq94FcAtWo0KrZ7QSdhVQAMUHE3-LsKeopvAr3jXJHehh3nZdHT1XRw0vgFQJTVLShfVGF5C4r8S_u8Gvvu1rL_1bjtyyEkDWdCjPoUlCgM6-8ccFxUdM7o3J9VZCscS7y6JZ0Jxynec_u3D6wO5PSu4vM70qJXuliwUDmWd4c1UEaNyGdGyQhRIzMiVIZQ-T0PdSboSninubykkkiRoILrw1KSm3PAeIHNo0vkQRfKK8Q141virnObaFQZIRJwddOI-DYqcJtBbh52Sdqzh5muiarMVbWuSIzeIEK0nmXMTu-P1YVZmPrs0wxY5QnPENhVt6O0OvMK2Xybk8woKKeMTaylwgukjKwoDQF2sBcTbRQdpBHTSMdwb9zikSO13PewxI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
واکنش مورینیو‌‌ و نیمکت‌نشینان رئال‌مادرید به پنالتی که امباپه از دست داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/105571" target="_blank">📅 11:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105570">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
✅
🇮🇷
صالح‌حردانی که دیشب یک استوری در حمایت از سهراب بختیاری‌زاده گذاشته بود، استوری خود را حذف کرده! با این حال سرپرست آبی‌ها به حردانی اطمینان داده که تنها با یک عذرخواهی ساده می‌تواند به تمرینات تیمش برگردد که تا این لحظه این اتفاقی از سوی حردانی رخ نداده…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/105570" target="_blank">📅 10:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105569">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=tbS3PPvlrH2hgzF4va9PJM_ALAKHCH5Doi8lMO6N-I3UM22mosPT4BcW0qlXYfV1GQi5YoH0EK6-knsdpAbsuWa_-IIRPXUKC9RwQxHcfFlqJhMQ8Q1VX6R9TvmFAcWy_x_HDB_1Cm7jAJ9W4cWsQsRb1dG37v-6DYrnq6z8wVHUloHV_lTmUaKe4VoFABEKrznoh0saa-llSJDqcsoEMs0NNZTszMZSz72vCiBEBpiZr84Ih2bTG2vWvMYO3L7Rm9Cu7hQpee3wqXcehFnIM66s57oUB-0fhFNJc1nluqBS-G2wHgcyTN4rZQKWmM2NxtbO3xrayCa9cg5X0Z8R6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf1cf6a70.mp4?token=tbS3PPvlrH2hgzF4va9PJM_ALAKHCH5Doi8lMO6N-I3UM22mosPT4BcW0qlXYfV1GQi5YoH0EK6-knsdpAbsuWa_-IIRPXUKC9RwQxHcfFlqJhMQ8Q1VX6R9TvmFAcWy_x_HDB_1Cm7jAJ9W4cWsQsRb1dG37v-6DYrnq6z8wVHUloHV_lTmUaKe4VoFABEKrznoh0saa-llSJDqcsoEMs0NNZTszMZSz72vCiBEBpiZr84Ih2bTG2vWvMYO3L7Rm9Cu7hQpee3wqXcehFnIM66s57oUB-0fhFNJc1nluqBS-G2wHgcyTN4rZQKWmM2NxtbO3xrayCa9cg5X0Z8R6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇪🇸
اولین شکست فصل رئال در خانه بتیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/105569" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105568">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQXZLKOozhID2sbLhADObvbb9RbgrZD2abGubfLPichqQUVvE6jWCKiuTzbIMkEC0EaTxXujMHA5m4NugSEZc8VKFEyF1nwnpLkJNqg0KAnx82Ne_nAUOn5YP-i7daV0InKvbyKlZLO0n-ON7a_H9T4mzrQI3gVtWdSpj2uQOLgnfHGnrNI8nhyKFu564btBDI-kL4YXsXXRf593EntdK_Qqv4ykyg-6QZRzGTMGTQkWL08iSctJKZlokB6A55jYWZ03Na7xKUhvU0PXYckUe_MsiXi1kcYK1z8vihqNcgmiR6ql6-v1_hbfX_HkefRDf0M8B-9nHRMC8vhU5tHYAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🇫🇷
لوئیز انریکه درباره نتایج ضعیف تیمش: اگر دوست‌داشتید میتونیم روی قهرمان این‌فصل فرانسه شرط‌ ببندیم هرچند که من شرطی که خواهم بست رو لو نمیدم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/105568" target="_blank">📅 10:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105567">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=ugT_ZdSKX7PJVJFQqK1WAkXN5AqSFYiNi4PapeCesbVonwxmdjiZuKZ_qOD22tXF45RE50xFY5Yy0E6v9mKjUd6Umym1UmgfkECABg-DlGESrlyGylTqjckDWyZo-BiGQUHg-tFQRnVnLdBNQQHjTOBoiYMoqqvhZui4K6ZXvf2maJxMjCDBH-0-Tu8mAOTmgxhqn1P2_wajqhTgh2YMpPrUkllGgIgSNz3u9fHseYYLeOeL_S2PYaw4KhHkj7QpPxNCb8Aygc_vfDyNemi0LpFwiU5CwhpBcturTUoH0bxMQv3PifVyHOdbw8WzDELuFwXX4yXyPLibvaU6PwlfLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0094c6fe9.mp4?token=ugT_ZdSKX7PJVJFQqK1WAkXN5AqSFYiNi4PapeCesbVonwxmdjiZuKZ_qOD22tXF45RE50xFY5Yy0E6v9mKjUd6Umym1UmgfkECABg-DlGESrlyGylTqjckDWyZo-BiGQUHg-tFQRnVnLdBNQQHjTOBoiYMoqqvhZui4K6ZXvf2maJxMjCDBH-0-Tu8mAOTmgxhqn1P2_wajqhTgh2YMpPrUkllGgIgSNz3u9fHseYYLeOeL_S2PYaw4KhHkj7QpPxNCb8Aygc_vfDyNemi0LpFwiU5CwhpBcturTUoH0bxMQv3PifVyHOdbw8WzDELuFwXX4yXyPLibvaU6PwlfLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
به‌نظر شما دلیل فحاشی به شجاع خلیل‌زاده در ورزشگاه عادل فردوسی‌پور است یا رفتارهای او در داخل زمین؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/105567" target="_blank">📅 10:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105566">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=hZfWXNNeaeofXIO_tZROIi13-iObo-tXe_Hdb1Ej1pPZCsP6zZqCZUjD26S94vI6YAZVRNRh79S0j7WWV5nrUX3vtXAlAB5wzb-iKQADDe_IzREAxI3gboe73WxLH2tQPIaVZBXV4m1nt-5J7L0PChsnNucvfEoRIbEnRKdDRCZwpsLeNfGPPXVbiaLHh9w9blmYsUa4RphE_2D7kPBibcZg3DYTI6NgF1owdEcKTwjHuZXmH2qMtczMEaSI2wz8Idxl1BB_VTmsufHG8h_bZTrBuX38WL-KpmgfCBqV4sS4yhJGM1JUqL74BLuGVJ5X177dxXeYyRT92O1KitYHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ffae934b6.mp4?token=hZfWXNNeaeofXIO_tZROIi13-iObo-tXe_Hdb1Ej1pPZCsP6zZqCZUjD26S94vI6YAZVRNRh79S0j7WWV5nrUX3vtXAlAB5wzb-iKQADDe_IzREAxI3gboe73WxLH2tQPIaVZBXV4m1nt-5J7L0PChsnNucvfEoRIbEnRKdDRCZwpsLeNfGPPXVbiaLHh9w9blmYsUa4RphE_2D7kPBibcZg3DYTI6NgF1owdEcKTwjHuZXmH2qMtczMEaSI2wz8Idxl1BB_VTmsufHG8h_bZTrBuX38WL-KpmgfCBqV4sS4yhJGM1JUqL74BLuGVJ5X177dxXeYyRT92O1KitYHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
‌مخ زنی به سبک مهران مدیری در سریال جدید مرد سه‌هزار چهره: فقط اونجاش که میگه برای من منگنه بشید
😂
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/105566" target="_blank">📅 09:50 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105565">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=VFA_YqFD0A4C84sjJfyFZ801jz149q4d177FABrEgbNTJG4ctKkANLReKlhmn3DwWyMI_CYb84_IklqDFmF229-ApPbwE2cB9r524JJhSI2Bro1QbYddegHTm83fsULu7BqjqQngXatWcKf0itP_qUqsdCi7jm3io_BSzIsnIEIkwq0UAibjaEAjPNBOT5-_DQKHb9kpgA2Cu8GFkQvVN4NKlbByIXWHit1qRVo1ScsiTpEKLcUBSLukemOx37bPj7y8jKEKRbFLETmUzQdeYV-eWty8ZKwu4Apwwn22RSiHy804giY3gGvECpv1UA9nsKTi8sobwHsG2ri0ZflfXJDwFH0Ck7uvER5XbEZz-WziTLQN7pd2lIGEt_9ZMTmlf3h1Inodv70X-0S1AezX0lT35so4D0TKZxp6jUrxu3Nn4AxmP_0vEDkOIr9sXhJ5ZW3cOjJVFPDw0uWnpEW7CEbMjqnV9IrpE6gZsxwE3OKVsm0hR2ScWQ4U1mzTnovppiltiehTd9LX7sjEHINssQDMzlDhLFvqrik6S4aGPa_Pt0nGTfPM6ARKtcyAEcRiUCPzsRTN_r8pjixpjP2n4y3tPNJRwdnTk4YajRTVoIzrdqSd84XGBnWX-fviAlGoNpPqmzxXopcEoJERVxM7y-ypA-mzto3_0Ze57WPrw2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe613df04.mp4?token=VFA_YqFD0A4C84sjJfyFZ801jz149q4d177FABrEgbNTJG4ctKkANLReKlhmn3DwWyMI_CYb84_IklqDFmF229-ApPbwE2cB9r524JJhSI2Bro1QbYddegHTm83fsULu7BqjqQngXatWcKf0itP_qUqsdCi7jm3io_BSzIsnIEIkwq0UAibjaEAjPNBOT5-_DQKHb9kpgA2Cu8GFkQvVN4NKlbByIXWHit1qRVo1ScsiTpEKLcUBSLukemOx37bPj7y8jKEKRbFLETmUzQdeYV-eWty8ZKwu4Apwwn22RSiHy804giY3gGvECpv1UA9nsKTi8sobwHsG2ri0ZflfXJDwFH0Ck7uvER5XbEZz-WziTLQN7pd2lIGEt_9ZMTmlf3h1Inodv70X-0S1AezX0lT35so4D0TKZxp6jUrxu3Nn4AxmP_0vEDkOIr9sXhJ5ZW3cOjJVFPDw0uWnpEW7CEbMjqnV9IrpE6gZsxwE3OKVsm0hR2ScWQ4U1mzTnovppiltiehTd9LX7sjEHINssQDMzlDhLFvqrik6S4aGPa_Pt0nGTfPM6ARKtcyAEcRiUCPzsRTN_r8pjixpjP2n4y3tPNJRwdnTk4YajRTVoIzrdqSd84XGBnWX-fviAlGoNpPqmzxXopcEoJERVxM7y-ypA-mzto3_0Ze57WPrw2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
باشگاه نوریچ سیتی هر سال نشست خبری ویژه‌ای با عنوان "نشست خبری با قناری‌های نوجوان" برای هوادارای نوجوانش برگزار می‌کنه تا بتونن مستقیماً سؤالاتشون رو از سرمربی تیم بپرسن. امسال هم این برنامه برگزار شد و البته با یه اتفاق ویژه همراه بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/105565" target="_blank">📅 09:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105564">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=RKF0LYhCK0KT65inccAs7QoRN5T96JQnkyh5CLFy6vKo2GMGBVqub4NLON4WH3N6xL3iq1XEFM9ehnEek2RWGnsV0D8XHnOHW4ENU8StJry60AGF3C-gZHVurcRO1NhkmhNk8YLI6uyqfd-A2w_JXwd60ih9SjG8V9sQLWBMbDMWC6C19edxkGmWKvJq21Nac4vlQz4AzIF4qfyQNRN1344px0-qAUI4K1fJzdjFAHMcQ5_8elMTEj_ZPGy7w9VhefqzGlkwyPdT6Z-5jT8h_eCCLA6tqCPAcT0yHRfbapl3-xaroEoKtUR_hEK9pSv7rXLAC-olmcWM5dGLL0hRuwgS1H9bntGFMNalkZLOhkRE7EETbEFQLCv88VnxuhrRJnfiFTVwsoKMfCV0D0UZ_AG86-zQTcaTJI62Yb6naRWpCbMrD_ltqRqVMxHYYbKFcHpLLBdkr6ZmEVqU7elGWmBPzcuu1VF-yP1yA6sD5hV6JTvw63iIl0IX5KSuRZCbZiavTqFCbcgqGLDDminy0DJAMYn8fNCVlVYQ2F-6T4HrZCqNK7Gc2fj071uGQpn045TjdxfuQ8xzhddjONVBjNHhH1YKy17VmSM9sqKcpXBE5mYB7HbyBR9u5nZkkVdF6BH6GnpHAvEniS1kUR2WDd_spL-Z6G_APjLYJWHzBkU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01f66133f.mp4?token=RKF0LYhCK0KT65inccAs7QoRN5T96JQnkyh5CLFy6vKo2GMGBVqub4NLON4WH3N6xL3iq1XEFM9ehnEek2RWGnsV0D8XHnOHW4ENU8StJry60AGF3C-gZHVurcRO1NhkmhNk8YLI6uyqfd-A2w_JXwd60ih9SjG8V9sQLWBMbDMWC6C19edxkGmWKvJq21Nac4vlQz4AzIF4qfyQNRN1344px0-qAUI4K1fJzdjFAHMcQ5_8elMTEj_ZPGy7w9VhefqzGlkwyPdT6Z-5jT8h_eCCLA6tqCPAcT0yHRfbapl3-xaroEoKtUR_hEK9pSv7rXLAC-olmcWM5dGLL0hRuwgS1H9bntGFMNalkZLOhkRE7EETbEFQLCv88VnxuhrRJnfiFTVwsoKMfCV0D0UZ_AG86-zQTcaTJI62Yb6naRWpCbMrD_ltqRqVMxHYYbKFcHpLLBdkr6ZmEVqU7elGWmBPzcuu1VF-yP1yA6sD5hV6JTvw63iIl0IX5KSuRZCbZiavTqFCbcgqGLDDminy0DJAMYn8fNCVlVYQ2F-6T4HrZCqNK7Gc2fj071uGQpn045TjdxfuQ8xzhddjONVBjNHhH1YKy17VmSM9sqKcpXBE5mYB7HbyBR9u5nZkkVdF6BH6GnpHAvEniS1kUR2WDd_spL-Z6G_APjLYJWHzBkU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
بیرانوند: مردم فکر می‌کردند این آخرین جام‌جهانی ما باشد. میخواهیم در جام‌جهانی بعدی هم باشم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105564" target="_blank">📅 09:02 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105563">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=vln6TfZvTaksWoYWTyIhW0EaNWuTEhnw-tv2EHgHOuwbd-iKh1UnAydXIBMhJwiDl8GYm9zcoV4eaf0c1IgSJ8A8kF6lyZr0K9UEX69ifFr8jOiNr5RRCwJbOQy4wxUifjVwsNNoAvCHFaL2l0mwRPbnbwsrPaHuRUt0NXUDEx-3XFz7kfNX3xv8Ll0pt04aW1iNX2Vgmp4ryAqSCfe__PBblKMjoMTxkdn-LNsHy2Wk5Fa8u-KVPdO78HIlbCAS9xoCYXSARucF0UID7SwLjTSnKHIy-2QUHQYxrz3KouxZ6vnWqoLZJX1v3UmLkjZWxKwgt3bdHu4fyENoze0OFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edf296c20c.mp4?token=vln6TfZvTaksWoYWTyIhW0EaNWuTEhnw-tv2EHgHOuwbd-iKh1UnAydXIBMhJwiDl8GYm9zcoV4eaf0c1IgSJ8A8kF6lyZr0K9UEX69ifFr8jOiNr5RRCwJbOQy4wxUifjVwsNNoAvCHFaL2l0mwRPbnbwsrPaHuRUt0NXUDEx-3XFz7kfNX3xv8Ll0pt04aW1iNX2Vgmp4ryAqSCfe__PBblKMjoMTxkdn-LNsHy2Wk5Fa8u-KVPdO78HIlbCAS9xoCYXSARucF0UID7SwLjTSnKHIy-2QUHQYxrz3KouxZ6vnWqoLZJX1v3UmLkjZWxKwgt3bdHu4fyENoze0OFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
🔥
جورجینا همسر CR7 با لباسی از برند گوچی در هشتاد و سومین دوره جشنواره فیلم ونیز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105563" target="_blank">📅 08:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105562">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105562" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105562" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105561">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BN30SfnMt9z9wd-Xf16D5qP5FIsdcbB7m-cAWZbXfTZsTcnTIxEsTX-eneiJHvN4UMM_OX1Yo0sYkaipdQlrFmvZ5zNxRS2-OLzB--e3sChd19aiqFvDkqLTkD9-1M1OKOFFW1dxoVnRfKs8Y_s2jDVhIQ3f4K2IbLn11qPN8R2TU9BPXEz-LlcVtJB8GPll69v_QIaAt4OIoP1xdtvnDVUlu9V0DZClGjtdzfbeOlZQRVbAfuRBjheq-fbOekA0h5_pRKwxKhfiMP9P3Am4umV5-Dz8cgFKPksF4a9KpjGWDCBDEjHG493ZiYHMc1dyUigJTHfbVlVVRnVeJZcpCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105561" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105560">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/105560" target="_blank">📅 01:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105559">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=u0WLylGMoTwaU6kCHeRWkENMMEU9f90TZOEkbdLPyfXPy21xPOYWW9DQbVp0wpZXWzhbu3Of3ktA2Z--xiGpO7jJAMYh4Meg7cH5WH8sDZ_DR4QUXq0Ks4UN28_CIVCAonLYMwAJ5Xee9S3ju4NxFQELUbgiyIVRvUmqi35hcdjy2R_px23QIGhE40fgvXhwrrUYQxF3YXs9rVE0V6zdLib5xuJPQOaY8wgVy6os57WeN4gIu5fuToXxvFnxpcnOyOfZ3ZDyqaJ0PMpOqbcO7fQMZWsekPZ2ul3TcvXoW61AsnTaQbUh1liT5rMWh87lWK3RjsRLYU30LuTJFdP1LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b6612a039.mp4?token=u0WLylGMoTwaU6kCHeRWkENMMEU9f90TZOEkbdLPyfXPy21xPOYWW9DQbVp0wpZXWzhbu3Of3ktA2Z--xiGpO7jJAMYh4Meg7cH5WH8sDZ_DR4QUXq0Ks4UN28_CIVCAonLYMwAJ5Xee9S3ju4NxFQELUbgiyIVRvUmqi35hcdjy2R_px23QIGhE40fgvXhwrrUYQxF3YXs9rVE0V6zdLib5xuJPQOaY8wgVy6os57WeN4gIu5fuToXxvFnxpcnOyOfZ3ZDyqaJ0PMpOqbcO7fQMZWsekPZ2ul3TcvXoW61AsnTaQbUh1liT5rMWh87lWK3RjsRLYU30LuTJFdP1LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
رفتار سرد مورینیو و وینیسیوس بعد بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105559" target="_blank">📅 01:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105558">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPS3tsNPuZMk4KWG_RFpOqaFEL-74eV95b39-zKJXfnHekbd0NPkLDsljYfZ5ElRYkEYd2zWTD8xR6k36ZswSnO1JnZ6uAh_Yty3y691P0ztLlsCOOMeHCkQP8rxrIkRHyI1Ikqlyi--aMnHzhYJRaJaOGjV1XQ3bshiP9vJPnR4S0YqkvdTgY0K-LY5palqvPnoSzienqluffrfeInkTcsxhzLmcHlOeuep7mjyCb8vMU4JAe-9_DjJp-Uq7Qtf1axtFdMGNdiSTnwUczZn0-vcUaky5hk99Z84f1gsPy3VJhzDNpSq0ac2gpmZ3BUx1EMWsauJhXkX2_LLAGnj8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
#فکت
؛ در آخرین‌فصلی که رئال‌مادرید مورینیو مقابل بتیس در خارج از خانه باخت، آخر فصل بارسلونا با کسب ۱۰۰ امتیاز قهرمان لالیگا شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105558" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105557">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmm-oQGdycOXrIYqG0_BpIRNVR6KgiZr4VXdxQeKt1GbdtihnYVxEGdt0AhHLGF_B4n6yMBterpzs_K76Q7YlK0XxassLYpsSQA8_KWHfgZ3aP6m0NWHvWdW2mp6sxr8FizP7EqpLlZiz1maGnKrfP01bim2shROXuQecbp32C8sMDkIbWugnkTZGFyrmNMzNjKlHMtOlCP0hzynf9wmoM2pBmctTiEMkBUhLZcMgseTlBmVl6UqrwhBZN0mO0IOuqXPmkidr_HMihgPgqKRq03Sax8OJtIkKAUXhH3xJLaTjcvQD0igPZ-MT-tGsCt-NcQ6U3DdXvmPc6sd3KS8lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105557" target="_blank">📅 01:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105556">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d903ez6eTC5DYuyDCI8NwotSOJepmJHH88cF4PqffM00OnyPqg8JUDEGEgtrnjPOOl4BHGzsmry-aQYEik4jnrOGEZj3YaGZMmh1uE3PBbtJRlbf7KEBFM7F85ZLmN0l24PvI73bvnvXvrZA-YaNq-v0DmzBhZ-qwo_GrM-gGcQk9_-pDDOciMfSCvGlT-5nVB42K_PX9_XAkDuToemc8QLcEn3e6kyv1qkViPxr3KS0xKlP3qVncs3DZnIOkwcug2WokFuD8VAG2WKKVUTdwLSLXc83um8zH0G2-OTYKNIKMSRHB6Ts9uyg_GRe3j-RdnlOH7SwXW7C-gR24fxHpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وسط ریدمان رئال‌مادرید گویا باید از اونور یه فکری به حال پاری‌سن‌ژرمن فلک زده بشه. سه تا بازی کردن دوتاشو مساوی گرفتن امشبم باختن! گویا اثرات جذب فران تورس داره خودش نشون میده
🤣
🤣
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105556" target="_blank">📅 01:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105555">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK4qCPo0fEDiDojnXbe6W6CjRQWMM_zMFov66Pu-k19TV2juFPv2bWkzfXgyjXGYaLR0Je3AZdHgIVPqfPlV2pusuTuI0zE9C285Ly_vjB35HSP68ctcAkg0EJ5u07EU2LHnDjJf-ViZwR5K8uVv6ueqxEuHRroC5bUumB3op2VeTGh5j_Nvy11vNfSQoP2YvRdCW0ASgCEK3tzplgRY0wQuKYv0GH5Af9NxU6q5aYFp19X0IBFsfX6ePo8R9Canbn94M3GOVCJHjiQniTczqKr_I-yUww0cMlEl-dmUx9Vd_g9Wx_d3Bgo8FFeaqVxslBRyMTSVDRjFN0alS_J7Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇸
ژوزه مورینیو: عملکرد داور بنظرم مشکوک بود هرچند باید برم بررسی کنم. تعجب می‌کنم چرا نیمه‌اول به تیم بتیس حتی یه کارت زرد نداد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/105555" target="_blank">📅 01:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105554">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🚨
🚨
🧕
البته گویا این صحنه هم آفساید شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/105554" target="_blank">📅 00:58 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105553">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoUbWy_2lcFInXNkCM_LOuKq6xp8F-z8ADnGaFmc7ak0tTJGoHIyWaK8uj87XraP4aaMJmXQwOBwDTO7Agz5b6puosyUhpykvAOcXk-h-Z68ifkvtBlg0xr4liuiOb74DFwhUCnQQtYvIEubrwpulvwm6B0u7gyP1YGZU3i-8ms8fRU5e7jAIjQWcHRiN-0Fp-s3TUhVO9PQz82h2YAdYjdMzlQw1mNHoQOJdFNIuinhYbByhr_u9o0lRceGjj7BbkcnHMdaBl25YACBcLGxaUMBr4V1-dnjDU4_QneA5i4cofr5Dj4Y-_AbcSoABTsuVJnm7w1UHLLQcQ7kD9piBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
📊
🇪🇸
رئال مادرید در پنج فصل متوالی در لیگ، نتوانسته مقابل بتیس به پیروزی برسد [سه تساوی و دو باخت].
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105553" target="_blank">📅 00:56 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105552">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWnk3ZaFMNxm79v8m55qI0_cvvj_zVJSrnW3J0x7MHPxQSRhN67rUIWBDqm4VYZSdetN9amGkkWD-RIdRWPCFBPcuLmrpNNu0Q_psuupLu993ZyNcypXwBh0U1-84-uX2IQCk_ESTXyHCQiAeZ4FWd0t3oGntVZmB8r7nHNmoIORi1Toz7tYy-dTSPx5IN-52T1U0anSh7Lv5s1iaQ_EDGHPIloCSZNJ93_ExrdeOQh72bFULRxlej02z95V4sdP2ieX2dLONk8ePSQc9fGh_8Pv6anmNTGD_XMh5aILQB5rfLTPrWUPSzu-VNUjBqL__Zi3OpZ1RcGM1euSQhCBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105552" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105551">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdSSoMXBj1HAmK0d_KGXdKtizDqAHXsdwcnoGlhLdny1G4VQeH3_zbpFXrxA4EEDFr0wCjn2zllWug8QC-v7dm6XyvzFflvdekda23cnkwe0hInMRq0Tsk8MvHqV4h2uixba2SPkh2Y48CbewtXkIxe7OXmZRcMD1mXRwQ9I1cKoGQcM1CxOsGKqWhkvPj7Sd5ENPfRQx_Cp5fymwnREgYdzmBLQrCuK3qcTsDAfVs5z0xqqGzU-wF722M0LDtldLTiBq4nNgzox85rljAR9RLQSYbLjVCT-SJD4UDhY1s90NYAChcgi6TKA4QL5YBoLWm0aMad62rMOpPIyd2fHxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هفته‌چهارم لالیگا؛ نود دقیقه نفس‌گیر در خانه بتیس؛ رئال‌مادرید با زور پنالتی هم به امتیاز نرسید؛ پلگرینی مچ مورینیو را خواباند!
🇪🇸
رئال‌مادرید
😏
-
😃
رئال‌بتیس
🇪🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105551" target="_blank">📅 00:36 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105550">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105550" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105549">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AE6jfLixIJt-yaneNJOWSXNSiZgDjKiOTCkrN80xcavxW7RjBjdRR8wEVz7YWLatU9DC-nldIFcbMx7ovJzENK153dzNq9ihWgjPsdOFkZC5yJwNshgGnbDwPVXvbegT46DJljEjmWga1vJ_-_fV0IkkRPEmTQxzDDLiaEKoHLP1eN-EEVOCh5s09gVTSa0v3OPkzmkN-EjDuvzmjHC5li5B7FNPjzFP-tNZsdaQCN_Z_m9Llf8hvAy0bUf2FjIGls1spB4DBChlgm8gvEhFWeRpJq7VK9fHUpy8e0s3qpxgi0MxLuR44lyJYwYG2K1gp671RMVUGzwkmKLcskTc3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
داور میخواد پنالتی رو تکرار بده
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105549" target="_blank">📅 00:33 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105548">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رئال‌مادرید بدشانسسسسسسس
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105548" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105547">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وای خداااااااا چه شبی شده
😂
😂
😂
😭
🔥</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/105547" target="_blank">📅 00:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105546">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
🚨
🚨
امباپه ریددددددددد</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105546" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105545">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">بدلیل خطا روی وینیسیوس
😐
😐
😐
😳
😳
😳</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105545" target="_blank">📅 00:31 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105544">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برای رئال
😐
😐
😐
😐
😂
😂
😐
😂
😐
😂
😐
😂
😐</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105544" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105543">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پنالتییییییی</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105543" target="_blank">📅 00:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105542">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV-nDXJnkToX0LF1sP99Tqo7VutR6U-Z0CTDyVPsJpn2yaDgl2s9J1PMWWPcyBgCTeXjIOaxJHJSsTfoe3ng8fxyam5NNf699jxmkNFXn2SHx1AXHAVvMhytB8J3WRJwl4zQSCt26C0jq7CN1bqJFXcoLb7X01u_pfg1t9XD_1xB3piu_1kSkL9V_JYLebhf-PH4Gp155a4USFjTmVoQmjfOn-haJ7p3EnmiFKzvFbai99Duqg246saCHckISl-supO-4TWGUSUXjg0HUrPAxjY2lKackuXJqyZy20Jh5iYhVS3GiBRI7yYm9PumSOqrKo6Vc_et9bSe4OtbS7oMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
آفساید ببینید و برینید
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105542" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105541">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🚨
۶ دقیقه وقت اضافهههههه</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105541" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105540">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7IFkEytNs1wvGrW_mzSPxlfZyhI5B6zJ1Sut1lk8p1Csemy8d9Qg5r-cub85pOkM__Ue7nVl6MkB31OFiBpLfX8qzZ0ZSvuVYsc92CXTeqKG_YbUxjelLQ7JQkxDxUMxJRywbnHE6nDgYAZC583oxGL4jI4KskQSH0rgfoSBGowi6zylOoBIIT1bHpE5Dxl9rb2Kvg3rcFyCFI-E2_RTupq8H5YcGWnO4haKe-Uj0nxlvyLxSZAQWH-bRq3bbXBMxT5vb4ETVQ_H5ScZL-Ud-7IF2qVlkpth-lab9kZarJ6fELkbk7LhW2CAvhYUM0VsmaSSX1MAeD3aju1xb4FfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید اسپییییییییی گرفته شددددد ریدم حاجی چه صحنه‌ای
😐
😐
😐
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105540" target="_blank">📅 00:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105539">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105539" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105538">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🧕
آفسایییییید رئالللللل گرفته شددددددد</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105538" target="_blank">📅 00:26 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105537">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اوه صحنه رفته وار</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105537" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105536">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسپی نگو سوپر بگوووو
😐
😐
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/105536" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105535">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رئال کامبک میزنههههههه ببینیم یا نهههههههه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105535" target="_blank">📅 00:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105534">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چه گلییییییی زدددددددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105534" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105533">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">پشماممممممممممممم</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105533" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105532">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سووووووپرگل اسپییبییبببببب</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105532" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105531">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گلگلگلگگلگلگلگگلگاگا</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105531" target="_blank">📅 00:24 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105530">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رئال تیرررررر زددددد</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/105530" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105529">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105529" target="_blank">📅 00:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105528">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اسپی برای رئال‌مادرید اومد که گل بزنه
😐
😐
😐</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/105528" target="_blank">📅 00:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105527">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">رئااااااال ریددددددددددددد
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105527" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105526">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بتییییییس زددددددددددددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105526" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105525">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گلگگلگلگلگلگلگگلگلگلگلگلگلگلگ</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105525" target="_blank">📅 00:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105523">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=FePUGi8MahagotJ4QQurej1cqdAgb4NbQvFLimg2vikaYEpai8Gf8Hc1he5hLhe9lWQ__Z6BK3-i-I0zYx3kZiJabqCvRvcc9t3IyPU_oVge6TCKHtBItWCh1vPkKi7Mi4PnvWtY4H0OXzqI8vWym_Gt6tjxrHAlahnr9qYcNzr2YyKWa2NzK_qJlOxcJKupv_U1RpaI1fQqdi0l0Vc8wgAuFMcF1uBgU819CSJnxZIhVAvSReVg2EsxEzUPvbMnxueUkviKMkAgy34jZRcE7RDiw80sistWOWveHjfenNYYPqQq2VZd-mYLniMjX7hAjnVWIkkcegPG8C-NDfPabXdiyIL2NWxwFAYtHc68T5KLBOU3p1LEOQKxQbIkxc5vBWtoOSneNqTZeEQ6jCXT1c_-tqilsAhGgmmxP5M7DZVWovj5p-OTDUfPM45vuqH1f9Nuhvr7u40sLj4m6h7BZVbZ4S-Fx7YRBXmnzbTcaHbTiXIHnDilTu0P6iRYhoPeqX9qOelu3B60y_YkTfQd6jv5hWKyTjKU3U1lkRl8O-PQXNbmOmRaVGQpjSh82HZKRwiaIrR4HEQIHoxlPcqAh8H6EAQE1W1wR2dJzpoR-l1woqchbgTuT_YSdpON3WmfThFeQ1hiebWxhMWJ4G7bj1kLdkPttRNH6rqKeqoUd7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e62db78c19.mp4?token=FePUGi8MahagotJ4QQurej1cqdAgb4NbQvFLimg2vikaYEpai8Gf8Hc1he5hLhe9lWQ__Z6BK3-i-I0zYx3kZiJabqCvRvcc9t3IyPU_oVge6TCKHtBItWCh1vPkKi7Mi4PnvWtY4H0OXzqI8vWym_Gt6tjxrHAlahnr9qYcNzr2YyKWa2NzK_qJlOxcJKupv_U1RpaI1fQqdi0l0Vc8wgAuFMcF1uBgU819CSJnxZIhVAvSReVg2EsxEzUPvbMnxueUkviKMkAgy34jZRcE7RDiw80sistWOWveHjfenNYYPqQq2VZd-mYLniMjX7hAjnVWIkkcegPG8C-NDfPabXdiyIL2NWxwFAYtHc68T5KLBOU3p1LEOQKxQbIkxc5vBWtoOSneNqTZeEQ6jCXT1c_-tqilsAhGgmmxP5M7DZVWovj5p-OTDUfPM45vuqH1f9Nuhvr7u40sLj4m6h7BZVbZ4S-Fx7YRBXmnzbTcaHbTiXIHnDilTu0P6iRYhoPeqX9qOelu3B60y_YkTfQd6jv5hWKyTjKU3U1lkRl8O-PQXNbmOmRaVGQpjSh82HZKRwiaIrR4HEQIHoxlPcqAh8H6EAQE1W1wR2dJzpoR-l1woqchbgTuT_YSdpON3WmfThFeQ1hiebWxhMWJ4G7bj1kLdkPttRNH6rqKeqoUd7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
مهدی توتونچی: کاش به جای علیپور، کنعانی به مانیکور می رفت!
🎙
وحید فاضلی مربی پرسپولیس: ناخن های کنعانی را مثبت می‌بینم یعنی او تمرکزش کاملا روی دربی بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105523" target="_blank">📅 00:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105522">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=OAoPXwjtPMCLBA6kdW1LgaqpnHwxAnyS8ORxMt0hY5inOrxeoLWSoxT9xnNlqOHGVcXsEep3pBmwCmlyWsPwsl4SBoXTdK7lesxY1WarONIGDcxv9mQpQoa4IBCqIN_6b5Uzhd8092z-tbwhtazOPDsmIkte9dIpFth76YJ4Bx5OYe4ZQ5Tf6WbNb6SpCJDyiyh9DF_lAxFAaCjxLHrgIFHtNd83x0s-cu-iIQsOHJXAPOCOf6gj3l47orbMMnS7kmPHPcsYTNFZrgsCHPIOn1JLnDYQQv0oT1215yEKCphPb1pDTHqos7-_c8juLzUvmU2QjTiAIR9FO4b5qHS44g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d308caf8de.mp4?token=OAoPXwjtPMCLBA6kdW1LgaqpnHwxAnyS8ORxMt0hY5inOrxeoLWSoxT9xnNlqOHGVcXsEep3pBmwCmlyWsPwsl4SBoXTdK7lesxY1WarONIGDcxv9mQpQoa4IBCqIN_6b5Uzhd8092z-tbwhtazOPDsmIkte9dIpFth76YJ4Bx5OYe4ZQ5Tf6WbNb6SpCJDyiyh9DF_lAxFAaCjxLHrgIFHtNd83x0s-cu-iIQsOHJXAPOCOf6gj3l47orbMMnS7kmPHPcsYTNFZrgsCHPIOn1JLnDYQQv0oT1215yEKCphPb1pDTHqos7-_c8juLzUvmU2QjTiAIR9FO4b5qHS44g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📰
🚨
📊
آنالیز دربی پایتخت توسط محمد تقوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105522" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105520">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N762x70PqEU7vGWGwfEp-GRk1GLqmp_s4SiQyHMGyFhO5CuJal969nKWd1I8D1340twCo8g8Eofsi9AnYPui9sYntCQuh39qsdO9pjWjgB00T_0GPur69qdjAnENiXyf89q0aHhf_97b-Hfj20yuJbLdzj6_-hkqudr9u6_CxRTlBRPh3WBFtm7PF0UlFHQc0xFBJq5hl4kWqRYiAyBP0AO8FQeWh-WWGf57i-fUAahvbukloVkTzEdG-Yd0ngpD2aokiX3sDCLC15Dwmr1YjTPDr2yVtKLtHaNi5cirS1ol-PRDRePYzK6K7bgeyqBMKcNjwW94LWWXUxOgpPcuAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇮🇷
برخلاف شایعه ساعات اخیر، عارف‌‌آقاسی مدافع استقلال دچار هیچگونه مصدومیتی نیست و در بازی با آلومینیوم به میدان خواهد رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/105520" target="_blank">📅 23:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105519">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDSmCoIn7FJlwCx9EKlynMCQ29_HdmrWAUFfBL_EVCRhgHr2fRLkXBVzSvqxsVnruN5tTE-x1prg_eDf2VOAl3BN0PQbfffNZxvj6svRfiWr4Lp_0ea5N_gypAyFCcChVKhzhLmoMVieDrkcBeKdBukEB6IWhBwC4Sd85VUzgk8JW_2lG3Xn2w3APrKx_io_2Bx74EAeMJA9bNZmuGfDKDn-2qSegoPCBAPtMjUpRyvxmFuikMv-NYPZt4YNlhRpAMeRow088SEpJCyibKHvZ-_I3KnCV3tMW3HQ9HZZVEmECLHfFK7Q6_hw_SL-kRZxi2Ayqk0lLLUig8UwvsdchA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🇮🇷
استوری یاسر‌آسانی برای صالح‌حردانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105519" target="_blank">📅 23:36 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105518">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1298395760.mp4?token=V8kTJPR6MCKvAPydgPJETvikzOxZsNuI2kujfOE1KOfYe-i5fCaVxIuVvjuwfWC8u28zzdt7Sq3F6CqyJj29UoDoMOd1msissFsrXWuWeoduMPFYKR6trMoQH9R7BkruSb9OwC7OpRKDz1kp2JK5Z5K10SOrvDbvIVKYhcfdk37h4WEMauBxROsdudhKkbfITz4kuOkaenI37X49AHAWL6tAmqPKdmEIvf6nssnW2N-9Ys8xgVHbFJubojNs7ubUZ8S4e-_Kqj2cmafjvOcloXYFpfUlDySJp9XJaVKLoEe_YFeboa-v6Ata_xVIYXJpkbyOtOcx7L1iTNB4JD0yqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1298395760.mp4?token=V8kTJPR6MCKvAPydgPJETvikzOxZsNuI2kujfOE1KOfYe-i5fCaVxIuVvjuwfWC8u28zzdt7Sq3F6CqyJj29UoDoMOd1msissFsrXWuWeoduMPFYKR6trMoQH9R7BkruSb9OwC7OpRKDz1kp2JK5Z5K10SOrvDbvIVKYhcfdk37h4WEMauBxROsdudhKkbfITz4kuOkaenI37X49AHAWL6tAmqPKdmEIvf6nssnW2N-9Ys8xgVHbFJubojNs7ubUZ8S4e-_Kqj2cmafjvOcloXYFpfUlDySJp9XJaVKLoEe_YFeboa-v6Ata_xVIYXJpkbyOtOcx7L1iTNB4JD0yqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🇮🇷
🇮🇷
آنالیز زوج سمت راست استقلال در دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/105518" target="_blank">📅 22:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105517">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbFKIIDR6-hA5moSfMEyzJn0OoTv0lz3ctObiqe8p97o04PLWIKhPxCZdZcpfg5GoY8qDfQzl0s2EYj7eMjuGa8kuSeMlLjj5GtPEPi_R1omoCREq1jELqMB7T-i0Tclgo4yTTmBA3rqHiho_JxcVpn3h1ZdZp4KtJtD3Ic782-v82dbfCf5pzTLsJ9dN6oNOkNTxTOTquPjmZkbwjTcpw3Zrs492ryScYWKBAseHpuSMCJ8SHhjpbKe9ddlZbt9nMjAcEZBUkzwj5Qe00Q0DEZrEPxHEEsWrZnfJTN2Qco-wtCV7Zgk9AbOMYvb6n3s1c2xr6vzkyR7m0EfCVYu_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
پاری‌سن‌ژرمن قرارداد چند نفر از اعضای تیمش از جمله لوئیز انریکه و ژائو‌نوس را تمدید کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105517" target="_blank">📅 22:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105516">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d0b4fd3a2.mp4?token=JwogUXpU7XYSqGEDqAjEU-WqwtEdiBcsm2hmz_2312hcQjTYz7Una8wXYvSCVTJscjMJmdJRClv6rKe1q0ixuU21GzkHB5aDQ8Mq-UQRRmSydalYAZYLxyuMd2sM8nQnZdtNgponwHJ3bckLIFt_nhLw7I6VWCXDaDvbyFcWIJjUGom-SE1X0Z4X8Z3BlSdoGlS4WdTzBR1SiQ6YZPhYBVZzyE2ERoEXqzE5LZjJMWu1vmrNcTAHlBCEeyxdNd-LtDsGvhj_ulJ6asFw8wUsYiig1cruN8Zka7SPJqxOb1qAB7Q-CuA63V0T-TdSuZtrBKXCjbxLq8PST97spNDu_GtsBRAaesoUl2Fu1JfQLiDv0I4ks_ujGRiJPjSWP9PRy2_MZST5Dg4pLOVnUHFT4vpE4g5llWWzvYKxYDjIuH14DvaMUIzhepLbaqhMJrW0fZibX6dRK9TRmg_4RRHkYTyTdnxuCSkeAn3Fh4F_xih-2cMi77hh4ZYeYJ-pPU-fdGoavyck2hx4KvnA1QVzY8s4OIj6d1GY7Yyn6MayAY1_N195NWWS0H_G2K4XpW7KvIFq-TjQIlJCmzGEAwvyWPPr9WFImV2idKO_qWWXokY1a5Xzp1CE19KCiOab1gDrYvdN91ws2NTbFLfJtPrgoB0B0fvS5Bzfqc2cjopW9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d0b4fd3a2.mp4?token=JwogUXpU7XYSqGEDqAjEU-WqwtEdiBcsm2hmz_2312hcQjTYz7Una8wXYvSCVTJscjMJmdJRClv6rKe1q0ixuU21GzkHB5aDQ8Mq-UQRRmSydalYAZYLxyuMd2sM8nQnZdtNgponwHJ3bckLIFt_nhLw7I6VWCXDaDvbyFcWIJjUGom-SE1X0Z4X8Z3BlSdoGlS4WdTzBR1SiQ6YZPhYBVZzyE2ERoEXqzE5LZjJMWu1vmrNcTAHlBCEeyxdNd-LtDsGvhj_ulJ6asFw8wUsYiig1cruN8Zka7SPJqxOb1qAB7Q-CuA63V0T-TdSuZtrBKXCjbxLq8PST97spNDu_GtsBRAaesoUl2Fu1JfQLiDv0I4ks_ujGRiJPjSWP9PRy2_MZST5Dg4pLOVnUHFT4vpE4g5llWWzvYKxYDjIuH14DvaMUIzhepLbaqhMJrW0fZibX6dRK9TRmg_4RRHkYTyTdnxuCSkeAn3Fh4F_xih-2cMi77hh4ZYeYJ-pPU-fdGoavyck2hx4KvnA1QVzY8s4OIj6d1GY7Yyn6MayAY1_N195NWWS0H_G2K4XpW7KvIFq-TjQIlJCmzGEAwvyWPPr9WFImV2idKO_qWWXokY1a5Xzp1CE19KCiOab1gDrYvdN91ws2NTbFLfJtPrgoB0B0fvS5Bzfqc2cjopW9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
هوشنگ نصیرزاده: هیچ‌کس نمی‌تونه از آسانی شکایت کنه؛ افسوس از این اعتراض‌های آماتور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105516" target="_blank">📅 22:01 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105515">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf94f3a1ca.mp4?token=UN-u6EpTJKDofPs0GGs-euhXMD0g8MTVNfFqA_1ITCFGAPNNgSXfwLKXhj98JxFzPA0OMgPCHFPJcRjhp5FYKdGclnLucGV4Mh6VrKRJjEOtFb6_BuobbfXg-CcjmDAqqD5BvyGqhQaQu-OXt1_2NL3fYvKDw5UaY0Y-xW1SuJDxVZXqJyoc0XbAceMb6MW4gEk9z85GYrxjJoaPE8RWEIn5DD33OatBwkiiWT288__9B6h2dRAplDnQqC9c2kmQLVgBZdlMNVvxzvu3svGKMewJsUDHCoQ5VnU4cZ3pJ3u9BjvOa1_VR9G-9shoYig_WWULSlFAJ6c-pDSt17eccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf94f3a1ca.mp4?token=UN-u6EpTJKDofPs0GGs-euhXMD0g8MTVNfFqA_1ITCFGAPNNgSXfwLKXhj98JxFzPA0OMgPCHFPJcRjhp5FYKdGclnLucGV4Mh6VrKRJjEOtFb6_BuobbfXg-CcjmDAqqD5BvyGqhQaQu-OXt1_2NL3fYvKDw5UaY0Y-xW1SuJDxVZXqJyoc0XbAceMb6MW4gEk9z85GYrxjJoaPE8RWEIn5DD33OatBwkiiWT288__9B6h2dRAplDnQqC9c2kmQLVgBZdlMNVvxzvu3svGKMewJsUDHCoQ5VnU4cZ3pJ3u9BjvOa1_VR9G-9shoYig_WWULSlFAJ6c-pDSt17eccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی محسن خلیلی از حاشیه‌سازی هواداران پرسپولیس درباره اوستون اورونوف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105515" target="_blank">📅 21:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105514">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qG50MPNW_iij_6raJWBSospR47zuCNPb9gxWKf3vIlQSz-mYh3UiqEqpTcK1fhT11kfMeizajw3gpQzT3875ypXANX66Ws_gqYRhkfsjmNh2M3biik1aNVo6ca2o-QFC0IMXckDgdrBHlSt_Qee4OK9UBmpvUF1LlZAuUBNK-0PInLxolEYVZSn7QDVaM9mJViQLAGTDpWdfImYn4bUkE7aNm6m31OhXJMQc_qNrYc48B843DRVdQ1SlvCgY5TUhgcEdHIyqvNQlWlBDywJKqozwvStBHNYxyKZjD_DfUbc6IoTKLSykpbwMyjqCvi7skJsP9awph0dqLD6UNFtNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
ترکیب رئال‌مادرید مقابل بتیس؛ ۲۲:۳۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105514" target="_blank">📅 21:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105513">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b668e9a164.mp4?token=ZA9h6-y2xyUFCnThrv69N-A8VBAgE0_Ha-SnKDEPXr7EzXPaWkGL_UwH0JnLrx-l-tHBX2rjImYQSZWj9bniYxJLSlWs7DuYF-i32WmxGcJzInikmrsI16eLb1GLRZUZ3kRzTN57PbSJVE7bQ5Qxgn1iDFCouRLG4nE_Yv0etPiZXckA8imFc6aHNCWaymn3gPcBVN4kKtz1rgOr9e9vYfElKGBObR0TcEJ_xtdZc-DzQhk44Nvid2ODQIs4h7trCCrxufnoXfZLYbyEKLCyx9t2JmF1NXNhOz-28TyyYjmiMLtjuE3vXu224MPO9p5PTWlv_zC62JUNIH-pt6qQxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b668e9a164.mp4?token=ZA9h6-y2xyUFCnThrv69N-A8VBAgE0_Ha-SnKDEPXr7EzXPaWkGL_UwH0JnLrx-l-tHBX2rjImYQSZWj9bniYxJLSlWs7DuYF-i32WmxGcJzInikmrsI16eLb1GLRZUZ3kRzTN57PbSJVE7bQ5Qxgn1iDFCouRLG4nE_Yv0etPiZXckA8imFc6aHNCWaymn3gPcBVN4kKtz1rgOr9e9vYfElKGBObR0TcEJ_xtdZc-DzQhk44Nvid2ODQIs4h7trCCrxufnoXfZLYbyEKLCyx9t2JmF1NXNhOz-28TyyYjmiMLtjuE3vXu224MPO9p5PTWlv_zC62JUNIH-pt6qQxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پایان چالش
🎀
🤣
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105513" target="_blank">📅 21:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105512">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=dNXsg0WgSuBcJhm1M6UPHoWqdZ9FiEIc5F78eo0NE_xYpp9IGGxgF8IMrgkEogKNLJxLT1aMYeCE0NKCSEQlHHRRV9nmW9Qwit9ODs-NYblmKDTujNOdLkCKR3gVyTyLrKvJ1rTJhbsk_9QIcsAmGKWk5XS7DbAdvKdvUjHPCHVzZo4DRgpOTOOEAZvVwOJLF92ZbWGP-zJgWnvLJxv1d4R5vG3V-E4BuOinUCYleuyiSciF3PgohA7c08WUrlEyma0y9y5e-f099T_gOPjezZLhNLQvWOA_5cHZxuupiEk1P6q-QejMoJHIm0HRKGZHXxWAyBGVefGOzCK4HF9LtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0ab284a6.mp4?token=dNXsg0WgSuBcJhm1M6UPHoWqdZ9FiEIc5F78eo0NE_xYpp9IGGxgF8IMrgkEogKNLJxLT1aMYeCE0NKCSEQlHHRRV9nmW9Qwit9ODs-NYblmKDTujNOdLkCKR3gVyTyLrKvJ1rTJhbsk_9QIcsAmGKWk5XS7DbAdvKdvUjHPCHVzZo4DRgpOTOOEAZvVwOJLF92ZbWGP-zJgWnvLJxv1d4R5vG3V-E4BuOinUCYleuyiSciF3PgohA7c08WUrlEyma0y9y5e-f099T_gOPjezZLhNLQvWOA_5cHZxuupiEk1P6q-QejMoJHIm0HRKGZHXxWAyBGVefGOzCK4HF9LtjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
🇮🇷
یاسر همرنگ داور سابق فوتبال:
❌
با یک عکس نمی‌توان راجع به دادن کارت قرمز قضاوت کرد. تنها ایراد وارده به بنیادی‌فر چک نکردن ناخن بازیکن است. داور VAR زمانی داور را می‌تواند صدا کند که یک صحنه‌ای از عمل «وحشیانه» بازیکن موجود باشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/105512" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105511">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=PYGL8I_OoSVGSgPIF1irNRRImoIB_4dfaQR46815Vkx-feJ7LXGgSku-ldzJR5wbyPPt_heWHQlo6RRlaEGy4nOQPnfkqIwYlGLahAfl-qZVi2XQCJua9CypHg9sjRotRn8Ej2p44ZgaQeOUBHDHYYv1yHbk0PTOoGc6NFAYjUdkhVkRB7CtQ9peoSYKOEzY2UjIWQ3L12BS9XcfbIAW9jy3gH71TE8LPKZhdAS7FXn4vdzqDsNOopyGbHKD8lonTym_9MjOajT752oLXdDxxf1VJfyZmfQ0SpRvKX9JJHi_0KTHu7ajf4aCLO23eET67dzHzje8lp4RNPmN7NnBSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae761380ef.mp4?token=PYGL8I_OoSVGSgPIF1irNRRImoIB_4dfaQR46815Vkx-feJ7LXGgSku-ldzJR5wbyPPt_heWHQlo6RRlaEGy4nOQPnfkqIwYlGLahAfl-qZVi2XQCJua9CypHg9sjRotRn8Ej2p44ZgaQeOUBHDHYYv1yHbk0PTOoGc6NFAYjUdkhVkRB7CtQ9peoSYKOEzY2UjIWQ3L12BS9XcfbIAW9jy3gH71TE8LPKZhdAS7FXn4vdzqDsNOopyGbHKD8lonTym_9MjOajT752oLXdDxxf1VJfyZmfQ0SpRvKX9JJHi_0KTHu7ajf4aCLO23eET67dzHzje8lp4RNPmN7NnBSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😆
‼️
⚠️
جلالی: هنوز هم سر حرفم هستم؛ قلعه‌نویی در اروپا بود، از مورینیو بهتر می شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105511" target="_blank">📅 20:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105510">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=g51uNTprlAVOmjN-03cmFGD-sarfmhifHVAFJLhmjHnGpHO7vRo4o_4TJSM8LlOrk7P2l7WdLP1p8AlKLXb2rDwNNySt_4JPxR2PBehRjh5Kn1dlF6q29sEbHAj_3LNse8MK_G27udO4b9jnWsHSDTERXJCX7bwJwGv1jmsTXFgL3juZm2IJFjBA8mnvxmV7RdeLJP3p74kMkf3Nlaoxcg1zsJoLDNWcX-Gg5ULyjnnlJ9YsrMFvTnFUJrFeOKS5ghzlZ3r_cxuAsS5p-hPefLQ-AsuK4HXC0L5IN94MBynaDslVRQfXMx96gbTezWRi6O_VZjSKvUhZC4ivuJGqkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e88a7236c.mp4?token=g51uNTprlAVOmjN-03cmFGD-sarfmhifHVAFJLhmjHnGpHO7vRo4o_4TJSM8LlOrk7P2l7WdLP1p8AlKLXb2rDwNNySt_4JPxR2PBehRjh5Kn1dlF6q29sEbHAj_3LNse8MK_G27udO4b9jnWsHSDTERXJCX7bwJwGv1jmsTXFgL3juZm2IJFjBA8mnvxmV7RdeLJP3p74kMkf3Nlaoxcg1zsJoLDNWcX-Gg5ULyjnnlJ9YsrMFvTnFUJrFeOKS5ghzlZ3r_cxuAsS5p-hPefLQ-AsuK4HXC0L5IN94MBynaDslVRQfXMx96gbTezWRi6O_VZjSKvUhZC4ivuJGqkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
نصیرزاده مدیرعامل سابق تراکتور: بیرانوند در صورت سربازی باید به لیگ یک برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105510" target="_blank">📅 19:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105509">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=Ap4ttqMQyijZIUZPtCvgKIrJgeULtfjgeweU_JBAE9Zl2gW05bs7hWYKqvIRIaiOqOaXd99BBJ3G3ltXBa-Ou_yFRFDlLvB7YkBOR6Byo2QE1G0IOIikdn4MumYjEavgsSV6QXDTP3l8VUQCUOegIDGU3jh4QlDOBf8Ewe0A-I_29MRYwVAW4Mlc4q1zgoDEIcH0ZmmniFm74f-N-AJKDk03ukysxwePLSshAFGL_26GQcf8kVAqE1gTvdLQEUIYPzJqlF08a9jL_AoJusB0wfMu_P3C-N16GCCmfM-IWZQ6kc3hw3abWDnzpl8W-2POqjI9tXQswKMt9Exd9J4mZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2862cc83d9.mp4?token=Ap4ttqMQyijZIUZPtCvgKIrJgeULtfjgeweU_JBAE9Zl2gW05bs7hWYKqvIRIaiOqOaXd99BBJ3G3ltXBa-Ou_yFRFDlLvB7YkBOR6Byo2QE1G0IOIikdn4MumYjEavgsSV6QXDTP3l8VUQCUOegIDGU3jh4QlDOBf8Ewe0A-I_29MRYwVAW4Mlc4q1zgoDEIcH0ZmmniFm74f-N-AJKDk03ukysxwePLSshAFGL_26GQcf8kVAqE1gTvdLQEUIYPzJqlF08a9jL_AoJusB0wfMu_P3C-N16GCCmfM-IWZQ6kc3hw3abWDnzpl8W-2POqjI9tXQswKMt9Exd9J4mZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🇮🇷
🇮🇷
آنالیز گل‌های دربی اخیر پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105509" target="_blank">📅 19:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105508">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">‼️
⚠️
رضا قیطاسی تو مسابقات طناب‌کشی بازی‌های جهانی عشایری موفق به کسب مدال نشد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105508" target="_blank">📅 18:35 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105507">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=i5aIFZ9_wYpzcuuon4Vh61Awk_nSh5-zTNlx00l63T7SKHztiyiSOd2flu2yONQAUoegM0ReE2fO5izEDJZQHKmbJXSx7iuAplsGOBUApFyDaza2viCo6La6gkDWgXmz12iCmiUxY3L87YcG6c3-N5Hf2pxS2zNuF0HdXRzRKDdnGubKcoy0ZX0DgfrPLTHfih-V5TlVulBHANQyPEeXNxR4vrfvqvXVbpG60LogEPBot1t97LnbfVXzvOZ-qae2GbOLoTtfJ0EsWUwmFG1EIHQrRG1x2r_5v5_Bwgavn4l2utYRUBXOaetlVUnnM1_Klqrt-nyIuAGCtA7sq_edT3IhQniV1o3p6gGiER8yS4vyzS6uSXI2sDzL-sOVC6ywUmzkGV9xcdW4SWq6ecazP-UsljsWu3r1Yc5cAYHyn9ispJxBveh167Y6HBGtUMzx1KN8sWEgpVCrjD3hDoVohhcWsyq_n4EmZACjaEeBTuSa_mzr6OzLoSsKCOzlKvuigZ1UHEGFJlWQXygjJKXMQj9kDl1hD6iqBOlHL-j1VAlfVANYiT-vFyGHo6XxXomQBwQKf-GJJDHWm0w5vBZBk3-rzvPwycle6JVeUMLvqeUGlEs4T8qCD40jVatyYJklOxyieoo-HkX95mWN-5RD7gM7G9KGZMAuy9xNbrRh-ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33404ffbf8.mp4?token=i5aIFZ9_wYpzcuuon4Vh61Awk_nSh5-zTNlx00l63T7SKHztiyiSOd2flu2yONQAUoegM0ReE2fO5izEDJZQHKmbJXSx7iuAplsGOBUApFyDaza2viCo6La6gkDWgXmz12iCmiUxY3L87YcG6c3-N5Hf2pxS2zNuF0HdXRzRKDdnGubKcoy0ZX0DgfrPLTHfih-V5TlVulBHANQyPEeXNxR4vrfvqvXVbpG60LogEPBot1t97LnbfVXzvOZ-qae2GbOLoTtfJ0EsWUwmFG1EIHQrRG1x2r_5v5_Bwgavn4l2utYRUBXOaetlVUnnM1_Klqrt-nyIuAGCtA7sq_edT3IhQniV1o3p6gGiER8yS4vyzS6uSXI2sDzL-sOVC6ywUmzkGV9xcdW4SWq6ecazP-UsljsWu3r1Yc5cAYHyn9ispJxBveh167Y6HBGtUMzx1KN8sWEgpVCrjD3hDoVohhcWsyq_n4EmZACjaEeBTuSa_mzr6OzLoSsKCOzlKvuigZ1UHEGFJlWQXygjJKXMQj9kDl1hD6iqBOlHL-j1VAlfVANYiT-vFyGHo6XxXomQBwQKf-GJJDHWm0w5vBZBk3-rzvPwycle6JVeUMLvqeUGlEs4T8qCD40jVatyYJklOxyieoo-HkX95mWN-5RD7gM7G9KGZMAuy9xNbrRh-ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
تلاش‌جالب یک پدر ایرانی برای گزارش دربی برای پسر روشن‌دلش که حسابی دیدنیه
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/105507" target="_blank">📅 18:10 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105506">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b357d488.mp4?token=JFEL5fjv6QFJAQzW3tN4sdcZScXNJ6Jy5zPzKTa311vvdtzZSA6p0tFXX5cgj-Fk9Nh5xEQIcpPHDSd8Dp6GiSI9X8RTF-6nMCw0rky6uOuNO18OmIzyHOIaeHu3ims6mHURIidtw-H6Hwm5cXwmXRn_kVzhVxNQ7v9hd8FD-mUty1PQOF3goBk8gp4hOCc8rsV4oWFDrx7Z6VwpbP2_ItEzO18IQucnRsYDhstaPDoM5S9HgireDnuOl9FK9mUPne-ULhL-KbD-CBOnp9s-OtjhK5Df6hFkCb0l6pUOZw4zy_llZb7LgF-tV92SKGCRlYNJ4sEZdNANSywCH7IwLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b357d488.mp4?token=JFEL5fjv6QFJAQzW3tN4sdcZScXNJ6Jy5zPzKTa311vvdtzZSA6p0tFXX5cgj-Fk9Nh5xEQIcpPHDSd8Dp6GiSI9X8RTF-6nMCw0rky6uOuNO18OmIzyHOIaeHu3ims6mHURIidtw-H6Hwm5cXwmXRn_kVzhVxNQ7v9hd8FD-mUty1PQOF3goBk8gp4hOCc8rsV4oWFDrx7Z6VwpbP2_ItEzO18IQucnRsYDhstaPDoM5S9HgireDnuOl9FK9mUPne-ULhL-KbD-CBOnp9s-OtjhK5Df6hFkCb0l6pUOZw4zy_llZb7LgF-tV92SKGCRlYNJ4sEZdNANSywCH7IwLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
افشاگری محمود فکری: خیلی از دربی‌ها رو از بالا دستور میدادن مساوی بشه و ممکنه هنوز اینکار رو بکنن
❌
نتیجه دربی رو خیلی از پشت پرده کنترل میکنن، خودم هم شاهدش بودم بارها و میدیدم به مربی ها میگفتن بازی رو مساوی تموم کنید یا به داور ها گوشزد میکردن اگه یک تیم گل زد جوری بچینید تیم مقابل هم گل بزنه یا بهش میگفتن اگه مساوی بود ریتم بازی رو بگیر تا با همین نتیجه تموم بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105506" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105505">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105505" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105505" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105504">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F8mc4pGc5CGshmR9ilce6-cywg4GXuQorftm5cExNVoIEYbYxbsSFoQDmKZFXaqcSGCjD_OrYnlq7Ae3ICho07QA5648w7TCCACeR3JF2MWfKl1GM3SOBK0_DlDtAt3DNQeApFdZUtxpiqhms5-D7xeVLracwJZ44C3YTezqpkFNhW_pd4AfFmvLo244kgD0szM9_iCyC-TdLQxYy5x9-1zfB-6SJE0gndkSa8SbWMB0gXu8Vf2XFoeRck5hCZFQkEntHP_qMbh0nfX_s9v16MMDcWsLEU1ZZ_ebCKnTqh6MvhLWwJ0qv4llmFqTE-ohDjc7g9rRF5wifD4OurVvGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب
⚽️
پاری‌سن‌ژرمن
🆚
موناکو
⚽️
را در سایت بین‌المللی
TrexBet
پیش بینی کنید.
📊
مونامو ۲ برد | ۱ تساوی | ۲ شکست | ۹ گل زده
پاریس ۲ برد | ۱ تساوی | ۲ شکست | ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105504" target="_blank">📅 18:04 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105503">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEfgjyBVKemNDveuJ3WxgTtluzzGP-g6zizqn5mH88YcjwpMjT5i9WNsdHAg5_jG4wx0q7zfUJLAoVoFGpjrgXdfdZkuT0PCbSt5sLObRd2y5nyUiSbkarCRT-AP1wnX9FeSRlZVYoCUL99F8funHRPFA2hN5WJ8FVTudEusHmv89nkG4mdEFrrKrfYh49Q4YCrxqslgkRmfx3ytLT_YK_eyPdllpO5AU9n_mg_Si8o3LpRsxyigjT1bJuMIu6X2lQHzKFctJcyq7ZcKtaPe46qb9Aynfjbik8jg9LEjNABoojQHxL2vMMN5v_fxBIC_H29AIPa9ADJyCzFPXWoFwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
💥
🇮🇷
هوادار استقلال در حاشیه بازی دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105503" target="_blank">📅 17:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105502">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=bI28t2a0Bh4nRwEL-0pi9LvVu2I43_BextT0GRdMk7nTMDxARJ50HOyGBjBUhQCEirxf3muHTBHMlCE0lU5tHDp-MjFoIvu0D23Fh7DSIoNMWc75ZY_qebq37dXtDVwubNPJoE8E2irsKYdf-GQlrlCZbhqTz4liPeEpjn7a5RbBf7HLMvyRN9SaxsNAPKfMyvcl03RH1-kAMl7NW4Ydg6JvHT0Z1SOm4-Q-VNbu40ZXvr89Ck7FdMBufOsKw_bnRiUrohmIO5867BtbzIWuz776iXT--2CyIqsckPq6_QLKIQMNgeDEAj70znX__r2KOx5qqNaaN4msMgis2F3dvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea454a991.mp4?token=bI28t2a0Bh4nRwEL-0pi9LvVu2I43_BextT0GRdMk7nTMDxARJ50HOyGBjBUhQCEirxf3muHTBHMlCE0lU5tHDp-MjFoIvu0D23Fh7DSIoNMWc75ZY_qebq37dXtDVwubNPJoE8E2irsKYdf-GQlrlCZbhqTz4liPeEpjn7a5RbBf7HLMvyRN9SaxsNAPKfMyvcl03RH1-kAMl7NW4Ydg6JvHT0Z1SOm4-Q-VNbu40ZXvr89Ck7FdMBufOsKw_bnRiUrohmIO5867BtbzIWuz776iXT--2CyIqsckPq6_QLKIQMNgeDEAj70znX__r2KOx5qqNaaN4msMgis2F3dvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚔️
🇮🇷
🇮🇷
نبرد جالب و دیدنی تیکدری و صالح حردانی در حاشیه دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/105502" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105501">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=Y5-m9TZZbFUIB_pMJzrpx0skt3W8AicGu898zBRA2aOAFtLhktKOD2C18pxTYoJrGrNEovd2KTi7aonbOqaF5OEC7CuhhYWjyg3g0NqdQ0AQjfr5FIkeabQx62h5CTu7fvQ9BXRHemvfBhRXlgb6zkb6lQY8ICFTteuBpu3NvnoUY8eNLmC3jw95Q6WM2uDJ9PC_meOCqxqKotutMNSbnS50uVl2_7qLaqmUXqTuX5cscmHIdC48f8ny1WfEs9vXjoddC8r3dgYNZSEmXv5RMvGrJ5pV2RbCSVhbZOjJ8cXaKb-uHtcSqhZcHDCgc09o9uWoEQmLwqsBCRU5DsnLEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d10152fc52.mp4?token=Y5-m9TZZbFUIB_pMJzrpx0skt3W8AicGu898zBRA2aOAFtLhktKOD2C18pxTYoJrGrNEovd2KTi7aonbOqaF5OEC7CuhhYWjyg3g0NqdQ0AQjfr5FIkeabQx62h5CTu7fvQ9BXRHemvfBhRXlgb6zkb6lQY8ICFTteuBpu3NvnoUY8eNLmC3jw95Q6WM2uDJ9PC_meOCqxqKotutMNSbnS50uVl2_7qLaqmUXqTuX5cscmHIdC48f8ny1WfEs9vXjoddC8r3dgYNZSEmXv5RMvGrJ5pV2RbCSVhbZOjJ8cXaKb-uHtcSqhZcHDCgc09o9uWoEQmLwqsBCRU5DsnLEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🎙
🇮🇷
علی‌تاجرنیا: خودم پیش قدم میشم و‌ مشکل بین صالح و اقا سهراب رو حل میکنم. چیز خاصی نیست. هر تصمیمی سهراب بگیره باید احترام بزاریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105501" target="_blank">📅 17:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105500">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=Mp159i65RHB3-1BxQMZtOCpzaZo5qyHb4Fw0IQXFDj6rlTCt7Vhq0MQEcFJM1qOwUVuvsRHykrqyCUejqYGDmSTEzUOvJmM50cprxdM1Xc5XRZXuUvbp7AejSaZllfK1iHAMwNmRYtOdWW0UkDSpEKkPWMGvE08qpSPFoSWnt4SL9eoDZYnwSajKNvrgupk-S67uMqlYuUYqwdmqaSukDnKDWXX6iLI-D1QALomNLooy8YilCBBSfPNE9jWlgJH-oB8Pytc_LQLY0sE6D_kZGaEU5gy5jk8grmjQ-JWhoPZ3P-Es6U3C2vwDwsHDhahSzeJ5nvqQDVJuFeR5rH_OJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89dcbb7663.mp4?token=Mp159i65RHB3-1BxQMZtOCpzaZo5qyHb4Fw0IQXFDj6rlTCt7Vhq0MQEcFJM1qOwUVuvsRHykrqyCUejqYGDmSTEzUOvJmM50cprxdM1Xc5XRZXuUvbp7AejSaZllfK1iHAMwNmRYtOdWW0UkDSpEKkPWMGvE08qpSPFoSWnt4SL9eoDZYnwSajKNvrgupk-S67uMqlYuUYqwdmqaSukDnKDWXX6iLI-D1QALomNLooy8YilCBBSfPNE9jWlgJH-oB8Pytc_LQLY0sE6D_kZGaEU5gy5jk8grmjQ-JWhoPZ3P-Es6U3C2vwDwsHDhahSzeJ5nvqQDVJuFeR5rH_OJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
💙
بیژن طاهری سرپرست استقلال: بعد از 23 شهریور که بازی آسیایی را برگزار کردیم اگر سرمربی ما صلاح بداند بازیکنانمان را به تیم امید می دهیم/ در اردوی قبل پرسپولیس به تیم امید بازیکن نداد اما محرومش نکردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105500" target="_blank">📅 16:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105499">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🇮🇷
❌
صالح‌حردانی بدلیل انجام برخی کارهای بی‌انضباطی خصوصا در بازی دربی، از سوی سهراب بختیاری‌زاده تا اطلاع ثانوی از حضور در تمرینات منع شده و احتمالا بازی روز یکشنبه مقابل آلومینیوم اراک غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105499" target="_blank">📅 16:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105498">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLHXljjdrruVSeRoUw-qgPBJJvfOCR3lLA-trKxOUNkdAcjFEoysQE5ae4tCTZIFlaUkTWI0QfwaZ0c_FMm_TU8E3Hk-nTIjVXjpDG2LLo1pxfWvDM_X-D3RH7U7wUFYbQJ7cuzVz2OmzMxmKaF8pvZMKsb4lMVgA_SKxQb4mcFAJzJZmSD6KUtaT3CuIhstvFgIvdzeQfbt8BL6y3iUPtW3dYCT5ShvQI7nKkwNo8SO19YM1WdA642DEufP1WBri4MPBVlmj-RhfmqFkdewQwoK7CRwnHhmAxqYKojR4Q0zD6BVahf4I9Ewwz45zvgIfRCtQ_spNwtoHWes59bYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105498" target="_blank">📅 16:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105497">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2WRbudnnlZoH_PgQ8MEfZFl8YwWn4Lz4qeQuwfviPWnbiBQu8kIW4D7f3ZmQa39Z39MHOHEqpb5DQbpfGxcTfD62Zn4RRbTMcgQLIydRMcC9Etj1cITDv1qEnuzRvockvkhPLxpN4Pmxw2PByazyBlcrIL0rj9QpGtpOctNyoPjttRnKAD7Z-CIH-b6eP3NE6hkd3quEObH8KvmYk2adouw3ky2kBvZVy4iu2MgiAKWNF8bOQikg9lNwqANM2pNwfR9cGtgZn4WqB8Og4tvAXzKcP0bDVHU8bcFPlv7A4ep1ev2VDidUJizVjLUWhQFPeviT0-fsxYgsXOAAobHew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
ترکیب منتخب بازیکنان بدون‌تیم؛ چقدر ستاره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105497" target="_blank">📅 16:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105496">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👀
⁉️
🏆
توپ‌طلا رو باید بدن کوارتسخلیا یا نه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/105496" target="_blank">📅 15:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105495">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=EZBpVYLOf7UeeFKskMgo9oPRsFF4LoLA5mkqjfVM3tB-4MFNYHvQpxGc4Ug7Y2MLwu5J-O5cus_Uc5YLrN2_WOPeTSfDDTDrouLVwQmHDy-B4QM1Zsajpj6uOJNBwbukiQpPCJVDLfbphfI8IJDtqb3CC-sZVHTsCHBoUcJGlNoOLHVMFPAOkFVfPAOHty_bVowWxnkThw8fZfaXDlY8J4JMIeCX9tAHe-CX9cRT2zyXgm8g3hpwSde9Nnl5FePjaJrjUbFvSxJZG9rCbA0fpb9iCQgNkaCvRyDQczU_N2y1D453xwKK1sgR4zvdT3NzqTOMU5ASkh_RnKj2S5jyH1bqijKN7YuFxMQ_0-_s9hAADayHQfJ1gUoDfjkvLk-7NFyOmWa2mT5O8NIr8xTC9AWqMthhSCSe7J1LC_mgved5pwSR1wpryFYSLWu7Fv_iwfWYC4X5-Me5OH14aw9RJiWb_FQvOiEYnn6CHQmH-LGHh1JBF8UvQVOLF_Ko8nmZzWxVY1k34WVvJHkzoT7HOiSVjCsnJBCSkjdPS6LXpGstYdNSqzsZ1wZzjcjNqSjQ62HnYKLeCG5k-kU-QIbtGuv-Mp3tahOg1Yg_HRrgK_KJLJoOEIlmkWesk47cT7Xz1wzcTTrVHKeviDJm38C4Qtw4Jecah82acHCk1YF8_ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61c1e785e5.mp4?token=EZBpVYLOf7UeeFKskMgo9oPRsFF4LoLA5mkqjfVM3tB-4MFNYHvQpxGc4Ug7Y2MLwu5J-O5cus_Uc5YLrN2_WOPeTSfDDTDrouLVwQmHDy-B4QM1Zsajpj6uOJNBwbukiQpPCJVDLfbphfI8IJDtqb3CC-sZVHTsCHBoUcJGlNoOLHVMFPAOkFVfPAOHty_bVowWxnkThw8fZfaXDlY8J4JMIeCX9tAHe-CX9cRT2zyXgm8g3hpwSde9Nnl5FePjaJrjUbFvSxJZG9rCbA0fpb9iCQgNkaCvRyDQczU_N2y1D453xwKK1sgR4zvdT3NzqTOMU5ASkh_RnKj2S5jyH1bqijKN7YuFxMQ_0-_s9hAADayHQfJ1gUoDfjkvLk-7NFyOmWa2mT5O8NIr8xTC9AWqMthhSCSe7J1LC_mgved5pwSR1wpryFYSLWu7Fv_iwfWYC4X5-Me5OH14aw9RJiWb_FQvOiEYnn6CHQmH-LGHh1JBF8UvQVOLF_Ko8nmZzWxVY1k34WVvJHkzoT7HOiSVjCsnJBCSkjdPS6LXpGstYdNSqzsZ1wZzjcjNqSjQ62HnYKLeCG5k-kU-QIbtGuv-Mp3tahOg1Yg_HRrgK_KJLJoOEIlmkWesk47cT7Xz1wzcTTrVHKeviDJm38C4Qtw4Jecah82acHCk1YF8_ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👍
همسر رشید مظاهری: شوهرم قبل از انتشار آن استوری خود برای من فرستاد و گفت که اگر حتی روزی به اعدام و زندان محکوم شوم، فدای یک تار موی ملت چون همین افراد من را معروف کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/105495" target="_blank">📅 15:15 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105494">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=aQQ92gDrmxEYPRs_p9pZ6hwvCPXeOdZdDnE5gGsTe_R3xXB8vgGHNvUqHN3FaK_ikfe5jjwjVIKEzBPRg_a-MQkTpto8kateydURtK18hqG74rNhA2-NdXUpdlWyzwAsY5ljqJ_K5N1NYQhprXT7ByvFXFCITC7DRNFiR35VTiRqBVtiYpvOs1fZjps8FZj0H1hbNSAxiU5XBc680dm1MmmrRqepsXBLm4RqMXpa7DdNXDleE5su-pzpmAh0tPgwQYf0MtSbhE-IvaP0wgeSX6AWLOzb4euUaT5o2xp1WHpdobd8ra4J_yhOayec1Eiry5bpv069FRcZ3ntk1o5zCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de11aaaa44.mp4?token=aQQ92gDrmxEYPRs_p9pZ6hwvCPXeOdZdDnE5gGsTe_R3xXB8vgGHNvUqHN3FaK_ikfe5jjwjVIKEzBPRg_a-MQkTpto8kateydURtK18hqG74rNhA2-NdXUpdlWyzwAsY5ljqJ_K5N1NYQhprXT7ByvFXFCITC7DRNFiR35VTiRqBVtiYpvOs1fZjps8FZj0H1hbNSAxiU5XBc680dm1MmmrRqepsXBLm4RqMXpa7DdNXDleE5su-pzpmAh0tPgwQYf0MtSbhE-IvaP0wgeSX6AWLOzb4euUaT5o2xp1WHpdobd8ra4J_yhOayec1Eiry5bpv069FRcZ3ntk1o5zCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
از یک دربی تا دربی بعدی...
💵
دلار: +۱۰۰,۰۰۰ تومان افزایش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105494" target="_blank">📅 14:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105493">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=KExyTQ7Asf307os30O2jl2np3OuHF3XcJj9apwsOfvjk0c0MpiYJeTT9V3D7wxjy23nuw5riJ7wFqYFOVRl83Mm9tL991MIB7Lz_hVjqdEpq9kmmfHSMF-GyXeZtzjRqS4m1Zavg5NhciTve-8o_CcPvfSmmjKAeEvN_ol7qsed1JPicl_ZKtyvuufsTx8mYX7nnVCBD2q1sZVy-xY5f0eNJcs5jh6xZBn7yj4-26MpxXjlPmAVA2FrRwXWmqloe8kpmrNUqGiuZjs_E3HdrITiEbwPRLsIwF3nx0w7JGm2MmTZHwJnov4n-WBRPOjfGUF7On4gg_twZeYh89vwuAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a3572f3e6.mp4?token=KExyTQ7Asf307os30O2jl2np3OuHF3XcJj9apwsOfvjk0c0MpiYJeTT9V3D7wxjy23nuw5riJ7wFqYFOVRl83Mm9tL991MIB7Lz_hVjqdEpq9kmmfHSMF-GyXeZtzjRqS4m1Zavg5NhciTve-8o_CcPvfSmmjKAeEvN_ol7qsed1JPicl_ZKtyvuufsTx8mYX7nnVCBD2q1sZVy-xY5f0eNJcs5jh6xZBn7yj4-26MpxXjlPmAVA2FrRwXWmqloe8kpmrNUqGiuZjs_E3HdrITiEbwPRLsIwF3nx0w7JGm2MmTZHwJnov4n-WBRPOjfGUF7On4gg_twZeYh89vwuAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی فوتبال به هیچ‌جای زندگیت نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/105493" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105492">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=TzF-qmOFGKEOyW0DeD3yHME6STPnUVADGQi0bATCMxvQBNa7RQQlaV74zHYzjD5I4UKiFERR7kdq9raX7byGDWFac8tvZ12XJUl7DwxvTCtAqv8izN4NuJmFCKppFSDq0XBw7HWqvHZjtm1TuMXHUs2PRspsJAIm8lSeTlAs-41bk34catht9pBZJ_pS67IDbVkxJ4kC0GksZ8Y1OMDiNOCc-31Ch-BlCaBIgz0FA1EcwL-RmlvBlPa5EIFrx1oZsqFrDs4v11zqAEltE6x8A714nz6EtP1iESJhaBMmUCQZmW09eyS8rk-zQh_ozWKEycJVL-n3pcYgAzQo-Gyf7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0801904cfa.mp4?token=TzF-qmOFGKEOyW0DeD3yHME6STPnUVADGQi0bATCMxvQBNa7RQQlaV74zHYzjD5I4UKiFERR7kdq9raX7byGDWFac8tvZ12XJUl7DwxvTCtAqv8izN4NuJmFCKppFSDq0XBw7HWqvHZjtm1TuMXHUs2PRspsJAIm8lSeTlAs-41bk34catht9pBZJ_pS67IDbVkxJ4kC0GksZ8Y1OMDiNOCc-31Ch-BlCaBIgz0FA1EcwL-RmlvBlPa5EIFrx1oZsqFrDs4v11zqAEltE6x8A714nz6EtP1iESJhaBMmUCQZmW09eyS8rk-zQh_ozWKEycJVL-n3pcYgAzQo-Gyf7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وارث شماره ۱۰ آرژانتین که‌ خواهد بود؟
🇦🇷
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105492" target="_blank">📅 14:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105491">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/878e055f11.mp4?token=d7TIbCYf-sGEsGpm7ksJp25QMPkFsTwwT7tBeTWZOYYIvU8X5tNEzryCco3DZUoYdB0ET3NPuntGfaji7pu6zd9_-iTXGulSMbJECD0QDnI6fEcPokINNRGvZRkP15lkPnGsr1D5xj9rqkcEXhSw6tJFETiv9yWoLcjdpm4PqoBYxGGP9--RjCAqobcxm-PCZkLY7-xEbEsAgqAAMrwL6KtKwhZXBM_l9skMql5tnxNfWkjhYr6kX94ukpHeUCz-C3Nn82XBEX2uqEhjNzhNz706wO17JUXz9sfQPwRf3RLXUkEeYpnez_SPxQXGpvIi_5EWatTzijJYcF2bLO0A9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/878e055f11.mp4?token=d7TIbCYf-sGEsGpm7ksJp25QMPkFsTwwT7tBeTWZOYYIvU8X5tNEzryCco3DZUoYdB0ET3NPuntGfaji7pu6zd9_-iTXGulSMbJECD0QDnI6fEcPokINNRGvZRkP15lkPnGsr1D5xj9rqkcEXhSw6tJFETiv9yWoLcjdpm4PqoBYxGGP9--RjCAqobcxm-PCZkLY7-xEbEsAgqAAMrwL6KtKwhZXBM_l9skMql5tnxNfWkjhYr6kX94ukpHeUCz-C3Nn82XBEX2uqEhjNzhNz706wO17JUXz9sfQPwRf3RLXUkEeYpnez_SPxQXGpvIi_5EWatTzijJYcF2bLO0A9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤯
برند Dyson یه مسواک ۵۰۰ دلاری ساخته که دوربین داره! با AI بین دندونا رو می‌بینه و خودش دقیقاً همون‌جا دهان‌شویه می‌پاشه، و تصویر زنده داخل دهنتونم روی گوشی نشون می‌ده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105491" target="_blank">📅 14:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105490">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آنالیز جذاب و دیدنی از پلن‌های مختلف استقلال و پرسپولیس در دربی اخیر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105490" target="_blank">📅 13:34 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105489">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105489" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105489" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105488">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6DV8Fc4BqtXETeDZOXtlrVKsOKu8zCRpxGITNn8HwcsQ-cORVBYnrJhI0jHKyrzXtnMWpb5Da_bt9pxt95gD3xoUDJ0IrS0_GVPQICq82wwoCTfPeiHoXvZrz_LiHyyBly9N9JpGA2jYQhZVfTUCdI49TyiQEKTJh6QJXWa8imvYLgvmHlijIhRtZnO-pSODayqF8PGfKSGfdFk5AYyvDG40S5557ejxxwHQoQznYPfDR963EvntrwcStslyrUtAEBCrZbvSdQ81kO41kehIlFqjCx9ankJCDKdwLzezLHBiMKtu6zfMtT9YMdUH91oRkDjkx0G2-LZ5-2nR3Sq2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
بازی جذاب رئال بتیس
🆚
رئال مادرید را در سایت بین المللی
TrexBet
پیش بینی کنید
📊
نگاهی به آمار دو تیم در ۵ بازی اخیر
رئال بتیس: ۲ برد، ۱ تساوی، ۲ شکست در ۵ بازی
رئال مادرید: ۵ برد در ۵ بازی اخیر
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105488" target="_blank">📅 13:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105487">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=KnnIasBMr4LSDI5Yv-RQ7f3997kr0IVv7Bcn-i67YGu5GapCSfJf52D37bmEOw9wR2vwv-jm_YO2GuZ1R3e-6EPzRX5SQb4nRNjfxbOTHcgxSi3cJ5Fys5-6gbAujUVafNEUNJBx7Tp4iJcHY8m2uqDeCjNnkF-CkL3buqunYfoephnMZ0TP-kMAbORgO01-1B69zLahikJ_SwuJcXmkuYmCUKBNtf3qCffm0NVjg01CPXc1dfjOUSDXyDXtSeCKgocr98my0DwjwZQa78Nzsv-_o8LWgMzIZr1p_G3YPdeAnoZn3VXamL-kYt9H83rChq2F1QbS9aonb9NXDc1hkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21372e66e5.mp4?token=KnnIasBMr4LSDI5Yv-RQ7f3997kr0IVv7Bcn-i67YGu5GapCSfJf52D37bmEOw9wR2vwv-jm_YO2GuZ1R3e-6EPzRX5SQb4nRNjfxbOTHcgxSi3cJ5Fys5-6gbAujUVafNEUNJBx7Tp4iJcHY8m2uqDeCjNnkF-CkL3buqunYfoephnMZ0TP-kMAbORgO01-1B69zLahikJ_SwuJcXmkuYmCUKBNtf3qCffm0NVjg01CPXc1dfjOUSDXyDXtSeCKgocr98my0DwjwZQa78Nzsv-_o8LWgMzIZr1p_G3YPdeAnoZn3VXamL-kYt9H83rChq2F1QbS9aonb9NXDc1hkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
👤
اسطوره معین دیشب به یاد بانو هایده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105487" target="_blank">📅 13:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105486">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZpYW3U-tdQKS0eJL4qTDJVceq92af-hsczRswolTcZ1zbW0ec1114Rr-l3jFqt3dvt7PyfQyZIN3mlEgBsvWxYuaHD3nqi4MPpU7547oVooKlZXA6ItLXkXpbPydJg66ZEUi3cqGxcUV9wh3RW8f7mm1DYqCqPvmX2kt8F9xceqYzV54n6ReJJNSJ4y698yPgZtYzsW000rkbwiiKPfBSh8acXu_o3Tr6GMvoFWEMlgp_CSxxUc9ZpnA0LmFSxlx5dHLHWTwehYi946MhZ6hiRwByAwEyFExHaXR-0GS_sQNPIIocdB0psKQvVNqVA4g8YYayfhU_WjlXRJxyrEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
📊
🏴󠁧󠁢󠁥󠁮󠁧󠁿
درصد برد ژابی‌آلونسو در تیم‌های مختلف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105486" target="_blank">📅 12:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105485">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=eme8pAfkGuq-TlC18KA4gOrJZBl6Id83ZCI8RSvCQWM_c9Zp-a6EmDRvB6-pb6Ydun0cRHMH1Sk5rUeZQHfY3b4_Mw6sKnXqg438ULNzIks0g7A48Jk4vDDUcJdl-3bwfT7Gi0DgXb9S2EgvcFAMpJK1ZCoebg2E9IhJQ0ZWipQ8zKqmI6V4EwJhdDKMbkXUJnuhyucPTYydhBONsCUFhr8lan8REK1miGORppuKx5b39sbUxdNYVT0Unljfm_dadL1TRaXHBC-1nk72SKC3dpJj_VCvpcb9WxsBDXP6qmrk-TaL70UXyYoZBiiu04o4kqUvsj3HMdIeVZxx3qnHPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00fbdf9821.mp4?token=eme8pAfkGuq-TlC18KA4gOrJZBl6Id83ZCI8RSvCQWM_c9Zp-a6EmDRvB6-pb6Ydun0cRHMH1Sk5rUeZQHfY3b4_Mw6sKnXqg438ULNzIks0g7A48Jk4vDDUcJdl-3bwfT7Gi0DgXb9S2EgvcFAMpJK1ZCoebg2E9IhJQ0ZWipQ8zKqmI6V4EwJhdDKMbkXUJnuhyucPTYydhBONsCUFhr8lan8REK1miGORppuKx5b39sbUxdNYVT0Unljfm_dadL1TRaXHBC-1nk72SKC3dpJj_VCvpcb9WxsBDXP6qmrk-TaL70UXyYoZBiiu04o4kqUvsj3HMdIeVZxx3qnHPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
اتفاق عجیب؛ نیمه دوم بازی شمس آذر و تراکتور ۱۶ دقیقه وقت تلف شده داشت اما داور دو دقیقه اعلام کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105485" target="_blank">📅 12:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105484">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLR4pF5XrEa54Xps8no9Qg7e3hG5xZWYbN2HSsEGpb9g85V8z7cnfhfqyeJhwpqFqHsvzqk3k9JLbnKkvFUdcmcOXjugjBwJ73iMTxZXtPhYJ4RL9vt5Lv3hkOLRJzhz4BzmQH_WtcfnqKIClpswIAZg6K5_ooegJg1jSjDD_9TLulurPT0W0a83BFPgXMfaOnFeJ8lfK2TSIvSBEfO5Ki1rakNlUR4MjigzWipZQlR1-yH-w-25e2XZvmZsRpz5e0WzMdVRAMdbCRY-O40OTLB3n3n4EhWPyZJa8-2ZZmx1dMItuUCcrjC9FbX-7Et3HRsKNyTbUuAoqErHWqOQAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥶
👀
نگاهی‌بهترین‌گلزنان فعال در دنیای‌فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105484" target="_blank">📅 11:55 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
