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
<img src="https://cdn4.telesco.pe/file/M6Ie8xSixTc1Aw5onol_Ny4Z6LVAEz6I9lsFxDZW1crsh6AIbX2GeYg89_7fUnrEH4d4IxftbhAVwj8w6QxW8TMVhwiIzyMbsEr06YSKMGkEfqBOe3OzO_xzBlHHFxxbzh67hZB_BzsdAvYRGnxV9AAqa0shOW40QcSmz0Mp1fPK6iRyX09ctWIXIx0W_wkFlV_YIeIFZ9QysLDwBIhSxAmMI5yRE2HzeE6Ir7swtADjiFbvywEfk1twvbybh8ukKTyQm0X8cB6fW-KCOeE6Ap6dgeu1RMfbVj8hUF-gY7w_RgV0_jokmfsm5LhEkFtFCRkR1547hEOU4NV1HqsWFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 925K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 17:00:45</div>
<hr>

<div class="tg-post" id="msg-132259">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
دبیرکل ناتو: بدون اروپا، آمریکا نمی‌توانست به ایران حمله کند
🔴
رومانی بزرگترین فرودگاه‌های تجاری خود را بست تا به هواپیما‌های آمریکایی اجازه برخاست و فرود دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/alonews/132259" target="_blank">📅 16:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132258">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca40d53017.mp4?token=D5IQI91O1YRwTEn-gynQdIqrctG7yVRIRxWzRuhdyaDAQNsdouG6bCkwcKtZHSRP4xmt4P38gK7ElwmkylZLFXUDuo97U9qWXV5QmPh1GrkA9Gpi9vYnO7EuWi6xlBKVyQNyrjaa5w88DVj3nK4IogRRVdcmurm-YtLHFmGV3UlP-ExP4H1NRH9s_1V06kuL5EtkrnHi-UQJ5fTwTii6T3sDlEJpOguihcEo6Emt4SqTNsj9EH7pksGfpB3thyQ9yv3EbeBbBcPxbOF51kQXLzugT3eh7ZmssulmP5tt44tZtFz_n-7OOs9Tfn02oMoSd4vERtfS-h6y0H0HOg2cNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca40d53017.mp4?token=D5IQI91O1YRwTEn-gynQdIqrctG7yVRIRxWzRuhdyaDAQNsdouG6bCkwcKtZHSRP4xmt4P38gK7ElwmkylZLFXUDuo97U9qWXV5QmPh1GrkA9Gpi9vYnO7EuWi6xlBKVyQNyrjaa5w88DVj3nK4IogRRVdcmurm-YtLHFmGV3UlP-ExP4H1NRH9s_1V06kuL5EtkrnHi-UQJ5fTwTii6T3sDlEJpOguihcEo6Emt4SqTNsj9EH7pksGfpB3thyQ9yv3EbeBbBcPxbOF51kQXLzugT3eh7ZmssulmP5tt44tZtFz_n-7OOs9Tfn02oMoSd4vERtfS-h6y0H0HOg2cNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره کیر استارمر: به نظر می‌رسد نخست‌وزیر بریتانیا دیگر در آنجا حضور ندارد، شاید به دلیل ایران.
🔴
آنچه او انجام داد، بسیار ناخوشایند بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/alonews/132258" target="_blank">📅 16:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132257">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
ترامپ، درباره روسیه و اوکراین: هم پوتین و هم زلنسکی می‌خواهند به توافقی برسند. متاسفانه، این اتفاق خیلی دیر افتاده است.
🔴
به نظر من، اتفاقی خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/132257" target="_blank">📅 16:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132256">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cb42c6a06.mp4?token=I4DBKLRvowNeDy62_dLcAis5B6EYQ3dnDOILI3eKesOsM6678ACaz6vtnK4MIbMQaiod87N5MkjUR1s-4I11c8-33yrY_ZgPYWvUVm4dNgechAVjah8ixuqy7rIJujdDiHMn5FelePFbrEMtZPrdmOTIa6c0ln4JbUxhZI3QrG8i1cyuugwfPCE2bytoGe7oB9r2pLnxLJXVK18_gloXt9TVd6A7xxPSn6eHmP4XTHDg3cBI4pGrE3AKdhkpJy9YGhW9kV83nO3sn3a-rya-zpuxgdYBR_C7hHM0B1RbO99ugCGdEpJLE8BQpYqCJJ3WPGtuFea8HZW8akhrbBmN3626nnK1jFZNfzTsrBAB2GZLUtRV8EBxeksP372iAP3s6UnK6UoUxrbLrLpMSkx3fiRFUqLrWpmworgfirQENrcpE5auZsuZCZOkdMi5729EZrHcsGfVbmAMaXY2rFepI3xNbAorYCXy8wB32k1o1hHNgOaza_ITU9UFAgTWSWPYthv62hjDmGCiqZ1w6trBzjtdcji2hEHa9G4ntt-CjMOrj8H9zwlVaJOg8EYr8Idr2YbEk6l9ZJh5M9ttB8NjEW29CkUnetMqvw91G3RHk0ll4Coy6lQyN5k-sfD3wQsQIFeAYWC0u4d2Sv5Ll7-BMiySnzHwDf7LUS9cPh_xSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cb42c6a06.mp4?token=I4DBKLRvowNeDy62_dLcAis5B6EYQ3dnDOILI3eKesOsM6678ACaz6vtnK4MIbMQaiod87N5MkjUR1s-4I11c8-33yrY_ZgPYWvUVm4dNgechAVjah8ixuqy7rIJujdDiHMn5FelePFbrEMtZPrdmOTIa6c0ln4JbUxhZI3QrG8i1cyuugwfPCE2bytoGe7oB9r2pLnxLJXVK18_gloXt9TVd6A7xxPSn6eHmP4XTHDg3cBI4pGrE3AKdhkpJy9YGhW9kV83nO3sn3a-rya-zpuxgdYBR_C7hHM0B1RbO99ugCGdEpJLE8BQpYqCJJ3WPGtuFea8HZW8akhrbBmN3626nnK1jFZNfzTsrBAB2GZLUtRV8EBxeksP372iAP3s6UnK6UoUxrbLrLpMSkx3fiRFUqLrWpmworgfirQENrcpE5auZsuZCZOkdMi5729EZrHcsGfVbmAMaXY2rFepI3xNbAorYCXy8wB32k1o1hHNgOaza_ITU9UFAgTWSWPYthv62hjDmGCiqZ1w6trBzjtdcji2hEHa9G4ntt-CjMOrj8H9zwlVaJOg8EYr8Idr2YbEk6l9ZJh5M9ttB8NjEW29CkUnetMqvw91G3RHk0ll4Coy6lQyN5k-sfD3wQsQIFeAYWC0u4d2Sv5Ll7-BMiySnzHwDf7LUS9cPh_xSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: می‌توانید توضیح دهید که منظورتان از پست دیروز در شبکه اجتماعی "تروث سوشال" در مورد نخست‌وزیر ملونی و "دستور منع" چه بود؟
🔴
ترامپ: خب، نمی‌دانم. فکر می‌کنم او شخص خوبی است، در واقع. اوضاع کمی بد شد، زیرا او حاضر نشد به ما در مورد تنگه هرمز کمک کند، یا می‌توان گفت که او حاضر نشد درگیر مسائل مربوط به ایران شود.
🔴
بنابراین، این موضوع کمی رابطه من را با او تیره کرد. اما من از او خوشم می‌آید. فکر می‌کنم او شخص خوبی است، در واقع. اما فکر می‌کنم او اشتباهی مرتکب شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/alonews/132256" target="_blank">📅 16:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132255">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNKzoG6XNQaMIRsmeoH8xgN9bwW3jghN0KQhU8k-6cawFAtjcf1V2JhFK7NtiB56TwtW_cWFlRi_Tl1aX00eaoKH9Uzo8UhOJTTtnnAb2HpuIQnLcfNjEUoEtfm4dMi8-CmBfASXmStyxLwjZfhDxrhdkXN7UYsKfCO-82mWPi-YFyRPSEH7mFcgfYihgvsf63cQr9CAO1_kBFxeU-OqKU4IVLaOFxV7wbNKVAcPB4MrDpc__fQhSP-yS_JK0h7ITX9AK24EnH6Kc-1y-rhEmhAhrPC6c4fqn9U69Ol0Wr5VmIvT4-9iVulpHQxEVnn3XHgMYkPUfTddr-eeGoRUkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: ایران شب گذشته به دو کشتی تجاری که درحال عبور از تنگه هرمز بودند، شلیک کرده است
🔴
این حمله تلفات جانی نداشته است ولی کشتی‌ها خسارت قابل توجهی دیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/132255" target="_blank">📅 16:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132254">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
ترامپ:  گرینلند باید تحت کنترل آمریکا باشد، نه دانمارک، و ما ممکن است تمام نیروهای خود را از اروپا خارج کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/alonews/132254" target="_blank">📅 16:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132253">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
ترامپ : ما نمیخوایم دوستانمون رو تحریم کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/132253" target="_blank">📅 16:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132252">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ:  ما به تنگه هرمز نیازی نداریم چون مقدار بسیار زیادی نفت داریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/132252" target="_blank">📅 16:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132251">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: ترکیه همواره یک متحد بزرگ برای ما بوده است.
🔴
آنها ایران را به خوبی می‌شناسند. و من شنیده‌ام که برخی افراد درباره روابط آنها با اسرائیل صحبت می‌کنند. آنها می‌توانستند در این درگیری از طرف دیگر وارد شوند. آنها یک کشور نظامی بسیار قدرتمند هستند، اما این کار را نکردند.
🔴
شاید آنها این کار را نکردند به خاطر من.
🔴
آنها کشوری هستند که بسیار، بسیار خوب عمل کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/132251" target="_blank">📅 16:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132250">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
ترامپ: به لطف رئیس جمهور اردوغان، روابط ما با رئیس جمهور سوریه بسیار خوب است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/132250" target="_blank">📅 16:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132249">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
ترامپ:  من جلوی هشت جنگ را گرفتم و معتقدم که جنگ نهم را هم تمام خواهم کرد و امیدوارم به زودی به جنگ اوکراین هم پایان دهیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/132249" target="_blank">📅 16:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132248">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
ترامپ: ترکیه به خاطر من درگیر جنگ با ایران نشد و نمی‌خواهد شاهد دستیابی ایران به سلاح هسته‌ای باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132248" target="_blank">📅 16:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132247">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e08920f4.mp4?token=CmSFcJVLHPmjZ7okTaur7xIRcTknSIk-vsaLbSnSmodlEsJr-OESuZGRVox1J6XFjCgcxpmbZlETM1vOMbfwjEawW-TqevDCcBrK2V8GMyM1CUEJvGL7jDG3k7y9MQNE0j6T-EdU7pNR_5GvGCbI6cIB181Vjprls2twXwEaFufk8JKQwrJi2jZk1jwQsPZMaxAwn5W7iq7dD-QXTm--vJSAbEkPc77X1bQ2U2FQ6SrCi32VPHeoC5z0LkJBXkVZPqyHNYupSc8j0a7oUMHsvCIBF5qR22xcWD24eFl_BYT6TQS9W-_RFIl7r538tyaSJy0O16mAYKdmmKUN2FcqOmpBJc6JZGjvL1bqG9s5Vyd8utiIb6cGw5CdBB-j-nBMUHCAgM0QjsnZDZCFO5OTAnWyO3f7c9KYHDvKAxUcQXKn5QLALVfya8vGQuHT3DKhhny_lFWgkWjjzi8yBaSOXhiM8-ceqlb5X-WTcMt3C0vwjstPJeOzR4WhLaiAnYHT8NdjXXj8l22WxeZdtED0BtT0KxhGJKyMWcULezFAl_glR59zfu_-45j-Ims0o3DQzGptiaN6UpyHr4O30zkdjgv0bpiwrhnW2hK8ZUGaglMvVrQhKQMI-YNHurd85sP3Venyzd1u2-3MOyaksOnkDC0zYIDJipfMVepXd-RnCrM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e08920f4.mp4?token=CmSFcJVLHPmjZ7okTaur7xIRcTknSIk-vsaLbSnSmodlEsJr-OESuZGRVox1J6XFjCgcxpmbZlETM1vOMbfwjEawW-TqevDCcBrK2V8GMyM1CUEJvGL7jDG3k7y9MQNE0j6T-EdU7pNR_5GvGCbI6cIB181Vjprls2twXwEaFufk8JKQwrJi2jZk1jwQsPZMaxAwn5W7iq7dD-QXTm--vJSAbEkPc77X1bQ2U2FQ6SrCi32VPHeoC5z0LkJBXkVZPqyHNYupSc8j0a7oUMHsvCIBF5qR22xcWD24eFl_BYT6TQS9W-_RFIl7r538tyaSJy0O16mAYKdmmKUN2FcqOmpBJc6JZGjvL1bqG9s5Vyd8utiIb6cGw5CdBB-j-nBMUHCAgM0QjsnZDZCFO5OTAnWyO3f7c9KYHDvKAxUcQXKn5QLALVfya8vGQuHT3DKhhny_lFWgkWjjzi8yBaSOXhiM8-ceqlb5X-WTcMt3C0vwjstPJeOzR4WhLaiAnYHT8NdjXXj8l22WxeZdtED0BtT0KxhGJKyMWcULezFAl_glR59zfu_-45j-Ims0o3DQzGptiaN6UpyHr4O30zkdjgv0bpiwrhnW2hK8ZUGaglMvVrQhKQMI-YNHurd85sP3Venyzd1u2-3MOyaksOnkDC0zYIDJipfMVepXd-RnCrM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ :  ترکیه هواپیما از آمریکا خریداری کرده است.
🔴
وقتی یک کشور هواپیمایی را از آمریکا می‌خرد، اگر نیاز به تعمیرات موتور باشد، به نظر من ما موظف هستیم که تعمیرات موتورها را انجام دهیم و به آن‌ها در انجام این تعمیرات کمک کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132247" target="_blank">📅 16:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132246">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزارت خارجه قطر: ایران از نظر قانونی مسئول حمله به نفتکش ما و خسارات ناشی از آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/132246" target="_blank">📅 16:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132245">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ترامپ درباره ترکیه: به نظر من، روابط ما با ترکیه در حال حاضر بهتر از هر زمان دیگری در گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132245" target="_blank">📅 16:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132244">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe9b46a70a.mp4?token=Mwf3EPp_DaXCfTgF75Fm7HKlxbtZ7uHodlIJ6yhUyFXBvWMQSe9RXk1IIUQsi15U8301nQLRmMtyS78oOpezvZ2urNKgwBE5TFt9t8z5TJZaJIf-YtuyYJXPKhXqD-rUuIgJ1WJKYNk5HWU2FmdpYFf7qq_peCUnAvf3jAqmZZJ9mm0rnaEdIzGG8UFrIHMYcfjh7M1HIoGkdCnLLAX8rQrU0yq5SK_bC4fnYeFwR6I4uR9w-y8sawQXKp08vIecgxCtpOptefNTOyL5hiJlUrqbwLh-XDni2UdQqM8eKNPydHsxKQbgOyeC29Ia-LjYsRq99L8yTTumjlREGIBfpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe9b46a70a.mp4?token=Mwf3EPp_DaXCfTgF75Fm7HKlxbtZ7uHodlIJ6yhUyFXBvWMQSe9RXk1IIUQsi15U8301nQLRmMtyS78oOpezvZ2urNKgwBE5TFt9t8z5TJZaJIf-YtuyYJXPKhXqD-rUuIgJ1WJKYNk5HWU2FmdpYFf7qq_peCUnAvf3jAqmZZJ9mm0rnaEdIzGG8UFrIHMYcfjh7M1HIoGkdCnLLAX8rQrU0yq5SK_bC4fnYeFwR6I4uR9w-y8sawQXKp08vIecgxCtpOptefNTOyL5hiJlUrqbwLh-XDni2UdQqM8eKNPydHsxKQbgOyeC29Ia-LjYsRq99L8yTTumjlREGIBfpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: نگرانی‌هایی در مورد سامان‌های دفاع هوایی S-400 روسیه که ترکیه خریداری کرده است، وجود دارد. آیا شما هم این نگرانی‌ها را دارید؟
🔴
ترامپ: من در مورد هیچ چیز نگرانی ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132244" target="_blank">📅 16:32 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132243">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
اردوغان، رئیس‌جمهور ترکیه، درباره هواپیماهای جنگنده F-35:
ما تعهدی برای دریافت پنج فروند از این هواپیما داشتیم و آقای ترامپ نیز در این مورد قول داده بود.
🔴
آقای ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه F-35، یک تصمیم مثبت اتخاذ خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/132243" target="_blank">📅 16:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132242">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae38c41f38.mp4?token=b68tJs0FjuInjG3Rx27qt63rx8wwfEvkSSJZA9BEz8nBQsx-iavbVtJMM1FFwbAklteTib21DZRiHPOllxVDI0m_j8uRXS0Uk7060PkwAuA7LjCryRuU_5pn2oRH2qmLlh689fky-IaAf55qTrs0TyUaT1wjrMT7vfcWQt9Nze8svjYmWQhrtXZb6-L-jkdE_wr1iMnyoBtROkzh-cYJta1GzVYGu2FCUEusVM_Rwe3iKYJSc1owKnjvo_GMJ6qSSn8anuZ7ho2VChdYZuxk4X2yE6SLI0LRMfKFhGOLxlmyJMMDVkhmQpXlJmNb6Li3TcH5DYQWYx4REiObFRVbfL2iqujGF2HN51CdnJU-jt4QR7sYpVnq_gjLYSPtQ021QEg_5GhT9U_lBXpMNjZR12rDfpjq1zgl5vvP0jK7u8VgHaE-1V0pL-zgmEYzCuMpfFZqHLJ6M4Fq22n9Lxn7c3pA5JFfqNDmPu3ViKHBmEMxSzd6vqU_19l5q-TEowPJbOetMm-Ri8aUgE4XU2JxiugGb5QV7ZO1Y3Rs0S_nBNDO2vtCCtVX4A7fcXTX6Tpw-pnqshlrpq-8XdnLgTQMYfwrzaY2UE1zWjWy2RE6Us9z99esrPfWlBCTr4RSRTIbYh806gtmsXrX-etwOxJ0rvBQKsTje0RM49wGfq4sWDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae38c41f38.mp4?token=b68tJs0FjuInjG3Rx27qt63rx8wwfEvkSSJZA9BEz8nBQsx-iavbVtJMM1FFwbAklteTib21DZRiHPOllxVDI0m_j8uRXS0Uk7060PkwAuA7LjCryRuU_5pn2oRH2qmLlh689fky-IaAf55qTrs0TyUaT1wjrMT7vfcWQt9Nze8svjYmWQhrtXZb6-L-jkdE_wr1iMnyoBtROkzh-cYJta1GzVYGu2FCUEusVM_Rwe3iKYJSc1owKnjvo_GMJ6qSSn8anuZ7ho2VChdYZuxk4X2yE6SLI0LRMfKFhGOLxlmyJMMDVkhmQpXlJmNb6Li3TcH5DYQWYx4REiObFRVbfL2iqujGF2HN51CdnJU-jt4QR7sYpVnq_gjLYSPtQ021QEg_5GhT9U_lBXpMNjZR12rDfpjq1zgl5vvP0jK7u8VgHaE-1V0pL-zgmEYzCuMpfFZqHLJ6M4Fq22n9Lxn7c3pA5JFfqNDmPu3ViKHBmEMxSzd6vqU_19l5q-TEowPJbOetMm-Ri8aUgE4XU2JxiugGb5QV7ZO1Y3Rs0S_nBNDO2vtCCtVX4A7fcXTX6Tpw-pnqshlrpq-8XdnLgTQMYfwrzaY2UE1zWjWy2RE6Us9z99esrPfWlBCTr4RSRTIbYh806gtmsXrX-etwOxJ0rvBQKsTje0RM49wGfq4sWDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره رابطه خود با اردوغان:
بعضی از افراد را دوست دارید و با آن‌ها کنار می‌آیید. و بعضی از افراد را دوست ندارید و با آن‌ها کنار نمی‌آیید.
🔴
گاهی اوقات با سخت‌ترین افراد، مثل او، کنار می‌آیید. و گاهی اوقات با ضعیف‌ترین و حقیرترین افراد، کنار نمی‌آیید.
🔴
اما از روزی که با هم ملاقات کردیم، رابطه خوبی با هم داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/132242" target="_blank">📅 16:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132241">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ : کاری که تو ایران انجام دادیم، اصلاً به کمک هیچ‌کس احتیاج نداشت
🔴
حتی خودم هم کمکی نمی‌خواستم. البته قبل از اینکه برم، گفتن کنارمون هستن
🔴
ما هم تریلیون‌ها دلار خرج ناتو کردیم؛ برای چی
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/132241" target="_blank">📅 16:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132240">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e5dddb6c8.mp4?token=U4jHeZ_QfrA79KHDSbRLGYe6K0r2kRsjqKydGYHUO8ehTfdds4Aqk3DBOTbeUkakt09slJC4kz65IrPfxW_Mqd7FKatysdvmZuTtMuLseAGWQA-3EUW0tdsXwLQyPVwFCzX70MFD6LIbczfdFcRbjFdgGgDUnl3lKcwPy_QHmOVLljtopzyjwi1F9ZSbIjqzVLc3R6HwqsbmHSM9OUB3fM8C3j2AkRpnwA5Ehb7yv_cFF6xC_w-SjQ9zilqMqIYX8t3_G17tWgYghGDWu_7mds5seJIzbVlTm3KuY6902g8dJniGD5jnDSGfuvtjTD5PxoCGUd6KiMKEd0xSFXNG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e5dddb6c8.mp4?token=U4jHeZ_QfrA79KHDSbRLGYe6K0r2kRsjqKydGYHUO8ehTfdds4Aqk3DBOTbeUkakt09slJC4kz65IrPfxW_Mqd7FKatysdvmZuTtMuLseAGWQA-3EUW0tdsXwLQyPVwFCzX70MFD6LIbczfdFcRbjFdgGgDUnl3lKcwPy_QHmOVLljtopzyjwi1F9ZSbIjqzVLc3R6HwqsbmHSM9OUB3fM8C3j2AkRpnwA5Ehb7yv_cFF6xC_w-SjQ9zilqMqIYX8t3_G17tWgYghGDWu_7mds5seJIzbVlTm3KuY6902g8dJniGD5jnDSGfuvtjTD5PxoCGUd6KiMKEd0xSFXNG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آقای رئیس جمهور، آیا قصد دارید جنگنده‌های اف-۳۵ را به ترکیه بفروشید و محدودیت‌های قانونی آن چه می‌شود؟
🔴
ترامپ: ما قرار است تصمیمی بگیریم. فکر می‌کنم خیلی‌ها - می‌توانم بگویم، خیلی از افرادی که همین جا نشسته‌اند - بگویند چرا این کار را نکنیم؟
🔴
ما رابطه بهتری با ترکیه داریم و ترکیه از بسیاری جهات بسیار وفادارتر از سایر کشورهایی بوده است که فکر می‌کنیم وفادار خواهند بود.
🔴
و مطمئناً چیزی است که ما در نظر خواهیم گرفت - بله
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/132240" target="_blank">📅 16:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132239">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
ترامپ: من از ناتو بسیار ناامید شدم و در اجلاس شرکت کردم زیرا در ترکیه برگزار شد، به پاس قدردانی از اردوغان
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132239" target="_blank">📅 16:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132238">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c86a1c1f7.mp4?token=RsJ76TrIArz7hChTy3d-WU4foUEC-7XZF0_jWVsyPDfaRj8CpOeIrI0ujKxymLuityT8PjxxeMFn9cVqH1XZ5ZMg0nxISzirkBNS0C3IiKbajbXl4ScuFwGoFvGF7ShpMhlPAZfQXxnMldTyqJ-d_5rBj780ala0RGId9zUp2mvJV6KZGHHWr4tPVTPUdofDnK98F7_gMuv3YY4VuS746cl3uFw3Q6oZ0mX0J7isAtgdd0kI4huw0FTEA2KYX82l8wH8qodtyvT8oJaBzv3n8Ejc7FqF3aDJA7x5o5yJWL6ijEVsykkl3MGIsFGvIL_l_oAb7GSnvnnDMW1mFPXcaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c86a1c1f7.mp4?token=RsJ76TrIArz7hChTy3d-WU4foUEC-7XZF0_jWVsyPDfaRj8CpOeIrI0ujKxymLuityT8PjxxeMFn9cVqH1XZ5ZMg0nxISzirkBNS0C3IiKbajbXl4ScuFwGoFvGF7ShpMhlPAZfQXxnMldTyqJ-d_5rBj780ala0RGId9zUp2mvJV6KZGHHWr4tPVTPUdofDnK98F7_gMuv3YY4VuS746cl3uFw3Q6oZ0mX0J7isAtgdd0kI4huw0FTEA2KYX82l8wH8qodtyvT8oJaBzv3n8Ejc7FqF3aDJA7x5o5yJWL6ijEVsykkl3MGIsFGvIL_l_oAb7GSnvnnDMW1mFPXcaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به اردوغان: ما امروز درباره تجارت صحبت خواهیم کرد. ما درباره چیزهای دیگری که مربوط به ارتش است، چیزهای مختلف زیادی صحبت خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132238" target="_blank">📅 16:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132237">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
ترامپ: ترکیه تحت رهبری اردوغان به یک قدرت نظامی بسیار قدرتمند تبدیل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132237" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132236">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
ترامپ به زبان ترکی خطاب به گارد ریاست‌جمهوری
:
مرحبا عسکر!
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132236" target="_blank">📅 16:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132235">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
ترامپ: ما تصمیم فروش جنگنده‌های اف-۳۵ به ترکیه را خواهیم گرفت و روابط ما با آنکارا بهتر است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/132235" target="_blank">📅 16:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132234">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزارت خارجه قطر: از ایران می‌خواهیم فورا به همه اقداماتی که امنیت منطقه را تضعیف می‌کند، پایان دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/132234" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132233">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
ترامپ: ما توانایی‌های نظامی ایران را نابود کرده‌ایم و تهران به سلاح هسته‌ای دست نخواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/132233" target="_blank">📅 16:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132232">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🔴
فوری / رویترز: نفتکش حامل گاز قطر که در تنگه هرمز هدف قرار گرفته، به دلیل آتش‌سوزی در اتاق موتور، در معرض انفجار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/alonews/132232" target="_blank">📅 16:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132231">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
آلن ایر: ایران در حال نهادینه کردن کنترل خود بر تنگه هرمز است
🔴
دیپلمات و سخنگوی سابق فارسی زبان وزارت امورخارجه آمریکا: برای تهران، مساله اورانیوم می‌تواند منتظر بماند اما تحکیم موقعیت در هرمز هرگز.
🔴
ایران می‌خواهد بر هرمز کنترل داشته باشد و در حال مذاکره برای نهادینه کردن این کنترل است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/132231" target="_blank">📅 16:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132230">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
لاوروف: امیدواریم مذاکرات، وضعیت تنگه هرمز را به قبل از جنگ بازگرداند
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/alonews/132230" target="_blank">📅 15:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132229">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ادارات قم فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/alonews/132229" target="_blank">📅 15:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132228">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
شورای شهر ایلام با رای قاطع، شهردار را عزل و معاون وی را به‌عنوان سرپرست شهرداری منصوب کرد.
🔴
شهردار ایلام چند روز قبل توسط دستگاه امنیتی و با دستور قضایی بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/132228" target="_blank">📅 15:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132227">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
زلنسکی: فردا درباره سامانه‌های پدافند هوایی با ترامپ گفت‌وگو خواهم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/alonews/132227" target="_blank">📅 15:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132226">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
به گزارش واشنگتن‌پست، ارتش بریتانیا اعلام کرد یک نفتکش هنگام عبور از تنگه هرمز پس از اصابت یک پرتابه دچار آتش‌سوزی شده است؛ با این حال، مقامات آمریکا و ایران تاکنون این حادثه را به‌صورت علنی تأیید نکرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/132226" target="_blank">📅 15:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132225">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/726b340c7a.mp4?token=n9MSv7_IO0dPhFjjB89WUeM81xsRC4sy1KzDVMBAgiwARC81UNgeCwiFwdo6iXng102AxK4kRdcoVm0aVxZ22PcGjJyuuaZ1jMRTVN9LRciKyz4N1Rd1OBSMD_Nh_HLldxUxwNGFOT8HJeZHS3CpJLphSN0qO_Lt3p2vHmYKDfqrQJo_zt1Mg1NIeU5ixdHxV09i20LwUrHQeVVnVr-urQiBB9gaaGr3o0gtvc6z9-hgGUCKzWc8lAhzUjuZj2S9yjtoj4E1hyUlxi4UaYKi9dIUZ_BPWlcqmxEuujyyOVCmLPGYacuvy1ffPO4L0TdpSm0RjKSI1_p1PbV2pYDcKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/726b340c7a.mp4?token=n9MSv7_IO0dPhFjjB89WUeM81xsRC4sy1KzDVMBAgiwARC81UNgeCwiFwdo6iXng102AxK4kRdcoVm0aVxZ22PcGjJyuuaZ1jMRTVN9LRciKyz4N1Rd1OBSMD_Nh_HLldxUxwNGFOT8HJeZHS3CpJLphSN0qO_Lt3p2vHmYKDfqrQJo_zt1Mg1NIeU5ixdHxV09i20LwUrHQeVVnVr-urQiBB9gaaGr3o0gtvc6z9-hgGUCKzWc8lAhzUjuZj2S9yjtoj4E1hyUlxi4UaYKi9dIUZ_BPWlcqmxEuujyyOVCmLPGYacuvy1ffPO4L0TdpSm0RjKSI1_p1PbV2pYDcKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پرتاب سنگ به سوی وزیر امورخارجه ، عراقچی که با چند متر اختلاف به ماشین کنار وی میخوره
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/132225" target="_blank">📅 15:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pgIvM4Bw0oG6DtkSLCDKT41ShwcAhD4bWmhVhfa_UzOi_l6c-irEK363jBbZuaj2h08-DycjaxS3Up1_A5FeLwerqhCvdOukFw1jZtYgt8bUjziBNjfdYRX_NqL9Dh2MGIUZ3bN5DUkzlNM1q6WVyA7mJRt8zjwKlMxk9wlzD4WJPwLFR6SiMUwLKQGntmnxqu0ythY9IYKTUoriWKIZuQbi1A3UtEP79wWNqa6VCHXgnEfA1JY6e4HqZdd2q_HNQ9GSHM57rwSAux7ZIdsVSvfzdJRW7FMC4aVms0q62t8OhDhi_gaEjuE5rJ7DqL0EIsUvw-eexxGLWMoU_INflA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S-zd9oX_T23knC8lLBlLzshYrC3VrjkE5ByYiJT3D5Xhtv0GYaFmyxVHyXFDy8qstjg-J0LjOvrWj3SYLhYEaJ_7wVwny12KWcWIgo41R91Pz6qRnngCDc4m48s-qjZIVPAarc_fEhHvExeE5_oaKDP2naK60cKfS5oImVv906rCns2WeG59aLIRQI5YtEe9lAU6sxW_fFqtz5ZezJhduJOSfVQtcA6Mz2WqXh8jnG4ZoyP4U2d6kqvCVc4NTfd2uvgIq42hoaeU2rC0FHrQKr-dCuxE_G8JZvScPUAiijw6iX-VVS8d1RXzjDaY1rjb6jjBWc12_CAXE-V4uZYecg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عکس های جدیدی که از دیدار
ترامپ
و
اردوغان
منتشر شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/132223" target="_blank">📅 15:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
زلنسکی تو نشست ناتو در آنکارا : الان ماهی حدود ۳۰ هزار نیروی روسیه رو از بین می‌بریم
🔴
فقط تو ماه ژوئن، نزدیک ۲۸ هزار نیروی روسیه کشته شدن و برای تک‌تکشون هم مدرک ویدیویی داریم
🔴
بیشترشون هم با پهپاد هدف قرار گرفتن. راستش، اصلاً به این موضوع افتخار نمی‌کنیم، هیچ افتخاری نداره
🔴
اینا رو می‌گیم که نشون بدیم جنگ واقعاً چه شکلیه؛ جنگی که ما شروعش نکردیم، ولی مجبوریم توش بجنگیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/132222" target="_blank">📅 15:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etBrfTwT7QuaUOUyenyqO5nQ7WrvvLdbIZyfYUZF25LH8LaXW3LEp0h5VBLU4xqMJu3lJQ5VTaIu5cc8_usfMHvrMNJrN8zDuyOIguOYdKPoeap60wAHEYbb45mqlbG2HHuxCnRL3yOzdusnskbB54CccQkkiQIkxPV9817-ONgzq5rSN6FzlOfyvvp2Ac0DkqlazCKqsTbclC4Rue6QEP7j4DfqLTidOyR5fhzcKW9yZDWp9r1cVyMoOq6Z_EIjpP2r8YtBuhP27182DClHEp3LUw97cWi8h92ZSUUAESVwEyqeL6TGHvvFaFABAIXThXH9tK4H_bpa8v_qCfF2XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / خبرگزاری CBS: علیرضا فغانی قضاوت فینال جام جهانی 2026 را برعهده خواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132221" target="_blank">📅 15:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ به آنکارا برای اجلاس ناتو وارد شد و توسط رئیس‌جمهور ترکیه، اردوغان، در باند فرودگاه مورد استقبال قرار گرفت.
🔴
به نظر می‌رسد ترامپ بسیار خوشحال است که اردوغان را ملاقات می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/132220" target="_blank">📅 14:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eO3-X8BOlxeS22GG4UFkzBYnQsU3zypa4EftwA_vucNyMvCSiEj5AFwR3S0E2jDVzGz1faEiwC2E7WN-naLor2vFepKo5rOX0tDoBiNACX3KIi-eZMMNP_c1xxTncjEOVLtvmxh8L0UaQpx-D-9D8AnknkFNsKY_PnOMNVOHQOp8NslTgS-lgw9cXErVDj-IT31y2WS4Fs13VJmyqbDytk7V3e609RQgVPUQ4VwSI9fj_Ca7OMsZ-dS2iNRCHfdt6u1r_TzoY934-xxOssN3ZZvRDqjxgx0e0edv2Qc59EqA6ywDmh8t5dJw2a8J48s8CidKG7iKkWfPpm0aG3VzHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویرماهواره ای دیروز نشان میدهد ناوگروه باکسر وارد خاورمیانه نشده و حتی در دریای عرب نیز حضور ندارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132219" target="_blank">📅 14:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
تلویزیون العربی به نقل از منابع: لبنان با انتقال مذاکرات با اسرائیل به رم مخالفت کرده و بر حفظ گفت‌و‌گو‌ها در واشنگتن پا فشاری دارد
🔴
منابع دیپلماتیک می‌گویند لبنان با انتقال مذاکرات با اسرائیل به رم مخالفت کرده است. هیأت لبنانی به طرف آمریکایی اطلاع داده که بر حفظ مذاکرات در واشنگتن پافشاری دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132218" target="_blank">📅 14:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132217">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
وزارت خارجه سعودی حمله تروریستی به دمشق را به‌شدت محکوم کرد و بار دیگر مخالفت کامل خود با هرگونه اقدامی که امنیت و ثبات سوریه را هدف قرار دهد، اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132217" target="_blank">📅 14:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132216">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
وزیر خارجه آلمان: ایران باید آزادی تردد کشتی‌ها در تنگه هرمز را تضمین کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/132216" target="_blank">📅 14:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132215">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
عربستان سعودی در حال مذاکره برای ایجاد کریدورهای جایگزین حمل‌ونقل نفت از هرمز
🔴
خبرگزاری رویترز: عربستان سعودی برای ایجاد کریدورهای جایگزین حمل‌ونقل نفت، وارد مذاکرات اولیه با همسایگان منطقه‌ای شده است و عملاً به دنبال کاهش وابستگی پادشاهی به تنگه هرمز است.
🔴
این مذاکرات در مراحل اولیه با هدف دور زدن این گلوگاه استراتژیک که در طول جنگ آمریکا و اسرائیل علیه ایران با محاصره دریایی و حملات دریایی مواجه بوده است، انجام می‌شود.
🔴
پروژه زیرساختی پیشنهادی به گونه‌ای طراحی شده است که یک گذرگاه امن برای صادرات انرژی خلیج فارس فراهم کند و تضمین کند که جریان‌های حیاتی نفت از نوسانات مداوم منطقه‌ای مصون می‌مانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/132215" target="_blank">📅 14:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e076c481d.mp4?token=dCuQoriKNslEcJv6U1DEwkdHPEohce9ODS9c_f3eeS1jPNi_QXItnhcCax1NUsU1PCBVBbj7LITJzUFrXdqS-qD2So65k4ZQN6NLYWDCRitGsnE6xja53AQiNziKRRm587ZwkQsdj1-0QJgB9Xv-tvBpHK9T1k28Socq0gXyEKa4UeNTt1F74G5wv7DoA6itRMIDdmUT1Bsl6lOneN9oiAmyVpnm9OCFZOrrGTdr5JJQYhz5pX_L5KBvqHfUV4D1AhMZGGHHwK4rfqbc2IP3cBFZv8H3igrYNydPA19-BgVgxjD4OoV0bxsDA-tKAjvH7m2MkNLFoCHK77gos__dH52HtAGPfKEeZt-VgmzOQGM-s5UZGM8CdoA5VMwywdr9rio1TVAjx4Rj4fJaeIPAD3LkN_XOkn7pv9IP0Hy5uRC_o2Hh6k0oFcyaEF54fsaQFiO2o5E_DYJ5T-fHn3AB6h_qEVW7fSOMCRG3KY_PyhN6YeiyQ14-fgdydPOtcj9Dz5PnJfH0Y-bR0oUTlqc6164JUMggs8oBJgiFzCKSgjAr7LfdFAFSi1YP-yC-aNAsbi7zvbjj82_wFBPDPSIVT9HVj_9VQVs7JRwl3lrlZSElxp3TU32BxqPnIahOMRznZ87ubz5yOqx-HMYnHUQLfA4vf5JKGrGYEjsWT7ISjm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e076c481d.mp4?token=dCuQoriKNslEcJv6U1DEwkdHPEohce9ODS9c_f3eeS1jPNi_QXItnhcCax1NUsU1PCBVBbj7LITJzUFrXdqS-qD2So65k4ZQN6NLYWDCRitGsnE6xja53AQiNziKRRm587ZwkQsdj1-0QJgB9Xv-tvBpHK9T1k28Socq0gXyEKa4UeNTt1F74G5wv7DoA6itRMIDdmUT1Bsl6lOneN9oiAmyVpnm9OCFZOrrGTdr5JJQYhz5pX_L5KBvqHfUV4D1AhMZGGHHwK4rfqbc2IP3cBFZv8H3igrYNydPA19-BgVgxjD4OoV0bxsDA-tKAjvH7m2MkNLFoCHK77gos__dH52HtAGPfKEeZt-VgmzOQGM-s5UZGM8CdoA5VMwywdr9rio1TVAjx4Rj4fJaeIPAD3LkN_XOkn7pv9IP0Hy5uRC_o2Hh6k0oFcyaEF54fsaQFiO2o5E_DYJ5T-fHn3AB6h_qEVW7fSOMCRG3KY_PyhN6YeiyQ14-fgdydPOtcj9Dz5PnJfH0Y-bR0oUTlqc6164JUMggs8oBJgiFzCKSgjAr7LfdFAFSi1YP-yC-aNAsbi7zvbjj82_wFBPDPSIVT9HVj_9VQVs7JRwl3lrlZSElxp3TU32BxqPnIahOMRznZ87ubz5yOqx-HMYnHUQLfA4vf5JKGrGYEjsWT7ISjm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین دیشب به ۸ نفتکشِ تحت تحریمِ متعلق به «ناوگان سایه» روسیه در دریای آزوف حمله کرد
🔴
این بخشی از فشار اوکراین به بخش انرژی روسیه‌ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132214" target="_blank">📅 14:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=qnoWHhU_KQFOS4bUKj8m5_9MFITVUIKa--ZB00lhHtT2SUS_nCJM58thZJRNkfpfudCwxuM78oqUQkI3DqcPxu7sb_lDmNPD6N0G6Msoz2ewOdR_cNSXVD-2F6edRPio7gR3nhsIv6Gl0GzLyIbw4BdhCAZh_QwIY8FCXvBWGTHn5w3hFmy3yQ84PbJrUaSXKNlP6I1ZphbwHJmW2rCXI1LIsLFwcsxmsxMJhduWwwd7tpF1fmZMghoZBHq7oOIRyRn6BMcs8nAE0C013mYQwhZoA9nNcoBdclUuQY0xADr7BDGum6YefPxk6-vLQoYzqpyP9_hs8_JLjHieOUJJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc22eef9fd.mp4?token=qnoWHhU_KQFOS4bUKj8m5_9MFITVUIKa--ZB00lhHtT2SUS_nCJM58thZJRNkfpfudCwxuM78oqUQkI3DqcPxu7sb_lDmNPD6N0G6Msoz2ewOdR_cNSXVD-2F6edRPio7gR3nhsIv6Gl0GzLyIbw4BdhCAZh_QwIY8FCXvBWGTHn5w3hFmy3yQ84PbJrUaSXKNlP6I1ZphbwHJmW2rCXI1LIsLFwcsxmsxMJhduWwwd7tpF1fmZMghoZBHq7oOIRyRn6BMcs8nAE0C013mYQwhZoA9nNcoBdclUuQY0xADr7BDGum6YefPxk6-vLQoYzqpyP9_hs8_JLjHieOUJJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ به آنکارا، ترکیه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/132213" target="_blank">📅 14:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
شریعتمداری: سر ترامپ را می خواهیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/132212" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
تعطیلی ادارات سیستان و بلوچستان در روز چهارشنبه 17 تیرماه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/132211" target="_blank">📅 13:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مازندران فردا تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/132210" target="_blank">📅 13:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر خارجه آلمان : حزب‌الله ریشه همه مشکلات لبنانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/132209" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
مدیرکل فرودگاه‌های استان بوشهرگفت: فرودگاه بوشهر پس از نزدیک به چهار ماه وقفه، فعالیت خود را از روز شنبه ۲۰ تیرماه با برقراری پرواز در مسیر تهران - بوشهر و بالعکس از سر می‌گیرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/132208" target="_blank">📅 13:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
مکرون، رئیس جمهور فرانسه :
اتفاقات تنگه هرمز باعث شده
🔴
فرصت خوبی برای پیدا کردن و استفاده از مسیرهای جایگزین به وجود بیاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/132207" target="_blank">📅 13:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ایتامار بن‌گویر، وزیر امنیت ملی اسرائیل، درباره فعالان شرکت‌کننده در کاروان‌های امدادی به غزه: آن‌ها می‌خواستند من ساندویچ به دست آن تروریست‌ها، آن حامیان تروریسم، بدهم و به آن‌ها بگویم که اسرائیل چقدر زیباست. اما این با من تمام می‌شود. من فریب‌کار نیستم.
🔴
من مربا، شکلات، گوشت گوسفند، میز پینگ‌پنگ، تلویزیون و رادیو را از آن‌ها گرفتم.
🔴
قبلاً آن‌ها چاق می‌آمدند؛ امروز چاق می‌آیند و لاغر می‌روند.
🔴
این‌گونه باید تروریست‌ها رفتار کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/132206" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrrFUwtf_JfgsXPmkjG6epcrQmkv0MVef_NZr-9VN1isyUJJAKXaM0sgDBHbBm2Dh0WQh5fx51PAUs_cJqCDyZnQnkdjoGmiwQrrEvr7Y02do96W5KPkLFr-jWbM7KPA3U5ju0zhQSZyJMW8yUa80Cwqj_Z6gwAJ2Dq7jbZ4QJhr3SaS4yn47L8H7Muvm56BQfR5P2O4hGK3MyJhzyJkktHVERIpxqZ5OIidjEtKDArza5-7aZx9XN4ZlKLj2Jpeto7_NAoVzcxbIPn9KO9ka35jKnVy1BzF1Vr24psIALWV_8_VZRJeWcmKub3BsjNeu_VxhDnXYyRM0a7BvuN7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصاویری از بازیابی کلاهک ۴۵۰ AGM-158 JASSM کیلوگرمی و عمل نکرده موشک کروز هواپایه در استان کردستان منتشر شده است
🔴
این سومین بار است که کلاهک قدرتمند و نفوذ کننده WDU-42/B به صورت کاملاً سالم به دست می‌آید
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/132205" target="_blank">📅 13:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e9c082164.mp4?token=pyeZVG5ffxOJNtGWN23KEd8sE9XRQNczofeWxWl8e38fcCAvUENOfI1H0WeAnF7WdqgexD0sTBha2vhFManuTUouSVQeekreawjPbCmw1MXH5DFKAP4k5PLwTMKLBjh4daZk43kKm4jQRdR2qZuBG1sIWv84kXqnhmpzsi-qr4DkzSDVtJql25IChrR-OhMwxuLbeVtSfGE_itZMMbZog5tpVBE6wjPK1Px_-sFHi1s0HG1amj3mW6zfXn6GdZu-6Y50tjF7QEbq5QwQkVLezP-fqVd9y-HOcORrGpZ4a7dWj4bTVFRqgbT-uOLdZajRJ_1McFryLfIH-S7NiQZ0zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e9c082164.mp4?token=pyeZVG5ffxOJNtGWN23KEd8sE9XRQNczofeWxWl8e38fcCAvUENOfI1H0WeAnF7WdqgexD0sTBha2vhFManuTUouSVQeekreawjPbCmw1MXH5DFKAP4k5PLwTMKLBjh4daZk43kKm4jQRdR2qZuBG1sIWv84kXqnhmpzsi-qr4DkzSDVtJql25IChrR-OhMwxuLbeVtSfGE_itZMMbZog5tpVBE6wjPK1Px_-sFHi1s0HG1amj3mW6zfXn6GdZu-6Y50tjF7QEbq5QwQkVLezP-fqVd9y-HOcORrGpZ4a7dWj4bTVFRqgbT-uOLdZajRJ_1McFryLfIH-S7NiQZ0zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره ای رویترز از مراسم تشییع
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/alonews/132204" target="_blank">📅 13:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCiFGVeGxOyIB9niAzP8jflLhXzyQh3if0WCkggmrxOPZdz8Uoto2X7-BzMosxuXWaZABkA1n4akqnw5V-6nMrAidMHbfrXQR7Y654rQQEvPNUm3UlbaZvMMitlDjVM3GYhJg9dO6VlqnJEFPW3v8blBXjdVlgjLCViF8JVs-MlDbtdAJwzRuGdLuHSI_Tbp5QOORTFSYr_sGh91YgiZCcuF80NCFLwIgEDIe2o1rprS4P2qROa2e6_LnXY0VPBa7qdQnbEStRvw-e68cuYzPqtLXPPG-TZITZeE8FCuk3yOBdvhGl2AKi6rQv2jLPe7kMb_FlVOY3l1m0bgEmgaPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار مکرون و الشرع سران فرانسه و سوریه در کاخ ریاست جمهوری سوریه در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/132203" target="_blank">📅 13:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
گزارش ها از کندی سرعت اینترنت
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/132202" target="_blank">📅 13:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
صداوسیما: جزئیات جدید از حادثه برای یک نفتکش در نزدیکی عمان
🔴
به گفته برخی منابع، نفتکش «الرقایات» متعلق به قطر، قصد داشت با حمایت نیروی دریایی آمریکا از مسیر عمانی در تنگۀ هرمز عبور کند، که پس از بی‌توجهی به هشدارهای مکرر، هدف حمله قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/132201" target="_blank">📅 13:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
به گزارش بلومبرگ، پالایشگاه‌های دولتی هند در حال مذاکره با تاجران نفت خام ایران هستند و در صورت تمدید معافیت‌های آمریکا پس از ماه اوت یا کاهش محدودیت‌ها، برای خرید نفت ایران آماده می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/132200" target="_blank">📅 13:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97ce01c0c.mp4?token=Q6vh1gaHV9RGK-DT6jGN08sjuKb3iYp963beF9500dVyzhcXXk_mm_jK07CaBSna56BjfDhUEqPioMoLOIEdmHjR5rLwMRtRpjeXDytGNuBn68u6K_j0bYCnEOaJRqC3kJrk4CJ0aM0iMiMvs4CQShBvyvhIafv0P0CdbFQksBVQYYKnVgScqXWwG_V4gN1-eh1EqgGok-jgT_Wbj5_eihka1Pwf8wGuR9N-LUKqhBFJYr4PI05tWQrHdC2SZSabXlK_846v9INyn5q2B3sdSxnnHzAepkTp6LT2xbIzOvZBpWdkhZsOJFyXxltQeC-jbdKXDlX5TYZIw-0Oi1gvQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97ce01c0c.mp4?token=Q6vh1gaHV9RGK-DT6jGN08sjuKb3iYp963beF9500dVyzhcXXk_mm_jK07CaBSna56BjfDhUEqPioMoLOIEdmHjR5rLwMRtRpjeXDytGNuBn68u6K_j0bYCnEOaJRqC3kJrk4CJ0aM0iMiMvs4CQShBvyvhIafv0P0CdbFQksBVQYYKnVgScqXWwG_V4gN1-eh1EqgGok-jgT_Wbj5_eihka1Pwf8wGuR9N-LUKqhBFJYr4PI05tWQrHdC2SZSabXlK_846v9INyn5q2B3sdSxnnHzAepkTp6LT2xbIzOvZBpWdkhZsOJFyXxltQeC-jbdKXDlX5TYZIw-0Oi1gvQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تپه علی الطاهر در جنوب لبنان توسط ارتش اسرائیل فتح شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/132199" target="_blank">📅 13:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
گلستان فردا چهارشنبه تعطیل شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/132198" target="_blank">📅 13:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
صداوسیما : نفتکش هدف‌گرفته‌شده در تنگه هرمز پس از نادیده گرفتن هشدارهای مکرر مورد اصابت قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/132197" target="_blank">📅 12:58 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال استریت ژورنال: قیمت نفت افزایش یافت و معاملات آتی سهام در ایالات متحده کاهش پیدا کرد، پس از آنکه دو کشتی تجاری در نزدیکی تنگه هرمز مورد حمله قرار گرفتند، که این امر نگرانی‌ها را در مورد امنیت منطقه دوباره برانگیخت.
🔴
قیمت نفت برنت از مرز ۷۳ دلار به ازای هر بشکه عبور کرد، در حالی که قیمت نفت وای‌تی‌آی به حدود ۷۰ دلار نزدیک شد. با وجود واکنش فوری بازار، تحلیلگران گفتند که افزایش تولید اوپک پلاس و احیای صادرات
نفت خلیج فارس، انتظار می‌رود از افزایش طولانی‌مدت قیمت‌ها جلوگیری کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/132196" target="_blank">📅 12:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
یک روزنامه پاکستانی: دور سوم مذاکرات ایران و آمریکا؛ احتمالا ۲۳ و ۲۴ تیر در اسلام آباد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/132195" target="_blank">📅 12:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132194">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / مقام ارشد آمریکایی به آکسیوس:
ایالات متحده با حملاتی علیه اهداف ایرانی،
انتقام حمله به نفتکش ها در تنگه هرمز را خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/132194" target="_blank">📅 12:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132193">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUCYE3VFojE1N6Abe2vdnyz6_apUZfjI4Bk0grgW4t4sJdHh6O-K2viKjWaKTZZ0uZHhSw-YTaQcuCzDOyy8lVfMYT1hpqK885JrUfYoLh5RP5zc125vbAtmHBi83dAjYQJT-shHITvKD2wSnrLpx4n12psFA4ZApnOCIvRbOw96kIK3k0fJ2nyqhfBmTCYj1PG40_EKqF8ljiY6ofJTVJ7HK2bF94jPQDmIUcZSa2IkdC8HImQaxrs-LdecL31K_cUynlP9GeP3OTUEAT5Ax5wbUtFbk2jRhZr616FSmDeaNAfK_l-dT2xyWzXpSnEXTgbqtothJxhaZc1Bz5R_4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش سناتور لیندسی گراهام به تصویری از او در تهران که با تفنگ هدف گرفته شده است: «حداقل از یک عکس خوبِ من استفاده کرده‌اند.
🔴
دشمنانم بهترین معیار برای قضاوت درباره من هستند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/132193" target="_blank">📅 12:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
پیت هگزث وزیر جنگ آمریکا یک دفتر جدید برای پهپادها در پنتاگون تأسیس می‌کند که در همه زمینه‌ها ، از پهپادهای تهاجمی انتحاری ، تا ربات‌ها و قایق‌های خودرو های  زمینی ، اختیار تام خواهد داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/132192" target="_blank">📅 12:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c677b2d00.mp4?token=BLwfA7u0EbFFHxdtByc335fVsRIz267lRaJmPqBp7vzbVXRezhyR5SJRB-7o7OstNBNOTWNgEYfyKgwXF5sGHhVA4BiZGcDPY6IIpVvZjxiVeMgUisV6HBtclC_BtcM2iVjX2OqiLC4v6D-ch_Oyteisa_8vfIg07H9jkXCPXDV8YMqd5kA-rLgoxJNbXRHWs0k2SFCQ72NTNCxindW4uvlGLgXQUVTGG9L627RF3QtIWYpOXWMf74NY845EdvAcYLEHfvQRNGPZkqlSTPgSAD6QMuQ_B2NHP1zFsYoNwg1P-NHEsIDGatu7rbMQPpc3MZTy4_uc39Ez0b3tkRYazA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c677b2d00.mp4?token=BLwfA7u0EbFFHxdtByc335fVsRIz267lRaJmPqBp7vzbVXRezhyR5SJRB-7o7OstNBNOTWNgEYfyKgwXF5sGHhVA4BiZGcDPY6IIpVvZjxiVeMgUisV6HBtclC_BtcM2iVjX2OqiLC4v6D-ch_Oyteisa_8vfIg07H9jkXCPXDV8YMqd5kA-rLgoxJNbXRHWs0k2SFCQ72NTNCxindW4uvlGLgXQUVTGG9L627RF3QtIWYpOXWMf74NY845EdvAcYLEHfvQRNGPZkqlSTPgSAD6QMuQ_B2NHP1zFsYoNwg1P-NHEsIDGatu7rbMQPpc3MZTy4_uc39Ez0b3tkRYazA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه وقوع انفجار دمشق در نزدیکی محل اقامت ماکرون رئیس‌جمهور فرانسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/132191" target="_blank">📅 12:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
تلویزیون سوریه: در پی انفجارهای دمشق، ۴ نفر از نیروهای پلیس زخمی شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/132190" target="_blank">📅 12:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL1kua0qsWlqkqlmTsMABgBdFyrJCV4jLsEYQkqwRLSPIia7S66NOB-RBalQdvqNP-Jz-E8OxlNIMln2Gb84AMk3nLhEXZHlMr_jcXDcbvyjEgd40cy-nGTDhjOb-vWvOMoAmGn5U6GFiMm2bt4jQRPuEF_NT8f2jzlCXw6DDMB-lK0fIzT9U-ohZnI_Mg53q85ReskaJyfDtNEJz7G6UZxrH2ps8qhbMIVb5W7RrlTilWz79DN-i4xE0XpqsNpi_PP5v4jWP6ThvQ1buwKrPdKsxeY_odv2xZesUZHmLbTPMQARGXjUt3Ise_eE8b-hmcGA1abeRstvI_6iI2N2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
پیشنهاد من اینه بازی با بلژیک مجدد برگزار شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/132189" target="_blank">📅 12:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
افزایش قیمت گاز پس از حمله به یک شناور در تنگه هرمز
🔴
قیمت گاز طبیعی و نفت اروپا پس از گزارش‌هایی مبنی بر حمله به یک کشتی حمل‌کننده ال‌ان‌جی (گاز طبیعی مایع) در نزدیکی سواحل عمان و هنگام خروج از تنگه هرمز، افزایش یافت.
🔴
قیمت گاز طبیعی معیار اروپا بیش از ۴.۵ درصد افزایش یافت و تا ساعت ۰۷:۰۵ به وقت گرینویچ به ۴۶ یورو (۵۲.۵ دلار) در هر مگاوات ساعت رسید و زیان‌های جلسه قبل را جبران کرد.
🔴
قیمت نفت نیز صعودی شد و نفت خام برنت، شاخص بین‌المللی، ۱.۲ درصد افزایش یافت و به حدود ۷۳ دلار در هر بشکه رسید که بالاترین سطح خود در یک هفته اخیر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/132188" target="_blank">📅 12:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
انفجارهای مرگبار در دمشق ۴ کشته و ۱۸ زخمی بجای گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/132187" target="_blank">📅 12:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
دبیرکل ناتو: اروپایی‌ها شروع به جبران آنچه آمریکا دیگر قادر به تعهد به آن نیست، کرده‌اند
🔴
بهتر است اعضای ناتو انتظارات واقع‌بینانه‌ای در مورد چیزی که واشنگتن واقعاً می‌تواند تضمین کند، داشته باشند
🔴
وال استریت ژورنال به نقل از مقامات: جبران از دست دادن قابلیت‌های سوخت‌گیری هوایی ایالات متحده آسان نیست، زیرا مستلزم ساخت فرودگاه‌های مجهز بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/132186" target="_blank">📅 12:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
سرویس امنیت فدرال روسیه اعلام کرد، هشت عضو یک هسته مخفی وابسته به یک گروه تروریستی بین‌المللی در جمهوری کاباردینو-بالکاریا بازداشت شدند.
🔴
به گفته این نهاد، اعضای این گروه قصد داشتند به ساختمان‌های نهادهای انتظامی‌در کاباردینو-بالکاریا حمله کنند تا با تصاحب سلاح، به فعالیت‌های مخفیانه بپردازند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/132185" target="_blank">📅 12:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
خوش‌چشم در ارتباط با خبر خروج سوخت رسان های آمریکایی طی چند روز گذشته: این گام بعدی آغاز جنگ سوم است، با لالایی دشمن خوابتان نبرد!
🔴
دشمن در حال افزایش ظرفیت و استعداد نیروی دریایی خود، هم برای اقدام نظامی و هم برای محاصره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/132184" target="_blank">📅 12:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
شاخص کل بورس تهران با رشد ۱۲۲ هزار واحدی در معاملات امروز برای نخستین بار در تاریخ معاملات بازار سهام وارد کانال ۵.۳ میلیون واحدی شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/132183" target="_blank">📅 12:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
دریافت کارت ورود به جلسه امتحانات نهایی ۱۴۰۵ از امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/132182" target="_blank">📅 11:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f388689de.mp4?token=q9d4qF23TTtKXEQe4e1BotJ474u59UviTTJEJoEhOd6v1m1Y6IG5QiJ_-eziDZ3hLSfrWdyxoRy4idIHtfCMih41HwJhbiECBJhy9rr6rDOMA2lPf8tGzpxC2A_yYfPCGF10b5djyC74J593GO3xBMXLKgkaKozC2lKh0mvJSW7Tbisr_Ui5hHVIqwomGnVwR_N0bvgxuSUJVnEMIL5daC-TEjoRPOSZSN8Jjh9XqG4v6QQ35zHTG5fq1fQxVDib2Xk4TuffZnF9j-u-naav_NOc_Bi8fnVSYF62Nazm-KeUxJtBZlwlWD1OIA4jdcTVqBviu4_FxJ0tJoaJdFT2fYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f388689de.mp4?token=q9d4qF23TTtKXEQe4e1BotJ474u59UviTTJEJoEhOd6v1m1Y6IG5QiJ_-eziDZ3hLSfrWdyxoRy4idIHtfCMih41HwJhbiECBJhy9rr6rDOMA2lPf8tGzpxC2A_yYfPCGF10b5djyC74J593GO3xBMXLKgkaKozC2lKh0mvJSW7Tbisr_Ui5hHVIqwomGnVwR_N0bvgxuSUJVnEMIL5daC-TEjoRPOSZSN8Jjh9XqG4v6QQ35zHTG5fq1fQxVDib2Xk4TuffZnF9j-u-naav_NOc_Bi8fnVSYF62Nazm-KeUxJtBZlwlWD1OIA4jdcTVqBviu4_FxJ0tJoaJdFT2fYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ناتو در 5 سال آینده 40 میلیارد دلار در زمینه قابلیت های ضد پهپادی سرمایه گزاری خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/132181" target="_blank">📅 11:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d9e55bd435.mp4?token=jlen8wwMIURiapqoCgO6XrRM7UeEGnTRNV6YeWiiVk7iNWIg1RzjS1zWjzD50B5oa1XxODknrWX7KvIapOJ-jZBwLmhurhGlWphwQEkH7pNVei6af260OsaDfwtp2A2Ko7PIjZEEyKNrLo0ypAJNoTlQx4b1G8aULI7g_rDUjamfeXoCYuRWGJLl_W8MsrNSzr6NZCN45zTEOGH6BaYpf-ly9V_uMD3cykGivjVocsq1jgughnkMbzRx931STcUIx_YSgGnQ1Ja8dZRL8kFV1Vgbg67Stoz9fMVCR5pDItb280wvXLaogup7DhltbkWVtUtUua3_tAdtzvkse4GVfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d9e55bd435.mp4?token=jlen8wwMIURiapqoCgO6XrRM7UeEGnTRNV6YeWiiVk7iNWIg1RzjS1zWjzD50B5oa1XxODknrWX7KvIapOJ-jZBwLmhurhGlWphwQEkH7pNVei6af260OsaDfwtp2A2Ko7PIjZEEyKNrLo0ypAJNoTlQx4b1G8aULI7g_rDUjamfeXoCYuRWGJLl_W8MsrNSzr6NZCN45zTEOGH6BaYpf-ly9V_uMD3cykGivjVocsq1jgughnkMbzRx931STcUIx_YSgGnQ1Ja8dZRL8kFV1Vgbg67Stoz9fMVCR5pDItb280wvXLaogup7DhltbkWVtUtUua3_tAdtzvkse4GVfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه انفجار یک بمب دیگر در دمشق دقایقی پیش
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/132180" target="_blank">📅 11:44 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132179">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
بورس انرژی: فردا بنزین سوپر در رینگ داخلی به قیمت هر لیتر ۸۴ هزار و ۶۰۰ تومان عرضه می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/132179" target="_blank">📅 11:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132178">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
کاخ الیزه اعلام کرد ماکرون در مسیر رفتن به دیدار با جولانی، رئیس موقت دولت سوریه در قصر الشعب دمشق بود و هیچ صدای انفجاری نشنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/132178" target="_blank">📅 11:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132176">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fwNRcRI2xZGh5M7PkhvqDWL7PTrTNb9Asm0_PDSAnc1JoLzgd335pG-yaDPJhduquyIzVU0XVDhyex3Ua4J-2EZeeKQyGt1iJqI9R4V9eS4iqtYcJE98z-I13lsTnIr0WBMYgFXyBQouOH5o7hUKYxq0RIQVHA0T33q1A4mokK66GjvZO3yfKVOeDhv7qwE7j_ShHqNjjNEsK1FWmKzTGUTyxi99TePpacb_WgVDXMqear3xmX2blBlJ3acR3QI8qgpX_Si8dwed2A9zpX_E2EXJRquQXBaOM9No1arBvhb74Ycj5pXEO_bxbBYALzsTNLwQHqtPlLkXkaDoNAPY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TKKymkDjYtSSWGp0Xd-UGLArphowzzQDc9zFRHx4V0zIv81jBrSrOUceWngkwgZvt49EBJIhWlEzZb9SZcXIONfHZkJx2ZC_MY7gyo7hxbCprEyr0HnDMVv5zpRTNzdy49GaFbD7Uav6FFXT9YQRKz8ufR7J-oSb_kgI72otP8vi_ctmqnnSaQcXkQF6kXYDmrQGtk1St9p_55c7aPL-ygdRoKdH5sUk0IeB1dXGBuVwLEceEw5q0HLlG04jnoumKfBYQ5mrJySzLDX0rlT0V9klKNvhjN-V0j2PgrucMMPq3zDyt2xtzqSNAeEmzYcZf1bYq_fOnyIL9s9TBtNcbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از قبل و بعد حملات مشترک آمریکا و اسرائیل به پایگاه هشتم شکاری اصفهان.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/132176" target="_blank">📅 11:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132173">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca0c1ded30.mp4?token=pJC2DYgPGjeC-OpMVv_MGOeeykAx1RpwiMiZXzGoM9vJkJmy5LQDe6Cx_O8u9rxhoLvYDU1ChixGTs1G2eLQ7R9MDgZM-FdNDn96HR6dL_l_jTPF2Jf1Si3knS5fIJU_g_cngl3xbXSPd1jjXFH5kk9C0fZsDxiNXUppXsQufFXQQ90vQNAM6H0mGelbTaZZjrYYQfuSaQ9kzleJbb8D6MWEgaDX2njOU9GES-ZBzu9rIcDNjaErNcj7Afn7CiW08gfBsrBRgEJOZ18f6Rin4L9Whr7ikVJB0JVSNlRMhs9uYDPCm1sV63o8038PW03OeCCPVgPSPewSnXOZ09e7Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca0c1ded30.mp4?token=pJC2DYgPGjeC-OpMVv_MGOeeykAx1RpwiMiZXzGoM9vJkJmy5LQDe6Cx_O8u9rxhoLvYDU1ChixGTs1G2eLQ7R9MDgZM-FdNDn96HR6dL_l_jTPF2Jf1Si3knS5fIJU_g_cngl3xbXSPd1jjXFH5kk9C0fZsDxiNXUppXsQufFXQQ90vQNAM6H0mGelbTaZZjrYYQfuSaQ9kzleJbb8D6MWEgaDX2njOU9GES-ZBzu9rIcDNjaErNcj7Afn7CiW08gfBsrBRgEJOZ18f6Rin4L9Whr7ikVJB0JVSNlRMhs9uYDPCm1sV63o8038PW03OeCCPVgPSPewSnXOZ09e7Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
انفجار خودرو در نزدیکی هتل محل اقامت ماکرون در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/132173" target="_blank">📅 11:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132172">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bGozmNsWCD1jWO3aWRYZnKqoIpTn-D8btYIziEs76IZIIQ1tvpeNACulOwt2XmNqgRFfIYvOL1zGu7wQlzd_L599AxmcI8ndBXAbl_fI7OGacHaEf20BtLTGzPc_EEBeJKQ1DISjZTnblrQiPr8q4Nq8Zk8n24CIHxWKWhsJpGFBHJ58XX72oxfVzSJ_p9OTpZ3zXzoM5Ka-oERyEJZd5uwQmLrlkS1fVxAXoRvhz3AJmgYBgyozs-dj6yhili_3eg-upGVnl6rrTuVbR8_x-mMfwj27C7brs58ykTnszlv_uVkNx3r_j1Th_NEQZreNjtXhvTwE9e4V96hrVmDHDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش پیج رسمی تیم‌ملی ایران به شکست شب گذشته آمریکا مقابل بلژیک
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/132172" target="_blank">📅 11:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132171">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
ولادیمیر سالدو، فرماندار منطقه خرسون اعلام کرد که حمله هوایی گسترده اوکراین به منطقه خرسون دفع شده و ۵۲ پهپاد منهدم شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/132171" target="_blank">📅 11:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132170">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gn3JWAm_wLMHpdd-EDeftkMxAgzDkKc4sgePGVc2nVOf2cMdAERm0ot9W5ofyNRHQ11TiHrrGhMS8KLGyKxCfC64SZl2uxgckzeOmlAt3uQuFonCfnVstIvCF293_fjhFp55yQh91QS3LNTzrYIqouIn4hCA8uyMPCuxVniEuaq8AvYC9d91DlHDzTTbuXl5iIAecf6N0Q4wioi6SbfelNA6PMUWFhBbnyqj8kz-QwaDSldbBzUhDm9E83xJ23UQvkWlSafDxLUm3DiyYp9jE-F29DP76xv2LfmfH6C7d6-aJgKZ4O2JtPDf_Fz58VbCyO4VAMy0Kn2A05yYb_dRFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از انفجار در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/132170" target="_blank">📅 11:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132169">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / منابع خبری از شنیده شدن صدای انفجار در دمشق، پایتخت سوریه گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/132169" target="_blank">📅 11:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132168">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / منابع خبری از شنیده شدن صدای انفجار در دمشق، پایتخت سوریه گزارش می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/132168" target="_blank">📅 11:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132165">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439ee96d4c.mp4?token=HJgQtawPdYsU139AKGuqOdvZbi5mfdGRoHd5lEffwJXWEQ9VKUii6b84A7zMnVkSNs1lzkdeMB7wgPn6MuJbC6-r0eThHbzJiqjv_l8Kp6N28DuPF3h7DO3WCfkzNPhCjuKvnPNJj7UvDvYLbxHxfp4zBgQhL4bjsYbXqVY1Aei_uzLZa4h2VOBzlol0zhMoZStgIg0rVmrl274VFLxpBYgQlZQa_vz2bo8rrVid2mDDENoDHw_E2XT3gjQTn0l4gSdE5wYhrefUVmDN03o_SzENnGXrAdvDhYUEdnsDI0iNjCz_zlEs6EDBI4EyENj3OD-F0oOBXtQhbH29rW8dQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439ee96d4c.mp4?token=HJgQtawPdYsU139AKGuqOdvZbi5mfdGRoHd5lEffwJXWEQ9VKUii6b84A7zMnVkSNs1lzkdeMB7wgPn6MuJbC6-r0eThHbzJiqjv_l8Kp6N28DuPF3h7DO3WCfkzNPhCjuKvnPNJj7UvDvYLbxHxfp4zBgQhL4bjsYbXqVY1Aei_uzLZa4h2VOBzlol0zhMoZStgIg0rVmrl274VFLxpBYgQlZQa_vz2bo8rrVid2mDDENoDHw_E2XT3gjQTn0l4gSdE5wYhrefUVmDN03o_SzENnGXrAdvDhYUEdnsDI0iNjCz_zlEs6EDBI4EyENj3OD-F0oOBXtQhbH29rW8dQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر هوایی از قم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/132165" target="_blank">📅 11:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132164">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
آکسیوس به نقل از یک مقام آمریکایی: سپاه پاسداران ایران دست‌کم دو موشک به سمت کشتی‌های تجاری که در حال عبور از تنگه هرمز بودند، شلیک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/132164" target="_blank">📅 10:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132163">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
سفیر اسرائیل: دور بعدی مذاکرات بین لبنان و اسرائیل، ۲۴ و ۲۵ تیر در سطح سفیران در رم برگزار می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/132163" target="_blank">📅 10:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132162">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tJHkfYQtOqoKpaIetWaAa4vGwoR9oxiz04-63g9M1snTjKHSDJgKEuJW-XWVpdcw7s0qpBxehH7SK9BxtbkJDwWzawl7rxEIG_DFIMSN-VTfBkGQSEj2Dwx2jnlJsjBMrmQg1RZDWOEcI9ZY8jjPmw1FkBL0pd2tgfXDiSwjwgNEf4JpgyTR0gA-cfpm-6jlMu_DBo35J0Im9XP4x57umayUpm36Ck534ghdwVniHe6A6z4w47uw03fjuh_ZXljdCsyFblGnO9-visVT-9UlrKNdWMXcZBMUrIvLsClkgUA03byoCvXmzuNgWFnDqU4GUPNToijHV449MnKhEAhxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مکرون، رئیس جمهور فرانسه و احمد الشرع، رئیس جمهور سوریه در دمشق
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/132162" target="_blank">📅 10:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132160">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6591abe34e.mp4?token=YB231WNMEWijjl9p83jrhQA-HLR9CmRk6Svr2y-rJ2WKR6v7fhcbOwZq00sU9rE08mIzRIZZNtAwamDh1xR2daqsRU7EmSmLwiHy6Nz7TVujr2Z9nJzHrSZowfMLrF64R7nGDsLQWedU-LwZ3qAnNp_ZAZcou6I_OyXW66sqQGh1uhnqqIV-at4jbqD3IA_ucwCyET2CCoHFIikoxMAa79kizct_hAnoMqOeqJNqOOXbA0FF5hsSjUE66AkM8AOyE7E0EZadTZbCF8hMOUbvPkD3JLzVbTMu2CJOviUpY_nXxHZjfJHxWSa1OE1GJMxzbdwFJUnw7kL5IZXey7RAog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6591abe34e.mp4?token=YB231WNMEWijjl9p83jrhQA-HLR9CmRk6Svr2y-rJ2WKR6v7fhcbOwZq00sU9rE08mIzRIZZNtAwamDh1xR2daqsRU7EmSmLwiHy6Nz7TVujr2Z9nJzHrSZowfMLrF64R7nGDsLQWedU-LwZ3qAnNp_ZAZcou6I_OyXW66sqQGh1uhnqqIV-at4jbqD3IA_ucwCyET2CCoHFIikoxMAa79kizct_hAnoMqOeqJNqOOXbA0FF5hsSjUE66AkM8AOyE7E0EZadTZbCF8hMOUbvPkD3JLzVbTMu2CJOviUpY_nXxHZjfJHxWSa1OE1GJMxzbdwFJUnw7kL5IZXey7RAog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مایک پمپئو، وزیر خارجه آمریکا در دوره اول ترامپ: حکومت ایران عمداً چهارم جولای (روز استقلال آمریکا) را برای مراسم تشییع آیت‌الله انتخاب کرد تا نفرت خود را از هر آنچه آمریکا نماینده آن است نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/132160" target="_blank">📅 10:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132159">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
خبرگزاری «رویترز» به نقل از منابع: عربستان سعودی در حال بررسی امکان افزایش ظرفیت خط لوله انتقال نفت خام به سمت سواحل غربی در دریای سرخ است.
🔴
عربستان سعودی، مذاکرات اولیه ای را با برخی کشورهای همسایه برای کمک به آنها در انتقال نفت به خارج از تنگه هرمز آغاز کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/132159" target="_blank">📅 10:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132158">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_Fdla1Qz_EE-aXf6pFHW8p0hA-n21EXyAlTckq-2_E4tTCbu_h3MzvdOE0FZS2JDL9C3DNQmHHTK_PgOP78NwkgPxI3GuVsLr0THdhlfJe7kHAxswq6wZXwfEnbKPslXCV7xlpkVaPVXB4EXhzam4sFo0Iq5CBSDnlrwo-X5zVim-DqKbPVPJpPNIuhxCFrgOt_W_T-86H2lpZkM6W-b-N1jb8ibWr5eDTnJIVA23rOocr3E0Owe8jQiA5tkD-qLwP96x2yditnZ30Vy6pxJoYuXlYzkBY8XiBUFIwPp0YO38QN-Ntdm3nfQZe1ZlJvFPlL4lr0sgMftCrkGavDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زلنسکی: بدون سلاح‌های هسته‌ای، شما دیگر عضوی از باشگاهی نیستید که دیگران از حمله به آن باشگاه می‌ترسند!
🔴
در عوض، شما عضوی از باشگاهی می‌شوید که می‌توان به آن حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/132158" target="_blank">📅 10:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132157">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
قیمت طلا در معاملات روز سه‌شنبه بازار جهانی، کاهش یافت و پایین‌تر از رکورد دو هفته اخیر خود معامله شد.
🔴
قیمت هر اونس طلا برای تحویل فوری با ۰.۹ درصد کاهش، به ۴۱۲۶ دلار و ۳۳ سنت رسید. قیمت هر اونس طلا در بازار معاملات آتی آمریکا برای تحویل در ماه اوت، با ۰.۷ درصد کاهش، به ۴۱۳۷ دلار و ۶۰ سنت رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/132157" target="_blank">📅 10:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132156">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
نیویورک تایمز: انتظار می‌رود ترامپ به اردوغان اطلاع دهد که مایل به فروش جنگنده‌های اف-۳۵ به ترکیه است، اگرچه هنوز مشخص نیست چنین معامله‌ای چه زمانی یا چگونه انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/132156" target="_blank">📅 10:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132155">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdoxZ1kw3iN50lYINd9LC3HPqGXnl26_5VBC6Zid7mw4guNH-zzWjzVx52CvQsFo4qFrAstPKmzn7cCcG1Xs1cXLlmO_zGMHBbLyVfoZKG2OV1DWyD4uKEDOSGwlWcfEBrRptmnsmvhH8waeKyhfXoQS0PJLk25zV0ghX1-sNRD1OFJBkFE9-lJWgELFewZrZ2uLDgxAcvt8wtosz7-1ihCT--m2qZIBMgfE0HGooLQbrp60fyFaWAPxRTq1K3Lld_dFMN-jvmBWHpQv9_0dor_6Zm86RRjcRRCL-GrxAZJpZ6NtdI9qXF8Zc0k221FkyiAhEp3I6PdoUDeBX5SuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میدل ایست نیوز: تصاویر ماهواره‌ای نشان می‌دهد ناو هواپیمابر امریکایی «آبراهام لینکلن» از دریای عمان خارج شده و در دریای عرب مستقر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/132155" target="_blank">📅 10:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132152">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6df8a4cb89.mp4?token=fc4qAbzmDs1F0r2sprSUVdCtPO9ilphrOVTW1XlnCWkKj--mLwLvZ_uYHUE_fZS-FC9eXJeb5bMvwzFe54YQ9KQwYpdh8QpEGARLcBaD3Agu_QkELa1nQqv2u5JN8SkDzDsUD4hClH3tPeCGM6h36pG0sF1fwScIgNM7K_EjZ4Kdgm6pPZb1xQHy_YJspfDw63hZ5ukZalC3L2fMx1s_30KJcE71nQr_mm3XXeCCdvNnL_e5CflE4K8rJXJ-OkOkiX3Z2vqTOxDlZS5i1FPPVAQWAsGogQRVqmI3V2o-kHOdbstZ0LgKaag2s3I0xE5Pb8VPol4YDiOqjGBN7CgzgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6df8a4cb89.mp4?token=fc4qAbzmDs1F0r2sprSUVdCtPO9ilphrOVTW1XlnCWkKj--mLwLvZ_uYHUE_fZS-FC9eXJeb5bMvwzFe54YQ9KQwYpdh8QpEGARLcBaD3Agu_QkELa1nQqv2u5JN8SkDzDsUD4hClH3tPeCGM6h36pG0sF1fwScIgNM7K_EjZ4Kdgm6pPZb1xQHy_YJspfDw63hZ5ukZalC3L2fMx1s_30KJcE71nQr_mm3XXeCCdvNnL_e5CflE4K8rJXJ-OkOkiX3Z2vqTOxDlZS5i1FPPVAQWAsGogQRVqmI3V2o-kHOdbstZ0LgKaag2s3I0xE5Pb8VPol4YDiOqjGBN7CgzgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اوکراین بوسیله موشک‌های سامانه HIMARS به بخش تولید خطوط لوله اصلی گاز  در بلگورود حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/132152" target="_blank">📅 09:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-132151">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSyOx6E0nh42GspToaYe10YFetOa2RCyIo2lcb0mB_nF4nmr4Ywz5yKIWYUu2Ii8pHCsk2MQ5KpSm_CCN696oShexSzDrEUgNF4EhIFAVN1ctzQd5gRjeCf37eaCrUgqaER6gIaoVdJYn2Lr8fK03DlxilB51Y9tgG2NUQqft0ytu04L_s8q4eFGfIpcL5XtoI9iEtvOaRp9JcrR6-gQuFVAjZAFeHqPLKUIn6ARo9OjMRDfJbOM438hpEaMci40xUZh9Cqacp9tue7LFQxMni_HCSOuie7EWIiel0vfTpql3DP6jsdrTvrqieYS3tHqS8NIVHK8zNUaNk5Ritj1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۹۷ هزار واحدی شاخص بورس بعد از سه روز تعطیلی
🔴
شاخص کل بورس تهران ۹۷ هزار واحد رشد کرد و به سقف کانال ۵.۲ میلیون واحد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/132151" target="_blank">📅 09:49 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
