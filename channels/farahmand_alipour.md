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
<img src="https://cdn4.telesco.pe/file/LiM9y70T67uES2dHp7-j85rNy85kESQfh0VCNkzBuZECpkEOmsB88Ws2Jrf7DfNMAP_nQ_qIw6kCFLFRt9qI47j222p9Mybf2F9OYL6Tw88hN0PhlXBliKJ0D8gmy2tPExFY-P9rV1CeEVd5G3Q-xxUE8UBrj7lR-S6mF5iOh3-U22xCd69UAV49qVDxYT3g818Z2jKxvBrkftj2PmZOiVwUfC59SrwA6NJ3_gZuEjMafdMEbHtPR7CzPgKRFGBB-rQtsFfOEb7XM8Fx8rTns5ry7AwzZLKp52RQyY5onAY5s02exUe3BVTmu5kDkLj92HIlhT2A3hYArUc-UfQSGw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 03:10:30</div>
<hr>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=HXAbnLyzHE8BgeIOI7wUN-Vig2tFSQNeU39XenrHiA2GOpbqwyXuJVLuCPnx6h1m9hevHCT3KcXnMWzFwxLczi6iWK-QIcTfTojgmQrXypGjgmkbXqdr9EWrarxStBgyoX8x-dH5UKpvqIefmea3IVa4Q7ygXWAUWfAQX2oT6Du-_U6TGG8mosZjRkWHrPEhQZv9n36hUV5wjOI7qBdgko6vacZXuhgkHrUGeWTNH5f5GtqKc4X4acFBE1NO9lwV7sKBsxMlxN2lNikvBbbWvJGgbTULTA-ZLjkfQJPkyFpaRMeUcwhHY92gRTLK4oEjwXE7EpDoPDc9m8rscxyy7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=HXAbnLyzHE8BgeIOI7wUN-Vig2tFSQNeU39XenrHiA2GOpbqwyXuJVLuCPnx6h1m9hevHCT3KcXnMWzFwxLczi6iWK-QIcTfTojgmQrXypGjgmkbXqdr9EWrarxStBgyoX8x-dH5UKpvqIefmea3IVa4Q7ygXWAUWfAQX2oT6Du-_U6TGG8mosZjRkWHrPEhQZv9n36hUV5wjOI7qBdgko6vacZXuhgkHrUGeWTNH5f5GtqKc4X4acFBE1NO9lwV7sKBsxMlxN2lNikvBbbWvJGgbTULTA-ZLjkfQJPkyFpaRMeUcwhHY92gRTLK4oEjwXE7EpDoPDc9m8rscxyy7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frdnezwfe6dK24lx2DR6Frc9c6TQo_eAE7f4ykAb5v5ZT9NS5PO7xhkPsITr7dyNhIeKUF1ECEYZlLrlfsOQz9BpYdVY4ZlTkUxpX-EW-t5f4XdBhc8Nwml9or6lDJAie-JGRyPwLmpkt7-72oNx7lueCi3LSnpW4it-yuIBp984bw41xuUuXMzqC6U4zTNZQ9Kp9cBJLAjglkbTM-S4EU4RtaNUCk7SUSkjIYzabyYp1EeLUCUppfWPt5H9aIrsXo-6L2MqbF-F52qqOE5bl9fVavmvJJAn43LY9ET4Bt-mFw22ym_murXzcZYMnGpDHPVLvcjDG4qlsFcTUMgSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD6eBFiRQ94BoEAXNqoK0YVJM0vaWDrRuuntHikuKMxpVm4-eOkOhdC20Fs52R1t59cyQDMZCnQytihtj6j3B5Pu0b9qkxU9uDFBtI2MyX0Je8cfqHraDiAcgeG8Y-MYZ-RZ3rlDk_CI3xi5jbel6oxL2OBBr3kKRC81kYjrPL2i7X_0ntalvJpctCukbLz_IdMKWvOOQVcP0s2hAJW54Mx-fcFL4x6qN_HAmwH48J2shF-5yDYnk6ah1OfueqO1IglCUFr0k_fdvyxSJ9s6jQlNZwxV_gkap9EjP2fqh7avAldaKwITOPdwuUR5V70oxaGnv17l475cwAzRzHj2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qx2hQ1bhS_mvHjTN8wezEje-l3IXDbK42p0HxFaXoLLfU-NykP6LVm2I4ZBNtt9_C5ajKnKzeAW4Z3NQYIvkhntsonggL2B02q-CGFQyjtJQFX4Wm5rBXJHYNu_X0_FfvPztuWxFZBndqiiOuf-rq3U4xHzzi_FOUMkkH-7Kz6T2VzH4jjxlss0EsYJxQtAPCiev5VirJp-bPx10G9_whAgnZlt7V2AsSqx18xQAnudB7_95HAPi6cRbWuXSrsEa_p0mB_AWzXnLObmglVBw1pNTQUSxDhbF5DFRdolElE-xSCvUa9WMCrQPLFBZ3xCPqAfPTlc6ktrVmXiVMBLJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bOEt0q7n4FDUaDhHBi4HZSL05ahlAxgr488IeG3RtE1Wen4Yidnnbruz6KIA8Squ2DK0s-1NUp6oulgR9Gf_puHZCotWRRodyScZTzqCqOliSM7k_bSzxCBb5_ZcQf9CRJ-KqVSvuK3OKqQDDhDM3CPz9cToquXgRfp8lKSxRMnsxCOu8MDSt18_fzmd-n4IcAo6EFYUrar0dTgLO2mp-rym08F1UAZrg9brtwTv4Fg_vKzYjPKCGJLslK9Z_fopRjM5eZG115oDaqLzX_PMeIAa7Q2gAf7D-OfwgHFtf7dl4hG2Ee60PCJVU6z2FyQ23iYkEPotEkUWqRfBuF7XCQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAlP4i7G7-b9_WtVV1A-PV5QkKQfbSkzAugkjjTVB9Go862E3PoZTbmDOfToutJ4LPS1ICV42M7WtWZ50UWsZZojL7zx--uQvfXBanGP57m0P-cqSS-BzivwcGUTE0TiFzkK9TYPlX0svvjF7kFpdLo93dhlDVp0FqINYacPWLXAch8BjqyWtOYX4QRXcZfRJrwVNVa3SPSylER5uLXx346-vscbaZr2g7Bwv_3_Y-WpCEmvbpzRJyLzDoyug01NZMneND93ZPEXS5NtTJtFvd5heH9vKXBR9Z0wQTS_s_iMahNvadkZazW4W8aeV7Rh2B5ICSZLAKSWi1o7C1eCOA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpdsHrxs5IrQM795GBNsxMNndaaiWmwYwnyhDBAi-Sbc-idzg8x6xIzEI26IgLTRV1prVsgdaq5P6QP3K1Y6lZ14guCyTzJRJ1fTDCcqnVrzTYm9IglbOWnRW2nmjz1VC2EQTCyLf2L1RSvovE31yW7c1tcder069D2FT9_PU-xVUhx6jBV3qFVgwQTMosuv8enq0uMXy2sM5ysGFXFgOaTRWV1VSVGMnv--AMv8S7elnQ_We4rrmxzEve7eeROT86-puByVJ4gZXALYYDzR1RlYgjJiXDgLdcoDjtNGx9YTMnBOp36nFrenrNez7ZI2ciSeb9Kme6kuuQri43KqHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=u4EteLHENx9L2LCGCgq5visV5hticpdSVoxWZlaLjxQ3V1vGcKmELdOyeCV4tAfPnTz4OIVqvxAjf-gBnrEjdgElWyFB6UI0S68caulaPzMqDeVka3oi3ERTjQOBLSdAS-KsdRNu9nBaDFMtLawAHLbJxNvnW6FCNjFk8rJ_BpU355FX5wh4A_K4bRUSxFbl8Lcd9YfAvbxdoE66OfdfS_J1pLLboOYy1w76y1MWwXNg897qY2r1TKQIGCHOSEy0oykaN1adctWBetkAe5dSR07HDfG4Fg8G03KovUr1GOv79BVLZ41uw3MwqxeolxRj21QBdGtlU_hlgwWP6TCg4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=u4EteLHENx9L2LCGCgq5visV5hticpdSVoxWZlaLjxQ3V1vGcKmELdOyeCV4tAfPnTz4OIVqvxAjf-gBnrEjdgElWyFB6UI0S68caulaPzMqDeVka3oi3ERTjQOBLSdAS-KsdRNu9nBaDFMtLawAHLbJxNvnW6FCNjFk8rJ_BpU355FX5wh4A_K4bRUSxFbl8Lcd9YfAvbxdoE66OfdfS_J1pLLboOYy1w76y1MWwXNg897qY2r1TKQIGCHOSEy0oykaN1adctWBetkAe5dSR07HDfG4Fg8G03KovUr1GOv79BVLZ41uw3MwqxeolxRj21QBdGtlU_hlgwWP6TCg4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=X-P1v-XKoNxlMzrx_KnHRaSBu13ccMRa9Nxxuupj4SaFTpV0zrnz3n1zIYSD3VLt_RBPIe4_5GlOZ20VeUR8JFTM9539cIHNjK_CFU_8kfaqnFd7fH6LceLGTQmXcf3lR5ve-cXjEM0VuTlx8611w7nHOF7f_TmPlJqtKrEq8yDavGHNxVhEyp8iHzSgXTAA_YJzNqoOzMV9mAmxwD4Mj1Dvv90Poe2kVyyt8N0U72Ay0a_P7rGma4737q1WIjaOvwYQpoGn1iVy-Ig3I7bQVr5AB-NLqEspq5fHQiasfVChfli7Vv2VNxn5fDWfSmfUmwYN8uZ-wFvmU_cwrw2711Z2fBUxGVui8QDQoDQlREoR8i4bJ3OadgJXyGPx95UPvb8EszQg-_wjHl3wNHHTetw9qe8vc7N1z7F1ArSRjymfhQ1T0pY48JZtUz2JEAbxioBVBsQI3OrT8eTnE2H-oTfqhdXiLGtE33mEwz0_5RQ8h6qUmg-Z8JTKuZ0KNi23lrXeYDiE4NG7Sjq6oxUaD2jGdOb6nX6IyYS6QXveEwRsXcvnwqvfB1nOdmvdXTI-tRnwu7Gwhi6-Y9lRquHOFecHw3wjIZguWy60hoao-3oobYfznFqGJF8pGr858xDbnwaAlOAWHK8lNlKshFk11TSMRiuFpbkJqQiqlkKaQx0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=X-P1v-XKoNxlMzrx_KnHRaSBu13ccMRa9Nxxuupj4SaFTpV0zrnz3n1zIYSD3VLt_RBPIe4_5GlOZ20VeUR8JFTM9539cIHNjK_CFU_8kfaqnFd7fH6LceLGTQmXcf3lR5ve-cXjEM0VuTlx8611w7nHOF7f_TmPlJqtKrEq8yDavGHNxVhEyp8iHzSgXTAA_YJzNqoOzMV9mAmxwD4Mj1Dvv90Poe2kVyyt8N0U72Ay0a_P7rGma4737q1WIjaOvwYQpoGn1iVy-Ig3I7bQVr5AB-NLqEspq5fHQiasfVChfli7Vv2VNxn5fDWfSmfUmwYN8uZ-wFvmU_cwrw2711Z2fBUxGVui8QDQoDQlREoR8i4bJ3OadgJXyGPx95UPvb8EszQg-_wjHl3wNHHTetw9qe8vc7N1z7F1ArSRjymfhQ1T0pY48JZtUz2JEAbxioBVBsQI3OrT8eTnE2H-oTfqhdXiLGtE33mEwz0_5RQ8h6qUmg-Z8JTKuZ0KNi23lrXeYDiE4NG7Sjq6oxUaD2jGdOb6nX6IyYS6QXveEwRsXcvnwqvfB1nOdmvdXTI-tRnwu7Gwhi6-Y9lRquHOFecHw3wjIZguWy60hoao-3oobYfznFqGJF8pGr858xDbnwaAlOAWHK8lNlKshFk11TSMRiuFpbkJqQiqlkKaQx0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWz38kcX5f03nTUUPnDfulalv07adm8ibcJX-rRAaP4khtCcJ4tblnRdHdqBdmNcLPMI0jiuRPkCGsfZUI3cuiN-jQVMxaQ6rI3tElctflIvAtfH5zor29lmcILXp113gkG0AUWiW727yPM7Ps-8MaSTuP-9PHlYB7yo-fVfoIIZqbswdWZaKv4_lBwo24A65A03Cs-ECLE0fBRfGPevY7OswJrEuYk5EkqfpxYKD-2Kvd59SJkxhHZrsnLt0W6HOOaYlSapkM-PSIea_9uId34aS0A56savb6XY2A01x85C9ua15AMYuDFGMT_7ArXULOHOdrIll_sOR2-Boi6BRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bu9SYrgfJd7rfayTuDKu-iavOPa0gtVIe_G6hdpOiCJzVH58y1H89DHgv-gX3sImtpRO1kUX23_4KjPVtCW_Jv6Y17rB4Qiwjse6DCYs8nDD5RX1Qzcx4DNUmLeZJoWsFcEEXRk24juyPSNOXEsHcPbIydZz7xFcWsdvRHzblO0Bn3P9k44qEfOIC8hnh0Fq7KrDhziMvDq5Gtv3Rafl1AzDo782Wb-vDPOuVWyDOoci_7lmz3nGBZejrfu3QFMAjnsHfWe5UpFkDVoqqRh9TMM-ERRiDSBuyLiSIlupRZYOd4fszRLWEYys7JNs0dlZGCvh7Jnubulz76WO24H0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UwuyG_XBE0yjq9nUvUxYz5JRD0bZiD8J7ozVAiEgfkQSPdS0sH_5vCH2NNSxKgJkN7zKNAPLn0sHO-pvAfcU_p6KgHaOZBP4KEwuc-oea6ugSfz2o26HbdmB5tLZol7fnAMbbVvL6de_4a9xuobbprtES0uUZly6wZxk3t0sozsUSAbTezt4jpBViU7hulDEBzAwCVgQwOGb3VK8Ry8CJutVo6Ddn6KxuNfxUWd0MiniE8IHoCooaFZtqW0oh6BgdQ1vpHf0EmIFsGpS8OTfF7OQDVZYZB-RY6hSKho7WCEAOwhzvf3CelZyfLJldm8bEofTM_KhwmmhAppyiLQP7w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=W8rn-wS8-ZATG-EYOeXPhHTyDclwUjz1Q6-L9bqZ1MQq6kUfXfdNcSnTNnQtqeqcAect_AIU9W0RnC1sAJXPoYSu8kfC4DMNZ2IysQJ93Orq_MEdE9j1v8krnReCOAfVYjj7Hgjq-1aKRZG8VmVjR69-WYUK7ZsDo33Rp9DIyKxVVTc8zedEhJmCCVTWdsHjQwhkMKHGq-Hy_wirmbtoXH5JcPboYQUizURCk7eiE0p-ZVUoMs1VgeZqgK4Jb1CaJRmWfFEfvlHjgtLExarEc-SFsaGkM7CKzxqRhYEIqhkOiKebvPSq1CQl6nLVKf_fLdzjX0TKaRcpxqRRlEFQVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=W8rn-wS8-ZATG-EYOeXPhHTyDclwUjz1Q6-L9bqZ1MQq6kUfXfdNcSnTNnQtqeqcAect_AIU9W0RnC1sAJXPoYSu8kfC4DMNZ2IysQJ93Orq_MEdE9j1v8krnReCOAfVYjj7Hgjq-1aKRZG8VmVjR69-WYUK7ZsDo33Rp9DIyKxVVTc8zedEhJmCCVTWdsHjQwhkMKHGq-Hy_wirmbtoXH5JcPboYQUizURCk7eiE0p-ZVUoMs1VgeZqgK4Jb1CaJRmWfFEfvlHjgtLExarEc-SFsaGkM7CKzxqRhYEIqhkOiKebvPSq1CQl6nLVKf_fLdzjX0TKaRcpxqRRlEFQVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=FAFlT7nEALjQL19YBJgUlrhU5PuvHIIpq96X21LM28bYFECCjLCyW3cXFhNlo7j-Se-v1I-sALJCXf1ogaKMWgFCivsBR6UykYgeSx9qlduicX1m_-Cmj2_slVYoqu0QA_voboLRDLe5tHxWuzZQLObamFTU4vkNT8yF7KXYLqPZrse1-xqFZG4ZQ1nqOGTkpNQK7b_VfbanCZLIRKLlZFkRVxJLJ-A5RiGeZRbjOdIcZGYP47XC5p4AbyfBKcaltHxpTNWfaFoMOV_hZRxdJ_MVWmSAnoPPLbk44n7j0hQQEr6msL7OYBzKrmD5eXSPrMx8PMLlCgkYvb0OX9gwsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=FAFlT7nEALjQL19YBJgUlrhU5PuvHIIpq96X21LM28bYFECCjLCyW3cXFhNlo7j-Se-v1I-sALJCXf1ogaKMWgFCivsBR6UykYgeSx9qlduicX1m_-Cmj2_slVYoqu0QA_voboLRDLe5tHxWuzZQLObamFTU4vkNT8yF7KXYLqPZrse1-xqFZG4ZQ1nqOGTkpNQK7b_VfbanCZLIRKLlZFkRVxJLJ-A5RiGeZRbjOdIcZGYP47XC5p4AbyfBKcaltHxpTNWfaFoMOV_hZRxdJ_MVWmSAnoPPLbk44n7j0hQQEr6msL7OYBzKrmD5eXSPrMx8PMLlCgkYvb0OX9gwsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mF2BshWIa--zvsiEyLchcu5zWjYx7L5zYTRmQPqDg_ZP7xgT7JSJhFl8aXyEJJFwXSBHgsOCj0h_7TU3deGxyUwBWDJ-uk8ddE1FpIINexuhXyec9yn3wSRWFSnnWPIO7IGlmT5Gtuegm2nDvTW41d-90x398JAMJZjov5vIukDnCkgDKHTlAdGFm1G1zPhn2sHOf70Yxc_xvOoFB6Ee_8XHH20-Nmk5YP5UEi5r1m5F0hiQU_Z9kBobryuDRAVBS_UM2dgu-kxgE5_DjjX3JPTOfUMbMK3CJIn0mNKOaSMN8eUAS6rUKdvtRjxXuYau-vkgZURkc5Fx8BASYhrZMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=elw9qA6GsDzHTPC3C40WuuGAZo47HuKHJL0w05IgXTdYDFnRYF80juI9t5C8qiX16eDmgpAoyshrH_UW9fB30XXgONLoeRA4pThoUhmEd0HrV-RydTn_3IG78wj-pj4hDakqlJohq-1aIsY_ivlXxa_o_Z6u4iccbvKW-10ENiuEjoif76oPGSxY6OnIuywE3DrYn7Rqf_avqa8KrFUZQwoPNdMni6G5PVNZQnlD0icW4bqE-ad12moT7URqR2LvnJIDngAJcyKVxSwPk8Kt8JWk1d4RGPwMtRJmwRouIykl2WfAys8cY9P-7D_x7wn7DITQBtD8sGuxXikL4XQkLqoRybZZ49e8RHiEegDn0uDnYk19SjqsC2KNCQySvzY2lhJPuzWc_BfByHZLwD5hZfhgDrxUYo--zABJK0ECeV2xsfLJFI2Y9gFIXsYf83QqbwJvfKkkh41OGybnQaTPwy04WgYXpZypazGfVH8-TsPv385v-4VblH8E8lJX1IoVW825U4LMpuo5_Q-Aobbjy0tz_ofEY7U98AKdpdXBtEwQJOshWnu3Odxubz4Qo882YXHlCTGu6n4cvlU-2HcGvYkPCi5L-MdoUAl445xw0AORiwweO8xIZo7ms0Rdel1MQv8pN8eHQhZOmNvY4Vw9Cr-AvPSrr_YrkU3CpdbVhSc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=elw9qA6GsDzHTPC3C40WuuGAZo47HuKHJL0w05IgXTdYDFnRYF80juI9t5C8qiX16eDmgpAoyshrH_UW9fB30XXgONLoeRA4pThoUhmEd0HrV-RydTn_3IG78wj-pj4hDakqlJohq-1aIsY_ivlXxa_o_Z6u4iccbvKW-10ENiuEjoif76oPGSxY6OnIuywE3DrYn7Rqf_avqa8KrFUZQwoPNdMni6G5PVNZQnlD0icW4bqE-ad12moT7URqR2LvnJIDngAJcyKVxSwPk8Kt8JWk1d4RGPwMtRJmwRouIykl2WfAys8cY9P-7D_x7wn7DITQBtD8sGuxXikL4XQkLqoRybZZ49e8RHiEegDn0uDnYk19SjqsC2KNCQySvzY2lhJPuzWc_BfByHZLwD5hZfhgDrxUYo--zABJK0ECeV2xsfLJFI2Y9gFIXsYf83QqbwJvfKkkh41OGybnQaTPwy04WgYXpZypazGfVH8-TsPv385v-4VblH8E8lJX1IoVW825U4LMpuo5_Q-Aobbjy0tz_ofEY7U98AKdpdXBtEwQJOshWnu3Odxubz4Qo882YXHlCTGu6n4cvlU-2HcGvYkPCi5L-MdoUAl445xw0AORiwweO8xIZo7ms0Rdel1MQv8pN8eHQhZOmNvY4Vw9Cr-AvPSrr_YrkU3CpdbVhSc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=oxGsuC6iA4aaQmZtaRaaecSe2Qlj8CHjJNV5tRGnHItuzAFPXnoMbCtkno9zK-ck2C6seD1gItUu1aO9IJTB0LQyQ1d_9VqL01KC9wZwyFxjB2p0T7zpiaQbAgIJ7U1l4bvqa7wxYl1TuZYX9PYiZnTUb2agHe8ZMtUd8xZbq6TIeo6DbBzBuSD2GhoewaVG9eeKTqqW7n-Pa4wyFrYiVcXpYWeEoU4cShtJeYcCW2Z3D9Pnuyq99Pef5NHGC0mwY4diFrONdNvkPl9yBUuFO7lWS2KPYGjwAhDSNd52qK3jKbkKoqtvAam9Q0AnUfKzUxfQOhUHAxBZdfNVx3ECqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=oxGsuC6iA4aaQmZtaRaaecSe2Qlj8CHjJNV5tRGnHItuzAFPXnoMbCtkno9zK-ck2C6seD1gItUu1aO9IJTB0LQyQ1d_9VqL01KC9wZwyFxjB2p0T7zpiaQbAgIJ7U1l4bvqa7wxYl1TuZYX9PYiZnTUb2agHe8ZMtUd8xZbq6TIeo6DbBzBuSD2GhoewaVG9eeKTqqW7n-Pa4wyFrYiVcXpYWeEoU4cShtJeYcCW2Z3D9Pnuyq99Pef5NHGC0mwY4diFrONdNvkPl9yBUuFO7lWS2KPYGjwAhDSNd52qK3jKbkKoqtvAam9Q0AnUfKzUxfQOhUHAxBZdfNVx3ECqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMQNWaNYVeTSnW35hi0bNK9RksxrcMk_BuZUsB5wSFpEa9RzUimNErMuzb6qXw3jcaSifl8EQzpjSb4NZUSFZqzNwmsAfe1B1JQ95hNurqCVWEQeh8YZ3q_XH-2MO1CT1BLdFR6QUtFS3-lG4lcOzcLlf0fR1jPrKcz1bgI4WQ2rHIVpz67iYjgEOIfY6InHerssKzisTRH2n7ryQ_X1KdmcezPOmmce-170aDLx-j541Bg2DAcM3T8ByiDX2Ij9BzQq06fz6RwV8JrI2haRtsIpx2JaUHNifuDILzCSB8Ekn5M7viVYDi-WmENFw5Of6HVrF7C86IaZJlw4pg45bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=pijPSk7QGTCvZAUyCf_OU8iMmfU1a5l5OqAR3eN3WHX165xg5VktClgQkN2YScGvdcDQR1YBmzdByxMBSoBJoabllum-GdrNPD6mKYxQydy3dbBaiSvC5WxbXfUqAGPLAPRqD0l-1qa0qT8qp_NcXLEsT1iLtKPXYmxXC260rtkTxt53u5-F8m9Fi7QHQb5MZ1AoCKjtgQURF9yisAy_nCRoYZihV6qcNLpr2xIx1KV7kyDG67uRjNTyivHdz1HrL9srsgYvJeNHfYyEx41SC1sQmgrIfre4cS605m8ti6YD17f7ABn9l5DTRsgivw_xasGA5USI4o4qGuJ9lyMlhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=pijPSk7QGTCvZAUyCf_OU8iMmfU1a5l5OqAR3eN3WHX165xg5VktClgQkN2YScGvdcDQR1YBmzdByxMBSoBJoabllum-GdrNPD6mKYxQydy3dbBaiSvC5WxbXfUqAGPLAPRqD0l-1qa0qT8qp_NcXLEsT1iLtKPXYmxXC260rtkTxt53u5-F8m9Fi7QHQb5MZ1AoCKjtgQURF9yisAy_nCRoYZihV6qcNLpr2xIx1KV7kyDG67uRjNTyivHdz1HrL9srsgYvJeNHfYyEx41SC1sQmgrIfre4cS605m8ti6YD17f7ABn9l5DTRsgivw_xasGA5USI4o4qGuJ9lyMlhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A9aCYg4xOoyoxuA8wG1hyFUQ0RLooTeQ7oM2tM8prCM3Qs2Y6larPmpRmXCow0C0evoyuPtiJcalmTMj17s3seTkKekg7Jki6y3ob7sJuTKtiQ1DJaOAYMQTmw2n6wO_FKSq2md2ZcSiMSlDZHf7iB04Ud_glSgXyUwImN4CXHSHIOfGVMcz-9AfQ4wzz3Mz3cN8UthfREZMfv3H5f9YFd27z2Ksfaj2gOv_whUufcpiatBddo0bz5YrZ2mtkQnLGJw_Mk4XQoA84r_Uykv9MVcf0_sSBySQmtrRfhrlSC0n9BN77zzqfqxf1c8uQW0rZTi5gHZotDKqaJv9utJcag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EgWUM6WzfnXXjcYIUlX-FSbfyT32MmR7T_sU2WWeW54rfuxtMQHM5w106hxSdRLp4_QKVflTg-vSw6MJDhffQDvVdwrd1kOLVpNr3ltXBwH9AXO4bWZJmFaic_QqZ9xdklLIgIg7m1Srms3ZGsJoStx7RGgE67uAQTYIE1PWKeSe6sG8BwBs_Du4DwXmPEupcmwyoecvOIFiTq_xqnRLCV_Avid7cXtTryDdVgLLq4gIjCDUy58lABUj_nanIp00TiaI6G3unxWU5n4IwMYdPVKrlahGAN9WxJJ71lE2uuoI4OhKIaqQsBFWGjDEA7aBkd0cSVPMdVd1ouAn2gdo4w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Vf2UcDKykxwALdiOoFrjpcJsJNLVp8TD1CRL2tX_rLShlPQCDn_bb1JS1AWPirYkCdbtnUQUbWt8kolG-xvDgDELG3OkZtukVmQHcMbWUsjg2ev-DyXlg65OrRxqEujMZLnOXKXGtVeUjef838RmOIKV3UsnVxoXHz7oMvF5hyydl922301dqjJ7_0RyUJg3k3KNbLJAU3p1q_yUIsqBPe56IcrculVxngta8bJAP7_J9cDSnfHKvsd4cRZRU3_98Jvpqvxmt1luwGazVSmPEU9kclYw409KwBBPPcnxpUYMQpuV1GPYDT6fDM6BHk4CfDij0BOhruVfvRJBAn5DIXpZzvNAZlDJl0pLrWSWeK1D049cXflF9pN-1cPmuneCqBgz5QU43RXdXm3AXUxAUQW8qdWNZAEyAcpd6IbQpiOgzF9RwCPyZKM5tM0tGc-WIIq9YPjUXf3l3X7rE1lNr2qN6H6SDUwF5fIvoBi8k9ixihHDrTeW7fFJlG8NwlpSRkR_hDqoS5rAUD3L0BUvi6WgY97DDS6ZeKzg7FnPRxJTtH4jEBSu-pDW49STFRecfIBAALOHYRaFP9ndhgDSJ7K4sbGQpebcMF2sfbkXA9WPxUXANkJqWd0YtvnabkMnwReFlcJGMNX7OPdOuOP63f3zN39-JlsgKEJyF1MQrSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Vf2UcDKykxwALdiOoFrjpcJsJNLVp8TD1CRL2tX_rLShlPQCDn_bb1JS1AWPirYkCdbtnUQUbWt8kolG-xvDgDELG3OkZtukVmQHcMbWUsjg2ev-DyXlg65OrRxqEujMZLnOXKXGtVeUjef838RmOIKV3UsnVxoXHz7oMvF5hyydl922301dqjJ7_0RyUJg3k3KNbLJAU3p1q_yUIsqBPe56IcrculVxngta8bJAP7_J9cDSnfHKvsd4cRZRU3_98Jvpqvxmt1luwGazVSmPEU9kclYw409KwBBPPcnxpUYMQpuV1GPYDT6fDM6BHk4CfDij0BOhruVfvRJBAn5DIXpZzvNAZlDJl0pLrWSWeK1D049cXflF9pN-1cPmuneCqBgz5QU43RXdXm3AXUxAUQW8qdWNZAEyAcpd6IbQpiOgzF9RwCPyZKM5tM0tGc-WIIq9YPjUXf3l3X7rE1lNr2qN6H6SDUwF5fIvoBi8k9ixihHDrTeW7fFJlG8NwlpSRkR_hDqoS5rAUD3L0BUvi6WgY97DDS6ZeKzg7FnPRxJTtH4jEBSu-pDW49STFRecfIBAALOHYRaFP9ndhgDSJ7K4sbGQpebcMF2sfbkXA9WPxUXANkJqWd0YtvnabkMnwReFlcJGMNX7OPdOuOP63f3zN39-JlsgKEJyF1MQrSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6hiqR7Y0lpNPn8c80jHfwuwfKSfuf5GQH4OgigsnTg1zgmk-NcOGFsJcDXWduHMO0p_m1BWCZ7ZK8kKoO2sGcyzUAMzQLK7rDG2KWjmOQtAYjGSu7K8tVqxBysbPcciqe6C6mJP57oP4vUMYwi0N4I8aNyp6zJER9QEr8cKOfTAKcEHNUoytEGpnEpxhwfmBNJX5F2As6wpYZvZAOsq9E35iUIZcmOcadYm1poBk7x8G3GBjssVnntbdN8WzFNKWk_PtvdeyTBZxqjVP2CTBDPpiIr_8jXfgWkyi_6mSXrZiSl8NR5n9VCFFwRc4Ltd7BE-7t8kn09ivQIduDd50Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgDk9IxpqGedcFPY1xCRzAePcIGebhSSBhGWwokGUzwoEVFd60B_X0fbSofRodNyR8yOsu16XdyeOqUZ6nJZ5BZKN2GLZYdY-xv3FQ_E2FcVwiReJ2_lDbRfd5UZbeCl9OKCTMFmaCSE-KQnzamuEcW-KlidH3z1oNJ7Jy_DIFCicS6u0M5bJ_NRcDkqXadSMgESejFgibbk_ZN2JiiwYoQmZcyqwdnBrKA94SGge-ISwqLB5PTUeMXGX_7XQfSY0J8DjsqdR1CxINoRfAAb0XdO3OQoq7YG2xm0tR1Wz506JfGhkH9kh-k50TMY-LSU3AAsncsUC2sn_byFZSPLKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=KoORCNAHdLQZQqcLcCb-j4rk-alrepDYAwv5TYH3XYeO9ihqmwEWwEhK5LshVvnWuEblFzkXIxOpVhHhf7tYIU-rUkbimyS4ly1Oekv_95QljRQIE0-yFu6ljJq0GBSIJpPdEDbfWRtwHefUos-I39gY8vrfB8C-_Fwq4xsek6gf0UUn5BmWI_Xy6mJtKoxuYGGqwE2RMRcy2ETUTQf_1SMPV1dJQLbUtF4R-iK_FDTAMNn8iUUqVL8Pzo8jrebgPUONxSA3pnuTD0X8yflib8jR1zmfozEmXXdM_3laZplMVo3XJ3OPGFnfPwpN_XeC_VfsNDZZdQGeYrCYtHwYgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=KoORCNAHdLQZQqcLcCb-j4rk-alrepDYAwv5TYH3XYeO9ihqmwEWwEhK5LshVvnWuEblFzkXIxOpVhHhf7tYIU-rUkbimyS4ly1Oekv_95QljRQIE0-yFu6ljJq0GBSIJpPdEDbfWRtwHefUos-I39gY8vrfB8C-_Fwq4xsek6gf0UUn5BmWI_Xy6mJtKoxuYGGqwE2RMRcy2ETUTQf_1SMPV1dJQLbUtF4R-iK_FDTAMNn8iUUqVL8Pzo8jrebgPUONxSA3pnuTD0X8yflib8jR1zmfozEmXXdM_3laZplMVo3XJ3OPGFnfPwpN_XeC_VfsNDZZdQGeYrCYtHwYgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=CVRQQFecIo2b4uOeSo8TwPg6Fx1ttCJqGTqJCZ_X_oshPcR1idWdWt1PntY11iNyezHUW3HSJ1QXfyXTAM_4DAzk-hWKLCkK3SiTklDAJS20g9iXnaWh_lSLaS-Su6bNWyZyGY6hxEN_YZysQHMtSCva7Rx6y290P3erfHeSWGqGPuL-2TJCKD4bIAIXyU0v--DJFp_ShuYPgL-5TXQBgVXs26lA6iwAYg8Xfwa-JmDBs7cHZkJulG9TfZbaRqerjPRjgDfYwgw_khLf4FYkAk6EPQZiHwObOvjXHo-fUkdmGusAueULrDnyLDmhGYzdweZR3U9o97LTNCB6EYEdMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=CVRQQFecIo2b4uOeSo8TwPg6Fx1ttCJqGTqJCZ_X_oshPcR1idWdWt1PntY11iNyezHUW3HSJ1QXfyXTAM_4DAzk-hWKLCkK3SiTklDAJS20g9iXnaWh_lSLaS-Su6bNWyZyGY6hxEN_YZysQHMtSCva7Rx6y290P3erfHeSWGqGPuL-2TJCKD4bIAIXyU0v--DJFp_ShuYPgL-5TXQBgVXs26lA6iwAYg8Xfwa-JmDBs7cHZkJulG9TfZbaRqerjPRjgDfYwgw_khLf4FYkAk6EPQZiHwObOvjXHo-fUkdmGusAueULrDnyLDmhGYzdweZR3U9o97LTNCB6EYEdMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=UpcycfpfvOvCEPzjeevgOl00kFZhjKR2jC0BfsHSyevZxoh347GoRRKFcSnm5NmT22G-06CxvphqgCuTzTZu4R25a7Vf6ODXN8Fbn-rk0yavjZflosvC3rFdk-Jz5-A61YaJkLWwpqhwJ_RO-MaFkFKh7F8_5Oq5vvulSSreuMrpeHDnYqA_uu5zQkCSxGSopiGkPHzWT33viHPVpheJb3ToNGttm8hKGEJC1YCDmzFk91LdcJr1Id_7ly6VeuXSSD81JH4EIj_N0NbxKLPMDltcs4woYZjlXuXhArTzr7O-lJTm19qqdsTiC3sEgl58agyTKpyaaIVB-vYbc8XH5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=UpcycfpfvOvCEPzjeevgOl00kFZhjKR2jC0BfsHSyevZxoh347GoRRKFcSnm5NmT22G-06CxvphqgCuTzTZu4R25a7Vf6ODXN8Fbn-rk0yavjZflosvC3rFdk-Jz5-A61YaJkLWwpqhwJ_RO-MaFkFKh7F8_5Oq5vvulSSreuMrpeHDnYqA_uu5zQkCSxGSopiGkPHzWT33viHPVpheJb3ToNGttm8hKGEJC1YCDmzFk91LdcJr1Id_7ly6VeuXSSD81JH4EIj_N0NbxKLPMDltcs4woYZjlXuXhArTzr7O-lJTm19qqdsTiC3sEgl58agyTKpyaaIVB-vYbc8XH5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmwNSwDbQa9HqwFn0ElfVSMG5erlq76uWJX05HjVR3JSc9xhwYsFP4lUI9PrhVhrEoNeZxa3a7Edu7QUafppq0R3x6nTaJ2XMcsqoP7NhJ6vM7rvb9Ah0tl3YkeG7wY4e7sogyoiBim4wEU2IzZTsUFEcCfsKIs3lQfFAuiue3hm-IxnBqm96SmRQs5JblpeBUJacxm0iiCOZS6Q1NrzPRxFjmpTsI4eb1kzIedfqsFGgs57T3_5i0T1N0hTOOB8SLUFwjc_GjJOWTdVoZ7MLYpkLsoQCy_Vd6V8RSqCL0obkp0upGLPue2SahMjZYz48aix_XJHTpmTNEp85OCl7A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EZIDkAAci38tIMLE5ctbTT5CkUZFXuvF2y1LaQ9XE_6eyXeoc0zCm24lfBiafMzed5vW4MpADDqy2owXMBTxVjMc4D8xdKZ2jcFv2pH3tC93mFFJ_IH09nxong9As15b5mB1zxUu681oLOztxQ3UDeIK_D8pgFO7vnMns2A0n26cxYEjOKrIpOR7MWpEh4L_7u87B1JdaL2xrHp93_ZPI-OfO0ufrD8_npcdA-8Qci0w7jbyWBxRse25tfxbxCGiDfDSDiAW0rYGUWUzFp6bCkt6JgwcNTByO00O59Yra11KVsQo45VtTBCFY7oEPIihFSym6pT5SPQcC_uLIYw58o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EZIDkAAci38tIMLE5ctbTT5CkUZFXuvF2y1LaQ9XE_6eyXeoc0zCm24lfBiafMzed5vW4MpADDqy2owXMBTxVjMc4D8xdKZ2jcFv2pH3tC93mFFJ_IH09nxong9As15b5mB1zxUu681oLOztxQ3UDeIK_D8pgFO7vnMns2A0n26cxYEjOKrIpOR7MWpEh4L_7u87B1JdaL2xrHp93_ZPI-OfO0ufrD8_npcdA-8Qci0w7jbyWBxRse25tfxbxCGiDfDSDiAW0rYGUWUzFp6bCkt6JgwcNTByO00O59Yra11KVsQo45VtTBCFY7oEPIihFSym6pT5SPQcC_uLIYw58o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=S0tdCwjoK0nMHD0rnmroCMbJjRW87Q6MdYLMMq0zMACDUD0x-8K1LHxveLyt8UZLYjsTMF7irvCkNZoJ85KcwLVp_NOkUiHZSY5n6NSlJaKLYIWjfh2Kn9P5v27OQ_qZbuHPusHG9wR7HLq0tI6kXLzm1-geZPM9kj2ZMKewj8A5761VLUgm389aM0aNOcu0OQi8W0lQizSsiZEWQM6l_Fpnp0ehkJFWWJTWx5sR9Snr5W9lly5kAzJWk6Myq_MWVckwE4c_m2kYoSCH642vnIzuVXqGuXap64Q9kxIfRTTGaLe-JzUr0TtP5QwomvgJlaLwz7ALszMzCQ_A0NWZdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=S0tdCwjoK0nMHD0rnmroCMbJjRW87Q6MdYLMMq0zMACDUD0x-8K1LHxveLyt8UZLYjsTMF7irvCkNZoJ85KcwLVp_NOkUiHZSY5n6NSlJaKLYIWjfh2Kn9P5v27OQ_qZbuHPusHG9wR7HLq0tI6kXLzm1-geZPM9kj2ZMKewj8A5761VLUgm389aM0aNOcu0OQi8W0lQizSsiZEWQM6l_Fpnp0ehkJFWWJTWx5sR9Snr5W9lly5kAzJWk6Myq_MWVckwE4c_m2kYoSCH642vnIzuVXqGuXap64Q9kxIfRTTGaLe-JzUr0TtP5QwomvgJlaLwz7ALszMzCQ_A0NWZdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWB5YTjr9swES7S-9cAYkeos6apc39i6WG1-QUcjRji8-4NjWMBrEUwIb7dJf8nC2bt8zSoA5LW0Z2_EckmDc-YLXwSczzcNHOa4I6s3AeypMsRBHgSzZ7H5XiWcEPSt8exoZlA8SdbHXCuZTOBORn0Eqkj_pPxHNsmoCchoZ0YfjO8Tkqkn0D7VFBF_HYUwUT_n2jlUz6O2a_mFrvjDVRqyimKxNoORvi0hyOWT3aUVgJWsJxT9Y8VbJXT8JNbp0sfPMIvKmjyFK0nfYkmWSWhGscrjGT8CzupgcA6GQNRFM0nt7copeK8iTCCqZqJytKnSfsIRHr6WyYoPl-Y5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=kcZaDFQAnUfk6xOoiZJQXupR73vL-iRkBvGUR_ScAnHk-fvmt2bCnSn5C8IpzFu9SHnVX5axYt-FR8avDNO0uALDSdqrqsmVN9AbQyvcmm-0BQNy-W1W7Dyw3TluIM1w1o4uyds4dGAa9Te6knweKedPthUb5WAAxprnaQ-K4xZmFS9qFsFwz-JW0m8qZjT75bTGljkebrkRgcYMkjT8lJhgMCI12GhGmw7ifeHaK4G9rDKHnqr0R7rXtAkDVazxb-02ewgTOAVRbpy48WHMMniHRQW9PFmMXF-eCYSu9i4n9sYR8OQuaQZuoilefOPOKdebS4_DlpHguKUAY7PgBS-sig0tbB1URE1MDsb2QycoWWqOYQ5kI6L7zWQLPMQUDxnY2Ohgza2_Y1gVWtdpEQiz-PXIHAQDW_2qilPpVGYXnylMdEz_OseLqboJcrmIhnSANnEEEiab6Z6dJasw_oxRVbnaEeDv5isSFf4FZkkPD66zJJ1Rztxlj_qfhguuVAKhKArYV7zZchsGqidhBv-LfbpjqgTbERlw_CH9Kcyhl91ybIxtTsbws1_kACzXzDPm5MfnWXFIVKpG1JKoCEezFAQQRpfQjNcoETsC8rAJA2BVAnakpoD2pql3a6IGB2wU_ULPok0-Ey-B_5lU7Ql3MyGa_4AyBhpMF-hGF0c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=kcZaDFQAnUfk6xOoiZJQXupR73vL-iRkBvGUR_ScAnHk-fvmt2bCnSn5C8IpzFu9SHnVX5axYt-FR8avDNO0uALDSdqrqsmVN9AbQyvcmm-0BQNy-W1W7Dyw3TluIM1w1o4uyds4dGAa9Te6knweKedPthUb5WAAxprnaQ-K4xZmFS9qFsFwz-JW0m8qZjT75bTGljkebrkRgcYMkjT8lJhgMCI12GhGmw7ifeHaK4G9rDKHnqr0R7rXtAkDVazxb-02ewgTOAVRbpy48WHMMniHRQW9PFmMXF-eCYSu9i4n9sYR8OQuaQZuoilefOPOKdebS4_DlpHguKUAY7PgBS-sig0tbB1URE1MDsb2QycoWWqOYQ5kI6L7zWQLPMQUDxnY2Ohgza2_Y1gVWtdpEQiz-PXIHAQDW_2qilPpVGYXnylMdEz_OseLqboJcrmIhnSANnEEEiab6Z6dJasw_oxRVbnaEeDv5isSFf4FZkkPD66zJJ1Rztxlj_qfhguuVAKhKArYV7zZchsGqidhBv-LfbpjqgTbERlw_CH9Kcyhl91ybIxtTsbws1_kACzXzDPm5MfnWXFIVKpG1JKoCEezFAQQRpfQjNcoETsC8rAJA2BVAnakpoD2pql3a6IGB2wU_ULPok0-Ey-B_5lU7Ql3MyGa_4AyBhpMF-hGF0c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hA_4yPP3l7XT5UjFF1QogIVigFkKmOHXY7uXKXQiBeLw7tmHNJuezkRIEHpqAHngtOqIsCKG9DWNVBqwAP9QWSHfg-d6Sb-GJPO2OnidYeftRkEAb0Z5hWVZayHLg-8Os1gSjPM3DLOU2gTf8sQVgDMDcUV9xdKg5aZQm1jnqWjWmLTEsaDBj6K1E3IqT1-RfMP-X99msYlJfWDBl13pHmxrR9_DKTsh7UD8jwjfUfv-Hau5NsqoWzpxavtbKWek0t035Xvl8VuQyf8iFuL5k_RMDChLUBPbFKwjmL-PZj6YCKiAuJlU3dlqk9EsfrEAKWXS1zoNbaLVWJmeLHB-DA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=PzVaR3HzuvSrros7k7JCADaSLzD1RfM9IvDMK2SxHitWBS_-xjjjvf6rv33sTH48DF6X8tWrIIMZx2psOV2SNjPCtmPdoDj6cRr8mMnlfj0NcKvCm4txdeUMDhnLJjVdFFWcPmOKvlj01XicTBV3_m587YDDGme65tgR3AYCUzKUQyzjLUKxCBzbXPmd7XHExUFLmWA6ivIZTIB-UitHVYSBN6Jb3BERR7E42V8EIPisUCW_d-D3MmnQhLnkubUtOZt7CvrGoGItEu2akb_xlCQGtorjhbJ89zx8JYRcMZGn12SuXyk-c_GTujn-RrTZ4ShUBI7xvPMlU6kifuSAqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=PzVaR3HzuvSrros7k7JCADaSLzD1RfM9IvDMK2SxHitWBS_-xjjjvf6rv33sTH48DF6X8tWrIIMZx2psOV2SNjPCtmPdoDj6cRr8mMnlfj0NcKvCm4txdeUMDhnLJjVdFFWcPmOKvlj01XicTBV3_m587YDDGme65tgR3AYCUzKUQyzjLUKxCBzbXPmd7XHExUFLmWA6ivIZTIB-UitHVYSBN6Jb3BERR7E42V8EIPisUCW_d-D3MmnQhLnkubUtOZt7CvrGoGItEu2akb_xlCQGtorjhbJ89zx8JYRcMZGn12SuXyk-c_GTujn-RrTZ4ShUBI7xvPMlU6kifuSAqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdbI4xVN3kSNQthg6VOvqdz0xM74vDij_yH4Idx0lCcFLV95FvjvXVqrKnw66MpOQBTJ4t2wlLy5HjhMHxvFxi6B_pqpjQEMMsJDvzImHdEcpOrMDlN4f4b_pyTRr0I3x_L1FcWOX18CCXqBdJl78FKbdI24EONVMwU8nnEWxH_sh4sQszsKTqADscBZ1GzQ2j5Oik8vXzxHTA-Zi3nq3_UUCDJDu5pyHerrwlbjB1T9E4xw1Si1y4GVbltPVfjtmgADFEdcEfGdrFiaJtrN47euNRQ8ScMgII_bIh0CNu6983Wl7AFmAYe9zjzDqhKyZUmvJu-KHRhwkno73AuTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDRkm819msqDzhyfvPCcUhVMmn21Vc_wIPf7VgG7a-kQdS8Sy5Umm8ma0KnIxgQ2oESD5KKz3AJ0yGOI7fm7KrFGlgSLUp5gc36wBam_kf-RNDT927NR_EeXf6hFeWjdEcspMtS8hpkGwDa_mdHicoCIYgXAQBbroim7xYyVvqyHPPe77itGDR5-Ee9P0WKt6VJW-fY2nNyihO0m5NYYU-3UbW6rsUIdKjfu3XCJLZkETZcqqWQhKULwP_1T93ARlCVd0MhyME2x8o-tkMjXaw7Nd4VJfXTSWMBeX8H4E2NienlJy8gO6zQLBUdEOct5tunXH62I1OIRSf1sR2or_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP_1m6VRD7Rh2kRnBfyst5ud-hgvFUM6Be-37o5LvdE1fGRnvb7i-VrrbyqIw1779GuzWmbecUDWfp6zLr27VFP1oRhZ1ao7U9-RiUDjHumGLUsxCIIKQ1IwuXKkQ3UWChN_4lbWgtZ-nYICDKrChZN8zSm22bZwprDe_2SY1ULfDv6Cs_yKrUsav948AOIFgH1x6DJE-c7jUvsysycTrM36KBQx-O1lSItle-Psh6_Yp_DBp4q30T6N0GtnJEKXeX26sBRcu8PbJb-rTkv9fdKlku9s30gfHE-Id9h1o2DeYwJ6Aia0MX02t4y9wkMJ43n-G8N3eLfXtXjnUlbDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=apOQ_ybkL_aGGWE2YSBCFNZNmKCeYKA4zje5f36iRtYoVR01GdQhK3X_XCwD98BxPQJZLSHrA4WBLYaNj2_hV9KUc8wOkVPjdg3tkPIcWDkG6hIrFpaDxtgqnL6ponhYLQ-TFAlcwwfRJKirpthqfxRa4ObpwRMt5Atv5XxJgIszrqAy0hvSn5_t_uJapMriQ1MDghV0hLDecwGzRC3SCfAPuhxnfhtiYzvgTdd8diKdQWDQ2GidIBE6wz3rOmh3RDOsAOcfG47XE54Y88HhDZHkZ1dc08rd4zBZcw0hwd2qjgEcuIszSaJxoWDslAfkjROstbwlWpaLBQULhNvn7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=apOQ_ybkL_aGGWE2YSBCFNZNmKCeYKA4zje5f36iRtYoVR01GdQhK3X_XCwD98BxPQJZLSHrA4WBLYaNj2_hV9KUc8wOkVPjdg3tkPIcWDkG6hIrFpaDxtgqnL6ponhYLQ-TFAlcwwfRJKirpthqfxRa4ObpwRMt5Atv5XxJgIszrqAy0hvSn5_t_uJapMriQ1MDghV0hLDecwGzRC3SCfAPuhxnfhtiYzvgTdd8diKdQWDQ2GidIBE6wz3rOmh3RDOsAOcfG47XE54Y88HhDZHkZ1dc08rd4zBZcw0hwd2qjgEcuIszSaJxoWDslAfkjROstbwlWpaLBQULhNvn7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqHJ3XltuqtWgU7Mtjj0pcTjRWYNdalS1JGyqTgAaXoPc-SpUVIi8COstV1_2lBFTaUu7lcgKZk63icsPTrCLf2SIf1Y6eWk_K1-OVKS5HHG0NedDpCdqoLyXj1FYDOZdr777yIC-H6kPLd4NZLZxdIMhvFVSh4PNTQXjmdajRHWgJX3yD5MklWKKpnXJm9rlgp1mPuSOSbtPqDU52W5dZlJqcpF5fKsbheSvvEHuqQD8hlT28lIUDtBDxVg3-PY8Pa6kT1OVMBN__bf3Nk5RimZGsLX7NvdSdJtpYAm_6DAFzeKmiV97Z-a7G7884WwRgXwiDAuYVkB3MlC7X1Oig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1IAyp1zxddOS6c6A_WaA91HSTNTclpgvHVnajaTyoOEV0sBAjNIeNOFgxpXDlZMl96JYz36itwCBDsizoGhlXejF1jQXGNYJDG0Mu5cIOrQZ8iy_OawOWeqMnnYKjzIGpQXIZnxDqNqYzrY64-4AGTSVCxr7eqVosydCsiJ2Nufsa3M8amz2RPYoqIK2ijsbkk1ekagRZo3nan8DFDSb-R3Rr3M9pWAXXL1PaX6ihP1kmG3jfMMzE9rdmTj7t78pN-h292cOz14vcBR2GlNbyvo10_Hj4UHj8ZGoQMKVCxSUT1i3damPGl8CkpZbEnnjosDRD1F3oBIrJAHEkOFDGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu1IAyp1zxddOS6c6A_WaA91HSTNTclpgvHVnajaTyoOEV0sBAjNIeNOFgxpXDlZMl96JYz36itwCBDsizoGhlXejF1jQXGNYJDG0Mu5cIOrQZ8iy_OawOWeqMnnYKjzIGpQXIZnxDqNqYzrY64-4AGTSVCxr7eqVosydCsiJ2Nufsa3M8amz2RPYoqIK2ijsbkk1ekagRZo3nan8DFDSb-R3Rr3M9pWAXXL1PaX6ihP1kmG3jfMMzE9rdmTj7t78pN-h292cOz14vcBR2GlNbyvo10_Hj4UHj8ZGoQMKVCxSUT1i3damPGl8CkpZbEnnjosDRD1F3oBIrJAHEkOFDGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p1hYg4nVicJ1E8nhRu_6bdsykJXLWE0217h3GolcgjEuICFQ0uIxkU7H1GARkPpi7pAvF9O960bvAtCqny1JSdKbPq92TcWDfPeh3RCSfrOmEuD6Thg5fmHgjqbtEwNNXWFuFFMTxXHA4_f8ypVMTABFgJLzSOjzAiq71Y4lYoq6O6M5U9QRQhJp4bzeAWJFfZr21HJqpYxSyD-8iaBM37ULpQN781Xfo2S3TGRF69xw6smbGMtthA9BNbLgjTRqS2U2_TzIi4UOhssnV_qMRq_VYo14kQT5jBMs3JWQx3Ng7SC7C8w1mKwrHif4xNxj0YoIgpMEmrsnwyfFykXqhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p1hYg4nVicJ1E8nhRu_6bdsykJXLWE0217h3GolcgjEuICFQ0uIxkU7H1GARkPpi7pAvF9O960bvAtCqny1JSdKbPq92TcWDfPeh3RCSfrOmEuD6Thg5fmHgjqbtEwNNXWFuFFMTxXHA4_f8ypVMTABFgJLzSOjzAiq71Y4lYoq6O6M5U9QRQhJp4bzeAWJFfZr21HJqpYxSyD-8iaBM37ULpQN781Xfo2S3TGRF69xw6smbGMtthA9BNbLgjTRqS2U2_TzIi4UOhssnV_qMRq_VYo14kQT5jBMs3JWQx3Ng7SC7C8w1mKwrHif4xNxj0YoIgpMEmrsnwyfFykXqhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=tTLLM7fsuZcFeFwSZpjfGdxV3s2T7M2jPAjHDN7TH-15KBvkhIoLHjK73nbxOM6BWoMbZnwuhT1ivaQ591eey8R5DqKw9ZKQC-Sxds2av5AVtoys4JGEfUGxuA41dI6i-78-j_KZJx-uUqUxDoFa9Ur6gWtQjXYQsTRzEaARXgSe0PgQ79FSxiEeu5OR-hvGUYO81sqOiiX-K5J3ziwXbAkQ4b2OBfWLHUT_V3M6Z-rQbP7zI8urhBeBxgxvbGPrhGK5Bhlk3LR0q-N09V1eUboDJHfKtLBO2NzKeGfuZNh8qWK9_5AI5mRx_Lz-FrzZEXg78BLHHnOCvwSuX_qjugocRZOv9N56-gPqo4z1uft6Kdu2P81fa_-mJ--J_8ISqJ3rhxH3_pEKuJwhdROgIR1VkYPPwHgwftGFu5OgXtTibK0Tco4aQS17Y6nw-n-cVbfwUVgtSVBmmO9xXJow9r-MV_-AeMAo_PxoU1JUYiEzPOMyHgDb4Pz-jB9J4WajiEHxoetMACts1B1tA1s6vILK5QB9c5KJGVTz6P0AxWHH7w6CNQiy84ogM6vKin7rxt74nOZcHlTjyx52Kx1of_2zQxIljfVNf7PSR3GJZBjVcjZXT7T8miykDEJ1QvaqxUFukCXydHbz6tRZfzN-GQvcqxBz0SbUE5dXUMAMhEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=tTLLM7fsuZcFeFwSZpjfGdxV3s2T7M2jPAjHDN7TH-15KBvkhIoLHjK73nbxOM6BWoMbZnwuhT1ivaQ591eey8R5DqKw9ZKQC-Sxds2av5AVtoys4JGEfUGxuA41dI6i-78-j_KZJx-uUqUxDoFa9Ur6gWtQjXYQsTRzEaARXgSe0PgQ79FSxiEeu5OR-hvGUYO81sqOiiX-K5J3ziwXbAkQ4b2OBfWLHUT_V3M6Z-rQbP7zI8urhBeBxgxvbGPrhGK5Bhlk3LR0q-N09V1eUboDJHfKtLBO2NzKeGfuZNh8qWK9_5AI5mRx_Lz-FrzZEXg78BLHHnOCvwSuX_qjugocRZOv9N56-gPqo4z1uft6Kdu2P81fa_-mJ--J_8ISqJ3rhxH3_pEKuJwhdROgIR1VkYPPwHgwftGFu5OgXtTibK0Tco4aQS17Y6nw-n-cVbfwUVgtSVBmmO9xXJow9r-MV_-AeMAo_PxoU1JUYiEzPOMyHgDb4Pz-jB9J4WajiEHxoetMACts1B1tA1s6vILK5QB9c5KJGVTz6P0AxWHH7w6CNQiy84ogM6vKin7rxt74nOZcHlTjyx52Kx1of_2zQxIljfVNf7PSR3GJZBjVcjZXT7T8miykDEJ1QvaqxUFukCXydHbz6tRZfzN-GQvcqxBz0SbUE5dXUMAMhEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GN7h56MelKZjj_d2iucfMBazmsqQx7vOBDIKRXwrvYryGaqY_qeg3Ed-KhNJYDrmJ7J4at2b1i_yxa6P0r1SSbQ6CFZ0v0P9B7djgLgHZUAzAGP3rnip2NRWQEV7e4zZ5J3FYuHbHuBBNhZq-qW3xRb9BtEtU7goFmP8MxrLBHkfOYNKo71M4UvpO_Q6f7OyiksFM-l0HhyqWsla8nXReGuRGFNxQGKS66K1igMVCYabPKlmlx0cGupSQQ68PSgsS2rRpV-PGYdnoY-qYGP4q_gq2DIUhriNWQgb5h9h7qjZNd8h2Qn39EG9wZFFxASi72gEZnXGZuD5lPxqHuEDTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GN7h56MelKZjj_d2iucfMBazmsqQx7vOBDIKRXwrvYryGaqY_qeg3Ed-KhNJYDrmJ7J4at2b1i_yxa6P0r1SSbQ6CFZ0v0P9B7djgLgHZUAzAGP3rnip2NRWQEV7e4zZ5J3FYuHbHuBBNhZq-qW3xRb9BtEtU7goFmP8MxrLBHkfOYNKo71M4UvpO_Q6f7OyiksFM-l0HhyqWsla8nXReGuRGFNxQGKS66K1igMVCYabPKlmlx0cGupSQQ68PSgsS2rRpV-PGYdnoY-qYGP4q_gq2DIUhriNWQgb5h9h7qjZNd8h2Qn39EG9wZFFxASi72gEZnXGZuD5lPxqHuEDTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-gMF-D2-8m8gPW8RrRqzndpC8xHYjwUf8TWDg04WLj1My7Ai6r1eyQg2KQtWY1TZmTuqsJkChjTqHmPWEqwIUoVXjHYyNwSWQovHReOo6TZbriRlNu1cdcDoDmZqhkEsjEnFeTFMPNrILWnBSX07fCqgLMeTegxOqcKUqI65fNrrbt4ODNaJ6CmqeSdo9nhKC7AhDsck6JOw438tKtYYFOE17KK8K-FXz6kaZ5P1hUy20ZZgz6Uk7Qj7LMRmG-7cJuPwmidijljQpkEGIVmAecmTRQmHCSstqjd8Tjq0cwM1yts3_LmCeF8oiSeUcKNz4UNuzViaQMxU8iXOrPsIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=t3m7wCOL6W_XY7WfDOZ1h1d7fCKbixS656MANyIVSPhOadWEPeV_9KVlcc72SCftQ9jtFseZYMlorcQvuG41R_DuLuXqIMSKjYgPNdBaqJnWfL_Y1LKazr4wDW5_y1yP75BN-wEIXR-hey5XuYzQ4cKYAMQX_Aqh2-YtsGCdJonoYPMRUzZEenShM1gmN23jPuMTt31SNZvzmSWxXQM05IxcNCp0T5XeQnWVLfDkxeHkxxgtMZNhnhXI9WJIr_B4dCuP9oWXqvEHwHmc-UrmLor3dOJOXRTQaOI69huS1b4Dl5EQbNnRgNlvq-Bmw7YNukEhoo0sbAP_yqySjl2I7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=t3m7wCOL6W_XY7WfDOZ1h1d7fCKbixS656MANyIVSPhOadWEPeV_9KVlcc72SCftQ9jtFseZYMlorcQvuG41R_DuLuXqIMSKjYgPNdBaqJnWfL_Y1LKazr4wDW5_y1yP75BN-wEIXR-hey5XuYzQ4cKYAMQX_Aqh2-YtsGCdJonoYPMRUzZEenShM1gmN23jPuMTt31SNZvzmSWxXQM05IxcNCp0T5XeQnWVLfDkxeHkxxgtMZNhnhXI9WJIr_B4dCuP9oWXqvEHwHmc-UrmLor3dOJOXRTQaOI69huS1b4Dl5EQbNnRgNlvq-Bmw7YNukEhoo0sbAP_yqySjl2I7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=sg9_YNRISRUjbzBP3i8w4xX6booBoTbpxjHZd7kx_vFUd-moVUHA0i4lcZDNS4Gk_dNIqLW2xH6OYot2-mDgRhIhNtS_gE-h7E2MiwueMqQtTPCeHDmQA2h3dpcz6i3l48MmsHJfor9MyjSIjnXZBLJkhmhchtAN-jyUNtkeroIxfB1oIjhTtWs-nHiRH4kltWNE1wyDLoox_rYNSypRot1un0bGmVMNSz_Ph1RAxhpl1o8zM88xCi9fs7HrvlSAHdPw114h3eTiAdRKKuuwB2Fg8p9qut7YlaAxWiJT2-DUkw6DxH4v9Ms-g3z4mPrj59EZEIr1BQOgjnjCnMaxaWWzNpJpIhMGMyTT03Aptnci_5HA7i2to3RiLhzLIq2Nn5SW8UVxtZIf1QhX6eZ_rZ3IIF8Z59707pICMYM9a_g0D4p2b3s8nRDaia7BHNasG54NT2HZkivjQ5_QTI33HRYwsW3MLvJJ04zKzOVHJ47JhiwQgq4yTx47BfDx3ulTtXL_yfAzwkK4FrcPG6bJQbzM_lSuizRzvUbeo3LS4mjmVKSRlybXllqXZdJzxDupDsb-pAPlATH0ioi9SdUzb0uIQTOHaF6FMeQTlUkM4bxJ8LXuoZfw326uMBP6m5gwfFIsI7YWijfIXRbxebKzkAOum_e9JgnDQYjS2m-NAe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=sg9_YNRISRUjbzBP3i8w4xX6booBoTbpxjHZd7kx_vFUd-moVUHA0i4lcZDNS4Gk_dNIqLW2xH6OYot2-mDgRhIhNtS_gE-h7E2MiwueMqQtTPCeHDmQA2h3dpcz6i3l48MmsHJfor9MyjSIjnXZBLJkhmhchtAN-jyUNtkeroIxfB1oIjhTtWs-nHiRH4kltWNE1wyDLoox_rYNSypRot1un0bGmVMNSz_Ph1RAxhpl1o8zM88xCi9fs7HrvlSAHdPw114h3eTiAdRKKuuwB2Fg8p9qut7YlaAxWiJT2-DUkw6DxH4v9Ms-g3z4mPrj59EZEIr1BQOgjnjCnMaxaWWzNpJpIhMGMyTT03Aptnci_5HA7i2to3RiLhzLIq2Nn5SW8UVxtZIf1QhX6eZ_rZ3IIF8Z59707pICMYM9a_g0D4p2b3s8nRDaia7BHNasG54NT2HZkivjQ5_QTI33HRYwsW3MLvJJ04zKzOVHJ47JhiwQgq4yTx47BfDx3ulTtXL_yfAzwkK4FrcPG6bJQbzM_lSuizRzvUbeo3LS4mjmVKSRlybXllqXZdJzxDupDsb-pAPlATH0ioi9SdUzb0uIQTOHaF6FMeQTlUkM4bxJ8LXuoZfw326uMBP6m5gwfFIsI7YWijfIXRbxebKzkAOum_e9JgnDQYjS2m-NAe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lC8KlUQI9kU414I3WQZ4yE32TfZDR9RLUZkTy2Wtiij0QXPSImpKuv5SEZc4yr_vXtYNmeoLK_1uwKRlw8TX0-uyHaEW7qzkx5Oaxo7LAjPDik7pVLW5XYsmhSUSgg40XKHSBpBXZzklq-sZOQepv_U1MWclkOj-SJcJYF7qLBc6uGbM4i7arafSpNSc2T8PEuL7TA_vneFM9a9ni_noCU4rqDAQZAlcrbIPXzdSqctkYi3LuBtD-6sY2OXSR3s2SRGXqBnmFD--c8qgeX28c1iMjbNteCrVt8WJ3UrVgjgosqCEzERaAJaaOqR0ILkiM_-_nWAScGO011fhk7bjsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ZOSRGkqwuDKX_5ss-EFYYyrmA-bylvimRanZ8Ux22QN6I5w790YGDloCXYgTrHhhQ0JV-e8sVoUiZ3tLs9bBwWWeouPgvZtd_Wv-sRVLBEXEmd5mybhw1RIvtT3U4UIqyTqyzNz2ymnKZqaHP-k6hd34H_ziG6hDmjdu4wIrcJqLe2b0zJvLQFZfYqhC6Zg_h-V55t2Eq34OvGfLR1s1COKI0yqRc-N6bA3qJtwvV5XXYk50yeJ0CR18_oKt8QwO32wC_5vNN-sziOyt2qCkAr5toHOtNBph3JenxLCb34_OYZLhO4sRfjGVQlTsvfZr4xephsNIn3m8cdcNiV6THWHnkpBSWdybbkReGk4AVUfdIqaS8tGVOeBcNf-_8NM0ovGj2JB25M0kF54O0Pk7bjnkEoOxRrYV1kLaBqxo_NNmO9nVIYLy1SiwJBrHXXcgdaLWTnS-my17G3AXcra9k_MlqolK9LjwfLl3QRHK7fkVfJZnH1PZVxWWeO42GuE3l9EADqAFixolUzSfLi-fcYevcqAa5BqZalX7rNlNMnEWEoQbjyg2Ceie6Zk7JS7bTsxj1-ntZp30xlLVlHlTgli89k4QTooicfUX8AhtlUE_gQM6FMfgno7DQ6A4FPQy1RN4vYtT7yCehSYiAvMsR8iaU0ffHrQGVrmAhtpYlCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ZOSRGkqwuDKX_5ss-EFYYyrmA-bylvimRanZ8Ux22QN6I5w790YGDloCXYgTrHhhQ0JV-e8sVoUiZ3tLs9bBwWWeouPgvZtd_Wv-sRVLBEXEmd5mybhw1RIvtT3U4UIqyTqyzNz2ymnKZqaHP-k6hd34H_ziG6hDmjdu4wIrcJqLe2b0zJvLQFZfYqhC6Zg_h-V55t2Eq34OvGfLR1s1COKI0yqRc-N6bA3qJtwvV5XXYk50yeJ0CR18_oKt8QwO32wC_5vNN-sziOyt2qCkAr5toHOtNBph3JenxLCb34_OYZLhO4sRfjGVQlTsvfZr4xephsNIn3m8cdcNiV6THWHnkpBSWdybbkReGk4AVUfdIqaS8tGVOeBcNf-_8NM0ovGj2JB25M0kF54O0Pk7bjnkEoOxRrYV1kLaBqxo_NNmO9nVIYLy1SiwJBrHXXcgdaLWTnS-my17G3AXcra9k_MlqolK9LjwfLl3QRHK7fkVfJZnH1PZVxWWeO42GuE3l9EADqAFixolUzSfLi-fcYevcqAa5BqZalX7rNlNMnEWEoQbjyg2Ceie6Zk7JS7bTsxj1-ntZp30xlLVlHlTgli89k4QTooicfUX8AhtlUE_gQM6FMfgno7DQ6A4FPQy1RN4vYtT7yCehSYiAvMsR8iaU0ffHrQGVrmAhtpYlCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Mtlqd84hIY1MwIyjn0VphOkQF_q_hGQtdOCVivFnkY0OM7l_3oyMPrPUlRjQKs35GKnrCdiTFg1mu8FXODMaryXHhu0NrUBATmi4Eh2ea0_AMX4wjOHpPKkkjPW3y5qZoK0ys1pOuDbLB8ZWBBIeSY8ESoN4uU9Fq17fei__fJR8z8c8T6zGAhbtaxOas2m-wA0snMmKVQUGpbcqgcBRETvC_iExV8u8OglKgIPvjiYsR2b9BFZpf-lDg1qlaftiibdeFgYBfL3Ws6uJ1w8ausjXZrkgnKPyKILr0vvAL1pQIXMnDQx4X3133jTtZE8RT5VcynDLcQJ04pr3g8ndzocEYB3zoqDElvVe1ck3bHRz8hplL_FSYxdsUeuen9o2EiyHqySrMI6uo2nQkpGaKvXIeCf3VvNdahiElwyntPn-1dzr3kqLO8gMm816ZMwIUD6VbyHTcFG6cOsDcYO_9kkUD6Twoh-EMbUirQ4w4ZhxBqwFOWvod6znlwRkEDRz1ARp3WDk94eh1S76RjzpQN24TkmkXtCHoQvEZqZXHHE3hmA2tSAuvEjI3tBNyvtZkR-_Sdpsy050CfY2nCY9qiw-PSLG0bItq4TC7-uKujNKrmKvZSQDw9MKO2mBHq780nuqX-FRwaRJ6BIS_GLIV-X4KtTW3HTy3NNv0-1yOS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Mtlqd84hIY1MwIyjn0VphOkQF_q_hGQtdOCVivFnkY0OM7l_3oyMPrPUlRjQKs35GKnrCdiTFg1mu8FXODMaryXHhu0NrUBATmi4Eh2ea0_AMX4wjOHpPKkkjPW3y5qZoK0ys1pOuDbLB8ZWBBIeSY8ESoN4uU9Fq17fei__fJR8z8c8T6zGAhbtaxOas2m-wA0snMmKVQUGpbcqgcBRETvC_iExV8u8OglKgIPvjiYsR2b9BFZpf-lDg1qlaftiibdeFgYBfL3Ws6uJ1w8ausjXZrkgnKPyKILr0vvAL1pQIXMnDQx4X3133jTtZE8RT5VcynDLcQJ04pr3g8ndzocEYB3zoqDElvVe1ck3bHRz8hplL_FSYxdsUeuen9o2EiyHqySrMI6uo2nQkpGaKvXIeCf3VvNdahiElwyntPn-1dzr3kqLO8gMm816ZMwIUD6VbyHTcFG6cOsDcYO_9kkUD6Twoh-EMbUirQ4w4ZhxBqwFOWvod6znlwRkEDRz1ARp3WDk94eh1S76RjzpQN24TkmkXtCHoQvEZqZXHHE3hmA2tSAuvEjI3tBNyvtZkR-_Sdpsy050CfY2nCY9qiw-PSLG0bItq4TC7-uKujNKrmKvZSQDw9MKO2mBHq780nuqX-FRwaRJ6BIS_GLIV-X4KtTW3HTy3NNv0-1yOS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=PoU80XWT4wtpeBR_AHxIYPtDkGRDCWpgNhi_iehs15Z0B-19A3sSVkv-PQ57NA5gNUwQ2uquhMGJpebpKZhtiJbKLvBA9i2AQ6XBT6LHyt1t4jtw3XuImvmJgxKJF4HCdtznu3BLs7QLYR7lG2T09QNU4g1ykZ6X9_QBoXqTT4zt4od-h9-KoUE7164kE93s9ymw4acQQfXP22IC06Amde87xdn9xkzxvGMV8vOYElmYioc1fXkkJWJ9wiD-J2mq0tQgFRoZgVVRT54DiCYQelbTFeH23wUu4puhaU7LuTeHPdkPOv-R6kfcwKI30gnSHreqjvsPkTxl8S2vWiPqTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=PoU80XWT4wtpeBR_AHxIYPtDkGRDCWpgNhi_iehs15Z0B-19A3sSVkv-PQ57NA5gNUwQ2uquhMGJpebpKZhtiJbKLvBA9i2AQ6XBT6LHyt1t4jtw3XuImvmJgxKJF4HCdtznu3BLs7QLYR7lG2T09QNU4g1ykZ6X9_QBoXqTT4zt4od-h9-KoUE7164kE93s9ymw4acQQfXP22IC06Amde87xdn9xkzxvGMV8vOYElmYioc1fXkkJWJ9wiD-J2mq0tQgFRoZgVVRT54DiCYQelbTFeH23wUu4puhaU7LuTeHPdkPOv-R6kfcwKI30gnSHreqjvsPkTxl8S2vWiPqTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ic1YkL5F9rWMuMRDXP4GSgea5X8OqugEs5_KSmlW8hKyt4BKLaaSVY96k_WcoJldh0TI9voHQB7ypX4qiEucPhh7rYnzKZuLOob65-zH9sAoME_DaU9JeCS4zC58-KbcQ-2KllXayvqdi0v5CJXIchXiHMebhYQI51g95vWKYXnsvyASnFZoN2jdonjo9BHjzhb3dDm78WdJwLLOv3iIectvKHJtM5gpkftdmkSUJ-T647Gy1ks2cJLQd2TcUbGhzfja6yfpBLKI8DtSVFZXpge4DIuKt9ffQwQk7tbk1qXJNOO_l8D-YqQRWZITZMbEd7ltsgsEJQ7TWdO4Kka8Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ic1YkL5F9rWMuMRDXP4GSgea5X8OqugEs5_KSmlW8hKyt4BKLaaSVY96k_WcoJldh0TI9voHQB7ypX4qiEucPhh7rYnzKZuLOob65-zH9sAoME_DaU9JeCS4zC58-KbcQ-2KllXayvqdi0v5CJXIchXiHMebhYQI51g95vWKYXnsvyASnFZoN2jdonjo9BHjzhb3dDm78WdJwLLOv3iIectvKHJtM5gpkftdmkSUJ-T647Gy1ks2cJLQd2TcUbGhzfja6yfpBLKI8DtSVFZXpge4DIuKt9ffQwQk7tbk1qXJNOO_l8D-YqQRWZITZMbEd7ltsgsEJQ7TWdO4Kka8Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=X7k48WjQuKCxRQPIjhaLYCxt8-N5pSlaX8ASpESLEDPGxvVcOZp6J7NoAlVzQwiIIpk67ELAInUI67XCsgsz68mU_liDLlwDv7JUwXLbSt3zSx-fgOpEf8ksIJEcWDQJNRQMJ1cghgS1qcsrJJs-ulsxBiJlR6zod7DbmuXWDs_p3qBabD4SlVXRN2Oe2bk2cAYICSh7X5-GreWD8FgOUZrr9r658c0ylxxipipB90vb3ijvAwkTB-ctcfZUz5XnBA56suRJegwgHJDfDtEozlf9MxFYE1CgfcVFVMN54AmuU2cnZ_7dMx9cKD8USxN_gMWj6ZfyUmmaUU-7Hzs5yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=X7k48WjQuKCxRQPIjhaLYCxt8-N5pSlaX8ASpESLEDPGxvVcOZp6J7NoAlVzQwiIIpk67ELAInUI67XCsgsz68mU_liDLlwDv7JUwXLbSt3zSx-fgOpEf8ksIJEcWDQJNRQMJ1cghgS1qcsrJJs-ulsxBiJlR6zod7DbmuXWDs_p3qBabD4SlVXRN2Oe2bk2cAYICSh7X5-GreWD8FgOUZrr9r658c0ylxxipipB90vb3ijvAwkTB-ctcfZUz5XnBA56suRJegwgHJDfDtEozlf9MxFYE1CgfcVFVMN54AmuU2cnZ_7dMx9cKD8USxN_gMWj6ZfyUmmaUU-7Hzs5yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Y18MN06DdtFQEoVBQwaoF_uKILI_B5WnXWf6ngW0Jhh6drn2X6ghXwfizAlnEAZq3S3xnuvEMTkueiz0p8ILPAgPGpkOdw9RKDzo5ue-Ua1Zdt9Aum5cr_L5BbDJU7eFE4-CNwHclH0jIxXFCCStEHpw8Ugs4DAjJWGV3V7QjefX-eNAeSog1YUbgCA-iIhedvhvRLisuWGdp7xA8Q0X89BCJlGtYq-lieSTm0hhmzohku0FakBJrbhnZoW5emO_o6mFRk48Mex1zPQoaIWfq5hQpDAu73uXfSEbIsHnrMSW0jiX1uqwlv3WdpmWNlm108fOrOR6PQhwjvzO4gjnoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Y18MN06DdtFQEoVBQwaoF_uKILI_B5WnXWf6ngW0Jhh6drn2X6ghXwfizAlnEAZq3S3xnuvEMTkueiz0p8ILPAgPGpkOdw9RKDzo5ue-Ua1Zdt9Aum5cr_L5BbDJU7eFE4-CNwHclH0jIxXFCCStEHpw8Ugs4DAjJWGV3V7QjefX-eNAeSog1YUbgCA-iIhedvhvRLisuWGdp7xA8Q0X89BCJlGtYq-lieSTm0hhmzohku0FakBJrbhnZoW5emO_o6mFRk48Mex1zPQoaIWfq5hQpDAu73uXfSEbIsHnrMSW0jiX1uqwlv3WdpmWNlm108fOrOR6PQhwjvzO4gjnoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=HN5fB4GUR-RHbJv6tKQvV9BNBm034QNKL5g6kLnxEsJxIOAUKy2QwcTnUVoDM7W_MSEWKmm7IKGdbrGyHAja8Bz0ze6nfhH7IJgZbyBwwrUJUENch8yWMCcndb1z-t0qzWSB5o_608FVt85IB1pr2pOBY9kKiNQTeEEN4FvR9L73Kxepo-XJiQqAcDiQEXLC0IZO5_tRMelUVG8V7ZTLlwzq2WzX4Jie3XOU-sWuvGZ9TlvuuSV_PFxUr-Vm_T9UczvkCNbmxUOMSnDwvNFR2u5w5cMvJVh2qA-cvp97HLYJKO9yn8cqEWRZLf3eMa-lDhpqaGkiUK9M7OUGLx3M1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=HN5fB4GUR-RHbJv6tKQvV9BNBm034QNKL5g6kLnxEsJxIOAUKy2QwcTnUVoDM7W_MSEWKmm7IKGdbrGyHAja8Bz0ze6nfhH7IJgZbyBwwrUJUENch8yWMCcndb1z-t0qzWSB5o_608FVt85IB1pr2pOBY9kKiNQTeEEN4FvR9L73Kxepo-XJiQqAcDiQEXLC0IZO5_tRMelUVG8V7ZTLlwzq2WzX4Jie3XOU-sWuvGZ9TlvuuSV_PFxUr-Vm_T9UczvkCNbmxUOMSnDwvNFR2u5w5cMvJVh2qA-cvp97HLYJKO9yn8cqEWRZLf3eMa-lDhpqaGkiUK9M7OUGLx3M1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=u_Wes5qm56lD9bkjtDaPhrmpes2_LazqUCE4TjoXaDEN5QDbLdc2kHcFMGuFkcZu5nXae6_40hnV3Gaz3GmuQObui-F_ipVEnm5AEYIyP4Fo_aRO6p7NvgdZkxwJsrNkb58MLZu9RdxKSU3Rg1AM63xKcADKWiz01sjIYWYbmxhP6fMH8lRMnMiaJAWb8PRwJNL-k-o80vXXFE9wBjnl6CqsFZ0m40NoRsB6BA6RCN1Wqc2dlS0YLil1E9pvZmrhrWHYZChOc81qItjRtkDvkuAT6xF34E6B8IfoEdQsWctZKUYrARyrvJ7x2_lF0PC9DY11t1hJ2A-Q3JOxQ1zaZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=u_Wes5qm56lD9bkjtDaPhrmpes2_LazqUCE4TjoXaDEN5QDbLdc2kHcFMGuFkcZu5nXae6_40hnV3Gaz3GmuQObui-F_ipVEnm5AEYIyP4Fo_aRO6p7NvgdZkxwJsrNkb58MLZu9RdxKSU3Rg1AM63xKcADKWiz01sjIYWYbmxhP6fMH8lRMnMiaJAWb8PRwJNL-k-o80vXXFE9wBjnl6CqsFZ0m40NoRsB6BA6RCN1Wqc2dlS0YLil1E9pvZmrhrWHYZChOc81qItjRtkDvkuAT6xF34E6B8IfoEdQsWctZKUYrARyrvJ7x2_lF0PC9DY11t1hJ2A-Q3JOxQ1zaZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Ww_02UfW6_U9zs7mMAQS0XGTrN61Giv1YUtctz9cGzQ-r2furyk9vrcHOw9R3cOGnFTqo9fOXk8SPlmElSUdDjSpe7xWApa4LaKgHCkWI1WfnosyGfaZDHT68FCCQ96b_6DoBwI0aSzn5Uf43_2ORuzWEotPIV4194NhBWSFH4WdaJSAuq3ZE8sid8q32dJ2EbcS9fnEUzcS44p96c6mDDZHziqFP_SPttHPLavvnwLqH3ZXOgRlG-lwW0gRIkxxiJaFwuVERB_u4UCAoPct4EAbmU51KG4iwcbgW-OVT_H8yq-MC_b0c5df3P6kFo6ukAEe-0YK41fToIQIZ91i4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Ww_02UfW6_U9zs7mMAQS0XGTrN61Giv1YUtctz9cGzQ-r2furyk9vrcHOw9R3cOGnFTqo9fOXk8SPlmElSUdDjSpe7xWApa4LaKgHCkWI1WfnosyGfaZDHT68FCCQ96b_6DoBwI0aSzn5Uf43_2ORuzWEotPIV4194NhBWSFH4WdaJSAuq3ZE8sid8q32dJ2EbcS9fnEUzcS44p96c6mDDZHziqFP_SPttHPLavvnwLqH3ZXOgRlG-lwW0gRIkxxiJaFwuVERB_u4UCAoPct4EAbmU51KG4iwcbgW-OVT_H8yq-MC_b0c5df3P6kFo6ukAEe-0YK41fToIQIZ91i4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EnxXzxN7oj5BtfttaqCnMnEs4wGEdCL92OxSR1iDsRuDmQOQLyg24jmSkTBncQ_zWz46EgvikRKsH6TEvQ4QB8nFlhSiYByFzZOnlaZHNmjeoBu0FwM4F5VcnlUO9QCCxyXDcfj9rFot7GsBij9l70PHfJI7-uAobr2ZGWxqnw4iFbXwnvadVSdmmJX_rg3Q1e_pr_7LsErbRjk1jXuJwGc_fnnPJcQTAf1koTIvarCuRU0Oq_Q8Lc40X4AkYENMFlqCSmhjEi3XsCHlGj9lrCdowhUL3LkuAuUh0nTGgoRvZcbjA33WL8RE4gKn4-z3MBCKPe5ry3_Z-rYp4SYEtw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=vZaY5rl1iSLzonNlQKbQM3N781I-LEYBjzoYvH6tk25iBdUSSjGAN_Yk2BsNwcnkQ4KTkkisGiwEiLMILCgoJzMfpvCwbgef52umH8JA9bCfwHvZhhmFa6wMGSSoMx8g7eA6SX9UyBTFudWHRQv0uwThGMxtqEnt4OEn1UiqMfJon9ws3sbWsJTc45hVZOkV1a0Ju6pnpjdkVHote8hxeu9Lpt9bAuY6lG2awhuzNxkOdLdAo4J-W6Z6lKyrcXQ2fg8fygvfAjRmH222c5VOsxo9ROYpjkGaeGiHzOdVHGkXbjE-uKh2KjTzLYhYkUgGGQZS6B8CAt_wZkC195OQhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=vZaY5rl1iSLzonNlQKbQM3N781I-LEYBjzoYvH6tk25iBdUSSjGAN_Yk2BsNwcnkQ4KTkkisGiwEiLMILCgoJzMfpvCwbgef52umH8JA9bCfwHvZhhmFa6wMGSSoMx8g7eA6SX9UyBTFudWHRQv0uwThGMxtqEnt4OEn1UiqMfJon9ws3sbWsJTc45hVZOkV1a0Ju6pnpjdkVHote8hxeu9Lpt9bAuY6lG2awhuzNxkOdLdAo4J-W6Z6lKyrcXQ2fg8fygvfAjRmH222c5VOsxo9ROYpjkGaeGiHzOdVHGkXbjE-uKh2KjTzLYhYkUgGGQZS6B8CAt_wZkC195OQhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ixlefmR8gECEJdoV_UoTnPaJOntbTpaM7kRxvcP0aPLCOaN7yFSwwczvi4w7nDId5a6UDTb4vuHrUKwPnu-QDc3dHUQH7GS2q4AeW2a9M65n4nX8AJkOmgiytOlhYPCVou8Ib-ZUs08wv4QfDmW9nU_-qjFXhpzBWVXDoOawjcvjmYZq2RoBr_OZ4KJpWHaYjDuWPOygvQt2mI3kaIym_Z9FUZM7D1DK6amESxOIQKajTo54a6Nl2p9tLTAysoYvPN6wkSdP27-J-qVByP3WVGSqtA6IXAYtDnFER5Zn5GL2PKWidYKFIVdLqwON_HU0QWQY_-fE-8S_b3Jlar1erA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=ixlefmR8gECEJdoV_UoTnPaJOntbTpaM7kRxvcP0aPLCOaN7yFSwwczvi4w7nDId5a6UDTb4vuHrUKwPnu-QDc3dHUQH7GS2q4AeW2a9M65n4nX8AJkOmgiytOlhYPCVou8Ib-ZUs08wv4QfDmW9nU_-qjFXhpzBWVXDoOawjcvjmYZq2RoBr_OZ4KJpWHaYjDuWPOygvQt2mI3kaIym_Z9FUZM7D1DK6amESxOIQKajTo54a6Nl2p9tLTAysoYvPN6wkSdP27-J-qVByP3WVGSqtA6IXAYtDnFER5Zn5GL2PKWidYKFIVdLqwON_HU0QWQY_-fE-8S_b3Jlar1erA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Hpm_mhSJBDtumepTCuRDYoplXyoraYnKTwTqa0HW_FlcNPN7IFMrvh1IDqbq4PAYZIGBdNxaKg0SKoXKTdiOqvLqxBQ6-cxYfAv9l92ipXsBWJa-5qmU3RyEGjOdHRAxQJF8pcJG2LQW2F8-M6I5uzl9E20ODSnsld-Abj3phUWMGwBTlTdM67hxyEGo9BOPftdQJHLQ1sD8-V0cTeDZOApDZEcJL9pKSzAN_7F-7L6RBsd0Ox3nmbOUeF6DmTM5DrvyJRhRilGU76w8yRkbGMcbWG-Cu3MlJC8cCuhKC5gH-Lahih9Zw8rQa_fQMWvR1-g_g9j4MkYvVV5C6DaN3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Hpm_mhSJBDtumepTCuRDYoplXyoraYnKTwTqa0HW_FlcNPN7IFMrvh1IDqbq4PAYZIGBdNxaKg0SKoXKTdiOqvLqxBQ6-cxYfAv9l92ipXsBWJa-5qmU3RyEGjOdHRAxQJF8pcJG2LQW2F8-M6I5uzl9E20ODSnsld-Abj3phUWMGwBTlTdM67hxyEGo9BOPftdQJHLQ1sD8-V0cTeDZOApDZEcJL9pKSzAN_7F-7L6RBsd0Ox3nmbOUeF6DmTM5DrvyJRhRilGU76w8yRkbGMcbWG-Cu3MlJC8cCuhKC5gH-Lahih9Zw8rQa_fQMWvR1-g_g9j4MkYvVV5C6DaN3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=f1Gc8OIf5yO4xBSXuLu1y6MHA9M1Ot8YiV8BRJz0LiYJylrtZbujlzty2HegystySeHsC96n-ccbvvX4f9Hzgu4cxqMepwOCRaZiELqnDOMNImXMddaNhBSfKN7fG7_1q6gxcT7rwHw1ayFp1gS0PdQNggNEMs3gAhKAYoqEpY62CRxUWHdfglAgSntOjY-iCUSnbCj5akh-n3H-AYLgFwUdaZ7dhqvyBeWf9dtYYAJ7HwYR0kw9ria4uNXOeP35qHa5WyX-lHWgzuTWe9PC4vkCg0cvaWpgRYlK2lYfU6CqkNmsYA08QQIchG3B_Jh9R52TSfw9LZ1gSmceOX6QCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=f1Gc8OIf5yO4xBSXuLu1y6MHA9M1Ot8YiV8BRJz0LiYJylrtZbujlzty2HegystySeHsC96n-ccbvvX4f9Hzgu4cxqMepwOCRaZiELqnDOMNImXMddaNhBSfKN7fG7_1q6gxcT7rwHw1ayFp1gS0PdQNggNEMs3gAhKAYoqEpY62CRxUWHdfglAgSntOjY-iCUSnbCj5akh-n3H-AYLgFwUdaZ7dhqvyBeWf9dtYYAJ7HwYR0kw9ria4uNXOeP35qHa5WyX-lHWgzuTWe9PC4vkCg0cvaWpgRYlK2lYfU6CqkNmsYA08QQIchG3B_Jh9R52TSfw9LZ1gSmceOX6QCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KSPnWRBPXcP5QqWGdVA6n89xkVBUnC9tRRDsEDHURyCW73zgybeGzYiaggkX42d_9aHE3K51Wzn0FMXKHBq6iTHUtEUzKfPpD2RCP3dyrdJ6gn1Cd1KsJogjdvD0UliCxso_lWX5xCMcfrd_V_Pq0V_hPvwIxESwNy2T2Wj6_aecOMnA9L8VVYdbXmXr9HSBHNQR1HFNuGipyS49c7rKaF4Tc-U5ko26OJ5ZYz-XlS5lCOv71GKS-hzQlae3XugWNihMShNUJlNdiCyJS4uqiqGrZzfvOZwtcEnXIYpHrKArluGaWnRBVwsX2EexVFx8YCnz3ehQI-LORWdIcyIZ6Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=D1bigj9xpMf0930VJ7IRFB3nlUM78nQ3DlxxF_EktfMaCE52xKcEGArTcrCpV2mDEyArGcDEFlbuyOOUnXXX6ujXIxbpa6NzSLXLJwJhKaptgw0WnvODPTx1yRi95UI5a91hWWoTL8FRJpl96-jzV1FRAcUiAjyIpqfNjfGje3NiBowpSrBhNOXvuPkkWSvq58XaP8W0yG2qgNrI-DBNT2L5ei4-uuwz7o9RBIAumMhqo5kpFnI_wiJXPUg7NETt0q0Q0ZrNcSAuP4E2lmB68YYPhVTHAnRyZMP_CKRaplgEM1yK_QRmYGVbqrbyRDELM2Eue0oiyg8Z2hQeCdeQMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=D1bigj9xpMf0930VJ7IRFB3nlUM78nQ3DlxxF_EktfMaCE52xKcEGArTcrCpV2mDEyArGcDEFlbuyOOUnXXX6ujXIxbpa6NzSLXLJwJhKaptgw0WnvODPTx1yRi95UI5a91hWWoTL8FRJpl96-jzV1FRAcUiAjyIpqfNjfGje3NiBowpSrBhNOXvuPkkWSvq58XaP8W0yG2qgNrI-DBNT2L5ei4-uuwz7o9RBIAumMhqo5kpFnI_wiJXPUg7NETt0q0Q0ZrNcSAuP4E2lmB68YYPhVTHAnRyZMP_CKRaplgEM1yK_QRmYGVbqrbyRDELM2Eue0oiyg8Z2hQeCdeQMjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=di_8wTpeHkGtEHes-wvu4WLw62XLs51GBlckkfwUb-2Wad9DnTirO2f-H7cNQgT6hOxcPSD6hYyQ-H4jexNSRYmEDcycb8XcMouhZo97DPoOiroLonSJi4B7NfDt51uaa3sebjccJRYfcRIikH5SbiXj03kMtXnVrDysi5C91mX6YHol9QEKZ1K3JoQF23wZD6ui9M941gU8i1PzALI3nxOkCVk-45w98iHx6OxOrZ7Jq1g0VHYnVA_3sz75uEHEUmx4GYsioqQ1iCxLVVLCweMQialb5UkDV-3YnMKWjgPR-HRDlb--KOYcNvimpIa7LfskdHpxyCtjo8juUlW9sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=di_8wTpeHkGtEHes-wvu4WLw62XLs51GBlckkfwUb-2Wad9DnTirO2f-H7cNQgT6hOxcPSD6hYyQ-H4jexNSRYmEDcycb8XcMouhZo97DPoOiroLonSJi4B7NfDt51uaa3sebjccJRYfcRIikH5SbiXj03kMtXnVrDysi5C91mX6YHol9QEKZ1K3JoQF23wZD6ui9M941gU8i1PzALI3nxOkCVk-45w98iHx6OxOrZ7Jq1g0VHYnVA_3sz75uEHEUmx4GYsioqQ1iCxLVVLCweMQialb5UkDV-3YnMKWjgPR-HRDlb--KOYcNvimpIa7LfskdHpxyCtjo8juUlW9sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WdwGvkbJWvMFrlKaU1ue3BXcJpIuNAbKNlBQDRwfj0Zxu2IUYkkVZQ92uPR29HsoDEJMhWG-eZg1GzmSbxKMXs6Cp2KCaKgFXiRAVIjY8yx-cCuhr-nB5UePeBAkTLiENu-r3tSxoNhAbWHabq1ZR0xM5eITIGSNqZDlMKvEmUcb-EgaakjZxToDWkE8kEWcBmcHt7-2PJidM7c_y7gsZOi8AUgcu2MGx4KjBaM6wpKDC9p8imqHiQTs-e3Shvq2uw_Vn5-EGxd2R7S1yF8x-S2FfWzJv6UhG0RqtLI8cKgegLNeRbOvIrmWvTz6SGQpDyna0aSL7_cafexksuaZaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F6Bg63NbYPdEBQKyyl13HstLCLnQKg1Jumyonyn3w3z1mjv698J3EyUuaKeZ7VBwp6d23ZcEwLGkGITLIe4n7cCa7DTzipXs2sOA0h-dDd2lBlUN8I5Sew_4yFckvcd1GK0LxGqyYnV7VzkdhMDNGgLBdKjYTz9qpArOGX5qrwYXE93FiI8GPeDI67F9KlzEicwJrq689xThO2ckDVoWSNmJXetolBmH1Yynrh22xdKi4f-GnfPf0_reJERYSX1EkyS4lfKXs1Z9KiaWeWXeky8OUU7ZTD64qfzdAc6ELb4zmCTmn1blG_NBYophFxcHNXdIcqZjWQNLvk06Zt7-KQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=M0umRpfrkVEZKFnMggbiFzk2B4HT6cdb4GsnIa_wzO_1FW81pZdi5rbVn9zERBw0jbnVvHn33MsnoO8GLcBhRLOSZ-XwcyvChHEHuWVLZSb-R4pxLgzwdKCHOUau3-5cbjR00II8gPMq8PItVf7hdgRnHQWFnYy4Wgke-WWY48RMnUFpUMSYuz-n7CuJZZ2SB6imX1WQj2QT27_wo9CRau3cz5yFLsluLpepGmDfc_4Rgj4e5fHy1OL9SPo62ghwXKODiGxpnljuapz5i2Q65ComfB5xwxj3rY3tq92yH17qZ4osnpbWtb-MAZRnVBcBp5V_3BG0EAigfvbJ2bSv5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=M0umRpfrkVEZKFnMggbiFzk2B4HT6cdb4GsnIa_wzO_1FW81pZdi5rbVn9zERBw0jbnVvHn33MsnoO8GLcBhRLOSZ-XwcyvChHEHuWVLZSb-R4pxLgzwdKCHOUau3-5cbjR00II8gPMq8PItVf7hdgRnHQWFnYy4Wgke-WWY48RMnUFpUMSYuz-n7CuJZZ2SB6imX1WQj2QT27_wo9CRau3cz5yFLsluLpepGmDfc_4Rgj4e5fHy1OL9SPo62ghwXKODiGxpnljuapz5i2Q65ComfB5xwxj3rY3tq92yH17qZ4osnpbWtb-MAZRnVBcBp5V_3BG0EAigfvbJ2bSv5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
