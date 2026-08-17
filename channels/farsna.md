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
<img src="https://cdn4.telesco.pe/file/Xv_Fisb2B9Gc4S4juiSUqUljC5omq2RpA4QBEO3OEyqu2DKfYoX3KieZ8feykro9bJ_cBkDhA-ZLBcoWTYTS0lMjMoN0vlYMoEkj8Q1uXdZdQoszwpF4y_WuvRoXC9roPbm463h6AQEwbnEdGMsVIqmAItV6jaHSrKqL-uF3Uo_V3kLTU5SWGhaoO03DQpFID-UUMN11FZNIB6t2Wh26RByFnMJwUnDYRJfGsfGI2wgMbhQP_ApVIuBNpukjNOo4TBI66Vi_z5nJjacRxQka0sCar-j8wHleS4LnlR1RSmAK0_Ihn4kIGC_0vDmGZqZhGSb5f43_b1c8Tqtt45sT1g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.81M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-26 21:22:11</div>
<hr>

<div class="tg-post" id="msg-456627">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">داوطلبان آزمون بانک مرکزی گرفتار اختلاف ۲ دستگاه
🔹
۹ ماه از اعلام نتایج اولیه آزمون استخدامی بانک مرکزی گذشته اما سازمان اداری استخدامی و بانک مرکزی هر کدام دیگری را علت تاخیر تعیین و تکلیف متقاضیان معرفی می‌کند.
🔹
سازمان اداری استخدامی امروز اعلام کرد «مشکل ایجادشده مربوط به خود بانک مرکزی» به‌عنوان درخواست‌دهنده مجوز است که مصاحبه‌های تخصصی را برگزار نمی‌کند.
🔹
بانک مرکزی اما به خبرنگار فارس می‌گوید که علت تأخیر، ایراد در سؤالات و کارنامه‌ها و شکایت‌های متعدد داوطلبان است که به سازمان اداری استخدامی هم ارجاع شده اما پاسخی دریافت نکردیم.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/456627" target="_blank">📅 21:24 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456626">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c22cad8fc.mp4?token=UDq1XgzrpkBuJcVdbeoa6c1yeDDh3JFkmEldru1PwN9zTqKMNqgBAHoYhP03dooGa3cCiqDU9aw489e72TsYSOCx5cV6HWJ_cbneaC4y2miH8UBZlTOn3QAYeEKSIBR9nm1u6IlG66f9piOt5netA6es0bqyxnke0ZsPicRBVEPbIUm3OAthU2eQvmJgPmFOyVOCXhEIPmIRWjY0t0INr8QBqbDoDpI7d1mB582rloiU0-sXCKSiR8mx55lAkgWkH8oZ-3b5j0BfEzVd2xmz2xRdVUJYhL8DuaGBmHvJj--XEB0yXg7pOvr8tcPwGNXL9hzirUAZ_8N4Uoz0pkH9oiTJt25L7DUu3J_qLctEAauKm4pl-B5mcfb-ubKmhaJQFFY2aBT5pP9vHuTJ3OBepfezLGgyLVwHAr4e9t2_qZm7t4dE9OmWHohw248qxcnNj8z9ZjqU8KgpwDE00ZW4DIWM8-zpV-vbr1ytKOh7XNSjHY5DEWnr4LSApiisuE9wGz7vPwf2FunoIo_Bk6A1_nyVj7BfIzzywjO-xSpsujan7SFYcy_QbttKgRh4CgYh5c0IrBmaGcU7wmCoNQNup49TvGcO0hsaKIEQ8_clny6mUzrP84DpNbymxvY-yJ2E7-FTE0UuRRpfuIyjbW-MEN2kufH_V0U7kTbUcUqOkzo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c22cad8fc.mp4?token=UDq1XgzrpkBuJcVdbeoa6c1yeDDh3JFkmEldru1PwN9zTqKMNqgBAHoYhP03dooGa3cCiqDU9aw489e72TsYSOCx5cV6HWJ_cbneaC4y2miH8UBZlTOn3QAYeEKSIBR9nm1u6IlG66f9piOt5netA6es0bqyxnke0ZsPicRBVEPbIUm3OAthU2eQvmJgPmFOyVOCXhEIPmIRWjY0t0INr8QBqbDoDpI7d1mB582rloiU0-sXCKSiR8mx55lAkgWkH8oZ-3b5j0BfEzVd2xmz2xRdVUJYhL8DuaGBmHvJj--XEB0yXg7pOvr8tcPwGNXL9hzirUAZ_8N4Uoz0pkH9oiTJt25L7DUu3J_qLctEAauKm4pl-B5mcfb-ubKmhaJQFFY2aBT5pP9vHuTJ3OBepfezLGgyLVwHAr4e9t2_qZm7t4dE9OmWHohw248qxcnNj8z9ZjqU8KgpwDE00ZW4DIWM8-zpV-vbr1ytKOh7XNSjHY5DEWnr4LSApiisuE9wGz7vPwf2FunoIo_Bk6A1_nyVj7BfIzzywjO-xSpsujan7SFYcy_QbttKgRh4CgYh5c0IrBmaGcU7wmCoNQNup49TvGcO0hsaKIEQ8_clny6mUzrP84DpNbymxvY-yJ2E7-FTE0UuRRpfuIyjbW-MEN2kufH_V0U7kTbUcUqOkzo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رمز پیروزی؛ میدان را ترک نکنیم
@Farsna</div>
<div class="tg-footer">👁️ 344 · <a href="https://t.me/farsna/456626" target="_blank">📅 21:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456625">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ادارات فارس چهارشنبه دورکار هستند
🔹
به‌علت مدیریت مصرف انرژی، ادارات و دستگاه‌های اجرایی استان فارس سه‌شنبه ۲۷ مرداد از ساعت ۷ تا ۱۱ فعال خواهند بود و چهارشنبه ۲۸ مرداد به‌صورت دورکاری فعالیت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/farsna/456625" target="_blank">📅 21:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456624">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ed9861801.mp4?token=bqrW53bfjYDDeCZYPnhpb3CUN5Dl51X-jBRl969_lF3_X2kaheZY7UFXG8fnNIWRp_0NmkYTpNvKJoGyr0XKTJ8scxm6n1MPnougGDBHKtJr6I5XW409ZjRueMRsBaGgdN2ltRCpNUmFqDitJ2ep4g1AM4A8FVSgLNMQVcr-lyrXBmXI6f_hnFBdW05Sv-BR0NLISdV87VdpYf5mhDP8xG_t0mOP_r-s4-CHJN7lRLVDLjGK7UHO4zJRhT8kURLB54FT4CfGKPMCcPHBSPOYzNhkyvHWGb8AIoytX5JAZEIm0YBUr92vDdjXSqBFscoqv3pqyh_ww5ILnPBWGYEm1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ed9861801.mp4?token=bqrW53bfjYDDeCZYPnhpb3CUN5Dl51X-jBRl969_lF3_X2kaheZY7UFXG8fnNIWRp_0NmkYTpNvKJoGyr0XKTJ8scxm6n1MPnougGDBHKtJr6I5XW409ZjRueMRsBaGgdN2ltRCpNUmFqDitJ2ep4g1AM4A8FVSgLNMQVcr-lyrXBmXI6f_hnFBdW05Sv-BR0NLISdV87VdpYf5mhDP8xG_t0mOP_r-s4-CHJN7lRLVDLjGK7UHO4zJRhT8kURLB54FT4CfGKPMCcPHBSPOYzNhkyvHWGb8AIoytX5JAZEIm0YBUr92vDdjXSqBFscoqv3pqyh_ww5ILnPBWGYEm1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی دروغ، جان آدم‌ها را نشانه گرفت
@Farsna</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/farsna/456624" target="_blank">📅 21:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456623">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f739732d28.mp4?token=cIB5hzZhQIeyhGm03TgA0nmnYki5AVv-V3uEtwW25phZEZRtbYlVBQwoajyLEYMsmB5ApsE1qmZRcp1NaSdmVXlZzxCa0rBwdGynO1XcmZLvRYlWWyYBxBwkQZaQZCx-bR4GILlMKJH_NAhYa57eOiSD5OSSwdzOeXxUwJg9fjCZlg5rhBtNKUDomhKKY_-PG9izXV1xzLNpyZeALtTUMbfQkJYwtdPSzsDgtCh5aJPXN0SOoa0eo0NKCmnyhZtgd03AR8VKQ9vrIC5Kl5cn5g5D1x_C8iyy6YAAHPYlLPRLXQPcXy7RpCBa-qnWkf5tBPwrFGr6kLFYyOEFy4TAPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f739732d28.mp4?token=cIB5hzZhQIeyhGm03TgA0nmnYki5AVv-V3uEtwW25phZEZRtbYlVBQwoajyLEYMsmB5ApsE1qmZRcp1NaSdmVXlZzxCa0rBwdGynO1XcmZLvRYlWWyYBxBwkQZaQZCx-bR4GILlMKJH_NAhYa57eOiSD5OSSwdzOeXxUwJg9fjCZlg5rhBtNKUDomhKKY_-PG9izXV1xzLNpyZeALtTUMbfQkJYwtdPSzsDgtCh5aJPXN0SOoa0eo0NKCmnyhZtgd03AR8VKQ9vrIC5Kl5cn5g5D1x_C8iyy6YAAHPYlLPRLXQPcXy7RpCBa-qnWkf5tBPwrFGr6kLFYyOEFy4TAPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس سازمان نظام پزشکی: مردم به‌ تبلیغات فضای مجازی در حوزهٔ سلامت اعتماد نکنند
@Farsna</div>
<div class="tg-footer">👁️ 1.34K · <a href="https://t.me/farsna/456623" target="_blank">📅 21:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b19927a3d4.mp4?token=Kp0UOJSInmWKBYuIYgE_c0sUoEDJyZRFEGP4g0Ep5xOBKttJxXfTcB1d29kI7HwqMnvLlqKwbSGjcIU2l5VFNSho_FDgzGqBsPBDEMzr4hOnZnpnCV_y1HtZi9uR-47uihl-uZbwlglaN4JvPBrGIHylIIXcpV3Yhz2k6QYlg3Pr7VTJXRtbzodZTBMZ3-XNnnmRmu9fDRjsEfG5VLbs2Tt7qJBBCTWg-Ejd7O5muoyPUzx9Qsal6qGde_fDSFXNrbOWXeZzbCDhLJa5nMqwOCnfI74rUfTuHArq_wfsXz7oM1QtFjFS_ygOdbKHTTL_iM4u73k4wk9LIj1Yyq5pojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b19927a3d4.mp4?token=Kp0UOJSInmWKBYuIYgE_c0sUoEDJyZRFEGP4g0Ep5xOBKttJxXfTcB1d29kI7HwqMnvLlqKwbSGjcIU2l5VFNSho_FDgzGqBsPBDEMzr4hOnZnpnCV_y1HtZi9uR-47uihl-uZbwlglaN4JvPBrGIHylIIXcpV3Yhz2k6QYlg3Pr7VTJXRtbzodZTBMZ3-XNnnmRmu9fDRjsEfG5VLbs2Tt7qJBBCTWg-Ejd7O5muoyPUzx9Qsal6qGde_fDSFXNrbOWXeZzbCDhLJa5nMqwOCnfI74rUfTuHArq_wfsXz7oM1QtFjFS_ygOdbKHTTL_iM4u73k4wk9LIj1Yyq5pojzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تفاهم‌نامهٔ اسلام‌آباد به پایان مهلت رسید؛ چه اتفاقی در این ۶۰ روز افتاد؟
@Farsna</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/farsna/456622" target="_blank">📅 21:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08d7c9ebcf.mp4?token=vadg_ZMCy2D7nfWH10CkSHXpNop4Z2hx9mEc0koXZZwRo5gi9uAU0OEQlyKTsobfBa8o2IwoZlrDUTT-Qm4cXqv480CEIvEcHccrPLtgLAMYuedijSmhXlwykMbdJxGhG7BTOflcNSWJLigNXR20Vyb_CR2W5fgQPPryBfs6gMUBpcmYouEazCLBt21Mq16MzIU9QPkxH0e34dCCnrHlPzNFt1-LpJ-FmGSJ2GzhG5FQQxnsftmdPmYoJ3lzBX3AXxfNNvx84wTfc44f0Rzt7EwG9liY_nShfFyigYcITYg4L_vLcuoA9lH1URqjaG9O0-sTUM105xa8li5HNht9dbaFlkbvMJXDBGGnLhiNSJGsDwZV7mp2uIkfL8ozsi5IltymLrsh06vpOm0oSSLr-3_1D4Xh09lug9aF-Swa-1lBuk4tCDUFkp1_k7gbZY5DcQnMh2WuGKuxRat5oyl3JgUmGnz3myXio4zoMl7UjJvDQnWxvMwcIVTGI5q89AyotStC7h8bH98ZpOTbVJgWQ3OwGq575ABE71Mrf1-RHIup_XBRemy6j29rlJ4jvoLBXfDFNg0KZhPRKA12j8Dqy8PB_CdC-OhRGzigpFfaKcKgxz-si39CJb4rN5ETUXE-Y9-d9qcU-zfHaJZ1bPrd_fqEMX0wMqWP5ugf1rsNAsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08d7c9ebcf.mp4?token=vadg_ZMCy2D7nfWH10CkSHXpNop4Z2hx9mEc0koXZZwRo5gi9uAU0OEQlyKTsobfBa8o2IwoZlrDUTT-Qm4cXqv480CEIvEcHccrPLtgLAMYuedijSmhXlwykMbdJxGhG7BTOflcNSWJLigNXR20Vyb_CR2W5fgQPPryBfs6gMUBpcmYouEazCLBt21Mq16MzIU9QPkxH0e34dCCnrHlPzNFt1-LpJ-FmGSJ2GzhG5FQQxnsftmdPmYoJ3lzBX3AXxfNNvx84wTfc44f0Rzt7EwG9liY_nShfFyigYcITYg4L_vLcuoA9lH1URqjaG9O0-sTUM105xa8li5HNht9dbaFlkbvMJXDBGGnLhiNSJGsDwZV7mp2uIkfL8ozsi5IltymLrsh06vpOm0oSSLr-3_1D4Xh09lug9aF-Swa-1lBuk4tCDUFkp1_k7gbZY5DcQnMh2WuGKuxRat5oyl3JgUmGnz3myXio4zoMl7UjJvDQnWxvMwcIVTGI5q89AyotStC7h8bH98ZpOTbVJgWQ3OwGq575ABE71Mrf1-RHIup_XBRemy6j29rlJ4jvoLBXfDFNg0KZhPRKA12j8Dqy8PB_CdC-OhRGzigpFfaKcKgxz-si39CJb4rN5ETUXE-Y9-d9qcU-zfHaJZ1bPrd_fqEMX0wMqWP5ugf1rsNAsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عاشقان امام رضا(ع) بر سر یک عهد مشترک
@Farsna</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/farsna/456621" target="_blank">📅 21:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32cce87104.mp4?token=Jahyky5nOKaNiXAGjbKv2UHkaScorAZ471dOZvkHlkCFTqL86AEojTGAS9I1UawPm38KZaBXa2NqKuApQHtElJFFjmxzGXpDBkwlGPo3pl7RnnBlW3RIonhtH0zdyYA8akycUVEiEz9f8jpMr8km00Qek9pb1cfdBQA4yLwVYXsNLXUSjd-MEZ6nnB_N2lnuAtye_joF-2D7GZ8CuGglRVYoCBZ7A-xOprfnM0g0H7bn-uI1LQK07KHuSlaFV_0ivvcy3bV5vMKo1SGEAyg7bk8_Aur_UkkjUAU9apbwQ5r0m67wx4_81qMteKXbaIZKftp7FbUlZoQuoxd6DFplwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32cce87104.mp4?token=Jahyky5nOKaNiXAGjbKv2UHkaScorAZ471dOZvkHlkCFTqL86AEojTGAS9I1UawPm38KZaBXa2NqKuApQHtElJFFjmxzGXpDBkwlGPo3pl7RnnBlW3RIonhtH0zdyYA8akycUVEiEz9f8jpMr8km00Qek9pb1cfdBQA4yLwVYXsNLXUSjd-MEZ6nnB_N2lnuAtye_joF-2D7GZ8CuGglRVYoCBZ7A-xOprfnM0g0H7bn-uI1LQK07KHuSlaFV_0ivvcy3bV5vMKo1SGEAyg7bk8_Aur_UkkjUAU9apbwQ5r0m67wx4_81qMteKXbaIZKftp7FbUlZoQuoxd6DFplwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شکست استراتژی امنیتی اسرائیل در مقابل ایران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/456620" target="_blank">📅 20:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PibKWO4hBmFVimvxaOpTvUAF85DPEBYo4mo3Q13uBSnEpw7vz-lB7Gj0OEY577kuWIljEq376pMD4wE7OKjqVw3cgUaJcADtsjE8W6xKZjkptA8wfZQL-x9lM7kUyXR8L2OtJ81ME-4wX0aAA3YaS1y89f-OoBzEaApiMveHtq_NTDrS-PlOoN9ctQVPXiCaWRMsAHJXqJG4PwWprCPqrpK4kBTYeZZVZBReFqfu97uGEyWm9CK-Vykz2tQkQg3eOCWpOdCQUPLX_wBLBoJKqMK9EFtHIZEU7arcoXOdo6OoqsEpP3qoxqQPAIGOGHu0spH4obTAFQFPvjk7CvA04g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
دیدار غریب‌آبادی با همتای چینی خود در پکن
🔹
معاون وزارت خارجۀ ایران امروز در پکن با معاون وزیر خارجۀ چین دیدار کرد.
🔹
۲ طرف در این دیدار دربارۀ مناسبات دوجانبه، موضوعات امنیت منطقه‌ای، وضعیت تنگه هرمز و همکاری در مجامع بین‌المللی به گفت‌وگو نشستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/farsna/456619" target="_blank">📅 20:56 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7778e2e9.mp4?token=c3jvA9dj-se3nyQsYyq-JER69V-euMUCfGhkdYx7ICqBjwB-HuAfnlo_eSS852jZ7Id3iISdATnMRc-tQ2l-gvgsIOmX6_ReGeZ_MB5rTshrVgmxC7PkCoL7Q6e298cJHFEZ8_6U3USOaKuG0Zd0VLcqIjyN8waQUHp26Xc8ZnF8fl1qDSHrDSHjQ-_MWiI4_y0pX-MCfUDH4Q0ewkWHimJIUJELOU_BhSMHRFJIZznlmBpapFenf7tYIuWkJIuaVywmhM8hHekf1Cd4XeA5Y6AavTfbNxXIKYBLPp2hTEQJ-HFsmAM_EvNB0KdzG0hmwSUTlY3NHSrSPiQX5zgJBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7778e2e9.mp4?token=c3jvA9dj-se3nyQsYyq-JER69V-euMUCfGhkdYx7ICqBjwB-HuAfnlo_eSS852jZ7Id3iISdATnMRc-tQ2l-gvgsIOmX6_ReGeZ_MB5rTshrVgmxC7PkCoL7Q6e298cJHFEZ8_6U3USOaKuG0Zd0VLcqIjyN8waQUHp26Xc8ZnF8fl1qDSHrDSHjQ-_MWiI4_y0pX-MCfUDH4Q0ewkWHimJIUJELOU_BhSMHRFJIZznlmBpapFenf7tYIuWkJIuaVywmhM8hHekf1Cd4XeA5Y6AavTfbNxXIKYBLPp2hTEQJ-HFsmAM_EvNB0KdzG0hmwSUTlY3NHSrSPiQX5zgJBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.66K · <a href="https://t.me/farsna/456618" target="_blank">📅 20:54 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IvfOiLrepdKlaPJsy-pPtC34WiuU0sgBYhaHrmV1vHCYgqMdJHPgNq7bkF5kl5J_h9mmD5xhCPTxdeFpYX4Nz6mNqj8v0gM3ZFrW1LNVeTfwd_7z0enJW-6cmOJhhfiI25pIiDzSR6_fKHc-B09rNkZOJB640KSpF2r_QAfi5A_yCjM2ZQfDA7MBJLQ_FbFH-porKKpJLHCYIHq9PJPbdkR0xQW4ZhQLdLYNLxuZ5U-x20-4rbfeKBrTyXCROYlsXPoLAt6LtyD-D_6Vbbq9jd3eZN-BeDfB6aRO8C3RrTsa8QdqdsMTxP_7qsKwJ9gMoSf7ATH-SPLH37J1JbuwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ادعای مسرور بارزانی: پهپادهای ایرانی دفترم را هدف قرار دادند
🔹
مسرور بارزانی، نخست‌وزیر منطقۀ کردستان عراق، مدعی شد که دفتر شخصی‌اش در اربیل هدف «پهپادهای ایرانی» قرار گرفته است.
🔸
این ادعا در حالی است هنوز هیچ منبع رسمی ایرانی چنین حمله‌ای را تأیید نکرده…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/456617" target="_blank">📅 20:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ce-l6Dxm0r52Tf42_4vjd2ljdfOUcYLtQLJOqFw8HiRghNX-a-HFeyDa2vvsX3ukhNNvtEkEOvgbCg0hFgBWBxt-6lrz41yd4pbN-qQEQf2HvIcoN9t3wDKe7v4zmwgKjaTAJXszbWoHLsIqCu29uOPM7YWG6VWNGJ0rfrcVfBycWFkoFc6vkSu-jugA2tuPqzDy6U9AFszy1_i0IHCRl1HKaOWBEIV4kzljitcuEgntbIwEYDvK5jPGAeXYO3OqU4HUbzKhPVCvB7GSEQUuQiHKHdp9n8EaCauz3k42Hp9vLAaqE29zsLliae-IoXRqsO9Wb1MEATs80nU6OJ1CIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلای کنوانسیون‌ها بر سر ایران؛ از پالرمو تا خزر
🔹
درحالی‌ عباس عراقچی موضوع تعیین سهم ایران در کنوانسیون رژیم حقوقی دریای خزر را به آینده حواله می‌دهد که یکی از مفادی که همین حالا در کنوانسیون وجود دارد، ۵ سال پیش نقض شده است.
🔹
شهریور ۱۴۰۰، بند ۶ این کنوانسیون که می‌گوید حضور نیروهای نظامی کشورهای غیرساحلی در دریای خزر ممنوع است، با برگزاری رزمایش مشترک ترکیه و آذربایجان در این دریا نقض شده و خطیب‌زاده سخنگوی وقت وزارت خارجه نیز نسبت به آن اعتراض کرد.
🔹
با این وجود عراقچی می‌گوید «بحث سهم ما از دریای خزر در کنوانسیون رژیم حقوقی این دریا اصلا مطرح نیست»، خط مبدا و تقسیم بستر و زیربستر به دلیل اختلاف‌ در مورد آنها از متن کنوانسیون کنار گذاشته و به مذاکرات دوجانبه یا سه‌جانبه میان کشورهای ساحلی «موکول شده است».
🔹
این نخستین‌بار نیست که کنوانسیونی بین‌المللی قانون می‌شود اما حقوق ایران با آن محقق نمی‌شود؛ نهم مهرماه ۱۴۰۵ پرونده لایحه الحاق ایران به کنوانسیون مقابله با تامین مالی تروریسم (CFT) پس از سال‌ها در مجمع تشخیص مصلحت بسته شد و مجلس این قانون را ۲۶ مهر ماه به‌صورت رسمی به دولت ابلاغ کرد.
🔹
اما دوم آبان ماه گروه ویژه اقدام مالی (FATF) اعلام کرد این کنوانسیون که حالا قانون ایران شده با استانداردهایش مطابقت ندارد و هم‌چنان کشور را در فهرست کشورهای پرخطر یعنی همان لیست سیاه نگه می‌دارد.
🔹
حالا کارشناس روابط بین‌الملل، داریوش صفرنژاد می‌گوید که از نظر حقوقی و مستندات تا زمانی‌که وضعیت بستر و زیربستر و خط مبدا تعیین تکلیف نشود، تحت هیچ شرایطی نباید این متن در مجلس تصویب شود.
🔹
او می‌گوید اگر هر چیزی را در سطح آب بپذیریم، در آینده، در صورت بروز اختلاف با این کشورها، همان مبنا به بستر و زیر بستر هم تسری داده خواهد شد و حتی می‌تواند «زمینه‌ساز جنگ آینده و اختلاف‌های جدی باشد».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/farsna/456616" target="_blank">📅 20:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktadaXCTf9zTJLA5mJkiXp9vlZXEEl11SH9-ngnXzS08pgVki-Yovdu91JOZ3B1q-KAHr-n8Bb6kxdnYd7oYyzfSx4YHrfSEhYjtwTZXbvniPs_MPX39IIZHmgwSPV5aEupPuEzpQsLZIMQkiZYDaW7aKyb8V_x0hIeqE53ixLsOFuYbrBm1gtbcs2ymjII1dCZjtmeEtubomSqv8EsvPEZXUHQPx2hay7IpA_Z72huonHNJURkAJuvwxkwCssDUNgnSi6Gvo9Gao74gPpEeVuizrAYhXi4mSlFQE2On7OesrtmNPy29jdDoLkFL45HKqBEcmw0JitW9EoKwvdmogg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا خواب بعضی بچه‌ها ناآرام است؟
🔹
ناآرامیِ خواب کودکان، معمولاً یک «انتخاب» نیست؛ بلکه واکنشی است به مجموعه‌ای از نیازهای بیولوژیک و روانی که هنوز به درستی پاسخ داده نشده‌اند.
🔹
از دیدگاه علمی، اولین نکته «ریتم زیستی» است. سیستم عصبی کودکان هنوز در حال تکامل است و «ساعت بیولوژیک» آن‌ها مثل ما بالغ‌ها تنظیم نیست.
🔹
وقتی کودکی بیش از حد خسته می‌شود، مغز او به‌جای فرورفتن در خوابی عمیق، دچار نوعی تحریک‌شدگی می‌شود؛ مثل فنری که بیش از حد کشیده شده باشد و ناگهان رها شود.
🔸
اما نیمهٔ دیگر ماجرا، «دنیای روان‌شناختی» کودک است. خواب برای یک کودک، نوعی «جدایی» است؛ جداشدن از بازی، از آغوش ما و از جریان زندگی.
🔸
برای همین، اضطرابِ جدایی در شب‌ها خودش را بیشتر نشان می‌دهد. بچه‌ها، برخلاف ما، مهارتِ پردازشِ هیجان‌های روزانه را ندارند.
🔹
در واقع، این ناآرامی پیام یک «نیاز» است؛ پیامی که می‌گوید: «من هنوز بلد نیستم چطور آرام شوم و برای این کار، به یک روتین معنادار نیاز دارم».
🔹
این‌جا همان نقطه‌ای است که نقشِ ما پررنگ می‌شود.
«
روتینِ قبل از خواب» فقط یک اصطلاح تربیتی نیست، بلکه یک «لنگرگاه امن» است.
🔹
وقتی هر شب، پیش از خواب، فضایی از آرامش، نور کم، یک داستان تکراری یا یک نوازش پیوسته برقرار می‌کنیم، به مغز کودک سیگنال می‌دهیم که: «امن است؛ می‌توانی رها کنی و بخوابی».
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/farsna/456615" target="_blank">📅 20:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W69G9fPhcuCoMZwPgbZNf4FTa-9lkN_D3yDJqWHqDV0Fq_DsevJN3kvpuxoEetUWrvilPD_50wufgjNxGJUexMlEvoyowiJYHbgRbQp2nyFweycVnIjioKfL7PTVYchbm8E_2r2KnHY2p0O-dNpWr10Ezt43O3ScHeYHm4EeGyG7p7kgGIwpGWJyPYC4dUEqDjVsY31l_TBoG0VYx-zSmkvhjdHC8lGB_8JVVTz0FVmdxaghTz73FFTx0y1uzkmRBvkxtQ8Vs4uWdfwfHNhpL0VaaI06XPF1jItS7viL224eEJ13Rp9RHC8ksQAzRhbMxtADIP8pydxU_s6OfLv3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
باتو در عهدیم تا صبح ظهور
🔸
مراسم چهلم آقای شهید ایران
🔸
وعدهٔ ما: سه شنبه ساعت ۱۷، مصلای تهران  @Farsna</div>
<div class="tg-footer">👁️ 3.56K · <a href="https://t.me/farsna/456614" target="_blank">📅 20:31 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/925bd4fa5a.mp4?token=EpMUWl5ouhXs31HoxURrcDuNVVh8v4EoIAtBwlNqQR_24JI5LBJaZ7Z5FOGFc79k7TgXHY9838_Qx1apJEksh-12NHYMVike9aqOJOXRxaiLuztdklj0HGTjCGazFv10M_bSipkt4csKuMiX4W4tR_tlSTnpgi8xxWTuxGakau6F98VFez9iaAPFoxtR92dAYsF-zhlZ9GjhMdqw7JFgcwC7h1ct3_JodIi5RFzwJEBzbY6BUdYq2i_ESUlsXkf3faVpWDi3aDiQpmgWpPpAoTvcrXoKgXbixQJcnNiSxW_4ewAM_x7t-0ycclSGv48Yu01kyVW2jdTt7r_Xzb4djw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/925bd4fa5a.mp4?token=EpMUWl5ouhXs31HoxURrcDuNVVh8v4EoIAtBwlNqQR_24JI5LBJaZ7Z5FOGFc79k7TgXHY9838_Qx1apJEksh-12NHYMVike9aqOJOXRxaiLuztdklj0HGTjCGazFv10M_bSipkt4csKuMiX4W4tR_tlSTnpgi8xxWTuxGakau6F98VFez9iaAPFoxtR92dAYsF-zhlZ9GjhMdqw7JFgcwC7h1ct3_JodIi5RFzwJEBzbY6BUdYq2i_ESUlsXkf3faVpWDi3aDiQpmgWpPpAoTvcrXoKgXbixQJcnNiSxW_4ewAM_x7t-0ycclSGv48Yu01kyVW2jdTt7r_Xzb4djw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در نزدیکی مدرسه‌ای در غرب کابل
🔸
منابع محلی از وقوع انفجار در منطقه دشت برچی در غرب کابل خبر دادند. این انفجار در نزدیکی یک مدرسه خصوصی و هنگام خروج دانش‌آموزان رخ داده است.
🔸
تاکنون جزئیاتی درباره نوع انفجار و تلفات احتمالی منتشر نشده و طالبان نیز…</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/farsna/456613" target="_blank">📅 20:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/456612" target="_blank">📅 20:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c53a4c455.mp4?token=r2Xo5ZYs9nWsmTFBDZs-1xCYuQUaMzRwwnaBrCaSS0w2kgTBVNXbcnEuWLpV7-7c7N0vsVjJMo2rSeYyVH9Or35BRJgbFcvi8pQJg4Vj0phhirrlGI29NCahPpjcpKc_uWowVbUi9NrlDWKJM0013FOEK9gwqjFbRD5WHoxQl1acdoO5syhz5pL7KQfnCcJ1pXtG3hlKa-5GaHVwa_nNLfKQlV1XEouabl0mvEojKnqjKeYwAdhjGcruZxsBfGTHxOeVhrm9m76t4TggzzIMWFiLa1QxXx99T9D6Za5hD9C6JNARw4MgpL6jrHBtLYIsjb0NxON5bbr5q_M-c1Ysmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c53a4c455.mp4?token=r2Xo5ZYs9nWsmTFBDZs-1xCYuQUaMzRwwnaBrCaSS0w2kgTBVNXbcnEuWLpV7-7c7N0vsVjJMo2rSeYyVH9Or35BRJgbFcvi8pQJg4Vj0phhirrlGI29NCahPpjcpKc_uWowVbUi9NrlDWKJM0013FOEK9gwqjFbRD5WHoxQl1acdoO5syhz5pL7KQfnCcJ1pXtG3hlKa-5GaHVwa_nNLfKQlV1XEouabl0mvEojKnqjKeYwAdhjGcruZxsBfGTHxOeVhrm9m76t4TggzzIMWFiLa1QxXx99T9D6Za5hD9C6JNARw4MgpL6jrHBtLYIsjb0NxON5bbr5q_M-c1Ysmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آغاز محفل اربعین قرآنی‌ترین رهبر جهان اسلام در مشهد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/farsna/456611" target="_blank">📅 20:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwfjEAnE9M4unghOQKVFImA8tKJlIfvpkmyZy51re5U5bjHn_2m23CvLKHBBfOYo7atXBlGcOQt2N_3L0StB8XlXUWRN2OM7pnwaZ4p6SBs53mfeXtwAl_ipqGckoT_aSFSuFviALRhQ1O-mPty9gqDqsM279DPHCy-nubvdx30jDmROyqfuDNzYQHPVWsj22OvFpO4ZSoRNTuZXfzLTxcFqO_kNg9VC5eGy85FDQgY1-VuAxplvGbzrSE-tbb7L6HWRP5uBSx0e4nn_tf-B0AElGyX9Ui0wSsmTrVDi_Lq9CLCWq5t-aPQ2E3aC5BYpTUQ6sax3d1bME_Zol5eLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استقلالی سابق در آستانه پوشیدن پیراهن سرخ
🔹
رامین رضاییان، مدافع فصل گذشته استقلال، مذاکرات خود را با باشگاه فولاد خوزستان آغاز کرده و طرفین در گفت‌وگوهای تلفنی به توافقات اولیه دست پیدا کرده‌اند.
⏺
قرار است رضاییان طی یکی دو‌ روز آینده راهی اهواز شود تا مذاکرات حضوری خود را با مسئولان باشگاه فولاد انجام دهد و در صورت توافق نهایی، قراردادش را با این باشگاه امضا کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/farsna/456610" target="_blank">📅 20:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35e2089c88.mp4?token=cdn2tj_tcy4G1jkGZZmY5HLSFjQqvZBWjggFfo-Lb1vH_8txFzX77IMrwsEbFr2PPIf6wosI0DAb4DtQa4e-pH_8kzGkUhAO7_Aa_71EAT3kHGTJqJ2MsDfcQ82HCLVaakVz6WGhMfqeMBVwpyzhLliP_okYONul4xeajiQDRAgoSDLYSvMo5eFmGOhZpMp9e__s0gYcBB4YUwdDmb4I0I3A-DHWCEByuiTEKGd6es5UMo5FYw1ok_qVKdXHQoTgDPPwoHM8EcO6KFpA2zaoDVac-ePv_00-eRjCbcEtm3l9bLwqsIqArw9qlUvkq7wCuwt0DBSEM63pkKwT75Q-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35e2089c88.mp4?token=cdn2tj_tcy4G1jkGZZmY5HLSFjQqvZBWjggFfo-Lb1vH_8txFzX77IMrwsEbFr2PPIf6wosI0DAb4DtQa4e-pH_8kzGkUhAO7_Aa_71EAT3kHGTJqJ2MsDfcQ82HCLVaakVz6WGhMfqeMBVwpyzhLliP_okYONul4xeajiQDRAgoSDLYSvMo5eFmGOhZpMp9e__s0gYcBB4YUwdDmb4I0I3A-DHWCEByuiTEKGd6es5UMo5FYw1ok_qVKdXHQoTgDPPwoHM8EcO6KFpA2zaoDVac-ePv_00-eRjCbcEtm3l9bLwqsIqArw9qlUvkq7wCuwt0DBSEM63pkKwT75Q-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی گسترده در اطراف میدان شهرداری گرگان
🔹
چند باب از مغازه‌های اطراف میدان شهرداری گرگان از حوالی ساعت ۱۹ و ۱۵ دقیقه امروز دچار آتش‌سوزی شده است.
🔹
نیروهای آتش‌نشانی و امدادی درحال اطفای حریق هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/456609" target="_blank">📅 20:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MwMDodkGMdd1WJCJ_6_UEf-wUj8voKOSOehnNZLzsj8KpizhZPCE_7HwE0EmCJNJLqvs8v1L1BgYKzjxvaeyYwGyXFIgPjoPJ6I1HXqSHY8o_1JY_3a2kYNTVHHrizhbS9K95bI9gNqg1GTU2rrx-FRTSmv15Eub6vLnB4iWGU5mrJ_I_bUQbqb81704kSU2XQtSKyHkH3uzIjoTC00t5MFLJ0AF_DlpdLpyGK71a5-k_Fc3cPyStMgIh5xB_1XGNoFGHOs4MjXxSrc6uZdXjnD6SDREOyik9BqAsuPI3HP-JAhKYiESJysmou98IZ2ImRbokikzSTvsYjwIDngbzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه‌ریزی اینترنشنال برای اغتشاش به‌علاوهٔ جنگ
🔹
رصد رسانه‌های ضدایرانی، از جمله ایران اینترنشنال، که همواره در پازل جنگ روانی آمریکا و رژیم صهیونیستی و زیرنظر سرویس‌های جاسوسی سیا و موساد فعالیت می‌کنند، می‌تواند شمایی کلی از سناریوی دشمن به دست دهد.
🔹
به‌تازگی اینترنشنال، زیر پوشش دلسوزی برای معیشت مردم، اقدام به انتشار ویدئوها و گزارش‌هایی درباره وضعیت اقتصادی کشور کرده است.
🔹
این روند بخشی از یک فرآیند و پازل ادراک‌سازی و مهندسی احساس است که قرار است در چند مرحله دنبال شود و هدف نهایی آن، برهم‌زدن فضای جامعه و باز کردن مسیر برای حمله نظامی آمریکا عنوان می‌شود.
🔹
در این پروژهٔ جنگ شناختی، این رسانه معاند در گام نخست با برجسته‌سازی مستمر مشکلات اقتصادی تلاش می‌کند تصویری بحرانی و فراگیر از وضعیت کشور در ذهن مخاطب شکل دهد.
🔹
اینترنشنال تحت پوشش بازتاب مسائل اجتماعی و اقتصادی، تلاش دارد این مسائل را به ابزاری برای عملیات روانی تبدیل کند. در ماه‌های اخیر، حجم انتشار محتوای این رسانه درباره وضعیت اقتصادی ایران، اعتراضات و نارضایتی‌های اجتماعی افزایش قابل توجهی داشته است.
🖼
اما رسانه‌های ضدایرانی چطور می‌خواهند مشکلات اقتصادی را به اغتشاش و جنگ بکشانند؟
در
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/farsna/456608" target="_blank">📅 20:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omIcmqwMVLlYyxR1Z5vBJqr8smLKzqPaVH6_lx2583G0LWFx18Es8s762YWeHtp4gp6bTlL6tXq8axdqh8T-T1fp2_Uyb4FsGUWgqS7H69AmKk1WtKE8LL0UFqOOoTVyn2VNGYdlMizxSssuxRfdgy3cPaZvkdp2QtQv9ukXqMJtHI_nBSenN3E9wLfvWbwfRFqpD1wFLrZ1tPVL2E_xbUgAYaY_k15ryiO40YUMLOtHf0dXK7slv2moQnn9XqPoG-YNmJ5478p2dYOU5WIB1cq_GMzrhkn_NC890sdPTJx1dyK3jt4CF4Z1fGa_5TQ4LW4-iodVk8znyzQXCrUoUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
باتو در عهدیم تا صبح ظهور
🔸
مراسم چهلم آقای شهید ایران
🔸
وعدهٔ ما: سه شنبه ساعت ۱۷، مصلای تهران
@Farsna</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/farsna/456607" target="_blank">📅 20:03 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456604">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A8pAV8p5NqF0eG6nOrYE23DosN2PaEwYPa34jKH6sT1jmqPcAKiVvh8grZ9VQ8-9-fyojDLTJpHAlySZXMWQ2uvvOgsBOWZFGqR4YLyzQyTWxjS1JB0jrctzjSF2WA7eZKRTgAEOBbz2qmRZlAh7ewmWy8zJiCX6Nb6NX1tQzyQUcpXOJxiG_zkZXku5SZkUB1TmPPPpw0NnckjXpC8AB9G96lOzEMwtNJJGnBEFTsjUVM3b5VQjcu5Rl9syU-6MrpEV9qQ3XQwdEkKvPQNe00RXReXQSOeMCUIUUG9DMieIrqBpEWCh21BL9PHxNcsIAOIFyyY-ozvGZ17PUJ7vMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JsKbMzjyLKGRO67ZSuvpISApySWunozNR41-rqvrr9aFGy0pZWx3afXghnF1KSvL4t-HiKcHrpBAyuMX7oySHvHjX03vptedbY3aushSbvpD7sLjtXAWZQIxfJDtDqmGwCpBp30yvtSUv59EKP9jvkWOkIyzStsBwDEniHmNDkhu2aJJPBZc3HK6juVJEW12PLfCQXQYxLeMWh893Q9rX4caMIa_o_nEJ22K7sD7t6Ie2jycPMlvx1yIZEr-f0Qj4WFwoldxUPsKLU73OHd52MnhG566VE6O2fW5HuxZxBDkckdIzIQwrD_JrFv4Ega3CikQuGafH9pcZrSzn4ERcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47448df422.mp4?token=nM4_uawg43hNydMj3Ys6r5GeW4uAMzx4_LmPfilfiep3QiTf5_3UIqvmA3ynidBNS2uMecehyaUe4FkmDJlxNbvKKOJ0rRGMIRpte1x1seOLxFWRUgf0Xtc6tYfMIc6zUrUwS5f-_in2liqiLV39wj4N2y9-lHakjbl3h3D4VKV5DC0NXXTG50pdbaK86Brqmb6ESx2JQVn-PQKf2mhtxMrMuu6yziRRglb0U9QMQpthUH2mWZaivN8Psk_oXoQ673DPU13YlGbpP0q9iVNZdYAongOmw7uIyjb2ebeBzj4RQMmFN-qsJ8CmDBAA11UCQROaizwEvkzDWoQsF1e-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47448df422.mp4?token=nM4_uawg43hNydMj3Ys6r5GeW4uAMzx4_LmPfilfiep3QiTf5_3UIqvmA3ynidBNS2uMecehyaUe4FkmDJlxNbvKKOJ0rRGMIRpte1x1seOLxFWRUgf0Xtc6tYfMIc6zUrUwS5f-_in2liqiLV39wj4N2y9-lHakjbl3h3D4VKV5DC0NXXTG50pdbaK86Brqmb6ESx2JQVn-PQKf2mhtxMrMuu6yziRRglb0U9QMQpthUH2mWZaivN8Psk_oXoQ673DPU13YlGbpP0q9iVNZdYAongOmw7uIyjb2ebeBzj4RQMmFN-qsJ8CmDBAA11UCQROaizwEvkzDWoQsF1e-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور سرلشکر ایزدی، جانشین فرمانده سپاه در رواق دارالذکر حرم رضوی
@Farsna</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/farsna/456604" target="_blank">📅 19:59 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456603">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8cfdbf1f.mp4?token=gZhREyHiPLJsAeNIknSwQ2r0XiFHyl2E14sv2Du0QUQ-4ynHWy2_v6PnmVTN08N2b_k_lPRzFgl6Y3Wb7HO8GmLUL_1qnDjnXT9aHv1RTBI0--bQ0HsfCY0kBv3EjTY-hV7E-WqsdwayILSFu2Rt9gIHvW8CzOogsbibzZ2XRnL29yoxoq2Sxeg4UK3VksvVDav0u-IueksvaN_7-_d9ymBVxCaA8wz7yhfh_MpEe3TOniTiMg4e3IckG9psWzfnaoF3y7qMrEzh23WVHCXThwbuo5Hk17AEzMFnweWRjeTNKwjM6HQe2FRB5oU6_GNGoOGC0aPdITzEdZ-TlKaXHJ8KDX9lhEmRi77B_XNCq5of4BZmVuylr4yFoXwb7Gi7CviIDdccv7Osdou-KfMah4mxGKDQ3pGmkI8C2D0kfwwgyFMlvJvU15blkHxUoyoeFxBaHYnN3Ave58odTcd503sGRr2XnbQjIXHqcNax9pIGIjN8s5tKXItZCgIv4RsQnkvckGURdgDsugJEP1V5ZAvFivTRcRL0rQzranG-mk2nFCBZT0PauNmM0aJRLQ3Qd3u03gZbAavG8O2xxBPYY7dgOfp-oEsnGiacvOlxyEhZamJrf0EcD9nQylNjXpWXec18RCPgP8eSvrAFQ7MjhCp6MXg1Gu7_C5vRV6Gnukw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8cfdbf1f.mp4?token=gZhREyHiPLJsAeNIknSwQ2r0XiFHyl2E14sv2Du0QUQ-4ynHWy2_v6PnmVTN08N2b_k_lPRzFgl6Y3Wb7HO8GmLUL_1qnDjnXT9aHv1RTBI0--bQ0HsfCY0kBv3EjTY-hV7E-WqsdwayILSFu2Rt9gIHvW8CzOogsbibzZ2XRnL29yoxoq2Sxeg4UK3VksvVDav0u-IueksvaN_7-_d9ymBVxCaA8wz7yhfh_MpEe3TOniTiMg4e3IckG9psWzfnaoF3y7qMrEzh23WVHCXThwbuo5Hk17AEzMFnweWRjeTNKwjM6HQe2FRB5oU6_GNGoOGC0aPdITzEdZ-TlKaXHJ8KDX9lhEmRi77B_XNCq5of4BZmVuylr4yFoXwb7Gi7CviIDdccv7Osdou-KfMah4mxGKDQ3pGmkI8C2D0kfwwgyFMlvJvU15blkHxUoyoeFxBaHYnN3Ave58odTcd503sGRr2XnbQjIXHqcNax9pIGIjN8s5tKXItZCgIv4RsQnkvckGURdgDsugJEP1V5ZAvFivTRcRL0rQzranG-mk2nFCBZT0PauNmM0aJRLQ3Qd3u03gZbAavG8O2xxBPYY7dgOfp-oEsnGiacvOlxyEhZamJrf0EcD9nQylNjXpWXec18RCPgP8eSvrAFQ7MjhCp6MXg1Gu7_C5vRV6Gnukw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نظرات رسانه‌ای رهبر شهید دربارهٔ صداوسیما
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/456603" target="_blank">📅 19:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4e15a27.mp4?token=WN26shZYPdmpJFGnqqCGUmf34pPVWwY-GU2XcxQrukicb3_dquxdzaEnfR0I44WsrG8JGvMfnZA0omarbljhISr5fF1jLKsFcHZPe1V1Cii9Ga4JYz7TwMmUcRwEUd-QWGley4ricow0917oLhmRO5AMRclGg3UCFkLMwygq6O96Pn_W9Th0_LzVp3dk9uO40Gjhlrs7tK-gwjbgjZx1BMhLZeOrBZzPYqkFsxIhYXiH3oLPHG36p3Oo2XvZCEMxmXqAz0yar7WjXXmpoZWY3GYOfh7zSlr8hCPHQbn_kXuz9jWULoGgDGW01NJSW_A5ODPcaCz2WBqAIVNJJdUWUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4e15a27.mp4?token=WN26shZYPdmpJFGnqqCGUmf34pPVWwY-GU2XcxQrukicb3_dquxdzaEnfR0I44WsrG8JGvMfnZA0omarbljhISr5fF1jLKsFcHZPe1V1Cii9Ga4JYz7TwMmUcRwEUd-QWGley4ricow0917oLhmRO5AMRclGg3UCFkLMwygq6O96Pn_W9Th0_LzVp3dk9uO40Gjhlrs7tK-gwjbgjZx1BMhLZeOrBZzPYqkFsxIhYXiH3oLPHG36p3Oo2XvZCEMxmXqAz0yar7WjXXmpoZWY3GYOfh7zSlr8hCPHQbn_kXuz9jWULoGgDGW01NJSW_A5ODPcaCz2WBqAIVNJJdUWUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خاندوزی: «مرتجعین» می‌خواهند ایران را به ۸ اسفند برگردانند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/farsna/456602" target="_blank">📅 19:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZYI1NNeg0eXksa5cdiwZoNY1qomuAsqZKNZoHZjwX-ja27_O3t9flymx1uuzPB8rvRR5cVUEbIWuI2pqiCRb1zEDbnVBB9RxM2PyrdjKHzDzcW11_K_YphFMtUvAsDuRgvxJddB-2EHlHKPBHk65qn_28nwLGatX2_0dY1r7uLHeiNkKCzSlRo6fq9HbdaJgzDjIUVli8eU3lxhATvzlMega8enFpRQIrZULiZzv2yIKfnxkKRK4dpyMiHDOl3ukobR1GMoJ08bPmF5HPpqqUkl4Ry5eeCb3qSw3FrTaNThs5YyTH-VIjYrKd3987VeTCvMULN6PwWDtrSQ6Ot3bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
توقیف نفتکش اماراتی در تنگۀ هرمز
🔹
داده‌های ناوبری دریایی نشان می‌دهد که یک نفتکش متعلق به یک شرکت اماراتی هنگام عبور از تنگه هرمز، متوقف شده است.
🔹
طبق ترتیبات ایران برای عبور امن از تنگۀ هرمز، مسیر ایرانی یکی از شروط است و پرداخت‌بهای خدمات و اجازۀ ایران از دیگر شروطی است که نفتکش‌ها باید رعایت کنند.
🔹
نفتکش امارات در نزدیکی قشم متوقف شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/456601" target="_blank">📅 19:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5ee7db29f.mp4?token=l2Xlh2hcMtZjGf3G3x3hqpW1h2Mp7H77M3Il9q4U1vBQCaAT2jlbD-wxHHFrIX1tWQLZFvDpVJD8PGzWZQZiyUXxrbHb1Hj65WnouYIz4nRSt_0EpelAf2Zd1H1b4krK47xeMma9RIseSZ5lyE9DQ6yb39E7pWcIYrOOKuugUz_Eo41FgxyHgNAoK47TYYw0iiKvnKmCkzkDKcC_EJsvViVCvZdO7W-e0fXy1IpigsAQ6iklOUf_xDHyes3DfNyqNpBS7lharduMnDEb48jmcvJeprYYVvABp4Cp3dIelXbdXkPkOhZLjm94BA7IkSkxO--TiOopEC_zrrzOHKoeXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5ee7db29f.mp4?token=l2Xlh2hcMtZjGf3G3x3hqpW1h2Mp7H77M3Il9q4U1vBQCaAT2jlbD-wxHHFrIX1tWQLZFvDpVJD8PGzWZQZiyUXxrbHb1Hj65WnouYIz4nRSt_0EpelAf2Zd1H1b4krK47xeMma9RIseSZ5lyE9DQ6yb39E7pWcIYrOOKuugUz_Eo41FgxyHgNAoK47TYYw0iiKvnKmCkzkDKcC_EJsvViVCvZdO7W-e0fXy1IpigsAQ6iklOUf_xDHyes3DfNyqNpBS7lharduMnDEb48jmcvJeprYYVvABp4Cp3dIelXbdXkPkOhZLjm94BA7IkSkxO--TiOopEC_zrrzOHKoeXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آتش‌سوزی بزرگ مخازن گازی در شهر گلنپول ایالت اوکلاهامای آمریکا
@Farsna</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/farsna/456600" target="_blank">📅 19:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456593">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bHMQbYbM1msX0Rcoe-mVhXrziNskOnLumyMh3W-jXfpE8LTeJaNaHfZEo6AMhYsyfSpsbiLOnCpCIX8K6BZfi3pLPGlz8dkqzE5kuBz_2PYOBZZ1Kdvk6KePu-eOuYKeYBr71Sm7k-LjeJ5AqQS0kZG9jpYQM4scSADA1m7oNXyIZJuAATxoMCjrD2gChZ0HmT5tXA_jki1upXH4BZWc2pCJewmiMH-8rsrKbVbcjeADxS81g-vDeTdiEhT5398ks9tfkwkaTe_mHZ_QT1RQGQIcgm5M8SPKq0gOVIMneOszEExz7T9kE8IW6NAe_bpBCrmf371XZh4uwzVicrtQTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HzSTVYZtcxvRWilCFJzXC0w2xMUvSSsItf_6SyGPY7cYO59iS_VejaEJMuksC85Z4ZJ4YYfDrqHLB0296Cdsh3bn70lck0LpBZg-rxwnBeKnqkI58Zv5imaxg3E3PpomIwLfSieg5nY-OpJvtvgz_HZVX-ry-fIaHjlD3KvbA2Buo-2p0FrwmigBa-PSQNSrv9Fo5wqfX-NWv0YawfIVuuYl7XelxpTZHmybN5JKNrul0VlT0No6asbkTHeAfQRBxFZujqO7a7mWlrayMHSHN_zlPkmuGlMwKpGmpZxKLTd1fMWbM9yv9uoSBpiy-pDQAv5_np1q0QVm8etFubWz8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHQjeBiGp0RlrR6CStVbjSLMii0tk_J3SkKBvXLf3g2O3gsSvrBJqhyzdQ3lMzTWjI7B0Xg7ypf49G0kHpNi33Py26AycXVw1OkofSeUJL10agSYsbQqtRqkfAuPXSb2d3mqX72gGFVEikafFUIRz3_0UJsNZC5dMY2LPf6jPLHBAesHT0S-xo0S-jYl7-5b2JHZ5PHNXFZBX-OO_Z-OgFKoO_vubnNiJ-2_400iijbzMH7PCbSPsmlu770DofOOR9oP2UnJ8iYxsTcLCbIumxWXyyO1a6rZ64VB5YZNPV04aKgIL_Asrxv4A4NdCgh2Axi9ahjN__3zcAnFqwYTMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwWrWGqFWYw1ns6ZzqLEDXGkSbU9Wk4lriIrc4lLJSId_8aHMKEipXI8fV_2c60kSAlDMSAjLDeCoOojGpx_CwFM3qPtYq6mM7h3j3XLzd2UlsBjbSzT5ZdCkbVYm2A_Ysu_vD_fhT-Zbww8A-IZvJPtZHQjvYBohk2fs3elYhKl3tRu8pVRQVsHuZgRB-TS4RSdgYpf2B9KYjBgHaTiTOyaqbEB61AHA4obW2yUciRwp6GB1lCqdjWpoimCuueLIGrYe9Q0qX0IMvhZH2-HQGis5mRLxaspcxZd_6tMHTECfWxJARi370LkVEsE0hQTgQHGXHMDFYyCZONakXvwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g39GWGwSUzf6BEWHEbokJJ2g6fShZfrlJBHoPD07H4NAiikHmqDNFYuzczw3O2nMMAX-uajO0hYAA7_bBGK3EnBAd8-b5UrjyfreyceAPb_E2E5Nr8Oe18LvBXj7rrNSpyoqf0osl7Qg0cqK_hjtmyMNBqIa9uZHFgEBuZbzanmLAdAzC5Whb4hjIrzQw9076hNBTXGK-QDRV_xijMzkTXBKMYDjhNTdBhI-Slz04bBpElMqNkZgtiZ2EsGmdEAienfLlJqwzOUFcU2NG_6ZPwoTvKxilK90Onrm8dii2wCOJhwfNUobipvVGRKUZ-ziiQ99rQaIsvlQh6ICk4wDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GquNPN1r8-OAnj1CbAdz4ukXsyWv2dj0cAjkVO36EON_JvXC0u0_vi81I0jfekrcRhhFikj0Io_4RsWU_7Iv-i6jUncVOWcG_cYFaLESjSvhNfJuw0CTYVM_QsgEXJkNYywdLqJCjftKkWI-ibFjRWr8FTBM6oMggHCQY2dc86KHClzYZRSqf6YNyeTkQOckATkwcmhiDMmnQStQYrbLc1_KNkz4AlLlF37Y3xGIAUBRN-HXMLtw9Xqo6VJMy8Qy6j8h-SZvzmGt-G-CArrJ8PDOxIJp2pnAoHMxkBfwy6EeXrIHod01Zs2YCUAQElQTXiFKWXXFxq7gDsFZJ0juHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EKK9ZNu8DuWZ3p_rTDkF2-yDpsTwaQJO9oqKNPUBE2kEmWZs7bXy5ACj6YcvgNtrgtyz0c9lMb-kVJV92vje3f1Iuwxua5IRr9rb1we55kuT96m1wDnXfDhHwugqYmSUWxa5uW-Oo7VkaZsA7FngOU6bnErCpgL90tfMgFIlRoAiTGBKEMR5OVYJTZox94xPlFTz6q0nfO7Aa5D9wC73YNanPTfihkFhhrl18CjQPb6A5Vss6xKrc9oGiKD_s_6DialSK-2EVUve-zycnK8OaY3qdeRLrS2sKJc2FTU4EHb8QXZVkJkYRd72Cf3K0fvhTDlaEnCCfbViV2rYHRQDxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
آیین بزرگداشت امام مجاهد شهید
عکس:
هادی ه‍یربدوش
@Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/456593" target="_blank">📅 19:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9490400.mp4?token=LSP-b5lHmIboOK6mP1fcJnwq0DN8KgZ99BXtoJuNay0Om5mQyrAgB9y2SMMqdxVvljETXxlJDEkIOBCYiTnTGiVJwa3vU0f__QYVDNaZjdj3eTHANZaprZrFz6Ya_ww5W4RZBf_zX63OwzPPN27E95dekSapZzPP30fGWIRGYPJxgQS2QPvw5o__he99enSX4MRcW02gm0vcJ7cS-dhNMARVVZW_d3Gpvdl8tqngYg-DofTsVGezzt8P1jY2h5xLfOhHPC3sWf8rW-woPUYk9pS_hu6Yl1BYfkEfhbK7-J-GSAcYWmPI9u3ihi8ZLQ3XSzIcaQQQulIGLKwT-vTJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9490400.mp4?token=LSP-b5lHmIboOK6mP1fcJnwq0DN8KgZ99BXtoJuNay0Om5mQyrAgB9y2SMMqdxVvljETXxlJDEkIOBCYiTnTGiVJwa3vU0f__QYVDNaZjdj3eTHANZaprZrFz6Ya_ww5W4RZBf_zX63OwzPPN27E95dekSapZzPP30fGWIRGYPJxgQS2QPvw5o__he99enSX4MRcW02gm0vcJ7cS-dhNMARVVZW_d3Gpvdl8tqngYg-DofTsVGezzt8P1jY2h5xLfOhHPC3sWf8rW-woPUYk9pS_hu6Yl1BYfkEfhbK7-J-GSAcYWmPI9u3ihi8ZLQ3XSzIcaQQQulIGLKwT-vTJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
به‌نظرتان چطور باید انتقام رهبر شهید را گرفت
🔹
امروز ۲۶ مرداد، تفاهم‌نامه ایران و آمریکا به نقطه پایان رسید اما بحث ما جنگ و مذاکره نیست؛ بحث ما خون‌خواهی رهبر شهید است.
🖼
به‌نظر شما چطور باید انتقام گرفت؟
پیشنهادتان را در بخش «
فارس من
» خبرگزاری فارس ثبت کنید.
@Farsna</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/456592" target="_blank">📅 19:13 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-J-FTK6xK8ZAUNYOZAWBAy9FRHZfhZSz_2RCsQknXT1W4jPONaLDoddPRvEbdbPJtbtDa-IdlXOD0h6HbBOrjDe6fZBHfOFKlX3DWOGEsssqCOtOq6RsE-1uOkK1B8lLNq9Lxoc5orAYRdhbkEukZhr-Ys_bvqISRMZ9tbsPhaa9V1sz_k16EmccnACteLfiCY7iGT_R870XsVtFLcoj6nI3U3NI3nujYEKOKvruvQ2TX8ASZFkkpWyhpzX_UuZ5jB08wt4Gm44ZtN_psmBuUQTqiJm_mMGHxo9TGihV-gogrP3Bd45g0Uk9iIkA2JMh6kvzIKbDP7ccZzPgCOqGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توافق نتانیاهو و داماد ترامپ برای ویرانه‌‎ماندن غزه
🔹
هیچ گونه عملیات بازسازی در نوار غزه بدون خلع سلاح کامل حماس انجام نمی‌شود؛ این ماحصل نشست امروز کوشنر با نتانیاهو در قدس اشغالی بود.
🔹
مشروط کردن بازسازی غزه به مسائل نظامی در حالی است که ترامپ ۲ روز پیش ادعا کرده بود برای سر و سامان دادن به وضعیت ساکنان نوار غزه نمایندگانش را فرستاده است.
🔹
غزه اکنون بیش از ۱۰۰۰ روز است که در شرایطی میان جنگ و آتش‌بس شکننده به سر می‌برد و مردم آن در اردوگاه‌های موقت و بدون حداقل امکانات زندگی می‌کنند.
🔹
بر اساس برآورد سازمان ملل، بازسازی کامل غزه به بیش از ۷۰ میلیارد دلار نیاز دارد، اما هنوز هیچ کمکی نرسیده و اسرائیل هم اجازه ورود مصالح به غزه را نمی‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/farsna/456591" target="_blank">📅 19:10 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af8bb75f65.mp4?token=mRCxYu0Z7ktkqAmdJr77Lr_h1R4pqwSKhaarGo9J4a-u0XMp2en3U51nmO1fNyi_oF_24Yyn7fmdl9RZ4jqo8UqcQJdRgQ1G5XmKTvuQSla40paPEUIlI9wePE1ZI_Mvt_7O_e0j7Qm788GrmdKndA1TXCorbX1PuJcP8q7-islidpPbZBOg4QPNYxZM3tilsSEEP1W3BwKeffEwfzC8MOTyGAXzeO8xyWVF13GjFR7bF1Q4x-kVTo1_YHdqA7b5YP_HCNWm2OlAHH1q8ODPP1L6ZZ4FaA4Jrc50BwoW_mC15HJ2Vk_9uCBaa4ne50m3bWZMQgZXzVOOEH9qg7Rnkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af8bb75f65.mp4?token=mRCxYu0Z7ktkqAmdJr77Lr_h1R4pqwSKhaarGo9J4a-u0XMp2en3U51nmO1fNyi_oF_24Yyn7fmdl9RZ4jqo8UqcQJdRgQ1G5XmKTvuQSla40paPEUIlI9wePE1ZI_Mvt_7O_e0j7Qm788GrmdKndA1TXCorbX1PuJcP8q7-islidpPbZBOg4QPNYxZM3tilsSEEP1W3BwKeffEwfzC8MOTyGAXzeO8xyWVF13GjFR7bF1Q4x-kVTo1_YHdqA7b5YP_HCNWm2OlAHH1q8ODPP1L6ZZ4FaA4Jrc50BwoW_mC15HJ2Vk_9uCBaa4ne50m3bWZMQgZXzVOOEH9qg7Rnkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دست‌نوشته‌های سربازان آمریکایی روی بال هواگرد ارتش آمریکا
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/farsna/456590" target="_blank">📅 19:01 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMKs4rdLGIwvbWp0p-P3ALkBjDeml7eN36CLEQtTF6GvNXo1eN60riGBicAgoEuAJzo-0TN9Pl1Zh2yBadZPC6ixqelSD0_htmftq-0LHAv1CuX3jSepcRPNhaY5uAMP_7svWSfzQIOeWKLhZAcUqBS2AQOafh8Dy8NFsUUkrpt2pYYeGnqzgt5TUPR6bG6y4knGLufTkXbQhqPaH0jAqH9x3PlA_SemexGo0UGffYsIWkyZLiHp-4k4O0_5m1GxL8vtq6sAZLim7wooHH7UnMdEJPdMFUipuhOQjiyK6hAw8rJwDJhPg4fWt6AWGWn7HFXkkZX0jzCUc_y5a45OYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لایحه‌ای که قبل از طرح در مجلس زیان‌آفرین شد
🔹
موجی که پس از اعلام دولت برای ارسال کنوانسیون خزر برای تصویب به مجلس در فضای مجازی به راه افتاد، خواهی نخواهی بخشی از توان، انرژی و تمرکز مردم و مسئولان کشورمان را از وقایع جنوب کشور به آب‌های ساحلی دریای خزر…</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/farsna/456589" target="_blank">📅 18:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XES8ma2IU3RNcrP0Yqc1ufV4xZ6aXSqrFNXJmydY4ZvRmHnQ2mIF-OMhtnZ1DveiaYaSIkuxdl_ExY8vyFzfic69vp4SxNX04oyPwDNSddP7DezPkohs4htKQLJRN74NxdtxmdYem65WXjby6tYy3CYMqCqtXCEmVh8xUmKpxFPs84TWxI7v_Taa1HpdIEBeKZsJiBPgHFeifhT4QCEOswxLf1a-ZaCIqBmDXJWsdylEtzbnoTn_ArMtjFka41kydkYmAaV_t-i9h3FBgM4_2q2d0ip4_QUkOBDAjR7IA7w0JGPU_8LQ1szrPy_OExXf5c_Yy_ZdQZ1ykq2tHGC_kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام تاریخ بازی روسیه و ایران
⚽️
تیم ملی فوتبال ایران ۷ مهر در ورزشگاه «کازان آرنا» به‌مصاف روسیه خواهد رفت.
🔸
فدراسیون فوتبال روسیه اعلام کرده است که این مسابقه به‌عنوان یک دیدار ملی رسمی در نظر گرفته می‌شود و نتیجهٔ آن در رنکینگ فیفا محاسبه خواهد شد. @Farsna…</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farsna/456588" target="_blank">📅 18:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس افغانستان</strong></div>
<div class="tg-text">انفجار در نزدیکی مدرسه‌ای در غرب کابل
🔸
منابع محلی از وقوع انفجار در منطقه دشت برچی در غرب کابل خبر دادند. این انفجار در نزدیکی یک مدرسه خصوصی و هنگام خروج دانش‌آموزان رخ داده است.
🔸
تاکنون جزئیاتی درباره نوع انفجار و تلفات احتمالی منتشر نشده و طالبان نیز در این‌باره اظهارنظری نکرده‌اند.
@Farsnews_af</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/456587" target="_blank">📅 18:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456580">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ugm_bLunFx-RAVi46qQH5NU7FUYC_9HcLSinMCC_q_eYUjCjBbqm5yIKNZ3Jr-SnefmW0v4zC6kzVs0HLo_7i0dTCkUDI4xvaU0v1mf7HAs2Us9UvDsZ1v38_TlawD8Mqj20V_nMvrbFBsEMCj4-hgXDvYQ994H5F_Sx88XdPnl8IsBWM1ZLfolfMMAAl5WWS6NytxFlNC92SD4UdqYRIMwRRaj3FsMRP_Sa4voJRqa9Eqtbr7bl3l2crBITsj8NWqA1ZhgJsgTcBd0Nm1qlG0OYfWk9fXw6DtGVTK3tWpIr0KLJnXzvqD7TbyFKYxEBSdSHa3J2r2NehspDFA8a1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SZ7WR4FZKNM6VyYw4MKwcYsoOArBt4sQljEcJDI22ULj1PGXuQc2YnoshU19DyFVVS6wZDICi3ggq3WhF1ZEfhjh1XOpt3w-fruH8284dWB8cjqGkPt1lu8xfJBQw9K4FsYIBpcdeIZazFxAqIEiR9vWYwDtsMf5ljrTJSBlfSSrQoF5OYYYmRDGU69dgcvVOUaIncKNZxoIWb6LxB50pTNmA7mjx92aYoL6hV20ETF88ue98e3NMZ9cEOe0L5qrFoVtdxs8xNDwPgd6sCKkmUFyMGvja-N7_wTHBGNWWuHeNqVK58g_ELeY1a67wg8uRfI_77MyR0UdtM0iyNKnPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_CQJ7MLM2Mh5eCoMOuemhn8aSfV78agCIZz7lZcYVBKao39VTAWIarkeUH_pyggdLCB-09529dHdKHnfuB15TPkyiLnGRKC3hf5OGMa_EJxGxAxsOwv0S1HnH87gugesmgI8HpEP0zKVVb4ERbGgwNHcDRqBE8pXssPGNMVUaXmJD_UL4JV7VC9ng-lf2lWSCnvyECn6W9qOO-GNVFdM5NCJaD0PN1OT4CXHMUR3fw8jq6GsfclpdSJKq6esiE45oiZ4a0-Kc-8kv35CO2jdOnldwbJfpEdy8kcE9esz7OP5wC9m3K4VGYIWnl_lXEb5GZwPQTWjBLQw_QEjBUUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MtGIFTnv0QbRbJsQgsSCj9j-NiI7YYAvDF583VqwNyNv_EtRGBrdbwZJAb9ABM6m7S9uxHJ7GtBOV1R9yaAptcCPeloyi4RcNMGHu0buTjPL5EZtHdmhqfjkEjag-d8np5r1S561Xh4HRaJu5Er6kRKpkCN9q8BOS8zriXVf54_mCod87WVcUCzkLPrg-I0CwfGcSEG8SMCg4l4Bso1Y9NNH2imtGcejRhySOlOKbwQrg9PyU_9b-VT8UMdOBky_TEP688dhu6fLdR5stPKKNoYs9v5Apc1Et4jkc8JsKPojwJb1xD9YfM_KGA5iB-gwNJ2tVQhhwlTMxMKc0vzY_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yw5_b-deXQ3Zfnr_Y9En-ugLqtRjb5uZXRcyChELdQsRq5a2eh-s4h5mcfNA5bv7NnLAGqVutUDiEhoodImdjUX9vyOIYnGcKIrGP7Rqim6lqJGJzcpOW27Y6J5Fa3PWZXq5vteSeJeDlWCNWo7Sx_NbZstWkhAzPvqnXQctXA0Ne19lUy78ZLsqW0kRwOn-uNDpU1o6O0TzKH-mhSv51bmt8bk0-dnqQw7TTFqfgyoDhWWvTzliB_cRmJwJyvu7mS1Vo2qfWuVMSDqdtlu996z21C21VcKg4LKd8EdliAowimNqxqSLcxYcYhIj5tLrlw0zYsZ0x-C5prDFBIqsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zx8Y9E2hYrDMP0SR_Sf6U3rWKZfRIdbEYNjHSeNqtRW95bsblMFHeTrNhGb7AUQScj1n6GELdtXeys2q9IG6ep337H9qQSkMUcEOTlHgnRB-yfxnvIMDjWcrbseJcYAMK_0JvzI-gWQuJOzbjPolrr1bebIp_Y1nmR4i5xhaStDPkdTezBY6j14LpqBCo-ZdnB1Qh-NKayLI0svNVZZ2oP5wcdjTUs4SOxm4RWSYxfb3n-DYN5D1cRYVTjSSHFcuASz0GjRb8sCv9keqM7jiVgmEKVnilgfOhRQX9D5J17XULMKOJ8g2F5YqOZ6bMp5YeIV59BMTqTVD8LpyY8U4Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ilej4JtRUKZeB1NQwHll5AQ4J1I8pyKJagIcXf4NJmPL0bCpi1HWeLAwDEfWizESNy_yC-mW9IsdaUxuXr9p0hMFQPLJcDckRnDXtBikteA6tfA0JCZ013NbRJxVlOqsTTj3CXFGZTzP8yKe0mL1sDAhHQRTmzixqQhBfvd7Sm4XF5mWzrrU00J5ueMN5i7o44ReMH_J5Wq6qxBvUzx0UCXhj7-xQgVEdwXQH0jQQuWYj-BljjtuzQQEgJnEEFqCZv_O8m2E2MqAnlRjysv2tC-D4ebF3kF40KKXix_sZ0oKIFN_OFt8PYf9NTqAt9RAa7hxXiS04kU9YVdkbj09VQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
گرامیداشت راویان خط مقدم رسانه
🔹
آیین تجلیل از خبرنگاران و فعالان رسانه‌ای امروز باحضور جانشین فرمانده و سخنگوی سپاه در سالن سوره حوزه هنری برگزار شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/farsna/456580" target="_blank">📅 18:19 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456579">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lx6uy35SuWH6AscC96auLeh1NBCziISx_yTaM27hTnToNwL8m2BgYo9VGCgoCC7MKDTZ2un0AP_2txgOLAutjDIf6_-w6P_pey2D9VVqWWMHZ_k1oO5urWzFXDOGTCOWbd5wYrziG_mjmdS5IakiA9cDvvehtyPR7GP6t_GRlmiXWwn922F2T4qDTX3h7V7ChjU--ThNoHa6LJepqDpT42Ojh15VqAAuWspr9xAvgurEOj1bDOKPmauo6tRibIhxLfezPSZ-KORlaprQSdS1ECpiUCoiRjlTrN9tlSRvGX8W27DfoWM0Pr4P4-w91-A0cVl9YUpWGTzPPDjKYN0UFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سفر عمره از اواخر شهریور آغاز می‌شود
🔹
سازمان حج و زیارت: اعزام زائران ایرانی به عمره پس از ۶ ماه وقفه از سر گرفته می‌شود و در مرحلۀ نخست هر پنج روز یک پرواز از استان‌های مختلف به مقصد عربستان انجام خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/456579" target="_blank">📅 18:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456578">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8e88157be.mp4?token=B3eTsef5UdiVAoqnfVmS7pvxM_3MDO24RfouPciwwyRAZnVkKxhb_HMBbKfapy0HfAVT_rZeZXf04MWfTBatLU1uvrTV7qahNJE8rRMB6ISJH-BE6D_6i8hQHeMj41AE_bfrh1TED2Ps-3wRED3rCiMEKKk-ABOjF8D1GLbYQ4Iko2IShIhMSllrXiBTAAo2kxp-LnoOUdudxiSdsW-YzKk0i0QKwo-hpy2NHNIBHRybN8YDsEdpohAg4PfSwH5rFz-0vKyDl8ydnudZE4kHAZOZt36OgevJtaLw9g7TdXLxeQwcnBL5Yn6RbXt-l455z6-A0W6WHaAF9cF2thTtog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8e88157be.mp4?token=B3eTsef5UdiVAoqnfVmS7pvxM_3MDO24RfouPciwwyRAZnVkKxhb_HMBbKfapy0HfAVT_rZeZXf04MWfTBatLU1uvrTV7qahNJE8rRMB6ISJH-BE6D_6i8hQHeMj41AE_bfrh1TED2Ps-3wRED3rCiMEKKk-ABOjF8D1GLbYQ4Iko2IShIhMSllrXiBTAAo2kxp-LnoOUdudxiSdsW-YzKk0i0QKwo-hpy2NHNIBHRybN8YDsEdpohAg4PfSwH5rFz-0vKyDl8ydnudZE4kHAZOZt36OgevJtaLw9g7TdXLxeQwcnBL5Yn6RbXt-l455z6-A0W6WHaAF9cF2thTtog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حجت‌الاسلام خلج در برنامۀ سمت خدا: اگر کسی تقوا پیشه کند، خدا برایش راه خروج قرار می‌دهد و از جایی که حسابش را نمی‌کند به او روزی می‌رساند.
@Farsna</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/456578" target="_blank">📅 17:49 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456577">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5074a8c966.mp4?token=CfVqNNGwtAyqwT9XW6Uha3Lh9f-2mQeJBqE8cvUD3Caa60tXNYXwQRGkaGaA7dNr1jqRQQsYLU2GHWP7aAX2MQczRBDP3tJj2WxCtTonWggJFNYffxJw0C4YgzTBVcoSMn9kB6aRMfBVadLD7QvJp_wfNYHCLNdOnM61tR0XLygz967mle_tWiw76F2gNzKZkdiwnd1lqr1HM-ey0il0nQr_-X-ZITDJs0Mq_QhAWPCdaLa0fDqfiJhlmQ3JI1ZEDt085w8k7iaqEdy_n8xJH9rn6Z8-vXHO5NeIwBAHIW64jbD88cg0B1gbpwvrnItCPcZkXCrJ1Q2v9fmAbX2JmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5074a8c966.mp4?token=CfVqNNGwtAyqwT9XW6Uha3Lh9f-2mQeJBqE8cvUD3Caa60tXNYXwQRGkaGaA7dNr1jqRQQsYLU2GHWP7aAX2MQczRBDP3tJj2WxCtTonWggJFNYffxJw0C4YgzTBVcoSMn9kB6aRMfBVadLD7QvJp_wfNYHCLNdOnM61tR0XLygz967mle_tWiw76F2gNzKZkdiwnd1lqr1HM-ey0il0nQr_-X-ZITDJs0Mq_QhAWPCdaLa0fDqfiJhlmQ3JI1ZEDt085w8k7iaqEdy_n8xJH9rn6Z8-vXHO5NeIwBAHIW64jbD88cg0B1gbpwvrnItCPcZkXCrJ1Q2v9fmAbX2JmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امضای ظریف پای برجام و کنوانسیون خزر
🔹
اگر درنظر بگیریم که نقش طیف اصلاح‌طلبان در برجام و پرونده هسته‌ای‌ ایران تا چه میزان پررنگ است، عمده مسائل مرتبط با کنوانسیون خزر نیز با یک درجه پایین‌تر به این طیف مرتبط است.
🔹
اولین مذاکرات پیرامون تعیین رژیم حقوقی…</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/farsna/456577" target="_blank">📅 17:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456576">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_73xRVHjLI1VLhjtodMvJs5B32cZQTF76FXb0x0eLcWy0sSmfh1ICQl4I_UuShEXvVd7-ct5jtrWtej2pHWHvMoH6_s-xmN6ng2kwBUwomy7EStioCT87FZIYEhm_NFEJXn_hmjXX_rGyr76NmxI80TR0W_cs_zmkJtFGjqJIqG0sgfmoqNIOeu_n0nE8_tsicx6M4TUyrTm_NN9_fQFHMe94NFp-2YWXNHNQfgiIpC4Gx_N0R7L15_yFqisAl_CMYG-JMX_4uWDNvNw6Qb01ID4UgUT2UgYwdzNebC8L2z8FWyVV2RNXHcRIwNuSDSAtM1vMm7kIUoYDl1yyxwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۹ سد برق‌آبی ایران پُرآب‌تر از پارسال
🔹
بررسی وضعیت ذخایر سدهای برق‌آبی کشور نشان می‌دهد ۹ سد مهم کارون۴، کارون۳، شهید عباسپور، مسجدسلیمان، گتوند، دز، مارون، سیمره و کرخه نسبت به مدت مشابه سال گذشته آب بیشتری در مخازن خود دارند.
🔹
سدهای برقابی سهم مهمی در تامین برق تابستان دارند، با این وجود در روزهای گذشته، قطعی برق شبانه و خارج از برنامه در بخش خانگی و همچنین قطع برق صنعت بیشتر از گذشته شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/456576" target="_blank">📅 17:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456575">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دستگیری عضو شورای شهر رضوانشهرِ گیلان
🔹
یکی از اعضای شورای شهر رضوانشهر در جریان تحقیقات و اقدامات پلیس امنیت اقتصادی استان گیلان، به اتهام دریافت رشوه دستگیر شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/farsna/456575" target="_blank">📅 17:26 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456574">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po2mOjPCQn5bL_IdaA3DyckzyeimczCjcivQ03R7raHgxKC0_OBkGEfDJLhMcxoRLtDlTH7CCEKsyGK8U4sQkAPwguzY5aICjgtR2l1Cdr9Y-eapNLZNSVTz14xunL0yw3S6ft2K9Nw8CP3oTnko6IFVb6FevFMGvNvelwuJyW-NE31aoM7RpoC9Wqqw1R6gnAz674M2kHKIFKVJvINT8NDaW4iZ4FPo10gapIueZstRJuPHXPuTlkhfLyTLMnYusIKWP9lEujnSQeUCTqDeEqF44DLuVN5hk6OfUYyy3iL2ghxcy4goeQc_gBj7c0owgU9gAz0D77Bfy5jUm0e5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
حضور آیت‌الله سبحانی در مزار رهبر شهید انقلاب در رواق دارالذکر
@Farsna</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/456574" target="_blank">📅 17:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456573">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a88979b73.mp4?token=dLN8MEuf4g4UIZ20PjI_VX35dEkAAxbO9hgcxLKGEaurFIpdOBfucD9Avkza61gG069yfTyT5YX6BPCdPN1h07Ice63UP7pkquWW5A3Pav4rQdMWTOHNVDzIDFrZpsSDPOAHVf2kNlwRZyX3amNnho0ZDdSvc2x0bQa4qS39e5LczCYCUOUhcpRLELt1--1gsDGbqbuU9YJ9yM4m-0xi-i6M8NX5gQQG-xjgS3kKqSTZvwbBJVIohJR1Tt69Z_fMrC3BLTLyjjVaQU0SZU7FSNS957rohoLUJ9XrPg_y0jo5FarXLA4WN5mcLmiA-TugZCJ91srgNjCVzmcGRVvYAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a88979b73.mp4?token=dLN8MEuf4g4UIZ20PjI_VX35dEkAAxbO9hgcxLKGEaurFIpdOBfucD9Avkza61gG069yfTyT5YX6BPCdPN1h07Ice63UP7pkquWW5A3Pav4rQdMWTOHNVDzIDFrZpsSDPOAHVf2kNlwRZyX3amNnho0ZDdSvc2x0bQa4qS39e5LczCYCUOUhcpRLELt1--1gsDGbqbuU9YJ9yM4m-0xi-i6M8NX5gQQG-xjgS3kKqSTZvwbBJVIohJR1Tt69Z_fMrC3BLTLyjjVaQU0SZU7FSNS957rohoLUJ9XrPg_y0jo5FarXLA4WN5mcLmiA-TugZCJ91srgNjCVzmcGRVvYAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس فرانسوی: ایرانی‌ها تصمیم گرفته‌اند کوچک‌ترین فرصتی برای حفظ ظاهر به ترامپ ندهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/farsna/456573" target="_blank">📅 17:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456572">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6ovHscbDaOXHqiz8L6UfhelD7DrC3ytEmLYKZvy0cFCZaw622j8OAMSifdlJ135grKLnfo8VkRvsyHYKOw8hDhekna-o56w9iUOnPAcXus40ShEOGpKnkX8N8eZS15Pl5SzlGnSdnLUSbB6cJzxEtxOQV3iW6j4H0OpiBHuTSUntthNpg_mN438INBxQDNSyZsC1JPcAPn4t_SFfSNA6cu3yt9OET7UanvVZ9BV0LznCLXB4x-AqZSg2LREbAFdY3Xtbgu4cs72hV4KB5Z2eCp2SRt-iKe1PUUNVn9wlt3NnmwGR0edoHSZHFHf7Dd7lUUtL87XH5NXu6wz1wzY4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: ادعای ترامپ دربارۀ گفت‌وگوی پشت‌پرده با سپاه، ناشی از توهم است
🔹
هیچ گفت‌وگویی میان مقامات سپاه با آمریکایی‌ها در جریان نیست و این دروغ ترامپ، صرفاً فانتزی‌هایی است که به‌خاطر توهمات و کابوس‌های ناشی از شکست و استیصال درجنگ به او دچار شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/farsna/456572" target="_blank">📅 17:09 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456571">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ehvWi61Etn9eB1RAWEO2ZKmfPzio3g_vQszNB_aocJgxHB9X6MoYMGMXXSz916tjQ4ck0mhko1ZLBbUPJ1P1YYnL63kQYyV1tVFg_fyTCJPo8lVf50y2vtROPJEvEKgSJLckQsRVkNsJzvNnWX-QE0tXSJbQdtgLQTSxs3xVfAmfsO_sfEP_tnneO1eHTPi36W0C5wbEZ_tIvQcFleGKGMHyJDPKz6ODexIUVDmyAbk3MdAPeIxa7sntJJw8Q4bYGpzTzqplTsoAip3DDgkiQlbM5p75If9YXOqZrjxonkNUtH2otyS8h1xrZs2cifrwE-a8fN1vXU8_6kn4wEhRkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نامۀ علی مطهری به پزشکیان: دولت دربارۀ حجاب بی‌تفاوت نباشد!
🔹
مطهری در نامه‌ای به رئیس‌جمهور با تأکید بر لزوم توجه دولت به موضوع پوشش در جامعه نوشت: در سطح جامعه و خیابان، مواردی مانند بدن‌نمایی، استفاده از ساپورت به جای شلوار برای بانوان و شلوارک برای آقایان باید به‌صورت نامحسوس تحت نظارت و تذکر قرار گیرد.
🔹
نوع برخورد با کسانی که پس از تذکرات مکرر همچنان اصرار بر ترویج سبک زندگی غربی دارند می تواند در آیین‌نامه‌ای که توسط دولت تهیه می‌شود مشخص شود.
🔹
‌عدم نظارت بر این موارد ناهنجار می‌تواند به گسترش روابط آزاد به‌جای ازدواج منجر شود و در نهایت بنیان خانواده و روحی اجتماعی را تحت تأثیر قرار دهد.
🔹
این موضوع از خواست اکثریت قاطع مردم است و دولت باید نسبت به آن اعلام حساسیت و برنامه‌ریزی مشخص داشته باشد.
‌
🔗
متن یادداشت را
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/456571" target="_blank">📅 17:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456570">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIxA3_8TpAqnAYWPg7jy_uyC-ADWmS19UbV2Hy0ECkubqA6JLx3_HB1UOzGGXOXvm1SmqGWiTJ36X-KXIO1-VQ6cZL2az1c95VjVvbkB_0HBqVQ8qk96WJqYuRMqPIYie23_y6rRjVImsWEZyghF8zQ4A-zuOQXPxBm_twAWX-99RrpWbkdiWPpfcRenkHYkcvx-Nq9Dgc9kaNtK8YHXSTVqfRorgZlh5hrcOtOHJ7elsRU2pGCZ6ELvf0MIU6wWVYtZHKcXvy0C8IHzAIgEvUIIye6AYKYvv87tk4kUe926XOWTmX2IjX9I1cO-fz_ZmM4C1t3IXXkrj65HTVpTbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدهی ۶۰ همتی بیمه‌ها مانع رسیدن دارو به بیماران
🔹
این روزها گلایۀ مردم از کمبود اقلام دارویی زیاد است و تصور این است که بخاطر جنگ، داروهای اساسی به دست بیماران نمی‌رسد؛ درحالی‌که صبور، عضو هیئت‌مدیرۀ انجمن داروسازان، به فارس می‌گوید: «دارو در شرکت‌های پخش موجود است اما داروخانه‌ها توان خرید دارو را ندارند.»
🔹
او می‌گوید: در حوزه داروخانه‌ها، مجموع مطالبات مربوط به بیمه‌های پایه و سهم ارز، از ۶۰ همت عبور کرده است. تسویه‌نشدن مطالبات داروخانه‌ها باعث شده بسیاری از آن‌ها نتوانند چک‌های خود را پاس کنند. آن‌ها با مشکل نقدینگی مواجه هستند و به همین دلیل توان خرید بسیاری از داروها را ندارند.
🖼
اما چرا بیمه‌ها مطالبات داروخانه‌ها را چندین ماه با تأخیر پرداخت می‌کنند؟
پاسخ
را اینجا بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/456570" target="_blank">📅 17:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456569">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqbewKKeRTCZQYg8SVgmpoJ7rXAF72mxccRxHGYR-218rsrkdvVzQ48eMHO3xCRdbjRDMuN5UVopKDoDBBU91Ya0SPz3l-F_ODSx78uceOMvC_q6rKgHLybViv0vycYFHNnUPokGAU1LP_IJk591k6UtwRq86BO86_0J4qb6drntIxe4t29do-K1QuQW6DSCTVFRmudc3uepJcEXQ428a3RaDPxeujhGPjskNzhvzVPEKuoBJWQbFmke1yw9hKc9sbPbnVbeHCck2FmlIkfxhz0eOglP8Wt5kG9Lt9CWFufwcZuQ0zHTTNbHweh2D1fxV-xcU_GHpgk-qapwyxRShw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حادثۀ امنیتی برای یک کشتی در سواحل سومالی
🔹
سازمان عملیات دریایی انگلیس: ۸ فرد مسلح وارد یک کشتی فله‌بر در فاصلۀ ۷ کیلومتری بندر ماریئو در شرق سومالی شدند و کنترل آن را به دست گرفتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/456569" target="_blank">📅 16:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456568">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29848cea44.mp4?token=GCml1VQfnQa_0XOzrB4_vOBYTDeUUND6earpiNGuEHQTgJYIrY1S7Hebhi4C44BCjn5Gz4iPp15wq6bCW208GZ_0TLfeu-gAZXM14Tk_O8C8vE-fYSMFuzxB5N79P7SLyZDCbATJ9cgKVlVJX3bp8QIDSU6TgoKsuMWRdCOgpLzAXzefY43VYJuD5N65QoORKE94HyzT99r49wqtc0-U0SDEc_2qaFYwLHCDT_l2ZsY0jUKWxheznzjbCpW80X_i56Rcz-pARR5TWWhax9roE9V3-6QT13egeS4ltlTpnkoHnucpecX6pAAukwtoxqCTWxdn5yiwctdp20cArCcTYGnnSoT45PbeGrywLuAVW9QxmlHW4HDFQcICww3e4D0dmcjFzdJQqP4CnTknBM2zaECgjmww4pxCcWYnR1nwSVP-yIY127CaTbUzOzQx8V2aNSUQoJnt5rnY-qsF9Jpt5sOjGLTOow1wVJ1fBbTOU6hctSElnvdPBvX5s5CIqThSlPUE_cX9C1mJRVBe0qEl9P95eItwPXULzUF2YSCpyroKAO5ahocbCpvTiu9A0E5MMa1LCTQzrJ_sW5hRamv0ycOVrKviDPIiSr5nILVODzfucu5dAx93qXL6gHniFmxRSBd2NrTHxlKlcSL4Po-PwzclzH12FQNPMkU8WYuEXmk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29848cea44.mp4?token=GCml1VQfnQa_0XOzrB4_vOBYTDeUUND6earpiNGuEHQTgJYIrY1S7Hebhi4C44BCjn5Gz4iPp15wq6bCW208GZ_0TLfeu-gAZXM14Tk_O8C8vE-fYSMFuzxB5N79P7SLyZDCbATJ9cgKVlVJX3bp8QIDSU6TgoKsuMWRdCOgpLzAXzefY43VYJuD5N65QoORKE94HyzT99r49wqtc0-U0SDEc_2qaFYwLHCDT_l2ZsY0jUKWxheznzjbCpW80X_i56Rcz-pARR5TWWhax9roE9V3-6QT13egeS4ltlTpnkoHnucpecX6pAAukwtoxqCTWxdn5yiwctdp20cArCcTYGnnSoT45PbeGrywLuAVW9QxmlHW4HDFQcICww3e4D0dmcjFzdJQqP4CnTknBM2zaECgjmww4pxCcWYnR1nwSVP-yIY127CaTbUzOzQx8V2aNSUQoJnt5rnY-qsF9Jpt5sOjGLTOow1wVJ1fBbTOU6hctSElnvdPBvX5s5CIqThSlPUE_cX9C1mJRVBe0qEl9P95eItwPXULzUF2YSCpyroKAO5ahocbCpvTiu9A0E5MMa1LCTQzrJ_sW5hRamv0ycOVrKviDPIiSr5nILVODzfucu5dAx93qXL6gHniFmxRSBd2NrTHxlKlcSL4Po-PwzclzH12FQNPMkU8WYuEXmk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای بازار ماهى‌فروشان بندرعباس
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/456568" target="_blank">📅 16:27 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456567">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jm2gYf4C15dTBjIK5nDTPkI6vC394ExB2cuiWC6C67svOKW41XbwbJsWojYZN6H96yl7U-yOH8mhDTTkohX-dM6pst50yuOvEdO2vdXkVewTR2UI0bpJU6KG0DHLf8Fqpoj-Ae8CJuo_nR7Z-9asfqyGLo9mKP7yMqSrkQ0lohCD3PX-ySz-YRumE_QL_rqwAMcps4cILm4XUXIjy98arnqTtej_nIqAkt6C2Jn4v_vLyeWi56ac2f4kTdH-r-mvhVduqyPeXQXxmJorIUpNIRXA6zmac3Gp7SGx_z0nK-FDb_JBhhYGjPrUUJ_Mi1dgGCTysllDaIhgzb1Dx75x8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: رئیس‌جمهور تصمیم گرفته‌ پروندۀ فیلترینگ را ببندد
🔹
اینترنت یک شاه‌راه است و نمی‌توان به‌خاطر برخی تخلفات، کل شاه‌راه را بست. من به‌عنوان یک استاد دانشگاه نمی‌دانم فیلترینگ چه منافعی برای کشور دارد؟
🔹
برخورد حذفی با فناوری‌ها نتیجه‌ای ندارد، اما توجه…</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/456567" target="_blank">📅 16:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456566">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNPid1BgytfvHoqxLcDcyRO-GmM0Dh4PWhCdvE1ACmLS7kPybgnseTVOcILvLt0xG1hvodCvZqz_ZHMuRGNCQNhkzf3UaUQwL1yV31GpgNID9yJh621ncUSR9TJTSM2sCDv6uepRRmgQnfC0QvcFbeCTZMRV3p6eCjASa511O4zSg-cXTVWn_kY0pXOIMleygNQmfxXaAGJx9UqtOX3RAcTkpQLEaILnlvrSb2rHOTBIv7qUJS8tC1Mxj6VYjzxuFWxKTzYGMPj2dgLscCXlamYtoLgp6W67JiIk539Q5BzA-D-_mLVJQWU8Cx2rKnDjwHKKR_jKXSdWRN08XTWaew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: دشمن برای کودتای جدی اجتماعی-فرهنگی برنامه‌ریزی کرده است
🔹
دولت پیش‌بینی وقوع جنگ‌های ۱۲ روزه و رمضان را کرده بود و برای هر دو جنگ برنامه تهیه کرد، اما آرامش جامعه را بر هم نزد.
🔹
اکنون نیز کماکان هدف دشمن سرنگونی جمهوری اسلامی ایران است و برای کودتای…</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/farsna/456566" target="_blank">📅 16:11 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456565">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سپاه: پاسداران انقلاب اسلامی هرگونه تهدید و تعرض را با قاطعیت تمام در هم خواهند کوبید
🔹
بیانیۀ سپاه پاسداران به‌مناسبت ۲۶ مردادماه، سالروز ورود آزادگان سرافراز به میهن: آزادگان سرافراز آموزگاران مقاومت و ایستادگی، نماد حقیقی مقاومت فعال و امید آفرینی راهبردی هستند.
🔹
سپاه پاسداران ضمن گرامیداشت این روز فرخنده به ملت شریف و مبعوث شدۀ ایران اسلامی، اطمینان می‌دهد که پاسداران جان‌برکف انقلاب اسلامی در این مقطع حساس به تأسی از ایثار و مقاومت و ایستادگی آزادگان سرافراز و با اتکال به خداوند متعال و تحت تدابیر و رهنمودهای رهبر انقلاب، با تمام توان و آمادگی، هم‌افزا و هماهنگ با سایر نیروهای مسلح مقتدر کشور، پاسدار حریم انقلاب اسلامی و حافظ تمامیت سرزمینی، استقلال، عزت و منافع ملی کشور خواهند بود و هرگونه تهدید و تعرض را با قاطعیت تمام و با بهره‌گیری از راهبرد بازدارندگی حداکثری و عملیات تهاجمی پرقدرت، در هم خواهند کوبید.
@Farsna</div>
<div class="tg-footer">👁️ 8.3K · <a href="https://t.me/farsna/456565" target="_blank">📅 16:04 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456564">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9fIs4mJEOOPNpJ7im1GCDwCxiFS7e-SaXhiu1lvABpGZwl4A7w8YX9tU4mE2VFzxUl96W6wpbqFVm36aZOL7g1RmiZS0mdm1F3fmvj5s-DX33nBA_6xH3QrIyld_dSsQi-hl7ZLblE_OlxUyzmhQ9Dm4RXhK-WNZHsPLp43gVguNkd7iWtZBcmkVbPHGLCa8_HIzonDdBrIec-1n6AMy637G_cZUH6v9_UtiEc75BL-F-s3ZfIp7vMzXWGuoQJfMrtsZ62XcowTfnHGua6kRE2IRo6tX_2RDd8N2bmDBGKF6pT7Ptq0xKVty89n3VwlGdwmzHUQxUNyddwZIpoGEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: دشمن برای کودتای جدی اجتماعی-فرهنگی برنامه‌ریزی کرده است
🔹
دولت پیش‌بینی وقوع جنگ‌های ۱۲ روزه و رمضان را کرده بود و برای هر دو جنگ برنامه تهیه کرد، اما آرامش جامعه را بر هم نزد.
🔹
اکنون نیز کماکان هدف دشمن سرنگونی جمهوری اسلامی ایران است و برای کودتای جدی اجتماعی-فرهنگی برنامه‌ریزی کرده است.
🔹
دولت بنایی برای اقدامات آنی و بدون اطلاع مردم ندارد و اگر رسانه‌ها دیدگاه منفی افکار عمومی دربارۀ برخی تصمیمات را به اطلاع دولت برسانند، دولت اجرای آن تصمیمات را به تأخیر خواهد انداخت.
🔹
من نقدهای رسانه‌ها درباره تصمیمات دولت را هر روز مطالعه و برای وزرا پی‌نوشت می‌کنم که آنها را پیگیری کنند.
@Farsna</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/456564" target="_blank">📅 15:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456563">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444fabb1ff.mp4?token=voG53EU6pF4ht72u4F8F0zmaprofMZU5_cnwFOTJXAlUFX4c_YlRUhWxVxbvso3evqrPuhyMyxvNM24sq4JDYqRW8Jlv-OMQfVURaoEAUnjvvtqwe-Ap6YFYYLm0QbZQC8ogJcMLFnRN4mM-Fg3IRLayMUasu3Lw8jJGvmQ2NQMRm2M-2a46XiMsUjKtv3RMaoUpPZIBrL9lJcLV7-3lV_mw75F8qoqTbJ_QkDBj3Xbk7G26oTHPxPoQ0lTpxpXXo6KCuOs1Q0Xwuma1ShYJMohCRphVRFThyDiM6eWbJLgYGElnxoW5iSo0_hOWvz_6mj7Y9zA9g_UHina0EJ3yuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444fabb1ff.mp4?token=voG53EU6pF4ht72u4F8F0zmaprofMZU5_cnwFOTJXAlUFX4c_YlRUhWxVxbvso3evqrPuhyMyxvNM24sq4JDYqRW8Jlv-OMQfVURaoEAUnjvvtqwe-Ap6YFYYLm0QbZQC8ogJcMLFnRN4mM-Fg3IRLayMUasu3Lw8jJGvmQ2NQMRm2M-2a46XiMsUjKtv3RMaoUpPZIBrL9lJcLV7-3lV_mw75F8qoqTbJ_QkDBj3Xbk7G26oTHPxPoQ0lTpxpXXo6KCuOs1Q0Xwuma1ShYJMohCRphVRFThyDiM6eWbJLgYGElnxoW5iSo0_hOWvz_6mj7Y9zA9g_UHina0EJ3yuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سرلشکر ایزدی: با یک‌صدم هزینۀ دشمن، در جنگ اخیر بر آنها غلبه کردیم
🔹
نظامی که مبتنی‌بر ولایت فقیه است توانسته با یک‌صدم هزینه‌های نظامی دشمن، جنگی را اداره بکند که خروجی آن پیروزی نظام اسلامی و رزمندگان اسلامی است.
🔹
اگر تحریم‌هایی که غرب بر ما تحمیل کرده،…</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/456563" target="_blank">📅 15:46 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456562">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1344ab35f9.mp4?token=hAkvXUpkPau_2-bxBqNYdZrnCEf_sS-UJVkXEF8EnG4lnzzcLejf4v-awElkjtOeN2kj3tfuoFmHcubmLJy0XD6kbmnw96oBapVJ83Abzz8FL84Vu0sfnGyub--ib_keFUPB_ilDPX5o_1P8zE7ObKF-eLMb9u9G8lTnqyDIbw0UQpu25yfEPKnLDE6LtBFeQR260Tzhxj87D-s0LDzAoJ1VT0MVB1u4LPSwIM9hDjD7O7T66DIB8iuA6JujO7Yb3qGEC8oLta7Ttilx-CHkhN14u0YzQT6fbwkFXBOFkl09zQWnCORSkikeS_sE-5lpW3ZKa861a56eBvnuetHOHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1344ab35f9.mp4?token=hAkvXUpkPau_2-bxBqNYdZrnCEf_sS-UJVkXEF8EnG4lnzzcLejf4v-awElkjtOeN2kj3tfuoFmHcubmLJy0XD6kbmnw96oBapVJ83Abzz8FL84Vu0sfnGyub--ib_keFUPB_ilDPX5o_1P8zE7ObKF-eLMb9u9G8lTnqyDIbw0UQpu25yfEPKnLDE6LtBFeQR260Tzhxj87D-s0LDzAoJ1VT0MVB1u4LPSwIM9hDjD7O7T66DIB8iuA6JujO7Yb3qGEC8oLta7Ttilx-CHkhN14u0YzQT6fbwkFXBOFkl09zQWnCORSkikeS_sE-5lpW3ZKa861a56eBvnuetHOHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آب از پروندهٔ مسمومیت‌های «باینگان» کنار رفت
🔹
معاون بهره‌برداری شرکت آبفای کرمانشاه: درپی مشاهدهٔ علائم گوارشی از جمله اسهال و استفراغ در تعدادی از شهروندان باینگان، نمونه‌هایی از منابع تأمین آب این شهر آزمایش شد.
🔹
براساس نتایج آزمایش‌های انجام‌شده، تاکنون هیچ‌گونه مشکل شیمیایی یا میکروبی در منابع تأمین آب باینگان مشاهده نشده است.
🔹
وضعیت منابع تأمین آب باینگان با دقت درحال پایش است و بررسی‌های بهداشتی و آزمایشگاهی تا مشخص‌شدن منشأ بیماری ادامه خواهد داشت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/farsna/456562" target="_blank">📅 15:39 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456561">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwuSBBksjdua4ZFUyBD92s054lZUbmC06Mqiy1Kb2PBl9T66pby16g1TjbimV0ONvc_1jvE-LcLoCTw_R579KHeRXNzDXIcNVMfi5fUxg9PFrUTbW3GBOj0qEbOOa4-k-X4B59yu80PQk40d9Dl3_nC45-6BZGACvjD2aJ9wvFKvMGSPkbhCZMcXs0eC57-690pNlbdKfRn9jpDvclSeJHdaifEvXGsmdDl1cUdsgYMcKFl3Daz6kfpRyEq6SnkbRz9Sz20ixeiGdCDw4VpmWT5oioFGdGkeigNtEze5IEEU5NicTHvM2AvQZK-dHsWBNAyBTGLqZod6zBQXl9-_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر عمان در خصوص تنگهٔ هرمز مانع‌تراشی کند، ما آن‌ها را به‌شدت بمباران خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/farsna/456561" target="_blank">📅 15:32 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456559">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gDF-DZyXo1jKK6yMjud1zxoFaUKmxM-vM0K-aEzpmPtgZJoehfQ6jhZQMcif0E-MYdVqI6MuGokKiWT6taD3AgeQIgPRwTfbr_kpy4_5W-9-JGujHx9M7shR4kbwAJifU0dDtQ_jcNAgNzo0AyxzvhaP2KOMjgRLD5QOsGmmdDdhv04Fa-wj4qHTFi_0Qd9zBITR1py1Xg7nowvqqrRZ80sInaqJ-lqYeNjeJ7pxFM-pR0lGyqZFgXEo2gnvY7monrrU1rcyAndcRl_UXbUkalgu0CCj4q3gOmC3w12Y5MlEOYle_2Iw79F3NCWGefZxCZ6X3bIGI2QmB_KpM-C7JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: اگر عمان در خصوص تنگهٔ هرمز مانع‌تراشی کند، ما آن‌ها را به‌شدت بمباران خواهیم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/456559" target="_blank">📅 15:25 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456558">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
سخنگوی نیروهای مسلح یمن: یک کشتی سعودی را هدف قرار دادیم
🔹
نیروهای مسلح یمن توانستند یک کشتی نظامیِ حامل نیرو و تجهیزات متعلق به دشمن سعودی را به همراه چهار قایق نظامیِ همراه آن در دریای سرخ، مقابل سواحل المخا، با چند فروند موشک بالستیک هدف قرار دهند.
🔹
این حمله با دقت و به‌صورت مستقیم انجام شد و در پی آن، کشتی به‌طور کامل آتش گرفت؛ همچنین تعدادی از قایق‌ها غرق و بقیه نیز دچار آتش‌سوزی شدند.
@Farsna</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/farsna/456558" target="_blank">📅 15:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456557">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuQVOtZ47_bmo0rN2_USpxlLvhyyYDwbeybrrRzmutdtP9x4tvK0tw1Df4GmmsFSqu9mLu1_D9TIAoi4T579G27ztIHr9LfM31gNrQ_W_0PnJq6EZdY8wHbDmG8L5YAjWIMovrPwrX2-Tds5GqtdaLKqhp3sebENK756AhWXa92XsX-vBdpMzXrhvE-o1UvN0-shKC-BPU_bEQ0JxGAXsDv__FCUbt772ZQNqoUoNIVEbpB09k4Cxhv7jKgJW_eGGoXqOOyZyXHjVcuSNovFcl3hK_xqDReRbq1HueudwjjR61m-KgijpZmpYhEgO6ezYNVhn_SyFT99RjiMvsKHyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دانیال ایری با عقد قراردادی ۴+۱ ساله به پرسپولیس پیوست
@Farsna</div>
<div class="tg-footer">👁️ 9.82K · <a href="https://t.me/farsna/456557" target="_blank">📅 15:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456556">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630026d9ce.mp4?token=A75J10k6m_gyLGm2R1HL2f8zLb4lfUY9hEq-zjKGPBuwoj5fTxE_RK9pnKWu6FwfI0McCGDLgXNGG4b5cgQo8Y4ltyo9L_IKstzraXF_18SafLdTDlfOu5iKd6yJOspTFn92WPAhbOxb9KkFG7YMVRsQPR2zNg_gom4lEAvE_aZNC5lBLAtYVZl61emZd6_UihP5l2KIqu-ObL3LEmjXmbXCI6kj972sWM3NcbemJRLmA44VgvNoei9X2ra1LHzwFTXQEUYT9J8x8rh5o6gdU1hCrw6ovUt5b1pyifYoSaUAVr9MR8xfhG3MGXAI3TX6_bcPls_XZGGC2kjg3_4PEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630026d9ce.mp4?token=A75J10k6m_gyLGm2R1HL2f8zLb4lfUY9hEq-zjKGPBuwoj5fTxE_RK9pnKWu6FwfI0McCGDLgXNGG4b5cgQo8Y4ltyo9L_IKstzraXF_18SafLdTDlfOu5iKd6yJOspTFn92WPAhbOxb9KkFG7YMVRsQPR2zNg_gom4lEAvE_aZNC5lBLAtYVZl61emZd6_UihP5l2KIqu-ObL3LEmjXmbXCI6kj972sWM3NcbemJRLmA44VgvNoei9X2ra1LHzwFTXQEUYT9J8x8rh5o6gdU1hCrw6ovUt5b1pyifYoSaUAVr9MR8xfhG3MGXAI3TX6_bcPls_XZGGC2kjg3_4PEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سبوس</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/456556" target="_blank">📅 15:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456555">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7bcb0b00.mp4?token=D2Ck_IJdWSjbQUHBhe3KHjMr2QgIBJ8I9wnNyByTV3JE5AJ9qrNrqhtzF2Do74l8SDyA21R09nV6sFG6aRfJQ4ZZn09jl-0wkhFFbos9opnHBTTM7ijfkmUQgn--xsj31Of1bXNU7fG3M92OPOZHY0kOId53rdHeQw6UHVNwi7UUqbENtwypowtUHc1H5DvX90_BkgZ6GE82aiIeOtAsNRnR9-0bR9JnvOgntOJXREZbXJz9KUXIaU5y0sbRsF0tcPyQm5M04cJ-oo35ZwEzsOcxIhT5-uv3JeFI8b45f1gKypcRIvh32FC_qzzq8fpUSojuYhx1N2wpGvF_3fIi3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7bcb0b00.mp4?token=D2Ck_IJdWSjbQUHBhe3KHjMr2QgIBJ8I9wnNyByTV3JE5AJ9qrNrqhtzF2Do74l8SDyA21R09nV6sFG6aRfJQ4ZZn09jl-0wkhFFbos9opnHBTTM7ijfkmUQgn--xsj31Of1bXNU7fG3M92OPOZHY0kOId53rdHeQw6UHVNwi7UUqbENtwypowtUHc1H5DvX90_BkgZ6GE82aiIeOtAsNRnR9-0bR9JnvOgntOJXREZbXJz9KUXIaU5y0sbRsF0tcPyQm5M04cJ-oo35ZwEzsOcxIhT5-uv3JeFI8b45f1gKypcRIvh32FC_qzzq8fpUSojuYhx1N2wpGvF_3fIi3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رکورد زدیم؛ البته در کاهش زادوولد!
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/farsna/456555" target="_blank">📅 14:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456554">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AYhaAuWt7pwMcoK7bdgvPJevdp512JOcDip6FQa7J7uC2j-38mkwujOJZd2ou0aCSCtegROIO9dwcDcTFiDA96PF9-UgaPCRQVpKOdttp8CWk00YOi2BQTMJZBe8oPyfWMsdSwpTjF07EZCbyAxnUApnDj2nNR-Kn4FIB04QwnhajkGK3V-8ZpDTKx3k7-IH-ZCYrwjXa0kc8JKY27uLRAWdlFPG58iOnM1CyJWAh2urohSljxLoo5LzQ3atsy3Qn2EYcVmYlyAQn0Ea1tVqTaJJMLu315QSLZDWWxDG_vT8S6AlxNlAFJFvmcv5JOqcf2t-moU20B-nLnRy1OziwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هدف نخست ترامپ از جنگ با ایران: بازگشت به قبل از جنگ!
🔹
جی‌دی‌ونس، معاون رئیس‌جمهور آمریکا در مصاحبه با فاکس‌نیوز گفته که نخستین هدف کنونی دولت ترامپ، حتی قبل از توافق هسته‌ای با ایران پایین آوردن قیمت نفت و بنزین است.
🔹
چندماه قبل‌تر سخنان مارکو روبیو،…</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/farsna/456554" target="_blank">📅 14:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456553">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفالس نیوز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/900d69e35d.mp4?token=uF5lKF8DGtCFy0dKucdmhsnD7BddTdzfK9sWhCBEhmPfjBYsNLJhj0qcKERDZvb_cgyBkFu56tx3dIUaV-40qc2iLB4msWjU8xh4tmTUX6W-2hL7sQ2ovMTB8JY9zTybo2UKnUq1qVGOwnNaX-GOsprYUmj9qGYt2TQEbiPpkZ7nf7u5K_8VSldwm_ebc7iQtf8HONMVDAapcaw58SrXNCN1C95qAUYKI8khOSW8k-77-4vlAx6Ksj8r7j8iSDxcvap2s3szhqi5dCZFEcQKzOMAR4rMuVhPO-FzWFD20_X4ci_pyTzopvcvg6aVaW8GmskqZvyM0tugJuOnzvxhyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/900d69e35d.mp4?token=uF5lKF8DGtCFy0dKucdmhsnD7BddTdzfK9sWhCBEhmPfjBYsNLJhj0qcKERDZvb_cgyBkFu56tx3dIUaV-40qc2iLB4msWjU8xh4tmTUX6W-2hL7sQ2ovMTB8JY9zTybo2UKnUq1qVGOwnNaX-GOsprYUmj9qGYt2TQEbiPpkZ7nf7u5K_8VSldwm_ebc7iQtf8HONMVDAapcaw58SrXNCN1C95qAUYKI8khOSW8k-77-4vlAx6Ksj8r7j8iSDxcvap2s3szhqi5dCZFEcQKzOMAR4rMuVhPO-FzWFD20_X4ci_pyTzopvcvg6aVaW8GmskqZvyM0tugJuOnzvxhyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقطیع صحبت‌های مجری صداوسیما دربارۀ «جنوب ایران»
🔹
به‌تازگی ویدیویی در فضای مجازی منتشر و ادعا شده است که مجری صداوسیما در آن می‌گوید: «جنوب ایران فدای جنوب لبنان».
🔸
اما نسخۀ کامل ویدیو نشان می‌دهد این عبارت، نقل‌قول از وطن‌فروشانی بوده که پس از حملۀ آمریکا به مدرسۀ شجره طیبه میناب در هرمزگان، از این حمله ابراز شادی کردند، اما بعد از حملات آمریکا به جنوب ایران، خود را دلسوز مردم این منطقه نشان دادند.
@Fals_News
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/456553" target="_blank">📅 14:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456552">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">‌ سرلشکر ایزدی: در جنگ اخیر بیش از ۲۰۰ هواگرد دشمن ساقط شد
🔹
جانشین فرمانده‌کل سپاه: در جنگ اخیر نه تنها ایران اسلامی تجزیه نشد و خدشه‌ای به نظام اسلامی وارد نشد بلکه خود را قوی‌تر و استوارتر به دنیا نشان داد
🔹
بزرگ‌ترین قدرت نظامی جهان و قدرت نظامی منطقه…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/456552" target="_blank">📅 14:33 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456550">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc20e07ba.mp4?token=Xij-WEtjC0mRH8sK0FYQo166OfbDJsCHit2-fZT6HX8BlQ2gJyAFM4sdk75oNwetn7G98hVbpCPQcu_INaD-RxmSnm2IoauANhmsU4CXaU0DFhjAtFKkatJHSsovXnawPGY53nQsQCRWBbKk6Mv8dhozuvI_BXxtUsj0gLR_o3CW4qxVVYz0Ev-EjO4c5Ll1qyk-RtOwFrlHKI_5-g9ejrswrJn3ENKAk3pahGKxrSfZkASYTTYTlJu4-W9T5OeNboTF-kTNxW7FtznlUpQ7cHESQ6jamnJCMmz5MBPoXMXNpsLHbC3J6YJHzSzfgw4hTpAJPJnKvn9GUggexcPnCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc20e07ba.mp4?token=Xij-WEtjC0mRH8sK0FYQo166OfbDJsCHit2-fZT6HX8BlQ2gJyAFM4sdk75oNwetn7G98hVbpCPQcu_INaD-RxmSnm2IoauANhmsU4CXaU0DFhjAtFKkatJHSsovXnawPGY53nQsQCRWBbKk6Mv8dhozuvI_BXxtUsj0gLR_o3CW4qxVVYz0Ev-EjO4c5Ll1qyk-RtOwFrlHKI_5-g9ejrswrJn3ENKAk3pahGKxrSfZkASYTTYTlJu4-W9T5OeNboTF-kTNxW7FtznlUpQ7cHESQ6jamnJCMmz5MBPoXMXNpsLHbC3J6YJHzSzfgw4hTpAJPJnKvn9GUggexcPnCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بلاگری که به مقدسات توهین کرده بود  دستگیر شد
🔹
قوه‌قضائیه: درپی انتشار ویدیویی توهین‌آمیز در فضای مجازی از سوی یک زن بلاگر، با دستور مقام قضایی متهم شناسایی و دستگیر شد.
🔹
برای این فرد پروندۀ قضایی تشکیل شده و درحال رسیدگی است. @Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/456550" target="_blank">📅 14:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456549">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EtBn22awwS49YkMmrTx15qlcZxCYo8q1OBXzzCU-EdwcokM3Jwd0Hc4TKIEFJeo7WwHKrjX2iYKrhH1V2bW6jnnuNBcxCwO2zexV07eLhlX4JYz0oAkH5aP9oxRBonViyCW6OlNHEjVdLWqc-jcwSBrt18X1QIj8eo2BiGFmptnZ71C9rfZeYkAtbYj1JmafGAoVhSQUrK2_aO7JmPlCoTPoEygf-Z0u7dVjCk6Md_q7V0n6t9KqMGWgjuiRcLPz3JRGG1o46istE4j5Rb-ccU4Z96MRMmjq6qsCJG5_DnEHIFXJnHHC92gL8a18kaBHVnY4iN59kboWGkF4Ktz4nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی: معادلات منطقه تغییر کرده و امروز خانوادۀ آمریکایی هزینۀ قمار سردمدارانش را نقداً می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/farsna/456549" target="_blank">📅 14:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456548">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: خودروسازهای داخلی هیچ‌وقت هزینۀ خودروی پرمصرف و بی‌کیفیت‌شان را نداده‌اند، فقط مردم و بیت‌المال این هزینه را می‌دهند؛ ما باید ریشۀ این موضوع را بخشکانیم.  @Farsna</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farsna/456548" target="_blank">📅 14:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456547">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTdWhUon7zjVpwptMHh1QekQnrzwjNVQ3CeotzK6ed48PxhZ28PunqFRuWODhH0YmMBwGj64QXYFbZSJ5m8ovod2QBZGxJrkPSkugbEtzdHRSHBhxtgTuSFoe77UDLtSZdaQ3cPhX3zYhqR1aHRgq82GuYL1vnP80ajrXVIfp_4dVfHgpNf6NgC_O0wKUrZMHTBxxJ5p78Bp94EXiB4FgO2XgHxcMZ5j-q1vXIDaO-eddY2yLyfeCMou_RJpfCqjGr640DVMnWt6r10EV1wAxaxo_1ZQ2BgLHNT-m_PH5HeMFspFrD7JRH5b8KS1YQJ95eRHIbd2Hv85sTClJnvPgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: رسانه‌ها در جنگ اخیر
پیوند خیابان، میدان و دیپلماسی را ساختند
🔹
امروز رسانه‌های ما به‌راحتی توانستند عرصۀ جنگ را شناسایی کنند و جنگ را علاوه‌بر عرصۀ زمینی، به عرصۀ اذهان بکشانند و اجازه ندهند دشمن در عرصۀ ذهن‌ها تصرف کند و یک جنگ ذهنی و جنگ ادراکی را شکل دهد و بتواند ادراک جامعه را مدیریت کند.
🔹
رسانه امروز علاوه‌بر روایت‌گری و واقع‌نمایی، واقع‌سازی می‌کند. رسانه امروز بخشی از جنگ و بخشی از سازوکار جنگ است.
🔹
در جنگ اخیر رسانه‌ها به خوبی توانستند رابطۀ بین خیابان، میدان و دیپلماسی را برقرار کنند و این رابطه را در اذهان مردم و جامعه تثبیت کنند و از هرگونه رخنه برای تفرقه‌افکنی مراقبت کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456547" target="_blank">📅 13:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456546">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">جانشین فرمانده‌کل سپاه: ملت ایران دستاورد ۳۵ سالۀ دشمن را خاکستر کرد
🔹
سرلشکر ایزدی: بعد از فراز جنگ رمضان یک وضعیت بدیع و جدیدی را در صحنۀ جهانی منطقه‌ای و حتی کشورمان ملاحظه می‌کنیم.
🔹
به عبارتی ما در این فرازی که نقطۀ عطف آن شهادت جانسوز قائد امت بود با…</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/456546" target="_blank">📅 13:21 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456545">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488dfc14ab.mp4?token=ACVbCR7PFT56NRwNdqtEpqImpwv8Y_llKH9o67G7avMyvq38mPQ6VUfJEht91GQEXdIUr0PKk__UZOPCWmc2S__J1ITeyzp9X19-24vMgo7N_xnv3yLKK1mOsxXOO_v5z-LEjITQGTJi1V6hjjbPkYJkOA_sFyYD9BU1Ma88iHbVFRCuYY3kmtEehrocZjA5ca7O1FhLvaCrXjzI78oXIGAlM2hiDVjVK2YYpKuc3dVNy8J4HDJnLh_CB3_7926YIi7vBKsWoIjhxD2CpvoQ4FXJ8SZPE0oiEVjJJBT2eDmU-GnT1vN5isIWB3MX2K6G-N6tFKYVKdBAYiyVlBsmtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488dfc14ab.mp4?token=ACVbCR7PFT56NRwNdqtEpqImpwv8Y_llKH9o67G7avMyvq38mPQ6VUfJEht91GQEXdIUr0PKk__UZOPCWmc2S__J1ITeyzp9X19-24vMgo7N_xnv3yLKK1mOsxXOO_v5z-LEjITQGTJi1V6hjjbPkYJkOA_sFyYD9BU1Ma88iHbVFRCuYY3kmtEehrocZjA5ca7O1FhLvaCrXjzI78oXIGAlM2hiDVjVK2YYpKuc3dVNy8J4HDJnLh_CB3_7926YIi7vBKsWoIjhxD2CpvoQ4FXJ8SZPE0oiEVjJJBT2eDmU-GnT1vN5isIWB3MX2K6G-N6tFKYVKdBAYiyVlBsmtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملهٔ مجدد پهپادهای اوکراینی به مسکو
🔹
اوکراین یکی از بزرگترین حملات پهپادی به مسکو را انجام داد و انبار فروشگاه بزرگ اینترنتی وایلدبریز (Wildberries) را به‌آتش کشید.
🔹
وزارت دفاع روسیه اعلام کرد دیشب ۸۰۰ پهپاد را رهگیری کرده و شهردار مسکو هم اعلام کرد که…</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/farsna/456545" target="_blank">📅 13:20 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456544">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q87TPguft236LJTtgk8O3WkxiVPEh6oxhMS2Wc9dZhtpk2q_pldB6hw41ypmGOwugDOEvS1IqdqbXzCE03BnrGfkv8uAFfeEK8RfLhpc6eV8MKrMTjceYRMxDiuFZhdRY_gZ23ALpGxMAV_h1SPUO3Fl-sehNpQWBNRiyiDQlXY6s7xvkju3RpUXFaveii7upt3AHnN2H8VOYGwxaGXy_YBKHUcW-OlhDjOEQUbZIEbn4UIbZWIxLBtSDu6E8unC6X_V5XyigDTP9BUGCgHHaYragt8RSDLmdwXJkZs4FXpxeVztiSUQO2QvwgZyAeMSvRjuPfVd2xvLN5lP0DA-6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اربیل مدعی حملهٔ پهپادی به دفتر مسرور بارزانی شد
🔹
تشکیلات «مبارزه با تروریسم کردستان عراق» مدعی شد که ۲ پهپاد انتحاری دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق را هدف قرار داده‌اند.
🔹
طبق این اطلاعیه، ساختمان سازمان امنیت داخلی اقلیم کردستان نیز هدف این…</div>
<div class="tg-footer">👁️ 9.61K · <a href="https://t.me/farsna/456544" target="_blank">📅 13:15 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456543">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62513eb08a.mp4?token=kxH_FBryMAoU4zKzX87dmhJoOTo6fhBqy2UpaIF8RG2NXbU-2V7tVCCgVIFqcLnFUwKvglWG5hEH3vLtHLFHjbqFylycRh2l6dwm7N0fxDNTIopopOK2_Uz5L0RziDQZ7QGyIvQ0GxC6532to4A1K1YIdYf2frlE_9faPlxll_dWG-QxVlfX48nJ0EmMMSUE7NakZDuea3FUnpi_-92V7ILry8DS_COknpVhyQjmWP4sPwDu25zChmOCgTjo6eu4rh3xC2uRydIGAiVE_8LDQUUoZATNAZnbsDI3kpQJh2fFtikpqfByes27oLSBXk8pL8T2wKtwZl6TMLjKANmjBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62513eb08a.mp4?token=kxH_FBryMAoU4zKzX87dmhJoOTo6fhBqy2UpaIF8RG2NXbU-2V7tVCCgVIFqcLnFUwKvglWG5hEH3vLtHLFHjbqFylycRh2l6dwm7N0fxDNTIopopOK2_Uz5L0RziDQZ7QGyIvQ0GxC6532to4A1K1YIdYf2frlE_9faPlxll_dWG-QxVlfX48nJ0EmMMSUE7NakZDuea3FUnpi_-92V7ILry8DS_COknpVhyQjmWP4sPwDu25zChmOCgTjo6eu4rh3xC2uRydIGAiVE_8LDQUUoZATNAZnbsDI3kpQJh2fFtikpqfByes27oLSBXk8pL8T2wKtwZl6TMLjKANmjBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اژه‌ای: در دورهٔ جدید قوه‌قضائیه انتصابات جدید انجام خواهد شد
🔹
برخی از افراد دور همین میز ممکن است به‌دلیل ایجاد تحرک، جابه‌جا شوند.
🔹
شخصاً پیشنهادات افرادی در دستگاه‌هایی خارج از قوه‌قضاییه از جمله سپاه، وزارت اطلاعات و برخی مسئولان سابق در دستگاه قضایی را دریافت کردم.
@Farsna</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farsna/456543" target="_blank">📅 13:00 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456542">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r4SDrz86quS3uD-9___-xuQlYINLiynaF7wyebrnFEdVmpxSYkt-X-HWT58CWG9ZWqGvzystGbWIaOMdfLclPrkhCeUshoKIpvx36KXbD5PZ_-lF0CQ4LYV8OFYptYm3O9O37N-x_0fQoMAtqI_WksyDdQR3qRb-Ni1_wL5g92gwrz_ygohlogdOHa4uO-vODv4oY2vlGjgaQYiIkJmZGIU1M3exxPcA6rqub26W9khIrvRCtTGEnBK0Ivt6x8E3EOQEmiYJBC9q-LZ6stDfGZWG9Uh6R6ryffEAQr4fDe556r_GC8PL8Bz4mYNoKjqtGP3VJ-6fUKeVnGHyd29gGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جانشین فرمانده‌کل سپاه: ملت ایران دستاورد ۳۵ سالۀ دشمن را خاکستر کرد
🔹
سرلشکر ایزدی: بعد از فراز جنگ رمضان یک وضعیت بدیع و جدیدی را در صحنۀ جهانی منطقه‌ای و حتی کشورمان ملاحظه می‌کنیم.
🔹
به عبارتی ما در این فرازی که نقطۀ عطف آن شهادت جانسوز قائد امت بود با یک بعثتی در جامعه مواجه شدیم و یک نگاه متفاوتی به انقلاب اسلامی و جمهوری اسلامی در جهان را شاهد هستیم.
🔹
این بعثتی که اتفاق افتاده یک ترجمانی دارد؛ این بعثت نتیجۀ بعثت درونی انسان‌هاست.
🔹
بعثت و بیداری ملت ایران در جنگ شناختی، دستاورد ۳۵ ساله دشمن را خاکستر کرد و جمهوری اسلامی را قوی‌تر و استوارتر از گذشته به میدان آورد.
🔹
دشمن اهداف مقطعی را دنبال نمی‌کند. هدف اصلی آنها مقابله با مبانی دینی، علمی و هویتی ملت ایران و به‌دنبال تضعیف پایه‌های اصلی نظام است
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/456542" target="_blank">📅 12:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456541">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kF0V4B0Qs8CSL1hX3Sm7RBYdRPKwtfxl3nu3O0eJKEZECHNMtj6Xv--zyGbPHxHTs9gle4o20BZ3ij7olnpvaCRZ1h16aayjhOwdGx9djMc1O2f3TvxHVBkvSgJXknQfkTBDMKtJT6zm1Hz-s4KCmFwWQg7ut-F8jXSCcJ_euWPR780SAvT6rsLHDYqj6sXS2GUaF13cGSQD5kjMcY9Jh4CSXQfnah-mUbUwxG-kE1AEA2jXh77vYgC1GGFNMziL0Uc5GhSXRcA-62u2hzwbimYOiHUJv-keNwXiZcoxeEoDgW0oFvhcXPl-SHWauFAEGLDOYqezqHYt_73CAUJUBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رکورد جدید بورس در مرز ۵ میلیون و ۹۰۰ هزار واحد
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۱۳۲ هزار واحدی به ۵ میلیون و ۸۹۸ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/farsna/456541" target="_blank">📅 12:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456540">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iX-N6Xigziku_awR91PQWghBqTKqIDz2G5O2C_-ASGjGG97ucSV_bwY6RHfeQP2GTdN0mUIpv2ccSGo6f9KBsr9ji9sWi3vyY6ULMv6of7XXRQg7R7qum4oLXOs_DIl92vYt3OGKEur9CedLP4qXc9OiVaKhzEzSgetfVN-sKLihgH4d0QE6OJcS5PWSpGXrRrxzmKC-5cvmd4ho2T-2JaLbuZEDsCwgqO5b-eMlz85u3NPMmsDnhx4j0XwpGQymRUw2WrI44YFkTGiSNEHyCdqbV4ZRhw8v9Afh0IgoPnAb60II8lM38fnY6wNCtriMCMGYUJX4kUQxhtkVDzdBCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی‌صادقی: هدف اصلی دشمن فرماندهی افکار جامعه است
🔹
نماینده ولی‌فقیه در سپاه: دشمن برای ایجاد شکاف و از بین بردن انسجام جامعه با استفاده از ادبیات دینی و حتی با عنوان دفاع از ولایت، افراد و جریان‌هایی را وارد میدان می‌کند تا انسجام جامعه را هدف قرار دهند.
🔹
دشمن با استفاده از انواع رسانه‌ها و ابزارهای هنری وارد میدان شده و میلیاردها دلار برای این عرصه سرمایه‌گذاری کرده تا بر ذهن و ادراک جامعه اثر بگذارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/456540" target="_blank">📅 12:16 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456539">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85391bbbde.mp4?token=t2LvkrvODK44PwqShrSDQp8mhqsUirsaGTuLL6puEnb2ZstZJbDzKRjuRp_XAO2GxfuQjRU5YLbasyr5jbS1tEwvGslFwQVKjxqKMFXK9fV7mv586p-tr_7f6MdRehGggylObPpbaqgy1X0A83zGCe6bFNyWNEQOflrmA4BCVYTTAUH4OCvmHQIlYSI9nIfBkeLup3AqrdXaYu6gb3K_zgkbeDcsEz6iJ52slmUtwOY74wIiykq1QniycmM_qS1sIeY5GDxz3ffpic7KXoJZhU_QD2-L5GmkHy4Aw9VX_bwIS_q3erorGLriauyu3ZxLF8WQ3qJvbIUSMU1EWykhdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85391bbbde.mp4?token=t2LvkrvODK44PwqShrSDQp8mhqsUirsaGTuLL6puEnb2ZstZJbDzKRjuRp_XAO2GxfuQjRU5YLbasyr5jbS1tEwvGslFwQVKjxqKMFXK9fV7mv586p-tr_7f6MdRehGggylObPpbaqgy1X0A83zGCe6bFNyWNEQOflrmA4BCVYTTAUH4OCvmHQIlYSI9nIfBkeLup3AqrdXaYu6gb3K_zgkbeDcsEz6iJ52slmUtwOY74wIiykq1QniycmM_qS1sIeY5GDxz3ffpic7KXoJZhU_QD2-L5GmkHy4Aw9VX_bwIS_q3erorGLriauyu3ZxLF8WQ3qJvbIUSMU1EWykhdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه در واکنش به مخفی‌شدن ترامپ در کامیون غذا: این ترس همواره با جنایت‌کاران همراه خواهد بود و آرزوی مرگ آرام را به‌گور خواهند برد
🔹
ملت ایران مفتخر به این است که رهبرانشان از خطر نترسیدند و تا لحظهٔ آخر در محل‌های خدمتشان از عزت کشور دفاع کردند.
@Farsna</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/456539" target="_blank">📅 12:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456538">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb708e5299.mp4?token=awp-fgzFWfvc5YJNmE2ES9AvVCYYjAG7tTMigB2Ff0Gm223y9IpGBtM3LqO2kEIa4aIyWXMJVcxp4l6D4wXvxMyLPEUrbQMWBKM9psDkWNUqncA3Ko-o_BoaVuB7IAXHSghxfTAEGN9MHzcdhxf1ndOHUSKxXrpYxIAgf45_eLO28Kt90KDiqQHC1zm99PGW1iYLRUNkcUJ20yG7LgppK9sPCdymFbOJyudjEYjkAujRYHR9-XnXEtXAITDAr8_jDfwmGLuzKODneyda7zPqwpSLS0ex2OdTxm-y8xb4mW37I1xChd4UeL-mCPYupAMpRCUUHLykwCpjPVpO9D5RwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb708e5299.mp4?token=awp-fgzFWfvc5YJNmE2ES9AvVCYYjAG7tTMigB2Ff0Gm223y9IpGBtM3LqO2kEIa4aIyWXMJVcxp4l6D4wXvxMyLPEUrbQMWBKM9psDkWNUqncA3Ko-o_BoaVuB7IAXHSghxfTAEGN9MHzcdhxf1ndOHUSKxXrpYxIAgf45_eLO28Kt90KDiqQHC1zm99PGW1iYLRUNkcUJ20yG7LgppK9sPCdymFbOJyudjEYjkAujRYHR9-XnXEtXAITDAr8_jDfwmGLuzKODneyda7zPqwpSLS0ex2OdTxm-y8xb4mW37I1xChd4UeL-mCPYupAMpRCUUHLykwCpjPVpO9D5RwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖼
معاون وزیر خارجه: آلودگی نفتی سواحل قشم، ناشی از آثار تجاوز نظامی خارجی در منطقه است
🔹
این قبیل خسارات وارده بر محیط‌زیست سواحل ایرانی خلیج فارس، ضرورت تعریف و اعمال سازوکار مدیریت تنگه هرمز توسط ایران به‌عنوان کشور ساحلی را بیش‌ازپیش، برجسته می‌کند. @Farsna</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/456538" target="_blank">📅 12:02 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456536">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجار کنترل‌شده در جنوب اصفهان
🔹
سپاه اصفهان: احتمال شنیدن صدای انفجار کنترل‌شده در صفه، بهارستان و اطراف آن تا ساعت ۱۴ امروز وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/farsna/456536" target="_blank">📅 11:52 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456535">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JYA-q_WoILPjPc_UuIqaeCMT1OcV8nD-zNy2hhLJ6jTfUj41PrGoGFQRxEdN_JVQhWb6pRfPQwE6gZ7OzEoBcUokq1HhV_Z_N1WdnUl3Uxhs-tYwGZQKMLumZPZhOD3Rm6FF29aNfik__lIJRdjzPEWXYf0JXkr45YxJKeI3DRUjVzwsLebH8CQeKoJHGqHDZ02v4a7HjJmHCAYJSdJdjJ8lY-p4nV0ywbec1t2NCyD228uJyw_YZdpcJHn5TqlgH5rGPHNCmilYicetGci6me4TY4QKhsPHJVI-XI4tuNm667sh6V6i9gYwy3ButhyPQ91J9snwDVAO37dwfdyhbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بخش عمدهٔ آلودگی نفتی سواحل قشم مهار شد
🔹
معاون دریایی بنادر هرمزگان: تاکنون بخش عمده‌ای از آلودگی‌های نفتی سواحل قشم مهار شده و عملیات پایش، جمع‌آوری پس‌مانده‌های نفتی و پاکسازی منطقه تا رفع کامل آثار آلودگی ادامه دارد. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/farsna/456535" target="_blank">📅 11:50 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456534">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa912b817.mp4?token=a7bcNafRLX4ga2kNtK_1ouimReO-H0NncOOQJxf7MZ3JRFd4vfP5J5swbRub9XpBrSAQWwTKyrpoUM3Vabk3cpR3p5ZyTh73NwSmnByZU8XUh1AwyVo9ZuulBF5Ysr8HQdFqkyBdxBfl9FCm1KuTPdepNpUpyZyQat9WiI1ppHtcV7ovQ_5qXqmfOwy-9cntd1n949DdzDd_Y24VcY6wQa-wacF-D6taKEM7d8kmhaGfsCaAUE33qocyGftkiNHvgxGxjOr1w5JWue__GmSbRLGfIy2HEQ5XE7-pyTU8mGYInt0nEp8xAp4DI_U_OXHlLOUyOZn30B3PKWxR5r3Tdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa912b817.mp4?token=a7bcNafRLX4ga2kNtK_1ouimReO-H0NncOOQJxf7MZ3JRFd4vfP5J5swbRub9XpBrSAQWwTKyrpoUM3Vabk3cpR3p5ZyTh73NwSmnByZU8XUh1AwyVo9ZuulBF5Ysr8HQdFqkyBdxBfl9FCm1KuTPdepNpUpyZyQat9WiI1ppHtcV7ovQ_5qXqmfOwy-9cntd1n949DdzDd_Y24VcY6wQa-wacF-D6taKEM7d8kmhaGfsCaAUE33qocyGftkiNHvgxGxjOr1w5JWue__GmSbRLGfIy2HEQ5XE7-pyTU8mGYInt0nEp8xAp4DI_U_OXHlLOUyOZn30B3PKWxR5r3Tdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: در تفاهم پیش‌بینی شده بود که طی ۶۰ روز دربارهٔ رفع تحریم و موضوع هسته‌ای مذاکره شود، اما به‌دلیل نقض‌های فاحش و گسترده‌ای که آمریکا انجام داد، اصلاً مذاکره‌ای را شروع نکردیم.  @Farsna</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/farsna/456534" target="_blank">📅 11:44 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456533">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
اربیل مدعی حملهٔ پهپادی به دفتر مسرور بارزانی شد
🔹
تشکیلات «مبارزه با تروریسم کردستان عراق» مدعی شد که ۲ پهپاد انتحاری دفتر مسرور بارزانی، نخست‌وزیر کردستان عراق را هدف قرار داده‌اند.
🔹
طبق این اطلاعیه، ساختمان سازمان امنیت داخلی اقلیم کردستان نیز هدف این حملات قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/farsna/456533" target="_blank">📅 11:36 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456532">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rt4_flKzwjqdK-Bw288faerbppOpPm1jSlpGCZoQDqvOv7kw5GDPr6UaYnLxZWZYy4KoomYN5T_wUYzB8Bak0nX3ExTVoa-TMx9RH9R3ywBoCIQZoyshEyftFRMCrwFyKD7-Gw9NQKItR5ARFDIndfqeRS7xWrhpSiBBO7Xq0xkyMY8X-w1Tv5-poiJITNbpajMKlp-L9n8xwrOU6BAy35ySGr7NpSCsbKmrfCTleNM-cYN-N9tEYQ5BEOYw2h_jOKe8raARq3ukJpaV2JUJykylOJ1IxZsHz-6gb-1jYW_RaI6nh3Yr3mM_QFG-p6yeWSKbwcWyAsuZblclo5axWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
رئیس سازمان بهینه‌سازی: ۳ طرح پیشنهادی بنزین روی میز دولت است و هرکدام منتقدان و طرفدارانی دارد
🔹
هرکدام از این ۳ طرح تصویب شود، قطعا آن را پیش از اجرا اعلام می‌کنیم و مردم را غافلگیر نخواهیم کرد. @Farsna</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/farsna/456532" target="_blank">📅 11:35 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456531">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25766eff35.mp4?token=qvaslcvdbqSCyba0_czJ7PlmJ-ryxEl7nOZkKuEy7K-6fPrHT4W8v8AvANUBVXJMS454TFduyOubDg9u4SRvzkJVcu7ZmMP7kuOZNYOxHJHMKIc01M9SggtFjMxzAlGP__wBieMJG-A8tK_7aCe41vtJ42txjV7bydH2AFKclBSgTkiCnaRbwBewC12N0R_JvXTNtNxYF0xT6Qn4SJQHILQCbhLIynH0G2nvzKAS6iFefrHxMK6ito4uGc3Cw1w1K-kpRu-Bp2F8psBwalxs4_bEx9v8z16SCXQq8Xm-8FXphso7tBe7SVn-YvswCm80PkOeo9PBvhJ3csE1sOYJLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25766eff35.mp4?token=qvaslcvdbqSCyba0_czJ7PlmJ-ryxEl7nOZkKuEy7K-6fPrHT4W8v8AvANUBVXJMS454TFduyOubDg9u4SRvzkJVcu7ZmMP7kuOZNYOxHJHMKIc01M9SggtFjMxzAlGP__wBieMJG-A8tK_7aCe41vtJ42txjV7bydH2AFKclBSgTkiCnaRbwBewC12N0R_JvXTNtNxYF0xT6Qn4SJQHILQCbhLIynH0G2nvzKAS6iFefrHxMK6ito4uGc3Cw1w1K-kpRu-Bp2F8psBwalxs4_bEx9v8z16SCXQq8Xm-8FXphso7tBe7SVn-YvswCm80PkOeo9PBvhJ3csE1sOYJLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عراقچی: آتش‌بسی وجود ندارد که بخواهیم آن را تمدید کنیم
🔹
آنچه در پایان جنگ و در یادداشت تفاهم اسلام‌آباد اعلام شد «پایان جنگ» بود. آمریکا تفاهم را نقض کرد و درگیری‌ها مجدداً آغاز شده.
🔹
ما چیزی به‌عنوان آتش‌بس نداشتیم که حالا بخواهد تمدید شود؛ ما «پایان جنگ»…</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/farsna/456531" target="_blank">📅 11:28 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456530">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">‌ ثبت‌نام حج ۱۴۰۶ آغاز شد
🔹
سامانه «حج من» از ساعت ۱۰ صبح امروز برای متقاضیان سال ۱۴۰۵ فعال شد تا مراحل ثبت‌نام و معاینات پزشکی با دقت بیشتری انجام شود.
🔹
سایر متقاضیان نیز بر اساس جدول اولویت‌ها، وارد فرآیند خواهند شد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/456530" target="_blank">📅 11:18 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456529">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8301d537ed.mp4?token=vflG4Ae4yaXMM8Ex7kLWwqXnCZ1QFvI6SYk7FwXptXYaXP-1SJCTh2ZYe7UDsR20Lf2B6xP5WNSGrzBcvhqQjotz5-8fx5S501bQQ8ZJ7MfKILKJ9o9QUP4KYZk5nrHC2Zr8RLr9PsXPMc02opNw9sVkqxytMGMaHNT0BjhaC8iPAIi0D677TtwtPWtMkDh2VKXL3E4z8WT2dNW7JfmoSVTqWZlua-3yfeLwSVpE_XCsYfoiFx7adSOXzipmrEbmLtSCZ2EwtCYV7p5Tw5IGkO2qcV3hHeq2LMmALqrFhpUDLAuaksw06iJh9ZLLnUurG0fvUz7N8y-OElMSn2sUBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8301d537ed.mp4?token=vflG4Ae4yaXMM8Ex7kLWwqXnCZ1QFvI6SYk7FwXptXYaXP-1SJCTh2ZYe7UDsR20Lf2B6xP5WNSGrzBcvhqQjotz5-8fx5S501bQQ8ZJ7MfKILKJ9o9QUP4KYZk5nrHC2Zr8RLr9PsXPMc02opNw9sVkqxytMGMaHNT0BjhaC8iPAIi0D677TtwtPWtMkDh2VKXL3E4z8WT2dNW7JfmoSVTqWZlua-3yfeLwSVpE_XCsYfoiFx7adSOXzipmrEbmLtSCZ2EwtCYV7p5Tw5IGkO2qcV3hHeq2LMmALqrFhpUDLAuaksw06iJh9ZLLnUurG0fvUz7N8y-OElMSn2sUBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: از زمان شروع جنگ ۴۰ روزه از ذخایر کالاهای اساسی استفاده نکرده‌ایم؛ نه‌تنها چیزی از آن کم نشده بلکه درحال اضافه‌شدن است.
🔹
محاصرهٔ ایران چیز جدیدی نیست؛ ایران به مسیرهای زمینی و دریایی متعددی دسترسی دارد و چرخ امنیت غذایی کشور همواره در حرکت…</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/farsna/456529" target="_blank">📅 11:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456528">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=v4VLU3bqkQMWKPZLJgwr74GOxkEu6cbYNu3k4phTnUD5sIYh7LEldiGmQCnY-CBHQBmXfEXFNsenW2eFMW94dkOyYXL8-JLeNKYR0YkqIfJQzKTd84zWzyMIYP2Uz9VCIpELaQykYrPsLiezoZUyVaRDtyreNvti4AUXgntcrsyoXn_SOO99mIxCHSEerxTJqO5OW2aMp6qofDqgBcUhJ-BgEKHAZlCRZuwHsX5ZO_seq-Mg3bxRm4vN6tBwsQeZvwLYX7hNUNZiI1zOtYMotBN5mtvtZ50iU_kRpAOBuZYm4uR1VuU5STbQJEtK5OKNtDqlP1x062jHbohWUoYQFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/944a019ec7.mp4?token=v4VLU3bqkQMWKPZLJgwr74GOxkEu6cbYNu3k4phTnUD5sIYh7LEldiGmQCnY-CBHQBmXfEXFNsenW2eFMW94dkOyYXL8-JLeNKYR0YkqIfJQzKTd84zWzyMIYP2Uz9VCIpELaQykYrPsLiezoZUyVaRDtyreNvti4AUXgntcrsyoXn_SOO99mIxCHSEerxTJqO5OW2aMp6qofDqgBcUhJ-BgEKHAZlCRZuwHsX5ZO_seq-Mg3bxRm4vN6tBwsQeZvwLYX7hNUNZiI1zOtYMotBN5mtvtZ50iU_kRpAOBuZYm4uR1VuU5STbQJEtK5OKNtDqlP1x062jHbohWUoYQFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ باقرزاده: قطر به جای تکذیب اسارت خلبانان ایرانی، دفع وقت نکند
🔹
فرمانده کمیتۀ جست‌وجوی مفقودین ستادکل نیروهای مسلح: تیمی متشکل از کارشناسان زبده نیروی هوایی کشورمان چندین ماه است که در انتظار ورود به قطر و بررسی میدانی هستند.
🔹
با کارشکنی‌های پیاپی و دفع‌الوقت…</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/farsna/456528" target="_blank">📅 11:06 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456527">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507dba98f8.mp4?token=krpLcEzmgj8YjmzdFoqFDKCsuLoZhhlw-sjOKw-n7-wYN19aXX5ipog6HdNiixB-0UFg63_dEzYFnoyzplz5YBszCShfSdVSn0GItg22A5BDBgIsjNxCXzuZkE6EpHPN7vK--dWBqjndUjwYnq4OzekSaBdkjgW1iSto_Q00F7vA7eVdeoZR_tGyYQYqdnIq30Wdw0Nk2_0g5iD0iXiYwiwqMvyyTxs4tjpXjkfbU8XOUOCTVQZKrJGG9HPjzIz2hiYUnGsWFUylW4M8AZvFBc_DbprsA4UstzZLkF-74nA5hCKO4-zhqj49bt5b4il5N6EKc9Qp0MmC9yOe_-y9Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507dba98f8.mp4?token=krpLcEzmgj8YjmzdFoqFDKCsuLoZhhlw-sjOKw-n7-wYN19aXX5ipog6HdNiixB-0UFg63_dEzYFnoyzplz5YBszCShfSdVSn0GItg22A5BDBgIsjNxCXzuZkE6EpHPN7vK--dWBqjndUjwYnq4OzekSaBdkjgW1iSto_Q00F7vA7eVdeoZR_tGyYQYqdnIq30Wdw0Nk2_0g5iD0iXiYwiwqMvyyTxs4tjpXjkfbU8XOUOCTVQZKrJGG9HPjzIz2hiYUnGsWFUylW4M8AZvFBc_DbprsA4UstzZLkF-74nA5hCKO4-zhqj49bt5b4il5N6EKc9Qp0MmC9yOe_-y9Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: قیمت اغلب کالاهای اساسی و مواد غذایی نسبت به هفتهٔ گذشته و نسبت به ماه گذشته رو به پایین است.
🔹
مرغ سال گذشته ۱۴۰ هزار تومان بود الان بیش از ۳۷۰ هزار تومان است که دلایل خود را دارد.
🔹
جنگ روی افزایش قیمت‌ها تاثیر گذاشته و قیمت‌های جهانی ۱۰…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/456527" target="_blank">📅 11:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456526">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueogWeBDy0_aauLxGxHm67ZTdqEmZqitk2R4EvXoeHWu_ydun48FEyXYWrHCb7k2P14nIy1v5BZ8aiOhWt3H7eBrPNbtq0jkK092MRpSJr0gHYatE09ComdZAYJWC5Zbz_Bu-vzlxBz3h8HAlSNFO0CnVwEEzSNfCnLmZoYFLLl2tLzrWSpIWNRrRJ7wMGX4Ax3QB4wFDAMr9eyq0ke3AAJe007AzuhmBHLHkgY6SqJu5cqbIZvxxKkaGlHpYcMZE0ivsrFYaqlVWyccQmGUzJp2yE5whITl9uUtuoYZGXjSm_PpaGkWLam80G8T2LNn7SkSWqMj9T_aeYsjFcRMIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسته بودن تنگه هرمز،‌ بازگشت به مدرسه را برای آمریکایی‌ها گران کرد
🔹
همزمان با آغاز فصل بازگشت به مدرسه در آمریکا، افزایش هزینه‌های زندگی بار مالی سنگین‌تری بر دوش خانواده‌ها گذاشته است. تعرفه‌های تجاری دولت دونالد ترامپ و پیامدهای جنگ با ایران به افزایش قیمت کالاهای مورد نیاز دانش‌آموزان و سایر هزینه‌های خانوار دامن زده‌اند.
🔹
والدین آمریکایی در گفت‌وگو با ام اس نَو از افزایش شدید قیمت کالاهایی مانند کوله‌پشتی، دفتر، جعبه غذا و لوازم الکترونیکی ابراز نگرانی کرده‌اند. یکی از مادران مجرد چهار فرزند در ویرجینیای غربی گفته است حتی یک کوله‌پشتی ساده ۳۵ دلاری نیز برای او گران تمام می‌شود.
🔹
این فشار اقتصادی به هزینه‌های مدرسه محدود نمی‌شود. تغییرات ایجادشده در برنامه‌های کمک غذایی و درمانی در پی تصویب طرح موسوم به «لایحه بزرگ و زیبای ترامپ» نیز دسترسی برخی خانواده‌های کم‌درآمد به کمک‌های غذایی و پوشش درمانی را دشوارتر کرده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/456526" target="_blank">📅 10:55 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456525">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd2fd5eddd.mp4?token=v5q75H3G0QllwBp7sPO6_7fEHFD7BxghyGf1-3HPN7E7kHPXcnZBE-3QZtrq_4jc2h-GJkEaYmMzZtmlGx0JUwSVD3iDvVUvo9W_EGcHpmdznrmHdhCRITB4o9KMLMoieWbDLTPmIEvp6CBVVWsLTeqXUA-8m82V7U0xG7knN6REV8sgu2of88YQx82rrTIm4E1ZWZCOX3kUwddy8e6duZRbe5QKQ7KDPe5PpsYnA3vmAklVj1IjoVw-B2sGT1kO7Xs5rw9uQNejzbjga40lWN-2O43-paJNUWEroSKiaqKGIwtmjEw_CQrWh48CKUMVq1yF1dPCDIIK2g2YMruPUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd2fd5eddd.mp4?token=v5q75H3G0QllwBp7sPO6_7fEHFD7BxghyGf1-3HPN7E7kHPXcnZBE-3QZtrq_4jc2h-GJkEaYmMzZtmlGx0JUwSVD3iDvVUvo9W_EGcHpmdznrmHdhCRITB4o9KMLMoieWbDLTPmIEvp6CBVVWsLTeqXUA-8m82V7U0xG7knN6REV8sgu2of88YQx82rrTIm4E1ZWZCOX3kUwddy8e6duZRbe5QKQ7KDPe5PpsYnA3vmAklVj1IjoVw-B2sGT1kO7Xs5rw9uQNejzbjga40lWN-2O43-paJNUWEroSKiaqKGIwtmjEw_CQrWh48CKUMVq1yF1dPCDIIK2g2YMruPUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکید رئیس‌کل بانک مرکزی بر پیگیری مسائل صادرکنندگان و پیمانکاران ایرانی در عراق
🔹
رئیس‌کل بانک مرکزی در دیدار با تجار، صادرکنندگان و پیمانکاران ایرانی در سفارت ایران در بغداد، مسائل و موانع فعالیت اقتصادی در بازار عراق را بررسی کرد.
🔹
موانع بازگشت ارز صادراتی،…</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/farsna/456525" target="_blank">📅 10:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456524">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=GesQIlHpP5OohsIzBP0lKRhMYzfWboMobIWd1mdszXt0pq-1mfaXSJix9ouG9ngS8DtZ_LeevS2maEs5thMk-Ft68gJY2p0s7zRfsNiFJFMqSkFaE6e6jh4r2bOtr6-uw0PPQ0wT8qrqo0wCTAaXvvtTQDuipx0kOyQWPzAXIMRlKicVCKaQcaG77J_m5_m1t5v_GapScgTV4WfXHtFJeSE7zmyhwsRYPkLrnGQ_rXdgSbmyGpSCdzgrxvO8ciY-8loPIjbzYR7iXR8JsT2mi6ejfYE3HYBxJHT0h7Wr0aZSiEuVioo0nAePAwIUIaYO_gEWGGmYNrK_hB4SIs0SzTKy1aUbhSrzHCuel15TwuHu6pdTybTdrhK10xQ6yT15ubfNbWpL2jmJKCXO0rrYOHX-NLJ5BsUc1qCb1mdN_u0bD3SjHYcSdXadL_ZJrTRShyZm_0_BZeiHAPSqVk9nhKqvzuUhXvqrOLAYvqbpdsQSenKamTe_mR55CqztMj8Kqvd_SgCs0kMLzv19dOqV-CCPXVr4h6eM56kINHNyD0iJQ0CpKpyL7i5JQkOpTb_24UokgN8KS46vE4Azwnaz8nV4bSd-ifIHzyNq3_lP354VD5xbBdFIp_cenjbuKCjL9WOrTImDDgSkH31VyuNbv0g2bxfvozlJ3IGOYimlBLE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8251e814b0.mp4?token=GesQIlHpP5OohsIzBP0lKRhMYzfWboMobIWd1mdszXt0pq-1mfaXSJix9ouG9ngS8DtZ_LeevS2maEs5thMk-Ft68gJY2p0s7zRfsNiFJFMqSkFaE6e6jh4r2bOtr6-uw0PPQ0wT8qrqo0wCTAaXvvtTQDuipx0kOyQWPzAXIMRlKicVCKaQcaG77J_m5_m1t5v_GapScgTV4WfXHtFJeSE7zmyhwsRYPkLrnGQ_rXdgSbmyGpSCdzgrxvO8ciY-8loPIjbzYR7iXR8JsT2mi6ejfYE3HYBxJHT0h7Wr0aZSiEuVioo0nAePAwIUIaYO_gEWGGmYNrK_hB4SIs0SzTKy1aUbhSrzHCuel15TwuHu6pdTybTdrhK10xQ6yT15ubfNbWpL2jmJKCXO0rrYOHX-NLJ5BsUc1qCb1mdN_u0bD3SjHYcSdXadL_ZJrTRShyZm_0_BZeiHAPSqVk9nhKqvzuUhXvqrOLAYvqbpdsQSenKamTe_mR55CqztMj8Kqvd_SgCs0kMLzv19dOqV-CCPXVr4h6eM56kINHNyD0iJQ0CpKpyL7i5JQkOpTb_24UokgN8KS46vE4Azwnaz8nV4bSd-ifIHzyNq3_lP354VD5xbBdFIp_cenjbuKCjL9WOrTImDDgSkH31VyuNbv0g2bxfvozlJ3IGOYimlBLE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر کشاورزی: با اصلاحاتی که در سیاست ارز ترجیحی انجام شد، تولید دانه‌های روغنی با سرعت بیشتری ادامه خواهد داشت.   @Farsna</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/farsna/456524" target="_blank">📅 10:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456523">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYOjrxBWymvAjJPA7416dz3dLrK4GHEREofrSomaJaHfDLf_b_StHLC8YRo8_Rrldxn3KYKE75VGYLdsnU286r4JHhSPjWlABRTu960fCkDE-yvuo_dJ36YYIv-nk4IzegqL7dJbjzskF6cNDHSzZsTrNLPM5HWwepniHxaAN0wBDdyijoFGIYG2uYYyQYg1mQDjFuihpShDSTB9-9U1XMe3lqFWqIHr65nO-tV054w_5kIRSgTtCgPJNatR20qq3skFyB1Lq8N9nbmPiOQqPrwVPruo7oMFnkzWZytlrJTi4rJRhAd6b5oKfsYxlzYT5rnDD7r8dcyB470wnWI0UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکن مهر در دستور کار پیگیری دیوان محاسبات
🔹
دیوان محاسبات: قصور در تکمیل و تحویل حداقل ۸۰ هزار واحد باقی‌ماندۀ مسکن مهر در سنوات گذشته، علی‌رغم ایفای تعهدات مالی متقاضیان، درحال رسیدگی است و فرآیند مستندسازی پرونده مسئولان وقت در حال انجام است.
🔹
در تعامل با وزارت شهرسازی مقرر شد مبلغ ۲۰ هزار میلیارد تومان در سال جاری برای تکمیل و تحویل واحدهای باقی‌مانده اختصاص یابد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/farsna/456523" target="_blank">📅 10:41 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456522">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5fa181a7b.mp4?token=gSdIHvxbchMDSkumbI0CsCWx6aEu4vjDtz3TlhrxaQWcQcATVRN7T68b3Wr2U_C-RJJhFkeiqhijeq0wl32eXCeUEH8Mk45WPyhjdrYGS0lZpcD8RjrSuPFONxDyvLsLLPS4U0Fs9xUHY0TOdgorSLO_gZZBjDjkJWx7ukwBfrJhPtMxXCca0U_tHYRUFgGcfEZUB35q2-gFjPFN3FFQoVI8h0ylFto9M7UWhmbfAUgBIXXGZskuTugjttRAIrHZTHH8uo89hqcV-WNRqTgjm_QzLlGCkbhFmPNrUANUIZoPUqmOoQD3AuwVDfoeFv6OrukQ6ag74Eqf1klHMGjLCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5fa181a7b.mp4?token=gSdIHvxbchMDSkumbI0CsCWx6aEu4vjDtz3TlhrxaQWcQcATVRN7T68b3Wr2U_C-RJJhFkeiqhijeq0wl32eXCeUEH8Mk45WPyhjdrYGS0lZpcD8RjrSuPFONxDyvLsLLPS4U0Fs9xUHY0TOdgorSLO_gZZBjDjkJWx7ukwBfrJhPtMxXCca0U_tHYRUFgGcfEZUB35q2-gFjPFN3FFQoVI8h0ylFto9M7UWhmbfAUgBIXXGZskuTugjttRAIrHZTHH8uo89hqcV-WNRqTgjm_QzLlGCkbhFmPNrUANUIZoPUqmOoQD3AuwVDfoeFv6OrukQ6ag74Eqf1klHMGjLCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهاد کشاورزی: قیمت در بازارهایی مثل قند، شکر، آرد و روغن مشکلی ندارد؛ حتی چند درصد پایین‌تر از قیمت تعادلی مشخص‌شده در سازمان حمایت از مصرف‌کننده و تولیدکننده است.  @Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/456522" target="_blank">📅 10:30 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456521">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc7bea42f.mp4?token=NAhjxLjKWksLOunphYS-lZKLfHSudLxDoefYsanSifkhOF_w1jBjrAH-aPwLQpS_2YjGvU-rzNzJx-uKDzs-BHBcwehibTFL8NDJmryrZZMb5VpCSAm_hb1bRK1T3CNQ_v0ZEVT3WPm92tn3W09lUvDvhe-3_EuXhz-ngBnJLd3OZc6KyfOXKKxSN_vlAg0t4sUOpxJXacGAfab29G0Ese7zqx5_2-Jb0v9s1nz1CnI4E2cUZBzUK_lX79gxIwhuW6FZy8I3qr67uwlR8rkb7U97A3a3D9cughVNO8NqEj4L41mOCmyGv08ZFc-xJ32D5thgUTnJgYffuBZ4OncPag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc7bea42f.mp4?token=NAhjxLjKWksLOunphYS-lZKLfHSudLxDoefYsanSifkhOF_w1jBjrAH-aPwLQpS_2YjGvU-rzNzJx-uKDzs-BHBcwehibTFL8NDJmryrZZMb5VpCSAm_hb1bRK1T3CNQ_v0ZEVT3WPm92tn3W09lUvDvhe-3_EuXhz-ngBnJLd3OZc6KyfOXKKxSN_vlAg0t4sUOpxJXacGAfab29G0Ese7zqx5_2-Jb0v9s1nz1CnI4E2cUZBzUK_lX79gxIwhuW6FZy8I3qr67uwlR8rkb7U97A3a3D9cughVNO8NqEj4L41mOCmyGv08ZFc-xJ32D5thgUTnJgYffuBZ4OncPag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر جهادکشاورزی: ۸.۲ میلیون تن گندم از کشاورزان خریداری شده و امسال وضعیت تولید خوب است.
🔹
همچنین از مجموع ۴۰۰ همت طلب گندمکاران، ۲۱۸.۵ همت پرداخت شده است. @Farsna</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/farsna/456521" target="_blank">📅 10:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456520">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/953c8a4026.mp4?token=ATebPtYMbHGuPTz30IXONQDGF-yvetCdPiJTpyep3QcfXWgudwTzjE83WYvnhPmjGk4K3qu4GlDGWsQyb0IjcU0dw9d1Jmo3xGIxRoy54Dr3RnAy8mH8z_4NuV-qe3jAZyqpw6y1B4xUatZQzi_BDbPEWQWZpXxx-jwK057r-YT74oVL4ccPw7wvJem0qAI9Z5vIBab8Aveui0yLgEpmNm5hdRCi5MoAco5e2RopK9iFpEmbzNupD66XrENvWaP1gUOTwKFPU9-I35BPRJpNNmf7M34ZddGtn9s2BISH9KiA4Rxx4Mmz68KYU0v41tQfX6JDooCWFiTgcy5dz7ORCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/953c8a4026.mp4?token=ATebPtYMbHGuPTz30IXONQDGF-yvetCdPiJTpyep3QcfXWgudwTzjE83WYvnhPmjGk4K3qu4GlDGWsQyb0IjcU0dw9d1Jmo3xGIxRoy54Dr3RnAy8mH8z_4NuV-qe3jAZyqpw6y1B4xUatZQzi_BDbPEWQWZpXxx-jwK057r-YT74oVL4ccPw7wvJem0qAI9Z5vIBab8Aveui0yLgEpmNm5hdRCi5MoAco5e2RopK9iFpEmbzNupD66XrENvWaP1gUOTwKFPU9-I35BPRJpNNmf7M34ZddGtn9s2BISH9KiA4Rxx4Mmz68KYU0v41tQfX6JDooCWFiTgcy5dz7ORCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌
🔴
سرپرست دادسرای جنایی تهران: ۹ عامل اصلی مرتبط با قتل حمیدرضا رجب‌زاده دستگیر شدند.  @Farsna</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/farsna/456520" target="_blank">📅 10:14 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456519">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/416e249c60.mp4?token=L7O1imtG0KtS5COs0kwIc8K9UvnLuUNwuC6iRMIEW7dQ4xh1Et70aJzj9CW9Ukh1pUuUpGyOIYPv2NVnbMrEqjo2QED2RNWLJ4QF469DhsytbwcWqS_RU0-2SMAAaxBQ3Dz6TrpuF3T2cwiOigmnKckmXNNrpPJRxhNlb08sJYHeTwTvTHN-0KstlNJKqtJbM7E6A_MBnxEtb_3l0oXHIRyn2VQcsrKReDgEKHOUVGOFftpDFTT0bgXCcVldg_PvzKPqPf5nZlYXtZrV3fYxNtfsH1sxLtx8_n4DTkvU7hhi6xbwAd3UEnuMasoaO2U5p4YHsv_zRqz6wQ3B_-jvGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/416e249c60.mp4?token=L7O1imtG0KtS5COs0kwIc8K9UvnLuUNwuC6iRMIEW7dQ4xh1Et70aJzj9CW9Ukh1pUuUpGyOIYPv2NVnbMrEqjo2QED2RNWLJ4QF469DhsytbwcWqS_RU0-2SMAAaxBQ3Dz6TrpuF3T2cwiOigmnKckmXNNrpPJRxhNlb08sJYHeTwTvTHN-0KstlNJKqtJbM7E6A_MBnxEtb_3l0oXHIRyn2VQcsrKReDgEKHOUVGOFftpDFTT0bgXCcVldg_PvzKPqPf5nZlYXtZrV3fYxNtfsH1sxLtx8_n4DTkvU7hhi6xbwAd3UEnuMasoaO2U5p4YHsv_zRqz6wQ3B_-jvGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات وزیر جهادکشاورزی دربارهٔ تخلف ۴۵ هزار میلیارد تومانی نهادهٔ دامی: چنین اعداد و ارقامی سوءتفاهم است و برای دولت چهاردهم نیست.  @Farsna</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/farsna/456519" target="_blank">📅 10:08 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456518">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ab49e9f1e.mp4?token=QkMDCxzLT-0N7eCQgMEf6TZD_NRkT-ev7Hdty-Tu_EgUxEFeZRkQIOfG8V35dAWMbqIaFKU2xjGqWIqajbq2RuYbpOf45UWPwEA5AxUKxxHXe6yi0N9hE5mYidlVcFKSsVENl4E5GrJvf1yXyRDcAc6wCXVv_F02MtGCLeBfUtBCbjy4582qogEE33atv12MA_kCoCFCztPUjmpRg0aUlNlJGU1dmzDQeqYYFCv95eQ2jm8gpCiWY2CGvJpuguR57cMNhYB1poXKO8rFGzjwR0FoNmE505QLYUQ1bK2FSk8Uq10ju0LS2grgSsi3dWMdh7PHuBs6kHwLFWdv5Y2BXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ab49e9f1e.mp4?token=QkMDCxzLT-0N7eCQgMEf6TZD_NRkT-ev7Hdty-Tu_EgUxEFeZRkQIOfG8V35dAWMbqIaFKU2xjGqWIqajbq2RuYbpOf45UWPwEA5AxUKxxHXe6yi0N9hE5mYidlVcFKSsVENl4E5GrJvf1yXyRDcAc6wCXVv_F02MtGCLeBfUtBCbjy4582qogEE33atv12MA_kCoCFCztPUjmpRg0aUlNlJGU1dmzDQeqYYFCv95eQ2jm8gpCiWY2CGvJpuguR57cMNhYB1poXKO8rFGzjwR0FoNmE505QLYUQ1bK2FSk8Uq10ju0LS2grgSsi3dWMdh7PHuBs6kHwLFWdv5Y2BXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توضیحات وزیر جهادکشاورزی دربارهٔ تخلف ۴۵ هزار میلیارد تومانی نهادهٔ دامی: چنین اعداد و ارقامی سوءتفاهم است و برای دولت چهاردهم نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/farsna/456518" target="_blank">📅 10:05 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456517">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN9V3x8jvFq36nF9mO86tIaUo11PtRLAVlCjhQospTgel8ohf73Jr8U9cFbJZ89ikspOdezml_wY6YkqbZmfjNcXSAjP-aBKTDCKstWh01kvo6Uy2Ar09Ipf6-k_xlqLBmTpBIwNmhlQ7F8ybCvgd1wT0a8PJkV2GBYX2MC8gue2kpEMzyylPBCofGSoIzZtnc--WlSc-6XtYCmoidTcGevtSHp-0327-sR3V6zW1pooDJEjGCEzn8TE5ydoNxsGfQy3nYrZfrQRU8pM1C1DhwmMMsTyyHA0fGDC2V0Zn-dXogEaeYNrTeqReSaCjTa1bpHmJnNe4WXIBFTtBbXt6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات برای نجات بنادرش دست‌به‌دامن خزانهٔ دولت شد
🔹
صندوق ثروت دولتی ابوظبی «لیماد» قصد دارد با پرداخت ۸.۶۶ میلیارد دلار، سهام سهامداران خرد گروه بنادر ابوظبی را بازخرید و مالکیت این شرکت راهبردی را کامل کند.
🔹
این اقدام در شرایطی انجام می‌شود که بنادر امارات به دلیل بحران تنگهٔ هرمز و کاهش شدید فعالیت‌های تجاری با چالش جدی مواجه شده‌اند.
🔹
براساس گزارش ارائه‌شده، فعالیت بندر جبل‌علی تا ۹۰ درصد کاهش یافته و حجم جابه‌جایی کانتینر در بنادر گروه بنادر ابوظبی نیز ۶۵ درصد افت کرده است.
🔹
امارات برای جبران این وضعیت به بنادر شرقی مانند فجیره و خورفکان روی آورده، اما ظرفیت محدود این بنادر فشار زیادی بر زیرساخت‌های حمل‌ونقل وارد کرده است.
🔹
این شرایط، همراه با هزینهٔ سنگین بازخرید سهام، نشانه‌ای از تلاش ابوظبی برای حفظ کنترل بر زیرساخت‌های حیاتی و مدیریت پیامدهای بحران تجارت دریایی عنوان شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/456517" target="_blank">📅 09:48 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456515">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2592cfef.mp4?token=k_ol12mMzVEpkUUkUo8QfuEZYbJ8-TBe1zZI4s2_-4gRWxILlLwEONY3hfzEROLKVxyX5AUGbl25VCb2VrFLDbX-p5qk40IEiKJMOn26uI4AuZHTaqKatUx2J7sHzrGzxcmdSzCVsOeH-BqclEDNu9BpV8QxLiDWfacucadea989j8ujs8Gk6gAt-M1NtTIlnO6dOk_gyr2hgiLJP6Ghy4pgC6P96pjqL8fFIYeJDhB7_PAFtiQBlNKVyrc0BUKd0iJHIKJtJckYNdx_yTNDzkOfYqWSYv4Yj-T8VU8EnzWZK1Zog2IlIdQk58WxpwswaHpzDa5AONMvSrC7b96Wmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2592cfef.mp4?token=k_ol12mMzVEpkUUkUo8QfuEZYbJ8-TBe1zZI4s2_-4gRWxILlLwEONY3hfzEROLKVxyX5AUGbl25VCb2VrFLDbX-p5qk40IEiKJMOn26uI4AuZHTaqKatUx2J7sHzrGzxcmdSzCVsOeH-BqclEDNu9BpV8QxLiDWfacucadea989j8ujs8Gk6gAt-M1NtTIlnO6dOk_gyr2hgiLJP6Ghy4pgC6P96pjqL8fFIYeJDhB7_PAFtiQBlNKVyrc0BUKd0iJHIKJtJckYNdx_yTNDzkOfYqWSYv4Yj-T8VU8EnzWZK1Zog2IlIdQk58WxpwswaHpzDa5AONMvSrC7b96Wmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شمال کشور امروز بارانی‌ است
🔹
هواشناسی: امروز در شمال آذربایجان‌غربی و شرقی، اردبیل، گیلان، مازندران و گلستان و ارتفاعات البرز رگبار، رعدوبرق و گاهی وزش باد شدید موقت پیش‌بینی می‌شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456515" target="_blank">📅 08:45 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیش‌فروش بلیت‌ قطارهای مسافری برای بازۀ شهریورماه آغاز شد.
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/456514" target="_blank">📅 08:34 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">آغاز توزیع کارت کنکور ۱۴۰۵
🔹
داوطلبان کنکور تا چهارشنبه ۲۸ مرداد فرصت دارند کارت آزمون خود را از سایت سازمان سنجش دریافت کنند.
🔹
آزمون تجربی صبح، هنر و زبان‌های خارجی بعدازظهر پنجشنبه ۲۹ مرداد، ریاضی، فنی و انسانی صبح جمعه ۳۰ مرداد برگزار خواهد شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/456513" target="_blank">📅 08:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456512">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAMAenRJR-71Rp5YtBz4EekmYcUyS6Vx5COChhk-XUWjntjMGrsl7HojXl-L-jt9xzskRVodxe37gJSPNzNAQLQU_SUtRXCBqPxoDINGCXA3mGzsGIxE9gCkc6F42lTaQtxlsZPyyasQfFu143dOB7PHJldmWDG9vVDFNk3WD3WQe5-jxTyqnt4uKWU0t8UL3vTCWQ9fAYB3LKg8bksJhfy9Z0W9DY3UvrKuI_irn5zzinUJfZ288prgalmCuYHA4CcX8rmSzorE5Jdyfj2Y_EPXMbVqFYwEaTJmOd1yuEYpMHClQ9q-UaTniSXFlgYZ1eFnbv2VAenAYM7dqfLWPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تویوتا در تنگۀ هرمز روغن کم آورد!
🔹
جنگ در منطقه و بسته شدن تنگۀ هرمز، زنجیرۀ تأمین روغن موتور خودروسازی‌های بزرگ دنیا از فولکس واگن تا تویوتا را به بن‌بست کشاند و قیمت روغن‌های پایه را در بازارهای جهانی سه برابر کرد.
🔹
بر اساس گزارش فایننشال تایمز، کمبود شدید روغن‌های پایه با کیفیت بالا که مادۀ اولیه تولید روغن موتورهای مدرن هستند، شرکت‌های بزرگی چون فولکس واگن،  استلانتیس و تویوتا را ناچار به جست‌وجوی ترکیبات جایگزین و تأمین‌کنندگان جدید کرده است.
🔹
منابع اصلی این روغن‌ها در غرب آسیا قرار دارند و اختلال در مسیرهای حمل‌ونقل دریایی و کاهش فعالیت پالایشگاه‌های منطقه، عرضه را به شدت محدود کرده است.
🔹
خودروسازان در ماه‌های ابتدایی از ذخایر خود استفاده کردند، اما با تداوم ناآرامی‌ها، این ذخایر رو به اتمام است و بازارهای آمریکا و اروپا که بیشترین وابستگی را به واردات از این منطقه دارند، با شوک جدی روبه‌رو شده‌اند.
🔗
شرح کامل گزارش را
اینجا
بخوانید.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/456512" target="_blank">📅 07:53 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456511">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhIPmamgMTPGS2x5vrKAOCQFvwYBC74v5fqmp36s-WjC564iwR-CurVfq20qyBYYM4r2QZ70YdcfHAk20mWH9nuZXhdByRMzMbyCyJcWSYuA-wMDTGXQpvKxZvZpYiEAAFungDWUNMAdyxmC9irEhp1DtAqLt_XNuEj47T7EugKi71LyRAU2jG9WrDGgdDxYUy4m2SdOE0yrsElkTpVRjvuz2Zwo_ua13mcqmeUXQ9G0jIC7_0xlxCB4UDPuoQ0TA-nzqznehYFNHPeHdbMZtSFKOQoQx_r4fa0f9YAQKyMBhYKrWOLjUYJpZ_6ceKR54RWKPMo1qn16ZTcdhgV-8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
معاون بین‌الملل وزارت خارجه: وزیر امنیت ملی رژیم صهیونیستی برای کشتار در غزه «سهمیۀ شبانه» تعیین کرده است؛ ۳۰ تا ۴۰ نفر.
🔹
این جنایتکار صهیونیست هم‌زمان از اخراج فلسطینیان و شهرک‌سازی در سراسر غزه صحبت می‌کند.
🔹
این اعترافات باید برای روز حساب و محاکمۀ این جنایتکاران ثبت و حفظ شود.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/456511" target="_blank">📅 07:22 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-456510">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7xyDzdu304Dyevdeq9am670-Fjq-Si087jWhPIn-5xgwfHSy-17GwOYVjKeau3Suk12qYSValnB33cuZ4orsIRO-XGfICi04fdzlETqYuT8LHA_SKGZFcZCJxbnp5Cv-kmRh7ia0ZZ_zfhpmx9n2JDQKzDHp64zcbm9Hl61eFm5qkRfgHf9220Xq7ivtxssgNgUrWVKGvne1KodBRvhpue_WguUqzp7Gdg15hCGoaqNyw7wGPX_9ZmwzwdrTvtfe9ST68ZiDtCuxE2S_vljbBRED3rWhXuuEa2tc-j1oQG4_dBVoe4NGO-wxlII5CJl4nhWbtcLVnL623fl4wpnLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز رکورد دست قدیمی‌ها است
🔹
بررسی فهرست پربیننده‌ترین تولیدات رسانه‌ای در تیرماه ۱۴۰۵(مرکز متا)، یک نکتۀ قابل تأمل دربارۀ وضعیت مخاطب تلویزیون نشان می‌دهد.
🔹
از میان پنج اثری که در صدر جدول مخاطبان قرار گرفته‌اند، چهار اثر متعلق به دهۀ ۹۰ و سال‌های پیش از آن هستند و تنها نمایندۀ تولیدات دهه ۱۴۰۰، سریال «تانک‌خورها» است؛ سریال گیل‌دخت هم  اواخر دهۀ ۹۰ تا ابتدای سال ۱۴۰۰ تولید، و سال ۱۴۰۱ پخش شد.
🔹
بر اساس این آمار، «دلدادگان» با ۲۸.۵ درصد در رتبۀ نخست قرار گرفته و پس از آن «گیل‌دخت» با ۲۶ درصد، «مختارنامه» با ۲۵ درصد و «زمانه» با ۲۲ درصد ایستاده‌اند. «تانک‌خورها» نیز با ۱۴ درصد در رتبۀ پنجم قرار دارد.
🔸
آرشیو تلویزیون همچنان یکی از مهم‌ترین منابع جذب مخاطب است و آثار قدیمی در بسیاری از موارد توان رقابت جدی با تولیدات جدید را دارند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/456510" target="_blank">📅 06:53 · 26 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
