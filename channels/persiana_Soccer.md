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
<img src="https://cdn4.telesco.pe/file/l0oCevYuAzu8-6evub6TXK_nCnwt-wU05fsP3PBBF6K5Qx4mntzGR6pQlHpTd-Ghb6AixaLqtLNchxwmp0NFA8y3wt7j_1p4sFU6CNbZhs6TKo7G0JHYzV4-rQe5--X2S-tsu8_ISxZwGG6pL-ts6HfnNZCxHMS2iqkz5ZdZUuHnrb96YX4mdj4BEJZGMlOvzQ75uVF17s6QIqIL4HSmXLt4esf14-j1ZlKjoYyRQRmnF41KOjiqnHjlNYRwfvTDXzpTI1pZRp7IhToU9CvLXTKGrvegZkEPJIFxnZW_IWGDSY1UXlpsJwbDUJ6QykCez0604nZy3Fx6_9-hI12Jzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 502K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 07:40:32</div>
<hr>

<div class="tg-post" id="msg-29920">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/29920" target="_blank">📅 01:53 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29918">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4OucnB1s5tYNz19miA2YEa8D_1s3eKyK0cj4n5qQOoyjpEkVzpdqPZ2IyXYv1_dwb-ylTlXsHyNtHNk3ecwHh9ANByd1E5EZWr_eUpp4RbCCu3OTdvcOpWEyUGM-WUmKEoYdCdd-0OVEI7h8MZRheroe92aKKv6i5ZIlvRtighmkVqGmOCf_nXgoM0Wk0cGzgPbOrd0WoNTuSH8Xh2RdfB4Fw11uAyYR1e_13x8lmnSY3Wi1-IaZDQQo2hzkSWFI_KDufLs1AURgC1TNNGpJGqhRAAzajEhdpZ8wxULNRoeSlTd_WmmOwO-Tx0QKYoA4Xha-QG7aeZQKZzzRpgWAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌ امروز
؛ رویارویی صیادمنش و لخ‌پوزنان با کریستال پالاس در هفته اول لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/29918" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29917">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUO7GFfy85KiSmGFuIHH_GLqoy6WU_pQo6z3aX2DpjqMY4ZcGqY69Iwk3Dg3PUPniOnAPghKHQwCO3fqTP9gRMrbIQjQVfllHBV0spe3oF6v8tN4XXjNWia8fhvUOQme6BlOKjjYVqTEvP1EQXobB89dX-Xzi6PCDCpETahIxqpr8mDND3rw9Rl0I_CTgQFLYHDACBbNcqNKe_YsKBzlQG4xOC1b_ZNHllUtIRhfn6NfpNMjUb1hT0tl4LUZ1tctYLhfShixMCV0YHU8pAkboppAPdVHsIp1SZ51XgDSPShvygUo_YkAyoewVzFiKgSTMSGHB7b5MzDZfblyEy70kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازکامبک‌برایتون برابر یاران کریک تا برد هفت‌گله بارسایی‌ها و تثبیت صدرنشینی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/29917" target="_blank">📅 01:43 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29915">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ne4jxWtkBQKgtGN8Jt8ogRjyFvRjuRroO57LjuHFfDxkIBh74dax4OtpCYqRBhVgmfhJmT427nEuJalLeCcS0kES0zA5Bz15TaF9ZBdnCcbmRji9pfrZQ9WgURZQ0ybLarGBPr2PkECZ7C7DsxbxB8OhhZYfv7DvdIsrqIA8jVy5SB3m6IHYBlSlVYv2oE7RdA8guBTxX42TSfiTHg93EdUAOyKtaF_1Vqds2m9NHC85PZLSA7UjimWfpj39eqCZJs-DaOxJdahTNatsb9HqmuOSGDK2fo4trm1HxdXurSUYDOXYFfKV_K5cAxqqQ2HEWYlklbIVokO_U38oNdHKlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/edqbb0ODooBJkCZZnwRZ4mZfKufDrZdohHEuye0xxsVnlx1MqSi-k8aYFWQN5st37LoMw1gvtz9wCQoFWUtXCMwF4V8I8mMjHPTLZzmCQWs53vrnxwjJ85uGaefSGs8xj24CTysTz6mTSwSaG48vtTY9yYIHA3NRchcg_6f6PbuvqYXGj1zihcXYTwceJeNNKRqQWnA1ivz77m_SplQbfeStRjwyimdzJS3klZ-QWqf1NABtyPV2EQ2eURumUEaNGdiF85t7rG7suqUf0BN1ugJ8alK_RE3mS_rGfNadTC_EBkwCXzmy3t0YajNlRWnNODiO7rGt5GOl1mEnLuWZTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/29915" target="_blank">📅 01:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29914">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ELhHKFzxT4MC5W8ASgvIwddzQhIiVYCOjGRYijkBqa5MseymtPVotDKrDLKCH90fQrIZfJmjEBAEAkPLsDl8dSaVKyQqQYT5Ivyvu4mVUxHxuyAC1ml8IcV1B7uEAzeQUQyQDL-xSJqpqEjEh7nvhlkgOzJuOczPZfHK9VbIY-UnNphQMECPtxZnryhCqAjZGbqNx24cmrGuBcu4lUsUhWyLP4lyb0jBYSBnNPuYa7OKImjCxWiPZo3sliiHOq-lwNrf8jLCvZPTDV7Q4uyXuqC8eD-WhgxjdJbHmD91sWsQk0YmxDSsC4I3ryfPyyeAYXT04qeepkLgM6NOjkfmMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
در هفته‌ششم‌ لالیگا؛ بارسلوناِ فلیک با نتیجه درخشان و پرگل هفت بر دو راسینگ سانتاندر در هم کوبید؛ 6 مسابقه، 6 پیروزی، 34 گل زده، 7 گل زده؛ عملکرد استثنایی شاگردان فلیک در این فصل.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/29914" target="_blank">📅 01:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29913">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv2e6-NWZ6ySH4ZD3hdCuIRPOwOsg2-xISeboE7G-8aakNMq3XQlezJBEvBc5Q2DAZ2DQFzJ_GNkMb24UQ7OqU7aMQq9ohDVwQc4rB2wbNNLsSt22-eFp73j0BgFuWoY5nTlXUYjUbTSUT-dSx7Z0W2HMHKpx2dtBSHKGn64lQKi7EMHP65Kpf1zm9mRysrGHoeh_uVYHwQxXJUDd6WwmZj946Ss-c-3mF6RzKyllJk1e8mtyDmSc1MK4ovBnLnpoqaAK1V2vmpdrYzRz_GWrXtw1AZmqzDptom0LzouDppphMHNOOFl67M9FiITUdw1m3GC3NnBw4sZE6lepoEtZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/29913" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29912">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLxQTddycIBl7lKbDdbXX-t5iqzXM_hJCW-ktELwxQBWLicLrO_hotLL95R-X01KeelXNIm5N1cAmoi2R0JpnvElVhxnYB640klio9nv7Eip2bkY70wKMbwATxBE_Z02GQPc5g82_0qyqEQvuKWuCvUgu04whnW7IntnwRVe-wyF98hQbRiYB0IUwWzBDMEG63d4dmjk6snbwwRoNPTkiidkRQkj19Dfda_XV3nfAC5XarHVw8r8-pXxiQeEsrFIU8bmODDkAd3VEY4-6v3ctljLjLzJFMaHWstxGBLVxu5MIDUChKMgN4XM4ePfwyNg1JQdnsZc-RpURp5moev8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
دبل تماشایی ژائو کانسلو در زدن سوپرگل در مسابقه امشب بارسلونا با راسینگ سانتاندر در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/persiana_Soccer/29912" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29911">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5atm9thW7z004iK_CpcD0EFuLK_nRDIh27NzP-ayoUc51Zu9g-HArJSFGx0T-BZie7OKNm8Lwjv8NU8mjxKF4X9Xez-gVVSnIqOwZO74RurPds1mjujkCwnLblKrfAP1lSoKveoMyyPmuLeAij0021Jr150PzlU11cksDOcc_tK-VXDQ-PzvNFZAsAVlFfr63XjVXhqUBSx0V7uOjity7SdWSkYKZGBcbyYdR3_DUB7SheSmhGa3HODL8h79EqvW7zpwBOMvqmSiO8Ub-bqmBxG_S85FDU2A5V6y924UaGVfv2feOA74VSW4IzsV4noiPIyEZ1r-iZ1ArtY2hjvdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎉
با بانس خوش‌آمدگویی ورزشی، شروع قدرتمندی در پین باهیس داشته باشید
🆕
کاربران جدید می‌توانند برای چهار واریز اول خود، بانس‌ دریافت کرده و از آن برای تجربه‌ای حرفه‌ای در بازی‌های ورزشی بهره‌مند شوند
💥
واریز اول 100% تا سقف 80 میلیون ریال
💥
واریز دوم 75% تا سقف 60 میلیون ریال
💥
واریز سوم 50% تا سقف 40 میلیون ریال
💥
واریز چهارم 25% تا سقف 20 میلیون ریال
☄️
برداشت راحت و سریع تاسقف1000دلاردرروز
🔝
تبدیل دلار با نرخ ثابت 2.600.000 ریال
💰
متدهای پرداختی ریالی و دلاری اتوماتیک
⚠️
این بانس تنها یک‌بار برای هر کاربر قابل استفاده است
🔝
فرصت‌های جذاب در انتظار شماست
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
p25
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/29911" target="_blank">📅 01:06 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29909">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nye-_8VWXAOIYrIUyzI99FMtfEPhZYXBtKKJN4VNttoos14yv5xp-MP0qaYkicet5_n8uivMTCs66Bjef81VfKV4glCQshoXhkDW-UzSrwvBldyy7r8bfCXV72RLsFfuWDcqHUT1oaiK0U4piIjcvqDvxgneQK0PPnRjvH3Fb4x3JmkDm-Xxi3pNmtnXFS_Mf92JX6f4Rml-entdjH0Ldhu7yIfAPWk5qaMZO94PGbzuL7OnhmNk_W9wsG3RfacvvpueCs62h2jGnj4CvRwdElHbRkmkp1KZTCHNzK6e2ik-PomFGrbIjFxWg9-LHRUdO8-ynxWIuGCKn5-cO6Ix3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l2W4i-KgQofWSaFRsGaa3Gp9ixdpjDxgzz4ZkHtR-8-H-JG41XzY2G_X0CY14a7eQWKNYOljezmdYtrNrJcr8HxbxdJbw2Swd2pgP-Zl2Gw2n3hMgmeDd_lr5TXEX5F8kz1ZA3PgB9SUgpaEVEIElOobJmiYLYw--zsvdfp91ie4U2oDET5TjmBFsVTo6zBljESvd6ikXtnmTpQN0f3uApQ5e1qcwQDHdFMa36kmWd8zyl6NRB4QYiAnbBJ4KoGJqb3cMm3VqgKE_ev3mZynFevQsqfTDRcuWXLyBtqB6nZSQhgcGGY-qIWj5miKxDMss0J2KQcuSvvw9U_-Y01DAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
نتیجه دو دیدارمهم‌امشب؛
حذف عجیب و دور از انتظار شیاطین سرخ از جام اتحادیه با طعم کامبک خوردن و شکست میلانِ روبن اموریم‌مقابل‌بنفیکا درفصل‌جدید لیگ اروپا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/29909" target="_blank">📅 00:30 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29908">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVkYo93re6bA_gXhmF8yK5pvmLH4NVYDL4vbeyZQOZMJ9zk_n7FeOVQPNuIvL_pOQdpWembxHLTV0SX7rypWgnpV3CG1ik-ZSQNbnaMl4SjtjHhM6SpEeOAQ4cAWY79NFrE4a4sYf20B2S4yV0xCwUD2db9VGjBRGxI2ipS6fh7PCN3btMf53dfnhmG0PcrcKPBj4aegiTnYsPtbuTI21JIh2GDy5ea4SLWxHKHsoIgoRsGcS2m1Qgx5QudoKaYEuiA7nwtdLqip6wGXfYQOe7wbcmdMJMpy7jd0iDHVRyn1lHOBS7oX7KkaM7sib23wK54fORFzdAKnSKpmF8nT1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/29908" target="_blank">📅 00:20 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29907">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9DWPuikI1E6KuVD3NbnbCY8r5LS8g421DXFJ9-NSVWdFjb4yJvy1yAT3MXfPjpnp95H1Z1jxKpTN7cZZGPsK16gTt3wRo7ViKdTqDk3b7tmY-cMB35MPSGf_I11rfRC6pOiXvYNpJE0wfD__DfqbDF7n0h2FiNnFr5eOyPh5lHDMNlimgYVEYuRRGxlH2pA5SqWYngwrWifLHXY0YcmemkprqUFfDrX5pRjTHWTpNI02SRCvURqALE6A10nkdN9d3wDScg-yzK15Fy-NDpAArEBR7VkbwYEGjNpeDp-2sdtSzn318W2hrWX_RFw0lYdNgmMAbp5FCPfz7IJb98BCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص مهدی‌طارمی و سردار آزمون چیزی که ازنزدیکان این دو شنیدیم درنیم‌فصل به لیگ‌برتر برنمیگردند اما این فصل‌قطعا آخرین فصل‌حضور این دو در لیگ امارات خواهند بود و درپنجره نقل و انتقالات تابستانی سال بعد به لیگ برتر خلیج فارس باز…</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/29907" target="_blank">📅 00:10 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29906">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgIlKg0lmBAX3q6m9CkxWTXf_DtJIct0lz2z_lBjEoTSwe2XgJq0sv_YY2nAtODiJRRzfduhoqNcbnvlxnCXANiyq6hsxMgfPJkYRVE2tmwmPq7Nxa8HV4HJNA0yXeQMAdX-Iow53aO2R0fi3sLag516bfBAh8gUt-yZ5kbxjuSBXK8zmYc4mrQr088VUaOELCFUskQ5UX45TU5YgEdDKuj_d6lVoof97GREhy5DxqvQoMbRIqkmdsThm0yjOyli8SDf-b36LkPHfk6RBVZQXegBlDU5C_YRyqeej0WeaCX0Gh-hMriLRLNIwo-MQFWhUjLfKlbQK9RVVjzhjApIyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رقم رضایت‌نامه‌سه‌فوق‌‌ستاره‌ایرانی ماخاچ قلعه، الوحده امارات‌والنصرامارات: مهدی‌قایدی: 2 الی 2.5 میلیون‌دلار،محمدجوادحسین‌نژاد: 1 الی 1.5 میلیون دلار و محمد قربانی؛ 1.2 الی 1.8 میلیون دلار.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29906" target="_blank">📅 23:49 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29905">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=p4ue0PTU_baDy4LJ4W_wxujg7O2yYxRWxt5XZfSn1faoLw7cdmi3-fRmT9g7z1eAEaMgC20gYei0Xb6FXpXUrUZpUX2yJefiSsCsAsziwFwn5bI6JyGbqZSZT4oRF_8-1wj6bkYawCKy-lzhuCbs9TkBoxFC6zRcJNslHYgnLPO6Rr4acFMA19Id7JTShQC-dHDc3Z8XtVl0cUSVEpXs_b8zS9_dv2WT09nrTnVnzURbu3QQd7L3v_JG4yee87yuWnQ15K8Qo4f2sjAgnXaEx11bXXVvOgR0Ml2c8VNmdKrbpydmcm2tPdsQZwRVA3i8WRyhF7_wriTyGYwN-oEllA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b56fabc8.mp4?token=p4ue0PTU_baDy4LJ4W_wxujg7O2yYxRWxt5XZfSn1faoLw7cdmi3-fRmT9g7z1eAEaMgC20gYei0Xb6FXpXUrUZpUX2yJefiSsCsAsziwFwn5bI6JyGbqZSZT4oRF_8-1wj6bkYawCKy-lzhuCbs9TkBoxFC6zRcJNslHYgnLPO6Rr4acFMA19Id7JTShQC-dHDc3Z8XtVl0cUSVEpXs_b8zS9_dv2WT09nrTnVnzURbu3QQd7L3v_JG4yee87yuWnQ15K8Qo4f2sjAgnXaEx11bXXVvOgR0Ml2c8VNmdKrbpydmcm2tPdsQZwRVA3i8WRyhF7_wriTyGYwN-oEllA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
گل‌فوق‌العاده‌دیدنی ژائو کانسلو مدافع راست بارسلونا در بازی امشب آبی اناری ها برابر سانتاندر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/29905" target="_blank">📅 23:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29904">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=ePymEQK68QpEofVDBTzyBjXwCJw_tXk30qiPkK8IlrBniNpAyW-WBjxEXkzsEYrugy6KQrekon8F7Z5_JomoahdkH2HwVu-mXGLZqh3f5x5-YFzgY5e2hAYhz9LbUIBy7Xt9teIRC5OGz4TwSdJXakBpD0F9cjYZfV7gTfJ1_ToFSQdtCChUmcpOc-h3v7AK6Q_dtXm81SdWPviOhU9XGPhtI-7PdrPNfF4KSf5dntHlDbDoTgmyBQ_wPrC2djggJoKW0vilE1Ozch-q23gd3_KuKB_jKllGoHbSkCpxP01O8NgMMH7jvZjBLG04M2N_Qnzj7icFOrQHJpAVfUDLuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7cbf3081.mp4?token=ePymEQK68QpEofVDBTzyBjXwCJw_tXk30qiPkK8IlrBniNpAyW-WBjxEXkzsEYrugy6KQrekon8F7Z5_JomoahdkH2HwVu-mXGLZqh3f5x5-YFzgY5e2hAYhz9LbUIBy7Xt9teIRC5OGz4TwSdJXakBpD0F9cjYZfV7gTfJ1_ToFSQdtCChUmcpOc-h3v7AK6Q_dtXm81SdWPviOhU9XGPhtI-7PdrPNfF4KSf5dntHlDbDoTgmyBQ_wPrC2djggJoKW0vilE1Ozch-q23gd3_KuKB_jKllGoHbSkCpxP01O8NgMMH7jvZjBLG04M2N_Qnzj7icFOrQHJpAVfUDLuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته ششم لالیگا|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29904" target="_blank">📅 23:19 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29903">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gyf1O2qFBzmHq_dpN24K8KqivfYy-m_taAmXceBl1wkTyTIz5VcSBrznkpal6pD9Rzy3Dz-ZisSBQzBBudybYRzW4twZ5GXQaqyWjD2S1ej6OwxhqGhPB8sBIUptjxLhhjVy4tKOxkqPH-A2LRrR6Ynmhb4sgFvr8ANbZQIxygPgxqe1zzUi-oF6ZT0V7Zqi3y1l4SpICJdGlpq7eAWKh6W_HP_luoWTrnIKUjd0jOdN0Qphigjwwkmr6RTkdQcksIWK6IzGaZvv8sbMT5qvRDNPcRZzgUYKyF9fhztB_ITjVQXMLoFUnvSeqTth4RwK9ayNK8HPKycpqKATBs5UOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/29903" target="_blank">📅 23:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29902">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L-ew5I2PUDaz2Q5OSwhVEt9b9MNNEbTvt-jjcrmPWVy9uwh3faZHLgsR7sWi8R6BK2XLxiSn9wvt_UDkYFl6a8oBpaQKcx0Xtt63T7xzLCkMqKSpUrFrGas_nKzynIacDI8pFDYOi1ShdtvHS1AkP7WP4r7J3CPWC4EyLfd0FI9yK7H1PzV5H_HDyQgzoK7KdegaSQiXdnCKiRtvUuGVHVCNyszbqPo0_m2lt3mbGyOvwT1mId2M67B9pVVUJK37H3qhIGkDtPV-3ekVJH2Nwt6TBUrnkWMCWxLGmvc66NVs6HXDJBPcEVBVd27BWtQv9CG04OTYZva2otDm3BNQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ مهدی زارع به دلیل مصدومیتی که امروز براش رخ داد2الی4هفته دور از میادین خواهد بود و دیدار با خیبر خرم آباد رو رسما از دست داد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/29902" target="_blank">📅 22:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29901">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GG1HccKMDPiIoqaFF4X1dMusyT2R-zE59B6NHn7JxGKnEuPZYNQrkpytRN-Jc44fl2w08iZy8ahnLloHczIqSXHIdQiM4SvMw_rc-vRqSB47FozB1XCxSQJxafT99JQ4l1Mk_3-eipkyg6cyjL_Qx50vq37ovYRr7NZRgdkSinqG173pDr6UNKl7zCBKArJAIuY7IFRcZ16wRcJkMW34rhUs4nTzjUhk1sPgcJ4s5HogisBQfRMquLsgx885pqlZ4u50yv9J8vEPDsYat9_zFLUhrhe-L2Mv6MXnfLAro4X0WRQYWeyryT6mTgrdl3jwNm_28axk9pfy9CbjONj5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇫🇷
فلش‌بک‌بزنیم به UCL فصل 2017
؛ که تیم موناکو بادرخشش‌ودبل‌کیلیان‌امباپه 17 ساله بورسیا دورتموند روشکست داد. تک گل دورتموند هم عثمان دمبله ستاره18ساله و فرانسوی زنبورها بثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/29901" target="_blank">📅 22:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29900">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzkkfGmG_oRI1PH97QiRFSc2K-MsTNmzQgfz5x7KDQVAFhCskDVJ69KvcsoLg3C2y2S0NER0JLUmtDnI4p-kNGMW4r3HqPKb-jgvd7J4EpauggJ2IYHVGDdAEsr_xzOWxiYCMFYFrTOk-8FXTPq3IJrZ2YVDjgY4bDwquXJ471GNBISi-LAgX2EGRtxNRYrXgvWz-FlLutiyDp0x40l1x5SQbeUlJPXn7infj7JWcAuoBmZcvWe1Wp5gyxKEntpWt6-8gpmwUblk_HuiUcjV1q1sgtx1ttk6NASoDT2jZNwvzkezOq-_-xR62eZpj9kreLgDFt1rXpoSO4c_5gQO8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش یان دیومانده خرید جدید رئال مادرید به شعار هواداران الچه که دیشب شعار سر میدادند که رئال کثیف ترین تیمه. اینم از حرکت دیومانده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/29900" target="_blank">📅 22:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29899">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nX4Z-5TuBvTvp0Ng9LdFtnZ6Gi-3kDhug_aeTV11BJM_nDvjnazFULm5LZfvnOxXwSnLJSuBOeImgoYgMJ4kAJ4sL7UZNhpHRMNNowXmz2TxXdVwJfiWEMQQG5qbIOynm74KyYy7UDQK0aPdANnkbZMQvhh2AHZtj7ZtaTOVOpM_nL3xxG1RPBocQ5Z0wk4hujSVtqxEKiExN7m_L6ZSyQtiIeiS0g6OFE3eujI9ISlWgdb4g4x-WY5yySN9PzAzJum7-tPltC5uCdCjetQ9CA-bHrVE0Ttc3eBmD64z96XyFuFityDch54dMjJM1eP-n0mzTrv2s5MRc4nS65velg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته ششم لالیگا
|شماتیک ترکیب تیم بارسلونا برای دیدار مقابل راسینگ سانتاندر؛ ساعت 23:00
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/29899" target="_blank">📅 21:52 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29898">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvJI7VD6VHcIjAJp-h693styN4lvEaDwYNtSkFF8OheA4Lio8TG6wkvEY6ugIaRaUeL2Mn0Qn4SYOrdUD9PH6qsIDQaa95jKJbd-a4DYQlxX8WVw3AgpkyICBkpSBTrrcywRjVS-jWzM0sL2zgm0W5eoytuLcjz-43G3lYQEZ02pCUS-8bxnJnswiMdSkyFll87u-FuxU1kn2XXqWp5vjEaiWkSPoHfzGnsgakvaa2CfGIyhK-nXpwt-dApA1caUR24RbWWXspHrLyReOlVsj2dKl_bizs7BsiI4BvDX5KPCYnz9Mmin31nR3X1TbDGpHpUrF98jymykvZ7IqyZgVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛‌ کارلوس‌ توز ستاره‌ سابق یووه: کریس رونالدو و لیونل مسی قبول‌کردن برای بازی خدافظی‌ در دسامبر 2026 درتیم بوکا جونیورز هم‌تیمی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29898" target="_blank">📅 21:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29897">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcsV9vPaVIUgQ7rQ2v9YNahWbNg-VwByWVmp39bHSoyd2-V59jzOHwLwriqcymbRpgOVFUk5XAtzm2Uh-XBCH5wEnM9F7-oVR5_Nbx6G52KNoIMZS7SEHxzO-YKjzxauxpJY564_eF-uz42xRikgVnoyOky6ZdZd6irHfkeUIl66xJVhhy0HfGXPuBeOqKx9R7GV2T-UcbzHLgFwNW6lIGrw_4hUbNt3qk1F1ivo-vF2HUFUoeIMP5VyYRR-bEezwWcd8px4FkQekA5nvX_V_TShijo0UIwcs70fHZthaZXMjE40kT_rtKdxKmkb78GyQuiA_MlY-Kp8YA97UlYj7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ رونمایی باشگاه پرسپولیس از فرشته کریمی خرید جدید خود؛ کریمی از 18 سالگی تاکنون درتیم‌ملی فوتسال حضور داشت و بعد از خدافظی از این رشته به تیم بانوان فوتبال پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29897" target="_blank">📅 21:22 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29895">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmoO8WaoJJTrb-lMvod_t6rErKjgWIYX1aBLvDIx1DxvxknnHvvdawNEag-XEGTU0M4kW0jkQ1yvsgOYHTQg6NkBpRRfhZuAt__sylK8yMz2ID5u846CZoaatfzYBMTH0AqVp4qQdo1LTl4iRbKcL8CplJH4NxsrMHXAW9PZ_OzdgujK7hWGProE7CNtedp1NrQsV_1H888Ph9c_UsWwygbblLLgs__Q1f1InhxViqEJVZvTyZEut7yPmEnE1zambLBP1e1RXAZ6tAWsxjSsgpAj2CvWv8UWWr57WCjHEPuJ1gNxghBc67vgKkpNRkXt8elqlkJmZwz6Rek1Loo3Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ یکی‌از مسئولان سازمان لیگ امروز صبح به‌مدیریت‌تراکتور اخطارداده درصورت استفاده ازعلیرضا بیرانوند در بازی با استقلال در هفته هشتم لیگ برتر که روز پنجشنبه 16 مهر ماه برگزار میشود بازی سه‌برصفر به سود آبی‌پوشان میشود. اتفاقی که سال قبل برای سینا خادمپور…</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/29895" target="_blank">📅 20:56 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29894">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nA2qVOnvnP-nKxgVlG160pifUFPm5uMX6tdjjGI7LIoET_tUdjeksLV2_hfu1rjC_W6hMHG6yT9RXdLoJuTtuQ9bYUXU4CmPcvcagbrT6qpu8gOBeYvS959HNt6UzC15l5MFJJ7gajUC0wqFe7vGYp1DhgEarP0lLimAsbYR7XyA-wPpZenJv0ELxvJjeKTsIzwa-S4gsW_a9jE2bRF1Dxec5wlWLjAO5dbzJROTdYI4y8UmBCnXjH7y7-RB5MpBbm6MHgbIVxP_3CS5ng9jU6PLxWiKJaAH2yb6YqrhfVUUhX4ldiezucc5VH-ciUQHZ1cRokpBAgmUPcGYD5Lhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه: پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه.…</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/29894" target="_blank">📅 20:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29893">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HILbmyK5hihWRQPE_K6tTYs2GUgAQXwUq8wjLnKlb6bS5QjlxBy3QUwvJtKyFRKb5esCjPkbXs9GuUCB6dkBwBYCYaEfZVHLBtTrZ0U5C-GVoJWf5kpTqqxhR-tnPyaF2EmTeKRWarFCAgZCE91ecauEVeFkzN47FUYnJIZwAayG6vWM8vjG9pRwaQjui9Yz6Ez4ZbNOcGNj3OLHyJ-B6vqLZ07VUtkQAzs131wBnGZ4kkpyNa5pUSC2tA-AA8m2G9XIcF96my4Eagvd1RpBHq_xXXB4cq0smTzeYXa0qLEE1Cta73P-WEZ8TTLKfQoZ0d-JR0pzj2WH9UvsUx1Qyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇦🇷
رئیس‌سابق‌اینترمیلان:
سال2012 خواستم به هرشکلی‌که‌شده لیونل‌مسی رو به این تیم بیارم. به او پیشنهادسالانه 500 میلیون یورو دادم و حتی معاون باشگاه رو هم به اسپانیافرستادم‌که او رو راضی کنه که از بارسا به اینتر بیاد اما لئو حتی نامه‌ای که من براش فرستاده بودم رو باز نکرد و آفر رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29893" target="_blank">📅 20:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29892">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paz2wId1lXrBecRDpItTt26HXoem70yN_0DXKEjjJBFfcPU5OEnxhjGD3ZVInfq8rMnr6w8l4a9ylvt5MuECItkXyiA7PP6H_kzwlSdQ0kfpQLDqw9FZO8bdS6YIHqqpDbIBiqS3OmsA09xlEwhlxwcGm_LVoXdCTxoL7OcfULTi_7lzN0QBnRC1u5XWd8TuUIdN7Iwk0TtEtVYKjxgKaCyiANXQOvJwLDUlwPVosps4Z--UTVzdAkpSo3tmlvixsi7VgC6GFWJUUJKzArsnt4jWraMgFJ93hOg_93etVqtu_9b1wAozqqMXJRq7taeXCAF7ctRYztKCf50CXz9m6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29892" target="_blank">📅 20:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29891">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRRr2Aci6lZ-mvbVfMkLcYjhZicvsG-xG1Rbo0IxS-CTMbwUGxJR3YrfXuMvHMsEON6lSZi0M8WEhWDUIwUjWkMT9DtTlbBm5CPX9mq7hUWKy1SnRzudD3foJN2khRDc-80yeDBqlyIyYhMVfd9yk0Y78c6BapN1noO_UlZa33LKcQfClzQkGhsjDxizRIXQJdKmdTlmltCJ0dpmtFTDxeZZhQXJtw_rxDE1OypmM0sClpyds3QIOs0HDS32XYflTlwfs-kbMf_Rr0xpfjNE2je3nZqf-aU04uhroieuH2H2JHCQ2xPl4I2QupUEDa93LBMo1A8DNudByYo1Qcazqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان: یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/29891" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29890">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W58zsQq6ya1gMm-NeyNgPqY6iFZs4cpUufzWejXEm6CnwOTBaIBrE6LbiLiPpZkQao3tX77sdMRLad3EscTr06camy5oElYK69gJpF1cljSWIQKAvqjpRWS3JpV-Kk9jKpYcT2ULYwv68aeFQFc46v6yeDNv7lUNMdhRYbKLyCk0yxdDI6b9Q_tQMg4VQl8RiS_-RGxmPnq7c8gLGPF_-N7T3YnFiNrpd2X4TBHSztjETOvnAHOGYFVTWNQ6tmm-dOlRatnNN9MRTDnPNN-Jt7V8JMZ9dgqgVQ2sWeG7mJ5fSp-l18bxlawi424On4VduTCGT-TjrYPJQJ-KpcRgkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
یوونتوس در نقل‌ و انتقالات پیش فصل؛
سه‌مهاجم‌فصل‌گذشته خود را فروخت و سه مهاجم جدید گرفت. مهاجمان سابق‌یووه این فصل روی هم هفت‌گل‌زده‌اند درحالی مهاجمان جدید بیانکونری در این فصل هنوز موفق به گلزنی در سری‌آ نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/29890" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29889">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDP6sKlv7sDxJdjLPPc4vQ8ymBzQjjqWdPxQAmFu6nQ_l-A_xCzVl2vNsTgZobE_m0IEqQUiMqhfGLUlmxx3YyD6RxDy3tjHcOl0L421r2cEb_KolvCyzlrLT5cO_tomytrQogdRCz7DPSpbcdHkJ9BqTmTi1RjyBEqmKFE18UoPTKCyn6Pmf7ZSNUu18mAhGwaYmmWaEbjvYVExuCsN0w_3qq718xaGu3sAwDrCgbOirJ80KxQJ9Fpvc9UsN3K4NVFRX--r56bSp8KfwqFdZ8H5nLJf7PFvtAJWksYAcX7VWM2_IvRGt4ucKNb9hWJvSYZP6e270Ca60FniuyWyrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
اگه تو این اوضاع اقتصادی بد دنبال یه راه مطمئن واسه کسب درامد میگردی دارک بت بهترین گزینس
💵
💵
💵
🤩
۱۰٪ هدیه ی نقدی برای تمامی‌واریزها
✔️
🤩
تحلیل آمار و شرایط بازی
✔️
🤩
بررسی آپشن‌های مهم
✔️
🤩
چالشهای متنوع همراه با جوایز نقدی
✔️
🤩
جبران خسارت برای کاربران فعال
✔️
💎
کانال دارکبت محیطی امن برای کسانی که به فوتبال با چشم تماشاگر نگاه نمیکنند بلکه دنبال یه درآمد مطمئن از این راه هستند
🔥
💵
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk
🌐
https://t.me/+KoqkzqAz7CszZjlk</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29889" target="_blank">📅 19:57 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29887">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1ChuR3yx_Y8oJtW86yYrviKsfjQyhvHTvQyHrTuaDmSsiyAs6AHBLoXeXJXmoIUjuLJaray7hNPFMWeBjwkX3w3HGfAANEoyJPSZI3vaxf16jM4RFLGPXFpGCp4dY9kcDIrISSAQrNDLNJda9nBekx_20uCUZIiNK0sZ8g041sBAEX_90vswTa5LtwRhWy49HkiI6Nlktn8vw48xAR5VYGAmBVdo8QBQ4ed_8u8A9zTBLxlUvUGlbaON8GKIV9HzvoZSCeMBMcmwciEUTfxCmqFiDpTjc6L784xCgqRwvg43mXQNDtCw3zRjIqwk3h3B1X00yLqCf0VNQBK2fqcJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
‼️
وزیر نیرو در72 ساعت اخیر دوبار با رسانه‌‌ها مصاحبه کرد و گفت دیگر به هیچ عنوان برق خونه‌ها اصلا قطع‌نمیشه. همین‌الان برق‌شمال‌تهران رفت تا دو ساعت دیگه! با خودتونم نمیدونید دقیقا چندچندین!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/29887" target="_blank">📅 19:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29886">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QDti5yAQV-m6fhpR8LXcuf9GkwZ-GUXEbheiWqjH848L48nP1DAZGaU5KRjDlFi47cFgrgOPFo7b29pzL0fZ1tPLIl0W84XC9Q4EtTFGbK5ipDJ5dIIurnk8PQgfWo0piSNdpBJ9DZJIDmlbUUBAJ5Tnyfk3m1S34t45ef_CkB3r_n2XpEyZ3APNLUyuVJIFOLSWIzqG9KfQv6tmuv-BU0x0D9UbSVgWbY5VX5jkkYpx2cAemM46G-O6bhPRMyuB-YfdMUCtNKWYF2ekxrQVKoLBDJVQKODQ5HiBZbJYhy4GXi0nMjUrIy3GLWEmmGk7M-sjyFObLRePu-JLNNz_7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام سخنگوی باشگاه النصر عربستان؛ کریس رونالدو فوق‌ستاره41ساله النصر در نقل‌وانتقالات نیم فصل قراردادش رو با باشگاه النصر فسخ خواهد کرد و از این باشگاه عربستانی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29886" target="_blank">📅 18:43 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29885">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R52eR578eXpklm1FBIV1GRWuBM4aIO-6e0nfOOgLJY7Djt-lnr2aaMd3UOAjbSycLY4Cmx9ykppCNjhCJn_KPCtgnOzWropd2a3igS-h2s_I5ZFb3x-Z5owrydKOGbXe8om8svqCnBQA6QyT6ZzbEFOrW-wfyoD9WFFAKAbNqLw1Zk-zI56rk5hGkmY4eCG4JewKaIO2179qu8N6QXpQnUqgUHfoJOX1SHLXa-coksuOTdDILptnljc4ZQcDL6btUJFk7NvRKq1nF9O4pkWp5uqJWDwf_qw_vsJK98LKIRC8poIIMnaAkwjlUigI9RHu6Z7BQSL_Q6wOgAFJqmKo-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
کریس رونالدو: این زمستون رو نبین ما هم بهاری داشتیم. افسوس که نامه جوانی‌ام طی شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29885" target="_blank">📅 18:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29884">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1SZcH2z6WMjk9oPYn-QQ-H6VY6KAb8-t54_3lAbsbv6qIrW0scf4JKYmI-hSQEN__-nejYfkb6EfSQv3eWfK9QDbZ5fjbD3Tw1zBjnnaFtAWK6HRdf8pmHmE-0uVnXWZSCO5m1AkRc3X4CSFg9kH6kVPBS68haBB6JmNbQEGsy0TlCiKQrXzlRz9ux7DRhiUb0k3mfLlTnHfsEthevUQqs2n4ptKm5j_oOFBDB_ZHyfkhPc-qZUSlcdMU-pITpJk_kiM_gP90rKBiz3-BH5_EUGAxVrUhb_IHkyqFvv56nIcmiVEwSbpVEl06OKh5sPDkaaY64IpOM0L2M3CJJcvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
وینیسیوس جونیور ازابتدای‌این‌فصل تا کنون 17 موقعیت‌گل‌صدرصدی رو در بازی‌های رئال مادرید از دست داده‌که باعث‌شاکی‌شدن هواداران رئال شده. پرز هفتگی داره 600 هزار دلار به وینی میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29884" target="_blank">📅 18:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29883">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6de055e3c.mp4?token=Fe7a-edlLs1Ua-w58ITKRUGhKuYNgChIaK1cFyD9kwRRlF2Fr_-4vQCN5kQ4oXq4D5XBQRCv_VzabJEQhOrMk2KhYo4gPpCCQVNHTBt1o5uDk8hyzoBzsJNePAdg7Qtj81t8vcjcIXu1AhS6352wDcdtDpfW6tOV3LqBgqwbsHUUzP3bYZsAzySOAcnMb93Cv69XtEgZzpld2y-rnVlB_cR3oZee0oalqjs76rYIyQuCluf2rMVjP8yveduwfxjaoJREV206eMJeApEtynljULj2s0meVlV98KEID-i72p9xC8kduFe8g-8qxn7ifiW5N5B7O5WULApapxeWQ0jEMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/29883" target="_blank">📅 18:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29882">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a7515755.mp4?token=C0F97XdMjzC4yVBmoXNelDh8AXgTv4F5iDPhomKrS-X-pX1Vx2sXauVFw8F7rrWMuY14NtKP81ahFNEgpacNk1ZUUAGZvTO7Ylj2GXmEwcZR_8pNqXGMWzCYItab9jurdbtAJvaJPgFlQAui_VIpTrfzOnwUypbYWPnh3RGCIQeRYygm1WOEN0J6F3LL9ClTMKQ1MMWldpWWCjulIkBDj6vwdav-PGhyH02AUzop_8fFb0aCobEUya3mA-C_Ysa39S_YTmAuqEfZ6Qp3kFIytvHAlkfT4JDYrzWfQ37gNiP9QmSiUyhainp14p-gUM1T76LANjnf_ZV72JmJXwhG2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
پوریاپورعلی‌هافبک‌پرسپولیس درگفتگو با عادل: عروسی خواهر زادم بود ولی وقتی شما زنگ زدین دیگه قید حضور تو عروسی خواهر زاده‌ام رو زدم.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/29882" target="_blank">📅 17:39 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29881">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14d489d5c.mp4?token=TYZ7Gxj1n2HHuoor5WI5S9LPnW31O6k6VkWVYse7SOuc4fwqUe-3VnJ2C_noax80yMpAxep0h7T-7-5IDSJho1MvwvGbVMDJHV8-jqvW2jfTgBodZqLCPt8Pmi5_arCoGXNY3XGQZZ0on6EDf9URS7pTwK6m2W7bTypCvDLh0wVRBxbIHy6rDjRSog8jx4VDt-aOxdGhNdTTh0FsrVo7wjH_zI22BH7o9z8j0gbZHmuoKNhYKM1SdestBxmC-XGhrJr_wrlwvAVmGbao_GTogBzpX-T360JjBCHw9vEvYdaikaNVkyiWLyKlrGiMvYo7ZqrZyExExG3uD7oO7zWIb3SQDDoNgGu29YDfmyYrKVBqYeKDo21ashtiEMs617gZLPIegYp7RQNCDC9TZfPyXmt0LjzUTo488l3eMBLvxsR4YUaoNC-4la0rHoqwUUMo2XgZN2NqezTRBKpha26N9MGL77W86oqBvDFeJR-8ddpeeA8XUbgLcsukSnU6sLsjUObWhiwY4FkH5LwhcpYXiurgORdMXcSVMCuUdh-31VzttTd_RLE-rRnjMcqSW5RgOCax6RkInc25OkOBbuLJK3eWHLhIZlGy5iivvvk_4REM9-VRiwhtnUIyHz67RKb_U_Fin8dBqvZtpBMfsX3rs-bur9e2cMgps-RWupkH6vs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت
؛ علیرضا بیرانوند، داوود نوشی صوفیانی و فرزین گروسیان سه دروازه‌بانی هستند که تا پایان هفته هفتم لیگ برتر موفق به ثبت پاس گل شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/29881" target="_blank">📅 17:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29879">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Utuex_a_ANeu6HGDsuJ7IfnyNHMCgCtyNWRNSmZkm5FdbQsScxww8kCUrVLglsUmCqGAKDxqO6gemXdm0ivj_Azq9JIzrUuwUggUeHEURh9WLNEenvkbLjzuokMbHixfb6Im9cotzOnMWDOYNIf-WdO-DO2QMZoryB5lEjppK_YTngyS0e-MADzoIvciMrIzyes5jG0p9BSzBGM1ukOnLaa_rkUvrYt47FAZVZXmua_bBCZE-ILfHSzaB3ktZ4wMDz4HglaU9NlQfw5C-46ymQl7Mv2R4wcJCJk5zhm8X_VpOCAYkwoK1vkmRS__fqFSK0p8wroiW2Yo2IOgFSSHkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زلاتان ابراهیموویچ اسطوره سوئدی میلان:
یه روزی معلم کلاس‌بهمون‌گفت سیگار 15 دقیقه از عمر آدم روکم میکنه منم بهش گفتم کلاس شما 45 دقیقه ازعمر آدم رو کم میکنه اون‌هم‌عصبی‌شد فورا من رو ازکلاس درس اخراج کرد و گفت تو هیچی نمیشی. داشتم میرفتم بیرون که‌بهش‌گفتم روزی کاری میکنم هرجا رفتی با افتخار بگی زلاتان شاگرد من بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/29879" target="_blank">📅 16:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29878">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ltBCX1xXLJYktdvEGNgkp40J2FTulOnXHRVQ0D-wSzxXrcpdul8UbinTVXCV5B6pYDwIRscTCZPueQyI7ywBalWnyLVR1meRzkpy4rz6vN6yb7Tw9jvfoprWDcHF4RrfsJxrtzpLcYCXRnadUGiGBnptGEKcPKnKk4Q1skkBbEGd-ut0CEVmI4IOiTia1nICO0k0jdCNu8n8y103z-p05KlbSPMXzQfIa7HIpiYDUrGEOepI6eo3gKKSeAd5aYml6qtNCFZeMVQcNfa4pIl1oqhs8I-BmBONomOsYTI_JbLBrvLDXOs_6If7zHV5n1KJEe0QJlRI9nAo70C8gQTVhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌معاون‌سازمان‌نظام‌وظیفه؛ از بین قایدی، حسینی، قلی زاده و جهانبخش تنها کاپیتان تیم ملی علیرضت جهانبخش معافیت تحصیلی اش به پایان رسیده و باید تکلیف سربازی‌اش رو روشن کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29878" target="_blank">📅 16:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29877">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hf87MZ2OL1TQR4cSkxAKjb0ymmoMDOMf_YHe-PyrSGhjSx-Lne-hF5CigwSchuzkAIYN_ZU_5oU1o6ShTRXn_y3V5TqrFXZuy8wFdMBTa4h51xTqxAQ0wYsJ6o6GbY1V1R9x3Hh0EP9BoY7-_FHEfJJ9cew03qu1EReF62vsOcsgVlpRwNp7TcEVay42-5XyJJpoJeXxJjYqMdGVnM4Vb_lsNCxTWjfkZm4UBNWSQiNuLsYodabtadNqcvil3_VCn_qammMC1gqerXyuNrWpbG6eKZjeFxqYC8JUKytFVrwvMypFO9TF-1YzjRvJTJIn8BlyozHUw_ysCslbACEHfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ اگر یک ستاره هر فصل به مدت 19 سال متوالی 50 گل بثمر برساند درمجموع 950 گل خواهدداشت. ولی‌کریستیانو رونالدو: 979 گل زده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/29877" target="_blank">📅 16:18 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29876">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owgrbg0cFAmSdBuYttNyhlKVVWd0I-u9dwLuNij0GsISiUmaH8jQOK6OlHMU7Rrb-t_nNPEmiPUYPxXwZn7OlnQZ10DRGgS0iEJa7Wy7JqLyiBzWsnpU2Bg8FVs09TNDw6YnAguN8VC81DuPK9FA-U-8d16aKclfpAp8ccMqFoKVC324j7qTsbKb65Dl3TZlB3yW8lFY73DReytlgxj4WBoR9rqtNjDssd27Vrv64YewomZ-f001lw3GCm9MVvYRwvI0fN91tmwCxE8m7dn4obJ5eKk0kEWy43xH7zpj2CVXxQ06ozm7sYfLVe6O4kTFLYFF0PCsSKsOerDGtLfydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لیونل مسی
🆚
کریس رونالدو با پیراهن دوتیم‌آرژانتین و پرتغال به مناسبت خدافطی فوق ستاره آرژانتینی تاریخ از دنیای مسابقات ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/29876" target="_blank">📅 16:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29875">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-AIT1BPZ8T1b3OOQtfG8lOX0mVWw43sb7xoLjCwMMnXISR8lMpmCY-k9MuBRgvncfsy6CqEfwlFrsqoYEV6bnpfMjbildwRLLxE1NBLXNjbxgvmVnw9kNPw9aU1ccCS10QxYO0j6W3TyuPTCnl0-VT_GS7kcb9Ytdg7HJ4AEA2g4OwaKatOQ_1lj7bbVPmpLM2oQG080suFT9rdhQtAx3_yM_nRs-RRh6yQYnP3rqj5ub0W5T4gtbsU3GB44zxO9umxEbzPo0HxbMBRU6kHpNUulA6NOPq8KsgzdEaMwZOpyYftVI-0xbNIhu-sfJ0JXMgCCj2rUMSgGgaxagx8EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
دیدار گرم امروز زین الدین زیدان و سرخیو راموس دو اسطوره تاریخی باشگاه رئال مادرید بعد از سال‌ها در حاشیه مسابقات جذاب فرمول یک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29875" target="_blank">📅 15:42 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29874">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iO4jGbua6eV8GP7MxEGIEKIp8ZCmvJKyuwepzTX8R4BekZm-Xjk81bggqcGap2WIqqmSqIPaoJXYOtNqmk4cKczPsib6oJn9dZZ1R1DIs5bn75Q4Bc1h9IomPlXks47jIlkZ9o4C6qjv5zyf4nT2xmGvhbIHxHlEmfiofiQSOKFCyl4bvYoqhL4AaXqYvJKQQc0HhJlHtxsiSvneGlU1jxJWEa2VAbXKAUOcMAlyMhclv7ulKTmKHrrSmBGGDyDpwO7P9p5ZpRbqRKVvRbI8TFTha2NrU1A2Z1vErdOjZ6D0oWdrJtTLNfmyq90sGQPVqdsHOoIKCPBFKMgq7L1H4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29874" target="_blank">📅 15:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29873">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHsgxYSBianWCEP_M-prFpkDetpBPvJUs2BBNDsDdEjkHSeHqAlzgoDJfhOfWWPRUsso0tI4IWZfGhdp8OGWIgfv6KyfLBumR3j6It_jbpHQiwECPsuMfDmlC8mRietZPSBrv6DnFgKwyH5Wzh6shaE-Cwxgegt5W-9HczGdiojVukv1ThccuJRZ1hVIHFJ07TaZpf8FsXxI-itBI8C-ihAnzShvTGXQTXKNLxMYPJc9-iPxXw51zIyUgv33GULHr6S9x0kmC2kCRdZPpXTZgQeCR8SxqSPfPZUV32GXA0soJDv0Q8hW1GxPPt__BX-ZDZcaT6-Jz43QJsq-cU0qMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29873" target="_blank">📅 15:09 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29872">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/flRs-VKEfqmH40Nyhte9LZ7WrSMSeupT3HXS9I7q_1bdjF_pFGDDKDEYrNm-rR9T4pDxFoyOnIIYxnUsx30guDnvZxAru3CCkXpoUWcnEU9cWKkPonHWZqj-dGJgWUQ819fIHvLB5ojLyVqWHe-ye_WmDn6j6JziPBYyY-gtjLxGA-2gRejUcki3gKJSZEp5vX-oGrlEedqkvXMX8snaJRZInR9x-vEBafxGPy5TGLa0k3SBP81tzXJGiN13O8-dUSW78mpE_d9R-Ac3FQsCTHBejko2q08TeegBHPF7m5vln10jubijnoMy1Dq5mpCU88VphqXYDP57l-T8iqac7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته ششم لالیگا؛ شاگردان خوزه مورینیو دردیداری فوق‌العاده سخت و نفسگیر مقابل تیم قعر نشین الچه با نتیجه سه بر دو پیروز شد و سه امتیاز ارزشمند این دیدار خارج از خونه رو از آن خود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/29872" target="_blank">📅 14:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29871">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW_f8juqD3EyOzXPMtIdVygXhVtwsLCWQQSb7Abx_WCSyHpQwWCpuF0Ew5gNQSde7-dUc9YBYFf1SvMD8GORUcHDPEVBO9WCJPIYFOpFf-HaWkGi660X_HpmdDPaJCHrYCvvqUI6UoUMfXPP24V0lRfJGb-mnKh_6a84I9TJxs-yPwsY3aV87gtJeGS7wAaDCVn2__Rn51FkbA0kpz0RvYxkPDFl_HZc4YVBWj25ua4KJBxeTrd1RRiyT-NODf9xruwnU8Hp3uIvW8j9f6Qxan_PusaUro1Cn0PJGxKVSK06zNskY4yoO0cx5X-2-q5kdrM5yMyUJmDchenngy3BzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
فرعباسی گلر استقلال‌که دربازی با السد دچار مصدومیت شد اما به بازی ادامه داد حالا خبر رسیده به‌علت‌مصدومیت از ناحیه‌کشاله ران به مدت سه الی چهار هفته از میادین دوره و فیفادی رو از دست داد.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29871" target="_blank">📅 14:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29870">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز فوق ستاره برزیلی بارسلونا از تو این هایلایت وینیسیوس‌برابرالچه‌حداقل یه هت‌تریک درمیاره. دیگه خیلی داره به "یه‌ورم‌طور" بازی میکنه. دیشب داشتن سه امتیاز بازی رو از دست میدادند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29870" target="_blank">📅 13:51 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29869">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NoXLaFD3jGyLd5m1D0WJe988ZQ3-XzpSzuGZfwJBh3rNbiOHY_rRaxycl-Q9gMjXOUR37HY0u2MOQcWhTUr6E7mScuIE1JG-nbF_s7K-kgD5jzcFhXe_wIumjYwV5SrbJxOM_2YSX_5eG-HfIEsByKLYw7SVP3VZSEzhTfOFFLzVNf_Poa6ZqaDWfEx1aBzAxg8yAeiNphksQh3xWwYUudB_fAxTir-y8UVsBs5ILGYIfYuWLQZo9ziUcIB5Gkc0rJk1FJUCZJcP2Czm9wNkw7PGH8JmgoVvY7mUi51p2F5JNgjtw3feafCIMzprrY1I104uJGuBRjahd5Ewcx_sIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🔵
👤
طبق شنیده‌های رسانه پرشیانا؛
سهراب بختیاری زاده نام دو مربی جدید ایتالیایی و پرتغالی رو به مدیریت تیم استقلال داده تا با یکی از این دو گزینه برای دستیاری او در استقلال به توافق برسند. بختیاری زاده اصرار ویژه‌ای برای جذب دستیار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29869" target="_blank">📅 13:47 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29868">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGoNkp9NTAQNIwP0EptRqtqj264rHXsmnjuQiCgl9Ies3WLM4vNFr0f9EfzRrmVHestT9B5wliF7VS_khc7RTgvfLcpAdcvJZR-cELFCOqJJJxfKUq826lQNRSVEjjHDEqqSYl3tpnTRRx9VBlrFTywVXrSHo0qRHTXqpSEcWVnKUXPYV5D1GHoJ-fVXA_GdXL6QwhpTpe6nWyj5JSJF69PUfwL46plW5eLUDrFITgrp7joIPWbIkglBbEAjwhCULmWHsxI1ZluIRcbLO7dV1rg3f5tsxoCnOa29D94ykuoUsJAXVXK2ywG62PWeZJcKcN74KvSjfrZyNn0xw3gVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکرد حبیب فرعباسی دروازه‌بان استقلال درفصل جدید در تمام مسابقات: 8 مسابقه، 7 کلین شیت، 19 سیو، میانگین نمره 7.9 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/29868" target="_blank">📅 13:37 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29867">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX8mfiNUjrBY46_ln8ITK3l5y4CiR6V1vYsOhLFt8F8_BQIzzenIH5-8XHXQ8iPaDm3dtFKT5lclAwv7tbtvc3OIITLdv2ACMHQ8RWButLmAoWqhcWJE27-MTe2sAU_hCyRdUNY9Q6UhujHE2dWK0GKUqJeqW-WjbvciOGHYjXQTJRezCZ7iHoshh9JZSWkJezXIcHGEkkHGQpS3GjFZWx4cCxqJQ7_BXCVEwfkkxUgZ0lVQsvtpgvdAzEGG2m1pn14rmFTXShteBbnoGalZ6Z4F3-i53D-0TO5nOhKo7pE-Ft2Z4AkXui4C7cjTruPOEBYDu_wqeAGNbPuFXGrSJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29867" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29866">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b508f4860.mp4?token=GBhk86pUR-Dd8PERdQwxju_eMxiEWaWeTPWcAoE80HvlSWgWk5nkB4mJ7o_OwMcMn2wUP8qJVhXnfAzBrSSA2vlZ8wZTmbTmokIucUWkYP_gOJaQdNfvOIn9plkyqmTcnb6XWpLPknNhY0GPwhi4a162C7tyTqPDviFbyVMNcA-B7ySKtHxfB8VvXMJOChR4Nk-aaZULJ-F02o99DnW9YzJ_3Yx2aWOAwEgl7NFXGesys1ZYox2sEciHV7KnpJu4PtO-16md3wRnXMUCNCir9Xa7BThVmxZV0YIzWk6vDXQOLWO_1JdYkmEU4Hi5fJZ2ryhc3AvIRgx8ZmvaPJQqsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
‼️
#تکمیلی؛ امیرقلعه‌نویی سرمربی تیم ملی به فدراسیون فوتبال گفته علاوه بردستمزد 100 میلیارد تومانی‌اش برای جام‌ملت‌های‌آسیا؛ درصورت قهرمانی تیم ملی در این رقابت‌ ها 300 میلیارد تومان پاداش خواسته و از مهدی تاج درخواست کرده که تمام این بندها رو در قراردادجدیدش‌بافدراسیون…</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/29866" target="_blank">📅 13:31 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29863">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8NvOEyRApGloPFVK3LqNip9AOr12TtZ_pwzg4G17Zi1F6p42rOLi5FSzVOlSKu8GVab8k19Ui5-8RcGvhlySzXyo3kJ8-EcpXcUYRDq8sQVfbYGp3SMpXznPBT38_CHK8SOoFh14xaayoRyZsC4BodTdflyZVgMmcyozwP5npRlqQrOab75_R8YBudTzV7H6rtbxcr6lIpc-NINwVzy7gy8YRlw5Rf8B_uCbi45mbCT_2qkwJcXaGVi7J7DX6DANzt2jKFxtnu96CuKFc_1SDyAtjNEsUfwpsKwX--70Ydktkh-j3pRQY-oSXtpXalJvAFzOL2XYjUvwnms3Nxe9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تراکتوری‌هایی که در پایان فصل قرار دادشون به پایان میرسه:
علیرضا بیرانوند، شجاع خلیل زاده، محمد نادری، کریم آذر، دانیال اسماعیلی فر، صادق محرمی، مهدی شیری، اودیل خامربکوف، تیبور هالیلویچ، مهدی حسینی، مهدی ترابی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29863" target="_blank">📅 12:45 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29861">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5t6oAzywEFCDsE5-OBMu7CtJ7VXyS-FRjxFPe1Ic3FcmRZidnotItHGfBiMCsZis-r2trLlr0OLrwQipoobFRYG3vpfN3Js8FAYVswzYyuqsHZfmajKnEnx8Hky4G-SKMLitIj_LSq8DuIKp3tybxGEi5Qwhxp_4hTKDCr4y5izu_-C_mq2CbUFu2xiSb4RdwACkWAUziISP5awluDvSkYfikV6CpoFlkw9Gx3vxRXkWlKjFU5CLPwhUJaJak1PpCg-YdBWt0Ye1Kwu39H-e8s8hxNWfIjyrJw6F4INrMsqi4P1rWBVKZiV6f95_oRer_M0_jufJwFoeAHVY4Yk_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه:
محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29861" target="_blank">📅 12:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29860">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2LFRyXRsfpaDz_rGRk01FDqs6NrAvpj0rr_tu4LDqjg17QBrsomZiKdMKWOMap-ZxB0u05u6zoOO6K0wO18AZLepSo2Kc49KAJr9nLNBBCLXFHmKAHTugee9tSFob5c2YoQYngq1eTZxbrS5af5NIRQUP2nsCUP9Z4TqzRVvwuFRxN2CAeZcMsVh8rdHAbqdjRFaVNriwVTzG635osIQKpKh_JI8qXS8_-MT9uY2B88eO7vbupQBK3hZ3NsfPH5Jsdy436-8BdwYL3oDGj7OnfbO2-3okPQtYB4t81H3gVUVcg-SYw5RfgB1_FD6oBj0VTpQbG9S9PibY4BY4JBng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌شنیده‌های‌رسانه‌پرشیانا؛مدیریت باشگاه استقلال قصد داره در پنجره نقل و انتقالات نیم فصل قراردادی‌ جدید به‌مدت سه فصل دیگر با یاسر آسانی فوق ستاره آلبانیایی خود امضا کند. آسانی از طریق مدیربرنامه های خود موافقت خود را برای بستن قرارداد جدید با آبی پوشان…</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29860" target="_blank">📅 12:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29858">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxWldIdBKC-c4_cbgqqIVnBkZFVh8gPViMZL7jbxDZhtK1mySdo8tj_97lapDnWzMLG7KCuJjOE4bxVTLEjKAkydcbaTFpZUKUwRto24pAyklWdd8-4er7MblxOF2o0WS_ogapRgaugDjCmpP-9df-qdQLTOxVl3WbPv6AfWJnGDyA7tUlp1F6Q9CU9C4SBmXoReZrt7Ny-VeXtTstT1pHYpY9xUeqMaZTA-oMbCYd4wanUE-QqPL1D9nbiEDhNAd29SQtxlLP15sxlR7sjiSZ76bJij2A2cCsB0F2Z49joCR0tPRciTzyIocjKs-SHl5cL0Xb2qw9SOtcckzv2QzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرسپولیسی‌هایی‌که درپایان‌فصل قراردادشون به‌پایان‌میرسه:
پیام‌نیازمند، امیررضا رفیعی، حسین کنعانی،دنیل‌گرا، مارکوباکیچ،یاسین‌سلمانی، ارونوف، تیوی بیفوما، ایگور سرگیف، علی علیپور؛ در این بین گرا و باکیچ قطعی نیم‌فصل رفتنی‌اند. اورونوف هم احتمالا تموید میکنه. بقیه‌فعلاحرفی نزدن باهاشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29858" target="_blank">📅 12:12 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29857">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ula_GVsUMOda3StiP63AJS4rLLPjz-SvkHem9F9mckdgQWhW8JnMnQKuyo61vHUkBPlac-HedmzpUcxmq84BhZMUghXEO9Uf2qPH43rWzh-HqOHjZGhWIitdZxQ2JVP0putgit8FWCX3XzLq2MSjHbm_AlU3Feiyh0LpEAsAHXR1dRWCdpkGAwbWTrN8WCsLPJJ4-eZB8MA4yhYbtjKEJbnvimkJUs_U2hjvQFpchEOLVIZbtQQASf4rObTBRKKjioft-9FoI8b-8f8PL53P4xJUdeniCR_apgYmGiZElQReFXYv3Osh7dOixhDpNQ-MGQBlp3IxwjkTmQQpK5lLnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇪🇸
فابیان روییز ستاره PSG
: اگه توپ طلا رو براساس‌تعدادجام‌درسال و بازی جوانمردانه میدهند خب‌قطعاهیشکی شایسته‌تر از من پیدا نمیشه. تموم جام‌های‌سال2026 روبردم. تو زمین‌هم‌همیشه سعی کردم آدم‌آرومی‌باشم و بابازیکنان‌حریف درگیر نشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/29857" target="_blank">📅 11:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29856">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50dfd8488.mp4?token=CKHbUuTsRp2S0qw7gcOxuQCCg8lo3sBGwI1_XxIH2zJhCeMfX0ml8VgcjeOGkCLELRei3Qrs3hGqmfi1UyvTPDYHIVX4esLgbr-2-DGCfdbCdot6StZ1ZpxvbVFVEDewzmg_YnXPzFdWTbjnQxn8mNqVqFd-P_0v5vNFS2K3VttJ4Jv5bv5J3vD98GVjvqPXYGlLPY9d0UhArGozlySWlTqA3rwgRlBTzXfNyx5ZSkL6lWZ7E8WEP89eLhE2ufFBNwGrRAskp9VxwdnXKoLeoBRuUpF_XohBbMVtaGHeCp9og6LwRRc9PGzBV-33xeQf2JMGi6TmizBz3XiDZosi7JsFR1g3pXWmpfZv4vkZfZqjeJYIG87HvdRQ0ec-AI6JKB0BqCBmDl6UYuDpf5Eyru4EuLBJB9MJ_fJi0pb12e_o3Fygo-dBHAjcFDRvkoCdQOk4qru62P9Nv9f2Wvl0pg-wVq2rDB7heolvlQQv1zXDtN9I7ynJt8BxyCZO3YLa0mMIUrjUI0aULZhZvOlGijkWXPNOewxVM3NcXjHtvnAGORVcRLbI7HyZFTLNfOy300dX9tJPtzEdB0XSYjJcArtuswaxrbvyaGQJNuKtudfBsuBzZZSDcQwK-7p7TGjpo2UVagaTUz0GmUYk6xiSNr_3AdVjLbscTOZSLrJG1pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
⚫️
آنالیزدقیق‌بازی‌استقلالِ‌سهراب بختیاری زاده مقابل تیم السد قطر در هفته اول لیگ نخبگان آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29856" target="_blank">📅 11:44 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29855">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDP5-7CCPW07vFXZJ_tET7IuOPVGmTW65LrZUJ0A5vd3XWsxAXlcpJHPZ4HGaXXLfzcq2DB1EaQlsKukYhMnuYdO8rfPs2ea_Fil4wGP5NIDRd3b6njUjua1B7cyI78X0Y_Wpd3jAFi1PKWAwxPoxqtLfms4zQkgpGE2vwtVoDkKXiU8dOrA9BxOzU9WCn_WDkinltZNJYrWvM03iqKsBExeF_gIV6NX9ls9S7hMEGsohOpr0R4hD-Njq93OP1HKspyW-7MDZhQe3jwEap0pu9DRf1p_kuqNLZ_wPgjZtwcKs5yUOyEwM9gm1DFwZdMtUHI9oqmkGurr6vOkugPByQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه اتلتیک: به احتمال زیاد جیجی گابریل ستاره 15 ساله منچستریونایتد طی روزهای آینده با عقدقراردادی10ساله به رئال مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29855" target="_blank">📅 11:21 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29854">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4P8NEdQqFx4X9AUeA7E0AFXDe0ox0JC3qliP3gSwey-l15-cVXzWbEDFpNJ0Iijo8oH6L-Mmpn7s2r-LjzfX7q3ijzEzX9OUzrABVheQ4bXOhrFSbWQ7dXMZd2Bhuw5zh4R7HnjGkaTQe_eYi8ayXgwWRJmYA7Tk3MC8Fhs2ewgnJhkQj4LDqegdohWprUJJtoANxns-j_US5ZUG7bPk9H0uSbJB93UbZskZSe4d-zcbXcMmXUXqFo4-ZOWIAok-UF9YEsPk0zu15JS1zL1s-aKi87psHI_oSHas8MFKn56hnLKrX_mlf71PMNbSY-HK_CaYGcUm2kNnHST-Notipk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8386c27ee5.mp4?token=ELUAiX1nNyS3YD1LkDWjQ6DrJlw5HqJAcKSBE0Wm4oKOaUvYpmbZOzDK6YnsF35Xu2YraZG_NGiK-E5Sm_PtrUu5iUvuiuM4U7HiyaZOcoMRede0xtAvdyQ-3U2aJgQTqoMolR8Lf3q6CBrhOQsSqsBsghIq3mcqaAWd8c3yrTR7AuwijdhJkg15TMer_L5ghiOFp_QEDI_qgBxsUzTZv1iFem2XMH9fGEZxGo2OhcLCRD_AeUy9N7rN9OO2P0ZDq8cXClYmlWafSNkprhTpc17oWoF6q4GO0iMfwPBe2zq82OegOHG_c-dyDch_3y3RgPWhHr9AoQFlL10tu3fQU4P8NEdQqFx4X9AUeA7E0AFXDe0ox0JC3qliP3gSwey-l15-cVXzWbEDFpNJ0Iijo8oH6L-Mmpn7s2r-LjzfX7q3ijzEzX9OUzrABVheQ4bXOhrFSbWQ7dXMZd2Bhuw5zh4R7HnjGkaTQe_eYi8ayXgwWRJmYA7Tk3MC8Fhs2ewgnJhkQj4LDqegdohWprUJJtoANxns-j_US5ZUG7bPk9H0uSbJB93UbZskZSe4d-zcbXcMmXUXqFo4-ZOWIAok-UF9YEsPk0zu15JS1zL1s-aKi87psHI_oSHas8MFKn56hnLKrX_mlf71PMNbSY-HK_CaYGcUm2kNnHST-Notipk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌دیدارجذاب امروز صبح دو تیم امید ایران و امید امارات در مسابقات آسیا که با برتری سه بر یک ملی پوشان ایرانی به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29854" target="_blank">📅 11:06 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29853">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔹
👤
ویدیو کامل ویژه برنامه جذاب امشب عادل فردوسی پور با برسی کامل اتفاقات این هفته فوتبال ایران با حضور دو ستاره باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/29853" target="_blank">📅 02:02 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29852">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=VC7ChTr1u4uXjbnQ3bRw0wGPRQDRiub74CVq4MPGhFvnez0lVaqe4FXuwJzlPiVaiieuinZqTOuR7ubAiCU5cz4SEQ9FDXkQZzJWxLOzknjbIQt2UUmVMEEd2L99sSMuDaOFHgKvKFhC3iq_tOPGJ6jEMmwInqFpaXD5FvoOBFWjDk2xFNyprP3nr064qvl_9vS8zYSLMWnVRK7VjDEc9NATMaaBnfj_vVPVCfWQ8upRwWe_L6EwmiGKiHkwHZWNct_Gz3GMYoi5MclUG2gMHvhfnpJ39hcggGMTzckLFHCoEOZQ-bEgIaYhBfnwcVNryc7EMtVSeOUMMx5TGncMHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a706b60b03.mp4?token=VC7ChTr1u4uXjbnQ3bRw0wGPRQDRiub74CVq4MPGhFvnez0lVaqe4FXuwJzlPiVaiieuinZqTOuR7ubAiCU5cz4SEQ9FDXkQZzJWxLOzknjbIQt2UUmVMEEd2L99sSMuDaOFHgKvKFhC3iq_tOPGJ6jEMmwInqFpaXD5FvoOBFWjDk2xFNyprP3nr064qvl_9vS8zYSLMWnVRK7VjDEc9NATMaaBnfj_vVPVCfWQ8upRwWe_L6EwmiGKiHkwHZWNct_Gz3GMYoi5MclUG2gMHvhfnpJ39hcggGMTzckLFHCoEOZQ-bEgIaYhBfnwcVNryc7EMtVSeOUMMx5TGncMHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛ صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/29852" target="_blank">📅 01:59 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29850">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ECabltqi5E5z6GEOcZjV2MbRz8OKIGB0Ck_6f-A3IldVj6VbrlEszTlaX1SfrChJb_nRWLDMitXwhFTw0NCYjN0wjy4fOGpzh5y2M3BdZMxnxOBwOK70ylkoDR3zPUXfLaUU0Tt-yheu3IayqiRbVPZKyFkILBHEPitT7OZiaYpJQkOCssjJZfbK8Q0fUynXrYO4pFVNBBDEJOTTf1likvDHET258RbHH8rVi1NIuEvnlczRvPxKSHNrPQTGP8VZCy7F3cirmQbc0rmshSPqTcSOEyw6w-nur5qEBBgSmWdNQPoCKwb7imJg_Jqx7-ruzk22eUjsxACn-bqv4quvVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌امروز
؛ از دوئل یونایتدی‌ها با تیم آماده برایتون تا جدال بارساییا با تیم تازه وارد لالیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/29850" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29849">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ObvmwFEVd1pO8X0IZ0JiYMUEOXW_w-XAovMRJz5k-DQ58Agfk2NSOixHpgR3Eejo78djwOgvfHuB3mUZgBGbg90u1wy8wADXGWGW5AC516rV1TX7pq3TkLso1SbEnFmJokpLe1oG_J1sLOzTm6Fnp1DkcsaYf4E48nARTF0CAzn58dB91ljVJxdOgf0dN4DT37MEno4msZ35MlQ2xf0YWSVSEW4Tt7NPGCjvyJrlCA0UerjXVdhrnxmov_aruYIKxdWKZKH1lPlEJ2kHVWA07Plg13G7rGl4CDfzTF-psju4GdLXo8XzpZcJs_3LC0QVO5AoPcEkzyO8aSIlIrr1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
رستگاری‌رئالی‌هاباگل اسپی و پیروزی غیرمنتظره العین در جدال با یاران رونالدو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/29849" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29846">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lr8_SdRejAcICAp7FBl4X49276FGxA8A_3LnQ51VOPbCh8WKscpvuuDUm9cUkJSDTT_fJYtZWrEEm__Gkm9iJcD3Nm2gmUEQOgCk2Rc0jBS7xLidtNcBYEchGndmIqtElivaztprHx4vOtnfYoy--zOlpZB-r-J0wqpjlZFpgmZGVIPVx5F__WbVJS0QgqFwYU2W7qsb-CsVGmMh2ejdDajrfW-NEP4702AHgmVnvSxyN5Uy21nudZjA3U56cJ_zDnf5eJLdyJrIdKL7RN4bZIZOiLu7lqP9TqxyVi_fypmXFwiJ7-2CxDSU8hg1dx6SCm8mAYK7EqaiEDmnHfyuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛طبق‌آخرین‌اخبار دریافتی پرشیانا؛ مهدی تارتار سرمربی پرسپولیس امشب موافقت خود را باجذب بشار رسن هافبک عراقی 29 ساله پاختاکور ازبکستان به‌مدیرعامل‌سرخ‌ها اعلام‌کرده. بدین ترتیب پیمان حدادی بزودی مذاکرات رسمی خود را با ستاره سابق پرسپولیس برای بازگشت…</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/29846" target="_blank">📅 01:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29845">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPEHLKPFB69YJRrKCXAcnDwLHvFsaFY7nRB6-qD4IzSMDxzEWdkU75f0CYN1BxthTBuEsPtJ_0cWBgmAkQle1WsKP4Tx3quEhDkuQjBhK2NSYLTOQsnt3jLcUfpYYc_klkqEBXfBOR2qI_VnITZKxLGLLI3GBZi10jvWjNLjFlr-87L7yvOGdDnTxTvAhmMkk8CNw9Qv_PWPckDjLMwrlO_U53d7us82t-btvHWXWCVmg_vkEhk5yqX2EWT3IdAfJiO0mfw3703FEVY5lvbmFp0RSN-kq86dqGZUWNJgr0XiS-JmNTUDkbNgfC54kIPeGEHMwncEui2sIaIZ9mAoPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مهدی تارتار سرمربی پرسپولیس تا اواسط هفته‌آینده پاسخ نهایی خود درخصوص جذب احتمالی بشار رسن هافبک‌ عراقی در نیم‌فصل خواهد داد. پاسخ تارتار مثبت باشد بشار رسن به پرسپولیس بازخواهدگشت و مارکوباکیچ و دنیل‌گرا جدامیشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/persiana_Soccer/29845" target="_blank">📅 01:17 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29844">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMaPL39J4b3NbqBkQyckAPxzI8PqTk0N7Z3T9K0t9FvlJI966JANsvTdcvQZcnObyM9vRAGmT01szol4lyZ-tZPFxoQQVXxx7HCdl0o2GrBoixmmZ4SryTLqhkaWbWntHNg5OugO6byAVSW4O3l5iYyA0deYvWvA1wqkBitbi3twsDdtoEdMTzJ9BtBnWCLiDYLc0qsc44rhRTnG6JSE9s8fVknBHohCk3bbjEBmK8eIT6PAJ9-zTRi7bRtD9E9tFiU_9MCyqD3oCa466fq6l8Y4omD4DZ3h8XfJQC7RPbF_s2AGjmtW5VAOyVlU3c2vNbVhGrDL_4ohxdRnpGEK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/29844" target="_blank">📅 00:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29842">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryEn6K9fJRbs5KVZ4ssjOR1nKAKrKSSqXOLlNVKZ_HWeBzu1eEgXTa3vWYzs0FV4Uo1A7mT_2uaHNXhcZ4pkTo7lsJBRU-OE1OHMIZSgXgyHvoA63IRw3DchE7Lrtcy2SxZjvZ0igE7Gegp7a6-n7fTfeUeIHjtBoA1N9jKplqWP5spatHuJau70AApAinlnIdUcpdQsOKh068XXVy0jQYuudyhcRkGvVnqlcDWBmoh6pm9ZS57Z7oIMOki80jA8i0X_OPtmYVHFnrfmTs857-EQWdstaUslRs_pFa2gUv28mCHOj8KN3mfySR_JUvRSaH0NE5UTOjnhOW_VLNPuuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/29842" target="_blank">📅 00:33 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29840">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sUSD-hX4wPmUjdmDRileHuIwjxiNABVNEeioCx09CqGGd5pDRqh1qSb98cUikpyRP0C_53TLK6tQ2tZbmWTww-R7MvdLJwDb0DgZKh_V70jZA-Cd0utj8mrv0OULa7uhTFH3o4DsbIo0P1QIQmasa_NwUYvldYF4ZLxduGG8E3q66kwPhZpvCW4pAjPOk6WtfG3FvVAncwVsaro14qir_yPgZZISYxpVEeA8aBO-c6SeVfZvjM5_ZFULp3MTqrvHUzX_9oiBJ4t7fvcy03mEIL2T0QiXRAwEG54BRmWm4KKz3rMxS7mdX1ko1V3nD6SIFosxef7KL4j3JqrF5A1UDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kFugzN09R8OxjO6KhBzejxPm23li2xZE7gmF01SQXe5QlEh4dMm5Od3MbyIhbJQ42p45H152A-kz5H4WvlBtVW7BJVRMbt4uHT32iq2QIKydRQKEwkWBDC_gJH6HY2diZ2sphdlS8lTFjY6-vzOxsYKEQRfCwFVLfStOBhlO008xNwFf7co1Z0OUq_s9QS7S579YHe_I2RP-IlB2hf3To83DZl0WqVbaqCJEyKP9z4xk5-tuieAalzL83helCVYB5NzKCcaCPk1x2eyAUv1iY9_kG035OJshRmHosnUwbV_ftIlqQyinpQhRtHPoRTWYsxnbVdIQpPD1zCF_m8i7dQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌ شانزدهم جام اتحادیه انگلیس؛
صعود راحت و شیرین‌توپچی‌ها به دور بعدی و پیروزی ارزشمند لک لک‌ها مقابل شاگردان دی‌زربی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29840" target="_blank">📅 00:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29839">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RbIcRTC3FBUKio_9-zcnqqCnRyWa47qPtp75Od0tSDmqV6srq5zmnR1d864OGZW59V4btgZmH5zr768wzg2zu_u-tMG-pVN_KUdt_Wv-Lp8PSqDfrvtopO1tyZTssM8DQxLaFia1dkVWasbOD_LI5a8A4m0w3kMCXNt2jtn4q9dfMK34GYwbs_nIVbB2eWywxEnh5_Nv5bzwS1s8L-xESbA3uCe7kSwJF_G4nYCtBBkg1ZHx9ofbtrK1YF7JzmL9nLTqKLPa_FMzGdZfxxiGkLTTcew1MP6R5A6llXfhfg9B-1E2-OHcfrFnNt4ArqDtX2AaJvb6GXuv9j12JWYGpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29839" target="_blank">📅 00:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29838">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=HcNkX0itIDlEY0C0XTsTIg-rsQRBp8rkk0ROx4XrEX_j5QFqbvlFHxyzM6Gz6DsKCmwCFhAfZ1S8b6ZP-8-bxxivfmL8o5YEGMPq_PRY35nEsrYPgqasb5os2tHJOceAdOX6vmcRuoKszd66QM0USONABIJ0fBuwnpQ9Ybt4_Bk4Ha-qtFDTw-2XCLwb2tTKX8YnnqQ3yt_WO3VLYwpvJ7LDoZTYzO-FbCcdOja9t-sI2mqBArYpoOhWtT7QQPQCO0WoSJt7qI5EsrKgqCACZ6oXaqU_-X1QkKO9ysBK2Lhmuo2Hkxpk61CJWZsujQuo_g9R-VYf43dAC7JEckop4ZbwfEBpuh9LovzY883Lk77I0H54uxjn7s8HxDZ3fFfwzMBiQh1l0OZimCNkmnJrRz2ac3Se9ru4XH_X83rPpJVd7iinSampiFrvWziF9kyZeBTrT0JqEgGCoPw42ICXyJe0x_itC94d7AASLb4fxW6BbimxPy7t2zPAtq9WONpkW1ssYnkdAFTnFVnbfU_q5KryCabniPlxq1F3Hd8LdDiVH5jI0lyYg1GHLg01LP9_YtnMoe8WVTo1Y1TTgO9uKeu5SHHWprRLnj8u52d_sQEkPoCKGRGq8oEPFUjqVSVcXZ-RfMNvRu4Jg2eRIlYo8WYxKCPeTtSUqO5P4qVAtvs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68fde2425c.mp4?token=HcNkX0itIDlEY0C0XTsTIg-rsQRBp8rkk0ROx4XrEX_j5QFqbvlFHxyzM6Gz6DsKCmwCFhAfZ1S8b6ZP-8-bxxivfmL8o5YEGMPq_PRY35nEsrYPgqasb5os2tHJOceAdOX6vmcRuoKszd66QM0USONABIJ0fBuwnpQ9Ybt4_Bk4Ha-qtFDTw-2XCLwb2tTKX8YnnqQ3yt_WO3VLYwpvJ7LDoZTYzO-FbCcdOja9t-sI2mqBArYpoOhWtT7QQPQCO0WoSJt7qI5EsrKgqCACZ6oXaqU_-X1QkKO9ysBK2Lhmuo2Hkxpk61CJWZsujQuo_g9R-VYf43dAC7JEckop4ZbwfEBpuh9LovzY883Lk77I0H54uxjn7s8HxDZ3fFfwzMBiQh1l0OZimCNkmnJrRz2ac3Se9ru4XH_X83rPpJVd7iinSampiFrvWziF9kyZeBTrT0JqEgGCoPw42ICXyJe0x_itC94d7AASLb4fxW6BbimxPy7t2zPAtq9WONpkW1ssYnkdAFTnFVnbfU_q5KryCabniPlxq1F3Hd8LdDiVH5jI0lyYg1GHLg01LP9_YtnMoe8WVTo1Y1TTgO9uKeu5SHHWprRLnj8u52d_sQEkPoCKGRGq8oEPFUjqVSVcXZ-RfMNvRu4Jg2eRIlYo8WYxKCPeTtSUqO5P4qVAtvs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ویژه‌برنامه‌اینترنتی شب گذشته لیگ نخبگان؛
محمود فکری کارشناس‌بازی بود. مجریان برنامه 500 بار "حاج محمود" او رو صدا زدند اونم کیف میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29838" target="_blank">📅 23:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29837">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PERwLh1WUi44XNwHExXgkBPpDle_CNFBpqaTRR5cwCgBLegcAosVFdJx4Mgw6iWRCQgeCmMsgFQ5jTyW1lrWe3hJj55TAGsyXw27pymG6VyQwTGjD6eXoY6NQ6OnMwzimONPxzf_g6z5DWiPTugDcOXkd9HIPShyfKTIfy-MjDrIawx4w_gVc39BaM6_F3k2CEOBTSpIgM8yp_JPOFG_p9aOzY07D2DqqeOuTYUMgfg7Jwfr3TucvuKQD6oTPjC5RKnIQ79T985VjboqKwXX4g-An8KD0qPq6ROAW6XNtrtZ5BSLzlFwOYxjd-rHWrhTTU_OXatLU9tl4Pl2HBn_Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
رونالدو امشب‌توبازی با‌العین اعصاب نداشت، مدافع العین هم خودش رو چسپوند بهش اونم این حرکت رو روش پیاده کرد. 4 تا زدین ولکن دیگه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29837" target="_blank">📅 23:46 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29836">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h1Ga8w-jZ7IgIXf_nOTwO6GzNjsbYplaTFthX534y3d8hzW8ba416nxOguRmGWjic2c-daVksJlHKiKarpp8YsM8Aad1Y9JGRPRFqSeWyTF884k_dWVvIKfAmxr0SYksMuVvmGMzXjkpmIDZvrMyTu2D0B9sK3-O3Ie_YLaHz1UvVpzdQeXBZMNJxnr5Ctls4YlpuiRNdgaK9rPE1aNcxg6jZBGgqWRpz4zTRrkYCOJ3kWpYXBjTAezbCF9RmI67mn8YwyeqNJoTIATTt8eFwY1aE2eQybGH3xAu53LrODSxMUXIjGZTkT_JAGOu1TWoLxdI7lssa9Z9DeFu-BN8Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27d67274da.mp4?token=h1Ga8w-jZ7IgIXf_nOTwO6GzNjsbYplaTFthX534y3d8hzW8ba416nxOguRmGWjic2c-daVksJlHKiKarpp8YsM8Aad1Y9JGRPRFqSeWyTF884k_dWVvIKfAmxr0SYksMuVvmGMzXjkpmIDZvrMyTu2D0B9sK3-O3Ie_YLaHz1UvVpzdQeXBZMNJxnr5Ctls4YlpuiRNdgaK9rPE1aNcxg6jZBGgqWRpz4zTRrkYCOJ3kWpYXBjTAezbCF9RmI67mn8YwyeqNJoTIATTt8eFwY1aE2eQybGH3xAu53LrODSxMUXIjGZTkT_JAGOu1TWoLxdI7lssa9Z9DeFu-BN8Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام در سایت میتونید مسابقه بازی رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29836" target="_blank">📅 23:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29835">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=iFedRU-EL_fqCF-AKVIzwRPUsdPI7V4qXu_1Cvivt2WILWDjehTKF1TRGfuSiEKgxEA9Zzqxo0dQHqWami_wTUZxh-1QQ66ma-Sn-6UbaVzwiFIBKWWKtpny8wu6t41bYKbxANXzMs5JKhkSS4ob6hwDqJq_qsum9EUzbJTmzm5p_6Ap2Z_I1w-IQw2X0VPA4LsLviboYgv8KRq52SX_sH1_NHKl9LIt1t_PY1Pu5vCaNy-RXWzV2MYG5-gH03JR0du3EUSAfifGAbVzFWP_tmzwTN4Xz6BB8rMurz7uNeFEwCO4RoubAe_vVYc0RzHbjEgSzGTy3A6l8CZ6zrd-yoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2095c958d.mp4?token=iFedRU-EL_fqCF-AKVIzwRPUsdPI7V4qXu_1Cvivt2WILWDjehTKF1TRGfuSiEKgxEA9Zzqxo0dQHqWami_wTUZxh-1QQ66ma-Sn-6UbaVzwiFIBKWWKtpny8wu6t41bYKbxANXzMs5JKhkSS4ob6hwDqJq_qsum9EUzbJTmzm5p_6Ap2Z_I1w-IQw2X0VPA4LsLviboYgv8KRq52SX_sH1_NHKl9LIt1t_PY1Pu5vCaNy-RXWzV2MYG5-gH03JR0du3EUSAfifGAbVzFWP_tmzwTN4Xz6BB8rMurz7uNeFEwCO4RoubAe_vVYc0RzHbjEgSzGTy3A6l8CZ6zrd-yoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
توضیحات‌مهدی‌زارع ستاره‌جوان پرسپولیس درباره مصدومیت‌عجیبش؛ دیروز  پزشک پرسپولیس خبر داد پای مهدی زارع در تمرین ریکاوری امروز طی برخورد با یک جسم تیز پاره شد که بخیه زدیم. زارع امروز خودش در استروی نوشته پای چپش به شیار تخلیه آب گیر کرده و اصلا هم جدی نیست.…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29835" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29834">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=TPt185i24zeQr56VdLmCI6oCZm07KbBBe51bvKGsFraE3xYoozJAYVrVmJFEfFgmM4NSk-aEFaBOzZJiabNmoaqrwb7n1R2KNLmTJmqEFjUtnLUbfPfBsBB5QfdvnB1gxO_ZkQeHN5C6IrFye0P0Krf6Z9V30RDGf3BlRfozJV8UEL_nVv7hr1J9UaKk-eZrZYBfRcItFEjqRtTxWRlm9W0ym3Fwd94Naawe3-r6SZwmv8Z9uBxdUQUXzaRnotUU-Utxr8dChjjTmU-6hOznpy8nKQjAHa01d6g4X7DQCkgeiZG7gXtE8xOn9pdCITqCJKhf_87DOFdX9BkTTRj70Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79e41b6414.mp4?token=TPt185i24zeQr56VdLmCI6oCZm07KbBBe51bvKGsFraE3xYoozJAYVrVmJFEfFgmM4NSk-aEFaBOzZJiabNmoaqrwb7n1R2KNLmTJmqEFjUtnLUbfPfBsBB5QfdvnB1gxO_ZkQeHN5C6IrFye0P0Krf6Z9V30RDGf3BlRfozJV8UEL_nVv7hr1J9UaKk-eZrZYBfRcItFEjqRtTxWRlm9W0ym3Fwd94Naawe3-r6SZwmv8Z9uBxdUQUXzaRnotUU-Utxr8dChjjTmU-6hOznpy8nKQjAHa01d6g4X7DQCkgeiZG7gXtE8xOn9pdCITqCJKhf_87DOFdX9BkTTRj70Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
یازده گلزن برتر تاریخ فوتبال؛ 21 گل تا رکورد تاریخی‌کریس‌رونالدو برای‌رسیدن‌به 1000 گل‌زده در کل دوران حرفه‌ایش؛ لیونل مسی هم این هفته 928 امین گل کل دوران حرفه‌ایش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29834" target="_blank">📅 23:05 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29833">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=cV491ItPVxkFGKrQG0o_hTfxl08H2d54pkMMhN3N-3HMfqcqMaqdz5aTHaJgC16J8Vq677ICaYw_RGKklzI9d6SwVJH1N7d2A1qkY3ekieDV90IbCUvz0Um66bZOEWrW5OS2_0jsrdHZ8sUrqzIgL5UuA0MUZ6_5Yty8VqwVKLZUG56p3mMxOwRJqmR2GfATzv9e-Jm484oLKc07_kwXBzbF1pDeePOuPEMEpgah0UnKTrBs0j9LqvjC3GWt_plx9BDzK3mp2Z124RGPd_ePEf0nR4EO2jazLJwScv_w6VnydI0Tg_DYbEwwte0AwjHBa0R7vBsckOwDf8Ltjy0PmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ccc2d841.mp4?token=cV491ItPVxkFGKrQG0o_hTfxl08H2d54pkMMhN3N-3HMfqcqMaqdz5aTHaJgC16J8Vq677ICaYw_RGKklzI9d6SwVJH1N7d2A1qkY3ekieDV90IbCUvz0Um66bZOEWrW5OS2_0jsrdHZ8sUrqzIgL5UuA0MUZ6_5Yty8VqwVKLZUG56p3mMxOwRJqmR2GfATzv9e-Jm484oLKc07_kwXBzbF1pDeePOuPEMEpgah0UnKTrBs0j9LqvjC3GWt_plx9BDzK3mp2Z124RGPd_ePEf0nR4EO2jazLJwScv_w6VnydI0Tg_DYbEwwte0AwjHBa0R7vBsckOwDf8Ltjy0PmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
درهفته‌اول‌لیگ‌نخبگان‌آسیا؛ العینی‌ها بادرخشش خیره کننده برادران رحیمی توانستند با نتیجه پر گل چهار برصفر یاران کریس رونالدو رو شکست بدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29833" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29832">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccmPyXyT9GUdMm8_BdlCEwtvpHJX7SvceUTZEZL9Vq-8ikg9D-WxYdCev1L4G6Rpd3ifgDVn1n3YaYsQOc1sYT9JkAmVeaP2QnU-Ha2SPQfsu527BZYiPU-xU-PnHqN4Vs7P6gW6Pmp10GBG_bmVuNMJ4bMFa-84Hi9aPJbS9OqO2QrJZNw2aNtV8ztWN3KvvSByd5hS0K67fNPVzeNxe7rZv6eFUelCbQngYGlHYO38Fr0dAqf5Z3KuhPrhuZWPN-V5KTyhUaPHXSpUM7gBGN5tWCfQbkTEHrzWj-2LgtmMQFqiHebC_T3cMA11aUUnRTADM0PYjzlBE5J8Lhu8IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29832" target="_blank">📅 22:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29831">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KH24AA9Sp5kg5-ScppSVo2o9BWkF6_BmQHLP6q3cjsMmqWDVvPBVlbdugMtplZSIDkWlG_nc53b32cRgb8qW8fZIwlu7EqOGBQVIUo_j-PlYXbuswupuzinUyQg8iTWRp2O6nAz9tkIKIfQmnznpn8GJr0Y-Lj-KB4CA2Il5UM-0Asa75wZBeWmVFZuGausjBb4dMVAA5p1TW0cPFKF_5paDFeiLvL0xjnbet7HBK86LWoVmg_wO6d5-TBlunBpJ8Ma7d-LAppD6p4jxDxqtJkogZXNsg7ZmYyKXDIhkuzOxMpfuK40AjVmsWVYvMadACMMsnHRloxEIYLDTcZT9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
برنامه‌شش دیدار آینده استقلال و پرسپولیس در تمام رقابت‌های‌لیگ‌برتر و لیگ نخبگان آسیا 2027.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29831" target="_blank">📅 22:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29830">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btKFkkvC56EqRYRGYiVp9GDdahrR6BjoZkH_6QRce1nl6HKUrxnN7sY0te0wkxMW4wobZflRlnFybUkKRbqc--sQrWbmT7pvdjSBq9m634d_Cba9-pLj1yz-_ujjJBKBtWWvffskczMsupPTYV7CKIur_TkBRqWBUp9tylOLWVCH2h08tGp10u3Pq3XVw1qhx-5S7VBUM9rpKHN1zcOZVIoT3GZaWyIChj4w8K2067VqfWSF0QeiJuHWQQvmg9-CRE_X1pOr95uipgkhm943qdORyIxDgmoe3aJYLFxOxxnQbmc7v3A3ieNy-ixLqiEx1X-mjDao9LXtYBl2pdAQyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌ششم‌لالیگا؛
شماتیک‌ترکیب‌رئال‌مادرید برای دیدار امشب مقابل الچه؛ ساعت 23:00؛ با ثبت نام
در سایت میتونید مسابقه بازی
رو پیش بینی کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29830" target="_blank">📅 21:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29829">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8W75pOQv_ruxLqbepaWjPZCsRc1X1agT0QNFI0wChD1hCt9aeZNhsfDZPObPqTGg6W1qyRuGJC5GMfmFSVIb2BtgUuvz4LDWrdeQSfRnlcOLCHQ3BduyZnFb0EUbQ0tPZqmP-0TpKbGCUAhqRdyZjWVjKXQ0lSTLGZprgjp7jUHNkiSPcYmNbWkIjAd_xqOmsFm7XC7Z2Ru7QegTkT4oW0qmSlIQ9HRhzQ52CphAS2MFxvpAcYou8ijENC6Xo41fU6TnjGV95au6FDV4lT9qCtklz1lhedzEyGA7M_D0rLjIlC-Z8mx34Kz_T5lPc8pgdEPT32WkhFOO_mx5VSikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
🇨🇴
#تقویم؛دقیقا 11 سال‌پیش درچنین روزی؛ خامس رودریگز فوق‌ستاره‌کلمبیا این گل فوق العاده تماشایی رو در جام جهانی 2014 به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29829" target="_blank">📅 21:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29828">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">❌
هواداران‌التعاون پیش از بازی شب گذشته این تیم مقابل النصر با هو کردن نام دیگو ژوتا ستاره فقید لیورپول حسابی روبن نوس ستاره الهلال و دوست صمیمی زوتا رو اذیت کردند.
‼️
در پایان مسابقه هم که مساوی شد این بار رفتن رو اعصاب کریس رونالدو که CR7 دیگه جوابشون رو…</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29828" target="_blank">📅 21:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29827">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=Dj_QSFgGLRWAd8Y1Knq3gtoy1LOCihK4My8-CnXfRd1skdLRPKb5AueKh07GNYyKrDvJ53ZphgrM9qI14z5OivKeNEAGjHxg6_OZJosm9iA3E7NwUFtKJOhR6JjrxVIH8KvUI1jUwRfSInI4Quwt-hOvXuTnobvrOeHuwYc0qjhm4k7bn3m2rir2ltme1QXONeHjBe1iQPIld_eBAjHtS6DBzSh-UJpOzPaZSZH7_siCoXu0wzLYVRJfEm1DDL-R9b3qCEwv9dSs3d4fqG9Cn5CWuDkoB_S18fwjk5E4s2Aw8gVI08ltZfG7DVyyZD-5Gp1UkFOAz0xHL16TbgX2nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9e1f9f6ff.mp4?token=Dj_QSFgGLRWAd8Y1Knq3gtoy1LOCihK4My8-CnXfRd1skdLRPKb5AueKh07GNYyKrDvJ53ZphgrM9qI14z5OivKeNEAGjHxg6_OZJosm9iA3E7NwUFtKJOhR6JjrxVIH8KvUI1jUwRfSInI4Quwt-hOvXuTnobvrOeHuwYc0qjhm4k7bn3m2rir2ltme1QXONeHjBe1iQPIld_eBAjHtS6DBzSh-UJpOzPaZSZH7_siCoXu0wzLYVRJfEm1DDL-R9b3qCEwv9dSs3d4fqG9Cn5CWuDkoB_S18fwjk5E4s2Aw8gVI08ltZfG7DVyyZD-5Gp1UkFOAz0xHL16TbgX2nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ادعای‌ایلان‌ماسک:
گوشی‌های هوشمند امروزی تا پنج الی شش سال دیگر کانل ناپدید میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29827" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29826">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFXAyUPHuPYEmh1UYzVYDBSrwmuoqCUHdOcbAmu_O8HS4XYDpbWSRW4r2VLvDfWEDEaTH4byhqN5jUm-mO5eoMUV3_uE8ta9xJN52Fq7hNB5zsO2A9SmtMVSw02TiYvFB2oMfO1ppTFUzTS7VYAzZMUzbeWpCua02LK5F2H3YwdUQvhS1lEt2j02ruAIiEVbYqEX7XdmO7G-Z6QLr78uSWG2wFew4EHhkmNsy82xJkIUVhBZSQKMilKRqtix2pK5lX0avGW0dalQVpFM7DNqOT8x9fZPmOAiqa4EtQHpENWqseEbCdQNiZZgw8aTIkuvR-ISF3GizGTJ4F2PDBstHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کارشناسان AFC؛ سعید سحر خیزان رو بهترین بازیکن دیدار امشب استقلال
🆚
السد انتخاب کردند. سایت فوتموب‌هم بانمره 8.9 لقب بهترین بازیکن این مسابقه رو به یاسر آسانی ستاره البانیایی آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29826" target="_blank">📅 20:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29825">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdwJHn02yD_WKKObW4C5WewwIKxuz-H6VhMdWHCRnZZyY4fUeKQyWiTZ3atPEFDUwBOaYe0OrK-VsaGiiWWW8d0d0W5kpNxwXfeBH8vMtFLqB1_fM7rz0nUzi_lzCNkheGNjiooqWsvZGSMjccjr3xxE7nklruAUqpkX5tkQQdVhy99NNs66_6YlvwhsivDng03QOFmHjV-62QNEm6lqAy_AsLN2EYp8Ou98P2gChT1fPlV-QJA6pKdTToZq_oqviiHfSLlu8ZmIsK7M96dRn6Eia2gNMhjEJkNOXXuoKaifl4BuaJURtLnkl2h_ml665myYe50QTOW_GDHGnHEMRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🇪🇸
رودری ستاره30ساله‌جدید بارسلونا:
رد کردن پیشنهادباشگاه‌رئال‌مادرید اصلا برام آسان نبود. بله‌ابتدا درآستانه‌پیوستن به رئال مادرید قرار داشتم اما بعدِصحبت‌هایی‌که با دکو و هانسی فلیک داشتم تصمیم گرفتم به پیشنهاد رئال مادرید پاسخ منفی بدهد و با باشگاه بارسلونا قرارداد امضا کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29825" target="_blank">📅 20:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29824">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5de2283857.mp4?token=SMdGQaB7X_eDmM05GCp5RZSGrY3Do95AyW71ld5rw8e2g6-Fdms2zgkWeu3v6qa5Rdrz7aXORUn4J6SFCRkZvqOc3p4zJvVTtYuIzx2Nc9nNXRa2yipyGVwGTA7BksWVFbHGPPSFIFdCl2p1aYzNJHBIIZV8QyT8kaQ0uT97nUsMur-128NDv0LVjy8b62hMT0YV-60MFzoCfwAHamAkJ8ZXv2mafk9_W7qiQ99u93G_0hDkMWFEF7cT28edAvWC8PkPXS6dxXjtftV1jH97RIZwl_eDTqmSth-kl9VtCdaell7wEly9D0cQuNrfkR4Y4ilXuqN9VMLAq-W_CQSdUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5de2283857.mp4?token=SMdGQaB7X_eDmM05GCp5RZSGrY3Do95AyW71ld5rw8e2g6-Fdms2zgkWeu3v6qa5Rdrz7aXORUn4J6SFCRkZvqOc3p4zJvVTtYuIzx2Nc9nNXRa2yipyGVwGTA7BksWVFbHGPPSFIFdCl2p1aYzNJHBIIZV8QyT8kaQ0uT97nUsMur-128NDv0LVjy8b62hMT0YV-60MFzoCfwAHamAkJ8ZXv2mafk9_W7qiQ99u93G_0hDkMWFEF7cT28edAvWC8PkPXS6dxXjtftV1jH97RIZwl_eDTqmSth-kl9VtCdaell7wEly9D0cQuNrfkR4Y4ilXuqN9VMLAq-W_CQSdUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هایلایتی‌از عملکرد خیره کننده جیجی گابریل ستاره 15 ساله تیم منچستریونایتد در فصل گذشته.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29824" target="_blank">📅 20:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29823">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1ACfvwJdnRG29j3V5eS1EV2Qtae5Arv4iFmNJ4gp-DLEauFaHfOZcKuC5k2AKhw2MOtyJE3zAj3OIxq2nqMN1ubIkQ8w4ChreUC3A7XjP1XvdObY6eCr0u6oQADygkQQKN2kVP1WEyFPdaK2tx38L1Nz4lDZsbuvn8AEvnRTDldEdXec-O13KYZ-EL5EPmufpIEsnuSOWKPLuPvrT9P8AeRJW3_D3Z2tlEhA4WjAXl1U2yYjJfh8_4q6HMqu-r8thanDm08FFmtqDfeNx24gQUsCXQLLO3uah1IFMwmsjHHciww2Ib2085K1sSRRytaGSUsj73ZwROxKZU0zETVGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ججی‌ گابریل پدیده 15ساله منچستریونایتد در دو راهی رئال‌ مادرید و بارسلونا قرار گرفته است. این ستاره انگلیسی درخواست‌ جدایی‌ از منچستر رو داده و به زودی راهی یکی از این دو تیم خواهد شد. گابریل 15 ساله در 26 مسابقه برای تیم زیر 18 ساله منچستریونایتد موفق به ثبت 27 گل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29823" target="_blank">📅 19:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29822">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jO7PhNwcK7Jc7LWzNj29ugqMIYgvHxVJqi-ZRvOTcbDCajyvRrtteL48_JvGl1dSAtRPHyayZgqCVOQxmsDIHtn_hmSsc7pw0TYAY_S7HKAxGDoe9OBKu_WSUEMDfcRd8FtFcZqGv9IzvfBngv1PKY16byoNBj3GaDpAtmDEN55tl0mIc0SHDwas4IPxVaJCpw15uQmUWXcmWqqHDNbGF50zAmiz4sJLTY_aQ_3KGWpuxTPEZdy8uAK3YGOymse8X3bSsUPdUs9VS7AVDUUH9sOch0-p0TewVp-5b80YWMci_NvoTLa4EzjLq8QX7lz14cmvvf5HXsW4PsHvQQw_HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
کامبک‌پشم‌ریزون افعی‌ها در سری‌آ؛ اینترمیلان درشبی که دوبرصفر از اودینزه عقب بود در نهایت با نتیجه پرگل پنج‌برسه؛ سه امتیاز این مسابقه رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29822" target="_blank">📅 19:50 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29821">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYjqm0VECCFv-wJfAQq61URf18fV1U86qMmF28Rb17H0nrQmGjgYRUho0C7-IaHcyjeMupMqapyWKOYcrSw_wCn_4tpBgiHahIbVX82yvgbn0wgWpjarYKAhAKqq8p-2hHihTnZ02_dI7fUSuM9x2jWU8oFSzIbyHDI1cULfEVjQBX8-Jbik_RLN1as0vkflbt56w5IJqS_GYprlaL5UPylwH167uz7QRxekXPDkGsmw302qEaUgRj3uypW9TldDOmI70nQ5OwBeQt3bO1rLMblOypZUHRWx3LuHuYm9oeGdNxMz9E7yhlnpcDv02Dbu9Pwytz_wEcQ38CtPktF6zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
مارسلو ستاره‌برزیلی‌سابق تیم رئال مادرید: برای هواداران لیونل مسی احترام زیادی قائل هستم اماهرجور حساب میکنم این صحنه واقعا کارت قرمز داشت ولی چون لئو مسی بود چشم پوشی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29821" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29820">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇪🇸
ورزشگاه 105 هزارنفری و مدرن نیوکمپ رسما به عنوان میزبان مسابقه فینال UCL 2029 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/29820" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29819">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HDFqTfPxVc42J73htnJgniyDK0Dr3Vysi-C1spGiv2unfNqXPunAyKhw-OiCe8fOW6z0L5J7NWEqEtAovcj3Fz6IbpTD6XS9-25b6l0WVG_bF4fUub9XYmDaW1POM9Tx1gsIonnGQwsfBsDYExTyJf9HyMGjiaNs1zgDclJMshS4iSFhBKeb45BXSenTH0UaFIzilbg-eKpNX2KQnHSDSTyiOqnxQErxhDTprOqArRuel9vbsDQoOquzCrcQecJRC-XPXHamkmttBuim6SCj-Z2My8NZONOm-3PpRv-pepyl-eYwRKGGebuGD9W1txZQ111ZmnbhSprfjuHpKaG92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🏆
لالیگا اسپانیا
⚽️
رئال مادرید
🆚
الچه
⚽️
💥
باپین باهیس؛ برای تو، پیروزی یک سرنوشته
🌐
سایت پین باهیس بابیش از400اپشن برای پیش بینی
🛍
پیش بینی باضرایب بالا
💎
🤩
🤩
🤩
🤩
بونوس خوشامدگویی
💎
🤩
🤩
🤩
فریبت ارزی ودلاری
💎
🤩
🤩
🤩
کش بک روزانه
💎
🤩
🤩
🤩
فریبت درگاه های ریالی
🤖
دانلود اپلکیشن حرفه ای
💵
درپین باهیس دلار با آربیتاژ 30 هزارتومن بیشتر ازقیمت بازارمحاسبه میشود
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g24
🔗
https://t.me/+FafS3mPlOZAyOTg0</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29819" target="_blank">📅 19:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29818">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pse1bZfThDZCSdljCc3MiV5ddkzRwe5enFdHAe3d2AZIvKwnBdWpLYzO47jRM5FyrdPuAbmGy05W5QynEmINoTEFmok2vKfM1LbwO097ZuWVlHDxUn5ILHZ2bnBmEJOidzZ5n-YTI69GuBu718J3xbMskl5_3i6ZBBydwUWLRQV8Qy3976kDHd_iAAKBdD1PwII6TnGz9cBixun9sBN1whymAC10vgeqWnc_Xt3DCEiS0eB8DriqkwXCqEWDPP0N7iIOnZ3fxBZTH5DrVtyFa7H5T_vnvfwM92OC_x6-t17B1jzfhD1Fg2BHNMDZpDgASnIzyRZFYZFHVZYA3HabDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29818" target="_blank">📅 19:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29817">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiDS4k2hgPOSBdQ8YrlsICmpCwjgV4IoIG9fWxa4NQCXKe_bsSuJs6XfvoqDzB_KGvZ6zzm5Ro_jTPUshNRGYDSIeiUBn3KBEgkQg4dxTyi4n8chgUj8u-L1FrBGVIDErnEf6OzNO0wu9QA9dh1z240CnkgHSQ9KEgQ9d9HXmd5sF1BkQvHjbLx_JDry27bqRN7_mP8TxhkyVFKqudyJQckWsJ-Ha-IwjYwenXyQSETADqAgo0HvjCqaPoXrPkkQnrssCMVZ9y6NHr8lYVIvKjYmpzAtDtqW4ORpha-Eofa9V1wvGvOxwH-LkVi9gf2IP2pqtmfOrKVXgzvwT_GZGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/29817" target="_blank">📅 19:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29816">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paKyJQdbKm3ORuWrXDMnR-PVN3sIPl1TQqgd9v75N1oWzdxD9ciPVHE1xXOMa1A9vLldBqr0udXcvPGjAth1rjEXRb7pVzehfexw7lhwUwos9lEHQ_zrOp8JBzdkTpDgrOdVh7fwIG6hdZLrHTPnnK8EV7aqU2l6sH1cl9j1qHz0T9JvAoPZxKsVZLwLHHF1qGXJKCv-_-EOPOuqT9BqKAPmAeTr2x9lJTA20DqKLpSmgc_74pGtenLgeh2VhpSmTtvhKXp9oOBP0DwcNXWxJ_3rH8ZeEL7u7aY54p3za-EknNql8HMeOIwAShBH8TN7h-pxYMwwVEb-OBc72flAng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لیست‌کامل بازیکنان گل گهر و الجزیره برای بازی امروز دو تیم؛  اندرسون تالیسکا فیکس شد؛ 17:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/29816" target="_blank">📅 18:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29815">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nP0rykm2nXc_AsIn0j4Q9kPMQnEPNRG5zlAXGBQja0fJ7bsNl2tEpuD8JtKeHK1jZAFMsnzgydDc9sCt2wq4Kok3eRD35ShqMJDsbNoeghn9Zjp8BMUpGU9a1xL_uEYmp_GOdX-WbtuWz9Fxlxa0CSdYk1C0AvMVlUrkl0e_fAxkIOQ_b32uWbd3BRmJTqSQgpJSGf7OAkXjvKgwPMa9eq-eKk-nAXT5NpQVCjkFBaRWknWfpOugrVGdOMr9J_nypiYARpgEYAeWdx1vUrxzrnqvNXUyN6eHolD8eLBNeIUMlOSvY_1wdaNJgs-Af8lP1J5yr0WtAwC8cAH0PwdYaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تراکتور از اول‌مهرحق استفاده از علیرضا بیرانوند رو نداره اگه بنا به هر دلیلی بازی بده اون بازی سه بر صفر میشه و نکته بعدی اینکه باتوجه به‌اینکه پنجره نقل‌ و انتقالات لیگ برتر هم بسته شده بیرانوند نمیتونه با فجر و ملوان قرارداد ببنده و باید…</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29815" target="_blank">📅 17:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29814">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9p0QsQhqs4t5NUS4JFT-GKY_sTvEEfG6wbiX_7x2LeZFvrKvHtzKuoL4siNW53huQEhmgsthdsNPAMxtiPOXlVNPnILtFYBcwnVt3HOYTQyT-f95OIfDfvdBxFW8RxZeA-kxMx1Pj6p1E0tFgWrYzAsUWl3RdLBHXTJD-jKNibXjseUYXWKid6nqMg9PT0cfc8rUcHTLRvdyePe6fsKMb_9ebaUh1pULbHYSTo19IscTgG4SVO9ejsEL39ZBERZ0UM7b6oQA9xxnX3b8I0MXjF7HgUwkmDM1LsX19IzxXX0XKhBxQGQXr1tfokIoGNMnbpWCiI3ORC2jBo6EguXkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
گلزنی‌دیدنی‌لیونل‌مسی فوق ستاره 39 ساله اینترمیامی دربازی‌بامداد امروز این‌تیم مقابل نشویل صدرنشین لیگ MLS؛ بازی دو بر دو مساوی شد. این 928 امین گل کل دوران حرفه ای لیونل مسی بود.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29814" target="_blank">📅 17:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29813">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urKXmHuvwrCFFVptR20s1o_-WUcEqRwxWad-axwhvPwZkKz2n8G7Fm9TvYggEhSPvl1ww_077R_w6nwWVz7vF5Pj6TRyhiGZbAT8GKjCGzxNIm2g_SRKqGtSgYk1RVrsnlXrxRyiaa7gTzSqF85HHoA3BTH68_3VRVLZyXBjZKp3PJA3arV24hzmlzJA8NwM2sm3k5yRoOCenUi1Az7nRYPlPaSjEyzsn0pyFVWhF3DpMW2acSqhQ267nssu9MiolptyitR-AL8WU2rAcz-FaX3ecr5K5YslOzDV1ZBcSdgJzR7xD_NOj3J73DBinhlRcVT2onQCrjtz9PGPI0vrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمپین تبلیغاتی جدید سیدنی سوئینی برای پلتفرم Novig هیت زیادی ازسمت ورزشکارهای زن گرفته اونا میگن این کارهای بانو ورزش زنان رو جنسیتی میکنه و اینجور به نظر میاد که تنها استفاده زنا از ورزش این حرکتای سکسیه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/29813" target="_blank">📅 17:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29812">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqI26eCWVlzatPOmYapqR4TEHi3wuVeJU2_yLc8mnhCPLNT4bEMSbRUmXcFCofTpddQvnSTxEPB6PjC6CET4y23y323Cxx-o5shLHDEFSBi385F0ZfY25LeeJu6Ftb2dpos7qLVFU3-aEBcP22cfsA4DwGdvXA8ToojPGvvUpntQCrNSlGiWJsmsoE6HIKL8unBARc12eqIBEeJFZ5c_cTszCQhK9D1wKXKO-ebyvEX04TMfrqlzEb4BChj1babjtXP_a1QQGCrnkbYANyIrBzW-kohk3Ay2AGWh1vjzuLKZQ09facwvjfzqdXzMceKJwEyaTjo6IU_KXaMkOpepYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای تیم امید ایران در مرحله گروهی بازی‌های آسیایی ناگویا 2026؛ فردا اولین بازیمونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29812" target="_blank">📅 17:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29811">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MddJbgAub8yF6QXa7Y3q9XY4Zjw_aTo_gFqZSjPi30gAePcb4PPSykiCjEhrh8nvGGOcT8Q_Yh6-9UksVLe4-Hqsdjfj_AAEmVjihxB-CH8p_UUB3SpH7wy4YeZ00PFAZpX2xt8aT65Pc9HHgvKMumjYwgSUYdSz_TByI8BAoh0b7seikyhIzg6thYBOsgokTaLuoVdBfBCbt75s3HjERCiLagZnGaQGphttuSVHEwkujag95ubBaOjY8Q0Lu7hR0nrj6SG47QYdtiJJVpLWg6EGJv1ESWDi03D7HCCWOTQHeafelvr_0aZjnxNqeB4mrdCByo8yRq0UnvuAWLjOHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
ویدیویی‌زیبابه‌بهانه خداحافظی مانوئل نویر 40 ساله از بازی‌های ملی. نویر گفته دو سال دیگه کلا از دنیای مستطیل سبز برای همیشه خداحافظی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29811" target="_blank">📅 17:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29810">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQ3OKRoNN4XPFv3vUyjMLh-pzMVUMeEEw532v3WH6PDOMty_J_Ko6rhhA4qs0wyPDPVR-BS0UXqaRbz_KXT6_ef-d5iIHkm8bPV-RAH6xf8DWJVSKdBrHqGgyebH8wJfu0UPJ04WNMSkHrEM2mnCtoANcr3gDET67ObHLFp5gzNAkAvWwtL95BBb_OK1n5v8eyYOa357Pu64n5xyIqmR5jgWNEmCzEWMHSDlruSxHotSjftTGWdKQHPr6H_5_TbWhQnvcBCN3pspP2w1CZFX0JEx_NqWKOxuzb_I3Cyxfn7qA-OeQ5W8twrZ6h3nyMTYzwmiooHoSsyPFlS2be9KhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛ تنها خروجی استقلال در نقل و انتقالات نیم‌فصل محمدرضا آزادی مهاجم  27 ساله آبی‌ها خواهد بود. مدیریت استقلال درنیم‌فصل 7 خرید خواهند داشت که جذب قایدی و حسین نژاد اصلی‌ترین اهداف هلدینگ خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29810" target="_blank">📅 16:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29809">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKwirteeKg1050L4rUAqDwBx1EN87LB8ly1LgXiuEo_h7uS9NyMh6hQWu0o4NoBJNz8zFkzHeXLdilfA4998XvSVIzPb7N1i7KhxafBfRdlcdHXjKr5sNUrIlqFmRwXB5lKE-GdrZVDsbGF0YlmQdYJW7M5UOUUM2OImBseWQq41N4_jFv0CH2c4hn2HCOY5HJTwiKu3rIo32z58uQaXCq6vrOdqPcWmtY9Lw3-i95gxQbbdIRMocepWsCKGEX-XqYQ3_WcuilvRUbLQEDcOd6VqxE3qS2zhV_XhBLaPgwTAb3STOiNI4Xn0niolBYt09u3OMo1YmQH1FaxOA4Obxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29809" target="_blank">📅 16:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29808">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5h8u-T_qkWH_wxGxzCwZOPf2I7wR514sNO-KXQjjfdVucbPVy4sQWLwytk9qFjOLykwqYR8hOnuqV36BE71VQ8Lb_tLl0QExsdf72-7zO9IHKzZL8YOu8B2bgviE6Fx1RGu4Fz99rliy53zO4t5FtdZqGexkBWQfVm9WRdpoJUVXfujGrj60aJdEtS6QvxFXb3FSJSv-CXgfgWGsX1Mi4GF_AofH267Ig7-axeNMFB4sMa4nw0YddY20s0dtrFroIejMRwO3xw7RJNFoZuTlFrjwTNJdw0PNUZxiLjJl9L6Ky3crR1Cw0BbNDCa0Tf1gMnjw92EZ0roxqllRZMslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ در قرارداد شهاب زاهدی با باشگاه جوهور دارالتعظیم بند فسخ 150 هزار دلاری گنجانده شده است. هر باشگاه لیگ برتری که شهاب زاهدی رو برای نیم فصل بخواهند باید 150 هزار به باشگاه مالزیایی پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29808" target="_blank">📅 15:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29807">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0-r0yx_9l9b9VNNTTXPSRTMO-Oje7Lp3jJfT5kPmDScSj0rO41in7iaPfRhqruhEWuAKfRCl3rYWlORlX5RLhDY6M5j9b9necYSdjSoHnogTxXXSYDkbnjTSqUq70C4aC1Os7_T4HBGKFO_K7Xc4lpgNzYoHbCGvcPYIOFy77aQdCA8zjDavzsNm8sHsYM4490gvnEYMqxkDUkfEx9wxMSCY_NjYH6yhqFZ-zGBEz-MyDXgjpeYUALK_L0tP-prh3FYQ-sc0FBguC9jRBV_whlGiqsFsIoFZ54PmAjspty8jRRWHnh1obD28fkPESvTSXKanCz8pSxun_n6o8pFMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قابل‌توجه‌مفت خورایی که با گذشت حدود چهار سال هنوز نتونستن‌آزادی روبازسازی‌کنند؛ ورزشگاهی که دیشب‌استقلال دربصره‌عراق از السد میزبانی کرد ۶۵ هزارگنجایش‌داشت و ساخته‌شرکت‌های آمریکایی بین‌سال‌های۲۰۰۹ تا ۲۰۱۳ بوده. هزینه‌ساخت مجموعه به همراه استادیوم ۵۵۰ میلیون دلار گزارش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29807" target="_blank">📅 15:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29806">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lce7TUlr9P31xxva1KC5A7CQMFngnPyHADm2CkkVT51W-m-s9guDSmxygw8LehlU29e7rktXg3VtZCAKZKZ3ZZuTNnsnfG1VoN6XwzBCbEKVKT3P-s0k54NhX_cqC-dNWyARuTwwH_L4uhDpazH4RLkP4KTyABFLBR_WhXstnh7jvSOVMDIXfhfg-ioMtK8v-nFZKIhl8jwwWfX_Xq1v9m5u630-1GfrvWjjuTePTAky5-n3B5ABevbQqE2_wIIMajScKq7Bx9yo3oROv_y9vr3mxNr_T59sFIBNnH9S6Ti2mm9aMuvQZ_7eDwZcbIaG2yxUrZT5CVNbJpsd67CuVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
🔵
طبق شنیده‌های رسانه پرشیانا؛ مدیریت هلدینگ خلیج‌فارس پاداش 500 میلیون تومانی برای بازیکنان استقلال درصورت پیروزی امشب آبی‌پوشان مقابل السد قطر در هفته اول ACL تعیین کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29806" target="_blank">📅 14:47 · 24 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
