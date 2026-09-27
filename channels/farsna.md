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
<img src="https://cdn4.telesco.pe/file/B3xCMfUgM297WjgXcPM9xwlIUwNE29zV6E-1yljg_mk2E0k4Rgm_hx0V0NNPweZS-Q4Wr7l7cHENF74ZZxWtHydIWTBtTeyCYoeat_eRkFJnl29wynAXUIuv5J4wvncj-oi_rTRHVMJpP7jaPoNB1vboItS_FLQJf7yP73OL26OuGG7_WTvpBrq-gh_PwEjf495RaUsU_k8C9MwsJ9ZYBSZ5iQZ2UD37-BwNcowboxButyiv-1GdTI7nP-fDAuPXncY-fgPPX0MUZ8vPvKfNMwMKSsXCS4CyUXtWCA20nkz-DhS0wlnVf3fpHCvqkxRutTAM-JvUL-QKALsUPLAy2Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.85M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-05 21:22:03</div>
<hr>

<div class="tg-post" id="msg-464826">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecb620bec.mp4?token=ZiEHmxWrKXGCP78vOe0gCgpp0KTK1GK3NhRxYMyxtUksd18JUwYOHd_tYQPD0UVjM_1lE9foZie68pBGnSd9m-EgWDwWDla3thOZVpHWlZ3buvwOUiCQ709Z8lidMEefZgYa07dFki80VEcGy0y8hK8Wetr8_utITSDALIxHEsS7cbME4XiJ36p8OWHl_nEV_UpI9hhh0EIw11eIjQN-ZV3jjfm4e5dmp39UoRRc1kvTBTa0Yz5v9iq_FhGM4IZuSquiAO_GP2D8Gx2OwS-DXFmdf1c-tVg9t9L_MIri_kWlvdeFbOw3m9Y0rk9dwZ3gNssSwqSXueA-3jozvO3LkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecb620bec.mp4?token=ZiEHmxWrKXGCP78vOe0gCgpp0KTK1GK3NhRxYMyxtUksd18JUwYOHd_tYQPD0UVjM_1lE9foZie68pBGnSd9m-EgWDwWDla3thOZVpHWlZ3buvwOUiCQ709Z8lidMEefZgYa07dFki80VEcGy0y8hK8Wetr8_utITSDALIxHEsS7cbME4XiJ36p8OWHl_nEV_UpI9hhh0EIw11eIjQN-ZV3jjfm4e5dmp39UoRRc1kvTBTa0Yz5v9iq_FhGM4IZuSquiAO_GP2D8Gx2OwS-DXFmdf1c-tVg9t9L_MIri_kWlvdeFbOw3m9Y0rk9dwZ3gNssSwqSXueA-3jozvO3LkTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یمن بازهم یک پهپاد سعودی را ساقط کرد
🔹
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کارایل متعلق به دشمن سعودی درحین عملیات در آسمان منطقۀ الطینه در استان حجه سرنگون شد. @Farsna</div>
<div class="tg-footer">👁️ 317 · <a href="https://t.me/farsna/464826" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464825">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8a74474a.mp4?token=s46zjKT7XR3GLYg3L1b7e87OFdMbx5MMDxHeZIOkqlXatcVeM3-YRLel2QcLpe_szEH3lIDtgQmvHE0Pc2kAHHxFzqtqnQFsdJXzc_ttZy59UtmRJAn9-K9CzV0EJc9pkAaU4DfS-GkxmJ-VawOA5EfLcwTuLQ2NLJXU2wDt5c1JvhtLSEo6WqbZIt3QOVBmiHrFKeI24X_D1uXmpGwCT3AmrGxVVAgD2ZK49OpLtNfPa0LTItMan3e6Ed7hEv15MpQQL5RDQOOxnUOE9mG7gTW_8wkPESRlM6T1vyvpXVfi_Zx0fR3YVFOIX2NGb2PFO7X7wguVvrHwaul9004G04i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8a74474a.mp4?token=s46zjKT7XR3GLYg3L1b7e87OFdMbx5MMDxHeZIOkqlXatcVeM3-YRLel2QcLpe_szEH3lIDtgQmvHE0Pc2kAHHxFzqtqnQFsdJXzc_ttZy59UtmRJAn9-K9CzV0EJc9pkAaU4DfS-GkxmJ-VawOA5EfLcwTuLQ2NLJXU2wDt5c1JvhtLSEo6WqbZIt3QOVBmiHrFKeI24X_D1uXmpGwCT3AmrGxVVAgD2ZK49OpLtNfPa0LTItMan3e6Ed7hEv15MpQQL5RDQOOxnUOE9mG7gTW_8wkPESRlM6T1vyvpXVfi_Zx0fR3YVFOIX2NGb2PFO7X7wguVvrHwaul9004G04i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نام نصرالله هنوز در جبههٔ مقاومت طنین‌انداز است
@Farsna</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/farsna/464825" target="_blank">📅 21:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464824">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1SHhftkjm195uLiK79drdStVG6f6SibpLr_vGsff8YbRcuQ7b-BdX_hn7-dN9xtC0Vwevs5GSHW_Fh2iJQfb7rt4gFtbS8TT-jfbjGYVhI1AKfDdAl3OwoTH1mqp5L4fmNjSQiHqSwejO0imxo28_QnSTknLsHn0U9lk72LGBQ1qkjQbVrM5Xa7Yb20cs8MCLT1JPaOdHaepl4zQxs5wDvzC-RvmjooM1S4CEWFFDWf7YngkhyZixcQknVi2vuzVJd9m2lSaiJ5Exiw03ERVMbXXryiVy4Do2oGddeBdG1kX0p3a5bJrg-GZ_piR4e5JGkSG2-7rs0Te_jAKAb78Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنگۀ هرمز نفتکش‌های کهنه را گران‌تر از نو کرد
🔹
فایننشال‌تایمز: اختلال در تردد نفت‌کش‌ها از تنگۀ هرمز، کرایۀ حمل نفت را به رکورد بی‌سابقۀ روزانه ۱.۲ میلیون دلار رسانده و قیمت نفت‌کش‌های دست‌دوم را برای نخستین‌بار از کشتی‌های نو بالاتر برده است.
🔹
برخی نفت‌کش‌های ساخته‌شده پیش از سال ۲۰۱۶ هفتۀ گذشته بیش از ۱۵۰ میلیون دلار معامله شدند؛ درحالی‌که میانگین قیمت نفتکش نو حدود ۱۳۵ میلیون دلار است.
اما دلیل گرانی چیست؟
🔸
ساخت نفت‌کش نو چند سال زمان می‌برد.
🔸
خریداران نمی‌خواهند منتظر ساخت نفت‌کش نو بمانند.
🔸
صاحبان نفت‌کش‌ها ترجیح می‌دهند ناوگان‌شان را نگه‌دارند تا کرایۀ بیشتری بگیرند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.92K · <a href="https://t.me/farsna/464824" target="_blank">📅 21:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464823">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce62a9d434.mp4?token=HXTtj60ar7UgLA7UmF9Uhmzw-CIcMENHQ2IbIR2zxpo4j3NzbkBH0PR8MUcPuEsv7IVzeavFb2UI79qhgCfqEofFhavLTcBbFrJMXWp0D7d_-QXd-oiAyqhA5R6h2s38J5bljxrehTfVSny0gy8wtPkA2Lq3nqiZFrp8udh-7T5nlUpe2rw1tdAoxJ4yVRUx9sAItE9VUwSKeoxzzKw33QsfmsivG-0mM2N1mf95reT_hYJHEwwdvS0Iul0cLulvEEKDsqVR8oJjtAtfsjJYFZuBHQfy-11kmnrE2O-hG9tTeKn3bRkbsvyzRaPzQEvgEMJVuImSNvrSWXs2txFW7JI3ScMGgYIQLHd1hz_qg6tlldLk6BOrg-GUE0IMdeChpveM2U9fy55Y-Eh_0x7Q4Y_n3E6iu_eZ9yCJXpFoVgusxkrHebwiwf81pv0tc4Tp-2I7J6nXhokk5M_xUEUW9yIR54SHXjm9HX7UMGs07M-KHWxtQf3bvKyCU0o9faMWXxSVkWW28_L7_CrJBNgHB2yYuwv4GZEVTHYv-jxvghCqfrdqWKxlDe9jLq2-AEWA3qSub8rF4qTDB8q_DYus7stxlzOZO5_AYTXsHHjWVekSw0GlGhX0RHFFjKPvGbs81HlGAATHcGtcA8yhZKF8mltU--DgI868-HLCfUNIeoY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce62a9d434.mp4?token=HXTtj60ar7UgLA7UmF9Uhmzw-CIcMENHQ2IbIR2zxpo4j3NzbkBH0PR8MUcPuEsv7IVzeavFb2UI79qhgCfqEofFhavLTcBbFrJMXWp0D7d_-QXd-oiAyqhA5R6h2s38J5bljxrehTfVSny0gy8wtPkA2Lq3nqiZFrp8udh-7T5nlUpe2rw1tdAoxJ4yVRUx9sAItE9VUwSKeoxzzKw33QsfmsivG-0mM2N1mf95reT_hYJHEwwdvS0Iul0cLulvEEKDsqVR8oJjtAtfsjJYFZuBHQfy-11kmnrE2O-hG9tTeKn3bRkbsvyzRaPzQEvgEMJVuImSNvrSWXs2txFW7JI3ScMGgYIQLHd1hz_qg6tlldLk6BOrg-GUE0IMdeChpveM2U9fy55Y-Eh_0x7Q4Y_n3E6iu_eZ9yCJXpFoVgusxkrHebwiwf81pv0tc4Tp-2I7J6nXhokk5M_xUEUW9yIR54SHXjm9HX7UMGs07M-KHWxtQf3bvKyCU0o9faMWXxSVkWW28_L7_CrJBNgHB2yYuwv4GZEVTHYv-jxvghCqfrdqWKxlDe9jLq2-AEWA3qSub8rF4qTDB8q_DYus7stxlzOZO5_AYTXsHHjWVekSw0GlGhX0RHFFjKPvGbs81HlGAATHcGtcA8yhZKF8mltU--DgI868-HLCfUNIeoY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آن‌هایی که چراغ اجتماع را اول روشن می‌کنند
@Farsna</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/farsna/464823" target="_blank">📅 21:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464822">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWcyNjg2_5FC9NcreWLnSDZCldYIZ8yfixpk0RjxceB8-ING-qRycaQbPNdSH5urOk06MZT8vsZgatZQRx02oiUCRUKKxcFKvtXVNHBkqt8sVyyJvgZe2z3O_z5NtRZLrIYRmMeiwH63psF9Rms4QRY3msJiPbcPfmZygTFrcZichQi4kpxclLAzsDW9iz8Hp1RfkMY7uh-5lNfdna15bBb6feRcJE3tfOdQtmZkGBiPNq-aU3dp9TRRwD2sik81HgqhqCXWnese10eeR3TJVUrOZIA9_sqqkiQ0-4ZYC5TiMtCfQGdT0trESjBpZHHkEm12KMfalrulYp90dIr16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس ستاد دیه: زندانی غیرعمد با بدهی کمتر از ۴۰۰ میلیون نداریم
🔹
اکنون کمترین بدهی مالی زندانیان جرایم غیرعمد حدود ۴۰۰ تا ۵۰۰ میلیون تومان است.
🔹
در ۶ ماه نخست امسال ۵۰۵۹ زندانی جرایم غیرعمد با مجموع بدهی ۳۷ همت آزاد شدند.
🔹
همچنین ۲۰ هزار و ۶۴۰ زندانی جرایم غیرعمد در نوبت دریافت حمایت ستاد دیه هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.27K · <a href="https://t.me/farsna/464822" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464821">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usUdkpgpkjsiHSKK9dJpoo0S7XP3NmbmtCeIl_TwoP-sIVrgszZW_17QhM3qv0CL4nJpH6C1HaR4mrbezr3Zgacw3PSGeOwaS8C2YPeW5JLZEzghoHHTEgBrjtAUfsDfefEqj1UjV16GnNDN8uw_7HSHbzR6aACF7QEDqRJkHtnRJLDDABol-wQwDcd-SxJRBEuqjtE25JsDTaayRxcZOuvEt8u60Swulq5toPFdu-3xjhLKE3UYmdGKw8wVi5p4DlXcA512mLQLDabCAch4DhcX-eX1v8MZIO3C-c2BZo9p3r73Ba8PMgMBZKrVMQSAtJv5jnDwiytCRuOwrQhYhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای حکم ۱۰ ماه حبس برای رسایی چه بود؟
🔹
حمید رسایی، نماینده تهران در مجلس، در پروندۀ شکایت محمدباقر قالیباف، رئیس مجلس، به ۱۰ ماه حبس محکوم شده است.
🔹
موضوع اصلی این محکومیت، مطلب منتشرشده در نشریۀ «۹ دی» در دی‌ماه ۱۴۰۲ با تیتر «دستکاری قالیباف در اسناد مجلس!» است.
🔹
رسایی در دفاع گفته این تیتر مستند به اظهارات یک نماینده مجلس بوده اما دادگاه این دفاع را نپذیرفته و اعلام کرده وقوع دستکاری در اسناد مجلس به اثبات نرسیده است.
🔹
دادگاه در این پرونده علاوه‌بر ۱۰ ماه حبس، رسایی را به انتشار تکذیبیه در صفحۀ اول هفته‌نامه «۹ دی» با همان قلم و اندازه تیتر ملزم کرده است.
🔹
همچنین گفته شده در جریان رسیدگی، از رسایی خواسته شده بود نسبت به مطلب منتشرشده عذرخواهی کند اما او نپذیرفته و گفته «دلیلی برای عذرخواهی نمی‌بیند و از موضع خود دفاع می‌کند».
🔹
رسایی امروز هم در نطق خود در مجلس گفته: «این حکم را غیرحقوقی و سیاسی می‌دانم؛ با این حال چون یک حکم قانونی است، از آن تمکین می‌کنم و حتماً برای اجرای آن مراجعه خواهم کرد».
🔹
رسایی همچنین محکومیت ۱۰ ماهۀ خود را بیش از حد دانسته و گفته طبق قانون در اتهام «نشر اکاذیب» برای فردی بدون سابقه کیفری، باید اقل مجازات یعنی ۹۱ روز صادر می‌شد.
🔹
برخی کاربران باتوجه به این‌که محکومیت رسایی برای قبل از دورۀ نمایندگی اوست این سؤال را مطرح کرده‌اند که چرا حکمی که منشأ آن به پیش از دوره فعلی نمایندگی رسایی بازمی‌گردد، اکنون و در دوره نمایندگی وی به اجرا رسیده است.
🔹
در مقابل، آن‌چه از رأی دادگاه برمی‌آید این است که مبنای محکومیت، صرف «انتقاد از رئیس مجلس» نبوده، بلکه دادگاه ادعای مشخص«دستکاری در اسناد مجلس» را اثبات‌نشده تشخیص داده و انتشار آن را مصداق «نشر اکاذیب» دانسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/farsna/464821" target="_blank">📅 20:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464820">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cy7K9jm5kozhCwseXrR59HVXQh9qwvBgMAW1sKiPnZNDq1DkVLM62mesFvbXfEZdEVZJzoagIS4DdMfjCOvjnTZyxEbhV4FmXCR79gNC5W4tMJU-Ab4pbYf2YqfiX-0-_Z6_tqNZLi4tRdN7LZAbtZAxs7oLXxF2CkZPSSbAPD7bIfAvzOACUyS0UWe9fRo_bYI7EbsEMtcF6nUN9TeplQR9qhdalpAMI3vt0ko_ovQlZSvfUEZX2fR_zgKPDDdv5iiHA9i-dNgLpn6XJbMtCmD2t9QKe7CsmN6L-Nu5dXBi4HnrJ-TSQX-D_AdMw-CqoR22QDS0wSZx4xQ1Ybh-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعلام «حادثهٔ بزرگ» نزدیک پایگاه میزبان آمریکا در انگلیس
🔹
پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست خبر داد و اعلام کرد که شماری از خانه‌های منطقه تخلیه شده‌اند.
🔹
پلیس شهرستان گلاسترشر انگلیس امروز…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/farsna/464820" target="_blank">📅 20:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464819">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7eaf9933a4.mp4?token=KbG6yIovxIeoMfRlnlABjpLH7S3GJr3D1QGPna_4q7nE3pDsKgwlIowIBeOFPC_shQr61ik9hvTubuuf8VP7fL1WIjeBZx24wJZARtXrgmKkmkiHwL5omigivVorMlrnSSNKmwtnRigzQLabhx01HSKImlM_i-l_TJgAnnbhDZjlYk7DUdjOzwj_UAiNmdEDImlUki8TmBt-rwpmAbR-wCWyXNrlT66MAic7KcSXHksQzZYyjyYlgK4CthRQtEQF35DZ85Er4jvxXnpW1edM5XoAS9Yht7gzKTNY-A6goAbDZrOGTJL7auVzUfJoNXoOW2fToSDOXNV6ayYi2PQlJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7eaf9933a4.mp4?token=KbG6yIovxIeoMfRlnlABjpLH7S3GJr3D1QGPna_4q7nE3pDsKgwlIowIBeOFPC_shQr61ik9hvTubuuf8VP7fL1WIjeBZx24wJZARtXrgmKkmkiHwL5omigivVorMlrnSSNKmwtnRigzQLabhx01HSKImlM_i-l_TJgAnnbhDZjlYk7DUdjOzwj_UAiNmdEDImlUki8TmBt-rwpmAbR-wCWyXNrlT66MAic7KcSXHksQzZYyjyYlgK4CthRQtEQF35DZ85Er4jvxXnpW1edM5XoAS9Yht7gzKTNY-A6goAbDZrOGTJL7auVzUfJoNXoOW2fToSDOXNV6ayYi2PQlJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شکار دومین زیردریایی ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد: رزمندگان نیروی دریایی سپاه به‌یاری خداوند طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/farsna/464819" target="_blank">📅 20:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464818">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qzXNDnE_n3Yx_AvHUygt8Gi-18QnYv8xY4igqbCZPoKDuoxglHm5YuKHr2jsI-JeqfkEs6lpfNPU-EJBr5NNveI9GrfEeu2Pwf7Cf4uIvJfZq9E8tDQH4MHuoq2B0YuvnAHRUK6UMjKGN0HV5hMMkT0K6zO0jSWDQ4KOZ9D40sihiLiAvSvks140665ndyolO7L5dM0lJFoqmPum9jUthbMTX3vcvLeXeOAeNnv_Aocc0hA0PE-MouEDU5QlxsUrOrHHYVpEesEdNygpuGKLX5K2vwpkYLaoRo-3Hbia08SV-KD-yGIx6FMVVWmB1iBu5YBBTsC-fF8JzpjBTv7BhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: یا بازار نفت احمق است یا ترامپ دروغ می‌گوید
رئیس مجلس در واکنش به ادعاهای مقامات آمریکا مبنی بر بازبودن تنگه هرمز نوشت:
🔸
بنگاهِ فریب‌کاریِ آمریکا می‌گوید ایران کنترلی بر تنگۀ هرمز ندارد، اما بازار یک اضافه‌بهای (پرمیوم) سنگین روی نفت کشیده است: ۳۵ دلار بالاتر از قبل از جنگ، و ۵۰ دلار براساس قیمت‌های نفت فیزیکی.
🔸
پس یا بازار احمق است که نفت را با این قیمت‌های بالاتر می‌خرد، یا دستگاه روایت‌شویی آمریکا دارد سیاه‌بازی می‌کند. برای کسانی که حرف آمریکا را باور دارند، یک دستگاه چاپ دلار رایگان در تنگۀ هرمز گذاشته‌اند؛ بفرمایید بروید بردارید!
@Farsna</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/farsna/464818" target="_blank">📅 20:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464817">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEKUYz_7mno656kpYXQ9PNtjwYwTnXSpLE5OaSwuvyDUUVeUqKq1neB3ZDi_iAGfGvv3dKzVD-fAQfW9QtPm7W0GE20lcPtTZnDmZR13dtEpRqr2O35T39BlbWcSCHHQuAUWi2glxCNiX5SnDng3km0-IgZVwRzJxVukdeQuocfeUid4bA6Qbru8KZOJgttF-dY-AzNewXJ1lid3EQQGzE54ZDnABbhQRgOwN9QtWD-HPcmnGT508Shiy5nZ3tnyQuqlEGfTvC9ZXIf1NKEmdOoUkOgl5GHj4-n7hQX0t0Wc1iSTonxQCPojO5jnQO7VGJchM7xTrbyZaFBhbGgFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل مدارک ویدیویی جنایات اسرائیل را حذف کرد
🔹
میدل‌ایست اسپکتیتور: طبق اسناد فاش‌شده، گوگل بیش از ۷۰۰ ویدیوی مستند از جنایات جنگی رژیم صهیونیستی در غزه را از یوتیوب حذف کرده است.
🔹
ویدیوهای حذف‌شده شامل تصاویر قتل شیرین ابوعاقله، خبرنگار دارای تابعیت آمریکایی…</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/farsna/464817" target="_blank">📅 20:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464816">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c478512e.mp4?token=e1eo008-Kp_bxWa0RWr31TwoDm90uq69_nmNaeSm_fM-W1mwiu_sT_kZ5RIVIzeo0UQeyFIJPa0Ru5YCidQuxSOBWmzqHC71lP22LpXte7NPzxahfVwJy1N-uDnTfTxXJun20oJcFzXUxs7Y6ySVuFNcwg5KrKDUVo6TcdzPUDZBkcCexnk8K4W8OwOe9eYJPxW0Vy69B4F9VtE4ku5jy6IITN8Pbf0XSKDfRWSdSMdsJ9vW4NVexFMbBsEC2kip2e-N8W4btS9okzOsqwAQvBoFwdAULRnznd3URdvws9LM7aybJyY3ubqfrJVI7gtcFjfDjDdwueK8AUap7qsEjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c478512e.mp4?token=e1eo008-Kp_bxWa0RWr31TwoDm90uq69_nmNaeSm_fM-W1mwiu_sT_kZ5RIVIzeo0UQeyFIJPa0Ru5YCidQuxSOBWmzqHC71lP22LpXte7NPzxahfVwJy1N-uDnTfTxXJun20oJcFzXUxs7Y6ySVuFNcwg5KrKDUVo6TcdzPUDZBkcCexnk8K4W8OwOe9eYJPxW0Vy69B4F9VtE4ku5jy6IITN8Pbf0XSKDfRWSdSMdsJ9vW4NVexFMbBsEC2kip2e-N8W4btS9okzOsqwAQvBoFwdAULRnznd3URdvws9LM7aybJyY3ubqfrJVI7gtcFjfDjDdwueK8AUap7qsEjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه گمان کردند شهید شده‌ام!
🔹
خاطره‌ای از ایام حضور رهبر معظم انقلاب، آیت‌الله سیدمجتبی خامنه‌ای در جبهه‌های دفاع مقدس ۸ ساله.
@Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/464816" target="_blank">📅 20:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464815">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QuVnR3x8U7eMZMA5zjimmxwfr7JzojrY1J1l5q0oReqDFQaNrzr0qzXwBLF4OKigo3EOKPg9P28LXDsPKGBn5wpEoER7sGTZsQ4jm0XxAtcbSkxdZNddjnzueCtXMvAVRo2jw_-msmPgAPED5o8vwNf0sCluSXh8d6T0TRDMRr8GEvPZrrPLCaBNOyc8ANWveISyOmjTPexzKBeGT_Xr8VIHLhVNJAExPlcKanVR8HMfzHAGZzFCx3110rAEhgzWe8vekc8HW79rG-QXQ8Ba7tJt1LUQo_MOpnAFIuFOevH92anjoFlH0ansCqeDfKFmdjMaG76UB7cW-f7n6TGQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
نمایندگان کشورهای ساحلی دریای کاسپین به‌یاد شهدای میناب ایستادند
🔹
در اجلاس «کاپ ۷» نمایندگان ایران، روسیه، قزاقستان، ترکمنستان و جمهوری آذربایجان، ۵ کشور ساحلی دریای کاسپین، به احترام ۱۶۸ دانش‌آموز شهید میناب و معلمان‌شان از جا برخاستند و یاد آنان را گرامی داشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/farsna/464815" target="_blank">📅 20:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464814">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTBwE-efd3_Z81BJ1LUOoYjxrJNZYK9mCUKbZPwWzT8Pj0FjJTd0u1OeBc-ty6qUZ9aWPOiF7-VpxXqErYYSvn_-7ytiyBDZIuWoT3y3mPjkdfovn9ceuOFZS8ER7hG-HUYUypDm40PTgxvkQ5r6KJoJ1xNHHq5G6S_gpIs-mJI7cFET6NIJ4FEKs8U__1GdNQIQlaqMIYsq47Zgzzbf6hD2ncNtTqg8TqnmhfJKWKDjSm4-yx3VwVcT1iH8DWrZ4gGBmeLHKaQ0_6GAr5Rfbd-svLRrPB0pbydkf6w0lN-3PRmJ8sPTk1VnvH4Bz7DQlPpLqAAUPefEwV3ZrSsMOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازهم تیراندازی خونین در آمریکا؛ ۲ نفر کشته شدند
🔹
در پی تیراندازی در یک زمین بازی در منطقۀ بروکلین نیویورک، ۲ مرد ۳۳ و ۳۵ ساله جان باختند و عامل تیراندازی پس از ارتکاب جنایت از محل فرار کرد. @Farsna - Link</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/464814" target="_blank">📅 20:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464813">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYq9TvM2c241YEgB6HORbpDUVNKY_m6o5qpZOgguvT44umq1DVAv6dq0NjEE68_MZWzS11Y2fMEp9lF5OjalQna9fllJQKp8OjTcJzAyDY0n1etxfb5Kgv6DoHuHMSAOVUM1IB1tqb4M760Z0KieU2-c2V9jfQ3pjnfpyyndsYqIMiO02art8OBKHNKsudlhEcb1Mo3lkPBdqXF3XMvDO2yiYTuzFjed9-sURhWOMcFcTP2Sws64O34XBK6mVpFAC23KiPsHo3f7quc7WtBq9Bxw7wclUVHCQYdD1CvE0YHLqdkKrrYpfEoN3o2N8qPoThdZip673yXYS2kYFPiTCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان جنبش نجباء برای تحصن در مقابل فرودگاه نجف
🔹
در ادامه واکنش‌های منفی به تصمیم دولت عراق در توقف پروازها با ایران، رئیس شورای اجرایی جنبش نجباء خواهان برگزاری تحصن گسترده در مقابل فرودگاه بین‌المللی نجف اشرف شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/464813" target="_blank">📅 20:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464812">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🎥
تصاویر منتشرنشده از لحظه شهادت سید حسن نصرالله در ضاحیه لبنان
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/464812" target="_blank">📅 19:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464811">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a87c72497f.mp4?token=Nrr3e0i8ye82zPycGXCy7VnbvIr7mcNsZKO5uiEpms78XUMbf5aOW1NN8LtcGY5eADqsRMm8XYlbNHdO8LNhq1HY4R4zgelwAsy84x-nPbCx7f5GAwE1xnW-I9Tgr9YXN5HH_mS2X_v3CdJnh9U6LxlMQqubfG5YTFQ2sY1bQCcGljxy7v4j9DfnVtt-vNHTqWrhz-Flak4x0HU-IaB3ujb0b-6jYN12_DrOg6YE-VaSbBQyh6aT4BpqPpMT5Jv-zDMUhaEPybtwkpBFkocsazOfgJ7eqf6EC7JheIo8_-pkkDWf8vrp4BKjW-_NgJGDvDN0rRmJ1dvs7XevKWpSVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a87c72497f.mp4?token=Nrr3e0i8ye82zPycGXCy7VnbvIr7mcNsZKO5uiEpms78XUMbf5aOW1NN8LtcGY5eADqsRMm8XYlbNHdO8LNhq1HY4R4zgelwAsy84x-nPbCx7f5GAwE1xnW-I9Tgr9YXN5HH_mS2X_v3CdJnh9U6LxlMQqubfG5YTFQ2sY1bQCcGljxy7v4j9DfnVtt-vNHTqWrhz-Flak4x0HU-IaB3ujb0b-6jYN12_DrOg6YE-VaSbBQyh6aT4BpqPpMT5Jv-zDMUhaEPybtwkpBFkocsazOfgJ7eqf6EC7JheIo8_-pkkDWf8vrp4BKjW-_NgJGDvDN0rRmJ1dvs7XevKWpSVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: غنی‌سازی ۶۰ درصدی مگر غیرقانونی است؟
🔹
ما اورانیوم را تا سطح ۶۰ درصد، با اهداف صلح‌آمیز، غنی کرده‌ایم و این اقدام در چارچوب تعهدات ما در NPT قرار دارد.  @Farsna</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/farsna/464811" target="_blank">📅 19:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464810">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec0e89a4a.mp4?token=g1QoIr85fJFi3-aReJOuEUc_zY2YwVCViko5lB6FkpLKpEs7QJJNq2nU9n2DsmHhlAQfuAasy_zwgYT-oBO-Kn8JvdJG4VRtpqLbza2DYQrz95KzuUHh1juiucd-ooApYRQkVht9Qp8yp3lHq3m4uCT1530i7Z6ZtA75cPSuD8oGSF_bQ32i6X0J_CGpH3yB-WHVetn1SRo4njPlyvQUqUEGTdHWEpiM22qcgGF2teRzoapLUGgwkeYShYZmsVOblgLh_39z7qyg36JpguFmxmoe5R-oXXmiimj3zxkWFeg11qoOyjShAJkF8RRLMwswlxWFaOP_OZls3YCao60Gw4gAbFNTF0f90EPrtznfj2P1m1ZTDPt6IOWSaPP9K1P3ZA1x1GQyb46AhmDJENm3nrMe3J2ZCSU2dADjAU1toiC7RJhklW0xw64aC5SkSrtTsUIm1yb65JR7ZlcKMweFG844CReUm30e6MqAdciHvOJkbYx0Taj6GuOvCAhkrBY2l43FEcSrv4kSAvylTKuraVJY1HJ-u1fik7tipixwXInALnaSbxxhuefbFgEWC9pvUeiRvahFoaWf4VvmMIFTpkhHKRS3h4zMkQ4-bQ8ep4AybRDdnq1i0MWqYYUYWc6wiJjYswIBXB-Gb03hGp2ydgGpI1DvkcxdHloM4-qowlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec0e89a4a.mp4?token=g1QoIr85fJFi3-aReJOuEUc_zY2YwVCViko5lB6FkpLKpEs7QJJNq2nU9n2DsmHhlAQfuAasy_zwgYT-oBO-Kn8JvdJG4VRtpqLbza2DYQrz95KzuUHh1juiucd-ooApYRQkVht9Qp8yp3lHq3m4uCT1530i7Z6ZtA75cPSuD8oGSF_bQ32i6X0J_CGpH3yB-WHVetn1SRo4njPlyvQUqUEGTdHWEpiM22qcgGF2teRzoapLUGgwkeYShYZmsVOblgLh_39z7qyg36JpguFmxmoe5R-oXXmiimj3zxkWFeg11qoOyjShAJkF8RRLMwswlxWFaOP_OZls3YCao60Gw4gAbFNTF0f90EPrtznfj2P1m1ZTDPt6IOWSaPP9K1P3ZA1x1GQyb46AhmDJENm3nrMe3J2ZCSU2dADjAU1toiC7RJhklW0xw64aC5SkSrtTsUIm1yb65JR7ZlcKMweFG844CReUm30e6MqAdciHvOJkbYx0Taj6GuOvCAhkrBY2l43FEcSrv4kSAvylTKuraVJY1HJ-u1fik7tipixwXInALnaSbxxhuefbFgEWC9pvUeiRvahFoaWf4VvmMIFTpkhHKRS3h4zMkQ4-bQ8ep4AybRDdnq1i0MWqYYUYWc6wiJjYswIBXB-Gb03hGp2ydgGpI1DvkcxdHloM4-qowlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: سیدحسن نصرالله نماد مقاومت برای آزادگان جهان است
🔹
شیخ نعیم قاسم خطاب به شهید نصرالله: شما پرچم آرمان فلسطین را درجهان و در حیات ما برافراشتید؛ فلسطین همواره قطب‌نمای ما خواهد بود؛ آزادی سرزمین ما همواره اولویت ما باقی خواهد ماند.
🔹
شما…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/farsna/464810" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06d01b5ae4.mp4?token=i3uJihkR443VyUZlzjqeT9axqFKry4y617R0OJ1F5birej30GYXKsuYLUO2k6ED2a-1TFx7gb5id0SFkk3UPoWY1UIwjo-ox2wNnmPgOurMWmGoSiK4Q9x_nO9hil0Gzmp8tIxcnqwvpHlZCZlsc8Z6vh-uYynxpSjUBEnYEXk5Kv3YTxO2ntA1ubuGlZPFR_Hh4CcIhzsTg8xtVF22CZmm27Rd06eOUO63gJ4880VTWY78B9GlYAV6reMOvirV7ZSgfljS3RedZNjd9RPJzuqFgQ_jW68tAm2-uFeFR3Fod9AKsVoIuOj4gzkH3P_rWvumO_FOBUyobvYwc9A5AaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06d01b5ae4.mp4?token=i3uJihkR443VyUZlzjqeT9axqFKry4y617R0OJ1F5birej30GYXKsuYLUO2k6ED2a-1TFx7gb5id0SFkk3UPoWY1UIwjo-ox2wNnmPgOurMWmGoSiK4Q9x_nO9hil0Gzmp8tIxcnqwvpHlZCZlsc8Z6vh-uYynxpSjUBEnYEXk5Kv3YTxO2ntA1ubuGlZPFR_Hh4CcIhzsTg8xtVF22CZmm27Rd06eOUO63gJ4880VTWY78B9GlYAV6reMOvirV7ZSgfljS3RedZNjd9RPJzuqFgQ_jW68tAm2-uFeFR3Fod9AKsVoIuOj4gzkH3P_rWvumO_FOBUyobvYwc9A5AaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ما کاملاً برای احتمال ازسرگیری جنگ آماده‌ایم
🔹
بار دیگر تأکید می‌کنم که در برابر هرگونه تجاوز جدید، قاطعانه ایستادگی خواهیم کرد.
🔹
ترامپ در جنگ قبلی خواستار تسلیم بی‌قیدوشرط ظرف ۲ روز بود، اما اکنون ۸ ماه است که آن‌ها درحال جنگ هستند، بدون اینکه…</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/464809" target="_blank">📅 19:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2db84a86b.mp4?token=rkDkullrgzR6QuGqn0Iia_DYVjpDkQuwwjANchj7_w_NkZZkHpzICExS7YyGPpRgkGAJC3dvUMNUAuyf9oYTs4bi7Fv9Z7MRT4yQHjecd-JHOZYZZsICV7f1li4Kph73jTePNutXFtdwICKBtwSXcIc8Xhl7NXBuNupGdKD2wR414eK1cO75WAKVbH-rHmI-tGR0GqaOCeoeZ3sbh-W2HBa548IJbJ91_hlcyt4LVpBgrLaw0m_A8h_4jReoGhd-QHxg3j88dN0fQKj7SKwpA5rX0X44o0AMg3PsKJpWLKMvspCKESfMeALAbBUU15-t7_t_02pORT7XYZ1zrRPJpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2db84a86b.mp4?token=rkDkullrgzR6QuGqn0Iia_DYVjpDkQuwwjANchj7_w_NkZZkHpzICExS7YyGPpRgkGAJC3dvUMNUAuyf9oYTs4bi7Fv9Z7MRT4yQHjecd-JHOZYZZsICV7f1li4Kph73jTePNutXFtdwICKBtwSXcIc8Xhl7NXBuNupGdKD2wR414eK1cO75WAKVbH-rHmI-tGR0GqaOCeoeZ3sbh-W2HBa548IJbJ91_hlcyt4LVpBgrLaw0m_A8h_4jReoGhd-QHxg3j88dN0fQKj7SKwpA5rX0X44o0AMg3PsKJpWLKMvspCKESfMeALAbBUU15-t7_t_02pORT7XYZ1zrRPJpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سه‌شنبه‌ها روز بدون خودروی کارکنان دولت
🔹
رئیس سازمان اداری و استخدامی: به همۀ دستگاه‌ها ابلاغ کرده‌ایم که تا حد امکان، روزهای سه‌شنبه را تا پایان سال به‌عنوان «روز بدون خودرو» در نظر بگیرند. @Farsna</div>
<div class="tg-footer">👁️ 6.63K · <a href="https://t.me/farsna/464808" target="_blank">📅 19:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464801">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hSFhawOydXIoCSQvGYERSrIEvkf-vi0FLkm4O9Q4hzAdruxTCrRxY-ruRJNrg2Oi5fUcTW7IR6eDAQn7MueNfIuhhO07vRQIS6deLufil37AqFOPNUpNNOKz5GnvD0Hyx0Na2ezTyhvWPPKzwCj_FHvpw1Hd7kDVVYgDnxxzFCKvQAACwXatIl_fzgeJPsKkqO9VnYmuvKB_sfLSa0EDsJJa1rxQ7TH4P-g-lBZCpWXtECy7V0_JIjosOHpeB4tEw7YOlcOyeXBKTEnvursJTX_hAPuAsRj_MVnGh22dM_NC4cW4q0vg_7fRsUSJkBU66hSSw8C4Oru-tASHljPcGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NO90ANuqw831kpmdpqZOPk4ri3glu8Ti7AYL4n3EwUiqjQsTn2-bVAuuwECMC6wCEvrY310fEj6GD9cHOWXriQ3oS0I4Vk6sJBZBXn-lwT5_W-XsAAfNX6Rk6cRyKoWSfj-fI-aknSrTloggREa9lTa1ci3mvqayUbrF3ozHME_293ABEeMbXSgUqvGRt13lmxy6iL86g-XkyTu_IRrcxWWigiXJfOCfyaG0xpKdnZtjsN2CMt2V1eaGk6Ol-Nn6lX_AEnowBnzvbs4bwii2OtDzO7OwfDnF0XVYkdXp4EBADs3cy24obGaWj_aybP54YGxCu37hhUmYMUfu4ZllkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEnwcuJBfRtoZNPJ897CeGCQm8OpULagnlKN0SXZJA58cEam7xFQZFNUJnuzzPbF9QlNX_CMU3tGxAL9Q7l-SGJ1RVTYiUjDhOjxTDgnfjGcVLT-IJzUWxnGGTSIB9fXyoDQnr26utApexQtp8q1HKcqtMpmANwdciz4l-h9gnrQkNa4DmrAoDQ7kn1R5-dxtceuTupHiWGO8OPsKXYELb-4UIq2Ydt0HUqJCB2siqhzjpBHpG_C5p73WCnkGtMkwxAcAZwteutpc4t5NFfgpMWo0f5eCybW6NvHtNYw6Ns-hg6Tk7KOQQQYYdm7_BmqFbWJMJ9w62bd3VlPZtcEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SaTA7M98pIxAPmjLxkLFWWK4WKTmB9oeJUZKz7Yps1nYNqTYxdU1OsjfhCnIbX2-vdkKa5Xux_HpDcZOYAufDJfePoBmQgEKlO02bu9fG9aDy4H4EAdfDqD0hYzI9L2NDLf7C5Ik_YP5ftFQj9toSK0DkhiTwbfTp2emKiaD-NaM48rriCVbIpq82ATRKDCH_kyXuIiRzmjmXBMWVHFvcnbb89GPyUr7nvGjAp5HJGqia6bSKbx2gw_i4opkjZWa-H4nI2xIGNtqjVueSM8zAAELtBxHEEpsDszoA-GRIWXvK5d-i_WkaBY38_D7vhh7WLc7p6ihZ3Wt8FzAmRMigg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y0htXfwmSJZVmDt3fnvJQ_v7czqcAIY-65senQIFD6ta95CVPAL-AijvksZsQfXOxfnQi1sKiJ8Pw1wqdy4fl-EnYEEr37uw_VvDoWKpICOXMkejdRUSy0b0Oa9M5C_knphUN1vseheCZqws-W8mvy9Cg4Lv7zJFt9Ek1CCevWJUz3SGUwUCoTDx7n0HrMHz1KdB9ld5mmZt2epzlTQmLt0o22dUHVQvrpIGiApYDV4V3Rh2FA01rWuwwSH7Yr4TWFRrBU8h3i__FulNgYdOwT03Yx63sO79zPkt-ZddbVfQD54k9nO5BqwrybACUP-lMh9DjnCLjp_woZwQXKkTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cr1QeuSTLtfoGNnP3T7JS65dlJ4KzZsb0Y_EgwD3MJ7lCo_RHk5wHdHSY733t01LxteQHUa94EevWu_mXQZzCuhK2gcQTE3QrL5Kbu7A07YxrVmrzVbI2rpmI-1LYINLVgEv_gencIhIPkYZcJlfBm6FNY5ltaNqKFnWP9R2u-suQ4VtK8IJaEGEtyWtw76wxt6xmbD_jikmVERGVffoAaL5Z-T5OR5vn5Q4VOeQPWzgKKvnsmf1Ppf-NQlOu12kEaK3djQyhUv8cly-nol1cMbAUwj9oEE1vvWyqQQRaO2a3F3_Tf90L09ZXNhEviSKHXPfO37mdT8enSNs9plpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T97EjFDVwG5OyuO-ZoP4zGlP3vhUmtPip86uYE5b5azsllDvqTKuqLVgXeyr3GXOZHBN4Bm63LeVJnHdDtNYvpw23DiVHX_h64CHUFkQMiD4wrxQCl0Utod-nkIYkAtoH4Ni4kSwLVHGNFtkPszezb06feauZvRD9wj5kmp76MNcbXBGAH0dW3SXbMGKa6RChZis6bgz-EdjZ0b837zNjJt6VfMOTw3eaxdiDaI51oHlukKSmj2G6HWLT-phjgS8wbnzRpPMWGOZGnLg6hEYiQKfmq5lMjkyVMEk7tGJNJT-BYqHhHt5ecLpRmOT4YirE-iFliVHCzk3L_e3oICEpg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نمایشگاه رزمی فرهنگی عملیات رمضان در اردبیل
عکس:
سیدمهدی پناهی
@Farsna</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/464801" target="_blank">📅 19:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464800">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj4Mrm1N1VsTCzGMyYAnoHDoVPu8fcZoROw8PdYge7L7FDUdM9lcgDR7ffou_YI4excj44-vxWg3JyypKMJBs8VY4PBuy_ubVNsKRB0v-9oxbyrFrIiXSfWZVbQ1-w7aDZejgwxykYqyCLcUCvW3uAh4VNdvzpPRxAsg1azuSsf-BJ93MLFI5QjSOoqxQodwehAJqjtilzvwaWKwm9TqutpDSNVKb5bcjvu3AgDgAFyA-2uq0cK4C3z_jkhidtaYVzxs5dUALBeNcWRJabz1QG_Z0DVuesYTiyqglnaTpfpILR7So-Z5mhDT29bUcpaaBiAwo0M39dY70UXaV1yfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حراج جدید شمش طلا سه‌شنبه برگزار می‌شود
🔹
متقاضیان تا ساعت ۲۴ دوشنبه ۶ مهر برای ثبت‌نام و واریز مبلغ ضمانت فرصت دارند.
🔹
مبلغ ضمانت هر شمش ۵ میلیارد تومان است و هر خریدار در یک هفته حداکثر می‌تواند ۲۵ شمش خریداری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/464800" target="_blank">📅 19:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464799">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/877db700d7.mp4?token=EKcsjl8tkXiK9b0kUWc7jOMb-tQN8160zkkC-sLop5lZ8Xyn2D_1XZvRIf_JYSYHZssBkK_q1BQWlaur0pXHmekkQH1etlEu-gVdFaizC2kKva8jyegCQqhiQ5ILwGQGvhdTMAv0TKBwIKthV0Kq6AlNEO5nlbpCk_p2ALGU3E08cXMtT1x2SCYrp42dI9EMWvfWXvHIoWoWLGsLRUETGVd_qZXNMs-UbEAKZMystQrfwRsxBas4iEvo2DPmp_V9OH0ik9lro0P8DpcU2RqiEbU9BvqExAgyxk5sX9x-nAT48ao98CxR9mG6Mv41SInQCpomB9XT0n7wC5XQDxV4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/877db700d7.mp4?token=EKcsjl8tkXiK9b0kUWc7jOMb-tQN8160zkkC-sLop5lZ8Xyn2D_1XZvRIf_JYSYHZssBkK_q1BQWlaur0pXHmekkQH1etlEu-gVdFaizC2kKva8jyegCQqhiQ5ILwGQGvhdTMAv0TKBwIKthV0Kq6AlNEO5nlbpCk_p2ALGU3E08cXMtT1x2SCYrp42dI9EMWvfWXvHIoWoWLGsLRUETGVd_qZXNMs-UbEAKZMystQrfwRsxBas4iEvo2DPmp_V9OH0ik9lro0P8DpcU2RqiEbU9BvqExAgyxk5sX9x-nAT48ao98CxR9mG6Mv41SInQCpomB9XT0n7wC5XQDxV4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: استخار‌ه‌ای که در روز بازگشایی مدارس انجام دادم بد نبود و اتفاقا خیلی خوب بود
.
@Farsna</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/464799" target="_blank">📅 19:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464798">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af748ff1e1.mp4?token=PRUcxXaYI9yfFtM1eQI_mzKbJT-WwOXLVfoo7PcVFi8wp-dTGqQS-W6_HYcMFvzlmkcTznsWN0QtUsmWChbLFZrK-cv8RlCPnfoW858uFtqThSf02NpMUTaY9Y1z3zMNYUf0gqTyeyihjEilIwpinK0jduh8ifpqGFzOEMLWHjjJsfOFXDiuq5GTe8-I8-E5yzFSCNzEQ8h3hyDrPVkeqf_R5oB036GAXiBLWMSDWE9GcIw50KRDcJosbJiVY9P_Cx8RQ-lNwHoJUwsKLk3zkDx8ub-r0JN9NKUFasSrDmFq-l8js6Gg_wxNabvGSuqpv-8zJudIWkPXlVGGrHQEDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af748ff1e1.mp4?token=PRUcxXaYI9yfFtM1eQI_mzKbJT-WwOXLVfoo7PcVFi8wp-dTGqQS-W6_HYcMFvzlmkcTznsWN0QtUsmWChbLFZrK-cv8RlCPnfoW858uFtqThSf02NpMUTaY9Y1z3zMNYUf0gqTyeyihjEilIwpinK0jduh8ifpqGFzOEMLWHjjJsfOFXDiuq5GTe8-I8-E5yzFSCNzEQ8h3hyDrPVkeqf_R5oB036GAXiBLWMSDWE9GcIw50KRDcJosbJiVY9P_Cx8RQ-lNwHoJUwsKLk3zkDx8ub-r0JN9NKUFasSrDmFq-l8js6Gg_wxNabvGSuqpv-8zJudIWkPXlVGGrHQEDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق در اعتراض به لغو پروازهای ایران در بغداد و بصره تجمع کردند  @Farsna</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/farsna/464798" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19cb2f3565.mp4?token=gxWS4T8BwljkaZneb3EPQtINxEbKsdqSdlRDW8eDhL3cbST_vHCFgWk2nAgH6V0Jo9Vy06A_yLLAPXDpFwnhOagRZqTWEGxWtKoZgYGbnE33h4ghdps58m8GTz2t5341wAYfXv1i4Wptr8-1t0PM9N-eZyK9WYQPVVPzewxVLteiYO5W80rjFSSSE-UTs3F09qBkBPv2_VzemvbUs0ZP3h6cJ_J7eepnjnlbO_PvD4WdeEYNKPgoECjqyrsEt0nSg3QsJMjp-QmQnjYA7OUmqLKCoqkh_isQLESYDooqZEFco-jHAjV8vbn7S15fYpNSFZRa38iPoaAVFByha8GdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19cb2f3565.mp4?token=gxWS4T8BwljkaZneb3EPQtINxEbKsdqSdlRDW8eDhL3cbST_vHCFgWk2nAgH6V0Jo9Vy06A_yLLAPXDpFwnhOagRZqTWEGxWtKoZgYGbnE33h4ghdps58m8GTz2t5341wAYfXv1i4Wptr8-1t0PM9N-eZyK9WYQPVVPzewxVLteiYO5W80rjFSSSE-UTs3F09qBkBPv2_VzemvbUs0ZP3h6cJ_J7eepnjnlbO_PvD4WdeEYNKPgoECjqyrsEt0nSg3QsJMjp-QmQnjYA7OUmqLKCoqkh_isQLESYDooqZEFco-jHAjV8vbn7S15fYpNSFZRa38iPoaAVFByha8GdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: دلیلی برای بازگشت به مذاکره با آمریکا نداریم؛ برای دفاع آماده‌ایم حتی اگر کار به جنگی آخرالزمانی برسد
🔹
در سال ۲۰۲۵ وارد مذاکرات شدیم، اما در میانۀ مذاکرات به ایران حمله کردند.
🔹
در فوریه ۲۰۲۶ نیز پس از پذیرش پیشنهاد مذاکره، بار دیگر در میانه مذاکرات…</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/464797" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464795">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oJ4LihMVN2b2T7hmtxErW2zXmy8lki8TiMW3ZK8m45H3L8SEbmmuoImb9-OxKTMmh7iI61d-YnTPJidcPpcEIIrx-yKAEk79DE-zaQbGOQZMxsh9JMByPSRBlFSWAYbWOEfcpl8tb4ZT0dy-omYnY6wlh-cuHwvSsW31AuTS0ZkSEWXXvNRe7mj9Ie30p0fi_nTuwsTJvoI_dWFkiFwuzQN685Kxv20pD4YK8KhE2u0TBe6RzNfI1F9ISu0_sEyts-Hi6O-i6k5-FwqIEmwcDV-1D0bPKqOIciJl3qawICDvO6JCynJBdN6PUXBbKE6xdWw-ofClyXHs1S4cJ97HBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q1IBhH06_xELd6JB-uuFYkkdu_5ixDlB1XIX0LJspD7kXT8jLaWOT_QFq9FZHgH64SMkswMK77r_KKjtCPMOJptyOmo2Mvi5IFvh5sYcYZo8QcBnZ3KObifDqlMzD-7y8NRwLkP3CP1LWck5GBVVn2dY4vB1qzycIu2MB5nc788Bbc7UoX3OYcuBKMat2w2KMiJAmXIdKUX7CcaUB-1IKjWA-Eoctd14ouuEc6kzucWUQYK3KFppIQ8LIp1fGNGwfpt3HiRe2-CzamvNzQeig2VsjIQm8_MV-eMfd4LIgXlEsh_qX-TRsQkx28HdnhhxYi2NLhsB6SNViZ-Rc2Cnmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
رئیس سازمان لیگ: طبق مصوبۀ هیئت‌رئیسۀ فدراسیون، لیگ نیمه‌کاره قهرمان ندارد
🔹
باشگاه استقلال درخواست اهدای جام کرده، اما هیئت‌رئیسه در این زمینه تصمیم می‌گیرد و من و تاج تصمیم‌گیرنده نیستیم.  @Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/464795" target="_blank">📅 19:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464794">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5267bbfaeb.mp4?token=cskT57G8EP2Yb4U5FOIsQqMiFtqINE--MUK6CmpplBerWb3XUvFbbRVG1Nh2RDBiB3g0ZmLfU5ksGfL6Kz0XVcB214_oKU3JeIJ_LMeeMXZa7PA6LwMYwc-dfgyDWU20ngaxouDyRKQxhH7Bs_GFwT6qk3afHBNIGeZXgBM-bF8Jz1H_z1QTv19tcF3ZcNcKqFwSzz9-EMxboyg4nlzae0RyLb8gYJlamyW0b9re7X21s1KXs3nTOXm-lM-hANjDbGf0csvMyFrlLZHpZdMXl7foUSs2vtEiHolvY7AU2oX10lSi1WteaixI90iMHsbXzD3xnc788fDy4_3F_CehFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5267bbfaeb.mp4?token=cskT57G8EP2Yb4U5FOIsQqMiFtqINE--MUK6CmpplBerWb3XUvFbbRVG1Nh2RDBiB3g0ZmLfU5ksGfL6Kz0XVcB214_oKU3JeIJ_LMeeMXZa7PA6LwMYwc-dfgyDWU20ngaxouDyRKQxhH7Bs_GFwT6qk3afHBNIGeZXgBM-bF8Jz1H_z1QTv19tcF3ZcNcKqFwSzz9-EMxboyg4nlzae0RyLb8gYJlamyW0b9re7X21s1KXs3nTOXm-lM-hANjDbGf0csvMyFrlLZHpZdMXl7foUSs2vtEiHolvY7AU2oX10lSi1WteaixI90iMHsbXzD3xnc788fDy4_3F_CehFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب چگونه چرخ صنعت پتروشیمی را می‌چرخاند؟
@Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/464794" target="_blank">📅 19:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464793">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVeHoVZBfsUxhp5jaUgNRPvTUNXEQrUIuCVSdOTzEaxXA1Cnkio-g70oxuUJWjlG6Me1zloUkCLFu4qaGQVlku3T0NcROBL7BjEukk9QGA76ICYOOhrueO2S6FDwjsO3jYUdFFDSNLKyLXsXt_iRG4_86osOBrHWufKeHL5DQ_nf-dV8cCeggPQ39jc04iW3dTol7RpnciWfJInYRDVZnhlSCArbCjckAXAlY0lFtPoDKclLk1eusv0eEQp91bSyjl4BaNPlgJbdtw-V5CbDGcAu1Nf10p7erWowX6wWFl0TmAxtszm3KoJmSlseqyh8x26csD31Qm4g98N2sAl3iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: همان دشمنی که در ۱۸ و ۱۹ دی آدم کشت مدافع حقوق ما شده‌است
🔹
رئیس سازمان بسیج: دشمن در کشور ما اقدام به کودتا می‌کند، سلاح می‌فرستد و مزدور می‌گیرد؛ می‌آید در ۱۸ دی و ۱۹ دی آدم می‌کشد و بعد می‌آید مدافع حقوق ما می‌شود.
🔹
اعتراف کردند که در ایران آموزش دادیم، پول دادیم، سلاح دادیم؛ همه اینها را به جان مردم انداختیم و بی‌ثباتی در آن کشور ایجاد کردیم؛ اما مردم ما آمدند و در عرصه امنیت از کشورشان کردند.
🔹
جنگ زمانش محدود است؛ هشت‌ساله، ۴۰ روزه و ۱۲ روزه. اما روایت جنگ گاهی قرن‌ها ادامه دارد. بنابراین روایت باید به گونه‌ای عمیق باشد تا با گذشت قرن‌ها هم دچار تحریف و دچار انحراف نشود.
🔹
دشمن می‌خواهد با روایت خودش قصه بگوید و مردم جهان را به خواب ببرد؛ ما با روایت‌مان ملت‌ها را بیدار خواهیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/464793" target="_blank">📅 18:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464792">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i__Hj1FRQgOnRvHTeK67Md2yQsjLdlcULMveUNg7A6wFddgLnMVEWVPGP46K71cm1wLcb8Yn8-F0DjfzamdzPMR-gMMQcmL_RtbgXVW4x_iF1kSvsdNhul482liC52x27-sndXpF_pVm1clWsy8e4dL4pBoldAnwWe1d2-5q1PZP7wKvW1nJaQDM_V0r3xaWLFrXjKl4nOVxcgSCoFHnlzDVpkg3NBlH3uTpmz64sZ8wXlMkZJFtzaSh5b0b2cz6GLTuNpl_aYcxz6q4iT5qThNdk6hBqj_c9wUVGhAavb43_l3y74bJe33lSRoQD0f3MUAyqfYduA4gzDVkivcWEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
قابی دیده‌نشده از دیدار حضرت آیت‌الله العظمی شهید سیّدعلی خامنه‌ای و مرحوم حضرت آیت‌الله العظمی شبیری زنجانی
🔸
رهبر معظم انقلاب، حضرت آیت‌الله سیّدمجتبی خامنه‌ای، نیز در این دیدار حضور داشته‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/464792" target="_blank">📅 18:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464791">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/551a5a85a5.mp4?token=poO7XPtfLFtDX7zSE3pM_JVdP9i2zXuSGG0kBbm49zABTRik2Wc_5M_N_jPXAgCwdFlEp3XlNBM9WqKkZuW9rvxgJx7-L6hFLOdbStQ_CmZC99VHaseh2KyMOihw5_9xoUH7h_uNOsUhhmywOpuT-72mrYzE4fGc6qVFPiWTGNytB4TJPXp9Kn9YSJ3naezX7W89PA7BIe65lzb6Krd20dH6o9Vh0Aa_Gu2kU6XlJAFUo9DVxZ08j037D1ercpdKnfiKufodeHk7RHpG0vENzMf-rhGZrc84OO2lUH5zcNIi-x61SEAG3jy2maHx1LsEAcAbeEDwIdDG35FCmWEsJaj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/551a5a85a5.mp4?token=poO7XPtfLFtDX7zSE3pM_JVdP9i2zXuSGG0kBbm49zABTRik2Wc_5M_N_jPXAgCwdFlEp3XlNBM9WqKkZuW9rvxgJx7-L6hFLOdbStQ_CmZC99VHaseh2KyMOihw5_9xoUH7h_uNOsUhhmywOpuT-72mrYzE4fGc6qVFPiWTGNytB4TJPXp9Kn9YSJ3naezX7W89PA7BIe65lzb6Krd20dH6o9Vh0Aa_Gu2kU6XlJAFUo9DVxZ08j037D1ercpdKnfiKufodeHk7RHpG0vENzMf-rhGZrc84OO2lUH5zcNIi-x61SEAG3jy2maHx1LsEAcAbeEDwIdDG35FCmWEsJaj9TtM2mI3JQVp9iBvjiVp8Cu6yzIASO_UJGuP9ayKXeeDltJ5TxgbSWUZuWGLa--YZ7VUCxdcXaednEzRRuMlINp5OeO4pJsPMimD0rXbocsRmIlRA65iAgQv9Ixlw10doRmAGzcSekZTz3xblYxiPzwr4PROJy_tmuJDi3Qsf9XdCgSoE-mEjWlWzjKXyav7duko5VSJ_U5cfgzSQtShZACPeh1but8XkYXsTwdktCcjz8FwnPeZIrDHnzokPKyf7tSBzjCiMttV96TwNaq1hXyTYafWl_halhEAS8rEicVd8KaK-XsWIAVH11hP5fpizWxysq4OASrcVM0flrBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این ۳ جملهٔ آمریکایی‌ها را فراموش نکنید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/464791" target="_blank">📅 18:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464790">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">جدال نفتی بغداد و ریاض علنی شد
🔹
بغداد و ریاض بر سر گرانی حمل نفت عراق به جدال لفظی افتادند؛ عراق عربستان را متهم کرد و عربستان با رد قاطع این اتهام، انگشت اتهام را به سوی تنش‌های امنیتی منطقه نشانه رفت.
🔹
ماجرا از آنجا آغاز شد که وزیر نفت عراق، در جلسه‌ای در مجلس نمایندگان این کشور، در حضور رئیس شرکت بازاریابی نفت عراق (سومو)، اعلام کرد که هزینهٔ انتقال نفت خام عراق از حدود ۲۶ دلار به ۳۷ دلار در هر بشکه افزایش یافته است.
🔹
وزیر نفت عراق در توضیح این جهش عجیب، ادعا کرد که خرید ۲۵ فروند نفتکش توسط عربستان سعودی، عامل اصلی این گرانی است.
🔹
ریاض در بیانیه‌ای، نه‌تنها خرید ۲۵ نفتکش را تکذیب کرد، بلکه تأکید کرد که افزایش شدید هزینه‌های حمل، ریشه در تنش‌های نظامی، حملات به کشتی‌ها، اختلال در رفت‌وآمد دریایی در تنگهٔ هرمز و در پی آن، رشد ریسک حمل، افزایش هزینه‌های بیمه و کاهش شمار نفتکش‌های آماده فعالیت در منطقه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/farsna/464790" target="_blank">📅 18:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464789">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZHZVkavQDTQFSZwjPHCOjhmbv7s1FQRPgL5QZkMePuQWqbFwAMynClRFEMmB4gS9lQPNF2lWc0satgSD48Uhd3F2ZaJ3U5_uM--CQdSmA3sJ0YqVdRcZmlHtmgIG0zmimNxsATyLpXR9PnRfhDV5Py9zJWjdzUhQejNsb-lOO6UtrnoYBNTvpDB6YjgfqhFyHus7JK0WkcjlOegbF9QeIE5-ZEMqcbYvaiMRtYQy8kP2tw98ScjcgIkIAu4NyQiuf4cYWjafKiYVCwelL-se_Fe00gMZM9t4z5uM3PThtRVftv94UI4t1MwdPIN6SobLd7kI_TYO4mr9dPFSeHWig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: پیشنهاد ایران را رد می‌کنم
🔹
رئیس‌جمهور آمریکا اعلام کرد که پیشنهاد ارائه شده توسط ایران را که به موجب آن، تنگه هرمز ظرف مدت هفت روز، باز می‌شد، رد کرده است.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/464789" target="_blank">📅 18:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464788">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7621fa550c.mp4?token=GFKcELA9nkT3dfH2bAhVFS674G2jqw3LkHoT8g0ilBUBV564fZ4ncyZgNcQQRZQRR1ONZznfE3alzSPph-7eIRNIsRtyHrpmoZ8SBv5nEyq-4EosZvQIVOdOlOWStIeQrD-fNANLWmX1DAd_J1osOlSvxR-5Z_X-Okh-nZuPpg5WRaXWHW8Z7uFGX9fehN0j2b8WKyW7F0Gp_b5WKlG8LDG6-nnmLkGR2HGjLF4j5HyOcQyCS6Ur0VzIRC8ZX3P66bXo8E1PeGw3-TGeUKXfhe_devFjFWhcCmU39Eldg90rvYm0ICQF7egiYx-sNEMiYcQMxTrt3Hb2iZaOw2HeDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7621fa550c.mp4?token=GFKcELA9nkT3dfH2bAhVFS674G2jqw3LkHoT8g0ilBUBV564fZ4ncyZgNcQQRZQRR1ONZznfE3alzSPph-7eIRNIsRtyHrpmoZ8SBv5nEyq-4EosZvQIVOdOlOWStIeQrD-fNANLWmX1DAd_J1osOlSvxR-5Z_X-Okh-nZuPpg5WRaXWHW8Z7uFGX9fehN0j2b8WKyW7F0Gp_b5WKlG8LDG6-nnmLkGR2HGjLF4j5HyOcQyCS6Ur0VzIRC8ZX3P66bXo8E1PeGw3-TGeUKXfhe_devFjFWhcCmU39Eldg90rvYm0ICQF7egiYx-sNEMiYcQMxTrt3Hb2iZaOw2HeDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رزمایش ۱۱۰ هزار جان‌فدا در بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/464788" target="_blank">📅 18:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464787">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TYo6ObtZpNprfy9SOIAkHy95svNKRXp1Wb6xSRoDQp5PhG9r-U2hU58iADjIx3TpFzGnWNgVXAgMB9sl-3IOp9xSzTUVn29t4_5SGc5blFK-AiJUwa-LKksWF_IkhOH_Y4tnbHevUdkP4Bq6nh-Y7alE8cAQsaBwsScK3_yn5Wqd9Y46nITXeS7ot6XnNsQyV7jJUaXEnXvilwHliMYn_x1l8H3wxRzclmyh2G7AtIujSK4MrdhGdN0A4SykinH4h4N8Md7CB6EJVxkzcqexe0w7_-YWxZ0Z-Vk-zdeRtaTrxqXT4yGbXVw_8FQ7oCEYAFx2F1E10DXGCluKQo6fLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادق محصولی: دوقطبی‌سازی کاذب، مقاومت مردم را جنگ‌طلبی جلوه می‌دهد
🔹
دوقطبی‌هایی مانند «جنگ‌طلب و صلح‌طلب» و «تندرو و میانه‌رو» با خدشه‌دار کردن انسجام ملی، مقاومت مردم در برابر دشمن را هدف می‌گیرد و نباید دفاع از کشور و ایستادگی در برابر متجاوز را جنگ‌طلبی معرفی کرد.
🔹
همه دنیا می‌دانند که ما جنگ‌طلب نیستیم و جنگ را شروع نکرده‌ایم؛ اگر کسی واقعاً در داخل کشور معتقد است که جنگ نباید باشد و طرفدار صلح است، باید خطابش به دشمن باشد؛ چراکه ما جنگ نمی‌کنیم؛ ما از خودمان دفاع می‌کنیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/464787" target="_blank">📅 18:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464786">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70394d0059.mp4?token=pjBwqPsshESxBqnoNSbOcT_nQMifkUuZfRjxAGm0rC9jHjCuLr4awl9zOtvEPjpNssV7QCy2dX9Yft5-se8N3fKaIjtYbA77MczIoi544GAgkXVdqTNxu8wKsvHkFejRm-D2jCutOTeHWo5bZbcJ5ewZCnrJQ4Sn71Nn0BaASBQ32M3hBq2MufYaXkZM6imCG7Pm9hH-tkOKsXeZOrRIPH8vvb0OYMyUHpLCo6WlUMSBBZhzdT-X_xDclsu39oi5J5yW4DlIg4uPX-hJvoGEBCkkDi7NRw5HvI7KT7-VwkbqbmWbq4xGHKtZBfWTTY_0lhV2SI2KFJt7ShLsJ-VmwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70394d0059.mp4?token=pjBwqPsshESxBqnoNSbOcT_nQMifkUuZfRjxAGm0rC9jHjCuLr4awl9zOtvEPjpNssV7QCy2dX9Yft5-se8N3fKaIjtYbA77MczIoi544GAgkXVdqTNxu8wKsvHkFejRm-D2jCutOTeHWo5bZbcJ5ewZCnrJQ4Sn71Nn0BaASBQ32M3hBq2MufYaXkZM6imCG7Pm9hH-tkOKsXeZOrRIPH8vvb0OYMyUHpLCo6WlUMSBBZhzdT-X_xDclsu39oi5J5yW4DlIg4uPX-hJvoGEBCkkDi7NRw5HvI7KT7-VwkbqbmWbq4xGHKtZBfWTTY_0lhV2SI2KFJt7ShLsJ-VmwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: دلیلی برای بازگشت به مذاکره با آمریکا نداریم؛ برای دفاع آماده‌ایم حتی اگر کار به جنگی آخرالزمانی برسد
🔹
در سال ۲۰۲۵ وارد مذاکرات شدیم، اما در میانۀ مذاکرات به ایران حمله کردند.
🔹
در فوریه ۲۰۲۶ نیز پس از پذیرش پیشنهاد مذاکره، بار دیگر در میانه مذاکرات به ایران حمله کردند.
🔹
پس از جنگ هم سه ماه مذاکره کردیم، اما ۲ هفته بعد توافقی را که خودشان امضا کرده بودند، نقض کردند.
🔹
به همان اندازه که برای مذاکره آماده‌ایم، برای مواجهه با هر چالشی نیز آمادگی داریم و در برابر هر تجاوزی می‌ایستیم؛ حتی اگر کار به جنگی آخرالزمانی برسد.
@Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/464786" target="_blank">📅 18:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464785">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: ما آمادۀ گفت‌وگو [دربارهٔ انحصار سلاح] هستیم، اما اول دولت جنوب لبنان را آزاد کند و بگذارد مردم به خانه‌هایشان برگردند؛ بعد خودمان باهم کنار می‌آییم. @Farsna</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/464785" target="_blank">📅 18:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464784">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر امروز یا فردا اسرائیل از منطقه‌ای عقب‌نشینی کند یا طرحی برای عقب‌نشینی ارائه کند، این نتیجهٔ مقاومت است، نه حاصل مذاکره. @Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/464784" target="_blank">📅 18:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464783">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: دولت لبنان به‌جای ایستادگی در برابر پروژه آمریکایی-اسرائیلی، عملاً دارد به آن کمک می‌کند
🔹
دولت لبنان مؤلفه‌های قدرت را یک‌جا واگذار کرد و همه خواسته‌های دشمن را یک‌باره برآورده ساخت.
🔹
دولت به‌دلیل دل‌بستن به آمریکا و اسرائیل، مسئول اصلی…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/464783" target="_blank">📅 18:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464782">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‌ ‌
🔴
شیخ نعیم قاسم خطاب به مخالفان حزب‌الله: ۲ سال تمام جان کندید تا سلاح را بگیرید و نتوانستید؛ حالا چرا این توقع را از ارتش لبنان دارید؟ اصلاً سلاح چه ربطی به شما دارد؟
🔹
در خواب ببینید که ارتش لبنان ابزار دست شما شود. ارتش لبنان، ارتشی ملی است و مردم لبنان…</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/464782" target="_blank">📅 18:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464781">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: اگر بعضی‌ها تسلیم را می‌پذیرند، ما زیر بار آن نمی‌رویم؛ لبنان مال همهٔ ماست و باید با هم به توافق برسیم و از حتی یک وجب از خاک ۱۰ هزار و ۴۵۲ کیلومتر مربعی لبنان کوتاه نیاییم. @Farsna</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/464781" target="_blank">📅 18:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464780">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‌
🔴
شیخ نعیم قاسم خطاب به مخالفان حزب‌الله: به‌جای اینکه به ما بگویید «چون مقاومت می‌کنید، دشمن به ما حمله‌ می‌کند»، به ما پاسخ دهید «چرا خودتان جلوی دشمن نمی‌ایستید؟ و چرا در مقابل دشمن کوتاه می‌آیید و به او باج می‌دهید؟» @Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/464780" target="_blank">📅 18:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464779">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: تسلیم در برابر اسرائیل یعنی پایان «همزیستی مسالمت‌آمیز در لبنان» و واگذاری کشور به شهرک‌نشینان صهیونیست
🔸
مقاومت اصولاً در پاسخ به تجاوز شکل گرفت؛ پس ریشه و علت اصلی مشکل، خودِ تجاوزگری دشمن است. @Farsna</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/farsna/464779" target="_blank">📅 18:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464777">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‌ دبیرکل حزب‌الله: ما در بنت جبیل، خیام، عیتا الشعب، ناقوره، بیاضه، علی الطاهر و هر نقطه‌ای از جنوب که مقاومت حضور داشت، ایستادگی کردیم
🔹
پایداری و مقاومت در «علی الطاهر» ۳ ماه طول کشید و در سایر مناطق نیز ماه‌ها ایستادگی صورت گرفت.
🔹
مقاومت بر ۲ اصل استوار…</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/464777" target="_blank">📅 18:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464776">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: برخی، به‌ویژه در میان مخالفان ما، می‌پرسند: «مقاومت چه کرده است؟» اما ظاهراً یک پرسش را فراموش کرده‌اند: «دولت لبنان چه کرده است؟»
🔹
مقاومت جلوی طرح و پروژه تجاوز را گرفت؛ کاری که مقاومت کرد این بود و نگذاشت دشمن به اهدافش برسد.
🔹
مقاومت…</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/464776" target="_blank">📅 18:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464775">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‌
🔴
دبیرکل حزب‌الله: خواهان تداوم مقاومت هستیم و برای استمرار آن در برابر دشمن تلاش خواهیم کرد تا از سرزمین‌مان بیرون برود و به آزادی کامل اراضی اشغالی دست یابیم. @Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/464775" target="_blank">📅 18:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464774">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان:  یاد سردار شهید عباس نیلفروشان که معاون و مشاور سیدحسن نصرالله و فرماندهی بزرگ بود را گرامی می‌داریم.  @Farsna</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/464774" target="_blank">📅 17:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464773">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i6hFPJlc6l26ONrNgq3anAyo4BS6UBnS0yP1hLGJkHJwyR41yMJ-qDezlbzKmO8Oks6rVVMZcgMKRYTgySQTWxirwOgL-39fMJ72GYM6MNAOgZXjw5jaxHZb032x85yRUSJPEyN-0WP6m6HXmmM3SyFW99SeAU3SN8lkUKYTO23Uwil5j4YscI06Ifk-BeDixuBy2SJyZ6N3XeoMbHLi5zJ0eKU98ORNMyLWyK56vKLqqsMOGaT8orjmXpipNMrChpRtnG0gP_dKMhQSCFPTw1nmYvb1iyO4oKJXyDrlO3EvYk7IPjp3gobddmzp2yqYGzfrdHNpYBdNFnv0DetaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیرکل حزب‌الله لبنان: سیدحسن نصرالله نماد مقاومت برای آزادگان جهان است
🔹
شیخ نعیم قاسم خطاب به شهید نصرالله: شما پرچم آرمان فلسطین را درجهان و در حیات ما برافراشتید؛ فلسطین همواره قطب‌نمای ما خواهد بود؛ آزادی سرزمین ما همواره اولویت ما باقی خواهد ماند.
🔹
شما…</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/464773" target="_blank">📅 17:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464772">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/084e5cf88c.mp4?token=tEGNT6RUCtA6TFUba6fm_P2sqr39BaEUw2d97AqpLEv_mmBr295xjyKiTrPXCSX6K-kDFs04v9sSeLeFFBfSZE1vPFKbllQk4_65J9oSGbh3mkmksJ0nUQWc6dWX5PukLWQJIbx2mP1WqKNhzlYYwTxml8nsiB3nOvcrfwpZW2OQfZmMO3Nmr86ztamyDhLj-baAgUGIEondbWlWdKu_ekTGnQaiRUIZj3OnIIhhVsPEJPOsxXP5kn-HHKxnpGogs6nfYCHDlqHuISYhba2FlAzvGW8rCm2WDPLj4PCEc7eKzgGDMWEoe2jJroS-liMdTyBx1IznF1ygXPQoKcPxjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/084e5cf88c.mp4?token=tEGNT6RUCtA6TFUba6fm_P2sqr39BaEUw2d97AqpLEv_mmBr295xjyKiTrPXCSX6K-kDFs04v9sSeLeFFBfSZE1vPFKbllQk4_65J9oSGbh3mkmksJ0nUQWc6dWX5PukLWQJIbx2mP1WqKNhzlYYwTxml8nsiB3nOvcrfwpZW2OQfZmMO3Nmr86ztamyDhLj-baAgUGIEondbWlWdKu_ekTGnQaiRUIZj3OnIIhhVsPEJPOsxXP5kn-HHKxnpGogs6nfYCHDlqHuISYhba2FlAzvGW8rCm2WDPLj4PCEc7eKzgGDMWEoe2jJroS-liMdTyBx1IznF1ygXPQoKcPxjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرق میان ایران و اوکراین اینجا مشخص می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/464772" target="_blank">📅 17:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464771">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FzscuB7-X-iVEsMOsqB6G8O2m4eNKUqlCBAwx6hen0cyix9Qmm0-bCqvUCOWA0pyuO4rZoPtYnJYkv7Nr7KUnq8EmoJnaApk0blV_l7ug0rjcrmwG9S9xqwchqOt5nZsWCvjNyN7Uz5Esk14WdZsoN-hQIxsB5Kfg9mvBahYayvYCqhn2MczcN5yqcBU4ov5nPHak1yalKtNpJ_D7kbcbhzSU-Szs0-50ECvRyXzLMdLQzMpOP2nPdX0QSWi9dN2EEMvdYGHwtxEgXwXD4qaYWTym_Hqtg0ZHWQieKoxiDbeh_hP5I1XTcZDf-KQMlo-ED0fnMzV9WZJH15eVji9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حضور مردم لبنان در سالگرد شهادت سیدحسن نصرالله در جوار مرقد او در ضاحیۀ بیروت  @Farsna</div>
<div class="tg-footer">👁️ 7.09K · <a href="https://t.me/farsna/464771" target="_blank">📅 17:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464770">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/074489213d.mp4?token=tNWg20CUOlje4QrPF0fWsgeAJFLMVfYh8_HHdk3UBgXeijbSpQOiyUnqKrdm7b_CTLDm1CvPyusX8lBsXIbw1U6wZzn59v00FH7hKpBdOGlMDa5A2WE8pVK40UUW9rNm64d20JUIDTKcgeEmMUjmlXXDtDOYybdoHzw-KpDyqbBG2CO5IR9v6Utxuh4ojhDjXdwYZ8fsiUguU0ihDx4OdLFs3dxvLn15QzZmk80BaAaWzmtUKN8-BnTTZw3-6rBlBBgK_h4dvobxgvac40I_kKzAbEQf0BZvZf7L84AwRJYlskAlzOoLvUIh6-MqXOr5yftdChtUVTXHGktkuWXPLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/074489213d.mp4?token=tNWg20CUOlje4QrPF0fWsgeAJFLMVfYh8_HHdk3UBgXeijbSpQOiyUnqKrdm7b_CTLDm1CvPyusX8lBsXIbw1U6wZzn59v00FH7hKpBdOGlMDa5A2WE8pVK40UUW9rNm64d20JUIDTKcgeEmMUjmlXXDtDOYybdoHzw-KpDyqbBG2CO5IR9v6Utxuh4ojhDjXdwYZ8fsiUguU0ihDx4OdLFs3dxvLn15QzZmk80BaAaWzmtUKN8-BnTTZw3-6rBlBBgK_h4dvobxgvac40I_kKzAbEQf0BZvZf7L84AwRJYlskAlzOoLvUIh6-MqXOr5yftdChtUVTXHGktkuWXPLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت خبرنگار بی‌بی‌سی از نفرت جهانی از اسرائیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/farsna/464770" target="_blank">📅 17:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464769">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f0ed778a.mp4?token=chzd63WdNCMik3xlAIwLnC0tRzTo1o4GRaLv6uq_vSeIlXpstbzxhtrJzr30ePzLFYUGuN2xEv6q8MKSmtQnH7uipO61qlJtW1j5iGUhCvZOct3NANckkcJGt_eANqbUriWKV-rATNfECi8-TpGy1Iy862wOtOnLhgGLhzytQO3AlCfim8wZuW_NNV7oMIRTK5s72i-RLMMYQTKFSQzZUKL03AqktMSgNG4TrTNbri__B_r4AIHrcR3uIOISNwfS7KTeAzdeztGdwsyqbI0AJEImvNPuqRe5npt59rh1J0-gdh8hbanMMlby3V87sZBJsS1OqyYPBNvWcE1pswTQjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f0ed778a.mp4?token=chzd63WdNCMik3xlAIwLnC0tRzTo1o4GRaLv6uq_vSeIlXpstbzxhtrJzr30ePzLFYUGuN2xEv6q8MKSmtQnH7uipO61qlJtW1j5iGUhCvZOct3NANckkcJGt_eANqbUriWKV-rATNfECi8-TpGy1Iy862wOtOnLhgGLhzytQO3AlCfim8wZuW_NNV7oMIRTK5s72i-RLMMYQTKFSQzZUKL03AqktMSgNG4TrTNbri__B_r4AIHrcR3uIOISNwfS7KTeAzdeztGdwsyqbI0AJEImvNPuqRe5npt59rh1J0-gdh8hbanMMlby3V87sZBJsS1OqyYPBNvWcE1pswTQjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌  سخنگوی نیروهای مسلح یمن: جنایت در تعز عواقب وخیمی برای سعودی دارد
🔹
یحیی سریع: تاکنون ۵۰ نفر در بمباران بازاری در استان تعز، شهید و مجروح شده‌اند؛ این خون‌های به ناحق ریخته‌شده، عواقب وخیمی برای سعودی جنایتکار به‌همراه خواهد داشت. @Farsna</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/464769" target="_blank">📅 17:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464768">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f52f42b09b.mp4?token=B3h_vHGhjSGi1gczdbpwO-qU9l2Q4zS3OqbXscBZMzRUL1nIgRVTT29GGphalg-jzkllni7939pczhajwjknMWIz9gzzy05ZR8Cixwh6yf0TdRjaFu7g60wZLqj8JomCPi_DkY4elSWDPz_B-Db85-nqMKbLB3Pu2xgbpZH5F5eSyA7KXFWtNgoe33JJxAT61d9ynkdURPTY0u9-CruZXEUZPSWoWu7FwBRCtaQEEQ7VhHv6rKZbBQ4XCxfPcE2gvvIAwWv1rzPY6wLOKZRDoOylRHz6vtpSjrl1b3BBDX2s0DgpNLfXrgL-2RXO1224qBGS9blKjf0_mZdtmsRSGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f52f42b09b.mp4?token=B3h_vHGhjSGi1gczdbpwO-qU9l2Q4zS3OqbXscBZMzRUL1nIgRVTT29GGphalg-jzkllni7939pczhajwjknMWIz9gzzy05ZR8Cixwh6yf0TdRjaFu7g60wZLqj8JomCPi_DkY4elSWDPz_B-Db85-nqMKbLB3Pu2xgbpZH5F5eSyA7KXFWtNgoe33JJxAT61d9ynkdURPTY0u9-CruZXEUZPSWoWu7FwBRCtaQEEQ7VhHv6rKZbBQ4XCxfPcE2gvvIAwWv1rzPY6wLOKZRDoOylRHz6vtpSjrl1b3BBDX2s0DgpNLfXrgL-2RXO1224qBGS9blKjf0_mZdtmsRSGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعترافات مهم یک تجزیه‌طلب؛ از پروژه براندازی تا هدایت تجمعات زاهدان
🔹
مهیم بلوچ، از سرکردگان گروه‌های تجزیه‌طلب در شرق کشور، به‌تازگی در یک برنامه به اظهاراتی پرداخته که ابعاد مهمی از نقش تجزیه‌طلبان در ناآرامی‌های شرق کشور را آشکار می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464768" target="_blank">📅 17:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464767">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixAJ2o87FP3M5IK7hVvrxw0jnTpwNno5GQyFb_QhncJlIgsWIRpC-mOYXIKe20GWLRILTa3WntYPOo3JY1M7am-yPfcfePD-t86vbobuOvJlr-phxoSeFeYcX2ecmk5yXPfAVLkseEPUm0Xz3DzHZfivbvgIAfG0uTkQYVCE_S0FogLeSaTiC0v0YlNUhtkuSHu_7U_ajkpsOmJ_-1zeKmSMEwqnTC5gDvLPzxqTZgbLYCypq5m7dIDtIm_AdXwkK2rbfqV0h_zyYJ2ZGfsiCCuHiEQ_aSHB7-bYbtdg9FhDBemyZXP70kCuOSlRHvw97hUGsfDJNzyxbQ_tkN1blg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش‌های ایرانی دزدیده شده شناسایی شدند
🔹
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔹
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔹
بر این مبنا نفتکش مجستیک ایکس…</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/464767" target="_blank">📅 17:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464766">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904ae263e4.mp4?token=GlHdzysIdZJ24XmMYcVrQDbTR9kyAR7VxSs8BqX4U2GqMSmrp1xajanGjnNt39FTXOdnUIeyRbEU39RNdL7UrkfUXgDkwKZ1UzyP4UXRVAwJ_3SINyAA6RgyYjykjQtg5WcdpYQktJlMcjjY7-_Fkf0mlHQlE0LjTNZ7_eMn5VXNni0OVu4n5AOceG2QtXp1HOhzn7fDviOTYkareBFQMXgCH6uPVFGk5nrEpG8xRbgK6onoHBxwAGT6lutJZTS7zqBkUyYFeRMVttVpvCBkspZhoD-4EiSh7jXfs4HwN9wc_Zl618O9fCKal0PzcNjoUJoo7S-g4UshsfGF20Xi5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904ae263e4.mp4?token=GlHdzysIdZJ24XmMYcVrQDbTR9kyAR7VxSs8BqX4U2GqMSmrp1xajanGjnNt39FTXOdnUIeyRbEU39RNdL7UrkfUXgDkwKZ1UzyP4UXRVAwJ_3SINyAA6RgyYjykjQtg5WcdpYQktJlMcjjY7-_Fkf0mlHQlE0LjTNZ7_eMn5VXNni0OVu4n5AOceG2QtXp1HOhzn7fDviOTYkareBFQMXgCH6uPVFGk5nrEpG8xRbgK6onoHBxwAGT6lutJZTS7zqBkUyYFeRMVttVpvCBkspZhoD-4EiSh7jXfs4HwN9wc_Zl618O9fCKal0PzcNjoUJoo7S-g4UshsfGF20Xi5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور مردم لبنان در سالگرد شهادت سیدحسن نصرالله در جوار مرقد او در ضاحیۀ بیروت
@Farsna</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/464766" target="_blank">📅 17:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464764">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sALiiOhFNMFTnuo5zjhSYMYFxm1X_cKFHmr5kmIMQ18HH73x1yE-zCq2-pwHe5c4Kdcl0RDQX576tJYTAXKXaETb-hyxSIg6NSmNY8eyFqcxQONzEIzPCqoaAzlBlt_In8atKAdAOeW_o5flL6dMFgG_7ZLRFWnmJAO_hYS9XlaoeFZT_DSdkVp4BL3Ww1ZGHUrH1aprBMKdw_OgMxblP1PfbOUgaT0InSBruPlmrHNHsafwdzgXT86da7Hy2UaMo4Ng8uDziwA-Xt1zT6YfOU9sh28aaKo-rGJ14TEwoKqaOesPajfXGlzM8M-n8AojKvsdC_jfAmaNQXVoa5Cfvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KCzukMd7h4uxmUbj2AIJ1o6X9JTHbe2Lyc90nkOHTFUTj1Kyv5o8sS4jJsL8CJCsK3wXsUdoAePLLplxhZns5hNYTapPAms2vC_NpmAUT2SNfw3-EvvFPQZVT-3xR64fz-chy36aguVDdaXO7ALKBqASz38w9PbQsbSnuoRNkSLmbQxWAKoMrbat4ZN1EWQdkG5Q3MGaPztStAcmg9VeoAQ9kbNLTpsdyVZ_mIxlBH4aNtUB5T9EEGUiqHBl4N1XNfZfH0-QkrQD-_GlIdUZM3CZcPHg-jm2bHiHbPpSDYyUdgEBM6cPuJRsUg7p5jPEZbDEjBmLigH4u5fSk1FV3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
نمی‌توانستم بر خلاف حرف امام عمل کنم
🔹
روایتی از حضور رهبر شهید انقلاب در لشگر محمدرسول‌الله در دوران دفاع مقدس
@Farsna</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/farsna/464764" target="_blank">📅 17:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464757">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33a13a9e9.mp4?token=habWHyfT7UC9bB2VYlaq650POkVRE_aWGWvtTP932PjEFckkGa8Ssdi_FsUBxijGVm86k7ax3UNoCMxZ0qMJAiWGIDAX3avng2jADFhdX8GuKZA6cHOH5B-7rPrAyhXcIdlSIQxEmJ9lj9wgnD1RwUuMp1nmPM7VlSytT66HGwHvHLxUsZ5gLgowR_NB3QpSTTFsYRsQvzDMCRiM3AL8j8XDkdmdO1Nwet7nKffDnLpWh3E-jJCsr3vfRzM4nOalTqxsecyilzCYqXcyyr0HM62EK5-7o4wt4hMh039XcKaaQAAXKNp1ocWvZiquHnc2txP4FgYV2YbYYMzwOp6MmopfbuNadozZ_TW1ZhuYx1txLe2AnSrnP-d2BWHX5DCbFc83HZH0mdlV45skWzntT_NXHKf3A9VhXv_LwuqIG3bI2vYu-gNych-_9NKMrucEHHs2uz0cnx_39WDjt3YlySkfciBVN1KZ79ls7XzmbNYRdpWCwVXpzmVZNPmtVSbzIx_F-n-cca60PuidHO0v13JC6BiLm58lRnN-WEZqRGanlcSMCGLdBQC-fHC7d69cSLqwhCahTkRJbYK2NJi59OdplYgcq0IEriaMYMjFzFTH30XgmCsiOVOIDwyR4-ejU02zpMxiRj4vR5Qfi7HlW6PofHuf-e_ElaMf2JrEsVs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33a13a9e9.mp4?token=habWHyfT7UC9bB2VYlaq650POkVRE_aWGWvtTP932PjEFckkGa8Ssdi_FsUBxijGVm86k7ax3UNoCMxZ0qMJAiWGIDAX3avng2jADFhdX8GuKZA6cHOH5B-7rPrAyhXcIdlSIQxEmJ9lj9wgnD1RwUuMp1nmPM7VlSytT66HGwHvHLxUsZ5gLgowR_NB3QpSTTFsYRsQvzDMCRiM3AL8j8XDkdmdO1Nwet7nKffDnLpWh3E-jJCsr3vfRzM4nOalTqxsecyilzCYqXcyyr0HM62EK5-7o4wt4hMh039XcKaaQAAXKNp1ocWvZiquHnc2txP4FgYV2YbYYMzwOp6MmopfbuNadozZ_TW1ZhuYx1txLe2AnSrnP-d2BWHX5DCbFc83HZH0mdlV45skWzntT_NXHKf3A9VhXv_LwuqIG3bI2vYu-gNych-_9NKMrucEHHs2uz0cnx_39WDjt3YlySkfciBVN1KZ79ls7XzmbNYRdpWCwVXpzmVZNPmtVSbzIx_F-n-cca60PuidHO0v13JC6BiLm58lRnN-WEZqRGanlcSMCGLdBQC-fHC7d69cSLqwhCahTkRJbYK2NJi59OdplYgcq0IEriaMYMjFzFTH30XgmCsiOVOIDwyR4-ejU02zpMxiRj4vR5Qfi7HlW6PofHuf-e_ElaMf2JrEsVs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض کاربران عراقی به لغو پروازهای ایران
🔹
در ادامه اعتراض مردم عراق به تصمیم دولت الزیدی درباره تعلیق پروازهای ایران، کاربران عراقی با انتشار پیام‌ها و تصاویر و ویدئوهای متعدد در شبکه‌های اجتماعی، تن‌دادن بغداد به دیکته آمریکا را محکوم کردند.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/464757" target="_blank">📅 17:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464756">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zw7k_V9Ec1bzJ-P6oSOWPjP0_D3e2_-IVS2MVC4FpFbfFozorAi-7YQ8tG4fG-xHU0ze-pWaTmXxSuoXKopMhLEs3zhSg9Otn1VlRg5x0QizKTWlG6cxv_VzGap0JDPwkw1h1gS88blbF9klSPP2UwAbMmNx5VuNsA0WRkjJOxYAB9GCtoaNbNTLOXF4Jny01Q5D-VsSQsbXqCxHv9hru44BgBNLGEz-XFqHvGpVMnXqAqD6nREcX2CD4ZY4Bs8mg3qnglG6G8gLQ73QTKcgD_BoOwHmMWvdA-QueAg7sfAmu1GB3CFLKFhEU_C_7eXWpPZ27aM1Nw8-q5GxmTYzyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاخبار: ضریح شهید سید حسن نصرالله عامدانه تکمیل نمی‌شود
🔹
دو سال پس از شهادت سید حسن نصرالله در حمله‌ای که با ۸۱ تن مواد منفجره محل حضور او را هدف قرار داد، سازه‌های اطراف ضریح او همچنان تنها اسکلت‌های فلزی هستند و در این مکان هنوز هیچ دیوار یا ستون بتنی ساخته نشده است.
🔹
فرزند شهید سید حسن نصرالله، در این‌باره می‌گوید «حتی اگر کسی با هزینه شخصی خود ساخت ضریح را بر عهده بگیرد، باز هم بازسازی آن تا زمانی که خانه‌های مردم جنوب، ضاحیه جنوبی و بقاع بازسازی نشود، متوقف خواهد ماند.»
🔹
شبکه الاخبار در گزارشی نوشته: چند ماه پس از تشییع سیدحسن نصرالله، به‌طور جدی فکر کردن درباره تدوین طرح جامع ضریح آغاز شد؛ طرحی که ابعاد مختلف و گسترده شخصیت سید حسن را بازتاب خواهد داد. هدف این است که ضریح فقط محلی برای دیدار مادی با سید نباشد، بلکه فضایی باشد که در آن اندیشه و روح با یکدیگر پیوند بخورند.
🔗
بخشی از این طرح، ایجاد موزه‌ای مرتبط با شهید نصرالله است
جزئیات بیشتر را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/464756" target="_blank">📅 16:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464755">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e9de6a68.mp4?token=VhHltxE_oZEIKulG7sdQy2Rb2CPy_Y2488Kr0tzDlGM495bLQLIJ-AUUqomDozdcy1j8Uq7_wD_TuTQYr3yY8aFfYXL9BLRmJq-vfWXYTvumz8LqXBjTc3b1oz5tf56oHkOmzvv3IheUM6gNt1a1EKEWhZqnerkpopCU9rcZSreFvQ0NnWhvp35Z4qcI0tkhcA2VGpfU7nNTZBOF4Ta26E2yAiIxD8t1gj80X1T9tywWMRRClTNKMvx8-2OZ21AZmO_u98QjmOenEq3RbgJAV1ipnT7noatbZ_930DBc2wNCdMGmLPLYlSWppL41moVOODR3aO67XTAg-CZrpcngZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e9de6a68.mp4?token=VhHltxE_oZEIKulG7sdQy2Rb2CPy_Y2488Kr0tzDlGM495bLQLIJ-AUUqomDozdcy1j8Uq7_wD_TuTQYr3yY8aFfYXL9BLRmJq-vfWXYTvumz8LqXBjTc3b1oz5tf56oHkOmzvv3IheUM6gNt1a1EKEWhZqnerkpopCU9rcZSreFvQ0NnWhvp35Z4qcI0tkhcA2VGpfU7nNTZBOF4Ta26E2yAiIxD8t1gj80X1T9tywWMRRClTNKMvx8-2OZ21AZmO_u98QjmOenEq3RbgJAV1ipnT7noatbZ_930DBc2wNCdMGmLPLYlSWppL41moVOODR3aO67XTAg-CZrpcngZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تلما ۴ قلو زایید
🔹
دبیر انجمن صنفی کارفرمایی حفاظت‌گاه‌های خصوصی حیات وحش: مشاهدهٔ یوزپلنگ مادهٔ «تلما» به‌همراه ۴ توله در حفاظتگاه مشارکتی یوزکنام، تعداد یوزهای شناسایی‌شده در کشور را به ۳۱ قلاده رساند.
🔹
بررسی‌های نشان می‌دهد این توله‌ها متعلق به زادآوری امسال هستند و متخصصان سن آن‌ها را حدود ۳ تا ۴ ماه برآورد کرده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/464755" target="_blank">📅 16:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464754">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">یمن بازهم یک پهپاد سعودی را ساقط کرد
🔹
سخنگوی نیروهای مسلح یمن: یک پهپاد شناسایی کارایل متعلق به دشمن سعودی درحین عملیات در آسمان منطقۀ الطینه در استان حجه سرنگون شد. @Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/464754" target="_blank">📅 16:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464753">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09eff2052a.mp4?token=tGf2W9RxxELhMU-J0F-v3JbuGipZ0gC2Tw62Zr5w2AnBxf-A5_c9ozR2yW5TDkfV_a2lcpgbgs0Vggyy9gKsbitkarHAFcj40edo-4xfAE02Qb9TWNX2X6q0vC0X6J1VyKVtzHkr4hOuqdE6njSU0G7lLD3KwgSsIsp-CcV4FpzIG5-ZwtEgGrV873cfP5NScfpLcFKKnnuWk3GEuJNoiOAluMQZnU61iryDkYpTdw2xEaUrk9HTg06znR4N8S7v5vHbTuR2csvHrsxn0QCu647OJ8SZ324v9W4cI9aoBrsKcF1uvcE1e3EgvtwrGjE16PtFFmx5vH16aeIJNlNqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09eff2052a.mp4?token=tGf2W9RxxELhMU-J0F-v3JbuGipZ0gC2Tw62Zr5w2AnBxf-A5_c9ozR2yW5TDkfV_a2lcpgbgs0Vggyy9gKsbitkarHAFcj40edo-4xfAE02Qb9TWNX2X6q0vC0X6J1VyKVtzHkr4hOuqdE6njSU0G7lLD3KwgSsIsp-CcV4FpzIG5-ZwtEgGrV873cfP5NScfpLcFKKnnuWk3GEuJNoiOAluMQZnU61iryDkYpTdw2xEaUrk9HTg06znR4N8S7v5vHbTuR2csvHrsxn0QCu647OJ8SZ324v9W4cI9aoBrsKcF1uvcE1e3EgvtwrGjE16PtFFmx5vH16aeIJNlNqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ: به محض اینکه ایران تسلیم و جنگ تمام شود، قیمت نفت سقوط خواهد کرد!
@Farsna</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/464753" target="_blank">📅 16:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464752">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‌‎  خاموشی‌های شهر پرند با آغاز پاییز هم ادامه دارد
🔹
با وجود آغاز فصل پاییز و تأکید وزیر نیرو بر پایان خاموشی‌های برنامه‌ریزی‌شده، ساکنان شهر جدید پرند در استان تهران همچنان با قطعی مکرر برق، چه در قالب برنامه اعلام‌شده و چه بدون برنامه مواجه‌اند. @Farsna…</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/464752" target="_blank">📅 16:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464751">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIcB_ghjnViSRd9pGO5TZzMIUEIrw_vlC-ralMWJGRL2FoEHmi4Kea40ZdX2Lkto9v2tqxB-8V-hmZhlRldZKwE-sZYxVtd6aqS-1vo2cJClJv_FPepLTcSHdueBk8ZyKSUg9nSU9rS318nuC5kmfEg87KHbwHI_bsWLb6cEUk9shD8Oe1nBzhxN8vfl7XibEq_rAePGhsFc09aU2y2zEpBMMfaP_SHt31h8QD6atGv2_gBeLOP9Fp8C22U-xyDs6iui4BzMMys4DejVuBmHPsXHuWY3EHQ12Sl8ORz2zfIyu3h_VP1jm0cg8e9aweERrrQRMFm37_XjHHKAgdtErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس پلیس راهور: تردد خودروهای دارای پلاک مناطق آزاد کیش و قشم تا پایان آذر در سراسر کشور مجاز است
🔹
سردار تیمور حسینی: صاحبان خودروهای دارای پلاک سایر مناطق آزاد برای خروج از محدودهٔ مصوب باید با هماهنگی سازمان‌های مرتبط، مرخصی و پلاک گذر موقت دریافت کنند.…</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/464751" target="_blank">📅 16:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464750">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOIxYKi47J0fIshXGnv_hB0rnE5-9K3rBRsoaI75D3GPgRBsnjHoWqJ3X1RkWvcBGKGxvDL5PQSjhLlD8kou9LIfw7j0rqsWUtn-pZqq-14d_QDBBgZ18T202HQ0Hu-pjNes5yQivhikRCkMEmnnQjzGHZ1D02momnZ0dOZpq6xn0ZQhJQJPHTmTCf259xYHYY1OfQKA0wDYFhko5hzPdRDEzm3sFuk3NJu6qxF6lZ7dteSI1lMD4LqlykgQFFsqSkgxEWG85tWvTH24tYuauAcnEuR3oD1N5HSnjXd2UvY0ffq0pJzNFsTfctG9reNlSjyZ4CovRIaN9FNbUVnS9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن: ۳ پهپاد و ده‌ها نیروی مزدوران سعودی را منهدم کردیم
🔹
مقام نظامی یمنی:‌ نیروهای دشمن سعودی که قصد انجام حمله در منطقه الوازعیه را داشتند را دفع کردیم.
🔹
در این عملیات ۳ پهپاد دشمن منهدم شد و ده‌ها کشته و زخمی در میان نیروهای دشمن سعودی به‌جا ماند. @Farsna</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/464750" target="_blank">📅 16:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464749">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Un-VQh8O_aV3u3ax_8ICCSeKV9nVZWWv9rrHjuywurBWTN56Rnfk-Rh4Lqw2GtOp0W2x3ZH47QjyiEMmwp-mMxuv1sQFnC66_BWlpb2mQzN2GfIUnHeJvUO3f1Zb5lCFbXEMu-_z96NfMwlYBvg9tXTzXkrB9heUn9w33epjLPiq1SEfJxjEvAZDRlPknvlf4Iy4kns5d_JR6_KMLfLI49ZFLkhQbn0_cEbHbiGVbSz13CU7OJ6ZYBvsIfxocf1Da0aLXgvzCE8Y8uL6i9Kp-Z58_ctABBC44IzPfDkux-tvQa4wrPUBW7aTwK3n3jghqM3EptlRl7YQvRLAySV2Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر صفوی: روند شکست‌های راهبردی آمریکا ادامه خواهد داشت
🔹
کنترل تنگۀ باب‌المندب توسط انصارالله هم یک گام دیگر در شکست بزرگتر آمریکا در منطقه خواهد بود و روند این شکست‌های راهبردی آمریکا ادامه خواهد داشت.
🔹
رئیس‌جمهور بی‌عقل آمریکا باید بداند که ایران شکست‌ناپذیر است و یک تمدن چند هزار ساله و یک ملت شجاع دارد.
🔹
آمریکایی‌ها رفتنی هستند و نمی‌توانند در منطقه بمانند؛ آنها صد‌ها میلیارد دلار هزینه کردند، اما شکست خوردند؛ این کشور در ترتیبات امنیتی منطقه نقشی ندارد و ایران ترتیبات امنیتی و آینده امنیت منطقه را رقم خواهد زد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/farsna/464749" target="_blank">📅 16:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464748">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/098ae7f6ba.mp4?token=KEHpMB5l40ownlFREpEFAlOFMKfqziqLWqF0M8V1NOhvTVTHZultmv9K9CaKdnq2kUvYiC7lF5ZaaH3kre3KcqwmBPJLC-OVm4-R_cuHBppx3Nk2hPuepGLKHo2GtvED8i4Qg7k2FH2-dSahhC725OzgSvXQ0gTlqhy9THO5zCcbwgRB1HMTkXJmr-yeNtNjh2NxMuDJSC1GKdUfB9mUxlWJj2r5vuspQfRNfxzsoTbL3GoX9hRpZwdDPybSEo3Y4pdwQGYeCdrEk8oYMVh3ldsLVBNZ9kkGkXy7Hp95e-jhFG2HP7DJxVv4_JqnPVv15fHQvGETbg_mJubqsCdLFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/098ae7f6ba.mp4?token=KEHpMB5l40ownlFREpEFAlOFMKfqziqLWqF0M8V1NOhvTVTHZultmv9K9CaKdnq2kUvYiC7lF5ZaaH3kre3KcqwmBPJLC-OVm4-R_cuHBppx3Nk2hPuepGLKHo2GtvED8i4Qg7k2FH2-dSahhC725OzgSvXQ0gTlqhy9THO5zCcbwgRB1HMTkXJmr-yeNtNjh2NxMuDJSC1GKdUfB9mUxlWJj2r5vuspQfRNfxzsoTbL3GoX9hRpZwdDPybSEo3Y4pdwQGYeCdrEk8oYMVh3ldsLVBNZ9kkGkXy7Hp95e-jhFG2HP7DJxVv4_JqnPVv15fHQvGETbg_mJubqsCdLFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای فیلم جنجالی ورود اتباع به ایران چه بود
🔹
در روزهای اخیر انتشار ویدئویی با ادعای هجوم غیرقانونی تعداد زیادی از اتباع افغانستانی به مرزهای خراسان‌رضوی در فضای مجازی خبرساز شده است.
🔹
حالا مدیرکل اتباع این استان می‌گوید: «امکان تایید یا رد چنین ادعایی وجود ندارد و نمی‌توان دربارهٔ صحت آن نظری داد.
🔹
بررسی‌ها نشان می‌دهد در ماه‌های گذشته با وضعیت اقتصادی افغانستان، آمار ورود مهاجران غیرقانونی بیشتر شده اما حجم ورود مهاجران، آن‌قدر زیاد نبوده که در فیلم نشان می‌دهد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.68K · <a href="https://t.me/farsna/464748" target="_blank">📅 15:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464747">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مهلت تعیین‌تکلیف وزرای ۲ وزارتخانه به پایان رسید
🔹
سخنگوی هیئت‌رئیسۀ مجلس: براساس اصل ۱۳۵ قانون اساسی، رئیس‌جمهور می‌تواند برای وزارتخانه‌های فاقد وزیر، حداکثر به مدت ۳ ماه سرپرست تعیین کند.
🔹
دولت از ۱۹ مردادماه با اذن رهبر انقلاب، ۴۵ روز فرصت داشت تا تکلیف وزارتخانه‌های اطلاعات و دفاع را مشخص کند.
🔹
این مهلت اکنون به پایان رسیده و دولت باید گزینه‌های پیشنهادی خود برای تصدی این دو وزارتخانه را به مجلس معرفی کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/464747" target="_blank">📅 15:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464746">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f1bcd111b.mp4?token=f6HHhb8Z_M9R4ett19H-Dq83zre89P7viPaZNBTmnRfL7ynoIVGRUPZhA9WSZmhf4s9viyLtkPLIFAhGJk1FjJcos2lKSIr6jtwr8GoVG6imvshsncdLypaV_3Cg5wW3AUXtM7xYYi3EmfB6uyvHjTJt7VNrxHtY1-zTGgx_2WRBTXTRF0-UAQM6ZYzB5Ew3OINMD63W3Gjgj0ERbPhmMLJ_4CGWu5EzWQtvrPH5YDtLGFXPtNUSX3MjoAMz5pZxUGP96jF3YIrpCH8slbMIoqyRcSW4KM5CR6Xscpph4OMBX6JKEH4j5aBxlUp5Skej5kubCKq89NpRpEYNtIAlDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f1bcd111b.mp4?token=f6HHhb8Z_M9R4ett19H-Dq83zre89P7viPaZNBTmnRfL7ynoIVGRUPZhA9WSZmhf4s9viyLtkPLIFAhGJk1FjJcos2lKSIr6jtwr8GoVG6imvshsncdLypaV_3Cg5wW3AUXtM7xYYi3EmfB6uyvHjTJt7VNrxHtY1-zTGgx_2WRBTXTRF0-UAQM6ZYzB5Ew3OINMD63W3Gjgj0ERbPhmMLJ_4CGWu5EzWQtvrPH5YDtLGFXPtNUSX3MjoAMz5pZxUGP96jF3YIrpCH8slbMIoqyRcSW4KM5CR6Xscpph4OMBX6JKEH4j5aBxlUp5Skej5kubCKq89NpRpEYNtIAlDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زارعی در دوی ۴۰۰ متر نقره گرفت
🔹
زهرا زارعی در فینال دوی ۴۰۰ متر دوومیدانی بازی‌های آسیایی ناگویا با ثبت رکورد ۵۲.۳۸ ثانیه در رتبه دوم قرار گرفت و به مدال نقره دست یافت. @Farsna</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/464746" target="_blank">📅 15:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464744">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZQI7TpRypBDRcBIJ_KvkSwObYgiv44aT4L6e6SHx2rAn3xwWwN2z9q5lpguvcq-2Z0ZKmsMy-1Y2eVLtkGzzgmRVzpigLfBfsaI5a4J4Igpqbr73DOAv2YbU2lqeGxy-FVyiSCywuXaoMvDoETHTNUfNg7kkaDUpvyn1KzDJ2uSZB8Y3ENpaAyjMCC2L8EpsUt9KJXTHUsvEVHNgsMMYst_sIZ0YCJu4w-vM_v5IL3la1JMqs3iYZIFazHO46-sSIDwJAK0SoDXi9o_otET78r5ff3gm2mqyF9Df28P68YmmA80SveE_vvsgvviGaFkK6eyMA8_CUqPW6Y7Hq0CDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عبور کابل‌ها از تنگه هرمز منوط به مجوز ایران می‌شود
🔹
نایب‌رئیس کمیسیون امنیت ملی: مادۀ ۱۰ طرح راهبردی تأمین امنیت هرمز به زیر و بستر دریایی، ازجمله عبور کابل‌ها و تجهیزات انتقال داده‌ها اختصاص دارد.
🔹
این ماده در یک کمیتۀ ویژه باحضور مسئولانی از وزارت اطلاعات،…</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/464744" target="_blank">📅 15:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464743">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ada5d8dc1.mp4?token=FN5hxOl-tloJQF1qp7FC68H3Lxb7bKgJaRp8Mtu1I03VXEg4rxnOhjh6adj5WvIT6DZBdFTzbjbrvqL_Q4vYDIO4uBe8zj9tmRpS2Dvx4zzG03wiFjVrM7N7RufcsM2qdbRjR6dzEUTfeQs88aOYRDo-EWKv_LXB7JSIprXxpFvvSbyYbQfqJV1dMnI9N87qVkgJPpeGX3PgcThC__tDaze8Ww2gWP6m3xdPhbWdTEeM1djPXTsItZEZQJU7W6slPlXHXzC_DTQyKGVgYAL9KFKQBmU5P_ywm5iV1n9zwMv84gOruLpIryaeX3e2SwB3-xercjyjgdoAtPW614QWYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ada5d8dc1.mp4?token=FN5hxOl-tloJQF1qp7FC68H3Lxb7bKgJaRp8Mtu1I03VXEg4rxnOhjh6adj5WvIT6DZBdFTzbjbrvqL_Q4vYDIO4uBe8zj9tmRpS2Dvx4zzG03wiFjVrM7N7RufcsM2qdbRjR6dzEUTfeQs88aOYRDo-EWKv_LXB7JSIprXxpFvvSbyYbQfqJV1dMnI9N87qVkgJPpeGX3PgcThC__tDaze8Ww2gWP6m3xdPhbWdTEeM1djPXTsItZEZQJU7W6slPlXHXzC_DTQyKGVgYAL9KFKQBmU5P_ywm5iV1n9zwMv84gOruLpIryaeX3e2SwB3-xercjyjgdoAtPW614QWYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۷۰ درصد دریافت‌کنندگان پیوند سلول‌های بنیادی به‌طور کامل بهبود یافته‌اند
🔹
هم‌اکنون بین ۵۰ تا ۶۰ نفر در صف دریافت پیوند سلول‌های بنیادی هستند.
@Farsna</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/464743" target="_blank">📅 15:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464742">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c38d61012.mp4?token=oRElhguQIA7pNpRrIyO7PHERFx3Zdq5HklSO_D_aPGCgD_A7bTBkWO1DuJAR-cJhLK_Xc2VuEGBIWM-pQX7iAsGg_TjS1WjwUR8YjKTWX18WCKPnEVhnECilc9U6OvNqnytZIXR2yuF70Un_8oNgaeMzb5KIEO6ifznJkx0LvkVR2eYUZzTiuJdcPUt2SSfS7fmOzhYiLUUrJBT3EDNZ6vYfBU_4yGO-aSHoOZvRELPDdo18EgCKROWb8yDoB1qvkFd_kfuTd_MdRIWeEPiJRmNqyw-Dp97fNmkRAbM6GN0WcOppBk4SkR0Zc7Yx6Q0dsR3gOysPQWcJ38cu--WwzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c38d61012.mp4?token=oRElhguQIA7pNpRrIyO7PHERFx3Zdq5HklSO_D_aPGCgD_A7bTBkWO1DuJAR-cJhLK_Xc2VuEGBIWM-pQX7iAsGg_TjS1WjwUR8YjKTWX18WCKPnEVhnECilc9U6OvNqnytZIXR2yuF70Un_8oNgaeMzb5KIEO6ifznJkx0LvkVR2eYUZzTiuJdcPUt2SSfS7fmOzhYiLUUrJBT3EDNZ6vYfBU_4yGO-aSHoOZvRELPDdo18EgCKROWb8yDoB1qvkFd_kfuTd_MdRIWeEPiJRmNqyw-Dp97fNmkRAbM6GN0WcOppBk4SkR0Zc7Yx6Q0dsR3gOysPQWcJ38cu--WwzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم آمریکا از اوضاع زندگی‌شان بعداز گران‌شدن سوخت می‌گویند
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/464742" target="_blank">📅 15:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464741">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxLrMvET5AetMugRdEe24_nTHYNTQcUcY2Ab4wJXQSWp5-iuy3grhMYb3yHerZvk7mcfqIzJTJvKGghSllsRUKRocQ-5gDQ-QVZBZz30ezPa3hFnAA4Qqlwfv6trG2mGhO2sov3J9pxh-kltNVAdguqZiAEa7ue6VJxOHFL14M7N_BEn8SOIP-F82g5dNqkr9HqjTMPJI-9eFh2BMi0V5tLxzx0QzAwo-A-9c81DYvci7MpjyCXOMkpXrhJ7sxWgRFIx2F1WiD-od4_oz0BknbPOfQ1_XmwCUXql5fLm4_WVLpDYbVyrRhBKQATVJz-1Cu0fZ7ScVl9vOWK-cOazpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
مسیر شتابدهی استارتاپ‌ها در ویستا آغاز شد
🔸
هلدینگ سرمایه‌گذاری ویستا، در ادامه توسعه فعالیت‌های خود در اکوسیستم نوآوری و سرمایه‌گذاری خطرپذیر شرکتی، بخش شتابدهی استارتاپ‌ها را به خدمات خود اضافه کرد.
🔸
ویستا که از سال ۱۳۹۶ در حوزه سرمایه‌گذاری در کسب‌وکارهای نوآور فعالیت می‌کند، با راه‌اندازی این بخش، امکان همراهی با تیم‌ها و استارتاپ‌ها از مراحل ابتدایی توسعه کسب‌وکار تا ورود به بازار و رشد را فراهم کرده است.
🔸
در این مسیر، حمایت از استارتاپ‌ها تنها به تأمین مالی محدود نیست و در قالب «پول هوشمند»، مشاوره تخصصی، شبکه ارتباطی، منابع عملیاتی و ظرفیت‌های مرتبط با ایرانسل نیز در اختیار کسب‌وکارهای منتخب قرار می‌گیرد.
🔸
تیم‌ها و استارتاپ‌های نوآور می‌توانند با مراجعه به بخش شتابدهی
وب‌سایت ویستا
، اطلاعات خود را ثبت کرده و برای ورود به فرایند ارزیابی و جلسات هدایت‌گری (Mentoring) درخواست دهند.
👈
جزئیات بیشتر
@irancellnews1</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/464741" target="_blank">📅 15:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464740">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمنطقه‌فرهنگی‌وگردشگری‌عباس‌آباد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eE74KMA1aJdSib1QAFgprX-GNq2uaS9tWgQj2nOfMXa_MvH7BZR-8ZdZ5m4Hx8FI6JIg7Yej-OmNKLugH4DFwsmTgXvJvqC2gCEvdJF0re9r4C_Y0S2hPEQ9ADgEf6tVRvoeQmEXcCWafkRVeJAYH3XL0D1PuFppPpf_3LyaKkwJwU4vgiXtmBmA8FTHeTFvHMwpogKmEnZkHUPmjg3RH89NKav4tIq9xkcwrZsYCSwLlcLkhTWqqh51AZ1ZKdtoQV9FUvorXOsnqaqnKYTpv7QgiLgHkddfNeB_txFsfsBWLQ5v3EkKAUFwI3tXps3_xufpmBSQn70Ev6fvXO5Mew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
فراخوان نخستین مسابقه بین‌المللی نقاشی «سورنا»
با موضوع «ایران از نگاه کودکان»
🪅
کودکان و نوجوانان ۶ تا ۱۸ سال می‌توانند با موضوعاتی مانند فرهنگ و خانواده، خاطره، رویا، امید، دوستی، صلح و آینده ایران در این مسابقه شرکت کنند.
🗓️
مهلت ارسال آثار: ۲۲ مهر ۱۴۰۵
🏆
معرفی برگزیدگان: ۲۹ مهر ۱۴۰۵
🎭
تکنیک خلق آثار آزاد است و در بخش نوجوانان، امکان ارائه آثار مبتنی بر واقعیت افزوده (AI) نیز فراهم شده است.
📌
ارسال آثار و اطلاعات بیشتر:
sorena-competition.com
🆔
@abasabadecopark</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/464740" target="_blank">📅 15:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464739">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/464739" target="_blank">📅 15:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464738">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c25457b08.mp4?token=DT8qPc83qa_QuNw1LCjR8g5kJxnjt0l3k3y-xaAsCFqFZ3FXL7W9tLPmeYBFN535AkbqjyOUp9b5Z6LXxQvpueFEULSUT6KYJKWBJO5nVR24ga6zEDDZuU6XCXo-dxtbKIYkQ2xqcrIUQihG3C3IhdaOs3G43hvjUo-Lb8EIxvYW7vJYrUsQQlreXUQHuS-1oy9MoqfCpjfL2BmELBP6Txt4WzdmtmbE55lihi_5rujGBtRE9Pkx71EEv4eSvQCvn2F0kpto6BYe2WM8iDAz6mUL_Xysrv1sbryqCa05_59uD1sDvQF6dQI9WhaHgv9inYKZc9FjO0OpgW5H5T-USA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c25457b08.mp4?token=DT8qPc83qa_QuNw1LCjR8g5kJxnjt0l3k3y-xaAsCFqFZ3FXL7W9tLPmeYBFN535AkbqjyOUp9b5Z6LXxQvpueFEULSUT6KYJKWBJO5nVR24ga6zEDDZuU6XCXo-dxtbKIYkQ2xqcrIUQihG3C3IhdaOs3G43hvjUo-Lb8EIxvYW7vJYrUsQQlreXUQHuS-1oy9MoqfCpjfL2BmELBP6Txt4WzdmtmbE55lihi_5rujGBtRE9Pkx71EEv4eSvQCvn2F0kpto6BYe2WM8iDAz6mUL_Xysrv1sbryqCa05_59uD1sDvQF6dQI9WhaHgv9inYKZc9FjO0OpgW5H5T-USA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زلنسکی بالاخره از غرب ناامید شد؟
🔹
رئیس‌جمهور اوکراین که از ابتدای جنگ اوکراین از آمریکا و اروپا کمک خواسته، امروز پیامی تازه درباره جنگ با روسیه منتشر کرد و این بار از چین، هند، برزیل و کشورهای «جنوب جهانی» کمک خواست.
🔹
به روایت ولودیمیر زلنسکی، «طی هفته گذشته، روس‌ها بیش از ۲۲۰۰ پهپاد تهاجمی و همچنین حدود ۱۶۵۰ بمب و ۳۸ موشک از انواع مختلف به سوی اوکراین شلیک کردند که بخش قابل‌توجهی از آن‌ها موشک‌های بالستیک بودند. متأسفانه دیشب نیز در پی حملات روسیه، شماری از افراد جان باختند.»
🔹
زلنسکی گفت: «ما به‌طور مداوم با اروپایی‌ها، آمریکا، کانادا، ژاپن، استرالیا و سایر شرکا برای تقویت توان دفاعی و پیشبرد دیپلماسی واقعی همکاری می‌کنیم. اما متأسفانه، آنچه جای خالی‌ آن احساس می‌شود، اتخاذ موضعی قاطع و پایدار از سوی چین، هند، برزیل، آفریقای جنوبی، کشورهای گروه ۲۰ و "جنوب جهانی" است.»
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farsna/464738" target="_blank">📅 15:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464737">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d71131b6.mp4?token=WOADt8qPF3ZjSNk2yxZwLGM9LR3nsIZbkFjGNjlB3TnSQOkd3p7HxTepahwtj7R2GsW5vRb7Yq8SfTW318nyxt6ytfuXZtiI44XftpY4Rbg5WcVhtDUhXt1iyRv-Tcw788Xf_BJtjPlaB0ZKBQzy1wXo_fSSefM0gTua6_Hl8oRiljTOKepQQL0pgM1q2-DyMzCDseqPGegjQx90vBOgrAwTqKC2Y4EdigFUhCx4uXyFUgmoTdTQeteBtUQUqWjnF7DFjf07kg8zDMFbiToxrXyGDsG-yBb-bJ-U_u356p4twl-O8uuNF-s5CDhikj-wQV5h_bBCIvIOXeJvbmWO9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d71131b6.mp4?token=WOADt8qPF3ZjSNk2yxZwLGM9LR3nsIZbkFjGNjlB3TnSQOkd3p7HxTepahwtj7R2GsW5vRb7Yq8SfTW318nyxt6ytfuXZtiI44XftpY4Rbg5WcVhtDUhXt1iyRv-Tcw788Xf_BJtjPlaB0ZKBQzy1wXo_fSSefM0gTua6_Hl8oRiljTOKepQQL0pgM1q2-DyMzCDseqPGegjQx90vBOgrAwTqKC2Y4EdigFUhCx4uXyFUgmoTdTQeteBtUQUqWjnF7DFjf07kg8zDMFbiToxrXyGDsG-yBb-bJ-U_u356p4twl-O8uuNF-s5CDhikj-wQV5h_bBCIvIOXeJvbmWO9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه: اگر تنگۀ هرمز متعلق به آمریکاست، پس ناوهایشان کجاست؟
🔹
معاون سیاسی نیروی دریایی سپاه: اگر ترامپ تنگۀ هرمز را تنگه خود می‌داند، پس چرا ناوها و شناورهایش اینجا نیستند؟
🔹
اگر آمریکا مدعی کنترل تنگۀ هرمز است، فقط یکی از ناوهای خود را به این…</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/farsna/464737" target="_blank">📅 15:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464736">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91d03fc573.mp4?token=CPfRYaD0fiJIoiudfCise3J_VVMblwEuGibS79iVuLGQ58NJ7XBz8P3Gnfvyabq0onbFM9FfbshsDGgjVvw_3FAK9fNHSJ0RZKIAwiCJIOa71UKrTjmdX8t0CtD4zBayiAKNxHUJW9tN2sx7ywIgXDMO84615qHhCB9b-2qodZKYXjyl8l8iRvInF95rGHCLwxAB7FBn9v9MPqbbT-4mwCfmiV6_g6xuPZOnvWkWEmOPd7hkfwPtuGZyL5KiITmgtSzmAs9LLTOvmNnNCDrZQaYcdx7ig6Iw1qemdWypt2vEuBe3giXQ-HCOhK8XE7tgc_cW4PfCWdrxB-QcNbAvlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91d03fc573.mp4?token=CPfRYaD0fiJIoiudfCise3J_VVMblwEuGibS79iVuLGQ58NJ7XBz8P3Gnfvyabq0onbFM9FfbshsDGgjVvw_3FAK9fNHSJ0RZKIAwiCJIOa71UKrTjmdX8t0CtD4zBayiAKNxHUJW9tN2sx7ywIgXDMO84615qHhCB9b-2qodZKYXjyl8l8iRvInF95rGHCLwxAB7FBn9v9MPqbbT-4mwCfmiV6_g6xuPZOnvWkWEmOPd7hkfwPtuGZyL5KiITmgtSzmAs9LLTOvmNnNCDrZQaYcdx7ig6Iw1qemdWypt2vEuBe3giXQ-HCOhK8XE7tgc_cW4PfCWdrxB-QcNbAvlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پزشکیان: ایران یک میلیون اثر تاریخی دارد؛ آمریکا چند اثر تاریخی دارد؟
🔹
آن‌وقت آنها می‌خواهند ما را با این سابقهٔ تمدنی و آثار تاریخی که ریشه در تمدن دنیا دارد، محو کنند.
🔹
ما این تاریخ را دوباره خواهیم ساخت و با سربلندی از این بحران‌ها خارج خواهیم شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/464736" target="_blank">📅 15:07 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464735">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f5c577e62.mp4?token=hnxbHnos4HxWbyRzOHXcHAzrMFZ1BGBHrJE8acjI8nD9CbRjIzGPZWxDJhzYAlF7g3W1vmqWR7VEtlKUEADGzQhd4JxXEW2s30mnq5H7kJGMA-XASPjhwA5kxBZGfh_VPBm4cH6uLgbEhrRr2tf9Kbf10Qo0KowHr7IeadAVx9ToHDKE7R1bacXnjBoJb7-ZOzIgtSCC6NbAIaqvnOGuV4Slh78zPVKr5n5rGWt1DcITvPwsZIG2vmMADN3KOAKVrwLLGpKGgA9tTrMWYQPuf-g1lNC_4v5l271B6XieV6vdOIwsNcit1nSn5vqmOQSgyvkXiDxHISphFXFgMVV4uRkg_c1nTnq-9Xz0wm48NoDw-3kasOqyoT6uAGZMW3JfGf5tmVKtFdtsaVyFSbGbQadSMTeQFAJoMxHgsCkqo6yN-Q1DJeLwn0AKFq8oyPnZK-E1tADYocR7-gcq0_vj-Aw6UCc5XxAKNgr9R44gTRvxOVKajgFwT3RVUCcnniK6JCQRqw-38JTbQQBI8Pch6BPeAFilG3_X6scupRcV4sg_gwwpOXMD6P19VSq0JsX1YV70vqE0zvKjOYOIahXmGM-MwWtm11K-PKTSchPLggemJdaatS2U4Qz0Tb3uQ9HCA7MgsdNawaLcPhEunJhAcGUIhHVb6oX1hxnB7DvjcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f5c577e62.mp4?token=hnxbHnos4HxWbyRzOHXcHAzrMFZ1BGBHrJE8acjI8nD9CbRjIzGPZWxDJhzYAlF7g3W1vmqWR7VEtlKUEADGzQhd4JxXEW2s30mnq5H7kJGMA-XASPjhwA5kxBZGfh_VPBm4cH6uLgbEhrRr2tf9Kbf10Qo0KowHr7IeadAVx9ToHDKE7R1bacXnjBoJb7-ZOzIgtSCC6NbAIaqvnOGuV4Slh78zPVKr5n5rGWt1DcITvPwsZIG2vmMADN3KOAKVrwLLGpKGgA9tTrMWYQPuf-g1lNC_4v5l271B6XieV6vdOIwsNcit1nSn5vqmOQSgyvkXiDxHISphFXFgMVV4uRkg_c1nTnq-9Xz0wm48NoDw-3kasOqyoT6uAGZMW3JfGf5tmVKtFdtsaVyFSbGbQadSMTeQFAJoMxHgsCkqo6yN-Q1DJeLwn0AKFq8oyPnZK-E1tADYocR7-gcq0_vj-Aw6UCc5XxAKNgr9R44gTRvxOVKajgFwT3RVUCcnniK6JCQRqw-38JTbQQBI8Pch6BPeAFilG3_X6scupRcV4sg_gwwpOXMD6P19VSq0JsX1YV70vqE0zvKjOYOIahXmGM-MwWtm11K-PKTSchPLggemJdaatS2U4Qz0Tb3uQ9HCA7MgsdNawaLcPhEunJhAcGUIhHVb6oX1hxnB7DvjcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۰ شب از حماسهٔ ملت ایران می‌گذرد
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/464735" target="_blank">📅 14:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464733">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k3wbeOMPJ8pHT1odIjyVcrH24Q7c_kVHMrTUzjxzyo6o4OphWP6W8DzyghS0BmNtAAGBNx9MMf1alLT716JY-gXB1RGv55TseSdq28fh3sgg6HuE_8vU6iiOfV1TsePoCDnIEGivAMxrD7i7uXI9x6PFyxzDaQqjmxUaGq0z3wD78xAHzeaqBb8Y7jodhrD0qarcwGVfpTn8comTKeYaaAgfXqmiCwWZ2rUDGB9sOs265uwIiIO8pl1OoVt0ee_f4dmOnypCPRaHbW1TCoQTctSDFqrlVrLzL2HkIfvocmcv9RUuRSChIAc6zOcDf8qaw9tv7BZec9hICN4yPq48wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7089848316.mp4?token=TWLi57L3uuDBB_CVFEeAvc94t6Xb1qrhQfkOUYH-pxGYS11svKADe2FO9pru9Yz0E6ZjXs9GHK7TwT5o6upnaefGimuclQZAdxlXDf236O4EoCemGQPe5VmV8tQ_JnG_8v8AN43mvVwmD2qn86xDVVvETk5NDncy_KL9ZWKw7sW7HmFt-5r3LyjKo_0xT_76llbgXApx7cj4DToAlY4Q8P8n3GCU8WkS_iWvWS-CZkyUzr973sX7oM-2_Sc2V6h0r0VWdyebi0lExSYeBQuM5Uy6TvEXaMMiVw1lRh8RnADwZIn2ZS5M34wSxbAJBk5T3saHeYB2BrGZG28eR0xueA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7089848316.mp4?token=TWLi57L3uuDBB_CVFEeAvc94t6Xb1qrhQfkOUYH-pxGYS11svKADe2FO9pru9Yz0E6ZjXs9GHK7TwT5o6upnaefGimuclQZAdxlXDf236O4EoCemGQPe5VmV8tQ_JnG_8v8AN43mvVwmD2qn86xDVVvETk5NDncy_KL9ZWKw7sW7HmFt-5r3LyjKo_0xT_76llbgXApx7cj4DToAlY4Q8P8n3GCU8WkS_iWvWS-CZkyUzr973sX7oM-2_Sc2V6h0r0VWdyebi0lExSYeBQuM5Uy6TvEXaMMiVw1lRh8RnADwZIn2ZS5M34wSxbAJBk5T3saHeYB2BrGZG28eR0xueA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم صهیونیستی شهرهای المنصوری و حداثا در جنوب لبنان را هدف حملات هوایی قرار داد.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/464733" target="_blank">📅 14:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464732">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/433e887041.mp4?token=PDOcL4byf5bi9ZxrDnJ6acE4AI_S6POd39vGTozCDLEO8VL0WBOyH2tc8h2X3Q5EHoQ1yVfig8pG_PlCSZtjydekqFpoaRlno3XpAJDtZ1m5YshoEyOeG_PJWORU8Our4gUoQmu2uzxbtzRHE30cvHGj3GxBIH-O6hyTeEFbM0UNUOo2kqJGytKuzBjiS8rw7scMOqOZ4VZK2fTPd4Ojb4reElVRtDxVskI4ROvOsGGsiKF14LvefP-GGs-dUeV0myQ-yF_XZphbKZh9kXyr-AWdEcIR_THl81_VtDFHH6kTb6ac2V8CE2029YUVU95tg2YvaMe4GVQSA4ScKbOWyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/433e887041.mp4?token=PDOcL4byf5bi9ZxrDnJ6acE4AI_S6POd39vGTozCDLEO8VL0WBOyH2tc8h2X3Q5EHoQ1yVfig8pG_PlCSZtjydekqFpoaRlno3XpAJDtZ1m5YshoEyOeG_PJWORU8Our4gUoQmu2uzxbtzRHE30cvHGj3GxBIH-O6hyTeEFbM0UNUOo2kqJGytKuzBjiS8rw7scMOqOZ4VZK2fTPd4Ojb4reElVRtDxVskI4ROvOsGGsiKF14LvefP-GGs-dUeV0myQ-yF_XZphbKZh9kXyr-AWdEcIR_THl81_VtDFHH6kTb6ac2V8CE2029YUVU95tg2YvaMe4GVQSA4ScKbOWyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی: ایران از شروط هفتگانهٔ خود برای بازگشایی تنگهٔ هرمز، عقب‌نشینی نخواهد کرد.
🔹
هنوز از طرف میانجی‌ها چیزی به ما منتقل نشده و حرف‌های ضدونقیض از سمت رئیس‌‌جمهور آمریکا زیاد شنیده می‌شود.
🔹
ما منتظر هستیم تا نظرات قطعی توسط واسطه‌ها به ما منتقل شود و…</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/464732" target="_blank">📅 14:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464731">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6fcbae90.mp4?token=TAXDTXOGilwBOLWwixStXVajGPoqH4Nx1QhvgklKbp8dyPmbYGYtaJGUvVEyCHlx_vZ9gcj9Ff5ghgkBKcIyUwexlfPsolkUlo3mTFIBw7AbqojMU9UlAYjBJHGT8AQ8Dk_Q-yfg5aE-hxAG60JcshxyIBWlKt2dOP5lT7dWZ0-WtWkwFAFIJRu1K2iq_505VY6eQhndgfL7321Z-jOtpnQBYGjwKgF9Y46D66yuvhb8NCvqHqbGWblskRe0ixm0RHsEx3qB1oZ2pSYGW1scTnC6bx-jf4VRhiWacmoPbP_IXvEAq1Kzfwq1wBFNwQQQutpNiKIQI1gtDV23mGT_nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6fcbae90.mp4?token=TAXDTXOGilwBOLWwixStXVajGPoqH4Nx1QhvgklKbp8dyPmbYGYtaJGUvVEyCHlx_vZ9gcj9Ff5ghgkBKcIyUwexlfPsolkUlo3mTFIBw7AbqojMU9UlAYjBJHGT8AQ8Dk_Q-yfg5aE-hxAG60JcshxyIBWlKt2dOP5lT7dWZ0-WtWkwFAFIJRu1K2iq_505VY6eQhndgfL7321Z-jOtpnQBYGjwKgF9Y46D66yuvhb8NCvqHqbGWblskRe0ixm0RHsEx3qB1oZ2pSYGW1scTnC6bx-jf4VRhiWacmoPbP_IXvEAq1Kzfwq1wBFNwQQQutpNiKIQI1gtDV23mGT_nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منبع نزدیک به تیم مذاکره‌کننده: ایران منافع خود را تحت فشار واگذار نمی‌کند
🔹
رئیس‌جمهور آمریکا اخیرا گفت که پیشنهاد توافق ایران را رد کرده است؛ حالا یک منبع آگاه نزدیک به تیم مذاکره‌کننده در این‌باره به فارس گفت که پیشنهاد اخیر ایران دربرگیرندهٔ مجموعه‌ای…</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/farsna/464731" target="_blank">📅 14:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464730">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e4fa82c1f.mp4?token=YB_iCUJRXgdJ3Y-PF_P-vJCd1cZdKZtr2yuAr6J_QuUQ7trN412jMqzfzHOybpxDwaz15TvdlM_ZHBVoWFbs1Lc47HZ3TdnXJuLlb9ltaPXiACx3kd-I7V803qIY2yd6XASgzPqjzNHkif5hg2kMOFWnmhE-L390upvRMli8WfjVEGcM9hrcTk-TM0vQtsR0MZsJ5EYtnOBz0t2pLs0ko8qbzlG0AJxDbFLzpYLkdwiy5Ln3kPrYrIGr5a4uKVddDVUOJ0A2pWxiXVmCVbyQ7tEFGZ8_BdvF_-CvJmB-PLCUTL5OwoLo18M5HQCkGOM5Ri3F_1Nm8BUJ8ZstexNdjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e4fa82c1f.mp4?token=YB_iCUJRXgdJ3Y-PF_P-vJCd1cZdKZtr2yuAr6J_QuUQ7trN412jMqzfzHOybpxDwaz15TvdlM_ZHBVoWFbs1Lc47HZ3TdnXJuLlb9ltaPXiACx3kd-I7V803qIY2yd6XASgzPqjzNHkif5hg2kMOFWnmhE-L390upvRMli8WfjVEGcM9hrcTk-TM0vQtsR0MZsJ5EYtnOBz0t2pLs0ko8qbzlG0AJxDbFLzpYLkdwiy5Ln3kPrYrIGr5a4uKVddDVUOJ0A2pWxiXVmCVbyQ7tEFGZ8_BdvF_-CvJmB-PLCUTL5OwoLo18M5HQCkGOM5Ri3F_1Nm8BUJ8ZstexNdjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایران در دانشگاه تهران توسط وزیر علوم به اهتزاز درآمد  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/464730" target="_blank">📅 14:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بازداشت ۲۱ نفر و کشف مشروبات الکلی در یک کافۀ یزد
🔹
دادستان عمومی یزد: از یک کافه در یزد مقادیری مشروبات الکلی کشف شد؛ همچنین درپی تست الکل از ۱۰۰ نفر حاضر در کافه، نتیجهٔ ۲۱ نفرشان مثبت شده و این افراد دستگیر شدند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/464728" target="_blank">📅 14:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e43abd7048.mp4?token=LVrB1UA5_gMo5tU7gUB4y-0RKz9_48tCZ8PLGqO8s0rb9x8kBLzqMsff-y_5aW_UzqkbQL1_dfDjy1BsA_Axx4NZcEI14Gh09i3cLwx0snUlSslBN3NpYZfAQwHw-oQadHeNl2pCipofOcLhm6YMRAJIoqI3PNc2Jh1CIXbx0r7jtNwfNkIrIfSqs7R0zbzmx_FNr2t3ctrgA_MwO52LZLde6Tuc05TFr9o4J7mmAepme_UahvQvcBoxRUZQDlYtN1zklJG2etuXRSZI501vvDqxJiworay8G8k_lVlVaDA_H_LjlLkGlMyUrfB_OWyR_iJmOWsRGudseCodZsV5ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e43abd7048.mp4?token=LVrB1UA5_gMo5tU7gUB4y-0RKz9_48tCZ8PLGqO8s0rb9x8kBLzqMsff-y_5aW_UzqkbQL1_dfDjy1BsA_Axx4NZcEI14Gh09i3cLwx0snUlSslBN3NpYZfAQwHw-oQadHeNl2pCipofOcLhm6YMRAJIoqI3PNc2Jh1CIXbx0r7jtNwfNkIrIfSqs7R0zbzmx_FNr2t3ctrgA_MwO52LZLde6Tuc05TFr9o4J7mmAepme_UahvQvcBoxRUZQDlYtN1zklJG2etuXRSZI501vvDqxJiworay8G8k_lVlVaDA_H_LjlLkGlMyUrfB_OWyR_iJmOWsRGudseCodZsV5ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
شکار دومین زیردریایی ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد: رزمندگان نیروی دریایی سپاه به‌یاری خداوند طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا…</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/464727" target="_blank">📅 14:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464725">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmLme-4_oDDV7dd2ugt0sHr7Pebl3ICELIYOg3r3ulegEpzKycsRmicure5L2B9Agu19gNq-PiduH8kLhdWjI4CMxPa4Vep_cveZfned-mB6XJzGKEasOq9pHLabrl0I3rdM8GLf4KTPzOatrcwz9-GWJQAwX3Sqs-mnr49B7tAiorHe_ghUn2ZG-Gz6hxC1XvTD3Td9jjZJZeriyq_7N3cYVtFCNx7ArXeNJ1tAXNMiSag7GoOOKVwi-h0Pkuo1wn0xsnXcezZXyCykc3HGZRsSlwEn-dZrpwd2wdzTZb0mP5TLPkpu_qe913IYcO5hmOEU8ZEj3-DemavM2kWbXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شکار دومین زیردریایی ارتش تروریستی آمریکا در تنگهٔ هرمز
🔹
نیروی دریایی سپاه در بیانیه‌ای اعلام کرد: رزمندگان نیروی دریایی سپاه به‌یاری خداوند طی یک اقدام هماهنگ و پیچیده با اشراف اطلاعاتی و جنگ الکترونیک توانستند یک فروند زهپاد پیشرفتهٔ ارتش تروریستی آمریکا را که برای جاسوسی در تنگهٔ هرمز فعالیت داشت، به‌دام بیندازند.
🔹
این زهپاد از نوع یکی از زیرسطحی های هوشمند و پیشرفته با نام «ریموس ۶۰۰» (Remus 600) بوده که توسط رزمندگان نیروی دریایی سپاه به‌غنیمت گرفته شده و اکنون در اختیار متخصصان این نیرو برای بازیابی اطلاعات آن قرار گرفته است.
🔹
نیروی دریایی سپاه با قاطعیت اعلام میکند تنگهٔ هرمز مسدود است و در برابر تحرکات خطرناک و تردد از مسیرهای غیرمجاز در تنگهٔ هرمز، با اقتدار و بی‌وقفه در حال برخورد هستیم.
«وَ مَا النَّصْرُ إِلّا مِنْ عِنْدِ اللهِ الْعَزیزِ الْحَکیمِ»
@Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/464725" target="_blank">📅 13:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464724">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hl4K0J7znUoTHWirltD5HIQZ5XeYMN-157jZVpVp0M2LtaYYBxsti2zkQqUFN9HEJ1e1UcfdO5Sl7SlYPGgUARqJsz3K27wnP7XzOYfXgh7GcUbHkBI022IxouAjl13JFG7NfNxd4rtH5o4_PsteCCkZQT34bfR4xOWf2PxEi9Bpy2r9X4tA_XSSBoDDo5m0zVn5tDNgYyI-P442mUSu9zcbME3KtzzA7J-j3s_0PSMV4yseNI-5ESibo75ZUu_JmjA3aDXSpKFSbww5gqOUOox6FLsDh7U-cBwk6OkuTPAGnBV0pO61I-NfnIVGXib_Y4gkO-OfQYtCep0twKc4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات جدید از افزایش اعتبار کالابرگ
🔹
رئیس سازمان برنامه‌وبودجه: فعلا برای حدود ۴۴ میلیون نفر واجد شرایط پیامک ارسال خواهد شد تا با تکمیل یک اظهارنامه شرایط آن‌ها برای دریافت این حمایت مشخص شود.
🔹
افراد تحت پوشش کمیتۀ امداد و بهزیستی، و خانوارهای مورد تأیید…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/464724" target="_blank">📅 13:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464723">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b747c57d0d.mp4?token=VTkOCDPwLvk-Yb88HiwBX2CLA6NP5azrwhgJvVvjwM6YqcbY7CvZ12doJalHiaIEJFCUZtskHqTR3u4oFGFPgMW_88U_7mAPqq58jRqHPCNrSxIqprTeyz4Sp7na88nJKdv1RYzz2Hb4GXDIgwtNG0rnzlVvQTsfLG3dWtb8aPmPNR2yqm7b8zqh8MvGqrO-oSnVOOXwXf0LR73HrqDlNoyxgYZhqSumqqZzxHPFeZqQ2Pg5w7NC_HKIgtTvOfmzcnYqCysa-TSYTGRy40cKpiWFO8x1IgkWUFoPdO80t5SlfZoxRc6AAnH0j7ix62clx7IOi9K4ZfIaTtx1Tw0V3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b747c57d0d.mp4?token=VTkOCDPwLvk-Yb88HiwBX2CLA6NP5azrwhgJvVvjwM6YqcbY7CvZ12doJalHiaIEJFCUZtskHqTR3u4oFGFPgMW_88U_7mAPqq58jRqHPCNrSxIqprTeyz4Sp7na88nJKdv1RYzz2Hb4GXDIgwtNG0rnzlVvQTsfLG3dWtb8aPmPNR2yqm7b8zqh8MvGqrO-oSnVOOXwXf0LR73HrqDlNoyxgYZhqSumqqZzxHPFeZqQ2Pg5w7NC_HKIgtTvOfmzcnYqCysa-TSYTGRy40cKpiWFO8x1IgkWUFoPdO80t5SlfZoxRc6AAnH0j7ix62clx7IOi9K4ZfIaTtx1Tw0V3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم ایران در دانشگاه تهران توسط وزیر علوم به اهتزاز درآمد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/464723" target="_blank">📅 13:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464722">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4WPPtYjTFg32weLCg-1q_FflUv5MmRjwCJomKnAEAcvasGBRnBmKDI3ucXyAvcEdfxO43IKjCxBF_UIkxyZGEZFA5xbWPzX-bifSYgDfHSTz3JhnXTDC9yr_u6n0SxxVi4OTnbaKavCSHH_thOmyFnlH5uJRXbqe9f8xag9bGTJYx87uVw3703lnGpdqVNrY-XZb9cyCG0oNbUtTHNFI-mkYnaifyQAsjaQoAbBVo0_qtncqJIHLjr2IsXkHHtrUAPLG7fjhPOBR8b8riY0H6fV-ZHGRSL2hgmTHqdQ4bgqt6v3UDsRe_Xur8d65j0WzvjsCWerUnRxD_JLvdX9DlHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/182adcc130.mp4?token=nVIsPnycY61KZMHf9_6uMX9mPALjXTSoJYppqJWnB-bEMCYixYXM8uLkXvwu3MynWgFombRFdPfbgP0DZuhNtBb6Cv9BEYGIfKLJnlVCeZyI1B7NZYSocbEJz826y2dJ0IkhY3y_AL2jprRPncZYOs167ldDOzjItq1did-f6U11AzCTk_h14V_MkoHTuQYkjri3bR68c7IFCKnE9fvS3DK_-wQwmRQVYI57BzcpsVrLTAqzOfW15LFlT9-eKVcKpnIlnaTCvMZtDlzLEBF8ETNT41uOZIrxlhS_zrdYnbX35vwNX0BG2_1JuHWp6C3rEkUo8BzMyl1j3pPbWABx4WPPtYjTFg32weLCg-1q_FflUv5MmRjwCJomKnAEAcvasGBRnBmKDI3ucXyAvcEdfxO43IKjCxBF_UIkxyZGEZFA5xbWPzX-bifSYgDfHSTz3JhnXTDC9yr_u6n0SxxVi4OTnbaKavCSHH_thOmyFnlH5uJRXbqe9f8xag9bGTJYx87uVw3703lnGpdqVNrY-XZb9cyCG0oNbUtTHNFI-mkYnaifyQAsjaQoAbBVo0_qtncqJIHLjr2IsXkHHtrUAPLG7fjhPOBR8b8riY0H6fV-ZHGRSL2hgmTHqdQ4bgqt6v3UDsRe_Xur8d65j0WzvjsCWerUnRxD_JLvdX9DlHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چگونه واردات کالا به کشور در شرایط جنگی سرعت گرفت؟
🔹
محمدحسین مصباح، فعال اقتصادی: سیاست‌های پیشین ارزی در کشور، تجار را برای واردات کالا زمین‌گیر کرده بود.
🔹
اما بانک مرکزی با ورود به‌موقع و اصلاح یک رویه غلط، گره کور تجارت را باز کرد و دغدغه دسترسی به کالا در شرایط جنگ و محاصره برطرف نمود.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464722" target="_blank">📅 13:30 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464721">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک تجارت | Tejarat Bank</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=nvj6SwLSU0KSjHHJp0YLHv6mqbJETEC6zTEtUGl7vfmUigzSlwumV1LuavjuhGeqOdLqWESnfozmnVymUK3495SGo10d3W3GBT9oB2RpcKzLQZ71alCvc9661mT-rgs_4JO787gvr8MQSjOrFiy7GDbpd7-6_2fmhwTzI1TXCTZguWlFC2P02Y1OcPTK85KFYhWf_vKQlNb_Y0sEoPgc1aVqW3n-gSSly3s9WGWp7zwecYDrqC_SgHw5MaEYH7EsT6zz4Kzu528WdvigCg5UARLhYCp_giZ0CcOw8A0_jwSN5qNzT5i7xSj-Grh6jeFZYoqX-hKg3_BIjBgRdSKjgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d2ab6808bd.mp4?token=nvj6SwLSU0KSjHHJp0YLHv6mqbJETEC6zTEtUGl7vfmUigzSlwumV1LuavjuhGeqOdLqWESnfozmnVymUK3495SGo10d3W3GBT9oB2RpcKzLQZ71alCvc9661mT-rgs_4JO787gvr8MQSjOrFiy7GDbpd7-6_2fmhwTzI1TXCTZguWlFC2P02Y1OcPTK85KFYhWf_vKQlNb_Y0sEoPgc1aVqW3n-gSSly3s9WGWp7zwecYDrqC_SgHw5MaEYH7EsT6zz4Kzu528WdvigCg5UARLhYCp_giZ0CcOw8A0_jwSN5qNzT5i7xSj-Grh6jeFZYoqX-hKg3_BIjBgRdSKjgIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💍
حمایت ۱۳ همتی بانک تجارت از جوانان با اعطای تسهیلات ازدواج و فرزندآوری
🙏
بانک تجارت با پرداخت ۵۱ هزار و ۵۷۷ فقره تسهیلات ازدواج و فرزندآوری شامل ۳۳ هزار و ۳۷۶ فقره تسهیلات ازدواج و ۱۸ هزار و ۲۰۱ فقره تسهیلات فرزندآوری جمعا بالغ بر ۱۳ همت، حضوری موثر در حمایت از جوانان و خانواده‌های ایرانی داشته است.
🔵
این بانک با بهره‌گیری از زیرساخت‌های دیجیتال و سامانه باجت، فرایند ثبت‌نام و پیگیری تسهیلات ازدواج و فرزندآوری را به‌صورت غیرحضوری فراهم کرده است تا متقاضیان بتوانند آسان‌تر از خدمات مربوط استفاده کنند.
📱
tejaratbankofficial
📱
TejaratBank
📱
TejaratBank.ir
🟢
TejaratBank
🟢
TejaratBank
📲
TejaratBank</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/464721" target="_blank">📅 13:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464720">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/464720" target="_blank">📅 13:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464719">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vp9ywixh9VBPzSsnnbAbUrcngypFhmzEdcWwF2oD0JsprLhMWRcHhy7djCPPo-IJwhgzanJVOqDbNVZgPcLc5nkhNUcYO2HhlPQpdLj7PUt0HH9vfeea6bazpXbU8QM1bJ0EoSOx0HUH0eVAeVBWjM7TAJsy1-R2dzPGPQgY8q7M9yGkhkaOH2Sj-PrrByD1Gamp4ZVKv2lqjGFtqrrWuQyzr0iODIMvO6kgDsS2-fIesXY6zGRklqyYyQAn8FK9XRQoa5BVOVxPw0DPyhtIXDoORctVuFPQ4gUNQ6dWgD8VTwfcBOsxexolG1a3hKj9YFbWBRGgFhf5pTu9xmlzfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خالی‌فروشی طلا مقابل چشم ۱۰ نهاد ناظر
🔹
با وجود حضور ۱۰ دستگاه از بانک مرکزی و دادستانی تا وزارت صمت و پلیس در سازوکار نظارت بر معاملات آنلاین طلا، همچنان موضوع دسترسی کاربران به دارایی خود محل ابهام است.
🔹
درمورد میلی‌گلد، این پلتفرم اعلام کرده طلای کاربران در خزانه‌های بانکی نگهداری می‌شود، اما محدودیت دسترسی به ذخایر طلای سپرده‌شده در بانک کارگشایی باعث تأخیر در بخشی از تسویه‌ها شده است.
🔹
میلی‌گلد همچنین از وجود ۹۶۵ کیلوگرم طلا مربوط به تعهدات کاربران در خزانه‌های بانکی خبر داده و گفته برای دسترسی به این ذخایر محدودیت ایجاد شده است.
🔹
بنابراین موضوع مطرح‌شده، طبق توضیحات خود پلتفرم، بیشتر ناظر بر دسترسی و تسویهٔ دارایی کاربران است، نه صرفاً ادعای نبود پشتوانه.
🔹
از سوی دیگر، سامانهٔ ناظر بانک مرکزی که طبق مصوبهٔ دولت باید ظرف ۳ ماه راه‌اندازی می‌شد، با گذشت بیش از ۸ ماه هنوز به اجرای عمومی و کامل نرسیده است.
🔹
مسئلهٔ اصلی برای خریدار، تعداد نهادهای ناظر نیست؛ بلکه این است که هر زمان اراده کرد بتواند طلای خود را بفروشد یا تحویل بگیرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464719" target="_blank">📅 13:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464718">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n8oDv5BOkTSD1ztl63bYrsP5qN4210LKwHSdEMW4Iej6zhwx0GdQzJv5Ge9ST3BlMiyEmV4Shcbui0RxYN8cClArZ_WzzrsQsXpbqvsunu7sj5LYKHB5uaD4dyxCGDIqdL5x0G1aorso-B8fHYKmauC8Csl9xMme2kMck3uRu9vdKHxp6ybOG-f2FTc9hF-6BCvyutquvGWslOH2XUF_4jWqB_2KrJ6IJ3VOnGSKpi1Mve9s_8SPtOx4ZxH3W0hhB6ldWNfG34Bdrk3eZf_lxt1DZKuZHm_X5jpJHnBjaR8_O-AHqMWxtEdpT4e2s7IjtGBXRTYhCjb0eZcylIl4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
تاریخ‌سازی دختر وزنه‌بردار ایران با مدال برنز
🥉
ریحانه کریمی با ثبت رکورد ۱۰۷ کیلوگرم در یکضرب و ۱۳۶ کیلوگرم در دوضرب و مجموع ۲۴۳ کیلوگرم، مدال برنز بازی های آسیایی ۲۰۲۶ را کسب کرد.
🥉
کریمی اولین وزنه‌بردار زن مدال‌آور تاریخ وزنه‌برداری ایران در این بازی‌ها لقب گرفت.
@Sportfars</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/464718" target="_blank">📅 12:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464717">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbca6bfdc5.mp4?token=IY_Ygtx1q2tzgA7drxyi2mIJKN_FsQ3pxZkTAsZ32Ygh3kcNloQDU7D6vXnzCEKVfbgTBqxw1LXMuVn3fgDsRJCF2TwBW1raou9TF-zOpMTpX_X8nildG7sueHgc0hCkUrh1DCTW8OEELxOLMGDzrTl3bYCElMjunI4fFIHhN52agiOB_5EAam3StXm18_NvdBaUBaISa9bU5YJqpRolgRk5pJz9qFiTH6OTJPi3kIADEJFmFiSLOOloDT9CHmS4zS-fMkjsyGBACB_Z76ZsnPkPo8leyzzbCkwDC81ncViVTcOr18tHiJcno61WGqZydf4U0ubLkCBGJXt4H8yaAHYvY2ImCa51lO_dQYVaLpaYS2x1ruDMMyB-3coPMe1ewlC5LXyoUOo_0UER27_vDTGb2GtvpjaWWoNLy1SY4-uXYZPi0KRXOXuKI7zkL4lmIlHaeZmQDyHyzI1XRjDsGrUqTa9xf_Ni4xHe5sq-MVFEo1LExJwuhGtZ6kuielG0FuEQ_DxAiWLj9DngWPf9jVhr8kmQzrzd_kO5OGifyP4_MF9Vz742OFspxdwYPbdghdHrPSThSqLOOWQoKJsDLJ8Xn0l_VojN0NfJBQyDCY9YgFk7YZlgSpyUEgs8r2zK_6oyMj5X3jV6_gIYrK8Z5EooCKI0NcKKDaMfWGBh0oI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbca6bfdc5.mp4?token=IY_Ygtx1q2tzgA7drxyi2mIJKN_FsQ3pxZkTAsZ32Ygh3kcNloQDU7D6vXnzCEKVfbgTBqxw1LXMuVn3fgDsRJCF2TwBW1raou9TF-zOpMTpX_X8nildG7sueHgc0hCkUrh1DCTW8OEELxOLMGDzrTl3bYCElMjunI4fFIHhN52agiOB_5EAam3StXm18_NvdBaUBaISa9bU5YJqpRolgRk5pJz9qFiTH6OTJPi3kIADEJFmFiSLOOloDT9CHmS4zS-fMkjsyGBACB_Z76ZsnPkPo8leyzzbCkwDC81ncViVTcOr18tHiJcno61WGqZydf4U0ubLkCBGJXt4H8yaAHYvY2ImCa51lO_dQYVaLpaYS2x1ruDMMyB-3coPMe1ewlC5LXyoUOo_0UER27_vDTGb2GtvpjaWWoNLy1SY4-uXYZPi0KRXOXuKI7zkL4lmIlHaeZmQDyHyzI1XRjDsGrUqTa9xf_Ni4xHe5sq-MVFEo1LExJwuhGtZ6kuielG0FuEQ_DxAiWLj9DngWPf9jVhr8kmQzrzd_kO5OGifyP4_MF9Vz742OFspxdwYPbdghdHrPSThSqLOOWQoKJsDLJ8Xn0l_VojN0NfJBQyDCY9YgFk7YZlgSpyUEgs8r2zK_6oyMj5X3jV6_gIYrK8Z5EooCKI0NcKKDaMfWGBh0oI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توهم تجزیه‌طلبان برای تصرف تهران با همراهی مردم!
🔹
طرح مشترک آمریکا و اسرائیل که به تشکیل یک مرکز فرماندهی با حضور افسران عالی‌رتبهٔ موساد و سیا و همچنین فرماندهان گروهک‌های تجزیه‌طلب کردی منجر شد، درصدد اجرای سناریوی تجزیهٔ ایران و تغییر نظام حاکمیتی جمهوری اسلامی ایران بود.
🔹
این طرح با حضور مردم کرد در صحنه و همچنین با اشراف اطلاعاتی و برخورد قاطع نیروهای جمهوری اسلامی، از جمله موشک‌باران و حملات پهپادی به مقرهای این گروهک‌ها، در همان مراحل اولیه خنثی شد و به سرانجام نرسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/464717" target="_blank">📅 12:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464716">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH1N6BZ2QH2hwwyIppyvE9cUWT3kZMvFcz-aOFbWpH1tgVj82Sz4aaGETaD4Qf5uZE_Ogri73O7zIQS1XjM5gCuY92CEa883hHzdwhUthgh4Y4tJJQ1APz6yUQb75n7aWOftKDgyOB1fyP6yXISzcQJBr6oYTX7CGEzPKA7Ow0-03LkmadKyVTzesrQcc-hC6lFE3qXdpBFsPqc0igZ3yZ0e6HS2880frBtkNdADfFyan1z4vJdHPSJt8qJjLrchX2MnkjusK9YyPoBB5Up7Ci14Jl2KhZT98AJQPjPXVV36Sve6rDHWceY7JdrN-MagZsJJAY_OUzqO2NTzxRyVNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به بالای ۷.۲ میلیون برگشت
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۲۱ هزار واحدی به ۷ میلیون و ۲۷۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464716" target="_blank">📅 12:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">منبع نزدیک به تیم مذاکره‌کننده: ایران منافع خود را تحت فشار واگذار نمی‌کند
🔹
رئیس‌جمهور آمریکا اخیرا گفت که پیشنهاد توافق ایران را رد کرده است؛ حالا یک منبع آگاه نزدیک به تیم مذاکره‌کننده در این‌باره به فارس گفت که پیشنهاد اخیر ایران دربرگیرندهٔ مجموعه‌ای از اقدامات متقابل و مرحله‌بندی‌شده است و ایران مواضع و ملاحظات خود را به‌صورت روشن به طرف‌های مقابل منتقل کرده است.
🔹
این منبع آگاه با اشاره به فشارهای ناشی از رویکرد و منافع رژیم صهیونیستی در سیاست آمریکا، تصریح کرد: وضعیت هیئت حاکمهٔ آمریکا در داخل این کشور با چالش‌های جدی مواجه است و نارضایتی نسبت به پیامدهای جنگ و هزینه‌های ناشی از آن افزایش یافته است.
🔹
این منبع آگاه در پایان خاطرنشان کرد: ایران همچنان مصمم است در برابر زیاده‌خواهی‌ها و فشارهای آمریکا و رژیم صهیونیستی ایستادگی کند و حقوق و منافع ملی خود را تحت فشار و تهدید واگذار نخواهد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464715" target="_blank">📅 12:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-peBbVa6j1uRuR4Lbu6YVB7XL1vrvvKamOobcQyydga5SmwAJvSo4gx2hHChsPzWijKAsQXP67OEZ7COBrWba3yX8YegfxX0E1nYrk-4Tzk_YCAmJJS2DZRvHT7igQgX2LkIMbHfNIa7eBFZU-VihZbtBIzaIGNsrMOvhBXY4ekhQyN-CdOUGOpvTwLVWnWm8muUgwT-WRfjy77rNRxFrvquTTkcwQlED7IP2F38Lh6mO_PRB-nrjHiRNOsnfab9aT1r1Wblgfl-EuRioJgYtEI_8xaceAt8EhBO8uJQeZUALrsqS5WKwKe_pU-O4dfeyymHC3zApg3WvtXsgDnfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واترپلوی ایران از دیوار چین رد
نشد
🔹
تیم ملی واترپلو در دومین بازی خود در رقابت‌های آسیایی ناگویا، نتیجه را ۱۲ بر ۸ به چین واگذار کرد.
🔸
تیم کشورمان در ادامهٔ رقابت‌ها فردا در آخرین دیدار گروهی به مصاف کرهٔ ‌جنوبی خواهد رفت.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464714" target="_blank">📅 12:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
اعلام «حادثهٔ بزرگ» نزدیک پایگاه میزبان آمریکا در انگلیس
🔹
پلیس انگلیس از اعلام یک «حادثهٔ بزرگ» در نزدیکی پایگاه هوایی فیرفورد که میزبان نیروی هوایی آمریکاست خبر داد و اعلام کرد که شماری از خانه‌های منطقه تخلیه شده‌اند.
🔹
پلیس شهرستان گلاسترشر انگلیس امروز از تشدید تدابیر امنیتی در این پایگاه خبر داد و اعلام کرد چند نفر را به‌ظن ارتکاب جرایم مرتبط با قانون مواد منفجره بازداشت کرده است.
🔹
به‌گزارش اسکای‌نیوز، تیم تخصصی خنثی‌سازی مهمات و مواد منفجرهٔ ارتش انگلیس در حال بررسی شماری خودرو در این منطقه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/464713" target="_blank">📅 11:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOgyJPxrO5GtwoMo1MAYWcEd_aD3o1xo9We-qZJ6D_SXm_aFyOp1LXzXkEJ7xoYydbX8iRstwTlVYuibWZ9mfi-xtnXrJydcxDZWxUSQ-FqmIPfdvAs1gs1M918nLWSXuOkHyFNHmJgXF_4Wjcp-b7pKbJos4-lJbz86kY4LV0GmHbMl0dMXxg5RFo1v1zdrIkCSJHNt3jQA2gWskRH49lUPFVoQIwehQ28hlnN6ZvNdzf6wXs4veJTQTDQ0VgBML1dkE90LLP2aaE2HAl3fKB2jhUAPxCHUsn8DpX0i0h5HcGfU_vvC39wzutd7I73NW1DIYKYgpg5qGQ38m6LhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل راه ساخت حساب جدید را برای ایرانی‌ها بست
🔹
کاربران ایرانی هنگام ساخت حساب جدید گوگل با ردشدن شماره‌های +۹۸ در مرحلهٔ تأیید تلفنی مواجه شده‌اند و در بسیاری موارد امکان دریافت کد تأیید نیز وجود ندارد.
🔹
این مشکل فقط به ساخت جیمیل محدود نمی‌شود و می‌تواند دسترسی کاربران جدید به سرویس‌هایی مانند گوگل‌پلی، درایو، فوتوز و پشتیبان‌گیری اندروید را هم تحت تأثیر قرار دهد.
🔹
کاربران ایرانی پیش‌تر نیز از مشکلات تأیید و بازیابی حساب‌های گوگل گزارش داده بودند، اما علت دقیق محدودیت جدید هنوز مشخص نیست.
🔸
براساس پایش‌های شرکت ارتباطات زیرساخت، حدود یک‌سوم سایت‌های مهم جهان به‌دلیل تحریم‌های آمریکا، به‌طور کامل به‌روی کاربران ایرانی بسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464712" target="_blank">📅 11:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464711">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KM8J1bWbklHhWvWPsGCrJln2pmrF3T026FTJ7rb9AmHN4JMwO2dwJ0P62W5kcYge0HWpIbt_fxKneEWIgaqQ6VNSJdiYtb4RQzLghacgT6-pS5sVoT3RwuxqQpcP9yk7U_tnTfH3wk20fPgQwx1oO79YFaL4pCLC0CXZ6puGfIkxcEC8d82gT1j3Gxmnxk43wqFHkFIYQDGnL_5aacLVI2OR0Fy8sB2a6qFwn1FV8q_IdjAmBBOtxrRlID6Z_hD_Uu4Rt1yrtLemwgS4rxnjp73ccWJ_785b2PiYLgqOyPX6dusw-0pld7uGeiR3uHd_VWMsexhEoyhmaRykJhJmeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده‌کل ارتش: اگر قرار بر ناامنی منطقه باشد، این ناامنی برای همه خواهد بود
🔹
امیر حاتمی: هنوز جنگ تمام نشده است. همچنان باید آمادهٔ واردکردن ضربات سخت از سوی سربازان ایران عزیز به دشمن باشیم.
🔹
اگر قرار بر ناامنی منطقه باشد، این ناامنی برای همه خواهد بود. نمی‌شود ما در منطقه زندگی کنیم و سالیان متمادی صاحبان این منطقه باشیم، اما دیگران از جای دیگری بیایند و از همهٔ این موارد استفاده کنند.
🔹
من به‌عنوان یک سرباز ایرانی از همهٔ همسایگان و کشورهای منطقه می‌خواهم به این موضوع توجه کنند؛ دیدید همکاری با آمریکا امنیت‌آفرین نیست. امنیت منطقه در درون منطقه و به‌دست خود کشورهای منطقه است.
🔹
امنیت در منطقه جز با ازالهٔ آمریکا و زدودن آمریکا و رژیم صهیونیستی از منطقه اتفاق نخواهد افتاد و این اتفاق دور نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464711" target="_blank">📅 11:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464709">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae1b2095f.mp4?token=YRS8wBAEyGRZGfH410zLA7Bk053q2bVm1Nle2ZFSv0GWuIXu5BZ7wI-hNVeN9gW61X3POr8ok03NOf82OsR7HZIqBkI3BMnnEfVKe0xKB5qSPQH_n5aXnLKr2VokyZj1RNXMxeTMVt9Ef-v37kkfaZJAbDKeFw3l0n5QDHJdRQ0cTW_i6SE1zSrWbn6y0WWtRJncT9dKptFmxmLKfS3xYhKxfUx_GoKVmSvqu70MWzO83Xk_8r3lNOFKbLzuxNzKiFIQP3A8Ve6jS5eVHvorzsWVOBoSw3iREWcspFtBQE6vqxflDylWsal5kIDALh_mh02Zlc5TrijflwZKbtcOUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae1b2095f.mp4?token=YRS8wBAEyGRZGfH410zLA7Bk053q2bVm1Nle2ZFSv0GWuIXu5BZ7wI-hNVeN9gW61X3POr8ok03NOf82OsR7HZIqBkI3BMnnEfVKe0xKB5qSPQH_n5aXnLKr2VokyZj1RNXMxeTMVt9Ef-v37kkfaZJAbDKeFw3l0n5QDHJdRQ0cTW_i6SE1zSrWbn6y0WWtRJncT9dKptFmxmLKfS3xYhKxfUx_GoKVmSvqu70MWzO83Xk_8r3lNOFKbLzuxNzKiFIQP3A8Ve6jS5eVHvorzsWVOBoSw3iREWcspFtBQE6vqxflDylWsal5kIDALh_mh02Zlc5TrijflwZKbtcOUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سفیر عراق در ایران: دولت عراق تلاش می‌کند پروازها از سر گرفته ‌شود
🔹
یاسر الحجاج: دولت عراق به تلاش‌ها و مذاکرات فشردۀ خود برای بازگشت شرایط عادی پروازها بین عراق و ایران ادامه می‌دهد.
🔹
توقف پروازها بین عراق و ایران یک وضعیت موقت و گذرا است و به عمق روابط…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464709" target="_blank">📅 11:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464708">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKadwjqaNY-_M_3uss9sZBaZ3Lk8iCSbtIH9wJ5grKitY0vynbl-uifBH3gg5ET6EOsfhHkpUyJWwBzgF96pfgPzVR6N-Q4oTyUHNbj-VTaINYh_ATRUlCiPxs9pkgukL8iZZZcumYrrb1qiAmFR2ZpcenY-C-Hp7Rgzg-jB3AU6BbtTNZvKwqbyCNxu9pni55guuKUpoLb25hYyox4uCaGsq3RGUG1iX-7J_NAiNWSFEi-RcHuLqkuzrcQYCB30jZKMCNxt6FFkv72pbghu4mO2xYAmgGsnz7wqCIeP2__T9DLGjdxk6qfg-wYofO_Zpcnnxma0kZ-LJ5WDET4O6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید؛ آن‌که از آتش برخاست
🔹
بعضی از آتش می‌گریزند و بعضی از آن زاده می‌شوند. موفق محادین، نویسنده سرشناس اردنی، در سالروز شهادت سید حسن نصرالله، او را تجسم همین برخاستن می‌داند؛ کسی که از نجف تا ضاحیه ایستاد و حتی پس از شهادت، اندیشه‌اش چون زبانه‌ای از آتش، تاریکی را می‌شکافد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/464708" target="_blank">📅 11:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464707">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SA1XsVFMG0hlnFsPSDPmnMbAL92okPVbv3FAiZxC5GjWo9PlKX3h6S1s7zwQEWCCmn_zv5tErB5Vfl4kNE8R-tXBBpkoZawEGclVYOjvOJioX2plpFJB8xqnwjQXZWSQYBMaE5zWN-y8Y90CGoLbQdTP9Y12aRD-7zTAocwYazD8BVf27_qUrvio2Ss-ngq4yJQ3m7yQg4AWxDapp8ppbycRW2__3c1dkEO2ViGj5LtQIwK_lETCvSrclxt-fx2LdJrImhWZT5OCJ4XAXIRJCl85GzkeFdv8ewGOd_3cm0hWnGP4Qb_tLKYkAAgwJZciHlZSwPB-Nus5KNtHrlLWkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ثبت رکورد جدید جذب منابع در پیشخوان‌های شهرنت بانک شهر
👈
پیشخوان‌های شهرنت بانک شهر با ثبت رکورد 12 هزار میلیارد تومان جذب منابع، موفق به ثبت دستاوردی جدید شدند.
👈
به گزارش روابط عمومی بانک شهر، محمدعلی بخشی‌زاده، مدیرعامل شرکت توسعه و نوآوری شهر، با اشاره به دستیابی پیشخوان‌های شهرنت به رکورد ۱۲ هزار میلیارد تومان جذب منابع و تثبیت آن، از تلاش و همراهی همکاران و راهبران این پیشخوان‌ها قدردانی کرد.
👈
بخشی‌زاده اظهار کرد: دستیابی به این رکورد، حاصل تلاش مستمر، پشتکار و همراهی تمامی همکاران و به‌ویژه راهبران پیشخوان‌های شهرنت است.
🔗
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/farsna/464707" target="_blank">📅 10:57 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
