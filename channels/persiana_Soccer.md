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
<img src="https://cdn4.telesco.pe/file/VcFXkz9pfjXvtleRhEeUb5VcTHeS1G6LfrOxkzd6OpvDnuVq-51HnyvMmqFmU_I1Geb4xdhAo1qZub0bVoZFqnUNHbNihJoYrJArkGRUgC7QMG2HvONh0spkVfB6IXSuE_T3zGkYRfxIP3JWWqTnu0M5thFScz-sW2jB7CJcUMZsu_Rfusu9jd35WqkcRO87iKnZWJCVDJhRDfdUYDva9C1bm7Tn_eeIz8B1Ft2ZYtxhVQXO9HjXt1HSCx3NUVTPTSz7iq7ntYd_s4ftFnmLoXOZyv0hZa1C7EHrlSX5CM0CzuItIZBiJkmiMexfjYYHRLQCq2aXmRDHBELUMV3Jng.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 626K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-27 20:49:08</div>
<hr>

<div class="tg-post" id="msg-28001">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a08f75b6c4.mp4?token=idgdxGz9zgak5Kh4fsyEUt3IuGVKo2XweL-SEoG8lrckn_wzIQc1VSGlZ0L-rLMfUE9op78vBpkAi9qVb_v_5FccDtFcSOvIQDhRwMwbw8LOdVqNIHmfoF9nvOIs-s7Gok7UkMjglZM91YpcWVn4d6__hk5Fg2kJLBhHh60SGeLFxM-ytBdCgqrRaUBauh0cMNNo9BU84tw566NafDwRLbQbEqemGUPszwQWgxoJwSCCPqPqjXbGRN0yMA7b66_lRNas1yONRjIHk50qSS1sg4s4XxyI94NN6ZNgvIioQBV2mfHO69yMuCalkT3cEgY0iqDJlY7gLxP0IObmFdvcSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a08f75b6c4.mp4?token=idgdxGz9zgak5Kh4fsyEUt3IuGVKo2XweL-SEoG8lrckn_wzIQc1VSGlZ0L-rLMfUE9op78vBpkAi9qVb_v_5FccDtFcSOvIQDhRwMwbw8LOdVqNIHmfoF9nvOIs-s7Gok7UkMjglZM91YpcWVn4d6__hk5Fg2kJLBhHh60SGeLFxM-ytBdCgqrRaUBauh0cMNNo9BU84tw566NafDwRLbQbEqemGUPszwQWgxoJwSCCPqPqjXbGRN0yMA7b66_lRNas1yONRjIHk50qSS1sg4s4XxyI94NN6ZNgvIioQBV2mfHO69yMuCalkT3cEgY0iqDJlY7gLxP0IObmFdvcSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره جدید بارسلونا به طور رسمی معاینات پزشکی را با موفقیت پشت سر گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/persiana_Soccer/28001" target="_blank">📅 20:20 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-28000">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMpiW839DsFUOL18-AlnMdPdaPRF8gr51IPGheZZG4pu_wnhd2UceJw-Qgm7vrx7HGi-tJEYT1SWAa-XoAMaYwsz2D9SnTZBcTLQQpZItFLjaY9pupz4CvBA_yPm2bTMbR64uxJhaNzXJIoKzUH63Znkr6A4ArGkMwi6hIW8U7LrOm-Aw25xNZBSmwmx0g3Esn6jnUMNLw5YLJq5T7Ndsq4I05ZQdXWDMWDiC_IlhYMiQcvP5P-PwIHLo05ReSVBEqCr-dgluQEulBa22FPGXEnUjwauglfUHaNNcBCannTGLj7TEHGTkYQ-OEVonl6cvgWNRiOhNmknEA4dekenuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیما امشب تسمه تایم پاره کرده و لوگو تیم‌هارو به این شکل که مبینید اشتباه درج کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/persiana_Soccer/28000" target="_blank">📅 20:15 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27999">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l20x9ZDoW9tb3hZ1y_bYCyin345LuDItB4RH-daeUC9bsLYpnDHHBooTpkCEfjEklixGAnawRD2KxSnIT7IIUkDQzE2wVc9XAJF-7EgKiFGoxkrsm8_L_cJh4OWSd-XzOPT4eRXN_Ezdq32PmoclnATwqJI16cfWlSnRmq94PqptTM9xLu2A9D6f4SzXkxFtEbynAaBPpybkdxYYvmYkRrpdyzXRUAv1BEKnR8ITpcge_AaqthIQv-f1frNcrurqklfiUtyNYQnpSnmPAV_WLPDNGAcG4UZ3iJqJY57aPEGyQ9aeElOvkZmQlEOJqnZ4btV7fmGDB-f9Fb7rmA_CTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه فردا مسابقات فصل جدید لیگ نخبگان قرعه کشی میشه به‌دلیل‌ اینکه مدیریت استقلال نام کشور میزبان‌مدنظرخودرا به AFC اعلام‌نکرده اونام گفتن پس هر کشوری ما بگیم میرین بازی میکنید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/27999" target="_blank">📅 20:07 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27998">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSeJFO-_hkotTT4Xld6wqtMEFrIbyKppob5sBK6a7B4DdmXTuwZdk5BijMuw129QBlxP19eYeLpEG7Ie-k8dRoQ-JKVL3KZLZoMHAPZkntbyPEozAwJyV_9ybYVUhUQnCtpdvPeyBVU4U3Q9a1qrTvGEl_RpFtSscImWLZF2pKJI4-uvEydMCMF0Eu3jr-gIsQW1M7CmY7AkCdY5VyGicURs050_45xwehvMAg0uSW1LbYVwLWNJZRKJ2TRh9HIcC66R8URgdHTGY8M1L9UeV4HnyT6n9S-R6OEehg3HbA8SCg_Rte25ipxp3wwMhZV_TgqYJdue36Oq8lVA8Ab3Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
شماتیک‌ترکیب‌تیم استقلال برای دیدار امشب مقابل تیم نساجی مازندران در هفته دوم لیگ برتر
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/27998" target="_blank">📅 20:05 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27996">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UnjR-M07ph1ZJXm24rwcAUB40e8ddig0jXdX7H5p6sY_ZdEdZqe7PNju4rtSUdNi0FVQGQk2fI4aMBpbiLyj_gl8aYM33XFOiT4C1ZUARUgcIO8152i6RTMGmHehWu3bQTcE6w2tB-0XrTnSpFTkHNz2Au2OqWvgMaEnKDQYSHOfuQhcqu9Xt6bGjxWWYdZ-mvapeYOcjiqzny9WUjjR8vuV8k8Fia9Ckua3iwQ3w6bk3NdqZ_rGQ9dIU09BaW83WEhwJAHaTuSDYLrmCdiYILQ1mFsWwB89jkTVSs9Xx8O7dEFTdowPmhhtPM6-G3Xyr90QiNVhhsc-hSqL4Ci-5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n7td-09LODcKh_VE4z_SPNB5dQNQIpjVa3khhqo0W6HLjTE235pbUbJHdru2lSvzC6OC3xFmbT_-X90oFYfuKBu6j5nfh9BYbBgFpP6c9RzkI8IrfHDIZY0EnzWFTdjlZQLWjQN3Hxbl1xr1pIJ-8pitTrA7XyaVFqs7pKLPj_Q1g5YoLo5_LkEww7z25f6XmEHgogg8Uu4IkJ64-hvx9ZlKc96aaAI9U000pbhj7cPSGNRWOVwTRumtuc-YbfSNZCWfarR-TpgnRvJV1jNWEkPpqypEmaVcMYoOyKiHYyGUgRA0MO3cS3zcomryqzC59V8KgxRavA26Wobhl2HA1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
جواهرات جورجینا رودریگز جون توی مراسم عروسیش دوتا تیکه لباس ساده‌ی ساتن پوشیده و جواهراتشم از برند chopard بوده که گردنبندش هم ۷۵ میلیون دلار قیمت داشته و انگشتر پروانه‌ایش ۹.۷ قیراطه. ارزش کل جواهراتش تا ۱۰۰ میلیون دلار میرسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/27996" target="_blank">📅 19:43 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27994">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YHQydYVwA62_jUJxwFp-OCC9Cf0owY4vqHngZWtCRYQ5IvkaX291mS8dJOs7BWrPB28uIrXc2Y7c4mLUDQMIjNbIWF1VsnZJe4hInlVvEzn0BftWRATQhzUfZxeBiNDw5rVY7gUHR0FsvaJfiAaeLiOQXce8MNVQpf9FIiSo040HPWoJ0SpoBFTWItvDfo4kMuJuar-vJrRnlMjDIv9LgYOMqx-YCldpViMMPg8ggTBJ0chsd9PgA9FUowEkhogTHM83cWCW4f8Xk-SCh6dIwiC_sC8yD5Sniu6KioM7kEtNU50EsX8wdNuPo0Ntf9a3_VUWENIfQv6rva-U1rVL3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pmOS1ywiWdnnm9GurGOHXjjwW8H3zbWfyHggXAkzbAjkuUJu3LbLBumRHiKakQaQeP3E7NJzYC3AwMW3H5fHqtjCfCv7PSIJRAVEUJMA3pSK6eJkOltGuupT04C4xYtYdDPIOSLyaumlzH2KH2rnLrSTPLNHxl9l9iDfQAq92p1wHziQy8xuz109SCF6Zfo0LBexoLAgall_e1iZTvlHqaf4KBJ_EwEdSlJ7bN0bpzfpMhIfmztrkmCnI411aus-xHeDHjbXSx9-8b_MmB5NZeNWcAqK4Yay2RH7PDoGm1Ft64MGs7GszF-nlEZGRRp_kv-y9pkLMoqyRM-a675aWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته دوم لیگ برتر؛
ترکیب دو تیم سپاهان - تراکتور؛ ساعت 20:00 از شبکه ورزش سیما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/27994" target="_blank">📅 19:06 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27993">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqpAAGG7nkVpAjXxfZLDfniAhfVId89WqZ_5RDsuhss8cmqv_EAOWMm64P4JWgW6VuzXKuu6FqUa8M4sQwuOHgqlbH7OJ1pPaM2s3IKUbg6mcne8Jfyk8f83zqt3wzYXGRftfs_XPxLXJswgKCkrydXodi4tChBheLNppI0ZgKpKsCGjNBRemWEvTqfO6imPL3hlgwWWren-f_ZK7Tqe6USDcKcxQlEdUQJK2-Tv_b3kEDanjEWGgqfu6pJcuLfUAd9P6Hz872_Fjk965t9zi5sniO8v-BPZXJWa1qPU_kIvdAZhFr1cC3KcVakQwpuhMHXGyLdm2rBPhdQLmXVZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
🇪🇸
ژائو کانسلو و رودری هرناندز رسما قرار داد 4 ساله خود را با باشگاه بارسلونا امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/27993" target="_blank">📅 18:37 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27992">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1EMC1I4Dx6zGUodFXuv1u21bFFKwukenvBipfmJ6XAkAqEOSSFoD7KDnKA05QxAfmxLcrQuR_GzNsIsPPZ0b4PjvMU7aJKKaR8kZ2mpysz-SWH6cXjlvJrYBJ_v8eDMgcWYk5FM7Jjpuq2qTpgkwnuCNXLciaj97OenWc7jlbFgUwQu6ZI67N0FP8LFDhodj5r-nHlvUkhL_iSF-Ubi-AP5Ellu2sBu0AHal9eUe_Hn1u4l_XdieIPHu0F79bFore3L4VGFcp09HPbZGJetuznvX7ryNiKYm3Y1wY9ixAol746J05PQSwYesWj87WArQvVqQiV7f5my9suU5Ais0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر|ترکیب استقلال برای دیدار امشب مقابل نساجی؛ ساعت 19:15 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/27992" target="_blank">📅 18:17 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27991">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJN6XsFQLYxWSAw_6T5w8aZfVhEDpGVi1ZPIzKMnPRsMtfxmM_z5jhEhfCF09pUL2aLJ8SE2uxkKpeEctooT8ONNRNpLc4DGwiH9GCbu1YrXsiDhDFCU7V0YE9QqU7wrYW9wWzBdZkqp64VEDOlFf5WrpPgyEpbVCRqv6923S_QwYxvRZTAs5qYH77Aysz04YX0rNCUpgoBnfM1-0jk29EM6QKR_khDldQQUH8WXERkYmPuQnBk3TMVscwiSWgpNHoVlod7U_lm7xr-6wy__OzWxrekr5x_0SAB5xKpiJuCb-nFRixFsSp-VZzQ8vlKByxhyifrgLE3WsJSzvYQClQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته دوم لیگ برتر
|ترکیب استقلال برای دیدار امشب مقابل نساجی؛ ساعت 19:15 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/27991" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27990">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwDkGN0zQ414e7GSuP2jFqaxruLlDa8Ix3DFJsaLAjrs9N0OtxyxnLnaVn2kBRuXYFy3p68gkf_RipyzIBOZSTHwtWxseUN8N2wjFwW5FStd8q-tkMgEgNHFzO1Iiv7OdIl5-vpkPTdXFX7ycULR9VlS42AQliexVvGD8CnSSLK-rHN7XxnyuAJnLctodUIHDiqg3sxu-yEBD8c-ZYfSYoz73gMVxHz7cQ-vgO_aGi-QbG5Di0vH-rpNgj6iZ1fsiu2YWkcngV9JooBe9h_xLHTPu8tfzWUEXj7csZe84iA85MqLx0YkBvYT0-DBahNvrwF9RTlhRm5g95UwegyThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصویری‌جالب از نرگس محمدی و علی اوجی در کنار پسر بچه‌ای که تازگی مسئولیت سرپرستی او رو بر عهده گرفتند. دمتونگرم چه حرکت قشنگی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/27990" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27989">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKsFw0fCp6AisuJyY5DnquMNImgD1-BTjl4U2m9K7FyB9gVixguOjaYm54of-_EEOoJjA-e7w-LRSs4n7BId29aqQExYgE14uUL4VwKnv1vba3c24DiAq-K1ALa6eMEoIw1rLar9WlvMSl6ys6IIGldL_ALr2jnkao1AC2k44qilK0QVW_c9fOJWs-fJVlh_kn2KtuaNjqispv4tEaduz0bbZ5oFO-6T_ozF-xGnapZ08HtlNuBaB0SlcjEK-3x4XPYCsFp_BWudRTWch4xMj2ZbLAp47X0gsObqqb0MdRxxr8QJSRWNbNs4yE2xVG__psrmwmewcryLLTZ_e1lX9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته دوم لیگ برتر ایران
🟡
سپاهان
🆚
تراکتور
🔴
🗓
ساعت ۲۰:۰۰
🔴
انواع آپشن پیش‌بینی برای این بازی
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
🔹
http://betegram.com/affiliates?btag=3_l7
.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/27989" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27988">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ4enumrIMX72P7aOsl18DLKujMzSGri-kVhnp0DVPwpgJTcLwV0eVPGQSKMOlUAXDHDCQzaaEHHjdjlFBVamLEVQpnJOLqUOMTcfHYb6yDCAFqh0I2ySSWsU9yY-EoWDnjfxNGNwDZ6RRUc1X_thZ8hF5DJCvq4bDuZ5IY4uzBisUEPmdSKHJhc8O_OgXDtP1WG5qIvpdRB9e0Tu7ICr3Rdof1oh_-Nbnb04nDnYoYkZ-akCBG2i3C4L278sLx6jIZD8vUPXu9QmkKGLb2yHi--324jU60NlYB785B30JgRb5Y8VNYs5cu_TRzAS4GX_bMcvlTfKITJausMOczPyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
مدیریت‌ باشگاه‌ لنس فرانسه بعد از پیروزی یک‌برصفر این‌تیم‌مقابل PSG در سوپرکاپ فرانسه؛ به هر بازیکن تیم مبلغ یک میلیون دلار پاداش داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/27988" target="_blank">📅 18:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27987">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzGhFVWord9oJjzVtzUzPftJ_xB6RMna2opVo1_z6Ue-9Ps_lOaLaSXECMzYzEU-AUt14uCZLoZEYf_a-H8N7QWyOsamlq7UEXtanaW54svi7-zuvcN_nDmk-Uq_R4b4E5tnAm2WXEoqeW6iHSVwWr-4VjqA95A8y3FUNNE0iKMfNJeFVT8XedBYfJz2-RgQLkbgE9c_e_gpdRlo7ehhHDeZpMXolpBBS-gYkda1_fFRl6LPn8U_XWh26Q9UOdqXj-128vE0eoS38RsWMs3_idob3GsR8pmE2trNUAcT3chj2VxkZmd5TNFkwTYB_chuF6MxD2-B-6yLT0Fdql3LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکولاس زوله30ساله‌ای‌که تا همین فصل پیش تو بورسیا دورتموند بازی‌میکردالان با این شکل و شمایل داره تو لیگ های آماتور و محلی آلمان بازی می‌کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/persiana_Soccer/27987" target="_blank">📅 18:00 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27986">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJodWqdQ1MB6Q33MHODmKovylxC_2JB_b57Nt6jaSwiEErvqCAdCJfJWCF1Av27nGqB3hA8txog010QzhV5IPlSO9KY6o1REy7OhrCo9ro3C6os-lHqCcYsZa6bMvMFETc3QCNeBfPw3ybc_dzrfoJGnhnfd1XcD57d_RxVaaKBIcgLsjfxnraq7qKwrt6B31P8jLvSTRA5A3qRcdkXzJbXPy8JZqHzZIXU3PYUqQMqZxPfIKWnb-ZTrxzuJ39PvhGLuMPhjvf3ZQ8C8gNLrbHR4IwlxiU_O2eqDJAD8C8eosMjUh4FRg6nZfOTwdIDFcx50chCL2cMoXwLAr-zjdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
برخلاف شایعات مطرح شده؛ کمیته انضباطی فدراسیون‌فوتبال‌امروز اصلاجلسه برگزارنکردند که به برسی شکایت باشگاه مس از باشگاه استقلال به دلیل بازی‌کردن‌یاسرآسانی بپردازند. رئیس کمیته انضباطی هم اکنون در یک مسافرت‌کاری درشمال به‌سر میبرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/persiana_Soccer/27986" target="_blank">📅 17:55 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27985">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKDAcQBCL4jpNBpq1-bA1zzjK12t46sv1Ebp_JWwoDJQ3O8iyAVDmCqH09EzXxbJsV8JtqNQmBz14cmCoV8KOwNNdTZQqT5ZxlHtgzVIXeRaEWRjd1vWYSpIX-wXrRr5AcW1Y3gUwmYKGtmR5-QgMon68oeyQZkOJIhio9_cH5ev8ZkGxeinm9-vnFpzwLgBw0SvmGpF_0Z_4jNB29DxDuow5SbQ0JQ7sHWn0axFfnur_ldNWhMmCWdK6F5GsF2aS43Z-P_I_dQvS6NH8YDUccAea4fAndnrS6eBLvQnpKhKipNg_dsuU0t2utX7cwjFHnt7e1PaKNKQ6QvhvfpKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره جدید بارسلونا به طور رسمی معاینات پزشکی را با موفقیت پشت سر گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/27985" target="_blank">📅 14:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27984">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vzo8FVsHh_R62sYNUlSPv-H4wCRSHBOwj90riECuSMfS40eNAgDPeQHo4n27g5mtyGaTrjOUTEkJi-hrvc3__BSqtmJoUS8_iopf43fnRnJo2CaMj9pHIVraoAPLPcqrTxbMtw5SjcH5FBw2Uwr8BFGm0W6OoTvVbqGTAbIR-lFvE5SMmR6H0DkJtyeTj6qTWwwT_s3PIEzz3IgZnmf3KGU28m7bw08Y_g2VjhfaG0AritbCW1_J8jP9NK30QV21nkRE9gF_1nAOw-kcLdoFPgrar4TqMrW_kkIByf7rPgNjavKda9cbmLesiMPAI1Lk_vmIcaL-cACNwjdnvqJDag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی پرشیانا توسط کارشناسان حقوقی‌فوتبال: آسانی مشکلی برای‌بازی‌کردن ندارد.
🔵
هوشنگ نصیر زاده و رسول باختر دو کارشناس حقوقی فوتبال: بازی‌کردن یاسر آسانی برای استقلال کاملا قانونی است. درصورتیکه قرارداد او در فیفا و سازمان لیگ فسخ میشد و قرارداد…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27984" target="_blank">📅 14:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27983">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X88k_UX6uVkorm_FmE_Rc8733F-OKDherSch541kiO-kugWuVKqlbkIYijdj9JKziF9a7TlqpYn5QHghHf1vcwvnvUgUkK-3Naj2-rhlFx_wrG6Htr3i9wt9qGqoQjIyqR5KUcf2r2CdzBEeHPksPZ5QXiIinF_yOgIchYp_c_SA9UZaGeb3g5Et571VvMG-HvlyI8bFcGe9aJ1IxwMSH-cZLUKsQWzIOer2mOz8IM0Ig96BaAQgCIAoMyrlm-Mye_azC8HOnonBrWEQNq4PcM5jeJZBXdfZ5R6G0WbeO6fP1qx9rTjJTsycCLeILtXtVTnA25VKYhjuV9BEIX2APQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسام‌حسن سرمربی تیم‌ملی‌مصر شاهد درگیری خشونت‌آمیز دوهمسرش دریک‌هتل در ساحل شمالی مصر بود. حسام‌حسن درهمان لحظه بیهوش شد و به بیمارستان منتقل گردید در حالی که پلیس هر دو زن رو بازداشت کرد. مجبوری مگه ۲ تا زن میگیری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/27983" target="_blank">📅 14:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27981">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZsLk9UD8bfIe2Kal27AeDtSH_IPwUQZv0WwRnDFn73YYdnrMx8a5JhPIq4vdkIN9yliZ2qiN2y2CyeKh6GG9GETnSBwohgqPSYxdtyEz4ZFcu7Mw39QdEZtE9Iw5xl-VPOdeX7ZtO_mpvUu6mP2Hgfb24khgkIU8zXLhF3GQZ1hb0TGHlvV0bGFt9iG03k0DiCxuzZ0EDMsTzMiXnf-vEphjxKl4eM0R66aIi2ncuwHO7VZ1y4LisYcGdsMrFjaYwz5qNsJVEazv7UMjc5LrL2QgxXaItkkBuyAZ5unDpk2VFoPnI6Z55HX4zWO3jAhsJbRtn4ybwxsPldSuR_1aGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره جدید بارسلونا به طور رسمی معاینات پزشکی را با موفقیت پشت سر گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/27981" target="_blank">📅 14:01 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27980">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhholAhsYT2MWBTyBKyRW3J8JvIayocilb_fxFuAqrbbxCU2BdQGhAYRpOTGV7rjWRSQ0S6DuwfLrmZWec3Ucds0d7KAOaV2Dzcupqp92Rohh3RJuNoMaE-_fnRdTpGpLtNaBYvpgXxa77x3HQr2_IWku6ByHr1whx7-F-CPZHxNF6S22lVRRRndIvBsxK2aGMILQ0D62hA7hZ29YkuqVCUDWs-UkDsYQ8ay-mT5u_EFKUaJgTrBEDjUS5WkOlACCtcf_su37SpqkiZ-cxBYj-WtTptkAbZw2IGAsGdIda4s_JjuwksI6ToaYDWwkpRSbWzFFZIopt0lcFqeLrSuxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رامین رضاییان ستاره 36 ساله سابق استقلال با عقد قراردادی یک ساله به فولاد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/27980" target="_blank">📅 13:47 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27979">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pgi8Djcv3VslfMfqOQKwV9O9QpdDzYj09MPtYQ_m-mwNiZ8_o52kYUDT60GX-HU7_tpGbY_tG26zWoEre3ZcThNt5xdRE2GuPCIhiIbpz9UAoUUMIl7Djs_7L9NDExASrWhqCCfCpklb6r9SAbHNXfTREeBeYxFcDomOmpsiez1vdL99A5dT6WSzszOWxMtML1bqh9gcP0H7TCkYTmTMMngJ_au2xHQjOBrTujPi3IQIMfYqJG0kHa-Lulyz8SRaDhKiC-jaEN5uShF37hjXaFtU5CZTRZN9z74bYw_c_uLWf4Lxpwp-TMUOOnzfqZcZ-xFRFN7cN5yNZLZrLaiI_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/27979" target="_blank">📅 13:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27978">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0OnawQihGo0bjg8DpFc7MhvH2mA8vnTWu5IXVLjjBe7j82gsxgODG2wcvEd3ClfH5FAU3tC4lzprsixe4Sc8mQcfW0YiTkucmfVKB84KouUbESad0yADtwybMmsbOyv7wkfaxnrtRsbrlSuSE9DyQfElVw1EfVE9iMOrfxZqJiZp8roQ9A7QxfC3pleRwzo-E10IxfXoGJUnZIeWRPElhuFIEA5P-K04FRuefB7BtRpswqltFbXpGTnd4WtGkTa2Xmz29YnfaIUXJ7mqXlTpRKHtM3CxScRZY0V9ncyDrfA2HZnNECP8PCwoLNaXwzGPh4evwwfbqN_hzjzMnHgdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ به احتمال بالای 90 درصد از بین مبین دهقان و محمد قربانی دوهافبک‌جوان الوحده؛ باشگاه پرسپولیس یکی رو قطعی جذب خواهد کرد‌. اولویت سرخ‌ها قربانیه درصورتیکه الوحده تخفیف بدهد. هر زمانی اتفاق جدیدی رخ بدهد درجا در کانال میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27978" target="_blank">📅 12:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27977">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emT4nQsnwDj8Ira0CYve50Ir_HmVMbn1MWYBMnuEV4vMQhfU4J7O-nklxCQqdS_ydrNx95_rxKgbSw-IcQD1T6eYVVaLRgaxpminCfZThF0EQje1vhJV9tw0g-642H1jl54_D7C8mTmIO52V5nGygefWUqLvuCXeH6B306DLWAbLXHZTc_1QBV4GS2SnbTP3MHiwurLtH01k1kAgEMNLuuPHLw9ZTpzmeKAHIiBOPu7X5S8IrmdznFyE7Wop85uN8YC2byNpH886TSl5yfpyQcY9o7Ey5uluIlhv-nuZk_-HXcTCFTI2seJq6a7_3B082nLwh5hpnDqvlBJD-iyUKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ شانس‌بزرگ برای نمایندگان ایران؛ نه استقلال نه تراکتور هیچکدوم در مرحله گروهی لیگ نخبگان به غول های فوتبال عربستان نخوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/27977" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27976">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlvZGT0Hn6lN6nMqyTELnlBK91BvW3TupuK78SFuE4AEp0aQBws_Z2G6DV-82TEadoN2nsWCiS7Nkg0DVO_YEASSOeu27C0cOn7w--Tb8qVOx-HksIKjCoh_EFQEfkpsiKCjGlc0LjNIAM4xTr1LsdJaa0nJ-QAygnxC2anTSOsgK8AyPjXPtxl8Vm5ognJkKKUcT0ppF9NtCRhwQzfCY0UhcnFY9usRU1oMNPDwzCPajKpOFHh_AEKjZBhGL0Yxu0AEwLc7iRmw8Y_sYfDnfoKlWHQAc-fzSTkSQPDsvzpEZHzApcCmRJA_DW8w1X0pyPYX5DIx0g827_4YAIxMUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اعلام تاریخ مسابقات فصل جدید لیگ نخبگان
🗓
هفته اول: ۲۳ و ۲۴ شهریور ۱۴۰۵
🗓
هفته دوم: ۱۹ و ۲۰ مهر ۱۴۰۵
🗓
هفته سوم: ۴ و ۵ آبان ۱۴۰۵
🗓
هفته چهارم: ۱۱ و ۱۲ آبان ۱۴۰۵
🗓
هفته پنجم: ۲ و ۳ آذر ۱۴۰۵
🗓
هفته ششم: ۱۷ و ۱۸ آذر ۱۴۰۵
🗓
هفته هفتم: ۱۹ و ۲۰ بهمن ۱۴۰۵
🗓
هفته هشتم:…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27976" target="_blank">📅 11:59 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27975">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsTCUUYSZWN_FN6E7OR2egzkI2titXNb6g_j7Cm8xO6qf2skfsPe35VpmaMUXgS8tnsSg44wFahW_30hOPFjkPDnJZXKdZsICowT9rTtkw3gNsd6mpmSuti79pDMMTucEJ7zhhUiST1FTrwVvai1_s2KLMCc9njU3OduQfZVrHs-UK4Twa7Hfo-Zziti0-CGJvzjmhojFDCTeSWogoKLdWQHrAYLSkYT68441QEpjtgjwsvoePHZkwS8b7uPttuUHMzrm_3DCLFQV0qrKipxrie_G1_HmtgQlhks_GqoF2XhNafdBSjxoDt25aiCErCXfvWWFpBnWyY4-njpXczoSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
اعلام تاریخ مسابقات فصل جدید لیگ نخبگان
🗓
هفته اول: ۲۳ و ۲۴ شهریور ۱۴۰۵
🗓
هفته دوم: ۱۹ و ۲۰ مهر ۱۴۰۵
🗓
هفته سوم: ۴ و ۵ آبان ۱۴۰۵
🗓
هفته چهارم: ۱۱ و ۱۲ آبان ۱۴۰۵
🗓
هفته پنجم: ۲ و ۳ آذر ۱۴۰۵
🗓
هفته ششم: ۱۷ و ۱۸ آذر ۱۴۰۵
🗓
هفته هفتم: ۱۹ و ۲۰ بهمن ۱۴۰۵
🗓
هفته هشتم: ۲۶ و ۲۷ بهمن ۱۴۰۵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/27975" target="_blank">📅 11:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27974">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT-c7FuKrGS5GyDlgCR7EULmBdJT40CGCJDUgsUK87g0CTSWvsWZUmY04encMxAa0mOwmRIzYYqSxSCt3Qe6N8NYtVu4uUN2iaaWx1GPESjfjMfqfiAJO57oDISr9nLFbAqVtF4igMn4eQabjlgByygTpDnozLiVChAk5PxfOBFZYd-dUKgW2i1t8daS87zY_OmD4zv_erOgrbKq69ubHbj7Nw_SkUlIpszDrg27x2jNxgW8c88aX7AlC-08OhQjRFWUiWzi6dxYOuhAcqLnJjv_VsHyvm5J3xT4obe_0dE8tQvXNG7AI2ClJ1epgJ_43brTcOQax1QnNtW5B61c2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ترکیب‌احتمالی‌استقلال برای‌دیدار فردا مقابل نساجی مازندزان در هفته دوم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/27974" target="_blank">📅 11:31 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27973">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwmng1FscG8PMeJsbY06kfzy-8Pt9ZvLTYdYvAcG7ODGh6_4LwyU-cHhLE6xVfZaON_v5pBBdTznIRtbrImKYZI08KZRrajYJohjYg-AbHTg5FY4QpIsOujOTSY4Cc676u4_s9d8XXITkpHC89MV41bApJ4lzInXU0D8yzBv_xmcFHqDf5MeRDKtfTHYweZWWZ6IhOrJ6dWorecG83WfH2ZE82tbWyquEh627grMkF1d_RjppwBzSYm7WjIqenAu1lB-4cie4ezBhW1N3mOiDOnjWUATuAGljoVRUVbYlBmML649qWg5aWjQdI2QCQhjavPrsjCXSLTk_zSEs2LteQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالیکه فردا مسابقات فصل جدید لیگ نخبگان قرعه کشی میشه به‌دلیل‌ اینکه مدیریت استقلال نام کشور میزبان‌مدنظرخودرا به AFC اعلام‌نکرده اونام گفتن پس هر کشوری ما بگیم میرین بازی میکنید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/27973" target="_blank">📅 11:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27972">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqYaGZzNMcb0feWhjPsCCgDf6_dEJ5v092c-ctOGq28iBvN64jHCdHLxjsJgqUpM9TYC9goDjvEQGYXGUAa-BieHnM7s8wVOGHcGGN4SQdaB2dZ2scopHEQJemkb5II6MOGlV-LScb5Iui27E1P_qibLSDFzes9M8y1o7J4yNodE-tkF6U-Bnv-ZTy_oLmGJJD-v7yUOkCIT7m2QmAg21xrqqsPVP1x-XyQkgNPjxAWGCgxEixAF1dGGwbp-S8KqraV-Qk5PH6t1rcpkBvz84HsXp4LRHL9EgbSc48RAAWEpMe9L-jI3Bpx1rCiwB_bR71l1NOcyY-uDLbplV-Nsqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ بعد از اعلام رقم دقیق رضایت نامه محمد قربانی؛ مدیریت پرسپولیس از مدیربرنامه‌های قربانی خواسته تا با باشگاه الوحده امارات صحبت کنه و رقم رو بیاره رو 900 هزار دلار. سرخ‌ها آماده‌اند تا سقف 900 هزار دلار هزینه کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/27972" target="_blank">📅 10:56 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27971">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">📹
ویدیویی‌بسیارزیباوشیک‌ازجشن فارغ التحصیلی دانشجویان رشته علوم ورزشی دانشگاه نیشابور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/27971" target="_blank">📅 08:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27970">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqWJbrdWFOqngNw4mZZUD56vSI_kEZwDxUe1quUKxnyCZiANXY-ZfStTCYrm-rhMYxOMoLtfQhwAORk1uQqdOuDoUwCfjjkVgR55-IXMkN9WnOcCVZsYOxTmP49AfMQDODwyiUjKdniuza-9cmHdOEeMY-Wbtz78a90NzRykR7fltunk6GU0lLdNZ3JDzBx6aK7MernemSXi-ahlUqNwzL7VQMY0zYTknVjjgP-PF2P8KdoHr1sJ11lJqAk3TvmcY-diXs8U1ZeBut2JgdzixXFUqB2BVnnyd7VbAlJHdnIVxAtq1WNM3irJiGm3rA8yy4ptJGf2Ai1w9U8KlhuNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇦
امریک‌اوبامیانگ دراولین‌بازی‌خود برای دپورتیوو لاکرونیا درهفته اول لالیگا برابر الچه گلزنی کرد؛ گلی که اولین گل این تیم در لالیگا پس از 8 سال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27970" target="_blank">📅 01:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27968">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwkQpD_RoU2nNINjpEbK44W9NKYHoBSmjMnh6WSZO9hbTDsyFVYhjr5yOdLFofRaM3-CCDCoyV71bM4Wga9ddJmsCLXttECmp9xoETyF06gKAy7C7yN__43PmnmyMft1DEnsfQdt0Huj1Pftgwdd_3Z-i_5XgAYj0AZxBLqfRp34oV1RahuMOlwrSeFT8wL1WAyBBBGyJSreYkZXW4UPLHBexiHuc8PeWGw6nKae8j_5ObteyJpt1PvtnxQQBE5mX5pRQ6Hgn8qn5RpFD-_Wwd4TYbyTeOH9NSBGxQS6xmX_PtffIJBf0w_a4cwfROfNlD-z_9Q-_t2F_h0ioBEDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
از مصاف سخت آبی‌پوشان بانساجی تا دوئل تراکتور و سپاهان در نقش‌ جهان!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27968" target="_blank">📅 01:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27967">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwGDCxb-9-YD2h4jXdTjNWtJfhbDfAM7ACHKUWeACvdMl9o8NC8oG5Ysgf6JLRvNAJGi8ZNrEFfO3LXO5UQlAHOAfIo6vixHGXALvbLO4jb2oFy-dRmYEpUmIJAcYJsjfoOpJTcgZ_yygFrFOIfHiv-a-ABXTcuVszM8S8Im54OjOFkRX2AarB5Msr14kkemsdiSyqiCwYpdboq4QhLWtquXdm1dfAOBGMcUKPIqRErN7bsjeDQ_FMPk4FGFva80hUHtbNd1Scxg3ZTR_z57WKwFUcebegKB9QxI68U0rrnuu-eYVT-iyxWCg7Woad2sTl44ovazYo1MyjfADp1wBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌دیروز؛
صعود بی‌دردسر و راحت شاگردان‌اینزاگی‌بادبل و درخشش‌روبن نوس پرتغالی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27967" target="_blank">📅 01:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27966">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT4lFpNdJh98g2NrfZoB5qMkkgwNn4Wl-NfK12U-6NbTv6Ew3xeyA3zeca-jbfxuqZbaxoyo7dKxi7fZ3V_PvstPRY6ZJiXBdPfHjUnKDrQKRmryZbJ59agPLNKvPnZ7LMaVaKquFhGHytb9FCwdZDr5t6UWyUykRcjV_ahIqaZ36FtWHByqDbF3aCCIhGyQ9vSEJGdDL8Io7glxVnqnh6-O4RKW7I6rNUgzgFMtB6dUPyhVVg7pE9oTrKzJv78k5B07j9BlTJ-ZERNF6p0Y8sqweHEGsQsFtzJLI3DBFFKk-__l7qnP5YlZKW1nD620AlBXTZmm0YdRFsXnCNcgGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
ترکیب‌احتمالی‌استقلال برای‌دیدار فردا مقابل نساجی مازندزان در هفته دوم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27966" target="_blank">📅 01:21 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27965">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PUMU8ly2fVzLtMOWzsq69rGB77YqCQl_3mMdS1N-Ofmo1zniwx0z_T9S9lR3Msrx1vxUs_eOGkn2-En5PEVC5jA2IAbnYGgvKvX9_fnEuGKrPNxp_j2gssbfYSzTe5QE3L8NQDinfMmD2F8LSu-3XDrNVJeofCeNZnVCDr0NIb2eOQlvqsgz92jLDv-rFMJhicV7j6tNWJKIaL8AE4sLahGW0gEt_q19wjViZOyhqaCfmw428sbAJ0LxRn5jDwPvmSPdJM_xvNY8IdagWiXAMcnVATl5mqc0GKTxpanFDWAOLG2HRHa2k2xwFVM4fFIN-jPUYlVEyEbYCPP3YMLQUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال و دوست دخترش در پارتی شب گذشته؛ به محض اینکه تمرین بارسا تموم میشه دست این بچه رو میگیره میبره پارتی‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27965" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27964">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
🇺🇾
هایلایتی‌ازعملکردخیره‌کننده رونالد آرائوخو دراولین‌بازی خود باپیراهن‌لیورپول؛ سرمربی لک لک ها گفته قطعا عملکرد درخشانی از آرائوخو در فصل جدید رقابت های لیگ انگلیس خواهید دید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/27964" target="_blank">📅 01:19 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27962">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JeMwBI_-ZmQK9U7rGCs04kv7MFgeuc1eGlul61d1TQOjY11iqTZh8eW3DOtL85Gy7zHe3cnV6TvxGDsfmpzSqzMSP0sWlAanlhnhZuLZ2dsFeLgSB-qmFBEIa7njaEH52nkEp8OesYZbhh26Or2r4fET3XZkrfZzSbDbVX51p8i0ktpufQ-e0MUkp8ZvzHp2nRaPN3JwYCz90MXzsED7g3zjbyp-gkCS29idLS6IVb-7JsUK9nlcPefgJjQw04yHpYuwlV5GS-dXaGmhviOjMqmmY6qP8Fg-KwXslEfFGJsLfp4e179o8q31ZoSyjv8NbGuG8VIwbJcr_cD5O_yqIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
یه لیست دیگه از بهترین و خفن ترین نرم افزار های هوش مصنوعی برای‌کارودرامد و تولید محتوا. سعی میکنیم که در کنار اخبار فوتبال چیزهای بدرد بخورم معرفی کنیم‌. با همون گوشی دستتون راحت میشه بهترین درآمد داشت فقط کافیه اراده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27962" target="_blank">📅 00:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27961">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Txryor--4KhzlfO3ShOPyMiAiKdtB0dq5hrTtAhGfulGtOw-ddIZ1Je-bOi1luvUPHEQEyxZyyPLGq5jELQ914Awe1cs5PAtwJjXJV9kqn-E54F2XNY-gc7ZRueN7r1CnCqsboRgIUxTgFA5zp9D6Lt87hlore_fZoyKukAS8zy8yplF1mQH3p_CmY43_nzjkRflzgbk5I9yJlwU__UgnUhzPx2JaxnNZR7Ri1TnynAJwErg3Xe9j1PON7EBgSJg3nta3MQUlo2cgYGFcT3_Ek95pFz-HWNJDr3KopzKuRLSW0l4wO93Xa-Y7_QLG1onM9LC020dwQl5V7OVFZcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قرعه‌کشی لیگ‌نخبگان آسیا و لیگ قهرمانان آسیا 2 فردا سه‌شنبه 27 مرداد در هتل حیات، کوالالامپور مالزی برگزار می‌شود. قرعه کشی لیگ قهرمانان آسیا 2: ساعت9:30 صبح به وقت ایران؛ قرعه کشی لیگ نخبگان آسیا: ساعت 11:30 ظهر به وقت ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27961" target="_blank">📅 00:24 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27960">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOHoq4kHhLWVPlZ3xuAtF0VaKCGwL7J5VX4TXIfWwnGBrnrCWe-pBX2YOBrYz2qSI-VQ7IJ_5tCSNIpQfJbVbhsvU6oT0uhHZEQSa8-kcz0kBSG34NiYPH-ACMCYs8N-ok7xF7ETg6QyAqYuB7p8gFEDS4KdAjmekmvZoS_4CUoESVKNRqtOxBCnPugkvLmpke3z01auttWPnt24FOaLEaUywYNiz36Ocj_z24alAF2uBftbtum1s9PdEQ8QbQjV0XBh-VzbZ43lNAH7ce-MyQ_-Yj-4nd9M9XpSqNfK0M4H31OtR_fc580howLq3tFBAplf37svLmZYHVQPuPKKZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🇮🇷
استقبال‌فوق‌العاده هواداران فولاد خوزستان از رامین رضاییان خرید جدید این تیم در فرودگاه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27960" target="_blank">📅 00:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27959">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpoFC-xrC1wqCbmkep7uhlNeHtwBelRkseBO8XE4AOflQrIIontT7HfF_2QtARHtBJSYlDzJk1WFlXkOa7yegNRAzyDYKt1Nh-aJlA8anHEKfnzDZzDcIgRwPYGaUJSCxe8mdXkReI4zCSTjQyfLUmcvQ-2Z2AI6e3IHBR8-voVxpvNb-rHUgFf72YgtutdTulMxrhoD2GE9yU_2fQGFS52ud4tNbw7g8H3qJuaj_d1ktlZzLx0GeBU4-ce6kR3Xiy7Opzl4f6uHbgbnpC5ME8hqfRJIsAK6AKbc0zvzFmsigJSN3DnZ7vdTldtKrzTXbT6lHubC726yAeNq6JGm-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت های لیگ برتر؛ مسابقات این فصل بسیار فشرده برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27959" target="_blank">📅 23:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27958">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ea8a6246.mp4?token=WQ2ADorczFMq4JS1cPj03xK5GR6IZLA9pdSkqvECh3pwcEorgXj55ujWpJagF_-nLFw-pXMSroYvJmvthHV0saO2GpFd3ltp1SaEF4ZB85lt4MLSrPteibxNFcN7vc3WqqkAG5A-0J9FRFIXY7gO5a9TAzdmiYst6RC1_4Xk6oIXVaxZ0oY_XZXuKK5q2eNUWQrn1QJdMPlrX4z6FQw1VfCVkv3y6LqeZkHway9Aj0l0RUz_2NvImizKceDRC_cg0ZgGEj0DrwpUPGA_FhPxkS_-D_AJyxCudV-fhrunDkTUJi-aNzljB6A7_vvxy7hoV7wSyKcxkHvjaKDBH4RR_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ea8a6246.mp4?token=WQ2ADorczFMq4JS1cPj03xK5GR6IZLA9pdSkqvECh3pwcEorgXj55ujWpJagF_-nLFw-pXMSroYvJmvthHV0saO2GpFd3ltp1SaEF4ZB85lt4MLSrPteibxNFcN7vc3WqqkAG5A-0J9FRFIXY7gO5a9TAzdmiYst6RC1_4Xk6oIXVaxZ0oY_XZXuKK5q2eNUWQrn1QJdMPlrX4z6FQw1VfCVkv3y6LqeZkHway9Aj0l0RUz_2NvImizKceDRC_cg0ZgGEj0DrwpUPGA_FhPxkS_-D_AJyxCudV-fhrunDkTUJi-aNzljB6A7_vvxy7hoV7wSyKcxkHvjaKDBH4RR_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ مدیربرنامه‌های محبی قصدداره بعد از بردن حسین‌نژاد به‌پرتغال، محمدمحبی هم به پرتغال ببره و نیم فصل با رقم سنگینی به ایران برگردونه. فعلاسر انتقال حسین نژاد به ریو آوه 250 هزار دلار به‌جیب زده قطعا سر انتقال‌محبی‌هم 300 به جیب میزنه بعد نیم فصل‌ 1…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27958" target="_blank">📅 23:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27957">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0831d66706.mp4?token=XY8L_07i5Fe2hrlh2W3sVwzvRwhSeF40hBaJYXxyq4Pmm8abLJsW7HyFRZiH651f4BedsK7RXkMp7lHDC4X9_63aiePinGyNLmUafsSd82p-E7fLWBA3YiU0CBgPlMT_UYwG-FKLW-seiBdEXOztdbYOHXbo-8MbASZikF8llxRU-520zUHCdXRJZ1wC0rZxYxFkXZCpIKRG9aXuPFaqVrWEfpkBorRqYxULWxzIV4A24y7g1Op01ZkE7_DqUGkXIgqOg0gfiqK3e35kkSfGVB1CoP5nGjjb1g5X7H1Z6BlahyxXUIL7a8v8D2USxqLgpHm-4BGMKj8aAqH_iPlqO3Uf2o1UQwN1-ZnT4AMTQdlgS_aiCl6dr3R0yTiu2Cfw_jSxzDPINzxhwFHkiMpehzTmOsXaRPY97IPtJ6zIzfyJIZ1p-2W6wMEGc-EM0rQCv46Fmf42RhRxnbPhTquWb--N9JBCTGOzO4ZoUGsge-GEqYtuZbT2Mva68EqLvEEvuse1kOtfhXhGL11SNe4kgmZB6QQa_upJTIP1MjPVMMzUzEEU6I17lc6I_XFI-jgm-H3iEFOmFoFR3oZLp9veyawWq5MhE-ZwRzlCVOEF4Kwna7h3i-hrBR2wq3JszUP6NShQV3T8imqlkfmDF6XME6DOGHLQeMbqNvLKGuzFtdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0831d66706.mp4?token=XY8L_07i5Fe2hrlh2W3sVwzvRwhSeF40hBaJYXxyq4Pmm8abLJsW7HyFRZiH651f4BedsK7RXkMp7lHDC4X9_63aiePinGyNLmUafsSd82p-E7fLWBA3YiU0CBgPlMT_UYwG-FKLW-seiBdEXOztdbYOHXbo-8MbASZikF8llxRU-520zUHCdXRJZ1wC0rZxYxFkXZCpIKRG9aXuPFaqVrWEfpkBorRqYxULWxzIV4A24y7g1Op01ZkE7_DqUGkXIgqOg0gfiqK3e35kkSfGVB1CoP5nGjjb1g5X7H1Z6BlahyxXUIL7a8v8D2USxqLgpHm-4BGMKj8aAqH_iPlqO3Uf2o1UQwN1-ZnT4AMTQdlgS_aiCl6dr3R0yTiu2Cfw_jSxzDPINzxhwFHkiMpehzTmOsXaRPY97IPtJ6zIzfyJIZ1p-2W6wMEGc-EM0rQCv46Fmf42RhRxnbPhTquWb--N9JBCTGOzO4ZoUGsge-GEqYtuZbT2Mva68EqLvEEvuse1kOtfhXhGL11SNe4kgmZB6QQa_upJTIP1MjPVMMzUzEEU6I17lc6I_XFI-jgm-H3iEFOmFoFR3oZLp9veyawWq5MhE-ZwRzlCVOEF4Kwna7h3i-hrBR2wq3JszUP6NShQV3T8imqlkfmDF6XME6DOGHLQeMbqNvLKGuzFtdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟠
👤
پست جدید رامین رضاییان که هفته پیش به خاطر عکسای‌لاکچری از مردم ایران عذرخواهی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27957" target="_blank">📅 23:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27956">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVkF3KsuqWNEx6w_qWKjWmfz5Uag_BUXLHKImvyWdG9whveNTlnxEDjSs2ntyNInpoztC_4X3NDsnpMzkfcCZmUOt4sp0XdwWWfK21gTscFF8zuZOJV2EobvKqbORVrhyi3AmhmBzyPCq2qRhbeEe7DcY3K6-DQOXiCSntrDIfa5GpPVtQdw3UfAm51diba6LprzxcTlda7lYrKOdsOGaaFSBjDOx87nCYO0c0KFXCjI5WwQ0pyNrFCI7uwY68tZmsRPWVQx957Xv8kmS-ABxY64lQ4rU14taaEkgR2ESorTxqkcqKLEy-LAD5eGEYap38qn3Fm0efA3cuoDTIkgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علاوه بر محمد رجائیان، علی تاجرنیا رئیس هیات مدیره باشگاه استقلال صحبت‌هایی با حمید سجادی وزیر سابق ورزش و جوانان و شهاب الدین عزیزی خادم داشته و این‌دو رو هم به هلدینگ خلیج‌فارس پیشنهاد داده تا از بین این سه نفر یکی بعنوان مدیرعامل جدید استقلال…</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27956" target="_blank">📅 23:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27955">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1JDyI8vwhRVNi-tK5g0_JHd2_9pPuK0aG_WML0PWh4hEsnoO4SfpLro6-Zb8ZfcPkEq3Pnj858LVzj3oNXctyLlWGmqv4JYJDbuF4sdc3JU-0TYeMa5w1ms43bWkKRKwDi-W_wDuoC4oaRnGpnNLkhbXNAgyjoEoIp9l7e7tkdL95RtnynNEkUh0a6N9DyOTi6peb4G6qeVcg7yB6_VzX15mHyBLCwJfN0M0C4AY-Bse9C1s-S81ioaA6TwAFdPSGRwfQ6meKfE5_v8DuwKNzjsi0BIPbA0Q2rTCOEV-9aExI8dmjyDmKiiOUigBlR7WkQ0VWO7GFHQQ0aT4p8TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کسری طاهری: از پیوستن به سپاهان بسیار خوشحال هستم؛ باعث‌افتخارمه که کنار بزرگانی هم چون سید حسینی حسین بازی کنم! واکنش حسینی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27955" target="_blank">📅 22:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27954">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmHyIESQ8WhkuLi-dPXFiIzlxFaIvOJQH0uAaMgraDFnbi4IFDjg-92_oW5xtNdEDNBiCn-hVajxtpog2OFeW4avfJ24twT6VZpiTf8oXhUe6rvoPt9n00YBcpRmA7ZNQ6Op1bbMtZAaLXOMsth9XpPY1O7x1O2qarQwiCpIfMgLPh5vfTin33l1VES75I1kiqSmkCWG_0sFn2D02Vm79Tvij4AlYspjNrkRnsI2zcbLtAOW2Fgwph7V5smoZrn4ZaKy5tJn5H7zuUewJD-eZlDC6h0B9nnK0PR0h7HUFXhymebzOU-OWt6pIR_6usKwQjWAr2-1vpwkey-knYwjxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
پست جدید رامین رضاییان که هفته پیش به خاطر عکسای‌لاکچری از مردم ایران عذرخواهی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27954" target="_blank">📅 22:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27953">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eelGb2Y7AT2T_Sy-PXNH_NZMajusiPHdZBC20tSZ0J5FXHINNet_MdyPqN6r6FWTn-Gxo5rkdzOcMi-WJ8Yg8r97frDQSyCKq9J9h20FTmX7y8s-QUsfOOA9dqvKIu0RshjCXSstn62OqE1BkX6DtRqqIxkQup7_hlBzmjDFR21EUQ7tpVyNrD9TV6mLJvTGmYrpMWNZC39OeJ6VRyuYojEbsRY-bTDUQZiwGYSkwYJ5Wkdfh02qlhsr6ZuS4iIHOgwLhqde9lRuZWKiNia8POEkjlSEdJ-27CwvhCZfl6AV9LMP11BYD_P4pQzpZetDX0NoKtHXUj2pjekuyTYW2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری بعد از رسیدن به بارسلون: با پیوستن به بارسا بزرگ‌ترین آرزویم برآورده شد. تلاش خواهیم کرد که امسال قهرمانی UCL رو بدست بیاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27953" target="_blank">📅 22:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27952">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqbjjBGcdhmb9CbI9s1fnjOw10I36ZqVKKelB87JXJR-62cIcmk3cbskW3pXxnPx7RnSpJ7GfvLaYW11ks7HrTBKtA2VzS0NLm4_xhegqQnmREXrcxTOIfuZ1yPQFlLwK_2IPs3ed4lOpznf-wtT8D8lNyn74EEb8l9XTL1Wo39HonE9zPWBqm_j9AoVEHffFFwsamlJBoCJSr25i7hGDZm9UB1YxWw_o0SD4U44XD3UyqLEAbdv7PApN1sAQsfgpBr-FIpWK6fokRQLWIHiUjhWrsHgC8o7qXbXTg9DBAkqt-JSZ7EFGYtXU7TVvOBbVZPHHiZwiazkNAJ3DxlW3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام دیوید اورنشتاین؛ باشگاه بارسلونا برای‌ جذب رودری هرناندز 30 ساله روی هم 76.5 میلیون‌ یورو به‌ منچسترسیتی پرداخت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27952" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27951">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koWBWbU5MMcii5L1QOMo6jYqHI5isvuEZos1y-czeCBsRPANijsJNkmDODgL-ajAAGTsnkAdD8FxbcJOv976c8BKwPQPvmrLO9-oKo8tmWpbzu9ONpEaSxsnSViNUVALnyIfvv8vI9rfN9ka6SqolyatSUurKQxUpGtDLOpZ2kaaZtkUBQoue61Lk7RrJOvQW2EQrN2njfH5qZ5PNcqkr_8pnU3gi3kg4qTA1axGsPRoeTI3-AAGDA0xkM_Uto6IqW1v4v4V8A-xCSF_HtyDVmP19VaHlVE4lls5FFGkZq9PIRKsWfyzoJ1g8L3mKbNyghfksqXxbZuKHm-hsNtgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت های لیگ برتر؛ مسابقات این فصل بسیار فشرده برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27951" target="_blank">📅 21:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27948">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZxh-ZGBg700y0-pfCf4nP_riMXAt_fCQT4Wwcbq07Subvk76z2lYxx0AG31RHTx8BXU6nWelBykApm9_e3B6N0YXzFtW0tviwoRvq7F5oONV8SpvljulY6n2BK0PZobDFXW6Sm8JZ5NAdD5nLNZteDw1NUqBVF4ZHCPOcEQfEX49Em3vweSIIheExa-QBBs0AVxM4jVafXe3RhAhwm2SzbJ9ohIVcDpPeusw-ZZmWtvCTG2SANQE2_GncUM13adxPgEPpm0iV09bIOSsuzwF9fYmuH0KY1jexfO-k2gT2Cg7QEDl4RDjDpGCwSVj8-865h1kjldGl-90SRwbZ6prA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pkVeF0yc0SBwZpSE9o5LcPHJS3gtcxSzlcKj_xFDWlmnNGGtcC164QTTrWb0uGYdSFKy-5gyquixWzGnTrEMdRecOky5QEjgvvadEiNvAebNLztsljyWaY6IaFUvoT-wgUXQe-3hgkpegl5Jklaqx5v0zf-HAJ_jW-bU6UiJGnD9SYjiulvTALS62EP_8wyUZS6ApvWx2-9HOipX9LoadX04tCUJkm4rbLfNe7GVt5wYyHeEID2V89hluqTf_OwezeqYusAO6cVUpXY25Rbbw67hLn2Hz-8MdJ7X3A809yliE2O8lpdXdt37aYGJZIOU751tDtnIRa-X7Bh6r7_VZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
کیلیان امباپه بعدازچندهفته خوش گذرونی با دوست دخترش با این وضعیت به تمرین رئال مادرید رفت؛ برای پارتنرت‌غذانخریدی مشتی؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27948" target="_blank">📅 21:42 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27947">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s5XLIGo4bD8X9d5DhFHLEdYza8c9QJlQIf5D9sPG7E8IsGgaqbJwJs9CvEmc6zBlmaLsQC2uFs05eBB97P7db4kqudvR58nw6FWntdccewNBFwHQfbrFyeHVtIelF5QvQxkET7Q-ZnSWF-KG_McqmAZ8zS8gPL_5YZL3Wj9ev3ST0LDDynjIyk1_oap8fv90MRLqr72P_4VNkJep_RE69e11Y3k4gncnxnACLEdEXGAx6lZgXCVmf2HW10qgP_nbqg6fOvCmCGeGgPM2iMujNx51pJEcp5YJImUjv4QpP5OmBYELpXPP6LJAp0x3tV-3ixjQp67lEG6T1JqCZqFapg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تصاویری جدید از دریا بنگر دختر خانوم 20 ساله محسن بنگر کاپیتان سابق باشگاه پرسپولیس.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27947" target="_blank">📅 21:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27945">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5xw9UfQOgngXyB5n0oB_tZtjZhhApIHRWJ45Zw_AYIq0LKDLUw6bFRdw4Qrj3G_E7DdcndJ1JEmO5ie34G_UEsktwRyYC9puzGLD8CtPBsXoZK9haU4eixNA0sPj1OMte4HOKgAfj11rcWF0aBKyOfff9uYN9RRJReDVh8AJU4R3JAXn7YczyJspHlmEpWB1kXdwt6p4Yo_l5iD3LtWSkvP-xYkkH0__8-UA5dBQcDVPIze49Di9jj3xEyDkaAzoLrPMw-RsDOh06APnpdqAWgT3L4ERV0Z_erS7GThutg7_wWkm8tXFGfqR5PWUfVl_AO6QlTjIhA9w4ralxNXLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtSFLSNl-fjj7l8SKPk6R1d5Ckij4dUo0Gmk-Fb3c7m3AssqsQE4dhOabGT3e-oB0v3iQc6sM931kFhe6Kz3hDpIUeyxRIeNPzSHgcKzNp-XdyNLsaxuSnmpq5pq5160fqsxoJsb-lDFGt9zhAs9Pw64ZoCLl9neWFYpasCaKh4gdxBBbreb2nmbviRrWuXIo59eIMGi3Fc4OPd87yfqCflCI2fsIvGvPaxDzkAy-v1mGI6kfBZ-8YQhild3JAh1GEuDf3iO80RfkPIU75quOE76aJ88WRoiFu-tntidEHt_90FRE6pv8k2IuSX9vHYKxtl-fsMmBP02p7vHlqxadw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
فشار بیش‌ از حد مسابقات‌ لیگ‌جزیره با شما کاری‌ میکنه‌که فیزیکت از این به این تبدبل بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27945" target="_blank">📅 21:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27944">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvgBHzBre1LIk9c-Eez_hgFUp7H2IXZUI7MSIxVwIYAxGUE34tkqT4YtC66ngLWorB37FMqTtsUtaZ0vyY7cRbC1OowZaHs36e10XIxMRrYl_Mmam2FbjjYkXO6XmKsVku3cdmt-NHqR_xOU6OWWgeFToix5QUNcNhz1braxuCW9eax3u6L3l5SBOPyk2zJpYdSe19BICOi00WIVT0QgsnYzKeFjrO6av3iM9dsR4J-Bpcdy0RUZTms2cm4yAZ2K563ji58c0x9eQxB3h9rgQTZz6HNNVzw-Fmv41tOm6HdxnYfkpbWiSEe4v_F71GE9nEs4YIgl_DiGrIIRckA1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه الوحده تا دوهفته پیش حاضر بود با 700 هزار دلار قربانی روبفروشه بعد تراکتور میخواست با 500 هزار تا بیاره که مخالفت کردند بعد پرسپولیس اومد گفت ماحاضریم 800 تابدیم یهو این گلی که زد و باشگاه پرسپولیس هم‌جدی‌خواستار جذبش سر این قیمت رواعلام کردند. قابل…</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/27944" target="_blank">📅 20:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27943">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDw_TT9xIrrcgb3og_WGP5PyKR9YCyGiJBP-odkN7NYrfpjMnJOHVKL2hwN9bwFp9K435tfMLOF6eSQO39wkywOGjOo6eaJZSjkl5ERGPMdNMV7teHlyb-XW2Hn1Xs5g1ZMriNbK3WIX9v6KYcMjvn6NFCA6SQdLfYzJn2-YSdt5tWSGPG2sRPo9w-tYcOs2Abxo9STj_Znxo6p5jsf6TPcKdu_SItj-vruhyWRAlthqCq4TqkeVXqXBtFHiWJ2SG3gQldhFIneFMxzCqYw47TsR6Ovyr3_7qkQnH44CsTuItE3zEI2QEwdDZF_x3nB0EFGqHS1dqBV5bOI9i5u8JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شش روز پیش پرشیانا
🔴
دانیال ایری مدافع 22 ساله نساجی با عقد قرار دادی 4+1 ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27943" target="_blank">📅 20:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27942">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuGjOPrmCQ-z6mnvdyln1yfpqQXI5hMtXy9BCaGcfnbSCO4Flb90P9BxMvXCJYkE6cc6CxEKqijpv2y6slcOn_CqMgJMDsGxPhTh1LG03D_NfhP_7N1lMIbMkZj2RzL--jEOpwR2oShISGMBuaJjq3r2A5nMgEqWaizckFwokb-pOFIq_7DSdp0a-i4TYuI6zciVUrzHH1qWbBpQ9FX3geQiXxS3smYV51hKKELtCaW4OnZQK9AuRPcKQgM-H6dLz19sP-aBso_ghe7NRdsCYeUeW0LaeaCDgBLVZ_qhlOuiwh_eM8lL0_QpP2Nz8XlqCu66UaGVg0_zCnxrXwsWMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
نشریه ESPN
:
با صلاح دید هانسی فلیک؛
رافینیا دیاز ستاره‌برزیلی بارسلونا بعنوان کاپیتان اول آبی‌اناری‌ها درفصل‌جدید انتخاب شد. همچنین شماره 16 کاتالان‌ها به رودری ستاره جدید این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27942" target="_blank">📅 20:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27940">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Lh5C9UqHhfk9fjAU60h95mKIyUGQeCmeESU8HFaS0dtKIXCQpPilz19VxUYMhKwcLrYq9QjU3u-jLwTRD0MueFdddd3Q-Sx6dbaPgfnbOpaOXxi-Lxz72T0o1AFt3h758T8UWexk9SmFw8_6q-3SKdaUBXxQBS1Anz2cUboaP1qBGJfsn6P08zzOLOs1ST9w9Y_7WMDmQKHKzzNEbil0QWJ6hFP7K0SR38-twoEpsS2LYX3mKTb9X0YsYUf-LjfEopwGwV3SerpJNoyrECjxu9jZGQ9iZ5DRYWSo4Cruj49P9SRqmJXPZRhXWHAZGQJYuUIx8XdH34Gfpn9RLGLB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRyUsN0u-uBrWL4_xY1iLzZlSYaBb8YP27Ho_UaPSiKYtpy81vHNctl0PbT0xkdgnYAuNDNSzgnWvi2Lih4-B2yKEUGbfC34rOxJ7H5skrfLYJq1p0FlnXHtlISWkl7PFhSogKzJv1Ap4f85r_pazsJXs7Zzvy08zmM4WCfV2D2UJZzyXODBIKvxqRDdcgn_sBwbckaquCgibLmMCRt7uUzfPBpgOmDKEXvf9_RbAf9WJWPOI7rR0xDMX-58CxZ2cKZgEBjq4e6011ajiJBxA7gI7Wq3kZ8MsoH9ys1n-E3gPJMEuFSvs_24xzct1vFBPdWtwjvnskOjeCs326ENmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جالبه‌بدونید با اینکه رونالدو چند روز پیش با جورجینا ازدواج کرد و ده ساله که با اکسش کات کرده ولی هنوز عکساشو با اکسش از پیجش پاک نکرده و گذاشته‌ بمونه! شما تاریخارو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/27940" target="_blank">📅 20:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27939">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtcmgPJv7DGwtYC2LlwQ70xIlJdd2lb_yrxPmD6OmOIbyuv1lE55z_yc9Brv6fu5kZHPZJjC3Wa_BmOdWXgaW5tpaIDz0NlhEHz4xUB8Q1cuFR8COn8t9H1wt-as2QW4UOpTmaw1SKHttuCCS1Xv4YhZcZLpvya1CEoXllhkNOIEE1LulGAaEFa3P3tiYltGcZnlFzFFaJjAQbZ42v-_Z2oMQzPe5_fz2fP9p1eDEjsThQD55mWxvb7AQ4qQ-dxYoYJql3hoJiFcWJeSU8_3c0_xTX-2wvkdKFkM21aXXP3lkjR8ohHqjR9gUYuCla1oNSjbHKlASuRwqjuZKBbBxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27939" target="_blank">📅 19:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27938">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpDJfMx5bhFDhiHNin-XZyK_dc5wUR6WwKzbX29wfAOPylELmKIgS5XZiGyIAxoJ3_1mOOIZgnz9KoaumNOVS9vBXwwedoXeTjvR7wX3dff7aseBuuZdHN-kABWZvMrz7MfXqWu3H29gdYOyVTRU0uHoYK1a4juuJBpaSnfpZKoMMnCzZjJGTHvNkjReIMGGoBnW94mud_ZfD8xMM_cnrPRtU_ge0ZrfBVDIVIkEhcxpX7vFbpRSqt-L4f1LhThqnQBP9FLQmnqF0E1oCcgnn3nOoHnAQEsxIN6Kf0FKmjINYQGAVGvbYjBu6_VBqGD7u0FVBcMviWK37z0Q3UY8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
درحالیکه‌اکثر خبرنگاران از پیوستن انزو فرناندز به‌تیم‌ منچسترسیتی خبرمیدهند رومانو میگه فعلا هیچ خبری نیست در ضمن سران چلسی انزو رو 140 میلیون یورو میفروشند نه 120 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27938" target="_blank">📅 19:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27937">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEvWSGFt05bsO466S718uf5BZF1Vbr6VOZrfYS6Bv4aR4f-jhmXgzNnESHaNAzwPZ1ubwAA5pYvkbd4ceOnLhWmc-jzYbf9mwzSRwHeBQAOkKscvPiLr9b-OR1Bl4Qd2JbTaAqVBdCfh7VhH1Ox1x1Gj4hsBdT0MWfgzbVZ8XwQZeEE__L5av4BDBBGRovLHDb3QayxW_oQSXzkn06FKSlndJpJfGXWf7xh28N2xkNXX0vlvosmjz-ug5Bs-wx_MHIG69qXdzSm536iTh4D4FDar22qPYumJwRti4VDl3P72Rj3T2gUerDvjN4IGL5zgMe-3CsSqIa0pZbcoq-bLtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بیزنس‌به‌سبک نساجی؛ یک ماه پیش دانیال ایری و کسری‌طاهری روبا1.1میلیون یورو خریدن و الان با 1.45 میلیون یورو فروختن به دو تیم پرسپولیس و سپاهان تااین وسط‌حدود 350 هزاریورو سود کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27937" target="_blank">📅 19:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27936">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49f3e1492a.mp4?token=eF5YZbOw4emRH3wPv8OeAqummOc36yOxUI2MryLlhCbr5sjbDnIsz1IROkLnNqrNCF-bJ0I2euno2mHo9OXjagHLjusKtYqBYDlXT8XAl4SbpfDh1OnqUXhfsnfE8Osc656tC9SweQumlO8Wr81YvFxvvwnwa1LaFHWJJ1WRp4HfQTgjW_SlaG1IFlbSCfc-AgpJTLyFLOEOaRGFscmYCf4gPAO0gn1LMbLzhd2R5g3wegGWCMIq8Oww5vAMTUA-Ju-wS-23hlXEEiwKZVT4l4aFZQ1blSpaa_EuUSxTDWmBqocdFeaCDYKC3ky6zCfamMVkZE7EIfE1eE7qd_q5wy08o_d1fcZIyxZdkOZUi7LI0gCVfYHTtRqSQ11d7YCczJTvgqTNjZwTzZpcQxS6S-roXfbbsOo020WUsfI7Ys3f0K-eYfI6S9W576Oa7wV9jQjOwTN3c9tLRs7B8UyWJIRjZx2uysQ_RvqFwtMB-tIDCCKSUHMdVMGfzjdWK93AvvOS2ONJNgvivM0l-6EIFrF8aCvpi9RdF4gKMxiqMO7njfXFs5QKZx75rS4NL375zAHOqS_4Q1bCcbHR0IQMHEVgnZBYCuoSzpMsXokxDU5zRy1NCMbUBYhkIYdUoDIGxpWfY3_QED_YSygImbgNApzQqI6361MLsRRXwNlWhoE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49f3e1492a.mp4?token=eF5YZbOw4emRH3wPv8OeAqummOc36yOxUI2MryLlhCbr5sjbDnIsz1IROkLnNqrNCF-bJ0I2euno2mHo9OXjagHLjusKtYqBYDlXT8XAl4SbpfDh1OnqUXhfsnfE8Osc656tC9SweQumlO8Wr81YvFxvvwnwa1LaFHWJJ1WRp4HfQTgjW_SlaG1IFlbSCfc-AgpJTLyFLOEOaRGFscmYCf4gPAO0gn1LMbLzhd2R5g3wegGWCMIq8Oww5vAMTUA-Ju-wS-23hlXEEiwKZVT4l4aFZQ1blSpaa_EuUSxTDWmBqocdFeaCDYKC3ky6zCfamMVkZE7EIfE1eE7qd_q5wy08o_d1fcZIyxZdkOZUi7LI0gCVfYHTtRqSQ11d7YCczJTvgqTNjZwTzZpcQxS6S-roXfbbsOo020WUsfI7Ys3f0K-eYfI6S9W576Oa7wV9jQjOwTN3c9tLRs7B8UyWJIRjZx2uysQ_RvqFwtMB-tIDCCKSUHMdVMGfzjdWK93AvvOS2ONJNgvivM0l-6EIFrF8aCvpi9RdF4gKMxiqMO7njfXFs5QKZx75rS4NL375zAHOqS_4Q1bCcbHR0IQMHEVgnZBYCuoSzpMsXokxDU5zRy1NCMbUBYhkIYdUoDIGxpWfY3_QED_YSygImbgNApzQqI6361MLsRRXwNlWhoE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فضای مجازی به ما کمک علمی زیادی کرده. مثلا شما ده‌ثانیه‌ویدیوحرف‌زدن آدما رو ببینی میتونی راحت متوجه شی دوز مصرفشون چقدره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27936" target="_blank">📅 18:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27934">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVeXco0Wlrz__wjZ5LNnBjjz5RdL-fYy1iDnoUr3rXYB1rV8REBhLcBofeLLvsputGQwp15OKjKJK2stFvpOnJ787ptitwbpWFAvlfqjapj38trQUGpnibvXhejaRYsqtppIt5NzsJGvbLERu9Bfqg0BV9zbMqA9cIN4opTcu-AsGQtxsG2oQx09vD7464sbHjO5t8eudMJahgS6FF9vRunYjNB9bwRJUPG9Y3PFNAu0FDUCfvgnc0GWU8DGE9aK7x3hLBuHd4gfXPlCa-g6Z07RiO5BK0yzEk0aMKpyuyymhY3JwTkPJPRaz0Bl_fG3PN_gLQy14_6G-ul8EP5svA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvpqK6IojZnPc1iDE1hot8UX7i3VUtkMmMBe2SkYG51R0fkrZDAFycqNSWgmhFtBHpCY4YqgIPM3evIWnK4BaaCiPxjtbyMavCewoDqPjAlrdbRzu5PWBY9o8B5Yd2JSnfupt7YLkTldDgoR9IuMZD1rfNEAcjjxbcNb4KSU-6g4ssQyNTq143ap9iu6Zjgct_74fkYIMuKdAt8lPwAeOcHYiLZarviCoPj1EvwtdITCZWCHFT1YBsBZlBL-OZnSkmdmouXovB5AdFwIKgbsfikbhzKTFtp78FfcrH7fHIgXRww0S9ltYl8lmFFyG5Gra26ZkYvzFvyUzelAmhJ-QA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟣
عمق‌اسکوادبرگ‌ریزون‌ آرسنال‌وچلسی برای فصل جدید رقابت های لیگ جزیره؛ آرسنال بار دیگر از اصلی‌‌ترین مدعیان قهرمانی لیگ‌برتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27934" target="_blank">📅 17:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27933">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/donH8hhgHh-LO-_Dh_uljtjak9D5_WkV9OMmfmGhTksrgR76dbWj_Mp57ZOjU2YTWGqBTlPYhGoyg2BjYVZiOeZopqdPHPBj7kEpx3yMwqlOPI3hXFPXW3wcfSgM_4rCJAQsgeIHIJI5u4eCwIwPwhQ1QT1siaoesrkZ6sFiVvKu2tpa1XrjKberptsGBT29TCBSjSKN1Ym0ZEoWurT3KYW442bXxNdBDLnK58D5ErEglqvtEo4WYCaCIsC8gf8STPCv_Jyj8A9gN61Utx4GpAWKgZDu-lynKLMysWmyjEIzKJjOUo6fsmf6hm70ESAQ_OTfXKJiuGujh0eqHBWqSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#تکمیلی؛ مبلغ رضایت نامه سید مجید حسینی مدافع 29 ساله سابق آبی‌ها از سوی باشگاه ترکیه ای کایسری اسپور 400 هزار دلار اعلام شده. درصورتی این رقم توسط خودِ بازیکن یااستقلالی‌ها پرداخت شود حسینی به استقلال باز خواهد گشت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/27933" target="_blank">📅 17:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27932">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJh7SOgJt4mn-7vqLSTe7x8dwEDWIj3u34muvq4Ws3guLqg9gQbQKNqcDDCap_9LbpuY9mVOCdPhO33STLfqCRdFOnxvVbh2HMdZEBWSLdjt1yl604Hx4p7l61-4F1PqM51-PKYgo4LftWLVwGVBVaMCUUd2O4dKC9ZEAniUsdllWGdPrQH9ecgTVrLM99T378yDGFx-nAnoVtqOIkgl8kqulVwIdcT-JU_RBlDe6JW10dvlvq-NpQpdTt-edc14yDv2RtyeOrxrn8yiX8Sb9DSKTxXsNziICt3cdKmuFG3VbDU1G02mNJ1zrwdlsxYqQY7ThLfBcDaILyLRajMKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#اختصاصی_پرشیانا #فوری؛ بعد از اعلام رقم دقیق رضایت نامه محمد قربانی؛ مدیریت پرسپولیس از مدیربرنامه‌های قربانی خواسته تا با باشگاه الوحده امارات صحبت کنه و رقم رو بیاره رو 900 هزار دلار. سرخ‌ها آماده‌اند تا سقف 900 هزار دلار هزینه کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27932" target="_blank">📅 17:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27931">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-8XR6VfRq8hrP3XLTZ0xNIqtW2uZ_nRe6QYDwipF7Xt9VWN19CDAajFoeBt4A9OmQbJRzuu00-qkLwmzg3G3Tg19AuxT11VYmWhQPnpRo34v6YSQVp1mYnGjkG4r6XoHrgmLBd-a0vPlibB_SusbL5aF0KBv0cW9qtZpsHU11RyfUzuPF6RMxKSevN_ypDErgtbiyDPK91_2Woq41ZkFX-yhqzoNgfoDoyAE8f8FAt7vehql5X7FJI9XyVkD-mTJrHBMiJcDNR3c2GhaYiSY3KDQNhjpaIS4DX6G1HBWfAFsJG4UiRt-H6jlmJ56vb_6hG9nJQu0cUw8FDx3KnC7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
دانیال‌ایری بعداز عقدقرارداد با پرسپولیس: قراردادم چهار ساله امضا شده و شماره پیراهنم 89!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27931" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27930">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN0l5t06NL2hFCq7aOLCIjtfQzUVPgVu8UGzWRGBPtMRM-rpcpvGVvp6IeeZkpM83se8yjA_2QkJlJz4kTU59LKFeLWeGNOnVgUQPpU1JK-zLFPp5ss598SkKOAV_KTivrqjMA_W0gqk-rVYmDy0axMDTJWwO3ZrShWz3gB8DuUIWgNa0GRGmY5Kz0h6IgbbMGUcWQUtL756hgok8CDnxPJnB-BpGWItELSJa2d6QxDsNhAxbOJDQfmg4RUw2ATpBiVeWhgH9WuTHM0NC4lakJtsUvqBS8Pmq9hXkZozoEuNI7aqQkZXDkKHyvdvaxqZyM57WRAKEzelUd0XzWYhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
با اعلام دیوید اورنشتاین؛ باشگاه بارسلونا برای‌ جذب رودری هرناندز 30 ساله روی هم 76.5 میلیون‌ یورو به‌ منچسترسیتی پرداخت کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27930" target="_blank">📅 17:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27928">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOel1iHmGHx1rK3b3GFPtpoxCaplF-nxiGqqRcxAIp0mtoI48tMg5i4P0NZSms1cmzZkPqxEQvW6kADsDg1Pz19CiSgMdzC371ngjXUpCaQLJSXn6F_DGkofasZ5slSqjKTwza3OGn2coToLXKDP8kkVXsnLmSgDF9uq1TbdiXMuRM6fMPpbGHYFV0-nkhEUfBs3N9qPmugVxS9J6MURhedpoyezVYVmFSKsQa5DlQcVDJmaaILK4fUyh7HbBzroafUSM6PXEy9ihIbU1RNrh-7ukfDt6xZTAOUskwzxU0HU05X24e-RstmNFee4Dgaew18WAgCQrBSSLGg8VL_wZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شش روز پیش پرشیانا
🔴
دانیال ایری مدافع 22 ساله نساجی با عقد قرار دادی 4+1 ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27928" target="_blank">📅 16:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27927">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IoIiXtq6Eypzun0lz61ZEMWuzibCCU2u5n5C_Orz9j3Ym6FqYYyIvV32o88rIuQml0_5EN6mTkvlYSeH5Dei76Oj87GJ2XeHrfhj4jeaP8MiwV2g5QOa7FGwepq-WYAN74dQCP_AUxHcWSP2NAOXxrmzrrh13_NsPFsOkFkQQaM23yx3SQNFdiYH-7PB19b0hL65SDHP0qQ_kB8TpfY97wwVqarLrletkzuwrkSoiJUHWHjXHgxATEPehid9bgajEkXu9wWLspswY0q9qgalitdcR7ZJngOGoEKPV1ixqRyOSFniFmcLuuc25QqIJZEm4FNL2t4y1rvIsEQQvIbluw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌انتقالات
؛ دیگو موریرا وینگر چپ 22 ساله بلژیکی استراسبورگ باعقدقراردادی 4 ساله به میلان پیوست. موریرا فصل‌گذشته 4 گل و 7 پاس گل داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27927" target="_blank">📅 16:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27926">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdde82e9ea.mp4?token=nDkEy6F_cVqd6mulwMv842KTvEOvqBKi7RQaGZRbX2b8PVmsVOLwu8elkF_kDDjyGGrE9cBRvpUG5E4xfTbo42VTLzdL4WtgiMdp2vJ9In9L-fSzVTZVBCHukUGca6L9xTbaye91823nyfHksMc4xXFPuGab9ww-cv9Aa6GSiHUniXlW-UYfc4i_ITXymCN2GBDaVVBS23jPRFNxLy3dlzmjdl9lznN3NfPfyD3ak-r16nbOanPjARiTlFLRmg4ESLoGxG9-XeVUZPPwzJeLfyHdUXfk440gsCJq3oSN45wxVhsl-sqFLc9tr9Ruts66SlHvs9eX9BZzqLLIl2auUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdde82e9ea.mp4?token=nDkEy6F_cVqd6mulwMv842KTvEOvqBKi7RQaGZRbX2b8PVmsVOLwu8elkF_kDDjyGGrE9cBRvpUG5E4xfTbo42VTLzdL4WtgiMdp2vJ9In9L-fSzVTZVBCHukUGca6L9xTbaye91823nyfHksMc4xXFPuGab9ww-cv9Aa6GSiHUniXlW-UYfc4i_ITXymCN2GBDaVVBS23jPRFNxLy3dlzmjdl9lznN3NfPfyD3ak-r16nbOanPjARiTlFLRmg4ESLoGxG9-XeVUZPPwzJeLfyHdUXfk440gsCJq3oSN45wxVhsl-sqFLc9tr9Ruts66SlHvs9eX9BZzqLLIl2auUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی شش روز پیش پرشیانا
🔴
دانیال ایری مدافع 22 ساله نساجی با عقد قرار دادی 4+1 ساله رسما به‌باشگاه پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/27926" target="_blank">📅 16:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27925">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnXASIOePyM1gxo231kkcN75O8FhOimotJfGMWarwuvNLO-AGVSHaUjQGAMc0pFRTXYen2BUqjypcGQT6nOHZPr4WRPEVmI2VpirKFgtXxAG1TGxfLitZf5mFIRgA8se9vX4C1mILCdFwX5K7jO98cUj6dVSsOz8vEzxZftKln7nGU47hL-IbUP_2kPl6DtBxzPP7c1S-LGLx4eUOGVtmd9lh2E02HRQKQCNNWNmu6vg7GlPUKdy23nwpWYrVDicVXc8ZLtqJpa9l2QlfnUo-dfyzpzC8sXKVHBkOCMqKfwcGoXk4ZBGRCDKkcRi8VB1r4MX7CwQvKNnAC-z4sJAdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
21 سال‌پیش درچنین روزی لئو مسی اولین بازی خودش برای تیم آرژانتین انجام داد؛ اما مسی تنهادو دقیقه بعد از حضورش تو زمین اخراج شد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/27925" target="_blank">📅 16:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27924">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enIbVivwstJMy92S9XCkeh6RtbpWU1xtnzd0GzyDxaxPrhW4ZrNCIizePfCxOGa-nfhU9GUN-bk2DVnUZQAWUd2SskK-UH4iLattQQNirm9cy2-hQ7RobBOSAUqc1H6Hv-B4VFDtEzMI9JsKy58dsaXiPBqUo-tvcZMilZx5euJdRgtIt3YcNAE45Rjq38tdaGy5bmBr3WwqMwuDsTIvj0dYZiLwOFO0hNnGt22w4U6M85mGdlFXcS_7NVuqeqvHy0QUUUDGSQnr_mevAOMQmdYNNTUCzVAG2ahP4-rmzsbTchYFOVOTps_Rx06ipa_vVxVOMZVByq2sy9HUKb2qxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27924" target="_blank">📅 16:07 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27923">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d79be75e0.mp4?token=h3tNtMCN9pXQkYGI3pNlUeCWTT75YelryjHDnRt-S566v2WAKGEnbTjyyr9fy4TtYj-87JOEZkC2b6F0uJGrEq004ZbgS2VZHuxmAAk-8VeAKOV47Qd7pb1M-kY5TkPHCWnGQgUZvR8BtCUjMRMvDOBqD8gC5Q6cQ0jPWyTxf2BmLxpcVdVSyAwGb-SiYEevtiYISNG1pkdJ03MAUytnICu6Z31lB9eh4j9dLdFFt065w7wQLUfNPru73WVbsNyQKcumjkPX1uOfigbgHwqhqTABXkB_KNvEUx_QPcgYXRahmnO9OSymh-PEdueQ6ZcNvMkK_PKcEBYKGLD_jPCevQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d79be75e0.mp4?token=h3tNtMCN9pXQkYGI3pNlUeCWTT75YelryjHDnRt-S566v2WAKGEnbTjyyr9fy4TtYj-87JOEZkC2b6F0uJGrEq004ZbgS2VZHuxmAAk-8VeAKOV47Qd7pb1M-kY5TkPHCWnGQgUZvR8BtCUjMRMvDOBqD8gC5Q6cQ0jPWyTxf2BmLxpcVdVSyAwGb-SiYEevtiYISNG1pkdJ03MAUytnICu6Z31lB9eh4j9dLdFFt065w7wQLUfNPru73WVbsNyQKcumjkPX1uOfigbgHwqhqTABXkB_KNvEUx_QPcgYXRahmnO9OSymh-PEdueQ6ZcNvMkK_PKcEBYKGLD_jPCevQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری؛ ویس‌کامل‌صحبت‌های گوهر شاد درباره درخواست‌ هایی‌ که رامین رضاییان ازش داشته: اول گفته خودت بیاکه باهات‌سکس کنم بعدش دوتا دیگه از دوستات هم بیار که سه تایی باهم سکس کنیم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27923" target="_blank">📅 16:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27922">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkDogEIGYO0WLD4f0gxGzCOZNpZNuD1ufPcpNh8GBQuombKDTs1avap9oBfyVd28iAlXF_MSA-e53D-DVgK2FxNV9dzd8CpmbPdxS9Zwb0txgztvu65J2K8JEBJS-_-g4PKCbybYdSCMsFFrUjxlpdVTBvnMDYIRWpsW2_apyJGa4ldrX5oQASJgXDa_u4knuQAdG4gR0ecFJmZwE80UOyRNf_Nw9xbp149u9rQK_2hFr9QC2gDSgA4Of8fDRti4ikkeU97GsmUScadL0fOH6XSJ_NwNCfpGwlXubCQCBQxcTMnmPQ8uyCNZko4iXw2xWa4le3A0pZ0ASr00Nd6BAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اگه‌میخوایدواقعیت‌ماجراروبدونید کسری‌طاهری و دانیال ایری هیچ مشکلی برای عقد قرار داد با هیچ باشگاهی درهمین‌پنجره ندارند. دیگه از فیفا بالاتر که نداریم. استعلام‌گرفتند گفته‌مشکلی برای عقد قرارداد با باشگاه جدید نیست اما چون مثل انتقال پوریا شهر آبادی و پوریاپورعلی…</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27922" target="_blank">📅 15:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27921">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRnfh23wNqZvCJuAUSoDqlCXhSIOzuOtLdrDbyi2FrZEPQ1Nd3wAuALoQGn9M8iKpmTaMgqmRF0JPITJCc1FwcSHQmKwKuueZ8G3mKTde0B-r2onIzvXcjpC8q7aLF4lNJS82HY0AYjVSakoWMx0FhuXFY0Sri-e-f-olXvzR8UImLhqpN43HmCJ2Mw69UQa64SZD3uRal6oAk7TmqbtEjclCqe_p3x-_zeT2zBKs-IZ9W__zyKo5qCpgllHdoqhaDLODQ0shC-B3gWZSByf5PCK8KjQuwZODrn-Vhe4LQu_X9lh-1o7CgysN9z4zUH8lkUl4PE0x_nzV8zPMh9_Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27921" target="_blank">📅 15:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27920">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkhAUDYcbY2fdgRqpL9ND83rT5t9uOd8ZfQeyfnQklC1-PIr2Z5P74vhSR3PrHm-yj-EwuXiucU-uyW5DEPnrNdIcsFYsjAzbEUbqg5oWbKLJOPAMmv7mvTncmAtH52d-nXXlw8y_rzTvZ_Omz0ATKi3KwmbnWrrZ9xYtwxfJXo-_PgtP-qSlz2faGv3Yts__MWJ35faUzXCa_zuQ0xYyPZVNwakLagJtIE83-TVpqaXkHvdmtQKhuvM3l6RcL-tZSNiNDTu9SooofzadJ_TdedEd7mR7-WGc7S1amHaNr9_XqdiiFQ4xzPfD7WoBHkrtQ2xruWD7d-49ggMaNsAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ مبین دهقان هافبک دفاعی 20 ساله باشگاه الوحده بامدیریت تیم پرسپولیس برای‌پیوستن‌به‌جمع سرخ‌ها به‌توافق کامل رسیده و درصورتیکه سرخ‌ها بتوانند رضایت‌نامه اش رو از تیم اماراتی بگیرند دهقان پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27920" target="_blank">📅 14:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27919">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e92cbf4ca.mp4?token=ht3wIXzsBbbyOvJle3xXrrEOkAWdYV97r4_bR69kSp-Uv3UCKDMOSKfm1xmiYWUB9HOQMXPOaOyCkIpoMrEwgHd4QgWdYY5oYgS68zKrXQAQa9PAzBgfHUy1X3m_6BvyrsAqtlKzhED7i7FM3hSlG3gPA6Lr5fiCAWYRitoOfCqKNf6sQgUAoJ_XNgNF35iX2NpuzqPLMNZq8f8nm-00fwvoJvbmKKj9TjPunBu9OLlSkyWSCjZdofemJVUEu-FBcAjUBmmPuME6sIkx5TiPFZRZyz6-KfeD-YA9KRO6iTRSCR0N50D_mi6W5C9ovocNY47KR5PX5frcKO8oBBERTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e92cbf4ca.mp4?token=ht3wIXzsBbbyOvJle3xXrrEOkAWdYV97r4_bR69kSp-Uv3UCKDMOSKfm1xmiYWUB9HOQMXPOaOyCkIpoMrEwgHd4QgWdYY5oYgS68zKrXQAQa9PAzBgfHUy1X3m_6BvyrsAqtlKzhED7i7FM3hSlG3gPA6Lr5fiCAWYRitoOfCqKNf6sQgUAoJ_XNgNF35iX2NpuzqPLMNZq8f8nm-00fwvoJvbmKKj9TjPunBu9OLlSkyWSCjZdofemJVUEu-FBcAjUBmmPuME6sIkx5TiPFZRZyz6-KfeD-YA9KRO6iTRSCR0N50D_mi6W5C9ovocNY47KR5PX5frcKO8oBBERTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
🔵
مدیریت‌ باشگاه‌ لنس فرانسه بعد از پیروزی یک‌برصفر این‌تیم‌مقابل PSG در سوپرکاپ فرانسه؛ به هر بازیکن تیم مبلغ یک میلیون دلار پاداش داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27919" target="_blank">📅 14:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27918">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHAI-rbVJrYUecCDFT-8FfOq5iQXAYB-tz4KyucxVTgBrfQI9VxA2sPgYPW1ZPBmq65k8hSmpUsGQl-rqkXfKsd-uiKDLm1q4PeeBPy-M3bnt1BzOA0OnFrAxiwEZcAL9jBrbjvIQkQk1aJzyk79EIEiMr6Qn4qpq_UCK168Q11y3Vb-txtcnlmbVxYzt46GhxgmDWAhElWWBHWmlBf4EfFp6GuWAiLgTDtugdJD3gekxK_w1PxoMZsBVLBXCH_iA9VdniHL6sNQMJxlbrfeUXlOCfk8l6OVrFCArCJFqCT_khUU8pVTMJ-4i7Y9UBe9hqsqhAaIwrQpK7P0FwrDRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عجایب نقل‌وانتقالات؛ ۱۴ خرید در ۳ ساعت!
باشگاه الرائد روز گذشته در اتفاقی عجیب، تنها طی سه ساعت از ۱۴ خرید جدید خود رونمایی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27918" target="_blank">📅 14:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27917">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDrsInD5EL25QZ1Mv6QITi-bGrI0jLkDahN6bGmpMBYeHmsG2i_H_Ngz6uDIx0j64KuW1uGcUz-8mNdRKjlyJoEZSNdCGfr9PSFc1GyImvo7PytY8RP5EB2OnVqa98CngG7F3U5A4sfaDOgG9ay5goEUuJf7b7_bLX8VxIdPBlbkLs0VgVeNhoqb2AtE6Mm4QNwOB13YJ5KMtQ0ILwEyDAY9givwnEPwD5JW0hPsqe7N1x7EyXZ7BVwc3KRRbkIwe7PNkdBOjffSm_353zL0qytwDo7_1ZCqcGxJ8HVL_HYkj3Y3Nv1C400TDTgOyDg3CcS1CrX-PWAt0JkLnjEgEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام AFC مراسم قرعه‌کشی لیگ نخبگان و سطح 2 آسیا سه‌شنبه27مرداد درکوالالامپور برگزار میشه: استقلال و تراکتور درلیگ‌نخبگان و چادرملو درسطح دو آسیا به عنوان نماینده های ایران حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27917" target="_blank">📅 14:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27916">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCSWf2WGqounUdGkfE89tLQb22pJgSoKbcce_66zgADUeVRuPRkIW36mdsQdvf52DOK0-R2dtm4V9YCgBZG0FEixA8yjrIQhaQkq1BVYxh_Fvfe66F-ZXJDDALqKZiQMPiRaDOS3vk82BKqvLjNrKXi39iSZRDA8PKUQSFZXf-_7wejORIXu1Fg4bOELNIvAl0oHSw-QI4yrOand2htGXDqqGluMGwlDi9-7xZdHtG13qL9x4Qqbre3opM7Z0fz384uzYYBBrJt4_5ZODWUG9VVsYvdVi3bSeGUmtus_c7jiVUUvvfuTTWNjmohNkd1VjNP8amGgDx8SIJ_fqFiztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
داکنز نازون و آنتونیو آدان دو بازیکن خارجی استقلال تاپایان‌هفته جاری به تهران خواهند آمد و در تمرینات استقلال برای هفته سوم حاضر خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27916" target="_blank">📅 14:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27914">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YfDLAWHw3jg6dTye2raL5J9zadn2mto3ur90ktu4nYpRvQwWUtXFC9vXrjMp7j0Vp7C-uoKI7X7w-P8OmGSeOkXVV2rZ7W9etIzLFb8QqF8RQfdCJOJqMXiR0SSevzEa_zTJM7D2N3rNdLWrcvXF5cOrt2wro3ey29LYuVbdmeWH7CO-0FEVF-3zXGbIrzCblAtWZQ6ni3zrdPsH4TnVaEFipDyl8HxDyPd7PMGDdU3wNdzysQyA1FOFsxBzDqcLeqPPsmfCthYnVjkNQmFdB0f1xCnOb1S3bOP74JMWJVCHxs8FYsPz2IPbzHM41hHH8VOA8Pbodz3ZtvXM73J28Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BbDprNcCUBQKA8vdzKkHW527X67qVGh7ZfRCenji35wmaSgScuY5hhYo21HPlcTEbv95Oyi-As2Zy5c9_bGikm16Lz_suStYnqhXaORvq_KJL0LptA0pPoL8KRgaJZw382AdPJSaeVdigHyYQdkvOXC3mFJ3giMkzMbr-38vhIgtM4-nKfOMxKopsamYZvKpFI95w3p5YXcow6TVfi0mJ_CqRt4nIyxr3dVcT4GeNUkYoWMYDhRDh5kQwqyYAvSErF4glKmSjtWH_u40OefgQhiljNdQaQ8639y-fgSheGuI-5T05C9l_KRPJfH2p_gQVLSWer9tlwEV5PE9bJ1k8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
کریستیانو رونالدو و جورجینا رودریگز در اتاق نشیمن خانه‌شان ازدواج کردند!
🔴
هفته‌ ها بود که اینترنت پر از گمانه‌زنی بود درباره تاریخ، مکان و لیست مهمان‌ها. از جمله مهمانان مشهور شایعه‌شده از فردیناند تا ریحانا بودند. در نهایت، عروسی این زوج در یک تاریخ برگزار…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/27914" target="_blank">📅 13:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27913">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm9S2944SiMp8AUNuKsCT1_S1IcI8Ipag_ouAgqWPc95QiwJ83OXRuTzDuZqqVFYpSdpKLGkRGaiR1Xln6QvFCYre3j1a81MsHFwBq_LFxqvUaCm231FgjyTfa485ty8qSxsMRz66Ol0tcyE9E9MIZuRGJIiMHunkJo44m87lAOzJdyvME09i_VghBcUriIORXiBd0htTYke0sAiFCU8x0mB4zIlj0J0mEB587csYoTysS1c5vkSKmG_m22EbAQzXRykoebCErl9mHWCUe6UWcN7D_9INorZpcJpxy8Bwc4DUPWtM887UNMzYdl0mURuIKK0j4zJfHSb8WxlCT-7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه شباب الاهلی درتماس‌بامدیربرنامه‌های رضا غندی پور اعلام کرده که حاضره این مهاجم 20 ساله رو با رقم 500 هزار دلار به باشگاه های ایرانی بفروشد. گویا غندی پور درلیست‌مازاد باشگاه اماراتی قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27913" target="_blank">📅 13:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27912">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9BSAUHlvVpAHB_KhPzOUBzswF6waHQmtAyv7em-DlHXF2n4FVA96QJ3nz-E1TJKEQCbXnqLGb7JwxeSd2dLPm_VDFKABTT9YVET7IF6rLEWZ_PF55QfQYZetOH0FZsxkull-xIABJJK9gQq7M9F793ymSwoy4VVvHs0HagkmRrZawbb9WUyk5ZLVwccSKavQnW81oKKjWm2X2ONEtG9uhVpbsssdqgSZWZtPB2eWSTo74qn3fXkPw5p3XdRAJKMKqP155JfVxpA1voWIHTmDDDen8aJeTUiFCpiasJtaNx43eL7oaFfPAEOsvr47RfwqX4jOh02cB1Sov2hwmuXdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ گوهر شاد: من‌آدم‌کثیفی‌هستم؟ کثیف اونه که جلودوربین‌ادای‌آدم‌خوبارو در میاره اما پشت دوربین دنبال تریسام زدنه. من اصلا هنوز چیز خاصی از این‌آقامنتشرنکردم اما بزودی مدارکی رومیکنم که  شخصیت واقعی ایشون برای همگان برملا شود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27912" target="_blank">📅 12:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27911">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🗓
هایلایتی‌خاطره‌انگیز و تماشایی از دیدار دو تیم ایران
🆚
عراق درجام‌ملت‌های آسیا 2015 استرالیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27911" target="_blank">📅 12:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27910">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQGGMJ1CkHC-GLoLKipO-bt6LUGy6TXX4n8wVRhyk-_-6yZxjNyurXvGHWT3GCyOwK0ZY6zlCDXmnHW7PHc9fJrH-EBsODb2RJ_FQHYpHw5RBvFjrdA9Ds6xHcxqzWdppyDmSquZ3r8ai5iZzVrtBgJoIFG3dxmAQTwzp6V81Een_N7bX_KY7WHrde9E2QazRg_EDrvQRBRCwnntmtuKKz-sZL5TezvCLVyKtJOaSeqx0KmFHMlYy4EPYRP8s0_YLeIU5KCG1hFb5OYu8Fhn2bE4siskBQFH-t571gygzpT7M6YSsmJZJx5FSHsqo_GRE4ZNAfpwhZVLqp8tspRwtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دیدارهای هفته دوم رقابت های لیگ برتر؛ مسابقات این فصل بسیار فشرده برگزار میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27910" target="_blank">📅 12:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27909">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsMm9zpXp4i9lsPgqyK0xRa5hBGDdnIM6NgrK2gxdV61qHHUgfOugoW7Cc2th7dqNK1OZAeoG7bZDTpPDOewQokzsYXUEVPvDa4whe7J9G-8TBKZ_KGMj29pBvzQthAh2a4O__9L0MCito9rbrLajs4InJwmQ-tVe8qdOs4sreihVm5Y9zP5yAyk6sC-wDvdIfdanPbn4R0_m-4tnMWsBIUoaBSolcO-e2vYBtVGi9v8C_mgsWAvkXtRNS7ZbVvDFlvXrJkqFIjpsg8KEerCgdFf9DmEVdyHrUh9EL-7BaTrkWX1u1C2x9yjTx5ySHQ72VTBeY1rt7c74BEt0smiWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27909" target="_blank">📅 11:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27908">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7lxpk2i2Llo1wn-Uc-_BdJwJxng158R-2UHwRZoGrPsJuBq_Cz50kaFTYHqZWcmpvh1xFOe30o0cDDjF58F0sAaIj4K-IA5880jKs3-1dPkjEZ6XrLjgEbX4d6SPEsOVKy_ZH2vtsNItEanpcLZi0Ftab_Se76b3wgl1MdVoGjN3ufubJ1GAnfAsJ1P69IZIlz0ZMm3J_MYJvufgVRU8vVQ6nHYJluvPos956x2K-OP0Idv_E_DdOXJn9CIOv-6IIZnyjzoJUFfLg5FXexZfUea2LkjpiFjyGqGmlNET1JCW4ryj5odQ0v20wa3G6sa20qO8R3Keg6B1-Wxg4R_Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
دو باشگاه استقلال و سپاهان امروز تمامی مدارک‌لازم دال برقانونی‌بودن‌قرارداد آسانی و کسری طاهری رو در اختیار فدراسیون فوتبال قرار دادند و بزودی فدراسیون در این باره بیانیه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27908" target="_blank">📅 11:47 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27906">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aly8WLXgJIOmn7An2Ympw3cIliyZ1T-RH9Q5-vo8MegaCXi7T9nmQGGRjeKafO93U86bTRw5JruZSTXpGtGltxYaQEZbZJk5Nbta4-eWRYmMkD7s7g59cFMt51sZh6FDIJnSebEfnpmDsn4bjMIGuwdUW9GwW3YTLcG0Tl73EIvaRKtvm0omHhs_G0CNTdtQ5-yLXL1638ktTVRzpNIOb8ObN635cVGibn0pjfujPaOIu1qJec-JEMdzpUxrC2UH-Xg053nR7VsVsl1QXe1nbbuyiOUfY_yim_Qwcr5MWL7FYZ-plsvnxObnPXJyuWNHcnjvHUFYOAshY82nzvn06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی هاشم نژاد دیگر ستاره پرشورها نیز به دلیل مصدومیت دیدار با سپاهان در هفته دوم و دیدار با پرسپولیس در هفته‌سوم رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/27906" target="_blank">📅 11:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27905">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec510822f.mp4?token=QA7XxgamifO7jHpl5kLZYLV8HKbztcfcYCPGUIYCVB7uZMyGguevDlioHL6rSuORJUmyuHuW_HHWuu4SfqxM4b7H78ZLe0PdA9l2ZzDEkEmT61EvYbLS-7HPNhQ1WQQJeqYAAcBxNf0oPAG0fVIudTlPtj5BVTK5CM2Qp6VNrgCtqoe-ukpILv0ULSvzRfL-Voc9Y-WQ1LD9iYkvMGHPrYG2OCmd6UAxln-yxBt3UO8EcPBeHaKOedwLnJPSkbjScUDV14tEuls_HiP2sbLgevi5jO_kx4NEo5ui0Sa7XZ1q1OZnuVmnfqUcnKBK374Q87UxcZNa3pAwuLPQGvd-By4UtZhtogGhDcsSkATZvU6uPdMIPOGFPKbGcR_g4ULbGQduTfzfxXDj1Fqms2C7Kiz-VDMqS66-Ovfo9yzxyIngldhTG1OGg6ctmtWKTlb2Sm2-oFsI3WR1w3aGUbA4tqh8UFpXRWlg76VhDsbjxD5KVY3VJmFVzG5xdQZUD1ex-qGUDIShmNHoyMggijB48SKbG2zItZ55dc39jADptYVQzRJcncT3jN1Qtn12DWQtTGqlGr8gERRmJlROQRksqzcMl6l8fzmf0oqERrmk7leHfZceiKLhhsNRseO_L0rbtlRkYsgDPZK7JoJwEi92to_lXT7gZgyxKz65ettyGEU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec510822f.mp4?token=QA7XxgamifO7jHpl5kLZYLV8HKbztcfcYCPGUIYCVB7uZMyGguevDlioHL6rSuORJUmyuHuW_HHWuu4SfqxM4b7H78ZLe0PdA9l2ZzDEkEmT61EvYbLS-7HPNhQ1WQQJeqYAAcBxNf0oPAG0fVIudTlPtj5BVTK5CM2Qp6VNrgCtqoe-ukpILv0ULSvzRfL-Voc9Y-WQ1LD9iYkvMGHPrYG2OCmd6UAxln-yxBt3UO8EcPBeHaKOedwLnJPSkbjScUDV14tEuls_HiP2sbLgevi5jO_kx4NEo5ui0Sa7XZ1q1OZnuVmnfqUcnKBK374Q87UxcZNa3pAwuLPQGvd-By4UtZhtogGhDcsSkATZvU6uPdMIPOGFPKbGcR_g4ULbGQduTfzfxXDj1Fqms2C7Kiz-VDMqS66-Ovfo9yzxyIngldhTG1OGg6ctmtWKTlb2Sm2-oFsI3WR1w3aGUbA4tqh8UFpXRWlg76VhDsbjxD5KVY3VJmFVzG5xdQZUD1ex-qGUDIShmNHoyMggijB48SKbG2zItZ55dc39jADptYVQzRJcncT3jN1Qtn12DWQtTGqlGr8gERRmJlROQRksqzcMl6l8fzmf0oqERrmk7leHfZceiKLhhsNRseO_L0rbtlRkYsgDPZK7JoJwEi92to_lXT7gZgyxKz65ettyGEU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
توماس مولر که پیش‌تر از لیونل مسی به‌ عنوان الگوی فوتبالی خود یادکرده بود این بار در تمجید از کریستیانورونالدو گفت‌سطح انضباط و سبک زندگی حرفه‌ای‌او بادیگر بازیکنان‌اصلا قابل مقایسه نیست. ستاره آلمانی سابق بایرن تأکید کرد: «من هم بازیکن منظمی هستم، اما کریستیانو…</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/27905" target="_blank">📅 11:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27904">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ac05124de.mp4?token=kqwqXuxK_ATTTfYUXeA0JlJU7MDIcCX3_8_XK_gJNwouY9aFX8jZskBtfFB-Qd2TYJoBBkhFqQXgxtYebgyGKpsRh2inL8hPou1J3NP9HT90Ku05vP4iBLgCbAmnlZBmDKjF9Ya_ys5G4PfSSF-9Mh8jZn-oFvsZ30ZttOlNqXwm0BhG-OUD3tx2obkIazi-hpMrcnxgadpMLJIwWQ6lqmGj72efS0y73qXM4FB1RDUqarWHajOFG-2tAY-smM4OKcCqSsbaN7M2t2sBf8P80kG1eD4IbwdL-4JuC_HV9PA6nB9q-KnTk96h7-AE4RWkj9fGF1_sU_yJPeHy7P0gug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ac05124de.mp4?token=kqwqXuxK_ATTTfYUXeA0JlJU7MDIcCX3_8_XK_gJNwouY9aFX8jZskBtfFB-Qd2TYJoBBkhFqQXgxtYebgyGKpsRh2inL8hPou1J3NP9HT90Ku05vP4iBLgCbAmnlZBmDKjF9Ya_ys5G4PfSSF-9Mh8jZn-oFvsZ30ZttOlNqXwm0BhG-OUD3tx2obkIazi-hpMrcnxgadpMLJIwWQ6lqmGj72efS0y73qXM4FB1RDUqarWHajOFG-2tAY-smM4OKcCqSsbaN7M2t2sBf8P80kG1eD4IbwdL-4JuC_HV9PA6nB9q-KnTk96h7-AE4RWkj9fGF1_sU_yJPeHy7P0gug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛باشگاه پرسپولیس برای تمدید قرارداد امیرحسین محمودی ستاره جوان خود به مدت چهار فصل دیگر به توافق کامل رسید و بزودی با حضور درساختمان باشگاه قراردادش رو تمدید خواهد کرد. محمودی از باشگاه قول گرفته که شماره 10 فصل آینده پرسپولیس باشد‌.…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/27904" target="_blank">📅 10:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27902">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfD9SfogWY7C7NS8T3OvSDUbNsmaGI9pMFdV8TlJhw6S6BrgU9PuklMPIBAP9jxKpZe5NclNTSIw7OrJzpFhfBh9PE6xx5XzHief5ROF0evYk__QZDrRgjCfQIPBDvAJDxVO1pgsUVQKEtDhKJIfUQYnSmILHCLn-cFzgJp49HhySstPx2SOIRjX36JwEyQhL3hgpIIVIRJQZwIpG4sSB6kJj4Cv5xvEUOjrFvXSELQyT6c-hmwxkKL3QPk_ARUbaWC4p4fa_4Rmu0laBCFdNHW-eZocoOw6IOpYvGON0gF0qCMagP_lnB8Fg6hSzbTb1NArBsRRSnNhT-DnlaH0Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی ترابی به دلیل مصدومیت 4 الی 6 هفته دوراز میادین خواهدبود و بدین ترتیب دیدار هفته سوم با تیم پرسپولیس رو رسما از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27902" target="_blank">📅 10:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27901">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GUy1hh3hcHv25JEx8mRKdq2pbi_bUodEz_TW1GwEoRGeeN7Kqo6F_qyQ1XbbiOeMVT6YsKEPyMmz-VDeCVmYeCK1zh9Qp1-PQhpQ2Vxp2SBjwUEM5oO5Af08SBzU5lEyfFT-9CsHvnf53plxzcsP6mFxGcDy_DTDTKVcJT1FWU0GQBg36sA_AJ4augu4EU53lg7dDS05apBwV3HS7FQGg_ajoT-IRfCNiqwwwYwefGA2jn4T4bS-gHxh2s6mTk5etBNDYm1c8j6xYd7fMuHuDTMLhVGKgweOW7_vC2fatahwXmJamoG684ZW6NnrPv_fpNAKl6Q6xMTXoIFP1vaMjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🤩
#تکمیلی؛ به دلیل درخواست 80 میلیون یورویی اسپورتینگ‌لیسبون‌برای لوئیز سوارز 28 ساله هانسی فلیک به‌سران‌بارسا گفته کلا قید جذب سوارز رو بزنید و تموم تلاشتون رو جذب آلوارز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27901" target="_blank">📅 10:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27900">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sukRg0ita2hWLLLXLLfgCl7epLzaGzHP0eHkmOt-XxOg5LicSnbbteLxK7bkW7G_9VPaLtBcZ2RvGIHQKuGUsOxUR64Aw91LT-aJXoPxdB7hIncNlYvp-xiUCfF4HxsJONKn5kHyTIRP3RVh8YEusL2Xn3KCYo2KiuohIjUHdOB-ZHtuKTBaz-i-vH4Egy1RJWhlfNsRjSdb2CeedR5ccm0I-zYqNTNiX-WjqtNE5plkA4wKJw1FH-G4Fj018TFgrAJMrUNs5KAyTwC3G5E3dMm5W1mo8IgkSqdF89rpFFYGiRWPG2ZRphvc2el0qhI4xhIMFfnUxNmbIA0M6VRrBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
مهدی ترابی ستاره‌تراکتور از ناحیه کشاله ران مصدوم شد و به‌احتمال‌فراوان همچون مهران احمدی یک ماه دور از میادین خواهد بود و دیدار هفته سوم باپرسپولیس در یادگار تبریز رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27900" target="_blank">📅 10:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27898">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHUuTt952zkxPw92ACiAQLAYYO6ZLUXqEviQdcf-zG3ktftgIHtLjdGRcZ3aEACoPzAeEg5p1T5dtXZfsQSGpGeA9sBK2g17M7P36mbgrH9bn7uxSaKTQxrjXkVA7m6psvske4FK8JH-PPfEKQoEqQnwKU31PUJnnLqPHHN9dacztHYbaQEwysn6AoIA5KUn8uWLFdGUX7rJmqxTU_lc70bqrFB5hOWJ_a0Rb96mSZ2iCs7jTlsirQQkzYGGgPyecYIgj7Rom67dHn4ItpvTnqwoLAU7Bjsz37BzCJG100rLhzmV1VcPoilajoEoIeilLWTHWiD9nvIrDDmVKCkjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با فرهان جعفری هافبک‌تهاجمی جوان تیم ملوان برای عقد قرارداد به توافق کامل رسیده است و تنها مشکل جعفری شش ماه سربازی باقی مونده اوست که مانع جدایی او رو از ملوان شده. این بازیکن در تلاشه که کسری خدمت بگیره و راهی باشگاه…</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/persiana_Soccer/27898" target="_blank">📅 01:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27897">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coB9SehzHOEIm4BpfKUxUWtD3EovdkRowmlf8Imdhm1yU96CjARddh7szft4qRfd_aXIx-Ns5sUCB56_rRAZz_Tw-J1c5_dKEbdCM8eDHB-KDIvXRWh2lkww1zxhQwqE_mWf0c9kj30FeAeNNos7iabpMrysUT9ZjZOJLEo9hwK5lrubhVUqPi2ZCv4ewxYBlMxdcQH1IQaAUqgu6mll3Nxd-BFVgXmoYqe797PUNcbuEW0yJT_1EvuBJPjpENXOOLCXqhgesSrrgQKntgSgz5yltW1jm3hLQr-P0RlrvbLxFoTXvZ_Jzy4hK4IlnCIYmuQeicHrpnq3cnPJuLPPGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌تنها‌‌دیدارامروز؛
بازی یاران کریم بنزما برابر الرائد درمرحله‌نخست‌رقابت‌های جام حذفی عربستان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27897" target="_blank">📅 01:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27896">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AHgrtDBTHWUJMbmz2Ap7lK54fj1HARjCM5yWlnF9iytH40IoB11zzlA_tJCU_yOMlt-ZrvK0GMLx-4ptDU9hyLaXQtAQ0_9SwQnG4NmiVEnBUocqmgBybXR-jN0gV5tppvvn8hPq4eMFRZJiOpUc-M1gVm_LavqKiiJZM2rjZC1yghrJf_1iTdDzsL-DBWpHDfU3bi2Bol1Nwl86-9hnynmu8T994ZKUM-Fpx2IWpIpIhI7bAWOKq69d2a9_H_OrY2JzRqT38l2tAEmuOp3kNB9_4IlVFWdgF6NcO3btEJT4QqyTJhQgxa3_-Uo-KyrJIRGM1DGHQ6wJNi-MaZQKoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
ازپنجمین قهرمانی آرتتا در آرسنال تابردپرگل بارسلونا و رئال مادرید در مسابقات دوستانه و از دست رفتن سوپرکاپ برای PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27896" target="_blank">📅 01:40 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27895">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ATz44F6DKmpIM6KNzXW5ppXah8BNTyvZJEMyUu6Wil-kynLybV9Ypy8dVhZ8LUOx6vJFTNvN8jh_B78l2aD0NFxVHuXpDmpwiPWxfGy6NuN5AdmrUE31KWa4GKF0ftDF7tEQsVOT0jt3uNWA-r_hIpBF_XZeEWYwLC0_7NbTSALRhYYS7qG4tkYvDTwrF0XwfN_mB3_o4Y8crUcanT71r_K9Y3QaKjJKNAWEtTxWueSkaQDZv054m-Lz2gFcC_YCoW776bWchCMpmCXcQbQjCDooA5mZV4txjVvz1efjb0JTLoNObUIZDqWv9AcQLjS2WywxRUTeJKvyyCygctg45w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بزودی باشگاه پرسپولیس جلسه‌ای توجیهی برای اوستون اورونوف ستاره ازبکی سرخ‌ ها برگزار خواهد کرد. اورونوف شب گذشته در پایان دیدار با شمس آذر درشادی بازیکنان این تیم شرکت نکرد که باعث دلخوری مهدی تارتار سرمربی این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27895" target="_blank">📅 01:23 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27894">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PFtOVctRgXKM4eC8GkskkHf5LMSWxRMpT4btlMAXK-zYIXaqA4WkbgJGDcygPjuVPWs48LMZKAleM4P9vfwvvz0ozr4kUhsJD6MUP_s0rUov_XUwIhX5Lh1R_w7m0ybBi8gLBO62htSamgq5kzuR4QER8vjh0w6OFqWNmuknU2WQAYCiWsOAA_gbDXTdGW2UjpI13ccJedkqrfxftbBlP_puJz0ylJJ48zcKlfUlUai9MqYrMa8hOcBO3ggdJqj4k-NZYPj2MTLaRkLVjLSSZKDojcqQcLBKTR0-_rktgqCCxHcm9ohm_HQvkH1P5JtjGoMgDzbcZzkHtcMYV6RcCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردین رابط وینگر سابق تیم فوتبال استقلال در کنار همسرش در تعطیلات پیش فصل رقابت‌ها.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27894" target="_blank">📅 01:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27893">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efS8teLPbWueDJkeDXi-xqIA4X5vgpJkK9bABf5ss9bFpEYsEXFzK_adcqMh8iZoIwi9cVZZ1HTSgFQh-E68uDYNTXXOQXBeAWyWE_F9GQTyPOv7DARs2iyZoxjux9lHrWRWke0074y_y1FNlZ4aVw2NwfJ86uY_oGZKeywmpmptl-bGEMvZta75fan8dnBPtyT-1iRvbmchLNzPo5woO7eenpgquAYGGV48j4Hj3B7moE8SyYd3WCBBGIOdePFK0K-9Rknra64V1hVZyKkF1QCpvYaMNmCwrw--BRko7vrbAvXEu5umdcITPxHmiqTx92Oyetk26HZk44IJ58ErBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سوپرجام‌فرانسه؛ شماتیک ترکیب پاریسن ژرمن برای دیدارمقابل لنس؛ساعت22:15 از شبکه ورزش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27893" target="_blank">📅 00:51 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27892">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZlAOjd4j7THjWDqcslkq6EuA-qTq-kT-_oe8WrTI1fkFiSVewwpj6GWeJetfsYkp9wNqKp4nU_M7UZCbTp06pv4OvpT4aZq0i5RjeTXFgB7r2Ga_7Hzm8K19wm90-NvbQP37a60wP9XLWhdPO9v5VqtaDh4EpiRIktrE56PATLXUrnoo0wmded46vVwVmU7qsplkX5uN6bEhK_GxSqnroiIjMmL06W_i7of3-wlVm-zwrt1CVX3AVka9RvJIl1H2soaeS_4hxF4gnXmiXMaWf11JQKGunxS4tpKlauj9sSXCa5z4yM5YzV2QrseYdvoWUwrICWLgrasTdFRdPwOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
بعداز جذب محمدصلاح؛ باشگاه ترابزون اسپور با عقد قراردادی قرضی تا پایان فصل داروین نونیز مهاجم اروگوئه‌اییه الهلال رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/27892" target="_blank">📅 00:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27890">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lemN-0rNKpXbOJk1wOSQqUe_Vh2uG6iq4UI12yAdJCYUPAH1HitQzqmG5mLyPIgO2bcs2m-IY-I4HLlTTYa_-GraImDKAyk8F5znSNpoYA7hs5_aFbVhHtP7izWlNJIBZDmyPe2AKaAO_1Qf__-CdLPL9s4lwIBSpbhx-BNJWHqjYmOVpqKLqCqgEJ3qu1JxCEGAbOuemVNx7Wf9GdfPttCnEZSjYPmtrgpN6KgJjv9GmOYoKvwfcTCp__ekD_V8q9lZCCNv6WWpFmQjeijo878sHi_5rsAAfcL1keq3iq760RIJWSbob8pmohfZdMl3M2bUKpvbsbFB8VTGPe9tTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmXfcVUrRymTb7Ye7O2PxVFaE8VZ2YQ6mLRH3RKGo8LWvs0TTBmFLCsO9CWdIgMlj9v2p0CVSgMx9EY2Vk2CDk7Q7pfyWJKJf-ARAbUPRgJS0v5IEEqbJAzxxKiqMyNu0d9GoNQWUEl9onwDGCDYT2rDjpVmFgXzU5BNyQgFbPesDQewlGxkCjkv9KYcnT1R4xlQEPG-spyA8X6fBT0AynBfcBG4NfiUrzDjgVqyrOjwx3qGePG3zcmnDMIizY6UOZEoKIrcJG4jWb-q6XjATOP6M8B5Yl0TA8OAAfe3lW653XeHaqgA4dllU5Ep0FENzCaAWhPwwbkKXexeB3hpxA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
👤
مراسم‌ازدواج بسیار ساده کریستیانو رونالدو و جورجینا رودریگز پس‌از حدود ده سال دوستی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27890" target="_blank">📅 00:12 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27889">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3nhF4J5AckuRvnBgcbDoSePcOq6DmkjOEsqUOm21vM7eVD3CgU_fuAKyH3iav0z_oJgcDp8BnHKLlzoIKT9frcvq152R7MqCUBy-GYCy1NI8vcGh_R4jHKBXmyaai3YoWrew-yWB7zax9WtSQv7NJWXMUGyuN4IWUn1yA7zfUzX0lwMurbdyqgz0QAc_wUjrcbJYRRmKRFzFtzf_SehvtVQbjteKngOOS7lijchrELP2W_CPHB3fFRIqK-e7RjMEjF8LTd-Rcr122ZDyVIBV_af3YfvNhOtw-qhczUSsk-zL2-ABhjO9vAbvXh04kCWehJqbVF4Y1S1YjQI5MR42g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق شنیده‌های رسانه پرشیانا؛ سازمان لیگ و فدراسیون فوتبال بزودی درخصوص وضعیت یاسر آسانی در استقلال بیانیه خواهند داد تا هر هفته جو مسابقات لیگ برتر با شکایت باشگاه‌ها بهم نخورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27889" target="_blank">📅 23:59 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27888">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYiAawTwzCVl5IL--IiGB111gAX6S4B9sUL9VmQmQDrBUfRGrOnNOhCSdVCgjJcTz35IZgVpa5fD1gAd0NXJVKCrffTu2_3tzaR6qmwcETpuh4H4Xu7JAOfYZexew13u8O9xcfvwW6f6iisW8QvSJrk9Vd_8h0_XhOH0oCC3I4tyUFMC6dPeHo0KAM8CXhQ9bRa4T9D4VASomlHZvczRv5fqBqo05t1VujI3GraIlJwFUJ7CqBzr5gLwnA4AYH0msyKFMFimB9VWXQTke2Noxs9D2b33eTuhqBZAxKdoH5tf08ZuR_pQd_q4rTZusrJ4YKNW_zVgiiR4XPOvdv5yhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
دوباشگاه ملوان انزلی و استقلال برسر انتقال ماهان بهشتی ستاره17ساله‌انزلی‌چی‌ها به‌جمع آبی‌ها درنیم فصل به توافق نهایی رسیدند. بهشتی در نیم فصل با عقد قراردادی 5 ساله آبی پوش میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/27888" target="_blank">📅 23:48 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27887">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mk_ufB9SS0Gy2K7Nj8J8ncmkqGuCcOgoJUWFMxbaJ0mxqatgH0f6GDlzY_PzCR08Xw--REWai8txf-OMnfeQBVdwyeZSg0__jXNj_kaBFqGYkmOqbYQROQ0rTciq7Z64nyDZqz0WqWwHMCrv2qoPNjnD5FvZTEIWmiefD8rEvd8KAq57MJjwLIK67N7raGA5Lmy6TuF4osjJUsleLEpOcw5uEF4SBjqCfhzQt0uke58bMCiQrGZSOG7lgc-azZZYGGZe4X69y36zzwEXCwCOgicjyx2T06_u4YtXDvE8towjeiuYl9maPEzbPeqwapW8DdtVnesf2DIE9sBUy1_eVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
بااعلام رومانو؛ رودری فوق ستاره اسپانیایی منچسترسیتی با قراردادی دو ساله به بارسا پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/27887" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27886">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b29fc31c.mp4?token=eygPKHBPAidvC_9xKGmw0jZJbFIkNddYcPjMCCm-sU1Mm-TL8q0nvmjUq072KhSzujVDClKcrIL06t9l0zo5C5dADN8b6ojkX88Mdo6FGRkUunLYNTOp1wHovJzxS_Oq5RvHO2QEVLGf8nR661JWcf_hoxy-IyjFwOAQVmwROipl5iHb7ZLX4nWXh6PnmbInP646FvlAWD60K-CUIrosJmUw8Ie0CcaWPP2n_jXmHa4DnC2T0KwAgOX_PyxDz57bKrsP3RKHsAke1lwQY8m_dbiFW7pQDBX23RWqBL40OLDcrcPDXobgqyoBuK39VEexw4Bdbyf8h1RKGCqrDz1x3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b29fc31c.mp4?token=eygPKHBPAidvC_9xKGmw0jZJbFIkNddYcPjMCCm-sU1Mm-TL8q0nvmjUq072KhSzujVDClKcrIL06t9l0zo5C5dADN8b6ojkX88Mdo6FGRkUunLYNTOp1wHovJzxS_Oq5RvHO2QEVLGf8nR661JWcf_hoxy-IyjFwOAQVmwROipl5iHb7ZLX4nWXh6PnmbInP646FvlAWD60K-CUIrosJmUw8Ie0CcaWPP2n_jXmHa4DnC2T0KwAgOX_PyxDz57bKrsP3RKHsAke1lwQY8m_dbiFW7pQDBX23RWqBL40OLDcrcPDXobgqyoBuK39VEexw4Bdbyf8h1RKGCqrDz1x3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مراسم‌ازدواج بسیار ساده کریستیانو رونالدو و جورجینا رودریگز پس‌از حدود ده سال دوستی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27886" target="_blank">📅 22:45 · 25 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
