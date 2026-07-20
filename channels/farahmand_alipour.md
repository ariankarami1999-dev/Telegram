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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 23:45:45</div>
<hr>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMD8LmlF9dtW_n9ppKxRpI6QEXxtDEOZeKd6k5r9jaHphX7ZuB2x4FOmuvzkpSzuhK3CooFbmgshifVFysRdGWvr4Pna4MnxN2FNp-esexuuFvmYCJAhgcUfSgH8eqhwpQkR6Yg245Us02bJktom1ib5QIBAIa5PgJ5LGU9C9FTumRkNzb41Q-lnnQmJx9sEq1lhVY0nerk_x5bbVpnD0635S6P9iWvAp_YA4V3r5IlbLiTJMlJLQjVjJUpsnEvndrzup1rLMfURtN_cudyC7poMQIUA-PiU7xaE7158WF3QTASLBthMmRX8yv8yfsd6sbX8zW4upsYobqvtIxBRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJ6rdm-hlmlotnbn9FaHxJ0RX3m0GzYfYxBtckZb0nIVWIxdx7j3lcHH864cKmsuIm0dwzJ_y3pBMEhdxArYfoBASdyluMci6fDXNIOVO2ZfEVlGnnd1FsxHIjDavIXSJWEULKrkwWBJ_fE55yeUvSO5hfN2ybvq2YBoc_Ts1WgzkBvyCkvriILoNLFpkToCbfh2SQfw92mOVU-kT9PVtCbyXf1bqQIwKdbg3ruF2SAB0GRlHHGLSZWBQV6o2sSUAsnod26XixMpiiMLAwZK1FmeCnc55yoqp54QRTdCTecsWubf5pSrh6dfhuu7kojcma0VHqryzf207W9pgS5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlNGoBP_zp4PgiwudZkq5odweOQ2uaMM_6xVDo6Dq8arlPkda4xu-ttOOsPaAoxXXOhN2QCTnYryoFJPK51WUha-2civah0yFAJ50qrdmBcdx1_K0_NksdVS-KAGY2HA-59mMw1ksy4dqE1Ec2JU79SC2_c3OQBDbR46WAQzXLsCNfQuLsauWQ1FY0BsQupo6VvJoGzpedWIyfWGiiAcYBUOp9Mnmmenp-2uSXfTkBWFzCzrKFdwQyDP_eerdTg_IruTjZVfj9qK1LH-K4L7TEeBSDmH36HEwKMgs1_o0-l-Fl8LCBRFh1RGnWpcHIUhMlcughL1qWMcDLfqOC8vBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okuTdKje8YFPAFaFtT8iK04tvGrvGBhCNweAigICTl9Ss3tUNEnsWFHD3T8lwxrziHEaL7O7HnifRaA5bKCU7hyJUfEPc9iO6bvbB1i9qyudjd762YYstJ-EEWxNljb0gQnRllat5LadLyshVFo7sPM7NMe3zPLXFpfSXZAsodvNPMUf1xwvDbM37nYdMMJxWqkLYVArVb0icyZcVGKPskPw-fT6JP17nxMInNiwrkuKv0thzA7i_SuzJn1ATvKYmWRnFk2A1elhgbvJXmYlTQ7VlmXkZsGZZGdFrvsrLBoV1rgq-UQuOLIJACpGEZexpFm7kscXgtjXwtPOLpbedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6HOGWW58Ca8r-IfC0ijyKWBEbOMY0OfGjz7IobZkHa-aFb8m-FOHAs580oxjfI-FLULgtoG-ornyIyE6DwdizY-8jXfwlEU96jGIkjEhRK4-uB62C8Uu5FxtP6EM3yTYj805it_LJZM-BBU2IGV_xlASohq3YLaMouLrpXlq4FtHiw97YPKktgC_kN5p2NOltNH62ffMmoGfdHTK4ISX_vAd0Kfe6QcXpqMmstJ5pXI4LRBg_Jxu9qhLbRR6MenRjkUEj8p4K7e3tUIDy73L7ZcW6eOrH_r_hmBpUgANFCbiO-dcOY_CuyWzvk9QIU9TO2DfIrggBBt5vWDe1aHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sDHceAws_DgHKJfPyxY_hbQFOKydTvRD8S_cgOocirT6Wx-ywl0KRXHQf6OhMNN3zocsp_m-f-qXQ5LsVUrIyAVJFqfaNc5rw6pss_ec7QVWAkSntWb2KwTWP8YwjbBOOMihz8GGAkNdJ8ch25z8QrdZado7tnLzBnW5Qe5efpv584P6L5_V7miT_QLG-SBABYenMKGWGB1YzjZ8woeN7pf2VImgkxl39Tm3qZ9YAEcN39WQJMSSSDCbPBI85r5LMCrbsCFz60xSY9D4pxmoZcKLUvjGJq3yRKS9pgyas2mT1tB2gou46k1MEs9KDv2QarRE2KF4-LjKR8PvP9KJuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JQTm-GORMQsHyoQA2Jfe9odBDfnVbM5wg4V5gYjcyBNcP5-N-mcPzn6CoE9Wb0cNKNhboYrr5VmCWpbBjgOua9Da7F7pXnc9pWvx_vqb95Pfy8J98qtAB8y40-DEhbThH_fxPQLv2PYX4I9L13zNe27kGLwMlHl-GrBtyRKIA5R91UYA6PSdBGFbhCoCpBOhNRMWNP6cblMKBmYyAMdgwixCp0ghnR92N84suRuHUGRzNK65D8nvMayKqteTQavqfCoYy5TsGTJYAM7_EJxKtZl9BRA_QIDnyWNICKImpt4obdRBKdmm2EDSgv7fODc27_CpxORuOeWjHQR4hFgyyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH_5S45MxowlJZKryRExdDv_YoI313N6BP4WuFfM0_dDBGIXRA_HeUilF1mZm2gQ8rQH96MuD5E6jXvzeXMjnpGwE_-M4Iltpjbsq1UsaFO_Cu4OR1Dg6vmzrn54i8qwQ7OfySz9oCihr7EtQDUDdv5qqv5tF2FQpYCbNajhLzk_hjqyqQDxHyrnnX2aLccb4sKepy6T0SkU1pk3DUfwPSkJU0_nsz-2WlvZHZXGzGBaiuhmpc7r2ooU-BOBMpWX4Y8IWcuOEaQeJw-iG9txi7iz62R3a_9NZljFKOkBx9dYIm6fuYivQNhoikQzw_rNVRt4jtbU5Asb3xPqEWxpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3U5EmnoKRO-Svp973nFJKjWsDKS9i8bLvawoZusSYgziOzP_sORDAMz--hf5uRH4KqFH3xOUmFl9RkLynARztJ5i4F2iJitHbLETP-mKnO8BWc-Uj6xI1W6r3fUzV5Aotk_aTh_wFBdJtt0agsPuwHCnkmUL2yeZb_H-IVsh9fDhb1Bhg9DQDw448qnwrzME46zH0WyVymJzauGVm4_Fhv58YnKjM_xsYOMoqP_34k09LSNZzz7oa5t23TrmcvkW99UyyaoBsUN4ZgTElQkrlFkMao8aEcx3kHWFnESdBH7SwwLi7tEtcWl3gnwsPowI5zVMWAm401zwF0oRnGogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTJP27xBNrimaOCWsw4qW_w9uYd6tWpqsyeoEtiOw12zjG-SD9AN15C2TGtBvTIPb2jULukfaQOnftkTuo7EL0YnlCWWZaroF_pfypSWfeClgylsOeQe_U0QDc7xtfUHSKOkxBowsgoz16W1lKSr0VV14C8g3POTi011ACt-qxJLRqGaVwJUO3Wl8PbBDW_jL29N-jVk4LSf6SriQ0kLCGD3BK-YjLxz8lcn4iVkR-pRphwG7t1Goj-4StgC0oM1R3gC1x60EKrNxk5yCgarTMl2D6gyufWqq_hNp2NZVgb9sHPVfanAzSbg78AYdyaaQWNF9Z_OEpAE6zF5Fn28uQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=PVlvyB9aZJ33TMJikDrpvYdh3aNDqvUh-0B62nsSmPXMeLHujNPpSMPbQ5ACOCZS0BTCh2Yo33epa1cgzlXLy9s_H_Szgn5Henua9OF2R5UE6u5w5lL-T24f-LhiY70A1QmG16-xFhv8hgl6lEjDn5PAw28R_MM1oxWLgyvkIcTY0Vmdoo_kQVxHyJKyZs92KxKnAQgw0AHhzqSz_Wg4VqCNdZA70wd1CI5bY2DdM275S6bPXng8F5k0qk494KUSy-eT-5Vk69CdcWANAl8sQ76lqeDiqIpCGhRY7KGMQIpo7NW-QtmUxdZTdK2wX73KBvFGubaVNQL5Z_Vn9PC0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=PVlvyB9aZJ33TMJikDrpvYdh3aNDqvUh-0B62nsSmPXMeLHujNPpSMPbQ5ACOCZS0BTCh2Yo33epa1cgzlXLy9s_H_Szgn5Henua9OF2R5UE6u5w5lL-T24f-LhiY70A1QmG16-xFhv8hgl6lEjDn5PAw28R_MM1oxWLgyvkIcTY0Vmdoo_kQVxHyJKyZs92KxKnAQgw0AHhzqSz_Wg4VqCNdZA70wd1CI5bY2DdM275S6bPXng8F5k0qk494KUSy-eT-5Vk69CdcWANAl8sQ76lqeDiqIpCGhRY7KGMQIpo7NW-QtmUxdZTdK2wX73KBvFGubaVNQL5Z_Vn9PC0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2EN_Gr6gyoLhFX7ZxqOUxp553Xt5fOiZU3RRMNukeFT69xMN_W9KF2rHmx7pPIjcMBW1jsAQuU3MvLc_6J2WDvxSENezI59Xfez1i0-p1MPiX-97J8hwAv7dITmdqF8H3qybSB_AWRRf9-TEA25x4iA4I-3eGTVJB2-o08bcRJ8eCCx-AVTtiSZI69pYQW1UQNgfVlPxxIXucOWiAXfZ6dRVenvyRLr555V3KK0HnSVNXCahZ3Dn6foWZsV7VNaG-1Le15sVPVwT_hQ5Bhy7WeFHMzDO4_3zTRpKNmn_q9oAjvdAHQ2AE2bGcoqx74FpY-profSkxloLaKdL5Untw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ain_wfi9VNoS8Ucp3wWTUQHST_fsKyxBBHzo_cy1mFDmH1jM5x1S_5SS8yHycBMVFsXUlBqiO1EyZKPBJSlHKgAnmCeqPBYDPCMVWMk1AgioOvQpiFz8DUA9NPDv50Ewk9RKpR_uGdvCaD0o9GbJyuwW_h85FMq_r8zBl7dfuYdz4pSEENiZp5FwQLtzVK63ItEZsxCBJU6JVz8aFWKVbnmIve0v53B60AsYNHvwuTnKAZNOM7SmQLzUklsvWyp7btbdmYuQKaM8fzFCm-4yGAoClbVbMkaNwUJE3HuOXA-l-eDFISfWwEa3CpVbgV2spXllv8CT-9UyTuAAgjtzcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ain_wfi9VNoS8Ucp3wWTUQHST_fsKyxBBHzo_cy1mFDmH1jM5x1S_5SS8yHycBMVFsXUlBqiO1EyZKPBJSlHKgAnmCeqPBYDPCMVWMk1AgioOvQpiFz8DUA9NPDv50Ewk9RKpR_uGdvCaD0o9GbJyuwW_h85FMq_r8zBl7dfuYdz4pSEENiZp5FwQLtzVK63ItEZsxCBJU6JVz8aFWKVbnmIve0v53B60AsYNHvwuTnKAZNOM7SmQLzUklsvWyp7btbdmYuQKaM8fzFCm-4yGAoClbVbMkaNwUJE3HuOXA-l-eDFISfWwEa3CpVbgV2spXllv8CT-9UyTuAAgjtzcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u33y44uykms5S2Jsp7l6EJJ7nJ4vlwvDhI0lyGfp3sDlmhn_vAc834uv4tvnT021rSUuVwSg91b9aPA0Myz5jIDPgrztq1Hk9G9R1TWKPB-naTf9GEkcFLqHJ-fwtE_3Pg85cmOzXuLIsLTIZxlw5vnxUNlDSF_vuJYGM5GexHDHd4YXf-v1u3mF8ECSwE_4WcGDlXU8pUeY7nkkLAqQuRAr4IWxqmfZb9s1Pksh8k1CA3RwqdRmKoDZ-WGijdPRzl78uNPD6SVMUsUYKIaWcwtPCc2FstDc7cZO7SrG8n1WtOsjuYQl6mOnvAme7Bu_WUL9REvGmHjwCz6fkWNf_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGDJyObpBUDoUZCTF1mHPOVhxdv4eERHRGjraFUn4jzQJEYZ1DY2_uK-YUNmMTT3UBZwGknE5lffYW5_lm0G65_3ZonjmU_gnBwWXKQUvYrf4oj1PyoKkmKfHl-6_JVRmU5qobuq6o8tYl55fVx4aYdDrtcu4PxcmGfYXmsY3S2X87miKCfLyQ8z8FP85sVwmtBZvWoKe44XWbPlf4bvsRqCNIb51MhUBoAlX7ekvkjOBIrDb8n798Z7aWv9AMWJPbclfkwVzzC0xUO2hX5AyTlKWQOYv0S5rtPT2SWiIPkNAOyd9MQ-nzEmA4-j9qaPRw_e8-jG_b-8LcubE8cYWkFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGDJyObpBUDoUZCTF1mHPOVhxdv4eERHRGjraFUn4jzQJEYZ1DY2_uK-YUNmMTT3UBZwGknE5lffYW5_lm0G65_3ZonjmU_gnBwWXKQUvYrf4oj1PyoKkmKfHl-6_JVRmU5qobuq6o8tYl55fVx4aYdDrtcu4PxcmGfYXmsY3S2X87miKCfLyQ8z8FP85sVwmtBZvWoKe44XWbPlf4bvsRqCNIb51MhUBoAlX7ekvkjOBIrDb8n798Z7aWv9AMWJPbclfkwVzzC0xUO2hX5AyTlKWQOYv0S5rtPT2SWiIPkNAOyd9MQ-nzEmA4-j9qaPRw_e8-jG_b-8LcubE8cYWkFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vh60qPehoe6Q0d4IqFjlOS5WWK_kG9Cy3O7hn0PkXyE9uYxztZu3MPQgFYt0yEpuDcEhjY8yD3auafMqyhIYVMuXBBTQAF_SWN7bdvvFyXCxz4M3ll78fwyw1VgkPmgAdIaMvKSOI7VxrnOjjdzZs1_FtWUIedQmtbc8jp5fTIPtbS5k90ZSNF3Z2zeHrTXD8ZTeu1lZ9NQ_sFMrKVvDS47RxeINHFIX3DmXvrPYQkROYGgVphPzV4CHsYTbJJWrIcRS7olCUa-YHZ3p6pHdz3S11_B3RQ9tLOGxp0Gg_VOEW-f8xkgdaCPQr1VYhVTS55SrFFAJ5v93EXIg9GsEQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=vh60qPehoe6Q0d4IqFjlOS5WWK_kG9Cy3O7hn0PkXyE9uYxztZu3MPQgFYt0yEpuDcEhjY8yD3auafMqyhIYVMuXBBTQAF_SWN7bdvvFyXCxz4M3ll78fwyw1VgkPmgAdIaMvKSOI7VxrnOjjdzZs1_FtWUIedQmtbc8jp5fTIPtbS5k90ZSNF3Z2zeHrTXD8ZTeu1lZ9NQ_sFMrKVvDS47RxeINHFIX3DmXvrPYQkROYGgVphPzV4CHsYTbJJWrIcRS7olCUa-YHZ3p6pHdz3S11_B3RQ9tLOGxp0Gg_VOEW-f8xkgdaCPQr1VYhVTS55SrFFAJ5v93EXIg9GsEQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BYJtS5K_2VwG8UgLDRkNaiiqgKnKTQFrR_4VCIJtAYGaCqg7Ah5hJ06pBTODr_ZajbfangJ1ljvlKdpcuPwX961bG1QGfVRzAOr84aPAwFFXL9Sh2KN97J6WqO5bJ-vBeTROJqgFIYjUMprOE4p-hedAfm-OEKpQwF4JSsJVZiPkE9kHkJp_vhF0_2qpX39QVPpnkjJ7aW9_7t_3ot4-FY9tnEGve-_hYafp5GEtn67AY20bNfBxLWdLii65nlBsrOssgYMo9h7pHjqWBacdSYh_NvNgUuHzxgHnI7SaWofCrfFAoHMLvWu3J7Nl-ooMOgx4ffqLSZlZ0cp79be410k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BYJtS5K_2VwG8UgLDRkNaiiqgKnKTQFrR_4VCIJtAYGaCqg7Ah5hJ06pBTODr_ZajbfangJ1ljvlKdpcuPwX961bG1QGfVRzAOr84aPAwFFXL9Sh2KN97J6WqO5bJ-vBeTROJqgFIYjUMprOE4p-hedAfm-OEKpQwF4JSsJVZiPkE9kHkJp_vhF0_2qpX39QVPpnkjJ7aW9_7t_3ot4-FY9tnEGve-_hYafp5GEtn67AY20bNfBxLWdLii65nlBsrOssgYMo9h7pHjqWBacdSYh_NvNgUuHzxgHnI7SaWofCrfFAoHMLvWu3J7Nl-ooMOgx4ffqLSZlZ0cp79be410k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu68rX0ar56yw2JxyUEaCoq_8q_yBmJDsrdfQpcyr2lSPKYy-pTHpyGdJPiKYiDJNMoONUcKRRfoeoa6aDvwlweMB5uGF2ojrGnKVdsCfPTmdbxSB5hjbsnH4-OmrTi7uS0WD10COlHese9wURIaY06dhkq17HrcDAYTTixx5g1RjXbMw8Ha8wK2UMVfaNBwy5x3VLZxpFrowXLsuCdDyRBZMFDVsUOwRU9OiS_EeUYvTjDUFwFy2IJhv2a_2kaULCdEIaDjKDlS-aEUhKl8V0hSaZZJ6hWOzj8km7LaXCLoSIlryva23ZvjHfEO8-emCl0HIbg_61aeLywicKDtpg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKBcnmijBmvwq8dbjS1SvtWagCOKOfMQKuVrDs68l8yBnmAVvnJGpejqzrh4-4PuqLVanjafFfvc4Jj2l-OJ3eaA0iAyXWHml87mnf2aOTIFksIl_ph-scPEapz51Vo9JdPfMNh4f_S2ye1HmWD3JimqRMPWPX--McvJ10QYTgQKaEcBxQzArVUJu8be2Fa9Q-RVA9lSH7tF3xGCGMqHvMCMzOVzTYwNdgXYwEEPV9GIwhdO1YGIGa5wfeT3ZLESApIocrgz8DDAthWhjOAeznSDVJfAvQE0dGq-BVHCuTmWZSz704ne7f808DCodjiQZ-xLi6PIVoIztY1LXiDxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDWDZzLcN6NCG7yvuIzy7tZlU9rfDbJliLg3YOT7AiLYBqRPgAZ9YOHIzCQAg53d3LceG4Qozjsmj-kearVRVW9Ye46S5QzbKzybFUurcPPHXBojF3UnfwFtStLl258SqgcCB_HjZqmVlbP-a-xo8MURNNS_iX6Cx8k_Uiw5fgCe4smTfCJVcXrySZJh6Vq-9F9X2kx0fqg7JKxc5gVW8gG2nAxH-D6T17IFwcfCkCxZLVm12FokwM02Mqj0xQ8XpK-6m1wPKUKHMUNzi2_kjLa1f6FyFnYaze3gukET-vwhaSv4f7lSnLY2fmlTOCmDNf4nAdrFkEDi8jI1-OrzdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJFtCkMtHGiVGYNn7xEDIzHQBdfYaw8NRtxsxrVKD_oJwIs6UFlT_gW1xFFgSVkZIG8RG3Tdp2m4VgYH8ccKR6gXJpPR-c8oLALh0SBLj9BJNRrin01D5oc4qKKSpG4QlqS3k-bk6pCA2QOqZmJRqXIaZsVvcYAyLu60De3s1LR9FJJOpHfb2aucCv3dR8KuVw-v1SlDaGVXPnJtkSITNurxxpR-6n7p_DJTYp_hxkwq3E2qkiNCYVDupzQOoqdlkVC9lbw4BuR-8Zsd-Y0mnR5LYYILPoMUc3x2wShL5YcmYlh557_QXYcKcJf9FYUaaho4xT3DrwlfNYpIKAGtFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mup8_8CH04ypLPMm2OM0x800YLmAdpdQATahDxe2PYYlORnh1V8UKNNNZ6NoO2Y1_WLFMMAmIIMBfsy0_PVnJ0r7xLX1t0zK9F4xaLjoPdeTHfp_V-F6n4l7SEbvQeEzD0fJ5yWuNuJAgXMVOZDBEmOE3Sh5tqDhy9RwZVHgzri3VcFmECZ3Q8EZaHqDLV88WirWSsAgcF7CPN3Ovk-wH2naPjirTGNb7S1w_Qe82lqfUMowd64lSeICdaoJUhXqT2VlByC-G-1U2xy05J0iZO-Bbgj7graqD9yehbUNIiSzC10Arfi8vInziyaYxIr82CxjeGFPS_VtbVXrhHKoBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozngCxiT2TfEOIFZJb-_wx4tG-MB98nJB1jupCimrepSmL79hqLvEutYN500PO5MF_-VkhaLSdHHAZm4vd8bmC4EStlBH6eJml4CtYs2L3_piB8JzayCXt0yGucYjgojO0K0UQWmJDffpYrW2TbO30Qx9kwV3h8_imgftYO7piPG-A8-Qagiq023edWFatuSNL8VDwG5068r2Spa41kTpo-FhzO4WyJVTfT4FSfrbfpvkg0xlqgaCiXwxwXDxaNqBez3egxr_n5hhKYF4SkDRTI7zvAHsgEC4vKZr4XqNQWWLIqhT_-_G2NmeYxu8YaWJfHh_4qbh-y3Ul5vXIvDoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lpi-eN-Tw9jrgPc5aHTBn6LQj6qOoXyEFZG1GPogqPQIHow34_GI9eKTheSkprhUUafrcnP05NJpwVigzYcaqyiZLWNVSJWY7Fp9FFreTn78pUQynN6yrZa1ZTDeywUUnA7ovL1uXy8gvcIaRmnAtrN_1Sv9_-j6gwT_khn-H0NV2D8R-WE3banQIJ3zTuIl3rf9gRWW_mR4VoKZ2pfTjL4kAm3_nxbU87pk7MvWvQ-aJGPRiNmgdFQ6iMz5K3nOSvJR10B_pKJUIBriAq75t1YPgR4U9QboF2TiHs71uvBT-xbbhLRwvNQ5fumexvCWpJVfAWHereTf2RfhOY4f7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkKwDETWQt4sx7Nsaj8wtxz13dlZH5dUr6TtIvB1b1JBds0GjyobEBTDu5cRhWadZ7uV2QvxrLS0LXwshBuBM9tE9WUToJ9HM6bhMQGAJWV-DSBvQ_ANAlQ2lWZX6KZlIJyxpKaBPTTHGTdBlQhDaknJnI0UhoJmtlVq7zgcMtZHjiUQh1J9IaH_a2G88awilR2uqyDEcxyP0pYioQqBGdOt-FmLI4fCaSDara7j0RNOY8ZoUGxSmuqq8uQiKzEaNq8hl-Fg0hXE82ImUK8kznvO-jJWVHatSAlpzzG55yA4nRlt1ArggXfHtFO3-eGyDfItpt4LtFQY_xBUuickWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiClTxXBsztK-D9nldHn_lA_vx0ChbVzpbNkHiIWLR1X8xqnIvRzWkiEQTQKDFxNvSgygraTY0WdrSSnR7v6KABvz2wJ04t6hfpjZ9TZ2-8toTdS1XKfYELl-WtAFyy8HXTAXUrAjld6br7OFLyPp8_hVCwNdi72Q_aBbXuV7u1M9mG3vcsuqe3k1nKgIrMyalyQQUok86Ye8hA0zs4sdgtQ18XzoaPyXfvPuWkJ268P5vjoRnp1iMpTieuvXYnyWu77cMXo-nZlbhjXvpXTaYqrsTqSunJ5X4__xDeacbm_ZqJ_cjiMO_kZYpKPB74WpIgLyze4h2dZmaQ5eyXj9Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IuB5rVTnRdWO36a1xn5psow5qes_zErORe0KGGNyLc13rx9Zvz-IUXFwe2kSN-N3LkmLw-mwOzW_XSswb6lx8_HBWrUkXtSCwMKc4GEU5pFzFswoqft4UdXBvV76oBi3aISN8X6rDwkCR9qseiVwIDixr4mIM0GPp6UFN1KDcb4LOKsVAyGgh3Tzr1KIatcvI0qnG7HZg2SdTWAq8psefAxWT5Eah7zYr-MZdpvDwFOBbiABgE0J0_nGHhbmHms3txUvFgFrVhwRk5j1sGus3_Q397tsQLE8GOjjBruGLhweU3gagdjMBGUNBFajIoCG61H_3jKwhdJo0x2utbirlA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wzy1lSUuvMJxBP7mztV5QGyAcRkP7c7NkUNDxBm755Pk7BMKNv8At7UfD09Pld2IsIyzPltHRZDo8wCvB0UL0_5V9bP_NFfkQWYvO9TRp0Hr3PSS1j__YOxfMVvZ3HAjH2bp-mvz-YWCx2LVSnw7b4xCrMgD6AA8h2kzYRs-TiPy4-Ha28bAp3M54__Ww0TMEYBHNuTxkXZWamm6E8-lr3TaNgOlw5GvCtWAFW0IOzVTCvRLrqnfQNKL3a14x840uUWZ3xqY5-UaoWpyIOy9OcEhrGVgaXtQa-DGvKMOFAQ9jB-3gyFgMvQCPIy_qQe1gGyHwXbZc729HO6s4Mwkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRax3mLvtGbUVOLfakGpEwUY-XxyGLBcjUcM5rpuB069Klx3PxlRPROxuAA7dX50CfxjQ4MUeXT3AihmY1ETuPDN6x9hyuOKTM21BXSnbtdRIkoRiv5HHrtD7-F67d7_j8sBLjJvs3yCuDg-wHDGNkW8cGs9gILheZi09Ey9rwg-W5G7AEcJCPAY7GapVrJ34Y7mZ45Ic8o3rTcStUo8HQXU_f7OqtyF5u6OPpzMhTmDkMyPK7ihYqqAOH8dmy53fi8t5fjPcUatQoatuQwsw60NnpB2RsKPDIQHvGCcx9bv-Hu3Z-AlNZRxbO7EEJW3qn5-A_8JyMdbX_tvPXZP7Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMCWzbjfOk6mnP24dc3imXNk5zO3f3YfdgxqLLedPMXwl5FRgXpPj1Drv4NMtGz2Ho02_u_JDx_scUCNihkU8M5Zk-cwjNy7MIYzxVnb5kuOifNDPilAKtigUA7LGxhrHcbjR0JhDsrQHGuOezbw5aap_ciF4dbzot32MCTijhAae_E-XGKt7dwzvqwZaCJwCTXcaSbSh0EWGciH9ggrWhF-9JmH_N-5lvo4LV7DVswXTv-X_92DFYCXDL7Uw3kokBMhDmigjPDV6vgLwNvDhzmqqgd7IzSpy_hyPMoyByTIIUfPpOymcGjLo81lshfoR-_KD7KuOPldo-lAyLBp9LSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMCWzbjfOk6mnP24dc3imXNk5zO3f3YfdgxqLLedPMXwl5FRgXpPj1Drv4NMtGz2Ho02_u_JDx_scUCNihkU8M5Zk-cwjNy7MIYzxVnb5kuOifNDPilAKtigUA7LGxhrHcbjR0JhDsrQHGuOezbw5aap_ciF4dbzot32MCTijhAae_E-XGKt7dwzvqwZaCJwCTXcaSbSh0EWGciH9ggrWhF-9JmH_N-5lvo4LV7DVswXTv-X_92DFYCXDL7Uw3kokBMhDmigjPDV6vgLwNvDhzmqqgd7IzSpy_hyPMoyByTIIUfPpOymcGjLo81lshfoR-_KD7KuOPldo-lAyLBp9LSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=EStspqkadRBNDNh9QMlNe8Tq2DM8NxqCTmel9tfvkvTXygVKKSnYgTsMXK2nNWmCMSiqWZYC4PvbWbhAQKOcHG60Yu3XbPB75DciSyQVWEM5_NQ78F2d3narIgnDMYI2TDv0HkMRtoJYYfW6wnRLW_X4ugVD3h3nfzzEWBVKOlWau1REH1DwoIR8E6LiQmaTbq5SlFWQDs9vwrWRrYcYLLCwST5Q1ZidwMpS7SlfSLzEebfBrHgyh_3ZZvQfFPVC9ZBf3f9N2CHoelNghteu9MItCUr6nadBzvR4T8EvMf8dwuFV6v8K2wtoJuM8cjPfAeLRCNxj2Sw_1F2nokz3dKQQ1bCAWhmm5lYBVAkMYw4DmHPCibaV5f91-kRfoaPGZcqK9asUawEGvmW23M7-twiV3CkrdG9z8fa41B7ZCMNHH7j6KvpgcYBwMb0WGHJzLPB2ggDvYAGYRh_wke790uWr2MNz5g7kzM9E4PvYjPYhh8-Cubmn6NlyZj2aG8lU4U3Y4bYq7Vpb0DtDN7-Gx75kMyHux1jbftsuNSZHngl1RVRyBYbnxKpA__kJwxbiRJSUY8PB3EFmnJXTFmbhYUNK8FZfYE8JTE8b_JHANtGKAmw2btC-0wKW9C9_j790zQAJ3HyH67NxemVezmFFMc3H0etIKkIbZPyoeHwNKBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=EStspqkadRBNDNh9QMlNe8Tq2DM8NxqCTmel9tfvkvTXygVKKSnYgTsMXK2nNWmCMSiqWZYC4PvbWbhAQKOcHG60Yu3XbPB75DciSyQVWEM5_NQ78F2d3narIgnDMYI2TDv0HkMRtoJYYfW6wnRLW_X4ugVD3h3nfzzEWBVKOlWau1REH1DwoIR8E6LiQmaTbq5SlFWQDs9vwrWRrYcYLLCwST5Q1ZidwMpS7SlfSLzEebfBrHgyh_3ZZvQfFPVC9ZBf3f9N2CHoelNghteu9MItCUr6nadBzvR4T8EvMf8dwuFV6v8K2wtoJuM8cjPfAeLRCNxj2Sw_1F2nokz3dKQQ1bCAWhmm5lYBVAkMYw4DmHPCibaV5f91-kRfoaPGZcqK9asUawEGvmW23M7-twiV3CkrdG9z8fa41B7ZCMNHH7j6KvpgcYBwMb0WGHJzLPB2ggDvYAGYRh_wke790uWr2MNz5g7kzM9E4PvYjPYhh8-Cubmn6NlyZj2aG8lU4U3Y4bYq7Vpb0DtDN7-Gx75kMyHux1jbftsuNSZHngl1RVRyBYbnxKpA__kJwxbiRJSUY8PB3EFmnJXTFmbhYUNK8FZfYE8JTE8b_JHANtGKAmw2btC-0wKW9C9_j790zQAJ3HyH67NxemVezmFFMc3H0etIKkIbZPyoeHwNKBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mn8NLH8SLCghWpWFMwrEF7nLz1vd-ADe3DFqrinoDss7a5opqt3CtHODn9emdLc6nXs8JcuZ0YtsLQeKZyzDsfcJf7h3dg0Q2yOhNW-zKFsZuVvHjPiG8clqcB8pXCUu5PiJYqDbu7VMx_-0SO3b1Q0pTpg4i2Ec2dCEmj-DHxl73_PCkTTy9Dz93s9y4svNBt0iz9ykXNpEPcE-y4ElJoJJ6SclEskYZAzEM-RjKT_Pt6XS9QeSnKnrKcQGvay5G0kEt5m4JNLa_y-437a8VCMVugsvuIwYr0YGk3wc3f2yqODK2YW04D0RjOSQgx0ec7rVGuvTnj2U63Lv-Ek_tA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=U_uVCYDjm-4lm2sbEeiOtzJV_Mcu79hf_94ZF3K-QOev9DW6sNGiyLgj_yJlMngZW2luyzrMCuDVSIRovOuTN5S0g3owC_9qkqUmJfYNVDa5vSu6UEG3rH1f2AgOsx3jAhYRWN7yha-SuXbSJ_IDYHJ9YeM25q2k4mgwLNAkh8Q795MiTPA_j-7cb9TCvCcofm_578Ywpjx4B2czxVufLZUNxbIcbfthfOoNuER5XPeGQgnCoxqPNzNvCRz-qGnSrMSbxpc-dPgcyIsBCMQ5-zFBg0xV-LZQA5yFFToRTY0wZnKtudw6TjfgPkvsYPvvdgJ1hYsUqAlaseybZxiBoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=U_uVCYDjm-4lm2sbEeiOtzJV_Mcu79hf_94ZF3K-QOev9DW6sNGiyLgj_yJlMngZW2luyzrMCuDVSIRovOuTN5S0g3owC_9qkqUmJfYNVDa5vSu6UEG3rH1f2AgOsx3jAhYRWN7yha-SuXbSJ_IDYHJ9YeM25q2k4mgwLNAkh8Q795MiTPA_j-7cb9TCvCcofm_578Ywpjx4B2czxVufLZUNxbIcbfthfOoNuER5XPeGQgnCoxqPNzNvCRz-qGnSrMSbxpc-dPgcyIsBCMQ5-zFBg0xV-LZQA5yFFToRTY0wZnKtudw6TjfgPkvsYPvvdgJ1hYsUqAlaseybZxiBoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=O0ul4w398Jn54AI-dDcia0ON4A2moNIj3P4UaKxLhJQ1Ca9Qyd8w5UTK6bGQrk_uPfHBWQTl7B7kzgx2hfsNtLqC8gGhmUFLeP8t6J_KucP2OvJoOBlYkcQD6EBrZHfI94jXNCpj8BMbthdqVPwLJ-Yg2JAJ77qYuEXTgusW4qQ7S3CxoiVRXH9zb49vMxICIjzacYzO_yz9vvBFK-wwD-jRaZt3DGa_n6oaeSQeYSPlfuNVmctH-eRm1Lyzhf7Q7fpKxfbuZ94Onadk2VW49IMH2GGZLt258Xxo6dHLY4XgeswDy3pUE_WXIyuDkfpRb_M3DQjnkdVdRmvkQ6h46g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=O0ul4w398Jn54AI-dDcia0ON4A2moNIj3P4UaKxLhJQ1Ca9Qyd8w5UTK6bGQrk_uPfHBWQTl7B7kzgx2hfsNtLqC8gGhmUFLeP8t6J_KucP2OvJoOBlYkcQD6EBrZHfI94jXNCpj8BMbthdqVPwLJ-Yg2JAJ77qYuEXTgusW4qQ7S3CxoiVRXH9zb49vMxICIjzacYzO_yz9vvBFK-wwD-jRaZt3DGa_n6oaeSQeYSPlfuNVmctH-eRm1Lyzhf7Q7fpKxfbuZ94Onadk2VW49IMH2GGZLt258Xxo6dHLY4XgeswDy3pUE_WXIyuDkfpRb_M3DQjnkdVdRmvkQ6h46g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRNhSTLbQubYAkQKFTIwcRwRObYmiGFfg3Ma1WRe4uv5kiLfJOyVw3guDHShV3KbUYmkrp-3pi8RM4DTQuWi8NX7gwy-fINdO5Juuu4CaIb8D_jmB_j2y5ReqsmkWCw6HJs4zUkMf6naZesbCLsK0FSWa4qewdFtZDnYhFIGexo_n98k51mtV9xcJ6c4PZk8TYwiexDEpZM0NsFtPtRmtdH7Tg8ulBtkEQA44nb2fZhYM2qkvdEOCS2ZdPYnuBXQ6dFdBthjTwIIWpliQbOnj7IdlbxdhpjJnODREGMEUjAqJxaw1gXQACHuo6xKHyz34hkV1m8DqkXWNTga-zxjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uTaKaNx-KBizhkuR0fznfOLY-Kv4b1T8mi5uPT4924ZF60KkolIdwW_1-M3cnwVZxMLz_mqnXbqHa8-uTwfG0LnRNh5-ZgntxMWtt84G_rz1y4kCvTw6FWMr0yrHvJDMFpkUDOf6HLYwLTmAB65hIw3xe8BUy5A31pjxljAgEwW-H_QUR2B9Xv1ea6_HGeJSbSn2tWfn81ErZCm2DtGUJfshifYHTUtbT61Q_2yxWLqQr-tTL6wkPh_TlqXrLM9BmYCeZLLrYCUyTH3WRb5dHM6z0RsclOx-H1PQG84lUkS4jykwMTJDDbNPECefXdKbjpYEh0oL-J94FoQMgUcKZQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=f9Pg5x4CEyVT1guVjWcQhP_MDg4xioTsg0m8X_ur5wPiEYBmr0pYNAzoxMwQBpqOrMwzN09JCFfspbJzBjHDAJLHrs3lona4oOLD4pT2eJU15BURucObdfXX-iq1cCrb04ab3cT8uyOb3fqMITVClvBH6fOiiqV11OJuxZ9XIakXXJ14sHBGkLyXxUno-cfj5CmWwI8GeIGFQLEZbcbQ8BhYSAnk5A7xp8lvpFxxQ5FiGLHAMeI2k_-OoAeldMj9H5GKvi4PMIlSQUpexKbAyWp6C3Nvn7sTY3cxmJ0DDDKBzUZHugn4zUIP0EsDnMjNvdBKzvWFPdbMGk6kDGICAC1qEJNv3_QYh1-jKwDdLhDSIVFt9sCzUO5XVOxDP_q9KX3jyhqczpqr5mJOJ7XaM7yHHDGjxBPcRflHBMeMrxrDzUMMciXyjxL1nbBlhnn_MjqlM44Uwgqvog9eBY6BrIoHczpM2N9ewMITVrl52KZVL30s91RsQ9oM8D2mJPA_rnbHTyx3LVDnr6f1zIqOzitNdUTrNgOF30jkVQhxmOyu5SllosYKiYjbqqPk9Ath5JFw-_e46XqkTpnAYxhzDs8yTFIPYGClpcMavSSvD0ebdLXT9axmw6NJ39o04AiBZOMCF9q9G4eCbpLY_m_t-g_HyN4gMu1AT7jK5LzlGuY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=f9Pg5x4CEyVT1guVjWcQhP_MDg4xioTsg0m8X_ur5wPiEYBmr0pYNAzoxMwQBpqOrMwzN09JCFfspbJzBjHDAJLHrs3lona4oOLD4pT2eJU15BURucObdfXX-iq1cCrb04ab3cT8uyOb3fqMITVClvBH6fOiiqV11OJuxZ9XIakXXJ14sHBGkLyXxUno-cfj5CmWwI8GeIGFQLEZbcbQ8BhYSAnk5A7xp8lvpFxxQ5FiGLHAMeI2k_-OoAeldMj9H5GKvi4PMIlSQUpexKbAyWp6C3Nvn7sTY3cxmJ0DDDKBzUZHugn4zUIP0EsDnMjNvdBKzvWFPdbMGk6kDGICAC1qEJNv3_QYh1-jKwDdLhDSIVFt9sCzUO5XVOxDP_q9KX3jyhqczpqr5mJOJ7XaM7yHHDGjxBPcRflHBMeMrxrDzUMMciXyjxL1nbBlhnn_MjqlM44Uwgqvog9eBY6BrIoHczpM2N9ewMITVrl52KZVL30s91RsQ9oM8D2mJPA_rnbHTyx3LVDnr6f1zIqOzitNdUTrNgOF30jkVQhxmOyu5SllosYKiYjbqqPk9Ath5JFw-_e46XqkTpnAYxhzDs8yTFIPYGClpcMavSSvD0ebdLXT9axmw6NJ39o04AiBZOMCF9q9G4eCbpLY_m_t-g_HyN4gMu1AT7jK5LzlGuY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=OUsxEiFMOjEV22ne7F5ozq7nef9NqRt2XTy9vQZq-HuPKv5ID-frU5uOxMRDn2XG9VxOsodxjhfrXufSTrzfJ2WVI1nP-teNi_U0F9rVHayAQVW0RrQdQz_Wz6nN1LbKlJJKt2SVNzeABD2MerrBOYq4wLEuHVsTMU9ll5AmucsVHMSobBY-1evwkIYrfItcz9olw675cHwExI-AOcywwfIAiIAUXFgkW6PsyjeLBjNncqyfpfDbdSu5q5LT35uDGGLo62ru23faf_e61Wys2rplP5JaVsIWl-1K_QJGOZFhly0_0qkcvHKyvMHLBaZ4xRSc41S6ZND_ynUmc_qFZjmcBr3x7h0gFxZz2lyVAVPA1rMwD0S80pxO03gdOAfYNs_q1x82SS10DXAWNUjEE7aPyBajpHhG8BQKc9Q6RHtu0zK48S9zP66evgMjKEnXF2wD1niMQ4iC1HYwk4WB1evHijPUKMtaK3PBhXfmdF0a6yC5j7_j3wRkmNaId3ENBIDKtZGHXWO3fR7E4CeJJNeyFToKnBkwckDsR0YmukYF8k7TD60D2_K5DjCMZqox2rG5myXK9MvOmRq4qK3Jae8rZdryCaUqwE-sKpJfAn7zcFFet2Cq2ryas_I6HbEKTPJ7cOpNeIKoi7HEY-ckmVFshNR9ldDNcTmhCRWEFew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=OUsxEiFMOjEV22ne7F5ozq7nef9NqRt2XTy9vQZq-HuPKv5ID-frU5uOxMRDn2XG9VxOsodxjhfrXufSTrzfJ2WVI1nP-teNi_U0F9rVHayAQVW0RrQdQz_Wz6nN1LbKlJJKt2SVNzeABD2MerrBOYq4wLEuHVsTMU9ll5AmucsVHMSobBY-1evwkIYrfItcz9olw675cHwExI-AOcywwfIAiIAUXFgkW6PsyjeLBjNncqyfpfDbdSu5q5LT35uDGGLo62ru23faf_e61Wys2rplP5JaVsIWl-1K_QJGOZFhly0_0qkcvHKyvMHLBaZ4xRSc41S6ZND_ynUmc_qFZjmcBr3x7h0gFxZz2lyVAVPA1rMwD0S80pxO03gdOAfYNs_q1x82SS10DXAWNUjEE7aPyBajpHhG8BQKc9Q6RHtu0zK48S9zP66evgMjKEnXF2wD1niMQ4iC1HYwk4WB1evHijPUKMtaK3PBhXfmdF0a6yC5j7_j3wRkmNaId3ENBIDKtZGHXWO3fR7E4CeJJNeyFToKnBkwckDsR0YmukYF8k7TD60D2_K5DjCMZqox2rG5myXK9MvOmRq4qK3Jae8rZdryCaUqwE-sKpJfAn7zcFFet2Cq2ryas_I6HbEKTPJ7cOpNeIKoi7HEY-ckmVFshNR9ldDNcTmhCRWEFew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=EzIO_YnEixyEPimiBUjh9vZasEF7U2fgnWpjMC4x0gi6c7YHAl98E_9DJG3niHhKOw4bTtls08_GCbQ-JwdwXY8Hj3G6ZDBF6S22M9ERL861uWsXEv9yB6VMAp79pvhVw8meHSBeUZwe5b8Xl1v4MNQKonuM3qU4q9RnEtYo5Dd-N5pRv71WJN1u7aCj9CPZNiFYkLsqWSd1LC1it-kU229jntrRQKNc1hI0hc7iVgAYueL_Wu9lO2m3Xefma7kFHOjGC1vL5_A5ErHhYVGWtD2niypTP3b9whXWsnHwEpT-gstRHlZCyJTRuYRDUTuSwZfFKjqOAz4WNbb0vJGZbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=EzIO_YnEixyEPimiBUjh9vZasEF7U2fgnWpjMC4x0gi6c7YHAl98E_9DJG3niHhKOw4bTtls08_GCbQ-JwdwXY8Hj3G6ZDBF6S22M9ERL861uWsXEv9yB6VMAp79pvhVw8meHSBeUZwe5b8Xl1v4MNQKonuM3qU4q9RnEtYo5Dd-N5pRv71WJN1u7aCj9CPZNiFYkLsqWSd1LC1it-kU229jntrRQKNc1hI0hc7iVgAYueL_Wu9lO2m3Xefma7kFHOjGC1vL5_A5ErHhYVGWtD2niypTP3b9whXWsnHwEpT-gstRHlZCyJTRuYRDUTuSwZfFKjqOAz4WNbb0vJGZbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hem8AxES8MGDPA3olJtDkMo-lbj9bb8U9hynu9VqpBePd0ngFjMp1bw7gRGTksPXQp9-pumnDyOiMpZ9wpQKi968zelwl4PCkSCLamblJUyy4y4KukWpoQytRXo3cS8MNpF5X6eennGtfQ5R8VH0WazIZGOt8tgsstzV_7GXNeHJIVK93V3DgRveAsl_EuRlwev1uhKlQnAyuwD-ljDUfRv3fqc1dK67j-tuxfBG__W1d8pMCuDfkBIHaXZZUFdcDg_IfW4TjfhLsTqLjtm1awJ9-WXv_wf4d0qnNJ5dPLzHNPMawOHZ4bvfJIPP_1sI6kT2Ui9kDgYT93k2rL5QFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=SryHP01pRb2D1tON29Q-Wcj_CaxX79JiN-FRhGRFMwhRcm6CPYdF0tNN9J7s--2j3TPvP2zSmLf958yAG-ep4gv3VqNuJT-c5vIijrC30JcNgJUnauv-x7101NJQ6DYKidOYSFKDn65aX5EjljWYRSH9soZVizO0tYA8N-lSya1xq9QnJXJOMIx5e-Dy62L7cMMehagCXdGGASV_0q2TOReSatDcVK4Br9dBPdY7ltR-JUMYkBOBASNXRst5c4TDoXXlb9_PYsQ6mQbd6h8PVgNgr1B630Ux8nt0bjDdOMqzfJCCPOctuEP6Jh4tO7oydKlLZtiGYVe1yvtm5R1TVAaT8V1oGtrQJTjBbj_v8TYF9RNy0Vs6vzdACujZxD7xxpIbcuyXz2mtnm4_KD2utT9pAlzPOJZxt5s92-f4VRP2AL0gPbwfP9FnJ48NRqeC9T4GTPHr4wPf0nSKEDrgjd9ud7H-SSAX6NWG7ZUNgVyc4SsRGgukRF-z3pA9j9XvC6NjRv1oWuPMeOIEpJt5RzpRu_4N6tkjfqiMhR9ldUN8J4hiSRhBEY4C1YPI6Ac6tV6i5RsSOf09bPpd2YsX7GnQaElcLvhJgVKL0hGuiNrHn-uSzGZepTJail23JjBG7mA-LqDkuY3Ax0tWD01relfSQf3nvURV8JtIXVTK2Wk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=SryHP01pRb2D1tON29Q-Wcj_CaxX79JiN-FRhGRFMwhRcm6CPYdF0tNN9J7s--2j3TPvP2zSmLf958yAG-ep4gv3VqNuJT-c5vIijrC30JcNgJUnauv-x7101NJQ6DYKidOYSFKDn65aX5EjljWYRSH9soZVizO0tYA8N-lSya1xq9QnJXJOMIx5e-Dy62L7cMMehagCXdGGASV_0q2TOReSatDcVK4Br9dBPdY7ltR-JUMYkBOBASNXRst5c4TDoXXlb9_PYsQ6mQbd6h8PVgNgr1B630Ux8nt0bjDdOMqzfJCCPOctuEP6Jh4tO7oydKlLZtiGYVe1yvtm5R1TVAaT8V1oGtrQJTjBbj_v8TYF9RNy0Vs6vzdACujZxD7xxpIbcuyXz2mtnm4_KD2utT9pAlzPOJZxt5s92-f4VRP2AL0gPbwfP9FnJ48NRqeC9T4GTPHr4wPf0nSKEDrgjd9ud7H-SSAX6NWG7ZUNgVyc4SsRGgukRF-z3pA9j9XvC6NjRv1oWuPMeOIEpJt5RzpRu_4N6tkjfqiMhR9ldUN8J4hiSRhBEY4C1YPI6Ac6tV6i5RsSOf09bPpd2YsX7GnQaElcLvhJgVKL0hGuiNrHn-uSzGZepTJail23JjBG7mA-LqDkuY3Ax0tWD01relfSQf3nvURV8JtIXVTK2Wk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=rYlV1hStXb3IFBbbreIhZdUQxyVFN698AGc7EtvgPQgkcIVS0XIf2TSmRkzFeDG9MqqFW2gzyxec3ksn_UIdQHHzhq8RTTnQf44gPhWfU-F5XiGS9DU2HZFSgRG7wi1bpXYrx9kY5aXTo1iXYO06rlF70rtIFtoml1Hp3_IQTL39QmpxYxHtXSbFg3euJNjYkUKSttUNJeKa0-tH7gEKl5nj9t2NUWxeNnlm8JaEvA1pOYl_oay_DvPPBPfpu89TVvEUCLwq62cGbFjoCCxGLY2a7ny09oSU0G23OUZrOgLeJ2pqzghSiXp-Jv5nVdl7ea1T3MLzgru1NLtOw1b28g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=rYlV1hStXb3IFBbbreIhZdUQxyVFN698AGc7EtvgPQgkcIVS0XIf2TSmRkzFeDG9MqqFW2gzyxec3ksn_UIdQHHzhq8RTTnQf44gPhWfU-F5XiGS9DU2HZFSgRG7wi1bpXYrx9kY5aXTo1iXYO06rlF70rtIFtoml1Hp3_IQTL39QmpxYxHtXSbFg3euJNjYkUKSttUNJeKa0-tH7gEKl5nj9t2NUWxeNnlm8JaEvA1pOYl_oay_DvPPBPfpu89TVvEUCLwq62cGbFjoCCxGLY2a7ny09oSU0G23OUZrOgLeJ2pqzghSiXp-Jv5nVdl7ea1T3MLzgru1NLtOw1b28g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptny9kZ0EnlOOvR8Du5itCGRe3pCBMEu6qpALB2OHXTNMm-GFlK7k7wtDZbj05dZo6ABmR8NcgF35jiBr1_3ofL5_wPX7W-l68wOuYVdrDLh9izUM91GgqwtnBZOS17jeI1mMMqwCD2UJ2jLZqJWhFNW-x4AQt0ZSwhVCmOdBqzuRgV1I5JqkFA-4CrjoB6AirPjyIlX2xdVsZzZeKTgsBr_xZkd_C4neX9s-dfuX5ltnQmhf21hAsV3iua1wgIh9S-Xj9aRjBrScj33HP9Ju4fqoPpHaJ3-YK3JCcd4yyxVWCoeMjUN9NL_vYhH-qDiUPjzBKyA5O_VfG9Gszxe_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ایستگاه مترو در تهران با مجسمه مریم و عیسی درست کردن (که عجیب هم نیست،
نصف قرآن داستان‌های مریم و عیسی
و قوم یهوده) و پروپاگاندایی راه انداختن
که ما چقدر احترام میگذاریم به بقیه مذاهب.
بعد همزمان کلیساها رو مصادره میکنن
و صدها نفر به جرم مسیحی بودن
توی زندانهای ج‌ا هستن و اجازه داشتن
یک مسجد به سنی‌ها رو هم نمیدن!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6188" target="_blank">📅 18:54 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6187">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWcbXSpyUSeqEhB6ZEH6qOLkJ1vCdVCMxuW_xKdjnqPv074tQCV2EfoboPddg5vEgM6e-NCN6yP3E5gI_aDx4KSTw0ZRzHzBF8iTO9LtbL2Kq0LsuvmylNibuduDNcrO92os6lDIx0kkVwSyWFEXF2lJvaCTi25MuIujj8LUHQqnHtxIdlmoxQwGULvD307BjiszYunKbQMqmQA4B8gwRAF82LQ4KVf2lEVeo4AIUPwXvM_vh976U6sT7c83shT6YpbVD3qO0aWRIveXXVcJKrw05WcDipx_n-zRtfv5iQMtfjwHwrbAlLjE7LYokov7-U-vAOT_KNWNu72YrTF-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pgmXh5MeTYiMth8dx11fhmCnrBppkfBz3kZova8EHW281zMdR5ZLt_GS0Tg1KJxS-9rPCdBw29-53pssfT9MEh0lr4BuwjAhBR-RP139M5PHJtcZLKcwHQzyF7e0MAeUVJKXSGK7sml23y-hCBzpyoVFNAvd1F6d8G_clTkoKQIThtHMgKQPFXVWCWKM53-ROmDIwBd3cWf9eIwydzN7rAsMEWUIsZfkHKh4j-1FoFRAcZ5njttIyA6MCuV5pYOdjtRtW8vOKd4a2ZFpSQW-w_md_hjRee4hfMe3vCpaXXfwjRHVbMiToAzc5xj4YQOVRFNoQBCwrj7uwMqal9iPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقل عرزشی !
من میگم اینها شکست‌های تاریخ
رو پیدا میکنن و به عنوان الگوی خودشون معرفی می‌کنید باور نمیکنید :)
تنگه احد! که نماد بزرگ‌ترین شکست و عقب نشینی مسلمانان در تاریخ صدر اسلامه،
رو شباهت سازی میکنن با تنگه هرمز
‌‌میگن همونطور که اونو در سیطره داشتیم
اینو در سیطره خواهیم داشت.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6186" target="_blank">📅 17:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6185">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JordQqj3woRlDrzMUnB9JGNoUAb4fz_SczWfOiTMEOLcrgyFr8H0nr_SM1k-0ga5NAZWOBBcvVayPI2XMO_G2QtSm_xcyf39N0c_EVVsUWld_bXnTu1H-fpDuEfNV9xvPQFWDJhNLuuIpUbUEhXj_IAVK-0KkalToAqJBvjAipCSNalP4wSk5GjSYS0VmgJME5SERGsGJyJukTcATmGgTtjM1W3N0xPYD7Of9NJVpVhULzLoaIE0N_m-r4Nlga3-ZTttpaDKYt9sV_Gii5vh2qzSEmPoDkWjh-_YihK807q6UQE4T9uOwVuLwCsaaUY9fCHMvfxegT6eSpOQHj06rYs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JordQqj3woRlDrzMUnB9JGNoUAb4fz_SczWfOiTMEOLcrgyFr8H0nr_SM1k-0ga5NAZWOBBcvVayPI2XMO_G2QtSm_xcyf39N0c_EVVsUWld_bXnTu1H-fpDuEfNV9xvPQFWDJhNLuuIpUbUEhXj_IAVK-0KkalToAqJBvjAipCSNalP4wSk5GjSYS0VmgJME5SERGsGJyJukTcATmGgTtjM1W3N0xPYD7Of9NJVpVhULzLoaIE0N_m-r4Nlga3-ZTttpaDKYt9sV_Gii5vh2qzSEmPoDkWjh-_YihK807q6UQE4T9uOwVuLwCsaaUY9fCHMvfxegT6eSpOQHj06rYs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6184">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WewJGDY_y9vWNGFH326H33YqVZ_PecElQePrXy6dA-qmdAJV9q8KPNo3JgGW80vhX7pJifgoy2a6K1uyapslD0RK02WQOyT18Vhuzm2Mm61rmbfbFsV6hs23eLAWaH1ZKpN840ivxj1zS32l1W2hF-UKpGZP-Ty_SbsPpkO1cRLMWnFrRsfVhG8HthvJt-E7ZcQLuoM2Bh3b0zVxd-BEo87AZ7Fm64XXvlQcLuCk3HnhpKonRmfcItobz6Com1CyRYH1NszXOJ2AEosXcWFrlDOYKodvX8053uPeNDfAhNqRtVrUWVF8c_1W7gujT2GhoPZXvwAgenXoXg4c4c7-Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی به تاسیسات آب‌شیرین  و تولید برق کویت حمله کرده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6184" target="_blank">📅 14:33 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6183">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NgVys5BTdugbjM0odnvW0gTEOYPNhedR1FQyvG0aZ-sV_MrAp20rLtUk3am8ghhWVe9t2FT56d9grXQ_mlF6Tf_u9LzDNqeo0lObNUJoFE1zNRoRXoiNNuWZGETsYteZhvGma0UrSZR6J6Eo2ZriS2XJLhb95h1oYRnQZAwXG-STcbMHN_9sUfpgQKGwH0XMumFjQhrCbJg7Lfe70vxVkJd1hYt_WNtYnoA40RAK82cdKBQGf5Hg5aRC_6GaSFUznlkMRd9axYDJViUEoYZpFZYnf2dsVK9sRhChldsE6F9GKAx0qUO7vFCj2z7ToU-5gCsZ3di3ilA4x87cxT8PVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61a69b588c.mp4?token=NgVys5BTdugbjM0odnvW0gTEOYPNhedR1FQyvG0aZ-sV_MrAp20rLtUk3am8ghhWVe9t2FT56d9grXQ_mlF6Tf_u9LzDNqeo0lObNUJoFE1zNRoRXoiNNuWZGETsYteZhvGma0UrSZR6J6Eo2ZriS2XJLhb95h1oYRnQZAwXG-STcbMHN_9sUfpgQKGwH0XMumFjQhrCbJg7Lfe70vxVkJd1hYt_WNtYnoA40RAK82cdKBQGf5Hg5aRC_6GaSFUznlkMRd9axYDJViUEoYZpFZYnf2dsVK9sRhChldsE6F9GKAx0qUO7vFCj2z7ToU-5gCsZ3di3ilA4x87cxT8PVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱- ما مخالفت کردیم، بعله، کاملا درسته!  ولی آیا شما به خاطر حرف ما دیگه لبنان رو رها کردید؟ نجنگیدید؟ پول و سلاح نفرستادید؟  به خاطرش حتی موشک به اسرائیل نزدید؟  (که اونهم اومد در پاسخ ماهشهر رو زد؟)  خب جنگیدید و شکست خوردید!!! هم در لبنان،  هم ‌در سوریه…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6183" target="_blank">📅 14:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6182">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/902cf63917.mp4?token=Cn7NEPKgSRSDwHiy44N1dKI-y7MjPcXyOL3FgX1tMTMX0fW2eIyNddv86DaZ0IW4FWUDF2ztv5Lcrl91HkDs8qL7tbbqU6g_QzGwNm8k8824neXHDbskxeOS5REiIFBtWG5yOWUEV10KoCv84x3mUDmvB1RzcKMNb_AY0nugRKSqtSfpbwwNL5R3uP_0Ki5ZCHpu63331_p2QA0N5tLZYJTvU4u4Otri0zY4pVhruA06QNrAjAruReNuj88GshvuInK1W0bDwGU6TQHZI6X1-Z5MbQ49OdoxcVn_ABosUhAjDpzBY29ygAa36mXu7Xdh_x4SWPSU-t5RNorR5HeqObJhA07htUF2DrTk2P9a7nl79TKxgkEraQLbQgI3y6Kwe_ha1Sw4SIAx3HsqX6VLoO2j2NsBdpoK1DT87O7XAw4SzaOJ2VKO4TjI5p1DPGmnwEWNhsp-vZXJXqPLNJfk5xApcTrkwSLYqdpPIip_Q596FZpTEbDr57htqokvwk64IATQtJnR6Cz9UgJyGf0Y9N_1194gLnywaUpNO4Z2hI8BuYbb0cG3EGADtruLECZAh0w68RyDBtVqXIVOixYTHvOps8GaF9iyeyoiYmKGXsTr4X8gIFj9AY4PldKHd2mjMXXLXEO6r4W21fTwFe87yGYfA2H8RI9V1zjEzwDqVsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/902cf63917.mp4?token=Cn7NEPKgSRSDwHiy44N1dKI-y7MjPcXyOL3FgX1tMTMX0fW2eIyNddv86DaZ0IW4FWUDF2ztv5Lcrl91HkDs8qL7tbbqU6g_QzGwNm8k8824neXHDbskxeOS5REiIFBtWG5yOWUEV10KoCv84x3mUDmvB1RzcKMNb_AY0nugRKSqtSfpbwwNL5R3uP_0Ki5ZCHpu63331_p2QA0N5tLZYJTvU4u4Otri0zY4pVhruA06QNrAjAruReNuj88GshvuInK1W0bDwGU6TQHZI6X1-Z5MbQ49OdoxcVn_ABosUhAjDpzBY29ygAa36mXu7Xdh_x4SWPSU-t5RNorR5HeqObJhA07htUF2DrTk2P9a7nl79TKxgkEraQLbQgI3y6Kwe_ha1Sw4SIAx3HsqX6VLoO2j2NsBdpoK1DT87O7XAw4SzaOJ2VKO4TjI5p1DPGmnwEWNhsp-vZXJXqPLNJfk5xApcTrkwSLYqdpPIip_Q596FZpTEbDr57htqokvwk64IATQtJnR6Cz9UgJyGf0Y9N_1194gLnywaUpNO4Z2hI8BuYbb0cG3EGADtruLECZAh0w68RyDBtVqXIVOixYTHvOps8GaF9iyeyoiYmKGXsTr4X8gIFj9AY4PldKHd2mjMXXLXEO6r4W21fTwFe87yGYfA2H8RI9V1zjEzwDqVsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=epnCNjSN_CY59eVLRgWTpa4SytbAjkfLyCe7_ygvegNUU0ilUY9mwuo3Y6RylEIPXuOGX0170ogHzwM88hLO0ybPYe56bv3ptio1gzEnKvk1DPInhrKddqOH2OyIXWrrpJUPFZ5xS4E_Yf5ToubYHTDIn6T2nZMOH5Zuh3blQ4r6HvCm98tzLDQfKtN8BoPTbDOTLllVPI3ComzJCRy1aGhS0Ib_TpC_HqTmdMBwdi8kVPkq47wLn5wUQQY-e3vK_pKww8VM6olVS8BivXnR7DfLT8oy-DpD81fNseSsgj0ClHUE2juMNJgFjaggcK8bIK80nWbfcglzkwYW7U4_fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c58aa42b.mp4?token=epnCNjSN_CY59eVLRgWTpa4SytbAjkfLyCe7_ygvegNUU0ilUY9mwuo3Y6RylEIPXuOGX0170ogHzwM88hLO0ybPYe56bv3ptio1gzEnKvk1DPInhrKddqOH2OyIXWrrpJUPFZ5xS4E_Yf5ToubYHTDIn6T2nZMOH5Zuh3blQ4r6HvCm98tzLDQfKtN8BoPTbDOTLllVPI3ComzJCRy1aGhS0Ib_TpC_HqTmdMBwdi8kVPkq47wLn5wUQQY-e3vK_pKww8VM6olVS8BivXnR7DfLT8oy-DpD81fNseSsgj0ClHUE2juMNJgFjaggcK8bIK80nWbfcglzkwYW7U4_fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6181" target="_blank">📅 13:52 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6180">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BijRRE6HbWNcpU3CjFNR91fyse4GaRtzA23CpkNtfGdGql7BqZ3tmSzxtftGRD_4nfQMHs81HqJ1uFa58tCRIflApGIRKPUjauKYf865U7wOYBW0P63yAvJWeyECdKv28Zlaa8TOyjAsjC120F56Qyd2Q2IdRjLJgqfDXFBwcrY6NLzC7LSiUXsiET0ih8cY3khBgnf-SS7lPIOjEU7DqtWu--Mk0Ftl3Au39f1VOY5ySKgKgKUc08xoCpDlOgrwTpV9SsnsCowl1sjqIVV96ulUqTHh8hR1DrR1L3VLRrTlEbQkIFyYCc3djAP1FOehJ12c_KzOvalLBCAMaM3CJQ.jpg" alt="photo" loading="lazy"/></div>
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
