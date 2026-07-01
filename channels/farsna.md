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
<img src="https://cdn4.telesco.pe/file/txYmQHHOu6jWbRhCp_AArcEg3lx8ScC8N7OsG_63nb_iwSVY1rDFcBqgB-7WW03NRRQ2CdVdQU0R95jwLCibiDr-PrQGKvA1PbK_sxzWOWcU54SJWSoMHaYRg6fjtmk_MYHbTOQ6LEPzvdOSq36Qo8mvrasTKjnx4ts62ydqV0FlzFAAgV8BTF3nQ5dY8oRl_zdAFrya3b94iEfulHWcZJD5x264H0B2Q88Yq4MNIrnhx8yibWqVUhijvJYT1ku3JH3XLzfjmuvoD17yjiZCmfbAI5crK6FizqKa6ppGu82v82rwV4cEL0N1ydGZLtHd5nDe3Owpvy9k3WlaEN2IJw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 17:41:53</div>
<hr>

<div class="tg-post" id="msg-445838">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd56ad542.mp4?token=flAn2m4Lw-0yqbY4TdjUz2XGvMB3SW4_YgQSZ9x-q1f2OaPHdj4KOf9rdwk7XRis0603_K1ZoSR9u7Z7Jlhk1tTtoXMhtX3Al1gU4AbKJy1iJOdeLxXdnsaHLfGZCEJwUBzAeRAE8v8k9Olmg9kXUv-hPr6KzIz4jjO_E4ZnHivLiTNaZDpNDU-v0V-YIxt8F38E7vKmDdmjhWUq2XeJcLmghAxl1I5ZrxOr8f-QQz4tBBiYtn3VOWF9qrgPi8JaLuLU25JJRZanXMsPcI8r3gjIyMfMvi8-HLS7UX0WJlvtfhw1K15f5yRGCHgFe2CdBkIO4Tl40Z5A-acV8BTWDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd56ad542.mp4?token=flAn2m4Lw-0yqbY4TdjUz2XGvMB3SW4_YgQSZ9x-q1f2OaPHdj4KOf9rdwk7XRis0603_K1ZoSR9u7Z7Jlhk1tTtoXMhtX3Al1gU4AbKJy1iJOdeLxXdnsaHLfGZCEJwUBzAeRAE8v8k9Olmg9kXUv-hPr6KzIz4jjO_E4ZnHivLiTNaZDpNDU-v0V-YIxt8F38E7vKmDdmjhWUq2XeJcLmghAxl1I5ZrxOr8f-QQz4tBBiYtn3VOWF9qrgPi8JaLuLU25JJRZanXMsPcI8r3gjIyMfMvi8-HLS7UX0WJlvtfhw1K15f5yRGCHgFe2CdBkIO4Tl40Z5A-acV8BTWDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کاروان تیم ملی وارد تهران شد
@Farsna</div>
<div class="tg-footer">👁️ 1.26K · <a href="https://t.me/farsna/445838" target="_blank">📅 17:37 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445837">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a1c6c24b.mp4?token=TRB-GtHdtZ6K0PVH1OkMX7z_2MHFnsEzZXNNpRyngLfoRstaCyHm20jeCHlOI80CU1RggAlYZ5l4Tog63QG1_U_XtlHbEGnVaghBuzP0doiIB-STBaZQFBjoNeNwHbwJLS9juCWE7i_QuejhIC2nMNjQMhUMvKwoWZmAVSADcudQXAAtcliQUqkthiVqhabcwwrZ8z5PmQHmWzp1ggxnMBvqmqf0O7vrq4UlbHvCRFQ2MrfKZTaiphpq8oCtO3igeWHywblwQDklJQ8u46eh4tM1zNGj1vwsjnX6L-Gm6-0NzlktkNVL9IsiZ6tfN9PPJvbRmvwEPcdi5JFstnit9TpnObrR5GZTAl4Yw5X8a8D8vMLVq5hjhEBD8P1Uri-bmRH08Yb8Qlgtsw_YiPT5S8Nip365fRA3oWRsovJy0Zam5YAhi0dmEs4WVeXEN_aDgFFQGJDMufOn9dbNM8i43HTUKMU6eq_edyYIahHW9xBfyxh4nAVARdToEsMhXRBUYv5_TsgalZprucKJlXSuY8SL4uw6IUbVU2nI5tJuy6msQOW-PmlQBq-KAdPdOQxffJ4v85_Q7-FjmLsWdVPHClyxgP9UkzyOL54y_P7co7ZI5GMTOHORuZB9U05isPCgoZzGDJ1BUAhXXY3_RhuY-gLKkr5FRjV5K6bQU2RLSK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a1c6c24b.mp4?token=TRB-GtHdtZ6K0PVH1OkMX7z_2MHFnsEzZXNNpRyngLfoRstaCyHm20jeCHlOI80CU1RggAlYZ5l4Tog63QG1_U_XtlHbEGnVaghBuzP0doiIB-STBaZQFBjoNeNwHbwJLS9juCWE7i_QuejhIC2nMNjQMhUMvKwoWZmAVSADcudQXAAtcliQUqkthiVqhabcwwrZ8z5PmQHmWzp1ggxnMBvqmqf0O7vrq4UlbHvCRFQ2MrfKZTaiphpq8oCtO3igeWHywblwQDklJQ8u46eh4tM1zNGj1vwsjnX6L-Gm6-0NzlktkNVL9IsiZ6tfN9PPJvbRmvwEPcdi5JFstnit9TpnObrR5GZTAl4Yw5X8a8D8vMLVq5hjhEBD8P1Uri-bmRH08Yb8Qlgtsw_YiPT5S8Nip365fRA3oWRsovJy0Zam5YAhi0dmEs4WVeXEN_aDgFFQGJDMufOn9dbNM8i43HTUKMU6eq_edyYIahHW9xBfyxh4nAVARdToEsMhXRBUYv5_TsgalZprucKJlXSuY8SL4uw6IUbVU2nI5tJuy6msQOW-PmlQBq-KAdPdOQxffJ4v85_Q7-FjmLsWdVPHClyxgP9UkzyOL54y_P7co7ZI5GMTOHORuZB9U05isPCgoZzGDJ1BUAhXXY3_RhuY-gLKkr5FRjV5K6bQU2RLSK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مجری مصری: آمریکایی‌ها با برخوردشان با تیم ملی ایران، ذهنیت متعفن و نژادپرستانه خود را به نمایش گذاشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.91K · <a href="https://t.me/farsna/445837" target="_blank">📅 17:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445835">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRVLEB-4WPXDvVkVUFH0YUmxd8jLJp70xXW8KgcrThfvF3BzDMmkHq4IJYdpYUJzsPtIProNvGe62fYwBucxEwS_1Lpl-aui30Awb5alMCRSBYCDDktKaN71Ij8nnO3AIAtfplrAbs0gl0QIUoIFomJEYQZeURPbNgs7o0wbCMiCyjxkpEMkm1eF3xoG1SBiEaAzWhSSjVFl7SFsaa4mAdpKhmVGx_o4RBazersjFvAP1d7y44zkjDyIB9egMfTrf8KGwCUxs1F8Na4sc9oSwmkXEBgxBgvQnyymf26kgN-rKJZVpTktN4TXD0itd5zKNz2NKZWUEqVTR8BEDOxzPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایان مأموریت اوسمار در پرسپولیس
🗣
طبق پیگیری‌ها اوسمار برای جدایی از جمع سرخ‌پوشان با مدیران پرسپولیس به توافق نهایی دست‌یافته. به‌احتمال بسیار زیاد او امروز، توافقنامه نهایی را امضا کند تا جدایی‌اش به صورت رسمی اعلام شود.
🗣
طبق توافق صورت‌گرفته، باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/farsna/445835" target="_blank">📅 17:19 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445834">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlVcZlkqCC8_YI50SCG8Jgu6zaM7zk0FujQWCf6efzWWcOrMX369t3Flc4PFWXr2-eTO8NFUYeV12TtRJu54t3qOqxO6exlKsV8mGV8KvADfSVS1L2mrrV3Qd413MeIMdQqSd7NJJLrIKI1KHmqfnuum_w-_1I5VxwVYQDrSSsxxMytHbJNOElFzaFMwyr8qjiSdoz1IacJEfWDw2EDnBHNKVd-UzOo52n6t8P7j9jnQpuGisrYa-0chkkDyEKgmWUGb6PwYCjjH9-vTJKTCG78n7hOD6dXl0oXYrTqJhZmN3_V7gNQG3A0V3JmSGuq1vWRwU9DY5dew8PaRxLPVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۲۱ ماه حبس برای شکارچیان خرس سبلان
🔹
محیط‌زیست استان اردبیل: متخلفان پروندۀ اتلاف خرس قهوه‌ای در شهرستان انگوت به اتهام ارتکاب جرم علیه حیات‌وحش به تحمل ۲۱ ماه حبس تعزیری و پرداخت جزای نقدی محکوم شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/445834" target="_blank">📅 17:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f34bd0aee9.mp4?token=KxzR56TwXr9IOqJVe7Bpv63UP_W2WA8-lozip3ZlDtN2Xsh7Mu1kyNUu58GvGmMTDYpbn_srJ4fDEi6ocU4EueneplgSnHhrl7L4l7co0cGrFCP8rm2VW-Vfr-hAYb4GudR718ijFLHdG2mgMMZFMEwAoBgs2IsDAzi4mzRWpoI9X16DXXV8Hfdm2uScfkZWzGJOEtOzaP5ZMHh_hDOOw8ySIb9glaMUvyG3cowTqmKQp-YoATB7UvCHkrUNJDfM9SYqv5ja4umXxDDXIbgH-Ob_CNMWE0y99qHcX9UUACv_TrJ4YxV43LagzT9_CMNb015ziN3N_pTleD-7HKMQ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f34bd0aee9.mp4?token=KxzR56TwXr9IOqJVe7Bpv63UP_W2WA8-lozip3ZlDtN2Xsh7Mu1kyNUu58GvGmMTDYpbn_srJ4fDEi6ocU4EueneplgSnHhrl7L4l7co0cGrFCP8rm2VW-Vfr-hAYb4GudR718ijFLHdG2mgMMZFMEwAoBgs2IsDAzi4mzRWpoI9X16DXXV8Hfdm2uScfkZWzGJOEtOzaP5ZMHh_hDOOw8ySIb9glaMUvyG3cowTqmKQp-YoATB7UvCHkrUNJDfM9SYqv5ja4umXxDDXIbgH-Ob_CNMWE0y99qHcX9UUACv_TrJ4YxV43LagzT9_CMNb015ziN3N_pTleD-7HKMQ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
غول ترکیه به دنبال علیرضا بیرانوند
🔹
میثاقی: بشیکتاش خواستار جذب علیرضا بیرانوند شده است.
@Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/445833" target="_blank">📅 16:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445832">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5ffdd081.mp4?token=o_sOFAKbrYPfM2d4i5dxiLP8DVeyOQ1VI6JOt5JmBRdRlYK_Km8ShyVZzTqWyrymeUsfjiqh5dOfDxRO1SdrJbqihIYh5zZOLFIxswJ_3JNG3fMkTNWkYkBytRs1eWIjHHu88Ju-oPDFhF0qURrriddBLGceGp0y-8Hh9XmGW0Rk0fzvOa5sS7z08I445A5IotAlgk2zHhZQr_WMTkYEkgjLX6ceAYBsxIOszOHB70j89EHOzJR8eVtSBRVHCGgobO-9Tylm0k83GM9sgpOBO-iuDY-YsvJ0MLkqcP2Tahlz03KPW3uOqrx7UUH9XL1E6bbWNXHl6RXsOS2DuK77rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5ffdd081.mp4?token=o_sOFAKbrYPfM2d4i5dxiLP8DVeyOQ1VI6JOt5JmBRdRlYK_Km8ShyVZzTqWyrymeUsfjiqh5dOfDxRO1SdrJbqihIYh5zZOLFIxswJ_3JNG3fMkTNWkYkBytRs1eWIjHHu88Ju-oPDFhF0qURrriddBLGceGp0y-8Hh9XmGW0Rk0fzvOa5sS7z08I445A5IotAlgk2zHhZQr_WMTkYEkgjLX6ceAYBsxIOszOHB70j89EHOzJR8eVtSBRVHCGgobO-9Tylm0k83GM9sgpOBO-iuDY-YsvJ0MLkqcP2Tahlz03KPW3uOqrx7UUH9XL1E6bbWNXHl6RXsOS2DuK77rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مدیر سابق روابط‌عمومی دفتر رهبر شهید انقلاب: آقا از ایران‌دوست‌ترین ایرانی‌ها بود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/445832" target="_blank">📅 16:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RCFeuHcIzLP8yMBJbrkHbZJ7fPCTrzulS1vQ3BUfdZNcjmi-BzSn0Jk1ARJO63YD5gaWlmDl-4NYLnzqBa94-U4aSk4OUXeAy1tu09XZLK1LAMpBtFrRePsh-hgGtCRKINv758JMSCjjttQmyKVavNdrOrjX7PhqgvNT8vZ2vge23PcYm5kTvdexJxxR_ToMOJErnoj7aA3cK4iO3fbNgjynCpAt-HzZhFnBD3cpcBsmj6HE-LkzT4j31nt-XKb5KLkQvds8Rn9lzlZuP_qV9UVbDfDOELko_z-dC-xaMYTh-S1TAEmvyFzAdWEU_O68UGtABVgwfeU-j2ejJn0qWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ایران ۶۰ درصد بنزین اسرائیل را نابود کرد
🔹
وزارت داخلی رژیم صهیونیستی سند تازه‌ای منتشر کرده است که نشان می‌دهد حملات موشکی ایران منجر به تخریب کامل مخزن اصلی بنزین پالایشگاه حیفا شده است.
🔹
در این سند آمده است که افزایش واردات و به حداکثر رساندن تولید در پالایشگاه اشدود، تنها بخشی از کمبود بنزین داخلی را جبران کرده است.
🔹
همچنین، مجتمع پالایشگاهی بازان در خلیج حیفا، بزرگ‌ترین مرکز تولید فرآورده‌های نفتی اسرائیل، تأمین‌کننده حدود ۶۰ درصد بنزین و سوخت مورد نیاز این رژیم است و در ۲ جنگ اخیر هدف حملات موشکی ایران قرار گرفته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/445831" target="_blank">📅 16:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XTTafB_utTV07ERzOsN2M9tfmIzNKJD9zzZDinYNfon0Ulr8VgHEzcFMrbJdHKJ1800TCviFxRt3JLXGLz45figLWNqwTJ83lB2GR1btjxvryu-JoOFz50TtitghKTbNTh_KBjybJ_AI4Zjtza8FXJzkQf2GGpswTrs6C74-kcliSO26P5JNp073F9MtvyZj6DG0d5bYHOx5Sz-qL2Xw-LiUOGbQIbq9y8GSW9XrkLGiDXi9wtYO5OI1gRPqBH9ARvA6I0ccKtdaMexw-WP9JIzjyti54NXKhfguZBngiIyuOPMxen7W2dkFYHPfrxtv329UVn41Rr2G5C8i7yv0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروندۀ استقلال در خان آخر دادگاه بین‌المللی
🔹
پیگیری‌ها از آخرین وضعیت صدور رأی محرومیت نقل‌وانتقالاتی استقلال در دادگاه حکمیت ورزش حاکی از آن است که این پرونده وارد مرحله نهایی خود شده است.
⏺
براین‌اساس باشگاه استقلال از طریق تیم حقوقی خود مستنداتش را به طور کامل در اختیار دادگاه CAS قرار داده و همچنین به طور موازی توافقات لازم با منتظر محمد، بازیکن عراقی اسبق استقلال و وکیل او انجام شده است.
⏺
در این مرحله هیئت داوری CAS نظر و لایحه نهایی فیفا را به‌عنوان یکی از طرف‌های دعوا جویا می‌شود و پس از دریافت پاسخ فیفا، رای نهایی پرونده از سوی دادگاه اعلام خواهد شد. رایی که مدیران استقلال به‌شدت امیدوارند منجر به باز شدن پنجره نقل‌وانتقالاتی باشگاه در آستانه فصل جدید شود.
🎙
یک منبع آگاه به فارس گفت: استقلال اين بار به طور کامل با ارائه مستندات از منافعش دفاع كرده است و مشكلی از بابت روند حقوقی خود ندارد. بااین‌حال پیش‌تر اشكالاتی وجود داشته كه هنوز هم می‌تواند نظرات فيفا و كاس متأثر از آنها باشد اما همچنان همه چيز در مسير خوب خود قرار دارد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/farsna/445830" target="_blank">📅 16:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اژه‌ای: خونخواهی امام شهیدمان را هیچ گاه فراموش نخواهیم کرد
پیام رئیس قوه قضاییه در آستانه مراسم وداع و تشییع پیکر مطهر امام شهید:
🔹
ملت مبعوث‌شده ایران؛ ملت سلحشور ایران؛ بشارت باد بر شما ظفر و نصرت الهی؛ شما که افزون بر چهار ماه است در سنگر خیابان، حضوری حماسی و دشمن‌شکن دارید؛ لکن قلوب‌تان داغ‌دار است.
🔹
او که به ایران اسلامی مجد و عظمت بخشید؛ او که محور مقاومت اسلامی را رهبر و طلایه‌دار بود؛ سخن از یگانه دوران است؛ سخن از نادرِ نَوادرِ ایام است. سخن از قائد شهید امّت، امام خامنه‌ای (قدس‌الله‌نفسه‌الزکیه) است.
🔹
اینک، نوبت وداع رسیده است؛ وداعی با اشک و خون. همانطور که شهید سید حسن نصرالله، شاگرد ممتاز مکتب امام خامنه‌ای شهید، فرمود: «ما با شهدای‌مان خداحافظی نمی‌کنیم؛ بلکه می‌گوییم به امید دیدار».
🔹
آقای ما که اکنون، عرش‌نشین هستید و در معیّت اجداد مطهرتان، در مقام قرب الهی به سر می‌برید؛ ما را نیز دعا فرمایید که به قافله عشق بپیوندیم و مغموم و مغبون نشویم.
🔹
اینجانب به عنوان خادمی از خدمتگزاران نظام اسلامی و مردم مبعوث‌شده، از باب تکلیف، مردم گرانقدر ایران اسلامی را به حضوری هر چه حماسی‌تر و پُرشکوه‌تر در مراسم وداع و تشییع امام شهیدمان دعوت می‌کنم.
🔹
ایضاً تصریح می‌دارم که کلیه‌ی مسئولان و کارکنان قضایی مسئولیت یافته‌اند جهت هر چه باشکوه‌تر و حماسی‌تر برگزار شدن مراسمات وداع، تشییع و تدفین امام شهید، در سراسر ایران اسلامی، نهایت مساعدت و یاری‌رسانی را به بخش‌های دست‌اندرکار و عموم مردم داشته باشند.
🔹
صد البته در جامه عمل پوشاندن به توصیه امام شهید و امام حی، مبنی بر پیگیری و احقاق حقوق تضییع‌شده مردم عزیز و صبور ایران اسلامی در جریان جنگ‌ها و تجاوزهای اخیر و اقدام تبهکارانه و وحشیانه آمریکای تروریست و رژیم صهیونیستی سفاک در به شهادت رساندن رهبر عظیم‌الشان و خانواده گرامی ایشان، بیش از گذشته و اقدامات صورت‌گرفته، تمامی ظرفیت‌ها، امکانات و ابتکارهای ممکن را به میدان عمل آورده و گریبان جنایت کاران را رها نکنیم.
🔹
ما ذَحل و خونخواهی امام شهیدمان را هیچ گاه فراموش نخواهیم کرد و ظَلمه بدانند که جنایات قساوت‌بارشان از عین‌الله مخفی نیست و دست انتقام الهی دیر یا زود گریبان آنان را خواهد گرفت.
🔹
بار دیگر با خلف صالح امام شهیدمان، حضرت آیت‌الله سید مجتبی حسینی خامنه‌ای(حفظه‌الله‌تعالی) تجدید بیعت می‌کنیم و این مصیبت عظمی را دگربار محضرشان تسلیت و تعزیت می‌گوییم.
@Farsna</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/farsna/445829" target="_blank">📅 16:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445826">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/227c74837e.mp4?token=GYIcr143eAC-7hCnExR7f38Ypg8qsDF8ROzoQChwMt29N_yoaEn8AreL6IvOrg1PIisfENbhFDSVCfzXWqEaXfuayMj6TGZypONiPCydrceSGxJNYFhLtlt0cEb7-EepdToON5SU2SswHklZK3qGGsy8PHBB-3l81dSzEJdBbBGgMU55uV2L5l5x6cCIaErBwCh8q14eQP-XxLfGFd2zMx-URCbcNR75JFuGMckyZ_ZWIwUkR8hHMbEHGTg2xf5WeHU396K0HFXUouo1himT1CB33SHNTBxcxtEQM6OmQ0no0jiuS-5pkcVOZ3jnFChjsrjbO-S1b_9ihy1EAhPEGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/227c74837e.mp4?token=GYIcr143eAC-7hCnExR7f38Ypg8qsDF8ROzoQChwMt29N_yoaEn8AreL6IvOrg1PIisfENbhFDSVCfzXWqEaXfuayMj6TGZypONiPCydrceSGxJNYFhLtlt0cEb7-EepdToON5SU2SswHklZK3qGGsy8PHBB-3l81dSzEJdBbBGgMU55uV2L5l5x6cCIaErBwCh8q14eQP-XxLfGFd2zMx-URCbcNR75JFuGMckyZ_ZWIwUkR8hHMbEHGTg2xf5WeHU396K0HFXUouo1himT1CB33SHNTBxcxtEQM6OmQ0no0jiuS-5pkcVOZ3jnFChjsrjbO-S1b_9ihy1EAhPEGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غریب‌آبادی: مذاکرات برای توافق نهایی هنوز آغاز نشده
🔹
معاون وزارت خارجه که در به قطر سفر کرده، دربارهٔ شروع مذاکرات برای توافق نهایی با آمریکا گفت که «کارگروه‌های پیگیری اجرای تفاهم و مذاکره برای توافق نهایی شکل گرفته، اما هنوز مذاکره‌ای در این قالب‌ها شروع…</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/445826" target="_blank">📅 16:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445825">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVbVTlJRSbiqhHnaIr1AwtWj0QdrSOuvd13PASK8k94FD6EeZAhQtf_swYNzvzzxPi9Ff_1L0BPxdRRae415FJF4j68eVLIo43Md_mzXalzCvsAGNVzQxs3y5X2Vapmfy2ai-LZWyDGe_mORTjziZtmhR7dZQgCPTMT9TD34DaY9q0iumTMGCQE2ZBmrB9aBXVifk3Vp-iXOpg_GPk_xnO9lhL9PH8q0TDcC4_zsUmhmc4CNN8-cb15dFUAyZvjo0pi2dtZYX6My16JhcoOcMytmMTC7jD1yLGNlAHM_YBh099o7NDIQHYuc_tD8-ZHxpvPkPDNEoN3IRezneJkLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای فایل‌های گمشدهٔ شما را پیدا و مرتب می‌کند
🔹
جمنای اسپارک، جدیدترین دستیار عامل‌محور گوگل، به اپلیکیشن جمنای در سیستم‌عامل مک‌اواس راه پیدا کرده است.
🔹
این ابزار می‌تواند به فایل‌های محلی کاربر دسترسی پیدا کند و وظایفی مانند دسته‌بندی فایل‌های دانلودشده، ساخت صفحات گسترده از اسناد موجود در رایانه و مدیریت برخی گردش‌کارها را انجام دهد.
🔹
گوگل می‌گوید در نسخه‌های بعدی، کاربران حتی از طریق تلفن همراه خود نیز قادر خواهند بود به اسپارک دستور دهند روی رایانه مک آن‌ها کارهایی را انجام دهد؛ برای مثال، پیدا کردن یک فایل مشخص و ارسال آن از طریق ایمیل.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/445825" target="_blank">📅 16:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445823">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DvDgn7zrfE8mFR-r9quPCpE4n3WBSDmRL52sDuB0sxoug5jTdf9okC-4_T-d0ejBsihNW-KX6WOuOwjTjV_6LCiYyKqnbaWLxqMpa-CV7Co-ARdwMpjLvImSx0KU2C2slZXhauLsCNU4E2fOCTKEyBw9bqIPOIj_J1pwH9oOwpGBpXRF1ik9scEjbjXeRzghZX1o7TXSLBiD-FIsmvn8_CgFUnarEuVqh28y9_IS64vw5EGWsDH8Gr6VallE224DpfKF5bx5bHYRSvP6JZjDDRb14cL_Fev4bQh9j7Mu_m2edXF_Xo6IOhsB7pjOezECtwu6oS5_GiALGdMNAuTOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KJvpp7qMwi83rLawRF2D1OnOnubLw05al6XUpKjZvdSmPE17G-h28h-WXfqaqslNKBHEle2zBowkgUwn_BBB1bBbJ0yobMgC1RIYWapHKD-gwTo2-fCDHUX6Lw3Zv9dPBCt2pVfwxL7yoPQviUdY4gVCVakS9JY_xcw7Ig1HPBj6pISEcAN0d2WrpQtqFbUfqxtRzMCE8_PlipULpL4Dis_0EYEdoi8ll63y9p-NM9It-ZZnjsgjlAbtddtD7fK6twrjOq84y1gYQJjhvPCKZpepY3V79GVwHCuF55-H8weUcXb-eRa7yd7ab9tDQu640bFBzbMKcksFgldHJ-oc4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاربران خارجی: گروسی همچنان غیرقابل اعتماد است
🔹
شماری از کاربران خارجی در شبکه اجتماعی ایکس با زیر سؤال بردن بی‌طرفی رافائل گروسی، مدیر کل آژانس انرژی اتمی، او را فردی «غیرقابل اعتماد» توصیف کرده و خواستار پایبندی آژانس به مأموریت فنی و حرفه‌ای خود شدند.
🔹
بخش قابل توجهی از کاربران، مدیرکل آژانس بین‌المللی انرژی اتمی را به جانبداری سیاسی متهم کرده و مدعی شدند که او از چارچوب مأموریت فنی خود فاصله گرفته است.
🔹
در میان این واکنش‌ها، شماری از کاربران خواستار توجه آژانس به برنامه هسته‌ای اسرائیل شدند و این پرسش را مطرح کردند که چرا مدیرکل آژانس درباره تأسیسات هسته‌ای اسرائیل یا عضویت نداشتن این رژیم در معاهده منع گسترش سلاح‌های هسته‌ای موضع مشابه ایران اتخاذ نمی‌کند.
🔗
اظهارات کاربران در این باره را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/farsna/445823" target="_blank">📅 15:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445822">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5d9c076fa.mp4?token=BKj9Nl7F4687_i609QWRnwLrn4h2YCpRL_5F0y6N9dAa1XvfZ3Sas5Z0QNGtNmGheVcJlgpZf9idyuCQ9xa81PMogrb8O3UvCT2OgO5UByf3yEew5MDbhYh_wbbkORKBrxC3aZR40K7wSV86blXrmJl_PBTNedA6Bjzq1hvfOprRUVQStlYBVtxwNe4w4G27PTt-eMZuoUJPkkDabQofmYZvHL0u2cPmgNCqsh1Uvqu3kJV2dqZiqV7s-eAU4Bln5z5CQI30mjEn4Z8pPyYBj1MQ-Ihxn7RHhmfeok8wIv5RcNBVlxZ74S3K7W9IC2UnB1FvLWOGpfaKeBz15hW00Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5d9c076fa.mp4?token=BKj9Nl7F4687_i609QWRnwLrn4h2YCpRL_5F0y6N9dAa1XvfZ3Sas5Z0QNGtNmGheVcJlgpZf9idyuCQ9xa81PMogrb8O3UvCT2OgO5UByf3yEew5MDbhYh_wbbkORKBrxC3aZR40K7wSV86blXrmJl_PBTNedA6Bjzq1hvfOprRUVQStlYBVtxwNe4w4G27PTt-eMZuoUJPkkDabQofmYZvHL0u2cPmgNCqsh1Uvqu3kJV2dqZiqV7s-eAU4Bln5z5CQI30mjEn4Z8pPyYBj1MQ-Ihxn7RHhmfeok8wIv5RcNBVlxZ74S3K7W9IC2UnB1FvLWOGpfaKeBz15hW00Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آماده‌سازی مراکز اسکان اضطراری برای زائران رهبر شهید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/445822" target="_blank">📅 15:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445821">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH8iDwFQ6oSNa9LSRP2nyiZ71cm9GABmHHo6UlTi61tpeJajOYx31Sryx-RmiE90K0RJov6h4hx8URxKVdeLsSXJUACLfiLU1jkTL2kaePsjyDHTY8G9c6zHMMdUpMGbxYcPdnpOAVmAbzwdc5-xATtrh9rJBVoeDHRYebUkND5rU8-yP_LN-ufUcFy3ShNziHg5uJZkCc-5HtKspq3HyXi1GZXFkvDU9JUfWAkxAdS0ARGgFrno2gqAVgUMh9G2RJkiSYomCQqtqw3wUgttgfrk6Ug_h1vlpZR3yV8InkO1aEY8MWVPJ7qx3OhMh85MVWnqU_pvgeIJvw-GKZ9v6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تأمین اجتماعی: بازنشستگان مراقب کلاهبرداران باشند
🔹
سازمان تأمین‌اجتماعی در اطلاعیه‌ای اعلام کرد: گزارش‌هایی از تماس‌های مشکوک با بهانه‌هایی مانند پرداخت مابه‌التفاوت حقوق، ثبت‌نام وام و تسهیلات یا صدور حکم مستمری منتشر شده است.
🔹
هیچ‌گونه تماس تلفنی یا مراجعهٔ حضوری از سوی نمایندگان یا همکاران این سازمان برای دریافت وجه از مستمری‌بگیران صورت نگرفته و این موارد مصداق جعل، اخاذی و کلاهبرداری است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/farsna/445821" target="_blank">📅 15:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445814">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8AQpE3IgZzmnvwDunVXfDEOKRq9pPYKah8Djk3qGILhqoakiU1BKGSkPfuKQPiiMB6L3P-zUg3MVoYemB2l3TylZUtPJZsyrxGtfz3bUWj9xmyhPfkhEjuFNtj33nj2g0eSPur_mCErNXk2Pad8mC9ntxZLADTlaT4UQCLk9s_UjIYRzgMZM-1jZOCIiLjchv-937hi1jimwFwwM0TobIxnoBxv1jN5O4x23--iklfdlYYunK5BSTtWR9JqKNvLKw0riZrPz88NeHGgvcIR5suCKsGh6_WcSvjjf7-FdxhqBWXcf9T1_McoonmbaQZl3IEP-L8hNIG2P1Df4d1hlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDS0ovMAijWpeC9fTe3XdADjQEmiotCh5P2Udb33TPdB4L7q0-KGz5-9kik-6r3rZ8nA7dX5-OGMfj3u8-7DcbEnnr17dG1E6AgafcBlY4R4aN4O-sYaRDwLH_GiQOy269b7xcbzGtO_5HwFFKxZprEw2AbTYhAw-plJ_zVoKbsHLTwDQyu6NZ9MMiahLIbRyj_cuB1tcIGW9B7abyCQ4Gha4tW2IEcledCk23UgpVZ4Tg-nZQZQ-PKp655Plb9yYxwMnf4GUEGBLJpQtSxESBJKtWs-bsCQEB8pSADEdJ0APRgl1PrPZ6M3U-pGM8Vt8VN2QAymmVx4Pjt7jR8Txw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gqr161faxqsfI0znG4qTPvGopAw7ztnceZT0WLy9rOKw0DR1Z0hkwt7ShpHLGcHR0fq14uc4z393q1huF774VbT3Kt0Fd39QTHY3DeDX3y5Q8m-ApmEQgYMv8m4EEPa2bFxHvwJKkLXctmRfZu7QWdoAWw1OK1tfrQucKeZo282cqVy7pZpYWmh2KUCmIGQJGZscHwarYG7CSUvZZf3-gmFmK0EIxVcQSZXBp0MShLL-rd_wOSkOfMTxOhUsv7jXLg2mZcSh4EdNYUKnRiDdI8s4bLIHeZGB8q-IegQBonF8Bb7e_mQP8qVSXy-517B_KM-OzLej4Gtm26uSacU_pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrAJBRzwdi3mcP6sigolm7ZDqKIdpEVAR4ao0Ta_XZk-EpEFpK-mMxnQ81S4jY7AMnun-rdUYXfoTknrYFqKumSzhMdgCJibkxGow4jUfi7mCmPB17eXZXBMQfVbsxxKPy2UQl-Ihc6hmDAyAj2EuOtu3bn2dFWrkpl7R68GpU5cScQuFgB1HxyL-hrfnoDsePYzZ2RxJtMTQaJyjul-7YyzNHiW5QAYjnOdcLnfKx1iXXD6OuzbBM74ts--t5A-IYFhKY5zgrrM5sfSXMCHsbIXgQiQqWcfzh9EBKnfoUaTfNqy3WhY3tD4MOtHxj8CnWXvXLn2TTu2TIOlGAInPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L9PltkGmgtd8dz6D_AU2HbH_fXSA3N0m3TzK3Nfwd5CgCjnmBMDJ8yjpGd-54VDi96jFI-_VnOcpwNjNqwof7Q_f85JrJZ-s0KmkyLXv0SFo_z1gFpsbAljIsM2z8bwGi2QqBWyHXb6k2IRC3ipl8LD68d5IylTw475bmyIW17D5JB9v9ghIzuinkN0KRSUMS6PhYte2zGimm272jYjzC19LmhSxDhxda7kPZqaEpnQi-wadgVkpjT4XsijIJPeoL8YBsLki90ewp1e80E6vG5DOdFL5YjyLf--SIGn9gdbemto2fJt9XPEVytIc13gyeLoUXkjPYZWrXSKsX2GSbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q78ONHZ1aqbn0-E6JEuVMutb0_LaA82sIYuupAVcithTQHfRb2jhclE7-Bf1lLUE26dM9ma4kl6pBVcpkbsDz6v2xbyCWq4BR7W05UPbXxhf3BYYc9H3YH5DE2wEX4q5cCt-N-N1kTeSzMMDPvK8sMuFTfAb6YSIujV4rz7TssNTv98qK9BMRv-RHjVkQP6vuMz6Dqg2eTkpJ9hvIq8PtiDRtYksOoLG3x7v2pOYv-QgbkTISk0gVDzIdrKkMMRIExY21YoiQwg7BdFJsPRqMhgEi4EssnU8jbxBHtuAnc4T-sXb5Cfn6vxcVtuxfLgzjqqurHxcfD9xv1mPUEnjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ME1X7PnIhufO3D57Gwow9mGTCIOdkw4Yz_uV873d_U_qKMjWDCiTNgbvq0k5ShM0dCl91EjghxnuKItBEr-wJuVsytH0xd22BnJS2gK8FoogezxKCqDfuNkFKWHGk3qAGeHUL39HLtd2EnO3ZYcKtXbn7YuLornTXnu6VeoeLVCF1YzsE-Vp73H7wP2BhPWni7O3unPiXxBfo-ZTgU_HmPc51xekMPKz7ug4KLkvSMXw5Cwd9WM-2u6tUEk80BUNbpKxCqPvjzABNkaCpWioEQBq08kz1SIXrc0mvQUkQ9cGGFpVTf1VPgaKr0BTfmqAn2j2FfgKm3SXYBi5ao9TiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
پشت صحنهٔ آماده‌سازی مراسم بدرقهٔ آقای شهید ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/445814" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445813">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6lWXYavYnpTc8NQtThyrEoVCZtuKIL9l3A1wEV_K-T0ab9uEQ3GemNZOalm3NtzWUs1V-n9-4pi3fBciuM0XB3cQzEURzut6tWnpeXRa6WiwiuCSycE9P7b5nvuQi1dhze7pWztfKEtwfl81IcJuTUWE-vkQTWr5aLbzMyRpPAFeWMPfvAguKP7pqKxUoM7zMMHOd_BJ7k6hvElZr2RqUA5vVvtKwVR7wgH9u4mrF8-RYqKi9eU9teBykhMRz_ezjMhbrPBtwSCEu0P2GGm0PA0_4m6QwWeqUlHTe4V9bQ8upOe9jOD98dnCIj0-mcg9kTPX86TQdwdzDDYSmBOaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم تشییع پیکر شهید مصباح‌الهدی باقری کنی، داماد رهبر شهید، جمعه از میدان دوم شهران تهران برگزار می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/farsna/445813" target="_blank">📅 15:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445812">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaM7LjCCQj1OlqKNsXNzWMnn8ZiXC6PVMz23N6NXfDb0XCNSaqoHbc4hBac2NgbEytH0Dfm4rCJk_IkNWzeemtfRlzuKFSlUedvNcpW9jxUgtPb0zMwJwLUpSaGCtmhgXy6B_VMKfU3e_RgnT2s9fdmCpt7egezdmIxX8HspgcO23ShP5nlyjqEnaq2XTeRuileTftQ5TBCHS0mDLsRHY3YTQpcIdkBZk5dEEawpUiSa4IGn_2nt_H-oE7Lnok-YSGG0ak4Z61rgpC4S8f7hW2obhMle6J3DtWZPzAvgu9Tu-I3AUSOr5EfLEL4fOVrnBHHtxDZuJUd7CW9Mbfih6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
برگزاری مذاکرات فنی غیرمستقیم ایران و آمریکا در دوحه
🔹
رویترز: گفت‌وگوهای فنی ایران و آمریکا به‌صورت غیرمستقیم در دوحه در حال برگزاری است و در این میان، قطر و پاکستان نقش میانجی را ایفا می‌کنند.
🔹
نمایندگان اصلیِ ترامپ در مذاکرات با ایران، یعنی کوشنر و…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/445812" target="_blank">📅 15:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445811">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=KPssRN6iJ_2dTwRYsjXm6-hMphAuRDWpS70zv3Db9zZq126xtDfFthZlrgeq8heVGkA2IJgiwcUaZCVfDC6NfpFAV1Bck8Jj5OTps-O9Y6swh1U8LfTPAQm6qjTn3hmdhntzRhSFzn9FSxWhE7-lJvTBnuME9jHS-WmkzU5QZVvBcgtAuozqcQStp9YZ4MBaTPBC7tlVP8zgpY_zk9Vx0-15njFOi1N_3H0I5_uaut_Hsbl3BhAZqo--hSqvHCeEOfSJbR264YAs5UtXR1DEttr1cdXGj6EN8DyRPRNdecZ-sXCOINoMu3nnjHeP8UQnY-1oXUmTegdcgrmkVIjePFOKr2KXToCjrkpTFJ9ULDOP-LEBvZjltA7zfflaCJitCxreox-n5PAAVanvCWPIOwscn9Huvui7iyfaAO4uUP9Vk9nc01tOYIgCCp3KtuWb7SK2Ckz08Altfzv1FfcdL7VdXNcJxpYsqK2rxsyfv3ARPVvJwpKt38CloPVBQzeIcWo99zag7d1GMgpm2jX7Z18LPayvaEFF7xVWBpyom3xMyCtaQzrujf0ch0zP1zL6IyjVtHdRDeRYYrkvk1j_MHdjLV_5mBApqKSlfu-FMRTxylDfEsTHt5bHNQOZ817XQA0M2Q_I_FJGdO6ZlhRLeFknCTgyipHO7ONJ_lYTRk4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9fa897e21.mp4?token=KPssRN6iJ_2dTwRYsjXm6-hMphAuRDWpS70zv3Db9zZq126xtDfFthZlrgeq8heVGkA2IJgiwcUaZCVfDC6NfpFAV1Bck8Jj5OTps-O9Y6swh1U8LfTPAQm6qjTn3hmdhntzRhSFzn9FSxWhE7-lJvTBnuME9jHS-WmkzU5QZVvBcgtAuozqcQStp9YZ4MBaTPBC7tlVP8zgpY_zk9Vx0-15njFOi1N_3H0I5_uaut_Hsbl3BhAZqo--hSqvHCeEOfSJbR264YAs5UtXR1DEttr1cdXGj6EN8DyRPRNdecZ-sXCOINoMu3nnjHeP8UQnY-1oXUmTegdcgrmkVIjePFOKr2KXToCjrkpTFJ9ULDOP-LEBvZjltA7zfflaCJitCxreox-n5PAAVanvCWPIOwscn9Huvui7iyfaAO4uUP9Vk9nc01tOYIgCCp3KtuWb7SK2Ckz08Altfzv1FfcdL7VdXNcJxpYsqK2rxsyfv3ARPVvJwpKt38CloPVBQzeIcWo99zag7d1GMgpm2jX7Z18LPayvaEFF7xVWBpyom3xMyCtaQzrujf0ch0zP1zL6IyjVtHdRDeRYYrkvk1j_MHdjLV_5mBApqKSlfu-FMRTxylDfEsTHt5bHNQOZ817XQA0M2Q_I_FJGdO6ZlhRLeFknCTgyipHO7ONJ_lYTRk4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آماده‌سازی چهلسرا در جنوب مصلا برای خدمت‌رسانی مراسم وداع "آقای شهید ایران"
فعالسازی تلفن ۴۰۳۰ برای اطلاع‌رسانی مراسم
@Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/445811" target="_blank">📅 15:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445809">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمس پرس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUiQeyCpRcIgQaeKFf-nQ3tTILhqJPzD0OG8j4CXcnYlPsBz7un7WNemXrw8K7mcObi8-95aPSRNtZDBQUbEh7yjDyOh7sX_strKQrh9DTLv7DiFkyRyBACm2dAZRxghiVxk_Z0J-IXVHq4j8UO-gUZltxf0JSIgQTz6bA8dMspQ1pR1NNqdooHG67-x7dsuVE2PFXkmHPayv3-gQ_kj-Dr0PEu014eqPmYW7m5oO3hippDxlJjJC19Ax0R3pmqFSW2tgheI8bw-jLsB4Rojok2_80dqWbRhwdlFVZrmyFAfO_jXDmfPOZm5Qbn_SDgKvLMf90Fq3PrKo2L3lgZyVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XWAyJyMZl0GFDzTfx5jOFxzHM56r5upHumgiACYnm7T3MQ6Bq7Jx9LfAojw3mTFJ_NdTp9BlS4S6SKJs3YzlPOfZTPxn6dhHeRKCAkg_K7aFyuf-tPpyTVT_ZqJ5MH0Auustokrv6K47DfxQS-iMf-3Mk45n0GSxNZJulKMcNeBb8UDFPOtkCKI01IvO_E-3uOPdAEwD-ffy5s4H2m2ovi-WgOOtuF00Cwr_1BWtd81ctl7uBjejnDRH8AgLyx2OMV4rM6hv_fd2ZaKom99G7-AjngNXER3b1qBFRRtjiZWeRIWOg-v5r4eARBAxAcJJjVlXi2WUoti94XI1zp-WVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔸
پس از ۳۶ ماه؛
🔰
ابرپروژه شرکت ملی صنایع مس ایران به ریل اجرا برگشت
🔻
مدیرعامل شرکت ملی صنایع مس ایران در نشست کنترل پروژه تغلیظ ۳و۴ مجتمع مس سرچشمه، نظارت راهبردی و تصمیم‌گیری به‌موقع و نظام‌مند را مهم‌ترین عوامل پیشبرد این ابرپروژه دانست و بر تداوم این رویکرد در تمامی مراحل اجرا تأکید کرد.
🔹
دکتر سیدمصطفی فیض با اشاره به آثار مثبت استقرار رویکرد مدیریتی جدید در پیشرفت پروژه، گفت: اجرای این طرح باید با مدیریت منسجم، رعایت کامل اصول شفافیت، سلامت و انضباط اجرایی ادامه یابد تا اهداف پیش‌بینی‌شده در زمان مقرر محقق شود.
🔹
وی همچنین بر رعایت دقیق الزامات حقوقی و قراردادی در تعامل با پیمانکاران، بهره‌گیری از توان تخصصی و ارتقای کارآمدی سرمایه انسانی به‌عنوان الزامات موفقیت پروژه تأکید کرد.
🔹
دکتر فیض با بیان این‌که نظارت مؤثر، لازمه اجرای موفق پروژه‌های راهبردی است، گفت: شرکت ملی مس باید به‌صورت مستمر در جریان جزئیات اجرای پروژه قرار گیرد تا امکان اعمال نظارت عالیه و تصمیم‌گیری بهنگام فراهم باشد.
ادامه خبر در پایگاه خبری مس‌پرس:
https://mespress.ir/x6Rn
@mespress_ir</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/farsna/445809" target="_blank">📅 15:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445808">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/farsna/445808" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445807">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcVGkQfhbOtv5bEjMBj_RkWvMo6MzNj5khplWQMFxAjTyDTB-20BzQNpLpzkHe3CDkfrjL42xwkin322epgKLcmkh0eroirX8imBYV9OAg-rix5PddaCDAqpiRedh1S-SyoD5-AScIC17sBaP7nFFgJMNVQsCxKhH7JwqJk_bKiS6n3PsGyae5S3_WA80TB8i7n58_0YO1a2yVAQi2h0DAMfex0fErMSjxdl3ejYgRC6uJTjW081bmz-Lwh1-mvVUTSQtzo1UZWO_In1GnOuAYhS2nRRk_T5-0SuIIqRGcEePK5UwY2GyQREqEVOn6HUFDQ4iWzetMsxSpOxGxUfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر اپوزیسیون رژیم صهیونیستی: روابط خارجی اسرائیل فاجعه‌بار شده
🔹
لاپید: آنچه در ۳ سال و نیم گذشته در اسرائیل دیده‌ایم ترکیبی فاجعه‌بار از رفتار غیرحرفه‌ای، تکبر، برداشت نادرست از واقعیت و اولویت‌دادن مطلق به ملاحظات سیاسی و حزبی بر منافع سیاسی و دیپلماتیک است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/farsna/445807" target="_blank">📅 15:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445805">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZwIoWOuM5mlDLQ1OrDRdFKArjKPdhplddNcxGDrajLWntvW3d-jF02FfkXTrP9I-ZmU3d9rQ9oKT3JISmFBRqzCLxBCczt-w3clV702Rj4L-pbSeYrdZ_9UfMo2Q-8HYu3o1rYEHIUEwi0YunEV9PsgygNrhirdn0KC8-lclB5H8bdZ7XQfGEvBIuw5iuIjL0sb5yO_PkgbgLF4b14yeeCq5lF6KVJB2JrTA3xtEiBFnLkkJTDwYpH0Mgypt6pvySG2Ug_Wm-puV-o4RaMArPBv23JWwkPcy-by1I75VDqSD4Hp4cZQ1LR4sBp6JWIN6lAvwvJM6Bhud4xrsiD2eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فوتبال کشورمان دقایقی پیش آنتالیا را به مقصد تهران ترک کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/445805" target="_blank">📅 14:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445804">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8290876f.mp4?token=XQMzOKVdciymVgxT2OH_TGMp6EvWCxf0hVNbu5KniXzzb7I5I-zlMkamFa6ItehP4GZbSQ5ajLi4-1FAS_nPH-g7Lv_Qo7nRfGWsTrAua_hgsNwXKn-EcSlrLVcjNUW_SOTijNOypLROMeqokmVCcMQ9_H25RbZ9h9q80vBlG8UmXvh2RgHdK5RO7vk9ENXL3P2Kiv6sKiCWKtY2bXC3RThRIf0p7Udfkryhql_UXoZau5fU1Oskmv8OlgjBHALvx5onqUR9HB-Wb66YY3In_1yxHvev0X4NXt22Y3Sz8kGRg1P_-np0EEzDT6yXV3xXwtbWqaqf9N8fBq3zBIwnExMSRGpyBWkHiJZjX2717pEROrshm1vM03uFjgQeGGRFLUA3Pc8hNIC8JDxkRL5bgQ5lSdIY9uKrUOxsewAxExEVUP0pIcMBaOnr18kwWuUXmeE4QvazJH53XPSh_Zf4BpVqSHcasMGxj1_v5V-uG4bx6xyv7BgtcFn2l7LvH8UjpmolY_dhPN2KZwr1PIxJpcofhrxH7IU3Ab5ITd5-3tLupFmZPLK7pvL8h0aLX9__fVAPuKgAfaCoyg7xNoGnQcY1ya49XlP66Z4niNilnPByhaxVLed2Ttcqw4q4N0_G1BVJYzl-ic-QgrIvGiE7a03KETWfyEIWlhqE10umTUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8290876f.mp4?token=XQMzOKVdciymVgxT2OH_TGMp6EvWCxf0hVNbu5KniXzzb7I5I-zlMkamFa6ItehP4GZbSQ5ajLi4-1FAS_nPH-g7Lv_Qo7nRfGWsTrAua_hgsNwXKn-EcSlrLVcjNUW_SOTijNOypLROMeqokmVCcMQ9_H25RbZ9h9q80vBlG8UmXvh2RgHdK5RO7vk9ENXL3P2Kiv6sKiCWKtY2bXC3RThRIf0p7Udfkryhql_UXoZau5fU1Oskmv8OlgjBHALvx5onqUR9HB-Wb66YY3In_1yxHvev0X4NXt22Y3Sz8kGRg1P_-np0EEzDT6yXV3xXwtbWqaqf9N8fBq3zBIwnExMSRGpyBWkHiJZjX2717pEROrshm1vM03uFjgQeGGRFLUA3Pc8hNIC8JDxkRL5bgQ5lSdIY9uKrUOxsewAxExEVUP0pIcMBaOnr18kwWuUXmeE4QvazJH53XPSh_Zf4BpVqSHcasMGxj1_v5V-uG4bx6xyv7BgtcFn2l7LvH8UjpmolY_dhPN2KZwr1PIxJpcofhrxH7IU3Ab5ITd5-3tLupFmZPLK7pvL8h0aLX9__fVAPuKgAfaCoyg7xNoGnQcY1ya49XlP66Z4niNilnPByhaxVLed2Ttcqw4q4N0_G1BVJYzl-ic-QgrIvGiE7a03KETWfyEIWlhqE10umTUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون فرهنگی سپاه حضرت محمد رسول‌الله(ص): فضای وداع رهبر شهید با الهام از حسینیهٔ امام‌خمینی(ره) آماده می شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/445804" target="_blank">📅 14:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445803">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ybb6UIO552OERJBKcwsijNFKVXwOMfI3wu4CZjoiJYlfEYZo5XV5tMuiDjED14N_2dTNWOG84R9xoPuleL2ZiFrAVcdBOQn2EsX-b0AlBRsKAhagl93S-nTKixin99HmUbWVFivrbQ3zZBkTbV0oLXeafm1fWvtfykuUaWSkm-X6kx6xyX4TTX0_FYHj9cHWgueeb6IMWMcW8TKQP7J10JeLE2eImz7cK4FKyxYagtv4oor2nNmSzBw_101mxgwAQdt9JG2XZo__NWnTbYzpCEQNZ4gUYLseom7_6SlzRfsQBmYG2_R-NgwIE9CRmKaHoVQdvWJ8_lP03dJqWMpsNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش عراقچی به اظهارات وزیر جنگ رژیم صهیونیستی: هرگونه تهدید علیه مردم و رهبری ما با پاسخی فوری و قدرتمند مواجه خواهد شد
🔹
رئیس‌جمهور آمریکا، طبق تفاهم ایالات متحده را متعهد کرده است که این جانور دست‌آموز خود در تل‌آویو را مهار کند. اگر آن‌ها از فرمان ارباب خود سرپیچی می‌کنند، ایران به آنها درس لازم را خواهد داد.
🔹
وزیر جنگ رژیم صهیونیستی مقامات ایران را به ترور و ایران را به جنگی گسترده‌تر تهدید کرد.
@Farsna</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/farsna/445803" target="_blank">📅 14:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445802">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🎥
تصاویری از جنایت آمریکا در مناطق روستایی فَشَم تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/445802" target="_blank">📅 14:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445801">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a096758b35.mp4?token=W3Yb4g9dOfQykKXA6OE8GuHN2H7ZEnCzUycdiBEbN_Ka-l5EKj7NL0rLPwTeIqwCm7LnQEFdL5RrYYrYZik7i8uGMjCo0WyTnpH0XGANUesdCg7kA_usHmFaHVXE30TjNm4mX_hKLcfGaCGFc57_FaC_5YwvEFQvJI_lOKVHmaxqQzho-gxjdOD1rRYzuVUgSbrfNdADomGb885eXrWX8efcqKTCQQ5LyoFPf-le6uoueEhhkT6xyWpkV6bD6czgv019c3_K8fIGveQFtBE9B5UI7phxsrbP0r_b7LnuIvCno6f-ktvyLdDf52XuhFTPn7ECcjd1NMxZge_xbwW-Iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a096758b35.mp4?token=W3Yb4g9dOfQykKXA6OE8GuHN2H7ZEnCzUycdiBEbN_Ka-l5EKj7NL0rLPwTeIqwCm7LnQEFdL5RrYYrYZik7i8uGMjCo0WyTnpH0XGANUesdCg7kA_usHmFaHVXE30TjNm4mX_hKLcfGaCGFc57_FaC_5YwvEFQvJI_lOKVHmaxqQzho-gxjdOD1rRYzuVUgSbrfNdADomGb885eXrWX8efcqKTCQQ5LyoFPf-le6uoueEhhkT6xyWpkV6bD6czgv019c3_K8fIGveQFtBE9B5UI7phxsrbP0r_b7LnuIvCno6f-ktvyLdDf52XuhFTPn7ECcjd1NMxZge_xbwW-Iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشتی متخلف خارجی در تنگۀ هرمز به گل نشست
🔹
یک فروند کشتی که از مسیری غیر از مسیر تعیین شده در قالب نظم ایرانی در تنگه هرمز، تردد می‌کرد، به گل نشسته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/farsna/445801" target="_blank">📅 14:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445800">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/096d63f2b8.mp4?token=Khw7jdNCR0PfvChPd86Nadel4m4hURhGqiP1F_KLrMuXI49ww9pYZ4wL30J-Ca1M2mbLd-F4AjwV9njb3dQD0iQ-fLkwbrpl-2OrZRpZXHXhoKDuQrrMsMEA8eK7C_2Oqatn1_R5DAXMpW8L8ug4Ix7QtOWXxsIghlIzKCpXzi2lWp19ft2YdkZv7QIobNzinhIprRiqygdk2FPiwioQ_1lL-NZMP_TMzghbVVJwkFvWXTwk9xXAZC00IdZgYuTVi_QaiFteThtDfTHiq_LOOfZJjK_2uKVkqKwAYirmP5y7z66GAdfzrhCpGp_Ox6gurU5YW8E8avrMqd6J96RM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/096d63f2b8.mp4?token=Khw7jdNCR0PfvChPd86Nadel4m4hURhGqiP1F_KLrMuXI49ww9pYZ4wL30J-Ca1M2mbLd-F4AjwV9njb3dQD0iQ-fLkwbrpl-2OrZRpZXHXhoKDuQrrMsMEA8eK7C_2Oqatn1_R5DAXMpW8L8ug4Ix7QtOWXxsIghlIzKCpXzi2lWp19ft2YdkZv7QIobNzinhIprRiqygdk2FPiwioQ_1lL-NZMP_TMzghbVVJwkFvWXTwk9xXAZC00IdZgYuTVi_QaiFteThtDfTHiq_LOOfZJjK_2uKVkqKwAYirmP5y7z66GAdfzrhCpGp_Ox6gurU5YW8E8avrMqd6J96RM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چطور برای اسکان و میزبانی مراسم بدرقۀ رهبر شهید انقلاب ثبت‌نام کنیم؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/farsna/445800" target="_blank">📅 14:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445799">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">شهردار ایلام بازداشت شد
🔹
دادستان ایلام: شهردار ایلام درپی برخی اتهامات مالی و سوءمدیریت بازداشت شد و پروندهٔ قضائی برای او تشکیل شده است.
🔹
جمع‌آوری مستندات و بررسی‌های تخصصی برای روشن‌شدن ابعاد پرونده همچنان درحال انجام است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/445799" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445798">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnCDXy5Ktwx2thISWltfkUbJYsnusX_-tYqq13OZ26TwtZxivc7qOP-BeuHO3nTHd5pXE1YfAe8IHHlHSPuZeA-sbs5ICe1NsdtPIwWvRoma7mExgT07oicgtP0X5-sPjNc8iolV2zZQR9MNhXVtLUXkcFWnK3Xo3gsF1hyZrRL-0MYAKbz6KO4rTFDrrf1EDQwFiSygWWpaTaiQRshZ-Ixi9jjG5mpJNKFAI-shwQ21V1JmSOhWM9BO1-LuEtlt7lEYnSESMVsOHlxs46-ec_CdF1vJBrutbIu7JVG2q-wJjIE5rvdFjXKWD73USZ3OPmdbxi_LQ-8f_U5WZktZzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مراسم تشییع رهبر شهید انقلاب باید نماد وحدت و انسجام ملی باشد
🔹
رهبر شهید شخصیتی تأثیرگذار در جهان اسلام و جامعه بزرگ شیعیان جهان به‌شمار می‌رفت. @Farsna</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/farsna/445798" target="_blank">📅 14:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445797">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b06c8e7fc.mp4?token=Aej7Z1nSlsXO_KtmNjhJ-obeyO3cMFdzyhrzfeFeaN9fSFRJuXOLJDYweePVLmWGHIoLPl_e7YoZm6iasv7heWmC7qZKg1reVLoUG35quBIH_yhxrubsHITuYOm200A3Swa0h0udjLK38Lf-L79vV3ZPnDlUEbAPf9aD_C60X8y-1wdhudxi_yQetxCgpdguRzrOueGTbvAf8yggEmyvoJ2BBwykOKVF1hA965rl3cxVXWlqBe2c4YJ3ErG7OaKCvn2odX7rxennbJIna-E66pBrh_mmECzDNXglWEnikcOq8FuyyW7DVO-4rSEMfzfgYlhkwBBLR8XSwEk7elkBDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b06c8e7fc.mp4?token=Aej7Z1nSlsXO_KtmNjhJ-obeyO3cMFdzyhrzfeFeaN9fSFRJuXOLJDYweePVLmWGHIoLPl_e7YoZm6iasv7heWmC7qZKg1reVLoUG35quBIH_yhxrubsHITuYOm200A3Swa0h0udjLK38Lf-L79vV3ZPnDlUEbAPf9aD_C60X8y-1wdhudxi_yQetxCgpdguRzrOueGTbvAf8yggEmyvoJ2BBwykOKVF1hA965rl3cxVXWlqBe2c4YJ3ErG7OaKCvn2odX7rxennbJIna-E66pBrh_mmECzDNXglWEnikcOq8FuyyW7DVO-4rSEMfzfgYlhkwBBLR8XSwEk7elkBDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مساجد تهران آمادۀ میزبانی از زائران رهبر شهید
@Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/445797" target="_blank">📅 14:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445796">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxsVrnzTzMbQDLiKDjz2cRgQCXgy4SeW-fLQ8NoGL1S3g3Ye9YEP2bzB6u-Rux_VmJkTBHyd1lX1jRlhJPL9v_g4Ek7tG5ECU9ttL21Nh53o3S8AAjo_FDUCy6HQ_WPxTbTRWMcpl8WJCfBWmQbmq5Cd6E6YGpWcwoW0tuNHJv_0BTNyXVYVtssCRFw33fAVyOam_QmRA4Ch40CNqACrBoIGjkLK-mBy5-nFyj5b1qmxK3Y7yKsqYU8vvnhZbAGj5oyEjL9TGo4v3JcfYTCT1O3d5xGPHfIjWo4UeUZV6Qcr2TivHiFV8d0G3Darkf3mi3jTeS5Vz8qhTu8WK8FkNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: مراسم تشییع رهبر شهید انقلاب باید نماد وحدت و انسجام ملی باشد
🔹
رهبر شهید شخصیتی تأثیرگذار در جهان اسلام و جامعه بزرگ شیعیان جهان به‌شمار می‌رفت.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/445796" target="_blank">📅 14:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445795">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W47IZonH_fvjwKgLBWPhi34MqcCUWOAbVf6b1T8m3tT9dhuruogVkgv36Gf-Y8wjVA79827I1XIzabSzS8X1f42UU5cFqfxxclUTh08GYz4I2TqKt3jW5qHw80o0takwVbwHeobmL8nv_pRoUBOx7OHekFH-e2fmCi3372LTMYxtirboDJS_ik-PIT7kQoCvpZ_T6hFcuiwqWNduTWDWI4HHkr90tuhlcw3SRgcm0Wnu93aNOtO3XjYd7qL4DC5Tcgx4XOgwOYGBA9xiBsYCpsyCBGDYkK5rQIWqwbqEaxauTBfGwsTTXL1rTRf3eKnMD39fjJaDf7SewOMqr1sm-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین لرزه‌ای به بزرگی ۳.۳ ریشتر در عمق ۱۴ کیلومتری زمین، پاکدشت تهران را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/farsna/445795" target="_blank">📅 13:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445794">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4eaefcd7d7.mp4?token=BPiKTQpSMnQpR60t2VvmX9-Wc4d7fOvP24uGUAs-HVWtduXn--g0RGyTjY42TIbd3pNXk_DgZqR2sqhRcq1AEHj_R6hj-8UDJepHQWemTw16PZPPKfjV-bX20-socMEdurw2j6VHv1X7J348eBZPEYExZ0j2wwJi5nlOoRq-fABAgXbyCoce-Vc4X-mbsYTlMcvxuuBOOI9qq3CY-Z55juFVHJnUwLtY1EQaaJkk3OnZ2iB8-03-ap5wglNZ0yzaLdW_QHGtSmqXXP4Qxlzlvo3FWYDWHM59oCeU4ijvUbj02H4J1JvjNh5njlo3ixt16Svj6Jvfh0J1ib98E6wfTlTsE0Sja_jbRjJ2JHdWViQgqylLZ1KJoHL1hqMh80et_THE45O7D_GGD72juyu_CLs8eKl-cFDLKIhFliyrowA8RC02v1tnzk1Z7h4Czi9d6Sul5Tp82TFzTKHgJHz2RVbiBBiH4NNN3m7ipMoRtZJJlqb2ym5ZBa-sf98tkSFQJNgQMyC5PkqeiOTyZFBN63OrsIxA9-ar3qeeFFYSpmh1bXQTVVho13wWLWmQBv7Csire7kKBzBA-U7uVfycQONlSfid61BcjVJoN22Hxz9qIF8DNOfXq-j23nPFWGvJ_UUWZzGg__KmCSEn0BDwejRfeZiCtECtMpsnFEMUTYNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4eaefcd7d7.mp4?token=BPiKTQpSMnQpR60t2VvmX9-Wc4d7fOvP24uGUAs-HVWtduXn--g0RGyTjY42TIbd3pNXk_DgZqR2sqhRcq1AEHj_R6hj-8UDJepHQWemTw16PZPPKfjV-bX20-socMEdurw2j6VHv1X7J348eBZPEYExZ0j2wwJi5nlOoRq-fABAgXbyCoce-Vc4X-mbsYTlMcvxuuBOOI9qq3CY-Z55juFVHJnUwLtY1EQaaJkk3OnZ2iB8-03-ap5wglNZ0yzaLdW_QHGtSmqXXP4Qxlzlvo3FWYDWHM59oCeU4ijvUbj02H4J1JvjNh5njlo3ixt16Svj6Jvfh0J1ib98E6wfTlTsE0Sja_jbRjJ2JHdWViQgqylLZ1KJoHL1hqMh80et_THE45O7D_GGD72juyu_CLs8eKl-cFDLKIhFliyrowA8RC02v1tnzk1Z7h4Czi9d6Sul5Tp82TFzTKHgJHz2RVbiBBiH4NNN3m7ipMoRtZJJlqb2ym5ZBa-sf98tkSFQJNgQMyC5PkqeiOTyZFBN63OrsIxA9-ar3qeeFFYSpmh1bXQTVVho13wWLWmQBv7Csire7kKBzBA-U7uVfycQONlSfid61BcjVJoN22Hxz9qIF8DNOfXq-j23nPFWGvJ_UUWZzGg__KmCSEn0BDwejRfeZiCtECtMpsnFEMUTYNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پشت صحنهٔ آماده‌سازی مراسم بدرقهٔ آقای شهید ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/445794" target="_blank">📅 13:51 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445793">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d96ppPSUPn-reQuHbbcf7pyOF0zTP5G5FVIsTzX_mr5IAg1rwUuGiEz5_VkqbgC61O1iVfMJIFEiUsCo3m8686GxDEVyudNtVDVACtmTetaQFfEz1vs4LD9Kyd1lmao8rxZLWjPlZpJXmbtNUhzFAcGqdbgQ4rUMcLCrDAC4VQ7ndxQLgYRm9Um4g3lBGW6WUOQ1I2ziXu0GMCmuGa6irSpFfyeS_Aala_W0e23MNh54VeFWeiQ2cKWsuOegMLO2dnlRjpl6Xugdl1TTEtyiyENhnr80VaYQ2R11htn8IDJjlImzcuBrtNaCPs9l1YAIXfCpnTBRYVqVamk-3EKmBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: امروز دکتر و مهندس بیکار داریم، اما تکنسین بیکار در کشور وجود ندارد
🔹
باید جایگاه شایسته‌ای برای آموزش‌های فنی‌وحرفه‌ای در نظام آموزشی تعریف شود و با استفاده از سازوکارهای تشویقی و مهارت‌محور، مسیر آموزش را پیش ببریم.
🔹
نباید افراد را به آموزش‌های صرفاً تئوریک سوق دهیم، زیرا این شیوه اثربخشی لازم را ندارد.
🔹
خانواده‌ها باید به این باور برسند که اولویت نظام آموزشی، آموزش‌های مهارتی و کاربردی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/445793" target="_blank">📅 13:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445792">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgqfNV3B8jS1TDE4uJacQJezzrlKWOV_hfx3wOt7nW2zpYws665BmpHQiA9TcnzvhE0y3Kl2ORS3EBalaVRSMJnMF0Rpe770G2d-331Na6EaxCoxBn_s0aT3Z2h0tQJ28JHjZIrjXAldOfkUYAJ9k9NhnbBNFaDBdMNxDawUvCqdH_J-LGyFUehKie80k2TgkYiz_aULJtB967ZjvD1xsvsS0GnImrtwshdFhgdd7DTV8nJLP5dGeB-yA2gvS07XfQHvNnTlG0Nh0rD0tykp5moj6PgXndw4zKZiQUM5d6QH3J1nvO0QLgvjuJDZgMWB4s67osLKyZbg8aM91xYw8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف خطاب به تیم ملی فوتبال: جنگیدید و اراده و همدلی ایرانی را به نمایش گذاشتید
🔹
رئیس مجلس: سلام و درود و خداقوت به شما که با غیرت، شجاعت و تعصب ملی، در حالی که سوگوار محرم حسینی و داغدار رهبر شهید انقلاب و هم‌وطنان مان بودید، در میدان بزرگ جام جهانی از نام ایران دفاع کردید و سرود ملی کشورمان را در گوش جهان خوانده و پرچم پرافتخار ایران را به نمایش گذاشتید.
🔹
در شرایطی که فشارهای همه جانبه بر دوش شما بود، با تمام توان جنگیدید و اراده، همدلی و روحیه‌ ستودنی ایرانی را به نمایش گذاشتید.
🔹
از تلاش‌های ارزشمند شما، کادر فنی و همه دست‌اندرکاران تیم ملی صمیمانه قدردانی می‌کنم و سربلندی روزافزون تان را از خداوند متعال خواستارم. با افتخار به خانه برگردید.
@Farsna</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/farsna/445792" target="_blank">📅 13:22 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445791">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW31SNCEuVY6Afr2g8FjdzurNJ3-0Ud9ePuNh9tHKyCkXk7vQxwY6v5PaxxS3u4L8MOG_4DWNKOyRr1sKLbC7GVKdvMsQlo16CAICyrrhp7Qk3TzvWBi0IkDRcB6EWtC7euHaSn6Is95R-5DqlXvs3pDx7ytmugThzx7czxo8UZRnezUxk9-Rjr2GlOFb3OZ0qE_4WQsOlcSJtUfdy-8yEEjAyHzlueE_tFj-FrI-CnqgzktdG7I948EM1rDGevrUJoaktH6bol9UT48nme2zLqhYkEsyxDlaYRsWebetEMSpTNGagzhqeBUkRT3Mh6V5SrT3H889oCRBvFvfYD74w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ سخنگوی دولت: تهران سه‌شنبه هم تعطیل است
🔹
هیئت دولت تصمیم گرفت که برای تسهیل خروج عزاداران رهبر شهید انقلاب، تهران سه‌شنبه ۱۶ تیر هم تعطیل شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/farsna/445791" target="_blank">📅 13:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445790">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjzPyYsVWGGl-w13aex_9uKRzr0H057GzuGXt9Zq6Uckatg53_BwvqpR4c_sTHdh7dP5kkOfdhPYTZs32kCVDoUyBpzHYPyXlpgs9ugkJVXI5Vl23V5yG7N10jzNXDIneoe7NM8-adWQpZnKBdQALktGfrJJS3WYjx4NTgjpJ5u5O7Z2weodzOEfHMW8J2GNhG5sQz3Vceg9jsoyhQNtRVVI8GSshFyxlFXOQ-mROoaINpcyIV_l4l5SV25vNS7NIL2RybPU5RNSC7TRVYAGRIPf3nV7WgM2F_qk8ETyjNgeTGLv_og7bB5ZMu6fbWk56rr_-gXBll3ANjkZVjCuag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرکز عملیات تجارت دریایی انگلیس اعلام کرد که گزارشی از وقوع یک حادثه در ۷۶ مایلی جنوب بندر بالحاف یمن دریافت کرده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/445790" target="_blank">📅 13:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445788">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEbn6akOXjkdanAkc5X4f7dllaShghgeoLFwVfWoi8nH0M3uvkEj6A-zOJ40PiUR009oReQ0sLN5bE5pnqoKWPAcKxRWjSmhKgs_TIpDLk7Cx_j5Yyl70Tgz04-5v5JKOn0BORZfpGWtuS6WTP5pD8hulVlPTGaYaN-XrbSO6TstHTzxhq45edpv3CjdV75JK1_4_P2UhKWnqX79T94cvLh7QAsEFkEWa4e8oh0g3dr1doatA4on2jNnESTQ1kpad-1B0MNJMCNEg7XfbnyU7Bp4b1Um5AxQbDIx2aHze-N-VropGtjh2R_wEHCw3fT6Ipm52Mxgghure-6dHy73iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همراه اول، پشتیبان رسانه‌ها در مراسم تشییع رهبر شهید
🔹
همراه اول با راه‌اندازی موکب رسانه‌ای در مسیر مراسم تشییع پیکر مطهر رهبر شهید انقلاب، از خبرنگاران، عکاسان و فعالان رسانه‌ای پشتیبانی می‌کند.
🔹
این موکب با ارائه امکاناتی مانند اینترنت پرسرعت، فضای کار اشتراکی، استودیوهای تولید و پخش، مرکز تدوین، خدمات ترجمه و ابزارهای هوش مصنوعی، بستر لازم برای پوشش سریع، حرفه‌ای و باکیفیت این رویداد ملی را فراهم کرده است.
http://mci.ir/-ELTRZ3
@mcinews</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/445788" target="_blank">📅 13:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445787">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=J5Dw3ITLV_sAjbx2aCd65-JsYBFfQxO8riO5nKtx7xIf4iUbvPEuZgPVXVYvfY03pgERBmeWa2RGU8_xyCvz_9N7BMsQWyKxdJo2KuRxUS4W7iCju3Y6QJWucIL4FoeoXJX0AXVqbVluZ4-OGVFoGNqvYoWILPNr87ILDtbudL-buRiCizW2TPTyk--RJZOUJuFCMaZZV1LZFOWfr1659SOPx0aS1u-W3P00v_GBFuVMjfzG5fOmc2JvnBC90n9tbH5Cy6ngm0KSseKc0mhQ-zz9krus3RP2Hi4tZjnxJ-5cHsbVXFnTl6n5UwsySwZ-3a605G2S77ZjLybFDP2qBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc523b2083.mp4?token=J5Dw3ITLV_sAjbx2aCd65-JsYBFfQxO8riO5nKtx7xIf4iUbvPEuZgPVXVYvfY03pgERBmeWa2RGU8_xyCvz_9N7BMsQWyKxdJo2KuRxUS4W7iCju3Y6QJWucIL4FoeoXJX0AXVqbVluZ4-OGVFoGNqvYoWILPNr87ILDtbudL-buRiCizW2TPTyk--RJZOUJuFCMaZZV1LZFOWfr1659SOPx0aS1u-W3P00v_GBFuVMjfzG5fOmc2JvnBC90n9tbH5Cy6ngm0KSseKc0mhQ-zz9krus3RP2Hi4tZjnxJ-5cHsbVXFnTl6n5UwsySwZ-3a605G2S77ZjLybFDP2qBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
✨
✨
حسابتو طلایی کن
✨
✨
✨
‌
🟡
۶۶۶۶ سکه طلا برای ۳۳۳۳ نفر
و میلیاردها ریال جوایز نقدی دیگر ...
‌
✨
جشنواره بزرگ قرعه‌کشی حساب‌های قرض‌الحسنه بانک سپه
✨
‌
#بانک_سپه
#نخستین_بانک_ایرانی
‌
🌐
https://omidbank.ir
‌
🌐
https://banksepah.ir
‌
📲
@banksepahofficial</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/445787" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445786">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/445786" target="_blank">📅 13:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445784">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
سخنگوی وزارت خارجه: با طرف آمریکایی در قطر مذاکره‌ای نداریم
🔹
اعزام هیئت کارشناسی ایران به دوحه در راستای پیگیری اجرای تفاهم‌نامه است و طرف بحث قطر خواهد بود.
🔹
هیئت کارشناسی ایران به ریاست غریب‌آبادی، معاون حقوقی وزارت خارجه اعزام شده است. @Farsna</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/farsna/445784" target="_blank">📅 12:55 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445783">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GunoU-MqsfmqRqMd_lQ-dQna3fuhFm5sgVKLj2d0tco2U8w68Az7sSzvemSbjBpL-3kwuI9A3JUtE8CzlxH2W3aF3dT9fEP9TbTl_ysbZP76p7UtnpxuIh9F4QunAO2eDsG8u4agGfHMyyTGGmfvbLxzP6yQg0j5iuGKxc-Ja-6fZvCWDRR8KXtCfJQnJD4GdaUo3iXf6YgSBdLeX3jNpg4z1iKlXrhfA5H2Rj4oX_bmYF6nXTVLo-enzUcmW-jwZzEHxwnDrC96R0jo6Pc2eTmSBVrGde7D1OQIO6Jzqtp6-kzUEMCo2nSfxX0Je2Ws8JLJqr84zACdu0kU_OKUlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاخص کل بورس در پایان معاملات امروز با جهش ۶۰ هزار واحدی به ۵ میلیون و ۱۸۷ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/farsna/445783" target="_blank">📅 12:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445782">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e882c1d2d.mp4?token=OnbGltGjiGFG_OpBJIpKL8JJEvujWN_bY3ak5wfp8mMaq97aY22OsCG3vejnnsFa8YAm00g3YJBY2QszVTlrWU1UsnPxxPa7k6PKlgk316ohJ2aE-Z0GaNOGipN0lLWpGpNm0lxgdoeDRFaSGXon_Tn_38RBkPlnjE5Bencb_3b_-d2mU09aWsj1MToW_e_wHUYQmMrsAr3ONIOk3TEwe4Lh3c8V1K90NUAvMbXDsZKXMKwWd-h3tZqUTWk8RJ-IeXvf5-aepfwjA4n1gpV506Fv8hPWvtS37GQzTCmfEBF_FmiaXePHttvP6LEKGO9XL7ydSL-MeJqTntc8r-tGig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e882c1d2d.mp4?token=OnbGltGjiGFG_OpBJIpKL8JJEvujWN_bY3ak5wfp8mMaq97aY22OsCG3vejnnsFa8YAm00g3YJBY2QszVTlrWU1UsnPxxPa7k6PKlgk316ohJ2aE-Z0GaNOGipN0lLWpGpNm0lxgdoeDRFaSGXon_Tn_38RBkPlnjE5Bencb_3b_-d2mU09aWsj1MToW_e_wHUYQmMrsAr3ONIOk3TEwe4Lh3c8V1K90NUAvMbXDsZKXMKwWd-h3tZqUTWk8RJ-IeXvf5-aepfwjA4n1gpV506Fv8hPWvtS37GQzTCmfEBF_FmiaXePHttvP6LEKGO9XL7ydSL-MeJqTntc8r-tGig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرم حضرت معصومه(س) مهیای مراسم تشییع رهبر شهید می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/445782" target="_blank">📅 12:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445781">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBuHs_WMn7Kp8v7UcLAWJ7Hw7y1EUAitbxUv-z8EsEgU4VfqiT2Bx64ZAM82ynmyxuiHqm3_TcSh70AAiYzwl9zySw6WPkQNl9whmJfywTk3GHUQMFHRQnR62PQ7z78ngNxYU-vvXIqS_G_kGhIVX5lGpV6Bvr-Ie3-ee0WMOpXKsjzFN2AGWobrz3bhFTyYJsgkHa7Cn6DFflrYwsj1DsZeWgeDlWLn8c-cDGConawNlV3v0E2EvFstMGxpp_XIco36JRObpB-pAadn4avr5wENbtnUKCDiSlgGQKgKGXdak_iRWs35hXF5LSr-sS2q9xVG_iln5I3h4drTuEJjdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز هم مرگ نظامی آمریکایی به دلایل نامعلوم!
🔹
ارتش آمریکا از پیداشدن تفنگدار دریایی این کشور که هفتهٔ گذشته در کالیفرنیا گم شده بود، خبر داد و مرگ او را تأیید کرد.
🔸
۲ ماه قبل هم ارتش آمریکا از گم‌شدن ۲ نظامی خود در مغرب خبر داده بود که سپس جسد آن‌ها پیدا شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/445781" target="_blank">📅 12:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gy1wrhOmJoKUjgo8aycwddigioB_Wpl0P9hlf3LcxtD6cVWgifpiK801UjD0F1n0-FjLjOOJQu1AzmlIJrVBF7XzrNo69yF2uTwKkOQzu8sQMJORnAGxlkONqYyczo0-527Vv41mflcaOp0s_9-OjBLY3-XIhC7fYytCOZfN4P6sQKdIXZ0QA9_RW_ywYRb5igdG7JL-seZKulYQE4F7usyn60THlXCk91zUMhZ28EU6KQAj3RyHDmn1SYdmLYi4roHyk1BzKeHry26uuyRYhtu2WHknnYDzjJhDId_k2EHIWejlui79Y56OvTtlZN7WEM4lDK_Y0d1zFpNuXXMitg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرمزی، معاون شهردار تهران: طرح ترافیک در روزهای ۱۳، ۱۴ و ۱۵ تیر لغو می‌شود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/445780" target="_blank">📅 11:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qizl4cPjqn-gU71i4L0J1m2LhSdKnm9eUi0_aAMjSIqJaXMLqkgA3EqRkbvdtLeUezNhr_JwShQqv47aAuqhZ9sZMcD0vgzQkYZvn9Rq_aSRbiLM2fn1Bz_uBkyD2Lbi8pBFC7y7TK6sogH-piCUPuEpJB8fe1IJYhCToUzlFCk72W58VU6UkjrhdJb_HbOnqiB8gcQfagtT0ogjrpViZvDdSw2iXoon3YHm-l8OCiB2mSMHRiwmyAKI5EQ4hWeBFci5J0yH_RGWqvXkioY_evHXq0LPp323IbrJYGtsP2CTT3_7Zkbf91hG2iPi6_9dbJurcQCDp3ZNY3v6Qel6rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذوالقدر: عاملین شهادت رهبر و شهدای مظلوم ایران به‌سزایشان خواهند رسید
🔹
رسانهٔ شورای عالی امنیت ملی در توییتی پیام دبیر این شورا را در آستانهٔ مراسم تشییع رهبر شهید انقلاب منتشر کرد: مشت گره‌کردهٔ رهبر شهید در لحظهٔ عروج، نماد ماندگار دکترین امنیت ملی ماست.
🔹
پروندهٔ انتقام خون پاک خامنه‌ای کبیر و شهدای مظلوم ایران، باز است و آمرین و عاملین این جنایات در وقت خود که دیر نخواهد بود، به‎دست «عناصر صالحه» به‌سزایشان خواهند رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/farsna/445779" target="_blank">📅 11:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b07raI41WDUmE__AIT7pw68iG6PM2EaO27AalRLd6m_DXjtt6CTOOww1VpDncuHV8z36y6aknlFVZGxUauR-oWfpif8hS4aqjSgx2MxAArE5Dh_QS9-wI4oiLv8nvqO_qu4BFNhC0j0rJ12f7VuBW0jcejMZ562peTFnRpu2ZIyECydEzhLK3n-ZRnBWcx2r00pdrNvqaKkUNQ1CkjdJOPfRQpabcDOu4nxtFN-7SY-eABbcX51rvyGXM3iSNtX3tbW32q0yCwQnun2L3gqD1oWW-QszfCat8XCrw2AF2UmncNSY4YmV2W4c6GB3VFmARpGWKTtBKdD4dYPrT-sRhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم سپاه؛ سرنخ یک روایت در بازی کال‌آف‌دیوتی
🔹
تصاویری از یک گیمر منتشر شده که صحنه‌هایی از بازی Call of Duty: Modern Warfare 2 (ندای وظیفه: جنگاوری نوین۲) محصول سال ۲۰۲۲ را به‌تصویر می‌کشد. در این صحنه پرچمی با ترکیب رنگ و نمادی بسیار شبیه به نماد سپاه به‌چشم می‌خورد.
🔹
البته استفاده از نمادهای ایرانی و اسلامی در بازی‌های ویدیویی به‌عنوان «تیم دشمن» یا «گروهی که باید نابود شود» بارها سوژهٔ رسانه‌های مختلف شده است.
🔹
اثرگذاری «کال‌آف دیوتی» تنها به فضای بازی محدود نمانده است. در سال‌های گذشته تصاویر و زبان بصری این بازی به روایت‌های رسمی سیاسی و نظامی نیز راه پیدا کرده.
🔹
همان‌طور که کاخ سفید در مارس ۲۰۲۶ پس‌از حمله به ایران، در توییت‌هایی کلیپ‌هایی از تدوین قسمت‌هایی از بازی Call of Duty و تصاویر واقعی حمله به ناو دنا، تأسیسات صنعتی و هسته‌ای ایران، لانچرهای موشک و... ایران منتشر کرد و موج گسترده‌ای از بحث‌ها دربارهٔ استفادهٔ ابزاری از بازی‌های ویدیویی برای توجیه جنگ به راه انداخت.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/farsna/445778" target="_blank">📅 11:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MH3f5xgoMMcapPGOmYpG3ruk8HXVGz_GGvp7c-j6B1MsgironBAxQo-IMhBbFkHeoMsUy0cJaBxt6CMYWzP6YfSrTt07IpIjyOVlR1jwknsd9FiJva5FGnlfsrOECL1iKb9v4p7Zb280n0_1vA9zm1ZvgdCW1JXKVsG3fvXYvqKrEkfte1KSriZcZLr4RRans4_9wAbcF-KWEpqrvlsN3lWKd1CLvvThDChuEVYZRAZX9G17zDw8W9gJFeYNGP-fDmlEGfcReLnY4dwcYA7pUO9jvA7J3wQNnO4Pf4yw1l-LYy6JgEEuvoWJkb4fz3rB2Q1hBQnX1s-I1PRdQuv9dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متروی تهران در ایام‌ تشییع رهبر شبانه‌روزی می‌شود
🔹
شهرداری تهران: تمامی خدمات حمل‌ونقل عمومی در روز مراسم تشییع رهبر شهید رایگان است و مترو به‌صورت شبانه‌روزی با سرفاصلهٔ ۱۰ دقیقه فعالیت می‌کند.  عکس: محسن ونایی @Farsna - Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/445777" target="_blank">📅 11:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/drboR3U8zRzIMUPMPTqV8c0cNVTHhtc30nymJLW2q7LyUmha0skxjLf4UIwsZNfLS_mDLRflCOMKem3yd-GPBchABgUbYYausmsRr85F8htKzQb0uhWHDXCjEID28HGDx8MPlAB5k0wSyiYPIFdzPDk8JlSEUJhVS2SAMS9-lw-Gn0VFH-Sug1lbYu5iEnilReYLtUQ9nGFrpDTsh6SbAv3wRdWd1fKmEj9gArbefBWPA0FpZNMB0VBhOOWKFqlYk1pv9iRTXbN6ak3DkYffhKl7994X9SjQFVlO0LKF5GnMKh_xOfGlO4bYX1cCKlRkENwPVcmtS23J3zXBMacgOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحول قضایی و حلقهٔ مفقوده‌ای به‌نام مدیریت اجرایی
🔹
چرا با وجود هوشمندسازی قوه‌قضائیه، حذف ابلاغ‌های کاغذی و توسعهٔ سامانه‌های الکترونیکی، هنوز بسیاری از مردم از طولانی‌بودن رسیدگی به پرونده‌ها و سردرگمی در فرآیند دادرسی گلایه دارند؟
🔹
آیا مشکل فقط کمبود قاضی است یا بخشی از مسئله به شیوهٔ مدیریت فرایندها، بهره‌وری و نحوهٔ ادارهٔ یکی از بزرگ‌ترین دستگاه‌های خدمات عمومی کشور برمی‌گردد؟
🔹
در این گزارش تلاش کرده‌ایم از زاویه‌ای متفاوت به این پرسش پاسخ دهیم؛ اینکه شاید مرحلهٔ بعدی تحول قوه قضائیه، نه در تصویب قوانین جدید و نه صرفاً در توسعهٔ فناوری، بلکه در
تکمیل مدیریت اجرایی
آن باشد؛ مدیریتی که بتواند در کنار مرجعیت علمی و فقهی، سرعت، شفافیت و کیفیت خدمت‌رسانی به مردم را ارتقا دهد.
🔗
گزارش کامل را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/445776" target="_blank">📅 11:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKLKHhyJSKda5wIdPj5xxRznxmSVsNO6E3ztnBXzwjkReHYss3Ax-osMQiJG3cXVK7g80h3MXi4J4a2x3WQMgbC0qp_Kzk3JR_xXpyKEfK0fuZ_LEEy7BDy0x2ALeWcygj9seuovzoNhjisguDGyB2p1KViOy_KrNvq4cZowV7expuCvZYij2ITOEt4fvB4xCoVAJ17-zxY4Y7JTMdR_nrsxQRazn8bvYJxNpMJxb7nkXSCnGssSDoB-c9j4eBjgHh2VUb-jhOpcTjBorAUAMdFVH5DM81YMslhKJQZ9nVKkLOwNhRD9ELVN_Di33JxbqbiRF_b_HLIllZ8Jrax88A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد رعد: شهید امام خامنه‌ای شخصیتی یگانه در تاریخ سیاسی اسلام بودند
🔹
رئیس فراکسیون «وفاداری به مقاومت» در پارلمان لبنان، تأکید کرد که سخن گفتن درباره شخصیت شهید حضرت آیت‌الله سید علی خامنه‌ای، به دلیل جایگاه برجسته‌ای که ایشان در تاریخ اسلام، به‌ویژه تاریخ سیاسی معاصر دارند، از دشوارترین وظایف است.
🔹
محمد رعد، در گفت‌وگو با پایگاه اطلاع‌رسانی دفتر مقام معظم رهبری (
Khamenei.ir
)، تصریح کرد که شخصیت شهید امام خامنه‌ای در یقین، انسجام فکری، عطوفت نسبت به مستضعفین، صلابت در پایبندی به اصول، امانتداری در حفظ وصیت امام خمینی (ره)، بنیان‌گذار جمهوری اسلامی تجلی یافته است؛ علاوه بر الگویی که ایشان برای حکمرانی مبتنی بر عدل و حق، و تحکیم مبانی جمهوری اسلامی ارائه کرده‌اند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/445775" target="_blank">📅 10:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p29djO0a-gXA-obYiMZTNMOT9GPPaFZTJxxSx19GCbh0REC-ev7ixdGaeYBK7sJBIiTW-1WoIG1RYX_BaxUk_hM_FF_4wZLgx7hg6F0JoY0WED9fuifBIY8pPv4C_gkBnrES7LXbRgd7NGSiTtd4i3Ajfcuk23mxRc3QPL6s3kGLYGO_bhCt-7gDPa5TqxYM8VymLAlkPO1MmYzCagCVdNH0_O3xWh-UYhGBb6yHG0tcJUeZ87CYParJ5fdD2ts-evgPLvjP9EBWq3b-5mWULI8nAe5Egyifzwsw3PVd_lFLluZezAMqu0BQdXDreAZqeKsLmOjtXFWH_xgWdWZI4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا ۲۵۰ کیلومتر از سواحل هرمزگان را آلوده کرد
🔹
براساس اطلاعات رسیده به فارس، ارزیابی‌های اولیه نشان می‌دهد هرمزگان بیشترین خسارت ناشی از آلودگی نفتی در پی حمله آمریکا به ایران را متحمل شده است.
🔹
در بررسی‌های اولیه، محدوده‌های آلوده در سواحل بندرعباس، جزیرهٔ قشم، جاسک، سیریک، بندرلنگه، لاوان، بوموسی، تنب‌بزرگ و دیگر جزایر و نواحی ساحلی هرمزگان شناسایی و نقشه‌برداری شده است.
🔹
همچنین طول خط ساحلی آلوده در هر منطقه مشخص شده و براوردهای اولیه نشان می‌دهد بیش از ۲۵۰ کیلومتر از سواحل هرمزگان تحت‌تأثیر آلودگی‌های نفتی ناشی از جنگ قرار گرفته است. البته این آمار هنوز نهایی نیست و با تکمیل ارزیابی‌ها ممکن است تغییر کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/445774" target="_blank">📅 10:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsaC6H37MxLZHQLKBYlk5mGERRTb8eGPtLBfT58ZW1EALugTqu3ePlrYojgcvyVoqmyyv-gxQLbh7Gjpngm3v2xj6KPSDzQ8VEteK6Xn9-o2k87ykvGEbz6hPaqUf_T7wsCCzxXaP6lkfHvb2jdoQgcfU5VC9i0YYV09Wvi6TQFUEJVrDnXt1PeAyiJnWhPG_jn7rMa-t1EPremNizk_DVFz6trpx0GXBrBtrvauUfw07GyTh8VT4ZVoPIp2BoA-XyjyFybp2S-wNQbWgqV3Nw668BP34nzLPPGIBKjpOgjiPwmVAwMIEP9bwT1Pz3x3XCmATvGd6ShXX4ySwpxT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت نام خادمین امام شهید در شهرزاد/ ۴۰ هزار نفر تاکنون اعلام آمادگی کرده‌اند
باقری معاون شهردار تهران اعلام کرد: ثبت‌نام داوطلبان «خادمین امام شهید» برای مشارکت در خدمت‌رسانی و انتظام‌بخشی مراسم تشییع رهبر شهید انقلاب که به تازگی آغاز شده تاکنون با ثبت‌نام ۴۰ هزار نفر از علاقمندان همراه بوده است و همچنان ادامه دارد.
داوطلبان در بخش‌های مختلف از جمله راهنمایی و هدایت جمعیت، انتظام‌بخشی، حفظ نظم عمومی و پشتیبانی اجرایی مراسم مشارکت خواهند داشت تا خدمات‌رسانی به شرکت‌کنندگان با نظم و کیفیت بیشتری انجام شود.
علاقمندان می‌توانند از طریق اپلیکیشن «شهرزاد» با انتخاب بخش «خادمین امام شهید» از شرایط فعالیت مطلع شده و ثبت‌نام کنند.
لینک ثبت نام</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/445773" target="_blank">📅 10:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7TsKz124aeHOztb6tTTbyy9sNB7MnpVVnz4oWnxABH14rb5Pp4HWPiEkaMlhGjr1M40dyrXIEpYf75zHJ55N3ZIckOiQ0xRwbn-KnzTjG_rADZL9WzF1idDPJrwb6Bk_XNRoiBxcS-QcA6lj9jm4_oDFbFD6rWscahrjQnqr5PruybC6BrJZ2YJeLODE1YFxtqv1ym--ZJBUoLWi9UV2d0mcf9hTXZlymG_qLhyM_HHgjdmejWJizp7t4mZavA8E-CW_IqGRIZz5iSwYt9opTqPOrf0LN7mUixP5v4XMIaEML9Rmca9RSEye63ZnyHknmcJg-bJP59cWsj2WQloHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
به مسابقه جام جهانی دعوت شدید!
جام دی همزمان با جام جهانی
با جوایز جذاب و متنوع
⏰
هر شب از طریق شبکه ورزش و
ویژه برنامه ۲۰۲۶، همراه بیمه دی باشید.
پیش‌بینی هر دیدار،
جایزه داره تو دی‌دار
ورود به بازی
daycup.dayins.com
#کانال
اطلاع رسانی شرکت بیمه دی
@dayins24
#دریافت
نظرات
@prday24</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/445772" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-footer">👁️ 9.37K · <a href="https://t.me/farsna/445771" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe4dbc6fa3.mp4?token=Ph9yH-ztgF7CDHWdnn5hXgn_G3UqfXCZMOjIXRBf5TwyP0SwmrcpVR4otVlVThRvxNpSV7xtbJtL3D8fx-U8FdqiCQBOQkV7gkG4Cgo5p-g_SkkWSRIjZXvu-bE9Fl1K-8mUGBY-XLBtVkLsKH2ZyI64Bxdgjf98Ws1Dzz0upd3GfSGemqP369aIQEDd-1L-SXPz9XUeH5UzsVhVuL0HF1T69vNddgWInfZYORRRLBcKYDLFMwPPpKlpcYl16Uqt1v6wIxko4m0X-kRMwH1wbtIbrXNQgnIiBRRmVv3DT5iOfXsa5qGWXicpF0bX8Gh06CUbYbswX7OecwSuRPAaQasetJAXcPwX6i54SeqYu0zQZPZdnnZ_1iDcMwjBLHs_rG-PgZdWe1xeNU-rtYP5on2Nz9Nx3px2j5U3MwKbsc5bLlq8v3p64E_Y6C1My8nMfQR3A4sN1MRCsq5oAve2eGt10n64Gpd6pjxTLTSYxR7lszBX3vYlc-GCaXBf7hrg6vgzqbfoKN-T_RBoHI93iZiC1IvqEYSsdnFQ5FdWBWevZFr1ZOknJbsCR3Jx_xQu05jUUa4YMyX4KOsUs7wiIl-7qcMn6AZ89LWOH9vFtbfc9b-iy9pprTgA8fa28MXxfAG_FwEpJI4ICsgzSYEpxd0FvVGVbMXCSBVyvQDOsTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe4dbc6fa3.mp4?token=Ph9yH-ztgF7CDHWdnn5hXgn_G3UqfXCZMOjIXRBf5TwyP0SwmrcpVR4otVlVThRvxNpSV7xtbJtL3D8fx-U8FdqiCQBOQkV7gkG4Cgo5p-g_SkkWSRIjZXvu-bE9Fl1K-8mUGBY-XLBtVkLsKH2ZyI64Bxdgjf98Ws1Dzz0upd3GfSGemqP369aIQEDd-1L-SXPz9XUeH5UzsVhVuL0HF1T69vNddgWInfZYORRRLBcKYDLFMwPPpKlpcYl16Uqt1v6wIxko4m0X-kRMwH1wbtIbrXNQgnIiBRRmVv3DT5iOfXsa5qGWXicpF0bX8Gh06CUbYbswX7OecwSuRPAaQasetJAXcPwX6i54SeqYu0zQZPZdnnZ_1iDcMwjBLHs_rG-PgZdWe1xeNU-rtYP5on2Nz9Nx3px2j5U3MwKbsc5bLlq8v3p64E_Y6C1My8nMfQR3A4sN1MRCsq5oAve2eGt10n64Gpd6pjxTLTSYxR7lszBX3vYlc-GCaXBf7hrg6vgzqbfoKN-T_RBoHI93iZiC1IvqEYSsdnFQ5FdWBWevZFr1ZOknJbsCR3Jx_xQu05jUUa4YMyX4KOsUs7wiIl-7qcMn6AZ89LWOH9vFtbfc9b-iy9pprTgA8fa28MXxfAG_FwEpJI4ICsgzSYEpxd0FvVGVbMXCSBVyvQDOsTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر ارشد صهیونیست: باید غزه را کاملا فتح کنیم!
🔹
وزیر دارایی رژیم صهیونیستی ضمن مخاطب قراردادن نتانیاهو، خواستار اشغال کامل غزه توسط این رژیم شد. اسموتریچ گفت: «اسرائیل آماده است در صورت تأیید نتانیاهو، فوراً ۳ شهرک یهودی‌نشین در شمال غزه بسازد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445770" target="_blank">📅 10:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucjOv3vsfXojBKeGtkfpvBUCK3sFDm4bql2nbuMMH16X9_nqdQghhm2_XgBAdXo7GmvEqLx_rE0yDnwB8gzV3ccrSpjroysoPRRjd3mYqnTKVLbQPPwEz0OyiJmqfr4SG_aN2LuvuJO8xFg7i74LtuwQuDQ7UwXxQfW-9d7e29vrVaDUme7xqRdvIHwa8NP1L6PCj-z5ZihkmpLNErh8m8s640sbN-da08QDDpUth22iDUC4XtSfTEot0--F7KXN1yvUKsW-IKwdrOqQ7JM_rwIZCSgM4oD_65z9MPhVkbIy0jwer1AMaiWQ8R2skatSd3gfqh_ev1eKe7SLEIwf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت یک پلیس در پی ترور ناجوانمردانه در سیب و سوران
🔹
مرکز اطلاع‌رسانی پلیس سیستان‌وبلوچستان: ساعتی قبل افرادی مسلح به‌سمت مأمور انتظامی اهل سنت و از قوم بلوچ که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی که ستوان‌سوم محمد پلنگی به شهادت رسید.  @Farsna…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/445769" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">استان تهران در روزهای ۱۳ و ۱۴ تیر و کل کشور در روز ۱۵ تیر تعطیل خواهد بود.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445768" target="_blank">📅 09:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">سپاه هرمزگان: صدای انفجارهایی که از صبح تا ظهر امروز در بندرعباس شنیده می‌شود ناشی از انهدام مهمات باقی‌مانده از جنگ است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/445767" target="_blank">📅 09:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445762">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fts8RkTT4KjgFor9dxW6866-aqkYhYzNbU6DW0YmeBdVDTNSNUaKbGCLL0kktg5QFWEbCDxev9y8zoTmcBrkwofjPaa4s3zQwNzv7HOa2_PfO0CklcxSfjjm1kcJ0wv_o88YVFbsSc0cCYelmsVSFouOgBHVfw-aRGtZRLaGOvkPPSZkgDov5hoLS3R3fjnCup_J9bQf5xwdloYA_6kKv-vrjiEID3Jxny4BVzikU2IykuLpTLMbQEEZc9STbUg7mTL0UxH1CLEGtB75-nD6ErG35bOSjLgh7gcDdoJqpFbCUQAi-daCkTq55NFeYwLA8Iz8D4NsP2rg8nnjAJ4Vjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bigj7AIMAQ0m3lCm5fWBGm3U5_MA3QXGDPEeEFehNHUmGjJipj1BAZk0AYRsiAtssU2Gfy9qg9s2yK-jzkQG0CsKwml8OqS0SslGcKw5LkpPtGYRzDuZy57-rvLua1irYIL7sGpb8oaE6G54weY-Ez2nkKgwpSvnIcgi77yGj55W4r7mZ60VpYO2VsgFAnexk9SZB1Yf8nmmrj4ei9ySNxbTesLwAlJsKfpismY7Eb47vbmBLthe5doMqz3QxmqDaAWSkj9ZIcvUMEoI-Zi0i1J99DVDVw6WYKPqF4jBoMffUXb_wJpoI_wba1oXieOpyZuCUe6XOJFmkTMUOyprtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/okNLuJOAcDZ9kWtLoi5JtQzCr-jbHSJf7jpoKCSd_wWuNZo8M6rLV7F7oswSMiupO1FpNM9QZmIugK1Fkf0zAQMlfQaipu2-gYzBVra1ny-Uwyzl53XjK8aMQz-yYz8ITbHNx2s9XaTo1sHLREfDOBnzPv3QqRWGw-qpHWcxsD_mhZY-NKUFVcdaJnOcYa-KzOJw_CAdLcaXZB3nwEO271tSgNrynF5LRYd8WnZWhKh0dHzKZqMqeY-xNSBPXff_Ex2gv-apCZy6429Du6RUMM4DnSna7TuNCO0NPunFUqX_FCuaGKq9yjwApcoHmLBrFyM_GnbJkmIX-xyuhaEUVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82b7158ae4.mp4?token=jM0NKWIgWTdYckJYStci9lU8KE6CFaM-rJ7KS4qebcfFAYWUm84DBThNhN6SW41MfC0KVTYSgwA1Do42Yej8U22FwtO6On6nBP-oGjExAdRkof1n3xOf10Cwlx1erCQhwvA5OntAu1biGCaZmKKiZ0h_ZsfwWomLNl_gPeMdnP5tQXaY8MTq4603BqrKb-dJ-cyUT4vWfY05intHpgFTVvN6wjRNroCsoZ-3kBwq5GXuvEWeWqvyI6MRpljl1LAWh0fqXXsUV8kgVJxYblOBpTjfnOsOhMBn9Mjs006WO407QPApzWbvZzOO_nU26ChRXkC6qFFFSqP7fpHhIyknfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82b7158ae4.mp4?token=jM0NKWIgWTdYckJYStci9lU8KE6CFaM-rJ7KS4qebcfFAYWUm84DBThNhN6SW41MfC0KVTYSgwA1Do42Yej8U22FwtO6On6nBP-oGjExAdRkof1n3xOf10Cwlx1erCQhwvA5OntAu1biGCaZmKKiZ0h_ZsfwWomLNl_gPeMdnP5tQXaY8MTq4603BqrKb-dJ-cyUT4vWfY05intHpgFTVvN6wjRNroCsoZ-3kBwq5GXuvEWeWqvyI6MRpljl1LAWh0fqXXsUV8kgVJxYblOBpTjfnOsOhMBn9Mjs006WO407QPApzWbvZzOO_nU26ChRXkC6qFFFSqP7fpHhIyknfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آسمان سرخ ونزوئلا در پی زمین‌لرزه‌های اخیر
🔹
تصاویر منتشرشده از پایتخت ونزوئلا، آسمانی با رنگ سرخ و نارنجی پررنگ را در زمان غروب خورشید نشان می‌دهد. بر اساس گزارش‌های منتشرشده، گردوغبار برخاسته از زمین در پی زمین‌لرزه‌های اخیر با پراکنده کردن نور خورشید این منظره غیرمعمول را بر فراز آسمان کاراکاس ایجاد کرده است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/445762" target="_blank">📅 08:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445761">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شهادت یک پلیس در پی ترور ناجوانمردانه در سیب و سوران
🔹
مرکز اطلاع‌رسانی پلیس سیستان‌وبلوچستان: ساعتی قبل افرادی مسلح به‌سمت مأمور انتظامی اهل سنت و از قوم بلوچ که در حال عزیمت به محل کار بود با سلاح گرم تیراندازی که ستوان‌سوم محمد پلنگی به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/445761" target="_blank">📅 08:10 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445760">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n723TDr-vq1SVQQOxNmdH_G3LuurVKkE1wBr_Og1UXkoUH2ZsuSaAhF-z6cP-m8x7hfTYmr19XXhRWMfYlCulrWBJWHnv1dY9Idqr-VGuBOHgdolDwoAsrtS46qBOEqutLzG8ra3bUyWHiWCvAPrNAd6vIjVPkfy3dUudnHKLO2SJUvLAg47UK68xdecxF4B00a8qlb5XDNQ8BSl99dnUn_RN8-cpUzMjddP1_QSlf0nilv8YysVcVALK0cdhnF1GBB3q2v3TGTzU-LJvNNVgUqsFcyGoEUxFk8hu-BPA8ueigiiF56hCPBrXQ1XHlsuZCcXgywpURz73OkNuYeI7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک در بهترین فرم خود
شاگردان اگیره در نیمه اول کار را تمام کردند
مکزیک ۲ - ۰ اکوادور
@Sportfars</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445760" target="_blank">📅 07:41 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445759">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7ppw1rWSzlyPJSSeDIjB35ZllyI7dzrgDeYX3MSECitFJlP4w_ebEcPMyVg2l1gsUFRrg_pYKlsIUd61qDyond4sNC7cdsYulLQ6hQACTXeGjIql_QJycCyDF0glZwdlIFUorIFMhefWiikgkUGM1iUsqnEaybjuugY9zO_T6-wLAVlA43ZakRo5bGjqnyefaMtDneIDNkDGB9RBr5Eq9pvFco-kJuAR0AOL11dS4XEY7eBFrZziqrP6r_4b1Szp7m4O28kjQAuY4ftV2BJ5pVZGvkwBS_zIVOmv0aJ5uP8IczPoA7j2mBuN17XDMO_8Y_EApL1G24aXZL0L8MDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی ۸۰۰ تخت درمانی در محل وداع با رهبر شهید
🔹
کمیتۀ بهداشت‌ودرمان ستاد برگزاری وداع و تشییع رهبر شهید: با پیش‌بینی ۶۰۰ تخت بستری و ۲۰۰ تخت پشتیبان در بیمارستان‌ها و مراکز صحرایی، تمهیدات لازم برای خدمات‌رسانی به زائران پیش بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445759" target="_blank">📅 05:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445758">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4Mj-Zf3tk0_74e3XjkkagB0VNcYqaZTw88jdxlnQINNPka7jp9r2NefAex9TvtJ8tGvwVeTstQP1JNbC_6KBalo5nDkHru__gScCIm7YcFr02Hj4x4wkn9HYLpZs2iVOsCESn-AKDKzrVAEjMeBmwHE_E_fuEylmQDZHe894iHvJ9S3ZhUmd48Wrh4ZWjNJYzW5wxLcX-F_r9NSfT8ZYuqnmXTpRkbEz32HZHBpksfMMlJf1aJlEem2wnpm2buv2KMy18tr5JcPKXuHHD0ib7aeHkQBHBJnk6q2HiuhZwVeYfqVSvJ8bT18qnn2YtKlnBnk9k1iOkg9sxTEXVJyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جیمیل به حرف‌هایتان گوش می‌دهد
🔹
گوگل پس از معرفی «جی‌میل لایو» در کنفرانس توسعه‌دهندگان خود، اکنون آزمایش این قابلیت را برای برخی کاربران اندروید و آی‌او‌اس آغاز کرده است.
🔹
این ویژگی با استفاده از دستیار هوش مصنوعی «جمینای» امکان جست‌وجوی ایمیل‌ها با زبان طبیعی و دستورات صوتی را فراهم می‌کند.
🔹
کاربران می‌توانند سؤالاتی مانند «تاریخ سفر بعدی من چیست؟» یا «سفارش اخیرم کجاست؟» را مطرح کنند تا جمینای پاسخ را از میان ایمیل‌های موجود استخراج کند. این قابلیت تجربه‌ای مشابه گفت‌وگوی زنده با جمینای را به داخل جیمیل می‌آورد و قرار است بعدها به برنامه‌های دیگری مانند اسناد گوگل و درایو نیز گسترش یابد.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/445758" target="_blank">📅 05:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7103294b05.mp4?token=hUCm7LfU6w4PTBLm5mQlJgyPw510T9ks899uTSiBhlDaOX5-1Y8RJpUwRrGOThAtj19pPrWkF16BYmZmof3NoR8_O0nGwVPpmKhjb_muEaOCVAacaMAp9sr0zR87TNQoR5xWm6GRBx4kKMl6boQ_xlEDKtDtMl_IuI4z7hBfgCFw4KzbgAlza2KZifL2IxD1KK5IHXYlOXpyuNb5Z9ujAAb5KD4_hWWL_NWlLZkFi2_pRCEnnnRemR0W4sfBPXNjcH1fvMNCJBiWauewyQRy1E57lSCOX1g9_zmocORhr4YLjMXFhd3jdX8kVtbmJvv2xs7iMw8LASH-Vu19hQvYuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7103294b05.mp4?token=hUCm7LfU6w4PTBLm5mQlJgyPw510T9ks899uTSiBhlDaOX5-1Y8RJpUwRrGOThAtj19pPrWkF16BYmZmof3NoR8_O0nGwVPpmKhjb_muEaOCVAacaMAp9sr0zR87TNQoR5xWm6GRBx4kKMl6boQ_xlEDKtDtMl_IuI4z7hBfgCFw4KzbgAlza2KZifL2IxD1KK5IHXYlOXpyuNb5Z9ujAAb5KD4_hWWL_NWlLZkFi2_pRCEnnnRemR0W4sfBPXNjcH1fvMNCJBiWauewyQRy1E57lSCOX1g9_zmocORhr4YLjMXFhd3jdX8kVtbmJvv2xs7iMw8LASH-Vu19hQvYuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گستاخی نتانیاهو با تهدید ایران به جنگ سوم
🔹
نخست‌وزیر رژیم صهیونیستی شامگاه سه‌شنبه با ادعای اینکه تاکنون دو بار جنگ را به ایران تحمیل کرده، تهدید کرد که در صورت لزوم برای سومین‌بار هم تکرار خواهد شد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445757" target="_blank">📅 04:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1BwPMomXPe-ZtFJeeB7FTWSX5u1VYeX_cHk71jqIcrPQiInDeRHKKi36UjTp5fREl3gst--qYF3IAFyxo_XGfb74JWTJF4P4VpiTCxW4BgWUUrQ9oYtrQG8Nqk75lQgve562WMHLJf7HWT9w-fWa-Fy9ZIAoxRr-1LcFGWJsuu41eHYadjH3Y97wudSQjmIrKtcD7EYkUFjx883mUyouK9-zcnYS7h-bzsDl9viz8ltJ_s_cYuc_oSRGddLfnvvilurlfPGp2i0QHOrx_QtMtftWVFBZQNWFXzkhJP8lKCrOGrAdSXpGocdL1mgiQuT54z-S8AKJ78Qwc-VkrghIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
دیدار مکزیک و اکوادور به‌دلیل شرایط نامساعد جوی و خطر رعدوبرق با تأخیر ۳۰ دقیقه‌ای شروع خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445756" target="_blank">📅 04:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e5ab27a5c.mp4?token=Pz4tvsk-_Y-8Qdovxvz5BmMl3pB11HwNF8q0Orf3Lzk39dlATqYkAWuJH4-1_yUFf46fdGRc2LQvYRoqqWCBBVnFGxknLLlc5l9tWiBK3hCWN3HlNWlDO71h83gcTqwsg9REUAevreJKMj8ewRConTTlQvcwyMZ4k8DfLH0VK5RYoc2HXap0sEWJiS4rHx1mEd8k6ayvxs_zICCOCW-HacqoAYnI-95JW6q5F9xFCZJHXe9iorXTEjoLom_9R-hTsagsNsNEfuBWjGhp2tsJSqqE9PHkshgnWt-Xb0sTPlEfwZZK_-78pohSq6TO6ftzoave0WHn4LEh6IBpfuQELg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e5ab27a5c.mp4?token=Pz4tvsk-_Y-8Qdovxvz5BmMl3pB11HwNF8q0Orf3Lzk39dlATqYkAWuJH4-1_yUFf46fdGRc2LQvYRoqqWCBBVnFGxknLLlc5l9tWiBK3hCWN3HlNWlDO71h83gcTqwsg9REUAevreJKMj8ewRConTTlQvcwyMZ4k8DfLH0VK5RYoc2HXap0sEWJiS4rHx1mEd8k6ayvxs_zICCOCW-HacqoAYnI-95JW6q5F9xFCZJHXe9iorXTEjoLom_9R-hTsagsNsNEfuBWjGhp2tsJSqqE9PHkshgnWt-Xb0sTPlEfwZZK_-78pohSq6TO6ftzoave0WHn4LEh6IBpfuQELg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کم‌کم به آخرین دیدارمان نزدیک می‌شویم
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/445755" target="_blank">📅 04:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c88c09b130.mp4?token=kRBYyZQzyBmUoEFPEWNxc9CezsB97CJOOKINtdQMD5jDxqcC154opaWG2U1hSZZ0PZkJ2GqppTVL7s_0_9wtK1Dq_apci2RpPvgFhMtqZRn29F1EpFDaVDl4eFnTuOUcUNZDk_DjgSCr3n92zLa54rTvJK2KKLWNH-v2f8sPixA5RD_K99t4Qb3ZYpjzFakDr0dEtg3WG9CwdDp13H2x0adlmQJEw7C81oW9h0CoLKnXgq9XeHNreZiMAzQeCoqInuwlBEM78CWbYYMkr4F1VC5bt9WUyIDCJKAP3oFATpD6kiVbRaixzbWLJe988Xzt_wIIFMoTY5xDrQ6XjMYasg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c88c09b130.mp4?token=kRBYyZQzyBmUoEFPEWNxc9CezsB97CJOOKINtdQMD5jDxqcC154opaWG2U1hSZZ0PZkJ2GqppTVL7s_0_9wtK1Dq_apci2RpPvgFhMtqZRn29F1EpFDaVDl4eFnTuOUcUNZDk_DjgSCr3n92zLa54rTvJK2KKLWNH-v2f8sPixA5RD_K99t4Qb3ZYpjzFakDr0dEtg3WG9CwdDp13H2x0adlmQJEw7C81oW9h0CoLKnXgq9XeHNreZiMAzQeCoqInuwlBEM78CWbYYMkr4F1VC5bt9WUyIDCJKAP3oFATpD6kiVbRaixzbWLJe988Xzt_wIIFMoTY5xDrQ6XjMYasg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف جدید اسرائیل به آسیب‌پذیری مقابل قدرت موشکی ایران
🔹
مدیر سازمان پدافند موشکی اسرائیل گفت که این رژیم در جریان جنگ اخیر، با بمباران‌های بی‌سابقه و مداوم از سوی ایران مواجه شده است.
🔹
به‌همین دلیل وزارت جنگ اسرائیل در حال انجام آزمایش‌های جامع روی سامانۀ گنبد آهنین برای مرتفع کردن معایب آن است.
🎥
فیلم: لحظۀ اصابت موشک ایران به نزدیکی سایت هسته‌ای دیمونا در یکم فروردین‌ماه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/445754" target="_blank">📅 03:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pBqXi-pevSTFX_634uy-olS5bK0Z7KdLINMZGvdmIoMvs_mgUy_Aq84chPMvihuP7VBKYmSTLJGy-wL9ReOS9A2jh6bZWn_maYPj_PmKhftXJ4VVtcSB6NrpxdqqLMHuxbhHHgwQEAfmtaJpslJxgkPrBClCpPk9XkTac4WtJ79r_QssxYo9xXwblfS1O9ude2KgP5HZVfGxr_t7LphZvZ9fixOtOaaPzG_-b7HzFyp1gilgbIDxkuHMo8zFMksQgZKOz2Reh9KKl1Q-85LQrkHRoplAQ69r01M6ThN9NBLW9qmAqTl7Y03kG1sahGhTNHIc5RceOaqNRZzY0StR8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راهنمای محل پارکینگ‌ها در روز تشییع رهبر شهید
🔹
با توجه به ممنوعیت تردد خودروهای شخصی در هستۀ مرکزی شهر، شهروندان و مسافران می‌توانند از ۲۴ پارکینگ منتخب استفاده کرده و ادامۀ مسیر را از طریق ناوگان عمومی طی کنند.
🔗
جزئیات هر پارکینگ را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445753" target="_blank">📅 03:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/utZ6vSijbQg2n8vm4Buc8d2ZyibI6V5vset_7vTBl9XMVPvrVhO-hUiMJsXa73xvbz6LumDQiiXRECp4_rnZVMvXq2uURBmQoj_dZlkV0Scd-uix8cEZjACzrNKXZN0z5PTwQAaS78DePlEz8hIcKiRW7mfBKla519d-sjH-hqavvH4AezpAARZt5ad7L9rK4TNzUf7uy63fUHigDDPgWl1XrBqVhFZ_bivn5usYdSKI7WBQwC0XbJdk76ROVLz_e46vgciK0paOZyfCcPygSI-piHIfx7cZedqMaOkcIl9IsMIPkeWMHU2RxOmn6MyFvQqi7NQXyFTRJZJGDy_Arw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امباپه و یاران سوئد را زیر پا له کردند
چه تیمی حریف خروس‌ها می‌شود؟
شاگردان دشان رویای قهرمانی در سر دارند
⚽️
جام‌جهانی ۲۰۲۶
فرانسه ۳ - ۰ سوئد
@Sportfars</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/445752" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">جزئیات بیمۀ شرکت‌کنندگان در مراسم وداع و تشییع رهبر شهید انقلاب
🔹
بیمۀ شرکت‌کنندگان و دست‌اندرکاران، از ساعت ۶ صبح ۱۲ تیرماه آغاز و تا یک ساعت پس از تدفین و اتمام مراسم معتبر می‌باشد.
🔹
تعهدات بخش مسئولیت ستاد برگزاری مراسم، معادل دیۀ ماه حرام به مبلغ ۲ میلیارد و ۸۰۰ میلیون تومان، و هزینه‌های پزشکی ناشی از حادثه در بخش مسئولیت ستاد، ۵۰ میلیون تومان برای هر نفر است.
🔹
میزان تعهد درمورد فوت شرکت‌کنندگان یا برگزارکنندگان در طول مراسم ۲۰۰ میلیون تومان و هزینه‌های پزشکی، تا سقف ۴۰ میلیون تومان برای هر نفر می‌باشد.
🔹
در موارد نقص یا شکستگی عضو در طول مراسم نیز صرفاً پرداخت هزینه‌های درمان صورت می‌گیرد.
🔸
تمام ارائۀ خدمات از طریق شرکت بیمۀ ایران انجام می‌شود و شرکت‌کنندگان در صورت وجود خسارت باید از بیمۀ ایران موضوع را پیگیری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/445751" target="_blank">📅 01:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445750">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
به گزارش منابع خبری در غزه، ارتش رژیم صهیونیستی درحال بمباران شمال‌شرق شهر خان‌یونس در جنوب نوار غزه است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/445750" target="_blank">📅 01:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445749">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ماجرای قطع مصاحبۀ قالیباف در شبکۀ خبر
🔹
مصاحبۀ محمدباقر قالیباف، رئیس مجلس شورای اسلامی، در گفت‌وگوی ویژۀ خبری صداوسیما پیش از پایان کامل سخنان او متوقف شد.
🔹
هم‌زمان، کانال رسمی آقای قالیباف نیز با انتشار پیامی از قطع شدن این گفت‌وگو خبر داد. این موضوع واکنش‌ها و گمانه‌زنی‌های مختلفی را در شبکه‌های اجتماعی به‌دنبال داشت.
🔹
براساس اعلام صداوسیما در پاسخ به پیگیری خبرنگار فارس، بخش دوم این گفت‌وگو قرار است روز بعد (چهارشنبه شب) پخش شود. به‌گفتۀ صداوسیما این مسئله در پایان برنامه به‌صورت زیرنویس نیز نمایش داده شده بود.
🔹
این مصاحبه که به موضوع پرسش‌های مرتبط با تفاهم‌نامۀ ایران و آمریکا اختصاص داشت، به‌صورت ضبط‌شده از تلویزیون پخش شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farsna/445749" target="_blank">📅 01:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445748">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0af691b7.mp4?token=oKEJoxYSJXsaL8wbyWnNlFJzi14ctLdMTOdiB4VC0aHtISbxubT8CReC9h2TTw1M1fo43S8B99h17khB_4v3EB9_5WMOuwISjpopaKQ0CMP-YiealowmBA2GB4RXJEKfHkwTA4bVT05aG0jr8EWxXpamU4pgHvFNhwbojdC0arUFp3on-QVnTYGAsb5Tv0P9tLD1bShsZ9iIUrYr6t8KBPU3Cip-CNLLxkYy0HoYHcjZKmmSkXY1zGWXrrA5QTW9NVGHz6cwDW4eyUo7Hb9lRPwLcjW00S1fPPFfdQGiZhZKhwH3t0f5-BGHBlOPagq9Ggeg0X4ZcakhbAiv4LKJWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0af691b7.mp4?token=oKEJoxYSJXsaL8wbyWnNlFJzi14ctLdMTOdiB4VC0aHtISbxubT8CReC9h2TTw1M1fo43S8B99h17khB_4v3EB9_5WMOuwISjpopaKQ0CMP-YiealowmBA2GB4RXJEKfHkwTA4bVT05aG0jr8EWxXpamU4pgHvFNhwbojdC0arUFp3on-QVnTYGAsb5Tv0P9tLD1bShsZ9iIUrYr6t8KBPU3Cip-CNLLxkYy0HoYHcjZKmmSkXY1zGWXrrA5QTW9NVGHz6cwDW4eyUo7Hb9lRPwLcjW00S1fPPFfdQGiZhZKhwH3t0f5-BGHBlOPagq9Ggeg0X4ZcakhbAiv4LKJWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار حسن‌زاده: ورودی‌های تهران در ایام وداع و تشییع باز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/445748" target="_blank">📅 01:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445747">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrzzV1wFcXUfPZjvy5d4ja7ejoyggv6r1S2DLvSoR-F8ihrt6KPuo9Bxt2W6lqWSwqg3qSrBt0ZA2XglfhgqkhhFbMPECtufChkbRZfDbr5HpZfLhlaNw_7Ct10W-wJvz95-0XNzVG8JqtYhH7FF2HNzAGa4iZ54aZN-LOHWEgPxlqHoaI0TG2jcNYL6jV_ZWluFtyw_k3lBz5xpmdQdKqVpJ5NFexFudN8-rDqxSeBPbxNClVpUi1Bzkg8tnntVvQB7f7V2uRjomRg7wANaYwNZh8vHaYRgmizgGeAc_CogdaXpQ8t_UXKsYl0V9eiNZeTfze0iU6WbXuql2somwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سخنگوی ستاد تشییع رهبر شهید انقلاب: پیکر مطهر امام شهیدمان تاکنون نه به خاک سپرده شده و نه به ودیعه دفن شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/445747" target="_blank">📅 00:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445746">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">کتاب آه</div>
  <div class="tg-doc-extra">قسمت ۱۶</div>
</div>
<a href="https://t.me/farsna/445746" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۱۵ – کتاب آه</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/445746" target="_blank">📅 00:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445745">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGunk2IshTY_Nho1F9hyRkPxriPVK-06ajEtpKNu7SX3TRWOZBQeZJ6SctOx_GJlKLhjm1w97HnGZe1n7kCDKmepL0DuEcpJOp2fPJ5fjxZOpaGtkNO0dRrMc6TbAiv8nHIK8k9Tc8wUVWbKg1sal9hl8BKp3fNmrrOPB4yBodTxcDcm5oz4JiZC2ez2TzDhoX9sm6Z0-Bs9HtvfKecBszWIyZgelZRdq6eDGSyeT-So2QL1c_0XHISLHzo75qUeRupfyYA4WNWiTOR9fi3x62cJ4F0BUOOFe4j08wYQ5CWa-BfwVEcO1Mcb2LfmSe6vIXm6kDvlLGSBvJwr6ngNog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین سخن امام
🔹
پس از شهادت امام صادق(ع)، «ابوبصیر» که از یاران نزدیک و نابینای امام بود، برای عرض تسلیت به خانه امام رفت.
🔹
در آنجا با همسر امام، «حمیده خاتون» (مادر امام کاظم (ع)) دیدار کرد. حمیده خاتون با دیدن ابوبصیر به یاد روزهای آخر عمر امام افتاد و به شدت گریست.
🔹
سپس حمیده خاتون گفت: «ای ابوبصیر، اگر در ساعت احتضار و آخرین لحظات عمر امام اینجا بودی، صحنه عجیبی را می‌دیدی. امام در همان حال که جانی در بدن نداشتند، ناگهان چشم‌های خود را باز کردند و فرمودند: «همین الآن تمام خویشاوندان و نزدیکان مرا جمع کنید تا همه بر بالین من حاضر شوند.»
🔹
حمیده خاتون ادامه داد: «ما متعجب شدیم اما دستور امام را انجام دادیم و هیچ‌کس از بستگان نبود مگر اینکه او را فراخواندیم و همه دور بستر امام جمع شدند. وقتی امام نگاهی به جمع حاضر انداختند، آخرین سخن و وصیت کلیدی خود را فرمودند و سپس چشم از جهان فروبستند.
🔹
امام فرمودند: همانا شفاعت ما [در قیامت] هرگز به کسی که نماز را سبک بشمارد و به آن بی‌اهمیت باشد، نخواهد رسید.»
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farsna/445745" target="_blank">📅 00:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445744">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1daa516da0.mp4?token=LXtzIfT4jN5UQt7aebN6m4M9gxGhl6paNYTDM3Nf77pOmv-WtTDBiakae6HkDD3t4uLSTZNkiQkO0E3ebBfQW8xmP63fPW7cxLq0E52jiq2fUYcTSxYZbKE5AuNth7IvC8JFTbe1HxVf_Y1EfNXHlw7Jr-7bLXMlnul2wXDyR-L9FW5w6WiaL6685KjcFng4IkcQtSTHSljsVziP0u4EqDZ9bk3_nqaghdWVca-pfSbTi308Th_mgWUYnwjxeFXpq2E_1sTZ5mVvHWZO7PEeOiAGbDqnbXfqi1fE5iLmS_Sypts-FHddIr07acis1lzT7t6bYF6WKWnkSSirWr2dn1sfpQUfvWN1zf60XUtJ9taMn7ck9I6O93FN5REEL5OlDLNBPNgbPI99ORz9KrK30hnJww4UnDOMwrN0-SGfLpdqEbd5u2jaewIds0tk2alFx_BT7IOCA2AmaOY-Y3dwwtdnqGJb_9PXXhodCXiVKpSy_ix250fSgrcS27Mwq7GkeqhUTCIvNBybt3rfbqNQoeN6oUc3DhsTLfk3X_EZXdySvo_ziwp8te7VAJyzbCzb_rfsR46FXucut58Ip7kF_zjPl-xEiWHXV8tLaeiMG_sUmL5QELVqxtELuiOruvIz7BjD754_Aegw3FqiJC_cyK_chdIN76pOiBABU5ek9O4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1daa516da0.mp4?token=LXtzIfT4jN5UQt7aebN6m4M9gxGhl6paNYTDM3Nf77pOmv-WtTDBiakae6HkDD3t4uLSTZNkiQkO0E3ebBfQW8xmP63fPW7cxLq0E52jiq2fUYcTSxYZbKE5AuNth7IvC8JFTbe1HxVf_Y1EfNXHlw7Jr-7bLXMlnul2wXDyR-L9FW5w6WiaL6685KjcFng4IkcQtSTHSljsVziP0u4EqDZ9bk3_nqaghdWVca-pfSbTi308Th_mgWUYnwjxeFXpq2E_1sTZ5mVvHWZO7PEeOiAGbDqnbXfqi1fE5iLmS_Sypts-FHddIr07acis1lzT7t6bYF6WKWnkSSirWr2dn1sfpQUfvWN1zf60XUtJ9taMn7ck9I6O93FN5REEL5OlDLNBPNgbPI99ORz9KrK30hnJww4UnDOMwrN0-SGfLpdqEbd5u2jaewIds0tk2alFx_BT7IOCA2AmaOY-Y3dwwtdnqGJb_9PXXhodCXiVKpSy_ix250fSgrcS27Mwq7GkeqhUTCIvNBybt3rfbqNQoeN6oUc3DhsTLfk3X_EZXdySvo_ziwp8te7VAJyzbCzb_rfsR46FXucut58Ip7kF_zjPl-xEiWHXV8tLaeiMG_sUmL5QELVqxtELuiOruvIz7BjD754_Aegw3FqiJC_cyK_chdIN76pOiBABU5ek9O4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۲۲ حماسه مردم در امتداد سواحل تنگه هرمز
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/445744" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445743">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28eff41b9d.mp4?token=b69Xp4Ua_3iTHd_ZURJfDqDVBOkbKkaSUP-5qWKZSzx9ChtPCgokkelBGWfKmDoXIiCko6-R4QtjT_Jg1lSP6Plvyj3Vrc0tboJ1XjHxbZTDJUaBR0Fl_8DgMeBpPCV-Fn1UKO8Ie9gmakqc6cgg9FmsMKUPmlW6AyLy_FtaDzoZgWYg23g8AMI5TseCee-MK4S2U_S-ZAOOZs4MlH8yDLhWlBXG__Hfz6RVyWJkPuw8Oxdhn6ZRnhY4K3VejaLnqiBuiIYDojl2eHIjrBME1_Ni8jaDTAe2_xvokShCazRMswnkDpWdG8-6DkkXjEWnGWOfVOUWiqFcrD3ZZrmEXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28eff41b9d.mp4?token=b69Xp4Ua_3iTHd_ZURJfDqDVBOkbKkaSUP-5qWKZSzx9ChtPCgokkelBGWfKmDoXIiCko6-R4QtjT_Jg1lSP6Plvyj3Vrc0tboJ1XjHxbZTDJUaBR0Fl_8DgMeBpPCV-Fn1UKO8Ie9gmakqc6cgg9FmsMKUPmlW6AyLy_FtaDzoZgWYg23g8AMI5TseCee-MK4S2U_S-ZAOOZs4MlH8yDLhWlBXG__Hfz6RVyWJkPuw8Oxdhn6ZRnhY4K3VejaLnqiBuiIYDojl2eHIjrBME1_Ni8jaDTAe2_xvokShCazRMswnkDpWdG8-6DkkXjEWnGWOfVOUWiqFcrD3ZZrmEXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
ما اهل کوفه نیستیم، اهل ایرانیم
🔸
ما بی‌وفاها نیستیم، مرد میدانیم
اجتماع مردم بجنورد در قرار ۱۲۲
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445743" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445741">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34c345c6f0.mp4?token=JCfzkuCFWIHJU7JDsbeVh3yzyq9BxMHRGGNq_AWsCGVt-59qUb_XgyVnkd4N9hRC_l93YpJ2FHSJnXc0xghxOkK77JftrX8Pb3ZoBJNiz54exoNR23GLhj4komDluBpUDtsDES5Glv_tPeKcBidr5t_MLE1oLJzSU-uE75N72Ny07xvnp302JCBD59ofAWappjzaNZnAWo4EPW6W4ibXkfA4R1Ure1Vkrs1zvi46Nay7LPrYt88su3EVUh2WFb_5yPWNAKhCUmO4tXN4jESdlyW4oZqGo_q4_vGAjbxJWxJv0NdBYW1WVOQFnblcApx25zJDMrqN04WINt18B7lvnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34c345c6f0.mp4?token=JCfzkuCFWIHJU7JDsbeVh3yzyq9BxMHRGGNq_AWsCGVt-59qUb_XgyVnkd4N9hRC_l93YpJ2FHSJnXc0xghxOkK77JftrX8Pb3ZoBJNiz54exoNR23GLhj4komDluBpUDtsDES5Glv_tPeKcBidr5t_MLE1oLJzSU-uE75N72Ny07xvnp302JCBD59ofAWappjzaNZnAWo4EPW6W4ibXkfA4R1Ure1Vkrs1zvi46Nay7LPrYt88su3EVUh2WFb_5yPWNAKhCUmO4tXN4jESdlyW4oZqGo_q4_vGAjbxJWxJv0NdBYW1WVOQFnblcApx25zJDMrqN04WINt18B7lvnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خروج قطار از ریل در آمریکا
🔹
خروج قطار از ریل در پنسیلوانیای آمریکا، پلیس را وادار کرد تا برای ساکنان منطقه دستور پناه‌گیری در محل صادر کند.
🔹
پلیس تخمین می‌زند که دست‌کم بین ۵ تا ۱۰ واگن از ریل خارج شده‌اند.
🔹
هنوز جزئیاتی از تلفات احتمالی این حادثه اعلام نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445741" target="_blank">📅 23:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445740">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6276572559.mp4?token=VhKMMOtF4PWxPjGPeAPriENh9b064W9h8yrzW4cemDAx-0fnOPDwCFaF77lLcA1-C__8bkfPKDY5mOi_4OhsBMehWuUnBBYxAIqUgju2OM7Z2J3j3C0nGTjunlUv8cbWdnC4hTEhU5lNq5FezT48bLFbj2VObC6aYOjBbju6Ho-OeVDY8Ea45xoBlgIOnULLrt3VdlVBmxZEaY-1PHIeMbT6H4cCsbAU5v4K5RAJ-ZB2LruB4hc-EBXbGnDIEE-Tvw42lBPLICbhT83c0OuhOdvsMEEa33VcqWf6FmeswyTBNRe5Emi81QVlcC5IrLj-JvShHtUAD0COUVlI4ArlGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6276572559.mp4?token=VhKMMOtF4PWxPjGPeAPriENh9b064W9h8yrzW4cemDAx-0fnOPDwCFaF77lLcA1-C__8bkfPKDY5mOi_4OhsBMehWuUnBBYxAIqUgju2OM7Z2J3j3C0nGTjunlUv8cbWdnC4hTEhU5lNq5FezT48bLFbj2VObC6aYOjBbju6Ho-OeVDY8Ea45xoBlgIOnULLrt3VdlVBmxZEaY-1PHIeMbT6H4cCsbAU5v4K5RAJ-ZB2LruB4hc-EBXbGnDIEE-Tvw42lBPLICbhT83c0OuhOdvsMEEa33VcqWf6FmeswyTBNRe5Emi81QVlcC5IrLj-JvShHtUAD0COUVlI4ArlGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس پلیس راهور در برنامه پرچمدار: هیچ وسیله نقلیه‌ای حتی دوچرخه حق ورود به نزدیکی مراسم تشییع رهبر شهید انقلاب در تهران را ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/445740" target="_blank">📅 23:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445739">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg_H0umDyA5gs9IfeR7S45Db77ttHx_d25tnB0CuTEr0GgTEHd_F-nKSJRCsGiivhIif2Vxsivwuu6DCJxVZgMCsq8jnW0gv3ETRghogYXIl_y0kVc42QtTMA0WSankjBk94oENNdsI_Q8gcPI_zQrHWg6jW6eseSGf1F0EJadWi2vr5V0D90L-oIr_YItRiEq9HQq8_vqfZxZL3TRwZVU-I9-2axAns81FtNc0RGIi4gtxYh2vTRw161-Cq0CFM3wOnUlRYdNXg2yHUdqLvyfM0PtsqoZqg1dhn2nMTmUKdJYnkXy4WyOfB3MqoLnmlsLV65CAaOAqyxa3HCEZzPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عراقچی: عراق همانند ایران، درحال آماده‌سازی برای برگزاری مراسم تشییع باشکوه حضرت آیت‌الله العظمی خامنه‌ای است.
@Farsna</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/445739" target="_blank">📅 23:27 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445738">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=UIgpKVMBuxk4yUcNcvJyBha9XD6GF0k-wDlrcW-IV4jsHYSOvH0-7WOiMEy9rNzIFNrN5yC4Lxa_CUd8jIulc7CH03JM5CzQL5qXUyIoqXcIitYhPgIFj2WSAoXLK1JBCAegHaKBfBEv_C-TmDyn3dCseJYLHzoGJkE0W64x3OGYJrlYJDLFtLOmCl7-9OiARIJKTTXUjwFMfnXsQP3EKpZUUM-JJXbEkWSejnxWb9OdH5zfUn1X0FO9BsVtbd7u2e6gY4Pe4MsPEOYlcN7hF-okrfOFemQqMCIAL75-cB2LDngd8EKJmew8E5PSgiymIPhcQvDSehuxnrWV1XUN-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65cdeb5954.mp4?token=UIgpKVMBuxk4yUcNcvJyBha9XD6GF0k-wDlrcW-IV4jsHYSOvH0-7WOiMEy9rNzIFNrN5yC4Lxa_CUd8jIulc7CH03JM5CzQL5qXUyIoqXcIitYhPgIFj2WSAoXLK1JBCAegHaKBfBEv_C-TmDyn3dCseJYLHzoGJkE0W64x3OGYJrlYJDLFtLOmCl7-9OiARIJKTTXUjwFMfnXsQP3EKpZUUM-JJXbEkWSejnxWb9OdH5zfUn1X0FO9BsVtbd7u2e6gY4Pe4MsPEOYlcN7hF-okrfOFemQqMCIAL75-cB2LDngd8EKJmew8E5PSgiymIPhcQvDSehuxnrWV1XUN-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: رفع تحریم‌های نفتی انجام شده است و نفت را ۲۰ درصد گران‌تر می‌فروشیم
🔹
اگر آمریکا بخواهد بجنگد ما هم خوب بلدیم بجنگیم.
🔹
اگر قرار است ما را از فروش نفت محروم کنند هیچکس از نفت منفعت نخواهند برد. @Farsna</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/445738" target="_blank">📅 23:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445737">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujdfq0ey1EdBWr-sMQkNohlzkUVAlK6nsEHdWKbUszymh6MpqxwpWC91vEPI-7VFf842Ym9rKwqZrUcvsd6Npc2M2zQG4INCnl3km7CIgIxGCvbxPO0Rv3qAY8yUjXfbjRxgd_7MUBmGvm2TyPNnDpwB3FglmJNgQVQ3HgV0H2a0ZuBq0EZ6cE2Nty8yr5sNpVrBSXwIFJ7vDaduFgD7k7nbXGvtjB3ydHxyN3cSzBWX4hoXtMIkoreIEI3u3kZsF9YVcuBtCl0TUDSW1n_1OBSkHn4XXQ5QdVX3NRD7Y9NR4oMUBAHmOpEOhCe4v3iCzkcfbDLNmLHoeKIkSXVu2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وایکینگ‌ها به‌پیش!
فیل‌ها هم حریفشان نشدند
رویای هالند و دوستان زنده است
نروژ ۲ - ۱ ساحل عاج
@Sportfars</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/445737" target="_blank">📅 23:00 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445736">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dccf52c2bf.mp4?token=RP1hAqi7NqjuTryBYxSzYd2T7yyy0kV2HQBozSRUe4XqqeGJqtih72Yx9BvTq3_2Fht_1FW03QdgU52-8JvUctAjmNNlq_uLL7BNYWwAqPIiiOHa7BzwF7ht0WFCuqWcO0kShAW7yvJzNq_XL5X4AGvGn2vn1U740fLeMYmnmhbNLdNcgshtQdWaxYS3dYJjOJicBSbC4Jcqzvd9lrkH9GkMWRZVWTiSIAlCvCJ3Bn-_UE6ytq8_rKqzirUtPpCc2Qc8yZkDl2QViL4My3K2oEk08ic8vkLEpR_lWeW8aHBxpNUd7s5qkf_oGvefw6FGOV57akbnm5b_4PjhJeuguQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dccf52c2bf.mp4?token=RP1hAqi7NqjuTryBYxSzYd2T7yyy0kV2HQBozSRUe4XqqeGJqtih72Yx9BvTq3_2Fht_1FW03QdgU52-8JvUctAjmNNlq_uLL7BNYWwAqPIiiOHa7BzwF7ht0WFCuqWcO0kShAW7yvJzNq_XL5X4AGvGn2vn1U740fLeMYmnmhbNLdNcgshtQdWaxYS3dYJjOJicBSbC4Jcqzvd9lrkH9GkMWRZVWTiSIAlCvCJ3Bn-_UE6ytq8_rKqzirUtPpCc2Qc8yZkDl2QViL4My3K2oEk08ic8vkLEpR_lWeW8aHBxpNUd7s5qkf_oGvefw6FGOV57akbnm5b_4PjhJeuguQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قالیباف: رفع تحریم‌های نفتی انجام شده است و نفت را ۲۰ درصد گران‌تر می‌فروشیم
🔹
اگر آمریکا بخواهد بجنگد ما هم خوب بلدیم بجنگیم.
🔹
اگر قرار است ما را از فروش نفت محروم کنند هیچکس از نفت منفعت نخواهند برد. @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/445736" target="_blank">📅 22:56 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445735">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc4d6b8dc9.mp4?token=JG8Df4hw4yjVD5nBh85V7iGB4ES9QZrL4ylDA5J7X1NC7vbFv8tWQSxZHLmJNW2V1R9bnWaWEx2mbB7Doxhu8NxJ0wzKsOfzFRb8-IqJSCP7z9JwhwxtQBM1XDyUqPDO5CrS4y_zphTOBgcq8hfjzDEz0Bvw56nusyUfyX6wmEKvW7DhKW7P8hJiIlUniQMHR7GMjsDPXtxKWsh9hYby_tS0w01wOfNMTJ_flD5qFt5XGJJjGzO81ZhELlZGqVPvg-yNUK9uiIXIcX_Zg7bg28f99CxEMRnjVb9_c30OznRHqEZsLLH4po6r8GYZi-AMwDVUTA7Gpm3-hutwkU-6iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc4d6b8dc9.mp4?token=JG8Df4hw4yjVD5nBh85V7iGB4ES9QZrL4ylDA5J7X1NC7vbFv8tWQSxZHLmJNW2V1R9bnWaWEx2mbB7Doxhu8NxJ0wzKsOfzFRb8-IqJSCP7z9JwhwxtQBM1XDyUqPDO5CrS4y_zphTOBgcq8hfjzDEz0Bvw56nusyUfyX6wmEKvW7DhKW7P8hJiIlUniQMHR7GMjsDPXtxKWsh9hYby_tS0w01wOfNMTJ_flD5qFt5XGJJjGzO81ZhELlZGqVPvg-yNUK9uiIXIcX_Zg7bg28f99CxEMRnjVb9_c30OznRHqEZsLLH4po6r8GYZi-AMwDVUTA7Gpm3-hutwkU-6iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: تنگه هرمز زمانی ارزشمند است که روز‌به‌روز تردد در آن بیشتر شود نه کمتر  نباید تنگه هرمز را به ضد خود تبدیل کنیم. @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/445735" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445734">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3b7ea635.mp4?token=j_w2KoBhL3ph15Le8yz6jok6n9v4gS64-DdEGVNAbvxxzcJkr52ZGGCV4ZoS91ha8Iivk0KoPSqNw1dQmDB2KmqWVwi3J0HaMcrJEsAPYKTFvMOBcj2G9fuc5syoHW3Wpw4ARhEocEzCE-kKPIlMF6bbfYiDed1zcoN1mpahv_9Z2RkSNWIJRntTOlu2T9o6Pjbbf6Ryd-xY4AWLcH71xCEscGPOdHqmh9S0lnCWMRMx1D-_-kOjk3OGRf6-jweYq2PXsoIO5O5s3wMeD0ihW0paHuDd13_Ug8zM-t_mnPblU3w5-s3nGVbKlFvpsHSISLXvaMfJK35pKywVrhahhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3b7ea635.mp4?token=j_w2KoBhL3ph15Le8yz6jok6n9v4gS64-DdEGVNAbvxxzcJkr52ZGGCV4ZoS91ha8Iivk0KoPSqNw1dQmDB2KmqWVwi3J0HaMcrJEsAPYKTFvMOBcj2G9fuc5syoHW3Wpw4ARhEocEzCE-kKPIlMF6bbfYiDed1zcoN1mpahv_9Z2RkSNWIJRntTOlu2T9o6Pjbbf6Ryd-xY4AWLcH71xCEscGPOdHqmh9S0lnCWMRMx1D-_-kOjk3OGRf6-jweYq2PXsoIO5O5s3wMeD0ihW0paHuDd13_Ug8zM-t_mnPblU3w5-s3nGVbKlFvpsHSISLXvaMfJK35pKywVrhahhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف: به‌خاطر مشکلات سیاسی با من حقوق ملت را از بین نبرید
🔹
کسانی که حرف ترامپ فاسق را قبول می‌کنند یک‌بار حرف برادر دینی خود را هم بشنوند. @Farsna</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/445734" target="_blank">📅 22:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445733">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6ebe8f2d1.mp4?token=ZN2htlMAW9MqNgwMMAgvUwiR83MLglOxSTFQYVYSn20MltsioGzV4Vnipi0eS3nONtPOd7mfEueHu-OHSvZFZJ_oqSvoEx-KyA0mBj5lwIWT16KiaIpGaHdw2qEd8xaaFxGFE3DWqIxUCaq42d9MD04pknCAD_tG5zhLZchvQXCjOCkAfAV0wzx4PdSp4nLRk_Y_OEf3CCUFBonIK6NgSF_9W31HY2poUwBYOLs66-Z05yvaIerQnOwjcYKDJoEDieRPbX7VCRYtVDA8J8TA1e9mHbllqRfrl_yG1ha_lJG0jbO2kVk9XI6hik9phxursVYzcBolQMXv79BqBb9GHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6ebe8f2d1.mp4?token=ZN2htlMAW9MqNgwMMAgvUwiR83MLglOxSTFQYVYSn20MltsioGzV4Vnipi0eS3nONtPOd7mfEueHu-OHSvZFZJ_oqSvoEx-KyA0mBj5lwIWT16KiaIpGaHdw2qEd8xaaFxGFE3DWqIxUCaq42d9MD04pknCAD_tG5zhLZchvQXCjOCkAfAV0wzx4PdSp4nLRk_Y_OEf3CCUFBonIK6NgSF_9W31HY2poUwBYOLs66-Z05yvaIerQnOwjcYKDJoEDieRPbX7VCRYtVDA8J8TA1e9mHbllqRfrl_yG1ha_lJG0jbO2kVk9XI6hik9phxursVYzcBolQMXv79BqBb9GHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: عبور از تنگه بدون هزینه فقط برای ۶۰ روز است
🔹
ایران تحت هیچ شرایطی از حقوق خود در تنگه هرمز کوتاه نمی‌آید. @Farsna</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/445733" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445732">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=Rq4KIo8-O8takW76brYWqyt-jlk4gC3rgMnL9NpqwYqgnEuqtbDMqg487ILn-ixUzasx-epjqraP7ZQYvU-KQ6PI-n4JToLSgKLeekORIBxMMNXQaICr4u0Qp0Rnvjtkr7xMzOgW1F7WZhbN-jgCtRTmuMW0fthezpnvCB8Teeoy87c66MPRCGIqd4Fj95Y9w5Uev70Ib4cVUGx77wm-cGl6ASNMPUSLji85Tg1AUnQmlWcFROpeOQvtN8l8hzJsQIkoId7snOL2PZYwOY22nEmGU12dY2lMHVtYOl5IVkGIS4fVOAME_GFUouJKppnznE4hq3rV-8FyID5PxESEzGec9Z8Bekhm36NvpzG_KxXxF_PLinI4PDEvq0hKlvLaCFjrPNs9_fnnYT4Sua8_l0oixJvnEIwjAhH6oGHOTmh5gi3L84ZCBX21KUw403uzeASYCBeYdzZxz7KTSFNhiMPiJ4O4UQyZtLOwBjq5f_lYrEUxAQ7ZjV6wwTZI6i6ASIniRZ6VKkRCgyFwAue2vCnMrDUtaxaq4oHL_jIBeLkECgm7s_NhMdX1k-SyPhWF4oIW88AU6rxM_t8yob7PMtzlIAOiQu24Nd6bJmgPhJOSitnhZsJ9tIAfOZP9y20OQ6vV-iXY1kyHnfxKY5c-iLCnIeIz5zC-48miZqg-mSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/554e01cd3d.mp4?token=Rq4KIo8-O8takW76brYWqyt-jlk4gC3rgMnL9NpqwYqgnEuqtbDMqg487ILn-ixUzasx-epjqraP7ZQYvU-KQ6PI-n4JToLSgKLeekORIBxMMNXQaICr4u0Qp0Rnvjtkr7xMzOgW1F7WZhbN-jgCtRTmuMW0fthezpnvCB8Teeoy87c66MPRCGIqd4Fj95Y9w5Uev70Ib4cVUGx77wm-cGl6ASNMPUSLji85Tg1AUnQmlWcFROpeOQvtN8l8hzJsQIkoId7snOL2PZYwOY22nEmGU12dY2lMHVtYOl5IVkGIS4fVOAME_GFUouJKppnznE4hq3rV-8FyID5PxESEzGec9Z8Bekhm36NvpzG_KxXxF_PLinI4PDEvq0hKlvLaCFjrPNs9_fnnYT4Sua8_l0oixJvnEIwjAhH6oGHOTmh5gi3L84ZCBX21KUw403uzeASYCBeYdzZxz7KTSFNhiMPiJ4O4UQyZtLOwBjq5f_lYrEUxAQ7ZjV6wwTZI6i6ASIniRZ6VKkRCgyFwAue2vCnMrDUtaxaq4oHL_jIBeLkECgm7s_NhMdX1k-SyPhWF4oIW88AU6rxM_t8yob7PMtzlIAOiQu24Nd6bJmgPhJOSitnhZsJ9tIAfOZP9y20OQ6vV-iXY1kyHnfxKY5c-iLCnIeIz5zC-48miZqg-mSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: از روزی که محاصره دریایی برداشته شده تا امروز بیش از ۴۰ میلیون بشکه نفت صادر کردیم.  @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445732" target="_blank">📅 22:49 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445731">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3065cc37d7.mp4?token=simAosgfJMFFsM5694FsORX9v2t1JtiRuGl7goe9pc4AidB4J_CVvgf3IKHbzosR5Qf2n3yKeD3Vke1rXRFxCTemT1xM7ULMuFijqAsULIrmk6FULS5EdrywLeOrrqDIZeTCXolBhX6_hoMFcN9aCCw93PrEfkEJt3n1gPlyeGg_RpNuF2xE9hQsgTuX2woQ8YuQE8-m-2PFlGPVrl1N-34ClJAGfMEHihT_j4HNijAHd-HP_v9K5JcN7dxUTtKCZu41pV97WSTjst88e4BulKesjj26NiveXKeYZI33X_PLNs1FlEcE7BWmbq9Mv04L17ie4lxcpz38wZGlBMbKXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3065cc37d7.mp4?token=simAosgfJMFFsM5694FsORX9v2t1JtiRuGl7goe9pc4AidB4J_CVvgf3IKHbzosR5Qf2n3yKeD3Vke1rXRFxCTemT1xM7ULMuFijqAsULIrmk6FULS5EdrywLeOrrqDIZeTCXolBhX6_hoMFcN9aCCw93PrEfkEJt3n1gPlyeGg_RpNuF2xE9hQsgTuX2woQ8YuQE8-m-2PFlGPVrl1N-34ClJAGfMEHihT_j4HNijAHd-HP_v9K5JcN7dxUTtKCZu41pV97WSTjst88e4BulKesjj26NiveXKeYZI33X_PLNs1FlEcE7BWmbq9Mv04L17ie4lxcpz38wZGlBMbKXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف: محاصره دریایی آمریکا به‌طور کامل پایان یافته است
🔹
این اقدام نتیجه قدرت میدان و دیپلماسی است. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445731" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445730">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01c7cdd6fa.mp4?token=GVh3gZe9P7NZ6WL9B6xnzin11Nf0VFIKwmIkSogGUdNtPvn_i_mwCO5XeQaqo0rS44EWXjFJGbfrHtgoH8NfksiKTzGTWkGUQ461F0Tc2x1HZGqzUmNqbIAe9_ddxRUkDYRskqsgEwKUbJFNSTeuYCPPUZWMpRDJwe6lksPaH4LVrC8BNjconFSGjbzF7kVYEdxdDvx1SImeWlunZkXErbO1jLx00MLRv3wwEtACHn5cQI7-2XxKV7fDonZkRtK5TYCm5wzUKD9bvhxBApM0MzcMCKi8W73pJ6Xo4LjD-mG9wVzMnBHhzC_2GZhjeR8MbTCEFP_yow21CRCgWW3vugcp2kW9qT75oEc2rpN8Z8K4N5NILmpKqYe85DlXBZXtJMhpDmGYmGAhOrHSu8i3M8F7c2FX8Cz2iauQqIqqohhOkPFf5tF0vc8L3mb2P6Nkn0vlsW15TfHfFwvp06O0drFrS_3nVO39qfcbRVTw_tjY_mLb75BSIpdcs2AmDwsx0n3U-CjPWGRDQTN7PiDWBSFzjCkAZjgoTW6cdsQw8Gb1Yz4Mrmqg-mJfr1G-Tqi7lSFjEzZlOacTJuuzXodLFE8P5LQthxSnYM5ujwG5zOvSWmunXDfuXYgJSDcwiDD1m0uDpYfd7BZ1q895RPHT11vK4q0P5t_-ql5QU7O71lY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01c7cdd6fa.mp4?token=GVh3gZe9P7NZ6WL9B6xnzin11Nf0VFIKwmIkSogGUdNtPvn_i_mwCO5XeQaqo0rS44EWXjFJGbfrHtgoH8NfksiKTzGTWkGUQ461F0Tc2x1HZGqzUmNqbIAe9_ddxRUkDYRskqsgEwKUbJFNSTeuYCPPUZWMpRDJwe6lksPaH4LVrC8BNjconFSGjbzF7kVYEdxdDvx1SImeWlunZkXErbO1jLx00MLRv3wwEtACHn5cQI7-2XxKV7fDonZkRtK5TYCm5wzUKD9bvhxBApM0MzcMCKi8W73pJ6Xo4LjD-mG9wVzMnBHhzC_2GZhjeR8MbTCEFP_yow21CRCgWW3vugcp2kW9qT75oEc2rpN8Z8K4N5NILmpKqYe85DlXBZXtJMhpDmGYmGAhOrHSu8i3M8F7c2FX8Cz2iauQqIqqohhOkPFf5tF0vc8L3mb2P6Nkn0vlsW15TfHfFwvp06O0drFrS_3nVO39qfcbRVTw_tjY_mLb75BSIpdcs2AmDwsx0n3U-CjPWGRDQTN7PiDWBSFzjCkAZjgoTW6cdsQw8Gb1Yz4Mrmqg-mJfr1G-Tqi7lSFjEzZlOacTJuuzXodLFE8P5LQthxSnYM5ujwG5zOvSWmunXDfuXYgJSDcwiDD1m0uDpYfd7BZ1q895RPHT11vK4q0P5t_-ql5QU7O71lY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
قالیباف: هرچه برای جنگ آماده‌تر باشیم مذاکره برایمان راحت‌تر است. @Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/445730" target="_blank">📅 22:46 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445729">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‌
🔴
قالیباف: هرکجا زبان منطق برای اجرای تفاهم جلو نرود با زبان زور پیش می‌رویم. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445729" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445728">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🎥
قالیباف: تا ۵ بند اول تحقق پیدا نکند وارد بقیه موارد نمی‌شویم.  @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445728" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445727">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556de6fe10.mp4?token=gyTe4JKDc2w4uboHfZou0ObxCV1JQe9vNv5TXp_wGqWhHhXs2dzB6lwcObUqfvIpyc3dN6i8ErMDOIR43eo2mrTDlU_OtuIMf3rXtvYyEUR4hr50SgzW6ISZHJS0quFNiaXjDo9hhX4mGGQnghi39UEeEcoWlG0DA0t5L6QGLoXKgiMXE7WS8Ty4QIv80mfD3qcqz6XLUJsKXKToWm-n8XcdkmuaxmzDkMY1lrbWq4pf7Ls_cU5Oy2jXifQNJi3ocmc1jjIXnCT4DYB8ibNkk6RZso2eF1o_UDM9DyA_zRALEo1dWaVBpfrEVQ2NN68NsPMHXZoLDYlYAamP3GQxjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556de6fe10.mp4?token=gyTe4JKDc2w4uboHfZou0ObxCV1JQe9vNv5TXp_wGqWhHhXs2dzB6lwcObUqfvIpyc3dN6i8ErMDOIR43eo2mrTDlU_OtuIMf3rXtvYyEUR4hr50SgzW6ISZHJS0quFNiaXjDo9hhX4mGGQnghi39UEeEcoWlG0DA0t5L6QGLoXKgiMXE7WS8Ty4QIv80mfD3qcqz6XLUJsKXKToWm-n8XcdkmuaxmzDkMY1lrbWq4pf7Ls_cU5Oy2jXifQNJi3ocmc1jjIXnCT4DYB8ibNkk6RZso2eF1o_UDM9DyA_zRALEo1dWaVBpfrEVQ2NN68NsPMHXZoLDYlYAamP3GQxjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
قالیباف: غنی‌سازی حق ماست و ما مفاد ان‌پی‌تی را رعایت می‌کنیم. @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/445727" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445726">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‌
🔴
قالیباف: اصلا سر موضوع مقاومت و هسته‌های مقاومت با هیچ‌کسی مذاکره‌ای نداریم. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445726" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445725">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">‌
🔴
قالیباف: ضمانت اجرای تفاهم قدرت خودمان است
🔹
قدرت آفندی و موشکی ما اصلا قابل مذاکره نیست. @Farsna</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/445725" target="_blank">📅 22:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445724">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">‌
🔴
قالیباف: در آمریکا روبیو موضوعات را یک‌جور دنبال می‌کند و ونس هم جور دیگر دنبال می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/445724" target="_blank">📅 22:39 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445723">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‌
🔴
قالیباف: ببینید حزب‌الله و شیخ نعیم قاسم نسبت به تفاهم‌نامه چه موضعی دارند و برخی دوستان ما در داخل چه موضعی دارند.  @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445723" target="_blank">📅 22:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445722">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">‌
🔴
قالیباف: وقتی می‌توانیم گره‌ای را با دست باز کنیم آیا ضرورتی وجود دارد که آن را با دندان باز کنیم؟
🔹
بعد از سفر ما به سوییس حجم آتش‌ها و درگیری‌ها و شهدا در لبنان سیر نزولی داشته است. البته هنوز اشکالاتی وجود دارد. @Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/445722" target="_blank">📅 22:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445721">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‌
🔴
قالیباف: ما به‌خاطر دفاع از لبنان، رژیم صهیونیستی را زدیم
🔹
در عین اینکه این کار را انجام دادیم اجرای تفاهم‌نامه را هم از دشمن مطالبه کردیم. @Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/445721" target="_blank">📅 22:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-445720">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‌
🔴
قالیباف: ما با یک دوست مذاکره نمی‌کنیم
🔹
ما با یک دشمن بدقول مذاکره می‌کنیم که هر لحظه که فرصت پیداکند علیه ما اقدام خواهد کرد. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/445720" target="_blank">📅 22:32 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
