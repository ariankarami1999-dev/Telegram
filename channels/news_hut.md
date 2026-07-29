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
<img src="https://cdn4.telesco.pe/file/tii12tyDIUX0tYNVbOdNprZNALc3QaI_S2unNAZ9L21VapsfkSipwbXxvhKrncfo_g2jQCGjqRjlS1jtsKijNKHsEBYdpaPdZTttcFwIJ_oRLzDDeZwxMvWrGTaQqpwbUVbA5O-zN9hXSwDgJx-hPmgWongNbmoDpKI-Tw2lfUSsxs7sJvovM_ZvQZQrRKmq429lKt9_mEmcGoGrfZc8BfFsWyTEhixEprGRegjrgyvvWZZRWDdGy_HGDyQOTz4vU2XFhGP58vWonSBrfvPwN9aakEUgBMjsaZg7q6M8ltyX8Qg3iw4AhNKN9zVoPv27jzMKxc_SKkxbcHMS1crInQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 142K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 16:32:15</div>
<hr>

<div class="tg-post" id="msg-69193">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9f57d9f95.mp4?token=o0hf31UDR4vAvJi8fWk4DKLiOirMAlhmlS-Apq87P_6q_W6JatOfbv08I3i7d2l4wcq7l-jJ4iZ3nEJY5Ity_nQuNyv3lCzr7uDERsUS2LfaESZ4TxdV6Pt73pRKec4GCGpr84mr_Zj1BYO2PxvaupWGpGmkmXRVabUGWvCfXUf-3ri8xYPn2L_AGNWHsFCHsBrcR2Vtnfxqv14DeDQ3xBuJT6vMsesN8OCfOY5uelGpF16hC9DZ7FC2DS6Z-33JnRo2afu3cqhoWj3jycEv7eGQ6kEU-gqmydCtRVADugdrxA73dgfy5mYcklJLIuqFcHDw5mdXJHbCcBDFA19c_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره حمله اخیر ایران به اردن:
این یک حمله غافلگیرانه بود. نیروهای آمریکایی تنها چند دقیقه فرصت داشتند تا موشک‌های ایرانی را رهگیری کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/news_hut/69193" target="_blank">📅 16:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69192">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c969cbc6b9.mp4?token=axBO2XWuaCc8uJ1rkPCrz8s_6Yo1TVdnQWZofAQIpAv7PLv9-fzqKGda0HcQ2yyvzcd53FLDbe_RBbtu2gHO4j6Yz6y8gFLtuI13YddLgmxzwv5Ut5uENZ9fNEHtStj97aBz3pIX5EZCyOdWouPwbHinzvA3y-Fr62UQhCA7gJmGTQL6FiBUUs-_Ugl8iT9G3ehTKJGsvMp_yNEkXiQIQ-A-1JU0sfUWtf9gknRMh77DS6MzW3afgFbrb8LIKqFOccGYvy3xmDgOqG08qSl4u74JsZZEWQgvJeZ6jZaUqgvwkp0-1OF0_Tc1vSQXtyP3NiSHbRkmdwGF76nLaj49Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ به شبکه فاکس نیوز:
گروه‌های شبه‌نظامی مورد حمایت ایران در عراق، یک آفت جهانی هستند.
من در حال بررسی صدور هشدارهای بیشتری علیه عوامل نیابتی ایران هستم.
@News_Hut</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/news_hut/69192" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
در پاسخ به حملاتی که اهداف آمریکایی در اردن را مورد هدف قرار داد، حملاتی علیه ایران انجام خواهد شد.
ما ایران را به شدت مجازات خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/news_hut/69191" target="_blank">📅 16:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69190">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZNIaNZz0Oy6Lm9J6RG6BdrpZiRj5dD1OBhv766NuxrZKYvBWbcR4Nn7TOZIXz5yusN3Wvr3s3rYY_al4h1kQtitZvIJ5vonjj24XYBBVKFSEOdOmJCJFmmG6TXVBRbeUqFW0w8CVTktKgmrYz6NBe7cLO4Zj7FAtaw_HFviIf7e9KM0M2VSmK8avbf061BeDV49m1j854gIw0ca1QTSoOgE_f1S-GBOu56YEExnqo-iGk7-4N_XUKxPV7UxSXV7mRjDoGACS2pbZsp-uooFFSijSa-SDgdAqIuCSWvzC4NxRKRHrYlmsDu6dbOVv98pkGsQlptRwmbz5nmxkUB-pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس تنش های دیشب، قراردادهای آتی نفت خام آمریکا ۴.۴ درصد افزایش یافت
@News_Hut</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/news_hut/69190" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69189">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640b7bb0a7.mp4?token=rWvjkMjZH_yH8hutcze4z4ihEwq0mTWfe87xGKHgpRpJYwmXD5bFK9iZT7fiP5pMmTqB5qdGK75YcP-W4_ha4ety-QQfTF_XQlj6yYLqI_gd__SLlt7y-1BiNVL-iNLihVAGRW744RpIDSVXfbVzhlKgw7IXCTUFYwUZVw77R_wrWzuPeFc_cDvgZCTUbpCck7Eqjw1ZCU9tf4qUwZWjIMNRsVJTsX4374Zm6r_B3ASkYTbK8zzU67llcoaYHyhSEwYTFnrb3sv6u7uSFMbj_4tPr2c7zUDR18fmhNdcw5rzvR5Sd_GiYrHGfyzJcJgDjqX1sc1ZdxDiQd-XmfZnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو مراسم ختم اکبر عبدی، مهوش وقاری وقتی داشت درباره مرحوم عبدی مصاحبه می‌کرد، یه پیرمرده تصمیم گرفت وسط مصاحبه باهاش یه سلفی بندازه
🌟
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/69189" target="_blank">📅 15:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EHaZ4pTdSy8L4GDtzgq4GnqLZhHPz0n8DygUwG-GZjHu90UeeXueUQf1FbK35nA2hz4WnU2e7MS9NPvbrPamhfVP8FBnsmSAjmqsFmejPSur9ROAz3ynT_T8O58XYYWelTFf3-OLRdvQSqDQALz40pq9XMRLOB5ErZUseDcQa97p0F_R-_LENZrL0VYP-1NlEZjbbjiyWP3WZObfwCcRtLJ9JNgsJDprDUJpT5q0S0BNALmi_cU55E6SSf3U_EPblMYThI2y_u0-IDXW0Q721w_aTjxipSy--jD9A-IW0QM5aVCunJ1z69KunBYP-PoQd0MNtbS1-odawd_NrXRVhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇨🇳
🇮🇷
رویترز:به گفته منابع، ایران ظرف چند هفته آینده سامانه‌های موشکی دوش‌پرتاب چینی دریافت خواهد کرد.
۲۹ ژوئیه (رویترز) - سه منبع آگاه از این قرارداد به رویترز گفتند که انتظار می‌رود ایران ظرف چند هفته آینده، نخستین محموله از مجموع ۴۰۰ دستگاه پرتابگر موشک پدافند هوایی دوش‌پرتاب ساخت چین را دریافت کند؛ اقدامی که در راستای بازسازی توان دفاعی این کشور در بحبوحه مناقشه با ایالات متحده صورت می‌گیرد.
این خرید که ارزشی بین ۶۰ تا ۷۰ میلیون دلار دارد، یکی از بزرگ‌ترین اقدامات شناخته‌شده تهران برای تقویت سامانه‌های پدافند هوایی کوتاه‌برد از زمان آغاز درگیری با ایالات متحده و اسرائیل محسوب می‌شود؛ درگیری‌هایی که کاستی‌های موجود در توانایی ایران برای حفاظت از تأسیسات نظامی و زیرساخت‌های راهبردی را آشکار ساخت.
به گفته این منابع، این قرارداد شامل خرید ۳۰۰ تا ۴۰۰ سامانه پدافند هوایی قابل‌حمل توسط نفر (MANPADS)، از جمله موشک‌های چینی QW-12 و FN-16 است.
این قرارداد با شرکت «ژونگ‌چینگ بائوشانگ اینترنشنال اینوستمنت» (Zhongqing Baoshang International Investment) امضا شد؛ شرکتی مستقر در هنگ‌کنگ که به گفته منابع، به عنوان واسطه میان طرف ایرانی و تأمین‌کننده چینی عمل می‌کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZuKddmUeErh1O8tH7ywLcdMiQPhTBbnMySB2rxAqxlp9L4xDfHda4E4xbc4YpyHJD37ue3W7S89RalUt3pLDppSgygmzcHUAvY5Hfu59iFbCl2rB-hKpOrugDMJOgI8aM15kZpxIwDRV8j1md-Su8dxcuD0ajhmItndLImYahpWcHIkxmOcDdYFGNTFwGYf-D51VlshM6GF4rPUDWHO4FMSW76tMNJdbsHThIJA5Ei70qtz4rIW8YOuI7nWcZA90WFbQAgYy3I__EpwvOwArZOTOSdrcdtfAV5HZucp2iQXuThxKyz9luc9LxAqXWRXnixpWtJxoKNFVyawPN0vY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عباس عراقچی:
وزیر خارجه اوکراین به من اطمینان داد که
حمله به کشتی ایرانی عمدی نبوده
و اوکراین هم
دنبال تشدید تنش نیست.
ایران هم قصد تشدید تنش نداره، اما
به‌صراحت اعلام کرد هرگونه حمله به شهروندان یا منافع ایران غیرقابل قبوله.
خسارت‌های واردشده هم باید جبران بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78f023144.mp4?token=X2996PbZI241PaIn25W1YiTQPgIDmu2uJGDsM5ATid3YVhcTMxyFBBk9SpiAZ_iqMIQDOb6mLm5yMQyQpshqX0vpMWiUvR8Rf1MQmcXqIDg0gGwXL59Y0xJzMEHvWu9sAEeWXJoPa_DiJuZXG5j9qGFavj90O2Z4_B7ECM0wnenmK381cihqNm7mFHpJDxoigK03cfULKZC_gSM4ayOEv09_oC1kMZ_qebWDxk3ISeR09kV129BCao6fKABL4q398JM48RnGN6MuQ49oF_4KpqXIUsR47wIdke8r0oNfLCeMPvfR-DVd82qQWQ3hCw3DAeihZf6QO3nRDTAiDcCVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بسیار کسان به این سرزمین روی آوردند ولی‌ همه آنان رفتند و ایران ماند؛
جاوید و پاینده ایران
🫡
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuQfLyQa76fPWCwu5JFDBEu5ufsePzg4B0sWoEDceRPmUwECyevkcubRKElyU6SGU5BAHaDr5hmrB903DBXj59UMQ0C-1Efdra_bQrL6mY-MxxkGmIP7PTkLOfMWtDNdhbpcypfnnXvVndXtww5NtSHtc4Hwjjh5exkFNnATEB_N_NDZ5LEQvBKeS4idLsxZ67YE43o80pqGHzVU9YMLfWcAZPA-QjIWGJZv7qee55fu1OwkFgNK0ofZy6bt8DkdQsxlrgZRrQOMtMZdYR9PwVCSyPfSkrRx3xA4Y0253zKmp2mJ_sX7ZfFds1dmXiw8XlPldr6PO5lG121PJ40ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f04q5kr_inKjUkXA-fAxRCi0JXJ8pFOnyfaxpcUVLtAEaapfW6xO1J-ybL8cy7MV61pV1JjZYBX3_spztVUk4ry2-YukezZvrzcrmILosGPB30bOq99FFnpAbtWeB_FnibaePcLA8ou8LplY6mL6WE21iOUTs2c9XBmgM-dICtCsVKqOHhyElA7Iw2HWO3ljXLNOJa_hmLcZBtsghbWMwsl7kjL__FRCH_D-DFw27yZbJpe668F5RC59DMEFkxscUy2Z5PrKjkRH3aQBNPP3QhzrcObB4NuYt-ekpZfJQjsOQOR9SR9ruT6Y4R3kruCnCisqmYDap9SnsURVsSW1uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
نایا
:
موشک‌های ایران، همسر دوم رو لو دادن!
یه زن اردنی میگه موقع حمله موشکی به پایگاه موفق السلطي، متوجه خیانت شوهرش شده
😳
ماجرا از این قرار بوده که هشدارهای یه
گوشی دوم
که شوهرش داخل کمد قایم کرده بوده، موقع حمله شروع به زنگ خوردن کرده و همین باعث شده بفهمه اون گوشی رو برای ارتباط با
همسر دومش
استفاده می‌کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8245e9f66a.mp4?token=nDyxe39lrg97YNMLWT-XY4i9OL0qdyr3HQPxFyBLWRxyA_aDZTHgDCyD-xs8FVw9JlNU8DbaWLBuFfnpqlVCwK0DLJFBTXQheGw6KhqokszQgWYtPebsw81arUbh6026juJHHP9aBrSodnfDn7qF39TfIBvTVLte5Zq0TOz0Vw1rxwNww_eFLCMqJjsrT-rFOO-z-JarDrs9RZbjABfS3gsT684JtRgh_42cicc2DteDs-mRYD2muRkc34BOEv30PnPhXJh0ICGcydeTBwXYm26pKz4hOE5h9IfWtlPv-7UQtbyVhDLWlYsOxK7WhWbrGPoNF_k2AdXsTFnk2jnV_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، درباره ایران:
من نسبت به این توافق تردید دارم و این را آشکارا می‌گویم؛ اما تنها راه دستیابی به آن، درکِ درستِ ایران از این جناح‌های گوناگون است. به گمان من، تفاوت این جناح‌ها بیش از آنکه ایدئولوژیک باشد، ناشی از ارزیابی‌های متفاوت آن‌ها درباره میزان سرسختی ماست.
کسانی که رئیس‌جمهور ترامپ را بسیار سرسخت می‌دانند، معتقدند که «نباید با این فرد درگیر شد»؛ اما کسانی که تصور می‌کنند «نه، می‌توان آمریکا را بازی داد»، معمولاً خواسته‌های بیشتری دارند. با این حال، به باور من، در نهایت آنچه تعیین‌کننده است، عزم و اراده ماست.
عزم مشترک ما این است که اطمینان حاصل کنیم ایران به سلاح‌های هسته‌ای دست نمی‌یابد تا بتواند با آن، تک‌تک آمریکایی‌ها را تهدید کند.
به اعتقاد من، رئیس‌جمهور ترامپ در این زمینه کاملاً قاطع و صریح عمل می‌کند و من به همین دلیل، عمیقاً برای او احترام قائلم.
آنها باید بدانند که اگر به ما حمله شود، با نیرویی وحشتناک پاسخ خواهیم داد.
آنها به خاطر آنچه که من گفتم، در دورهای اخیر درگیری‌ها به ما حمله نکرده‌اند.
به عملکرد امروز این رژیم نگاه کنید. این رژیم به هر کسی که در دسترسش باشد حمله می‌کند؛ به عربستان سعودی، کویت، بحرین، امارات متحده عربی و دیگران حمله می‌کند.
این رژیم به هر چیزی که در برابرش باشد حمله می‌برد و ده‌ها هزار نفر از شهروندان خود را به قتل رسانده یا دچار نقص عضو کرده است. این کاری است که رژیم ایران امروز، بدون در اختیار داشتن سلاح هسته‌ای، انجام می‌دهد.
حال تصور کنید اگر آن‌ها سلاح هسته‌ای داشتند، با جهان چه می‌کردند. این همان چیزی است که باید اطمینان حاصل کنیم از وقوع آن جلوگیری می‌کنیم؛ و گمان می‌کنم ما در این باره کاملاً هم‌نظر و مصمم هستیم.
مایلم کسانی را که به دنبال ایجاد تفرقه میان ما هستند ناامید کنم، چرا که من و رئیس‌جمهور ترامپ در این مورد کاملاً با یکدیگر هم‌عقیده هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2265e1ef.mp4?token=dNMPk1r9DhONkAz9W9O30NEI1dsyiaCgaZb4MSXO3DVzljop7c5ANlkcnEXyILDEf2c_PlTU1idyP5VNkx6UBf5cRJHhcKm1hQAzmqsCFkGVUE2wxzFI3C7pnjTNMO-fHVD7Zqt116yu_CcFoygO8p1l9qu5wzCVnWsjkGnw9yM_gHy3VnOUR2RiWoLU5slgc9V63yKQGqbllD7KbmMm9eq4JVSv48pCCNVw3ZgKlXHax3xRxIov9jfGGssn35i7P1anCTDRBOBlsuDKyaG6MoWEaVZEMehjgzOpJvb2Z1BMk1qVi-r1YXyZ95Hlbh6P0dnQheXz2NEHGiYO2T3ONg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این خانمِ باردار رفته بود سونوگرافی ولی به دکتر سپرده بود که جنسیت بچه رو لو ندن تا اینکه با این صحنه‌ مواجه شدن؛
شومبول آقا پسرشون انقد بزرگ بود که تا دوتا اتاق اون‌ طرف‌تر هم همه فهمیدن بچشون پسره.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGZyj8yLFc8tJ52ej5C2aIR8eLS-flrwkPArKO1nSj_64cv4J3N3ErQe_vXPXoCi4qRYRny3BtG1rKgaYy-76M_8tw1f5ltJctqAD93n6f25xJ4uMc2jaaN6kZN_U4qPRlUUVitfqqnKQ6uCAvOzmX1AHEQ10HT5PMCm1SYJ3G-eagNmpy40PUF8HCIzTslbcimV-RyVrpQj8WRdrVMme4ZelcwGu-rGXI1E9DPp-CxpyvSWwQk5tSibS53hWDN2iJjymLwfedb2dAVcKgxpJy3ypwHJY3DKva93lCd6rtxRHPLdKrpoyu80f89m3rLN4oj-ZpUdhWPUM1Uv33MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=LdQwf-7_WLo0HfB4aZ7XDGfxyval--2h5GEhbyHgBO9sZ-gQsD_cMfq2QkdFGl5ShNL0wVwDXW1YHLFa-Nklqkfi20-GN3x6ZB5vVX6ltOZSDlEp1JzlWWNYAHbX6DPXDjau7wwnBgQfcV3xA91H2kqZpFq4dDjV_tFXpLpDSuURiCESbk8I3sOaUEt0xyTWOBARpCqo-Z-bBv2XAic7XnpAinSnStwUoabommEtUzyOKhU2JRcNJwZqQKTgxCkJ4wJSw8AB27znQ1ahSvlwhT5c7AO8laEVDWit9xVVVpf_wXFpjO5MUxBKiqgDnoOKbA_qLfNd83gYUoUjusN1sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b39375dc32.mp4?token=LdQwf-7_WLo0HfB4aZ7XDGfxyval--2h5GEhbyHgBO9sZ-gQsD_cMfq2QkdFGl5ShNL0wVwDXW1YHLFa-Nklqkfi20-GN3x6ZB5vVX6ltOZSDlEp1JzlWWNYAHbX6DPXDjau7wwnBgQfcV3xA91H2kqZpFq4dDjV_tFXpLpDSuURiCESbk8I3sOaUEt0xyTWOBARpCqo-Z-bBv2XAic7XnpAinSnStwUoabommEtUzyOKhU2JRcNJwZqQKTgxCkJ4wJSw8AB27znQ1ahSvlwhT5c7AO8laEVDWit9xVVVpf_wXFpjO5MUxBKiqgDnoOKbA_qLfNd83gYUoUjusN1sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
کاخ سفید پست جدیدی از ترامپ با متن «کار این جنگ رو یه‌سره کن» منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305091e76a.mp4?token=cutrD9X1GmzNSmEU4egm7NtBEhZbjJs8y3HQowJ6yzAqru2-HWbFIMj1a2A3s_AA1KGSu8s3MP2woU5veP-fxp3zL6eO7Z7djylipZQAtvEmTHkz4HV4pWmaS2e-xdhmpVikoBvbI7uJb8Q3LFpZ7su8s4z2V1tkO8Mh2CaPGI3_zvmXzCXAenNyGqptaXVbdK29ahdU43e8wwEM2QvP4elbFPiR4P9vVBr3VUV8XDGi1F-J86VU-G1Cl18vlQBpMjtPqKESNvwZcbFOny2Y_UNdndxQffPp4rGx-s_DhlB_viD1yjkaiDLT-1ZJGfpdwLB6NcJGxQK4VhzAJb-VNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305091e76a.mp4?token=cutrD9X1GmzNSmEU4egm7NtBEhZbjJs8y3HQowJ6yzAqru2-HWbFIMj1a2A3s_AA1KGSu8s3MP2woU5veP-fxp3zL6eO7Z7djylipZQAtvEmTHkz4HV4pWmaS2e-xdhmpVikoBvbI7uJb8Q3LFpZ7su8s4z2V1tkO8Mh2CaPGI3_zvmXzCXAenNyGqptaXVbdK29ahdU43e8wwEM2QvP4elbFPiR4P9vVBr3VUV8XDGi1F-J86VU-G1Cl18vlQBpMjtPqKESNvwZcbFOny2Y_UNdndxQffPp4rGx-s_DhlB_viD1yjkaiDLT-1ZJGfpdwLB6NcJGxQK4VhzAJb-VNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی از لحظه‌ی حملات عربستان و آمریکا به مواضع حشدالشعبی عراق تو استان واسط، که توسط دوربین مداربسته گرفته شده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74196ace24.mp4?token=vGImj1bxQvz1NswauDzss8GvC0-XWz6d7Dnwqd9U3F4ZsEYO-2hWV11zup654ipLncBKax2BhRDHV7DBuKjiFY1XM6LbMpxVjMD48W7L9P8ETXN7qUXsGg-1nPXK3ofOnsJhrCWHRPFBX8gUtaZ56V15G3-KfVo_AwAkLkQQzLBsmM4BjdZ1asWTIGaGLriMxABCFyKI7uA9d-lQ04lQXc9ZhRqBQ7SBDxwHJF39a88Z8MyfXCeNp8sPSUFulZjIlh2vHuqny2y1HA4ET6yzAqGh82QqTU7J9JwzvRI86HVMQLoejKWtuYpCnZ9H9J_6UKiLeAwSn1ycBH6DqrLuNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74196ace24.mp4?token=vGImj1bxQvz1NswauDzss8GvC0-XWz6d7Dnwqd9U3F4ZsEYO-2hWV11zup654ipLncBKax2BhRDHV7DBuKjiFY1XM6LbMpxVjMD48W7L9P8ETXN7qUXsGg-1nPXK3ofOnsJhrCWHRPFBX8gUtaZ56V15G3-KfVo_AwAkLkQQzLBsmM4BjdZ1asWTIGaGLriMxABCFyKI7uA9d-lQ04lQXc9ZhRqBQ7SBDxwHJF39a88Z8MyfXCeNp8sPSUFulZjIlh2vHuqny2y1HA4ET6yzAqGh82QqTU7J9JwzvRI86HVMQLoejKWtuYpCnZ9H9J_6UKiLeAwSn1ycBH6DqrLuNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
خداییان، رئيس سازمان بازرسی : بعضی تراستی‌ها خیانت کردن و با پول رفتن!
یه تراستی (شخص یا شرکتی که حکومت بهش واسه نگهداری یا انتقال پول، اعتماد میکنه) فقط 200 میلیون دلار پول مملکت رو برداشته و از کشور خارج شده!
معادل38.1همت!
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MsCAC8akjb_WkApy_1obh2DDhThBI8hZNmbbmj2x3hLeMImgnwiM3v87lgpamc2V7US03KSq8XtsE3SQjEBDlVjiiUAHIqtzGxhHWopU02CBibWsEUCTBiU1cJXElnM9cmBPAEuLKoayOVYsWxL81uX0y6N2tC27ibWuK7Kus_fKgcCVSmQ2waVT60AH2ha0jEoiWE8TfklDVxyBOjSCd6PiLmyYv8BA7Z9BYqxEvkSMzfvfVnYHh8Hv-Cu8G1bSr5BASuMqrR1FKXF8fWJol2OTO_hqGItQuHZu1GlNo9os_lCzA3h0k1_e80NhEuxHMoN55cZvTpiFZ1LlYO74BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم:
تحلیل تخصصی بازی‌ها
بررسی فرم تیم‌ها
آمار مهم قبل بازی
پیش‌بینی مسابقات مهم
نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای
اگه دنبال تحلیل واقعی و بدون حاشیه‌ای، همین الان عضو شو
👇
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWnjfiksSHODzqsjSoMpCGguSDcm6QH6LoZuHS4DlYqIeB4G2s_yXlAfGZpFXGvmJFTcBmMBr-QvLaFtN9f4SuZVr2EF6iO9rAndrK_2bu_vjF_qFVJlVv13KxWEIe3j_eWKvQLrKXxbIoFcM7H5NHGCt3tmwu_8Usd3vLRTlturEqIRqLBwpdM6lAQOic0X_NLucPYeTnEglw7uTBvgIOTcCTM6AJ0RVxFAmEIGKo2b4mJxCu3Zc9Scu17JRmH_e90fs54nac9HMNn1Jipiu1qHMekKu22qrJ3vGaTHUCITWT_TbYplR-S5ZGyEaArE6AnJR5NFniRvUdjEfOKHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVws3qCMpZh3ZofX1NPDxICk8qY24h-ezbXDH902NCBC9HL1fWDc0DNHrgT7gyvF2JP_eYtFjH7_mpU11YnIpCFC-TdPAvyEPqE5Xe3dtruNkvwAJHJTnaTmnGFEXyOV_XPpuE0EuQsCq_eDbcxQ8eZvdMcfpT9D_eIePZ54mmtzEIEZ2pXbNfLf-ZTI6KtOSXZQFXGdv0gQb2-p-MrqT6hYYW1-0ne5eb5US4rNOwNPRyHrVsWxj9LwWlB-rHGbeVc66dYY14wbG11svc6wCuntukoL7eMvcd-haocadL1AhZbrGSqKnPLBy-CDD7uvthPmX2ru63xlj2oPboD7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58608400cb.mp4?token=e5Z7cTrGiRopGnM4yA-2XTQO-vtKynYKtuCVbAJTkTipYB2efHuq20og6LqfDlawB7ndBmBDqQ0uiwFPjsZ_QAw2QES7aBMSGeF6dIPfsPOnN8QRdzf7E3PyOcb_ro9WGD2htlCwuXmQSUoLQ3It8dhD8geM7tmIKc512fs6RosO55owexuNbQ-K0dzI_Q8Zsyi5W34-ASbynfBcq5Z_FyF2nTvfI77v7RJb0RagpQ7YRVczrSV5rJCc1dYMjz7khW3bSvN7j82g_5Kk8gi1w0eA_luMnPUdKfNjvHZ4CW9dVqPFkKMR0l5O1KQbQ1lqOHGAQkxgym9pp5iw2UIcgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58608400cb.mp4?token=e5Z7cTrGiRopGnM4yA-2XTQO-vtKynYKtuCVbAJTkTipYB2efHuq20og6LqfDlawB7ndBmBDqQ0uiwFPjsZ_QAw2QES7aBMSGeF6dIPfsPOnN8QRdzf7E3PyOcb_ro9WGD2htlCwuXmQSUoLQ3It8dhD8geM7tmIKc512fs6RosO55owexuNbQ-K0dzI_Q8Zsyi5W34-ASbynfBcq5Z_FyF2nTvfI77v7RJb0RagpQ7YRVczrSV5rJCc1dYMjz7khW3bSvN7j82g_5Kk8gi1w0eA_luMnPUdKfNjvHZ4CW9dVqPFkKMR0l5O1KQbQ1lqOHGAQkxgym9pp5iw2UIcgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ خطاب به مجتبی:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVPNx4Zlp3YrRdTdV4xsRDe0Q-Qy5BtS6q6MeCeqGQocKvL2iDAtp-j0Dwb6l-T43h-0dzXBxuNAQQzT-YfDVeh64hyKzXygctRuJT4hmSMjEZ52AmAqjaCiTOoOG5QOtbXfRGPUkIWWNDNwQxNGGlrBBgl6sa26EbwaikLNVH8UpaXwxmBD5aPxS8bcRyQcVNGzak7Le-oLsuy5VHvobkPNnfVBKObeuXTbQkZXJWskfegwXKl3V2x872GlSeV5Ky4jgOn1-_dqIdC4fuqd2Vx9zCWDPsZYYMYHuh8367iPDuF1tJJ2a2RaoJmafJCENsglL1J32pk-OC8unAuMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl9Lw5bw4Ch0NaP6EC4PbNHSO9wHIvSvQsl0BF22syZ7qFAO8TI4ugUonPz4CCjuder3T4MdQAiDrfsUr3Zz4CzKdEr36wW3iQxLdV86rBLqffBJwT-2n-s5b704NWzLB4OLS_h5wcX8LfJzHb5XNLadO38TuPo82wFRt38PAZtdz8NGybxRROs-gM8L9_BiloxdBiXQwqJOphrQ-19lbp4F16yJpIL3pqckd7bEcXYmo5jmYc6qs_khvhfdzmbVhbecEkJFursVcd81yTa_3GJEK32oEprQ7Ge9-17MdBPqn8OYPqVhnS5lJKJNydDs_lgYMEIL4PwP5RHdT3G66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/lnZ3sOx5obt7dheNfL6aWJQ8GqwAOXfrLFpXxOv8sALRVJU0FcjEtwxMOjfJ_FQ3s85u4D-Qo0IOmE5zoZOf6mEoHTRAL7WKgSZUFl0M8kSnpWeVI8w5NtP6Gs00Jk2GV1ZRI9lIrUZ1QnJlCYawdlAoG7G03BKLxlUMO58ZIht-y062D8J-edCWcF-XGCYvt5tC6XA3DmFid8XF9Mx2rahG7I1P7uUk9EDOKt1BpTDrGiXU5mWrBv1Ps77fhs_rBu0qYUaTi1iSK8PDm1vHumIOg_C6M5A-_2HcjCwx_zIaCzKr4bbgZ8CY8iBADCZOfuJjE0PQMfL64uVxZDcR2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pAGmPjSdxWBxi3ps3gKf_XhO0xrjwWHBp84ZVyq3oDbHTA2-9vLm5wj-bBFVQOlwD3dQVIYEmqqIxW24ZGj6GGl_HQulaI3oDh2vix33S2FNMC1_OVA1xcltpm8V8-u4KCyEfkrfXcy01p0aI0TvGzPwZSlShYIpSyo9Sr91UVUflLd9WzVNMhL83JiM8RMNm2pO5LcLQRblet6QnDEAQE0CHH8yDO6y6IHFs8oaRyn8bC_vcTIRgZwvLMGsNH-O5ppSDQVQw_k0q7JfnwhnNXVRWSX3WaRwgnFYgGuSXssEqWpGjTr--GNcGLLmVutmMGAyiGwEiq2uG0SnGx2Xcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41f8819418.mp4?token=rXWhJc1M-9nS3RSejfFDvkTBmZdmVRmWEH_Q5f58LsKE65da8CKr45p0ER9540ZT_8TpVtte5fbZXLeri05cF3P-_C0IDqy9YUiVVB1q92yI2QMxbLXA4_w22IZqvEbx1auMt3FPwC-JHhaqCJZzEQTxZ1vU5J7pCGmmfkIItODLSTQ2frMuzuuNmcxSSfMnXs6dyEMHYeM6pdLCiuufj3z6bFbqpdzzUsy5vk-egFl__305-6HIofQDO5xt156BEAb0df74mPkiOrGMfqvQbZUh5sVRaVkvqbob0J2u3luSP_przCoQ30fiQHiBBwM7fvW5fkNkbPh1mXYYQ2RiNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41f8819418.mp4?token=rXWhJc1M-9nS3RSejfFDvkTBmZdmVRmWEH_Q5f58LsKE65da8CKr45p0ER9540ZT_8TpVtte5fbZXLeri05cF3P-_C0IDqy9YUiVVB1q92yI2QMxbLXA4_w22IZqvEbx1auMt3FPwC-JHhaqCJZzEQTxZ1vU5J7pCGmmfkIItODLSTQ2frMuzuuNmcxSSfMnXs6dyEMHYeM6pdLCiuufj3z6bFbqpdzzUsy5vk-egFl__305-6HIofQDO5xt156BEAb0df74mPkiOrGMfqvQbZUh5sVRaVkvqbob0J2u3luSP_przCoQ30fiQHiBBwM7fvW5fkNkbPh1mXYYQ2RiNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/X9RWCcrczoUR0wYDz8dJ8Rpwbb9D0JcSYGjPtNcBwatg0zfYsWAeIiKSZIfJJJq0JHpk1cV_aGjG_AtGpNPUCMEAXp9p6WVi4BdFO7953wbzAqlDDJuZApte17oSDnVb54OY71IJuJgnyeCecd6VWJPCZ5TPym7E4IIYhPxFgnqyuU-mnmD6pCmAUvXcKOTDk0o7cnbIdcCP-wLnnCT-vsfy3gERKf1AqWEtZDdiMWyAIxEk27Fo9HRjKUdcdodgFA_6zqxGXuPlsH-zfv9BaO6ITw4ZvkzbbQdjXpU1ot0uvE1ryqivBrBK3_wVuLBUV4coIdxZFaQB2FZUtME31A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=insFyC_bXFg_BSkCdV8_pMSdt_pd69f-tv_Hk_U5JUsZ8u0Fi--8kK_PQSj9ZPR1fAmgraCa0pWh3aRiCppxjPRdm-ueTA8i5mBcSRh9VM7nvwypYBJG0-XdKN053JOmrHdDDny2Wh7EbEH_BPObXLfVu6xe4suhJNHoOfauR4vMoe8aWHwjdwcnzQw5ADgO0nakNRikUcxhPvjdDySQUQTyarksPAaeVM25rSe813F1-DrDbxf-7_3aAL7u8-_lO3If2inD9J97njEW3f6PmoGNGWN6y0XHmCY3WI1Z10xU3X1ZYwNHIhs4Q5LzX7-6N32ZGvGX-HbsTXTVsI5ypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=insFyC_bXFg_BSkCdV8_pMSdt_pd69f-tv_Hk_U5JUsZ8u0Fi--8kK_PQSj9ZPR1fAmgraCa0pWh3aRiCppxjPRdm-ueTA8i5mBcSRh9VM7nvwypYBJG0-XdKN053JOmrHdDDny2Wh7EbEH_BPObXLfVu6xe4suhJNHoOfauR4vMoe8aWHwjdwcnzQw5ADgO0nakNRikUcxhPvjdDySQUQTyarksPAaeVM25rSe813F1-DrDbxf-7_3aAL7u8-_lO3If2inD9J97njEW3f6PmoGNGWN6y0XHmCY3WI1Z10xU3X1ZYwNHIhs4Q5LzX7-6N32ZGvGX-HbsTXTVsI5ypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeRH-3xd31SnPdHReCkGxyGxXOr7OSZDIYQKb1nuZUDGfpPzVhbfYJYpwveBXsjbBlMXMCDVJ3VHwTm1Zpdd8hSbhefQpAokK8_iqn0BJ_sdVuYT0X4-5J0QrVcAv0FewiPAwgurvlW8r18zPFnZpvrZftPOVZJ600azDih-9dG_j0YmzVVvSm6eM6JlPwaIn1aSAXNOjGUJ3JqzDFu2SjDek_a67nEVo3ozxHaiQxiB6LNWqNpKa-qmS0bEZbBZDI_TrOPuznSZQM_3lqUGi6jBlKwj30MnlfRIPxjF7HrjJQX6QjnQ8DRG5x_caWe2tz-ms2JR6XDlJJgTtQVD0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSyTKTf6vR-rHNdDRyPt9t95k_blHm98MBSUP2fzqQfaAXTDp_P3Sd4zobuu5vyEMV-BeIfDVqkv2N4UkfeI8QnVR1c-F32sQY-2WBpB1Sspn2KgI_chwpCXlUeIDKwKyFDwAGZzchFXXQ8EqITPyPFKOfoUIKo2W96wR7yapuO2_U_rdMSTENPmDuJGhhAYu6RWXCGQSBzvByYWxGv9cLQRJU21SaxkyqAaX243nzbclEbpeDykv8soJsk9RrQ0QA3BhhfL5vFSYjTyyvTf-0-BidglbgidsPRWuiLXgjglYZKkHXeOTiSy4kERld1pdO60CGbnDETMAjcDmAGCbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=lT-_XkFJ0Df2arpnjIZb2B9KhIBw9vQqBjZL6o8uUoYgmkhVJ7stEFpbQR8chIbxr7jqMj2Hl7DTlQsc4FYgIrfN-R7z8d9K0Bol0XSOaU49Rd-N1F7b8LeJ__wumdlq6DcZPFwV3SRHjzqLS6uJvDK0RKUxeLR0-PFhmiRjQJiyl5XDwsBeRWtpzp3J-ZJNs3BX7rd7yX75hXnS4PbLacEPqk2vgVXjBrQuWc9tSmWEVLnRzlrUSL_oaJtXAiNSaVTTimrKQhefWuE2YW9a2wF9DJa0wmwYWKXC9NIlevdMr-UVjIvsYbntS3523_k_fjaKfzOyOyqbuLIH8KgZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=lT-_XkFJ0Df2arpnjIZb2B9KhIBw9vQqBjZL6o8uUoYgmkhVJ7stEFpbQR8chIbxr7jqMj2Hl7DTlQsc4FYgIrfN-R7z8d9K0Bol0XSOaU49Rd-N1F7b8LeJ__wumdlq6DcZPFwV3SRHjzqLS6uJvDK0RKUxeLR0-PFhmiRjQJiyl5XDwsBeRWtpzp3J-ZJNs3BX7rd7yX75hXnS4PbLacEPqk2vgVXjBrQuWc9tSmWEVLnRzlrUSL_oaJtXAiNSaVTTimrKQhefWuE2YW9a2wF9DJa0wmwYWKXC9NIlevdMr-UVjIvsYbntS3523_k_fjaKfzOyOyqbuLIH8KgZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oqLRbyxGHzgEwhfslx41wF0j11E17LhmayUXDOWi1c_ZhxrtxSvuw057iFmZ_yvWA0iQqXJzWAoWTKMn-RnDR3yyhkjOocgrahc47y35w6S04UE5XittQRwAdm465CO1IVBsMPi1UZeJgEm_oQsKMivrKcgVPRviSSxZLb7hEBYBxg-H3r97_PIIPRaaOQZUFY-IOHDitNMK_lCr-lcoQP1gBLXGgbqX0knFG2NRY4LPCKwPxy-WYXdmXDTiJvdeKVdmPuQUXggSmW3mqsCTxyc-QQrr-d7I98OlmezPHk1gLBJpDqZFk_nfRCvmBypmXf0RPFGF3KHi-cFTZWeoSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=YJHiSrzepSQcjyet4WTMqvkxUKnaUHUd-Y60gP5YWVAwaIHmmNOiPjHpaftoENz7sNfY4b7cbsRX_Sd1deDrUHia95SWWiH_jqsSavCawqlufYs9aXFPiNYXYHR-Ujw2ziWFw7acEPMvrf-tFJIhLwwvQlE1xf7DuP5X0yWQ2QgzuN4o6dw3NYmx9cTM4ZP7qL3tUlo3CVRBe8CV3vGcV1AuD85AHF1E3rnf6UII0knCSORaEOqtRrRE7g_JCkQhruWTbiA822XmGbVAdn6KqJVv8ReK3-dQODrU9iWCnFbC5GwVFdqO9E7Q_wJoR4X9dQ7Ark6YfAA6vrKyA89AOVA92H0NHCLvq8T3rxguHYuhm5pqixAWoi6_Sy_KSpjLW7RNf_xXy7Jc0oPx2Y-WtzByH0RIqg5Ds3r5f7WdNtfoCLGMbsd_oTY5MTdfs2LhwlyRJFU55w0s13P77rEunik_B9PbiwR--ctAr038JG1gAD53R1-w-RpXPBp-E7ve7l_Dhjy46MR7R5Nljy3jnCUQqpMgd1FbAMKmyK6AxZjQPJyjfJXGh0XGQUwqjyBHTo7tvtMHqu746PplvM1vT3QRz3EoVgehxunMK3ot33px8r2852AIwVrHiLFAzCypsWUzR8-2XY1HHIfPfhshjxpjkYmEBILmoStP9o9O6ks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=YJHiSrzepSQcjyet4WTMqvkxUKnaUHUd-Y60gP5YWVAwaIHmmNOiPjHpaftoENz7sNfY4b7cbsRX_Sd1deDrUHia95SWWiH_jqsSavCawqlufYs9aXFPiNYXYHR-Ujw2ziWFw7acEPMvrf-tFJIhLwwvQlE1xf7DuP5X0yWQ2QgzuN4o6dw3NYmx9cTM4ZP7qL3tUlo3CVRBe8CV3vGcV1AuD85AHF1E3rnf6UII0knCSORaEOqtRrRE7g_JCkQhruWTbiA822XmGbVAdn6KqJVv8ReK3-dQODrU9iWCnFbC5GwVFdqO9E7Q_wJoR4X9dQ7Ark6YfAA6vrKyA89AOVA92H0NHCLvq8T3rxguHYuhm5pqixAWoi6_Sy_KSpjLW7RNf_xXy7Jc0oPx2Y-WtzByH0RIqg5Ds3r5f7WdNtfoCLGMbsd_oTY5MTdfs2LhwlyRJFU55w0s13P77rEunik_B9PbiwR--ctAr038JG1gAD53R1-w-RpXPBp-E7ve7l_Dhjy46MR7R5Nljy3jnCUQqpMgd1FbAMKmyK6AxZjQPJyjfJXGh0XGQUwqjyBHTo7tvtMHqu746PplvM1vT3QRz3EoVgehxunMK3ot33px8r2852AIwVrHiLFAzCypsWUzR8-2XY1HHIfPfhshjxpjkYmEBILmoStP9o9O6ks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=kden92wLJvj0zCRyIzqcIt0By618VfdTaF1f1vvzUNfK0ebJs4BhJjHDyaN3gAW1qRy54RrsvXOfcY__NnqujCQeqfpycXcdAfmgvok8rnYT1HDmpXYjcjJVJxwVgSTTPPmGXK_4vux4i1FbNUP0n9mcBmSgcZikCVdDq0EOgFDtOoBRc_vCHIHeQL_raI5KqnNNT_HPWNGrXzYTRk5Xx02XWReoVkj2vWlhS1RHLJM8OG-A2cr0RavEu89a5-PPCOYgqlSSlSaLvnIghtJit5vPiLDQa6m1hSd5XX__ZWVxr_E0gqrSRB9c2gxfZT6ZbgylSdRWJm-ZaND641hz_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=kden92wLJvj0zCRyIzqcIt0By618VfdTaF1f1vvzUNfK0ebJs4BhJjHDyaN3gAW1qRy54RrsvXOfcY__NnqujCQeqfpycXcdAfmgvok8rnYT1HDmpXYjcjJVJxwVgSTTPPmGXK_4vux4i1FbNUP0n9mcBmSgcZikCVdDq0EOgFDtOoBRc_vCHIHeQL_raI5KqnNNT_HPWNGrXzYTRk5Xx02XWReoVkj2vWlhS1RHLJM8OG-A2cr0RavEu89a5-PPCOYgqlSSlSaLvnIghtJit5vPiLDQa6m1hSd5XX__ZWVxr_E0gqrSRB9c2gxfZT6ZbgylSdRWJm-ZaND641hz_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNN7u1SUXIu8bpzMFg7eWfFp1yMhbhpRm1UV5XRtHas3aV06e10AbECRaBX9g8iJcpFvfO1mhAdTTGSfSwVpZgEyqv-v8OnEDrf50tisn6SR5vkpE9b8lWQTB85HoH7gN9DL2aAhtWnCeXNLCMhxJHyiqD8uBjvRL9X90EFUrXqSS5oSJewwWd5k7sMxruMb66Agaqa_wlY695rpB1WmmMG8BlMxW-H3g5l817xnbARUzTfSn1lH0C55knIysGl_DefdB7arFtkVY_-Nij6LGGzZdFLmCA4Lqmv1NgjpB9hz5dw1FErg4tJaziAjsXXEFVKxK5ONbnfH4cPq56Ok_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=qM3tKi1XvIh-KRiipQuf-uSmqEPuhgeH1JPQqHCCaeMq80S_LgRFZU_529kmwe9EnVMJsEFNB-fVRCI89l1Lp9lFZpsHr58vSI5VmxbaKGAw3L3U-THnzHuLFFxAHHDukkeAzERaT7u6NuzaAP4fEvmfxN9N8yYAKOjT6550RVYUhDOwYQLEdy9WNQDxgN0u0O1NdZO-vW6B9r1gD62Ti-N0lf0TdQrzYM7t3LUk5dHEWWzvXu_dw81Q11hP9ucTeHdC6RaBBnu2CmzvGszgajj2WmTNVZreosLqVDQgmmfOHet3wOtbKF0FcHuprNbRHe676lXAviCbOVJ5sR0YUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=qM3tKi1XvIh-KRiipQuf-uSmqEPuhgeH1JPQqHCCaeMq80S_LgRFZU_529kmwe9EnVMJsEFNB-fVRCI89l1Lp9lFZpsHr58vSI5VmxbaKGAw3L3U-THnzHuLFFxAHHDukkeAzERaT7u6NuzaAP4fEvmfxN9N8yYAKOjT6550RVYUhDOwYQLEdy9WNQDxgN0u0O1NdZO-vW6B9r1gD62Ti-N0lf0TdQrzYM7t3LUk5dHEWWzvXu_dw81Q11hP9ucTeHdC6RaBBnu2CmzvGszgajj2WmTNVZreosLqVDQgmmfOHet3wOtbKF0FcHuprNbRHe676lXAviCbOVJ5sR0YUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/0050768259.mp4?token=Zqnr4A98w4ju8ulWJL_JcBzIi32AoAja8MOjwVKm1H1i5A1R-LzWcBNrOTisuy3topQebzVZoE8CN5nriRF9X1QTo647BFX0Ee7xR_e8ZVLKVX6HJkQ8BA4bFzHON4eqvHEDg_GDsoXDQcpKGHfBjfpA0riT2mpWweow3v4kVFlF2hau5GAwuxJIXlSKTrHU_ylTrCm7Ji3aQUY0W_BjAkSvt1RLINKR_8xLAtiIa9ZU8Ui2lz9gfXPasLTix9xikh7R-wJCePo8469NHz4AdSrDioh4etlLIOvoPMTGqhtCcoUQE54dV5BlyjHRVsORdS4MX-kA0vTp6fhUZuhKwg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/0050768259.mp4?token=Zqnr4A98w4ju8ulWJL_JcBzIi32AoAja8MOjwVKm1H1i5A1R-LzWcBNrOTisuy3topQebzVZoE8CN5nriRF9X1QTo647BFX0Ee7xR_e8ZVLKVX6HJkQ8BA4bFzHON4eqvHEDg_GDsoXDQcpKGHfBjfpA0riT2mpWweow3v4kVFlF2hau5GAwuxJIXlSKTrHU_ylTrCm7Ji3aQUY0W_BjAkSvt1RLINKR_8xLAtiIa9ZU8Ui2lz9gfXPasLTix9xikh7R-wJCePo8469NHz4AdSrDioh4etlLIOvoPMTGqhtCcoUQE54dV5BlyjHRVsORdS4MX-kA0vTp6fhUZuhKwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
تصاویر بسیار نادری از به‌کارگیری پهپاد «گربرا-سیکر» (Gerbera-Siker) در نسخه انتحاری هدایت‌شونده آن منتشر شده که انبارهایی را در شهر کرولوتس (Krolevets) در استان سومی اوکراین هدف قرار می‌دهد.
پیش‌تر، پهپادهای «گربرا» عمدتاً به‌عنوان طعمه (Decoy) برای فریب سامانه‌های پدافندی استفاده می‌شدند، اما اکنون از آن‌ها به‌عنوان جایگزینی ارزان‌تر برای پهپادهای «گران» (Geran) نیز استفاده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HotwnUIKrWbj73ADV14Vvm2AI27sflvi8U9CvZwBou2SAV06fTqn_lq_4oo3pkAEIyNxtQPojqkLrCP0Gi2BHQWA1xI8LMpjSeXsiJys4UxvXY1DEBsNLJhUynhUdhSSubgbNcqVJA1gyhRjfMU4QmBfZjRRiv8daNUOBxZLALHbRdw3vZut5ig8d7pBd5xWUYUcW8da6aENJdupV_EP9b1eZ_iCoAuOMaZseJr4OM_6cOD_ZBs0h5IbOx7i_fdMNr_j8uhIal89srp9OoHOBUWrorxMNkejuLo68KpHSGKYWpZl0-V0O5vIUn4Rr1co-LbFY5EQwRKq9lIFGVVJWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از برند‌های محبوبت،با تخفیف و ۴ قسطه خرید کن!
😍
🤔
می‌دونستی می‌تونی از فروشگاه‌های فعال در شبکه‌های اجتماعی مثل اینستاگرام و تلگرام و سایر شبکه‌های اجتماعی، با تخفیف خرید کنی و هزینه‌شو در ۴ قسط با اسنپ‌پی پرداخت کنی؟!
🤩
🤩
کد تخفیف ۳۰۰ هزار تومنی: PAY3SCP
⬅️
از طریق لینک زیر لیست فروشگاه‌های طرف قرارداد با اسنپ‌پی رو ببین:
👇🏻
https://l.snpy.ir/v06dj
https://l.snpy.ir/v06dj</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=tlb_y-B94bx-0d8xO5MOxgQC4yDivmOypvdSuk0G3CkqGHBkecF2YpoaJobP2MZnQsMbToke0K97muBEIao9EDoTcidYmjmu80uxI4wSaeno5z-0x4WLWlElU_6CsqQA-koRTkatFZbHL2Dii0H5ckouS7d6s9ybDz0ZxixNzSCfWT25h74pNWDeL8i5_PweIg0k3B-MtpEW30oPvnYJvh-dkBsbbpTcz7b0HtzlE3ZMNFToSTllRF1FQkNfeZipHDuc5viJNWnH5Pj24Lx_ZsqYfSlDeSA4FKrntOOasnZFLKw_e5Ng4YrpKzNOEv2IQzbC6jQ2JP6vgvK_00fBHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=tlb_y-B94bx-0d8xO5MOxgQC4yDivmOypvdSuk0G3CkqGHBkecF2YpoaJobP2MZnQsMbToke0K97muBEIao9EDoTcidYmjmu80uxI4wSaeno5z-0x4WLWlElU_6CsqQA-koRTkatFZbHL2Dii0H5ckouS7d6s9ybDz0ZxixNzSCfWT25h74pNWDeL8i5_PweIg0k3B-MtpEW30oPvnYJvh-dkBsbbpTcz7b0HtzlE3ZMNFToSTllRF1FQkNfeZipHDuc5viJNWnH5Pj24Lx_ZsqYfSlDeSA4FKrntOOasnZFLKw_e5Ng4YrpKzNOEv2IQzbC6jQ2JP6vgvK_00fBHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnRy2vpmh0cFAPuGBjupLRaJ3hsj9whQzz2-ZkhORSowDCUl70Z1iVFkvdFjzcK2WzX_fQQG1jV3D1EpRfpQVWDnbzX9uwLBMBELxTpv1cC4HlRkE1aCeiOJl_wzwn5zPueGDXSzUVA_0gcQVjFrBoka6-FushrjVbXwKHKnqfY4sNJdBLzwA4pTXIjM4EFm6zsGMnUEEXtz5Wh_BulTRMDrrynEIVAxhzbQfB8ac3Fq0Q5qO2Qn__KNM1Osr8lLMWKn7aLjfnPJP3xEF1wZOEQdmS4pdKGDDo2ogYzWUqI4QSszqake43ZmHzsSQtSyDjtBU_jFJkurmLZYm-qQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXPGnPLvLJ9M-AbbEoaU8mv18vswq5M6OTlSGbnlJeA5vczIyogQsnUiU17vl5etx5780lNbnrAZjxbxAy1zPqkemVEi2j7t1uV9ijzO122uZw0e59dqfjFwrfr8d_1pfjscxd-9muKZrRLz5PtRygCO0aj525SpcTeCrcdrI5M6ru-McyeUMbxSWmInKtAOICAZiQkipDAo4YFFjk7X2YixlBl-UDpFoan_aonRH9eIeS61C3o7am19pEas5PmuH2iOqEkn8KqNaxSjaiA6T479vrZ0sjSaOG6DEt4TehxX8oRj_tnlDl2KNpO8wpFjlZklv0z2wnarLhPMjYC4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UqtH8wvNoUPRr4aMPC6OH3sOd7htCBNMsV6xzq9cS1sBf6NOy5vNq3pa78UeZs_hVtdDKnM-UvCM5rboGOWI6YySoqT5fvns4J59B8Alwma_EIGtjGlryLMWl7D5IlSH0PcKCm879WM4hdqsVSeJkNo0-4QbBw7g6v3bL-Q__zvn6P_AmASDmNRTSIhxKz7gnQZcvaBYGYO58Tt3DSrru9t9K-TTsuPgvmGCdZ3YHSgt5FuCJcVz6ey-GPOZ0TPQCsQmfSEt8ycwogMvwfDyDJMqnxLaSYlPmHg0wXQPTxoHsnvfQIyq7IMjigAMWAKHj_lIYQ9FQ7KI5fXiE0XnXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
آمپول لاغری زیکورپا(
®️
ZCorpa)
؛ وقتی درست لاغر شدن مهم‌تر از کم شدن عدد ترازوئه
در لاغری با آمپول زیکورپای عبیدی، هدف
کاهش توده چربی بدنه، نه از دست دادن عضله
.
📊
مطالعات روی تیرزپاتاید (مولکول موجود در زیکورپا) نشون می‌ده:
✅
منجر به کاهش وزن بالای ۳۰٪ می‌شه
✅
عمده این کاهش وزن توده چربی بدنه و سهم کمتری مربوط به از دست دادن عضله‌س.
✨
برای
شروع لاغری با زیکورپا در کلینیک ویهان
، پزشکان ما به صورت رایگان شما را راهنمایی می‌کنند:
مشاوره پزشکی تزریق زیکورپا
کلینیک ویهان</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYk8QNlFIiisf0MO-EqaL0GIKaNVYh26QccJ4w8Sl1OlNVlTfkJ0XfQhb54H8gygjwVSwugJ-jJX5BmgN_YWGf07mAC1Wrovoghx2WlS36MnCMrOL7ltl7ln8kxTg-G_AwI361G3KsKojri8GCsNHnS_8meistv5zFqcx7Du0Y-FIhKib_mvi2OIeE7XLw_3Z-p5dKGpVkQfPAi1RAovME1jbTIYmGmfQKpHLuIU8XfVnWdS96nmbQAav4wGGPXR941wS75Acgw7XJJg0d3FKHaOmrBJqvZn_OWNDR94pQHvqRYNmHGDHh85Jq7H6rb2G_xpfElUYBrtr_-HGMo41A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=aytcFjPL4e-i5aky0vHfA0WG9E_8SWIyDWRzefjP7kqvZVEQFGUafy_CZPFqz-gwe4eLUVepuTs3Vz14KEL3khY86s1TgoDbmSrvp2ZnPmc3iBnf49yned2rsZFB8y-cf28VEyRWD0Cu3msIgcsfxJgWzJmg703RE6SJbnSdMsIXh7iRvBCrXhpGACwiKXfF5HCSP2AceSA51NiyfJLUeT0rBLxbYI3F7dEbOMRzubZGWSLsR2VUGZ3LIxC8UANlvfmjwOskQbA1hK9Qmk-TM7G71PuFSnNJDgkTgm4pZgU2PSei40gy36_ic6NEBsMbp-J2INVfWA6tbHDhrDVgLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=aytcFjPL4e-i5aky0vHfA0WG9E_8SWIyDWRzefjP7kqvZVEQFGUafy_CZPFqz-gwe4eLUVepuTs3Vz14KEL3khY86s1TgoDbmSrvp2ZnPmc3iBnf49yned2rsZFB8y-cf28VEyRWD0Cu3msIgcsfxJgWzJmg703RE6SJbnSdMsIXh7iRvBCrXhpGACwiKXfF5HCSP2AceSA51NiyfJLUeT0rBLxbYI3F7dEbOMRzubZGWSLsR2VUGZ3LIxC8UANlvfmjwOskQbA1hK9Qmk-TM7G71PuFSnNJDgkTgm4pZgU2PSei40gy36_ic6NEBsMbp-J2INVfWA6tbHDhrDVgLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQ29ZJMjTbeZNJJdQ7ReotOVa7wPfpU8gHKcGaMrx0yIBZH_E_5LY4YBLToiFdd2QDNdVwIDZB7bbY4JXqIVTEsYaacxjbP6WuDEd7WozxnUN2MMt0WbjM6Py4JcTLxW_mbjz6G6gn7lfRxc9_M7pEbmMSSXu0UfQx5i4lwuhM7IyISrAjQJ51k8BtMSKAmmQPviTWPa1V6lxjfBggxev6QUlBD9OQRkfYQBOq8JElphmWDyYl9FxL6Pql0_G1rcgzbQNRrpzohB0Z7zyZrFnl1iZPZzzIZ0m3QpARwcVWBAZJHy_ll8UNw5Yq7tnwrgl0hbtEx9kJ84gznnDktvwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=bSL9Og9QL8Jv_OauGfgE0G2TMhXOjTY1_e3HK0QzTcrXKCel-1iUUYlOaJS5zV0R6GKvnTt7FrHGi_BvZTp2JtBrVhy8TaA9fJiPDcLm6w-KkVLC1e1wul4G0ITaDulqZtNZUo2UiPqchCwuAytGTT1I_xm3XIDtt5VWZPrxuDjj5GoPDwfkc8N20mpm45NVrd7TA4w9aNz40BpBstTeWJYkYKKjU-L3K1aVZwMdNXLW7sOWdDmOdVA2Wr-R6PdE8qjfW6nfuJRSrmoqM9DQg-47W0RtMfJl2gdCqBEl3QtnnkIHjHJPoPgX0Q2ijd51QThq5RMm1lpgiKAXviy0hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=bSL9Og9QL8Jv_OauGfgE0G2TMhXOjTY1_e3HK0QzTcrXKCel-1iUUYlOaJS5zV0R6GKvnTt7FrHGi_BvZTp2JtBrVhy8TaA9fJiPDcLm6w-KkVLC1e1wul4G0ITaDulqZtNZUo2UiPqchCwuAytGTT1I_xm3XIDtt5VWZPrxuDjj5GoPDwfkc8N20mpm45NVrd7TA4w9aNz40BpBstTeWJYkYKKjU-L3K1aVZwMdNXLW7sOWdDmOdVA2Wr-R6PdE8qjfW6nfuJRSrmoqM9DQg-47W0RtMfJl2gdCqBEl3QtnnkIHjHJPoPgX0Q2ijd51QThq5RMm1lpgiKAXviy0hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SB2KwXNXg0wvKwtIuFYXnt_XCnIPQsi919X-sE7nUchaWmfSG7k0tV67VqUtlkCVvaaE7JN1Ftxq5TJ0hXUOdZlux8BzEOK4fTM88rrNQfAw9KXxzQJ6fB4e64GLnBnQJAlV-yeFr_TCnTJFFqptkOFjMzZfFfVQ5Z5fILiSSbleOy6uA7LFTp65l6grCh70E920zrJh0lWB69rydGNIGhcpgqu6FFxthmTh1pafskBHdjPDITAAmHoRtVt8GIbBKQtPwOUuVRLGhTGRh8176lIWTUXrdQPkrKJF-6CsqKn5yv1U4lbor5RIvo8A1MCgTP_9u4MPP2BVzbjwzABnbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FqLjUcY-9Yr0hgApIx77Q2b1dC7a34AuuJXwhclEy8Fou7WMogdPepAFJALJCefonMD1JDPpLRAHfkK1CpEWm5H7cZZggoDfikmuutHWAFIaf4sPEwcRnaxiR9IVt2t_XK4jt1v2sbAZ3zGs2ESr3kZJ236V7wPe7hXDooMcRsyRsNBFGusiEvMVsvXWb4e1FwQ49WWgLZslHEAKyP0GBahpjZBgODdMfSxZ0YN9zqgHnMMvCKM8Pg14YuNKwe2hIwyCgQdbKDE9hfA0E_GhqP64FKIcMsjn7mF8AHeILLO9mDXAuBPJX2Jb83uCRJivIBOPz22DRGo6JK6F8PJ-NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L3bZODXPjQIhetNvmBf_2oRiXxyrYUNc6TpH1OFHV9nm4jPyEiwNolMsOG3nCBqvFwmOCn81k9_VtzM-A2RiWbokKRp1pUibktUdd_6g-dNeMl7pd-wVpVQruPyJXbY3WiRRTBDSTMma_x9kEol4ZUttnV2Tryng2NBenJlNLxdjtm5KOOfbRHDpGlWTLiMep5JaQis4QS28ETuozpsHMerWS5PIGaiPpFxXGblAs-Z_IitMNA4x9ydzCGOsgOhW5_dc7kwWj7_IluG9cRaNvDoHItuVP5c_0d5JJQ07lxQFQOx7Bf4Bc-Du1WS_V_f6Z2gNB4DVaT4SQa7_rEXkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Sn_i2W_3NR3k8IEuaD4P6Y95d1egyVecB5xIOjUlVgKCIttUpCcKUTNCGLGnef2xbw-wtsxOTMaWpPv0L_tdh-WY0A1JuGCRb_ILJ8nd0jwqxoZ9XhflC-97QEMn-kxVtmsZtiTbvz0FjoJSWezQ9a0KjqbQhd30HRguNfUsrdMhhTKIwAX3VG-Zlyz0vsIZdT4EbmcMp1lp1wwq85tFdvtf9hGTthrCinWOqkQzfWQuE6QUgUmXYV5mVkGbJ2u1eUAq_VJQQYHkyGoXStAiKcZsmA_OVi1vhHU4KASTxKPVYO3_PkKsx9vWuq-90EhvIeGc4XZsUDUyqcYIULbxcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cfXo8EwX49z4_KnwCbzRdE6KM0ZU9MhLxyA91SjA_8NBLvRBxxY6J3iJ0p-hD8ijabfkHHxeKb0mmBM2y0iy5gBjgfOvXniqxpEKZ5BNl-QwRT_c23fvuKXcKvvxZpaFcmfnVrwbrdTBdtbyFksfQahc-YX-d32cKiiRVSzRnlr0VL0OxHh0fTzadQSvZjHrYumpqpxud2nRS17qzV8rnU3gh3inowzzUZg0ZlvUSUVF41aAJ9ZvIkH5PIXVhqKJPBZCqzgsmSTBVQAd4VYiNuz5Ow5FLKPY-qWKicJjvM5K3OCF-6g01Y0RxYGQWBdbzt6pLV3Zhb7_CDgj2FwEmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vv2WVvTQLsY-u8D0MIAKTee2SZGWcBSyucCavNd57iXnsFIHDj-Fhmglhos8G2q_eYI4BO6-QZbav7VwB3d6EjGeaSWJ8JVf_IoVZ12-qAvksi23jlNy9O3QiVt6lWB7b42SuOTry2QunWe-YhHGrfF99D3l7dyfim4AWOhWk1fbJ-6nFXO06N6oQtZ7k-mlKhqs2lG4nUkSdIvkFeOJeSAJ4vT-z6o4OelCRqM6H694kge_LpXZ5-3GWbHgpQHzwZedO1i8ELvFxJ6Kbd77lHdC2zKXVfmIZKYgJ-M06CM0z56difu2_5oA_zLSMIuZmLc-ZgqDkruZ3VL1Hypcrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tajsp0ueu5o22CQWB7c3r9W9AChQXt2Hh-knUMbInlqYorgjflo554J0l10s6ZrelFX1jmfPC3MRL66nCzmbBMk9m5IRCOdUrbuJgj8mQM2AM8fbf7KFVo0JU-M4T_hMEq-U6ZTFTpyokcCSLzOU5OtGjLR9-jv8ZGlEVzaiCUnJeH3DBGiJHG5Jedu2hBzp-ZKwIKkyGlllA2x9dbnwNROLG_CFoYuibCylalwRghg4Z5ShBAxZ0JnnWmw56OdUqFqWaiHoc6HaSB3FZSgbJtkODV6Y_WPvgMaQo5m_PoLzuojxnP_0Qcsg35R5GHz_8eieHqYSxy6lGXwySp_Wmw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=QVOIi9GZIYpdPdmLi-QngT3XekAQzm4EscSXP46PU3NcgprSQYas7xEnP5x8rfVcVjzfFHTQ2Zix2tvxzrU3FXyepUyohph2zTFrl6b9pBzSlkd_RGYHaTDV-Up0FrTqQPAlHvODTAtXTei3GHTokdL8pFV3t7F_cwI5hm6-4B5TnqpiylB9z9oOXx1Z1eb1tS9H1NO7XZlVuTDldyc3NvDmTJC9FBnLae3z8fdFF94dxiUAKqKO_tuSYearH_jer_ExcLP-lfPIVuZLIXOdcMrpzYBCi0rZsSwLb9TBjdAbmPqSw-7YSNOykFpDvdz4VBf9NMqs2riHN3GJVLCCAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=QVOIi9GZIYpdPdmLi-QngT3XekAQzm4EscSXP46PU3NcgprSQYas7xEnP5x8rfVcVjzfFHTQ2Zix2tvxzrU3FXyepUyohph2zTFrl6b9pBzSlkd_RGYHaTDV-Up0FrTqQPAlHvODTAtXTei3GHTokdL8pFV3t7F_cwI5hm6-4B5TnqpiylB9z9oOXx1Z1eb1tS9H1NO7XZlVuTDldyc3NvDmTJC9FBnLae3z8fdFF94dxiUAKqKO_tuSYearH_jer_ExcLP-lfPIVuZLIXOdcMrpzYBCi0rZsSwLb9TBjdAbmPqSw-7YSNOykFpDvdz4VBf9NMqs2riHN3GJVLCCAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdlwklbVIpJoDfQIxd5UCz9AxvMgT2DgaXldvpXNMJcQRrFMBT1f1F9GR7Ct_lAPSX2KMvqnbhO0LlWRAjP8p6jQJh0ZfQHR8FVH76Ch4yCnNnyZ8bDGLv5pAIMyTlvGqoM5yvk7r5kUM9OWf4WqFK0x8tFd2plo7FL33IHbnmcYNLxLIauI5CQSIaSRH3Y41aVOSxRX0Mkb9Mz09hsTagCHeMQwEPb9zDlXe_Y3N8geJEFIMQ_6ko5GFnceDWn6vX_D7A_SILLGP0KQRKerDQ3ocjgEvaspgU0IDgzYgdSZsT_zHcmzZ1H9V0SZuf4zcqETMqueBSbanzyV9P8pZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=nwJDUsdUFdvG15eH0RxadsqZFRsy-QX0-cdTXfLT3E8FXi26TP_g2U-W5QCrLsgkCRtDA3e5eXrknq_B9JY8zFRNmfZfhub-tdI9kGU8RZSeXetJGIbBt8XtKppimVP-_oZzoM6f1F7QLHzAy9tSjSHdpwxWqX-EopLglC6uG4jMnBDs5Y6kIde9wPj6Ghx5cEAxzK1KxPu0RJ85rz9toPlaW0ZsQcS-2KjXYyjAV3PJCdufdXBorwEuNBrm0vfaFIXcE2zhp-dCmjHzDHWlsQuCgupJ7Tu_kcY9v4KnhYQ-5Kuyi5gH7H2jpGmVdZB95ve0Teg8eSF5nThu5hJzHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=nwJDUsdUFdvG15eH0RxadsqZFRsy-QX0-cdTXfLT3E8FXi26TP_g2U-W5QCrLsgkCRtDA3e5eXrknq_B9JY8zFRNmfZfhub-tdI9kGU8RZSeXetJGIbBt8XtKppimVP-_oZzoM6f1F7QLHzAy9tSjSHdpwxWqX-EopLglC6uG4jMnBDs5Y6kIde9wPj6Ghx5cEAxzK1KxPu0RJ85rz9toPlaW0ZsQcS-2KjXYyjAV3PJCdufdXBorwEuNBrm0vfaFIXcE2zhp-dCmjHzDHWlsQuCgupJ7Tu_kcY9v4KnhYQ-5Kuyi5gH7H2jpGmVdZB95ve0Teg8eSF5nThu5hJzHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=XEqhEvd3UlOJxez3Ym_G2MYLEe1FWCVD06NdAhx3wNpiA6r7NpNlPH5DCq2SIeokJ0q_K46Al0Rndo9kkyTunwaixvRNVjxK0ucSY7xwhZxTUi-vK-eFdq2fji_NG_vdc_Hp7yiUjwaepHK7ZeV9i4Uq41zmU__J3bxoVXm7OWWfRhjh2ktX4Mb7yrBiYQhynEm4AdSLHYTEblPSLlHpCzCFl4oLOXpn-tR53QTs1ls8oitlESlADrD9y6cDaNoOAhLBx7cTNbEhqk2xUDliXt0yt1zxu8wMbFHC770ZwUJ0ixyPWbADz9D3xfS4xDYUREQD6pPSnLZPqKZlWojhPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=XEqhEvd3UlOJxez3Ym_G2MYLEe1FWCVD06NdAhx3wNpiA6r7NpNlPH5DCq2SIeokJ0q_K46Al0Rndo9kkyTunwaixvRNVjxK0ucSY7xwhZxTUi-vK-eFdq2fji_NG_vdc_Hp7yiUjwaepHK7ZeV9i4Uq41zmU__J3bxoVXm7OWWfRhjh2ktX4Mb7yrBiYQhynEm4AdSLHYTEblPSLlHpCzCFl4oLOXpn-tR53QTs1ls8oitlESlADrD9y6cDaNoOAhLBx7cTNbEhqk2xUDliXt0yt1zxu8wMbFHC770ZwUJ0ixyPWbADz9D3xfS4xDYUREQD6pPSnLZPqKZlWojhPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=mnG_npOKvzlueX18KafaR-hTZG6Hk6X_R2cAt9UjdmIsdX1FJ578-_25svObsNh_yrZAKJQJCxlwMellbBYiCShYIt8zJOwZSPOnIxSJlf54_CdmljeFR8tQ3vXEnY-WUXnrdvzNW1hKjE6fSKHfynJb2hr2ErfO6sAeFWpWhViY22j_JaNEmQHeOFHHvcS6wjWJBNpF955EyugRMI7JXw2-nSp8dZfolLf0l5MnU-qX3pMKvZbFaOssBwc4we1V8IedI2wwu-AmJwpYKIVcrwdLQQ8xkxplz1NBZjjlQwcbRgD3OB73iar-0u9GnnAysv5LQHfUBHcqrkDpS4mTjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=mnG_npOKvzlueX18KafaR-hTZG6Hk6X_R2cAt9UjdmIsdX1FJ578-_25svObsNh_yrZAKJQJCxlwMellbBYiCShYIt8zJOwZSPOnIxSJlf54_CdmljeFR8tQ3vXEnY-WUXnrdvzNW1hKjE6fSKHfynJb2hr2ErfO6sAeFWpWhViY22j_JaNEmQHeOFHHvcS6wjWJBNpF955EyugRMI7JXw2-nSp8dZfolLf0l5MnU-qX3pMKvZbFaOssBwc4we1V8IedI2wwu-AmJwpYKIVcrwdLQQ8xkxplz1NBZjjlQwcbRgD3OB73iar-0u9GnnAysv5LQHfUBHcqrkDpS4mTjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما محاصره رو برداشتیم، اما چون اونا توافق رو زیر پا گذاشتن، دوباره محاصره رو برقرار کردیم.
اونا مدام توافق رو نقض می‌کنن. دیگه نمی‌تونیم اجازه بدیم به شکستن توافق‌ها ادامه بدن.»
«ایران تنگه رو کنترل نمی‌کنه؛ ما کنترلش می‌کنیم.
اونا شاید بتونن چند تا مین دریایی بندازن و اوضاع رو به‌هم بریزن، اما کنترل تنگه دست ماست.
حتی یه کشتی هم بدون اینکه ایران جلوش رو بگیره از اونجا رد نشده.»
«وقتی قاسم سلیمانی رو از بین بردم، ضربه بزرگی بهشون وارد شد. به نظرم اگه اون هنوز زنده بود، ایران جور دیگه‌ای عمل می‌کرد. حتی ممکن بود به سلاح هسته‌ای هم رسیده باشن.»
﻿
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=i8HVXMXuV9l5jw7Re7G3DhjgYJA0c4D0xIAEwtFae8AbTlJmiA8nnaOHlXwOCqKJALZJRB5OtvKZROtNTaD3Zq9HY_CMwDyKnYCyg9mZqaj4D3EAiZseaJHscQJhfrIgmiAsOXLqisI9ksrWty4c7B9RattVaxJKlyLT5huNt5Mt3L4D5uusUh7awO1ypV4E-lCiiOkGoJtJhm5byXxBuzDnEXfTeGRUxHy6lLS5ttohA4bYtDhndj3f1LfS8dusl-kyH2kSVBxPzq401fs_ZF6p9Z1mw8Eteb4cX9j2KNWc61Ky4oK962tK1zGxrm-tDYqprZ_l_VlEnlZ0nctiDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=i8HVXMXuV9l5jw7Re7G3DhjgYJA0c4D0xIAEwtFae8AbTlJmiA8nnaOHlXwOCqKJALZJRB5OtvKZROtNTaD3Zq9HY_CMwDyKnYCyg9mZqaj4D3EAiZseaJHscQJhfrIgmiAsOXLqisI9ksrWty4c7B9RattVaxJKlyLT5huNt5Mt3L4D5uusUh7awO1ypV4E-lCiiOkGoJtJhm5byXxBuzDnEXfTeGRUxHy6lLS5ttohA4bYtDhndj3f1LfS8dusl-kyH2kSVBxPzq401fs_ZF6p9Z1mw8Eteb4cX9j2KNWc61Ky4oK962tK1zGxrm-tDYqprZ_l_VlEnlZ0nctiDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه دوباره برگردم و بخوام کار رو تموم کنم، همون‌طور که بعضیا دوست دارن، خیلی راحت می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهم ایران رو نابود کنم.
ساختن یه پل حدود 10 سال طول می‌کشه. پل‌ها سخت‌ترین زیرساخت برای بازسازین و بعد از اون هم نیروگاه‌ها قرار دارن.
من می‌تونم ظرف یک روز همه نیروگاه‌های برق ایران رو از بین ببرم. اون وقت حدود 91 میلیون نفر بدون برق و بدون پل می‌مونن. برای همین این یه تصمیم خیلی حساسه.
اونا می‌دونن اگه به توافق نرسن، من این کار رو انجام میدم .
پل‌های اصلی واقعاً از بین میرن؛ فکر می‌کنم تو کمتر از دو ساعت بیشتر پل‌های مهم نابود میشن و نیروگاه‌ها هم ظرف یک روز.
ولی اگه بشه از انجام این کار جلوگیری کرد، ترجیح میدم این اتفاق نیفته.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9Hjphz6gMmlq096gCjh6Upr1AkYAq5fxRpwtcMy40rwZDrWk1wnNTAWcxkbXNwSVq_U5eczf-GIqPJRJlgJ5aIKGSrmms0XzJUihI-_TKfWcIJ9xhm81rKc6Nzi0zijBkC3SJ0RzlvAi5DLMSrB5D17UijeWAMaP73z5zeJHygUsjxRKT8J8D_zMDoXCkjdTdPIuAH5WMec5CcvnQDOjcziyyPk1i9VjRNNKRFYSW90k0MviKglEfWHTx8gFdvB7CI4KO1Xp3NykQcDCKnE6wK86Z4xR-fgZgKbbhlFc8kyh3XlVF0bJc3G7_qniNPerkv0jr_cl8FUzQiZkl37GJHbSGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=DL5h9EQJPyEKJdZWF3Qv-VByX5yBWpfH5rGCkmgF6xThHL_A7qkeDjyjA82ZCQ-2HtL7iGhRAwYv8pcWJ0UmiM6VTQ-CxFwdo9EkvIJmZzni-bCBh447R5UFhWBUF27_vJHOR-0_2ITNp_dkTvQmZe8HL9CD2NnxGC-y9XcqCa47tpw9edERaGe9K2NL4taY9M9xIGKp9jDe86QY6nHqh_5NC40APVtQTjce2H__ImC2Lq5cg4wV_M4FIV8HT74GD8a2Omi-2ScO-NeJfVWKy4juV2ursnMPe4wPCRyyFBOhwcxaZSt_K19eqNPDYaFh2xPNWCtxaPVkGsfzD9Hjphz6gMmlq096gCjh6Upr1AkYAq5fxRpwtcMy40rwZDrWk1wnNTAWcxkbXNwSVq_U5eczf-GIqPJRJlgJ5aIKGSrmms0XzJUihI-_TKfWcIJ9xhm81rKc6Nzi0zijBkC3SJ0RzlvAi5DLMSrB5D17UijeWAMaP73z5zeJHygUsjxRKT8J8D_zMDoXCkjdTdPIuAH5WMec5CcvnQDOjcziyyPk1i9VjRNNKRFYSW90k0MviKglEfWHTx8gFdvB7CI4KO1Xp3NykQcDCKnE6wK86Z4xR-fgZgKbbhlFc8kyh3XlVF0bJc3G7_qniNPerkv0jr_cl8FUzQiZkl37GJHbSGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI4aJdXbdhCNyzJZz053vCfSnVC0TAlTSdJnjBt4n5tGObAZ-SLAg8cNXref-qg1LUqHK1oAeeP8Ey2LMZNPoLy_3OkmSD_zNvClYfqXSPRzguTGw8quDmdQE8aY7P2vNlVDElfQILyF2LkHV0i8z3iCuPal8AMxFXRJwSyPRZy-1HJwxvxvI89CG_zWInIGYSKz6CwCwKqXVCgJluYTgH_VBFM_ICD0BDCh08jNJvzctJ3IzRKPg3yLyjEkWsaf8Vzrc6-nM-7GL52m7c0iiy7-lxtvR5ty3lWERvqKbDYBgh3nw4suE2bQkSKJHJ3kIRUwGUxiHpM25tI_kFgfqy5U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI4aJdXbdhCNyzJZz053vCfSnVC0TAlTSdJnjBt4n5tGObAZ-SLAg8cNXref-qg1LUqHK1oAeeP8Ey2LMZNPoLy_3OkmSD_zNvClYfqXSPRzguTGw8quDmdQE8aY7P2vNlVDElfQILyF2LkHV0i8z3iCuPal8AMxFXRJwSyPRZy-1HJwxvxvI89CG_zWInIGYSKz6CwCwKqXVCgJluYTgH_VBFM_ICD0BDCh08jNJvzctJ3IzRKPg3yLyjEkWsaf8Vzrc6-nM-7GL52m7c0iiy7-lxtvR5ty3lWERvqKbDYBgh3nw4suE2bQkSKJHJ3kIRUwGUxiHpM25tI_kFgfqy5U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=r5qAq7ZYktO-fFqmnJMdF5VLPCyoajapYECrwZVWg_wOMRrgw2Pwr9URXZoyAgV5Wr0j0ZfoNLthkRebiRWkNz3zcWks5PQKFbkdasOKYfYUACEalsu1gNn5sCpcUIawO-47pldab1P9Jyrc5pzYMnB2H2Tznp7KyiRbLcuWFBV5oA5OHetz3NZ-fKgnM5XLG9c12jkkVmMnn6E9KVJmZ9NBJGVMxym_8qWbopHLwb7BlDxuLeNuVclCpogs5bq1939BI5nMlXlAx3sZ6j3CmcqhxJcc67-8ejWc5E4gXgTsT92_CkPCAO1n8pGLmiub07zTUBd1RcGKt40tUHnHoV4pWXB213UzyCtsS_JRMgZDbVjwtNblZWp7m2FxPTcPF-ojqVRCH-3Mu4lazJW49f08Wzy9pxlKI1QHH_IzLal_jg2SYngIJa0NOWcGxPBwYop_OnKoSuI1t_4R1B7UiwurV2HAcKPVxpdOC4Au-b_k5IOZ4SCxFFWEhlWW5v4jdZzbbzW-KqSk7vQMJz6ZdqhQZu43ZLZqzPXu30hMmFSu9HNl97y2WZxrzVf8b5CNHaf73LoEitiX6JdIv6beEp08L1OsKR3KgvUnrmqyztHNTZ6VZte5WPtwmOUJ-B_KNdHBfvpwiAzoN4Qe6zjeoJ2j4Kk1CvDn0xTrK7GVsd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=r5qAq7ZYktO-fFqmnJMdF5VLPCyoajapYECrwZVWg_wOMRrgw2Pwr9URXZoyAgV5Wr0j0ZfoNLthkRebiRWkNz3zcWks5PQKFbkdasOKYfYUACEalsu1gNn5sCpcUIawO-47pldab1P9Jyrc5pzYMnB2H2Tznp7KyiRbLcuWFBV5oA5OHetz3NZ-fKgnM5XLG9c12jkkVmMnn6E9KVJmZ9NBJGVMxym_8qWbopHLwb7BlDxuLeNuVclCpogs5bq1939BI5nMlXlAx3sZ6j3CmcqhxJcc67-8ejWc5E4gXgTsT92_CkPCAO1n8pGLmiub07zTUBd1RcGKt40tUHnHoV4pWXB213UzyCtsS_JRMgZDbVjwtNblZWp7m2FxPTcPF-ojqVRCH-3Mu4lazJW49f08Wzy9pxlKI1QHH_IzLal_jg2SYngIJa0NOWcGxPBwYop_OnKoSuI1t_4R1B7UiwurV2HAcKPVxpdOC4Au-b_k5IOZ4SCxFFWEhlWW5v4jdZzbbzW-KqSk7vQMJz6ZdqhQZu43ZLZqzPXu30hMmFSu9HNl97y2WZxrzVf8b5CNHaf73LoEitiX6JdIv6beEp08L1OsKR3KgvUnrmqyztHNTZ6VZte5WPtwmOUJ-B_KNdHBfvpwiAzoN4Qe6zjeoJ2j4Kk1CvDn0xTrK7GVsd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YZUdTt41swQaxynaibOBRq3x2epQwXuaDZ7yC_B9HgxBoNqLcpQFPc_mGq06UWzpj6bkv8R9Ix0vDY2z6SEbjFkZiGlNoBI_7p3JSzKsjs814AYt9jF5N7Jb4iNxrKoEeL-vpg6NvS4A2XcM_TB542K8IlEjgo_Jwhszy2JZ14uf7npcsvpskDr5WDegsVA6DcRSCdQRllKb6qVpzdkZ04E74FEJ8sQ9r1mII99bEb_rtfLcS6TVEQNyuGH1HheLaDiEJRuquFDq6RFemJrW4PyS_fIRUl6tD8xR-fwJDbF783dBt57amd8Rtzrepmaolj-rV-6YoHE3AYUuRYcSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LmsA4I4C9eDRaf3wC7jM0B57U7sLyfwpREiXRAW1x_qtcoEGkH4oHlcLDPk_50NMPCAintCPXSk3NZGfVpFHfKmz10vxCymAQeFM-6c3iYP-wWcKjPNSNbno1GbqGJ6R3WIeZBeCSyks4Aiun5GMIEecUZ5T4OhxbASwZO2gqGqFLidhN0xWN0gLtUwlG109r5h3iahbxJeZ1X6rq7Ky93tw5nqSzBnI5sIEG2q3wHsnenuHeMNkLRuiAt75_KRlZtswsk6PKU0cki7sI73129PeD8F7TO6HN7TYXz9AQ8ToepgACpqgHR44NDPUiKFGn-VNSZKQKxGAtPjHosKxoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=EZ4YaUnhybpmnN939cVIlDRKASKr22U6PA80qFIz4ezzbZUyQi9DMXPqWp7tAP6lWqxYfVziZKqgcelNz8LcvunPtLlr_1AOq4qkLvAqaVGn-DJbpLLdHLBOdN1kMCt2S7zPeJV9H9FVjRs03AHj4HSSCTqqKgIkl_6es6c3McVbz5YxsQ0w7OS2fCDYYNOOrfzAP1B-9UzTqaFFxP5vlO8xydofm5nkxXIYgmxVofsXNgMxUA3PLjmmT4ybQRIAvtvHm44rckNHMJpV9_ntLcZ_348XdtuTzSpYcN8UpxLKDXlpbbJWmX64j4ULYa_2_agZZUJVHd0cu6VNZwtmNDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=EZ4YaUnhybpmnN939cVIlDRKASKr22U6PA80qFIz4ezzbZUyQi9DMXPqWp7tAP6lWqxYfVziZKqgcelNz8LcvunPtLlr_1AOq4qkLvAqaVGn-DJbpLLdHLBOdN1kMCt2S7zPeJV9H9FVjRs03AHj4HSSCTqqKgIkl_6es6c3McVbz5YxsQ0w7OS2fCDYYNOOrfzAP1B-9UzTqaFFxP5vlO8xydofm5nkxXIYgmxVofsXNgMxUA3PLjmmT4ybQRIAvtvHm44rckNHMJpV9_ntLcZ_348XdtuTzSpYcN8UpxLKDXlpbbJWmX64j4ULYa_2_agZZUJVHd0cu6VNZwtmNDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=Ls4hfFzZQ4XgfgyefL586k5UW31QlLvH0vUq1C-NBpUC0zhE02RC6Sa1nOtDKFSFGF2XWsZHCeIO7JsTg5BlG5yweAArAjJa7FyST9t8VexwwVlYZA0zEueEF152PuVcCSWsgkpffeTkMxSs-y2_Dhgj27UBC432dRxiuiVu8lNsElagZw8mvHa7uYJvIT4yqCfTzXvCGn7rCqzeivu5gmTdoPoMCKnrhyVacCo_e-9xLstlatZ6xr3__4_AysS66BusuZE4QN684Q7uLmKP48MZd1UYaliUWM-jMlrJuPhEQ23zBhSiPz3M9xlXw9SNpqqH9m9cI5enwsXSCHk7wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=Ls4hfFzZQ4XgfgyefL586k5UW31QlLvH0vUq1C-NBpUC0zhE02RC6Sa1nOtDKFSFGF2XWsZHCeIO7JsTg5BlG5yweAArAjJa7FyST9t8VexwwVlYZA0zEueEF152PuVcCSWsgkpffeTkMxSs-y2_Dhgj27UBC432dRxiuiVu8lNsElagZw8mvHa7uYJvIT4yqCfTzXvCGn7rCqzeivu5gmTdoPoMCKnrhyVacCo_e-9xLstlatZ6xr3__4_AysS66BusuZE4QN684Q7uLmKP48MZd1UYaliUWM-jMlrJuPhEQ23zBhSiPz3M9xlXw9SNpqqH9m9cI5enwsXSCHk7wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=uAhZoMhEuy3oFPbA4vMbn2hxEmzJUWxZxcJKkCGhoVEGE5z29TnzQ1D8XM1kXTrG3AtZJH3rOOeiwSRczAVjCsKlPmd3QaeH4kklQz9APTyfKIPiDkl6mFOI_T9K6UMhv4aOcz94Bci9f9w51H7SZ4uWiiHhfgTr87bifuyGzFjW2p4DcXtdNSqPYn5_tYjla0b2qWjAfWo-87ISHreMl1ydj3Dxm-mLxZPX7cFwSZVXTk-0hbyhz3udTcxcXVB9_pSzjGzcWogspeB3TLM8SxY-3NjKvrk50q6iAAIGlcGAHgSUIqdatPaB1iSsMvQFqBlsY9hgAzrM67kkB5Ml3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=uAhZoMhEuy3oFPbA4vMbn2hxEmzJUWxZxcJKkCGhoVEGE5z29TnzQ1D8XM1kXTrG3AtZJH3rOOeiwSRczAVjCsKlPmd3QaeH4kklQz9APTyfKIPiDkl6mFOI_T9K6UMhv4aOcz94Bci9f9w51H7SZ4uWiiHhfgTr87bifuyGzFjW2p4DcXtdNSqPYn5_tYjla0b2qWjAfWo-87ISHreMl1ydj3Dxm-mLxZPX7cFwSZVXTk-0hbyhz3udTcxcXVB9_pSzjGzcWogspeB3TLM8SxY-3NjKvrk50q6iAAIGlcGAHgSUIqdatPaB1iSsMvQFqBlsY9hgAzrM67kkB5Ml3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=nFTScCHTbrdQEEuRv2u4xWHGQae-FEQia1XU6iXHTUGC8w0eDBBVsjsKJ3BccPANs4PFd9ci1kG-HU69iftmOccJEgF1_10ekByDemTu-niSIUPGm7JQ2KyaogII1Vm2UUD9KSV4WwxTarPLbE4XdfsMTF1ITBqazhJlc9W-EIuCNzR6XNhS2V14Sx9TbznZkqJxPetlv1zUG3e3-VOM0SJHKyIPgxUo-7De2XdD8N0lCmTR_J-WXgdQBfg7IexDDkt4imIXR5urrNneRVxiQMpapSjjtT1L0s52YXA7TrdW-TRQL0lPgTry9p8yE2mo53qWoMWh3dxfVz2HBZ6t6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=nFTScCHTbrdQEEuRv2u4xWHGQae-FEQia1XU6iXHTUGC8w0eDBBVsjsKJ3BccPANs4PFd9ci1kG-HU69iftmOccJEgF1_10ekByDemTu-niSIUPGm7JQ2KyaogII1Vm2UUD9KSV4WwxTarPLbE4XdfsMTF1ITBqazhJlc9W-EIuCNzR6XNhS2V14Sx9TbznZkqJxPetlv1zUG3e3-VOM0SJHKyIPgxUo-7De2XdD8N0lCmTR_J-WXgdQBfg7IexDDkt4imIXR5urrNneRVxiQMpapSjjtT1L0s52YXA7TrdW-TRQL0lPgTry9p8yE2mo53qWoMWh3dxfVz2HBZ6t6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=ZZdhYjpqk_CjWTQOHgkoSWe57bTaiaiIhWNuHxp8oaogw_6bSv51WtMgQNRUJFe8Cicq_xegvtslLcb3eR12u5rreUPUt_GtZ-92yNdjMosvMV3fBa136A7MrKqFzOrTLwVp1h29hKo8mOa5gnDIHfU7cE5NeoDh2KLE2QXyGHnfr8vXgXiKfBm5pMjyxSTzqkyhZydqOyaF2K0kYov94YujVJd0kYUs7wB1NO-31OwB2e60gG8S6wBS-iwzC4Blk-pGiSdVw60uS3YffmL24On5NfwT5v76Lph8imb8r1VdK8ujxJihaRQpDujvSGnG--aRo61eXNrz-D_GYUOnGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=ZZdhYjpqk_CjWTQOHgkoSWe57bTaiaiIhWNuHxp8oaogw_6bSv51WtMgQNRUJFe8Cicq_xegvtslLcb3eR12u5rreUPUt_GtZ-92yNdjMosvMV3fBa136A7MrKqFzOrTLwVp1h29hKo8mOa5gnDIHfU7cE5NeoDh2KLE2QXyGHnfr8vXgXiKfBm5pMjyxSTzqkyhZydqOyaF2K0kYov94YujVJd0kYUs7wB1NO-31OwB2e60gG8S6wBS-iwzC4Blk-pGiSdVw60uS3YffmL24On5NfwT5v76Lph8imb8r1VdK8ujxJihaRQpDujvSGnG--aRo61eXNrz-D_GYUOnGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=timhgp03b_KrXRMHuK6YbcGZolZRBWRZa4PKrE0y-cDzXv_SuNeSnZk0LRDGYpLeM_xv1Oxv2To3eR21mof5m65osTwfdVRW8wdgvrbVdkVd-GeUxUPzFFv_xVzll9dw_hnIhob7xUL7DYDuNnbtrnLAKquIv2ioupgIu46dfDzgMdgLuJHVnj5KNT0wicsLvR8uubeBCfcG6W5bg0w3Q2Ak3CzT70TBcgYRGNcyOsqH4GbpfIxwbFxepfFKuJdTvgUIKMTNAV-Qmw_XCm3taQ1Dw9bIqiSSeG68exnyQNNluFTJ-Am16Mth59oFVkOKUFeCEtspxA9WHAFKgEB1QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=timhgp03b_KrXRMHuK6YbcGZolZRBWRZa4PKrE0y-cDzXv_SuNeSnZk0LRDGYpLeM_xv1Oxv2To3eR21mof5m65osTwfdVRW8wdgvrbVdkVd-GeUxUPzFFv_xVzll9dw_hnIhob7xUL7DYDuNnbtrnLAKquIv2ioupgIu46dfDzgMdgLuJHVnj5KNT0wicsLvR8uubeBCfcG6W5bg0w3Q2Ak3CzT70TBcgYRGNcyOsqH4GbpfIxwbFxepfFKuJdTvgUIKMTNAV-Qmw_XCm3taQ1Dw9bIqiSSeG68exnyQNNluFTJ-Am16Mth59oFVkOKUFeCEtspxA9WHAFKgEB1QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r4PcHK6D5Hre-BsdGjLyM4qUJkcQDTAQFNlgijFoa4JlUmvHJgCczSKw0dEiwscYZ4n87KU6PL1awDr8hX8664SXyYHtrHcq8v-lCIMgXedrcRc1-7UU11eygFMwEXjwY1Ossjlgss1kFgnceyV8cr9jI7P-TSwdmxOJ5hKraXoj2qtur_CzKNipGOTwilV_XO5uptIL5hwe5tAKX0Q7Z05wIlZ65GZlWenXYIVSnMekP7bnWADy5v9ghZODS7zHyj7GHAx1L56ttmip9nd6y0Uf1ce9YtNIwO5jCw-uGSjKz2tMde0DW7yfu_iahdES6rWjy98gxiqxymY-I2reGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOEnGUeQYrveImsx1Lhg_xMsklyCdJQsa5EGjaAj7i8gCj2xghElYkD6OpaX6N32wZd8Mu_myCMY7kucXJO4SF3bdv_J561V6h_-1nywOsx7mOKLqH4vXLYoi5TpW05Ab5UlQYCKCaR48QA8ZS4d7Nm-hcdMt20qw-xwVRA-5RFU46ev7oQeP-NmHqqe0fFxvlKjeFwYdfCrH-wAluTPu2wwy694hQY5lknFa9RtQNaueB3D2CBY8vDBvGxwce24-JaAvFVeQXlFExq3ZFTBFzjl2eJ7dIrAcss06TWrFAJEhDr6vDOe2qiOJG5g3KCaARSH8JAbcaZsZcdyLA_S6g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
تو‌ جلدی که مجله اکونومیست از سال 2026 منتشر کرده بود؛
زلنسکی
🇺🇦
درحالی که دوربین دستشه، داره به یه کشتی ایرانی نگاه میکنه!
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69107" target="_blank">📅 12:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69106">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=ZCTMK637NsTPofke87rgzc_hpB4Df5MiInQMh3elGXD7XvjZJypvS9uqfxb2pLMruxY1oc_M5ejoihJxOJeZdOvYhcGSF94UakqpixmvviPfn0k0S6KFIP0kL0SyYs-p37Q15bh7issl9bIr-C1fnqU8GLg4QUxV-SZ4_-KECC3vrTID0n_TSEVS9Kgc-92_ylbPzvnIUIaDiBvkMeo90g20i7TPn74-RHV3CJmd-vhHrrowoz-ijb_Qw6VGKNWeends7Jo0kkw2f_Hcrh6JHmPNDphSIFp4532u4pq3OeIjblZ560GEAWcTr5kVqpgcDe04BKGvVskBDoN4Zptbmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=ZCTMK637NsTPofke87rgzc_hpB4Df5MiInQMh3elGXD7XvjZJypvS9uqfxb2pLMruxY1oc_M5ejoihJxOJeZdOvYhcGSF94UakqpixmvviPfn0k0S6KFIP0kL0SyYs-p37Q15bh7issl9bIr-C1fnqU8GLg4QUxV-SZ4_-KECC3vrTID0n_TSEVS9Kgc-92_ylbPzvnIUIaDiBvkMeo90g20i7TPn74-RHV3CJmd-vhHrrowoz-ijb_Qw6VGKNWeends7Jo0kkw2f_Hcrh6JHmPNDphSIFp4532u4pq3OeIjblZ560GEAWcTr5kVqpgcDe04BKGvVskBDoN4Zptbmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=RlY-hOnP8W8v91phVwjyN2suPgHKneNtIUd9cd_Eq4BqqPtJVlJRHoTM32QUhtxoLmlWHhoOCtYU3hgLOV3Bavc-QOlqQY1FALPZUNCvdioNFvcwSNFbITKaIlHxfDrq0agQP-zecB9DGvwpw-Uc0Fx_rTj5-Wrc9Z1VVhrL_kDaFrjHPelQVY6RTMXJ9m8XM3UHlpCqtT5QC6sc8lIXKhtHd1uvYzEHOOFQrcYK_QDeMuVDtuVjvqOk_yf-IErYgjHzV2Y6Zkuub1zLb12eaJB2LNpQWLexIQeywwPg3R1BvlxkiEgRsWZEKQ5iyqZs4KiCsfL_y9JORWNNMUH3iy6W_UoVUkGjwtIyrkcx1SEyLd6o3GV7TWVpc4zwcztrSNNroJI5lrbcmvT2YS4J8f8NSVrFNTFcgiRM3KFZPn1nRVlfqZYmgzrPLtzY78nbjPz9-aQirzJrsxvuxZ-M-oEiSXGzGtaFEPGyhaG73V2NemgerQX6Nnrv8k_3XR_V6BaG4KaBDraYoeYDi6Ibeq2x1zMXuXB2hIaSSjssWSJT0DoPT9oj1wr9FCXRHpPIVFA6383x7_3eo6OuOwYejcaJAukWKsjLs1gtmbawcetsxp9N0iWN-l1K0Z0IvfdOuXG8ANb-5GqN6lHpK4l5-Q9NHTMeeWmMfDDOMULjXbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=RlY-hOnP8W8v91phVwjyN2suPgHKneNtIUd9cd_Eq4BqqPtJVlJRHoTM32QUhtxoLmlWHhoOCtYU3hgLOV3Bavc-QOlqQY1FALPZUNCvdioNFvcwSNFbITKaIlHxfDrq0agQP-zecB9DGvwpw-Uc0Fx_rTj5-Wrc9Z1VVhrL_kDaFrjHPelQVY6RTMXJ9m8XM3UHlpCqtT5QC6sc8lIXKhtHd1uvYzEHOOFQrcYK_QDeMuVDtuVjvqOk_yf-IErYgjHzV2Y6Zkuub1zLb12eaJB2LNpQWLexIQeywwPg3R1BvlxkiEgRsWZEKQ5iyqZs4KiCsfL_y9JORWNNMUH3iy6W_UoVUkGjwtIyrkcx1SEyLd6o3GV7TWVpc4zwcztrSNNroJI5lrbcmvT2YS4J8f8NSVrFNTFcgiRM3KFZPn1nRVlfqZYmgzrPLtzY78nbjPz9-aQirzJrsxvuxZ-M-oEiSXGzGtaFEPGyhaG73V2NemgerQX6Nnrv8k_3XR_V6BaG4KaBDraYoeYDi6Ibeq2x1zMXuXB2hIaSSjssWSJT0DoPT9oj1wr9FCXRHpPIVFA6383x7_3eo6OuOwYejcaJAukWKsjLs1gtmbawcetsxp9N0iWN-l1K0Z0IvfdOuXG8ANb-5GqN6lHpK4l5-Q9NHTMeeWmMfDDOMULjXbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=AFRWqZgYMlf92Ml8oi7WtAA8R3eofXuwMAYsHMWkC1xaLvMo6Mq-3mb0dYCKHmsJvbkFbLn6fiz72WoZvim6nzEgMPVhWj3S3fOudmgriCzJH6iFDOO0PhCTUS2gpW86T5TGUQJ28_iSYIDydn1_pRDV2ge8SgyXuATaeA-KWFbUhdZ7Dh3LEqs3-M7G_qnyHdIcoxyfNy47D7f4D-aa7_Pr4NCWdzPA3i1EGe2V0aACQG3xvMIDOmmPOGVOY3HjYupyuqcfYJ6fzku_u1h7WPSQKlQL4p-xLk4fCU09nrynjQGAFKCIEx7zQ2w151_HH650C2F06II0HZFjA3jekQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=AFRWqZgYMlf92Ml8oi7WtAA8R3eofXuwMAYsHMWkC1xaLvMo6Mq-3mb0dYCKHmsJvbkFbLn6fiz72WoZvim6nzEgMPVhWj3S3fOudmgriCzJH6iFDOO0PhCTUS2gpW86T5TGUQJ28_iSYIDydn1_pRDV2ge8SgyXuATaeA-KWFbUhdZ7Dh3LEqs3-M7G_qnyHdIcoxyfNy47D7f4D-aa7_Pr4NCWdzPA3i1EGe2V0aACQG3xvMIDOmmPOGVOY3HjYupyuqcfYJ6fzku_u1h7WPSQKlQL4p-xLk4fCU09nrynjQGAFKCIEx7zQ2w151_HH650C2F06II0HZFjA3jekQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzSRX8ORCTuwaKU5sKkSx7sNihsiLrxHoECn0UfEb_gLISM_6Vxwne2tAfiLtzjABL69HesxCXT7D_q8Y6WZmJBtYf7psEXeUvqJyS85GMiSl4VUHa3yid9D0VQxD4u1YZrfLTAA6Gstje9VMjiDDShVrNMLY-_wWYCyK0IVVUoHQMZf3GajX4hhctuAxgMT6we1j-XPFgcxrxatehvPATMVagHMUssQ9ERWNtTc0VzEr5nvjTynC4dS30pH6_Nn8bx2i07CBUphC01r-2SJU9bTTKGsHBP74p0nhdAabT9tqG_Rhec3ZdEqW6Y3noFB1xs7hbb8dtvupLxV8QmEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=rtN3VWli_gBXjKw6CMMrY7gUspvkFNts61EE3szVPznYk-Rdo5j9WZUznGlZh3IJerYMIMqdS6Rui2QZvig5XOBgGAdMzljW3y8vra6PF82L3VW7ZKt5ylSDP_QB_QpjtXX35cfKlhSOtfXwunbNydKo2Ngs2cw8ePR9ijtzvX7aQRwdM_Gbg6fDzGFvWFme0v0HvhocoAMxIqGWejwDcdslX73XVRLjk1JfsvUSznrk4WmFDiLocgut8qYyFN_70yzNLVvQluwWzwvY-x8svll7eDpUu-1KPJ7OtuxQgwQ9qqBLRw7YltRP46MGsF9cJArjO0zGyj73M3oc8BJXoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=rtN3VWli_gBXjKw6CMMrY7gUspvkFNts61EE3szVPznYk-Rdo5j9WZUznGlZh3IJerYMIMqdS6Rui2QZvig5XOBgGAdMzljW3y8vra6PF82L3VW7ZKt5ylSDP_QB_QpjtXX35cfKlhSOtfXwunbNydKo2Ngs2cw8ePR9ijtzvX7aQRwdM_Gbg6fDzGFvWFme0v0HvhocoAMxIqGWejwDcdslX73XVRLjk1JfsvUSznrk4WmFDiLocgut8qYyFN_70yzNLVvQluwWzwvY-x8svll7eDpUu-1KPJ7OtuxQgwQ9qqBLRw7YltRP46MGsF9cJArjO0zGyj73M3oc8BJXoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHOO1kz0frJs87jN3QH6mFH6mRfT43GZrNkHt6Eh2nNf8btJePXNVlKtuTdajJKWmghbM_33EYEryP2VFU5MsAtaQ5yJe7w_ftuLPyshsaPSB7rf-ci_ZJeglKLLhd9lZ0FX0BCMWXAttMDHL5tXITBzVUbHo5zfQhjZxoy4el-MhzwhSZKFxxA1HsKl2wTDOlNnyGluP2fOyt1WvFf9tNaOMTI7HyUIQ6kU_xfWEJbYDoiaZD6BOrjQui66o4-vH-nwKJ8t4XG9ZH55tH_zDl6rmQeJ1kjkpn06R5VgnOLx0uuEniaDKU9dA1QAifJplqb9TuTiQVgVci2_Hw2-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hXxbthefbsQB5__7wqZ-5DCQvfYwG3mtQh23z102QZKalHpxIXN5yDdq9QuCfU4nXzscaE2MJgtgYgSH-hK9LBHteP777dgud5FPrEIyl922R2fjO-I5kR8iTqqVzEmQvoSbB-zZoBdnwx0bElslh9XB92BsQIBmoERPEtXSoY5WDvChucbUeqnX7cCrnQpZlGiF0CIj6JlIoLkjyfRQOxyII5_p54QY9QF3W3TivqZPkBTBMxkk3P3vTR7HVFmEB5AJNcyHavMAc2F6e3g27QHqom2twZHE815xJuShtiq94XL_XtOiS8z6b5jlKiMiZT2GMm-NfwzcvdmAVcJjqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=AGnMWpAS7JJKBok4ASAuZULBqaIZg2mUk-9GlNKRP1GLyhsexrmIu7X6haZqUWMHXLeo0EuB9zTiew9FE_Aq1gCVmXtCvUxcOD0o1mM71OicLUenh2dLBCjXxaIDZiHehDExEhl-vZoZzdIPuW8Idck7fakOfVsdMy6H1NwZSXcHUvhq__F6KpA5okNH3zShAVXWTeJknA5SHARWEkMUgRQq7TOQq_Jby8LCbdMD3zwRBQKHzOGoCNt7WGE9pZ1tkHrqdI260kXAseYq0EPGMl-F6TyTZc29Thypx4kdsnMduNhJggBF0whYTb5IPMHOupnYEOMwLIWBqzq1Db7XpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=AGnMWpAS7JJKBok4ASAuZULBqaIZg2mUk-9GlNKRP1GLyhsexrmIu7X6haZqUWMHXLeo0EuB9zTiew9FE_Aq1gCVmXtCvUxcOD0o1mM71OicLUenh2dLBCjXxaIDZiHehDExEhl-vZoZzdIPuW8Idck7fakOfVsdMy6H1NwZSXcHUvhq__F6KpA5okNH3zShAVXWTeJknA5SHARWEkMUgRQq7TOQq_Jby8LCbdMD3zwRBQKHzOGoCNt7WGE9pZ1tkHrqdI260kXAseYq0EPGMl-F6TyTZc29Thypx4kdsnMduNhJggBF0whYTb5IPMHOupnYEOMwLIWBqzq1Db7XpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=aCoCZg_xfA-FXZ7MbvvwaGRJQEwtX-zKYTEqqOndedo7huiXOV3uBUVE7d6Urbo1TzNRwN_mMQHOB-jTadfztB6ryHDAiGxGgqTwVhsbcpkdZY_A35FEyS3CL619KrYwVe3JbmXsTA0s7FmJGdmhNVix_L26jQmMbfpRvBfWxoKulBzQGJ47OiT-OwPpxtN8eu7czQQyl3bz9zxJeXY8T2FivHCNrsMM-KE7fYpULmgfRKKu1yhupr57oXJKxY3PPdJCF8ICDm2Tha4wneu1IhWkK2bM3lB_9YgTuu-DLY5IFoqB1z1KfuAsmLjnmZQVZzywyTOTGsscIXgHV1ssxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=aCoCZg_xfA-FXZ7MbvvwaGRJQEwtX-zKYTEqqOndedo7huiXOV3uBUVE7d6Urbo1TzNRwN_mMQHOB-jTadfztB6ryHDAiGxGgqTwVhsbcpkdZY_A35FEyS3CL619KrYwVe3JbmXsTA0s7FmJGdmhNVix_L26jQmMbfpRvBfWxoKulBzQGJ47OiT-OwPpxtN8eu7czQQyl3bz9zxJeXY8T2FivHCNrsMM-KE7fYpULmgfRKKu1yhupr57oXJKxY3PPdJCF8ICDm2Tha4wneu1IhWkK2bM3lB_9YgTuu-DLY5IFoqB1z1KfuAsmLjnmZQVZzywyTOTGsscIXgHV1ssxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eJ_FL8at7e8rxNiqvmi2ITimSm_WZdB4HMIxZGcPUjTXKXl4-Cou4rSL_-CLCjwRE3ypUziOAVclmEMml2MQCXAzvfeICgAOmSGRLqMsAqAMInS4pHhhvZquiJqAw7nJ2UX1-WI-qqyYF0FEflgkyeEpK6aR3p4pLMn5awF8ekJB6cKDGNO5UBvO5z7-ycFX9akUa9zNRwGOuX29PWdGJz2hVxvo3Py5dwer0kJj6RdzmAJC7Uwgb1faCT0cR9_dIEFlYXv8r2WAuLd6_ByUlterUFd5K_8m1FQUrYWP76a268CPRyrH1fOYlKLxnTjrm3Rqf69bE49uRiYY5DReIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZT3PD1eYx1EdxQL1NvY7TVqY-JKu5j5rlPSM9LwfjdNqBw7XAgyPUXwemQeKzZMNBVeTWcVM1ZBrWf5l8ZIwAHT9RI521vQoyrFSaj1AMiyxRIo_pMKJYt5b2zOukE93tyhy2Nu0O_MPG_kodDBuR0BRNxQGe6LXiHIzYJT1rYhBm0MyVkZZFNK9qq6aUNTpnbB6uYNTYJwB2fSnI48zgjPQ7SijobEeAb99x5P49v7Da_GFUHDcrUsJ4WA6GnSuiV6fo_kLiThIQhGk1LJsdujrZqAB9hjYdirY6QuUk73kzZH5cq-m_34s3CWFIWnfKV_6D4Qn4NvebU3mL6mY1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_G_70TLBQ1K-kYkY3Hb787SW8JOHdjw7m2OEDueDSn4_ZgkanJKJR_1i9wX-u9PAptnlUHgSg3bE-iOqUrVzq5tnirAzA0AnMGrTB4Z__bbik-e6aEi48VLqZqk4LlTGE9sQc0euYEsOqXwkvmWZNNxCtOaEyDFTXyC9X61Z2t4cGFplo7zUSPJ-NvMs5iEiJZZGWXqDGkABfC-eUMm-xFl0qyC46sjzY_EmJYqeGMkLI4zRbVL5CpXa7vOtyXESZEB2JqIvGm4RHId0t_s1X875MnkRyILb8vcvWgm1h7iRx6Uth14bnd3D3xFcRU6ED7F12q6IBIXiYa6mX2uDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=V2Apx-ED9DmiyjFmYi5zHHtocO5DenA36Tb89Qtj4E8HGtiJMg_NA-racTVTnAbG-P9OyyP2jmWC75geGH-plSG_7YxgMaYGw7mFAq9-sjxsKDmWoYMjHR7hgfWcU1o7KX8cMFgLsJXtxbvqOTgmXXUXWoQC6Hq-mGQojoW0Stz8hpQB-dOaLDbb-J8Lx6upItTMVepNYX0F5xAT26C6M-JtG1_OhDIONmGpD2n40oaurdKUAWAE7HI2an5pius8fK-JyiP2KtncJyfLJqY5-Y_kYjm_8W2Svd7TKA4FTl_CEULr_p0dbWOVfpFiQJqN1mf9qEeHYmBYqBlGK2VmXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=V2Apx-ED9DmiyjFmYi5zHHtocO5DenA36Tb89Qtj4E8HGtiJMg_NA-racTVTnAbG-P9OyyP2jmWC75geGH-plSG_7YxgMaYGw7mFAq9-sjxsKDmWoYMjHR7hgfWcU1o7KX8cMFgLsJXtxbvqOTgmXXUXWoQC6Hq-mGQojoW0Stz8hpQB-dOaLDbb-J8Lx6upItTMVepNYX0F5xAT26C6M-JtG1_OhDIONmGpD2n40oaurdKUAWAE7HI2an5pius8fK-JyiP2KtncJyfLJqY5-Y_kYjm_8W2Svd7TKA4FTl_CEULr_p0dbWOVfpFiQJqN1mf9qEeHYmBYqBlGK2VmXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=Dp02VmCNJhi0ya1uM_QrJkV4OTxTIKn54CsTpKLkhSLeWFCucUku0hlcYQEtAWgcLWLxGHe9inlAz6JPaD0yk-crpnq449UtqD6UsCq62-b93BeA52o794XEsghjY_rwaEUbPoQiXUjqFSHR7cG-MkqSn-0jXYE4fJsQzDLriQ0lUG_4nFUjyLOGHgQEqRcDI9uoS7X245WgN6FR4Udz63lauQ_QlW2hhPfOar4pZQOzPKx1cfbJFDTSySp0krWKnuUz-IV_88GF2HZI8EefnVnZk9dPzzqBIKuuAtlZeDCb6rv5TmgQUeD1NOulPCw_JFDGucirAfFGFjgNhIu4Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=Dp02VmCNJhi0ya1uM_QrJkV4OTxTIKn54CsTpKLkhSLeWFCucUku0hlcYQEtAWgcLWLxGHe9inlAz6JPaD0yk-crpnq449UtqD6UsCq62-b93BeA52o794XEsghjY_rwaEUbPoQiXUjqFSHR7cG-MkqSn-0jXYE4fJsQzDLriQ0lUG_4nFUjyLOGHgQEqRcDI9uoS7X245WgN6FR4Udz63lauQ_QlW2hhPfOar4pZQOzPKx1cfbJFDTSySp0krWKnuUz-IV_88GF2HZI8EefnVnZk9dPzzqBIKuuAtlZeDCb6rv5TmgQUeD1NOulPCw_JFDGucirAfFGFjgNhIu4Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MvTrgUJHPslbHJCXfOObxIlSGJYtPIPLtiaiOv-MZSP34VZHdGCKmxENB62bcyOyu-S_XgSk31hW9WYxMT8DGeaCnQ0Gt4oGkCFqg3EsP2kGIWsBLJjX6UPecBgMFscklQGjKNiwBsy8_whCGGrmz320sOQ1Q85UTG3dFpUQhSTM1Ld9wzO-7OuNYhzyquCOV9XLlRFSsziEtVHsldANriZpZv97yL4st_cNiWO6F1o969rYvWvVgzZZ5mPUKNi6e2bNKaNvAj0xtzbbd9G5J_zzeh4r_dxcERICK5vtOuTUmq5A6m-ZLGDzHYikFidOtZtJgxt1B-cai-b_gpFMsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=MvTrgUJHPslbHJCXfOObxIlSGJYtPIPLtiaiOv-MZSP34VZHdGCKmxENB62bcyOyu-S_XgSk31hW9WYxMT8DGeaCnQ0Gt4oGkCFqg3EsP2kGIWsBLJjX6UPecBgMFscklQGjKNiwBsy8_whCGGrmz320sOQ1Q85UTG3dFpUQhSTM1Ld9wzO-7OuNYhzyquCOV9XLlRFSsziEtVHsldANriZpZv97yL4st_cNiWO6F1o969rYvWvVgzZZ5mPUKNi6e2bNKaNvAj0xtzbbd9G5J_zzeh4r_dxcERICK5vtOuTUmq5A6m-ZLGDzHYikFidOtZtJgxt1B-cai-b_gpFMsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDLVlHWI5Ui3Q7KsW76Wr5LCYizf8dOL88L69b6Al_G43WUbq5oXFKPqtGOulUJzMCV0Ibk9QfXSYsr68aFnKDND8SmjL5j63zSxujhglI8wdM93qs73BOvXU0Y7T3zaiRiBw5AxzlQXRBg_L2vTspAz-_XsqEagO9G93363A0eLAXSGmadu3VXXJqfyBk2G8HFB7dAEnFGa53sLA9SNUuhznP89okstUI0A84MF70sOF9f3196ZOuhFbWCNRSxTz4fsh1foMCToyLvWpoz1r543qXBCZLE9HAUAJIBTUAN0zPF67NhLKz1cD0f3Nlmb5Ydx9GrDkNZwtHpqj00zrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnDoC13bqNNf9JlwE4_Ab0ilK0TvtJbVVZMn6smufxvzDUQBQ5Wa57RYlvrsyIUbyXvb88FMEvFJ8btCfNoYpC-bR8TMy_MW0G-Y_i_6CXfE8EIAlpsqnw2cfDCliIqisc4S5O_YxjJqhqGCH8fmVNrDZ3oYvzpKcKIi9UlWPcwy1JQeq1edKDi09HHBRPeuWXFehrpI3SBt_IorztReqeJ3zQWvkHFs4e3yb1BBjJFxTgdoYLzULY0aRkhP9yWx0-ZpeA5qZfOvBw9Kzla8aP_-F3drSAteqjwoPMj-Lf4o737MAJerWDYIDjX5LaBHatN5OdRdM_5kbNN01M2McA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LI854PnIxDHgKH1fecwHw-fcJ5BlIqC4abGuFDK5E7Pq8hnnfNl6N5w2r6seFeBBzgbjHUzxj5hgcMuShtM4ggQh3nA3f0SiF5DA8TpbtzRdvUZyrht9CjLtJGDlWjPSKQjKbhXN7kofvUPBDoqQF4criHu70akjIpelC9gdIdZyEonr-t3k6-3t8uohURH1rPWHR2i_EPljlbiJUNefFJd7TVLxIVhhl6Vf-atQyvKwUqDE3eUd36yUbqzrgTmJdqbqCVCr6fj4f1hjKeTWGoxhaDr2mXN8BYx7cwv7c6l_iJUNt_DHCUd_XcI6jtePA395027814IXgTPALqSmHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=o_CVu5tpqvWyjOY3w_1r5dlmrLMqeGxZ2NP2pzpsrYvsq7Un8cKws7n6FUlsXk1_wBtwJcxgppRuzRk8GN1hWC7rWN6Dq96cAn0d--x8zUA-nSrL2w8OPIp5r4oW-iGnvtKDLYp0RHBdbza0PcFtSdK5uB7BmHFjU1AiQYzmKlSU-55p1vGuzR-U8ucddTlobZzZvPEBiFaO6ia9QH-m7jlJ1ScAsLx4-QWqM3ZmqtLIQ95s968oAByyKj5BcxkLE_VRlcfT4viYo9r4feuvGo7Rr0qirGAoyg3xECoVObmTpMW793jGNov4AMaqRA_qmCuUxoIKk0HeYq8Jhl2Qug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=o_CVu5tpqvWyjOY3w_1r5dlmrLMqeGxZ2NP2pzpsrYvsq7Un8cKws7n6FUlsXk1_wBtwJcxgppRuzRk8GN1hWC7rWN6Dq96cAn0d--x8zUA-nSrL2w8OPIp5r4oW-iGnvtKDLYp0RHBdbza0PcFtSdK5uB7BmHFjU1AiQYzmKlSU-55p1vGuzR-U8ucddTlobZzZvPEBiFaO6ia9QH-m7jlJ1ScAsLx4-QWqM3ZmqtLIQ95s968oAByyKj5BcxkLE_VRlcfT4viYo9r4feuvGo7Rr0qirGAoyg3xECoVObmTpMW793jGNov4AMaqRA_qmCuUxoIKk0HeYq8Jhl2Qug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWl7xjciS0H_RHBUUKzG-AEHRSyWxKF-3jg273i5QWW-ALWwN7LnuTD9_uKcb9Wf4nQ2VgXfsfXQUkm7l8_SrO48dp5VEFQMgQh-0zobOX23nZE97wbLedsAlSeHoXMkwNkoqXMhD5FuthWYHLudNwHY_VZlOGdrzVBIkoYzv9UJJBWH-MW18yw_7an1bA0LaTxReY-Nr6yEY5emBs14QaKL97BM-IBInrh8Mu_Of04JACEGLVXI7-KtDmQEvAtHJ8lrDsxEFdXeXggfJ-J_U3CiEjilBdPpgF59MPZkyEK1mrPzTAvZ-ex_l-7bSrifCYyuJKhnKSNOMeXKSdIe_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=lsDOYEM1VRxyeRAtnxBaZLMk7JWsoWCatGHp87NX8AHbxiAuwcMxwyQ_okQ3x9TpjzCo5DW5MsZ1eJ-NAzlm-L7n3Azbc5v2c9dzNyFk6R2RYRi_0JoyHQCg34-8vgw6_Nhu918uNsuYubO3OeldgMEhBKiWu_bt1lD2YCZxrtgJDtVuOTL2xUJhyllGLcU8zOHh1yt6giZ2NClZ2yamSetzLKqJqDDBF95MDuKRBue9PQUd9ioTkZl643m8caWIQLRuczM_OuvQcHwVSZVX-UpEKnMeN0QP00TJqf8nEQKU-SeHw_-2cBVvG3cHFVkYOdNhJ9o_yGtn5w4AZXhXPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=lsDOYEM1VRxyeRAtnxBaZLMk7JWsoWCatGHp87NX8AHbxiAuwcMxwyQ_okQ3x9TpjzCo5DW5MsZ1eJ-NAzlm-L7n3Azbc5v2c9dzNyFk6R2RYRi_0JoyHQCg34-8vgw6_Nhu918uNsuYubO3OeldgMEhBKiWu_bt1lD2YCZxrtgJDtVuOTL2xUJhyllGLcU8zOHh1yt6giZ2NClZ2yamSetzLKqJqDDBF95MDuKRBue9PQUd9ioTkZl643m8caWIQLRuczM_OuvQcHwVSZVX-UpEKnMeN0QP00TJqf8nEQKU-SeHw_-2cBVvG3cHFVkYOdNhJ9o_yGtn5w4AZXhXPDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
