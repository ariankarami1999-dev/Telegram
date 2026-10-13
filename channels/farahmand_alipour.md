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
<p>@farahmand_alipour • 👥 62.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 15:51:52</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frdnezwfe6dK24lx2DR6Frc9c6TQo_eAE7f4ykAb5v5ZT9NS5PO7xhkPsITr7dyNhIeKUF1ECEYZlLrlfsOQz9BpYdVY4ZlTkUxpX-EW-t5f4XdBhc8Nwml9or6lDJAie-JGRyPwLmpkt7-72oNx7lueCi3LSnpW4it-yuIBp984bw41xuUuXMzqC6U4zTNZQ9Kp9cBJLAjglkbTM-S4EU4RtaNUCk7SUSkjIYzabyYp1EeLUCUppfWPt5H9aIrsXo-6L2MqbF-F52qqOE5bl9fVavmvJJAn43LY9ET4Bt-mFw22ym_murXzcZYMnGpDHPVLvcjDG4qlsFcTUMgSCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hu-MKvbn0Bk9MT1uEOR6fKH4qdUYUbDmcyUW_zDp_AAtQxJAFphuV_7pfPtwIO7386KOnsPE0pT1ZZvHI0pld8Awee3epp_0chm6Q5LdC8n-aM1SivXfGbDznhKRtyBBMiEGOCj9YpBtGmyHgp8vSYGwa5fJvd3-ZcIxzkvDssGR9PQOi_dzHE7xRfMY4Ng0L7iUE4KxJ4flK4f3QEOFiMHk_Cgn_zKz3czVqjp0-XXiV-PkCcmYKAqzrtx8IDCSkESVvRrXlaCehHF38OYo-Z0Jb4xAxkhu_-WniVLen7aIgE2hEjBAbUUD-1GmNuFPQCQ6daZreYPdMeUzCAAmZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d9F2WRRa7cRZiI-AG6cxfVDZNOmIZtlKB4GPl_lsfRWb9wBjsvFP5g9CvKo3Bz-Z7n_GGFvR395pH2U16wmk4T-GYu7dBO4hNznnXxMjvkKfO5KqFf0XFKdHcZ-vxT7gFR4uhBjYyL9-8Dct0wOAYqike7qwhj8U7mxIv8YcMovXLWhqRRHdh_h9gJ9rTghZAXeH6B9l1qS_XDn4R14CtFohuk_vS6X74nOAY-Y_ZpLaDIevMUL-ndn7mQo_FiTzImqQAUCDcsO4v4_VQ_RxMLYhvlLRBOojLgUhsFhRcdXnURPFSJIxqA9E58YP0dYN54_nZ7TnZ4QEY4Z1QHk9HA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=b32B94sJO43yV6WO3exnklBECa2PBZ9TAfjzxeV0V5C7jU8sgzsiu8hWUZwsOOoF8XU1DWf3zjRliBvtO0v1tpW52w2jAHt1Ss0BYej5tc0kTnajIafXkDO_nkMo5dhDLo3vBBLULVwuhSDFvG7ebGsS2z5sVHzXrnZKM3w2slYiRkz4oUJJANrL-kGMRVM6fWZQq1-iGrS7PGJtv1XSWV1sH2bvL54lCefn-1qMBPOmaX-rPNQIKIW9jQSV15fU350nBwn1X6DG5FHujyV_yw5j6XBuwE1LMP3IFhVd3khD-RBoVk_v_DbppyfdUaZqp9lahivXa3qnZ4odB272QIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=b32B94sJO43yV6WO3exnklBECa2PBZ9TAfjzxeV0V5C7jU8sgzsiu8hWUZwsOOoF8XU1DWf3zjRliBvtO0v1tpW52w2jAHt1Ss0BYej5tc0kTnajIafXkDO_nkMo5dhDLo3vBBLULVwuhSDFvG7ebGsS2z5sVHzXrnZKM3w2slYiRkz4oUJJANrL-kGMRVM6fWZQq1-iGrS7PGJtv1XSWV1sH2bvL54lCefn-1qMBPOmaX-rPNQIKIW9jQSV15fU350nBwn1X6DG5FHujyV_yw5j6XBuwE1LMP3IFhVd3khD-RBoVk_v_DbppyfdUaZqp9lahivXa3qnZ4odB272QIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=Si4_GF1m3IS05eQNtkQfgKRtNdwKRfK1qrl4o87L2NnCOaEJI4RLxviw8BwXT4zeZvu-CO-uVKROaJ5EEJIrkR_WxgE8vSy_5rZX1QP2Z0nU9TUAg6aw9Osy4_x8kTDqbEB06rUICTwYbx8bK1JSg-sBROZ8FnYOdU7eB3YfGYNQ_W6mSIefsOCZ4pBYZX_ZnRoWZBIAJWBx-XTM3-fiLSHJArvSBW-6ZuQOYWt-Nx-Cw2EP-C4QZTcRoPBj9FKRwMdOggqjju_ZidPpOg_4poSEmpexPNJqVyR6s4lKDAdg7SeDM6ottOU8ohWAR54dMyXThBZ3wFxqfQOGiswANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=Si4_GF1m3IS05eQNtkQfgKRtNdwKRfK1qrl4o87L2NnCOaEJI4RLxviw8BwXT4zeZvu-CO-uVKROaJ5EEJIrkR_WxgE8vSy_5rZX1QP2Z0nU9TUAg6aw9Osy4_x8kTDqbEB06rUICTwYbx8bK1JSg-sBROZ8FnYOdU7eB3YfGYNQ_W6mSIefsOCZ4pBYZX_ZnRoWZBIAJWBx-XTM3-fiLSHJArvSBW-6ZuQOYWt-Nx-Cw2EP-C4QZTcRoPBj9FKRwMdOggqjju_ZidPpOg_4poSEmpexPNJqVyR6s4lKDAdg7SeDM6ottOU8ohWAR54dMyXThBZ3wFxqfQOGiswANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjttljYjeM-1CKkWnTeHaeEFfJ7Q26e7x1pUHTHhC-zMb6OfAH2kLkahxpFMj4_KVE37c8lZU9qwbSqVDRJEVXvmsoiSDdohVMCvkRvIKwvjY0iz5SbdCKPWCHM68vQcRHQJnwlNDFpMZJf0l17MvsZKSBft8-dsF2W6-3Bwyi5u7dJcE4NQAbYtBVZIMU_TO90dDZmYuF0BA8Jd4XohFBCT6Umg-el0QzR7A5gD_Wm3fgThtJJwsBwX_Ny_5ai4vWNRyBQiDnytCFXnFcFYgOsKtcE9T0EY4LFH1xcWkG2MwOoPb5gpfb8tE2aCncUHZW7WzXDScgsm-Fupqyduhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ppdOglHO9Qgfne86nKp6ez1zwmdmS8bD1Rao3V44zEem5zyT_HVR333R3cexkw1yWmkbxYc0E5tNq0YGcFuFE_rk-StduaVF2dxNmpYYxVJUzK0p28svBcFv1Tg-DLPv4neitBfU1nSRniESPetj8yMm-lSDMmwU4hAi8_m3VFfqEZHpo0L5s6CtnTKeSGgmxg1lzfqYxRxU8Kij8LRFAPolP9wCJA91sSgTTTLzgd6wFacy-mIlOieG6owF_281NEiS0QTam8CpQpe0qfoJmSBJZbI_3mC4_12TmNsF2RzM7K2il472u0oDnmlj5k9Dd0HIIk8wclgwzUZqM8_1-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=c-cRUKYP41XqEtDgw5nnz-wNursPNMobJIAbBoR42SkuBG3v9Hp_E2KHh34Y9LQNLZJZ6gPKOTMjH6LirTu24u5h9VWiuGV6hWL5b8FeZ5ggaGPSxSmBrKqGptjj-Hon6pBp3q05O6uf-X4xAMWHsmbcL2grw97_-rG0mgBLCitTuNjaoHP_mPV_GP2_U1HEOU_lix8_M0sdSlg-7y4oky3OKrB3FmwSD7in96ZCIuN8FehaZa46fMR-S96DHHzIB-kggKFwpk_bEYFEWWwKFHv4LZDhtzELO3_ZYINw5PRbQYElgGfw1yzM6qHRDoAWqe_woG9prDe_k4iVXV30xqBTi-FC_UZ5A40B51mX_rDlEPeF6f-24SCXPMZmtrh-xEDOoGkBZmca6iBAvwFRLmufg2jDyGr7syMu7AjUUjvAW3sXQhCCmkSeSjjhg6Gw2airLAGR2G37hsBc4_SQtf7ZAM7ocX06pU7qbxbc7lRpXaLtK4Ak-9lZ4Np-yvksmfH4ABiInQDJ1FClIVadl6gb_h1Cvlux8esvs1HMFfET51Fitoy05E5fVht4BGlFJ1Q5fxLwgWYdRmrDNPtiy2N16SxCTqwj2_X0ZtM697lkQjdkK-KkrsJWyah4QjYVZwR9giO4Ir_n66ZIj4VHf2lPZKqQtvz6tcGwTrCh170" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=c-cRUKYP41XqEtDgw5nnz-wNursPNMobJIAbBoR42SkuBG3v9Hp_E2KHh34Y9LQNLZJZ6gPKOTMjH6LirTu24u5h9VWiuGV6hWL5b8FeZ5ggaGPSxSmBrKqGptjj-Hon6pBp3q05O6uf-X4xAMWHsmbcL2grw97_-rG0mgBLCitTuNjaoHP_mPV_GP2_U1HEOU_lix8_M0sdSlg-7y4oky3OKrB3FmwSD7in96ZCIuN8FehaZa46fMR-S96DHHzIB-kggKFwpk_bEYFEWWwKFHv4LZDhtzELO3_ZYINw5PRbQYElgGfw1yzM6qHRDoAWqe_woG9prDe_k4iVXV30xqBTi-FC_UZ5A40B51mX_rDlEPeF6f-24SCXPMZmtrh-xEDOoGkBZmca6iBAvwFRLmufg2jDyGr7syMu7AjUUjvAW3sXQhCCmkSeSjjhg6Gw2airLAGR2G37hsBc4_SQtf7ZAM7ocX06pU7qbxbc7lRpXaLtK4Ak-9lZ4Np-yvksmfH4ABiInQDJ1FClIVadl6gb_h1Cvlux8esvs1HMFfET51Fitoy05E5fVht4BGlFJ1Q5fxLwgWYdRmrDNPtiy2N16SxCTqwj2_X0ZtM697lkQjdkK-KkrsJWyah4QjYVZwR9giO4Ir_n66ZIj4VHf2lPZKqQtvz6tcGwTrCh170" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYzjxjsIQYy8NX58WCqayj_HoOPsdR4vRQQCNJfPqwcD57gFe_Q_ZfqDRGA0Z-kAI0Oge4r1uWgIJYqzDGXOsi2DOG9L95RGgwMuv3fTJxAWAv-n_qlHUY-1eVQW9UX--95PB_6T406NSV1LUbGxHu8lbqkr-1cafU9lsFIM5wJFQNYrc6_YqPBe4LM4YEpkoIwKN6rMXVBqPHs2l9aa-VYYj6fs6kOahmdD50KssWMkwXuR7i4mFVnL-Q98SorFnWKDuNklxbEW7d0fKrG4V82ZotvKYmVJGqq4jG8qGTyNwDJm3-x6hC55yjQ-35QSjYtqPMMpbkMo86gCjy_FlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t_ETiImk4CKqikKYasDQfFo72MVsvc27QoveeDJkFMtaktDd9Qdy5puifmtZlkdnPFRYnnv7OJ_SNhVxof0rk2xD7Qdr6UVuDxUKB75IGF1224kXnroTpJsFBBICDJ61ZjvaDmVhncIBRsQtpqNHpKQ6tR64K6BBiesWIOcRkla9D64qnqDl29QsGTVwRX9UivWr-NvrjJacUP1sxQJXqK7_7EgGxPuqZZ0Jpf7Dqgs7vHhaVHJkqDpdOQgdzWH6BeXihUfsN11XM0DVl9jo1yhhvNFkLHSTdcckedDPTtj8NWnJoxWiN2C_f6EBrLaOGgWwxYy6bGQM6ni7LNl-Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nrVoXjft--QEA0a68oQ_Om4xROsthNQT_OcVO47yMwhN9T5jp7QDSHwv31SUXrX-STHBEfjOPah__5m3oLHqwnKYcruOWQX-u1ukiZfPiiIQKRle14QScXkIs08uU5ju4NHmpcxrsgRIBEwvZmkv0AGakj2pUJvw3Lp0W7X_Wkwmx2-Fh1aLJ_h-I8ukS71iLbu0CwwLfgn9d3f9TKT6FmEP17F-n4g4nPU_b97pLZPNlo8nlsVPl1sYAFDSVJRy_vyxnotwP6z_eMdB9FIndV2MUSzV8cyRXJmbssTUgyA_ENJjVvgEU5lvrEPVJAwP2rwGiIHVXdsw6Fqt58xJ8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2FkJSgbxsojPYixJ6aKJ5NtVSyZ6uQjInCQYTfqb_1l9OW9Htz4WzEoUqaf9CtSBCKMQO9DmzIlVdhKeHBpPxMcnulVrtWU8KahCvqzpbJma66cI873RggiwEZaRGcuqkwy9sJGPb5xzA5xMt75qj7q2Zirraa2-IROcdod4cc6cIHnOhOccuY0PtT0Jpm_0ndKMZHmu0hIWhq0ziD8pWRyGVx4VCBKoiny8M-ftcc0z7cAbGiN8Y73raKy52GvS6YraUe6kTsfqcIaFCum4RCfBPVxHxipC91fhJuJv1Rawrqn_h5oL8s2oRD_rfqvgZyA_JjhzvX0vdC3ifbz8Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bK-Eam4Fd3b-aL0UdX_tWWGcaawBdwoxZ8xod12ii0R2ZMVHP8q3vjhkWseYElASkgkslP6XV91hwIrKN6J617y_DzW66ZXHmXP3YBifQ_5YXXanE7ZYwLoh6XDkpoW1f-TetOfqccjoku7uAUrWgOHp0R7tkFktcLHRRkQIrCsjd8R1UyTaPkPbw1lhCKt8SeifiYE9c-D7hN2Z3YRxYv60hx0CI3GO8rQRhauz-rntdRNpMGrxsNUmaYlTdRgQS2KU4Ayqi_PorEbAR1AS1qlaC1gP-MzLwtma6CYL5u4u5NRaRWUMhaRza4-p1njgEBsWg_C-bXEciccmg-AsXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LK98MC-x5nusnq0xnm3jTbpxXZKemSbQBrPqumkzDv3j7bPW73v3-2sMwWLfS6H2Cm-tylleV_dgcWAE4bLZmrKWkJsL05QIsY5m8u2YmM4tgWHCoy0nYG7YYqbJeCX92ugTsAc5zI0Whz6iJzBXjX91QGmn-B8Gme2sp6gdMoyoWmZ338i90TJGh6N04Qke5Jyg-UTpg0QFayc0uZrKDk251X6mkzBsoZUhbdMVjx_oGNVFu3GjOTfMDA4-892MBoSOSJJ7qIlqmZdiFyNdeSaldSW4_xrtMGwJIgL1VjBtGcibXRlhrt8fhREK_6O4uFP5wDO2wefQDCkSm2CMdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=RVsuO3A2JMQgUa2tA47ZAapU6m97T8qyrn9Fw1249upec5-G_hPei_y2ArLzJGFOdPXvl_XWRD8bK68J-a5rXIgEl_y5s5gp1_2D3g3e5qoKUP4sh7LDNWJp7IuOctHmHHNK6BaEC5DARsElWWpuBUzMOqYHQkwCwC01sC4uGXu3KglhLUVV9QqIzBBLt4izNRTTJ7uVa5QlZLDYGSaQ3ykKUOiYVKvZkDvvpoL9sP0toRZa5GzjbreVliIb6oByijR3x5sqUxQwz8azrYyL1okde15sK1zACp7288MovEqDHEWdTNIdPsKPFcXv5_Cq_tNZyM-60AZYMFzk0_rXdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=RVsuO3A2JMQgUa2tA47ZAapU6m97T8qyrn9Fw1249upec5-G_hPei_y2ArLzJGFOdPXvl_XWRD8bK68J-a5rXIgEl_y5s5gp1_2D3g3e5qoKUP4sh7LDNWJp7IuOctHmHHNK6BaEC5DARsElWWpuBUzMOqYHQkwCwC01sC4uGXu3KglhLUVV9QqIzBBLt4izNRTTJ7uVa5QlZLDYGSaQ3ykKUOiYVKvZkDvvpoL9sP0toRZa5GzjbreVliIb6oByijR3x5sqUxQwz8azrYyL1okde15sK1zACp7288MovEqDHEWdTNIdPsKPFcXv5_Cq_tNZyM-60AZYMFzk0_rXdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Fvvl4ze3IAd-2ZEH_bnqSMCmMY-OhW0uDNbP0rOmURUGu6WRoKoVmBSg4Z3iGno9nVgkIlUR2V2VAs-rhSoAmyqq3A9mycwMIeboRqUvp-DehrR0XCHkW-k9TL2gFu14kxWc36ZVx5OFvQqxWdyOuuyUpFVMFdadg2UeONJkWIN4CbNL1Ybt8o00Ta9ZjydEwNrCSXvwMDQmbmL5MZ8_c3suIXUWMVNxHcxjbojjwxvTWK-cCeGw8Fl4ChNXtw7BTN-RP8zwa5IhGYH-0hA9EF_Zj3IVmFW-oIQI4SJ5AVox720XM8U9Q8Kh3E-pZWJmu9TE0Jh6NbT0sbYKcnI4mK1Xx5VIkQYeF2nx-vawi0A-BQ9NaT046BhVGo4oelcozXr49591MP2REQedqNvkrqd9t0ilTN-Ndo-gymfBOYdpZ0_HRhazeGHeqaxanvgq0UM3CfVgInq0AputrHEFTpne-jhO8BZjCQhr9fysq5WwvcdGqWlsOVChJJrGbUunKeHHqk8m6eWVdE1LvIr97V1vUYxYnL6vdnjBtoSICCnJv1o4N45xq0rAokzF7G4g8Wl9p7imxlsnsDPsZMZB1JnPsy2g2RO1Pb7RcwFSfB9otrGwdjCBMZTtEpXcrQQIlq0t1fl8L4cewVdj4iiwHFRkxxOcsTHnGbJTJn86rqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Fvvl4ze3IAd-2ZEH_bnqSMCmMY-OhW0uDNbP0rOmURUGu6WRoKoVmBSg4Z3iGno9nVgkIlUR2V2VAs-rhSoAmyqq3A9mycwMIeboRqUvp-DehrR0XCHkW-k9TL2gFu14kxWc36ZVx5OFvQqxWdyOuuyUpFVMFdadg2UeONJkWIN4CbNL1Ybt8o00Ta9ZjydEwNrCSXvwMDQmbmL5MZ8_c3suIXUWMVNxHcxjbojjwxvTWK-cCeGw8Fl4ChNXtw7BTN-RP8zwa5IhGYH-0hA9EF_Zj3IVmFW-oIQI4SJ5AVox720XM8U9Q8Kh3E-pZWJmu9TE0Jh6NbT0sbYKcnI4mK1Xx5VIkQYeF2nx-vawi0A-BQ9NaT046BhVGo4oelcozXr49591MP2REQedqNvkrqd9t0ilTN-Ndo-gymfBOYdpZ0_HRhazeGHeqaxanvgq0UM3CfVgInq0AputrHEFTpne-jhO8BZjCQhr9fysq5WwvcdGqWlsOVChJJrGbUunKeHHqk8m6eWVdE1LvIr97V1vUYxYnL6vdnjBtoSICCnJv1o4N45xq0rAokzF7G4g8Wl9p7imxlsnsDPsZMZB1JnPsy2g2RO1Pb7RcwFSfB9otrGwdjCBMZTtEpXcrQQIlq0t1fl8L4cewVdj4iiwHFRkxxOcsTHnGbJTJn86rqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4b3muj1fHExw5ix1EZUViPqKnd5FKwa2o3X5lZIbuY_TdoXAUWF4DPc-BjBuO83ZKiZjgSS_rqIANwWuV2vvOr8wNgmEtohx69BLQUS_C4tNT03Lye5QqvoIIVxyZJiUru6LQtJ_bEIVbduDBoYjZijVuqEFjiMBw715ZBirVCinM7Gt-dn01k2sHFkZACaZHh65xmXk6N1yGpv2GLFBFWFovpRvw6luPLa6zqweIzIbbtUuPsMoA_jc_CpSNSrXJ84n3N71tQXzRmhyBagn88yhBV0WiwD9cAMQt4dglW5ux036SSBvQfyV-VVt2GCYRw4tO9gjY4y1giv51LWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u56YUmDR_9C-WS7S5zWqt4rOjc88OlcL7hBNXd4RnPP4oIEKN8nfNDy8PmdYf8fVdBDPXWlpYFD_yZneCaLsiE7fuHVbWux9JZDS9RNuuUSF072PoxIDMOg8s-lfOSv_NsQJ-AE83bEqY1JDz42M8ZBhLigkH2AQpaeVPiT98C3e5mYvS5KQgyZ1SqOgzsgcPtdCmK8nadlZN0XXBQ9TSX6xTYq9L5iSOB1nXkIJbYCZWsrb4w5lJmf7eiTzl5pmh8w01uNZkXinXz83H57vCX6s2qBOAA2RTOoFP0dSWNE1d_ecToqZIPulsM1N74CtW5b_aim0oxuuUq7yjNjRnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6ztBWROauj0ZlIHkIiXgIWf-KlIZUGig4ot8Jm5vmkAtAV8PnxLbIcQIMdqi9UlduCW46gTnYujgJaF3VDQ1vXJcnQ9yiQVhImtQFJhqxqxgfXewyRBMYT_7BRJciffGH-TvfTy2fsdbeet6vtEC1cWJFIa26tamxWFkDdDUXiKJp68Naap7x16RmopQwC5tP6L6LxfBKvSV9aBERU93sS8Y6szHdy2bfqSQcuhG9QZf6reTpuxrx8HwOTwdWDx1htH3F_H_nPdgJbmNaM43wt4qh1pNyrLwkGVA3jvQTBCbmBDPWq5km-8QrykY6utjmHBwnRtBoxrq1-NV7ozpQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=WSlvNyxlO6jhwvD5_JNJY8upSnlwEuRN0eMUyqJRebVAJ41yqd2b85T16skQUJuKqNFAWAdu_iyfYlWshSXivLYI-3215_Esj_Mw6brgARfsQvOsksMuqvS4uR7_1Mx_ii9OsuMJcgE6yvWftQjzHxhz1EL1gbWtaPxLVT-P6GoCpyIgvJ5BMYJgkpxBBwNXw-dNZ1vlbXUUjkyWnjV9H8PZdphO-p1jr68HyOCYg5lIe5mJs1k7xUft-ONAjFVRwOccW_XAyQb39VesoY-m-xUjIPOFJFuxUtbhnyrAaM5Ur7ZvfcxEgiYysX_dKsHRZbVxp_RKDiJbqM7zf3MiPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=WSlvNyxlO6jhwvD5_JNJY8upSnlwEuRN0eMUyqJRebVAJ41yqd2b85T16skQUJuKqNFAWAdu_iyfYlWshSXivLYI-3215_Esj_Mw6brgARfsQvOsksMuqvS4uR7_1Mx_ii9OsuMJcgE6yvWftQjzHxhz1EL1gbWtaPxLVT-P6GoCpyIgvJ5BMYJgkpxBBwNXw-dNZ1vlbXUUjkyWnjV9H8PZdphO-p1jr68HyOCYg5lIe5mJs1k7xUft-ONAjFVRwOccW_XAyQb39VesoY-m-xUjIPOFJFuxUtbhnyrAaM5Ur7ZvfcxEgiYysX_dKsHRZbVxp_RKDiJbqM7zf3MiPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Qvlwg3RXZLbqz-TfPxKQmnPeQAYFszySytN2A7D60BZ-wsHcCpw0PkEuuF6L7C871nefkLfVSZaL4M2XVNyngMo11DTdY1IR3E2rKNSu9stzhcXRo0uEqxU_5QRQ9DcVBSEqNdzIP5VqMSAuuLbZy9e8J5AuSVIBj1RfGzzfV-WIXpnMOCz60-BWvyTzPwM0gwkKa_nTYIiaWTcBNuAxqOjX9DyGVny0btKyZwqL9sYsCDYVF_NwY52q_05kNG5dDtPuEEVQpTMd8RyBoO3qA2auPUWkvIzNPx2x6aJWJFROu6lCM9EMKxhbOWWEERrVtZ1BPMZUd1r5Jk2PLSUxRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=Qvlwg3RXZLbqz-TfPxKQmnPeQAYFszySytN2A7D60BZ-wsHcCpw0PkEuuF6L7C871nefkLfVSZaL4M2XVNyngMo11DTdY1IR3E2rKNSu9stzhcXRo0uEqxU_5QRQ9DcVBSEqNdzIP5VqMSAuuLbZy9e8J5AuSVIBj1RfGzzfV-WIXpnMOCz60-BWvyTzPwM0gwkKa_nTYIiaWTcBNuAxqOjX9DyGVny0btKyZwqL9sYsCDYVF_NwY52q_05kNG5dDtPuEEVQpTMd8RyBoO3qA2auPUWkvIzNPx2x6aJWJFROu6lCM9EMKxhbOWWEERrVtZ1BPMZUd1r5Jk2PLSUxRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pu1H9EHEzPQOAOqVjsjZm0XolOteN_ExCWa_Sffb_JF0yYXJ9NbHVjsallkKeSa_2rbN501iWVQkdafRF49wlNTPwOnAUmGqQZXE-i7g3jv7sgK8JA-i30vbDXknW2oxXtcBGM8cqzeX2iw50PwLsHJUSD_Yl3s92lpOUPqZHTce-tcsTXYIQNI4Kr_UVs8uScsnlYw6Vlp_tp41vVUqDgcFj9yD7J5_f2OvSl1p5zEOxL2vfTK8FwmmhGGcOlEZTKg2SRC4tP7qZVVJ8fcJAnV4_GT1FBvEDR7T_hPTzxXwsqEriuKO0L84mTaCdZ506qONeMkVz2kpEOXP7A-EhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=YQ_CW6CNRkUmUroIK8iv6K12Baak0acrEpreS2WPuyYeUvxJahXJmMN-k_koKju4I83xape2OzZu7QzwYvmkJT04hV0vBHYCbP3wiVIBNrV0xsnMrMpXqCPhj3jdRpp8HZz2j5dycXEGPmy2ye4O67l9wDB4gEKFZExZ6N4K03V5dntLRJ7yWuMbdlmViWG0VVEXxFg8SgoZvM-fDSQHMC1yxxpUcPM8asBEu3qwAcTDRC7CRrl9hb5_zFCReyMdJbvgVw4yNEobInayemJO2_Pn68Ju5fHtRV5OJ0gccumB8XZck1jp9Em7ruIvmaZ4OotQE3zCgtaZuVRg2wOg3FmZ2w6QIigcTdJ2DXKeym5-tsawnb4wTuUeu2VQXYEA_K0e3neI__eHLxkZq4qPB-c8AyiKkwEsrqZG1OWYl1EgpkPsy-RH3ASLWtK9b1guDsxDa3MprcJNOymt_l9swMfUvpWVjjr1yc4upqv2uHZYz-EbBv0Iz1v2LaPQBjYD5S98Ghh5OOga_omC7yhSOv4uVWrJ2kJFDyG-JP9IOT0OXrDVKn7qFkEISz0tpQN46tleDjns3A1i0Xt5g5rZznM2_MFH2FmkEwIu1e2_S0wYettiqZN8GrQAnF8RFEHngsqxvqv9KkcPqff_f_nxRu_pMc7hS3kWkvb3g9TNLcM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=YQ_CW6CNRkUmUroIK8iv6K12Baak0acrEpreS2WPuyYeUvxJahXJmMN-k_koKju4I83xape2OzZu7QzwYvmkJT04hV0vBHYCbP3wiVIBNrV0xsnMrMpXqCPhj3jdRpp8HZz2j5dycXEGPmy2ye4O67l9wDB4gEKFZExZ6N4K03V5dntLRJ7yWuMbdlmViWG0VVEXxFg8SgoZvM-fDSQHMC1yxxpUcPM8asBEu3qwAcTDRC7CRrl9hb5_zFCReyMdJbvgVw4yNEobInayemJO2_Pn68Ju5fHtRV5OJ0gccumB8XZck1jp9Em7ruIvmaZ4OotQE3zCgtaZuVRg2wOg3FmZ2w6QIigcTdJ2DXKeym5-tsawnb4wTuUeu2VQXYEA_K0e3neI__eHLxkZq4qPB-c8AyiKkwEsrqZG1OWYl1EgpkPsy-RH3ASLWtK9b1guDsxDa3MprcJNOymt_l9swMfUvpWVjjr1yc4upqv2uHZYz-EbBv0Iz1v2LaPQBjYD5S98Ghh5OOga_omC7yhSOv4uVWrJ2kJFDyG-JP9IOT0OXrDVKn7qFkEISz0tpQN46tleDjns3A1i0Xt5g5rZznM2_MFH2FmkEwIu1e2_S0wYettiqZN8GrQAnF8RFEHngsqxvqv9KkcPqff_f_nxRu_pMc7hS3kWkvb3g9TNLcM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=phlbvADjwl-LpNObqzholoQv3PQK8oqVI0S0C-Bt2I_3VbvMr00I5PDM34oxn3TixqGm_h2rFJdrdhs4aNBjU8ZRPC9ovad7JLVYHZ7q4giWYiw1UZlWUqEluj0lYuIM3eNdk6glFLkVpQLH5T-AWuczPJfVZBmeV3q7iFxUVpPrcIqdLu-FvKfHX9QDt0SLbo-hCMqx5hcLchQGYusjq4SlosNyPgMZx4peAs2S_23_S6h8nuKd_WSShI9uq8lcYEWe9xghHGNqpcIcoYusaGpRH1ri9rn1wYuVXf8Eyqe5R8kdfh25LUbkz_4EcOjDXR1l2e97esmDCa7KTtrb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=phlbvADjwl-LpNObqzholoQv3PQK8oqVI0S0C-Bt2I_3VbvMr00I5PDM34oxn3TixqGm_h2rFJdrdhs4aNBjU8ZRPC9ovad7JLVYHZ7q4giWYiw1UZlWUqEluj0lYuIM3eNdk6glFLkVpQLH5T-AWuczPJfVZBmeV3q7iFxUVpPrcIqdLu-FvKfHX9QDt0SLbo-hCMqx5hcLchQGYusjq4SlosNyPgMZx4peAs2S_23_S6h8nuKd_WSShI9uq8lcYEWe9xghHGNqpcIcoYusaGpRH1ri9rn1wYuVXf8Eyqe5R8kdfh25LUbkz_4EcOjDXR1l2e97esmDCa7KTtrb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv6bXtizXagzjEENy3qdO_XtVgoJPtNTfQCHpxBIhcWJsdeh8FDrbFdobx5X2jgKH2cMHpMJYyzLrm3VRm2hG_rVE__3qVdueW871uT9V5YVym2mp4IXIUD-1jslGmxER706s5hG7RFKXRYJAicLsUt7doKexh1e0zrZCOw7ARizOnnXfAeN2sozApmvO4kuPQGj5sR5I553xkxTsdK6WGUNznYfKJldDSCEE5MrIUmu-jzwRsCV4CwjBKcflBt6EitMIEXQFgKrFiYBLQaQGn9FyYMqvuAhvCMLpEMi4GonyMf5_6FGhQkSaPegXXY-KzSjI8L66HMvtb4Ny-4lXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SDLkkA-SXFAvuqWjjsmXf23GPijtkn0ZfQG7WaPSs_pOs83r2HIPoIINNyZu_Eo4NxKGRMc9_HA61o3Ctxf9jXR8bojp9nI0t6MARzHHu6KWbD2yWIu6kqUSPJyNVJgtV4ApYuRuyVyjxKf_bVgk1ejD6LxOEJraX6OrWZBlR5yaqZyXDzr9FZVhCb8Skh60HjR_izTZHNkaydblf1xiyou1i3g3FY5nY0MIWIb_HwFrxdj0PmBp5yNumyA-33-uX6LWuTK1039hjbQjl8mD2asQPOWTqFwz7QOzv4MANRkdaCN8oZ-a4PdB-BLdorb_uwv7sbdzCv4jFR-p0dwyoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SDLkkA-SXFAvuqWjjsmXf23GPijtkn0ZfQG7WaPSs_pOs83r2HIPoIINNyZu_Eo4NxKGRMc9_HA61o3Ctxf9jXR8bojp9nI0t6MARzHHu6KWbD2yWIu6kqUSPJyNVJgtV4ApYuRuyVyjxKf_bVgk1ejD6LxOEJraX6OrWZBlR5yaqZyXDzr9FZVhCb8Skh60HjR_izTZHNkaydblf1xiyou1i3g3FY5nY0MIWIb_HwFrxdj0PmBp5yNumyA-33-uX6LWuTK1039hjbQjl8mD2asQPOWTqFwz7QOzv4MANRkdaCN8oZ-a4PdB-BLdorb_uwv7sbdzCv4jFR-p0dwyoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_XsQw4icd7H-6tyUjLl_TaZBkpp5wPZUDSkGsu5PZOL7xKUplNXrnkbJXBFMHG4BbRN5snQlmRvugQlWSqqTOEWX3_OakTRcvwa5Fg-Gf42y7TRut9_jO2XH8-h_L4GfCS9KgD7nB9YTZ9rg5v_DMy4JLS4oy-lS4hatbRZ3_c5TYVBjnlBmxX1-iNFuy94Ibp43MFleGRsXdC52eLoZUljO_yeMkmMSoQeNHK3ZWixr-7K9aAfqU9AcvfbBj03KtocAdGAaKGEgh9GeeR6SnMIRiPsqctJGDdPD9YpU5B5dC-YjYRRhh3j86epqcxc1nQ1uHGtru57i32PiKQgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWae5gpd2u_smmLgpntr3Yyelqbin_EIpc4vsthM2Q1eEBNYjIC9ISfblwDFg6u9V_DlXQYktDMvhZ9rXLMhIs82q8ZDpw0V_11Vjs9QmswjywD9O2MZeuyZIht-Xy__CJlRUyHAYJqQL6sxyTmgfS3WyfYeTo3xfQUHKy4uZSGHmkl16De6xzCKFm9uA-aMJJhLzJcp495Azqzwb2LrGfElSICjsj9uC6arHtN7tF4NC60FcLkNh1_9IJ_Y_zAKS8pvWs8t26AJsgY7xq8coDqp-WSNJuKoOSwEPRdTb8OknLqPd0hHTykEMvpflSNFNAzVEt45Tn7ip0FLZ8jLBw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=EoENjBijGEnCf_yF_zPvU1QpH4L4CpfuUHLG4gOVwD53mPsgh-5j8qKHrtUrbAsbFUAbkUxNNPyYa4Ap59rBxNM-KnYNr4Fwor0z-l_38g72tSAHNSNe5nO4Iv53KLri_2WZFU6T6vDbtg2MyH4D1D4TX92k2TJ5R_OMInFfwJm6TpmtyevuBTcvMKVEJ7FkdHYoQqsThMu1hOfh0QUrQbqpSDm4iSGjENXsdsi3lWl3q718lvPlJLrDMJnowzUEwyOFjrwCY-w091CNuCgMBIldt0S11aby_voyuJPpPUNSSBLmFPKmpb_hLqtFdMttBXvK5_7oBuPouXxGwcyzobsAtu5QlnE_ETjb8TdFNiQIuAbKBH0E0FsTobCeUSFHUq0_--g-VBFzhGl4PKTiDdKq9ErLm-P4xGux9NKxVRQaSa1u1uWfrk8DzB154_11cQl949yCDi_GJSGVdhxAEuDaF7NpWmbczBzbYwUusWeXtp08y2JM-1J8WrWquM4vcMjGx0js8NaL6wbNzb5mKY-IbjBPFhUDUJbDkrqHow3kYq4zb-kB_Tg1dgR3QZMmpWDRlWJco5QZPV5eHT4TuHD17PWp0_YD8POWb27EMrYtZ3dmw5Rd5D00UWj5jAvaVCaYkKxqvq4vpcNgVzJCP_iNimC76FzY7FBejSpXEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=EoENjBijGEnCf_yF_zPvU1QpH4L4CpfuUHLG4gOVwD53mPsgh-5j8qKHrtUrbAsbFUAbkUxNNPyYa4Ap59rBxNM-KnYNr4Fwor0z-l_38g72tSAHNSNe5nO4Iv53KLri_2WZFU6T6vDbtg2MyH4D1D4TX92k2TJ5R_OMInFfwJm6TpmtyevuBTcvMKVEJ7FkdHYoQqsThMu1hOfh0QUrQbqpSDm4iSGjENXsdsi3lWl3q718lvPlJLrDMJnowzUEwyOFjrwCY-w091CNuCgMBIldt0S11aby_voyuJPpPUNSSBLmFPKmpb_hLqtFdMttBXvK5_7oBuPouXxGwcyzobsAtu5QlnE_ETjb8TdFNiQIuAbKBH0E0FsTobCeUSFHUq0_--g-VBFzhGl4PKTiDdKq9ErLm-P4xGux9NKxVRQaSa1u1uWfrk8DzB154_11cQl949yCDi_GJSGVdhxAEuDaF7NpWmbczBzbYwUusWeXtp08y2JM-1J8WrWquM4vcMjGx0js8NaL6wbNzb5mKY-IbjBPFhUDUJbDkrqHow3kYq4zb-kB_Tg1dgR3QZMmpWDRlWJco5QZPV5eHT4TuHD17PWp0_YD8POWb27EMrYtZ3dmw5Rd5D00UWj5jAvaVCaYkKxqvq4vpcNgVzJCP_iNimC76FzY7FBejSpXEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X6kolUu4UAlRCkvFYg7copkaan8lcWZrWfZHa3mM1l-fbFEUPKJPBL1slhsKAPX00IppSNMjUDl0IL1CZ6lssxIst8MRhc8o3LlsTHq4m_XOi0vTntU5aL-59JmUhPnt_VwGU3jowazvcYLfY2JuJHxNZL2_njfn63ZNaFBCUenpo-WglyzBaL0dC5axODyu0I2eM4XxP1tJbqkEjDJ1Cv3e6OPA-oghh_o8lmK0oveoQDsibNzAAnIYRSMkEyoBI3CWRVQLCl5FOoYK1Bg2BQKtvirNlW2lqa7urK6Mr6h0UPqKGLl-Cd1TckMSBnmEquWHXMeBiIPYg67wj7rp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYWhjBdD6ylbsOjN6JM78KH3yMmeGxosmiMXvpsrwsZwCW4_faebFter0XsPguILUDx8BNL9G9ZruKnulzN7wX5wdQfQSAD0P386j3ooBbRRMORMWz_NF0gjUKXgvYnNnSal5ldHMaend_tcSVt5wvKTNekvVYSZmJt1YwOdmQVTtBn_CO3SYfWGwAZGCzyz5FkdBDOlmpx5sNWTYVASr3BU7rwCNqf137IP4pAhIIdAZ6D-wMSopDNKNRUAWIuVk8CCgKa5sQmgU3qYsyNgZeS2VL1U8UeSH43yYE5eW44AhhpLM0xg_Os8_Tj3nZuHaXZ3y4CoxjfRi_5cgSgnwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=q_kStiEbNfnPxx3XWAH9E6n5_53BzgENyCxynaJ-JuIjdxiFS5zWQQiejBJLMydFL4svI3FJHvcVbLydpEXPTMPo8_DWn1SQ2v8OAdEr1VNGwjvr7xKkIvLNmDon4vKe76DTnO11199valfmNG9McrrctR_JgUEGF50su5iOwotlkeCK6B_WX7bkq2Tm3SWFlw20R9TB8Q3szkgqjRK8XY5lM-kogNuuBUeI2zDzunXVGaSmiSRw-LJwDoe3yoKDdVYPTTVLwrr5sjyMCeyaEwSSKWUXVaNCQRqlrLrPvUzCwTCQ91aEu7r6E3FDePUTMY8z5bwbMLYNGFLtLa5Eqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=q_kStiEbNfnPxx3XWAH9E6n5_53BzgENyCxynaJ-JuIjdxiFS5zWQQiejBJLMydFL4svI3FJHvcVbLydpEXPTMPo8_DWn1SQ2v8OAdEr1VNGwjvr7xKkIvLNmDon4vKe76DTnO11199valfmNG9McrrctR_JgUEGF50su5iOwotlkeCK6B_WX7bkq2Tm3SWFlw20R9TB8Q3szkgqjRK8XY5lM-kogNuuBUeI2zDzunXVGaSmiSRw-LJwDoe3yoKDdVYPTTVLwrr5sjyMCeyaEwSSKWUXVaNCQRqlrLrPvUzCwTCQ91aEu7r6E3FDePUTMY8z5bwbMLYNGFLtLa5Eqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ZC0wkVmZ-riUYr9kEbGTHd9UqLcYqNFqXG9e4jfa-ZG-Ocy6B-elqxrCgyKkrkIFkU-QStAMp7L84P3EMqT8xebfQbAmYDTbamEJeWZ_nEfZ6jB7DFBvE57qbjIrflaYD_lqx6Ec0V1bq1cDQIZ-76wWD0_xsuYoR4G5n55pLrd2JROR3IlnGIgpwbkWSXp3m9LUw_2yfwljdeks5FTL_-QKgKl3_YPKIw9q1XAUjgAhtBVbpXeJwHdpg_agZxGfuCAIZs4klNuY4YoXELT6JovRWI81dHuy_nZc4yPcTHdxCaN09lZc_ruuH4tvFb9BFj2zxd4J8SXayHwY42r15A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=ZC0wkVmZ-riUYr9kEbGTHd9UqLcYqNFqXG9e4jfa-ZG-Ocy6B-elqxrCgyKkrkIFkU-QStAMp7L84P3EMqT8xebfQbAmYDTbamEJeWZ_nEfZ6jB7DFBvE57qbjIrflaYD_lqx6Ec0V1bq1cDQIZ-76wWD0_xsuYoR4G5n55pLrd2JROR3IlnGIgpwbkWSXp3m9LUw_2yfwljdeks5FTL_-QKgKl3_YPKIw9q1XAUjgAhtBVbpXeJwHdpg_agZxGfuCAIZs4klNuY4YoXELT6JovRWI81dHuy_nZc4yPcTHdxCaN09lZc_ruuH4tvFb9BFj2zxd4J8SXayHwY42r15A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=RI1WuSyPvLyZ8_OTpF5suaZo-hhNbIQd571ItFN8vXNnDRfjTSUKOkcfQtyhsWe-hZz_f81K6CJazcuFXKe6UvUCvWj-8sk6tut8GPXrkHCiOxDCnyjOPcMeukeSRIPjHM4OYypquwTZGnQtXlJrNIuGmNkHK0Xpd6zyPKit26cYXWRXf1AEsajFP65Gnosycu2U5OWa66TrlcvBzL4CqSGkp1ZAr4k09QSXCVQf6pjYwzSmrWM832MzuuTF4rUTlqRenMgXMrGyz_Fhj9n5l6U_UHTpp_f0AawIbrOpcfWrGXviAlayGbAXKfb7wAFJ3iw-AglZ_KLSIW8dsGZlqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=RI1WuSyPvLyZ8_OTpF5suaZo-hhNbIQd571ItFN8vXNnDRfjTSUKOkcfQtyhsWe-hZz_f81K6CJazcuFXKe6UvUCvWj-8sk6tut8GPXrkHCiOxDCnyjOPcMeukeSRIPjHM4OYypquwTZGnQtXlJrNIuGmNkHK0Xpd6zyPKit26cYXWRXf1AEsajFP65Gnosycu2U5OWa66TrlcvBzL4CqSGkp1ZAr4k09QSXCVQf6pjYwzSmrWM832MzuuTF4rUTlqRenMgXMrGyz_Fhj9n5l6U_UHTpp_f0AawIbrOpcfWrGXviAlayGbAXKfb7wAFJ3iw-AglZ_KLSIW8dsGZlqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ti1Ms8DcxRhOsxYkxu_dHcjEapdTCbPt3e0BuhC9n6gTCJOykeB1muG_cypsZNcFDVBTjj3-O029vtnJZ8_hAjM8Ze4gVMN3UDMUUfL2N-MbgtUzQg69h8ACXyUbbM9-_twDnoN17zicUfeWbMjix86mJdLHdMlCeCZXXVTq_pQka7PV6DvgrRBGmu4lMtljjOo7Y0IJWkmL2APcevLSgJW7fYhvVPo-ulX0T29VgF1VsXo7c6qM4nCXKByZDaRaO3p8dEFzASW2-B7DED9GndsemHZRKgtMtp14CRJAB2G7WU3-fVsVSno9g8KvZCpThwvPVMj_t6ED9acYouIezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LwTCgexsTHiVv8k-TErlqa67nOP565MbEN43QAA14NFWJiemrkK182-yNCYj9Ov3aGsa77LoNzA32XpHqcw3xeQ7jP2MmepU_M1XKWDduUYeQ_-IDZxrpdMcDyq_UZSmkciQrd2rRr8pBZB02EI5GPbCAaJeR9qXW0gFywriurMT89AabOTjMZJ4nZZCenXxq2eVStB7REReVgW7YYtqvL-D0YUVuE5JD1oCdtifAHlN3nHuot0hJ_V352rxIHqTV9y7Tdwa1jD_aRPGEbPBnuUeD1v-IWewDyW-LjfHSiG8Ce6XZBbqb7gdlfdlIj9s-TNwKwEuWd-gk7bLWPB7uU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8LwTCgexsTHiVv8k-TErlqa67nOP565MbEN43QAA14NFWJiemrkK182-yNCYj9Ov3aGsa77LoNzA32XpHqcw3xeQ7jP2MmepU_M1XKWDduUYeQ_-IDZxrpdMcDyq_UZSmkciQrd2rRr8pBZB02EI5GPbCAaJeR9qXW0gFywriurMT89AabOTjMZJ4nZZCenXxq2eVStB7REReVgW7YYtqvL-D0YUVuE5JD1oCdtifAHlN3nHuot0hJ_V352rxIHqTV9y7Tdwa1jD_aRPGEbPBnuUeD1v-IWewDyW-LjfHSiG8Ce6XZBbqb7gdlfdlIj9s-TNwKwEuWd-gk7bLWPB7uU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QgJhkd6W9l_MjOXXM2VEYRkcJj_zJ0NetRyjaYDPDagu0Kn3ZWB_FDnt60FuguK_yQ4YhUfNqOw4rNMtiY1FkZhJ8PEJP-gP8WH6l1CZTUUq_M9ABfXQEDyWtgErF0lO609eEKjgPByaV76DhkAixohbgRoAh1hVpx3cX1eAQGzEe60NwGWzoGGlFgw713j77zjMCwXXlCCsXgE_eNBPyVr4D3-YAtpeWHQ-ELNooi0YO7K6i6QalcLR8hHmU6uUO84iW_yYMLoXlGTaMfEJqezfbUl-p-Q-4n0sTsH5wtN5NuQ5lpBo6XM0e1OERGxG68tHHg_ScTEN1eNj_ZeNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QgJhkd6W9l_MjOXXM2VEYRkcJj_zJ0NetRyjaYDPDagu0Kn3ZWB_FDnt60FuguK_yQ4YhUfNqOw4rNMtiY1FkZhJ8PEJP-gP8WH6l1CZTUUq_M9ABfXQEDyWtgErF0lO609eEKjgPByaV76DhkAixohbgRoAh1hVpx3cX1eAQGzEe60NwGWzoGGlFgw713j77zjMCwXXlCCsXgE_eNBPyVr4D3-YAtpeWHQ-ELNooi0YO7K6i6QalcLR8hHmU6uUO84iW_yYMLoXlGTaMfEJqezfbUl-p-Q-4n0sTsH5wtN5NuQ5lpBo6XM0e1OERGxG68tHHg_ScTEN1eNj_ZeNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCEuXfmEt-Nxd_Mn6mudHZqwishUj8sH7ajwepdu4bmuZXjGuMdjyM3_BKVnN5KtenqJr-FVSCws-DykjFryzK7sCOTyeszz4z17n6ukdYRn72wNa9ektfItz6hAwIgusQthDSI5ZItvLNeDcDPS6FwTDUl1JNHqaWzgEjK9o7nyStpJv_NVeizq7UUH7aDNtzrrLQZc4E6xXUNtCgi83OiRa06W56GYa5YgqzYF-g02UDldT-Jq73d51o3hRZMvUE4tbF0EgtOWTdkIFcCSe_AYEH1CGF8gJFr6GHOiSTqwwpukRU23X5c99wy-GodZKnHeYUf6-xVnFCJcTHIhjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=bPBp5YdRNV1NOoikqLUtQxi-q0qpGuf4We3MMBoEGScTRExK0LrXTBaJi6VY_ZuTCqROLkqciJEglGngszzMj_iCQaQ0ZdFETWM9To8J65g13B26Fg8NBeqFNYkh16qgSahNYRtOWXJ_j7ur1CeNdpQcZDAr_BDiqr-bliM2_lJxd1T1zyx-hq9PqBlTg2w2n9_sko76guM877k-WpHLLUXf7OIC_Rq-51VTsVxsW-TfC4e9l75igRxvuiR5jnjVI5H3rYc3sXLw8Hw0hDElGIYz0PsagAW1VwATfbcF0Y-OQ_QOnkwFAJEdI-ib_2HNA10fDnjAOV8hivLiZep3-SmNR9yCb153rZZ9VzK7oPw1TeghdjGTnoRp5bQ5L11K6hbrtjAEy3bYRSU37eWXXWnB-WM4ZxxWlSNDEnJ9cc37MsWI26Tszme-qSwpr6QvjNOKaZ0UtTXc8CDROXjqPqkkwIxNFyZr76FxmIuicyL6eNo9yoKcbHqNny971wUntcyv3JvirGQcdu5gnErAxVJ6LXZJHCk4RuR-ebOuxbSQyTpAtGj3QiJBC3QDt6G5WrLbiIE4MvYzwMINoszcp475KaLfNxRHIm1B7MMP_-glJR6W_wDnFBoYIMqgdYjlrdJa6eECHFuE_1H9A0wbuPlbi03MSojtmnvEO-RlhOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=bPBp5YdRNV1NOoikqLUtQxi-q0qpGuf4We3MMBoEGScTRExK0LrXTBaJi6VY_ZuTCqROLkqciJEglGngszzMj_iCQaQ0ZdFETWM9To8J65g13B26Fg8NBeqFNYkh16qgSahNYRtOWXJ_j7ur1CeNdpQcZDAr_BDiqr-bliM2_lJxd1T1zyx-hq9PqBlTg2w2n9_sko76guM877k-WpHLLUXf7OIC_Rq-51VTsVxsW-TfC4e9l75igRxvuiR5jnjVI5H3rYc3sXLw8Hw0hDElGIYz0PsagAW1VwATfbcF0Y-OQ_QOnkwFAJEdI-ib_2HNA10fDnjAOV8hivLiZep3-SmNR9yCb153rZZ9VzK7oPw1TeghdjGTnoRp5bQ5L11K6hbrtjAEy3bYRSU37eWXXWnB-WM4ZxxWlSNDEnJ9cc37MsWI26Tszme-qSwpr6QvjNOKaZ0UtTXc8CDROXjqPqkkwIxNFyZr76FxmIuicyL6eNo9yoKcbHqNny971wUntcyv3JvirGQcdu5gnErAxVJ6LXZJHCk4RuR-ebOuxbSQyTpAtGj3QiJBC3QDt6G5WrLbiIE4MvYzwMINoszcp475KaLfNxRHIm1B7MMP_-glJR6W_wDnFBoYIMqgdYjlrdJa6eECHFuE_1H9A0wbuPlbi03MSojtmnvEO-RlhOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cpFJ0MIn8h3HARzQLuGJHmwylMlyjmUJKYn6MQF4ReseIlRhD7uVHZFBxPoJTQpE_SBF-VIAFiuV2bMC-TVRH8Rk9MWa6qYQOgq1_SHg2nL-1HMxEiBqI5Z05btEWArl40j1tf2qS00w6DymZ-dYBssxxr1-h9XDPXj0FPkuOx99jVIVMExcl4QZReA-uSswwa61eKBCBUAlPYbiimYSXDXdHaKKTK-CuRyoTP8hxidVwHexxm4Kt2feRgULgPyYWM4DhaCqscFW03cS4kcQY80vRkhWPtQBbUU1o71_J4SoSUwURqF7BUsFUa_jiVUpSAPulErANbnWyDT30LFWEQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=A4cIdwxE8dAF-hUHUquYL5zWFj_I3Uu22Vs9tUJl3pWQerhvTXAQJwBdD3fwHkv7WSzT6b52j0cAQKulGcsAJupfYuPsWgb8oFuRW6f1MT7u92h84129PW_fbDpBUsKB2HCTmNmtBSwVghsX74Jf6YgOjw_K9cnHuoLts6NMh3nf7-l7MOlqOlbvek1w8T5T0w7gF22Hw3xbnI1YogPeGDS8NZ6IG_jGoao70L9YzYpcv87P5Gv7aqx7dm02plwEJqIo3SgUbE9PUU_NL6f6oOngLOw72UGG5ISen8W-5xdWEMkuyyulnX_21TZERLEuoY3rbVjtHOOrpHtIVVtjbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=A4cIdwxE8dAF-hUHUquYL5zWFj_I3Uu22Vs9tUJl3pWQerhvTXAQJwBdD3fwHkv7WSzT6b52j0cAQKulGcsAJupfYuPsWgb8oFuRW6f1MT7u92h84129PW_fbDpBUsKB2HCTmNmtBSwVghsX74Jf6YgOjw_K9cnHuoLts6NMh3nf7-l7MOlqOlbvek1w8T5T0w7gF22Hw3xbnI1YogPeGDS8NZ6IG_jGoao70L9YzYpcv87P5Gv7aqx7dm02plwEJqIo3SgUbE9PUU_NL6f6oOngLOw72UGG5ISen8W-5xdWEMkuyyulnX_21TZERLEuoY3rbVjtHOOrpHtIVVtjbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beAAiRuA1orcu--I0fN1tLSZ4avESCKV7WPgtDdouiqbGK9BL6jX9Bbc3Zl-Ma7T_IJKlop_nhosj7H6DYoBQoLm6gz0Ln7WBEy1a1bzWUVTRpmDFL87SMLXOmogIUjFu6wJAceu16cNnmjpPOWqr9CWS_JStOEUqvAB39QhY7UGf-p5IsF1p7ZrCQt7w1UHRjHzTVc4mC_CBjGunGSRBKODggsjYWFk94Nrk87sIpcXJiH65kojHv_CnvcUFqHh4h7NiXGCzq7LRWB8wag2BRFh7G3LdvPN-C2X_Bbe_yb5MYohwfz81-mgEcdpwh5l2_G1TJY7xgy1TEQQvl1RbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eNFJU92TQAhn6yEsPV2zgAGz057v_m6W00m0bzMy7kOB4tct132h5YLkmCHt3Y19ePC9ncTGOmMBTVHjw0pvaNT8HlgC37V7x_x09qAhScUA9hfV7QYDERI7CWiWi3_46XzfXydOgfP6SuSMXlCjn5Z6xwh6JpnGmzn8958lBF43KGnlSMLenISytJAWfLZrhOSmkPza2g7Lq2qyEzm9nQ5-MD07VDk0OmRb2QeKb5IYlzpvxW9-vT12-d76_i0IhNalW4NS8lKln4KmAiptQRuWX1QEZvalwUJ22d34HfjVUVAyELyjwhvjJHi2dm8542yffFRRC1-lF5n22LdEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2t2yWQAYkuNxefMRC9AZlSIg2LxAkeg3kkDAPddBSlTrW0GvNP9u1xc3afWlw2r-sZ6s3aVv0xXfwMII4A3ACghi8YxsPqNVuZDiunNo1vyTGsXBQ1KNhTjY-LFKdDJG77XVTuilv0sQIH5o3kKIofw1TBWkvNz_0HFH2sjRxYbMVE7kTyX1ZlaLihOyjvgriXASSA8CXAgcz-ZlCqwDLAcB7O1I16YJ_ojQFYI5SoLeyEc9vBsmhTbe-A1k7vPESGEWHlb9gfF8Mz7F_7tDV2iwzKTvjP1CVOi4614oUWFt_NSI70Y5KGFPGxi9KxetoZYf4zoeMophgd5c78sSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=HBEEPcWx7k_ONACU6IYVDuzfnZgbHtdQ-vXG6iRb0V3wkrlIprEushg5Jy9y2lcC8OTgA96p1CXS36vfy8qycAGPLtRBcGUAadPlznDMGN6WBumDZlL2njJhvoCb60AJ2xGvsEr-kBqYCSP5hfH6xNMsyKxH3f_iFpwpIuKmJdv2E9SAE-MT-j0bSYFQ9hL33NAG_DhET0Qqre02d1Z-VPq3S0FbgvjCiFbrNyYlw6MBhaVcsxweFmiVjAulredjX1BeGBqZ9aGMlU8GutXdAVeJD8tSlmKBxyfAYGSGZkjgYQnuCC2YQBX7q4z5Gu4rnKLE3QAJgCvWea9FGf17Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=HBEEPcWx7k_ONACU6IYVDuzfnZgbHtdQ-vXG6iRb0V3wkrlIprEushg5Jy9y2lcC8OTgA96p1CXS36vfy8qycAGPLtRBcGUAadPlznDMGN6WBumDZlL2njJhvoCb60AJ2xGvsEr-kBqYCSP5hfH6xNMsyKxH3f_iFpwpIuKmJdv2E9SAE-MT-j0bSYFQ9hL33NAG_DhET0Qqre02d1Z-VPq3S0FbgvjCiFbrNyYlw6MBhaVcsxweFmiVjAulredjX1BeGBqZ9aGMlU8GutXdAVeJD8tSlmKBxyfAYGSGZkjgYQnuCC2YQBX7q4z5Gu4rnKLE3QAJgCvWea9FGf17Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k9x74U4dvSiiGYsyLS5qnGFMt-wG48Tw5r_NpZp4qP4QMoszoZ2dhHQospkGHMpJjAvUhgQbcU5j7y5W_doPWsBZmR1H0-JWr0TrUSgjTOtwiTLKYgBYflWIB-rXo8thV87ZsPTpba4icKJedZfJDCQ317ND5q9AO47g3fzp-mPy0zBUkP6Oi1FKucJz9F74aAmX_6O2irePdv_qKy_0z2oGlI3ZTAfA8Ukn--VWIyp4V3J_v4uKeqH1Dz29EJad9Oq80bJAVcaWRSf_IoZo1gYn2E23U5PPUqGeQx1JZxoF-kcj48gHck0mwDZnqd46xq6_c2BKKuSV2vyvXaShtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5Yo9DqjAEFxfYOJzuPCpn9bsx45xIfb-3d12mDNqtsBQa-Zel2Da1AzcueCEzxtGI5S8Lii_5Vy5zQ8IfBh2mtrnkXSp8kdwSOeSkeGhemLAZfJWi7aQckY8sjMqdpUc7tbT7f5s211ddwJjgF4MaizljH-AgPBQfK6GyRggf55NEJEjL4mKE_jUDWUmt60bddxP3ktOWYDU0PGOdVyjGRbf3IEVPZoIhy17azvXpGnqauW-6KsLWQAJChFXVEcG9y1ViQzwEXDKCSiKbMhA9W3mI5qm0f-aD9vXeL3G_eA_I0tDHr4Aa7jflxRrk3B09BujKZmMqnFJUWmL3hZoLk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5Yo9DqjAEFxfYOJzuPCpn9bsx45xIfb-3d12mDNqtsBQa-Zel2Da1AzcueCEzxtGI5S8Lii_5Vy5zQ8IfBh2mtrnkXSp8kdwSOeSkeGhemLAZfJWi7aQckY8sjMqdpUc7tbT7f5s211ddwJjgF4MaizljH-AgPBQfK6GyRggf55NEJEjL4mKE_jUDWUmt60bddxP3ktOWYDU0PGOdVyjGRbf3IEVPZoIhy17azvXpGnqauW-6KsLWQAJChFXVEcG9y1ViQzwEXDKCSiKbMhA9W3mI5qm0f-aD9vXeL3G_eA_I0tDHr4Aa7jflxRrk3B09BujKZmMqnFJUWmL3hZoLk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ndFj_p5lN9NfY6CscW3QQ9-72h1wFkQlkpbWyiSmZ4Ld3Msw3roC5dYd4D5V6jQ2zwtQZT6TYAweEb_utZsR-m6mT3sIEs8JSoRlW7RmSOgdBJYtSkGwx0iXNW-bWB9dxvSZd1KAe5Q63Rj47Qgmbq7dxgFYPNLsxziCuGIOLKMeHK2iQ2rV1sGloJPedjkweDwxf9HjLwSqYcKcc6f6HsDhJHqgQOZkjiq51pmpcsDJv0K3wWPixI5H6AcxL5DuoWvw_30atF1K433MyyAn-fnphFlUAVA8JMsGndcYjsl5mpm2XXj0--_wGHOo_MK4zD1ChkViwyudSf-e4SV8zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=ndFj_p5lN9NfY6CscW3QQ9-72h1wFkQlkpbWyiSmZ4Ld3Msw3roC5dYd4D5V6jQ2zwtQZT6TYAweEb_utZsR-m6mT3sIEs8JSoRlW7RmSOgdBJYtSkGwx0iXNW-bWB9dxvSZd1KAe5Q63Rj47Qgmbq7dxgFYPNLsxziCuGIOLKMeHK2iQ2rV1sGloJPedjkweDwxf9HjLwSqYcKcc6f6HsDhJHqgQOZkjiq51pmpcsDJv0K3wWPixI5H6AcxL5DuoWvw_30atF1K433MyyAn-fnphFlUAVA8JMsGndcYjsl5mpm2XXj0--_wGHOo_MK4zD1ChkViwyudSf-e4SV8zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=lPzGpnPKuNiMwmRQlhVHIaCuHgMyssezl2ThoJGHhu_BFEf0UvlnHMnmr2lw21RimQDoHiBKaJBNl_WxmbiUX4mdt58OaipJ1eKY0_lskwD_Mye9OVYRvJ8vlot9EeJ5BkfHIHqkXCLMZNvxDus7yeDwYvmctuSEG5YyPBcJzGEkuzxu6tkunoKJLzsepu3Wl8yBL6Tm8Oe0iTqGNG6rNLnUNY65NZBcdCVb4FiqHuP99b2KKdR-IHwbudvnBDNgfeXXHdQv8y4WU1_tvtUltv06ZxGqWMs38SSaaNcogA5NRNDJ-_FO40wfJddQdy_ZX0Vs17SviyURZFAvnJd-GHnNh7xib3ZLb4Bf-t6iC1WiinBeoio5i9kIpX-Cd-Ry5M1iHOn0V1Qpro-nthtUzJ-xoBi-SR27MIHeLcOCM5i_WJgdkkFeKvW5qHNHOs8HokxXH8NX0WIXR0jWD0Q7WKkteRaAy0M3Yj1cDQ5e8FkiXe282yBYA6dmifX2o-qrd4ECCcOVQ1do_-Y-MYJDksVuuqz1L11zW73qXDIObHdQWwrcHGsBMtmUr0GhiG1Xik6vBmDenyI9MQVgCqlccoV421-4TugVgk_UGMf2KOKi3UFwCJIsrGurAYqHsk3lXZ-g18kc8FD8J00vYLLFz5PtUWB6yDaF44FjXedXCM4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=lPzGpnPKuNiMwmRQlhVHIaCuHgMyssezl2ThoJGHhu_BFEf0UvlnHMnmr2lw21RimQDoHiBKaJBNl_WxmbiUX4mdt58OaipJ1eKY0_lskwD_Mye9OVYRvJ8vlot9EeJ5BkfHIHqkXCLMZNvxDus7yeDwYvmctuSEG5YyPBcJzGEkuzxu6tkunoKJLzsepu3Wl8yBL6Tm8Oe0iTqGNG6rNLnUNY65NZBcdCVb4FiqHuP99b2KKdR-IHwbudvnBDNgfeXXHdQv8y4WU1_tvtUltv06ZxGqWMs38SSaaNcogA5NRNDJ-_FO40wfJddQdy_ZX0Vs17SviyURZFAvnJd-GHnNh7xib3ZLb4Bf-t6iC1WiinBeoio5i9kIpX-Cd-Ry5M1iHOn0V1Qpro-nthtUzJ-xoBi-SR27MIHeLcOCM5i_WJgdkkFeKvW5qHNHOs8HokxXH8NX0WIXR0jWD0Q7WKkteRaAy0M3Yj1cDQ5e8FkiXe282yBYA6dmifX2o-qrd4ECCcOVQ1do_-Y-MYJDksVuuqz1L11zW73qXDIObHdQWwrcHGsBMtmUr0GhiG1Xik6vBmDenyI9MQVgCqlccoV421-4TugVgk_UGMf2KOKi3UFwCJIsrGurAYqHsk3lXZ-g18kc8FD8J00vYLLFz5PtUWB6yDaF44FjXedXCM4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=DxNVKMlG1HxgW88zUN2N2_0dSnQWJBIZ4WBesmZKTsCBIaj_so-KWY_gPm3LNp6gFRO7FBDj4wvWIRKLhq78hv625HbAxwvja48BNVVPP_zRKUvLhS2jGbvh6-hgpgfXQL_3lOBS1ARpaVICzpzYsG3h8sx8plms-7rlMonI7Znc65tA72Y3Ywb9PFcxSDn7xHGu1ZptV_W1qqQzjoPBjP4xEvKQ2jRppSqDNJg4EDLWJE7XXPO5Q0WwztOtu-CoPjlJ9gxEwvKjQOV_3Xlp8gr6YFBcpCyywGhewpzTsz6dNnu3UmDHnqm46d26mPKp28sPExSxKhnoaiYkmYw8jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=DxNVKMlG1HxgW88zUN2N2_0dSnQWJBIZ4WBesmZKTsCBIaj_so-KWY_gPm3LNp6gFRO7FBDj4wvWIRKLhq78hv625HbAxwvja48BNVVPP_zRKUvLhS2jGbvh6-hgpgfXQL_3lOBS1ARpaVICzpzYsG3h8sx8plms-7rlMonI7Znc65tA72Y3Ywb9PFcxSDn7xHGu1ZptV_W1qqQzjoPBjP4xEvKQ2jRppSqDNJg4EDLWJE7XXPO5Q0WwztOtu-CoPjlJ9gxEwvKjQOV_3Xlp8gr6YFBcpCyywGhewpzTsz6dNnu3UmDHnqm46d26mPKp28sPExSxKhnoaiYkmYw8jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYPBzKIVDk1NWO14YIWntvmhMY1fg3dTbakMBjkzt2yVxHZp4C5kCmS0TrqenvjXo7C4ibOHl9Hk7FC6xn8Lz3dSnzREozjvRvvi8HcqhwFH3p8rzFd51MF-rl5_LF1p8tqFpp-D0bZSJuPT5ceJ0LfYPDk_JFH659dd4ZYk0IqqekX4FX3izTZ4ec4ZFkPB6pM_LdA123BLloR1Jhl2iwqNBSnLJd6OCHaEpHVnDhMflArtGe6Wl3r2VFkokkZJ9_xagR4d7C33pp7zR4de2_oaARVBR9Rt8hdmr3mF0QIsnIWun1JX9Zx2eNw24SuQic-EWUhBzJJRhyZqDSB7Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Tb3C2-fS--Rdr-EJf-ZVnvvulhWbHQIBMGi2x1R2UNX0DSk99umxuNl9kXvYuvcuhyy-NZ8zaX7kt66uM6sFbXDxSG48WreNiJofnJ0QZQE2hxYvlVUtDipg_oS2YUDzDl_RU4jO9TXYZH_JWtzEg4dx6VLbg_VgF3xSbyUQoWKiYN13I0K-x76hW0poGNF8myqgnQSWCKmlxKvrra6xDN1zwuSyE7t0QULnxqjyLD8P9IUXCdd-vpXw6UO5wLpnSjYm-9qEm_pTIObgCcuMqVwoVnirtmeyP8bcCCSNCIjkkxloZvpKqYuGjiZKoEumWjD_bZ8JHyhfaSf5g6k3-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=Tb3C2-fS--Rdr-EJf-ZVnvvulhWbHQIBMGi2x1R2UNX0DSk99umxuNl9kXvYuvcuhyy-NZ8zaX7kt66uM6sFbXDxSG48WreNiJofnJ0QZQE2hxYvlVUtDipg_oS2YUDzDl_RU4jO9TXYZH_JWtzEg4dx6VLbg_VgF3xSbyUQoWKiYN13I0K-x76hW0poGNF8myqgnQSWCKmlxKvrra6xDN1zwuSyE7t0QULnxqjyLD8P9IUXCdd-vpXw6UO5wLpnSjYm-9qEm_pTIObgCcuMqVwoVnirtmeyP8bcCCSNCIjkkxloZvpKqYuGjiZKoEumWjD_bZ8JHyhfaSf5g6k3-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=tWP310PXMiqX48ptWMB1YgW-KMnVjZe6_WcEQeZmOmNuuvcaZJhL0uVHRcdKDxfWfaXPntV1fq0FFesdJIwfSIe-KlMclqVPgn-QZpugm7vMi40-QLc8-9vQKahuKn5ibAYmLvw86tkWtKMHnHRB8LrrtW4Gi9CQQtoCyQ-lmGc4GHfscI5ahvwVCl_ADwkrgCQ6-w7v4Cm-gXwM-yM6uBnlwB0LWXdaI-1bIJvT-AjoOG4vDpJi9CiL7EhdNi2GBxxAeyH5VnoxkT1qcjb6TnYd6PmJ4mQhE8qjCMaGWwbTrTnWLTFoTd5Xs51KLOoep_xEPfw9e4UtwLgEkA62l3OUF5Q4xaLKQFlTaJ2A3qtQg9lWnA7ioUx0ZjXmK6W71b1Ek3ELkg0qUmw4lvfAgiqEUZJfrxljCyDunOm7yDCSA8ddPdW7foxva9ECE-_n4gTlHqWZJth5K-uDdSat7GQC1KwHdJfNvJp53m454mL-vG8Ob8_KivV4eeXRNMwj7J4hYR05hpkkxcivgAGlq_2qvL_-c5F6qaKnwXaQT9XwT5hN5zATqliBDSRCrxbjnzwj8cANVxAS-Oq6BW2itcUmZyALk-jlfY2olk5eUclO59anWEQbJrWsdPfYYSHPW5zO0jyEO0X5G2mCA5n9znHuCJjfveSNcjuqeIbEypU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=tWP310PXMiqX48ptWMB1YgW-KMnVjZe6_WcEQeZmOmNuuvcaZJhL0uVHRcdKDxfWfaXPntV1fq0FFesdJIwfSIe-KlMclqVPgn-QZpugm7vMi40-QLc8-9vQKahuKn5ibAYmLvw86tkWtKMHnHRB8LrrtW4Gi9CQQtoCyQ-lmGc4GHfscI5ahvwVCl_ADwkrgCQ6-w7v4Cm-gXwM-yM6uBnlwB0LWXdaI-1bIJvT-AjoOG4vDpJi9CiL7EhdNi2GBxxAeyH5VnoxkT1qcjb6TnYd6PmJ4mQhE8qjCMaGWwbTrTnWLTFoTd5Xs51KLOoep_xEPfw9e4UtwLgEkA62l3OUF5Q4xaLKQFlTaJ2A3qtQg9lWnA7ioUx0ZjXmK6W71b1Ek3ELkg0qUmw4lvfAgiqEUZJfrxljCyDunOm7yDCSA8ddPdW7foxva9ECE-_n4gTlHqWZJth5K-uDdSat7GQC1KwHdJfNvJp53m454mL-vG8Ob8_KivV4eeXRNMwj7J4hYR05hpkkxcivgAGlq_2qvL_-c5F6qaKnwXaQT9XwT5hN5zATqliBDSRCrxbjnzwj8cANVxAS-Oq6BW2itcUmZyALk-jlfY2olk5eUclO59anWEQbJrWsdPfYYSHPW5zO0jyEO0X5G2mCA5n9znHuCJjfveSNcjuqeIbEypU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqP3tLGTsxA0Tipt6XXHiRK3b9Zazk44nmOs6vNaCTFyBvYsNSA13RX7XIjecKbQtktRVYonwd-hbGsX9UuJIgcTLJgPKzimK54-hu87lnh6yOkitXryfHRoJP18KOnC27DAiA32TrG46EHc6uF6orQX5Bi-UqKXN5LffyYBAR-m0Gzux3NOQ6ZbKa6snhTYF7DQAld9gDhNVZD4f5uvTy4Mw80IXdlu1ed72pKhD8wbUgIAoUFpvToyjFHx0sfjlrsdceXd1P916-qBEsWnik2cHKQ2Jcgd2oGP19tW4Tp5EEX5ETxzTKnGDZ4W4Sagykf58OSep4g7E-ow_i-uwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ghwNsZVan9YepIn7OGOmCc061rUsCUUaR0uU5ZO--Ruyh3i63jvuxABDfAcnuuMJP07pOt8CFVUT03fZoBHIgr-yYREM5JW-7DCXyQMQ80AinQKXEJQWZx2JQ-Zlpixi_bKf83h-QKiq9hPGs5a0IzufDgIUiN86eotQUDwtsrBJMALbbh68Tcjnrtv6TA1yl_4XBjlJOlF3IIN6Btd4LU3HqEw9ctp8YyOJcQgdRmNAIuP0iF0gESdw0s533I4dFrYQR95splUYP0agRL4BRioN7cG8rJ6PNwxQwFN5QRo-XkrLLui5skOUO3K33B9xy6Ul4t_3BuVlzbc1mhshMThTpLfFw_Vx0jlC6pv2PeSwPmmnmO2ybS5KU0OzD836wtWXFofLYGE9AvkA7QYRXwGimIx_nsKteAV3Jww137mCoC1jmk6sTyeHxoYlQOYSJwPVUg7xNv2CeN_r2rywDdjp-1zvBGGo77DVMb6U9Tc4IigDQE-5uNGUBefqnErs8RlHuQcIEq2BA9dYhMnG05084KxBo6_QzBnXn0v7sYzyw5F461zw66vJFXsuA_d-kbCblkFhQgOcpa8ug_DVeuihLLv0lpccEKSpvltWC9dtF1WPmp_vq3OaZ_v5zag53KltU7Pd9SbALKLPhVD31E4_eIfR8Yk6yZIQyTxDvWE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=ghwNsZVan9YepIn7OGOmCc061rUsCUUaR0uU5ZO--Ruyh3i63jvuxABDfAcnuuMJP07pOt8CFVUT03fZoBHIgr-yYREM5JW-7DCXyQMQ80AinQKXEJQWZx2JQ-Zlpixi_bKf83h-QKiq9hPGs5a0IzufDgIUiN86eotQUDwtsrBJMALbbh68Tcjnrtv6TA1yl_4XBjlJOlF3IIN6Btd4LU3HqEw9ctp8YyOJcQgdRmNAIuP0iF0gESdw0s533I4dFrYQR95splUYP0agRL4BRioN7cG8rJ6PNwxQwFN5QRo-XkrLLui5skOUO3K33B9xy6Ul4t_3BuVlzbc1mhshMThTpLfFw_Vx0jlC6pv2PeSwPmmnmO2ybS5KU0OzD836wtWXFofLYGE9AvkA7QYRXwGimIx_nsKteAV3Jww137mCoC1jmk6sTyeHxoYlQOYSJwPVUg7xNv2CeN_r2rywDdjp-1zvBGGo77DVMb6U9Tc4IigDQE-5uNGUBefqnErs8RlHuQcIEq2BA9dYhMnG05084KxBo6_QzBnXn0v7sYzyw5F461zw66vJFXsuA_d-kbCblkFhQgOcpa8ug_DVeuihLLv0lpccEKSpvltWC9dtF1WPmp_vq3OaZ_v5zag53KltU7Pd9SbALKLPhVD31E4_eIfR8Yk6yZIQyTxDvWE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Dp5E7cwNNb3ikEHWGG8InY5GUEauqcioHlzC85zwtdF_C8gpNAKPZaoGjCGAciQ001vTtomyy5Oyo9vKChJmcuK1Hkao0CVUYSuTlX03gIO7Tv5KoVqfxTNu7S3b1qOTD0FBZ2q_MAauBdO5qyso8iFkPiieOV4DK3pOAD7FE3-95ci4CV047Gfs7iT0kiBtrQ6oWnH1KzzfVAe45CocKmwq6H4IUoZIqzcnQp04NoFRWYgT9VovO_MH2NOCjE6odnxokygE5BkioOUZpF_ZKIu4PZE9WzbyGoivB3u-X8j4kuH6hz_GEoUZy7riweK3-HZFdX0gPhBo3QvNoPGJ4lvV4Ez6rJ1E_PKO84z-wvWuiBuXZhppflBJ_PBbu1IuBR06HuIjJueykE96wN6L8VBsXkJAjXNjwUU813zUw1BsYgDJ9dXj2hHwLB0vzeCcuwOGTBVzHV8xunmSY4Cgtcc0ecRqIgajJfefXa6uoO-6sok9IL5wbvUIqUdN073QE_Rm3oGeoVVHqFndGDthpLZpV36nNNJzX-oQWwumhT0_5cro4m76uabkrFKjar6iD5ceerUwxtPJ8rD1Oxod19ADaC0rkfgKHtWUxOVNBqQjt_45u4gYfJ7oKHExb5e5andqi01WZF8AvqJf6OR3OdbFk2d_7ro2CkIYKFprVr8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Dp5E7cwNNb3ikEHWGG8InY5GUEauqcioHlzC85zwtdF_C8gpNAKPZaoGjCGAciQ001vTtomyy5Oyo9vKChJmcuK1Hkao0CVUYSuTlX03gIO7Tv5KoVqfxTNu7S3b1qOTD0FBZ2q_MAauBdO5qyso8iFkPiieOV4DK3pOAD7FE3-95ci4CV047Gfs7iT0kiBtrQ6oWnH1KzzfVAe45CocKmwq6H4IUoZIqzcnQp04NoFRWYgT9VovO_MH2NOCjE6odnxokygE5BkioOUZpF_ZKIu4PZE9WzbyGoivB3u-X8j4kuH6hz_GEoUZy7riweK3-HZFdX0gPhBo3QvNoPGJ4lvV4Ez6rJ1E_PKO84z-wvWuiBuXZhppflBJ_PBbu1IuBR06HuIjJueykE96wN6L8VBsXkJAjXNjwUU813zUw1BsYgDJ9dXj2hHwLB0vzeCcuwOGTBVzHV8xunmSY4Cgtcc0ecRqIgajJfefXa6uoO-6sok9IL5wbvUIqUdN073QE_Rm3oGeoVVHqFndGDthpLZpV36nNNJzX-oQWwumhT0_5cro4m76uabkrFKjar6iD5ceerUwxtPJ8rD1Oxod19ADaC0rkfgKHtWUxOVNBqQjt_45u4gYfJ7oKHExb5e5andqi01WZF8AvqJf6OR3OdbFk2d_7ro2CkIYKFprVr8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=HGRJtwkfVAOCEag4ALcyxa3DLWC4c0V2O8wIu8YvfH3rHYp4zaxKFwZ-RU574QphW-QxAueCOYZl-lRjXhPgufBSn6U48cNdbR6Uq_ASAvPo0-A69JQsgxCzB21tTnyBh0nKvK3fQ7bYexDEMXZqOZIVLv8Mv4Y5rc9XuOtfVsHXFD3vcEKCTkqosl-zzh9QU7nVyDYcYZtzJl3JfuxgXhR5C6pZif2S9l_krWCQEFbpVdNNlNy8zwtVCwiqM8WXAUyFHa77UkRnvgAXPj9AT-BXLHMdG9gs_rEmUpxGZyFZ-h_WOSdgP_QgyRd2vW6JAC-UMel03GcAo21mw8P_Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=HGRJtwkfVAOCEag4ALcyxa3DLWC4c0V2O8wIu8YvfH3rHYp4zaxKFwZ-RU574QphW-QxAueCOYZl-lRjXhPgufBSn6U48cNdbR6Uq_ASAvPo0-A69JQsgxCzB21tTnyBh0nKvK3fQ7bYexDEMXZqOZIVLv8Mv4Y5rc9XuOtfVsHXFD3vcEKCTkqosl-zzh9QU7nVyDYcYZtzJl3JfuxgXhR5C6pZif2S9l_krWCQEFbpVdNNlNy8zwtVCwiqM8WXAUyFHa77UkRnvgAXPj9AT-BXLHMdG9gs_rEmUpxGZyFZ-h_WOSdgP_QgyRd2vW6JAC-UMel03GcAo21mw8P_Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ijSQgCBicl44v7nuuq1GFOq68OkPKRo5_umHM5XIsn9mplhHr_3vELf_7hEW8wOqHv2vI-D5_GjGDv-2fNfu_1Jt-lhlb0aGqXW_Wq-NH7KLI0p9YX_LY0ex2mlo8v9q9GPQsE8Se4t5vB_rNlt0VTxV5ek169DTW31xZwdDHRETy_uwdHqTD2pQyzKgb7S60ga8FVof0iCoZsz_JMKD6CDX69D3nMVXlG6htPpv9v7tG7vbkwZIHE7NOvZSYXQfOOjKId1AETBDuoNwKWcadKoi3UT33sNra-s0TxvNjq3OEVd5HCnv63JoBC1tp-1hPFX7_QojTOM6U1rE16Iz3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=ijSQgCBicl44v7nuuq1GFOq68OkPKRo5_umHM5XIsn9mplhHr_3vELf_7hEW8wOqHv2vI-D5_GjGDv-2fNfu_1Jt-lhlb0aGqXW_Wq-NH7KLI0p9YX_LY0ex2mlo8v9q9GPQsE8Se4t5vB_rNlt0VTxV5ek169DTW31xZwdDHRETy_uwdHqTD2pQyzKgb7S60ga8FVof0iCoZsz_JMKD6CDX69D3nMVXlG6htPpv9v7tG7vbkwZIHE7NOvZSYXQfOOjKId1AETBDuoNwKWcadKoi3UT33sNra-s0TxvNjq3OEVd5HCnv63JoBC1tp-1hPFX7_QojTOM6U1rE16Iz3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=rsT-h8jSCynQQqVuqTfTzPwDxxpxEQ2aZ_mt0nuHmCuc-cN3XjP2K5v-bBvp1qF2wi-ndWHnUMmguGuyP0_n8F2XMHiZ1vytexCd6AQ-YfGPChIqpsC9GZYU_MHqqqcgidpoJceouahCGUEOU5IXXFdS9lIJNWzueqT_YoE5TaGtGZv7asdA4p9OqgG79_OaWXvVenwwu4iOJgwsbur4YT0YXKkByZFpxT68MF9L218obdq77fMjbFiycoXZWbgzFd9PL8ZuhQpwILskFBnPUL6hB1Ft0y1nHQuHBkbBOOJEIm9YWg1aWzBEFCK4sMtPhlBk_K0DyiLAlXubQzS-TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=rsT-h8jSCynQQqVuqTfTzPwDxxpxEQ2aZ_mt0nuHmCuc-cN3XjP2K5v-bBvp1qF2wi-ndWHnUMmguGuyP0_n8F2XMHiZ1vytexCd6AQ-YfGPChIqpsC9GZYU_MHqqqcgidpoJceouahCGUEOU5IXXFdS9lIJNWzueqT_YoE5TaGtGZv7asdA4p9OqgG79_OaWXvVenwwu4iOJgwsbur4YT0YXKkByZFpxT68MF9L218obdq77fMjbFiycoXZWbgzFd9PL8ZuhQpwILskFBnPUL6hB1Ft0y1nHQuHBkbBOOJEIm9YWg1aWzBEFCK4sMtPhlBk_K0DyiLAlXubQzS-TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=pDoz7bv-AhbVAOBNtXHRw5d-y4cASXOAU4Y_qgmu0wAZ2E14UAExfSj19l9IWzTePUSrZOeJgyp3PfpukPcCClQwHiQWvJ_yRbyd-ihkCD0ceu2hC90-SOm67F6bjUe7t04Fdq2cj5hOSZBDc3x0nkfzJUzURINFu8K8ryXPSKomLh5UiHHeNgaZppjiiTnPmn0elCE2YTMZIkA-26IVyORYZSWE7qyPyQNeh1WvlzkRFydAxgOO_mJp4o0r2nbPyFZMTO3SWAtQX7piVNXx63if2bRXOdfDlVQVK8e3NradUVv4HoFv7SZKoe38O_dTzjDwb5COskppHRcKzuZeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=pDoz7bv-AhbVAOBNtXHRw5d-y4cASXOAU4Y_qgmu0wAZ2E14UAExfSj19l9IWzTePUSrZOeJgyp3PfpukPcCClQwHiQWvJ_yRbyd-ihkCD0ceu2hC90-SOm67F6bjUe7t04Fdq2cj5hOSZBDc3x0nkfzJUzURINFu8K8ryXPSKomLh5UiHHeNgaZppjiiTnPmn0elCE2YTMZIkA-26IVyORYZSWE7qyPyQNeh1WvlzkRFydAxgOO_mJp4o0r2nbPyFZMTO3SWAtQX7piVNXx63if2bRXOdfDlVQVK8e3NradUVv4HoFv7SZKoe38O_dTzjDwb5COskppHRcKzuZeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=TDCX4WC6MIaxmR7UFfe-VR3Fn20ou71KKQbJeDr2pAThcuAZqbRfeu_j8n3qhE2UFSwW9qVhvwbU8dEafY5cJIhHmo-xanoxiPtJYLUTFRwAFfHOTy_-CBcBX3TsykIsIpSHPe7ZpH9a3BKbqMmFZsUXhL5WTYK0ULfhpjDnJNLCaAiCDaEUGcOxZK8WP48XqssaFwZSks4NM-nLPtpaVlL6lSIK2-lI0J4K4l6wW-EFh1lULdZstkc79RNIgQf6MRx9vuAtaNm64ri4m4CTy0SE2SQcLxmEsC2x62R1u8gFBMAbumi7qVO1vreKUATIWjl8mjgwxqVzgzSGayWNjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=TDCX4WC6MIaxmR7UFfe-VR3Fn20ou71KKQbJeDr2pAThcuAZqbRfeu_j8n3qhE2UFSwW9qVhvwbU8dEafY5cJIhHmo-xanoxiPtJYLUTFRwAFfHOTy_-CBcBX3TsykIsIpSHPe7ZpH9a3BKbqMmFZsUXhL5WTYK0ULfhpjDnJNLCaAiCDaEUGcOxZK8WP48XqssaFwZSks4NM-nLPtpaVlL6lSIK2-lI0J4K4l6wW-EFh1lULdZstkc79RNIgQf6MRx9vuAtaNm64ri4m4CTy0SE2SQcLxmEsC2x62R1u8gFBMAbumi7qVO1vreKUATIWjl8mjgwxqVzgzSGayWNjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=DV4_eDZmXw2EXISH0simbO002p8GwdvXyhH2ORGfmPcHNOg90F8-2eoteiEJuuQgIEMbz5_sPAgzeKEAe3qNi96ku4zw4fXW8jX-fzGw_566FxPXnNr6YB9V6OCJn6jHfpcvT8WddDddRBkl3LMR5DcgYWmE1woNVq8H_Aae_oXjrIHblU632UtXQEUbmUAwmQ6ieNDUtdNGdaeNKw7goKuJIz3flqNc67fq6e6Ld59BfZr1-9tiM3HFtlkgiIQrJDItXy-DxQuMDJY0cVX4WLIMd3cufEb5F4s24Kc2586tq4cKPA31iKW6qAydGUzuje6pRqbbETqvyMuWRmLctA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=DV4_eDZmXw2EXISH0simbO002p8GwdvXyhH2ORGfmPcHNOg90F8-2eoteiEJuuQgIEMbz5_sPAgzeKEAe3qNi96ku4zw4fXW8jX-fzGw_566FxPXnNr6YB9V6OCJn6jHfpcvT8WddDddRBkl3LMR5DcgYWmE1woNVq8H_Aae_oXjrIHblU632UtXQEUbmUAwmQ6ieNDUtdNGdaeNKw7goKuJIz3flqNc67fq6e6Ld59BfZr1-9tiM3HFtlkgiIQrJDItXy-DxQuMDJY0cVX4WLIMd3cufEb5F4s24Kc2586tq4cKPA31iKW6qAydGUzuje6pRqbbETqvyMuWRmLctA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jHxap2JzmZGuUoVY03Qdw690xnqwvOGGs11dNNPoAMxFIITkawJ9gZsmqX4WK_qwaX9wpQbmhcBUOu09aJ4H57pJ_Ewt0ptbNoK6sPacGqUO8PGvZAtZ1q6goEND8-pxr_OW7wX-TAK2CoYWqoJl1VQpxsUKyj5txV1qJlstKiX2alk-fTy58oeYKGMYtRq55NHEjKpwV8HTfT-538aFN-IgWG1mHLmwBqsW9QAw2JKldT-vtgNew8VU43YEOBvy7lVXNWk5HckB5dGgNtDaIBX-YyACeypBRM5_y7lIqxfjxkQN4r2biXCsMSmG5jkZZcVpUBaVviYdsb9_85ZW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jHxap2JzmZGuUoVY03Qdw690xnqwvOGGs11dNNPoAMxFIITkawJ9gZsmqX4WK_qwaX9wpQbmhcBUOu09aJ4H57pJ_Ewt0ptbNoK6sPacGqUO8PGvZAtZ1q6goEND8-pxr_OW7wX-TAK2CoYWqoJl1VQpxsUKyj5txV1qJlstKiX2alk-fTy58oeYKGMYtRq55NHEjKpwV8HTfT-538aFN-IgWG1mHLmwBqsW9QAw2JKldT-vtgNew8VU43YEOBvy7lVXNWk5HckB5dGgNtDaIBX-YyACeypBRM5_y7lIqxfjxkQN4r2biXCsMSmG5jkZZcVpUBaVviYdsb9_85ZW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_a22pOzUxzuvcxdZAafL0c4i8CTLxxS0RCnRDaBfeezguq8Q9uX5MRgOMQEny63bt9z_nB1daR-gFrwr33jLOP504V_X1uXn7mTa1m7QMwzlNHATpsVKm_Uu2XO6rRGKsTz0iIWlP0yh3UmzlKbulhnKLvu85lhqG--XBBbEOt1O4URlN_48D4yEYxpTRQAcu4OExkE8-Ys8K_HVpTg02GsxRtX_GDN6UkUJJZfrVUJv5lFcDqJeiLr9NTRHC-g-sDJqlM7oD552YZL6XNOCRh3Ls860zdCx5t08ushZhyo_hbiXRyq3Qo8_rrx0QIqHoBwSpBRRcNk_9o4HGD0Zg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=iGdaK0j1s39G3Um-hw738fXicZl-snF2RfV4ugNtWEoyzcs4T_n7A5VFgC5okxYK0EWmLb4onZKTuYKsj4umyfhQkTlOBQAHFtCQihgSXOVmEuHbq2zufhouL5PQ5xeBI9JorTorRRBt2epN1_wjkoTMWRiZlHyrfAKt9fOQxtX4FjQoWSHOSLyRNEi64RpR2lL9AetqGXe5T6mOCrw85FHpThCbxDkAzftE8Ugz6sq4ryzxK1Lftb0a-cFZvafnoItgIjUSWPoiBumcS7VeW4msVjPxRl4dIN0-R9d52KtpoyFQL-4ndpekHH8dNWpVOVuYSepWGrG5qdqmFnYFgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=iGdaK0j1s39G3Um-hw738fXicZl-snF2RfV4ugNtWEoyzcs4T_n7A5VFgC5okxYK0EWmLb4onZKTuYKsj4umyfhQkTlOBQAHFtCQihgSXOVmEuHbq2zufhouL5PQ5xeBI9JorTorRRBt2epN1_wjkoTMWRiZlHyrfAKt9fOQxtX4FjQoWSHOSLyRNEi64RpR2lL9AetqGXe5T6mOCrw85FHpThCbxDkAzftE8Ugz6sq4ryzxK1Lftb0a-cFZvafnoItgIjUSWPoiBumcS7VeW4msVjPxRl4dIN0-R9d52KtpoyFQL-4ndpekHH8dNWpVOVuYSepWGrG5qdqmFnYFgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=sSVxts_c-1ZRcOsLCH5BCQg4GclPAYkVAe9jdphQ5QOH1tuhPnF7f7pznOpd53LCLd5RhqqQL0m_Dgff-9uNnTIpFPqesFOU3eat7YnfQ53nMrmHVI-DnNHek8zGl_uASLnAYjgXXXZjT082d8T8287IrzRsQsmEx-l-X25AEsEKv-Ku3JwLnCTsKdctQYwun5ehzfSXFL77Eue5Wt_oib3dU3oyZV6lzmLi2KEDQn1ZWY5TjdaO5VgkgZC2JVh6ioT9xSImg1iPCMRkbGLMOAN4YD6BeYS8s36AHDUqU-wsf9Jg1bRyR7VtEG9uprcaIFzGYTTKsX2d9uMFFPieew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=sSVxts_c-1ZRcOsLCH5BCQg4GclPAYkVAe9jdphQ5QOH1tuhPnF7f7pznOpd53LCLd5RhqqQL0m_Dgff-9uNnTIpFPqesFOU3eat7YnfQ53nMrmHVI-DnNHek8zGl_uASLnAYjgXXXZjT082d8T8287IrzRsQsmEx-l-X25AEsEKv-Ku3JwLnCTsKdctQYwun5ehzfSXFL77Eue5Wt_oib3dU3oyZV6lzmLi2KEDQn1ZWY5TjdaO5VgkgZC2JVh6ioT9xSImg1iPCMRkbGLMOAN4YD6BeYS8s36AHDUqU-wsf9Jg1bRyR7VtEG9uprcaIFzGYTTKsX2d9uMFFPieew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=NgFFw0rduoNupb3KX2x-xU3iVCs8Pqo44hs_A2_cQWbe0MPhhgoLN2E6N8t2C5_FGiFLISwhWUP9oH2luHyvcCdIK41TqSJyrvHJHuO39c0PX9KfbUrjBU8NLlMTHYmEe4FIlokQgTtlKtSi_QhZgFxEGeSFJgq6Y071T0pW33GJDoTGIMEl_IwNT8u_hD0ueGnb_pP5UDvEmWcNL7DH3znLSPZVN0ulfFp_lfhs5WLgwKdgG3HreO1DgGgFWdDIRoT-5k55hJ4_YLArISdYTZ8p4eYG7kZiro1MV7UoROE_TrnACqD6YPolizl0e-ozz_aqNbf9jWr3L6KjgG5oVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=NgFFw0rduoNupb3KX2x-xU3iVCs8Pqo44hs_A2_cQWbe0MPhhgoLN2E6N8t2C5_FGiFLISwhWUP9oH2luHyvcCdIK41TqSJyrvHJHuO39c0PX9KfbUrjBU8NLlMTHYmEe4FIlokQgTtlKtSi_QhZgFxEGeSFJgq6Y071T0pW33GJDoTGIMEl_IwNT8u_hD0ueGnb_pP5UDvEmWcNL7DH3znLSPZVN0ulfFp_lfhs5WLgwKdgG3HreO1DgGgFWdDIRoT-5k55hJ4_YLArISdYTZ8p4eYG7kZiro1MV7UoROE_TrnACqD6YPolizl0e-ozz_aqNbf9jWr3L6KjgG5oVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=m6M4bPqEHcXEyp86kh-5PIAXugvzhkIkcaLPoRo5Z2nQWyMEx0LxBcO0Z-7lqeW-HY60ns8w4L_6kHpCb7cPE3Z1BhnBH9TdHCxDhKEhDNymk_YvjpdvNLgWKjkjXmb_P--ivMBnWacF4nmUUla4g_CeHCKiEG8yST5zwqIllO_wVDRBcMVZvizKsvCQxZeA7atKrKE-jTObuKco66hQIyNf1ZV88FbcHvJem69reT_tQtSOXkYq0un_a6pQzGhPeFNHpAN0xFE8lt91zgK-_sk7SBVfwc_AQdM6cwrpS4QkBT5sbv-4YtnKja9QlgqdvW5cIF0VAsNK_cZE0LcBng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=m6M4bPqEHcXEyp86kh-5PIAXugvzhkIkcaLPoRo5Z2nQWyMEx0LxBcO0Z-7lqeW-HY60ns8w4L_6kHpCb7cPE3Z1BhnBH9TdHCxDhKEhDNymk_YvjpdvNLgWKjkjXmb_P--ivMBnWacF4nmUUla4g_CeHCKiEG8yST5zwqIllO_wVDRBcMVZvizKsvCQxZeA7atKrKE-jTObuKco66hQIyNf1ZV88FbcHvJem69reT_tQtSOXkYq0un_a6pQzGhPeFNHpAN0xFE8lt91zgK-_sk7SBVfwc_AQdM6cwrpS4QkBT5sbv-4YtnKja9QlgqdvW5cIF0VAsNK_cZE0LcBng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nud2d3ka8c9rCYiypyo3p2NRbYfxY6of2vF8sckIMoenMFyx1l2Rwi9_psH_cPoKR8u4IQC6oq0z1nW2VX5crRqGGZciKs-0eluEntQYsqa2izo_0BdT6tKn7GG4pmbN7hTQaFghdvRbEFo3LCl14XRZYGs539WfygtMTPa-iZohS8zoL6dHRLM3zv_7zSUSlyQb_9P5nmP3lOQ_gms_l3LsqlgrSdRIoDCmZ6Kv00leLj59yYislS3iYQaIX6R0XPw2RqdpVYFzHWIyjCXAuZpL87HOrtHY96z4tSrY20T-6ADY1U2TSeLeD4BGdTU0IMqhgzLUFrFOiXhR0qxE9Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=eS3mxOOcq5UhV90XuecsovnBiXewvpeRLsMc052OYquwjODz4fJWaVmuNcOB3NHfF9NkHB-UVKlXkbFnw-hb35OGDfUoP1fyXGyXb0gOEXpJIXbetrKsNwaedDmMeaT656bBFE--DKU5aiKs-lar5n_nT_P6_1gLptyIX_OZV7luaruB9yjtg1MNREZ92pUub_ey0hSNwIyJkC-W8ZmolgdgBap_gMZsg-R6ad45tcLiVLkLs0-cQIm2HpOkZAkabhr66Px3zMmC6RxLANMQdaRkoXb4UOx61jHdie6UZwEfQRL3pJbGmQE4iufRw6Qu0tIPqYCFW2B1r3tR-RC71Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=eS3mxOOcq5UhV90XuecsovnBiXewvpeRLsMc052OYquwjODz4fJWaVmuNcOB3NHfF9NkHB-UVKlXkbFnw-hb35OGDfUoP1fyXGyXb0gOEXpJIXbetrKsNwaedDmMeaT656bBFE--DKU5aiKs-lar5n_nT_P6_1gLptyIX_OZV7luaruB9yjtg1MNREZ92pUub_ey0hSNwIyJkC-W8ZmolgdgBap_gMZsg-R6ad45tcLiVLkLs0-cQIm2HpOkZAkabhr66Px3zMmC6RxLANMQdaRkoXb4UOx61jHdie6UZwEfQRL3pJbGmQE4iufRw6Qu0tIPqYCFW2B1r3tR-RC71Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=foGs7m17-9xu8a25wxnPoFR4ba_yLSnezZbsT7XosL-qcU5y93BvQUXeRlzhPNQMis1YUQ12WX9mJX8x3my8nliDqdIohNNFsOHG32YVKQ6kuRp-5eumBxBb1399UL_tQ6I_CLbqdLq1bV0vsGDqXxm8a_yIQkDZa3mJ_Go290TyOJ2g0jn0dWvz6DdNKa7QEKCO2UwIIWPGxfWExMlEDb7N6R9rrZuiKKXWRuYoOtPCfq_nqSZ9NtmiZZktgSoW-HbGibs0rvW23-ZjKRsaWbFhsFbAimiIAilGAtuP5L9zaw-wTZuQUwMp1gd-JyeVzYyTyRDUsb0cPppflCYLKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=foGs7m17-9xu8a25wxnPoFR4ba_yLSnezZbsT7XosL-qcU5y93BvQUXeRlzhPNQMis1YUQ12WX9mJX8x3my8nliDqdIohNNFsOHG32YVKQ6kuRp-5eumBxBb1399UL_tQ6I_CLbqdLq1bV0vsGDqXxm8a_yIQkDZa3mJ_Go290TyOJ2g0jn0dWvz6DdNKa7QEKCO2UwIIWPGxfWExMlEDb7N6R9rrZuiKKXWRuYoOtPCfq_nqSZ9NtmiZZktgSoW-HbGibs0rvW23-ZjKRsaWbFhsFbAimiIAilGAtuP5L9zaw-wTZuQUwMp1gd-JyeVzYyTyRDUsb0cPppflCYLKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S9-J-HJnS6AWrpRSbd1_Uu3xT_Y7L5BhX-z7vNN6CaSR8yPz7FJfJ0NkQbk1nJrABxKuhmFjpYjGzDYe1dHRBjw2zDFKpuOIBTWJUw9wJUMG3R1vqMRPkrqc5PXvHPAJn7MfxkomBvbwjINx4oji5iuQPS2_01t2xPFg5K1BImPJnmb9RqyMzBIbNRBzf68G7gXZJwzbCO3s99QD6K03kSZGxMRla7rNJnsJ3LFas6zAZYHjg_7iRsKX0-nwgo6iZhXZfLGUZd0vgnB7eKwxWSLq20S_j3TWKqbrw4wiaFmj3EGJljpKg1TzxDdai_Jf6UnTYfUixczzzmGrWItxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQho4Z-ZD5l5tpncwbzSsMoj2RdYZnvsPYJG7vnoCegpTeeJ-G2f3yCy2ffTCDTGeVWgS8IU7IXdmNdGbtr2dvoK_4XsQjbNw8nAhjQVzqQhP3Pgfq0d3AdsJLbNymnnHZK2d01cSK31Cy0EQoUCsSlzdKgLkMPCOWL_u4kESY5iGqUZTi5L48LeAbCQFNW7I1os0p97nweXStYjFA98kOWgrrwC2orgqxszUdc6kBmw10SMn5haKEgXWPVnn43ox7idUHZ7P9CrPIIpjfp1rVrvK_NzW06bovHIgpw5Eo5Wn_utiAepMNhHgIplbSK6q5F2DGzSHwl0eYx__0WvAA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=V7w26KhLBEoPeBQRlz2yOrTAeecuUa96Jsq7lr4cF9M3KiSTpdwcGujy5e85S77Vwn-OQsls-kSDskFfbl1MhNFEewNpxL_pJ-4Ym8VRfRIEONbT5k2aSKyQfmvJjPeYkVOQs_AcvRkJ2jU2WHwl5Nm_EqDa42nGlPZObgf_vkPbuO29ZlLo6wwgAggriLsD4agV-WzHW9LGpzyqnC_S0oVxduFq_9-Y9wxQRdMAoKncH_6XtwxJiqNZWFMTmnFkW8GPXV_GOOzUwV7RGCic7ucSh9MjeZ23hDdIKw2qXJChcCRss3Hm6FL5mJpjuALhF6DZQvTgXfNYjX5sMfGfUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=V7w26KhLBEoPeBQRlz2yOrTAeecuUa96Jsq7lr4cF9M3KiSTpdwcGujy5e85S77Vwn-OQsls-kSDskFfbl1MhNFEewNpxL_pJ-4Ym8VRfRIEONbT5k2aSKyQfmvJjPeYkVOQs_AcvRkJ2jU2WHwl5Nm_EqDa42nGlPZObgf_vkPbuO29ZlLo6wwgAggriLsD4agV-WzHW9LGpzyqnC_S0oVxduFq_9-Y9wxQRdMAoKncH_6XtwxJiqNZWFMTmnFkW8GPXV_GOOzUwV7RGCic7ucSh9MjeZ23hDdIKw2qXJChcCRss3Hm6FL5mJpjuALhF6DZQvTgXfNYjX5sMfGfUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
