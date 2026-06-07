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
<img src="https://cdn4.telesco.pe/file/QmPwEQcZpIpNjiA4Jg0SjR6nSDK5YtWhw42C3PCaPhKURtkzmQQ16r5pT8m0xU92vGDFyHMxcFhBypBtkr_TIxPpjU9FJpgKGdZX8ldtAVXMAay1bmTyf0Qea0SemQu997j-1q5rz1-L6rNXQmTTmjS9lLHlhQv15sLn_FzFXkqok1b5rYX8ZEYKNn7z4GLLvO4L561KfP5KOtAzNxsxKPYNNo04W97c9QGJA9iko59nWryIu5fmpTrEo_O173ZnrOqvsKyjKT9yJb8QKOCt0uTg_lpGL3icwPtRrlZXO9xDLdijRMVOrOaMvSkAGTcTX_esvYUyyVVtHH1dLgneRQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.83M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 19:37:35</div>
<hr>

<div class="tg-post" id="msg-440447">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قالیباف: نه به آتش‌بس پایبندند نه به گفتگو باور دارند، و با محاصرهٔ دریایی و نقض توافقات دربارهٔ لبنان نشان دادند که فقط زبان قدرت می‌فهمند.
@Farsna</div>
<div class="tg-footer">👁️ 364 · <a href="https://t.me/farsna/440447" target="_blank">📅 19:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440446">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb98e9b506.mp4?token=Xw7WRZ4U1DmEIp9P4MtcouDTAW0KBNAPYBcrhKMLWFRsaD9ZjLjjnbVS3B8XTODp9i_Yn1p64l13nzBmhm3_mZw7lMkeMkXzopb6Gg1G-jj_v3O1aoAqMhJ7ka_BfQ8MLJ2l2AFwVWlC_t1laqkW5jplZFuY0OFvAlskUBOp3oWfyAbc5x5I8vDIPNfcY5WH3eB3w9Gy-x-ZFTZxVuEg8bTEDeHdWfiYte--X1xjSEHONPmC2RY0GTWA27skGYKT6sC2YIgIt4zVWsTJ6icNhjk4p4F2C7qIxZyB3K_eFfjhnLfwX9Qp7Z1_0nwKeYnS9JFlFaAJVG8kwPPKxBcqFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb98e9b506.mp4?token=Xw7WRZ4U1DmEIp9P4MtcouDTAW0KBNAPYBcrhKMLWFRsaD9ZjLjjnbVS3B8XTODp9i_Yn1p64l13nzBmhm3_mZw7lMkeMkXzopb6Gg1G-jj_v3O1aoAqMhJ7ka_BfQ8MLJ2l2AFwVWlC_t1laqkW5jplZFuY0OFvAlskUBOp3oWfyAbc5x5I8vDIPNfcY5WH3eB3w9Gy-x-ZFTZxVuEg8bTEDeHdWfiYte--X1xjSEHONPmC2RY0GTWA27skGYKT6sC2YIgIt4zVWsTJ6icNhjk4p4F2C7qIxZyB3K_eFfjhnLfwX9Qp7Z1_0nwKeYnS9JFlFaAJVG8kwPPKxBcqFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده  @Farsna</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/farsna/440446" target="_blank">📅 19:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440445">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=IkWH1QsVCsuyAb4-roYCsskfgrzZQXOrGITuj-QUa-CPeuXXh-Z0fpXiOEDmH2QZW7zYcnykUar1bkIWuR6MOJLTMEj7knTLW-hwIRV-xBBY7sbIoSszu3e7MxqwawjKDETZnl0iFH2J0GK3wXcOsBQkikbX0fq1jqPqjhAUC6re46nzL7ftZJGgFap5IjfUcNtF8y4fvX8WDEBO8SMauJxMj2mNmOdjct7GzJoQtpzdGowWa9mfRRxYD0ZylAJNPonvBB9KEj8tyyTIHaTRdN51b2J87e3mLQvoukJ0cfgVOrAra7FDvQBOqfOiMX8NRunjL-ZKN7Cm5o-LbqG-ulpx-th_Zt7qTAsaF3b5_7W2T1lx9vYfWAq9crEYTRSbElDyvY9zHhkiB0AE4IpNv3dNPw_sRdPKJXiaxuLaSgHwXlutQWvqgvTeqatwCjiAsYSaprdSeMMwPg0naFxkel0edAL7ZUbm3ggpQk0NxsUqD-rDpZQlSOyGvKCU4Z0Wh2COWXVuvWbQDMC8W2-50At4TL30GLFXM9619aKrN4velpOELWkslt3PWhCbYaFAZFXVNGp8uVd0IwoRuveujckKrpmiL3HFccsrCISlTYYuhV10kc7G2egBTAZWYeuU00zsGENY_SwmygxvX6ZA79C2BMIGOqOKfd6ZCToawBk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9383ef4fbd.mp4?token=IkWH1QsVCsuyAb4-roYCsskfgrzZQXOrGITuj-QUa-CPeuXXh-Z0fpXiOEDmH2QZW7zYcnykUar1bkIWuR6MOJLTMEj7knTLW-hwIRV-xBBY7sbIoSszu3e7MxqwawjKDETZnl0iFH2J0GK3wXcOsBQkikbX0fq1jqPqjhAUC6re46nzL7ftZJGgFap5IjfUcNtF8y4fvX8WDEBO8SMauJxMj2mNmOdjct7GzJoQtpzdGowWa9mfRRxYD0ZylAJNPonvBB9KEj8tyyTIHaTRdN51b2J87e3mLQvoukJ0cfgVOrAra7FDvQBOqfOiMX8NRunjL-ZKN7Cm5o-LbqG-ulpx-th_Zt7qTAsaF3b5_7W2T1lx9vYfWAq9crEYTRSbElDyvY9zHhkiB0AE4IpNv3dNPw_sRdPKJXiaxuLaSgHwXlutQWvqgvTeqatwCjiAsYSaprdSeMMwPg0naFxkel0edAL7ZUbm3ggpQk0NxsUqD-rDpZQlSOyGvKCU4Z0Wh2COWXVuvWbQDMC8W2-50At4TL30GLFXM9619aKrN4velpOELWkslt3PWhCbYaFAZFXVNGp8uVd0IwoRuveujckKrpmiL3HFccsrCISlTYYuhV10kc7G2egBTAZWYeuU00zsGENY_SwmygxvX6ZA79C2BMIGOqOKfd6ZCToawBk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نبویان: زمان توافق نهایی در متن مذاکرات نامشخص است و پایان تحریم‌ها به آن موکول شده
@Farsna</div>
<div class="tg-footer">👁️ 1.67K · <a href="https://t.me/farsna/440445" target="_blank">📅 19:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440444">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39a90f4ea9.mp4?token=nPM8coMniA1TyeRHqgnmG2_e6nURPb6uyqyF5xOxKoALf5D5imZ9UbkiTnp03064XzlV1Q1wxoFZb8CIvoRObqioohJ-Qog3YCavjBStPUR8ec8Rvbzc4wFDfUHdJCZs01mWWxgjVNqRhNLDai9Cy4-hqYh4m55L5PjB7bEQgQPm3OFUFsh3fLSmh-0wcTkS93QQkWx1Jd93_VBaH364gGc6Ssa7FOQ4IRd-2rALXVfFtsOhO-iSdYc1F0pc_RCT-BCaAPzEclbVQlL8ZVTEmVM6zJ2YnCycKYE2GwCvAG44aO2uhKEO7RB8G3gF48UNQ4cCRK7LW1rdrZ11fWaowQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39a90f4ea9.mp4?token=nPM8coMniA1TyeRHqgnmG2_e6nURPb6uyqyF5xOxKoALf5D5imZ9UbkiTnp03064XzlV1Q1wxoFZb8CIvoRObqioohJ-Qog3YCavjBStPUR8ec8Rvbzc4wFDfUHdJCZs01mWWxgjVNqRhNLDai9Cy4-hqYh4m55L5PjB7bEQgQPm3OFUFsh3fLSmh-0wcTkS93QQkWx1Jd93_VBaH364gGc6Ssa7FOQ4IRd-2rALXVfFtsOhO-iSdYc1F0pc_RCT-BCaAPzEclbVQlL8ZVTEmVM6zJ2YnCycKYE2GwCvAG44aO2uhKEO7RB8G3gF48UNQ4cCRK7LW1rdrZ11fWaowQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حمله راکتی سنگین چند روز پیش حزب‌الله به مواضع نظامیان صهیونیست در شهرک العدیسه لبنان
@Farsna</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/farsna/440444" target="_blank">📅 19:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440443">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NuNS32CuT_5RQe52GZw-RW43JmHcOQX8WSMoVO8G4ToGjhYx05oWqxADMWIuDWOVOJW3sBURSZQAY1C4GrjixWpQMCCgMpTECj2K6nGHc2DcxLSVOG3jPUxo8GvU7nEgDoQVqrIHYAxdbRRTCQGkesoqLW7P7eFVLN2W3r5Y-3Sl3pClqGo37W6q4rw4q_HCJTYNIdPH8XltzOT5_vTw4EOk41YXx0O-WT8xUvMuTwdoyVZDyUchMJOl7xUqsI7D8ujBCC4df8mdsXbXXQP3O-i2_sgf0UdBW_gvR-GGNXeQZA0W_Fz6B3GPhFvWRprH_ZgStn_9DVcWfSW1dnSz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤝
امضای تفاهم‌نامه تامین مالی نوین دانش‌بنیان بین بانک صادرات ایران و صندوق نوآوری و شکوفایی/سازندگی نوین با تاکید بر اقتصاد دیجیتال دانش‌بنیان؛ نقش محوری نظام بانکی در تثبیت اقتصاد پساجنگ
🔹
در راستای تقویت حمایت بانکی از اقتصاد دانش‌بنیان و فناوری و تسریع در تحقق سازندگی نوین مبتنی بر اقتصاد دیجیتال دانش‌بنیان، تفاهم‌نامه همکاری جامع میان بانک صادرات ایران و صندوق نوآوری و شکوفایی به امضا رسید. این توافق با هدف جایگزینی ابزارهای تامین مالی سنتی با روش‌های نوین و حمایت راهبردی از شرکت‌های دانش‌بنیان، گامی مهم در جهت حمایت از بخش خصوصی به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/farsna/440443" target="_blank">📅 19:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440442">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWoARGjZ4hrH84GjpBCrAyOwY-iFbJJ0adGQg_KkYSqE9GfHJu9U_tiMzTTgfoq_Rcxl4wGnZ-lsUMJIm9xeALJ4Sk0GhNGt12k5r6OQk2qWv6KYtx6QpMQhQb7F6APRfl0lZ8z0Gz25HNDuuq-znMn_CJLHAVpebkc7-L-teG2HXua2O0nRDy8XHXz6MizS_kKo_GGbLbYd1KQV7nzfZojmJBJDq60xPWbzA8whQ7-Psowh10I_qaStxGZsQ8ejC9qjaMHoF1T3ZcWzHZr_E4JoSA8BIspDde66IjE87QH6Nx-pzKMpVvXqw_ls74sc9TbvFBlVVbLro7MHKyCpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
مشتریان بانک رفاه کارگران معاملات و فعالیت‌های مشکوک به پولشویی را گزارش کنند
🔹
مشتریان بانک رفاه کارگران می‌توانند به‌منظور پیشگیری از اقدامات مجرمانه و انتقال پول‌های کثیف به شبکه اقتصادی کشور، گزارش‌‌های خود از معاملات و فعالیت‌های مشکوک به پولشویی را ثبت کنند.
🔹
مشتریان بانک رفاه کارگران می‌توانند از طریق مراجعه به سامانه گزارش‌های مردمی معرفی شده در پایگاه اینترنتی مرکز اطلاعات مالی به نشانی اینترنتی
fiu.gov.ir
نسبت به ثبت گزارش‌‌های خود اقدام کنند.
🔹
دسترسی به این سامانه از طریق سایت بانک رفاه کارگران به نشانی
www.refah-bank.ir
نیز امکان‌پذیر است.
@Refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 2.7K · <a href="https://t.me/farsna/440442" target="_blank">📅 19:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440441">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/440441" target="_blank">📅 19:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440434">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WjJPtLw4QDovAGKPsS-qMQDDXHmZInILSp_cSQR-QV__dwhForD0jeyj6TJ4FSQlZwjVyMFzopdAVui8eNC5GGQMGe3_suRFEKRldoo744ZnfY7zWfGuIAH_rkhdzWTSPWGCK37xLfdzHWRYX93IX1iSR509Rv2cs3VTLjD31eE4pEllKonFXk4Z0wfBcY2UuHS0HOSNg4-3mxx8vDmInl9rxiomqMNJRNUGog6ErijSkqg4iRdpuPDv9XTE5PMoL7AkeMVmLaYXO_oQtXRnXhPlShiIr70Qg7ApObc0LXNi99LfxcSZwaYUy1eHTH4vX2bzsxj6g8UCwuON0J0t1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGx4zvBxikedHqGdvSLrA53SsFRCkYt_g3rutBvnky-gcQP3SGtFABobkhbljYaJJ0D356bAu9eKwwh_H_SZmUopLCd-q-5Jbq3dAHswA9tUPY1KzXK_M4yn3U87lEC0eZgs-EsXpCzbZAOgDqrSUdzWAtXMy53Mcd1FAMf5v00ODBNTz5RVg_heoSXitFp5S4BvzFGX54pI1aUoos5fQ5cxVAaTcS2UNXts_XEPkeYZsz-0rehMKAxaiVHHVQo4BUK26LK-CXwGblWKtPM7NaGX9bS9dI-GRE18k1vB3OWGqwLuLFeQmzWcu6CaxOqb5P_9vpW-oCzA7L54f_YwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYct5nwnwyvT1H0dy39Zah-yriWC94-fP44JxXXNWlbTxdX5rwORvOIKZHY-vB1N8bZERtt-LE7TvRMvZB523548W6ch2lbVjXxp8LJiRqQDmRirQVsg5Fkkn4IhXoPxfgdVsettiJzrejiTLlPXkQCNICRGLHodIbTY29gkAwwACFWQy3yGZhM8M76sh8JIEU30rVakiNhoq87F_Pho9rOInZjW7348bkhS1yUI4L9IV1mnB98-Dddn5l94NDe6T25UlAXe0ZyJ80kjClgm91DtyYvBoaeG85pVdqzQRZG1bZUx_tgmeN_FtHjSEjcFpiZqRC2UVC3Zvfl6lyRMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIpQOkeCpFCCP95AZnzVUFtYM1cgQUgW2akC4LP69B9f5S1CS_xYHLbs7twLX186udfinb0H7ZDqj_k-B1GMJ_tJrE6Tw7d0npgdBOw1lZ2jgD9qex6cG24Xnd81d_hXAJuHOUwaERqLDOnoK5rUbxkkUYwec7fgSqqhTXNdV2muT4YG_MsfQ-9J8yRkhh2d_9s50Vmfrl2eVLJmxIznsINVAejp8lwXOeTf5djSZUK7Ty6jlPW4NfOwTnbOFnE8LOC0VLbdwC6k6421bdQdQ_1DsT2-tu5pnb_Baz9Letzo92IgvGEvB9QksN35gf_ajUxJRek6s0idE_Bo6mApMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YyQEhHKpbEI8t9Sl0V8wZ9gJQ1ND-oiuiFQRDbDvW044BogJlBc2Ng-A18YLen8JLfBfYhX08agLzc60wdBe29XywPjDaXSafKklHI3SZ2HPTzV7jiq0bPLeP-A7r4Frx1S9L-Zgoqlf7TPpZ6YrBgfvo_ZfhWbFuxdBol9o2cjQxea6WpgasO5xHCXKWiBEJm4GWQqGmcJBiwUT2OsJkLdhp7risanBNoCLRY_1UYN8jbXbCNBi19O5AB0aM74iM-trA1J6hEawNytym7hCkoACFn3VwXIypzd1Nc_BUcgcYGWGHTI_X5tAQVr9zfDbnboANifVgR7j5AWS-a1kxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HO8Iy1VBc7IDArDA3gE_up9Xbo92iRPlsr-L9vO1TytW80srV6fPaC4WEa-EzLEpZmaDyS39yOMSTb7t1lczh0MdlYFpG552g0_eDTefTgmQSmE7XicyobAmYw_YCWopOGPoEFQIAW18xH-230ioPQUn3_G6WLOfK1k4BKaQT0T1KgGRUHdx-cTIdVvFm0FEwe6m43tVpnDMTGMnAIRF-dBW3ZPnKNdzjgHd4Hn2ekmb3pemy2ozlNObRKTIyNbeE2UYgNvxLg0aUO5nXy9UWADUbbpzghaUxduos4oB3HUWNmbRIkxVRmHKp9IaAhwrUp1AMP-NjHodZw3s1TAs2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت شهید پاکپور و یاران شهیدش در حرم رضوی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/farsna/440434" target="_blank">📅 19:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440433">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QxZJHTCd6-HJTihQ3a6pt_zfY9YShdm9Zp7gog2BJVNJeO2JmWmZTHzCVf3H8XI-AiLosJPtb6ALMOldVG4NLdY5MZJCy4UFIk7tLhSk9JIvBHyf18OHX1W_C6A8_JdxIMxDVArSgEC2zGIE2V7Tmva03XpwSECwM-LSnJW2ufVa7qdMkW3HU0mbZRfNKjLjxy8jdVslrhhbScbf1-PChAHSPgZVHJRUc78EBy1QcueVzQ6FrVHSTbbf2OkMkTUQYAskTP7RhKlFUPDbU9y08GGlSimwrujl4bMxkQ811Wgn0jY51RrgXQ794QnYQtR4mIiq_26QY67J7_nSFvntsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
مرندی: صهیونیست‌ها مجازات خواهند شد
@Farsna</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/farsna/440433" target="_blank">📅 19:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440431">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">خط-58.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/440431" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۵۷.pdf</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farsna/440431" target="_blank">📅 19:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440430">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8f8a22db.mp4?token=vCfntdSw8d8_GqErWoI8d9skVZO0U9nY9XMS8ve66TkRKPQmbdo3G8Dhn7QaCQw64FxMzjv5YCbvvB5GGTBPXV35Mhx04wKY_ax1GI4wxBmJN6Ori29vf6gmcFqZHrAU13_iY5RQQIQYw-RGtMWHw6Qjd93KuuO3Q9bM14pn6Eyez3HLsqr1Uh-M3xDErP1ul2i4NNum5TZ5z970iiGPYJuwoauWs4JAgq8Wr3-od9-tSU-4ZkcxBOeeyl04bPyxDhOciRr6ESmHXIRPzzvqIkotnDMTYmi7gd4EOaFAYFEE5SIICkzJDt5h3vaLx5P8wwP_crqQ-SLRUok3II5jCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8f8a22db.mp4?token=vCfntdSw8d8_GqErWoI8d9skVZO0U9nY9XMS8ve66TkRKPQmbdo3G8Dhn7QaCQw64FxMzjv5YCbvvB5GGTBPXV35Mhx04wKY_ax1GI4wxBmJN6Ori29vf6gmcFqZHrAU13_iY5RQQIQYw-RGtMWHw6Qjd93KuuO3Q9bM14pn6Eyez3HLsqr1Uh-M3xDErP1ul2i4NNum5TZ5z970iiGPYJuwoauWs4JAgq8Wr3-od9-tSU-4ZkcxBOeeyl04bPyxDhOciRr6ESmHXIRPzzvqIkotnDMTYmi7gd4EOaFAYFEE5SIICkzJDt5h3vaLx5P8wwP_crqQ-SLRUok3II5jCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ با عصبانیت مصاحبه با خبرنگار آمریکایی را ترک کرد
🔹
ترامپ در اواسط مذاکره با خبرنگار رسانه آمریکایی ان‌بی‌سی، پس از سوالات این خبرنگار، با عصبانیت جلسه را ترک کرد‌.
🔹
ترامپ در حین ترک مصاحبه خطاب به خبرنگار گفت: تو یا فاسد هستی یا احمق، رسانه شما هم فاسد است؛ همچنین رسانه‌های سی‌ان‌ان و سی‌بی‌اس و ای‌بی‌سی‌نیوز هم فاسد هستند.
@Farsna</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/farsna/440430" target="_blank">📅 18:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440429">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkClwBI3idoDUj-kV3NZvmo_-QRXMoqylMZ_QTtqNYk9KtQJCtfzBHlMF214KdY8h1vEXagQvZUXDcDIcu96GmN_hbzjI1-KyhCXXAgvF3GT4Uhkvo4kf6HkVQKxjF5Vl5RNq7dJ2f6vjFOyMaiUjXaaC8RSDSxMfFAuY4yiIMjUjkU-2W638gPkwWiVELBTZIrYgg6TClfOZBMwWufeY8ccd8AU7vbMfX0GHdUfdbY65Mi5EE-P8KstkMOcct7HNP_EaKncr9LrzJPzwYcrXeOxVg-qCHeD9xYQBTmPK_dNcaoLiych5AsNXQNfOCv5_VLJum6WTdvppT5r9xj2ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی کمیسیون امنیت ملی مجلس: به حملات رژیم صهیونیستی پاسخ قاطع و دردآور خواهیم داد
🔸
امشب آسمان سرزمین‌های اشغالی را ببینید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/440429" target="_blank">📅 18:42 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440428">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-gUQXGa5TH1eTCKn5PBodOqLDgqpgIJhkofETh9_kIk581gxq2m2QeWuIpTvfIXUHAKaJPOUAgA7XWUZYom0Pptz_gSqwgS97r5PtZR4Szck2AZE2FJ5D03JC2TZThbwqrrUpIFqVx0vTqsxHyJGD-yxO5b_F3MApZWTW01EuhPYCp2xdswdjrLmCDVOiVWi_MuEuS9MmiFgUqViE8x4p6xVIQuBVCO-_3ZMbnhHKevWK6SbL-woPPAVFVPVnhHgyOuLdgyku4JvLrJoJfpkK8WjBcgzLBIX9l9Y1-SqgBHkq6K8DDYeCkLAxGcuKdx-cSOOCogm_HMQAMU6P-rLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
کاروان ایران به مکزیک رسید  @Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/440428" target="_blank">📅 18:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvfSikICAkfwUk_1BRCpKNuFgCj1A8FN4UAAHmFSlxVvlehvyBTFjUeVkgT9ZnfJtIdvRLyQkKZcv5Q1xPJsbn3eFvhl6ymd9neiGWwk_wcZAk7kf8V4lEiYNcK8pVxyz1EsdggArKW-bZ617nWDCJaUGcDAVpZCXTHOtd64qXubLzH22BhX5P9XUKFtWXsYUUY7Kk5FZ4cvlPoXAy3SlTIKTPpWYp_jKUR0WbwFyHu7Bch_HMfF2BrQLhIuZbDbFwsT9FbRKYCDmGrYaBYuGTppjZU6Cofsi-fgBPzbFoBgrIi3sWE0A3rRHqp_8QQt2IeyJEY-5YBmUpqaZVEBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrOP_3-iTpaUtkzJ0USp1giDSWxW9cj5hmnNh1dLPC8SW3aUIREe7NMcj9UZVRWmYX8Nd2Vlrba8P_8bjrYTa8I6UF4oud14IJfOnCsRVz7hTBGXZFOrgK1eX9psLKVmmglCKxzQS3lmTA7AdAB1JCq98s8enisESnBiLfdJX0uAd8K1ulGjiTerbj_0zmH-7qKxwmGmsoxtypJGW_FYxo2llXSrS7EwhmIdjQfHbtKsI4a_ftphTIup7ZGj5sEWiRV8bZkWJERTF6QhfdW6h_QmVeldWxxIGYYJfCgFtzBXbMHMoMjwhwEpo-HLxUe_jOQHZoaE089VR_I4_Rd6bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cu6gpeil7c4KLTd7CVaF0oC2AXac07cgB5avQNNb6adtT727TvdRG15L8w00nHYmRmHM3BehzEqUetKDQVweIIApATglAk4MfqqMLc0p499mJE5RPLV0g0ZzjcOzzg-HPBEGe346Dnbcn3V0yU5Gk6HadRUjo5_gI1NPTRzfCj416U4HTS0-o2KyFMDyieGvBXZRTnblZZ5ww5Lpm9R7HPCBmb4HLR5NzD-AonybhFOKqjXTLMNPANmU9XilaxkjWgsRVbl6b8mlQVNxo5J2QNlIPgJ79PRs8Jkz5z28UaI5wyoYkxsQ_OEqNzXSMwiruMp4N4QRGx9T-ksD7r4otQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVr92kIb029aB9DQXinAkm8EUMD5kdLVIH2aUylbb-LpUOpKEWIWDQ5CrvWU_WEeQlLciavOnWSdE8ACEiUYs4QVDXy87JUlYqH7eU2ycqzCg3sNGWUJPJeZPXlXSMmmCB4jAktJsJzU_nNPhO8UV3cl33aug97jC2kDM9eWaIt2os9dt04wYhhOcnt9FNly0e6Ma9r44rjBl8Fbmdh65Sn14nCXVv9wgCXuugJprJWm_jDaTCQDhSdLrOiIk1_jmJwKiHmMr5yBZIh_Ae3m7RMamEnAiN0mESXvi557kga1CF-vGQcN_Lx-bXCKAO8-0SEXyHwlqQqo_I84_eDDpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wte6MoNVxvyvFND3ycoaBhxlsdi6ImnRm-fILF4tjjLVeiB5oItty7k7XlEis92kLUbuy9gN9PnjOYg4GW4hOCC-XVllBxiLH9LXDSYpBEpkmJz-PnwteUJ3hA_PPKskfSd8EQsERRD1V2XzUREzmrNEAFWed-Kb3N-VMjGVYFiLiSxl_OyfqHlBjWt0P4c-zJuR7h1Pg2cCwIZAOjiA_hWZd_Mw8lz40GO-hHyMH3_aAzh5DcJO-WsFzNcUCdoTR0zZ--mmuxIeewtVGTLG___SmG1fz6m1R4_AsM3RHiJGqJKHDw20Y-XXdgD0xtUFZ6TsVrXRuYJ9TJs8NllTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdlZfJBVuXzoYWgfAKS8jsX9riHghG11g5nreE2zSEDF28K8tUi2xR9rbHtfappsSrhAMWZGZLRKLa7HQo8S_avPi_NRF4Wd14YBcVWh-1iqzDcXIhGyEZPmx-_UxXA0L1pe3ap6L4bWxZeyZM5TpzDbYTtCU3kgILwUjH_EbYhon8jxo-9dZnrGTXkm2KqwqPqq7kyFXq9CLeVTb7hEcIaUJWK8msFDXpqGPx8I7heHk7q_xF1O8GGjgyu8l4CTpS9AUqSkX4X8Gxng0zfXzS4sOfWNTKNkaJKx_EXK-G4SmWiRyqanykr8BSaX-TGdLFIuBK4PrZYczVMYBBXVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iloeN-s-8WfWf7mtEh6e8QoD_4rNx8h5UgU3eG3Ip1ksZRcEIDB3bpv26Xa9RJWibwJMIO4xfGT3375mip73kbGGIO1QNicqc95fAa-gscdtj7hmzU8gnlSgRvvILZTotOK-zaRKqs46EpPIGrkuvSgd1ktObPZu6VGaKAOKYie57X7tD87cxZTHkFo1y9gBoyjX4mJfOJ6-ZVU1Bu_dH4G6wsFULCIk0uLBnolZsnT5zhRHmFmc8GGvBenxbp_Ot8oDEfgtaO6UyfVj4NNwutRCd4CXvpVHfpZDe9vBByr0H7DX06vtxup1Ajyh3q3bv49n20ozLF6m02KjY4qZSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بزرگداشت شهید پاکپور در حرم رضوی
عکس:
حدیث فقیری
@Farsna</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/440421" target="_blank">📅 18:20 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
حمله به «ضاحیه» بیروت با چراغ سبز آمریکا صورت گرفت
🔹
شبکه ۱۵ اسرائیل خبر داد مسئولان رژیم صهیونیستی پیش از حمله به جنوب بیروت، آمریکا را در جریان آن قرار دادند. @Farsna</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/farsna/440420" target="_blank">📅 18:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440418">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG3VD6UVoLgPD2eh3VkeFrRl_4r7Wdcd1S2rQrIyGZhVrsyIcA_qr5wL5wHaq6X0fvplYTYDsciNa9dr9DRByIhYHTPH4sp8C2LxaQkJaAAtgw7pcKbCAyR9O8nsOBqUM7uT1BqzKqLt4WGoxBg4_cxJKCvB7ZYk6wkEWAUC6ihaeHm9rqGOh25PTifnvoEA6Zby5qAyqjznWgq6xVbKZAtI7BtwICXm8fMyYiuUT4_9GSF0oALYWPp50truHHuJyDJoLjz7H1dicEtc9c4BQ82_UWZv43U7eF-1ZLLmgCmRePjLjhyaN8gBwbtQdso9HMRqsbS2SYzYXln5yP5ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fdea240b7.mp4?token=aTEJ1eKFh4ashlTkppiLk4_XAv2_r1aEUHqx1M7U8xTU4MuL4HCJSTqyrL1tuqVEHjcK0q1fc9hvoQNB4u13ttOD38R8twvTWM8DvAP4sV-qTrSOKruXJ36DB9dgeBy38VE95bj9hpy0VWXbUzGYYu4g4uTvtPiqNqTVLI4oTQ6YZRrtP2iv2Mvfb65XIorD8F_S0mKhUKAHFlaCVhSAC-caX2aNvK0QQdIvG6vZr6sMgHvOET89BMxuofKRUuTreuDfDgsi9GgS89CdIwEBIikrPuUe8BTllSwhhyR7ONMwh-KfFEppy8maNnmmqqmIi1yGh0meS__EcewyPj1V9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fdea240b7.mp4?token=aTEJ1eKFh4ashlTkppiLk4_XAv2_r1aEUHqx1M7U8xTU4MuL4HCJSTqyrL1tuqVEHjcK0q1fc9hvoQNB4u13ttOD38R8twvTWM8DvAP4sV-qTrSOKruXJ36DB9dgeBy38VE95bj9hpy0VWXbUzGYYu4g4uTvtPiqNqTVLI4oTQ6YZRrtP2iv2Mvfb65XIorD8F_S0mKhUKAHFlaCVhSAC-caX2aNvK0QQdIvG6vZr6sMgHvOET89BMxuofKRUuTreuDfDgsi9GgS89CdIwEBIikrPuUe8BTllSwhhyR7ONMwh-KfFEppy8maNnmmqqmIi1yGh0meS__EcewyPj1V9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژیم صهیونیستی شهر «صور» در جنوب لبنان را بمباران کرد
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/440418" target="_blank">📅 18:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440417">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5357002414.mp4?token=XhNmuFbK_omm_G7f9djr-5XtXT_FVJY-_D7tEWdlIc43m43fQ6GavlMRcNDijyR0k1nzNpYNllUJ25xFPe43VUzZNdcJbolcqsDAU7-AsYP2rTUxAE5hbYm89Cyiq2aEMbCvyc8Gom0pnTy67sIE23FvEJLNq9R7ZSq42mx5ABnJg0LfVsaDjgJ_Xt-pmY-KtNlB0HE6cE6HoPJnfY0a5UVXVb8_cL9FG9EH9i5T_OLzT6xUMkKVn91rxd7g3KrlCfQyzlOoAftw-tiF19Ts8gWOZ5OfVOi4xdNV2__GFKBhmZvvqU8qHHJTWzlSsJWq6roZkUH9djG0k2AfNOuNUi4glTdwP1AIqhSWoXvWfFCrQICR-TBqbmZDjnmc5mF_MV3ziidk85pv2pO3AIKv_NRItt5QH3aR6Dr3jTxXZmqe53xyVoHL3XqFik0fvlSfl3kLlCfN7xxUw6NAC-3KyEd5mElG4fA7ZFMxYhYIre7BXpwAb3IAIWGuGbzpjNZokc2GLHnbDxayi60OSN9Lzsytvl4VIqn--dkgbkI3P6q_KTzGXpkyTjU6NvjZNwqGZiv_shzlviTQpg-svv-FyEflWaUBCBkfkOxikonajPBO2l1TViiTVr2cKpmju9aCg7tDJdjg1XZphKjnYSoKQineP9SAlMJKlXEE_JO2wJs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5357002414.mp4?token=XhNmuFbK_omm_G7f9djr-5XtXT_FVJY-_D7tEWdlIc43m43fQ6GavlMRcNDijyR0k1nzNpYNllUJ25xFPe43VUzZNdcJbolcqsDAU7-AsYP2rTUxAE5hbYm89Cyiq2aEMbCvyc8Gom0pnTy67sIE23FvEJLNq9R7ZSq42mx5ABnJg0LfVsaDjgJ_Xt-pmY-KtNlB0HE6cE6HoPJnfY0a5UVXVb8_cL9FG9EH9i5T_OLzT6xUMkKVn91rxd7g3KrlCfQyzlOoAftw-tiF19Ts8gWOZ5OfVOi4xdNV2__GFKBhmZvvqU8qHHJTWzlSsJWq6roZkUH9djG0k2AfNOuNUi4glTdwP1AIqhSWoXvWfFCrQICR-TBqbmZDjnmc5mF_MV3ziidk85pv2pO3AIKv_NRItt5QH3aR6Dr3jTxXZmqe53xyVoHL3XqFik0fvlSfl3kLlCfN7xxUw6NAC-3KyEd5mElG4fA7ZFMxYhYIre7BXpwAb3IAIWGuGbzpjNZokc2GLHnbDxayi60OSN9Lzsytvl4VIqn--dkgbkI3P6q_KTzGXpkyTjU6NvjZNwqGZiv_shzlviTQpg-svv-FyEflWaUBCBkfkOxikonajPBO2l1TViiTVr2cKpmju9aCg7tDJdjg1XZphKjnYSoKQineP9SAlMJKlXEE_JO2wJs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر عملیات هلال احمر در خیابان ۱۰۵ تهرانپارس در جنگ رمضان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/440417" target="_blank">📅 17:58 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440416">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0036f2550.mp4?token=c802JoyXdRaTKbzIpzYpAlGYdOr2q69hlI5sDfJcjKxUC213Q4-bQJTQaABXtLZ6r6rW8OhdZl7wCfTWBYc7kbQfgaz16BM53-5WFmU__x8UXD6XraD-mnYqUQRR1zTiNiRxt52sV6jUu4N0RJT2OOuahsqRLrfm5rUYATq8y-yF23IJmSmGk-dE7gsUfDsk6gJU5a51WYQV-e_DEAEb7od3dsIEnaK78-2djXXRvid7Mo7fDWLnGNXi8ZDE_nGop9X8S9Vt2E-vcGzRpEZF1V0j95Z-_GkR9ty0RehnnEu0gxmldl3Udwoyz3IpVBghwPKHKqTp8y3A4_xzfLHXgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0036f2550.mp4?token=c802JoyXdRaTKbzIpzYpAlGYdOr2q69hlI5sDfJcjKxUC213Q4-bQJTQaABXtLZ6r6rW8OhdZl7wCfTWBYc7kbQfgaz16BM53-5WFmU__x8UXD6XraD-mnYqUQRR1zTiNiRxt52sV6jUu4N0RJT2OOuahsqRLrfm5rUYATq8y-yF23IJmSmGk-dE7gsUfDsk6gJU5a51WYQV-e_DEAEb7od3dsIEnaK78-2djXXRvid7Mo7fDWLnGNXi8ZDE_nGop9X8S9Vt2E-vcGzRpEZF1V0j95Z-_GkR9ty0RehnnEu0gxmldl3Udwoyz3IpVBghwPKHKqTp8y3A4_xzfLHXgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها با پرچم ایران به استقبال تیم ملی رفتند
🔹
جمعی از ایرانی‌های حاضر در مکزیک و بومیان تیخوانا با در دست داشتن پرچم ایران به استقبال تیم ملی رفتند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/440416" target="_blank">📅 17:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440415">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsNeXSrle-Uur0-n82Kcimx1VwqceygdT9dVVg4DKYjjdGW_yEFHrBy8zHE6BlEsXvJKAt_ZlzygQlAj6ldXOJrNtJy854Ces6uCjgpF-UhhR8q83yVQb9CGzSfIWvNB89LwWwLDsN_Ej7j_gAYxZcgtfDdHPkbEuHQdRqOsi-YqnQZhXa11VwYuURat8afKY9k9_F_9Y0jzwyDM_hiOXgbdyVzc2XjOFV3tIbFfOv_WNHvWnmtihJri8tZI5ZU9-lv5bkezdH2wuzdDk8-1xJgr0IWpNxjT4gOqKNP3whnt7KkBx1er_aVDndczjl5jYE6ib11e8fxv2DtqxZdbAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از قدیمی‌ترین مناطق حفاظت‌شدۀ ایران جهانی شد
🔹
منطقۀ «قمیشلو-دالانکوه» در استان اصفهان به‌عنوان ذخیره‌گاه زیست‌کره در یونسکو به ثبت رسید و شمار ذخیره‌گاه‌های زیست‌کرۀ ایران به ۱۴ مورد افزایش یافت.
🔹
قمیشلو از قدیمی‌ترین مناطق تحت حفاظت ایران است و زیستگاه گونه‌هایی همچون قوچ و میش، کل و بز، گرگ، کفتار و پرندگان متنوع به شمار می‌رود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/farsna/440415" target="_blank">📅 17:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440414">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQhzXMu_k9mPyWxsUHDeaes4z0dDKuI6apF_iTjrHtoIRmY42x8uHXHtblIYMKLckfcLpvYCig6oUxlN9XK_vm3dFQXcPtl_LB4GbUzgMIcCKs1OrMtgT_T1sFuE3DxcH8z350IpabkPVNHy4pOiM4H6Ue-UPA-DFrgqHQChUH3tNzARxR8E6mFILY6HOlZKkgBzD1-rUg60p2qu56-RIn3K5MH20LJaJxXmiIcWE9ryRs4K1o9KYJPVoCArjuulUPlugcolnbrtsuDrolvw8hzepgOQ9Hy5hqb89b6dL1Xo9ChVWMIOwu0PeKcGklBSs1-vwSyGWWyHYnPVjSAqJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت عوارض محیط‌زیستی در تنگۀ هرمز به کجا رسید؟
🔹
سازمان حفاظت محیط‌زیست از نهایی‌شدن پیش‌نویس نظام‌نامۀ دریافت عوارض زیست‌محیطی از کشتی‌ها خبر داد؛ طرحی که قرار است پس از طی مراحل قانونی، برای کشتی‌های عبوری در منطقه اجرا شود.
عوارض برچه اساسی محاسبه خواهد شد؟
🔸
نوع و ظرفیت کشتی
🔸
نوع محموله
🔸
میزان خطر آلودگی
🔸
نوع سوخت مصرفی
🔸
سن کشتی
🔸
سوابق تخلفات زیست‌محیطی
🔹
سازمان حفاظت محیط‌زیست می‌گوید خسارت‌های ناشی از جنگ نفتکش‌ها، جنگ خلیج فارس و سایر درگیری‌های منطقه‌ای، آسیب‌های گسترده‌ای به محیط‌زیست خلیج فارس و تنگۀ هرمز وارد کرده و کشتی‌ها باید در تأمین هزینه‌های حفاظت و احیای این منطقه سهیم باشند.
🔹
معاون دریایی سازمان محیط‌‌زیست اعلام کرد پیش‌نویس این نظام‌نامه نهایی شده و پس از تصویب در سازمان، برای بررسی‌های قانونی به مراجع ذی‌ربط و وزارت امور خارجه ارسال خواهد شد.
🔸
جزئیات رقم پیشنهادی عوارض هنوز اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/440414" target="_blank">📅 17:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440410">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqoSj3XNLsdaDPQCIclet_DNOcFZjQrbWPV73FqMoqCK7KbIqiQtYTRhfWJEZlC_k-W6SMzRG-CDAUiLrLZPwoAMXmJvl06qMdLaDttZXQI3LzEH5jcg54xaNHCcTx6mjGiEKi8hpOy2C2godsPYVmevUKcA9fqIp0Xd2x86iQI6sGxzWH4qPfnpsCMa20JNZDn8AH0IVmnvvuUYiNPQ58my3SQ_LT3gTbbX1vWHuPmAvLrpeNgI3iT3JRIAxwxOwyuwh6MMLUtbbSeoG5__F92uU0PPN9OMrt05V3TUMS5BHHZjMtEjaWdja0JOYcuk-hi9d1nohZxTsYKuSX_1VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkxIsxucXfknsmaZ4N5qGERZBhkw7EutmNrdP8Zr8n-4GzCqQoL2dQL2xN1KljLQ_4f8rAaQ2bn7pBQKPwbVGaIoYXmvfES_siXMxObxJykFx3INiA8CaXNqI1ecwUnjYEKaxdQibgXLLtg-KODt9i6Bx4u679PzeobEJy4u71PWHJFHCLaqnxBSbqNFtF8xxB9Z6XRh3MPsLQ9M-9KtZtD4rW8UtfPB_c15DQ2GBSlvB8Q04ASNU4mCQXPX8SGhVGBwqLx0KZDoOZbXcKy1M7UBVSs83BzrG4tTwV6k1lmRhQ3a52DBOiR7j9W07kW34kcOOKULfG7YRwi9Tam2Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bplvZaOyKNE8L6YppUTj52RgWMeqGP1JbGL_V2eCv2g0awawLFZT2vDDOCqaDy2QYoW3002WVHypmLhhCgWRyZ4fPw_sbovwQXUvggYofPN6hCpveSgZN2WfrJimsZSved8ae25jikaaqJLKWyL-tEKCVWQu4qfNiUYow2tICeUzAKqHb5PAx4i-R8DsA7NUsI0ydJ7KKmxYuIXhnAi3FAuXthiXyygLHwYoZ55nlpjUTW39x3slzluJlQoJl4abTNgTArEzb5wZm5dcdPRslHTY1tzoKdwoYhKtBK1KfW_Y5TOylqUO37DxHaocbBet5eVFTLCxvMZ3CQSng0qAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jR1YqpuD2oTPj_pcIIxfnb67iFwzylQ6HKgQt72-_-fIBNku91gAHylrwQa0GRWN3vl3scP9ObWQAmh8HGTVwSOal2rWUGskFcYCejx9ZWz8e6PNGOwzKQJD9XooLWcqyJch8s9EDR38szcnDkL6Id7nL8FhNutF63ecSs2yMR8muCbPGA-j1Iol-moSzRCNcBVVBL8KchVKpWOfPIzaq6vGTHGWzrLC-43MQIxBiHRpVKBfGpgV1iifs_21LNwdAvUQDu5K65sZiORO6020h1ajsvkHIhrVOX8lZs-ST-9q4XLMD86G_QTpB9UaRzlKuyqvBvdf8vhgGF3fMR3-pg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
کاروان ایران به مکزیک رسید  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/440410" target="_blank">📅 17:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440409">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1759b086c7.mp4?token=vZoIOosMjlFE-aytu72PNN4v1nvKXPMu5hpbEpGNt0S2a6oZhHktN5sofdIPU9KsHyPmrEbGY29gWh5y5q_2UdAUNs158fdvZ-RAPG7B3_gLHBqDReI5qHUhztElv7e9mg8zt-AmALFBl5BuYr3xPeeR8wxW8nJy21D82wZjGNOqeXVg_4A0Am1TOIyQPGAgupoUzyVwYlMMv554iKedArecmvJHvy5nENp-URrx-tv3yNzvJqlVQaRGIes4dtCFEBoEa6GlEwxKLoEzivcnOtPIRCWvUkJVDD_MkcQuvmFE58HMquuJiNlvBvdjjpDYdbk_QyPSuTlThQ-ouLUkWC1QvQ0YzfWGKWGJEukEyBdYzSONPHY0fxukVYFku2wAN_hCFmenF5kt6ory_4iPnKAqOzmTYShGmr0uv7flGzoHTREfuugPiQPYzC92JxEd_KmDO6rhVpkusHWXlK0BwB9NqD8WEcX5xtKHecV9dXyBf75eV2JljsQP9vgc-6CTpg3DLWNbFR1Y5ol23fn9J2W5evzR4HacuXrXA_vtoCliJbzovK3XlSLTaNtJeBQc6WJDinzgwepSLqdMHrCR0yzJtiGURGFmtgXIChavAB6sEEX1WZGGN3NYHXAR9ZHoj296n8gO7PXKtzcwPFkmFoAwJPMCcO0TLX0MsdiS7_s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1759b086c7.mp4?token=vZoIOosMjlFE-aytu72PNN4v1nvKXPMu5hpbEpGNt0S2a6oZhHktN5sofdIPU9KsHyPmrEbGY29gWh5y5q_2UdAUNs158fdvZ-RAPG7B3_gLHBqDReI5qHUhztElv7e9mg8zt-AmALFBl5BuYr3xPeeR8wxW8nJy21D82wZjGNOqeXVg_4A0Am1TOIyQPGAgupoUzyVwYlMMv554iKedArecmvJHvy5nENp-URrx-tv3yNzvJqlVQaRGIes4dtCFEBoEa6GlEwxKLoEzivcnOtPIRCWvUkJVDD_MkcQuvmFE58HMquuJiNlvBvdjjpDYdbk_QyPSuTlThQ-ouLUkWC1QvQ0YzfWGKWGJEukEyBdYzSONPHY0fxukVYFku2wAN_hCFmenF5kt6ory_4iPnKAqOzmTYShGmr0uv7flGzoHTREfuugPiQPYzC92JxEd_KmDO6rhVpkusHWXlK0BwB9NqD8WEcX5xtKHecV9dXyBf75eV2JljsQP9vgc-6CTpg3DLWNbFR1Y5ol23fn9J2W5evzR4HacuXrXA_vtoCliJbzovK3XlSLTaNtJeBQc6WJDinzgwepSLqdMHrCR0yzJtiGURGFmtgXIChavAB6sEEX1WZGGN3NYHXAR9ZHoj296n8gO7PXKtzcwPFkmFoAwJPMCcO0TLX0MsdiS7_s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمد نجفی بازیگر: کسی از خارج ایران حق انتقاد ندارد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/farsna/440409" target="_blank">📅 17:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440408">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🎥
آخرین خبرهای حملۀ رژیم صهیونیستی به ضاحیۀ بیروت از زبان خبرنگار صداوسیما در لبنان  @Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/440408" target="_blank">📅 17:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440407">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e688388c.mp4?token=Qm80MivgIo_Ji4WQ-O-RsJXJZXipnSaqGtX1hdHpJYtkoAPg0MoAWq-HBf9t0zTzN_Ig2z75_M4rRNFnNWbjiGPsJRCPVELReB5M_bPAqj4l9Qb7whUPmz2OtBQySx8G1xbrsTdG77wErqY62RObuAVj3CPWQ74yPCrkogQa2WaOImzh7SY6mfzG0SD0vqRFHR21dKP2V7j02dIpNxSTt9njD2DW-_6bo5V2Jwg7h63E_eU9uVKUuRCsh-3upLzRui-jAvPI_Ip1z40hu1bzfqowaLIuGq58FMwaQdTcHVFoQT5-Jeto3Vm1USK8ELy-wkIxWY0395mlc5sCqvzCDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e688388c.mp4?token=Qm80MivgIo_Ji4WQ-O-RsJXJZXipnSaqGtX1hdHpJYtkoAPg0MoAWq-HBf9t0zTzN_Ig2z75_M4rRNFnNWbjiGPsJRCPVELReB5M_bPAqj4l9Qb7whUPmz2OtBQySx8G1xbrsTdG77wErqY62RObuAVj3CPWQ74yPCrkogQa2WaOImzh7SY6mfzG0SD0vqRFHR21dKP2V7j02dIpNxSTt9njD2DW-_6bo5V2Jwg7h63E_eU9uVKUuRCsh-3upLzRui-jAvPI_Ip1z40hu1bzfqowaLIuGq58FMwaQdTcHVFoQT5-Jeto3Vm1USK8ELy-wkIxWY0395mlc5sCqvzCDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
خبرنگار الجزیره: حزب‌الله با یک موشک زمین به هوا، یک جنگنده اسرائیلی را در النبطیه، جنوب لبنان، هدف قرار داد. @Farsna</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/farsna/440407" target="_blank">📅 17:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440406">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4ba37fd4.mp4?token=jlxmXkOQWa9ipJqQodewm3mgjNHxb1HoV4uaJ_E4C-20z3jCcVlfbWgwEloDZLykdja1dLeVSfT0qs_4I8O8A8SSdlL42WTEtmmt1Edu-MYUbsK3v3dF0orig4lrbH_F3boYfErdFhYgFn4r13qaHtCZkOuZg4Uj_51UoejzYD_VYlDd_QVUJPpCzAgmVZgAhvBKl5oZYC-ax5P2S5H-nWlQfFIoLZ_FI3o4DAv0FuzO4zOZ2fsRvxbeG8iXrk2SE9JmwS7ILWUZHqpKlAJYz9u_aY0OEryML5bVvQLkCov6ZVyY3PcFuZJvKBm3lPgZG8Om7tUd2GYtg1M6TQWerQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4ba37fd4.mp4?token=jlxmXkOQWa9ipJqQodewm3mgjNHxb1HoV4uaJ_E4C-20z3jCcVlfbWgwEloDZLykdja1dLeVSfT0qs_4I8O8A8SSdlL42WTEtmmt1Edu-MYUbsK3v3dF0orig4lrbH_F3boYfErdFhYgFn4r13qaHtCZkOuZg4Uj_51UoejzYD_VYlDd_QVUJPpCzAgmVZgAhvBKl5oZYC-ax5P2S5H-nWlQfFIoLZ_FI3o4DAv0FuzO4zOZ2fsRvxbeG8iXrk2SE9JmwS7ILWUZHqpKlAJYz9u_aY0OEryML5bVvQLkCov6ZVyY3PcFuZJvKBm3lPgZG8Om7tUd2GYtg1M6TQWerQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان ایران به مکزیک رسید
@Farsna</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/440406" target="_blank">📅 17:08 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440405">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">‌ سخنگوی شورای شهر تهران: طرح رایگان‌شدن مترو و بی‌آرتی ۱۰ رأی موافق کسب کرد و تصویب نشد
🔹
براساس بندهای یک و ۲ این طرح، شهروندان خوش حساب در پرداخت عوارض و دیون شهری با تأیید شهرداری و همچنین تمام شهروندان ساکن یا شاغل در تهران در صورت احراز رتبه در باشگاه…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/440405" target="_blank">📅 17:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440404">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqGBIu7n1xXlvcMxicTYuTf7dviuCYKuqLM2wBi7EWsRYuqkC7zmrWW2tN_x-8heTW6mJwh0BiHprqI9KNygP0p2JpsIuKJHkZMLNgzYxn7j1CWNdHcMdxcHENo93ANYdZlroqEbCuP503j2Emnb-lkIUom8JMrVZ8uVF7VZc_FcRLU-Cc1-I_YqJsZStEF5eMY4XrSO5Vv3_8EocxQYJMTE6d_IBZ0fzLOIcokx8ACnv1aecoPGyDUflibjurFAw6koKezobhfHM2lrVxeSS8nsXRTG_2ujrpWE-HdFMF9p0QjyB8bM88ALXQ6obwXNQr3Mly1aIl0JmxD_MwL1oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ به ان‌بی‌سی نیوز: من درخواست نکرده‌ام که لبنان بخشی از توافق کوتاه مدت با ایران باشد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/440404" target="_blank">📅 16:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440403">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f57S0iw-weZ57lEvJauLfeppRTBMRi4922mlQEnLTPZxefZFZtWPGM5l7QHBCsKgGQ_UAHkP6BqReKHP8y_6aRp5jFA_rQPadKr4CQNpNvZ8lmppbbs5aAMuJT3AkxOIaCwNrX6KMiWL-_D8puPv1CtUEKOdi826VL8RE2IcEVUK9YyLcpYQKuGxoAPip5cAhqoO7o-dKzJduJdhsB9tstSuQgTClbjU9DC3BK61jK3PINwtZhHJRs98U7OK5b6gZSDL7-6PHhyzRlP0p7Ogs2OiHuu5dwMgBdzx0fyOouXly6YPJPN8kmtXFtJJbl2fnx2anrzG_vBMYQ76JmgCEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترامپ به ان‌بی‌سی نیوز: من درخواست نکرده‌ام که لبنان بخشی از توافق کوتاه مدت با ایران باشد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/440403" target="_blank">📅 16:45 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440402">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‌ ‌
🔴
رادیو ارتش رژیم صهیونیستی به‌نقل از یک منبع نظامی گزارش داد که ارتش رژیم از ساکنان شمال اراضی اشغالی خواسته برای پاسخ حزب‌الله در ساعات آینده آماده باشند. @Farsna</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/farsna/440402" target="_blank">📅 16:37 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440401">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
حمله به «ضاحیه» بیروت با چراغ سبز آمریکا صورت گرفت
🔹
شبکه ۱۵ اسرائیل خبر داد مسئولان رژیم صهیونیستی پیش از حمله به جنوب بیروت، آمریکا را در جریان آن قرار دادند. @Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440401" target="_blank">📅 16:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440400">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff4573fa09.mp4?token=grZnqKBvRFQrt2ZGMp_ZCyQnC62lfTK68JKj7hTyY0yyJk6HQyMbZ9wgUjF28CMO3_rX_RAmyTa3qFPctNFPtdc-N_cW9d0MUALcQMHtmxeVc1KDja2J7IMr6NUKqob_ZFn9jtY7HnxlGDFEm1qd8C9_vHjJD8VRdndcu_4EPBwfs3UzyICkLNuUGYm3SbMaWm_8SGWruGE4rXTVRE5q1Rx2XAcH-VDlC0gs0BGILXrSxIy8QSKZVDeXpE8DwlS8zaqjBA7sn4rveg1kvuF7SxNzZ3NLCqt_E7Yk5pCi_EZeOU9zYZ7CerqsKz6KjgJ8hrZ5cVPtrzUxa8QLHpdIfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff4573fa09.mp4?token=grZnqKBvRFQrt2ZGMp_ZCyQnC62lfTK68JKj7hTyY0yyJk6HQyMbZ9wgUjF28CMO3_rX_RAmyTa3qFPctNFPtdc-N_cW9d0MUALcQMHtmxeVc1KDja2J7IMr6NUKqob_ZFn9jtY7HnxlGDFEm1qd8C9_vHjJD8VRdndcu_4EPBwfs3UzyICkLNuUGYm3SbMaWm_8SGWruGE4rXTVRE5q1Rx2XAcH-VDlC0gs0BGILXrSxIy8QSKZVDeXpE8DwlS8zaqjBA7sn4rveg1kvuF7SxNzZ3NLCqt_E7Yk5pCi_EZeOU9zYZ7CerqsKz6KjgJ8hrZ5cVPtrzUxa8QLHpdIfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رسانه‌های صهیونیستی: ساختمانی در منطقۀ المریج در ضاحیه با ۳ موشک هدف قرار گرفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/440400" target="_blank">📅 16:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440399">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5L0JFWARajqt_04eyekYtJ3A4CvPVYMf0utqx1lPjeKlRPp3ShCP2GwUduB27P5rzSBq3MGvYndCMcLhoZrGzmNTa16ZwJ3pFGXVWR2tjldFzHZAYSU30dmqnozx2so-a5E58cd0ZzpJlm3cvzdLfJL3wfuef09KZNIG3uofcwtx2tTwHAhEFAcTm1-cXOPyiwEMTKghe_v7rPPg7zAfzXKxXRN4Rd-yggp1IqChBH_Scj6Lo94vpImoxWaBpxuWuCxHrJPnGShWtERR9_dpC6e4-106bndBKyZFBKPi0aoIOyGOmu0kFxRldDU_a07nblZvVZa0oUvFdnCOwE2MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدادی‌فر سرمربی تیم ملی جوانان شد
🔹
پس از حضور حسین عبدی در تیم ملی امید، با پیشنهاد کمیته فنی و تایید هیئت رئیسه، قاسم حدادی‌فر به‌عنوان سرمربی جدید تیم ملی جوانان انتخاب شد.
@Farsna</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/440399" target="_blank">📅 16:15 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440398">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00d1abf1a6.mp4?token=tYz3hQAelD6JsmhGIf_UevVx5Yfz4fNH5VQXDUeFPAq3I5c_SI_GgG7jAU-XEAnVZD_gEb-i9rzmvR8RaUuuV-D4kqJ2O5Pn7XDm7LG1PIiqB40X49JbZvI2f93YiL0IPS-SPO7CPZm9h4ztcPKYP6grQ5o7kPJRKpWMJ7Qo4oxbBszE2dESUVT8wqKU_qMXNsyLVN4ObUdjTVZSmTFXtk7p1ut7LkOmI9dctyz8U0vKHK1EyTNujBTMfz6DTayT7Mj7oBh5auagw4jmyWNwtT2VbuljZcH1MViF-LdFSHFyq-cxlc7CnnnClwGHG2OnJ614dGl3KWLtiXi4Pd2AeYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00d1abf1a6.mp4?token=tYz3hQAelD6JsmhGIf_UevVx5Yfz4fNH5VQXDUeFPAq3I5c_SI_GgG7jAU-XEAnVZD_gEb-i9rzmvR8RaUuuV-D4kqJ2O5Pn7XDm7LG1PIiqB40X49JbZvI2f93YiL0IPS-SPO7CPZm9h4ztcPKYP6grQ5o7kPJRKpWMJ7Qo4oxbBszE2dESUVT8wqKU_qMXNsyLVN4ObUdjTVZSmTFXtk7p1ut7LkOmI9dctyz8U0vKHK1EyTNujBTMfz6DTayT7Mj7oBh5auagw4jmyWNwtT2VbuljZcH1MViF-LdFSHFyq-cxlc7CnnnClwGHG2OnJ614dGl3KWLtiXi4Pd2AeYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلیمی: جلسۀ صحن مجلس یکشنبۀ هفتۀ آینده برگزار می‌‌شود
🔹
عضو هیئت‌رئیسۀ مجلس: در صورتی که منع دستگاه‌های امنیتی برداشته شود، مجلس به نحو متفاوتی برگزار خواهد شد.
🔹
فعلاً تا زمانی که این منع وجود دارد، جلسات به همان شکل گذشته یعنی وبیناری ادامه می‌یابد.  @Farsna…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/440398" target="_blank">📅 16:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440396">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5343a7af7.mp4?token=lPVNrDrKA1NpaFi76_U4Qe4oPXziYFwPf5isnmB1HgP7DXG8O8ycxQynfjKQTcDHmNxRfmR0TYvMOL4dUgDe2YFsINuM_U6KANWARI0y-R87Zu4EwUxQdTa3X8yLCdOGrvAvLB-D173yJu26kLBTptbhp_vS_cr6s_7i8usIWaqjiJVnBnB0xWBsglna0CsrClR5Zko1ecLuRdqbgK3dmxzGJeCVfmW003sjJxSJTwGtMWqiTJsL-BqgvQLybzgUNxA-RAK37-MwFXATjov-5YGX6v2eR6wFWvIJdP-HX9ROKr8Ym9Y7xstVAV0BRlaiSKGe_o_7lhkjMLD-Slh4Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5343a7af7.mp4?token=lPVNrDrKA1NpaFi76_U4Qe4oPXziYFwPf5isnmB1HgP7DXG8O8ycxQynfjKQTcDHmNxRfmR0TYvMOL4dUgDe2YFsINuM_U6KANWARI0y-R87Zu4EwUxQdTa3X8yLCdOGrvAvLB-D173yJu26kLBTptbhp_vS_cr6s_7i8usIWaqjiJVnBnB0xWBsglna0CsrClR5Zko1ecLuRdqbgK3dmxzGJeCVfmW003sjJxSJTwGtMWqiTJsL-BqgvQLybzgUNxA-RAK37-MwFXATjov-5YGX6v2eR6wFWvIJdP-HX9ROKr8Ym9Y7xstVAV0BRlaiSKGe_o_7lhkjMLD-Slh4Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دفتر نتانیاهو اعلام کرد ارتش رژیم صهیونیستی حمله‌ای را به مقر حزب‌الله در حومهٔ جنوبی بیروت انجام داده است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/440396" target="_blank">📅 16:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440395">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شهادت یک مرزبان در مرز زابل
🔹
مرزبانی سیستان‌و‌بلوچستان: یکی از مرزبانان وظیفۀ هنگ مرزی زابل به‌نام «سیدمصطفی حسینی» حین کنترل و مراقبت از مرزهای جنوب شرق کشور به درجۀ رفیع شهادت نائل آمد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/440395" target="_blank">📅 16:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440394">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">‌ زمان صدور احکام جدید حقوق بازنشستگان اعلام شد
🔹
رئیس کانون عالی بازنشستگان کشور: مرحلۀ سوم طرح متناسب‌سازی حقوق بازنشستگان تأمین اجتماعی همزمان با تعیین حقوق سال جدید اجرا خواهد شد.
🔹
براساس مصوبۀ مجلس باید ۹۰ درصد همسان‌سازی حقوق‌ها محقق شود و سازمان تأمین…</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/farsna/440394" target="_blank">📅 16:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440393">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f71d087acf.mp4?token=GtQ4ufs5OPfgLmuDt0VXWm1UqumtF5SHSSrPM67Tinmpuj2AP6pcJc93vwdmvWx2hy4ueZdTdSCCwPFswZ8xqpWolZybT48Czf1YUelQzQsNhcdWJq6Tr0v4uUl4v9iguvxs_RSDiDgiiFeNqGJWyVOVzvgJDAXf8x5JT5lXRMPrMQl7YlLBUXGZD8yl4lp5mJz55fhuCo9Nej6mjarzNZNA8xUVlYlPwaxsTxdlob-pNmzm0txwd0it29-txeHuwbhDjfgU8oQ34og5bFCLCfvWZlaFl7A8ML0wnuECdCzmgvbdCSo_50byHVozCxF5H5aAq5X7dX9i0KxKg5GZeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f71d087acf.mp4?token=GtQ4ufs5OPfgLmuDt0VXWm1UqumtF5SHSSrPM67Tinmpuj2AP6pcJc93vwdmvWx2hy4ueZdTdSCCwPFswZ8xqpWolZybT48Czf1YUelQzQsNhcdWJq6Tr0v4uUl4v9iguvxs_RSDiDgiiFeNqGJWyVOVzvgJDAXf8x5JT5lXRMPrMQl7YlLBUXGZD8yl4lp5mJz55fhuCo9Nej6mjarzNZNA8xUVlYlPwaxsTxdlob-pNmzm0txwd0it29-txeHuwbhDjfgU8oQ34og5bFCLCfvWZlaFl7A8ML0wnuECdCzmgvbdCSo_50byHVozCxF5H5aAq5X7dX9i0KxKg5GZeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار بزرگ در ضاحیۀ بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است. @Farsna</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/440393" target="_blank">📅 15:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440392">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjkYJ1ef32kbD5siWqK7VHQLINNH7PgcYJMThkKYvFv6Gu5wkG6f0uCjWm8nm2GbEa3y_F1YhIyhoyD8716DLEdne7M0Gw_BF2EZzmolzr2wCGch7OHZ8X_L-GpSoJP9uk5Vx-IeYRrC8Vgc4BfE1QmI7xL7LyaFnYk_pS4vobRMxDktztrVZ8tDjF8lq605FSwM0rl6Vod8vZjPql6RALDp08-Z8-9xyMJd2aJU-JN2Vx19rEq8o9JFcSYV_Y5Pwj6hgdYZdXNB5dIqBUS6U4-bfd9ObNIScDshC890SQyxunFvQJsIFjYYdEjdBJUR9RokD14gD6QHu0K0jzyIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت‌نام مسکن اجاره‌ای زوج‌های جوان با تخفیف دولتی آغاز می‌شود
🔹
زوج‌های جوانی که کمتر از ۵ سال از ازدواجشان گذشته و در دهک‌های درآمدی ۱ تا ۶ قرار دارند، می‌توانند روزهای ۱۸ و ۱۹ خرداد برای دریافت مسکن استیجاری دولتی در سامانۀ
Saman.mrud.ir
ثبت‌نام کنند.
شرایط اصلی:
🔸
کمتر از ۵ سال از ازدواج رسمی گذشته باشد.
🔸
متقاضی و همسرش در ۵ سال اخیر مالک مسکن یا زمین مسکونی نباشند.
🔸
قرارداشتن در دهک‌های درآمدی ۱ تا ۶.
🔸
داشتن حداقل ۵ سال سابقۀ سکونت در شهر محل تقاضا.
🔸
برخورداری از فرم «ج» سبز.
میزان اجاره‌بهای پرداختی:
🔹
دهک‌های ۱ و ۲: ۳۵ درصد اجارۀ روز
🔹
دهک‌های ۳ و ۴: ۴۵ درصد اجارۀ روز
🔹
دهک‌های ۵ و ۶: ۵۵ درصد اجارۀ روز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/440392" target="_blank">📅 15:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440391">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ed369fc52.mp4?token=EHFOoD9atPhc_DUitde-rGGpBBBP8ZulC77OewUQ_Zr-VavAzelNGWC83JvKAWQbMRsQcseOItSRDa5yJNDc0kcCS7IRf-X2iP_sc4klBvD3_MeyiQ_y5mCKvH_jkfmveEz0zQh5hmmWDAwAh6dACpREDxzYdTMBB7lXdWdjyGlvPJgeJpYyocj72iQ1GOfl0MEJXM6rqZQgFTYJZRteStg5K-tuDcnuxHWxT4JuFhlVoCxWRatS3UXetabeT9KVRp5UQGo_t_rWIs6QwSnHgCikWob9YT5ei1sTcNVy2VD-pXIhY6loq_ZWNgAnyBGOh6naan2G2Xj7iRIzxbIZ9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ed369fc52.mp4?token=EHFOoD9atPhc_DUitde-rGGpBBBP8ZulC77OewUQ_Zr-VavAzelNGWC83JvKAWQbMRsQcseOItSRDa5yJNDc0kcCS7IRf-X2iP_sc4klBvD3_MeyiQ_y5mCKvH_jkfmveEz0zQh5hmmWDAwAh6dACpREDxzYdTMBB7lXdWdjyGlvPJgeJpYyocj72iQ1GOfl0MEJXM6rqZQgFTYJZRteStg5K-tuDcnuxHWxT4JuFhlVoCxWRatS3UXetabeT9KVRp5UQGo_t_rWIs6QwSnHgCikWob9YT5ei1sTcNVy2VD-pXIhY6loq_ZWNgAnyBGOh6naan2G2Xj7iRIzxbIZ9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار بزرگ در ضاحیۀ بیروت
🔹
اسرائیل اعلام کرد که ضاحیه در جنوب بیروت را هدف قرار داده است.
@Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/440391" target="_blank">📅 15:47 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440390">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfULo7wnhLsj11U3SF9HS-I7xLeTDB9zyWcXuslZbcqerAAktq20QbwLrm1IUkXpmK1_LVpwEphyN6VYc5BcsgbZZNqvEyktreXGdTXdb-aeUFL4QMjvrY1xS-FDZrHdcjrGll_YIf2q_M5E6__10H58LUruX8gGf55xaF8T2697Xg7TyrMmJLZT12d7PtsPFC_D94LMjRH3zc8e63IRdTJA8pLIK9uraTyI-Oq689z7yGhJ5_Hhxu3N0wu2-8hSgQPtQEVwZmRiERSB6wxoxZef2OOy1IKJBoEwLOuHSR7KjLYPBEm1ea1mWA109qorL7U3bQEKA19N3BCFSpWL7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمعیت یوزهای ایرانی کمی بیشتر شد
🔹
معاون سازمان حفاظت محیط زیست از افزایش تعداد یوزهای شناسایی‌شدۀ کشور از ۱۷ به ۲۷ فرد خبر داد.
🔹
با وجود این رشد، یوز آسیایی همچنان در شرایطی بسیار شکننده قرار دارد و تهدیدهایی مانند تصادفات جاده‌ای، تخریب زیستگاه‌ها، فعالیت‌های معدنی، چرای بی‌رویۀ دام و کاهش طعمه‌های طبیعی، بقای این گونه ارزشمند را با خطر مواجه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/farsna/440390" target="_blank">📅 15:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440389">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d28440e3c.mp4?token=gwP7ixXPVW-LcaWvXrj4PxjQ3hdWjiBuRCcAtOspbKSj8cKHSBgDjyfccFjUso9lw0lApClmMlSUGmQE_zBeUdsrQCxEfdhicggl4swdsk0V6M9zhB6OrovEppbNJ4j1MkHI3RYVy0mcunUY87x2GycZxt5zBeWSsSpgspvxmIJjXISgKgfyK6RfShDrYgrqzxSlwwkVDd3Tvu28cY9khG68UIOUU_-6a0cxrJVmV6av5ZnzncY1JzeKaopvfO6ttOXEmF7PLh2CokqT7yT2_DQgbIQZIBrG129J0JRgvMOD1cBsm2sYxEqTU54Q5ivTOmf_3S15lph8z-syjJdUCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d28440e3c.mp4?token=gwP7ixXPVW-LcaWvXrj4PxjQ3hdWjiBuRCcAtOspbKSj8cKHSBgDjyfccFjUso9lw0lApClmMlSUGmQE_zBeUdsrQCxEfdhicggl4swdsk0V6M9zhB6OrovEppbNJ4j1MkHI3RYVy0mcunUY87x2GycZxt5zBeWSsSpgspvxmIJjXISgKgfyK6RfShDrYgrqzxSlwwkVDd3Tvu28cY9khG68UIOUU_-6a0cxrJVmV6av5ZnzncY1JzeKaopvfO6ttOXEmF7PLh2CokqT7yT2_DQgbIQZIBrG129J0JRgvMOD1cBsm2sYxEqTU54Q5ivTOmf_3S15lph8z-syjJdUCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ارتباط مستقیم با شناور سرفرماندهی سپاه در تنگۀ هرمز
@Farsna</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/440389" target="_blank">📅 14:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440388">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTsqNC4__gZxF5aqn7_QPE9GlXBwCp61CRX00MvTxhAoxDlYB5IjayesFN3p8_RBUMBo8_oaDbEe4--g1wd_6AM3Q_y3Znkv09fBOAESBtNAW7IkMG09FGDW2EqR1y9q0VOMCrrIGU-enT3gJAzynhgS5ObFjg5rTJuf6xNp6EF-zKZP3R0eB-miDOgwZjuLqD3B86BtKxUQu1Upce_QvfB1Dg176_v5_iPEE_0ICcVO5O60zBZ8n8fLt6w6eG8Fyh1PRlQcTgO-7kxRtaHK6i_gRp1bzAoqcnPqx91eyTOvLVT6xOLyXSecpkvaq0luWHpXZAE2_sJQnGwrT7upvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شمال تهران ۵ روز بارانی می‌شود
🔹
براساس اعلام هواشناسی تهران، در ۵ روز آینده در مناطق شمالی استان به‌ویژه دامنه‌ها و ارتفاعات، رشد ابر، رگبار باران و رعدوبرق پیش‌بینی می‌شود.
🔹
از امروز تا دوشنبه نیز وزش باد شدید و گردوخاک در نیمهٔ جنوبی و غربی استان دور از انتظار نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440388" target="_blank">📅 14:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440384">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BCeH9iLaaxGeI6GSkEc6Yc5SUbJKzI7W71b1JFq2jjGagbDmdPS5GDFDGHRGChI2XfzYrdHSUp-gNCaW7tF0_GehL5QqL3A0h0IdimBTz6z3iHWlbVpIbJCzgHkn7awfyPvrkwCqbR_zY2FjH2OGChkZ3Vu4_Dv_pnAfXveqpd8rdiiEiruHsP1DB9tiYxvYwhYr50OJgfeoKNCRSQ6HNfxVubtf9nxRviByw9k9ipJSTE6hWLoWd1wsxlcO4pcKT3dqFAsYp5Ic-qh7sxv9Mr_BhEUYTwBL2QhAj7pwlXrbsY_bj6eHgFqPZLbJMms1j-L1gyoXLCqw-nav3RgGUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fh7CGfVIOEYIf85mIxXJz_FxHgEDr2vSGMcha0ADHxx2TColO2vCFgHdQCv_gypWNEbJHH5Oe-30sLq_dE7Xbm8GgbDnhznY46Wl1NkH7kiTZhyzC6CMOtpWwouT4pKvguqoGx3hjpqnuiEfhA4ChXzyVjzZgxypRyPJrYR3ti9H4glNTMk-CWLLLlTx1EtrKE0YypCgnzozwUX6D32AuS54uj74xyVZ28VkzwCWAPe8FYT_7-ZjrMTdZz67iJaY6fTDNnf-idmBz6a4pQrAOGCmehRJ4-BlnSP7IpeuUcy9HsceBONi2mEg0SyfG91uZvUAw_ZOrDj2GDsL6AYtHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_5cf3HWzTs8f6HEGFOUxO_nL2zf8Q9OTL_2STHUM8AQsYagYZaAV7PUz7ZlL1rB2MGEgbs9rkbfQ254ECceE2paMAlHWHGvVsD4UapgjNYf5KK8Q6Y3QpMsEIvniL4vBBYGYWXSI-FiNAGt_WV-EN4qcCYaeyZs4OKqgMVafTLAY4OOQK8CvaVEn-J-fTVjbkQFx9TB_kXtBlqSw3k2iWQVieme3gq5xs4kfo_5VXQcn2pwJy2bsQp0UAaB5XPIlqGIhNKURREbKhy3zJ4lVdUYcpvgr7uRLKQ2R-1EFAVYSWuB-Wgkab1oiXtjdsJCzq6gF-pyUmUzkfNezRz4JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EE4iS0HWI8rxASDkdn8CarLf1aA3Hrt_aOQuKMvgnukMmGjXxLueVuzqjUS92ud_BcYucjVmBy35HiX9rXmHtFTh01hksHgD_SRR0AEL56KVSIVE_m4fuqUj_k4BUBQvD7qbTbBuKAS9AorPwAhPrIQjJwCtwC1SpSUwz5MVtkONTXFXowa4CIwl6cxrqxUFH52zXx7Id2U4bdh6NZHZiUcH56FRtx9V7cRvpM6bdkUyaVd-6XhpMAJgG6betKYs2qYyMyLGpd9oC6CcA-dVt3Sc2QV0Bl5m7WfpQsER4TOcn3oYKIGxaqc02lrNp7PsWMPcJ2ZMbY6EALkAwrgZDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار وزیر کشور پاکستان با عراقچی  عکس: زینب حمزه‌لویی @Farsna</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/farsna/440384" target="_blank">📅 14:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440379">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWgjzNyh-rCK5TUSUnn3PXTWeAt7pU7J2SlaTUv3EUa8kpJVwKiQPN_-yLRaDec2feFSksDNxYFckqtdO3BkrjeXSjtQwh1yr7bqyVji_EVtEOEWGOyjT6PAJPoms1TERsZsmj_e8CVOds5LsVM3E3iDwiGzpvoZ7jL8zRgEOYpjFZO_-viBMKOf51PSfU49ytgvPMWUZL_TinKEsZ3116OQKLVz5thqSQm5YcAU04TN3it8uwvhs92l-f_s9KriAwohGMFPMJZ22bF1aJlQFloH9TbP4ZmhuEJ-umIaTxP9u6LHA8f44Xa2skLpI2HxHkIi1oJDRUIKnRak5MDmGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد تعیین یک روز بدون خودرو در هفته توسط رئیس‌جمهور
🔹
پزشکیان: این طرح می‌تواند در گام نخست برای کارکنان دستگاه‌های اجرایی و ادارات دولتی اجرا شود تا ضمن کاهش مصرف سوخت، به بهبود شرایط زیست‌محیطی و مدیریت مصرف انرژی کاهش هزینه‌های غیرضرور نیز کمک کند.…</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/440379" target="_blank">📅 14:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440378">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoTXZvHcpxuhLJzYDzQT6KZKs0IkzZi002WDfgENemganFEXEge36rJncTaiWZUY7HW4ZrBTZa9ruYawPL5CjhKy9kcOowOLvcbpJx4OkwErH6jxpB1Pg7CWzZvcUNQkVV-BvR4HDntmRam-u0o55iUXIUdqaGfH_Hxfo4diXzG2G1YKloIM8-4i1_jvpTJrACG93D-Xzx4OsuXzJwcIFc4KAyrf29sCLSjk-q0Nl0oUejdAZiuDkLGPCliM2dwI-CtOlskmhA4GVpQzh7hVYqzuv5mgF0C-ELByaD33r6YwajaGhnI2Vg2VHWgIL89W5TtEov9l5QA54tkokgEHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: صداوسیما نباید عملکرد دولت را سیاه‌نمایی کند
🔹
در شرایطی که اقتصاد کشور تحت تأثیر مستقیم جنگ تحمیلی آمریکا و رژیم صهیونیستی علیه ایران، محدودیت‌های ناشی از تحریم‌های اقتصادی، فشارهای تجاری از جمله محاصرۀ دریایی است نمی‌توان تمامی تحولات قیمتی را صرفاً…</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/440378" target="_blank">📅 14:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440377">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nb-JlzQnecXiPGsvj5GJQcbR4bmM8gqXK7VVmA_LE5DHPHl_UuUaAVQCD9xkDX_5XZcVW_cghZJhq-L8OnIsoUnkhf999wabzYXgw2oTr6n9hF5MtIUvcJxqO4Hvq-7cFAioWsUg6RUb6B0Nf1vbEhqItRP6ulXmkui97PW0wkV3sakGNz3lsLYHXe-AORkEIsvJWqQchGhwnL5BNqFh2QeTlpcxYp5eOaBnFQNdG6TwU0Ey84ysX9COwN9gKM98XrOMF2dAeRRVyB8DCXP6v9BlWiRoDEUy6FZJyXdMhX6ru4tqPDyZFcq-BIFzcQL7ULv6f8jb4GYw-PhKF0_r4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: حداقل ۶ دهک پایین درآمدی باید از افزایش اعتبار کالابرگ بهره‌مند شوند
🔹
اولویت راهبردی دولت در حمایت از معیشت خانوارهاست و موظفیم با تمام ظرفیت‌ها برای تقویت قدرت خرید مردم و کاهش فشارهای اقتصادی بر اقشار مختلف جامعه اقدام کنیم.
🔹
تأکیدات مکرر بنده…</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/440377" target="_blank">📅 14:32 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440376">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70f2691aae.mp4?token=v4LwgjKqvxWPsG1tqxziJDEGvQ5xYA7viJQBp4YVoEC6eS9lnLtHf2fTVipLVjaTwB_dpN0f9Mx4m9WdwmB3XEwrGRobA1oi2tv4Td0P0-olhhGDYG_6eOE2RCEx4ekKzrvhGXTNcwapJV0T_D84Y3FHs6jg63VQFA2PmJ_UYCjx-JMwBGggisWvEKpQH2EfjwyDYVqvNunmY_F92kJ1Tbggzok8yHMXEWPzfMPIpH5awcPauHlwzR2acneZxKh9v4uL80cXbfu-vkU1zFOZkOQFdhhMKzRBcHXO3Mopat-B_5EO5UJBj1pT2nPiok9Djn3FSW_maqsKJMdBxaVBhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70f2691aae.mp4?token=v4LwgjKqvxWPsG1tqxziJDEGvQ5xYA7viJQBp4YVoEC6eS9lnLtHf2fTVipLVjaTwB_dpN0f9Mx4m9WdwmB3XEwrGRobA1oi2tv4Td0P0-olhhGDYG_6eOE2RCEx4ekKzrvhGXTNcwapJV0T_D84Y3FHs6jg63VQFA2PmJ_UYCjx-JMwBGggisWvEKpQH2EfjwyDYVqvNunmY_F92kJ1Tbggzok8yHMXEWPzfMPIpH5awcPauHlwzR2acneZxKh9v4uL80cXbfu-vkU1zFOZkOQFdhhMKzRBcHXO3Mopat-B_5EO5UJBj1pT2nPiok9Djn3FSW_maqsKJMdBxaVBhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رحمان پنجه طلا
🔹
عموزاد در فینال کشتی آزاد رنکینگ اتحادیه جهانی درحالی که ۸ امتیاز از ممدوف بلغاری عقب بود، ۱۷ بر ۱۰ به پیروزی رسید و صاحب مدال طلا شد.  @Farsna</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/440376" target="_blank">📅 14:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440375">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vYmJymqPZ1PDbFBXRNUD2PsPAocwLbJrx5OEnJ-QW2XLSiMmFDrD17IXk7f1AssarpbM8subAxKP_wlxIy6v6wal2W9k5w1qDpgeB1gu-Eb8tiC1kV1A0WHL_MAk0OJD7t13kx1bdBRGypFSuJna4ZqobXTF-UZ7HZRbA_3cAUeZzJf_qn26y6P2q_lxZKzauiaFpnmp4dMIgdZB__MevBHL6H-OPK0RgkzyhpzjHUDJWAnEUimbpOC9ZQ4NW632NINDbZmCCcQKgmN4wt70fvNps4bDI8-GxbDIiH5L2fxaAN9ECU7i4UCzY_XZfHG3zz1i7m9EeNmIggwHEmGHRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
افزایش مبلغ کالابرگ شاید زمانی دیگر...  @Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/440375" target="_blank">📅 14:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440374">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMgMjd7dE0DK1FV--3D_nB2leztW0XZgpLas6RJaKRy0IDQpBAgI-YFz7zbkZicAWzl9KlN_T9_Gu9GwDN_EynUSlzoDtYMx5wdWSJzhSdKF7Hfxe3y8td2JXWc8uuVWCKjNfk1jzE7KcX95_wfyFxS2KQwZJE8dnZPvwQ-uoRmKt6_F4YsaAdFokUs4Ne9KmLKTTc6-m83CbiW4zGAakzz37hoI1ohhvdFBX8ZBz4gJfMUuXlVdg-eHScRgyiEANwxH1vSmIlz4vDrALG8d5HgXax8GskFoCm3hxTuwrnNd4n01RdtYgBKCZZIpSuGdkI9142YkttCMupA4zPd4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بقائی: وضعیت آتش‌بس بسیار شکننده است
🔹
سخنگوی هیئت مذاکره‌کننده و وزارت خارجهٔ ایران در مصاحبه با سی‌ان‌ان: ما چندین اختلاف در مذاکرات داریم که موضوع اصلی آن پذیرفتن حقوق ایران از جمله حق غنی‌سازی توسط آمریکاست.
🔹
آمریکایی‌ها از زمان اجرای آتش‌بس چند بار کشتی‌های تجاری ایران را در تنگهٔ هرمز و آب‌های آزاد هدف قرار داده‌اند.
🔹
شرایط منطقه و آتش‌بس بسیار شکننده و خطرناک است و این وضعیت نتیجهٔ رویکرد بی‌ملاحظهٔ آمریکا در قبال منطقه و آتش‌بس است. نیروهای مسلح ایران در صورت هرگونه حمله، با تمام توان به آن پاسخ خواهند داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/440374" target="_blank">📅 14:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440373">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e31621ed9.mp4?token=W1cZRuH3BTn7F6zi0ZCsuRJaeYslRe-TvCpDOnoEahowYaZnYzFPS-9_etqiLQitXX5S8JsxNYkrVgGpVPefESlrMAW9enj0UfwnErzquqhZ9jQA23BuRZi0kTpzXwwaX521Or7cmbdKap6isxF__izLAsaxzqBehpl9CcnJnTpB9RLOlv8mXX9uQkEIBb7dKxApnlpJ7XsSPQjzbY2iEPq2WU8ng0D3DoKqsXNgID2ETz3lXi-l6fSEqTiQCCsj2x-rAu4zv74FroXbxELuklHWK6cVttHOVCmxTVCqoLCV7IfokxWqvocV76xvVEz4wWNGOKOzFwzwydJ7mbaSoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e31621ed9.mp4?token=W1cZRuH3BTn7F6zi0ZCsuRJaeYslRe-TvCpDOnoEahowYaZnYzFPS-9_etqiLQitXX5S8JsxNYkrVgGpVPefESlrMAW9enj0UfwnErzquqhZ9jQA23BuRZi0kTpzXwwaX521Or7cmbdKap6isxF__izLAsaxzqBehpl9CcnJnTpB9RLOlv8mXX9uQkEIBb7dKxApnlpJ7XsSPQjzbY2iEPq2WU8ng0D3DoKqsXNgID2ETz3lXi-l6fSEqTiQCCsj2x-rAu4zv74FroXbxELuklHWK6cVttHOVCmxTVCqoLCV7IfokxWqvocV76xvVEz4wWNGOKOzFwzwydJ7mbaSoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رحمان پنجه طلا
🔹
عموزاد در فینال کشتی آزاد رنکینگ اتحادیه جهانی درحالی که ۸ امتیاز از ممدوف بلغاری عقب بود، ۱۷ بر ۱۰ به پیروزی رسید و صاحب مدال طلا شد.  @Farsna</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/440373" target="_blank">📅 14:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440372">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1133bb2ef9.mp4?token=Rrw9RNE0gVNeR2ceKG52RNLPstrg9lbhdVJ7q0GK1ESBrKNl_Qf57X9kDYJJ19wCgNUetRUKyUL3_i0kTXNKwfKXtEYUEbW3LzMODG0f1fltEHfrM9sVsBEuug0Ta3TdgC2Wj7hg885h2V1M1zATzZlBSlCLHAFevDhN3ztfadG929KlIPzIim--3BCN9vHK9ByPrDNBdxRMJF7GNa7bA27V_G_HTlFTduN8TCB0I1YYLry_JF01aRDF0lQsNyGPW5KtXEm6Y-6JsXWX_5IuQCwvqBJJGLgBYFJ2wehxGIGXtzACnOHrFvqa0U59GDtPjrYadccF1L3LgmpaRJIFK26elhxHSPNUy8uMynCTk37oWDclcuGY3H3T_YCG1GoRH6Pj7CxTRK1QLG7BD9NFmWuag7vEkxo11cP2LtaG1HNvaqVSzZoYI2cbqh4pd2tPUDmIKXshmkKuJ4yPmdd6-25dXNfeaylomPV3nD5YhewY9ZocoeZTiuxHiU7uOsQPtwZidqJ6JNiDw-ImzWlrj7jhTH6o56jmD1KA2rs1kokqUgKynMs9v2nUDeui9VfIrTm2dDdwIAxxF8Q4zbOqmDfW_OtPTYjFKvH92YIITOBmklWgJGSKwyXiUnLVSLc1PxslPH915vRpDmFa3Phak7M2rycZ0UWeoxvAVvRMqEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1133bb2ef9.mp4?token=Rrw9RNE0gVNeR2ceKG52RNLPstrg9lbhdVJ7q0GK1ESBrKNl_Qf57X9kDYJJ19wCgNUetRUKyUL3_i0kTXNKwfKXtEYUEbW3LzMODG0f1fltEHfrM9sVsBEuug0Ta3TdgC2Wj7hg885h2V1M1zATzZlBSlCLHAFevDhN3ztfadG929KlIPzIim--3BCN9vHK9ByPrDNBdxRMJF7GNa7bA27V_G_HTlFTduN8TCB0I1YYLry_JF01aRDF0lQsNyGPW5KtXEm6Y-6JsXWX_5IuQCwvqBJJGLgBYFJ2wehxGIGXtzACnOHrFvqa0U59GDtPjrYadccF1L3LgmpaRJIFK26elhxHSPNUy8uMynCTk37oWDclcuGY3H3T_YCG1GoRH6Pj7CxTRK1QLG7BD9NFmWuag7vEkxo11cP2LtaG1HNvaqVSzZoYI2cbqh4pd2tPUDmIKXshmkKuJ4yPmdd6-25dXNfeaylomPV3nD5YhewY9ZocoeZTiuxHiU7uOsQPtwZidqJ6JNiDw-ImzWlrj7jhTH6o56jmD1KA2rs1kokqUgKynMs9v2nUDeui9VfIrTm2dDdwIAxxF8Q4zbOqmDfW_OtPTYjFKvH92YIITOBmklWgJGSKwyXiUnLVSLc1PxslPH915vRpDmFa3Phak7M2rycZ0UWeoxvAVvRMqEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رحمان پنجه طلا
🔹
عموزاد در فینال کشتی آزاد رنکینگ اتحادیه جهانی درحالی که ۸ امتیاز از ممدوف بلغاری عقب بود، ۱۷ بر ۱۰ به پیروزی رسید و صاحب مدال طلا شد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440372" target="_blank">📅 14:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440371">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EfCGX6SxvGqweSea7H9ji1apfbp8m7rHP3jem6SLJbZolpNvk9Vzk16JQrzu3pFkZudPS9uYvLsA5EtIny5rBK9CASoxvEka35OuQSdUPRgpI35vSe-KXX0AAvFKFNJL0UHFakWhEmb8bT8j2pCB_Ju78Vm-zwAQ_a_Web_S-9qmSh1HkKnL6AA1gdOhavovuQPjwfb7C9NBFFhZxJnD71IM-6NqDh2q6_hPvsXzEZccfdYndNq7VIaH299ldYnps9zGBs56XjHN8Gk_8IPGL94fpLC6GRi3TGVaeYHkR1jOLoOlW-VbU1LXYgaQ_Rs9MhZwgVcycuZNok-iRyKGmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲ زمین‌لرزهٔ خفیف شرق تهران را لرزاند
🔹
۲ زمین‌لرزه به بزرگی ۲.۶ ریشتر در عمق ۹ کیلومتری و ۲.۹ ریشتر در عمق ۷ کیلومتری زمین با فاصلهٔ زمانی ۲ دقیقه، پردیس تهران را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/440371" target="_blank">📅 14:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440370">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bHUSnvGsUMl5zam7NNMkgD5-pmVoDg_c5kQ2F4ZEVrxYW7etrdAl8_4aA2uw6sq8BREQ23PuoPD8t4GyG9JMGQ447jssWxV8lJPYhCOo3myuKf2OQCHmcgAcO1aKRH_BF4wki9QVcQkpiUVC2UiHzGlO_Pd_W0IXtOuuOWJuqVPVnn_rSqt2X1AiRfWY9367qUmLKf5NK9L95Mjun22TyNoOxRIIJRiQWgisH3k4sknOcwFse8gGbTAxW1XdcriwMRQ79tEN1KwC70GtosSj2Q0hn0r3qC8KHVH6el1FDNLoVZ0GG853NOZexCrwOMZPyCZrm5v7yCoiQZpzQAHurQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نجات
مدیر شبکهٔ ۳ سیما از سانحهٔ رانندگی
🔹
درپی وقوع یک سانحهٔ رانندگی در آزادراه اصفهان-نطنز، علی فروغی، مدیر شبکهٔ ۳ سیما، دچار مصدومیت شد.
🔹
به‌گفتهٔ رئیس هلال‌احمر نطنز، او پس از انتقال به بیمارستان خاتم‌الانبیا(ص) نطنز تحت درمان قرار گرفت و پس از دریافت خدمات پزشکی از بیمارستان مرخص شد.
🔹
براساس گزارش‌ها، فروغی پس از این حادثه راهی تهران شده و وضعیت عمومی او مساعد است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/440370" target="_blank">📅 14:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440363">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YaOGNZlNkyDOvkVq1El_dgcyCtZOthVQUk5mgKgeZpeGur5Sqbb5niuy7K7EEfztqx7DPGZzATSh-lzdT7EOV8li56W63RRoZSsH99pWzsNlJRA4SKgjL8XFf4UIy1dvpD1u63dUd21MQBQYBA-7Mjc4PvXe3CwamnStUZnR-amHd5RUE9jMtbQt5iPOJHfUuce24AI_rWL5Dr5p9CDSUc7c-Xkrvi93Nzmulff0Tp5Exhis8-OKGna_ymLKZfa3p1YWOw4z7JWGhXKjWaGwYWYlqSwhiYjeycoe0fPkd7Od4YagfoM8ReLBHVxr_I1I3i5PKdicexPVUK5pPdbOSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jP2mFQN1QM6sKzAHAd7s1F7YpZOxlw-nnfnB79HVw_Q-6dIVX8DGZkzSWxg6fW0BOk1ttX6tF_H66VhfVDFXHj5F2gRoH5YVQyBO1B4f0X6Juv_XmwcBL90k36SVSn4NThmJIETV2hgkH7spYG4MT3l6VBFtziHFrvcTNecyJ6K4fAdf0kySX3fxZl259SY1h4JfdmEY-NEK2eO-SRZ9OqxL_lS0uaG_-Go06EzPeDtBOxnHy8R0OHFOMsZzrlcqh0oIMOSPjfhk2epZEbY5Qlq7jQGDern1qd0BJPGDyKvhPboNHNUulqok7jreAOW8_qLoQzqBuN522GZe50750A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cOeC8XdGkOQbdU6xYjEWMuJz8JvJXdZys-7y0UtlNuJfsrQ0UkUO_tt9p__I4XQAQ9iADLdo19gGGYZVunAabSju27mie5yrChZiDIJtZcyrB8POzhCREgCYsv1wNy6mNuDB5epaC33m2TS7qiiIz4-7uMZmHRq3YJDU3Q2foY7frUyJ96TNPEiB9xqi72XctOIOO8RbqIODPCasqtLVBXySuBuBwLwqwzpAgREcVIR8C9vY__IVmQtbCIvzWSqB9sr8W2DTrC9MDcyFqpm9xTJlvXgBaWyPD3tQpAU9uq-filTdBizEo5T_pLkrgMIHziSqgQGGxlK6L-Rdwc8Kpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kdoB6MzO4YRhtq3L8JVx-C5ymanZqZD64D8Mvo2qMOaDzcKcTTC-YNpZaJ7SNFETETIlIrI_Rm06ZxZLHXbe-N4dGZaImV68nj3iSTLnBO-bH-Zww5USWvCJUs6dfUdqB4p986HUQNpB1i5TqEXu4MjCRG-whxqZo2bp18YFBgwvb9m6PE7yjt5JUe9B9dDugKQQD0DP9kH0o5Wn5xQ0QYtObpH3KCN6TU-ifMlIvyt9QogMoTik0-hcPOIW1Mxuyd_va9V0nrP9e3hV7leRTIV0yIeuTxCkWxgK5CPySj2HMwAeaXcmnBKUtI89NVtjpKGI-2bIN0NS0HhCNkcuIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YFIcwE0nubizzrflQi0E5z2h9TVCnOlD7tArvU7NQD5MOuA0zVuolPARVpHcPWqIUgIcFQRiUfU1yjUE7YotP4YT9lRQMxUlAwRQOY5xLsXo8GrLX-e7X11KxKAv1Y_Q80EiSQDJIASkMQKdCFEIrsSQa-ZqIf_cR3AGjdPLkylhINePR-QQC1XqovlqmcqiUE5zl5PSzo2E-oWliCo5_2zsRyeIO2wEIqY3TJsx9DrdieqMk0Jnzgjk7NMZzMO-C97FXX4ZESYQypJ81d0yZLJj61jlKMRDCyXWyL4YcxQ7LEwd5GZGpngGjWnZc_gdYrL4p_Rq0BqZswb0Lp5swQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuNfDA2FlJgXdOW0MB9QlnNTf83c_vXKvUjkmQ_Yj_nGLc75l0vwlM30oJVqBCEXPyejqqnAjEYVs-SeGnqMvqScQIYb0ZR500fyqc38coQLjEwEjUFB8iAIVhW13KI1QC7vvAsCXPMPM49mWuhvkd0jV6pKprtPR6sbeLKqlebjn-5Yv08xg1GlvuAYANIJE8wnnOngj5XwnLtZhxf6q7ryRz50RKgv5mxW99J47Ml3O3R2KtNPW7WmXZ-YoFHArkAX3raWbAUkV9jEiM8inPYnu1QiASW-c24gQ5n4J_iiyUUtwFmikZqsAs3vXS36UeLofH5gKqFBBsfzt1Z5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IeMCmYkn9_wZ7rMmWf_e1PdXAIFL1dxxGYI0PViD1W2VzFlt8_QpDPZeFUL-ctifkuMSOP5tXLndhBBw__nJtSbDoKgrXP0CnwrCxy4pmXcYq4A5-L2-q1RoY1szNTsD7qQq7YhXUJnd6HPsLYseLPpqPEorRGCWr5xngkekeisWIqP7--XCPSATNYbfJ52jNtz0AkJwfmHdkugQbOIC7P75EMj38o_GYlsBnuqYs6WnqxsvErl0zIpy4afuun4XGoGIOqKLFPjQPiNQbSdUTSWZsyjLjCBTygMn3kSJCc9cdMPttp5-XqvLfumYDcYn04tNmzpDpufT0HcE8v9fdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان پیام ویژهٔ دولت این کشور به رهبر انقلاب را به عراقچی تحویل داد.  عکس: زینب حمزه‌لویی @Farsna - Link</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/farsna/440363" target="_blank">📅 13:55 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440362">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">وزارت نفت مخالف افزایش قیمت بنزین
🔹
سلیمی، عضو هیئت‌رئیسۀ مجلس: در نشست وبیناری وزارت نفت صراحتاً اعلام کرده که برخلاف شایعات، قصد افزایش قیمت بنزین را ندارد و بستۀ جامعی برای توزیع انرژی با چند سناریو تدوین شده که دولت در حال جمع‌بندی نهایی آن است.
🔹
مقرر شد ظرف ۱۰ روز، تکلیف تأمین سوخت بخش کشاورزی مشخص شود و همچنین برنامه‌های زمستان آینده به مجلس گزارش شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/440362" target="_blank">📅 13:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440361">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoZYQ8vJipS5-zoNDtfZ7z2eaInV8VycFGMXcpoGuat5b8iArs7W9tqKWEKVnUZ0dyamb_DGKKrITgsNM2aOvXkt2dp4wrcPRZUmyKW3vF8m144kiKkX43BN0ermJrkb041jxbPrF6pj_1CHcJ4FuMpR6NgwlS_1MRHJZMrpXTNU5b2d8BbEqwgAUI2FgF6cb2lktNFfXTz9ciJKdhzMgmfMlZO00l4KOQrqVyhqEKqKGLv7gINSUtFWi4p5LT_wm0P5sUerjH9b3HZlFUiUzgZOSCOXZTQkw-Br_LR5aYTGBBfRab49VtBWqzeprqPobkv6NOgqSz58CDgsVE1rIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریافت بهای خدمات از تنگهٔ هرمز وارد فاز اجرایی شد
🔹
زنگنه، عضو کمیسیون برنامه‌ و بودجهٔ مجلس، در گفت‌وگو با فارس اعلام کرد که درحال‌حاضر از هر کشتی عبوری از تنگهٔ هرمز به‌طور میانگین بین ۱.۵ تا ۲ میلیون دلار دریافت می‌شود.
🔹
پیش از این نیکزاد، نایب‌رئیس مجلس، اردیبهشت‌ماه در سفر اعضای کمیسیون عمران به بندرعباس و بازدید از تنگهٔ هرمز، از تدوین طرح مدیریت تنگه در ۱۲ بند خبر داده بود.
🔹
برای اجرای این طرح، مجموعه‌ای با همکاری وزارت اقتصاد و تحت نظارت شورای عالی امنیت ملی تشکیل شده است.
🔹
مبالغ دریافتی نیز مطابق قانون بودجه به خزانه واریز و در محل‌های تعیین‌شده هزینه می‌شود.
🔹
بخشی از این پرداخت‌ها نقدی نیست و در قالب تتر، کالا یا تهاتر انجام می‌شود؛ به‌طوری که برخی کشتی‌ها به‌جای پرداخت پول، کالا یا خدمات ارائه می‌کنند و ارزش آن از مبلغ قابل پرداخت کسر می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/440361" target="_blank">📅 13:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440360">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcsUrwH0Lv946x_YVbOusFtsjBtIS-vX0i_NjA8sBzjyI_cTtAPMmv1SSXCYfbIcT4zJFAhg9tI_QtFClkaMSMe0CUoYKE00gvmRNhxlnzVbjN7YH3h5QQEh3czt638AtkrxjF_9MrnnAO7p3YLofnxsw-H3Plmyw1EEfPIugc2XSmgOr5enarxXxTtq9OyVMw70-pvwJdVmwb7b5vOjwMb7-kEgcYfG5OWbG-QJjlMD7QMHp3dqxU8YC6N5tuw3o19FuAtyRjDDB_kqfLvz4FcKMyiRBNrf4PNkWV_g7AqlcK05KYXEKjt94rr6B6ptQBgaRFcQ6FwINUbcMd8voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اعلام جزئیات طرح «شهرآسا» بانک شهر؛ از تسهیلات ۱۰۰ میلیارد ریالی تا جوایز نقدی یک میلیارد ریالی
🔵
مدیر امور توسعه بازار بانک شهر از اجرای طرح «شهرآسا» ویژه پذیرندگان و دارندگان درگاه پرداخت خبر داد.
🟡
به گزارش روابط عمومی بانک شهر، رضا قنبرزاده با اشاره به حمایت‌های بانک شهر از کسب‌وکارها و فعالان اقتصادی، به جزئیات طرح «شهرآسا» ویژه دارندگان پایانه‌های فروشگاهی و درگاه‌های پرداخت اینترنتی متصل به حساب بانک شهر پرداخت و بر مزایای گسترده‌ این طرح از جمله تسهیلات بانکی، تجهیزات جانبی و جوایز نقدی تأکید کرد.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/440360" target="_blank">📅 13:25 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440357">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">هلاکت ۴ تروریست در سراوان
🔹
به‌ گفتهٔ یک منبع آگاه، درپی درگیری نیروهای امنیتی با یک گروه تروریستی مسلح در سراوان، ۴ تروریست به هلاکت رسیده و مقداری سلاح و مهمات از آن‌ها کشف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/440357" target="_blank">📅 13:16 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440356">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUArHJ2V3gX02LOr9jEHEAQELVeUL8F62Pz8aV6-uWPNqstCjxkok3lLV9gZmSJYWwlrld5qpD7RLBgFFuGBtlAIaBtGk7vjfa2lcQ5C6ubVMb0HEbxP2IsMC4HSgQU0YxAClbmM-2ZdkMxKxma2JRknv6JlztsjCF2IqxWbES7lH8w-pWfj0RCEKFbLrwRmZpsgS5L4bc3h31XJLruqLZZVZg82JdHq4wQPFrLjeCIfjVLcTy8fr9nEZYkrgQGogjKLlvQtummCAkdDHhfDjoqP9zA038yAF38T5NgMeihpTj0Zuxz77YICbn1MFJyuwlJCSTyrfOF43sasjOaNvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جهش ۳ رقمی بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۰۲ هزار واحدی به ۴ میلیون و ۴۹۴ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440356" target="_blank">📅 12:34 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440355">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5018b84b14.mp4?token=n1QCNiJ_yMZs1CkRyvr0bRX-YCWCWiNRN1C3IixL9ZYB-uxpbwLj7OQVMrIU8lFWMy1NTQMOQZqY1ClzOPO22dz4PN-k6bTeWmMdLvWN2LK4pCN1VU4eSXINLm6ce9wEitaSdQopK7SV57BiCB_wAIe8c1B8eS6B0ZmtzOQdd94pUuMiqX-mvupkepYf1WvJGWT2E2qCtUIq5itYPKOo5Q7FW74ub6q01mr-pizA9iUPCPIJ4C8mcOdJ874TtOOI7tQ2ikoM6reyrEyQEyfilipcXLjEMNMEOcXs-yfcHLsQL_pVBg0ySkVXrnOXL8GZNhxB5zKi5pr_iyH2EbgXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5018b84b14.mp4?token=n1QCNiJ_yMZs1CkRyvr0bRX-YCWCWiNRN1C3IixL9ZYB-uxpbwLj7OQVMrIU8lFWMy1NTQMOQZqY1ClzOPO22dz4PN-k6bTeWmMdLvWN2LK4pCN1VU4eSXINLm6ce9wEitaSdQopK7SV57BiCB_wAIe8c1B8eS6B0ZmtzOQdd94pUuMiqX-mvupkepYf1WvJGWT2E2qCtUIq5itYPKOo5Q7FW74ub6q01mr-pizA9iUPCPIJ4C8mcOdJ874TtOOI7tQ2ikoM6reyrEyQEyfilipcXLjEMNMEOcXs-yfcHLsQL_pVBg0ySkVXrnOXL8GZNhxB5zKi5pr_iyH2EbgXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در عملیات استشهادی در مرکز فلسطین اشغالی دست‌کم ۷ صهیونیست مجروح شدند.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/440355" target="_blank">📅 12:33 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440354">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وام جدید دولت برای کشیدن افسار تورم
🔹
براساس مصوبهٔ شورای قیمت‌گذاری محصولات کشاورزی، شرکت پشتیبانی امور دام کشور مجاز شد ۴ هزار میلیارد تومان تسهیلات برای اجرای سیاست‌های تنظیم بازار، تولید قراردادی و خرید تضمینی جو و ذرت دریافت کند.
🔹
این اعتبار از سوی بانک مرکزی و از طریق بانک‌های عامل تأمین می‌شود و هدف آن حمایت از بازار محصولات اساسی و کنترل نوسانات قیمتی عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/farsna/440354" target="_blank">📅 12:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440353">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkuy760JUXXYRrHcj_haO-0HT964TKy3C2dJj2BccH3CuuKhpvH3g1AmEMcE54i-Fj-s1Fk_eftrTTLU9GocO8bq-RNzVrFGKWzFFcYYRy0Y-_oMkzGErckqFTH-xGRzcLlh1jaZkBFD0AWcubyYr_u-fpuYSWEL-EJsvyROTAT8j3nvFE-0ICbDlanDGe1SZRcShe-MIpPD5NyhFFyq37inwdP7IPLmEXaywyQ-QF_vYkmfo5BMRyEP9nXs61rhNX3Zbd3PvtV9ahNpDed4f7tO9YLYDThIXs6l8B0iPlK_tqG8BqLYiRmhqJHLpPxADWJMrRBAFl62jp8fGGVJTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
وزیر کشور پاکستان در تهران با عراقچی دیدار کرد  @Farsna</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/farsna/440353" target="_blank">📅 12:03 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440349">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnES0j3Da9-FylIG9NvASnvWoKUzLtdNugc3xtRgdfKFSkwV5JVBXGb6zHHJuLxtYUK0aFn7XOx_tldrURPgku5JwATYHPurnZk5pvBCoV1Ghe84XlIMCIuM1c7jZ6hBEog1dx6BZ3ZWcYlcGzsxCcABGqgalDXoeP0sx8g0XC1u7AbYqACXQEe3VOLr9A412ri3sCG5bChDXmQ1y6TiW2Nl3_jZr78zsGb0n1EOr4MFe5qtE2-g36gCm6CKFk_0aSciGy25ejs035FRxZxKfM8RWBtUjkUYzR_Ewi0EwqY3k6Hl15X0c3_H2-YUVpbVFnO7DHXHWQZmWwQjD9n2fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bm8pgsWbhoFt3IQK5d1ALLqOacvrISDc1z432LjdABuTZiZPStlibV_IUaqb47sB9ugjTVraCkz-1rVmM1QM_v-j6nv_WlQzbi9MDclPlJwO9FcMvimaji5F_8rOFK7DPslzY5pOntNERLWI74fXVx_s2E9wX5U8a9Mxi7QFCJkkGBx0xgYG7gfZsLfkUKxIwRGMzAo41QLaQSvO4bjJsrZK9HksdnuXKLqTtIXwRtSvqdLEvnZmwHkLitJ91vZYFKaeUZKu94QqBtdeboy_CK9yPdRjbLGS2FKKEFZ7QcjDaUql9DcQRYTGc1NJd3hgfuDNL-qeOn02oNv_MScOMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUFeAMHe8Tegj1O5mqP2FJyi_kILcWOg-jtqHeo0jyGFavwJRFazIcTLW-Ktuc8YCxMf-8ujgW6jrpRWgO_ifry1bEfzp6NNR28O53ea5oQ5vcZx3Xvbi-dMO4tPwtVdegwFYOPVWR565pz0qreU08c64HJ2skrL0L_Nbzhr-9pvwa2yqTmRyG9xoix1ug1L3wG7HNYbAoV0Gde9NGzZoWXRYGswTDAvU055hdp4IiM2Pw8kUL0kIZVDf65FZK2s9R8r7t79o69edRTXjMX7FhxpwnmmIvtQr_9yvCYBdFa9lC-UIEy5xsPdtSo2r7es_imOwxwKyCD4ZQIESPPPwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tHm6qd_LhIUYGsZzzUB012cTg88aBklwMrNtq2DRmOodN_CRg8Bil-8Fq3Hw3stSZUWYwEjFmBW19mdSrGsfIOLuob9bSFEUuObaklmED4ZJFKUWUHHJgOC8lJkJ5sDF5E5-oic6N9GPbGfJOAblrFElCFaVmDC25bV2q051639PXI3vn6EYwv3Q4LEmt8jnJI6SYRsrWtuWChvVr6TZl2NkmmzpNNsS3_PE1sv8NCZ4AcKbhvAoEPxcNncN-4YGghxX-0niOR0kTX94Q2dpGA8gbGqY7ZXVjgQFx-8t1MSYUMwTXBM8RzU9ys14EW8e_3w92dbookk21GpWzxi-Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
وزیر کشور پاکستان: من در ایران هستم تا نامه ویژه‌ای را از طرف فرمانده ارتش و نخست‌وزیر پاکستان به آیت‌الله سید مجتبی خامنه‌ای تحویل دهم.  @Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/440349" target="_blank">📅 11:44 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440348">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvJytMXUCzwyJYZcOV5x9f1dKg-FCIQWAgMGBJenQ9NYfwBjzlX9XOrT-5EvajPGzmnkup42chhu3sSE57_hCPtY_deqPojH5p7l2DIaWX_kOuZBvxe4z9fIDMttRprS73x7zX-knyQK9nTu5cHhfu4dn6l9tc3LNkHyPXsV1mZvYwjbtwdcNP5pVqqIfRyQbcqTWE-nUqaVlSV0fpVBRNcktUrOkiBquG67erIwKhJGgKgY6ZZQTTRHFy83-hb8mpvStrSnzUmxa0rckMPNB6sa-rRUHo7O2xWu80zR9_NBPtxGZyOpCoEt3hG2lpJ2sWNXvgKsoMTyulzEEG96hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فدراسیون فوتبال: اقدام دولت آمریکا در ندادن ویزا کینه‌توزانه و کاملا سیاسی است
🔹
در آستانه آغاز جام جهانی، دولت آمریکا در ادامۀ اقدامات کینه‌توزانه خود علیه تیم ایران در تصمیمی غیرورزشی و البته کاملا سیاسی از صدور ویزای ارکان مهم مدیریتی و اداری تیم ملی…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440348" target="_blank">📅 11:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440347">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌ طرح رایگان‌شدن مترو برای ۵ دهک درآمدی در شورای شهر تهران رأی نیاورد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/440347" target="_blank">📅 11:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440346">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d04f539e7.mp4?token=Ss4jQJoU90te_zMgUNSWb6MvRs1FpIbHJcI8t-PphFr1H41bqi7k9ZRJPNL63-0667Qt_IG67DkzbIDBDRv1dPxPbI79TPbKcZKbTCWHLVdqZjxG2N3IJPKTAmUcDVimtgpiagbWxwiVxENrNtLlyJWLcOwCitF-a9gU_fErr91e6MYLK9JkPL3ZpnOPwZWOSzH5e1wfKbJ6fMaWhFwY2RagbOUFJV9maDaQXbMyTaM1CFOMPBMeteqKkljSV4a6VppSu2JP86l9My1iKbM2FastdbKPjDKT3vIKvbl26o-fGKI6Nbk2GEQEqoElHKHfRxMo5-jmbNpktZkvZyYM8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d04f539e7.mp4?token=Ss4jQJoU90te_zMgUNSWb6MvRs1FpIbHJcI8t-PphFr1H41bqi7k9ZRJPNL63-0667Qt_IG67DkzbIDBDRv1dPxPbI79TPbKcZKbTCWHLVdqZjxG2N3IJPKTAmUcDVimtgpiagbWxwiVxENrNtLlyJWLcOwCitF-a9gU_fErr91e6MYLK9JkPL3ZpnOPwZWOSzH5e1wfKbJ6fMaWhFwY2RagbOUFJV9maDaQXbMyTaM1CFOMPBMeteqKkljSV4a6VppSu2JP86l9My1iKbM2FastdbKPjDKT3vIKvbl26o-fGKI6Nbk2GEQEqoElHKHfRxMo5-jmbNpktZkvZyYM8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امتیاز نیروگاه هسته‌ای بوشهر ۱۰۰ از ۱۰۰
🔹
رئیس سازمان انرژی اتمی: نیروگاه بوشهر در جمع ۱۰ نیروگاه برتر اتمی جهان قرار دارد و فعالیت آن بدون توقف ادامه دارد.
@Farsna</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/440346" target="_blank">📅 11:30 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440345">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رئیس کمیسیون برنامه‌وبودجه شورای شهر تهران:‌ رایگان‌شدن بلیت مترو و اتوبوس همچنان روی میز شوراست   براساس پیشنهاد مطرح‌شده، گروه‌های زیر مشمول تخفیف ۱۰۰ درصدی بلیت خواهند شد:
🔸
دهک‌های ۱ تا ۵
🔸
دانش‌آموزان و دانشجویان
🔸
سربازان
🔸
خانواده شهدا و جانبازان
🔸
مددجویان…</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/farsna/440345" target="_blank">📅 11:22 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440343">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLcmM2QWx7ro3oDePsWzc8T8r3EnHgDpAB5Ew-SjvH5uAkYmKKlJjvGSgJQB3DsYII1uc8OHwxTsHJUwmfLixkcCp4lbip4SyTvDrNKOlloDoszFRvj4ZAdHvaq3Y5C7Kr8QJVBrHV5FQxKWwZI4N4fAz3yGfFGQNT5gV-nvAEBM3uE0FkXqnApu47bsSWA54yqP3H8-f9FJfWSB2-yXHCSBOQb6R_vksDckPzZRSkt18ftUGfsBiEuizy88kkXQmAD64kUrrYzvDAdhuh2qu3k_FGHAiO5b1Gqs9rqJJdrmJU5HoBrfatqGN-jB7LFe-dPaSR-QS4OBZXdIuJl0TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: هر جا دست مردم باز باشد، گره‌های بزرگ باز می‌شود
🔹
پیام رئیس‌مجلس خطاب به گروه‌های جهادی: تجربۀ این روزها بار دیگر نشان داد هرجا دست مردم باز باشد گره‌های بزرگ باز می‌شود.
🔹
در جنگ تحمیلی سوم که دشمن با موشک‌باران شهرها زندگی مردم را مختل کرد بار دیگر گروه‌های جهادی پا به میدان کمک و امدادرسانی گذاشتند و در کنار همۀ مردم آسیب‌دیده فارغ از قشر و سلیقه آن‌ها ایستادند.
🔹
بنده قدردان این دل‌های بزرگ و دستان پرتلاش هستم که نشان دادند قدرت واقعی جمهوری اسلامی ایران در همین مردم و روحیه جهادی آن‌ها نهفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/440343" target="_blank">📅 11:09 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440342">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">احتمال شنیدن صدای انفجار کنترل‌شده در یزد
🔹
سپاه یزد: امروز به‌دلیل انجام عملیات انفجار کنترل‌شده در خارج از محدودهٔ یزد تا ساعت ۱۴، احتمال شنیدن صدای ناشی از این انفجارها وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/farsna/440342" target="_blank">📅 10:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440341">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210ee8a515.mp4?token=tY9iR3bXGchUQVJ8X_VtevJTZaEvE3yKMz1AUBCkHxBJmoCTCxMfXfeFZG0sAShxSH3Py5YWKjV_0tDfSqYOF6xV1PbXXkhpJRFvqEVETFkqU2v9C_vqzwg1CxgV2ZoxLnjSzx0pU5b3MghHSAwCyzBg-nQvd1eKy8NSe7DOWz60btFsRV2I0SWYSQz1q2E1xDBABk0bIO17i9MBm2o8g0V4168MpCvRZUB95b28m6i3bR9JpA6H3s0tgfMPOC6aB7_gb45v9ge3NYRkctbQvmPbU65NU81410zOharh1hcihAES1snwbTb6Nvc109NDAkrRd8PCYW46hK9cF_wDKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210ee8a515.mp4?token=tY9iR3bXGchUQVJ8X_VtevJTZaEvE3yKMz1AUBCkHxBJmoCTCxMfXfeFZG0sAShxSH3Py5YWKjV_0tDfSqYOF6xV1PbXXkhpJRFvqEVETFkqU2v9C_vqzwg1CxgV2ZoxLnjSzx0pU5b3MghHSAwCyzBg-nQvd1eKy8NSe7DOWz60btFsRV2I0SWYSQz1q2E1xDBABk0bIO17i9MBm2o8g0V4168MpCvRZUB95b28m6i3bR9JpA6H3s0tgfMPOC6aB7_gb45v9ge3NYRkctbQvmPbU65NU81410zOharh1hcihAES1snwbTb6Nvc109NDAkrRd8PCYW46hK9cF_wDKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر نیرو: تا امروز جای نگرانی برای اعمال خاموشی‌ها نیست
🔹
با همکاری خوب مردم در حال حاضر میزان مصرف برق ۷ درصد کمتر از سال گذشته است.
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/440341" target="_blank">📅 10:31 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440340">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cU3SIl0ttEx6zvX_aGmHTXsbwvlR8ev9_hpLA4PigPpsKJIbKw3n1DrGMYT6CtNasuRTI2Mv171zH3J0iS0cmPmXMSVB2juNMuD2xB6fp_SjzRSJ6NLQFL3IODO0ZPq5CecmsrU1JtW2qVKAmQlFQLfwclXi347FG5DEdbnnSJjKOjMdP6bvH-muob2lV4IEmQS8gMuDtOdOkheYgTgVHvLXYoGEgS0EzrmTumMI_S94rsEEePToPg8dUUODnbfj5pxdDEjkuf-8vhfMgqKHf6zDwe3e8oFr-f0eAjzJJLCV3q3YDbMqXejDjK1ZVvxE7oaYMRxaNZafsooYK6ZH2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک ملی در مسیر بازآفرینی/ رضایت مشتری، فناوری و اصلاح ساختار؛ سه ضلع تحول در بانک ملی ایران
بانک ملی ایران طی دهه‌های گذشته نقشی فراتر از یک بانک تجاری داشته و همواره به عنوان یکی از بازوهای اصلی تأمین مالی اقتصاد کشور شناخته شده است. گستردگی شبکه شعب، حجم بالای مشتریان و سهم قابل توجه از بازار پول موجب شده است که عملکرد این بانک تأثیر مستقیمی بر وضعیت نظام بانکی و حتی شاخص‌های کلان اقتصادی داشته باشد. با این حال، تحولات سال‌های اخیر، افزایش رقابت میان بانک‌ها، توسعه بانکداری دیجیتال و ضرورت اصلاح ساختارهای مالی، نیاز به بازنگری در مدل کسب‌وکار این بانک را بیش از گذشته نمایان کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/440340" target="_blank">📅 10:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440339">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4fc7a747f.mp4?token=nDkBzyK8VhO6rPAZ5dFzA575N9dO_mRAxfo26od_WQg3HTWM5D_nycoy8B0HvXl4u_ImVUntnTuK_yRzWyuKLJ22FurchEdYtbz870lPbtBL4JpQ9ApUw82Thtb65lLYeG66H9JbBp74M-sj_8IWwkhIIIyceIsELFwxk7p3JnrAsMz98Hk1jWuw9AE_sve5bvrgleNTRtaj42SLE0X5rsl7ZHlOZQFyBa7BwOf-p2IMIskHgObAFZVruGUHwbTD2-AEUKJWQJzNdrYSXfWJkdjPEOAsBcsHR8_gZAKksDzPBQ_Qplzttj49YoOoVQKOALWx_SolsFQHMPXLVUGVmg9tRYz21ywBXJpa7TSqHkHvi28T_TPP4wLe9SLyenrikI6sLjWAWwW7mriBx61fhIm09YQWVf4meoYhP2g5rFQSvJ5yX_pRT1pINBzzYUlqRH1ynHYTrUHoNF7jwMbmPNMpISFZg3QvLPj2L4K1w3KCGwfGb3NAOiFWCkiPmmJBcSPeiVNtp7H9aYH1YLzZ9TkyUSdeuu_XfP9-DUvM4zPJ3keUyT0HIN2fGRZ8x9UpP8QRHHohkl0wKtccVqOWhHukziirQ-WO2w_xR7JpY9FlV2DBkJC50Bk2QxUyq0IG7hMILyw29TESPKtC_HmZTdXqgtUlXpGvkHIc5DOjjTY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4fc7a747f.mp4?token=nDkBzyK8VhO6rPAZ5dFzA575N9dO_mRAxfo26od_WQg3HTWM5D_nycoy8B0HvXl4u_ImVUntnTuK_yRzWyuKLJ22FurchEdYtbz870lPbtBL4JpQ9ApUw82Thtb65lLYeG66H9JbBp74M-sj_8IWwkhIIIyceIsELFwxk7p3JnrAsMz98Hk1jWuw9AE_sve5bvrgleNTRtaj42SLE0X5rsl7ZHlOZQFyBa7BwOf-p2IMIskHgObAFZVruGUHwbTD2-AEUKJWQJzNdrYSXfWJkdjPEOAsBcsHR8_gZAKksDzPBQ_Qplzttj49YoOoVQKOALWx_SolsFQHMPXLVUGVmg9tRYz21ywBXJpa7TSqHkHvi28T_TPP4wLe9SLyenrikI6sLjWAWwW7mriBx61fhIm09YQWVf4meoYhP2g5rFQSvJ5yX_pRT1pINBzzYUlqRH1ynHYTrUHoNF7jwMbmPNMpISFZg3QvLPj2L4K1w3KCGwfGb3NAOiFWCkiPmmJBcSPeiVNtp7H9aYH1YLzZ9TkyUSdeuu_XfP9-DUvM4zPJ3keUyT0HIN2fGRZ8x9UpP8QRHHohkl0wKtccVqOWhHukziirQ-WO2w_xR7JpY9FlV2DBkJC50Bk2QxUyq0IG7hMILyw29TESPKtC_HmZTdXqgtUlXpGvkHIc5DOjjTY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💎
گزارشی از آئین معارفه
#وفیروزه
هفته گذشته، آئین معارفه گروه مالی فیروزه در ساختمان بورس تهران برگزار شد؛ رویدادی که سرمایه‌گذاران، فعالان صنعت مالی و اصحاب رسانه را گرد هم آورد.
گروه مالی فیروزه با مدیریت دارایی بیش از ۱۰۵ همت، حالا آماده عرضه اولیه با نماد
#وفیروزه
است. در این ویدئو، دکتر امیر تقی‌خان تجریشی، رئیس هیئت مدیره، از تجربه سال‌ها شکار فرصت‌های ویژه در بازار می‌گوید. هنری که به گفته او، شناسنامه فیروزه است.
🎁
خرید نماد
#وفیروزه
با
آمادگی ۱۵۰٪ در کارگزاری فیروزه
💎
گروه مالی فیروزه
سرمایه‌گذاری، برای همه مردم ایران
🔜
+982179672000
💎
@firouzeh</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/440339" target="_blank">📅 10:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440338">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/farsna/440338" target="_blank">📅 10:26 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440337">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/620c7560bb.mp4?token=X8aYbd5FwPjPlrmunsh0l1SfMhmR7iMLN_ef3LvA9cD2Pza0JFcYsenG5dxKC-wJ7E0PRc2ejEZHBzJUAvBJBdGVRGgiaVtGF3cqdBCrPxIk-7bm5NabZedbyS8Clj1Vj_Fov7umGOw2rVJ9kPXxqooXwi1qmbiuMyAkYL25avmm31CDkP2Ab4tr15jNAMXAXAbh9r49qU_nwnGxngTLXNGp5NKlY2Tv--3fEqRbiBXTZodbRdTphHM1VNJ6Z5Y5PmlezXEam2M32HjVsWbgEPRgY-ztzGe6vuK1Oa6BFkkZe7zSIh8Kwotvs4Iph4qZOzXQ--5lpIWGsbowXqliDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/620c7560bb.mp4?token=X8aYbd5FwPjPlrmunsh0l1SfMhmR7iMLN_ef3LvA9cD2Pza0JFcYsenG5dxKC-wJ7E0PRc2ejEZHBzJUAvBJBdGVRGgiaVtGF3cqdBCrPxIk-7bm5NabZedbyS8Clj1Vj_Fov7umGOw2rVJ9kPXxqooXwi1qmbiuMyAkYL25avmm31CDkP2Ab4tr15jNAMXAXAbh9r49qU_nwnGxngTLXNGp5NKlY2Tv--3fEqRbiBXTZodbRdTphHM1VNJ6Z5Y5PmlezXEam2M32HjVsWbgEPRgY-ztzGe6vuK1Oa6BFkkZe7zSIh8Kwotvs4Iph4qZOzXQ--5lpIWGsbowXqliDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تابستان گرم در راه است
🔹
رئیس هواشناسی: امسال احتمال شکل‌گیری پدیدۀ ال‌نینو فعال وجود دارد و تابستان در سراسر کشور گرم‌تر از سال گذشته پیش‌بینی می‌شود.
🔹
در تهران، مشهد، مرکزی و همدان شرایط بارشی و منابع آب چندان مساعد نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/farsna/440337" target="_blank">📅 10:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440336">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9b0a4b99.mp4?token=m-03rvQErVUZV-EeDaUiC6_OArL4oPeanPhIl2_IG6aXid7dprArVYHtea1LH6EilFADxYB2-Jn-x2KwbTQERwWnQAe6MZkWOaNrhUzCdA7bSM9posff4DZXt4cqN2aLLSnGWJQBcmI5LYRaJZ423dLWxj5XPZtuTKZ-LS9D0kOrkVJiIJ6OgaZWm4rf7gnFnzP8U-poBM9fzc_G6KXU-1FgXwZVFs7mlG6yIdKBB12xUY1rlbb0blP-QnMVZqrvotgMR1fj5UQooQtxl0XjGfgxO2qqx7giPy_GZAG3PeZeQcOm4e4Xkclxhy2lLL6ZQbeItS6uuidKGFCTJGHiBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9b0a4b99.mp4?token=m-03rvQErVUZV-EeDaUiC6_OArL4oPeanPhIl2_IG6aXid7dprArVYHtea1LH6EilFADxYB2-Jn-x2KwbTQERwWnQAe6MZkWOaNrhUzCdA7bSM9posff4DZXt4cqN2aLLSnGWJQBcmI5LYRaJZ423dLWxj5XPZtuTKZ-LS9D0kOrkVJiIJ6OgaZWm4rf7gnFnzP8U-poBM9fzc_G6KXU-1FgXwZVFs7mlG6yIdKBB12xUY1rlbb0blP-QnMVZqrvotgMR1fj5UQooQtxl0XjGfgxO2qqx7giPy_GZAG3PeZeQcOm4e4Xkclxhy2lLL6ZQbeItS6uuidKGFCTJGHiBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستجردی، دبیر ستاد جمعیت: ۱۱ نوۀ رهبر شهید انقلاب را در بیمارستان شریعتی و رسالت تهران به‌دنیا آورده‌ام.
@Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/440336" target="_blank">📅 09:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440335">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار چهارمحال و بختیاری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d4527ac0c.mp4?token=EkotANBB2gC6J82fkYALX_tE7YTo5RelaqgmBUXRIpMcj8Xk7kMGupIduaeDz4hxy9nYcObDwTPY8tjHQh4CJB6v4hrWeDSNmJicAPQHpzZ_vzyiNp8NEqwpBgfBcVvP85pa2YzQXoaTO6dCJfoyW9H2CmByx6wNS04kWZy7FziGM9zhMSn0Ai6N-KEiHrrZ3Har3-fepCs0aGXwUNb5alOGAn9romNdSzJdyFt_vgVt6s4OyUbp5HnvCqX_5f2fszumsQFu7hk7VOaDmcqaKxXbRLF2k0US7-tgQAXkfbq6jvN5qnAghHngiIlnc6ykoP5-hr1CJx9X0TLA0PxtwlN35DDe-kLUbzyNRyljWuWTpdANjQ8QKsiaZtIXMGIEKuOECcixzailyZV4cgll5QWatbspWBHHfE5JetTnWjuiHmIGAlBOGSBIzikpw4xbrMlaN_Rv9XiS_eTL3guR76uHeT6CNOzbmfRjxShr1fJPdwZoHkUpj9PZ7-M8JI8KmaDsTVmobJHIemy7JeBE6OPhEnqdOu6Xzy0j76KuLcsGrBoi5TR45f50r0toj-UTmM9xhm9ZglUIE_YEToJ_Q3Ic7xrXi1CPc3pk74vEAlvZ8WH022lvXl0kAUmYGJOfYJRTI6SHBGU2hqi77Pi79Kb0vu5vfci0OuCkrbP4fnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d4527ac0c.mp4?token=EkotANBB2gC6J82fkYALX_tE7YTo5RelaqgmBUXRIpMcj8Xk7kMGupIduaeDz4hxy9nYcObDwTPY8tjHQh4CJB6v4hrWeDSNmJicAPQHpzZ_vzyiNp8NEqwpBgfBcVvP85pa2YzQXoaTO6dCJfoyW9H2CmByx6wNS04kWZy7FziGM9zhMSn0Ai6N-KEiHrrZ3Har3-fepCs0aGXwUNb5alOGAn9romNdSzJdyFt_vgVt6s4OyUbp5HnvCqX_5f2fszumsQFu7hk7VOaDmcqaKxXbRLF2k0US7-tgQAXkfbq6jvN5qnAghHngiIlnc6ykoP5-hr1CJx9X0TLA0PxtwlN35DDe-kLUbzyNRyljWuWTpdANjQ8QKsiaZtIXMGIEKuOECcixzailyZV4cgll5QWatbspWBHHfE5JetTnWjuiHmIGAlBOGSBIzikpw4xbrMlaN_Rv9XiS_eTL3guR76uHeT6CNOzbmfRjxShr1fJPdwZoHkUpj9PZ7-M8JI8KmaDsTVmobJHIemy7JeBE6OPhEnqdOu6Xzy0j76KuLcsGrBoi5TR45f50r0toj-UTmM9xhm9ZglUIE_YEToJ_Q3Ic7xrXi1CPc3pk74vEAlvZ8WH022lvXl0kAUmYGJOfYJRTI6SHBGU2hqi77Pi79Kb0vu5vfci0OuCkrbP4fnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زمین فوتبالی که در کوهرنگ به گاوها واگذار شد!
@Fars_Chb
_
Link</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/farsna/440335" target="_blank">📅 09:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440334">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7301e98b8.mp4?token=clgiyUKR05wEfQhztqI4z03cZ3g6giKcbC__kkUyslrLl8-hmAv2sPEz35MSSM95v37L71lGUjw90-Froi7A8hMw8oVlILL0PsTTpl5h78d1r3rStBr-YK4FlIUcBQMbpDDJ2syPZDR-_FxFJauKX5iL2NSybyooY9N0fjLnehKpa6sgLVQOK0ihyMHKcmtG9N_muRNWYyhvI2eWy52bWhBiTRoAiV4HunvkPXNz5PQAJFHm5KzrDjUXvyBapMKQzo_huOcbSydkVWiXIkSa15_H4HsxqBERZWpVixhMz9va0AdtwtWN05e_aV3m9VL38bdsNdlzjWfov70sWU5u4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7301e98b8.mp4?token=clgiyUKR05wEfQhztqI4z03cZ3g6giKcbC__kkUyslrLl8-hmAv2sPEz35MSSM95v37L71lGUjw90-Froi7A8hMw8oVlILL0PsTTpl5h78d1r3rStBr-YK4FlIUcBQMbpDDJ2syPZDR-_FxFJauKX5iL2NSybyooY9N0fjLnehKpa6sgLVQOK0ihyMHKcmtG9N_muRNWYyhvI2eWy52bWhBiTRoAiV4HunvkPXNz5PQAJFHm5KzrDjUXvyBapMKQzo_huOcbSydkVWiXIkSa15_H4HsxqBERZWpVixhMz9va0AdtwtWN05e_aV3m9VL38bdsNdlzjWfov70sWU5u4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخستین خیمۀ عزای محرم در کربلا برافراشته شد
🔹
درحالی که تنها ۱۰ روز تا محرم باقی مانده، این خیمه با نظم و تزیینات ویژه برپا شده و کربلا را در آستانه عزایی باشکوه قرار داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/440334" target="_blank">📅 09:28 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440333">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
آژیرهای خطر در متولا در شمال اراضی اشغالی در پی حمله پهپادی حزب‌الله به صدا در آمدند.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/440333" target="_blank">📅 08:24 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440332">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nDtWNR2BlkY18kAkfeGnzftltZ8cKW39PVmQMb1dVm_aO1JiporsZHYqRiw3QIIM51KOlmHV7JP3OUcgaS3xNYzcDkWZ81EAKbYFekVrOKV6oYWP1Tsc7eJfjNhrqpl8JeLgTHY8bp-RSNuSMeU_hoz1SJxqjTWQTqkvJo62FhbkEE7mLalJf4REUb5eU2-FM-D5O_2U1Uy0UDCh6ncSDfJRbgrcSuVm2VI6lEnjrGoXLeWOkQl9a15H2Y8IAAFPUabnw75ssu1o7HPVItHdYhOyOHB0nssy8D5Mw7wnf9T0RQbd7YFdqa9Ry0ePShq47_uYpfxWNJx3HkNhoA7x0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
تصویری از سردار سیدمجید موسوی فرماندۀ نیروی هوافضای سپاه، همراه با شهیدان سیدحسن نصرالله، محمدرضا زاهدی و محمود باقری
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440332" target="_blank">📅 08:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440331">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/heAZ0reZZj6mXCAF5jKVE2FQHn12_AIAl0w6sUt35I0eRIffmZzrVCxGCtqMaDMGS52vpe3ovlDDD_qBhRvNe1aTOuGslkKLzWJ0qnNIazwNdroa1sChvZ0uDsC-d-X-rQc2YD2pcJVHIl_T9bl88ZFsldx-3zFiCkwdpJkW4WeEhDvdXzCHX5F8dd3yVhODJ3KVBp6faZj-HlCSwiJShrU3ifgHmILXeQMb8YSwRj696PNqesBA4_Tq-vEJQ89SiWX4XK6apo3TERjwhpIQ1wytIkveVXGkMjFfUkiPkIVttBXcp_xLs6hH6p41hRnoBQd2toDejUUyBNhM7mprIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودزنی آمریکا با بازداشت بازیکن ستارۀ عراقی
🔹
روز گذشته، ایمن حسین بازیکن تیم ملی عراق به‌محض ورود به فرودگاه شیکاگو به‌مدت ٧ ساعت بدون هیچ دلیلی بازداشت و بازجویی شد.
🔹
بازداشت عجیب‌وغریب ستارۀ تیم ملی عراق به‌محض ورود به آمریکا، به سوژۀ اول رسانه‌های دنیا تبدیل شد تا میزبانی آمریکا قبل از شروع جام‌جهانی زیرسوال برود.
🔹
نشریۀ موندو با تیتر «دستگیری و بازداشت چندین ساعته بدون دلیل» به نقد رفتار نیروهای امنیتی آمریکا پرداخت و نوشت: جام جهانی شروع نشده دستگیری و اذیت و آزار پلیس مهاجرت آغاز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/440331" target="_blank">📅 07:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440329">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqaaZXG4GqHVWDhRHaXWIoxEmMMtHwgGp5zE7REvLnVayoaAXR65PmSFAwX0s1-N1XsnRsmdlAIs0KY89H_tPqWchtlG-LhkrEQsmVzI7vNGMSnyimHxHRUQ5sFfvDu4tYKTBUzYfNXFALk5GL-vM0sWSnrY59xbSgQD4o2yPiZ-O4S7PBpDNza2IfQL0koBFImt_jAvJMw7Leqv6e9fmht5rCSfIhC6Y7Of-eQCogJpKpI7VdKpkdlI5uvKGgzgVB9lG_Wrziz_DL73XXH47XmCr0NPgtXmxErSZ668zKjz-h9ZPdndmrH6Xf4Byk4mq7FNTf5D4ykpstblI52CRVlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2ffdac381.mp4?token=e9x6iGT-1Lyu84BQdvZbq3Ew-Xuoq6PwA81qaG879PNeBQPmcy5foAt7LYZVUIqCCwOxZw2evDjOPtOR4gpa3H_39P3juMhydJ65mAyFwupH92PVDHyNMn8EeEn_-rN1OmsO7ztQyXSIBX8AoBRYzZz3-ehWMztRd8z876jYR814bj45hSXGIwtd4DpCILmacSP1tt68qXB-1lhq5nV14fOSe1G-D2FzKSD5hJw9aZKelCacn5-iTxVKj3pxYB_s0AkUClhjgDER8brbNk4D1jTmPWVh1ODjSF64WcLxJAEU7OdRU_ATqnpc1UG6gY592z5PFBwtxjHJTm-nHCHBqaaZXG4GqHVWDhRHaXWIoxEmMMtHwgGp5zE7REvLnVayoaAXR65PmSFAwX0s1-N1XsnRsmdlAIs0KY89H_tPqWchtlG-LhkrEQsmVzI7vNGMSnyimHxHRUQ5sFfvDu4tYKTBUzYfNXFALk5GL-vM0sWSnrY59xbSgQD4o2yPiZ-O4S7PBpDNza2IfQL0koBFImt_jAvJMw7Leqv6e9fmht5rCSfIhC6Y7Of-eQCogJpKpI7VdKpkdlI5uvKGgzgVB9lG_Wrziz_DL73XXH47XmCr0NPgtXmxErSZ668zKjz-h9ZPdndmrH6Xf4Byk4mq7FNTf5D4ykpstblI52CRVlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازگشت فلامینگوها به دریاچۀ ارومیه
🔹
با بهبود وضعیت دریاچۀ ارومیه، پرندگان مهاجر از جمله فلامینگوها به پهنۀ آبی این دریاچه بازگشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440329" target="_blank">📅 06:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440328">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EeL8r2-3BDNmz-sdA51B1Rp--aHco3MJK4VsRb6byWHMwRhrGLsA-c1VdMzYiW104xlnwdjgYC1JBYGUhRXZOqLwFOVtCABzeLj5VECSwlEFmd54JA6T7b-FyDelueFxqhx_XYrsCKZr8Gzp3wqxRYRwhR96kSG6_IQQybtscq9noeUJVuve1P3QnQxopDVoRsy4gAHFMLasxuDgg7Nz5Coaq2knsgsgi2Oycfb04SG2UzOI2oz04J6OeAwjPF4wjsdi2etaRQasfF3VJOgRezNhA77ecT_2XF7nej-gc9RWJ2ubLhWryfmviumN4J1s_4uPEPLM8I_eNEllAE4j5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش جنگ رمضان کرایه کشتی‌ها را شعله‌ور کرد
🔹
موسسۀ دریایی دروِری اعلام کرد که از آغاز جنگ تحمیلی سوم علیه ایران، نرخ حمل دریایی کانتینر ۸۰ درصد جهش یافته، تنگه هرمز ۹۰ درصد خلوت شده و ۲۵ میلیارد دلار هزینۀ اضافی به شرکت‌های جهانی تحمیل گردیده است.
🔹
کارشناسان علت اصلی این جهش را اختلال کامل در ترانزیت تنگۀ‌هرمز می‌دانند؛ جایی که حجم تجارت عبوری به کمتر از ۱۰ درصد حالت عادی سقوط کرده است.
🔹
هم‌زمان، تغییر مسیر کشتی‌ها به دورهای طولانی‌تر، هزینۀ سوخت را افزایش داده و فشار مضاعفی بر قیمت حمل وارد کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/440328" target="_blank">📅 06:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440327">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0b485ee0.mp4?token=vvY22Apbz7nFqE7G4BOVlmDKdRY5UWfn1VJ3TI3RCzvUH4AO0-li4RMf3cuAYVWvyipR4hWsQwnBxMgT_DOYtKpBM_os1C6Mn7bPsl5goWAhWmUQfwFKGLEkcRkHXki6Jk1YULZuQBZHfJfo61WN3BsMCSfDsw5lEM2AqdR-BBm2SWa1zLJoWQWta3VB1D59ZgYP1zJ86x4Zhha17iKIUv0I1uwWd0VqmO6SqAVzDyq0uWFb9gurhxetAQ5kdP09WUkj6fO_ykOSdybssyN4f68yv5Q4u1MH5FLooBpo8L9QqZ4FiEaiwxF-Qk3KW96wCYW44jOO4VbQOWMfVbzWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0b485ee0.mp4?token=vvY22Apbz7nFqE7G4BOVlmDKdRY5UWfn1VJ3TI3RCzvUH4AO0-li4RMf3cuAYVWvyipR4hWsQwnBxMgT_DOYtKpBM_os1C6Mn7bPsl5goWAhWmUQfwFKGLEkcRkHXki6Jk1YULZuQBZHfJfo61WN3BsMCSfDsw5lEM2AqdR-BBm2SWa1zLJoWQWta3VB1D59ZgYP1zJ86x4Zhha17iKIUv0I1uwWd0VqmO6SqAVzDyq0uWFb9gurhxetAQ5kdP09WUkj6fO_ykOSdybssyN4f68yv5Q4u1MH5FLooBpo8L9QqZ4FiEaiwxF-Qk3KW96wCYW44jOO4VbQOWMfVbzWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امام خمینی(ره): شما جوانان به ملکوت نزدیک‌ترید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/440327" target="_blank">📅 05:41 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440325">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njdmX0yv6Vosdd6SEG6d5eWkMEng_HmsNbnsAOd6XzvEZANRUIn1zmt43VXR4PLTOG0WqfGJvDJpFEji2ifBSgTHZgqND2x9LVlgnBIFiJH3zrswit-G7SuTeLPRxEL5wtmYpIcC4cGQZwguHFIaxNHaUiGGvbpPW7CWOYRvVYsAh7V9mAQj-nkTbjvdt2iS6fGqZjnDaqX0JyHg-krXcwP1QvzPYsnphAfmgE07FtWJKbptcrXXh4mOjxpBeTdS08JVreAf_qEwWpnKEo4gjdVTDlbFbF3Kzx6k8RmPlGOVAqsoBd_7wffSoLQzAO-11Bai5oytqbUZBO0oVTNmkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب خزر به میانکاله نرسید
🔹
سال‌گذشته بود که مسئولان سازمان حفاظت محیط‌زیست از ضرورت احداث ایستگاه پمپاژ برای انتقال آب دریای‌خزر به میانکاله سخن گفتند.
🔹
به اعتقاد متخصصان، این پروژه می‌تواند نقش حیاتی در تأمین آب تالاب و جلوگیری از تکرار بحران‌های زیست‌محیطی سال‌های اخیر داشته باشد.
🔹
با این حال، پروژه‌ای که از آن به‌عنوان «طرح نجات میانکاله» یاد می‌شود، همچنان در مرحلۀ انتظار باقی‌مانده است؛ انتظاری که هر روز هزینه‌های بیشتری را به این زیستگاه ارزشمند تحمیل می‌کند.
🔸
فعالان محیط‌زیست هشدار می‌دهند که ادامۀ این روند می‌تواند خسارت‌های جبران‌ناپذیری برای شمال کشور به‌همراه داشته باشد؛ از تهدید حیات گونه‌های گیاهی و جانوری تا تهدید معیشت جوامع محلی وابسته به صیادی و گردشگری.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440325" target="_blank">📅 03:46 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ETGwQ7MBTq6-2fSOR4qXKtAU4eUrREBQoMKeiuMFnVTT82_jRdZb-WUhdPcrCq_QCX5USxj-1psSHn0X93pJiQh2SAxgqwBHAzzKFmoaz85yPrQd3P_I_MHKcsDF4K9A1PAhq79NWPBNciM0IXfRm5DopUnnKGnh0s7NwqcGT1XVsjHgH-_l6qBaXEQJZQbv1Oi_F-3iIh9xl6BaG8JyZ3Q8UX0UKKdzOwgU-DFRsdZrGR0gFGKZ2pFsWP8Wn9pJK90tSDopjSAp1133Lc6wUd6fgk4vunacA_ZLhphDsmbFOtImzQIdXffUEzAHFQqHpDhWyHwM3b7hZPOZlq5jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XbWmQrX05x6C2YqoDcJaUyuSBdRxNU8M5aq5DQZI4m7khFWQLG7IfQpDNor6QNJS-02o0BYRsTUEemOK6Y97zk5mTnYCK7vcrwQL4EFZgU-MWsGahpUtZl4VhJ-QUBhQJ8WLffxGlLWR6nEAqs14BqFSp0jy27fSrVi8-NXr-jaZhRdUp-beXRVIzCGP-gem8c9wb4Md__bboBf-9y8Enpzx3NIwPEoPAt99gem3ETsfxYpE0OTAf_WK-s7hOYfAKYWPu1wxF5Rl_jECvVwMvNdbY2641kNh9AdoOW5HH0P1NXT_0cSBT1azaWAuInY4YzZtlVUjfG4AbPlsttasOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Szkv9r8nUbPoxO-ZtU1GPMlh83qy-HKcWFuSQZgC1MGURY-Kq9HCu2ir1WOiN2If9Eq5-h2O7VyBR1uLQyaJsPNw-RHn2UYXr9qbWKRxiw3ab9NMbNisjoBxX_AI-WQIVsUn5QVeUD7SlnYZpKkYcrGRt4ymklKS49WqojNDOZ0a850YQJHNBNCyV0mpm22f9dkfgc33ALFbuZRemHZCwlCHDsExhyqOCJK8vEfxD0hpYA-lEx0ApOr8q2zHpAD3BjwoT5dxCHqNW4cQPi_Wb0IxadD6P_zf2aBIVPeQvfg9JuEJXMd7oVTeQOutBBlo8Deo0HHcFIjXSPI_wSG1EQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افشای ابعاد تازه‌ای از یک جنایت علیه فلسطینی‌ها، پس از ۵۹ سال
🔹
روزنامۀ عبری هاآرتص پروندۀ یک جنایت تمام‌عیار را پس از ۵۹ سال گشوده است. جنایت شلیک‌های بی‌مهابا و بی‌دلیل به زنان و مردان و کودکان فلسطینی توسط نظامیان اسرائیلی در جریان جنگ ۱۹۶۷؛ شلیک تیرخلاص به زخمی‌ها، شلیک به کودکان و به رگبار بستن پناهندگان.
🔹
یک نظامی اشغالگر این‌گونه اعتراف می‌کند: «از افسر پرسیدم اگر صدای گریۀ نوزادان را شنیدم چه؟ آیا باز هم باید شلیک کنم؟ او پاسخ داد: زن نباش شلیک کن...»
🔗
متن کامل گزارش را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440322" target="_blank">📅 03:13 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFAVCo99X-M_vHgo5-Y30IXiqlUhcX0JWhM8gb4NFKwW9T_t_C9IbdkNip7VYlG1g8TMSTKFajINUsMVrJBgczj6N3vUlHBxlEmhYfgkFIRlbc5Ni6Q_jDbimLSEc76BFZfQ9zy6dFBMofAUEicR1hDdfdsLkxoPB79eBgstKsvk9Ed8zlo8oHvuevMAmVhLZNw01BfXxS7IRnpfOCEQXusnU9tl_OWDGTQXNfomb6qrIffnB8Gxs0XrszxnWiB48yzTy61ygimr70RKJB8ic12a8Z3KYXKU62s3W5Joq5AOrWp9YA-RlyVCV0FUG8148clNlkLAk3x4HCiKbmXODQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ برای شرکت سازندۀ چت‌جی‌پی‌تی دندان تیز کرد
🔹
ترامپ اعلام کرد که با شرکت‌های فعال در حوزۀ هوش‌مصنوعی دربارۀ توافق‌هایی گفت‌وگو کرده است.
🔹
اگرچه او نام شرکت مشخصی را مطرح نکرد، اما گزارش‌های منتشرشده نشان می‌دهد اپن‌ای‌آی یکی از گزینه‌های اصلی این مذاکرات است.
🔹
طبق برخی گزارش‌ها، یکی از سناریوهای مورد بحث این است که اپن‌ای‌آی بخشی از سهام خود را به دولت آمریکا واگذار کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/440321" target="_blank">📅 02:35 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">روسیه نسخۀ بومی استارلینک را راه‌اندازی می‌کند
🔹
روسیه قصد دارد از سال آینده نسخۀ بومی و کوچک‌تر خود از سامانۀ اینترنت ماهواره‌ای استارلینک را راه‌اندازی کند. مدیرعامل شرکت ایکس هولدینگ که مسئول توسعۀ این پروژه است، اعلام کرد که این سامانه هم‌اکنون در حال ساخت است و ماهواره‌های آن نیز به مدار فرستاده شده‌اند.
🔹
به گفتۀ او، آزمایش‌های این شبکه در هفته‌های آینده آغاز خواهد شد و مطابق برنامه، خدمات تجاری آن از سال ۱۴۰۶ در دسترس قرار می‌گیرد. او تأکید کرد که توسعه این پروژه از مرحلۀ طراحی عبور کرده و وارد فاز عملیاتی شده است.
🔸
تلاش روسیه برای ایجاد یک شبکۀ اینترنت ماهواره‌ای مستقل در شرایطی انجام می‌شود که نقش استارلینک در جنگ اوکراین بیش از پیش موردتوجه قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440320" target="_blank">📅 02:10 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440314">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DetZ6SUa6r7S2_8WTXENJCCMxGCBm4Vq6198Iwm9lzlcpXQzKqTTniLI_LYD0xMnZ3MBKfcQs4EoxvPGUDUm8VSeKfTj1NdLHk34I9EJ5Qg2y9Lc1xX64rcax4kvn-03s-0G6BFX1m6ev7sMmLRHrQZxSNiYoUf-zQPUiLY--v0Xl_vt_V0jpn9WpbUUmQ_CEjSFv2kJUKhnTbyKgFnD8Kr7zA9kfdHz_V8rk8J_5seGsLc8zH896pZRVQXKA-1ttdWyxQgI5QDxG9IboVv82gen2x2S5xxInXCx8vrCrHPIJTDFcdhv87pU1M-_eLp_ETHaxRZE_GNX8L_ZGBHfpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fgUoBI-WPe-WWDpqoGt0xz3BzzCcmukB27BdrRGK6KhoyNylktHZVeMOAPbRdpDfei73nc5Zop4fUOMWeUAod8JmGPfgW91PVnMla6D8GoQLUGjZ0x2p-TJEG9VA2-8qC-cRNlMnVWGsJpTmff6b_0E_GhhlGq9D28yfDALojdd7CEf8ylNKkG84_mdEihLUcu0GafoMNegdgsdJXfjYYzGdYz-AYR82PhTaCLOm-3t29wcoSv661g9q9ZrY3b3o_RZ2MegBJN-P8zFN0kNzGfToZ65h2wpgikZpCBVoWiuUkydHu6efojBtGgAm3RaRKtbmT6EibJrpS4JmbVbxdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vMvQnrcBOhJAxNmkK8k_-yZs07vBABjxFppjQN8pzhS2q_wF3aKxyeoDgDwprMJpTP8q9IN72rv55L17FGz4AjMjIfTOrnV79so1-LfLdr4yfNw_I1NwvayNQD9T4BiAiQkciFfhR91o5BiEOIqWLW-3egJrtqRoPL18EZDdJmVCpr8y_Dhen5nn7dqA-EEi8U04OekdU4JpDegHt1aVtfz4CRM1VNnHQCg64jC0cHMcOeh_LyAHaQZFh5-9TsPzf7CVWPDX7mYOhJ5nBaykC1i9YG9bjrR7n6VAenaNL3TVh8NlpS7WfQgjB6pxhk-_rxkjKR_S7H9kE7LTJA8BhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jlBd9l5DdDXo8oiRvmFJhjfWKC1JxCHlbRuxm7Prt_GmnoOvu9ZtpnbxwHhDhL7EYFQO3Mxmxb2rUF1C6yy0J7xaOxu4S8i9yEwVwo8pgqVVcPC9VmUgC7H0ytb81VBfQYxm1OubLTzQ_obKp7243cp70uxc6BiN2SZ8cIWVIE2xEIdYOqEfop869WLEqLQ-oHhaJgdMJjLHTideMpUmdYfqKXjVUlO2euQwqvXK97zU9UBQx6DxmBZPwmksb5r0ijGoZqRoXkp_J2MNa1i_f3jlSoZEopSTYkWYXgdvkvWQBXzL2w7iHAa22rT8ET0Qd2CRm_4ppiIcRD_NTr281A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kz477NzHDqenx9jU6FYm52pRlcQxijFd3gA6sl5mYJZIMViy68-qfbRu-KLZwkUf2uPTknjNyPXqskTanjCds5EI41z9mx4uGvyC0vXizrDuenTGDuXirUxhUVjkouyJznf_lPrY3WfRgDnU9QaMV3FZ1w-jJON0DDxPYU3EF3AaN10mrd5mrcmJ4SgKlMTqnhGMOzkdnHJdwAXAsmHJzfI61bczvIqvVDM_CaiN257uqXZCiKJx1fW_3hukmqTdwhtTXRDSpbH5L2v_GaIzzKoqXp5boIjRCtNBC0vXgoMxlua8BJh7XdTuGaoZTYdRn2Imn7OsEcgU39cW0rYk0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u0hEU-frqrbf5cInjRt-iRqnVOaFV7ILYJRAKGk3eKtYO2zbABlhEa3nX1UowTiEACnqR7kgiI6uTVzDuW1NoYwmjC2Py-8bZgdpp46ukgmkl1e0tqsatsugUzpYRnC8i8zvbgJSQz583XWFqF9b6o-SyqriSMBIYFMBoxOZwPp1KMLdbKIYTgO6TZpXwTwtznvxMGtpKoGbzBhglstMYX3h0NkZ4Jf4OB8U37n5Rq_T93WGFm82jtbzrF6AVGwsVyElqq8Jl-6lmxGITBv1STyC1TIs-OssJiVK3R0xSjnhjUWtcrcXr0aD4y0QPDrwBzBcvFn82C7QxZFJfTUaBw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | یک‌شنبه ۱۷ خرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/440314" target="_blank">📅 02:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440304">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYTL8e_0wasmD3v5pC7PNb8ylL2woyaoBL9fPgGrkgdgqO0r5Idu9VjrH1_lYEHotmuzZvN-2ppYZjEujObHrs_OrjBVuvX_2BhuzDmnLuiikrN2WgN0JT1u2Z4plIFxdGevHu3nuojmqJUBnWOcu4HF_UXlN4h5kaPwzxMgqOJ2RfiLd_eClIBxIP-V-AE9VZuCFFQM7KD0l4zkExPhPI6fPfHil1KYhJ94JmBUB3F3Na4EZ6VWPw-Cr1pARq7yv-emiBETToU42LxDazQTVraWPgxpjJw3LgpgqaNXN8SDTJ6ZGSMWw1XWH0FeLjDNu-vJa0vSqmK0hNGAEsmVSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AjzLYqVYNUa6IqlrW_VZBG2YGRDhbNZEahiYwj9Yp5p3NlVu1r16JilS4jvh6Fv9k8791FhMcvJs5cXyo0pav44oQ5TOEyKLy73jWSls8oCWdfEV36YNgcglqQkLtSihG3F42Ygbng3TXJK6xwxdLD_FVS2UNtE7Yo8OkAuFWxuzi1-lapk0ikKWsxhgV7_55SXgbXb7hSgo2SAOGSDoF-yODmhQbmKkldHawgvHzVqHLwsDXdbi2AEr3z_yiE-lbhhh_yV57UEQwm7_ZZmTW3XrhHOHZoTvHJsxeYzoPcrFYHBl_aP_i7JeXYggJERPAkCW0xKvzAPH-oKBi0GMVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLPw6XcjmkIp17lyjuYoKVeEE3Ey3bYpYR_wbhsrnQoTJVDuU1uok5l3fj_nYDiUu69ab-6kUyC8yYzqXMmbTgCULRffVY5lst98yK8WK7LcLHB6cZ3DyRZSBU41jh_tSUAhawqFfpyQLzXoDa1VmKR2ZGIVhT9YsWLrvA2BkyGtYCwqIdCFd2lw6DpBV-27Q2H4weCYClVVBrPGrw8RX0T5UAbyU_o9aJ5Zv3e_QO8ENL4Yvicmfdt6XdGSEAqgziDBETDjANF9Es2a7Rc4oO_-WG_olQUam2dqT-PBnba7w_6j121XVRKCryQD1YmKTm0kj_jkocMgZe0WXAmv1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PH0k2i09mCChp59klK3B9RECShMRgS04qbgZuBtL2O3Eg35c624ABNM0hJlK3w66jrsFq5PM8S7Mij4phcX7nS06uNJwzVa06dm4MbzAqQAsZoclKqgqPJ60H2nYm7nV0g4LL8PVKFemNy_hCftfbV3TVZL1HMoGx3jvurf7NxaDGPtSVkczby1PwtuSVqmfZ1D5pvpgTYlZrUsk6egPBjyoxZ4o9-ziJiqQRCBRyioBCD0JHyxySN8S2SmoX0QFUoIyzNmHoKwnnIIxoVpVUHrhJgs48Yf_fRQufg6m7pHK7dOSV4DK78WYYFSIeMVdaJBQc3xXG_GSNwAB2hlDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eX0eLKpSJA-sM8sVUJXn7PXBbvM0c_VyXjklPCuCc7EWaZSH9VPPbnAuPQPlKIugcTqs2wRzPeu1RNCM16uOZt4KHQK5-5Y-CqhOuKCM9pyNaNWKBSUYWoEn70-12jfkwxhVdq-cTZh9puezzgaRaama7rOnMIDTGDm-e7Gg-DBLshaDeK20VJMf9rcOLhDZMb-VEqG1Os7w3lx0OhXlY6wuevwGOkOGcAURP3mucoPcJZ9wyXrPK7bCvEfsTT50rALqIpIle0zj1UehLF4ohwyNf85A852yM21vquXxViin5CVL4nPCMwdka_a1z0UKYdJazPKHp1RuS15d-EVLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_MAN3nnTcdzEWyM1n5DJex3pS2Xr5EW62ne-rtSR6sdoz4FqY-pcbZ9po5-TnaV76pmYgEbxXQ8fi7k-1dAq3r5ktlXY62skgJ09UPLMkAIK56HmzDU6dDRo_6g9s412tjfAv1r0jO5t9bO_Qpq-KxO2XxqprpzJ1uKPClO2MR5ntCbgK6UOqp0p2yWVtXLG3kltqeIagNkMBjufmE22w9k2mi5iS4J3NLDKpqvASeMv1Y_RetIUpVY-LaB5zPspBytQ7tVmKDndh6p5QFhdyV9r2uTi6PFYgjYcZQKuuHSZiw5_5wtV4oOp3Xg6WQv7If33oe_7c-5NVYy0PbQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mg9RtrbO-1gYWUbcrJ69hXkbTj-evFdI-kYIFq4V4RFIuWLgbpMQZU98dfoWCIu4czTayX1eqegpV40uF89ptLQqJBR2uQ8gckyRnLGrUYYU_fZysdZ4SCYauqa7NQqWbVVd6ey3e2-oYTs6Zsi_7OtwAyie4ocq0kqmlB_KHELv1Ui2np2tnuPaCa-H6AB2M6-H0ktp730yuJ06HGFrCmqdtaFK0_8dhaV1sEOo6M7zAqeruE8DqO0F3g7F5WkC-TgyDutTWGhe3OCDey85MfCamNpkqK7OHgk6hTM-HVPOHHmv1RxrJzyLzjdAOifDZwGuXZFD9JH6O9dIzrg15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROezQLmm3bG0BNIu_-6gabqm6EOnN999WGiuQ8ESRNCQ3LtFnTS-Isrb-gzb98to8J9DlW7fJcDMwEkGEgDXKTk1zgcsAGz7eDksZqT59NsR8EuQ-dESiMlGkpKr8ZJaqbd2Rn-Fxi1GIBckvlsUNmh02moM9KJAJ_ylENkWdaK64WQEXcwWpxQARZVTCWFA20kpsERWobiTvGV_QMWvrThbDu7tAFrTMP1ZCxOlE7kJi540C_U0kW30xwX0JtGePdov9PPyJjFp1LDVwrZP8lTGew6Ag3id6euNLv1HdBGoG5zhkJzpEwfB2_L6Hoe2XtYZFSoHOrz0TqWl3hzz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b4Bp5tn3C4U89GzrPWSqbM5htbSBXqhlsx99ltlYcv9gZfDOLdRmSlAI7tsYRBrvI-IXjXsA_Vi1FGq-zUlbbnQI-bMPOdwWaS5XbofawlWr8hfdDFlKPckIwYWL8n85jAxPNjFy2ksjTNgMGliDiIRwub8-NO_SkugINS0WYdpmvIEK3S6vYyw0Q88O1ZjJlrs99Za905Wq6zmzWwOXhYPC2Ri7RJr1l3UysD8HhbPNuKZqNtgNujlm4aEalDLwC7i6Xrl8jFPRr_WPfeWtGNs49KWeor8Nlw0vc6t9ugVXkVCOEFrGXnjKQ5bT9Z8zK6FikwnnFcEpyVCbbFD8Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dj1MidbiLQDTaFFzU_fNACldJZ9_1gjDipKlJQ7I-hpgqrgEkgjDgJL4NVFpqkE4uomzCR_-09ePTnP5b8itHYPlFdeVGxtogZL-jErPMVxa5Xs6ou_9fAIqLCjXOxaS5Bxy3Z1v_pYGwXSBc8GR8mThJQK6Ce_10-zjta2WXlZpMkPwHEMcq0TORHs6NLVHE3vMhWDuatvhLtazw1-js5l2vY72LUQ-F4zmmLPhm6IZ5XiS6dXGG58k-NKLGPaMtTYgB0Ev_vGB3S_XUZ9991tDvTmCRyHRKbFcTHLAzNqDWVNM8phb7DywcduENXmleff8BJgvcU2EkrNXjmEHww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/440304" target="_blank">📅 02:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440303">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">۲۵ عملیات حزب‌الله در ۲۴ ساعت گذشته
🔹
حزب‌الله لبنان اعلام کرد طی ۲۴ ساعت گذشته در پاسخ به نقض آتش‌بس از سوی رژیم صهیونیستی، حملات به غیرنظامیان و ادامۀ تخریب خانه‌ها و روستاهای جنوب لبنان، ۲۵ عملیات نظامی علیه مواضع، نیروها و تجهیزات ارتش اسرائیل انجام داده است.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/440303" target="_blank">📅 01:51 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440302">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TX-1-VRe8hC4EJiQcqmvt8bgI4X1vh1BXKwVbxHJ9JIQJTpqd7kkKBnl4uG-CqvaMdKDhgPKq4l90srjRTDi_1WiCGPeA8Nz8rxFeovG3Cyx35ZT-nrJvlZ8IIriznjkfbz02Z3R-6655B78tLLARfXBS5lYDQTNcbTrwhHcAXSqjg2M1J9-Wnk-XmmVe1erd6xktfepZ2VYKKd6mxr1UIvenY6XnD5JQZoH7u9QcatiFjyFuoo9RlIQfQa_XUSj0mSp00PhQ9ox1ZOStcTYCPtLjafdy9VpXEizXOe4JgTUT6Ebr1qI9vLGwK8_5Ic5gv0xWpnl7RJy00q9S0z1_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا در فکر بالاکشیدن اموال ایران برای بازسازی کشورهای عربی
🔹
خبرنگار ای‌بی‌سی نیوز، به نقل از یک منبع آگاه گزارش داد که دولت آمریکا در حال تدوین طرحی برای استفاده از دارایی‌های ایران به منظور تأمین هزینه‌های بازسازی و جبران خسارت‌های واردشده به متحدان خود در حاشیۀ خلیج‌فارس است.
🔹
به گفتۀ وی، دارایی‌های موردنظر می‌تواند شامل منابع مالی مسدودشدۀ ایران در خارج از کشور و همچنین کشتی‌هایی باشد که پیش‌تر توسط آمریکا توقیف شده‌اند.
🔹
بر اساس این گزارش، دولت آمریکا هم‌اکنون در حال رایزنی با کشورهای عربی متحد خود در منطقۀ خلیج‌فارس است و از آن‌ها خواسته ارزیابی دقیقی از میزان خسارت‌ها و هزینه‌های بازسازی ارائه دهند.
🔹
این منبع افزود که وزیر خزانه‌داری آمریکا به تیم خود دستور داده است شرایط کشورهای منطقه را بررسی کرده و برآورد جامعی از هزینه‌های لازم برای جبران خسارت‌هایی که به ادعای واشنگتن از سوی ایران از زمان آغاز درگیری‌ها وارد شده، تهیه کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farsna/440302" target="_blank">📅 01:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440301">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a70d2b9884.mp4?token=qDVf784t7Mdcbca9OKcg7F4DEanLb9bf6EvYj0uKnmZUTRpsYENwRJJM1QzrDf9Unq7XkPoLCrHlSTAd4biFHmnrkeufA9hO5YOO9JvggqCcD0wRISWveB0WWkKIMt21qt8laOKLEu9wbBU1MDWYFY1VuTATSYNRjqLRllwQFtDasG0b2xNwp0C2Zsu6Sug787nfakFNUSh5uyRRMCRB1MmvsBF3otp0TuYd9KIV-tIAH9M0WT8wQFjxTaK9zID1zgSDY-KvG8D3PiFcPqf9EkwJnFGjNRCtO6lfns2qeUPP54Y_IQSMqMJG1NDfVRV2F3pMUnRFTzKv05beQsBj-ToO8Pz35b1r1yMyWmeU99kAaQ8qO3jLEuSO-V0ioVyfylj057WbVBi5Ptd9FOmhjHXgonVsPv0beUcnb7UwbAbZqx9qpq9mzFGrD9iAE96ZfkG--Paru5jM0BWle6ViJ7sx90mO9EhXAqQUnKGF9Xe7dAhq-HV-_TA9rm_xbrvnIOnQsj2BHcpfZUgY8bLts3Re2UmA43rgDP7lZFFrAcgsckl1mIASAI9pPoqIaH4Nru4PnrwJtxQrVFTkhyVOAzcYx58-NlTR_otMYmuvDO184i2GaewieElB29CZLk6NeY6zdrZm4SiOX1Gk401Z3SblfbZh1r40o2oAZMjXIBI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a70d2b9884.mp4?token=qDVf784t7Mdcbca9OKcg7F4DEanLb9bf6EvYj0uKnmZUTRpsYENwRJJM1QzrDf9Unq7XkPoLCrHlSTAd4biFHmnrkeufA9hO5YOO9JvggqCcD0wRISWveB0WWkKIMt21qt8laOKLEu9wbBU1MDWYFY1VuTATSYNRjqLRllwQFtDasG0b2xNwp0C2Zsu6Sug787nfakFNUSh5uyRRMCRB1MmvsBF3otp0TuYd9KIV-tIAH9M0WT8wQFjxTaK9zID1zgSDY-KvG8D3PiFcPqf9EkwJnFGjNRCtO6lfns2qeUPP54Y_IQSMqMJG1NDfVRV2F3pMUnRFTzKv05beQsBj-ToO8Pz35b1r1yMyWmeU99kAaQ8qO3jLEuSO-V0ioVyfylj057WbVBi5Ptd9FOmhjHXgonVsPv0beUcnb7UwbAbZqx9qpq9mzFGrD9iAE96ZfkG--Paru5jM0BWle6ViJ7sx90mO9EhXAqQUnKGF9Xe7dAhq-HV-_TA9rm_xbrvnIOnQsj2BHcpfZUgY8bLts3Re2UmA43rgDP7lZFFrAcgsckl1mIASAI9pPoqIaH4Nru4PnrwJtxQrVFTkhyVOAzcYx58-NlTR_otMYmuvDO184i2GaewieElB29CZLk6NeY6zdrZm4SiOX1Gk401Z3SblfbZh1r40o2oAZMjXIBI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
درخواست عجیب پسربچهٔ ۱۲ ساله از آتش‌نشان فداکار
@Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/440301" target="_blank">📅 01:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440300">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/445c9c889f.mp4?token=spC9lujZCaxAxdBAN6xToFIEI6dqxF0d1A8ak5QtyoBQs9KBU4eyRhFgQSTKLZVzEeGuO0Zgxx8B2m4MmbsNylH54r4tiazxBB_hIkYBV4-K4oYQ7jzVyNHkGpoIoT6JJXc9XeaZWbLSDbzQcIwDPdVgps0AZOqBFtnq0d1IjD015bU-5k-GnfeRDyb5AOKEjELedtlC1CoEpXrAaDC2r2RhQp-hlTEvD4xOcxalFMk3rRdKqO_34FA8mbYkXMRGLwvAXIkI9y5NtXHO9QfcE6jZe_crDBNjSf0vgELc52ljX5rRAX3gCb0CAyM7NNPDvB234SYO6UNSdLjh_Ux_KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/445c9c889f.mp4?token=spC9lujZCaxAxdBAN6xToFIEI6dqxF0d1A8ak5QtyoBQs9KBU4eyRhFgQSTKLZVzEeGuO0Zgxx8B2m4MmbsNylH54r4tiazxBB_hIkYBV4-K4oYQ7jzVyNHkGpoIoT6JJXc9XeaZWbLSDbzQcIwDPdVgps0AZOqBFtnq0d1IjD015bU-5k-GnfeRDyb5AOKEjELedtlC1CoEpXrAaDC2r2RhQp-hlTEvD4xOcxalFMk3rRdKqO_34FA8mbYkXMRGLwvAXIkI9y5NtXHO9QfcE6jZe_crDBNjSf0vgELc52ljX5rRAX3gCb0CAyM7NNPDvB234SYO6UNSdLjh_Ux_KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در بمباران چادرهای آوارگان غزه توسط صهیونیست‌ها تاکنون ۸ نفر شهید شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/440300" target="_blank">📅 00:36 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440299">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede6fa5c47.mp4?token=N9113SjJ6BinNazdAVuALcX2f48mes3jk48EEjQxj20F4aMsbOhWpYE4yde5SBy09A6fAlKOnfNBeUNE1Cyic0M2kyf4RUGdQ5i-9mtRhzRRc-Y9w55rx8tjf5Y0ecsDqO33WluWFbbMF4rp7HUaybHuUE8dZsDxmxEoS6Fjmh5LFsGpdwv6NVXLcFxS6o5vi8a8x4c2r-gon7WYKz2vbQcdQTyaJJS4TAk3v8my8SSmAEZyoi4A-MOD2vGRa1kTHlTp24dIfSV13oUGGsYe2sW_MZsnHUhlsXU-BNEaD7nAKmtyGvKGmtdCMGXS3wLIHRBygWKHVHdAm-eAueVzTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede6fa5c47.mp4?token=N9113SjJ6BinNazdAVuALcX2f48mes3jk48EEjQxj20F4aMsbOhWpYE4yde5SBy09A6fAlKOnfNBeUNE1Cyic0M2kyf4RUGdQ5i-9mtRhzRRc-Y9w55rx8tjf5Y0ecsDqO33WluWFbbMF4rp7HUaybHuUE8dZsDxmxEoS6Fjmh5LFsGpdwv6NVXLcFxS6o5vi8a8x4c2r-gon7WYKz2vbQcdQTyaJJS4TAk3v8my8SSmAEZyoi4A-MOD2vGRa1kTHlTp24dIfSV13oUGGsYe2sW_MZsnHUhlsXU-BNEaD7nAKmtyGvKGmtdCMGXS3wLIHRBygWKHVHdAm-eAueVzTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
وزیر کشور پاکستان به تهران آمد  @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/440299" target="_blank">📅 00:21 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440298">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🎥
مردم شاهرود در موج ۹۸: فرمانده بده فرمان، حکم آنچه تو فرمایی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/440298" target="_blank">📅 00:17 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440297">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38eb300b3.mp4?token=OJu55pxBJ0AJuZhYtds6VtmZL6E-PVCIPor94JYRzgPAZsl9wxeOBiQp2ywcRdXQd_f__5ta1ksLxlwNg27gQ4zhLviCA3ta2KFI7qQslmqkBV2uR2_80cLm2bVuW-kkkSk6rc-C3OmXK-ZR00W2Z9M8gVjHzMZIfAtlQLz7oGrA70RKdeAbynTbUE-nBpOmjHA8xh6cwJu7o4gZHVIDTCsycEND8z2CanyIfRDQtlw3oNnTZf7MTvMO6Qe88lATvKpRj6Yfte8QI9yzr3_TMkG5UBGm3Z78nbGCurg2LfA4VS0JXdy6EYh4VVsrNbE8VXrRx0cBzWFywbI41u9jmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38eb300b3.mp4?token=OJu55pxBJ0AJuZhYtds6VtmZL6E-PVCIPor94JYRzgPAZsl9wxeOBiQp2ywcRdXQd_f__5ta1ksLxlwNg27gQ4zhLviCA3ta2KFI7qQslmqkBV2uR2_80cLm2bVuW-kkkSk6rc-C3OmXK-ZR00W2Z9M8gVjHzMZIfAtlQLz7oGrA70RKdeAbynTbUE-nBpOmjHA8xh6cwJu7o4gZHVIDTCsycEND8z2CanyIfRDQtlw3oNnTZf7MTvMO6Qe88lATvKpRj6Yfte8QI9yzr3_TMkG5UBGm3Z78nbGCurg2LfA4VS0JXdy6EYh4VVsrNbE8VXrRx0cBzWFywbI41u9jmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خون مقاومت همچنان در رگ‌های رفسنجان جاری‌ است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/440297" target="_blank">📅 23:49 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440296">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dca6844e6b.mp4?token=IbcYpb2esAhpoeboDnTeaoDfJWutUO_-ZRRCQv1MbAPHevOl7Ai9oMIqq_0ukE40Fx7gFoMXa8OWw53uIlyYn8Iufb6OvOdXu4TEBOAl7FGc9jMrV1FdccjX0KoEB0SrD2j-tIiv_iV3NQggJY9ywifOwwHaeXfOJoR7giBhmYQDcGkJ42C4DGRj6w0gaPM7g_7Uso5xRhQZmOBpLefU4c_Hda7G5AKbdMRvZnEInTYOlR67ta5B1IQVSCsePgMnzMnIpJCjkXnJgo14t4_WNplnIag_jdtD7vVv3yxWqJVANcqVxjwZ8SuBv8foU484dlYcmwQd4TK5qSKv_5x-Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dca6844e6b.mp4?token=IbcYpb2esAhpoeboDnTeaoDfJWutUO_-ZRRCQv1MbAPHevOl7Ai9oMIqq_0ukE40Fx7gFoMXa8OWw53uIlyYn8Iufb6OvOdXu4TEBOAl7FGc9jMrV1FdccjX0KoEB0SrD2j-tIiv_iV3NQggJY9ywifOwwHaeXfOJoR7giBhmYQDcGkJ42C4DGRj6w0gaPM7g_7Uso5xRhQZmOBpLefU4c_Hda7G5AKbdMRvZnEInTYOlR67ta5B1IQVSCsePgMnzMnIpJCjkXnJgo14t4_WNplnIag_jdtD7vVv3yxWqJVANcqVxjwZ8SuBv8foU484dlYcmwQd4TK5qSKv_5x-Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروش قلعه‌گنجی‌ها در نودوهشتمین اجتماع اقتدار
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/440296" target="_blank">📅 23:40 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440295">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pCUXAizNkOgVc4KlyaFvBHhbPFODuaw3gV0DftHnmRuW-gmHQFitCREMBuhIPZRfTMS520aRKfDTsPh1ZksYNlo1CqtW7loFmw7EvVCruL_wxqMfH-72GUmWcWoAfqrNoGZ459IRmqvR3VcoUrza575t7zKQTOFzdf1Be1r0gbbXfAE9ZLWyZP8pSDRusHOaWD15RgltvKBbVmnGenGA2WKYjMTdy0qapV14MvlBUMRUOANlDs-ogF_seAulSIoLWk3GgoF8eScbMcqz6q_KDvh1DISWPwxZfxkqFWCWuekU0bplnysz-e38_FSHC7HdJxvHvCA-PNuo5py1b89GRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چاه‌ها آب را از «پریشان» دزدیدند
🔹
تالاب پریشان، یکی از بزرگ‌ترین تالاب‌های آب شیرین ایران، امسال وارد شانزدهمین سال خشکی خود شد.
🔹
لاهیجان‌زاده، معاون سازمان حفاظت محیط‌زیست می‌گوید ۴۹۰ چاه غیرمجاز به‌همراه تعدادی چاه مجاز با برداشت بیش از ظرفیت اکولوژیک منطقه، از مهم‌ترین عوامل خشک‌شدن این تالاب هستند.
🔹
به‌گفته مسئولان، تا زمانی که وضعیت این چاه‌ها تعیین‌تکلیف نشود، احیای تالاب پریشان امکان‌پذیر نخواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/440295" target="_blank">📅 23:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440293">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN72QyN40YVMee7tEXO_p_IUHnJnMG_E31PwWku2FZ7dkW4r2yFjMnaTjTZskYAgrP81UKiLxdx1LWsezsbPo8TN6W1XtpKVw1_vrDT5k_5ZZuvrwuNi8Q2h8KOtPYzbw0hoY7FOg3YVmzkdFN3uppYN8SlmchnCDRKEjG42EtMQmzBVqh3xMx2kmiJnEWd6k-AAfEjkRj5Pcqdorg-WJUzPa22I1rMA_DiB0qS7av3U1yu6XwCoEwK-LoXOtJoy7hifOrKq7G8Q35RcqA4uAsyECn2bITcUikgr5RZ7SbjHnpU35HObPPqrv7k3clfJnDxZs3sHjC_oL1Y37TinIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده صهیونیست: جنوب لبنان باید اشغال شود
🔹
فرمانده جبهه شمالی ارتش رژیم صهیونیستی خط بطلانی بر مذاکرات لبنان و رژیم صهیونیستی کشید و خواستار اشغال جنوب این کشور شد.
🔹
او گفته که خلع سلاح حزب‌الله بدون کنترل و اشغال جنوب لبنان امکان‌پذیر نیست.
🔸
در راستای اجرای همین سیاست، ارتش صهیونیستی ساعاتی پیش دستور تخلیه فوری ۵ شهرک و روستا در جنوب لبنان را صادر کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/440293" target="_blank">📅 23:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-440292">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cB5EeQLb1ztYx3LaKNZKQdBCjs5wqgLgxn_IAf6uWi0l0a58e9aABRzhuAcY_86v3zM7uXkmWO0d5U1lWq6dK0ZmKykmMjd5g8sHfYXZ2nu8UNjDDF1CmZ1B_YL2Mz-_pw5XgCql_GhPPy5bT2lWeneFjU_KtwP8qyZs2PsW8aRUk92c2m_8r7u-BA3nlOczXHnVVP5IIdDNY1iix4ea-mWnxHq26azCZq2hu05V3QHcgCny9Ht4wL0WDLS9ca_aatC65DuOvMa4VSXzkJNfQ3wMgeoyTuELHvfMX_c4BgpFfMQR0mKaJx43y5A01oHQ9bTD-wj75sxWP3UsVWoSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا عکاس تیم ملی عراق را دیپورت کرد
🔹
طلال صلاح، عکاس تیم ملی عراق پس از ورود این کاروان به آمریکا برای جام جهانی، ۱۳ ساعت در بازداشت بود و در نهایت به بغداد دیپورت شد.
@Sportfars</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/440292" target="_blank">📅 22:38 · 16 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
