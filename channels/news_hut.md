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
<img src="https://cdn4.telesco.pe/file/GtgpS4OSr6-C3lKDcBTpU0TTIzrlOuB0-an4VuSbr0DROZgN1gtvmWYdfD_V9ATD7KXqbp_IEQRXEBe0BmfzoDtujY1DI14xTM37MwOM4nkeg7BZp6guvijfJb_YWpMy8ZtN7jDLejTy9cHEffsNzOL0U-q2pACYNvSMoweHj8l7IdJ1BAjKQ8l48fMnOPQTcv3iWcprBh0r75E2oIIC7VIRGNQX1nkH2iIG8bG0YljPFRw_H--WsKRujNw-GiXM9nENIxq74GuBRARD-8tmrA-mpikxcYiMHJw-IqQpnYiAFcLa2W-pstEvb9couoX1bHzYQikI6UACRdLUpUVi1A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 219K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 23:20:31</div>
<hr>

<div class="tg-post" id="msg-66941">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚠️
🔴
مارک لوین خبرنگار نزدیک ترامپ:
اگر این رژیم در ایران می توانست، تک تک شما را که در این اتاق نشسته اید بکشد، تک تک شما را می کشت.
هر زن که در این اتاق بود به آنها تجاوز می کرد. تک تک.
اگر اینجا نوه داشتی آنها را می کشتند.
آنها را سلاخی می کردند، تک تک شما در اینجا میکشتند چون یهودی هستید یا مسیحی یا فقط یکی از آنها نیستید.
@News_Hut</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/news_hut/66941" target="_blank">📅 22:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66940">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c163cfe19.mp4?token=YU8vhMNkHsTbbL2QOr8LqpcUjM9dbYakBZw9oW9nXDZlnXfpOm1pGazoR1e_n9bwu9PKSquHIV-SsKk2bxXqjMRa0bYbbe_g5u-JLQAStm_l1fytOdON6ZRmp5p2Vb8fpuUA-bBqReDHoqpfyoqLoR3eTqCL_sFC5dlHs4FkCgaXPs1d2qmDAPMLsh3EeW16xDfcO84qiMHkRzbZKhcOmEhjnWPgjUNOjp0pnGasmwIrBZTp01m94UbR8FJuoI2YGmAmnGQsi4jcvFe6fQTgKf-xN5Br2hX4-m_2bZMnl8XdQreYveY7Xk4AFwMzjq2Ei6Jb1yExobKVSayiQwXpvIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
بنیامین نتانیاهو:
دیروز تهدیدی بسیار دورتر از سربازان ما وجود داشت - نه در برد فوری.
آن‌ها هفت تروریست را دیدند که وارد خانه‌ای می‌شوند. آن‌ها هنوز شلیک نکرده بودند و هنوز خود را سازماندهی نکرده بودند.
اما آن خانه نابود شد و آن هفت تروریست حذف شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/news_hut/66940" target="_blank">📅 22:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66939">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35c79910d.mp4?token=esl9njUAoYewhC5__UsK6mG-SmpmUvpLO05M5OQlC7GcN0uGfQcN9P-aM2cippM0mtX916X9MZPZVxG7ILxrWhGRDhiaTWIO-5aFoPIxuJAA6XgdbOPlecBWBIzqBG65JFI1GqY6fvMluIkBkUUfwZwESaOM-PU6uNfkwhEVF5xxWvaI2jTQTv8W6Gc-tbL8DZ4ciG2kGf9Rr3klzip8kO5DnTULhzLg9QfkV64zNiuVwQjkHEX5j7U2Hh8rxpzwC8aYIi1jXEYgVIhKYYEU8iMy7kF8mBQafViFCz0nI-V-n7tw-bl1vd0TNy7icbscKW6Sr3G-0HRmLkWXIzYf-S4ntiA2_PXkr0EXgCUuWAxQhphgR_UrBrXyS5ixAsuPFx2Vk1nUeEtH91UhxPi_UuX1lZ1ZaUgVup2JWqsjpT95PRQeVkKq4miEKXv3Ts7U9LjnutdBCmmQMeIqwRi9PGiBQkFi3oJB9q6rfkIdA86REhGkX7qybYQqDv2H43epWrQYRihf4Y97qDD3gRX1JeYDoDDD3dYdkpYUlPAUCcAy_A-F4vfaD8ODxCSzoW7m3iqizhyc-n_gK85Ehyvo6UhQz4Jps_TAGZ-sgR0Q280XyqmSlvpOqt0rw0oO2ozIKtux9c5bhbIyhcqW2SRv2L3eA9fsYCWbDx8X-hIm7zo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو درباره لبنان:
اسرائیل در منطقه امنیتی زرد باقی می‌ماند که ما را ایمن نگه می‌دارد. و این یک دستاورد بزرگ است. بزرگ!
چون آنها چه کردند؟ آنها تلاش کردند ما را از آنجا با انواع روش‌ها و فشارها بیرون بکشند. البته این اتفاق نیفتاد.
از رئیس‌جمهور ترامپ و وزیر امور خارجه روبیو برای مشارکت و کمک‌هایشان تشکر می‌کنم
@News_Hut</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/news_hut/66939" target="_blank">📅 22:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66938">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67074bb47c.mp4?token=pagtbWNGi06q7SvHMA92r0tlSAyzPgUIuzyfqLaysrrwTmlGDDwtrJLlJrwC0nH8Hy0HhSHaIEkOrbkGgwreOgeNHtgq15CRGyEBFRgVCGprCrKHEyZTPubFxIdh9mG6Pq3fscYIoL3Y8s_Vqv7dU0rG6SUk9DO7cviZGXnoHm7-3aApWuHvQOtBhoMkfmsJCLkh52BigiUIkujnf1UMb0KTeBfeseMR4VpX2VHl0ktjA-REf-pjw8oh-XbiClXFfhiTF72lXwHMoBYze6ZQscRM_9UHBxZDkXYTfVAuR1NKXK8LlwMpWJzYQAH-LfJE-mheDdn0yv3v4YvJmua1Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏کاتز وزیر جنگ اسرائیل:
اگر ایران برای جلوگیری از اجرای این توافق تلاش کند به اسرائیل حمله کند، ما با قدرتی قاطع و کوبنده پاسخ خواهیم داد و شکاف موجود در توان نظامی میان دو طرف را به نمایش خواهیم گذاشت.
این توافق «ضربه‌ای راهبردی» به محور تحت رهبری ایران وارد می‌کند. اسرائیل در منطقه امنیتی خود در جنوب لبنان باقی خواهد ماند و تا زمانی که حزب الله به طور کامل در سراسر لبنان خلع سلاح نشود، نیروهای اسرائیلی از آن منطقه عقب‌نشینی نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/66938" target="_blank">📅 21:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66937">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8KMrJMrSqeADz7xqtE1sehGPQyw16MYXOFOEDeoDFpfuFfBwCp0Jh_S3ztInHcyI0pu97wkNj-et4mza45BQLOgeB1MVoF3IcLcpu1il-Dxy_4yI7gqjcc1_S9-v0oFd2lchmM8dlijFIYV9K_lzegZ6qWGHDlOZT55SWrNH3pTlquM42F1vBQUX5ftlzH9m-iJJCNwA0lWA8dkn421XqtTsHUGnqrRDh8qjmmG7EphqualUHs4BFe3OYvtHdY2rsyGpffotgZwAqKpiXR9BpGMG5mTQL0iRyHoJoHGWBe5-ngGBWAnvm41R-N1VuV4vL_AFsV2-P1rmF5ugKWn6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
مرندی:
همانطور که انتظار می‌رفت، رژیم ترامپ چندین ماده از تفاهم‌نامه را نقض می‌کند. در نتیجه، ایران نیز مجبور به انجام همین کار است. جمهوری اسلامی تا زمانی که تمام تعهدات ایالات متحده به طور کامل اجرا نشود، به اعمال فشار اقتصادی و نظامی ادامه خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/66937" target="_blank">📅 21:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66935">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KV8yrRWd6bcOPlPLHkmTl-itH8illelxyH99UavFuI7Efgr99T1Bq7DGyeKYahg2tVBexklkpuvRBkzbZoSbbgsKUc62F2eTqOQHAr7zZJNswCCSmb3y0XnUEPNjtdsQdiD3khIws_TrQwYI8EzA3SUiBg-bUsYOQyTNv76lgcbOeJelrlg1Q18-Bv0X0lAn9-v4y3KWmrEg-WDUSv0udfe55wnZa6n8iHpmUVrL-xjsuqoZAsDID12-TSgnXyxELiHZj5rRFQRAX8PUZN7ChHYIFzZtRf-u1lfY70NA_ubwmRU-BA3ugEMBpc8HLGcVaEJlMwlCd1xZEEWh4o-MKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IAM3pt0tJaht_Ro9SDqWpeYfByIHM2e3Dp-IvWnuviXnS6WfnJ_72Uftif7uCvs7oOLBeicX851YIoCcH7nWM-F6xijCgibwaUPAIDFTOQ3xjwa97MjG_4Yx6dPv9eenM75veWkAVPKcMHbxiyxijaw_r7j_4nvvmyBcnY2421-LkV82T4-xYJuJ4eBqulS2TYbvc8FTPxJkBpmsPPryLRbf_hf37zbxYzl3b9tUqZnzh6yuJL8Vde3Kh_0NwZpktVJosYYhb3Rl0jEtIjE-sbq28mSpyyzHhhO4R5gIFyjEWsFa7JUwg3BrCQb-43bco2ysORNIVCSQV4xfB2qw1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترامپ در تروث سوشال
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/66935" target="_blank">📅 20:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66934">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWXqgtVdeEtlH480L06Tcgx6i_FMRLuiiFJgJp5dA9t_1dd9HCrR-akhDqi2PLSC2fRod075ShkQpFZq8ZSaTTiK6WGfzzCvkLIRU8xVBg9p_LoZbc-Y5pvsgZOqRsYdrNiRC-8HaWNRjdBtZcGO6Cuej8f7ZFWXMW3BtXgaRk-wH5AxLZlB16yUdenBhrFPvA62JsMT4VPF88o0TTbja4zsSZrnIJw5YnjZfczrJCz6lU5nEJ8aroU6j_352vFYS9UBs2VHlnQM0duaL_c6KuWWU2CmRSOpLMMoUY1BEexjoWm5k76PSNSFe-mHgExnoZI0j4Xp8DYbLGQYuy9fXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کامران غضنفری، نماینده مجلس:
گویا قرار شده هر موقع آمریکا یا اسرائیل تفاهم را نقض کردند، قالیباف ۴۸ ساعت اخم کند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/66934" target="_blank">📅 20:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66932">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/quxvzbJAjYCCk7ecuy_ywPjqHeKQDxqHJ8BVnqc7FkU0kNqinZLdE82eZOMb3FO2eSP7GvPgrB7KXueTDm2OH0s5a24-2YJYyDkpRDS8gN4BDXrW_hDrpgy7warZOTxGUpedHV6ZpJM0LBbnb5zEDI20DfVx0V6vwrudPqfyGBRcEOtm6WQDrFwohpyGsAyq5PpNP7gU-Jwimf5bfVgDRsF8L_5m8pfguFlUN92dK3dbrcrmFkkRhTvgU5p3JpMB3WYUZ3lat2BUEHW3mupHBWG6xCVa25_XRvQj1XFVQDsOT7AVzJrlYo4IHfF--2-kY6hzovOFb3na_x3EJXk5_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25ed09978b.mp4?token=BPdQu5xi-GjZPCuQ-jqOzv2g0mk9YVrl8ZUm2uscfewlr8zXFaFclcii6uVCvPeqWhGI5du0eGlDz-MiamlwFg_jh_q01Jv9N98zZgyEGwLiBfjVrdo-FUE_Lt9yvJoMK5Z11pjZKH3EQwMXyBEDv78DigQVKp_Dw0-rGxQUW7TIdNvUy6sosqmGhwjzU8mKWpQpjGNv-jGZ8pANqMZ_SOrGomOcIdzeMorANfLbqH3tvKsN1s9ymy-Gjh4Lw2CGNZhcQhvfr7yyITmMCMT5JRZxpJcQE8qJHsFIb9F-4NVlVZMTXauqdNXQHdRjvGy6H8LxaQTH2NKrJ15gqV3Whw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات اسرائیل به نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/66932" target="_blank">📅 19:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66931">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97e8d5b77f.mp4?token=bbalWJXusDVvu7Svt3osCUTP_EmeC2MCsJ48HAW8A08hDESQENvLi7HhqPNzT5eMmenMAO-29cRUdX5x9VsBdNMmQLwhRulLeaj62KMICXdS3MHJtD2hz9jgPHcm48YwuEcPcb28-0n4uLHEkmPJZDqB0XPQyQKzpbx6r4nyuTudCktOoh2-PkCV-mepIG7harJ0tjF8T3sAgcgfbBdWyNBVJ8zw2oEX9o4PvrpLujtyuVyNcGlpRRvMVzUR1YYWF6fCgs0Ix2JlVz480mFrmZZtraGP-ef5ntijsQBNZEUN5aumUF3s__DILN7vDJvDZLpcJ7aTFS3pY4KTbeaH_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نفهمیدند رفتنش فقط پایانِ یک پادشاه نبود؛
شروع رقص طنابِ دار و بوسه مرگ بود.
عکسش رو از اسکناس‌ها پاره کردن،
و از همون لحظه سقوط شروع شد
و نسلی که خیال می‌کرد وارثِ آزادی می‌شه،
وارثِ تحقیر و فقر و چوبه‌های دار شد...
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66931" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66930">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10face1c1a.mp4?token=lwU8DNLGsBfraOIHBq3_lQFiWKJb_zkBSSRqqz6DLzDo-NxTvGpHS_xrjWBOELJ7OG3O-LxC9cxruW5o0h6RmBliOGruki-4w2XowzZZb_O7vGAvNyY1cSwYNhnfyWfDtATCPAZpoIFiKw0BeEny4fsiU7eapekS_uqbXfZJZziaZYI7GqJ37TXPy7jMU0vGGqwugiM-OqGYdMStoi1mzHiPow4yc0fmeKi6x3PVeZ-6ucBGUexOuPqG5uqe9kRt8_mnJkroPyC3rQIm2oL_R-WDJ4x27AyfZ259b-B216fscCk9yDFd65-MlRU79EFm0AYcn-qofa3XBgXa_6VjHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گزارش تلویزیون الجزیره از خوشحالی مردم مظلوم غزه بعد از گل مصر به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/66930" target="_blank">📅 19:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66929">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krxVMbbD-b9Fwuz5FsKZYNm3kNf1p5lhEfLs70-VF1Kcg2WBkBzfKOssYd6S-PqKQpZtZAGXN1rBW6az7gcvP2VfMV-ADOhTaPteip8aY1MMIz_oaE-bK4qLWJnsbBh1oWAuvUeAlYNKnDowL0AJVZjHiQLVMJeL-QnU3fTpC2onudC2Yu-rl57_R3Ka7wJooaA7zrkae1DiLZ1s8N_eBKt_I7D8afpybqyk2VQFr04OqFZK_flbrl31s0FLIuqS5OKCBeqT0MYg1OOH-WMl_oQLWPf2QIj1w-mrS2CskYHYqNukBhFxyOyfDBdlCO6O8sTZzow5CPtENpsoAzuDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه به نقل از سنتکام:
حملات ایران به کشتی های تجاری را نادیده نخواهیم گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/66929" target="_blank">📅 18:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66928">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/843a55c77d.mp4?token=m3lcvhFppsqx7nOibf1MH2AX6CoKq17Vlz0JbFbGJN0PdUc7Bpbmds0sLVib5qYHL1qqW_3zfrmGo-apX1ZBimtPDq-KI5mTyOh0VVQu4B4twLEpAD8FELD5tby84xISQ_PVXK7dd6yp7rB9BUcRYqNBLXiEb134hm7pDIE9PGaykQ8KakiE1JH7gQ7S-kqcAiDF9ZpLbOGqMxGcdwnMmdKATvAxglyAvveqrXae33msAfM6a3JAuDDSzzd65uJ6Fff-6dpK2hDVZHsNueJ24W0z_gLSI45Z0zhJq17R5JbUw1pLUpoP7oM2Bnm77IV5ywahH9VXG5PSTst2WLs4Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
صادق خرازی برادرزاده کمال خرازی اعلام کرد عموش بعد بمبارون خونش زنده میمونه و تو بیمارستان بستری میشه که موساد میره بالا سرش و با گاز خفش میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/66928" target="_blank">📅 18:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66927">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2861d69191.mp4?token=GgEkcE6otmZrT3AjNBYYqaIQTfPy7APys7lJol-IgEeCQu0YxrsszG-mPJ9mgJDT73QCEXkGM-sAebkaYj-IGaUgbqX7evJ5iKk09UmOgh2X0pSDZpPbFmVluUoucVj1x9HoaYbtU91czJvxp9AbONMS-Q_8z0ub_5hnxl-we4GpRn8oo64bX00taDFeXXz1AAucC9LdvKaNwra-WRwH3wf2_Tx4Juo4ytYKpiwX9OUuqDlr_7u08ZtyL9DxoVsyy8dAA4EmoLOAg3lx8Em18uF6xJu8BlITLQoxGZg4g5EspbkU2sJpt_M2Hvjew2LCmo4cSCWRU0M4P-ligj7XrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سلیمی، نماینده مجلس:
اگر حزب الله در بیروت نجنگد، ما باید در تهران و کرمانشاه با اسرائیل بجنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/66927" target="_blank">📅 17:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66926">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🇱🇧
نعیم قاسم دبیر کل حزب‌الله:
این توافق باطل و بی‌اثر است و مفاد تفاهم‌نامه ایران و آمریکا باید اجرا شود.
این تشکیلات، ادامه اشغال را برای سال‌های متمادی مشروعیت می‌بخشد، امری که می‌تواند به الحاق این سرزمین‌ها به رژیم صهیونیستی منجر شود.
ربط دادن عقب‌نشینی اسرائیل به خلع سلاح مقاومت، پیشنهادی بسیار خطرناک است که از تمام خطوط قرمز عبور می‌کند.
ما به مقامات لبنان می‌گوییم: وقت آن رسیده که از اقداماتی که لبنان را ویران می‌کند، دست بردارید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/66926" target="_blank">📅 16:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66925">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23291f5586.mp4?token=thksge3Hv2N1-k4oh4a7n04qtYbdCBsjdXEo1ZZBsORx6KT58zcBu_u3DkopQv8L40b28yEDWUtxXfoLVo498-6tSguQeCeXlgtUiGl4Xll5xc8QEURtwK7nEKK-BC5M8XXbymPjrHUz83xycjtbZ9J7U8-EJugZphRuDfa-g4X4w8gY7Nn8qA6o4LhDLLCuTTi8J4RPO7eCwiB61bQtNBh8tgqxVbxAHALR-NfMoGPN_Lh35fBCbFIqotGoFevgK8vo10dPqXITY9tIWhevnFI4r2Ef3FgF8MAl3G8ydPIf7b2zO8MEvrPYk_J3K6UGSTgEx3PqtSwqxaz781oAig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو پخش زنده ورزش سه چخبره؟!
به جوادخیابانی میگن چرا انقدر الکی از قلعه‌نویی انتقاد کردی؟ جواد هم قهر کرد و کلا از برنامه زد بیرون
🤦‍♂
🤦‍♂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66925" target="_blank">📅 16:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66924">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/516c2865c1.mp4?token=XLfulJ4yLvKWk7dBQ8AgbM3h5Iplv3r-LIX0dhEaP7jLNUh7eZ8QfKa0-KINZSu53ODlhl62WYvPFB9k9ezu2dwDXNrdKxkPtWOs6NutL70mCP5fuTeA4La5OVB-7wPVZAS6bRrXQyMLB7mjPQfnSPSTXBas7xW1mrzT1RDT8WJYhFko70xGR-ozcGb1-bk-86cAYvmjjHrm4XgCP8Ib278aYNNsHLZ0g1DOZhlOzUYYTVCx7X2Ho_gi_tYpHWzQkXK-j-d8qZ659bN233KhR7v_q5SLyTVud_FvlQ119fWqdleabShvIqKK7aFoPEhvSDLkYFhZVj1T5wWSrvlcsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ونس درمورد سه قطب قدرت در سیستم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66924" target="_blank">📅 15:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66923">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/097bf86cd1.mp4?token=B__oPwVIHAMh4iJW5hYctSkBUOZh7ajiNt3BgeBNo6WcQucmqpvbYA1wwoeaPmUhLytLTsH5E3jjGObZlM1ub9jG9eV2_bYbsMTYarr5qeiOQuauaTA0OPszAEKXs70qxbIrbbKM9a-UPJQDNW1Z1nLL_Px3w931nCQEsJ84ZT73Zha1b6pfpP_gupjrxcoQKkk9s7N5wFmYM29E9r88dDOBpbiB0XQtxDU8ls9lwHKxVvn14Do5t63we2MMItmy_SFfBIKQEoCgmEnPyKAVDWH3gyilDXoKU7SL8HDcg9_iUfryuov4-HlW-cQ7qSV3YD3Z-9Mb_Sf4gRr9gzGjRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
تصاویر ماهواره‌ای از قبل و بعداز زلزله‌ مهیب ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66923" target="_blank">📅 14:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66922">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgC2Gh9lAPm-Sytlwe2MJTZn0rqvEs3J-UCCWAPQrj0nk6V4ZkS58U6al_JP2ND2Q4Y87FE0ldZt8J3Xiyec8Sxd90KdvKgTYbDcym4oF3igqADc03jFYzWqZNELx3H9ctOfbM09GKwN46UusthHhmknOZO1NuOZ7qrarPkPJdi43TpuDlFXA6WHTGhclawMrmnm9sDLQJ_73i1LTO03BacuYhZtnj4Rp2ZlM0MrmXAcU5WNs46JXijcKFYel5x3_ystu__2KakJ_jdEXMIi5ErfkKpMwou1vSqsJVfTKqF6ulhoD2JopNVfjzPh-TYPwHZVuRyDILZwTjHYX6EsIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن رضایی:
پاسخ به ناقضان تفاهم‌نامه سریع و کوبنده خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66922" target="_blank">📅 14:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66921">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
🚨
⚠️
صابرین نیوز:
این نفتکش، برخلاف مسیرهای اعلام‌ شده از سوی نیروی دریایی سپاه پاسداران، قصد تغییر مسیر و عبور از آب‌ های عمان را داشت که در پی بی‌توجهی به هشدارهای مکرر، مورد اصابت قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66921" target="_blank">📅 13:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66920">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UuVa4pik5EfxKduS_tZMDPZQZmR0FmuHUqNZPwjLmzCTCysUaFlXvbWe9RtnOeuVecweDvbNo3EKJ8SLNa7ceVFmHrIFwEVNDOc2umjrie3zAPvMAFKR7QdzrJPJMh5RKfv0xTbQgSfKDXqarxmMNjCNyLVv55PEj8zabG_ekIBddlfA9saLnlK66DJpq36Z_wN38m37rArC0WTewgzyp5Tqx9BMNe9QwUWVrNy0qvdTE2R89ZYgKFbDjNB0D7d3MlZAPF2jrJammzPL45Oaep72HtyB-H9aehmyqH9Mvxob2tmRJoTMebg8rBfYBvQc4WJxq3FPwHEi9AD2tRJPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فوری
؛لحظاتی پیش اکانت عملیات تجارت دریایی بریتانیا اعلام کرد یک تانکر در شمال کشور عمان و در ورودی خلیج فارس مورد اصابت یک پرتابه‌ی ناشناس قرار گرفته و عرشه فرماندهی کشتی دچار آسیب و خسارت شده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66920" target="_blank">📅 13:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66919">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
بحرین:
صبح امروز جمهوری اسلامی با تعدادی پهباد به ما حمله کرد.
ما این حملات را با شدیدترین عبارت محکوم میکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66919" target="_blank">📅 13:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66918">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvWRSqtPgJWEfT1gkr_wSEesoZpL8nGvhH4NcMUpsB31gE_Lyv85edsGJuXtiOXPZdAXipPfWsjloB1n5i1L472bCmQfxHOjcH6H67k_CGjgIwzkJpiGBiSqxH7BG9skAlyvVcQgL6QgbfoYbSc_6JEob2SPj3O7H8_4ioDTHhZNr_2vDJK-CXYnsF5TDavFFhYD1Ds7CI-VXq8Ic-QOXiaJKOembwg4uPE9hNeLrho8c0qi5-f7Lw5ck2yY_b6fGsaqUdqv5MslcUpiSZMhWlEmEfafS-QfdUPf4SdTy2c1rcjk9aDfdVTfZtYdJvMl-nkbi4w66FKaeqoG-H_r8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
نبویان:
ضمن تشکر از سپاه قهرمان ما به خاطر پاسخ به تجاوز دیشب رژیم امریکا و در نتیجه نقض بند یک تفاهم‌نامه، مطابق بند ۱۳ قبل از عمل به بندهای۱،۴،۵،۱۰،۱۱هیچ مذاکره‌ای نسبت به سایر بندها نباید آغاز شود.
منتظر تحقق شروط و واکنش شفاف و پشیمان کننده‌ی مسئولان مذاکرات نسبت به نقض تفاهم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66918" target="_blank">📅 12:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66917">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6e496d9ac.mp4?token=bynGzpRYPjR8mCLsLwumKO0O17RBUGUCAP4Bc0HyzoE4NRQIZSe3T606qyWS46_T1KSbWB5DCT4zTazMZGnT4jfvv_ijhsmSzrnhrEIvsC_bkl9AnTb2QWq7l3_VH4YHzQAIy8MjhVuCsDdnRTQv_4F220VA6tnu9nh9v8I5i56q_ELelmP3gFNTnf0JkXGN1RmncW-U-tJZzl4DPTNnYG7fWO7-D1YNrDAx8jW-h1RXLGweQscT-xitxRI_vDl36-fWfjIFLhuvQm1iOqftngGFMM8rdqbxcKqpxIIq7u3gjmrUpTF_PBCU83oQTGq1_jxf427W0U-b5dgOegeWiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله شیر تعذیه به جمعیت
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66917" target="_blank">📅 11:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66916">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02aab4b18.mp4?token=Ncm46_2bEu6Z8BGvTmHFjjrB_iJegPM_SmC3EeLx3TNkkG2DHLCM5kEF-I97ImcO0v1NtqcLLOMr_46BlqvmM6fUQ56eFX5n_Ag5v7azb5FuX3tO8zfUhdQQF-fqbagULrgoX4znbRwAf3cp7K94BIl0EewHm88VMXLg2NZ0L3OVYfoHCLdA21jJM5U3b3hwn_agrcKKnndfbmim2GJusDmacExwOm_vfINWY5BvmbnUWSGPaHFUw_2OqJxUf3WKeKp1oLWDphJdrZTnedy1_Odc4EYBv5Wpf3hTQWZV04waTPnPuQPrV_mTqe7bpxEMF4h6Bkrl69sDL4T2dTnE_qm8cERdV9VQb2xhM-fz0lAqD8n-lc_yLJb2Qp121AI5GjV80yR_dX52YPDn7NedYzgaSKsrd5Z6FBRhlBniGABk4kRKGk7h1C_QPkhrUzbiN07Bg-95Map9b5W2UR2L24rc4Zb29NkCwCQg3L4WsXwCiOsidFNljgRJwzcrFtxsFiHY7A7W9MmzJQGNso8zRPMXivOucb1hqB8HdCtVr85dYzY4v11fijnQ049oW1mKXN5mJg45kY_RGD-7FATCrn8AmcQYcSUx4YZPKOFtGpCa0LAkT4dtotfkV1zYZdA8uAzocNj0iDyVZf5wGO8EH8V9G1JfH__5wWSFuMpkki4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک آخوند:
غلات آمریکایی آلوده هستن و میخوان ژن مردم ایران رو تغییر بدن. آمریکا قبلا شکر شوروی و برنج ویتنام رو آلوده کرده. خون هایی که قبلا برای ایران فرستادن هم آلوده به ایدز بود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66916" target="_blank">📅 11:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66915">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vlf3k9TXdq8D44ve_uadCLO5tJwOJMbkafc9XA6e6ITVCvjqOgP4Ln681-ffb2P8hxEq9KPQdtfoictJbf77s8tFiz91JzG3to4o7cf58YM1J2cQMhc-0sFBHWoZXles4PGF3y172UR7QIN9zlGpSScw5vp-x7JGmebZyvScbzB_Ij2XIcWbCaB5SWDCER6GzkZsdJg14f_KImnxIA2u3jJKyi-9nr1qt7gFzxjiH4DDuDd2bmD7fpa1ZmQMavSPJnCVK5qDqzx2EBaWFlRV8Yp7saR38PHmjeJysQ_Wjsag2t6Kr69l5We61lfi12YNkQFDD0NCL0BnBNc4En3A_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ در تروث سوشال:
نمایش هوایی چهارم ژوئیه، در آسمان واشنگتن دی‌سی، پایتخت بزرگ ما، بزرگ‌ترین نمایش هوایی در تاریخ ایالات متحده آمریکا خواهد بود.
صدها هواپیما از انواع، اندازه‌ها و سرعت‌های مختلف به نمایش درخواهند آمد. من حدود ساعت ۹ شب سخنرانی خواهم کرد که پیش از آتش‌بازی است که باز هم، مانند نمایش هوایی، تقریباً ده برابر بزرگ‌ترین آتش‌بازی در تاریخ کشورمان خواهد بود.
پس اگر هواپیماها، آتش‌بازی و دونالد ترامپ را دوست دارید، آنجا باشید!
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66915" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66912">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uhYx6bnAVroOoIUDEcnLljcxhNe8hxDSN1CsHaSeIenouILd2uBxEN35iOLtpwLBgQVSzJMde5AH3J7FMHeJ17Be6dXf9BsSXm-C3mRE7cjvwDuYjnyS18WMB-dGdCOBZ1PxcT8VLXofX4q1b7vUE0MtpBC30B5-stb7jF2QVPu_4iiiL5GIK5XGS1WUmDCcTYZNQKs3_ofBbD4CUCQ5tDtvhXbnD5XY9lENJNB-W9OlMw9Pki8wrXx4_RpAMTxyu6GOlcFLj4JOm9JuviODvCFzBZCqHyP9JFXuLOF4FTVOhuoJf9hV8bSgMtydZu9z5ZLmagKHKtwxvugnth73oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJJn9gM8OEL-Wy9GzVzbXm_kop0eBm6ncb_RsketF2hyZE82D59rBZuX2DTCRAwl5lAx6bgykV23BhUPxBXz1Yg_NXFC3o53-wSYdp-T7iqzOP5TfM9BWIpPydXFF2aEchRdowAAJzRW0eT1KPlYWnmUDrYuq9HH3is-WWsCfqWyeGwL1noKgenMWLyt_UCaD1zm3K34Hr7wn5QQQXgo75MiL0_ATLhWGQUp_HKZvak2Sax24i0xX0xfJM77mHL15_5eqLSsPc-3Gm2hR5Fc_gvl-8v2Z5KWWDpgVKRGbThCIZgnyCZF-j6QWD99rZz4SFPKBwWfolhmZx3m2Z0rcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/812712f3b6.mp4?token=oZQYx_UDDBEWf21Y5gapWIyvSR9fMfumnAe6Vl1TEE8hHtMrpHSrQG2AgJh9LI6l9LTIT0Kwn2S5AXnZwyUN9iY9Hu6hJwLaEoltZX3iWzCRrzEXfg-cfbZ_SBZ9Gv96feeBaUan75VKEXktMchx-dI3XzFs_NERW_yXIRZIMgH9Celmfb81_zKSKprNIOmtHIjVt6SIbeTMzWqchL1ZJVX0eXcQwBQYSx7tdw28vxOtN80VaENQX8S7thvhl6-JZjGIUNyrLBCL358bPLfJdKX9FQfDfqoYujsKJpnBqIxllfkhDI4CbIALS2RcMeTrjmKtBUJccVm62aSut0d7jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برخورد هواپیما به آسمان‌خراش ۵۱۸ متری در پکن
یک هواپیما با آسمان‌خراشی به ارتفاع ۱۷۰۰ فوت (حدود ۵۱۸ متر) در پکن برخورد کرد و سپس به زمین سقوط کرد که منجر به تخلیه ساختمان شد.
در اثر این برخورد، دو پنجره ساختمان شکسته شد و هواپیما کاملاً متلاشی گردید.
دود غلیظی از طبقه همکف ساختمان، جایی که لاشه هواپیما پراکنده شده بود، به هوا برخاست.
شمار تلفات هنوز مشخص نیست
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66912" target="_blank">📅 10:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66911">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFe_kQ5s1Svw0XvkIBCKHF-GsdX0x6JkqrlakBOr56BFtx7Xoj_zFn-CidjsVwlgwUBCR84UIkueSntFaLwaCBQ1IPiGz9RfizZMblQUZ2Kdgm4SLbFUBFZcGJUNlOrOpJu0C_Xlgk429Z-oN2z6mQQ8Fbh3YlGJNG_UnFJJmu8I1Y366OiomUBJKhLzjKmIKiFBB0YNPSGCZG5BwcoTfwRMF1-J5EqgnDlzHwA9wrTgRfOjXCAkPSoocmpyg8sM9u7vrONQXfUgZqAJ2BnhlQNf9xUDug43BJ6IGhu1I4qwtkr3wDR-4NCj6P1x1Iq2wrlH_I067rEFQHFbcei_Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
❌
🇺🇸
آیت‌الله جی‌دی‌ونس:
ایران توافقنامه آتش بس امضا کرد. ما آن را گرامی داشته ایم. اگر آنها در مورد نحوه اعمال تفاهم نامه اختلاف نظر دارند، می توانند تلفن را بردارند.
اما خشونت با خشونت روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66911" target="_blank">📅 10:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66910">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=fK_T7yztAfYsOAV4Q1ibH1ZNoIb9It56lVSdty9tN1ixLVGUCkb6nvxdQpzsDEtbvHWovRRmeU4UJnUOZOkRp1JjpPOYR82iuGqWGY2gvgP9bh_9CaAigmV3M9-bbbsZiRHWDTGuSibgr_N_Y6IfqAQV9tYe7dLzdFkXDNMLCP3KONKasFBk4oAYNwR2rURp57EyLWGqFKYTAhKwe6CQQSBNwFsod4oMSudRBycvDCHUnPrttOhqY6s2qssfqbFlgpDTDg0T-KVGwYlQvfnflStVt8B_FYLM-AAYMakAESpD8xHAdDR8SdfdwhHawGWRFQhh8avDMqElkwz4DPfApA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01b5404ad7.mp4?token=fK_T7yztAfYsOAV4Q1ibH1ZNoIb9It56lVSdty9tN1ixLVGUCkb6nvxdQpzsDEtbvHWovRRmeU4UJnUOZOkRp1JjpPOYR82iuGqWGY2gvgP9bh_9CaAigmV3M9-bbbsZiRHWDTGuSibgr_N_Y6IfqAQV9tYe7dLzdFkXDNMLCP3KONKasFBk4oAYNwR2rURp57EyLWGqFKYTAhKwe6CQQSBNwFsod4oMSudRBycvDCHUnPrttOhqY6s2qssfqbFlgpDTDg0T-KVGwYlQvfnflStVt8B_FYLM-AAYMakAESpD8xHAdDR8SdfdwhHawGWRFQhh8avDMqElkwz4DPfApA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قلعه نویی:
اینم یه ازمایشه؛خدا داره منو میکنه
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66910" target="_blank">📅 09:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66909">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e70e539fa9.mp4?token=PDiiO3IXLhEri4L9UeiIlNtbtzmd6muDXpQmq7K9c2mF7C6cnAMlxCmRTV6qDVKp8S8QHaKBg2pDyBI3GNMOL8Hd-g-BmFrNzBEosURYEr2n0QcxjmM4-ZTU5Ju5w33pJCMzQy3_61uUg1E8LJqrwodaMEpwflSE3XbXMqBTUu9Sl4zdchsRtsnQySKTlbs6ed-SuAQl3stvvvHI3pb-lqHxVPZmmKZlXq82TLCkbtHxibESkgWds854kbjnvH6qHqJucPRYkep7GlpzqCsoa9VTZfKErnuculFfTklThe3GwnszXCsp6R1_Tw9EzjdQ0_wKx7Zutj0e0yJb2X2wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه رامین رضاییان بعد بازی
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66909" target="_blank">📅 09:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66908">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=BdS26E3SO6jNfAf12G68NAGI_bwpHpzt0hSTv-HNWcyus70WMT7hA_M0CM0cZWi2bP1wpp5Ttmh8xb0MJZj2zpRFZvhTwWc_0hIKNhjzjvA1k1gsmqwmUVNinXhWC8v7FUKqX6IiUmlAYEf8IUvnfTGjH9PSESNwQcp3geIpssdYQsMpX3jr7-ouG48Mt5Dw7pMHhaXJJoC37tB7CViYf5gjaSNKVsBeR9RBWK4ogMTH_AaT6YuO6JSdeHahEqyzzwCelg94n70A1_SgOtMw21sIjmMigFbHlW6X0f4TbFqtsU_z_kdBmx168N3-QTnEiL74KwY8pCOD9ADuql6J_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/449f3cb5a2.mp4?token=BdS26E3SO6jNfAf12G68NAGI_bwpHpzt0hSTv-HNWcyus70WMT7hA_M0CM0cZWi2bP1wpp5Ttmh8xb0MJZj2zpRFZvhTwWc_0hIKNhjzjvA1k1gsmqwmUVNinXhWC8v7FUKqX6IiUmlAYEf8IUvnfTGjH9PSESNwQcp3geIpssdYQsMpX3jr7-ouG48Mt5Dw7pMHhaXJJoC37tB7CViYf5gjaSNKVsBeR9RBWK4ogMTH_AaT6YuO6JSdeHahEqyzzwCelg94n70A1_SgOtMw21sIjmMigFbHlW6X0f4TbFqtsU_z_kdBmx168N3-QTnEiL74KwY8pCOD9ADuql6J_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فرماندهی مرکزی ایالات متحده (سنتکام) ویدیویی از حمله نیروهای آمریکایی به یکی از اهداف مورد‌نظر در ایران را منتشر کرد.
حملات سنتکام در واکنش به حمله پهپادی پنج‌شنبه سپاه پاسداران به یک کشتی انجام شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66908" target="_blank">📅 09:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66907">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
بازی تیم جمهوری اسلامی و مصر با تساوی ۱/۱ به پایان رسید
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66907" target="_blank">📅 08:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66906">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66906" target="_blank">📅 02:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66904">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qrO7cSrShcbA7oEVSGy5OWRjzxGLCxF-edMDWKn1RPt9HA9KJVM3fXvMWYGyOQsPlN68UOuZ0g8AHCZgyZ7L3BWLKZtMlLzsQSY1x0O0QdGP7qSCPQLv0GaI9GUDiVk0GA1dmY-QquKn3M2ufhxBj6mgV7dTo_P12UOu8c6qVOv6_vBlLp0jPzhbm7XZCQh1DPPQ7kSRx7BqnELKKgbLNgcJHjiavAahFoarTXpMkfnAlxY3UENbDS0V1bja6AbgWFiYB539GxTZ0SpjFhldfLt2L2yEb19ChY_es5VRk8i1QiKevT7Ghc24Xg_jMvOSAxlKKD6nFUghENAHiByVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66904" target="_blank">📅 01:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66903">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
سی‌ان‌ان به نقل از یک مقام آمریکایی:
حملات آمریکا در ایران اکنون به پایان رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66903" target="_blank">📅 01:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66902">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه پاسداران در واکنش به حمله آمریکا به سیریک:
نیروهای ما موفق شدند این حمله را خنثی کنند و نیروهای مهاجم را وادار به عقب‌نشینی کنند
ما تأکید می‌کنیم که این تهاجم بدون پاسخ نخواهد ماند و پاسخ ما در زمان و مکانی که انتخاب می‌کنیم، سریع و قاطع خواهد بود. هرگونه حماقت جدید با پاسخی سخت مواجه خواهد شد
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66902" target="_blank">📅 01:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66900">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=HJxBo0cfAs3SjLGQulv9YBju54HAfcLpbkL45d9eIpTqcG8oe2NBdGqq51ySSF591hkPe0yRt8G551Zph2okMJC7owW_aeO5i-fjF_xtWGaEAWozKkTb7OyM0Pex82o0uAKWgHgwA8vhm9X-1to3dBGhfSlwzEvQ9uzVyvNJePYA7najkY5JvC8EVVO3GV0g7jK4fWj-0843xY4Nylpemm4W3nGeciMAju0JnSu1bSHl4t_KO8baZAkCgotG0I843bW8ZFPC94jghMkgSGNlzP3y3QIDfJeB4DOjgsjlmSz9xMO8ma5qbDvGbuvWfNuTjTPvvjYmGdTHPVoknUF5Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/378d83ba5f.mp4?token=HJxBo0cfAs3SjLGQulv9YBju54HAfcLpbkL45d9eIpTqcG8oe2NBdGqq51ySSF591hkPe0yRt8G551Zph2okMJC7owW_aeO5i-fjF_xtWGaEAWozKkTb7OyM0Pex82o0uAKWgHgwA8vhm9X-1to3dBGhfSlwzEvQ9uzVyvNJePYA7najkY5JvC8EVVO3GV0g7jK4fWj-0843xY4Nylpemm4W3nGeciMAju0JnSu1bSHl4t_KO8baZAkCgotG0I843bW8ZFPC94jghMkgSGNlzP3y3QIDfJeB4DOjgsjlmSz9xMO8ma5qbDvGbuvWfNuTjTPvvjYmGdTHPVoknUF5Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
اغتشاشگران در حال حرکت به سمت مقر های دولتی در بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66900" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66899">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66899" target="_blank">📅 01:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66897">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A2dJUbzTQauCO_ciIKS3yxYF1vuNa320SMxZanGwEG7MQgJzfkej5AKvTjcdnvBrV8T4RiKR3RHUl4ON5OGtKg_xgFiAmOFDc87VWwQFm6LyAtG3hcPg5TJAC0Pi2kIDAih5FLgWHt5dsajT1LLVb7pdieGGg25jKETqrStR79ftFIZaosNa-hRsQJP_hScKG23QTMe9PoIgmFoD3-kzninrf3ugm0NZfqjUAvm9SJK-hwiYVQO_G9T-_kptkP_JwFUTIvneZGTjs7Pthb1llfEMppwPRdIxMNlzHdSkiWxUeNbMvPzNFRMkeSB5Rp24vh4zNoNknBGeivlmfC7k4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c146777e05.mp4?token=ZJkgb7NAAL78yjwDDzwFB43q0R8swNQHnvuBhiNlY_HGgRyO9CTX3D6lyPxdjOtSSXsiYguiryc0DboJxJp7Guaj4wuCb8vLJ-eL727qQyj9PEXQ6FYwIg8VjRivRrZPdgul1I6hHEXua8T4L8Xx6Ei4mNqP8IPD9PQw36HqcAD12kQz43iViOcs81GstDoIWJWrdwQzBXp-kruq7qsMBOSqeBQihknrsJqkW-IU9TJuqzMOOl7xvAhCbskk3xcBpJcXV4bkAcB6QT8uVBB2ScLj5Yqyj1QmJDOzPwfnPogOLjFaszrLqEW0-uLQqxabnCYNEgt-JPSff_ulXy21NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c146777e05.mp4?token=ZJkgb7NAAL78yjwDDzwFB43q0R8swNQHnvuBhiNlY_HGgRyO9CTX3D6lyPxdjOtSSXsiYguiryc0DboJxJp7Guaj4wuCb8vLJ-eL727qQyj9PEXQ6FYwIg8VjRivRrZPdgul1I6hHEXua8T4L8Xx6Ei4mNqP8IPD9PQw36HqcAD12kQz43iViOcs81GstDoIWJWrdwQzBXp-kruq7qsMBOSqeBQihknrsJqkW-IU9TJuqzMOOl7xvAhCbskk3xcBpJcXV4bkAcB6QT8uVBB2ScLj5Yqyj1QmJDOzPwfnPogOLjFaszrLqEW0-uLQqxabnCYNEgt-JPSff_ulXy21NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
اغتشاش هواداران حزب الله در بیروت در پی امضای توافق اولیه میان دولت لبنان و اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/66897" target="_blank">📅 00:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66896">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
🟥
فاکس نیوز به نقل از مقام آمریکایی:
حملات آمریکا به اهداف ایرانی همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66896" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66895">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iC3lCHwOgYNse6hqaRBpq2uBZ7n2QvIArxC3pj5YgMPFs-E9u9T2x045V3uKYwwDE4YX5gwR0Ga98MCr-o_fwJ5bQRdRJB2-JNzpGNs1uKJrDVj8viAO-SZV56-f4LBR1etjcp3uqrBsOlJASiy3Bjnax7Bm0_a328fc_TxJztUjFK8PnwsZ-KlkxOQbNTtggHLls7q2lxomFJpsOU5DEZ-pJmP5NTAborZBOAEpgaPBZ9xp4Had5QaZXhKNUiY48lohWApsocdolifeB5mQ3u8DJzk94NpYJDvi_DGLosLnyFOLWDAc4zEZaOCAaOTOEVLfyVnLHvpZf_4jTJGZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
سنتکام:
نیروهای فرماندهی مرکزی ایالات متحده (CENTCOM) در ۲۶ ژوئن، به عنوان پاسخی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی را علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آنکه ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک طرفه، کشتی M/V Ever Lovely را هدف قرار داد، به محل‌های نگهداری موشک و پهپاد و سایت‌های رادار ساحلی ایران حمله کردند. این کشتی باری با پرچم سنگاپور در زمان حمله ایران در حال خروج از تنگه هرمز در امتداد ساحل عمان بود.
@News_Hut</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/news_hut/66895" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66894">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
🚨
#فوووری
؛باراک راوید به نقل از منابع آمریکایی:
ارتش آمریکا به اهداف ایرانی در منطقه تنگه هرمز حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/news_hut/66894" target="_blank">📅 00:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66893">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
❌
صدای انفجار ها به «طاهرویه» در سیریک هرمزگان مربوط بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66893" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66892">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=e5r52Oru92p7jrhUeVuBzdF3_bhvMNDHVZ7vDREBRfGPsWOA8FPZi2fzgbP5SK1-1vAVqpboQNYj6tvNfK6pyY_7nQm-BXBSernwZlga8FlMUY1gshNxgOZ8FnJXBPrZjP7ze1AFGaj9ISv1-cAbHLmd9LoBWSfeKJppPQsZCsQbzHUKvdRk0bscnz0dbo5GHjE4rkjiH6pXBMYLEHAhxpHlfZd8hqjjBxKOXPWHZ6RXu5pGM4paHeoTdAPGC_E4xmzEHVYOnWmgb8AbqxvBsvax2sRDhrNz-QPkR46W5nBwvvIWG5zRR3B-MRKcSHs-L9UnSXU6Ez8YJPJZ7V6Qtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c003ad7ec2.mp4?token=e5r52Oru92p7jrhUeVuBzdF3_bhvMNDHVZ7vDREBRfGPsWOA8FPZi2fzgbP5SK1-1vAVqpboQNYj6tvNfK6pyY_7nQm-BXBSernwZlga8FlMUY1gshNxgOZ8FnJXBPrZjP7ze1AFGaj9ISv1-cAbHLmd9LoBWSfeKJppPQsZCsQbzHUKvdRk0bscnz0dbo5GHjE4rkjiH6pXBMYLEHAhxpHlfZd8hqjjBxKOXPWHZ6RXu5pGM4paHeoTdAPGC_E4xmzEHVYOnWmgb8AbqxvBsvax2sRDhrNz-QPkR46W5nBwvvIWG5zRR3B-MRKcSHs-L9UnSXU6Ez8YJPJZ7V6Qtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ: از اینکه ایران پهپاد شلیک کرده اصلا راضی نیستم!
خبرنگار: شما گفتید که ایران آتش‌بس را نقض کرده. آیا این کار عواقبی برای آن‌ها خواهد داشت؟
ترامپ: خب، به‌زودی متوجه خواهید شد.
خبرنگار: آیا آتش‌بس همچنان برقرار خواهد ماند؟
ترامپ: از اینکه دیروز شلیک کردند، اصلاً راضی نیستم. در واقع ۴ شلیک انجام شد که ما ۳ تای آن‌ را ساقط کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/66892" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66891">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
صداوسیما: صدای چند انفجار در سیریک شنیده شده
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66891" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66890">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
🚨
🚨
🚨
گزارش ها از انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66890" target="_blank">📅 23:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d178038cac.mp4?token=SXd7vHoSR3yb47GJxiPQaVwOvsxlnsGh06tTVZ7FHJF_6g88tfsVxPjejwM2vKK3E3qwvFxMLXFeLbJOHO8mwfjD0jhQsop6GptFG48QsH-Sgj1G_OL3rTqrhcVNATxAmqFHkdkPXwGrzothL9iGihCjE9_l9Ql3fNb9FhobsAJIQt-lrBF7KlcMl-XWujqU6lWEmb_WyiT_OI-okGrf5tgnqFLjdUhSIK6X7QHQ_HE7Y5HXBVKziDMlkLp4Iv2iYLr3w0Ck2e8D9ROZXYf9Zjje-Sp0X0IgFvV9lpKNaRLQ3Y76vZP5--5OZhHj9zBNwhjwIvzAutJLjv9fwWDf3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d178038cac.mp4?token=SXd7vHoSR3yb47GJxiPQaVwOvsxlnsGh06tTVZ7FHJF_6g88tfsVxPjejwM2vKK3E3qwvFxMLXFeLbJOHO8mwfjD0jhQsop6GptFG48QsH-Sgj1G_OL3rTqrhcVNATxAmqFHkdkPXwGrzothL9iGihCjE9_l9Ql3fNb9FhobsAJIQt-lrBF7KlcMl-XWujqU6lWEmb_WyiT_OI-okGrf5tgnqFLjdUhSIK6X7QHQ_HE7Y5HXBVKziDMlkLp4Iv2iYLr3w0Ck2e8D9ROZXYf9Zjje-Sp0X0IgFvV9lpKNaRLQ3Y76vZP5--5OZhHj9zBNwhjwIvzAutJLjv9fwWDf3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر مسکن و توسعه شهری ایالات متحده، اسکات ترنر:
خداوند تنها دو جنس آفرید، مرد و زن.
و زمان آن رسیده است که این حقیقت را یک‌بار برای همیشه در کشورمان تثبیت کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/66888" target="_blank">📅 23:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXw0mL0-HeMB5HN2zoFL7gf-O8lGJDJrK9vYZV_xUeeZGN57i0nAbN-M3NpxNKMDit3Y-h0dNm5CEbpmp49QOIl4MvwzZrPNY342ZRqfhko1UVPgEyh_omEWPqlgFbDBJQu5_OCVbt_lfJnVBAax8iVL2nM1eTx5el3tt3Z2oZUMmkmGs0PetXXof6-Y9RYcdH5WtMej1vKhE-Sk7Rj4tAsF3eddGC_Bn-SG6Sjb6er5AkF-DVl6w9hRs3cMYj3A8qDHuZAnBD6tE2O6wFY89RA_ErArN-rWQ9Nt4nsV_YQSBiJw0aG7S8hshyUOVNuve3lq3wvQ8nPFz9GdBg-xKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66887" target="_blank">📅 23:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=uKOPwYn2JUJnQ-5fnXbwPbLD5tXUZEd_G_0AXGjDGpbji4trum1xLGPRrnVxjlJ36yfMakPD0qLsHuwM-VwxVI1XE6L41jYBshSn3jLfuDv2UCnB7mVT8x0zcL3-dkdUVN-97mfewrFEMh26O79oEydpu_SR_gY0abfQpuEqrTYe-z66fdN5rUgRCTb8V9nckHUh1Rq9jgB5d1ySnGVQ-xMNp_ZUAn6hj7FgQJmUnoKFDLjkcRZHee0W0uPOUASiDrPbXvv3Z3yjOta5r-SuHq2t68F1sMB6fK2vS1GQyRN7LNboPMubPMXpVCUF-2w9ujm_oMQuNseaD_UNEOgPgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4fe545d1f.mp4?token=uKOPwYn2JUJnQ-5fnXbwPbLD5tXUZEd_G_0AXGjDGpbji4trum1xLGPRrnVxjlJ36yfMakPD0qLsHuwM-VwxVI1XE6L41jYBshSn3jLfuDv2UCnB7mVT8x0zcL3-dkdUVN-97mfewrFEMh26O79oEydpu_SR_gY0abfQpuEqrTYe-z66fdN5rUgRCTb8V9nckHUh1Rq9jgB5d1ySnGVQ-xMNp_ZUAn6hj7FgQJmUnoKFDLjkcRZHee0W0uPOUASiDrPbXvv3Z3yjOta5r-SuHq2t68F1sMB6fK2vS1GQyRN7LNboPMubPMXpVCUF-2w9ujm_oMQuNseaD_UNEOgPgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ:
کشته شدن سلیمانی یکی از بزرگترین اتفاقاتی بود که تاکنون در خاورمیانه رخ داده است.فکر می‌کنم خامنه ای و دیگران در ایران از کشتن سلیمانی توسط من خوشحال بودند.
چون آنها هم از او می‌ترسیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66886" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66885" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NToiJD1eVSSdU2tkxESqG39AP6wixh76RCOcytE-UFOU0TADlXE17Ak-37IK4EQTNelnhhew7mXJVx7SQgQDFRMkw4uxVR7UiWGFHT4xxmjFPVNvLoLkehIiwQw3OfDfGR1XmfVedc_KFRHKIcmzKCwOXsNFwNhm7XxdGiHoE34DvhOlWYvrHY3GtNIgSzYBaKgDlkOIDEXX8Dh93x36E-7L8BOEnGLlDGz1j2lrH1yuRQAlTxUUS_aDL3K6inVK9YwY5l8TeQjI8qKfiRgPRWTiCAVBQOe4sh5vihleezRyjDvFxj7WUCeqs-TJYr_gb2gOedta2Y27SlQHKraZdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
رئیس کمیسیون امنیت ملی:
به سران شورای همکاری خلیج فارس هشدار می‌دهیم، قمار بر سناریوی آمریکا، ثبات و امنیت شما را بر باد خواهد داد.
دیدید که پایگاه‌های نظامی آمریکا در کشورهای‌تان چگونه به جای تامین امنیت، به منبع تهدید بدل شد.
قدرت موشکی، پهپادی و همچنین مدیریت تنگه هرمز، خط قرمز جدی ایران است.
تنها راه تامین امنیت منطقه، فاصله گرفتن از امریکاست.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66884" target="_blank">📅 22:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=gPOmYgqRFtC8rBn9gLX5fVx66aFw2cTA3wlcmQWOUjg9DsQT6KPrES-Qg9uAhRYIonQR_Cw3_b8u3rCPTctraQ6yvS--xP8Cx4YgUXkI1voIC4DU0IxTSjML_xBkVJhFpX0wedj8sYtUmEdqWZ-kL3Qq5mIPYAYasH9T6wdnRl8IE7fT_QI3QX7Q-e-9BTQZohMv6ZkyzpCBQcf1rm5-Tlq5djXY4DnifiRUbdwGUkB9MNzU2Ek4CV0hGZ6Evn_SYSlhPDstbZIh45R1u-8UuxaNCsH3lqpIdQ-lLjbVyE31btQ6h7JmR1Wal8Q7Coyr-GF0kqxB-aetWX3OCqh0HA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bda20ad94.mp4?token=gPOmYgqRFtC8rBn9gLX5fVx66aFw2cTA3wlcmQWOUjg9DsQT6KPrES-Qg9uAhRYIonQR_Cw3_b8u3rCPTctraQ6yvS--xP8Cx4YgUXkI1voIC4DU0IxTSjML_xBkVJhFpX0wedj8sYtUmEdqWZ-kL3Qq5mIPYAYasH9T6wdnRl8IE7fT_QI3QX7Q-e-9BTQZohMv6ZkyzpCBQcf1rm5-Tlq5djXY4DnifiRUbdwGUkB9MNzU2Ek4CV0hGZ6Evn_SYSlhPDstbZIh45R1u-8UuxaNCsH3lqpIdQ-lLjbVyE31btQ6h7JmR1Wal8Q7Coyr-GF0kqxB-aetWX3OCqh0HA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
‏نخست وزیر نتانیاهو: اسرائیل تا زمانی که حزب‌الله خلع سلاح نشود از لبنان عقب نشینی نخواهد کرد.
🔴
«شهروندان اسرائیل، پیش از آغاز شَبّات می‌خواهم خبر یک دستاورد بزرگ برای کشور اسرائیل را به شما بدهم. همان‌طور که می‌دانید، ما در واشنگتن مذاکراتی میان نمایندگان اسرائیل، لبنان و ایالات متحده در جریان داشتیم. این مذاکرات طولانی بود و امروز به نتیجه رسید.
🔴
مهم‌ترین نکته این است که اسرائیل در درجه اول در منطقهٔ امنیتی جنوب لبنان باقی می‌ماند. این یک دستاورد بزرگ است و تا زمانی که حزب‌الله خلع سلاح نشده باشد و تا وقتی که خطری متوجه کشور اسرائیل باشد، این وضعیت را حفظ خواهیم کرد.
🔴
این همچنین ضربه‌ای بزرگ به ایران است. ایران تلاش می‌کند با زور ما را وادار به عقب‌نشینی از جنوب لبنان کند. اما در واقع اسرائیل، لبنان و ایالات متحده به آن‌ها می‌گویند: این موضوع به شما ربطی ندارد. شما هیچ نقشی در لبنان ندارید؛ نه شما، نه حزب‌الله و نه هیچ سازمان تروریستی دیگری.
🔴
نکتهٔ دیگر این است که ما به ارتش لبنان اجازه می‌دهیم تا سازماندهی خود را برای در اختیار گرفتن برخی مناطق آغاز کند. ما دو منطقهٔ آزمایشی (پایلوت) ایجاد می‌کنیم که هر دو به توصیهٔ ارتش اسرائیل هستند. یکی از آن‌ها اصلاً خارج از منطقهٔ امنیتی و در جنوب رود لیتانی قرار دارد و دیگری در شمال رود لیتانی است؛ بخش کوچکی از آن در منطقهٔ امنیتی گسترش‌یافته‌ای قرار دارد که طی دو هفتهٔ گذشته به دست آورده‌ایم و ارتش اسرائیل به آن نیازی ندارد؛ ارتش این موضوع را کاملاً صریح اعلام کرده است.
🔴
ما همچنان منطقهٔ امنیتی اصلی را که خارج از برد موشک‌های ضدتانک قرار دارد حفظ می‌کنیم. اجازه نمی‌دهیم نه حزب‌الله و نه غیرنظامیان وارد آن شوند. این وضعیت حفظ خواهد شد. و مهم‌تر از همه، اسرائیل می‌گوید: امنیت ما بالاتر از هر چیز دیگری است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/66883" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdEluqVyXk-6uGklNG4F-1UvnIcF-ICFcnlqzT7QgLxUXoJMxL63w3GAfzpUhXvwQ7DYgH1BxD9SBPhpTgeCG6ax0E45kDQOkHw7EPOyIU-tbe_3OyQsMgw7jHCDPUdhpk9tnL6t5GBlhbKZhde31GLGIMJ2RRs9HaMPb7Bb2033KG0T6vGbdq6ljNmBKy15oW9XJy0Da1FROA9EZWEQoTzDLS5Egel7LNs-98eTv8CzXaG2yLNJ24D6TsTm4u4y13oPjmKCVb00C83oMq_fJrpVanwpg0qvMelKayYw0oQXDJtJyz2vju-PMRMVKeCbEr3oG-uP6OKInt9IRnMNUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
اتاق جنگ اسرائیل:
اسرائیل و لبنان به تازگی در واشنگتن دی سی توافقنامه‌ای را امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66882" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‼️
🇱🇧
حزب‌الله تصرف تپه «علی‌الطاهر» توسط نیروهای ارتش اسرائیل در جنوب لبنان را تکذیب کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66881" target="_blank">📅 21:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9BmMUPakqnzCDRtlpaAwbOof5utTjWQdrf3zhgc1k2NV_YYJMLvEXWJjpQxQVN1CBehS6M4-Tk0W_zJSujd_GhUZgNVxbuLNuOWcVl52baH5stvHmYxcSe8ZLbOpm4V-9zsrYc7HnSblPDFj2psf73znYFAWy6M9cIJeUNG3e1ZW4FfC-5NmlS8J98Up7s9wsSMELEZzme-eY94UdZEi-O3Xc0bhv6Nd14k9EAoTqHdcQlZwFeS9izCJ55QJdYZQJEXUPaz__f_Fp7GhhmWRLEpbl0jq7Mwi7YFCtOAGMbUyx9Np6XtEKb8FqSDP9ENqlYJZmPAd6yqoNGOco85aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید اکسیوس:
مقامات اسرائیلی و لبنانی به من می‌گویند که انتظار دارند پس از چهار روز مذاکره در واشنگتن، امروز توافقی کلی بین دو دولت اعلام شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66880" target="_blank">📅 20:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66878">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USh3fpfyzVSFUfkaOw7AMu94KnIRPmE2pqWuHpXHx0LrRDLmzLKg1LCOURaC3FtgAHUtnhWF4crp53adeCJlXLw_rwMvPMjDYE3agmZTvEdcd2eGNv8WxvtmJJE7EZ37rjitAWCTLkZE6pvpVqZh5cnHYkG2cKhXXfxjiaXjaJOPIzPx-oRBKNKpNuYmxD6k9mNrRBgkVvY7ZQ5SM3foQKCzGX8hZizULi_JoPNl80WK1AF2AqixTlygMu3V9t01q46LjlaQGxFko1kR3PQocNJYXHiTQl5jVL-HKbSemBrfxJncPZ2Ncn_nZO9qtv12thbVASrnpd3N1-MwsXAXoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OkrN5_2HUBabXiC9CWt7jKKC0kEj8CmH93caMwFyedUuxh94mAh_KwQCqm53YpLMgvlYs_dftG1uUx5_prhwNCvt6QAlICb-U0ZSjp_JHwCcs8Ky8WKs8CXq43BBnPFdUawMiACwv_3NSAI7_yShz_tZNWLqqoPSmDzdTW-F4fDJVZFErBLMqTWWNdvBH00WcUDMx6aGct5Z2FBdnlk9i4T_n_bC1Vhb86mOH5cIP_y_i_b5uzS4mJt-NeiMVsPgWDpaL_NF-QcifGC3GWXU10kMduw9S4WsazdyUIWm7gnHzYHry1pMZxvu178LlJJiRJcM6benyWOj1d_M2ltZlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
در فاصله چند ساعت مانده تا آغاز بازی حساس جمهوری اسلامی و مصر رژه‌‌ی همجنسگرایان در شهر سیاتل آمریکا آغاز شد!!
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66878" target="_blank">📅 20:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66877">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lu8_b53VvXTs7inV-S5eMxWv4z1M9LFDrhZyT6Z8tlgPPdTlM8guJAAevyrrffaYnYMNvt5semf2RIonoH8vp6d4rc8D6mAZdk1WC4-YznvMJCJ938SEZ1D1eRWBYQ_NcgqPKx7sspggqiQ_EJ6n1Fqkb2aVO_eA-qQzICuUhH8CBlr_GMOxF3pbhG6fPFZTeh8WYE1UOCCg8qyOh87_q0p5cp-Ky6wDqvadE-JJhX-49B5OuSWNHzMAhQYkqLhDAsnuSiWJognj7bHi8Ohq8Ap_6NE0cSkM0DfvUaoFwNA7yrBmvZ6eaNaxyF2LkTb8GLo5IEu12UZ_vsYLFDGcog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ: ایران حداقل چهار پهپاد حمله یک‌طرفه را به کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد.
خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد. ما سه پهپاد دیگر را سرنگون کردیم.
بدیهی است که این نقض احمقانه توافق آتش‌بس ما است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66877" target="_blank">📅 19:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66876">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYM_iDbD10aB52A_H1rs7JbnkwWY0Nr4fCH2T8w2WNlr-39ioo9-aYLp5pIcUEvkLFBeedRbx3IhI51F9x-z02RUK69Tq1TdOrSSt40VmPNun8cnsFVqsWTrF6fmx99iSqkmFJc0IeGbuVeqRBG-MwUwaLII9Pv3gAGc3gRFWvxkqAC7C_rAWkSxNYdBOtTTtbebi84kv1QbDg20xlAals_iK0CjZc1ejwP04YGp3jKv55jBHTWqM0aAk9u7CjnohYXeZNue--bX0ag9A1LXjozvS8XIxr1oi6aaSGsB9jI-Yb4JIORriS46l1vu7x9EdzCsqllN5b9wYJp3x-yvkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بلومبرگ:عمان هشدار داد تنگه هرمز به شرایط پیش از جنگ باز نخواهد گشت، کشتی‌ها ممکن است مجبور به پرداخت عوارض عبور شوند
عمان به متحدان اروپایی خود هشدار داده است که تنگه هرمز به وضعیت پیشین خود قبل از جنگ باز نخواهد گشت، که این امر نشان‌دهنده احتمال اعمال عوارض عبور جدید برای کشتی‌ها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66876" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66875">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQKAmCj1PxWToQMFbTB6Go_tw9DAen5Ds1PZmT1hwUnBudd0k0WEMSSInqdI_WKKe2-kIji7cn7c53XceGSfVPW2ZBo3i60UrGGlIWjNr6EhZiIeAuZWYdeKaZsB3BqS8cqU4l4j-kkR6PtKLuCSlIx7xaCtfI7SgrQ5rw04OdSqlU4DExVAqF8ihl1FHpZed69bzVcSdfudBDqInozHZ2uIrU162Z7bB6QUgi5yjLyVoTH6dc21Frhvw0wisJUYxbfUbTphwaFwkXw_Se1sHLZEuSZvi2NTfZ93wXHFvmVpgMEzsgsWXrSHSO3uvkJ7QR4ZP2rQxM_pP_tukX4NBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😢
رونالدو تو جام جهانی گریه می‌کنه؟
پلی مارکت می‌گه ۶۵٪ بله. احتمالاً آخرین تورنمنت ملیشه و دوربین‌ها منتظرن. البته رونالدو رو که می‌شناسی، شاید حتی با قهرمانی هم گریه کنه!
قبل از اولین اشک رونالدو، پیش‌بینی‌ات رو توی 30 ثانیه روی پلی مارکت از تلگرام ثبتش کن
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66875" target="_blank">📅 19:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66874">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=jE3qaK2GlVtWyQlenZc5njsRAYY-q4b6EDSWUFzlYyxDc77ygSQLbmN5010dOY3JGl15nLr83zROkA8Q-nHxuc8w2lW0U-y4tF3R_v1axRMTPbxnYlT7KWQXoq_jJp-6yRybKX-E0g6LSZSHZY_PPdBvVgN9V9BEwEl0MXosnJyItMHiG4gpKGK1B9pG2yNlYGd-Ck_advhVjvLaWtweVVCBXZlqThnm4dZAhzLv5Eh2VvkrRlweJxuR8TqcWbhOZhbcnEEyzrJMyUMvP2vU6OooaOkKLjLtQUOl2JbRlIzLuhnksk1wUFkDl1pNscoL71ZABOZ5QtCb2iD_ZznjuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=jE3qaK2GlVtWyQlenZc5njsRAYY-q4b6EDSWUFzlYyxDc77ygSQLbmN5010dOY3JGl15nLr83zROkA8Q-nHxuc8w2lW0U-y4tF3R_v1axRMTPbxnYlT7KWQXoq_jJp-6yRybKX-E0g6LSZSHZY_PPdBvVgN9V9BEwEl0MXosnJyItMHiG4gpKGK1B9pG2yNlYGd-Ck_advhVjvLaWtweVVCBXZlqThnm4dZAhzLv5Eh2VvkrRlweJxuR8TqcWbhOZhbcnEEyzrJMyUMvP2vU6OooaOkKLjLtQUOl2JbRlIzLuhnksk1wUFkDl1pNscoL71ZABOZ5QtCb2iD_ZznjuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قاسمیان:
به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/66874" target="_blank">📅 18:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvL6zIDVUbzcEgSp3FJ3YQs9z0o_dXtwYGOkhlpw6reCmXg1F6Qm-HUTlzAH0RXQhOybCSqo1S6zh18W7zgcBFU-l71bUeAikmQ_37Hc-LFTk1X592IgDUISgwouu7v9Wga_bV3WmRpov2MSx57TXSeHhZ943kbmxfdccrzCjlItSjJDujuo-WeqIzD6J9kFapCzb--WlCHDKT_APUp815tD1sMIDtflzLlIOgRB7T8l2_-X4C73ZFoDLBtwCQmVTngIBZwZH3KCiMvmJ4h7qHnOKhyTIZl802Yi4l1jov9CxVl1PJNDBcYa_b-ZBAyIbqs6d-3pa2tQDIO0Ot3j7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇱
توییت کاتز وزیر جنگ اسرائیل که قالیباف و عراقچی و پزشکیان رو تگ کرده:
فرمانده نیروی قدس، قاآنی، این روزها مدام اسرائیل را تهدید می‌کند.
به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحکِ تهدید به او می‌آید.
در هر صورت اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.
نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان، هیچ‌‌چیز ما را متوقف نخواهند کرد.
نیروهای ما آماده‌اند تا کار را به پایان برسانند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66873" target="_blank">📅 18:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=c1a1RVfBy3BXU_9B-gjNYw-2W9BCObh7w8ZvBAyVmavcNc4Cce56awrQxORX5WqtxMHADtLMDsBT9LLlLcvhwaeJwdlEzDgOKEnQCF8N-fiGzNh5cvo_krZp1Rdm-kLYnUzp2tO0LiNP-JgbA3ZU0SJS4YyzK7LiSRkC2H3WwhKGBj9GD3sqsSQfNJkF2jON43UP9GLn_DKjS_9Hb6xazVyUq10_0K_WEBgMrefRSh0oLFC8aRT2frV1cj77U4oZDtalqnDDf2V4rFWn4FznCB6TeLu3f3rt3yR1cgVWZRgW_u_95Cn6uAy-NomMIVgWyfsUxUkqUt5s2awqJJgqZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9a88d77cf.mp4?token=c1a1RVfBy3BXU_9B-gjNYw-2W9BCObh7w8ZvBAyVmavcNc4Cce56awrQxORX5WqtxMHADtLMDsBT9LLlLcvhwaeJwdlEzDgOKEnQCF8N-fiGzNh5cvo_krZp1Rdm-kLYnUzp2tO0LiNP-JgbA3ZU0SJS4YyzK7LiSRkC2H3WwhKGBj9GD3sqsSQfNJkF2jON43UP9GLn_DKjS_9Hb6xazVyUq10_0K_WEBgMrefRSh0oLFC8aRT2frV1cj77U4oZDtalqnDDf2V4rFWn4FznCB6TeLu3f3rt3yR1cgVWZRgW_u_95Cn6uAy-NomMIVgWyfsUxUkqUt5s2awqJJgqZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای وایرال شده‌ی یه آخوند تو یکی از هیئتای مملکت :
حضرت آدم دید هر عضوی از بدنش به درد یه کاری میخوره که یهو یه نگاه به وسط پاش کرد دید یه تکه گوشت اون وسط اضافه اس٬ گفت این دیگه چیه؟ هرچی دست بهش مالید دید اضافس بدرد نمیخوره؛
حضرت آدم خنجر یمنی رو کشید که کیر خودشو قطع کنه که یه دفعه حضرت حوا ظاهر شد گفت آی آدم چرا میخوای بیچاره‌مون کنی که یه دفعه آدم دید کیرش راست شد؛ بعد با خودش گفت این مال کس دیگه ایه٬ این تو اختیار ما نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66872" target="_blank">📅 17:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66870">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dcl4JkJiceVnwG7LICQ-HPRBDGI1zOJgkHpdQkrcSBdLW1UpgfqWKaxd0tyXB8X_9Ryjg7GJZfSHhxhDG-3NCAbtenILXvGm-OAPQdfLCfGyckOeXm4L2vj5wpLGoDaW5EMGeuEgdEIlWVW--iwpjhGoUuigf9sDvA83IFMYOle8aAm6GbBJusAqOwLZs3_5j6BfQ1ohBdQ9fRnjTFl5QHUxkAKSEC4VpUTrPUAtgjBuFqs5h_O0JQ1rx4CnTvzs_lXVd5XBQGKCKgYRcxuENqsOX4DUIJ6_RzU5oDshCzJn1vcXK4R1NnmZbJLfE0hsaTm0HzWKb281ikJw2WHyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B2f0_yUEqlWiyv5l996s-b4wkpwHTwLPuOIhcyf0-NEyig-LntEjAR0ZrTISzqD1jFYVda3hv3L9BtxeKQ9_1Sx-QxKpsrF4rIV_GWoJnRvBzaptwTvwnZdeR2FQQkPodCNSIuM45m_129Iml01uEkmsnAvruhQcXiCk4iXoxrYCSp0fm7hFojn1TsuTU1rMuZORVJ20D1QjCyOYDLRlB8UK8wU97_aCeHWixalfg_AANbWWGHhwQFCYnZYipgMy7CwMPNCfYxzs84BXWLHC4guzvzq3NgiHtxv3QOwx_X_QGfgcIh-Odi1FhdlYYryc_cwChQsKxJbIrgj4IPUeyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
‏
بر اساس تصاویر ماهواره‌ای که روزنامه وال‌استریت ژورنال تحلیل کرده، حملات موشکی و پهپادی ایران خسارات گسترده‌ای به پایگاه نیروی دریایی آمریکا در بحرین، از جمله مقر ناوگان پنجم، تأسیسات ارتباطی، انبارها و ساختمان‌های پشتیبانی وارد کرده است .
با وجود اینکه پنتاگون اعلام کرده عملیات ادامه داشته و تلفات انسانی ناچیز بوده، این حملات آسیب‌پذیری قابل‌توجه پایگاه‌های آمریکا در خلیج فارس را آشکار کرده و موجب بازنگری گسترده در آرایش نظامی ایالات متحده در منطقه شده.
مقام‌های آمریکایی در حال بررسی انتقال یا بازطراحی تأسیسات کلیدی به نقاطی دورتر از برد موشک‌های ایران هستند. گزینه‌های مورد بررسی شامل پراکنده‌سازی نیروها، تقویت استحکامات پایگاه‌ها و گسترش استقرار در مکان‌هایی مانند اسرائیل است.
برآورد می‌شود هزینه بازسازی خسارات واردشده به پایگاه بحرین حدود ۴۰۰ میلیون دلار باشد و مجموع خسارات واردشده به پایگاه‌های آمریکا در منطقه از ۲ میلیارد دلار فراتر رود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/66870" target="_blank">📅 16:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66869">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=aPTMhMMuw215Qfuzg4sBQBf5kivbJNOMh3xFeEoa9NfI72q4dxCXc7EbQZ9hmsZeCvKXMIP3VSItYuOy4RBu6lEYcFam6YK4gTE201ZV221lnyCRRKxnWUZjSpbezTJcaKFNUG-5Wo0z0sVN8bKbLAoFJMYmI-rCGAwDe-QpQeoYQYde8dH_6Tlsn4dn6KreBsvgiV15FbSWQdHgGGO7NfmnqC_Bs6uku_SGWnFrP1I-iX63einZM8nSNqAcx86ZAzfFejF6-o1vJea-t3Z4fZFXPjpjKLGmGmpO2ULCF8_q7s4FCQmkvYCohlePdTHX_E6WERznqL1ImnakQzkYqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60f93beda6.mp4?token=aPTMhMMuw215Qfuzg4sBQBf5kivbJNOMh3xFeEoa9NfI72q4dxCXc7EbQZ9hmsZeCvKXMIP3VSItYuOy4RBu6lEYcFam6YK4gTE201ZV221lnyCRRKxnWUZjSpbezTJcaKFNUG-5Wo0z0sVN8bKbLAoFJMYmI-rCGAwDe-QpQeoYQYde8dH_6Tlsn4dn6KreBsvgiV15FbSWQdHgGGO7NfmnqC_Bs6uku_SGWnFrP1I-iX63einZM8nSNqAcx86ZAzfFejF6-o1vJea-t3Z4fZFXPjpjKLGmGmpO2ULCF8_q7s4FCQmkvYCohlePdTHX_E6WERznqL1ImnakQzkYqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟥
فاکس نیوز:
دبیر کل ناتو  فاش کرده در جنگ اخیر فقط ۵۰۰ جنگنده آمریکایی از مبدا ایتالیا به سمت ایران پرواز کرده اند؛
«اگر ایتالیا را به‌عنوان مثال در نظر بگیرید، ۵۰۰ جنگنده آمریکایی از پایگاه‌های آمریکا در ایتالیا برای پشتیبانی از عملیات “Epic Fury” به پرواز درآمدند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/66869" target="_blank">📅 16:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66868">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=mpDK6Qxe-wua40GZhl0CBEPnUDpg--KcMvKAEuX-3o-a6vIor2ERmZ16wG2oVSOuatc-4ZfJgRrzcF-DDFFSLobHpP8ivM08JSr-bZ1BgyISc72BKtDTnVEYNRhFpNG3O9hCO1xCDAF6rVqhjNRBbejImc0uos1z48O2zhMSNicdzzI_K0oVWtbUqjE6xw0Pbi61d7WcDr46-O9UsM8gJLHYqgnkvSP7Iw6lHT5SycwAO4o9NJULn2xz9x29d6du1hMeZQ0JWM_h7qkCLhYnvCCUB89mA6bO1WdjUC6LxpRoG0sVqL8LLkNo6GlejWNbEuowvyTOeIUp2cziajhbNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/403bcac56e.mp4?token=mpDK6Qxe-wua40GZhl0CBEPnUDpg--KcMvKAEuX-3o-a6vIor2ERmZ16wG2oVSOuatc-4ZfJgRrzcF-DDFFSLobHpP8ivM08JSr-bZ1BgyISc72BKtDTnVEYNRhFpNG3O9hCO1xCDAF6rVqhjNRBbejImc0uos1z48O2zhMSNicdzzI_K0oVWtbUqjE6xw0Pbi61d7WcDr46-O9UsM8gJLHYqgnkvSP7Iw6lHT5SycwAO4o9NJULn2xz9x29d6du1hMeZQ0JWM_h7qkCLhYnvCCUB89mA6bO1WdjUC6LxpRoG0sVqL8LLkNo6GlejWNbEuowvyTOeIUp2cziajhbNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پاسخ سخنگوی وزارت خارجه به دست ندادن تیم مذاکره کننده با ونس با شعر مولانا:
چون بسی ابلیس آدم روی هست
پس به هر دستی نشاید داد دست
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/66868" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66867">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66867" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66867" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66866">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mqATysasm6HeU0klLoWDKiCyDZrc2ZDKXFqkpM-beJQ-CJA8b7iPZstD8Y2lUACCn-xVM5TGcwOAwfqTALA0hpRH6D8mcooAAaX2ilRkYQgwDp4YrZkqoXCogg3b1AubB5IAiPbjd4uojDyiyvo0yPUZ1g7P0GJdLCipaE0QexH8-V3H_vJNiwXBUxwFCp4qtiWlj_v4ATmKaFcY47iCZ1iA0vRBytXO3A7VvqmGnVL1v5ux0-LeVI6RKtmvNUqaBobjzC1kQ-XDROWuGT8PPJYUqt8Zu4_fiBf-2MtqrgOrrH8GFTx3TkNQdO_0lh5uGjBgNvBcDALvfKv45rubdRYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=mqATysasm6HeU0klLoWDKiCyDZrc2ZDKXFqkpM-beJQ-CJA8b7iPZstD8Y2lUACCn-xVM5TGcwOAwfqTALA0hpRH6D8mcooAAaX2ilRkYQgwDp4YrZkqoXCogg3b1AubB5IAiPbjd4uojDyiyvo0yPUZ1g7P0GJdLCipaE0QexH8-V3H_vJNiwXBUxwFCp4qtiWlj_v4ATmKaFcY47iCZ1iA0vRBytXO3A7VvqmGnVL1v5ux0-LeVI6RKtmvNUqaBobjzC1kQ-XDROWuGT8PPJYUqt8Zu4_fiBf-2MtqrgOrrH8GFTx3TkNQdO_0lh5uGjBgNvBcDALvfKv45rubdRYlmh7KTb2JExap6Ary2h6OgDi9cOLhfFbX6akGhqUX-nGjkR2wsrSyTI5NNnvXSoB6OiJvPBJQVdfK8fhin1GCknuRQcmtXBnkd9xtehz0iVnfVvFrTjRlatyIPfDAzrk4sknmVHtcg1i1esYNv_um5bvmWli5SKrnEPvkj1Xyc58xDAC0lFhxuqtf5x_2oiDIYRMaNBet_TgQ-6m4WHvRKPNZLyDcwquVN0jWLl4Sf_rGwJHmudoETsg6sC5pFX-VwPLk8i9MkAYbU-VRImgb4q55xwuQJN1l1Gull0VKm-wp2wnZDwjre_qLGYgbZppJ9D7lmOVGz60KM4JbDUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66866" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66864">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BseZ0nZ3p9TkNtPMD04fpE-KRqUsKYGqdp4aqFo1gY6gbuNXVlFccR_YpOPU5UtDdPukafoYtbZJ80N9heQfO04CIQi2o6Gnr1VH6BX7pum2D5U5hieXt3v48SkXrGKNXR6I6sLCc4UTZVIwBYLqCeFhx8edGf9KBMqQOfffaJWtCt9qcdD6N54dxiNpAWUpPd4eE-f2VDFMrpdmVjn2e6m1ekShBGhf63N9prjXt6lmxIA80aJvWGP3VLZyCzaaTcuA_Q7kaqefVA3V4hYiuo05IGVRrqKfm7DUwi9bjVeXgix3IaA4XBh6wI6XPTwXrJtldw5ZYFV-QOrQxvCjFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K4AgxFUzb0om7Lcp5fMJxubFIDPTHspHG1urwLZwccq_YM2OVs9dZuWUueIxiTYfhbXSHCkdkd0cAyDpKLON-mOmDKjRyW8l40tkjgTxFO3pJA7JzsrXMKxm4zIs2zAUdUrcjpQDThVC_1P7-tCUWcxkMtBFDBEock6R0liNV2gfZ8NnkVGACbROoh9qCUMUqYPi2YprNUMrouMOySvexqLH0c_FXPems9TlptD6YCox8xGj-JzorR-EkFIgn4EwfUns4SnumoznUIe1DnWexXLrIJ_mKz4FHnIcU98QSG_tQSeM5ZREfotxKSPu2Da0-KNWRzZAh0fenk9KedAEMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a41ee6c687.mp4?token=K4AgxFUzb0om7Lcp5fMJxubFIDPTHspHG1urwLZwccq_YM2OVs9dZuWUueIxiTYfhbXSHCkdkd0cAyDpKLON-mOmDKjRyW8l40tkjgTxFO3pJA7JzsrXMKxm4zIs2zAUdUrcjpQDThVC_1P7-tCUWcxkMtBFDBEock6R0liNV2gfZ8NnkVGACbROoh9qCUMUqYPi2YprNUMrouMOySvexqLH0c_FXPems9TlptD6YCox8xGj-JzorR-EkFIgn4EwfUns4SnumoznUIe1DnWexXLrIJ_mKz4FHnIcU98QSG_tQSeM5ZREfotxKSPu2Da0-KNWRzZAh0fenk9KedAEMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانه‌های لبنانی گزارش می‌دهند که یک پهپاد ارتش اسرائیل، اعلامیه‌هایی را بر فراز شهر منصوری در جنوب لبنان، نزدیک صور، رها کرده است.
روی این اعلامیه‌ها نوشته شده است: «منطقه خطر! دور بمانید! هرگونه نزدیک شدن به نیروهای ارتش اسرائیل شما را در معرض خطر قرار می‌دهد.»
هنوز تأیید فوری از سوی ارتش اسرائیل وجود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/66864" target="_blank">📅 15:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66863">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=DNUzF_OngSFaj8WNgqSmrIJZYIz1AoP20-OxE2qFfVWjiQaoJHsXe-oc42RTe08yEfpfq4tX9KXWUdKsUDPoaD6gUJQNCmFeZzEWLHQRFLlSThhgdkH7oeKIk9hG-DQJg0D6nl5TUPlPumkuMR7DMF8xI_WDGFHJpEv5yol_OJ3Ey-5-eJkGbX0OWgWoacQXrKOZvLE4eefxvSeVosh0x89I2SVzK2SbAHWdtE69ASelHYGnc-Fh4eZZoYcPebYg53j5KxAPmRjwg4c09rlNq1gfOy-0w_IeNz3i8fub2KelT64XfUJH6rLxKDuf-8FHt5EO_i4X3e5JssmcB8LyoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22157b34b4.mp4?token=DNUzF_OngSFaj8WNgqSmrIJZYIz1AoP20-OxE2qFfVWjiQaoJHsXe-oc42RTe08yEfpfq4tX9KXWUdKsUDPoaD6gUJQNCmFeZzEWLHQRFLlSThhgdkH7oeKIk9hG-DQJg0D6nl5TUPlPumkuMR7DMF8xI_WDGFHJpEv5yol_OJ3Ey-5-eJkGbX0OWgWoacQXrKOZvLE4eefxvSeVosh0x89I2SVzK2SbAHWdtE69ASelHYGnc-Fh4eZZoYcPebYg53j5KxAPmRjwg4c09rlNq1gfOy-0w_IeNz3i8fub2KelT64XfUJH6rLxKDuf-8FHt5EO_i4X3e5JssmcB8LyoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ترامپ:
اکثر مردم نمی‌دانند که حرف B در کلمه dumb وجود دارد
😢
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66863" target="_blank">📅 14:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66862">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">⚠️
خبرگزاری فوق معتبر فارس:
درب تاسیسات فردو، نطنز و اصفهان به روی بازرسان آژانس تا زمان رسیدن به توافق نهایی بسته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66862" target="_blank">📅 14:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66861">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=AlJ9J8gFTX0TobUy8ppBKHv9IUev4NHQNdDZ9QXLAMx1cgaSa2uPbJCGRyBAeLs2a-TIQgoddKBW47KAdXfd0gcCm9vVdXxaqEuLN_3cxRR6EOZvvIn_lnLSYKgJwtYMutvCylXLng9--LNVKB79I11qb8gqT6ao92gB1QUmZT2MuQhpzX2D8McMa-51ejHeA0OXbD_6IVvN26uycN6xhawCTG7W7TL2XPdHDQKDRe7Xu0t0nNoW1g6NxH_3sFKcIApz9P9F5RPvKyIY65UAARE9h-7OqDJWJqDDRPXEhb3RKX5da-tEO-PLIgri1cOi18-mN9DE2AJ9CTXHn44hbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=AlJ9J8gFTX0TobUy8ppBKHv9IUev4NHQNdDZ9QXLAMx1cgaSa2uPbJCGRyBAeLs2a-TIQgoddKBW47KAdXfd0gcCm9vVdXxaqEuLN_3cxRR6EOZvvIn_lnLSYKgJwtYMutvCylXLng9--LNVKB79I11qb8gqT6ao92gB1QUmZT2MuQhpzX2D8McMa-51ejHeA0OXbD_6IVvN26uycN6xhawCTG7W7TL2XPdHDQKDRe7Xu0t0nNoW1g6NxH_3sFKcIApz9P9F5RPvKyIY65UAARE9h-7OqDJWJqDDRPXEhb3RKX5da-tEO-PLIgri1cOi18-mN9DE2AJ9CTXHn44hbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسمای محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66861" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66860">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❌
قرارگاه مرکزی خاتم الانبیا:
🔴
پرواز هواپیماهای نظامی اسرائیل در نزدیکی حریم هوایی ایران یک تهدید مستقیم محسوب می‌شود و اگر ایالات متحده اسرائیل را مهار نکند، ایران این تهدیدها را تحمل نخواهد کرد و حق پاسخ را برای خود محفوظ می‌داند
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/66860" target="_blank">📅 13:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66857">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0_ioG5zAeBGgLrc2W_nGJNAU-78QsH29rxZQFM-rJbvB5xSzscssvy93-omqRNd2TwNMDQfs90GbC_ufRpMEPoyCQ2Et9khuQNE2zGNgHRTKl8po-X8E9AiPwghg1yqrjhZAFhBKM5MKljb2nSlWeck6kqWTHDXbaAdQfrJk9LIiSjTRdRf5VhvgevV9Ex_TOusORgmS_GXYs0UioNtDLxl-iqlBqMi48d_FPj9lea0k1ac18YjA2nM8__F7btIE0Wx6aAfjbNWQqO-9vYkqouZ2Si2uWJuDXBhtqJxpyoLSau80FV7OciyH7o1HgVKK48svx3rtB8X44B-XWnTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AcSOwYZcODeJBMJdYJNb9a79t3g_TSOJStQprZ6JYb4Z4XLaw_5jkx06FHxzFdXJBuoHvSgjpIMoPvTzlN8xpiL_2HP7yYLPnLEkAwcu44s5RQichhGBNUrdhzO_MCQriOYaTVzmmOCSsl29fuONJFL-jjdXxGDmycm7t8EhDvisa_s2M76P1tz79HuAhWAl16LdJwGkcqOYV7XlyqYmQ1xF5Ga9xLlghL5xjbEl2Qp1nDYAkwG4NRa0ECJ55MUB14mALF6KZe1WBdRYHL2pKFZYo59vHRUrqCm4bY9j_t7JfIvWBWWzcdSTJsx0qVRqlw_qwzoUMtWk9xxWDNe-Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UIRd61cEh-n2bgdAmCFUUE1KnWfC_eLKGmzAa68XlrD_ZlNGH8joUG98mWJZBwteajqsV6Tp61HvR_jxwgKogAmXuqokzvH1QUBgwYuexcz9DG_boFMuRCZ48d94elNYVz4o4yZFgDaY2I6qvxr8Jsjk4YNqldG4mGiiU7i7_mTGv2k6iqMMqfLNKpC2b2HTIaz7E4lZtHRlTMo3GEXLuH1LtCk1wsF5ii2uN4jA6KIxYLwrRkkQTGQn11qlbq9vtD6S0BWXXiIA7h-pWQyJcA4cyXuyyArbe-vsYRFUb4xfA1_-MHMFH1amdg5iTQRtwUwg2khBDSmAaUwhWzbNLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
حملات هوایی صبح امروز ارتش اسرائیل به جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66857" target="_blank">📅 12:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66856">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=mYtItfXxaDouADxn-i_nHR8GpAn1zWr1Fp9Lf-jLc3XgwKN70zyiJEJazom7MJ5JwSTtQYfuwGsiegBx2VppPnXdfRLXFc0lLeaVURrGCEML2FpP07mJJ76mAAfrhmGGlCHZ-MKz4sgXl6nZsHZ2DC57D0RVhUWMw6nX8mcI0CqSqOZXterb8YGSkVpHYZ2_Fz9ACJChTcMnG_oFTuK2j0gndc75TkHRY9gV_D0Tf2AtyxbzN1-AhXUf8yUPcSWBmhmKDJTlCZZMr8K3lAKSoBvp6Kvx-JLXPai5j4oRK4MPMsjUm0QGXE7wiZtRHVdgnrgy0ya4v1YA-O0qp-7ALg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67fdc892f6.mp4?token=mYtItfXxaDouADxn-i_nHR8GpAn1zWr1Fp9Lf-jLc3XgwKN70zyiJEJazom7MJ5JwSTtQYfuwGsiegBx2VppPnXdfRLXFc0lLeaVURrGCEML2FpP07mJJ76mAAfrhmGGlCHZ-MKz4sgXl6nZsHZ2DC57D0RVhUWMw6nX8mcI0CqSqOZXterb8YGSkVpHYZ2_Fz9ACJChTcMnG_oFTuK2j0gndc75TkHRY9gV_D0Tf2AtyxbzN1-AhXUf8yUPcSWBmhmKDJTlCZZMr8K3lAKSoBvp6Kvx-JLXPai5j4oRK4MPMsjUm0QGXE7wiZtRHVdgnrgy0ya4v1YA-O0qp-7ALg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ درباره ایران:
«یک بازار جدید دیگر هم در راه داریم و آن، کشور دوست‌داشتنی ایران است.
ایران کشور زیبایی است. کسی دوست دارد به آنجا برود؟ جمهوری اسلامی ایران با مشکل تأمین مواد غذایی روبه‌رو است و ما قرار است بخشی از پول آن‌ها را بگیریم و آن را خرج کنیم. همچنین قرار است مقدار زیادی گندم، سویا و ذرت خریداری کنیم و این روند به‌زودی آغاز خواهد شد.
این برنامه هم بسیار بزرگ خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66856" target="_blank">📅 12:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66855">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqOOkg3WAjv_YmAaDUkW2JXEv5eddQNBFaeTJwV-wqtctZw9zOAIri5eBh3ra6h9p5x7aSvEctGErx6jyTY6HTQEOaccPSxm7CInU6gZ841z7KkQIxQf-H85ny_XVH6rtERjZNpuI4U48BoLQTX2Ea4QKFgFplh3k4RhXpe2Ayu-dVfVyfi7j9tmGt7IXYqwCmMr64PFY--vGNXKXX2meF68wpwI5s__OJi4Zi-BbSONKc9_qUrfd7gNdoprY1ljCWR39J01Fem8fmd27isKlPxDk6Hlkx8-mW0mwl4ftkEzFeYtIDIM2tQvMTXDAAtQUwcF5EsbyvC_1G00unl6gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
پرزیدنت ترامپ:
روند خرید محصولات کشاورزی ایران از ما خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/66855" target="_blank">📅 11:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66854">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
جی‌دی ونس درمورد ایران:
🔴
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
🔴
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
🔴
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
🔴
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
🔴
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
🔴
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66854" target="_blank">📅 10:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66853">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=kt-FOEv8Xp5243p5V5k9TOVbAz1SsO9QAitVg3Dd3RcEzgMgpHUF67oodDtiuyah7WKZEXRnaD5n3rYnBzXbhnV7l7gYnK918YhzgiEE4WEU3cvXaOs3GONGp3RTiooUqq9dGVQOAJzVnWmwAyHj8UxxL-2BJfc8FYhmCcHP-UcH6xW_8p_Q_N0gv2gAcgEUmbqAqVDC_1lGypHxve8KXR4MDkY_bEl0rfkL35ivBELvXhQLk8lfbOhljWDR_91WEYv5lHQbJ6ObBJwvQ_wP4nF7K5KfYOmnt1Gu41u0CuW-YTqxbiqZS43PIqOW9qX8XvNab3tLtEPrwWpEtti-cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aefac4ff7d.mp4?token=kt-FOEv8Xp5243p5V5k9TOVbAz1SsO9QAitVg3Dd3RcEzgMgpHUF67oodDtiuyah7WKZEXRnaD5n3rYnBzXbhnV7l7gYnK918YhzgiEE4WEU3cvXaOs3GONGp3RTiooUqq9dGVQOAJzVnWmwAyHj8UxxL-2BJfc8FYhmCcHP-UcH6xW_8p_Q_N0gv2gAcgEUmbqAqVDC_1lGypHxve8KXR4MDkY_bEl0rfkL35ivBELvXhQLk8lfbOhljWDR_91WEYv5lHQbJ6ObBJwvQ_wP4nF7K5KfYOmnt1Gu41u0CuW-YTqxbiqZS43PIqOW9qX8XvNab3tLtEPrwWpEtti-cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎯
ارتش اسرائیل: ۶ عضو حزب‌الله را در جنوب لبنان ترور کردیم!
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66853" target="_blank">📅 10:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66851">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=N6Dv0AoZ3x_s2kMtwrn_VV95SJAhDbVFc69QVF34GqBRnebpzKfeIz-5Wfmo77ScL6DIxeYEWGaFuJ-YuIB5IVfKb5v4mcJaP0x-ux9Yzp4UctDbKhtkcQjw8fgjcdEB3GxKh42guutK73khDHvII8beLUsoOITVcKTvsh3v6O5BJAZVOH-34nE0n75xX9cFuVsA1DnbrllMzkfPakmbO5_E_8F4K7G320tJgyVWe2gPcPw33eWMCcQ3Gz_klhCwa7nehUUQCb6NnGQNxEzoS0eSDD5juRTriOWz4jugQiPD-Zc6p9HhRhIOF3f0v8Hbc7vWSe0j7727mHY_G9j2Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73a731d25b.mp4?token=N6Dv0AoZ3x_s2kMtwrn_VV95SJAhDbVFc69QVF34GqBRnebpzKfeIz-5Wfmo77ScL6DIxeYEWGaFuJ-YuIB5IVfKb5v4mcJaP0x-ux9Yzp4UctDbKhtkcQjw8fgjcdEB3GxKh42guutK73khDHvII8beLUsoOITVcKTvsh3v6O5BJAZVOH-34nE0n75xX9cFuVsA1DnbrllMzkfPakmbO5_E_8F4K7G320tJgyVWe2gPcPw33eWMCcQ3Gz_klhCwa7nehUUQCb6NnGQNxEzoS0eSDD5juRTriOWz4jugQiPD-Zc6p9HhRhIOF3f0v8Hbc7vWSe0j7727mHY_G9j2Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قالیباف با روسری و ماسک اومده بوده هیئت
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66851" target="_blank">📅 09:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66850">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=v_UJGwgddGV156_azMLd9VaLyuZDGWG3ZR_RuFiY7v6T-ISzUmlkBcQtxBy3vmCDrNxZ3JIpyATxva5JETnS-ildEvERB3d-RuzOnEubBWlj60sZLthTQU8WCyEvSvTS6puthLBmgsnSXj8sziWZ0naDo9romT-2vjwkASkzoYnEKG8n_m2x1z1BtPpBGetPu-csPN2wo7oUSrgAspppasB1HnV3gI3k6qIsNA-MjiBdAKJoLSu-wrLoRq5aCvtALEdiHNeCwIbfaP2L6QgJRB7gWxxyLwje8Ov1wdhcgO58VebPWgm-VFCvjtrJTuij1VDt0zylKzBNg_bSw8pXLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff13197ee.mp4?token=v_UJGwgddGV156_azMLd9VaLyuZDGWG3ZR_RuFiY7v6T-ISzUmlkBcQtxBy3vmCDrNxZ3JIpyATxva5JETnS-ildEvERB3d-RuzOnEubBWlj60sZLthTQU8WCyEvSvTS6puthLBmgsnSXj8sziWZ0naDo9romT-2vjwkASkzoYnEKG8n_m2x1z1BtPpBGetPu-csPN2wo7oUSrgAspppasB1HnV3gI3k6qIsNA-MjiBdAKJoLSu-wrLoRq5aCvtALEdiHNeCwIbfaP2L6QgJRB7gWxxyLwje8Ov1wdhcgO58VebPWgm-VFCvjtrJTuij1VDt0zylKzBNg_bSw8pXLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرماندهی مرکزی ایالات متحده:
جت‌های جنگنده اف-۳۵ بر روی ناو هواپیمابر یو‌اس‌اس تریپولی  (LHA 7)، ناو پرچمدار گروه آماده آبی-خاکی تریپولی/یگان سی و یکم اعزامی تفنگداران دریایی، در حال برخاستن و فرود هستند. ملوانان و تفنگداران دریایی ایالات متحده در دریای عرب در حال عملیات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/66850" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66849">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال @Palang_Bet شو چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی @Palang_Bet     @Palang_Bet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66849" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66848">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guEOXjAySzpO51HYFiXRyQs1bsqrEKhOCfH1-ypCWbyKGWbK66nF2TUEII99H6yYKmJHgqmUm2zMqccpxLc_1iX1tmxN3b-sp1hH2k186ov5WEPlfQrhV91ZMXP5nC2Z9Gz_X5SNf0S3nxw5oB2RwPxbu_hEy6ggJ9G7Sczrz8Tq8gryyhcvOeS_kKAPxPl65l630cH55TC1BuMLBBt8L1jl5Pni6chBA-S-cvyAqjf6l6WogtaQt3QU3MFPvMqS33TZ-MvBHau6_kxjR6cE6F02KDiTRt9pm5gYGvH45v_JmAAiuwPEVm_vfLbTkRUSgyAfr_9CWHEZemrq3ON7kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
@Palang_Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
@Palang_Bet
@Palang_Bet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66848" target="_blank">📅 02:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66847">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbv67rbbBdVt_9Vl7lmYUtVEzc7ql_iBc_ISzK-aOnELaoZipRSFcP-iaOqGnAoJFXvDFoIqtt4_2P3mOHsIqjWA2st3yKe6qTvAia1O0WGS0-owGAUjIdgTBCCX4K3tsM7tv2OhonJlnSaEjLAE_7LGmsbbH7CJqL-Slov81Pa3-L58JjbV3pc3A2H6aEvhINOBtAXnaaHXP_LsQbOXkTdk4ZyoB37HXF72yUyLj27ZpsadVYH_QTLlgpdvZMNhdSs01bkxGMpUuNVlBYWXAnzVXixNgddf-5zQKBEuevwmyVehu-vE3zyVBK2st-cQWxcWxLVsrOjs46oXXDDVeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏بر اساس گزارش وال‌استریت ژورنال (WSJ):
🔴
ایران روز پنج‌شنبه به یک کشتی باری با پرچم سنگاپور در تنگه هرمز حمله کرد؛ اقدامی که به‌عنوان آزمونی برای توافق هفته گذشته میان آمریکا و ایران جهت بازگشایی این مسیر حیاتی کشتیرانی تلقی می‌شود.
این حمله به پل فرماندهی کشتی آسیب زد، اما هیچ تلفات جانی در پی نداشت.
این حادثه چند ساعت پس از آن رخ داد که ایران به کشتی‌ها هشدار داده بود از مسیرهایی که مورد تأییدش نیست استفاده نکنند
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66847" target="_blank">📅 01:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66846">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رسانه های اسرائیلی اعلام کردند طی درگیری ارتش اسرائیل و نیروهای حزب الله در منطقه بیت یاحون در جنوب لبنان چند نفر از سربازان ارتش اسرائیل از تیپ ۷۶۹ مجروح شده و با بالگرد از منطقه تخلیه شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/66846" target="_blank">📅 00:57 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66845">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">با بحرانی تر شدن وضعیت ونزوئلا و مفقود شدن بیش از پنجاه هزار نفر گویا به نظر می‌رسد مثل زلزله سال ۲۰۱۰ هائیتی که ایالات متحده آمریکا به این کشور نیروی امدادی/نظامی ارسال کرد دولت ترامپ هم به سمت همچین سناریویی پیش می‌رود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/66845" target="_blank">📅 00:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66844">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
وقتی نت ملی بود ، تنها سرویسی که برامون قطع نشد همین بود
🔥
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66844" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66843">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giVL5FY0B4teXZP1C9-PKdF6ILuZ6eQPAN9HMVVovOFITowhS_BkVRUFDvFS5bBsbItgfXzEzkMhfA5Eg8FLIfRpHTQ7WI44AKjhIw182os2yzK3vTCsgeQxsfF88udD7hQnPRzCUf2AVYKs-duc9tgjXQLC5H-1FT2dAqZVuVvTZIdlTnLjuBupDCfPBDfCiZy6mCuZq_Wk8Oo5cQ9PQsDenWlIbitn73sGGwIulbSREMZ5Fm9xZiOz_EVMm6VUH6jUv3hv94qyS888mxDUzxCoLw81atQuTgcDcQuQuoMLGIz2tQTcNp8z1uD3MJWOKzzYqAdDJDRrzyhclbOlqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
کانفینگ نامحدود برای همه اپراتورها
🔥
⚡
سرعت بالا | بدون قطعی | تحویل آنی
💵
یک‌ماهه: 380
❗️
پشتیبانی 24 ساعته واقعی
❗️
✅
سازگار با تمام خطوط
🚀
اگه سرعت مهمه، همین الان پیام بده
🔗
@Kaviani_Vpn
🔗
@Kaviani_Vpn</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66843" target="_blank">📅 00:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66842">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6p1dzZe35pz9CJfq8RXESPjncfbQ-kTY3-6EknCD2_ZeZsv9uwAUyUZ6S-HXYumuukYeBGWgxFQwqeRcouB6Fgb_NbeIKxYV12bFA8ZHI0byL7C4jx_Y2zmewrMqwIjow2ebQ50xHjfAzsMbQbAhzXpMdN7DcbQR-PbAnB_sylK1D-URsYidtKChVhWYswsm5AFkdumcpD5pt1K0kQfvGfC88udBgJ__ymODV1iRpCP7oZqeXX5SdWbS42ikxkJ8Qbb36lPzEtlrOhaDDhB6Cs08SYmi-tH_NwbKdokszQHcO6e5Phf-Qpwfn76jHX7TYVYMsTBdqcBTgyvqny1xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
گزارش از لبنان: جت‌های اسرائیلی به بیت یانون در جنوب لبنان حمله کردند.
این پس از تهدید امروز سپاه پاسداران علیه اسرائیل صورت می‌گیرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/66842" target="_blank">📅 00:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66841">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=IkawKeYM_M47ZroOv0AoSP7sMgdYU5TX8Mb7o1_vEjb7WqoI22AyPE-tuDlXKrHVxbvm90OeKWRqXOjrss0QMIcEieYETTfi8dVPGBM_J8xCCQIH6g1XS4kkSCTSIA4VbjvE56_FMmJbXC7Ivlj5_mMMcD-_nVClvcfRnSVCCt2Ic6FxrDOPXLSs5bTeaBHOxZVpWvH67c59SyE2-wTcY9AbizunsQEwQtXmNJlv957nGQeidzGxKEMDe2FZ0yt95pddvuz37-p4O8Eg0a8_5svnKbJMHdb0an6Fn8B6nXM3s5HtQ1S8dgFryLgaamcr9Mboeuo_wqkeclEfRh09hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b6d00bedd.mp4?token=IkawKeYM_M47ZroOv0AoSP7sMgdYU5TX8Mb7o1_vEjb7WqoI22AyPE-tuDlXKrHVxbvm90OeKWRqXOjrss0QMIcEieYETTfi8dVPGBM_J8xCCQIH6g1XS4kkSCTSIA4VbjvE56_FMmJbXC7Ivlj5_mMMcD-_nVClvcfRnSVCCt2Ic6FxrDOPXLSs5bTeaBHOxZVpWvH67c59SyE2-wTcY9AbizunsQEwQtXmNJlv957nGQeidzGxKEMDe2FZ0yt95pddvuz37-p4O8Eg0a8_5svnKbJMHdb0an6Fn8B6nXM3s5HtQ1S8dgFryLgaamcr9Mboeuo_wqkeclEfRh09hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار:
«شما قبلاً آن‌ها را «دیوانه‌های دین‌سالار مذهبی» می‌نامیدید. آیا هنوز هم فکر می‌کنید این توصیف دربارهٔ رهبری کنونی هم صدق می‌کند؟»
🔴
مارکو روبیو، وزیر امور خارجه ایالات متحده:
«ببینید، موضوع این نیست که من باور دارم این‌طور است؛ واقعیت همین است. نظام ایران توسط روحانیون، یعنی روحانیون تندرو، اداره می‌شود. همیشه هم همین بوده است... البته در بخش‌های سیاسی حکومتشان هم افرادی هستند که ظاهراً انعطاف‌پذیرترند یا تمایل بیشتری برای همکاری با ما دارند. ما در حال مذاکره با همان افراد هستیم. باید ببینیم نتیجه چه خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/66841" target="_blank">📅 00:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66840">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/345e633380.mp4?token=Bv68xH0yxnCatqehXtHyCZKfCkJBUOIP6Gr-EhirsG1-vF169slxAka0DXvp7z4c2z8ZkL_EZmdRf5ZmLCWj2INg6BaRX4cm_XH1NqOdBwFZgFMKUx4YxITUJ-BuDF3L0gfW3fjoODtPgQq1sEwr2QrKkTbZY0XlA87mGdIH3eZr_3_cUTFKoeELK0HYtl1hGj91-A04r8H_NOC-DgN57QAGAa2Z0lUSZC41svaEU9SlNVr6K3DhxIYlV5dExIvXLntamUnooR_Vhkc9AW4SXEaLNxfR2kW8-fRosJJxYaKdkgorLID1T_gNfTwge8benc1WJekIBFE5_rTtauGPoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/345e633380.mp4?token=Bv68xH0yxnCatqehXtHyCZKfCkJBUOIP6Gr-EhirsG1-vF169slxAka0DXvp7z4c2z8ZkL_EZmdRf5ZmLCWj2INg6BaRX4cm_XH1NqOdBwFZgFMKUx4YxITUJ-BuDF3L0gfW3fjoODtPgQq1sEwr2QrKkTbZY0XlA87mGdIH3eZr_3_cUTFKoeELK0HYtl1hGj91-A04r8H_NOC-DgN57QAGAa2Z0lUSZC41svaEU9SlNVr6K3DhxIYlV5dExIvXLntamUnooR_Vhkc9AW4SXEaLNxfR2kW8-fRosJJxYaKdkgorLID1T_gNfTwge8benc1WJekIBFE5_rTtauGPoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری:‏بهای بسیار سنگینی.
رئیس‌جمهور ترامپ این جنگ را آغاز کرد،
و وعده‌های بزرگی دربارهٔ تغییر رژیم داد
و وعده‌های بزرگی به مردم ایران داد.
آیا ازنحوه‌ای که آن را به پایان رسانده،ناامید شده‌اید؟
شاهزاده رضا پهلوی:خب، نمی‌دانم هنوز تمام شده یا نه.چون همان‌طور که می‌دانید، هر چند ساعت یک‌بار ما یک توییت متفاوت از این
رئیس‌جمهور دریافت می‌کنیم و ناگهان موضع
از یک چیز به چیز دیگر تغییر می‌کند.
بنابراین من خیلی به هیچ اظهارنظری
که مطرح شده، وزن نمی‌دهم.
و در واقع، من فقط، می‌دانید،
کمی دنبال می‌کردم که
در به‌صورت زنده چه می‌گذشت.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66840" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66839">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">#فوتبال جام جهانی فوتبال
📊
2 گل آلمان و ساحل عاج  کد:YXA6P ضریب:2.3
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
➖
دانلود برنامه ملبت @Palang_bet</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66839" target="_blank">📅 00:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66838">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=vr3FMq6cQlkpciFE5MqRcVYoy6DfnNkaBTxedImDnJKj886kC0g4AbO5-NXCjG82cf6nUVNcFcXEnQN4uCH_dFuosDvBxhUQb8L02LfghjpwXbeCDLWLpHoBxN12JHGz8TZCraAKokntrvtaXdphvATsCEMtw_jTnJOEifEZov4MEwBQqr167s0H8xobV0EgTVAuWFJllXvp1q5AQe_-ByPrCtq--jvA6ipVj8tNcnYdeH-knJe_AIYc9ZWPN98JiZub2XJCYLrCn0VLLbDJ0sHofPb4d9u0iMF97X_-Ap5YfZa-MpQtCigqmhbnYcXRi7G-t0QTaVSQhHPntu6gtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f455bc9393.mp4?token=vr3FMq6cQlkpciFE5MqRcVYoy6DfnNkaBTxedImDnJKj886kC0g4AbO5-NXCjG82cf6nUVNcFcXEnQN4uCH_dFuosDvBxhUQb8L02LfghjpwXbeCDLWLpHoBxN12JHGz8TZCraAKokntrvtaXdphvATsCEMtw_jTnJOEifEZov4MEwBQqr167s0H8xobV0EgTVAuWFJllXvp1q5AQe_-ByPrCtq--jvA6ipVj8tNcnYdeH-knJe_AIYc9ZWPN98JiZub2XJCYLrCn0VLLbDJ0sHofPb4d9u0iMF97X_-Ap5YfZa-MpQtCigqmhbnYcXRi7G-t0QTaVSQhHPntu6gtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مفقود شدن بیش از ۲۱ هزار نفر در پی زلزله‌های ویرانگر ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66838" target="_blank">📅 23:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66837">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VM00YvtiYFzLrhYw9vExRKxQhH5qTtsqBVd9C9tDWDtYwpSt1TNxQwXJJ6OasfwuBVIRoUyx9Butmw8D9PncahPnUHeZ14tzoIppiSZeOHARaKs1C0JkVmurNT5xKcqKub2dqlLExjMPAM4so09xqv8qVswU0PPbKWR29s_xnxmqXkXUiE-PQsFdPNa-FQIiwdIpPenQRPQuj0YzHMON7oKHuQtBx0kLhX0EtYhCWUn99abCy1tJUqRNorzntfe3jHUiTGnKgwRjJzs_9E70NZ_nZDypTxN-hB8x3F8MuPlDX_w3wVkqOiovk_k2kLb77rmx1PBpP9r5h6yJ4ehwPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
پس از بیانیه مشترک اخیر در مسقط، تماس تلفنی سازنده‌ای با وزیر امور خارجه عمان داشتیم. ما مجدداً تأکید کردیم که ایران و عمان «برای تعریف مدیریت آینده و خدمات دریایی در تنگه هرمز» گفتگو خواهند کرد. ما مصمم هستیم و این کار را با همسایگان خود انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/66837" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66836">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=mEnYLcaMCwAFI6pF4eTMGvE4ghYMngAZij_4R6iWncsQQTgKuiNbavdGi6-4hJeH2A5gVDC76qiz-chmfvIHFBRcjvK9UJ_VY2OlzupPA51UA_rXJ8r_210q0lNs-nDR9hWNk5N-FHa0c6fTHXkync4jb1RfGkMcmkdwQupLlYzywf9AjuLjoc0HDYKjVpIS4xGzy3DpbpdtuuMFdlbOMcChYCPRbUcyHSTt3T-6Vm9lD_ZseZL_3dfhOIC8VWlhzkJM9etmkz4B-787ATpRmgfl3uofWQDvplf9wzT1c54fMVuKN1LtWeB3lpJdWXaHiQdbpMlIGahsfDFHqu127w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eab5d7e42e.mp4?token=mEnYLcaMCwAFI6pF4eTMGvE4ghYMngAZij_4R6iWncsQQTgKuiNbavdGi6-4hJeH2A5gVDC76qiz-chmfvIHFBRcjvK9UJ_VY2OlzupPA51UA_rXJ8r_210q0lNs-nDR9hWNk5N-FHa0c6fTHXkync4jb1RfGkMcmkdwQupLlYzywf9AjuLjoc0HDYKjVpIS4xGzy3DpbpdtuuMFdlbOMcChYCPRbUcyHSTt3T-6Vm9lD_ZseZL_3dfhOIC8VWlhzkJM9etmkz4B-787ATpRmgfl3uofWQDvplf9wzT1c54fMVuKN1LtWeB3lpJdWXaHiQdbpMlIGahsfDFHqu127w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
روبیو درباره ایران:
ما می‌دانیم افرادی که هنوز در بالاترین سطوح آن حکومت حضور دارند، همان کسانی هستند که به همان ایدئولوژی و همان طرز فکری پایبندند که رهبران پیشین آن حکومت به آن باور داشتند.
نظام ایران همچنان توسط روحانیون تندرو رهبری می‌شود.
همیشه همین‌طور بوده و همچنان نیز همین‌طور است
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/66836" target="_blank">📅 22:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66835">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=UQ6Wjy0t9uIl9eP7dSNPS5d8d8TF0o9DhV0GUT8vm60fjJ8bL8yQzsaHdgfzR8TKgZHhMKjkKFRZOT8vyPhdndLTdIOGE6uYA1IfB8YKHvGfR2p2SoQovX0sUtqOs4OFcIrYSWzEDWG4XHfcHJYMpH3bAsD8MXNiHCRVQdtVmhnr-aA4LzeCZ0SoivIFTGTdewsLWBZeCpwrq_Uex4BQIaz4syvc5GG7v10f3qvICnyQ79DqLVekNBdcxoY9LkIdSdh63bM6ItVtCuMHGUdw5ak7LQ7JEgKvd1rtU-CGITk-tsVhmrfZzeB8dDQnXnizp3p9mf5DSyQHTAlV14LZPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=UQ6Wjy0t9uIl9eP7dSNPS5d8d8TF0o9DhV0GUT8vm60fjJ8bL8yQzsaHdgfzR8TKgZHhMKjkKFRZOT8vyPhdndLTdIOGE6uYA1IfB8YKHvGfR2p2SoQovX0sUtqOs4OFcIrYSWzEDWG4XHfcHJYMpH3bAsD8MXNiHCRVQdtVmhnr-aA4LzeCZ0SoivIFTGTdewsLWBZeCpwrq_Uex4BQIaz4syvc5GG7v10f3qvICnyQ79DqLVekNBdcxoY9LkIdSdh63bM6ItVtCuMHGUdw5ak7LQ7JEgKvd1rtU-CGITk-tsVhmrfZzeB8dDQnXnizp3p9mf5DSyQHTAlV14LZPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پزشکیان:
نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/66835" target="_blank">📅 21:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66834">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSnT9w5mne1gQfNesPx_OeEZuPy09n9Hp2aZeBIi0ykoiB0wQiTd24ol7JTgdkrr7Fqa9K9els6j55gQ6zWXw9VDmG_CPGP4JwhQA8fJnkuxPeI634546NI92ewXtqiWP22WQ-63E_OvDiJeAMLw_5hpzDhOnnbPUzBU--DSAtqjn6DgoEjIRCOLjxYBRa3d8NMaLc_qQxMF3UpDM9I6JO1TTbjguIOXieE6xg0KXU6T_dOIJBS1S5hILdRS1QulCml-A6q6tUOm9TuBJ0PV-6sbFv3fM4-zSQ7kVwf7WbySXPFvme9-YHEgfyRdXoVNJN7aePJOufaNzfJbRrGtFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه پایانی نشست مشترک شورای همکاری خلیج‌فارس و آمریکا:
🔴
تاکید بر اهمیت بازگشایی تنگه هرمز بدون محدودیت و بدون اخذ عوارض عبور.
🔴
تاکید این که هر گونه تجارت یا سرمایه گذاری با ایران باید به انجام تعهدات آن به موجب توافق منوط شود.
🔴
تاکید بر لزوم خلع سلاح همه گروه های مسلح در غزه.
🔴
تاکید بر ادامه حمایت از دولت سوریه در بازگرداندن خدمات، فراهم کردن زمینه های بازگشت داوطلبانه پناهندگان سوری و مبارزه با تروریسم.
🔴
مذاکرات لبنان نباید به نتایج دیگر نزاع ها مشروط شود
🔴
حملات متجاوزانه گروه های شبه نظامی مورد حمایت ایران در عراق علیه کشورهای خلیجی محکوم شده و از تلاش های دولت عراق برای حصر سلاح در اختیار دولت این کشور اعلام حمایت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/66834" target="_blank">📅 21:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66833">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/965348f417.mp4?token=kHNpqocULxXGjafzHORjcJU2cTQoRbOpn4oTpwmNh1hQ4xPNWNk-6vIup_Sl86sCSSPNElmR51FRdM2iY7cr8C_hg9YYD7G0bizYe7Z9A6uIKz-fWD-V-bnt6gnHu0C5-eN2Xxy_sKojVBe4wXb22vfiZI8Q7HW_hywjhCvBBoGaZZZQQvM1VPhRUcISGzKdUYThABV97gXcdi5F-58e97Ue9JOY3ED3VF_-8iR5NkP6F9gnmfBeC8XBG5sCzuJ5AJnX-yVkxqHkL0ujo3C3iumVLEimTNbvg0eDYcIHWa6CpxsqSUYBGJ_H2ka6qd_Zsuo886IQfI6NnsgBb948hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/965348f417.mp4?token=kHNpqocULxXGjafzHORjcJU2cTQoRbOpn4oTpwmNh1hQ4xPNWNk-6vIup_Sl86sCSSPNElmR51FRdM2iY7cr8C_hg9YYD7G0bizYe7Z9A6uIKz-fWD-V-bnt6gnHu0C5-eN2Xxy_sKojVBe4wXb22vfiZI8Q7HW_hywjhCvBBoGaZZZQQvM1VPhRUcISGzKdUYThABV97gXcdi5F-58e97Ue9JOY3ED3VF_-8iR5NkP6F9gnmfBeC8XBG5sCzuJ5AJnX-yVkxqHkL0ujo3C3iumVLEimTNbvg0eDYcIHWa6CpxsqSUYBGJ_H2ka6qd_Zsuo886IQfI6NnsgBb948hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو:
فقط یک آدم کور می‌گوید هیچ دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
من همه آنها را فهرست نکرده‌ام چون می‌خواهم شما را نجات دهم. شما اینجا زیر آفتاب سوزان ایستاده‌اید - فهرست کردن همه آنها زمان بسیار زیادی می‌برد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/66833" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66832">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQBFxZVPE5UoGAKWUzaMKlTp_6pJ6jSOmIuPHgyxkWGGJ3lXkMJaIuL6rpMvrg3t-OsolgZ8oJc-Hd7hoQkrqFXc7stn8bSkd0WLBW4eDtQYEW8MdDEsWeLgc8XDoZa6YyRvjihSOtLyXYoDiRtFLwkMS4LwfICqAKzZtgKZCXdv35u0aNJ5b9wWiKWlX1Lj2PZb8JEH5c08kY6kyuY0P9tfsDlzPvU_PWdgsFyHnGdDoKnAiRg1HMmZspoVglcpi0yBYbsKY-LZNVMLFPFI9UWm9PF154RIDHbrJM96ncmpsUFz_EJWY4CQBSRR6oJg05lwFtmA9pTLn3tV_THoiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
با نهایت تاسف از وقوع زلزله در ونزوئلا. مراتب تسلیت خود را به دولت و مردم ونزوئلا، به ویژه خانواده‌های قربانیان، ابراز می‌داریم و برای مجروحان آرزوی بهبودی سریع داریم. جمهوری اسلامی ایران با مردم ونزوئلا ابراز همبستگی می‌کند و آماده ارائه کمک‌های کامل است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/66832" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66831">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">این آمار فقط مال روز اول جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو پلنگ بت جویین شو بهت آموزش میدم چطور پول دربیاری و تا اخر جام جهانی سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet @palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66831" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66830">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6P3Hag_D4gPAjcoytQCN97Tqt3LW12wzI9jlLXuMKebe17mltiavfgPmJexxrtrr61ZGIBk0jMR9xUYtY7OavWUNEYviB_7K6gp6_P-jGx82XPgP51VEzuA_rV9GSVPHtPNN86W1DMosIamOJSXF78tDANucY8wo2dY5HVr_pDUylguedmKvIZYdD5IqjyQaqGXYEqu7Q1brKkSPSiQbEegTjmeuOfv8MXR3VeoQvEnYjMBkf4pTjVnmjTtlq43KAdJYgpzTte9ZOWk6sFZdjEm95DK54_bESitCOCRG1w5euoO5JrU58CBbUfx9feNL9Mvbjy5RNqxBwu9idooNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این آمار فقط مال روز اول
جام جهانیه
🔥
😤
میخوای از پیش بینی فوتبال پول در بیاری؟!
⚠️
تو
پلنگ بت
جویین شو
بهت آموزش میدم چطور پول دربیاری و تا اخر
جام جهانی
سود تپلی بکنی
❗️
اینجا میتونی روزانه درامد داشته باشی
💵
🔥
@palang_bet @palang_bet
@palang_bet @palang_bet</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/66830" target="_blank">📅 20:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66829">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=ZGzrMGzxiOHd0tJlFT-iHAWMbcHHKbZzXejDUNyWO79GBi-RLpegvMK8SX6ShQBq9chnMAz0rjhm0WOwHcab3LDXU6WnPL4BpzoDMHBbJVT2xSPrXZZ9XPusP1AfPFEyieX7YJJQpTFBNvPExyel8ERlSJ8iCrZLKMer5oc5pLyIdnCaukYFYNRr4TujRpY7Ggtmmq9SQGxmdqIk5lgMOEPNR8rWelcjpSXlqJNM5zUXOYdrlCf7jB5SO1t5TJ7jFvw8nE3zpes0IuS8E9elAJtZKQ-SIQgcqSrHvHcgGYobWrsIgyPGhjUjlYSI6kn2UNglJ1bJw7kWVJOZ_5oP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c8c286a22.mp4?token=ZGzrMGzxiOHd0tJlFT-iHAWMbcHHKbZzXejDUNyWO79GBi-RLpegvMK8SX6ShQBq9chnMAz0rjhm0WOwHcab3LDXU6WnPL4BpzoDMHBbJVT2xSPrXZZ9XPusP1AfPFEyieX7YJJQpTFBNvPExyel8ERlSJ8iCrZLKMer5oc5pLyIdnCaukYFYNRr4TujRpY7Ggtmmq9SQGxmdqIk5lgMOEPNR8rWelcjpSXlqJNM5zUXOYdrlCf7jB5SO1t5TJ7jFvw8nE3zpes0IuS8E9elAJtZKQ-SIQgcqSrHvHcgGYobWrsIgyPGhjUjlYSI6kn2UNglJ1bJw7kWVJOZ_5oP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
من ادعا نمی‌کنم که پیامبر هستم.
اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقهٔ ما ـ و به‌طور فزاینده در سراسر جهان ـ تعیین می‌کند:
قوی‌ها زنده می‌مانند.
برای ضعیف‌ها جایی وجود ندارد.
آن‌ها طعمه می‌شوند.
و از میان می‌روند
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/66829" target="_blank">📅 20:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66828">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=IEiPtaULFHQAIC350YvYPt6R5KFkHCKEodw4qTw_VXEmqPcH2A1JskdurFxRFLvr_ByvXAAyh1vxgwOaojKOCGnRRtdQmMZwzHjkHSLvRqE7OFZ7yNtmmjdydV9Q22VzYaHrrWyxKuzPsAccs6A5JOVodfnhJoNXADSjLbZikmOH20rPWX94214tVpoos0nRvoztCIBLJ6p0tBR2dAmeKIbiVcUTo_kAAmx3B18Uy12-vcD5o1yaR84tvwNI8hTDJEWATjDXR7YpIJKbK7g2gh91uCLcDUuJXpSX4zVRqqT4nGvnQ0-rRjIqLqKaUM79lMmzqf-Qs8mf7MTGR738xA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4c620ba.mp4?token=IEiPtaULFHQAIC350YvYPt6R5KFkHCKEodw4qTw_VXEmqPcH2A1JskdurFxRFLvr_ByvXAAyh1vxgwOaojKOCGnRRtdQmMZwzHjkHSLvRqE7OFZ7yNtmmjdydV9Q22VzYaHrrWyxKuzPsAccs6A5JOVodfnhJoNXADSjLbZikmOH20rPWX94214tVpoos0nRvoztCIBLJ6p0tBR2dAmeKIbiVcUTo_kAAmx3B18Uy12-vcD5o1yaR84tvwNI8hTDJEWATjDXR7YpIJKbK7g2gh91uCLcDUuJXpSX4zVRqqT4nGvnQ0-rRjIqLqKaUM79lMmzqf-Qs8mf7MTGR738xA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت. به هیچ وجه اجازه نخواهیم داد ایران بمب‌های هسته‌ای توسعه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/66828" target="_blank">📅 20:20 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
