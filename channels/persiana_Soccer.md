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
<img src="https://cdn4.telesco.pe/file/q9EIGojXLT9w_yuw8Z0tEd2Be5zZ-5HPVIRK3qw0QwN5E-3Gc2k_9SjktQQQa1ZaJGoHe5iHzMeyMuv_f9IcNCLdwaiRTH-7Mnk5gpQXIjsDvw9965zEqlv_VRKUyhp_YBwP-FfeFOi6xSo-TSMSl7W0vCpFPPGHHTq4A38jwL7q7w0zEGuNvKm9uN-jlbiK3dUtYhi-u9MN82zNJZ5T3xIYp6N-goh8Rd9YgCysC8z4PkpmfCF9rnmUUP9mEx1H1JKYdmoc7ySIUKhn9Z4rG1sgPSnDXN2yNytohB7jFFNivM0NGgZIKJhhEjh58T30pT3N6UWLTSkSOxk1q0rnKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 476K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 17:47:22</div>
<hr>

<div class="tg-post" id="msg-30131">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/persiana_Soccer/30131" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30130">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=sqVyndeAzHHrMV9woT2k4ixA_5jkOx-N0_VmBA2q-bQssqWPhdTMpEH0qCSEMfqHgzGelgRZFoGNdZMH7jMccTL7cfeh7hTogIpe33T-sjYYStIc-nC4iq_jCxkq_jJ8hWgo3N-6jh7ym61q7qyTxHG3Hgio0Yh0F_WCEFgxIy26NMbtvVnN3lPnIwd0O8pjuE7_L291o2N9F8BVXnkz1SSzfJfbYX_taaIMVYBnqJj3fW9ta7P4UijCjZQYw0OjYqDl_7U-lSsfbmiS55SoXRsH39ULPlxJzdl8P1_dRIfOyHS8IbNSn-9eb_v3j4-IWQo5fbx2FiVyVK7FRcvvrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d3be7a360.mp4?token=sqVyndeAzHHrMV9woT2k4ixA_5jkOx-N0_VmBA2q-bQssqWPhdTMpEH0qCSEMfqHgzGelgRZFoGNdZMH7jMccTL7cfeh7hTogIpe33T-sjYYStIc-nC4iq_jCxkq_jJ8hWgo3N-6jh7ym61q7qyTxHG3Hgio0Yh0F_WCEFgxIy26NMbtvVnN3lPnIwd0O8pjuE7_L291o2N9F8BVXnkz1SSzfJfbYX_taaIMVYBnqJj3fW9ta7P4UijCjZQYw0OjYqDl_7U-lSsfbmiS55SoXRsH39ULPlxJzdl8P1_dRIfOyHS8IbNSn-9eb_v3j4-IWQo5fbx2FiVyVK7FRcvvrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ از مصاحبه‌ تاریخی‌وفوق‌العاده گزارش گر صداوسیما با یه‌کشاورز؛ خیلی خوبه حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/30130" target="_blank">📅 17:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30129">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=YiQd4ABpkhZZpWbGWw3zgGCU5vzARSSI6mJA9IbDp-c2tVJHKyM_li8-qP5h9AMMjdGEqMgqrjBX1NhqvYvm_wlUveCmmKpZgs4O3nHUWb8HiZjqlGdmrz0s9USGrdxhJgEK1sMlpg9GJXNsrRt_qNU9afAfTojZSBORVNN541U7agWOcGujIs__3RFxBpAeL8IxCPec5nHJLVBpYiA9tbj57-ItXEH5YDPAWYsjnF3bL-ZQqhvE549Fd98I3q642T0Y8gNMMkOyOX8EdPXv8AuNQXEnBGtBLG3SiL6VyjCWDYSZ3OPqoWwPlx6bamRBgZFmgSUKnhSSNHzy-3-n_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37c2e1f8d1.mp4?token=YiQd4ABpkhZZpWbGWw3zgGCU5vzARSSI6mJA9IbDp-c2tVJHKyM_li8-qP5h9AMMjdGEqMgqrjBX1NhqvYvm_wlUveCmmKpZgs4O3nHUWb8HiZjqlGdmrz0s9USGrdxhJgEK1sMlpg9GJXNsrRt_qNU9afAfTojZSBORVNN541U7agWOcGujIs__3RFxBpAeL8IxCPec5nHJLVBpYiA9tbj57-ItXEH5YDPAWYsjnF3bL-ZQqhvE549Fd98I3q642T0Y8gNMMkOyOX8EdPXv8AuNQXEnBGtBLG3SiL6VyjCWDYSZ3OPqoWwPlx6bamRBgZFmgSUKnhSSNHzy-3-n_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه مهم مهدوی‌کیا اسطوره فوتبال ایران به والدین درباره زبان‌انگلیسی؛ حسرتی که مسیم دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/30129" target="_blank">📅 16:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30127">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m8xV_2g2kV19NZOBk3Y9w-qXpajAx4o9W4dW4gb1i7qnb2gxO_KqKzOB4pTdAIvtCIlv6TJFpHGcOWnw714r8dEWU8JeoNqF8xXIPeG-Mp1WcVfKvDLlcXUkn9mA5IfHZq0r9zLBYwW7_2Ef2JSYSE6z1alo4zYGfxIGETMG8bL9ybR2JHNBjYg_whQe2w990gm43OFZdZmh80m7EwqwVpXX3fMcZM5Q2k472xNdw0eEwDlhF4AW51wIQjqAUH0Ops35NUpW6vR8NxxtRZnXZwF_h30jFDJKAQUEWeegSv4BDZTZjI4wrW2glAUS5pLGeo1zBBm_jPRo-RXAQjKRIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NsIBT9s6pfIZE17JGfyKMN8RpI8XkBDYiLT0yGEAZ2FlMnD2DMUslSQOQPfA2knMVw2eKp1dqm9KDaNvrIL3SIOk44NWySiD4GNMsy0xCwoDu2XTQxMdCrDmzSqfUMIBZEhu7ct5fv4p-N0ee9NYpFk8TAa9MBHf9gZQX_H4vW_b2wntcXw2QM2RIt0lOOe-4A5mZUya8ThodStPJe18LKflDcfaKp9lGXR3qt2csA1AD1R_GLxJ-1v2W7-uvh_Ui1BdK-MQXW3sCj7D0oydmpLjTHTlNnKGAAJ9kw_IdCaFUCXNC8c8H7dojdRdQ_hgcGp8R-SneaDFqeBou2srTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/30127" target="_blank">📅 16:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30126">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6_FpapALdvVM4ghWOtmwK_gSLqZbnB59WWHcVQXly7Tbp8w9KflokRN29nKRHmNpchLw3-PXrGSiQ6OpExTMP-1GVUUC0IcIcm9QGjchdR5bB4us3zleI4ytoNIXYrrysphyMixpjd2g843g5OTDUsqxiPUlQ66DeKo-eyAFx9pvmHll1VGzgV4vXY4099vTrz_vQ9FOYM43Bp-R1j2tTXqo0nn6djFf7IjRagpHPf9JvYuKoSMnmomYJLy3KIqQgszaZj-oGxDSxsWnfXi6Jt5nh1gfL8J9MSBxy4kQ-U6lU3sBLiezCS8FSRBrF0Fp2mapPUWXEPLAvNfx0Vbkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛ کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/30126" target="_blank">📅 16:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30125">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTJ5sBfvalcmj9_safd0IEP8ugMRNhZ-dSYHGncmJPUDzahD58_wjBNkFGa0nZ7Ib4RCHb-iL5-1v-60EOuXLXbP1WoxdLuOvDqPf59BS-JABDooaDc0UhcFD3X702dDjG1cWAY7dfI0U-1ps_dTcbhMzYk22_rkOcRxReYrlIYCDtTwOaXPFPT4FCl-1l20Ziw1RX_f71hrjqqnIIvVumXUVdg523tCIUHOMbkXy_JbLW6jO5k3QRE8xzPuE0GaY6Ki6LF1BtcSN00-TFNqiZW33Fey_-IetFerWRwzdcjcpdy-O--lZTjMtvwCQe5Xl4Q1UQnvPfguA_Oe12LYnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار تقابل‌های لالیگایی اتلتیکو
🆚
رئال‌مادرید؛
کریستیانو رونالدو بهترین‌گلزن دربی؛ 22 گل؛ اتلتیکو در 10 دربی‌اخیر خانگی تنها 1 شکست داشته؛ 5 برد و 4 تساوی. مورینیو دربرابراتلتیکو:11 بازی و هشت پیروزی. سیمئونه در برابر رئال: 50 بازی و 14 برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/30125" target="_blank">📅 16:06 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30124">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJhv3DXz2gZlndqaJgHhgUn4q4aSwduyjJeVnSnt0OEdASgzULKSluOatgMhQcTMGG4R9if8OtXnbCtGw5u0Qc-sgWPGAu4n6eZyTng6yuzimQl3kotKmThms1cF7SyYrrIJe7KcgmHDueS_5kUj8MgUzsPe1-InINFnNQ-fRTzLAqfIoLwzGSFDP3VmW9S6AHtwll-fcmfEGgY2XWaQWGT7kQwT2fLQaJ-aylMveRShse9aqNURZ5MDB8BhDnfR37a20-8Cupx8jNI0u44fNvB1Z8dfV_GGOdBvivUxsUqFsJCs42Mxa_rTlsjt9GP6wneSLUtCRXOQ5OaiPI-ZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مدیریت استقلال و شخص‌علی‌تاجرنیا رئیس هیات مدیره آبی ها بعداز انتخاب‌مدیرعامل جدید آبی‌ها با مدیربرنامه‌ های یاسر آسانی برای تمدید قرار داد سه ساله ستاره آبی‌ها جلسه برگزارخواهدکرد. درباره مدیرعاملی هم چه فرشید سمیعی انتخاب…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/30124" target="_blank">📅 15:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30123">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujye6Y_nLJ9y2wOAbKEXOnU9Z6410YWVdsC7cEAuVs9Pi5inr8FmkdVv1YFWkdryTPqhxYaHJTie-pvmwT4x2-uejOIwMxLIHr2r_-ayenbpdV9aysqAt0JKs5OzN3BvosB3QrQpoW3bjAO0J8w6XCTye94jfVnvdOmwVPGRWaRS3jfAEIr83XHTr_bEsYqiyytFvWi0rdZlyKA60TNcoFipecUvbuOMWYbqbUp8ZnqVLYzRIkkSRHpOFSkWbEYNbrqPjRpU5aH1aKyEHOwvo8pCJebRy3Y8n3yt5Al-le2m5ogz3o6TmRozuLNy1gn88FUk0GAa58ljKdVlC2SJ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مقایسه عملکرد رابرت لواندوفسکی و هری کین در 150 مسابقه اول با پیراهن باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/30123" target="_blank">📅 14:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30122">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09969a195.mp4?token=MluwmVJV3UjINIPVm5EWFBbcLHP1nX-pN4VAgLOf-JupQ9hz-MRNgQIqRKQuSizelLat6wWm_BMZjDG5Hw-6ztKHv2agCg6X2bao_v064xgeS8Ve6odwbGce6_syU3okRRMaI0vatqxbwRIgNxL1kHgOrTMghN7_i4uEYDhUeJvJYQwWIA-PZlrxEqcWrOO96ru8tGy7ph9Ej_gmS0pCGhEkBufXI8EQZqR_UWVqCopLZVi0PL5HJgvtxSeBLxWmR4QsQQZhNF9ysMspL6q-fPKLrRbkePT69eAsEijgUE3qV5Yz_6m4DWa3oEwcOs3d87SKNYONKg_nVBLYZ5S6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب‌ و شنیدنی این نابغه هفت ساله اهل شهر تبریز: در آینده میخوام پروفسور بشوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/30122" target="_blank">📅 14:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30121">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJD06fYXFgazvIGMUfZBqXfB_uETzl5biV5nsgHZjgGoQ4imZ90qb6n_Tp7yH3GEgBQ6JDbKhnq0scJcpJ7TBlzAQ_o6DSxiTATXmUn6NZpTcBl7WTTb3SJ4BtxwiyuHgDQ4p-J84JKn1KFkXGSAezOAzbXacKJB5WyLi-XYdWf3CM-pIVTLTIu09lffWDkFQgp13JV_z6QWI5MZr62iB03y-RCxXtPTPzui5jucbmOEmM4mUFADi_qAtaqfXeRc6RQtbV2LYEdwFgvBPrY3fl_3WzQCUUBMfdCd1MOa27lpyxEj_k4RpaPdELsA5JKFbZr_iqhbxUUFUIseRWze4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق اخبار پرشیانا؛ به احتمال زیاد سعید دقیقی سرمربی‌جدید نساجی میشه‌. فرهاد مجیدی که مجوز فعالیتش درلیگ صادرشده دیشب ضمن تشکر از مالک نساجی به آفر این باشگاه پاسخ منفی داده است.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30121" target="_blank">📅 13:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30120">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXvtCab2ZVyz2hzkkujE7ClS98CTdotEo4kcd-59jH9WRmGIgvJczPpGZltRlnDn5ROiNxZcqYGYqWSYbRLVhoxekTiLwGPIaG1An4S3fAR7k2_Q0_F0Z2pNzmcZMQGZOS5UtV1GofDoJAlFUYIA1CxHhexFP1rDV9hSVOYtlZ9IJ3VEXjyG5ZegCCGezEyrUS-bu3ksFV0GWiu4JL7tQlztxjtcZb6NVMahO5TZEvesr_2IJoP8ncMF-hdZLL8xq9qTFDEs5EeV38OBUd16V9kNRjggLqwT8VV0LkOmRnsu9n_cGef7gKOCyZTU8wICYD4aUbG0CEz1hfNFXPMzeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فرشیداسماعیلی‌بازیکن‌سابق‌ آبی‌ها:
رفته بودیم اردوی کیش با چندتا ازبچه‌ها عکس گرفتیم بعد از ۳۰ ثانیه همون عکس بین فن پیجا پخش شد. از اینکه به این سرعت عکس پخش شده بود تعجب کرده بودیم. بعداً فهمیدیم که خودِ سید حسین حسینی ادمین فن پیج خودش بوده و اون عکس رو گذاشته بود. تعداد فالور های اون فن پیجش هم خیلی زیاد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30120" target="_blank">📅 13:45 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30119">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7061b4b2b5.mp4?token=GccpSAhP0b9KA8YkufcZ0W4RzCpiwGsZCKGb3LhWK_JeJ3odoh8OvzRNjAkTKEwht3pdknzwYGwMstVJJSd8BvdGwSj_vqpJoIl97bcbpnJ-p2vNG8Xt0US6Hrbgs2RJO9IwYOiaXegZoM7BgluH_4-u2VNonoKDu_NFThJOEEwz3WKAUVGBKNEgbwsRS1aJNGEQzk093qQEmNr71j8P09MJtsuU_ZYMcFBEjSJmaT46DfN6AaRbhlgL9aVVNKBqWVDoIODoPNWIXTXA29uS7OOZfsJ_DYg4l452jdlXKrplGcDPjCIM3PTFAOhgrKnN6TozgoENLi_h1hZ_ezsjrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
👤
#تقویم
؛ 20 سال‌پیش درچنین روزی؛
ژابی آلونسو ستاره اسپانیایی لیورپول این سوپر گل فوق العاده تماشایی رو درلیگ‌برتر انگلیس به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/30119" target="_blank">📅 13:37 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv4Pn1JBP_DtFOzkYICBj4miL8mLszgj0l7ZhXD_n_dknpES3B_z7PoKdUtVzLCEkvph0iexBIJwekGVMLuCTrO9BMh0CrkehsRspprEZGZlTAPytLEQpxwguVSHZJWGzeKOeiZBISBTVczoQS2epW_G_0auH1ex4dmqyUl41R3yU5E4m5xpQCWqMf0rN1dVVwil97NxMUj5JXRwpYjnElHJ2SkboWs2f-UZZuSDJ6HERsuj6HA4kOsf3fH289ZLRzZerKSbA41rdxqZPmWk-LqVsgk6hDr0i4Zmwj-91ZH9D6rIYxjG09CO_b6fltuHODqEKvhbrr4FJElpOlgzMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/persiana_Soccer/30118" target="_blank">📅 13:16 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVU6ElnhcHCwOogQWFCa-xMwUgVDmtqDoUr6_NcFDW30AJ6ToxE2C3P96vOC6kF1-KpcBqGn37b59Q_wWNZeYT9LMvu5psiZNqHBCUFFr9lJY-kTzZmpQeJ32cmm2AcbZA0lgaV7wsvmdcC1QxlJ8oFTpwoN6CF86sLX4oJkn7cSoS871dGrmhovycMr_TUyoFFfR206K2fHqmEyu0OI7oBbLYxmy689QDXvIBV7BXzWy4JXDjQ8IpTd4_KEitfNmxjfyENLRdOsEn-J5TSDnYm1qHqpOAKPGCkG3OTqqD9i6CQDvaTLfiM8GEG0FRk0LAGw7Xjgnsz_86PKacq9Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های دو تیم رئال مادرید و اتلتیکو در تمام رقابت‌ها به مناسبت بازی حساس امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30117" target="_blank">📅 12:48 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VePK8Bwk6nci8rGCuAVW8xLemTqr_Q3mg0xtM_56lm5McLV6wniBX_dy1EuJUuppfeKMqZ1-qXR2wPNY3VedOTD-T4UJKxkF5tnHFJ2rjq6uE9vgxlYegBo-Goy1d1DXnnhsNjXlEoPlhVTDN6hawCfbcT7XoXfOoqi4uag1rDLenhdex-JuCUjtfxFAlOU8zaXMcO-6kMTmuSHsgI3ufEd71hJCTT0KVew86DEtxvWRA_Z3UXDYt_yZbAdvKc2eBGEHQw0tn0W17OZMmsG4_lLNwFSnI5SIhz5-PxLYQb6WVFSTPDOatomuNGoK6Kb_2zbgCdMKjnszdFrtHLBBBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عباس کهریزی وینگر20ساله آلومینیوم یکی دیگر از ستاره‌های‌جوان لیگ برتره که مدیربرنامه هاش درتلاش که در نیم فصل او رو به یکی از دو تیم استقلال یا پرسپولیس ببره. شانس سرخ‌ها برای‌جذب این‌ستاره 20 ساله کرمانشاهی در حال حاضر بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30116" target="_blank">📅 12:27 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWwZCh-ORmAflKjgt8Swt_P0Np_NYYa2WP_Wm4rPA91fDMWn4UcUehJHcSpXHlNfF2NhhNqApEAcOvHIFpova9wf4rv413RQ2WA9N7Z4qVif5009rAtaTs6T_SM6RZVenwz4vr_QnUTOCgRW37fskMwjwodhjJ4rhjwEcdOLhaXCJIIb9ev1h0BpLWcKYMc3h50eCYpp969t34tM6kencDDKQ-zqQ3utctNg_HObaFLSixKWjXu0yVrgnMrmhtGUR6LDC0xeIEP876AvkWJAhpSYG1kdCdvqYB_MYOPnFtRtuMqhCEXRPdEx9-IYPjAVZi6eqBIb4xT4XGtOQ4Ew6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇿
لیست‌تیم‌ملی‌ازبکستان برای بازی دوستانه با ایران بدون حضور ستارگان استقلال و پرسپولیس! این‌مسابقه‌دوستانه روز دوم مهر ماه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30115" target="_blank">📅 12:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30114" target="_blank">📅 12:10 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCVsVrcjTpZIEgIV7Dw4SbeyeXIgynf8UFyWvcOyyD8groxXqgIpXPdwpY91Tk2LNjfhekFekbzFEeeJaO9NA4dVyK3Wh91yK1NOtsTJPQmbkj_mB3WmKbZAXu3rtgy8iM26oD3sY4VADjED2-LLTC_Ov7erbsInjcfkoRtGGNnG8tzvGZI6lPR7Z2zno-_85ctLBh9kPhX6sQjTUPmTZobIJgTyJsUGp1h7Jjfq_bn8gpgDaecEnUDx0Lumyvv9tq_DF8Zc3N-3LitatizeiHAR4Noj7SLgSpwgBQyXIwvHakXsGD8LETBMfwxPirChre_Utw8MDikdAVXih88MLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال اواسط هفته آینده بامدیریت‌تیم فجرسپاسی جلسه‌ای مهم برگزار خواهدکرد و با پرداخت 50 میلیارد تومان رضایت‌نامه یادگار رستمی وینگر 22 ساله این تیم رو خواهد گرفت و رستمی آذر به جمع آبی ها میپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30113" target="_blank">📅 11:53 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30112">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QmWHL6oJH7poRkYgW6SS68JCy42ru2qzJVkwkhHPJMBS4LoclSKP5LNkmZdYvA7Z9lqbOXN8cp-Tfd1zYh8pKGCAHKoXalFjOVA9P4lIBHvFwez-nYGOaiU5ePVzYlkrlWXayyLxkxGiIknG1bvyUSUBsAHck5cYi_PtM6Fg_ubzwS4OjuOw3ENnqrPq3DJGOZ9HBN2pzUngY6UWpnAfltYY198047k3vO9_S6pYs2xAVbJA_TYzc455VN0Ec7EO_O8Sb-10TCBKJ71bLc28f4ojOjy6uD8KGLKwNzV1ZKkc78oZutQUHZbbhNr9i7-RT6AulGqbtBmqJsABTjQqGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
رافینیا دیاز تنها در یکقدمی رسیدن به رکورد رونالدینیو درجمع‌آبی‌اناری‌ها؛ از رونالدینیو تا رافینیا؛ ۲۰ سال بعد یک برزیلی دیگر در بارسلونا می‌درخشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/30112" target="_blank">📅 11:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30111">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KnMbVfUm5IaC_sb5je2UHA8VeYB-1TFVze3l0p8gzIDEs-gxlx9mHIfG0ibC1-wFiMqsIjKu75A2Mf8x85Jq2IKT9WTVkRWseSMp-p6JURc2C_sIxVpzsUkjRrlmWTVcwfT8cZgjpikJXgtT0YRIKcalzrXCnHoawobhzDR0gil41SOpW1srB_vUWwZP96w-s2N9_FJB3gWa_DMLUUNEJ-jXfomeSxEXrO3rJY7WBmRRHe-gV_38scXTRVbNg4WOKIVbqjEqVeJacpJgpdSkPMcRexBpXwDLlFMYWzfQmztrSyLzJY_I7YZKcZIRHMA_EhveAyXE-pdmi_CjitunHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لیست‌آپدیت‌شده‌سرمربیان‌لیگ؛ مجتبی حسینی اولین سرمربی جداشده درفصل جدید لیگ؛ سرمربی بعدی نساجی‌به‌احتمال‌زیاد سعید دقیقی خواهد بود. فرهاد مجیدی آفر مالک نساجی رو رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/30111" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30110">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPgBOpaxFPSDi73cfgR3PiNR962bxugv7aEGToKmJW1LtvBavFSgWGiM3BIynZuf9KcPHamPNLngdGnaq3Uh_k6sawQSzvau1PL3wSH4MiL_vsFhO24zkbC9DrsKWuz7eOpaIyLrtTAdW697UJI0nbzWdMGKpK7c9SPy1FEK-9O5tymiDxmTvNzRMd1XHGKWCnBKgwU2nWEbEQpvpcbOuOG49ITGw_oSvSaTA9mAUR9pT4f5kwIA4oB-nfhK8Q6mKMzrsH3H57iraHz1p0DfnWCZWL6Vqbopyy3kBkPsCY9EOv55LYsftnvedHBvD98EyZxKKrwbxXxdj38olsqkEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تیم منتخب هفته اول لیگ نخبگان آسیا در غیاب ایرانی‌ها با وجود درخشش ستاره‌های استقلال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/30110" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30109">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLK5QnupFyZSNVUqLdg9sEwsHHxiS-JwqoRw0DKpV6ib6uxu52s5NwUvELnSt8_cfuvy6TDekU9vKgcavMt5ZfX-jfNdKvxv11burmROUst_4-D2AEUnm8ukaMD_DumBoAowLemDvaHSsrzS22PMZbanum9I9uWwJj_rUVhapLqsEv5AdlT_G9wGUCIzRzAJipTAAe9ickfb1xUMM7-07-QihJRqaLlxumseivKjhy9Y6kWImyHGROxju6iXJ3kh76aXKb60auuHg9itD4VotWFMmljuczE-yjcKY2gAgxNBzluKw0dD-XOiECyBV5fssx9QlOojX1AeqCl7U8Jfew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
⚽️
لیگ فرانسه
⏰
شروع بازی ساعت22:15
⚽️
مارسی
⚽️
🆚
🗼
پارسن ژرمن
⚽️
💯
اولین واریز، اولین برد بزرگ
شروعی هیجان‌انگیز با
🤩
🤩
🤩
🤩
هدیه خوش‌ آمدگویی ورزشی تا سقف 250 میلیون ریال
🖥
امکان ویرایش شرط ثبت شده
💥
برداشت سریع با روش های ارزی و دلاری
💵
شرط بندی بدون محدودیت، بردهای نامحدود
🎁
با هر واریزی
🤩
🤩
🤩
هدیه ورزشی شرط‌بندی میکس دریافت کنید
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
r29
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/30109" target="_blank">📅 11:19 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30108">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛ دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/30108" target="_blank">📅 10:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30107">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBzFmoH6A8m2X0bljK_aK-gXLJq_ZXDydk795eU2fEIAOY6eqoZWjgm4Aruy6AW3MFZgPQ9CKKAIa1iFgwSb7QFkYJTDtQUgR8OFiBdKpC6xUzOBt2Hrfmf7-E3YTZiN09qYN5zQtsS9xAMRqdJdbDDFx6O_R-b1VPWKOm104gy8d8ZH2uy5YF2yYfOh_qi7r7RgnYNPzmrBg7Tp8dsbvY_0SsfKAeXWi8ODN1KftBYtDMg6H3LbWMiCsujrBgGocCkhnlFUiiSrJX5wyCVYgyAJngWXUnd1Vbrk4WPilUFnW61TG7v-oidYlu3tBFmX1NvAeytPwtc_AltTUZPEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شرکت EA پیش‌بینی جدید خود را برای جام جهانی منتشر کرده و بر این باوره که اسپانیا جام را به خانه میبرد‌. این شرکتم تاکنون دقت 100% داشته‌. ببینیم کدومشون درست درمیاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/30107" target="_blank">📅 10:13 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30106">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi-nzu3wbW9O5ndF1v7hr-ziYRmcrY1-sqELVXW5q47lo5ZkYNOlLF7tMi7i54z-jawpDIqod3s4Sh1RVvRf-gxpQGGu4YcRPApBEiif_Klw7yw3EZD0CTrrAGW3zj4EawprlYaKV8gVZxjaLuHig9rgkI7lN0smEaDoi3Z2-JqRGA5SUD6jQMXbLG08YAeKrvYMPD3mtew-erkgnLQW-7Lh9O_oImlr7RWDNzC-ridTNMoat96-Ty2u4D78yxr3I0ffv-cQCOZJPQRc16qumfk44Dtd4hAB3ycWmiBIoRgxyr_3yXMx8KMwhyQFMlOt_vUCPUJiY9m8SofJON1e8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت فولبک‌راست‌بارساکه‌دیروز به لوانته گل زد شروعی خیره کننده در این فصل را ثبت کرده. هزینه صفر و خودکفایی از سوی لاماسیا عاملی‌ست که شرایط اقتصادی بارسا را در سه سال اخیر بهبود داده است.  قرارداد بازیکن تا ۲۰۲۸؛ دستمزد بازیکن، هفتگی ۶ هزار یورو؛…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/30106" target="_blank">📅 10:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30105">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9e6-1VPGoGPUe4tH0VheyQ743sleEjqYcAKvOXVlGlO1k747WwlaXta9HzM4KlkrzclD5h7Oez6IyY0Ca9n_kMRflg6UXDwxpMy1J9rAuEgdOQFgXxAzXiJCYWZ1hrVkoCXv2kCFUukYn76NTisuCfswltdTFKqn2nWK69GpEuj-vLdQpNtknbAqkI0USWwIx3EXl9ljBhja2dimf38xL-TxKLntl-w0vk9RW6LgbZUWMTMTmmbOGBRbFe-ei63OpYeclU20Kz5AvldC48m0E7AgzYAZv-dwpjEIGiCGjbVDw2P84y89nEl00kR4DqTMkUnx_lbZoCUpzo5LQipgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ محمد مهدی زارع مدافع میانی تیم پرسپولیس که‌هشت روزپیش پاش هشت بخیه خورد از اواخرهفته‌آینده به تمرینات سرخپوشان باز خواهد گشت و مشکلی برای همراهی تیم تارتار در بازی روز جمعه 17 مهر ماه با صنعت نفت نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30105" target="_blank">📅 09:25 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30104">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUFTXieoG-yxxXDYRWKQLdfaxROIjhAd1u-tdDiI4O9PcE8b6VRdT-wy9AdKS7GpWZcAssAf0uiMIOU3MfFennpOtkZNfzsbW3td72IsaHpVs0OXh0DG7c7KURDBa7L5IyhnKIhQNpT7q00bppgzBTiJ9P0zIgTJT9Lm3XtXQGGD5rTpsXDVhfAI62pmgH9KHZ0zsKgrRN5tbYE_ZZwhyoDSMkCDPeeE47BgJg2S0JywTeJUyvAtqPlLavlaxwQsrC0I_zw8OshhOVEi-in2ZJEjvKFuRA4KIQwODc5-Kpq-baqoowAXKJHHqtQHICczKbyAF8abkRPQnQOfVKB-cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30104" target="_blank">📅 01:30 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30102">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3cOl_PxZpvQqewNuue5PEE5E4uASzpR_0h2hWoJzZDlGnjAmijxO72kKmaDWptdLxb2fvwXEYnSpjHe7Ig9SYfksfcsxFcp60B6pzg6ZswmO8b--sRehg5Maae-H_qNy6PI4zkC1wtyUT6I-7l9Z0T6L4T8gZKg0AfQ07cKTQyy9dhIzvR7qML4rEr2iJRRv3fDi4UwDb0qWl29-gb2QGhg8ilxf3_Fj8FJheGsSOHg126epCrtcabK2JJGJOJYxDEi6pBf2PqF4IG4Vp90DiMFlr-835dWl00a8Owp6cXu98xofFHpvphT3TjMNCHu7eywZV29PrZWeI8SnXSBpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ از تقابل مارسی و PSG در لیگ فرانسه تا دوئل حساس مورینیو
🆚
سیمئونه پس از 12 سال؛ اختلاف با صدر زیاد میشود؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30102" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30101">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qgLra4lCkA_uR9jpI1AnGSI3zAWfhWmLrYtmjdQVXjPqRQVVOQNXHKTFAjlVLw5ZkNbzeIidp8o5ALVZkEZpWe4xN8XU7wQJOirC541jy3GLrHCFGYGQPAjLdC7o8_gIvBODdgbrU8AXVSXQciOEQyaLoNLJgViSL3-8UgfkcvKXHZyf5l0jfJLG2_oQKy6IL2W-Puur3YzANvfT2QQ8ZRgK4hMH93o4On1cj4CckpynHwDQln_u5Xja4vppeSgJghfGw3tiFUI6IAsIcggBJHsdLy6cawTzJDLrYBqIWoH5Ed0Go-Bz_gjsY5tPnnUXE83T5R1jgOmSbuFjPsMgQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از برد بارسایی‌ها با هتریک رافینیا تا تساوی در دوئل آماده‌ترین تیم‌های سری‌آ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30101" target="_blank">📅 01:28 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30099">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTJZhTQkWLE9ufxjMprg8XTfpFSNk5LqaG3XfXQ8aimoZ3GIGWOdY1OXhYHrn4Ry6DiUZ__ELIlT7JPWcd3UlePWIs-Z1RRz9Gv-BYilXn5aMgtYWvf5Ebh7QtBxarhssMEtIKDMBb9Oz7r_DrCcqwaEEPGB5w75JKeQ5IbjvsBydYYJ4TZpGyNfMRRB_YZF4eNZ5GnbgtbfUttw2utvb0Mxc1tPEEgXrJXtCE0N1sOu6ew70014NDkkzCkv_H8NKiEPfhhSdmC_bDdBI1wDsv4a5X_Yb0yJXxCtQCfka0CqFPjHTXbb-y_eNiRkD1iCtik1AQ173fU146MJHmIuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q-UH_msEs5wRcau_cvTcjNJnIgd0Q2GYCBAEepETWiA3VC5qyeioT7a6TgvaUpGHk9JxTwLiX2OlFlZ_WuCE8mKChApb3BlUFNmgsgsdnohxEcIcH9mE3W6bFInwmFwfGYsBy7i4SCkeOYgA-wH1wV3GiBDGJmk-Xll58n_e_Z7sfnJFaBx3cGhipk8J7TfUCoVw7PjCzrBYYZFtjEot5kPw8xaNcWwvVh8C4kzBXKZ6v1P11dzVrpik5dq8YGDYAE2aZjrcz33PK2Cwg84JeHVIxS21WvuGPNR-OA0MLpja2BlHNXzjyvuqu2oLeBckxUaeIPetDarsQfVMSPQJ8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30099" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30098">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/msdryoD3u0kk2kpjUjWcNHvEg0CiYwgaKYOH6JrZc2UsKN1JblWNxd3QuFGXBngFTIwbtpk2NTdXJU8yNj3sa97qGE0PmkGZ1CFb_4V5-tbnqFKjgGWAyW-rIoj9UrARfcb_16NUHFw-kUfPN7n3pmXp1eTO1SLk0CYY_xyDRLqStftekiac8kQFgZ-PQLzJDznO3AVfskaVidvB3p0kxXMaUrOxldrbK5M_k_VuZA5Z37moSU84IA_SkFhFRPmWcTwC7rXhl_F4aXKLbATZBh8FH3PGxoKrRu9cdlK_5SxdmbYHdJDLltcDM8mVgaYvmeNIs30O1mUdvR_Xy-Xbtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد فوق‌العاده بارسلونا در این فصل در لالیگا و چمپیونزلیگ: 8 مسابقه، 8 پیروزی، 36 گل زده.
🇧🇷
عملکرد رافینیا این فصل درتمام‌مسابقات: 14 گل زده، 3 پاس گل، میانگین نمره 9.5 از فوتموب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30098" target="_blank">📅 01:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30096">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4fLrMFBsAqc9DW4j9qSTWtZuhNXRg2FOeY-uwQN3MTjEFU4c-anfwHMh0Bjn1wp13SJ11gjvFkLqxMDyq23dmYd9z1XPgrSwue-eSu6Sw-jhoGtWNWeO86Bx6-rDBLlD9yCaNzS1OfMifajUoF3j3R2jpJaVt7J9_a_knvIi-3unAFy1FB2rhQ0Qvy6Mxg-Mag5jrv75Jx3JfqGmjk7wKp7_IEYXBUbg1WaifnWFfyraLyrpdR5zB3yQuwuH11Aj-rl-edWNloev3Y3Dkvckmhm_NJTb79R1vUe0TGn-f3mc924_V1HVlx7d4WUMGUAlJBvIjVQ_b0ubYwuGHMddg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|پیروزی شیرین شاگردان هانسی فلیک درشب درخشش خیره‌کننده غایب بزرگ لیست توپ طلا؛ رافینیا دیاز یه تنه با هتریک‌اش سه امتیاز مهم بازی رو برای آبی اناری‌ها به ارمغان آورد؛ هفت مسابقه، 21 امتیاز، 31 گل زده در لالیگا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/30096" target="_blank">📅 00:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30095">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NywnF7s2etYwcQiNVe_ZJrxSHavA-6PnR8feHdxwnbovAxseDOGFjdVnlDCozPbO69bXiI7MZSmM82mjrG8PlwDdHBHTf-4vuvjn7S3NtUIc_syyoyb2LXeK-P_l4evANLm_eCH6ZosJC2ytyqfSx4TQoFTrW_eimMCKVuT5sjDzLkt8vinYTVg1IQAO6u_noppfcom0yZ_QDZeW2JLjd741OpGUVAbf9BSHbzCiYIqiYtRdFX-Gb0ryAvV3JD-HvVf5ORnubQbO8VQdUfVl74WC-StgquPphZkURojqIegwxf-t02Dj70xMbLKl2jmQ5wBOWhAviX9t7vcjRvvbmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه‌بنده خدایی تو سایت پلی مارکت ۶۴ هزار دلار بی زبون روی پیروزنشدن بارسلونا مقابل سویا شرط بسته. اگه‌این‌اتفاق بیوفته ۳۰۲ هزار دلار برنده میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30095" target="_blank">📅 00:29 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30093">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqJmLqgCqN1XhPo88bgZHsVCbUItP7mFzpCHzUpdqjAOobEfRqUjDqD-se8w-l8Qo1ITPjbmym2ixg4BdNDU2QI8JqQuRYptBi7uA7pUkC6zeiMVQmrwoYBg_075uTb075NS57xFg4cdq77boQEG_PKT81h56tCA1VEjlbZh9YvJ9sUlr-o_QdgZZV1JgzVoPG6XSuLnHDysNRIvmNsbIZMFPlvqicWw_JOJam8BCYxk9_z668KpezeW2_h7mPFGSoCai5AooVrTdubyz4LL29wcUYOzrzC1BGt6wI4zoM16yUQ-FwcAuOJpF7rww6uMkdnPyAnAsk9rQtMxBuuVKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
گلزنی دنیس درگاهی دربازی‌امشب استاندارد لیژ مقابل  سرکل‌بروخه درسوپرلیگ بلژیک؛ قلعه نویی تو جام جهانی 2026 میخ کوبش کرده بود رو نیمکت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30093" target="_blank">📅 00:15 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30092">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLx02XFM1mIqwN6NxerZNS7Jmzcj4RaMmdioRtUAhcR4V6nEWILjzkajHTYnUj1Eu7RQaIrErvpifB7If7YWRwaV7xiq7YeaNYDrleY1cqPNXEZ9YDRdC3oBuXxrqKbPnvwVXluQQHSF_tLX1B6YyoU4Bhyaf--ON1uFdbVUpXf9YE3ttF7xvZnX0_NlxNqHEHY1nBaBy4zyS5NQDTJJgVLJx7wD0vfdH9qs9ZGooreqI78KX21O5tarbk08m9Jwxx_PlXyZdt8CKS320HSF6H0ApZR5FGFr9R3_phrqd8JwT8CSX4D93gx0JgZ36HGuAYrfBPtlWxTTmdtqXjKREA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یگانه اکبری و آیتک سلامت دو خرید جدید باشگاه استقلال برای تیم والیبال آبی‌ها هستند.  @Persiana_Pluss</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30092" target="_blank">📅 23:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30091">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onylzP1WjChArR373TBFiqEYy6hspV04RiNes6oZ6nxCKn_xP-HSeNoNNcebYO0RfeREfNzh0ua5PyeznfD6IrzvRnHG1hhIgg_mds-20_TutUVPJTAzxj0R-KP5G2ESU1h-26mnAWKhSFQVvRl1pMUIUfckkFhYrkMK27EVzYxI6P_xNo-kpBEKEwQ2tcLV6F4Vcr0en6efNuDjv_QrWbxbv7P_fQK_Ry5qFwoKJRK6kNvJYFrzRRsVlMnz_nHF3-fcvEdYP9xVJqA8B5Rsg4u_Us1mCIrfMMIdK-3Vs54C4YWF14RON0VaP_c9GKV7oOkGQVftbF0PYuaky3mc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه مسابقه فوق العاده حساس در انتظار فوتبال دوستان همراه بامراسم داغ و جذاب فرانس فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/30091" target="_blank">📅 23:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30090">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇹🇷
🇪🇬
درشب پیروزی پر گل تیم تزابزون اسپور در سوپرلیگ‌ترکیه؛ محمد صلاح ستاره 34 ساله مصری این باشگاه باثبت یک‌گل و یک پاس گل و نمره فوق العاده 8.7 ازسایت فوتموب‌بهترین‌بازیکن‌زمین شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30090" target="_blank">📅 23:23 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30089">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqQJ1ShrkIBTxnPkyj_b-7yXXmYX--kV8RBm7sD3TJlSNypLRuVodZj6C41M9hLBkG7LlitLICl29zOHw4PoN0qqldfYW6tHRjyDiVKDbapDcOF-jPEzD-j89PqLdZAjZfqFYgv_nA5T0_CgErVLeQVIxTdInoN_-D_2r7YuLbVBiINhbdulZUQzO5LM-gefUomRZtccVEmqvx0tSnGBqU_LEzVH7i2fXdE4k31tKejITVKWURMxq5EtxiRcoRvjKuSh6Wx6SsL3getVgNYWbpHMhyDgVL6VhYVGfg4FukSCuR75l39NX7beskGKDCo6gOBCkMXZpOBQPXVB_-Csmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ مجتبی حسینی باعملکرد دوبرد، دو مساوی و سه‌باخت‌از هدایت تیم نساجی استعفا داد و بین محمد ربیعی و سعید دقیقی یکی‌بعنوان سرمربی جدید این باشگاه قائمشهری انتخاب خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30089" target="_blank">📅 23:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30088">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idmj79tJZ0IEuZYu1KMv4Se-mzLIcq58QMBcosNbCSqS-lPUBss2HDr_22HHxL7Vev-OStpCYues9weaqvA0AZ60nS0mkG4LqZ3bMnjZNwIdfQnE9WMdEfxr16wUIBHHkXekxNNZlIcWsBgpR87MyEUayuhZ1HpGZCadaUNjZeKMOBmJzsiHsfpbCq68HF6abpGiCrCkA7PkHLch4nXDdos2qwzOtoUj9OHQQPsAnWckE-mu1MUtk0hB9ezUpfJ2SmIz7rZ-FDKrdvlkQVQ0631DR7Iw2qGXhrkpPpPh3hDhKLzsKpguTNnY3h61lMvVOb16yEGA_GibyQoqGWAzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌چهارم‌بوندسلیگا؛بایرن‌مونیخ‌با درخشش اولیسه آتش‌بازی به راه‌انداخت و با هفت گل یونیون برلین درهم‌کوبید. هری‌کین‌به رکوردتاریخی 100 گل زده تنها در 98 مسابقه با پیراهن این تیم رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30088" target="_blank">📅 22:49 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30087">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m19aYh2UQ82j5vDz7erQgSp1N78P-Z-TsR9ztREqwQQHG9fZwrPZP5syf3qMpn0CciILeLID3kB242_RICzWxOAv2i4dG1k5rd-DiNrvThp1NHN0gWrduv2LdRau2sPndBQqIUXc-jhAugmiSUOtfvFxoVISbbwjqb_FN_rCdae12kjZIy_d67oYGE4GA6TlhAIn-GBGqhQPE7_8dFK5gWqgHGViw6y4c-LBScaudLc4laCc0qp2y2pWA0cVjN1-SxEMp6IVd18XrmJLmaMeNHrv0AO0qQvDu8IN9nKzliotsiGhUKVWu-TcCB4vVTbHaCQ-iwX2FzS365XLiobcjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30087" target="_blank">📅 22:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30086">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aE2hzFqR0MdokBiXKPkmbEWxoXNvQFZ_m0zO6hZSXbdN659yk5lZM1mgVtCXrRupo6xgrs-Fp67PJ_fVPJnxgU2_3_KPKhjYJyA-ydfIHUPRrOrbZN6Pw3zBl8kIL0xGob7cr6GfUxKKyum1d49hktRyOiedAh4RgEgcSqQBd26uT5oGMcX7dsmqDtWmnkP8uaa_befU0JUNd8heUG4TDoxudKQH2EZUKQgwJZgFr0guza7iC5c5uROxuV_Itov4bI60DrCA9LI8dw3nD7JmjsVBALio4Xx64Y0CY5ctKTVlBCFY4ce_IibT0TZrDgfIz69WbuwWHo1h5imHWhk11A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30086" target="_blank">📅 22:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30085">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mthtyuuvogo9OwwN2JuT7Qtd_6IT5hNd23xtRaOSWIlZsEvFiboZc5861soGyV2X64_a3Y6eUaYLM8df9ysysao1TAsCbi_Cx9DsmbNziGVPfVYnde64YslTJ6iOSGFF__0piArA2Rsc1pmsMps05ABI0zHK51HdG3R1dRJE02U-4935KdmpxSQ38tF5tkffsMCHCUCsOg0-kDrcmVRWRW_1mMbTjZ_98sjWBTDFbSIAoP8QIRMbPvMBInbrGbMUKo6ISuOkAJyGXeUpwxvhR-rlIuqkT9RG65C9yHdZcJC6YqZUyIcld6VxFQm7IhAZLnji2JbSpL9f1MuRt53KSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
دومین گل مهدی طارمی با پیراهن الوصل؛ درحالی الوصل امشب دردیداری خانگی دو بر صفر از العین پر قدرت عقب بود مهدی طارمی به این شکل از روی نقطه پنالتی گل اول تیمش رو به ثمر رساند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30085" target="_blank">📅 21:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30084">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYXxwO-wa0k846V53zN4mHs5zFO0vZwnuWmxcvdMBgldEwJERcjhhqynKBW2J0IxI_BIKgdqaTQFbbhpvRLn5-YWtMtd9MnnQMVj03qtcW3o1MOqw_T_LP6IU5lh0gwbEoEAQwY9VLIMtE-D4gGEAOAZUntK6t1cvpLEovkmQO7L29GvAxu29viKa2h0sEpeV43rv7ts-APeKbFwcSubUxrFMO5q553vz-x0J9CEIbbrKM9lgqEjJ2qz-ByKE9_tDQcid-LhNYCOpVfXMdj_Smh671FlrjKbJMlh2P2CkrEo0-Qew3vZfFMQjzBmTm_ogLQqHao0ag5ObEDtHd5nCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
در هفته پنجم سری‌آ؛
دیدار تماشایی و مهیج دو تیم آاس رم
🆚
اینترمیلان بانتیجه مساوی 2 بر 2 به پایان رسید. گرگ‌ها در نیمه اول دو هیچ‌ جلو افتادند اما در نیمه دوم افعی‌‌ها به خودشون اومدند و با دبل لائوتارو مارتینز سه امتیاز گاسپرینی رو پر پر کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30084" target="_blank">📅 21:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30083">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwIoZy1QYDmSVis7B09XO4nMC72xYpWa94TuE6iMWFiGGGYckAfSMZwgwnKL91HGOudEEaF4FrjoZxLFkomjFM8fTSGQ33FE5RUsqfn-vv_trq68hbMUsgX6Xj5TsFWQoVzuWDlwPm5aAbJnDIOu6cCMP9crNZikxtX2DJ5u7wOzXXzA1viLiVetD9eGFZoHHjruY0d0CxQtkn5p36aTzj6jXRP2ESN83Y0fki2XQPRV4XcOyxHAPqSjBINbolxYTz_kkGlu41kpYyEHNzKf7VBCJxE22emPqqwNgRhIEltq9SzDRHdXtrMDo8N6QQ7p28fOTIlDEG4a4rRJV258Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هفتم‌لالیگا
|شماتیک‌ترکیب‌تیم بارسلونا برای دیدار امشب مقابل سویا؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30083" target="_blank">📅 21:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30082">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeEoFbtKI9PtMdGfhrIZ_pnU9BlSMAmHxHDORJ8egI7wxuqITMcrvz8dtMNPLT6mgRh9Y5Ojvurr2MD3BOWcBhd6pJsTwT6xNIaYmogXnrsElrIvT5P4Um16fxEaK1OZhPTHwTbYaSNw3wR3FaRnk2dHXrDT5ehmwR1glDmE7K9dtjM_Vmz1L-YZhlry_7PtQ2AqeMvWS4Vl1_KgGVsmzGjHiyGqekPQ-8jntY1eM6t6brvA4ge-c8nckzdJgQJDIsrpsuO9cz7yBa_gJ7DsJpem1YCJX3GSiXOtSUzSQgYyEJt2fYRP1HSVNDAJPi44HOdj2U8apeKGDITcpoykTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
ویدیویی‌جالب‌درباره زهرا گونش ستاره تیم ملی والیبال بانوان ترکیه و یکی از بهترین‌های تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/30082" target="_blank">📅 21:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30081">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZmNg83CmHb3Ky4cbasjRik0_cOSK7UPloLP7OQ68JGLSAycmYwI8T5_l72AQzXV-qrkgrp05gs8P3Ie4UP4dzZS0m9Wrl6gr2QSApMQtGq2nPurFPY3CVZ0swzaJys0LtfXlv7H-JTC9SCbfEiYv6cLlXNXnMczK3XKc-Nc8pPUggVI-GZHM5xctV8dGzb3ecdtuUFs7oto2GJRhgfWiXkORVvRbgt0KkeQZ6AHYvKEwJ12QU0Mh8CEIWD3lFk-fRp0OvLpZKC3E0hYbbJQajeO-e9GbzDV53EfgWyt_amBBHXPOTgihhBZ-gGFRiuv-lJuzemgObUATnheigC7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدرضااحمدی مجری فوتبال برتر از صداوسما انصراف داد و به مجموعه آپارات اسپرت اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30081" target="_blank">📅 20:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30080">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=NBHfNv-4XK8RDmX-kulF4zMDanLnsTx3YB6IJubpOw6JCKyHLqrzQ3fiJGNRM1nETXhuFaPdUxBgsxskuZT2mvWndpKO8mXaccFZ8XdqO4r7rMKiO4vobA1wbmE94wygFT0ZD2aUn3xdpOZKxB0jWVF35tSjBOoDmwF3E2Fm67eJoQIFDXvfyojBoYpl-j8A3tqXV2bhcr2qlLT8iUWFfiJ8qc8LkKzIzQs2HlQv4wXREzG0HkBXuJ5LJuAAZe3NwORLt0SPl23Q9BGU5j352pgUKDM2_Ok4SOLcKsGdkrGAeVQzHotGYYiskt3Tns5cA_odHSqA9FOnb_vdDP9ASw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d622da65b6.mp4?token=NBHfNv-4XK8RDmX-kulF4zMDanLnsTx3YB6IJubpOw6JCKyHLqrzQ3fiJGNRM1nETXhuFaPdUxBgsxskuZT2mvWndpKO8mXaccFZ8XdqO4r7rMKiO4vobA1wbmE94wygFT0ZD2aUn3xdpOZKxB0jWVF35tSjBOoDmwF3E2Fm67eJoQIFDXvfyojBoYpl-j8A3tqXV2bhcr2qlLT8iUWFfiJ8qc8LkKzIzQs2HlQv4wXREzG0HkBXuJ5LJuAAZe3NwORLt0SPl23Q9BGU5j352pgUKDM2_Ok4SOLcKsGdkrGAeVQzHotGYYiskt3Tns5cA_odHSqA9FOnb_vdDP9ASw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
اولین‌گل مهدی طارمی با پیراهن الوصل با یک ضربه سر دیدنی؛ گلزنی ستاره ایرانی الوصل در بازی امشب این تیم مقابل العین در لیگ برتر امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/30080" target="_blank">📅 20:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30079">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSlldy4v-Y_w6WP7f0EzoWrWl3WxSdZ0CgBk_EMzbPGflXMDVhQeSWGTy6GFuulYIJPGpsZ96zfC5PZFnQ1xwYrjhgI8gGX3A8M_MF8a2zTeCuU1gJ-ru9aaPQ7lwojHPBfKt0Nx_CJyYljHFyGt7gVp71AqKxLQH5VtJhUxfxNmlwroKD1v8Oke_myxMZws_UZ7-koTsf-HkkxfURNE7TdXVkzXu4BwnhEto-RMq65Hg88qTAHoDNB7HUB8x89qIASh5sLfshecDoBVElpmjtyuJc4Q33lDwzaI1NWvK3rlOrKn0lC3a8-RvpR3XFiUox9oJ6UBYYLyWCFdFshy4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
شنیده‌میشود میلاد محمدی از وضعیت خود در لیگ بلاروس‌ راضی‌نیست و ازطریق نزدیکان خود در باشگاه پرسپولیس پالس‌های مثبتی نشون داده تا درصورت موافقت مهدی تارتار به این تیم برگردد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/persiana_Soccer/30079" target="_blank">📅 20:37 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30078">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGugPRA5IQ9Z16qzKBce9N7np_gUEH2R19KJpUnK7apmwzIX6ejTbha95oQ40ZX6j_6F1mW1hAHEAhLidZL1eAOeGC6AJbBOW8vIyLdgo0uH32GQp0ozjz001xgtgQUKxZyHHPA5vdxUkOuemgAVDywYtQ3L6bu6he4mHSTkkVifk2JJdjjJKJFNIy26vgAyD3KKUIfQJ2CUYNQ9mJWle7eY5menbLO46vW0XD9ThByeIgueqJcy0VaDhguap-c4lud_-ochTs85-inNih1z6Mh9Bo9VAB-CXzzJYIudZ6exnxB5vf8jIvrR1-wBEh-1Rwey2ql2YCTDEx0Dz52VRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
ستاره‌جوان رئالی‌هانیومده صدرنشین شد؛ چهار بازیکن‌رکورددار بیشترین‌تعداد دریبل موفق در 90 دقیقه در رقابت‌های این فصل لالیگا. نکته جالب درباره دیومانده 19 ساله اینه که مورینیو فعلا زیاد بهش بازی نمیده اما این رکورد رو ثبت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30078" target="_blank">📅 20:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30077">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKSrAjgxEc3YuDvQukqrK9MIpH3oUEFj5wPwPkJaNwz-u-LUaS4ac_F9sJGDi5yyhFpBWo_gDiD5G8OADyUHbbtUhAI8gYstp-XkJVA8uCNpRpg5TTJQnnUdqtYhJobponHesiek8CYRHVRZ1wGWNOBqWRe3B2f48n7Bmnb9m0lANYg_hrnw4FpvNh62xmAsPGMlUDPreXVrgKb0FJob1ws3dZTKKKU_sp_kpE3odbiQHeGnCs86CT4pm-_LG0MdHl5MU6ESLCkHJ4ml-B5vceFQ9X4VLRaBDwLY27VTWFtAyFzBWC2mITJk5n8dMhKkBckunMEo2xF6zyGM-n1fFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درآمد لیگ‌های معتبر اروپا از فروش حق پخش تلویزیونی در فصل جدید؛ نوار سبز میزان درآمد از فروش داخلی و نوار آبی درآمد از فروش خارجی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30077" target="_blank">📅 19:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30076">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🟣
در هفته پنجم لیگ برتر؛ شاگردان ژابی الونسو در در دیداری یک‌طرفه‌متحمل‌شکست سنگین سه بر صفر مقابل برنتفورد شدند. برنتفورد برای‌اولین‌بار بعداز 88 سال، تونست توی زمین‌خودش چلسی روشکست بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30076" target="_blank">📅 19:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30075">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5BSgqvybJGjsAQuXUIORRAgv3TVFUd8tAlQBbMM-mjR1QWRzvD3yW5cSEvVKo72JsS0K8Nk2T-L6ozc5v_ttIhfrhfAe-y7xuwvv8m-zAma7GEOUH4BybuZ8Ybf1KrIBy-pc_OhsjUAxWbAOMPvRX5UOvmTXAYKxoDRxW-JWr_uy_80naf-taBfpcflKYgZAr1dVU_wxgoOu7enT_uOaenllq_17jtl3f61iyE18BhnnO_T74EJB8PBlHczVQ_Hnwyf0_RrvmzUwek_CoEysdLbM2mdH86K3xUK7RbeldaYKOl2h1UvtcqeK-cbOzzBzqfGT79iS0mBLbnp17u0fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام دیوید اورنشتاین و رومانو؛ بعد از منتفی شدن حضور ژاکا در چلسی حالا این باشگاه به درخواست ژابی آلونسو درپی جذب جردن هندرسون کاپیتان 36 ساله سابق تیم ملی انگلیس است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30075" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30074">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=Tqg4dEstLTEJeZUnXFRPhVgPHuffHeRoHSkxR3iJgacSGILY8pC4X1WoqH6xLnHe5eE6Vb8Lqs-hGRFAXUgmbp-ntDYlKWHfLAPvVJ0xgAnehUTDhrpZ4p4bAf3ayrcMlT1IdSgFXrH3iMrt7Xkagq22F8jZxlyBt9VHigOVp6gvVuWMJtl7PMgVYsN9C1ezZ34ny27GDbDHm-I5FwRq6J0_hLQHCUPRRPmL5wllYqmyWhwz6RBmAx2ULiJZvUblaa2dVSIG29jjz0USxQIOAglSEjOi7x6w6xlR3TuxDczNUKO_lwVADH17xJEY1DXGvYLmczd716y5eMvw_deARg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5018b3d28.mp4?token=Tqg4dEstLTEJeZUnXFRPhVgPHuffHeRoHSkxR3iJgacSGILY8pC4X1WoqH6xLnHe5eE6Vb8Lqs-hGRFAXUgmbp-ntDYlKWHfLAPvVJ0xgAnehUTDhrpZ4p4bAf3ayrcMlT1IdSgFXrH3iMrt7Xkagq22F8jZxlyBt9VHigOVp6gvVuWMJtl7PMgVYsN9C1ezZ34ny27GDbDHm-I5FwRq6J0_hLQHCUPRRPmL5wllYqmyWhwz6RBmAx2ULiJZvUblaa2dVSIG29jjz0USxQIOAglSEjOi7x6w6xlR3TuxDczNUKO_lwVADH17xJEY1DXGvYLmczd716y5eMvw_deARg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30074" target="_blank">📅 18:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30073">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIIQ-JOVEkzO6nuKDjN99kYQM4icEOvXK1VQXD1T6zNG6VNBu4f4EwlYE7BmTk8EJCZJVGKltfECVNdXhsdCyg7xo9aVc9dckwa3zrEXNlX49IILQFMecDGNr9kN-W9fFwTzd4MkHCK1DcG65OxTPmRhcRONw2aAMuck2uOeplsdWicSEd8dgtOXbqIhYptMI2e_RZ-STIPVBbPF8Tkk0TJD-AMI10XDckmrDgI4QrvZeiQDFYQc9IjykiYvoAUbflSIi055Y9weQfoVXw_Q8gP2CUoa0LWgaU3drwZaSoku89iqXJfh7sMhpAjNUoczjycvaImQd014DQl5pM4Z8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ دستمزد بشار رسن در پاختاکور سالانه 600 هزاردلار بود. این‌بازیکن در نیم فصل قراردادش به‌پایان‌میرسه و علی‌رغم اینکه پاختاکور دنبال تمدید قراردادشه اما گفته علاقمندم که به تیم پرسپولیس برگردم و اگه باشگاه بخواهد حاضرم مذاکره کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30073" target="_blank">📅 18:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30072">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=NMsIvO7pvskz65e_XgF1JdVtrA4cMh_ouDoz3agsD4UeipIFrgbTxzYy06sZTHTZXwQdB9Qh0krPNwpdAhj_NZcEfhkNTAKoh5CkPGiiY3OmpC5v0Cb3hO9CuFZkDKujq47JCchMC5VqUyQBm2FOHpDQCdJQDuwtmr734LhOpeLhZSXpPa5uMUpTxFj4zLJ_NnLC0yhfX5xZNW8lSBXmRkGmbpO1yldb1TY5ngPZACtDScYPfrA8kSO_vMQj5ivIu8a0VAfqsIO_49PoVkj9MkKuYfORQRCqWF1nAFObPIUfPXWBbKnLU6pN0DLQ7Wxncl6PPH-R13d332Y_8_z3Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9989fc3781.mp4?token=NMsIvO7pvskz65e_XgF1JdVtrA4cMh_ouDoz3agsD4UeipIFrgbTxzYy06sZTHTZXwQdB9Qh0krPNwpdAhj_NZcEfhkNTAKoh5CkPGiiY3OmpC5v0Cb3hO9CuFZkDKujq47JCchMC5VqUyQBm2FOHpDQCdJQDuwtmr734LhOpeLhZSXpPa5uMUpTxFj4zLJ_NnLC0yhfX5xZNW8lSBXmRkGmbpO1yldb1TY5ngPZACtDScYPfrA8kSO_vMQj5ivIu8a0VAfqsIO_49PoVkj9MkKuYfORQRCqWF1nAFObPIUfPXWBbKnLU6pN0DLQ7Wxncl6PPH-R13d332Y_8_z3Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج الطلبه و دهوک که تحت هدایت علی رضا منصوریان و گلمحمدی اند در فصل جدید لیگ عراق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30072" target="_blank">📅 18:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30071">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDJWK9emWXq66yAxjVv2c2GevtCBvRn-X4jHo0fFXVAAVMlt8A9Rl9PW6GSawH2ICy2fSbClYk5xZSpdVDM9Nr5-mwP9vuJaUe6soc1UocZzBmjZL1t3h7FtUzPkU69lI2ujDM3P9wgKU9VvltsGOXr4TMG-LhWm5TB7kB5VNrT_Aufhmg-fMbKiKzOFXcqJrl86LB3K4lg2OokZAstXe45Zf2N8VmzODTUrcdsczuzXe5a1g9f8AOqHSORvzViYC4F1685Gt_DxQ45jWLDmx7z9ii40UyVzzkTYmuzjrZnv6yw3wBxcyJSH0YAn88l4lAfsEPunZvAEFnkhMwCYpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
👤
احسان حاج صفی کاپیتان‌فعلی‌تیم ملی تنها دوبازی برای شکست رکورد بیشترین تعداد بازی در تیم ملی که دست جواد نکونامه فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30071" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30070">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUJKf5DItL38qdgIBMc5doNb-DyZdKUIHfqQ35BZ5IompZOuzYV7D9ECA17A1Xocc0_nDujmqrIpDZ2ApKTpghQVVqgzCa1bEbCi9IG258uW4omaeEJI4P46bEhfZrHeoSFhNio6LBU-2KlZozB8lqbU_OaodyJ9iBcB8mSedCNTHDZiEGDdXkgIDQukO6Tue1pi7ESbneki2NaG49swvN2qPKZSEVpAxXj4SkJ06d6-3alY7jZAQzAm0JHa9Lq1uOaV8oLoFmyb4AZwyKqg9hS_sIJKo4LCZ4vb8IU9CbE1ivDWV2yX3PR-5t9K2S6z1aAf6xcfNfme08CPeZC0iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/30070" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30069">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gct-brLePo6yLmG2Zv06lmYRQjV-x3BSxENaFKKg2kUa0rqsPhO1VVwe5Ao-5iq5EY1uYobSLN35hr0nsT6JDlSx3W4uBWU5SNHagfZWXydDYPJQQkSB94xpcLibcrSBA4IB5I0caFYZm6eMscApyCV7IYYwT3w1QhTmYAgNVpG7lDBCV0BUZDaO1kDK6y7ICXLaSdBs3SXvp-OScsOw7u2Dbt9cIay0rkEeNvv6gmx_IcDVEBeYFYgV9tEL8u6n_nY8-I9CtjvW8SmRC6x_9PhuYzJ5KZOpLqBhqHfG1Z9dXBsiRF9XShH42iYgbFAysfN2TiA8O7IPpk20d4j_WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی Yekbet
💎
🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🔔
فرصت ویژه اولین واریز دلاری در یک بت
⭐️
یک واریز
🤩
دو جایزه
🎁
⚠️
یک انتخاب هوشمند، دو هدیه ویژه
تجربه متفاوت با اولین شارژ دلار
ی
🤩
🤩
🤩
فری‌بت ورزشی +
🤩
🤩
فری‌اسپین کازینو
👀
با اولین شارژ حساب از طریق ارز دیجیتال، یوتوپیا ووچر یا پرمیوم ووچر، هر دو جایزه رو دریافت کن
🗓
شرایط استفاده
🤩
⭐️
فری‌بت:شرط میکس حداقل ۲ مسابقه با ضریب حداقل ۱.۸۰ برای هر انتخاب
⭐️
فری‌اسپین:قابل استفاده در بازی Yummy از POPOK
﻿
🌐
لینک بدون فیلتر
🌐
ورودبه سایت بافیلترشکن
------------------------------------------------------
📱
کانال اخباروهدایا
🌟
g28
🔗
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30069" target="_blank">📅 18:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30068">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=aszp4lYJswf7q2yCEh1VgnTrDUgcnKK32fZCRuzyZO12bRtlNRM8yxcF1RCW2hGKhHFojqgby8y4n9a1oSod2g8BgNwUyzta3TP30IzbED6tQkskiLaVIJW5nqu2cT0HDChv2CUVRsnrSo4b9s3jwQCBMuLxfPYlencD-WhIMRs3RltOg_Q3QipGkRpgYbMGLpWVsT3zIIcbBwEphqv6BkR_be1pkYopAi-LJRqbGfsw3JulNNhf885u0rAKrXcLWXAa-y1hORZsstQZiqf7GBxPf4hOhelqzqZheZpAE7dmrN6LVFgMkidahjFSIqCXaRNcC_tu2bPSL--mcTeBXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/841d5e76bb.mp4?token=aszp4lYJswf7q2yCEh1VgnTrDUgcnKK32fZCRuzyZO12bRtlNRM8yxcF1RCW2hGKhHFojqgby8y4n9a1oSod2g8BgNwUyzta3TP30IzbED6tQkskiLaVIJW5nqu2cT0HDChv2CUVRsnrSo4b9s3jwQCBMuLxfPYlencD-WhIMRs3RltOg_Q3QipGkRpgYbMGLpWVsT3zIIcbBwEphqv6BkR_be1pkYopAi-LJRqbGfsw3JulNNhf885u0rAKrXcLWXAa-y1hORZsstQZiqf7GBxPf4hOhelqzqZheZpAE7dmrN6LVFgMkidahjFSIqCXaRNcC_tu2bPSL--mcTeBXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
عملکرد لژیونرها در رقابت‌های باشگاهی امشب:
🔴
الشمال
2️⃣
-
1️⃣
السیلیه؛ پیروزی‌مهم یاران امید ابراهیمی مقابل حریف خود با گلزنی بغداد بونجاح!
🟡
اتحاد کلبا
1️⃣
-
1️⃣
العین؛توقف‌اتحاد کلبایی‌ها با وجود درخشش ستاره‌های‌ایرانی خود؛ سامان‌قدوس ستاره تیم ملی ایران زمینه‌ساز…</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30068" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30067">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QsUpFttgzNh_E3i0WOsve-neNtvta5NfnWKGs53hAH4ZlorXywAdwfXrTnVRFRm9ZS2JqofeLRo4E5NyeUZewOkSyeyhL163rJqSzhaKTYp2zdMkDMLhC5T2xewpx3IbEb-ygxNdsOJ_x8w77vsmWFDR5uu3Sjf9-CIBG4pkXW6fhg4Dt09S32DIA0ulR5WHcnpekZPxDj3Igr2jEy8iSwCseIMzE5JAaRYC-z2gAdqyIBLFTTyxzvebxP1CkarWdJ3alEISEMQY3FmLmwmI_3ORq4Ml9nHX4bRS3s--049mG-ry0F8S_LOHcSnunjo11EWrNZby_kupphhsM5hnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
🇧🇷
#تکمیلی؛ مدیران باشگاه بارسلونا بزودی مذاکرات خود را برای تمدید قرارداد رافینیا دیاز فوق ستاره برزیلی خود تا سال 2030 آغاز خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30067" target="_blank">📅 17:47 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30066">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8Pt63JXQ_oJH4CWO0HUoC9Z2x3ECl6_GDcLptnGwDNGQVCjT1HI6Z5slu0n8scuSobUL3uUQoR8jxQkeaZpsWtrDKXFoUD28NZKSdyo8WUy6b-Pp8ZnAce4oF6cDCQAj3RA2l4ER2lPF8zsXMIHKm5QoM6jg41jjDQa1eEY1KWLyjG-cLwL6uBFFG8orQtCYXKVyq3nGYWWpJ47Bn99LVn_yLDuRxPzO5oPP9VaoqgKWIAM4lZMT0FWndLUN5_-RLp6c6O7FbC4CCEP7xB4uasn1LBrkS9NQmSkpYryaGTM2bV0bt3O4_n_UcLAMtDJNIOd7qCqoIovTlkwVqbEkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
به مناسبت دعوت دوباره CR7 به پرتغال؛ نگاهی‌بیندازیم به‌عملکرد فوق العاده کریس رونالدو در تیم ملی پرتغال؛ نکته‌جالب اینه که پرتغال تموم افتخاراتش رو با حضور CR7 به دست آورده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30066" target="_blank">📅 17:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30065">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDtK98HC6qZ5c9VHQU6YyUff0xF2UPkTeasTMRsmM_zIzco4CNHnWL6bMylJbdcnN_o5C3LT80hNmBm1sykx6MxK6wnaVpdh4mMGY5dgPM3Rbfk_JSXOuJY6aNJQrXjy3xW0IJIcMAr-5qlFyBYd0G0M2zFRwvr1cimi1GEq8BI8OPnyF56hhUNEjJrX-d3OG5O30s4Njhv_Nzqu_6841qx9oS9PLR5LbUZoMlP9jvBE-0aVqkiwDtIIA1bM6gwSYhIx2MXBsphmMrl--1F5T6glC4XGOjxYX8I61ZffIKFtmJZmhxLkG-RZmK9owpDlQ84mwf_xGFHGrO49eQkwZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عملکردفاجعه تاتنهام دی‌زربی در این فصل لیگ جزیره: 5 مسابقه، 3 شکست، 2 مساوی، 0 پیروزی، 8 گل خورده و تنها 2 گل زده در این فصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/30065" target="_blank">📅 17:18 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30064">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aUTWJR22L4ALDbU0ZRy6GI5WSc52PuLwOsR2bKSekltcdfP-cYrwIcdWzS0NJ3NnPqZsp99osI3UtK5jlguwxpxbQjiE5_Ktfu8jZrmLl01OPzpXiaHvb-QoDpXVFBhmcW3PYDOOiczCjZ_C5YgldT9MtDddCAsbTMhn9ni5v3KUjEzyeGdgpkACG4BjN5AaHiP53T-q_Gn7GjuZKYYhTpq9C-Gi64vSOVZstqiYuyPFZTdTwcGBIxuObMrf1_mtR8oCidklHoq-dqM5A4EYbgHsHbhf_WQf4_Da56Bn1b7_ruJqaw6uLgOAs0Ntg0GbkM6DIAAuWZ_S9ibydjJHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی شب گذشته پرشیانا
◽️
مجتبی حسینی سرمربی آلومینیوم با عقد قرار دادی دوساله سرمربی تیم‌نساجی شد. درحالی گفته بودن بافجر امضا کرده گفتیم فقط مذاکرات مثبتی انجام شده که دیشب مالک نساجی پیشنهاد خیلی سنگینی به حسینی داد و مستقیم رفت نساجی.
⚪️
…</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30064" target="_blank">📅 17:10 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30063">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=TbbN139zKJhT_jrHA-oUtmCST6H5-NvC5fdt9tKa_uj4X_BJCZThk5CgaUKXq11-A5AydPLxJjEalGwK36wMc5KHnbg_FDLLlnF5qm3MgkqL0pnqAFRyM5W5s08cP92uRoHc40DA1X6e_FJ8zTMuA1K3B712cwRUe5BEYwRbs0Ffudoq7z4ExtrPepaO8RFLB-1iIhXRMv3Vbux2SD2RhNPEXx1y46ErT81PIsvHjoTsqc6FJB9P4rxzjX7FOCanrcppkRXPQZ3djGK3YthgJKMX4vHpxi3wmhKz84YGoYa2ORR4nAA-Q1xIMlI47VxeJ7P5_6y0_r4fzttEqBRK1Tq5NNmAIg5BG5IjvzXvyQDJTyGXHV5hIbXVMgetgOstn1eJ6QGIGiVW5f-lhPUViMirNzXsJKaN2psAF-OIODCTg-cKdx2Dr1Yf234mLVD0JI7KVgbr1l5ZBW4HtRLEm8cxwGzCCefrDTX86QiUTr21p8hZX2f65JRZPThbhOM3PqjN0iTlA8syor05OrlumJUdd2MBgXgEM6uVKNY8HJ7pY_h55E1Uf049wYV4XaOdztXHROGvWWbgEAsdYML_1XQqP1MKVkMqsR7uvvYmSfwPt5cQK0Btko_PW3HmBE6BZFJQ4Vx8fednAgXSnpJLHBzN7fFyj4NbcOHwt8TCCfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a224e3381a.mp4?token=TbbN139zKJhT_jrHA-oUtmCST6H5-NvC5fdt9tKa_uj4X_BJCZThk5CgaUKXq11-A5AydPLxJjEalGwK36wMc5KHnbg_FDLLlnF5qm3MgkqL0pnqAFRyM5W5s08cP92uRoHc40DA1X6e_FJ8zTMuA1K3B712cwRUe5BEYwRbs0Ffudoq7z4ExtrPepaO8RFLB-1iIhXRMv3Vbux2SD2RhNPEXx1y46ErT81PIsvHjoTsqc6FJB9P4rxzjX7FOCanrcppkRXPQZ3djGK3YthgJKMX4vHpxi3wmhKz84YGoYa2ORR4nAA-Q1xIMlI47VxeJ7P5_6y0_r4fzttEqBRK1Tq5NNmAIg5BG5IjvzXvyQDJTyGXHV5hIbXVMgetgOstn1eJ6QGIGiVW5f-lhPUViMirNzXsJKaN2psAF-OIODCTg-cKdx2Dr1Yf234mLVD0JI7KVgbr1l5ZBW4HtRLEm8cxwGzCCefrDTX86QiUTr21p8hZX2f65JRZPThbhOM3PqjN0iTlA8syor05OrlumJUdd2MBgXgEM6uVKNY8HJ7pY_h55E1Uf049wYV4XaOdztXHROGvWWbgEAsdYML_1XQqP1MKVkMqsR7uvvYmSfwPt5cQK0Btko_PW3HmBE6BZFJQ4Vx8fednAgXSnpJLHBzN7fFyj4NbcOHwt8TCCfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
لامین‌یامال زیراین ویدیو که یکی از فن پیج هاش گذاشته گفته همین‌کلیپ‌مشخص میکنه که من در حال حاضر بهترین بازیکن جهان هستم و مستحق بردن توپ طلا فوتبال جهان در سال 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30063" target="_blank">📅 16:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30061">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UCim-z2YsCF9zXueTezlpBJKzhF0_Svi0nppj8YAeRXu2IrxuAb8QD1t_ed9JcNMy2q0meJuXkWqP2oaF2b7Q5e44d0TIzcTBekquPFMpjbcBSmLK1avj589riu_JkeMFK-FnHlrqLHrkRtpqJE1N3J6k4NCPdfjH8ot4Oi3y_3Z8rpsXEgbvpKrVMFWEwU7eiGSSY37ahkwfGe-sB_md_uCdZDQ4bmDGalmZTNm24rjeMDU1i7sVWAyotXYBOvBykPA_67Sy_EDvDhOIuIzBMo8EFofqpV5iZD-rDz6KIuTVA5dDfLPOH9lAERrZUD0ZxTCAO2aXXApPr-YA3-5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
طبق‌شنیده‌های‌رسانه‌پرشیانا؛ باشگاه فولاد برای فروش یوسف مزرعه وینگر جوان این تیم در نقل و انتقالات نیم فصل 150 میلیارد درخواست کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30061" target="_blank">📅 15:58 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30060">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9VIYMTg9Q0thTfunwrU88BP99PsgIh--8IQ75Xekdl8GW5JGUaNCm2AaJn7z89oW5zRguX4Rgva3TsP_jX_hd-gT-3IFdAnMLoEdeveYRkUHGL1TcGrCUTvk5Lt3lwkeFaS3tq3xIF0iIWeRBbiV8VnbmiUYwolW95CosX0fa175fCgZYQB-egM-dtqlxS3Oo6GNMOznVK6anNzrQ7XUcECYxCBa5VberG0mhzFKty31eVPNp3ZrwuQ1z2MVnu6olhLOt-FnsVRVsw9WkVmUwEYHF1WEEhblYwt2y7TFCLazrJErd7J9IyS9HznukS6X6wQQ2HOQymb4S1daLezSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛رقم رضایت نامه عباس کهریزی 20ساله150 میلیاردتومان تعیین شده. حال‌باشگاه پرسپولیس میخواد که با رقم 110 میلیارد رضایت‌نامه کهریزی روقبل از پایان نیم فصل بگیره. کهریزی از استقلال نیز آفر دریافت کرده.
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30060" target="_blank">📅 15:44 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30059">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3R_wCJSh6Rn_1NALXBnZ29zdP-IldWXFFE3iJd6IYndoEQf6m9KNPs4KiwpXoDLl3GrWkej5NrlkGjJBEvHAd38XCsp61osvh9UCijOrBZLx9Wjl1UTCz1ZjzmJ3fp-BW63U1Eddhcu9E6A1fMals9p5ALU3ubbtkyfsil4AcoBW2qVXdq7nH6JkOzGYhUOSnNb8hAS1HHkg1TVVxvqcixqBEuUb-caPGq9QDU5FFCGPW669t5-4cBro-XuxDC3COucoYDj6ydbjxEKJ8d_CnoYN1q_Cg41TOJY-TESu3HWE0aruongMEXGlyeG3hAUy9L9PbA237DW_z-qesJoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
👤
خبرنگارت: بین کریس‌رونالدو
🆚
لیونل مسی انتخاب‌توکدومه؟ مارسلو: کریس‌رونالدو تا ابد. بنظرم بهترین بازیکن تاریخ بدون تعصب کریس رونالدوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30059" target="_blank">📅 15:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30058">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sw0CpPQcNOZWLHwrW_ehnxLc7Bd9LTQ_qeuzqnm18J1KNJwdc4FvRNu2QJM_5pJllQFahZKbSYX41aU4iwbTXGgBD6jS1l6tq1-StIxCTklk-KmMeakR1TbhHxb4OEHJo2gtlgEDWWk3Y61UaGgw5BS27DBqiPxo2TG8aB0zy8ctp1jC4Au_4va752R0RB6V0nZzaUcnvi51GqdyMefcM7T-3SnHumIOPVt2elq1Ifb8eS-1UvYACZg3p8CxSFeCLbonNb-Arq1bBSRih-kEL0MpEh_KoQmsq2Kn5n8Po4eqtQPUFPuzo_Tqcwx2pVvKY8VNQg45IfPxM-DL6_Cwmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس امروز مدارک جدیدی درباره قرارداد یاسر آسانی به کمیته استیناف ارائه کرده و قراره تا اواسط آبان حکم این کمیته اعلام بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30058" target="_blank">📅 14:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30057">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yy2jdsf_ynvjEVw6V50YMDscDDLEpsjjFLm9An6Fdsf2vFx2Q9odImZ0vljgtZN66kxf58JXSDDzd1c5UzuGZwdSa_KmLm4AUeKHV_tviyYM_FScTWBI0Y0Ywa0XuxWtxTbJd5OdN18Gho_jriq-0gGQBwmN0L9yfjgn2nB7Lr4n7eVpr3YBJ7VQqp6oIsso-3qidgIfGkEPTZEdx7vb8wBGhpvr3170QoLR0toNCNLrhGEPtXcS949TUz2hzDaBeZIDiRjY2HfgOpp6-gCoS4UOK-nzJfAz-CeiTpe0g3vW9Aih6gF5Evk-68_qV25M2HVewbTDTBVg0owdFZR6EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بیانیه‌رسمی‌کمیته‌انضباطی‌درباره شکایت باشگاه پرسپولیس از یاسر آسانی و رد شدن این شکایت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30057" target="_blank">📅 14:43 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30056">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPLMeXZI7zsn-Eua8_2Fg8PAvdrYyXRCYQs_ZxPNgY45QgDQc7mY1JQ7GAAi2eSLMyCWTYDUCd6UGRM0k9ia5e5u-gEcGXLYTfCO4rfM7jAiRawU5nEC0EuANxboXOzWTa8Ak5K4cNEDTFZcc4Z1Zm4olKy_KgOmZHFC9f1MeecupNCWlfqfrX4ncVBSoXjFf_vlaGThDuH5TchL_ekC3tljXB_ki8rpF1fuDgrZYcvyAtZyxP1bx95fmK9Ols2XYswxdzanAyRcmQSaT8m282WrO3B34pbmdvLLQ0hqaTZkh_FcMuCQSWK5Tnx3HSqWy2E9jt2ghsCb3d0wj8x0gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی پرسپولیس در دوهفته‌اخیر بارها به مدیریت این باشگاه اعلام کرده بود بین امیر جعفری مدافع چپ گل گهر و ابوذر صفر زاده یکی رو جذب کنند که انتقال جعفری حدود 100 میلیارد تومان برای سرخ‌ها هزینه در برخواهد داشت اما انتقال صفرزاده به شکل…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30056" target="_blank">📅 14:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30055">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30055" target="_blank">📅 13:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30054">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHo6kvCUitw3boRcGloPqT2vo_ldxN880_p0aLnohKfoR5aG6sYBPlw7W1xcyWzXO3OfKy_6mhIoYp2o2D9krG60UHoaza3IyNAyWAqZ_MiALlXtiYE-BwMl7HOEXYOo2O7U9863lOh69YiBIA3BNo4XQr-sgZKr2aGNC8AW99yAeYeblm-FAxM8yDEGhbQAYfVE9JJP0Dj0FF9MMFo9lDYXSOunjLWoHsJYdk6b7ujwl0zX5uVY028ziPdGJ-ahuOWbaMlELHwCuwA78xivrGAabq9iILZzFobj2JM4BsvepzS5YwqNlaMj1jcQL_hoQ_DdkQ-Oo_NdxrV9C1YrAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇳🇱
وسلی اسنایدر سه گنجینه گرانبها از تاریخ حضورش در تیم هلند را برای مزایده گذاشت! توپ نقره‌ای جام جهانی ۲۰۱۰؛ مدال رتبه سوم سال ۲۰۱۴؛ توپ بازی هلند-برزیل درمرحله‌یک‌چهارم نهایی ۲۰۱۰
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30054" target="_blank">📅 13:28 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFAEypKFGOb_jHJ7e5UXmzK4VeieQfUAO0YpbIovXFU9-MgTu-Zzs-NdovOq2KFtg2eWye189Gy56WaQqP7AeB688aTAnKynnWTv25ETIk6S0KtB4IaI6SnPQaobrB_tBPuDPBAaS4j4YZmwvyvaybBON3ye_Jox9IznHqYZCfElFC094qOPAvE4bM9d4GB3qM4TUgMAslxgTk51vulYWEhU7yZHB498UJNpKpp1gMC7GjRa7_KE3EB1nJ5Bf4IpixHQIKQlY7FUILWU9j8qg8fcAqej2kO4qwU-tXsj_4nDU1pBKRIOAbl6wFCHtTb3YWRkbNCzpdlqWYumlNxQww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=iUFB4ZMkNfqY18451UqLeQWmzaTnUFoPaPhO_hLTFCbe8N7z5ep6m8FdIibLSp4f-Qr6CrT4uHuN_j-JT2iFAzUY-z70P_1fu7nbZ3xCNahf2KkdohhOZYdbCA2STbde4elPqsXEOJ47muOu52wWGZOYaQfWBXPEJxH37V2NaJG9jcRNwHF0vpnqB33KnNJ_P02jrgQUMyLoDvPwTnWzhRexElVBxoBjYgkbmlDuk8GWShwI1fMp0tjstBUAH4-ExHDdVJP49Oxkq01OndbWwRUOj-p40iCn2Bjwpf29FkUT8I9G-KHOtQj2m71y0BS_GERDhNn9TXOMBnuCW_KgXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5ef3d951.mp4?token=iUFB4ZMkNfqY18451UqLeQWmzaTnUFoPaPhO_hLTFCbe8N7z5ep6m8FdIibLSp4f-Qr6CrT4uHuN_j-JT2iFAzUY-z70P_1fu7nbZ3xCNahf2KkdohhOZYdbCA2STbde4elPqsXEOJ47muOu52wWGZOYaQfWBXPEJxH37V2NaJG9jcRNwHF0vpnqB33KnNJ_P02jrgQUMyLoDvPwTnWzhRexElVBxoBjYgkbmlDuk8GWShwI1fMp0tjstBUAH4-ExHDdVJP49Oxkq01OndbWwRUOj-p40iCn2Bjwpf29FkUT8I9G-KHOtQj2m71y0BS_GERDhNn9TXOMBnuCW_KgXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇫🇷
در پایان بازی شب گذشته بایرن مونیخ که با هتریک مایکل اولیسه همراه شد بعد بازی ستاره فرانسوی باواریایی‌ها حسابی سورپرایز شد. نیمارجونیور کیت‌خودش رو برای اولیسه فرستاد و باعث‌شد‌ بالاخره اون هم یه بخندی بزنه و چند جمله‌ای با خبرنگار صحبت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30052" target="_blank">📅 13:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJrwi3Ut1s2_w4f4CwYRYgRBC0mwH2gJrSQSCAsAhDWpCPE5-Ed2L1b5hrocA_YhCxU_VCijJ5bY4_hGU7zNVdCdTU7lT84F3CDtuwYaE5EQMY9wmiy-U7cTPPSUqKO8UmgWlCRm9P87ZteLq0-UWmIvDNPv4oHSzEsFmyvML1v4-E2VKsm26OBMwif_nbjoEhccjCQSu8CQpAmNkK56u7thdMGXHHUVEYz8q_UFzcSi5ohkd1Is452YWV_cIYH4pWVKBf2drqZfkx1ahSW6_wBfvGxEGWKo7xpslmzmobLVCIXHyS7JHOzKg4VKGHLFqMBdsgG5S-9mbuoV7fs64A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇩🇪
هایلایتی‌ازعملکرددرخشان کریم آدیمی وینگر فوق‌العاده سرعتی‌ بارسا باپیراهن این‌تیم؛ آبی‌اناری‌ها برای جذب آدیمی تنها 20 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/30051" target="_blank">📅 12:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=dia_5C41SBqvpSJKYtHyJuDMejdIqlfdj1lHBzLBEi3FhuaEwPG3jDfaDEkxS51muThs0Zc6YC9A3bRVlNwn11IFwn1iu2HQKkN26jPG4BkZmqQej4gUKD36FRzc_XthgS9nAEF4pntIraBym6bcqD3d4_emgmys225MkZtj8xuNzRVGOoSu3mZe3XRoHUapnXcN9Hb62Ze5L5YI1rFICIyJHvMZg8i4olzLlBE-SfzawaQLVFSPVN_H2-bZCC2_3g7e-ydu4kh3sskAO0PJnOAVRnoHJZNkTR96ac6Em5pKn-mcCZVssWF0ZJ3cGSlgP4g8ULL5wqm6-nA2m2L2Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6111cc9977.mp4?token=dia_5C41SBqvpSJKYtHyJuDMejdIqlfdj1lHBzLBEi3FhuaEwPG3jDfaDEkxS51muThs0Zc6YC9A3bRVlNwn11IFwn1iu2HQKkN26jPG4BkZmqQej4gUKD36FRzc_XthgS9nAEF4pntIraBym6bcqD3d4_emgmys225MkZtj8xuNzRVGOoSu3mZe3XRoHUapnXcN9Hb62Ze5L5YI1rFICIyJHvMZg8i4olzLlBE-SfzawaQLVFSPVN_H2-bZCC2_3g7e-ydu4kh3sskAO0PJnOAVRnoHJZNkTR96ac6Em5pKn-mcCZVssWF0ZJ3cGSlgP4g8ULL5wqm6-nA2m2L2Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
سوپرگل‌دیدنی‌فرانسیسکو ترینکائو ستاره الاهلی بعنوان بهترین گل هفته لیگ عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/30050" target="_blank">📅 12:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30049">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWZCkwHBDigqEG-Lg2qM30PSp_weZgq0tL2qoiSvd4LRTgP2muCEeo8aOobSGcdNHwJV9QdiWMH7Yt4nGMaw0gPjcheWuXfF_XLvM6-XMnlt-dOnzhAxTlSdpJ2hXJG8vjZTgGqLLD5mIjKaRM2ikDQsvkz3x9zJxZxZ4olHcNGMrgHTVGx7V20PksnvhqJM1Bazv7JrM7xD3ZN3ddJPd_33kXD1ztiDflebAicqfa5yc3bV1FOZTLcFrdCDi_l95Gro8_L6ikFdeW-G_Rlhq0sDaryyOCgxiEw_0d40NOrF6xhLpmICgAC5Gw83Rr1l84SMnnOMNhMyYxEQFTwGFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آندرانیک تیموریان دستیار قلعه نویی در تیم ملی بعد از سه سال کار با او از کادرفنی تیم ملی جدا شد.
طبق شنیده‌ های پرشیانا؛ در صورت موافقت سهراب بختیاری زاده آندو به کادر استقلال اضافه میشود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30049" target="_blank">📅 11:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auWGKKxoboKSmFeoI4AXWXZYsy29rB_l4rkN2XoPE2F7G_GaXQFO4TU_fKFQfYhzTDRjqpmb3nb5s0nGQX6i6z_-6HVxnogHAwKyi8aFKEmGjAssjfA4yZkVOcOMZCebOSEmYpFl_xa8fj2vxZ6tZBK-iUaCKYbgcK6ToZlJggRTg-Z78F1H6qRcwYbDoU2urldYfhPqU2k_mBbTT1sUOJQUoZRspb5RSygRZsvpgUahs7rctiOtLdvK6vtIox1Dr8K1b90OIR6djxunOKl957EsDLeO_lq4FiRQ42mSVDCQFdsrDeq21TFoxJegSaz1rBJfqU791X15HB7vTrbopw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جالب یونیون برلین بعدِ گل هفتم بایرن؛ کاش این پسر 19 ساله بارسلونا دهنشو ببنده! کین و اولیسه امروز واقعاً روی فرم هستن و ثابت کردن که شایستگی قرار گرفتن تو جمع مدعیان توپ طلا رو دارن. واکنش اکانت بایرن مونیخ هم ببینید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/30048" target="_blank">📅 11:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFdRiXBsdbbav-WushFokOLFfvrPCKEiBSWQV0VKIYdNMFdbzpIDmPFNPVdOJBbzYv_zdyQwi0pdPs_0p_q5A5zGfd-lQuMss4AzqeYe2ozNhSLYBEepuZXp_bpRGVx6pfPX6vWExBDPRqfhXu6_OyKi5P6BCEFXrNrA5TltVsF46s8sJ_FY6xdoPL5ukICn4CI-smP2oSBbS_vcdahR4s8Hiw3i3W8spMLekbPnW0YItUnTN6uyfXX5Mo-vKIpTaJrf1pmfGTzy9sWbqNRbPk7eEkRphrUADyfcZ6JhIH_KPKyT6RR8Hn8ji62nR4UKZ0cdWUjg5ehKN6rMyCTkDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
یه فلش‌بک بزنیم به زمانی که ژوزه مورینیو سرمربی‌پرتغالی‌رئال‌مادرید برای اینکه خشونت بازی پپه را کم بکنه. فرستادش با تیم زنان تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30047" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30046">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ljxLcj0QeqPghAD4EuujmbtmCMiIU6fWgsssScpinyE6ax0zY5rG8AfjSrWBxl0BMbM4cRuqYmxAwsThViwBL3D9z_GaQKYzc2n3dFVJqAMp_aQI6EcmsT1LOMxYLHgKtfG4bcACpoXruAaO4lmcIlhS6rkfS7cMe0i_UzYLGyRWJA0e-iOkVoKURPGc2ReoNfh_NKiT0PrjXWvLNGgQPcZaEG9mw-vm7s4MwBUVQU4ytWSU-0oQbbwpSkfa_eamFsJPH006MugEkPIN2cRHLwReNrYkGVdiHbg9scpHVVXPgJ__P19oo71tawCglrOIR7RblEn2-vKZ_f4_4K4GzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کری سنگین مارسلو ستاره سابق رئال مادرید: خودم به تنهایی اندازه بارسلونا، چمپیونزلیگ دارم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30046" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30045">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9VhISWZ_A4tcJba3AGVkievN7mWDXD8Wc5TB6YLRwGXsHd82ppI_saxfjzsT2O3OOjxFUNPVuW-jTsdyFumx9TYcqDpxtCH2EC9a4GQaH9ecDlu_gRCQTR3d5Q2FKd7m61WUDlUUFh7ZPfWnndokG7_-4TiJJrocMpQd7s6WoCha5hN_QJ-KOzohZ2FFPxLn5ftVmrCT55PbBPlPRXq0jM7jlqwb6lf1p7EH08RvtRAQ7M1W29JpX4ki0NXdcrXWTsi288fDI2xsUmVLPld6c8wFizxdCjnWZgM6z3gy9Y1I4MPYUdqaMnJ0W9w4tVPOgfQTSSk2hmV8Klv_bclYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌تعدادفصل‌های‌الکس‌فرگوسن و لئو مسی برای رسیدن به 49 جام در کل دوران حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30045" target="_blank">📅 10:59 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30043">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=BYBkBojG8JtrjWupmNG6keOfWnFRLJYEq0tJcuDv_uuxLbU5z3SsXzKqkodU6ImiYwKitpHOw35LbHk8m2uc2tlhRNLezTadcGbo_ahulD543hiT1o_tIhGj3uh8MQSiOwsHmrVXNSyTyMVwJgJGtJWf-uFZ3uLsXoG03g9zR4ZeGjPEwg9MhHPzTdplFbJWrQVRStvF0sRA4AnPBhqfWysW_PUQqmNPJhZx58D11dm5FJfD_FIfI11ypYeHwEQ73zfK_oijho4n_hzk6ULKsd0-ykIMppNeyhqd8bEmm43zR0HOrM-i1FFvHp_Ng4r2TNrSzSiKEsqMHEE1pXQTRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83a5244f7f.mp4?token=BYBkBojG8JtrjWupmNG6keOfWnFRLJYEq0tJcuDv_uuxLbU5z3SsXzKqkodU6ImiYwKitpHOw35LbHk8m2uc2tlhRNLezTadcGbo_ahulD543hiT1o_tIhGj3uh8MQSiOwsHmrVXNSyTyMVwJgJGtJWf-uFZ3uLsXoG03g9zR4ZeGjPEwg9MhHPzTdplFbJWrQVRStvF0sRA4AnPBhqfWysW_PUQqmNPJhZx58D11dm5FJfD_FIfI11ypYeHwEQ73zfK_oijho4n_hzk6ULKsd0-ykIMppNeyhqd8bEmm43zR0HOrM-i1FFvHp_Ng4r2TNrSzSiKEsqMHEE1pXQTRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش امید عالیشاه به فحاشی ناموسی خداداد: وقتی گوش دادم. دچار شرم نیابتی شدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30043" target="_blank">📅 10:39 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tjk3j3LnyDQWfF3WeLq5oL4_dagMMeTa21OVRhJ7x_RZnwTBMafYrRXM9NAnatPDUmWejaGAi5dJaZllpYReN_E4RldslXWKcZ-irgJoAabYZHvtui7nrGQEO_jdwa9DPcf68MzTW7_Q6F3mFza3PdJ-i-9JKLmW188WqNuP7Aqnj6L0Ii3BnZGjguKXiCSWpoQu64FskOljKJVea85EYZz_bpsHemVoPHap_SCOCh42XkQmPnyaA9M1egeMtyeF05AF3cQV-51jdC38WQzH4IJ2RYjXOg9xRA6Lt_wwniD1vqru7bS92TmtQhlZ7IXko-P0iUh2GZwv8VEQmH07kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇲🇦
🇪🇸
🇧🇷
ادعای نشریه NC اسپانیا:
باشگاه رئال مادرید بار دیگر مذاکرات رسمی خود را برای جذب عبدالله اوزان ستاره 17 ساله مراکشی برای رقابت با وینیسیوس جونیور ستاره کهکشانی آغاز کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30042" target="_blank">📅 10:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYtUkCzguwwRyFzGWsgCCcF2Y8vQepH3kY1qFj1jlc9a2DhPjnPFcuewuV2owioBRgFNX4jyzxC2vY4Ia_be1lHqZCyk7acm1JMQLuq2XjkK-tL0y50URpz-ld969FAKedIHrzadwkzCC6JUVXJoM79qhY0m1YyTwU3AlGmJNKZsWMI5gWKrLn_0mWPUoKr-5V7qKQubH-idKQAZYfDlhcUWXo0NxQ-7oSk8DTOBC9g_Fu0T6vG_y2p-TivEssNDfIquSDiRa9t0odcCP1HUwN83lh_EbXP6Z_5Rf0Yyvuh2XvRGQZL_GCjr1cC8ZsY-F5NtX4lkQe6xbBt6YRdXUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
یکی از مدیران باشگاه استقلال: محمد خلیفه و حبیب‌ فرعباسی دو‌گلر تیم‌استقلال هستند و فعلا هیج برنامه ای برای جذب گلر جدید نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30041" target="_blank">📅 09:46 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz-M9sy6gZFIWKTJNnTYlloMlS1pwmVa2NP-Cw4u8JX9w1QyiyKcEyFHhcrchdvfWaqDn_BdGA5VPyBdXVMHaMSiviL1Szrw0gVzBqZLH-ZUU_A0ARfUYtcjrz36ItKxgK3NawU2WM6rShiGOHBBj567ohHeEjOP6NOpNJOUspI5Ec32f_38zOhhZWQy3-kJFUL1Riu7AV5xodkDfCETGckt0t9yI7WWK7ron8mpQL-VfR4_OTEmEeYfMqmF8xOKyVFU6MYHEDSjLMPJCgRDK7CnVpXqn62mYwmm-lZVc205EJIHCKtXehBTvZlm2QUngZWHbKF_dAEh2lO0lILgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ محمد قربانی ستاره‌الوحده امارات امشب دربین دوستان نزدیک‌خود گفته از وضعیتم در الوحده راضی‌نیستم و نیم فصل یا با پرسپولیس قرار داد میبندم یا استقلال؛ هرکدومشون‌پول رضایت نامه ام رو پرداخت کنید مشکلی برای عقد قرارداد ندارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/30040" target="_blank">📅 09:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/135cc26708.mp4?token=XBLW-j165e2T0Tnb8nACZogD2MoEAkhnRkGLIFWeviDoGSL01nNzw-TufJaTk4eo8Ad1y19iRMN4eVwl1agQpJ6w-F4DZse-tXdgagmA8MPI1XkZEuaf-t64fKVDfM3kRh_cyXVODgCR5r4wyu1Hakpa6vKmXf_WWcp3R_gNDCohZK3OaV9EDUAPTwwa77Jl0Xvnb5XS5s-41b5f-b97jvIwA34hGeHga5iXis8t4c3E-JuCJsy2IX0_xD1bEK0fDwIQNIUSKSMsgO-qJxz1NWW4Pxb8nlfE5O_Ujdszj7JGbbQu9wzQz3kGiGMWiKblYv5fxd_qoSQX08FJ4N86mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/135cc26708.mp4?token=XBLW-j165e2T0Tnb8nACZogD2MoEAkhnRkGLIFWeviDoGSL01nNzw-TufJaTk4eo8Ad1y19iRMN4eVwl1agQpJ6w-F4DZse-tXdgagmA8MPI1XkZEuaf-t64fKVDfM3kRh_cyXVODgCR5r4wyu1Hakpa6vKmXf_WWcp3R_gNDCohZK3OaV9EDUAPTwwa77Jl0Xvnb5XS5s-41b5f-b97jvIwA34hGeHga5iXis8t4c3E-JuCJsy2IX0_xD1bEK0fDwIQNIUSKSMsgO-qJxz1NWW4Pxb8nlfE5O_Ujdszj7JGbbQu9wzQz3kGiGMWiKblYv5fxd_qoSQX08FJ4N86mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌سنگین مهران مدیری درقسمت سوم مرد سه هزار چهره درباره فرهنگ سازی تو جاده چالوس!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30039" target="_blank">📅 09:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30037">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=AVOGUprUzEZ63XHIkPt7GlcOtO5RKKBauYVGFogQ1WpypaNXVT_D3qw5K00L6Y5hpWgwhz51sZkH62ThDLEJFtUrVTMA_ERCq_oYkWtYqwTnA6fb9OLpfC2hYAoJ3uzZxY2kRObehrdYvxkmJZs5mK4vIWxz7YZYfr5KiUnFcC_btuM8HaQTqMavbINIRutbfEguAndkrrvXjIzBvmhaQy88ku7RjdpZfA9t0XuoVkFg6XnyLBseH2LbVF6557jztzUySboX7tcWH1CuF0LJ9uCL3bomzhv__9Hdcvstz5r1YkIc-WrsHXQTEMr1CDOmtHUQri1gEtvgpxyHFh92qJFO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ac719facd.mp4?token=AVOGUprUzEZ63XHIkPt7GlcOtO5RKKBauYVGFogQ1WpypaNXVT_D3qw5K00L6Y5hpWgwhz51sZkH62ThDLEJFtUrVTMA_ERCq_oYkWtYqwTnA6fb9OLpfC2hYAoJ3uzZxY2kRObehrdYvxkmJZs5mK4vIWxz7YZYfr5KiUnFcC_btuM8HaQTqMavbINIRutbfEguAndkrrvXjIzBvmhaQy88ku7RjdpZfA9t0XuoVkFg6XnyLBseH2LbVF6557jztzUySboX7tcWH1CuF0LJ9uCL3bomzhv__9Hdcvstz5r1YkIc-WrsHXQTEMr1CDOmtHUQri1gEtvgpxyHFh92qJFO10GOZ6C6xyChNtRJKxv2si5ypG8d46WiVqRTbNNOcjRsCt0E0gl0UfhtcOrhSkg4U-oOtSYrYDnEyxew4or6eC8qtYLMURYzsWCLV5kGpd08X0QzvL2NJfXkcvGdHSjZdbZsdTL354Anqz0S2-lQkvOlamD53DmKLu5bWZIPJowRV85Te3GeZEtDYQnU7trJcKuzQup0eLYL-D02yTNkdSR3Px7lWKjMpMjMO9j67RxhcwMmlRDneMB2CUUeF_MQMrGB0_wnLD-Bc98y0spQ0FaISZLAEUn_NmDRVXdqDD74-lKVn-FOVqKrq2VX02SHu33bd6-KDk8maIt9Zu4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌مهدی‌مهدوی‌کیااسطوره فوتبال ایران و باشگاه‌پرسپولیس‌درباره‌پیشنهاد 2.5 میلیون دلاری باشگاه چینی داریان که به آن پاسخ منفی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/30037" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30036">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KHchxEcaOWsRjc7A9z35iEozyEGGlFNplZsNO7WrRC8Zy7vNBrZh1SKYgkfpJVgf3VbImc8ykfpjLg8a3DHegXMNG9t8fRVJh6Glq0RbsHa-hMBs2BXgONl-rjCnQ0kVG-aflLoma5TW9gGolsoKPliF1ueIL3fFPLxaV5TIZiqgXqr3SU5EES_XrU73e8zL8a-ox4RWBZau_oo7M9TCR2f0VLFfd43duwi9_Vd-gSMeigYxvANeBqZRGTMd5-rF2pWqZHTFzL6KZ5RDuf4SnL5tzHDD9805r7AVLyYHtNTRbdMXqZhnO95sW0YW9-NhbG_IN2N2qujEG32WHQBeZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ دوئل‌تمام‌عیار یاران دیبالا vs لائوتارو مارتینز برای صدرنشینی در رقابت های سری‌آ و مصاف تماشایی شاگردان فلیک با سویا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/30036" target="_blank">📅 00:57 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NCm6sJWMY0pH7IcoNArTiCrIk1u-lVCDPUZjZ7PoL_wkJaavoXYZ8gk9pcTeCYXt-wPks1OMynfLOiuOJAyPjZWDFWhnKHmPmRXssj_AXM48eGsJzwkZCOWJffhl8LCQSyA6ZeMdw_NbJXDTpgf7qsajEzhplOqC71jKpslBccHNp3q62EwhtVB94WJUzOLFVIOgeLCY-rmSu_se--CD2pmN-1Hg7joxGKq05c_993ZW0Ops1ppd4oYlnORB-sWh0e_l39URokd7eD1raKZyU549u8XZ3MYkXBhi3QtG578XDsbp0KpSr7mRxMDM88C5gxvs-NNcmJdrod88Q9iM0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از نمایش ناامیدکننده یاران ژابی تاجشنواره گل‌مونیخی‌ها درشب هتریک اولیسه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30035" target="_blank">📅 00:56 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‼️
#تکمیلی؛بهداد اقبالی مالک‌جدیدتیم چلسی: از کادرفنی‌حمایت‌کامل‌میکنم و هرچقدر نیاز باشد برای این‌تیم هزینه‌خواهم کرد تا به قهرمانی لیگ جزیره و لیگ‌ قهرمانان‌ برسیم. به هواداران قول میدم چلسی رو درآینده‌نزدیک به جایگاه‌اصلی‌اش برمیگردونیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/30033" target="_blank">📅 00:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opXJo4Qlc-GbGQnCHBdxmnBdA4mHnrou0WyROjan-M6w__nRC6jwOsO7OQ41uRbOC1q2nsM1Q_bGRxUfuFO6MIHIGDAq7Z3HwwuwQM9-g3kZB5Lq1Kr-Ul4cduIYPGUpwBi7tosZidfMRrpx7mM_T9kwJc0PjXDrG5F0ZAA0idpfThTmucxinQq78g22N2d68DE_lDSPOmTUd-fO3dhzwyGnOenFTyOV8KXzL1G3JE2vW3M9YETCTQkktCuZwhXxdK8ZXU6Msx5pvs23mzM4bkqMfhnNvcSZowmpPxzufi1bDxk-Vz5MjxKwT05Xsuy26f1J6iWzYLw2iRz3q_AC0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
لامین یامال: دوس دارم در چمپیونز لیگ به رئال مادرید بخوریم. برای‌الکلاسیکو 3 آبان بی نهایت انگیزه داریم و میخوایم یه نتیجه تاریخی رقم بزنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/30032" target="_blank">📅 00:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بایرن‌مونیخ‌امشب درهفته‌سوم بوندسلیگا با گلزنی هری‌کین فوق‌ستاره انگلیسی‌خود دو بر یک از سد الفرسبرگ گذشت. حالانکته‌جذاب‌این که در 100 پیروزی اخیر باواریایی‌ها در تمام مسابقات هری کین تو 97 مسابقه تاثیر گذاری مستقیم" گل یا پاس گل" داشته. امسال خیلی…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30031" target="_blank">📅 00:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30030">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFoQQryFenoDDbIHGi3qiDzHxybJ2ID2cvPskZBWiRMCHnz6j-7qxWSpQX3YVsvK4G1zzvvcq3GYKMa2GvqPL5ElWiVyehkzgORmjWEjrGxVq1PBl4pz1jYCV-VhNBCdRDT2C1iHRlCzj2yiVOfCL38FzjnTetZ69cUYXZcpL3aaFL_1BotZcd8l2i7wYZFkldNFlbNyoKHjX-h7-gNe2V98ffKcqMta4epNsE3CjIqX69fGDyY127UEv19GpZ-YNdtvh0gCulB8B5zhLIVMUaA02nl4h7lbfCKqtBLqM75wgvBYu-vav6gLdFf7Wu0w3QVZM8BX_n4khsUGWhQ9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سهم‌یک‌امتیازی‌یحیی و علیمنصور از هفته هشتم لیگ‌برتر عراق: دهوک‌مقابل المینا به تساوی یک بر یک رسید. الطلبه هم با الجولان 2ـ2 مساوی کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/30030" target="_blank">📅 23:57 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30029">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX2FvlPZlzhOazCa52iIp9hTNnMScN54VzzGhBoIFlXUN7j3eI-tVT1tZUwr3VEt0ErHPjO4OCoY6S7iqzZuKoYKOD_yHF3SYcIVAq8esNif893sSd-lY5y2RvxrxLPbIOJFKwztiUHo9Ay4w15WgAk2mCfldBIXosU-HycvQlNDtUyuH4kLq1GXUcJ5JizyzkG7G9dWZUfg-GktheU1vHrqljNseO69O4_nxH5RF3CET7QWaT7i9zQ_hbAxzMXcARjnmUUex8G1T7lccVV7JImIAGHgDy4dqrPqWPSw3aDNVWtpZeovOeK94HAuqWD9urFhAMXhquITCnhe6rONdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نتایج دیدارهای هفته اول لیگ برتر بانوان؛ استارت پر قدرت استقلال، پرسپولیس و سپاهان با برتری قاطع مقابل حریفان در ایستگاه اول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30029" target="_blank">📅 23:45 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30028">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=CicKp_eee807zqRjFMTp0dweUbczir0LfWYEhAtZwoiZqA0W2x4Ts1htafrhu1NSvqn56y8Fc-G5EEnPn-z3Geswlo0pyytkLBHN4Qvux6pI1p_G_7YxK0nC0XqbSjJ9U8OJbVPtXmfZCALbxulUiv9vn2OH-mkZNO0hQzZSGPM9Z3bF7ocIlGkboXjIvRyYE14GNl_-1wHFB8C8_y3-998VcpD7J9MI2cc-GegBjbAkywJqAcSCiEiiXlWGSKQzKelt9yVzhr7WSnEQtyvDqlpp_AOrI5lf4caEj4LjYIkBjyXlFJ6t6buxMAo96DH_i9boHAn539udBc2VHHbSmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5df38636e.mp4?token=CicKp_eee807zqRjFMTp0dweUbczir0LfWYEhAtZwoiZqA0W2x4Ts1htafrhu1NSvqn56y8Fc-G5EEnPn-z3Geswlo0pyytkLBHN4Qvux6pI1p_G_7YxK0nC0XqbSjJ9U8OJbVPtXmfZCALbxulUiv9vn2OH-mkZNO0hQzZSGPM9Z3bF7ocIlGkboXjIvRyYE14GNl_-1wHFB8C8_y3-998VcpD7J9MI2cc-GegBjbAkywJqAcSCiEiiXlWGSKQzKelt9yVzhr7WSnEQtyvDqlpp_AOrI5lf4caEj4LjYIkBjyXlFJ6t6buxMAo96DH_i9boHAn539udBc2VHHbSmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نحوه وام‌ گرفتن درایران به‌اینصورته که میبینید؛ تیکه‌سنگین مهران مدیری به وام های کلان بعضی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/30028" target="_blank">📅 23:17 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30027">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=WtFducdozd4BMzZezV1bQvvE6nTSb2cNXaMVPaieSMGA3dS3zwjoSeflXIrDhNfT13cH4DzOYnlqJqzWSNLiNYnBQu7LimYdgr4OokeGsbE4sGBRt1RJ1qDzATz1i087GlWv2cmRpkbcDDYa8Rkds4PB-iduc3GmHoPT9RLROnMs0lS3bI3r2ZmzY4pmByXMobHetiVxSRMOlsJGdktgjTECSmvW8OeCSM-IOMBFWa4HciENYe2ycMzv71BHSdG0GX2v0KuQXnfXzjWMewTOlV5Oxm9V6yDBBWiSkYikMBcPFH8UPLeWEISIekZnwuVQoayrWY5XqKPAVsrmUudX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4323ee05c8.mp4?token=WtFducdozd4BMzZezV1bQvvE6nTSb2cNXaMVPaieSMGA3dS3zwjoSeflXIrDhNfT13cH4DzOYnlqJqzWSNLiNYnBQu7LimYdgr4OokeGsbE4sGBRt1RJ1qDzATz1i087GlWv2cmRpkbcDDYa8Rkds4PB-iduc3GmHoPT9RLROnMs0lS3bI3r2ZmzY4pmByXMobHetiVxSRMOlsJGdktgjTECSmvW8OeCSM-IOMBFWa4HciENYe2ycMzv71BHSdG0GX2v0KuQXnfXzjWMewTOlV5Oxm9V6yDBBWiSkYikMBcPFH8UPLeWEISIekZnwuVQoayrWY5XqKPAVsrmUudX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ویدیو باشگاه ماخاچ قلعه روسیه از شاهکار تماشایی محمدجواد حسین‌نژاد دربازی شب گذشته؛ تکنیک‌ و آگاهی محیطی حسین‌ نژاد خیلی بالاست سریعا هم تیمی‌اش رو در موقعیت گل قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30027" target="_blank">📅 23:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30026">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAR2fjnrtnP6LEFjFsuXHh78vk2T4vDBQrAAkfLkhJE4-ksM6mKGQ8KnaPODOqp0HFjHSDkj_G1pFM72EjbUnAxGMTqL5KT8cwBCzdIYemKrMrYVOg25ykpuRSHuJPuuKzrkaCMqmJttG53eG8CChFbaynRD-bhvhrDyF4QVk4xwNb3JgczbZTIelszZ2cddiBp__er6ebFzCRGi3xGWt5H0rDFW_fUyKdjEsvSaTO2hop2cos7ki07DWttX9nOOO7T0D-hSpaW01LY_UJMrNUqlEfHPuLZCHpgC81k0Ae-xrDVQYWGsUys6AFxYCxsTasr77s3xDQ7-E2EX7pbmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ بااعلام مدیربرنامه‌های داکنز نازون؛ بازگشت‌این‌بازیکن 31 ساله به جمع آبی پوشان منتفی شده و این بازیکن به مدیریت باشگاه استقلال اعلام کرده علاقه‌ای به بازگشت به لیگ برتر ایران ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30026" target="_blank">📅 22:28 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30025">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJDEILAfZgvESf_hhcKwa8Os6mg5noWYR_SVsuY3CdyleyvETWQCpvdcQ_LHoQILToBoFsIYtsMrrwhvIDg_lNdcYwc5nQIm17ujk5KPDIqcblTQ8xops0Vuepy4fVRQ6IWiU93ezLK3QepI8NlAkmkx3IHVcKoRHkCjfhEZ7V9YghpQpHDDWjU0FPG1fFyAmRLyQ4f7hV7Qa_2T3SrUdIIRn7GVOnfIsngdf4s9yhYUNHP2qHrENWnV-p0wNOFqUQ6OQAq6NOregrJCTM-xn37u2btvPAPwd80j_lTPMRi_POSgb4SY0__aPcLVxYH7sqJoZHOWRFhIDY6XjrsTbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه‌اتلتیک: جی‌جی گابریل ستاره 15 ساله منچستریونایتد تصمیم‌نهایی‌خود را گرفته و بزودی با عقدقراردادی 10 ساله به رئال‌مادرید خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/30025" target="_blank">📅 22:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30024">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccOthH2alk_LlwTu-TAOANu4WkPK1-E0PkF7qCNx5Gl9S8WCEwjis802D9eF471gSns53NDT7UwEI8wQq2rSdu-SyXgkxWwqk6BkmgS98X3Rth5mZLnraOYIv3ZjZcbv2pWeQB0EDGcEtkcIPMHvlS4bv8EyTZ0bs0dv2WurSyDOolTMRmcKqYqvRTkQd5GhsZvxnsr02NFR2MaEhno0MSGoZFlbQhzk1jHV4vrb7xqEfHS_Zy4XfE4R7OASzUFpE9ntbrAVCH8bIOL_mP3jMiZXKRY_IN31Lp9q9FdZDxvGIlwCKfbJAzDKEA2m2U35NlGNAmrnugEwaEnmqAEkuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نگاهی‌بیندازیم‌ به‌ نتایج مرگبار حریفان بارسلونا مقابل تیم‌خوفناک‌هانسی‌فلیک؛ شش مسابقه، 34 گل زده خیلی‌خطریه‌خیلی! 38 روز دیگه الکلاسیکوعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/30024" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30023">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DytIKUsi1HxOmhL926fJLbF087aqXjZw0rU2ZIuUWVs5urdJeSZoBMSnjTqLi7CmesBuu45Vz5B5pX_UMHSay9axJ0CHk0qH92vi6NXNIaGKw77pIXBlGjefXRXRKrMpADSe99buMMDZTcWAKLJOFBdkOG0DzC_YYoKDxK6PcFHwT7hvzTembtAu9kTft_-QIBxSQDbgSdA9SKtv_dOb2GH2n4fKIpzXgduFx_FxMONo6r9dFZVe9Frixb_uzdX0_xX1MRcfqG9Thbpmdmid3ksW_NExaFgXIR4bqoRDsXwFEy4TagWyEQJ8Fu1xStUGfuPREWl2Jr2BzgY-_kfYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی تیم ملی پرتغال؛ کریس رونالدو اسطوره پرتغالی 41 ساله تاریخ رو برای فیفادی پیش رو به تیم ملی دعوت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30023" target="_blank">📅 21:53 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-30021">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivwWjmd7ecqTfB6Fvl-_MjxIY0ZYAkx22uPNkPQl_-PSF-m72lpEclwEhVoTAujFRP8GHi6YLh2G8-RdOspkTCubLEIcxep5-WVYanPC6_rtHf60Wjnmlep5pX25AdL2lv6okX4FK7yfjKOtm6vBtgsv_7P7jAGcKVED6C7_9tYYNBBKcQTUNAg2f95IHDAhw8lAnZOpy6V8YY63bL3JbNk7QUNBqZ23p9ob0E8BpFCytwAFhQ0UqX97iAqtfzXU_Tgv7mhOIcmnC5TL7IB1WtT48nHFmI08zGUI-fsavY898LA_FUWPflmWiv-8Xm8dc7L4h_DboNyGXTgSpJsQVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
دوتیم بارسلونا
🆚
رئال مادرید روز یکشنبه سوم آبان ماه ساعت 23:30 در ورزشگاه نیوکمپ اولین الکلاسیکو این فصل رو برگزار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/30021" target="_blank">📅 20:42 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
