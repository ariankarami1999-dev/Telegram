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
<img src="https://cdn4.telesco.pe/file/OFmAsl6AJkLnCDdVMTYWn0Nvq4a6zMxJkG7jW0LVOWH0zYiDhf8XYAfIYYEbtUaHMt9KBURRypRn607pWUJOE9IA78uZwioSJPKGswfd1ruU0z6iQaJjwa_BrpbbqkrQDIMzzOSAIY8XouiewMkIyl_W8k4UZ_TZHpL1Y9fEuCUrb_jmqcLUhGAAT4zBwd5_mTMUXrD1FFB1Y6PyvCrUKEj30I6qGNc51Udtn9IPVyPkf0rwqP9vbr5CMKDo7COiNh4M2nKEZtAf1ZOiFsmmKu6rN3csrbxgZw_emlj4uyQ8zgNyC9piy1cPnelRsnxLk0FKWmc3CzW_uMN449fR0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 924K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 01:18:55</div>
<hr>

<div class="tg-post" id="msg-134258">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/alonews/134258" target="_blank">📅 01:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134257">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4784c0afa9.mp4?token=piMDef5cXJXp5GSBY_9zT-NWgeW2BrsEg8Zq4a3LUK276OrlWENh4ucDyE3cZHLWc72UaoXEDCWHdmM2QJ1-PcyUvmi0ATWcp7OOIZghXUnYcvtxl9nhCjaAkA9fxDXvqMvIcui9keKTcjnmDIt5svsAO-J5inrX5TceRfyG_8OBnkmuLaU7F9R9K3UqPe5ZoPI6yO6X-Ubxx0LHHvQRyC7f4y6laten66aR8owBUETmwmLgSwBaXYdSqwy-owULHxDqFvfqwfD85Ks9-1Jm4KTqIS4kNxl2VpU0K4sf9mj2k2DXvH8PcbuqRsABTDfiQGKqpEdgCH1mIYL2VgonnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4784c0afa9.mp4?token=piMDef5cXJXp5GSBY_9zT-NWgeW2BrsEg8Zq4a3LUK276OrlWENh4ucDyE3cZHLWc72UaoXEDCWHdmM2QJ1-PcyUvmi0ATWcp7OOIZghXUnYcvtxl9nhCjaAkA9fxDXvqMvIcui9keKTcjnmDIt5svsAO-J5inrX5TceRfyG_8OBnkmuLaU7F9R9K3UqPe5ZoPI6yO6X-Ubxx0LHHvQRyC7f4y6laten66aR8owBUETmwmLgSwBaXYdSqwy-owULHxDqFvfqwfD85Ks9-1Jm4KTqIS4kNxl2VpU0K4sf9mj2k2DXvH8PcbuqRsABTDfiQGKqpEdgCH1mIYL2VgonnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دریابانی سیریک بمباران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/134257" target="_blank">📅 01:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134256">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
طبق گزارشات تو چیتگر پدافند فعال شده و پشت سر هم صداش میاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/134256" target="_blank">📅 01:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134255">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
پادگان ارتش و سپاه شهر بمپور که کوچیک ترین شهر ایران حساب میشه کلا ۶ کیلومتره با ۱۰ موشک فوق العاده قوی منهدم شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/134255" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134254">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
نکته جالب اینه آمریکا این روزها فقط داره پادگان‌ها میزنه و گویا داره شرایط رو برای یه سری کارا و تحرکات آماده میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/alonews/134254" target="_blank">📅 00:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134253">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
گزارش انفجار در تفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/alonews/134253" target="_blank">📅 00:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134252">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
انفجار در جزیره هنگام
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/134252" target="_blank">📅 00:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134251">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
گزارش ها از فعال شدن پدافند پارچین
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134251" target="_blank">📅 00:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134250">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
فرانسه هم باخت و تنها ۴تیم تا الان نباختن
آرژانتین، انگلیس، اسپانیا و ایران
🔥
🔴
باز بگید قلعه نویی بد هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134250" target="_blank">📅 00:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134249">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FALG6lZ5Ov21I8yX_bR0khsKkH8amlJjNZ9YfhEfNRLIEkr6Mt6D39GzRDI5UY-EzDqIYv8qSVCxwGXJsVTOPgcxgejQC9_79zOiZj7psySTgvt2lVByZBeUz-VmsUPmvMOnMaDrNSbFmUJuNW_rvhrdnf1NXN0l3m-4xzmn9e6DJ6ROubpLkDRwaqrSLAyaUPLYmAafngOQqOZlRndYQ4hyR8_gQrkLCfyqhQ_7mHG_SUtlVGHveJkqo4_vh92R_ClpkFKXR4Q_UNEWnS1k6BloobhGxFmFQRivltrmuFYopwXnp515s1K-OGOaNmXDnTpuFXzs2orcdh2fIJqv0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانالای ایتا نوشتند که دست خدا عیان شد و این عکس باعث صعود اسپانیا به فینال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134249" target="_blank">📅 00:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134248">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
انفجار در چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/134248" target="_blank">📅 00:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134247">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vw5TsS3WefnJMRNKXAUgmQPrYuSwNFjJm-Ama7jinlqtV7LvLVRBuiC4k_36wOnRCFzUu_aTYNX2CEoulEC2_LQpT-rAAtuxHQyElN5q2LR0iFkpPyo0uDU59mcboChfjY8ycHSYd6Kr6ZMUJaZDkTTKD4SQhcVy7C9nOD1nwKq4SxMHHVAuHsqk5IW83md2ddfgniAjpvESbX6mvhD8nBNWNTX1Aeru4UgIUsJb8tsjlTIgpYY5yBATWpDgtyeR6FutaOCN-iSa_wN6N3AbIY6Z9kSr9oN-do7YPl1sQINVW49JHniIU1Kso8MRDF0XQWgz__NI1tkXQ67QcyFaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما بشنوید از کشوری که در جنگ پشت جمهوری اسلامی بود و به فینال جام جهانی صعود کرد.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/134247" target="_blank">📅 00:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134246">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kx29CJhHuoGEgNpdj0JEDaujwhBYjoJ2nYi_uSMp3d8gzQ6B9gRVRyOt_-YEElCEyPI-_9Hvw5QgpYNmzOqF4cRfG7mVtmJcI2RIHHPaUNicEEd8pzxkfADGQwkiK960_2TWz60rLrkw2WPRLqbmMUydGJp-C39YNxyuXGetOPXRQAVyY_3SQ2CzA76DklPqhQredm_SvXGatYLGhV_CYFTnhAEbjn2d_ZuTb3m3dk_RR-gYpgsM0zVBwc71euGH0EOJNkW8IkZbBa_wNzx2MwZctKGGnBcUalqy4DbO9fcGlNb76ZiJbnPA0cC3HDlN96iWydWjhMqIedgo8ZzT-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
اسپانیا
2️⃣
➖
0️⃣
فرانسه
🇫🇷
اسپانیا رفت فینال
🔼
@AloSport</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134246" target="_blank">📅 00:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134245">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vn5PTZ2pBSRrMHQCMe9LQrbXxgOAwp28-5NBHylQ8NBL3T676p-23CZYHqzxVvd2U0Hpvcnj85PPMMktnvaojcgAJqnKCW8evZjvFbNYsWPgcwQ78zDAcFKSRQt-Gel_4UbLLGdbUT4t-Rdldb9M60MW5wfP6PZ7qbHDlwvd-P41lh6KnEg-aT2XLPk5ey0hL_tfs72eDMYPqzLhcArQ8QI8lhtvIcosQss-ogQGRcBZaXZxbJJAFB-Go193QVTtqL_mHiWEIJHgCE0FDcNOMjkrLbuFiG7OEv3Qt0bSJCCP-XYjEHStJoQIJ0ws8-YGenKaa8N5toPo1tLvlYIdRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سربازان ارتش اسرائیل (IDF) مستقر در قلعه تاریخی بوفورت در جنوب لبنان در حال تماشای جام جهانی فوتبال فیلمبرداری شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134245" target="_blank">📅 00:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134244">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ4-I8Ec_J5kRbuA-SAomh-VoYvM7y6gu0rqio4zXlRY2MRhKt4T_vmBhJv0NsY0YbS0kkKR9pBhlGz2V86Tq_yw-VyQBMxsIYILml9kSALs-3Dp8pVm5vi2sYQBenX6PrFU5_4urgUC695g4e5MasyZiHgkAY9ViPpDY1tepw9T48BsgSkb_tC68ftFBzOUBRi09yQZFV3CakDQjomUdWfsstiaj2xg_xFq24NHvPZ1mWiXmYf1cCAcWwDAUZ-VlfOJZEgWoi2jwZFxlWfNibe5dKvsmb_noaLzwOcdJT4vhEx-3HjjHzMD4N671E0PJfVwNxXI3hY0qmNzz9uwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید: در حال حاضر دیدار نتانیاهو با ترامپ تو برنامه هفته آینده رئیس‌جمهور نیست، ولی باید دید چی پیش میاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/134244" target="_blank">📅 00:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134243">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134243" target="_blank">📅 00:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134242">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
آمریکا شش فرد، ۲۴ نهاد و ۲۰ شناور مرتبط با محمدحسین شمخانی رو تحریم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134242" target="_blank">📅 00:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134241">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGUEG0fw6gfBNoUZXxYKyHE-KKjsX7fyCxSog9U-zqARFeIu-4l9AnONHhwitRo2S4aQLN56xcd1XwQ6bJ3rr26kf95FEoEo9KuNuGalvoCse7qXm3SAoSCMMypylyCU8I4W9-b7FZzCInNa0iXsG_K2yPNO8mKQ5lGbUx2iLiVMk8R7vAtrj2ZyIyhY4AAFWH3iX8lRSLoUDjrgTRIafhH-VwspT9DnX-0YoSytWhNkIiPPbs3av7PuXmb9OoocP74L1bSOO1so3WIoSxlyk8zcUSDIDBiebcS0-ZsgTH7g_Dfgt29d4pS0jOQiyZLSnfmE2eVjm1Z4N2D0mh-FDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت ، وزیر خزانه داری:
رژیم ایران با فریب زنده می ماند و شبکه شمخانی یکی از سودآورترین موتورهای آن است.
🔴
وزارت خزانه داری زیرساخت های مالی را که به رژیم اجازه می دهد تهدیدات خود را به امنیت ملی ایالات متحده و حمل و نقل جهانی ادامه دهد ، تعطیل می کند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134241" target="_blank">📅 00:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134240">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw9lYtEYezsvQkB5UvoLpqRpZhw22igL1vTMvAYIVw4P-4gKNZXKFq6zjSsoDpsIYuN8_LpkyzlH07693YQ_KH1mays1eG-sMV3k8up31KHpsvR9aYxXXgeV_4YBLvOwS9UvBziRv7Y90oCNhjGCKi_11pqO0FIYiklj9L8i56G_oJ2VrlC6NOzPtvhlc0x7vDClFmsY1t9dmAdrUq-tgXKyr9lmMHuTaF1QTkHYO-ENp8dX8RBW9G3T-GnzJM2nAbJF_BydKwvF47Ewf7UnKwAsBlEgaePaxUSPzt5X6KQBSrdgkuCICd-rrlgEA0vx8_39EphFbOT4jEsFrL1lKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
‌
کان نیوز: نخست‌وزیر اسرائیل بنیامین نتانیاهو قصد دارد در روزهای آینده به ایالات متحده سفر کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134240" target="_blank">📅 23:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134239">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e5a29b67a.mp4?token=jLdHA69EKYJP7hJOrMjN_ERUfl26SLTgOWGdpt_ZKDjS9yiuUI_r9mdMiTUP8iPLdhWnCFkpFdFpOasiCSNg42wp_l3t_xQDFqRoqXAOaka6ZvoeVCQq5JMFM19mwDQtfIQgd1oe7IptSwaMdownAGABscpnBikcT9op3HWhBY82tZGYAEzzc9f9sxqdyAhrIBGQdh764WaPaY2Z0gxkM5hVSZZXDH2cuDIFVeqN1q0Xoh4f0YcV3ywvqgWuNyMKFi9hmnmiW3MF4oW29TNhAtshXUo1qE6wdY2ezef2uZKk9w-ylKlgJ92dv-QVEkQy63tlC5wBhDGBjhQCdt9xig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e5a29b67a.mp4?token=jLdHA69EKYJP7hJOrMjN_ERUfl26SLTgOWGdpt_ZKDjS9yiuUI_r9mdMiTUP8iPLdhWnCFkpFdFpOasiCSNg42wp_l3t_xQDFqRoqXAOaka6ZvoeVCQq5JMFM19mwDQtfIQgd1oe7IptSwaMdownAGABscpnBikcT9op3HWhBY82tZGYAEzzc9f9sxqdyAhrIBGQdh764WaPaY2Z0gxkM5hVSZZXDH2cuDIFVeqN1q0Xoh4f0YcV3ywvqgWuNyMKFi9hmnmiW3MF4oW29TNhAtshXUo1qE6wdY2ezef2uZKk9w-ylKlgJ92dv-QVEkQy63tlC5wBhDGBjhQCdt9xig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل سوم اسپانیا به فرانسه توسط یامال که آفساید شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134239" target="_blank">📅 23:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134238">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f5a541186.mp4?token=kbeGERXWXrc5hY2nKGERs058tgzkmTz3n1YHqAE0ZwmE0yis9RinHyd-oQxTtRKDEK-7GrCxCymzmET4nVVct76G_831dryemTsytCVAFekP_b8F6iIjQLtVMfDpDXT9yZT0FC8FCgl_5bZ0BRs1z_6dU3JGaEOLK8aGfdR2v34AxKvEXzvA4Wkxs5r5WSlwu8xH4fEqm9cv6M_QPXiQVn5TN6PlHojCLPARl24LQ7Ut2iBcJOmpPrwLV3QUaDMraqZ23MrNp_oBQNcar92ZcJcCWKbru95qgmoLTQUJ_cOLXanY4sgKURze9rSp-WI9E6Wf4-EKLfK9jyIm7KRmjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f5a541186.mp4?token=kbeGERXWXrc5hY2nKGERs058tgzkmTz3n1YHqAE0ZwmE0yis9RinHyd-oQxTtRKDEK-7GrCxCymzmET4nVVct76G_831dryemTsytCVAFekP_b8F6iIjQLtVMfDpDXT9yZT0FC8FCgl_5bZ0BRs1z_6dU3JGaEOLK8aGfdR2v34AxKvEXzvA4Wkxs5r5WSlwu8xH4fEqm9cv6M_QPXiQVn5TN6PlHojCLPARl24LQ7Ut2iBcJOmpPrwLV3QUaDMraqZ23MrNp_oBQNcar92ZcJcCWKbru95qgmoLTQUJ_cOLXanY4sgKURze9rSp-WI9E6Wf4-EKLfK9jyIm7KRmjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل دوم اسپانیا به فرانسه توسط پدرو پورو
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/134238" target="_blank">📅 23:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134237">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc7SrDhrESBcHWpyJTSPq85z8neNUou6utf4F3eT3VEVtNIhduf6nOXjcaRfCpKc6gQNe076FL3i0X1jy27OjGX73TdsYMH-dzf3Jv-331eUeVH1Vkp61ZtXh9C6stkXfbfgcwwixoAqV-QujzKwv2b9otRBTl05ZCrwBq64oWREmmilqr44uYpPnBUcb1v0pZY-H_uo8XM0rDmTf63UQoTP3203YGWCmCUafKvRShfqx6lqZ1TreppZdrCfpuw15xpkRsyLY9qzFW5rO6yMQRV5IrBtUGSN_7THDUEg31rHZK97KxJL1pacpQ42NGyt2lLPl1sJRWrTp3DGkB5cXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعضای بدن یک جوان کورد در بیمارستان تهران
🔴
سمکو گلچینی ، جوان ۲۲ ساله اهل بوکان که چندی پیش بر اثر سانحه رانندگی در محور بوكان سقز دچار آسیب دیدگی شدید شده بود، پس از بستری در بیمارستان مسیح دانشوری تهران جان خود را از دست داد.
🔴
با رضایت خانواده این جوان اعضای قابل اهدای وی شامل ریه کبد و کلیه ها به سه بیمار نیازمند پیوند اهدا شد تا آنان فرصت دوباره ای برای ادامه زندگی پیدا کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/134237" target="_blank">📅 23:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134236">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: پیش‌بینی می‌شود که نخست‌وزیر اسرائیل، نتانیاهو، هفته آینده به واشنگتن سفر کند، البته این برنامه ممکن است تغییر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134236" target="_blank">📅 23:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134235">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
دقایقی پیش صدای انفجار مجدد در اهواز شنیده شد
🔴
در قشم هم صدای چند انفجار شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134235" target="_blank">📅 23:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134234">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
گزارش شلیک موشک از کویت
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134234" target="_blank">📅 23:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134233">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vkBYfCclLHCG3owrx7rp-uRBKtYDQyOVeP4sDDkk7V3bPidfcNfb9jcNRXr7CWMtQZ8JIBVnr9Cr7s3tnd3nm-KPWumy-6e_o4B52jvo4M1lwjsTgzCH5gwGfPz7eXX48O2DpjmLczrFrLwOm3N8gUSPek0Buc0UlX6fvuncKWOjYsSD3NS84v3UWBu-we50o0eX62UW7D7xSTdfbgwwdVADW0a3jGkwgcvtgwmzIa_KSbR7ICluCpRaC24K6i5yVUeVyH_rYx6KkCLY8OEuv99MmpAnjVSLNhO4Rckn6mvtbmo6R7Q6w3adHzyeIICDJeTCTzoBwe-422b6iTs0-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
محمد مرندی: ترامپ برای هفته‌ها مخفیانه در حال برنامه‌ریزی حملات هوایی گسترده و تهاجم زمینی با حمایت دولت‌های عربی بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134233" target="_blank">📅 23:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134232">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/134232" target="_blank">📅 23:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134231">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLLbDvJLJSQ3ixzWV5C0rttgz3UnqSvsLD_nAnNViD4YCb4rFfwTUJBOMeIGqkdevozb1wfMKZfIbf0YM6BD3ZrBu80Ma00dQDQsWmPC79pRepN0BaGedC-E0Ta9su1od7ivp3D43hKRHEYS5W7jjue-jyulMXEhegFJLFbUn72YpyvtOseFGdAWnrcxAoF2iY-lStwhVRzg7G3lvlOrBbYQiur9LWGC9M3-jnriXAMTYDAqmPWutuAAzzad3aFX-WnWhoG-773F6I9kPrt16wDFhkk39DdWyhTXsRBCW1pLbkHuGaKuebZR8Dbs1U5WczqXKZFeYG7XtqHzuji4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله اسرائیل به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134231" target="_blank">📅 23:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134230">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
هم اکنون تمام واردات و صادرات ایران از راه دریا متوقف شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/134230" target="_blank">📅 23:31 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134229">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
فوری/محاصره دریایی هم اکنون آغاز شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/134229" target="_blank">📅 23:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134228">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ایرنا: همین الان بندرعباس رو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/134228" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134227">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htF-LKZgkBvSYHG7MPx29p0oVylb93TTCYzePbZnysLIltFT-LYxGEam_15mhdApfKhv5PXrZcsYMOm4ojwcpL4GZQSIjCXi3vSkd8akXA0CAJ3XqLuUxUct6QR7PoxhyywME437bk92kXa8WaPqWIwCR4BV7FO5fN3BTVeWroCNaYYGfiPXBMZJHUyMty89fUuN18opoDbnF-iwCP3-9enntHGvTAqkY55bMYR3En15S0Iia8S2DXcBrvnvNUTZY5Ecb9oxFpV3Kr5RFxXvxIFE1Gmh2zlZQPGEE5_6VWakZPf2i90W8E8Ko0bqsUBF0nLg5x7uRR5lY51kMEIn7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا تحریم‌های جدید علیه ایران وضع کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/134227" target="_blank">📅 23:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134226">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ab_HCG9QRcCwfmU-0pCY9o134ALXGHgwG2-bkD6VqnG1gWaBgWCSuM3zTSLEeZTkx05mRnZeBJCxpdZVIrVtIb_Dsi_4VNQkZU5K_-KhVBIptR4EClYOcwj5kOtBS8uyagl0Mrygj-95zq_vp4i_Q8Etgzk8LvUcbUh8ehViAv-A6DjvsTlBfGQVn-slTyh7z601yQtuM1hYQVIhGZhM2m7cNhQbfNTAVX8mT_dehlkxwmaTq1D2-RpjwtdiHAEoqL7pIL8ehLU5dwt7UUnf0nr3t9AgUReSRz8BSx847wt9EjgK7dzIh2mjiP9dOtKAopwJsp1eOelUE8pN_zFZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/134226" target="_blank">📅 23:28 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134225">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
آی‌۲۴نیوز
: مقامات اسرائیلی معتقدند که ایالات متحده در حال افزایش آمادگی‌ها برای یک درگیری تمام‌عیار احتمالی با ایران است، با منابعی که با واشنگتن در تماس هستند و برنامه‌ریزی گسترده‌ای برای بازگشت به درگیری‌های با شدت بالا را توصیف می‌کنند که ممکن است در عرض چند هفته رخ دهد.
🔴
یک منبع اسرائیلی گفت: «یک جنگ وجود خواهد داشت. تنها سوال این است که چه زمانی.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134225" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134224">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✊
عرزشی‌ حرام زاده، مگر ۴۷ سال شعار «مرگ بر آمریکا» ندادید؟
🔴
حالا چرا نون رو به نرخ روز می‌خورین و سکوت کردین؟
🔴
اگر می‌تونین و اگر به شما اجازه می‌دن، یک تجمع ۱۰ هزار نفری برگزار کنین؛ میلیونی هم نخواستیم. بعد همان‌جا شعار «مرگ بر آمریکا» بدین.
🤔
البته بعید میدونم چنین مجوزی به شما بدن، چون این روزها شعار مرگ بر آمریکا دیگه به نفع حکومت نیست. همینقدر ترسو و بزدل هستین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/134224" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134223">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گزارش فعالیت و قدرتنمایی جنگنده های نیروهوایی ارتش برفراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/134223" target="_blank">📅 23:25 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134222">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/134222" target="_blank">📅 23:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134221">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
انفجار در بوشهر و بهبهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/134221" target="_blank">📅 23:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134220">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYDgCrFIIhKJgqMx__pa-klcxIUgMxLl1zqVHEsIB1yxl2j9WZ_JLRtCCS-L-wylDrXmrZtkG3U9ThtYw2G_w_jC3SPmDxlxL4DalqBGz_4UNzxwZMvv8j6Hxkr-D8Fvo8BoITGO5aVFrNUpquG2Si0P92H7ZPBjFRqDjI_-X-S27QiUYdwZrdKacpJsiuonuEYCAzw_Ijh-_PebfpFWIh0OlxHIhDd_0Zk3VUeNVskBQDO3H4XNB-FVRlVg-FcClxQpfhGmbLufvzzWuPyW9VPrfPZFuQ08lkJ7gnsqDUQw5IKiU53zkKE7m-_J1MPKf2xHHTRZ9Q3yHLvZuFNR5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💔
عکسی قابل تامل از زباله گردی یک هم وطن
🔴
اما دغدغه یه سریا انتقام یه نفر به قیمت نابودی زندگی ۹۰میلیون نفر
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/134220" target="_blank">📅 23:20 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134219">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
دقایقی پیش حداقل ۲۰ انفجار در جزیره سیریک در جنوب ایران شنیده شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134219" target="_blank">📅 23:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134218">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
غریب‌آبادی:
یک روز پیش از سفر به عمان، حدود سه ساعت با فرماندهان عالی‌رتبه نظامی جلسه داشتیم
🔴
در عمان درخواست ما این بود که مسیر جنوبی عبور شناورها به حالت تعلیق درآمده و موقتاً بسته شود
. در مقابل، با مشورت فرماندهان نظامی که مسئول کنترل تنگه هرمز هستند،
پیشنهاد یک مسیر جدید برای ورود و خروج شناورها را به طرف عمانی ارائه کردیم.
🔴
پیشنهاد ما این بود که نه از مسیر شمالی و نه از مسیر جنوبی استفاده شود، بلکه شناورها از این مسیر جدید عبور کنند تا هم امنیت تأمین شود، هم از بروز تنش و درگیری جلوگیری گردد و در نهایت، همه طرف‌ها به اجرای تعهدات خود بازگردند.
🔴
در واقع، جمهوری اسلامی ایران در این مذاکرات نهایت حسن نیت خود را نشان داد؛ اما در عین حال تأکید کرد که
استفاده از مسیر جنوبی، تحت هیچ شرایطی، برای ما قابل قبول نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/134218" target="_blank">📅 23:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134217">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8voIILuuUyex1KxFBRGaDHrOhLiBPp_LH1ksMsxYkf5rm3dj0xvxosaFyZkv_6eJMEN6c8sUp523LTdY0aSIfKiKRkRJAZ0Zm8oSKYZ4Rm7OPqokYo9P4vQUG0-KP8jkGvsOG9uVWHcz7k699zTG30bWeuYdlygymNpv79ldSWUfLwzr3qV0lPCzLkK6lsaR6-dQFzrxS7gisADPjjhnvFROU6F8si6fH3NjwVUZiRBJbrfMIEgRW__pjlTa_hlGG783og-iqkvRqpIfmAVcRObuZ61jFePT2V2pH5jBaBECUFmSfMRuqlHG5GA-nKJUchrteVPGhq8wElaizxEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: محاصره دریایی ایران تا ساعاتی دیگر آغاز می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134217" target="_blank">📅 23:16 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134216">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134216" target="_blank">📅 23:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134215">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/jYXDsZjaY4bubKHwUbXT0qmwgrOGMscEw9hg_OLRXRMIzyP_uhP55VWT5mCllptCyRttzppi5dupv6zo2hzFLu73El409aKay4uX05sV-5bNzp4qFtdIecyzR71C9XSdm70PM65WUppviYK5NaKffGNyz5dGkBk9jgc9XLOnSsP9MbuGDIt9AN8EuCpRdZL61vv-iEm3rAMVWzNgyEtMhAU2bkM9az1nzHl9zdyEko7NPByeSGol_Iycn4kiLTm9Khg19ZfogJDhlAvZ7Tj6cYF7yc9sQljhrvh3aSCX5lejHWfRGzHVByiwvCwQKSCa-JQXKsIVDO-hKAVi8N3yfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پخش زنده جام جهانی ۲۰۲۶
🇫🇷
👊
🇪🇸
▶️
کیفیت FULL HD
▶️
رایگان
▶️
بدون سانسور
🎥
شروع پخش زنده</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/134215" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134214">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
صدای انفجار در اندیمشک
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134214" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134213">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
صدا و سیما: دقایقی پیش صدای شش انفجار در بندرعباس شنیده شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134213" target="_blank">📅 23:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134212">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McwO1bnHzAe3qZ-JHc3uOceqLnlvUiZiB8qA3-f0rfQ5loHRAwiGZnuZv0hi6KgnBdUpwoRawnYgmUnblI4QiT1I3ddfghPT_ffApPBgyVzvmSVz5ce4A7L9Xg9TCUJ_D8bscjOvSTarkNVjA8biQVDcDEnt5uVjZrCalI8EmIkqssyupSDs8XjxokYYGj9qB2yin1VW5kQlKn32pDGg4heitX63kZYBcVUZn2njj-X-NIe8qGUSD-j5VE-4SLr7jjkdqH-NnhsL1wVOisCIvC5BBAwmy7Ui4nt1MjhmMo48lWXbVwjE8c2K7_gV5sAd3JNH-iWeE-FE8ySHMwiAUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طالبان نماینده ی بوکس زنان افغانستان رو با این وضعیت به مسابقات جهانی بوکس فرستاد
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/134212" target="_blank">📅 23:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134211">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">✊
عقل عرزشی حرام زاده
🔴
18 و 19 دی تروریست ها مردم معترض رو کشتن.
🔴
یکی نیست بگه اخه بیشرف پس چرا 47 ساله مدعی امنیت بودی. کدوم امنیت دقیقا!!
🤔
یه مشت دروغگو وحشی ان که فقط بلدن پیشونیشون رو با مُهر بسوزونن تا رانت بیشتری از حق بیت المال بگیرن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134211" target="_blank">📅 23:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134210">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
صدای انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134210" target="_blank">📅 23:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134209">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/انفجار در خوزستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134209" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134208">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری/انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/134208" target="_blank">📅 23:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134207">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41839db9d9.mp4?token=v409y65gHMs6Mms2fjCeF7thZUwPLimOuFT2E7EUDogTFQoBvflS_th0LqrX5gW-gXZ7pI1_-raAVU0HdOiJabX5IXfhthoAl5wCUyHrhnTg1UBLG80QB6v0aU6fzLCxlWw61I1K52MZDztRadZSGE72-LbWoOVWTe8z3W6DXhnozsgtrDwIiFHNap67bbDZ0rLU6_DQ53QGGbIc5vDLAJog5GMk04g5D1Fq8241ewjcGylwdzLJLwMNLqM0kL0SbGn_PJQnf_Z6lmDtt5ufIV96dyGKN5Lm4KUDVHhmLSOrE0T77ZNWsfkxJwrnE7mIWqbutiOLu3pSxO0IyaFzNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41839db9d9.mp4?token=v409y65gHMs6Mms2fjCeF7thZUwPLimOuFT2E7EUDogTFQoBvflS_th0LqrX5gW-gXZ7pI1_-raAVU0HdOiJabX5IXfhthoAl5wCUyHrhnTg1UBLG80QB6v0aU6fzLCxlWw61I1K52MZDztRadZSGE72-LbWoOVWTe8z3W6DXhnozsgtrDwIiFHNap67bbDZ0rLU6_DQ53QGGbIc5vDLAJog5GMk04g5D1Fq8241ewjcGylwdzLJLwMNLqM0kL0SbGn_PJQnf_Z6lmDtt5ufIV96dyGKN5Lm4KUDVHhmLSOrE0T77ZNWsfkxJwrnE7mIWqbutiOLu3pSxO0IyaFzNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
جلیلی سلطان کلی‌گویی‌های نامنظم: انتقام باید به‌شکلی باشد که مردم از آن راضی باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/134207" target="_blank">📅 23:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134206">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
دارلین گراهام نوردون سوگند می‌خورد و جای خالی برادر متوفی خود، لیندزی گراهام، را پر می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134206" target="_blank">📅 23:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134205">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ps47ADl7Z4GQAh2wckwz8pKMugsNlbUFBUCOYxde0bmktCQh73bdgz5fEvwzTeW-eZIRAEtnIdGCXJJ2IlLeL9iLHDzECZLZAXmHQmP7Zh9TGBgVG6Sxq_QNFviy9dUH3Q8aZWaG3Qhq3ibVU71IQXUfy3L4SKHsD2DqdQ2oUi6JdnLIAJ76QWR_e4P0JJvbcOpK-Q__elUDk5oXTTG7ddIqNYtmaTVG1HpnScREiyoeZSc2Wdpct1e_B7QamhKyhIBXcNjY9D5mIeV2MyUVpo5ZSmZNE03W50l9_tQ6QWc1EiVzsx70qDUZpKAuGWRYdn6fallbR80dFW9flQGY3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام:
امروز، ساعت 15 به وقت شرقی، نیروهای فرماندهی مرکزی ایالات متحده، دور جدیدی از حملات را علیه ایران آغاز کردند تا به تضعیف توانایی‌های ایران که برای حمله به کشتی‌های تجاری در تنگه هرمز استفاده می‌شود، ادامه دهند.
این حملات در حالی انجام می‌شوند که نیروهای آمریکایی برای از سرگیری محاصره دریایی بنادر و مناطق ساحلی ایران آماده می‌شوند. این محاصره از ساعت 16 به وقت شرقی آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134205" target="_blank">📅 23:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134204">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pL_apyoCzoYpw3uuyacpB1B1YdYtnn1nQgWSOWK7nP5YH8WGOppChMz8fIMZ5rY1VnlLWxNXzQWU_Z2Wyg9HraS3hVujihlae0jYfF1mF0iSfOxhUtiayakiKuuO7Q9PWUEkHrpiLCpT-t6DjrpZpg-iUwgewrRd1qxkx81CfTfHD1u08fmEmZ7w_EXI6L_CXXGvWMZ78-AtfAuQRoQdt-kb0aAp-wFVHWXJ2wekHcLazMiq9bBc9_WdQvDCDAnFcZij9X2yJ39JU8J3-Kvm5RRZqhBxGXylPfzRA6wumCw0zSnM7xRw2CcMhEeifJV67JiURgAphy9nDz86k8DrWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا چند موشک از کویت به سمت ایران شلیک شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134204" target="_blank">📅 23:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134203">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
برخی منابع از شنیده شدن انفجار در حمیدیه خوزستان خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134203" target="_blank">📅 23:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134202">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
بی غیرت تر از عرزشی داریم؟
🔴
برای غزه، برای سوریه، برای عراق، برای هرچی غیر از ایران یقه میدرین ولی حالا که جنوب ایران رو دم به ساعت دارن میزنن لال موندین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134202" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134201">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر امور خارجه:  واقعا این انصافه؟ حالاچند کشتی تجاری دچار حادثه شد و از چرخه خارج شدند، اما آمریکا در پاسخ بیش از ۱۰۰ هدف نظامی و غیرنظامی را هدف قرار داد و در این حملات ۲۰ نفر کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134201" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134200">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EYNfkDLb30puOjarbHawcnsCp1zWE-Pm0EORMZpFXPIoWD-IXbPP5Ez39AuUN7ipuReuXeGG2V-FtdCeEWEP6CUVOzvi5aOJVua-B4Wc870MwMnLNh2WaclEEYCwOTqaLCxIrVGzJuFcHENkFcH_Qk3aL1jhdYG228mOTPDRiUdBsZfXRFiplXc0emgqrVO-G8JXm7pIsYF0w2Iw5inj2FnxFay5T5YBbOYMlhxj2FHJ_1FS6dVND_3AlzJOWagHOQAqkuwM6a0ufUhj3cIeYNVhlEJ4-fW7FYovejya09LiNLsyP06PaA-4Uj83ktHQwahKgArCjKkH8ThEeUOT0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غریب‌آبادی، معاون وزیر امور خارجه:
واقعا این انصافه؟ حالاچند کشتی تجاری دچار حادثه شد و از چرخه خارج شدند، اما آمریکا در پاسخ بیش از ۱۰۰ هدف نظامی و غیرنظامی را هدف قرار داد و در این حملات ۲۰ نفر کشته شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/134200" target="_blank">📅 22:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134199">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ارتش کویت:
یک شناور متعلق به نیروی دریایی کویت امشب مورد هدف ایران قرار گرفت که در نتیجه، چهار نفر از نیروهای مسلح مجروح شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/134199" target="_blank">📅 22:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134198">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
هم‌اکنون حداقل ۵ حمله هوایی در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134198" target="_blank">📅 22:56 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134197">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd811093e.mp4?token=vyiauV1E4X1wYm4oORaXX3_NDVCX6TLX2Yjk3LZUm3QUc78fstHJXMDLc7oWX3SAVgURDb4XlHQh_V3XdHQvCbq4CUswxUNwpO0YAPxw4_yWvWrYlpRetzSGuhQ2gyDhd1virwgi67FKORKbNEsyLLKI9bGX2moyHX_mIaYIYzwj2iMMhuDS_no42f0DHaqQQEmGhG7pPZod9QepVNEb6KvNSkiB2OfbSNKqGIVvL4kVF4Z-8xEaqFCKbfbLcGZ8f_5W3F_uKMef9TFyhzBXYfNFGeGQzAQVGUyaUTHY-U0vBiJFhCMmui2fTUM2hPp0PY15chlzQVsU0LLpHimaEUSmWdfnYLMbXLDapGtE9zn94tPpdwVeGsFV9YQTuKIqBAsz8SDgAx3GUcJbebx_hkb7rMSnoARoUeAE9cskmqk2Busy-62r6xBO1WDK5Lje0MfRt8LQGHZEB2aaLBNd320MPzhlQ_4Jm7Pd0SXVMOOAGt4t829RsL19gUkuAi8SOKEEpGysAHOUK-o3dv9sjEeeE3xdc3zur7qRI1twUH8xQNtDXOPlw7ltWky3It56ernXc0_2CnnNSsktNKugfNDE7JXIEFBNri8PSn0AWwkMsk1n3pTweWpb4q9kbkvV2TPKdbZsUZxhg4labBkGh_CMhfCnFhUWh6MXexUhAt8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd811093e.mp4?token=vyiauV1E4X1wYm4oORaXX3_NDVCX6TLX2Yjk3LZUm3QUc78fstHJXMDLc7oWX3SAVgURDb4XlHQh_V3XdHQvCbq4CUswxUNwpO0YAPxw4_yWvWrYlpRetzSGuhQ2gyDhd1virwgi67FKORKbNEsyLLKI9bGX2moyHX_mIaYIYzwj2iMMhuDS_no42f0DHaqQQEmGhG7pPZod9QepVNEb6KvNSkiB2OfbSNKqGIVvL4kVF4Z-8xEaqFCKbfbLcGZ8f_5W3F_uKMef9TFyhzBXYfNFGeGQzAQVGUyaUTHY-U0vBiJFhCMmui2fTUM2hPp0PY15chlzQVsU0LLpHimaEUSmWdfnYLMbXLDapGtE9zn94tPpdwVeGsFV9YQTuKIqBAsz8SDgAx3GUcJbebx_hkb7rMSnoARoUeAE9cskmqk2Busy-62r6xBO1WDK5Lje0MfRt8LQGHZEB2aaLBNd320MPzhlQ_4Jm7Pd0SXVMOOAGt4t829RsL19gUkuAi8SOKEEpGysAHOUK-o3dv9sjEeeE3xdc3zur7qRI1twUH8xQNtDXOPlw7ltWky3It56ernXc0_2CnnNSsktNKugfNDE7JXIEFBNri8PSn0AWwkMsk1n3pTweWpb4q9kbkvV2TPKdbZsUZxhg4labBkGh_CMhfCnFhUWh6MXexUhAt8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
گل اول اسپانیا به فرانسه توسط اویارزابال از روی نقطه پنالتی:
@AloSport</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134197" target="_blank">📅 22:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134196">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYa7yN9v9byRl76diaxNnleqJxnKz830oI47dnPFqh2B1jjRS13K36N6Zvm4xqeDIcsYMOKsP-95sJiWKVhfMPTT7_rkah-577xp9GQzc8wooyU6D6YMi9ocoSm2Qkb2Z8Tm3VN9Kb6PaYJSmadXvUdvOuAp1PWkCCqjz5ko49yP0-cmC9j5yWvlNVXE1Le9WriuFmLZYCCYh2YuTjU62yK0j4WLEpSJoOUTE2mSORtcRE5otjAZUfM76jXxEutf7SnMw05uVkyAbB8D2G1rYupn6-AAtAnEnJ-9PUa2DfvJsnJwSzK0ndZ5kMmO2QD8hTkcmBn_V2u2JCt1HWgocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کیان‌شهر اهواز | اصابت موشک به مقر ارتش زرهی ۹۲ اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134196" target="_blank">📅 22:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134195">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86ee55e092.mp4?token=hSaxXj5xc4KfA940Bh8GS9kdqIp1POTIq-G-GL0JQu5xP5hWblO3kwEn1q5LIBIfcc2YXM1v7CoXx4Dj7WzABSbKJX8QrT5HZTSThP-VbUMJsQZqVdrZSTBn9qT0lwqrHJRMA6EeI1c_Zny0d1I5sj5m2-9dqxzVLztv_8oGCCSWMK22DxsqgcSsA1ILUel31PqHWL3jbRQ12ihCBTdRjj7TKJss1QQNJmU6sqWVYdQo6-vz2UhPSuJgWNtToaDIjEKaNCfpQoffyn4V15k3dhAFXJ5s7A3GCdzecDY1d53RslvOmmW8yXmF7l1oGgbfxuTPbldkyhIj_HPnP7YGZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86ee55e092.mp4?token=hSaxXj5xc4KfA940Bh8GS9kdqIp1POTIq-G-GL0JQu5xP5hWblO3kwEn1q5LIBIfcc2YXM1v7CoXx4Dj7WzABSbKJX8QrT5HZTSThP-VbUMJsQZqVdrZSTBn9qT0lwqrHJRMA6EeI1c_Zny0d1I5sj5m2-9dqxzVLztv_8oGCCSWMK22DxsqgcSsA1ILUel31PqHWL3jbRQ12ihCBTdRjj7TKJss1QQNJmU6sqWVYdQo6-vz2UhPSuJgWNtToaDIjEKaNCfpQoffyn4V15k3dhAFXJ5s7A3GCdzecDY1d53RslvOmmW8yXmF7l1oGgbfxuTPbldkyhIj_HPnP7YGZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش اینترنشنال: برای یه لیتر عرق مجبور شدیم ۳ نفری پول بذاریم روهم، عرق شده لیتری ۷۰۰ هزار تومن، مزه هم یه میلیون هزینه می‌بره، دیگه نمیتونیم بساط کنیم حتی.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134195" target="_blank">📅 22:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134194">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
شنیده شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/134194" target="_blank">📅 22:50 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134193">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoSLvjZDIdDqxl02vk3wspMoChrKdRBR5FEhdY1O4AmWG0ZSvgdH8aupUYFI5Su90Xh8vqKDwewSWMMGbymGcTP-Oypxzu6v2dPaUTFgNjGZjxlhfou2ORBQklBgISNOGfFTdkmFOz3ETJe5F8vHo02IM3KcQhFCEoHh-ZKo8oliTHdhvz9emUac9SPxI0r3NB50ezxo8mKcyu1DbH_VeHc5Fsbp0QLfTX-I_-oBIlJ86uT56atsQbOgMwqt15RgCwqJGQj6v8V52TMxqt8R7xnTjz7O7_Dd18nJK_fJ6-UJwPywNfOKxKUZEZ1Ld1B5zDjMTPAsiUGyjRI90PfBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش کویت :
پدافند هوایی امشب ۱ موشک بالستیک،
۵ موشک کروز و ۳۳ پهپاد رو منهدم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134193" target="_blank">📅 22:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134192">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2495adb8ba.mp4?token=PfpQo8x-_OPHbk_g3MTNdjpKKA7MLEqTGk2gr7ccYALxYDQBdNJ1ATMKMkbEN_qS_IcY6vq_jR5-B4i9DVUFwcSS5XQSHo8IBABCfkf2o86UXAHN9pR5abUySxGa_KOSkNbJYs2IYIA0HqcrqgJffrHICkqcUxGQu0kccBFbDI_d1aoqY0zKu4vgV9gNqYmNKiAUszaIsWzPxdWN6syMcWPlqMWj8O5vpV0u18kGwVPJcOA0CO_rfO7NEstEqoE0pI62OT8q6G6ecpceBuv_ty9bIMbeJr-9JZgCn-E9p9xs9cyZ1h6KRRJhCPN9dZrjxcOOD2xxUVhuGLCrcoXO5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2495adb8ba.mp4?token=PfpQo8x-_OPHbk_g3MTNdjpKKA7MLEqTGk2gr7ccYALxYDQBdNJ1ATMKMkbEN_qS_IcY6vq_jR5-B4i9DVUFwcSS5XQSHo8IBABCfkf2o86UXAHN9pR5abUySxGa_KOSkNbJYs2IYIA0HqcrqgJffrHICkqcUxGQu0kccBFbDI_d1aoqY0zKu4vgV9gNqYmNKiAUszaIsWzPxdWN6syMcWPlqMWj8O5vpV0u18kGwVPJcOA0CO_rfO7NEstEqoE0pI62OT8q6G6ecpceBuv_ty9bIMbeJr-9JZgCn-E9p9xs9cyZ1h6KRRJhCPN9dZrjxcOOD2xxUVhuGLCrcoXO5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
غریب‌
آبادی :
آمریکا با لغو رفع محاصره دریایی ایران
- همه تعهداتش تو توافق اسلام‌آباد رو زیر پا گذاشت و عملاً این توافق رو کاملاً بی‌اعتبار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/134192" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134191">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🤴
رضا شاه بزرگ نه تنها زیرساخت‌های ایران رو بنا کرد، بلکه با قلدری جلوی آخوند های مفت خور ایستاد تا فرهنگ پاک و اصیل آریایی رو دوباره زنده کنه.
✅
@‌AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/134191" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134190">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👑</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134190" target="_blank">📅 22:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134189">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/لشکر 192 اهوازو زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/134189" target="_blank">📅 22:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134188">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/سنتکام: دامنه حملات رو افرایش دادیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/134188" target="_blank">📅 22:37 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134187">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
حدود ۱۰ انفجار در اهواز رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134187" target="_blank">📅 22:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134186">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/انفجار در دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134186" target="_blank">📅 22:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134185">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/134185" target="_blank">📅 22:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134184">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Azrrd3pGwG5971pUhHqnVqjWD6m49CoXbX2A3ySu4xPhursCzdQjznQ97rb3o_49Sp_XJm0arSaOlnEAjKUhFKp8dOZ00Pj2cdlrS8W5Tp2tdD9XupIhgL3Q2XqBzNwFKb9ggssXcC0j-jHmbBqqvF02UyrS6hwjLHyRhdM9MzzhmExHnjUd0FKuaHJHFGzPOQkaHMjgGiw82oUOh8k8TKaNfp9bZAKiXCMhISvmz73hWntr3g_aCNEo4o5BgJbPdlBvWpe06dKqYgTBsvyElveCFIY5kdJFhWRkyMIDRJ1eRQC76Vn6uy461sSo_XEJ_56er_o8X-InNWGiXcEmOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
زیر 18 سال نبینه
‼️
بلاگر دختر و معروف عراقی که فیلم خیانتش مثل بمب ترکید و توسط همسرش تکه تکه شد
◀️
مشاهده فیلم خیانت بدون سانسور</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134184" target="_blank">📅 22:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134183">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔴
فوری/سپاه پاسداران:
تا زمانی که نیروهای آمریکایی در این منطقه حضور داشته باشند، "حتی یک قطره نفت یا گاز نیز صادر نخواهد شد" و بازگشایی تنگه هرمز نیز به تعویق خواهد افتاد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134183" target="_blank">📅 22:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134182">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iw_rNIt0p7faQ5PW0ArxX1BwrFh9WeTw_PGw5vNKXCLdTUdEHHBZdSCzAPKYJ6F2S5xAXdGVBN__jmYJXOm8otfDIAvmKn9MjELOfy5OL782o61fDr_bIzFhe8RlKoJoRnAci4llbzINxA_7nJt-9s4gpVxhILQuOQDmjPRBbAovesrjnW2mGJ1IKs1FKT25dZbjldXScSboXNakB1VNBec__6xgheNHOWqCjkm6f3jYNeHaCc47c5-Z7i-EnmJfDcrOfyOMYfVapp6fCfRsWh6sQaEG_6HiLCCOOITFjd30ZYDsBdDvd62zbCz9j7_epaiFFHva1tDkQ5GeEHQbpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فعالیت پدافند اسلام آباد غرب فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134182" target="_blank">📅 22:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134181">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jq-FJHfGtNetNYXWZPh2GU0vQgeGd8BwbbI142Ocs48Jf98zgK7R2vzdflKhqzZrQd9JHevnFMXEHZ5HcPlikuZRw_Rh7F6Ct6u4wrTUsEh_uTbHOxaFOiaE5DTPIiTuhKabFf2-d_uyRb0x8Yixf3f9hD2kz25eusOLlQD5ES2nC-76Uuay-7WwhZpgZb4XTfeEFzGLYwDwEc2tslh4tkpUw43hqlzUCQnphJHUHmLe7egXDQNuW1RjhfzqRrF3l26EcZ085mqFN2iWbmpj3DlGZLTA9vW1QHjOamxVLv5lq89vOh68y91ZkHnlkWqPczgG_ez1JwGeSJkGf2a_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری
/
غریب آبادی معاون عراقچی: هرکسی که در داخل به ما بگوید برگردید و شروط را اجرا کنید یا تنگه هرمز را باز کنید حرفش برای ما اهمیتی ندارد
🔴
دیگر متعهد به تفاهم‌نامه اسلام آباد نیستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134181" target="_blank">📅 22:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134180">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/by6Ig35tEiXhLZ95KmnbKAduWFOkZ-szRRK5gNpDpe4K_nmeUmtrFY9skQ6GN4u-ouYCLgSLqfl0WKzoEMy-tvAl3EA-KH3NPXNeeBHyQWXzlr7TkXeZf3WyINfq3WbSgUARE5inzxNXQc39TmJvMWOI8j3xkSfptFkaOCX_KOWYj7tGTP423oktaRwHnsOiyXOKV3ojvWrqhc0ZfBNwpm_mQiu-37fDKKWlg8wqVffWMP76cTGn6hlwDlCj-h742F_BDaAmamNb38rVWND8KGd1cyHtFglNaHU5PYFaiy7RM00F4vz90BMRkDSw7cr6N8cRD53hK2vezu1BCSF75A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پخش زنده جام جهانی ۲۰۲۶
🇫🇷
👊
🇪🇸
▶️
کیفیت FULL HD
▶️
رایگان
▶️
بدون سانسور
🎥
شروع پخش زنده</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134180" target="_blank">📅 22:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134179">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
مایک والتز، سفیر ایالات متحده در سازمان ملل:
حوثی‌ها، یک سازمان تروریستی اعلام‌شده، پیروان تهران هستند. آن‌ها از دستورالعمل‌های سپاه پاسداران انقلاب اسلامی (IRGC) آموخته‌اند.
و این اتفاق می‌افتد: وقتی ایران غیرنظامیان را ربایش می‌کند، حوثی‌ها نیز همین کار را می‌کنند. وقتی ایران پشت سپر انسانی پنهان می‌شود، حوثی‌ها نیز همین‌طور عمل می‌کنند. وقتی ایران زیرساخت‌های غیرنظامی در سراسر خلیج فارس را هدف قرار می‌دهد، حوثی‌ها نیز همین کار را انجام می‌دهند.
وقتی ایران شعارهای «مرگ بر اسرائیل» و «مرگ بر آمریکا» را سر می‌دهد، حوثی‌ها آن را کلمه به کلمه تکرار می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134179" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134178">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/NibiqQ-W_id63cxKrc9kpbciNrKNAGyM4Xs32ErsNIk-9oXZUiwJOGrS5Wy6B0lh4LBnDEh3SgMc57mVoaPyreFzkQ5B0wVt3Je7bkfUigLywo-_3Fjd7g1ODOSEZ5GEARrKyo0ihZx6H_c0Ixjl4Xjm30ufmw2nUlsUDUoeHIQOtgw2X8QLbCrbQKczQpKck9EyYOfCngCSEpQJspgr240BVLbzUGX3KxS5gnjjF3N0izCX8MZRWHbLEfKFtQEzNzwhtSs1iWuF2W1Yw8KPjO-O8aDwaUjochTACmrCyBXQ1-hjZa8OBL997I4OnPj91lYNDg5rS6keSvOjmIcUZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن
😁
به شدت داره وایرال میشه و همه دارن امضا می‌کنن!!
اینم لینکش
⬇️
https://www.karzar.net/333344</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134178" target="_blank">📅 21:54 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134177">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
دقایقی قبل نقطه‌ای در جزیره قشم مورد اصابت پرتابه‌های آمریکایی قرار گرفت که گزارش تکمیلی پس از ارزیابی‌های اولیه اعلام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134177" target="_blank">📅 21:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134176">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
آموزش‌وپرورش: حوزه‌های امتحانی نزدیک مراکز حساس و نظامی جابه‌جا شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134176" target="_blank">📅 21:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134175">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
به گزارش پرس‌تی‌وی، وقوع انفجارهای پیاپی، پایگاه‌ها و تجهیزات نظامی تروریستی آمریکا در بحرین و کویت را به لرزه درآورد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134175" target="_blank">📅 21:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134174">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
سی‌ان‌ان گزارش می‌دهد که حداقل ۲۲ کشتی تجاری در ۲۴ ساعت گذشته از تنگه هرمز عبور کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/134174" target="_blank">📅 21:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134173">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
اکنون وضعیت در بحرین عادی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134173" target="_blank">📅 21:30 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134172">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری/ یک مقام آمریکایی به ای‌بی‌سی نیوز: نیروهای آمریکایی در حال حاضر در حال انجام حملات هوایی در ایران هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134172" target="_blank">📅 21:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134171">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
وزارت کشور بحرین: «آژیر به صدا درآمده است. از شهروندان و ساکنان خواسته می‌شود آرامش خود را حفظ کرده و به نزدیک‌ترین مکان امن بروند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134171" target="_blank">📅 21:23 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134170">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJCDH0Y_c-nvJ3BLtC_HPdm107ijbZdKOXtplf5_utFuwl6QOuovTVINZzZ162S92h2zyiSiKOTlnCs01J4aC0-lsyhy0tI61cdgC4RQ5xsXtPDa7Cj64AJJ-fGYR2EuaX3kfxdkuv05hLZSd6W5Eo8vdNp70e38JQtsR2Bd1k2DSBBJmTYTFyI1thcjY0Xi8r6v7GhgjRIfvUAkZlyGueoMJcMegICNfAclKEcH178aIOJ-e9ttSMFKLq65_GmOgUn75ldJ2z05HApAFe0-sUsxpbI-GKYANkoCsppJQitFJjCCC8vFjrvuhnPRqUrW1K0uWy4g3Fr9hlBo8xbDrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ا
نفجار گسترده در جنوب لبنان؛ حملات اسرائیل در ساعات اخیر چندین منطقه را هدف قرار داده
است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134170" target="_blank">📅 21:22 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / پایگاه پشتیبانی دریایی بحرین. صدای انفجارها در نزدیکی پایگاه شنیده می‌شود. احتمال اصابت وجود دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134169" target="_blank">📅 21:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
فعالیت سیستم دفاعی C-RAM در بحرین گزارش شد. این بدان معناست که پهپادها به اهداف خود بسیار نزدیک شده بودند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/134168" target="_blank">📅 21:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c346e03d.mp4?token=mrtN_b1V1hjlt4gZd1cNBf3OdL-A56dXxJs_Adh16GXKlNIkHM4F89t3L9gV6JE3IPv5fcAloH2jDw_K9P59fytDf1Nwx1UmaS9A6knzlrhgipW_I3fnN9cWjKB_rBTFcfEErBB2A8hNNiSaSh6Tpt-btRNEcVVVNX3OpvQUjhG_HO_cTox1JuQNtU1gP7FF7VRVJ52AXaRYnIf7D3eqAvGWL3mvVW1cuwfWt2akvGHsHnCE6uSoX-pPPl0etzCOFy98tJ0aCJASxD7exXLb7EsM4KGGzXcu1szn3GbZnDJnAZ8eHZaGLplD9i3FKKa-RIKq5Q74XIrBdZMn7wpH-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c346e03d.mp4?token=mrtN_b1V1hjlt4gZd1cNBf3OdL-A56dXxJs_Adh16GXKlNIkHM4F89t3L9gV6JE3IPv5fcAloH2jDw_K9P59fytDf1Nwx1UmaS9A6knzlrhgipW_I3fnN9cWjKB_rBTFcfEErBB2A8hNNiSaSh6Tpt-btRNEcVVVNX3OpvQUjhG_HO_cTox1JuQNtU1gP7FF7VRVJ52AXaRYnIf7D3eqAvGWL3mvVW1cuwfWt2akvGHsHnCE6uSoX-pPPl0etzCOFy98tJ0aCJASxD7exXLb7EsM4KGGzXcu1szn3GbZnDJnAZ8eHZaGLplD9i3FKKa-RIKq5Q74XIrBdZMn7wpH-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مهمات خوشه ای شلیک شده توسط سپاه در آسمان بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/134167" target="_blank">📅 21:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134166">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی مدعی شد: ترامپ از نتانیاهو خواسته نیروهای اسرائیلی را از سوریه و لبنان خارج کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134166" target="_blank">📅 21:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134165">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سخنگوی ارتش: تنگۀ هرمز وقتی باز می‌شود که در آن ترتیبات ایرانی اعمال شود
🔴
مطمئن باشید دربارۀ تنگۀ هرمز حتی به اندازۀ سر سوزنی کوتاه نخواهیم آمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134165" target="_blank">📅 21:09 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134164">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/977fdbd2de.mp4?token=jIjv5D1-_meR5KiwgSmP3_FLxciLjtFUhD41htg-ErDzLeLymPmFCWof6G9ppgKlMBgKgEe7LBFBCtIpPudzowjeNAHMloHELcUWhpGA8HkZDeic04Zjkz-zEfVRe7p9U0CtwkbNeNBOXxlaEnambwHSLz_T9aNCKkjYys4EPmEYJs14IGxRWP-S_QrP8AKn9kgKzCP4fgJte7KBRo7JguWGTOsHk6ipF_h6tixgCIEi5cJdvRHmQxtr7EpDTQBzh-2orEmXMizSLHp_N6lScDsl-S3788ISbcDANKYd-nachrCDLPWGmNhDaiZ1jZFoBiOHi_RS7vv-oIFoy56Bfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/977fdbd2de.mp4?token=jIjv5D1-_meR5KiwgSmP3_FLxciLjtFUhD41htg-ErDzLeLymPmFCWof6G9ppgKlMBgKgEe7LBFBCtIpPudzowjeNAHMloHELcUWhpGA8HkZDeic04Zjkz-zEfVRe7p9U0CtwkbNeNBOXxlaEnambwHSLz_T9aNCKkjYys4EPmEYJs14IGxRWP-S_QrP8AKn9kgKzCP4fgJte7KBRo7JguWGTOsHk6ipF_h6tixgCIEi5cJdvRHmQxtr7EpDTQBzh-2orEmXMizSLHp_N6lScDsl-S3788ISbcDANKYd-nachrCDLPWGmNhDaiZ1jZFoBiOHi_RS7vv-oIFoy56Bfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
‌دیده شدن جنگنده اف ۱۸ سوپر هورنت آمریکایی برفراز چابهار
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134164" target="_blank">📅 21:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134163">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
بیش از 25 انفجار در بحرین شنیده شده!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/134163" target="_blank">📅 21:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134162">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
صدای انفجارهای بحرین به قطر رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134162" target="_blank">📅 21:06 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134161">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8vim3RQaxk4tUUdmp8uFYvcp6AsyId1uMjhK9_jwxSY1Q-CWbUu5H8bI31fn4LkdNvFRkVNLVpNnLWuZF-Lnuf2JAF4MWop-Pw-vFlu4N5ogOnQnL47-RoQqOIXNHnFluExoXTptwiSbqMORd2d9aPPOnUX1OZGSfKlsLoOdha--ijffMHOp3-H_ZWmW54fXnQyqAmecDXKeM2qVHTk7KDSqTSQaXVGqe7hyljlLUR4HpMLYWpDCpLMYttHj7RLlwarb0HwuQ7Sz_jYvBLcFg0_mierzPQRPdlssFG_LOYMbHYoYDA5VAJU-T46uhbBXOj7K6VcYTMfBzFTDfUqAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیماهای غیرنظامی عازم کویت در حال بازگشت هستند و برخی دیگر به دلیل حمله مداوم ایران وارد مناطق انتظار می‌شوند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/134161" target="_blank">📅 21:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134160">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
هشدارها در کویت؛ سامانه‌های پدافند هوایی فعال هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134160" target="_blank">📅 21:04 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134159">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=WI7lF2-UQPQCYx6faWCRgINAMYhEJMTq43Rp8HX4YlGVd-YEdhN_0XXF66Bz6hLWne3Ccg29Uam-V8EeOzWkrY7llRWhu9CyG1PcB30BACqSX1E5znCdm30aSMV3iJSBODftPwV2HN5r3m9pzsdhrHALR65I3quMeFfDOr9HIn3RmpCQPlUgG4kCMKJWTrFdaga75j3jx8NsrZiOkWx6xGwvFgw8yugvQZgLvA2dR2JaRLjMYswHeMfPYetZO7nIFV0_eOcAY9wNvwzp2gZ1E51rezBq1rpSeMxLd9iXHd1zNGIAYPuC7VTNjFIvAe4kf_FdFQJTy8AesXQfmMtj8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/346a1329e1.mp4?token=WI7lF2-UQPQCYx6faWCRgINAMYhEJMTq43Rp8HX4YlGVd-YEdhN_0XXF66Bz6hLWne3Ccg29Uam-V8EeOzWkrY7llRWhu9CyG1PcB30BACqSX1E5znCdm30aSMV3iJSBODftPwV2HN5r3m9pzsdhrHALR65I3quMeFfDOr9HIn3RmpCQPlUgG4kCMKJWTrFdaga75j3jx8NsrZiOkWx6xGwvFgw8yugvQZgLvA2dR2JaRLjMYswHeMfPYetZO7nIFV0_eOcAY9wNvwzp2gZ1E51rezBq1rpSeMxLd9iXHd1zNGIAYPuC7VTNjFIvAe4kf_FdFQJTy8AesXQfmMtj8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر دیگر از بحرین
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134159" target="_blank">📅 21:02 · 23 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
