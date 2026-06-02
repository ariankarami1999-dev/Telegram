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
<img src="https://cdn4.telesco.pe/file/ODlY8868Vc1bENeazxxYpXjdBdUGsMLwuS0XrzyVImHYtcj4yEkilP5ymy3ES7TdD9EHKzXC5N90Nx558M445Iu5uylHm4eI6QEFbyQWGnbtZhenF36IvwGZSKy08as9_sBKxlfCQjbdKY0zpb-EOQRnHFGPUAlJywFMwRZifCmewZ1IZYcmvWV6NYBiGTNoGCl07zgIZkY8UV72bEQY_0Za1STc8PX8n9Y4uL-_YuqfM-gk_q7yp-w8HGzWLyQrOkNXQ_ZVBSkwWFeFNij3xk6uC8xornvXh3zBlmNDL0Ite2CEfIqAlvj54hCtSveClKznu7LCOgb8drJVereXkw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 945K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-12 13:15:45</div>
<hr>

<div class="tg-post" id="msg-124422">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac51ef1b61.mp4?token=IxEXOcmcInO1BtCzpkxUDYwmzXCuBkNhZJbk-Rkq8hg3J4N89CA3VoXsmTIvTH3GXPIRSBCYTaGJg_I9e8O9e0sioMsdkO21s8VdMVTzdNjxQBdilRx3uW76fwYNhHWVAaes7_CWL1HsVSoecyme0f9Ase9LBRkE725zunHck8O1GwXs331Owh_H-pObZ_ni-B_DSsTRF-x6Q1flCml2uxPDuE_2im7mq8UXjUDuEwd5IftvHjhNf4VTwf1RjkJ6XSu4B4HrVaKFA2bTrQXaViS99XLVGzAngGas36X08iySnLG3taH5zns5zSxojb4clBjcUXS3rpr3uTnc7RlULg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac51ef1b61.mp4?token=IxEXOcmcInO1BtCzpkxUDYwmzXCuBkNhZJbk-Rkq8hg3J4N89CA3VoXsmTIvTH3GXPIRSBCYTaGJg_I9e8O9e0sioMsdkO21s8VdMVTzdNjxQBdilRx3uW76fwYNhHWVAaes7_CWL1HsVSoecyme0f9Ase9LBRkE725zunHck8O1GwXs331Owh_H-pObZ_ni-B_DSsTRF-x6Q1flCml2uxPDuE_2im7mq8UXjUDuEwd5IftvHjhNf4VTwf1RjkJ6XSu4B4HrVaKFA2bTrQXaViS99XLVGzAngGas36X08iySnLG3taH5zns5zSxojb4clBjcUXS3rpr3uTnc7RlULg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جنگنده اف-۱۶ اوکراینی در حال سرنگونی موشک کروز روسی Kh-101 در ارتفاع پایین، احتمالاً با استفاده از موشک AIM-9 سایدوایندر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/alonews/124422" target="_blank">📅 13:12 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124421">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/159f752950.mp4?token=m1K4VVPpWT6tXz5Ex84Paf4T0L1jJhdMe82ELrDzJtTHKilOlJyN6bMG2bMeRMw4qyn8OPIuGcQr8dk3fNgfRAIwWUh7l3wcYc7K0ICnjU_QlLz51uEIxHulcQNRsVzrA5IkcUTFk33c1zdn4pDDuZ7HzuHrl3RquO3M3HSPYlD5Nn26JjrZGBaHIBIEam6KlN0Q-QHUGQFZKRBuEaAbOVHbtIJnve_m4exVr_PmWGa_H5vsVrFllGUZLWWR9FIeE5Tov7YgJuuFE9rc3rbk_x-LP5aRDRhVYgFGdA8O2LQViVTK751fnxQyQVHcdYA5yYsb0K_K86MCVDp9IDVkRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/159f752950.mp4?token=m1K4VVPpWT6tXz5Ex84Paf4T0L1jJhdMe82ELrDzJtTHKilOlJyN6bMG2bMeRMw4qyn8OPIuGcQr8dk3fNgfRAIwWUh7l3wcYc7K0ICnjU_QlLz51uEIxHulcQNRsVzrA5IkcUTFk33c1zdn4pDDuZ7HzuHrl3RquO3M3HSPYlD5Nn26JjrZGBaHIBIEam6KlN0Q-QHUGQFZKRBuEaAbOVHbtIJnve_m4exVr_PmWGa_H5vsVrFllGUZLWWR9FIeE5Tov7YgJuuFE9rc3rbk_x-LP5aRDRhVYgFGdA8O2LQViVTK751fnxQyQVHcdYA5yYsb0K_K86MCVDp9IDVkRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو کالا‌ف‌ دیوتی‌طور از درگیری تن به تن نیروهای ارتش اسرائیل با نیروهای حزب‌الله
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/alonews/124421" target="_blank">📅 13:09 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124420">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AzefnOFmBf2Q7Ei80aFO7aKBc418i_sfxqcd6id29eEo8_NyqAcxA8LOg3KeR9uDoR27wagkVgSWgKeXaU6q2RmjJI5o9QUzDHLpof66-oOYtbR7-gb37RVTlSRfIoU0pNOju_cFzsdew8ivsVvCt0Xj6Nk1DsufaAr6P4sH-J_HVMe3jkI_YxnA9x4Io_o3u9TFV3jhXI7QsWph94jeJ9crT7UV1ePNLPOUtCNJzWrP9PQw3Pu0aPpkuQBAp4ZE9BDhG8Du_FQyZjS5gbkQyXfiA521fhEcqEnnIacBDQ8pmub7ipJdWP4NfFb9deJrdQ_VQUZ7hh6Vq27o3LhNww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سخنگوی ارتش اسرائیل برای نبطیه در جنوب لبنان اخطار تخلیه صادر کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/124420" target="_blank">📅 13:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124419">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
روابط عمومی سپاه: در پی حمله ارتش امریکا به کشتی ایرانی  " لیان استار"  در محدوده دریای عمان،  نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی  "msc. sariska" با مالکیت دشمن امریکایی / اسرائیلی را  با موشک کروز مورد هدف قرار داد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/alonews/124419" target="_blank">📅 13:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124418">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgbXsVMO5V4Rrt8ewo6CEE7D7nt0w2kyjKqvmRyWQf5NNKw9DGGmIh31v-jadAIV3LcRY0F-N1jx4_aWbePCgZbRbyLOssmxjSJUbajnA27ta9B82QV62SA2glvEWhH1NtMfw1TMyY81tbLnO1I0nSKWz5of49Rh28eVp-Xipi2yq7ubpMKMqC8ZqNj6vZE_TxA26jF84D_0O1fPVZ3r-NMkRGlaQKOZ4h-AXlecTKq6Cv7C6l7IBQcD51ups1Z9h1sAXl66UTu61z6r5fba13vTs6-_nAJvGcL4hlkavcwT5pbA9-sRJJpZ5yXr6gOzcuWzu2IOAIPVUPQLN8Xx8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گروه تروریستی داعش با انتشار این پوستر، تهدید به بمب‌گذاری در مسابقات جام جهانی آمریکا و ترور پاپ کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/124418" target="_blank">📅 12:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124417">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید 90 گیگ 100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!  @Netaazaadbot @NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/124417" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124416">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nR18q8Q3gwlpJaal7RZ8V-4vvfTARzxoOm2rD_IlHOhRY8MODHplanXlj1VtYKyl5EYULjN39wTutmmpOLSDXMGLASuxvLqyNHO4fNm0CB92GezlYyOkeIMajoW6wOpqJDhJnS_RYBFs3eNaz8UZMUiZzbPxmoILXAIt8xIOOgMfbPZTo_FdW4GGCSTzRgJ0z0O8N9L7jSEnO6aJieZiKHAz4DH5VyqT3Axp3qHDvnbuU4IvnFeErI_4H2KI7UxNrLkhADaCIqTi0Xn3-R41JkZl_D7YAKoWPv_U0afgS7YkmUPQqqVk6TmWjZdHcWM1z1uV_faFpa3ryVMTMZPqiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/alonews/124416" target="_blank">📅 12:53 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124415">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gz8MVO1tK_NnBcZN2zC5m8YW75tgOqSx_nZ3M753NWIe9KxCwzc8xSBGjdp-8VpMsORR0r7Xjxrw0L6vTCwqBSGHhjFA2S3REYJ-L-oqMqelGJl3sbIDtkZzbLCLwv46QbTm2UqVAG7BLFEDXBXKmhk2oJu0CUz6-9ybk_iXWAek2oSftuqH68y8sSwCNO-r0Voz-Do9B7BXXsPXr9KgLQpuWY515F9a8BuWFIyR0UfDKCY0IG-U6jLqB8futrEfo6K_dhDZ1IJ7ZMCDrqEHxEw-9AQd9067a3qUPwkIWspsFzeuMO6QG1sd5N84bY6UImXvfWq-KAkoeSyOMB7QUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تجمع اعتراضی دانش‌آموزان مقابل وزارت آموزش و پرورش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/alonews/124415" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124414">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/421e450ae9.mp4?token=uaXL4iBMmY-LGSVP2KL1nIx_XD2a2DEspYmnlXRfAti76bzeWweEwrjen3ETSrwhPMSGfcxhylsgsih7DNzEL57ziIxWGVWSlZEHjVGfllBEH2vV-fdwovcreeXdP0bidT5rCBYpNj6zf-rPmrN1BLqHdzAS-hVM742zDlyuNG-G-YZGDmgGZpuA8ZW9g211OqbZxQ27DHJOYplD8IevJivQM4-wD8Qzr_OZwxGDUdGgSDy4jnDHzBDNMODV7wwd3JL1Lpd0af9ter_0XXAOusy0QLEJbveqeCmOutlYYhPYePe5uBf8HULa4OX0Hhidw_Zw61k0greC27Aok-8Uvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/421e450ae9.mp4?token=uaXL4iBMmY-LGSVP2KL1nIx_XD2a2DEspYmnlXRfAti76bzeWweEwrjen3ETSrwhPMSGfcxhylsgsih7DNzEL57ziIxWGVWSlZEHjVGfllBEH2vV-fdwovcreeXdP0bidT5rCBYpNj6zf-rPmrN1BLqHdzAS-hVM742zDlyuNG-G-YZGDmgGZpuA8ZW9g211OqbZxQ27DHJOYplD8IevJivQM4-wD8Qzr_OZwxGDUdGgSDy4jnDHzBDNMODV7wwd3JL1Lpd0af9ter_0XXAOusy0QLEJbveqeCmOutlYYhPYePe5uBf8HULa4OX0Hhidw_Zw61k0greC27Aok-8Uvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع اعتراضی دانش‌آموزان(مینی تروریست‌ها) مقابل وزارت آموزش و پرورش: در شرایط جنگی چگونه درس می‌خواندیم؟/ «حداقل تاثیر قطعی معدل را بردارید»
🔴
گروهی از دانش‌آموزان صبح امروز سه‌شنبه ۱۲ خرداد ۱۴۰۵ با حضور مقابل ساختمان وزارت آموزش و پرورش، خواستار بازنگری در نحوه تاثیر سوابق تحصیلی در کنکور شدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/124414" target="_blank">📅 12:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124413">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
نیروی دریایی سپاه: در شبانه‌روز گذشته ۲۴ کشتی پس‌از دریافت مجوز با هماهنگی و تأمین امنیت نیروی دریایی سپاه از تنگهٔ هرمز عبور کردند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/alonews/124413" target="_blank">📅 12:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124412">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KwRPt08CKG7quBeYJzMcBHd_FYxbNZFGx22am1vZGQZS_kOJxeJOhlQcUvTFEm67J0DynwVbQ-53P33Lv2k72mDZWNxLkPab3XHNz1S_SU9TqvbWLXsQNaoQUhWdi3guS0klO07sblegEfRz6kdNbD4RA51ofsCHnyJelQMih2_zNINcw5_k3HVN_wG0_30ZoTrLK-prdBPNd-3PVkUTaW26prAg0ysZTvLB6ljLzEyLyT9QC0PMx4SfsJKVC2HWgIsLmjCXduOXomqUXGlazYidKfAqugCdoLCC4P3riGnJUJIWi--9OOnD7fxe5QzdT5JIXMgJ-OXlCVOnC8kglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۳.۰۶ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/alonews/124412" target="_blank">📅 12:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124411">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kq7iCWWnELuq2PR9IlxUE69GoTpwV-o8-N4Uk8Ymj_Td-HawDrZ-6kArSCh5ip8X-vlIUvtTUVPsPvkoQ5jABjVQ4rghXnuYZS-cfcZzvzy-d2taZHBNW8A4IDEfC-fSTnTe1K5Boce4uFVAhKz-3tvbdNpf8Xuh18uhIOYtYdxahvLQUsPEn2knkPSbp02FllzLHzC-z_zFvTGkd_rNZ096dH73tu1lPGgngHiNnXpmIHckv6fSF6PL9rsNtjpCq-ouAlhrrN2azMiBP-y8p6aES0xfbNhvFngR_Zhb6sabwtJRIOy8VTv4xEK4ZKc45X2758Ut8mWlDR2JmoHumA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایالات متحده بیش از پیش رویکرد بی‌طرفانه عمان در قبال تهران را خصمانه تلقی می‌کند و این کشور را تحت فشار قرار داده است تا با انتخاب یک طرف، روابط دیپلماتیک خود با ایران را قطع کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124411" target="_blank">📅 12:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124410">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
شب گذشته مناطق مختلف اوکراین هدف حملات روسیه با ۶۵۶ فروند پهپاد و ۷۳ تیر موشک بالستیک/کروز قرار گرفتند که تا کنون دست کم ۱۱ غیر نظامی نیز کشته شده اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/alonews/124410" target="_blank">📅 12:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124408">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afip9TupCmncpzNztb1oKD1EzjurvZ1CbE0bFY_O5BzqLdrCRlAGekGGEyJ4CbP-gU7DVZt_CUzu1DSaJUpLLtco7rWnJYqykX3ZEKPDc-sMXMOgb0ddpU5px75xvI70kGZ5UVAsMPAhd-XA4ePkDZuJdhT_jJtIjtALXzcF9Xi-EIgc_BFjdu_w1cs985xB_6XDzqLZKUqNCP9JCaN9HDg1YJ4TstPQexi8a1ea90oxXWWNNm4tP0ChckeDM-O21KNpES9ST_EERaeAcbVJKJFUf29w1ZD07g6P4bdaenbWand1_5lgNzip2ovwlKBx4cAlfmhUFv8Sh8GLVrgAQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f70db3ec6.mp4?token=v8BfJDy4KAHfmefC_Bu-jQ-lIp3tcRwKjHjCxLqPCxSg2asXQjs3nRi7pvbMNt5ixAYrG7J5VypNW2caDwzRcu01sOtSH5Nh4G_W8MJHeZFSi5Eb6ew0cYHiedontBIKLlZl1ZQoCXlYiXXIVDVt3c6W1ZqY6B984vdb_RP5z3Yv4h3HaqDZbL1i3LxzCV9gMkp6afsuCsx_kiqg0rb0t6d9N_4iq2lwHPuMVpZU_FePIwgJGKtvOjx_ANPwF_C54pZT4Nk3zDzqOSEpAfWIlO6o4ZiPjMZpuPRKFbe5FeVpDr0KtqWcR53SNOtlfHdzZgqPEDdqU-gvqSZDlNLCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f70db3ec6.mp4?token=v8BfJDy4KAHfmefC_Bu-jQ-lIp3tcRwKjHjCxLqPCxSg2asXQjs3nRi7pvbMNt5ixAYrG7J5VypNW2caDwzRcu01sOtSH5Nh4G_W8MJHeZFSi5Eb6ew0cYHiedontBIKLlZl1ZQoCXlYiXXIVDVt3c6W1ZqY6B984vdb_RP5z3Yv4h3HaqDZbL1i3LxzCV9gMkp6afsuCsx_kiqg0rb0t6d9N_4iq2lwHPuMVpZU_FePIwgJGKtvOjx_ANPwF_C54pZT4Nk3zDzqOSEpAfWIlO6o4ZiPjMZpuPRKFbe5FeVpDr0KtqWcR53SNOtlfHdzZgqPEDdqU-gvqSZDlNLCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حملات ارتش اسرائیل به لبنان همچنان ادامه داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/alonews/124408" target="_blank">📅 12:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124407">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ان‌بی‌سی: یک سرباز آمریکایی و یک سرباز بریتانیایی در جریان یک رزمایش نظامی در شمال عراق کشته شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124407" target="_blank">📅 12:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124406">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
روزنامه ودوموستی روسیه: جنگ علیه ایران، آزمونی برای شراکت استراتژیک این تهران با مسکو، همانطور که در توافق ۲۰۲۵ تصریح شده است، خواهد بود. فشار غرب و جغرافیا، روسیه و ایران را به هم نزدیک کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/alonews/124406" target="_blank">📅 12:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124405">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ادعای نتانياهو: نظام ایران در نهایت سقوط خواهد کرد
🔴
بنیادهای نظام ایرانی تضعیف شده و آنها در نهایت سقوط خواهند کرد.
🔴
هزینه‌ای که ایران تا کنون پرداخت کرده، بسیار بالا است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124405" target="_blank">📅 11:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124404">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
سخنگوی سپاه: برای تمامی سناریوهای احتمالی آمادگی داریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/alonews/124404" target="_blank">📅 11:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124403">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
احتمال شنیده شدن صدای انفجار در محدوده جنوب اصفهان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/alonews/124403" target="_blank">📅 11:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124402">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f68e86a7.mp4?token=tQVW4rZuBQVd0gZcMKKgLyziCMfMuZU1BG4jkXl1WzMR2RHTTHwUR7I8fyqpSBKx7noYbxr5URYXIALulljzv-y6-eRENnc_5kysj0VZDO4bT2rNqcGGhPpdHotGvQZ2o2PLzpZzgDGgFW3yEV1S2ozICQHS5jpmaCnDmkyBWqxSeWW1x10Ry9sPD7c9pozyFyeYqXxDHKjTP8HIsjDyZBJ82rj6RGOkv2ax4WtVf2en77BHW2IdT4Fmjkavcfq4-AZLDO18DpxAXPQtT-xFmgFe_W_A9f-i6vX5n96bjrVSPns6fsLdha1UIoV-FZFQTT0VtPxV9dC7kFEKNVJhIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f68e86a7.mp4?token=tQVW4rZuBQVd0gZcMKKgLyziCMfMuZU1BG4jkXl1WzMR2RHTTHwUR7I8fyqpSBKx7noYbxr5URYXIALulljzv-y6-eRENnc_5kysj0VZDO4bT2rNqcGGhPpdHotGvQZ2o2PLzpZzgDGgFW3yEV1S2ozICQHS5jpmaCnDmkyBWqxSeWW1x10Ry9sPD7c9pozyFyeYqXxDHKjTP8HIsjDyZBJ82rj6RGOkv2ax4WtVf2en77BHW2IdT4Fmjkavcfq4-AZLDO18DpxAXPQtT-xFmgFe_W_A9f-i6vX5n96bjrVSPns6fsLdha1UIoV-FZFQTT0VtPxV9dC7kFEKNVJhIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دموکرات‌ها نیروی نیابتی ایران هستند !
🔴
برایان مست، نماینده جمهوری‌خواه کنگره
:
"تهدید شماره دو ما، جدا از سپاه پاسداران، دموکرات‌های مجلس نمایندگان هستند. آنها دومین نیروی نیابتی بزرگ ایران هستند!"
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124402" target="_blank">📅 11:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124401">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcS6kTm2Humukt_iZYU8LMfjQjDPyptUQ0j720_5P9rwyk7BoW_BGqIOWFbbL_zJjaJFSW9bw8PJpmhqWZEFn0AG3Fmt4PaM3c9EWZGyTwkBGr-0MnHV0V21O6UJSnsMgvYQWorhC38Sp8coKuhuvgwylUFit9X1RWwI2DK_fD0zXl7xjYUc-haZw2r-q-CLTnAbTAZuVbMePqZuQZuLARyKAgMKTgIHn-oaSufn4oKA5gPXD9TQkFoK9mpATBt_4UITlXem_Z42q8dAZMClU6HVVunohBNXBm17itNWjznYoVVPg7u-nyaozpZsv3AbZXETfHRo6rjQRg7yPUHQzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آبی خاکی باکسر حامل واحد ۱۱ سپاه تفنگداران که شایعاتی مبنی بر اعزامش به خاورمیانه وجود داشت طبق اطلاعات USNINews به دریای چین جنوبی برگشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124401" target="_blank">📅 11:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124400">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
رویترز: قیمت نفت با توجه به پیشرفت مذاکرات آتش‌بس آمریکا و ایران کاهش یافت
✅
@AloNwws
خبر جنگ</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/alonews/124400" target="_blank">📅 11:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124398">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/637826146d.mp4?token=I7JB2ebmwr1edes9GHNxQGwZoXWNLXhh7Y6SZ1ubTZu5OKFmi5lpxie110ZdKOJjpRHW0IJV49HMDKuHkfdyF-EF_kfPTQxyjHdJzWDAg8hsHM3g5Nqn-MsXnSb781Hn9k2kbBZi5bsbHrISwOn81FxsMDBPEkDnQecX_Gh6cyuUd1IIp1ojFn58IJL_MFa6z5gcv6lli1BlEYFgD7IYQMPvi8owO-B47fbHc1eLdOIAh0a2iskeNoz1ipg7pVEo_ajn6CAJJiyVK3PYXgmNNcHEqkRzL5TPoFbJLEaoHiBOMt6eU0OtY-slHDN9Wbm5Q2I_JgVCSrgvmA8Oi8TVxg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/637826146d.mp4?token=I7JB2ebmwr1edes9GHNxQGwZoXWNLXhh7Y6SZ1ubTZu5OKFmi5lpxie110ZdKOJjpRHW0IJV49HMDKuHkfdyF-EF_kfPTQxyjHdJzWDAg8hsHM3g5Nqn-MsXnSb781Hn9k2kbBZi5bsbHrISwOn81FxsMDBPEkDnQecX_Gh6cyuUd1IIp1ojFn58IJL_MFa6z5gcv6lli1BlEYFgD7IYQMPvi8owO-B47fbHc1eLdOIAh0a2iskeNoz1ipg7pVEo_ajn6CAJJiyVK3PYXgmNNcHEqkRzL5TPoFbJLEaoHiBOMt6eU0OtY-slHDN9Wbm5Q2I_JgVCSrgvmA8Oi8TVxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون دانش آموزای مملکت در اعتراض به تأثیر قطعی معدل در کنکور دست به اعتراض زدن و شعار میدن.
🔴
« دانش آموز میمیرد، ذلت نمی پذیرد»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/alonews/124398" target="_blank">📅 11:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124397">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkulojYUg6uJOvfg4KCtC0tumS_LxAK8Pxb7PrgZ-ol4ggggT-ccu9PfEeGAV8fjedxlpMu569nz1Xe8K1Efpm95pYMtGOzGmskU_n8pkS0gCn-o9RpO5HbJpS2Cvw7Bq_lp6X_09NoDFV9rtEmRreiaKlrWxYo7JA4Uz0N_n3jnn0DJDTPViROha8srU2VMg3V0xFzqId5GJVPj_pnsOK6ncZwZZYSU76Ts-yTGNjHSpxcuyf3hX7-oDvMLr-faKof5NE8xlXAxkiN613iz0BIuQwjEOOGZKMdoJKX1bOGEHu7rl9SLR2E8aDRmQxpjOSu6XZWqhG31EtVi6sL6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله هوایی اسرائیل به نبطیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/alonews/124397" target="_blank">📅 11:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124396">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
سخنگوی سازمان مالیاتی: فروش تا ۶۰ میلیارد تومان برای امسال معاف از مالیات درنظر گرفته شده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124396" target="_blank">📅 11:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124395">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0240861db6.mp4?token=jTXI-3a60PquE2URrSxc3D7JwtO6PTRq9tGVOFIcuY1T6VeCQteVHT5aodoACPPGH36c4v9OH3kvT8iuDxr899prcQAWmBUHYk4wWnx85uOSBn1rb2FjaUVo-WMIZp7ffuprEITMsPz89baL_GOC73y3aYaWJY_qtd7pdx9kpmmMdp5Lm4CmZQ85V4f50ncMAn_dXgnkwVBiMjU_vfsJn3unt8R0rLrUiaNVEdfyI3j_kO1CqTzVOLt8D-gM4NFxdb6vbRrTRr-lQe8_s2vVjr4sWGZAATW_Pe8rCoWW5sMVzQFSixjsx4S1uJ_sj9EgcICPUdmnCX6JVnR2DKq4FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0240861db6.mp4?token=jTXI-3a60PquE2URrSxc3D7JwtO6PTRq9tGVOFIcuY1T6VeCQteVHT5aodoACPPGH36c4v9OH3kvT8iuDxr899prcQAWmBUHYk4wWnx85uOSBn1rb2FjaUVo-WMIZp7ffuprEITMsPz89baL_GOC73y3aYaWJY_qtd7pdx9kpmmMdp5Lm4CmZQ85V4f50ncMAn_dXgnkwVBiMjU_vfsJn3unt8R0rLrUiaNVEdfyI3j_kO1CqTzVOLt8D-gM4NFxdb6vbRrTRr-lQe8_s2vVjr4sWGZAATW_Pe8rCoWW5sMVzQFSixjsx4S1uJ_sj9EgcICPUdmnCX6JVnR2DKq4FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با گذشت حدود ۸۰ سال از پایان جنگ‌جهانی دوم، در پی انفجار بمب برجای مانده از این جنگ در شرق اندونزی، پنج نفر کشته و سه اندونزیایی مفقود شدند!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124395" target="_blank">📅 11:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124394">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
جان بولتون، مشاور پیشین امنیت ملی آمریکا:فکر میکنم ترامپ واقعا در تله‌ای گرفتار شده که خودش ساخته است.  به نظرم وقتی حملات به ایران آغاز شد، اهدافش را به‌روشنی تعریف نکرده بود.
🔴
فکر نمیکنم هدف ترامپ در این جنگ، تغییر رژیم بوده باشد، با اینحال ترامپ می‌داند اگر توافق بدی هم انجام دهد، چه در مقایسه با توافق هسته‌ای اوباما و چه هر گزینه دیگر، به‌شدت در معرض انتقاد عمومی قرار خواهد گرفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/alonews/124394" target="_blank">📅 11:04 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124393">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gN4cqSLgo8jtA68Iyzmw-zizHs56Who8G9Bht1_qDYSrm-uYuuUJJCS2yvAI11S5WmRof-1Sbv6z2dNrOSIIjGWTm-hWYiaWZoipdBwzNkXj-cRNwF77PaJIicXahdHDGDp7hQeqq5j5EiLQPrPDlgV2OfUHCIKY7FdhTYaaP6Qi-axC6zJQKQ7pZRIYv9L4wEbPWyWWAMBoQIY1GydgNSxKKOyupc92ZcNNHy_a1SGZD3gCVgFpM-l8xoedIK7aadamxgPpj9fw6XtSNXggzO4sDb7VmChGvvPj95uDgw-FYN2IoGoeRhwfU7iiMkXlTiYdnawH_1zQtadtxcui1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رنگِ "آبی درخشان" یا "Luminous Blue" با کد «125-28-38» به عنوان رنگ سال 2027 انتخاب شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124393" target="_blank">📅 10:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124392">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
وزیر خارجه فرانسه: هیچ چیزی نمی‌تواند اشغال طولانی‌مدت اسرائیل در لبنان را توجیه کند.
🔴
واشنگتن و تهران پروندهٔ تنگه هرمز را سریعاً حل‌وفصل کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124392" target="_blank">📅 10:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124391">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqyWD3jxrkX2BkYTopvvBMeBKbImjtlm-R5DvbI4QLsCbMOwxiiqJRjtxpeOsZj9OUpr9KvggbcpI-TsQ29Lj9Sqot59SRDR5Jh6ngd1TXJfRsH9jkGGHEDPyZi6aYp5C-CmKthOf14JDd1NaVLvMalhvOyrNppFAebhjnLgJ4XO4TBPRIBikHa3b6JXAIVNsq8qf_85kbyMK9j5rpOGtN7jbizKwNdkrETjn_qlUkAsvhf4cd5wQVWuDnvOb-sgyCOKkm1BTT1innldoDA1sUPMZO9lT0vO9Sa0NNsSOBi5vB9Rm7A1J0OXT5jSZrWOX_4FvXMcQiWCA6m_LHmwnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روایت آکسیوس از تماس ترامپ با نتانیاهو: تو دیوانه‌ای لعنتی. اگر من نبودم، تو الان تو زندان بودی. من دارم کارت رو درست می‌کنم.
🔴
الان همه از تو متنفرند. همه به خاطر این موضوع از اسرائیل متنفرند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124391" target="_blank">📅 10:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124390">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
یدیعوت آحارونوت: ارتش اسرائیل تحقیقاتی را درباره چگونگی موفقیت پهپادهای حزب الله در رسیدن به نیروهایش در طول شب آغاز کرده است
🔴
ارتش اسرائیل تعداد وسایل نقلیه سنگین خود را در لبنان کاهش داده است پس از اینکه این وسایل به اهدافی برای پهپادهای حزب الله تبدیل شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124390" target="_blank">📅 10:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124389">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCzhB6Hhpt4LHhB6sL2cafo-4qq37hjPhztggDbpETq3lMr1MWLmBWAxZ-2DBS9EUdVx4ZYe0zLxI_i2Ku3FHRcCOb2kxKmh37WQqQi403R9HXnn90fE2jHOxVhTwv8RM6o69Rk7IOyThZBxMKtOyqCdT2JvMZsm18-UG4iHw5h3l4VfJZLHqGscSRP19DtMRTFNUFFdQ069xH698oDnFKTZvpSNR_Jzh20TotFbsPwHJgKT9JKgJq8hn0UZkbejZ_VMH2VS_sOvU_HwPOUc1OEcUnSxLtJcAEJgk0C2I2BuXLSFP5aWLoiIJngYf3FN4kUr-iOl-OrkGGWKhR7qag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بر اساس نظرسنجی جدید نشریه پولیتیکو، اکثر رأی‌دهندگان دموکرات خواهان تغییر رهبری حزب خود در سنای آمریکا هستند.
🔴
در این نظرسنجی که درباره انتخابات میان‌دوره‌ای کنگره در سال ۲۰۲۶ انجام شده، از شرکت‌کنندگان پرسیده شده که آیا چاک شومر باید همچنان رهبر دموکرات‌های سنا بماند یا خیر.
🔴
نتیجه این نظرسنجی نشان می‌دهد که نزدیک به نیمی از رأی‌دهندگان (۴۷ درصد) با ادامه رهبری شومر مخالفند و خواستار تغییر هستند، در حالی که فقط ۲۸ درصد از او حمایت می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/alonews/124389" target="_blank">📅 10:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124388">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=RngrGu1-ENx3hZOYaLubmGa_Ok4rCOpJK5WAp86KloyX9vnpg8KDRdJ4oh4iyjkOXtVZ_Z5s9OJdx0gKTKf3zWt2lOGk_sOr-rtFYQxFCmr1YnBs63NoIpU9f1GOqn52UP8fRj31bqNkEtc7pD3heEXJKnSmE82MQHSThl4rQyacLC8KTe2Ojwh7uE5_kRUe98sPkpNXnrAO9IDa_xBUaFc356ORjIx1DImvGItGMYdPI_u2cGJUwGnvw4GY4UtOkLfFfQ5DM7uqTjtqi80pSE1iKwGSjIaxuYpjtbvV_KvMwrRpbkNjxDkNGZVDeu8wDw2gRVYBuvXHLiP24DhpxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b11e2b7f3c.mp4?token=RngrGu1-ENx3hZOYaLubmGa_Ok4rCOpJK5WAp86KloyX9vnpg8KDRdJ4oh4iyjkOXtVZ_Z5s9OJdx0gKTKf3zWt2lOGk_sOr-rtFYQxFCmr1YnBs63NoIpU9f1GOqn52UP8fRj31bqNkEtc7pD3heEXJKnSmE82MQHSThl4rQyacLC8KTe2Ojwh7uE5_kRUe98sPkpNXnrAO9IDa_xBUaFc356ORjIx1DImvGItGMYdPI_u2cGJUwGnvw4GY4UtOkLfFfQ5DM7uqTjtqi80pSE1iKwGSjIaxuYpjtbvV_KvMwrRpbkNjxDkNGZVDeu8wDw2gRVYBuvXHLiP24DhpxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع دانش آموزان مخالف تاثیر قطعی معدل جلوی وزارت آموزش و پرورش
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/124388" target="_blank">📅 10:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124387">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
العربی الجدید: قیمت نفت با دو ریسک هم‌زمان روبه‌رو است؛ از یک سو کم شدن تقاضا و از سوی دیگر کاهش عرضه از خاورمیانه در نتیجه جنگ علیه  ایران
🔴
از زمان آغاز درگیری‌ها، قیمت نفت برنت بیش از ۲۵ درصد افزایش یافته و به افت شدید تقاضا منجر شده
🔴
در پی نگرانی برای وجود مین‌های دریایی، حتی اگر توافقی حاصل شود، این امر فوراً به معنای بازگشت جریان عرضه به قبل نخواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/alonews/124387" target="_blank">📅 10:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124386">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
وال استریت ژورنال: موضع بی‌طرفانه در جنگ علیه ایران، در حال تبدیل شدن به عاملی زیان‌بار برای عمان است
🔴
آمریکا به مسقط فشار آورده تا روابط دیپلماتیک خود با تهران را قطع کند و جانب یکی از طرف‌ها را بگیرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/alonews/124386" target="_blank">📅 10:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124385">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
وال‌استریت‌ژورنال: آمریکا عمان را برای قطع روابط با ایران تحت فشار گذاشت
🔴
روزنامه وال‌استریت ژورنال نوشت اگرچه عمان در مذاکرات ایران و آمریکا نقش میانجی را ایفا کرد و در اوایل جنگ اخیر برای حفظ کانال ارتباطی کوشید، اما دولت ترامپ اخیرا رویکرد عمان در قبال ایران را به عنوان رویکردی خصمانه در قبال آمریکا دانسته و مسقط را برای انتخاب میان تهران و واشنگتن تحت فشار گذاشته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/alonews/124385" target="_blank">📅 10:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124384">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
مدیرکل آژانس بین‌المللی انرژی اتمی:
انتقال ذخایر اورانیوم غنی‌شده ایران به خارج از کشور کاری «دشوار است اما غیرممکن نیست».
🔴
چنین عملیاتی آسان نیست، چراکه (این ماده) به شکل گاز است، بسیار آلاینده است و عملیات ساده‌ای نیست
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124384" target="_blank">📅 10:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124383">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
یمن: اجازه نمی‌دهیم حزب‌الله به‌تنهایی بجنگد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124383" target="_blank">📅 10:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124382">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VfN_wDzfsw-MqVgL_-VYGOlOPgBfDzT7We2lt6PJ1jkJWH0Nw_UGn2NLZ1FU5eNwcSiw1VZzYDh70IJCKFuG4rG7SACq9AM-osSQR6njbphV18Y20ZevfC_4GtxRC2ikrnkImE4XPl2QKF3SvmJGxlrc-vzpIci6v1OHPCtOY8L8YRgrA5TTMmOFIW1R0yqOwhNWRfIEXYoNtdYQUtyiZBmjHnXtgYwBH6HTklXr-9RwNHJl0BIYrjTh9IgCzbSjqYr-hU-6xcz-zK4zVMJVRY2DhqHEl0a23IfypsRb2EhvlwU8m8hlvv9pWR6ZAq_PRP-gn_ewqFINhcifC3Mjog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تولیدکنندگان بزرگ گاز مانند قطر که زمان و صبرشان رو به پایان است، در حال زیر پا گذاشتن قوانین دریانوردی هستند؛ اقدامی که می‌تواند پیامدهای ماندگاری به دنبال داشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124382" target="_blank">📅 10:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124381">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUC-cf2CVVqcdUsrIO9Dn2iiimXFNlK90H_Wz0ojAJzyqQSpthyLt244Zvq1s_kcILR7SSLBLExCft5jzqx6B7bWHqZ9zrK5rdba09ezJye-hPZMNlGNsUszBHowAe5eFdZRwMEZ0nWqFuCJg4Wk7sU_wmAOqJRNFomHf-YhOl-5fs58wswd73T3Qwq3l6xQtfNaHxlWiff3A4ItBurX0avQDrraVqtXrJMq6p1uMsECbM93Ke3bevAjgVpZwDBBV_OcP3k5kPqZ0AjzLbnjWxkB8fkVeYWQiwLXJo7YMeao9sdlb2nvsl00TuDuZsTXvVXYuJEvJoScb0hOZAqT5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / حمله هدفمند ارتش اسرائیل به یک خودرو در جنوب لبنان !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124381" target="_blank">📅 09:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124380">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
مهر به نقل از یک منبع آگاه: متن نهایی ایران همچنان در حال گفتگو در تهران است و هنوز پاسخی ارسال نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124380" target="_blank">📅 09:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124379">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
رویترز: درآمد ماهانه ۶ میلیون دلاری سوریه از افزایش ترافیک هوایی پس از جنگ ایران
🔴
تعداد پروازهای عبوری از آسمان سوریه در مقایسه با ماه مشابه سال گذشته ۳۷۵ درصد افزایش یافته است.
🔴
بر اساس هزینه ثابت ۴۹۹ دلار برای هر پرواز، ترافیک هوایی در ماه مه ممکن است تا ۵.۹ میلیون دلار درآمد ایجاد کرده باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124379" target="_blank">📅 09:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124378">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p5qwvJOY7W2hQRHW-wXtCJyrDrEqu_JLdhcMhgT-n6oIA3r4z7yJu4-pG-flt10x6b0U1YAA86hRcJLy6HhE-0Cxem-fwNmblAfissqDUg73wgh2tXnei0gFjHqbfEsYocsan33SWWqDrXSSW4Bdn-TICSSxIyli244CjUGv9NvxaeowtnAljgJQXuYOSMAnvT0F0TsI1JhjvL1ThN3bqwKHadTnAStIgVPIoxSe6DUbyRjFQkhBoF8SywGB16rROZjZeFQWizqFPofIpuFPaRoZ-Crw4wv3hKUvbmRBmVuKSTm4UlKiP3mYwzgsqpBKakdcAgHaeyBU4BI_ub01-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش NBC News، آمریکا در ۵۶٪ کشورهای جهان، سفیر ندارد. همچنین حدود ۲۰۰۰ دیپلمات آمریکایی در یک سال گذشته از خدمت در وزارت خارجه کنار گذاشته شده‌اند؛ چه از طریق تعدیل نیرو و چه بازنشستگی اجباری
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/alonews/124378" target="_blank">📅 09:50 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
وال استریت ژورنال: ترامپ نمی‌خواهد قطع رابطه علنی با نتانیاهو رخ دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/alonews/124377" target="_blank">📅 09:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8cLXIb2w1uQKcPrXxzGeT-vvDVOHPPOjfuEwkKPk323g8BSYIdIhSqyKiHOxYcXUdWnAjNBhkril2vwj-fGquyeHB9Fc5edlwYo5cS8-dLw6M4QqBdTSRlZOC50M9Ox6Pc9Ea7XdWK97fsJupzOluXBd9bHZJcEIuHm62_EEpRINu_dd01S9tOH9PSR1QhNBZiNSq3U4e8AFX_g69neGbgfnRTawXfvF4wDG804OmeXbdCgfn75QOGglPutbnGPTs35CevVJkVepkJpOOHXZafd-nVOLAkUdItIOnfOw0LmlC3QzjmclFXLJFHtuf6moaDhU-KEwYr7amPnv8p8pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: قیمت نفت پس از اظهارات رئیس‌جمهور ترامپ مبنی بر ادامه مذاکرات با ایران کاهش یافت و این موضوع باعث کاهش بخشی از نگرانی‌های بازار شد، هرچند عدم قطعیت درباره مذاکرات همچنان بازارها را در حالت اضطراب نگه داشته است.
🔴
نفت خام برنت پس از اظهارات ترامپ کمی کاهش یافت و از سودهای قبلی که به دلیل اختلالات مداوم در حمل‌ونقل تنگه هرمز به دست آمده بود، عقب‌نشینی کرد. این اظهارات نشانه‌ای موقتی از زنده بودن دیپلماسی است، با وجود شرایط سخت‌تری که واشنگتن اخیراً به تهران تحمیل کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/124376" target="_blank">📅 09:41 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGNlccebASGhR6-uMz5iavCYxxuqPzZ8rcbR2HfKA4PBvw1yeX_Q2WEy8p0EET7HvcPnND0Y1GEi3uMwqe8wbPmh4qdaFlWELFsKmWE6CZM8EzlhqsPBPzvBGcakqXz5clZVfWEBv8o4zH3ScY8PHXClt6jFs6oC1F44pVczSNcIxZfMCL50isPPfcLdQlPig-j9bBIFu-kfe-lqHhLXUTwI7e74y9ipWbSi3jl91KBngtpEzv9DFMITRPjfEXNGWEIsfDa3Pyhb7ZEnjPHW0nXZDUfztsyp7aQyfPiLLPKDt58L6ThZbD1cqj-_jM_pkTYSVRh_sf8XLZg4hHNVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت قهوه در ایران از ابتدای ۱۴۰۳ تا امروز ۴۶۲٪ افزایش داشته؛ بسیار بیشتر از رشد دلار
🔴
طبق داده‌های منتشرشده توسط مؤسسه مطالعات اقتصادی بامداد:
🔴
قیمت قهوه در ایران: +۴۶۲٪
🔴
دلار بازار آزاد: +۱۷۹٪
🔴
دلار بازار توافقی: +۲۶۳٪
🔴
قیمت دلاری قهوه در ایران: تقریباً ۲ برابر
🔴
قیمت جهانی کامودیتی قهوه: +۴۰٪
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/alonews/124375" target="_blank">📅 09:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
وزیر آموزش‌وپرورش: ‌امتحانات نهایی پس از تأیید مراجع ذی‌صلاح برای فراهم بودن شرایط حضور دانش‌آموزان در حوزه‌های آزمون، برگزار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124374" target="_blank">📅 09:22 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDB3_aCOVm8_NdpULNr9P9uiBqyrzuhczmJgUydn-dSZUsMGT-ga-G-0pZtmMtoGU7MeFs774li5pfWpNbSm8lgRf4fXHn0rrJ0bUFNzqbo6A6cm9BedlMXEpn8EsRZNXoWHmsFN6JALbmvjiWgXRXLF6t2N1iVRiePM7ljCiqGx2p5CPhoH7MmWB5w_He-L2oRwI1zsixqV-wAK7o50O0-HMcn7EaQT-JLRj3e139O_kinrEyeM7MDXms12nKBYw8DM7wZNHEiR2eZ0qmB9NUU82Vq919-uNGa_TCmbYbTtwNEiRBix886X_-eQTkd922ntknmWWrdaSqZJelXfQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آخرین قیمت نفت ۹۴.۰۹ دلار
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/124373" target="_blank">📅 09:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
مقام اسرائیلی: در حال حاضر به بیروت حمله نمی‌کنیم اما نیروهای ما در جنوب لبنان خواهند ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124372" target="_blank">📅 09:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124371">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بزالل اسموتریچ، وزیر دارایی اسرائیل:
اروپا باید در جنگ علیه ایران در کنار ما باشد، زیرا اینجا محل تقابل آدم‌های خوب و آدم‌های بد است!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124371" target="_blank">📅 09:06 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124370">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فایننشال تایمز: آمریکا مذاکراتی برای گسترش استقرار تسلیحات هسته‌ای خود در اروپا انجام می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/124370" target="_blank">📅 08:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124369">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
اکسان موبل هشدار داد: با کاهش شدید ذخایر، ممکن است قیمت نفت در هفته‌های آینده به ۱۶۰ دلار در هر بشکه برسد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/alonews/124369" target="_blank">📅 08:55 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124368">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
رویترز: حریم هوایی سوریه در ماه مه گذشته، پس از آنکه خطوط هوایی مسیر پروازهای خود را تغییر دادند تا از حریم هوایی مناطقی که تحت تأثیر پیامدهای جنگ آمریکا و اسرائیل علیه ایران قرار گرفته‌اند، اجتناب کنند؛ شاهد بهبود قابل توجهی در ترافیک هوایی ترانزیت بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/124368" target="_blank">📅 08:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124365">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e1a95424e.mp4?token=owojJQkSMMFjncU7rv6z0VmtTb5Y_mJ8idtjUGUCgDGo8-2snsDOuQ2wc6UzmioN8WvKwh3IkD031UMYYNtF9BXLZMwY0pnoS9bt-0j0Ewpa3Aq09409X-2BWTzlbqqqsWvIzf865oS7mgFlI7Xfk9kIp69mAdfYN3M18vSeNsmaGIrOtGZlPsINJuEw86HGfN9AGd75f6QaI6epNqSvzuYniq2nLxnh_LnOQS-kavg-ghmnaWyJzMx-dYzrTebR0G0QD3PMF0V-UzZGK30p9QxiTBOkK9Bs65tlXcIdFbPVUMMqWJKjuYM3A7OAzpmysZjFrFFKE2iXn_B_MLFM9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e1a95424e.mp4?token=owojJQkSMMFjncU7rv6z0VmtTb5Y_mJ8idtjUGUCgDGo8-2snsDOuQ2wc6UzmioN8WvKwh3IkD031UMYYNtF9BXLZMwY0pnoS9bt-0j0Ewpa3Aq09409X-2BWTzlbqqqsWvIzf865oS7mgFlI7Xfk9kIp69mAdfYN3M18vSeNsmaGIrOtGZlPsINJuEw86HGfN9AGd75f6QaI6epNqSvzuYniq2nLxnh_LnOQS-kavg-ghmnaWyJzMx-dYzrTebR0G0QD3PMF0V-UzZGK30p9QxiTBOkK9Bs65tlXcIdFbPVUMMqWJKjuYM3A7OAzpmysZjFrFFKE2iXn_B_MLFM9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی‌ها در سراسر کی‌یف، اوکراین ادامه دارد.
🔴
بیش از ۷۰ موشک، از جمله خ-۱۰۱، زیرکون، اسکندر-ک و اسکندر-ام، در حمله گسترده روسیه به اوکراین استفاده شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124365" target="_blank">📅 08:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbBXpBHBmAac4CI2Gn7UtteO6KqBI6BlhdtjnmDcPQ8uJ_LNzxkAbQUUH4lzU1N4gNIPWwoYVBZuE25LfAUEgvtHpIMLJXhBW7viM3bx57XRaX4f_Ev9x7uKuZ6jg8rorp-UltQIcbTd4dTaKhhtb0Qtqz_VJQaZ11eSHO12GZwd5Q5zsLZXcUXdV3yosAcZMEz32WH-M4Ivie2JPX3r21atIwl3N2P6ahvFB3zKUS3djvF3EzPqA2xqyw2tv9MiymLm60HS6vHju8CbC-psQ8Q2MQqNRQ9WNPX4K5Zgdp3FmVk1hsQt7EgIUTtumdRF7dQFkjWGLUSr6dsOVYeWZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس کمیسیون امنیت ملی: روز های تاریکی در انتظار آمریکا و اسرائیل است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/alonews/124364" target="_blank">📅 08:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124361">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Etrm6ldtzTbPH_yVmuhAl8SMRZX2bArhB33f9U9JbdDK88EBS8S440kB5Z8aJle9X6tBZ66qGl19Wkmod89imRnl7c_AZOKQvSpkL0OM83UgCQhwa2x2mgoTdz8BZ48wNBQgLJolOwd2FmFq-wW6PFHbGqIFKIecvIcXg9oQfujV1uPmCYRJUQNpKg9XuqI-X0glksH6KD2yEdTNiHrgZ16hIu5rCqtH-TaLHL7yEF1UiALYk1y4My2jRRzbU8EchkOAGcSw06Ow7bDAZDXZ4sXgcvC0wO0yvJyz4eU76e9XxvZlQvmN2VFxm-tUtH_U_Q7uM75TEjqTuiTgPQhNQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/285b55c0ee.mp4?token=QcA1_2wyBIbC458-x9wpoGXstlbHsDQNqrp4_Rz2kxL8fcbEfr13SReofQJvFVoqcYnKSyvLPAy9-Vr8HegwUf2W4sQwojp54W_GXIUSEj9SJtMMPSLdjkr8JW_LQyZ46PjiUyAnny02_wjZeZWTUQKO7JwhSE4gMdPEfAQdekqKpo1IHWPZWQKfEoq_epDo9XJaVHFklfdVE7rEIjX4vou5VTwsLiKpDAVsdvYS4znPzMHFz8ujCuoVcsK9n2BsOUz5uBXFzKYluT-Hu9mBQ4pcGD7JvFbIQJAjsBFC9Pcs6O8pHT1KLa5YQgOS6xladUUGcoms9VxFzCnYqDlE-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/285b55c0ee.mp4?token=QcA1_2wyBIbC458-x9wpoGXstlbHsDQNqrp4_Rz2kxL8fcbEfr13SReofQJvFVoqcYnKSyvLPAy9-Vr8HegwUf2W4sQwojp54W_GXIUSEj9SJtMMPSLdjkr8JW_LQyZ46PjiUyAnny02_wjZeZWTUQKO7JwhSE4gMdPEfAQdekqKpo1IHWPZWQKfEoq_epDo9XJaVHFklfdVE7rEIjX4vou5VTwsLiKpDAVsdvYS4znPzMHFz8ujCuoVcsK9n2BsOUz5uBXFzKYluT-Hu9mBQ4pcGD7JvFbIQJAjsBFC9Pcs6O8pHT1KLa5YQgOS6xladUUGcoms9VxFzCnYqDlE-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیشب روسیه حملات سنگین و ترکیبی از پهپاد های شاهد و کروز علیه مواضع اوکراین انجام داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124361" target="_blank">📅 08:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124360">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
الجزیره: حمله هوایی اسرائیل به حومه شهر تبنین در جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/124360" target="_blank">📅 08:38 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124359">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
قالیباف: ایران نه تنها روند گفتگو را متوقف خواهد کرد بلکه اگر اسرائیل حملات در لبنان را متوقف نکند، مستقیماً به اسرائیل حمله خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/124359" target="_blank">📅 08:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124358">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8kV5Lq8Ecr0wYinuY7HaIeQavo5U7dLufJ4IdxA-qjkQvIhZKY1lpjQkuGiZXkIH49Pf3l7v-k6dcGQ8SSI6gVXPENXY_R7iVGpumgp-BeBPVHCLK_VvNbaFdF6jXbp14Y98HoHVcXBgBEtNfEKk6Pzzc3W3kNxd7oASFub1NxZRY2aPfKTokkpLUZh1-Fmsvg33bShw0CtIv7SczpD5jEbcZSkWHRH0cTTgTV8FgJkIpm1V6ernJgj9J9mRL5_a3HrxvK_p5f9PFBQvERlxWv5AykYjuYOSbv35I7JCfYKgyhKoTUz3IXOz04z6zZ6ZTlZ-zh6IeWrt34b-p0e9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ برای بار سوم این توئیت رو منتشر کرد:
اگر ایران تسلیم شود ، اعتراف کند که نیروی دریایی آنها رفته و در قعر دریا استراحت می کند ، و نیروی هوایی آنها دیگر با ما نیست ، و اگر کل ارتش آنها از تهران خارج شود ، سلاح ها را رها کنند و دست ها را بالا نگه دارند و فریاد بزنند "من تسلیم می شوم ، من تسلیم می شوم" در حالی که پرچم سفید را به شدت تکان می دهند ، و اگر کل رهبری باقی مانده آنها تمام "اسناد تسلیم" لازم را امضا کند ، و شکست خود را به قدرت و نیروی بزرگ ایالات متحده آمریکا با شکوه ، نیویورک تایمز شکست خورده ، روزنامه خیابانی (Wsj!), فاسد و سی ان ان و دیگر رسانه های خبری جعلی عنوان خواهند کرد که ایران یک پیروزی استادانه و درخشان بر ایالات متحده آمریکا داشته است ، حتی نزدیک هم نبود.
🔴
دمکرات ها و رسانه ها کاملا راه خود را گم کرده اند. اونا کاملا ديوونه شدن!!‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/124358" target="_blank">📅 08:00 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124357">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
یک مقام اسرائیلی در گفتگو با اَکسیوس ادعا کرد: اسرائیل دیگر برنامه‌ای برای حمله به مواضع حزب‌الله در بیروت ندارد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/124357" target="_blank">📅 07:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124356">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Q5y6Z7ELi14sm4nNL8-Iz1DFPNZ5mhkXM-mAp9mRDk9G13R3lTRlG9N9wp644wvZyRus2MUXtoL6FeeUA3uPu8l5zOf3pqvEPlhwXjT7j66r3IvVCkUBofDrylHrNWrRe7jnuf5-ktiGncHxqgD4-ErN8gq6hMnqBat0XZLWlMwa4nzw6SJKXm5rDXokghzbmgDCpFgSrFk4bu_cuho4lh7f_3HQ4PkAY3eW57k1qQUchmFfBU-QIXA42LH66VNDCdTzo3VNvJF4rFxOHjcBT8kQsXSjfJ_RMbjCYZVhkGh66o-jrNDLZRehYulPqnab50bnULdL8YOkvrZvHlWM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
همراه با ساب + حجم مصرفی، فقط 8T!
🚀
😍
فقط گیگی 8 تومن
😍
✅
باخرید
90 گیگ
100 گیگ تحویل بگیرید
😍
✅
❌
فقط تا پایان امشب
❌
🔥
اگه دنبال یه VPN پایدار و بدون دردسر می‌گردی، این پلن مخصوص خودته!
@Netaazaadbot
@NetAazaadBot
✅
همراه با ساب + حجم مصرفی
✅
15 سرور اختصاصی پرسرعت
✅
اتصال پایدار و بدون قطعی
✅
سرعت بالا حتی در ساعات شلوغ
@Netaazaadbot
@NetAazaadBot
📩
برای خرید و دریافت سرویس استارت رو بزن
✅</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/124356" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124355">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9vb3iRObxbB4XNVPcNmGvySYMj_jswccNOxKE39SXT2woycx3NFGAhjKOixBC6Z33GoOzn5Js6f_pvqiTi1SyFe0HT610pGndXP4n6DulvmTa_4n1IDq8dXzHmtMQ5_rXdAZKvC-Ag3zqVambVbuS0Oj0ta8FBxlDdqF7_1xQTB16a7RIP1De3LP88xhnuGbMw6_rgRcBLdsFrbBqz-mjrJ_Y567wTxd2yfPc2qv6I2FXF9fdcz6ajJ739OP_mhGHcrxqy6VIEc1AImMXJZaCuCVX86S_8OZXQQAXA37nbIK4CeYvE4cIMH8n_-UJt0xWUH0exLNncnl9YigUyrFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند و من سریع مشکل را حل کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/alonews/124355" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124354">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbwtjQpYNjt8slyaFeG-tptz0ZN8Lc17ko8mYZla6lMuT72xb7uGu2mqe5UKXx9LV1imPVlDATIx9BbRpBrpS6q8dw5m6Yn3x9lTzm3GCwxaQjnpxgPsxzk3NIt2RHotT6OTeL1pz8IyRKTCMSHO-1zxCbqWgPSblFqwePs-2WO6iTuSH1TW2wSgOz4FUi9_HFQ3LJx8ci7oXSB8nAL4KYuVkItndwPI8s_mtgyDa-AQhbSMaRPjmVnVO0qyj_UNqSYtItqr1N4bAVzRET50IaFKgQAMjLToSDy4SbiiekHpn8dkspitf5jUk2qMu2P3NEcRtZQ1H2mPXK2XrtvxAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: ترامپ تنها به دنبال توافق است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/124354" target="_blank">📅 01:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124353">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
کارشناس صدا و سیما: خون یک لبنانی اندازه خون یک ایرانی با ارزشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/124353" target="_blank">📅 01:35 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124352">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qAv2xhcgUuk2UkIqltuTmCfXR3xp_ing9uQnB9SRtVrKUXAFgyPBux7CXKSZY_1d4ILNlJljju1e8UMhX8jdV7OlI5X4espgHxhdsgpVpNCKUjkoNuE4HVY7niXBTJi2Og_VNL8steTgnvN7U2118eIPYESFKxKFeH5ch4urN3N4xZJR_E-o8LvCpLQEpSpK_h061lGVT9nB0kB4Rq9FIjv51XdJKRpgoyeqq5wZxbrLa7AU2N9eOZNfk94jRucibnFsx8MF13kGZNcpq1J4bOhnB3ooPHR6E6gKovNwfLJQQZX9pxVL0WH6qwUHI0EjKpJ__ewV--SUWZ6LOZhFYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر جنگ آمریکا: آماده‌ایم به جنگ برگردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/124352" target="_blank">📅 01:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124351">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQQTgYRbZhsi16_7tXEaU-TXVUwIVVwUi_sA9qLf_vYcx_p0nl-TnPt3HndI6CLib0ZiqQVATcRAzqxb4qJ6WvUp3N86r0K7aIvb-E3XPHVMH11584pabOQvGQkeH4O0uGBHqu2bNUW25t_YMS9uwhcoiBcSDxZ4WlRhwRoAepFaCK0oL12rSOL9DYd9Ll9wO7eDo1WINRVagSLU1koFQb8fxMKgGpp5b6bhy2gQPiQktVLc9H3CUPMQlQtZdtcenFL8_KTrc4dg2dVU_cStlPBmFJjFI07xcXIuAsg0lXQtg01imGun2ijyFRza-VLoZxQl3WIhTB-aPKj5Wt-veA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
4 سوخت رسان آمریکایی در نزدیکی مرزهای ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/124351" target="_blank">📅 01:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124350">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28a044344.mp4?token=Z_YhC7H8IR5O_Jw50-2arGjhjyE7IPEsPJ0HXoqkK_5IzZo1zVgAe1mIP9-PrSU9UULI7gPYtDJs2HJyyCpPZlqQ9t2Abi_lvx0Spe3M3Y_MIkvn7MX_FIUlzpGYZCWLaNTfaVtRPtA2yKU05JH1Sw_S-AwpeCmWvnOOItrF-aD8thFJ5GinOlliGMzNXz5lncD1Ck2nhgw45z4o6oJ31BuuR-pRzHcR9TS7c3EkifgmpbDxg_IdI50IX63hvgyl4HgdFhdMdnkLFkfnEUop_XyphDoIpgcP6-8URFAtQlaroZBm1IjpBZgqeho5wRP-h9g0Z72WUQrrcZs1FRE2EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28a044344.mp4?token=Z_YhC7H8IR5O_Jw50-2arGjhjyE7IPEsPJ0HXoqkK_5IzZo1zVgAe1mIP9-PrSU9UULI7gPYtDJs2HJyyCpPZlqQ9t2Abi_lvx0Spe3M3Y_MIkvn7MX_FIUlzpGYZCWLaNTfaVtRPtA2yKU05JH1Sw_S-AwpeCmWvnOOItrF-aD8thFJ5GinOlliGMzNXz5lncD1Ck2nhgw45z4o6oJ31BuuR-pRzHcR9TS7c3EkifgmpbDxg_IdI50IX63hvgyl4HgdFhdMdnkLFkfnEUop_XyphDoIpgcP6-8URFAtQlaroZBm1IjpBZgqeho5wRP-h9g0Z72WUQrrcZs1FRE2EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش تاج به ناامن بودن شهر تیخوانا: کاری به مواد فروش‌های مکزیک نداریم و نمی‌خواهیم هم اصلاحشان کنیم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/124350" target="_blank">📅 01:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm2uYev05GfDDzxioUFqf7jr6a5mYgwT5qVviEDbX_K06N-LpRe4x5JFS2zGNJNlt5GPlsfAYXOK92mz3NxjG9Aj_8TwvpjbqT_vAcD1_FMBwBJb92gVg3RFsynZ9XbpFWgVBPUGt5k6v_XZBESSNasqODe1HR9RyXH4hO5-VQXScGiw9FAPY3c6xuMsqEw73SNTobny6zwuX9ZBzW4j3p2ipPXyff35NogE-qgMQYUCuJx_DDoAp5s3zBOFdWVJeCUd2jWrWDHimFW8zaEXonR7PYjfqgfPeIoCHAeo_-OjaH97IDLByUQOLBsid0vLfyhtsxrP-GWb5Gk1RDZeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دوستان این تبلیغاتی که پائین کانال نمایش داده میشه توسط تلگرامه و دست ما نیست و  کلاهبرداری هست و فریب نخورید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/124349" target="_blank">📅 01:29 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kj40knS7bLdHJbecOoPjS2I-nxEN7DmmPBwFalxikkllGnGQUyKh6q56WFJwmcEploNkM7nVX9jiFB30xjOcnwYOH04qtnPJI9_rGKy6GjmxOMP1nwt0sdar6EROPC2TM7d8kjH-O1I7VafYTogPIjkvf1M_wJ987x4BKQPXZvFwaDfhCFhbvN3omr5MZg1YDV8C0cpmy9W4Dyz8ZfZXFlQQTjcJTHqiH7T61vvpmsiDNExc2YiPtqjmx_dyu6sptD68ybQd88S1-nydFIivIG2GOy2T9j4NMVxop2VwTJgyLcFFOovltvQVWJcaFB7ZMOCp2Ma8U812LBPJ4iGmhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: فعلا جنگ نمیکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/alonews/124348" target="_blank">📅 01:27 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYMXL-ekURemRlnwo2b-v7NCWYO-U7zFu9Q_uvHjLqscALqxwQbiG4q8_HaixE9h_LFKyYi0OIiUnNnx8oCWzVFFgaeGVUNAFrgHZqBMc5ZgS_oyx5Pj3fxndQOL0HgUk-1qNlXuAdz6c0d0V5S8BOxtYjq-_XZhq1228f5vBerm7ENnIWsIjKbNKovyYGlM4zJorMsi1AYhu9WVGAE1LxNjHRtdi61UNFuvE8_UhhQ56A9-55IWpGnkzaI6sY1dLCiqXr6nf5EtSqcPa25uP2CRPmsTcyH52OQGM5ViSFvgJe0aUCDRFZacg_o-QMwO_AfOcl6-BBsmTjcSPoz1AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رئیس جمهور ترامپ:
امروز با بی بی نتانیاهو صحبت کردم و از او خواستم که به حمله بزرگی به بیروت لبنان نپردازد. اون سربازاش رو برگردوند ممنون بیبی
🔴
من همچنین با نمایندگان رهبران حزب الله صحبت کردم ، و آنها موافقت کردند که تیراندازی به اسرائیل و سربازانش را متوقف کنند. به همین ترتیب ، اسرائیل موافقت کرد که به آنها شلیک نکند.
🔴
بذار ببینیم چقدر طول میکشه-امیدوارم برای ابدیت باشه!‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/124347" target="_blank">📅 01:25 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c51d90e9c.mp4?token=GDJDXKOKW5uUu5CkqE2ycjhuJbJcZNpy6NDzXcr1XsbdGLmSlcp-5gvvnaRSO2YccWFOcUVHRM0W1hjPnF1spPkE1gZ9npiBCivrThbQKUE6E5gZUhIrnQh_DIOsxJCxWtrLxoEBpok_yJIl_NR4Kjl-cIKywfPBeSNqibpXvDh3qhkCh-Uk6PFM3VOMxTkY3w8tF2gxvExsdl1zvrXXJK9aflzSdELNKQZ65bOWjNQgRBk-w4_l4VicD97xuTxBWYialJMImgn4M9UEVvhiHiDCSaIR8KSANJuQex1P955Cr1HyZNkf9aA2fPJ8nugsxCICMwzXJCaUtFixgDrUdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c51d90e9c.mp4?token=GDJDXKOKW5uUu5CkqE2ycjhuJbJcZNpy6NDzXcr1XsbdGLmSlcp-5gvvnaRSO2YccWFOcUVHRM0W1hjPnF1spPkE1gZ9npiBCivrThbQKUE6E5gZUhIrnQh_DIOsxJCxWtrLxoEBpok_yJIl_NR4Kjl-cIKywfPBeSNqibpXvDh3qhkCh-Uk6PFM3VOMxTkY3w8tF2gxvExsdl1zvrXXJK9aflzSdELNKQZ65bOWjNQgRBk-w4_l4VicD97xuTxBWYialJMImgn4M9UEVvhiHiDCSaIR8KSANJuQex1P955Cr1HyZNkf9aA2fPJ8nugsxCICMwzXJCaUtFixgDrUdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم وایرال شده از بلاگر روسی در کافه‌ای زیر زمینی در تهران با حضور جواد یساری
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/alonews/124346" target="_blank">📅 01:23 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1MUm4b4jxnDsrKXkIwZXa-KfuPhVxg6okIscRdQvz7mTqRUgprWdctTAlDHAisqGmKxKShHLU4nOO0cojnaGDGK8VBRT_RDPoYH5YmJVKgDqdc_ehdU9qhKxrK7JiztAYPpEBeHF_Mk2KCh8AV_dZR06bCaD4ETzzxA12dlvrrbeos5iR7N75VuHnRbZmVJS_pnLV_khuFyjmXJV0iSSt_s1amFKd33gju3JZlyUWvDaMuub8TDtHkRL-8xxd3u7VuMBzW52kQfvptrm_3utaRm8Jfj8D0l1ER0fTQhcYX2ZsqxX30kOneXMb2yKFQxrWtDjiJb35BMXYAHyiyrIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qf8bcBLKsKCAqRvg6PD_eVJksaggsaqpoPD4UsmhXJNTycoaXDSR8bFuvw8BQ8BDcC4wMMGEj6jsSFUPNHxjVJmjlULDBLJeYmeMZdB2WbHPo2Wgh0UFpBj6TspIOyFCjrB2szIp_mpl4U1_mUgyzJI6RmWYlmceUQBkmNtoHO-c1saUui6ixo0Edk1AyVyzniC31ygAJiltnlHcGX1Xpe3QYXEuGXkyaaJegSEJHl_hoGdfhi58rf1e7PGNhc8wc7dxh1jlIco4RML_SHUiKcxHo1b7W_jZEjOnQcxoKnrBdS2SBJ3o-16jFlWBXd-fyrFymcXPXo5wG55prShzWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💔
جاویدنام حامد بیابانی، ۲۴ ساله، اصالتاً کُردِ کرمانشاه و ساکن پرند بود.
🔴
شب ۱۸ دی، در تهرانپارس، وقتی دوست صمیمی‌اش جاویدنام علیرضا صحت‌بخش هدف گلوله قرار گرفت، حامد خودش را به خطر انداخت و به سمت او رفت تا کمکش کند و او را از محل تیراندازی عقب بکشد؛ اما در همان لحظه خودش هم هدف گلوله جنگی قرار گرفت. گلوله به گلوی حامد خورد و جانش را گرفت.
🔴
خانواده‌اش تصمیم گرفتند پیکر او را به سنقر، از توابع کرمانشاه، ببرند؛ شهری که ریشه و اصالت مادری‌شان به آنجا بازمی‌گشت.
🔴
حامد از آن آدم‌هایی بود که عاشق زندگی‌اند؛ اجتماعی، شوخ‌طبع، پرانرژی و سرشار از شور. هر جا می‌رفت، فضا را زنده می‌کرد، جمع را به هیجان می‌آورد و لبخند روی لب‌ها می‌نشاند.
🔴
حامد بیابانی و علیرضا صحت‌بخش دو رفیق صمیمی بودند؛ هر دو ۲۴ ساله، هر دو ساکن پرند، و هر دو در تهرانپارس با گلوله جنگی کشته شدند؛ علیرضا با گلوله‌ای به قلب و حامد وقتی برای کمک به او رفت، با گلوله‌ای به گلو.
🤔
عرزشی حرام زاده، اینها تروریست بودن که به قتل رسوندینشون؟ ادعای عدل علی هم دارید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/124344" target="_blank">📅 01:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
باقر:
ایران نه تنها روند گفتگو را متوقف خواهد کرد بلکه اگر اسرائیل حملات در لبنان را متوقف نکند،
مستقیماً به اسرائیل حمله خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/124343" target="_blank">📅 01:19 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
ترامپ: مردم ایران مرا دوست دارند زیرا رژیم را عوض کردم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/124342" target="_blank">📅 01:17 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ: «کار ساده‌ای نیست. شما درباره یک کشور واقعاً بزرگ صحبت می‌کنید، آنها یک کشور بسیار بزرگ هستند که می‌خواهد توافق کند. خصومت فوق‌العاده‌ای وجود دارد، واقعاً.»
🔴
او ادامه داد: «بنابراین این کار برای آنها آسان نیست. در واقع از منظر ما هم آسان نیست. اما ما داریم آنچه را که نیاز داریم به دست می‌آوریم.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/124341" target="_blank">📅 01:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ در گفت‌وگو با ای‌بی‌سی:
من هنوز این توافق را تأیید نکرده‌ام و هنوز چند نکته دیگر باقی مانده است که باید تضمین شود.
🔴
من هنوز با این توافق موافقت نکرده‌ام و هنوز باید چند امتیاز دیگر بگیرم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/124340" target="_blank">📅 01:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ترامپ: شاید این هفته با ایران به توافق برسیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/124339" target="_blank">📅 01:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ:
امروز یک مشکل کوچک پیش آمد، ایرانی‌ها از حملات اسرائیل به لبنان ناراحت بودند.
🔴
بنابراین من با حزب‌الله صحبت کردم و گفتم تیراندازی نکنید، و با بی‌بی (نتانیاهو) صحبت کردم و گفتم تیراندازی نکنید، و هر دو تیراندازی به سمت یکدیگر را متوقف کردند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/124338" target="_blank">📅 01:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
ترامپ: صلح با ایران شاید حتی بهتر از پیروزی نظامی باشد‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/alonews/124337" target="_blank">📅 01:05 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فرانسه: ورود نظامی اسرائیل به داخل لبنان یک اشتباه استراتژیک است
🔴
«ژروم بونافو»، نماینده فرانسه در جلسه شورای امنیت درباره لبنان گفت:
🔴
ما خواستار برگزاری این نشست اضطراری در پاسخ به تشدید تنش‌های بزرگ اسرائیل در لبنان شدیم.
🔴
هیچ چیز نمی‌تواند ادامه عملیات نظامی اسرائیل در لبنان را توجیه کند.
🔴
نفوذ رو به افزایش اسرائیل به داخل خاک لبنان، یک اشتباه استراتژیک بزرگ محسوب می‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/124336" target="_blank">📅 00:58 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZqJ2qeuU1n6rjeUYJ1UmpQqm2YPYGGfZ07RXR22T94XGPt55CgZ4d9KO_iE4XC6r5IMcz30hiBa8ZrGzmHxa6ZlIW7jrjaJEujo9cXNbWjPDndLjbWqiQ1W9m5fSW0GvLFXH-LWRFsWGqFkN-Xq82_u215Z6-TaA7o2Cshtt4xCOjG69k-C2g4HQgoMrtR7O0JKId4sSiU9isEIZvt9FU8ErUt8ULejEv_Qj7sAC77gij87xNQigG-r6JoWy5eON0bk8QK2eY3CnCGzUtJ1KmDX8l28n1CiAIkGUKlMytHM6I0AwVXI0jopVu6MN1XdSKVWM55BGdwLpZUGM2cAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید کاخ سفید
:
«به ترامپ اعتماد کنید.
فقط بنشینید و آرام باشید، در نهایت همه‌چیز خوب پیش خواهد رفت — همیشه همین‌طور بوده است!»
— رئیس‌جمهور دونالد جی. ترامپ
🇺🇸
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/alonews/124335" target="_blank">📅 00:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1207bac6cf.mp4?token=NfP6hkiZFlFPy2Nlr1QAIh6cdvc2oPlnHkDMxPx3xBxNfT4_F8aOAjkyeLTqUarHil7hsy04N_IrXMTmab8ZfdzLYwttCmTWaWhHLfDUg0g_fA9c6CzLrikcJNl0agDp39ppfr1TXTzBdeEeKhGbSm5mD5XkH-6Uw_mPOP8yn4UAcIuajLXRvOGnpUQySTVfIbzPt2EYqWswZK6r30txtxuPjgG4qsRrkjvrzLCdCbLDJtfVXeX06VG-E-prk12cICoq-ztiBHUsepn4oOu8XZZ1CpQPCrElfRg2gWUDMa9rSbMIw-GLY-GLP7P14lrveM9CdZSAd8MUxBtdvw4y8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1207bac6cf.mp4?token=NfP6hkiZFlFPy2Nlr1QAIh6cdvc2oPlnHkDMxPx3xBxNfT4_F8aOAjkyeLTqUarHil7hsy04N_IrXMTmab8ZfdzLYwttCmTWaWhHLfDUg0g_fA9c6CzLrikcJNl0agDp39ppfr1TXTzBdeEeKhGbSm5mD5XkH-6Uw_mPOP8yn4UAcIuajLXRvOGnpUQySTVfIbzPt2EYqWswZK6r30txtxuPjgG4qsRrkjvrzLCdCbLDJtfVXeX06VG-E-prk12cICoq-ztiBHUsepn4oOu8XZZ1CpQPCrElfRg2gWUDMa9rSbMIw-GLY-GLP7P14lrveM9CdZSAd8MUxBtdvw4y8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
@AloSport</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/124334" target="_blank">📅 00:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124333">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca354355b.mp4?token=ginlYqx7Sot0XbKzhN5bEJdhudkneOMRQJ5wz99ZxlVFNdlG6nJYLPKS6iD6fEPgKCHIHGAO70E0lTz1hHcJpH4n_V8qe1SWsYIeEk5oF9_Lov7-VOqv-_b981ENv7iIBirNB2n23LVqosUI4NRTQ0o7k04GxD_HDf52zvKJ4NVoO6pMbRpBveEq9EbhD0ysysqbMWXPMlV66Po9Mu7tCcEbzANIuXJycgGGr_H8f23H3a64DnWgQFHQVw9PMvpGb_JhlhcALQ5J3mF4gi8OPmRVHGMYOgILGuGK4ubUh5o0IIclHd-e3v0OVzLYwbJE9BoyYN94iTUHGiOkxDri6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca354355b.mp4?token=ginlYqx7Sot0XbKzhN5bEJdhudkneOMRQJ5wz99ZxlVFNdlG6nJYLPKS6iD6fEPgKCHIHGAO70E0lTz1hHcJpH4n_V8qe1SWsYIeEk5oF9_Lov7-VOqv-_b981ENv7iIBirNB2n23LVqosUI4NRTQ0o7k04GxD_HDf52zvKJ4NVoO6pMbRpBveEq9EbhD0ysysqbMWXPMlV66Po9Mu7tCcEbzANIuXJycgGGr_H8f23H3a64DnWgQFHQVw9PMvpGb_JhlhcALQ5J3mF4gi8OPmRVHGMYOgILGuGK4ubUh5o0IIclHd-e3v0OVzLYwbJE9BoyYN94iTUHGiOkxDri6TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اگه واستون سواله که موج انفجارِ نزدیک چه شکلیه؛
🔴
این ویدئو از حمله به تهران رو تا آخر ببینید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/124333" target="_blank">📅 00:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_5WclMqKjIONSmj-Fe9yWqxA9puwIvvRl4VqjrOF7KqLx2uoprGFk5SU7fpZxCxXNEGbP7PE20g6AX0v0T2Tf67fkboiab4S81Y048xp5XzO5JGwwUBH1dQ98IgaAGm7ctAwi0kj9TaD_N9bhqnQne8gTFUWDTmQ-bCmcNb30tNHs3QOwKJCnymMBXytG09kxD5-RZAV_eSg3aqDs027Ytf8KfennK9SCxY4kTEJFtT2AAl4G_0LImv5RARYSwStT8DKOeTK_cZI-6E5WESUeEktuxU3yV3rfUWsYC0ENP3RPan-BvcBaaZUlQk8A0sETCt6v1xcFVHObuH5poN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NDlL8MQlgdvgsQ_IaILLm6Pr3oOmRqAr8GxgAgteAX-ALnrp02fR5T6TUlG4l-arbg8QVFe1OIU3FjPhOC5UYokOEOWgAjo3nRHFz1T9bQbHdT9hkS7fqZrFNxfVnpgyPe74NSReEEE48_hm9OWcyUlxR9a2gpuGfI5RqmeG4XJEjWfo5DGGroyfxB2RWUsXGw-HBUKkJ7uWdta2r9h3afyfwkClBM0BqEV8lDF2PpPnVcxWLelI5lciHt92nbi2Mz-knCC-CA2xSetALCCvrO-VmY8URXDV6Bk_FN3oFtzhjijhB8tAheGFBACMq9Oy_t6RglwDQHCJW5AH3HY4Mw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💔
جاوید نام سید داوود امامی 39 ساله، دارای دو فرزند، از شهر میبد.
🔴
هیچ کجا اسمی از این جوان که در 39 سالگی پیر و جاویدنام شد نیومده.
🔴
رنج زندگی رو تو چهرش میبینید؟ هم وطن ماست
🤔
عرزشی حرام زاده، این تروریست بود که با اسلحه به قتل رسوندینش؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/124331" target="_blank">📅 00:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfb6BS8JcIrUoI-OldO_vvTcXEyHbt368MW8saDEpGarcXQIx16ejOZKRExEkqxlWWrP7bixZNPtuvZTQGhdeKBWXhtBnz791kmUgxXl9C_Eym5qKw1v_lLF7E2Ngq67dvSVzy7rgaM2BQuSbf0aDTlgP-FWdxxsb1B6r2UWx9REbeWzh_LuJ0Q1FkRK2e-BIKzwPIwee9CrG5xVj4iMy4pJkNr4jzwTn_j5AfFDdOOQGj0qn6cLbYdVdnU8hJp29HkkcSu_gxKS4gkM-1WCXZG6ZCBw_yDK6Dbv2DEP9RgaUHCRg2SCe5huaNTniO4EUsgjbhvLFSgc8lLLGqaxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: جنگ نمیشه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/124330" target="_blank">📅 00:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sEM4PgScoMLOdGoeNetWPu4Lv--3-0-FkmhFg3XsVWNy5tsRMee0TsFXmlHUK_xoZXXa2XKJnSJ0PUEqKJmU7rX3flxfdZjmrtuRrWkfhDSUKouYE7vld0m1Cm6uNyKcLttb3YfdKkqca9SYvURH3vm-2QuuJhAI1HQqfBcREPMluXC2pApfX2kXYx5xIKABWeTuwg9ZRGLghOU7AcqKLhA9FQA2zPD6ld7u_YwwT0UjDJhfhjUmUkmk72-tzA8ww5iTmcuRkp3FkqqqtwQ4OtWOJqPZ5CSjVsL2P8J8CTOEJhTMwhWDr17aHzx2gQ-e_oN0VIAsSF5ISeMbWgtJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JH1lHvI1mZ4wFs_9QQ41sei_rCQhsGIZJ0vcuSg9PRMmaGCnqYODuxYU2GJIwuklkCesLfZ26Fw2gg_RolCIuOWVyB3jAMpUh6ga0Q5mEs44WzKXlnt-Td0tYqaZu0d6c5NufotYc8tv6OGKouibgZ8W4EqlpPo1P8MJJW_32Ol4zP7OWxWT5-ePg5Pz7RNNTwIhfZtjw0CiuUQ1JNw6KkMTG7bsyjqZymnyxG9xJgemqLUEPkqT8waI_JkeBM_lYGW1HuBq5DAj7l1_U03UXlu7oeN1R0RDF-Jgkg2iSSqwmevHeQmsY3H4m-yr67Te_yAReFPa5Q4heTeKsV1hJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
سپاه قم اومد یه بمب عمل نکرده از جنگ رو خنثی کنه و ۲سپاهی بر اثر انفجار کشته شدن و بمب خنثی شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/124328" target="_blank">📅 00:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_9RKq43TYr0IQjFgC6z-ENmpqB9-kAA4__bwoqUV1LtfJY6lRJHC7NhS6DDZWFo8vCsZF502z6madm3iJYauCqW7nDSOjJcKqX6a2qHA8VdHCX6vKETN6EnNT_T4MUQgwlXeT-ABnasrIct6k7D-D1a50JUnnnyejSKvPsiOmiXHEowoSUmsjaIjau0qDzVOGjGXJMHtF5Cf3ettMmQmJ-2JloNEDVfag4H_NzEgYgBkrA8PTBDlTV0FjVoc8djMlwwW2cp2XfrIyU2zmfVjPGu9BRSmODnJZqODaMTRpq7QXWjlZHZJ6fZvq7aGiU-KSubnrKoyenDRA7G9uQBhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حزب‌الله چندین راکت به شمال اسرائیل شلیک کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/alonews/124327" target="_blank">📅 00:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/124326" target="_blank">📅 00:02 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
فووووووووووووووووووووووووری</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/alonews/124325" target="_blank">📅 00:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نماینده حزب‌الله در پارلمان لبنان اعلام کرد که پیشنهاد آمریکا مبنی بر توقف عملیات مقاومت در مقابل عدم حمله اسرائیل به ضاحیه جنوبی بیروت غیرقابل قبول است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/alonews/124324" target="_blank">📅 23:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124323">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
سپاه قم اومد یه بمب عمل نکرده از جنگ رو خنثی کنه و ۲سپاهی بر اثر انفجار کشته شدن و بمب خنثی شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/124323" target="_blank">📅 23:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🔴
فوری/رئیس کمیسیون امنیت ملی مجلس: اگر جنگ در لبنان به صورت کامل متوقف نشود، روزهای تاریکی در انتظار آمریکا و اسرائیل خواهد بود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/124322" target="_blank">📅 23:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124320">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YwPcGSIVJHUQA_TU9CqNk2jMQ0ohbP3N_HZdDtPZyvExy7J9Ia3rm-ZKV3qsvvNYy_Xu0mOaCb-Gh7kw2H9xjBFsnuVWRvtOHcu676U3GvoMQj-4A7_814IXJATHCE1HhC6z9JYyHkOz_Gu03VVKQWPsHwVhI-MPTvmfZI5Qtvc-ShPwVIggacMqmkQtdvfk-XYBD6Yviru4SJtuK45-7hUBJkqshmAk7cxAIUA711LY1jUbFCoiBbCr5Ok2wHts5XQ7TGeTpy2GUWv0p988TkrIEcWcZam5vg0GBFNIvYViVGoEVxnbGhb2PPAzqfUj53Yt227QhzrJvnyNkA7OmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-3kX-AP871xWq1L__5FuabEw-utVltcEuURv6GY_7f3o-jgJWLbbNz7J51kJtJehQexwJvdT9NywqRoDieXusuJaSvAIIITF7UiQReRrZLAhaGxD02__EDTHCLaXWe_OVn8aomLGDqIZRYMAvrVQ2Aqu_uURL5ag798tqGWV8M0xC8VPuU986Lgl6fuL7rlsApy8xXs1-cOV7qz5OQ9qFCpGm3OMobY7ReSVmFtiIGlEgLo07U2dITGn-LPRKNgGSIb-ZK1XnLVmGKcRa-v2CUwV-rNV_YnIHZ0GJTnascCTANu5ojkfMJhPQuJnOq7_HFt3hqIN1rJ4bT0dLLANA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
جنگنده‌های اسرائیلی به حملات هوایی در جنوب لبنان ادامه می‌دهند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/124320" target="_blank">📅 23:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124319">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">📱
لطفا توییتر الونیوز رو دنبال کنین
🔴
پست های انگلیسی در رابطه با جنایت های حکومت به انگلیسی نوشته شده و افراد مهم منشن و هشتگ های مهم قرار داده شده.
🔴
ریپست کنین. مهمترین کمک این روزها جلوگیری از پروپاگاندا حکومت علیه این قتل عام مردم هستش. خونشون نباید پایمال…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/124319" target="_blank">📅 23:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124318">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17ae224db9.mp4?token=v8rdTbbKlaw7uzTbnT49mysXxqohNp6NfooLPEbmFh26loWF4hoXKybN3o_6HRXuOwLtWHqtH3PYgQOEzr_AhwLePKKYqNQq_s93p-4S58_DIKoatyG6b1OVd7vFH2nJN7s8Xx3mPBufLAkCyfKwehH9roIFNRB0qfNDgAKXdRleBPhewZIb8fUh9dAAJJd1hsmFaZIUpEw4HPJk4VGMx3sDYf50myPDqODJAwmMw68JJESMZSjoH2GgomStxABqRJFppmbkn2Oiosk49QufbSkXgOCJXKNjydhVB8QzMr_NhyJQfh95yyQUDbDb4CVec4PbsERpqsM1JxkqQUTzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17ae224db9.mp4?token=v8rdTbbKlaw7uzTbnT49mysXxqohNp6NfooLPEbmFh26loWF4hoXKybN3o_6HRXuOwLtWHqtH3PYgQOEzr_AhwLePKKYqNQq_s93p-4S58_DIKoatyG6b1OVd7vFH2nJN7s8Xx3mPBufLAkCyfKwehH9roIFNRB0qfNDgAKXdRleBPhewZIb8fUh9dAAJJd1hsmFaZIUpEw4HPJk4VGMx3sDYf50myPDqODJAwmMw68JJESMZSjoH2GgomStxABqRJFppmbkn2Oiosk49QufbSkXgOCJXKNjydhVB8QzMr_NhyJQfh95yyQUDbDb4CVec4PbsERpqsM1JxkqQUTzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روابط عمومی سپاه: در پی حمله ارتش امریکا به کشتی ایرانی  " لیان استار"  در محدوده دریای عمان،  نیروی دریایی سپاه طی یک عملیات مقابله به مثل، کشتی  "msc. sariska" با مالکیت دشمن امریکایی / اسرائیلی را  با موشک کروز مورد هدف قرار داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/124318" target="_blank">📅 23:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124317">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5Xdr6a-WJZ5lKMISMvHMzhgua8kYbf24TVlcRJtNRFta1N1NyM5xjXwu-wP0J3vHz0hp36oWtro_4LSCyqX9SPigiwZWaymdSmpsyKnSQm7W8qEwDllfFv6Ox2sVuhlbB9u9dcdoQd6acrZaNgXNUihT__v1LupJZq41HligwM40niJ4UclQKWQfMtqyIbcBnhKOcxYXYT8C68Ex4Ev6rV0gJheUdTpn7-wwb8YHnefzXOXyprAdOzIBz5JkNprD2wkW8LvTNUydA0nKOg6k7vECkl7WgLN4QEtMZq2KnBs81cg0CTmywHHGWtDevNL6wd8TTpvCeXg1ki-JXeg6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۴ سوخت رسان آمریکایی در نزدیکی مرزهای ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/124317" target="_blank">📅 23:36 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124316">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtLNieKzAWj5TqlWh3mLD8xam2tMoinI-ZPlGNFFiN1GZZsWsmvt6CprA2w4k27gBRC7RpVobO-cQSqunmeBj9DaLewAB4q4-ekyoUdgPueb9te1wg55tofCL5Gcs8oxve87O7oqRnj7NMX4MVem_ajP88uIGZTyIVFy0B_uw_qmgLJLXft_NDQNIu0PnzPK2AI_NjsgJaNG5-kTYh_pSV7cNBKQteD5SPtFjvr9eOuMapCYGI3JBprnx3uw8ayRabxPsteaVqRY4KGXphYzM81odKEViPxbkveZHTrlaoqR01Di8kPhPC0jr_hL4rU0rf-7Wf1qsGwg2XzDYgP90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت استثنایی و کیفیت بالا
❤️
تا ۱۲ ظهر فردا تخفیف جشنواره هم گذاشتن
❤️
دارای لینک سابسکریشن جهت دیدن حجم و کنترل مصرف
✅
بدون قطعی
✅
بدون محدودیت کاربر و زمان
✅
جمینایو چت جی بی تی و... کامل اوکیه با سرورامون
✅
🏪
پشتیبانی کامل
✅
شروع فعالیت از سال 2022
✅
پرداخت ریالی
✅
از رباتمونم میتونید تهیه کنید
💞
👇
✅
➡️
@Napsternetiran_bot
☑️
ضریب و این چیزا ندارن و تا آخرین مگابایت برای پشتیبانیش درختمتیم
🥂
چنل کانالمون
👇
📣
➡️
@Napsternetvirani
☑️</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/124316" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124315">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
هم اکنون موج جدید حملات اسرائیل به جنوب لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/124315" target="_blank">📅 23:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124313">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
یک منبع مسئول در فرودگاه بین‌المللی رفیق حریری بیروت اعلام کرد که پروازها در این فرودگاه جریان دارد و این فرودگاه تعطیل نشده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/124313" target="_blank">📅 23:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-124312">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
نخستین پرواز شرکت روسی آئروفلوت از مسکو به مقصد دوبی در امارات متحده عربی امروز دوشنبه پس از سه ماه وقفه انجام شد.
🔴
‌ این شرکت هواپیمایی اعلام کرده است که روزانه یک پرواز از مبدأ مسکو به مقصد دوبی از امروز یکم ژوئن ۲۰۲۶ میلادی (۱۱ خرداد ۱۴۰۵) انجام خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/124312" target="_blank">📅 23:17 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
