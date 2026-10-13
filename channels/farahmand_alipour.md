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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 08:11:45</div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frdnezwfe6dK24lx2DR6Frc9c6TQo_eAE7f4ykAb5v5ZT9NS5PO7xhkPsITr7dyNhIeKUF1ECEYZlLrlfsOQz9BpYdVY4ZlTkUxpX-EW-t5f4XdBhc8Nwml9or6lDJAie-JGRyPwLmpkt7-72oNx7lueCi3LSnpW4it-yuIBp984bw41xuUuXMzqC6U4zTNZQ9Kp9cBJLAjglkbTM-S4EU4RtaNUCk7SUSkjIYzabyYp1EeLUCUppfWPt5H9aIrsXo-6L2MqbF-F52qqOE5bl9fVavmvJJAn43LY9ET4Bt-mFw22ym_murXzcZYMnGpDHPVLvcjDG4qlsFcTUMgSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8XuoRqaGqZ5eLQjIk4Jo9q4MtQMauAuh7EynFzh5RkF5W21kXEewb_T19kZlDOx5Vzn9h-RQx5e15JD3kD2EV44aw-XefHYUTvy3a7yd1lzvP6vkivvoGaefYuALCullOQ9nY65GrUISG74y4iAPStgUE79YXKXv3Wcm_lmPnCJWLue4Z4y8Z3i1zmK0xdHff6TT4wtRJ7lEVrBSR8yLdYlGNQxB58mKthJUTh8SmHUZT5Q3sATzwgvy9gnT3G-D_ebC-pvjRhdM0cgf4NSC0bZXjTvLhkOBSHweL5OUnpKr7DaYT4AY1eKeUuw_veiQ9fjNz6kBv93s71yeabwKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8wi9VVNi7gG_7F6A6GExdZK1mX520doutT9qnTRYgtMKSOxfJXxmOc-E325w2OvUtSd-ciERsn3K9wIzJlnw84hXRkIrC2D5PyJpPAU1iXOwYVjJDhsibPnAByBgJhpf5v4bSDL-gxlXRDaqsIFkuEq5z9Lr26aC23krYItpyR5ZMSpFVExVdkQT4IfXIif4H5SsgC25OuUWcPJudYdY8yoXMDcsOM8skl57bZxW4F4JCfX2-llFYvsQtcbLXdAnAv58d5e_FL3FQ30mnRDw8oFpfcVumQi6ga2Ob9Qhp-nHTJzbyRKeqgK-sHwDR_nZLNgdaDw0Jdcp5hje1_n0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZW2oR2varHvSKjOzU9O58RBxqwMMOKMSxKCj8qT3CfLkBkwUpI6zZlCfNZrRJ0T_BjJQ36C6z0Gi36P5GbhaReX6yFYCeQHTGGpZNn4b2J86zOk26kVx6eUZC4EWtOk5dIQTB5OkEA0j2f9xhYyw_5e5MQbhIyW5O58LsciyAdbLd9Sqa9neSbzD8i4_KZbgleQZlwjFzDj4WyW3V6oFQ9IvPT_qUGzp9ZVAk0HfP2E8ygUrJFlVQ7bwDQ2Jv6EtJCFc7Kgs5Lv8_D2Q4FUrSbW6w6Fjw8XTN7AQe4u9_uMrNB1uvNJJYCcErqCHmsvNuONf4Bnc9GsEuozm69C5jQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=nzK3d7_XFjHjDTNCNASmjj65aToTV5gSqv4byaENgaYdFd0qSsOWMeRLfivnNEQk8HE6PcBszyYc8kPNkcnzWeWQZnFO8i2OvyUMkTjqm_NeoGotcfrDGWlWLRu3IT8iDZeYh5fZu-4PicX50_K_yCFsRRVlZMmLh3XKeB6QVedMNviibrOnunV1kkSq9fEil6BkHePZwhdFaDSfWJBuf-tCrFeLZAxj0n-TN_YtFVUgeTC_pUhFBG2zfktmmxOnZSBuPTi2fy8a_2KGo6ARvSQ4E7C4vZb7C_2GV6j_5zJlSHaRUbgiBkznOMJWMZYubB4HCQIqFzqa-VCZRxeVog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=nzK3d7_XFjHjDTNCNASmjj65aToTV5gSqv4byaENgaYdFd0qSsOWMeRLfivnNEQk8HE6PcBszyYc8kPNkcnzWeWQZnFO8i2OvyUMkTjqm_NeoGotcfrDGWlWLRu3IT8iDZeYh5fZu-4PicX50_K_yCFsRRVlZMmLh3XKeB6QVedMNviibrOnunV1kkSq9fEil6BkHePZwhdFaDSfWJBuf-tCrFeLZAxj0n-TN_YtFVUgeTC_pUhFBG2zfktmmxOnZSBuPTi2fy8a_2KGo6ARvSQ4E7C4vZb7C_2GV6j_5zJlSHaRUbgiBkznOMJWMZYubB4HCQIqFzqa-VCZRxeVog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Bm-NQRbwnREN-itp_baDJP2ZmPkeRLDBAJ8Z8R5JS_Saq_cb_Ns-jOEumiBAQiyYodE13oAmn9rm-LCPRponuwlow8Zqa9FVHTxm3cGwdsE1b8T4aeeLozDObXGPb8B1sMceKKQpYpGMNVUSKvwRaUsL7Gnfn64DdpA54tig_8YkriGHmNHLFmqysAYavtUxSEJAaiyxGAhSIZYH5oO0iD3Zos6VMEn2MUrrB-2wtktal-1-eYW3RTJdOnhyZj0axyfwVlxvPNJAA-ir8G-Vx4WeVZ9k6lZ0pfI5ySCd1b-Zl3RG-aRU5GKuj212upuQpZRMWj8PAdBSIF3OVXQ-3FYFwLz77We5quKPmAOkrzw_sgNUDdnJJIKZtQpmzx4uMeb61sRkPpNd3UIeKuqQy03VtN3ft4IsR0ph3jRQRIgQfGj-sdmWZEpmwgIXxVxERWqID65Fdp1gHLI0zaeu71oRiMEH59fCPpqZtgStL7eORE1chv9lbH8nnXLHpR3mDUps1qQdhaBVDKk87y7pd4uZkBcN78NG8xTz-nGbZNJeWxv5YlTXZysgaKvHVxKIvClQpYLQgps_6tdrFR7Qh2BTYQinG1coCxik9_yqYjMYhcC7f4suXOS2Z38o6eWdp3j1GELykWIA8DIZAJFKQaJ0fd20IdbLX3sQnOrdZ7U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Bm-NQRbwnREN-itp_baDJP2ZmPkeRLDBAJ8Z8R5JS_Saq_cb_Ns-jOEumiBAQiyYodE13oAmn9rm-LCPRponuwlow8Zqa9FVHTxm3cGwdsE1b8T4aeeLozDObXGPb8B1sMceKKQpYpGMNVUSKvwRaUsL7Gnfn64DdpA54tig_8YkriGHmNHLFmqysAYavtUxSEJAaiyxGAhSIZYH5oO0iD3Zos6VMEn2MUrrB-2wtktal-1-eYW3RTJdOnhyZj0axyfwVlxvPNJAA-ir8G-Vx4WeVZ9k6lZ0pfI5ySCd1b-Zl3RG-aRU5GKuj212upuQpZRMWj8PAdBSIF3OVXQ-3FYFwLz77We5quKPmAOkrzw_sgNUDdnJJIKZtQpmzx4uMeb61sRkPpNd3UIeKuqQy03VtN3ft4IsR0ph3jRQRIgQfGj-sdmWZEpmwgIXxVxERWqID65Fdp1gHLI0zaeu71oRiMEH59fCPpqZtgStL7eORE1chv9lbH8nnXLHpR3mDUps1qQdhaBVDKk87y7pd4uZkBcN78NG8xTz-nGbZNJeWxv5YlTXZysgaKvHVxKIvClQpYLQgps_6tdrFR7Qh2BTYQinG1coCxik9_yqYjMYhcC7f4suXOS2Z38o6eWdp3j1GELykWIA8DIZAJFKQaJ0fd20IdbLX3sQnOrdZ7U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FgTasXEllw1dxgHKxODDLlAiNqYGo51BcwtDxeS1n9C9CnDOBBbKGB-VirpOrU5fKnlroCOf5qCKAXzEUhKciSp15mlO8HjvSxEZvXnB4REYvLgbPwC3eBmzuKH-Qbm8SEJaeT2y-3J3WxN08vmUUs3I4SCSH_kulH_9pA5vc8x96Tqn6G1IVqy8rLTmSHqk9obun9dwV9kOO8VOOO0UQR0X2GxvDAsbuNfP2pWMWznScgJY1dFalk1LczBkG_OTyaMIgtqR6vHwFiZfSv9FCcWTsiq7i6KE5Z-qD0gHbHMZ8qRNUlJ4-pMVUqVG-3MwjyUdKs7t-GT6w7fSkV2-RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9FdU3PBgsF7WHCLYuKno0df1L_pOVWSGsme-7GbobjnV7VzKV5LAGlYlfWwrtjepufuWLzDbB1417zjTrUD22O7GyYRQGLHaWhaRRt0GVXbvBCJR2DJfCvowZEINavXhR8qv9ZqLl2yZUaXkbC9Uky-fq5M3l9HB4QQAEepiwXnZt85-uNFE7lyqLEi3ZwP_1bpr1QBDVGe4OyqhS4zaDiX3j5Hsg-o3YErb8qTfRXxApoSIPbm834THTZ4rloyEm18khErWKQOX-lZTTGIWlxqCTERkmG839jf8mETib3HbHERQ8PWI5UVLmaYb7eO2s8JrsNdvte1qCBuytNDkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y7IuG8ZPtBS9gGHyIGkcVjtyLn-GkELnB5_r5jnri15zC86L3V91jKbpm8fqJOTqyqnY7uOVhnJGaF8vsk5D6NeSLKQ2jfVAgR7GqQf64CB2zPC8ymAYD5LKo4gRjjs9I5owRYIWXyrOlRQNIU1KEePMvjVlmLDFJvoUHt9nWeO24SOSWZuBVtx9NlNjnOmZbiR_k4PmsbKc21V2Q0tfbPpnz6KLZeTca4R-wNqmmrcJXs4RrYdxLyYwLUGcdZCDQWUmprHxYvDXXMqZpxccKg0MLCtHfkQ1wCje9Q3yGkwJkOyQA3YrcbLj40B0cn2bLR_h1F5OSW90i0NfA-iWug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=kTTMi-vFUwQjFY9Mh3UmBFbfiFwSQLkuQaMoKizTA3bhNJJDUt_edaJd45tQGi1TE3LH9WCFUbfVnsaQyoFTyvLhLYdq6SbSyk8jtE-XnPK_6nw0LBiaukOt1TEWD4mTksB8m58n6KqJIlVWNzh4qurlm5XTL8wjLEc9oqrcU22U0EYZjykNnrImsEs_TsgNEGPiL_A8cvqi5xUXYX9LPM0pGdeGkz0XgICd1fc6pBP4B6776JUY1YLqtFGI3VI-SocnXXuz9YKVgYl118_9LG5SSZKxm496EXOZ5zj_QJwhOHhJOzfp2igfv4_8jR7Ek_JHml0Bh8-XL42KpzGDmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=kTTMi-vFUwQjFY9Mh3UmBFbfiFwSQLkuQaMoKizTA3bhNJJDUt_edaJd45tQGi1TE3LH9WCFUbfVnsaQyoFTyvLhLYdq6SbSyk8jtE-XnPK_6nw0LBiaukOt1TEWD4mTksB8m58n6KqJIlVWNzh4qurlm5XTL8wjLEc9oqrcU22U0EYZjykNnrImsEs_TsgNEGPiL_A8cvqi5xUXYX9LPM0pGdeGkz0XgICd1fc6pBP4B6776JUY1YLqtFGI3VI-SocnXXuz9YKVgYl118_9LG5SSZKxm496EXOZ5zj_QJwhOHhJOzfp2igfv4_8jR7Ek_JHml0Bh8-XL42KpzGDmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=VKM49xB7LEu2JrwlGCEjBGgnGqU1Xfk6LQVI2lTus2FAkTKhq8R5KBXn6oJ9e8875K9x6mC4rJGfldThI5JfXHfYiifgwlgh1VwmBb7LADg1G_mwEp2qzT2Ec3oCzouvljGyoUAg6o7ZHsApsbqOxBpkDz3M3jev2VIjvdQ6tcvgKGTzPP0ydFwrMMYwJPdLBLXp4yu48GGGYD5UG0bB-_ubDpj6zHkYs99AHuhFnGj7-Y_AV-oBR-X0-vcplSsKbuWu_TPaZ24k7u2FoRbJkj8E6X89VwsWhzMDM2pZ1MJXl07toWtZACATms31P8y_rCcHlo_A3rixOA4kl76tAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=VKM49xB7LEu2JrwlGCEjBGgnGqU1Xfk6LQVI2lTus2FAkTKhq8R5KBXn6oJ9e8875K9x6mC4rJGfldThI5JfXHfYiifgwlgh1VwmBb7LADg1G_mwEp2qzT2Ec3oCzouvljGyoUAg6o7ZHsApsbqOxBpkDz3M3jev2VIjvdQ6tcvgKGTzPP0ydFwrMMYwJPdLBLXp4yu48GGGYD5UG0bB-_ubDpj6zHkYs99AHuhFnGj7-Y_AV-oBR-X0-vcplSsKbuWu_TPaZ24k7u2FoRbJkj8E6X89VwsWhzMDM2pZ1MJXl07toWtZACATms31P8y_rCcHlo_A3rixOA4kl76tAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwKeSB5ydBFONq3gAF2bj4DZ5ndAvQA3GWX7Bsx_KQdJrMoKuMPbjQdrZfDiBMKz_2cJJ63qlPpvG7zcXvSMpDWXoyekvj8xFbj_1xylnCf5NpNYZhxfMhDqI6XtzM1RuCEU5US3zEuTMNxWlhSFyjbC3Ka83IGpUbdKTGk6zolMN-PW38LKyXOKa37eMlX4zxpiBT8GhQfP8uiG9pJhVuv29j_R4z4iPH1AI__4_d4W6PJJ1UMqrUd-YMqOpCTch8gglxTDwYBiALFyCtRqzSG4XAaJbZ9BDMGlT7IEFrMsV59TthpFqgInsLT8nUDaackZmI8DX9jgYoukafd5tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=kUWcxN7M9csD3qRLAdFuLB6B46qL0PbLpvGITIFEWszBgPuIHlqza6PfuWm14hO1iX58QWWGl8MCJ5jBjFy20mz3iG8faXmMUcFm07tlj0JDmlfwET0brbCUvrK6XeZf3gEgYFLRUaYiS-QSYW8WYqf7po_-lw80zUlSgFSAaXbKxrZUmrvhvcU0zjtiPM8Wz1DvwgCklc4K7oQYQI4va63zx3a6lW9kSSXD0R66MosTLUG_0XkghCXr8xSSdhZP6_PNPs9W3zX7OgzAeb26jWEEN16jZOo6iVQ7g3zcW5w8-mGCfYi8xwfOGFbHKdooI_3hPKqkLAbMKuuXUPq64X6H_XaUHVnzRzgS0qP2HHXZMzuJUSN_6_oSWKgyFihxjri_bjMbXdbz5T5opsksPcLilNKKNDqp-kby4AQOGu1bN96CYgkFRTcheZfFE6YoIExtvbTJUt_4Vy8OQtMqw39ntv6asPA5uVuiid8MnnrhIrLU4vsCeRDhl8SDOYyQiGLdFUKJtUote5kojkUtAfmOWIXjVgtYARkdghNp_GNBALEuRNZB2wXzIznXNo74lqK39h0ehq-YOM467_BbJP3C-rNeMlPUMFvS8By7qvIB3O5xiwkD01mGu-KO8hnMm9CG-uKBUicP4ei1JiNp-RdM9W2yfkHyd7aH6PLyD80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=kUWcxN7M9csD3qRLAdFuLB6B46qL0PbLpvGITIFEWszBgPuIHlqza6PfuWm14hO1iX58QWWGl8MCJ5jBjFy20mz3iG8faXmMUcFm07tlj0JDmlfwET0brbCUvrK6XeZf3gEgYFLRUaYiS-QSYW8WYqf7po_-lw80zUlSgFSAaXbKxrZUmrvhvcU0zjtiPM8Wz1DvwgCklc4K7oQYQI4va63zx3a6lW9kSSXD0R66MosTLUG_0XkghCXr8xSSdhZP6_PNPs9W3zX7OgzAeb26jWEEN16jZOo6iVQ7g3zcW5w8-mGCfYi8xwfOGFbHKdooI_3hPKqkLAbMKuuXUPq64X6H_XaUHVnzRzgS0qP2HHXZMzuJUSN_6_oSWKgyFihxjri_bjMbXdbz5T5opsksPcLilNKKNDqp-kby4AQOGu1bN96CYgkFRTcheZfFE6YoIExtvbTJUt_4Vy8OQtMqw39ntv6asPA5uVuiid8MnnrhIrLU4vsCeRDhl8SDOYyQiGLdFUKJtUote5kojkUtAfmOWIXjVgtYARkdghNp_GNBALEuRNZB2wXzIznXNo74lqK39h0ehq-YOM467_BbJP3C-rNeMlPUMFvS8By7qvIB3O5xiwkD01mGu-KO8hnMm9CG-uKBUicP4ei1JiNp-RdM9W2yfkHyd7aH6PLyD80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=J4P5m3n4gbAPWAr707SNJ_PhD10K_nsGCAFRKH5Fi32bGArAcwUW7ktYlHgnMDww9r3EkEjcEM77f0jwYFztsk2qrDoaLNqoI-BVCihqxLwA9Rgh6JHZ-RnxBIrSBIBKwStWZVW6_6X2ErYdLe7cnVSJpB_618FCSrEHNvlaQulsKwsPtu81JLLD_UXPY5LLg-3-WGyLd9PcwQzwBkpP_ctNQ3qwLW5Nb7f9gdPqVAbUIe7WHNeZxv6oFW1iE-WkM80E-pb4W-TZrHxTX-ekKYigwkou7YfHlBhEF3CndUi_YeuDar5xoRNCdTrMnzuJ5x07z3XM8uvYbRD8s2PdAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=J4P5m3n4gbAPWAr707SNJ_PhD10K_nsGCAFRKH5Fi32bGArAcwUW7ktYlHgnMDww9r3EkEjcEM77f0jwYFztsk2qrDoaLNqoI-BVCihqxLwA9Rgh6JHZ-RnxBIrSBIBKwStWZVW6_6X2ErYdLe7cnVSJpB_618FCSrEHNvlaQulsKwsPtu81JLLD_UXPY5LLg-3-WGyLd9PcwQzwBkpP_ctNQ3qwLW5Nb7f9gdPqVAbUIe7WHNeZxv6oFW1iE-WkM80E-pb4W-TZrHxTX-ekKYigwkou7YfHlBhEF3CndUi_YeuDar5xoRNCdTrMnzuJ5x07z3XM8uvYbRD8s2PdAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STtBSQzPZj4LWbHayDtn_RD7gvo-ptBAnvyw0J3tG9KdvRBCeaQpVCUEGAEJiDKOfEp3ubzBsyTLzswI4F3hT4x9l5_a760Wz7vpvNMKP8nXllCnXlum28x5RU4o6_CcHXm0Cn68xskqrLhmxgmBv-pP_Upy3h7XW5Ce_lxAHUUz19OdXUCj2FwVy2G1Jx5EmATNjWiv8VxtkYAsylGReqsVik6v8LyAvvLNfKfZFfe2ixhCr2bWVRRxdQDgoSkt5C-5JLjlaqekbrk1LPUXFnQeBJR2zK8_DPX-4li6gEkpT-mDNo-F8VOJ7HZk73G5DCTo2nuWlNavnnlRSP4WhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=W2Z3zH4x4lsaCzWRgH_PuvyKJe-9dwbYTptp6G_AMzDWTxPpxgauW_VHSFa4yZkf9r81wXk4kT6bDGtug1RFbZ3pvjBrx74fnoS4DJmQ8BT7ihGWLRtT_6jZylznK9vnLFNnZWcfvd66razb7sN_hjk6YA8d3XEro4v-JzU9KMwSwSnsV4_J6tURLXLoyrGlkZH7NTPvYqzCge4RUKLMF7InPsTsSLoihNzLrmmPuDiHRobqHuDPJiIzTrpYy4Qa4STf_OOT_1vQahPHqHpF544JRDCTHhuLCXKNRUEGhIzE-75u3O1G8mcvGwq9gsYeG2bowb31jS0OxBo4iWtQBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=W2Z3zH4x4lsaCzWRgH_PuvyKJe-9dwbYTptp6G_AMzDWTxPpxgauW_VHSFa4yZkf9r81wXk4kT6bDGtug1RFbZ3pvjBrx74fnoS4DJmQ8BT7ihGWLRtT_6jZylznK9vnLFNnZWcfvd66razb7sN_hjk6YA8d3XEro4v-JzU9KMwSwSnsV4_J6tURLXLoyrGlkZH7NTPvYqzCge4RUKLMF7InPsTsSLoihNzLrmmPuDiHRobqHuDPJiIzTrpYy4Qa4STf_OOT_1vQahPHqHpF544JRDCTHhuLCXKNRUEGhIzE-75u3O1G8mcvGwq9gsYeG2bowb31jS0OxBo4iWtQBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi6K2LmyBwkxxmRhiGIuiSBmtpeVzFzqrSg-sG5fP2TIp32nYf33TUdcF492zoC5sPfvAmrOcUPN2nRJkkcWRRfrVZXPNEyVv3YXMMdik4ChSj71y_gaLjm0QQfW_XNFbv78JG5JgycMpwSHqU6TH3NxIP-9VZcwoLO9nC8HHaSUUyhUzYUjmU_24Wlumeha-y1-WLwKBeKgMCvdCpSS0prsImFcnjr6xR7KLuWA6JKf2T0hz7qmHrupfBg69yqTUFjU198-GAxvS83PBNPwMEYSRi62g86vn0MfoRBwsQK7slPIcQmO_pOo0ayW9C10ZrJebWAiID53NARFalBeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vj90AS0aMeInHlucQdlM4MzftqvZXtUIQpA2nJmnpEDNBrfn5xhB9DZnKDnLVCSuxPQ0px757eEamGIyCeF8RARY0pnXqQ0KGthpzuvI8PqqhAGSRlQ5JdOaxEAN-HK6MzAnZgBN_TQVHlkwPimcLTid_cnMmWWAjCpudUlsSRLLw8JZKd7If1_jYBcRoXu5kFcXTYXq4y9h2kgLJuHXkrONZa3KO6zb5KJiLsds5dwUJS39PYN-YMCb83BsqoIKoogyIQpyODAxtcmKIdrTUN9MaWpm3UnefD-C54btVyL0rjeHeVIl33QMwUIOM97tIrdLjGXtG-pCbs33VggrRA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Mo_0D449HLbbf0e21HozCF7wBnXl3P1_Ho9YrmSKTnPw6QgDxqjw2Pum5eEXBcW5ZVyYM0EvptH6YclF-zA4yaNWKjxs2XaMIVEDpWVq5Y1bIKn3h4VfwXISKUWgyIBNBF0hnfm4MsBEIjL-MXjcHYbqKRpdY6R306R7-zX6z97C7xr2SlCw3sz-pBO3G0PLELuXiy-Jmi3jh5aYCP2I2KrmFyarxF9NIhKdrRiGQgmwIIqaWLjgSGIfGl-oQZFYYgIyNY2q4CJ-v-9VzOFffaqhm2Xnh9WhYRG8lY4zB2TSDnFCz-rDF-ZRMPcJ4rbS0vv5WjarwWlb0lePnrwxu2umO5rkjqhEl5wPiDvEYv5o2oUURsS0HmPtLUV19mnKb-53Ek5BrcpUIVcGBDWTZXba61v4GK7FQkCf47T5rBIQqRxdpdJ2m_nuR7kSabdxrkqK6PNB3m1AeJAGylRNU6LKt7JeZ4Z5PdK7hsVdS5tsfwZiFZuc4tw5xyQvFUv3nkr0elThEM04OwQ69fJizMrgTfURqAmKgzu95yQjDs64bZQMT7cUjjW-ValO-G57P8Xc9uYwAb7Y7AGQejwY7izP3c_0KVQn3l9yN2oR7qQklRMeJ-BGxn98SYWNyIyGYlSnz4tjazX7NYSVxTuiO0AjTMiRz6CiZMibbj6atX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=Mo_0D449HLbbf0e21HozCF7wBnXl3P1_Ho9YrmSKTnPw6QgDxqjw2Pum5eEXBcW5ZVyYM0EvptH6YclF-zA4yaNWKjxs2XaMIVEDpWVq5Y1bIKn3h4VfwXISKUWgyIBNBF0hnfm4MsBEIjL-MXjcHYbqKRpdY6R306R7-zX6z97C7xr2SlCw3sz-pBO3G0PLELuXiy-Jmi3jh5aYCP2I2KrmFyarxF9NIhKdrRiGQgmwIIqaWLjgSGIfGl-oQZFYYgIyNY2q4CJ-v-9VzOFffaqhm2Xnh9WhYRG8lY4zB2TSDnFCz-rDF-ZRMPcJ4rbS0vv5WjarwWlb0lePnrwxu2umO5rkjqhEl5wPiDvEYv5o2oUURsS0HmPtLUV19mnKb-53Ek5BrcpUIVcGBDWTZXba61v4GK7FQkCf47T5rBIQqRxdpdJ2m_nuR7kSabdxrkqK6PNB3m1AeJAGylRNU6LKt7JeZ4Z5PdK7hsVdS5tsfwZiFZuc4tw5xyQvFUv3nkr0elThEM04OwQ69fJizMrgTfURqAmKgzu95yQjDs64bZQMT7cUjjW-ValO-G57P8Xc9uYwAb7Y7AGQejwY7izP3c_0KVQn3l9yN2oR7qQklRMeJ-BGxn98SYWNyIyGYlSnz4tjazX7NYSVxTuiO0AjTMiRz6CiZMibbj6atX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W16XTKWx8894eeyikG8f709GX_Vcbnrvyogu2oURwjElZ7MH5_T2U2PoQkR8dq_VsiBI0ZyevOWebHbkWfRNar4lS87GQ79XPOAku8XF-nFx172PZVnokrJ9yK1Xob5WN2jH-0ccZJ6u8cOF8EIGlP17T82DQRhj1WQ-wFVKlfTbORiVb6aXhA3ZXQ0hRrtWxkAlRDwkJcfsIbu0D0sRYN3xdqZtdG9t6PkNQ4452_0hVRbOVPnWv6p1usDox4b8QjXUHailRpLc-pJtkUabaDPGTl5TQr_lpB4AuHqfNf1liioXJVtwrI_GZnqeO7043ruoUkGTlv9JUhxPxyo2hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9asPwmHiyvzkkTqLZ-U-SZG_WnctZYp_m0WsnGuSD_a6NcTJiZdFw5Avdr-HWGDje7GVtqrbk3kyzFfsP0K6GRU5u2iGl7G-wu1fz7f9-09SIqffe_83iJcJzm4q-MkJPowgJp_eRXiHhu16sUCgHQto5VNM-k8wQ77v4GgtA6DHwck8i8USy93AT8VzC3PaPJobP3tcTjJC3lq7_tNc0CkVZ-7jh8I3lrlEuq6vZj9tsKC30xWNZoXawNAcS2T-z07spZue1m1y3_bsi2B4q7RVPjAuSEjemHUYhQVOZ3PPQ0S6Awg42bOoEf3cui9OmhVht5uw1O_QsEN9U0ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=nmWTn_pG87w_teuK88JV3ELohkhwQpbvGVuTVdCwLo0Xlg1vjwDfYV-TZoxlBTVw1orzyQ5KIkJO34MdSiSZU7111d1teqQEzdVsGSiGqBQDMmAyEhs7NVUA-pZz3kHwCzXMSKECJ_899bAmj5wz7sPYajXcz65w2u-PCB7b_AOAeKsGAd_u-HMk65N2kI4OZ3Qtl9lfs1OAT0cu4pLq3oMJrFPmZYl6GfA02JQfmdtAltCFgMjxwfX5HOiNWTUeBMx4xJ4Vl7bOqFeGyEZScS0p6nHyiPQTLLF-IEumNC_x1tZ5HfTH9Tm5cEaUFeyLCmeIN6SLdDZIEmvr1X2Kmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=nmWTn_pG87w_teuK88JV3ELohkhwQpbvGVuTVdCwLo0Xlg1vjwDfYV-TZoxlBTVw1orzyQ5KIkJO34MdSiSZU7111d1teqQEzdVsGSiGqBQDMmAyEhs7NVUA-pZz3kHwCzXMSKECJ_899bAmj5wz7sPYajXcz65w2u-PCB7b_AOAeKsGAd_u-HMk65N2kI4OZ3Qtl9lfs1OAT0cu4pLq3oMJrFPmZYl6GfA02JQfmdtAltCFgMjxwfX5HOiNWTUeBMx4xJ4Vl7bOqFeGyEZScS0p6nHyiPQTLLF-IEumNC_x1tZ5HfTH9Tm5cEaUFeyLCmeIN6SLdDZIEmvr1X2Kmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=P6bfGUJ7gl3BElXLn-eMN0ew7s_Imq45kSgGch84f7EcGmmsAG2CL3vgfOfiq878ElT9lVAxCm__xUVKtNhCO9v6Wn18aicZW9AslQSQZMhohR0wGJuRUJPkTRhz8-UXFQJC4knULg4jsKb8sdjbA90dJ72ZVpdSwyn9JQXKjyeGTt08gDknY5fT3_xyIWalmj0X8PF13qs2PkemgsERx4z_HRaEDjzX_oyH45Ua71rX3676KCD5nXUkFI_7IH-tK4CSxtjwk5qwxFW5GFzWp0IOG4hhGH18s2h2_WpEXPaWjM3z-IUEQw0g3pZMcN02OU3yKEhEuy141pQcBSI5Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=P6bfGUJ7gl3BElXLn-eMN0ew7s_Imq45kSgGch84f7EcGmmsAG2CL3vgfOfiq878ElT9lVAxCm__xUVKtNhCO9v6Wn18aicZW9AslQSQZMhohR0wGJuRUJPkTRhz8-UXFQJC4knULg4jsKb8sdjbA90dJ72ZVpdSwyn9JQXKjyeGTt08gDknY5fT3_xyIWalmj0X8PF13qs2PkemgsERx4z_HRaEDjzX_oyH45Ua71rX3676KCD5nXUkFI_7IH-tK4CSxtjwk5qwxFW5GFzWp0IOG4hhGH18s2h2_WpEXPaWjM3z-IUEQw0g3pZMcN02OU3yKEhEuy141pQcBSI5Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=AWTs9ii_-Sq7J9FcU_83B-EIgFR-8J-D14cE4A7zYw7Zljlf3k8ofoevVclxL_64CC80SXmI0fyRy1lvPIWJL-cIHBDdwED79K-kVvM6dAfGautZZ8y0TpFqd2yXahx8AcDyyOVz-Ttu7UJqEKmzgvUCgJIN74_z3XYTNcTN9-CgamVO7NnugHSc7bdF-7PA2UpP6CPaIMbk0tU732UmXqOc-dIPvI3wXC1z_r7P6K4Le6jKMThLkRtyI4sIcBuP8qR2FTj0z7UESVvoaLQy6gEIwMbSLHdcmpfLxBNYdHcZ_oMkIEPjgfW-eAv1u7-QRC9KTmVIiYEjuMYW9-MU9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=AWTs9ii_-Sq7J9FcU_83B-EIgFR-8J-D14cE4A7zYw7Zljlf3k8ofoevVclxL_64CC80SXmI0fyRy1lvPIWJL-cIHBDdwED79K-kVvM6dAfGautZZ8y0TpFqd2yXahx8AcDyyOVz-Ttu7UJqEKmzgvUCgJIN74_z3XYTNcTN9-CgamVO7NnugHSc7bdF-7PA2UpP6CPaIMbk0tU732UmXqOc-dIPvI3wXC1z_r7P6K4Le6jKMThLkRtyI4sIcBuP8qR2FTj0z7UESVvoaLQy6gEIwMbSLHdcmpfLxBNYdHcZ_oMkIEPjgfW-eAv1u7-QRC9KTmVIiYEjuMYW9-MU9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rf7uT97LHBU_kJTtdb_m9rbo-Jid7bVeNQZAXVbp7ABo_jnrfV1ZAtvA2pMwCQDo6RupJI64U0Irs0x5yQl11Ar1R1FUzoRg_7COph6xB01ctYEgOol0mvnE2BQOt5dy9pyuVqLLCBAKHbhGboqrE6Pltzf3Q0fJcqH8faXahTyHDpLnCB9CdyKEQhiUzRS0nIXgTxA8N9FDTbgwCpWSMM0t37GAYh2Nep3CdJoDlPMxRsyj2Ce_KeUY44mgSaJ_NNUmbt3V7etA-ONKomhDArRTOvdojKFG-xZi4ckbR0ruBRIYrCGO2WIQW7a1xVFPCVUibFvIWmKNnSJxFpDr5w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8BHxPERWZkF0aTYj8NLxRR7q8BVF5Y0qYeg4lPggfGk--etauaKV0PZfoznT2hZmU5uqOkWOMvnnDt5FfzatdnLEdnS8mMJPEY8mtK29xdAJkNSIAb4XRJCdblUaJMCqwWmuhmUpmX_81asEhIi02AbRDi2oF2yJobGPh8_wdw3FilBB1k5CNHSdbCg4f7sfmxIga9ydOErXgPISUqx0DHrZUrq-KuLC5jX3Y_EIWfWN3pZpPMhV_UNxJfobyLzgcC8JqDXO56jZgPEGE8Ix-5B-E-lP8ey7mOBz8N0aVz0BZflXuZ4ofBTXUGDz__JVZ8_ewVHaLe2sNJ2ecSEHUw4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8BHxPERWZkF0aTYj8NLxRR7q8BVF5Y0qYeg4lPggfGk--etauaKV0PZfoznT2hZmU5uqOkWOMvnnDt5FfzatdnLEdnS8mMJPEY8mtK29xdAJkNSIAb4XRJCdblUaJMCqwWmuhmUpmX_81asEhIi02AbRDi2oF2yJobGPh8_wdw3FilBB1k5CNHSdbCg4f7sfmxIga9ydOErXgPISUqx0DHrZUrq-KuLC5jX3Y_EIWfWN3pZpPMhV_UNxJfobyLzgcC8JqDXO56jZgPEGE8Ix-5B-E-lP8ey7mOBz8N0aVz0BZflXuZ4ofBTXUGDz__JVZ8_ewVHaLe2sNJ2ecSEHUw4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=PhJ1vX1H2y1zyBllOD3DrpKx3y6eukkioSFApdWveu9AasUY1aBRdbjI4uJeSh1yqCMpD1xh68rqAf-YBj2DWejB1B_yIBOKXcDfTP6F8_-_bPGHZyr5vnyZ61yitlBtbsopkWdBFuyYLzBIPrUEexM5w1Ri426kneYxsczo22BFkWOzFKG7JlzdNCYDLzAu6WpeIWn_j4guNXygoRE8jjBXbcxFnUNt-hRlJImb9wik7rfrE4SGzdy-Qbv4K1Gu_vrWiUE7qE6D5pTe-sj-3UM_cYvWERpRfy1aV-HpylAu-S62rUPP6q7dUMz4VrC6Ds4hnfIapyaXZVFnZFuhiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=PhJ1vX1H2y1zyBllOD3DrpKx3y6eukkioSFApdWveu9AasUY1aBRdbjI4uJeSh1yqCMpD1xh68rqAf-YBj2DWejB1B_yIBOKXcDfTP6F8_-_bPGHZyr5vnyZ61yitlBtbsopkWdBFuyYLzBIPrUEexM5w1Ri426kneYxsczo22BFkWOzFKG7JlzdNCYDLzAu6WpeIWn_j4guNXygoRE8jjBXbcxFnUNt-hRlJImb9wik7rfrE4SGzdy-Qbv4K1Gu_vrWiUE7qE6D5pTe-sj-3UM_cYvWERpRfy1aV-HpylAu-S62rUPP6q7dUMz4VrC6Ds4hnfIapyaXZVFnZFuhiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FhRDXbIVB4jRFnQni6NT3xYwX8IkMx5jejCqzdcEN-UusIsH2TGUuSBIOjKCnmntDWXVMyh-0k2Ck-s5n1_NLqr6annXZKRbS_j-VZt0v_L0Oz6M-XM5TUEqh38kbBWyAUad3N3s_lQIirtysL7bIwa9dThy_GOhuV1BweundXn8iouRWBr8ieVqRrhriCAYi8InA1loQAbWB9d6g1FmMVWVD_cQKRpFdN1AWBxrtTcspdPElyBNJRCLaLcOQFZuESPKquxXa581C8DkTpQp1NyPznOcA_co9rSgBtaeaQfh5d-rahiDNUy1tYqI-YzyFgXvbtGGYnoUdM896m1-Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=jT4jJYM6XaqCLNtO3YWx7ItQhsc09_wLIzgFZjFZMy6sK-Z0jFsK8v5Po_emDmIJpPQDSpZQf0-uzwCUrJz6GZhTTGPOKK0PrUtVuLvZc3DfOzOkwnH0qku-sPL0Xz7WLHL2QGBUO8r0jiz-6wGBH-xVRhbspO2BHAS0VdylYe1eDPKHGmkypCk_giluDMaT8T_wxHgEtS9h0-_DINrCvAi-yuGcKEOtUfh0zjUSSKxv-NIlC-rN94bhy3q0l7dWQkGglwgbsh1g5tnoxgDgOMtnkeW5ChQstH2h8GqlAu-t7jHm5ROTggAduhe6e-G7D6fVuExf18gs303tIsCxjrNcwQBfsanhMojNzfTAsd27k2FkqBqu89gm10KjAzCQ2MswFwNA6QkunQWuotu4fGvjBNIxQUWN0w3uyMJ83wK9cBZomJBF1SKlYfWDm3cxsgrA51yaNciAqW5wLlruHlLiutGZD-dfkL8Wl1V1nnob955UF1NUsCcn-JJ0aBbt2NA6lBETM0lO4QYBKBJA2SiX9o-AsK39R-sgW901PfNVFkXnQiqdTMk7FTUS09CsuJMkhhSQ9lhZUfK81gytsM0KUV-AVo7BydqlygfvbjddBXN7YMqoHo1d4nLKwTvEYIuywnPZzWBGgzIHabOjjmbMpO30ETje41hzGiKYXWs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=jT4jJYM6XaqCLNtO3YWx7ItQhsc09_wLIzgFZjFZMy6sK-Z0jFsK8v5Po_emDmIJpPQDSpZQf0-uzwCUrJz6GZhTTGPOKK0PrUtVuLvZc3DfOzOkwnH0qku-sPL0Xz7WLHL2QGBUO8r0jiz-6wGBH-xVRhbspO2BHAS0VdylYe1eDPKHGmkypCk_giluDMaT8T_wxHgEtS9h0-_DINrCvAi-yuGcKEOtUfh0zjUSSKxv-NIlC-rN94bhy3q0l7dWQkGglwgbsh1g5tnoxgDgOMtnkeW5ChQstH2h8GqlAu-t7jHm5ROTggAduhe6e-G7D6fVuExf18gs303tIsCxjrNcwQBfsanhMojNzfTAsd27k2FkqBqu89gm10KjAzCQ2MswFwNA6QkunQWuotu4fGvjBNIxQUWN0w3uyMJ83wK9cBZomJBF1SKlYfWDm3cxsgrA51yaNciAqW5wLlruHlLiutGZD-dfkL8Wl1V1nnob955UF1NUsCcn-JJ0aBbt2NA6lBETM0lO4QYBKBJA2SiX9o-AsK39R-sgW901PfNVFkXnQiqdTMk7FTUS09CsuJMkhhSQ9lhZUfK81gytsM0KUV-AVo7BydqlygfvbjddBXN7YMqoHo1d4nLKwTvEYIuywnPZzWBGgzIHabOjjmbMpO30ETje41hzGiKYXWs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtqTb9H6nLMXD9VtZwjW_Hfu1M6lyu2KzHUuRoJfQiEUE1pA8C8Lj6J-Wv27N53k2o0QhxgnKVuUlRKvfM2I6hzNYNAplPMbF__uep9oEB9GlBjPv0nq4EWe6Vt0-OtPv7RwoNhKG6SYU5VObhnc7-VGOysOTrp5xo69m_La5wcQ8XSOLsHXup_CWXa5qj28sAdEzPy4uu0fmIgGtydA34MlqhbHIY6-q_G3M9V5m0Wy6rwo_dkXEvsiGLYeeYgDNsxNsTybuDKL-fhyM5eOHtFTlcJYwmbQ71x0lz2o-gGMki2xAYm3Xdm7BgdLvtqWqpb-2UIt5dgJY7kQ4hHLiQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=dZq6bXxShegqavBQW75DTp3bhSoNFINHAD3sT2-1k56FnPhdF8hTVx3eHD1kPweyWUtRr_cCp2s_xm2bpKHI-_b8AZlQFmA1mVACAlUqnc76r0Vf0KJU_XjHaMdz6MgInwdusIe5GM8EKpzqwmIYC7tNiBlGJ37v35eZSqXgVHVG8TiNkvVVBMhhj8lKpY7Tm_oeNzH9ouhdy0eBGn1F2o_4bS0DF5OUmzKz4I-FQuJtkngy4N8h341TlRKhBfH0CcBLca3yKvSxBWabk9esRrTjBJ7bGiLC23JQSpsG2jc-OXhawBBWE4QDDdDqFBKAGSq4muGsISWlrcmJ3d4Clg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=dZq6bXxShegqavBQW75DTp3bhSoNFINHAD3sT2-1k56FnPhdF8hTVx3eHD1kPweyWUtRr_cCp2s_xm2bpKHI-_b8AZlQFmA1mVACAlUqnc76r0Vf0KJU_XjHaMdz6MgInwdusIe5GM8EKpzqwmIYC7tNiBlGJ37v35eZSqXgVHVG8TiNkvVVBMhhj8lKpY7Tm_oeNzH9ouhdy0eBGn1F2o_4bS0DF5OUmzKz4I-FQuJtkngy4N8h341TlRKhBfH0CcBLca3yKvSxBWabk9esRrTjBJ7bGiLC23JQSpsG2jc-OXhawBBWE4QDDdDqFBKAGSq4muGsISWlrcmJ3d4Clg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cH1fLvAYG8-f4cBUYkjb3yTvrUMW7X9g9tIIkCJCTFnnCf7v7Nzdi7l7LR0YF-E8RBC2fqxG9BR0EkdDztXS5ipaGHloVNWxGuTwKeBkWxZKeaosjb1yruZv3Jk3cxMklZPusLdkaCPicRoNn4SxBIBEit01edHbo5Sj47WGcarpcSjENZO-OCrF9jXnB6Y8CwStgwpkRs3zWy_PDURI75m8s5UBr5dyOO-8QaPT_5OZfscOWyNA8F85DL6C7AMKVqtoEcTA6DlNzb87wU63LcFeGTUY5ogyDFheji_nhZHS-Ck575CsNHCKupRAYVqYee1OTTNDwKorydD9pgK05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gHMKtSWDnTXnR55SK9_yFA0D11MuYuCiUKNJVA4cveyOIUcD7EQBJkk5tDRzQvF4PvWbYr9s1LtaHTWiYhaLd9CvDY0eWjvwmzhWThcpYWxJotWU28bN0D87QGhcWdOY5KEDBFs2EEUX2QmNXkFZ29Wd8lQkyrSLwTH_UUqP8Y2CbNrRdq8ZkTDSlV9jAidl2UrgQae062Z5rHlkSINVwIaKPoWK8eE9wcrzugARIZ-t3qsiDLtWb1iwra6w0FgvAd2jo7iVSeSr5QKkaDELanCwh4F_NmVKw930_PPvmJVTuZXVHrNX3Sdj5dnReiCt7dc4lEnmytY8T4Zpk0DVfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnmYryU-fW9N0Xu0wLqwyDDGPhyhPPSIAGp4jTRkeVeLBCcI0ExHCXt0r7iwjlXr9AhuvQTkYJYNdD-am9sAZ1RvHhaH49Y5j7GWkrwWgItWZ22-YPvoxN_oLIxSk8g8vQxoA1u_5xIu3RQ0Tt_50WnW6sC18Xta911_O5St-IIOCw1ERdKAlpKJsPZxz5m7fA7npIR72n4UQUJw222IXbq_lb2gqjoF3Y6wtx6O2aoefer1Ntr8yZgZ3AeraTP4HcJThyiTEZOq27Kf_L24n2Q9KLxy4NxNryZmwXJo5Zhf3S2bVRLJ4hskOafzZGDxP6koVyl83EB9Ji8k2Ylk1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=OqyGGdNE2t4lL_ncFNicz3pK3U38I9ltCfyBdg-6MGzlnC3LrLYQubvwb5Ki2PgClOH7pFJ03EQLrQWFdoK7kRci-FinCeRgYfRHCv0XARMOsOHiMys7sjV44DXyvMooIRB5eBLLi0M2dvEeL-xY0Q4Dji-L3I3fXPBVdxiK3gaOn9LBSO_PKa_s07Tz7vTUQaS9CwV1zftV_XQChJXPkPadpNaJmDDy_YoNxNz3iZ20f6lcuVE8fvfOC5w_mvn8kYHLvxJYkWbstD5RlMsJpayOKpj658erLrzx_evISkELGTcqeGNdUBa7x5YSGpDwBgMc4VLogS8jYlPqSR8-Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=OqyGGdNE2t4lL_ncFNicz3pK3U38I9ltCfyBdg-6MGzlnC3LrLYQubvwb5Ki2PgClOH7pFJ03EQLrQWFdoK7kRci-FinCeRgYfRHCv0XARMOsOHiMys7sjV44DXyvMooIRB5eBLLi0M2dvEeL-xY0Q4Dji-L3I3fXPBVdxiK3gaOn9LBSO_PKa_s07Tz7vTUQaS9CwV1zftV_XQChJXPkPadpNaJmDDy_YoNxNz3iZ20f6lcuVE8fvfOC5w_mvn8kYHLvxJYkWbstD5RlMsJpayOKpj658erLrzx_evISkELGTcqeGNdUBa7x5YSGpDwBgMc4VLogS8jYlPqSR8-Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8mCPKMyq6S8vNWd_J8s63y7Qm0EtTpPxjK9ymNuuApb4bRagpyhSC7oRTH4Wqr0qqVYe3TDfKi8VayF0JVzbe74Y78wE62fMRoHnBa9Gc3ezT66zeuh47afvzo4ikVnLJGX_ls1YOicuz8Zw6f8G_pSGIlCzpgi8_QA7fT2Puf6C41KHWeWKwXy_jU1S7ZJ_D1Jf3uGk0r7aM38-KxAdIcr1WxAt49P4yd7629ircfQN6EuTWTvpEqOl5ugQnTEuqYT-Gf6v32Kp49vxlXdgsMCXmAhwSfhMOsBzI2CYqu5x2WiqGSc9oi_jiW9_Ro2NVuKhyiN_DWKVK7TuyM3ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFBTT8S5RjkFZkNTahtqC5wBama3mMngxsYPmFOdRxU2Tfb-JAamt3o56q9dypP_ASvBd6_Z99LgQfOaQ7gTVgh2K1wR1mDq9jfiTAobIPJwGZFhPVDaTYCS8_Gl-piS18hkGHMjQgmAZeWzuNpSPmfH_roCteZrTxaKWj8tQUaWDRIvotKb0aPTc4wxov0zBpJHaKThrvinJm1xFfPH-7h6Yp6mNaY3pLiAqbqrvUZLML1Ss7h0xWWSa2RLlI460tGugMgmBjDVJow8zvhHvmceAqWmT-rmexMMei5ds_tdPAru9A57RdxSlvEadUIUBx8uQbsgbxqRb8GFO9Lvww1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFBTT8S5RjkFZkNTahtqC5wBama3mMngxsYPmFOdRxU2Tfb-JAamt3o56q9dypP_ASvBd6_Z99LgQfOaQ7gTVgh2K1wR1mDq9jfiTAobIPJwGZFhPVDaTYCS8_Gl-piS18hkGHMjQgmAZeWzuNpSPmfH_roCteZrTxaKWj8tQUaWDRIvotKb0aPTc4wxov0zBpJHaKThrvinJm1xFfPH-7h6Yp6mNaY3pLiAqbqrvUZLML1Ss7h0xWWSa2RLlI460tGugMgmBjDVJow8zvhHvmceAqWmT-rmexMMei5ds_tdPAru9A57RdxSlvEadUIUBx8uQbsgbxqRb8GFO9Lvww1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=bEEbxSCCfKogYjz1k44Ov8oEVvAaOi2qgLT8SN5S_oOHXBxhE_YzzkSnXk-NKvU-FuRidwKzj3tqfONQP-XyI6qIG-AlE7ChURUQH_uQa131CBctozz3ahwb3zRnifIe49DUPK3nLWq22YCzZRF4r5_pnLjYTjzeXRv87c9T11TWp2YV1hBfF8_B7HkH8nO1jP6nN9nhWxsNEGAr7-JVYZ_0NzivkYveJf5OXlVXb9ISGHayuK0V9OLj24wMb_sPs7lOK7cBCV0sBvrlvm899o0pQDpJnrr-n3xrF6oINzU9E8rESSrXhr1A21ZIvBlOgL6-kEPJ6AIEtuubxoTZPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=bEEbxSCCfKogYjz1k44Ov8oEVvAaOi2qgLT8SN5S_oOHXBxhE_YzzkSnXk-NKvU-FuRidwKzj3tqfONQP-XyI6qIG-AlE7ChURUQH_uQa131CBctozz3ahwb3zRnifIe49DUPK3nLWq22YCzZRF4r5_pnLjYTjzeXRv87c9T11TWp2YV1hBfF8_B7HkH8nO1jP6nN9nhWxsNEGAr7-JVYZ_0NzivkYveJf5OXlVXb9ISGHayuK0V9OLj24wMb_sPs7lOK7cBCV0sBvrlvm899o0pQDpJnrr-n3xrF6oINzU9E8rESSrXhr1A21ZIvBlOgL6-kEPJ6AIEtuubxoTZPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=BFAFbOy1eTLobr3NdKO3cByaA4uho2TDBI1N8aaN2fxN7TTBjhtc7VXuXK9XjE6Zzd01MtpgJt3ZpZ29Fn_h1uJcsCYLfEYxSBEg5AiiHVeT-KG_s1EVowvLbjEKJApCAMpFhIg0y-3PzTCv282XUUnEwJew7_oapc4PRyl1qNxbRRzt4rf_aCki6rdlD7BL3mALIWDt7-1k5IDhPR9uwWN2XwbZxXh1BuZk07zq97UzZ7aC9LAhRGJDWZrm6RdlvkiuqbLxYXI-2Q2eW9y4K7SoUJLb8w2uuh9Eg0O-FLyICQf-0OFQqwt3PQDL5zBzZ22XVSvHr7c6HWSo8tTTkz2I-rkbIXqWQRulA5xlyhJptk_Eim_7DDJoWX9u_O10QUrhRG3u9bIw4z0sYD5XVxhw8pBxF3HzR9CdhkkG_N0HGJRuYql-6dLZ0IvTR1SZP9WSVe5sNoiWO0ziKw6TVy1s6g3Oju4GYOwG0iUcmhQXsJlvOc5Fxzk4w0PSx8ZVHFGusf1Esl55xMwc_jAR9FS2hzhUi03uOUoW-lKasosdwWXwyYVwS4CB05AAkKL5ODdV5q_S_nXAv5Lgy1396feqxZFPpa4_gN1O8EH7aVm2BKEdZTu95-1nQBnELZBz2OmqWKgX-jewx5RT9Rt-XW9-sQrUNLGKqu24hp0gQq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=BFAFbOy1eTLobr3NdKO3cByaA4uho2TDBI1N8aaN2fxN7TTBjhtc7VXuXK9XjE6Zzd01MtpgJt3ZpZ29Fn_h1uJcsCYLfEYxSBEg5AiiHVeT-KG_s1EVowvLbjEKJApCAMpFhIg0y-3PzTCv282XUUnEwJew7_oapc4PRyl1qNxbRRzt4rf_aCki6rdlD7BL3mALIWDt7-1k5IDhPR9uwWN2XwbZxXh1BuZk07zq97UzZ7aC9LAhRGJDWZrm6RdlvkiuqbLxYXI-2Q2eW9y4K7SoUJLb8w2uuh9Eg0O-FLyICQf-0OFQqwt3PQDL5zBzZ22XVSvHr7c6HWSo8tTTkz2I-rkbIXqWQRulA5xlyhJptk_Eim_7DDJoWX9u_O10QUrhRG3u9bIw4z0sYD5XVxhw8pBxF3HzR9CdhkkG_N0HGJRuYql-6dLZ0IvTR1SZP9WSVe5sNoiWO0ziKw6TVy1s6g3Oju4GYOwG0iUcmhQXsJlvOc5Fxzk4w0PSx8ZVHFGusf1Esl55xMwc_jAR9FS2hzhUi03uOUoW-lKasosdwWXwyYVwS4CB05AAkKL5ODdV5q_S_nXAv5Lgy1396feqxZFPpa4_gN1O8EH7aVm2BKEdZTu95-1nQBnELZBz2OmqWKgX-jewx5RT9Rt-XW9-sQrUNLGKqu24hp0gQq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SbhDWwoL5BniPvz58BNN5D9qekqCYatWqjUIHIBarKovIAJHZP9YlEafDVuz-gwAsXxRmVnUgtjrhQON-Et_9d27rrX6zlfmUEvVOlz6wrqpM7AbCz8DkKD4OrxTN384SSebZtaLH6kYyevklVtB2E_5GVrWxhiMm3NLAWdK-gsRtL_N3201gNcoi_pgcYFVwwHbEH8bC9KlyzYS6UEgHhP0k4dVxIge0CKRS2kbi1TGORs0TsSAh5BIJ0dq06p5ZY9-gH942a8DzDILeFW0HuyEjnoj5zg7kwKu6rdTdpLOmG2pokdCTiar86sGP22oxnQPVu_rgOwv1TiAPjitKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SbhDWwoL5BniPvz58BNN5D9qekqCYatWqjUIHIBarKovIAJHZP9YlEafDVuz-gwAsXxRmVnUgtjrhQON-Et_9d27rrX6zlfmUEvVOlz6wrqpM7AbCz8DkKD4OrxTN384SSebZtaLH6kYyevklVtB2E_5GVrWxhiMm3NLAWdK-gsRtL_N3201gNcoi_pgcYFVwwHbEH8bC9KlyzYS6UEgHhP0k4dVxIge0CKRS2kbi1TGORs0TsSAh5BIJ0dq06p5ZY9-gH942a8DzDILeFW0HuyEjnoj5zg7kwKu6rdTdpLOmG2pokdCTiar86sGP22oxnQPVu_rgOwv1TiAPjitKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pavaL3IgmcXWHH-O8ExSguC02BqiCzpUvBeDswnXOOaLZBok6DSAHKvwjr50RE69GMkRN7o94O2dmZBxUNdLnmGMQXEQoJhAU8KpkLGqlcRKXKWpYFNBq7pfCkmZ-WW76TIWFuB--Olf4F-UDstBQ99X6wr0kgzljrRvdbtzQiaxdJ9U8EKMqRRgN1SEl4dG4spxplX_jn7e8hbs1Rhsp8sMLgP2VnUz7S9irwLV7_BTeUS_Ed6vL7-KORSv8T-AhPovLEotMZFrUveAvyp93XuqiDsfJ_lchGfuvwdz7_eK1szTmFnC5pIQGhj60dZwnFfLk7NH5wFY7h1-9HbBTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=aTrvtu11yDV1oZiXHLdNW8_ycDn6IwL51V48BF3Tslza87kzG306YvyqL9l9dOww-Tm5WgprOEwH30CGbLHLe5qQC5aX85EcpPog8P0-muu_UYJnjbcj8E32dL4TX-SwztTSQr-permt9royTPIybmyuMaYPwybMOb0rP8ajk0nR4CtbS7rZQMUbH4dVbzh6zZ0y7bMGI4tai6yzSBxwgASEbRkjbhtVSnS3rF7q3M_QYoV9z2GGD2U5BZ-y4DZgfC2kjxpqHF_OjiSSIwVbJyRQLQcimi4e-oqv1-QoWNU0Uw0q7tV3MI_DiThOU1UCyJso7UPtrnQZ5c6PuNENNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=aTrvtu11yDV1oZiXHLdNW8_ycDn6IwL51V48BF3Tslza87kzG306YvyqL9l9dOww-Tm5WgprOEwH30CGbLHLe5qQC5aX85EcpPog8P0-muu_UYJnjbcj8E32dL4TX-SwztTSQr-permt9royTPIybmyuMaYPwybMOb0rP8ajk0nR4CtbS7rZQMUbH4dVbzh6zZ0y7bMGI4tai6yzSBxwgASEbRkjbhtVSnS3rF7q3M_QYoV9z2GGD2U5BZ-y4DZgfC2kjxpqHF_OjiSSIwVbJyRQLQcimi4e-oqv1-QoWNU0Uw0q7tV3MI_DiThOU1UCyJso7UPtrnQZ5c6PuNENNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=p6Kti1qBpRc5-iQT9eGTrR3yTn7-HO-GEXxWM6E0MS1NlykhBsKXIqSqVjyzsO2xmUbr528dIEVlgqhzDmwPPQPsi6yxgauJTr_9TxKQUSbGbHudSgv19DKJ8SZ-OqMXqfnQETwzyGAKF7_h3UD0hC3IdBwuYR5KLDcTBKeGdAN_nViNAATEhLhP5VXAT-QKg6KphyL6zh9xJ4kvkVAFSIRANJfUuiokN2MsJmYTcmvkLgnqr2cWiev-lYpKjfhFggslENV6v0y8bE3Z78Iu7y5m5yGVxmYXhbUQe7xlQ6sAPAx9baugUrDGaNhLt--QNffdP6UEjN8zrR29oPHxQTp2aun4q-OprxUrYI4O7GqmtJ_0ArJ10-QOdynYhRXfVOVZN-YCCnT7nQtnK2zButLDhYi1DT6kx-FdhA2vMKcVfsE4HOqQ4RxD9TsctFUdByDyRpmVAKVTKc68UT4Xj2G5PIcqQf4w1d0izLJOf6SezRlt5eK6BqQ5fW-Vfd_QhcieqEkkjINaxrEaRdGFemyI7YZKDwhngvHtn8ycHyARfLH9TGJ9t-NT3109OQgP6rvJLrCm1QyZ_cu1NQ4THFlPz7eVof4ZwOGe9mmVanqSQweUj4gU5iEGOONwUlLhe-iRB5wI46xQBG-YvcHq8KM8xdafjnkh4u1P23unyds" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=p6Kti1qBpRc5-iQT9eGTrR3yTn7-HO-GEXxWM6E0MS1NlykhBsKXIqSqVjyzsO2xmUbr528dIEVlgqhzDmwPPQPsi6yxgauJTr_9TxKQUSbGbHudSgv19DKJ8SZ-OqMXqfnQETwzyGAKF7_h3UD0hC3IdBwuYR5KLDcTBKeGdAN_nViNAATEhLhP5VXAT-QKg6KphyL6zh9xJ4kvkVAFSIRANJfUuiokN2MsJmYTcmvkLgnqr2cWiev-lYpKjfhFggslENV6v0y8bE3Z78Iu7y5m5yGVxmYXhbUQe7xlQ6sAPAx9baugUrDGaNhLt--QNffdP6UEjN8zrR29oPHxQTp2aun4q-OprxUrYI4O7GqmtJ_0ArJ10-QOdynYhRXfVOVZN-YCCnT7nQtnK2zButLDhYi1DT6kx-FdhA2vMKcVfsE4HOqQ4RxD9TsctFUdByDyRpmVAKVTKc68UT4Xj2G5PIcqQf4w1d0izLJOf6SezRlt5eK6BqQ5fW-Vfd_QhcieqEkkjINaxrEaRdGFemyI7YZKDwhngvHtn8ycHyARfLH9TGJ9t-NT3109OQgP6rvJLrCm1QyZ_cu1NQ4THFlPz7eVof4ZwOGe9mmVanqSQweUj4gU5iEGOONwUlLhe-iRB5wI46xQBG-YvcHq8KM8xdafjnkh4u1P23unyds" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmakYsCtyU31CjVsLpe5oW0AyqbA_AlyJz8cfTWa3ahrWropd70R2FcES0bTFG8Gz3NMJ30qmaM4A3g8gEeqpDy86V2IEys606HMeZSSly2YkSvBnUGkmRYZEv4kuv4tYYNIOy8ROP7ngZBF2yZ3l7zurBwJUkZAdCDTYmorl8D89S7YkTv7k844Cyv506jf1lPkrkaUNVGtddL7FiZoPT3m033QNzSlVLI19GqTNZfBCUkShvVNYiAp6cJqZSsWN6YPKKDon74Apm2ofBmT0Jljgd6NtZpVutEkboF0dL5wZ3t7hrcNrmLbh9dD2nUrlg2YNVXg2OM11HvtiZ5saw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=YoSgtK8tz6it7_M5VWAFBiSkn1DN652dVHdNa1L7T4c4GfYcqcLsRYUQDDa2GfiQoNZA9OShrGHqQPa4RwBzyWxuUsIYOevNEntlrOKZ5_kvM4RYLTjWNh5t_F9_zpX2ys-fiO6Og_Awqbl5ZAH5a0NT72qEcigh0Zmz3wt3jPwoqCh8d9X5VP8H0HroAhY48RDFYUCNDT1A2h8dfn-ZtizePYTq2t_L_SzQZPw5-Q5OgYNLDc9zBB0DNL49l0yvlGhx7z7ntIVuztUtqXbX7aI3gQNRUurzcqlgXGr4TjyIMxLUwFSpmbraPphlkQXMy4Qz2FXydEe8Sn4DE09Yf1orBInWnTH6dSaBA3nv-oany-CB2nN2P-Fre70MZgD5wxo1-9baV3xvXb_oMiI5vMpQfmoHMKKqVBc7RIJIeXY0nRerTJa1D8KBOsGCvCETHlbxfLiCn5MTHaSKj36AlqhfiEz_7HrfRt9d-12a_D2zpqTUGkqolQurLg7V8VPmBmR3QmKK-5zJMh5HCmj67uuuHaMtTam5S7IrCVGPq_nUYgqx6JuLmYccAAR72LJHanHM_KVRbOPudSMh0JHUDXBG70TvVs5Wy6TUZk1GAFLCTKzFdtdwWqX2sWEBELkNpU8cb7QAxcMwolHFr-z-PfpCZQLM1qRzpQO0yPt1XgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=YoSgtK8tz6it7_M5VWAFBiSkn1DN652dVHdNa1L7T4c4GfYcqcLsRYUQDDa2GfiQoNZA9OShrGHqQPa4RwBzyWxuUsIYOevNEntlrOKZ5_kvM4RYLTjWNh5t_F9_zpX2ys-fiO6Og_Awqbl5ZAH5a0NT72qEcigh0Zmz3wt3jPwoqCh8d9X5VP8H0HroAhY48RDFYUCNDT1A2h8dfn-ZtizePYTq2t_L_SzQZPw5-Q5OgYNLDc9zBB0DNL49l0yvlGhx7z7ntIVuztUtqXbX7aI3gQNRUurzcqlgXGr4TjyIMxLUwFSpmbraPphlkQXMy4Qz2FXydEe8Sn4DE09Yf1orBInWnTH6dSaBA3nv-oany-CB2nN2P-Fre70MZgD5wxo1-9baV3xvXb_oMiI5vMpQfmoHMKKqVBc7RIJIeXY0nRerTJa1D8KBOsGCvCETHlbxfLiCn5MTHaSKj36AlqhfiEz_7HrfRt9d-12a_D2zpqTUGkqolQurLg7V8VPmBmR3QmKK-5zJMh5HCmj67uuuHaMtTam5S7IrCVGPq_nUYgqx6JuLmYccAAR72LJHanHM_KVRbOPudSMh0JHUDXBG70TvVs5Wy6TUZk1GAFLCTKzFdtdwWqX2sWEBELkNpU8cb7QAxcMwolHFr-z-PfpCZQLM1qRzpQO0yPt1XgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Sec0JWO1mc6ie8BAz5Wt74Df29U_wv4G6EX4x4hfKW08JQPhxp2RjxX0yRwVxGxgpDjyWN_HSJSGMatfI5AOY421KePcyX3eb4cBAw1DgmuTudfC4SV_FBpgo3UDl3n2dcECmVLAiX0pRkMgoMrz58mC4lZ69KWDFkMbY_qvDPabv6LfGM7xKG9PDJ1hVbY6kG_s89DDzydkRLuRkPq_gV-zhNcDIXe6kCl7IbhUYLQHTGCdf09Nel1Pup3gxngHH8h2cOrj5z1A2_5GfF41pBzgZ9Ew3xdgNOBXQ-3CdAhaVQXG5U4Llg6gXi6J8HIaAgBVEEmMeRQjSpSqpNHaSTKpcRgyCgQeg8MquTCwEju9WnvXNc24uXySj-nBLFybBj6e5zHTNu3snTt5i0HydPZtRyOg8fc9RyrDWh1YHFocVUoqwL_DzWu5SLoT2vglMbk4Hzf4UhuTgThAj74BvzSqGzAEdFhu_Pc-s7T4544E3bax3MJ4Sql-wI8J7Ytb7RTZM-rgoBDcN-dhsULhWWklKNILpYA0LzwIhtmj2YpvxHAJPsvJLXNdKTlt2RMg_6T6xFCl6H9OPzi83oJCCJlZNi2iraYew0QGdvpryxuucdlmRnFavjtvdd_-SMZ92MQ7865GEYy-XbBWT66fkYo1-IpWRva5EUiIoTOWukI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Sec0JWO1mc6ie8BAz5Wt74Df29U_wv4G6EX4x4hfKW08JQPhxp2RjxX0yRwVxGxgpDjyWN_HSJSGMatfI5AOY421KePcyX3eb4cBAw1DgmuTudfC4SV_FBpgo3UDl3n2dcECmVLAiX0pRkMgoMrz58mC4lZ69KWDFkMbY_qvDPabv6LfGM7xKG9PDJ1hVbY6kG_s89DDzydkRLuRkPq_gV-zhNcDIXe6kCl7IbhUYLQHTGCdf09Nel1Pup3gxngHH8h2cOrj5z1A2_5GfF41pBzgZ9Ew3xdgNOBXQ-3CdAhaVQXG5U4Llg6gXi6J8HIaAgBVEEmMeRQjSpSqpNHaSTKpcRgyCgQeg8MquTCwEju9WnvXNc24uXySj-nBLFybBj6e5zHTNu3snTt5i0HydPZtRyOg8fc9RyrDWh1YHFocVUoqwL_DzWu5SLoT2vglMbk4Hzf4UhuTgThAj74BvzSqGzAEdFhu_Pc-s7T4544E3bax3MJ4Sql-wI8J7Ytb7RTZM-rgoBDcN-dhsULhWWklKNILpYA0LzwIhtmj2YpvxHAJPsvJLXNdKTlt2RMg_6T6xFCl6H9OPzi83oJCCJlZNi2iraYew0QGdvpryxuucdlmRnFavjtvdd_-SMZ92MQ7865GEYy-XbBWT66fkYo1-IpWRva5EUiIoTOWukI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RM-9rWVlYzfUEk0mjt8QE_du44MbJf41cTYORCL0n6_1AEDmooLN9ORu0Tduw6X66KkZZvosnjCnUBNlcKjyDONcqWydmgKN8abf9fpIcKgTufv7vxT2QKpaCJgM4SMAWwuOPRmuwGl71coQiHBRDWFDY5Cz4a93Jb2BBKMp-Az9fQdhHjzNcDg3Ib_xKI_49K6CJ5rdOOyJC5Dx5ny7HN8r6IGqEnMGv41ndU2LTsbt0DuG2iERwoJUHrDUwhpotCDy-qnDM1UyFIhf40a5xur1jSP25kfKCMf2QyLt3ZACRetl0oBLx-6huxCaGrKnz7dcEbo5tGgMyb0-83UCfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=RM-9rWVlYzfUEk0mjt8QE_du44MbJf41cTYORCL0n6_1AEDmooLN9ORu0Tduw6X66KkZZvosnjCnUBNlcKjyDONcqWydmgKN8abf9fpIcKgTufv7vxT2QKpaCJgM4SMAWwuOPRmuwGl71coQiHBRDWFDY5Cz4a93Jb2BBKMp-Az9fQdhHjzNcDg3Ib_xKI_49K6CJ5rdOOyJC5Dx5ny7HN8r6IGqEnMGv41ndU2LTsbt0DuG2iERwoJUHrDUwhpotCDy-qnDM1UyFIhf40a5xur1jSP25kfKCMf2QyLt3ZACRetl0oBLx-6huxCaGrKnz7dcEbo5tGgMyb0-83UCfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=EBH2vFS0VvrP92PSsJ8DyvWsaOUtBM9tWZ95JXewyjvdKkzQyg4Q5Q-Zxhg_0bTWQqCArlpQo-HNYO8aTdCImSCBYAncgYg3mB1j8Tr1hXmD8potOCjKQ_cVaZwQ0dHwzYKSE-sFiX3_j10We8G-ZfF0kulK_UB7FFQ-w0p6ILi8RwQW1g_JaoiJU4WqKFt-ngBpoEe7lXA3Ynd0Qzi-tOIHrY2YuqADf9d9FqOtO3sCAGy7f0iluCTjuyRhjp95DAMfHBPVB09z6hQt4ahvo3_1VAiddcXzbl5bLWRxd8KPv_WR2pcw8BfvOUKr-Yhe9msWLSSffxzqrqIPidD2VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=EBH2vFS0VvrP92PSsJ8DyvWsaOUtBM9tWZ95JXewyjvdKkzQyg4Q5Q-Zxhg_0bTWQqCArlpQo-HNYO8aTdCImSCBYAncgYg3mB1j8Tr1hXmD8potOCjKQ_cVaZwQ0dHwzYKSE-sFiX3_j10We8G-ZfF0kulK_UB7FFQ-w0p6ILi8RwQW1g_JaoiJU4WqKFt-ngBpoEe7lXA3Ynd0Qzi-tOIHrY2YuqADf9d9FqOtO3sCAGy7f0iluCTjuyRhjp95DAMfHBPVB09z6hQt4ahvo3_1VAiddcXzbl5bLWRxd8KPv_WR2pcw8BfvOUKr-Yhe9msWLSSffxzqrqIPidD2VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=W13XbFDMZKYOUSHQhZZpUt3hhZf2Ei7T0K-CQHf_CdZX6o1PO9UU_L9gUXvbWggZ1qEiXAHTfdLtBCQtfJC3fwxJqGAmQLGAve7Ws6lxyXy0YLty6b2QqDyI5p9-cEWcIHPb31_nwuKXwzyrEfaei6MjgwOvawdyU1NNZuq72MbY1QMhvowL1FfAaNbpf9hbNz6ZD-FB0oFJucgvt5IOBNe4lRoT-_waVqwv4etkQqbIXPMmVNUqEJQORkU7GbjdH9dJS_arCfOfcWVnPkqe-R8S9XhLjy2WCntaWbeVV4zkiSREtrR-Hf7GbZ1Dc1-WKfTGXZLlVAlmjv3A8e-Ksw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=W13XbFDMZKYOUSHQhZZpUt3hhZf2Ei7T0K-CQHf_CdZX6o1PO9UU_L9gUXvbWggZ1qEiXAHTfdLtBCQtfJC3fwxJqGAmQLGAve7Ws6lxyXy0YLty6b2QqDyI5p9-cEWcIHPb31_nwuKXwzyrEfaei6MjgwOvawdyU1NNZuq72MbY1QMhvowL1FfAaNbpf9hbNz6ZD-FB0oFJucgvt5IOBNe4lRoT-_waVqwv4etkQqbIXPMmVNUqEJQORkU7GbjdH9dJS_arCfOfcWVnPkqe-R8S9XhLjy2WCntaWbeVV4zkiSREtrR-Hf7GbZ1Dc1-WKfTGXZLlVAlmjv3A8e-Ksw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=RdK61GoZtdMxFfzsTYZ5By-12zXeXEg44GKkMeODcYkXwMWBw0zRgGT0ojSUMsVq9w9puPVymqYRWghuRgwmEI2jsFWj07Fk_IRp8R4gJPMrwdB2zBcY88iJJSmgR_z0S1Mt9OPsBZpkobTwekIxHNddcKD-i1HR_6uMU13rIdJoISuS4ibrtxpvjrMKU4ymlE5J70_8AMS3J7IwF1M4Lp4Vvy6j0azbf-B40-mEYcWDL9hL9ENrWIXWD7GUKt4zFQPuJbdCKfsqOCYlSiJDmiWLSxm3AXOXOZON5bp-4Vx7FAgPqHlnhCouGsIaLMZ70jpZbzLV0hZOS5TpDPoDPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=RdK61GoZtdMxFfzsTYZ5By-12zXeXEg44GKkMeODcYkXwMWBw0zRgGT0ojSUMsVq9w9puPVymqYRWghuRgwmEI2jsFWj07Fk_IRp8R4gJPMrwdB2zBcY88iJJSmgR_z0S1Mt9OPsBZpkobTwekIxHNddcKD-i1HR_6uMU13rIdJoISuS4ibrtxpvjrMKU4ymlE5J70_8AMS3J7IwF1M4Lp4Vvy6j0azbf-B40-mEYcWDL9hL9ENrWIXWD7GUKt4zFQPuJbdCKfsqOCYlSiJDmiWLSxm3AXOXOZON5bp-4Vx7FAgPqHlnhCouGsIaLMZ70jpZbzLV0hZOS5TpDPoDPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tFeFHnWLak3fmbMAspnUAgJv6akhKvtzVjWEeYnhxZbQspglBK5yPlGyPxxsAQPDesQze8-uLyYFtIs7-5ifBnWoj1AtFxAakZpBojLtsVn5FcqOvVyQ-iUH3_W6xcCTtdMcCoLquiwDwnaRUjY4qyY7p9pK0EJFLjnczhdfGPqpNTq0aCzsYaU5xW5cFfuw58ehnAME37lrrzVWbsg3Fpzr1dokvf1sR1GB8wTwXLI_ddvFvTo8BeNrlFucFJw1OLl9ccv6_ItdG6l7Ii6Qr6ChgU5pzqjeYOV1Hk4hBWraqPOEgGEfewYYU5SCx1xgZQyGGTzT2mND97ppO_Reig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tFeFHnWLak3fmbMAspnUAgJv6akhKvtzVjWEeYnhxZbQspglBK5yPlGyPxxsAQPDesQze8-uLyYFtIs7-5ifBnWoj1AtFxAakZpBojLtsVn5FcqOvVyQ-iUH3_W6xcCTtdMcCoLquiwDwnaRUjY4qyY7p9pK0EJFLjnczhdfGPqpNTq0aCzsYaU5xW5cFfuw58ehnAME37lrrzVWbsg3Fpzr1dokvf1sR1GB8wTwXLI_ddvFvTo8BeNrlFucFJw1OLl9ccv6_ItdG6l7Ii6Qr6ChgU5pzqjeYOV1Hk4hBWraqPOEgGEfewYYU5SCx1xgZQyGGTzT2mND97ppO_Reig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=NJW7i7AI0YQ7kD2AN6HFcxtRGfpM6y6XJfbGz3VGVF5LNBjWFOi3utaRdvxznSFIbVug2icrJh50RUEmUDljnVt86Tg8Ljooazf_Ue70awYdtA5JCxsE5D8ONwIhQBFPh4FvD5BU6cdoTZM8-bPTWEY_kgh3wfMXWz30T7PlCjrIEDh6iTCVmKoBty0jr1-Iji5HJazrzbHYojIF-zgEBrF_z_bj5PlfURPw82BJVtSLNRslY4IRa7T7HUnBfbHDZXs4m6QPtPQ5JawGOCSE2dWWDDLekyHc7AtLPPJ0Ii4DOLhi8xVQtHLTVz9uQWMl15-ZEThiU8FzVyy1PFgqkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=NJW7i7AI0YQ7kD2AN6HFcxtRGfpM6y6XJfbGz3VGVF5LNBjWFOi3utaRdvxznSFIbVug2icrJh50RUEmUDljnVt86Tg8Ljooazf_Ue70awYdtA5JCxsE5D8ONwIhQBFPh4FvD5BU6cdoTZM8-bPTWEY_kgh3wfMXWz30T7PlCjrIEDh6iTCVmKoBty0jr1-Iji5HJazrzbHYojIF-zgEBrF_z_bj5PlfURPw82BJVtSLNRslY4IRa7T7HUnBfbHDZXs4m6QPtPQ5JawGOCSE2dWWDDLekyHc7AtLPPJ0Ii4DOLhi8xVQtHLTVz9uQWMl15-ZEThiU8FzVyy1PFgqkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=d7nyRD0cPDKnj0NxJS21Po_d4bVwsxMKbzI-1qVjP_Ose7re0VbmpDnVlcWzDBJBCq54oEphN62kbM9nO9f_QS8_HcKzWoth7KLegrDKuZwlrmzCQUefuNn1BSKh3aVuhE9SNR5XM8j2c0cKKQ2kN0NSghEAQrYFU51v0uQ2R08byPn6gJ4NdmXJb2BS083SECojidfNZ1GM7aKyUXf0SYMEjF5URYudaCRp5vsrAS85bAx4VL4auL230mL50UiaDnyXGQMAZ3S6Q0koYRzrAeI3FXvoWTSp1mMpaoiLN_2OCMp34NChAuA-isBJORd76iKxRIFfzmuHyjj0xor2RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=d7nyRD0cPDKnj0NxJS21Po_d4bVwsxMKbzI-1qVjP_Ose7re0VbmpDnVlcWzDBJBCq54oEphN62kbM9nO9f_QS8_HcKzWoth7KLegrDKuZwlrmzCQUefuNn1BSKh3aVuhE9SNR5XM8j2c0cKKQ2kN0NSghEAQrYFU51v0uQ2R08byPn6gJ4NdmXJb2BS083SECojidfNZ1GM7aKyUXf0SYMEjF5URYudaCRp5vsrAS85bAx4VL4auL230mL50UiaDnyXGQMAZ3S6Q0koYRzrAeI3FXvoWTSp1mMpaoiLN_2OCMp34NChAuA-isBJORd76iKxRIFfzmuHyjj0xor2RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4l8Pxvg9cKQnlbOjk93epdxGjo_eJohQPKKuYZUJ5PkCCtXl0qGnptXGOA_woABYbgwInWTGMhPoPQ8aOjnaRSsq5LS5wgXfL6m5Y0dEPFwhElDPO2-8RjbdjABoCEpbUHllu3ZAGybZQ_QZ-_H1VjUdntD4ERsae0VGkzhPUXCjHeFaEdy8xPOVJM7u-8EWYh_61nTXDN1Xuti_-Qr_CQdXbfRMbI-a0T8yVdwZp125cnHMbljUAL2WDuICaBiSA8hDuTAwuV1_soFiy-U5kll1_uuvW94FfTQJfZFmcfBopRujJsXYQ45YF8RERGMEVHz5MTkkx9fIZaSHPflVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qq7aZFtkWm6CpPa3FJscER3h02bZl5P3eihkIVBR91_tvOYeguWYnRdeiA4zwrBbc07PYJR2n3fQ70UnVOLay7N7jKG63qrt4TLrSV7ENxg7sASbYnzd9yPW_m0SNmC4Jajkeqb0at4EFR--IXBfD-ze9uCtN9fU3kfm4OuLBNIUvG2WufRlfI7Y6AAXULMnJCX_g7LbkQdtHGow2PuLHUHR26hy8-ecw4GSa0rYTTzaltggewrL4Dm7qPSWpT30yTjcgEpyO-ImcHWpAfSE3kuk2VEUFkefCoJ03Y17ND9e3OdO-izv88UXh5MofsigMycAVbYm-Ssmz7_6RcIPpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=qq7aZFtkWm6CpPa3FJscER3h02bZl5P3eihkIVBR91_tvOYeguWYnRdeiA4zwrBbc07PYJR2n3fQ70UnVOLay7N7jKG63qrt4TLrSV7ENxg7sASbYnzd9yPW_m0SNmC4Jajkeqb0at4EFR--IXBfD-ze9uCtN9fU3kfm4OuLBNIUvG2WufRlfI7Y6AAXULMnJCX_g7LbkQdtHGow2PuLHUHR26hy8-ecw4GSa0rYTTzaltggewrL4Dm7qPSWpT30yTjcgEpyO-ImcHWpAfSE3kuk2VEUFkefCoJ03Y17ND9e3OdO-izv88UXh5MofsigMycAVbYm-Ssmz7_6RcIPpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XXrEDg7VfUSwYIatM91Ix401v-AaT91Tk2z2wnjYrBcnopP_1kO0fm-DKEC6Zuin8JJe7RHGLk9j5qMpTZJqKrOdLICTvPwSPeOhQG7_NNHhpySl-FedHICBkbBwyXkxH8GxhwAbQQHZt2h4tJMpFbaJXvMZ7P_kb9j_Fqu09IToNSHsuQXpvunoTuw1oo8wDYFgp7bzmO4rRXzKmDyHw5J4WerjMsqk2p55uoicotExuLi_422e3bPn9a9WoeW0O_AniJEPMSGKHng94sCEitboHqPJZKFOISTfFzVYY2NLqsLxu1VjvGmYaYmyaGf8meiLLh-Gol7fyj7WuXEoVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=XXrEDg7VfUSwYIatM91Ix401v-AaT91Tk2z2wnjYrBcnopP_1kO0fm-DKEC6Zuin8JJe7RHGLk9j5qMpTZJqKrOdLICTvPwSPeOhQG7_NNHhpySl-FedHICBkbBwyXkxH8GxhwAbQQHZt2h4tJMpFbaJXvMZ7P_kb9j_Fqu09IToNSHsuQXpvunoTuw1oo8wDYFgp7bzmO4rRXzKmDyHw5J4WerjMsqk2p55uoicotExuLi_422e3bPn9a9WoeW0O_AniJEPMSGKHng94sCEitboHqPJZKFOISTfFzVYY2NLqsLxu1VjvGmYaYmyaGf8meiLLh-Gol7fyj7WuXEoVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=E0Ieb71hlXzxunEPIzUHMeoRUua_4rJ386FjGSkvHclak8XYmhLurTzC9Ny172hg9dJRSuN3nW7qDYAvmWdGJsiakxSBT-4ApQXEuOVoOucyqScWJm9f-KtF8nrga_VEt1W7drCv0b8nC85kvW0JbB9f8UVIj855ukvk-28c7Zn2dZzpIGgaykpeW4K1LDoNeg4l2WcmgHdCqmk2w7L0C_6aTR4XbEC3luErWBmIZ2252fvlEGm8pfHTyruwroAfkS8-ZEbFbpKgHinX3B8qS5eDTPWFDU-I7YytIYgAfNuF8U3JktSogvJcNzuQZLJ5Aibd_AsjWxnlT79Qqr6j4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=E0Ieb71hlXzxunEPIzUHMeoRUua_4rJ386FjGSkvHclak8XYmhLurTzC9Ny172hg9dJRSuN3nW7qDYAvmWdGJsiakxSBT-4ApQXEuOVoOucyqScWJm9f-KtF8nrga_VEt1W7drCv0b8nC85kvW0JbB9f8UVIj855ukvk-28c7Zn2dZzpIGgaykpeW4K1LDoNeg4l2WcmgHdCqmk2w7L0C_6aTR4XbEC3luErWBmIZ2252fvlEGm8pfHTyruwroAfkS8-ZEbFbpKgHinX3B8qS5eDTPWFDU-I7YytIYgAfNuF8U3JktSogvJcNzuQZLJ5Aibd_AsjWxnlT79Qqr6j4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=fArq7Hlee9UxvrROYXXXH7eXnZlMw0nM5QMmfL9B3g7FsPxEryMQKxkxkGToZ_4EhxJ6FYxnbfur45f4VJUcHX70OaXwStxxoXpz_DFna4fL_3NtmrfKhdQyKl0LM4cpOKCTwpbSUhh5DxkwgUpnKXgIysaSAVvAcRXgv90CSbVhANm_NUMPF6tSDYqZzwQ-pu8_T9R4dXUmH3yDqGNoJGvARvryguHcwov8s9AmOXfxspemiMWUcKn4BoB9-CvACpc8z5PwQw4nV9nhojQC-R2tWj_6ipL-tK9rOU6ukM2Qvi8_CHFiEFBHNB2pM65YzN4AdxYuxSbUDuyQlTTyvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=fArq7Hlee9UxvrROYXXXH7eXnZlMw0nM5QMmfL9B3g7FsPxEryMQKxkxkGToZ_4EhxJ6FYxnbfur45f4VJUcHX70OaXwStxxoXpz_DFna4fL_3NtmrfKhdQyKl0LM4cpOKCTwpbSUhh5DxkwgUpnKXgIysaSAVvAcRXgv90CSbVhANm_NUMPF6tSDYqZzwQ-pu8_T9R4dXUmH3yDqGNoJGvARvryguHcwov8s9AmOXfxspemiMWUcKn4BoB9-CvACpc8z5PwQw4nV9nhojQC-R2tWj_6ipL-tK9rOU6ukM2Qvi8_CHFiEFBHNB2pM65YzN4AdxYuxSbUDuyQlTTyvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iucyj_WF9CvZ4dt98idKTQm8zUQBf8nnOYGyCgqDP2brjMKjav9xiT2b7IPRZY7YTfA-x3LiPMTLd9aMAJFCFmJcHPqMTppp3iomE5DmYHLnnBxfr2x9zilG1QcoHfEJ8NUgz_bo5zTFcDnFp9spj_W5mVdlGpRiFXQ5FqhYG03lwl7UxYiAnXz44nBOtezvw15W4osHGfMugq-OFaRywtixoHzIUBSnsUGrnkUR6vZIgAf6ApJ0gldB94642XwhIUxbBdgh_6l0HApyVn_y6aMP_dC4bDYJMYyqlXx6Svv91VfkiMS4jMpiRqT-yBo_v7foI3z0lvKEOzX2JgZGzw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YNP4Z2PrZHQx9eDZTyJ3NuQVu3JTDUWKFFWuNvM58J1EdAzjm2-xu5I6G8GQjh4S0oDd7lWtrrm-JU7OjXoEv3TLGLoNl9HElWjISOOXv_qIg6CKdib99Snb7QoFuQW8yzHGTgGFLUjd--RKAKaXfk0QZXGomWw3owcTe2U0NP8Zl7COx1gsqdQYjZriIFNbElBN9hOp2s871YXL8VuVde6ho9x_eNn2f21HPhNmqJMp7ITy1Ctnusje01kB-z9Ue6rHNtyTjwN7agHuC2QYc5s3xDbxOHe3IJcqB4ez8t06SZp8GlSq5DPToZFAXU9Ce_WUc6ESQCY9T83bXj8jajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=YNP4Z2PrZHQx9eDZTyJ3NuQVu3JTDUWKFFWuNvM58J1EdAzjm2-xu5I6G8GQjh4S0oDd7lWtrrm-JU7OjXoEv3TLGLoNl9HElWjISOOXv_qIg6CKdib99Snb7QoFuQW8yzHGTgGFLUjd--RKAKaXfk0QZXGomWw3owcTe2U0NP8Zl7COx1gsqdQYjZriIFNbElBN9hOp2s871YXL8VuVde6ho9x_eNn2f21HPhNmqJMp7ITy1Ctnusje01kB-z9Ue6rHNtyTjwN7agHuC2QYc5s3xDbxOHe3IJcqB4ez8t06SZp8GlSq5DPToZFAXU9Ce_WUc6ESQCY9T83bXj8jajzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CMrU_vAjWVmzovcy3t1LTx6LaN_rS5366zxrdhi58GCDkp11ijZWQTLAO2UME567Nn6N4oHswAOokSNKZxJx49KuYdUGx1MHjJGIeBjOS1ZH4lcuGaXjLY4CZ8cAt9XM6hFJ4ARcKr24TLjhrpw1RT8uJuJ4V4VJExSZK2RnlZAr4oj6HmJX8_D05RFsVmOsVa-B9NcE9fHmfU47G39_wdtqrnH3bIKTh5wVr9D9KXQ-rhkeBLnMy8wk6xggOU8bjBomaI9I72NAMEIISoMSvbQR8BiN10mlsizJKLo25xoxWM-UcUn_EYBC8ywLSlcSCQudcDcemC48YZLSi2sZZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=CMrU_vAjWVmzovcy3t1LTx6LaN_rS5366zxrdhi58GCDkp11ijZWQTLAO2UME567Nn6N4oHswAOokSNKZxJx49KuYdUGx1MHjJGIeBjOS1ZH4lcuGaXjLY4CZ8cAt9XM6hFJ4ARcKr24TLjhrpw1RT8uJuJ4V4VJExSZK2RnlZAr4oj6HmJX8_D05RFsVmOsVa-B9NcE9fHmfU47G39_wdtqrnH3bIKTh5wVr9D9KXQ-rhkeBLnMy8wk6xggOU8bjBomaI9I72NAMEIISoMSvbQR8BiN10mlsizJKLo25xoxWM-UcUn_EYBC8ywLSlcSCQudcDcemC48YZLSi2sZZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cWOM_GUPXNayBOcqVW-rmQajpVqiXXEohp5pkFAovbFWXR9z5jy2CZkVpNoEd-IEcIIt5WFwaVZU_kfgEVvf5_86jPIk1vUZ1SYIrrBFyu6IoalpOmtG_aIAKwjnbplic3RFyCkoBw7tQGFrmguOS4EeDT03tzA5cSUCOM8mVZIMZ0I76yeBzvJQLCuXUQa_qasnwVZxGATeGkna08bQnNvIobdYSr_tYcYZ6lyaM_ntDKqmJLgqbED4G_irtq4wFSEJlWL9nEldvX3eMBJUAZQKljGW3Tq9Zqi5GoKwqPzgwpni0BLnKLd5vndAIdVIpRghZ_N9jMBq4N0xlW8fiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjXJbxKU4476l8lumXI7b0YTuZ1eszwNy1QI07f3BQnn9drN4RIUC7qLZCeK5jmZuDxqJQLsT_ZHJNx39Lf0r1fViBYmJ3y9fN989QYadt3iPb8dbSlrSG7Anms-7pHe-KvxkLZAZFeUPGFFrtIMofB5lkwFuk9L5Pfca6JGLU5mDIIihJtZKNdqsXqZzb74Zf-ILF0Bl7_JpqzgOkctKyH93bwxwRpdZeJQe4512c_jTAFw9GBeTsWFzfn5lBKCBw7wYutbp7C1OS827ll23y0lpcYcIQIHbWg_dltJRd7emNUzGUaP8gU0o0HFR9ZQ6V8ueWAa9ohtMh3B-jrJow.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=UhifFwDcFiOm0FKJKQOQ27iVVR_3KDTDPDyvX5jgEt7qGqxe1mgvY71u3ETkaqP-P526syvTczTlqXkq_0QEk8rK97bjqYENc5WW-XiScAf2vQEQw_zVjPy6aOe26KV9iqMuqvnFBPhXgVX9MXc25d5um4zcn8tjhSohdDPrrZ7TuUBajNHwNb_HLAaSfd9xiaxfLXpMIpHHksJZR0Kujth2Inq6rK6tTWeoJL3zKX1plXAI6g-Gzq_6KfQmg8VswbY84Dfbe8HBYEIOrzHydVCJD-Z-UYUwkTDs9bQ6zGQ8jFDhxjO4fScWAHVJtyE0HK9HpNfu7woWm9oGq-ACRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=UhifFwDcFiOm0FKJKQOQ27iVVR_3KDTDPDyvX5jgEt7qGqxe1mgvY71u3ETkaqP-P526syvTczTlqXkq_0QEk8rK97bjqYENc5WW-XiScAf2vQEQw_zVjPy6aOe26KV9iqMuqvnFBPhXgVX9MXc25d5um4zcn8tjhSohdDPrrZ7TuUBajNHwNb_HLAaSfd9xiaxfLXpMIpHHksJZR0Kujth2Inq6rK6tTWeoJL3zKX1plXAI6g-Gzq_6KfQmg8VswbY84Dfbe8HBYEIOrzHydVCJD-Z-UYUwkTDs9bQ6zGQ8jFDhxjO4fScWAHVJtyE0HK9HpNfu7woWm9oGq-ACRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
