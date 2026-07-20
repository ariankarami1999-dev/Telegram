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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 02:18:51</div>
<hr>

<div class="tg-post" id="msg-6287">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Y3Sq0ge5wkSXwnaCLRVbvLNob5qftXeARuCaX80EIfg0f9DSeu0eZVNrV1GZ0DTxD_qP6mK-4EIiuKnBPv49RP528AmVG6ZQ3cxjXI7FNCgkBc0pqN66wm5KItbp4QDnR_nVqEup3YBzKyQrLmZqWLuacYk5dZR8vSzfCyarIGwpxoIOBZPbiJmE4C6t2eC5Eg7ZrhZ9luUgOKhLzROVH0WzU_JA2SIJ62Jjtob65E4NGu451n8VQTZUhfzqmrRtHPfvVzfW-4m6183ztldQjsFYiu2bRBhVjNG8sJ9foV4GcXv_LWHsM1dF8eNb6JKzdtxgsxU9GwNzuK5izNWp5H9rBwTpYLLuwKMcIpE8rucgx-5o9i3KzABa9bl_p_r3IZdLS8mwJqkRkhEmXvHZO6ZKKDUs8XquKAXxIAjcf1DWVJJDoZjL-qW-qKUe7Oqd-OLWbbyPJSZJYzeuZJduCXeYFeujOZkli7wyURM14cae_E3TX_Udyc4UoQ1ZMMIR0gdZyvpiCpFAYMUvk5Ru2NYaJuWugGY92LA_8mg9n-4uvcNiRkQ2OhVzkaozFExZiI2l03VK5-4DlbD0xOPNo9eyt_OqyoOpJ_Hy3zX4nRjrIm4HF2CuFGoDk07hCj9J11_LYew-6fR_q4L43A3MQKez3hzaUORIUoD07r7ERlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75cc0ec8fd.mp4?token=Y3Sq0ge5wkSXwnaCLRVbvLNob5qftXeARuCaX80EIfg0f9DSeu0eZVNrV1GZ0DTxD_qP6mK-4EIiuKnBPv49RP528AmVG6ZQ3cxjXI7FNCgkBc0pqN66wm5KItbp4QDnR_nVqEup3YBzKyQrLmZqWLuacYk5dZR8vSzfCyarIGwpxoIOBZPbiJmE4C6t2eC5Eg7ZrhZ9luUgOKhLzROVH0WzU_JA2SIJ62Jjtob65E4NGu451n8VQTZUhfzqmrRtHPfvVzfW-4m6183ztldQjsFYiu2bRBhVjNG8sJ9foV4GcXv_LWHsM1dF8eNb6JKzdtxgsxU9GwNzuK5izNWp5H9rBwTpYLLuwKMcIpE8rucgx-5o9i3KzABa9bl_p_r3IZdLS8mwJqkRkhEmXvHZO6ZKKDUs8XquKAXxIAjcf1DWVJJDoZjL-qW-qKUe7Oqd-OLWbbyPJSZJYzeuZJduCXeYFeujOZkli7wyURM14cae_E3TX_Udyc4UoQ1ZMMIR0gdZyvpiCpFAYMUvk5Ru2NYaJuWugGY92LA_8mg9n-4uvcNiRkQ2OhVzkaozFExZiI2l03VK5-4DlbD0xOPNo9eyt_OqyoOpJ_Hy3zX4nRjrIm4HF2CuFGoDk07hCj9J11_LYew-6fR_q4L43A3MQKez3hzaUORIUoD07r7ERlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده رودان :
اول جمهوری اسلامی ‌آتش‌بس
را نقض کرد و سپس آمریکا پاسخ داد.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/farahmand_alipour/6287" target="_blank">📅 01:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6286">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
گزارش انفجار مهیب در شیراز
🚨
گزارش انفجار در اصفهان</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farahmand_alipour/6286" target="_blank">📅 01:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6285">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
به گزارش خبرگزاری ایرنا، در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
فرماندار چابهار : از محل اصابت‌ها هنوز اطلاعی نداریم!</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/6285" target="_blank">📅 00:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6284">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
گزارش چندین حمله به چابهار،
🔺
چندین انفجار در بندرعباس،
🔺
انفجار در سیریک، قشم، بوشهر، دزفول.
🔺
پرواز جنگنده‌ها بر فراز چابهار در ارتفاع پائین.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farahmand_alipour/6284" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6283">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
آمریکا از شهروندانش خواست تا هرچه سریعتر خاورمیانه را ترک کنند.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6283" target="_blank">📅 00:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6282">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMD8LmlF9dtW_n9ppKxRpI6QEXxtDEOZeKd6k5r9jaHphX7ZuB2x4FOmuvzkpSzuhK3CooFbmgshifVFysRdGWvr4Pna4MnxN2FNp-esexuuFvmYCJAhgcUfSgH8eqhwpQkR6Yg245Us02bJktom1ib5QIBAIa5PgJ5LGU9C9FTumRkNzb41Q-lnnQmJx9sEq1lhVY0nerk_x5bbVpnD0635S6P9iWvAp_YA4V3r5IlbLiTJMlJLQjVjJUpsnEvndrzup1rLMfURtN_cudyC7poMQIUA-PiU7xaE7158WF3QTASLBthMmRX8yv8yfsd6sbX8zW4upsYobqvtIxBRbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
اگه قراره کسی دستگیر شود، سران جمهوری اسلامی هستند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6282" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6281">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEJ6rdm-hlmlotnbn9FaHxJ0RX3m0GzYfYxBtckZb0nIVWIxdx7j3lcHH864cKmsuIm0dwzJ_y3pBMEhdxArYfoBASdyluMci6fDXNIOVO2ZfEVlGnnd1FsxHIjDavIXSJWEULKrkwWBJ_fE55yeUvSO5hfN2ybvq2YBoc_Ts1WgzkBvyCkvriILoNLFpkToCbfh2SQfw92mOVU-kT9PVtCbyXf1bqQIwKdbg3ruF2SAB0GRlHHGLSZWBQV6o2sSUAsnod26XixMpiiMLAwZK1FmeCnc55yoqp54QRTdCTecsWubf5pSrh6dfhuu7kojcma0VHqryzf207W9pgS5nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله جمهوری اسلامی به یک کشتی
در تنگه هرمز</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6281" target="_blank">📅 18:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6280">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlNGoBP_zp4PgiwudZkq5odweOQ2uaMM_6xVDo6Dq8arlPkda4xu-ttOOsPaAoxXXOhN2QCTnYryoFJPK51WUha-2civah0yFAJ50qrdmBcdx1_K0_NksdVS-KAGY2HA-59mMw1ksy4dqE1Ec2JU79SC2_c3OQBDbR46WAQzXLsCNfQuLsauWQ1FY0BsQupo6VvJoGzpedWIyfWGiiAcYBUOp9Mnmmenp-2uSXfTkBWFzCzrKFdwQyDP_eerdTg_IruTjZVfj9qK1LH-K4L7TEeBSDmH36HEwKMgs1_o0-l-Fl8LCBRFh1RGnWpcHIUhMlcughL1qWMcDLfqOC8vBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش‌هایی از حمله به شیراز
هدف: احتمالا صنایع الکترونیک شیراز</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6280" target="_blank">📅 17:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6279">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟  پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴  که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6279" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6278">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این سخنرانی ترامپ در عربستان رو به یاد دارید؟
پارسال، درست در  تاریخ ۲۳ اردیبهشت ۱۴۰۴
که به درستی گفت :« رهبران ایران روی دزدیدن ثروت مردم خود و خونریزی در خارج تمرکز کرده‌اند.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6278" target="_blank">📅 17:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6277">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6277" target="_blank">📅 16:00 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6276">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6276" target="_blank">📅 13:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‏
🚨
دقایقی پیش، شنیده شدن صدای انفجارهای مهیب در ⁧ ساوه</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6275" target="_blank">📅 11:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
نورنیوز رسانه شورای عالی امنیت ملی:
شب گذشته تبریز، دشت‌آزادگان، ماهشهر، سربندر، سیریک، بندرعباس، چابهار، جاسک، کنارک، خورموج و خرم‌آبا‌د مورد حمله قرار گرفته‌اند.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6274" target="_blank">📅 10:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">وضعیت اسکله بندر رجایی - بندرعباس
بندری که ۷۰٪ صادرات و واردات کشور را بر عهده دارد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6273" target="_blank">📅 10:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6272">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
فرماندار بوشهر: دقایقی پیش چند نقطه شهر بوشهر مورد اصابت قرار گرفت.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6272" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.  به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6271" target="_blank">📅 09:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">علیرضا پناهیان : اگر بی‌برقی و بی‌آبی را تحمل کنید، اول منطقه را و بعد جهان را آزاد خواهیم کرد.
به زودی نام نویسی برای آزادی جهان آغاز خواهد شد و آب و برق جهان را از ستم صهیونیسم آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6270" target="_blank">📅 09:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6269">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6269" target="_blank">📅 08:46 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6268">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
کویت : در حال مقابله با حملات پهپادی هستیم.
کویت در چند روز گذشته در صدر اهداف حملات جمهوری اسلامی بوده.
مساحت این کشور کوچک عربی به اندازه «یک دهم» مساحت استان کرمان است.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6268" target="_blank">📅 08:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6267">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okuTdKje8YFPAFaFtT8iK04tvGrvGBhCNweAigICTl9Ss3tUNEnsWFHD3T8lwxrziHEaL7O7HnifRaA5bKCU7hyJUfEPc9iO6bvbB1i9qyudjd762YYstJ-EEWxNljb0gQnRllat5LadLyshVFo7sPM7NMe3zPLXFpfSXZAsodvNPMUf1xwvDbM37nYdMMJxWqkLYVArVb0icyZcVGKPskPw-fT6JP17nxMInNiwrkuKv0thzA7i_SuzJn1ATvKYmWRnFk2A1elhgbvJXmYlTQ7VlmXkZsGZZGdFrvsrLBoV1rgq-UQuOLIJACpGEZexpFm7kscXgtjXwtPOLpbedw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استانداری بوشهر:  بامداد امروز در دو مرحله، دو مکان نظامی در خورموج مورد حمله قرار گرفت.  این حملات باعث قطع برق در مناطقی از این شهرستان شد</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6267" target="_blank">📅 08:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6266">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
دو زمین‌لرزه ۵.۷ و ۵.۲ ریشتری حوالی کوزران کرمانشاه را لرزاند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6266" target="_blank">📅 08:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6265">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">« یه راه خوب اینه که چاه‌های نفت
امارات، عربستان، قطر، بحرین و کویت رو کلا بزنیم» !</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6265" target="_blank">📅 01:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6264">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQj8n9BNSfHj2cw5lYbPpxpRgEkjVnGnU3_e-k6YGU4KDxybIxMcm6MnY4hSncbXhtcIQIDo2dUbXRulq-xmbHQ9N4uBhyIQv7eQZYUr5szQUhhodOf5fvp_trM6n2iav-xfAtjRQ2lIpDecbhprH0NR1IQTT_DFxx0yhdYWKPXqxyfgJmk8YW_bYjAiAK47XkTbvo4hGX2S4YFDyN3u0k-jWO-fX_Gun-BAZXs9f6fKOWpaipmk0vsIXix_THLBgSGDaJdGwm8WRvO66TJbTrUQv3BFb0oQDS4zb_nEovkMNG-P8ek7IycMdA4OSP6sCqcsDwIoJXha4QeYLRocjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیسیمچی مدیا:
الله اکبر - اسپانیا برد :)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6264" target="_blank">📅 01:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6262">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jWJaBoFw6T3jZLZlXYUTWfBd32P6EG58gWRxd0aUpfuu_1Vezg26LO2wxHk-zFblxLdLQsGR43t9Jx92O74GJMox2mJULYpCo1By__Um8EhOgTQRC0AcazAC8DGUpiQlUzJZ9iTqa5ykExQnG9xdTcRniRLQO1y5C3RLN1NzHosmb2yt7M6ie1ISaqAK0d1nke2Gk-fgmatHorLuuvCMoShlKf_Ka1rPhZSI6ItGjKDs-GxLTSZfxnV_qQFYhsZNAM4veF7r0Cd-TlWZBRen0UibLhNj4qh0Db_M7GOsAhTN9sA8Rsl-yA9Joe4whMZopHJUCYqiS_N9IzgGFWOdbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OmTADiQvwChS_pV7sEVOHUB7GZB68tMRTdEshnLGMRV1nSo4MJO3muNjhjgMTMG_2vrlzSkXUJnpfos7ElhckneiEi2zucGkRcZTADN4oF8PLqUVEBhoywhhsHRoLLmHC9ocO4S39abAjjR4KYVslw9JIdeqRukp2XX_MX5Jc9KGKX01_ADypiozEvtifkL-b0dCTRKM8OfsZKFOeSODYvwM3tM4Em_lzAs0HURFs_DKson5BXLZs_XT92OOClHK52KDVzAhQI8irWB50ffY4P3lQycZsSJrEpijnkzXZ8nJShTTNad7tYaKpNTocYFEhIYKv4ByzNAYzj7PsFerDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حمل  موتور پهپاد آمریکایی با الاغ</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6262" target="_blank">📅 00:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6261">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6261" target="_blank">📅 23:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6260">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OH_5S45MxowlJZKryRExdDv_YoI313N6BP4WuFfM0_dDBGIXRA_HeUilF1mZm2gQ8rQH96MuD5E6jXvzeXMjnpGwE_-M4Iltpjbsq1UsaFO_Cu4OR1Dg6vmzrn54i8qwQ7OfySz9oCihr7EtQDUDdv5qqv5tF2FQpYCbNajhLzk_hjqyqQDxHyrnnX2aLccb4sKepy6T0SkU1pk3DUfwPSkJU0_nsz-2WlvZHZXGzGBaiuhmpc7r2ooU-BOBMpWX4Y8IWcuOEaQeJw-iG9txi7iz62R3a_9NZljFKOkBx9dYIm6fuYivQNhoikQzw_rNVRt4jtbU5Asb3xPqEWxpaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2078890340753568161?s=46</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6260" target="_blank">📅 20:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6259">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MR8ITFqlJDq3hFOcHAREgGsdh1VSNZl1pkF3mlytJeJk3T_zAXcuiKYteVP6Tqh0G0r5dndob_LAPk51-5NH2v3KM2vREnDLX2daP9A02NRPqely7uPE97YMU5bdf_AeUkWEjafLF18aNuo1TJOB14A1TY6bIdghe5rGus-P8seRrDEOgIZ81Y3uHr968b2OPleXf3SJLHSmijrIQ0s5ISBrMB28oIIKwKc5wlJwyTaLlEqnvqCN5m0N5W3z1d1YMBEazthEJ7arsL1jojLA-pf6TD6w8xsQPCMRapQD9C3af0TxXNif7RRozoaj6SNSv8f_ADH35VvFMpFipTTd5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رهبر گروه تروریستی حزب‌الله
به وبسایت خامنه‌ای :
خامنه‌ای گفته بود سوریه
ستون خیمه مقاومت است!
امروز نه از خامنه‌ای خبری است،
نه از نصرالله نه از بشار اسد و خیمه‌اش!
ظاهرا ستونش رو برای
بازماندگانشون نگه داشتن :)
یک «هفت اکتبر » راه انداختن و همگی با هم رفتن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6259" target="_blank">📅 20:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6258">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTJP27xBNrimaOCWsw4qW_w9uYd6tWpqsyeoEtiOw12zjG-SD9AN15C2TGtBvTIPb2jULukfaQOnftkTuo7EL0YnlCWWZaroF_pfypSWfeClgylsOeQe_U0QDc7xtfUHSKOkxBowsgoz16W1lKSr0VV14C8g3POTi011ACt-qxJLRqGaVwJUO3Wl8PbBDW_jL29N-jVk4LSf6SriQ0kLCGD3BK-YjLxz8lcn4iVkR-pRphwG7t1Goj-4StgC0oM1R3gC1x60EKrNxk5yCgarTMl2D6gyufWqq_hNp2NZVgb9sHPVfanAzSbg78AYdyaaQWNF9Z_OEpAE6zF5Fn28uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای ۶ اسفند ۱۳۹۷ در دیدار با بشار اسد : «جنابعالی با ایستادگی که از خود نشان دادید به
قهرمان جهان عرب
تبدیل شدید و
مقاومت در منطقه به‌ وسیله شما قدرت و آبروی بیشتری یافت
.» !
قهرمان جهان عرب!
که مقاومت به وسیله او در منطقه قدرت و آبرو یافت! امروز در مسکو به سر میبره و حتی در تشییع جنازه خامنه‌ای هم شرکت نکرد!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6258" target="_blank">📅 20:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6257">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Aty9EUZVBZDoqiPYie6-q2BRAP5braKtWmFW9d12KyshTwoLab2cJoKwFY85A7sbuW8xFrPtbnSjjdrfqkXMjhBqxs7sIdRLI_x7JT6IQ2xNXLKelwemBes3zICGzpmQHvaKDtDBkIFfsF5sbVlYRifUKbXwP-CdoM9a2iUp0Y3W1nISL5cip6c6_qf0q9Mi2KfdMHL9dYISpDJNxUEu1Gbae2H2ZacT2YJqkwVDKi6GoFTkXdmn1tbilsumBvlK88EfQ_dino6yN3oTK_g1Rtktgh8iOJ85M-o2AeE6J-4YN_0MrKqMdT_L-YJaaAefJsJgVg9o9lu5TSz9xSZkFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ebaca90.mp4?token=Aty9EUZVBZDoqiPYie6-q2BRAP5braKtWmFW9d12KyshTwoLab2cJoKwFY85A7sbuW8xFrPtbnSjjdrfqkXMjhBqxs7sIdRLI_x7JT6IQ2xNXLKelwemBes3zICGzpmQHvaKDtDBkIFfsF5sbVlYRifUKbXwP-CdoM9a2iUp0Y3W1nISL5cip6c6_qf0q9Mi2KfdMHL9dYISpDJNxUEu1Gbae2H2ZacT2YJqkwVDKi6GoFTkXdmn1tbilsumBvlK88EfQ_dino6yN3oTK_g1Rtktgh8iOJ85M-o2AeE6J-4YN_0MrKqMdT_L-YJaaAefJsJgVg9o9lu5TSz9xSZkFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آتش‌سوزی در نیروگاه برق صبیه کویت
مقامات کویتی: در پی حملات مجدد
جمهوری اسلامی، یک نیروگاه برق و آب‌شیرین‌‌کن کویت برای دومین‌بار در ۲ روز گذشته  هدف حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6257" target="_blank">📅 19:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6256">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftSNMWwFxm7ISdWnejerwkzQHaNzkiugpntlfrfYLORD1Mlh2AfxIsBdrxQkRIippDo5QVwYvTZCzIMKG5bxsGZu38UIAcdS9tnEZEG7Y1ycfett8IQ8J9U5hOb56jrMH_N4XiR7lSs5fZyypUZHfXIV0YUQLcX-zBnGwbm5f3dxMJDx-WT2A8-bXMqCuE4xmD68lsZ85_jDP1ceZj2tt2TEF55Tv1bEdjQY_NLKmpIuVyiqQJIYYEK72luQObHQDfv-amai4JcLCSZTD8SOizOrQjzl1pc1FNQb3AFb6Yqh5mBO7k13TXbgF4NUMMt8rlJheDHb2Mjy9eupQVtuig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
حمله موشکی آمریکا به نقطه‌ای در آبادان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6256" target="_blank">📅 19:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6255">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ZiqoAi5xtwUcknVbYO0ueJu-7hsqlcFZCBsJUrzLeyDZEOBD05R5-Iz7_jwCLeYVgarGp0bGzHZh0l6nlrVvkATDMZVc3XR3VIykLT0kVwOShLVS7jG236D-d8BxA4ezjEi4XKJL404UI30bGvdOGllGnS1QK-qfre-PaT5_D42-f4qU5oRgLoPoqH6Onu0m_OnGJc0G_9jPeCcEd6MXnu2gsbM4e0uorevN86mHQcxAceLO6MApRC9MBxmQWhklQLYjEtrmxCrZr2bw6e0Jg-FfMxiiQUIq5kwouVdDc1rVEjSnqBtyHEPAPF9vTOHlHiCS1Z51szDtfq2OeoBCkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad154543bd.mp4?token=ZiqoAi5xtwUcknVbYO0ueJu-7hsqlcFZCBsJUrzLeyDZEOBD05R5-Iz7_jwCLeYVgarGp0bGzHZh0l6nlrVvkATDMZVc3XR3VIykLT0kVwOShLVS7jG236D-d8BxA4ezjEi4XKJL404UI30bGvdOGllGnS1QK-qfre-PaT5_D42-f4qU5oRgLoPoqH6Onu0m_OnGJc0G_9jPeCcEd6MXnu2gsbM4e0uorevN86mHQcxAceLO6MApRC9MBxmQWhklQLYjEtrmxCrZr2bw6e0Jg-FfMxiiQUIq5kwouVdDc1rVEjSnqBtyHEPAPF9vTOHlHiCS1Z51szDtfq2OeoBCkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمایت مجدد نتانیاهو از آرژانتین.
دولت چپگرای اسپانیا در ماه‌های اخیر تندترین مواضع را نسبت به آمریکا و اسرائیل داشت، در عوض رئیس جمهور آرژانتین
«جمهوری اسلامی را دشمن آرژانتین» خواند
که دو بار در این کشور دست به بمب گذاری زده است (از جمله انفجار آمیا)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6255" target="_blank">📅 19:13 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6254">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-poll">
<h4>📊 دوست داری کدوم تیم برنده بشه؟</h4>
<ul>
<li>✓ اسپانیا</li>
<li>✓ آرژانتین</li>
</ul>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6254" target="_blank">📅 19:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6253">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLIEJ-Wj36Z7dk6K3cpDXhMFRn_CT2nzkDiGFXiKxbv6RHT2wDp28rNdD9RiGHjdZVgkitb21xqfP8I3pA0Yx9Qq1BXvnNGVSEJJOhgw6LJyKjRL0hpwLrrvfRRlohMc3MVtupOKOBmjKNjOSYUXl6po4bshzwGnRxF00jEm-4SDWN8VF2dOhfpXS-rdS-TgNU5qliiKi4RTZy2Sw0XMoVNiZNU_WOOrh96sLrvHyGIKN6nVba-h8MwqSIZ4qKTXlQCQFeC8NnK9Vg2hiReqM50EesLH4sBsml-uizrfYfXbVl7qnKfMNVWv-_A_COLmqiEnvPYJrv7-JpHB7QbuCA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6253" target="_blank">📅 19:02 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6252">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGF2E_kQKBjf5g8RqbHJReq2RGVSyzaGNrDxIO3SBPFHKizu6PedOVq8NwKht1JIzaNQ90GOBR_g4pTqXVJcM6lba8-jpR7ZFnVZW0Cw6dJFhRh3fn8bb7ML9cApff9XUCTc1va5syy0djat7mGADfCVQ7xqolb1bCbw3f0UIDOayPDtU1fAp53XB0McBpxwAheESUl5p4MSZLncpU2IlCn7fFbA0IumG9bLiUSReEWv1MoIkHpemv7FJUaNauAZBLhXzi2h2K7Zug5XUCyTUcngqHSrybHE4Xyeta3_tD2MSYNKHXJKnABoRmXET8DZGsOz3FX3NRUjXTg_1S_FkG1k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28653e7d3.mp4?token=Wo1MhfbDy39Rl1VrrHzCb7lkHfSRgq711gpd09eALPNbKG0bc2TrznHhKrHIp4MmrDAfv5v1u7pD40eaZu5BMWXUxXETVAUAVZPoiqFrKLpyBEiXy8mYCgLXf-f9q0bHhskvdQJAIAa_qU6-mJyC0n8T69cACn0MqBJ_1YCFFIj2z3VpY95HoWMzwLaqRFo8OqJU5PRN3btB-IVLEw8EttHbZKJtrzV1PlIruH6daO917HPkhOu_NY5zcofoUKUQoYGzgNUy99CqwwR3y3AAcPzm3HymeQy-oFTK0jkI8KTAlCPYriCJSHr76HgNSuYTRIBiyHsLa4-hwjK3-bHtGF2E_kQKBjf5g8RqbHJReq2RGVSyzaGNrDxIO3SBPFHKizu6PedOVq8NwKht1JIzaNQ90GOBR_g4pTqXVJcM6lba8-jpR7ZFnVZW0Cw6dJFhRh3fn8bb7ML9cApff9XUCTc1va5syy0djat7mGADfCVQ7xqolb1bCbw3f0UIDOayPDtU1fAp53XB0McBpxwAheESUl5p4MSZLncpU2IlCn7fFbA0IumG9bLiUSReEWv1MoIkHpemv7FJUaNauAZBLhXzi2h2K7Zug5XUCyTUcngqHSrybHE4Xyeta3_tD2MSYNKHXJKnABoRmXET8DZGsOz3FX3NRUjXTg_1S_FkG1k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی وزیر خارجه جمهوری اسلامی :
[ در این ۱۳۵ روز ] تاکنون مجتبی خامنه‌ای را ندیده‌ام
!
خیلی مهم بود این پیام را به دنیا بدهیم که سیاست‌های ما تغییر نکرده و تغییر نخواهد کرد.
درست میگه، جمهوری اسلامی هیچ وقت اصلاح نمیشه! نه با انتخابات، نه با اعتراضات و کشته‌های زیاد، نه جنگ.
تا باشه همینه!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6252" target="_blank">📅 18:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6251">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">موشکه دیگه! میاد میزنه
(سیستم پدافند و دفاعی ج‌ا]
عراقچی از روزهای جنگ ۴۰ روزه میگه که از ترس میرفتن تونل‌ها، جلساتی که در تونل‌ها برگزار می‌شدند.
از اینکه ساعت‌ها در ماشین در حال حرکت بود که جاش رو پیدا نکنن.
از خونه‌های به ظاهرا شخصی که پنهان می‌شوند و…
مجری برنامه هم اسم دو تا از تونل‌ها که فرماندهان اونجا پناه میبردن رو میگه.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6251" target="_blank">📅 18:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6250">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامپ درباره مشهد درست گفته بود
مشهد برای چند ساعت سقوط کرده بود</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6250" target="_blank">📅 18:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6249">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحافظه تاریخی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=Yd3qZ5MXtv_jpiZmSxZCweYOnF-qbopmWC3XIjIWgRrkdehvXk17K8eUL9B4RwGM_x4Qt24GI1KoNXv34jzftBg8LHZPmY28E4gCOcWNpZolikGziGQVX3aUw-Yg8QORTZ7h7ZsHFp7Q35kC7ACEL5VB_0vJBsXEe_r2sNwkRnEBtjm7waR3p_QZxm4JNdi_jODIA2h0Dk05hZsfHdAxHgm8NvSwR5RX-Mftwp0sMlWStWePOZB7we3I8bktVHV6SUKC_nOiPxujMn4_adxVwAZBimCOvF6h7kHRrztK0XoTf0FVKH_z7dk6gv_alOPPLvE_EIeEhH6ny2tNgSTpeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d96f954f.mp4?token=Yd3qZ5MXtv_jpiZmSxZCweYOnF-qbopmWC3XIjIWgRrkdehvXk17K8eUL9B4RwGM_x4Qt24GI1KoNXv34jzftBg8LHZPmY28E4gCOcWNpZolikGziGQVX3aUw-Yg8QORTZ7h7ZsHFp7Q35kC7ACEL5VB_0vJBsXEe_r2sNwkRnEBtjm7waR3p_QZxm4JNdi_jODIA2h0Dk05hZsfHdAxHgm8NvSwR5RX-Mftwp0sMlWStWePOZB7we3I8bktVHV6SUKC_nOiPxujMn4_adxVwAZBimCOvF6h7kHRrztK0XoTf0FVKH_z7dk6gv_alOPPLvE_EIeEhH6ny2tNgSTpeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی خامنه‌ای، خرداد ۱۳۸۴:
خیال می‌کردند حکومت اسلامی یعنی خلافت موروثی، مثل بنی‌امیه. یک نفر مستبد با نام خلیفه اما با باطن فرعون. بعد هم که از دنیا می‌رود، یک نفر را جای خود معین می‌کند. در ذهن دنیا حکومت اسلامی این شکل تصویر می‌شد که بزرگترین اهانت به اسلام و حکومت اسلامی بود
@hafezeye_tarikhi</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6249" target="_blank">📅 17:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6248">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZGedsiAxra0veXP6j5pQbdRz9at1juZ2esYPPAqBgjV-SbNPxqA3orqVch01Gr9nST1rXXeAzk8LQKR1cTydL-qWE7WkcO0vq0ui1EMYD9m1Fv1T8UNoCjHS3OwhB7qbrr7loY0lo5HPqF9oJxsTCfdgKZ9EpxARcSHECBq2nPzs10x_MoRB6l8ef8zYCQYcI4GXjwHQj7ulz27pkt-02TKRNgcBlckfZHvKr9XWSIX2FF3oc3tWKE5y3AJplgzkJ6QgImO8QndceTAxVHpdOdSTITPEYF54Y_BnqgMs6pY8nbs3o3fps9dK25GeVYaNJuk-9n0qrIULIWZ8GsiN9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fcb2949cf.mp4?token=d2mZo952KSiSdcGBy20rXe96sMnbvPlbOT8fYxKTRAboNuRC-z7rpbcSuSLFEFGwDt4DMgidr3u0v2JS9mqcpbNmeofpRRWJ_hMBUTSQ55dYrkH7yprVygKveTCog-EI7TJqUZarYXa27vwwe4_-tv4JQx2kOjFTnxG0Z1AIjP0nBVOEkMSQPnVa37MmMU4gNUNZv-CovPbEUCOVjLBdg9umaWJJAW8plWoJiLjAYGtsfHAaef4bGBnAbkaLqORs77lCLylTLUHR4WkCex-UgrMu1iqk3t_vIUOJcmLQZXQODAtP-fJKcsuTaVj6XfYcYJyhSs2XABNP1MmgkhX4BZGedsiAxra0veXP6j5pQbdRz9at1juZ2esYPPAqBgjV-SbNPxqA3orqVch01Gr9nST1rXXeAzk8LQKR1cTydL-qWE7WkcO0vq0ui1EMYD9m1Fv1T8UNoCjHS3OwhB7qbrr7loY0lo5HPqF9oJxsTCfdgKZ9EpxARcSHECBq2nPzs10x_MoRB6l8ef8zYCQYcI4GXjwHQj7ulz27pkt-02TKRNgcBlckfZHvKr9XWSIX2FF3oc3tWKE5y3AJplgzkJ6QgImO8QndceTAxVHpdOdSTITPEYF54Y_BnqgMs6pY8nbs3o3fps9dK25GeVYaNJuk-9n0qrIULIWZ8GsiN9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار غلامعلی رشید ، فرمانده قرارگاه مرکزی خاتم (مسئول اصلی جنگ) که در جنگ ۱۲ روزه به دست اسرائیل کشته شد:
«زمان شاه فضا چنان  پر از خوف و رعب و وحشتی بود که حمل یک سلاح! یک سلاح ، دشوار بود! »
برای «دینامیت» افتادن زندان
و بعدهم آزاد شدن!
توی حکومت اسلامی ولی برای آتش زدن
سطل آشغال و یا داشتن سنگ در دست
حکم اعدام دادن.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6248" target="_blank">📅 17:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6247">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
گزارش انفجار در آبادان</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6247" target="_blank">📅 16:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6246">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8wZrI0J4vUaXS3FoNsG3lHCbvuEXX4Op2NzM7ELz4x4WmzXDNJt6SssbzxyPeiteF6hVjia8QhlRhXmsribJj6f8GJGLqJOGjlxCFAPfNqU5kcnJvPjtfqxTs4FC16RwrOrLxb732NA2NOPocGO3MeYRh2ug77e-tPC84u1kh61DVkeelH7AEeg5BDd80yrnlDIwmglPpvr3PdAHIOtLTUngY-3bEXgG3bP8kXdKm5fXBErf5R9t3bR_nv5kqwEQhzr_9sUJsm2sjhC_9yhtQoe5SEHOmp_ghGSoa5-EPVOHaGDH-rbss0ksG0vSOBWmA8lriTd3OMO4LidRm9pRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اردن : جمهوری اسلامی با ۴ موشک
بالستیک به بندر عقبه حمله کرد.
۳ موشک رهگیری و منهدم شدند،
یک موشک در یک منطقه‌‌ خالی از سکنه افتاد.
🔺
عقبه تنها «چند متر» با شهر اسرائیلی ایلات فاصله دارد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6246" target="_blank">📅 16:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6245">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WUsgX6TLZbpUe4Tmq5KeyAq_hZv7A8eTRP7RwMRjOdaEKarGyC1BTUpYmCtxRNCCMvpGL6D25LWYaJLhGjU7LlOtijlKwQ_OKLXtceGkj12zQybmeWjliA4yZlMEbLaqqc2oUMUiPrnmOVxdi7NHHlXbPW-Fm7f6n3BfwrVrOkJCvqExfOIa3TDCjN0DWmCweYiMqVvzsw0kleIXHEAc0RnZL4z6vZzlhlkShMCCYNX6qsfagWpBFFkR-jWx9xnnQpS7xyy6mvqh0MDNDXnerSqhsEAt5loYGZsdO0LFuB0kzjrK_7fPcLxpnfKro1TdDSKWITsYNlyD3SqZzZEyQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز ماندن جمهوری اسلامی
هزینه برای ایرانه و فرصت برای ارتکاب جنایت</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6245" target="_blank">📅 16:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6244">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حرف حق :)</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6244" target="_blank">📅 10:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6243">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6bWTd_kLgRcIaiKOCNEnzz71RI-fajULf5CXb4wGVX0c9euiWYuguUDpCnhLNufOe0CNm4f1HQXdjMBymHKJEtujjwmD2kmQeW3-D7g3_up9CYKqpOlONwmOgTM3iEzDh8uoAZyFJiaYPc1VOlPsThnVqB95D99A2XRy9kU7ogncfVUHbvNuhSJfvNUN-1o8SFDpLWUx7hEz2V0OhgPS29z-a_VdKvtgbFMj6rAQNBLslqbhVlz1F6GmViTOzh-JlRg0nQ4xIRFj52nh1syX2aWuauv7V8FfJ0J8lyXzd2hnQhWEJazXWNS9tD5TRitfEUN2NK5VFZUiuHDXSH0Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏خاطرات هاشمی رفسنجانی ۲۰ آبان‌ ۶۰ :
‏«شام را با احمد آقا و آقاى خامنه اى صرف كردم!
تصميم گرفتیم کمتر به كشورهاى خارجى فحاشی و حمله شود
. صداوسيما هم كنترل شود.»
https://x.com/farahmandalipur/status/2078615489446543468?s=46</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6243" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6242">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
چند انفجار در بندر لنگه</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6242" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6241">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
خبرگزاری مهر : شنیده شدن انفجار در کیش</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6241" target="_blank">📅 02:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6240">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
گزارش انفجار در اهواز</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6240" target="_blank">📅 02:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6239">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
گزارش حمله به بندرعباس</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6239" target="_blank">📅 02:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6238">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
گزارش حمله به اطراف سیریک</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6238" target="_blank">📅 02:00 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6237">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
‏
آغاز دور تازه حملات آمریکا در نهمین شب حملات
اطلاعیه سنتکام : «امروز ساعت 6 بعد از ظهر به وقت شرق آمریکا ، ( ۱:۳۰ بامداد به وقت ایران) ، نیروهای آمریکایی حملات هوایی جدیدی را علیه ایران به دستور فرمانده کل قوا آغاز کردند.
این حملات برای کاهش بیشتر توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز و
مجازات سریع نیروهای سپاه پاسداران انقلاب اسلامی
که دیشب به نیروهای آمریکایی در اردن حمله کردند، طراحی شده است.»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6237" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6236">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فرداشب اسپانیا و آرژانتین
در مرحله نهایی جام جهانی
به مصاف هم میرن.
در یکسال اخیر، دولت اسپانیا به یکی
از مهم‌ترین منتقدین اسرائیل
و دولت آرژانتین به یکی از مهم‌ترین مدافعین اسرائیل تبدیل شده‌اند.
نتانیاهو در دیدار با سفیر آرژانتین
گفت که فردا از آرژانتین حمایت خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6236" target="_blank">📅 01:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6235">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsVYILvzjGnrf6dTCX-pLHjkLWv9S0J_LWybTaQfe64852m7ApU7RqC4a6_hqLQajBm9OpP13dYfulcM6V6dgJn3XiWFAOD7I1xTkRJpwQJqT2avkMNfYOKI69YeVQy2DUo2MYSM-4O6j8VvV_MgghtV5gMrv0IncFg15yWKXUbYdv4l2o8HL6gI2sJkN16PVJeTOINtDJky2Hxy-cWOfV8mFgB77G824x5g8b_badPkr-Hg9Z77-RsR3MJhR1rQsg85SppqXLAb2K7iIRWF4zj6yio_PRrRVP4OCyTm4Q4Nv173Zsb7FEDO15mOKs1Z-cHvz1Alngn7xwpHuOX_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۳ اسرائیل :
آمریکا ۱۰۰ هواپیمای سوخت رسان
به منطقه اعزام کرده.
آمریکا همچنین بدون سر و صدا
در حال اعزام ده‌ها جنگنده به منطقه است.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6235" target="_blank">📅 01:11 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6234">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نخستین واکنش ترامپ به کشته شدن دو نیروی نظامی آمریکایی در اردن : «بسیار غم‌انگیز است، از وقوع چنین اتفاقی بسیار متأسفیم. آنها در حال خدمت به کشورمان بودند.»
ترامپ همچنین بار دیگر تأکید کرد که
«ایران نمی‌تواند و نباید به سلاح هسته‌ای دست پیدا کند.»
ساعاتی بعد، پس از آنکه جمهوری اسلامی اعلام کرد اجرای تعهدات خود ذیل توافق موقت را به حالت تعلیق درمی‌آورد، ترامپ در واکنش گفت:
«ذره‌ای برایم مهم نیست.»</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6234" target="_blank">📅 01:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6233">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!  در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.  این…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6233" target="_blank">📅 00:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6232">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV90OR5lFGQ4xdqGv-u4qMTiT0vLgA3QUKKD0DW4aKtEcykIoPK5FqBCcbWP6sbaF-FepsRwpV5V3iI1PtHKM08iQ1WjNNNpfCzGwNoev6yWzJ7Y-Imqm4KuFPTOPzfplRccjUKbnXkoHQzsA-JKOYEuobZTVyKSrxyN3mmEUcBGWuyXMyRdGrmzx_5K91biwXTv8LyEAVFTHF-QU7N9MjpmF2LHLBYtlNssIRYblVzSXUZQ6oeRCAAHsZSF9m35OHCwRhbWfSVE69yDXJrbSoHdVqp87PsMdyz9O2oL25-seH6cDy8acxaOv48SVq43rDpL4b0irz7NCgTZynFklw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در این شرایط،
جمهوری اسلامی نباید مردم رو مجبور
کنه که در این مناطق که نه امنیت دارند،
نه برق، اونهم در این تابستون سوزان بمونن. همونطور که وقتی  جنگ ۱۲ روزه و ۴۰ روزه شد، خودشون به مردم تهران گفتن که می‌تونن برن شهرستان‌های دیگه.
اونجا حکومت نه امنیت رو می‌تونه تامین کنه نه حتی برق رو! برق نباشه هم آب نیست،  نون نیست! و …..
جمهوری اسلامی ولی مانع مرخصی کارگران و کارمندان و….. از این مناطق شده!</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6232" target="_blank">📅 00:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6231">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klYWfIxCvuuQNlI9fTSRdtIs4w4YJVSGxVDkWOzkxe63wdGduoWGQrOQ2O0wNwy-5sbqers3bTOkpoQmVm-wE6I-NZunHvXvfYEX6rSQcdP5tuttFT-PfEEmANgP39-K42AOF-6GOv2ZD-gs-X5Mz8QBSL0VZWS2mXh8UiwzpacijhwFejUeEFzGJJrSmqDB31CgWmZyCY6mz9pX7YPEoErb4LdzoFYGq7AyprMcX7OBgh9pkDowbX7VkBTkgP0j_pOc5xQcgK0P3ZlFYKOpZq75qIhDAU0gEbKuhPDpwe5vM6FE98YXRA3eSCtsjiygDHQC-6ABNF0hXzY7_8gC9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی رو میگه؟
مجتبی که مثل باباش شجاعه
و در صف اوله!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6231" target="_blank">📅 00:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6230">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
انتشار گزارشهایی مبنی بر اینکه دقایقی پیش آمریکا پل سورمیچو که ایرانشهر را به چابهار متصل میکند را مورد هدف قرار داده است.
🔺
گزارش‌‌ها از حمله به قشم حکایت دارند.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6230" target="_blank">📅 23:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6229">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LE4_YlfSpgp8zzuW9vvXBAxLTYfuQNtO-joZHUHPk9MBEcnxgBoJlMDRaYlwJ18SPa-IFEo2fXhdu67-tO3OM53n_ISzPZ4pZMZqBuGReqaE_5qr8rouKgPN9mbmKJSIQ396vuH53AcBC1rncYCca2J-Ml05MQeseNuNu39hQ7FbA-hDwMc5OF8nAIhRduWFzLj-Ey3crCN6bepAdRgquGzGXvtp8ioeAAVMOCBb9YfM2LhJ0PMdpKpdbt9Hii_kXm16SRLyfRTiUmlXmVNVl9ibjuoOBNPVZ8--dPa9ud5tD20s58B-0KRwjGs0ZEWZII4FoZDyvQudM6LUHDHQmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی ترسیده از آمریکا
مراسم ختم خامنه‌ای رو لغو کرد!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6229" target="_blank">📅 23:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6228">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEbNRdW0xSwkYLl3c5fkvgnyaSTgzJe-RET51FcOrUK5dRuWtaBV3zlEijxt_jnQg2spoTwbtSZBLwAZ8bcEgIYNzQOrSsZabDnp-VCcl1NFJXq2Hp7KlLlQvdVv8kzd8x8B_m2Jn-otc4jwcyOxWWHMbyx-10uGlKMpYzbZNNLJdSPwWdtECdRCOoINfqMufusfiLuoxCR1Rv9YSbTprQBl-Iymc1znACrrHh8C5_tssimnHOxc-m0y-p7XgQUtTfSX8mW4T_ul2SwdAVahPyAbgcfVuSbPWG7EZP4lRG4w0NEd1kK7uZYXttaCGn2_OJLuVi3P_6AlChwU9Tfduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خطر اعدام برای ۱۲ جوان‌ در اصفهان</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6228" target="_blank">📅 22:09 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6227">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWbtaCRHeZTwHhHXc7vPWB9hK9ljICBWbL7_W0RqoxGiofpQFQpPFfNwiclur04yoXYUU18PKSaihuYV5Hdak_th8y1LIHdid4nDDtI1hGWz3iOmkMDKwKQSqOlKcC-KyfWBotGk0WU4PmQG8CVQfdNKcN_K3d31x707FYa1xz2HcJIey3JF-RUZ3zww8MA8JwDR3quMEAHKsLw_f_O_nKEdfbV0aQDzBol3xX_466FVdNHp-P6Xdvy162CGsogJdAKoU3ySF5truYMcE-X6HODdhSRqzRmlL2n0YqrDFKsDG37axv7CTW4lQ2-gOpxOxXlwreUkV6r_PKusvZA5Ig.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6227" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6226">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
استانداری هرمزگان با صدور اطلاعیه‌ای از مردم خواست تا از تردد غیر ضروری در جاده‌ها خودداری کنند چرا که احتمال حملات مجدد وجود دارد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6226" target="_blank">📅 21:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6225">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
پیام منتسب به مجتبا خامنه‌ای : نقض تفاهم‌نامه بار دیگر بی‌ارزشی و نامعتبربودن امضای رئیس‌جمهور آمریکا را ثابت کرد. برای دشمن آمریکایی درس‌های فراموش‌نشدنی داریم.
احتمالا به مجتبی نگفتن خودشون به سه کشتی حمله کردن و جنگ رو راه انداختن.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6225" target="_blank">📅 21:26 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6224">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
بر اساس اعلام ارتش اسرائیل، ده‌ها فروند هواپیمای سوخت‌رسان هوایی دیگر آمریکا که راهی اسرائیل هستند، به‌جای فرودگاه بن‌گوریون در پایگاه‌های هوایی اسرائیل مستقر خواهند شد.
هدف از این تصمیم، باز نگه داشتن مسیرهای پروازهای غیرنظامی است. وزارت حمل‌ونقل اسرائیل پیش‌تر برای کاهش اختلال در پروازهای تابستانی، تعداد هواپیماهای سوخت‌رسان مستقر در فرودگاه بن‌گوریون را به ۲۰ فروند محدود کرده بود.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6224" target="_blank">📅 21:22 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6223">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tdYSkNkkE6vIJfewCF3jGaiMC9TIqWdWiLVxzZUpSDfYSIqi4qhPRsz8J6GeSNibdE_0-6d9bbjNnqbGmQkOebvaN82S4FpRTFOnx-JsY2LWc4k22YaqHRdxEXIsfDOQgNMnJLcKIEa5mNL86eBZW0of8PtZXhCYABy0aMgmDHDFMRhtMTcV6M7-TVadU3jGNhbydMn-zg8e1xVDT2PECiE2bNYY6P6_QLLh161k-u_k5VxxAYrZNK4K9KFnQ4FFWPR54ncFH14DGwaKDqUqhOzaK_eDS9ZvEk5iSP5KP2IGqmDaY__5Hf-JhHwpplsksZknL0Bv2YXwpqSGfn--ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
بنا بر گزارش سنتکام (فرماندهی مرکزی ایالات متحده)، در پی حمله موشکی جمهوری اسلامی به یک پایگاه نظامی آمریکا در اردن، دو سرباز آمریکایی کشته شدند.
🚨
همچنین یک سرباز دیگر مفقود شده است. چهار سرباز دیگر نیز زخمی شده‌اند
و برای دریافت خدمات درمانی به پایگاه دیگری منتقل شده‌اند.
🚨
با این حادثه، شمار کشته‌شدگان نیروهای آمریکایی از ابتدای آغاز  این جنگ
به ۱۶ نفر افزایش یافت.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6223" target="_blank">📅 20:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6222">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‏
🚨
حمله سپاه به یک کشتی در سواحل عمان</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6222" target="_blank">📅 20:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6221">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyf5u19l8s8QPfQkiwcoBIYNftzPssg80q3JIXBH5-RDY94Jf7RnRFPreYEau_AA4bXI8YEqd67rWgGpmZy6SW05Bw6mVUIrHEU4JStpKoUCudOMA3NMoN8rQaHx1VdPBl9qV8fz1y6V2xKstCHy0iehYbGVncpNkHc2YnU303K3rvVuuZb_nque2QpsHVRgXIV7_YWuR4dHxbypTlCG3QeDvnsRrXV-FH-3Xjv64wUNDpwagFKqJ4W8zehc_Py95yOrm8UCgRhKYuv20EQp38wNjMysB0bwVeLENKnpmggLPQ591_7cdmuzjwxAh6WhBGutgRKneKirtz3avPrjxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس وابسته به سپاه به نقل از یک مقام امنیتی:
اگر  آمریکا به زیرساخت‌های غیر نظامی حمله کند، فرودگاه‌های دوبی و ابوظبی و بنادر جبل علی و فجیره باید تخلیه شوند.
هر ۴ مورد ذکر شده در امارات هستند.
در یک هفته گذشته جمهوری اسلامی معمولا به بحرین، کویت، اردن و گاهی قطر حمله می‌کرد. اینک اما امارات را در راس تهدیدهای
خود قرار داده.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6221" target="_blank">📅 19:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6220">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N4q9b3C3cxijjZbkbhjQ1hXuEDIHO2rXV6FtOm6wCOuHFp9rt0s7Y7Y6bkoObHUWhlKwLxDYNpB4Q2SjqLRQHxZY_nc3G05iOia8yYDbKDCIxWvU9XCHRW8CVd8M1Nwf49FP7685kw-kxPRa8uNkNObKIhEsOEyi3_qywj2L7SIpJiV-B3PHujKbT1b9fD7nLbZukvS6hN9YUWloMZcN1Dqqisu2aFDsMFRJLILUrrJA0B3Bbd6EZXj3vCcbhvnDTFeQ10-dXKyN21Kyi5VnVvx1qlBPP6f29vNj6PmeZcfFSVI5-KV7QCveVHJP4k-iUXoi_0ACs6v3ZcD3J2ZeFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
استانداری هرمزگان: در ساعت ۱۲:۳۰، ۱۶:۳۰، ۱۶:۴۰ نقاطی در حوالی سیریک هدف حمله قرار گرفت.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6220" target="_blank">📅 19:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6219">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">- اگر در سوریه نجنگیم باید در ایران بجنگیم.
در سوریه جنگیدیم اما در ایران هم جنگیدیم پس
❌
اما یک گزاره هست که دقیق تر به نظر می‌رسد و باید بررسی شود:
- چون در سوریه، غزه و لبنان جنگیدیم، و همزمان دنبال موشک تل‌آویو‌ زن بودیم و برنامه هسته‌ای، مجبوریم در ایران بجنگیم.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6219" target="_blank">📅 18:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6218">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
حمله ج‌ا به بحرین</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6218" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6217">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شرکت ملی نفت کویت گزارش داد: در پی حمله جمهوری اسلامی خسارت مالی سنگین به یکی از تأسیسات نفتی‌مان رخ داده است.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6217" target="_blank">📅 15:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6216">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آماده‌سازی اذهان برای اشغال مناطقی از ایران در صدا و سیمای جمهوری اسلامی.
«مهم اینه که گریه نکنید، بری تلاش کنی [اگه تونستی] پس بگیری.»</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6216" target="_blank">📅 14:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6215">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMHrA9_4OeW6T0knNrKjH0qGc1qXJCNY_hTt7t14Ol3PdD5qEGiBo9fcSf99Bjz5o_yyrotpppseW3dtaD4YdKGY97SLemoLWC18iZ0GJ9LWUKWGiCX-WiV9QVhxIFID-XYYjxeGqa7IMln4I3jG_sv4U5JAXKdbajPrZhjHF3-iWCbrJAZ4XHpyVmBsd474g5hAFFySzRjwJOJu5Fi_yoSwnFoRDOUuvL1tDCuoRqypNSYx16inXKJ0er2b8BMVNXurEe5E3Hl0BAsuJcU2lpKCwDHTPHGhwoT4xMHmmY_oMusBLNv_U_pazRj0KKDN8nBSrdD4NBF43IoePfjYUWdc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8760b84619.mp4?token=hiPFdQgPXZ0hqyEoSHplUdLwXKuZnwQGRQ7_m1DsDYlcPH2zFnx4BgXYJdRe9zdklV8cvMot2EJI3vvu6xTy4-EAbfb-D3JQBwzaNFdOvJQQz1vzl1YeWYzfYc2X7n73PB6xrPG-D3ws8nw2l3qk_GJKBoraK2Tg9Ch2k1Ljt4NRBYQvUTbakEe4k-PQcaHWtBa3fYcwzwJX9wo15zuAX4wlc8aHL3vVgY12uKVV51Zrls-2WZeibgaqws1S5Y-vthhhaPLpzyF5YnCpQTLPU8YrUeubeW1Rx3TYvtwAreHjDOtMAv6cOTDJVzABP7DyRRq3Kk_roEjrcouZIdskMHrA9_4OeW6T0knNrKjH0qGc1qXJCNY_hTt7t14Ol3PdD5qEGiBo9fcSf99Bjz5o_yyrotpppseW3dtaD4YdKGY97SLemoLWC18iZ0GJ9LWUKWGiCX-WiV9QVhxIFID-XYYjxeGqa7IMln4I3jG_sv4U5JAXKdbajPrZhjHF3-iWCbrJAZ4XHpyVmBsd474g5hAFFySzRjwJOJu5Fi_yoSwnFoRDOUuvL1tDCuoRqypNSYx16inXKJ0er2b8BMVNXurEe5E3Hl0BAsuJcU2lpKCwDHTPHGhwoT4xMHmmY_oMusBLNv_U_pazRj0KKDN8nBSrdD4NBF43IoePfjYUWdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنرهای جمهوری اسلامی
و کودکانی که تقاضای «سر» دارند!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6215" target="_blank">📅 13:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6214">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=aWqo5kvxfiYmxjcbKNncnF6B0OSK4m_gjPac2W4kD--rpQK6T4Xixgre4hgolRZAbJgVRt3yV3hiw1KqtQKhDDmirJbVTH1EaLC5KtjOdgDHTEJxyb1KL7xib7mEEtZvL9ON6YzwxAbpatgAKHlQuXhZiX_NBrMEG7C9SEYSL9mwrpm1bC0AvHJ9bVyJymjrTIe0DstqvoYmDpQR27bYS1_5YEzakx7KeUboWJ52KNVjmXPU_BdwYoTOpC8KmNtuC0RiAvz86HW1mEDzt3j2ZdlywpMFlISsnRBsBFBHBhAfPsbdOeklB-F19H-8AKgZ_ePHLAq4q-5GWrNfgPhQNjkTxUrVCGaDskHAHi9J7-AV1WRXPSmUquMNyMjjUlWX4PiXD1Sit1li2iX_RQa5khm1xAeVsrHAVkLvVUpiNTCSrXassl8CcBxU0hlvpSkExUtM_HdGtQHPzoTIDTZfYnitiNTZlAjtp1yTJXJHAnNMbZYDS8iOw7Wl-PovSSGhsQE9re_f5HMw3btxymhgSqdhfOl4PgNLrV-1aQAnEhkFiWFFiSYPMRjL4w4j_gXuYI0pKUfxfSkYKJ5Z83FTVLwOFEfjtDK7_eVm-Trd1g3E0srQwkYMukVxd2_qApxrR1OW4KjUYOobGldzC842DQ0CXTD3tBQrtKWp0x2Xlho" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbfc942e21.mp4?token=aWqo5kvxfiYmxjcbKNncnF6B0OSK4m_gjPac2W4kD--rpQK6T4Xixgre4hgolRZAbJgVRt3yV3hiw1KqtQKhDDmirJbVTH1EaLC5KtjOdgDHTEJxyb1KL7xib7mEEtZvL9ON6YzwxAbpatgAKHlQuXhZiX_NBrMEG7C9SEYSL9mwrpm1bC0AvHJ9bVyJymjrTIe0DstqvoYmDpQR27bYS1_5YEzakx7KeUboWJ52KNVjmXPU_BdwYoTOpC8KmNtuC0RiAvz86HW1mEDzt3j2ZdlywpMFlISsnRBsBFBHBhAfPsbdOeklB-F19H-8AKgZ_ePHLAq4q-5GWrNfgPhQNjkTxUrVCGaDskHAHi9J7-AV1WRXPSmUquMNyMjjUlWX4PiXD1Sit1li2iX_RQa5khm1xAeVsrHAVkLvVUpiNTCSrXassl8CcBxU0hlvpSkExUtM_HdGtQHPzoTIDTZfYnitiNTZlAjtp1yTJXJHAnNMbZYDS8iOw7Wl-PovSSGhsQE9re_f5HMw3btxymhgSqdhfOl4PgNLrV-1aQAnEhkFiWFFiSYPMRjL4w4j_gXuYI0pKUfxfSkYKJ5Z83FTVLwOFEfjtDK7_eVm-Trd1g3E0srQwkYMukVxd2_qApxrR1OW4KjUYOobGldzC842DQ0CXTD3tBQrtKWp0x2Xlho" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرنوشت ۹۰ میلیون ایرانی افتاده دست این جماعت  متوهم</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6214" target="_blank">📅 13:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6213">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">آمریکا ۷ شبه که به جنوب و گاهی مرکز و شمال ایران حمله میکنه، اما نه عنوان «جنگ» به کار میبره و نه حتی «عملیات»!
در جنگ ۴۰ روزه هم از عنوان  «جنگ» پرهیز می‌کرد. به این دلیل که فرمان جنگ در اختیار سنای آمریکاست و رئیس جمهور می‌تونه فرمان «عملیات» بده.
این بار اما آمریکا از عنوان عملیات هم پرهیز کرده و به نوعی داره با سر و صدای کمتر، این جنگ رو پیش می‌بره.
رسانه‌های بزرگ آمریکایی هم  گرچه اخبار این «حملات» ۷ روز اخیر رو پوشش میدن، اما نه با شدت و هیجانی که اخبار جنگ ۴۰ روزه رو پوشش میدادن.
شخص ترامپ هم از  هر ساعت توییت زدن و تهدیدهای درشت، فاصله گرفته.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6213" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6212">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRJZnrO9yAG4Ugy1C7pY5h32VAk7RFzWRXE9oSUVsh456F9C3MW7jz-XyfqLrfhFpXdkhVd2ZuHCxgRaFX1ZwiAyM7ooAn7_241SNkjo3XsdLSO7n1HpSrvD1Biid7hRif-Zoiz3ytGZwBotjeUFddVeAHLcGn5TOfuwRxxf2Tv9zSOqRWDTvk5KhdfAfq7RQc13Lnxjw4dLqa2-P-U_lcLjc93dLulbmTm-fgz2FWaO-qLCuXY3lmJSccNSHVCLH9GJOOqZTMYlpOSyG_e6x6aJtZmwr0wZFF3Mz3374XMBJGXKzejfWycAbTWnR5jzimKjd81N3Y6iMbvcU838-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه : در حمله به اردن حداقل ۲ جنگنده و ۳ هواگرد آمریکایی را منهدم کردیم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6212" target="_blank">📅 12:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6211">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه مرد هندی دیده یه تیکه یخ توی فریزش شبیه فرم مجسمه «شیوا» شده، یکی از خدایان هندی! رفته به همسایه‌ها گفته، ملت هم اومدن دعا و نیایش و اینکه این یک نشانه است و بردن غذاهای نذری و…..  :)
شیر، شیرینی، غذا، میوه و..
صبح یخچال پر میشد، شب خالی میشد!
و مرد هندی میگفت، شیوا، نذری‌ها رو پذیرفته.
در عوض مرد هر روز چاق‌تر میشد
این داستان‌ها براتون آشنا نیست؟</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6211" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6210">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💔</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6210" target="_blank">📅 10:42 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6209">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f27e890899.mp4?token=iG-8BXR1IR0FIj9o1ZAOm6vHJs-xwxt4e1Rk4jQQxGL0_b7_kz2LFf_kW6r1WJ1Zf3lVbCZWmefAuWT16_aFpWa9-I2ohvNHY44bhHRaIuMfWaxU0kobvZbNAttfcmLBaClLKpVPDcLH8kp9GpMTkkCffy2kNdqRbpDgiMVr1OoiqV8A3iyjtBOLTlEgDW2Bj6xoFi-YhQAy0pNtjG2UKL0Ft3dXU6UbDzEcrPb0I_89C4R1sZD3UU_63CvHH47oqb-V169wxre3V3SNXT8CaDkQ-lFYG12FHfZTplxP_Ab2PznooAdb1fsGCYkFav1CU2NqQGHomx5Rlx9VpQ37kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f27e890899.mp4?token=iG-8BXR1IR0FIj9o1ZAOm6vHJs-xwxt4e1Rk4jQQxGL0_b7_kz2LFf_kW6r1WJ1Zf3lVbCZWmefAuWT16_aFpWa9-I2ohvNHY44bhHRaIuMfWaxU0kobvZbNAttfcmLBaClLKpVPDcLH8kp9GpMTkkCffy2kNdqRbpDgiMVr1OoiqV8A3iyjtBOLTlEgDW2Bj6xoFi-YhQAy0pNtjG2UKL0Ft3dXU6UbDzEcrPb0I_89C4R1sZD3UU_63CvHH47oqb-V169wxre3V3SNXT8CaDkQ-lFYG12FHfZTplxP_Ab2PznooAdb1fsGCYkFav1CU2NqQGHomx5Rlx9VpQ37kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از پل‌های غرب استان هرمزگان</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6209" target="_blank">📅 10:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6208">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
دیشب ارتش آمریکا به تونل میرزایی حمله کرد و این تونل را در هر دو سمت مسدود کرد!  این تونل در مسیر اصلی اتصال بندرعباس به کرمان، یزد و تهرانه که ستون فقرات حمل‌ونقل زمینی بین بزرگ‌ترین بندر کانتینری ایران (بندر عباس / رجایی)  و مرکز کشور را تشکیل می‌دهد.…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6208" target="_blank">📅 10:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6206">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
معاون سیاسی، امنیتی و اجتماعی استاندار هرمزگان می‌گوید که چند موشک به تاسیسات برق و پمپ‌های آب‌شیرین‌کن مستقر در اسکله روستای بونجی در جاسک اصابت کرده است.
گقته می‌شود که این آبشیرین‌کن، آب حدود ۲۰ روستا را تامین می‌کرد.
🔺
شب گذشته کویت نیز اعلام کرد که جمهوری اسلامی همچون پریشب، به یکی از تاسیسات آب شیرین کن این کشور حمله کرده.
🔺
ارتش اردن اعلام کرده است که سامانه‌های پدافند هوایی آن کشور ۱۰ موشک ایرانی را که وارد حریم هوایی اردن شده و خاکش را هدف گرفته بودند، رهگیری و سرنگون کرده‌اند.
🔺
ارتش جمهوری اسلامی نیز با صدور بیانیه‌ای از حمله به پایگاه آمریکا و چند پل در بحرین خبر داده است.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6206" target="_blank">📅 09:58 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6205">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">لغو آزمونهای نهایی یکشنبه و دوشنبه در هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان
وزارت آموزش و پرورش:
🔺
با توجه به استمرار شرایط ناپایدار در جنوب کشور، آزمون های نهایی تمامی رشته های تحصیلی پایه یازدهم و  دوازدهم در روزهای یکشنبه و دوشنبه،  ۲۸ و ۲۹ تیر ۱۴۰۵ صرفاً در استان های هرمزگان، بوشهر، خوزستان و سیستان و بلوچستان، لغو و به زمان دیگری که متعاقباً اعلام خواهد شد، موکول می گردد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6205" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6204">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=VTsnopKj_2xCqbohpN-uDZZaJgErQ71Siyz6U4CIak2q6trxJ3q2uKE-rwJ4nAPvFWenXs6tpsic6b4r6siLA7_oA3mqzJ6havBX3fKomrNK7R1EoW-qfQ1GgbNdwKupTee0luWhreVuwd-rzryBssyh06jjM0zttCnTgFBMKEgjTEws3jdhcdQEqnSdrf3diNEDy9C2s1W5oJX6qLNf12I19NqAPAnZK2AOI7iHyBOAl7PXy161yHdzRhKwTd-HmkVJNZcfeaAKEOhVJB4Gi3kXnuXmAyQFR1lbGCkrKWiDq-Q25dRj5I8NFFMY2mHxqzUpPW7DZGrlRlcgMzIhWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/284d23eb93.mp4?token=VTsnopKj_2xCqbohpN-uDZZaJgErQ71Siyz6U4CIak2q6trxJ3q2uKE-rwJ4nAPvFWenXs6tpsic6b4r6siLA7_oA3mqzJ6havBX3fKomrNK7R1EoW-qfQ1GgbNdwKupTee0luWhreVuwd-rzryBssyh06jjM0zttCnTgFBMKEgjTEws3jdhcdQEqnSdrf3diNEDy9C2s1W5oJX6qLNf12I19NqAPAnZK2AOI7iHyBOAl7PXy161yHdzRhKwTd-HmkVJNZcfeaAKEOhVJB4Gi3kXnuXmAyQFR1lbGCkrKWiDq-Q25dRj5I8NFFMY2mHxqzUpPW7DZGrlRlcgMzIhWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت مسیر ترانزیتی بندرعباس - سیرجان که در ادامه این مسیر به تهران وصل میشه.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6204" target="_blank">📅 09:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6203">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipaiWeWIwsFNbACU6a5cqzv21bKLClKysWhAPxudDzmaiOE_6vTNrOyugHbVLpxMcDmISwzyeHfk31TVIFcBJhhDqLLjEdANXRIk4U5aFRf_dVuUh9InLHJVbc23JDORjC-uX91ej6KR0CEcKJBFxzF5_fCmw-lAVN-22mciBLtaxe8v01SqPKkpaKGMXDEW8FIXMrNPlUSpdJtn4BRkagLKwcwI94d9-oClBRtv0LNr9KuTwoM7aqsw8Z9R2Y8ppBIk2WgC7dW1rij-hddVvZ2Zf1_T7S2gWTg7ZCWELMq7JuKuM2mXtGFDoy_3-ZfFN8f4Q-6IKffOGgKRktclEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه سپاه که میگه شب گذشته ۴ کشتی با کمک ارتش آمریکا قصد عبور از تنگه هرمز داشتند که سپاه بهشون حمله کرده و متوقفشون کرده.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6203" target="_blank">📅 09:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6202">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhMkFIckRMpG2xyQuoAEMGXhF2NbA0pHJqXTPzXhinz2heyzaWUyXnzY2dMFOlq0TkVN9SZYbvg0pQHCDcyJlgMyGbS1eAmzl7sWgrAzKhaFz03ibB6V8OHHVxH1WL84BvStRaSrJPvkYJFBivwYa4edCq9710YY3GxnWsRvs7LjqUrAfUh_Q_HejLWfoQLtWLGqiBlycmC8ToDhPtkAFJa-5VT5FgwLSS8QiXv3xwd_yPqdZs9JcKQ8vRR9-uFH-QmnT51xqXmJH_UIppMfO_JQSaGZyDONvyqMn77_0L97d2-JCl4fTA-zeZqNSPMTRPHo_Y-Zk4T9cZ1ZoEYV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش آمریکا شب گذشته با موشک
به دکل مرکز کنترل ترافیک دریایی جزیره لارک، واقع در میانه تنگه هرمز حمله کرد.
این مرکز برای ایران یکی از مهم‌ترین مراکز دیدبانی و کنترل عبور و مرور کشتی‌ها در تنگه هرمز بود،که اکنون کنترل تنگه را برای ج‌ا سخت‌تر می‌کند.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6202" target="_blank">📅 09:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6201">
<div class="tg-post-header">📌 پیام #16</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6201" target="_blank">📅 09:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6200">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=LY96nKawx1k9n_paBeA0jzASCtT33HKeXjqYHzlyCSJUCVT_0N-aLZfsgnYHS8siiSrr68QZEBgCZXOrFEjfJDJB2jxoOHj1A0uIpXY8Be4Cj8GtZnVdCnas1MMDT2dyeIgywd-__zzL8f3MeNz3USzwDZDYpmwfDOipJC3D3wEhIOZLw5HudlYy5ck-rJCMQ4MIwlYCRI0DHy0RAtQWQQj8tT26szZmQCSdA9HMu3MTkM_dYMmOidgUiI4e3URpGUpC8Tlln4bfqF4XsuhWpSq5c7v898cWUGf9UaqzdWmpatkav9c5THoG1yghLEMkrKzMPMKhUgoWU8ETJSLfDEGEfzhFwxU4UrGHLco6E8z_MV6Zaf7HrcCuM2qqzfU_785yLqJNNFByEDJERmqSZbKLgYU4Ha6SGwV8WqovzEw0OvmF90OfK17fk0xTbRhjdhmmK27LdpIJAvLOnO98xIiDDysjK8jzHKjFUMVaT4AH9MHA4aUiMIQTnrcbVaIXUJOUGf8JWO7Km2zq25qgLzVvPSuH0VBlA-kmykt_EsJNeK3bKm3oCpX4NkvDkqW-IMH_bhLQgr2ZgJpYzw06T3W7n28vMTUOcHdJ-_bvKKlV6GICPAB8SJg7whKlO3nhs7W_fPnsdr2rBnHNAkJKDIFaHjApj85UM1CxCF98Mzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc06e2272.mp4?token=LY96nKawx1k9n_paBeA0jzASCtT33HKeXjqYHzlyCSJUCVT_0N-aLZfsgnYHS8siiSrr68QZEBgCZXOrFEjfJDJB2jxoOHj1A0uIpXY8Be4Cj8GtZnVdCnas1MMDT2dyeIgywd-__zzL8f3MeNz3USzwDZDYpmwfDOipJC3D3wEhIOZLw5HudlYy5ck-rJCMQ4MIwlYCRI0DHy0RAtQWQQj8tT26szZmQCSdA9HMu3MTkM_dYMmOidgUiI4e3URpGUpC8Tlln4bfqF4XsuhWpSq5c7v898cWUGf9UaqzdWmpatkav9c5THoG1yghLEMkrKzMPMKhUgoWU8ETJSLfDEGEfzhFwxU4UrGHLco6E8z_MV6Zaf7HrcCuM2qqzfU_785yLqJNNFByEDJERmqSZbKLgYU4Ha6SGwV8WqovzEw0OvmF90OfK17fk0xTbRhjdhmmK27LdpIJAvLOnO98xIiDDysjK8jzHKjFUMVaT4AH9MHA4aUiMIQTnrcbVaIXUJOUGf8JWO7Km2zq25qgLzVvPSuH0VBlA-kmykt_EsJNeK3bKm3oCpX4NkvDkqW-IMH_bhLQgr2ZgJpYzw06T3W7n28vMTUOcHdJ-_bvKKlV6GICPAB8SJg7whKlO3nhs7W_fPnsdr2rBnHNAkJKDIFaHjApj85UM1CxCF98Mzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب گروه موسیقی پاپ «BTS» کره جنوبی در پاریس کنسرت ۸۰ هزار نفره برگزار کرده !  شخص رئیس جمهور و همسرش هم مشارکت کردن.
راه کره شمالی : موشک، جنگ، مقاومت ، تحریم، فقر، گرسنگی
راه کره جنوبی: احترام در جهان، تولید بهترین کالاها ، رفاه مردمش.
مردم کره یک ملت هستند، با یک تاریخ و فرهنگ و زبان مشترک،
اما در دو حکومت متفاوت!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6200" target="_blank">📅 09:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6198">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5132059c16.mp4?token=oP6NIBYDFzZpA58PpAJU5eYXKZ84_P5bibCf5GcK3S00vqRyjjcXgnY-4j0NqtOZBDicFdVz__CHqt0nAyCa0yv9kho9EBUuBmEdAf4tKCcPUV1WuiOtNbZNyqVsRLy0nCI1OJi3EXSZAFM5FZNbrMQxwuAzroQNggpE_qFJeEjj6CDIjDTadyRbI2_LMmOpftnWDUA7HwY_UvA1I9geL02pwbLxBvx5ia0NPFKS13P3RNeKfXG02pHM0U8mArGwpOcV80tx2GOLrU438pwvlfZZhCeWkIB2kbBgbNaJ70c0xWKLUYkK0BlL88IU7N_IiL6swV_CNILVl3AbiB3RbC7mXduxJJum6X9pfHNkWVPTPDV3_GbyixFW8lEVwtx-PiIlwMEmU7PkSXuXC6_L8P-0exMd7s_Z7R1swcBHKkgOx4EaJAUebGfXDCag7wD6qiM9Nu3TE2fjkZAHRwToKmFwL6oyR8OoaaY1n4aPTUEMoQ-RUPmrw7tjtVJ_xE1QnF4kn4ZLsRieTLCodptRtj_AScv1iUD9Fpig_fa7jB1y8d6WN5ILuIbiUXmoYClATkzLOAsX39_UNGCWOQ0-OXmC5qmztyKYU1dOX0BafsOR9rJyNmNpug-uGYDN8RGSu9Zc9m1-rqH0ID8kqEg8LUvIr-ljdlINQ8eGExpqKq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5132059c16.mp4?token=oP6NIBYDFzZpA58PpAJU5eYXKZ84_P5bibCf5GcK3S00vqRyjjcXgnY-4j0NqtOZBDicFdVz__CHqt0nAyCa0yv9kho9EBUuBmEdAf4tKCcPUV1WuiOtNbZNyqVsRLy0nCI1OJi3EXSZAFM5FZNbrMQxwuAzroQNggpE_qFJeEjj6CDIjDTadyRbI2_LMmOpftnWDUA7HwY_UvA1I9geL02pwbLxBvx5ia0NPFKS13P3RNeKfXG02pHM0U8mArGwpOcV80tx2GOLrU438pwvlfZZhCeWkIB2kbBgbNaJ70c0xWKLUYkK0BlL88IU7N_IiL6swV_CNILVl3AbiB3RbC7mXduxJJum6X9pfHNkWVPTPDV3_GbyixFW8lEVwtx-PiIlwMEmU7PkSXuXC6_L8P-0exMd7s_Z7R1swcBHKkgOx4EaJAUebGfXDCag7wD6qiM9Nu3TE2fjkZAHRwToKmFwL6oyR8OoaaY1n4aPTUEMoQ-RUPmrw7tjtVJ_xE1QnF4kn4ZLsRieTLCodptRtj_AScv1iUD9Fpig_fa7jB1y8d6WN5ILuIbiUXmoYClATkzLOAsX39_UNGCWOQ0-OXmC5qmztyKYU1dOX0BafsOR9rJyNmNpug-uGYDN8RGSu9Zc9m1-rqH0ID8kqEg8LUvIr-ljdlINQ8eGExpqKq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6198" target="_blank">📅 08:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6197">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔺
سپاه : به انبار دپوی قایق‌های بدون سرنشین آمریکا در بحرین حمله کردیم.
🔺
حملات ج‌ا به کردستان عراق</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6197" target="_blank">📅 01:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6196">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
وقوع ۵ انفجار در یزد
برخی گزارش‌ها می‌گویند که حملات در پارک کوهستان یزد بوده (منطقه سایت موشکی)
🚨
گزارش ۳ انفجار در اهواز</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6196" target="_blank">📅 00:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6195">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=cZ5g9NhlS4M_FAtna6hCbBw0tf9UVMafrYy5gN8BWX7_UfXTPmg_xfBHfBKxKTCmVWw73SJQgbVuz-G-d-x0KdNwbK8aJNBM0h5-PP06NMA6VGlyprcmEGCVcXqUzxv22B1S6PAsPRm3D3f_qyuNaAhC69nWYEzyOG9kmqBQZ7fGcBfmnJ-bwifID8dRsFklj4YA3IiU1GMV6lwSTPC2aCYLhB-nDCxSoOM8XWeFh-2tytUrBW8wbYybU0KjYHk-q6ywkctAvUTAyrccQSA7R9a_D-n4gd0A4SQEzZ2Dsv_uZ_W9X-uvYLIIx3YOT12gjWWvrokLPIv9KofmWHZrug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b38ca5f240.mp4?token=cZ5g9NhlS4M_FAtna6hCbBw0tf9UVMafrYy5gN8BWX7_UfXTPmg_xfBHfBKxKTCmVWw73SJQgbVuz-G-d-x0KdNwbK8aJNBM0h5-PP06NMA6VGlyprcmEGCVcXqUzxv22B1S6PAsPRm3D3f_qyuNaAhC69nWYEzyOG9kmqBQZ7fGcBfmnJ-bwifID8dRsFklj4YA3IiU1GMV6lwSTPC2aCYLhB-nDCxSoOM8XWeFh-2tytUrBW8wbYybU0KjYHk-q6ywkctAvUTAyrccQSA7R9a_D-n4gd0A4SQEzZ2Dsv_uZ_W9X-uvYLIIx3YOT12gjWWvrokLPIv9KofmWHZrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گزارش چندین انفجار در لار
برخی گزارش‌ها از حمله به سایت موشکی لار خبر می‌دهند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6195" target="_blank">📅 00:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6194">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LH0EuRSRn5MvEJMAXz8Pt5KZBBgyQjpU7pMj3he01WVnsUn1IeQCogiSnyD7jRlAPc50uPaNNGF1vwNDKYiWUkBXcDtaPaOqwLmgtDrYNABJYvNy91W_RSkXTld5nvCeUiyj710wF7zS81msQipRBPy4Nw94x4K_4xZe4FBWiCoxIplwwMKP3lKlfBXkBTjV0YKFGb3VJPPk0qsnWM9lEM6GN0SMAkzkGGDQ5JpfU5zlj2KHodVH2GN4sbgKKCzA61klMXgcEtWLuZujvXsyBcI3yNoJnPFvr0bn8Y52jJwAeyWf_eDDWJhJXP5wGkN3g4PTR1iLnsuYCp9H7-oSxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گزارش حملات ارتش آمریکا به بندرعباس، قشم، سیریک، بوشهر و اهواز</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6194" target="_blank">📅 23:38 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6193">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
سنتکام: ‏امروز ساعت ۳ بعدازظهر به‌وقت منطقه زمانی شرقی،
[۲۲:۳۰ به وقت ایران - یک ساعت پیش] برای هفتمین شب متوالی، یک دور حملات علیه ایران انجام دادیم.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6193" target="_blank">📅 23:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6192">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029791358c.mp4?token=CJCdMo_EiY3XZAmSQ_lYYmJPJIJRrNHjzZ_OcHYHzi0l4tB6MrFRjUUP3Ll10RwHkumeGkLL-TBoMbCMmFugFp8owYEgNNpHat8zkKwjYcDVUPsDqnNkt79PhCwAH58oRQ61XwF0ve0QzC68EcmjcHVGJDuf31bJAOV2Y2F9RzAXhn7dhkA9WwVidzUUgJGgkNxWPoQ7F85mj9xaZdUuD1mgYiTX-u3x_T-X1uE2N8ShaHK46IeO8Xedk1tnaHZbr5GE973hlP__ezeNMI3csVJZLDCfbVC5WGNIkkLydmmdCjCeUbMbcaXGz0CtKXPhleMz_1i8K-xBIOUwZzRHLLz-xbNZHSN-OR08I3izRNXbXAdhmnpfTs7F4v3wf33ARrCRgkyu3BejkJh-PLvyRN5F2OmPtNnNv1McYOvi9UfQWrz6O80u7Xm7Rv6x8oSax0Hue9rBVQv9uSrs4xpw2TBdWDGOfBTx1WRq5CdnykMSMMTycszbfAAYMn7cgIN3kdqT1Iv8GGJy9mqHQbncelKBmofp8OoQxpJZHK-kQ3dak7c3FXdcTIjYQADUPCK6NLv4Qz-TMzDz44mG4JBi3Og9L1tEdUpo4p8oMeYr7vrt9G6W0_MVBi_PH8o-apAQ5HLlvP2s9rzXRGDQT002EgrJEl3i4W9bYVKfK24_PxM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029791358c.mp4?token=CJCdMo_EiY3XZAmSQ_lYYmJPJIJRrNHjzZ_OcHYHzi0l4tB6MrFRjUUP3Ll10RwHkumeGkLL-TBoMbCMmFugFp8owYEgNNpHat8zkKwjYcDVUPsDqnNkt79PhCwAH58oRQ61XwF0ve0QzC68EcmjcHVGJDuf31bJAOV2Y2F9RzAXhn7dhkA9WwVidzUUgJGgkNxWPoQ7F85mj9xaZdUuD1mgYiTX-u3x_T-X1uE2N8ShaHK46IeO8Xedk1tnaHZbr5GE973hlP__ezeNMI3csVJZLDCfbVC5WGNIkkLydmmdCjCeUbMbcaXGz0CtKXPhleMz_1i8K-xBIOUwZzRHLLz-xbNZHSN-OR08I3izRNXbXAdhmnpfTs7F4v3wf33ARrCRgkyu3BejkJh-PLvyRN5F2OmPtNnNv1McYOvi9UfQWrz6O80u7Xm7Rv6x8oSax0Hue9rBVQv9uSrs4xpw2TBdWDGOfBTx1WRq5CdnykMSMMTycszbfAAYMn7cgIN3kdqT1Iv8GGJy9mqHQbncelKBmofp8OoQxpJZHK-kQ3dak7c3FXdcTIjYQADUPCK6NLv4Qz-TMzDz44mG4JBi3Og9L1tEdUpo4p8oMeYr7vrt9G6W0_MVBi_PH8o-apAQ5HLlvP2s9rzXRGDQT002EgrJEl3i4W9bYVKfK24_PxM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت شانه خاکی موقت کنار پل بندرعباس</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6192" target="_blank">📅 23:12 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6191">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏یک گزارش محرمانه که برای رئیس جمهور ایران تهیه شده است، نشان می‌دهد که تنها ۹٪ از ایرانیان از وضع موجود حمایت می‌کنند و تقریباً سه چهارم آنها یا اصلاحات ساختاری عمیق یا جایگزینی کامل نظام سیاسی را ترجیح می‌دهند - فاکس نیوز</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6191" target="_blank">📅 22:44 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6190">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:  ترامپ به ما نامه‌ای داده و صراحتاً نوشته است: «بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6190" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6189">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a688590cec.mp4?token=FkihivzgCbPsDSQNTMTVk3PPgkxD1AaIL4PClywHJAcpBLV0GaMZnml1yA1NrOAUs-xixib2rPoM9Isyi0IqsH2WqVMq735cdfYFo541Zge3BqNXGoR46bZ0Lgi_AIJ8bzxQX_uLy_m12Vwlusayp3AyI1VZWakAyOzcCWxhYNqeZUFrrPVhILJIERHlRreJVQHX2iuvKowNXWpuh66dcV5xyWbuRPV18YWGmFOWz1JLHTN7syJeIPKEmx4YRNRYAwIUOCNHIU5Jim85BZ6ZNwUyJC75TlA-VrAWpZepVrcbhl1NShr0UN_eLGt0iX6TVygmOoWicf5RMyAFqRUNew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a688590cec.mp4?token=FkihivzgCbPsDSQNTMTVk3PPgkxD1AaIL4PClywHJAcpBLV0GaMZnml1yA1NrOAUs-xixib2rPoM9Isyi0IqsH2WqVMq735cdfYFo541Zge3BqNXGoR46bZ0Lgi_AIJ8bzxQX_uLy_m12Vwlusayp3AyI1VZWakAyOzcCWxhYNqeZUFrrPVhILJIERHlRreJVQHX2iuvKowNXWpuh66dcV5xyWbuRPV18YWGmFOWz1JLHTN7syJeIPKEmx4YRNRYAwIUOCNHIU5Jim85BZ6ZNwUyJC75TlA-VrAWpZepVrcbhl1NShr0UN_eLGt0iX6TVygmOoWicf5RMyAFqRUNew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی در ۲۹ آبان ۱۴۰۴ گفت:
ترامپ به ما نامه‌ای داده و صراحتاً نوشته است:
«بیش از دو گزینه وجود ندارد: یا جنگ و خون‌ریزی، یا مذاکره مستقیم برای پایان‌دادن به غنی‌سازی و برنامه موشکی.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6189" target="_blank">📅 21:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6188">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGkJPV-ZKICMDvrdleTK8LDdxx9ndA8wUS1eA_cwzDueCrakqjzemIDplWhPKTLzmapf6VqVVAPZOS6ZTkdx94_YckVT-9QP-bFGqZV7k2ZuhDypkT2BIWbZNVcfzpv-8KMU1Z2LNeHEmY7QkLle8Ocb1yS25pH-02-Zu1Fj7r7bKd3anyirnnItIepd6cWphpyyEjGOq50GAnfVF99OUmETKdqIhb6URb7jCsZt86o8dVVvIUZBZuvdYxEokAy1wYde9i3fzWeA4tAjr4CbpyniPOcXJp_IP2OK4I5xZCoqEJWtneW8M76r3n1qq-xmog7G8ayUsjXwzLHRKy-PtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsd4NVa289lCxvTSgVsoUhMebmyo2v88-IPDM9Y3YB0jb6H8tnCCEIxbXStvZEVUZaxnNg1Ivog4xV2jYmNfQGT7G568vjanKoNipUkcFH4pp2K4ak6dr0nkGCbFlu2TTpAw1Lvay82ZnnQYAE-Z5c4Qxbe4FghbNmj5ndHJ2XhIqIqdsikDXc0jbjOvm1M000kxY5_pcAnLF8UmjyF1VHP0ut6vB4F9fgewKdxS20J_ypok4rBRDAmAO3FiUXN6fkGZwCt0kjbRuGMQg7LnXmHQigFYC_LfErC-kMaeTniJW9tUmgSLaDH0s4wPHMdAxwx170LuEmYcb3Mzl4C66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب طلاقش بده :)
چرا اینهمه کینه؟</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6187" target="_blank">📅 18:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-6186">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKcNiymA7URFg_rTix5cbnaAo9W0ZQwE8clCFT-G1pyhJg0X7nqNcqyL-mXiQxUYkVcOtUHfgpi4yyFmdWkai_VECP-JwuaiivwwsfG7LCwLM3QFonzIrWwQzvkfXi5BK5QfM80DVt40CfWAVc1KLc1O0f74Qkwr0Jj__lMxlkH1_G5ddYSyVaLy_Bcd-DXSl3MPSStfgu2p7tzjIgC-hVIkiDp08mCsBFYv-UkGmu31lJcZO5pgzYPJl_ISPVw-VER1t2cOXTOUoEieMZUzHX2DkfKb8aeysIhddWyCnIHvyeWNLKo7Y9zgK2FK_YtqCBmGM3ANijRWBj4cmDTXMA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JgaEOsSSibqOUoQ6WFU1BYKkvK-WoO0ohbJdlROkSRieongQJ-FWe03CN7mPK6-YXbph6eBhy7aPdjxkzKhGN7GSktm5WDZnM1sAkFKNMW-wpeaJrGGE5uTVCrWs8DbatUxhqM3Nr2LT7gd3twxMaQ4aKOkDN77cA6NlDyvGZA-L7pnCopP-pVKMjqxodelXYMVqM2p0Knm06eQpiwRjkjH3oVk7_aipJ7kKOEZTucI1-gDQeAdl0EvF-L13jMjiCCDieQFLoPaDhi0Idi3-G4I-eCF-PR0UfiuyMhHkTSSNLX9O21EejlUGGrmUowLty5FSl59m4tJS5bZEj_6SB8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d213b51da.mp4?token=uPfrkKk8qYizG85BR1VSbl9IWLI-rvnGdT79fD90EKwOsa-JZHUFfT1bF62TLgyy2fQvaAxGqAn0SD5Ls_72TBBDgS9biyzk2o4Sn3ezOvu05dsALNLZiflvH9Jwkc-uQTfkucSVvj-XGwObOQ27LaGHT4M-KNIheZTvJAslpXucMOWANBxUJAG3gZnJ4ckWB128nqx8WH1C8WS6y7bIfrTRCNxmC_RrWBrDyixJJ0wvxcXnp1y-55lLOyPJkBa21jdAtAcjuMSJKZhuklrKEHk3Gnu9jC5QLJEFu6SS22WgvOHsAA61iaSpLRYZnzfjAcTsgBC-ph6d833v-Pm7JgaEOsSSibqOUoQ6WFU1BYKkvK-WoO0ohbJdlROkSRieongQJ-FWe03CN7mPK6-YXbph6eBhy7aPdjxkzKhGN7GSktm5WDZnM1sAkFKNMW-wpeaJrGGE5uTVCrWs8DbatUxhqM3Nr2LT7gd3twxMaQ4aKOkDN77cA6NlDyvGZA-L7pnCopP-pVKMjqxodelXYMVqM2p0Knm06eQpiwRjkjH3oVk7_aipJ7kKOEZTucI1-gDQeAdl0EvF-L13jMjiCCDieQFLoPaDhi0Idi3-G4I-eCF-PR0UfiuyMhHkTSSNLX9O21EejlUGGrmUowLty5FSl59m4tJS5bZEj_6SB8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا بودن شعار به زبان عربی میدادن؟
چی میگفتن؟ میگفتن  سرباز ایران و وطن هستیم؟
نه میگفتن «سرباز دین و عقیده» شون هستن!
و کنار لبنان هستن! و مسیرشون همیشه مقاومته!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6185" target="_blank">📅 15:24 · 26 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
