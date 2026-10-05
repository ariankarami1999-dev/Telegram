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
<img src="https://cdn4.telesco.pe/file/s8k8TQdC7E1PGSvXDGszNjLKZulW6a2xpR0ZuMASembELxw1Wj6VXDNQXEguzdXDgGIQwZ1oG_AS-dkCnLsE4LSdP-Wvo3nz6s-LpYYlv2aIi7lljvK9S9vwsBFPe8ezsNxZlWNAHQTRa9DLhG-usJ6ukAtOxcIL5B0pTsvceC2VTgENuTFJUZ7ZaHhkZCJOAXw30UljmZ4A_iILcxLclvRa0_9-niUam54TF_an2Vpoj53UitWcR7CVU2HObrIQuAcpw3A2qmNDwmb-ApAp6S1xI5r4wNTHZZJ_DoGuezBwPDB5qarONtCb7P5PD_8JEUQcqJan6lkL_qpG1TOjIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.8M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 12:49:28</div>
<hr>

<div class="tg-post" id="msg-466403">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/farsna/466403" target="_blank">📅 12:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466401">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff1b081cda.mp4?token=Ar3CTj7Ata4im4rYsYFH-89IEHXxgJBJOGJu2PY4Tv2t2hr4ennSCl37XRbYSRd3VvVjVDaCdI993wEwWn_SQgml5ieETlWN_j3yYHg1NXvRTNySTZaeKXiKeAKv1GKWw0rwuN0amRoyg1LirV3jcnSO4lcB8ncVaAcsde3VkTPTSNSUgiiy79NxfPo33ftjnl_UX_ZfB0nChv_DEnxgX8xjQtTiIBABKVP_3faUME26G1OCVQh3_z7S3bwNoj_xr-LT9WvMYB0yBQWDWB_jye2Hu8j8J571sqPj-R7c-oeyKuc-1LaIfMyzIte4X-FiVwKFNX_sgNK1o4J-z4NplQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff1b081cda.mp4?token=Ar3CTj7Ata4im4rYsYFH-89IEHXxgJBJOGJu2PY4Tv2t2hr4ennSCl37XRbYSRd3VvVjVDaCdI993wEwWn_SQgml5ieETlWN_j3yYHg1NXvRTNySTZaeKXiKeAKv1GKWw0rwuN0amRoyg1LirV3jcnSO4lcB8ncVaAcsde3VkTPTSNSUgiiy79NxfPo33ftjnl_UX_ZfB0nChv_DEnxgX8xjQtTiIBABKVP_3faUME26G1OCVQh3_z7S3bwNoj_xr-LT9WvMYB0yBQWDWB_jye2Hu8j8J571sqPj-R7c-oeyKuc-1LaIfMyzIte4X-FiVwKFNX_sgNK1o4J-z4NplQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: مراقب باشیم دشمن از اختلافات سوء‌استفاده نکند
🔹
رئیس قوه‌قضائیه: دشمن به هیچ کدام از اهداف خود نرسیده، اما زخم خورده و کینه و عصبانیتش بیش‌از گذشته است.
🔹
دشمن به فشارهای اقتصادی و تحریم‌ها امید بسته تا پایداری مردم را کاهش دهد.
🔹
باید هوشیار و مراقب باشیم تا دشمن از اختلافات و دوقطبی‌ها سوءاستفاده نکند.
@Farsna</div>
<div class="tg-footer">👁️ 2.53K · <a href="https://t.me/farsna/466401" target="_blank">📅 12:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466400">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CE_skjxjoR2mjhrfwOTzQZV3pCud0FmuGtPkq_vlO3xk3pInRGvM11c9DALGvUBkLKKWbnRIqtphvOm40AR6wdMkp0zyHdr7ivhzYp0DIdNjCA5zpeLnORMJeqbywG_4rcslsxyudo-sSkWH6Lk3C2Q0Cul0fKAqsu7_I0Ee_Jj09RA70zw9_GWELYF3-NQGkFFjjtVZPiHqYlSpVX7D_Ur0q4d9QHpP35_9Ok_n_UqUcZqC_i2k3Xj4uJ5TKPbWJtzs4SHeLRfDzR4lYNMZKH-bqOadrsO0p_vLuqZMGLKn9tZu2vU-yGs06EdC6vOsfOY74u716AykclTxjCLCYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستور جدید پزشکیان درخصوص تورم صفر
🔸
شهرداری تهران از هفتۀ گذشته طرح «تورم صفر» را در پایتخت آغاز کرد. در قالب این طرح، قیمت ۱۲ قلم کالای اساسی تا عید تغییر نمی‌کند و این اقلام در ۱۰۸ میدان میوه و تره‌بار و ۱۸ فروشگاه شهروند عرضه می‌شوند.
🔹
حالا با دستور و…</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/farsna/466400" target="_blank">📅 12:22 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466399">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‌
🔴
سرلشکر عبداللهی: قبل و بعد از انتخابات آمریکا علیه ایران اقدام شود باشدت پاسخ می‌دهیم
🔹
چه قبل و چه بعد از انتخابات و با هر نتیجه‌ای اگر خود و یا به تحریک رژیم کودک‌کش صهیونی، علیه ایران اسلامی اقدام نماید، نیروهای مسلح جمهوری اسلامی ایران بلافاصله، با…</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/farsna/466399" target="_blank">📅 12:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466398">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">‌
🔴
سرلشکر عبداللهی: ترامپ بداند، ایران منتظر نتایج انتخابات کنگرۀ آمریکا نبوده و نیست
🔹
رئیس ستادکل نیروهای مسلح: رئیس‌جمهور خودشیفتۀ آمریکا نیز بداند، ایران معتقد است سگ زرد برادر شغال است و منتظر نتایج انتخابات کنگره آمریکا نبوده و نیست.
🔹
بلکه این مردم…</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/466398" target="_blank">📅 12:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466397">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سرلشکر عبداللهی: جنگ جدید دامن همه را می‌گیرد
🔹
هشدار رئیس ستادکل نیروهای مسلح به سازمان‌های بین‌المللی به‌ویژه آژانس انرژی اتمی: حضور رئیس باند تبهکار صهیونی در منطقه و اعلام این مطلب که برنامۀ هسته‌ای ایران وارد فاز نظامی شده است اولا از روی توهم است.
🔹
از…</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/farsna/466397" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466396">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qENSZxqVwkaKnIzcXOVlMggmd3gC90zH-SZ6JIFZB6q7aao5e-ztO5F5TIPKrrOxoBtcb0fWDZH4j_0s0os61nrKRZN_nZemGMQWSlvlYmzyzNDpceST-ETpx-jx0fzUQGt5wl_538GuUFlN6YOXuGX0DZEUnaJt3aNy9DS2Od5a01G6Bg1AeyI5zICkzS-mtnkydwKTXvD8Cmx3V6Y9lzGx0DAhlK52TEWZ2nC9nS77QcDrTRBCghJI2wHyEpAJvFtRWFoT6Br1hCAkYRztsbEyAqKvs7009iuv3RyixNr6V6A43IWJfwh4LHUmyk6bhq3g1lVJQkL4RP7IcG7AUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرلشکر عبداللهی: جنگ جدید دامن همه را می‌گیرد
🔹
هشدار رئیس ستادکل نیروهای مسلح به سازمان‌های بین‌المللی به‌ویژه آژانس انرژی اتمی: حضور رئیس باند تبهکار صهیونی در منطقه و اعلام این مطلب که برنامۀ هسته‌ای ایران وارد فاز نظامی شده است اولا از روی توهم است.
🔹
از ادامۀ ایفای نقش گرگ در لباس میش خودداری نموده و از ادامۀ اظهارنظرهای بی‌اساس در مورد مراکز هسته ای ایران پرهیز کنید.
🔹
آگاه باشید اگر جنگ جدیدی علیه ایران آغاز شود، آتش آن دامن همه را فرا خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/farsna/466396" target="_blank">📅 11:59 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466395">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2AKGjgH-myBd6hNAoH7SYEjX3w43O1X7nNW-qSaqBjdYfU7SEI1c5nz6j58xJ4XD7p_r8k_hjMO-z6Zoapo_r0RZ3Cyah3fdSjWX-j37uUJ5fCsZGL8gKbErnxgo-H3z_bVaA56Rd7n44Do17vEJMbuP1LUeEkJJn6vp0DsJau5Oxb6mG4jyacssZ9B68b4epeOpAVC8D9BWndBaeEbw3b4tggYW6eGTyrwjQ6kQX8LgFgDWiD82ZDaFY3E-XDJ1YqrcJLoNEyGaRxzoOs1gmKBppDTHomAA9h2QFEzsk9R6KY23Atyg3D-ArxxEck4g3jubctshQxcUg3E9fiyCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌قیمت کالاهای اساسی «تورم صفر» اعلام شد  برنج:
🔸
برنج پاکستانی سوپر باسماتی: هر کیلو ۳۳۵ هزارتومان
🔹
برنج پاکستانی۳۸۶: هر کیلو ۲۲۰ هزارتومان
🔸
برنج هندی ۱۷۱۸: هر کیلو ۲۸۰ هزارتومان  گوشت:
🔹
گوشت منجمد گوساله یا گوسفند: هر کیلو ۱ میلیون و ۵۴۵ هزارتومان    روغن:…</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/farsna/466395" target="_blank">📅 11:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466394">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dbDGekd3-N2WujSk-4xdogxRitBSQzwsGVGoaKNSg11hcIqWxYl6xQCTCYVNePDCdHqvRlpRZHR8Osq3kbrcuALLtD8sxUDb1r8re8Y7DGroUoSr0ueLJyXH_zgCqBGAk4rOBdWZZFVXyFeBp5dJRmMPCjpwQFutSRS8ZKVYMSpzpgbXhKCtmGxpUsKs6vEpoNgrkZmC5_YlxxqNA0EBOJ7ufabhuxDcGu1d2es736kEwR1_aL_Grvnx0oJJu6hKTI3v4baAKOUpis3yv-9QgemBhUerFAB7XhhauDWHStNV08PUdKbI5GiCYLLrJFeMVk9JL0ujmRoMlyGvM27vQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قالیباف: موضوع طرح فروش ۱۰ هزار دلار بانک‌مرکزی را پیگیری می‌کنیم
🔹
کوچک‌زاده، نمایندۀ مردم تهران در مجلس: چند روز پیش اعلام کرده‌اند از روز شنبه به هر فرد بالای ۱۸ سال برای رفع نیازها ۱۰ هزار دلار فروخته می‌شود. سود فروش این دلارها تنها به جیب دلالان و رانت‌خواران…</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/farsna/466394" target="_blank">📅 11:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466393">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c7ea927e.mp4?token=hWAU9qexrSkLKJxnvV2k73EBRRtCwfal33ZlyWcevCNsD-9U6Tp4NPOcLrZevvtmylnxhLz_QJtGXD3Zr5gJzQ_dYVvst-poBkJLUQb7hFODIa2MaSmGdB4UsxPb04rc4j2xmSPCr60DhAs-0b4Zya5QbA3djKPhrPBpnxiU4VrWPuJi2XQ8EYu4XOj5qf95wMORvXC0igwd2cqtnTHAvderSjUHQeK1l8HFXVjp36v9MjqWeWCpuuTfilT6gIznQZHke7eOsNGCKI6O-E3IE63HhcGLjOiSBqr2hyt4Hv4zjQacTmczGdeQ5ZP0gmYx6yt5YG4o9v5UKwJIb5OkQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c7ea927e.mp4?token=hWAU9qexrSkLKJxnvV2k73EBRRtCwfal33ZlyWcevCNsD-9U6Tp4NPOcLrZevvtmylnxhLz_QJtGXD3Zr5gJzQ_dYVvst-poBkJLUQb7hFODIa2MaSmGdB4UsxPb04rc4j2xmSPCr60DhAs-0b4Zya5QbA3djKPhrPBpnxiU4VrWPuJi2XQ8EYu4XOj5qf95wMORvXC0igwd2cqtnTHAvderSjUHQeK1l8HFXVjp36v9MjqWeWCpuuTfilT6gIznQZHke7eOsNGCKI6O-E3IE63HhcGLjOiSBqr2hyt4Hv4zjQacTmczGdeQ5ZP0gmYx6yt5YG4o9v5UKwJIb5OkQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازدید ۲۰ میلیونی نامۀ سپاه به مردم آمریکا
🔹
نامۀ سپاه به مردم آمریکا در سکوهای داخلی فضای مجازی با ۸ هزار و ۳۶۰ محتوا و ۱۵ میلیون و ۷۷۰هزار بازدید، بازتاب پیدا کرد.
🔹
این نامه در سکوهای خارجی با هزار و ۶۶۰ محتوا و ۴ میلیون و ۸۸۹ هزار بازدید، انعکاس یافته…</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/farsna/466393" target="_blank">📅 11:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M640Xi7SwltAA635Q11T2YFJtr8bisKYdmr-yUD5kGopeZ4rarmlMFDB-CGwJDDr1YHOAXLGK8VbQ58PT7hq67ecueK3Mq17T2S91x4dwITrL4LB9a5PBoiNZQJEfTSr9Fugrm9x0alGKsYsKlfJU3QhqVOh3F7H_J6W4L2PytvrdtbPfBUEbXFICWMxzbhXij7Wj94H_liqjXfierDbei8Uz3gOyxGsmOol7LRg1zbgLiiX0IdBas7Qj9RO5lob4qmIEzRH-YH0QilAda5udzjMzKjE0mnlV-UuHmgV1yXU9lNWt7U0-UGvf1U5bMovWPARD53gNz4vTJW6hAhkRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقامیری: در کودتای دی‌ماه پایانه‌های استارلینک را از کار انداختیم
🔹
دبیر شورای‌عالی فضای مجازی: در کودتای دی‌ماه، سایت‌های غربی گفتند ایران اولین کشوری بود که به‌صورت مدیریت‌شده در بازه‌ای که می‌خواست استارلینک را از کار انداخت.
🔹
البته ما چون خودمان انجام داده بودیم، می‌دانستیم اما آن‌ها خودشان اذعان کردند.
🔹
ما در آن دوره یکی از فناوری‌هایمان را درگیر کردیم و فناوری‌های دیگری هم وجود دارد که از لحاظ فنی کاملا عملیاتی و آماده است.
🔹
اگر این باب را به‌عنوان ابزار جنگی استفاده کنند، می‌توان به عنوان هدف مشروع نظامی در آینده در نظر گرفته شود.
@Farsna</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/farsna/466392" target="_blank">📅 11:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466391">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dLjdnV8fQWWvKI_yXrrf__mEK6oTh7K3Xw4ap8-yay4ldBK-j0LCSmVlhpxOPM5RcTcALse33JHXwEvDv5bF_9AdQExBPDdg0BwfLRCeyS9-gTpbEnvkTHwaeqYAyVQu1HSTaA4x-tiUPfM6qG8AgDejPxoXWJl24bpgaVTXwzc7pfXXip5PFww7QJsBgOr9Aivlm0BAuWkjejXKbmduTAhMunX8i1bbHeMmGHOEvbEQ6N7cgG7twlroVHNdTKjXh8TgrhUR2rBmUjQfhqCaxOe_TKEkM-Pl1uAphiRVLZwCdNcAEISMMiNprEtkJr1HQaFpwtLJmTwTfkS97IssSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار عراقچی و میرزویان وزیر خارجۀ ارمنستان در تهران
@Farsna</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/farsna/466391" target="_blank">📅 11:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D77YDam32BwsKGfXRFGGDbVf4BXbBo2160ZsA0Il2pP1QH7DlEsybHGWFhA9lj_Lnqbz8KL-chQr-1_CxTZK8URbnHM1u5qngJfF03PJkgXCIw9tvfcsGKToeVq7f8fvgC82Q2jJhnM5CWD7w2RloZL_Kr8_YpF3nEfGzz0JT4CHTG57XKu7jP2BqXJEx0T2jU8Nt5DfqDT3AEwV7ZLQy3MLSZVLMgfiaCCF5KQRV5_LLD3qeQUfmQDIDlzjLHhpc086GC24-MhnQWy9wNkoTgEqPjSrY_Tp0JdL7sQU96Cjhyd1UV6VLnJ9J-9CUZGInfXj9C1gVMmDz1WiSfaA9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جلسات مجلس از هفتۀ آینده در محل دائمی صحن برگزار می‌شود
🔹
سخنگوی هیئت‌رئیسه مجلس: طبق مصوبۀ شعام از هفتۀ آینده جلسات صحن علنی با سازوکار دیگری تشکیل خواهد شد.
🔹
براساس تصمیم جدید هیئت‌رئیسه، جلسات صحن هم در محل دائمی صحن و مکمل آن به‌صورت وبینار برگزار خواهد…</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/466390" target="_blank">📅 10:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgShqAsLJZP65P_qEThlCVm3oidUzQvMvZF0ZLyjdczgARxtSj6PRFr2IL1h7gSqmRWywC0xp25F6QQKC4pCo-osVuRmVR6smPN1drI6MupAqXqlcGR_dNg6c-h4W_J71xNKHx8pCSMfrV4aNBCuJZd_0M2A7Z0GnjG1idWLDtfqTZlUy_OlPeJRLJv4o8hhZlCM4HdbnggX612jM36waEyDrZUyldAheq_S5wJy3jWaI0-r32xc-_g5OXgietyLRX-D6bAQaxbp2Kvvld7PRyBhNI1kw1_Mr-q2xreIF81hlrM_iSbvlBMUvXAP8MYF_8wGwQNQiQCMgQdlGb6IyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گزارش مجمع وزیران ادوار طی نامه‌ای به رئیس جمهور به رئیس جمهور از عملکرد دوساله مدیریت گروه صنایع پتروشیمی خلیج فارس
✔️
هلدینگ خلیج فارس با عبور موفق از تنگنای دوران تحریم و جنگ وارد دوره «جهش سودآوری و توسعه» شده است
🔹
این هلدینگ «دوره رشد و تثبیت» را پشت سر گذاشته و دوره «جهش سودآوری و توسعه» را شروع کرده است و اکنون از نظر اندازه، سودآوری و ظرفیت سرمایه‌گذاری وارد مرحله و موقعیت متفاوت از نظر خلق ارزش افزوده بیشتر شده است.
🔹
سود خالص ۱۸۷.۵ همت سال گذشته نسبت به سال قبلتر ۶۷.۴ درصد رشد داشته و تولیدات آن به میزان ۲ میلیون تن نسبت به سال قبلتر افزایش یافته است،
🔹
در صورت تداوم وضع موجود، این میزان در بازه زمانی منتهی به خرداد ۱۴۰۶ به ۲۲۰ همت می‌رسد.
🔹
در مقطع حساس دو جنگ تحمیلی و محاصره دریایی، علیرغم تمام سختی‌ها، روند تجارت و صادرات هلدینگ خلیج فارس به‌صورت شبانه‌روزی ادامه داشته و در بازه زمانی دوساله اخیر، قریب به ۱۰ میلیارددلار ارز حاصل از صادرات محصولات شرکت‌های تابعه هلدینگ، با استفاده از سامانه نظام مالی-بانکی فروخته شده و به کشور بازگشته است.</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/farsna/466389" target="_blank">📅 10:55 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466388">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3vpoiZOZrW4L01AxHY9cVogowqszyX_p_vINvsMj8LZrNxYtWT5rb0kAmrKLwX5vrOE_r0hr6gB8DPZpBxNAxfPjpYccLv6fxRg7-Yisd0x0GaiHjYdTROGpEDqx5eRNazKwL0S2AKI61GbdKO_vVKNLDJghRuagD-hl0IhH3vqn26d3yvIxnuq3w4opP6KLaiKvWXCs9bpOS9kzzkyc4NjU4ovtnsXDroc7iZo1cK8scttfc_x6LJj7zAv8FYoMbE40xY3jYeC54ad4d3fFkJgoFqOT3OqDQlVkCJvXqvCQcDjLfJF9LeKgxHdgSDoPAWrOfTuXpJA3kIW4M091g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرداخت 8800 فقره تسهیلات فرزندآوری بانک پارسیان در 6ماهه سال 1405
بانک پارسیان در راستای حمایت از سیاست‌های کلان جمعیتی کشور و تقویت بنیان های اجتماعی، در نیمه نخست سال 1405، عملکرد موثری از خود نشان داد.
به گزارش روابط عمومی بانک پارسیان، این بانک در راستای اجرای تکالیف خود همراستا با سیاست های کلان جمعیتی کشور، طی 6ماهه نخست سال جاری، 8،861 فقره تسهیلات فرزندآوری با اعتباری معادل بیش از 7هزار و 860 میلیارد ریال، پرداخت کرده است.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/farsna/466388" target="_blank">📅 10:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466387">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/farsna/466387" target="_blank">📅 10:53 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466385">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J4-SzHDXSMmYVANiJOE7ciA4hpvzkCka9t-a0WmrfHez_eEAy1Cpqf4yQQkmlJEuCkwFhNQrBwEkT4KWagOHYrUs5ALdPnpF66IRgcQxwWYpwyKO3eeQKHrj_D0tkGDMfMif-EQUH7Emr7M5vNz7eoUrGTTI4nwfzrkUjc9zRUr1GkgwU4QpbvogRrAH6M2nd_wDdWXEw111t-0nCUAB_0ppmelahFbJ3xLww_VazfH8tSWxS-v9_G2yaGBC_qalG8KQOxtuoEIm4jej2j_B0RYoMy1UXTqddavMIvKr6k4i79e62B73rSIyy_smFQ0U7GXtdJ5JSMePlJzNjx86Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C2jSgQc8zMvKt8J1gtKtMrcfGzVp0E6LGKJh_jzK-85lOP2GELHz9wYJPXRfSx3klcsAyKV55AauK8KmuRpxRZpPUgohYkZMcsfHgnTCS2ybzitJw-jTx_SgMM4bJ5-hbRkVtChXt11wtCaD7OFvP18TfJusiuy441-NcORkn_TfEk7iwMCNz2lqXToSxUWUfa4tozsu_SdJybypELLw0v97kTSzh6nrIwC4BDfuTYnTPysXyib5goO2hfOG71UKiZ5gtcexQfGm0vXA2Adr0ru4hCOU76VcY-naNarZhGTzuRxNBT1-F6eY4Pza68SnC2lTH2gQu8j2sUz8_Q1c7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شهادت ۲ نفر از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
ساعتی قبل، تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو فرماندهی انتظامی شهرستان بمپور که در حال گشت‌زنی و تأمین امنیت مردم بودند، حمله و به‌سمت کارکنان انتظامی تیراندازی کردند.
🔹
پلیس سیستان‌وبلوچستان:…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/466385" target="_blank">📅 10:18 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466384">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HYh-v9x2WuE75w_rZyGeqUHfkJqX-4BkscsWdk4zUFWkrcms9dwywU3kPHH3fE-Uz6HRUDiwGG2Hm9qBNsqoYdzAAAennE0IkkXuE1xsIljG-DhIZiXD9QtHitJgzhJGOb_VRJ8zPQXdrqwI3Io_WJQX0cD2ORr1M4LqBW6iXU2aVP-MN6pp4XSt4IimOMjizUCt92wqCeZ4lk6yrd46AeXQCEXr2NxGtr_m0qd-YEEBTwt4K46WrWCkBuR1E8ZlSBxEbkI9ndT65yhxdvujKn8uziOCqpbA81Z2r0U5XGgrY4bviNr-LjMDOWPV1eQg3Z4vOpFocKVWyUjv2-LhTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/466384" target="_blank">📅 10:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466383">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f778845b4d.mp4?token=a3nW16eO6oEyVIoXVFhXcj2ecXIi7-h3wynt9C4KJIDQqTNw7_UL-8EoJPHu__7wbbAGrXurx_TC8sXl5CykmN1KNFWoplgTbIFfI2JpTvPYyFrnee1jrx3PMql_I7819SF2C0WPeW6OJ4YpEy7XoYvW6Y5V7mqC7qrgQo_2pNIKNLPRihmFBo-CodmdoWLsw0YCQDMluYibTkmi0P0U6WGfE5XNcQspSaFobYAp2fSS2DcbEgr_fd3K08Zo4pHU8MW-tVUFlEssfs2wKBa-8MewMtUFDHvnJDUqv6Yu1wJFdYt-JRN589tFS6J0cDVTOypMCYFA9CW9nEVy8HCiEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f778845b4d.mp4?token=a3nW16eO6oEyVIoXVFhXcj2ecXIi7-h3wynt9C4KJIDQqTNw7_UL-8EoJPHu__7wbbAGrXurx_TC8sXl5CykmN1KNFWoplgTbIFfI2JpTvPYyFrnee1jrx3PMql_I7819SF2C0WPeW6OJ4YpEy7XoYvW6Y5V7mqC7qrgQo_2pNIKNLPRihmFBo-CodmdoWLsw0YCQDMluYibTkmi0P0U6WGfE5XNcQspSaFobYAp2fSS2DcbEgr_fd3K08Zo4pHU8MW-tVUFlEssfs2wKBa-8MewMtUFDHvnJDUqv6Yu1wJFdYt-JRN589tFS6J0cDVTOypMCYFA9CW9nEVy8HCiEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اینجا دانشگاه است، مبدأ تحولات!
🔹
دانشجویان دانشگاه‌های خراسان‌شمالی این روزها با برافراشتن پرچم ایران، پایبندی و وفاداری این محیط به حریم وطن را نشان می‌دهند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/farsna/466383" target="_blank">📅 10:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466382">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شهادت ۲ نفر از رزمندگان اسلام در سیستان‌و‌بلوچستان
🔹
ساعتی قبل، تروریست‌های مسلح به گشت انتظامی پاسگاه نوکجو فرماندهی انتظامی شهرستان بمپور که در حال گشت‌زنی و تأمین امنیت مردم بودند، حمله و به‌سمت کارکنان انتظامی تیراندازی کردند.
🔹
پلیس سیستان‌وبلوچستان: در پی این حمله استواردوم امیرحسین قاسمی و گروهبان یکم نظام دست‌گشاده به شهادت رسیدند. یک نفر دیگر از کارکنان انتظامی مجروح شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/466382" target="_blank">📅 09:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466381">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5BlecaF9A2eYVtnkO3A42TtN_zGV-yz_d-dxlwCiNJAbRAysUnEnJqvM2FcDkYJslt5oYaoDAlr4i6v4t6hA2nS2jF6CgbyvnANYtgEwdxh9JVLluSE1gF4KGXBFD6Jc25P7Ou3f9VpnNFLtom7m2-a--0BsmaCZausvSPJJ8jx-dQe6nZ4TZHyt9uuiiaR3ER-9u9WOlwZfvFnf1xj3PExwh45cKnQMus_V6nOFFNyJX9t5KaPVo5jGjiun8XF4ZU8EgbE0UFxGrAgfgndKZqw7g0E1e5nlgfZKqG3MkGs3Kz-5R5aFE1BfqC1TZidlTnCpweScZfR4mTy6D1NDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد انصارالله: تعز عملاً آزاد شده است
🔹
عضو دفتر سیاسی انصارالله، با تأیید محاصره کامل تعز پس از آزادسازی مناطق اطراف، این شهر را عملاً آزادشده خواند و تاکید کرد که این پیروزی با مشارکت نیروهای بومی استان و حمایت مردمی به دست آمده است.
🔹
حزام الاسد در گفت‌وگو با شبکه المیادین همچنین تآکید کرد که نیروهای مسلح یمن جاده میان تعز و عدن را قطع نکرده، بلکه آن را ایمن کرده‌اند، در حالی که این طرف مقابل بود که آن را مسدود کرده بود.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/466381" target="_blank">📅 09:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466378">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuhMLxzTHZBj83wdI8Rmyn8sYQQlnDC68Lg1DOT5VpvPCEXlGr407Yzhfo6EZbfWBW_cuxANzfLmJGU0tnTFIiDdYjGcnT503emxZ0AUymHLLR_2jzWann-rX6ZfHrUGyUFSTzux39EC9cwoRFP-PNidcqi725U0CjvAJjtyGjarNkKLA78JXZHlxH86_r7WajfqQAqs64tZ9cUo0-25bEWW6EhhAEGLhAhHPUTd77cDsflmiTAAa_PzdVECOrOY9EArobfTajMo0rZFaTFwKlqi7OS8EwmGZJww6jMJ4Rwks6QZiUo-Qe1MGqwKFrlrHiA00o8pfm5WNmOF7D7fJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fb3MSZp9equvFlqr8_Ih-UuvkpJtD2woRfuPiyKe_RW9vwptp04sMdeyVNu-FaBw2KD2WnZuN7iXvEg57mXDYjmmxQM1Q_GDWBO5Mx3OposXRiVFUHOGUIhQqDFCLj4jKXzGuFEsCmUNinA2DF1M26cYLV1_8162mEECWR3gLwXOc6RhLDJsnCP-TmxKPEv6-9ho_3r1slYv5vY4dqsEGXUFv3NxSnnCeeF6L6kdWs6K1PVgyQH6kQiqRdZLeXpHe4Sp1s_Zj2eYqTsiQ0AJXqbhDKB9suDDBKpJD8BHOBjIrmcsNBHRdn4uPBfNmGpVMLavkUtWtiJlj6ETk0VIfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rHU5WvlZwq3olJhnMapr3nr4hds_xRlKTgh98IhDENVDQk8_yBaVg1DdmVdUJl1srq1-aCR9KUSbONcVBiGSHPpn5ydN5LsW8ks-TEjWrViugbN-ezInwmNkFCwkSq8WsqWPb4rUuHcVTFoxZ_xVuTsJ9bV9pVUi_1H6JLpxW75VLyAoJ78xXUpmouey1MJnTj14qVDUUFoi89M9-XjjktYQ_tZR_yFZtJqI5rmaVpMXskRzWjsFjnXKBMc_uy5jmSbmR10YeFVxTcUC9wuox4aFNB6msUDGzLvxrAuhyO1N33N8SeQ6-tqiRVWQKPE6UlEbvzQpwaKq92wdVBBXPg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
زهرا زارعی در دوی ۴۰۰ متر مدال نقره را بر گردن آویخت  @Farsna</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/farsna/466378" target="_blank">📅 08:50 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466377">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316cf2ab4e.mp4?token=HE5q0MxrdIX1BTopEFirkDfP_U3u5ANYFH9-3W_FDUMU0CW45odyYfOtdoVoQw_Ug9TwLJ7E_cC7iqp9ORrYyXFNBPurLevNoFRccD1A5i-5UhxmneuVoafZmD7wAksWkS4WWqazaxsz80v4Udho9vgGWnWTIbEvLjLIWym6yZLMIrJlPirVzDiFtDRUHbIxTrAYZixfOsTgNa9sIBj4dF9nyoqxGalrJ_DIKgqWJdK0fZ7EC5LFj0rs0YMLbFH_gqVCOIGouZzTmgZ7jcKUuUNzy5M4xg-sILq5tYNz1DiW1I9pl-xPx_b-Vfp-oQl-0pOTElMLDFTpf0imIeTtXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316cf2ab4e.mp4?token=HE5q0MxrdIX1BTopEFirkDfP_U3u5ANYFH9-3W_FDUMU0CW45odyYfOtdoVoQw_Ug9TwLJ7E_cC7iqp9ORrYyXFNBPurLevNoFRccD1A5i-5UhxmneuVoafZmD7wAksWkS4WWqazaxsz80v4Udho9vgGWnWTIbEvLjLIWym6yZLMIrJlPirVzDiFtDRUHbIxTrAYZixfOsTgNa9sIBj4dF9nyoqxGalrJ_DIKgqWJdK0fZ7EC5LFj0rs0YMLbFH_gqVCOIGouZzTmgZ7jcKUuUNzy5M4xg-sILq5tYNz1DiW1I9pl-xPx_b-Vfp-oQl-0pOTElMLDFTpf0imIeTtXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دزد خانۀ آقای سفیر دستگیر شد
🔹
پلیس تهران سارق سابقه‌داری را که از خانه سفیر فیلیپین سرقت کرده و به اسلامشهر متواری شده بود در کمتر از ۲۴ ساعت شناسایی و دستگیر کرد.
🔹
سرکلانتر دوم پلیس پیشگیری تهران: در بررسی‌های اولیه مشخص شد فردی که به‌همراه همسرش برای انجام امور سرایداری و نگهداری از فرزند خانواده در این منزل مشغول به‌کار شده بود، پس‌از دسترسی به محل، اقدام به سرقت یک ساعت مچی طلا به ارزش تقریبی ۵ میلیارد تومان کرده و از محل متواری شده بود.
🔹
اولین اعتراف سارق: با حقوق ۱۲۰ میلیونی سرایدار خانه سفیر بودم؛ ساعتی که دزدیدم ۵ میلیارد قیمت داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farsna/466377" target="_blank">📅 08:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466376">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">انتخاب اعضای هیئت‌رئیسۀ جبهۀ اصلاحات برای سال دوم دورۀ سوم
🔹
در جلسۀ امروز مجمع عمومی جبهۀ اصلاحات ایران، ۵ عضو هیئت‌رئیسه برای دومین سال از دورۀ سوم فعالیت آن انتخاب شدند.
🔹
آذر منصوری، محسن آرمین، سیدحسن رسولی، بدرالسادات مفیدی و جواد امام به‌ترتیب به‌عنوان رئیس، نایب‌رئیس اول، نایب‌رئیس دوم، دبیر و سخنگوی اصلاحات انتخاب شدند.
🔹
هیئت‌رئیسۀ اصلاحات از ۱۰ عضو تشکیل می‌شود که ۵ عضو آن شامل رئیس، دو نایب‌رئیس، دبیر و سخنگو، مستقیماً از سوی مجمع عمومی انتخاب می‌شوند.
🔹
۵ عضو دیگر هیئت‌رئیسه، رؤسای کمیته‌های پنج‌گانه جبهه هستند که پس از انتخاب توسط اعضای کمیته‌ها، به ترکیب هیئت‌رئیسه اضافه خواهند شد.
🔹
لازم به توضیح است که هر ۵ منتخب مجمع عمومی، در سال نخست دورۀ سوم نیز همین مسئولیت‌ها را برعهده داشتند و مجمع عمومی جبهۀ اصلاحات بار دیگر با رأی خود به آنان اعتماد کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/farsna/466376" target="_blank">📅 08:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466375">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ba26dbe8.mp4?token=dv-LrwjNzkg8daBvzuCxBIAnxzNkkVRh-irH64FgAgMOCN7qGbGl6ZkpNFD9jQQ5za39GslQyJqPfd7EHSMGwpofiDP0yOrSoIw7B659dv2eDYmjnh5kJGaSFGgzqFs3AAFaOABlJl7xablDbmSGAPLWoRU7DQMvRox0Pv0SqERr0cVBjwOYD1o4dNmgB54bCveYa53FTXwnyRTr7SwSQyawI87m7ikNjeaePQKrQjEl1btvx-2jx_pJXXRnSGmTPB9fvEX6ryNiDRTNGDsmCJHU7KK5qUuJ7xnDie56Gk7EKe1GxuhSnsCo2nBgQUWxOlDVf5ZdOv-WT-xW6GezkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ba26dbe8.mp4?token=dv-LrwjNzkg8daBvzuCxBIAnxzNkkVRh-irH64FgAgMOCN7qGbGl6ZkpNFD9jQQ5za39GslQyJqPfd7EHSMGwpofiDP0yOrSoIw7B659dv2eDYmjnh5kJGaSFGgzqFs3AAFaOABlJl7xablDbmSGAPLWoRU7DQMvRox0Pv0SqERr0cVBjwOYD1o4dNmgB54bCveYa53FTXwnyRTr7SwSQyawI87m7ikNjeaePQKrQjEl1btvx-2jx_pJXXRnSGmTPB9fvEX6ryNiDRTNGDsmCJHU7KK5qUuJ7xnDie56Gk7EKe1GxuhSnsCo2nBgQUWxOlDVf5ZdOv-WT-xW6GezkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمریکا ۱۲ بمب‌افکن B-1 را از انگلیس خارج کرد
🔹
پس‌از وقوع حادثه‌ای در پایگاه هوایی فرفورد انگلیس، آمریکا تمام بمب‌افکن‌های راهبردیB-1 مستقر در این پایگاه را به آمریکا بازگرداند.
🔹
این پایگاه محل فرود بمب‌افکن‌های آمریکایی برای انجام حملات علیه ایران بود.
🔸
طبق گزارش وال‌استریت‌ژورنال، این تحولات پس از
حادثه‌ای
رخ داد که هفتۀ گذشته در نزدیکی پایگاه فیرفورد در غرب انگلیس اتفاق افتاد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/466375" target="_blank">📅 08:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466368">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIhtaRkAyzTzeZNrz-zB4QHAKkoVs6ECAfTYuVq5XgCr63KJA_IryPbfbFaAin2aGLbTgbbpZuFd9QaLhyCcPswlBdUoSgtXTQrxwPXj_UQlN-5YxRQZNfqZbVLzyvqv-8_3B89H2K_66Cva6MQMbZLy4kLupTPfmFC2uhCNNp2Zek88CUeXolQrTv0CiLAKlStt_UkaanXZR1YnVyjgSgaWbm_Gw9gGO1r1bJvvr692_5IaWktUKqUFBGAeTGfvK-4FiRN_SObodCQSZMzO0rPcVpxwSxrSv8UTJjnFh0orK7uavt48hHBspzt-5ZGNzyEP-OuQWhKhrDPaakpSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GTTxLpUTfVOa5st8Wo7nnQqZpPARY0ireQlgNSVhuGurzk5pgjnYbXQrdgh8mhMEAh7MGZBULL1CU6k5fxILGhOvkCplrFOQRfdII_d1JC2ia_9nZ3aSJZkaYo1sSCwqF6OHb_RRuEc-yyYR-C5BrkE5Tf3wawH7QtlTp7FstG9m_Q3FfchTlvg48q-EaWIbyGXtN5oJ98bKu4yOJRw3Zkjc6R0DImnsoSnKhen57E9r9lhZaUKA_aM9AXZi-aiDQ7adrIJLTBQTaPzcgTYgtvW9nA3cJvb9nYF1ArIMAKVya6yHBsyGGZo5Bt7n54_IQoAtOmIpsW-U_GA9_kUj8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZBwBesw5eVGYnDmOQNPKfLbdWTGS-UYUhWl-9yHPCrwyC6fDpXEUK9I679nw3qwiyXE_N3zWxY9m4ZpDiVPcZe84K4yf7FBf4g9w4-Uv1zs8Ts6RCxy51aODyV4WvbaRcwtLuezrPHNgGX1MagO2OrhNCbCpUoIAePzdy67w7SB66Bb8P6IgI77CEq6xtm5A4a8zpFPbrhi5Z-1ufKpCw1vcFWILruOh2zUKSYTyqQwEnPPivkOWAlcerSEKAQZO0CdiEXPIgyeyIPDVLC8idXKkPT5fEHVqX08Pfu8Y3RewsXrcNszIzpJhXD1G-x2sbocheEH_DXaKHsUD88RQvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDNgNLFRE1K4NhhcfZ3yoPukca1gvcNZooVOCAkN6J9OpOWAeoZTh0pGu767BGa4KI-9OL4v3aO8S0ehaGHTR4DEGwiHjAmndkQ3QqJ6fJKqb4_vOAiWdORbNnrWotPQD3Z8dOvSFOAtRiE0L2Hwdx4wTbxsCNnskyAlCBCPNFDojXwBPIHMzanF3OLHQE6rEOK6uAbcZUvc86cD_JAIBjUNhSUgANJmPXqbDqblMzuNLSC0tXAklTBDtf-HAYt2Ou9H6zED6gsCo5HmV_ooxRA_ULEowgkCTsWfmaWg4g04hiyRpwkOnuniAbjQgVQjtbqr1ByL0T8yqK16VxAqQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ye925VUs5aAxDzbDHYJDWPYZTWsmLd25UXshtESH6UANKIErTZOMpPe2tjz9aV6ms7k2e5U8kxBseIxqho15CHZpeyVeK6sMbhxtUCvoiuHNwWfSa_fonD8lw2DSYgLNqw1xaMHx9J-x_Df4x0n_kkcmQqstORYI24VKBhDkJLg-nYWfcEkJ-KhtkoN9qswPc10Mngzzty3ETd7S3wnD5ey_GPbUMXCkHvUq-M26rdSpGcfO82M81pwtvglNugPu6MxlV1n9vhEuxcBmokxo4dNfp2NbiTK-_xWtaCA3vNbfhc_lEJstm98xrcxJXGYbB6YXeNQL-xzP4yiIJxIRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2qsus671cNnt45ZSdj6-e0VsKfUBUW8Cz9Xv4acMzZNGClThwkhU4QzmjNOnsIJTl9OzRbvzJmTF6CzWcRfZ0oJ95WFXw8RtsUhkYQ2yl-3AVgx8UA2ksmH0e0HbrvBwaPvpkZkTT4NEmn-uFMletKwHrQxYFJl3fY-2CM-jzCjfSVv14vhUrDDYvFByQtdSbkyZtde8A6HWM7PZjN31LZ_fiptPQfUfeAK_wC7KcUZusb9dG009pOW7EAtL8KvOsVg2RXUMaoqQ6RXCtd2zccikQA2S2zSI6c6aKZCpUCqPbq0EJW7f9wYh-lNdw1YZ-ymY_PfsbcLDP2_W4ikwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PCJSJpvLMjmXbhwM-uhBdOZA8xwQf4QWPY92MICIurQB2i-7B9IigQqe3FZjzfwArnVbIruNObVb80FkDOP3eif2-S0YJTdBcBxzi8abm4lF4_sz-ST4iL2kJLT-K5bufarSBFXsWN11ZP1obRFeGBi0S3Dz96UGnthoAqf-WSRPyV39DYl63aBYE9YhzAY02-PNDp6b31nEPLm_1VDZQNXDbnFNDabD4JKDLNH5RwrM0hc9EinADGAkPfXqioT12T6kb7NmlYlcNYqH0vV33gVx_xNnYcyEQHIVajTOP_rEgl0srsBS5fribDJIsceSojIklVDowqJCHGV9NeAIXQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
عرضهٔ ۱۲ قلم کالای اساسی در تهران با قیمت ثابت
🔸
شهرداری تهران با اجرای طرح «تورم صفر» نرخ ۱۲ کالای اساسی را به مدت ۶ ماه در مراکز عرضهٔ تحت پوشش این طرح ثابت نگه می‌دارد.
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/farsna/466368" target="_blank">📅 08:33 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466367">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af80ea68b0.mp4?token=rZgxplVR7u9xa_EbDaN3cndUn2qgzWNxHGUPQooLcRlp_Iu8fVSWa0Y-F97p4fK42hQely1k1IeQ_bsPX6HsURlXeP8FEc3rdDqH1HxQhyIwFXKeuXLJpBvE9unDPw1FNu5B-VkAzqc_yhDEB4deZ7HRfeJquZ8ISZF9eEdzU9i3tjcNG762YiSyK-TpeCDw-zCLAzDNGuokjKGWMh9JIdpUkeuyDsjaEy9keC0k885U53ZrNUYgqrZvISqAlXnhl9pHtBluPOk0R3xSoSMUTt6d8bqsXuZeAXjSYEi6MwLoJiM2td0oFsWM_g1ZPxV1LpTUx3BY25aR9V52hiB8EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af80ea68b0.mp4?token=rZgxplVR7u9xa_EbDaN3cndUn2qgzWNxHGUPQooLcRlp_Iu8fVSWa0Y-F97p4fK42hQely1k1IeQ_bsPX6HsURlXeP8FEc3rdDqH1HxQhyIwFXKeuXLJpBvE9unDPw1FNu5B-VkAzqc_yhDEB4deZ7HRfeJquZ8ISZF9eEdzU9i3tjcNG762YiSyK-TpeCDw-zCLAzDNGuokjKGWMh9JIdpUkeuyDsjaEy9keC0k885U53ZrNUYgqrZvISqAlXnhl9pHtBluPOk0R3xSoSMUTt6d8bqsXuZeAXjSYEi6MwLoJiM2td0oFsWM_g1ZPxV1LpTUx3BY25aR9V52hiB8EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چاقی بیماری است!
@Farsna</div>
<div class="tg-footer">👁️ 7.85K · <a href="https://t.me/farsna/466367" target="_blank">📅 08:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466366">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp6cWtMsTuk3wi8fkr-1-xFF84RmmEt-ofcNS8qBOsnIYD474Qn8tBDMk2eCnzAmzU77S-uBLQx5rW37BqTCbXbaY09obyh6JXERexO5uviaF2Xxr6PADkvEFjTrL1BUgdmYLkaAMwtD0NpxQTrxGXBtPKyIxn_DbcT-aJG61RtjcaW_Ke4ANqinS-5m9DqaIGVGRH_kqJd10p8OZ1KkintwCh6Dc6fdHqngX3oLqvaoXy4PomI8a3XDO7t7v537W9hNH3sovhkQrMhbgPuFJX0BCz1JCDuH25LyAhBN6atrD3hCxRT6RPX0t-_DsLsB-MJPqWw20T4Afei1Or6lcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح «تورم صفر» به زبان ساده  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/466366" target="_blank">📅 08:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466365">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Km3jEbDZKYf3SWEqaQTuMbKMTUDQbQI-TlYVsTqW8KVCz9DyUeDfpbaFMzSgS9atv2whoGwnSdP2LOvOfcDHBRvcyRVeh483HGMsG1sVE43OvG52Tr6Z6vVzSP89Wm15Me__z1R87jjlu5A3BhEV582aM_mCfCq1QF3qdw_1ulvhgX6s7qftjGAsNSitoDjXZjHSG-l0YC5jiWJQOHUf87WpgiSH_H72bnie2u1Wawvphd5HsmRJ_qtIfUrLh_P3wI-ymEno9UWIhgRridTWQR3rdo7tmIGswOg-ef5FJzKNCJPrqfYcbNr0LWjeBJdEDpqmhdEu0Qyasu1oY3k6yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رتبهٔ ۹ کنکور: می‌خواهم به‌یاد شهدای میناب معلم شوم
🔸
هانیه قربان‌پور، دانش‌آموز مدرسهٔ نمونه دولتی مطهرهٔ مینودشت که رتبه ۹ منطقه سه و ۷۳ کشوری کنکور علوم انسانی را کسب کرد، می‌خواهد این موفقیت را به‌یاد شهدای میناب و در مسیر تحقق رؤیای معلمی ادامه دهد.
🔹
او می‌گوید: ماه‌های پایانی کنکور آرام و بدون دغدغه نبود، شرایط جنگی و خبر شهادت رهبر، شهدای جنگ و دانش‌آموزان میناب بر روحیه‌ام تأثیر گذاشت و برای مدتی برنامهٔ مطالعاتی‌ام را تغییر داد.
🔹
آن سحرگاه را هیچ‌وقت فراموش نمی‌کنم. شب‌ها گریه می‌کردم و خوابم به‌هم می‌ریخت؛ حدود دوماه ساعت مطالعه‌ام نوسان پیدا کرد، اما تلاش کردم با وجود همهٔ این شرایط به هدفم برسم و دوست دارم این شادی و موفقیت را به روح رهبر شهید و تمام شهدای جنگ تقدیم کنم.
🔗
شرح کامل گفت‌وگوی فارس با هانیه قربان‌پور را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/farsna/466365" target="_blank">📅 07:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466364">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZNQHWQ4j8tsoIZnrZ1cYqG8oO5OHIVacIZi2MYZTois2BwX_jqKoncEjeDqsHM348iwZTDtU3U8ol3DkGtsfHrjBAIsH5hNbDMbPLBCz7xVoP5sMLB31hh_uQJrRaUKLBiA9ZGy7U-SRIi1e83PWPGbQX1I5EbRk2rTXKpKkLDItijAZrMOFOHBfJNzVLmbe1tQ8ibnTWGzbQ5hWWYwCeCdHldBB8XAP43po1E6aJAbLhO0dIyNb_a1jxAktNYSPNkLioA-zEF1tPxv7Sfqkp80Y5_cktAGHjzTShpj4iH8KtSmpRTW9iG_ISbgqZINkc9eLZLnGDyLdopBhztvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نیرو: افزایش قیمت برق در دستورکار نیست؛ اما برای پرمصرف‌ها جریمه درنظر گرفته شده است.
🔹
تقریباً تعمیرات اساسی همهٔ نیروگاه‌ها انجام شده و آماده به‌کار هستند. امیدواریم زمستان را به‌خوبی پشت سر بگذاریم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/farsna/466364" target="_blank">📅 07:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466363">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOYROqC0hYQIN5pYw6zJGFRAv1B9zZTBbgOXC1jr8wekTUkGtT2F_AOK5ncd8hwQ-N_rXG-ODYmtqe3rnpnz3_sX4FMAxemfp3iHqrznfEFp7dxe9PFiFBOytJNm00FCDUsEUGSunqrVeQfg0r1q79mCfa1vakAeyec68ZaEEaJfNWeL23Gw_53-MxnSrbNLVu5Gw94HneyMTzjIPnYOVfR4mVahpqNWgfaMM02WLB4mgI3SEYHv0vQHuh0Yu_4eaZKXpciKFUm-jDm3GDtpOd1QP0lEYy64UjqZT09BZ02eWjX_xUzOv-0pyg2DXpl5JZkKEL7X0tI_m7N1Pdgksw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز انتخاب رشتهٔ کنکور ۱۴۰۵ از امروز
🔹
فرصت انتخاب رشتهٔ داوطلبان آزمون سراسری و دانشجو-معلم از امروز آغاز می‌شود و متقاضیان تا پنجشنبه ۱۶ مهرماه فرصت دارند حداکثر ۱۵۰ کد رشتهٔ محل را در سامانهٔ جامع آزمون سراسری ثبت کنند.
🔸
هر داوطلب تنها یک‌بار می‌تواند انتخاب رشتهٔ خود را انجام دهد، اما پس از دریافت رسید، امکان ویرایش فرم انتخاب رشته در دفعات محدود فراهم خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/466363" target="_blank">📅 07:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466362">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oq2Bvgr98QMmmpCvm_54HiqRbGsa_yHy1y2XryhyxB4IupO1ooYmSgU3Zs9spdO1muuNhK-KBzkwWmAYWsch2qJBhXGpzC7-xPcpq4DiMcxfuhDu_Wzsn65gxYssIjDoiwVPbGyG2p4GKsVwR7_9_dFbz_u3zxPOruvcNEtn7ysuR_nWlAOBNwbeyQZvl2s0rf3KJOVJfK6Nd2D-dBtWpDMUz-G-_CNBbBTOvkpVx7NddJDl27W3fjyMAxR-StKnkcUI-sd8aHrkKy9htthXuepl8frIERTGfwFZNW65HOOE_OW2pGCi4SwEgmMwpJtaE1oMc5HACmoBS3oIHTaC_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پلیس راهور: اسکیت و اسکوتر سواری در معابر ممنوع است
🔹
پلیس ترافیک شهری راهور فراجا: تردد با اسکیت و اسکوتر در معابر عمومی ممنوع است مگر در مسیرهایی که پلیس با نصب علائم، استفاده از آن‌ها را مجاز اعلام کرده باشد.‌
🔹
در صورت وقوع تصادف، اسکوتر نیز وسیلهٔ نقلیه محسوب شده و نوع وسیله، نحوهٔ حرکت و شرایط تردد آن در فرآیند کارشناسی و تعیین عوامل مؤثر در حادثه بررسی خواهد شد.
🔹
هدف پلیس جلوگیری استفاده از اسکیت و اسکوتر نیست، بلکه پیشگیری از وقوع حوادث و آسیب‌های احتمالی، به‌ویژه برای کودکان و نوجوانان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/farsna/466362" target="_blank">📅 06:54 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466361">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌ جوکار: زمان برگزاری انتخابات شوراها هنوز نهایی نشده
🔹
رئیس هیئت مرکزی نظارت بر انتخابات شوراها: هنوز زمان مشخصی برای برگزاری انتخابات تعیین نشده و موضوع در جلسات کارشناسی درحال بررسی است.
🔹
دربارۀ احتمال برگزاری انتخابات در آبان‌ماه نیز فعلاً نمی‌توان زمان…</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/466361" target="_blank">📅 06:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466360">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
مدارس و دانشگاه‌های مناطقی از کرمان تعطیل شد؛ آغاز فعالیت ادارات با یک‌ساعت تأخیر
🔹
به‌دلیل افزایش آلایندگی هوا، فعالیت مدارس، مراکز آموزشی و دانشگاه‌ها در بخش مرکزی
شهر کرمان و بخش‌های چترود، ماهان، شهداد و راین
امروز تعطیل است.
🔹
فعالیت ادارات، مؤسسات عمومی و بانک‌های این مناطق نیز با یک‌ساعت تأخیر آغاز می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/farsna/466360" target="_blank">📅 06:21 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466359">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgdTOQ26kIVxtM0qwQK034dElcsMkpunnO5MSVc5eiYseOE0o27ZAWVUxy2L2aVAUPavcZWIDsomKi3t9jPXhI04pazYAKEqX-a1qHZXMH1Ee1MkoUiAkfPrv8i0FJ0TDClYO-SGBDUu3vwcsMSlRY7e845bIJaRzxEwlCL3qAsPWlWmNoVw3kmsjwMd7sAXT76ARnZyF4Hh7u_kWbc4pCxQsiAk_XZn3eu_pEugXcuwZBPFj9GX7DXgVbT7TI724s3zrZQESKJ4pVSAwF5w8RbNF0xxu63d0gsB_99Z8-yY7bEKd7XVMANxfQ7cRAwRXuVsM70Xmik7yl9yd-N5TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجوز شورای‌‌شهری‌ها به طرح معیشت
🔹
اجرای طرح «تورم صفر» شهرداری تهران در جلسه امروز شورای شهر با دفاع برخی از اعضا همراه شد.
🔹
سروری، نایب رئیس شورای شهر تهران با انتقاد از نگاه سیاسی به این طرح گفت برخی می‌خواهند با نگاه بسته سیاسی بارقه امید را از مردم…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/466359" target="_blank">📅 05:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466358">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLQlOxve9NwAwX4adVpiW3-Rif8JVVR9Wx91hF_Fh9GnSuP_9JKB1CVpS8mFZsCI0RoiKu53U22IgBtTKWLxKP2QNyqqDd8XAsHpT9lOxW1X3gMZtDepM9BE3S-_a5r0j4plJzVOjRCSXzXDIySMhZ_-1cJ3Uw_HzsJGCX-ZY5inf1kiFdFAWsq8o_myQ1Hv6CmdXjwi61rjzEkaZEwtaR5w4JaGRIA6SAhq0O2BA1wKS-3bAdlNCY3xABqt3xD9CSR-msbva3o4PLIZC3jYwTX2HGTKSngkHKZZUpBTa1ubDM_ulkMyDU05O3HDvwhz2fm_qqgFyfFUlwCtcwiOgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۵۷۹ مصدوم و ۴ فوتی بر اثر طوفان و سیلاب‌های اخیر کشور
🔹
سازمان اورژانس کشور: در پی حوادث جوی از ابتدا تا ۱۱ مهرماه، ۵۷۹ نفر مصدوم شدند که ۵۷۶ نفر از این تعداد در حوادث ناشی از طوفان، و سه نفر بر اثر صاعقه و رعدوبرق آسیب دیدند.
🔹
در این بازهٔ زمانی، ۴ نفر جان خود را از دست دادند که دو مورد به‌دلیل وقوع سیلاب و دو مورد در پی رعدوبرق بوده است؛ یک نفر نیز در حادثهٔ مرتبط با سیلاب مفقود شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/466358" target="_blank">📅 05:30 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466357">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuUTgG09CGgjunk-6nUHFJpAE4IN0XMD_v9mvrRrCE9G5BR3N3HwPCeb4y0nQudckPYbcftoDRk9h1AJKWxMPiW9KpBSTfWn0vIn1YwxapwOd7ta4W6sOyY9eQP9ckEQq7_SMf43xpHBX5cC3sFCkxivdMKw4h6T3mbaX8Cl3emrd1KGZv1FvQvUI-aql0Vwe80951o_j-MjoBUW7M5WRXFcJyw1HYEAAvfhHnJ8fDZ-OBARK_XubLAkmqdXoppK7bAFLAPBMMJPzvxC071PUFS04SGhYCDADz3pAQ49FPLY7WRVyFMMD7ANLTalg_K0B29FxEBKZGxqFEUe5KIQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ مشهد: شهرداری‌ها به طرح «تورم صفر» بپيوندند
🔹
حسنعلی اخلاقی امیری: همهٔ شهرها به‌ویژه کلان‌شهرها باید با ایجاد چرخهٔ صحیح توزیع و حذف واسطه‌های غیرضروری، به کاهش فشار تورمی بر مردم کمک کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farsna/466357" target="_blank">📅 04:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466356">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Znuk3gFFNwgnhVTZO57fBtLfNVYgGKaWJ_YPqeU_-uCMvN6TCZOeVygf8I5ihEcGo4q2pCzLMJQNrH1ZPagborn_oyatFHUJDET3hbj2bAAIKsc6CoyHQUcCaeMamX_Dz4fwvxhW3KVUBSVDyVrcwfuCdL7-pbBrCGLV7VDAIJF-_6JHlaC1yBBQ7LlreI2m4Z7GwbxWFNXP79QReVtjTu21drt3XXYZjhhpt7H_9V8QHqlux_aOR7m6HI5wXSyiiP91I8Li8VjMFts9u0OYmYPGKFioHqaFc9pTTrb6Dyh6rfgOz6W3ztqHLjTfwzfebfp4nWJnrx3bP23pMz1KKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعیین رئیس‌جمهور برزیل به دور دوم کشیده شد
🔹
انتخابات ریاست‌جمهوری برزیل پس از آن‌که هیچ‌یک از نامزدها نتوانست بیش از ۵۰ درصد آرای معتبر را به‌دست آورد، به دور دوم کشیده شد و «لوئیز ایناسیو لولا داسیلوا»، رئیس‌جمهور کنونی، و «فلاویو بولسونارو»، سناتور و پسر رئیس‌جمهور پیشین برزیل، برای رقابت نهایی راهی دور دوم شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/466356" target="_blank">📅 04:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466355">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iTzu5gG-TL3glUOYzdEuMa6AsMEF9uHX67ZYratG-upLP7-NL9uoA6ycbkB_8LrryAXifpncvTj78M32enVSbXYvSVSpjnbiknjbiBLvOU8_5mSRZlvTCOazhckTTgiMt13FdpPskPHfnGelKlSDLsuL4e9IfsoaCE38yME7pxnh_Y2d12yHK8Gcdc50qH03zdD-onMucMOUglKglkPK6s7roXWi0MmIrJFIDMhtFzY7LU-_VGS62GhIlnIiK9I3oEcRhrD7g-OXL4xuY4ye3augyryI3aSQyHN_rxASa7-xd2v1kI7loqUo3ZqiY6XTPQD7vfHa63BUMoJgMIxb1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گوگل با خبرنگاران جعلی برخورد می‌کند
🔹
گوگل دستورالعمل‌های ارزیابی کیفیت محتوا را به‌روزرسانی کرده و ساخت هویت جعلی برای نویسندگان، ازجمله استفاده از نام، سوابق حرفه‌ای و تصاویر تولیدشده با هوش مصنوعی، را مصداق فریب دانسته است.
🔹
براساس این دستورالعمل، سایت‌هایی که با جعل هویت نویسندگان وانمود می‌کنند مطالبشان را متخصصان واقعی نوشته‌اند، ممکن است اعتبار و رتبهٔ خود را در نتایج جست‌وجوی گوگل از دست بدهند.
🔹
این تصمیم در پی گسترش رسانه‌هایی اتخاذ شده که با تولید انبوه محتوای هوش مصنوعی و ساخت خبرنگاران غیرواقعی، به‌دنبال جذب بازدیدکننده هستند.
🔹
گوگل تأکید دارد مسئله، استفاده از هوش مصنوعی نیست، بلکه جعل هویت انسانی برای فریب مخاطبان و القای اعتبار کاذب به محتواست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/farsna/466355" target="_blank">📅 04:09 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466354">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">منابع عربی از توقف پروازها در دو فرودگاه ریاض و جدهٔ عربستان سعودی خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/466354" target="_blank">📅 03:39 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466353">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kf7r1zXnRDf6EJm7kD4ee8ojBM8rgIHi3UV9vV7PX8JXXuog36qHbiA9vNnkncU2ja7LkEAHYsc-nocjqx3L3AQgkehcbl-v-xco8W9wQkVJHNmpv2lJE0v2GyuesOTJWdmDFUBYZdMPH8E0uclPnTmUYjoUV2LnQetzg7S10pc6ilhDwFWJKQt9DSR-bxHJJ4eEkeJ_hYExgXedic2-woAGFhecNw0u2aQ0m3uEsxJpanpvxBwag5g5fkVXYvGJ50JNgDb9WWfraoBZLUyF7iY8yG8K5cU1NzsVqx29l-x-EOL-18158vYhhKomDdFtDQurV99TQZIf-Ez4M72JPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش آمریکا برای تشکیل ائتلاف سعودی-اماراتی علیه یمن
🔹
گاردین: کاخ سفید از عربستان و امارات خواسته اختلافات خود را کنار بگذارند و برای مقابله با نیروهای مسلح یمن، فرماندهی نظامی مشترک تشکیل دهند.
🔹
همچنین نتانیاهو در ابوظبی، پیشنهاد کمک به عربستان را به نمایندگان…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466353" target="_blank">📅 03:29 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466352">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52295b88bf.mp4?token=SxlotsjqCAtQu-N25FtSYnpMfsk2AWEPDWBbZxQfk4bvaUs5n2PvrI7qPwvTVHUoZoK3IIT9Q_UijWRm57PtDhcEjPii6uwkfmsN0Hfx4DzSl3aDCQcuqIQTPRZ_zpB0UUxiQGFtR1O-fhnjuP-wbERTKxNoKRqUwODhat4ym5CaTzAsHGRCgLCJCrXIJYmhHkpbjEy7_qJKxVoR4lv4zNQ2Nap0uZ0cNNc8RHyOD5K6uvklmYNSo_vlLoZmxlGHfMh6hsGrl-urFa_ECoTrOutiRpO7pGGq9toH4IO89kudQNwLQmBH67rr2YNiScXcFe5rabp9bVZbG__ct6M1wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52295b88bf.mp4?token=SxlotsjqCAtQu-N25FtSYnpMfsk2AWEPDWBbZxQfk4bvaUs5n2PvrI7qPwvTVHUoZoK3IIT9Q_UijWRm57PtDhcEjPii6uwkfmsN0Hfx4DzSl3aDCQcuqIQTPRZ_zpB0UUxiQGFtR1O-fhnjuP-wbERTKxNoKRqUwODhat4ym5CaTzAsHGRCgLCJCrXIJYmhHkpbjEy7_qJKxVoR4lv4zNQ2Nap0uZ0cNNc8RHyOD5K6uvklmYNSo_vlLoZmxlGHfMh6hsGrl-urFa_ECoTrOutiRpO7pGGq9toH4IO89kudQNwLQmBH67rr2YNiScXcFe5rabp9bVZbG__ct6M1wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جسم نماز را خالی از روح نکنید
🎙
رهبر شهید
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/farsna/466352" target="_blank">📅 03:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466351">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/466351" target="_blank">📅 02:57 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466350">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iT9yUaI3JkGdw7YOk8okP11InikiiRFR3tyoMwZEtkXOqZvRDc4gjTfwwmtfDzGNLwHMb-DhK-W9HBOeU4gzm4c3WnRnZS9h19cZpnZ0Ywg5Wb80hKfZqul6XqYWiUArmCYf_mgHIow7faGFCi03LvpNIrMtOKBvek_HAZ2BuE_L5lwc5uUM01ZQ9NlotsceorPMSUhJRaNRsebvp__sAeppnFFQ0SUhn1h_VNC7825RiozIJudDHa-FNccmujtHeWSmx7uen4YB5s7ZJ-bXfgBcDzxbYTf5og88-0PVc4ERdyy9nlqwX4hy3phCDBVPG1hQ7ieoJfCbuP3hYkGq-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دردسر تیم‌های دوم برای استقلال و پرسپولیس
🔹
طبق قوانین جدید کنفدراسیون فوتبال آسیا، باشگاه‌هایی که دو تیم دارند مجاز به حضور در برخی از مسابقات (مانند جام حذفی) نیستند و در صورتی که چنین اقدامی انجام دهند دیگر حتی حق حضور در رقابت‌های لیگ نخبگان و لیگ قهرمانان سطح دو آسیا را نخواهند داشت.
🔹
به‌عبارت‌دیگر باشگاه استقلال که استقلال ب سیستان را به‌عنوان تیم دوم در اختیار دارد اگر بخواهد همراه با این تیم در جام حذفی شرکت کند اجازهٔ حضور در آسیا را پیدا نخواهد کرد مگر اینکه باشگاه استقلال مانع حضور تیم استقلال ب سیستان در جام حذفی شود.
🔹
تیم پرسپولیس هم که به‌دنبال خرید تیم دوم از یکی از باشگاه‌های لیگ‌هایی پایین‌تر است همین شرایط برایش پیش خواهد آمد. مگر اینکه تیم دوم خریداری شده برای باشگاه‌ها در سراسر آسیا اساسنامه‌های جداگانه‌ای داشته، و کلاً از تیم اول مجزا باشند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/466350" target="_blank">📅 02:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466349">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9UPDABRlsYt22sWrpT_U4P364hBJqY15-KFoJi4eh6-l58pN0KiX2bm0kzEvZ0fPVlKt8Bz7KcTpNtj03usDjgwAakG1faXI71VsgwTkHgEiKihsW0mvVLdUaB2qSweTDRRHl6GoXERuOyzvFX0q396AB7VqqeggShapUVZsAMEimg-W4GBflvSSmJpI-O7Kt8TifsAK4hz9xFo35voCoohU6P8YD-Fh8SkLuufCrh5Oze1yWW1HOqVIDi3PUS6QBNe6cNZQHTlweDyKW_nEPZOQqsuLrwcbEK9axSEy8y3MKdF_RzA5bJ6te8a8C1SdWzCzeuSXcaf8wDqfoxdFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت سیاه اقتصاد آمریکا پنهان زیر سایهٔ افزایش دلار در ایران
🔹
اگرچه اخبار نرخ دلار در ایران، فرصت پرداخت به وضعیت اقتصاد در آمریکا پس از شوک نفتی تنگهٔ هرمز را کاسته اما افزایش تورم و نرخ بهره اتفاقی است که فضای رسانه‌های غربی مستقل را به خود اختصاص داده است.
🔹
دولت آمریکا در تنگنای تازه‌ای گرفتار شده و برای آنکه اوراق قرضههٔ آمریکایی خریدار پیدا کند، باید بازده پرداختی اوراق ۱۰ ساله را به بالای ۵.۲ درصد برساند؛ رقمی که بی‌سابقه‌ترین سطح از زمان بحران مالی سال ۲۰۰۸ تاکنون است.
🔹
بازده ۵.۲ درصدی، بازار اوراق را به رقیبی جدی برای بازار سهام تبدیل کرده است؛ سرمایه‌گذاری که تا دیروز بازار جذابی جز بورس نداشت، اکنون در اوراق قرضه پناهگاه کم‌ریسک‌تری می‌بیند.
🔹
نتیجهٔ این جابه‌جایی، خود را در سقوط سهام نشان داده است به نحوی که در یک ماه اخیر، ۷۰ درصد شرکت‌های شاخص بورس آمریکا، افت قیمت را تجربه کرده‌اند.
🔹
تحلیل‌گران معتقدند تثبیت این نرخ ظرف چند هفته منجر به ریزش گستردهٔ بازار بورس خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/farsna/466349" target="_blank">📅 02:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466346">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگالری عکس ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcaj59MT8mkipPtnJFaaARwDJM_us8o0mG2T_HtjrhIz1iwvQK9_sZGhpTlBoz1NFVI45N3EWrUnPxAaGOb8Gjph-iA3ogbUeIczmfis06pvPDvs4pdAF23l0Zd6mkn7uEg5IYY_fL6lrBoBl92vff_k5x8HMm3rbKpdtZqH2yJft4Ry5yg8N1kz5-iltus3dCHsFLV00PKYuIrq82hQT2g4KOwiV_A2rilHfZ50LAKnF8rYPiWXK95sRGN9mFbI0BjUO1wnRjd9a6HtsjuuObnSwPkS8yF-jO7PshBoaG_AaHNybEE9kXGsjdAKBf2zsw985XLKnUKdeNqjAtoH4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A90CBN4e564a0dZECHBlT72yrEsmxZY6mOaHnY7zRFT5ve7ZbCNUOTP2VeDXrCOpY59Tw6kaQPvtLyrSIh2kP6M5hdOhp6Ccp1Vgpn39l3KXfB11j61rpGVCHSGuszwd2ah0rNqdMw9KxfWxLudVVltMVa8CGiYY-gnFNTFZpk9DO03Frdh4Wv0X7D9tvSrOBiISH94jpDaKTewQWAhp30H5GX1U8EaPzX_88T5VgCTdn3Uy5sPqrmo_G3Ouog07a5kBKOZcKenT-CXRrOTk9FcBDmc7j-Owyq1UnW9WqLFoq3c69tlXXfiUSRALzIpUlNvunAZLeJ4ePdn51pUXGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGO_EZQNEnnBkJAcP0sUTFjccIuh3H3PLwjmNmZ9GEiGECdcfVY-Ka771iSF6d0AFIxhoW48dqSVVK653P1zKOWc8rNqOSAM00P9tdZDMSkuxTUFNjFP7ugf_rd5c4Xa4sYSFYef4iwccbq22RiJAjhD6q3FiC2aVSyJiaQd4gYWiwKVCyipWp-fkiSX4gtq7LxyS0yfr0B3LJlhIhtreyZKM7N4DiX8O9N4vuCEc8qiLucRCtbPm5tgJ2RznG6paBge22_63lCwGSircgvyfw8IvnTn3Uf2DnEIvOjV_U2CiSL69jSBBgp3aiJh9t3IP0s5-SP4C3nIEI0SPlXVuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ماه و خواجو
عکس: محمد سلطانی
@GalleryAksIran</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/farsna/466346" target="_blank">📅 02:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466345">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ادعای شبکهٔ اسرائیلی: کمک‌خلبان فلای‌دبی قصد داشت آن را به فرودگاه بن‌گوریون بکوبد
🔹
کانال ۱۲ تلویزیون اسرائیل مدعی شد کمک‌خلبان قصد داشته ابتدا هواپیما را به‌صورت عادی به سمت اسرائیل هدایت کند و برای فرود به فرودگاه بن‌گوریون نزدیک شود.
🔹
او برنامه داشته در آخرین لحظه، زمانی که امکان رهگیری هواپیما وجود نداشته باشد، مسیر آن را تغییر داده و هواپیما را به ساختمان ترمینال فرودگاه بکوبد.
🔹
این شبکهٔ صهیونیستی جزئیات بیشتری دربارهٔ هویت، انگیزه و نحوهٔ اقدام کمک‌خلبان ارائه نکرده و این ادعاها را از منابع ناشناس نقل کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466345" target="_blank">📅 01:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466344">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اعتراض ایران به نروژ درباره فعالیت‌های غیرمجاز استارلینک
🔹
مدیرکل صلح و امنیت بین‌المللی وزارت خارجه، سفیر نروژ در تهران را احضار و به استمرار بی‌عملی این کشور در قبال فعالیت‌های غیرمجاز استارلینک در ایران اعتراض کرد.
🔹
او در این دیدار با اشاره سوءاستفاده آمریکا و رژیم صهیونیستی از اینترنت ماهواره‌ای استارلینک برای اقدامات مداخله‌جویانه علیه ایران، تأکید کرد نروژ به‌عنوان کشور ثبت‌کننده شبکهٔ استارلینک در اتحادیهٔ بین‌المللی مخابرات، موظف به جلوگیری از ارسال‌های غیرمجاز این سامانه در قلمرو ایران است.
🔹
او با انتقاد از بی‌نتیجه‌ماندن پیگیری‌های مکرر ایران، خواستار اقدام فوری و مؤثر دولت نروژ برای توقف فعالیت‌های ناقض حاکمیت و امنیت ملی ایران شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/466344" target="_blank">📅 01:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466343">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7e3aed45.mp4?token=pQsz22mrASM9463csyL5y6cyMo0rOqKemWIBsEJqywd_5eKuR8uvHecznG7qw--JtNqlKRXl-zRuW-BeBZwxtbvaTfqSZuUinslK09Y3ueNP1fHj6qlsaYqKtl0BYaMK9XCsUHFsi4DWc-NOoX6SKd1qnA35HrfqJHDejHWK6wUlhSeKYs-0zZywWxJ8nLwOQTd-4NxPTN0MKB3Xm9JJWmjPgQ6FaW1blkT-ExVtzV7D1Vfi3C4Jy9_0vrhlEfkogj1n7hh7YSQmP7iVsfbIxUSVqTJiEKxPytXHnEN-8P2onVz3wRs6MMvG4APUnFw7i3typpDdzKiXoiw3f6WduIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7e3aed45.mp4?token=pQsz22mrASM9463csyL5y6cyMo0rOqKemWIBsEJqywd_5eKuR8uvHecznG7qw--JtNqlKRXl-zRuW-BeBZwxtbvaTfqSZuUinslK09Y3ueNP1fHj6qlsaYqKtl0BYaMK9XCsUHFsi4DWc-NOoX6SKd1qnA35HrfqJHDejHWK6wUlhSeKYs-0zZywWxJ8nLwOQTd-4NxPTN0MKB3Xm9JJWmjPgQ6FaW1blkT-ExVtzV7D1Vfi3C4Jy9_0vrhlEfkogj1n7hh7YSQmP7iVsfbIxUSVqTJiEKxPytXHnEN-8P2onVz3wRs6MMvG4APUnFw7i3typpDdzKiXoiw3f6WduIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدارس فرانسه به دلایل امنیتی تعطیل شد
به دنبال اعتراضات دانش‌آموزان دبیرستانی در فرانسه شمار زیادی از مدارس این کشور که در کانون بحران قرار دارند تعطیل شدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466343" target="_blank">📅 01:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466342">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سفرهای گالیور</div>
  <div class="tg-doc-extra">قسمت آخر</div>
</div>
<a href="https://t.me/farsna/466342" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">قسمت ۶ – سفرهای گالیور</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/466342" target="_blank">📅 00:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466341">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3skRVBLMvYc6HCI7_0441W_mABGbHQ0jPB6Lu_eCYXhsgRlVSGnSjMGYySPSFgtCL7P0CZMHFL83vlpGY1sDP1jU6ZWHgcPOWyob049s4pVUX_XWUtVqAGVLDHNWVRKU6TNnJAJ3oA8dAAKvqk5n-9piiBF2LaBKglFJzbSHeJpJtQZNlzIZpuq3KF98skwJBsVK801SxGgcRTPBWHDl9vAPCXhU3xIH68YjvN6zp9OMGDVBkRTTHDHOSycAivUVVXYBgCgyA6Z_UzkH8_slyaRy7ct5_TYRaF4g0dD1KNx3Puh0QIv2K599PZ0dDak3oJlnXW6yIAgd03_MEL84Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاقبت رفاقت با فریبکاران
🔹
کلاغ، گرگ و شغالی در بیشه‌ای همراه شیری زندگی می‌کردند و روزگارشان از پس‌ماندهٔ شکار او می‌گذشت.
🔹
روزی شتری که از کاروانی جا مانده بود، برای علف‌چرانی به آن بیشه آمد. شتر چون با شیر روبه‌رو شد، کرنش کرد و شیر نیز به او امان داد و گفت می‌تواند در پناهش آسوده زندگی کند.
🔹
چندی بعد، شیر در نبرد با فیلی به سختی زخمی شد، در غار افتاد و توان شکار را از دست داد. حیواناتِ دوره‌اش نیز از گرسنگی درمانده شدند. کلاغ که درپی چاره بود، به یارانش پیشنهاد داد کاری کنند تا شیر شتر را بخورد.
🔹
شغال گفت: «شیر به او امان داده و پیمان‌شکنی زشت است.» کلاغ پاسخ داد: «چاره‌اش با من؛ حیله‌ای می‌سازم که شتر خودش به استقبال قربانی‌شدن برود.»
🔹
کلاغ نزد شیر رفت و با چرب‌زبانی او را راضی کرد و قول داد کار را چنان پیش ببرد که نیازی به شکستن پیمان نباشد.
🔹
سپس سراغ گرگ، شغال و شتر رفت و گفت: «جان سلطان در خطر است؛ بیایید وفاداری نشان دهیم و خود را پیشکش کنیم. شیر از گوشت ما نمی‌خورد، ولی رسم خدمت ادا می‌شود.»
🔹
همگی نزد شیر رفتند. نخست کلاغ پیش‌‌قدم شد و خود را پیشکش کرد، اما گرگ و شغال فریاد زدند: «تو جثه‌ای نداری و گوشتت بدمزه است!» سپس شغال داوطلب شد و دیگران گوشت او را بدبو خواندند. نوبت به گرگ رسید و آن‌ها گوشتش را زیان‌آور دانستند.
🔹
شترِ ساده‌دل که این صحنه‌سازی را دید، با خود پنداشت اگر او هم پیشنهاد دهد، همراهان به رسم پیشین عذری می‌آورند و امان شیر پایدار می‌ماند. پس پیش آمد و گفت: «تنم فدای سلطان؛ گوشتم پاکیزه است و همگان را سیر می‌کند.» سخنش تمام نشده بود که هر سه حیوان یک‌صدا گفتند: «راست می‌گوید!» و بی‌درنگ بر سرش ریختند و او را طعمۀ خود کردند.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466341" target="_blank">📅 00:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466340">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFLuBI8fqZCW1pRwwmjAOlkaRdD7IVNByWsSwj9kQ2zEQzUHGEytvKjaOX7XRCpXhW9cWIWYKk7OrlurGdJ2F7M6YAaSvdJbVv_S6osqQogbBpVIYg0AyYwWAp6FslKUveYdHklswZ-OVPF0XBrQJj1C8L94I_5HBmnJ9XEeEFF8R0Ka07tPkscqwl-kkVTm6WgpiuoCrMvygsCnN7hkmDzY1vvvPzaMqAktROEwvxrQnsf-7ldvlBvQzxrTSLxAd_EKZ0ApgewSu4gaSAGHaaE-PEUZG-uqNejNsEw1m60mSOmBjz-e1YDy-n11QUcyKBC_mvBNFF59oZF2AcvYsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466340" target="_blank">📅 00:02 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6ZQf2eMUgoJW1PT7Pe6tsNT9OtjH0KWVrzdGUN0ojk3mmgMXoN_-ga35uHRA9TlRh2bVFRKg5HACttlaVwzsvTsDy25__8HoQio8cKTfQiIdYchQztrVcCmzrAyuxPPfZ5xvU6Ska99ELgn7ghiZy-wiUQBoV_skUX0PWIRk0H0HVU-ycDmkTFoCIEFHKAcANjSqYBDGdC3G-zJ8fcWgldc74cNmW_BDNjRdlv7baXOQV9Cg_Meftv_EWYtemfjqnRZ2zVJ5TUZYt-621gOTHr_Mr5B-nlO_1xywz4cUUcuqvv0UTXuJp404z05PwiofcGIsHp-HZ8I6pPQzJhvOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I-OLlsX4iROs0jQ0dcfDm9nabkS4gtksNHwJveoJAlxo4fTmeMfac4BC2fsiC0G9JwfwFDI6uWZV3-MU8GEc5_CDo6pXVK0xflNb3dMk3IehPwUOk9RJw8hqK1YL2xeIJs_iZd2l4u-R65iW4EgcWpVxekmIlJQYJSIjzfUWRYuKR-8Ubv4QnazfQswXjf416Wbxf4VKVmRgz6rbY45H2SdHDIxBeVc66hn3nvcDp18OIBmREnxr3kB3MwBn_xUazS6huKR7msBpcM-yJfvhnxCS99-mWGmHweT6raDUAlTWFkZG_qaWTP-6f-Osi3_5FW4APy19-eOkUxDt0RhoSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AoglK_Lki2w2CeDoc5JRkVJ_Crf8k30S9i_jomLrWXIy1pmMBg48Tk1z-vfrNQiVWouB4WO8KkDVS4464vDitqY7N9Xp0IR8PMQl029x4B6q0QFsA1MDItH_FUPhDDfRWO_j9SXQbC5a19jW6Wkyf3GZcV_OL8bEDSawjtgssuXbIdwvupkS4B16nrgqKj91_V6ZVMndXpiLhIEbaRxf27Z2vGFbKdKCSkz3XUEfSZKuzHMNS97cCS8AUngbOrSpPBmE424mj0ydrnOt-YuMABqaOoFl9sOpL887a2zwqMksXP-XVGno4gCuB1dCaap4PwnATKW15C1t05L81NEriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHDN9q-G8b4-hnSncsR4NF7cojEB_D7uaX8O0JPOQYqSs7dKgTznwBM8WuXn1JjjwMP_Q2y97L6Cv42qmoLDKarX7-l8pSmozlUK_VdNG0QEllf2gluQo11Nmq6p7DgdrryhGgz1S9jF-88aKW2KPzVYYbRvH1lXLU6Xx-ybJG0PfnyCuDkk1M-tkim4Sgs2DM5VNt24ywB4NZDkbHQF7ARVqf-38cd87CVwdv12BomtqH3XboATWljhIMtQuPrsGtj30HkY2BCCEwM06k-etLFVh-omSZYp6imcVQvWuTxzcV05zv1uSgnSL7_kBzwnqN-4OXico77_RjsYEjdDGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jOP7516v2iHh2A__JrRToI8NnLC8ckvhELZ-NK0MEAJRbgZ4kX-ajKPOnxHXVD4SMtkIWbCMGN25jeysl41MH666zZeMuLRP6349As88HFWTErIOZcIU7b0GyBSaW2JAIdqDCL_p0nyKLMrfony79YzViUYlKkQA1t2KOTn0su8zIl_SUOu3qmC_RpNeU12YD-QBf6ahOLr_bmDiqZLAh77h9v9aZHm14KLF3P-BFzQRpOFlE59sAoOH7y1Z3UGUOStt5jS37Hc-Gkeljne50ngHNficxU0z77LvonRgZBQ-P7ZNDP7HVZucqFrQ5uc_sQLz85zTjrjo8h7ghet9JA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
یادوارهٔ شهدای عملیات رمضان در اهواز
عکس :
محمد آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466335" target="_blank">📅 23:59 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466334">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79723a5117.mp4?token=vGmmLrwEJmOOkPbJMt_RUmlLpRRkckkL-NiOsMhSzR6M_Ndh3czsPrb9EBMMPFVv0xd4omdnYODPcwuJkh6LBf1bANccY7xG3f8njFHJzFJCg8FLSTTFL0ckV3uvHi0zjGcOZSNUp64vugmUtpB8Fk6MOFFx_j80w-v7rwzs1ZB-l1ZBePY2fY-8HQyn0ReCYhzmT1p1UsicAJYwK8BU_VTnAtNfSDk9I2MJ6diwt1pnDC1JfhxxGcw724xSUx4WY3DFfZRk2ZoJ5-qDhkCF7xVqe-n3AlRA5LmOlhENBXLAEp3TMxsU-n9hiq8mjun0QZoFzOeLv9l639d_g63SGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79723a5117.mp4?token=vGmmLrwEJmOOkPbJMt_RUmlLpRRkckkL-NiOsMhSzR6M_Ndh3czsPrb9EBMMPFVv0xd4omdnYODPcwuJkh6LBf1bANccY7xG3f8njFHJzFJCg8FLSTTFL0ckV3uvHi0zjGcOZSNUp64vugmUtpB8Fk6MOFFx_j80w-v7rwzs1ZB-l1ZBePY2fY-8HQyn0ReCYhzmT1p1UsicAJYwK8BU_VTnAtNfSDk9I2MJ6diwt1pnDC1JfhxxGcw724xSUx4WY3DFfZRk2ZoJ5-qDhkCF7xVqe-n3AlRA5LmOlhENBXLAEp3TMxsU-n9hiq8mjun0QZoFzOeLv9l639d_g63SGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
استقبال مردم شهر آسترخان روسیه از اجرای گروه موسیقی سنتی ایرانی
🔹
هفتهٔ فرهنگی ایران در روسیه بعد از سن‌پترزبورگ، مسکو و کازان به جنوب روسیه رفته است.
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/466334" target="_blank">📅 23:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466332">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🎥
آقاسیدعلی مارو ببخش...
🔹
صحبت‌های تکان‌دهندهٔ یک جوان در رواق دارالذکر در کنار مزار رهبر شهید انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/466332" target="_blank">📅 23:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466331">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5bf0750c6.mp4?token=hwIulhWYaxxej5TEcNLtd-BsOql4O7HpdrsvV13bMVynQCxgxY2hiCT-oVrjWmA7BagJLCudeif4SkKLLLNwAo1Xpw7MHer6Y8e4yo6c4cledkI5jLQXIGqLTJoIQk4XCbbz73Octy_KhdWoy4XnIeZWwiO59gp_Eq3UPGuOdX1UKpvJveFUISVJElnbbTPcGfbrAqvD89H02oUSGc3YSObrPUGGvfkjYjGpf4K4ydLCsmn4LTofLHrpy-6FhpsK7k7O7_6X72sVvZE5Xx5Vf2s5aO32UiGmScKybh-U62RiV9mOibAtDUeKHdwsVAx3PIwp_TBWGuXI7CEEpQLSxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5bf0750c6.mp4?token=hwIulhWYaxxej5TEcNLtd-BsOql4O7HpdrsvV13bMVynQCxgxY2hiCT-oVrjWmA7BagJLCudeif4SkKLLLNwAo1Xpw7MHer6Y8e4yo6c4cledkI5jLQXIGqLTJoIQk4XCbbz73Octy_KhdWoy4XnIeZWwiO59gp_Eq3UPGuOdX1UKpvJveFUISVJElnbbTPcGfbrAqvD89H02oUSGc3YSObrPUGGvfkjYjGpf4K4ydLCsmn4LTofLHrpy-6FhpsK7k7O7_6X72sVvZE5Xx5Vf2s5aO32UiGmScKybh-U62RiV9mOibAtDUeKHdwsVAx3PIwp_TBWGuXI7CEEpQLSxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها یک صدا برای ایران خواندند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466331" target="_blank">📅 23:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466330">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9f90a9a7.mp4?token=IOfVpVnZPPZ8NMOAi_J0Od0khCJ66EDTMoVzr5-lhCF7ZzpV7hhDbmxeVCURaz91gnAnyQ90CHauRq0mxKNltYrPrmrWmW0WRrLRKJjeq5t_qHWfvloElqpQ5pb5lFQmDsdwzvPxfTjkT7v9OR9cJilk10ys6p84iTT69CznCf13XG4OYnh5UuUIwY9FwrjEh50J6kek0FfEnyDB-hSpnDvVHxlewtLkwdTB3tI-ieBXsS9OpMUHldCZ5HtGXWlPgBE8AlPtgds3ZHkRN64WWNo8kdrPikPg2rraHW-t-uDRw_DdJ5rnAUjJS0P1E3hO-WD2yvFFXZl-XrAxOFQI8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9f90a9a7.mp4?token=IOfVpVnZPPZ8NMOAi_J0Od0khCJ66EDTMoVzr5-lhCF7ZzpV7hhDbmxeVCURaz91gnAnyQ90CHauRq0mxKNltYrPrmrWmW0WRrLRKJjeq5t_qHWfvloElqpQ5pb5lFQmDsdwzvPxfTjkT7v9OR9cJilk10ys6p84iTT69CznCf13XG4OYnh5UuUIwY9FwrjEh50J6kek0FfEnyDB-hSpnDvVHxlewtLkwdTB3tI-ieBXsS9OpMUHldCZ5HtGXWlPgBE8AlPtgds3ZHkRN64WWNo8kdrPikPg2rraHW-t-uDRw_DdJ5rnAUjJS0P1E3hO-WD2yvFFXZl-XrAxOFQI8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: آمریکایی‌ها می‌فهمند که هیچ منفعتی نمی‌برند و باید هزینه‌های زیادی بپردازند
🔹
آمریکایی‌ها در منطقه که آمدند، تمام خباثت‌هایی که داشتند و تمام اهدافشان، ما بودیم و در تمام مقدماتشان شکست خوردند. مگر در افغانستان و عراق و قصهٔ داعش پیروز شدند؟ در همه‌جا شکست خوردند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/466330" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/044e50cd6f.mp4?token=a1WlmgJJIMUvgfNDWRIR-oa9sOtdjcYWDa-qh2hXPWVyzLsq2hHKoySiCgjEUtiBQUXvstTop8fJigKhnF85LTKC1OWwiQYmNPfYcvDHJGaCZGO6Si2oHpPGWOUkwZvqBji6mjvoJVOT-kdSmc9VcvKDzKt3gHdRs_BGU6zntpqz_DggOEHGXGeVmJD-n2GTseg3LqaoJXfL3vPkVfKDAlMWvHf5Z9wLDoP7HrE_gMSnmv6755iCT0qeswgxl38DABBNmGpcopwx4-5ePnu7yPDzuT96DfEEi9lcilYg32Uk_A_IOiK_UmNeygFekulPZHYBBQUx7yIReqin2ZWAUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/044e50cd6f.mp4?token=a1WlmgJJIMUvgfNDWRIR-oa9sOtdjcYWDa-qh2hXPWVyzLsq2hHKoySiCgjEUtiBQUXvstTop8fJigKhnF85LTKC1OWwiQYmNPfYcvDHJGaCZGO6Si2oHpPGWOUkwZvqBji6mjvoJVOT-kdSmc9VcvKDzKt3gHdRs_BGU6zntpqz_DggOEHGXGeVmJD-n2GTseg3LqaoJXfL3vPkVfKDAlMWvHf5Z9wLDoP7HrE_gMSnmv6755iCT0qeswgxl38DABBNmGpcopwx4-5ePnu7yPDzuT96DfEEi9lcilYg32Uk_A_IOiK_UmNeygFekulPZHYBBQUx7yIReqin2ZWAUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: کشورهای منطقه اگر بخواهند می‌توانند در برابر آمریکا ایستادگی کنند.  @Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466329" target="_blank">📅 23:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466328">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a74e8ba96.mp4?token=v_gUBNwB1YffKMm1o8fQDCZz9_xU8NQDCTvyxRMQDGlHs6VVe0XSHPtxnXGmoU-lDvOhox40RkIqwoT7z6kc-dKDtJgYjDRLWfuLvviN8FXOiH6JsXlCJy13nZQhJj0PsL9Q9CQu_pSWNCZBf80uHQrO_H88146xKe9ZreOA6i73pZYLP8kQAPHQmH33f0W13dbM-z4U7uyDKtXKu9JEtgZ0GcCDN6EEwq6XKlBSWLL8h7u7wGOXNnuLJStsZ4QMBnqy3-0QKkHfUB8--a5O4p9QSrI92_UJeNqv8wE4q7axuz_V2Wl0KtHAfLuynx9MmHyvYhcqscnLDYY4-g7kdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a74e8ba96.mp4?token=v_gUBNwB1YffKMm1o8fQDCZz9_xU8NQDCTvyxRMQDGlHs6VVe0XSHPtxnXGmoU-lDvOhox40RkIqwoT7z6kc-dKDtJgYjDRLWfuLvviN8FXOiH6JsXlCJy13nZQhJj0PsL9Q9CQu_pSWNCZBf80uHQrO_H88146xKe9ZreOA6i73pZYLP8kQAPHQmH33f0W13dbM-z4U7uyDKtXKu9JEtgZ0GcCDN6EEwq6XKlBSWLL8h7u7wGOXNnuLJStsZ4QMBnqy3-0QKkHfUB8--a5O4p9QSrI92_UJeNqv8wE4q7axuz_V2Wl0KtHAfLuynx9MmHyvYhcqscnLDYY4-g7kdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: قیمت گازوئیل در اروپا ۲ یورو شده که یعنی ۷۰۰ هزار تومان
🔹
ما اینجا ۱۰ هزار تومان پول بنزین می‌دهیم که حتی یک دلار هم نمی‌شود و اصلا متوجه نمی‌شویم گازوئیل لیتری ۲ یورویی یعنی چه.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/466328" target="_blank">📅 23:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466327">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f77840eb.mp4?token=nclkqHw5XlVjTKZ50wR8HPlWe7XEny6TnXG4DU1tVwK8Abap-jcXWZLtkv-x_Xe2H3ZHP_EJUQY3cK1wQkA_9step4TkRi6u0Q80g3dXvaLyJcbWm1m3m8_YHKrFj55g9OMEIz2tkcLH1m0bRtn5Yaq67mxCifizPbj83HQ6vsXGZkznBYR3uruW_PBH-po3wqKcv73Yu4lJp9ybOA67fqhvBVWSq4fQTRuc8HrTb6GmYWFuRAlLwB6iBX1n0__944SCw1svtAPhYqE7MFfBTeLd_FFgcWQdor5IGOTFJ1ib3TDgpaw8WrBcdnq70v1R55XfutyyEy6MRfdWbKuSaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f77840eb.mp4?token=nclkqHw5XlVjTKZ50wR8HPlWe7XEny6TnXG4DU1tVwK8Abap-jcXWZLtkv-x_Xe2H3ZHP_EJUQY3cK1wQkA_9step4TkRi6u0Q80g3dXvaLyJcbWm1m3m8_YHKrFj55g9OMEIz2tkcLH1m0bRtn5Yaq67mxCifizPbj83HQ6vsXGZkznBYR3uruW_PBH-po3wqKcv73Yu4lJp9ybOA67fqhvBVWSq4fQTRuc8HrTb6GmYWFuRAlLwB6iBX1n0__944SCw1svtAPhYqE7MFfBTeLd_FFgcWQdor5IGOTFJ1ib3TDgpaw8WrBcdnq70v1R55XfutyyEy6MRfdWbKuSaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: ملوانان کشتی‌ها به ما می‌گویند نمی‌خواهند از مسیر جنوبی تنگه حرکت کنند اما آمریکا آن‌ها را مجبور کرده  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/466327" target="_blank">📅 23:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466326">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3315a230c.mp4?token=VujIw_cNqyC6iPlY9h7yB__nUdxJPSA_WkTIRWiZRuS3nBHgjUO0FodcBINxmE9H3r_oa_qWk6sX-86jmdMDyouxU3Vh2FZgTjMinsEvJmrA1N5LaEBaaLa4hZj1i04mZwPq7I0HT5uLo2YkudYgkUDc83mH6--tBtA3M8HTNbb7bGs4LIHWaDy6ED6J0LhXPBw1kUXveUc_NrijQRXNzrbJx9ISYvIqR3r65O8LTL9Poxss-ExLfZ4MK5haonvThWDW2M12n0AHtGQwaTrHUwyUrPHFyWJvfiuHGQ_Otlc5UhfOihF3VlgMqcMHrMfjNsIaUQjflq6tGMP3ez2k2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3315a230c.mp4?token=VujIw_cNqyC6iPlY9h7yB__nUdxJPSA_WkTIRWiZRuS3nBHgjUO0FodcBINxmE9H3r_oa_qWk6sX-86jmdMDyouxU3Vh2FZgTjMinsEvJmrA1N5LaEBaaLa4hZj1i04mZwPq7I0HT5uLo2YkudYgkUDc83mH6--tBtA3M8HTNbb7bGs4LIHWaDy6ED6J0LhXPBw1kUXveUc_NrijQRXNzrbJx9ISYvIqR3r65O8LTL9Poxss-ExLfZ4MK5haonvThWDW2M12n0AHtGQwaTrHUwyUrPHFyWJvfiuHGQ_Otlc5UhfOihF3VlgMqcMHrMfjNsIaUQjflq6tGMP3ez2k2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: هیچ شناور آمریکایی و هم‌پیمانانش در خلیج‌فارس نیست
🔹
آمریکایی‌ها از سال ۱۸۵۳ در خلیج فارس حضور داشتند، اما اکنون برای نخستین‌بار هیچ شناور آمریکایی نه‌تنها در خلیج فارس، بلکه حتی در شمال اقیانوس هند نیز حضور ندارد.
🔹
آمریکایی‌ها فرار کرده‌اند…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466326" target="_blank">📅 23:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466325">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">حمله به یک نفتکش در سواحل یمن
🔹
سازمان عملیات تجارت دریایی انگلیس خبر داد، گزارشی از یک حادثه در ۶۰ مایلی دریایی جنوب المخا در یمن دریافت کرده است.
🔹
به گفتهٔ این سازمان، یک نفت‌کش از وقوع چند انفجار در نزدیکی خود در جنوب المخا در یمن خبر داد، ولی خدمه در سلامت هستند.
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/466325" target="_blank">📅 22:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466324">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c36029544.mp4?token=Ce5c2yRtSvpJuSDA0pyPIXXKJ_y5MXyuWMFjThqLoPdFFtwRXB_6kltb3fEAKyh2nruT9wQax7eptwMei0CJnrMXLDUrqzw_3O--xlfXQc0NrmialFjVFopyiVxmWp4Zl1Otz9HbPDGLRfX70LyFKTrQnaMRB39eRrjxPs84VO7fCL2LM6XvlYbJuHPRnCeXGkzML2UxCLbNqwBIadzqvoiehdBIycog_wTYPh_5cgSRUzhiCPnIlKhDUO8__hOZZHfnt4zpAMg4JdbeXap9RK13drAOgZpyXOZaVPmmDPnuNlWumS85vYtZzehSu5WPpExD1fpkjg4YWeiE8fxNeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c36029544.mp4?token=Ce5c2yRtSvpJuSDA0pyPIXXKJ_y5MXyuWMFjThqLoPdFFtwRXB_6kltb3fEAKyh2nruT9wQax7eptwMei0CJnrMXLDUrqzw_3O--xlfXQc0NrmialFjVFopyiVxmWp4Zl1Otz9HbPDGLRfX70LyFKTrQnaMRB39eRrjxPs84VO7fCL2LM6XvlYbJuHPRnCeXGkzML2UxCLbNqwBIadzqvoiehdBIycog_wTYPh_5cgSRUzhiCPnIlKhDUO8__hOZZHfnt4zpAMg4JdbeXap9RK13drAOgZpyXOZaVPmmDPnuNlWumS85vYtZzehSu5WPpExD1fpkjg4YWeiE8fxNeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار فدوی: هیچ شناور آمریکایی و هم‌پیمانانش در خلیج‌فارس نیست
🔹
آمریکایی‌ها از سال ۱۸۵۳ در خلیج فارس حضور داشتند، اما اکنون برای نخستین‌بار هیچ شناور آمریکایی نه‌تنها در خلیج فارس، بلکه حتی در شمال اقیانوس هند نیز حضور ندارد.
🔹
آمریکایی‌ها فرار کرده‌اند و بیش از هزار کیلومتر از مرزهای ما دور شده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/466324" target="_blank">📅 22:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466323">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fefadf12c.mp4?token=bCOSOj4aQnFRAcOt05z1EEblgNhNoGQyKkK1hvEAEXZu20RghMb_3niOTNfuSCShWlp0fe3_AIEi4IwmwsfAa-ykUpa9clW_qu60U-pOfY8w2WnjsuOeoHLlocp-fRd2qz34CsKgU_qJLjFARh_JUStSchmvKQuB3zT3NpnyCmqakPKcs7ZGPm2Hl2qStiYPl8X5AVgml4N2YerUQ0nXp-LAV6O44K8fHZQOSuoSVV3G2NntQ0sEC9uSN6O7Z8LeOqVaKd7zklIehpmgLeJWhB-n_aCCol3d-CpQU9tiCBx5rUsYGt-Ey3WNCmgzciZRW34wWd34GsRdDSbWPX21KlJ45vNes4-Kphrnk7wocUT0IS2Y6WO4aGs1J8fPP3zfb_4ptSgOGqfysJ9YXKsn8RQfrO6TwP6_yPrcSR-QBahsRc_IDrfunGN_zvmhVQTyTcbQFZG0CE6nHphsYmy-o8EufaSsz0BQOlFZFdDsSG7tHi4y7G7XSsCC6L2RRV3E1tATTD5OlGdoESolYP2pOhG7nF0K51-_8LSeYOUNm0NoFQ9PuqiRvVZI_v-uFkd_y_6bzXWglZR-bYhe45qjBNzIrW_egAWaJiqXa8CVISZhBcJUIn_W_yLwGoPay0zLwqwelQsgsAMJ_PNz4gbBsLyaU0yxlb-f_o4ktR-alyo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fefadf12c.mp4?token=bCOSOj4aQnFRAcOt05z1EEblgNhNoGQyKkK1hvEAEXZu20RghMb_3niOTNfuSCShWlp0fe3_AIEi4IwmwsfAa-ykUpa9clW_qu60U-pOfY8w2WnjsuOeoHLlocp-fRd2qz34CsKgU_qJLjFARh_JUStSchmvKQuB3zT3NpnyCmqakPKcs7ZGPm2Hl2qStiYPl8X5AVgml4N2YerUQ0nXp-LAV6O44K8fHZQOSuoSVV3G2NntQ0sEC9uSN6O7Z8LeOqVaKd7zklIehpmgLeJWhB-n_aCCol3d-CpQU9tiCBx5rUsYGt-Ey3WNCmgzciZRW34wWd34GsRdDSbWPX21KlJ45vNes4-Kphrnk7wocUT0IS2Y6WO4aGs1J8fPP3zfb_4ptSgOGqfysJ9YXKsn8RQfrO6TwP6_yPrcSR-QBahsRc_IDrfunGN_zvmhVQTyTcbQFZG0CE6nHphsYmy-o8EufaSsz0BQOlFZFdDsSG7tHi4y7G7XSsCC6L2RRV3E1tATTD5OlGdoESolYP2pOhG7nF0K51-_8LSeYOUNm0NoFQ9PuqiRvVZI_v-uFkd_y_6bzXWglZR-bYhe45qjBNzIrW_egAWaJiqXa8CVISZhBcJUIn_W_yLwGoPay0zLwqwelQsgsAMJ_PNz4gbBsLyaU0yxlb-f_o4ktR-alyo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همه قبول دارند جنایت مدرسهٔ میناب کار آمریکاست، به‌جز پهلوی!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/466323" target="_blank">📅 22:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466322">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ec5950702.mp4?token=Hl4fuhnTUSX8W0_R4m473AYB5OgAc_QlG5A22vZQ8peMboTpdA6HqN_fBmsIH1bXIt66tDg2xCinn15XJl_lPzs6dkSR_6iQT3NfSwiuuZS5jKObob3DbJEMhcqloghF7GPi7HZX1wDdg9yP73f7Ioajq3-NdGPo2m6kdPae0CXMe-yq7z4Ww0tccykLJSyI3vxpfk7WyPN5yFW-Ofku2sjkt00YufyEcK7N5kzg9OrBr3TyJ-144UBwDceda83V0sFkyzV0-sjF4tBNN1fMYTkXly7S_g3KTaLbhYBXSqWZPNiXa-rVlDEprH25MZZS3B2ytQDCdqfVasClw5B0ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ec5950702.mp4?token=Hl4fuhnTUSX8W0_R4m473AYB5OgAc_QlG5A22vZQ8peMboTpdA6HqN_fBmsIH1bXIt66tDg2xCinn15XJl_lPzs6dkSR_6iQT3NfSwiuuZS5jKObob3DbJEMhcqloghF7GPi7HZX1wDdg9yP73f7Ioajq3-NdGPo2m6kdPae0CXMe-yq7z4Ww0tccykLJSyI3vxpfk7WyPN5yFW-Ofku2sjkt00YufyEcK7N5kzg9OrBr3TyJ-144UBwDceda83V0sFkyzV0-sjF4tBNN1fMYTkXly7S_g3KTaLbhYBXSqWZPNiXa-rVlDEprH25MZZS3B2ytQDCdqfVasClw5B0ioWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۲۱۸شب از همبستگی و ایستادگی مردم کاشمر تا مقاومت و خون‌خواهی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/466322" target="_blank">📅 22:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466321">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c72b757f9.mp4?token=Zqydxp14NLDA-r6qDxTTW_MjWOd74sNkk5j7Y9Rw0KnSp_GauKRr8NfioP6x5MSW_Q8bABXcgWdR2M6Ty4Jyv4aKOe1B6Z9r36lHU9IzcQreUOjibuXsmrKbzYoHhayBP-_SSqIawUQDM1J8cuz97kD05neNC-YuNgxm9Wl4SJEhXmZUURY81P5AE6znQm3n3y4rZayrFHWtbsaGPxHxRhBPZE3ysr9sgvVBecEWhvmmumRjTEH-l_ngrNgz7QLDuGTFel0dRocqv3Pl4Vb0-HjoVDsfObtGwlNo3LvR8kqIDqNvcd5lheNKZiMPeGGbKtKKJ8cMLRCSsGsYJohMNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c72b757f9.mp4?token=Zqydxp14NLDA-r6qDxTTW_MjWOd74sNkk5j7Y9Rw0KnSp_GauKRr8NfioP6x5MSW_Q8bABXcgWdR2M6Ty4Jyv4aKOe1B6Z9r36lHU9IzcQreUOjibuXsmrKbzYoHhayBP-_SSqIawUQDM1J8cuz97kD05neNC-YuNgxm9Wl4SJEhXmZUURY81P5AE6znQm3n3y4rZayrFHWtbsaGPxHxRhBPZE3ysr9sgvVBecEWhvmmumRjTEH-l_ngrNgz7QLDuGTFel0dRocqv3Pl4Vb0-HjoVDsfObtGwlNo3LvR8kqIDqNvcd5lheNKZiMPeGGbKtKKJ8cMLRCSsGsYJohMNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سلیمی، عضو هیئت‌رئیسۀ مجلس: در طول جنگ مجلس تعطیل نبوده
🔹
از ابتدای سال، مجلس ۴۵۲ جلسۀ نظارتی داشته و تذکر، سوال و تحقیق از وزرا جریان داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466321" target="_blank">📅 22:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466320">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a5769ab9e.mp4?token=LvwNZ0gDsuq7oHWWoVEhAPmqm_0K-kKqdBZMgP23bn_j7bWF_eyL-9r8bK-cdMGJi-_ZUWLD86S7JVFLRnJZI-H60s0LnE5VFyqG_EFlzUA90mKQ-yBSYI3eMYzlcAVycaoWAyVEAgDAX4PHBdBBYfAGc6fTKpNv7VRK16V88gTS-8tu7GgH9Cb64g7orKf-LQJrSxlJGz9kSsgcOqXxobhlMnwso-UqkYbLRRLYedRDjTKWALn-rBLa8J0AvBgERO174jIqjACNZclKthTntIhWMIwOIeu3x-M9AA0Bd4-FeD_7StDW6XwxDKCYTlLeuPo8SEnoLXUCMq9yhYSLWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a5769ab9e.mp4?token=LvwNZ0gDsuq7oHWWoVEhAPmqm_0K-kKqdBZMgP23bn_j7bWF_eyL-9r8bK-cdMGJi-_ZUWLD86S7JVFLRnJZI-H60s0LnE5VFyqG_EFlzUA90mKQ-yBSYI3eMYzlcAVycaoWAyVEAgDAX4PHBdBBYfAGc6fTKpNv7VRK16V88gTS-8tu7GgH9Cb64g7orKf-LQJrSxlJGz9kSsgcOqXxobhlMnwso-UqkYbLRRLYedRDjTKWALn-rBLa8J0AvBgERO174jIqjACNZclKthTntIhWMIwOIeu3x-M9AA0Bd4-FeD_7StDW6XwxDKCYTlLeuPo8SEnoLXUCMq9yhYSLWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما چه چیزی باید بدهیم تا آمریکا راضی شود؟
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/466320" target="_blank">📅 22:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa71ac9306.mp4?token=c4U7kuT1Lv-2TLHgDMzrgj6CoNd5gMasekudgiB_ofbdSLdKcLxsHCp6KDfdSxK5J-iPL7aGfrQxrupTDUkwVKTsZafiqFGoIgwSUBnd8Cr8himRyjyrAvqL6M_sNKfPHMx3ZNJAl0IriJnQoxd-BwR39aXRNDhpjKvxYhQ5R_z-7-fUDu7i8buUQDX8rtIuHSnJouShIJJk12cp6D0lyPKcfw7ungFBqGkm_4565IAHSIs2NnibXsJdDqwMVM-CcCc2tMDY8nJ_SbIWJC8KX3y_8fAzhgqkfNg7tn15ptqu958DL1UVhcG2kaaASlVtDO1JOF9tNIGNs5bWen9aAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa71ac9306.mp4?token=c4U7kuT1Lv-2TLHgDMzrgj6CoNd5gMasekudgiB_ofbdSLdKcLxsHCp6KDfdSxK5J-iPL7aGfrQxrupTDUkwVKTsZafiqFGoIgwSUBnd8Cr8himRyjyrAvqL6M_sNKfPHMx3ZNJAl0IriJnQoxd-BwR39aXRNDhpjKvxYhQ5R_z-7-fUDu7i8buUQDX8rtIuHSnJouShIJJk12cp6D0lyPKcfw7ungFBqGkm_4565IAHSIs2NnibXsJdDqwMVM-CcCc2tMDY8nJ_SbIWJC8KX3y_8fAzhgqkfNg7tn15ptqu958DL1UVhcG2kaaASlVtDO1JOF9tNIGNs5bWen9aAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۲۱۸، هم‌چنان پای عهدشان هستند
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/466318" target="_blank">📅 22:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jph6VnKqGarAuDJH1YRCs6d77n2t4qeXoQkgr8G94-hGIZ9LiLONIthwzuTmq4LwQejpNh7BKWFjLgkX0KaA82JE035u0U8QmsfoMyAthcbk5oZEIq3QKEY3JDF7LRZOC-hDBM0f4_cSWwa_5YWgddrAV3wnoshnz9_ZgyfZjPXcYFEE0I9uytD6cFmkIyCw32_J2Sm-a9rgjpEHhMtd87srrNcanrOrWyzHuc7nFO2WWGQcTvQ8XZ-JaRukGk4iqPrmd5lWtj3aLWvZpBUuMJd0i-Ju4_D-z8qC9Iy3DT-4VPukIJuX7RdDo2SEFkoZjrDLrHvKtFWKy92cqcRUGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کمیسیون انرژی: قیمت نفت باید از ۱۱۰ دلار عبور کند
🔹
عبدالحسین همتی: ما تمام تلاشمان را می‌کنیم که قیمت جهانی نفت از آستانه ۱۱۰ دلار عبور کند، با توجه به شرایط منطقه، ظرفیت افزایش قیمت نفت همچنان وجود دارد.
🔹
بازار جهانی نفت به‌شدت از تحولات سیاسی و امنیتی منطقه تأثیر می‌پذیرد و هرگونه اختلال در مسیر انتقال انرژی می‌تواند قیمت نفت را افزایش دهد.
🔹
اگر ایران امکان صادرات نفت و فرآورده‌های نفتی خود را از منطقه نداشته باشد، هیچ کشور دیگری نیز اجازه صادرات از این مسیر را نخواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/466317" target="_blank">📅 22:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466315">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaqFixI6u20T9GQ-G7VkiuVJ89N6jfH475ZUXgifJM-KurXLSk_XyW2WTUYjp4PmUALQSFZrhS0phurZB8WThmfvOEWkkTGeeGSUKQW9WJXWTHHRf_8HrHbs-I_HYcBt39yAQB79oTbcMlolL_jDSW2KDpM816bfMHv2Oev4t78PPvHc3tRv0gZcu183Xcecn5TcxLhaTkiNpjXGqwXwxf0gbJdo8LqIQSxbTfEzlHfxYABQzjUaBNL88CIb8sVtBpXDrAaMIMGxsoj9Vw-G2qx3YrGdBQs5Yn1gZXyOcv5CBALJY5zO6mqskN0s5PFZk_oHWBryv5Rlch_Ze87dvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Uej63rHEfdxzV8zbxM71KCzukxAxhZ-_R89YMvvniM_KCgfiw96R9Cquyc4ovdDOVbE8A7Kx7oJ2o6Df09oWfUAltPcKyPC_FOQslsGvkBkpp28I2l5ouaFWqERm-7i9Sh7vksyO3boUIWbhrXK57lsxUCBHJOoq0UMp066hqhHOLGqJO8g5WN5bYJatdgFWF7p0do-l-b4j6pa6foNg6wEFo69eanaa9npEkn9bv0alkI0jSFXqLaYFk0h6n5JkYXvxSWvV3tia8SymCVmW8AUnFyPpyqphFTY1Q0ra02kIJffjiZAPhCglmfJAMax1ud5oD8YtXLA8-RYP59Tcaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پترولاین عربستان دوباره تیر غیب خورد
🔹
براساس تصاویر ماهواره‌ای سنتینل-۳، امروز ستونی از دود سیاه به طول حدود ۵۰ کیلومتر بر فراز این سایت دیده می‌شود. داده‌های سامانهٔ FIRMS ناسا نیز ۴ ناهنجاری حرارتی در این ایستگاه ثبت کرده است.
🔹
خط لوله شرق–غرب عربستان تنها مسیر صادرات نفت این کشور است که از تنگهٔ هرمز عبور نمی‌کند. این خط لوله در ۱۱ سپتامبر پس از اولین موج حملات بسته شد و در ۲۲ سپتامبر فقط به‌طور جزئی فعالیت خود را از سر گرفت.
🔹
تا این لحظه جزئیات رسمی بیشتری دربارهٔ عامل حمله یا میزان خسارات واردشده منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/466315" target="_blank">📅 21:56 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466314">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEVFoDRomn1bGIgw15LVonY6unBl6Xz1VjRNkYYCoinexFILqGEZXe5_rPEDH7_IXoFEGYgnJTJ8XuJSGiLNAXy21TjhyFXDv2RJ4-jJAPbddW6-OKXKEUZqASIP3vWEGv6A9RHqzlHU0hd5du8QAhjBVQgac8XKsMAUIi8RADQjr7nXymlGQGPqV1IwVJ_eZmuiW-WxfEMICIU-09dwPIRnyOoJHcKLGkVP4QiuGY-_J_JXnAtMSrixvHtaVpIhqkNQDzSR1GmbSHExOa5g1R6E5b7CFrNHe2-90KN_-59RdeZGM3p6-NuYXYjtQd45FigS1xim4ClDgpU7738qlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرسپولیس علیه استقلال تا دادگاه عالی ورزش CAS می‌رود
🔹
پس از هفتمین دربی پایتخت که با تساوی استقلال و پرسپولیس به پایان رسید، باشگاه پرسپولیس به دلیل آنچه حضور غیرقانونی یاسر آسانی در ترکیب استقلال می‌داند، از این بازیکن شکایت کرده است.
🔹
مسئولان باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/466314" target="_blank">📅 21:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466313">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یک نفتکش در تنگهٔ هرمز هدف قرار گرفت
🔹
به‌گزارش سازمات تجارت دریایی انگلیس، یک نفتکش در تنگهٔ هرمز هدف اصابت یک پرتابهٔ ناشناس قرار گرفته است.
🔹
ناخدای این کشتی می‌گوید که بر اثر این اصابت به موتورخانه این نفتکش آسیب وارد شده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/466313" target="_blank">📅 21:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466312">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f9314b8a6.mp4?token=eGfuUz-9ZFDxb4YeuTbxZ5ejGS2Ig2_MueL88jIjDwXrIuOMdN693L5hdozsiC8kgdeuFAn8Jwe1rBvcFDubaO2Lg7UacslnTlIjEO6BeDEUMlqHz3DXTYvg3XTZQaLXVrKi4qL0ueS4cv37smtG1lObcqTxGKtNrBD58KydqFYbBzZooT0NzRLO6PZ-I_l9T-1Th8fKYbBTONRZmLaugZFgmZIgG7J1dgmchvO9Coj3Yx-Fhryi8TpJ_fzc-vIG6AlQPTfry25uByuvHbI87phhDPY3VdNF7kFsw7B60xWZEfPtiiyCY5RDyjEcBetIzOJ-lgohvqnaQLqcF5jnrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f9314b8a6.mp4?token=eGfuUz-9ZFDxb4YeuTbxZ5ejGS2Ig2_MueL88jIjDwXrIuOMdN693L5hdozsiC8kgdeuFAn8Jwe1rBvcFDubaO2Lg7UacslnTlIjEO6BeDEUMlqHz3DXTYvg3XTZQaLXVrKi4qL0ueS4cv37smtG1lObcqTxGKtNrBD58KydqFYbBzZooT0NzRLO6PZ-I_l9T-1Th8fKYbBTONRZmLaugZFgmZIgG7J1dgmchvO9Coj3Yx-Fhryi8TpJ_fzc-vIG6AlQPTfry25uByuvHbI87phhDPY3VdNF7kFsw7B60xWZEfPtiiyCY5RDyjEcBetIzOJ-lgohvqnaQLqcF5jnrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/466312" target="_blank">📅 21:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466311">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f6b828b64.mp4?token=ESmokFBluyJm0DrqQ9W0ObeZbK71hFSaWS1UmswqlbqPULkZHla_AOeJKDQsX7h1i7t7MMdCeA1Sd6UgK67BgemofiqcHZ7zfaRGKAn0sSRsIOlmpcTbW9vXODvA2OVKP_UdUahUS9losmtIo5qckJHZ5avUySZAFkyvHW9UO3DZo3b2BcyJQTBpFFJA-mo7f4IevjjeEFw_ktz1rjZx5SKGaoECSlEE4dLOdpTF2mTDjnXnA92icr86x3Da46r7tAwSZ5Eywa6ZbDTER5nTZOGRYQ7dl5XR7ILaCbULpM5w5O9crC-zByLf14tDopt3RtrXK524d_SJGkYQ_cwXEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f6b828b64.mp4?token=ESmokFBluyJm0DrqQ9W0ObeZbK71hFSaWS1UmswqlbqPULkZHla_AOeJKDQsX7h1i7t7MMdCeA1Sd6UgK67BgemofiqcHZ7zfaRGKAn0sSRsIOlmpcTbW9vXODvA2OVKP_UdUahUS9losmtIo5qckJHZ5avUySZAFkyvHW9UO3DZo3b2BcyJQTBpFFJA-mo7f4IevjjeEFw_ktz1rjZx5SKGaoECSlEE4dLOdpTF2mTDjnXnA92icr86x3Da46r7tAwSZ5Eywa6ZbDTER5nTZOGRYQ7dl5XR7ILaCbULpM5w5O9crC-zByLf14tDopt3RtrXK524d_SJGkYQ_cwXEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ترامپ هربار با توهمی عجیب‌تر دربارهٔ ایران برمی‌گردد
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/466311" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eca6430549.mp4?token=c5LKOdpipJGczP_BnTYWTrejhZAry-KeRNlaQl4kqQr0tFWjeHEN-syuovJ2TIumoLuJkPmF_WtRgGqibm3SaIUSCcTEBiFOCzFMXJvHMLmXnyfd0V2rkxJzuWI1WjMX_6o9B3nDO5A3JC0lvWZwAzpae_7FebXVWCcevVSsOzU-suYwttVXp3jUdN4bHOWg3bdeg34_sfVmS4W6Kp3tgK4eX6kcozByM7za-hF8VC1KQQUBzMPuukOVKQPWr1MnUboD1p57zzj1YY7i9zJCK6lWVUbJ-s9xXkTTj7jyIIt-YwkHl7dVlRxTdnu62x4wMLz5cMafC1UtCnl4TyFseA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eca6430549.mp4?token=c5LKOdpipJGczP_BnTYWTrejhZAry-KeRNlaQl4kqQr0tFWjeHEN-syuovJ2TIumoLuJkPmF_WtRgGqibm3SaIUSCcTEBiFOCzFMXJvHMLmXnyfd0V2rkxJzuWI1WjMX_6o9B3nDO5A3JC0lvWZwAzpae_7FebXVWCcevVSsOzU-suYwttVXp3jUdN4bHOWg3bdeg34_sfVmS4W6Kp3tgK4eX6kcozByM7za-hF8VC1KQQUBzMPuukOVKQPWr1MnUboD1p57zzj1YY7i9zJCK6lWVUbJ-s9xXkTTj7jyIIt-YwkHl7dVlRxTdnu62x4wMLz5cMafC1UtCnl4TyFseA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تعزیرات اصفهان این‌گونه مچ طلافروشان متخلف را گرفت
@Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/466310" target="_blank">📅 21:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fe94c4a5.mp4?token=HLdkfN2lM_PXa1SJLm8gPOA_b2BCSfejM3449LUGuCnln-j5Spi0XrcCi7WPic7vg7M_PT93fUa1s_shVP89oeAtMCDnZW1O7vu9hh0hTpVJokfFV8AQEkP3mri9GC6BElQyWDT06YD938gXwai62OjYf9A0onJoPhentZi7-HcGkMNSTquKlC_mbHfJBvHT8Kka6CQ0FjsnbFfp-jaWTPAhPW2b104uAkoLqFdRDn06w69cQ1Bz9sdb8hXZW71oD6E_OruoBprpQdfHAW18pATkWf2ikNXeJDHtALfifuisBzoLpshXxFrUWOUWckNIZy_uEXy4Ua7iQ5N1a6jKyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fe94c4a5.mp4?token=HLdkfN2lM_PXa1SJLm8gPOA_b2BCSfejM3449LUGuCnln-j5Spi0XrcCi7WPic7vg7M_PT93fUa1s_shVP89oeAtMCDnZW1O7vu9hh0hTpVJokfFV8AQEkP3mri9GC6BElQyWDT06YD938gXwai62OjYf9A0onJoPhentZi7-HcGkMNSTquKlC_mbHfJBvHT8Kka6CQ0FjsnbFfp-jaWTPAhPW2b104uAkoLqFdRDn06w69cQ1Bz9sdb8hXZW71oD6E_OruoBprpQdfHAW18pATkWf2ikNXeJDHtALfifuisBzoLpshXxFrUWOUWckNIZy_uEXy4Ua7iQ5N1a6jKyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سردار رادان: مردم به‌زودی می‌توانند با اسکن کدهای نصب‌شده روی خودروهای پلیس، انتقادات و پیشنهادهای خود دربارهٔ عملکرد پلیس را ثبت و ارسال کنند.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/466309" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14bf1ad55b.mp4?token=m8-i56jLV3in1wLRz6jeV_KUbaFllnLmsp6AG53DbE9HjLn6PELnOQlV7ZP-4vcZwAS1ZVw-fUW3_FNxJn2ZxUet0-Kqlv9cY-8Q4AK1esJ-8asvb6ArLuAak-0Ml62xjOXo9mKNdp4M2RT8MJiU3MQKCkFbOZHzey80vMDX7K2gUQiAToIvccrJzxUflpv_7S5I-PKnD1wh2LEyNm8sRKLpAuDAlJJCdbSzBj2n-ZkOQCAC6kW88Uu8QKtXGdBZ4srGx6d6koFLOg-v3Izhj9oAABYkpSENL_NmyTcZDZUcDk2N19EaATcQWMYsviETes_3-xGCZIo3INZgr68nDQDq-g1hWjWFsDjhG7U3bCzbFK_JRWZ91fRBe8oqaqyT3RrBdUa4Rm8agAWnZOCrfVb1jaJCSAhtPSIcp85fKpRKTtXnC6CsswjCoseZeSffXjYH1ujB10AJRz-xZke6msukJxH8cTXBdxWqv8oE3eeomW1jOMwH0zGYHdpuET-7zV6S3b10Xt45jEryk0qog1HD7qZJUn8BnRWkAzNBQW27HjOFs9Hu5lFckXHMVJnNdOF7fng8NAztiQtJghZadOaoXjLwFvoKh9UA0GSSdnbLBn8JXReGvjZbrD11RRK9DEes1MU5JHNGBRv_0RWAxCXzzFLzzl6p3lUvS57ROL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14bf1ad55b.mp4?token=m8-i56jLV3in1wLRz6jeV_KUbaFllnLmsp6AG53DbE9HjLn6PELnOQlV7ZP-4vcZwAS1ZVw-fUW3_FNxJn2ZxUet0-Kqlv9cY-8Q4AK1esJ-8asvb6ArLuAak-0Ml62xjOXo9mKNdp4M2RT8MJiU3MQKCkFbOZHzey80vMDX7K2gUQiAToIvccrJzxUflpv_7S5I-PKnD1wh2LEyNm8sRKLpAuDAlJJCdbSzBj2n-ZkOQCAC6kW88Uu8QKtXGdBZ4srGx6d6koFLOg-v3Izhj9oAABYkpSENL_NmyTcZDZUcDk2N19EaATcQWMYsviETes_3-xGCZIo3INZgr68nDQDq-g1hWjWFsDjhG7U3bCzbFK_JRWZ91fRBe8oqaqyT3RrBdUa4Rm8agAWnZOCrfVb1jaJCSAhtPSIcp85fKpRKTtXnC6CsswjCoseZeSffXjYH1ujB10AJRz-xZke6msukJxH8cTXBdxWqv8oE3eeomW1jOMwH0zGYHdpuET-7zV6S3b10Xt45jEryk0qog1HD7qZJUn8BnRWkAzNBQW27HjOFs9Hu5lFckXHMVJnNdOF7fng8NAztiQtJghZadOaoXjLwFvoKh9UA0GSSdnbLBn8JXReGvjZbrD11RRK9DEes1MU5JHNGBRv_0RWAxCXzzFLzzl6p3lUvS57ROL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم دربارهٔ کسانی گفتند که در میدان ایستادند
@Farsna</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farsna/466308" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVUTH_yfkfuh7P0LNl7Gl5mZW6xMBEr8bNqb_rwju-u8mbxwTjvw42NH0EzrR3QNIfECGYAfGsIq43cl4VObenWksj1SsGDao0hX9anyIodUYXJXetsMoDHvGije8OO1j0haUFpbMs5lHXjgW_w2ZYJFTGB7_IklFT_iQ03XZ9oJb1e0cxd8Ev1I7q4gTloSfBitC-idsT__ar2l3pGb8wUC2KIalK_F9z_CELgVSReB70IkGwXFVaI63e1jfeDgjRN4hBxnbuv6EMNLcera5xcDMCUVeBaZtJ9MokdHsyXIhK_IvCB_tODKU6hcbTI3Dw7pp9OxNp9ylOWJoLxo4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
۱۸ فروشگاه شهروند به طرح «تورم صفر» اضافه شد
🔹
از هفتۀ گذشته طرح «تورم صفر» برای ثابت‌ماندن قیمت ۱۲ قلم کالای اساسی در ۱۰۸ میدان میوه و تره‌بار تهران کلید خورد.
🔸
امروز نیز ۱۸ فروشگاه شهروند به این طرح اضافه شده‌اند و قیمت این ۱۲ قلم کالا در این فروشگاه‌ها…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/466307" target="_blank">📅 20:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621b24ff29.mp4?token=WD7s1irNiaEJ-ZzS-aYX7sAL4owxJJfkGWu1abSLubpnLKTi5_5VvWKBknmq1OexmXCS7dIDaR1ZZBNH4zmyuTiDSSTe5mL0FlDQrWc_8keAtLq0cPnH8QEgHtYhMuOceBw8wmPH1i-EAqR3tVRu7BZrPdyOvmzpLKHDZnhEKekAbC5jL04fSyqqLiZLztgj04ngnPLwG9l4hFv87u2gCFd6RkYNJwTlxMSM5MQM0h9OXlz3gFkQ33w8JWyBNuF0t5AGL_1HR0phm8tCEtRDj4HliHVikbHts5LPDVy1y5x9jsWRtPjWrfEIZ2VYVqJ5R8yNpwAWmRdMgJ6UFvwHjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621b24ff29.mp4?token=WD7s1irNiaEJ-ZzS-aYX7sAL4owxJJfkGWu1abSLubpnLKTi5_5VvWKBknmq1OexmXCS7dIDaR1ZZBNH4zmyuTiDSSTe5mL0FlDQrWc_8keAtLq0cPnH8QEgHtYhMuOceBw8wmPH1i-EAqR3tVRu7BZrPdyOvmzpLKHDZnhEKekAbC5jL04fSyqqLiZLztgj04ngnPLwG9l4hFv87u2gCFd6RkYNJwTlxMSM5MQM0h9OXlz3gFkQ33w8JWyBNuF0t5AGL_1HR0phm8tCEtRDj4HliHVikbHts5LPDVy1y5x9jsWRtPjWrfEIZ2VYVqJ5R8yNpwAWmRdMgJ6UFvwHjTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درخشش ایران در المپیاد جهانی نجوم
🔹
تیم ملی المپیاد نجوم و اخترفیزیک ایران در نوزدهمین المپیاد جهانی این رشته در ویتنام، با کسب ۵ مدال طلا در میان بیش از ۶۶ کشور و ۳۲۰ دانش‌آموز درخشید.  اسامی مدال‌آوران ایران:
🔸
سارینا علم‌پور
🔸
محمدحسین حسینی
🔸
هیربد فودازی…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/466306" target="_blank">📅 20:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466305">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kh-Wxr_9x_pCtCVQazJ2ayShOp_xyfyb9QHms1c-gb16krJRwzn--kT9eYzrPrcNyMdSs4vLcaY_bXo_fSG1tcpDyGtO9DKgKNPd7gklKqXDH0-QmQM7HD_8PXd75nWTwobGZn5prGeNOVOf6Bv7o7oNfG1jHw8cRv3WScd5N4FwWkVU7ze9b9qAyKBcfMQdSJEnarU9GIJ163BsZyE7H2hpN6_LC2ZzVHchNvBkYHoQpSpai215y3kOXsQuocxHjg8uvhJy0CtCH6L0AzaQxjx6Ew1SGjMfGHrbihHQKVuN4UEsMONsiJRl5JF-VLb69NJEJS1qWVGlEhiW0ilZjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farsna/466305" target="_blank">📅 20:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/466304" target="_blank">📅 20:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f2372ddac.mp4?token=suGd1cDAKLaCmTrvKo20flPnfiBt8JBNROx0GwBf-OcTo8HvBHQvanlKGxb9W2rft_J9OOcicuZuz2XDpwDQPo3HQU6SEZA9LDaxdL0cDl_QHIRpAzbjBmfsFhJauXD5VVbaCY66OtBx5WujqtNtpGEUEvojW-L1nw6KxLNuZel9DimgK84fCLOF9Q3wp16xZj7wGxENjHc0C5OiClYOBoX-OFhSGxXYopGcAAS29huRZSQZ-h-MTTkiKDqGb-MZpxjV968SVBmZm9YKYG6LJDeYox-ukVlEZtouEYZE7-OavF38F3RUvDxDtSTwf4QPX7DG5FmXO-DhgnmCQAmR0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f2372ddac.mp4?token=suGd1cDAKLaCmTrvKo20flPnfiBt8JBNROx0GwBf-OcTo8HvBHQvanlKGxb9W2rft_J9OOcicuZuz2XDpwDQPo3HQU6SEZA9LDaxdL0cDl_QHIRpAzbjBmfsFhJauXD5VVbaCY66OtBx5WujqtNtpGEUEvojW-L1nw6KxLNuZel9DimgK84fCLOF9Q3wp16xZj7wGxENjHc0C5OiClYOBoX-OFhSGxXYopGcAAS29huRZSQZ-h-MTTkiKDqGb-MZpxjV968SVBmZm9YKYG6LJDeYox-ukVlEZtouEYZE7-OavF38F3RUvDxDtSTwf4QPX7DG5FmXO-DhgnmCQAmR0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی: طرح تثبیت قیمت ۱۲ کالا در سراسر کشور اجرا می‌شود
🔹
طرح «تثبیت ۶ ماهۀ قیمت ۱۲ قلم کالای اساسی در تهران»  مورد توجه دولت قرار گرفته و قرار است این طرح در سراسر کشور اجرا شود.
🔹
قرار شده کمیته‌ای ۶-۷ نفره تشکیل شود تا تجربیات و زیرساخت‌های ایجادشده را…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/466303" target="_blank">📅 20:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIxYe0AiOs7LF5YCNFNxbOZi9jCdMQs8X7d7PShkyJXhC0K4-KKGgvvf8QDkv6ClzjRjlfF3mBwgZa_Xj7o3tR6fvg63S1ze3i7GyMBXr1fZjX4hIDrX32S4hmu6w74N2DmJ67dD2nMbBcYQHFHGlMuT_Cy19rIyF9uKLqhcQohNCGTiXRifRCjI0OivA-XKPmZBh24eiqX5BJq653sFzomlnOojWK6PvA_ON_LeMBH9M3o0up5Qu3mhFhu-JB_pTaL43M8z6g6-DL-dUK_M3cAy1ClJxhO512WyZZ7H2Vo4BSF4ONe6WGmf9CS6qQ9TXo9khtjI9B4DIvE0hAAcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: طرح تثبیت قیمت ۱۲ کالا در سراسر کشور اجرا می‌شود
🔹
طرح «تثبیت ۶ ماهۀ قیمت ۱۲ قلم کالای اساسی در تهران»  مورد توجه دولت قرار گرفته و قرار است این طرح در سراسر کشور اجرا شود.
🔹
قرار شده کمیته‌ای ۶-۷ نفره تشکیل شود تا تجربیات و زیرساخت‌های ایجادشده را بررسی و به کل کشور منتقل کند تا با همکاری دولت و شهرداری‌ها، این مدل در سایر شهرها نیز قابل اجرا باشد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/466302" target="_blank">📅 20:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cwIcNLUW3aBL1DQbj56pOXN63_VW-e20MREbKp12OZvVkdzyfmFTsSDUj2kvZKpdPVHn9gZ1odMHrR2CcrhOA101vU7j0fc5h0FvzCFjErbJA7LaZjK8HuXUx5TlidvAHEv6RqrixFx-yku0T0KnK10d1Bv9SKPzXXWbmhXDlgCuNnK-sLWtSL6DLBckEsYHMeXYV2cBqqfZl985djtUJQE5TkefWKmudKhoi6wKlkc7fnq9lKCKC1GDYSjNrmEc4DPhwZW6tndTWlFzHAUoJH4AD2uQS4LGZ9W3OnHicc2qu3KdwmZPQIuVVORZvXpxPNyIea6WcoNSud1qIk9G7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
محل‌های استفاده از طرح «تورم صفر» شهرداری تهران را بشناسید  @Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/466301" target="_blank">📅 19:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466296">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">دفترچۀ زبان.pdf</div>
  <div class="tg-doc-extra">17.7 MB</div>
</div>
<a href="https://t.me/farsna/466296" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‌
‌
🖼
دفترچۀ انتخاب رشتۀ کنکور ۱۴۰۵ منتشر شد
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/466296" target="_blank">📅 19:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466295">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70fcd4c336.mp4?token=UWepxLzA_coLq5LGXCZhC-SnoKNdmqKo4LtHYp7RzD7A52Qt6Jf0x_luW0vE4S8Vq8p6V1zgQ5Pl4ewlRiL3rJ1krymy_rDsYe1ICr400JPPyCkWm4lZ_KfGK8bODLA0zV8A28vQ0SdXh6GnUDXaFhEoFUaKRUArB14j2FlQPesVjFl18bvgNAYE_dO9eRbfhmhsU3U_W5PGdFr7QttM0Jm1UlFWJiBGi1kk56iaoSsVJ1XktnJXtiQ-zOkAglGJ0Dr7Kp9lM5FbKz2JUce2BguRkKECVQqcycZpkXtxM9qpciO_643OsDwqJJQGhWcjnji83_szRMapBUgKJ5yJPIOYJdhjQ-ODgyLZkJw2_VqGb5vUkquacqcE89GWQir0oeM-XbZ76dXeHCbNnUUl0SD3mBwCtCwt5Ruh7aC5TgmGWTMORdt8-TPxUqbZA2kBxEWdR3AmkvIaq1mGL6SS4CtFh83pgvYbzXdOzJEcFrZUyFRU3lTbgwQDwWAjCouk9th_0-hc8YBDlgmHDlIdmb0hIA1zGozQVUAQKxTQy6eu0N9bJHrs9c7qmeRH_MjJHJZw3xYqOaEBco6BLTRBQAFLLVRywZM8D1MXQ00RZHYuc-zGPd8G4c7uy_MI9xsDVB7crn9iGiUh-DoldRX8MXTAhfJXOmhsIs2xM52tcYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70fcd4c336.mp4?token=UWepxLzA_coLq5LGXCZhC-SnoKNdmqKo4LtHYp7RzD7A52Qt6Jf0x_luW0vE4S8Vq8p6V1zgQ5Pl4ewlRiL3rJ1krymy_rDsYe1ICr400JPPyCkWm4lZ_KfGK8bODLA0zV8A28vQ0SdXh6GnUDXaFhEoFUaKRUArB14j2FlQPesVjFl18bvgNAYE_dO9eRbfhmhsU3U_W5PGdFr7QttM0Jm1UlFWJiBGi1kk56iaoSsVJ1XktnJXtiQ-zOkAglGJ0Dr7Kp9lM5FbKz2JUce2BguRkKECVQqcycZpkXtxM9qpciO_643OsDwqJJQGhWcjnji83_szRMapBUgKJ5yJPIOYJdhjQ-ODgyLZkJw2_VqGb5vUkquacqcE89GWQir0oeM-XbZ76dXeHCbNnUUl0SD3mBwCtCwt5Ruh7aC5TgmGWTMORdt8-TPxUqbZA2kBxEWdR3AmkvIaq1mGL6SS4CtFh83pgvYbzXdOzJEcFrZUyFRU3lTbgwQDwWAjCouk9th_0-hc8YBDlgmHDlIdmb0hIA1zGozQVUAQKxTQy6eu0N9bJHrs9c7qmeRH_MjJHJZw3xYqOaEBco6BLTRBQAFLLVRywZM8D1MXQ00RZHYuc-zGPd8G4c7uy_MI9xsDVB7crn9iGiUh-DoldRX8MXTAhfJXOmhsIs2xM52tcYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رهبر انقلاب شبیه‌ترین فرد به امام شهید است
صادق محصولی:
بنده توفیق داشتم چندین جلسه خدمت رهبر انقلاب قبل از دفاع مقدس سوم، باشم؛ جلسات دونفره و در موضوعاتی که مورد بحث بود، خدمتشان باشم و از نظراتشان استفاده کنم. به‌طور کلی، برداشت من این است که اگر بخواهیم در یک جمله بگوییم، شاید ایشان شبیه‌ترین فرد به امام شهید، باشند.
🔹
یک بار خدمت اخوی بزرگ‌تر ایشان، حضرت آیت‌الله مصطفی بودیم. بحث رهبر انقلاب پیش آمد. آقا مصطفی، علاوه بر توانایی‌های علمی ایشان، در مورد زهد و تقوای ایشان مطالبی گفت که برای من خیلی جالب بود. ایشان با عبارات والا و شایسته، در مورد ایشان تعریف ‌کردند که الحمدلله به لحاظ تهجد، زهد و تقوا، درجات عالی دارند.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/466295" target="_blank">📅 19:32 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466294">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbewat2DgO3hMiRwKPhKRuliDtMTyDw2LqL9XplAENIoPbQ9P7TeF2gs4rB6itibgMLyCG1OnYj_tud7KeBYJtjGcL1OIaRTS9AHLYWP_VZFnSoRGxh4XUEGgN0Q1Tf5Bi1LzSX365TkbhWeGpSX15T36EU-ioxLvPwYhkiEYBQm96jwI03sFLlWVqFkerApYbXe3b2fW1sccGkIXcXX-qYZnUt8A907NUZmfJ0XKXqSwlV1rUQCkeehMUYaqVMK024zGod3q5AHVy9aIYdP0GfOnQm8QBWzGSwQR2VaSA0SApnLFi6hegrk8CY9JhCfkPXHkOBROMUXh9p32H6eaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ فرار نیروهای سعودی از چند منطقه در تعز
🔹
خبرگزاری سبأ یمن: نیروهای وابسته به سعودی از منطقه التُربه و ۲ منطقۀ الشمایتین و سامع در استان تعز بیرون رانده شدند. @Farsna</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466294" target="_blank">📅 19:30 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466293">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGMGQNlGW2ePYEzTzDFL9vfpqRWoarL8LSNo5NrVB9LqD3ZixvaNQC8rcxb7whGrc5xipd1CPKqTvRrUhA7f41cnDdSHnBKqBV-F63Mw0RRUmRdi_tNkJ9UTii-44XJ4iMeMRFu6HccEClISyl19S-mTJ5gpdCKSnJRgZ7rE1l5_RPnXJsiGlMRiy4r7U2IT5BgWGivLpuKQZv28x1US803CjzDP01C-HCFH_TQPNENrrNjXLClxfHpsnkzPz4nD1x5lMuJjXmvJF_MWfipRV2tMueJn8h6vsWrGtp4v53DFtk6EQ0HH_Wg0q3xa-M0OHi2qQZGoVBsW-PJdDWxvIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
قیمت هر قلم کالا و نحوۀ ثبت‌نام در طرح «تورم صفر» چگونه است؟  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466293" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466292">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5w3apwYkZW2OodK77wWzhp8K_EaJTPrSNO6XjxVjAZVyfFq4cNOsIA49WfX8GD6mYxXF7o7baaRT7WYaVaCdN3RyDjqetXP627T7GPgRTaeTdvKjmYXtzT8_epg3WBUeWGcj7hG1Zgjq5RnkPsGDekGeYFcZakXu5A_hNi-0CVduddkCwergSRuNdm51vL5XLVBUKZXOss560n_bG-Sf8SoyGpeqbxFmP7ko2F-2-juEsHVcUw6tSCvWVHU9FnYDeEaVeDE6Ik9sB_vDDsZhYTmOWHezYsAHavVEpzE2Lyv-XuhvqDvEG586ivIVuIEO5nJQlYVfXFv2TgKCdlihQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین برف پاییزی بر دماوند نشست
🔹
با ورود سامانه بارشی و افت محسوس دما قله دماوند برای نخستین‌بار در پاییز امسال چهره‌ای زمستانی به خود گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466292" target="_blank">📅 19:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466282">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک صادرات ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c31larpnYS91ESl9QYNAWTofjGPRqDVy8YFc5uGc7vjTleBNK95Mk1Mbs06OqISffeXfg5EfREFmMxnUi5ptbAXCawBbtaQaqQnFNKG7o7yiPta437KkLgwkh9_gQFNWF6lXEY9LqPYGyl-giAMS6RuM8cfIUVTA2lG5Du0qetyUyNL1R-0YCcyeXT9ZYv28GYuZl7FzW3X5jaaTe3I9r1jC-dExF85JO-SN4TxtLf6mrgW8hgl1dsvuRKNa5J0YEk2nnp0Sparxfl-Ntlah-cNxCtURonk_zNxuC7Nz0WlRXZSD6U4rh8IKHpmRqYau6PBgtEsU6BBUeCLYhKUK0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a5rJ-cGYsw7FJYKizACLHk1L5nUuAY020ZTzlfjxm-BUoxgJWICTBFOTS9hktxJ73KKJtgcaLK40gekGettoaHH2IU2eZMKGaPZdEoaeqPUuIJEF-DBngMWxBTQfSIyUTSgD7_0yopV-FJrzVH_vuMYIO-pWAEy79juYLw1ad7yldBh2OR85saByJUF5PMjdimRz5hO1usQQ0ffDsOCxLu6e4XSE65TtS6XikKRPynOhCAqi9XdOdvHetvaJ4Hr9S6JCX09XAeGGPuPn9PHyV7YmYMaAdhGwRgyqo1jqRfo3dvu8OT70rKt4L-GMgL400OFldr_sP2HPnLt-Xz4G3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CaAunHJhaVv2fofzha5GkG0oKTvxMOD1Hjv1ESCiS5HiLD1tyQrP54AXWbqW7Wf98cRCpVdkl6CnP-Bwfm5cU-L_FMuMaOfIutrVEF4WWSuCOdQQKEwmLoVeL3ci1W4IFAFVDPyr5-U2r2qAnvGUn1fvXApzLB2kN2zDaFlytS7EaDqCA7T4MOfevvopTODIOErBYrTcCqAqHv4XIliOCPu4ydurNsA01DBMph27ChQDLVY3dVfodcc107LdMuwtsMjdupGxxeM60ECqRMBc4TXilhb7vf3fh4iQMJkSf0mNwkbkMkx8jYg9cph3HtrdzPIPwjFfbjFKkRyqLyudRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2bzZYTNuUlLq8tf1RrrSZ0DE1vqq31Bsb0mcSGc7YxODcr2pp28LvRUuYE1rsNqGsVsIg1VOdqamBszx-VmPo6iDRzw0kA0UIco6gZOcN3JhmogE4rWK0AnkcIdoRN_Pl5dzVtMUFztcHa5zEQqwM-e7IUfGuneDIAKO4nUp1narlGUjWcjGH7Aw3eQBTMA5wWbEidmjdE8D5kkg40U3OCXwnj_NDfwllHIC9jUVxEcHXqymn2ZnfqCum9My73XMYii8JoIoYxraNk04KvEK3WL3WX0dwWUXkZmvKwb6v8kIYpSPZ0FRhEjz6NDw3rQMGHm8jzHHg43aNNw-GW_Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H29RxrYnhVsrxUvvs7Fhjruc2KY2pzIFIMYrHyTC6ahuabV-1p0vAdPPwHm3zBm9AOV8kEwexuf68uAICi3zrKJdx6ILne3txH9hLL17AerkNqppg8zPqFORZ4lt-42TJEcsX3m8j4G-vw9O2_HpMWwpSCJ17sMC-kCfEFoCtwhhnsjrxWEJH1OMNTe9jtThStwJqg2utP-hr8XdrKjhG83MOXRtn4szk5FQGTBJDcO5_Psi7FTuCjwiUf1RnCWzwpY3Qi4bQa9C7gadLxykZgLrOHCvVoVixcsuw-eiq4HCWN89-yS-WPq77l-Jq9KzOaHuDDa0OmZwutwEj-ZPbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rq6Gk4IEk32tgcWiqorOESdq6615OWYwG1mCnwA9J7hx0Q_4lr507qAtgc0N3rFrAndDzcYf9AW48Euu-Ge-oJoQ-ek0PxfoSykpuoYI8e4o0ecvWtFPiFncdP-tSCXx5OVKleBcygxYo13lWDt8vm4du-FqxV6VIpLZqByftLNOCF8HTQKDouUb79BmSnBrMsuFnDSec3MHS47jqs5cePEYmUEY0jTaEecIubWFi_7bEloyN-UiOs8Pom4hGo_I-HQ6cFFiiTbIKcu0zbJd00elDkidVh6Z1tPJXM4-aL0D3fyvZKxno5nN_CSyFVxjZ_vyj-vmBGv5mwemiFQmHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ly9IsHOXdRhMraaV76Ww1Jb5FBs9QqEVHSDL8WuVYIBgQb7kpD9oWX9CC73JT7gndWxDE81WL8vOvkly2GE1S9st9FUeoSN_QLtoHx64X44-qPKlvIeVDj1lZx5-qQSz1l9zC5VFHttJ0hdRnmslOHuuQTewp2u4P9yTfF76j0s5-R5HqTntskX-RdQ3LaqPEK0KbNbI0-7vLQDZTIgkhOkDm9tnB2z-r6WF9I6AEpW5PggT85rGAlXSKjStss5S15RXzv_PRk1oy-8BHA9UQfZU4W1spVJ-9lSzIcob2MrtQgvQpPVEqIq44kkyCBrOXPG-sPuab4-v5hNBW6wucg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PHhV6qWa7fXNEX4yNXU9i37K2AuIoXoXMnXYt0dI8qfNaR30_rRuIxXqWqMmP-FnQMzLGTIJ07EAyZ1iOC03Jecopmc6ZNFg69DiM9gYslC9WqZSFiCX4KdEOlfuXrIuQGKEu35vSyX2nnaNNkcEuVdjM4E-5gFSds2QPmJMc7Lkwgr-ttkyTrNnsjHq07fhuUJz31WoZOoxqHB0zmZFgJvsxfx33nDsj6vafAxle2XVW02wnvx3uM4VdGjnFW0EaXatWTHS472qY8IwEOMc8EgsRb7ICrn7OXI53_M1gCwjkuF_NbrZmZveY5046QH1FwJv7Ou50VZqtX8sJUa2QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pVGa9ZXi-R3nTXWSru8BFySn5gws1VnytLUZ8O4YfLnbCwh5AwTejyRp87zLN68kbPWn7WLtB1nP0OhUcgVOVg181JBLmykRIL8Fueps9xFTSQjgnUPJtSe77i_gpXUwQqZQ2-eI_Wdw7aCF0XBhnNGqYWTLiWo_5RrKkO-uQeJVF1MJlWOg71aHzQpjIRJl7hPeALuoIBDRgAWnwO4kZgB7xtepksniMRW1two64K-FPETj5Cc-arKCvVEfCk8pUeXTt6d_FG39AMpJ6vMNMNz6YCowmpV4KD1srV4OZgcqnqa74nRYQ-egtQG3FE0qv-DFgUFlfRFC3zFwN7oOVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iGulOsEZUDTI8NQGyTXW1rQfJ54Qr6UDZ1zGYgUFTTz8IiavsGKQXzfALQ6C0Yjobu5b0rTaLvJvWPewjrbzOCt6aAB4I8GmKJwbcFDqpJfWQycl0RTtXu8NpnEDDxG6o8xWntA-f56PdRGL4xAD5BC7I4iOSWgtwHyUkNwKoGaqjO3bK9WKA73xzRVSm_wrEqj2QgXa19KgTVMobB2wyAk07KuzmR06FXWuwccHsB_5P7yjaOH5tEuRZudL5tD-FUPN4ZR87djr_1BnpAAvsr2doHlYlAv8rfF_kIVe4Oh2FtvR5KAzARPbv9cSdwQIxJYmRFthVbkpLC9OUv26Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏋‍♀
استقبال بانک صادرات ایران از قهرمانان وزنه‌برداری
🔹
قهرمانان تیم ملی وزنه‌برداری در بازگشت از مسابقات آسیایی ناگویا ژاپن، مورد استقبال مدیران ارشد بانک صادرات ایران قرار گرفتند.
✅
بانک صادرات ایران، در خدمت مردم
✅
@bsi_1331
#وزنه_برداری
#بانک_صادرات
#بانک_صادرات_ایران</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/466282" target="_blank">📅 19:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466281">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAy5B7Ot68AgVrkgEiCIEf-f6kv7zQ48tMk84nCTyhc9XSpm7XM2HTSJf-kjLrIlZQopcG-PU0V3AStIP3XIk6apYbJr8FuJ3HhBpshWjN_0JClIakvXIe45VeLHHvf0VJcUWLN5Tukb63TwseL01ye8Tm7fhd8prrn6upUhRo6KkkPjSaIJKsM_11jJlCgZBvTwE-8hGTAz1sl9U41XHJ1Shec_B3e6L1aBiJ7jiV0VVEv0-GTeL815_2mlz-kblySSj3JMKOiCh71ctOS5W8h48Bc2LUK08bPySd5AQumsQNuxcZOj2TY9ZmI-wFqn_yAh1R8knVhIM2xFw1dkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طلای بازی‌های آسیایی ۲۰۲۶ ناگویا در دستان همکار
#بيمه_البرز
علیرضا عبدولی، فرنگی‌کار شایسته کشورمان و همکار
#بيمه_البرز
، در جریان رقابت‌های کشتی فرنگی بازی‌های آسیایی ۲۰۲۶ ناگویا  به مدال ارزشمند طلا دست یافت.
مشروح خبر:
https://www.alborzinsurance.ir/PublicBlogDetail/5106</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/466281" target="_blank">📅 19:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466280">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/farsna/466280" target="_blank">📅 19:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466279">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2014acdb2c.mp4?token=kG-dLnXYnrljLqMMB4vZAF1VYZuW-sOPv0FLqBvBhGd83JsU5YR-qo12KQqO7TtW7zORcdu6O_grm-uIwSN6DdsuDaPBHmzTebqyY0e57dBxOOyJSIxfs8PHcgKaeC6N2tZKdcHnORn92b7ej4owO1FxscdahWFBM1NVBxAL3C2pVhZf5-XIlv8yhy3D54tZ-77UbJTs0cE09r70JiNw1wR4HarzmO8D9u69gEEY2kyA_VNzw1wonyR4rCi9xhnvrhqffTctq9FPZOiewgMqxW2pMIMW3M-5JOzeQ1KVspR5QeP-YTfAExlME4q6AXMxRmGF3wQTebg7veuH1nnDTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2014acdb2c.mp4?token=kG-dLnXYnrljLqMMB4vZAF1VYZuW-sOPv0FLqBvBhGd83JsU5YR-qo12KQqO7TtW7zORcdu6O_grm-uIwSN6DdsuDaPBHmzTebqyY0e57dBxOOyJSIxfs8PHcgKaeC6N2tZKdcHnORn92b7ej4owO1FxscdahWFBM1NVBxAL3C2pVhZf5-XIlv8yhy3D54tZ-77UbJTs0cE09r70JiNw1wR4HarzmO8D9u69gEEY2kyA_VNzw1wonyR4rCi9xhnvrhqffTctq9FPZOiewgMqxW2pMIMW3M-5JOzeQ1KVspR5QeP-YTfAExlME4q6AXMxRmGF3wQTebg7veuH1nnDTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رتوش چهره تروریست‌ها در ۵ دقیقه!
❌
رسانه‌های ضدایرانی سیاوش جمشیدی را با دستکاری و حذف سلاح از عکسش با فتوشاپ «معترض» جا زدند.
✅
اما سرقت، کلاهبرداری، حمل و نگهداری سلاح غیرمجاز جنگی، مشارکت در آدم‌ربایی، تهدید با سلاح گرم، شلیک با سلاح کمری و اجتماع و تبانی…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466279" target="_blank">📅 18:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466278">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJXPsy0YB6nksIZMa_fXOpcz_qIxnGJ-SSE_PGS-u138aXIwA5mM63J-2zu6iak38c6jYQMLX74hniPtMbwmlGBzht07Zl_7d9wen6e9sZPVRPdrphA_T4y0OChTh-IC5yg3KP35_V3eV5A0wyLxRuCugjjVKcdLHSurh958RlOqkmsUzTPyR_kcaK4gGbB0o8b73XmP_a2F5WsfrGisg-oLxFW0PpfTQXM-1adxdp75x0HD-lhDmwn5ZUi_YHb07Msqp6K8I7gYhbh4-XngePV7bivcpPFgZ5jaeT8Ti8p9ZNQvSW90l1xPPL1Fc8PgoMI2Pg8wYOJTbf5kw0ZJ_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت بهداشت: عمر نیمی از بیمارستان‌ها بیش از ۳۰ سال است
🔹
مدیرکل دفتر فنی وزارت بهداشت: بخشی از زیرساخت‌های بیمارستانی فرسوده است و برای افزایش آمادگی در بحران، تأمین اعتبار و تدوین استاندارد ملی ایمنی مراکز درمانی ضروری است.
🔹
درحال حاضر بیش از نیمی از بیمارستان‌های کشور بیشتر از ۳۰ سال قدمت دارند و ۴۱ درصد بیمارستان‌ها از نظر ایمنی سازه‌ای باید در اولویت رسیدگی و مقاوم سازی قرار گیرند.
🔹
۴۰ هزار تخت بیمارستانی در دست ساخت است و برای ارتقاء ایمنی اطفای حریق، آسانسورها و اجزای غیر سازه ای بیمارستانها حدود ۲۵۰ همت مورد نیاز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/466278" target="_blank">📅 18:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466277">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تداوم پیشروی‌های ارتش یمن؛ تعز در آستانۀ آزادسازی
🔹
به‌گفتۀ مدیر دفتر المیادین در یمن، نیروهای مسلح یمن در آستانۀ به‌دست‌گرفتن کنترل منطقۀ راهبردی تربه در استان تعز قرار دارند.
🔹
کنترل تربه می‌تواند برتری آتش نیروهای یمنی و امکان محاصرۀ بخش‌های باقی‌ماندۀ…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/466277" target="_blank">📅 18:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466276">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBrkdz1poOvlcfMOJoVESyB3b9Ad2LudcIIcY_adHFEze_4BIOZrookb_TPEOFLdT2DomSk2e5i9pP5COJMrXyalUHk5Y8-LWjH4ulYIpImtlOpDvl2IvbuRLv7oWMOpQsGjFFuA7aITZ9TLclvo4K463fqBdeZwUYmVerw3Hzv7IM9vBe7dWn8X5Nh5UNr1619d0srZbXZ4WCiEBCv3jBIdk6uGYH98QbgMnafscOJnlw2vv6gzmONhsFd05mll1-AxAZEKoytuy7hDzry2SPbU2qQj8yR5084KH1ZXw8_IrBd5V9ucy6diZqFfnkEI_4gq4ZivwQxAmy4LpfJQ8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه ماندن خودروهای گذر موقت در کشور هموار شد
🔹
براساس ابلاغ گمرک، مدیران گمرک در مرزها و استان‌ها اجازه پیدا کرده‌اند بدون نامه‌نگاری با پایتخت، مهلت پلاک گذر موقت خودروها را به مدت ۲ ماه تمدید کنند.
🔹
این اقدام هم شامل مسافرانی می‌شود که دفترچهٔ بین‌المللی تردد دارند و هم سرمایه‌گذاران خارجی را در بر می‌گیرد.
🔸
پیش از این تصمیم، رانندگان پس از پایان مهلت اولیهٔ خودروهایشان گرفتار یک بروکراسی طولانی می‌شدند؛ پرونده‌ها باید حتماً به تهران فرستاده می‌شد و پاسخ آن هفته‌ها طول می‌کشید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/466276" target="_blank">📅 18:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466275">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qqvm3Vji9ndERgNaK4RR24F6A0z_OfIeQlbypJGSiGTe45ExHZ42up0blORAV6fKstKJq-M5wgeXPos42M0D0wPJ8QK-8880mKnemuX9E1lw2RovmnOqneuFjwwPKdA-EngqELqG8Q3Dc7oRqML8bCRbPWNjjN1-OvGSmREzLgqX6Dry131B_PHaLW-eua65LgXfQ7DbKwFit27C7fceIpgZMMmKdsBXJCcWocA5esBOTDAkRI2i5P9eDpyOh5pidKUVOmoo6ahRqgx6rZHMC3fZFNgjl_KNnusIpb-zH5LQgczGKGMbaN6U2h6H768RExJGvLiLagYYvOE4QdznRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیر رسیدن آسیایی‌ها به جام‌جهانی فوتبال تغییر می‌کند
⚽️
کنفدراسیون فوتبال آسیا درحال بررسی راه‌اندازی لیگ ملت‌های آسیا از سال ۲۰۳۰ است. این رقابت دوسالانه قرار است با انتخابی جام‌جهانی و جام ملت‌های آسیا ادغام شود.
⚽️
در طرح پیشنهادی، تیم‌های آسیایی در ۳ سطح قرار می‌گیرند. در دوره‌های هم‌زمان با انتخابی جام‌جهانی، ۶ تیم برتر سطح اول مستقیما به جام‌جهانی صعود می‌کنند و تیم‌های هفتم تا دهم برای ۳ سهمیۀ دیگر به پلی‌آف می‌روند.
🔸
لیگ ملت‌های آسیا علاوه بر مسیر انتخابی، قهرمان هم خواهد داشت و ۸ تیم برتر سطح اول وارد مرحلۀ حذفی می‌شوند.
🔹
این طرح همچنین شامل سیستم صعود و سقوط میان سه سطح و حذف تقسیم‌بندی منطقه‌ای تیم‌هاست.
🔹
ای‌اف‌سی برگزاری یک دورۀ آزمایشی در سال‌های ۲۰۲۸ و ۲۰۲۹ را پیشنهاد کرده و قرار است نخستین دورۀ رسمی لیگ ملت‌های آسیا از ۲۰۳۰ آغاز شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/466275" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466274">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۴۲.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/466274" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۴۱.pdf</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/466274" target="_blank">📅 18:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466270">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pHoO6cLiIheZk7HBTE7PoBWgxAd-HjUWQ9PfFARj4_MRwkprIiR2wDFSzUWlr3eiq0BoDiQsAOUvjkQh3cjoeqNu8WJWENA38_v4lG7uK4H6IGUu0DoVWfT9YSEott0JTJlVxWjqfnJYmjHgWoik5SphyNZJE3jQ8yWthC5TuonfrgzyD7PUOWdxC_WLqp4U4zACLUZYOSCQh1b39AWQySwJNc0VihHpIIPQOwax9e9bpI5bJAWDIHFGMPtp6Slh-fkMfts8nLjblxlECzZftpSg9sltw4_p33RumXNxADD9X5_vM5Ybh8qNF8leSWk-GTXOT513Pk9DsrZH8SG4tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hcihaVWjfiNWkd7qICzJfmtwNT0vrRzgY0yd_20Y9OK8QlgInB4eKQSOSEYk-6wc9REdfXegsm9g8ZtahSiTUSTFGtJ_gOR0EmUwmC9HgGeSu9sH5ctec7wAvhk0LgSsscmNBe6fjtE3XUp_ubsscF_TOT6y-slEGIKDfeMkf__8EJTzOMlz-LO-PchSyFH-wG7K1NRYENlrc5-QoTm5AYbsrSTdZlN-q333Dl_ikyiBgTo_qB_rAECW8EG7lkuBNLCb4I75W0ccoxnuJ33Cet7d46TmJZKbua-l77SZeVnlGKaU_0GbtdlJlDQ9cvyffzOntwA9zEk5Q-61nasU6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ifg7XdEqGe-kNv_Bu-SoLe7Yw8glDok1XhpIZPu4vfBuHT39hoQsw4Ty5hEC_8MKQ8Z-FfjJJsyNfMfIMuptPMar0G-PsEinbR3KEDD7-d9ZWjG0hj2WTfihnn-OwBeyoKff1TRaiebU8TQPijqZg6O-a-Q1WSjvgs3rdQHv3ufgtLEpWZDGMDH9koU_hVacf9fJANjJxLeDGAviZTdrXH6BkBauIwWw58CBVXKyiDptgBZKl4SPEP3qTTce_Em5M2MFZFnLwvmZ91KeZziCK9QGZZL0lXedOXQPbTd2pd3WRnfersj0rljhtgBTkWCc9LxjeRNdO5PEmgZ38XdV5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yea1T4ERDZ6p3kfL6Xkgsa1hXR9lJh_9mcvHmml1BGirccqqli4zhksJGB5jQ21rzeFod1sVWd0Wog1jmHf7oqSETkGYhKY80C67Rj_MPAJyf1xZiFvrFRhf6hP6nlID-W8Ngu58zS0rbM_jX6A0BzprZwXWxyYcZl0VpoZlXeieYjsTyqLVpD8_7ZgzBSEs5tyU1-kLRiwq1ylyn38RgSL6Cylvjud7psH7zUzFV06d6Sq_r7hrUatAmLN3evOYBFiyLCMZ6OPzZ1-yAdF-yfqIc-vqFzWKq01RBfcgADL1DQqYt8gXEndJrDctwOBZ2JqAV23EFVuxJ_DN6DLa8A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رتوش چهره تروریست‌ها در ۵ دقیقه!
❌
رسانه‌های ضدایرانی سیاوش جمشیدی را با دستکاری و حذف سلاح از عکسش با فتوشاپ «معترض» جا زدند.
✅
اما سرقت، کلاهبرداری، حمل و نگهداری سلاح غیرمجاز جنگی، مشارکت در آدم‌ربایی، تهدید با سلاح گرم، شلیک با سلاح کمری و اجتماع و تبانی علیه امنیت کشور؛ بخشی از کارنامه سیاوش جمشیدی که روز گذشته به سزای اعمالش رسید.
🔎
این اولین بار نیست که رسانه‌هایی مثل اینترنشنال، BBC فارسی و منوتو با انتخاب گزینشی یا دستکاری تصاویر تلاش می‌کنند تصویری متفاوت از اشرار و اقدامات مجرمانه ارائه دهند. زینب جلالیان، پخشان عزیزی، وریشه مرادی، رامین حسین‌پناهی، شتاو ساعدپناه، نوید افکاری و... نمونه‌هایی از تبدیل «تروریست» به «معترض» با فتوشاپ هستند.
⚠️
اما رسانه‌های ضدایرانی در این کار سابقۀ طولانی دارند.
نمونه‌های پیشین را
اینجا
ببینید.
@Fals_News</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/466270" target="_blank">📅 17:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466265">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nt_amRuiTk3GpIaSkkTFJC0bJeRSt_QwtUnegV07v1CofEyF9dW8sDtphHI2Ib-_HbFt7PHl1HcF_nPNs3FxP6_T45fQN8QmRlrR4Em-_eboxJS7i68u0-3WzfBi5rQF1Vwo3AXiSecdSYioZM4yhW087tMArp8nsJF1vbz5HhQoNIH8Wf_KwsEX1RzgtugiMV24SSJyn_FfWabWE1mvSb6AsAsecZ0U4S5ASRVr0IlQ8rvxsdBhGJbNfh1Nww8lmVN_wPWoC8RG6AU4o9aGCvd_Ll5NacKz9WgMA78ZLu1x0zxZeynbL89k8nGNZuvnlezD993whRVETrGp0pMd8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tn8R67gKNCe1Ts_9271w1PL-Aryde-2yT7Lv7FI5tAs_6GQ-Bg9vEhxLN0I8jGF4oY4jZ8LoguNE4sM9aGPKK1-yOCkNvlNPEbw25o3L_irXzTzXMvnQsYQ-INExlw42yF7tR2SvhIroMNIkgRWFeGQlYnopJC-GT9E28ARubbI1LEAbQGdM4Pk12CyOgZPGUUBhB0hYA2tRYGYuAgK_OzLDOhTMf9NQxWYlVhXsrXIQg6eyEZiA03Cw9cTOCf6dPpZ3GLVX3mYK7opfQ47ybhSUbZqtEUYq34YfXLTFloA63LkWFtqF8Mdhf2BM62Poris_Z0PguvzYai007X9HDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cHF3M7mC-8y1WSCihe2OEzo2CtfGBhbIMvU0zI2uj89im5VUEVYTVkYbXzhJ1ofg5EmYDxEzwUEEQkvb8erb8TSHoeeXha7JxPT8glBvCpzF7C5OznO3rTjKfVna5fCurYxpfX0_jTWyThYB98I3U9BJW_p9aKNw3ip2zHuo2frRIxDvpEKKvGW8CWg1gZZUCl49AGUpIITUS3HCskNQq0rKgqsu-R5gVmSlfmOH5RBRNN76WdwppCOIEAEbA8pt7qT9owOTYqZExt4r2ter7-G7ThwfpOj8xXuyTa17yyZpCJYvdNPOtT5ABl7U5CdTVo-1JWDZhBmJagKl1by89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OsSgxaiKswnY_xlODJQ8zRl2Amu7HLmeZZ0GkpQVL9uQwIFHW7gAq3HkpB9L7gnIQIB4KXyHCzfiF43dTzXnfJrHYiHySjMDUDk0DBo8rL3XrUCPs707ICMIr-e2oyzlMzeRnMEauj87I5hOndyX6EliQzaJpnwqq7wySzVuBiKPBPcitQyCIJFPZtbVQxwxY_duNQ-bPXDWPaa__wmk7M21zUBh2mlncnPTim85Kmq8mIj0_QVziGEa8eQfrJprHMJ91Kk9G_atY_qBtOgoQHEtcqOFVjufSCupLO37e4EV4sG2iiqATvh9v4hQ7OrBa2hlQD2LnFfqvCwXku10sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e2cI-QK9-5OUJZduL6Q0Ihqix2O8-kqkLHbgHDeP8CwqI6tWdv9pjaVERecw0NK27hrl2UeSkf4qSXeF6lHZa2Tj6177qCv80fEcXpGjvLp6vKT_2fQF0qBhp92aIGJyUqQEUUqlsVtE9Y68AO9wGG2qFR79gKh24LHgyYatEcSy1l6p41RbK3QUkhfz-OjoCaja782sp35rmffSW6a8ssJh2psP_WGLYISaYLU2SGuMtc_orpCdS6Qlv3Qz0tdWwtDylBKloXtApgWZmJ-YpASF1F8ZN5eLd2J6pgTSt3zbjuF3r4lSZa6NUNxyfm0kkq2WbUqTrr4A3TTGWTQ5gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
افتتاحیهٔ هفتهٔ جهانی فضا
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/466265" target="_blank">📅 17:37 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
