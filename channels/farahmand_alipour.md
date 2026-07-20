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
<img src="https://cdn4.telesco.pe/file/DhagzxL07yQhsjYeVb6Gs0aKX4GzOiQdpKhqv-EjXOUxuHVS55sxq4mM5JXB9cvkAAorSaJU1cVQ4ls4AYxarIGINnruzNKjr2rjVoDK43vWQ_dG6GB_M_NBlzEygyi92G2-TzbamMu6BJVLiKekOB6i0-DH0kVir0RziioBAAOKDXrFwAS30QYKRYmaP4e16SfwGy4lBmwUkfk0kt94upjrDDcamoX_rN70jGsTJ-Y_13HF5EJ56gb04UKFPDAb8Wfn9_3TURZVRd3p7R9dT5wZuvHX2YcnkDnjCfT9r-S8MgRxPtRWQu3xGdkNZwzkuMulOBSYX4jB1ZleeQAfRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 65K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 20:21:39</div>
<hr>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJ6rdm-hlmlotnbn9FaHxJ0RX3m0GzYfYxBtckZb0nIVWIxdx7j3lcHH864cKmsuIm0dwzJ_y3pBMEhdxArYfoBASdyluMci6fDXNIOVO2ZfEVlGnnd1FsxHIjDavIXSJWEULKrkwWBJ_fE55yeUvSO5hfN2ybvq2YBoc_Ts1WgzkBvyCkvriILoNLFpkToCbfh2SQfw92mOVU-kT9PVtCbyXf1bqQIwKdbg3ruF2SAB0GRlHHGLSZWBQV6o2sSUAsnod26XixMpiiMLAwZK1FmeCnc55yoqp54QRTdCTecsWubf5pSrh6dfhuu7kojcma0VHqryzf207W9pgS5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlNGoBP_zp4PgiwudZkq5odweOQ2uaMM_6xVDo6Dq8arlPkda4xu-ttOOsPaAoxXXOhN2QCTnYryoFJPK51WUha-2civah0yFAJ50qrdmBcdx1_K0_NksdVS-KAGY2HA-59mMw1ksy4dqE1Ec2JU79SC2_c3OQBDbR46WAQzXLsCNfQuLsauWQ1FY0BsQupo6VvJoGzpedWIyfWGiiAcYBUOp9Mnmmenp-2uSXfTkBWFzCzrKFdwQyDP_eerdTg_IruTjZVfj9qK1LH-K4L7TEeBSDmH36HEwKMgs1_o0-l-Fl8LCBRFh1RGnWpcHIUhMlcughL1qWMcDLfqOC8vBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qcdmousp0lVeyaVGAmZ5EDquZe0KQ9zsmf3709S9R8ZeqxtePuTSnNDAXcUPwqbAAHKBQKXZoHHu6oJIzGuV5VAaxi6cA8wfLbAkC90h-w-mFZ0wmt0C1zNKC9k96TcPCgbpciThDLa1s3KfYo5z7IEPaWiO-1RTu3ArcS4W1HrK-zznAeqajy7Q6N_0RRiLmoTvJOSRDxyf4LVOc46SHTMfwNXtXFyVocMmTS8i8HJtNIexcnsZAnW38YOKd0WH_uonoTL1Ni_rhglNN_gL0JzM6KI-YEtIWActCDCfmGzrOVtwMoeUrxGjQBw3tbZkS35k7lSzsqbSnnbqfdYzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تروریست‌های حوثی‌ تحت حمایت جمهوری اسلامی یک
«
ممنوعیت
دریانوردی
»
را علیه عربستان سعودی اعلام کرده‌اند.
آن‌ها همچنین فراخوان‌هایی برای بسیج عمومی صادر کردند:
«از همه می‌خواهیم که به بسیج عمومی، فراخوان همگانی برای مسلح شدن و آمادگی کامل برای تمامی سناریوها و تحولات ادامه دهند و جبهه‌ها را با جنگجویان پشتیبانی کنند
هرگونه حماقتی که دشمن بی‌پروا، یعنی سعودی، از طریق تشدید تنشِ همه‌جانبه مرتکب شود، ما با تشدید تنشِ همه‌جانبه و شدید با آن مقابله خواهیم کرد.»</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=V-GfGla_5EIojnHgbsZVg18Dn7lbQv6aozxX24bwMZhC-slIv8wewcWxnS1VrrrkrJOeJ2lXub61RMh7ezzNIBc1ZXsHBfuwcbSJied-hK2oVS5-baLfEqn0OQxcITrwTzsTiL-e_rsya2oGdLRYOqlhu06u8Yv5Z_q4M0QGxxTAvzaPSrJKfrZjsho0EEsw8CbbewhkbvuPJfGR2ToRAnYc5gWomlkwS7Yi4zRpIaqz0iyaJLQPx4Ma1QB5e-JU6rpZs45nfdxinN2EqJOvWq4y2Vg1sc29otF9ICWCOgFniEP5zwXBM5YuzUj_5fkxygDEUlfzPxDq-JOqBYCtSZVTZlMrFgpbRgAcpSQZHkUlDFq8lxhZ-sxa0UGKSUdsqaCWDT8ZWbD_dLkVYXkwVL9F3O2S0mOTvxhAOXww7apzsfJHRR67enkf0DPSD_0Nq8G7LPRObthHmQr6AeSCdlvn4vx1EEKrM8-lDRMLPUPug7rub1e5dX5pc7JPnDRJOsOnF1h3fq8maigf6yTnsb7Hg5e4L3FcrfDM-OQKrqcQf6GKHpk-1-cii_t0eFlC-saaM7yyD4Xr8iEqNL889xHzhXHcs1JYgelUviVZeEdWsB0hGZcfl-vkxowuh13Y8IAcGr5sYsovfpu33nuuhFY0nQSkw2uyzGaHPT6K9OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d8904c5eb.mp4?token=V-GfGla_5EIojnHgbsZVg18Dn7lbQv6aozxX24bwMZhC-slIv8wewcWxnS1VrrrkrJOeJ2lXub61RMh7ezzNIBc1ZXsHBfuwcbSJied-hK2oVS5-baLfEqn0OQxcITrwTzsTiL-e_rsya2oGdLRYOqlhu06u8Yv5Z_q4M0QGxxTAvzaPSrJKfrZjsho0EEsw8CbbewhkbvuPJfGR2ToRAnYc5gWomlkwS7Yi4zRpIaqz0iyaJLQPx4Ma1QB5e-JU6rpZs45nfdxinN2EqJOvWq4y2Vg1sc29otF9ICWCOgFniEP5zwXBM5YuzUj_5fkxygDEUlfzPxDq-JOqBYCtSZVTZlMrFgpbRgAcpSQZHkUlDFq8lxhZ-sxa0UGKSUdsqaCWDT8ZWbD_dLkVYXkwVL9F3O2S0mOTvxhAOXww7apzsfJHRR67enkf0DPSD_0Nq8G7LPRObthHmQr6AeSCdlvn4vx1EEKrM8-lDRMLPUPug7rub1e5dX5pc7JPnDRJOsOnF1h3fq8maigf6yTnsb7Hg5e4L3FcrfDM-OQKrqcQf6GKHpk-1-cii_t0eFlC-saaM7yyD4Xr8iEqNL889xHzhXHcs1JYgelUviVZeEdWsB0hGZcfl-vkxowuh13Y8IAcGr5sYsovfpu33nuuhFY0nQSkw2uyzGaHPT6K9OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو :« ایران کشور ثروتمندی است.
یکی از دلایلی که امروز ایران در چنین وضعیت نابسامانی قرار دارد این است که هر پولی که این حکومت به دست می‌آور، چه از طریق کاهش تحریم‌ها باشد
و چه از محل فروش نفت، آن را صرف تروریست‌ها در منطقه می‌کند، حزب‌الله و حماس می‌کند…
.
در حالی که باید میلیاردها دلار برای ساختن و توسعه کشور خود و مردم ایران هزینه کنند، اما در عوض آن را صرف حمایت از تروریسم می‌کنند.»</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=AM5aqFRw48bWB3Aug0gRhMlTLAP7WdvAd8VUYcgBJMIUlH2HWvhoobesVRdDp8q5L74GzzV8gMUKUMXySSfhNHWGWmDogwnWFncWrbKMMXPKtBM_FgcEwoaAFb0rxk9MKzUH5WUvEDP4VvqSApvqCS3rda9MIDMuhCUYhrA9kSCr4gqCYB_wtuYAaf_bGd45aRCQ98iU9L8DIthkTNpTsEevNN5nqQh98O1lzowGUP_mJc0EXW3XGAYB9rju0yEvG9bTvCWqmuCqjo3fixjWKJVAm_xtw0evH2e_8nur7Cq89Ir0cLAi1ryG6TugqzHluikFbVnw2aJYUKfkesrNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e62469a72.mp4?token=AM5aqFRw48bWB3Aug0gRhMlTLAP7WdvAd8VUYcgBJMIUlH2HWvhoobesVRdDp8q5L74GzzV8gMUKUMXySSfhNHWGWmDogwnWFncWrbKMMXPKtBM_FgcEwoaAFb0rxk9MKzUH5WUvEDP4VvqSApvqCS3rda9MIDMuhCUYhrA9kSCr4gqCYB_wtuYAaf_bGd45aRCQ98iU9L8DIthkTNpTsEevNN5nqQh98O1lzowGUP_mJc0EXW3XGAYB9rju0yEvG9bTvCWqmuCqjo3fixjWKJVAm_xtw0evH2e_8nur7Cq89Ir0cLAi1ryG6TugqzHluikFbVnw2aJYUKfkesrNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئوی منتسب به حمله و  انفجار مهیب دیشب به تبریز
مدیر کل مدیریت بحران آذربایجان شرقی شب گذشته در مصاحبه با ایرنا از حمله به یک منطقه نظامی در جنوب غرب تبریز خبر داد.
برخی گزارش‌ها اما حکایت از ۳ حمله به اطراف تبریز دارد.
حمله حوالی ساعت ۲:۳۰ بامداد رخ داد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okuTdKje8YFPAFaFtT8iK04tvGrvGBhCNweAigICTl9Ss3tUNEnsWFHD3T8lwxrziHEaL7O7HnifRaA5bKCU7hyJUfEPc9iO6bvbB1i9qyudjd762YYstJ-EEWxNljb0gQnRllat5LadLyshVFo7sPM7NMe3zPLXFpfSXZAsodvNPMUf1xwvDbM37nYdMMJxWqkLYVArVb0icyZcVGKPskPw-fT6JP17nxMInNiwrkuKv0thzA7i_SuzJn1ATvKYmWRnFk2A1elhgbvJXmYlTQ7VlmXkZsGZZGdFrvsrLBoV1rgq-UQuOLIJACpGEZexpFm7kscXgtjXwtPOLpbedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
یک نظامی آمریکایی در عراق کشته شد
به‌ گزارش سنتکام :
یک نظامی آمریکایی در شمال عراق دیروز  ۱۸ ژوئیه، هنگام انجام عملیات انفجار کنترل‌شده مهمات منفجرنشده باقی‌مانده از یک پهپاد تهاجمی یک‌طرفه ایرانی که سرنگون شده بود، در جریان عملیات کشته شد.
روز گذشته نیز سنتکام اعلام کرد که در پی حمله ایران در تاریخ ۱۷ ژوئیه،
دو نظامی آمریکایی در اردن کشته شدند و یک نظامی دیگر در وضعیت مفقودی قرار دارد
.
پس از یک عملیات جست‌وجوی گسترده، نیروهای ارتش آمریکا امروز بقایای ناشناس یک فرد را در محل حادثه پیدا کردند. روند بررسی برای تأیید هویت این بقایا همچنان ادامه دارد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rIOQVfZhz0XXHmouuOFUMaUiXc2QtDnpHgcvJ_6lMyLvPvs8vAbQMS96y4x7Fu4lDImcltyaeO8qcsieUdVVrjqKvLhVz07RWiYvEFnCkc5oEGMA-lLoYN5cDatcaY-zGj6oPI7Qm46NNOvRDBhCi4U1Jlq8OEUBy_4XnOo1zaqrfKEbt0K5KwyvFFMkdEg4g67rxaIVirQN9_0UIn_o8wFWi8hihh2gx97z3j5bs0XutuWDNU7b4xStT6ya4yX8-Ag8dIL_Q6WPFsMnI9tyJXPXa5_fgJOgJpUDHnJ7_LSTh7ubMeAxPL1wUlAXvn9ggmQQZSi1SaUNzFZR-02frg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tTz0It8Kw4G-Ucv-hxslvWXTBkJ68KPDhYyCb2FAX5DfM_z-t9v-qs7KJ5muCU0ki9ONoBwN7hq2OtbmGgJws--F6RA4O7N2vsrYxIcP8ilEZ54JEDuvc0HUQuW-5IWNkQkP5kzcDOsfyiiyNh7aEyUFMnZWv6Cj6vm0g65PA4f_arnZ88czs6u2aUYakS8cy4IASf_LIZ-Y4p9zG5NlL6ucNPQQ1O66tJJZY_XBIVI9niViumjq6YFoMUIcjZVqk9tZLsBz496I66PJtufiOynwt6QTDu4VtpcaR3ua9SI4JVx-0pLwQdtbrWRUyAAP5ZT0rHp_rheXRm1gSTmR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cqeuu4ceKzOBlynP3mmG4SHUXB65rc4HB6tm845uQ3o8keyMxYKKgyRhpth7aoa6mCRO8znjouz6urvggBKWjyzXNKZV7-s9CCvU69nncXOo4MM1NC0CpyJU2tAoOBhXYKdEZHy4Io7OeASrTyCZ506WD6gItONPMyPu18j99j3kqbBFAukiA4QXEvTiYUtIT43c6fh4H0QF0Dnh6Bex_FiQvPegKkaOrxYxuPzumaJt9eekU5re9azpr2jhBkbcpQpO756NaDWKRcC11CCQjmBsx_8PCZwHARWyko5CFJ0RMLqfJmRUfA1txUD0FZsoFBnd5g57KoJlae1l9ZziBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=vuqUiTO9uut6KWpMs0sSqEYscZcSnH60AEIjX04I79zpCP6nq1E9p9P2r6il71PTsvJ_00mMSw0wxJejoWxZA888kTHu0a3ub8a9nP5LY-E0DzHrgeM-SnKhpardySavu28NDH4AwKwjmTYPkhRBI_VoQoVoKOq3DummraghY9cmcTWNtTMKJd5I1n2ntTVQF9R3e5gXoDoTLsmgSOMl514bbfCLPv7vj2md0dPEDb2oggxKSzu4o71GenHVQJZis_Q1MixuicZRA3Fe8COsllZIXyuq9khJKUzByG1e25sX-wmLVxUkXEXeZJWs8sJHwzgkEGoEMmwuszTisKJdkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=vuqUiTO9uut6KWpMs0sSqEYscZcSnH60AEIjX04I79zpCP6nq1E9p9P2r6il71PTsvJ_00mMSw0wxJejoWxZA888kTHu0a3ub8a9nP5LY-E0DzHrgeM-SnKhpardySavu28NDH4AwKwjmTYPkhRBI_VoQoVoKOq3DummraghY9cmcTWNtTMKJd5I1n2ntTVQF9R3e5gXoDoTLsmgSOMl514bbfCLPv7vj2md0dPEDb2oggxKSzu4o71GenHVQJZis_Q1MixuicZRA3Fe8COsllZIXyuq9khJKUzByG1e25sX-wmLVxUkXEXeZJWs8sJHwzgkEGoEMmwuszTisKJdkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7R4EKUXnSpyDYybnm96kjXCHUAEzrzGT7HPHz9sBtSmPYQSn5DTt5J9v5uAeBHwyN8u6sCrTsfdrne2F3R-WK7ibwAYuveDkHR_mHPP5sh9Q_o-76b4yYR1pxosJ6OC_x8gGEmJ8ERRYZwYqBLcsOl-w-qG2LhgZ1WZJomsRY_yk5I_y33nhuhfBa20lwufckpEDvolWpnK0d7qPVm_CJjVqm5E0G6zJW2MQppnlEcogUF9bwk3xsotTtSqLTqaSJD6CpbPwUjTktmRHYy8klVjuFkkotCde4_2O_eqMFH0uOq5sQ90Ad-APSsGC6aB6qPYXCdEDAlmpW44d7S7qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=DWoKnBQmDtsyM1tfFgZIU9A0NIR8g-xcB6ekQ99Ho-8I8mGpYHOKBpfVC73EHxs8m-BTN8kGMmHgRS38UO3h0apUrFDelkVb6SjvB6ZAtq_Dfbx0fyvVevjVCBP2ar2clVwpJvpe0Zpu8S2RjNWsFbv-3JBuS7UNJrhpDFKluJfPC6ei5QPCLGcvSj3UKQv5rNcJOBrJt1TD32Qi_qDD8FalDTlgBrn93tlwXnMs1ZHo2gORq06MB6OqJZ_SWLLWZs5VvI1c9ZulQtc9apAjtaHHo-HTECatXk9i_0xGHYuHt_ZaHmBp20Pe18P9oc7AjTH1uiv9VlK9PcyNvbZg4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=DWoKnBQmDtsyM1tfFgZIU9A0NIR8g-xcB6ekQ99Ho-8I8mGpYHOKBpfVC73EHxs8m-BTN8kGMmHgRS38UO3h0apUrFDelkVb6SjvB6ZAtq_Dfbx0fyvVevjVCBP2ar2clVwpJvpe0Zpu8S2RjNWsFbv-3JBuS7UNJrhpDFKluJfPC6ei5QPCLGcvSj3UKQv5rNcJOBrJt1TD32Qi_qDD8FalDTlgBrn93tlwXnMs1ZHo2gORq06MB6OqJZ_SWLLWZs5VvI1c9ZulQtc9apAjtaHHo-HTECatXk9i_0xGHYuHt_ZaHmBp20Pe18P9oc7AjTH1uiv9VlK9PcyNvbZg4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrtY3jUUeAtqnjr9wDdpaW-mVE10SfpAlSMYL60UDXXj03kbspMW27-vYb7NeqMZeEGARLXkKEmAPuM0HeZfPsUs_u0S8jCu-b1-tGquN87Q_hHz6yxRWAULj6MD0uoaGuFVIGNdFxHMk_A35X293Irja4iJwg7KQtVtmQiab44qqO8RB0zcUSQ2bME7Gnwo07y9Axk07f9cwl2pQn5fNZEpXsTB4-hhhKB3iEPTcfpXbMu6_mlN5E0vlLdjHMkOFtXnRLXw3_Vh_OgQXSL0oAMAg-jeaGSZIQslYkya28UBfwDj-6Nrf0YYrGFLPKLqQHoHyYCzBwLHhqq4FdaqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
نتایج دیدارهای آرژانتین و اسپانیا تاکنون،
۶ بار اسپانیا برنده شده و ۶ بار  آرژانتین
و ۲ بار هم مساوی شدند.
🔺
از اونجایی که تیم ایتالیا سااالهاست!
که دیگه توی جام جهانی نیست،
و از اونجایی که نیمی از مردم آرژانتین
ایتالیایی هستند، اغلب ایتالیایی‌ها
علاقمند به پیروزی تیم آرژانتین هستند.
🔺
آرژانتین ۳۰۰ سال، بخشی از اسپانیا بوده،
و زبانش هم‌ اسپانیایی است.
🔺
نام پایتختش (بوینس آیرس) اما از منطقه‌ای در ایتالیاست (جزیره ساردنیا)
🔺
گاه برای شوخی به آرژانتینی‌ها میگن : «ایتالیایی‌هایی هستند که اسپانیایی حرف میزنند»، فرهنگ غذایی، صحبت کردن به دست، تلفظ کلمات و آهنگ زبان و….. متاثر از ایتالیا است
🔺
پیش‌بینی برد اسپانیا ۵۸٪ و آرژانتین ۴۲٪  است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGEnFnkyTMfr3Ayi9pvLzCUAEo83lX8HVLQBUpoHvP26GhcRJZhNB3MtzafwvwQukxV1wQVhib5uKv5iYwG-u5NRWYmxXXO-S4JAQVrGsQkqq0va9AAiBA5vsimPTzdrcIhYchNMrcPOoUEYrA25IrIoU2eeBJduDgR54V7sWEtjMGB2XSoeQzSD3YbSzmWPdX1CSAuhUIHHdQ-bOQ9tkZKhLGuTWrmxtuw6z0_WakY696mwWwzD2-4KDNhTYOT1DiqoKlE8ijSnxTdcYySsL-vfaFi-z9rI7KQlK5UBEdfGYPF4IQZCe1xCiicnpB1h9NhcN0YaqsMc4Ghj2jkKOM2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGEnFnkyTMfr3Ayi9pvLzCUAEo83lX8HVLQBUpoHvP26GhcRJZhNB3MtzafwvwQukxV1wQVhib5uKv5iYwG-u5NRWYmxXXO-S4JAQVrGsQkqq0va9AAiBA5vsimPTzdrcIhYchNMrcPOoUEYrA25IrIoU2eeBJduDgR54V7sWEtjMGB2XSoeQzSD3YbSzmWPdX1CSAuhUIHHdQ-bOQ9tkZKhLGuTWrmxtuw6z0_WakY696mwWwzD2-4KDNhTYOT1DiqoKlE8ijSnxTdcYySsL-vfaFi-z9rI7KQlK5UBEdfGYPF4IQZCe1xCiicnpB1h9NhcN0YaqsMc4Ghj2jkKOM2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=FoeRE1zVnO_bU9lmq_Q2ditUWycSSc93X0iaGC_xsshpgApVSFfPjXqHzReJDS8Ql4q9uLm1e9c_pZbNrmUodKaomsWrVMLxdp1mjlceLtjcnSfT94VPMrvK09sc5gp68K9gD920ZpIsu_IBJrwx5z8WGmYugMJ_s19BNlVHOrMwRIylsGIsYnHp02VbJPYEFenX8OQsHKeRjXKLhygoArGobppQDYmhFRIgXU8RLKlDEL-n8zPRGdxAZ2OXzr6OU7bk1LSK71QHVYswp4wCHT87u_Fk0ZJR9D_Y-VYWeVxnHAUR5sbGA5CAdmju1AfUipZYvOgKgaQqSkJrkQsvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=FoeRE1zVnO_bU9lmq_Q2ditUWycSSc93X0iaGC_xsshpgApVSFfPjXqHzReJDS8Ql4q9uLm1e9c_pZbNrmUodKaomsWrVMLxdp1mjlceLtjcnSfT94VPMrvK09sc5gp68K9gD920ZpIsu_IBJrwx5z8WGmYugMJ_s19BNlVHOrMwRIylsGIsYnHp02VbJPYEFenX8OQsHKeRjXKLhygoArGobppQDYmhFRIgXU8RLKlDEL-n8zPRGdxAZ2OXzr6OU7bk1LSK71QHVYswp4wCHT87u_Fk0ZJR9D_Y-VYWeVxnHAUR5sbGA5CAdmju1AfUipZYvOgKgaQqSkJrkQsvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BaPjYeVSzGCf3DH1EzeiYxsGzZ46nkt2e_bt9pnmGrtNi11AvDvcsPrjlZXzwIwhcTBaz-FsVQVsQKTOt_cKV2obDPBg7n2xwq3FMOgPIJc-vm-CznEWIcNmD4xslnq15K7yAEGutRBx9YxGyYIjICfT0vF3d4yKRHgPIrniYAuEi6J_wpnDCajKN3pZPA_xGZSjO52mqoIGKxV_p2aK2bTvDtK-IBjUOeLkKx6GlPFRDNZ7zcA5OD5cPCworjFKbPkg7a5V28Zfsa80344QecnqZGxMt3ybHi8YtVv5d5iKrwXXU1x--2kP9-QYUzVfi6KJFa1qfTl7uxrRUpbdZKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BaPjYeVSzGCf3DH1EzeiYxsGzZ46nkt2e_bt9pnmGrtNi11AvDvcsPrjlZXzwIwhcTBaz-FsVQVsQKTOt_cKV2obDPBg7n2xwq3FMOgPIJc-vm-CznEWIcNmD4xslnq15K7yAEGutRBx9YxGyYIjICfT0vF3d4yKRHgPIrniYAuEi6J_wpnDCajKN3pZPA_xGZSjO52mqoIGKxV_p2aK2bTvDtK-IBjUOeLkKx6GlPFRDNZ7zcA5OD5cPCworjFKbPkg7a5V28Zfsa80344QecnqZGxMt3ybHi8YtVv5d5iKrwXXU1x--2kP9-QYUzVfi6KJFa1qfTl7uxrRUpbdZKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scigGElGeCIdWEisGNYrj4KWXNdk7vsfTVRY8WxC0DZjPCvh1B8KJ9wt0Y7YJsbA786CXjeumcb-2NHSUnhMVYo2y6ztUsuzDmp5_-J_DgeMzx9nJdIixphBuhywi8X5h8S7-tCmj0ty8d7NDiM6GkHQuTEQE13NBLbAFuo4U6UiAZPwYZ07S6F-Ba7OhGfmsK_A50wtlcge7vO3fdB5vgViweBOz8THTH5LsljDYYx_NGJA1fEl4hYvl8Z1swR1zvReSAEHkqxuEj0GQTvvckh4wjS5irygVklNG0F7xwhXVhcaorOa-RsLm1aoFUfcnIMr_Uy2lLbKM4LtfSzPnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LjIrdwGwe-afY6TgCGf6ko6mxv-aCGNCUF_KDWCSzGorhyFtojaE4edvEWudwSS7yMaT9Z-ebcFqTU1SkDe-QAAeFHrzCYTOyOHvJl63T7ukjURSNIVftf7uTkOvYOoLaTqAxxSoY-jAfXDt9JQGZHwTWGz0Tg8GjhYj6F4g6bJc7FUtu4uKSVIQxM3LhCGK3lzJlxEwkf2RurAF0CaP750T3T0bsPDcP5ZL5WIF-tD58UuLiFiDlJjTghFgccFOYKR-fW9YKY2UV9XXKpQgeTkbSdEjrniTQaX9jfjSSqiMR_l6TI2H9_vVYWIvnVkFjulo13Du1M6QEAD9dlSVKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huAodYXx9ddruXTg3FEBTRBVcCtl0R4dtogoKuhRIfyMEjhmxgwHbf7nTGLwhWelyMlB65pVCYTUl95LQvy1BuZ6TI9Ak6JU0e6ryZPdExFh4ZPSvNELfqL0iGFOmCZrNOcx6kPinETp0VXhb_-VhLBqr3t3CDFi050sj3idFBBEfIbhUFWcNJnv2kVJwro2BUhi7i-YrSbd1mYJsnPEjVBEjyk85nR9NcPxuzDHSf8VmwmphdkDUAyDfC9ku3Hxo2sku0U4G6fYSRdhskfWhrIsBRwHRvZFzpS__ddyPC7jKvafRN4yHAMvjtCR3fPtUodFwGFvdssjMwDwpAnOag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bQZU_jqwOvcai25xKxSbQpu_hWfxSIAJ9On6y0YjetX58Y0xvfaGizvw_-KUiSPQNZAFYWlKdnD97REE3kg9CuDSwtsRPy9UWr0Ru4t6Fu4yjLDxSbTxxLUaEyZWaSbAZcbwfOttQE2uQ_ZqpgwUo1LMnhojU_H9aw2Lq5M0DlFIEXF5Ig0uLwnB8KplbC_6u2rBG-oFCcG_WSLSXEjL2p1z_0T6WVJpz1PjD-2V9HNsDmq4i5xsz8PVJoeADWVdwq6XDzXP15T0pSfbSbpmPgLkqIT4Ak2E_xbo1wUh7wJgjEjBqnk9SZUPUGF16DpCmqSxHl-l908ZfmFdD9WmDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okDK367Gf3s9SGnmn2FqZmS4Ywsci0D__msGZAh9TjFizj-FvQ_vOiQyZ0mDpU8P9-khNrlzlaYw9HWQxIC-B0dN1m_9A4tb4EWNQlZGI9KNiuFgdn0c1W3Olhpa_C8x8bLKQBUqBjALj3kBqVpm21G0YZFlPxRf7wFwlcUhd7-DvSMwo4ltSPmDfKTNSP0jQQiFxr8hcnlCnY60VhwVXqqJvx3yoh9oo1YPcadq5jpBkxwGliAj6icsyjEDNe3Eb3aIBDDZj1cMuFzdBeKVYbXzv_cPa-qMjbgftT_sXzScZ78XaGQXbSCOX0ooKEPyEOpCJOlWoFwV7PSRcOtAvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd0VGcR3Wh_NTnG9Messy8qgASjXGWmMC8a_kEgvXGrzUm8hMvx1_-9ZtEA2-PRiw3D4uvrRvhX4HFaZ1OniRRpGH1FQChGwSCr1n-UOenOGEnT3aTjnQZxL9s1UqfxFyRcY0qDfsWA2sbJdh5mx67QEyUgL3rD-c5dB19tmf7IS2uQ2Z_MpLVKDuU8_oEPxHOSeqRx_cAFn1VS93jPU_0Wk3idtxCsIrr2svsrRHhE6xP-6QPZL-niFaHwMMSUBVnR7Wp0Tg7czImcFyydDMS8NL2lDevG-_Rb7G8TnqyybRsyM98YQCrs7S3wEoE9lwC72sjP3uRV77tdhDxfXsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czpReHbcvJ_57HpaBIEiWJ9eRu3qI4vVQw8IrwK1k7CbhNo8m64Yzj0V-19iulhLp4hk-z8Kt-WJYNnUpba98Ze0_oONQuempap4h6Ednqlk7962DjaLh6Ky1NUIMg-cckMYTyczDVIcAkm1LieWWiGVRaf2-Lssa12hyO4hlPt1PUVcF15a8VZDJ_1P_93VXMz2s1ARXXUk9ao6QR55QZdKQPftrcpdjZaBngskAo727RCIhvM3qxOf7QYo30iLGDdAnMj_eqvx6mZa1kfZVW2h9U-rMntkkq1vzHDC6GEjuE4RDoZPwpU_Y04SzMAg9yW6kzt4PjS6sDceyX9P6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qY7YSDCYNpy-Cwpx_TGMWKlYiiWAd3D7VvkrmayfL9cgA6JuiZBXNF_6Epv_Vke1eYTcM9kqmIMqN-K1sCI1J2Takddd7uk1Ly99MtV3qX_vJtb0StnHGZCrp5tcUCvIYO2nrIn3wjdBFe1wSLgGjhm19rXyQW_PmQS-5mfgmATehwLhUHOcOCNT_Oz2PZOYjDgs13ILkBELuV620zWOrIrVaVHVuAzWV19AEV2xIlzh4kgSJHRBAi-5Iw4ZIERqyf2XeQusXENf6a44iGHHhLIYonVCLg9lgcf9Hp6vyio3Gr5RxnFOfZZWC3FdJE_elCq0TWbfQIZhLJpVBXT9PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6lik7lPf9SErJoepAwHa-VwseUkdzOgvjmPHxw3k7tdPLyx8Jl35mh4n9kaH5Ubf7IjGLptXzquneyR73u5wjUqbVROXPXR0vkeNTbFkjEWlMHvzE42hprC3yWu6mGxLg-9Kojp6pldHCt-qixH_pXJOLwpw4cUYAp9laawraY-Lc-izTYnKXoMnIokZvB9rmdZYWBbEvlgQFjWc3VHE8sP_2rz44R220uFL1c3f03aur5sV2JYWb3h9avIMR583C1nXISVh3VdzWjiGeBzdlwl2JUrvEJt5CuzL4S6UNifa9yPaUpDt-_5EvS0glLe0-EKkD1MBEK402N3Q9E9iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استادیوم ۱۵ هزار نفری «بنت جبیل»
در جنوب لبنان که با هزینه ایران ساخته شد.
این همان ورزشگاهی است که
حسن نصرالله، رهبر گروه تروریستی حزب‌الله لبنان در آنجا در یک سخنرانی گفت «اسرائیل از خانه عنکبوت سست‌تر است.»
همان ورزشگاهی است که احمدی‌نژاد در سال ۲۰۱۰ در آنجا سخنرانی کرد و گفت : « تمام جهان باید بداند که صهیونیست‌ها از بین خواهند رفت.»
امروز نه خامنه‌ای وجود داره،
نه حسن نصرالله و نه استادیوم!
و احمدی‌نژاد هم متهم به همکاری با اسرائیل شده است.
در
تهران اما شعار می‌دهند که جنوب لبنان
الگو و اسوه‌ای است برای جنوب ایران
.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJaLQ0HJ04cQUQRgkxcgnxrEKE6kfeSGFPC_s04BOsoX64-B0a5xUH5l3cetiQklY9piS2QxtW0wc0Z4TmKvI4eYkZgga6f7RSEHX33aN3uYZ5zCHX7sw758ZKO8nNCfouM0k6RtB_k7rXaSfZsV_-vHBlnOyWI6MFdgTuPaU8Q-yWEH3cHNlx-_PWGbjgHRVl5H4GH17LlDM61IIojPXrhOQVUmIuKpBvMbA_II9uu9pkyuiKgTqJ-d91U4AtqXgS9L3hEci53IBHNRACwtTTU0ZWCews6QIq9kfzcLfcyZ1fTXKhGgHlxN_Rq_vPn3wgWQBgdx_ZzO2a_MeQrD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vu638km628KC0tpRNhruVUZ-VXVFoZyLSCue3TpSKbgxkVrt4bHm1PsskIqed3yMvrgkLSidU6ZjxTt7Dc5W6BMC_4IFieegPl_DyZCCmfZVfDRNOYsByX1-tzla_Wcb7WUEYdPtrPDkMa4Cpuwvp-gQwvAQ5cBn7Do4drG_M381flwveISyXC_8_PWIuq0_KN_n2Lgx8jI7m28pIzGshfA6u7SNEwtfcT8bH425LTaAIVyHzumkvvu9bgk5AbDfJL1fe5O-4b3M13vqGHg2H4doT91dhVI24mpSagII6UGJrxQukd6En_q7lX9TGNXT3EZ0Lx8vg3GT50RlhS-kLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVV84qhsTRNy4pnzWGTPOx--o-sEvQJfB16XKv7pOZ2tiZoJmXz0FqV2kMGshslEiI3CquG8y0znRScJKYQgz_3Uj9YXTl4tR6wlcSgeUJdwICf8sd0EBFmqUl37A8v23dsWU06s42UKPzntcunKdUvt3SbBaHvTOKSFnpYVzfi9vBc7s6bBe08U14SW9O3JAVpDMlZ5w4rMXCLb6cMvrt6-W7nafUI-Y5QAhLxP-CYOE_YsRwYuqEsaDi-7JxV2xf_h5mmL58s3RqL2VocLEQSeQV0C3ncmMEUEKolXHcGoKCnBm56B7dZQD4KyX_cq4H8HTd6SLVMHETbyNNRTFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p46jULFRT62vroNph3z0Z6zuM5Ts3hrIDeFKI9aGYPukppGZvHq-09rwOZTTt-FwuEDc1BDmDp6oELT7Xvp7IPLZ4-uNKydtJnGjhCkkPd-SKJTQxoNURyfruf4IHMFc-2h1qwnlUshozIH1rAnI9o80FLttYiCIPqfXSCVrF7mHrL8pe389kG9x05gFqWmTEXGtMwlOV_LwcfUQkBdS8ke1QnPTrU4rmL9-38jMWHyk90l--lHDdLZiLygxpGREPqsa1TySA2yVmG1zwL-cuk8KIEKntB4v7AC_A2iaRnhpNtadHw7KCeptWVdbOUgG5JI8pzIB7SAOIDKwJ91EY98" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=OtmY0SVqgmc32Zl5cu7V9RbqF4uOtVoO70lu5DIPJp6tnJuGK34TC3TQkL55oGpy9Yp-fY0Ihph9ZiTNwNuYfJSrt1YofYFE7PLHsY_BNm5LJRl7bZRmb42HvBIX5g4cDZD3kiAIb9oR5Nkva-DZK_bApm9dsSe-jpnbvlkBosvZbZYAf7Tw7R2lE_leOcS_QMgZpchYQb3p5LKItf-oelVe8bDmF0qJ67e5dUiX_8xE7z0dYHbfoIX3TeSJSaMCjqtxGnnh11DhpaFkfY2wL4ymoICoAbA-MZtewB9j7iLKhwh4DXVCkEU6j06JQb1CItSwjMKHC86EcXlOyWQ_p46jULFRT62vroNph3z0Z6zuM5Ts3hrIDeFKI9aGYPukppGZvHq-09rwOZTTt-FwuEDc1BDmDp6oELT7Xvp7IPLZ4-uNKydtJnGjhCkkPd-SKJTQxoNURyfruf4IHMFc-2h1qwnlUshozIH1rAnI9o80FLttYiCIPqfXSCVrF7mHrL8pe389kG9x05gFqWmTEXGtMwlOV_LwcfUQkBdS8ke1QnPTrU4rmL9-38jMWHyk90l--lHDdLZiLygxpGREPqsa1TySA2yVmG1zwL-cuk8KIEKntB4v7AC_A2iaRnhpNtadHw7KCeptWVdbOUgG5JI8pzIB7SAOIDKwJ91EY98" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=vmsrSUpNUXa6m0jjKkdSSLtNphexjxQLu6M2_WB3hlaTjE6c10M2cBrCfkYQCqGJlKkaVtfy-s8fMvBnjlK-t4AFj93JI0STE5hNsQNhVfmVmtYDcAcL9bkeG7Rbo7UiTuXoClhEmW54-Qe8KBFslWoUAJMh-fh0e8cSkX2GkVe1DHqlzKrWRfvRnWE7zTbkvbUDLQBarn6YNLNpUTvaTwoMER7QnDPqYzqWET3HgqZYM-c9nteK7aQsZb_J0-T4W1SSyt9VbE0Yx5UjhEexlmGHAvSahUsD3WlAg_WnMpzbumz5EJ9vhzu0Roaz95kOYGXCoWxcSwZsbCUNnz_0jzQszAWQljNdnHj-nRnAw-Sf6v_70Fv--qSAkCC2GO4lkQNA7K8FBIw9DXpXsNVcATIgcLPtp4ZcwF9Z9fkNY282icpFbUnz_VJvYzP27icBgI6no5--SVl04wLjzeFH252kZTZ6h6lybCCvv9f62ss8JSua8cAkVeF5ByyYcXOVm2u0XwrDuL0RsJlKBxQwTnYomsYMHNE5uQWFT-_upGcF5W_qob1CzpjYk8OenSVlPyRzo62tYO1Hmh3ltR8y5PfxXOzrn7nVols9Il4zhBbdvM3YnAWFxWGhfKWPFQZXIWZBYqo1RSXC1bOs3SxNSuOpX6apKkfoSX_moGCh1i8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=vmsrSUpNUXa6m0jjKkdSSLtNphexjxQLu6M2_WB3hlaTjE6c10M2cBrCfkYQCqGJlKkaVtfy-s8fMvBnjlK-t4AFj93JI0STE5hNsQNhVfmVmtYDcAcL9bkeG7Rbo7UiTuXoClhEmW54-Qe8KBFslWoUAJMh-fh0e8cSkX2GkVe1DHqlzKrWRfvRnWE7zTbkvbUDLQBarn6YNLNpUTvaTwoMER7QnDPqYzqWET3HgqZYM-c9nteK7aQsZb_J0-T4W1SSyt9VbE0Yx5UjhEexlmGHAvSahUsD3WlAg_WnMpzbumz5EJ9vhzu0Roaz95kOYGXCoWxcSwZsbCUNnz_0jzQszAWQljNdnHj-nRnAw-Sf6v_70Fv--qSAkCC2GO4lkQNA7K8FBIw9DXpXsNVcATIgcLPtp4ZcwF9Z9fkNY282icpFbUnz_VJvYzP27icBgI6no5--SVl04wLjzeFH252kZTZ6h6lybCCvv9f62ss8JSua8cAkVeF5ByyYcXOVm2u0XwrDuL0RsJlKBxQwTnYomsYMHNE5uQWFT-_upGcF5W_qob1CzpjYk8OenSVlPyRzo62tYO1Hmh3ltR8y5PfxXOzrn7nVols9Il4zhBbdvM3YnAWFxWGhfKWPFQZXIWZBYqo1RSXC1bOs3SxNSuOpX6apKkfoSX_moGCh1i8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxqIJWBx2vkLqoxsdbf7al5TcrMrDUF1KWiNhL52QoaQpaiijQzQDXbIKKnM_95VkCWOSPDJI-s1nxb3khhIrKTVzr-y2uag4gsKkvMGtex_4yoEsVkA5RSoPXiJQu6WUQJjyKYXg2GP38W-BR4VXwSwfU_keI73gpNjajov99ER0zieHpNFkFCwehvG0Lk84nE3VmBgXyVkBVyPaJ_XRbNQhH6As_9tAAltnA0HFazE9i-u7GXXZ02eE66YDmzDbZV1obS_OeU2sAUPsWwQ93ssqKmGI6WF8DVN0qDEPP9mVOifnIoMiAb7wGkRILfEF_aSKSlSAUC4uR6fx9n6wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=ujOMz0h4OHOBwWeNpG4AZa_bdzguGSMgSkw7W-Ad6OHM-AoTXa4djzjfNBGxnkl-r-Pnnsp6Pm1NR8kXlEJxby11zuQ8RiOkK0R2Y-LqPEymf7u4Z-uO_EfpbRZ02FXkqLPJcE2B_bsfur8IScDPy15zkj_sb_n84kemJeIsl8GDkK4cxNETqj7TUFNDEB4PDQtUAbDuLJSTwgygkjpY0wswGmIjOQTFhYbzuBJxbLlbp59VV2J5LHfzh4VkPVF0T-Ml0P8Z0tiuaze3bUJIfmNCX0NH5wRkp5eyUGDKZSxfo54tgmkD3vxtWMqqUkKfgpVchame4Do33NuMx2PnNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=ujOMz0h4OHOBwWeNpG4AZa_bdzguGSMgSkw7W-Ad6OHM-AoTXa4djzjfNBGxnkl-r-Pnnsp6Pm1NR8kXlEJxby11zuQ8RiOkK0R2Y-LqPEymf7u4Z-uO_EfpbRZ02FXkqLPJcE2B_bsfur8IScDPy15zkj_sb_n84kemJeIsl8GDkK4cxNETqj7TUFNDEB4PDQtUAbDuLJSTwgygkjpY0wswGmIjOQTFhYbzuBJxbLlbp59VV2J5LHfzh4VkPVF0T-Ml0P8Z0tiuaze3bUJIfmNCX0NH5wRkp5eyUGDKZSxfo54tgmkD3vxtWMqqUkKfgpVchame4Do33NuMx2PnNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=QfAKi9RGpKWwHjwN4guH-2L6YLVZFQWaAilr6XfGDw1XTr1wjRLNH7Vc3uFIVia--H7wXmd8S66MESfMilOghDA2DhlNvpP7NXXTdO7qUEEcfufTIAZaPHFW6rAdbBHqv_-8rmmc8Ur6gYsHTzl-DXIiqbSeRlRVJxgRnFMNqBhXdA1nkY-h1eIBti2kTDlIktkP58nZdPa9Po_4CGqYoxBc8_Jb0b-Wvcq3-4RwZCECQxGIDFMB9X72wWicMuOzObK-iedBT2i0vCHueXGLeuqWLDPTywydqubyS5JWFtPrT_HmvroyFW6mm5EstLCIyPKVE04Xsv6izqrGdxatYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=QfAKi9RGpKWwHjwN4guH-2L6YLVZFQWaAilr6XfGDw1XTr1wjRLNH7Vc3uFIVia--H7wXmd8S66MESfMilOghDA2DhlNvpP7NXXTdO7qUEEcfufTIAZaPHFW6rAdbBHqv_-8rmmc8Ur6gYsHTzl-DXIiqbSeRlRVJxgRnFMNqBhXdA1nkY-h1eIBti2kTDlIktkP58nZdPa9Po_4CGqYoxBc8_Jb0b-Wvcq3-4RwZCECQxGIDFMB9X72wWicMuOzObK-iedBT2i0vCHueXGLeuqWLDPTywydqubyS5JWFtPrT_HmvroyFW6mm5EstLCIyPKVE04Xsv6izqrGdxatYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJkSycsV4TvH3CKvkq7On0cwic5WP33XqirOtWl-RJe2Tx8n-cpKmmacLmOioEgiYGsycCEXq4z0owGBrvLrNAF-pA2jPs_39-sT5mbJkOCEX6-_gUM9txuoRIHvGPf0RGsDdqI-pr65VJUlLqa7SIuBymCHZI1qIzlezmZWMwZvYix4XizvmRfcgukcaIOIrmOLcTWE2nfxouMnC2jzoagL5Xr1mY8JMukUOfBqMIWUSNE1m9FMkvrMQbmahOqBePq1pBvIyUEoyLNtU0q4hP8kQ3WzDYUJCCcQaf9Jn2--c4nZtCStU5rBbKtJAwkvGAAPd2MNbJ9vYBL7Ono05A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pcMfPBh_CPigIcb63_wfVmcN6hC8xFBJW-Yb30p1RRZbIOCPpXaNBulSXAu6pdRDlOrGfrJ_Sg9omuA13d31h5FaN1IhYYgXSa3xzS-PQj395UINPinsHHmGNxhp0JAlCG4thoRbAy383OkUgCbssHUj3ozECcaUOvPZhsz-21YSuLVSHfFebWfSPSU95YJTqYO_EnxzO3ed3AilDn3nWodhVX1alv1wvrYdUH1xJfzKDTaKJqco19M_C1adfddkzgzlL0OvFiWLjMVqW1GkiX3C4ZA6p5irdDtaYjb63uL-_nEpZFVrzwX80yNbZ4O5MaeuP3livNYVAWz9LKWlJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!
این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.
🔺
ارتش آمریکا همچنین دیشب به چند پل دیگر در شمال بندرعباس حمله کرد تا ارتباط زمینی بندرعباس با بقیه مناطق کشور دچار اختلال شدید بشه.
🔺
بین ۸۵ تا ۹۰٪ واردات کانتینری کشور از بندرعباس (بندر رجایی) صورت میگیره. ماشین‌آلات، قطعات خوردو، تجهیزات الکترونیکی (لپ تاپ، گوشی و…) مواد شیمیایی، مواد و تجهیزات بیمارستانی و… همه از این بندر وارد ایران میشه.
🚨
کالاهایی چون گندم و روغن، برنج ، ذرت و…عمدتا از بندر خمینی (شاهپور) وارد می‌شوند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=POrqIBJpFGBCzFcUj01xZWgcmsrNLZIK02WduvaeWrIgfZ_fHElCr4HHriekfYhJZXf_EYIY1L1yqlCh-2eHpTiVWj_8Br4AAKeLhM5157kMoBBIx4uhA99Mh1u1V7pTkyVHWwf9XDGkQMe3PulZmL_yL9JWb3uTLaYqjsluVGFpwyERJmhvSEgQFPrd2J6WFd7SFScgQ40dSZcObeyVX_9OKm-A-nLHRqPZMgjC9naQ1IT23rZTDVp010XtL6EMJa2dUeMIqM6vKo201UNgGhS7v3yMInKOZ1rPyMSIPzXb495msmH0lLmvA8hhXcuNsX1s--FPpDPydeiycayuTB9g_z0jK9qE447uv6tAlfax2-3iwdir6n6ZatCzxcEW4YvTXfBlB0pjXgIAMaCWJa_uXKcVIjHlhzO6tJPnNqsfBRtaF2hAL9uqemdrwfVCXHmM58ZAAVcuvr1nDTc6sR9eKwJBJrlKR3ATDkcN5HFk0MmIaIKjP-RQ51BGGwd05LmkZiQyugWXeb6CglH8F8IfNL7Uohibw71bQEyYkSNF_1W83eo39RonnVRwi4gmAQUs7KHIKNm5toCAQ2T-BjsNLwVZI-zwGpbBdd8mfLLhgtMEJohmxVPO_-iwvSoc7XCJDJVphyA0xKceqVGkVH9MIA_t3rRHZs3iZictvHo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=POrqIBJpFGBCzFcUj01xZWgcmsrNLZIK02WduvaeWrIgfZ_fHElCr4HHriekfYhJZXf_EYIY1L1yqlCh-2eHpTiVWj_8Br4AAKeLhM5157kMoBBIx4uhA99Mh1u1V7pTkyVHWwf9XDGkQMe3PulZmL_yL9JWb3uTLaYqjsluVGFpwyERJmhvSEgQFPrd2J6WFd7SFScgQ40dSZcObeyVX_9OKm-A-nLHRqPZMgjC9naQ1IT23rZTDVp010XtL6EMJa2dUeMIqM6vKo201UNgGhS7v3yMInKOZ1rPyMSIPzXb495msmH0lLmvA8hhXcuNsX1s--FPpDPydeiycayuTB9g_z0jK9qE447uv6tAlfax2-3iwdir6n6ZatCzxcEW4YvTXfBlB0pjXgIAMaCWJa_uXKcVIjHlhzO6tJPnNqsfBRtaF2hAL9uqemdrwfVCXHmM58ZAAVcuvr1nDTc6sR9eKwJBJrlKR3ATDkcN5HFk0MmIaIKjP-RQ51BGGwd05LmkZiQyugWXeb6CglH8F8IfNL7Uohibw71bQEyYkSNF_1W83eo39RonnVRwi4gmAQUs7KHIKNm5toCAQ2T-BjsNLwVZI-zwGpbBdd8mfLLhgtMEJohmxVPO_-iwvSoc7XCJDJVphyA0xKceqVGkVH9MIA_t3rRHZs3iZictvHo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=GSOttnt727a3Xep1Hic-1AM8TpoS6Lvi1zuvWaxvr5Hm0BzfcI8asH22lpRjX909XdRks-azy7mGD2gXNVCb1W8PZAy7YWMb3iKlrNLJ5OtQ5vWljWxRUzjjY7v_CDBi38p_dDqgwloTNFABzjozgeFicUzbeLSudqJIjX05OpSC0cM4bK9MdWVuN19OqzO51nltgnew8x2aWqiI-MlbUBiQwcPGVm2rMGtQaEEcG42R3HaUxiGpxKTkAefk8zvfNx9Ho3K3Ac6papGdsU0N3_Q0MZp0rZllv0FHIQpeuFqW4Wpc4InKofmmDqhAGkhpMfK2cpytjD9NegIqjm9EjYIfMewrrfPmmTpr3hJ2hVHC5_c31vtFOCRdCuNsUFQDWo3glxWBmH5qbGO-KCjjNzIOQMXgyDnoEMtrVrIcDEUJPgHsHUWLTeJupVmud_vIv4ITh2k9vOJHKEmjnKa1smP19aWCHR7tChh1OgAw0jqAFgwPYzylfV9tl48k4Ex0IyCTSynx9zE4JprFsQm_JOIiSUE5sQAFK5a78a81cOdOU2vE7l18xrFRHxXXS_DktridHfs3nGTMPvDhDyMmO5RWML2xmDhqRvvKkn2mNzhwFkdf23z-o93xhX5-LfMpc-p-8lN4lJJcZ0NDrXbLlMjxAhkFp0a5ZTCW01wAjA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=GSOttnt727a3Xep1Hic-1AM8TpoS6Lvi1zuvWaxvr5Hm0BzfcI8asH22lpRjX909XdRks-azy7mGD2gXNVCb1W8PZAy7YWMb3iKlrNLJ5OtQ5vWljWxRUzjjY7v_CDBi38p_dDqgwloTNFABzjozgeFicUzbeLSudqJIjX05OpSC0cM4bK9MdWVuN19OqzO51nltgnew8x2aWqiI-MlbUBiQwcPGVm2rMGtQaEEcG42R3HaUxiGpxKTkAefk8zvfNx9Ho3K3Ac6papGdsU0N3_Q0MZp0rZllv0FHIQpeuFqW4Wpc4InKofmmDqhAGkhpMfK2cpytjD9NegIqjm9EjYIfMewrrfPmmTpr3hJ2hVHC5_c31vtFOCRdCuNsUFQDWo3glxWBmH5qbGO-KCjjNzIOQMXgyDnoEMtrVrIcDEUJPgHsHUWLTeJupVmud_vIv4ITh2k9vOJHKEmjnKa1smP19aWCHR7tChh1OgAw0jqAFgwPYzylfV9tl48k4Ex0IyCTSynx9zE4JprFsQm_JOIiSUE5sQAFK5a78a81cOdOU2vE7l18xrFRHxXXS_DktridHfs3nGTMPvDhDyMmO5RWML2xmDhqRvvKkn2mNzhwFkdf23z-o93xhX5-LfMpc-p-8lN4lJJcZ0NDrXbLlMjxAhkFp0a5ZTCW01wAjA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا قبل از جمهوری اسلامی
ایران همین جغرافیا رو داشت، همین تمدن همین مردم و همین نسبت جمعیتی،
اسرائیل باهاش دوست بود و آمریکا پیشرفته ترین  سلاح‌ها و تکنولوژی
رو بهش میداد و اسرائیل برای کشاورزی
و آبیاری به ایران کمک می‌کرد.
شما اومدید شعار محو دادید و پول و سلاح ریختید توی لبنان و فلسطین و…….
🔺
همون روز ۲۲ بهمن به دفتر اسرائیل در تهران حمله کردید !
🔺
اردیبهشت ۵۸ رابطه با مصر رو به خاطر فلسطین قطع کردید!
🔺
دو ماه بعدش روز قدس رو راه انداختید!
اینها کم آوردن ، میخوان مردم رو فریب بدن و بگن «مسئله ایرانه و تاریخ و تمدنشه»!
نه خیر! مشکل جمهوری اسلامیه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=JzMbiOdij1xDF6oIYfJJvMF59dszJUF0w-NnTaS9quO6tfSuNhcRowVQYCRsCq8KlNwf8ScQAXlWGk4x03XWOBw8-geN83_Oj0JgXKKipMxWaYrAkP_mQKQkGlPxDHR2PUvHgyR2Sl0wJEHI4wItrvegAYxGqqO8QK3VJBiMA6lHTjuBPozuoKV1TFhEKxMNxS1heOFvQHDB-oxKq4f8mzeGfQNkH-VFUe31ruZ3by09nCr9VQtx2p9uuciL7buBmvXvIGbSELQcF4mHUV63Q-TfQxixQ8glr5i5747VYHQ7hvUOuJ8a1P5S2YUr_-v5r97zLPWuNT2uQqdWNZf8hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=JzMbiOdij1xDF6oIYfJJvMF59dszJUF0w-NnTaS9quO6tfSuNhcRowVQYCRsCq8KlNwf8ScQAXlWGk4x03XWOBw8-geN83_Oj0JgXKKipMxWaYrAkP_mQKQkGlPxDHR2PUvHgyR2Sl0wJEHI4wItrvegAYxGqqO8QK3VJBiMA6lHTjuBPozuoKV1TFhEKxMNxS1heOFvQHDB-oxKq4f8mzeGfQNkH-VFUe31ruZ3by09nCr9VQtx2p9uuciL7buBmvXvIGbSELQcF4mHUV63Q-TfQxixQ8glr5i5747VYHQ7hvUOuJ8a1P5S2YUr_-v5r97zLPWuNT2uQqdWNZf8hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvTf8_nAYLIxP-02c_a3KRHQoW4oQ_16NOXzE317UwfC9aOzzefcyieYWLR-8JwaRsechUfOp23txNl-_VD29-scIPaaqCxv0LsCiDTGhescKoT7vHTNWy9WCgag28meAd6V_3vUj4IhANmQHTlo-1pIFHnXbhWELWkkDjRef9qZi5-8U210P4mnImz6n-RP_HUe5FbW7O7Rj67DEYukEwk4QaNJUFbpR24PE7sEo56UNd-TexfIJqzQuu-brrovKZupnOb0wxX-vuWw-6zGsc6MyXl2iZrh36PCnVPqJDToL2AXp48XGipMrKslupxWLtMeeq1XVEvLpYPj_cWNxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=feMJ64EioGCkR1VkY104DFggtQJ0Uca1BZE7DXRq8Y8ywwqiBTSbmO_4GJ6JZrlX4WtxFOue9Gfg3bXx2ZYfIYjmp1jPqEyGBF4zKyKekyyq5EMGAd9gLy5IKvuM5JsuNOPTVY23fvM8wIb1Ri8f4NlVI5m6KZHILgSZTHbiOW_-Zx_FySlLPq0arvGue3FpzFJsOM_B2asyHEizCezbARBJXeoEgVXr-icFRQZtdyA2Q-mVbxGgbj7HxSNREUqfzxUreE35czmjm00Svq_xiMeNucVSR79nN8fqZ3mWhk6u2yCRgpZpzYWRX8TkGHoJ8PZNw5pwHCaBWpleHpuqB1XMKpWWFdsyv-TFRKwn3DqUMPNOZO3gufgPnPexAP0mrcYgk4u61RQTJ54nHRLg5O-bgsaU2zhLnU3T9lV4OLz-w0TfmK_K0AmKL8v7V6cCSXlzQbKFXtM4z3iM-4j-R2ddPqo9jrXnfPTLOcLn30K1ZpGrKOXEQFP-bwZgbgl1-CLJJSiv5wEdLFiomtJw1md2krQVZJjtJHj-aSC5v_Ax8wmiMSx0qpa2yBwo9cOAhsmzsC2DsTxbLQYQXmY2O6YtN8rNRMKkt3kRiSmdIr70v4RAIfGNCrEnt1OtDMLDNqiBARqfbWmZa5b1HU2AxZLYA27nQakDo3fQz-9foKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=feMJ64EioGCkR1VkY104DFggtQJ0Uca1BZE7DXRq8Y8ywwqiBTSbmO_4GJ6JZrlX4WtxFOue9Gfg3bXx2ZYfIYjmp1jPqEyGBF4zKyKekyyq5EMGAd9gLy5IKvuM5JsuNOPTVY23fvM8wIb1Ri8f4NlVI5m6KZHILgSZTHbiOW_-Zx_FySlLPq0arvGue3FpzFJsOM_B2asyHEizCezbARBJXeoEgVXr-icFRQZtdyA2Q-mVbxGgbj7HxSNREUqfzxUreE35czmjm00Svq_xiMeNucVSR79nN8fqZ3mWhk6u2yCRgpZpzYWRX8TkGHoJ8PZNw5pwHCaBWpleHpuqB1XMKpWWFdsyv-TFRKwn3DqUMPNOZO3gufgPnPexAP0mrcYgk4u61RQTJ54nHRLg5O-bgsaU2zhLnU3T9lV4OLz-w0TfmK_K0AmKL8v7V6cCSXlzQbKFXtM4z3iM-4j-R2ddPqo9jrXnfPTLOcLn30K1ZpGrKOXEQFP-bwZgbgl1-CLJJSiv5wEdLFiomtJw1md2krQVZJjtJHj-aSC5v_Ax8wmiMSx0qpa2yBwo9cOAhsmzsC2DsTxbLQYQXmY2O6YtN8rNRMKkt3kRiSmdIr70v4RAIfGNCrEnt1OtDMLDNqiBARqfbWmZa5b1HU2AxZLYA27nQakDo3fQz-9foKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Zy6IQ_zX0fKkVn2UqK2ZElNobJdB6EGEbeTfq9hmM-CURrG0bSYRuaseyGIbd3jrpzuN-gOMPq8salyvw9FeOnbUUxFKxjzeQ8RjEsqaIsI-OinRX3wFVIQ3rYf7j4Skr-GCKgIrH0Nqo3hPbOWSd2987yskWMMXjoHxaOmPdJWGO29USSvpQAKCqSwC_dzxmQwSIWxC-ZNT8iiDv1Y31e0xmKxMGylTCT1eEBTZynUpfLpgCOV8qJZtD_s5irxcfQn8E7SBaLgNIO1-pEqvMZ2mYGtwLkLjXN1EtgZpI0X-WhmYIMUY0K0itn-sqBrNDykv5f9B2dfDAQQ6lYyVRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=Zy6IQ_zX0fKkVn2UqK2ZElNobJdB6EGEbeTfq9hmM-CURrG0bSYRuaseyGIbd3jrpzuN-gOMPq8salyvw9FeOnbUUxFKxjzeQ8RjEsqaIsI-OinRX3wFVIQ3rYf7j4Skr-GCKgIrH0Nqo3hPbOWSd2987yskWMMXjoHxaOmPdJWGO29USSvpQAKCqSwC_dzxmQwSIWxC-ZNT8iiDv1Y31e0xmKxMGylTCT1eEBTZynUpfLpgCOV8qJZtD_s5irxcfQn8E7SBaLgNIO1-pEqvMZ2mYGtwLkLjXN1EtgZpI0X-WhmYIMUY0K0itn-sqBrNDykv5f9B2dfDAQQ6lYyVRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2HkCZsmfv03Pip7epkvghrPlVBbIl2NfzQF3qu6YVQQs0wrMSEl_bqL0KFPX6SobR3NGv-5KmJpO2pP6_Tkpmq49Ruw-bx70er3KaG8eAb02wzKdL9FtgWt5gzcNwueIraj9-ZzDASmN61XItQYxI4iLs7kTrbZTylSzg5VgyHmT1TnU9kAxwzVs21T1eqE9Ry-RCba176ylT2gzRPV12NRDb4Gx7E8QdcPvvBNECtR0N4UqUXRRXKcE3Q7OiTk1-_R6KDpyQmDKHFpUGer1Po-WHziO-Z_ZkGeBabI_50PTzCs4YPeUBn5TeAZih4vanR5Z5N5OKNQXWvvuL6cWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oq8XZ8lGW51p6Wqqc8Xp8FXR96G22d80-dGS1l0j7yMYaaJwD4oH7uP0F0E7qRRhxbi9lv9ni3mvAm58GrDCZKxPoH7_aGAQO9HSYSfoWPZSTwcztBxKBXIBsQl3qPzp3i_0nUU5ejAvYb2Ij4J2nh7CHbdFnCT-6TOxb_hyxkfBYciJfVItqj8Di0v39Xo0qf5xVjsvFF6_j_ZOrJsWi64C0aojUAUJf-dWTknV-ImQkeY1d5T-JZfd67roFiE753ut0wkTtfKnMFMoWFW6_C6xYsdlC-1F2X0rhac2LTWfr7KfgIGSmQ1VOuArTvhTu2VlbKTD65uJ9IOxml-hzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JlkKletnm6W9O5_Vf_yajjFWBoDz-73l1izh1UEKrLskDbS8-HKQp6BAosV_-z57t4OmaIxCGNsQrS-jLyGCXs2h6ycjqnD-yE4qaR1jShxJ03UzWB0Rk3WSdI9cp_l4J8Lzp0Q_ret6urSIFHH-AhZwpsx9pq0izXznZJyAA_ILiLhKjPddQlk34S-oe16MIn97BF3w46iCAryQI0g-FqIjIQykqHuK_vNMuCbCTKbzU23WZYihWzGtY4mRifyzwrNzULHYTUzze3MgTp8BGSlbtaDcTyWftb6vlhGOYobTGtigjIJlyGBzisxjYxeFuFVYf-f6CoJogOEfzhjXCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JgRQqKEkViyM3DKhSFWKpUjN0k0dA59hiAWrrNX5OeAtmFMxb8qHbiXSclGL3-4OylxN7oE712GmswcDfpQG4MXkPOrRupniYZ12r41ulIP9EtMIQK19x6Fp2fvtsjkdyTYygQ2EbP7AwL1KmEyPCXXzIeuWS5FeV3QjNb1ipX8THKQOAzg_ZTNkp7QkH7mmqomMeByv7GqBX1mVrMw0VfKnDRe2BvWIfCl3Vet_I6msF239UZRK4qsbGtOuLLglLMGEC7AWKMCsGotHvSGso_VJujScwy2tt4qtxoXgSNIQ-I2jLfElDxGahd7-Z_x80tAsGwgK7I-T-inp0x72Ugo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JgRQqKEkViyM3DKhSFWKpUjN0k0dA59hiAWrrNX5OeAtmFMxb8qHbiXSclGL3-4OylxN7oE712GmswcDfpQG4MXkPOrRupniYZ12r41ulIP9EtMIQK19x6Fp2fvtsjkdyTYygQ2EbP7AwL1KmEyPCXXzIeuWS5FeV3QjNb1ipX8THKQOAzg_ZTNkp7QkH7mmqomMeByv7GqBX1mVrMw0VfKnDRe2BvWIfCl3Vet_I6msF239UZRK4qsbGtOuLLglLMGEC7AWKMCsGotHvSGso_VJujScwy2tt4qtxoXgSNIQ-I2jLfElDxGahd7-Z_x80tAsGwgK7I-T-inp0x72Ugo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3wSTaXiTFHTP9dbc_bSpC-m5wDuPMIHfClt2QnkN0SV9xqxtuXxA_gwiPYYcsGeMBuyazreoILfp_TM-HaSPd6UZ2NmXF1MquLRlVA4hN53CZAD12EiBYNIQJo6hUw9F7NwQ1uuqwXWw7RvFot7MXd4yfR5TDisRiBVWiNaU__A9OKR7IvJHV7aOJA_OwKVSODjlLWOwgTxnsozQxd5jWlE3XIBwGEQB57zKMag6edXnbfeDbO0FuM_q0Z8Ot-JFpfJx05Z6Lfp3SbRmugLTGtz74RCifCDTeLHnPfmbAmcYTWFP4I4Q6ijPJV7ggIQYWFiCIfox1UfdctbUg1Kpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=QeQEiK988gywLcGgVoZXa6dWHhoKcfOpkH6aL0M0zfJQSK_rpahX8iH3BMngyXqSJK2p5DB503z5rKHhF1tMxVnEbeD-7A_ydJnRQ6pYATVImT0LyHwWF6VK2GOSGJ-lBkWdHRxmmCn6M5sww89pFuSP0RmWG2-uA6bCdPEoLASUZpzkL-TSkPBzMAx8lwAL5TLXMfj9g7HbcvDCpa7Edx8cOBT4gaiZ_7aEiXetWRVKhLuX6KcbtlQE2ibflz6hLJCIDGH_BNxtia1ChLh909T6EGYYzJ3kI13P8Q8EdzSSfA3LM5FDuz3lQQTXrA_UbLGb_VwlA8FubqDp_ZRy_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=QeQEiK988gywLcGgVoZXa6dWHhoKcfOpkH6aL0M0zfJQSK_rpahX8iH3BMngyXqSJK2p5DB503z5rKHhF1tMxVnEbeD-7A_ydJnRQ6pYATVImT0LyHwWF6VK2GOSGJ-lBkWdHRxmmCn6M5sww89pFuSP0RmWG2-uA6bCdPEoLASUZpzkL-TSkPBzMAx8lwAL5TLXMfj9g7HbcvDCpa7Edx8cOBT4gaiZ_7aEiXetWRVKhLuX6KcbtlQE2ibflz6hLJCIDGH_BNxtia1ChLh909T6EGYYzJ3kI13P8Q8EdzSSfA3LM5FDuz3lQQTXrA_UbLGb_VwlA8FubqDp_ZRy_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=UiH8usodFumHXPEVDf253QPpLvg6hLhfIoaTCFqvq2B0iH75E0qY-EvQ8Rp7a_4YO3i3rovLQZtZTekCpWkU_d7xx6try7ZYkgTe6-pTPF9BEOXkphtfBWy1DGNLOfDlUocLtbeNq9FwjmFrkb5TOyfiJQEkTLToCRZzqmGfRL_6XuKoC1rNurtov2vXUsW66LcMl0MKK1ICo5wnTlfhvbsl3tMk8XVlVBpGQcAOOGmAjLcFTqf8TD1h57BajQ0nMOkFdtpysoWcU5lMP8ElM5dA8b7CETmbBEYxBZEas18nFFbN0jF2yqgFWMo6JBxzjCajlUBXaixK3WmxuA0byb6-_QK7PvM_AIrjk2M8PyM2Zg0lNH8r51qYnEm7dR9Nb6HwSSBMVbm4hz7ZSuQtXopDO_NYDxfhHMwEDmxhkBR30nLR6CyJvQIvfXZ9vTnuYApYtaevM0RxTfSDv-cuJG2A7GUsCHFa0lI2UWW2jYYbUymNdhQKtYi-MQ7Dqypjh_w_l0Dtys77yNyPAjpiq3xhkceJmRN_QEYqRAsfDH-EJMtwKJsEPXBZECiH1IlpO1RsN5NJRosymWTd1AvxhhVQNJcqDfi-ohFP-GLXrEWl08ZsCJIGY6y0EbS0YSp6KYLirrwll-iTslkuB7G8MurNuGy79wbDb2GnYkj1Ft0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=UiH8usodFumHXPEVDf253QPpLvg6hLhfIoaTCFqvq2B0iH75E0qY-EvQ8Rp7a_4YO3i3rovLQZtZTekCpWkU_d7xx6try7ZYkgTe6-pTPF9BEOXkphtfBWy1DGNLOfDlUocLtbeNq9FwjmFrkb5TOyfiJQEkTLToCRZzqmGfRL_6XuKoC1rNurtov2vXUsW66LcMl0MKK1ICo5wnTlfhvbsl3tMk8XVlVBpGQcAOOGmAjLcFTqf8TD1h57BajQ0nMOkFdtpysoWcU5lMP8ElM5dA8b7CETmbBEYxBZEas18nFFbN0jF2yqgFWMo6JBxzjCajlUBXaixK3WmxuA0byb6-_QK7PvM_AIrjk2M8PyM2Zg0lNH8r51qYnEm7dR9Nb6HwSSBMVbm4hz7ZSuQtXopDO_NYDxfhHMwEDmxhkBR30nLR6CyJvQIvfXZ9vTnuYApYtaevM0RxTfSDv-cuJG2A7GUsCHFa0lI2UWW2jYYbUymNdhQKtYi-MQ7Dqypjh_w_l0Dtys77yNyPAjpiq3xhkceJmRN_QEYqRAsfDH-EJMtwKJsEPXBZECiH1IlpO1RsN5NJRosymWTd1AvxhhVQNJcqDfi-ohFP-GLXrEWl08ZsCJIGY6y0EbS0YSp6KYLirrwll-iTslkuB7G8MurNuGy79wbDb2GnYkj1Ft0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!
ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟
به خاطرش حتی موشک به اسرائیل نزدید؟
(که اونهم اومد در پاسخ ماهشهر رو زد؟)
خب جنگیدید و شکست خوردید!!!
هم در لبنان،
هم ‌در سوریه هم در غزه به مردم گوش ندادید
جنگیدید و شکست خوردید!
۲- اتفاقا چون رفتید توی لبنان و غزه و…… دنبال کشیدن «دیوارهای آتشین» علیه اسرائیل و نابودی اسرائیل بودید، و افتخار میکردید که  بهشون
موشک میدید، از طرف دیگه دنبال اتم
و هسته‌ای بودید، اومدن و ایران رو زدن!
هم اونجا شکست خوردید و شهرهاشون نابود شدند
هم ایران داره نابود میشه!
نتیجه ۴۷ سال اسرائیل و آمریکا ستیزی شما!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6182" target="_blank">📅 14:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6181">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=fDbE-mYwQo5MNmrG_ByOl65_i3T1yVkGXUQSF8n37KOJ4HEMWIgIf8AuHPNyqhBxrDn0ma-u2_khPdMmGhXZB5Pa9dfomfdhR76wzIbiESbRsiNbs4M4gdHV-qhXO9BwZ0_Vn67-hFtqQ50nxl0KAa1N9g9kSFxTbuEUGML1L-Obrumhtyb_tGX8AZlWIMwaYeYFxiRJkB9ZqrxP6YrvuQiKGXUNBxlaxUTdEe9ImXeczgmw4UhJ9GT5kS29UsnBBKgAZq5IeC6mq4tdYhXjnYBwwi9GPbtu7uXxGGeeqNo7KHvs769fPVZlXuft7AHF8DrmpFGjGksgw9UXZfy4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=fDbE-mYwQo5MNmrG_ByOl65_i3T1yVkGXUQSF8n37KOJ4HEMWIgIf8AuHPNyqhBxrDn0ma-u2_khPdMmGhXZB5Pa9dfomfdhR76wzIbiESbRsiNbs4M4gdHV-qhXO9BwZ0_Vn67-hFtqQ50nxl0KAa1N9g9kSFxTbuEUGML1L-Obrumhtyb_tGX8AZlWIMwaYeYFxiRJkB9ZqrxP6YrvuQiKGXUNBxlaxUTdEe9ImXeczgmw4UhJ9GT5kS29UsnBBKgAZq5IeC6mq4tdYhXjnYBwwi9GPbtu7uXxGGeeqNo7KHvs769fPVZlXuft7AHF8DrmpFGjGksgw9UXZfy4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حکومت وراثتی بود
یکی می‌مرد یکی رو به جای خودش
معین می‌کرد
مردم هیچ نقشی نداشتن!
میخواستن، نمیخواستن باید قبول میکردن.
🔺
خودش چطور رهبر شد؟
با نقل یک جمله شفاهی از خمینی!
گفتیم بعد از شما چه کنیم؟
گفت : همین آقای خامنه‌ای»
🔺
حکومت وراثتی بود : مثل پسرش مجتبا!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/doRNNMI94ii4nHeXo3sGzz1o7dQCNmjmvydthXYVqojVA9dWz2y0XjbE4DByOhGf8Pgrujq1zMsQORI8Hg4WKb6yCD9AGTDEy2mOZ1jU7Rw9R_p6D6xogXY1Dc7n-z5ASlBueytrNEaF2bMOUZMQ2NOrOecjLUST9QAfraVXCGEteDF9_bGoHZf4bjdo0NqfhbJcFJv5mBRRIysGMyowmiN_D3oMc14OSEJbib5UIamdgkqn5eNOAR9JaDj-vKStTLdRx7BDzCW_wBCD71zzuRSRCuyoL5KPMUwkvJY9v7wIB7RYQC-LeO3uJ9XyPEYkMBtXBOdYiBCDdaOMzJf5Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تاریخ هزار سال پیش نیست!
که هر چی دوست دارند روایت می‌کنند.
داستان همین روزها و جلوی چشم همه ماست!
گروهی برای خونخواهی خامنه‌ای
دست به حمله به اسرائیل زدند،
اسرائیل برگشت و ضربه‌ای بهشون زد
که یک میلیون نفرشون آواره شدن!
و همین امروز و بعد از ۵ ماه، هنوز نیمی از این افراد آواره هستند!
۴ هزار نفرشون از جمله ۷۰۰ کودک کشته شدن (خود قالیباف و خود حکومت گفتن اینها برای جمهوری اسلامی کشته شدند)
بخش بزرگی از جنوب لبنان رفت
زیر چکمه سربازان اسرائیل،
رهبرانشون حذف شدند.
دستاوردش چی بود؟ افتادن به التماس
و زور و خواهش برای «آتش‌بس»!
الان میگن این «اسوه و الگوی مبارزه دلیران» است!
این اتفاقا آینه عبرت و نتیجه گنده‌گویان‌است!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6180" target="_blank">📅 11:48 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6179">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d198d21980.mp4?token=nmJtVxifJb_0lMa91vfxQB2Kl0yaAISti-Ev3AkU1SixHAeNpQ6da29DV_trj8khvPxrYrUf5HM_9EN-eIvw5WfySPzG3XLeoeSsoYswX5sth8hkWlWiIgk_f4TrlpUX4IXdL9UUmDwjJr_jlindk75eyrSqAMfkRqamseAxDITGG5rc5bZ56jylF6NTYIjdGLABxJH7Ucw8j_mViYlXZUotw7QRp0ZnFuE9d6oFtWvQD71vk5xa5n7z5hWntGZyD93-Z458ddmlD8Zw_Mapu6Cro6y6nrAfBHbIFaiFQyyCBbYkjLxYGI4-7OAesO445mTdY0sOWChLg4Y_0miXYib-6KpROpnNjAXHb109a6NpaZnSPgzNfibcXee-vKGfnNru19BpEEYGF4XzB_LRtcEtfb_tPNrrm49csRanR6vkuiG4d0nM6JJgnjcETF1N1Un_g9Y9pYsyiaXu3YPCqr-iLUbb2BKq0AH6xPf_Jni3lCuxEkfL3MHF6ufTmX1BThienJD-3_7JvXMpbBbilPf53GuOtEhf4zkwxVKQB7dvSEPzIBvl2_Era1H-FPpHYOguqyPYkc18meiUOBbaQK1izVEKBs9a_tD9eiSuwLwOBxUGAvqxztEsorpQ9ozjA_ADrxR_mHIOxE-zPdRHxpIS5H-1YpAUzutBm4Getb8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d198d21980.mp4?token=nmJtVxifJb_0lMa91vfxQB2Kl0yaAISti-Ev3AkU1SixHAeNpQ6da29DV_trj8khvPxrYrUf5HM_9EN-eIvw5WfySPzG3XLeoeSsoYswX5sth8hkWlWiIgk_f4TrlpUX4IXdL9UUmDwjJr_jlindk75eyrSqAMfkRqamseAxDITGG5rc5bZ56jylF6NTYIjdGLABxJH7Ucw8j_mViYlXZUotw7QRp0ZnFuE9d6oFtWvQD71vk5xa5n7z5hWntGZyD93-Z458ddmlD8Zw_Mapu6Cro6y6nrAfBHbIFaiFQyyCBbYkjLxYGI4-7OAesO445mTdY0sOWChLg4Y_0miXYib-6KpROpnNjAXHb109a6NpaZnSPgzNfibcXee-vKGfnNru19BpEEYGF4XzB_LRtcEtfb_tPNrrm49csRanR6vkuiG4d0nM6JJgnjcETF1N1Un_g9Y9pYsyiaXu3YPCqr-iLUbb2BKq0AH6xPf_Jni3lCuxEkfL3MHF6ufTmX1BThienJD-3_7JvXMpbBbilPf53GuOtEhf4zkwxVKQB7dvSEPzIBvl2_Era1H-FPpHYOguqyPYkc18meiUOBbaQK1izVEKBs9a_tD9eiSuwLwOBxUGAvqxztEsorpQ9ozjA_ADrxR_mHIOxE-zPdRHxpIS5H-1YpAUzutBm4Getb8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو‌شب پیش شعار میدادن که
:
«
جنوب ایران نکند جنوب لبنان شود»!
حالا دیشب شعار دادن
«جنوب لبنان و جنوب ایران
اسوه! رزم همه دلیران! »
خودشون می‌دونن جنوب لبنان ویرانه است و
مر‌دمش هم‌ آواره! فعلا هم زیر چکمه‌های سربازان ارتش اسرائیله. برای همین اولش میگفتن
«نکنه مثل جنوب لبنان بشیم!»
حالا میخوان هندونه بگذارن که جنوب ایران «اسوه رزم » است و برید جلو!! بشو شبیه جنوب لبنان!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6179" target="_blank">📅 09:28 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
