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
<img src="https://cdn4.telesco.pe/file/Jiw9pe1vta3Gog8mIMz1nQVW0XegOH7KG_VvJzsP-GEQmcdKN-PyCwF1eZlxVBLUQkNwPNkKv-XGIuBKCdRd4L3fGyz1lvZTBYMEhmknE00td56WVSuMAxIG9MRWUEOmGkosGtQ7voKUqQDD269zyo3x6rIdpaWfO2InDF1vWIjrarr4tAvLVt5fHSLkdsab0g5Ia37psYObv3tBlm4xCBAp2tWs8CaQa_xqyfK0H7gbBymgPiOj6c3RjCwy1U_ddrVGfLyxyF7KH28VEYyk2vtXRQXbRNJA6NVcCBQS9egSbL1jcvDrUm61CUzHbg_F_ib40binEsXso8SwYUYwuw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 568K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-18 00:16:33</div>
<hr>

<div class="tg-post" id="msg-29342">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2_9-UBEb4pOar93vmvHfM7U5LtJUzRiQGK-gEVO9kSDEu0kPcMUa04Dl4xuAolrInUaVWS4CBm0eALjmKAJ94UcqdYz_QbRJaYyLcBdBKRHR37dwcPv0MDsy8cVz08VxV-pZdrK3DSM0WIi8TS2mhwOtD0zxLGnnYijxsoDzaJ63ci3uNm0BMlsr8kMwgen7zHlqLoN__eWE9xV_qM5l4FQ4R5GTyyb8BZTA9Dpq5-DPtpiI7v-Ak4Aa3HV0dJrJLmVVyy4qHO2tjLnenJzFAvVJ_Kh6dPKfteY3hYpLvwYPEEFK2xktWLjT2Tko-8qjXWkMpbu0VPgeUrIzj7xEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.32K · <a href="https://t.me/persiana_Soccer/29342" target="_blank">📅 00:11 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29341">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51b900e940.mp4?token=kRHHbLprySyHDRP-CvT-FpXGPuoA_2uP_MLCEvVZ6iypxdIoq-2ZDV5Grc--Q7CAAzpQIgwrTRGazcZ7XcRSNtEd4sYzIb_Btmp2lRKQ8WtD6ElfjM29RdZTbr2MJW2ngjlBnIizoyQ1aJBKQpBMo3FR-Co-GY5c91_84m-D4r6nMgyFlaBywL77d_srJ36JKIc0JjSiyjJ1m-dRVCHOJzPEwuGgH7qGtqaJ7qjoEGTtum2ibK-ZiEz4wjomEJc0DhM01tTkwf9Xyk1H6124icm-t48_XTyH8NZs01fNRAhdhv8TZEtfgNpq-hATEvgc4KDAewH2P18k_JEG9rXEgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو سوپر گل دیدنی شهاب زاهدی در بازی امروز جوهر دارالتعظیم در حذفی؛ ضربه سرش رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/29341" target="_blank">📅 23:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29340">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtIVccgzJO7TFRneekJOQDZjjUmu0WdD90ToktTs-KDwbfj9EDco4QWSJ9a7BdeUiB1TaHzfLm0T8BcLO0fxzt-hP3wOzWp266pq3wmpSJvFn4qy-QwXq_KgJMIg8qSgnYWf0YCW8rcefKgrSZtdpE7Wv-kpwj8YCap8LwKKWzADXZM4hjSu4c5GhZDPYNQUQnyb_IIuA9ZuxPX486y-BOKfu2aPnKJ0zAvW_W1s6o71Q95VKtLZoFMFYAeWXYo8aUq7ejDp1y2lGMCHgFdISCtYb7vSxRYvrs0ffl3PmNzuwA18DczU25bNNXetBTBfcxxeDHRcFxTfbE5i6SDpGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/persiana_Soccer/29340" target="_blank">📅 23:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29338">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/29338" target="_blank">📅 23:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29337">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
👤
#تکمیلی؛صحبتهای‌پزشک.پرسپولیس درباره مصدومیت عجیب مهدی زارع درپایان تمرین امروز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/persiana_Soccer/29337" target="_blank">📅 22:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29335">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sFibL4_wOkF9V30_VjIxA97niEN2Muj7T5yA06AGK6dNtfugfS30e8FFRmG-BfYHbHTQLFu24jE5IkxQmZyCJTxPd5OoztgSlycB1oSEk7bwmy9Pjg8D4GEx_GcWI59Xdjv02KrDsdBqL0HRlDqiiVCSMA9VnPLjRvd9u2wlMPSAs7QqlLOykgCpWKvsnumdf0PqJT8gQwnRxw8x2rfnQg-QfDlM_bddA4hzgUS_K_VbaWh_0ehyU4tlLpbSxUnT1dZEqPmCIAMZBVEiRtt09_77NUTLOaKBinTc-GIc1f2GUqr_5SFycTJMNNzUK_fXSi-OzM0kN6k_KAPYOOr2NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pWFqWcAPAvf5QU2D-MfIeZk1mt3fd4VRobLHFxeu9p5vcs6q2XDBD68438kjAZrk5BwRHwvIZLHHdso3VgVbQFI9R17nLM152f8R6DTEAMOqWRKWgBvB1F9NTH8gWPWY0QRePV9Ne0auSW6qsKvhCNDN5ADFVOFwdWYX5fltWwQeXKwfzgpkVI55Pr5BrhJtlPGIPJCo8fFT-A3u40AqAAPqZ49hk7cGxRMDpZ5MQKLBIf1xSK2eseVJTrQPdR9z9jb2nPvbR8qDwsdxE66biYO_x7_DS0-6NW5zw38IUEy3B5347YwwnEQj2tpbsDsRslJwq03w658MpoaG8uXLuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/persiana_Soccer/29335" target="_blank">📅 22:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29334">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=Nfoau2PMfsHfOkf1SB81wWhaZAwnDaqwpqe1xSamGRpB8FL5vEsmAvOz1qTdT97airJlXIUDaCAdJZ_eg_GoqnlQMAeqV_n8w9l5sSnpBSdoYrl-GuNZB7nDLoGUyptdNfziuCI22rmqV1rjXKr20iooySxW_Ng1L_HzUdLrzTmxRSaFz6M2RlJK7_drdeDSmAfndBVul_huRdWiI-22UoG18qp5-OjDiYsErl2llAyJEUb8xvCs8RB9NwyNvOMg07vmY6TNbKWb-ro6J6ZDL6L1DHxXS9ik0zWUB629yxWh6Wb0ndupkyOh_YXRCN4dllwbvmHg-naty939SGthOBhXFeXtaM_aaQbR9OkmgeRXC6za-vImMLYg1_FT1Sn2tCQQ5Mo0Nh9qn9w5RkAGCxDeqFhJH1MA-gLhyXpmHU4qSUD39UYkOHpnfd-GPltdgMCLiJrIVnIrVUB7LzuWHI93peXn65iDuVeQ6pad5OoGVOprmKaLi2pEoFJKG5snfEWoiuDKxQnkqbNROg-c7ij7BAoOw_UUe7uxtsyORNvr0P669p_p2UmY1zdzGLQAPvUaCciA9VLI9MJEwQft4w-zRScKy_bCq28Y4PqvltoSkQngjKhGB9RsvHz40Wyk3c02Yy5yTlcbFzSQ1oq-dHQ3CKeKJzo0fiSZoRCMJ18" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e83f3f081.mp4?token=Nfoau2PMfsHfOkf1SB81wWhaZAwnDaqwpqe1xSamGRpB8FL5vEsmAvOz1qTdT97airJlXIUDaCAdJZ_eg_GoqnlQMAeqV_n8w9l5sSnpBSdoYrl-GuNZB7nDLoGUyptdNfziuCI22rmqV1rjXKr20iooySxW_Ng1L_HzUdLrzTmxRSaFz6M2RlJK7_drdeDSmAfndBVul_huRdWiI-22UoG18qp5-OjDiYsErl2llAyJEUb8xvCs8RB9NwyNvOMg07vmY6TNbKWb-ro6J6ZDL6L1DHxXS9ik0zWUB629yxWh6Wb0ndupkyOh_YXRCN4dllwbvmHg-naty939SGthOBhXFeXtaM_aaQbR9OkmgeRXC6za-vImMLYg1_FT1Sn2tCQQ5Mo0Nh9qn9w5RkAGCxDeqFhJH1MA-gLhyXpmHU4qSUD39UYkOHpnfd-GPltdgMCLiJrIVnIrVUB7LzuWHI93peXn65iDuVeQ6pad5OoGVOprmKaLi2pEoFJKG5snfEWoiuDKxQnkqbNROg-c7ij7BAoOw_UUe7uxtsyORNvr0P669p_p2UmY1zdzGLQAPvUaCciA9VLI9MJEwQft4w-zRScKy_bCq28Y4PqvltoSkQngjKhGB9RsvHz40Wyk3c02Yy5yTlcbFzSQ1oq-dHQ3CKeKJzo0fiSZoRCMJ18" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/29334" target="_blank">📅 22:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29333">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6ay5NHYDZ8m69MAo2O1UxTNeA0JkyMBy4_yoAM8_9m4n9_Dh0d7tesJVZB86zngUwh_WzReNfpx1LMrI5fHu3j23pTdHkxJL2HovB9aQnfeTT2jglSZ0MurrOR-tYGZ9BJV3p3avyICY9ivFORmzkHGNyWJF85JX4Yfp97nsXuHJNd_Hn5XxGEGzS1dHbBzeBc5-moxgGZquR_gvMRVF1mVq0gyw-8Xr7AFxXCYX8o6ZQ4O7JnlwzG12yp_ajEFOV6CXKY7XGaPfshUernXCH04Qoyj8RdBWlxgdDXvH_BgNQV3eeNhi7EUykD616tXlh_hP9Cx7LbHtTIj4ODVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ایننرمیلان هم امشب بااین ترکیب تهاجمی 352 به مصاف‌رئال‌مادریدمیره. مورینیو هم برای چندمین هفته پیاپی یان‌دیومانده خرید 140 میلیون یورویی کهکشانی هارو نیمکت نشین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/29333" target="_blank">📅 22:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29332">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7emQnQv9SWOspBpziPT9Sku9V5zjhRTAyvihejg_hkyf-yJUWHt0HsEemgFGNhu_f7ETq-mHWjMG7HXFv1BoRZzjoJXCmJEeBRwLpMDsKw2-HaD7SrsGPzK4ORyAIOnsXlQsKSxTRr57ZX5WrbM9mHF5W1q363EV5d6D_-VsUvujs9Bo59bZ4y97ghFE0GctHHKjWM_CEa27-y9DfVd4gViub1ENcvSD4MbZUQsWTq4Mr--8zTYaWHtrxNlswsnD7HgIlNkbA1k4I0wuD6YqmKblaW1W51qFs-QGo_r0cXrMO21m5kNFILpH4rSvoC514bigTwkcC5tNeWlFLzF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/29332" target="_blank">📅 22:12 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29331">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iR1_eRXY7W2GEExw1HHGfRP_Y2e9QJMMwDEZqInBD7tAL_OxY1vaHZRb2yNNySRVEFW22oXAEAjNKlGLaAUWVLTllHYnmIX5DTs5LD2Y1C62bbXmC5GMDRypj3v0Ksxi3onV4QJ87DkZwk9wA4TNELM8l0HnrXpGhuYwQxXDnDV06WYfVy2msQORvlNWCd82thGBDqcwIVdwxNVafVp4ZvxQs8Z7SYqdeR6e2VKw0hzaRqMO7tVf1Bauc_QVhWsfE97vk0w-f1HnegMsUhlj_1fp3EtZPazP3DMKA99MiEgOKLbYruYSu0Y4CinOpsMGe272C3L6Nw3MeH0btIcCMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
👤
عملکرد تیم دهوک عراق تحت هدایت یحیی گلمحمدی درفصل‌جدید لیگ برتر عراق: 6 مسابقه، 5 تساوی، 1 پیروزی، قرار گرفتن در رتبه هشتم جدول!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/29331" target="_blank">📅 21:57 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29330">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scAE8TZM7FwEcFEDe8_fD_M_zWUmiTbo2O43_qM88yAa6XN10uGAJUysEkTP9QTvrmFJm-IP8zNHbjl012dyEzoNyPSrRcaQ3Ebf5ekeNzrbw7Y22QazzGNYDNjLBHg4nfn9JilLVv7I3KZ1LtC29AY0Fm2F7nslN19sKL--lZ7qba5tClGy8zTtLQAdkj1jUzBUo_8w0oKpaH46DfzX_46N3lZpT_giPbqIrPWJ-r6gjjhCTMdtBPj3Zevpx8i3YDzikCBrYtxPvzEt00CCUX1GSinOTWy8rGH_JA77L5q_hGLeXWfTiO0ZY_r8gjZekXmPZAh6wkXYA8U3B-0-TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/29330" target="_blank">📅 21:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29329">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BioZb-vyVR1ZUHejTYoY-SJ66f5UhLzgQS_77kaqhtWHKWQaPJ__vvUaTLaZrNiOFMNJcB35VMv4PsyjULjM2KRQYkNRxnY-7j33U2EqG-tWIU4i1t_-Dsr_uxW5yEsM5ITDN8lfA9r6CXJMzNZVGqIOUf_B_TdmkWkpfbQWjLdqv91ycSo457T5HSmlVtDk_7G2pkwpfXCTZgtgjTinJoUdUfTzKOrBo8RArHE2s-z60sRqKvAQv-UztGCHTzVbtfRnLkIb-UvwGBUpM3hDj0VMCSfZDliPtDAfViGNXVHGlIeCmUssF6D0NvXpxdDvxFam0X4wEc5f3oshuX9JHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌چمپیونزلیگ
؛شماتیک‌ترکیب رئال‌مادرید برای دیدار امشب مقابل اینترمیلان؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/29329" target="_blank">📅 21:18 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29328">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/939eacf7b5.mp4?token=hih2Xy_TkY4Vuiaij76QKZzF-TTMAuFhLKLtAP_D50nxlublY0PCmagouoLjFgRh7NraF66dkPbBuwJYnHkmBbB0AJ4CT4_qMk217784MEW2sEQESXFjQEH4OQBS1xpphx5ZwlYEgZIZFZEBu0dq39tvIuU04LFeUr1OyxZAVDJPaQLJuKyhAzRDr_8Eqprp-pc0IcXctSKZSgKrRp3h1-xPzsmJV1yfWuVOZZOfyrxv9I3B57-RS5BLPA9JtjQs-xCf_KhH80SFol7DnwsxYuAw0YYIl54aD7Mk_EotuL2_q0kkIET7aplm_jXzClEvmLpF0XkILfNN6zbCp1ipVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/29328" target="_blank">📅 21:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29327">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d64e7feb91.mp4?token=CQNwFk2oOiaA4N2k7hi95rFGvWeUm87G9mVwLO5xrLA61Uk0n6snrY3sqM8-8AakDD8Cdj4XWJouf7IttlgxchyiQyUBSSgVn8X-NhnXloD8PQK4F0HSzUXS2kUMig8pnoyHv0y2SSYJoF7BNxll35a9fyzIY8SCYakPOQ-DUwOekmeSJJChxoaiK5mJ3n3zcF-9YxvYIDrqg8F5Xm1NJ4f8OZbWRPgisALDVtgXYbj7zwQtOCXCHNEvoMjAlfsJkG87Mpfe-IdGC6i_bQNSGsWGC0LXIZyH1H-O4IZ1-zgNxnZ0VwUCcBjprfD7ZUKQ_nxU0EHDFXr3sYFfDMf_WGv8rcLc7npRppIuBV4dxnEUulPF4iCreQrDei9G_Dr5PEEsbkU51pu4cjNOlAfoJoFRS3U_7ftnPrnm4oBuonPY5j0jVjk_ydXQVfksH3IIlIpvUKBNRF5KH_zgmn3h1SAf6kyXO3LncsV_dmnHnn0OHFw220CEMUxiL-7-H0j4XUPFfaroo4KfmE8rAE5ZujXRtvbxN2ErzW6Xj0i1glipjHnzSxYKf16fvUQrQCMq8bIUhO-mdEt9EptUmSvsktEvgrVJeUJpgX-thTevvXUMeYg3PehVXSN_HoepJKPKFjFzM5cNb_8iPlO119qD_atnoaau3JjINTHe4qsSH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
ویدیویی فوق العاده از دوران درخشان نیمار جونیور فوق‌ستاره سابق تیم ملی برزیل در بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/29327" target="_blank">📅 20:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29326">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbHerOwSqTt5xI9sePputFlz3BL_yOjnRc8-Rq16zGMRU9uk8B9sHirdIJdICN9gNUy1rE3nzjOnIp5T7KzLmcSnFjEF6Qdo0rireQ_KN0MltyD9RR3drlNJnTLE7L40yVqUgwUcUb3U7_J6OMwgr_mOYxIZR9ArupfwB2JdqsoFCBzYxj1_yu5ECUcewTN6CtYyJSEVL3Pq1Mb0qNOpvcWQjJG96iRJte13t5bFI9Li7udO--skYi5jBwChMOPT-WWVKXy9bx2RzTEuDPVEtao8U1eCFVlx1yjSH0w7p1QeqJVKM1Qqs8pcySZbxdOhmbO9E1LrrgODCsfUq2mocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
سامان تورانیان مدافع راست استقلال که در اواخر بازی با آلومینیوم مصدوم و تعویض شد امروز درتمرینات گروهی آبی‌ها شرکت کرد و مشکلی برای دیدار پس فردا مقابل پیکان نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/29326" target="_blank">📅 20:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29325">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ASgS6HDXc8zKqrMt5TA9BwOw50lndc8oXPVZnfeB6oQRPGjSkiBp2wQgmvBDtfDjNpgXsjNYS8T2CaWVYx9GsyNLuWw1ckbpheYRLUKcWCmTO5jl5t6u-4Jh0Kx2VQ1TeSHpGK8BQR0xMXME8mK0raHnXHPYKCQPv3cGNcA4tfMuguDqkt3uSqXvpexN38w56U_cALN-daa4GJ607-ZgYb5JVcg9bA0t732MAgp3br7hj27Q5th4MPy-HWCiPbxGv7155tw0UEFQF0CveaYUUmYNxJk_Y4CGyRjTGL-73pyEyoLdNbsS2SZPCvA49z_i-NTIcELkSg7UnVrT5mGPqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
در فاصله چهار روز تا دیدار با خیبر؛ محمد مهدی زارع مدافع‌میانی‌جوان‌تیم پرسپولیس در پایان تمرین امروز سرخ‌ها هنگام دوش گرفتن پاش به طرز عجیبی دچار بریدگی شد و حدود هشت بخیه خورد. احتمالا خواسته که موهاش رو بزنه پاش رو بریده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/29325" target="_blank">📅 20:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29324">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4y2_gPVqVvapKJUKCxAUiS9myHcip5gXauIyJ1Be5ST-9IuiYU8qIXTWSRy9UMAht9MaAKM8Mg4vkMXXLuKJ04SVo8XY7SHNdhuj6AT3nKe8YgOGZIa1L8jKcqaV76mJYuEcwHWdRjDH4O4vups7AG4AfPivCuHzDaoM521dYbXn5q6mFfZf7MJLcGaFwg-U7anzSwqymv6LmLGt4l5s_Y_ZCRsv81dP8mN4Jrbwh0qo72glrLM4t9_DW3E-N_q3lk4murEUWrlhwogtFrvwWFFAqwuxkki3Drtuq_oamjWxuaeL0w5krBgqEmFle6x7QwE3TU4jMwE-ladRS7ARw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاپایان‌هفته‌ششم‌لیگ‌برتر؛
جواد نکونام، پیروز قربانی و سهراب بختیاری زاده سه سرمربی هستند که تیم‌ هاشون هنوز متحمل شکست نشده است.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29324" target="_blank">📅 20:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29323">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TppZR57SsC1ECAQhrZ0oIMYGMZG2zuF7xkos6ATt1XsFUuAnl4xRM-dVnHTU7jCfWS9Gjivttt7os9y0Ua-nXIk08yNWh3I8OsChDBEbw7D-smOhgTRWCU3y7X4r-mYTeJBinDtbS8ytQ1cwr4Fp6xJFz6uc5VpZ1KPI61tRUCb070ezfmYq1Vv2vKGSAmKshLC1a5VUu1IFwE9Zn0JPP6HUad8a4dnG0B7ahy_-U_G5jXuxDDHIjJvaRW2nZZM2XUi1FiHOf9OWyHTpGFLkJLTRSMNL0aGNM6lHm9kDAo0R49ofGP4abg59IxywSQ1zzxOUbxhdSM-tagLumb4hsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/29323" target="_blank">📅 19:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29322">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hGb4XwN5bSSsQFQ9NrOmioccd-pMBs4Ciy_XL3u1i0gd4tVApI03Yb0587bbJCjG4Zjw2gqh36Q9i7BbeNUz5ETdly6lTGA-_nIUF-rgLhG9T9N7-39SIeBnKXvZmC59rKfTV1bwfhhvxBnJni2MsSqxtMrWNy4dA_X7eU3lyZnxfoJdaRIrB-tmREEx7r3_xfHT_xpoMRCJeSbkg7QTyCawAh4mrZZmDYHau0ACmtrlE2QCy5fr3Kl9TWy7K8fRm_-B3GAgh4unpNSTiRlTtBtfzAW3aiIpy0IhFA-2Z8ZtKIWZRoGpbtq9_hHvS9HzndJY4e8SEzWtWpJ5wTdK5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3830a1509c.mp4?token=hGb4XwN5bSSsQFQ9NrOmioccd-pMBs4Ciy_XL3u1i0gd4tVApI03Yb0587bbJCjG4Zjw2gqh36Q9i7BbeNUz5ETdly6lTGA-_nIUF-rgLhG9T9N7-39SIeBnKXvZmC59rKfTV1bwfhhvxBnJni2MsSqxtMrWNy4dA_X7eU3lyZnxfoJdaRIrB-tmREEx7r3_xfHT_xpoMRCJeSbkg7QTyCawAh4mrZZmDYHau0ACmtrlE2QCy5fr3Kl9TWy7K8fRm_-B3GAgh4unpNSTiRlTtBtfzAW3aiIpy0IhFA-2Z8ZtKIWZRoGpbtq9_hHvS9HzndJY4e8SEzWtWpJ5wTdK5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به سه پاس گلی که نادر محمدی روی پرتاب‌های اوت خودثبت‌کرده‌حالارسانه‌های خارجی معتبر جدی جدی‌ دارند او روبه‌آرسنال و میکل‌آرتتاپیشنهاد میدند که‌در ژانویه این بازیکن رو برای توپچی‌ها جذب کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/29322" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29321">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIItUveZwRjND2tIfH_a3Jm5PTcGDP6oQ_lMbN-5kqc-rgT9edogYZngloIVgp2YnGB784Ly8ZiaDGlNrvRq0eWBvPPkipufa_L4mck3myjaAabx6Y0BIJM4Tfxd7fUAQwVIJWbyn5-pCsg6068xhNrhsr9SM1gKdWrjXx3LkHxFjCMbZuujzeQYQ2bNMM9cOfNTt4JEvt1ZavCYHP7cNjECwX22KySIiUDAxp5BrsyjiaWHNohGsosk2lQfKyDSNq9hgfExmNTPeAB99zY1QgYmDswRpwEr6UZFjlNRa08QkAq5pvsb94Kcs-_4pz0tL1-lno4nBxcXGPw_kU25bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
با حضور لیونل مسی آرژانتینی؛ لیست 30 نفره نامزدهای توپ طلا مشخص شد، مراسم اهدای توپ طلای 2026 روز 4 آبان درلندن برگزار خواهد شد.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/29321" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29320">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJKovoVNMys3kNlEjD_-4x6edSC0i6X7M5om3qwYRcd2BuaNFzRHvZcoIfMbLMhCMqwFdtRMAOjcPf41rMlAsMpfq1zZIwXmkMbFi8NbDv0Gt14ZTvqMnkBAPBEWwnAN8L6E-5J_4TJdw0RwfiRsP1vHJH-i-qUDxlWm17XjCNRGAliFbMOilBkC1xbHmHOUN8dwJFx9M-Qo8lBE3OMGabaj923_yxbNrugDcB5iqbm1X-lbFT9knU7SWUlZeeRJXZYUW6ihE5maG4YjheOXe_qi9MCm863JHVDjf7MwXVEWHG9mwSZ1bo2Bm5vFO49UoqRVWWhmcuOrCXe58CkJow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇪🇸
رئال مادرید
🆚
اینتر
🇮🇹
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/29320" target="_blank">📅 19:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29319">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/197500367e.mp4?token=ATB7vprJvoGUENvcgyovPAoDU_551V3GfxEHYrv-6Q4HcFA1avZyDynjPgBId4vWVb9X-qMjiKbYrJ7cZWMKxKpmCHxeVhx3SaysXdMsKkvNjozGOSaCvmCRTP7u1wdrGoyUVTUGQM8Ve1q-8ITbNAY8uRPyt6TiEEOgIlzKuEce1PDohayZlAzQrrjNxLwzNfAqIWdmWOLrGF0RgtZxJpIeF3ye9_cSByEGE5rAqUbkGDay54x5p_YH17C5dY4MKu1GY8z5r8dk1cCfYBFzzV45iG9b3Bc8VGKLtQpKNBgXHHB21ABgbCqLhYbKL0LWZN9LmM91wNOZtxxFirA6-A1Z-I1hq4PV8ia3W6kITkP9YkCwsD99eEqhphWDr_037srPdaqKxIbrA5V2iZLLZLSC__2ROWxs-J1LUlZwkzszXjdgq5TZudZDc7gttZqWWVRoJ_MlNFTTvybHhMFMvgWHW6TlARRmugoOTzcizzXUz6lelCtWJK17t3Ew6Q-oI_GxjdTHC7D7XqPNj05uT_8ey8mb8hOHNzy2mtAI-K7KtflraUZar_yN1xQvL9k_-MrSxK1ePGUjrKA27eAfSCE8JCYMx-ZbF2sAjlvPiwggEN_BkpY7Wo8UUBn3TA_rw4SWy_rk4InSXj9OClVKkXCQpoxrUZz3jSdoUsFmxig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/197500367e.mp4?token=ATB7vprJvoGUENvcgyovPAoDU_551V3GfxEHYrv-6Q4HcFA1avZyDynjPgBId4vWVb9X-qMjiKbYrJ7cZWMKxKpmCHxeVhx3SaysXdMsKkvNjozGOSaCvmCRTP7u1wdrGoyUVTUGQM8Ve1q-8ITbNAY8uRPyt6TiEEOgIlzKuEce1PDohayZlAzQrrjNxLwzNfAqIWdmWOLrGF0RgtZxJpIeF3ye9_cSByEGE5rAqUbkGDay54x5p_YH17C5dY4MKu1GY8z5r8dk1cCfYBFzzV45iG9b3Bc8VGKLtQpKNBgXHHB21ABgbCqLhYbKL0LWZN9LmM91wNOZtxxFirA6-A1Z-I1hq4PV8ia3W6kITkP9YkCwsD99eEqhphWDr_037srPdaqKxIbrA5V2iZLLZLSC__2ROWxs-J1LUlZwkzszXjdgq5TZudZDc7gttZqWWVRoJ_MlNFTTvybHhMFMvgWHW6TlARRmugoOTzcizzXUz6lelCtWJK17t3Ew6Q-oI_GxjdTHC7D7XqPNj05uT_8ey8mb8hOHNzy2mtAI-K7KtflraUZar_yN1xQvL9k_-MrSxK1ePGUjrKA27eAfSCE8JCYMx-ZbF2sAjlvPiwggEN_BkpY7Wo8UUBn3TA_rw4SWy_rk4InSXj9OClVKkXCQpoxrUZz3jSdoUsFmxig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29319" target="_blank">📅 19:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29318">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqBxV2AQ6vETsvSD9ChCSX1G7YIf7q5CuQN2HwT4bsGe6QwvykrCvOZxH1yY2TMPSdDXH4IZwwc1oRjVslZfx1OEGcHuyGyx6hpd36eFiHLdI38Mqbl_mm3hx1ZYBZlcZoV-U7iEQfwue0E1TmCt6DGSLSqAoi8DySG-PfH6CcWG-EpY6XnoxFvgGOmXItrcII7EeI0t8B-Q8l-lXfAFdZUIIiuMAzjds5ZKh0SfkxO3451HW6HfUt_NloFn-0h6lUqZVeIZypSk5J2vDnEq4J_8IibC_muyf8VAoo4Ay5TNSFw0shrY6QaWslzoCKInQ2gHj6JyCzx2c1DXsShp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
به بهانه شروع فصل جدید چمپیونزلیگ؛ نگاهی بیندازیم به تموم قهرمانان این رقابت‌ها از گذشته تا کنون؛ رئال مادرید با اختلاف زیاد درصد جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/29318" target="_blank">📅 18:55 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29317">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFYgF1y13wXM0rqVk-KiA-fUfWpWDgvFaNVviAoMcweZ84R86QLuYA97xBRGfcsSfA0CT5wsWiwrHhqRmYrIAA94QvZTlvNLrJVV-GXgs_5EpIlTRnv38KGcKMMgm6y4P0qYjusiBSntHvSfEbaJKhuBd95TZQY6Joj1Kvf0u2-PnwGiVMXbMTa64gVMyaVwxTI4Ba_QGMCPlWA6b39jeSQLw1qwvN0cwxDCrGIpEpspX83NhoxBptipWjPKogYVeWeVPUd6gjemVyOSi7Y3Z1j9_JZZEt0zPgHagzlQwzKs_i5Ou6kCWcCFNfA4t3pjvabROhLOBVEXocOHg7ZwsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رکوردداران بیشترین نامزد کسب جایزه توپ طلا در تاریخ؛ کریس رونالدو در صدر جدول قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/29317" target="_blank">📅 18:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29316">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=LeotnZRJThoN9b6Pi2xmJBcrEPlWevC-gAhqbmkuVpkGc0auYANS4H7mfukJ1QUMg1qjFuXV4K4Sk4B88zaVHfyduhm37mqk76QFrb4dPARVkZHTb3m6xvpQpYAGjh9d1NWqIj18ePIamSbth7dIrDi4HJwpfACdAR9AE4uL1OxuakVVr0cz70-CsiD39UBf0VYconuAx1VUKjNnJIO46lDLaFNJzqgTBV0nvO35xN72BWjUtabHIsBWunXfZl_7LzVOjnkPzPRupVsXLkZEktetfuooqpGClcp5MNv8GvYFNdZfMCqg1_U92aJf75LGBlBda3BLq6TogudSvI-Y7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ba4575c98.mp4?token=LeotnZRJThoN9b6Pi2xmJBcrEPlWevC-gAhqbmkuVpkGc0auYANS4H7mfukJ1QUMg1qjFuXV4K4Sk4B88zaVHfyduhm37mqk76QFrb4dPARVkZHTb3m6xvpQpYAGjh9d1NWqIj18ePIamSbth7dIrDi4HJwpfACdAR9AE4uL1OxuakVVr0cz70-CsiD39UBf0VYconuAx1VUKjNnJIO46lDLaFNJzqgTBV0nvO35xN72BWjUtabHIsBWunXfZl_7LzVOjnkPzPRupVsXLkZEktetfuooqpGClcp5MNv8GvYFNdZfMCqg1_U92aJf75LGBlBda3BLq6TogudSvI-Y7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی بعداز مدت‌ها پارتنرت رو راضی میکنی که باهات یه مسابقه فوتبال ببینه؛ هیجانش عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29316" target="_blank">📅 18:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29314">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=REfLaLa8B1i1eIxkva5zeyHjs_Hc9zL1BYz_bffap5iwi06agU6LTz36T07pOIqAWFUpYZngjkmDSfyW0gYDLhaLF31dCvtR0Ndda1vgYmH_O2VapTYb1pdRhK1yo00PqqMnRbeHpdPcyRJMgo3RGoLNyHGifWnfVtpRhI7flbFS6LsHDNYY9TUnY2DpPND8pZL6DgoeTWyaAixOcnbKvSBR_rZ4_rKihJn5Bwm743jtSAt3ZAvMVVEZoaKgMa7BSCW33y248ufU7HZ8QkRb8hFD8CWFFarIV8riHNaRj6XBj1_2e7Rdir-yAAFJEvg1L9v74my50l4Vy6ua7vHh2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaa9ce7068.mp4?token=REfLaLa8B1i1eIxkva5zeyHjs_Hc9zL1BYz_bffap5iwi06agU6LTz36T07pOIqAWFUpYZngjkmDSfyW0gYDLhaLF31dCvtR0Ndda1vgYmH_O2VapTYb1pdRhK1yo00PqqMnRbeHpdPcyRJMgo3RGoLNyHGifWnfVtpRhI7flbFS6LsHDNYY9TUnY2DpPND8pZL6DgoeTWyaAixOcnbKvSBR_rZ4_rKihJn5Bwm743jtSAt3ZAvMVVEZoaKgMa7BSCW33y248ufU7HZ8QkRb8hFD8CWFFarIV8riHNaRj6XBj1_2e7Rdir-yAAFJEvg1L9v74my50l4Vy6ua7vHh2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره بارسا:
"فقط کافیه تیم‌هایی که این اواخر جام بردن رو ببینید؛ تو پاری سن ژرمن همه پرس می‌کنن، اینجا تو بارسا هم سعی می‌کنیم همه‌مون پرس کنیم. در نهایت تو فوتبال امروز اگه ندوی، هر کسی هم که باشی، همه تیم‌ها میبرنت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/29314" target="_blank">📅 17:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29313">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NGJA3tB0W7QzN1c8QlThCkwNaNmac1TGBxQEAQFkQdhZ4jK94kvjB60ZbFRz7ZtC7NO4MwAFa_jEeCs-qcNZEed5ULKnjtJBrIddHMB6l0INoH7WxXzwt-0aFAVVC_JkD5xS6-YDCIMaMiUd09wQ7JWqUZvLS1o_qNAJMJJbgEU0UjRSI7EJ_Je-bjiUKJyJaxmH_Wr9Xow_9iy2uN9akE31TwHUkPR4p8AT2SQSkvhvXu9xHCoN-2PfFq9_0b1FhB02nY4fl5CU_m6eORJ-DpFkK_Zf62y6qQcWWOUabv_KUNu5Nl6m0n9w8uSpx9sld7k3daIWuayTsAe4TJlLcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/29313" target="_blank">📅 17:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29312">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyMM6fq_YQttxFVlvM3fU_a8G1N-QCuaWxcthm6DyjAxvp1TKUTiBYdLVbKR6ubYi7zEbnPtrR0ILSRc5Q-8h39npe9-gl0UgeUqpiLqAfAjoaJdlgca-SFXgE89ArbLZkVY13dXhc-QC0I2j6DzJwWpE-AtCVR44x_7I9R0ebTJ77bK9TQq3z2BIZKTOYJADbLVPGeC57eZvrqGvWyBNRpiMMgHHphL-F83Q_quRaJS3N4fEuYv4mHe0X0OIOQwTCq9ys4D2KaO2BaCJ5fxXLBaKCYsOcK1diOxpzPZG_S0QWOJrlAgLVciawEmLwiy-9KXrgguBw_Uhqgf0Of09g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/29312" target="_blank">📅 17:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29311">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R93EB6xcySV-cOGp_XBTzo_gYg_gP18KZoXP_2-McSBW_dssPSoYXBndFYV4lxWausHIleGfDJUPt0nQJF-ZPD8jUNqVnQl0xutf7Ss1XnFyrkiQZGDVyIjgHQhJf10GLIivkEN6DUuM1YHXBn8A9R6kmuDdIEZF0dNqHzLGOA3rovub_k1OCOMsQ1EfNSv2Y22WfyJVaJ9PrJ7fiHRToH6-9TDj7-Psf67MAqNpAnY6jhS5atDT6iZpaP19qEPEdNm_w3rcGNzuI72mo_i93BhyzCQGzPwiT0mHz3sp24SRAKutOKAhodd18veXYd4O9kxr7I9VlOEGjA9rhuGvAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ اولویت بندی هلدینگ خلیج فارس برای مدیرعاملی تیم‌استقلال مشخص شد: ابتدا علی تاجرنیا، دوم شهاب الدین عزیزی خادم و سوم محمد رجائیان. از بین این 3 تا یکی قطعا بعنوان مدیرعامل جدید آبی پوشان انتخاب و معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29311" target="_blank">📅 16:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29309">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sWY-ENO1T7QlrhRKez5WGtY_9vF6sW9C57o9-PfOof4kHWGaofSAPGDpqX0XV98dlE0U0bJQLbxXIC8J1-0cxQnXZmRZsJzxf5FhLXfFi8ZEfb1sydy6j266RlumhcKw1ccfPjpzY0cO8sYcWEw43r9hukUux8NJZlTXu_-xel26f1EukYAp5H9D27Nus1qYNTpt53f4GDeSctA-j48GaamC0Q7_MBtXDqwDFrEbUQD4Xh0eJbY8ZDhqT8IWyDd0gQT0b-3LWwrjqKFJyIR8M1w7MUeKqhbmN8BV3pm7e9LIQ1FYeeM5lwDxhwCuWcElgt_6RL6O_VKYvbvx6rx2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مادر کوبارسی‌مدافع‌بارسلونا:
اینو حتی خودشم نمیدونه ولی اون هرشب تو خواب حرف میزنه. یه بار رفتم تا ببینم چی‌میگه دیدم داره تو خواب به مارتین میگه خط آفسایدو نگه دار بازیکن تو افساید باسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29309" target="_blank">📅 16:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29308">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
هایلایتی‌ازعملکرد موسی‌چنپو وینگر مالیایی سابق استقلال در تیم جدیدش پانایتولیکوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29308" target="_blank">📅 16:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29307">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vt4bOvzdbnxBJGmgn8Qnfw7p6IaZLF5GlzFU1kM_MlqFBeIDjs_GtL6LXcG7pAeilqj2r4W9s971a5-6FLmf3Ls6YJcpWBznZBFNtFtIdhCpkN4Tc4uSu4AsLRpeMEQrMbb6q-aD_TOXBb5iPt38qzt66jzc0sdUNdlHvw5AYkrZCYPKztWTsYSagKXAmh9l6dbYBNRrd-eZJsNYJhmAwHwhLtKnc72CzkBx9gRk3pIVFcF-L1D-aCd42OhLVl6k377_HQccXEJEEeNVJrqnCHFpi-XOSSTIx8QPfE88pGgyTHGD7bQ4B6Fe_4OL2OLpdekal6CYCeJferbU4eYz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین‌گلزنان‌تاریخ‌رقابت‌های لیگ قهرمانان اروپا به‌مناسبت‌شروع‌فصل جدید این مسابقات از امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/29307" target="_blank">📅 15:42 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29306">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YGy7AvCRogbR8wGoce_YAYdX-Ng5_qFyCDBIOwM1cjKbZkS_NAcba1Ug1rbvkdUeGvx8-wHKS-kStgnZjmMNt8qC_cuAb3DUV2ZBXMboCIeFwvlf88Ghw59-JXk4tYu6eP04gtN8RvVTAqJfnL4xOBp-_VSZuAtDOhCu__1VU1OACoWA0WR4rKHPWsuS_2qhzE5DD1-8Nt6-r5ynpKQ6YQiRfx6u6ihtthUzwsx8gjUgbudRKEO-dmey-nXo_gHwCQEKMKPln3srEGUm5-T2mKW5ADKFVZfjdjvUTUgaO37EHYlJeUCTmzmftRTOZa45DvDwlgoKBk8Cv-ZznFkgMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
👤
به مناسبت شروع فصل جدید چمپیونزلیگ؛ نگاهی بندازیم به‌عملکرد کریس رونالدو بهترین گلزن تاریخ این‌رقابت‌ها با وجود دوری چند ساله از UCL.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29306" target="_blank">📅 15:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29305">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=E47ssO6SJuAua_VwNFEyezpnuMagg-GHe0Sx4Q97IGe_FHS6tvMEpDlwx9FzH7H7rRE0Wvr2w2tBy_6jjFADozuYisvcEOEjOLPMsHWfRLcgOa6KAEElepP24hd730HI5ttpU5Y5mBud1vCNUUijj7po6vsGPvkfbCa4-UipYNdkJGEUQrD7BiHSH477kKGFgOnDDlFiD2798hobeDoHW_JRqJm_dAhvrPgFinAoDcA7U8HUhflHvHjXxMBlajhD6LU-spEK3Khi0SDp62F6U-AwX3ZgeTtC20tYQ24peEJU7HUDtmjl6yPFglCoUxps25GV5Uki3tObF3XV-sFRig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfa4b6c3a4.mp4?token=E47ssO6SJuAua_VwNFEyezpnuMagg-GHe0Sx4Q97IGe_FHS6tvMEpDlwx9FzH7H7rRE0Wvr2w2tBy_6jjFADozuYisvcEOEjOLPMsHWfRLcgOa6KAEElepP24hd730HI5ttpU5Y5mBud1vCNUUijj7po6vsGPvkfbCa4-UipYNdkJGEUQrD7BiHSH477kKGFgOnDDlFiD2798hobeDoHW_JRqJm_dAhvrPgFinAoDcA7U8HUhflHvHjXxMBlajhD6LU-spEK3Khi0SDp62F6U-AwX3ZgeTtC20tYQ24peEJU7HUDtmjl6yPFglCoUxps25GV5Uki3tObF3XV-sFRig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی‌از لیگ جزیره به لالیگا میای؛ برگای رودری ستاره تازه وارد بارسلونا از سطح بازیکنان والنسیا ریخته؛ پنجاه بار گفت داداش اینا خیلی ضعیفن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29305" target="_blank">📅 15:14 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29304">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgXwFaaPoGaAX0jlpju0BohhQhyuIAVHdXgW7ssTdUWYtU49LsrZjbkqJ8IeJD2lZbjXgat_7hXTqYVzvYtaHf-uUH_sOr8v4Z9Bcf0CLYaTpUVBEGjJRY2CvtPsJvc6ya3LA3rcvaFpm2Qt-HRLzcwmW-W8e_1ePXpv8DhDlTyoouTihbQOtNR2Uz2IIkrsko14nyXYP8ik0cnEWq4ST_d1D2yMLPxsMmNHYtkuseYgnUH55FNrVU0yfTClwfuWsJb5wqjJ4hkV7r9TsqRbOR4TW7fov1U03GgbaTtGHN_R6JZSlRd94jG6yivLIxmehUDKxu2fCX1b4gYbwejBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمدرضا شایع به این شکل جواب میثاقی رو داد؛ تو خودت مفت‌بری. دیگه‌از مفت بری حرف نزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/29304" target="_blank">📅 15:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29303">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZH7J7TggoJbQ8uusB6UMs4q75YweS_ySFxZAZfSvNlZ23P5aZeoEQGzjPDHE-DVg6A1izEHOtvz6dwbXANAXLWIrJnS1CsSFjXuLphbsVvd5P3FlSnFrX2Hi4oJTdq56--hxG9s0GlbsFP9xSpdb5wXCTAbCfip3mhDWvIvMmsTCXArduaCtZ4V2z8epjHOgZGUiYjGUihkYDdGRNDJI4dPsTgXTHihXNru6ufEvVkVguGbXZQBeiYyMKEDalCv3dEl9XaBmlH1BpSvHpxaFLdOt6jmAS9Keorcxfz0O4RjHZJ8wg023-hhBOAA6JN96U-CUpmYRaRZRNXa8THV1QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29303" target="_blank">📅 14:27 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29302">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBD4Zgnu2QB1gd8KzIbgmvM-yi2jV9U9J4ggG6PZes-L-KVbkevz8hUAK6IVMUrmIlJC0ADMfpeqPFqvogXQFVoKrP8HbNSMReDR9kp3RWQbQUO2KIcOeJA15nTDBM1ycATegjlXUCT7WGn230VK_dezEL30Um6kOaAog46l8g4OJCqMUMdKnudyDHVt3yUHR2vp00vAo_SeYpnmdxqloGwUgSudo7tDX-kvKLtSXntNVjc8tFZJa9-MXEfPCh0k_S5HLcjp_jpv6wklXyVW_KxCusbzizty54Nf-Bxv8CEqBt5uNKxog-CEBqYuHAZ-E_KfXb0j2odXT5C1rT7ReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هواداران باشگاه فنرباغچه بعد از شکست این تیم مقابل تیم بشیکتاش خواستار برکناری اسماعیل کارتال از هدایت این باشگاه شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/29302" target="_blank">📅 14:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29301">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=UK3AMP-eTWx5Dhxyp2N5Tc3Ky9AHfKlwiuRrfC3yTKL84R-n2o9Wjh_6SeaeAs9sPJZygnm4lF5LT6D5Yqnd7EPtjv50y2YpQI7cvVtVdoL5a1NpA6t5rvoWZfogs4EJJNX4wlkUVZSTWZobWdqkgnvPCxwKiPrspwbcSLnjieWn0YcQ9wQERop21VJc13bQl17dCv7Dqekdn_bskWomYg3BTRxiEi_7_SFP2ZER17DYhqbySl-WEwbW86QLGI4bEaOiCYOWqDdZZlPGg0fVG6VRtEFVdM1fQmpTafa2030OmYgRVh-3L1uZGF_CjJRKsCtmGXVG6LNT0wyB6-QBuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d011bda7dc.mp4?token=UK3AMP-eTWx5Dhxyp2N5Tc3Ky9AHfKlwiuRrfC3yTKL84R-n2o9Wjh_6SeaeAs9sPJZygnm4lF5LT6D5Yqnd7EPtjv50y2YpQI7cvVtVdoL5a1NpA6t5rvoWZfogs4EJJNX4wlkUVZSTWZobWdqkgnvPCxwKiPrspwbcSLnjieWn0YcQ9wQERop21VJc13bQl17dCv7Dqekdn_bskWomYg3BTRxiEi_7_SFP2ZER17DYhqbySl-WEwbW86QLGI4bEaOiCYOWqDdZZlPGg0fVG6VRtEFVdM1fQmpTafa2030OmYgRVh-3L1uZGF_CjJRKsCtmGXVG6LNT0wyB6-QBuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
خولیان‌آلوارز
🆚
بارسا؛انتقالی‌که‌بالاخره‌اتفاق خواهد افتاد؛ رسانه‌های اسپانیایی خبر از تلاش آلوارز برای راضی‌کردن مدیران‌تیم‌‌اتلتیکو برای پیوستن او به بارسا در پنجره نقل و انتقالات نیم فصل خبر میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29301" target="_blank">📅 13:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29300">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCJPOi_nb9pUO-N4wIy54s4cJWqC1_NgAlaKjWpjk_F60ovf5pZO2Ln8LOppYLSM2UhJFg5YY7FqkbXwsmfDKDn-OZOyuKxTxiJWQf5WL9SED_gPwn3dNjTmVIaFKVinG4ZbT4hu2P4SBg_sPTp7V64f2h24ZNxKzZkd4u4x87M64nvxu5w6OsvL69b7_RkY5Zm_3foh4kt7Kk0tDdkFxdBXWf9S7hScT8ilWqz-krAnOxGFkB-i-zil7UvmCdP5-kyBAqkMK_eCB2rzSWP0EL-JSyPja5JTg-qi0qG2ze_GuLGdwS2_sTkgBn1y0I1ZkXbF6UuXDmffu1up2G2enQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29300" target="_blank">📅 13:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29298">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s06Uf2PCBkDXxYuj1962IMI5aSnsxRVK6VqQWioH3ocr6sTz71w-kiNve_koCLF-6PvZG3n_USZTh6GeHCUTAxEOpLLOExic4UHxVDhLeKT9LnM_qtNjRzpAPrp9ylrRt1gA7rsnV1BnSpHNcj2qi9rUuW0gDZFOud3_G8J9LbPSkNrLCyqpGtdNcQjAbZCX0u1stWeAvhXUoq3z_g-78IQieYB8FnSJSYgkaY306XHUfkSq29kWNkqYy1HO-wPFIWiEory2J6P4cg8O1ON-Oc0Xv7DwBKpiz_C4cOmL9IrKizo89auTg7fe1Uod6jXJsCSRWGCqUtdNWoGxFeWFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U8RLHy9ykZD7v8pCNYAeW6MyR015ibnj2MIIDeMc1CMmS4IzucdZOqu5O7CFQuLaDJEDAneOy1MrbasAtiToWK9_tcicqDPUVNgqfYq0fU7TYwl_WR7f5pxq7r_5HNqaHjDRemUGHYBIBstXFlbLKiDZkMDCBQFOLLERZLzbQ_3nVmxI8yuaWZeCs5WsRj2eZCk1f7QlgiRg6paBrtiSlJzKwyog16rGRWd8P_zGESJMU1IREAeqqd7OFzGh0rE7GBiblsNX7BzTnDmuGvZ6P19CxG8WiNm0QhupALOhvWZvUW9yxDBrYytHEwEuhxRwZBDtKGhWWbzvh1Mnp8vF2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اسماعیل کارتال امشب در دیداری حیثیتی و با ستاره‌هاش دو بر یک به بشیکتاس باخت. ولاهوویچ که درجریان‌بازی بااشکرینیار مدافع فنر باغچه بارها درگیری داشت دقیقه 73 گل برتری تیمش رو زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/29298" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29297">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyyIE0oV7ATWAmqnYtGsiNRLz0HREuRvN2MsIhCEqGLFZYaQYzcXL0AbtLc7RpMYvV1FkFc570NKXplD_1KwuFrXzaPDZOJmL8bNso_ffHBEA0ch1dl1GOXGgsj8XguIhz4phmBMH_uBNUyDogtH5Ieo90AhQB325_qTcOWZDJajvztcrmDl6titcddvl-L09yecgqsiPIOtn3IfHicOMIGySrqUKdtJZnbW4j-Payr4TLBlyxGenmaf4L4zdbEi5yzfm8DLi0kAww3ISbA16C3ee_LZ8RrU9G68cOTVtsV_VAYtXkD8K9MZPq2cvpSX8MpY9hI4hqIUnL_bFTMwDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29297" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29296">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omwyTy3ZgxH4ydfG0rSWK8cy8uwBQl1vAojVqsAJi0dqEY8zv0ouxAwSfFYQff6_5UfZ43XBNr5soQakNS-ndFqrdfIPHtssa-utJODwJzclDJG3-NKhEFRYvsgx8DxV-YWR5SboqeB4TI9-bfCgPVGgVVX5VXi3nBri7hK9Qgnq3RwvOHvrkgY6yiFOHbs_SwQVvg2VN2VN8OwV-fWTNMRqrWjv0ij41Ja4KVZagG2OTx8XIzrBsa0x08ufkDwZ2Cs8xMpgnfHmUOgaDCL4b2N0SSQ8eA6OASxORaBY9b0ybqcDKbgowH84CgpU9y2m5-vHOL5y1xs4MIqFQPeHrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته اول لیگ قهرمانان اروپا
🇵🇹
پورتو
🆚
منچستر‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌‌ ‌‌سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⏰
ساعت ۲۲:۳۰
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29296" target="_blank">📅 12:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29295">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tE80mNxQZfg4VZDpSQnJpN3jIiTOoAripR1N1JFqrD6gfsqdJw-5h0a60ujB97bYbAnxG4Tw7e3aAv5G3c2kq5iK3TuG_soy17OgT2B_MuPNZIuMatV32Wf38oY7vLUnMddURFcc43XaklTsOMduEaPAKfv1w4xS3KNLP4SWpX-skY9amAlrbgkssfr0-ZhbmgFlTPokXxHS-RDhnK4QPiAfXCKKx1Dj314GOfAGBK1EVcxp2mwvGhHUezsewxIMTKCKArcoeKWVPuzqwcVbJB5093fMCbNbnDCYfrwX8ZadN0706yW8vJV6skXv0fRbQ0rERYifrdoNfBUx-dQTlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد نیکو ویلیامز، کول پالمر، لامین یامال دزیره دوئه در کل دوران حرفه‌ایشون؛ یامال هر همشون کوچیک‌‌تره از لحاظ سنی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29295" target="_blank">📅 11:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29294">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REG6MATZ5ifdTY1yPskm_YKbPOzBdaqk71zMI6JQtNiEqm8x-bzcEBYRJbKxx1QKU4grQtc0z_j4zuiifchWrikernUqwsQX_vkDTQu3FzndOHcW3t2aBJdlSGfPGvc_EcPomAPYFPb0k6k3MFodysEJkQNtbqd3WhGiS7Fc5Xaeuq7iwke1wqLqoEP13DNqdOloP0GiHVHWTnQmAsqmM1iQTY_9hDX9bksKNQt4Z8OR2RIErO2-OnIQDKLvKPqNMk1cy6zHRjBVZEK9X__OLHq50Hj8CSAHGNckNprFZLwl3b-glPTS9KbEF4FhvzXfnGN5XD-ILFCVP3xdz2AISw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29294" target="_blank">📅 10:56 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29293">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CfPA1tsCdJv2xnsQ5xzVO7-kvLH_hC7zd4rz1T4pbN8BihTQIlItIeCQZhqDH28-bcd6IEh9xESc4hId7okOcZSia0QrnpGo6IVX9p7jtt4YOo1qnbbREmCFSD4GV64IVBWFAi1UHGQ34QvX7pvX8WtYxrSZxidetQo3p-b9yERP4Oot717fVmVIXEU2o-2cKk2EQw_1JF09Kn9vxKQgp7t0MWlZQQ2dxeygIBCJLEbJFBm8CKQ6FFxmM2d4yivNSIKSL1oRAsg8Rubte07mlVnIegLvyJdrRVNCurNZXuHJ3eAcWNBRrfe3ZsdpOioLci7mpba5ZVJUohEuj2dn9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
منظورعادل‌ازاینیکه‌گفت خداداد یه کارایی کرده که فکر میکنه هرکاری کنه کاریش ندارند یعنی این.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29293" target="_blank">📅 10:38 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29292">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jInb9oV8PzyrlRUQ_yTak5xMQobfrEA1qIPJHZvnR80qg6Fzp5NYU0Yah9LLhoj0bTMyRUHHxIUa-jdiPsZTNX33YcaBBkMuWe3otcDwz9ibtVxFqtDuLC-ItopfxDIIndjJxqVjtkuJq9GJ42kuHSVwN3Rk47mkteYXR9NQpL75TskHvOtZ4Z2-XkMRnNtNySz9mZ2tqkxxnwMgnwOVkGTAG-WOoq90qZ-Dj6A-SeHtSehX03JEdOc-ZU5zkXn4xMIO3LaFJSa0qtNb_jfkpH4mOjZhziXBAiND2-zIEX85b_o-dfJhux-UKBcEqls7oNvbNcMNuHWH0TiTPyszpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دنیل گرا مدافع‌مجارستانی پرسپولیس به مدیریت این تیم اعلام کرده با دریافت 400 هزار دلار حاضره قراردادش رو با سرخ‌ها فسخ کنه. به احتمال فراوان بزودی گرا فسخ خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/29292" target="_blank">📅 10:16 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29291">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPGHge9v6PpQDyL2LFZoNJTGpphZVoH4OaYRJI_WdhZy27VhdtAfoN4E8C204Qhk3IAb3X09L23VqwhQYBpdLW2PD8IphdY183gnOAMxCN_eKUqyexvIvBTPfYRvORuNliIhGQOiIuXkZXQ915RBy2wgviULRh1y_Bsuxs8Z2knpSOta5-pZMm9xrBDfBBa6Y29gXUW0q7-UBTq4w9a961AvoAJAJ599NKvHW9mvI-5ElTFiMD4FVnpYJIMQkC0Bb7aS49_1okcjMPN7smceDog2h7CBLqvcYLXlrHqapmBNNliu5-T7JXOygP1OZO6pXD2LGxxxKN62ewCXslo65Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29291" target="_blank">📅 09:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29290">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFejEkcden04Nalmtl7ZwKidv7d-dvMVWSAgAbH10vKJs2T-bBjKYnLedllV_cO4R8MTDFWW4Ru2W0Nbj27jIQhnneHZUCcMXD6ZdAu3qeRIREFXmaraA_xl_4stl0cLWSyU5VSOPETCh-poyOu87lANg3gM46gBgQ95Vbf8-hlHMsktHmg9P7Hr-IkBB-p3JZurayUD7pKKxOY9Gc0N6GaNuzqGwrt9i0-1vwPLTsCnE5_Ceb5k8DF4imZsHoFLNcVjAm35bJo5TyhBZn_GU8zyZVrBsVM85VfBgvzq563KYXQw9hS0qSr_SMhXMkwN_efjGBxILjWX-4qrQ1CXOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29290" target="_blank">📅 09:22 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29289">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره جوان فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29289" target="_blank">📅 01:43 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29287">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhGIQ26dMhOQ1ej8sOELtHFFR-eUI0H1GahsbFtS7EKFgIYc7Rv7Wb7ASb42bQFPcjBNftO2uSRg394TG5oviKWPvZ2Qh2cIItOJQ7dTFi2PbgMG_w5SMmDJ2jo-v1tlms8zgt4SAP_EYx0Y1gvJaDePq3lv5-nsRvBqiA6XPErG1IPUoqY67bzECNacstCftDiTDcLqvauIcwRM2uyJ_JQUmSSPFLIzGUCGvqzAOfQVuf8IBUTPcfAXdsLL8VeLoEJKGw3EKFEatG68X02PRIn4ao6MWJfMSz7m8HsI9I1JKv3caZBAmSb8B6N5rrMKe0TfF79eSSYP55AwceBr_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌‌ امروز
؛ آغاز فصل جدید UCL با میزبانی کهکشانی‌های‌مادرید از تیم سابق آقای خاص!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29287" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29286">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPsklgOZ4YVgs47LPS5bJmcIFZt-hjV_9LqCMr0s6b2dV2IMbTbHnxQh3QP4J1fsKuKafbfjA2_1kg7kDWAv6J7pKaQxj1u27SRX3yuynZzpPjhyzZRybIX7jqohZZROb8MFEEWzNIfThsU2W6FgDTzrUXgDnSpYwaKMSyqKsfrEJ5yy1a-P5mQnnxP0yt8HCGDqeMwofrQRBFgLsCgWZWWiSGJBxDmdJ9dr7dr5AiBMZhWVCTsqxGpFsFsiBd6hScLXgtMytMWfxAxc-E7fXyLf-pfoF6PgOfJgANOr9FxZJpiIxKcfE7CIDiiGxBzuA5eOuSQeaFQ-XbDHIg7zbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
برتری‌ارزشمند پرسپولیسی‌ ها مقابل ذوب‌آهن در پایان هفته ششم لیگ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29286" target="_blank">📅 01:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29285">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuayoV5AMmbrSN1xRxdzfuZWTyN4GZUE2ADFONvW_IY0lyXl4ccm4mZYU7fsRAm3Vj2tC4Bge9I_BD6xCpXHNFzcUqQ4cLcFiRlhZ2fH8wJxZA1XIvyEAe4FtgZkZ8Wwbr6mEJc5yHQFXI7usTAK9PCBBhHCf5i6JkaVOa1ZjCUiYXq0rsjkmfEtwSNkVuzOmB_6bldw75B7a7bGaYgy2UrznKyP0Hxv0VRio7U61WbIBKnjqvBDGaMQmXxTk04Xu02cPzgUhqj9zl_rW4ZEDT1o2vJPf5HupGsVeXIFtMEvlGpjXYdRVKxlVjzQhqmANCOl3DoKM9tbDZkvmP0GXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه پرسپولیس بزودی‌جلسه‌ای رو بانماینده دنیل گرا برای فسخ توافقی قرارداد این بازیکن برگزار خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29285" target="_blank">📅 01:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29284">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gBvLvaoqS3Saa-tkGnkRPnHQPzPc2xew9QaNQEyUKNHwVSbORA2fVlzl2rrxNpS6lP_P6qKyqEyJMhJW7PeF-Wfrmo3euZU2-hGfSVjxYBtYt_azirPGpkyW1rFJ_MGUQTD_yh0R728H7VxAxRIVTTxwYKK2rjx3SVkFDLrWQODFS9WBRBf0C-jYfX8b6fdTpul6G80U9_iK-AfZs4XqdYFDmqeciXAs1iYM5so9Rw9tBhIs9BCYQ9DXARIFOChRyfCmFZxJVZ6ghOHfMmHfnmllJpD35w1lDhgIXsfOpms2NAwso1LtVOVKb6991FS2f0KxDHlHcBc4YgmYAI1KvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
از پس‌فردا دیدارهای هفته هفتم لیگ‌برتر شروع میشه. تراکتور دراهواز به مصاف استقلال خوزستان خواهد رفت و آبی‌های پایتخت با پیکان بازی دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29284" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29283">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=ZNakYpHXsCgPFCoibRygXRX36bakKId-Ga7UstN4MPRvCI2C0okrntQO2rBn5bZ2YxccNspLAPODDh2DDDya0wEyWJY9yK5JikHV88hbULoYTe1h_n_pUjHw97ExLBTEJvzA0y_-v2QoG29qrN_p6JNQ6UCWoM1xD6-IHK_amJd-EwcVfZWUucmdM-MWTaV4ngEsZR3wICrbvjHJl3VtHHhjtS8aYNDw7dHHmfWNS2PdAVpwJTxPIHQf6DAa3tZPXyGP6zZNBBqKM-diolxLozELMa4T4_6Dg1qluPp_uWJrCGp8ke3G18ItxWN4_lioG28zVIQ9xnWQPJ_K53jhrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c1c191903.mp4?token=ZNakYpHXsCgPFCoibRygXRX36bakKId-Ga7UstN4MPRvCI2C0okrntQO2rBn5bZ2YxccNspLAPODDh2DDDya0wEyWJY9yK5JikHV88hbULoYTe1h_n_pUjHw97ExLBTEJvzA0y_-v2QoG29qrN_p6JNQ6UCWoM1xD6-IHK_amJd-EwcVfZWUucmdM-MWTaV4ngEsZR3wICrbvjHJl3VtHHhjtS8aYNDw7dHHmfWNS2PdAVpwJTxPIHQf6DAa3tZPXyGP6zZNBBqKM-diolxLozELMa4T4_6Dg1qluPp_uWJrCGp8ke3G18ItxWN4_lioG28zVIQ9xnWQPJ_K53jhrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این‌ویدیو رواصلا ازدست ندید؛ خنده‌های عادل وقتی عضو هیات‌مدیره‌تراکتور کلمه "بی ناموس" رو به زبان میاره عالیه. تلاش کرد سانسورش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29283" target="_blank">📅 01:11 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29281">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=bVK3EhsCKrbu3QYGjzjtLuKHXRjDUy_CuH17iytIMej8nowJB2DiTbXw8fFAatmH714sS9Vf7_lMZWNYBMaqsZUBt-zO9YC4kG0n3hcD8h8NsMaDnwGwjavbLc-3VtA1HF3u3K_OO0QfxQ2MCc2GUF_CXY4tw_bZaCjLiJSwnChtDNX_VlzOo3BTd4FtFLhDX9nlUiF6BdYdT7F55AN6_aeYoaP0S6y_wKUEA3iPv89qhcRcT2vGWXj40w3-sBaQtkODkZDuZy7opzmy5TDr-xds0Xu4u94wmYINhWTjj9MmdbMFSK87as0eUAyNoDE0oF2TnHBDeOWPY5h5TRw9fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7672fe1ae4.mp4?token=bVK3EhsCKrbu3QYGjzjtLuKHXRjDUy_CuH17iytIMej8nowJB2DiTbXw8fFAatmH714sS9Vf7_lMZWNYBMaqsZUBt-zO9YC4kG0n3hcD8h8NsMaDnwGwjavbLc-3VtA1HF3u3K_OO0QfxQ2MCc2GUF_CXY4tw_bZaCjLiJSwnChtDNX_VlzOo3BTd4FtFLhDX9nlUiF6BdYdT7F55AN6_aeYoaP0S6y_wKUEA3iPv89qhcRcT2vGWXj40w3-sBaQtkODkZDuZy7opzmy5TDr-xds0Xu4u94wmYINhWTjj9MmdbMFSK87as0eUAyNoDE0oF2TnHBDeOWPY5h5TRw9fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
کیلیان‌امباپه ستاره رئال‌مادرید:
من بهترین بازیکن دنیام؛ و با اتفاقاتی که این تابستون رقم زدم، حس میکنم امسال سال خوبیه برای بردن توپ طلا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29281" target="_blank">📅 00:32 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29280">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/932bc654da.mp4?token=QCwmFkeBbNki-ptxIhkOzNKUlFlbXiXxQNhjQBXyYF-csTLyeqn0mZM633UwCTys-eYV4IiiErjsYdqrp-cpBb7SKn31NUQvVuvBvjFu69m3nhQzI4kOEix8tX6aXpj5hcJZQVrgFHOki53EO5Xz4si8x3k081QsnsY83r7VsugcGs5lCgRbNFoiCk1auUOCQkF94PbuSyVXhaerLD4VPdTiCWnm75i1Tsi_pcOy1WErWSm0dtBNMjd5UMYxAPM43Kzfcprup1JjV58ldVOoq9hJLXpgI5BgYG9X9lykdmDhxWvgjauP3POOpaBTDW8avN_tNHJevdxfZPejOSiVrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/932bc654da.mp4?token=QCwmFkeBbNki-ptxIhkOzNKUlFlbXiXxQNhjQBXyYF-csTLyeqn0mZM633UwCTys-eYV4IiiErjsYdqrp-cpBb7SKn31NUQvVuvBvjFu69m3nhQzI4kOEix8tX6aXpj5hcJZQVrgFHOki53EO5Xz4si8x3k081QsnsY83r7VsugcGs5lCgRbNFoiCk1auUOCQkF94PbuSyVXhaerLD4VPdTiCWnm75i1Tsi_pcOy1WErWSm0dtBNMjd5UMYxAPM43Kzfcprup1JjV58ldVOoq9hJLXpgI5BgYG9X9lykdmDhxWvgjauP3POOpaBTDW8avN_tNHJevdxfZPejOSiVrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چه‌دردهایی‌که‌ بافوتبال‌فراموش‌کردیم؛ ویدیویی زیبا ببینیم از یکی از زمین‌های خاکی فوتبال ایران!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29280" target="_blank">📅 00:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29279">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un1ZMkA_OLRog9aCUV_0wjYGweDdKulmrwSDbRzwvRYgsTLkHV5GWxA2cps9iiSrSviWiqmtjOKydnpPf2jsDzVyRu3Kn36JRNvgCE2avOVpxev8wNkK_Jg43yqc3JSOGKFTTwZAp-y_5FnzgzHLEFHeYuOY3XWJl7iCitAgyJozDOYY6gI3loG1tpw0i2GhYqM9JU6qL7aBmmiJuhRe4XK-Gbljs10EzTULsF8cAJcNch_y3vBieBCRvglsHE9XHnueZhL7YR-F5akRhYvxfVSGcDkfBetUzeVYeXYC61IcwfxfigywVO9A3zeg_JZ9SFZi0_vcijFA1IXNzvNflg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه نرخ بنزین در جایگاه سوخت به این شکله که در تصویر مشاهده میکنید؛ نرخ سوم که بنزین لیتری 10 هزار تومانه از 12 امشب اعمال خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/29279" target="_blank">📅 00:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29278">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzUGT9rQjpwO1ZMTl4BBi1BmO_kq1VtaukC2dxQR-gZFxrWMYQFJwj9NdbvZceNwiVa0dnnybt2X3FoDllnwL9zSyj67FSPu8dzhpYgoUWlBaaVWQ2ijX_KP4c2rOc8AA9KrEzyfYOrfmGAAhOJBI-XNVX108bkebR9hSBiTT-SBMXtmAk8VScb0r6_3HOXhz6HAMUKFixNd27rqwfAZRmr0w55u8LtHRYUrwvWS57C14l8tnIq4KYpneKZoVXp0UuYZJ0_yKPhTaqPq4xxCtjX-aq3DNkYICRQAC2c1tn7bXtCvONNjUZ1GWc7J2GisUB39sh0PoVFAII58hsJQnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
ترکیب‌احتمالی و پر ستاره اینترمیلان برای دیدار حساس فرداشب مقابل رئال‌مادرید در هفته اول لیگ قهرمانان اروپا؛ ساعت 22:30 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29278" target="_blank">📅 23:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29277">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BcvoHzC_p04vQtv8hmFJXn55QHv85A6zPYjWwcc8EuhBTGUXpMDaipEkzGA5xpb26k-JGy5YBVflyFQf7afh4XKQCTfC57yz43aWlJEtDqJpqdluB6SDrDo0wn3GkJ0BWOBIdzNJFMQi1IMAVE976iA0ZVlXVb9BTv9bVD9Vb53HxzUre8K4Fk-17SiyhGKSSIUnK2Xl8kE7qSRkBMpfn5OcKrA5z7NX-KeIKnTYHJvdcySJaeHOyvbNUZcxgK3qDk58VLOQkpCUJ5MTHrv5ps6DGyrDqqbjJ8PU994ka5l3ub3EUyJjlXChTkXXvo6MXxNJ4Md30H-KxHJjZDpYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وقتی‌میگن‌فوتبال‌غیرقابل‌پیش‌بینیه یعنی این؛
الهلال اینزاگی امشب با تموم ستاره های گرانقیمتش همچون مارتینلی و واتکینز اونم در خونه دو بر صفر به‌تیم نئوم باخت. حتی نتونستن به‌این‌تیم گل بزنند. نئوم تا پایان هفته ششم  دومسابقه‌باخته‌بود و چهار گلم خورده بود اما امشب کلین شیت شیرین کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29277" target="_blank">📅 23:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29276">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=cQjcrnl9yYFrNLyqjhITH-4IE39mb7WkesxPVH7A7WEv8wMR8J5-Z-jxCl9M0UFNoX6r1QrQ-O6kYlg39RpxDePVrfFiaVMVoQS3-se0c2DKVhJX-tCI-EZbUl0XqmA0MHZ_xQZdJomStLG-7glkgswOZL_h7VVUNOJ1sQ338BulnBFQraKx3J0xy6ueO4GmAb020RtO4EujYmSoV4j96klgOpZUBZAMcwSvHq6hQHstIRPsI0y_rS45LmdhoklSOlZa2dnZhkwdEYI3qZhLxUlqIt_pSPdsqMZMcfCyhqmx798qtAdudYF7OEpuPS3kaql_TiSmpzTxMISaWEuT9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4bb9f937c.mp4?token=cQjcrnl9yYFrNLyqjhITH-4IE39mb7WkesxPVH7A7WEv8wMR8J5-Z-jxCl9M0UFNoX6r1QrQ-O6kYlg39RpxDePVrfFiaVMVoQS3-se0c2DKVhJX-tCI-EZbUl0XqmA0MHZ_xQZdJomStLG-7glkgswOZL_h7VVUNOJ1sQ338BulnBFQraKx3J0xy6ueO4GmAb020RtO4EujYmSoV4j96klgOpZUBZAMcwSvHq6hQHstIRPsI0y_rS45LmdhoklSOlZa2dnZhkwdEYI3qZhLxUlqIt_pSPdsqMZMcfCyhqmx798qtAdudYF7OEpuPS3kaql_TiSmpzTxMISaWEuT9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی هیات‌مدیره‌باشگاه‌تراکتور در گفتگو با عادل: عالیشاه به خداداد‌نگاه‌کرده و گفته خفه شو بی ناموس. فحاشی رو بازیکن گل گهر شروع کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29276" target="_blank">📅 23:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29275">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=YQ3Nsjp9wZW34tRxdT7y0gHohM2ABc7KWmmmsDnkOXw2T-NMMTYGZcgxLa5z-jVy3RbYPnRhwCVyxRldUWyyIAuECCNva2oCnATSfMzXJ3Amssu5qSa50y9YWa7Yyy17IysTDbDCXcrbw9ugs1MZ9tOPi_LA_MhbFrv-ZTY_UUNYamHaAGMQ_bCNacAPrT07MBEVRFzQfHunK8dRjsG4fOXzyOQq8JmWF-G1MFy92oN3txoDFSlWrKQLuEev7j2KgvO05GdpZpYFsRHbbTV45irqPiaMGw6TAjEt05LTcrhn8yamYA9XBalNMn8FkwY10nnN1Dfjvb_DPni9FZqfOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba75a2423.mp4?token=YQ3Nsjp9wZW34tRxdT7y0gHohM2ABc7KWmmmsDnkOXw2T-NMMTYGZcgxLa5z-jVy3RbYPnRhwCVyxRldUWyyIAuECCNva2oCnATSfMzXJ3Amssu5qSa50y9YWa7Yyy17IysTDbDCXcrbw9ugs1MZ9tOPi_LA_MhbFrv-ZTY_UUNYamHaAGMQ_bCNacAPrT07MBEVRFzQfHunK8dRjsG4fOXzyOQq8JmWF-G1MFy92oN3txoDFSlWrKQLuEev7j2KgvO05GdpZpYFsRHbbTV45irqPiaMGw6TAjEt05LTcrhn8yamYA9XBalNMn8FkwY10nnN1Dfjvb_DPni9FZqfOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29275" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29274">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e_Dm5Nl_9oAbnlPmGzynr_jgC_fHwitGZ8MN4GhfT_eswistSL_U7gQ9MznDn5NuuKQc1XQQZfIBWxB5vv4V3Q6XRAgH4Rol_UcxXSC6yA7WTwQLzzBca_-UOt2Qje5tnyuxB7YB_G-xb9DfBaLbHRgFquh0b9RFqNBVtb0UWjsuosRk1vLQxDZpu0mZVZQ9k3S4WxvnW15oRdmevJ-ZvjVKZz3_5Ure_3pIKUF7pEQcZA9XntGI12G0y7lwwvymBVxbESjNt1A21RCQ4TMZQZf4SubF0lFPnYGK2msq6wBY9_8stjI1srx0c71uBsJ8jQefk84VGK_Xg38dzsNGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارشبکه DAZN ایتالیا که روی برد اینتر در بازی با ناپولی شرط بسته بود و 650 هزار دلار برده بود. پست‌برگ‌ریزون ریپلای شده هم حتما بخونید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29274" target="_blank">📅 22:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29273">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gmuikm7WnqLm7gL-tuDj6lc-PhyTE6T-t1M6ktufznqkKVhct2APlXQG_K1jCfcXbJFZeNws1TjbRoFYdlgSePM0O1RJQdTnmaiDb2DInMoNyYi6lZT8oc1Cuk6ltfFZDOO8Xhd-mQ0oqoEB41ojGr_VtWBIjMdQ5vlmJDIWUBBOMo_lZa7286q0YpgdOlrN8ojDuUr6aObFiMu1e-LD4iuUK9GQfkpBYMkqI93EbqoMglvNWjSB-v022PxnV-fg2wExFTIDSs5tb8YQ9czKLqf7TQvXfRzqbwpVX5aBY9LOVt_NFCk573khl54m0sQsPowEEhFTL8vIzXN0DFEQKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
تایید شد؛ با اعلام کمیته انضباطی؛ خداداد عزیزی سرپرست‌تیم تراکتور به‌دلیل فحاشی به امید عالیشاه چهار ماه از همراهی پروشورها محروم شد. عالیشاه هم چهار مسابقه گل گهری‌ها محروم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29273" target="_blank">📅 22:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29272">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">📹
خلاصه دیدار امشب دو تیم پرسپولیس
🆚
ذوب آهن در هفته ششم رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/29272" target="_blank">📅 22:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29270">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FA-jq83zwBrm1cvAjZAPbo8B7cqKNFg2ZmsUDCc_7Y_msO8KsZIdFqKDZ3rJhhDuoCvBghvK5dSJR1cV4s9hHipzqdR77ZFlXpq6NOWzGP_QbRJw7YttoMLJoG4yqcWjF2pR07preHKoCwNr9V9c9StPYCjRKIf-pRCuUeOKNklh1Jm7hBzlE2C2Nx5DvZK6mBz_fqQFHCui-BL0QDAFsr_Tk10EG4WFVgfaqnK29idJwm4aZc2hYA_8mu71Me-O6PqhXPjUz14vpSNHqjFYDDdN_mlZHKnpVFao45iMvl1shZ1UsvweLehCPfffFeZ2LvOhEPR-Ru6Tp_2_3rx51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgT9uaxSnFZXW1ASXJT0iPcW2XLeooRhAin36ZGj4whGYcSS6Jt1Q7piICO1V4KiN5t9S-eV4-TQ6RYatZAOynzT4EBzVIcO1t8omHw5w73N0-Wxab8tFqnk6vhgG3-QJ5pvUzhaE6WdEQ7bGWKyOGbNC-4jOF6C4ddhfmIHU02VtbL8WKHhC0wWmxc4mAmQjpvYgvie5uNHmEanB3m-mpMlM9Y8-68LGCart5vIyXLFXfaulFwie59GdOHBbQUsrT2JSep2nlqSvLVMdXAbXMqZmeyT4K5xeZIlsucqVxCEUi2Pg6NqI7_QB5LegFL_Dqm5L9udgxVwUcJhi-iKVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29270" target="_blank">📅 22:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29268">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vWJJBP-uys8lfdK_YokNH6BGL0ZnUKmFnSuLivE1LBJ6vkm1DxNc688TTXAJIkkustf2RFmAtFIXRPsakzCoyD3x8aMic7OG8ZQVtIGnuBogNV-5PzlzPKISyXH0yevDk1LcA7nRG9jqyw4Z3bxLIs4stE19aI5WdQvG_qmIfCoovwcHGsSNf0haJXjbgSuM4xPlpXopg5YlyRyxuDHYSyqMxCo3p_NcwKo5jfdSiSP-YAbpRvNLAFdXlElIeLtePnq7MRqnudDgUkOwY8K7Pqrncdmmj3DCIxVvHLij8BkWXisFb6_ixy5vSWhkb8hYgG3J9Kuez1U19d1ZsJv8bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bvyc2cmWlb9vulgZZzynnyoml-GVTjmgorySaaWfyzCZK4HXyLafYTzQYXGoILn3niJVpyxa_IdthE-Bnbiq4Q5NAp-4Gk_h5zT7AyqW02gDQCwXKZQFaa99e8QFk-HyYELXGCkJWU6fAKFGvje-A5FAF_A6cQZVPejLtmkf86BQFB1CNBs8ltfbe_50ODu_FhvbfxTHZB0YRYZEkNNSQHGnuqStRpELjnykbQPIv0OdzvxvR8HxqsyNSd_h69tR0yNWrzKQUHqxklCSfsh2M9MXgk8qarHEVV89b6SenBkOCIAGCnks56_ETf0MvTrWBoYd_n64GmQHlMTS53A_pA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟢
🔴
بانوان هوادار تیم فوتبال پرسپولیس در جریان بازی امشب سرخ‌ها مقابل ذوب آهن.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29268" target="_blank">📅 22:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29267">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=Oe0qh-M0XgiMtACp-raM3RiT0rjesJ9er5zBPqXzXEQ996xYp82Wh1aZWxP9k_GWUB4NO3E-pFufsshnknvn0q2Z45Omfy5W3Tyv4Es99U4JUXnjl6SCEL1PyiiDHu4pcTAEFIE-QyALGQw3cmma_Q5bzuiF9z0Bo36Q97OizcdDfVaNL2utfH8YAjBOdIKyfQTJUD42suoQ8nsCFmqqIboflyF-r06s-kGjhsMyU2QrU4497KT_mNC1uBhVEZ-_FnKzfeVKFFCt1qi-zlhw_6XX0GyE2B6k-b4WMbBzDQL3zXGgPxwiAhV2OuvNGxnPr5XvqQscbDjOlxNyF9PnALLl4zg6WRlIo8ND1sntmjtNrdSYBME2l_voMWxW_hh6ql1te__mglZXVJp8EbuUll2mPaeIZ9vl7t6J6li5_Wl1hNXJNlxhIhjfafuols8Zu5aayamJC5fSBAxSZCsOiQLN5qNHKv2USYi7yz15P32KWpSE_m9y1UVI2xo4Qiv8TNby77CHGJqBpXFsytcH6UCyvbbRRwl9RuvBfi7DDAox1Mjqzmu3RbdgStIpKUepjEgyG04ydjBGfr_Nh-SiX6pwwdn0zviwYRuTL1xG77i2kwe29uS455B_WvZiCbicqsAQ2sLkS1VuRN8JIvywnlvmNOYgZms2ziHpisJ1bd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93952feaa3.mp4?token=Oe0qh-M0XgiMtACp-raM3RiT0rjesJ9er5zBPqXzXEQ996xYp82Wh1aZWxP9k_GWUB4NO3E-pFufsshnknvn0q2Z45Omfy5W3Tyv4Es99U4JUXnjl6SCEL1PyiiDHu4pcTAEFIE-QyALGQw3cmma_Q5bzuiF9z0Bo36Q97OizcdDfVaNL2utfH8YAjBOdIKyfQTJUD42suoQ8nsCFmqqIboflyF-r06s-kGjhsMyU2QrU4497KT_mNC1uBhVEZ-_FnKzfeVKFFCt1qi-zlhw_6XX0GyE2B6k-b4WMbBzDQL3zXGgPxwiAhV2OuvNGxnPr5XvqQscbDjOlxNyF9PnALLl4zg6WRlIo8ND1sntmjtNrdSYBME2l_voMWxW_hh6ql1te__mglZXVJp8EbuUll2mPaeIZ9vl7t6J6li5_Wl1hNXJNlxhIhjfafuols8Zu5aayamJC5fSBAxSZCsOiQLN5qNHKv2USYi7yz15P32KWpSE_m9y1UVI2xo4Qiv8TNby77CHGJqBpXFsytcH6UCyvbbRRwl9RuvBfi7DDAox1Mjqzmu3RbdgStIpKUepjEgyG04ydjBGfr_Nh-SiX6pwwdn0zviwYRuTL1xG77i2kwe29uS455B_WvZiCbicqsAQ2sLkS1VuRN8JIvywnlvmNOYgZms2ziHpisJ1bd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اتفاق‌عجیب‌پس‌از پایان بازی امشب دو تیم ذوب آهن و پرسپولیس؛ اعضای تیم ذوب آهن به خطا روی بازیکن خود درمحوطه‌جریمه‌تیم پرسپولیس معترض شدند و VARهم‌صحنه را چک کرد اما داور در نهایت این اعتراض را نپذیرفت و به رختکن رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29267" target="_blank">📅 21:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29266">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hcbl01JRt4sKWfMpHaRrJZ3GtrhDd7Onl0nkoY3bN8tk17OFQBbt2FXLJVl01NUs5JsO2EMdG3CtklS0Qgxas2GJIEqWC47y-UVCZhRZBq62YZQf8BLrnyKyut_JKpNDmFqMFzx__Tc2XxhUOVgvLQO4ahkx7VVW4utHoKIXGIU82D7K2Ub-Mb_dCohtdQ2CR49cvc7Q9lH0tLrL8LCy30iHKXleAd5QtpXeUUZ-6AvgcQ-5zceby5WrnHDmjr3Djt0NmoAdNLs8jtJEb-huU49njRGD1JIZeoPgMnNqV-DjHshZ2ZcxDnAgwmR1qcjzPxWWaKl-jbN3pxpEusGIWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برگاتون‌بریزه؛ یه‌پسر ۱۷ ساله اهل مکزیک بوده و بعدِ اینکه دوست‌دخترش گردنش را مکید، جان باخته. شدت مکش به حدی بوده که باعث تشکیل لخته خون دریکی از رگ‌های گردنش‌شده‌ست. این لخته به سمت مغز حرکت‌کرده و باعث‌سکته‌مغزی‌شدید شده و پسر تنها چند ساعت بعد جان خود…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29266" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29265">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/taUexrbVEuIPKqArCVSQRLVSGzkQdTtMSxT92sJWR7LzecV5uf2FdksHYPuAjCk-6F09AEq3Tmx6fmeLnxxm8g09R0hRjeZtYKuR233cfuj0ett3FwgPlfQcJ1h1lXXmcNnENc2-R5gk9VmLQjtjIvwV5HffVxAtn0M9Q3Y92nFqpzfk-HQCMApSb8qJV0Sgp7-olJ_uz_B7rFPCc0EAjKjiW6b18c2cehhniJkNgAAjCH0f9xKZUNjzY9sYoWa-hTSgpMl-u2RHzQks1YNv_AAtAwteyXnrwBkhS7HbmXMWCRJ9cJ4J9dtjNZbhp3SOOZQzw_gfPSXcKn-sSZxBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ایساک کونده هافبک‌شانزده ساله لیورپول با عقد قراردادی تا سال 2033 به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/29265" target="_blank">📅 21:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29264">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=PRK8nbvBVp48XIuefPaoYLggkyJJSGaGNG7mKc-VRn4c-R5gU-x2TkbtvgqeD3igsWbGVTxgAfpEWEjmoMsF6aLzfc6R3KZeKFVHrw2EKUuActN8e3WEpKAR_dnA9VZNjG8ZYvncAzsNa99qFDZPcsYNwTbREVkGgDEqqo8SO4sYUKg1AOM6is1GM7ZjYj2AulZB9CjFvwIYnsAS9T_F3XuVHLo6SqXZTq--f_ujXNe72KTl-KgaWIP4-UVe3NLoJdaci9nsfVO5q2uvYktVJ9TZWkDO2jv31X7VLzHbaPfPbgvmuW8LSMArMGFBMjy02PhfDvVT85VPYSkGWdgskA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f001dc45.mp4?token=PRK8nbvBVp48XIuefPaoYLggkyJJSGaGNG7mKc-VRn4c-R5gU-x2TkbtvgqeD3igsWbGVTxgAfpEWEjmoMsF6aLzfc6R3KZeKFVHrw2EKUuActN8e3WEpKAR_dnA9VZNjG8ZYvncAzsNa99qFDZPcsYNwTbREVkGgDEqqo8SO4sYUKg1AOM6is1GM7ZjYj2AulZB9CjFvwIYnsAS9T_F3XuVHLo6SqXZTq--f_ujXNe72KTl-KgaWIP4-UVe3NLoJdaci9nsfVO5q2uvYktVJ9TZWkDO2jv31X7VLzHbaPfPbgvmuW8LSMArMGFBMjy02PhfDvVT85VPYSkGWdgskA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم لیگ برتر؛ دشت سه امتیازی ارزشمند شاگردان‌مهدی‌تارتار در دیداری‌خانگی مقابل گاندوها.
🔴
پرسپولیس
2️⃣
-
0️⃣
ذوب‌آهن اصفهان
🟢
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29264" target="_blank">📅 21:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29263">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vhg5GZmiuYNDgBZYDrLZvhHXeAHX77BE5h_y9dszc-hRc_ASbxa0JLd_gLkuOw0Zt2zsMlczAWB-FPWNHvhGd2UbK8Ali-HBkN5_C_3utTRj-xwqmpHoGyFbWdjzrSvF19cNab17n9nw0zEHabuqPpscT0VbAG7Rlfzej2w5gkrsdcaUa0y18flMUcn8JmzrfjG5S8V3U-ke8A_6VyeMYHUMvqErcTI5dazLXiFYL_IpYN8m87q7cgXH6M8hn8UbbqzUunyJYY1mdtrNcHcIcbr13XgJmyqGSaMgqC8LxxmhvctGPFXoK3oZQb7z7v2jb7_VoDWuleLCqH7QE6pnWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29263" target="_blank">📅 20:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29262">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WG8SiGUWQKf-hooRq66XS67q7qLgN_Pz_3CyNHjZg_VTqvO5bYg3gVgavWsevtkt820Y7XlMnVGh0TDLqo5ln06MVdCgRWNgHTFXw3nEl_Qbr5etSbBQcY8FWQNNuQVUWVGfUmN7lJpylz3q463u4udj3p5sbT3g7bEwPCVSaXj3q7U8zAwrLDu7rytZAlfzdEaiZQXU40-46FHt94EXmpOxjNIJaAb0zAljN18k95NOJ4u-PsBgG4jO23oVo328jrGl0-wWr3DXId004PtQaoxbiDK--A62kPcTnlKfA7un1WkE6WLdPpOaYs_AiSZD4ErgA-1UqMw2sNL6FgbA3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
این‌بار علیپپور پاس گل داد؛ گل دوم پرسپولیس به ذوب آهن توسط پوریا شهر ابادی در دقیقه 63
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/29262" target="_blank">📅 20:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29261">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=BEzLbrHA58LXpYgXzFsUXLwEAzPAGR2l-XS3jSjIZYMLJb-ioByID91pFRUMWC47T2DogKllXQ9ibEdpMbsRy85mM1lu2uj8TL9X-jnEz1KRpvgUP-lNF2XSlrU1G5hOHjWmdOOmsxa5UZ0HK0T94oS9fE7QBKeyYqJ4VsbKdqqBwR06Q0LvB4TEKMosNFR5Ckwi6RLQeXVYLhYKgd1HAUi0z7n196vSVQ9mnpmXtpM3AkKk8g89qeHZ96s8C-4BS_c3SAri_4I2Q4_JicLq4ZWjCoVVEBuGC4RCuIza2Ayf5bUyNep2YTA_q8bg8vTAucPPCZg7jJELkaP6RCHyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a13ac35bb6.mp4?token=BEzLbrHA58LXpYgXzFsUXLwEAzPAGR2l-XS3jSjIZYMLJb-ioByID91pFRUMWC47T2DogKllXQ9ibEdpMbsRy85mM1lu2uj8TL9X-jnEz1KRpvgUP-lNF2XSlrU1G5hOHjWmdOOmsxa5UZ0HK0T94oS9fE7QBKeyYqJ4VsbKdqqBwR06Q0LvB4TEKMosNFR5Ckwi6RLQeXVYLhYKgd1HAUi0z7n196vSVQ9mnpmXtpM3AkKk8g89qeHZ96s8C-4BS_c3SAri_4I2Q4_JicLq4ZWjCoVVEBuGC4RCuIza2Ayf5bUyNep2YTA_q8bg8vTAucPPCZg7jJELkaP6RCHyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
روی پاس هوشمندانه مجید عیدی؛ گل اول پرسپولیس به ذوب آهن توسط علی علیپور در دقیقه 41؛ این 96مین‌گل‌علیپور باپیراهن پرسپولیس بود و باعبور از پروین به دومین گلزن تاریخ تیم تبدیل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29261" target="_blank">📅 20:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29260">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOnz6xrfqZjNjkh3Y8LFai2CBbIs49dgFAW4NXqQ1KQkBrRx23iuioFZKbxWu5EDHYDRrZ-uSlxi77RVDcv6Xqs5D53qdY5-idT39tiGurrXMP5YhsoWGiikfDbHOnIih_dm6HHmUuVKavBAgednAArZox4KIZo4K_x30ZdXDGX_juehN7mogMKJqursgfUL56veEfpWu_KBu-hhZLffQgofe7lgmbJyhKEgRyGqul08dQqTuv2t3uxH66kxlyLo6QbMRv1Qc1ppDjLmzEJ9Akt9cWqVZpCMVF8DsgAx8HyN6iXELPHHNn9HCswIpeR7l66AqTwqEz5JSxGWv2mOuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/29260" target="_blank">📅 20:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29259">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f02306a280.mp4?token=Hxh5cyil8AasB_Wh91GwytS1xbS_EiN07Y1MRX4F-bTyjmPd1xCL9FhKF22KIVcTmc7Kc71xnGCFBTrZ8qXGMWZo7za-lkIch2btSQXJEVlymwD-8prpYglz0wLwTZzjfi7MJACOkBNxuoceR5eP9WFWosBLEVcyseNaX227_vK7fQDmF42pogvrk8tumxF-ebo9Iq8XHtSYgqFb1Z7QLJlWSQ1xa1_eCKUEhlEkjzbqFe6ao1Z7yV0gzRZJYZP9Y4yDAylQLl2z9tvQ9RY6LyJfMJkpgPwtwDSnvd-wGNxyyvejqNFhR2-HVQZhE5fNqI0brn5f09rH8gC4J39oxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f02306a280.mp4?token=Hxh5cyil8AasB_Wh91GwytS1xbS_EiN07Y1MRX4F-bTyjmPd1xCL9FhKF22KIVcTmc7Kc71xnGCFBTrZ8qXGMWZo7za-lkIch2btSQXJEVlymwD-8prpYglz0wLwTZzjfi7MJACOkBNxuoceR5eP9WFWosBLEVcyseNaX227_vK7fQDmF42pogvrk8tumxF-ebo9Iq8XHtSYgqFb1Z7QLJlWSQ1xa1_eCKUEhlEkjzbqFe6ao1Z7yV0gzRZJYZP9Y4yDAylQLl2z9tvQ9RY6LyJfMJkpgPwtwDSnvd-wGNxyyvejqNFhR2-HVQZhE5fNqI0brn5f09rH8gC4J39oxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇫🇷
حرکت جالب کیلیان امباپه درنشست خبری قبلِ‌بازی بااینتر بابرداشتن نوشابه روی میز کنفرانس خبری و جایگزین کردن آن با آب به سبک رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/29259" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29258">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=duEGWtHdl6NLaYGU0es9SCMis1AqJANHsIcX-J2Qyg9TNlPLMNg1JaGAIcJI5XI-ERw3URx7LKrl2yILl9Tn5rt1MN218G92cCkSjNjquiGNIS0ahnzEIkFFk61NKZ6V1wVXzEyRasyPZlDMzqSMt8i83t6ca0j1Tnrvi5Ru1XX-fhDt049JO7A4Na8DRtqGcZJEzuUYNAILR5sqSwq8N465rLx_eCvmx-Rj2-lYGeJEk4i_w4xvpT-F6yAxfvY_V23DyfYKBLJ44M1_6kCj68VeoJnuwz1dLcZe4extFk1n1oUjH_Q9E3zyjeai2cT0hkDqkuJVV7HFNxURmdvKLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e921c3810.mp4?token=duEGWtHdl6NLaYGU0es9SCMis1AqJANHsIcX-J2Qyg9TNlPLMNg1JaGAIcJI5XI-ERw3URx7LKrl2yILl9Tn5rt1MN218G92cCkSjNjquiGNIS0ahnzEIkFFk61NKZ6V1wVXzEyRasyPZlDMzqSMt8i83t6ca0j1Tnrvi5Ru1XX-fhDt049JO7A4Na8DRtqGcZJEzuUYNAILR5sqSwq8N465rLx_eCvmx-Rj2-lYGeJEk4i_w4xvpT-F6yAxfvY_V23DyfYKBLJ44M1_6kCj68VeoJnuwz1dLcZe4extFk1n1oUjH_Q9E3zyjeai2cT0hkDqkuJVV7HFNxURmdvKLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد؛ لیست‌بازیکنان پرسپولیس و ذوب آهن برای مسابقه‌امشب؛ بازگشت محمدحسین صادقی به لیست هیجده نفره و غیب ادامه دار دنیل گرا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29258" target="_blank">📅 19:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29257">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=Wfb5oWdB0gILwviBiShE_Fp1JsMVq8PfOUOGy8tbbhFaE0YdPC22xRu-PlCyMKDs6KJao37BzdaVElJIixkv7JI0zyB-uwMFmelFbQB53G0vzNPC5az0JEXqBlqNqvAAT5Aw6WuZ985KNcEFNq_KPXtNaUuCgVRVvtBOf7S6HdAmtZXGclMi_71adexLY-3wuLyP6m5v0G9AD4lYzbL6EyPhffktbExdlB83R7CH7SB039zUdb3tCCvqp4bB6B6Mvbi_mZ9HnBnxan1moa9BE4To6lmvTmgg5lvdGKEOnmGhYWb2ahpgoQdnRMBhyZ9qhO4CeIYcj0MwY4zoV4uPDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e05ba1529.mp4?token=Wfb5oWdB0gILwviBiShE_Fp1JsMVq8PfOUOGy8tbbhFaE0YdPC22xRu-PlCyMKDs6KJao37BzdaVElJIixkv7JI0zyB-uwMFmelFbQB53G0vzNPC5az0JEXqBlqNqvAAT5Aw6WuZ985KNcEFNq_KPXtNaUuCgVRVvtBOf7S6HdAmtZXGclMi_71adexLY-3wuLyP6m5v0G9AD4lYzbL6EyPhffktbExdlB83R7CH7SB039zUdb3tCCvqp4bB6B6Mvbi_mZ9HnBnxan1moa9BE4To6lmvTmgg5lvdGKEOnmGhYWb2ahpgoQdnRMBhyZ9qhO4CeIYcj0MwY4zoV4uPDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
🟢
مسعود محبی مدافع میانی 22 ساله مدنظر استقلال درنیم‌فصل لیگ برتر باز هم با این ضربه سر استثنایی و محکم‌برای‌ خیبرگلزنی کرد. خیبر درپایان مسابقه رو3بر2 به پیکان ساکت الهامی واگذار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29257" target="_blank">📅 19:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29256">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇪🇺
🇪🇸
🇮🇹
هایلایتی‌خاطره‌انگیز از بازی فوق العاده تماشایی و مهیج اینترمیلان و بارسلونا در استادیوم جوزپه مه آتزا دو فصل‌پیش درلیگ قهرمانان اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29256" target="_blank">📅 19:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29255">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TRkybSn1AdUKZkX661N3DJCoCmTnS_JVkdfJgzRdA-ZR-G9Qv72gy0ZplL2KvYdP5Q7EqQjIUmXfiofX3k0DdJh6OJ3BXq9jBoEVL6gij-MfYj_pNn_KSaLHGUEa1P3ime-7DdsT1rIwRogEdVC1VRopE1rkVfYZZRWOUjVaAFIeM0b2tCZ3Wlh2w-PDueh9qX1wdvAA42hjpgdz19qo7qe2s72sLXjRogGz05uVuH6fpKT_ggq87QL4M1IJ7Ad733CToIVam-YSsHIkNQgdd8-YMDVL8VKqUBgPknNg-Gm2b_Orkr6xXruf-BWWSyro6kZlnt_xUNu9RpjIsRoBGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
دلیتا گزارشگرمعروف‌شبکه DAZN ایتالیا که مدعیه امسال‌نیز اینترمیلان قهرمان اسکودتو میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29255" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29254">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=NN6WIf4rEg7y9NarTVVxPReMIE0X1NCdCymCgnAzo1VNTj-uHenp1h0Q6UEwmMO-Ag7fF3XW2jzt3qmTYM0_8M8UA8D4YXmgT3s0cgmrHnzYszGJ7B0dl4YyUU83zddvg91I9cu_Acb4Pi3qk2ZRsxtx5PTl1HS3B9jhbBNvICjBbCuEFAgs2xDPG_yD5QL5OqLJDBoLfj6dAITVLzClk-5cqbnlG2VTNvQ725OyHAHpvP6TVh-4FpI0bI6m6mp7DsMEVuAFJWnwCCoRGpKISbpQ4reX7e8LhUE6pqi2bgQDzzLYdtL_FtZQAIQGb0saZ2X3XwjZf4cLzFsXRK_tug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69cf7a72c6.mp4?token=NN6WIf4rEg7y9NarTVVxPReMIE0X1NCdCymCgnAzo1VNTj-uHenp1h0Q6UEwmMO-Ag7fF3XW2jzt3qmTYM0_8M8UA8D4YXmgT3s0cgmrHnzYszGJ7B0dl4YyUU83zddvg91I9cu_Acb4Pi3qk2ZRsxtx5PTl1HS3B9jhbBNvICjBbCuEFAgs2xDPG_yD5QL5OqLJDBoLfj6dAITVLzClk-5cqbnlG2VTNvQ725OyHAHpvP6TVh-4FpI0bI6m6mp7DsMEVuAFJWnwCCoRGpKISbpQ4reX7e8LhUE6pqi2bgQDzzLYdtL_FtZQAIQGb0saZ2X3XwjZf4cLzFsXRK_tug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکردبرگ‌ریزون ادواردو کاماوینگا در فصل اول حضورش دررئال‌مادرید؛ سال‌گذشته و در بازی امسال عملکرد فاجعه‌ای داشته این ویدیو رو ببینید باورتون نمیشه کاماوینگا تو الکلاسیکو اینجوری بازی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/29254" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29253">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=riXWXfiNhcakuaJD-cOC0kaU7nWYsoOUjCWgl6aOWaVJ3VT-RrrN5SLWfbjNOej6tgOkrJOTDUZzJIO9j6O4H0qcxf517Go2COH5WMZA8P0wMXpfa6sw7S23uNZzymgvvNO4vwRgU0nH1b9Nwcj-gwTYvXZVKo2Z3D3PvGGZAorjWZMDrKiIBanisTHdtDMdUPkGPQ6RUk2NGYhUv2hYzG2KavP9kNi24Wxm8DvRf_Gqhe_SfrcB6njEM3c9wjgkLGl5LDXI-01nURqeCFtSu4kNo5qGyKiqzliUHZf0f-sNznnsjTKl5mk1RICh0GOMTJIEivQWanBLJQ58uRPdnAsP31kdLkG2-ywSh0CHa82Folh4UTaAK1xDOYbUZvGEyU5DBnRuL5KQH6Y7-ZMhM7aRlzbKtaAxJ9rlrWPGmJEyIMNL-DL3K3zZJ3Ltl-RApWoHEpmTOXuc51IoI88qEll06Am6hP8DDCbne_10CWUgjSSlGv_a-rhwewBZj7Sg6FJ0Inebm9fy9RKkEp8T9YZQcYJ17RikBal2Fmd3e11b776ayUy0IFyKRPhRSKoK_xIyIXwBYgWxUf9BBi1OJMTfaT2IZUO60yRGwCdOPSiSoASY0ueJGfT6au49sTJu641MQPbjCEYAUmWQ9cGtpQjVLK91B4tyl8vQMWE38y8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e3cf516a.mp4?token=riXWXfiNhcakuaJD-cOC0kaU7nWYsoOUjCWgl6aOWaVJ3VT-RrrN5SLWfbjNOej6tgOkrJOTDUZzJIO9j6O4H0qcxf517Go2COH5WMZA8P0wMXpfa6sw7S23uNZzymgvvNO4vwRgU0nH1b9Nwcj-gwTYvXZVKo2Z3D3PvGGZAorjWZMDrKiIBanisTHdtDMdUPkGPQ6RUk2NGYhUv2hYzG2KavP9kNi24Wxm8DvRf_Gqhe_SfrcB6njEM3c9wjgkLGl5LDXI-01nURqeCFtSu4kNo5qGyKiqzliUHZf0f-sNznnsjTKl5mk1RICh0GOMTJIEivQWanBLJQ58uRPdnAsP31kdLkG2-ywSh0CHa82Folh4UTaAK1xDOYbUZvGEyU5DBnRuL5KQH6Y7-ZMhM7aRlzbKtaAxJ9rlrWPGmJEyIMNL-DL3K3zZJ3Ltl-RApWoHEpmTOXuc51IoI88qEll06Am6hP8DDCbne_10CWUgjSSlGv_a-rhwewBZj7Sg6FJ0Inebm9fy9RKkEp8T9YZQcYJ17RikBal2Fmd3e11b776ayUy0IFyKRPhRSKoK_xIyIXwBYgWxUf9BBi1OJMTfaT2IZUO60yRGwCdOPSiSoASY0ueJGfT6au49sTJu641MQPbjCEYAUmWQ9cGtpQjVLK91B4tyl8vQMWE38y8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
ویدیویی‌از آنالیزعملکردخط‌دفاعی تیم جواد نکونام که در این فصل با وجود گلر 33 ساله و دو مدافع میانی 33 و 37 ساله گلی دریافت نکرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29253" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29251">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNLwPt3pmMTd1arLla21NZ38cCMX_YKnKIPY9KwklARHy-myY1dKUsaKYzARitdALVKau6ykDqprzvxYGeSm-lc89VATKHySDgGH0lVRRy4K5A3SqKO_pf5hzkpgev06gkyHIkd7dkPWlJyShq_ySWpMcV1KTewmfoBmopeXKkUXkkfxKEn1NzL2jM2nYrykpBAcIpCAWU7h8W6m_KWVhichhQuIVyQLOMdqaGoiHjIfc8JsnI9uRcM5qv1cmwWdkzOuQGEus6xcLFVTX-OTXmBm5LvMJbqQE8ngKARXTtKFLT_gmWWhJbJXLzNz7d-d_ZI_RU7x0fUMgfR0rbbkug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محمدحسین‌صادقی وینگر21ساله پرسپولیس که در پنج‌هفته‌ابتدایی لیگ از لیست سرخپوشان خط خورده بود درتمرینات‌این‌تیم با انگیزه ظاهر شده و از کادر فنی سرخ‌ها خواسته که به او یک فرصت بدهند و در بازی پس فردا با ذوب‌آهن به او بازی بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/29251" target="_blank">📅 18:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29250">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k06fSFZFqk18X2YJo7dVNLNwuXVVY0vrWtUVWwG9rsjguo3WBDxvhaFc3Iz_0cqkrZ5qTDcjnrp04f_CVn3NJuX5aEGODXA0X8UyylRCV7Tgxnl-Tfjjtv_Lr2mLppb9i2MPC9UTzETzCuT00rme7h4fd9-qRIr0sTzbzigPZOLbtpTbDKxuHl2TeftyXphvdjdY7lAbbxBoqdVG4DelutRBbXPIXaadR2-4rfY5VvuoIfq-7s2AyG42nnFxuwm8MDzIijB7h3v9CwIjpHI3FZn3cIsi4R6W9__aJC-1Zlp839d-68zqVET8ab_KyZckN--JS7y7P3wp_gPA34ZPDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29250" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29249">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxDS51psC5PflpNdUD7i5d9WPDeJfEKZYIjPgG6VliLdv4vprZ7bW2J5gN-eTvqdcefChyut2QnGYYQ5t6wf2On-QKQIR8AgVXI5Up8dCpn2PEvwr0ThQ8b1UPXjX-qYF7WT00oMb4m4bx2fdxb_-kPy_grOO7_O59KLWwm9lsitVMwrOkbOp0BMMI0t6OJYzlUAWeqWlphnDrIUFAHHKe8MKaTSt9X_mg1RThVLcK4duvJChdpZTmBKwAdvK9hLzGzl95YYANPZZdOGLSf1BWwv2V_zYmWORYRLLLo5epswnI25fGe4IVXhqoovaBwgRfEjImG1F0dkzPA-d3KfvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ شماتیک‌ترکیب احتمالی پرسپولیس برای دیدار فردا مقابل تیم ذوب آهن اصفهان در هفته ششم؛ به احتمال بسیار زیاد ترکیت تیم تارتار همینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29249" target="_blank">📅 17:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29248">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPqF2VP8BOE3QuAWn3TJoupfd9H9jG8Zv2jOOVIplJiklcUqahBWCt-TfjXiw7wr4pBb85H-rBmg-a904oQgtQ96rmOzRYfr77QQve_zuTf1cck2SY9Zc2tDhUCedaeoZ2FBqM6KT4x17lz2rML_s5jDKpb6DO68hTwVOpDrRDqoIpQnTuY5-L3u6WPSr67SxqLgnLii6MmePI9yI9fclo90Htx_2h4v63ZJ8ZfQF2qzvG0SIHA2snVGOF-PVskrHBoDQruGLtXDNcM7rQLem0QDkB0cLpkU86B9EUF9LJrr6j1x707st9OrRZoUMMxXidRH9VU5Rs_4PgY8J8E35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای‌نشریه‌کوپه: براساس برخی مطالعات و نظرسنجی‌ها، هوادارای بارسا تماشای بازی تیم هانسی فلیک روبه‌رابطه‌جنسی در زندگیشون ترجیح می‌هند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29248" target="_blank">📅 17:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29247">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=YayEyulpzjmSivHvQpv3myH4eJxy3QA7TtlZ9KiZMavtE3xEGBTIzUOi3as9mYMLQBHSw6DKihX_3h3hTIFaKZvYHs0cjJvqwYpIfL64jXvCPxflrWrbdjKGFDkEBUVM9EvwFsxKeKxIYkbgq2famT3SIihfTpjnw8AwSbdL5NgbmnyulPsuPxLNvNwMNpkZBgE3-hT3i_BTQpviHZNgouQ5O5OxD1xNi5SOujroV2QUd3VU1hVrEz9b2xTzW85Kj2msa64O3WwoQVP4Z34Q6hvjeZbThfH_cwy0-A2Fg0zmmnpwjxPcoHOn5t_iLWmgJTESZZQGjxszgi0kRLRLfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6979e1d0.mp4?token=YayEyulpzjmSivHvQpv3myH4eJxy3QA7TtlZ9KiZMavtE3xEGBTIzUOi3as9mYMLQBHSw6DKihX_3h3hTIFaKZvYHs0cjJvqwYpIfL64jXvCPxflrWrbdjKGFDkEBUVM9EvwFsxKeKxIYkbgq2famT3SIihfTpjnw8AwSbdL5NgbmnyulPsuPxLNvNwMNpkZBgE3-hT3i_BTQpviHZNgouQ5O5OxD1xNi5SOujroV2QUd3VU1hVrEz9b2xTzW85Kj2msa64O3WwoQVP4Z34Q6hvjeZbThfH_cwy0-A2Fg0zmmnpwjxPcoHOn5t_iLWmgJTESZZQGjxszgi0kRLRLfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
پاسخ‌کوبنده مورینیو سرمربی رئال به سوال خبرنگاری که‌پرسیده‌بود درآستانه‌دیدار با اینترمیلان با کیوو سرمربی افعی‌ها تلفنی حرف زده ای یا نه؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/29247" target="_blank">📅 17:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29246">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwYr6Yc2B17hBrpzI0CyNMTmaT_7Z5xvgiMzRsVshcDQfbCdGb4Vxm2NvtglmgXyLJKEybUw18Aky-A-18e81DDcW7mkAmhTjo0gY93ps2PiCr9Y5kKBXsGk1ku5dFIfpAUS-Ad_v37C2zuX1nD7iN0cQBsLiuybEEzqoGqhZn94m-MbOhPFGShLZ04a9QZSLpVPA4lE9b2yVswgXkzqJT-6RANpnjENQ3misSI6iDG_ZWvu2nxjyWD91zpHAdyi9mkUb-7IFtHyBFxV-fjAdkx4MK78VaJgvkJMG4wfLqFC892LdW_i4o64x5Ud1B0Dhq-dusAnSGYufnQITD5k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کیکه‌سانچزفلورس سرمربی کهنه‌کار تیم آلاوز به عنوان برترین سرمربی‌ماه‌لالیگاانتخاب‌شد. سانچز در دو سال گذشته بارهابااستقلال مذاکره کرد اما بر سر مفادقراردادبه‌توافق‌نهایی نرسید حالا با درخشش در آلاوز بالاتر ازفلیک و مورینیوشدبهترین‌سرمربی ماه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29246" target="_blank">📅 16:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29245">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=Zl_N3RBKWkK4sX4_lPwf-_eOTK7c8ERPsrpAIgc6R31AHXQZckO0sy-oseBVPJo0RW5rF4wrAo_W_mjyOggExuC868wPO8567BWDXPqX6ct54x-hnSHm4M1npj3QD2AFlSdscLarpUEBgeZE8wx7DxE3ZYrjG0yOirj1xELtsdyQ8Hte9FxtD91ex_Z0a5LvqSUj8RKV-9BQMqUZfAevlVTLgnOjKvhQuGs6e3PXTAzsj9sFxqwgC8mIWOjwL0yTDCmjdgesrlR44AACi0wZCDdpPzBk7t0nfBhmS1JLEAwNEZ97jw2M0OeEQre1m6XoGVEalpUDdf-j7EYJkFxQxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08ef1daff4.mp4?token=Zl_N3RBKWkK4sX4_lPwf-_eOTK7c8ERPsrpAIgc6R31AHXQZckO0sy-oseBVPJo0RW5rF4wrAo_W_mjyOggExuC868wPO8567BWDXPqX6ct54x-hnSHm4M1npj3QD2AFlSdscLarpUEBgeZE8wx7DxE3ZYrjG0yOirj1xELtsdyQ8Hte9FxtD91ex_Z0a5LvqSUj8RKV-9BQMqUZfAevlVTLgnOjKvhQuGs6e3PXTAzsj9sFxqwgC8mIWOjwL0yTDCmjdgesrlR44AACi0wZCDdpPzBk7t0nfBhmS1JLEAwNEZ97jw2M0OeEQre1m6XoGVEalpUDdf-j7EYJkFxQxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
امباپه در پاسخ به اینکه آیا باید در کار های دفاعی و پرس بهتر عمل کنه یا نه و مقایسه اش با عملکرد عثمان دمبله و رافینیا در PSG و بارسلونا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29245" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29244">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU2hjPzvTfWpSQ1xeftQfVKiMxslYaz6EAiLJFQE-faFpnO9YzZgD4O2Vxp1k3lVJiG9kOsFT9TMr259e7ij3hANuMm246ExKE63c53xyZsX_U67dZ6uUY3icfbz8qKKn6N9fxN5k_whxccplnpXt8JKgS_p-5Iz2WZgZikKyYjLvJTG9muwkEW05FoOCTTwMp_rRvzy28ChzvuFtnTiHsGBqvku4uazYCYbDZqkgLaGXowG3vZCg8VLespyoB2nMY8DWM-Xbx3jWyj-KnNomxxisVaBfQ_iZzj9cUOWaaFnxMKaECGSMUi1eVrRTzFxaPd5n1he7HK81X5xUaEbLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد خیره کننده خط حمله بارسلونا در فصل جدید لالیگا؛ به‌ثمر رساندن 17 گل در چهار مسابقه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29244" target="_blank">📅 16:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29243">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnNoxKv4U4D1ZT38k1XT5wzu7rkvZCvGJjEnCyV_xUaXia43oG51s_fqz1X2w5Ks0DLxETdM9d0ZZN6WdBsYK8FKkP5nKF06bc6c1wMCkagzKYD8ASWNoNbNI4IVKMl6HnG8R9e1R4wysk8EpfRUtNKhFXSQ7H-YwjZN3nF6JE16jIXCfhJU3ANfqYWnA23jILiufJBZ0wJKCvPP79ebkgl9RuM9rhKanHeBaSNjYTerf7mDRQ_ZbyBEU6nb98sZcKVuWkJtiO8E3zVhYTs0h0v_4fES5soPpfWlaLM3Bp2D5vVP0Gi6WJzjfJf4GncygndLED4Yj4nqzu189kaEBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/29243" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29242">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQDffN74S2DxQ1_u4rx_mhzYmTkT3zdpqvO21SD2vxBjEEGtrl2JTOpsF2K0nbaBptRcGT1aFiV1kz26c8rBEJq5z-iMUmjWKl3w7o5HLONcOyJfTnq_5yNiWpNRGnAinLQmgF21y7CRKs9eomn1qm1lxf1UEq3Nq-TXLDjhWwSJ2K8Rw-9oti3zhe9sc4r8qw6CTV4E-s_h0mscA2sKQqfK4CRl19onrv3pEV3uLn580ZDvaKcxUynDWDa62XZyWAvDbGa3yvwtSRJyH9hmH1Fk_4h1UVeR_mV9BPjVuIB8BkvM5x0A1gpaQaDXw_6HXhjaiZAGKemc6UMZOALTFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29242" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29241">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=UuDlcq7C5JNo7MxiER5FaFXmGU-FEtb-3sXcbEQwi7gbK4erQhPy1Iw-1F45lDQWaQPTYj_pGRMNSgjTfdIUqHoAUovI364TFsJsLBRwEKIiNfzjgpkWwVPylPPIIWKuvaez192Wufm6vMKwdsG9tTwvzGqB0sP838opKrDWaWnbWY--OvxKEd9VlyDUB_ivnn3tD7xLJ1jqPTwoZQvbrEQkj7mwKxHnOKyf7-rkvYhb820-SXpvn8LzSRF5kzuamfHUsZbVY3uwBAB4ZA_pNL7qiC1GyOUY_ucjK-p5QM0Yt16DX119kGazASPo_F-CerNXLRxi9caMsDnk0j8DxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3910e6991d.mp4?token=UuDlcq7C5JNo7MxiER5FaFXmGU-FEtb-3sXcbEQwi7gbK4erQhPy1Iw-1F45lDQWaQPTYj_pGRMNSgjTfdIUqHoAUovI364TFsJsLBRwEKIiNfzjgpkWwVPylPPIIWKuvaez192Wufm6vMKwdsG9tTwvzGqB0sP838opKrDWaWnbWY--OvxKEd9VlyDUB_ivnn3tD7xLJ1jqPTwoZQvbrEQkj7mwKxHnOKyf7-rkvYhb820-SXpvn8LzSRF5kzuamfHUsZbVY3uwBAB4ZA_pNL7qiC1GyOUY_ucjK-p5QM0Yt16DX119kGazASPo_F-CerNXLRxi9caMsDnk0j8DxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29241" target="_blank">📅 15:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29239">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mz69gwcKK8uU5zU72kf_VGiszNbgMtN6SIGy03xR5cKwmay70thg5U4x8BbIw2EVRWJBJyypeEmvqvEI3BSIucavNCo8MHMRO7FCfWJyCF89MKtAJRimWY6RGmOkra0kAJFSs9Uh26wkv7D6J9BJmc17XF7QF134UTvzDGHbQN9Pos8Hd7cBK7XnaCPVpo0udPB7zthYetKmPu_Q-syj-bze7J06WZ57i496U1hnB24WOQAld8yntIqQrJ1AlzKZyqkv5DQiUPCcix9XF7WHjj2EHJJlqRgL4dSjJ6CIooLVkEauWYoQNggXh7SOaFHVrFvqS4_Cg0GjpQrdOWts6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLqE6GtYlIc6B1WaTk_9rf0MJom1k2tuDBipGxwB5nbWkl8Viw-lsJbvIQWb_LcAursqmgb2LDJV3X6-Ob2h80M8Vz-4eWKZKFRUHk7KehrsIIycnaiAWP5H_lcUx8qCwUYUkO0DXybav460hi8CColu-WpeC-KflObB0bG3mMrf-mDEBCFzZ6M15MlPjeFyrdtiKKovJUL1fHWw6RXCmCTfgCyDWQiagdpGqfuoF8OKgD5T2LdfpcbALSR3al22pjElyNPiUi_1aZVC2esZuP-_gq8oizAZBdJ9uSp30-rLSJFSkl73MgsYg9FSQHihI1vkRYUS8sbp0BDiy3IjoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
هواداران سه باشگاه اینترمیلان، آث میلان و یوونتوس که مدعیان اصلی قهرمانی اسکودتوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29239" target="_blank">📅 14:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29238">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HiZMZJ4SG-Eb-w_xI6SaOCJv8BlOMm2fZ7Qa8Xiub1g62a2npdxxcHhRfANXayua6XVBc-m-KUt6dAjRblnMiCalRKkobTjlY0HfpkNzxWpDONAmd-TaohbFCLBseOpX3cMV5jArM08LHHhQkc8pBWrD0QJg-UrJoVwPWdGYkEF7JJDqFhREaH7kkGK4B9zprusveOHVWY1CIXxoWQ42dD2k6o0jcY28m4irW1sYjNogKKmCCTYeCi9Y3EQpSDphDLcz9kgArlCKEV3Yl-KocgTPf1tvhotU4RuHs6UkxdXZfIM0GurL4ndrAUTU3BsMI8fcF2xDaIHa2v2uiHO0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریهTYC اسپورت خبرگزاری معتبر آرژانتین: لیونل مسی و رونالدو به‌مسابقه خداحافظی کارلوس توز دعوت‌شدند و ممکنه باهم‌همتیمی بشن! فکر کنم این‌آرزوی تمام هوادارای فوتبال جهانه که یک بار هم شده دوتا گوت تاریخ فوتبال رو تو یه تیم ببینیم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29238" target="_blank">📅 14:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29237">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIt__6My-X7k0EDgY263Y1yIU5ANELrvghBwTdU5PKH95y7zcWppptJb2ei3C2Ia3V0DwqqSXiOD_ZZNDmMHMqVsqFBOCFhbWBxWEsJzNYrSP5NkTPBMVZdxVK7cU6nGThkx7ayYSCoail3uZKO6qrT0xp1_KQ35M-PzIJHthTyHN-xLgRKpYJOg6YW1dlso2r54-IF6bTfmmKB0DmO3rFyH6a-uzprAyw4AXtuW60wz7juDhBg_8CnXNAn8SAXs_MyeSswwUhCe-McYQQeHv21AvSOWXlTCAt-Wwhy1YnY9MMHZYDhiGI8hvw6YidzmQb5J8WCDz9bM3I1JrnMwFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات
؛حکیم‌زیاش ستاره‌مراکشی سابق تیم‌چلسی با عقدقراردادی دو ساله به بوتافوگو برزیل پیوست. دستمزد سالانه زیاش 700 هزار دلار خواهد بود. سال‌گذشته‌ایجنت یاسرآسانی‌تلاش‌ خیلی زیادی کرد او رو به لیگ ایران بیاره ولی شرایط مهیا نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/29237" target="_blank">📅 14:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29236">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKmuepUrOzzeQNijb9d5P5kxPdKmnJNEWY38Ewg6TFBrqFApNeiXvfzNBD-jdI79uBhlgH3QiX21-pKAnwPChg8AIh6TZmNwe4CXPOL1JhGebhl2L0Ghiy32m7vGDO-0_6-jXeUAX0cp2lM2A2QZytR2jtHklK6NTaBznR55RWul5Y3SHzM_WymEWHNsMz45OeYRJtjck4aojzJLFc5wh81M262mMXDWUrcuLEBjXELS-uZDHuvecvjjXvEtXkPBSjgQC2X1DQAVj8xQJ7aoLLIFuKXbKXD7Ra9uK4NnNSepw5oevhHHK_m0cfMbUZ4GFR9LiLeBrgLatKoay30hOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
بهترین‌ترکیب‌تاریخ‌لیگ‌جزیره از نگاه نشریه سان باحضور کریستیانو رونالدو فوق ستاره پرتغالی دنیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/29236" target="_blank">📅 13:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29235">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsxjXkfvSp9S8QgYf8j2eXvV_ZaYsNml3xg6VKHxBWQrGBYu2rSQSiB9nWu7dZvdrb9H3QbNC0A8m51tO3OkEpIn6RFVwPRfrC5RUUfRGjrCJX2vfXyc1upDgdcrJVGR5MX4zzTuAt_vSQE0Gs1COZJGgFIrOJSKeY8nhY3tov3yIuLrFwlYFjxU2b9yTMGZhE-ivOa8MWPy-GuAYEmZWV7Pu9wH1mA4oo_aoUjc-6DP3j1yyhqVSuHjsGBvCsPMnwrVCXL05wwFnUO4gAERGaxi0Qe8C6NlxZMo5sHH1IXxfTpTvd8cfIgz16jexffx9Ja0F-xZd6S8IVpJbK0SJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌‌مهدوی‌مدافع‌‌راست‌20ساله‌آلومینیوم یکی‌از بازیکنانیه که قطعا در نیم فصل راهی یکی از سه تیم سپاهان، پرسپولیس، استقلال میشود. مهدوی چه در فصل گذشته چه این فصل عملکرد درخشانی داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/29235" target="_blank">📅 13:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29234">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlkXABYM8sakFfnlgwOPjdZQ_So0UPq_UIWioP4gr09ObiWP1ptPpEzNQuyfmbSggdPNv4bf6AGwRRHXeBIrbSe1DPWAALNCga-cPllTNZgMlyD3L_9jUT1UkKJ5MIkbHV6z0fn051IAJ6WGy1Ms34yN6x6mGEanx-JTt1abJZI_38jdTAYoHe6RXn8Ec34M-W3IBlxaRav90WtD2RYGCbT9AS3kya4SuhmlL9ug4ntONGGJBqsY0_EviLJKmmZUcCND73lVEggs0w9e8qhMiSczf09X0Wtyn2SPiekGXcTnlyga0C_1XVzJojd_t83N9J8qxK8pOOefj-gMlCjQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های مهدی تارتار
🆚
عبدالله ویسی به مناسبت بازی امشب‌دوتیم پرسپولیس
🆚
ذوب‌آهن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29234" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29233">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTIuUzo0eobuMbuS3E-6uziJ8NJq_yijHlSMrkjtnA9BCHEwaSCEjt1fB_GHW0P99tylQEsTpMImTb5FIIKsTqxGG6axXJXZQD1cqXqPEMo8Od9Mqv4ycT5IH39HwzYX5i05Xj2MR-aR6EulgG2OKBho-4zlqdD-qMvWNaqKGiNz9Txy0VNSwWZfVNd5kOsmgR87pffGxhB-pkuietOyHPSgL8Qe-S5Cnf7MYdUCIGawgDl2wUm14Ot_Ov-BsaRWpI9PrUgaBRDqh0ESYvn0qXGF40O8hHVpRhR32UZedVp89Uosk3BoVrDlJJoWtx_gQcHZ4GITNLfz-k61mtPjbHlk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/536549697c.mp4?token=shKyeXOB8NK3kqQ814UoJ6M8chAzp7MCr9it7nbVVP9-9-Zi5efLF2s8Z2aNVQZXWELnI1mtzfHfkc5CNS5ZqIqdrhYxNzpGI5qKxo9TEsyWmIiVQO9I7K9m2lvFqdKRG-OOS3gQC7UHcvXC446_Xt-k7hS4OawR1Q-0MwegBDYBsiGXtYjux7A1-wBfnldvinmEDsObMNqxvVxq-DSipSKhStIjSf6pILihvtZtcETOoXo95Fn3TmW88NX79kV7M_HZvkQ1CnSRrBq52UDxz8ZReXqee5SIF7SXRaAKcwvQrXYNxgWfzGQhtXWXl_uFTO3ZGnGjCv0GLc3J0kfMTIuUzo0eobuMbuS3E-6uziJ8NJq_yijHlSMrkjtnA9BCHEwaSCEjt1fB_GHW0P99tylQEsTpMImTb5FIIKsTqxGG6axXJXZQD1cqXqPEMo8Od9Mqv4ycT5IH39HwzYX5i05Xj2MR-aR6EulgG2OKBho-4zlqdD-qMvWNaqKGiNz9Txy0VNSwWZfVNd5kOsmgR87pffGxhB-pkuietOyHPSgL8Qe-S5Cnf7MYdUCIGawgDl2wUm14Ot_Ov-BsaRWpI9PrUgaBRDqh0ESYvn0qXGF40O8hHVpRhR32UZedVp89Uosk3BoVrDlJJoWtx_gQcHZ4GITNLfz-k61mtPjbHlk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
هایلایتی از عملکرد درخشان و خیره کننده لامین یامال گراقیمت‌ترین بازیکن حال‌حاضر فوتبال جهان در تیم ملی اسپانیا و باشگاه بارسلونا.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29233" target="_blank">📅 13:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29230">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nqzbGe91KnJ5EqrxxpyJEnFrAXChXXTRAiD7drca8eUmCVxy7DHsZjXrt7j6psdJYFavXf6yXi6CTfaEzmRdGWFo7LcNfC62SA8Ry5FY33JXcGxyDvIQtNiAIi78kpXAPVDSYcP8bNBsxDYtm8iKYlcm4V1gOW6rGPIx6HeEmERx9_EUG0-Hyxy48Hby_X3TnX7x2wXD4mzjl9PD4KB415ujKuJquvKFhViOQXjD0l4izPaa1gYHdJUjkQeYlxVlAbusU-wTOrncSqj8028_BZtTUoFKh_WiLUZKBACpp_1QJK1n2cW8EtEoV1VcnPy7HxwyEWfDJB6gGCmOgzAxXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFIMJxGTddriiX1IdulAAtd7VZRbo5oHg1ANhaE_75wfUMdXvFnH5Fpm8x8JTNfuU6wrgVQbXFPdZUV5WOcjuMyjGZi8WctO4uAvm-xwMWcFHkGvjMsaHrLaBhyoB_8er9Ck02ti40dIWjKom2zEiV6HmKEvtA3Cr60MhdXBE4yjeGhc12iIAQqNxtGJZhA0WzamErDT0Fr-KMBN55k2Ynv1adHIXbcji58Tjnky5uS9LYZEuuADoJc3OOgyEEkhuxlaNGWh88P16wpvm9qgRR74R9X85J-Y43A_wVl0n6VjZtwtYxw0gsByod9-PrgJLHfLUvRJv-IhGRKjh2Vj7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
هایلایتی از عملکرد درخشان رودری ستاره جدید بارسا دربازی‌روزگذشته این تیم مقابل والنسیا؛ وسط زمین با حضور رودری و پدری بسته شده برای رقبا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29230" target="_blank">📅 12:44 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
