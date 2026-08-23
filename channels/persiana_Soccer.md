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
<img src="https://cdn4.telesco.pe/file/HlVACjRpQNce5LZrKAbtuhmVlQr4bU5kL1_u3beGGr8dZK_WLfQh8bfr75flo-aofB5fWvDj_jAIyGUC4OHjWh1namIO6kbbOOmmNe8G3aa9Qtr2CyLoUbBu5zb26o47QIw6zeIgyiZfw_M9Y0aeiVmBMGFc7U71_jTIxI59FDqdlaNOwx0v_ZrzH-C6j_aU2jOTwLlZGQ2QTJb3W9zFm2fehpsyDwSDrr_0XPOQqwOsZTSr2QYoIPp3xBlW9buD8lbMV99jF1XEUABndeBLdrwlpXPQIMJaAvViZbrNy3os4xcofH6o-rrNJfvmyGyMLgksK08n9rRzZAto8aHuuQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 614K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 19:13:37</div>
<hr>

<div class="tg-post" id="msg-28324">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTjgP0nXbefQNWmaNXyX_g53OHPjbGf4Z2XAuw31zAVtDZXFMUyAL8qWKllPTlvq8Xs1-6izpYuW2b6MwwwGKXDmVx1sbzeyxtCFoh_qbSkNokPwFrtrEZtHg6uWx_nujkecvEf4q-CRUjD_2xOL7Rcde1_GiONNfJqfQCsPDt8W0Qk928fppvu8VxNH4d3aL7XkR72MtYvMPwXJ-t5YTNsgagFB5mxACaa8TJOPmCsjrNeHDRQPPbuNbaSL2msmzPaHe4OVTu4bABEta7-sb_E2o7qvH1OPuqJirnl7Iug5e2HPovukMI7qK9BUt7JSZvxXtzMiGrXLWoZcQKcsyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
10ستاره‌تیم‌منچسترسیتی که همگی بعد از جدایی پپ گواردیولا از جمع سیتیزن‌ها جدا شدند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/persiana_Soccer/28324" target="_blank">📅 19:01 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28323">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgVls_xQsRgQS5GeHRNhL9fN9aMTBaIpzHwko-4xtZNDkQ_FnlwW3idMLaSxtya-uFnhs3ULaJmzkYCMWw3wqvgaI0_dvtrwVh5ytVLe1-gWh8jI5hGnsDI6SUdGzAFslqzftAbrvroFaQRX4WA0hWDeyADcCOjRPxIXXEN4ODXNf5euF2_3MVfQqqzoBvdGEBP60g1Gf20LdsirSIVMzqYXgvsO1NnMp58UsaJRk7QfUtfh8PGB5rZUD3RHvFd2QT6N1O-BiE5kcanUBDOmg41P3RC97YyWuMCnLOVB-_YuDx0WxCQ-_B-ewB_ZRpauTa-KoO-N90ereK_IhT023Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/persiana_Soccer/28323" target="_blank">📅 18:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28322">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U299K_PZBSWCNCVbd69isOnXFBmGWzuHanCU0OMiQc_ZhpLRn1Izk6pBuJd1W_thH2uDwL_qLM9JlfSUWeEF6A3MC50tcp9_yjyKDT_TbuL7yx5Q0lGmALgiuC4CudZd0nlg7VwLDDCFRexSVCN7wNHtCmPINrgpDhYbKfzZUsKEm8soHHXUJya7ksnTl55fJGWJGQxIdSky_lWwctmOHVp6gUUEI9JmX5Acl9TR4v3G5H_NY5YozgEbZIToO_85v4x3Ceq6Ks_rqCnklybChVXKegEeEReRXGs6vVWtXl7odl9f81-1Ic0nIS4A4LkgGi5pHwCmTG7dQ3a9TlG8uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
شماتیک ترکیب رسمی استقلال برای دیدار امشب مقابل تیم سپاهان اصفهان در هفته سوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/28322" target="_blank">📅 18:44 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28321">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qppc-m5_1VBjMpJK2P0rrvnqd816xROAJ6Z7r8ckFvEPfbSdxV3JusIX9efIJQvKmssN7iWZhxqfsbxqYPuTWpCrBUNmTJZlutavPmCJn7kqm5fp845LIN8VmWONY1gsvLQ4_7d0-LLyAi_4shp3CMnCGouGJ00z3RN7zxFmjrLQRFvkEcszhuAEhTdjhqmiNYq7JqQjBkd4m25oPoZaFkxAJmMfvmPpwtwwkmmeRqlHlFJHoi8Y5636hgatgvAW1DcUTZ3UFeb6gaTfSgFdzCFedcgqPD_6N08VIkUXibTOvbiH0jyNvhbJIYXoVhr16Q9-U451JZyVOaMEe6JOvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته سوم لیگ برتر؛ ترکیب استقلال برای دیدار مقابل سپاهان اصفهان؛ ساعت 19:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/28321" target="_blank">📅 18:33 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28320">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdVAuig3X--6KeFBKdnIiZg2cqPJRwt8OSfkNFvh6BTs50rOLYcKGP_v6qwkZDRpazsCiKw-5MJagoAk6GelAop6xZJ7zopDDmwAAm6_hvCx9-O6TZM59iBMnyf5hA4QuQn2_BGuiw2lo6D_BecnOJmrjLxuqeY7BVuRnkgG6kyn5mIm4-4QN7H0O_ZPZutTyOyY0WVoIj3SxXA7JB6LG-mWH02o5ogv7NFYaRQxFPdbZ-dEM0L6iDe9WTBC6qM2vSgog42ZhFiI3uSWZdEnZZ_6PfTubGUthKlclc9Fmxu9JNN_3jL7APgnUCkWzSA3hGUFjjgW7PyCqF3tITc68A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/28320" target="_blank">📅 18:32 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28319">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1FyfxfX2MsqNKXTHFmAJYY1B4R9sTjakbNfeR_q0Q8LLdF5XU3dLEwAOJhCFiRJMOczD62rx-Eo8gY_WsNK7vf3Yq75uaIoJCLIU0ztySoqMrNH_dPQRKugWyVrxSpFSrMaM5g_UrRM4wcHVzAz3Ai4hBRZIbwfCN0xuGfOXG5N4RvVD9lFQec-HfA3ItSJtJgL_lks2NG_ZQ_7Zn7uJaCXcwpKs6zv0ef1HjwB5nGKCmJtxKCFHDhu7brKt4nbwhyv3faXd-5KcMDyyDD-ZBtcKSirSJ2aWQqzVWRQXJO3iSBOLh824AF_UA4Oqn_-t97YkC7rfGLhs3bj-piHoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌‌ها؛ مجید حسینی مدافع تیم ملی آمادگی‌اش را برای بازگشت به استقلال اعلام کرده و درصورت موافق بختیاری زاده با او قرارداد میبندند. حسینی از نیم فصل میتونه برای آبی‌ها بازی کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/28319" target="_blank">📅 18:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28318">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NOdrXF9wqEAtx6YljMaaWK0sGJkoxGKHm-Ava_M7J8REdUZF05idBES1uLtieIFdratJf0jtyfJevXOHNYpUvSRfMALs2t5Kz-1W48U5l4MqRBktVgH09LvnLEpRLC1iZejgIRmpKgTz95Zg2RLt7UAqDdridhOUvGU3DlKV4mfiaK8iBwcc7dNcqvQuln8Hu8tPsL4VWapEsqYskinz3NGNL2vJgjWBwAB5xbSbKRqlqJibeTbp-7mPb2WXu5A8bXLqRnNsrR5xpRqAG5-DtyLYkwTihxUAUtHowCIen6mro-rbaMphnhjiI0XLf3yi7Y45M0aHdEW51zhGjFj7kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/28318" target="_blank">📅 17:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28317">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=edF_EFbF-dcp2cHplY-pABHFhjXPh_vdUiF4IfXfWTdeqXy5SPqif1KKVLZhFB5GoLKTOywIkzVAejIJ3fD3z5A9n1nEpLok8IFkC4XJIZJigW0cRD3G8I3D8UxIuzsxOUjnA17qmkmJWOspT-4EZHR5FQ8mYkK79mb3sA-ycu7Uyh3Q49WfMcdtx8tHt0rPH77oZR3cqXkcOoke6Qg4e5Lx9iVvEfq-0tekLa2WmknHhFhEXC6IkeJuyMD9rBvDgR_znu_8e3XVMoPsf9VnOq-PXeyl0ofsLpk59qTClYQJRZ3qTUiHupSJvrwXsFn9TV-HaL7L_NXhmkfNr2HxVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3040660e7.mp4?token=edF_EFbF-dcp2cHplY-pABHFhjXPh_vdUiF4IfXfWTdeqXy5SPqif1KKVLZhFB5GoLKTOywIkzVAejIJ3fD3z5A9n1nEpLok8IFkC4XJIZJigW0cRD3G8I3D8UxIuzsxOUjnA17qmkmJWOspT-4EZHR5FQ8mYkK79mb3sA-ycu7Uyh3Q49WfMcdtx8tHt0rPH77oZR3cqXkcOoke6Qg4e5Lx9iVvEfq-0tekLa2WmknHhFhEXC6IkeJuyMD9rBvDgR_znu_8e3XVMoPsf9VnOq-PXeyl0ofsLpk59qTClYQJRZ3qTUiHupSJvrwXsFn9TV-HaL7L_NXhmkfNr2HxVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/28317" target="_blank">📅 17:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28315">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5-yU-FZmHu1AjnDA5a6XesERKeBXzOv5BKdFo90pD0vJq9jQ9f2qChQaHU9p3kwssRzS0IhYmLF-fKl9DvTeMySO5kmJduE6KH2ReXGT4dQ9S2fZEW_h_02VMvUcR2l3AQnxBZZZ8bydq2WjXm7oVCqWjk8SxpEVWSEgMoRbAO9PHd1QGXJPrQgV4FkR0RJi7re5Q5zR0qlaQ3mNPWSzNKx_PIEJNROZCH42m64Q4w_kQBpjIDVU6sPVH495vHPMhKK8BSgkGtSAYcQuhvI1Tc-5xqpuij4iZr40r1jSsA_ra9Q9PMTOdCSHg5EQF8HJX3i0sNtHehlLOl2WKhHtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=QDDBw1zmvTjvp7ZmQ6WUqMdeMePm2NdIj2tnHGCwvSkI6wfcV9P2WF7ZfL24Oe12ba6dI7YtQaJIBGBCxcqp5dBXzskmC4vV8mDGI2dyuALl5N97AgberrOGsMUHseAbZpGpOpmKvsMKwkO0xvKFWbKKECTB4JgP1kx6VNjj-lXgv5rANr-OJimkhsKPcEnOIjNrK97d_xLXi9-6tehbIyV3ighCla4CJBBlUbSkm8CqCFsSRmBGlr3Gcs1Uld3Avip_TyjXMgRSQvXmePdLzGUudvajY5CJ8gN_mOdN3xcZj9Z7Ncji27CTaoqyswdbbr39eccMVsQuJ_6vzGUoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f8039bd8.mp4?token=QDDBw1zmvTjvp7ZmQ6WUqMdeMePm2NdIj2tnHGCwvSkI6wfcV9P2WF7ZfL24Oe12ba6dI7YtQaJIBGBCxcqp5dBXzskmC4vV8mDGI2dyuALl5N97AgberrOGsMUHseAbZpGpOpmKvsMKwkO0xvKFWbKKECTB4JgP1kx6VNjj-lXgv5rANr-OJimkhsKPcEnOIjNrK97d_xLXi9-6tehbIyV3ighCla4CJBBlUbSkm8CqCFsSRmBGlr3Gcs1Uld3Avip_TyjXMgRSQvXmePdLzGUudvajY5CJ8gN_mOdN3xcZj9Z7Ncji27CTaoqyswdbbr39eccMVsQuJ_6vzGUoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/28315" target="_blank">📅 17:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28314">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmh34n7gMTUNBhD6Ekolz7SJREj1Bb4MWRA8oKbghv7bkAqeUmbSiilBSNTyazHNmF602vMPnq9xISf3V2QzCqLFATsZhL2bIOaxSQ824baZ9WLesYNbUOgvxVY74aJU_C295sLtCaP_zZV66wgtQnWQd8vxLTwVe7RHSAzhv7WZ0kBWJB5meZKXZ_xjnXRvhhDcipWFvReHVTeKZrBGF5p_ftFudkqOl-AuvqjclkUi-KES5tkasOPtbYKj_fRcQPwg3ph_EHjhTStzL4C5UKw4my7N19uLCQifcHGXMhSrd6khTrLNtT5yxdzPpnwNHY4smJcbA4W3xRgfU8ZOxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمد عمری ستاره 25 ساله تیم پرسپولیس دچار مصدومیت جزئی شده و ممکنه کادرفنی به او استراحت‌بده و دربازی‌حساس‌باتراکتور غایب باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/28314" target="_blank">📅 16:43 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28313">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00386372ad.mp4?token=paYqQucyTQQyg5XXONnXIF1l6BpEEzZnDvc-mOuAoHtAUmu6lJ_pMvrHeVAKDa4ZFNZjdz-JqLhJKkDxIqANU_63OljBsenZxuXm3Wb1tth01qlvM1SpPbsxI8cEur-LxZ4Mcr_ctZtX5AlkjnllN5IqQ2lYf5tEflrqwl7BIDNJPUZRsJsfk4gUfdeu7q8eZBHr57vAs-wLQ3ZxLBTyhrn8wfRF8PtTpNSeqRSacTey_0pbkuvlQU9xwlyCYbrUnj9hAQg4B-OinlPZbIACbAwWHStimIQ8DW6kXTFaJdsZk2b3HhbuiKL90BvfU3OZPeTuFGt7LeFSUUfNBlJ3WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00386372ad.mp4?token=paYqQucyTQQyg5XXONnXIF1l6BpEEzZnDvc-mOuAoHtAUmu6lJ_pMvrHeVAKDa4ZFNZjdz-JqLhJKkDxIqANU_63OljBsenZxuXm3Wb1tth01qlvM1SpPbsxI8cEur-LxZ4Mcr_ctZtX5AlkjnllN5IqQ2lYf5tEflrqwl7BIDNJPUZRsJsfk4gUfdeu7q8eZBHr57vAs-wLQ3ZxLBTyhrn8wfRF8PtTpNSeqRSacTey_0pbkuvlQU9xwlyCYbrUnj9hAQg4B-OinlPZbIACbAwWHStimIQ8DW6kXTFaJdsZk2b3HhbuiKL90BvfU3OZPeTuFGt7LeFSUUfNBlJ3WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
🇳🇴
واکنش‌جالب پپ گواردیولا به مدل موی جدید ارلینگ هالند؛ هالند دهن سرویس بعد از اینکه بازکات کرده اولین نفر با پپ ویدیو کال گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/28313" target="_blank">📅 16:16 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28312">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jr5zZAgIQi9h9endlBlGtEHHbCu_KSCMP4VRFCZCKDafQMg37aXRVDX1XKXg8qd5wKJR_wuiNv9PRVclXjBuiINx6G2OS986jPmoBDc4Ppax7TcCCCPq_hWkdz1cedIyBWsZYp6Br6b1gb-EP-jwBJsz_3qL9vGLFQHKK96t0MWszZNhunMku7tKxxha43b1LYvcQlw_d6V2Sxp3G3zvBCm1UA7iuKiOcLOeKFxWNKeyT2is74o69F76Bj3XosyHEvUZDaijeXnU2KzZatETKD48UjgiB49DDw1_aRMlzoaudHSfVLPZuEvFcCKQUeMwBd42K4nUyMqbD3_KQoPp2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شماره‌لباس‌خریدهای جدید بارسا در فصل جدید مشخص شد: آنتونی گوردون شماره 17، کریم آدیمی شماره 14 و رودری هرناندر شماره 16؛ شماره 9 آبی اناری‌ها همچنان خالی نگه داشته شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/28312" target="_blank">📅 16:00 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28311">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnt7SWENw6FIfqB3M7NvuWOyJmtppTXjpilkL7YDX9KTaSsgVlEHF8AZWxQJxE-1Z_hCgMw1bJdOaEpxRdumnQ2b8_JYxdvBKTxLILjrkhoRKOskfl7e7aiXRJ7FhDeicZHZ-4FqnGwYDXVaryq41fGH5ziosNu-6-TJYZGFqRigl9iAZaqUuRVy4Cm_oX_nQu3kpQ4Lljj9UnfZ7iixAlfnCEGQ9I17wrDTC65zKUyd948DxX47V5yUNVtsszRvq3YQDkwv2lVUu7SFC-ki0EWiVYx2sSvBbvCNbJ9PmenMFam3dLl4nZdqhAXl0AqyAa5-M0o8YfgM4AVs1JMtUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
ازهواداران تیم شباب‌الاهلی امارات هستن که علاقه‌زیادی به سعید‌عزت‌اللهی هافبک ایرانی این تیم داره و با پیراهن عزت‌اللهی رفته استادیوم مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/28311" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28310">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lu1MCt1A694PY1rfme5B9qgmHo2-P3enRiAWD9sFiBNXY6kNlLKrYmq0Aqqj6oqS7ZzWc4BiMV15j8sdlPT4N5cb5p9TcvZZ95zNAHEZDkzpcz44s5H-7rN5Er0VsEcvs930DB4_5LDri5WAY4OHGVznJcqbU3TRMVAgU_s3UaLjjLHJi7YpDeUEuomGpfv1iMQ6WFlibXTDpUlliYFUdgekvdnp2LJ83yecqHhHtAgVIRkXgMHuYwWyMunt6b3jaJ99ESshFWZDrpTYltc9lLzM0McpRxPuguoxwkvR_fohxdNuUPMIfWgyz3fhTH-GLAKqZHnmOKt0e-TrP0ZeDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/28310" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28309">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ro69xx8LaufW3EAC94j3naMWEZWnNKytaF_1OIZ4BmXcYTXpXrxuWVSzduhP5l5HT0GNKSrcqgawDMJBYeWxSQBS6zRwbtsosMeiLFLxkfAo8XfVnSxXRxIlkWq2l69ZpWKwPs6YatFdBQnPBfjBq-7l4nY9wwKagqwCLEmInL10LywC5zoM1FWujdGECzVdGzoqBRa_5tKAybEAKmT8iwubvv_iuS5Fhv6cC6n9bBMVwxjBvlGdsnJqbQoSET-LE95XUFf0lSqeUkioL4yUQtpyhPa75Y5BCbufmPKFshRIJ1qB_fEREMWjxZ_azz8OKUcz73qKnTWYWm1kEmAXEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته سوم لیگ برتر ایران
🔵
استقلال
🆚
سپاهان
🟡
⏰
ساعت ۱۹:۳۰
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ ‌‌بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۱۰۰٪ بونوس رایگان اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/28309" target="_blank">📅 15:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28308">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=ae_8f52uG1jol0UaSVIsQRYbqsR3lQHvW6B0103M9J8lZkNrVA2yHtp2bmSTXb5_V8_KVscGaH08FJiib3dPKqzy3ehmqgwO-d_wllP9ujYvTMu_3Qt2DAgmTHFP9WyTVaANmTx-l1RQ1MqE9TM95PNMUiI1nKGw1KHFiDKrW4gXbQR506sVaRxbfEmZ6tEhO0LmcuHIKQb399FNKkyKq8o5xArRiAIKYiYs2nTYnYcCXEJGdT8o0IaxQVXoPs1YFljl1TsC9dfrhEDxD35cBnMuDQr0Xu9d6l2DUoF7NlMygzXcTzRoUopNhSzvbdKJ66N59fmpKsdQtnkD-dmq_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa9e980fe.mp4?token=ae_8f52uG1jol0UaSVIsQRYbqsR3lQHvW6B0103M9J8lZkNrVA2yHtp2bmSTXb5_V8_KVscGaH08FJiib3dPKqzy3ehmqgwO-d_wllP9ujYvTMu_3Qt2DAgmTHFP9WyTVaANmTx-l1RQ1MqE9TM95PNMUiI1nKGw1KHFiDKrW4gXbQR506sVaRxbfEmZ6tEhO0LmcuHIKQb399FNKkyKq8o5xArRiAIKYiYs2nTYnYcCXEJGdT8o0IaxQVXoPs1YFljl1TsC9dfrhEDxD35cBnMuDQr0Xu9d6l2DUoF7NlMygzXcTzRoUopNhSzvbdKJ66N59fmpKsdQtnkD-dmq_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترابزون‌اسپورقراره‌دستمزد ۱۷ میلیون یورویی به محمد صلاح توی این‌سن و سال بده. صلاح این سالها پیشنهادهای زیادی از سعودی داشت. الاتحاد تابستون ۲۰۲۳ بهش حقوق‌هفتگی عجیب و غریب ۲.۴۵ میلیون پوند پیشنهاد داده بود. سال‌گذشته هم یکی دو تا تیم عربستانی دیگه بهش مبالغ…</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/28308" target="_blank">📅 15:09 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28307">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMduFw8TSGw1cJp4FuatQjkIMA53Y1inTXjRRm1nan1up80ywCSBjRjvDnSomv0BsB9oPXQ2aFImb3IYmjdaPBMa6p0fx_m9fJq1f1a2Zr2bfhm8oOYmjopj3J1dzalltkHqw8J29v8stcIMJUjk9l1f4Ua81z4Hb31nmzVQRF_mQD9JS89ykMkoiOP9TPjAfNnl765Mlp8-QAL5o0L1wT4gZNM5mq9wm0eG3RLuA8BKtc-WPb6hV9rFqkRU6Xp5ykwT9tWfH3v9Tc0FxhtnR6uoY_b7A6dnIvPCYF1SK0Hq-yo4nvYsu0MKaV2L467JmVvwrdJzwEs31ssuFRa74g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی بعد از مدت‌ها موهاش رو کوتاه کرده و مدل بازکات زده. ویدیوش رو تو کانال دوم گذاشتیم میتونید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/28307" target="_blank">📅 14:52 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28306">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bbedbe559.mp4?token=Te5SZvXwEtxYbS5wtCITI1_QyehQU1e8iNEd43fhCR7ETFqGiU_Pui0zveDTK4KJB6zT6-ZZyd7oQWNjZz5amKXPU3rk6rWRb1YaRlsN8vfygauZeXyWoz4u9rVrLRmMJecRTzgBxJzrQMdgxrJ_vDDx4phF4TU798W4NKMvNeMafyyt7-9UUgQpB4Q6w5C_vhxXvmrgly82H8SDoH67JqISBnkjmNWFrBVLQc196RBKqOdCU5U2-vpc-RMmRo-urrLt9jtvfboxcHV1AwVtHqPs3F1Xx3f0dHYFBZ3naQQ34eIEuvMa_PqrMuY2u_hFRGvVUcPpxbtr0ZVfAOvTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bbedbe559.mp4?token=Te5SZvXwEtxYbS5wtCITI1_QyehQU1e8iNEd43fhCR7ETFqGiU_Pui0zveDTK4KJB6zT6-ZZyd7oQWNjZz5amKXPU3rk6rWRb1YaRlsN8vfygauZeXyWoz4u9rVrLRmMJecRTzgBxJzrQMdgxrJ_vDDx4phF4TU798W4NKMvNeMafyyt7-9UUgQpB4Q6w5C_vhxXvmrgly82H8SDoH67JqISBnkjmNWFrBVLQc196RBKqOdCU5U2-vpc-RMmRo-urrLt9jtvfboxcHV1AwVtHqPs3F1Xx3f0dHYFBZ3naQQ34eIEuvMa_PqrMuY2u_hFRGvVUcPpxbtr0ZVfAOvTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌سم‌رو از فصل جدید رقابت‌های لیگ عربستان ببینید؛ چهارتاشون به یک باره خوردند زمین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/28306" target="_blank">📅 14:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28305">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/powXykHs7Fs8jmvfNxd03tZIOdPynUmOz6JLj7cHXPcZTTDnTOy_JKYx_fjy2ZNMIzRupH3sWsJc5rzq9me_S3htf0h81g-hDMUz3CiR_oyGX9Yq7SWPb6Ey-1O8Q1Q6QM_mw5sMtlfP6ZT42MmnApV5O7CRcV_XMiQtraNZER6EGy6JVgYn4eDepRjkq8JdJ23YmBPJhM4l219ZR2eZCCpZrNydyV9EhSqp277h_MV3-DwDEBjC89Tvm5SAfavIuNrlYujjiFgLiDzw1u1QiQ7Rs6EtJ-q8ATii-jbzE4cpY0SnAf4CE8Ohq_TW9RcLLdOvoOeFB9EODrMK8o_pYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دلار به 200 هزار تومان ناقابل رسید؛ یعنی هر یه برگ دلار بی ارزش برابری میکنه با 200 هزار توما ما!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/28305" target="_blank">📅 14:05 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28304">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xy48jQdp5YAe1uwZtr801UpApzssTASmninC4PjfOgBPmFVMBnT0j71g8nN8ePeZMXk-g_CL-YaEWyXna14TLt-OJYPCuuUPJ385OL5pdi3ifHr6XyV56tXfa8xuB12zPw_bXgyT6PUJZJfVt1rChVJymbnEqmcF3wSLSfApllkXQvZuvnJQY-k9agMXMZ0nyoGlT8HKXaxr2kq-Eg9dbd7RRUEH9cu0eP1ZGnQIdUXPsFKR7xtd8Cr6lPG68rZGnbPzFFURHEOh3Y7g_xiuoyVZA-lgasfzgzhlvQQY7-eLT7icJrZzJ_ooydAw9K4Wd0Bz3UFVhKtmypsa_Dha_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارلینگ‌هالند مهاجم نروژی منچسترسیتی موهای آیکونیکش رو اصلاح‌ کرد؛ الان خوبه یا قبلش؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/28304" target="_blank">📅 13:30 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28303">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBEJN3tB-uJl4Q3rU2mDRGwBAXqupXKP3sBgC7bJsHocJbFyP8XaN_k4W1FXFNdNPZ6UaYNM7KxJhLhez1rwX3lopbJEWsPr3-g4-PK0rvDRpHKJ6R1jRlI-Olm9_nU0Ji6AttXNdaWCX-XvA4gMfuuFYIaCeeNUuIa1snNM0Re4_rFbAVU_bD_W4tLZ_NfYmhH9Gow2qLlRFK_fBMEq6U43GldBsmVUIbNBS3ifFcATUHXcvrQoMYetQpoRgiMHxnxIo5g3AJTS6CbWHWRBJRtvqwY55JXIEU3b_FG_-doPnWg4Sw8OdUUd4-Xu44G0Zgux1Fr1HkUkAy1j88lIJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
#تکمیلی؛خبرنگاراماراتی در ادامه خبرش هم گفته مقصدبعدی محمدقربانی یکی‌از دوتیم تراکتور و پرسپولیسه و سران الوحده با هر دو تیم ایرانی برای فروش محمد قربانی در حال انجام مذاکرات هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/28303" target="_blank">📅 13:24 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28302">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=qp9gbTMsGumObmsh64S542MlPWnaI-5-0CLWoSKl77W9J17O5niBKRoYiIXOdMYQfR1tF4PETpNd64mZEYy7cYMRzGsPBRfSjxfx3TiHKLpECmNIG06GsxUCNpiu574U0aIkKaGLhhbPXCjt9WVtQ3m0WyRxWkney-diNsM1aHjiDUCdCgsVGd55uRZKiP3bg-Rfd6y6l1v5e8VUqIg6H56TPrhL-9WVIMv1lARfbBKDbrLo23tOZR_zkrJIhF9b82npU6qqhbuS0S07nMcRAYMCGrjT4mWKyt6P6CNIJNX6r7ceS_8n4liLyIEtBi8HBFAzaDknwSkXoen0rR8cmzQy5txK7c-6OVUSwnqFKHv4vWoC3sxfGrA8FGFNnfRewtDmImxstwypfPKL4lEtYebVHJmFNpUQ6MrEsYwd03YKWmbNm4-D8xdC82e0JwAXzNSqkuoSFxLaPtQLr1KMInnr1wbHN-RoYSZnAw19TVYZcpIhqsB6bldhUIq4J9AFxtXAx73E0JJyzfCEABVYZT9ZhOJaj-GSRf7U-Q5grtbqLjNtgiZkWucH4K3Kb2ch76UGs2j3kE2kqbR5Cw9r5lqhasmk-rXngUzPt2UMpvh1bbLhJQFsnlY7TPN3onCr7ZPsy-AdoCs7I7vEvN4dewi5HuQWvto2zKAbRg-0B2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf8c217136.mp4?token=qp9gbTMsGumObmsh64S542MlPWnaI-5-0CLWoSKl77W9J17O5niBKRoYiIXOdMYQfR1tF4PETpNd64mZEYy7cYMRzGsPBRfSjxfx3TiHKLpECmNIG06GsxUCNpiu574U0aIkKaGLhhbPXCjt9WVtQ3m0WyRxWkney-diNsM1aHjiDUCdCgsVGd55uRZKiP3bg-Rfd6y6l1v5e8VUqIg6H56TPrhL-9WVIMv1lARfbBKDbrLo23tOZR_zkrJIhF9b82npU6qqhbuS0S07nMcRAYMCGrjT4mWKyt6P6CNIJNX6r7ceS_8n4liLyIEtBi8HBFAzaDknwSkXoen0rR8cmzQy5txK7c-6OVUSwnqFKHv4vWoC3sxfGrA8FGFNnfRewtDmImxstwypfPKL4lEtYebVHJmFNpUQ6MrEsYwd03YKWmbNm4-D8xdC82e0JwAXzNSqkuoSFxLaPtQLr1KMInnr1wbHN-RoYSZnAw19TVYZcpIhqsB6bldhUIq4J9AFxtXAx73E0JJyzfCEABVYZT9ZhOJaj-GSRf7U-Q5grtbqLjNtgiZkWucH4K3Kb2ch76UGs2j3kE2kqbR5Cw9r5lqhasmk-rXngUzPt2UMpvh1bbLhJQFsnlY7TPN3onCr7ZPsy-AdoCs7I7vEvN4dewi5HuQWvto2zKAbRg-0B2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
به‌بهانه‌دیدار امشب‌دوتیم استقلال - سپاهان یادی کنیم از تقابل فوق‌العاده جذاب این دو تیم در شهریور ماه 89 که هفت گل تماشایی در برداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/28302" target="_blank">📅 12:50 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28301">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=jfIWPkl-5oUZiG-bKvCTGNCIqFExmcht_ugAl8YclhXFiLE3VizaHXO7hN6ZDXvDBlgBWVFMiLmAaWn8qG9RY4xfNKS6PWN-oa1wKVnmu31ePWH8i-hD-bGAbv77E_0KddEMEBqCIkpFMQs9qpuNMtWiVU2QlFTzUxK-r2M5UuYQDqFJ3PaHArnINHMYf0fcmLtDxzusuzTtIKY7F4Deo2F6yoPfQu-0W6geSHTDR2gM10JC0vKCPT8n46owqi4hy__ldJkKdu3feWY89yeaRJJ5q-BKUsH4W1NEYVaJXRJodPjuHJOzFfdL5wUalvdyWuQtBT2eH1BxZaBgAyaf9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dfe668338.mp4?token=jfIWPkl-5oUZiG-bKvCTGNCIqFExmcht_ugAl8YclhXFiLE3VizaHXO7hN6ZDXvDBlgBWVFMiLmAaWn8qG9RY4xfNKS6PWN-oa1wKVnmu31ePWH8i-hD-bGAbv77E_0KddEMEBqCIkpFMQs9qpuNMtWiVU2QlFTzUxK-r2M5UuYQDqFJ3PaHArnINHMYf0fcmLtDxzusuzTtIKY7F4Deo2F6yoPfQu-0W6geSHTDR2gM10JC0vKCPT8n46owqi4hy__ldJkKdu3feWY89yeaRJJ5q-BKUsH4W1NEYVaJXRJodPjuHJOzFfdL5wUalvdyWuQtBT2eH1BxZaBgAyaf9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته اول لالیگا|برد سخت و نفس گیر شاگردان مورینیو در ایستگاه نخست با گلزنی کارلوس اسپی.
🟠
اسپانیول
1️⃣
-
2️⃣
رئال مادرید
⚪️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/28301" target="_blank">📅 12:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28300">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3pY4HGKUcJ2iszyfi_kULpp4uUk0o631-XM2vUcPnHiG18wvTJuwydN7gKXt0ttMBVorsiQykgv3d1bd7i6Fcd3ltZGDyBp6fTn7sqbhAa-sPVGI37EM_c_mAgZvZQRVm0_Oe0CW2MS3lAM1hxkySgPfTB7wLRP8tcZbk84_UFbSAeK8tSRKXjlcWoylajqJNKz1grv7TocLZgZIdLlzTJ9EEQVu55lP55WOY4t9-i_blGENjY5w64cR5aKvgl5ITJUhTRIpml3g99JEVdTbwf8Mo1fnAEkCZjD8LaUVbBi7Xkfyelt8VHJo5t0EnvhS0TghQJPZIyG5bASCPnRmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام باشگاه پرسپولیس کوروش اژدها کش پدیده 19 ساله فصل گذشته آلومینیوم با عقد قراردادی پنج ساله به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/28300" target="_blank">📅 12:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28299">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGogk1Z_HmB1Rk9pQxSrgqpbsR3x7cq8fW1ZycD03oIWc8quK_TmSmeryB3yBP0xRHy7q_eiNlVckg0ov-Z6KBDbh0xMEB1BshnXt31q2o_5DvNR9NPLEPqxo2PP1U94nLWxxvjS1UxytJRFAU6il1QHGFO69yVgxWPK2KEzIdBbqg41WL3VDr2TdfQ7XCUchrsO0XHspJMdR3BAzqyk1o72tk6hq-1ev-FFD5HmUr1ePYrLk5A9DEKto9kOue4ybJ7LmDXn1IMjsfNr-7DyWIHhfTLYscZejDotuk98guOgfb1eQ93GDaZv34Or_iEtv7wDv_nxKPMeDrD7EAbdvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
داداشی‌های‌فوتبال ایران؟! پوستر دو باشگاه استقلال و سپاهان برای بازی‌حساس فردا شب دو تیم که شبیه به هم طراحی و منتشر شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/28299" target="_blank">📅 11:23 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28298">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RBAqx9EscWZhDEVr1oHI4sfKrgcrkdxXRMhZR76K6J_OzUJYknIonb2ahyMjFMtw9u4TzbRkAjlXDJByIQVWQvKwdmoQZC7wbDqnQt5Oth0SWM3uhBo6dGsTEEp0anzzTI-p0Cbn3OMPhgYwVv8Cp_g0RdO6WbLg_cbDafbmbNeNpznNQ2etUzH0S_LNJV9-0GOsklQ8JKC8vmxiBhV5vEn_7tfHYoNrKpPofiOjTYJHgU-qV5Xr3WIV9oso8fPOdsV7jnGSDjQnfvj7vyouwfzIdmTuCepW3DOI0J9lSzq5D4nU-va1WVmgvEUFchMt4sSQSjKGoe9fls2P6WSrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه‌تقابل‌های دوتیم سپاهان
🆚
استقلال!
‼️
این دو تیم تا امروز ۸۴ تقابل رسمی داشته‌اند که سهم سپاهان ۳۲ برد و سهم استقلال ۳۲ برد بوده. ۲۰ دیدار از تقابل‌ های این دو تیم نیز با تساوی به پایان رسیده است. درتقابل‌های لیگ برتری سپاهان ۱۷ برد و استقلال ۱۸ برد…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28298" target="_blank">📅 11:19 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28297">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2XLQ9HZo731IoFKhg2587QtKpLlBnM1s33ygpCZWu2LkTGy2HwPrSUc1bqiq7X7vYqcJnoIXE3qujE9_UNVSuc74b0j9JuKfsxpltYCtUXvasFHdFe36vPCf-SCRdPj4qa00MxXdiPJkNJuaVKM-iulOOwKGlAol2C2NosPlrsjvGltTEimEiZs-k_FNPEFPatRcljnNIk1N4LvjQJ9rRjfaQTQs7VXbtNM3gvho-QPCndYJN1gUyo0mMvZEiiMXnFl5ehD5y65qSKsrXa2icE6Idl-n-Ph0Uon6Oo4ApxTHQxqhy4qXfv7pJK5cV1BZdCbk3Wc-fMAIxNkEPnwyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28297" target="_blank">📅 10:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28296">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7MlxUbEDATZs4nITfRBiSt1yfKoi0MkmaOBh7pVBGfLg2ZrEu34Y4qOeTksp1IYITX63lIweo6LzHHRAG7f-HpGdolAoWzIhDVFhXJtzGL-efYBkBMIIoQwaMABrnf8s29AZlRo7TKpnfpnpf0hg5y9KdhCalJr4kPZMD_DgpAZ6OV14RC4ttCOOyn67nZlSWiKhsHi7W-YB16DPqGs9vZRK0BIo0kkc1MVZk8PltSJZPqp0xp1jIXSJWwZSbYzHZ6YjWxRbXd_iYlRPKlvHHp3aU8q4XWiiNP28S8MtYM5mWnz9BQ9MU6-V_FOH_EooJUuLSA82MeHDz4cEYS5HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28296" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28295">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNyR_58ocjI5jwdJBQU1bKSSjkPVS8O6qZVmrbDJcE6eBBPtxKc5UtRqBb460X3bysubkV0Y5lhKwTLrT44C6ldgAcgkG5xmwgaUZMsSp1tTGuerd63xmeoLywtrdo1y7Lpm5sJodfRPn9JHBA4NZe8BHLrFNzamjshy1fXtL8xO7QqummLy6UuE20eoWX4nXB8VD5Pf7FCAUGCvnBnC4jnWa5dkY7Ks1CVP_Gu5EdvwNTjZzigsINjNvWQNDVoTgXpAivqzyonUGTuFHnYC-KA7XJMJku0vmFukEDrWf6sWYPMbvn9PnbyqFukrK0gjshT2k9uE1aHOjBCsuSyoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
در سال ۲۰۲۳ بود که لیونل مسی از یک رستوران درمیامی ۸ پیتزاسفارش‌داد. صاحب رستوران خودش سفارش را برای مسی برد و از روی احترام به کاپیتان تیم ملی آرژانتین، حاضر نشد هزینه‌ای از او دریافت کند.  اما ماجرا پیتزا فروشی همین‌جا تمام نشد!
‼️
چند ساعت بعد مسی یک اسـتوری از پیتزا با نام رستوران دراینستا منتشر کرد و همین استوری، باعث شد، به یک‌باره‌افرادزیادی به سمت پیـج پیتزا فروشی هجوم بیاورند. تعداد فالورهای‌رستوران‌که‌حدود شش هزار نفر بود، در مدت کوتاهی به بیش از ۱۰۰ هزار نفر رسید و این‌پیتزافروشی خیلی‌زود برسر زبان‌ها افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/28295" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28294">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDOULZSo5i5qRfPNq9a7pea5vcAe7KZKr2K_ykll7EVzo2w7-ff4xVpOVJCRoRRcTo_8hgtfyKvA6UnuofjVATh8RFcxwxv48mqo6tUIQAZ6gBA3Q2WpmyiwiFYgtbu0E2kda9-13P4aLVkl5fHSPs9n9RI1QQu_rMjtqF5h5XfFFLubODilRy3xLVRO5l_psGcrybE4wlTTIIZ3_TEyiQgFfbT04KmRYqJdEGcuUcHVpBDpDHYDlDsdHPByNqKIFYNwl0X1LfcuVHiRuqpQ9xGmxBKlYUu673k_cemxUpjzFYmIazn8XHI0OnYwkvhsk8RXqrgEk4hbu7jnq3RQ1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
بدنیای پیش‌بینی فوتبال و کازینو با LINEBET خوش آمدید
؛
سایت بین‌المللی و معتبر LINEBET
⚽️
پیش‌بینی فوتبال
🎰
کازینو آنلاین
💳
واریز و برداشت ریالی
🎁
بونوس 100٪ اولین واریز
🎁
بونوس 100٪ هر دوشنبه
📞
پشتیبانی فارسی فعال
🎁
کد هدیه ثبت‌نام: L5670
🔗
دانلود اپلیکیشن اندروید
👉
🔗
لینک سایت
👉
✉️
https://t.me/+dukgrB6-zGsyNGM8
🌐
برای ورود به سایت از IP کشورهای آسیایی یا کانادا استفاده کنید.
🇹🇷
🇨🇦
🇮🇳
📚
آموزش کامل سایت
👉</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/28294" target="_blank">📅 10:31 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28292">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=q-5rbmS1I4MwBTNrPhEKHz8kBhVkwWISZtg71IaN3B_5yxpc-HJWfQ9CadAK37bp9M4MZUhyPexX1ViNuo3RgPdO8p63K04Ug83rL3y6G11TZ3fOXLjQ9mtnnfIabJ8yJYoRHCXsD_7nxCb-SZAGaA0T1iqQ-Ualq5XzEyHVenhwdSROsuTPM7ADD68ne5i2ek0xXG0v85xyhXhRuF-j4mStL7AyYygFzWo-mbaMnJaPV-hsYQm_-iy6AeisnLa3ijjZMczGO06o7o-QR2ISE7ojZIT_pqsjdb1v7oGwWuMYN0fi-OVX63G3HhXbJoR8zjUsUYZ5jATB4wHNTqGW5J_vPxGOcAAEiiZV9F4XxgehYmle7SCFznwLzuisDBl82gjorjab72sj29sbM58ceYvnnSQfIwN8Pljyv4zD0X3j7qXE6MVe64CG5CXyNvhI37Rc11B8glSoONQOeFPbCt1fH7Skpdb4bYY0YB8ICh_jqiREcvKurd0uTUM32Pv_hLU70AhEKlSTf0of0VBrc6TXHK_l_jYLYEe0iqulvTcviJjd6YCDvQoMLH3naqbNJ6LfjMLFZjNUFDx1_mJaXlP7hjL6z_kF2UZZMo4hxe5_oSIl2kby2RtIvt_eMDVPb2C7me2qe7xRTyiohWbGFL3CY6of3cOGlRyeecJNTDE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0aee2a837.mp4?token=q-5rbmS1I4MwBTNrPhEKHz8kBhVkwWISZtg71IaN3B_5yxpc-HJWfQ9CadAK37bp9M4MZUhyPexX1ViNuo3RgPdO8p63K04Ug83rL3y6G11TZ3fOXLjQ9mtnnfIabJ8yJYoRHCXsD_7nxCb-SZAGaA0T1iqQ-Ualq5XzEyHVenhwdSROsuTPM7ADD68ne5i2ek0xXG0v85xyhXhRuF-j4mStL7AyYygFzWo-mbaMnJaPV-hsYQm_-iy6AeisnLa3ijjZMczGO06o7o-QR2ISE7ojZIT_pqsjdb1v7oGwWuMYN0fi-OVX63G3HhXbJoR8zjUsUYZ5jATB4wHNTqGW5J_vPxGOcAAEiiZV9F4XxgehYmle7SCFznwLzuisDBl82gjorjab72sj29sbM58ceYvnnSQfIwN8Pljyv4zD0X3j7qXE6MVe64CG5CXyNvhI37Rc11B8glSoONQOeFPbCt1fH7Skpdb4bYY0YB8ICh_jqiREcvKurd0uTUM32Pv_hLU70AhEKlSTf0of0VBrc6TXHK_l_jYLYEe0iqulvTcviJjd6YCDvQoMLH3naqbNJ6LfjMLFZjNUFDx1_mJaXlP7hjL6z_kF2UZZMo4hxe5_oSIl2kby2RtIvt_eMDVPb2C7me2qe7xRTyiohWbGFL3CY6of3cOGlRyeecJNTDE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
گلزنی لیونل مسی در بازی بامداد امروز تیم اینترمیامی در رقابت‌های‌ لیگMLS؛ یاران لئو مسی این بازی رو دو بر یک به حریف واگذار کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/28292" target="_blank">📅 10:03 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28291">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqfxIhP2lb0HAzwE5AWgE3jUR62rEuqDy9BScZQueZZyfFHKG-Y78An1vQw1QrIh3EOHPhDDI_76nQWS5VO6pKxosOrl1OYTWbksZhdQ6nF6K2URmnljaV_MGadIS7lE5hljL3r5_Y7awbX8Wi2OPnplzvfEbhoWSroP0dm5LRrxE-_CaqEAyF6VrRj0DkDgSNtt9xJoLaqGkCWIyY6PPVyd1GAkmEZaj4wVjb7Y_e-2NkL9McuG6ko0cDUgfIZaIVGiSMhGnJyIgJ4HYx0og-8wkD8BwkpigKJsXcsfncH2rSU25VdB33-_mI5t5HQi8MbIVO6dRPzzOumk6DqFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ شماره 9 الوصل به مهدی طارمی مهاجم جدیداین‌تیم رسید؛ طبق اخبار دریافتی رسانه پرشیانا مدیریت‌پرسپولیس بعد از اینکه متوجه شدند که طارمی دراروپا نمیمونه قصد داشتن برای جذب او مذاکره کنند که مهدی تارتار اعلام کرده بود که سن او بالاست و فعلا نیازی به…</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/28291" target="_blank">📅 09:35 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28290">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=abdup8E7E4_1hI_W38-kz-57GsErQQ51Lk9bG8ApTK9vVGD8UKqZZR48dscI69baxhOnOrZPndPiZV1iJcMpkeK50FXVpwwsh12gp6dPwsP-S1svHImBswHrgwjI4awF8two74emXLgrVmB-IRJBQJImW2L54TuAaoAbOHV651q_2ehj23xaDk1_-tZYoeQ-i5DUEBgD8nAUn_Mb3BommUjWoy_tWfTJt_ZmPYi_hpAh1PptMjkr_Eg78IW9Cug0V5RivkLl_cOy7-diuUGBvzwSsyDmFvVxZ_eH2pXnmpVLH1UJlSWuRSWM3Ja-9dDtLeX1piPfygb-2eSuz-Uaew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a83ce844.mp4?token=abdup8E7E4_1hI_W38-kz-57GsErQQ51Lk9bG8ApTK9vVGD8UKqZZR48dscI69baxhOnOrZPndPiZV1iJcMpkeK50FXVpwwsh12gp6dPwsP-S1svHImBswHrgwjI4awF8two74emXLgrVmB-IRJBQJImW2L54TuAaoAbOHV651q_2ehj23xaDk1_-tZYoeQ-i5DUEBgD8nAUn_Mb3BommUjWoy_tWfTJt_ZmPYi_hpAh1PptMjkr_Eg78IW9Cug0V5RivkLl_cOy7-diuUGBvzwSsyDmFvVxZ_eH2pXnmpVLH1UJlSWuRSWM3Ja-9dDtLeX1piPfygb-2eSuz-Uaew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوم بالارد ستاره بریستول‌سیتی رور گذشته این سوپرگل پشم‌ریزون رو در دقیقه 85 به بیرمنگام زد. گلی که اولین گل رسمی او برای بریستول و نخستین گلش‌درچمپیونشیپ‌بود و خیلی زود به‌عنوان یکی از مدعیان گل فصل و حتی جایزه پوشکاش مطرح شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/28290" target="_blank">📅 09:13 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28289">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">📊
🇵🇹
🤩
تفکیک‌گل‌‌های‌زده کریس رونالدو و لیونل مسی درکل دوران‌حرفه‌ایش براساس باشگاه‌هاشون.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28289" target="_blank">📅 09:07 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28288">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d382486c.mp4?token=nW2jdlsf7pbTp6r3AyifS83uqhXcIyMSI6uZrCG4Xgv9MmOfW0QTAogPO99dQwfWX7wVTp5EFTKSmFHXZVFTMMVOPVnSAU9TkujK84If-JKznfs-x3I2ufmsZyXxFK2oKzc3nVCgCYNiMlxlARcnWyy73qnYYr_3rd96-B0WV2fWmznX2vK0LD_riU9oirfLNHE7m76SuCy_ufplQHJOPlLfMJxM59yFBDQa8VCxtxLw7pqOx3fuyiCz7lBgHMrtd5vNNbP4Wx9t5h6Uj9fcRe8hOFBK392RMyPMNfz86Hq_rofsS9Ms6rq4mun4S69sdli4WpbA1KQMF8e8oWOxoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d382486c.mp4?token=nW2jdlsf7pbTp6r3AyifS83uqhXcIyMSI6uZrCG4Xgv9MmOfW0QTAogPO99dQwfWX7wVTp5EFTKSmFHXZVFTMMVOPVnSAU9TkujK84If-JKznfs-x3I2ufmsZyXxFK2oKzc3nVCgCYNiMlxlARcnWyy73qnYYr_3rd96-B0WV2fWmznX2vK0LD_riU9oirfLNHE7m76SuCy_ufplQHJOPlLfMJxM59yFBDQa8VCxtxLw7pqOx3fuyiCz7lBgHMrtd5vNNbP4Wx9t5h6Uj9fcRe8hOFBK392RMyPMNfz86Hq_rofsS9Ms6rq4mun4S69sdli4WpbA1KQMF8e8oWOxoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نون‌بیارکباب‌وسط‌برنامه؛ اونجایی که السا فیروز آذر گفت میای کار داشت به جای باریک میکشید:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28288" target="_blank">📅 01:59 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28287">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YYwR69UMZErj3HnR8I2eC9HYKQ-y1N5qBF-tRunNh29HPaGLM6-RTJtpXhZ_XfdT14yFC4aaQweeZGCntefEOcm1-k8g9DdDeoEszN5_vgvOJ42kNzvV8_-Q3qbB1kYdOyCvrv_j5qhKqnf1lJnTnAxgOzkSQJEeZHh7UxR8G_DZiwjAkQKyUwdt2Y1T_nELdfsTLBEfs7O6wtm3-2HQ9XpvJxGWdnzpm7qj-mUigFMTLOP9COIOyJ74m5GXVJ_wPZ8u_rs_AZ9_Kqv-R09Pjcuxi8oUViZLUKwF-QL3eXjhNd2ZvhJdjaKf6z5E1l7gIf6lcvueE6daQ2ZWCGLpuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ مدیربرنامه‌ های‌ یحیی گلمحمدی در روزهای اخیر نشست‌هایی با مدیران باشگاه سپاهان برای پیوستن احتمالی یحیی گلمحمدی به جمع طلایی‌پوشان زاینده رود درصورت شکست سپاهان در بازی فردا مقابل استقلال داشته. درصورتیکه توافقات‌نهایی‌بین‌نماینده…</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/28287" target="_blank">📅 01:20 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28285">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XZfaCD7RmXgcgeiW0Gh6O34wcYOxmlbMtMFQOROX9g4BJCucpX83XTq6iJjM2tTWXXkRoyFx57x2KQ2Lp0ASVCY1d4VYx-Zeh6Ecb_6xCZUcdSaVQghAZsOCECpkeqsP5ii1oOA3clWl3W7tDKu51jqZwR2fcbVerRU0QVjKSdDiHSeidRR9RkgZmnBOIj3xDV-WH3kJsyhwGZ3Vw_MQwilESprogBkDZLNFrj3mZs_0UzgKaT2X3OKQ8613AlgWh0KezYsV79nF9GzoiAqk34GppTfrNpUtx6JBs1091QTSuK-AAfBiPNU7Ki7w817QEoG_isbNu7ELP7wk0d9xiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از تقابل استقلال و سپاهان درهفته‌سوم‌لیگ‌تارویارویی شاگردان فلیک برابر الچه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28285" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28284">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jrIAxheHRpON62LjsXzJP1lWYUcHjKy--_c1tpwpRFijYJChZpp2TMgu7DRXensSzfTsxSuUz3r8iuOL9qkx1BVkZgnUOynsd37emnyuG-cliID-txmfFiJ-N6pXzzFMn1lG53NK19uMZECQRHUm9XCgLBE1P729m08h3FNjtJfjwIPA8sgryOQWJnTpi7wMEo_q0GfuPQPg7bKcn-HucA7auOSBcHTQlHSRX67HJCZ4QNcHfTlkos42vgUnUnWTVIMGPNHNvpZPslr3djv8NCAnqU-kDHAx1fhwXGVm7OCuYF8DkcSh71J-ckiFCF9czKolgMAEExoWcLGYKN5Nng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌ دیروز؛
بردارزشمند رئالی‌ها با گل اسپی تازه‌وارد و سومین‌باخت پیاپی دورتموند مقابل شاگردان کمپانی این بازی در مسابقه سوپرکاپ آلمان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28284" target="_blank">📅 01:15 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28282">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUP1alk3GGHLnvuABQJ7d5eOer7O043c4sn3vviGO7FY9n5hoBVsCN7vdX1UzxSXZ_WgKep53ZhVuz5UczWgQ0AEFrD6iS7TM1QVwlo7ZPfcTuPhiUwFDfY-Sl2NQ7wzqt5EC3ZkEaxuKGn48UPF4plELfl7shqLXJsO4zf7ZWRXzhiYVZPMRMHu4VhMxxuItX1AimGuH8Elz7zPdFegfsKG51tlm60Xb_8c-PfgPRVKUpYZE34JCoAi_ImIAep2xkuTKPEAO76G2cGxGusmZhoxlQuFH1JJOphNkPEId0Q2RVjkTnChDCeSTRE9yuVU-8MV4zX_oxkSRmxFr3PMkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب با اسپانیول؛ ساعت 23 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28282" target="_blank">📅 00:58 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28281">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZoC-Me01-4QLmn__5YSF5bZCviYXDvcM-Zu2qbk537ZwqLxPsUOspLSYVsXxPctp9dnSmDCOdM7XDzk8Q6Itsao0c5UNvHJK1UVoUtTN9NpgKWDFLpgCuuC482AIXMRe2app2e1eNMSikA-uJg1MJqbV6xEXJbI51OULpz_ZsjaakVwSQCpcpFSFWdR23somySkhKN8mChQojKyKDyLxlm7EsSW8glJ0W3bvE3rprLMhKcNkwwcZYHS3Elg6AmO0NYXfx9dh-Gm-b6uqbH-oyl8Nx7W5xjkxb9l8K7hI-RYG5pQ89fHG_STghFmuVyjkPEQxvQi_kfX2alc3k9ANQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگردیم به روزی که هواداران تیم ملی کلمبیا رو سرو صورت خونواده داروین نونیز مشروب ریختن و اذیتشون‌کردن داروین هم برای دفاع از خونوادش یه تنه زد به قلب هوادارای کلمبیا و باهاشون درگیر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28281" target="_blank">📅 00:49 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28279">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtrqYmM168vMkHZzhWQEzlkkMUyv-Tg4_Aivvbr-W4RSZWsy06teTtTmskeJHV6lxS7AHrmI7SGOxvkJvwpf9Qbk0SQDASy-L626M1GAyXxIDHteGW_2G-jdY0i0XD3vgwPG0JB4P3WeQpJUOv0NlsN6WjDmqCK2kUwHkGaep_PKMKJiM0edlauKtdHj843TZrhmTxZze67ybbTCs7Cdro30gSFTF-XeHsM5mrM3p2-MAZGHxV-I4gnZHMbhGxxJbuaD6r7JUd9w-2w3OwXEYe7j4BdRQzaXgjTFFsVGWdJdK5yNdDU4xgovXqI320JpHa8LITWDfPhbaViph7B9Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R39QBp56N1m4oOQHzeynK676znbn5nebagpsoVxF5Kh7b2u7cwgP8WnIF_KqK8CcuMsUPvPg08K0pN1VtQ-zIA0lpUJIkPw-xEpH7PGcMqi0o3NRjTqiG91N_EaQimA56wl4D-h4Hzs6dOoi_Z4OhWOrR1ZEE9nEWRfN2BryBnnUtzGG_H_mGTZ3YpQokkxnuJ_BisGKq3PhJGTNWOg4hxI-H9M43WP8FHs-K8ry4H5YgSDVntSRe_cea8em3apVqMrQpR7oFCllZj_03yhxZEpFpACvI7i28Xf1i8W3tgK4GjuBRKt9gnwdNKqgGmVaGwP8xmhiTiIJ3xkwpJIJjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
🔵
ترکیب احتمالی استقلال
🆚
سپاهان برای دیدار حساس امشب؛ ساعت 19:30 شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28279" target="_blank">📅 00:37 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28278">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dmq8kkV2A__gAAMMtBeKWGDb5SZ9dbUiil2erFLc3Y_kdwwbxwi4_YBVutpVGATR36obSujQblS1yPoOJxHrpiaCvuTKiuJmf01vPZCQqc38bnX_sAfjtINH9twTkuxsAdOB7ouuRlfjxb50VX17e8HmhCsa2vZBWGPqHioFGAY5JD7wgaSe-ELlK6arYLGcZxbaMFYhuep-KXBlxq-0KaK86lEyrRN3LHZzk1FvhoGRWWX9kgarAb2ZaLnDW7Aoq5H1qGZBBiuF7stuAXIdoTTOk5dXRb8xsm77u9mD5q5r4tMOJDLoDwPFho3zpWFezqkLxQO06MixvMKWgiy9gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ احتمال‌دارد یحیی گلمحمدی بزودی‌ازهدایت دهوک عراق استعفا بدهد و به لیگ برتر باز گردد. بوی یحیی در اصفهان می‌آید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/28278" target="_blank">📅 00:12 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28277">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMYRrrOSNeLC5exBJ7XEbS80dbfrlhXYs7agz0l0l8m_ToEetlQ02oy9vdwuAI72VxrZtvMe5i7LkC-8uKeP7zj6lFEhBBlkiLQPat8n4LIq-Bj-0dBw85ASfjm5-lMGfXEMzmJJjM8JUkjess7A48X25cKeHMNEZRfLFcaupVQl7gOdUuwnl59FUicwLIMqsPcUaYqRDd5AwUNrsGMBo_b0l48T1v8atJ4oicJrayXXpH0T5m0LeYXgZKSn8X6cbY6Z1J4K4l0uRobRRiq12S51CG3lFkMnToD0whXS1ASnFyxfBTTKsgxV8jCKG9OOxjsP0Yh03SyYdJnLkKzfVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپر کاپ آلمان؛
قهرمانی باواریایی‌ ها پیش از شروع‌فصل‌جدید بابرتری‌مقابل زنبورها در سوپرکاپ؛ کمپانی فصل شروع نشده اولین جام رو گرفت.
🔴
بایرن مونیخ
2️⃣
-
1️⃣
بورسیا دورتموند
🟡
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28277" target="_blank">📅 23:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28276">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt1KPT9fdZ3zufcW07VSdJSe0fa9TXiaQQxvNxcYL8koCOSYXhkyrhedxo0iLfW9XYv9n0lFHysWdDl0oQLh1toToUCjupcmfK4NRiZsvVjVA4p_cJVbBUXkQuLNauYmpIOxOIlmx0SXX2_eflCfmyEKiiyoh5OJNO36A0_APZaDxaeVHXBxeEW20z8wprWg_2lR2cuczV8NbUa7FoR3qq0LUG9lNRNFFA3YxeGUDyWqLbS-G9hsDeLabjxZHjj1RHjGiz9BOQ4gJngfIaDF8VONtQCNmVNrtMCIZOh00Le2TZIDESqKt-YP2VACwq6el3TzYngj2cVKGyuDgGpx6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛ تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28276" target="_blank">📅 23:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28275">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBC1KnB2FW5dgjd7k-W3zwhyJJ2VaqexWod2rk2pmg2W8f1bTTbyMhE8YpnyJexTYTHc1UloM107sj9woxQOHKM5A_oXm2H84CuSnfCNOJZvanS47CgJbpfo1hClqAgN6wy-mraJLYoWP9CmS1IRsl6HoA0fzHWlfCvCO_qFxfRuib52tJtWCWVs1FIAbHQ_zHqKir8fSqKekcJnM0j8HAQ54GYWZyuNUDq2iCZW2ORxqw4KG3fbqp1vJfvz81WdmZJnEXjXa6pdCStjSZkHkWH-8QDGdxfefx_IWJnN5XtHOc1y3NlfjuSatc9LytdTnsQqsVzxFVsFHZY7nI1eyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ‌ برتر عراق؛
تقابل جذاب شاگردان علیرضا منصوریان و یحیی گلمحمدی برنده نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28275" target="_blank">📅 23:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28274">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=eZ3N0V5aEVHKADlHrZuYTLYeGNyjNQyOXE8gjY1OL7h_5Cx7Bo-562VTMCXrMfXpDdU8n6E13Bz4bzxUXyVrQot4KWLfjxMa7bTMm03Tw-8-5sBXIV1ZavqH6H1o8dp-ZOr_x-WIrkGnNaXAe-oXzYu4DZxc-awiC5wBdpAGWOEWPQXJ-626klrs1DOQbcn9nvUw4jP4tRWE9x8S61TjxqAXyn_BJaT9Njnx2YrbZsajb5AahDPwuKIFKwa7aZtVitKbulUp6swWV9RL6WAIg0MteWa7tHzIsltbu_w0ghhAK4y8waHhotxXvBOf5cAeIDx0B0LtvlSULdaRsPEhOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0d528c86.mp4?token=eZ3N0V5aEVHKADlHrZuYTLYeGNyjNQyOXE8gjY1OL7h_5Cx7Bo-562VTMCXrMfXpDdU8n6E13Bz4bzxUXyVrQot4KWLfjxMa7bTMm03Tw-8-5sBXIV1ZavqH6H1o8dp-ZOr_x-WIrkGnNaXAe-oXzYu4DZxc-awiC5wBdpAGWOEWPQXJ-626klrs1DOQbcn9nvUw4jP4tRWE9x8S61TjxqAXyn_BJaT9Njnx2YrbZsajb5AahDPwuKIFKwa7aZtVitKbulUp6swWV9RL6WAIg0MteWa7tHzIsltbu_w0ghhAK4y8waHhotxXvBOf5cAeIDx0B0LtvlSULdaRsPEhOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
اون‌هوادارمنچستریونایتد که قول داده بود تا منچستر 5 تا بازی پشت‌هم نبره موهاشو کوتاه نمیکنه رو یادتون میاد؟خواستم‌بدونید امروز 683مین روزیه که موهاش رو اصلا کوتاه نکرده و این شکلی شده:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28274" target="_blank">📅 23:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28273">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ix9Wf5n6OCVWupQzPNhArK1uWKzyHGkoJqhSa55vQLFE6BCCe2Btu8HkHI_G-uFxP2u0TBpTB-0JtiMdkv2fiBUVX7lF6KhoW6jt9ezRXgUWBatbcEkgY_ZhfDYq9AibwYA-MukBxYhx9hIlNJR5qefbtSlzm1h84JHCwcIQSWdmOZvoVvLlVsw9bEQCbVofgWX_Zk_k_HI56HHpDKP4k02cAweQLjwT9R5SmF_gnXxXmg1bOBAr5bXp4tIBh9fFEkfUyR10PBjrywvoGJlC9MQggrhEfXRALnGzt_jBR7S0SjRvZI8W5QFM14LuPEVQVqgAwPJiIMCeCE4i1F48Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇮🇷
العازی‌خبرنگاراسپورت‌امارات: محمد قربانی دراین پنجره‌از تیم‌الوحده‌امارات جدا خواهد شد. این باشگاه‌بزودی‌ازپیونتک و اوندر دو خرید خارجی خود رونمایی خواهد کرد و سهمیه‌‌های خارجی این باشگاه تکمیل خواهد شد و محمد قربانی رفتنی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28273" target="_blank">📅 22:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28272">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=bai6rhg02jRBK0zDdZl-ffY2pbJ6AZqU8R0eMNovwSCdIeXQPeDMbNhADYReUg1pEZ88X_ST-M8U8Mn8YBH71Zpr-9SBmqQ-CS4tolWXU5lPB_KdXZgc0e0escL36-YduoRgbKs0B5njT2sAzZ19n0hc-brLKu_J18GOpdSpduFpSIq6NBdz2k1BGlfxC1X8tN73bp1PSGPAKkiWAIpWfPYTT1-_AqFY0MdecAPYL60ZYayvxxSUmCW_p65lD2eOC1t8vpIbm-WcK5P_7CooFLcppsc7uSHjmkbURP7gGjLZ5sdmrrdD06Wv6SHZ-6mnPkO5VuzAKizkEfoM19EoXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cf22c74a.mp4?token=bai6rhg02jRBK0zDdZl-ffY2pbJ6AZqU8R0eMNovwSCdIeXQPeDMbNhADYReUg1pEZ88X_ST-M8U8Mn8YBH71Zpr-9SBmqQ-CS4tolWXU5lPB_KdXZgc0e0escL36-YduoRgbKs0B5njT2sAzZ19n0hc-brLKu_J18GOpdSpduFpSIq6NBdz2k1BGlfxC1X8tN73bp1PSGPAKkiWAIpWfPYTT1-_AqFY0MdecAPYL60ZYayvxxSUmCW_p65lD2eOC1t8vpIbm-WcK5P_7CooFLcppsc7uSHjmkbURP7gGjLZ5sdmrrdD06Wv6SHZ-6mnPkO5VuzAKizkEfoM19EoXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28272" target="_blank">📅 22:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28271">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=C8C62wVazY03K_e92kJD51B4P8QtSoSpz0Jdpe9Z0Y2kmQxfFuPO1Ov4RRKv7gLK9OdQvH9m33WZCBeDPAJHwc3kiUEkarSkxeeCPe2Jhfj4CvLoR4S9MlBMsmLk1uPFw0m-ZcfqsUjogYfIRmVUbcSxSzIsiDnAUoqLNwWUrA-MkOBbKtH7OgKvXe0NIPtObcVKj-t9ESadlJb1WdWGzTGSSL5nJu7MMpEqPrPDgSRK9pZWXRTFNuHmCSvtSlacbIhC1NOYEE5aLj34Ir61Aq7HTmBmRxcCcKtPie9h1metg3K8K2iU_SyvP4nDI5jxrqhyzCOf4ZMTtZuKbEZyeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24c1f411f.mp4?token=C8C62wVazY03K_e92kJD51B4P8QtSoSpz0Jdpe9Z0Y2kmQxfFuPO1Ov4RRKv7gLK9OdQvH9m33WZCBeDPAJHwc3kiUEkarSkxeeCPe2Jhfj4CvLoR4S9MlBMsmLk1uPFw0m-ZcfqsUjogYfIRmVUbcSxSzIsiDnAUoqLNwWUrA-MkOBbKtH7OgKvXe0NIPtObcVKj-t9ESadlJb1WdWGzTGSSL5nJu7MMpEqPrPDgSRK9pZWXRTFNuHmCSvtSlacbIhC1NOYEE5aLj34Ir61Aq7HTmBmRxcCcKtPie9h1metg3K8K2iU_SyvP4nDI5jxrqhyzCOf4ZMTtZuKbEZyeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
سوپرگل دیدنی امیرحسین جولانی در بازی این هفته فولاد مقابل شمس آذر به سبک تونی کروس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28271" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28270">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/28270" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28267">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ESDm8lUyFnv-ZIF5O3dX-lxk8vgkZWWTplFpMJo1hS5DeLeSLNGVAbvCtK0F1cOUQUPrP0lwxWo7kesxt5hH107tIy9OGk64k6b1LrvAfRJcddxhg1kHizw_WOG_Nv0P1iOx1uo6521Sp8wNjsK5NQ7l48-MNZjDPhDgXGYlyQ6O60Zgoe-yTlfqKqa9_cpGEnqL29vu5zIiLtMlbMvno4_12ZcUNwd0j3ETeFKLeN2YvQmiMxKWTYBUHM-a5P78Tzl-mHTq1X4ut-t9pLff9b0szY2HHEmgA_VjC2eDWEdkJPQhN7ZMgLoXWnGfaEX_x7gsNXQjbSIN3_uk2lvlzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWo-FHzSbO1wyfYMRBZNHEA1fPhw5OEy2IydHrNrWz9o3HRrcMJ8FMfPYvvNOzhN2CgIDhBiRhY_RJ3hSjr7W_Pj3PsCcG535ko41yGkCqKEwcMMeahjDvqRzMPoUSkGDYCJZpH3vrZ62THIOJFxJpygp_5Q7nIkr-iIcKcJAEJpY3XpdHt-ZBkLNCMJL2ggRI1tU4MLLAoRTZmYgBaz-xTtyF4VawX1xfqcx2BB9qK7ohbmhou1NTePcbqMVMeUmZHoJxUahvQllTNi-NLiIUmwak4jcMCtVJSnC49bFsS9W210ntQ-sVkwBqXBhUBHvPI2_lt0RL4mZhI0E9HBfQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول‌رقابت‌های‌باشگاهی؛
مدافع‌ عنوان قهرمانی سری‌آ فصل جدید رو با پیروزی پر گل شروع کرد؛ تاتنهام همچون یونایتد شروعی نا امید کننده داشت و 3-0 بازی رو واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/28267" target="_blank">📅 22:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28266">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gpmn4NGqhsecU4j8n2Op9fuKGVm2j6VKUGPjtUt8nu_oIIxlQ3OdTafrGBthn6xpGSENcazXQvbgFXSIMtl6bgOx2v8jL_Iv2Cc8jYqIiuwzKMDWucLYylTNbWEI28uCqhmjhkkYj3Q3WpChdqRhoxiNoKgHv8F9HN_wm3CXdhhLHLQej40AYSLOuSVeI0m4AGrB8tppSi0Fuvad6OOxNMz4FFITiyx4Je2W9pw1XKotavtZ4J_JkevtYftDHM1nwufdrIbWf7i5CRfSofoYw6DDMctoagpiCBnzuVpekWusia5lvkzJbaCe-SX5p9M_sCCPIPrrMVnbONUPCvJSwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب با اسپانیول؛ ساعت 23 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/28266" target="_blank">📅 21:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28265">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqHCp0Z4dTnBaYwka8i2GEf5WuSXqOtNIxkIxNiy_69MqPE_oitEgVLHo1Z6NnIZ6pEElZ6d_QCOvHVsL0-1_2u-bkOLuzZ5yjjZMfEN-pYqEkVA9tN-bnGcwTnR-5orlwXSYx63teMB8GNlVFOuKy8hv6riGyOaT5OErLxEUCnjUhbgUrk7FBSAGtdOyzxdSRS8w5Kegmjsu8o71b7MOKNFUpIwUsoii9IvyKDS8vrBsdaQPL0czCXtYtjjkqTmXb70MTJL5w4bo0rvyynT7-gZ571HslD74wqk2VXP6jh8sirasAB5uGO4q0YkNSvqT6SPwtX-CdP1064DTOu26Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
24 ساعت از 72 ساعتی که مدیران الوحده به مدیران‌پرسپولیس‌وتراکتور برای‌پرداخت رضایت‌نامه قربانی فرصت‌دادند گذشت‌و‌خبری‌ ازهیچ‌کدوم از دو باشگاه نشد. رقم مدنظر اماراتی‌ها 1 میلیون دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28265" target="_blank">📅 21:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28264">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfDlj_F934Xao9lHXEG8KeAC4aW6qXwSCYgRbiDkuNDQ3WP83QdFHVIYcJchN0qLQ7kVfL5QxAF11z3rgP0ZLe0Y2vB4ln1ZehRG6X400uAvu3WGBWQSHVTlVJdif8VfMeDl4p28QdfKJXgo8IIKI2k626A5qFJi1xaE5mT5EY30N4uo6T4k3_mQiVcSLfLGjcUre3rVVciN2vgha3HBMIUelj5hn2t_4RpRghwNJs5DloyFy9hECrS9GoEA3lSxeMhKQuqytXbuhB2S3Y643U5oL-MxP-vuOQi56OIuS7PiZcyNRaS3YfGpSAxqF7nq9bNG5Y-MhorP9yA5NGn_LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
رئیس هیات‌مدیره استقلال: اگه استقلال رو قهرمان لیگ‌معرفی‌نکنند از طریق فیفا و کنفدراسیون فوتبال آسیا پیگیر حق این باشگاه خواهیم بود. چهار شهریور پنجره نقل و انتقالات تابستونی بسته خواهد شد و ما برای جذب سه بازیکن آزاد از فیفا استعلام میگیریم اگه مثبت باشه…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/28264" target="_blank">📅 21:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28263">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/495f39b6de.mp4?token=k_4dUgV10bsAxG0f8jXe4eo9Dr0kpmZ9TqiSrtYw1Ja7Z4meKvs8JxanPql0PnnGVY2b6psE93nZAyrCoc6_0HvZzz949_E_7TIl_CVO2pH2zASU7HcsyQyyDr8eRwZMgvEXefvH_rvTd_jjST1uMAuHoSsdTvGAazCU1CXHFnUPHjrQ-XCnFVP6y0mHXOohkoHXJZclTElWOHpZsEjRjERwTNsd9KyEVcDsYeT21eOM5IPocRw2Nur_T6sf4z2Olkn91VVa_EHNo6ySqGMPz1xMjNQO47UxT72toDwc_7DYaEFX142DqbfUn53A0O0-h7HhqXYdKLcoWoV8IBGt-JEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/495f39b6de.mp4?token=k_4dUgV10bsAxG0f8jXe4eo9Dr0kpmZ9TqiSrtYw1Ja7Z4meKvs8JxanPql0PnnGVY2b6psE93nZAyrCoc6_0HvZzz949_E_7TIl_CVO2pH2zASU7HcsyQyyDr8eRwZMgvEXefvH_rvTd_jjST1uMAuHoSsdTvGAazCU1CXHFnUPHjrQ-XCnFVP6y0mHXOohkoHXJZclTElWOHpZsEjRjERwTNsd9KyEVcDsYeT21eOM5IPocRw2Nur_T6sf4z2Olkn91VVa_EHNo6ySqGMPz1xMjNQO47UxT72toDwc_7DYaEFX142DqbfUn53A0O0-h7HhqXYdKLcoWoV8IBGt-JEGhtDkyFFJp20J7Tm0DiyeR1D9-qQbMJLVwlFk-S6dir0ka_LXCxsddyLb4aDHhJ8FBPtDPd1-K9gcjhxkhNaVyRS_CJ_yl4UO31WqAzk1R0QPGph4Vv7Y2VttcYFrSMoi4527HTGu_vu-s0LRuXA7qYHkrBE2RKe4MXa3GckEMEz7KaJXjioLFQIKxI50xelIlSIrl5EH8B515BXXFhU5BADJfxJ4anC4Im0Srt_u-0pxbfeBjpxMSdlbZ8LOdFG_0rz0ttEjr9AvOGOUBSn-mqtK22wPe7KWFT0ESeAbz_7oPsQoYisDz86Z538iA-bnDSGg6mcPXd5p74J2eJ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جنجالی و عجیب و غریب حسم روشن درخصوص ریکاردو ساپینتو و کارلوس کی‌روش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28263" target="_blank">📅 21:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28262">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46b6436f17.mp4?token=KU779UgC-7PpKYOOR1naOPZL8o5WEmazrIYucODCkMTKGNriiex-_Lsx9skIlE3hMhDrrbChMac5f3w5zR1wmpFQfGk6pAIgVNu0grbxiGmdmgEk3Fwg52psHePGj9Bqwysac-7Fqop7sc-QfPsYoS9aGAekZ0m84g76BjF31X1yJIYVCV06X-M9VhINfUGMNTkWsXvsFdMvvHi0wKnJ9lAv1GwwmFZZEDuYdrdXYmjlVxchk72bWbCZvYU0YrZPQeHoGLyiS2_eK5-ByJWsYWlHiyp9-v_hGEmWCubXlx-rl44NoObk1eRocHf1zy7rlbSVmAhK5DTO6DoDxyZ-Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46b6436f17.mp4?token=KU779UgC-7PpKYOOR1naOPZL8o5WEmazrIYucODCkMTKGNriiex-_Lsx9skIlE3hMhDrrbChMac5f3w5zR1wmpFQfGk6pAIgVNu0grbxiGmdmgEk3Fwg52psHePGj9Bqwysac-7Fqop7sc-QfPsYoS9aGAekZ0m84g76BjF31X1yJIYVCV06X-M9VhINfUGMNTkWsXvsFdMvvHi0wKnJ9lAv1GwwmFZZEDuYdrdXYmjlVxchk72bWbCZvYU0YrZPQeHoGLyiS2_eK5-ByJWsYWlHiyp9-v_hGEmWCubXlx-rl44NoObk1eRocHf1zy7rlbSVmAhK5DTO6DoDxyZ-Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28262" target="_blank">📅 20:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28261">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiOcKp-YDGwM_D0GDynd_hrR_dWZW7Ev0jElajQCXJah8LncEMqL4RY0p9-jcvfXIMFwHMDCH7bi3DLL6vks4ZrGw0pUt1t-J2hXuB2qjdpZGIyJB9ulJ3RTZGWfpoIepnCEZIY3FKYmBBQBpmP2qHzlaFymBmHQGuvJiPr7pkJkxKh7kiTWVCs6nRn4zShDoQkQrV8NjV4A3X-y74X-kd8eMFyWAPL76eptPr0pXhIgaWWWHtrZmfJybPSXjTHB9oS8OFx057ERdsA7RLPaHuupablBqbc52jYooSPMsnxxRAFB848sAf7P_ip9o5FccgpsSyX5P7hnQRJZEXqZJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باپیوستن‌طارمی به الوصل. الان بالاترین سطحی که لژیونرهای ایرانی بازی‌میکنن لیگ لهستان و هلنده سراشیبی سطح فوتبالمون خیلی وقته شروع شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28261" target="_blank">📅 20:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28260">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136a8275f3.mp4?token=lIZ-TaX5G5twwq32ux6Wdw_ca6rFZ_lmpBBdR-d6wEOM8sh6vgfgbWyTCCfB4h6eU3JMf38-hl9cVkp5BEAjiRlH5rV8WE6PiRmh9y1gAiR_HlDDPXoX0H4QvXX747FHTKidoDteaixnsxj5vb2v8Q21ifdCYpWJZaJaHw5-6NHAiJGjZDz1S6FRUlHl_bVv8fIZhqwEmYLAq_7YZiKAVwyCqT7LMUt0YFWIpV1m9yjzh-EjxPWBR3x-XqzH1wOMOb4zzhqjKMraHQHClyBFpByuKXLZfUQo_iJrKw4zIAgTovfu2N4eD5AYeZCFaVtEj_I1lx3vubz2DFaoCjBqVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136a8275f3.mp4?token=lIZ-TaX5G5twwq32ux6Wdw_ca6rFZ_lmpBBdR-d6wEOM8sh6vgfgbWyTCCfB4h6eU3JMf38-hl9cVkp5BEAjiRlH5rV8WE6PiRmh9y1gAiR_HlDDPXoX0H4QvXX747FHTKidoDteaixnsxj5vb2v8Q21ifdCYpWJZaJaHw5-6NHAiJGjZDz1S6FRUlHl_bVv8fIZhqwEmYLAq_7YZiKAVwyCqT7LMUt0YFWIpV1m9yjzh-EjxPWBR3x-XqzH1wOMOb4zzhqjKMraHQHClyBFpByuKXLZfUQo_iJrKw4zIAgTovfu2N4eD5AYeZCFaVtEj_I1lx3vubz2DFaoCjBqVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
سولوگل‌دیدنی زبیر نیک نفس در بازی هفته دوم مس شهر بابک با خیبر خرم آباد؛ قرارداد زبیر با مس برای یک فصل 8.5 میلیارد تومان امضا شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/28260" target="_blank">📅 19:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdcjjOOP9cLVKkh-1F5RneSfCbOCAjpMAbxWAXi0SZOasgxfLYvvXf0ZYQ4qHX9mwvubDp7rgEPA-rzQJ9Oj4bJPj6WQuPcVMlo5DToOJJWItWSdHKGM--_1f8bq9tf5wvo1TZf7f30sDEJ7y9dNfRfIXUuAgtL1H1cP0zhqc4MK9xtOc6ksM-V2oxwj-q7LhL4wgpX_mvP5VrxDzdt1CZ5Io4rSJJ_n4j4RPrBxazqw6SkCQAl9YHNvLuv34TpWXH8GHsmvRqAWkpRMTj8MDcWiYlm5g-sq76XKztiIZqaogOURbzrqSM_c9i9PlpHiOlAPMS1ggZGbhq79_IR5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برنامه دیدارهای جذاب هفته سوم لیگ برتر؛ 24 ساعت تا دیدار حساس دوتیم سپاهان
🆚
استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28258" target="_blank">📅 18:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28257">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_apKGTUSZdM5Jy5h91s-nlxVWk3Gph4tyF7iUjL7DHzPb124DpcN2_r2P5Wh5M5Hb9sZH0iIlSYGpqLZpgvYf-4uzvrT-6cUJkxl3l8lrwnUwq3zt4Gmz0J7SIUljOBLx4m2Z3kP516gKOaDPNSfYP6jy7_YKFjvVgZLvJbNr22HkuVtDeP8k4JaP4gyIsZcRVtWehXI1MlKxq_gSkg0RKBQwe9pkKPm-z0v0g2Q7ja5BBr1jvy9wkEW6_PCGEmXqvtq-eKuSlaBUUzaIXkrz-Kv9JDlwVZ9uio2D8_xMIwEjSjQ8sOXvZJoNhDkGIs4o8anSek637gAREfOx3QSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام خبرنگار باشگاه الوصل: رقم قرارداد مهدی طارمی برای دو فصل حضور در الوصل معادل پول خودمون حدود هزار و سیصد میلیارد تومانه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/28257" target="_blank">📅 18:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28256">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urKT92osDDn70kyX27CskIyxt16JCSsH8ShxLRzpt_XwhvcqNfZYIIbE87UY8thyu97IBumfj6elLlktq5DOIbeX7qNb9jVt7n3AShpim4bU5n2JeSAFOWqvrlI8RYx-wlqy_Dni60mMfXUOFhbR-40gv_ByF0qHrYA2U_PKzpQ1aDNMI1vt_SfFmRrWD6v0jh6fFEfFHAG4gQt-E1zSCqPDb-QxA4rvHWYa8ovLXwMnLXN4B11e_0uf9p6E8_7nDmGZ64RGyYaXA3CXT1v-ug1kquZ-8sytu8p1egIWqUEiubunKeBuHa85DhbpIcBa5NQVoJWRH4aWxiw18uHT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/28256" target="_blank">📅 17:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28255">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e01212702.mp4?token=Bra92m6SkLxXL_9AQHpum-38Zb8Fi8QXDwNbGcDDKDGQ0snyExWqUCw6WH8oGhccf2Jl8GsJt7_imvTsumVY92PAmW-0bUaerOmLmYJoHgVCDE_85GwwpLhDM7X9DqEt-J0nY65Me4Mbbam_W_eiSHDjosrDHsRHdKWZvrZtIG86sI1z3-mN_3tlwdQIveImzdobKg8JFh0HzPgVhMt3q7f3bJQXSTy-aD2TVPvlH3xhSioBeD0vSfBgl2812YPxac-ZjDm2ywpb0IReR-2AXqT3X_mFXQot3F5lw7eLi0QuLoIshDq6DdlzRUQXI3C9r4aAuukH8JXSBDbYcgZ8FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e01212702.mp4?token=Bra92m6SkLxXL_9AQHpum-38Zb8Fi8QXDwNbGcDDKDGQ0snyExWqUCw6WH8oGhccf2Jl8GsJt7_imvTsumVY92PAmW-0bUaerOmLmYJoHgVCDE_85GwwpLhDM7X9DqEt-J0nY65Me4Mbbam_W_eiSHDjosrDHsRHdKWZvrZtIG86sI1z3-mN_3tlwdQIveImzdobKg8JFh0HzPgVhMt3q7f3bJQXSTy-aD2TVPvlH3xhSioBeD0vSfBgl2812YPxac-ZjDm2ywpb0IReR-2AXqT3X_mFXQot3F5lw7eLi0QuLoIshDq6DdlzRUQXI3C9r4aAuukH8JXSBDbYcgZ8FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
هایلایتی‌ازعملکردفوق‌العاده دومینیک لیواکویچ دروازه‌بان تیم ملی کرواسی و جدید تیم بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28255" target="_blank">📅 17:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28254">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1l6ZPJYJw5GqF8YPlMkJxwCfuvmRy4OG7_zfeDn7yc-LlTYbjuA3XStLQCuGowYwgs56almbovLl18jyk1-lxtF9hoTCEv5xdyxTiONpQoOGOvpBGKA8Gs7--DaycT5a0ImPRCu7fPXnt1BodF2Ky71idhlNNwJg_A6mD3LwzzW6tbHyVqeruH9jeJVrWtPIYed-UGadlja83QX-IfGggkFI0q9yfRKnruIQy-rVoDDn4o4dNLOOreGjMxr6m1hsnQfGmWOkmM5ZEeUrlDEJ8uhmm07s7Crvl_g_fX-UR205CHKFg831XovYOMknsNpsfx6EZc_dUO1XYQosVXPnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ژوزه مورینیو: یه‌فصل بدون‌جام تو رئال نشونه‌ شکسته. حالا هر نتیجه ای هم بگیریم. شما میتونید ساختار روتغییربدید همه‌چیز رو بهبود ببخشید، من دوست دارم برنده شم تنها چیزیکه مهمه نتیجست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/28254" target="_blank">📅 17:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyrJ0MEChq5Jd0FlKJlj3jlIVnPpfeIjWCWJTx0XLSvN4gDd0qccMqi5Z3U1CVBvJ9dYxD3-ybkzRqzhM8_EqY5C33n4MyJL9iUtG03FEh-Cw0hG6Idr8E5LkUDeLsvrDCe0KZrFJIiAj_Wznn2DEaDG8WftxP696T4bceMLNEIsOe5o4WqGGUOq6NnsP9_hOPP084RB6-9D1XcB-xSQe9qWriuo9h5R-MIn_26zmBAEdAbrhStYoZ9-7uQS0RRbVN4qQP5eZ20Z52RQTDwMlXN5wCmsAKvudaJGzcVmxblfIaKCoWErTRFRS9POlZ3OqIalD-9iWNM6ySM7EJ9EZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام جرارد رومرو؛
الخاندرو بالده مدافع چپ اسپانیایی بارسلونا تصمیم نهایی خود را برای جدایی از بارسا گرفته و بزودی از این تیم جدا میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28252" target="_blank">📅 17:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28250">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507b6b8171.mp4?token=DqD9hsFk9lIFfjYg1ht3YGnrI8_xOaiDLw9luBYkbcBMPkxNaBiBUeHCYt7jbap7nti927mf98wcgGJf7uOfmtv73bCvHxz5elHbeb9YQzEmeKbnuScbEttxRIP7WFUq-HqbJ9Az4Pawdbd7ubf2NwJcuwEZeQpmPTRT9J99x6ecQpyuCtyyIfCopC_qCBfmWDx38pPKM2C2e8xIM5HyYyMWX3Gah8mazh64anoh_diQZVdS13Y7hjRrRfpFePG_KP9C-Z59RZVF6SR-uxfpmDy0gkdRfHivsFGfygau9B_ZcXxt7ie7fzKU_14ZxTFfbCddP0oFyJpO6JPhImjwm4ujVqHzZvXH4Y45Fzk5gbdf9SA8CZoqnWwvEO1dxuHbuLURYDx4nfcntobmXjcESHdQXvXaWADIQrEPtK3zjBCWDLDrk41g7_M4cgiFkP8uo8G4JRQjhbnYGTdJGIQ6D6hghvXq6YfbQOmexdEzc3PXZF_0-h9kqgb1Q2Qgvzr9JPoOGRHLK2koCqlOMT3Boz4hKfZKwVsw6eXDjFjQiMyOWWbHYIxkLU6IM90ghV8QyTCfnPnaDBfkhAavmTg8YnzgHub1Ui1fN0t2USoX41WJ5AoSaW3AJz3n1qHW4YNuTzSu7MyKAT20LwAhvgDz0h_WipdAarMY2M7WYMbJh70" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507b6b8171.mp4?token=DqD9hsFk9lIFfjYg1ht3YGnrI8_xOaiDLw9luBYkbcBMPkxNaBiBUeHCYt7jbap7nti927mf98wcgGJf7uOfmtv73bCvHxz5elHbeb9YQzEmeKbnuScbEttxRIP7WFUq-HqbJ9Az4Pawdbd7ubf2NwJcuwEZeQpmPTRT9J99x6ecQpyuCtyyIfCopC_qCBfmWDx38pPKM2C2e8xIM5HyYyMWX3Gah8mazh64anoh_diQZVdS13Y7hjRrRfpFePG_KP9C-Z59RZVF6SR-uxfpmDy0gkdRfHivsFGfygau9B_ZcXxt7ie7fzKU_14ZxTFfbCddP0oFyJpO6JPhImjwm4ujVqHzZvXH4Y45Fzk5gbdf9SA8CZoqnWwvEO1dxuHbuLURYDx4nfcntobmXjcESHdQXvXaWADIQrEPtK3zjBCWDLDrk41g7_M4cgiFkP8uo8G4JRQjhbnYGTdJGIQ6D6hghvXq6YfbQOmexdEzc3PXZF_0-h9kqgb1Q2Qgvzr9JPoOGRHLK2koCqlOMT3Boz4hKfZKwVsw6eXDjFjQiMyOWWbHYIxkLU6IM90ghV8QyTCfnPnaDBfkhAavmTg8YnzgHub1Ui1fN0t2USoX41WJ5AoSaW3AJz3n1qHW4YNuTzSu7MyKAT20LwAhvgDz0h_WipdAarMY2M7WYMbJh70" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
بااعلام خبرنگار باشگاه الوصل: رقم قرارداد مهدی طارمی برای دو فصل حضور در الوصل معادل پول خودمون حدود هزار و سیصد میلیارد تومانه.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/28250" target="_blank">📅 17:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28249">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2XFLwN9fDqxD_2BhpFSgUuNiEJT7S2DEMteMeQ_2Ttf8VXdEXh17C6qfAPgjySk0tdZtuC32Z6OyQmzT4sn-WBAR4lvDXHTsl0QkYBddhCcsbFAK2jMsKPWVUhvQiuL3g16k7-Evq1JT3nVWfPwcNsKn1CpyxbrFsqqiGn5Df-sbvpxz1MVFHiHdxr-6wJ-9Ijsc3N-Qjr74CBEN96_QialvW7ISu7LNWiWnli-KJ5M9lQjZPgYkIa3LXHMb_GJpZWLgxKCMHocFDNxN31QHPhxV-LPSRUSuYDEwQxYaiVhIwEVvU4tCnWapKh9W3y3L4Zowyup5tB57iHdqW1k0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28249" target="_blank">📅 17:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7653009269.mp4?token=kyzs_4seHR9HERZexpKY0_aC6QFSjmEsrmvZL4UItSvMFgk3_fGKOxx1Xwdz0eQys4BnnGzuFTmUW2-R7P0KSm1p8l3QCGJs10omlarkkOUt3OWjWwM0JtSd5xKl4ulc07ldvcXUqfbSV-6utKU6FvTJpWvDR3J3WF4ulq4vT_gQF7k00RIz1zgeu70jacra1ZR-l9TQwQ-7jZutjcuYedsATQCfU8RcUvBkKzJcLn0JEWTlxZkEtHWqEkxX_u8v3KYW14tKWYYvSecsnzH2USXL3PxztmTe5-2jmZ9mMu8w2gIhU_TPepaOFZHIlOTqgQO67lNoCS5-J6IGhahZcXYlrXIUbXwB7yCfetiRPL0-FWRmjRvfOrGLAPC39usvpaQqJWY7mEjbGxcnvOFoISZbPCvlHEhICUNqfEpbCLayhDhx8sL0MWwTmOe2ebYjmr-dclGaJKsGAZ5eiasQHq4cyIml51WB8GjEG18EdUtklRsU62WojadpwrlPu3261fgi3xb_ULRbdt4l8LUPYKrHzqNNOiD801DpGhk7-kO1Eqecy6H_owbrUFf8MrYSWjzv6UJJgH_NJiz7tzthtEI3NMXpQf6bYHRFJ-LM-gIlf2KJyB_DRwjLzxjVTMhYultdiZl80zeqNFyuPJGyp366LW53lWrrzHuXhUKjPqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7653009269.mp4?token=kyzs_4seHR9HERZexpKY0_aC6QFSjmEsrmvZL4UItSvMFgk3_fGKOxx1Xwdz0eQys4BnnGzuFTmUW2-R7P0KSm1p8l3QCGJs10omlarkkOUt3OWjWwM0JtSd5xKl4ulc07ldvcXUqfbSV-6utKU6FvTJpWvDR3J3WF4ulq4vT_gQF7k00RIz1zgeu70jacra1ZR-l9TQwQ-7jZutjcuYedsATQCfU8RcUvBkKzJcLn0JEWTlxZkEtHWqEkxX_u8v3KYW14tKWYYvSecsnzH2USXL3PxztmTe5-2jmZ9mMu8w2gIhU_TPepaOFZHIlOTqgQO67lNoCS5-J6IGhahZcXYlrXIUbXwB7yCfetiRPL0-FWRmjRvfOrGLAPC39usvpaQqJWY7mEjbGxcnvOFoISZbPCvlHEhICUNqfEpbCLayhDhx8sL0MWwTmOe2ebYjmr-dclGaJKsGAZ5eiasQHq4cyIml51WB8GjEG18EdUtklRsU62WojadpwrlPu3261fgi3xb_ULRbdt4l8LUPYKrHzqNNOiD801DpGhk7-kO1Eqecy6H_owbrUFf8MrYSWjzv6UJJgH_NJiz7tzthtEI3NMXpQf6bYHRFJ-LM-gIlf2KJyB_DRwjLzxjVTMhYultdiZl80zeqNFyuPJGyp366LW53lWrrzHuXhUKjPqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
هفته‌اول‌لیگ‌جزیره|شکست‌عجیب‌ودوراز انتظار شاگردان مایکل کریک در ایستگاه نخست رقابت‌ها.
⚽️
هال سیتی
2️⃣
-
0️⃣
منچستریونایتد
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28248" target="_blank">📅 17:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNZVuiRLRQSKaQeYF8OkpY65DQHYWqdXG25u8ynWKQIfleiF2KssUeHk1ralU4D-8UfbsUT-CzAbcC0YJcfIFubjeEIxK9F6I7MqX58lNiPijGLYbN2QHDT9w_qbUlq_5YET6FzJzVZ0PJ9YeZbCw8KMx1V6suy95UyE9D7r8nF0pD4n1VGoeYzVm-WudZr7u96gSxd3iM4DSrQBFgq7ocgOQTD7l8HdV_fiI12offKiOw47zDvxYJPk3YCN3xgmp9ftPFnIgiRvtc7vkvJGj5uPvfXNgi2wRZwIwN_Nhi8f_6jXPNRO9R079AX-v3Sef-bQnirEk48zNdZEhHXnGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
هفته‌اول‌لیگ‌جزیره
|شکست‌عجیب‌ودوراز انتظار شاگردان مایکل کریک در ایستگاه نخست رقابت‌ها.
⚽️
هال سیتی
2️⃣
-
0️⃣
منچستریونایتد
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/28247" target="_blank">📅 16:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbZ-4iEdgPtSPwdhQNJeQ8mlC1CY2YcTX4OMxl9xz5_lyPdW1cpfNS8oA5gATxVBFC4BC7Y0eAuLRYHBOQOiB1UyVM-q_6nNwJRI_yU2z4mW2rACtKVvD0sBcm5OQSaWR1fw298biG2e0RYR2Fgh_Jqm3bRacLNWlRy3ghKmW3GyCr4pt_7xaYH6cZaNtvJQ9BkMrSYmoG_YRxNMKQ4t3dMPPSL90F03M1zeDMVdhGPYihy2bh-gGpOkQKoq7doTdEvDHucchnjAczhmPaBMwb1IlYyqrZvweBHDA65tauje5CxZ3ysFJWQoHYWPC0fL8j7Srh0O3osE2FQ69IMS5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعدِ حدود یک‌ماه از بستن سایت و پلتفرم عادل امروز پلتفرم ایشون باز شد و از این هفته دوشنبه شب‌ها تحلیل رقابت‌های لیگ رو خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28246" target="_blank">📅 16:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UOjE8kMIPO2iwckTA0ZneZwj6CmzTy5vhVK5Ckjl00NdmjlYmUuF-jwt-CacyB57bFpRLMISyLE7WdDwuMg0LVnWVhtsCcFcKdTIY5DS880SMv-m9lAbETuSMSwORk2Ub2otE3Qf8R3X6-bh-vCMil-02Iz5DueJCD7fKCp0-DadZqi5WR4Y4papt0uiZ7mAnHcy29W7mJ9YSQCqqhk1Y4VkKYOu_6eBWKIK-xi4ABNwOGygYgC4MUD_Ij7bPeA7q_VyVmgJExneV0t9GOXJddA9dx6Ht2U91mE6k7DqExLJ3T8LumMC7GBXBlzbnMd3hq19Q-TE2CeoyAOpC9aQAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌های‌اماراتی؛رقم‌بندفسخ مهدی طارمی 500 هزاردلار ثبت شده است. مهدی طارمی پس از غلامحسین مظلومی، فرهاد مجیدی، علیرضا نیکبخت، حامد کاویانپور، ایمان مبعلی و محمدرضا خلعتبری، هفتمین بازیکن ایرانی تاریخ الوصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28245" target="_blank">📅 16:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/laHcxb4UNTNz-L3Qy_rx15KCkNBzCuB2sNSaZ7mDQH_ixmYbVFfUAiZk2XEhWn1Ps6EWASZA2JTwYdgrmfNjz1keQcvuoFIODc5Gn20dGgt1r3bqcOLoLRqWpxz_a1AteFGyivrGyrBzw4MNLIfcXtcytbI2iMjMcgL8GHDaSDROldtkQAKUCBC9HoU6tEpfOSw4GTWmmfbnD3KIs6-Q8ubDYjMNsZHI4T9hwSV-nHTyUtXBG-94-F1bgD-MPXZ4tApMG-v78APUV4SRBhQuGsihF_p9nXmGN6RnXj_rqaWeegO9N9j8E70Lo1BLXnOx82ra6FzTxYCwlSybr-3e_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
مهدی طارمی ستاره34ساله سابق تیم اینتر میلان و المپیاکوس با عقد قراردادی دو ساله رسما به الوصل پیوست. الوصل یکی از رقبای استقلال و تراکتور در لیگ نخبگانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/28244" target="_blank">📅 16:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28242">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHIbyG405fYj-5emjWZylzVhO1dBwVrXCfnEcBG3XS1WNYhJyY3nlIpWyHtcSwtoWHXczrYASgJwrGtMXR76lTd5UvLhehRLFKlQsFn4bG3zbwAXsvfOeihPoexgeYY6fwH5GP5f8Bfq-bhTmvPIRe-7OHtd6lrRWBjMF2bT1xvZ3rBfGdUUHGM5uMIBiYo2Rzp6YPZPdNlaFtnCmmQOitFAB_UYJ8YFeSpZYqB80nMa-KEuvDXkxda3qkwOYzq8iW8TjIQRFm8yGEa2kSrK_sp9-q9ahn_vxQrIUREI5H8ZmC0LgsYbXjUqclzPDq-v_47p7urOFd1HNF5GC5WdfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ob9awtWmpH6zh4a0Gx4UC9_vVfRj73mDqKx6GHFNfxfzsmg_rAKL-8CIi05KXAvRNtx-ztZLOoJz5XB_BbBcoFgiQCsTXgmRpLLbYkK029J7-AYDper3DDVmoBWuYWAp2jrEPtGzRosqFHtnS6JipqRnSfA6HNOcz3acdBp3wKCHJ5Wzq_f4m38kBtDdheq4L5iKBvOq9sFk0SktANWVdv1v-5sv_rYNrFpRCYq3HCcI5IFy20fQUBBKdJ_6SgLO7Gr-UaB40KxW86mlRUT8jST2WwoF1gXvBPr8WAKsl-tRxeK_P49BxqBkALYloKG855S8ShTZn_dwOMGfcWXK2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
رسانه‌های‌یونانی: باشگاه‌‌الوصل امارات 1.5 میلیون‌دلار بابت رضایت‌نامه مهدی‌طارمی به باشگاه المپیاکوس یونان پرداخت خواهد کرد. با خودِ مهدی طارمی هم 6.5 میلیون‌یورو بسته‌اند برای دوفصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28242" target="_blank">📅 15:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28241">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QfxSVZOh4HLwVeGMqOKuk1urLLhiTa55N3c8cas0X8Gddgk36UjOQk_YhPuFvcFhGWtzQ62GE-rVBlMLMDRiKZM59SyWl4_z-v5GRW9suD9sflPghJ7DvFrUCvQdIJkuzzL0AMQWMEH7cStz0R7wbxRtXM1f2XcA1feNV0dCEvcSoLcQGLI_V9cA_vSYctl3ZLvJ-RJaN2hX2SK4WR_nLvihBavp-ae3YFfsDg7jwiAsqejmTjrY6XzqZ7cSEH8vli9T3BFXLQgwkKTwSvp7_BakRHbLYlDjtJXBZ8tSz7cOWwEnnPaov5FWAnwuwJqUgZSOerSde6aGhgovMFEXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بنده‌خدا که یه دوخرچه سوار حرفه‌ای بود و ۱۲کشورجهان‌ روبا دوخرچه‌رفته‌بود و هیچیش نشده بود روز های گذشته تو جاده کرمان با میکسر سیمان برخورد میکنه و جونش رو از دست میده. طرف هم بجای اینکه تلاش کنه جونش‌رونجات بده فرار کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/28241" target="_blank">📅 14:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28240">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9j7tRY-7fMNbesvsP0uaYgfxLG6CbQqzcF9x3y86l8oWmM_7_hV4qmTKRZDJSAuaSGUR9u6A3nY4kcb4hV5r40kPFiLJQujwxdrc5l_6ZmIY3JuZaXjPyE6VRWADuRrn2XarHxAY3UEWb8_hRevYhRhsk5H_SOA9EwrEh5jzyKthtu-4iN2XU6UOhCJ03mIsX8fd3tKcNAh42g_75w10mWLfpXw2RtdqbPWL2UjBV5080U1sP8FJhP-Ootnh89mK_5H278pmC2ptclla_oX04ytbeLEBgortU2tWGPBSIJ2mAhfk7CTLXBxGjvIQJFDtTwSv_GamuRiG8ZYH3RS8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌کامل‌بازیکنان ایرانی در ترانسفر مارکت که فعلا بدون‌تیم‌هستند و در مارکت بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28240" target="_blank">📅 14:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28239">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZnLmJVcUMwW1s8SN1FS8B85quB8_-CMzH-Ko3qG1FbEmB4PXSxr6OlsDe-s9tps7HJI7o8AOGnK8J7tqICRV414DGWC6-FKw10Lq4MbOnwjwM6rwKTeYvrDgE2wa0V_5PvrvyvFI69HRjUjFpFh58e6awcYx8gZ6MJid5FdOaKD1A6sddQzARoIiCX5I0ih-_cUGJXd0UUxEWDNYIt4QEha3BD3-yPSiRvCKcVbJd9ArzsEVo2qQ3w_zAmUUFnlw0swO7NSsDmTkNtwTQ6av9MxaqmJZhQuAZreOvnK-O82CF-8-ZqC22msZLWHy9w8yc0WJ_m2F2OLNvCRcWQ5-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه فجرسپاسی اقدامات لازم رو برای جذب علیرضابیرانوند انجام‌داده و قصد داره از اول مهر ماه این بازیکن رو به خدمت بگیره. بیرو هم درتلاشه که با پارتی‌بازی معافیت تحصیلی خود را به مدت دو سال تمدید کند و در تراکتور موندنی شود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28239" target="_blank">📅 13:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28238">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b1fb0883a.mp4?token=MJ2z80ft2Jd6J1cQXXINGGX00hHrq-vSY7cHu19rPKsIx7WUb4K58ZUs9O00FIcUqZSzC8B42hAyns_SwS1sDFD3REGFAKq4sRHvp5CU4brUv8Hkj9NfNKdVC1j1RMemcoqj0uKNwyBuE03X28ZDxpjLm_GFz2NUIBs7wbbKFnPa530T_k4pG-B02-ss6aeBFtvkO1wtaNZEXtigebUSV0aTV2cpqOhvQjvLwtulRnSemXobSpmHpnPqzoRmCd9C_N2vFVpdCWieWUYGtgXRvlU6Gz5QpURmJKkFDVq4n0gKPIEllrGivigarf6BetBgiZDpAeVxnkNf58NTkl5uLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b1fb0883a.mp4?token=MJ2z80ft2Jd6J1cQXXINGGX00hHrq-vSY7cHu19rPKsIx7WUb4K58ZUs9O00FIcUqZSzC8B42hAyns_SwS1sDFD3REGFAKq4sRHvp5CU4brUv8Hkj9NfNKdVC1j1RMemcoqj0uKNwyBuE03X28ZDxpjLm_GFz2NUIBs7wbbKFnPa530T_k4pG-B02-ss6aeBFtvkO1wtaNZEXtigebUSV0aTV2cpqOhvQjvLwtulRnSemXobSpmHpnPqzoRmCd9C_N2vFVpdCWieWUYGtgXRvlU6Gz5QpURmJKkFDVq4n0gKPIEllrGivigarf6BetBgiZDpAeVxnkNf58NTkl5uLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سهراب‌بختیاری‌زاده‌سرمربی استقلال: نظم و انضباط برای من از هر چیزی مهم‌تره. فردا علیرضا کوشکی رومقابل تیم‌سپاهان فیکس نمیزارم تا بفهمه اینجا استقلاله و نباید رفتارخارج‌از عرف انجام بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/28238" target="_blank">📅 13:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28237">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21259a9796.mp4?token=Zy-5gyvruTbxiPAAzrZn8YgfM9rRNUlI2JxhDE0JmuzrFlQRWK3S0B2embBhYtiKGrt7i2bYxj4yi8hcnS0oT3ONnWDGo0AAsKrfjdhogNp0PEnok2ZjQgCo5lyIqg6Qo1G0LFUO5itLdGASfLjnSbqYn7DjU1vOJIuroeD4IuTF7o8P1NFctd30qzE_d9EBnatC3CA8Sj35K-ynmrZ9XYG85O1JZ4TYLyRy6XoQIz6wKk6L21_W5oZmMfmjjnE4xivugvO-njPXqVZqlk87SkS5dVMv282NTSqpQ4fXzIyIM9r_X5MbZ7Qld9_tZdw_ru7HSlhfI0_CtYzxMV-IrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21259a9796.mp4?token=Zy-5gyvruTbxiPAAzrZn8YgfM9rRNUlI2JxhDE0JmuzrFlQRWK3S0B2embBhYtiKGrt7i2bYxj4yi8hcnS0oT3ONnWDGo0AAsKrfjdhogNp0PEnok2ZjQgCo5lyIqg6Qo1G0LFUO5itLdGASfLjnSbqYn7DjU1vOJIuroeD4IuTF7o8P1NFctd30qzE_d9EBnatC3CA8Sj35K-ynmrZ9XYG85O1JZ4TYLyRy6XoQIz6wKk6L21_W5oZmMfmjjnE4xivugvO-njPXqVZqlk87SkS5dVMv282NTSqpQ4fXzIyIM9r_X5MbZ7Qld9_tZdw_ru7HSlhfI0_CtYzxMV-IrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
تغییر چهره برگ ریزون و باور نکردنی رابعه اسکویی بازیگرسینما و تلویزیون درسن 60 سالگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/28237" target="_blank">📅 13:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28235">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ciqTnbK9-v_fzYty-Z34nxnUas4IGD6C8SSbczIdjovSmA0y4e84Sx14-cctsKwluvhRjrIg39bZAJXGXI9uwLgN0pn1lTBwCxphC6H2Ub9pLWCh_X7o64ho7JO9C9gr5-dljzkPmO5ZaRRIiXL20BqZMTDoiGoYqHBaZ4S_1e91uYdWXW1u4Vr4D3je0yhjhvQFQ0Bm7Zwzo6ssqbdNZFdxk3EAIodLNrYEoUu6IIxBxr-r2oJhI-bnsXVYXfX5sQJIQNJtEF5Fm4_iJ7vVieGjd_-nURcQQzE0AsZkKdre4nEMZAesIy6VfFMoG4apEpmZi41jvMPkG7mRJ_yCHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رودری با پیراهن بارسلونا پیش از دیدار با الاهلی مصر در جام چهار جانبه خوان گامپر؛ این اولین بازی رودری برای آبی اناری‌ها بعد از پیوستن به این تیمه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28235" target="_blank">📅 13:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28234">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s88t43r9uzgGHGZ5cCP6a4J-Rky6ZEVr1y8E3zqrPNQcPv0iS4ySRcKuBr3m3EP9YC-KlABzeEwhGBXTQLAoAt0z3uKdfC0qI2ASt7pXaEDU7u1vA1cJm0RB1tVEU8Jkr4Iqf2G4HUiRfpe18PgShPNB8NtgoAS43KH6cNETgKtF4h2pdUaBUY-z8tTaEVwwnWq7QXFeyhgkZqM8D5aJ98QOQJscrat2bDt8KwV726C1z-M95UkHbbwEtw7nY6deNi7FyfRPDug-jZU2Btu34sCQu2ZD6w2yTYoWv3ic4J8kEqiveEIpEUFJSdMJkZWO3zxYU7HtOeIMpbLzh_KsHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
مدیران دو باشگاه تراکتور و استقلال به فدراسیون‌فوتبال‌اعلام‌کردند باتوجه به همزمان بودن بازی‌های آسیایی این دو تیم با بازی‌های آسیایی تیم امید هیچ بازیکنی رو به تیم امید نخواهند داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28234" target="_blank">📅 12:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28233">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CP2MT3JA8zE1jt018ksgBlZiyZ1Hjmq4fINrM6exNL_gN7ZBtJ3KWn8GNdTStkb0RaExj81bgdYdaEANTCAQmcpkFn5nKlIUWJZ_v_7hasWPC_8bEhzU1bVxowkB3zPV0Tqok9_tuLquAbPGHmJi38wzF8FCElY4ceL1BV679Uq8lRnxJ73IdQBuiUoZoZHUjmFZJ4lAZAXww72bHyxSQhfj1lwadt0zbHlQmpdY_T0BnuysjBpJ7QSXYvhjGtOZVSxnkJbGUIZMEYgcGNBlInD3nNj6c7V6vRLMAb6DrK7nZ_bbt8cxtpZaGxVGH3nFvXf_RmAgbnYD5qzcPrfR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سهراب‌بختیاری‌زاده‌سرمربی استقلال:
نظم و انضباط برای من از هر چیزی مهم‌تره. فردا علیرضا کوشکی رومقابل تیم‌سپاهان فیکس نمیزارم تا بفهمه اینجا استقلاله و نباید رفتارخارج‌از عرف انجام بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28233" target="_blank">📅 12:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28232">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7zXEXXqdgKHgJ6LdmyvrhcZBf-xNg_rtvm9iLonsSkaC6Dkfe5ZDO7OrV--QhGq6sexM-5ZKpdoaqK6_0-YA9eHJ7rR-fhejPy0-uVa5gMqLDHdoFdGzo9mpaeataLhSjHilrfgMY_F7LQ2k25kVbXlawx3AWu2tE-NCfvEKp1iZunqziXhw-TEJbCL0_OhVpBHKesYFTXUmQBghTwAMpMkYdqs4ltCBmxzzBT49cM97GNbURpoJPXV5CbYnIJjsvQVnXInwCIzOD14jX2oVh8jXywTOTtnN4ycfjOu727a7WTpT7qAsjHj4o5L9JJKq0c18G9BlBkNgebWREYnAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
ژائو پدرو مهاجم برزیلی25ساله تیم چلسی قرار داد خود را با این باشگاه تا سال 2034 تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/28232" target="_blank">📅 12:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28231">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXotGEwyrKHHVVFOaSGZRHpVA8NPHU5kVE3JVzFBreJgDeZRt9iKgDWAmV6sD3mMBY0v_w88dVjIPCkDq4vKJ3o87COr5cy3yf6Il5SmXD16pWekAWhku4xxr9qm6-8lFV84bf8nmn3TEMLAnf4hOngffTHSnvNlQdWqf3jy0hJo6PODd5D65bvLGivefiWUgkkTOcpXwTAW68Ce9Sezs7fWajWeQ8Esu8NX49151EqE2r-yzjKMfWGCLrPr7cLyZ93Sp1kQ0dDARZDI4kVCpfD89Fgj9g_6va5jiiqY5ItokC30hT9DCKe07bUdlH5fpnW90a8jS0ATASR_TRi2Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
داداشی‌های‌فوتبال ایران؟!
پوستر دو باشگاه استقلال و سپاهان برای بازی‌حساس فردا شب دو تیم که شبیه به هم طراحی و منتشر شده است!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/28231" target="_blank">📅 12:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRd3jnWtvzDog8QIWguDS9qTSsbpsARVxG55WMQBhoQBaH8O0GHX8eaqqlsrNNTTl31n09W2zCPwbwBfwImG9ABV7Zw1zJflgE_v8ro9W_R6h8BlHwcYy6I3qSZkaoMbUlsaAPtg-J22V28so9wLhmVXbT1ZqleQ9zdzITIx0QCUSdDO93wARQ0f5xMb9qU0VTjQDVvb6i2E23B63I_0bOt4Emb12mySih2PyzihUGzi1wRzzhFmzIvPpImS64tlDqCIgI4i9txKme9hzkFd4RWL4-c9U7aFk4xCOq0CgMksHezmAVbWm8k3TsIsoSEwMmzQ1YTdxjmP3Ks_KuNzqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
درشب‌پیروزی‌شیرین‌چهاربرصفر النصر مقابل الریاض؛ کریس‌رونالدو موفق به‌گلزنی در این مسابقه شد. این 977 امین گل دوران حرفه ای CR7 بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28230" target="_blank">📅 11:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XPJ2qmyLfxjfjMfuBwmFQLO9m1pKUoVSb24Ur7n1ov11lbBwIAoayaTOGFeQGWVdvno4-j5jWtu7vN-UfsI37v-K0W9SCkmEdMatS2AQT3oxIdteaKCe8zHLGiOo5f4mdwqH4CsGeFk5iVpZPh_b_7zU2srY1jT4_LAU8dwX2lJuNcC9P8H2Vez_nz8UlvGWPT8voYgGIExMIxx5cv-SDYOQqIe8IZiTVZJAHye2vkWtjcS5Yyge9nOkyChNlRX1b-fbMNOUy-r9R5Rkzb6bi-CsrLt5V0pYVQdHYAB0dwqAI7zSKKSm9bLJvEbxgxjsWXGoRRMIlcKYel9wDdSJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
با اعلام کادر فنی تیم ملی امید؛ علیرضا کوشکی، مهدی‌هاشم‌نژاد و امیرحسین حسین‌زاده سه بازیکن بزرگسال‌تیم‌امید برای مسابقات‌آسیایی هستند و خبری از علیرضا بیرانوند نیست. همچنین تراکتور و استقلال گفتن به خاطر تداخل بازی امید با بازی هفته اول این دو تیم در…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28229" target="_blank">📅 10:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y73QhBpRjiF0SztqUG02aU7tho6I9vjfj6TsQFLz-srH0b9EhjTFMeqDgSqooAvsX4L4Puu6so6eOTXwTD_45AqR8nQOlYNXXrss0GAJWfsOhx2yru43qE3gEXvMBwuVjThLSTEXLgXIdO2kHCXUP7Cv4X135gzzHx6y0yGao3YF97PnsWFa8th7AJ8KN2c3X9f4i_MdSKQGd1cq93pwXER-RTYsrpxZ2RaZohkPL6hdylV4dLMwtfq_vd_fqTxG6igySoNA3FTo5wJljOumpYhQzJmJNTgiZtzRKT97IwhF42ujgTph7y2VcD8bPEKdZDQe0l4IYYE5KAJHFR4zZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ سردار زاهدی معاون‌نظام وظیفه عمومی: علیرضا بیرانوند ازمهرماه سال 1405 سرباز خواهد بود، و باید ازیک‌مهرماه‌به خدمت سربازی بره؛ زیرا مهلت معافیت تحصیلی این بازیکن هم آخراشهه و بزودی به پایان میرسه./ حالا اگه یهو زدند معافیت تحصیلی بیرانوند دو ساله…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28228" target="_blank">📅 10:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a06b6F2eWnP_jqGfURoL3rWGv5HuPcZTUo_H50jGmW-B0Q2MOTTJh9a39PYOcDElsCWK-DyueYaQ2WF-jJbinz4P-JUN41vs0Pqy4b285uni1WoEcEYtWpCFfHYOM3ba_cwg89OqsrmZzV_esA0kR9QoWQar94ONUQ7a5I3vzuHgTx-KxGD1Gbk5OjlyhoUICfR-LTq6FEhyMb6C0BfT8pq1ps0hbQu0PIYck-W9rgC1OTk7fXd5JTQ5f3V-mJxV5Cw_ZcS9NUaM_ZShHi2Nk2uv-4bcB7hqGB6ouJwjm9kMLF3STMB_PyovUVWV0U_dYNafpDSVzjJFVvP5nkDYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یک‌باشگاه‌مختلط در تهران به خاطر مختلط بودن و کارای +۱۸ پلمپ شد و هفت نفر هم دستگیر شدن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28227" target="_blank">📅 10:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28226">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpOWE5AFS5yCY1Znlv6fu59TomePcbMqdHylNfZxaPbiKA5RL0V99pu0GpR5tPvmthbUK2N6rwJu7IaIQ0inKC_N8s7eWvi0Lg74SQt1RmiRZeBkj9IaQ3ceoa9uKbHYvIOhHqLoGG4V4-yenZiEQkBXFtp-enNwf5lt1tODcXNAinfJrH5FabGy6Puo_04TaEIjFDySyEMMPgwUEXNuwG-VVip3sU01t38HGnXvmjRPJGCuFW3ywxTSYOsy2yniS62oBYzTulaCu_o4m42yQIJy9afMssr0tJSlA6kBApyZUVAORiu0LYfYaDAhk7sr2dFpiyjtfXxkXKd-HhIu8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام اسامی داوران هفته سوم لیگ برتر
؛ پیام حیدری داور دیدار استقلال-سپاهان شد و امیر عرب براقی دیدار تراکتور-پرسپولیس رو سوت خواهد زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/28226" target="_blank">📅 09:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28225">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9413e45de6.mp4?token=LVWIQIPizRGoJg0pcpUO9-fs9gJoPDLXv6_SIUFwDiXXkB0NMMWBfFLEg3s6ijHTNPZ6soydcPY-xUCJsjKLDAOaORvbXvbhD5il3AOeMNKCpHrdZ54bm_AExZgl3t5TYMUDOogPCi2OsIvJ7lhrwOl_Hpj7RuEhScJ1nzW-anl6wvxc0N8fTeh2Q_YK84rSiVI7zxskTh0OChxLoflqyxm12gSLUeIoBmqvpVm6sdP938dX5qDSMGWGzZudiYUgW-S7B8JZAwjbgh_MqlE12bgPqVFME8bpTgzfShBH-wRkX-gACtWCnkaN9_5OqkHr2kayrSC4hKmBBH-kNmAyrGg3dgJWy380hVxtFMXz5nI821tZgUs4oXtwa8qUCiTM7V051t9AxoweSXRrxE-Xj_yHX9_PjLUE6fTRzxAQDQPcw2GnW5GLjmLt55o3jZEZCwmxVlOfrwwBebfuangu5Y7aX7waX3l5pkatmAHxDWDl63Nxx0_8H3fO5L9bubmucd0Ln_s2MHziHuSnpHctWRR4p3NEzjtX2N-XGON4wT0XHICuB9eRHsQbWY2HsqFsrJIbwQFy6hV2JC67v1AzgeAnoMGiTcbTTDaD_b_QApzY_zTVzkOHrj-Apvc3HjJaNjCWPFlfCcxOShTWLC88XhpxAeH_R5Z6V2igliRtMQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9413e45de6.mp4?token=LVWIQIPizRGoJg0pcpUO9-fs9gJoPDLXv6_SIUFwDiXXkB0NMMWBfFLEg3s6ijHTNPZ6soydcPY-xUCJsjKLDAOaORvbXvbhD5il3AOeMNKCpHrdZ54bm_AExZgl3t5TYMUDOogPCi2OsIvJ7lhrwOl_Hpj7RuEhScJ1nzW-anl6wvxc0N8fTeh2Q_YK84rSiVI7zxskTh0OChxLoflqyxm12gSLUeIoBmqvpVm6sdP938dX5qDSMGWGzZudiYUgW-S7B8JZAwjbgh_MqlE12bgPqVFME8bpTgzfShBH-wRkX-gACtWCnkaN9_5OqkHr2kayrSC4hKmBBH-kNmAyrGg3dgJWy380hVxtFMXz5nI821tZgUs4oXtwa8qUCiTM7V051t9AxoweSXRrxE-Xj_yHX9_PjLUE6fTRzxAQDQPcw2GnW5GLjmLt55o3jZEZCwmxVlOfrwwBebfuangu5Y7aX7waX3l5pkatmAHxDWDl63Nxx0_8H3fO5L9bubmucd0Ln_s2MHziHuSnpHctWRR4p3NEzjtX2N-XGON4wT0XHICuB9eRHsQbWY2HsqFsrJIbwQFy6hV2JC67v1AzgeAnoMGiTcbTTDaD_b_QApzY_zTVzkOHrj-Apvc3HjJaNjCWPFlfCcxOShTWLC88XhpxAeH_R5Z6V2igliRtMQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇦🇷
ویدیویی‌کوتاه‌وخاطره‌انگیز ازحرکات دیدنی و محشر لئو مسی در دوران حضورش در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/28225" target="_blank">📅 09:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28223">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bv__OhyT0G-cHN7AsX5KIfbvfTmwPkDHNJXizpDzDXgLtkqaEu38tAfE6SlzwmFUKHc_1HRUHCbfBY9YwnJY-lT5HVRgs19Hc_Bil1mwyUCM6tHMSYG7Wg892hi_zIJEZXe4RltqtN322ga3KBVPT_hSeqnla4wSSiapH2cuNZmMDhy-nkOKV1UWgydUhNW9PovrsFzjOgASw0OkpjEKZbK5WuQ_MnoHckWwauJXd9-iXn_RP9zEum_Wm1EtvksZ28tfZFlxL_ToAyUo4MwtoXcxwADihzdQ29FNw0R1JAOqgzKz9Mr9FxEcLMOtE6JImRx4IqHxi0_H0IfUIrojLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد حساس دِرکلاسیکر در سوپرکاپ و اولین گام آقای خاص درفصل‌جدید لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/28223" target="_blank">📅 01:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28222">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbSYD8zUqKa7LOgbbIKXp1Jij7jOWIYBdx-f72RngaDtNXRJECSKRmsAxP98YGi_Woz2h-31eu645WLhtpX7BHy4LNHn2KRK6Ztm9bN84w4dMi3PHbn49uLIah8Kz9xay6KGglSU3vii2inIpioFhFVEp2LhFN5yuXNU0l8NdDh68JgoibpEccHDYLS8lC3f0gT9zewgHOxLHihvKmSymn8w_RdrUrfXJ5TJ2uo4MCPdGDUQs77ZLpvrJO82Us84DxF4sGgwL4MfcHG5QRkgm6OS7LQkpXQhZy110NvKglfxwKTkLCXxLNngviUz-i1eWhN6xaeC5xqrXa2o8Zq3og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدارهای‌ دیروز؛
از برتری آسانِ آرسنال تا اولین گل رونالدوی 41 ساله در آغاز فصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28222" target="_blank">📅 01:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28221">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=iDXFdzoA75CYgyOSFyIl_0WsTjG-lPMWfdz3Yo6Oy__eLCN-lBeKt-UCxem2XOxweK8aGYvJZcwPJaPPGXTavsEg_L6oxx2_yOYSQIARHoVyWRemsM-j-_l8ZK-QDQcBQz1VFYzL8egy_IybbvwxDDF4ld4KwObf509886m_PWFX0GnBBYr6shRHA1bxECWkBHHZjOl9_bAFeYoZXXgSU_CK7EyOodXUEraSbaKrU02jmTBvedPTQQkJdu8QqPBfd2gwI1Kb1wrTxlNYmhEgqeGFbClcISsyFNz9-HHT2y-WNXurjdQWgLHP1sl8UQzPWNs-ab6ESB3Qwhm_9Tnz7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521128dbfe.mp4?token=iDXFdzoA75CYgyOSFyIl_0WsTjG-lPMWfdz3Yo6Oy__eLCN-lBeKt-UCxem2XOxweK8aGYvJZcwPJaPPGXTavsEg_L6oxx2_yOYSQIARHoVyWRemsM-j-_l8ZK-QDQcBQz1VFYzL8egy_IybbvwxDDF4ld4KwObf509886m_PWFX0GnBBYr6shRHA1bxECWkBHHZjOl9_bAFeYoZXXgSU_CK7EyOodXUEraSbaKrU02jmTBvedPTQQkJdu8QqPBfd2gwI1Kb1wrTxlNYmhEgqeGFbClcISsyFNz9-HHT2y-WNXurjdQWgLHP1sl8UQzPWNs-ab6ESB3Qwhm_9Tnz7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حشمت‌مهاجرانی‌سرمربی‌تاریخ‌ساز فوتبال ایران، به‌ثمر رسیدن اولین‌گل‌تاریخ ایران در جام‌‌های جهانی رو با روشن کردن یه سیگار جشن گرفت
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28221" target="_blank">📅 01:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28220">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80639b9fd3.mp4?token=rmVQ61bFDITH7aG46aL74KraB6kDBBXtYVKoTLd6vnXneiGHYZ660kTa4-St5XMwQSpVPxYX6ExLviAKkg7maOcEVf4x1d7s_0lP59cAb7MpEghCJDwKKe8vmjsUJH2j8lTDqHMv14s2eH5B7L4kNjdfP7jy_pjT04ge1xBm8Rmjo2jHRPkqsV6p-l6NoVrbwSdO457GhLGoXkQHyFbPZFngKSKVv7xPAHZHQnNyxN1GVPCBkemyNL20fjepKphx5KpA8iP6DSpk0jefdIToy_MyPLKriAUhzHtiKbzw-tUSCyJVRRpeytnHHZ3_QIMAoJvCC2YtP9Xlvw3HwHTEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80639b9fd3.mp4?token=rmVQ61bFDITH7aG46aL74KraB6kDBBXtYVKoTLd6vnXneiGHYZ660kTa4-St5XMwQSpVPxYX6ExLviAKkg7maOcEVf4x1d7s_0lP59cAb7MpEghCJDwKKe8vmjsUJH2j8lTDqHMv14s2eH5B7L4kNjdfP7jy_pjT04ge1xBm8Rmjo2jHRPkqsV6p-l6NoVrbwSdO457GhLGoXkQHyFbPZFngKSKVv7xPAHZHQnNyxN1GVPCBkemyNL20fjepKphx5KpA8iP6DSpk0jefdIToy_MyPLKriAUhzHtiKbzw-tUSCyJVRRpeytnHHZ3_QIMAoJvCC2YtP9Xlvw3HwHTEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار از ژوزه‌مورینیو میپرسه؛ دیومانده گفته حاضرم برای‌مورینیو بمیرم مورینیو هم میگه این یه اصطلاحه من که دوس‌ ندارم این اتفاق برای کسی بیفته ولی کاش میگفت حاضرم برای رئال بمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28220" target="_blank">📅 01:17 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28218">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5613ee8bb.mp4?token=vc3aUD6sl0fvf8XgruNDGqjjAh8rGVmbxjrfvW3Y7PwrPIfQCEAVonWpXQAMs3B1noRQqY-kypIDyHDG3DGv5dOlz6dV34qfEuekfJtr_S_uTDwlnMqNOWycEZA-6pee_dULYVve05-Nim5MKf7bmjA_Zj6Txx4BQwfcd8sZBlv2quNBZswZk2B9uXt_17y5nHdcVNgtIMV7_JHvZk7v7p9_5i8n62X8oYY1SrvlBISiGOa3Tb38ieKgebrQLdtjr9DTgs-mIGg_9wiOGEqeABfsJ7EYm-n4PQtHaonl8k8282S3O6asxJN0m_bWhNOK1JaEYiNRWWBNPNvv4bSJeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5613ee8bb.mp4?token=vc3aUD6sl0fvf8XgruNDGqjjAh8rGVmbxjrfvW3Y7PwrPIfQCEAVonWpXQAMs3B1noRQqY-kypIDyHDG3DGv5dOlz6dV34qfEuekfJtr_S_uTDwlnMqNOWycEZA-6pee_dULYVve05-Nim5MKf7bmjA_Zj6Txx4BQwfcd8sZBlv2quNBZswZk2B9uXt_17y5nHdcVNgtIMV7_JHvZk7v7p9_5i8n62X8oYY1SrvlBISiGOa3Tb38ieKgebrQLdtjr9DTgs-mIGg_9wiOGEqeABfsJ7EYm-n4PQtHaonl8k8282S3O6asxJN0m_bWhNOK1JaEYiNRWWBNPNvv4bSJeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خبرنگار از ژوزه‌مورینیو میپرسه؛ دیومانده گفته حاضرم برای‌مورینیو بمیرم مورینیو هم میگه این یه اصطلاحه من که دوس‌ ندارم این اتفاق برای کسی بیفته ولی کاش میگفت حاضرم برای رئال بمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/28218" target="_blank">📅 00:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28216">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZEOoZdcYyfVuNKJNPL9fFyLN8b8cTSRHicbV4BykGMCQ6BGJcmB33djZS_WGrflJx8AU0wjxW25TXP0ANrEJzJ0DaVqFOzaE6_G0fmO8yZ2UxLsW29NrCOW1PS46unRq3klKfsF66Wbx7koXE6bdphbHxvJy-plhAaSl7cL5Q7a-g_noW8hbbV2CR00HtEFRdccQzyHIkyBjz5REUZCvgYbrFg9WnOjTsDtmZ-XKWFrA8FBQC-8CrPg9n3z6C6PVlK3lKALgUd8QppjnMJACszYV2lI5rqBcD1J7SCV81GyMzX2RDEseBZxhASElNdrGAWu-S4DJNlxizAQ26xp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
روبن‌نوس: هنوز با ژوتا صحبت‌میکنم، چیزی که افراد کمی از آن‌باخبرند. ما یک گروه واتس‌اپ داریم که من همسرم دبورا و همسر دیگو روته کاردوسو در آن هستیم و همچنان در آنجابااو گفتگو می‌کنیم. هر زمان که اتفاق خاصی رخ میدهد من چت‌های آرشیو شده‌مان را باز می‌کنم و…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28216" target="_blank">📅 00:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28215">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🟣
هفته اول لیگ جزیره|برد قاطع و پرگل توپچی ها در گام نخست رقابت‌ها مقابل شاگردان لمپارد.
🔴
آرسنال
3️⃣
-
0️⃣
کاونتری سیتی
⚽️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28215" target="_blank">📅 00:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28214">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SVFEFfnZRdLTplZhtMSb9x8p3NiUZASK23lIOBd6UqDj_WqgPTEXkYdvT_9C0beSPQg1LZQ5ZAhs-tp7MmeFMpBSJEyEyPp-gOLDQerodayy77bLRQXWgoZJrJCkDED-RIWhqs7d3VM-3sT79zJ9YPI3K_NfHhhS9jjJlk746a74Gs9npsNzOjunp-damOKM0nwA3q08Ie3FbbSzIQDNR5ggnFJ0BYw9P5SjogBeyBJ65KGBQ1aT_fDr577436BPokctrBrL7hwxmdn-fur5GHyP5WOQMd3iEzkmSm0dxqnM79Qv9Hh03CbBb9EqtspB_NZlEmEvGneCYbLhdLeMNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛ بازی افتتاحیه فصل جدید پریمیرلیگ با دوئل تماشایی شاگردان آرتتا vs لمپارد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28214" target="_blank">📅 00:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28213">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6905786d2a.mp4?token=WDHtlnMpoZfVo7II10ktVbglKTtG6rpxo1_K4TuhKuyE93hnbmhbuwD3QMy0ZG8Nm-GnXV6EUT1XTcsEq-gN-9Y_x39pityUlLG7IJ6KP8KGqX-ph1c10W6NIQcV9-1cji5XmMKRg5FYi_ek_9TmZTVNNFEIbSnu3GvRTUtZvVa8lGWZK9tP2V1WPGeEPKNxyDHAQHwzH0ZnA9WmSRkpg-HVm7jcLMhM0kHJtYVknmp6QRRRb7O7iTgHm-f28ujH8cAC4TXo-BbJNyQffazU81CYPluCxLGQnhWhHOFeviWwYnDHjN6x6WFDGDX_AeI5ZDechrBQH9VP8JuGoshmIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6905786d2a.mp4?token=WDHtlnMpoZfVo7II10ktVbglKTtG6rpxo1_K4TuhKuyE93hnbmhbuwD3QMy0ZG8Nm-GnXV6EUT1XTcsEq-gN-9Y_x39pityUlLG7IJ6KP8KGqX-ph1c10W6NIQcV9-1cji5XmMKRg5FYi_ek_9TmZTVNNFEIbSnu3GvRTUtZvVa8lGWZK9tP2V1WPGeEPKNxyDHAQHwzH0ZnA9WmSRkpg-HVm7jcLMhM0kHJtYVknmp6QRRRb7O7iTgHm-f28ujH8cAC4TXo-BbJNyQffazU81CYPluCxLGQnhWhHOFeviWwYnDHjN6x6WFDGDX_AeI5ZDechrBQH9VP8JuGoshmIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حرکت خفن و فوق العاده دیگر برای در آوردن سیکس پک‌های‌شکم؛ این‌پست‌های‌کابردی رو یجایی سیو کنید و برای‌دوستانتونم بفرستید استفاده کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28213" target="_blank">📅 00:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28212">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWiu3DNuZ0ZewIi2_FTdlWmudAaqpdGuAyMjdxBkN29JM8Pee4ueNOkzf6Tbf_OS53C3yDNEGPW0uXoYsjuvI7exWl-kgh4n9x4sgYnZjuct3APIUd-OgrrK14BAhewgFAhEBdsAR4fNJZ6h17zc2gwWhqQuu6oytY9zbtjCJCGJeeL4j8JL1BIhfAm-PDA0iN0da1S1LudhvddzU1sjiWxPVnexRVcCgFpnLuidSI78vimyxykZn3MEEvsIib8w4JHTclNai-gMy0c_fBuugLINs4fSUOUZEdW8nzlPHrZB0JvxjCkUKoCdGPi9PX6ytSDZArvI_Ne5w3GwsatlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باتوجه به‌اینکه ابوالفضل جلالی در پیش‌فصل مصدوم‌شد و جدیدا هم‌از ناحیه کشاله ران دوباره‌مصدوم‌شد. مهدی تارتار رسما درخواست جذب امیر جعفری مدافع‌چپ 25 ساله فصل گذشته گل‌گهر داده و باشگاه بزودی باهاش مذاکره خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/28212" target="_blank">📅 23:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28211">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NS5-Rhth-fUu01DMWBGdCH8dnQbFjGatuEvW-qG2gmnL1z-vAASOYP3_4LvN9GiiRLyEMVV6RGkB3U9rWIygyh4T3vmmG9ZLI-ioRT_arBG5T86FbY_t3bgxcGs4YKbTynD8yqHIXDZ9ikGIXc2TKnN4npFQ_o7ok6iLQBTLEyg3oel6rTwQNKWPyC_8_UnAZgdXMNBR4n65hgHY2wc9n5GJw3HURWRhO5zwnlPt5X076QMbgmU89mXztApuYYUKkVVXYJZP-bJjjNXSziQ3XOJTfyFMjTZ3_fl0nyd0N56kRixGXqh9LWQN5SlEOHf66TDZePS6-QVLc6xE3Sc0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
🇮🇷
طبق جدید ترین اخبار دریافتی پرشیانا؛ باشگاه الوحده72ساعت همون"سه روز" به دو باشگاه تراکتور و پرسپولیس فرصت داده که یک میلیون دلار بابت رضایت نامه محمد قربانی پرداخت کنند تا این انتقال نهایی شود در غیر اینصورت منتفی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/28211" target="_blank">📅 23:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28210">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6rhGs7BAdurAtB2nm6T_hPQl3OqVaIDfutKILLLPCHGiyIbKcm1msKCPSQxLQAorZl9QE9oPb3tZJUtH5P_x67WBBLhLvU5yBAGHOwVxZsahijgjZcBEOJ-IPKD_AM0FlBZWjZvOK3yoRUCV9QM_7C19nP1OeuZUadmD3Z_Vw3P6nOy1yN3ttyTWYrXUQZp5TY5sgzd_APiddl4rly7HNSeOT9P10jUjivaTkkVhWFaNFBNCtMD7CehSWx46Xi75friZu_JwVj_imnkBRBK5hi0ummEAxJ7y6SpExpd7JL9vBuXqJf1ve1kWAv8dhA6dwgExX0Tm3cbBZtbfCqO6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فردین رابط ستاره‌سابق استقلال در کنار همسرش در پایان دیدار روز گذشته تیمس در لیگ دو لهستان؛ تصاویر بیشتر در این باره در ‌کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/28210" target="_blank">📅 23:06 · 30 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
