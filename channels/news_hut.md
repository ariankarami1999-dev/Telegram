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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 14:29:53</div>
<hr>

<div class="tg-post" id="msg-69188">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/69188" target="_blank">📅 14:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69187">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/news_hut/69187" target="_blank">📅 13:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69186">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/news_hut/69186" target="_blank">📅 13:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69185">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuQfLyQa76fPWCwu5JFDBEu5ufsePzg4B0sWoEDceRPmUwECyevkcubRKElyU6SGU5BAHaDr5hmrB903DBXj59UMQ0C-1Efdra_bQrL6mY-MxxkGmIP7PTkLOfMWtDNdhbpcypfnnXvVndXtww5NtSHtc4Hwjjh5exkFNnATEB_N_NDZ5LEQvBKeS4idLsxZ67YE43o80pqGHzVU9YMLfWcAZPA-QjIWGJZv7qee55fu1OwkFgNK0ofZy6bt8DkdQsxlrgZRrQOMtMZdYR9PwVCSyPfSkrRx3xA4Y0253zKmp2mJ_sX7ZfFds1dmXiw8XlPldr6PO5lG121PJ40ySA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ایران پیشنهاد عمان برای مدیریت مشترک تنگۀ هرمز را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/69185" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69184">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/69184" target="_blank">📅 11:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69183">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/69183" target="_blank">📅 11:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69182">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/69182" target="_blank">📅 10:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69181">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTGZyj8yLFc8tJ52ej5C2aIR8eLS-flrwkPArKO1nSj_64cv4J3N3ErQe_vXPXoCi4qRYRny3BtG1rKgaYy-76M_8tw1f5ltJctqAD93n6f25xJ4uMc2jaaN6kZN_U4qPRlUUVitfqqnKQ6uCAvOzmX1AHEQ10HT5PMCm1SYJ3G-eagNmpy40PUF8HCIzTslbcimV-RyVrpQj8WRdrVMme4ZelcwGu-rGXI1E9DPp-CxpyvSWwQk5tSibS53hWDN2iJjymLwfedb2dAVcKgxpJy3ypwHJY3DKva93lCd6rtxRHPLdKrpoyu80f89m3rLN4oj-ZpUdhWPUM1Uv33MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه:
سه کشتی متخلف میخواستن از تنگه عبور کنن که مورد هدف قرار گرفتن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/69181" target="_blank">📅 10:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69179">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69179" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69178">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69178" target="_blank">📅 09:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69177">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69177" target="_blank">📅 09:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69176">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اگه فوتبال رو فقط نگاه نمی‌کنی و تحلیلش می‌کنی، این کانال برای توئه!
⚽
🔥
تو این کانال هر روز داریم: تحلیل تخصصی بازی‌ها بررسی فرم تیم‌ها آمار مهم قبل بازی پیش‌بینی مسابقات مهم نکات کاربردی برای فوتبال‌دوست‌های حرفه‌ای اگه دنبال تحلیل واقعی و بدون حاشیه‌ای،…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69176" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69175">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69175" target="_blank">📅 02:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69172">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWnjfiksSHODzqsjSoMpCGguSDcm6QH6LoZuHS4DlYqIeB4G2s_yXlAfGZpFXGvmJFTcBmMBr-QvLaFtN9f4SuZVr2EF6iO9rAndrK_2bu_vjF_qFVJlVv13KxWEIe3j_eWKvQLrKXxbIoFcM7H5NHGCt3tmwu_8Usd3vLRTlturEqIRqLBwpdM6lAQOic0X_NLucPYeTnEglw7uTBvgIOTcCTM6AJ0RVxFAmEIGKo2b4mJxCu3Zc9Scu17JRmH_e90fs54nac9HMNn1Jipiu1qHMekKu22qrJ3vGaTHUCITWT_TbYplR-S5ZGyEaArE6AnJR5NFniRvUdjEfOKHqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فرماندهی مرکزی ایالات متحده:
امروز ساعت ۵:۴۵ بعدازظهر به وقت شرقی، نیروهای سپاه پاسداران انقلاب اسلامی در تلاشی برای انجام یک حمله غافلگیرانه علیه نیروهای آمریکایی مستقر در خاورمیانه، چندین موشک بالستیک از خاک ایران شلیک کردند. تمامی موشک‌های ایران با موفقیت رهگیری شدند. نیروهای آمریکایی همچنان هوشیار و در وضعیت آمادگی بالایی قرار دارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/69172" target="_blank">📅 02:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69171">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UVws3qCMpZh3ZofX1NPDxICk8qY24h-ezbXDH902NCBC9HL1fWDc0DNHrgT7gyvF2JP_eYtFjH7_mpU11YnIpCFC-TdPAvyEPqE5Xe3dtruNkvwAJHJTnaTmnGFEXyOV_XPpuE0EuQsCq_eDbcxQ8eZvdMcfpT9D_eIePZ54mmtzEIEZ2pXbNfLf-ZTI6KtOSXZQFXGdv0gQb2-p-MrqT6hYYW1-0ne5eb5US4rNOwNPRyHrVsWxj9LwWlB-rHGbeVc66dYY14wbG11svc6wCuntukoL7eMvcd-haocadL1AhZbrGSqKnPLBy-CDD7uvthPmX2ru63xlj2oPboD7pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران برای جنگ تمام‌عیار کاملاً آماده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69171" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69170">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69170" target="_blank">📅 01:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69169">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IVPNx4Zlp3YrRdTdV4xsRDe0Q-Qy5BtS6q6MeCeqGQocKvL2iDAtp-j0Dwb6l-T43h-0dzXBxuNAQQzT-YfDVeh64hyKzXygctRuJT4hmSMjEZ52AmAqjaCiTOoOG5QOtbXfRGPUkIWWNDNwQxNGGlrBBgl6sa26EbwaikLNVH8UpaXwxmBD5aPxS8bcRyQcVNGzak7Le-oLsuy5VHvobkPNnfVBKObeuXTbQkZXJWskfegwXKl3V2x872GlSeV5Ky4jgOn1-_dqIdC4fuqd2Vx9zCWDPsZYYMYHuh8367iPDuF1tJJ2a2RaoJmafJCENsglL1J32pk-OC8unAuMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
ایران چند موشک به سمت پایگاه آمریکا در اردن شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69169" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69168">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
لحظه پرتاب چند موشک از خمین</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69168" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69167">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl9Lw5bw4Ch0NaP6EC4PbNHSO9wHIvSvQsl0BF22syZ7qFAO8TI4ugUonPz4CCjuder3T4MdQAiDrfsUr3Zz4CzKdEr36wW3iQxLdV86rBLqffBJwT-2n-s5b704NWzLB4OLS_h5wcX8LfJzHb5XNLadO38TuPo82wFRt38PAZtdz8NGybxRROs-gM8L9_BiloxdBiXQwqJOphrQ-19lbp4F16yJpIL3pqckd7bEcXYmo5jmYc6qs_khvhfdzmbVhbecEkJFursVcd81yTa_3GJEK32oEprQ7Ge9-17MdBPqn8OYPqVhnS5lJKJNydDs_lgYMEIL4PwP5RHdT3G66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پهلوی در کنار یکی از طرفدارانش تو مراسم لیندزی گراهام
#hjAly
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/69167" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69163">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69163" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69162">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n1mGrc94TpfwrKUSiuWMWZyOw6Slv5-Ci7H9RhDJf8weyMkUfX15of2R_-Mr_sw5mgcpIVM6asPRMXS-iTi5z8uUaGH3aw-5e4JXwDILj8TSsh8oYO3yqT5IEgNdYZe9kLYVlEJuWxtbLQS3xSQhizYdOkIJKl2Xa0zWZqEbRsu12SDtAmzOHcSpzh0l05cIeeM-BgipPQoplscCiHG5jowOlvWnLA63DangaufBIIRoCencQuBL2rGFc8PGQYX_WwMxtKpjZz7OWOcOcmggQkZC4b3nZk4ryOshroOoX0W2V_V3jQk1kEon01PhmCa5AwOGkTbSKqB0cNRpUCKPJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سریع‌ترین مرگ رهبر و حاکمان دنیا در تاریخ پس از شروع جنگ:
1_ علی خامنه‌ای:
1 ثانیه پس از آغاز جنگ.
2_ هاردرادا پادشاه نروژ: 5 روز بعد از آغاز جنگ.
3_ جیمز چهارم پادشاه اسکاتلند: 19 روز پس از آغاز جنگ.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69162" target="_blank">📅 01:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69161">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03145bc392.mp4?token=XW-wHuNCAR0nqcnajLbmPga2VS6MVCw1nxev88axPt6xxalGBItTUMtniaa2xkYvGoOQPkWy5rjtm3g_Cu9udvrFTj9kQXvNLkCJa7G4Gqmgx-UUE-k4yaHhqn5qDAKnTbr7rDImlbQfsglnO2cQ2vNc0PM0SPxoEP2o4nGNkOyIupwvwtuNzUI53QwRR4MMCUPykYhNGwSMGLELy8OIwyRokUQ5fKlTxdfbuTXkTp1gl6zniCjUluQF_G3pMXfV7oeFko0cRpQpAaFqhrXG-sR4Y2ax_ABuRkPgwFqSxzCmotZhQSwuhVSqms_6CAQVn0xHPhax9mOgCb8ysxcfNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03145bc392.mp4?token=XW-wHuNCAR0nqcnajLbmPga2VS6MVCw1nxev88axPt6xxalGBItTUMtniaa2xkYvGoOQPkWy5rjtm3g_Cu9udvrFTj9kQXvNLkCJa7G4Gqmgx-UUE-k4yaHhqn5qDAKnTbr7rDImlbQfsglnO2cQ2vNc0PM0SPxoEP2o4nGNkOyIupwvwtuNzUI53QwRR4MMCUPykYhNGwSMGLELy8OIwyRokUQ5fKlTxdfbuTXkTp1gl6zniCjUluQF_G3pMXfV7oeFko0cRpQpAaFqhrXG-sR4Y2ax_ABuRkPgwFqSxzCmotZhQSwuhVSqms_6CAQVn0xHPhax9mOgCb8ysxcfNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69161" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69160">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
منابع عربی میگن سپاه به اردن حمله کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69160" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69159">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scIochdYx6FcxmheIfGc2I03WUp7KUE45fjgDcT2bVXFFyMogihoaZE2i827GNXQ94O3Bb387FQqBw4x7Op9zXJBVymQU5vT2WLY5LbPoed57PXXfOctg4CudsYWtnWuCD9ZdKho9G2tsadbGF9CThcXrgsrIgK9Eu_kzu7Ms4Yms2u6QzgpkBYANvnmdbDA2sAqgQ5VbGLdjGNfWyxjnCZfS5WM0EW5GmXNs40buXvwgQVH1DC8mEVFHBwRnt7kX9Pfdtmnu4vjz7uOvdwmlJSl88teofKCgACUGNT-gCFWAFtEKdoXrGAlcbEcvucDxZp681xzhbPgXx73IlHYzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
سه موشک از خمین شلیک شده
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/69159" target="_blank">📅 01:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69158">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGTj8-faQ6kFNU7ZAHgX2V8oLxgQNqQYqjDBMsxlhGUn1l1PJQV7DXQ7EdhaVR57ZYwOD4QDeiYYtj5wWnKI7KZHotLClvAIIor76eghbryKo_YlEUDe7ttaFErr_y9hfOqJZjmj5mnF28YN4Hr3i42Tm1-NYwyZoHAWtqliEYml-f-wEnOyHEGddQ6RvQ_MiL-lBdFYH6dCNLB12hcNvOPeqgltHcFPh36TLJGLt3B4pY0Bfzlgec6kRGp6h2yZFTPW-BylBSUfMOecR7tYkHUu4iQoFrYX328cfq73l-KZc4-uVnCORuHNYcis5CVCqwBjlYJ4lkzAJHlUH72_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
منتسب به خمین
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69158" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69157">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش های تایید نشده از پرتاب موشک از خمین استان مرکزی
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69157" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69156">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/650687a011.mp4?token=GeJfpo0BRg950gCGmNc9Bxqtsaxlzzu5NOJLXhyfAoAUtcvH4OQ6zc64DPnCzFwcc5Ap0QxQjgGLW-uKrsRNAmtmxlQsxzxWvRsW-OvNlBnB75ksx0PVSdgWvmdsCssthT5puU_67Ysh5oCZuE9C-aP3mVT4hOaONNm3cD6V7FVlOMMdY3TEwwG-1VcRB6-rqhM9z-8OxzgjOjVcqgrQH8XpQnT2LuuWBt0kraIq7a2cglx7D6WmceKLz9zczrGpZ84A0FTF7NM4iPvD3oOF7Za1lTq5NRaMntoAbYKmDeV3MR4ib9eVE4DAcRHHmXi0e2dAjKhC11bMYAlo9ZIOxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/650687a011.mp4?token=GeJfpo0BRg950gCGmNc9Bxqtsaxlzzu5NOJLXhyfAoAUtcvH4OQ6zc64DPnCzFwcc5Ap0QxQjgGLW-uKrsRNAmtmxlQsxzxWvRsW-OvNlBnB75ksx0PVSdgWvmdsCssthT5puU_67Ysh5oCZuE9C-aP3mVT4hOaONNm3cD6V7FVlOMMdY3TEwwG-1VcRB6-rqhM9z-8OxzgjOjVcqgrQH8XpQnT2LuuWBt0kraIq7a2cglx7D6WmceKLz9zczrGpZ84A0FTF7NM4iPvD3oOF7Za1lTq5NRaMntoAbYKmDeV3MR4ib9eVE4DAcRHHmXi0e2dAjKhC11bMYAlo9ZIOxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
املاکیه دلقک در حال تلاش برای خوردن آب‌نبات در مراسم سناتور فقید لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69156" target="_blank">📅 00:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69155">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‼️
علیرضا سپاهی، یک تن از زندانیان سیاسی که قرار بود سحرگاه دیروز همزمان با پسرعموی خود، ابوالفضل سپاهی و همچنین امیرحسین صفری در میدان علیخانی اعدام شود، اکنون در بیمارستان الزهرا اصفهان تحت تدابیر امنیتی بستری است.
او در جریان فرایند انتقال به محل اعدام دچار سکته قلبی شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/69155" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69154">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vmE4CKLCW31yg2LjrFa0c0K7Hk-FL9tquXxrqsbMkFqP7LZUhOhmDtbJijJwLtUQONZd5hygh5iUfeU675LzjITsjXpP-94NP1G1uXMGYO0AfzHByW38Py4PkJ5mA-P6vP3boIuyq7O67rFIE3liQ6iErhzEEmWV4Ke2QLEa_sDCQu91JorwXHZVT1SolwxdySdeyp3XgJ87oMxHme5X774fy72oUcq8D1hVK1cd1KgSLiXgQC6e_0SXTcFaJwu8b4z1dZlbb-tgxbrBc72MIrwTG0m9Yx6LocKEEyOCSlGx2G359zjEzUjKye49O6AgX5C0Fm-ptCR3-9hrBKy2qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور شاهزاده رضا پهلوی در مراسم لیندسی گراهام
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69154" target="_blank">📅 00:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69153">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=VpSaDJvjFQmiKqB5rEOPUYoLAP8Q9C7Bq42TkLrc6LeRaZgi2gXbdsP4UBmb-WdCSLQLAdYF9mFx_DiJ8Vn0LGn7C1B41h8et7DOU2GCiw-2lfSRHd2i_j64zEWuEzuFv2-BFB5L_ceTgTO72qlNRPfs2hz54uHtfwCgwNl4v4GC5qAbEWQLqKJxgvGeashT8YaWHOyd6WRg9_8ZX5X0T3YCjA6k1Bqso_gN5QOEtj7BgbZQK7vg_v5jWSS44wFc-blPBPkGPkL3aR0lWh-MqVeSN7xsEBTvaLb6s51izbQK7QEjEKfnuM8ruKHIQqeDPgTG4qrqpNybIncpgQJk0wLDZui0SHdEWcBuwwqANXrjo3YbEE0WQptNnGLOq1ropB4He3MTes-iW0AIxpNwfxCZeKBaYn3KLtTAToE7XDzbDvzV7DHopHRF5OL-BM86kMlf7jgXZUVp2dEBQBZ0Gz81vlrPFL8PiYwQCRFmE05yW3okHA_MnJfOq1B4URaS8Y2oePYKP8F1m9TUODruUYvZsckkGITOEjVbyvhPT9oPcHowHa_Bjk-2RNNDVuUZPXtX1YbOGxjfqOEBcpj8Mn5jwvyUKZP82BQhZ2yEoSbjglxTj1d4hTCTmC6wOdqoqIr28OyQpo_OtrEWRtHo17iAFw-BYQVcZlbV4CztOE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4805d382.mp4?token=VpSaDJvjFQmiKqB5rEOPUYoLAP8Q9C7Bq42TkLrc6LeRaZgi2gXbdsP4UBmb-WdCSLQLAdYF9mFx_DiJ8Vn0LGn7C1B41h8et7DOU2GCiw-2lfSRHd2i_j64zEWuEzuFv2-BFB5L_ceTgTO72qlNRPfs2hz54uHtfwCgwNl4v4GC5qAbEWQLqKJxgvGeashT8YaWHOyd6WRg9_8ZX5X0T3YCjA6k1Bqso_gN5QOEtj7BgbZQK7vg_v5jWSS44wFc-blPBPkGPkL3aR0lWh-MqVeSN7xsEBTvaLb6s51izbQK7QEjEKfnuM8ruKHIQqeDPgTG4qrqpNybIncpgQJk0wLDZui0SHdEWcBuwwqANXrjo3YbEE0WQptNnGLOq1ropB4He3MTes-iW0AIxpNwfxCZeKBaYn3KLtTAToE7XDzbDvzV7DHopHRF5OL-BM86kMlf7jgXZUVp2dEBQBZ0Gz81vlrPFL8PiYwQCRFmE05yW3okHA_MnJfOq1B4URaS8Y2oePYKP8F1m9TUODruUYvZsckkGITOEjVbyvhPT9oPcHowHa_Bjk-2RNNDVuUZPXtX1YbOGxjfqOEBcpj8Mn5jwvyUKZP82BQhZ2yEoSbjglxTj1d4hTCTmC6wOdqoqIr28OyQpo_OtrEWRtHo17iAFw-BYQVcZlbV4CztOE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش تند چند آخوند به حسن روحانی
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69153" target="_blank">📅 00:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69152">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=X6I9BtIocmRn9yOq-_AuMJ7Ze3THh3Ye0078wDNCZ9qI9ni6_68utEACRKo7Uy5f_Zl9rNftna1ozjN6bpyi6XlBWwibeiKy7u33xvvzfe_j0EKCFSSGUWOkEQR44EMV-cSQaBdfYTxbFvYC-AjHc5JWX7j4XMAGbijLA5MlpP-PRnoX5umCLo_nbfNH3oPZ3gDiCXPdl11kMi4fAhNCYBbha_KbO-DCCGWFeHBUYI2LA4cbh-Lj7-dCVh7sSwd5Qn8XgZgE5SqPQfIac_KjBnyaLdQmUUtATVt_UgVin1ZwUPM1wah5lK2kmjapY_3g1TH_MNIrGdmYTDcLoSg2Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a509030f.mp4?token=X6I9BtIocmRn9yOq-_AuMJ7Ze3THh3Ye0078wDNCZ9qI9ni6_68utEACRKo7Uy5f_Zl9rNftna1ozjN6bpyi6XlBWwibeiKy7u33xvvzfe_j0EKCFSSGUWOkEQR44EMV-cSQaBdfYTxbFvYC-AjHc5JWX7j4XMAGbijLA5MlpP-PRnoX5umCLo_nbfNH3oPZ3gDiCXPdl11kMi4fAhNCYBbha_KbO-DCCGWFeHBUYI2LA4cbh-Lj7-dCVh7sSwd5Qn8XgZgE5SqPQfIac_KjBnyaLdQmUUtATVt_UgVin1ZwUPM1wah5lK2kmjapY_3g1TH_MNIrGdmYTDcLoSg2Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو مرزداران، یه جرثقیل سقوط کرد و این بلا رو سر ماشین و خونه مردم آورد؛
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69152" target="_blank">📅 23:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69151">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekx6gmlBOdgL34zBnWh-6oJJNwkCHguYmc1t9vhsjBG0c1DYXAIe8YWpDEHfrAeBYMClbVbjaFXLZRGxtEnfeUrbZHnaCbGN63PBXsklUWU37OHk5Pr0TVuN7O9pRNQnueJ3ojdDcFmJ49qV_5EEPo-3zmbD1VFUqLJth4Wl84KV2ouVrbgjLE9kMSDOl2-pGRppveTtWj1EreCQ6EXqB6kbLPzqYdk8e81WTMEdCbhvjOwprpgwJ2PeB7tFIpCLMdu6ceH9OYhQLlHDPeRTQbF3f-p87yydMvUpj74ZQ9IO1YE4Y909qUjYcIqLA_wkuPS7PrbdH2QoIK9QKAzDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
اکسیوس:
دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روز سه‌شنبه در دفتر بیضی‌شکل کاخ سفید دیداری ۹۰ دقیقه‌ای و «سازنده» درباره موضوع ایران داشتند؛ دیداری که در آن هیچ‌گونه نشانه آشکاری از اختلاف دیده نمی‌شد.
- تزیپی هوتوولی، مدیر ارتباطات نتانیاهو، به خبرنگاران گفت: «این ادعا که اسرائیل در حال سوق دادن آمریکا به سمت‌وسویی خاص در مسئله ایران است، صحت ندارد. نخست‌وزیر به رئیس‌جمهور آمریکا نمی‌گوید که چه کاری انجام دهد و او را به هیچ جهتی سوق نمی‌دهد. هر دو طرف خواهان جلوگیری از دستیابی ایران به سلاح‌های هسته‌ای هستند و راه‌های بسیاری برای تحقق این هدف وجود دارد.»
- هوتوولی اظهار داشت که علاوه بر موضوع ایران، ترامپ و نتانیاهو درباره احتمال عادی‌سازی روابط عربستان سعودی با اسرائیل نیز گفتگو کردند؛ اقدامی که ترامپ خواستار آن شده و آن را بخشی از یک توافق هسته‌ای با عربستان دانسته است.
- به گفته هوتوولی، موضوع فروش جنگنده‌های اف-۳۵ آمریکا به ترکیه — که اسرائیل با آن مخالف است — در این دیدار مطرح نشد. همچنین ترامپ از اسرائیل نخواست که نیروهای خود را از مناطق تحت اشغال خارج کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69151" target="_blank">📅 23:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69150">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=AxMp_i5Oi5M5gCv2eUpykUyEOFSYEGJ-XBcVGXOJtN2hcCpESK_mbfR9AyPTY7Ctf0P4qdfMfIC1TPsi5ltBmAFWajg86WyyjHBoHg4Vkw0X_KJhM2F3B57L9arDCmhd-awBqNOvPxBdddabweF0JM6L6rupPqg3buGCMJwdHrvMp3CQP-LRb2VX-uR6W2CbX49Isso2hQbEGtmsUc4TheUOJsAdOUHj-1s6BR3memFDderNUIZ4ALXf_fFFbjICmrTyOE4X-CeS49bts4Ne9stTaffP261ZFdNB-aPmqwKgBKsXtEqxCBfSWBrrMrrZXEL0_MHeSkRlH-TSdWfX9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6524c67cb0.mp4?token=AxMp_i5Oi5M5gCv2eUpykUyEOFSYEGJ-XBcVGXOJtN2hcCpESK_mbfR9AyPTY7Ctf0P4qdfMfIC1TPsi5ltBmAFWajg86WyyjHBoHg4Vkw0X_KJhM2F3B57L9arDCmhd-awBqNOvPxBdddabweF0JM6L6rupPqg3buGCMJwdHrvMp3CQP-LRb2VX-uR6W2CbX49Isso2hQbEGtmsUc4TheUOJsAdOUHj-1s6BR3memFDderNUIZ4ALXf_fFFbjICmrTyOE4X-CeS49bts4Ne9stTaffP261ZFdNB-aPmqwKgBKsXtEqxCBfSWBrrMrrZXEL0_MHeSkRlH-TSdWfX9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پژمان یکی از شرکت کننده های زگیل ابدی تو صداوسیما:
متاسفانه من اول که رفتم تو برنامه نه میدونستم قراره برم چه برنامه ای نه میدونستم چه برنامه ای هست
من اهل ماجراجویی هستم و دوستم اتیلا منو قرار بود دعوت کنه مسابقه ورزشی ولی ساخته نشد و منو دعوت کرد تو اون برنامه
ولی خب باید تاسف خورد چرا این برنامه رو تو ایران نمیسازن طوری که با قوانین جمهوری اسلامی سازگار باشه
اینطوری فرهنگسازی میشه برای مردم
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69150" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69149">
<div class="tg-post-header">📌 پیام #67</div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69149" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69148">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSnappPay | اسنپ‌پی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVr8CxSl1Lm6-9GmjPP2j6I5DR97n2PzxMGCO7hO1ttfgYIBYXFFiQuzarOd7OCj_8EkxTXCsHp7rZy6et0XPHQydr25xjWNdi0MAa3NwIfXE5Epon8v-yzRhxnvTmy9V1RGMceVPJChl8H0r8BGzWE2ciCyz0BXyIi2yH9xIhKIKI7whTZ1tKjQUgLqxIV5MvlDpHjAeaknRbS_u8hXd_DZEY--I5KbU3RkQ_zSxn3xqUv3Ii1c9sNZofQxyRKkIx014F0XLM44IsezKp-LqlUmiwZ00DLyjU_S3Jb5JIHrR-MEFGTsIB68OdsFD5h8mY_oJLLz_nEVjhA7d1yc1w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69148" target="_blank">📅 22:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69147">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=Yo_M10uWLoMkjaha_anvWnjitAEBJi3bruwqRPg15dHJZpjhVZ-M0eszqZMDIuOK8w_SNiNtrVaKdCTuc8mD6V-U1k-3BXTQpIwmuHN2jd7c_3DkrZsHCGb-bfa2mNjzbbgqyNfCZ5X4Qkdm4o6WtHPUW4esUvoV05NPxnezFr6BRVOckEMhh2k6cAmewGs6YhZ3T6nMmgZbi8DMwvZdI4OKL3820Ttu-L29rENhkSDSt96sx1e1Vt9agLAADx5F1U9y9tz36beEDY3K31XAwPsI08TIHeL5Ks7eHnt0TkWWBBbkHDO-dPumiztSs_CZieoqVh8gxpd-lu22A7Pq9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04ca836fdf.mp4?token=Yo_M10uWLoMkjaha_anvWnjitAEBJi3bruwqRPg15dHJZpjhVZ-M0eszqZMDIuOK8w_SNiNtrVaKdCTuc8mD6V-U1k-3BXTQpIwmuHN2jd7c_3DkrZsHCGb-bfa2mNjzbbgqyNfCZ5X4Qkdm4o6WtHPUW4esUvoV05NPxnezFr6BRVOckEMhh2k6cAmewGs6YhZ3T6nMmgZbi8DMwvZdI4OKL3820Ttu-L29rENhkSDSt96sx1e1Vt9agLAADx5F1U9y9tz36beEDY3K31XAwPsI08TIHeL5Ks7eHnt0TkWWBBbkHDO-dPumiztSs_CZieoqVh8gxpd-lu22A7Pq9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
من همین الان یک جلسه عالی با رئیس جمهور ترامپ را به پایان رساندم. وقتی می‌گویم عالی، این فقط یک تعریف ساده نیست.
گفتگویی با مشارکت کامل، با حمایت متقابل، با درک هدف مشترک اطمینان از اینکه ایران سلاح هسته‌ای و همچنین اهداف دیگر نخواهد داشت.
یکی از بهترین گفتگوهایی که تا به حال با رئیس جمهور ایالات متحده، دوستمان دونالد ترامپ، داشته‌ام.
تمام تیم ارشد او و همچنین تیم ارشد ما آنجا بودند و در اینجا نیز فرصتی برای تبادل نظر و همچنین هماهنگی مواردی که برای امنیت و آینده کشور اسرائیل مهم هستند، فراهم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/69147" target="_blank">📅 21:52 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69146">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/byxHZ-LFmKD-cnwnHnejNFXLXgIjscCIE0ocqEXp507av0aufDMXnwogVbL-leJ1JiCUnAtP_mcO9AILTFokYpfB4hopof4fUO9MIFXWzaXuPUslIWcehMzwt0YLnbJ1UQ4qF2X20Pv0sJtb7mmkehomYpsVIKnR4rF9yKKD9YpbAEea9-3-VyXZYp72MY5ZBwWpFUPRj99GmCWKCEwOTA-OzRFMoCWvIaXA39CGk9jsK-Tk0jOxAfZNO6td9OTulo901zfMZ_JeEbQJTbid7mZUG_Wgr5ychXD9CIJCcpb6qgsEQj9nnRJYXq7UHm-Evjzm3qk3d8oHUiKf56jNoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
علی قلهکی: مراقب باشید پاسخِ احتمالی به اوکراین، کل اروپا را همراه با آمریکا علیه ایران بسیج نکند
به یاد داشته باشیم که ایران خبر اصابت کشتی خود را رسانه‌ای نکرد و این کی‌یف بود که خواست آن را منتشر کند! حال به چه علت؛ درگیر کردن اروپا در جنگ با ایران یا پیوند زدن پرونده «جنگ روسیه_اوکراین» با «جنگ ایران_آمریکا»؟ شرایط پیچیده‌ای است
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69146" target="_blank">📅 21:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69145">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🇮🇱
یک مقام اسرائیلی:
ترامپ در دیدار خود با نتانیاهو، خواستار خروج اسرائیل از هیچ یک از سرزمین‌های تصرف شده نشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/69145" target="_blank">📅 21:21 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69144">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpldMGhT193qfQdg2RR9Q4dyJhOBp8elpDcmqq26dHGE0TIMWB0vL23vHa-A_4eLhcCllNs5ffk_tBzglJvVX7-J3cwRyJHfyWIX1e0rzU2BEqPUrTVSanJvcbbyqrr3xXsI5pWHBfFfUTnih_nNicq0YHeuCrqCQbFdPSXDmKJgEfQeJVg7AA1DriRfDhKIwO3A7NLHcYjwZZDZB02FKFxXsqKyY2wa1bsYl3qMVF9uLE38sjdMWWcyQWCaNaPLn0r4JuXNX6aWs4AhI-CVnqdoiKUClcADRZzojcAi_Aoa4-kX4vVhHoCs5qb1MtL6cEc9FQ8DT-Mm_Ogg3K1SjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
یحیی سریع، سخنگوی نظامی حوثی‌ها:
نیروهای مسلح یمن نفتکش غزال متعلق به عربستان سعودی را به دلیل نقض ممنوعیت دریانوردی و نادیده گرفتن هشدارها با موشک‌های بالستیک هدف قرار دادند و این نفتکش مجبور به عقب‌نشینی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69144" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69143">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz5r_D5jLLOCqHzgTNRLXGLFcahHBr2PcX2BhW6qyPctbd4fMTXX-HxwIJ2UpiGgR49hSnNNoUwpj1quczpKOSYFWUld98MPHmfB9cD_lZyuMxbXW--LrG9_2k3aoWKSSrCBxdFHI0UqJPRTJamsed4FMr4MdpeaxTCDkpMgYjEKx4vAY9t52nxrRCG5BS38AvRSDm1Hm7FFlm8K4Nhdb8y55SnLHBQTfpykvjossXAyabArgHSb4jw8EyTz7-r77UFtw2ZplZnw7FKZ256vCUG61Fz4Bnz2h98H2i77MhjJN3nXtzOMJxXqFVcrMUNgkrSy33RcbthaNvU1JJc8tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69143" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69142">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
⁉️
کانال 12 اسرائیل:
دیدار نتانیاهو و ترامپ با حضور تیم‌های گسترده‌ای از هر دو طرف، یک ساعت و پانزده دقیقه به طول انجامید.
یک مقام اسرائیلی مطلع از تدارکات نتانیاهو گفت: «ما در مقطع حساسی قرار داریم.
رئیس‌جمهور ترامپ به‌زودی تصمیم خواهد گرفت که در کدام طرف بایستد و چه مسیری را در پیش گیرد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69142" target="_blank">📅 20:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69141">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9zSTkl1vaSa2IWLJDARdu3VICP6G976VcjXh9Zlc-5ARKgfrXan4bNFriXxdHEXqvBC-5RDTmk_RRTEjXIiAYKeyv0SjoibNYFuE8INAcb90JG3HjWXqeB7sNVmC5KkFp61obdKv5BIJspW3eEUYX29KBx-ZY1D2SZLMuPlZKXtf4Qfin0Gkk_aIDn96HJZr7gC1VYRZsCeLhkizu7J1xZfDsUl9R9nKW7AvESgJAhc8KtRjQlDu7uCTEficKUZwt4D6vzaGBs8oLA85x10GDaI0vAo62Gqqjm0aX7F9sV5ugqzBGPgfp8kFqJ3QOOm0AYl5mwXz4ZlSASQoPDPJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇦
آندری سیبیها، وزیر امور خارجه اوکراین:
من با عراقچی، وزیر امور خارجه ایران، برای گفتگویی صریح تماس گرفتم.
من تأکید کردم که هدف ما جلوگیری از تشدید غیرضروری تنش است.
من مجدداً تأکید کردم که تمام اقدامات اوکراین صرفاً با هدف دفاع از کشورمان در برابر تجاوز روسیه انجام می‌شود و هرگز قصد هدف قرار دادن کشتی‌های غیرنظامی یا مردم را نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69141" target="_blank">📅 20:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69140">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001cd370db.mp4?token=Z0noQQSsAkVc0TX0FSlwYFQvYe8Y1A_q95irXXXUlQ-NowECdSQ-mk4myR8VjirJ_rz45D4DMIvavtcEj8S3kblUrdSw-qld_lwwrRCEQhl2x3uZYS-pMVm9EtQbzT2cqkF_XcIRoe0ZslT7cZBIzB-PkbLZLI96Kcv_68wEkyA3GGYecv84r_RDvp6qWex5SHufj117NnsQRoFxEbSF1R3nPv0HdvnbgBLyB_cXr-_DTma-Ja4OvbQnpqhHO2xnKWICKMAeMGALHTvx5WVBvkLl7NOBJjQ0lJlUVvfAZMoovzUqN-ZGhHfS_Rc9QgT1Wr2SlMSuYAmWnPk0yyxWcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001cd370db.mp4?token=Z0noQQSsAkVc0TX0FSlwYFQvYe8Y1A_q95irXXXUlQ-NowECdSQ-mk4myR8VjirJ_rz45D4DMIvavtcEj8S3kblUrdSw-qld_lwwrRCEQhl2x3uZYS-pMVm9EtQbzT2cqkF_XcIRoe0ZslT7cZBIzB-PkbLZLI96Kcv_68wEkyA3GGYecv84r_RDvp6qWex5SHufj117NnsQRoFxEbSF1R3nPv0HdvnbgBLyB_cXr-_DTma-Ja4OvbQnpqhHO2xnKWICKMAeMGALHTvx5WVBvkLl7NOBJjQ0lJlUVvfAZMoovzUqN-ZGhHfS_Rc9QgT1Wr2SlMSuYAmWnPk0yyxWcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
غریب‌آبادی، معاون وزیر امور خارجه ایران:
ما در ۱۵ روز گذشته هیچ درخواستی برای مذاکره با ایالات متحده ارسال نکرده‌ایم.
برعکس، آمریکایی‌ها خواستار گفتگو با ما شده‌اند.
آن‌ها همچنین پیامی از طریق عمان برای ما فرستادند و اعلام کردند که هیچ‌گونه اقدام نظامی علیه ما انجام نخواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69140" target="_blank">📅 20:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69139">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUvRo7IRzN6Tfl6BzsBYtTvQiKPZyZEcbhXMMViOdEq_UHOjEnQT4yU6-J71qbGd7BaPzdXWFYcwsXrgzRIYAum3EOEmf5rDVBzMj6ciGukXEe5FJhcQhBVWoHJLPTxa9ozXGXUHOcgO09RlusUBNBapKx9jyXZm2NXv4WqY66Ro88_O9-FNcAA4CphYtj4aTGxjbYM4snq3b0A1w5mclBfMw4fPzs15i9DZnU_DViEMIUvK02ZxVDreERKkD3f-lkn8C7uyKTjmr_GiAFosle7H34mc8XwzFVtq3wWz1-6ev16hVx30ZqKKzhFlgLL_pePJGR3PPB8w6V682U65Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
سخنگوی کاخ سفید:
رئیس‌جمهور ترامپ دیدارهای خود در دفتر بیضی‌شکل با رئیس‌جمهور زلنسکی و نخست‌وزیر نتانیاهو را به پایان رساند. هر دو دیدار مثبت و سازنده بودند!
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/69139" target="_blank">📅 20:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69138">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=Vk4XiHIMa0em39m7koZ1UqpM6O6IQFpff-AzLNuUrF954rG_m1gWBxCgDBgFX4dXKAtNRrNWvZvg_OD0rY7QudeTLeFOJ5rR1uClEEHW3ffqvoYtQQ7Xmam5fIawubq7fJXDYb3crrZ5UC0VZdgJYp2B6EK2Ii8nUsv0aV6bxbru8EHWzvGtFnN_dkthYT0Et_1WMwpFwCTvWHVqlNuPu173UdWuOGtUTXEAVLvPCqmDAx7GJ_fYt-Zs7-ttqnjTeYGCp4d-OK-yzqEL4X-XIKhuRxPhj3yEeohn0rAj2N12YZW9aEwjFp2qXcHRX8FWZVgnHlENjJq07QzYfXTVtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd737689.mp4?token=Vk4XiHIMa0em39m7koZ1UqpM6O6IQFpff-AzLNuUrF954rG_m1gWBxCgDBgFX4dXKAtNRrNWvZvg_OD0rY7QudeTLeFOJ5rR1uClEEHW3ffqvoYtQQ7Xmam5fIawubq7fJXDYb3crrZ5UC0VZdgJYp2B6EK2Ii8nUsv0aV6bxbru8EHWzvGtFnN_dkthYT0Et_1WMwpFwCTvWHVqlNuPu173UdWuOGtUTXEAVLvPCqmDAx7GJ_fYt-Zs7-ttqnjTeYGCp4d-OK-yzqEL4X-XIKhuRxPhj3yEeohn0rAj2N12YZW9aEwjFp2qXcHRX8FWZVgnHlENjJq07QzYfXTVtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نایب‌رئیس مجلس:
نباید به ایالات متحده اجازه دهیم هر زمان که مایل است حمله کند و هرگاه با مشکلاتی مواجه شد، عقب‌نشینی نماید.
اصلا نباید با آمریکا وارد آتش‌بس شویم.
آتش‌بس با آمریکا معنایی ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69138" target="_blank">📅 19:55 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69133">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xfp2e8G8uQ_KGhIKWK1klGV_lygugmEwvzdGee0Tkq28LMEKQ0s4-93jgDuqCfwPWmKYSWD2NqL3QX7X3iwJGxSeVAKWggMIALgNNeH3i7bWqbRF_0U3vaGri_xYYHNA7bZ_QwKYUw_OpXabTKvrvFJkE6tFHh8JGrPFIzrVnnUbETA9wtnGwPFNS23v9XBTDLgwFyJ9Rxz1pAwRKhc6BWKqinZs44L6wflCiXJbLjm1CxMBEpwuXdYMnW2dHqH9P7V7ZrXReXWg6f6uFYRzhCDALFoAlIUkihBI9flHOzBKDJcPyQVlStpXdQz6a84Qh6ieIGkp5sZavzvEASenAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYLd-kCjRDUypzKqCRJPXM57O1-uwGTJrVdqUI3hFb8CyTDw3ISk8F2ZDr3Bf5YzU-gUYZlc2tWnCVHX4jEZ8s-dccJCyTpoH_sPIisqWVM3gtAlDU7B9hoN-yyZzIiirTdTHm7ykIJ-z1GeH4r7sF8gC-90gcKl-wTOKq0ah_pl6j4e2zugw9HQex7kDb-cEfDbs-99Sj0aH-KPcapOjjv1DM5bJuKSW1dz-VaZiZng0Ovwg2JHCqvn8hF24re5VeADgHBEGzjitaFCgHMKUGkIY2UPoFrTbLyW5txrEM74tyGGzqhOKNY_TPOwlPccdKHyxc1Wz9VZ_qKQ5sLJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MNKqRB5JmKfE-sQWCMN-NTUgMnoFtlOTCGfhIgWkuh5RLmEkotSQJiVzNzz6axgLpK758go8I-zCWUF366q6XWIkKWCYZbKB2tJKzWU174Qt4329m5aRSbGk0Yz_Huc6PBRt1LX6zwD52T9Tsq-_QM2rqX2ks7mYofefTkwL55i_Qjk3OKRwAIO8WI8W-vBo0JEhWeXboHRv7X7cgjU5WNzimOxcEfPszdmciJJiXKCxBREWrbS3g8k4NxdcRk9Gk1pGpUlPnCQTvrtkFE1JeouFcUMPERKdgXT_npC52lzTHPaa7-xGf_REFCpvxIOMZtnOFK5Jg9qAjxxi1pWeNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i6JH1j0skb7g1uUrtXaZTK8upf5bXPP7rAf3CGxeBD_o_oXWecvrqryzuH4QflUTohRk8MltfYMc--Gh6-WeXZlhKrZdBEaRR2VhOfElRB9fAUpaBM-guiF1aubsMlK1P3eb81p3Wtz7OZkDtsfqNe89jdGriX3jYfqUPu_q7UJLqsxHVzAntXpIUJ7yH-vzjAYfTbXCAJRztoU_lFNTAO_u7zYHU3YrUTOIx7EM7Lp5YAXAfAylBZIINB0LfWKR3wMEtsfGb9zJ9jRLnmEoaIJyvTj8qjT01YwE_Hl8f2iodI9B50bxRDn9GKBBebpSzaU8kyXk0QWxQG7y6VwcmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S7F0GLeGfgbM56VrDNqdGUpLXtjNAWbxOYSP6mezydBmOCAInzCihIhlkPMixJ2Mp8xsgqjXhNk5DmCFGCfvSfUKcSTb_2H3mi1qrBgz0JyZv2XKIc6nMhKLfzTUsbkC3VJNs4dpsL2ZyXntY8TqRXPJ-XOTOZnSUM8LyZqQ2KrJ4oYzCqGDvG9pb81JY6WH8jkMHgpPloyKntGtRQMi7RDiE5DSkawSHuftrnnXzfSW35At3yAVvSBSCDj8jkU9-yj4Zav11h9eHDA1i_3yXuK81KjfsqZ0dGuxfhMO5XM8vVjOr-QaWTwM433ixtoTEN66cviZ7xNyRFQPnMyIOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
تصاویری از دیدار تیم نتانیاهو و ترامپ در کاخ سفید:
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/69133" target="_blank">📅 19:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69131">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XhaQqJCyqiArVI7WMLlJK7GhV-1PkwklgGrY1965WNwE9pC2lZwBZGkwWqTLSnoSxP0uHA7qz04wTZ9A58wXiAbRuplM0chr69LftrBsW4Y26Czvg-GWmgXZZ9dOv6hOTr-D2sGStGC4HbKjYDRKSRtx-IwXzurO9giK3Hpk3TMvsCqoq_kxgOjwncQRSz1LP7ocmDDfqjk7Y_vZtaKJYeeQActtlk7ae3pVRsBNUYUYHf6YjndgHaZw0sEqdBAQ-EUnIxEQ8HoNeT7CVtoKn_XqdP5wDoRORdE9iF0XcJpOqcpBLw0gYmZtI6-8PzRe4oPndIZA2O0q151miwVB6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j28AXEMXOCCrxtQfBRCslVj-j8mchbfqpoUz7zjRQy5ibAAsMurIbbFjnNyYli1HAUD7U8MoYMLgj7zJK7N8GxW53Xd3EEy2e3Q9rQaBzuWCkEOlHDFBErHW8P8332QG9r3q_mpZAsaAzDLb8J8eFAOBJmrIwk61oWxYLivf0JBSSR2JcPZGGQjcog199R8rYNytdAdw2ulb_QvuBKhE5WhN4TSpLn411mid_bP62fBrMnXgZt1OY15M5Gp9TXkYb1lZHEexnePOZTpVClHxsStEkBfN2rtgPWQcW2PLtsfmJs6wqrLO-cW8onhYOaAcqstlSzItEIlqWYZYYnGxSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست وزیر اسرائیل، پیش از دیدار با رئیس جمهور ترامپ در کاخ سفید، با مشاوران خود گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69131" target="_blank">📅 19:16 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69130">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=v3yjprkHJkGILfdyUiuj7k-FTs8Ua2LT1RzCaAzublM-d6UymkrS6D_dR0jGo75G-hg1Fxkx013tQaXdxJF7fuxogKV_1k5y_BXf1cjsdREMSVLKnakBwKup20Z-_HjEV-2xxafFpHiyYMqKSITlh_bPi_gr_Gl6gsSldQzgDhTayopx3qZfKzWgpIEn0WU6j8JfJN60Gz6-Zj4o7Bu3Tk4i0LkjQ1_CMOqM8DofXHPHJPcc_iGLiWizRp1I6qS6CtACKNrqeoOShPPA56zq-rpy9aiUd1ySlrXGj_rJcwOAWf0M1XvmxGnx-_uMeeo7mmMDpOSW29SfycDx5OH8_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6822c0ad1f.mp4?token=v3yjprkHJkGILfdyUiuj7k-FTs8Ua2LT1RzCaAzublM-d6UymkrS6D_dR0jGo75G-hg1Fxkx013tQaXdxJF7fuxogKV_1k5y_BXf1cjsdREMSVLKnakBwKup20Z-_HjEV-2xxafFpHiyYMqKSITlh_bPi_gr_Gl6gsSldQzgDhTayopx3qZfKzWgpIEn0WU6j8JfJN60Gz6-Zj4o7Bu3Tk4i0LkjQ1_CMOqM8DofXHPHJPcc_iGLiWizRp1I6qS6CtACKNrqeoOShPPA56zq-rpy9aiUd1ySlrXGj_rJcwOAWf0M1XvmxGnx-_uMeeo7mmMDpOSW29SfycDx5OH8_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مدیریت بحران تهران: این بلندگوها و سیستم های صوتی که نصب شده آژیر خطر نیست
اینارو نصب کردن برای پخش صدای اذان و ما برنامه ای برای اژیر خطر نداریم!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69130" target="_blank">📅 18:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69129">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmMq7rirw-nj8PRxjuug0PLePURW5Gul5IHTaIvwNS4KS5IxbxrA6DcwPjsmoWvaqKghvaAHYdWYYdF-KbhhBwRzOV-3-VX1GC7kaVr-pJoU6Ml9saUKFqCgXB4bI2PlAaeCCT1zAJc5xIeSQJrYwe6em3qBidE3X52hRZFRWR-5W6rlKm-SqFKTRxr-n4Dtr81tHm5kZuGH4bkmeHtJ9IBBOF0cfH9zTgWC8iS7Sq6pk5IsDG9PUK5HvE6KWiQUHl3gOQksA1947dcVAtZMpqNRhz9HMQxymcViuIp0E9NK6nDIWRAseCgly89swhgDren5oqNHEUiZaKHnLYQY9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
تصویری از ورود نخست وزیر اسرائیل، بنیامین نتانیاهو به کاخ سفید
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69129" target="_blank">📅 18:37 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69128">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
کانال 12 اسرائیل:
دیدار ترامپ و نتانیاهو دور از دوربین‌ها برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/69128" target="_blank">📅 18:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69127">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
دیدار ترامپ با زلنسکی پایان یافت؛ دیدار با نتانیاهو در نوبت بعدی است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69127" target="_blank">📅 18:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69126">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=fpnzzFwpUKJ1TTyCXl0g9roqsg-s0bXeK-TDKExDpD8YRzuvTDamhowlnUrE__-BK5_uqGnvNXgj0gszRKMKDVasGToNe7Ff_s2EAyCG6c_gntdfX9OxDGDyjESc7kvSXHlmSEqnyPDmU96FQDf-OfyBZU2OZDh2-sespr0Es6iI4PcxE-X5vBSfz4cAWuz78HN2dnnoFmdcH-VWc2HtVgVBn9ouibT14rwbpR8iyuEmDQ60ko2ho6F6-virPO-8Lt0RINf9fOpl24YZFSzCy6HKzzybr3ig_HiNnDylus17cdhdVQDKYZL2jAfxNAONl_rgeNC6mes3m3yRRW-zYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8339055d6f.mp4?token=fpnzzFwpUKJ1TTyCXl0g9roqsg-s0bXeK-TDKExDpD8YRzuvTDamhowlnUrE__-BK5_uqGnvNXgj0gszRKMKDVasGToNe7Ff_s2EAyCG6c_gntdfX9OxDGDyjESc7kvSXHlmSEqnyPDmU96FQDf-OfyBZU2OZDh2-sespr0Es6iI4PcxE-X5vBSfz4cAWuz78HN2dnnoFmdcH-VWc2HtVgVBn9ouibT14rwbpR8iyuEmDQ60ko2ho6F6-virPO-8Lt0RINf9fOpl24YZFSzCy6HKzzybr3ig_HiNnDylus17cdhdVQDKYZL2jAfxNAONl_rgeNC6mes3m3yRRW-zYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
🇺🇸
رئیس‌جمهور اوکراین، زلنسکی، امروز صبح به کاخ سفید رفت تا با رئیس‌جمهور ترامپ دیدار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/69126" target="_blank">📅 18:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69125">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=lxx-FC1k7kv0Lr3QVTe6w_inUGYiEJZ6DXHQr0SXt7NUqI0GxXDHUgWVExUlYSGQNxPJ7YuYn1GiLiKPpPE_DpKhaV-N9mis2GkBKDE_q0rZxB2jmhD0YJMEGAFbhoxpRrnHtz36B_s9Zoil2EitVwpgmH6Re0bdh_TaQ17hs4V52Gr9QhZ-31lPySbHX608LT3xk9n99xLai_T4RiYJk0pXEPKZ0WPLaiGB_UkzO2LNt9XybBJ0A8V6pCV3Lv86y0s7-12J5gNLQWJn0aDJ8_owiZDGMKGGZREn6sbUPijiDzMBjHwwgir3AMgscvaY_njDQHIwGqc9Hl_y5sb55A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634ef5a127.mp4?token=lxx-FC1k7kv0Lr3QVTe6w_inUGYiEJZ6DXHQr0SXt7NUqI0GxXDHUgWVExUlYSGQNxPJ7YuYn1GiLiKPpPE_DpKhaV-N9mis2GkBKDE_q0rZxB2jmhD0YJMEGAFbhoxpRrnHtz36B_s9Zoil2EitVwpgmH6Re0bdh_TaQ17hs4V52Gr9QhZ-31lPySbHX608LT3xk9n99xLai_T4RiYJk0pXEPKZ0WPLaiGB_UkzO2LNt9XybBJ0A8V6pCV3Lv86y0s7-12J5gNLQWJn0aDJ8_owiZDGMKGGZREn6sbUPijiDzMBjHwwgir3AMgscvaY_njDQHIwGqc9Hl_y5sb55A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سخنگوی قرارگاه خاتم :
هر شرکت یا کشوری که از دارایی‌های بلوکه‌شده ایران پولی دریافت کنه، دیگه اجازه عبور از تنگه هرمز رو نخواهد داشت.
همچنین به ترامپ هشدار میدیم که هر کشوری که از پیشنهاد آمریکا برای استفاده از دارایی‌های ایران استقبال کنه، شناورهاش از این به بعد اجازه تردد از تنگه هرمز رو نخواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69125" target="_blank">📅 17:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69124">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=MjfxlZtWI5jtAa57H3ZbVqSYY055CIWSLVLS2WdO-xLVXQjraq5kovLXO0Ns34SKocWTDMsXROERoS62JOISKYU5vBR4SDyedYV0z04iNG6uoptXDh5sINl4suBvlGaDt4oW-j_JNfR-qDsPIu5_dKJQKDGul4TdLuooiLHCsIIqxs-Z0Ae3vmm_oXUMrJ4hvzh4bGdNuu60Mh_oTgGR4KL-boULGXzjXlx3JUw85x_9xo_wQv2mO2k86VvSixwd4k3ZbxN5hWMSKgK_NTRlI4s6LHgm3ST5AxvWelv2DluvQ63NaOpY1mO1_gMtzMYWkwtwLAu7VxzMmSD2vVX3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9cd6b53c3.mp4?token=MjfxlZtWI5jtAa57H3ZbVqSYY055CIWSLVLS2WdO-xLVXQjraq5kovLXO0Ns34SKocWTDMsXROERoS62JOISKYU5vBR4SDyedYV0z04iNG6uoptXDh5sINl4suBvlGaDt4oW-j_JNfR-qDsPIu5_dKJQKDGul4TdLuooiLHCsIIqxs-Z0Ae3vmm_oXUMrJ4hvzh4bGdNuu60Mh_oTgGR4KL-boULGXzjXlx3JUw85x_9xo_wQv2mO2k86VvSixwd4k3ZbxN5hWMSKgK_NTRlI4s6LHgm3ST5AxvWelv2DluvQ63NaOpY1mO1_gMtzMYWkwtwLAu7VxzMmSD2vVX3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69124" target="_blank">📅 17:38 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69123">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=nqm32JCkQAQD3jsM8q_a5sI9vWtT1EBdNvQzAb-JN7kTo-fKor3Avpc8Ee7TzBsOs1NJ9SUb5ldo_U9rdawTBwi4wDuHOETovS5_bmT0_724CSIVvLKxQdBEvXO8M7pBwywKmB_7WraHEXEMOad0rMdlzxGkb8LnphZ1IEEZAgQS27P2AwUz0v_Pudx1zhpLoHwKAq4sxyJTu0kHu5I6OZYGp13e46YC49t4eympiLriSTiLnipCnsFu_KnNwTfnPZceEIKhs7GQHo8nxwKp7-yELrxFxXSpwl2mckkxll6x5ik9CDGgLZlD_QvAT72UGuxQm-qL9RnysvTWJ45q-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/803209f6c9.mp4?token=nqm32JCkQAQD3jsM8q_a5sI9vWtT1EBdNvQzAb-JN7kTo-fKor3Avpc8Ee7TzBsOs1NJ9SUb5ldo_U9rdawTBwi4wDuHOETovS5_bmT0_724CSIVvLKxQdBEvXO8M7pBwywKmB_7WraHEXEMOad0rMdlzxGkb8LnphZ1IEEZAgQS27P2AwUz0v_Pudx1zhpLoHwKAq4sxyJTu0kHu5I6OZYGp13e46YC49t4eympiLriSTiLnipCnsFu_KnNwTfnPZceEIKhs7GQHo8nxwKp7-yELrxFxXSpwl2mckkxll6x5ik9CDGgLZlD_QvAT72UGuxQm-qL9RnysvTWJ45q-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«اگه من رئیس‌جمهور آمریکا نبودم، امروز دیگه اسرائیل وجود نداشت.»
«اوباما فکر می‌کرد می‌تونه با دادن امتیاز و پول، با ایران دوست بشه؛ اما بعدش رفتن دنبال توسعه برنامه موشکی و هسته‌ای. طی 50 سال گذشته، همه رؤسای جمهور آمریکا یا کشورهای دیگه باید یه کاری می‌کردن، ولی آخرش همیشه این آمریکاست که باید وارد عمل بشه.»
«اونا عملاً قبول کردن که سلاح هسته‌ای نداشته باشن. فقط مونده این توافق رو به‌صورت رسمی نهایی کنیم، اما با اصلش موافقت کردن. چرا نباید موافقت کنن؟»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69123" target="_blank">📅 17:36 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69122">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69122" target="_blank">📅 17:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=UnNC7Gr4DC4kA--kf-Q4dkXfGO5bo0IB9YOhyqtDyFf6iZrBnSlMbiCtj2bnLnfbHX3eIxvoKyNTwUV03pN7_4VrkZTibrg6oOSbgClYj_AzFngZTDDC633QnzSnpjqPOW8E4D9QesEnYYoUKlAGVMf2ADh_P051Gsxfyq8oadcaxR39EVQQkQYss8upz8hEgPaJlW5fXmkiV7fJKQS-BrYeMpR0LfyF6uicCf7JQhYRkeEWIRSXH_INQyFInAwsYlWbnvEBr_OM9eYzm0VrHm8Gv8Ub0fOamiLO0GdIGnhCSsTArHW8bdtwA7I8IP0w4RzLdi3acFRwblEGS3Ab_DUnIGPD3h1YK2HcHKlLDlCng2vJTYvo6PdgS6pQoTXurP_KUW0Pfe7Ep6aK6ju-dQHafpp_MlUeLSs4WcBJ5rJf0fo5hV7a3dWofZBlzBq8G0iAdiUqRUB78LDu8YzXRH9HF1Qf0Fev2PNzHHJXYvuYQN8o1SQPBQyscHu7GVOFO9DbQ9crU09ntn3DdhZvFtLSscm7t5R4GHmkldoN4tW9pK1l0kIqR5cBkvTexZ39Mtvy6j47HoLhu6bTkKfAHcIzppMRRH0-yi4Ui6BJVZIPrWPDYRiUzI5jFQcIpL23vooduTtFPsXc-hGHT9x94m5nP7_BwGlB3gFEepB0Emc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a44e71f50a.mp4?token=UnNC7Gr4DC4kA--kf-Q4dkXfGO5bo0IB9YOhyqtDyFf6iZrBnSlMbiCtj2bnLnfbHX3eIxvoKyNTwUV03pN7_4VrkZTibrg6oOSbgClYj_AzFngZTDDC633QnzSnpjqPOW8E4D9QesEnYYoUKlAGVMf2ADh_P051Gsxfyq8oadcaxR39EVQQkQYss8upz8hEgPaJlW5fXmkiV7fJKQS-BrYeMpR0LfyF6uicCf7JQhYRkeEWIRSXH_INQyFInAwsYlWbnvEBr_OM9eYzm0VrHm8Gv8Ub0fOamiLO0GdIGnhCSsTArHW8bdtwA7I8IP0w4RzLdi3acFRwblEGS3Ab_DUnIGPD3h1YK2HcHKlLDlCng2vJTYvo6PdgS6pQoTXurP_KUW0Pfe7Ep6aK6ju-dQHafpp_MlUeLSs4WcBJ5rJf0fo5hV7a3dWofZBlzBq8G0iAdiUqRUB78LDu8YzXRH9HF1Qf0Fev2PNzHHJXYvuYQN8o1SQPBQyscHu7GVOFO9DbQ9crU09ntn3DdhZvFtLSscm7t5R4GHmkldoN4tW9pK1l0kIqR5cBkvTexZ39Mtvy6j47HoLhu6bTkKfAHcIzppMRRH0-yi4Ui6BJVZIPrWPDYRiUzI5jFQcIpL23vooduTtFPsXc-hGHT9x94m5nP7_BwGlB3gFEepB0Emc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ایران دیگه نیروی دریایی درست‌وحسابی نداره، نیروی هواییش هم نداره و ارتشش هم ضربه سنگینی خورده.
اگه توافق نکنن، دوباره اقدام نظامی رو از سر می‌گیرم و کار رو تموم می‌کنم.
می‌تونم تو کمتر از یک ساعت بیشتر پل‌های مهمشون رو نابود کنم و ظرف یک روز هم همه نیروگاه‌های برقشون رو از بین ببرم. این رو هم توی مذاکرات بهشون گفتم.»
بازسازی پل‌ها سال‌ها طول می‌کشه؛ خودم سال‌ها تو کار ساخت‌وساز بودم و خوب می‌دونم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69121" target="_blank">📅 17:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69120">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI6zpb3luiGRh_JtrRgDsegeiTH1DBJFHF7yFKlSMpswqSrb64Lf1O1JZVV8gRuPaFWu0xzv2SqX_QV-TQJ_AunK1WYcz2yQIlA3zMtcWq6OglXqpf43_7gSel5_EOk-gkSzlktn-MrH3D7IUGt_67kFZx5b0Zb4pW1JfBw1LFaU0Bp2GJWXZHXk-A-TqoU1_uP6QX8bQnIy_nl5IJWDok5PvZGKGCMWqdblK6P9JdNBS8iZCIJg4wweaX4EgXIgRCA0oYL7Z4VGvNOsWhIhAt9XcphnaDYr6qxjOXuqJHxxFO0AxUW1PQreP3L1zml7jzusDcMlrWwUaK498J1wqvaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b8f908317.mp4?token=cuJf6AxFFFx1K_ROVcXbKYB2CrU12Hjbp7YofL96hEoKRDUzPiaJTdYePPbSpgX3VMWrE0iNqF2ZfkpyNKR5uJ5KoF2Lhq2VC6dJkJlkUhvedBz6NZPlmG3P1AoNmzYABBX5ETpcaZC0yKS5PvV6S9U3m03ZE2YJLnbSQaEWyV4hFdrBP29aDMy5yuwDN_1Wr-Sb3_lQii2NNLURn1maMVJsSGgc1oRr0SsTi2uSweTM7y0AUcxvpUXANxdn-_mRdA4rzYcQbHvKdzR3vVHCGNKKqdh5Af-mPlw_HhQst3wvqdV_ADXi5km3_g28yax0ePLfSp9cyaeiNX9B0rhLI6zpb3luiGRh_JtrRgDsegeiTH1DBJFHF7yFKlSMpswqSrb64Lf1O1JZVV8gRuPaFWu0xzv2SqX_QV-TQJ_AunK1WYcz2yQIlA3zMtcWq6OglXqpf43_7gSel5_EOk-gkSzlktn-MrH3D7IUGt_67kFZx5b0Zb4pW1JfBw1LFaU0Bp2GJWXZHXk-A-TqoU1_uP6QX8bQnIy_nl5IJWDok5PvZGKGCMWqdblK6P9JdNBS8iZCIJg4wweaX4EgXIgRCA0oYL7Z4VGvNOsWhIhAt9XcphnaDYr6qxjOXuqJHxxFO0AxUW1PQreP3L1zml7jzusDcMlrWwUaK498J1wqvaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
«ما دقیقاً می‌دونیم تو تأسیسات هسته‌ای پیک‌اکس چه خبره؛ از حفاری‌ها، تونل‌ها و جاده‌های جدیدش هم خبر داریم.
این اصلاً مشکل بزرگی نیست. بی‌بی مدام این موضوع رو به من میگه، چون می‌خواد همچنان تو این قضیه نقش داشته باشه. اگه به توافق نرسیم، پیک‌اکس رو از بین می‌بریم؛ اونم خیلی راحت.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69120" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69119">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=qnGjy0C3TbVn1UC1tCSVcTYOJgPFAZLSj8cAY9logIw7mWwjYGa8cSyn1EJ-idYKort-_9NDLysB7VzU9hzD-EKKpPY6d3UtJsAiM2aY4tiSwqSZ3JAZmzTbjPhebkZR8I9R2EDizkxGLuaCm6HBPANBOPfoyp6if79M8QesF5rSesVUtHl8w-lKYXd619Cd-KipNDMONlH8V3Ob6YtQzNDS82sZKtiHLH8Aj-OmUDByyZ6KJpg8PmyunimJM1F3faHbMdaYmkc_AZYBEy5SHZqmhEuoTbCzVc_R60JDFup56IGrlZ4FERwr_7vNsFWkkoKLNzfifU0k7fmdI4EV8mYoSYrPHPPigjZ5JpuP1cOtioN_SuquqjCYTpYb6akGu2JY6gzY1zrovSni0PulNTaBwIHUZOtQyWkt035F8QZ1nnW6d2ioFeRbZdFhDKxBTgCpPmShhi7MN5tAhHH9NPxSTv8i-NObaBPBhI7dZW2en5GFhBtsZdNtwrQjUb3wf8bkZ4M7SsyScrJOhqxP9aOHyniAz0l-JUNa9JgJQc8vlitcOKZqIqMs4Bq4qjve6HFQjRV_dKdPaEpE3bOmaVUFN1U24EfCLAuQQubIBklTM9BwL86gA8OQdiqcP6P4f_v9sHZfanNmWWPKJeLiby9HMy2rgeXgsJJmx-aH3qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/825bd1594a.mp4?token=qnGjy0C3TbVn1UC1tCSVcTYOJgPFAZLSj8cAY9logIw7mWwjYGa8cSyn1EJ-idYKort-_9NDLysB7VzU9hzD-EKKpPY6d3UtJsAiM2aY4tiSwqSZ3JAZmzTbjPhebkZR8I9R2EDizkxGLuaCm6HBPANBOPfoyp6if79M8QesF5rSesVUtHl8w-lKYXd619Cd-KipNDMONlH8V3Ob6YtQzNDS82sZKtiHLH8Aj-OmUDByyZ6KJpg8PmyunimJM1F3faHbMdaYmkc_AZYBEy5SHZqmhEuoTbCzVc_R60JDFup56IGrlZ4FERwr_7vNsFWkkoKLNzfifU0k7fmdI4EV8mYoSYrPHPPigjZ5JpuP1cOtioN_SuquqjCYTpYb6akGu2JY6gzY1zrovSni0PulNTaBwIHUZOtQyWkt035F8QZ1nnW6d2ioFeRbZdFhDKxBTgCpPmShhi7MN5tAhHH9NPxSTv8i-NObaBPBhI7dZW2en5GFhBtsZdNtwrQjUb3wf8bkZ4M7SsyScrJOhqxP9aOHyniAz0l-JUNa9JgJQc8vlitcOKZqIqMs4Bq4qjve6HFQjRV_dKdPaEpE3bOmaVUFN1U24EfCLAuQQubIBklTM9BwL86gA8OQdiqcP6P4f_v9sHZfanNmWWPKJeLiby9HMy2rgeXgsJJmx-aH3qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌐
هزار سال ایستادگی،
نامی در میراث جهان
قلعه الموت، افتخاری دیگر برای ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/69119" target="_blank">📅 16:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a4mtpIgAjX_Y3MOM5ppDUUlZaj6CbxJfRsfI9JbaRDDGu0sq5G_73KtxmovIQWFE4-8ahbCIy71arXncyYOEt9TAEyerX6yjku6R-A61ON2fvi3v3wwQ3z80HXJD_nOI4urgOM5MCrebgyToHkCheOZhckVxGvYPLqNdrmuik9nocZ8I7ssjx985A_yzdDpABPx5u0G-J3feNik4Mx_is2c7yS8eaypa74HzHGZT922LQyuV4ZypiiqtOWYln9ZTi8NZIwMEhvEoISxyN6x5UmYl_Q1ngsdHu21oF-_OBPpHLT707NKKzmkaadicKwtITYc2JBm4SQKFQ8CqW80vXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYRkwvsa6upXB1NBrzyQQyP2AiFFC15gv0ESSXzCTrM3hRzFhvUG00k6_2vjteW37xiT-xk0jFUYcjeU9Y6ld7KUyq4Wng2zHXxYje_UPqvueWhe-3u00GuafUpnPPOhQyia3odulRHAL53mIgw4lt1ssSuDQoe2LGRpNj6Fxsoo-ntGyeKWlmyp8dIXAOLAgxaiwZTkgfAkpA3d8mw-zs2TXPQtCpIwVxXuyMd5EQ6Nc7KlkaiK2yESyBRLuXpl9MURVgoPB8FaMm9zqns-hhH6IYbS8OhJE573tYTgpJ4cDY5DIfNtTHYt4fyQjxDAYJjzDk1GLfo4dP08nuTiPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
🇺🇦
❌
🇷🇺
اوکراین بیش از ۳۹۰ پهپاد را در طول شب در منطقه مسکو به پرواز درآورد، که به نظر می‌رسد تلاش دیگری برای حمله به مراکز لجستیکی Wildberrys باشد، اما در واقع به جای دیگری اصابت کردند.
در Kaledino در نزدیکی Podolsk، یک پهپاد باعث آتش‌سوزی بزرگی در یک انبار لجستیک شخص ثالث به مساحت ۱۸۳۰۰ متر مربع شد که به Auchan، Magnit و سایر زنجیره‌ها خدمات ارائه می‌داد، درست در کنار یکی از بزرگترین مراکز Wildberrys که به گفته Wildberrys به طور عادی فعالیت می‌کند.
در Chekhov، یک پهپاد دیگر به طبقات بالای یک ساختمان مسکونی برخورد کرد و به بالکن‌ها و دو آپارتمان آسیب رساند، اما هیچ آسیبی گزارش نشده است. بقایای جداگانه باعث آتش‌سوزی تایر در یک کارخانه بازیافت لاستیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/69117" target="_blank">📅 16:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=NrQ3ccy2D5QvsJHxg0Ak7rcp1JG8ux8HGUNGCS-dlNV4aje6J9Adk5n24LaswimOxzbN0lwUhuX-p_vTbc5Q4QWMiyNZ7BfreESVl5KwWYbPEscBTlLx7TiI9rJbjUka4UgdJgVZG0hchmsM91VxM0mE9Uubihz8LKI1csaGTw9vMYMwcAIGt-eD3TPdC8brQqOnxa8a0JKhX3QSb4aqyNcBvU4hh6N05rGhX_u38Qzx0wpDAD0G8f0MHI2QIhI0V8FLEZFLTkSi3z5KFeiK9OPKYXpXKNdOhteQPoxG4HAR-rA6QgJ1jhAFrx_n7VCCz7w0TMbx8m1ppjiP4gYqRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0df10b659f.mp4?token=NrQ3ccy2D5QvsJHxg0Ak7rcp1JG8ux8HGUNGCS-dlNV4aje6J9Adk5n24LaswimOxzbN0lwUhuX-p_vTbc5Q4QWMiyNZ7BfreESVl5KwWYbPEscBTlLx7TiI9rJbjUka4UgdJgVZG0hchmsM91VxM0mE9Uubihz8LKI1csaGTw9vMYMwcAIGt-eD3TPdC8brQqOnxa8a0JKhX3QSb4aqyNcBvU4hh6N05rGhX_u38Qzx0wpDAD0G8f0MHI2QIhI0V8FLEZFLTkSi3z5KFeiK9OPKYXpXKNdOhteQPoxG4HAR-rA6QgJ1jhAFrx_n7VCCz7w0TMbx8m1ppjiP4gYqRIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
بخشی از صحبت های دیروز ترامپ در میشیگان به زیر‌نویس فارسی:
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/69116" target="_blank">📅 15:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=ZJnrqbTG8vC2JXRzCtHe73p4AiSXnYHnb9g_vAJ_jPoTb5JPDjG5ItEWTv_dGYLFm3QlfJx5vwpdQcutSUiF8vK_KxMciBlteASbouDZVrHynb_iQ3UEwNZS92yLrIiOwj25T-WiF46BizCCgbARSqOeCYTB4so-Lj3-1EQRueGXJ249x-qqvsJXIn2brTX6rFHYwjlINqkgVauadty0Mc1ypyFAlid3biBtCs_W87ByY4WJJ037ENTocvZ85wPRl3hR0GM88nFpfyXnxOMGr9eDZdnRA3rqbZtulfsUKfx7HlJ2JZVzH_1T5Vdf7odVJo_3OsU-onc7apM0gYdjGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/200b5b3122.mp4?token=ZJnrqbTG8vC2JXRzCtHe73p4AiSXnYHnb9g_vAJ_jPoTb5JPDjG5ItEWTv_dGYLFm3QlfJx5vwpdQcutSUiF8vK_KxMciBlteASbouDZVrHynb_iQ3UEwNZS92yLrIiOwj25T-WiF46BizCCgbARSqOeCYTB4so-Lj3-1EQRueGXJ249x-qqvsJXIn2brTX6rFHYwjlINqkgVauadty0Mc1ypyFAlid3biBtCs_W87ByY4WJJ037ENTocvZ85wPRl3hR0GM88nFpfyXnxOMGr9eDZdnRA3rqbZtulfsUKfx7HlJ2JZVzH_1T5Vdf7odVJo_3OsU-onc7apM0gYdjGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی تحلیلگر ارشد اینترنشنال:
جمهوری اسلامی فهمیده که ممکنه آمریکا و اسرائیل یه حمله شدید انجام بدن و همه مقامات رو ترور کنن.
بعدش مردم بریزن توی خیابون و انقلاب کنن، برای همین از قصد داره معترضین رو توی ملأعام اعدام میکنه که باعث ایجاد ترس بین مردم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69115" target="_blank">📅 14:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c00215915.mp4?token=as4k52XQIE3LLQZIQtWz3TgadDzobtOn8jfnZ3IyHwzEO5IDdMOD2WUWCac6kf7AgzJqgBrik4ai4vqZk6-0ZRqmgu3ZaZ5A1Dnaw56myq6vURu0CMWFQOcM4BT7jop0RQ5QV1lFP2Um0Ny2YAnXUGYxU1aEqE9ep1MmEugSH6roHiJXwsumwZU9Zj9mx1p4QeTSkl-9Ng_5JA9Ur_pwnMywzlCso9ePng7VNjlIT_PmnBKhV38MLJvahUlEX-hknfOp2BfoOZexsM13-HbdhTZL68_f2QA1ieYIb8Gss6hRKRwrL88lPox7h2Tyy8js1S4TkpkRuUQ4W1WT0j1KWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c00215915.mp4?token=as4k52XQIE3LLQZIQtWz3TgadDzobtOn8jfnZ3IyHwzEO5IDdMOD2WUWCac6kf7AgzJqgBrik4ai4vqZk6-0ZRqmgu3ZaZ5A1Dnaw56myq6vURu0CMWFQOcM4BT7jop0RQ5QV1lFP2Um0Ny2YAnXUGYxU1aEqE9ep1MmEugSH6roHiJXwsumwZU9Zj9mx1p4QeTSkl-9Ng_5JA9Ur_pwnMywzlCso9ePng7VNjlIT_PmnBKhV38MLJvahUlEX-hknfOp2BfoOZexsM13-HbdhTZL68_f2QA1ieYIb8Gss6hRKRwrL88lPox7h2Tyy8js1S4TkpkRuUQ4W1WT0j1KWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مهاجرانی، سخنگوی دولت:
تو بنزین سهمیه‌ای فعلا تغییر قیمت نداریم، ولی هر وقت تصمیمی بگیریم، شفاف به مردم اعلام میکنیم و اونا هم همراهی میکنن.
فقط مقدار سهمیه دوم بنزنین (3,000 تومنی) از 70 لیتر به 50 لیتر تبدیل شده که اونم بخاطر حمله دشمن به مخزن انبار نفت‌مونه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69114" target="_blank">📅 14:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=fmJTbvGpIppIh2wL6S8cw6trReHZoytqo37qHXLgpKPFss8wz6dgO-Q1v2fx4Qq-CW-kuKb7WCjvoyIHGeKeNl0ne3OxtISEu47oz6h0jqEt3Wfsshq0qNSAiKe51YfNBnTHTblyK9689AI8WexEjctwBLh0hmXk2zarAn-XKc-Ean3gzHijtxVwx6KLjWyd4inhrfZMfYdgV3mxmKWaRD0fMeQmA4k2cVVw-_pi4Si5L0ahMKal7UOAJMXVUnBQ0j4XwE0rRS6kt4wsPe9nrhbyfpiOrxcNiGJsbnsdhuDa7Gsti-q-DAbG8E_cXKDTh-O0T7c7ikt59tZEqjW3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd184b2451.mp4?token=fmJTbvGpIppIh2wL6S8cw6trReHZoytqo37qHXLgpKPFss8wz6dgO-Q1v2fx4Qq-CW-kuKb7WCjvoyIHGeKeNl0ne3OxtISEu47oz6h0jqEt3Wfsshq0qNSAiKe51YfNBnTHTblyK9689AI8WexEjctwBLh0hmXk2zarAn-XKc-Ean3gzHijtxVwx6KLjWyd4inhrfZMfYdgV3mxmKWaRD0fMeQmA4k2cVVw-_pi4Si5L0ahMKal7UOAJMXVUnBQ0j4XwE0rRS6kt4wsPe9nrhbyfpiOrxcNiGJsbnsdhuDa7Gsti-q-DAbG8E_cXKDTh-O0T7c7ikt59tZEqjW3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
نتانیاهو به دستاوردی رسید که چرچیل نتوانست به آن دست یابد.
او ترامپ را با ما همراه کرد تا به ایران حمله کنیم؛
بدین ترتیب، پیش از وقوع یک «پرل هاربر» دیگر، ایالات متحده را به اقدام نظامی واداشت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69113" target="_blank">📅 13:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=AUo-j3_fHY15PUVPCaeKlhHFyg86nmEPLC-JdA__U4nTueP0jF9zQ_St9tdDOSA4o2lezEzZAQmJMX_RM_3w0hWxfrS04ZA8RfDgpSQUUj5EHorO-YVerM4J9jSmMSLtskC7QUuDxAROf6evJrjMGHAtIOaGgHmmwXk4vaATRWDmstvKuN_L1VpcMpPxP0m1B3sUbidJzoPNGzrab6r5TdA-84_ONXs0tbJPrUMdCJidtsBXSx8dxb9ipQxaQKfYkfVVryvPFHSdkCbY7zQ1KrWOURVTOTE9FiRs2Nv8xdFd6pPa69r3T99yg_mBYOH519gFI3RExR5gGP-RDK5LzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/136b2d25c6.mp4?token=AUo-j3_fHY15PUVPCaeKlhHFyg86nmEPLC-JdA__U4nTueP0jF9zQ_St9tdDOSA4o2lezEzZAQmJMX_RM_3w0hWxfrS04ZA8RfDgpSQUUj5EHorO-YVerM4J9jSmMSLtskC7QUuDxAROf6evJrjMGHAtIOaGgHmmwXk4vaATRWDmstvKuN_L1VpcMpPxP0m1B3sUbidJzoPNGzrab6r5TdA-84_ONXs0tbJPrUMdCJidtsBXSx8dxb9ipQxaQKfYkfVVryvPFHSdkCbY7zQ1KrWOURVTOTE9FiRs2Nv8xdFd6pPa69r3T99yg_mBYOH519gFI3RExR5gGP-RDK5LzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
اسرائیل کاتس، وزیر دفاع اسرائیل:
ما بسیار مشتاقیم که به تأسیسات انرژی ایران حمله کنیم.
ایالات متحده در حال حاضر با این کار موافقت نمی‌کند، زیرا نگران است که ایران به کشورهای همسایه حمله کرده و موجب بروز بحران جهانی نفت شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69112" target="_blank">📅 13:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🇮🇱
کاتس، وزیر دفاع اسرائیل، به شبکه ۱۴:
جنگنده‌های آمریکایی برای انجام حملاتی در ایران از پایگاه‌هایی در اسرائیل به پرواز درمی‌آیند و ایران نیز از این موضوع آگاه است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69111" target="_blank">📅 13:12 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">‼️
❌
آی‌24نیوز:
طی 48ساعت گذشته حدود ۲۰ پهپاد توسط شبه‌نظامیان مورد حمایت جمهوری اسلامی در عراق به سمت اسرائیل، اردن و عربستان سعودی شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69110" target="_blank">📅 12:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=pnhag1tLkzg03XiVicLgjJiwEe4s1W-uexnaerTFjQLJ_v_EkYNGH7pRENOqC8R0AzJgYwzVlFcFchNaYpi7UoO7sGrcl0WiUEuPp5pSpyCOeIbSYtq7RP7fKR8DgbZiTuN8KIFr7k8om1SwnT3TWLQZTJWcer8mNGvdhTVuqsJN7xrOdwb--2r2RkL53OQsV1asSX19_f4mTjTKsthECqFpvnWjyMdqAvvcsZ2yKYofwg6sLcgwWDZcT4V-H__JjFWU4AEYufW-_BWC7LhhjNbG7Hbw71fThFo6KI5hY7tQzcaJynbAOIVygA4u8-5_F9Ak3BZvOBo6ufvQ5bDc2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b2c6cefb08.mp4?token=pnhag1tLkzg03XiVicLgjJiwEe4s1W-uexnaerTFjQLJ_v_EkYNGH7pRENOqC8R0AzJgYwzVlFcFchNaYpi7UoO7sGrcl0WiUEuPp5pSpyCOeIbSYtq7RP7fKR8DgbZiTuN8KIFr7k8om1SwnT3TWLQZTJWcer8mNGvdhTVuqsJN7xrOdwb--2r2RkL53OQsV1asSX19_f4mTjTKsthECqFpvnWjyMdqAvvcsZ2yKYofwg6sLcgwWDZcT4V-H__JjFWU4AEYufW-_BWC7LhhjNbG7Hbw71fThFo6KI5hY7tQzcaJynbAOIVygA4u8-5_F9Ak3BZvOBo6ufvQ5bDc2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇦
گویا زلنسکی هم در آمریکا حضور داره و قراره با ترامپ دیدار داشته باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69109" target="_blank">📅 12:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69107">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SdovdYjRsgpeDsoLV0AfJAJBfx6086MMPucMhm3iRak_88kJ3_-2RVH8r4EzwDQ2hqVg-yYYjsTKstTR-49AWLc5ANn-oIS8AYLKmnVEUzS4XYGAXtIVvw5QCoU18nt1zZ2RtHhfh7eyd9NAAVayJ0ce2Q2sLp3Xlumr1ulcqfXcHZCG5QY0O1sLL62dOJHaL7GIIhEmj9b2zlm7R767E4lOPzUYuwYI-HK-J8Essn9eH2_GIBKjcQ9wn29753svjGA4K_tLBMjjZk3MvFksDoZiF6dnqxnQViod0ItMXpIqzW9ueZlu3yqjZ9Zz35AXSSasWo6POQBo6oNsTNEVdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxdhvbed8Y140ARAxVXUWAggbBUCXJcbHwUmzY4YfHjz9fvk5CSfJ3AxPoumJPwk0qgVlHZCVK77DBTodcAdUu6eR0lWHW2RkrpLS23etCaxpTNVHJFf9yQKKQKVMdGixiWUFqoVWtoTONzYeZBYf7FR94WNoeFyn-u2PMr_Jva6VNpoXHhXvydHr1_rQmsE649NgVI3jfH8QsdZzI-Y-eRD4fo2ycQ2N2-v2TaOyf5uul2KYduysgMOELXfEzxjM_xlZDrVB_EDawEpoh3kZAkda1rFT5_-7KhNKWt6iMkYySW2ZaMQ2IY2own5PY6laMooDuO6IFL8pVhCtTC9Fw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=U9WYdCUdNxax_qYitkh-8buMRtSTLqJNFQUq73Uh5n0avliOIvnivYWjQ0EweeXI1xqlpuIjLGgB0Yd_lTzSrgfMWvBzh3-t9J0PU5067h2_tWCY7qNCKuPJzhLKdbfXH6L9AzNDEMjPkqDBe4frfviA5Nlpfc-_YiZFwXzRyt8npbE1i4LA5ZYaxni1UP8uX8i4_hjMRTQDkpZY5z3Pq2PWE_lKoaP0kKsJav3Ci5G2y0GaNbo0WspqIUNEl_blqUuyHdelEZCQpJTifT9wKrXtPcZpARjVXLyeqZQFAaP7Kf4fdx3F5kO0ZYpB2XWkojXOzbCmNEm-8m2wTH-v8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f0b26c19f.mp4?token=U9WYdCUdNxax_qYitkh-8buMRtSTLqJNFQUq73Uh5n0avliOIvnivYWjQ0EweeXI1xqlpuIjLGgB0Yd_lTzSrgfMWvBzh3-t9J0PU5067h2_tWCY7qNCKuPJzhLKdbfXH6L9AzNDEMjPkqDBe4frfviA5Nlpfc-_YiZFwXzRyt8npbE1i4LA5ZYaxni1UP8uX8i4_hjMRTQDkpZY5z3Pq2PWE_lKoaP0kKsJav3Ci5G2y0GaNbo0WspqIUNEl_blqUuyHdelEZCQpJTifT9wKrXtPcZpARjVXLyeqZQFAaP7Kf4fdx3F5kO0ZYpB2XWkojXOzbCmNEm-8m2wTH-v8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
ساعاتی پیش بی‌بی‌نتانیاهو به واشنگتن رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69106" target="_blank">📅 11:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=dqckBMDZq2kWEQZQgmIzkwxX33WsdvZ5LXgOS4AUJzlBo7SDh8_jxoXZ2D547IZersAhTFHQRVga0R3z9NklfU_TaR5LnQwyVrdB759DKmjRDPLtJ-A_lpVOjJYBK00aB2XdAAtGd0lX9zY6SJtfkpBMsmfCKDy4b2L1rzEj2cELk0oUBNH8m4zc43ZoQA4HFI4WSm-IRDwGJP5Hdb-qgbSTXpzzaNX8umDsrAEeal3xQmPPcKzFsjJogD2rKu3j2S7JkJlK0dps3aEBwoUfdw9jko65q9Uaij7JGD4YmKHK5SekU8mKNMMpar1B7hnCyFqXHu0SiT6sHecGoUvMaHnKrIa1_BxUcRt5Uhh0YYUKkoqcbjrs0j-2b-ZSF8pINbuHtq7w9SBLBQfA413yu5KkqAW10XAUhxWL30hsxu30KW_zrqGqbmD2WtTecHYZ-wQ0cCzbwcQgptHDn1MYYR6grMDrK4ZjH35QihXskRIHVz92_d7mra7p0hoo_PmZUURfO7eWMFd4MJWe_2CWsmXxFyHDQ2v9glCqwpKb0UyF_N-Xz59vUqu9mPGHOV4QWX_WK8TmZOnI-FYh_jiclVqukvas5KFy7VqhDlHEOga7Tk__uWzuh9PObtHC2KFuE6I1TA8KUv8ivCSR-U8wpd-k78o_slY30akWZ2yZzWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=dqckBMDZq2kWEQZQgmIzkwxX33WsdvZ5LXgOS4AUJzlBo7SDh8_jxoXZ2D547IZersAhTFHQRVga0R3z9NklfU_TaR5LnQwyVrdB759DKmjRDPLtJ-A_lpVOjJYBK00aB2XdAAtGd0lX9zY6SJtfkpBMsmfCKDy4b2L1rzEj2cELk0oUBNH8m4zc43ZoQA4HFI4WSm-IRDwGJP5Hdb-qgbSTXpzzaNX8umDsrAEeal3xQmPPcKzFsjJogD2rKu3j2S7JkJlK0dps3aEBwoUfdw9jko65q9Uaij7JGD4YmKHK5SekU8mKNMMpar1B7hnCyFqXHu0SiT6sHecGoUvMaHnKrIa1_BxUcRt5Uhh0YYUKkoqcbjrs0j-2b-ZSF8pINbuHtq7w9SBLBQfA413yu5KkqAW10XAUhxWL30hsxu30KW_zrqGqbmD2WtTecHYZ-wQ0cCzbwcQgptHDn1MYYR6grMDrK4ZjH35QihXskRIHVz92_d7mra7p0hoo_PmZUURfO7eWMFd4MJWe_2CWsmXxFyHDQ2v9glCqwpKb0UyF_N-Xz59vUqu9mPGHOV4QWX_WK8TmZOnI-FYh_jiclVqukvas5KFy7VqhDlHEOga7Tk__uWzuh9PObtHC2KFuE6I1TA8KUv8ivCSR-U8wpd-k78o_slY30akWZ2yZzWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=XvVZa1sGCszs6ktS3JWSQfpJDdB4VFzqRcaOgGuAB-XHXHITN8-PH-gsjMsjxTNPLr2v7lTcDmnWXMkG34lIZ21Ac1jOJur_EBhTyvUEjPbWgZCpTo995ufhHFneQS0FXXYh_OQOA59qE1Roe7qv1pnxtfyJXVxJltqKxntSwnnARRhsF8PvWQkOeTDNvDgUBS84Bc4jO2r3mFyk0HKvKg2sm9I8PHlRpS6vPgWUqaf26tV6gSB2H2FDZ0A5u_97Uf7n1Acu7TCcvC55P6x34wmtDk_WPdv6ohSqs3V2kYflRWt5ZCz-A7ejk8LkiS96u5Bo0GW7TAZ-SeftKPadEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=XvVZa1sGCszs6ktS3JWSQfpJDdB4VFzqRcaOgGuAB-XHXHITN8-PH-gsjMsjxTNPLr2v7lTcDmnWXMkG34lIZ21Ac1jOJur_EBhTyvUEjPbWgZCpTo995ufhHFneQS0FXXYh_OQOA59qE1Roe7qv1pnxtfyJXVxJltqKxntSwnnARRhsF8PvWQkOeTDNvDgUBS84Bc4jO2r3mFyk0HKvKg2sm9I8PHlRpS6vPgWUqaf26tV6gSB2H2FDZ0A5u_97Uf7n1Acu7TCcvC55P6x34wmtDk_WPdv6ohSqs3V2kYflRWt5ZCz-A7ejk8LkiS96u5Bo0GW7TAZ-SeftKPadEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJCm-UIKXv3IRpim4Si3phw8zzKhj1LxyymEU5f3KGHJ49utqdJtliKzMAI56tuzE8JkZ2Wusbd14AeRDVjAfRPvI-PhSTMLPcYXtCF9JxUruWv2n5LXn0sH5CH9KbvkEGWZPCj9yHYEvhAP4ob-tuZ18C5XT7Aevj8PSQ3eou_Yzoz7u_gjP-S9b32UzINkU3PhjpLdwrVRlrUygHgVoF6h3k-QozPc4ru1PFm2s040Gftx8YCjEnOyYejdo3pWhB0rcGea0524a_bBVRjIUmhU-HSvHgmDFM5UEl1DgQE7oi-r5_nIHFSCAkArMfj1IXeU1JA9m8TEqSie7gbVwg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=nYdoeLPpwOfADHCdzvFRN-T293kBrgtZG-sdgrSkcfqSpPOU9MihqIrYzzOaBVxERR-FtQIavDzDmtdc4XcR9VTnLr97vWCmm2XiatRSTBVDEkDRXe8Frmfdppfc_wV8ZS81ky8-0PP4AhG3eCCP3HF5l6WHftI6m2X-yDAudn_SAs8u9lRMSoVTbLh_tc9C-wWJ_ppATYikQDFkMd3OJCwcj2P0gh6pdG7ZqWsjjzdcCk7GBmp21klLxuFh9NkvkWXxC68DI6nCekRVeEQFkaW5d0xdfg_YWhzekMkeD7CPKDYXxM-GYMW9Gw8ESBnbrsvWmSHoLCEObnJc-4G-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=nYdoeLPpwOfADHCdzvFRN-T293kBrgtZG-sdgrSkcfqSpPOU9MihqIrYzzOaBVxERR-FtQIavDzDmtdc4XcR9VTnLr97vWCmm2XiatRSTBVDEkDRXe8Frmfdppfc_wV8ZS81ky8-0PP4AhG3eCCP3HF5l6WHftI6m2X-yDAudn_SAs8u9lRMSoVTbLh_tc9C-wWJ_ppATYikQDFkMd3OJCwcj2P0gh6pdG7ZqWsjjzdcCk7GBmp21klLxuFh9NkvkWXxC68DI6nCekRVeEQFkaW5d0xdfg_YWhzekMkeD7CPKDYXxM-GYMW9Gw8ESBnbrsvWmSHoLCEObnJc-4G-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nHOO1kz0frJs87jN3QH6mFH6mRfT43GZrNkHt6Eh2nNf8btJePXNVlKtuTdajJKWmghbM_33EYEryP2VFU5MsAtaQ5yJe7w_ftuLPyshsaPSB7rf-ci_ZJeglKLLhd9lZ0FX0BCMWXAttMDHL5tXITBzVUbHo5zfQhjZxoy4el-MhzwhSZKFxxA1HsKl2wTDOlNnyGluP2fOyt1WvFf9tNaOMTI7HyUIQ6kU_xfWEJbYDoiaZD6BOrjQui66o4-vH-nwKJ8t4XG9ZH55tH_zDl6rmQeJ1kjkpn06R5VgnOLx0uuEniaDKU9dA1QAifJplqb9TuTiQVgVci2_Hw2-tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D2ZA4-T-j3fE7cNOraUKiAd8YFcY-lovRUmt4DZDSgVbM3caOcGxFUc2LMuct26Jeb0onoigLfEabdoLulrB7Zu_NUhTkLwOwpPgvFJYNM1CmLRPwSuOQ6ZHJLerRfpKmdiJqYiCnFaV2xJ8faBiylgso0rPVMuPK3kmQtUKYIPlEsOlV1xbYnbnkJjcX0uFqgrgbGUO8T9o48Fak7smwEN7LLnFQS5A5iTBw2mGOqjFAD0gAUKRhoMumbUxN_NKZQZN2TzyB71Xf5xACfQ-0jOqJE-37UOdHID8sULuZ6rN5i5_8_QBs_mBSwV2HWprlX-8brKwFhdNn5HPiQJZXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=PciYXh7T9nB-hE6ibJ6j6fAZspyq52Sg2gijbhgdLrXjUklCeioxHOwpkEpeTXKN5MiHZ_eWUQr0MEzukrDMz0qFVWJftx842HR5EcPP2UHxZzs-scsccHfYlmqu4-oVXtFSeXoTvMBPhfYgf3IClFq0t4Gfntd5hX346Sj5PEQI3LxrmwL_tXiBAne10-8HuHAy8VXTnM4Lm1T0NlIk3GCfF1CLuzjufeQR-3B8JM_kINQXudsoh41-kV_Q97jBY4NSxWJnJTJwjMBBUMkSun4P8vXRMTK_e8Hc_PrSAaIZrStQLWFMyf5EC1uNf5TB8jo_H-cnwVrcv82X8YGa5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=PciYXh7T9nB-hE6ibJ6j6fAZspyq52Sg2gijbhgdLrXjUklCeioxHOwpkEpeTXKN5MiHZ_eWUQr0MEzukrDMz0qFVWJftx842HR5EcPP2UHxZzs-scsccHfYlmqu4-oVXtFSeXoTvMBPhfYgf3IClFq0t4Gfntd5hX346Sj5PEQI3LxrmwL_tXiBAne10-8HuHAy8VXTnM4Lm1T0NlIk3GCfF1CLuzjufeQR-3B8JM_kINQXudsoh41-kV_Q97jBY4NSxWJnJTJwjMBBUMkSun4P8vXRMTK_e8Hc_PrSAaIZrStQLWFMyf5EC1uNf5TB8jo_H-cnwVrcv82X8YGa5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=qtkJ70zS9RcFCFtwQrdNQjvHxWyxNV50vJLtnXnBtVXN6k0KHBwrCjsRvFpqmk1qwKMTzBBZ-taJA96-kIwb6zgmXUkb5ytVdI5U9xFln7jDx1tXm1enMTg-HMXN1kyoLqUYhMef_lYMjjuKjXOaMmUOY4EId4UKXdoiTkMc1egj_Vglaov6HnS5FFFuHaFg-LTw6OyVDKVHWC4hlu4QYfF3-dNepDoMgV770eklTahQYdCIxkSnSNdOFATI4sgB5y0-blcrBPxbnEzhAYWx_OHmwu-_7JDYk1uwMBpqisnqX1yQQ7XgWJ7B0vrubET2V10mwbHPkEgcFfd0oHOTlw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=qtkJ70zS9RcFCFtwQrdNQjvHxWyxNV50vJLtnXnBtVXN6k0KHBwrCjsRvFpqmk1qwKMTzBBZ-taJA96-kIwb6zgmXUkb5ytVdI5U9xFln7jDx1tXm1enMTg-HMXN1kyoLqUYhMef_lYMjjuKjXOaMmUOY4EId4UKXdoiTkMc1egj_Vglaov6HnS5FFFuHaFg-LTw6OyVDKVHWC4hlu4QYfF3-dNepDoMgV770eklTahQYdCIxkSnSNdOFATI4sgB5y0-blcrBPxbnEzhAYWx_OHmwu-_7JDYk1uwMBpqisnqX1yQQ7XgWJ7B0vrubET2V10mwbHPkEgcFfd0oHOTlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N8HUzbh0kuMxToscqI6ifNN7Kk8q_w-SPp83pLBP1Hj_bLs09tRPEOGOMidNhC4J4jIKQ10iNwhAn-HH8KmK5wqnrLTWBhqNUbB1iepmi4Gf_lWtQ0ygBmae3m8UTmtowEgqKRPjqiWTAWoAULSWHbKgck0RjgACRa4yKqjsKg_Shc_pPRBy_vld5koe_ZhSFFRTJ6o_plbamOvk2aICAgHfyjSYw8kJhtxC-HdsAUZvB6S1PhKmJP9wvF9eq5LsvGr6-8cjVK1K4lBhRe4ySBVYHJWeSvPyKjVcIdCJMpuyGvBOHqRKkpxVFepmE2iZzSFqKUKtS4eARKTBFcQjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZfVLJe1_jVyeEgqmVgKrYIM7vsXVtlzJButd_CafUiaID2_nKpdGTfFqigoQ3TEJz9VnRBxAA9Vics865szeGfqIDQwymFT9tcxbZWxSOt3FbNK-3F-9f8z0vTrt-eHAVIDJl1SNOlPkt5Bcud2qUOwnhN2UV5G6vjd0LoarzyXAubRBgZBVaZPng5xa-rgUiR64toBti9mPjWLSQwcqFFKzXefi66HCa12bGU5lq1Bpx7E9wxNFDJpeDTHDzfLFPjm1JKqgyGaTeF3RwgbEm5xlj6G91QWGU2ip_ijRxRBrXjnXxVsyTWVd6VGJ2xfgmnYSg6y3P59ta4RGCFC2KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n43s-I_fTp8yJOhRhry0QQBce9dMbOcn1GSJLvguNcGHr324LR1dTBBMTyatorNIRoGMZQzH71TvNClsbtoLCTUJZTGDS7mYrY0IiAWBqvYOAxCRtd1rJoDr3WEM6giqUeouZsGmDS3wsf4_fxSS8aN8x_vR9V5szv6Glm_GxJ6HKH2w9jekRz1kHWX3a3qDmFGoofqme_yfdE43PAhjTmvIZFLihtr4UQjGMJF9QKcJQF_Q_c4x3QuNnNapJa9NunH7gCqwof_jVv9cL4S0qO3vKdpu_m3qGPayzr7NOI7Ue2vwBDHvFHLy_4dvJCrdEJbKGHlJpxGOcI7NkkzViA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=A6fplk7BRZnNVXppX7NDvCXyHL0ixIdGemlu1kXQNuwxOi2nBBx9cp8EWR-0SbzGLK_DYj2Uw9KkUUn9-ipjEV1drfKQr8FrxjvYnQzqmwtNDKhSF1IXzgFxpuW5tN0g0AcHp4RLPowEyB36s95L58FoJzXtqJS9zAE1xRyeNDeBKtB1X98keNpfqy4Z1TpmHwu-nE7K7RX6KHd3w5diCb2FYH_uVYpdfumXN4uJmHtnfyD8ovfLIIe4DDUbfdmpy-rn5KOy2IVYc4AogtDyeAVqWdEnMSJFi-53Je18B9Gc_lWLovdOh0lSDVDUpEyi154yAlmU6eiAol5ykZs40w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=A6fplk7BRZnNVXppX7NDvCXyHL0ixIdGemlu1kXQNuwxOi2nBBx9cp8EWR-0SbzGLK_DYj2Uw9KkUUn9-ipjEV1drfKQr8FrxjvYnQzqmwtNDKhSF1IXzgFxpuW5tN0g0AcHp4RLPowEyB36s95L58FoJzXtqJS9zAE1xRyeNDeBKtB1X98keNpfqy4Z1TpmHwu-nE7K7RX6KHd3w5diCb2FYH_uVYpdfumXN4uJmHtnfyD8ovfLIIe4DDUbfdmpy-rn5KOy2IVYc4AogtDyeAVqWdEnMSJFi-53Je18B9Gc_lWLovdOh0lSDVDUpEyi154yAlmU6eiAol5ykZs40w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=go1FwD6fyZQR7aMkE8yC5ghmrw9-xPR5A2NepGm2XZEe32Uykt6cm5WOoMIUEn1TETtCylXIbhgXUyVqGJLuDnCl8s0-PXWYY_JgbBxn21J7sFT8IRMLoXIcMmRezsOvXy4XOVVVFvmzAMBMSJKuC2vnZNu0B8ek75pubt6Q0ZlzaLRvR3roH0aiU35iHXHrxTUXsm3KzG9pQNef8zHWpV_ziRc6uI8VayC4LAqqWSORVo2PgEm1XaF_xK7FbSPy6l5qD7wmQ6TSGV_RKd38psUa_kYQQllK8XvZssLSQmrRnHUOWaSpwCqRkZ0zWZ5I5tU-vG0ro7Qt7NeF2aGkHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=go1FwD6fyZQR7aMkE8yC5ghmrw9-xPR5A2NepGm2XZEe32Uykt6cm5WOoMIUEn1TETtCylXIbhgXUyVqGJLuDnCl8s0-PXWYY_JgbBxn21J7sFT8IRMLoXIcMmRezsOvXy4XOVVVFvmzAMBMSJKuC2vnZNu0B8ek75pubt6Q0ZlzaLRvR3roH0aiU35iHXHrxTUXsm3KzG9pQNef8zHWpV_ziRc6uI8VayC4LAqqWSORVo2PgEm1XaF_xK7FbSPy6l5qD7wmQ6TSGV_RKd38psUa_kYQQllK8XvZssLSQmrRnHUOWaSpwCqRkZ0zWZ5I5tU-vG0ro7Qt7NeF2aGkHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Z6S-R7tlW5-jxUlIjKhvoc5zYsoupF-mJJAhtjLs6Jfs9g4CRp-9V7YvkM-L2UGSRi5S5XchsFTL9RVD76RpEyyJpk5EmfoY30_hixndGYzswAWfVguDeKS26dHIvZ4IJulR8xqb8wzFswhEl-kvwExFzDA5jiTDdZ2ARHDgEIEMMwUupVIuCn8qGakgy8Mi7pL-FDK_uu2tV3LBDVnMSdYwyuYwukBz_PaACS4dpljpV63o3AXmvsoJYb4XgeOz5xsvPoMLeMeR90w0nKPqCA7Qdf0yXEm4dgmYtqzwOQrUW6KP7hr9H_0k8XD8j7kWiBoLle--hRaFUtcXzfY72w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=Z6S-R7tlW5-jxUlIjKhvoc5zYsoupF-mJJAhtjLs6Jfs9g4CRp-9V7YvkM-L2UGSRi5S5XchsFTL9RVD76RpEyyJpk5EmfoY30_hixndGYzswAWfVguDeKS26dHIvZ4IJulR8xqb8wzFswhEl-kvwExFzDA5jiTDdZ2ARHDgEIEMMwUupVIuCn8qGakgy8Mi7pL-FDK_uu2tV3LBDVnMSdYwyuYwukBz_PaACS4dpljpV63o3AXmvsoJYb4XgeOz5xsvPoMLeMeR90w0nKPqCA7Qdf0yXEm4dgmYtqzwOQrUW6KP7hr9H_0k8XD8j7kWiBoLle--hRaFUtcXzfY72w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDbMgEd3HV-6mENdOU_aX3tu6yu0QiDTCbxpKxLJyQISUGsyfhz17pRjICuTNVFAzyE53FrBcVUJvzx2EzalLQtpHiQEZmLdbomJIlmuH9r-pbJUr5ADHI2COm2UjgDJkSAy8Wx8ncGWdOBmXlkztiU3hgX-8UGLu4JDurqBU8OF0NzfipB8oTY1slGYkemfx0coZuPlkMl0n4tan5zl8M0e8-chaN4-ObSokX6IdKGfnpH1jEIiy1VjKkLuFC4DURttRi6LV3ghBS_bzBILTh5yaaOvhqukyYygJr_ISahiDkC3xUt2w30zs2YZ15R3vE_N6B2di3agHn2K6AbvSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LDgFR3dSLUpSi41gtl1DYUfb-6NCYGNdblOnIxt8T8QZ2LPquEoXLtoLxX1gArQ1PvNbaGaYIeB25lLmBOPVzTT04NijHOlGWZ9xPf2Tb5GVWXFP9bMB9cVfWs4zbIU2G3EfZmFUYDQbEiBe_6jugbYN9xyU2WgGkpRZflQKHp4ivVrqV5FUsU38xncEB8acrAUtKCbtZzxeqKMZXNz0HiklOwFZnJXdW4t0TNqBqazORSNgIVEUpg9imYgBOBnErvTETBHI-LIwJtYjw12s0X1Hu2VyOsUheUMwzxqnJqYG13Vv89bn2jkcfmSgPcu7eqzo8Pl242C6x7raUJ0FMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ynh6AyxnC9BEiSC9mOoS-cOgkMqMVH9M9She8SMlgkKMtN7RpWDAc-Fi1x2yUK0pNw3bUGKkpL1fENo3tWQWAiuwc-gD914GBZ-5MlZ5rYLRbpDQc03F2hYhwLzI4TW_zVG00i98Oco4kb4edmZia6UWRbC-5qwyenzsYWVznDCHSGrPu5QUb40n3IWn9A5ckQqK7hreWCUN8cCi6qU2nRanS3RHedg3u6oq95qWjfq2P6wMFsrk3Oc-iP9jfHqH4im78Ac6t_y4ByTyPA9cjmnfhazIeLqLIwqoMZrrot6AVOviw_PelzZCIgczGZC8FKTVnkGqkEe_1WD6O50ujw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=KGacDimmBzp32nhKPVr7V-5bENDSTuB79RYnBT2umpqUKAHuPyo4qZIydwMjYsBGSFcnxZK4c686Ma33nuyfG3b5BxXQVEIq4OcCpxED_6Asfzhk5iKcMqcGTS1Zz5Pr699SeVqHLsxjAuXDm9x6yDR1jkJJWyZ3r0aT_fEHFYmexscJgk4Jhugw941HShBpyK7mENyVXhT53U5TTQWG3lWUm9M37WLIpOewuIjHws6h0cDZd8WdicjSyB8n9uuqtj5VNtHv1HohX6CcseiWmu--QDIcGdGL1sxcEYTbBcJtKn3OTA_LJ73kv13QFQMTbENN28yBnx54cG6lEBHJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=KGacDimmBzp32nhKPVr7V-5bENDSTuB79RYnBT2umpqUKAHuPyo4qZIydwMjYsBGSFcnxZK4c686Ma33nuyfG3b5BxXQVEIq4OcCpxED_6Asfzhk5iKcMqcGTS1Zz5Pr699SeVqHLsxjAuXDm9x6yDR1jkJJWyZ3r0aT_fEHFYmexscJgk4Jhugw941HShBpyK7mENyVXhT53U5TTQWG3lWUm9M37WLIpOewuIjHws6h0cDZd8WdicjSyB8n9uuqtj5VNtHv1HohX6CcseiWmu--QDIcGdGL1sxcEYTbBcJtKn3OTA_LJ73kv13QFQMTbENN28yBnx54cG6lEBHJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrLAGCitZVZwRTDFfc8LAuIl8vOJZIhtWQ6yvDZfE4yytB4KBRXN0bw_CWJHk8UrbocFAwh_5BVk-DnA22HCCJFeSuwHICqen1wutslwOqVuqbWmlR0C8or_hgPXrbI7p0TfNW4wyL5c48UoCOKFhJjdvK_JldxZLGiqKeQmwAXvtUMpjqdfgNpjZoDKiFxGcrpityMofn6mldur2Q-xbX0iEP6F2MjCe9ol1nVqsHJXEJV8IX8HpqhX7_1xH_3w1QIcXJs4ZgzrWjf1HsYsoZA-ICJSeiqhOozHiNpzsOmz73agOccdrP4qISiw5F75SsyvO_bjJl4_MZegjtPfOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=s2jpdYfnmp4oo6FLDapHx556Rdv5u8kpfdwPgPVUALbvRM5hj8zwJILAbkYYStrH7hYodlfwWjPz4UugZckCKNbI-CP5pgVX-Z1JblvJag31YZEdN4yHMgTArtIVTX14lgK8NKOsqkBIZ_0oXSjBrF1if-LmBnCuef5zAZieuoZWzf4t7CntwJvpnO3JDmu2XEwM-4W6y1WLa2Fy9LFHO_51lEnJoMoajaifGOlCJR7708B7w0yQiTWIcDiev0iDaI1a3zEnjkUSytslXyamiTnxkHXeU95XXcxE2-8qsDZFLzfz3qlAASRSFUcy_NXcVlN1euQyfl_WFt7UMKhR4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=s2jpdYfnmp4oo6FLDapHx556Rdv5u8kpfdwPgPVUALbvRM5hj8zwJILAbkYYStrH7hYodlfwWjPz4UugZckCKNbI-CP5pgVX-Z1JblvJag31YZEdN4yHMgTArtIVTX14lgK8NKOsqkBIZ_0oXSjBrF1if-LmBnCuef5zAZieuoZWzf4t7CntwJvpnO3JDmu2XEwM-4W6y1WLa2Fy9LFHO_51lEnJoMoajaifGOlCJR7708B7w0yQiTWIcDiev0iDaI1a3zEnjkUSytslXyamiTnxkHXeU95XXcxE2-8qsDZFLzfz3qlAASRSFUcy_NXcVlN1euQyfl_WFt7UMKhR4TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cofojm8Hql4JexjN49JIBSDE9J74mcv91vl5JDf-PcXFXsgxx7kX2r9-ec9hzCaHV4kG3MqFl3x5He5b4UjAXHvrFRJ7ZKujv3gnKll6GaOWE4bSeksm-SsJreT8sscY2uO2jSxKWo6DWa67OeJCtPuDkbeD3vk1fo9MwerG509nZDXwv_oOKTXrKVYFqUpGKeD1E4nXUuFNffK6Km4j0JHT8Z4iUb7ceijFiDEuXQGo2X6radLEXIiQVWvVN2yBLFrIOyO6onf0iC9ikoNhKSyO_F9wiW7KrdzAYJqJV4IH3Hiqsj_ZUO1YjBVNpwe7ij1EQ5c9ktmJ9TatY4RnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=TSl6B-zPBX6Ld4WA3yqE3OLav5eYKy3S4Z6eX8rI2Sy0CE9A0FW4u7Wf9nNiuKluvk5gC1IRwVKF7rlKumVQL1JaP_E0zImAxOCIlH3K69k5Y16rX7mDIdftCAPuYNQIb8MabsNp0uQic-lorWcU0PlE_6JDhkXEwbPtYvTyToL1HHQhOeV1rPuf7cnZAZsFD5hVc8MDd0AgplU2ii9Csdd9KOTJGU9DdXN9GEhtLJVPAGHaQXbit6eiUzaPb7-HdFxjgcpCBN4a4RgoSkdnGp_ajlwKHA5lGq2TmE7f1NWETqGUfQOnX7QWlJWC9wtAkdZanU5hysNo7JxhcAuQ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=TSl6B-zPBX6Ld4WA3yqE3OLav5eYKy3S4Z6eX8rI2Sy0CE9A0FW4u7Wf9nNiuKluvk5gC1IRwVKF7rlKumVQL1JaP_E0zImAxOCIlH3K69k5Y16rX7mDIdftCAPuYNQIb8MabsNp0uQic-lorWcU0PlE_6JDhkXEwbPtYvTyToL1HHQhOeV1rPuf7cnZAZsFD5hVc8MDd0AgplU2ii9Csdd9KOTJGU9DdXN9GEhtLJVPAGHaQXbit6eiUzaPb7-HdFxjgcpCBN4a4RgoSkdnGp_ajlwKHA5lGq2TmE7f1NWETqGUfQOnX7QWlJWC9wtAkdZanU5hysNo7JxhcAuQ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7Yb8lHhZJh_6XNyN0rcenD9VeA2cFzp-Qiv5pmV6-eywThaPgjtS0NEjNNeD3du34XMypWoREIZP9H8_9g9gRSC2GWWS7DxT7uohyc7wZXJF0_cWJxPuNFd93i_bO6UHYm6lha0nspzv1zoSlrD42P2DXv3SRQVeRAm9NdapJ60ytzYGLHo4-c0IHMG7tVRBc8frZRpBxYf4yzuw_f8QxxQnJI_RY8zeNBsQyvuamhjqETJV8afNModXBrUDQd4MmNPLC0g5cNUR-2u0NcZmsGRvTUMRorM_F0pGPhNjzCy6WvVkMWniQv18JKXLgqBmqLyZLAAQxKdAkpks7WFfx0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=ZnBe7sYYlaYL3cnGvxMRD8BM-9uDGxZUcetz8iW9ePml55gN2nqs2GE4eZckM54lTgAwUkODzHAKWfC6ii-YWqdDz191ZtWFhPeFBPW_S6o0xwRMcnwQVsNHRHznMUGUeuCBdsQhc7sXL6MpARJZIyH54zvyKN4Lc1DHGhMyj5qRZEsQjm1QOPT83x6zilY5s_hr8UBPQY6Y6-KvALUhaKB8YT6o6dCOp4IsoYZ5Fqp58buZAyAx9VqKWrp0h0uY8GBtofi2GTRZcczOviM9XkpTOABlMiZhALmNrzYSmlBDKct106ERnJCbehdD7kz0W8cs1-rydiscQnqH0XQB7Yb8lHhZJh_6XNyN0rcenD9VeA2cFzp-Qiv5pmV6-eywThaPgjtS0NEjNNeD3du34XMypWoREIZP9H8_9g9gRSC2GWWS7DxT7uohyc7wZXJF0_cWJxPuNFd93i_bO6UHYm6lha0nspzv1zoSlrD42P2DXv3SRQVeRAm9NdapJ60ytzYGLHo4-c0IHMG7tVRBc8frZRpBxYf4yzuw_f8QxxQnJI_RY8zeNBsQyvuamhjqETJV8afNModXBrUDQd4MmNPLC0g5cNUR-2u0NcZmsGRvTUMRorM_F0pGPhNjzCy6WvVkMWniQv18JKXLgqBmqLyZLAAQxKdAkpks7WFfx0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=fwJzgXPA4zznO7g6PQNJ7cbxcQZygXFOX-Ztk2jmlNoSeUEhjzTdH3-tjRM9rEqAB4r8W2ckSGMs7l13hEkaX1u6F7tsMO2yff4NeQnjP9ohDqLnqvz_yFy--x-awf626qDtCKVDiEtGgoiO5E9ZICWOSK1yCkhBgGlzzyhyOYKb20ArZAAlC7C3q1KY3dPFdhSeXUakm75ioB-yYEzAGe7gJxJGLJwWsk6snfM1fhI-vz4HUpZsbEBngwJZ2NtxY_EXaRuU6dXZt7bn9vHWxt0FEeh1OkWIniF37ASS4hFp3T3ckxak5TrFa-ZomOEaEveO0V_NZDSFICnVZZjjXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=fwJzgXPA4zznO7g6PQNJ7cbxcQZygXFOX-Ztk2jmlNoSeUEhjzTdH3-tjRM9rEqAB4r8W2ckSGMs7l13hEkaX1u6F7tsMO2yff4NeQnjP9ohDqLnqvz_yFy--x-awf626qDtCKVDiEtGgoiO5E9ZICWOSK1yCkhBgGlzzyhyOYKb20ArZAAlC7C3q1KY3dPFdhSeXUakm75ioB-yYEzAGe7gJxJGLJwWsk6snfM1fhI-vz4HUpZsbEBngwJZ2NtxY_EXaRuU6dXZt7bn9vHWxt0FEeh1OkWIniF37ASS4hFp3T3ckxak5TrFa-ZomOEaEveO0V_NZDSFICnVZZjjXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=DmJsKSCA-MIx5LzBPCN4U4YPbtwTK3AnB4umEj3PtF4fync2BVDTorVywFb_4XQg14iODBLFP931-QlbSar8dJdihCeOCfRgGv-nRlDr68sP1J-OVZMlFHjrEAQt1OrjDucApfUD8pMzim7jWXnhs98yHIQqmd3Tc-kxywqQjdF70DaayTNb1JM-DVee1-PE-Wks45IQ8Kbul0v823RG17YCAE800hm-tFDIKmNRFF6IuKmchFIj5BnKPZyBBM2L61P4SwHpc-ShO9WNjJZPPzhzx-VyA9RmvH8kHbZhzG0xRTwhLKEv1QnP_NGZs0YPjzwuY7k9tME17hAxz8_ACw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=DmJsKSCA-MIx5LzBPCN4U4YPbtwTK3AnB4umEj3PtF4fync2BVDTorVywFb_4XQg14iODBLFP931-QlbSar8dJdihCeOCfRgGv-nRlDr68sP1J-OVZMlFHjrEAQt1OrjDucApfUD8pMzim7jWXnhs98yHIQqmd3Tc-kxywqQjdF70DaayTNb1JM-DVee1-PE-Wks45IQ8Kbul0v823RG17YCAE800hm-tFDIKmNRFF6IuKmchFIj5BnKPZyBBM2L61P4SwHpc-ShO9WNjJZPPzhzx-VyA9RmvH8kHbZhzG0xRTwhLKEv1QnP_NGZs0YPjzwuY7k9tME17hAxz8_ACw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
