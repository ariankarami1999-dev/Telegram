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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 22:18:40</div>
<hr>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMD8LmlF9dtW_n9ppKxRpI6QEXxtDEOZeKd6k5r9jaHphX7ZuB2x4FOmuvzkpSzuhK3CooFbmgshifVFysRdGWvr4Pna4MnxN2FNp-esexuuFvmYCJAhgcUfSgH8eqhwpQkR6Yg245Us02bJktom1ib5QIBAIa5PgJ5LGU9C9FTumRkNzb41Q-lnnQmJx9sEq1lhVY0nerk_x5bbVpnD0635S6P9iWvAp_YA4V3r5IlbLiTJMlJLQjVjJUpsnEvndrzup1rLMfURtN_cudyC7poMQIUA-PiU7xaE7158WF3QTASLBthMmRX8yv8yfsd6sbX8zW4upsYobqvtIxBRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJ6rdm-hlmlotnbn9FaHxJ0RX3m0GzYfYxBtckZb0nIVWIxdx7j3lcHH864cKmsuIm0dwzJ_y3pBMEhdxArYfoBASdyluMci6fDXNIOVO2ZfEVlGnnd1FsxHIjDavIXSJWEULKrkwWBJ_fE55yeUvSO5hfN2ybvq2YBoc_Ts1WgzkBvyCkvriILoNLFpkToCbfh2SQfw92mOVU-kT9PVtCbyXf1bqQIwKdbg3ruF2SAB0GRlHHGLSZWBQV6o2sSUAsnod26XixMpiiMLAwZK1FmeCnc55yoqp54QRTdCTecsWubf5pSrh6dfhuu7kojcma0VHqryzf207W9pgS5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlNGoBP_zp4PgiwudZkq5odweOQ2uaMM_6xVDo6Dq8arlPkda4xu-ttOOsPaAoxXXOhN2QCTnYryoFJPK51WUha-2civah0yFAJ50qrdmBcdx1_K0_NksdVS-KAGY2HA-59mMw1ksy4dqE1Ec2JU79SC2_c3OQBDbR46WAQzXLsCNfQuLsauWQ1FY0BsQupo6VvJoGzpedWIyfWGiiAcYBUOp9Mnmmenp-2uSXfTkBWFzCzrKFdwQyDP_eerdTg_IruTjZVfj9qK1LH-K4L7TEeBSDmH36HEwKMgs1_o0-l-Fl8LCBRFh1RGnWpcHIUhMlcughL1qWMcDLfqOC8vBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okuTdKje8YFPAFaFtT8iK04tvGrvGBhCNweAigICTl9Ss3tUNEnsWFHD3T8lwxrziHEaL7O7HnifRaA5bKCU7hyJUfEPc9iO6bvbB1i9qyudjd762YYstJ-EEWxNljb0gQnRllat5LadLyshVFo7sPM7NMe3zPLXFpfSXZAsodvNPMUf1xwvDbM37nYdMMJxWqkLYVArVb0icyZcVGKPskPw-fT6JP17nxMInNiwrkuKv0thzA7i_SuzJn1ATvKYmWRnFk2A1elhgbvJXmYlTQ7VlmXkZsGZZGdFrvsrLBoV1rgq-UQuOLIJACpGEZexpFm7kscXgtjXwtPOLpbedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bolKITap9CnAfddu3Xbnnbc_Nol-MtOcRkkM-MACb4q4R2NTAfRflUDBd7sJJbniUeoQupKSU3-_0qdPuuNStkRxwH-acBTRJlIDMDjtV9AE34I93hBMFQs7WmOEqwcPXhVOwbDV_xdt34idnW0l-dDSeUSUBxg1O4ibEugq2vWaLXqRVFyOMEe9jdO36h964aPsMi3PKNfhGZf3YOah05e4A7c378dOVMCXOl1pqE4UHagkxXkdPL_LbgLZ_jcK5AdmHcSRm1zZhhH1T7KpGemqIUB59Sh1-FiowBk2_zAFcOLXhU3x_wn2wxY1wipQrm3WmcLv9WyNvOOVIty64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BGYr6Tu3uLAxT6kmfIjXrmJZ_2iPRXvaCgij7JIR0WWSdFoH_XlOpoFQg1I04_tixYQ-_g_YRk-dil80y4IMQbh3E6THmqt92zVA2qNZsOhpecY0sG11xGTQUTQ_vUb5FpHMS159suKKWNCuhuR1O3ncKCT8cvii373FRltkDUTgx8bLWpbeckJ50xZr-hZwG3FYlqktqhMjcbgvqsyWdemlOVpQH9m50DgEACMnBvpOYvmvk2XVpKXAR3EFbJiHEU0h36yZEyXBezIe9V_E5qO4MFvnDPlvBze6iLJ9x77Ju89svG7zXAzUdmQp35vFO-y_VuQiOxKjH7rhLUk20A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qH577wtHQL8guJYdxY2gkjwnlp2Gt5FeySa5jIYe_rcDpGXKlW1CJGBdRXakR5H8vb7DMejlZNblkUMTlXnISBVgpM7ecRkf41Iq74dsAiuP68aXDCxS0zfFwDpbY4r78-bNR3P5NkWN1_DkghErKDBKUABv3dnwxKhz9UfU1hkQMACcdSQz1xIs_nG1g_acda_aHfhnlvnDrpE_UApfTqK--a4FRQI9cTOIoCiHZ3bO9mq1CFL92Fyn6etZ2yicG3Zu9NeO4RYOKI3EcveA-8jEExdo3TUaUktU_HFQ_2wigCZNgdsyhpFxw8ddhn7bFXAlexdtMV2nkopqixbd2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=V1TbNJx4rd4atrYmFRxoqJp13TxmEywIl3cdYN_ZcIuwMaCcFwcLK7XMC8kSqyXnFsl1J81XHu-v0xSh-g0L8P0qF--H7piDoROM_6ctNjOm3G_gTuryWvBLZp-k2I14yBsSzRMRCc4K14mTkIQIK_TWwUTQOs4-rXVjzdCBsnbRpGHIsIqr0saBhgrrBwbzzX36tOp_L3RB17DjWTub-52ybXEwWYgeK_uPOmFxiVdeGzxeqVo_Zk9VON2BPW2lOYjUHjd6jKObpy7ingFNO8ZmweLF_TIZ1H7O9ea2btY5S-ufJZfqiU3bxxmP6RsYS6ZibIMn4qK-aVhNXr29cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=V1TbNJx4rd4atrYmFRxoqJp13TxmEywIl3cdYN_ZcIuwMaCcFwcLK7XMC8kSqyXnFsl1J81XHu-v0xSh-g0L8P0qF--H7piDoROM_6ctNjOm3G_gTuryWvBLZp-k2I14yBsSzRMRCc4K14mTkIQIK_TWwUTQOs4-rXVjzdCBsnbRpGHIsIqr0saBhgrrBwbzzX36tOp_L3RB17DjWTub-52ybXEwWYgeK_uPOmFxiVdeGzxeqVo_Zk9VON2BPW2lOYjUHjd6jKObpy7ingFNO8ZmweLF_TIZ1H7O9ea2btY5S-ufJZfqiU3bxxmP6RsYS6ZibIMn4qK-aVhNXr29cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcCeTglkybgU-Ni4A3jXNooU65DAUtec1lyJnqXPTqZppGOHr8qSjlpxs86CQ94YovolvX3rg-vwSjBIavfeUdvr-71Qu4wZaXvgOLM7rq1MwpKkT03EM1wdHdvahtfXp3dJrQvr5uCpJe--SiDPkn-GEEWO2Q_6M40aDE6vL2Z2p9F_3SULJzrAs1HsABwCcyGABkIWbbzzuiT4JqT1Baqm_OP9YPJ_HiJHr7l7pGj_8BWNSg6QjDIPf3BFj-nOKAkHs0fAq__PABuML_o-w4G_SvJyEBxmS_419uJUPAJaxFumkDWJas3P74T3KIFswcSNyb8F4-_i8SiFTKq1pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=G-rw1xSWjvyvGecK6MZg23u-cW8xa7TyCbEaFdQari41LzCglguHg5wmll4cOshCNJqWifbkMza1k5fFa-M8CaeHdPrYv6MW47SSXrGZoVAsmmZDJ1m6Ymlxf5u2Oqd-YQPe4Zovdrg9xcd0MxQFSOwo0QreSGS0w52XaSXOHw7SivUptcEr5PvRCknVQ30Mo8hv53uhbJkkGowwbS3m8iV8Bu7NDxa1N7w5fV6mM738OstFRDcSXcDzNDniO-phENI_LMNV9f6zHgKkV95skRAVy05lIjvpKvD0d-yv03zm9SIryCOqvO4FkA_8W7YdmbnKPUAW3Rtk3sOXJ51SHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=G-rw1xSWjvyvGecK6MZg23u-cW8xa7TyCbEaFdQari41LzCglguHg5wmll4cOshCNJqWifbkMza1k5fFa-M8CaeHdPrYv6MW47SSXrGZoVAsmmZDJ1m6Ymlxf5u2Oqd-YQPe4Zovdrg9xcd0MxQFSOwo0QreSGS0w52XaSXOHw7SivUptcEr5PvRCknVQ30Mo8hv53uhbJkkGowwbS3m8iV8Bu7NDxa1N7w5fV6mM738OstFRDcSXcDzNDniO-phENI_LMNV9f6zHgKkV95skRAVy05lIjvpKvD0d-yv03zm9SIryCOqvO4FkA_8W7YdmbnKPUAW3Rtk3sOXJ51SHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oydY6mDACx_NI_ln8yrQgZcR-Yg_rbKsPBYNsZl4aTpWwLQA3ms__i6Fhx67-pBqARXgO_a5iSfiFbuqtFf6wc9IS2xhp1tEbVg9cg3t7jpCemP_-ycnooHMTRLNNeb9AJp9TsBOewc17NZe2YCCsKCAgXVVNUx7N3uDwERpQg2WqbTpElXSms-eZN4mWZbmbdEkOj9pVwgJVnpA8wOwMonI7O1ObYDWKfBeWCQHzaa57dZtPCetNWmaoHt4u9HDU8Up7XhvUNLGzneYchAap75cqz9lum0kYDFGTayDm3Sz8rRqEoSnUK7kEA47Iod1cNbaPLbeGSgJSJC9n9T4jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGAOy6QkV3xGCANTKsClx6DMhCJL7LWKnqup6ELIxEIcBE1v5pDrsf-VWHFKxYp0TRNatGe0W9e9cBiA_7TPj_wsrs2Li51Ih-S1sTeQgP4Zd2RJwwYd_uhXQtG-HxWAkdExpKml49vKNtF8Y1fUGXIXoAN0AeyBBRZE8DSk123aP16JfDx_MX166LO85WBjDVR-PP4NBP0iLgmpv3nulRtkTaqX-sPlKX0QNAvz1m8osAKtGCgvYjmy2rkdtWRT9al1iZdEKQp7RPqiDBNYICkeWhzQhQR0bHsj6qeoQqGZjYlOkT9K0ICLEtgK_NV2ijZAjjP7SUmbqQ6JJ5iQ9PP4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGAOy6QkV3xGCANTKsClx6DMhCJL7LWKnqup6ELIxEIcBE1v5pDrsf-VWHFKxYp0TRNatGe0W9e9cBiA_7TPj_wsrs2Li51Ih-S1sTeQgP4Zd2RJwwYd_uhXQtG-HxWAkdExpKml49vKNtF8Y1fUGXIXoAN0AeyBBRZE8DSk123aP16JfDx_MX166LO85WBjDVR-PP4NBP0iLgmpv3nulRtkTaqX-sPlKX0QNAvz1m8osAKtGCgvYjmy2rkdtWRT9al1iZdEKQp7RPqiDBNYICkeWhzQhQR0bHsj6qeoQqGZjYlOkT9K0ICLEtgK_NV2ijZAjjP7SUmbqQ6JJ5iQ9PP4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=XsNo_aT8QNBc6Q2ZJ5AdTQmbxkMI-lnSJz-CV1s_-tTHk3FxoKxct-nt4-ZPDzepsKwurunmvHQ8pBsPj3xm-twIN--21EcNywDnr7BZ-uXVKy6m8NbisW_m7aAxp1IqI2d06AJRbgsZ4aWAUJmkKOWgv6Z4v4cDshbUNQmQH6hVHzzGCJxJNppq3PkIz4kM2nDc0Vy4bvskrcqCCiDSmpWsrvBp4920J1VJRyvN5htD3lLikqeaCn3igvbZsWS-eGADO6608I2tm6kOUxniZMTAafhnW_9_fn2paX8Uva2ZDM1TtZhqtdK0bfcB7u11tvPCXnyxf3KxV7bDCZ7HOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=XsNo_aT8QNBc6Q2ZJ5AdTQmbxkMI-lnSJz-CV1s_-tTHk3FxoKxct-nt4-ZPDzepsKwurunmvHQ8pBsPj3xm-twIN--21EcNywDnr7BZ-uXVKy6m8NbisW_m7aAxp1IqI2d06AJRbgsZ4aWAUJmkKOWgv6Z4v4cDshbUNQmQH6hVHzzGCJxJNppq3PkIz4kM2nDc0Vy4bvskrcqCCiDSmpWsrvBp4920J1VJRyvN5htD3lLikqeaCn3igvbZsWS-eGADO6608I2tm6kOUxniZMTAafhnW_9_fn2paX8Uva2ZDM1TtZhqtdK0bfcB7u11tvPCXnyxf3KxV7bDCZ7HOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbGvezfh3Hnxsz6ZjacoEnjKm9qPlHXgnplOT01jCftP_o-ZQ9MEbPNl2L88t5Fs_kj98Z2ciMu5pRRFCRHhkFs96UBpi8Oq1Dwo4On2zFc25RCmGeqM9Bm_rMka5vdVjw40QlRDob3YALx1QcaV5hcBEslHyTyLPF6worPQ7GD7ZWJRHWEtoH4SGjIdajJHXgAmQqTNmGQVgalIDVEX6FU30Ojd6IDriLlhzjeaZa5TNxS_tj6EufzglurTqT8_s-tBXBNuj5mYKmlyNncn4q0UlpTQlMYduz-VbwB7XG64L58rrQqLi9Iujg8D1fg4uVFYwlwjDnmvqO1KTfjUj9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BbGvezfh3Hnxsz6ZjacoEnjKm9qPlHXgnplOT01jCftP_o-ZQ9MEbPNl2L88t5Fs_kj98Z2ciMu5pRRFCRHhkFs96UBpi8Oq1Dwo4On2zFc25RCmGeqM9Bm_rMka5vdVjw40QlRDob3YALx1QcaV5hcBEslHyTyLPF6worPQ7GD7ZWJRHWEtoH4SGjIdajJHXgAmQqTNmGQVgalIDVEX6FU30Ojd6IDriLlhzjeaZa5TNxS_tj6EufzglurTqT8_s-tBXBNuj5mYKmlyNncn4q0UlpTQlMYduz-VbwB7XG64L58rrQqLi9Iujg8D1fg4uVFYwlwjDnmvqO1KTfjUj9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FVV9qg1UzCz2vN74VS1a8qp0h_X-AgqIUWz_5r_Mb01OvJYrb53t_b3G2mMLtj-uiedqUorYHOpaCoLJsEhTkOTKUK8lksEKRxZZHRhr5ygERIdC2nNF2Oia7a4jadLu98YXRe7H49JBOnXUQauwq3Bagp-Xusz0behoN5g3xGg2sGI9mRudrJmHsAsw3ZaNdbEiFM_op8PZCoCI5sJj3sNIOTy1TEEaSc3ciJv35Ext8T7yc21n1PdKkjkbAzhshfQahHSsivNhtmqrUvLHK58HUe3WX9YIlCdn9yhnxi4AtQpzjZMFAH3C0VYqShqmc3IGIUZzwC_ZEc2q2iwvdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSa-aXvTwn-oA9flI7cRFmDD1VBP3g8oza1xX0he6SHJy9ehmaiNlup2QrHZWZU2dJ9kel28mT4Ba9s6ms8MzGDD6Pq0OejET7-E9q5vWQwzc1bX_-LgmaiMjq8BiNxh-NCIucfyZQ31Fw1A7iByjVoJsJhi4J0htWymhTpeE3J4CXU_Gp8g5RfoDIm0LDZUE03BPDM9y_CC8uxL3O1zH5C3R0NLMtsrAQEFT8e3dQr959lXa-VoHqscgRqKbyLt9K40lcVMR6Qc0kvUzpc-0vaw66efj1k7jH7j1x6hfRfy_DiqzHSZHLuH4TOUtBA814QcH2XQ2HlJ7fNF53sVyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JC8KbRsbvyOr23C3llQ6_rRhzdrxgVYB5nQaxetfw1bTyt-GsStZcLiVNAfgI_sl7D4GxvJR6TcqFpPj4XXESwNg9_C86wNSxxJJf7uyug1eII1T4Gucl3vMNDfflg38J6yysGFIlahhY3t75yLUySkKwp0DrY3eLgY61KeAqkZrtqhurZpSetyXvgnNZZpWCZJAy_TeCJ1MK2z9N-gw6J8s7n282h-Ff8gdoFh0ktDbOWQChAIHj9x4BeQ8zsY03K7Sl4xVyltHvMhe22u1jzrrYE_gShTNnFk9bLgWGc3EQh4VdabvhPqNRPzrY6-NKxUYwjD3j5UeViu2-iPVmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SWTisGqhsJKs0jblfV9gdonL9UJ3c1mKqeblfD7qXwhGGvFok-cfB8nQRgQBMWv_udaTG4ZAQu23whoglLd1gUhLlX8IjXvdA2h9uZaOK6Cp7Ru7J5YQqR-58K3gS1QNzIZoYh4DpwtvuIIis7kphFk7NllS839CS83ZYmC4-vObc2gfoOD4sTxbqWVRFQ2pCuQch9jDOGA4tqqcSby6bOS4n9pfSuDvcxM6BI0ta8QacDgsIaubLBAHlpHmbNvmaID4PYoZte_HCS77W0wSqbPLVrJfnXCXfyYDz-vtU9se1ibcFxvgU1pFDvJ4uEdPz5m-DrX-oop44cWGYGi2QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWVq-XjX3WXbqQZOTiP677f6jygo7n66WZwPvqCOV_qlh1pxVUMHbkenzhz6RMJT3FrNcNq6kDA4b_nY6u3GKyo87dixWH6RilfZ_MZAOlvI9wCg1gBXGO3pyAJYk-xA7WJhbej7gWdGXJHHzM_nAKroc1Xea8MUnrV6qADG9TOiIxxWaHk01YtZxjiQylQSOoGoLIWc1aPSmdQlcBADqZqfzHIAYYRl-tsDaL37-c8eI0iYajILaqy537_S7NQPseWJKfHcTQVCE45i7Wt5n3v738DyZCzeALCSXdKDxcnOMXHOK76F3BBIYtmb0q20jbsocVInWIkAJkcDXJIW3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ef3zC6hHUYQbhRRVQd7UsFdRxdI6pHWDw5qJiKkLQJgvuE8vUv1eclFr2BoMhCDp3ssGj_idFMCf9RbCvJDVM1VqW7tLzMjQb8qiJtHu2m_h3vMVpKm-87biJ3amC_OqVRWXu5xrPLVs1_srSxZYRS_qAog6e5uiFxadXUSrGdejLKAM3FqZPFOOLpP6km6j3u5lne4WfVYGwOTm2HbSihnGJQBO0kv4BKJ79t_jaJU84isBYSlYK4DAzFzbA5vVzLmO3rjUer2DCZg49cYj8_1bjmJH7matP9544rX8bggEaMpNn9PpP9k9Xr0aMSKtQYYi926WhmTX_F-xg-qBtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfRd0LvFIqnT2si52XyLZ6GaLBlk9egpt_PRd2g_JfPrDpLisWeiJed6JAt4xyjLAum4ymLGYdOtjc3zPleUo7POD5G5nOx8Tqsw4AvLgkXXH8QLF2jA25n8fvTPmgd8jC9O27OZPJoshiooXU9d6QJrfkwtrpG1G_LRL9ycsL_myUQX2EE_u6asIgbCBOyq-b26nYqw5f1vqMnkFN-aDzDZDhxZyjmJPAD0maFyz65yi2I3K12ox2XqjsNEpxj6BjT6DJr9l7utF4pEUJDOiHxGX5lL0FquwE576VqIOuWSaMGgLx-yzaFgXiQaZU07j8TJPiDB6OkkWsTsCEM5_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P86Uq9iw3RfRVXd0n_86p6lLKTi2aWRGmid5bIPwMRQP_R_3CrI-i717xTtjvgztzlqFkCGwYuopm4p1zHoXJhA8AdGj4SVe_Kh1FFnepoeBbuCi3Dse8ENiLW68PygC6GxamL6h97QH3YOkxgKX7eF_YfW-rk4xeDA1koTgzMGgqIVW6bgcDqGBAR0d0_sBJ_oY3Y_rBYqw9JCW0-D-XV0Z1rIYVfBosB3Q2YGv_7KhccNUfzPgoENqaKm_aS_ehLRQY887d1QFbvj0ZtWcZFxVRpInsqGIWKt3tzhZXxu3w1uOHsTt8GkmlTrh48mO1CR3Xg7WgQY-R1ekeHg7wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NItQun6hCmv2j0sunUvzUPKdwRBiQzOoujkyDdx-GhPetbUbllarcsAbBguToSUnzZgtYcDZATH2cJwV8iNGbNwIEbqiOPoD-zYV69N_hqtzRsM_tJDDzwKjF4XlVnKmemDLQu92yMzczs2KCxO-o1ksJjjBx4fKhgrd53eTpWTbZSHvqgTDRz2wBxuLJnG6UMVvl2VYAkZI5H5KOAi4nyiDWIixEAAK0sqpFRDLaiBhff1omMJi0Ah0Ml6B1nUURj2DcTybhARdYFlij1KuCKMHt-HcWQY91PBOkX1Y0VGsCjuCzO6zMP4WyN01Z6NdeasUpjwdItuY8cPTF6Cn6g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtcjIzyltfUp46QmGIjiD6nkgh5FCeTK-o3WztTd4NY4x9_335VmHG0EXn4LUvnF3u3f3w8sInjHDDz_OE98dqeXl76crONnn_1IxJsU6RmSSu1fGpyS0FGTZFTrZYbi7pv1liOTAPq-v7-oqmDAd55rFY-ZNrh0B018_9gbKqhWRE7dd14Pjg3jjhWQ4nFqQ-y3pM0cOPHDnQfnJZBIsbleLNCBXkRw3bO5p5izph_7y5-luUlvHlRxesODkw8wR2fRncNXM7s5CtPR46Op9x6oTvW5nLze8h4H0poLmOQJYMOXPLZMolHUzB4qB7eiFuX2HrbpaKBfV4PNfFU7Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/junrDRE903OndExrK6-Q631PHkR4YFg6Sj1A_T8WF9bZ3dWxHLyVF6aHLXXWCRurIMkrTBSLzt7N9imwwL2cUbaWlvZS6V5n0eYpSYIzpu1jkM1CZOwY7bpYkLKqVWBxnnHc_IUkfWAzl1_qrPkBqfUYaMf6-myVeyE7oTKGP9I750gqtVWF0BddCua2EoZdgAgbeO71nhxCwQARE6M5kt0wd5mfTxoOLmr4tVagv0Y_4Wl3sPMGw1pnTM8qkWITWpa5j91HlxSz72Ubm_FcuJzKyqt6b7h4lXmHO6-RVEdkRHV-2BZyyfaTzl0OS3kCQil6xA-2ZTGr0QyqKNtibw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvzmFRdLvhSjJpZM0j8St8EkeuFfqyZjGsgW28eFGyEII6SW84UbpIjSjKXTstHh0y2u8wTUvz9Q-fXh1ZeaTgVw-is6nLESZKkcRJvC9yQ8-Np4PR13kIvHzGeFX-4XzDcODJlz4POJ38K8h9GQ493Ppn2rhqLXlbcrvtQdPvGannANmAIsAhfQ_kWYOTXV5CslnOIXUlqLYtNrJtu7o4bIo0Q2eR52otd2mojKrF3Im6AjZ0Nn2iw51uNmYOKzXodmZMOWV5Z5C57wID4V3tbTYlugVfF5Zq5qEKieigeDNdHgBwH_ECynDjbQSiF9s6pge_lFIq8fokygXIMc0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMLetOcPfvlBV0jM-cavm3GQoAavtID7i5cdxxguhBtYbDnidpluKUq3K9ShTq-eG963lzTN569N56Wh9DE8wjHttK6u_lNXpK5BMjo0qMGMaJ88OWQyFqmXUaUFus5Cj9kj-znTjLJbNjY0pzkU7KkVaijrfbeyruSJdttieQhaJIju9Sx4hJbImjbZ5j5B0kHiRfCTW5zqetjjc-SphGzvyXZACV2befAjw6RxflIPXtBwdxgzFabvgz9BjBGbNu1vbFGMcTgi7sAypGc0TgzbECQ9RCtS4K-atnTxJLxK7-5jvUMSNuHl0fBUP88kGoXn_bbjWOVIj-hMC11MEXnY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMLetOcPfvlBV0jM-cavm3GQoAavtID7i5cdxxguhBtYbDnidpluKUq3K9ShTq-eG963lzTN569N56Wh9DE8wjHttK6u_lNXpK5BMjo0qMGMaJ88OWQyFqmXUaUFus5Cj9kj-znTjLJbNjY0pzkU7KkVaijrfbeyruSJdttieQhaJIju9Sx4hJbImjbZ5j5B0kHiRfCTW5zqetjjc-SphGzvyXZACV2befAjw6RxflIPXtBwdxgzFabvgz9BjBGbNu1vbFGMcTgi7sAypGc0TgzbECQ9RCtS4K-atnTxJLxK7-5jvUMSNuHl0fBUP88kGoXn_bbjWOVIj-hMC11MEXnY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SwyzQVbF4GLOIbKeQ25tZJh2TeO5UCZx3c_BLPZuiEgVV1yp39-YrGfDroF8A_ti2WLI0zN3j_cbPtD4U7CcuGLK_ndUcBCCqemB1xWwUoATJDbSLc2BXcb3Hnd1o8PVEvQHQHVuYU1S-Vl6VopMjpdGfNCp8GLA5z5gQo9RMLFYNAQphF4PhS3HLrcMUy9n-yf4ibmidV529bavVvjFXg_kpNynLTxpFSwg44vJFe24VEmg7o5LWJKJNC5zB8vYH-81f87cYo1SDeVd8Rd4m6RN3OwGGadWueCQC7Zr9s5jLhO4lKCoDDIbhEgvlMbcSBxKI0kFoU4kws9Iq2-DwKjivPeJDwZstmn0OZgCPo6IDHMZDBlSRcsi8UUg_6x29CwWbob34zK24m6rv4TZpnYoCxq3wqqY8fPe2ERgHS28YNEKMhBoXLk6BbgYgfGHYlV5tai_3C76E_tWgasg4L7OrB9aDX1-Jns0DE08_4fqGVCC4lhpKlkDobue8TCzfoWOpCaKmKxJKHd3wfrTeOuVnvGspHNkxPb_uyvkypr19B3vBbg5KP8ckb6hHRoFWPkH342y2lwaLjGKTqCh4_RN2U7hiw32mQA3IxYLLM-UPblga-UVwpeP97p2jAClG9i2TLmkASUeOb9ZJfjMDXmWNU8fnTjo_gRQOvyBvTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=SwyzQVbF4GLOIbKeQ25tZJh2TeO5UCZx3c_BLPZuiEgVV1yp39-YrGfDroF8A_ti2WLI0zN3j_cbPtD4U7CcuGLK_ndUcBCCqemB1xWwUoATJDbSLc2BXcb3Hnd1o8PVEvQHQHVuYU1S-Vl6VopMjpdGfNCp8GLA5z5gQo9RMLFYNAQphF4PhS3HLrcMUy9n-yf4ibmidV529bavVvjFXg_kpNynLTxpFSwg44vJFe24VEmg7o5LWJKJNC5zB8vYH-81f87cYo1SDeVd8Rd4m6RN3OwGGadWueCQC7Zr9s5jLhO4lKCoDDIbhEgvlMbcSBxKI0kFoU4kws9Iq2-DwKjivPeJDwZstmn0OZgCPo6IDHMZDBlSRcsi8UUg_6x29CwWbob34zK24m6rv4TZpnYoCxq3wqqY8fPe2ERgHS28YNEKMhBoXLk6BbgYgfGHYlV5tai_3C76E_tWgasg4L7OrB9aDX1-Jns0DE08_4fqGVCC4lhpKlkDobue8TCzfoWOpCaKmKxJKHd3wfrTeOuVnvGspHNkxPb_uyvkypr19B3vBbg5KP8ckb6hHRoFWPkH342y2lwaLjGKTqCh4_RN2U7hiw32mQA3IxYLLM-UPblga-UVwpeP97p2jAClG9i2TLmkASUeOb9ZJfjMDXmWNU8fnTjo_gRQOvyBvTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyUcfEqp8NSPc7ZFI_IsVD6mo_--a5K4QfxeYARrUt09rrXXJETDcZsqxtgLNuULFaD7pKDEmOWTLL5iy0IR8FtiyaaZeaDp5gsgBLALGLILRBEqCzIpO3b-EVpqI5OQDxVTWKeu6Qlwe1-dRLmyq3vJwYeUg61qujryzCIKa06L2xhTziV95NH-KjgtHp848uf13Om4PyqB3VJNrySosPYroKuX_2M-FWSb8c_F3CwGWZ1msrzW1HI0ylimyAaIYj6pdwMqmFzhauS_LrO9mp81pSYHzHqswsyZQ5Nuvtc-TMNoDr0_gbCKZV30xp7tpyhm1VQIT36Rs7PbPr8-EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XgHJpxZg_h85Qh_VQXJkFwWUJf5ymDM1DSHj0n4ERfQVvK2RmJsUThvfwaBCiexWjfqlQ6VJplYsoFb6t7yCtMBJnlye8_PxUdSJAtjLfYeWmjTvPhkQxpccyj5aauXkOPZrwtFob3eZ_y2rP1bJ6QUyArnxcB046bpS8ZTUX8aU7zDyMPnBupa7VJIfXr82SMsH9oH4fZbdkWeXS5JQBEEfqYNOrSmlWwKV2QIBdqQfTjIvzDxDnS2BYr5PLsHlKPiWiaDtoBC5gfLl6holdY5q2M2SblAMhQGy70uvq_R4eY4FWqRnH2akmDjs6e_6sin4DSoaCmHFDMRs0kyMWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=XgHJpxZg_h85Qh_VQXJkFwWUJf5ymDM1DSHj0n4ERfQVvK2RmJsUThvfwaBCiexWjfqlQ6VJplYsoFb6t7yCtMBJnlye8_PxUdSJAtjLfYeWmjTvPhkQxpccyj5aauXkOPZrwtFob3eZ_y2rP1bJ6QUyArnxcB046bpS8ZTUX8aU7zDyMPnBupa7VJIfXr82SMsH9oH4fZbdkWeXS5JQBEEfqYNOrSmlWwKV2QIBdqQfTjIvzDxDnS2BYr5PLsHlKPiWiaDtoBC5gfLl6holdY5q2M2SblAMhQGy70uvq_R4eY4FWqRnH2akmDjs6e_6sin4DSoaCmHFDMRs0kyMWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=V5wDNmzLGUuHod7_rtrGTHYYOKEhAT3ysOJ7RAAasOIaaqs67UOjg8898ogNkw4W-bodG9UblGoMWi5ZIOCRqwe3IYNVA7Y_-m2_2kwJw77E8SLXXtu-3BYTD_RSMxA0x9HdBXRF0F8cOJDGvMKig2PFhb2Ycv59oi2mi9fgy50iaRnncH80Y8NekGdnkmOKps6sNYgvIALzvHmdoaTR0K6Z1ahS4iL0RpT0_E65suJiXO9L1BdtB-Cq_RhO6o3NI9R6yPuy61wxiOxejdw5JjTEaiJhIGyzp2BnLXqdq_2i9hRwM5yYxHsKru_HFgt_FU029DSiDF1jJ8kA10oYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=V5wDNmzLGUuHod7_rtrGTHYYOKEhAT3ysOJ7RAAasOIaaqs67UOjg8898ogNkw4W-bodG9UblGoMWi5ZIOCRqwe3IYNVA7Y_-m2_2kwJw77E8SLXXtu-3BYTD_RSMxA0x9HdBXRF0F8cOJDGvMKig2PFhb2Ycv59oi2mi9fgy50iaRnncH80Y8NekGdnkmOKps6sNYgvIALzvHmdoaTR0K6Z1ahS4iL0RpT0_E65suJiXO9L1BdtB-Cq_RhO6o3NI9R6yPuy61wxiOxejdw5JjTEaiJhIGyzp2BnLXqdq_2i9hRwM5yYxHsKru_HFgt_FU029DSiDF1jJ8kA10oYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZh5yaYOnYfrDMU0GnVb9rMV0SkdFruD35bB0epUZZggt2DSafp4GKz1yoTHwqz_qtJs954T3ZuxkgjW51HiC_uiGrvA3FfUphcApxBin4NZTdUdRK9QyOrdG_hzep6JaniGXjmCg8-maieGu8oWseNb15WXdgbHOXmN_hzwdEtXBeSEHHPNbs0GKBDJIvonJP5xf2OfUuxD16mKU29lTM_bIiTqUW_WBTLuCHAOF2KABosuifRCtCsiMHTCq1mL1_dNXUylAFnTdJkAhnxtLzwcDTthxDvhLHmKpQ7LBjsZPxTxi_O40Ieh2xA4HNNBNPptqudYrqnbiEKGnwIh3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IOiTQBYzXWvsjTs9_L3XcxjeG1cDtupVl7jyJ6IiWxX7T6kf1BPlsa6Qn5yEE7utXMVNDj-5AaVHDmgijF1BSr6i307Dwqd8x7JTkBAobchyniAMqaAzzUez7oasA8o9Ph-7VNbEIlOaUTK0qeQTR1jKY85iamOCDOWUd1o-6ffrhthqAyqRjQD7bewvZvC7ZVJsoqJUTRa642jnaWe8soo5luY1Dz1eQ5doo_DKeHD0jZXzlAT9x6023OxyFzN1i9DJSp5R5SftuTMTHkoHFp6l1SCJdlmcf26H48dMscSqaXdBIQmwkv1Fqo_8XLOywgd2b5uIOQnEiGZXKEBY0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=nq4t5Qa0mCztg3cujuTB-79TB5BiwIPG8FaBsh_owuxXXrBw1bZBnCEyqDUomwemQqqeq95ANmPTvVc2FCmmcxsnCuYqyaP7LGfUwNT98GfFqtyg65THyEwIrc1KRkBRQiXWE5W7s5agpBdw63RVBbPua9LXHvAEH1knXjHz9FLIolVGltUzkBovb-XS4UGhTZd6p2289y_03n2pDN68isNnGOe9QOIkK94JU-SpIe0pl4pu5Lzq7atl1Ea7JXOGb6eT4VmxMcovh7iRWfr3tzdzPulXkOQfs8X89a7NN3SQuenPUrqoa4TXhEtDwPnyhIPHKrZ014vvzfG8QuR9-r60cMW655hZjw8sPgjLg5zbyHYaup5oasrNeVCbci8E_65-pDFQV1d7R0CZ2usg610rbVW0WJrhsoX_9fJrjohtnP0symT7BFTJfQYtzYX3yb85FGiX5is_OtaPK4FNUh1QTxcLxx6oSMAD4dby1OXIBYsB_g-YmZvydSevKuJKaWejHs5ALlgyzFArQmmrNmTWRA84AZFl1504JMOg536FE-2cqfsHRhdlPldGfAKfXdIAriNtAB4In9-ES9ajkMX5JL0x9R8y3-i8ldIiOq1dhvvkHRhXpZp7LzYer383v_Fga23TotlL_PhA2vYfO7LC0Jx8UE6FGGaw6rOZco0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=nq4t5Qa0mCztg3cujuTB-79TB5BiwIPG8FaBsh_owuxXXrBw1bZBnCEyqDUomwemQqqeq95ANmPTvVc2FCmmcxsnCuYqyaP7LGfUwNT98GfFqtyg65THyEwIrc1KRkBRQiXWE5W7s5agpBdw63RVBbPua9LXHvAEH1knXjHz9FLIolVGltUzkBovb-XS4UGhTZd6p2289y_03n2pDN68isNnGOe9QOIkK94JU-SpIe0pl4pu5Lzq7atl1Ea7JXOGb6eT4VmxMcovh7iRWfr3tzdzPulXkOQfs8X89a7NN3SQuenPUrqoa4TXhEtDwPnyhIPHKrZ014vvzfG8QuR9-r60cMW655hZjw8sPgjLg5zbyHYaup5oasrNeVCbci8E_65-pDFQV1d7R0CZ2usg610rbVW0WJrhsoX_9fJrjohtnP0symT7BFTJfQYtzYX3yb85FGiX5is_OtaPK4FNUh1QTxcLxx6oSMAD4dby1OXIBYsB_g-YmZvydSevKuJKaWejHs5ALlgyzFArQmmrNmTWRA84AZFl1504JMOg536FE-2cqfsHRhdlPldGfAKfXdIAriNtAB4In9-ES9ajkMX5JL0x9R8y3-i8ldIiOq1dhvvkHRhXpZp7LzYer383v_Fga23TotlL_PhA2vYfO7LC0Jx8UE6FGGaw6rOZco0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=Lyt-2SIsV68pubBfiWdnhXKjLXnTm2yO_I2zc5ezCVGXGHsl0nS38R0VG6h8wkYuN4ZdvDlxYVLCt8TNxHAqjt51mbKnG-LCNLwym8bCLcJfkkt2Q1UXkne8Pfx_oQD0JckFa03TXPiNBVrXUrqNxaUQxiaVfIbpZbB_rfGvOn2qr-bLIh-Rb5DHSsVdvDtFuiQC43j60ho5bliM8beS1R_v6saXlL6kQAWvas5BvHZqB5GqoIXoBi518eISfMB22O51bSpUuKbE4ePd7u5CeMKsBnbVZGkozvF5i-HcS4J0mQFDNVlTDPn3NvDHac9qG6jDTxQE1f4Hu3l3NTZc_IGLgsghuMjgsZKXvRKK5kY02s9azxoFx9HdK0QFbWGN19wpWi-VUzjA9mVlD_LzBQfNtzHFGoZdSFRDPRAStDIV-OnnQVNqq-aXBXg9dRA7ZjC9jteuj6eouO3IMAlGwINXdFKrHPhPz_nh-P7sjvmRck13qTfpZYLR48IzrPol7FzlBJuETts9xSuEOnEmysdPRwLt3orNDl3zIy251dvHblbSImVA9RZHWNY3Y2Gr1jyjS4kyQEwHBjecoM2L8qLfej4Y72ynQXVTcRFxFt7Qwc1OqtulbvothnFUGXgKN09pdd3LnJOtLkSoFkqkF8Dc2McOoCn2A36aztPxaQ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=Lyt-2SIsV68pubBfiWdnhXKjLXnTm2yO_I2zc5ezCVGXGHsl0nS38R0VG6h8wkYuN4ZdvDlxYVLCt8TNxHAqjt51mbKnG-LCNLwym8bCLcJfkkt2Q1UXkne8Pfx_oQD0JckFa03TXPiNBVrXUrqNxaUQxiaVfIbpZbB_rfGvOn2qr-bLIh-Rb5DHSsVdvDtFuiQC43j60ho5bliM8beS1R_v6saXlL6kQAWvas5BvHZqB5GqoIXoBi518eISfMB22O51bSpUuKbE4ePd7u5CeMKsBnbVZGkozvF5i-HcS4J0mQFDNVlTDPn3NvDHac9qG6jDTxQE1f4Hu3l3NTZc_IGLgsghuMjgsZKXvRKK5kY02s9azxoFx9HdK0QFbWGN19wpWi-VUzjA9mVlD_LzBQfNtzHFGoZdSFRDPRAStDIV-OnnQVNqq-aXBXg9dRA7ZjC9jteuj6eouO3IMAlGwINXdFKrHPhPz_nh-P7sjvmRck13qTfpZYLR48IzrPol7FzlBJuETts9xSuEOnEmysdPRwLt3orNDl3zIy251dvHblbSImVA9RZHWNY3Y2Gr1jyjS4kyQEwHBjecoM2L8qLfej4Y72ynQXVTcRFxFt7Qwc1OqtulbvothnFUGXgKN09pdd3LnJOtLkSoFkqkF8Dc2McOoCn2A36aztPxaQ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=KWcYnd593ekXZrzuvrXCtKqdau-htU2rXn7FRfDyrLmjVYGbCIuLeyCKHKu8Q0_CwRgz900oYRzS_NbR8YMvjWt_aTPV-x4yEEcy-8uBtKL2Jni3XOlszkO6brRhQxU3XvEoRO9TUTgwj0Bm9Ex-erB0PXW3hxtULlowgDGfowmj24RGmhDNPNZgDwtPYmxHNAhE5_YuEojqQ2YIjXv4zOADQx2YO-SjRPKmy7eMBBg2jk28i8T0PZGIiUmV9iozicPBUg5PxVM7zUV-lJ18fseU3NUopv00aK6d7jGaUXzO1MWUdgYTPLeaYKUnjPL1LaB5zvnWo0ejo8wmT2DE3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=KWcYnd593ekXZrzuvrXCtKqdau-htU2rXn7FRfDyrLmjVYGbCIuLeyCKHKu8Q0_CwRgz900oYRzS_NbR8YMvjWt_aTPV-x4yEEcy-8uBtKL2Jni3XOlszkO6brRhQxU3XvEoRO9TUTgwj0Bm9Ex-erB0PXW3hxtULlowgDGfowmj24RGmhDNPNZgDwtPYmxHNAhE5_YuEojqQ2YIjXv4zOADQx2YO-SjRPKmy7eMBBg2jk28i8T0PZGIiUmV9iozicPBUg5PxVM7zUV-lJ18fseU3NUopv00aK6d7jGaUXzO1MWUdgYTPLeaYKUnjPL1LaB5zvnWo0ejo8wmT2DE3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a5YEoo0PJeGKCYwuiuivmCD02IRnaBVPxPvDIqTFXpgoDYfXbDRPqIjx5K7xaW0nEYn5qsSZuk2-fpIJw2YLTWfiHJL4SdHQMAcANoGc4cW865QSOIewnNo6F-4w_MBRxP3TSkPu3Mp6YKG4qSUvVj_p3BIMt5EoFQR6bQc4UbOpxiNVEvfQN9ksZUeQd8BIIHjm94hc-dzJ3OA8kl0fAAHD3vwZL5QRptOyZHmyTXLjeLIXgLn6ET-NLakraferMw9P6Tf_nH6Xk6ACDAOqhaa1g1C1IQH9wNsW1V4rJkK1FYFGFLJqRHXLb7B_VgNuaN2ty8tWQPYntMfPUZwFeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=XGxEfLRylQVZDQ9ioF031bRSCct_n99Ejv1UJ-kA3Kylb2Gd7_pb4KbiEb4yR4RZY4cZtSkAeR7TL6Kz90tXoCJYfg4xIEcG9lR4p9OJT6tSXgOZCG6oOmnMLyiN4i-eKcndZLB03hSP8kbGebw8UBreUV0plFGk5bU_v6K6kJnf4msYqwv8MUgKQcPXCc0XlnvgR_KWXo5xayT_gTb0w_bQw8Xa7T-0vHFCcHuu9L4w2FsXWwaAdRt3-78v89lzskdKG_8rRtNciq9eBnHtf4Oy8jSiAN2lAQ2BNC8M9CNkLssmgIvtuaBJZLtno_2Kc7rGQzd15wLVi9USKGO2OjIXHeFBXfzXeKVz6qhldkCdMBtGV1De1Kl8-G8hjMvfbOfG9La9x8JjaAmEsUzMeOBPVV7QPf0bxgbOvxhRPnklydio1QYReXt0Nb68aUm-LPe88cqld9lVFVzEyuZt12P-43JJ0wSe-LJ9LCO60PAQ1wvtClmOgGEQlg3Ma861y7tG0ise2CyDv1SaO4hhHkHkBllB9ZX-7NLoqj-HzDUlCX868r7yxNkG7VEG61UwR67ISueRaPxM5ekBJj-upPVh0W_F85GGMJDGh5g7vBTzwbZ4fKLNpTU9N7CJNKHfLZBUBPxd0CmDUI2JdRILFuU7wmSbqIXWJeaEt9xe9lk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=XGxEfLRylQVZDQ9ioF031bRSCct_n99Ejv1UJ-kA3Kylb2Gd7_pb4KbiEb4yR4RZY4cZtSkAeR7TL6Kz90tXoCJYfg4xIEcG9lR4p9OJT6tSXgOZCG6oOmnMLyiN4i-eKcndZLB03hSP8kbGebw8UBreUV0plFGk5bU_v6K6kJnf4msYqwv8MUgKQcPXCc0XlnvgR_KWXo5xayT_gTb0w_bQw8Xa7T-0vHFCcHuu9L4w2FsXWwaAdRt3-78v89lzskdKG_8rRtNciq9eBnHtf4Oy8jSiAN2lAQ2BNC8M9CNkLssmgIvtuaBJZLtno_2Kc7rGQzd15wLVi9USKGO2OjIXHeFBXfzXeKVz6qhldkCdMBtGV1De1Kl8-G8hjMvfbOfG9La9x8JjaAmEsUzMeOBPVV7QPf0bxgbOvxhRPnklydio1QYReXt0Nb68aUm-LPe88cqld9lVFVzEyuZt12P-43JJ0wSe-LJ9LCO60PAQ1wvtClmOgGEQlg3Ma861y7tG0ise2CyDv1SaO4hhHkHkBllB9ZX-7NLoqj-HzDUlCX868r7yxNkG7VEG61UwR67ISueRaPxM5ekBJj-upPVh0W_F85GGMJDGh5g7vBTzwbZ4fKLNpTU9N7CJNKHfLZBUBPxd0CmDUI2JdRILFuU7wmSbqIXWJeaEt9xe9lk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=rkMoXufYU7y5wGo6-Xbsfan8ofid7bNyE16gXBo8szi_88GQkEQY66i3vVyMVVuenT_h0L33b41n7d9-N6c_EQwn-OXCGn7_jWOcZNAEY6Gds0wAC7_uAshJGQEHaEbuEjmS0w_isFVnQvtJlUQVglWqYCnncKH80nxRs2w0SLGQVPPGtFQns-boc8AIiN9rdIkmFB3j82r472bzrf4tF69GJ07fouS7IH7mJFblNzTq5nBzGWrAOLb63GD7alOyn6aywZczhYzjIwsVM11wnHRkNasJGY4gYuiheSdtH8z9IhBvY9-fhKpPeL6dtbJD-pOqoIJVTO1gUKxBkCo5lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=rkMoXufYU7y5wGo6-Xbsfan8ofid7bNyE16gXBo8szi_88GQkEQY66i3vVyMVVuenT_h0L33b41n7d9-N6c_EQwn-OXCGn7_jWOcZNAEY6Gds0wAC7_uAshJGQEHaEbuEjmS0w_isFVnQvtJlUQVglWqYCnncKH80nxRs2w0SLGQVPPGtFQns-boc8AIiN9rdIkmFB3j82r472bzrf4tF69GJ07fouS7IH7mJFblNzTq5nBzGWrAOLb63GD7alOyn6aywZczhYzjIwsVM11wnHRkNasJGY4gYuiheSdtH8z9IhBvY9-fhKpPeL6dtbJD-pOqoIJVTO1gUKxBkCo5lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9gU_BS9zkLWB05FqljLD19BvpGCiAiAMV0yYXv04Ufr8DCbXtHS-vQteLeHHj3XvYt1esCCM97pmehD5knQGXFQyQ3zO7-MBQmgiOUXgTWTPabF5WQGniOi3rjgiBuHGTfLU2ysEEvBBkIz7Yi8QXZMKnzmml2Zb9DvoSzBqmaWsOwMzNevwKyyALv55y7YmlmZ7q6RHCk39UaUJ9aBhf3ELZMOtO0-zSOey-ISLU9u_spbbh_DsBfl-S8BNPR3K9AkGZS6qRjYOE1HLVz9eJbD2XM49Dv0dBrW3ujQ1-9eKPfDeIlTimBLy7c26lBM4_IkvRmoOKiEHqGNN6FWpQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NzqzOQ-Wddxdrjv0h9sp_UGGAK1rkS0k-80xNNzw0LXk4JDBf5_BCThVrTBlmYUvY2ID-Di4hAiEfBRmRn2xAlajruQr_aOo6ft1ZExSNPloVEbMMuFkjKPwiqFggYZ-uhqC4ENxyouy-Pe8j3gm1SqfnXTIK35gccOoXbQbYxKgNm-GYDOZZoV_BoSlhZfwqy8DfVRzNFa0Fp46pK-u-eUEQMoREuB4m8Gl9rZW1Tq5evsrWMYWYBn-Rr-SPHSS0Ykdma1DzQnN9dRRUpKDLZ4hvPA6YKMik7o59Ycnv8G2f7W9WflVoLb--NTh292HiJLgHVeGeAxJPMpttSSB8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuQGRUhadRTN14iCQcmDB-hxB8r14B5vnzYL5ooBxphzjypXYOEvlFoxqNsvnTD9DViE1aQJCrq-jyad3zEQ0hfY5w32HXxWbvlFMYzxVLUDNtskSWu1oVP18l8TLQ4s9hQibO8EGYxTa20KjwdEjj4GLAvYuoVvZNuiAT1HbMW82qliDulvjxkC2O1UU_IjK5E2jNwR9eOnDgqczfm9A1Nn6PIz14hy_Qur_uHGrdhH8hBT9Orkotl2UH_CAx9ME7N6Zo4TMQndLKAUx9h6ppXuELElJshVi5rGuZfd9JpK6QaWjhgc0o7f-x3OQKd6JeB_Xj1XFhfNCAv2pEQWdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JpLbzKhoe-l_4VIteSlrv_0GcTPYrlEMs5d3i-Cv994rCjgx26vjh45QijdHU9cNo-w7XvRkRemFrVN0q7O_V5iJblrI8WHHH22IMSMpJ1Yb-DTX-7fCbbCY-8EvSIW-Xq7kYrbpgb6Wrv3wtJJq3HC5NIOmDLbBzqtSqw2EP2TnvpR8vARoqss8jMLrk_gLiLtVuY3cFPRcgyO18lAifn8clBSeECH_ylLDj2iaV3_HJH8sI63IkQSyFK_pkLvDe2B5qEMxRX_jRApg62xLBli6lNoKpSTUAk2d20kTdSb6Eek8r1wQfV5WrSZkUJjHKzKqcY4wq6uaX9pRJYslCSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JpLbzKhoe-l_4VIteSlrv_0GcTPYrlEMs5d3i-Cv994rCjgx26vjh45QijdHU9cNo-w7XvRkRemFrVN0q7O_V5iJblrI8WHHH22IMSMpJ1Yb-DTX-7fCbbCY-8EvSIW-Xq7kYrbpgb6Wrv3wtJJq3HC5NIOmDLbBzqtSqw2EP2TnvpR8vARoqss8jMLrk_gLiLtVuY3cFPRcgyO18lAifn8clBSeECH_ylLDj2iaV3_HJH8sI63IkQSyFK_pkLvDe2B5qEMxRX_jRApg62xLBli6lNoKpSTUAk2d20kTdSb6Eek8r1wQfV5WrSZkUJjHKzKqcY4wq6uaX9pRJYslCSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFt0mhiMkRp-bbDSXYGxzuX_V4MG3hQjSsJMhvS4_IPJwL_gMSF3z7pkwCcV6ozrpFRcfi4BC0FnXXZmxg9VA5c25Mjj-a2n1r5M6_KP8sJdfwFQid3GmItCfiPzv2Gbhf09ySun-kDJiSNdo17_D_GWGSy63RbqLp3pq7hO8rZQ_0Gsd_UJEl2gvUgCqDSDQa4sAlB7WsE__xK3AOI5ot8v5g-up8JZhdGSo3ipsW3aq0x3y6YknHGTD0tuBAMJQ0RBOlDDQH9MmWdxO83Xdpje_uvPUyFruXjWeSKPzDgKu1gQq2CZYicAjzCslXyfUgyohaqZXsnhy9TWHuzYaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=V8KLyQuYp6yQw_0j9ycVSnC8NF1TBs1xkpnZS8uu5TCmi1qO0nqb-LP3NSn5lG_uqjRBJLck3Smy9mG6yz8lR6NnOqmPMpMpTHlOq1VazTS4T3_YQOa8nEn2byCN0kvoGil48D-IcFKr63yMAFd129LIbHwBGQA7HpFhuicMmxqKuFEZwGSylwIWm12f1nvDvbovZw8-HJOqjOKVAYGkCuU4ijyA-OJ0syS6Nmu8BsLmKb_z83AMO2lT_54BhyJLhF1aAPUvx6_m3RXZRbTEvzb36zp3nHJNs7GMmJYfs3qyWD5epOYjrZjm4QozlUxTnlJ0tyeeQqg7s_zltCILkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=V8KLyQuYp6yQw_0j9ycVSnC8NF1TBs1xkpnZS8uu5TCmi1qO0nqb-LP3NSn5lG_uqjRBJLck3Smy9mG6yz8lR6NnOqmPMpMpTHlOq1VazTS4T3_YQOa8nEn2byCN0kvoGil48D-IcFKr63yMAFd129LIbHwBGQA7HpFhuicMmxqKuFEZwGSylwIWm12f1nvDvbovZw8-HJOqjOKVAYGkCuU4ijyA-OJ0syS6Nmu8BsLmKb_z83AMO2lT_54BhyJLhF1aAPUvx6_m3RXZRbTEvzb36zp3nHJNs7GMmJYfs3qyWD5epOYjrZjm4QozlUxTnlJ0tyeeQqg7s_zltCILkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=FexO32L7zuoIo-GlCPLjm-vHFGiL7IkeSSDqoV3Lx1Tfu_hkk9Cy5QWcYmE8CfJtdkQamwg3TcdsH-FDDWZiog1DR7Pfco8kxKRSUAYYSJzLRMunOC5ORzg8H-P1zhUKo19cXEjJBQRxkvOkWGPURJoJ0mGMPiVQymfAcZid4uSXPuxI_ZpgiH8wLydKDJWFC4_U3b1OfGTZFhbjnJHcb1BBebulKfSlMZ0t9GOlcX3-uH8PLKLsCZl4r81I8hdm73DsqYPRMPqG2SG4EdUjS6-ChhI_54sdHNWuvHt6MfmWM8z93GedNKn0HsEh2ugyQzbJdkCBcDTBkHjBv6QRlxAZJ_zRky2AmTINaj76cZychStcJcQoEFQm0IK1yrkmH1XSv_oV6xl-lArLWZwZF6RrhjryspDuxVAhGeBKrhbzaQ_NOCyv6HoASqxUiCmnVxytS3EzbIbjG_4tnLTTq8jtuOWDtltOWJD6xwBekfDWFsVTGk1atELPadKnmSLQF8uNsKuPtOUIefIdqP_J-olYzpNHMXsFyjQ0FshXUhEZssN_-WMRm6Vd_K2ShrjtyeFwxkVSNzfh65tdvVZUN5-A51gvFEg95dOmyZOc1KZ7pRVyo6t81Gz2Supt-X4vTQOdBUpcvzDRXy2gmoSUKIqSlDaR78f_YBiQtEhTyPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=FexO32L7zuoIo-GlCPLjm-vHFGiL7IkeSSDqoV3Lx1Tfu_hkk9Cy5QWcYmE8CfJtdkQamwg3TcdsH-FDDWZiog1DR7Pfco8kxKRSUAYYSJzLRMunOC5ORzg8H-P1zhUKo19cXEjJBQRxkvOkWGPURJoJ0mGMPiVQymfAcZid4uSXPuxI_ZpgiH8wLydKDJWFC4_U3b1OfGTZFhbjnJHcb1BBebulKfSlMZ0t9GOlcX3-uH8PLKLsCZl4r81I8hdm73DsqYPRMPqG2SG4EdUjS6-ChhI_54sdHNWuvHt6MfmWM8z93GedNKn0HsEh2ugyQzbJdkCBcDTBkHjBv6QRlxAZJ_zRky2AmTINaj76cZychStcJcQoEFQm0IK1yrkmH1XSv_oV6xl-lArLWZwZF6RrhjryspDuxVAhGeBKrhbzaQ_NOCyv6HoASqxUiCmnVxytS3EzbIbjG_4tnLTTq8jtuOWDtltOWJD6xwBekfDWFsVTGk1atELPadKnmSLQF8uNsKuPtOUIefIdqP_J-olYzpNHMXsFyjQ0FshXUhEZssN_-WMRm6Vd_K2ShrjtyeFwxkVSNzfh65tdvVZUN5-A51gvFEg95dOmyZOc1KZ7pRVyo6t81Gz2Supt-X4vTQOdBUpcvzDRXy2gmoSUKIqSlDaR78f_YBiQtEhTyPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=PieUqcRYtgbavNlmvi_glMvnU26F-He38zkIBNA920UQUvw_0Dj1SKWUcUwi5GMplG8q2Yr9VAl4Y1InjYsiHgWVrd2zAo6jAxF-ZemM0qqrpFf_9Yhq7VyFhAXJjEqCFXgn9EXVJreqz4KdoF8BrZOD3zq3iHLq02LYs7PAntJiyt1z63NYbaPGqdynw7TDQLI5wSr85ajiW83TBDSV_KhJzrv53hSzyrf40VMpja7Zxnqtg8_XyvfRcMQ5r7Ah9xWf9YDrP3TdtcyEDVMmRVyHEJHTcNifXEI9Di3OYik6g6ZuEt8IIJqm_z4SJxLrDYYz5t1WRWi0NE8FyIR9YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=PieUqcRYtgbavNlmvi_glMvnU26F-He38zkIBNA920UQUvw_0Dj1SKWUcUwi5GMplG8q2Yr9VAl4Y1InjYsiHgWVrd2zAo6jAxF-ZemM0qqrpFf_9Yhq7VyFhAXJjEqCFXgn9EXVJreqz4KdoF8BrZOD3zq3iHLq02LYs7PAntJiyt1z63NYbaPGqdynw7TDQLI5wSr85ajiW83TBDSV_KhJzrv53hSzyrf40VMpja7Zxnqtg8_XyvfRcMQ5r7Ah9xWf9YDrP3TdtcyEDVMmRVyHEJHTcNifXEI9Di3OYik6g6ZuEt8IIJqm_z4SJxLrDYYz5t1WRWi0NE8FyIR9YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU0ZMHRMuZarCv0u1Y480vo3gE1qWoA0_mxFuFtihVA-dj4b5Uf3dPQhHFFtnm-60tgoQxbBWSvawT_AgSN_2bAeukGsRPA8NaWEM81ejhauZbcHYADRMo3wgXAl8L4SCmEI4jyAIg4XYYelX0hueinP8od3Y2lpMphRnw1SVFPqd7gop8OPIMPKkpWVQkU-zrLoTkpp5jzLbP7i3jQ2JT_oiHQo-pzBgIj4pcyjQhbI4Bhd9vZNNjaO-KBe8CFBDfnG9dV3wJbKPdmZfpQgYdRovgMGH-AmOkXYnMZ7cxlRfeJxxlZYPnPp8bYduRS0l5eYjkhZr-j96uNLo8P1tA.jpg" alt="photo" loading="lazy"/></div>
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

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
