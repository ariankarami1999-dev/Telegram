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
<img src="https://cdn4.telesco.pe/file/JMKqRfaKIVQ2fMHNKU7rXbjRySqRczST6_KjXemvx1qtqUFCF5i-VyjPVLK0pt5t_UgL8xdnDwb4juznMRn9vsi_Qs2qh3eWHbHn3pNF-sKAjXqIWM8Xt65FGLvkpSeKqj7zZhzst0b3koLW6vd0DQgEuCFB_7toCmIugp7RSo-R7l-j5B4XduiyBFsAc9gZAmvjXDjuguWL2F5IT7raYY27aLokpKAJ27rnOZQfWMT_g5em37UXmPYnGNQbsfxWegLj8PdCrT5MtmdQYrL1ByrUiCcY9S9X5I3SZi5L6JAohL0Eb901C-NJJWsA9Ux_A5B9Dm_h_AJAd8gd6krqFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.84M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-18 16:17:25</div>
<hr>

<div class="tg-post" id="msg-467488">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🎥
چه کسی پشت بازگشت گلشیفته و خواننده‌هاست
‌
🔹
در قسمت پنجم «پشت صحنه» گپ‌وگفتی داشتیم درباره خبر بازگشت گلشیفته فراهانی به ایران، کناررفتن وزیر نفت، روایت هالیوودی از تنگه هرمز، فروش ۱۰ هزار دلار به مردم، شکایت پرسپولیس از آسانی و موضع ایرانی اصغر فرهادی.
🔗
نسخۀ باکیفیت را در
سایت فارس
و
یوتیوب
ببینید
@Farsna</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/farsna/467488" target="_blank">📅 16:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467487">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نیمۀ دوم مهر آغاز</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/farsna/467487" target="_blank">📅 15:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467480">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eoXr1Y-IUMNB_A8KxUEXrrK8ZmGqz1-83p9GDHKglcAxJ8egi3fA2noVGvNGEKEOnkWc2hs1crnOH-OTHccqrAjzgyrxjUMTcVoayTMPdJhOe95c7P-hDgy_53-RmiHZg3ZiyFBTUGwrlRjW3SsrqqFYt7fzoF5MGDMZ55jFwFRfZmy3MEzVDW5rqQmRV8GLKQZkzqwRmdOQTcWrMSbcrH1S4yYoK-1Sw4hFNZBDTpUq0dSfBOdq0L4GN7v-D5miQlWlneXqVHDACNe8cTbz-dmVWSdQI3oVut-ifWPZbfj4wZF6tEtLwwlgn_mAnqsfAv59gzsSaEWzFWMAPlSVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tV846eNSt-f7NX5TBzSYTIMz6A9N6ys7FC6ABOq6WR5eL9wkDlICofkLZwfYp0KhrOF0E1Nmn84cl_A4-VRVC8Mezr5573wstsueyR7et0rnQCPRxnRE8flvhmnUIHf77_yRnwealeMYp6c9slQSl5JB36-zhG6WDeyhGC44dQABMtz2PAWnPMTT7O6Bdbj8mzSnJIxOYCOco2Un3kn-37A4WBitcoAfttUJF1yg1yy7DzCQz0t4PTQfP013Cq1hhVmT5qN-zpbJWp0Q9Au5T3-WmRPPWWBP9QDS0BuB78BvmsLiKAUp4KUrINXGrbrTDlcqqggg3JFLkVW-DBYv-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/onpB3j5XnuL5fs1HPGsDGjmSE8oT_eSWyevGHMg8bOV_izQRgVZQgIVoWmi35g4bDY4z-C1MXE28DETIjM_xgZ2PrBvcK2pFMxk-X3nrpizzUmhjT88hIAXnykSfF6PIgL1_Oz3YDcKtOfmYkE8aRIffHgFczbTJ7A7aYqVnN1BJl2okjxGatrv6l9PBMkmPRBEIwe7SqzYl6SSJrx4r7365PQAfOcRf-W6tIvgGfzC5gvBtOVdsrra2emKjstEuk2AErfQJ5PEIln2hM0KH2coPb14Jb6_P817L7KGwU5Laz1_cASn0Sx6Aym-R0ulP2YMRSGALMk4QoHLbQNt00Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TTxi6ZOvJIcA5kYaCw34bdIV2MPAoy1NwNEqUH9r8sPvNpLqoi033PlDf1c4FstsLDF3hXPME_CZVSq5hQyog1gHjlsGwBR6jUG5aHUYGJaUaJXn1i6UgeQUoYVZWhahrSsJMW0M53IT8fgtgUe9DGtij7YRm4f6ChUOOW-ZQPDiCaPZ8Iv23_OtG7wVZnhQAEm88QOZfiQOYVTOcnF_YfcvRuLyOqZC1OYfkFIOdYFuIpT-pYzmhnzs648woeSusnm-pMsaGsa-0APArRXhTT4m8x_zvBleIxBn4-2gpsoUOJ4iHWQZmOSjYleMdCzaRzeMLzRFLO4v7aYSZpNAtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FrG4PlDcWP4fvDCJAqN-GRBNtRXYuJbXFWUbHg9Gkdz76cntmaNclurkUaftfbQt9eeM434uJK7h1PjvqIk9IyhclyX6fAij7bdxthoO03oMq2FNd9HVq5oVfyVC7ctsilHeamDEWgW4JLyXycbZn8JkFiWufyAEfoGnytC9_j1yxC-69-cNIl4NKguONfWdd8nX9fLD-OHvhd8CuYRv36kEQq55WHwUgILrJM99E0_1MChiNZGUxqH9anfnQ4d8nO8ugIjcd4_orKP3fyPvQhqUTR4n0bqs_8zHzlxOsSenUoo3qCHISZaKQfX700r2LpPIsb2BfAzSkugbBeFfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qmf2lfaTVE6MqNAMeuFaI1-qbXnALUsZHlCCKPOiTnO0YDboJxE2N4F_R1Ti62HEAzkQ2Kn4sjIcI7koj9vAqVDTpI4fIIRbd1xgJbYsNDA8WxRG89Fsf1QNlU_2Da89eTKgRflx6gwX3BiTwKuuq2RhryOYOsoYcmTW2xmcQXofrzy72JsLmeanhpob17KKes6jS5gBDg3tcUoc5phak5-KgnMNJ8VHenRagm1lfJKr9baA6q0PrWrFZJnFSwdiU8alWbuRbuRjtiGWsVM76lM_4xQlesEGamRGASXiRhJSAkkyj8so8JWrOdPFzxoYPnw66ZTpJP72JUzTzmjhvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hmv_HfSDSGcrzqeXtgJW9fj7X2tNvB3UXmVvQb9vkJZZvo7z5dVWW9YyiuJ9S8Vm0FEMdhBWDaJmpVM6doIgch4dbgZnma_HWr4u7APtTeTi8rX2HgWgUX9Lzyb5wFJ0t-xTCAY4ltuHd-ZOFwO1xpJRoP7LUTnUDkegv8MtHzW8BB5VYaqB0tg4kTwcxL6IGHw37csongK4sxPL1IEiBWHdsaB_i9yGJIQk9y9LyqLoUqsxUhbh600Jmq840WGZSdGNlbKVWIucjgIQyQoiLWhQb_-ALoy4OUh8ol8PT3OL_k4xTgQuq15IB9NDxqpkDrDCezmy6QfMjZUy1b4OMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
حضور رئیس امداد و نجات هلال احمر در خبرگزاری فارس
عکس:
زینب حمزه‌لویی
@Farsna</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/farsna/467480" target="_blank">📅 15:54 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467479">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PySuQ7M8XJEFUIvN5aF5HieEWK5w98lwAi1Y7-WfYlFrfEsMSsRNiMRQsozORuWhggiZVC8OYD6JSrFA8JFVZBusG54hrbWSS12gHxNsbE0Ognru2eA2kaip8A7Epco8etEqqHs4rtgBIVyLNqruUYzME7AJcdJe5KrDqf06aj6XVgiyror-pWlZ-sXsfp5OGR5fU-P8InzL9K926eYNfjsjoqy56cC_tZUBQrwg88NeA-FwFF1rkamp20eLZBqcPsz6EeYX1YGRXOFN0LZGY1kWL_hFQabq2UA6p_ARvcxqCokA3TsM_GPmESe6C_98XltYFj-Mzlnl7VgAhE-egg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکش دعوای بیرو و تراکتور به یک نفر دیگر خورد
🔹
ماجرای اختلافات بیرانوند و مسئولان تراکتور ظاهراً به مسائل داخل باشگاه محدود نمانده است.
🔹
شنیده‌های خبرنگار فارس حاکی از آن است که فردی که با معرفی بیرانوند در یکی از شرکت‌های تحت مالکیت محمدرضا زنوزی مشغول…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/farsna/467479" target="_blank">📅 15:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467478">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3a66UUTswg73qyFCmOf7kzOi1WHm02LTskgiaVwfZPX6CgAyVBeRG5tzI_r9g0Eh5u7eVBndQgZaGtfqEPJl8hXvrxcriHILQ7ADzdFyxys9c-JuzSYm2NNq6wXh9W6AeBG906RG5VWF1xRgWXa23CuSM_Ri5H3iiWUQgymgonBvYsufTjk586Aqd9J351wkBidSjM3PZtTYrBqQ544LbUNkmSwAWSZCV-cThkylOJHO701UPfoD9V6G5vxiNRIjFPkxn1a90KGC5Fm--wFBY4CmwVqytFVQ1gKqHzvUkkCTL3pzHNoNfLyQxnhWWLejiTgx6porSpXE9KqH8UH5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ قالیباف: شهیده نصرت افتخاری در دورافتاده‌ترین نقاط سیستان‌وبلوچستان، پیگیر مشکلات و گره‌گشایی از زندگی مردم بود
🔹
شهادت مظلومانه و ناجوانمردانۀ معاون فرهنگی و اجتماعی فرماندهی انتظامی سیستان‌وبلوچستان، در مسیر خدمت به مردم، ضایعه‌ای تلخ و تأثرانگیز است.…</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/farsna/467478" target="_blank">📅 15:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467477">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812e55ee69.mp4?token=Zo1Rk1_08S8bwxKd9M35B5bgaCBRHoH_33c09YUJx-dMjLd02k1ngARrBnvBwHY3rhHnPIXtXbyp4QQqcYwVbg2NgvCzUY1Emnu8p09zglTsdHMN_mgj4EXpYgyOtPAHbPawx5Al4bag7mMypu6W1FIbq7lxmVUv6xnpiiQylT3fCR2z2buG_tPCYHVeZQjGUjXnhHhu4EFqsDOosc1jjgWrPSHac97QsoMQ5R-l-lonqjLYIOadzUuWOn_mOiUHpUl4cy5WjOniVvoZ2DufGjoT5dTL0FCwz0N9Vhjk46UL48-AeibH_xK5mkdcmCCvvwE9yayqRVHLl8t73y2m_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812e55ee69.mp4?token=Zo1Rk1_08S8bwxKd9M35B5bgaCBRHoH_33c09YUJx-dMjLd02k1ngARrBnvBwHY3rhHnPIXtXbyp4QQqcYwVbg2NgvCzUY1Emnu8p09zglTsdHMN_mgj4EXpYgyOtPAHbPawx5Al4bag7mMypu6W1FIbq7lxmVUv6xnpiiQylT3fCR2z2buG_tPCYHVeZQjGUjXnhHhu4EFqsDOosc1jjgWrPSHac97QsoMQ5R-l-lonqjLYIOadzUuWOn_mOiUHpUl4cy5WjOniVvoZ2DufGjoT5dTL0FCwz0N9Vhjk46UL48-AeibH_xK5mkdcmCCvvwE9yayqRVHLl8t73y2m_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خیابان ستارخان تهران به بزرگراه شهید چمران متصل شد
🔹
پل دسترسی خیابان ستارخان به بزرگراه شهید چمران با حضور شهردار تهران و رئیس شورای شهر افتتاح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/467477" target="_blank">📅 15:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467476">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORqkvGdtSp55qOV_QCjAYPYk6vx7lVo-quesY8RbbmW744t60jNvtOYa0hdjeXA8_vYRNq4HD5WEuvxuHOir18qzP4x0R7Zgydc5HSmwftxw-a0GgkcNvjk8EfQlPh2SUzTzhpalS289xRRotFwXcP4_xronvOzkY718LZqsaCMl7dGjxVRrsQCX71rYRTa2gFQ9P0OIVELmbGcLhStAYWudM3Ljj3FrjpCPCc0-ITmdKOhnJD1gtrLyAC8ESr4cA9ueyLAQXw8Pwgnx2MRVOFhKTDiV4n9LAHDcIadbikucU-UlNSMAaT8c7LJTvVEFGXaiPF_yx7HHt7PIM3FRfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ واردات ۳۰۰ هزار تن گازوئیل از روسیه، مصرف نیم‌روز آمریکا را کفاف می‌دهد
🔹
برآوردها نشان می‌دهد ۳۰۰ هزار تن گازوئیل معادل حدود ۲.۱۷ میلیون بشکه است.
🔹
با در نظر گرفتن مصرف روزانه حدود ۳.۹ میلیون بشکه فرآورده‌های میان‌تقطیر در آمریکا، این حجم معادل تقریباً…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/farsna/467476" target="_blank">📅 15:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467475">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT4IrNErztWn9DTbiDmz0ZxC3qLcGUKdJ1LhcG3oA-KUcttPLZdkR7Q3MKmNSQ_oxTfpoLcpXL7fE2N4hcyTRqd4rmcJiBjOt-mMLUfeJ88wj5XvpiUfHUJLRFWMVrmhwnur4QP-GvRIKH9D14LUDYkEBkfpVNOgHYdKuxAu-raEd68Cs4gpUdWxlroGbEPVhmPODUhx55OZ_wNYqeS5hgioxpRco1XX24yF8m1EM4x46xrc5l5rp99oOm2xj2J3vGNSvHOraw9o89u8-Y2OOdhRM16tqA-M9WgUw5o_pQ61QQ0JiOUYXujeVwRIGtIa_5byY_pz1S2_e7PcOlZmHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاهان خطیبی را به خط پایان رساند
⚽️
با اعلام باشگاه فجرسپاسی، در پی کسب نتایج ضعیف و شکست ۶ بر ۱ برابر سپاهان، رسول خطیبی از هدایت این تیم کنار گذاشته شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/farsna/467475" target="_blank">📅 15:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467474">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLl4HvOFlOxzXGmdFhdik9jP-w3bpD1trLEmXWG5jxYJ22BFB88RClIN8K5o1Yy1nf0Khwq0k5G4VDQgA6dx9hymMD_Ud6172TUAu3DXvGfbMR6Ut6AUmhhSAe7HxncjcmI29knARt1fFORPkawS85P6LCQDEpVZhie-elkfIwk7G3s_EI8SNyUmiVBAuMxRWXbiDs1-0jO2LfeHhKWFl_IcK6rej3SSkrf8pPSqKW7u0TVqkQ2rIttf4HbhPlc2XdNFHwJQ_28n3F6JBisFncgQcNNiCIHwMBRlOSS_mST64gq8PUCzjPkmg133sKNHDfyEc-oXLJO-OVMLSh9aeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رویای نفت ۵۰ دلاری بر باد رفت
🔹
رئیس اتاق مشترک ایران و چین: سال گذشته، کارشناسان قیمت نفت در سال ۲۰۲۶ را کمتر از ۵۰ دلار پیش‌بینی می‌کردند؛ اما حالا هزینۀ حمل هر بشکه نفت از خلیج فارس به ۴۱ دلار رسیده است.
🔹
گلدمن ساکس، سومین بانک بزرگ آمریکا، نیز پیش‌بینی کرده بود در صورت نبود اختلال جدی در عرضه، قیمت نفت برنت در سال ۲۰۲۶ به محدودۀ ۵۰ دلار کاهش یابد.
🔹
با این حال قیمت نفت برنت در پایان معاملات جمعه به ۱۰۴ دلار رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/farsna/467474" target="_blank">📅 15:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKf9NM99PkVk-1PGo9NYjFhFwtnGDKVHqSLdsJP0aeBZfQglcSXWmQwBRphzK-zclQI0q5689azANYCVl0nrToR8ZNxBrWLcNoOLIEMid2-EqFEqKE9tnDAnxuWZVkEslUA0UGeS0F6KnRXtt5uD80fHhcCE3P47MCTF-KcE8alAQzE81wbVtd5d-39isF0Xb6EHsyH4hQ9KAP3cxhnmPBfsQM6KvcD3OLv4HXot0L-gcwcPOvqV_QNYEWi4buOy_K7mBV3MI00KGvfwQQlaajL8oPDaeO8ImkLwuMho_4A4vMTy_zvfZ8netf81GxAyaqVNO1-aQKSmGClr9QIwwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روایتی از «آن روزها» که سفیران دولت‌های مستکبر برای ایران نسخه می‌نوشتند
🔹
مقایسه امروز و پیش از انقلاب در پیام رهبر انقلاب در حالی است که اسناد آمریکایی از کودتای ۲۸ مرداد تا روزهای پایانی حکومت پهلوی، از نفوذ آمریکا در تحولات سیاسی، نظامی و امنیتی ایران حکایت دارد.
🔹
این روایت فقط در اسناد خارجی نیست. حسین فردوست، از نزدیک‌ترین چهره‌ها به شاه، در خاطراتش از نفوذ آمریکایی‌ها در ارتش و همکاری برخی افسران با مستشاران نظامی آمریکا گفته است.
🔹
اسدالله علم نیز در خاطرات خود از گفت‌وگوهای مستقیم با سفیر انگلیس درباره واگذاری بحرین می‌گوید؛ روایتی که نشانگر نقش لندن در مسائل مهم منطقه‌ای ایران است.
🔹
خسرو معتضد هم درباره کاپیتولاسیون، دخالت آمریکا و ضرورت بررسی اسناد انگلیس درباره ۲۸ مرداد می‌گوید.
🔗
متن این گزارش را
اینجا
بخوانید
@Farspolitics</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/467472" target="_blank">📅 14:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6642900d47.mp4?token=ozbtmHQ0dWiZloKcTg6p03aDNLHrJV-vKVH8Pu7-aKTx5T3PAwUG-tggU9XFotBx0jFNpnO6-pjKb-mkdFevU4QkF49JaHXSnEZRqSx_miY51dYNIYVzRW-1XMniQcrGoyQVUfvbUSknsv-QrsfvQjqyGTO9UpT1AGWVYtQP2z8R1F6_Wg6dkmyGMnk4YOvo_cO_mjmKdhiOZ0Yda263LD1flOefy0trv7BhcIS8J77pznUpEoHdN-nbzP5jWR6BUttcri32z9ZQmYoGzLQx2mBtycsZIdLWgQsI4OJgXnshmbcCHj48hPj-e7AWXFex4O767q5Sgjnx-L6dsZrFbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6642900d47.mp4?token=ozbtmHQ0dWiZloKcTg6p03aDNLHrJV-vKVH8Pu7-aKTx5T3PAwUG-tggU9XFotBx0jFNpnO6-pjKb-mkdFevU4QkF49JaHXSnEZRqSx_miY51dYNIYVzRW-1XMniQcrGoyQVUfvbUSknsv-QrsfvQjqyGTO9UpT1AGWVYtQP2z8R1F6_Wg6dkmyGMnk4YOvo_cO_mjmKdhiOZ0Yda263LD1flOefy0trv7BhcIS8J77pznUpEoHdN-nbzP5jWR6BUttcri32z9ZQmYoGzLQx2mBtycsZIdLWgQsI4OJgXnshmbcCHj48hPj-e7AWXFex4O767q5Sgjnx-L6dsZrFbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۲ هزار عنوان کتاب برای فهم رسانه و جهان پیچیده امروز
🔹
مرکز جامع کتب رسانه انتشارات فارس با گردآوری نزدیک به ۲ هزار عنوان کتاب از حدود ۷۰ ناشر، مجموعه‌ای تخصصی برای علاقه‌مندان به رسانه و تحولات فکری و فناوری فراهم کرده است.
موضوعات این مجموعه:
🔹
آموزش رسانه و جریان‌شناسی
🔹
علوم شناختی و هوش مصنوعی
🔹
حکمرانی نوین و آینده‌پژوهی
🔹
علاقه‌مندان می‌توانند برای بازدید و خرید کتاب به فروشگاه این مرکز در خیابان انقلاب مراجعه کنند.
🖼
برای آشنایی با تازه‌های نشر و معرفی کتاب‌ها، ما را دنبال کنید:
بله
|
ایتا
|
تلگرام
|
اینستاگرام
سفارش کتاب:
عنوان کتاب موردنظر را به شماره ۵۰۰۰۱۶۷۶ پیامک کنید یا با شماره‌های زیر تماس بگیرید:
۰۲۱۶۶۹۷۳۹۹۶
۰۲۱۶۶۹۷۳۹۷۴
🔗
مشاهده کتاب‌ها در مرکز جامع کتب رسانه
@Farsna</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/farsna/467471" target="_blank">📅 14:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k1TrhWSelsf1PSp3l1zxrl5QnGzIzixgtrjsWqOVjnllw6QNTrGOJZRFKH47JBNSGN2jayPl-jmcB3hDevnRhmHIgV6cAp25ybpHqSpcUTJWBLXI9h5aVjV16SjP0Y1X6cCiLAqg0k2FhnP94wn_J6o7sxEQUAdPRs-WEOxxrC4AmTeg2RblwxrmVxBm_sxgr6TS9MGGssVG8lMW5hR8eJASlX-Gy-CXh3WIz36O9LJUrRs5LJ-NBOca3UFdpPalv9nfD2bHuRYpZJxP0hqK-7LCGJ9Yag2CCaoSK0bvuhDJ0CD0LslBvACiHfK-uPSH9TdNNDgmcTgijpB1I1FuSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تنهایی نتانیاهو در سازمان ملل برروی دیوارنگاره میدان انقلاب تهران
🔹
جدیدترین طرح دیوارنگاره میدان انقلاب تهران به مناسبت سالگرد عملیات طوفان‌الاقصی  با شعار " روز به روز منزوی‌تر" با موضوع پیامدهای جهانی و انزوای رژیم صهیونیستی اکران شد.
@Farsna</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/farsna/467470" target="_blank">📅 14:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XwFc6860P9IOSsM1jlBrLfwmwf2S4aZ_9ryMq6EJAO8dgbBWUrtYzCPt7ZklUJNi81G7EHU4LbMzMJzn0cFgSGxoE2GSWgDN97ilezcrgZIIiErKNweOCMvlizp3oPBAIi9-23tlaJbYaMiBDxUjm-h6I-ZTq_VKC4rseSol8l9-FfR-VCSSBxl4CzlMhsOiOjkTMqqhI3Sx4dGOyAN3_NOSFwhMJac817FC963bEovPhOF6G1cun-esghxIdykioVurpiafgAw5Ej5TALp6u8H1mH8BliRyT3rfoqBT6wLCMjpfYsH0Op3FeglTULH6Mjl0YHM1AcjuWY-m26HfIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یار دبستانی اُپارک شروع شد!
🎒
💦
شروع مدرسه رو با یه خاطره هیجان‌انگیز برای کوچولوها همراه کنید!
🥳
اُپارک به نوآموزان متولد سال‌های ۱۳۹۸، ۱۳۹۹ و ۱۴۰۰ یک بلیت هدیه می‌ده.
🎁
📅
۴ تا ۳۰ مهر
🎟️
کافیه هنگام مراجعه، کارت شناسایی معتبر کودک رو همراه داشته باشید تا بلیت هدیه‌تون رو دریافت کنید.
👇
برای مشاهده شرایط کامل و اطلاعات بیشتر، همین حالا وارد لینک زیر شوید:
🔗
لینک</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/farsna/467469" target="_blank">📅 14:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/farsna/467468" target="_blank">📅 14:48 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaBHBD95ktGk1b1l4bCcPiAGqBXs5x3zLExM7AuJrkvwTaC6O8gIeukN9FQW5gqLb9PnkRb_19HPHbx98aQvWXAo3mMtOZD2qUEHJYWY1WP_ZHJ1Ka7mQFhe95ZbnFBzjZvYKbKo9ljqdVOLg3RIouNNdFiDjYpYFThR-ymEvw_XxjOm89rv7JPv-yiEn2vP94wHg7I7hymhdvIQsLUsVFYipcioOlCvQFYs8Vx_7y7cRa52hgDXqFjLdP1hhoZbkjSrX8ZCt6Bi8_s9xgqCmoerHDLrYq7bwATONmtIov0S1mGcU68AG6BbiW5J-8w66NN5aQGgpOzxb-gtgNLxHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین همچنان از دلار فاصله می‌گیرد
🔹
بانک مرکزی چین در سپتامبر حدود ۲۳ تن طلا خرید و ذخایر طلای خود را برای بیست‌وسومین ماه پیاپی افزایش داد. ارزش این ذخایر به حدود ۳۲۳.۵ میلیارد دلار رسید.
🔹
در مقابل، دارایی‌های ثبت‌شده چین از اوراق خزانه آمریکا در ژوئیه به حدود ۶۱۸ میلیارد دلار رسید؛ کمترین میزان از اوت ۲۰۰۸ و کمتر از نصف اوج این دارایی‌ها در سال ۲۰۱۳.
اما دلیل این اقدام چیست؟
🔸
پس از مسدودشدن حدود ۳۰۰ میلیارد دلار از ذخایر بانک مرکزی روسیه در سال ۲۰۲۲، توجه بانک‌های مرکزی جهان به طلا به‌عنوان دارایی‌ای که می‌توان آن را در داخل کشور نگهداری کرد، افزایش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/farsna/467467" target="_blank">📅 14:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a85b0adca3.mp4?token=vwSUYmRq0heqqHF1hhpU6zK6AV49OT5aveq8UO9l-fEtxyU1mJbKg6OpnURfUS7LCX97meEfEAwm3_7n8hMPWmI2iMafC5yVWVXkAeKNL1YymM_qt7mz4Z2hwwiwt_vAKHyr-8DkvqKDLBlf4GiWx1tpMatCy0Mi9daU7G5aw-2Ip4J6ROO85lkmLMG_snBHQEEnaUFPC2gGbTV-rx5IQLQRxnBd7g_47F9aAx7NkUZNdmQx6sGWPSAMsWpriJMxT-lG9UAzKm9IN8R4Jce7JllWapfstGPs83Kwrh3SVzTWiomkoZ3a4kH02xW4eZOmoL0jh-Z0061EEBG9-Firew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a85b0adca3.mp4?token=vwSUYmRq0heqqHF1hhpU6zK6AV49OT5aveq8UO9l-fEtxyU1mJbKg6OpnURfUS7LCX97meEfEAwm3_7n8hMPWmI2iMafC5yVWVXkAeKNL1YymM_qt7mz4Z2hwwiwt_vAKHyr-8DkvqKDLBlf4GiWx1tpMatCy0Mi9daU7G5aw-2Ip4J6ROO85lkmLMG_snBHQEEnaUFPC2gGbTV-rx5IQLQRxnBd7g_47F9aAx7NkUZNdmQx6sGWPSAMsWpriJMxT-lG9UAzKm9IN8R4Jce7JllWapfstGPs83Kwrh3SVzTWiomkoZ3a4kH02xW4eZOmoL0jh-Z0061EEBG9-Firew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس ستادکل نیروهای مسلح: در جنگ تحمیلی دوم و سوم فراجا محکم ایستاد
🔹
فراجا باوجود آسیب‌های وارده به مراکز و تجهیزات خود، با ارادۀ الهی محکم و استوار ایستاد و خدمت‌رسانی به مردم و تامین امنیت کشور حتی برای لحظه‌ای متوقف نشد.</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/467466" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651a7ff2a6.mp4?token=fDBRn2C3qn2chi8g9OHFbCeHjKB9WpMq24dImGhZdeB-TveC4tG5EjBWRKHo2YXv2icK_boVu8-FiAYPoafGTnlpH3iQ-28YxXbJj_bZYHMB88Kojlph70MFOc2uBR2SFIISG86eqrXFAysNghyabTwFThXPZMooZhqF3NsvzM8kqKJuy0YOhZoQUzOlB5cd265JlLVVQUP0VcM9xWPaugGziRiZbLuIqSM8eW8pH8nmSTFJ13fl9_Emje2gf3GU1St85PqvXGwGekWT7W6IoxUs8hEwsyKPWD_HWNDYHEtNQu2IPqbaq-0RULgJI4PF78tv5W77PoWGvZENaEF7Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651a7ff2a6.mp4?token=fDBRn2C3qn2chi8g9OHFbCeHjKB9WpMq24dImGhZdeB-TveC4tG5EjBWRKHo2YXv2icK_boVu8-FiAYPoafGTnlpH3iQ-28YxXbJj_bZYHMB88Kojlph70MFOc2uBR2SFIISG86eqrXFAysNghyabTwFThXPZMooZhqF3NsvzM8kqKJuy0YOhZoQUzOlB5cd265JlLVVQUP0VcM9xWPaugGziRiZbLuIqSM8eW8pH8nmSTFJ13fl9_Emje2gf3GU1St85PqvXGwGekWT7W6IoxUs8hEwsyKPWD_HWNDYHEtNQu2IPqbaq-0RULgJI4PF78tv5W77PoWGvZENaEF7Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: قابل‌قبول نیست از دیگران عقب بمانیم
🔹
قابل‌قبول نیست که ما به‌عنوان انسان، ایرانی و مسلمان از دیگران عقب‌تر و ناکارآمدتر باشیم؛ باید ببینیم دیگران چه کرده‌اند که در برخی حوزه‌ها از ما جلوتر هستند و ما برای جبران این فاصله چه اقدامی باید انجام دهیم.…</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/467465" target="_blank">📅 14:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467464">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRXiRdWUqwyBkfOnEteVRo_sIr9wViZDvtI9RSaadKM8Y0W-W2v-mBE1Qf6_O_1ldhrA4zL0DuwwqZ7Tf8Wsv0_bS7SJGXposvARrqSUb-Eg2wOcVTsDnRRgv6qwwYKmQatWA8IOKdXKzzsRVZjSmLMWi4TYvsEylybUM2WkqV_oy3yHbvF2z1e1ifhJP_Ex1SXcWnX5EiRfUSMVMe4nEPMg1VNbTbC7qXE-k9WNKXeVNUTaOFejqOpPdiT7xI5nRcBMJsW0FQMqT9Y_oFORWKG8al3WUdh2WV-_FWskCm9NwwI862PlImv1ZT1DRxtx9DE-kyah1xLXWznlaBKPgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلال محاصرۀ هوایی آمریکا را دور زد
⚽️
تلاش باشگاه استقلال برای گرفتن مجوز مجوز پرواز مستقیم به قطر در لحظۀ آخر به نتیجه رسید.
⚽️
با وجود محدودیت‌های پروازی اعلام شده، کاروان استقلال با یک پرواز مستقیم به مقصد دوحه ترک می‌کند تا برای دیدار دوشنبه‌شب مقابل الغرافه آماده شود.
⚽️
استقلالی‌ها بعداز به بن‌بست خوردن مکاتبات با قطری‌ها این موضوع را از طریق وزارت خارجه پیگیری کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/farsna/467464" target="_blank">📅 14:08 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467463">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVWy-BcXYz2MlMgvW51rYdehwQasLZt7D-n8jcu9qITXK6U7oz7_NgoMl_vDyip3SkC30UEOGqMHzMVmiCNA8z_VY5S-hlZlyNyGG-9wyOO_64m8ic1Yn0eACEdJfdyvfrD5xsqOc_C1BQM6W_ibc1AJLBPMLqlT3zLnI6HG-LpW2j98kQTe2N4ChrbeH6mNL__JrXO-TEzQSA4hbSJfqPmiyosvHt_TpYkH_tWkFT1Ps9zpKmLaF_Wi57hiuw66E4Rekfm76pnzSHtAytr92CBHUaPzMg4HkzQy5hRrrDg8wSC3aQDsTXu9cG4YGTKjlBHnMSAYD9Jk5aJ6H7CMwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجهیز نیروی زمینی ارتش به سلاح‌هایی با ۳ ویژگی راهبردی
🔹
فرمانده نیروی زمینی ارتش: پس‌از جنگ تحمیلی ۱۲ روزه، طرح‌های عملیاتی را بازنگری کردیم، در ساختار و سازمان رزم تغییراتی ایجاد کردیم و تجهیز یگان‌ها به سلاح‌های جدید با ویژگی‌های دقیق‌زن، هوشمند و شبکه‌پذیر…</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/467463" target="_blank">📅 13:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467462">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKHFhg0F6Kmio0VV6x7uUimQO1ErT3-d-zx78-VINYje65aGmtPQgNXEGjvPeDm_Jg9QhGfTT3n03QLAQ27vnes3vDH-fXuP6ZZAPlYSpbixfPyq_pD0jW8Av5g9ql1-idR6VUcfrZraHx7-Re0yBKqbUWnRXRnuLdBt66aGezbRT_LAJEzj0Lih7LHk-A0GRH0_vrqkngNbTccLwvwxXppq0KKuTS5YbwIYi-_Wo_maUNNKvvWHdrjdHIAG5SAWGZ_lQGxH4ygfB_0u1U61hk1kzk2jSO2v1vEbVqUENbHdu1HZdX48mgkV3mVUYMUCbMaomUHRHwopPjuUO7Uw6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجهیز نیروی زمینی ارتش به سلاح‌هایی با ۳ ویژگی راهبردی
🔹
فرمانده نیروی زمینی ارتش: پس‌از جنگ تحمیلی ۱۲ روزه، طرح‌های عملیاتی را بازنگری کردیم، در ساختار و سازمان رزم تغییراتی ایجاد کردیم و تجهیز یگان‌ها به سلاح‌های جدید با ویژگی‌های دقیق‌زن، هوشمند و شبکه‌پذیر را در دستور کار قرار دادیم. همچنین سطح مهارت و آموزش کارکنان را ارتقا دادیم.
🔹
یکی از تأکیدات فرمانده کل ارتش، کاهش تلفات نیروی انسانی، جلوگیری از آسیب‌پذیری تجهیزات و آماده نگه‌داشتن یگان‌ها برای اجرای مأموریت بود. در سطح پادگان‌ها اقدامات گسترده‌ای انجام شد، کانال‌ها و تونل‌های متعدد با طول زیاد، مواضع آتش و سنگرهای پدافندی ایجاد کردیم.
🔹
این اقدامات موجب شد پیش‌از آغاز جنگ رمضان، یگان‌های نیروی زمینی هم از نظر روحیه و هم از نظر عملیاتی آماده باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/467462" target="_blank">📅 13:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467461">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlE5OJ_lc4Et9Wd2b90hA3l8ucLyYSgoBFip2O6I_YHrwFnPdLTiogRClnsfYn5z-tuJwuBBiHouT7nF9jcyF-T7mcwiMBTFQBR62cWY0HdR39vfusXE5GNhNfIZam212RIauES7FJgNieFPYeyl4eptiTWjrtpZ-n9z_GLS9w5Cl6iaLxqpcyD5jLK25bZKtXtOzt5H8d0hk0OWmy2TyC2IBkbKBbI58UQXRmzwcvjOaSZ312yfCON3-yLf3lJJOqWFgOmSjrVyF6jKek9GQegsiA0a61CdsO0_GQpG3-gYvMBVPSmt8U-zm4c0ccBw4Re0KPDAIcnmPTy_DnOZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ تراکتور به بیرانوند اجازهٔ اقامت در هتل را نداد
🔹
در ادامهٔ درگیری‌های مدیران باشگاه تراکتور با علیرضا بیرانوند پس از پایان دیدار این تیم مقابل استقلال، روز گذشته اتفاق عجیب دیگری در تبریز رخ داد.
🔹
گفته می‌شود مدیران تراکتور به‌دلیل اختلاف پیش آمده، مانع…</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/467461" target="_blank">📅 13:22 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467460">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd5b650df.mp4?token=Lr1MgmF-cyMEJCzEIB39-nsqoUoqHQJ5G4Deo1tiBFbYdtnndyrVDRfCqnY_8z2_-h6MCt3gmf0ok_gQMGeoM7C6ifDumVMEgaVTmmuUpuNaZNPkNMX9oWqm-3IfmrKAOqEc52xEzk51_BNy1jq_Lh7YFFyu6jMqj3MDYIsG7wQ1QxoPV2PB50KsHhbmRGJKvtcpZGqg2OKlGCPbBM6keupCUASnUcglE4U3oIinvrNWyo7IQjYS5geHcGyYlG71uNDnQIfUI9xi_L9DN1J_7i7DoFFhQIjqGl8Rt7zxK89CxpcKVWCo7WcJc3M9LZNIw6afh3-6eqM4_fnw2Gsx_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd5b650df.mp4?token=Lr1MgmF-cyMEJCzEIB39-nsqoUoqHQJ5G4Deo1tiBFbYdtnndyrVDRfCqnY_8z2_-h6MCt3gmf0ok_gQMGeoM7C6ifDumVMEgaVTmmuUpuNaZNPkNMX9oWqm-3IfmrKAOqEc52xEzk51_BNy1jq_Lh7YFFyu6jMqj3MDYIsG7wQ1QxoPV2PB50KsHhbmRGJKvtcpZGqg2OKlGCPbBM6keupCUASnUcglE4U3oIinvrNWyo7IQjYS5geHcGyYlG71uNDnQIfUI9xi_L9DN1J_7i7DoFFhQIjqGl8Rt7zxK89CxpcKVWCo7WcJc3M9LZNIw6afh3-6eqM4_fnw2Gsx_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون‌اول رئیس‌جمهور: در مرحلهٔ نهایی‌کردن تامین منابع برای افزایش رقم کالابرگ قرار داریم.  @Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/467460" target="_blank">📅 13:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467459">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmGk-cTxbgKldwovcOilEblnbjCSPYkeXcbFTObpG00jpqzt3TypW9Fl0iKbV8zN4e2m6qjCiU38x-UkoGEgW4LC4d-N6OUqXP3vBbHsQ4Kz9qNd6wtLd1PdQmwn_wkxEhpRjCzb4VpXVMtouCkNOmjoa96S79DbJA6wU0hrjP8RNvCWHJ4mnEppYYuWEXmaulYfHD9tlZHfFAFjMUZXuBMsjtXqRZ81LMQ7sEo6pF2h4_medgYP6h4y58-JwHNQiMPhK1-7ZEEz7qFX6fwSF3w1-ogcK4PvHP1w5dH_hW2byoWGCaUBEN_wBEeNW_L5MbNgq7Q2QzUAXpEhIVhqXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
بازدید پزشکیان از نمایشگاه توانمندی‌های روستایی و عشایری
🔹
رئیس‌جمهور صبح امروز از غرفه‌های مختلف تولیدات و توانمندی‌های استان‌های کشور بازدید کرد و از نزدیک در جریان ظرفیت‌ها، محصولات و توانمندی‌های ارائه‌شده از سوی روستاییان و عشایر کشور قرار گرفت.
🔹
پزشکیان:…</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/467459" target="_blank">📅 13:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467456">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mA1gAE8kloLKOf_83xBKVIH8clnNzJkYjcWn69OWuASSSfxyOczvxnJ00Uww6gQarFWhKT8EXwwE3HsqDk0MkN-EQjtBxi8bJfTLVl2oiAmNqLT3SilcqEeX77me3qSrRneNtz_FGutS080pu4D4-h0aP95dVvhbvTBkpNjCyh2AK52fecjtwOx_YKLZ7cvbF_WeM0NYJlUnRM4TKecH4yBX1zeGQLiz-n5Uam3U_g-xZI_c9nZBy20ZAXsLokmRSaXowMBYHeMkWPQwJ13YEfcOFs6xcepqEapujRfRoFGB_qq5LqsKZYrB37Fud9GrvIQV_U8TuZ4WbXJExUIDbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZ85jYRyYKiWXBLBZmf9-ZuF-SHNIqTStksg0cbWqqWuZF23jkH9xe2k5XQlkt-YgHYt8mf1-irrPbSruLgLvybdk-b32mdUMwpTlSaBUJ6eo2My7BReKUA6h6nxnaKdQD4lS4F7g92_9wXosBERZQseV5ygCet_C-_pUDg7ewHu6Ye_B6jKbxgEZ8AgOz8VaJFd1ZGdh3zYiD4gWw3sm9IXOJ0YqwUnn7-iIaGgTnm9fN30D_aYPCA3gJN0mzgZTN32EsA-79ST8FlZn5aHROA8x5YhAZ9SDYMtVFg1HMdzwXFcdZU7smCGoqcd9TwlS-cYy9w8AO5DIYP1NmJ5-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3Cpwdl-n9knqBvcZO3dE_Phl8h_zRKPvBqrngxiu4gIPlnwUSwn2KKzdo_A-XhgAflXZsSt18JnbKD7fxNaf_thuG3jjIVpgwebHuTjZb0FOOoBRCDNTrc-i10wOclGXMpcC84yAOu5d1g9M3TW-PtWDVVhHbFT9thufYuaHrGWVrlEnq6A4FsKJYWo7_5boXL1r6UBP0UtHUBv1ys1DuBgRBWMJhi6Zj7_Zp3tcX3NfWhKdGDS0bocdyhBapyaoQv3cNyvmBcDQcZHkRvTxKYRtGzbujiiDhWpxiz0hg9VYmq_g38K_tfi5TPPRx4-PtPDxMqdfSdQ39G8ve3eXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان برای حضور در گردهمایی آیین سال زراعی ۱۴۰۶ به کرج رفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/467456" target="_blank">📅 13:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467455">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7b55UAAJTpbE3zugusU9NhklswRVZ6qK-NmY_QWTefiZuSJBU9SNiUyrvKDwSbaAb4Qxf_spgUVD-jANGhZhlVcOY1PRiuPH1Sz33KVaduIciH-AVooNZWN7oFRuMuCZL6PHNEqR7HY3R20ttmDCMWeEecMId2iOD5GVenObk9kJx71k015dhyz7SA-cd1A1rsG4NndHu_3c5WQvw5R_l1mjF0NJptffSTU6CzgfUi1UWrFb5LuhkzXqpkXZd243DHa-zmH8PjrtdMubezdCEEljfhcUjW0TOZTrz8AA34wugt-4g_zheszovM1Rz2P_rpdR-saGs26NMdKZ7lAtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدور مجوز جذب ۱۷۵۰ نخبه در دستگاه‌های اجرایی
🔹
معاون علمی رئیس‌جمهور: سازوکارهای استخدام ۱۷۵۰ نخبه در دستگاه‌های اجرایی و دانشگاه‌ها، با همکاری سازمان استخدامی و سازمان برنامه نهایی شد.
🔹
فراخوان چهارم جذب نخبگان در دستگاه‌های اجرایی قرار است اوایل آذر از سوی بنیاد ملی نخبگان منتشر شود.
🔹
تأمین کدهای استخدامی این تعداد هدیه‌ای به جامعۀ نخبگانی کشور بهمناسبت روز ملی نخبگان است.
🔹
برای تسهیل جذب اعضای هیئت علمی نخبه در بازۀ زمانی ۱۴۰۳ تا ۱۴۰۵ توافق شد. براساس این توافق، کدهای استخدامی موردنیاز به‌صورت پیش‌دستانه تأمین شده تا روند جذب اعضای هیئت علمی با مشکلات پیشین در تأمین کد استخدامی مواجه نشود.
@Farsna</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/farsna/467455" target="_blank">📅 12:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467454">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RWHk9Im6JHbIz9gPpHfFej11xryGZO_5v_LhmEfmVpmbN-yp_Xti9uEW4KG_egj4cnpz5zrI6AwBQTO84YulgWUb4_6a068trJErKKt1XbK1q-8b1HbRF-C2x12mUYgSooEov1U9RgK-AzmoNbvxbRMANAS7rU1O03y5Y8kcGGhH1vHwemlkl9PFz5tIHaCb7cmhilkyWWXLF-YEaLInJg4StVcX1Vpet1hZqN7vNUcePO6zhU-JQ-Bb4kIGR9I6bRErPkfBWU2-pfMbLXT1NuGEyBoOlevSbxsm2JOWhpFOzjsiQIeeZSi9wgLZv9BdA0T85R8CaHtOnKJQiBZgXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنبهٔ رکوردشکن بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۴ هزار واحدی به ۸ میلیون و ۲۶۵ هزار واحد رسید و در آغاز معاملات رکورد تاریخی جدید ۸ میلیون و ۲۹۰ هزار واحد را ثبت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/farsna/467454" target="_blank">📅 12:38 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467453">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f2a4a24de.mp4?token=qtPFt9Mgn0qL5iaJMTgOfydp_UABsXyvJ8FMzFbZHG96ObkzN1CbLLo1UpGg99UbY-Nvf4RcBPzBsoF8H6NF1fSqiCC_bFIUifzTAvYVihRMYh45gjh7mRik2g_ohjlQq_zfmPeAkYNSisNLNrQ0LteDITjOxsHyX2bdRT2fg2cx5DZTa7v0fL4SE8l_9kHITQS0dBD-H7O59SauHpKd9NFteoBAm8HrW0a46jL0u7ol21tyzR2Nhg0VaVpIRbbN7I6uZYfZxHr0ascu_AU2ITzw60yJ4s5HYN6RZHnLC8HoD4K8xibnbnGjD_TTE9xAoQzZWNHGJiBvWBVEtkeWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f2a4a24de.mp4?token=qtPFt9Mgn0qL5iaJMTgOfydp_UABsXyvJ8FMzFbZHG96ObkzN1CbLLo1UpGg99UbY-Nvf4RcBPzBsoF8H6NF1fSqiCC_bFIUifzTAvYVihRMYh45gjh7mRik2g_ohjlQq_zfmPeAkYNSisNLNrQ0LteDITjOxsHyX2bdRT2fg2cx5DZTa7v0fL4SE8l_9kHITQS0dBD-H7O59SauHpKd9NFteoBAm8HrW0a46jL0u7ol21tyzR2Nhg0VaVpIRbbN7I6uZYfZxHr0ascu_AU2ITzw60yJ4s5HYN6RZHnLC8HoD4K8xibnbnGjD_TTE9xAoQzZWNHGJiBvWBVEtkeWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: نیاز امسال گندم کشور را تولید کرده‌ایم
🔹
برای ذخایر احتیاطی چندماهه، بنا داریم گندم و محصولات دیگر وارد کنیم.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/467453" target="_blank">📅 12:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467452">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">انهدام مهمات عمل‌نکردۀ دشمن در ملارد
🔹
سپاه سیدالشهدا تهران: انهدام مهمات عمل‌نکردۀ تجاوز آمریکایی‌صهیونی در شهرستان ملارد امروز از ساعت ۱۳ الی ۱۷ صورت می‌گیرد.
🔹
احتمال شنیده شدن صدای انفجار، ناشی از عملیات فنی وجود دارد و جای نگرانی برای شهروندان نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/467452" target="_blank">📅 12:28 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467451">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxYJITi3PlZA6rBrSb_o2un0yHRF34Mi1HoGdF94Lu71j7OKlCBR7uWQKWgbaT39SIMoBYddIUChAh7TQlcJLRhNnBCBkM-dFkNsHqLPhVA4pe32S6M9Lte86gsv3IgCwFpiJohDt115gPIyVWdxvK98CZ3xEteHWr5zKkyZYdNN5u_QRrELnVWOciE9W1KVysA-x4L-VJs_h_7D4oIigwNVm4ZCS3Pv8GEaCq4ddb-Cm1CMnTTfVg1xJCocRqBHSOomRNy-T773gQt-8O6eiBJ7hbh-q8BZ7cYC3ETCLPFOH3PuDy0WdwXNcPjrOe7r1jJQEEibHV-2AwZF6RpTLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به روبیو:به سرنوشت والرین دچار خواهيد شد و زانو خواهید زد!
🔹
رپیس مجلس در واکنش به یاوه‌گویی اخیر روبیو در مورد تمدن ایران نوشت: در طول تاریخ، ما ایرانیان با کسانی روبه‌رو شده‌ایم که خود را سروران جهان اعلام کردند و کوشیدند تمدن‌های کهن را…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/467451" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467450">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خنجر یمنی سینۀ تأسیسات ابقیق سعودی را هم هدف گرفت
🔹
گزارش‌هایی از وقوع حادثه‌ای در تأسیسات نفتی بقیق عربستان سعودی حکایت دارد؛ مرکزی راهبردی در صنعت نفت این کشور که تصاویر منتشرشده از آن، توجه کاربران را جلب کرده است.
🔹
براساس تصاویر موجود، مشعل‌های نفتی در…</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/467450" target="_blank">📅 12:09 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467449">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">جیش‌الظلم مسئولیت حادثۀ تروریستی سیستان‌وبلوچستان را بر عهده گرفت
🔹
گروه تروریستی جیش الظلم مسئولیت حادثه تروریستی شهادت معاون اجتماعی انتظامی سیستان و بلوچستان را بر عهده گرفت.
🔸
عصر امروز در پیِ اقدام تروریستی و ناجوانمردانه در محور چشمه زیارت شهرستان زاهدان،…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/467449" target="_blank">📅 12:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467448">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">صدای انفجار کنترل‌شدۀ مهمات در بندرلنگه
🔹
معاون امنیتی فرمانداری بندرلنگه: به‌دلیل خنثی‌سازی و انفجار کنترل‌شدۀ پرتابۀ عمل‌نکردۀ دشمن در حملات آمریکایی‌‌صهیونی به مناطق مختلف شهرستان به‌ویژه حوالی بندرلنگه توسط تیم‌ تخریب، احتمال شنیدن صدای انفجار شدید امروز وجود دارد.
🔹
شهرستان بندرلنگه در ۲۴۰ کیلومتری غرب هرمزگان واقع شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/467448" target="_blank">📅 11:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467447">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ردپای شریفی‌زارچی در حمله به مرکز سخت افزار هوش مصنوعی ایران
🔹
اصابت دقیق به زیرساخت‌های پردازشی و GPU دانشگاه صنعتی شریف، بار دیگر بحث «نفوذ در لایه نخبگانی» را داغ کرده است؛ جایی که برخی تحلیل‌ها، نام علی شریفی‌زارچی را به دلیل دسترسی‌های پیشین به این زیرساخت‌ها،…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farsna/467447" target="_blank">📅 11:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467440">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FupqwLUcS_fCKUI3bRGUYyIdevlZ-jQmHAuydh0PnKGzcCdSi_4UsGxre-IuakhepWhBXFvBPOGweUi0OiWjzlIFt7D35uwYbwjUwPZFUFcxeP_RaVMpB4oVpd_ILOQhhYm5H4DUJWnq4fXfMBNGPni-VjTpL_TFsBPAX4vT2c8ccVrb0QTLjVba3klschcFJkepqneTGQTtWU52RZFiXagnbMBSukt-LFEs6Uy4Qg-YaTOUj8qpzCQEmbKH0skIyCrlC9va_HMdAt2HZw3VJ_-j06BonLMc_pR36QwFRN4seZakImeKlj2CqDJiwOgtoGeDHvFYoTRfLuWUsZgJrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u3V5PzKDhnL00wANRMwbXjQJ4s540Bj09zH7Z0uErt2T6ZuYeLtx-hl7j22W9-jLmiZTNctWqym4B4PeQbzrbO1BqlHRWJiXkhg1uStzBSvWG-qpkRtD5Uy81sVhMcCqAi1MYIiVDv64FVa8PYuSxy8pMcV9DXB3QNXQMGR0w0gUrm2Q0mrnhS3IwD-H_Q4XRHqb3lVxm_NQdiwCTyQruSIKBrVbvwqUvuoNr7D5nHISf5-AbI2q5LCWCQtnnwzNsaqB7pj3DHgyJtDHFeZ2WMhur43rpzgC8OD9ryaGDgYFN7gSASp5Fme-hK7pL6A8r4t6mcHTpo-u2rYS18aQpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PsRhhcuiLTbiGtTpB5V5F1d_bIwo0ojGf4Fn1JNEf3H_UrgXUwL0YF93EEHfNrSCCR5SkbmkHnbqFG2I27Z7DXz2H30GtPUXgAOHAGiFNqvhkkNef1snIwN1SQJqeJyaGP-MwbCxkXYOR_PxXemXsGXBKLN-PyaEl55PpRJv-ZkJis3UC-bN0TG_nnYweOusx0DXGbXLKruoz5HUlVzrfhRpL8u1cys6wkAdSz5HvdCnXRWysnuXWR1nyTD5mxcwsN-XdX7ASTrBetg8ToDWKI7jwbNYGeGMb5fJmLprVZqeNaWImZnYf96yP8ZNC6VAmAYy4ZcOwZzonaZSY4RxEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a936W48yejoFAy2h6hK1Ig-k3OoTa68ROxWkY4uktl378ghukUWqNiOn0_7V6_xgl5Ny1zoHE8WmhRv8H5u6jGQrvjeyMXIE8EeX16Q2aMLRJQEYdT02xehuZ5TxDPxa9zMmmS5HXBJnaQT4RACqEQpMr6pWmsML0B1l306_thw7dZW70U_bj9dMlsQoJFKm-53D4GYGLbWlAUt3DOnbTfatXoK9MalBPa3ED6wkoYOxLNyY8jC4aRgQ_pbKIO9KBQLJL2mt5sZDSLBlB2UOOCh2ZVNHhAgi3RvumcFzhxjxXOqz9FmY7XYP4o-of3LY_QI2GlpM4odtY8_h__oVpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KFE6bqbp_SVXojz63EZF8upRDE-RitIdlf4akqBW5G7u_BT0Wfx7RzXZ1Bn2rcQP6XY0_qW0OuGlB-pvrx81njAIe1SOMnOHrHsewnw6s5-JcyAicEsx6-Iv7kSi7-nso5OtxNtAjhFR5L83MI24c3MLgL_lo4XaNMG3IfPuZxTke_tVXPn0P10NqSsnd4skBBkian7067RlqgoUkg_KoJaMDx90VxmR-gjEmzDxTJ7xjFVBEowPD5NvrjI2PJhcFJXqfYRCIHmMJ8tHz96Te_PuYfEEwwtubRyvbiSQoFC0eNP1gWGKDXT-GmXBf6KjTl1Ijzl98TsWSon-Oo-UXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kV8WYsKm1wMmvjT8JIj-FDWH6R9vENYyUIzftekpIYIDwpoQNoUtKEBObFiSmzeMj16pLgCxCQd-gtuMdPNyWqqAhahQQV2bdF-YvLu_gg9EcUZcHn2NUiaKfMUipoJo7fk3JXhFDXQwz9xYz8tSt0uic9R_-m_UqJcWMtsZYJL9hCbusj5ko-cebsQsRaVZMFSXJC4fV3tDwq0Eyzs9NrWK8Bo47EJ9yk_FyfEsHYAoTB0LX5m-j5XmlfEwfnBnmz7QZaAeNCZnnf90vevYGXZ8Tn94lyk0EO1UXiazk0-SmHUc1kIqBQVfxeFFalFGbjDNUmgOPYdarvqeZCunEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8PRrzzq7HNFS4jaJB_v90VoMF_Z1Th69Xt6uz2m9pWVla2hfBA6N6szz8vEar0Vf7fYJzTVvgo1c8kB0L1CAZDvZ-uHw8rjPCO3n_jE4urPJ4sSdfonKYiq-1ijDBe4cusxj_QgYP90v4VkA68GceK4mOU4kF144wqZ47fg9Ym2G82gIPu4COlYtbyoFpDsKq94N5ZGAR2YBQgmDOcXmBEH_TV6s2Z1T5m47vtQHZa4dviDe-ustbdVqSiVKbAvXTGomZuu56TrXvJCPItuDRj1_oHNuBzrLRh1BBGJZ3bXZrYjtJCjeAvFD9qUB7xrevMRcmkwCIQXtjETBRtKxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مُشت‌وآتش در مسابقات رزمی غرب کشور
🔹
مسابقات قهرمانی چندجانبۀ رزمی غرب کشور؛ یادوارۀ شهید حاج حسین همدانی به میزبانی همدان در سالن ۶ هزار نفری شهید سلیمانی برگزار شد.
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/467440" target="_blank">📅 11:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467439">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">‌ رشیدی: جلسۀ رای اعتماد به وزیر پیشنهادیِ دفاع یکشنبه یا سه‌شنبه ۲۶ و ۲۸ مهر برگزار می‌شود
🔹
عضو هیئت‌رئیسۀ مجلس: درخصوص برگزاری در صحن مجلس تصمیم نهایی گرفته نشده.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/467439" target="_blank">📅 11:19 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467435">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alFJFKBw-4CU8T9pnAn0qDo-Cd8pD_EpocislZpVJ3J0R3jzI1gyE_O_5_sUov-Li8DThTjCb0azzPlBkEEITJk2KsbA16v4eyjBRS3cDSAXLcNGmjuh2VOa624A_iBqm8y1a9xWL6X2VqczK3b1PTrdQcGeIqSrKLD-3Obe7zWXobRishaXIl39F5cN92b6xNLxhg1tcifAYGwJsfUfOWwxMChok7c1ri6VIMc6KM0OZYre7R3eRqsLgWCFf0_Veq9xhL5qBwh6yjcTHR872Wb-fDHt1c_pQ3WkZ50DvKY-YBY-1Fp4LnJQXkOub1tsFLpRbUGfnr1K1MM2d1M3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g_lvLDCeqmWu52jYVbmk-ZuEKUFqYlHMcrhtzgRMt9kKquEikli_BeI_OxciL82GzBa9WrDY9E9QKnu3UQkgZUABNV0iOpD-P1cE02KSVXDcwlsZqu7ZyT1SHAycBVxS2iXSpOk-BAf0zaNRd46anmHbp83t9u-ugjlDN5VvsS3C-YlWo4vq_D-Pg0VRRYNpGfSfTN_GPbzVK2kr8L9vFm4poq4uI-v8qFa4aPESsQsPEK2SsN3i1WuZ2_wMDK3TDk_AntoXe8GLVnASJ9c0ezFivkBCmmVg6pyUqP5yEZlgBYda6Qef3X6Uf2vY-o27WzG0ojCYSq5Jo3dDLiRQYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G2cCjadhj0wEGcuBbsOExu4gOgwFwnBDRRK7HeXt3paUyxB-0vt628TUiQC6DFxWx32FU-9lD1dfc7ol5H6LxP92Xa8h6T3BTdpEfPIdDkJxwijnooYIjYl-Wk2AsEnvnl7KUzUyc6ijzjOHhe02R6q1MIrDDpUnAZi0pIsZ3XzI9dihyZ7-q1CJ2GpWbbmqGQc88-KNAtsUPk-ViRgtTNiwNt74gkbMgQVxv4FsnWJHFO4NKHB_dXaTE27EWsD29NMVD-Oo74MxjIPajZkTCcfDS-SsPvwLReBWX6B3lylA1OPgqz11_201OOvZ54VFZ-tgJOJl4vylXGelIV8blg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZktlsR5T2DEBUwX5TyJ5tk6R2igwUpj_3FlUUeOghwV9v4BAsoRCTzOg1nWvNW9Tqb8-fABenNvslaYN8Crk_DK1EwIvKfKvI-dRRTMSRmICgJRy5Lb_F0J2BW5vUBpoNvh6odWxTh2N3olnXRw54U9OMwYjaAzkvfq_hWkpdfvFuGZBNl_oKcXAwcIB-F6SCpj7pk9LuhdqpSo3zbZYd291wkNRHQs7-XIKdinhGWXMF27vSD4KNTEcrSA4SxFGURGuL14W0GPhDlihKUl5hF_v7B2BQSOXpf2TcXePmZid9c9MtgTPLgJS6cq7E9mhOxfZvUYXl_v6gqQejkCdig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پنتاگون آمار تلفاتش در جنگ با ایران را باز هم افزایش داد
🔹
پنتاگون در ادامه انتشار تدریجی آمار تلفات خود در جنگ علیه ایران، شمار نظامیان آمریکایی کشته‌شده را تا نهم اکتبر (۱۷ مهر) به ۲۱ نفر و شمار زخمی‌ها را به ۸۶۵ نفر افزایش داد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/467435" target="_blank">📅 11:17 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467434">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07ce55938.mp4?token=MVgn8u49hjdigadVC-0S4MWN1iWkCfJ0sgmChyFM9fdQukVuvKou2ljScKeAQafIqZz6hCxm6YEB-Kd2E-vYtFpsxNDKqXmapI79DfxnwuOZVkmwlo3XoVuRprH1p7dzcv4kclAHizVOkzfWx4_ahNXVPDDjPoxI2DhTrCIwBgsf42fueYK935EaZ83DBWNMBC9970KE-CoxF6fvPV_D6Gsa4-dPs5YeW4moUHG6YF7vKll1YLYMzCRjBXFe393qd6rvc0E8trdEzYPa8jGAS-iXsqwp654xez8pu1a9RTe_g7u4oo4ZHjDhh_yEatgeJwQHu2gafgPCRwvrgioR4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07ce55938.mp4?token=MVgn8u49hjdigadVC-0S4MWN1iWkCfJ0sgmChyFM9fdQukVuvKou2ljScKeAQafIqZz6hCxm6YEB-Kd2E-vYtFpsxNDKqXmapI79DfxnwuOZVkmwlo3XoVuRprH1p7dzcv4kclAHizVOkzfWx4_ahNXVPDDjPoxI2DhTrCIwBgsf42fueYK935EaZ83DBWNMBC9970KE-CoxF6fvPV_D6Gsa4-dPs5YeW4moUHG6YF7vKll1YLYMzCRjBXFe393qd6rvc0E8trdEzYPa8jGAS-iXsqwp654xez8pu1a9RTe_g7u4oo4ZHjDhh_yEatgeJwQHu2gafgPCRwvrgioR4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرسش و پاسخ‌هایی که رازهای پروندهٔ فساد را مقابل رئیس عدلیه افشا کرد
🔹
اعتراف متهمان پرونده علیه هم: در ۲۰۰ پرونده ۱۰۰ میلیارد حق‌الوکاله گرفتم.
🔹
متهم دیگر پرونده: حاج آقا این فرد دروغ می‌گوید؛ فقط در یک پرونده ۳۰۰ میلیارد از من گرفت!
🔸
متهم وکیل پرونده:…</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/farsna/467434" target="_blank">📅 11:07 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467433">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d006e0e9.mp4?token=RyAAQFa7dLzSm5Ody72LZWAhVRQ9c9ofg2gNsN3Ot2mGw3oQUhqT0KLBFhQfc3Zgwck7Q2DByV9h09AQdA_kXJyi-rsMftqWYsfqdiqRnuqlLI6Rugzb2seqKc02ZMlhQtGWfaQNIe9HM_vzBcdBfVoWoZx37qIdPaLwP1ORdiEpXwgjFiVyjLZ1cCHisgr7P_pioozRrw8DnW2DgUyZLd3p7b8usRKFFPHJ4faY8_Ek9ChkgVa-38RE4uKLwI74f2zKpoSQjrYbyNBklht5-tAhMvREE9K2j2SRXuAhp63MBAwxn0rduEF_9cQskq_UggoGMuZ3_F4KbhUbxS4KQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d006e0e9.mp4?token=RyAAQFa7dLzSm5Ody72LZWAhVRQ9c9ofg2gNsN3Ot2mGw3oQUhqT0KLBFhQfc3Zgwck7Q2DByV9h09AQdA_kXJyi-rsMftqWYsfqdiqRnuqlLI6Rugzb2seqKc02ZMlhQtGWfaQNIe9HM_vzBcdBfVoWoZx37qIdPaLwP1ORdiEpXwgjFiVyjLZ1cCHisgr7P_pioozRrw8DnW2DgUyZLd3p7b8usRKFFPHJ4faY8_Ek9ChkgVa-38RE4uKLwI74f2zKpoSQjrYbyNBklht5-tAhMvREE9K2j2SRXuAhp63MBAwxn0rduEF_9cQskq_UggoGMuZ3_F4KbhUbxS4KQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حکایت دوست‌هایی که باند اخاذی تشکیل دادند و دلارهایی که در یک کیسهٔ پلاستیکی برای نفوذ در پرونده هزینه شد
🔹
اژه‌ای خطاب به متهم: می‌گویی «صادقانه صحبت می‌کنم»؛ کجای این صحبت‌ها صادقانه است؟! شما وکیلی با سابقهٔ ۱۸ سال کار هستید؛ کجای این حرف‌ها صادقانه است؟!…</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/467433" target="_blank">📅 11:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467432">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c2d1e6453.mp4?token=lckD-DwRdZUUKrt-oMA1dbsB2PPlpa_HHt5UU5bI9oMWRALznMtzZbQiky8nntV73KwixoEsEJSA4yb8H57akhNWQreGaIBcGUfi5t3e6oPK4qEEW_1W1TFMCrIpkoLsbiT7XRBdbRtGYsZiLlZc2QRN8D_ilagBV_cTi0ZghRRgoXE6WQpN0XADVDfgB9Wgn8iREkltmmg01ZA-GWe-c7mFJtNNNzyIXkXH2wbd9u38elJjNfHByFgDsN5LbJYF7h9v6pvITg4SKRDxfZaRUJ7kMCoBJ0iCHAtu58dZYVG6ZAocpBwSS7LnhrIry6kHLGgbUJmas9iwJ8r2qsoGAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c2d1e6453.mp4?token=lckD-DwRdZUUKrt-oMA1dbsB2PPlpa_HHt5UU5bI9oMWRALznMtzZbQiky8nntV73KwixoEsEJSA4yb8H57akhNWQreGaIBcGUfi5t3e6oPK4qEEW_1W1TFMCrIpkoLsbiT7XRBdbRtGYsZiLlZc2QRN8D_ilagBV_cTi0ZghRRgoXE6WQpN0XADVDfgB9Wgn8iREkltmmg01ZA-GWe-c7mFJtNNNzyIXkXH2wbd9u38elJjNfHByFgDsN5LbJYF7h9v6pvITg4SKRDxfZaRUJ7kMCoBJ0iCHAtu58dZYVG6ZAocpBwSS7LnhrIry6kHLGgbUJmas9iwJ8r2qsoGAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: کسی که وکیل است و در یک پرونده به‌دروغ می‌گوید «من سابقهٔ کیفری ندارم» درحالی‌که سابقهٔ کیفری دارد، دیگر باید حساب بقیه کارهای او را کرد!
🔸
وکیل کارچاق‌کن با وجود داشتن سابقه کیفری به بازپرس پرونده‌اش می‌گوید «بدون سابقه هستم» و در ادامه مشخص می‌شود…</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/467432" target="_blank">📅 10:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467431">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/522474d843.mp4?token=m5tQXYsWtKpxdh298RSPNrjdm7DK1KnWK8mvf_-nChta3LcMbGX7wzVyVg8XefroHmr1s_j9-2fgYj3TXuDaH2wdLLUq-y0zS8K7YmKEZwH4TFFCU7jEvfv4wmOot22ay4GsN2zum5Qnw8KFaYV5FpkLxmw0CRvL91dC0PXkHjbFLf-MW-oZpUYHaz5IjorqhnO-WOtqkRwCT7cYKfP8rwv9xM4HxKlVhqmzRm8vUeIfJIsJbImCZvVqqIW6Nl7F9m8A0-LXEjLwkRSJV8sL232Mh2hW5rNsEeWDalrW_wRrX5SoeltmTPwb744Ddm5JthOzbcDVyqTENnHWseoauA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/522474d843.mp4?token=m5tQXYsWtKpxdh298RSPNrjdm7DK1KnWK8mvf_-nChta3LcMbGX7wzVyVg8XefroHmr1s_j9-2fgYj3TXuDaH2wdLLUq-y0zS8K7YmKEZwH4TFFCU7jEvfv4wmOot22ay4GsN2zum5Qnw8KFaYV5FpkLxmw0CRvL91dC0PXkHjbFLf-MW-oZpUYHaz5IjorqhnO-WOtqkRwCT7cYKfP8rwv9xM4HxKlVhqmzRm8vUeIfJIsJbImCZvVqqIW6Nl7F9m8A0-LXEjLwkRSJV8sL232Mh2hW5rNsEeWDalrW_wRrX5SoeltmTPwb744Ddm5JthOzbcDVyqTENnHWseoauA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: فیلم روش‌های عملکرد باندهای فساد و کارچاق‌کنی را پخش کنید! مردم نباید گول امثال این افراد را بخورند.  @Farsna</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/farsna/467431" target="_blank">📅 10:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467428">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R3wLdNXTPpOPkeGUM8SbZ451DX7zzLmBWldeJeyZG-_xZyahBOpZpoZFAQwoxlhdym42JXEJdtmf6Gi86N3JnBdSCCldan_ftV0JmydVAvF1igKgxzA1t13bpQ_K4ieGqCU9lnrBopiJCEAVL2pz1wDTLPUZeNcg__tU5QwEQDSS1mE0OaDSdjssmN-BdnKkROMFnBgKCi96UABfKr0XBe_zqgtqqP9QrJUqMLoMzC1tzBrOlEVeD8wVyul_Ixofa0X1CeJgoPDZlF8MbLJmFKv3Lx3deaxjl21LYXnpc2iBMMqSjrZwMGfm5P1Wx9cqXM3Q-FBb025yTgFNfEVBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AS8hdrGnXkCO5G9Uj_1AZbUei1n19xUTrLZe03XRPUjll4cJ7Cyy1d9lYDhztr8L45Zc7RPrEInhX7cZgiSt2WG6ANmfvR5TZQZudlea5qEcXlsosZshLrSTlRu90dOfGIMjDk0yjlYil7bqpOGz6jX12Su3TrfaGlEv8RkcnmPHBfJl8bNqZ_blRGX0nwwRMoVuMWaipzRitF21c4TMVB4W-f6WVHJmaLdn9xsqr333dxMfqM4AxN9P6R9zC36dn7AGv8-DffQ0rpVpOaWwiHyHU61wbYvhylO7Qwk2Y1EnbCGuuTqyNW-B3oxL1P5bgjHULlpWf_NwytlGlLpNLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N2mI3bI2S1QDC3iDjNZuvgil8wd7ESKfeoK5UwpapA9s_hBJc8cxBd_8tw4ATAz0gjMm2kOKHeyArOiM1NEjhhD4otOuI8RcascNhjYlbaZEmPcMygMIahjy5t0lTgPpfEmS-ol38sVM3MyMvIHjCL0G99nk2ZGJDFRCF741oMqY37aapSWKP8R9z4WgyvyqdjOHFBfNG3CBZyhNAyIQ9kYwVY1KzQID7K9j4Maahskp5LMP3a1agHSQSYW3aMICG_NsSag1eKEP99mU2oyYfWxDcaTdetFAOGf9vOAg7sRi2k4hgXM1wjzekuriY7SqxSFPjfz-jrRs0u8LQUlP1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ورود ۷ اتوبوس ۱۸
و
‌ ۲۶ متری چینی به کشور
🔹
معاون حمل‌ونقل شهردار تهران: ۲ دستگاه اتوبوس ۲۶ متری برقی، ۵ دستگاه اتوبوس ۱۸ متری برقی و ۱۰ دستگاه شارژر پرتابل مخصوص همین اتوبوس‌ها وارد کشور شده‌اند.
🔹
از گمرک ایران درخواست داریم که هرچه سریع‌تر نسبت به ترخیص این وسایل نقلیه اقدام کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/467428" target="_blank">📅 10:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467427">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4c6ed918.mp4?token=sFNrDVzjmWoQ_YZzlDbYwptL7Jt56neVaa1Nfa7T3bTqFEp3FKSgLOOT51RSntMq7DWvCveu6tNIn-ZkWyFzDjiA6bd1NpmX8ogh7ASdpvBkFpPfVyYuiBgsWpbbSEGPniYHd-Nt1yQE3-U0K3pEllhYyy3qsozsmkIKWlHAL__hhVAQqiqjf0rcRAIHTFc5uDq7L3afeuWfUOcQgktZ0Xn_YPxGK73t5Fy34EKliEN7JYGXK0g17on3JU943UugULzBJn1hA4LcWQElLhz4rW_k0-zDPD-dCiIEMz8Pz5cyuDjiGXo3w39MFGuX_k8tJKTsqwkbQZt_gLk4dVdUQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4c6ed918.mp4?token=sFNrDVzjmWoQ_YZzlDbYwptL7Jt56neVaa1Nfa7T3bTqFEp3FKSgLOOT51RSntMq7DWvCveu6tNIn-ZkWyFzDjiA6bd1NpmX8ogh7ASdpvBkFpPfVyYuiBgsWpbbSEGPniYHd-Nt1yQE3-U0K3pEllhYyy3qsozsmkIKWlHAL__hhVAQqiqjf0rcRAIHTFc5uDq7L3afeuWfUOcQgktZ0Xn_YPxGK73t5Fy34EKliEN7JYGXK0g17on3JU943UugULzBJn1hA4LcWQElLhz4rW_k0-zDPD-dCiIEMz8Pz5cyuDjiGXo3w39MFGuX_k8tJKTsqwkbQZt_gLk4dVdUQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعجب اژه‌ای از مدل رفتار یک وکیل در یک پرونده
🔹
رئیس قوه‌قضائیه با سؤالات مکرر از یک وکیل متهم، تناقض حرف‌های او در اعلام اینکه سالانه مالیات پرداخت می‌کند را نشان داد.
🔹
متهم: ۹۹ درصد وکلا برای فرار از مالیات دلار یا سکه می‌گیرند؛ من سالانه تا ۱۰۰ میلیون…</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/farsna/467427" target="_blank">📅 10:49 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467426">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78bccbf3da.mp4?token=SjA0koaz31e2oxTi3Ei2-MOrwjcj96EWKGSYUMR955AZ4FRtJiE_SK55QbJ0ztUdiEPWYQTfWr9LTfCezzJX-rSI-11jhI4ZPANGSx1fbfnkJ3EmkTn8tcuXfOz7lxTW4yS_E9lOWjlzXdn4Sy4b5mBOgmwg_rdDkOFqAgymxqZVxOOmdxP8wy0AulUoGLkBKFaVxmENd-ozCc73sZ6Ytf7tmjoh_FR8ttMMhwq1ESkdBgao99EVBDESELr0L57nVZSPpQufUXv6XrQYRzzkZeo9hWy5_2FQ8g8g5cOFHdGMEwG_ywZ_nMmfMrzlS4V8wm5eZ4t6WXFoOXu_xEmZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78bccbf3da.mp4?token=SjA0koaz31e2oxTi3Ei2-MOrwjcj96EWKGSYUMR955AZ4FRtJiE_SK55QbJ0ztUdiEPWYQTfWr9LTfCezzJX-rSI-11jhI4ZPANGSx1fbfnkJ3EmkTn8tcuXfOz7lxTW4yS_E9lOWjlzXdn4Sy4b5mBOgmwg_rdDkOFqAgymxqZVxOOmdxP8wy0AulUoGLkBKFaVxmENd-ozCc73sZ6Ytf7tmjoh_FR8ttMMhwq1ESkdBgao99EVBDESELr0L57nVZSPpQufUXv6XrQYRzzkZeo9hWy5_2FQ8g8g5cOFHdGMEwG_ywZ_nMmfMrzlS4V8wm5eZ4t6WXFoOXu_xEmZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی مستقیم اژه‌ای با متهمان یکی از پرونده‌های فساد
🔹
رئیس قوه‌قضائیه یکی از پرونده‌‌های فساد با عنوان «ادعای اعمال نفوذ در قوه‌قضائیه و جعل عنوان مقامات» را شخصاً بررسی کرد.
🔹
اژه‌ای خطاب به شاکی پرونده: نمی‌توان این عبارت را در قبال شما به‌کار برد…</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/467426" target="_blank">📅 10:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467425">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77c43ae4f.mp4?token=WeVekmxBSWxKNsk0jktsoUMuxXzQ3ZQ1FMAf37d7IS0CwmU7wIVi-2cdgFakOWy7pR0p1m8SDcLmBk0osZQ5MNIi4YDK-T3panltlMsOmBIexxJj6z2ZyYOqxaofThF1sYmXXLb0M1b1A1bpk8gN0ZCsLU9QqXHFf6s1wUPLQtpZRU8qcEg4l9Tanqv651zeH7xMEEnOgLUGPBTBKq9KQ4P_Gzao7bAX-8ym97LRPc30icpvNq5lA6qh5MMu4DNHQzsX_FjpXWMlXyudjzjp8FK3VJdJIKvZFmsRYzzyDcTVPL7cJrHGX51jyAqQiNq_-Kh3comygut5cpdH5EjEVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77c43ae4f.mp4?token=WeVekmxBSWxKNsk0jktsoUMuxXzQ3ZQ1FMAf37d7IS0CwmU7wIVi-2cdgFakOWy7pR0p1m8SDcLmBk0osZQ5MNIi4YDK-T3panltlMsOmBIexxJj6z2ZyYOqxaofThF1sYmXXLb0M1b1A1bpk8gN0ZCsLU9QqXHFf6s1wUPLQtpZRU8qcEg4l9Tanqv651zeH7xMEEnOgLUGPBTBKq9KQ4P_Gzao7bAX-8ym97LRPc30icpvNq5lA6qh5MMu4DNHQzsX_FjpXWMlXyudjzjp8FK3VJdJIKvZFmsRYzzyDcTVPL7cJrHGX51jyAqQiNq_-Kh3comygut5cpdH5EjEVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگوی مستقیم اژه‌ای با متهمان یکی از پرونده‌های فساد
🔹
رئیس قوه‌قضائیه یکی از پرونده‌‌های فساد با عنوان «ادعای اعمال نفوذ در قوه‌قضائیه و جعل عنوان مقامات» را شخصاً بررسی کرد.
🔹
اژه‌ای خطاب به شاکی پرونده: نمی‌توان این عبارت را در قبال شما به‌کار برد که موردِ اخاذی و کلاهبرداری قرار گرفته‌اید؛ چون شما با علم به غیرقانونی‌بودن فرایندی که متهمان این پرونده پی گرفته بودند، اموالی را در اختیار آن‌ها گذاشتید و از همان ابتدا می‌دانستید که روندهای طی‌شده توسط متهمان، مجرمانه و خلاف قانون است؛ لکن برای نیل به اهداف و اغراض خود، اصطلاحاً به ساز این متهمان رقصیدید و هرآنچه آنان گفتند را اجابت کردید.
🔹
بسیاری از افراد تصور می‌کنند صرفِ «ازدست‌دادن مال» آن‌ها را در جایگاهِ بزه‌دیده یا «قربانی» قرار می‌دهد؛ غافل از اینکه علم و آگاهی به نامشروع‌بودنِ معامله یا فرایند، عنصر بزه‌دیدگی را مخدوش می‌کند.
🔹
ما قاطعانه و منطبق با قانون، با مدعیان اعمال نفوذ در قوه‌قضاییه، جاعلان حرفه‌ای و شبکه‌ای، غاصبان عناوین و سوء‌استفاده‌کنندگان از نام و امضای مجعول مقامات برخورد می‌کنیم و در این زمینه هیچ اغماض و مماشاتی نخواهیم داشت.
@Farsna</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/farsna/467425" target="_blank">📅 10:35 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467424">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هشدار یمن ۸۱ پرواز صبح شنبهٔ ریاض را لغو کرد
🔹
در پی هشدار نیروهای مسلح یمن به شرکت‌های هواپیمایی بین‌المللی دربارهٔ «تبدیل‌شدن حریم هوایی عربستان به صحنهٔ عملیات نظامی»، در ۳ روز گذشته ۵۸۷ پرواز در فرودگاه بین‌المللی ملک خالد ریاض لغو شد.
🔹
داده‌های سامانهٔ ردیابی پرواز «فلایت‌رادار» از تداوم اختلالات شدید در تردد هوایی فرودگاه بین‌المللی «ملک خالد» ریاض حکایت دارد؛ به‌گونه‌ای که در ساعات ابتدایی امروز هم ۸۱ پرواز در این فرودگاه لغو شد و دیروز هم ۱۷۱ پرواز لغو شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/farsna/467424" target="_blank">📅 10:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467423">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bbbec628.mp4?token=ja70OS2EttcSMN2O9zT9eYy5uW8_fPZk-S_nV5OUzLuNr-sjyl3PBf3y5dNlb0nqjY6npheamBUFuCK0Pnv6TSFxOf_-EtAnta5b4K6tDgl7SPDt1XKCR9mPvUfuGWG_88rtUUYU50XN8pwulj3FkO4vepfrAnWcx6kvEJzhIWqeGeq8LvrbJVJSVaTheyBwtshaKLYI9wzfmN0eUaxP883QZJmLNxkhie_1RQwq8yG0ZNUzSTh4kwRCyfQnBlX7xkjEBe-1qi-xdTtfYuLvBamijUAFu9BRevNenmR6SjBKD7PraGU-Y5dRYH_yOr_f4wiIsvNyYssl18LxFTPRLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bbbec628.mp4?token=ja70OS2EttcSMN2O9zT9eYy5uW8_fPZk-S_nV5OUzLuNr-sjyl3PBf3y5dNlb0nqjY6npheamBUFuCK0Pnv6TSFxOf_-EtAnta5b4K6tDgl7SPDt1XKCR9mPvUfuGWG_88rtUUYU50XN8pwulj3FkO4vepfrAnWcx6kvEJzhIWqeGeq8LvrbJVJSVaTheyBwtshaKLYI9wzfmN0eUaxP883QZJmLNxkhie_1RQwq8yG0ZNUzSTh4kwRCyfQnBlX7xkjEBe-1qi-xdTtfYuLvBamijUAFu9BRevNenmR6SjBKD7PraGU-Y5dRYH_yOr_f4wiIsvNyYssl18LxFTPRLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خرید هواپیماهای اطفای حریق در دستور کار مدیریت بحران
🔹
رئیس سازمان مدیریت بحران: سفارش ۲ فروند هواپیمای اطفای حریق و قرارداد تأمین ۲۰ فروند پرندۀ امدادی و اطفایی انجام شده است. @Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/467423" target="_blank">📅 10:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467422">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5KbI_ciVYtuOnDmdcdlcy2PFeV4Ef1UnzjgvZ_7RR0UKHnRVnfmM54YL1VvzeF29b79KaZC5ZLeIkP6PMGGqru9fyOorahxxkpXgg5JfJE3Y5EHIIiISNZyN-oOnEFL0r2Z9cy9m531IcwOgy-oXCUfxwXdovTCR7BG0yFxmSACsHYTLRO__JRJA79GSPTGYraUPs2GnMxqfLP5oWi0LjNf4F3Tbtsdi8uspE9VoFSC2A5MpeLF8tgxK0VuFtxSkn9gwNeQo_l6b68sKGDJuytfQFOH3B78Z4JCN7_uASl6Gc705NXQspP_l5LaaQvTQjKb9JAuI-tqxfK2OAt3_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان برای حضور در گردهمایی آیین سال زراعی ۱۴۰۶ به کرج رفت.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/467422" target="_blank">📅 10:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467421">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f85b96f75.mp4?token=rfTJDqZ6Ujb9ocN9vOrHbVN2MWcX-S1RkY6L7iZfeoXi2xupODx3-4GtsPXZG-Xt_Z3tQjD_4QCWBpJndXVv3U8DKAfsTfBB4YV-ksivBse8HTOeB2sJCv-IVpSzIiU5b1XqWtHAvHtIZYgioOyyUTQRkw51-hEcU1Il6WhecKqft3zAgzaISbqEsQTC-EcnrE4XCX_IFfDwH1zDmwYnrPoAGlZVAAidiVEUg4xvUw56ryxQxgoC-mlR_tELFo2hzWKL362967IE-fRHjVGtz8CPP6H9rG5n0AF7Am3kzxnH9cQIL_C7PMyURGmcHK0vMDRkb4L7r19SJqX5T8Magw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f85b96f75.mp4?token=rfTJDqZ6Ujb9ocN9vOrHbVN2MWcX-S1RkY6L7iZfeoXi2xupODx3-4GtsPXZG-Xt_Z3tQjD_4QCWBpJndXVv3U8DKAfsTfBB4YV-ksivBse8HTOeB2sJCv-IVpSzIiU5b1XqWtHAvHtIZYgioOyyUTQRkw51-hEcU1Il6WhecKqft3zAgzaISbqEsQTC-EcnrE4XCX_IFfDwH1zDmwYnrPoAGlZVAAidiVEUg4xvUw56ryxQxgoC-mlR_tELFo2hzWKL362967IE-fRHjVGtz8CPP6H9rG5n0AF7Am3kzxnH9cQIL_C7PMyURGmcHK0vMDRkb4L7r19SJqX5T8Magw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان مدیریت بحران: برای پدیدۀ ال‌نینو آمادگی کامل داریم
🔹
مردم به هشدارها توجه کنند تا آسیب‌ها کمتر شود. @Farsna</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/farsna/467421" target="_blank">📅 09:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467420">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fb2e8355.mp4?token=MkJ5mx-1TclcONrpcKT9QVRlmUcF3No3gR7Wv15KoLyNYWa9uZLhyBJgwsHdbEG-2RrnX7MLNTBkuVdoX8UNR6IQhXu2tLhpwRW8k7lyuwb9JqbG_wwe5rjexRPnXLrpaS-VD-BOH4hyKKPAXd4LrmR8C27wbFCRMQdcfhSDIYRRcto8TSZ0x6nc4gRIyozOQ6beg6yE_R7mrGwVso-zbLMxlMmIxLylGhWiJrYMQh2kI69_sT86g3J-1YJOw69AFQ9JLPUbTXFi3IimJaHnuRAmLPVLkdrS0fh3lS6tN_qPUjrJoCFDhYQV0Hq3IE8JCzfE10k9B1jZbyGAMWXjhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fb2e8355.mp4?token=MkJ5mx-1TclcONrpcKT9QVRlmUcF3No3gR7Wv15KoLyNYWa9uZLhyBJgwsHdbEG-2RrnX7MLNTBkuVdoX8UNR6IQhXu2tLhpwRW8k7lyuwb9JqbG_wwe5rjexRPnXLrpaS-VD-BOH4hyKKPAXd4LrmR8C27wbFCRMQdcfhSDIYRRcto8TSZ0x6nc4gRIyozOQ6beg6yE_R7mrGwVso-zbLMxlMmIxLylGhWiJrYMQh2kI69_sT86g3J-1YJOw69AFQ9JLPUbTXFi3IimJaHnuRAmLPVLkdrS0fh3lS6tN_qPUjrJoCFDhYQV0Hq3IE8JCzfE10k9B1jZbyGAMWXjhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پاییز پرباران در راه ایران
🔹
سازمان جهانی هواشناسی به‌تازگی اعلام کرده احتمال شکل‌گیری پدیدۀ النینو در تابستان ۲۰۲۶ حدود ۸۰ درصد است و این احتمال تا پاییز و زمستان به بیش از ۹۰ درصد می‌رسد.
🔹
النینو که با گرم شدن غیرعادی آب اقیانوس آرام شناخته می‌شود، معمولاً…</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/467420" target="_blank">📅 09:37 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467419">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8g68APR9hcVDt8qH3P5s7XphL8bfX8Cj0Fx6wooYQFAhbm2b7Lu3VyzV9VmzKEG0Nd0cqqAjxF8frTxY0gQ9jrYNIYWcOKC20shM7TOdgYeLwlZC_HCqmHAeVwB53DLZS74IDVYgSRDpzIUr6-wwEcUt7xOL5-BONOokA5rizA23jvkD3K4PCFL2qCSzA9OBzikPHgpQcbbWnQtCyBJQIQNl36VrQMJDRnSERjjG31IT31uyMlp8-oNNBR_E9zb3Uc2nPL6XFUTq0GGDTTrJQ0qAEYpRZiAWoN38nAwE9B1O4FGPSHsZld5v8URRJyqrLgbPlAkLVwzEqaJcov-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/farsna/467419" target="_blank">📅 09:30 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467418">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YklMJPb3WpUiNtWq6p85IEUvib8ZOpNzqgXXaqCRZPQZYCiTJNipT9FxMgQE3dFS8STbJJYzuaWSdzuBXHUn9sQQ-NCgktiFMDcqnkVen2T4JESWcmNwvouOLWRC1KFcMPqFbVYkjTCd0VC5Wum_GzsF5wyQw-VAV_qeOPbrYsAI1uS9YUgrb-HYKE94SC78RLILZBHYjbrRUJwSYWvNVFIYxB15R2afYQRfH0AR00wbZZo8f9Sr6BZ7LQzr5QbpSvpIuWD3Pku-oJfIGCzoSgi1qd5e4gr5mjdjK5hSjujGFpqDC1q6mp9HC-WhG4vp7ncmkGepdEjSkp7065qrKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان برای حضور در گردهمایی آیین سال زراعی ۱۴۰۶ به کرج رفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467418" target="_blank">📅 09:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467417">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc5ec9619.mp4?token=lK7-rFFrDSaJaeqbIneV9j6TzDuLcWoQOZhZ43pG0nveZyrJ4lTptOq6jpmt7-7S0Lu9xsmx62JqRSnlWKzpXKErcz0nsrbGg4sML5CMGL5WogOdrNvqvnjgzgh05XzbQOgmEnuhAjcQGvAGhSuWXbKSq4L0B550Z_ogHsNvngmskflKCE_SRY7XCrdfA_Hm3ty8CkAXr4Rm1u-H_kEhEpXOCEJfXRHjjgxmoaM5ug4GylwA8J77VwdwBvS4zlkXgbnmagKslAKWb_bY1pY6T4pxf-Jsn9YE5UW8vYf1Fid89yAvpGCrr20AxuOozpyBANnlt9QgH3ooDkpMlIbRMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc5ec9619.mp4?token=lK7-rFFrDSaJaeqbIneV9j6TzDuLcWoQOZhZ43pG0nveZyrJ4lTptOq6jpmt7-7S0Lu9xsmx62JqRSnlWKzpXKErcz0nsrbGg4sML5CMGL5WogOdrNvqvnjgzgh05XzbQOgmEnuhAjcQGvAGhSuWXbKSq4L0B550Z_ogHsNvngmskflKCE_SRY7XCrdfA_Hm3ty8CkAXr4Rm1u-H_kEhEpXOCEJfXRHjjgxmoaM5ug4GylwA8J77VwdwBvS4zlkXgbnmagKslAKWb_bY1pY6T4pxf-Jsn9YE5UW8vYf1Fid89yAvpGCrr20AxuOozpyBANnlt9QgH3ooDkpMlIbRMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
در طرح تورم صفر، قیمت‌ها چه‌طور ثابت می‌ماند؟ پاسخ به چند سوال مهم دربارهٔ طرح تثبیت قیمت‌ها  @Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467417" target="_blank">📅 09:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467416">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آمریکا مجوز انجام معاملات مرتبط با واردات گازوئیل از روسیه را صادر کرد
🔹
در چرخشی قابل‌توجه در سیاست تحریمی واشنگتن علیه مسکو، وزارت خزانه‌داری آمریکا مجوز انجام معاملات مرتبط با فروش، تحویل، تخلیه و واردات گازوئیل با منشأ روسیه را تا ۷ آوریل ۲۰۲۷ صادر کرد.…</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/467416" target="_blank">📅 07:57 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467415">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMvN2Uac8AqWkugoAw09s6LVMKSCBzargA4qezMXm3eYeE3OYBv7PmZKIocRe_032V0oxNF5MmzpzvQ6RymIxIS7ZWAziuxvYQzCoastOpnk5hESeOC_KTSP57NjX_foJu_AkDROPivIsBWmFD2nyKERQUlW1EwrpVWNFOn3VCpzOONbiMrh5oGt5zg-UXi9KFRlB9WforDT7qjZJmFiBW_J4D7u1oO5FFE93zz6_RqaNy0GuoBgweEvhS-0LHneQle4V_1BYhT23Kc1NN4Lygx12CUmiMGYG_wg8Zo15z5qzzsDe0HJHO677nZCyyJS9rH9dFy-GBOu-N2PhFAWqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ رویترز: توافق ترامپ با روسیه تأثیر پایداری بر کاهش قیمت سوخت ندارد
🔹
تحلیل‌گران بازار انرژی می‌گویند توافق ترامپ برای عرضهٔ ۳۰۰ هزار تن گازوئیل روسیه به بازار، نمی‌تواند به کاهش پایدار قیمت سوخت منجر شود.
🔹
چراکه این کار صرفاً جریان محدودی از عرضه را به…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/467415" target="_blank">📅 07:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467414">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjPzOKiMoLaMKeesT5gXzNiT81wYGzIecA4fwUeGlBlZpid7DH82C8I5o1uOoROhnvunIqevCLs6fj_tRaEF1LPf16xfaIqQW2ViKDcKbeBVgsJbsU9REzj78vzvSTNX10n8KeVcodXmbexsdevf9_-Sr6UlKMZOFjWWys_45woQDDZPnpcTHNYCX4fW07ovhgw8LowzRUqCO127usCsNMT900IyEXOjpP7dl3-w7g54-dnRG5pAsIezKlHMRTcmAwVsNs-ODjMEw_HvvTc25FAPp4ciukkddQP9UkMrpR9N0aB-jw_VCJrh0CiqXEXVjrmxGpQHiQGL8kwZdgsqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستیاران جدید نکونام، تراکتور را در سفر آسیایی همراهی نمی‌کنند
🔹
کیانوش رحمتی و ناصر فرشباف دو مربی جدیدی هستند که به کادر فنی تراکتور اضافه شده‌اند، اما به‌دلیل صادر نشدن کارت مربیگری امکان همراهی تیم در دیدار آسیایی را ندارند.
🔹
آن‌ها از هفتهٔ نخست لیگ‌برتر روی نیمکت تراکتور خواهند نشست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/467414" target="_blank">📅 07:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467413">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آغاز هفتهٔ جدید، با هوای «قابل‌قبول» تهران
🔸
شاخص امروز کیفیت هوای پایتخت روی عدد ۸۰ و همچنان در وضعیت قابل‌قبول قرار دارد.
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/467413" target="_blank">📅 06:42 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467412">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‌
مدیریت بحران مازندران: از کوهستان‌ها و مسیرهای پرخطر فاصله بگیرید
🔹
از بعدازظهر شنبه ۱۸ تا بعدازظهر یک‌شنبه ۱۹ مهرماه، در تمامی مناطق استان احتمال رگبار باران، رعدوبرق، کاهش دما و وزش باد شدید موقتی وجود دارد.
⚠️
تأکید می‌گردد شهروندان و مسافران از اتراق و توقف در حاشیه و بستر رودخانه‌ها و مسیل‌ها خودداری کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/467412" target="_blank">📅 06:10 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467411">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n3iJD7_ama-NwqJ7d7yOsoeHALmzMIekJCjNToHX7y4F20MU669gj6SZNR8_le5YRS7CQ1CvHvY_oJdx8i7riqZteIvBdNzCLH6VZle3aVxwXPSaHVmd7jEiWgDj9-yPFssnE-4-DfjEl89Lc4zM8dVScXPThibTZhAKeOlzpqXE9MyPT0akprzy4CPbqFwLzWYTBs7jU-mzWhqtdWHqKCovznvpzHq7XMneOcxsIgWrwsGZttFpUcHGw-bXnHHATH6_Hk04aEmKfWg3GmfVQY83H4VC1UZ8eVR52boK8dJTE50tsWmZyTMfmus3QpdL_0OLU-5TtNTGCydL1RaY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پزشکیان: دیپلماسی منطقه‌ای برای ما، صرفاً به معنای برگزاری نشست‌ها نیست؛ بلکه باید به ابزار مدیریت بحران، حفظ ارتباطات، جلوگیری از گسترش درگیری و فعال‌کردن همکاری‌های عملی تبدیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/467411" target="_blank">📅 05:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467410">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gevGMMMbq2xV8k1gVlI1Pc7ZH4adErYey4jrdut5XA_Jj-SZV5jwy6pGzlLuDrwSkDlGZtjOyvqCp3xTLfkkltwNfmE-mTR4PkrNxdbtM0ZeDr6UcEEQ_E2xBoNCcZGlw8bm1xHdcOdtvUMc2Wsktr75_blouFw8EKfXnDfFRFqoEEaBaNKXQzs8LkBkCcZOvESPLUV_0IlYpAnfSmGwbxFMG3dmMw6ia8YisRb2xUz0M7zgg0FXq1iyKlBJhEPwtagrmFaMzGaX75zJqgduuwAoM3moMQVp1zkj-GEAvMNqwz133lHFShVUp-30lD_OUtPXeA26VJUu4zpntvPfIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
در طرح تورم صفر، قیمت‌ها چه‌طور ثابت می‌ماند؟
پاسخ به چند سوال مهم دربارهٔ طرح تثبیت قیمت‌ها
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/467410" target="_blank">📅 05:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467409">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=gz3BymbB83i99l6zKbXvvS_a1MgjIizGTwevq7ZNOZPlxU_7JVT-1Sprg_rV1er94vi5neFa6OgfPs3ce8yHcd-JK-PZg7J2HC87iQ0P04kL0wqf4Vr9-wygV5A-XdbGEFDU4YiGlqmwDkK6wM7TuLfsHL94X6VT0sDDJKObxvRIhYGi0mFQXfUzpIt-58tcF3kkdjLe53EewBNL8zx48aORluQqdZkciqlfccSm-9Fd9lo3GVUYEpg07XCypyt8NwlvSNfzd-5Icvx8TJ_ZszxiB4ssXNdDvQMnfmVZmnMGESSFaZqxjhp7zrOxlJa_auKi7zUsbKYAmmt3FfOSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7ff41a1b6.mp4?token=gz3BymbB83i99l6zKbXvvS_a1MgjIizGTwevq7ZNOZPlxU_7JVT-1Sprg_rV1er94vi5neFa6OgfPs3ce8yHcd-JK-PZg7J2HC87iQ0P04kL0wqf4Vr9-wygV5A-XdbGEFDU4YiGlqmwDkK6wM7TuLfsHL94X6VT0sDDJKObxvRIhYGi0mFQXfUzpIt-58tcF3kkdjLe53EewBNL8zx48aORluQqdZkciqlfccSm-9Fd9lo3GVUYEpg07XCypyt8NwlvSNfzd-5Icvx8TJ_ZszxiB4ssXNdDvQMnfmVZmnMGESSFaZqxjhp7zrOxlJa_auKi7zUsbKYAmmt3FfOSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ دوباره از آرزوی خود برای دریافت جایزه صلح نوبل گفت!
🔹
دونالد ترامپ، رئیس‌جمهور آمریکا، با انتقاد از تصمیم مربوط به جایزهٔ صلح نوبل گفت: آمریکا، با نمایندگی من به‌عنوان رئیس‌جمهور شما، باید جایزه صلح نوبل را دریافت می‌کرد؛ اما این اتفاق نیفتاد!
🔹
این تصمیم، لکه‌ای پاک‌نشدنی بر دامن کشور نروژ است؛ تصمیمی شرم‌آور و مایهٔ سرافکندگی!
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467409" target="_blank">📅 05:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467408">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp_Wiox7jFYR0QdgeoWxU7eyxO3-SBCL2216fLTU0_-zDaYBxXVmpB9qpNZnA29xACwlqoQlOuyO15x-TH6zjWtld_pQZN6xxOEJfy0EgUBtsbpScmod2I4YIgsbZNTj8ci9ej-k96-fug9i5862LT5aiTvgGAUeM7Dlsa_Ut7BgEQ0e2WPYlwCT8y-O_Mz15GH_JxKlLpyazViMaNs2T1vM_J4zN2ayMTczwIYJ-qjFv5qUKoFzM1y7izrncqSI9rjKrl1ZQV6sGl205Mde4tRuHdTbzxeWzvm_HO7zV37wSkbS_NQv5yzYSpGt5XNlSsSMQ9CTdB40-C3QePPoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی به پلیس گزارش قتل دروغ داد
🔹
مدل هوش مصنوعی آنتروپیک در جریان یک آزمایش خودکار، گزارشی جعلی دربارهٔ یک پروندهٔ قتل حل‌نشده را از طریق وب‌سایت پلیس فیلادلفیا ارسال کرد.
🔹
البته پلیس اعلام کرد سامانهٔ ضد هرزنامه این گزارش را شناسایی کرده و اجازه نداده برای بررسی در اختیار بخش‌های تحقیقاتی قرار بگیرد.
🔹
این اتفاق بار دیگر نگرانی‌ها دربارهٔ رفتارهای پیش‌بینی‌نشده عامل‌های هوش مصنوعی و ضرورت نظارت بر اقدامات خودکار آن‌ها را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farsna/467408" target="_blank">📅 05:11 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467407">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYgZ5yv8rEmCI5wFUHiHyZdFiDmSarQbrpdpX9oPfINGTgeP_2EwBYJgX6ydionCZWMzExVOVbX9CzKDcv3VrvL9pZzB_sWKtVNWoPpHn6BckIeIgPTQOe3brRRld_Bs3fhWG2NUBun6feFkT3V98QPwyFk2mUVVIk46txkILNZqMahzYoiT6Is-ijPDAAH5ViLxUheo0ks8b2lth8hIZl59pw8wbN4rLE_am-OKDmzwqbRpl2Uda2h9OsP0ImJWvyXkbEE4_I7E6dNwmL5_7XzbW6WInmpEO7A0G2YfrE97HjEZtcELzVDgip9jH7Cx7bPx7FAj34D00ESj0aCtQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دموکرات‌های کنگرهٔ آمریکا: بهای جنگ ترامپ با ایران را آمریکایی‌ها می‌پردازند
🔹
دموکرات‌های مجلس نمایندگان آمریکا با انتقاد از ترامپ، افزایش قیمت بنزین و گازوئیل در پی جنگ با ایران را محکوم کردند و تصمیم او برای خرید سوخت از روسیه را زیر سؤال بردند.
🔹
گرگوری میکس، عضو ارشد دموکرات کمیتهٔ امور خارجی مجلس نمایندگان آمریکا می‌گوید جنگ فاجعه‌بار ترامپ با ایران باعث افزایش شدید قیمت بنزین و گازوئیل شده و آمریکایی‌ها بهای آن را می‌پردازند.
🔹
او همچنین از تصمیم ترامپ برای خرید انرژی از روسیه انتقاد کرد و گفت این تصمیم تنها چند هفته پس از امضای قانونی رئیس‌جمهور برای اعمال تحریم علیه خریداران سوخت روسیه گرفته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/467407" target="_blank">📅 04:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467406">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAAuZfh_jld9X1LbtGNHSAabhEXmS--XL-vSW2wkXEhyZDItbcCApR0bb0W22J83K6lP8Nkrfe9qBC51zJbddxVFjPftdXjoAcMPrKBON3cEtH2RA9Z7L2gLbwkDYkP87xhnwWYoBK1_WbTn2iATOsyH_-2s5sPlhYTNlO65sziYFSWcz3dMLMd0YA9N_NJU_Zmb_w6Y1i45V9eRaArOaD5wnkWJMHabhtBI4gHchOvNWU4Qvu-ykp43Q7VDTnd_-3v2CZ2Le52YRnVrH4pNJ95g3JX50MFuVPE2lGzWUOElSld2fQlJHi9H8MdiARj9Hy5MjiTl-K4KIKbw5etYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی کودکان حرف‌هایشان را قورت می‌دهند
🔹
بزرگ‌ترها میان کار، مسئولیت و دغدغه‌های روزمره در رفت‌وآمدند و کودکان گاهی تنها چند دقیقه توجه می‌خواهند. برای آن‌ها، شنیده شدن لزوماً به معنای حل شدن همه مشکلات‌شان نیست؛ گاهی همین که پدر یا مادر گوشی تلفن همراه را کنار بگذارد، روبه‌رویش بنشیند و اجازه دهد حرفش را تا انتها بزند، می‌تواند احساس امنیت و تعلق را در او تقویت کند.
از یک فنجان چای تا شکل‌گیری اعتمادبه‌نفس
🔹
گفت‌وگو با کودک لزوماً از پرسش‌های جدی درباره آینده، درس و موفقیت آغاز نمی‌شود. ممکن است از همان لحظه‌ای شروع شود که کودک به خانه برمی‌گردد و می‌خواهد ماجرای کوچکی را تعریف کند؛ ماجرایی که از نگاه بزرگ‌ترها چندان مهم نیست، اما برای خود او معنای ویژه‌ای دارد.
خانه کجاست؟
🔹
خانه جایی است که کودک باید بتواند سؤال کند، از نگرانی‌هایش بگوید، اشتباه کند و بی‌آنکه از تحقیر یا نادیده گرفته شدن بترسد، احساساتش را بیان کند.
🖼
چنین رابطه‌ای می‌تواند به والدین هم در امری مهم کمک کند؛ نشانه‌هایی را برای پدر و مادر روشن کند که ممکن است در شلوغی زندگی روزمره به چشم نیایند.
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/467406" target="_blank">📅 04:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467405">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wg8-oebYWG0tQO4se0m0QzCRj62Yc9GqfYpAO-xfUXeWOpiF5wvWGbIj8Od8yIKzeitKIW_H2wi00HVkZUYDqBukmgo80DcEc7Nkc4D-xY3KrF1rjem2gbWThVavZ72XE8Ks0bB37YaFofyNbVrQ8706A0Wg8c9vY9bxkgjQYZu1t6hMJYSYcusPdZgJnCQF1bDe1AIS1YgXswURxqHudbE9Of4n5G4gg-jGlwON3AE6PxQnkfXVb-3gnsAZ8JgtHTGs8V3mPqZTph71FtwpbVAJot8RdWS7Yz-gJPSGN3ndBDhLtcamRYaniBiWh8ICRjEf-6pZdUXPDYbYJM_MfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به مخفی‌شدنش در کامیون حمل غذا واکنش نشان داد
🔹
ترامپ دربارۀ واکنش‌های کاربران فضای مجازی به مخفی‌شدن او در کامیون حمل غذا در فرودگاه و تغییر هواپیما از ترس تهدید ایران، گفت: این موضوع مربوط به سرویس مخفی است. من فقط از دستورالعمل‌های آن‌ها پیروی می‌کنم.…</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/467405" target="_blank">📅 03:39 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467404">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45298b396a.mp4?token=WhKbRoydpVK1YF_wDVgNRYsJ5UWbepxHbWh5JUlVzWNeYQFA05xX-tggbKIC8tt4op30-6UtrqX1DYgqzmG59mAbODotRtGj4R1PlA8pANe3FcnBNxcFyf75PCmkbCD_SDHIB2A6GKBMS45tf_5_L_KU-bdWMFTDuOKUqQrsSVWvEe8_-mR5N4PNm2HSsKLn8LmS0UMbdkDLT0gnYQeTNlnAhyzO_d4-gYOGUxTTQ7R3MF7W6JGZYw6WmLGdlMWEW7WGn8PKwJwBjpRU15grFfvnqyHiK8yt_hAaN3L8ys-Ch_a_zyRKbvHQ420fBBOC1WPOTmflgJ1AtvoHpO1NhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45298b396a.mp4?token=WhKbRoydpVK1YF_wDVgNRYsJ5UWbepxHbWh5JUlVzWNeYQFA05xX-tggbKIC8tt4op30-6UtrqX1DYgqzmG59mAbODotRtGj4R1PlA8pANe3FcnBNxcFyf75PCmkbCD_SDHIB2A6GKBMS45tf_5_L_KU-bdWMFTDuOKUqQrsSVWvEe8_-mR5N4PNm2HSsKLn8LmS0UMbdkDLT0gnYQeTNlnAhyzO_d4-gYOGUxTTQ7R3MF7W6JGZYw6WmLGdlMWEW7WGn8PKwJwBjpRU15grFfvnqyHiK8yt_hAaN3L8ys-Ch_a_zyRKbvHQ420fBBOC1WPOTmflgJ1AtvoHpO1NhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مقدمهٔ
هر راحتی یک سختی است
🎙
شهید زین‌الدین
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/467404" target="_blank">📅 03:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467403">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رسانه‌های عراقی از حملهٔ تروریستی عناصر داعش به یک ایستگاه امنیتی در استان کرکوک عراق خبر می‌دهند.
🔹
گزارش این منابع از هلاکت و محاصرهٔ مهاجمین تروریست داعشی توسط نیروهای حشد شعبی و پلیس عراق حکایت دارد.
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/467403" target="_blank">📅 02:56 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467402">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انتقاد اوکراین از توافق ترامپ با روسیه بر سر گازوئیل
🔸
رئیس‌جمهور و وزیر خارجهٔ اوکراین از توافق ترامپ با مسکو برای عرضهٔ نفت و گازوئیل روسیه به بازارهای جهانی انرژی انتقاد کردند.
🔹
وزیر خارجه اوکراین با انتقاد از کاهش تحریم‌ها علیه روسیه گفت این اقدام نه…</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/467402" target="_blank">📅 02:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467401">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HUnIm89IOfpzcFBUnAt358lVlj0vdAHondSyTBunFIyp12bLy1jeTqYWDrEJKQfdvk1SjdtTA-nkv7gcJTpm2qneTydsD-SCc_VMG47PywswKEUPxZYLK32nh_uvnLz3jR7UDjut7-725LJrwX46OeTlvW2fchKKJtCtR4KoeCmIJqqrVgOy22IDANr5QuXli0NOfQ_lEn9Qrh9OhPRlYL-wbTzJtpH08zCgXwBbtJCA9a4rhcuk5lwICnjQhWI4BdTVcTgcZwrN6YEpW2dg8pNgh44Xzpc6myiIch6i57u9lPk4cFYynmncCEqVmifdB0wXo7Pj0wqPPt5hNeY99g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک به فضا ارزان‌تر از اجارهٔ یک نفتکش
!
🔹
اگر بخواهید یک نفتکش را برای سفر از آمریکا به چین اجاره کنید، اکنون باید بیشتر از هزینهٔ پرتاب یک موشک به فضا پول بپردازید.
🔹
گیبسون که یک شرکت کارگزاری کشتی فعال در زمینهٔ حمل‌ونقل دریایی است گفته هزینهٔ چنین سفری اکنون حدود ۸۰ میلیون دلار است، در حالی که طبق محاسبات پرتاب یک موشک فالکون ۹ شرکت اسپیس‌ایکس، در حالت معمول ۷۴ میلیون دلار هزینه دارد.
🔹
همین مبلغ در اوایل سال جاری میلادی برای خرید کامل یک نفتکش تقریباً مشابه کافی بود.
🔸
فعالان بازار نفت دراین‌باره می‌گویند تولیدکنندگان خاورمیانه ناچار شده‌اند نفت را از طریق تنگهٔ هرمز منتقل و سپس آن را به کشتی‌های دیگری انتقال دهند. این جابه‌جایی‌ها گاهی حدود یک هفته به زمان هر سفر اضافه می‌کند و بخش بزرگی از ناوگان جهانی نفتکش‌ها را برای مدت طولانی‌تری درگیر نگه می‌دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/467401" target="_blank">📅 02:00 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467400">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">زلزلهٔ قدرتمند ۷.۷ ریشتری پاناما را لرزاند
🔹
زمین‌لرزه‌ای به بزرگی ۷.۷ ریشتر روز جمعه جنوب پاناما را لرزاند و به خانه‌ها خسارت وارد کرد، برق مناطقی را قطع کرد و موجب توقف پروازها شد.
🔹
به گزارش رویترز، این زمین‌لرزه ساکنان را به خیابان‌ها کشاند و بیش از ۱۲ پس‌لرزه نیز پس از آن ثبت شد.
🔹
تاکنون، جزئیات بیشتری دربارهٔ شمار احتمالی کشته‌ها و زخمی‌ها یا میزان دقیق خسارات اعلام نشده است.
🔹
رویترز همچنین از صدور هشدار سونامی خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/467400" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467399">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/467399" target="_blank">📅 01:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hh2-saj57bzxO4MtsZD_KfM1_TIJVzCPLpYAGRHIMrFHRSzUItP_IaSQx7I1ZfzfJAUv-XpFQ3pWvePxfQ0T8urY2DL5sM5c9OWfICHTUJRnJA5Tr6p4E9CBVOzxus0UZhDHm_wK_bjKcZCOw14f0rnjHdMk3NS0B68ZG_-HoskIboo-w_bDWdhDD1qQj1_lT4ZvKvhdakmLFTdgHWFNQbnEgKEiFxyIIurDpbUiNR6x6xrUib0icq1Q4p8ku2EdKgv3dqBL4_jXJXqQiwKl2C6b-rZNxZRLocPy_rFnyT4GpuVuTLdkreUzyhli1LZdF55SQl5zZVBp3GsUpfOC8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصادف زنجیره‌ای در محور دامغان-سمنان با ۱۹ مصدوم و یک فوتی
🔹
این حادثه در فاصلهٔ ۳۰ کیلومتری سمنان رخ داد و در جریان آن، سه دستگاه خودروی سواری و ۲ دستگاه خودروی سنگین به‌صورت زنجیره‌ای با یکدیگر برخورد کردند.
🔹
طبق گزارشات اولیه، متاسفانه یک نفر در صحنهٔ تصادف جان خود را از دست داده، و ۱۹ مصدوم جهت ادامهٔ سیر درمان به بیمارستان کوثر سمنان منتقل شده‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/467398" target="_blank">📅 01:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BOfXz2-yk633aZG0eYZ5mqy0kCkwVBgZzytP8_oe3ArOg8mjobuoc23Da2kRUlBLZ-lGr8LdCFq_KWFObCAel61NIg9GsWn_Ah0XaOruhEnbM3j5bw_KgCPPPygUkPTSYO62pEEgvWh1UY2NIzI2-t3lmEVFi7uwTKzPNlwfRd7wHm6j2De18VCyuD5A3RHqtF9_H0cr8HN1N9ox5Fw80gUbPiGIqxWblo5PuLPdgUSRBxVTDBSsU18WrTvF4QLWflSsBUmVb6aE48EDWq4ROyT-eppqOWkBv-h5QhaOv-bflKlXQXXkIDuy3cYrS-5MVNvWQNzizQYuyiLgjocdBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش اپراتور فرانسوی از اختلال گستردهٔ اینترنت
🔹
در ادامهٔ اعتراضات فرانسه، گزارش تازهٔ اپراتورهای تلفن‌همراه از قطع خدمات تماس، پیامک و اینترنت همراه در تعدادی از سایت‌های مخابراتی فعال، به‌دلیل خرابی یا عملیات تعمیر و نگهداری خبر می‌دهد.
🔹
گفتنی است در روزهای گذشته، فرانسه شاهد اعتراضات گسترده‌ای بوده است که در پی آن، وضعیت امنیتی و تحولات داخلی این کشور مورد توجه قرار گرفته است.
🖼
در تصویر، سایت‌های دچار قطعی خدمات، اختلال شبکه و تعمیرات برنامه‌ریزی‌شده مشخص است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/467397" target="_blank">📅 01:04 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E74hAaoJ4bVh_g8-b_Gl92DLzkB30NUcu-f3IctPVNHFvd90vcyavsFsHo9r4rwwziyaKx6Nq7jduLoSw1sojrq9q4jeEeNsfI22O-xQaCG_Kto9dUSOVemQb2n0IwmO13pCf2GcR7431QiNgoe4ElsW-YdMDdzhsqG0jX3rQgjt4b3rFTBBwzsxGRx1cgYNmKzCTzMsAeewtngCPivWbJAXu4iH-cb2OAHROFfWfxzVowmZ3SG3bC8NhtBpAWA-ViRMWk5RcILB2Sf8wA6a2I6Y6TXTetYtYZS23sdDrM-3GPU7-R2aFLVbLLHaea9nGWhJJH66ei5e33ZZHkBc2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ پوتین و ترامپ گفت‌وگو کردند
🔹
به‌دنبال انتشار اخباری دربارهٔ توافق میان مسکو و واشنگتن برای عرضهٔ گازوئیل و فرآورده‌های نفتی روسیه به بازارهای جهانی، کاخ کرملین از تماس تلفنی میان روسای جمهور این کشور و آمریکا خبر داد.
🔹
الجزیره گزارش داد، براساس بیانیهٔ…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/467396" target="_blank">📅 00:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">پوتین برای عرضهٔ گازوئیل به بازارهای آمریکا اعلام آمادگی کرد
🔹
رئیس‌جمهور روسیه: مسکو آمادگی خودش برای عرضه فراورده‌های نفتی به بازارهای آمریکا و کل جهان اعلام می‌دارد.
🔹
ورود نفت روسیه به بازارهای آمریکا دلالت‌های مثبتی برای اقتصاد جهان خواهد داشت.  @Farsna</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/467395" target="_blank">📅 00:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">حضور بیرانوند در محل تمرین تراکتور پس از شب جنجالی یادگار
🔹
پس از صحبت‌های شب گذشته علیرضا بیرانوند علیه مدیریت تراکتور، این باشگاه با تصمیم جواد نکونام، دروازه‌بان خود را از تمرینات کنار گذاشته تا روز دوشنبه جلسه کمیته انضباطی بیرانوند تشکیل شود.
🔹
با این…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/467394" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467393">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5452qjJzYxcHmuawB2Mvs5jgG3peMRT7mSV0Pzjtg9_0-unA7HRzScRAJe5yCZhmkhz_EP4k33yz49gqzDcxfRS2rMvmekCV8QF5EiqQokBAPIhhatPq98v6emEz2Jb7YKomBRjEmpQuWa31HONqAKOgkaIiFESGB_cMqbt1o4T3forUivlRSJdsphLU3q-6wO23zgqs_4jslhruq6TVA40IkMkdLZzKNMJmHak8a3g0XCPfB--4XFeE4ROT7x5TE2wvoHKnQlqSDn2xDxuRWw31cMBm49yzVIF2D8TTINxJTnqjM_E28zltCXEmZLzT1s69_C0tlxItZphzUTnaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرانوند ممنوع‌الخروج شد
🔹
سازمان نظام‌وظیفه اعلام کرد تا زمان مشخص‌شدن وضعیت کمیسیون پزشکی علیرضا بیرانوند، او حق خروج از کشور را ندارد.
🔹
براین اساس، حتی اگر این دروازه‌بان با مدیران باشگاه به اختلاف نمی‌خورد، بازهم نمی‌توانست تیم را در سفر به مسقط برای بازی با الشمال همراهی کند؛ مگر آنکه مشکل خروج از کشورش را حل می‌کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/467393" target="_blank">📅 00:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467392">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7f_4NmoEt_mGth9ZuTspJJrWGqKTYyw6gd-KH8HSwLGsaIWT2O6un6QFsEiQauUBbPu6s4Dfeus9bRwQMS9I-j3rgVzwVkgd1IzAkhp1Czfh0D3ONVd7BtDWwXoODnUx4WIznx3Y8tmNxr7HRobB59cuEdLl9cupcOKH_NaL1wj9V-Bw9yvNlFZWXSUHtn8WfOGEk19lT5ymTD6w8Ad7XQksl6s1WKMMEAQ9D86WRJO0gplWEldMiV89dg9UfsLeCtllXJfiXA_YpK2MDgRE7tF4w19VBjbdBwNMqognOvuldw8mUCz4wgFnS_17pz2f8XBPcqHHNpFJzZ1buQJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس را بدون اختلال دنبال کنید
🔸
به‌دلیل محدودیت‌های ناشی از تحریم‌های آمریکا و عدم ارائهٔ برخی خدمات زیرساختی به خبرگزاری فارس، دسترسی به وب‌سایت فارس برای برخی کاربران با اختلال مواجه شده است.
🔸
برای دسترسی پایدار به اخبار فارس، آخرین نسخهٔ اپلیکیشن فارس را
به‌صورت مستقیم
یا از
کافه‌بازار
و
مایکت
دانلود کنید.
@Farsna</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/467392" target="_blank">📅 00:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEDrL-doas47UTxMr0Tsfs-3lV42eYrpFLIOqbw962_REpCn9eEuDJT8z_FKgmHzP0JJA8FGpiFD7H1rqJ38KEQowmRsL0ibvI0dqR-59yhyHMrrzYF2KsoY1JRoiwZaCzX2TZuFA_Mm40wGHnna1-3lPqhLoZzppsBA_yh5ZmzAa_huyNb7rAYrOQWluuF3vD8Ql8sedNmXwzE6qls2of1WLiQj4YiML2BQ7c1bIy_EC8_OF0kDbNiICFkWUITUeX2QyjVctyCI68BzlOwN3IUL640ZdEy2U6HZakKrBGCyI8HjFVaEsWdV0K7OlUtW3AvuJE17seVIyBAJQiqbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زلنسکی: اجازه‌دادن به روسیه برای فروش فرآورده‌های نفتی به‌منزلهٔ سرمایه‌گذاری در جنگ علیه اوکراین است.‌  @Farsna</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/467391" target="_blank">📅 23:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24e30c480.mp4?token=QVFW8b--22wo9emVSN4i5YHUQFd2f8dQmVpz6X3WQBAJFXOBEUU-GOVMeP2ev0GayfWPjj2Too2Q7yd3sY19jzT-oEJhx9l9L5Yn2wWee6ZaS-WW8HVXowwqgvdIgeVyie4rbFQ5M41N4pXXp0eyCEWyvM0ff3u0bBEEUU-79J1chAjbyoRULkGsD2rRxq-1HAGhJqygZONBdcg5lYWxKRnHXll-RvVfTREYaL_SmeW4bkySDc3LBYwd1zl9yhWt-PJXXL7RWKhX73-xYcoaVcnMPIMraGz1tJiHL374pHvj3ehSAKbmACPO9rthLDPQSlWCO_RuGHjg1fN7lfM5jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24e30c480.mp4?token=QVFW8b--22wo9emVSN4i5YHUQFd2f8dQmVpz6X3WQBAJFXOBEUU-GOVMeP2ev0GayfWPjj2Too2Q7yd3sY19jzT-oEJhx9l9L5Yn2wWee6ZaS-WW8HVXowwqgvdIgeVyie4rbFQ5M41N4pXXp0eyCEWyvM0ff3u0bBEEUU-79J1chAjbyoRULkGsD2rRxq-1HAGhJqygZONBdcg5lYWxKRnHXll-RvVfTREYaL_SmeW4bkySDc3LBYwd1zl9yhWt-PJXXL7RWKhX73-xYcoaVcnMPIMraGz1tJiHL374pHvj3ehSAKbmACPO9rthLDPQSlWCO_RuGHjg1fN7lfM5jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بیانات رهبر شهید انقلاب دربارۀ نقش مردم در قدرت رزمی کشور و خطای دشمن دربارۀ قدرت نظامی ایران
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/467390" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c107f3d38.mp4?token=EWRYY1EkRe32pFUKyGt3_HH_75OHOALk9q-oKQ3nMNYAO4KW3daK4AoUHD1BQLksM4tzJkvNu6zqYgMfjbIHqxLGsQj6puQ-In_KEpIlBCZMRX4-cLP5TEAffr4gYLrsz4J0HiQioStuktP5Pb7459mK4S8hQ-mf9Tj6XYBMsbQ1J0m6i0BBzbmpLMO_rhtgu1ndt1LN9f1fjK1DnkphVHrmIBW0eVjJUA61DXkWUU1JP7TOEfmo45TG2Y9m2oY2MmmGEGm9lAXNPBpfYXv6_48QL-nQ0-NWO1rDC_klyQI7JOsdaEQL8qWLcfWcnkpbOfH1cTwYyC9Jygq1f8DXGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c107f3d38.mp4?token=EWRYY1EkRe32pFUKyGt3_HH_75OHOALk9q-oKQ3nMNYAO4KW3daK4AoUHD1BQLksM4tzJkvNu6zqYgMfjbIHqxLGsQj6puQ-In_KEpIlBCZMRX4-cLP5TEAffr4gYLrsz4J0HiQioStuktP5Pb7459mK4S8hQ-mf9Tj6XYBMsbQ1J0m6i0BBzbmpLMO_rhtgu1ndt1LN9f1fjK1DnkphVHrmIBW0eVjJUA61DXkWUU1JP7TOEfmo45TG2Y9m2oY2MmmGEGm9lAXNPBpfYXv6_48QL-nQ0-NWO1rDC_klyQI7JOsdaEQL8qWLcfWcnkpbOfH1cTwYyC9Jygq1f8DXGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تشرف اعضای تیم ملی کشتی آزاد و فرنگی به حرم امام رضا(ع)
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/467389" target="_blank">📅 23:57 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/984e3a9a47.mp4?token=vaaiBVegMEOm004hblec-4huLuts6dDyFFeMURdmxWC0VR3-jsZ1PmupmlEXPogy4g0EWP6tg_sJpzBk1rBVTcFipVua5dUWxiFWdZaGjqMgTUWQQI61tfSRAFaFYRP-ThE28bCd5gaoppAS4x6LtSPtlfOWUBTBkvYh_DKz7tC-1bO3ZO3G1nM5Si9ef1EJndOOl2pcQxtkht6pXI25oWcoCm7KO2UHMRSDnpRf3cfcC0S_8H7o80nn0G7pb4z5HMhzhpipoPwAu4ujUFMAtTiZvJpFpwsFZZpHlaoXjHf6GYXm9wSp1Wq7nZp-Ctb44Imfk5n16f76Vm3blx47GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/984e3a9a47.mp4?token=vaaiBVegMEOm004hblec-4huLuts6dDyFFeMURdmxWC0VR3-jsZ1PmupmlEXPogy4g0EWP6tg_sJpzBk1rBVTcFipVua5dUWxiFWdZaGjqMgTUWQQI61tfSRAFaFYRP-ThE28bCd5gaoppAS4x6LtSPtlfOWUBTBkvYh_DKz7tC-1bO3ZO3G1nM5Si9ef1EJndOOl2pcQxtkht6pXI25oWcoCm7KO2UHMRSDnpRf3cfcC0S_8H7o80nn0G7pb4z5HMhzhpipoPwAu4ujUFMAtTiZvJpFpwsFZZpHlaoXjHf6GYXm9wSp1Wq7nZp-Ctb44Imfk5n16f76Vm3blx47GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم فاروج خراسان‌شمالی سنگر خیابان را در شب ۲۲۳ هم ترک نکردند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/467388" target="_blank">📅 23:53 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467381">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAuNN9SygSVSpwRgClG3mvaDPmYiWUaMRmRCc54yBkC0WLXg3Av2KMnRVbg7xjRkvekxm7OxeEpbQ_ozhYkrREssJXzv4MDyMAcgPmD82OgUt0Z-CCfyeiafJOJPAfO37hmfCi4K8jwPKtvK9DlWCaJgLKKiiJRiuD5bWtRAZ3B5vRT_ZQELvSuMD2Q1X47Oa4SUbd4-gQiEbkrin_QdD9aJIwulV1ZMyuDY0Z2RPfwa_IoF5wCEE0gDq-rigaj3fzPkS6jpjGv4c2_Nxk9_3u1lSwKxXjwXg2Sr4hEFCeoldilsAQU4dhrkNGJSfW_7kwa2qNWWqERsMXU1COcjQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V-8ihuj7p1ilMKf2MPGtyv6xSoWG7E23maytvI3u2GQK7g8zozh3Sm-wWN2sroBKsXEKFrg1x7kQLKXnwEb1-ZFN8uVBSfT6Q2IJ54z2FOeqVjHfevxMzMQKydbS_pAqtOktiFmPSRUWaG2XrXOvgythGtAwFIaNjULb1YSJzmYN8Myx3ie_YHJHGFlxw_J8FItsZCuLPat6qqanslIqq_D_B-XV3j-Q2CknyTfR4Hy0NLc-uQCqvvVYu0juZyZTQvJnaNUfF0PPi4nQhUpbvEHgy6d70_qToAoRXTPN3YUH5i2Yh0H-jvMYpFsClCKTC2SkvICYxXEarqNUlq9rUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EK3BR6a2roDEm8DKqClaWetuTh-IJR3ZoFvT3BlSO6qV5OFcnpyxk_2ItlOKylNsMEvEFmZO6_V74ZeiQ9B56LwIxhPi83dDWefzKepVcNZ9bibOKYlq6enaVDZpguzR3cXDLNRCyus9hH9sfbPRVfOe85Rr3fvS6adndulMqkhs-PNsPXJzZsO1pNLtioXaejZY8966tIHQVGamrNskYbmHUWARyeqHrrMBNnU-fAQHN9UPTLo4Pw591Pt2m5_n-DlyCpmPhkDzeTfaKQjhfFHSYPEfIFAHQcNC_qeaxGhm8YGMzR0VY0JGgspSdh_50GsZlMx7D5YvNIuABTyeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eH4C-07mtYu8052zgZ_gnWOmb_OSMvToQlKeYLeMFNHkiff1NAHwbLkqxsKQnKTZOyIgdZ7XqhU3gcohXL_eHjKXzu08Zg3CQayd95DGxmM07P3FbHNBZGwqzQ2iGmCC_4NcsYgMpXL_2r8Xb_xMND4u3EJzsB2PnfX_wTAQL7Gk-r5Re6yLSZHn29pWdoISDowuIq-Hv5dA7iMjWtoF2AlH82e4bhAqmmCBVFXgNwzweZCRw-RYUcW252SNGZbMJulvFXGw6DJ5DDQLbBm4sa-X19ENJ_x2oYK4ESt1MwVsFBgbN23vUnMQjEpoiYe888iqn3aMT4FS-Im1KhqLvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W_sFsQqmKEGT8innfA2ACa4cZlxUXURj6XZuuLU-v4u6BM939dQskZFGwPavLfJ7SX4PiJ6R-1uqzQMbtUjOPFxj56gy5xi_uRA114vre86a5TWd-Ncm39fPRPgYpUEp7DLDWO6MsZCJ326XtUZGCI6SBDI2ul5Ideas92vFYg36QECLrfCRCspr3UjW2MeHORrS-fOUua3hELCcS0prDve27a91OMG0b_HfG-28otIqsZsD8PWkHv39P5WRlYKw7GOA5y9_agI4WecK5OC_5dxfNQ2pf6hW8DL96_9gsCwlb2Jt1rHmhK92q2pVwLmL0qLHUaha3QHFUnlaH0A1-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dI3wSg2qCmCbyvFGazSpG4KJ-Ji41ogIdKjsP6kb7qe4hQDPlDDD9osOBC0mysmIzPTZMia8IomMFlKkd_WSsBMzDiAg0Tul1Kd6LpDnfR90f5Ab6vFn_PhUDFR-TaC-oAfuAQEh0HfgDv7SlliK3OE8XDHX0y_X_UtRVO2eEfA3-YefeJgYgGWBtsbovpWICLxjUKaXLDtg7RCSAtGuRqrogy6DVLZICMxLUAT4cWaf4N4eh7p1ULCs37TbBhFJ7-GHt8f12tkUMCNOsCyP-lMyZdxf6OrkYItOllXd5yc9Y1y8oEd2HIWMggMj5owbnQ4ylnsCNtMWWD5iMBKo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MLbIUB8B4sI5f5j_8QN1gsmSfRcqQGHxJSShoDK3u4T7r-pklP5QZK-xNv_kmhoww-x7Qw93hFCp5EiG_T0sL7YSHyNmiT_YDIluAU1g1Wp00SEHoid9-RlnN_WijLXBTWPxn7uWUyE9dErYzxP9TLn037U72hSk0qRDHRU8Nkf2-EHMP4v_Wt-p84CsTrth7VviU-fEH89Vt_Rw2xUq7OmysArrtNdwum-qutROdC7farYJ2ixbgEZWwsO8WtW5rFBPbXuMFKvyoN3a_qFiWyJFJYnL2tj5HVe9pjONX9Y59sERTrcGWj-4PWrp7Ka7wznSAaO8z1J8nfjwOZbi_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
گل سوم برای پرسپولیس؛ اورونوف در دقیقه ۸۵ اولین گل فصلش را زد
⚽️
پرسپولیس ۳ - ۱ صنعت‌نفت @Farsna</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farsna/467381" target="_blank">📅 23:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467380">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvX8w6TkHano7gxIb8Hb9ZxJYS-eru276RSpkMXWcMyWh4UbNd9gmtBs33YL2qmf6Z2yYSLTT9qDrUJonaUd3rxwE5E_tRPI6487F4vqmq194sijE2OFnJY2RI6E9HBvBtWTs_cBeLk4csRoLoIOydlyCn4P6w9isjKSAcP9y6bQbQNnGUV57XF1JAeqkSjYnBowMeUBxCs_SGqBMc5UnNQNnzNNWiMOsSuV4BQ5BmOPmJu_G_cJj3AuUmFmWLtzBFkYLjd3jqtXmLQo-x8jRq7z_QdAnUxVn1xSgh97hx1AHNnLbPqHryw2CK9gMg45UVPR5h_Rm6-7VBGqMZlteg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کابوس ترامپ به کف ۴۴ ساله رسید
🔹
ذخایر راهبردی نفت آمریکا در تازه‌ترین آمار رسمی به حدود ۲۸۳ میلیون بشکه رسیده که از پایین‌ترین مقادیر ثبت‌شده در بیش از چهار دهه اخیر به شمار می‌رود.
🔹
بر اساس داده‌های اداره اطلاعات انرژی آمریکا، ذخایر راهبردی این کشور در هفته گذشته با کاهش حدود ۷۸۴ هزار بشکه‌ای به ۲۸۲.۹۸ میلیون بشکه رسید.
🔹
این رقم در مقایسه با سطح حدود ۴۰۶ میلیون بشکه‌ای در مدت مشابه سال گذشته، افت قابل‌توجهی را نشان می‌دهد.
🔸
کاهش ذخایر در شرایطی ادامه دارد که دولت آمریکا با فشارهای ناشی از اختلال در عرضه جهانی انرژی و نوسانات قیمت نفت روبه‌رو است و ترامپ با انتخابات میان‌دوره‌ای آمریکا و نیاز به رای مواجه است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/467380" target="_blank">📅 23:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iU1FYdDR0HnDzxspkfLeY2rYoB0meUISLf3HYZXmCx61psYsZNgXiTewu2IQXweBtVb408UHlE71BtZhnIwu5ZnUE1Mn-vWR1gfnqsm5LXBrJBH2Qg9WDBm23e4gEu-Yrl6Vw2Dfptfquo9i_hCkHVIB6HWAc4rjb1zG2wHzeGrAN_qBWDY-iQfpd88MfUE2iQzyfZbGj3SFuPR9a8eGinQpDKPSHKXAOvpAXwn9XAqa31tq_fJ9Dy1IODqGEcL6Cksbn4aKTfPwb8XQ0NpNsp9A_fTJwnF3ppFoqCiKUSlga13gSI5NKEORD4JO30GFwmWdrgwCJhjtuEFBngpcrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ توافق با روسیه برای تأمین گازوئیل
🔹
رئیس‌جمهور آمریکا مدعی شد با پوتین توافق کرده تا مسکو بیش از ۳۰۰ هزار تن سوخت گازوئیل در اختیار آمریکا و بازارهای جهانی قرار دهد.  @Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/467379" target="_blank">📅 23:25 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467377">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a40913d7f.mp4?token=VCApqXnDbhRlI6-9SsFinTD1KBRyOS4zqvKVnypzK3iCp3G5UMmtQoTsdbtsfKcSYIxpcA74h5sOn27tPbczRP6f1-sKPKtJIuZZ-8EpfikL7MdZQBIRRt8UFoMgW9mUOvZe8GSjgHitFCGKbyr-CjhFUH77U00iXznavud8Sm2-P0ecCtJWzr7DaRXvreobKdJ7wk2_msr_SdE_iX90OvczHWTIFb0ylvH-hkp4-tfl1YA4wY1o7SdBwdeL2SvcLQAN7He9ozzftjIllVXRkJJBc4lcBxSf81jmLLZ4wvACDGnWrdf8c9OT1GhiAO1IxnJl1Afm3p1EUs2wx-WzIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a40913d7f.mp4?token=VCApqXnDbhRlI6-9SsFinTD1KBRyOS4zqvKVnypzK3iCp3G5UMmtQoTsdbtsfKcSYIxpcA74h5sOn27tPbczRP6f1-sKPKtJIuZZ-8EpfikL7MdZQBIRRt8UFoMgW9mUOvZe8GSjgHitFCGKbyr-CjhFUH77U00iXznavud8Sm2-P0ecCtJWzr7DaRXvreobKdJ7wk2_msr_SdE_iX90OvczHWTIFb0ylvH-hkp4-tfl1YA4wY1o7SdBwdeL2SvcLQAN7He9ozzftjIllVXRkJJBc4lcBxSf81jmLLZ4wvACDGnWrdf8c9OT1GhiAO1IxnJl1Afm3p1EUs2wx-WzIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تاج: یحیی گل‌محمدی به تیم ملی امید نزدیک است
@Sportfars</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467377" target="_blank">📅 23:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467376">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FBMSHrQyfWHor9AOaNbi95GE1Ww9Ql2iiHFKa-81qYLp2YSYc3_Tg89et5Zh-b8xIh5akyWPJ1JXQU-04-YfQFObOAU7RZuCiW1Y-wKHHjN3AHwIZLRIa29Ff_VBEJGebiy56_Df8isZT53txZqYssSvYRzlUgA75phn7CKuZ4Nx0ZEKvtLCGMzyzBHdBzS_vhzqURhOsL2UROz7nLCbOoyA20vGjsQjQjCxH_wq3wOJf119Hk9xn8IRYvz9vHf1CsT2rRUYkVcpA_-ZNksQq8JXGmeTnD-xkUyn00i8G7rLM0h3DoZoGrsWxll9T8moT57qPqIhNJ9ayKDWdTz04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه نهاد آبراه خلیح فارس در مورد وجود دامنه‌های جعلی
🔹
نهاد مدیریت آبراه خلیج فارس: با توجه به برخی گزارش‌ها مبنی بر سوءاستفاده با دامنه‌های جعلی، تاکید می‌شود کلیه مکاتبات پی‌جی‌اس‌ای از طریق ایمیل و با دامنه
PGSA.ir
صورت می‌گیرد و سایر دامنه‌ها فاقد اعتبار است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/467376" target="_blank">📅 23:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467375">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ls4BHMF2hEnbehwuCB59M7CSjec5Z5kIzqD834pFufTqCzkFuOkdb9EinuIPIVJfeca9LlonUwenQWk-w65VQ-Kemi0CiCImIIQx79ufEkpgWZBLSPqVqZxDN08UAd-LMYJwJ8WoRndleV-eQTse9AXxu7sKv8srWOt1_t4Sp04Uy0O8naKpiJoF6QmP4kqmdklUSbx3yfA_pcHf0GgCL3aVS1yNvlY5alX2-Fp7VnLfy7XRVT1vY504u5t3XKjvutZhfr7McWDofJEVi7venfI7VkucTk1C7w8CmkpkVDBuS8_uDUnjvugCfIzhpzHwt5vGu_CZndM4JVSN4yzOCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: کشتی غول پیکر حامل گاز ال پی جی مورد اصابت قرار گرفت و دچار آتش سوزی شد/ مسئولیت تنش افزایی در حمل و نقل دریایی منطقه بر عهده ارتش متجاوز آمریکاست
🔹
نیروی دریایی سپاه: ۲۲۰ شب حماسه حضور میلیونی و ایستادگی و پایمردی شما در دفاع از حق و عدالت دنیا را به…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/467375" target="_blank">📅 23:11 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467374">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxHXtYNWryxVRQHvlnzfkhJp8TAYOkaIMSFgRDjyAFg8sYrA5nRiFU4_jLmiMHkq03kpQcLKZXwl1FkC8TJ5DBg7mImDmopW0QgdpY2eyH85XYQA7bVL9c3GFPuDOhronT6qowgyrIGeHJkbBNU-30t-SOH9ZHsSlMiu76dZMqmjDi9_ksW4QBw84xhWD1Ug-0UViEsTgjAyAstAVxRG-0fcIG2jslvBUVxkZrE92ZZ977M1H8ZWihRQadNTV1fAcqBMMFnYxTyPHXrUyw0RXui1K6bZZ5_hjKE1ccd5gCSW61lRIoT_OWbwvh1KEiLrZXFScJo8i1qmfh5rYbCyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
مسیر فرار نفت عربستان از هرمز در آتش سوخت
🔹
تصاویر ماهواره‌ای جدید یک ایستگاه پمپاژ متعلق به خط لولهٔ راهبردی عربستان سعودی موسوم به «شرق–غرب» را نشان می‌دهد که درپی حملهٔ پنجشنبهٔ گذشتهٔ یمن، به‌شدت آسیب دیده است.
🔸
این خط لوله حدود ۱۲۰۰ کیلومتر طول دارد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/467374" target="_blank">📅 23:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467373">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2407f2c6f.mp4?token=O4FWpIhRoPOWmIDKUI1TZ572lmwrCBeQoe_w_2uKLwds-H5SV5H6ce0Lp-EjDOIiP5aVeopJ6NcuHlHdyiJhANBscpOjaJ3FF6iyPE5NEmc97n7DBb-jn5YtgboqRjDGAJYSNxYEDXiYWW6DO9xs2lx902dtfhrxQkKFizxrd3wztVm8xlOXy2GGdybUl9x5tOiXGXpJN9R6IFfvYidSKq6zqWvPVUpuTv_KtbWuMItB3RG22LYb9pPcB4Y6QWt_ACqIIIZNJ4k-ZF3SNmVYk8ap1U_MMGUafmgsznIzHako_bLTAkUIY2ey_gN1wDtd_G8zfg5khFzqjELK0nCjD7UuDfR2Ijt_vfyQr41-tB84-BZV5g-CGPlyAXhDELmQzLk4Hy9aLAuLJC5oKE0RoXaqdCYn4r2SYj37-Zp54fb64Vff-nTEPt7lJnzqH5yJXkLeknne60fB3yz0uKhu_23LFASETc7YAZVKh4ELHwpNlvt5J7CsEjIcvk68SM2e6Pa-PaY0rsLpSEXc6dakGcb9auEGZETXCoE7HUrIq2AH_YdEkpHRHob7lq5dLDWxIh-RebspejWMQyVvlgz30oFxC3QDMJKW4XbExe0zrZEk1Hn2GMuwOLB8lUT23jGyTGmjlUlVeibae7cQQWF5XCVzGj2FRhF_nkiIZfZJCT4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2407f2c6f.mp4?token=O4FWpIhRoPOWmIDKUI1TZ572lmwrCBeQoe_w_2uKLwds-H5SV5H6ce0Lp-EjDOIiP5aVeopJ6NcuHlHdyiJhANBscpOjaJ3FF6iyPE5NEmc97n7DBb-jn5YtgboqRjDGAJYSNxYEDXiYWW6DO9xs2lx902dtfhrxQkKFizxrd3wztVm8xlOXy2GGdybUl9x5tOiXGXpJN9R6IFfvYidSKq6zqWvPVUpuTv_KtbWuMItB3RG22LYb9pPcB4Y6QWt_ACqIIIZNJ4k-ZF3SNmVYk8ap1U_MMGUafmgsznIzHako_bLTAkUIY2ey_gN1wDtd_G8zfg5khFzqjELK0nCjD7UuDfR2Ijt_vfyQr41-tB84-BZV5g-CGPlyAXhDELmQzLk4Hy9aLAuLJC5oKE0RoXaqdCYn4r2SYj37-Zp54fb64Vff-nTEPt7lJnzqH5yJXkLeknne60fB3yz0uKhu_23LFASETc7YAZVKh4ELHwpNlvt5J7CsEjIcvk68SM2e6Pa-PaY0rsLpSEXc6dakGcb9auEGZETXCoE7HUrIq2AH_YdEkpHRHob7lq5dLDWxIh-RebspejWMQyVvlgz30oFxC3QDMJKW4XbExe0zrZEk1Hn2GMuwOLB8lUT23jGyTGmjlUlVeibae7cQQWF5XCVzGj2FRhF_nkiIZfZJCT4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا خودِ مردم راوی ایستادگی و مقاومت‌شان برایِ ایران هستند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/467373" target="_blank">📅 22:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467372">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RFJpp8jB0Wx23kqP0t5_oAU7O7zVFbGbeQzBmMBuTTNNcuv336m-ezlTh3FuxCcF3Lo17j04bc9fZYlLMiRdCrp4eZgPC4x6cCcLPH1aVUfmDPOlThyEztP-yRP-_FhW8rdg-rXhijE-f5CsUz9_OEItJQM1__hwZNKZritXIXWAvZb9ZoX2lHGjfiQ7MsE3iJEnKXiAwJMUtThu4BvGxLaQ5ODggXxdlTbFx1BD9qmZqb3Ciwu5NmYwikApH-9P9fvCeWduQwLzfuyMypQumlBMlKTslBVoiD_5GZJlF10r_3jsApAttKb6Lf4oHz1FO4Q5sxzxEqSUhyCJBwHaDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
حالا نوبت دعوای خطیر و کریمی شد؛ جروبحث دو عضو هیئت‌رئیسهٔ فدراسیون بر سر تمدید قرارداد قلعه‌نویی  @Sportfars</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/467372" target="_blank">📅 22:37 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467371">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maJA_zalTWhCPp92YfY7qECzZ6LLT5jKFKvYcEPnN5cZPMawwt_PIY3969MmwmLR7Nw6lKH5DKq0I1tfpTTNbemI7oOZGbhTPCWMd9CrMs2E4KF7UPPoXIXiUEuTOZCbuXYYZja6gbi9Ua9o8riUpVeaVoRBQPNS01_q-XJxrYFy-R1gJi-DbvGOElK2dzsGKR2aM2FRZqVPqUEmv6iUMeUyZLplxthV2J9mPv_75Z79GWeCky3YquqmPL4Xxs1Ff-aUBj72jxJPpoOTlAAb6lPL7DqGgmTYNSow247r3xLbQ9Jy9ZhzlbDbjczQ69MW4tePY2oetnJQF0D-hckcKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف در پاسخ به روبیو:به سرنوشت والرین دچار خواهيد شد و زانو خواهید زد!
🔹
رپیس مجلس در واکنش به یاوه‌گویی اخیر روبیو در مورد تمدن ایران نوشت: در طول تاریخ، ما ایرانیان با کسانی روبه‌رو شده‌ایم که خود را سروران جهان اعلام کردند و کوشیدند تمدن‌های کهن را از صفحهٔ روزگار محو کنند. آنان با آتش و شعله آمدند، اما با گرد و خاک و خواری رفتند.
🔹
کسانی که به دنبال میراث اسکندر هستند، سرنوشت والرین را خواهند داشت: زانو خواهید زد.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/467371" target="_blank">📅 22:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467370">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c65ad3179.mp4?token=P_U_mz4r0bwvwrAWFkjQSvxWSuH148FgpluncsVSPjBXdR2WPz0Eu9zait6o-w4QGrVo1VZcfPX5mgdztbCKazxi4YQv0ejGEqs-kFHSMKAO-GrJjFhQbj8fqBligdZ1WBFaby0u-6wmAaqgQ6d35ku4pgId_NtstFn7dzHzmlaPQBcaihdaEKy7fUgWFXwYDgXpSZLiIyXOFTNl6hMUna1BgKt8ruo2p4ye-CsqjnexeBecjucpuhIRhU4T-kjUe2tYqBTo-g4AovCrm5wruLLGRub6JiCGl97xGqhr33-ncRauTTBxDH64Or7VGFgWIWLPupaCS5Auf2T20VDy-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c65ad3179.mp4?token=P_U_mz4r0bwvwrAWFkjQSvxWSuH148FgpluncsVSPjBXdR2WPz0Eu9zait6o-w4QGrVo1VZcfPX5mgdztbCKazxi4YQv0ejGEqs-kFHSMKAO-GrJjFhQbj8fqBligdZ1WBFaby0u-6wmAaqgQ6d35ku4pgId_NtstFn7dzHzmlaPQBcaihdaEKy7fUgWFXwYDgXpSZLiIyXOFTNl6hMUna1BgKt8ruo2p4ye-CsqjnexeBecjucpuhIRhU4T-kjUe2tYqBTo-g4AovCrm5wruLLGRub6JiCGl97xGqhr33-ncRauTTBxDH64Or7VGFgWIWLPupaCS5Auf2T20VDy-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم رشت مثل تمام جمعه شبهای ۷ ماه گذشته نماز استغاثه به امام زمان (عج) خواندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/467370" target="_blank">📅 22:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467369">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شهادت مامور فراجا در حملۀ تروریستی در فاریاب کرمان
🔹
سرگرد مهدی جمشیدی، از کارکنان نیروی انتظامی، دقایقی پیش درپی تیراندازی افراد مسلح ناشناس در مرکز شهر فاریاب، به شهادت رسید. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/467369" target="_blank">📅 22:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467368">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYDSYNOHGV_HNQskSvgqCkeKYuDpsOf87cxcM_4lm3FmQsQxYdF_P1Rkeu-BwBhR2ei6PB6PXVh_OSayjEPn7SidmX9C9VeRJ7PhGx7MC7DXM7KSyAnjOSZKVceiV3tCrr6vlF4tkTbR5m0CErr2hzBVKbpgznOmLsfsPKM6PRhArtR7_S726sICF6FcGqVsID6d2AUrP_tLgquo_reqyI6NVOLC4BzE8ZrTE-v65fchOs0btuQjl7RTHVD8jSNDGLajNLTShR3-F-mw1bH_XE6R2_cBQD3hTNFfTz_PI8-M41owycriZY2LmEONNl8-dmMNQaEUumoluKUMYAvkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای ترامپ دربارۀ توافق با روسیه برای تأمین گازوئیل
🔹
رئیس‌جمهور آمریکا مدعی شد با پوتین توافق کرده تا مسکو بیش از ۳۰۰ هزار تن سوخت گازوئیل در اختیار آمریکا و بازارهای جهانی قرار دهد.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/467368" target="_blank">📅 22:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467367">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8698bd0285.mp4?token=Olo9_324RvL_TJ22bK4lNw7LNCrW_IAOpi1P517jjSYGCwvlNXjCOeo4zx8Bp3vBTEa1w4ut5Lk1ZjFm5gtotebeKZhBGuGbkIO6HDMFLDos9Sr3M7lDRW2heLQczCjmqJGY6vqa_HxM20z5ZJlqEEkCFCo8iwKsFio8fgyg-raM9X2_5gxWwb-nxTRz9yTNOyLUOMvRU9K3gzEcX-3RbiH2xdp0Z_BDZcrfIfCPBhtbGquSQYRc2OAn6obrzF64vVL_ZRahor4oexnYgt3ItF6-mpvg8oYoExZ5YMpZd5WkpqR2L1ZTxBHIciHK95CzaBjrLhXcqFeQbS_KQPc89w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8698bd0285.mp4?token=Olo9_324RvL_TJ22bK4lNw7LNCrW_IAOpi1P517jjSYGCwvlNXjCOeo4zx8Bp3vBTEa1w4ut5Lk1ZjFm5gtotebeKZhBGuGbkIO6HDMFLDos9Sr3M7lDRW2heLQczCjmqJGY6vqa_HxM20z5ZJlqEEkCFCo8iwKsFio8fgyg-raM9X2_5gxWwb-nxTRz9yTNOyLUOMvRU9K3gzEcX-3RbiH2xdp0Z_BDZcrfIfCPBhtbGquSQYRc2OAn6obrzF64vVL_ZRahor4oexnYgt3ItF6-mpvg8oYoExZ5YMpZd5WkpqR2L1ZTxBHIciHK95CzaBjrLhXcqFeQbS_KQPc89w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم خون‌خواهی امشب هم بر دوش مردم گرمسار  بلند است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/467367" target="_blank">📅 22:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467366">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78e9475d72.mp4?token=jp1gfgUq2H0120dNBOHq0nNa3-jLbcoyfBXq0rCtkTFD677gYNFkf-FtN1yLHcnwXKY4nLfq2J4flj2pEfjdDw1v_k6grgPbP45X-Rpp0eFcU2Idof2JO44QIdqqD5VF8R9qj1dX26p5gOkVBjTe6GYlC8XHIeblkr2B4Bq42zbesb_A3_iYG2jiW0LyycgUKALXOIx6GmNPhgygo6UJaqtlnqjngi5ha7ks1b2Ks-dmNSMXboR57p2D66TYxapzhXU8h7ZkE8j5kWnVth3fl_fL_H5QS93341J8pptnLmnonfdkrcSMSws9azFo7R0Rrk23JwIM4Tx8b-Z-NhGm4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78e9475d72.mp4?token=jp1gfgUq2H0120dNBOHq0nNa3-jLbcoyfBXq0rCtkTFD677gYNFkf-FtN1yLHcnwXKY4nLfq2J4flj2pEfjdDw1v_k6grgPbP45X-Rpp0eFcU2Idof2JO44QIdqqD5VF8R9qj1dX26p5gOkVBjTe6GYlC8XHIeblkr2B4Bq42zbesb_A3_iYG2jiW0LyycgUKALXOIx6GmNPhgygo6UJaqtlnqjngi5ha7ks1b2Ks-dmNSMXboR57p2D66TYxapzhXU8h7ZkE8j5kWnVth3fl_fL_H5QS93341J8pptnLmnonfdkrcSMSws9azFo7R0Rrk23JwIM4Tx8b-Z-NhGm4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گناباد، شبی دیگر در امتداد ایستادگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/467366" target="_blank">📅 22:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467365">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d06b82efe1.mp4?token=iN-Hw35smnr6Pvay4MkqYvZtQlKyVtob1KQf5tU0PkNXAVIaW_CcfgbIaX10NFi2x8a-Xu2IP4iC2V8LbfWtQhzFBw0phGAoDqgpwt8duJVUIU9XnKKn9wgS3GKtuX3aOHxVwkp3E7iRXpzLTKX1AzP8kCGAy68A4ediRvgAyB-oAv9V3P3AjnTEeJ-W44qvGWRM1NGIRpDT2KvnvIawRoI8IGjxKD735-E-2Kt5JM2cTilVR0_25UiSsUxH0MK8nSVJ76mjjuPd4PlE2A0ztGKwsxg2KGVCojHYd2l-rR2ORtFQzkH3e2jKh0q1_LJ5PfleblmT2U1EGEkl4NTlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d06b82efe1.mp4?token=iN-Hw35smnr6Pvay4MkqYvZtQlKyVtob1KQf5tU0PkNXAVIaW_CcfgbIaX10NFi2x8a-Xu2IP4iC2V8LbfWtQhzFBw0phGAoDqgpwt8duJVUIU9XnKKn9wgS3GKtuX3aOHxVwkp3E7iRXpzLTKX1AzP8kCGAy68A4ediRvgAyB-oAv9V3P3AjnTEeJ-W44qvGWRM1NGIRpDT2KvnvIawRoI8IGjxKD735-E-2Kt5JM2cTilVR0_25UiSsUxH0MK8nSVJ76mjjuPd4PlE2A0ztGKwsxg2KGVCojHYd2l-rR2ORtFQzkH3e2jKh0q1_LJ5PfleblmT2U1EGEkl4NTlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترافیک سنگین در دو مسیر محور هراز
🔹
حرکت خودروها در مسیر هراز به کندی در حال انجام است؛ حجم ترافیک در مناطقی همانند پل لاسم، گزنک، محدوده آب اسک، بایجان، منطقه چلاو، تونل سپاسد و نارنجستان بیشتر از دیگر مناطق است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/467365" target="_blank">📅 21:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467364">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1d9e35815.mp4?token=L1WaEyXHxXNaadg-ZtTDcfb_e--Ycij199FuhMUKjR1kooPC_YrYst374oynhPm64xqZkJxUwRExJYB16RvAu1QnIcHjqzImykICEhpg-YE8Q_eZ2R1fuxGAv1MNQg47LtJKW8sypuJKHJqwTUAid78Twtu8018Q1LHGnXEN7iqL5-VFtgKMEoP5BQsxjhR6lkH3Q_K9AAJrXxyrQITeeXx6d-nrn2GpAaKNNIXJsNa1ZyDUWvMKYBsA6wlEwd0_P3YqPXjTx3cE4TvGyfDOzTyHfRKdy1lZtljsxNaNqUTyjBFjqEOpm3z3HFClAktxQW9Oc2xS7QiH7KdRYEdgbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1d9e35815.mp4?token=L1WaEyXHxXNaadg-ZtTDcfb_e--Ycij199FuhMUKjR1kooPC_YrYst374oynhPm64xqZkJxUwRExJYB16RvAu1QnIcHjqzImykICEhpg-YE8Q_eZ2R1fuxGAv1MNQg47LtJKW8sypuJKHJqwTUAid78Twtu8018Q1LHGnXEN7iqL5-VFtgKMEoP5BQsxjhR6lkH3Q_K9AAJrXxyrQITeeXx6d-nrn2GpAaKNNIXJsNa1ZyDUWvMKYBsA6wlEwd0_P3YqPXjTx3cE4TvGyfDOzTyHfRKdy1lZtljsxNaNqUTyjBFjqEOpm3z3HFClAktxQW9Oc2xS7QiH7KdRYEdgbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محیط‌بان منطقۀ شکار ممنوع سوادکوه مازندران در جریان گشت‌زنی روزانه با گله گرازها روبرو شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/467364" target="_blank">📅 21:51 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467363">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a1f2962c2.mp4?token=Xp82YwfcbrfZwUC3xcFfppUfRjosrJbcykmCy5f1xtDMP1tHzW53F3StZ3TtX_cuALdLU8E7YCeDK7P_E_3w9FG5hKV9QSdRYLKKhFAMXpQ3YkNWGGt6Di01f26SunUD1eLufC9ULzT-ei0sRGQ-XCMqMbKxB63R_ynv7IBh-OAwLGIRqNcw7YPhpqfs6ESl05owpKq0OT2iRxTUeJHx9n-K8KnEhUudOrRP5MLMt9D-0_cMQ5CsEL5pGhv6tC8Tthg-O94L1DHmmifJiXwmSJWZIjnUyJaUoBFuLEjhMn24QHfpCDz7ze-WQDTKxSKxoFzj2wkHqaVTW_UbGba9JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a1f2962c2.mp4?token=Xp82YwfcbrfZwUC3xcFfppUfRjosrJbcykmCy5f1xtDMP1tHzW53F3StZ3TtX_cuALdLU8E7YCeDK7P_E_3w9FG5hKV9QSdRYLKKhFAMXpQ3YkNWGGt6Di01f26SunUD1eLufC9ULzT-ei0sRGQ-XCMqMbKxB63R_ynv7IBh-OAwLGIRqNcw7YPhpqfs6ESl05owpKq0OT2iRxTUeJHx9n-K8KnEhUudOrRP5MLMt9D-0_cMQ5CsEL5pGhv6tC8Tthg-O94L1DHmmifJiXwmSJWZIjnUyJaUoBFuLEjhMn24QHfpCDz7ze-WQDTKxSKxoFzj2wkHqaVTW_UbGba9JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقامه نماز استغاثه به امام زمان (عج) در شهرکرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/467363" target="_blank">📅 21:44 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-467362">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c10040e9d0.mp4?token=j2Ug4WarqoKMJKHwHm5AXainfMBr0nmgh3Z1XycbA22Kn-AjTsjnjM9oPXGzj-UkE2H_73UD5aOWTx0yqbSCjjhaTQjEC34LmZ7w5E2FeRX3S1UFoarIqLy0dOwEyw6eboV6Ur-hoCOAmlP8zAThwQrkeSfMc3IV5li3F859tetegsIelRgNpl0VrdKoMb7PTDZSJpByzH9cBYim92Yy7NWPMdRZW33RP6wcApxODWIzFKz_cYwFYeb-lYSqERqjbW4gKuM45UYbBRB3Wv_QStuIXpXs77p47NlVhsZxfVtvpt0PyUWgCCSQP605rexWQX5pV29pI2Rt5W5eXpu9GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c10040e9d0.mp4?token=j2Ug4WarqoKMJKHwHm5AXainfMBr0nmgh3Z1XycbA22Kn-AjTsjnjM9oPXGzj-UkE2H_73UD5aOWTx0yqbSCjjhaTQjEC34LmZ7w5E2FeRX3S1UFoarIqLy0dOwEyw6eboV6Ur-hoCOAmlP8zAThwQrkeSfMc3IV5li3F859tetegsIelRgNpl0VrdKoMb7PTDZSJpByzH9cBYim92Yy7NWPMdRZW33RP6wcApxODWIzFKz_cYwFYeb-lYSqERqjbW4gKuM45UYbBRB3Wv_QStuIXpXs77p47NlVhsZxfVtvpt0PyUWgCCSQP605rexWQX5pV29pI2Rt5W5eXpu9GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۲۳ شب ایستادگی در میدان ۲۲ بهمن ایلام
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farsna/467362" target="_blank">📅 21:39 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
