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
<img src="https://cdn4.telesco.pe/file/stYXW7QfUQm9UEG8aqJcsUdVyDrsBGPAawqztMK9ybFDHGd6XZ5lJmrgv184Rr2HY_3oDNoLWB3r8e4WxlVQ3x5nIsR4NZ640T9VeC7lFfOLJ6GTOifdkzKJ3mOzjzYPg_dMjHw6hp3TcGA8Cl4rbD4-iPMiTWr9zBV2hVDcxtIuCK3iMNuw6fdF6fU3tZi_SWlz6qSpMaX5C2KFUrTL_pi77jX9OONNq3Um5cnosr53wIoF9iwHzLzONwIHzJNuhLOi8aD_r37FjEUnJ4uXfHFTNObZ7B6rMeZ9IMJshOQ5171NO5HifZCFAGRAViL0qavOU_4Qnwzb-7rgmnNZ-Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 20:39:24</div>
<hr>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=ZXtXPfTibwVxdci2nLS3uZXCcrKc6hPc17sLXNVwobukXIBdlYcCXDwMCtGQlXlQ8pW_sKMZYcem0Jwv7T7sUj16p4pN1_CP4FOjelw5CU_v2l_0P5LTzCcjB8TilVWFzkO1Rz2vviSLli7L1yHGPWPn1eElrurGSSnU5ZWWa3BjRoWwoK0KADpSRzGWN9hcu_Bq5u1z_vtYwYBAo43k7vNy_RVOC05QUj5vWM2eB6cxLEHw8_Ay45hW0nShiItZ8t51QUHtv1aicJuL-N2eHWiZHhGBXWIIFlaOx1jYDbn-6mNbyqxOrAzx5ppPaGy_7JPnP8hioaiT_syiZjqtLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=ZXtXPfTibwVxdci2nLS3uZXCcrKc6hPc17sLXNVwobukXIBdlYcCXDwMCtGQlXlQ8pW_sKMZYcem0Jwv7T7sUj16p4pN1_CP4FOjelw5CU_v2l_0P5LTzCcjB8TilVWFzkO1Rz2vviSLli7L1yHGPWPn1eElrurGSSnU5ZWWa3BjRoWwoK0KADpSRzGWN9hcu_Bq5u1z_vtYwYBAo43k7vNy_RVOC05QUj5vWM2eB6cxLEHw8_Ay45hW0nShiItZ8t51QUHtv1aicJuL-N2eHWiZHhGBXWIIFlaOx1jYDbn-6mNbyqxOrAzx5ppPaGy_7JPnP8hioaiT_syiZjqtLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyaxen8k8EL6XqQG9f0XvZYSurP9g-0TQBaYv1Lz474tTCveyKNP4hsEvlOJth1t33u0k4GDpogbu-i1vJoVJtogTxz83Odo-36hS0BWv3U84CpUv9AUrfhJniR_AGe64VDiPHSSXnEQH9IAWorb84tjreS7fqrnyIM6UvEjkx-y7ZLKO0vzVJFbPs3qZTCytUxz78TsXMbJKGxiYanXS9ydSJMegWnE1mxbOIKWFEnF-5O0KGYLNmp263hNW-69OcVOkqE84ouToZ8-4V5tH8EbgmgDizppvEl5otVj2LEByWADPABttubcw9DRDdyG7TnQYPp8AcCp1kCTLgrfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mmavFW0IOfZSZGZqQyPTKVfERfLc6T0U2vEyVlEH_mrqwT4m6C7t_F0TPBC7rVnoXJI2SIDI0aARlZH-WMLvGeDPTlFTMZFFrdm9APeI7ydAFAHW0pa4mbg9eLHKr3h8KBEUOelll6BHNustRZtzuASajyDSBj3bcW8XwdF0IuRalOEJt4R0KqTMlIy_KzfZ1GgLlzz4YiT178UnWuXbLDWCqwjzVs0SVfwVooBO-PKdpGPviYtTHK7_AULeoQ62nzECPAlcXCKBl33MZ-UOk33bShytcNfIwINnO92KvEKgHYsifAliAM6w3FcRiBp2QxNRwiJV9w_vJXeZ5x3BSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bU90QwJFDx6x1iNxJXp0gochdC8SiyeYEWRPCMcs-Km3TYUR_-CosG3lQixub7pX0nXgB5w3P3Q0dg3JOMdHtpqRzkVLnQtYipVOJoArf6Tg1Lokv4VImk7mgbc0cQIyfhetzeLSsrkJGDf260q6YoRuBQAcRc_F6b1Fmj2MuiQiMPobXYdYIfUceRDL2LwpBTyhScVc6zPjwmd3N2263hguxduMaaAvgzdt_Fhaocjey-DJKQfkVC-OKf2fJ00Q8-3LFheAm4QUCKZBHRwkty_JK0fnSg-_3J7x2AMLDBohMrXVLINbCsyyGQaLkRnKVFgcrHX7rewDdDolfCg7FQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=OgtO2GUp-cGG85MYDaakt_WORQxdueIZpkSwm0CR3C0OcRad29UvD2tOayVBBKzT0Z7wDtlKvL1TBNfvs-wSmPM6MnoKQpoW3jrs-aYm1ZcglrXDRn9czoYUU0jqeL6vPdq_tekARuFOw4kKim-bemF2MJWj-2MP2SiLvt_npQ_ejB_frifD40kOs85KWKq6_dMTU0V3-pZggpUIy8jgXgspzgxUvRwuRAxhqp2yWhc64K9afMgxlno6FQ327TKxJk6mEz7NBRH0VZhVhPFBx6JBYUUGHU8YSLBKOovtH6AwLMvxr8NgxzTKMJMVI3vwgICTXCDxUotaf3veExSADTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=OgtO2GUp-cGG85MYDaakt_WORQxdueIZpkSwm0CR3C0OcRad29UvD2tOayVBBKzT0Z7wDtlKvL1TBNfvs-wSmPM6MnoKQpoW3jrs-aYm1ZcglrXDRn9czoYUU0jqeL6vPdq_tekARuFOw4kKim-bemF2MJWj-2MP2SiLvt_npQ_ejB_frifD40kOs85KWKq6_dMTU0V3-pZggpUIy8jgXgspzgxUvRwuRAxhqp2yWhc64K9afMgxlno6FQ327TKxJk6mEz7NBRH0VZhVhPFBx6JBYUUGHU8YSLBKOovtH6AwLMvxr8NgxzTKMJMVI3vwgICTXCDxUotaf3veExSADTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=btih-XZyLY0TcioZX7v2vnzbow43KCIIaUJUelO3rifYmz9KrzpcTbhDtqXreJOiSkGPpKfloabPgPIFUOL0jO8JylzjtUJ4yYLswJ_rY-ynWziG0yvLwwRq0unzmhcUxkuM_oFrVUgANjtz9_NFNG2YODVxhujFz4wqmdEFtlg6r0HtKwd91LR5iXkEL_nd77gQRjJYOLrYcJKjWzHCLTrtmx445BQAyLv2R8nLjr0M3OKSYddyCV51zd0PcOCMdzY2Xh6rGCDSh2QcBDBoIfmEGm1g3Gp74zIDD4gBWkuvryiK36_bVAcWSJGwfRXHSV7nOnKCCX7yQRAmy5SjJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=btih-XZyLY0TcioZX7v2vnzbow43KCIIaUJUelO3rifYmz9KrzpcTbhDtqXreJOiSkGPpKfloabPgPIFUOL0jO8JylzjtUJ4yYLswJ_rY-ynWziG0yvLwwRq0unzmhcUxkuM_oFrVUgANjtz9_NFNG2YODVxhujFz4wqmdEFtlg6r0HtKwd91LR5iXkEL_nd77gQRjJYOLrYcJKjWzHCLTrtmx445BQAyLv2R8nLjr0M3OKSYddyCV51zd0PcOCMdzY2Xh6rGCDSh2QcBDBoIfmEGm1g3Gp74zIDD4gBWkuvryiK36_bVAcWSJGwfRXHSV7nOnKCCX7yQRAmy5SjJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD6eBFiRQ94BoEAXNqoK0YVJM0vaWDrRuuntHikuKMxpVm4-eOkOhdC20Fs52R1t59cyQDMZCnQytihtj6j3B5Pu0b9qkxU9uDFBtI2MyX0Je8cfqHraDiAcgeG8Y-MYZ-RZ3rlDk_CI3xi5jbel6oxL2OBBr3kKRC81kYjrPL2i7X_0ntalvJpctCukbLz_IdMKWvOOQVcP0s2hAJW54Mx-fcFL4x6qN_HAmwH48J2shF-5yDYnk6ah1OfueqO1IglCUFr0k_fdvyxSJ9s6jQlNZwxV_gkap9EjP2fqh7avAldaKwITOPdwuUR5V70oxaGnv17l475cwAzRzHj2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OnjHkBgTYC2q_qrlPzUlssGvjQmzJ8TrNYgjk6FRkqWSWOT402zwg_UxG0kG3eIKfVKDYIgw80HIxyBY6bdZVaUt5jNiofB-xuWsbENToRAL4FiTR57M9fuLIaJI41Do75GrFALAkl905x574bWqOkYQV7pK7DkHDsL36nCofty1QgpFLfHaPN-0SsCNDwhRVDutaGJvS5Jppk3smaifGXE5xSjzmMQS_OwSrt6VH7lF5_iqV-hVFuK6bm71IHNInpsiIW-cghCgFTIKTmmRzRrvi-Za-yO9sRC6ZHp5KziNtSmVhvlMoDUuDp2Cxja7ulI_x4saE7RVVBINztFJVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=gYLyTph6p9tD5iaPo8ECSqyLxedCZqUhyhuDd0BR4BXODVUKQKF0gv-eKmz3XQDL-KWxet6eddZFAZFDsgDmQREWq-CKt-ATd4UXi_aYKYppV9t3bT0rF-hxR5Clk4S22eF9YEZBHHuHPvskG-1j5mJkP6jvvC3ucl7FQYL7K5-AlGk9Cbp5-Qpop8xZrKpl6IXrX84qby7GpixqHu4tJC_wDNOe_cvqrpKWLim8GhQpGH8Acvfb1uH3SNtQcg_VcVLL2CkpucriDSdIuvEQ9izrc2L5MEqHCqcjzYC7twQzJTKjVFDEb3WTIQO_R5vMBdK18DDsBO1x0N0g1g3YpS3iHke7f4ti0uGwhozi81WfDQFq9_8lLmSSkT5WzLjjx7bm3pm32vZlE71mvWYweAvI2kPgVqTj82l3k7bNqr2rrFGZNrAuHPJQMpZDmpXUgI901TuTqIObwlPnI7qo6wOsk4ihJyUom3_SmVokpFthcpmVz5lec87xJQmanwNMLJVTxMxMDN8AdbN5SVP4-4gnnevgBcuUM8-v_m0WKLciFJC0kqRDxcuw6SZjE46BZrUoJh5NnYSKY1zHjWxIedgaRoMbwWy5dfF9nWJ2mAh41Y7c4M0u3jTVNMLXae4XMEBsA_KDMl19Dq1__Fr6t8D9ZWLKNZ4-l6sqZQAnVKk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=gYLyTph6p9tD5iaPo8ECSqyLxedCZqUhyhuDd0BR4BXODVUKQKF0gv-eKmz3XQDL-KWxet6eddZFAZFDsgDmQREWq-CKt-ATd4UXi_aYKYppV9t3bT0rF-hxR5Clk4S22eF9YEZBHHuHPvskG-1j5mJkP6jvvC3ucl7FQYL7K5-AlGk9Cbp5-Qpop8xZrKpl6IXrX84qby7GpixqHu4tJC_wDNOe_cvqrpKWLim8GhQpGH8Acvfb1uH3SNtQcg_VcVLL2CkpucriDSdIuvEQ9izrc2L5MEqHCqcjzYC7twQzJTKjVFDEb3WTIQO_R5vMBdK18DDsBO1x0N0g1g3YpS3iHke7f4ti0uGwhozi81WfDQFq9_8lLmSSkT5WzLjjx7bm3pm32vZlE71mvWYweAvI2kPgVqTj82l3k7bNqr2rrFGZNrAuHPJQMpZDmpXUgI901TuTqIObwlPnI7qo6wOsk4ihJyUom3_SmVokpFthcpmVz5lec87xJQmanwNMLJVTxMxMDN8AdbN5SVP4-4gnnevgBcuUM8-v_m0WKLciFJC0kqRDxcuw6SZjE46BZrUoJh5NnYSKY1zHjWxIedgaRoMbwWy5dfF9nWJ2mAh41Y7c4M0u3jTVNMLXae4XMEBsA_KDMl19Dq1__Fr6t8D9ZWLKNZ4-l6sqZQAnVKk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx2hQ1bhS_mvHjTN8wezEje-l3IXDbK42p0HxFaXoLLfU-NykP6LVm2I4ZBNtt9_C5ajKnKzeAW4Z3NQYIvkhntsonggL2B02q-CGFQyjtJQFX4Wm5rBXJHYNu_X0_FfvPztuWxFZBndqiiOuf-rq3U4xHzzi_FOUMkkH-7Kz6T2VzH4jjxlss0EsYJxQtAPCiev5VirJp-bPx10G9_whAgnZlt7V2AsSqx18xQAnudB7_95HAPi6cRbWuXSrsEa_p0mB_AWzXnLObmglVBw1pNTQUSxDhbF5DFRdolElE-xSCvUa9WMCrQPLFBZ3xCPqAfPTlc6ktrVmXiVMBLJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohEQWDvsg38hH6oWCXjEIPIBAzykJfcCuwFK_lKudYd7MqJ5u97nybnmZx3SBE4O1zPt0j0hVz7xB7zyfWsdZfyDFSZ_8eOiyXWndl182HqB-sxrD3nJ0xJnhk_DhmGmWBZuHEfp3oEmEIo2HOO73T8Dkekpmm6t_VkhOfV3uaXidyH0juDGO2cxZqRQlSIbfEFnUU0HEH4NsEIe2fyxc_wo88zDJKbDihWhkkhIHui0qBQNcx3TzT4uaGxVH-73lEY7-FCfPLGCK-iR_bk2BKtqkbQjWQTQYW2mawcPIpYyOb_7ZyYlSgxQHvNXaESnn_AXI-4pI9C8vnY4gDsBXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KlgE5djW0J58-8rwQ_VDhFHr9Pl5uZBjTTRLLJu58pAhuYjKSmlRb1lSKkFvzkXqar8FSe3_H-qyeOdkNc5cMh4nKwEy3SBbPGDgVwZQOVfANAJ-QXRkTVrCslg3SW0KKyj58UhhRfJklSvTaMkGtA-EElgAcUDjB_DHE5F7V5QgAtcjhrAcfa0Cze4a8klt6tRs6p4YHdPtdSabFFJjCmoQtWExx-yMQEC63hT80PJlhYDw8JMuI0tsRaaEQK3aahM7EQe-QxOm2pMQKO2Z9f5BHZV1QUjKZ13amll27LjNgixOAGxX6QOAm-uedS5h_xXRehsLA8n9xiSITe8rSg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRnGlezpaUSP-FlEhG72pW6WApo-v2oEUBd58es8eJ4YXbCgJbaUlqJVJySCS6cEqstNSGEaorejMPQStzqhri2vK9mfih-K_0U53xuYPyDt8roR5GhCDCNdi3ob15pmYC8lkFH1Q5CI2SDdrmcu9WigFhr3GbAihVEc5GGmQdOZhqenbiDOYp-2AmfI6HczS8LwUavbUIpGUNvs981OPPLXhL6gDAJ-fSmb13ZWZg862uRxMtvfIc9Zvw4Qva8jsIhk6uB-Dh2SGeYDWR4gtupi-D-QJ5pzt8F9BBPgZyQspIN4N7YN4SZGRVmeWTCPfGBk2r8WQwhRka9pAGufwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YVZNQzFg5vct6tM9X3YQE9g8Rha37QAK0N9k51b78OG_VQzsZP9476JiD3DI0EnqyRpFXwwTc6q8GzIchftf3gEpXGdawTRLfHmSX4gXsJKzDpIyBrG244ENS4m_eOv-kqyY1Uc88iQO_nZjeah8xyBlSel6nE-NCMNYOLSd681xm0NIO2fkKH4GLD-vcA6_mrTSNRaKLwLoVsijcx54gDOodl9kIHXlk9E_7PbpdmyHEspGGw2HMq_RUFw6QbMGTr1p66P0FxzV35688Z6n4tZiOEsp1l7zgsWCqOHbkQblaolC1ZfiAJxeVip4muwKQ06iCzVJX5dG27VRTxPk9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRsQ7vAlyUMOGdicL2Qc_bskepLbgFig1zhhwfs5p6yPl8C3s4UZEZ2lqZuB-cSEsKTRZsmhFQvSR47wG4tPKHzp_SB6c33kjkmJ1JvMV2ajMxF7ZKDVhic6FuvoPCkJz58Vm1H72OIC5SYBpl7Tcqu1JkI5WtPbhF2wfYqcwSetOx8PAg4flvosS1r6jyhm_5bOdrrM9tcvTFcZ64FYuEExu72B-W1TsOS5GUN5L3umlWO-A6glh_x2uEhAbXTziXOhinQh7F8rxTmFfDT0n3a8LZWSvFF1sLo2z74L8fsO2SZBP9iVNuMc_X9PyEzhbI5IrbAvwsIM4n-uH2Oz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=U9wXujronihO7nr6LSVCw2Rj3Dg_2nQXIAstGJX_TasjVaUlGOCbw4_Q5widUxikikqa0iD7p-m6qis3SpbNhT5EYBSTjc-VPnXytT2nOplVrdb2yJCnkj7sH19KrYvK6QtOA4NJiUJVfdJRgSSwnEofzjwd3477QTOvNl-Dn9gUEvW-hT3uO-9E07GuBfK7Pob_9hMOsvc-Iu3iSY0W2tI56zgbSykROcQOPUlwklon8P4VqJaXpCiGz03UBs6w6HMdE8_8wYzcWgdsmotgQksiRksuI9s6jcWb-WjhA6NfrYtD2aETK17El7EXC2gTXYaxFNZTQuaHBCTRVdgIcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=U9wXujronihO7nr6LSVCw2Rj3Dg_2nQXIAstGJX_TasjVaUlGOCbw4_Q5widUxikikqa0iD7p-m6qis3SpbNhT5EYBSTjc-VPnXytT2nOplVrdb2yJCnkj7sH19KrYvK6QtOA4NJiUJVfdJRgSSwnEofzjwd3477QTOvNl-Dn9gUEvW-hT3uO-9E07GuBfK7Pob_9hMOsvc-Iu3iSY0W2tI56zgbSykROcQOPUlwklon8P4VqJaXpCiGz03UBs6w6HMdE8_8wYzcWgdsmotgQksiRksuI9s6jcWb-WjhA6NfrYtD2aETK17El7EXC2gTXYaxFNZTQuaHBCTRVdgIcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=MoMnIDpJTZ5riVeaoF1wgiMgtYtj1aQd8OBNOSiJkvfVvTRGuzToBZE6fQg4yZYIc0ER_kvplsBZ-VE9rrhaQklqn83PFsPrixH17Nj8Ed5vPv0eRzjkVaeihp_7sZ8dv3TRE8DrzahVorHhRMPuUxKQQHcFkWesu9slcf1T0WFJJwcyY_A79XX3wbAvPgmAwJjIRvBRJzKr4pAcM6erPs6zJm-_Vsp5DmzodRParcNqH9Qzw0rTJfOKcimZpSrPjaU2q8hU9cgSXoTnH4wFzKM3HXv5T9nXIYOtmHVIvAtX8umlvabfap5oCIUz9nKkopCFilqZjLGJPbRcnrAzGET7pHDqXMbBd5CJ6o-mLDqBlP_dlmEvjnFZbh37ZV7KoDiGkJv_6q3xd7fOUWQ0nigs3BxQoF6jS2IfuQ8dufnKtytKC5RcBG4JqPTG5ZbSgw8ddUVV0A9wALWGyFuY25rLhEYa0oQf0zG9uEz8UNKWoox8JdQ-I2WUHt6nvD6s8HcARIdSnvNFZsdEaoUQ1gowUbt-PugKrT9H0Z8Vb0HHlFe-FXDrbrvFWkGt7ZWFPXQOuSj42jLrtBk9mDoK-U6g1muIynDdQilSNAAerNgNqzhY3fC2tfJJotjozKFo9Og6C69vKg7215cIU1ZaYh0O6puAa_s1cZqeunXiLEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=MoMnIDpJTZ5riVeaoF1wgiMgtYtj1aQd8OBNOSiJkvfVvTRGuzToBZE6fQg4yZYIc0ER_kvplsBZ-VE9rrhaQklqn83PFsPrixH17Nj8Ed5vPv0eRzjkVaeihp_7sZ8dv3TRE8DrzahVorHhRMPuUxKQQHcFkWesu9slcf1T0WFJJwcyY_A79XX3wbAvPgmAwJjIRvBRJzKr4pAcM6erPs6zJm-_Vsp5DmzodRParcNqH9Qzw0rTJfOKcimZpSrPjaU2q8hU9cgSXoTnH4wFzKM3HXv5T9nXIYOtmHVIvAtX8umlvabfap5oCIUz9nKkopCFilqZjLGJPbRcnrAzGET7pHDqXMbBd5CJ6o-mLDqBlP_dlmEvjnFZbh37ZV7KoDiGkJv_6q3xd7fOUWQ0nigs3BxQoF6jS2IfuQ8dufnKtytKC5RcBG4JqPTG5ZbSgw8ddUVV0A9wALWGyFuY25rLhEYa0oQf0zG9uEz8UNKWoox8JdQ-I2WUHt6nvD6s8HcARIdSnvNFZsdEaoUQ1gowUbt-PugKrT9H0Z8Vb0HHlFe-FXDrbrvFWkGt7ZWFPXQOuSj42jLrtBk9mDoK-U6g1muIynDdQilSNAAerNgNqzhY3fC2tfJJotjozKFo9Og6C69vKg7215cIU1ZaYh0O6puAa_s1cZqeunXiLEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1RS5tDCSnUtasQt-C9DKOj6fvfy-E1dnSgs5Hl34EadgrICpO750WXkZOaawpfn7lzDRnQy7uTpi_1lwIFLaKy0TN5QPp9BBcNLQwvOWuBDw9qfZexzpxNCzkGgtcxnUvALQslkClX9yKKh1hyTrLq0IZUEh0IzG2y01uWBlOcs8xTLo9hRRoCPIzWLaz5NJe2QHSDclUlGeF5dxyM4iigeJMyHMBImCAzzYzrx8GkBipP9vo-x4oKX-PibRvBtnJe7Syw_ndYC5TAAKeS37eIp34q8hICwWuFNkH-BcHeE31CjhII_g-qMfKDQksP9gjh6fVZj4HldeL8EhG-OWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TyPze7I3MujC5fmVwKIoHdTtj83UMyMLCjdsIr9p58YeLFjE-dJ9hTGtUUzyfKiOT2w0kd8iEi9FvKSB8dWHP-QC_e6-63Mo1QSaD_RQYfzU1K0eCeVCt20JgklIvpoQEqZ05q7oeiCZqjF8u8NvMFcF4HptW60dcd677o2jxqLLlpRyWHpC47RBD7-8a4jIFxn28GjsS6OrAs_OHFPoRSNVUPMHnNKoDlNCuLO9ef_Bc2y3YXf0r9sj64PRUpjpXJxSFtJf4CdM1P2Tt2P25fZLm8eGnbCQx7HRbt8SZAxx8AFtY8Bn4TJCRAaNBbRllpJxqRYBEAbLXGTOEfQ7sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H1nuA1BKZSCeDFJI98jbQ6slsPtfT_ra7gcYJeaHVwPBE-yCKH6FeoK3WNtWR0P0EG3_Lff7jPaQS-kaeV7PtHIVFeoAs4YMMXn7zWHigaNMSiUCPLGI6j7xhOatZrCeNgnFtdVNfj7EOhDtXb1e_TrA8TIdBsOFsiQrpACwB1ounH7VZzbof0A0iTFvQ2-pO58NOsnBXTnY56w_88zUt1gHdCd-ORPffuRHGiTTTp66p-rjdWs_zS_FMbkQfneEN6lOB98fqzf2kD5NQ-lEJsI9cXc9sgRQn8ox0WWgqFqnDnMOIlLlxFWtB0X1OREgQT_bMqoD7C7zL4_z-oVELw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Pt1QmA1NPS7YQt-0vcg_IscanFOM-xez7jqFgjMLZ59qF6hl67LwICIPu70c4cApyzCeTmVRIkUJDRiZn66WIkAgK2t4vdRoObfzty9eLRReoT_KJ_elnTbszzNZaAAACKCAtXsh0rhd5sO-l7DrOLKYH7RnjT3hKY1w-cbTivhOCoQSGsRaPk9TJzhIAzShVUvYff_QmeYRY30hpVSSndYvU_kmk_4rs-2Eme0BAo49AYeDCP7nAMYYqNsi7s0MiMpaWcUEMoj-cIpThzXp3UG0ZLvC9owxpEahKfQon8-COKyQ8p3PT9ZfG8Yu2HrNQH3sKCri2oue8Q_RFdYieA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=Pt1QmA1NPS7YQt-0vcg_IscanFOM-xez7jqFgjMLZ59qF6hl67LwICIPu70c4cApyzCeTmVRIkUJDRiZn66WIkAgK2t4vdRoObfzty9eLRReoT_KJ_elnTbszzNZaAAACKCAtXsh0rhd5sO-l7DrOLKYH7RnjT3hKY1w-cbTivhOCoQSGsRaPk9TJzhIAzShVUvYff_QmeYRY30hpVSSndYvU_kmk_4rs-2Eme0BAo49AYeDCP7nAMYYqNsi7s0MiMpaWcUEMoj-cIpThzXp3UG0ZLvC9owxpEahKfQon8-COKyQ8p3PT9ZfG8Yu2HrNQH3sKCri2oue8Q_RFdYieA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=ZNaEgWW02A-xZsitgJOjsxjyV1QzwC_qurui_k2vGh12CnG8CxOnPJqmRkOmXqBV_3ukXRp-fWMy9Wpau5gIm3H2rnUYzS9xcepaU1AD5EFi5S6gGomyOgy-IKa68ADB6l4YDCi30o6-1lIIwqPSqLKCwatIaAH2-KXrFgHR3ZlGK2w9Cde66GqOMuZIdtCb5PgDiJYBVpGcR7qyPepFM6nNqalagCWWd5EgnzQg3t6z6gustQxGNsbombe1UL9IVZS3pCH4Yo090Nx-NO8neoRGs__X8fIRKjpETnJFV6GdGI-z1zDa59Wsl4N4BLKYKLfj8eqh7dNGyGTVF5Gf8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=ZNaEgWW02A-xZsitgJOjsxjyV1QzwC_qurui_k2vGh12CnG8CxOnPJqmRkOmXqBV_3ukXRp-fWMy9Wpau5gIm3H2rnUYzS9xcepaU1AD5EFi5S6gGomyOgy-IKa68ADB6l4YDCi30o6-1lIIwqPSqLKCwatIaAH2-KXrFgHR3ZlGK2w9Cde66GqOMuZIdtCb5PgDiJYBVpGcR7qyPepFM6nNqalagCWWd5EgnzQg3t6z6gustQxGNsbombe1UL9IVZS3pCH4Yo090Nx-NO8neoRGs__X8fIRKjpETnJFV6GdGI-z1zDa59Wsl4N4BLKYKLfj8eqh7dNGyGTVF5Gf8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtCoZ2Pgw1cG6viHOhGlHclM7ArC5_oOaGNmDUBxExj7MaS9xkumgXxJSEwQ2bh7t5vGFziOogUtSZg3O6dztCYGBXR7cOidOKK5kr-BhC5NH0l_bjewW10BQmCVBX_TdRkpO7v_-AT7EqeJny7KnfPhaM2NP8FC1ycQVh1ngIK03PSJfjR7azG8CwfUREvrzXzjRXIm0tTgWMWQTEKzD0pI02RAAx2ocuCp2j87GmzOhDCfg2XjCssFYgMY5vvDnxfU6EdVJ4knJ-timKFKJ79SEVTQ2k5PLtX7J3ln6XmxbptAi-AsgALlb4KaLbRp9bJ587YDbXG1mNJrSasgFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Oz2zg3Qdk_U0BE1qm5y8ZwWgn1xBSU3R08NEA1wk4_qXcV7Kt9O29BvcTl9eoRJ7Q0Y_8WRLjfxmW_nSEYRspN4t5eW1QVEmeNFr48R8si47rYFCxF6f8cV7L8BqTo3VtFpac-SgjGqQm7A6GW-dyX-t5_6oUGfKy5aYRzp5-ZihevMTDnSu29ZRj4sIAvGdXSnJH0Hr0i9lbw8Zf9vwndyMlHB1s3_rmfkoOURbVpUepWAPrv3D2xjac5fppVC83PSu5s703qu3teSYRlxjtnIllvJvajrK3SrTvapof47iHtjWoFdY0ZeZAN9CMSDAYW5WijIXZBodPwmJsQdNJrrB0h1enBvCqlf4GXdGvSpkHnjNUmZb1VnjLFnCo1QX9bN8SCsIp1HIj7fpphOHHxk1L1R7bZoytq0yJgddx_tA5IiCe4YbMyNFD0RY273s6KLLxYkJsN04Ua1mrZxWPdx7AJtYL0luourydkpXo5IaFAWZxs5gJDbv2loKFE5bVS-URzaCGFiAcHQP2KrFfBiTXfNaIOfHvlaDxxiR_EESCSAWCDT3A4pr-Z9vS68voGzCZTsWhEix8bWivC2dDkE_fj_pb-yr12lv0q0KKjqr0mY2KKgqdJbyPS8p9m7kggcOz6dBjhtMft1eMGT2MIml41A5YOBgNCx_vTQsl-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Oz2zg3Qdk_U0BE1qm5y8ZwWgn1xBSU3R08NEA1wk4_qXcV7Kt9O29BvcTl9eoRJ7Q0Y_8WRLjfxmW_nSEYRspN4t5eW1QVEmeNFr48R8si47rYFCxF6f8cV7L8BqTo3VtFpac-SgjGqQm7A6GW-dyX-t5_6oUGfKy5aYRzp5-ZihevMTDnSu29ZRj4sIAvGdXSnJH0Hr0i9lbw8Zf9vwndyMlHB1s3_rmfkoOURbVpUepWAPrv3D2xjac5fppVC83PSu5s703qu3teSYRlxjtnIllvJvajrK3SrTvapof47iHtjWoFdY0ZeZAN9CMSDAYW5WijIXZBodPwmJsQdNJrrB0h1enBvCqlf4GXdGvSpkHnjNUmZb1VnjLFnCo1QX9bN8SCsIp1HIj7fpphOHHxk1L1R7bZoytq0yJgddx_tA5IiCe4YbMyNFD0RY273s6KLLxYkJsN04Ua1mrZxWPdx7AJtYL0luourydkpXo5IaFAWZxs5gJDbv2loKFE5bVS-URzaCGFiAcHQP2KrFfBiTXfNaIOfHvlaDxxiR_EESCSAWCDT3A4pr-Z9vS68voGzCZTsWhEix8bWivC2dDkE_fj_pb-yr12lv0q0KKjqr0mY2KKgqdJbyPS8p9m7kggcOz6dBjhtMft1eMGT2MIml41A5YOBgNCx_vTQsl-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=jkZWDn1w8SmAKbVODpe0efacqXT4OH_svcv4dvFIO7OuxT4kz_6kCDDwGRvuFCenk4QY_cFuk0Ddsk_f8rPUHNuOkqKu-LMGpp4GXr1UmdQarRtsW-6Jgm9uwos_mDs3TG2gmAmesuCmShEqYujGtf8k8wJGrY9g4YIbwVV3G9FiJIV3ilydymIajfVTr1tnI0yFQbh6d7fK2njU7PDwlw2kp9GgcQhuyofN1PuzpDhxf2YxeUYrU2Pc21kHmLWP318BAfbSMfPoJsR7e8Z86fGcy2_HlmhwXhNMa_sgl4ArssLx-YoVWB1yEz6H03NV-ziCg7wWl6CMq3-sC00q0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=jkZWDn1w8SmAKbVODpe0efacqXT4OH_svcv4dvFIO7OuxT4kz_6kCDDwGRvuFCenk4QY_cFuk0Ddsk_f8rPUHNuOkqKu-LMGpp4GXr1UmdQarRtsW-6Jgm9uwos_mDs3TG2gmAmesuCmShEqYujGtf8k8wJGrY9g4YIbwVV3G9FiJIV3ilydymIajfVTr1tnI0yFQbh6d7fK2njU7PDwlw2kp9GgcQhuyofN1PuzpDhxf2YxeUYrU2Pc21kHmLWP318BAfbSMfPoJsR7e8Z86fGcy2_HlmhwXhNMa_sgl4ArssLx-YoVWB1yEz6H03NV-ziCg7wWl6CMq3-sC00q0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1gbEXShlwgV1I6pMc5VQG1z4tml6yZVxW6Cgl8Z16Nc-yXNMmkqoLI8fQz_R573Q5LWga8EZjzEX3wrK9iDlErs6BJx4fyfbRtlEic7d6Wmskl2FI7-IuCYYxddCN3_72rbJF1AcHEYdXqno_sgLV63cdpkSbzSjdTOT_3q-Vyepuh6AptvXuO3D8YAieNGWQJjnvpMSflySgeY81vpHkLXmulRcvkq9qWG7Phwi_2mw3dflCKV9tXPwlRvxo8oQ7Yy3yraR2P6OBSS2kt0ZnfbenIG4jCG9c-A3IDv29tR_JkguaPmkJ4Ft0WQs3jyejK_QfPWVDI1KZFiX63JYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=BPehXpUIy5KhbQCGR2hu4JAKQTTqIJs6keSg8Xyy_HoU551pTf17ssq0gt0ZeU5JC-aXgrCM42wbCpnV7lPbLpIujeZhiNqmN3C5cRBkRnSOT78fsLQeC-G7gLf5QY3QI4JzBcUNH7I53OrZAmRrXvkeQnqEhJPrDdN8vLPdzCNQXvKS4natlyqcNkWCJPDro2RPGgpxv8W7qg5AS2iRhoS1uxcmKLhBVquUNW9qbjMzcLisjjRAXpS6dhLcquLOfFX7fnedp4tMz7N6z2pFeNT58KAlzu5HPi8lMjTFLMUQ-NDQ62CU6csrTuSjlqWRXh8I-0Em4gTe9FStxEdc4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=BPehXpUIy5KhbQCGR2hu4JAKQTTqIJs6keSg8Xyy_HoU551pTf17ssq0gt0ZeU5JC-aXgrCM42wbCpnV7lPbLpIujeZhiNqmN3C5cRBkRnSOT78fsLQeC-G7gLf5QY3QI4JzBcUNH7I53OrZAmRrXvkeQnqEhJPrDdN8vLPdzCNQXvKS4natlyqcNkWCJPDro2RPGgpxv8W7qg5AS2iRhoS1uxcmKLhBVquUNW9qbjMzcLisjjRAXpS6dhLcquLOfFX7fnedp4tMz7N6z2pFeNT58KAlzu5HPi8lMjTFLMUQ-NDQ62CU6csrTuSjlqWRXh8I-0Em4gTe9FStxEdc4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpNp3Pk-DOKvslCryYPeUOaw6jNxjv_uNXys9Cg4iN6NJWGMTosL58nGfmYds7S9AmR8WNChiiDKLaVg4hCmpC0kfNGsdEKLSkUicdbS4xvN5rja4EgsTM4Y8uNMYYai3B6Ps7XwWFHyz1nsUxs0foVMMli3qSZl0FPHGw-gM_fgLUc02stk9L3HAWlTHQO0g4k3ebu1dRx1K_rAICYvdZA08k3Fz7qqVFU4I8UtbYVdnSUWENoTSbORUtmFmiGvf-bppusLTaOLzERYlyOvSAmYu5PsSdHAF0aEaZp1WhMMsvgmnCQcbRZoMlC190MN4ZQ2TVHhCcF35mixoQg49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJbes0ts-AjID4rVhSo9czisjgQB0rO8CnwF3Wm-4KZrQPaOhjyB5U2Rv9-x0HGeaQ5vmN5dy2WPZqUcODieR6J7DbtTE4RflNTYqyDwaMMP7Xew7GG7lcAUno3d9CMWB-D1NpSx6r_aumwr4tSz20XrwApb69Hgo_j8NaqMqPZsAttH0PovWzd7pG8dt6Kog5SLcc_S5JtqD13l4u-zeUQcBNqsZMgaoAbPMmH--FuWdn82SoUpd2N_puY5U4yuilrduh6cy5rmipzHv16Bn0svoCEq1PcZqAXdE2TAG_zCTlj_r83aN7tpmVV6sMbYhxBRIjuWBLV-Y7hzJFaGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ohIMc3SmkmcS9KCtxdmT6E1tsxQ7IEY_LiX6GdZ_PHKFjxnA64k4i_vszqCkzQR4AWTrVzIqxAXfoUM4UM_cyZKkGWFyUDIp2-zb8S5SFukYXT1txCdAjoJKq454UYD8Dm222OgtgT78WtXUDcQV7ZHpylhpu6w4v4BgGE8pDcH2dwBOX3a3lTxAyoxIdp4DRp6ub-Mgnj4Vseyb80-5PKTteukbg9JtKbkkZf0KpNxVDh8ma36-sUgTOBINKuJwKPnQyRKHjMAb9dbNMJM2ndsRPRA2KG92GfrmvcSKEBv1eQSWXGr08d4d8NgbiLWo0xuD4-Kzk71_9B6kOWAcC0J9yS_hfcKqfrQTx7gpPBnmmVQc3mu03XNZLfXvozsYqFNFXxOB8bFeBJn5opj7jujP6lJ5eQ-YDf5SteIkcVFy3G4EXlHkWX0tn2rnUYAELOmTDtA2oQWx7iuJmFplHTbka_48PlydZt8jahIyPY2xhvvwdQVkFHpMFGZzx_XBY7ZW7QJ2dVldy5ErjIWlHQlvYhQYVE669QoRXKVVbP_CvpqaG7FwC_4HzA1LVeE4mnpnkFf8lmHVdw4gjfZM-o0CyGKli5NQsCl72rIvQyRf9_DWyAl-Yo4LygFxvLcYSmePHefYI0oh4fipMXCHerAy5xkuTklJGVEwZeiu1tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ohIMc3SmkmcS9KCtxdmT6E1tsxQ7IEY_LiX6GdZ_PHKFjxnA64k4i_vszqCkzQR4AWTrVzIqxAXfoUM4UM_cyZKkGWFyUDIp2-zb8S5SFukYXT1txCdAjoJKq454UYD8Dm222OgtgT78WtXUDcQV7ZHpylhpu6w4v4BgGE8pDcH2dwBOX3a3lTxAyoxIdp4DRp6ub-Mgnj4Vseyb80-5PKTteukbg9JtKbkkZf0KpNxVDh8ma36-sUgTOBINKuJwKPnQyRKHjMAb9dbNMJM2ndsRPRA2KG92GfrmvcSKEBv1eQSWXGr08d4d8NgbiLWo0xuD4-Kzk71_9B6kOWAcC0J9yS_hfcKqfrQTx7gpPBnmmVQc3mu03XNZLfXvozsYqFNFXxOB8bFeBJn5opj7jujP6lJ5eQ-YDf5SteIkcVFy3G4EXlHkWX0tn2rnUYAELOmTDtA2oQWx7iuJmFplHTbka_48PlydZt8jahIyPY2xhvvwdQVkFHpMFGZzx_XBY7ZW7QJ2dVldy5ErjIWlHQlvYhQYVE669QoRXKVVbP_CvpqaG7FwC_4HzA1LVeE4mnpnkFf8lmHVdw4gjfZM-o0CyGKli5NQsCl72rIvQyRf9_DWyAl-Yo4LygFxvLcYSmePHefYI0oh4fipMXCHerAy5xkuTklJGVEwZeiu1tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1g_YMf-drQ2AdzNUApmfWRHHzC22aa68M3buEyp7RxLpTANJF0ieG8kLzoIECQcGeM1WJP0T8WvvpgyCm0v2ZTYncCky7HQ9QpLQTCkDHWw819NkBaWiBTu65rjjWu_9DVFiqbwOPnk1tStXCXbYIMUv7ohqSmalbe2gD55pqIM68kQ8_kQS2xPUmB_MB8eIJDQzCzTF378YqLRYDSE6yYLxX-MXzY6vjwmGIxQYWuKqthx2CCWXD6LN1KNB-sxQ-8P6mf1uKjBisoRZO29t5IwAENqXedHYI_Ty7_78fk_I2ImBJXge_x3NHaajRfJqaRVYRdt_XEWhP6zcBRgAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9dUSZtzPn6y93FBZUQwJY7haD2gp3BfbiFgpAkWFQqxYpM9FI1CKYPzIqvTKKOsYMSvaxpM_yMLPnoE2fiK2sRuCj_M3rtxLcbJ_FOA-UkIpQQ3PsGnikX-qjVvIIFhZConxlAz3NGJJVrz_atLnisgT1nk4wMQTqvThfclcWhZb3FczOrWpNM35n03-e-E2dOS9w1LPf0CkoHAnIPrrCRHma5Q5icMbbRdRt0WeLo5F69nOEuDS5_I819QjtVAh6VMXISRSvpEKAa1boSZdv_tfTnovTDkyRchUxIPFi54z8-ofsOzfDmhhwGVYCSdnHmGUQd2-zjIaMes2h17lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=UuRcMX2tMM7LBuzhhjWhWU5KxjJ_hYoLQ37onVuDmHOjGkGJgxksXKdT9FQ9ZAvIio-CzsA2qSfodqgHVa8kHRBiMvPRoOkJZVm4nzvfkimXGF92MzQMcStG9dxjUXOmVfbgdS-WVeW12XBReGtH9-A6UbKl511Nv8EKmY-Ea700XM8Mow28W-39o8B5jc3XNvJN40su4ScI411U11TVg69ipn9r-JxTY89COhmT87Q4IpQPVGiBbP24ibUBXbhoIdWjWY1zJE3zBa5iWg-ejEG_NmT8LcApj_pLoC8Kw5eEtCbEdgzem2EhUe7MfWikCZ4gdcZvKAIm-RlM2FMBlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=UuRcMX2tMM7LBuzhhjWhWU5KxjJ_hYoLQ37onVuDmHOjGkGJgxksXKdT9FQ9ZAvIio-CzsA2qSfodqgHVa8kHRBiMvPRoOkJZVm4nzvfkimXGF92MzQMcStG9dxjUXOmVfbgdS-WVeW12XBReGtH9-A6UbKl511Nv8EKmY-Ea700XM8Mow28W-39o8B5jc3XNvJN40su4ScI411U11TVg69ipn9r-JxTY89COhmT87Q4IpQPVGiBbP24ibUBXbhoIdWjWY1zJE3zBa5iWg-ejEG_NmT8LcApj_pLoC8Kw5eEtCbEdgzem2EhUe7MfWikCZ4gdcZvKAIm-RlM2FMBlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=H6fVzGqS1s8_92wkj5FnzUsg_JELSk1Qm05trtR8bzL4nlHgBBzPKL2qHM636-oZ_yWKG58Q-fswI5lCiwrZG2t8E5FWrJplYbQGBTi_7cHx-slPEmMdD66JLzCCUyskKawGqBW9swMQjvOEIOL23qeTequXA8HbYxEAx_XYhdCRphkS-1Viitb3_UbyjzS-vSII83EMAqGfere2p8ZWqJu0b7ssfDrgfaUZGF6irK6QH_BMtpY2jOTkG2GvCrZIXhSb7E8AfrnuwIHGXV6vDO4ovI3KipV12LOZXnHOMHYrufp1D4zkgttijwGVT7l0WI9UueRCB_iV9S55Ms-vNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=H6fVzGqS1s8_92wkj5FnzUsg_JELSk1Qm05trtR8bzL4nlHgBBzPKL2qHM636-oZ_yWKG58Q-fswI5lCiwrZG2t8E5FWrJplYbQGBTi_7cHx-slPEmMdD66JLzCCUyskKawGqBW9swMQjvOEIOL23qeTequXA8HbYxEAx_XYhdCRphkS-1Viitb3_UbyjzS-vSII83EMAqGfere2p8ZWqJu0b7ssfDrgfaUZGF6irK6QH_BMtpY2jOTkG2GvCrZIXhSb7E8AfrnuwIHGXV6vDO4ovI3KipV12LOZXnHOMHYrufp1D4zkgttijwGVT7l0WI9UueRCB_iV9S55Ms-vNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=JGI9gacPFnRCtNKu93rj7TYQFSPiqnEP_n1NP-OUt1GORP2B9RbL26jWRFKYvoDKPBn52Wf7_fCs4mNIU_BaFpqo2GAgnYUL3apaB1Wj9oKJqrY42Q6OLqBLE_2uS5isMsH-VGQGKcmk41GoJqG64o6FKewZKATTa4J_jbVntTjU3qkBIJX7Dwmkdpudo3HVlvS3A2WofIQ-0njTGez6WvH3Z3DAn6kTKPFgCcdbgvTcU4F7xFbEC_fEXoHkkqGsVv9WlfPtuLGs1ghGAu89eQgZdgCLF4w9PwtqJh-RN_Sl01Of_RVBz9wDzqghxWy-SMvF50g0RGpyHD7sPe_Ezg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=JGI9gacPFnRCtNKu93rj7TYQFSPiqnEP_n1NP-OUt1GORP2B9RbL26jWRFKYvoDKPBn52Wf7_fCs4mNIU_BaFpqo2GAgnYUL3apaB1Wj9oKJqrY42Q6OLqBLE_2uS5isMsH-VGQGKcmk41GoJqG64o6FKewZKATTa4J_jbVntTjU3qkBIJX7Dwmkdpudo3HVlvS3A2WofIQ-0njTGez6WvH3Z3DAn6kTKPFgCcdbgvTcU4F7xFbEC_fEXoHkkqGsVv9WlfPtuLGs1ghGAu89eQgZdgCLF4w9PwtqJh-RN_Sl01Of_RVBz9wDzqghxWy-SMvF50g0RGpyHD7sPe_Ezg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDHafmaAfRjHyxbV1U6GnyE7Lf1eiY25jv_KrJcW2Ou_D44Qym4XbkwCyxlPI3fuufclU43c8viatvMSz0X-BYV34Mrh1ynNvOcMI1eVrenYJCPZG1e74MZMJWgM10ckX9JkW5aiX3vQVte0_QZlaIoHn8tVkm2Mdy4jvb-J6Na9Z-62bpyxnB-5LYaWtu68HrPXIR5S7oUcoSz03XNqnOi497jnRAudDRK3rKTeuALSVZWf0MZ9Eri8yL4ghJYUfjQS7mgAD6CsNDPTHus6xSG1AwyYK9CGnWVAQ5dDujewMRkrOlLeeRkKE5DMKAQYyhD21TW5-7YlQAEsWW7g6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IDXeslWqqj4TxzRwiHeFMeBDz6ONV-yMp82jT7Dy5BDnyrqvzzczoTX2THruQyY8rU6q5RQp4vyjUXAztY7vvILFvCGtGBsXGGQe38_LYwMe4Zc4Hti4BQo2tD_HlrImXqi7A-X4HT69KdIOrp11i6d9pMyPC5ChYpRelQxBgXmiRMn6_16KO0xR1dsRXNfvOUNHozPWXNSNgx_8WLnX2KvXsq1f84-Duhznk-fQ6B6b2kBNrqZP3aFFKr9DqKyiQE1dckQx4GciBbx8XcjTo72GZuZJ2BJCi_6lWn1QLWEr5UmvHK66LSrEwpPQezQzplLMpnizfYR9RZkzV-jDss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8IDXeslWqqj4TxzRwiHeFMeBDz6ONV-yMp82jT7Dy5BDnyrqvzzczoTX2THruQyY8rU6q5RQp4vyjUXAztY7vvILFvCGtGBsXGGQe38_LYwMe4Zc4Hti4BQo2tD_HlrImXqi7A-X4HT69KdIOrp11i6d9pMyPC5ChYpRelQxBgXmiRMn6_16KO0xR1dsRXNfvOUNHozPWXNSNgx_8WLnX2KvXsq1f84-Duhznk-fQ6B6b2kBNrqZP3aFFKr9DqKyiQE1dckQx4GciBbx8XcjTo72GZuZJ2BJCi_6lWn1QLWEr5UmvHK66LSrEwpPQezQzplLMpnizfYR9RZkzV-jDss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gSOU91W8FtYjvWo8essrXisrIK481Qdx9V5TNl1HygJQ43l_jX6_vUQutO5QbbCkhg6DuqYSL5MqQ-Lr3gkEDHA-zXHmdJlK7VGCmDjeRh5Ki15WU8qFKoY8ZTHcZzHP1Usj-hvwj6UWypZorsGj6w5LHUkn8kXVmwJQd5wZTvbx1Tvus8LrwzdMpxmEFfSUltsF6rY5eUJw3wwVbOLI5pc5lWguWeCZXyP0Hv06QVzTlOpzqWOKxzf808h4hfoF-edeD4JP_hmyfbTJ9l-rVRMeE4RZHxlrqiepmnkhESPAwjBgGjt0c7EJNp7p64L4GQG6Nvbbr-qxDJX0b5DdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=gSOU91W8FtYjvWo8essrXisrIK481Qdx9V5TNl1HygJQ43l_jX6_vUQutO5QbbCkhg6DuqYSL5MqQ-Lr3gkEDHA-zXHmdJlK7VGCmDjeRh5Ki15WU8qFKoY8ZTHcZzHP1Usj-hvwj6UWypZorsGj6w5LHUkn8kXVmwJQd5wZTvbx1Tvus8LrwzdMpxmEFfSUltsF6rY5eUJw3wwVbOLI5pc5lWguWeCZXyP0Hv06QVzTlOpzqWOKxzf808h4hfoF-edeD4JP_hmyfbTJ9l-rVRMeE4RZHxlrqiepmnkhESPAwjBgGjt0c7EJNp7p64L4GQG6Nvbbr-qxDJX0b5DdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ky3KuUoCvuHVkCCPJGWY4KUCZa1YIck-SaME7FX44xLzP8_UcsTbx31DejH5fhWJ991LPmjCvkrDYpuYLHicyPlWaL_HJ6xpDkkjTm51pGI5cXM1jYSx9xJc3pO5nbwIberMMBsrEkiHZaORnKyOebCU1bhp7RYiYECpiMeCf19X-GgFkFC00wErNzM91aTOAlf7GHfgs2ReBrX3xVy3OcgzoJvOra1UYnSdESf5E398-7w245CwXDmc5GbhVgtmuozWAOry2TA3ObmOui_7Le1ShkwsPl8ZdwvOLwEOKHn3M8pbyC6_le71qYC1OPK_smXQfhZKVIzvZGlfaSQvmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=MHm9ENsh5-CYLgRl7OWfHWMcGZQn3N2wIoeVdvyG3jAlNNlv71QQ84n4L6MXEj9TO0abCLz_M22ZLalfUObGkvnK3eVTHIh6qsWyQH3M1DHC70cR71FhSEsXkP-WdLNJPtds_llUsKCpfQR-A-S3y5i1DyZAHagQVVt-RA0cvmxWuJV1Oll2ElMGZu6Mqf2sBkX68h8FPB740yS310dWDxa_PNdBfSzgdnUNJdURatwGzaL03c8mW2nP2DrUMaPDjvgdsoo_IwpL-EVQtyreNOdsdtDt7kD5DwQAJU6_3lqX0MVc2s-s64xmsJGtDQwvOPkmuW8d1SSFfUxkJnPkCmYtJzGyeDV83escrqSmLJH3T207aBt3zGWE-jT1DpdKy-hv2zX96NT2BNK0zoBQFOvbllAhj8Gfqd4wVxUb6dLRYzs2NvWf1phbI-YMqDWqmyELCZMGp0S6pf5iiym9TwNu4gKBoASNowXwQNQ7yPjOLs0kh9OVJOZozwv4mC-NzU5at4lSRivKQBNN2qw-fgLk-CsC53_t1eMezXqJWUonGiT4A1D8lDxlYx6r--19PABC3sZNc9W3qlEWTiYswKGcLLwWm_THtCP_5E1w9q7nnSXP2BzNst1nkrJy5mWO_6DSlXT4N06dZ3IuXpu4C3h7zuRJx955fp7y8sZd4YY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=MHm9ENsh5-CYLgRl7OWfHWMcGZQn3N2wIoeVdvyG3jAlNNlv71QQ84n4L6MXEj9TO0abCLz_M22ZLalfUObGkvnK3eVTHIh6qsWyQH3M1DHC70cR71FhSEsXkP-WdLNJPtds_llUsKCpfQR-A-S3y5i1DyZAHagQVVt-RA0cvmxWuJV1Oll2ElMGZu6Mqf2sBkX68h8FPB740yS310dWDxa_PNdBfSzgdnUNJdURatwGzaL03c8mW2nP2DrUMaPDjvgdsoo_IwpL-EVQtyreNOdsdtDt7kD5DwQAJU6_3lqX0MVc2s-s64xmsJGtDQwvOPkmuW8d1SSFfUxkJnPkCmYtJzGyeDV83escrqSmLJH3T207aBt3zGWE-jT1DpdKy-hv2zX96NT2BNK0zoBQFOvbllAhj8Gfqd4wVxUb6dLRYzs2NvWf1phbI-YMqDWqmyELCZMGp0S6pf5iiym9TwNu4gKBoASNowXwQNQ7yPjOLs0kh9OVJOZozwv4mC-NzU5at4lSRivKQBNN2qw-fgLk-CsC53_t1eMezXqJWUonGiT4A1D8lDxlYx6r--19PABC3sZNc9W3qlEWTiYswKGcLLwWm_THtCP_5E1w9q7nnSXP2BzNst1nkrJy5mWO_6DSlXT4N06dZ3IuXpu4C3h7zuRJx955fp7y8sZd4YY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc86q_EEM5zNBPcdKtGGr8mhn18xzbONCT5QsG2BDx61ueKlaiVpInCjHxTapV1C0lncRwOBzsLu3Jyac0Da7J9rh_uE0_HTDeNQqpkJlZ-XvikvrzncSNYNZvedWWKNlUiCrMjRObIzOGFkOTnB_SYXuP214tQTTF25kUODhs8RkEuEUWXfAIVGsAgnVJnOauR0L5K1gl-_Wp_Z358nsTaWy2Tvbavbc7gkh2yXOZAWmXKuuSM2-uJw9iS41Xs40jnWPmNSJhZoGuylY_q46009EIU1z5uyupY6GynS8ewG8Yc-c_XvhEUSCTKR0RbXWnnx_GDN1qhihnNhvrOBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=XY3Z0ViL4CcU3XHRY9YSFIORoITkiVB1zMTGqMa32FWieS03G67imScH5krELl_gFkuXP_NAAD1RqiQI2RckVkCzaMmNkT23NYDPo4z1DdUXp6mRQMU-lLIbLfhwqh-FT41O7syHri0r3oOSHyL9wvpdtrk2rEW01wJUfvO0mO_4pJThn8Yff4MVD_PxbY64lvgE6uYi9vn69Rsc_KY4Fc7ncc0fmg5Q8Yl7pWBEVKOZpjLvBK2FoGUwrTy7iEXUKanjVjFdf25N6RGWSRf93fm3TMwdxNGCgyNJEsrt-F0oaEDxoGhnKFIvNhg-FJZJVUn_-LPRa_cQb5vns2HS_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=XY3Z0ViL4CcU3XHRY9YSFIORoITkiVB1zMTGqMa32FWieS03G67imScH5krELl_gFkuXP_NAAD1RqiQI2RckVkCzaMmNkT23NYDPo4z1DdUXp6mRQMU-lLIbLfhwqh-FT41O7syHri0r3oOSHyL9wvpdtrk2rEW01wJUfvO0mO_4pJThn8Yff4MVD_PxbY64lvgE6uYi9vn69Rsc_KY4Fc7ncc0fmg5Q8Yl7pWBEVKOZpjLvBK2FoGUwrTy7iEXUKanjVjFdf25N6RGWSRf93fm3TMwdxNGCgyNJEsrt-F0oaEDxoGhnKFIvNhg-FJZJVUn_-LPRa_cQb5vns2HS_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qA7mm16Layp3OZIF07SZpS3nMJCunuSYkxWp9WcRfjYHrnYzgBYZBBNZW98zRLCVoT5zYQ6uXrKzbslr81kph0pcq1ZTfA5owL4TMnr2FkHyYbEI2-aZFfE2Ku1l3CjQ8xyRbyjrX4mfmQ-GrGPt_Mam-qAHbnu0g3HpqoDS8MqOegvCJbfoDfMBUWOz_UeJiwljpC4ae4EsoYLXpkEIIFTb1XBtojwI8ydJTVDxlxefQmGqweh7z_4DFathj2NnxqfIU_vxwvj5a8B2sRPXDc2DX0zyltAU7oagQ5KxfHc6FKmnH3NZtvKf3xUIjXQzt1IkxecKc3YrwpdCrwPGmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/te8hl6lezC2dSFv2e2XRhG6i4DE4h9OXKEp4ttEWJlxaxja9Ca8f3c4ulAUrimZXpHTGjAiOKcASM53tQ_Hf_JEGgoOyvM7Xe2xLrdaqnRj8djE9bNcWsx5qH8PkvyHMSvUifWaHQvigRP8Kz-p71rEaMXKbPcjLvuNXPQXaWSZ3rJB8HQf7_ViVOUpqstnzXmty-PNMifZOgDxbxvkTW4vugDyzBggNwCL0ZnrhaX-l0RsaHagAjLM4F0mrOdxWiuiLrY-mpOmjvOcFReZ1LHw6mO28ycEN4OxUIcC-UA01eUexxsdw7LIbk1oYnEUUmDNchuvwxu9xux9nTbxXWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHyuQriet6FgCAcuejWywd95hBK5Xxn_lBTSl8x1ZyxmftKFy9RgbpLGbyVD36yRzWUEmvRYA4-aaqBzFXUoxBXO3X4gDV7qnaHr1faQrMVTPKUhyK2kh1LDIK6FwEF_yWt4CbFtwDsY4gXUs3SzF17i1AMU6sAylrZwkQcwq6td3FR3H2MHHYxEsvo4IIemUb0psKZUSd74N58CaBuBVrkG_UzTCARb8v-_W7l_StdKeL-hSxbfRR3VWzM1uek08aVHYkOvVbm_gqUY-dbvFWAujsTbDIRdq4UIScSgFyeGz3oTLwAyGyujWvbY_8mXG3FmCBXqwv8O0Zl_DlDLkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=IDQrtKs8WLm7htiyScSgpVwSm3dpmqTW6KFln4dGU4OUp2gRqJG1eEuFN5V1Bu44bqPm6_DihOhQis_NFFEefBxT6jpd4CAz_UUPMsHOaNoaSQTBswmFCtcjHe96ab_cCsTIdgNYNMb_8sKnJGhcLfV3kSMNh071yTqtgTLgXaimQJxNng_-JIlEtvz1FNgIGJ-Fa1sbh1IvuNeC9z4I0xz6l8D8vQ6xp0L3wD2IjGSM35YVFlOUSPsYpCf1wmuzlz54dImUW9ShqTL7-ze51oQgGng7ozhnrfBiAQzqdehF31X6Por4Cm6Ywd5Yw9Sxo99KBsbQT1T5bi_xmmR3SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=IDQrtKs8WLm7htiyScSgpVwSm3dpmqTW6KFln4dGU4OUp2gRqJG1eEuFN5V1Bu44bqPm6_DihOhQis_NFFEefBxT6jpd4CAz_UUPMsHOaNoaSQTBswmFCtcjHe96ab_cCsTIdgNYNMb_8sKnJGhcLfV3kSMNh071yTqtgTLgXaimQJxNng_-JIlEtvz1FNgIGJ-Fa1sbh1IvuNeC9z4I0xz6l8D8vQ6xp0L3wD2IjGSM35YVFlOUSPsYpCf1wmuzlz54dImUW9ShqTL7-ze51oQgGng7ozhnrfBiAQzqdehF31X6Por4Cm6Ywd5Yw9Sxo99KBsbQT1T5bi_xmmR3SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD3nR_tjIp7puctGyC28Vh6OCCbxKFN0g0pJRG7cNq6xZUiGJXFo00qzowe7uTXltyQmBgxlL41GKqz_bgBh3aIDs9I70-ty0QkYymEY-Op4rRiFULue5lqcyEJS05pv5xIvIJH_ALA_mZESDs_fr8N1JISkwbfwMnLa4iNwkfTzB6xFGllkhoAD2qu6LZrXQoNRM9K62-Rz3ycjXVEPdScAf1S6C9Z2ST-Hz_RW0YA0NRN1bGornDvZd7d5cL_R3CESK_UmtwO2kFZLs6oC8aJuMrbG-kU3-3VR7fXEAzZe--ENI096Yexa9TIPZU3PJYBfL2JWQFcD-nY7Wn8uEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu41zfNleny7bOz0El-0pacvg4HPjZNOtvkCY5WR517abk7dSrU6ZmMRYr-qJlsvwKNfuRl24FNRf9PwJJSRUDt_XCdZQbwv-P9mhTdyfVDDjDTJ7yi-G-d7ZS3EBLPUH_1eoWiMPDLGPRP4IDaexPSnvxpTTrnEpTRh4XbYktqWT4gnfnwvcLmWloGbVzZONDcKkj7nf9cXCzOtkgTV1u-1S_PiSRLxKbKbQRnioljZabPWfPqx4imHDYrKFaelNi92wDsXo5LbVaB0kh2STr3CBdlqA153eBxjhG1sCJlEm7Sb5BV9Ut5l1pTPqe70fB6q1mKsPcuun2tGn0yWHiOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu41zfNleny7bOz0El-0pacvg4HPjZNOtvkCY5WR517abk7dSrU6ZmMRYr-qJlsvwKNfuRl24FNRf9PwJJSRUDt_XCdZQbwv-P9mhTdyfVDDjDTJ7yi-G-d7ZS3EBLPUH_1eoWiMPDLGPRP4IDaexPSnvxpTTrnEpTRh4XbYktqWT4gnfnwvcLmWloGbVzZONDcKkj7nf9cXCzOtkgTV1u-1S_PiSRLxKbKbQRnioljZabPWfPqx4imHDYrKFaelNi92wDsXo5LbVaB0kh2STr3CBdlqA153eBxjhG1sCJlEm7Sb5BV9Ut5l1pTPqe70fB6q1mKsPcuun2tGn0yWHiOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=NJtUDWN4WPz_QMePGqa95yK9Epbg54oZkQjhcddoENV3RCvakRWG-Ha2DWyRIfZ6vOsvJUEBhS9hmm3UBt64LOwK-inHnNld0dkL7AcxpmN4Psl6Li6OH02Bwg7VlAQ5nHd4gBPNtNQH0SZwFxVpxR0ulOrOlM_S1s_ZB5TBDn8gSM16HkpuBgG3vTMZK_iICU9vcvFazEszznLmU_rtbs9miwxQms1fYtTW3T03inZ6mC7tYQeR95SrYLFk5QQSJj-nWIw6zh7j651jHG0vv_VGV-WBXw-WeTtiAfh_xf2xFnndt8DtYXWmOmWpk1xesHft8aUtW06c0gIbUv_aWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=NJtUDWN4WPz_QMePGqa95yK9Epbg54oZkQjhcddoENV3RCvakRWG-Ha2DWyRIfZ6vOsvJUEBhS9hmm3UBt64LOwK-inHnNld0dkL7AcxpmN4Psl6Li6OH02Bwg7VlAQ5nHd4gBPNtNQH0SZwFxVpxR0ulOrOlM_S1s_ZB5TBDn8gSM16HkpuBgG3vTMZK_iICU9vcvFazEszznLmU_rtbs9miwxQms1fYtTW3T03inZ6mC7tYQeR95SrYLFk5QQSJj-nWIw6zh7j651jHG0vv_VGV-WBXw-WeTtiAfh_xf2xFnndt8DtYXWmOmWpk1xesHft8aUtW06c0gIbUv_aWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=QdbZGRMD2ScKcREUQ6H-uOWMOfwjqr8Qx8YuIIiwkgVH7gT3JBDxSkiKCARnRcyb_jwufwYYneMWUyvo5xQm_DC3TSN0GEX9REwIqheYLV9QhEeFog3UIk6fuH4zSmGpr7wlEPtMmeN0KwQm7IbHYJA0nt4srSRBBPlSDtgc1Jrp4om1A0swRrpugHNsRbToWAlzhnFrenHlNEEMKpiJuazIUstK1BY7U2XkeK16j3bmzcxQXEmpFkqRkGA7WX1QASvUv2Ud5NvCYDDOjaoTYok8TxYF1eYGvBjfF7JrohOH9rgjVWfVeXdTZv9CRfssDOfukfaSjK9FV8WlsSKgtzlByyyw_FN3ITTfN67zja40_KpXZ1jHUIloDdMeP5nJh93xMFAxzNZdJG1K__A2PQtsgeMA6g4ubEC3IF24pCluiKmNZLUxPWkQX--l1repnG-pGsW7VZgN1q0RWL73_IZ8fzUjcNb9D8eduoxKzALdRjIUHP5XciNrVhlCahvofScqFjwxShxkDpRybgnlZseMjLVb6lIKJ-YgZTQyOYbCPQ3gV0tjNCp9DsrUeCeOVhazqhG1xwDIH2TDbr-m_o19CHpvUnKdrbu_DyW7RjD-C9BPw3_FwW7Thd7CfA3tAY9V844wTAginej31AD0tfWT4NX502lVk0GRvFrnwoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=QdbZGRMD2ScKcREUQ6H-uOWMOfwjqr8Qx8YuIIiwkgVH7gT3JBDxSkiKCARnRcyb_jwufwYYneMWUyvo5xQm_DC3TSN0GEX9REwIqheYLV9QhEeFog3UIk6fuH4zSmGpr7wlEPtMmeN0KwQm7IbHYJA0nt4srSRBBPlSDtgc1Jrp4om1A0swRrpugHNsRbToWAlzhnFrenHlNEEMKpiJuazIUstK1BY7U2XkeK16j3bmzcxQXEmpFkqRkGA7WX1QASvUv2Ud5NvCYDDOjaoTYok8TxYF1eYGvBjfF7JrohOH9rgjVWfVeXdTZv9CRfssDOfukfaSjK9FV8WlsSKgtzlByyyw_FN3ITTfN67zja40_KpXZ1jHUIloDdMeP5nJh93xMFAxzNZdJG1K__A2PQtsgeMA6g4ubEC3IF24pCluiKmNZLUxPWkQX--l1repnG-pGsW7VZgN1q0RWL73_IZ8fzUjcNb9D8eduoxKzALdRjIUHP5XciNrVhlCahvofScqFjwxShxkDpRybgnlZseMjLVb6lIKJ-YgZTQyOYbCPQ3gV0tjNCp9DsrUeCeOVhazqhG1xwDIH2TDbr-m_o19CHpvUnKdrbu_DyW7RjD-C9BPw3_FwW7Thd7CfA3tAY9V844wTAginej31AD0tfWT4NX502lVk0GRvFrnwoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=aQtq_mg4tq2Gm9YHkdwu3Usaa9jROJDW91rz8fYJOqlZuJIZCL0xOoyuTLyu_vHhiGIdQ4xKrLF2Mxpqhf5BfXKy46eXX-OxsQu9mnVGTn14Jkpa1hTnKPD3aJXpd6W8_B-qm0VyDHW8RXzE2_Jk9xNVNZtacNOYvwbxkZuW5QNotdcqXBvRM23ZmnB0q6xI9-z-9HUEPjppvq709_xiUAsrxF_pMqAbBOD43ZcfHKVtixjl_XQ3jJPmtmxBWPdFaccwLqlwxzvRpmOQJZkd8MYI_ej7qw9QcBB0PPhTtVVx29hkEXGQsd1gHLMsOWJyPsn0sT7Eblg52fIyf1Jepw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=aQtq_mg4tq2Gm9YHkdwu3Usaa9jROJDW91rz8fYJOqlZuJIZCL0xOoyuTLyu_vHhiGIdQ4xKrLF2Mxpqhf5BfXKy46eXX-OxsQu9mnVGTn14Jkpa1hTnKPD3aJXpd6W8_B-qm0VyDHW8RXzE2_Jk9xNVNZtacNOYvwbxkZuW5QNotdcqXBvRM23ZmnB0q6xI9-z-9HUEPjppvq709_xiUAsrxF_pMqAbBOD43ZcfHKVtixjl_XQ3jJPmtmxBWPdFaccwLqlwxzvRpmOQJZkd8MYI_ej7qw9QcBB0PPhTtVVx29hkEXGQsd1gHLMsOWJyPsn0sT7Eblg52fIyf1Jepw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eH3Ztuyfa4qvh4BxoPyrUY2yice18Lg7LVjWCTPbaEpwrvpf4OCWEQRQEijL5EuvBNxgtKH2YBHW3VFPRl06w4rBsj7qnLNlpWpvR0grfyXTYWVDj2a_QHrtHlJRLMxo4YvHzZEPzqlgnnae5NLcMfTwihfkmuBho9GFx1U40kQK2iXzqcbaxDGtsi5fUv3E9V3M7t-QxlUiIWOpRh4DN-SatuWWxCr6fkcLw4fPGLPoI9ifQMCgvBIpS7wI0xlXa9g5zv08yTCQ5SlPM91zISZ1k35aIp8dK9Em9eYtvc3vevaZ2-SFTliWVfU87Cyltr5dGmNt1-hPSFlHP_7euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=XsaxrC8WYqoXUV27I_4WU-ZaZzJmExnKe2IbW7tqHBFcadINxTfBFhz5oKciYDr9AMBkD3wLCotnyGzwBEXICZwpyeUeauoVTYjiW8a7fSvvzvV524qF2NXRbg_xqa60MwgfjQHtsadiS2WE7ZgI8IBFlRqAElCRGglqsbRQkyQCvbtHLl4fDsQf1AR31fcR4b7hBtkxSVRAhYTfgsdENv4sQLu8NqCZQb7YXcpPk0hqMC6-pZYT8PDddOUoSRVocvE_Yc5TOECoIODqUtgIpwvtJtle8T9CfpL_uunTmle1oykKjsSVm_DHmbWw-51o8XEti-bACwE8EOzZNfsqeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=XsaxrC8WYqoXUV27I_4WU-ZaZzJmExnKe2IbW7tqHBFcadINxTfBFhz5oKciYDr9AMBkD3wLCotnyGzwBEXICZwpyeUeauoVTYjiW8a7fSvvzvV524qF2NXRbg_xqa60MwgfjQHtsadiS2WE7ZgI8IBFlRqAElCRGglqsbRQkyQCvbtHLl4fDsQf1AR31fcR4b7hBtkxSVRAhYTfgsdENv4sQLu8NqCZQb7YXcpPk0hqMC6-pZYT8PDddOUoSRVocvE_Yc5TOECoIODqUtgIpwvtJtle8T9CfpL_uunTmle1oykKjsSVm_DHmbWw-51o8XEti-bACwE8EOzZNfsqeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=N8KLrzOzcUE-tLfxf7kVBh2ghfGN2g2vn90xi1L4X50zdg1ejPCTAA4RPdwoGrARBFpTD9kKn9dNzyHL7Oiz-NDN2qyy60H-3feRS2YFaEEoj6F_YBKDuV9_Bv6PEvxRxux9N918F7XtwxGXqq_sk5qqADTfLclDjfK6BqKWtSDRfuk486J-mxyKPrwfdELA783-0-_ZrKUAzhw-iActQi90gEOPDseZLS4M5ljBejPAgdCY-HrohVm4V7ejHimvcm6Fulr95PqTOVPCwbQ6PB-dQvZsoVHhWDHGvMnArSkYQ5KmCpPE4rulNrEtFqwBJyIUGE0T0x9trCwLXDbHUzTIB8siU1fSbjYoxNdjqzd68eUow6c5zMAk7QaduFbIZSijwQOGZa9ntAo0p8s3j2Qi5jcllVKnxOPzr_MwSGYNfLoo1aTngDMyooPOz4zzCjg837oPB-MPWvtE5oMJY-aeaY01QN5srX2aBKzQ6se_2JRwyamoWp45dxvM6ZywrfbS39BuI5b7TVu97mxR0mGOx4tQCIK5pvfB7eagoll1Eu3kICetO37qRoIylvj1qWPhWKytCDel1_a6fqgWRSJa7ugvve8X29PWvK9KOXx1E8fVH51KFOAn2B_QsHZp67Tw7qL3J4QyHgiMRaRNZl3eaRj2CWjgi9xPLKEQLts" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=N8KLrzOzcUE-tLfxf7kVBh2ghfGN2g2vn90xi1L4X50zdg1ejPCTAA4RPdwoGrARBFpTD9kKn9dNzyHL7Oiz-NDN2qyy60H-3feRS2YFaEEoj6F_YBKDuV9_Bv6PEvxRxux9N918F7XtwxGXqq_sk5qqADTfLclDjfK6BqKWtSDRfuk486J-mxyKPrwfdELA783-0-_ZrKUAzhw-iActQi90gEOPDseZLS4M5ljBejPAgdCY-HrohVm4V7ejHimvcm6Fulr95PqTOVPCwbQ6PB-dQvZsoVHhWDHGvMnArSkYQ5KmCpPE4rulNrEtFqwBJyIUGE0T0x9trCwLXDbHUzTIB8siU1fSbjYoxNdjqzd68eUow6c5zMAk7QaduFbIZSijwQOGZa9ntAo0p8s3j2Qi5jcllVKnxOPzr_MwSGYNfLoo1aTngDMyooPOz4zzCjg837oPB-MPWvtE5oMJY-aeaY01QN5srX2aBKzQ6se_2JRwyamoWp45dxvM6ZywrfbS39BuI5b7TVu97mxR0mGOx4tQCIK5pvfB7eagoll1Eu3kICetO37qRoIylvj1qWPhWKytCDel1_a6fqgWRSJa7ugvve8X29PWvK9KOXx1E8fVH51KFOAn2B_QsHZp67Tw7qL3J4QyHgiMRaRNZl3eaRj2CWjgi9xPLKEQLts" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB_lU_Nje5DjWYyr5XcxSs-lKDiQRKQcyY_VBIJgiTaO5H4Gvcb3ndyUqfO6w5nrvOF95TMPGbJIDmiJ-wh-Ld-Yq5kn0nD6-ytX0zGSnphBohuMH3sOsIunZU8g1QzbO4jjoJdGPTN1lJyQi_X8fevAj_4drm8VNdi9SN3hd7UhtZKK2izHXBIg87NfKHRz8DfijNgH8RxQizyOy5gZqIC5-q7H0E8Klp2mghWrjeaLlkQcPBp001Z_ued8MEfYBZGuics1lc3cCffSe71CUyevDDWlPpTHz4DcJZM1V5fMMA_9K-dcRTZ_hUtGaCrOZzd2WsUe91swE5LW1jIrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=fJLhYPn27A1rgOzd0BCMYWtMktka3GppBUitCt6zbXzyDNKNZgPTTW3cXOMg8FgvIXxghKTYQ211bUWKwLAeUkDTuLlSXuU6gxUiS7hnxhB2CaosOmGrU2sVpQLN_I_PFlsbwY3Du74YFakEeXy9bY1JqKDRUvtjrK70UEbQi0GHtm3ogFQ3QT0Y_dUoxGuUtB04rInNuZ1P_dqN2hY8CKLx6_8-4vD2Qn-h0n8flCmSeJ4eZwNIijk1bRHAEYaJ6zsXWZpqsVM27eHSdO-QUwVhOWxwNMNUyzkUrQIFD2VIv-eHIyQZ0-W7qdr0Odi4bVogAw05nq9ieWbwtM_BKL_GHKwRSadQGynYKYMl-dh-Q4oEEUaaO2ZXd5Gv8p_dHmu4dFCVE-ZU-EE8S6_0TmVKRyKc39pdAGNKey0n8SJk7tzUn2GbBxV6bmg0JQaTTKMoHdp4bD84km1pchxRGAsyNH5MUPbXOUuGInSKP-_S9gqOwDzJM65ipWtL-fyeeiECC_6W4bzooFdoGWidZ-3WjRkfm6dRfoEt4KEJp907NGzQD0AqFZ2TIljlRMoQdyj1xqa9M-p76CN6A6Lq9NhwYbIR1eu3qd9TW5V2PwhCOZ3UCE6ub13gA9Ba4M_vz88wMJ3C64O8hIzpD2SsNhHyaP3gdqTQWEolAQDxXAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=fJLhYPn27A1rgOzd0BCMYWtMktka3GppBUitCt6zbXzyDNKNZgPTTW3cXOMg8FgvIXxghKTYQ211bUWKwLAeUkDTuLlSXuU6gxUiS7hnxhB2CaosOmGrU2sVpQLN_I_PFlsbwY3Du74YFakEeXy9bY1JqKDRUvtjrK70UEbQi0GHtm3ogFQ3QT0Y_dUoxGuUtB04rInNuZ1P_dqN2hY8CKLx6_8-4vD2Qn-h0n8flCmSeJ4eZwNIijk1bRHAEYaJ6zsXWZpqsVM27eHSdO-QUwVhOWxwNMNUyzkUrQIFD2VIv-eHIyQZ0-W7qdr0Odi4bVogAw05nq9ieWbwtM_BKL_GHKwRSadQGynYKYMl-dh-Q4oEEUaaO2ZXd5Gv8p_dHmu4dFCVE-ZU-EE8S6_0TmVKRyKc39pdAGNKey0n8SJk7tzUn2GbBxV6bmg0JQaTTKMoHdp4bD84km1pchxRGAsyNH5MUPbXOUuGInSKP-_S9gqOwDzJM65ipWtL-fyeeiECC_6W4bzooFdoGWidZ-3WjRkfm6dRfoEt4KEJp907NGzQD0AqFZ2TIljlRMoQdyj1xqa9M-p76CN6A6Lq9NhwYbIR1eu3qd9TW5V2PwhCOZ3UCE6ub13gA9Ba4M_vz88wMJ3C64O8hIzpD2SsNhHyaP3gdqTQWEolAQDxXAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pnCdCUmRvVV6xF7n5Q6YTLf-nXE2ECXUQj-TsrUsfWtSgTajMxMsrx8H4B96qkLsbbcWHW1JQrjlmyhou7n9IJIrZKbAeyK2VYIBOTZZgKPEQ2jTwDNU5VMFZXjKuzyoZXTgaxCeL_1wUrI9npwVPVQqcJnpFPNO4dLsIntW2C_tEk0ipg3TUXeutMlW3PfsjgdbxMbmvl1KPmtDg_LxM_COdFE9ATgCC_RYseNroXHrtH7CKNOt5mTewj3HGz1VuVuZtX2wI3MgZtFymgM8WFHteN5cEL0qipSsnfHYv7HNAAln326sm2BVW68T192VDh4nzIFE91RgDaebSrTQSYTSmOEnMHf3_iIPwFQsOHsalJ2sRqTKy4SFEfHuhAhBuNSgLVxjzozkLCpcV7Oe7zXG0t3bajgWoONowvI6qVtO_ANnFkOURnDcNSTPMrJcR2wYQiR6gxzvTzlbfemW9dNzr8ivKfqU8MYXAUk-X1RSjlBd_OzARuuvy0P_eQXtVfpoBrlQnYeSYn9ZYuXr0_WdC38jfHdlw1uS7nToZUh-nfr7tWaHSHet117FXripALVmFPKcG0eIBoF2JneoSGlcTQEtNaKkrjCjqjeBemD7_4DdjFY-RI7PISd1qC2DQTrmhvfa6shC0Kr9SS3M7uxxQuyuEg7My4j9lzc5rwE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=pnCdCUmRvVV6xF7n5Q6YTLf-nXE2ECXUQj-TsrUsfWtSgTajMxMsrx8H4B96qkLsbbcWHW1JQrjlmyhou7n9IJIrZKbAeyK2VYIBOTZZgKPEQ2jTwDNU5VMFZXjKuzyoZXTgaxCeL_1wUrI9npwVPVQqcJnpFPNO4dLsIntW2C_tEk0ipg3TUXeutMlW3PfsjgdbxMbmvl1KPmtDg_LxM_COdFE9ATgCC_RYseNroXHrtH7CKNOt5mTewj3HGz1VuVuZtX2wI3MgZtFymgM8WFHteN5cEL0qipSsnfHYv7HNAAln326sm2BVW68T192VDh4nzIFE91RgDaebSrTQSYTSmOEnMHf3_iIPwFQsOHsalJ2sRqTKy4SFEfHuhAhBuNSgLVxjzozkLCpcV7Oe7zXG0t3bajgWoONowvI6qVtO_ANnFkOURnDcNSTPMrJcR2wYQiR6gxzvTzlbfemW9dNzr8ivKfqU8MYXAUk-X1RSjlBd_OzARuuvy0P_eQXtVfpoBrlQnYeSYn9ZYuXr0_WdC38jfHdlw1uS7nToZUh-nfr7tWaHSHet117FXripALVmFPKcG0eIBoF2JneoSGlcTQEtNaKkrjCjqjeBemD7_4DdjFY-RI7PISd1qC2DQTrmhvfa6shC0Kr9SS3M7uxxQuyuEg7My4j9lzc5rwE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hbuGRv8CYABbpsLRgKCyJ4in0TFdv0Vfqz7WeOgdwXR3c1EoaJeUtTBV0rSpfj-EzRdyUI7BzYQsPtgxmSARMtS5y92Hr-VxeBvWne8kbJ4lgMZeQTP5JOhnRf4whtHDwrSRd6r0Gc5X0MUSyK2pz0rPLVSx6yirxaJLpJR4Uz2M6fjXhpc2QTdRLVFTUnsMIRgjWMTStpRRgSPz_AP1T2KYmyBE3f-vdwPXZax_Qmt1MFFZz9yFz1VdLEsVBYkUoorPScA0-3MheUMcIC2YtSXUyiBttZm_6icfdrYB-PcBr9cm5tXF6y2FIxbKoeyvNtV9E3fXKExIyPpRDbWQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hbuGRv8CYABbpsLRgKCyJ4in0TFdv0Vfqz7WeOgdwXR3c1EoaJeUtTBV0rSpfj-EzRdyUI7BzYQsPtgxmSARMtS5y92Hr-VxeBvWne8kbJ4lgMZeQTP5JOhnRf4whtHDwrSRd6r0Gc5X0MUSyK2pz0rPLVSx6yirxaJLpJR4Uz2M6fjXhpc2QTdRLVFTUnsMIRgjWMTStpRRgSPz_AP1T2KYmyBE3f-vdwPXZax_Qmt1MFFZz9yFz1VdLEsVBYkUoorPScA0-3MheUMcIC2YtSXUyiBttZm_6icfdrYB-PcBr9cm5tXF6y2FIxbKoeyvNtV9E3fXKExIyPpRDbWQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=MXNjOkHZwtpAccXfcYVhHE7GQ5s2ZebTuxbTViVzhywRUk6f7mVXeIViy8DlkNjNVHnnXOCLlmd8hFT52RUYI2flJ9m0up2eLmKQhYfrypJafxPhubcylonCOTZGkRVEs7feho8UELtgAzQ06BWv0SLw1NFBxePObPLcGS8WVY9ZlsyVwzJ0WfGNfhEHylf_4JEynfe89BMwRVAfRqe8rtGxGnHK6Dotwbc2UuxH7F7wHckD0JF3S_CqY1CB9oRTXjZyHpdXz-mmUi1xy3PxnPZZIC8M_A52sfYgt6cORRafFSmy3Mt8_e919EwzKdNHJY-X3SHnLmupVMfuB61nGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=MXNjOkHZwtpAccXfcYVhHE7GQ5s2ZebTuxbTViVzhywRUk6f7mVXeIViy8DlkNjNVHnnXOCLlmd8hFT52RUYI2flJ9m0up2eLmKQhYfrypJafxPhubcylonCOTZGkRVEs7feho8UELtgAzQ06BWv0SLw1NFBxePObPLcGS8WVY9ZlsyVwzJ0WfGNfhEHylf_4JEynfe89BMwRVAfRqe8rtGxGnHK6Dotwbc2UuxH7F7wHckD0JF3S_CqY1CB9oRTXjZyHpdXz-mmUi1xy3PxnPZZIC8M_A52sfYgt6cORRafFSmy3Mt8_e919EwzKdNHJY-X3SHnLmupVMfuB61nGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=dFRfh77ah0yo1AsONULAe8AzAuIf3_upzLYaQHCF_7UFiYZXadtLyhsMxO1tZWUVsCclBIR-fpG0P2dof7gL4CBPJFzv6glc7c5aW7XmnCNgxu03TRFkTBgLeawAjHl5E38bQYDQ-710lpSda0pNJsgPiGLZ4LjLD4YyCFgou4KETi4RqqNTagpNPaSkLRhRCEDYn4oDshPPyOtlNx2gROzXImUXBt8283xPfbbBCuOLzMeSXd_RP_eWrMy5anhSlgsGaJ4TU3UrBpXHpWp110kSVDXEWZGe7fATmtFLrA1Y4-38ymW5NYpN0QnpPUQhKz8aWmZkZii5u0eHO2LW_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=dFRfh77ah0yo1AsONULAe8AzAuIf3_upzLYaQHCF_7UFiYZXadtLyhsMxO1tZWUVsCclBIR-fpG0P2dof7gL4CBPJFzv6glc7c5aW7XmnCNgxu03TRFkTBgLeawAjHl5E38bQYDQ-710lpSda0pNJsgPiGLZ4LjLD4YyCFgou4KETi4RqqNTagpNPaSkLRhRCEDYn4oDshPPyOtlNx2gROzXImUXBt8283xPfbbBCuOLzMeSXd_RP_eWrMy5anhSlgsGaJ4TU3UrBpXHpWp110kSVDXEWZGe7fATmtFLrA1Y4-38ymW5NYpN0QnpPUQhKz8aWmZkZii5u0eHO2LW_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=N0FpbERT3O6i9uDp4ZxIfvax7x4EjpV_qjT9G5YJ67-boTVVIfRtQKIBDWrHOkhc5-b1Ube1Q0GKh54hvK5sIxtLXfp_OL81QGwr9ryPFfBUp83wsNZHEa8WmYgoNY29MZ1764F7F-5newOZCoWOmmhmS5yp5_rDGmMWIViCGYoUsjXBM0w07vY4HD6a6WzpFG_zVGCz5Ii5PJj25t_gegM_xU05ZSb4YIRUoqaelTPLcj5sTzffJ3KCYNxI0Ni1HhK-t37Z2o5ECM8O2VZSiXIAChY2WOeR9saUDQJ7jlU4XeV0Al8vfXyqt4WgE3fTcYXZ_YWfRGj7QFIcW0-pzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=N0FpbERT3O6i9uDp4ZxIfvax7x4EjpV_qjT9G5YJ67-boTVVIfRtQKIBDWrHOkhc5-b1Ube1Q0GKh54hvK5sIxtLXfp_OL81QGwr9ryPFfBUp83wsNZHEa8WmYgoNY29MZ1764F7F-5newOZCoWOmmhmS5yp5_rDGmMWIViCGYoUsjXBM0w07vY4HD6a6WzpFG_zVGCz5Ii5PJj25t_gegM_xU05ZSb4YIRUoqaelTPLcj5sTzffJ3KCYNxI0Ni1HhK-t37Z2o5ECM8O2VZSiXIAChY2WOeR9saUDQJ7jlU4XeV0Al8vfXyqt4WgE3fTcYXZ_YWfRGj7QFIcW0-pzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Xov2trRz9cyotSvkcgdqk7B-uVCCg_JVDk2GH56PoU2qk8mlkoVfceV9c2ZgpadqmHnLz_jIADjo4A0fvQ7XmHm6AxwraATnMrpBJi_JiUFIRuq-nw7CtbO1KPT1lPiF9gfyrdwY2WzRTm-0dkFX2_5rCOZva7Ed9p13JfTSXpv1RjPtw5rsmmtZFoQKaVgVRnQJgCrZaPh-mgXEOTSdDIHT09nn5ral2tU_SXiiL8oCHxEUJSSzzLhJhmhw20EfcixpjmBPugdrBXRUs8IjvVWuikNVqwhtXI3fn8ngfWPngbUKQCO7rMyvpV5cFzgN0uajMyjPy4bSa1fTdvlDKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=Xov2trRz9cyotSvkcgdqk7B-uVCCg_JVDk2GH56PoU2qk8mlkoVfceV9c2ZgpadqmHnLz_jIADjo4A0fvQ7XmHm6AxwraATnMrpBJi_JiUFIRuq-nw7CtbO1KPT1lPiF9gfyrdwY2WzRTm-0dkFX2_5rCOZva7Ed9p13JfTSXpv1RjPtw5rsmmtZFoQKaVgVRnQJgCrZaPh-mgXEOTSdDIHT09nn5ral2tU_SXiiL8oCHxEUJSSzzLhJhmhw20EfcixpjmBPugdrBXRUs8IjvVWuikNVqwhtXI3fn8ngfWPngbUKQCO7rMyvpV5cFzgN0uajMyjPy4bSa1fTdvlDKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=V143tVdM5iV7iz8Zcivw4YUtQvcwNLvxbtWV8GKJsczNMZy9uxvN4HHow0z0I_AmlWmSC13okcgeLWNIZnrijlbjjVQQaMLebpc9k_uKSi6XYaZqZGIXcDnw-s19a3Wm-_ysRpFEFD_eiQkFTfJX2qs0loDUZ1iJ5-ILWip9gD8t5eihAWR3arYkuFHY-uWcBK5HniGX4mx511ClaOE_oK4YdzYH9Dto7wM-EpBBVzhlgMf_9xy68sBKn9jIxZ-q77D7nKQhPuQlCF5cYzWQlKl87ImyE6xjlPUjN6WSD1MVOygJiuxCwbCl6GMpXWYASbVVpuW_9AG-CtbeENSbUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=V143tVdM5iV7iz8Zcivw4YUtQvcwNLvxbtWV8GKJsczNMZy9uxvN4HHow0z0I_AmlWmSC13okcgeLWNIZnrijlbjjVQQaMLebpc9k_uKSi6XYaZqZGIXcDnw-s19a3Wm-_ysRpFEFD_eiQkFTfJX2qs0loDUZ1iJ5-ILWip9gD8t5eihAWR3arYkuFHY-uWcBK5HniGX4mx511ClaOE_oK4YdzYH9Dto7wM-EpBBVzhlgMf_9xy68sBKn9jIxZ-q77D7nKQhPuQlCF5cYzWQlKl87ImyE6xjlPUjN6WSD1MVOygJiuxCwbCl6GMpXWYASbVVpuW_9AG-CtbeENSbUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=E_-ogz3b4JCw6kNbeta2ZgmjLyhIOlUaPpFphBqDZ9t-Y5mFpWlD0CdzZsy3HRD0yjtE0rqHsC46Iluqd9TtH3miWrx3i74-fmxpGfo-yb3C9ZLlbFqgJInR-GkiGaqId_jwaa0pN1gjQO_p0knkZhWEPbckY9EQgS9vk_F06_OVpNvr-tFzC83zeyVqHCREh4e_fFg3HlN2TlZ4Z7swK4A_pVx1bx8sp3s0INBn9rnYMmUHO9WfmXn9uciPb5h7UkU-38v96SumkV_DuIXrMKdduYE82vQi8l3m7hfjD2szYW6-5HlVijiL6PbF28dqZdAAt_RR7bi26X2BfOU8DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=E_-ogz3b4JCw6kNbeta2ZgmjLyhIOlUaPpFphBqDZ9t-Y5mFpWlD0CdzZsy3HRD0yjtE0rqHsC46Iluqd9TtH3miWrx3i74-fmxpGfo-yb3C9ZLlbFqgJInR-GkiGaqId_jwaa0pN1gjQO_p0knkZhWEPbckY9EQgS9vk_F06_OVpNvr-tFzC83zeyVqHCREh4e_fFg3HlN2TlZ4Z7swK4A_pVx1bx8sp3s0INBn9rnYMmUHO9WfmXn9uciPb5h7UkU-38v96SumkV_DuIXrMKdduYE82vQi8l3m7hfjD2szYW6-5HlVijiL6PbF28dqZdAAt_RR7bi26X2BfOU8DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSDYzvRbFOJr1FQFuAm3QQ90Fx7mrMG5gBjdmcJ6RZEn-xW-xtCEnzBOMXrb9KTo8o4KgNg7x5rXaag_DtXsfDIbOk-vustNy3Gdkp1FJj7JuLnexStwEGEx1SS-x7NdtxQ7Jnaho4cvZ3p0YfN8a3BOykL5o4AbK9R-2e-z0NqBt52AD9mtwAUQohVrC0Dr9oIphTQBm3WuDRHoU56w0zw1ZP6SZhIzvusDYo0wgEVg20FLZYKj2jOHYl6cALlkDjePYQFbBAVewN8uc6l_MmyfBIQ3WR5-Z7m2SgQOVf-HFFakx8Ri_ZQ9bQSJ2ueqHJLz7gZFOKFXDlwghzP3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=pZevwVgXJNpxBsWg0fub5gbDk3J6tDcwuuHY3l6BM8892e_uYZiN5L85rRO8CIDgTIEpPaLJmOSVMqqdHLPk04eybmflrLWeu7cP2sIUNnikTve3P_ByBew9tFJiRmGJnbhfW8bVSSBNhNQkbHIq3X1hu707kaX0tQDIcsOOav7jRkb6AKOZ3N474T2udTYcwHHevj3-3Uy9DgmVy6Wdq_zGm1dqdtRBbWc56qjZJzgsBDnYgjV8zNWf7dJ4dnJ9LYjPJlBcSRGMNbnhgwAh4-6hx_9hqdAmfkvF7DXdD7lehh6NwKwW8oh7IKIPyRvvc4iqF8PJ5eIxxWCgpBdM_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=pZevwVgXJNpxBsWg0fub5gbDk3J6tDcwuuHY3l6BM8892e_uYZiN5L85rRO8CIDgTIEpPaLJmOSVMqqdHLPk04eybmflrLWeu7cP2sIUNnikTve3P_ByBew9tFJiRmGJnbhfW8bVSSBNhNQkbHIq3X1hu707kaX0tQDIcsOOav7jRkb6AKOZ3N474T2udTYcwHHevj3-3Uy9DgmVy6Wdq_zGm1dqdtRBbWc56qjZJzgsBDnYgjV8zNWf7dJ4dnJ9LYjPJlBcSRGMNbnhgwAh4-6hx_9hqdAmfkvF7DXdD7lehh6NwKwW8oh7IKIPyRvvc4iqF8PJ5eIxxWCgpBdM_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VFSEuTcsf4GSQ93EpOdAEO5F-S0VBKby0-KOUjtyJgxqk60HtszISSgi2ZKOz6w6S9xsa_t6-2VX_G-n3soHvuOHOMdWCYMLLEtZApWjnekswu5QnmqzPSfBkNlXc5lDPE7YZ12PmdNTZd40mOfouVmyaYF0R7tAv9Yz_3_8JL4eBCL7pCjggDu1w0j0woS-On-NI37sc1MXdgXmEN2ljfcX9jXTLsTNszPAj5IYKXMgbxXaJcZfutik32REsI3wYRkKLL36kard-vAw9SoxhHjqOwCCDN9Pe_uteE_SYpHw1_9Yi1gEtswrzqIgsw5ItLZeUgnVRI61qGrdPw64lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VFSEuTcsf4GSQ93EpOdAEO5F-S0VBKby0-KOUjtyJgxqk60HtszISSgi2ZKOz6w6S9xsa_t6-2VX_G-n3soHvuOHOMdWCYMLLEtZApWjnekswu5QnmqzPSfBkNlXc5lDPE7YZ12PmdNTZd40mOfouVmyaYF0R7tAv9Yz_3_8JL4eBCL7pCjggDu1w0j0woS-On-NI37sc1MXdgXmEN2ljfcX9jXTLsTNszPAj5IYKXMgbxXaJcZfutik32REsI3wYRkKLL36kard-vAw9SoxhHjqOwCCDN9Pe_uteE_SYpHw1_9Yi1gEtswrzqIgsw5ItLZeUgnVRI61qGrdPw64lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=avICNoVgWhNhkaqVpuP8tWAJGZa4lmjJm0V39Apk17ZoRUlXp0Ll6fGGRhHN3dgswL2SnUhAmnUElqueylgBqssNhxNO_0fmCIk7zAD1QHF0DahUlLpiKWBjvxdWKggeLdEaq6imTdsrWgBXFtCn0egPZt5FFFQckwvUUxNwcn_1WjgBiCqRdUZsshw_k7Q77LXgSEdBsuCQI0TnG8sJMCKtBrwFJTqgKgCMGk6xJWFftDSm-Kwvu7EEhS9COmsWfqVE8RSO5CpQnUClwbm7zu_VOixcSlXxL4yhb0CdR2C001xIoLD01X6PlXrWvGd3wWj0dhk5ImeQd090AY6UgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=avICNoVgWhNhkaqVpuP8tWAJGZa4lmjJm0V39Apk17ZoRUlXp0Ll6fGGRhHN3dgswL2SnUhAmnUElqueylgBqssNhxNO_0fmCIk7zAD1QHF0DahUlLpiKWBjvxdWKggeLdEaq6imTdsrWgBXFtCn0egPZt5FFFQckwvUUxNwcn_1WjgBiCqRdUZsshw_k7Q77LXgSEdBsuCQI0TnG8sJMCKtBrwFJTqgKgCMGk6xJWFftDSm-Kwvu7EEhS9COmsWfqVE8RSO5CpQnUClwbm7zu_VOixcSlXxL4yhb0CdR2C001xIoLD01X6PlXrWvGd3wWj0dhk5ImeQd090AY6UgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=CvopW-JZgDclb2MgG8znd1eFGSbGmxSF3K2EEw0ZAQ4YXDKDJ879DefO90PYfEsfxDWysAu1to5I7cSWT5iD63IZKxqyDxSjnLVoVMXzbhzCz6BWUUCbf5Z2D9GzbWQ70csG2pCSKlUAujagpTh62xdwzt0iDyfZKsdJtOb7Vr1yg0KbcrbLVgMzlLRR5bAWsWJZPPY7Fy2SH-VBbw6GYngzIuqu9Fmwx9kSYmrcG8iQBGCrl1qT6rib8gZNkk6oYG9IwE8xBlKNEou-mvyNMnMvwcrL9CEOkFMjVYwRa9ty7wiT1-Cn79E2SMRvpOpwnDpKXg2bEC2aL3VBYpjXYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=CvopW-JZgDclb2MgG8znd1eFGSbGmxSF3K2EEw0ZAQ4YXDKDJ879DefO90PYfEsfxDWysAu1to5I7cSWT5iD63IZKxqyDxSjnLVoVMXzbhzCz6BWUUCbf5Z2D9GzbWQ70csG2pCSKlUAujagpTh62xdwzt0iDyfZKsdJtOb7Vr1yg0KbcrbLVgMzlLRR5bAWsWJZPPY7Fy2SH-VBbw6GYngzIuqu9Fmwx9kSYmrcG8iQBGCrl1qT6rib8gZNkk6oYG9IwE8xBlKNEou-mvyNMnMvwcrL9CEOkFMjVYwRa9ty7wiT1-Cn79E2SMRvpOpwnDpKXg2bEC2aL3VBYpjXYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Csyb_ujTHnXZJ6v6Uf79M9-rZk-JRSEeHgObiw1jhHRbsEl6GmMeb3jGZB6R0iQOULBIxYcoawDc0WDAfGO7ph7Zmb42-y3Rtq1OlcDX5OYT9l5b8edrhf4UeHN1KjBedR8LxJe0nY0uplIEZxsJdv5RDDQjlkM1qwsghDfR8V5ALCrwIUR6QbN4Q6f0HZwZ1rQjdqcWw-fYJb-uvKFOINcDXg5JDiCMusq2YJH13nrriMfqfGyYZqZ2F3lMaXxjCvryuV7z7XvEYL4itePxKSfRgZRomlgekcgJpEuW_4TAt90oslHbmXsOi18EXJm5MgFnVQhWPC8fv2_Le3BLqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ObSfo-xLhDStQdNE9lIUe72CKt18Zk0NJDXmQ3qEPbwJxhw_Fc_OGjKKOUsEPH_hRD0e0kF0AQnDrpiPXu0itBF6Ds_vqEYrXjDdGcVW8Atd_bm6eG8UhY3SaxmQ5Aee-A1Rj6Uxe5FT32t1B6Mzxi1SpdEe7u71zwKCk6WdNoZ3vBhUDyF1unurZZDjfmEYmJMaF-xGlZ8NSIabMy9snNqWVo6d5GVfBZr_yVEbt_jpukpzcSblzhxiOtdKBY12_3gBtWJngb3_Jg1L3kZJfZ05SVMQT6BbUI775aDphPQLcDr1vMwWxUAPkBXd3UCHYcChsaFbNH2nyJ3mN0AnlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ObSfo-xLhDStQdNE9lIUe72CKt18Zk0NJDXmQ3qEPbwJxhw_Fc_OGjKKOUsEPH_hRD0e0kF0AQnDrpiPXu0itBF6Ds_vqEYrXjDdGcVW8Atd_bm6eG8UhY3SaxmQ5Aee-A1Rj6Uxe5FT32t1B6Mzxi1SpdEe7u71zwKCk6WdNoZ3vBhUDyF1unurZZDjfmEYmJMaF-xGlZ8NSIabMy9snNqWVo6d5GVfBZr_yVEbt_jpukpzcSblzhxiOtdKBY12_3gBtWJngb3_Jg1L3kZJfZ05SVMQT6BbUI775aDphPQLcDr1vMwWxUAPkBXd3UCHYcChsaFbNH2nyJ3mN0AnlTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=i4vyMMFsAKicD7IKUn2cSkEHAWv8Jmn6lvKEQO4rYm1F423ypg1L9KyegXcxjrLzBq1aQAtubZnOOCvdnoDm4mtHp-lsl13EnNStioT-0pAhEI2SEdjjfpvwej6pxTvUhLlW8EmRokAERSwLqMDaKpOA_m6Yt1jAVvEcluerp7n1K2_LiW0rMReG1MS7STxpxlCLwiTWC7mzjQ5mmkecyHX7_2pZa7yD9seuPaoiZJCOe8HFSGlZ4-1-gPOj_dHgmc7ZtTMxcLQAMwyKiaOoSNcO4W9yxbRfFFuMAfZmjF0HpZw6aGWLZAUg-Dh8qQzCkeGITgqIIuAuCqJkK2LwBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=i4vyMMFsAKicD7IKUn2cSkEHAWv8Jmn6lvKEQO4rYm1F423ypg1L9KyegXcxjrLzBq1aQAtubZnOOCvdnoDm4mtHp-lsl13EnNStioT-0pAhEI2SEdjjfpvwej6pxTvUhLlW8EmRokAERSwLqMDaKpOA_m6Yt1jAVvEcluerp7n1K2_LiW0rMReG1MS7STxpxlCLwiTWC7mzjQ5mmkecyHX7_2pZa7yD9seuPaoiZJCOe8HFSGlZ4-1-gPOj_dHgmc7ZtTMxcLQAMwyKiaOoSNcO4W9yxbRfFFuMAfZmjF0HpZw6aGWLZAUg-Dh8qQzCkeGITgqIIuAuCqJkK2LwBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpcGJfhd9HUYpiC2Ie1YWC8DUhhRZssW7LgY0Jg7n31HYdRO7LFOuwiSyMZvr7G3l4HcYU7pmi8Dbk7GgRqcL39xjuAsHxK2l8iOS9YS5NeY4Rwryxbv2igzw03_h2-vgTqX5yg2xVpIo0F2ifjqD5t5hlfsPU5393pqCGyzFLSEu9bf_cQLWf2-xnoGMjanP2ZcQIax0afU_SLOHWI4JEvkAMsB71aMidBHUn7XIhUscagCn9MZtrnf7SiYCWNer5CmkccNfLGhv2rSJKf6iI5X1qEzpRKnstssX0EqkSTzfNKged5A4f1ylfMC6gqHoOZxIgLI8ZE8QPeCyNhBJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JDrzuOrSKfmxo22h2xPtTWw0pme110q3-FSye-2JBjtuPeQVCzjoFjhowBTAoLQKSuBkLjzvSkNZRDTmbwPXGF7XFBjKUcLBx8UfNSCW2FxtyPHdPr4-a4Pz_z94NBUKjNv-vjJhOgW8snxmCgPBY6sITFSsEaodV6yx2jtNeOs4fpWnU6BCzilBeajf-KntJB_PohbwReSQ4Zj1cVzhKSaOFfTNtKFlfCy-WDjBTdjXNqlA26tQomZ2awFC_KcvQikGeYt1xVKQat0MRiMcIqsp8aQXxNIiyxpic4jb8H_GSteMUS3VTwPvZiuHmh7PI4oWuWNpCb76AqHNVq0NDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=UwjXsI2sEq_v6570CMdNr4RAXOqmuza828OWUK0t6aKK0H1Oo6Z9lOouFzcPVdbofFAue-3EMQQZbpzvUV_nt-AAyItdQ6jVCqDbZHvRDn2kbvWG83Fqr0CUdM_lu7ZD4lZHWlNI70FK9UutQGatjm3_-JDhbbA4BlA8-HBmQ02hxKn7a4xkmlD2NxmA53fvgJwGtlw6GfaOReq4AM3fKPIlIWqespMAGiPsCRYlJAWyO4EkBdI6EXLzMBww8_b4V5xUfykJDGZ49CtcX7H6rCJgBEnXPq6KEiFOXhtpgXy0BUj6t4-PUc9aMsyr6YbHVQuaAUrSCj_BQykqDkVy-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=UwjXsI2sEq_v6570CMdNr4RAXOqmuza828OWUK0t6aKK0H1Oo6Z9lOouFzcPVdbofFAue-3EMQQZbpzvUV_nt-AAyItdQ6jVCqDbZHvRDn2kbvWG83Fqr0CUdM_lu7ZD4lZHWlNI70FK9UutQGatjm3_-JDhbbA4BlA8-HBmQ02hxKn7a4xkmlD2NxmA53fvgJwGtlw6GfaOReq4AM3fKPIlIWqespMAGiPsCRYlJAWyO4EkBdI6EXLzMBww8_b4V5xUfykJDGZ49CtcX7H6rCJgBEnXPq6KEiFOXhtpgXy0BUj6t4-PUc9aMsyr6YbHVQuaAUrSCj_BQykqDkVy-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
