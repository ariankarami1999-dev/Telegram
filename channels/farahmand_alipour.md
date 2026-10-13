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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 22:53:43</div>
<hr>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=EJcYm06O3RU-gGvVB2GOBeLcq-4XUgvPC_izq7UmcK5LChWuaZS7aQs3pIx7KUSNRIEPCoQU6ZPO3rnJNW5ZydJTjw8-obWPBD6xHE842oiZ21NthuFmOsTIDs0sJr56x0lDp1wJfbqRVJ31O78JostGrRKokL0r72duWJrNfBCT6u7bsbKQKSztf7yQMagQhn26ZrlXKhhyzLkDogA98wt3yXaTy3FNpQcxWlfGvwLt7vntWzsTYyLeT_pB4FqtUXza59o5ycBMV7f1KhST2LhNxW67OtTLx08GH2uoG2ZcwG4A_qZ6UxQ0KpCq0r-0QeFGexVTM1bJcvBr-UDhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=EJcYm06O3RU-gGvVB2GOBeLcq-4XUgvPC_izq7UmcK5LChWuaZS7aQs3pIx7KUSNRIEPCoQU6ZPO3rnJNW5ZydJTjw8-obWPBD6xHE842oiZ21NthuFmOsTIDs0sJr56x0lDp1wJfbqRVJ31O78JostGrRKokL0r72duWJrNfBCT6u7bsbKQKSztf7yQMagQhn26ZrlXKhhyzLkDogA98wt3yXaTy3FNpQcxWlfGvwLt7vntWzsTYyLeT_pB4FqtUXza59o5ycBMV7f1KhST2LhNxW67OtTLx08GH2uoG2ZcwG4A_qZ6UxQ0KpCq0r-0QeFGexVTM1bJcvBr-UDhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9CkvVaVmzpIvxMcsldzN85wp9cchB41V0pCS6D8yN7VVFB57jCL2CLRaZ-wPYLUqq7kOYq1Wt7j4ykPeG0P0SYzhtsPwXjZ0hiDDSlXDIpYW7EPjeo4AzzHKH62X_lT24ubinWBzn_KNSy2Nz5xGZJfr9AjIoiBDWia1fi3yMh_yBRl_PRXq112cZbVxiBI4PTI75lSQ8BLQd6PxCgWVXNXymZlKZXNB5IMpf4l9k3wlwxFWOi409MZQtuixXCeMNHz-575EDR5QLWwCADR3r-Y-wgM2SqlaRSpa-9CG2jRss_P7k4obMIELciHnKsheJjNzfYuXTmelrUXI193Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjttljYjeM-1CKkWnTeHaeEFfJ7Q26e7x1pUHTHhC-zMb6OfAH2kLkahxpFMj4_KVE37c8lZU9qwbSqVDRJEVXvmsoiSDdohVMCvkRvIKwvjY0iz5SbdCKPWCHM68vQcRHQJnwlNDFpMZJf0l17MvsZKSBft8-dsF2W6-3Bwyi5u7dJcE4NQAbYtBVZIMU_TO90dDZmYuF0BA8Jd4XohFBCT6Umg-el0QzR7A5gD_Wm3fgThtJJwsBwX_Ny_5ai4vWNRyBQiDnytCFXnFcFYgOsKtcE9T0EY4LFH1xcWkG2MwOoPb5gpfb8tE2aCncUHZW7WzXDScgsm-Fupqyduhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PugdJJ7MtoGP9TqetHkIJklPUWG7oxaYWnxIzH-LJLsr_ivFfQHNL6soRgGWDF6Y-EXMMV6ms8vM_eHYIjBu3EjX4qgu_FOYJb0Zxv5bG3UsLFsL7lGlEk1845k6Rs0EakacZfR5eY8V30d5b7RETgmnrfkO-8yF-gP5wsRK-F2mm-Xe-1m761PPIGw8TBvKyOr4iUBzy9rswikdGLRNeEcu2Qr1-TncHMXiJpLvT2C7ufF3s0cgq90ATpDNi5fnF7zjo6FNieIs41KfvRHEuPBPKE8Jbwt55uqWklIhBHzTbZrJ28geWhPG9d6fZJcGUfFDfCPUdhtOkw-w-rkYkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-at5ygl8kDaHve3MbThxomMqxHAg34XL-VJ1TjLgGjcmSkn4WuGcWcjTh053Yj2dwGrqc5Bfp5E5YrUzF9_HOIU4Od3GbM7P1T8fv5q_WLwijE6x0ENcRlL-U3XxJR9SNApsHkc5gkXP5WtChv2jose5kufGzpkxD1xHWkvFyjnYCKDGxq_oa4IzAKvj3EnDI5_mrhaschHC7ipjueh2c8xxSXSggLpJ42RsfYYAh1V1gwrcXzc1Mi6eViLyYx-FA2yb_paHAEsrVDXf4kAe5W6ZQI5bvl8T4KVyV_dwPqBna7XZmMB8YmnByYFo3xlZgOuEGgS9tNkQdVCAUw-pw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmE9SiMauF2AXzTTHwmM-eVQ1_u7Yu4Cn8lyvJD8-IvlodcICMaQht_CQ0a_TQTTCuoZ0HwyS80RrIXsphq6S8JVx76RS8SJ9L5xrP7pk0W8NBXbie7pL4lxUmuPKiGmFhlJ8ktBitsQ4TxvEkfWkouFtbocAji67Up8SBKZlSVzo558Vag-kIWM2ddIFeV5bnXC-yUO2pb0M_NBJqsjKnFZrDL-3KN0wGnNpj_Uef5idCwqQXqp1SMuzMA8MzFPsOpkY2-xbYHm4ACHUgFTds20is_bBZuat7TICz9zgNZqRBcB5qXN8ch9kgzmgTzIV2Q7ds5tNz6cxHSkEQQS2A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=HczAvgIhCeolMwI8Xlv2V9EWX0jg00Nr9jZJpLamLes0LMGy6z8hQzwyfvpoqYAnzgvS1sxU7GYR_xDla-7ZNrEIH8sGSx-drsvnxgq9DXdwsaksf7_eIIS-jOlCT0DeC0cWo3Oag-Tev6h60u6c0Q57FMUwGWdvNeaKPbUqcmiKp3qqlejSfdkBhmVsEGWphQR7VfoB4XN7uaJlBCIGkj-R1i2Xvl4oj3O_ijzVjsmfq6bm3CdfOIVZthsTxZfZ1Ou56a0KPR8Bkejpid8YZO3qZbLb2OfCVckkV1EJSwfUrIYzklqiderzw6_BWxYCnKEOYkWkeMZYBPCbXT7kbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=HczAvgIhCeolMwI8Xlv2V9EWX0jg00Nr9jZJpLamLes0LMGy6z8hQzwyfvpoqYAnzgvS1sxU7GYR_xDla-7ZNrEIH8sGSx-drsvnxgq9DXdwsaksf7_eIIS-jOlCT0DeC0cWo3Oag-Tev6h60u6c0Q57FMUwGWdvNeaKPbUqcmiKp3qqlejSfdkBhmVsEGWphQR7VfoB4XN7uaJlBCIGkj-R1i2Xvl4oj3O_ijzVjsmfq6bm3CdfOIVZthsTxZfZ1Ou56a0KPR8Bkejpid8YZO3qZbLb2OfCVckkV1EJSwfUrIYzklqiderzw6_BWxYCnKEOYkWkeMZYBPCbXT7kbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Ahwst7zJqTvD3BnCoMc7nd4KmKvVNwwYxYlJqWO1KuMANiFmOvFqpxdgDZ0d3KJAcy1A4UTWdtgjrnfRygj80DqZ1Jbi1eBFDWKkqqX9-DOH-UY9lZVWIfKwlZOceKYFkShsUvZ8ZvbQQBgd6kAovFNQN2lcXN_W02PNxHwanb0z8SOMU7IS_hjpWBYZBSjxPHyfPcq3s5_d_cef7S2gWJSeZdhRtTOOCyUTd4lHGJUJqOHetNDAp2EmgVTHiP4KTfKV5EFgPwN6y1YPVZC2vWYLZv2sEWXGXHDcXnUBf0LN8YQLoc8EegnQ7CBZ0itW9wB3ikJVmWDCwlpUdTRczDGKrzQj7z6bb10hbWg4mObVnchMIdG0XphfttTjJMgQVlX2OnHfeyV3TT1eQwqr6h4wtl9olXjEWpmH5zYSDPmp6ny66DD5juZFBD9oAPtnUtIGkTFn6B8ztqVGIbmEec2XhjZqkCRWCNynI-9REcMAIzn7T-9fDcz5t1gNraQEtcpsTtRs1ZG6jSaBjP8ks-WEVpkbcqEDJagU3DD6W3z4MslBW0ls3MEDky5KpxDhJ7y66rPS9abVyjlN-lGh9H20a2-k0iVoMqy4bap-D615SE3W4gwm3ZN-nDpyD1FZU2l8qml8mViwQ_hEc93Jvi7dwXUJplSiO0MUbtWhF34" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Ahwst7zJqTvD3BnCoMc7nd4KmKvVNwwYxYlJqWO1KuMANiFmOvFqpxdgDZ0d3KJAcy1A4UTWdtgjrnfRygj80DqZ1Jbi1eBFDWKkqqX9-DOH-UY9lZVWIfKwlZOceKYFkShsUvZ8ZvbQQBgd6kAovFNQN2lcXN_W02PNxHwanb0z8SOMU7IS_hjpWBYZBSjxPHyfPcq3s5_d_cef7S2gWJSeZdhRtTOOCyUTd4lHGJUJqOHetNDAp2EmgVTHiP4KTfKV5EFgPwN6y1YPVZC2vWYLZv2sEWXGXHDcXnUBf0LN8YQLoc8EegnQ7CBZ0itW9wB3ikJVmWDCwlpUdTRczDGKrzQj7z6bb10hbWg4mObVnchMIdG0XphfttTjJMgQVlX2OnHfeyV3TT1eQwqr6h4wtl9olXjEWpmH5zYSDPmp6ny66DD5juZFBD9oAPtnUtIGkTFn6B8ztqVGIbmEec2XhjZqkCRWCNynI-9REcMAIzn7T-9fDcz5t1gNraQEtcpsTtRs1ZG6jSaBjP8ks-WEVpkbcqEDJagU3DD6W3z4MslBW0ls3MEDky5KpxDhJ7y66rPS9abVyjlN-lGh9H20a2-k0iVoMqy4bap-D615SE3W4gwm3ZN-nDpyD1FZU2l8qml8mViwQ_hEc93Jvi7dwXUJplSiO0MUbtWhF34" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9JwyP2YQcHeVMwKq09SbWsb24sHyH_eMehVilGo1VII2NAAMUxvoufgSCRNHb4HkhegmhdRzmtUXAR2KpxW6aR0pDZRTJ0lLFqEwOze7DmV7tsZewRDVSyKKYN2zCIOSLukobF6s5dnEK-px8EKnRMIY9nRTabKMAedIuRStHBDYVWDfpv9cyNltKDZvSLSlcBz9SPuDeq2nlqUNRVmAUIveZDd2_aoByryAogLgXeAnqkrC13mNB1NVTz3kfsQ43mB71uwQlqUYwx7HsnxUn8b1KPyOnDPfoBaWwA88SyrgK-Jca_NR7Oz1h2exkzSrmcbB-uWl9NBYTOIw3KK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ANvE8F-mwQlc86uXzL4FkKa6899_K-dMUmWQ3CpQzR4WjfwWZfHrhIjQ9QCcOgNWWYBfPEuZlGK_731xNkHMecsbYSOjWLHNt8XxVHq_GhVlNkIHPPNghGgT69BNydLhxbaqALw-syBhw58bFI0ZZIAJauFDEreaxBl8GEf-sgl9cnyf4CBFnSY3ctT8lbjKNVQUzuicPWN5QZKr4T3ERqdKR-ewXPQu0q5OeyxzwrkpX1dJaGWeEorwmQwIPR9jIeEg5-tltWaqXucJcfXiKf_43UQ2TQtxwd7ag6dykzO4xaL9Zbxb-ROIwgvWePjNsTrruay7rJWXVGZP18NQ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9wbZGDxx4jMD9Pg9C-G_UHAYSx4ohPbxV8oqg_oO0hUFftUa97FQIzIrROewWyHBOd3hik29Eq6nhPobnVCdh9BkbNsOGV2-04Kj3cdgk7MGyPYbUkDr-xsQD-9YEIiQon7A6bZ_YTFwdzLsMNFne2k4Zq1Id4obSbFYv9ngMeM-Oy34sL3LFaCoZyrJCNESV1dUre0gqWeu9smg7cO5ywq-r2skUONga30Wc8FC3e0s9bmo33RbtPgmZoIYb1dpp53mL05udbGQZWHVvhb6kJWNvy_4lNb7pzBcqcUcH-U0bh0ofGna5GedQqswuwiUKTF2BI12riiJ5XNskpFsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=kE221qDgcyf7BAfnZgncR3JC3G3S22fue8AC6Wv_IApohMTmaXZSGAH8nZg6oB5zALJrRD0j0bHiQ7Iba9M9vbAKTz6KZyd-HiTTh82eq00ePzJpm-t2arv3wCS6KIWQubiPZuFLVotbw4SubiL-oiqNeJqxgfAQj5wjGkkbeaiDLoAmt6_HxEP7kpzeinvmDJhFksfcH-K6bCpKlb58VQ-Dc2mWfI55KP4HtFZXCEqKJdjEow3AsooH1rpTEkSkX4-W48eY2aNG3y7gBtTTfeK_EJ6z0tRpxhhdooQ3rCRU3lTBOb3Cf4loIBtbp9G5ZwUtfrEG1iOsCsMd62hMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=kE221qDgcyf7BAfnZgncR3JC3G3S22fue8AC6Wv_IApohMTmaXZSGAH8nZg6oB5zALJrRD0j0bHiQ7Iba9M9vbAKTz6KZyd-HiTTh82eq00ePzJpm-t2arv3wCS6KIWQubiPZuFLVotbw4SubiL-oiqNeJqxgfAQj5wjGkkbeaiDLoAmt6_HxEP7kpzeinvmDJhFksfcH-K6bCpKlb58VQ-Dc2mWfI55KP4HtFZXCEqKJdjEow3AsooH1rpTEkSkX4-W48eY2aNG3y7gBtTTfeK_EJ6z0tRpxhhdooQ3rCRU3lTBOb3Cf4loIBtbp9G5ZwUtfrEG1iOsCsMd62hMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=RDdiBnynKLxTZhfbDHWmMEm6Slq7cy90vYy_UoBjBG747jWmr5mjrX0r5_yn098gKng67iMh4CwDw0ZjTlikQvIWjh2ZVV8yEsURVYj7w4CIpMZU5HYUMOtWEcZECFMGx3sO30xwPlmP520YtK6pPE6NBtkq3MrAcBPc06xiAXRu6FXWCsODmA3g1NczWTeHMzQ-HRuX3ueawD1laQ3pVLffrgusBhJULCsULr_6_ZJUHtu60qLoIiGr7AMp-wrE3C8pqAzC25TdU5xmC8DWh8L0sJ8k_rGJ5N_Bd1nWKa1S5_PmVeFzjSRR7trfzYEWzQjmhkvZgyOFbaJJKgg0VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=RDdiBnynKLxTZhfbDHWmMEm6Slq7cy90vYy_UoBjBG747jWmr5mjrX0r5_yn098gKng67iMh4CwDw0ZjTlikQvIWjh2ZVV8yEsURVYj7w4CIpMZU5HYUMOtWEcZECFMGx3sO30xwPlmP520YtK6pPE6NBtkq3MrAcBPc06xiAXRu6FXWCsODmA3g1NczWTeHMzQ-HRuX3ueawD1laQ3pVLffrgusBhJULCsULr_6_ZJUHtu60qLoIiGr7AMp-wrE3C8pqAzC25TdU5xmC8DWh8L0sJ8k_rGJ5N_Bd1nWKa1S5_PmVeFzjSRR7trfzYEWzQjmhkvZgyOFbaJJKgg0VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZg-BhzErGIOKD4xU5uPaH07aeT6y1Hsz3J_w_16gYn2rMqYWQNarGZ4XNdGwbtHnpcqHopkAap7W8KZ0lKgWf5U2ErB9vk9kyyN1g1kk6rT8lEQp-7bAyXbOD6Sgwe05X8v-PQqx8lbAxr8wdFDdjTSb8Kacs2ULTEHZvEVPIy6tyuZ5DdQTjoIOiUp-D_SL5wBBLUcwte2uGJcP8Wb7vWOUgbTjMFQ-5xoIvkB9jHG3cc4oY5Xk3GrhnjgSh1uBtRdic04SfAG_NcJdhAyR-u6mqSvFPthwqP653nEcvpGpWKOLEFz4ksSyyg3Zb5VSBuYcWnsj___5kqBfBywsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=sBcHYXoDpj2CcOA4OpL99atzyyrZzWS84qd2BbaZ2CR3N5fgGH6XqFzO6b-8fGzjTRNtejanZcOfjZEWXvSHJCwIddSqI3f1jims80a-AcZcCL42jKd3js3X3_IKYHYAdxRi57PDl_FFbTtioFjdNI2aOI1KhasGYHdJ935VgXuqWrnmZZOPAKLs-qFq-M2HQTEKJ5yMhLeNssLP3s4vw56hTRXfytVVLmZ9ZFJfT0_zPa_cl_ZmdHNVoU-iGX0atWnbDTn--6_DpYN69yFTAEJbXABmjqCYiFc4IQgmMP1mJOhEqZbaybQeNOqATbJ27PB-gxyFLMWpCJ25W06O6rqobBvIRcMy8oJvaJvwt58_k-zbPYPetOghKCT8v-QUHnvKRm0hmgVUjFDiC7dh0yf8ogMB1n_wkkW_MBS7TcaAi_zNhxn_5UGL2H65-cJfLYsOxC3IMI_CUq82i7aUoRAzl8TC4C4HT_uKfTDNVmX54pAeSKkcT0Tv4B-tGltXYHsVU7G3vMz6iicTHKBKj8FxLqdagxxqdDwdnKaQYIaBkW5VPQiNnZrrBleptCOpy0s_ahBRwh04zVObx60GjkJ246AoUqLV4n8dDBlPP3Pg9L0YkqLLziKTetCbh9sZM_uhqA9_FYlcf_FvNkkzi4xTto3C4oHB88TvLqgCf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=sBcHYXoDpj2CcOA4OpL99atzyyrZzWS84qd2BbaZ2CR3N5fgGH6XqFzO6b-8fGzjTRNtejanZcOfjZEWXvSHJCwIddSqI3f1jims80a-AcZcCL42jKd3js3X3_IKYHYAdxRi57PDl_FFbTtioFjdNI2aOI1KhasGYHdJ935VgXuqWrnmZZOPAKLs-qFq-M2HQTEKJ5yMhLeNssLP3s4vw56hTRXfytVVLmZ9ZFJfT0_zPa_cl_ZmdHNVoU-iGX0atWnbDTn--6_DpYN69yFTAEJbXABmjqCYiFc4IQgmMP1mJOhEqZbaybQeNOqATbJ27PB-gxyFLMWpCJ25W06O6rqobBvIRcMy8oJvaJvwt58_k-zbPYPetOghKCT8v-QUHnvKRm0hmgVUjFDiC7dh0yf8ogMB1n_wkkW_MBS7TcaAi_zNhxn_5UGL2H65-cJfLYsOxC3IMI_CUq82i7aUoRAzl8TC4C4HT_uKfTDNVmX54pAeSKkcT0Tv4B-tGltXYHsVU7G3vMz6iicTHKBKj8FxLqdagxxqdDwdnKaQYIaBkW5VPQiNnZrrBleptCOpy0s_ahBRwh04zVObx60GjkJ246AoUqLV4n8dDBlPP3Pg9L0YkqLLziKTetCbh9sZM_uhqA9_FYlcf_FvNkkzi4xTto3C4oHB88TvLqgCf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=BTE1SHtG3zuaGrN1xBhMpvyBFCnT6a4D8Wwupu6KT--5ZEUdWGEGAMyAlUit_uDgZHRTIdPAxBbP-IZ2x6-2Pw0Odlt2zmL0XlJABG43tmcIU6mSF_lgKGOjuY9gra8wUm8ZJ0rBb4vaWbGzqHND4nUjrajMx_rvBMFDw7FsH3iir4LdAHnhICW-VwCjFswE_r0eSL9lV3g3UU1QQWhQen1dNdOHjR3waEeuCY-dWgHo09EAZrvu9hZgeiT-26-_JmXvYSjpoG0ZHk1nw4_GdCzGV6ARodjMpkbbkitQFHx1EBuT4IniBJuG4Uxyly-hL-HM35q4ECEDC90E5NuPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=BTE1SHtG3zuaGrN1xBhMpvyBFCnT6a4D8Wwupu6KT--5ZEUdWGEGAMyAlUit_uDgZHRTIdPAxBbP-IZ2x6-2Pw0Odlt2zmL0XlJABG43tmcIU6mSF_lgKGOjuY9gra8wUm8ZJ0rBb4vaWbGzqHND4nUjrajMx_rvBMFDw7FsH3iir4LdAHnhICW-VwCjFswE_r0eSL9lV3g3UU1QQWhQen1dNdOHjR3waEeuCY-dWgHo09EAZrvu9hZgeiT-26-_JmXvYSjpoG0ZHk1nw4_GdCzGV6ARodjMpkbbkitQFHx1EBuT4IniBJuG4Uxyly-hL-HM35q4ECEDC90E5NuPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eT0pUv6etjAjQZQ640LjlFFKOIGnT5JpWdGisluKcmTMwoxovlYMT2SXhE-qEM4A6bSCznV9Z9V3CfzdqdiD7w71IaQx_rbtraVNr_1ISpWYsys14wSn4FPyXi-88BjXC21kusMTZc-iIHgIM0zlOg6ExJOPxyXyRn10mo_w3gEtniIND0s3Amao2PUhACGNBWKYN-jKoohaKP0vEzJwcPstLqvHKs5LG-Gfr6YGwWMk6KpwrThcpovPrAZmuEFmD70e54Zvr3DyDwAaUD6z4NazrwB9tkiBwD6IJc-GSgFm3ODzPEPFcXLVvTAsFXWEpAQUDHU0UnRDkSt0Vt4W5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=UA7M0DUuqrIbPSjtbz6SRIPz6uqoEEqsIrJae2W_iZ7uI62T4zcpjAxfTljmTwkUxvy4TI99HyT_ggWFp1H2q_N2LcYEofLzYDkD2_XeGWVjK0OQRw8hpAALOfXT_CN9LAbepXFVCRRSo0DjfKQfIKUPXvxgQ7BCH2v8osDejk5wbyH3nKLG1Qg89qf4ZPH2WRTg-ignk5rUbglU2jcYAI0FWygU2NUFtKzLacSEblCdvT_q_IVBAGV61A3XdLwCwEBwdlC-zA7FQo-tsmiUi7T_ryJ-IjkrdTyomfQhBh0JuaRS_gIKDcCbvQrb_48jR3TFby7CJHpMLrhp-CFigw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=UA7M0DUuqrIbPSjtbz6SRIPz6uqoEEqsIrJae2W_iZ7uI62T4zcpjAxfTljmTwkUxvy4TI99HyT_ggWFp1H2q_N2LcYEofLzYDkD2_XeGWVjK0OQRw8hpAALOfXT_CN9LAbepXFVCRRSo0DjfKQfIKUPXvxgQ7BCH2v8osDejk5wbyH3nKLG1Qg89qf4ZPH2WRTg-ignk5rUbglU2jcYAI0FWygU2NUFtKzLacSEblCdvT_q_IVBAGV61A3XdLwCwEBwdlC-zA7FQo-tsmiUi7T_ryJ-IjkrdTyomfQhBh0JuaRS_gIKDcCbvQrb_48jR3TFby7CJHpMLrhp-CFigw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFBb8rXZKMGGXm-EEjqCjxOjVFWgcOsKW1TroK9vqmYdKHO6Dcsf2gCnhs2zL6yt2R7AW-gNEsJquwYVuUfYL3L-Jp2bLOLvdjIQOeZ3JoxMxLhxWFHBqPH-a7luWcMZgvd2drIcJ0i_pPfLRndhxjhnML9UaN9FMB1Yo9VvbHwTL3xwKMGDbB3un4-wPoTT44I9xlFpYsDjocQjyqvoWSfbL2FfTNMHcT7YI6VtIkANvFboUj-kHd_h77VLGWjRVwqIgtrpg5C1j4tDXN6Rll0O6iGpa7Pxu8HHb3ENm4AjbBA7nlX1J8ijhpByXl-lDsoIErFca9dalzqeCczPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFRUqPiozkStOZJgNvX4xg_jECoWrN6d4DnxC55EQYaJMBom109GZcKyXdEW8Yqp5j5w8xYFX8ULXwm8JCZDg1bmcFbAhTYmVS0vZfpzZ-NZvhqINEQUJsdwaDfUrAr2ZJqZCdhZ8pr3wK9mRHNeavoURcyKNQ2gtNK2hs1dI980NsGNjLg99KaGG-MbFINJaj09dsJiB7lRxIOTWKZ9Cc5omxEOgetbAgbgarNlZEsqezT5UEBnoWpRhaKcKiyWrLzcqZCitU4Tqi8MfAeJThan9SrN1rS7wHLXgkbTSLWWjwVDg_pI6B6SdNPeJm1_Q2UAmZ4pDYWJFMQer8FndA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=BoIsekUKXJLkI85a_1IJLKG1-ai2z7gWLE5qu5tbhrbdrdipGNMWQmV0yOq2eClAvQ59h-LsckN-Qe5ThNlPsIrtf5neovDZ-q8t45hYB55jOjRIxtRdNQp85K2z7kawCCz6E1_gTtnt9pSzUnPcP7q73UtwgGwI2mgUMdutI6OHf8LmTmHE1CJZRXDDtAcrsAAqIFFHVDPzI83lPWnxqCwXQHPyBP2DtCP74avZiizO8NY7R7WoGL6FpduZknJXZPCNzR6Tg-oylSoam9Wo94SGm57t0Dr5-hYJcK2u3a6Acpl26eONqntJkYIlIxn1RJOLcX6pS6pfJ2wmnS9BO2YlbOpnWgZoRXbMW2gg87P3is8XJSHzsgUwa9n8RIA8DS_G7iC8kAPf-e2Xdy9rH8nsH5Ocv-zt6Ww2-cCgz1e17GKbIgKK3aAGtiFTQoX5e1IC1W4LBJtoYxqMnzqrpUc2I0WQj-rfSHuUWFtFszOWZpn9lBUITEU1gLijO7LJbM_32BHOBWWNe2HXGZovB_4Cxy_bJNPU6Fqoyb9qwYooMy6jgWHZ8stSqSGPb5xov49PDGTBsk7fDgQp_OpA14OdIOvGRwimDDY-EO-6qtivEvXaINVCxKhhLmkVfa6NWVwUtSZqJ7bex-rxzKHeEiX5VbLsQNyDydswJRdR5pU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=BoIsekUKXJLkI85a_1IJLKG1-ai2z7gWLE5qu5tbhrbdrdipGNMWQmV0yOq2eClAvQ59h-LsckN-Qe5ThNlPsIrtf5neovDZ-q8t45hYB55jOjRIxtRdNQp85K2z7kawCCz6E1_gTtnt9pSzUnPcP7q73UtwgGwI2mgUMdutI6OHf8LmTmHE1CJZRXDDtAcrsAAqIFFHVDPzI83lPWnxqCwXQHPyBP2DtCP74avZiizO8NY7R7WoGL6FpduZknJXZPCNzR6Tg-oylSoam9Wo94SGm57t0Dr5-hYJcK2u3a6Acpl26eONqntJkYIlIxn1RJOLcX6pS6pfJ2wmnS9BO2YlbOpnWgZoRXbMW2gg87P3is8XJSHzsgUwa9n8RIA8DS_G7iC8kAPf-e2Xdy9rH8nsH5Ocv-zt6Ww2-cCgz1e17GKbIgKK3aAGtiFTQoX5e1IC1W4LBJtoYxqMnzqrpUc2I0WQj-rfSHuUWFtFszOWZpn9lBUITEU1gLijO7LJbM_32BHOBWWNe2HXGZovB_4Cxy_bJNPU6Fqoyb9qwYooMy6jgWHZ8stSqSGPb5xov49PDGTBsk7fDgQp_OpA14OdIOvGRwimDDY-EO-6qtivEvXaINVCxKhhLmkVfa6NWVwUtSZqJ7bex-rxzKHeEiX5VbLsQNyDydswJRdR5pU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8xPmNHKt-4S0lyGgRHzgOy6jmV_uVRPQOgTCRNbKoVHL_A1vaetxqBAHaqV-0-fdINOqS2BVD2MUTI1cmKBFCF62lqJqaL1FYSVYgqTSP-JXOKHFguCLr2ln9vCSme3f4Gf_EZ3iAzT9Q89dH2ELnRDCMqPbDuf8X0mePzNUgpxkbQLZuuWOH_cH_akQ9hXr0e_s-iynhv0yYjZUCYYS47irLF3nbJZxCCrUdYOxXi8p_LmpMgKjiu5t0UYt8cT8Pf-qRTBPCU3mxSpH3Cs-EuHu1MTtvGlQ1xFx93ugQ5Pfi2rM4M7gESyADJApLEJosEMAfQYNzLonbemncRG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKTi8dFXGNOlCXHPv6YjTAfIv7skHUzvMxFSx0cP83m8Cm6adcu9K5gT9rPdYL9QfydYCoX11P5zKJZste25-TXUjVG4wsjRBZbNyzD5SGLoHcKHd7u5vV-Ls6TTvvdytnO9MFm-Or29jI31905qw7euBcX0Hzlgr_xW8f9KAMxPOZE18AGq8EBYRIUxSzI3GgGojcVpHdAbG_gfDqJNBCYgq1UkgENini4oGkB8KFEgk4isPQXGdcWOxnto980vnBz6bfUg14kkS9SB47YR_6cpLtiPOr3pDfYMk5DVve9U_o0ZViMqMZ1op72JA5zi4_4wpfsnkNFW0FjhYDxrKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=lxl6sgF2CZfIro1dARTr-KBz2jgBrkcDvij7-qC3tHQc4Cdvy64TbdErKpdqD12uPzLX2oT9Kh2Jrf24TtfOKT8ar2NLSR9MpgfK0jcecYOalVYw9CenhMO39t2zvBMLC6XV-KtDwngforMMq1tLW2avjPUubf3-uMjNzNI_jkle_mGMfAJ9hx-59ddOHNiRjPhNiCaEPzuM3sZkfpHuSfaHMDSP-eAdflpFtrk3VpleVcuZhAfK5x6IBU_S-6Swp0kAQfmPUNSPQuL6Y9rGvMveHH_NbfZu-05jZ7clN33ke38XAx-0ZchYWccAvKhpANc_kkiZbe3aff3gJ7PX4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=lxl6sgF2CZfIro1dARTr-KBz2jgBrkcDvij7-qC3tHQc4Cdvy64TbdErKpdqD12uPzLX2oT9Kh2Jrf24TtfOKT8ar2NLSR9MpgfK0jcecYOalVYw9CenhMO39t2zvBMLC6XV-KtDwngforMMq1tLW2avjPUubf3-uMjNzNI_jkle_mGMfAJ9hx-59ddOHNiRjPhNiCaEPzuM3sZkfpHuSfaHMDSP-eAdflpFtrk3VpleVcuZhAfK5x6IBU_S-6Swp0kAQfmPUNSPQuL6Y9rGvMveHH_NbfZu-05jZ7clN33ke38XAx-0ZchYWccAvKhpANc_kkiZbe3aff3gJ7PX4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=Q-VN_OfQkX_gn_xRwNvXWXj3NL6g2FjEL0wUZocAgsmzjB48_NpSwjyVYdomXqKjJXXlseIL_3a-4IxeeP5mn9kP5aTiJxekKREjLtMyxd2u2h0AEyEiYb-UkTMDz_1SPMyrUFow0fwIDAjZDGp8H4k1uf_JRODZMPAgwf8n4b9kt_00ZI5DlY825Num-EaESYhIN0QfTXnlN04swp0svvnVIkjayhtvefW-pUA31uxEy_dGxLPDP1Ud_E8AiaD62DFfNR21Pki7OGuuc1g7XdR2ffVimqWm4mTdYxHzfujPcZC55LPr3jpufQYtvPcbpnYh_YkXIWpTF7H0Symd0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=Q-VN_OfQkX_gn_xRwNvXWXj3NL6g2FjEL0wUZocAgsmzjB48_NpSwjyVYdomXqKjJXXlseIL_3a-4IxeeP5mn9kP5aTiJxekKREjLtMyxd2u2h0AEyEiYb-UkTMDz_1SPMyrUFow0fwIDAjZDGp8H4k1uf_JRODZMPAgwf8n4b9kt_00ZI5DlY825Num-EaESYhIN0QfTXnlN04swp0svvnVIkjayhtvefW-pUA31uxEy_dGxLPDP1Ud_E8AiaD62DFfNR21Pki7OGuuc1g7XdR2ffVimqWm4mTdYxHzfujPcZC55LPr3jpufQYtvPcbpnYh_YkXIWpTF7H0Symd0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=VmclNrR2IVvYfJFIf6TUKcmfycGs70YLO7Y_ZL-z4bIy_fLtqconhAn91pxXwcfWv-YTmnZnfUHRuZUlkQZJn3rK8j_Hzr8_h0sN8KYRpUeasp2PV5hf8EGpdwxQpeI2Y5qNzLkeK8ojfHfxy2LTRFpF2QJKz-ZFnC6VDrv7U7k8hiMms7AJwUEvzvX1lBTYyIGDcF2n1VnnzBOKVTNLWVeXv9VEnATrkT8ELOY__MEY7UEQ3Wa_CNNFVWIq8WyG8l_IKE99_3LV2uqXAckMtyE9lG-5Vl4ibFkI_UV56Gaunwn7DY6meLPr1Dwmn0HjgmXk17D43W4Q5WPgtZiLOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=VmclNrR2IVvYfJFIf6TUKcmfycGs70YLO7Y_ZL-z4bIy_fLtqconhAn91pxXwcfWv-YTmnZnfUHRuZUlkQZJn3rK8j_Hzr8_h0sN8KYRpUeasp2PV5hf8EGpdwxQpeI2Y5qNzLkeK8ojfHfxy2LTRFpF2QJKz-ZFnC6VDrv7U7k8hiMms7AJwUEvzvX1lBTYyIGDcF2n1VnnzBOKVTNLWVeXv9VEnATrkT8ELOY__MEY7UEQ3Wa_CNNFVWIq8WyG8l_IKE99_3LV2uqXAckMtyE9lG-5Vl4ibFkI_UV56Gaunwn7DY6meLPr1Dwmn0HjgmXk17D43W4Q5WPgtZiLOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXY9EUbWDfJD45iohsAu-Mh3EA-BTD5z9z1vByUXWcw9kQLN9IcZmGeD7hiTCkCUCttUqljW-fVTZLVNnvyO_ExF-5PJo3deXfJ0Hy3S_jKnkTl3uRmyT-7r-oW0vrDItf5QYiae0DSoZYUmaC2q5RcOhvm1tGifW-3QlDXXEcWXKd-F3nPNiAaBhF067OED9qvwsw2SB4iywi3_McCwta9HbcrAfgS9jeLvNFw4NfimdY5MujxfuBCF4daoHkTOxy-3R1XJEGoox4QOT_rkDYpBgquLau6zME9X22TazNmTOcxaip28mjDmPadrLt6AAqWPAs5pCGXcsvp7Z1arig.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FFD816x-385F-GbecTqsCxOLM-MM9NaAnVS0ec7j5wQF5WNuZXNGLWUWJDoXoQKMFXAvUzUx1iU4nA-oAC0NQcV25JJaZUKW7K2Y1rrxibOuGzPIPgqhavdQeYY8-EizSIpyFDOUr769j-ouoFgNy1LWBz6kol9Nc522go0YqFoVOtD3MbV_Z8ZRio3ZTJQPkS_O6U2_bI95WmSVx7NQaQ0ViniSwkVIA2CqrVJedAx86bpeUWzuhyyb-vsXvswqv9BhW53Jq_pUuzaPVRbLC4R43UPPXWFFJozlvszbKny90aZLham4nKDWxq6WnXUMu1sfFaWczsW8hdzDpRk1bE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8FFD816x-385F-GbecTqsCxOLM-MM9NaAnVS0ec7j5wQF5WNuZXNGLWUWJDoXoQKMFXAvUzUx1iU4nA-oAC0NQcV25JJaZUKW7K2Y1rrxibOuGzPIPgqhavdQeYY8-EizSIpyFDOUr769j-ouoFgNy1LWBz6kol9Nc522go0YqFoVOtD3MbV_Z8ZRio3ZTJQPkS_O6U2_bI95WmSVx7NQaQ0ViniSwkVIA2CqrVJedAx86bpeUWzuhyyb-vsXvswqv9BhW53Jq_pUuzaPVRbLC4R43UPPXWFFJozlvszbKny90aZLham4nKDWxq6WnXUMu1sfFaWczsW8hdzDpRk1bE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=NpjZpUUiLXWQcR_i9Bln2MZujVEJQOmfpmBgaRjg-dW_YLkqOPjKg6UfKxatbwl2QBIADcdsPxIjS96MFtvePbaWaDtQYKfOTbmuZVMpWBlZX9ovvOgHsOldYxUAL34qfqqM55z12oBJvUZ2F3LZuPJIqMdfmx0cBCmW3Em52FSkknlRECN8HfbxJMXyA5VYIZa7TJlTC2ZnYnpVDKAztZK9CKdjls4cVh-8-GA73osLyAc5sJjcXM6toXyiuvJq9bXxb8BTmmGsTJAqDyUQAGwbsIyCCNcU0pnrzRLUxhrBNeDtWTh88SA12ZZ7T6ZH8zDfzWqVb7-Rsw2y4qcISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=NpjZpUUiLXWQcR_i9Bln2MZujVEJQOmfpmBgaRjg-dW_YLkqOPjKg6UfKxatbwl2QBIADcdsPxIjS96MFtvePbaWaDtQYKfOTbmuZVMpWBlZX9ovvOgHsOldYxUAL34qfqqM55z12oBJvUZ2F3LZuPJIqMdfmx0cBCmW3Em52FSkknlRECN8HfbxJMXyA5VYIZa7TJlTC2ZnYnpVDKAztZK9CKdjls4cVh-8-GA73osLyAc5sJjcXM6toXyiuvJq9bXxb8BTmmGsTJAqDyUQAGwbsIyCCNcU0pnrzRLUxhrBNeDtWTh88SA12ZZ7T6ZH8zDfzWqVb7-Rsw2y4qcISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RatEHsrZiqCSTWwOw6WAkYFgaRBWPlzdBhtMw5rhRnOM_PeLSRlEl3WFumQRAquWSQffwMCEFxuhnicv70_a8l5OTfE1yJvwN3nnQqqfkBuKY2z2mG_ZoyQFcMip68Z92T3KF5fxjfyqDo18NpXPphz1nIt1FoLStpnnqoz9v5g27I-p293ckEBcv-HWC7Ly6Yvh80X0NxDITJ9ki1I2X0QE8hz6NpHZYLTCHO4bUqvNlCLZpwKo6d8VKNE5Hhf-HBJ9eWdKW-o4IDeaOtEG1Q51QQ56zwRWSw9NJ8Gd86OYAOofKBq87rwZ59y365JnY2gyvFQudae971zFp7BQcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Ph3RJXQ7484MNBlK7z3xTnE5yOoV5GdlI71vbQl2eihJHB7h2hS_1FXtunasUXTecsyIRiQxkwU0sVCu218oLT8wZwyvUNb8za1e6lWoOYvBxUdtQ9tFhVWAxavyJLKDz50djrlEQZJnkcjITLA3FBxQ0Mnr68nqg9YU5VUWu5ScAHDwM_pyBoGJe4MR_u6fcnVbTzgXaxEgalYzLIwGoNmWjcnuP4lPV2vWB_d4AkS5bo-gT8CTr3qrq7IO3EUD5DY5-nvHMefeAI6-V20ZfPZDqQDxNz6KAiM4TPQ4GtRRJGI0vlbq-GEUufqsv93DOIP6LjgiF7f1OQGmN1I8ybBODq8zlQU7osAp1MakdQTzHtfiePXaeuGxLKarw54TIpp7gEeCYFrFtDtb019RGgelGQ95SLNzuhGemXPj4IzM-C0ASSDrD9IzBFhWsXExH0d-4ZsB5rG_bmwXkWihLbtOeuriyhR0-fJ7Tjgf0XqxouRkSJ-Pv5BxZHz3meMFupjd8sSM-VlFiATsMNh_4zMbRQJxKQVU_CdI4CKRuwizeJH7ebfkn-zgnKYJPSvUMaEvkDW34bLSv-TR4JPNg4bs0KNzrnn_xd-CuXBNesdYWsXJWAYJ7QYj3BSabqrTt8DdJ-gSNeqgI5YOs5C6HvrH6fW0OXoJiNXs9V2EtK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=Ph3RJXQ7484MNBlK7z3xTnE5yOoV5GdlI71vbQl2eihJHB7h2hS_1FXtunasUXTecsyIRiQxkwU0sVCu218oLT8wZwyvUNb8za1e6lWoOYvBxUdtQ9tFhVWAxavyJLKDz50djrlEQZJnkcjITLA3FBxQ0Mnr68nqg9YU5VUWu5ScAHDwM_pyBoGJe4MR_u6fcnVbTzgXaxEgalYzLIwGoNmWjcnuP4lPV2vWB_d4AkS5bo-gT8CTr3qrq7IO3EUD5DY5-nvHMefeAI6-V20ZfPZDqQDxNz6KAiM4TPQ4GtRRJGI0vlbq-GEUufqsv93DOIP6LjgiF7f1OQGmN1I8ybBODq8zlQU7osAp1MakdQTzHtfiePXaeuGxLKarw54TIpp7gEeCYFrFtDtb019RGgelGQ95SLNzuhGemXPj4IzM-C0ASSDrD9IzBFhWsXExH0d-4ZsB5rG_bmwXkWihLbtOeuriyhR0-fJ7Tjgf0XqxouRkSJ-Pv5BxZHz3meMFupjd8sSM-VlFiATsMNh_4zMbRQJxKQVU_CdI4CKRuwizeJH7ebfkn-zgnKYJPSvUMaEvkDW34bLSv-TR4JPNg4bs0KNzrnn_xd-CuXBNesdYWsXJWAYJ7QYj3BSabqrTt8DdJ-gSNeqgI5YOs5C6HvrH6fW0OXoJiNXs9V2EtK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gI23zHPK0fhWlND5j7CMUhCYiyOGGtkNLNPzzYqIw5_TVhQ35SLrV4dw_ns3mJ5OCVzaTjhOpAlTdfcvRWjiqDHD-OJiEF-szIzlp6toKj4lnlYHgouyPyho6XzqpeTrTmw5fprbdzKvhy0FQZeGvYWHsmcGetWufWfNsGkS6Axi_4S9RwJjV-FnFkKOE0pY0qMVf0ZF4AYsbEBHazfR83sSqQNdQMfFJ3VaEnA6F1-ocPStbG1W4KHAfJWt5eZ0wVAtESndrWOjK-n1PyPqnYo6Z6fggg34D3yeiiye1LA1ODXpbUYdAbP8vC5m7SUzOYYZcal57-IuCgClNXXLcQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=WFBduaJ1VIMEWl1XmXmBd1bVI68xdn5_2S1LhMiv8TEWmWEl0ayrffGTKb7_YaImfL_6KVbbOevnLEcyxf-CJSYmgzpkDo3ok0HPZ117ECB8FvOoXds0L14xwmaM7l_6nZxD6FrOTl6QSk03gvHkEFp7gI7y2-VPsPZx1JvZ1eb4-5Gs8HpOOp9B059UWgmUkEUJjNygEpYlBzyIvXPdyOE4Fjutdmp1iNBFokG0BKNkFJI9KmYzmVjBpFANtJS_Jrdl3st1TgB9ysLr3TNfdwjr8AhXbQcQAGbD-7JqS8eWHMBgNXzNR1oR6Z71sb8AHHTmEu_jDqXU9Wxano9bXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=WFBduaJ1VIMEWl1XmXmBd1bVI68xdn5_2S1LhMiv8TEWmWEl0ayrffGTKb7_YaImfL_6KVbbOevnLEcyxf-CJSYmgzpkDo3ok0HPZ117ECB8FvOoXds0L14xwmaM7l_6nZxD6FrOTl6QSk03gvHkEFp7gI7y2-VPsPZx1JvZ1eb4-5Gs8HpOOp9B059UWgmUkEUJjNygEpYlBzyIvXPdyOE4Fjutdmp1iNBFokG0BKNkFJI9KmYzmVjBpFANtJS_Jrdl3st1TgB9ysLr3TNfdwjr8AhXbQcQAGbD-7JqS8eWHMBgNXzNR1oR6Z71sb8AHHTmEu_jDqXU9Wxano9bXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNYPDU5NqVHXo2BTGLqhHHROepMyTBXSdwbobUAMB9k2B-dI4bzPkt7XFhrZz6DlC8w6_OmeELwoGYQtSy--iBj49PuLBN0K7MR5hm8rjx4fWu3rPplkgBMaD5G-AyH34H6lZEE8mdwrElOXTH60VdTk5os-BuR6XBCGKkhoMBlQCjD2HyuIwLMJg2xxVpvx9SlvOidzL2YYXnsj5QmpuQNBe0l8Cs5hjncSzxdnmq8Dx4ig526upUPHH56ZhOYeSN8KRrqUf8pqL4258lpD-SkBEktYAuH7YKVhq-LLSSuTUbNiOEFZfNQunVRHtsJe8oNQOzFw3dar3HEEUxBoNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5txVNpzPDbuPoFCjK54V2CbzplAVebQz_uMQhDbwZDT12R7qM5VU2wnX2ujPkJtt_BQb7u9n5Gw87sENc9F7hCzTPq82-dP8s33qa-Yjf4N_p1jHvWhMNmBpYloIy7L7TOr6BPSVzCv3Zmm_CfIWV5d4csNasBqE4CPj3Mfi6QgqTXQHOrdEou4MnI845Sgr1PqkfB4WoUkJWCE4yCOPCWk0NR5CZ0y6x-Md4PXlPCrWdIyKvDJ9l0JqFWVdshKXzigPNofYLZ_a90rhaW4UpRnodjATMxly0lTVGYq871H2p_1YeMKihVXZjpoLKMUEYPisMVJ09aT24kSgnfCbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jcHPokZSyqS_qduXaGI1DK39UQvr3ZF3c7hDQKME8IeCay0SmIIjkiZsxC0doaqBizxIfoKX9T6p-0PPg2tw3-SpMVdXjgN-QELMxEnlrkTKBl-FAUFxGmSljrMXl8-8Lj8-Z56KH_UGdh8baU34B1ccvPNAHNz3NKHI8qik-P8uu5zRTrH-_ayIaFAL9rhmsUo9kVr2WZcfiJ0_5TjFd3zzf7YH7mP6wAQhs1jKs9zaeNfVf7iPLgMTyt5MymqaKrPE3Y5OMjcE0RvD7A_LARaJvNbUKNFqrjugtVkVvYiUQUQFaJOUvTAna1bV-42Wy--dC33YCwvNqSSNuDvHxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ktYDu6NIzML8dLScKCaDSvNzd20Jq7pT9jOUPi97KfwvCwCGHLu9x-kQxkHFzZEZUoVRjUM2Myt6DS2vT6X2YzeIbGPxUK9uhcoPSM4yweChGBPowIWgwGqX2-uCb6ONbVY-qsoXLuBdrEtEMYuA98eYFhFoFDpyHBNsOJccEj7LW-17vHoDp0AeWgnybkBVZ2hjbsk2jTLmbEtqW8_3rBfN7Fz2G6ny-wVRTPdo4o8UVqMeJghFnUayozNQGpPo9hajjFxx58F5gVeAXHL2_L-sVXdmmfNucWfbYTby6Nc-DmlsbTMRTOua0Ko6RSMUuYYzByuNE3pcQxtYcKh7hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=ktYDu6NIzML8dLScKCaDSvNzd20Jq7pT9jOUPi97KfwvCwCGHLu9x-kQxkHFzZEZUoVRjUM2Myt6DS2vT6X2YzeIbGPxUK9uhcoPSM4yweChGBPowIWgwGqX2-uCb6ONbVY-qsoXLuBdrEtEMYuA98eYFhFoFDpyHBNsOJccEj7LW-17vHoDp0AeWgnybkBVZ2hjbsk2jTLmbEtqW8_3rBfN7Fz2G6ny-wVRTPdo4o8UVqMeJghFnUayozNQGpPo9hajjFxx58F5gVeAXHL2_L-sVXdmmfNucWfbYTby6Nc-DmlsbTMRTOua0Ko6RSMUuYYzByuNE3pcQxtYcKh7hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/caCb7B8vTWRqKHscn1Oq1BGTk1brnG6JY2aPA_Qrzv-S__wWvzHUZa5x2vYwDzcBipqOm6qwlzmUkmN51kLFdK-PClEHXyHdCRJTzFtP-ur_jR6m-8-vpIvFvS495w0d3RB47k1vkhlXuJlNwAwViQcmSahzWyVDARUsR8yDsakjoZ_5onilFP4VFBzX0Utmx0NBVVcqh0ZzxKl9R51csJBhJpkF1cEr7Vj4xJTysEcB3Z_b9I3db9AqEP_oRN-W5MiwblHmQdzJqVqXin06vY5GoaNi6ATivRmrnB7sK0337675dN3jNFaeN99ODtgTtZYPE0eChL-QeD_u7twndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuzePaMYqF_rxUbV9k4_p3s6VmGllEsFvOqtBcpBtw1nLL3B6cKPU8t-tqBDZxj_VHLpma-uAVkh7QjJyJsDKiePONghO6k0VkhFpzk_RhonnrbDAhfXNRKyJGtIXJSlcsZBs1g2vVLGj6q6K553OUjG4WAEiEz0-SB4fh4CuMufBTnY-LfMtEnc6ax0mPgrnRxaQmJrPpx8xCIOKRLCHDWxts6bjdf6tgQr7CtwdpfHDgt0MgRC8X7DFoTsWAJQtKFDRW6oXhBrnWOVBalGBiGpm1eYX_4LTDtovGt8Imb7nBiLiJzoLzuYs59C_1c9YKxLIB8yEF1mS_a7A3S8H_Ak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuzePaMYqF_rxUbV9k4_p3s6VmGllEsFvOqtBcpBtw1nLL3B6cKPU8t-tqBDZxj_VHLpma-uAVkh7QjJyJsDKiePONghO6k0VkhFpzk_RhonnrbDAhfXNRKyJGtIXJSlcsZBs1g2vVLGj6q6K553OUjG4WAEiEz0-SB4fh4CuMufBTnY-LfMtEnc6ax0mPgrnRxaQmJrPpx8xCIOKRLCHDWxts6bjdf6tgQr7CtwdpfHDgt0MgRC8X7DFoTsWAJQtKFDRW6oXhBrnWOVBalGBiGpm1eYX_4LTDtovGt8Imb7nBiLiJzoLzuYs59C_1c9YKxLIB8yEF1mS_a7A3S8H_Ak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=fRtR4Rl_V5HNycGIhz-U308RrX7QYgVl3XkCAxlaiDi2vhTwloJykw7JNd1FDD7KXGLWzl4wtI1R8G4GitJVWed9Zs7Kl2UH_DxEwk3IaeGh3BWyzu6nKOizjxIi-EcNRRznaQPbHhEviPAlILVOYIs9Kx6hMgL4ZTNCkemimrRdHSu6UKo6GpMJDUY-62vlt_lSZQL158hQFEEH77NDIm2PeXxG3Wrqw17pziInb7UA7CbT9jU4Zta-LY3e4x8n7VzaRcv46j4GCqVvRodYLSSPD6h02ft8XTfPnTy3zFwk0349g5UpaiBxs4zZXCT_cF_kZfGT7CxaimO0ia1ijg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=fRtR4Rl_V5HNycGIhz-U308RrX7QYgVl3XkCAxlaiDi2vhTwloJykw7JNd1FDD7KXGLWzl4wtI1R8G4GitJVWed9Zs7Kl2UH_DxEwk3IaeGh3BWyzu6nKOizjxIi-EcNRRznaQPbHhEviPAlILVOYIs9Kx6hMgL4ZTNCkemimrRdHSu6UKo6GpMJDUY-62vlt_lSZQL158hQFEEH77NDIm2PeXxG3Wrqw17pziInb7UA7CbT9jU4Zta-LY3e4x8n7VzaRcv46j4GCqVvRodYLSSPD6h02ft8XTfPnTy3zFwk0349g5UpaiBxs4zZXCT_cF_kZfGT7CxaimO0ia1ijg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=tLQs1BNMR-fSowBRQpYfRIOJITAAu4er9wVOA9O35nB7sKjMyHE4gTISK6uoLL-88dqmZlqvIMfySVbwHMGN1ELDrfwWULhPDawaoASNZEFS_1W-V6qZDqBBd4JObFJngBjTBlt1Vom00wiDbBIqxScsa0dUdfWA-zFuTJReBbTxLkvUq3yEdQgN6yLs35HNJZwLO6RF-ruZhFMtUAiBYW3vcH3GVmqQ-8TWk_d1YY7yvw0jK_qSJyVH1NnCiD2Pw6NuVgsdWkHDBvnzCqSnBxGQyGQE7qrH-fN6fbSz5TZF8SahWrabZf0MxGMCF-yc0teQcONcFyG75LYEsCVvlGysRtQA4wnl31i_6KZ7W6cdvA788HhMjCtpXJXIJGaGyDcUN1KRNmKlwiKjzmYKqkDlPOZQPaF4Rxt8mVAnuTCbOE8Xa6lzfWZY5l_x-vWHDDCJSqnVy72tZpGdHLFykt7fkPPlFx3z9eNNGzOgp5NMAAh0d13nGNIiKC9peDGCn5LImPoo5M4gBl4cLnzPXUQjTA0ziAVd_tJBM_p42W1CwRk4XSn71dvQvW9VZNUxl8T6N10-l9H6-LcfYU7AOo3r1oeSlqoG96j9NdiptBU6XghK-q438dAkCu9e1AXeh2SgiaOpZjd7yKm9V5evdFekOFf0j3mXl0Q0fOFYEhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=tLQs1BNMR-fSowBRQpYfRIOJITAAu4er9wVOA9O35nB7sKjMyHE4gTISK6uoLL-88dqmZlqvIMfySVbwHMGN1ELDrfwWULhPDawaoASNZEFS_1W-V6qZDqBBd4JObFJngBjTBlt1Vom00wiDbBIqxScsa0dUdfWA-zFuTJReBbTxLkvUq3yEdQgN6yLs35HNJZwLO6RF-ruZhFMtUAiBYW3vcH3GVmqQ-8TWk_d1YY7yvw0jK_qSJyVH1NnCiD2Pw6NuVgsdWkHDBvnzCqSnBxGQyGQE7qrH-fN6fbSz5TZF8SahWrabZf0MxGMCF-yc0teQcONcFyG75LYEsCVvlGysRtQA4wnl31i_6KZ7W6cdvA788HhMjCtpXJXIJGaGyDcUN1KRNmKlwiKjzmYKqkDlPOZQPaF4Rxt8mVAnuTCbOE8Xa6lzfWZY5l_x-vWHDDCJSqnVy72tZpGdHLFykt7fkPPlFx3z9eNNGzOgp5NMAAh0d13nGNIiKC9peDGCn5LImPoo5M4gBl4cLnzPXUQjTA0ziAVd_tJBM_p42W1CwRk4XSn71dvQvW9VZNUxl8T6N10-l9H6-LcfYU7AOo3r1oeSlqoG96j9NdiptBU6XghK-q438dAkCu9e1AXeh2SgiaOpZjd7yKm9V5evdFekOFf0j3mXl0Q0fOFYEhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JbNFM-fpVGU90Mula1bqBAuZarTvQU6ekgRKVPwAVHv0XdJ9FHc0USztXt3liDZgnOK1WA6-Cf9RcY0UjpezLljI9LmlR_YmcnRk-aCu2s2LmkN3nWNAar_q4NoZnQDqybHWBQoV1w_ld96aiVe-tQJUXDkhv6p-sZgTrZmM8jSXnoVSth3SkfJSwiOV3FG-2svWfiCbCVlTpAlfKhGmKNyjc5erBfuKf4QNuEnrW3e_SnJenVdCe7BySByvHuMI68nR-AEoyny8BXxyjq9_Btbw3VIBYTsMaenPBw38zPL-fgGruRUbmz_0W3G7ZVs-4BWygA2EF7AM7g6o00m0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JbNFM-fpVGU90Mula1bqBAuZarTvQU6ekgRKVPwAVHv0XdJ9FHc0USztXt3liDZgnOK1WA6-Cf9RcY0UjpezLljI9LmlR_YmcnRk-aCu2s2LmkN3nWNAar_q4NoZnQDqybHWBQoV1w_ld96aiVe-tQJUXDkhv6p-sZgTrZmM8jSXnoVSth3SkfJSwiOV3FG-2svWfiCbCVlTpAlfKhGmKNyjc5erBfuKf4QNuEnrW3e_SnJenVdCe7BySByvHuMI68nR-AEoyny8BXxyjq9_Btbw3VIBYTsMaenPBw38zPL-fgGruRUbmz_0W3G7ZVs-4BWygA2EF7AM7g6o00m0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7i9ae4ntlMJAug7LiQfvjqjdjmK013towv3Ci9ibcGrECLT6wFZcljvnX7_Q3WtC1UgwSfdHb-IibZq0hQepexX5BZLJrPpeS2A_gCU5zV-l-hV8AklvmUufStjxoMenmQOi2PCjsJq4LAERglI3kl6MuFjqVeqMQfZb7aDQSLc00CoSSh3R9HzDB5zTblHiqM_iq2iXsP_3QODfJvwxr0cm-qNEXBThoUgOHRnFE1oGpD_3I0kk3K_NkMf6dAXKssrLdD0fskrPt75g9VwglNcNBOYTW4LIoPz4UF_fFoK-VhsOuDsbuouLZG7P5OXyvxdFM56SRWMynNwILm1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=GOPTiYJZXc8_l8C8pw8oHXIygvsVWSibUnh5Fzsr0XMRMvkRhyiF2BLNgyHwXT84SxLNC7K4NKCT1aq1yZC0sHGgQknqjB-a9KmwJyhyPp3iVz_R0q_XDAnog7R1pbI8hlSuF2DfqiuJTJWbOgC2E-gLOzrnP3_kJEyDSm916BpJNgo9U87NsOc0Q3P3M9DJIf7BMq6z0ZCbv6F_7jKA6y7AT_lA-pXExmpKBko_ei1rlltjRodqQFkFGjvKUz7pVWogn3l1QpG0aTDWIecz3YvQS1U3nmicJY4PFR2Ios5VbuYUO1wyQ-pmdncXpxe2DI576SKYTmdNP8J2i7zEig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=GOPTiYJZXc8_l8C8pw8oHXIygvsVWSibUnh5Fzsr0XMRMvkRhyiF2BLNgyHwXT84SxLNC7K4NKCT1aq1yZC0sHGgQknqjB-a9KmwJyhyPp3iVz_R0q_XDAnog7R1pbI8hlSuF2DfqiuJTJWbOgC2E-gLOzrnP3_kJEyDSm916BpJNgo9U87NsOc0Q3P3M9DJIf7BMq6z0ZCbv6F_7jKA6y7AT_lA-pXExmpKBko_ei1rlltjRodqQFkFGjvKUz7pVWogn3l1QpG0aTDWIecz3YvQS1U3nmicJY4PFR2Ios5VbuYUO1wyQ-pmdncXpxe2DI576SKYTmdNP8J2i7zEig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Uo0JMi3-hzOs2_rgVIfFFYKRT2JPiWtTYNxmOEieXchzAO9zUVFDKEGLqrtnrvKNe1ccFfJZJ8zOisW1kJVNAWd6JuBgd4a9QAxDeRzioqFfHrgT8Q9U9f6EMaj24-9dK4VWLA-Z-2OTDJ_ey1mJI0FUAKXKfAC2i2foT_BtYH2G-sDqor7kiZxI5YffW3nQ3yh1ivvVn-OCeoU-zZGiChnYT0XvLySZkn_Z3-EbMf60uLkI9wqWezeFXnL0g_9fvyV9vR9Q_OTBRXcYhTSzhjpjRE94-2rgKWgmQ0qEGMCG3gqlMBPSBLqJhMr5-MTyMz-8-OEl1z8y2_PKGHyB_QT7IPyo1Fs7JwPeF1jXUA4Mx8ChLauw4GC5Yw2Rb5YDXdBoEYkiHeoONJ9PG10WIBEUQ_YwZ2GB868xxf9zt_9O1KvWWlnpueblazoJsU4KSqs-Q9ZgOiKN6hQaHZjOOslQnJpTWvTzLZJLMjXRc2G_9KHQFIVblwWExIQdQYoNSNMuRXBN6e5eHZxIzfcTvTEXwmvr4SlUSHpimV8pGWUngxlOMrjg_d_iiHkPZxqOV5pR40h3NvRwjOqJmVmq32EeQ3PKFFD4tk5oXdK0LNMNXmPe_b8ztg_0WMnXIbqPWOOfhwN_CqYP6XxnfBl1bO-7tX1uaxKBHYoCkVW1brQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Uo0JMi3-hzOs2_rgVIfFFYKRT2JPiWtTYNxmOEieXchzAO9zUVFDKEGLqrtnrvKNe1ccFfJZJ8zOisW1kJVNAWd6JuBgd4a9QAxDeRzioqFfHrgT8Q9U9f6EMaj24-9dK4VWLA-Z-2OTDJ_ey1mJI0FUAKXKfAC2i2foT_BtYH2G-sDqor7kiZxI5YffW3nQ3yh1ivvVn-OCeoU-zZGiChnYT0XvLySZkn_Z3-EbMf60uLkI9wqWezeFXnL0g_9fvyV9vR9Q_OTBRXcYhTSzhjpjRE94-2rgKWgmQ0qEGMCG3gqlMBPSBLqJhMr5-MTyMz-8-OEl1z8y2_PKGHyB_QT7IPyo1Fs7JwPeF1jXUA4Mx8ChLauw4GC5Yw2Rb5YDXdBoEYkiHeoONJ9PG10WIBEUQ_YwZ2GB868xxf9zt_9O1KvWWlnpueblazoJsU4KSqs-Q9ZgOiKN6hQaHZjOOslQnJpTWvTzLZJLMjXRc2G_9KHQFIVblwWExIQdQYoNSNMuRXBN6e5eHZxIzfcTvTEXwmvr4SlUSHpimV8pGWUngxlOMrjg_d_iiHkPZxqOV5pR40h3NvRwjOqJmVmq32EeQ3PKFFD4tk5oXdK0LNMNXmPe_b8ztg_0WMnXIbqPWOOfhwN_CqYP6XxnfBl1bO-7tX1uaxKBHYoCkVW1brQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ikpOYN-ULXPt-qJI40GgRKVQTtVci0L-943xBZv5WcBVroq-nlzw0jcMq1UK8cUtDM2vKXI8NlHVI0o9sQlkPJbHCZwWe0hZwSuAsnrRbIYWaz80F0IgGZS6t_nfeQrUyVfplvnvkQkear9k2lJ_uYB5wnAudbJVYWMN96xGNqgSk3vC1rV1FZLsDf1ryPwyhic5yHSkpw2H2upw5nRjegp5ZK27svTWJc4ozp27W77LqHUaXYrKeXBQ2e7wTDd_TtDPGVg-3XmSSq2RTuLPS_MX2JoO4P4VOM9n1O1NvALY3KydEXAFuJrZ4iRw69l016tM88UeIgEZi0HUVYdhLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=QWLWGFJVRamTR1jshq-mfKq9PMdRiHClpeVEp4DarWoVMGhRLyIF4bFKPXvLPmW2kqnzFJs17I4wIpDYLeWymX90kfdDc1Ss_byiF8xG84YDvzjXlJnu6zd0oLLcokPJhjU5OpkW1oLLjlwXyOPTwm_IpH0o27muCbeijrfnMPONz8posP-wbikK5nYBMQoohsdukYG8jN2EsfgtrxA3BqOVRGvfjxIuH6H21dwkUrRp6drT8IKvsMcaSwoDVNn9iEy0-kic_6qM_UVwN8LTF8gPocr1zurZWh4N-GldoEkWxHzyAbi8mh0l_t7LW4Cj4lodFPqrkgM1nxlMzkKI53-6xb6XfptlOBSTTxL-glTjajPAEsVDzU6GeQ1DSK0rj3zEw89ImSjRIdBtjEqTD0Z6ZjFKctL_r-_Zc5oETSQ4wpCxRMRcEF3pACxRMyHLnvZFIDm2O3Bs4lkRWBCPTgHSJm--X1C40OwMGjR9VzObKGLsaQbjvrfzBZ182__g8r061hQj8WChTDm0hQjkYjG594YiDmEMVdrL2sTBB6Rd760GA4e28IrrkzGTjNPu-lBSy1B4WyBeOPGAQHqDH7-fP3GIqQB1ZlZQjNKasePxU4V-WUllkJJMovnpsWv4DBycqPiZoDngIJSNYJ8GlVsmTvMvWBpW2VEoWEFqp3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=QWLWGFJVRamTR1jshq-mfKq9PMdRiHClpeVEp4DarWoVMGhRLyIF4bFKPXvLPmW2kqnzFJs17I4wIpDYLeWymX90kfdDc1Ss_byiF8xG84YDvzjXlJnu6zd0oLLcokPJhjU5OpkW1oLLjlwXyOPTwm_IpH0o27muCbeijrfnMPONz8posP-wbikK5nYBMQoohsdukYG8jN2EsfgtrxA3BqOVRGvfjxIuH6H21dwkUrRp6drT8IKvsMcaSwoDVNn9iEy0-kic_6qM_UVwN8LTF8gPocr1zurZWh4N-GldoEkWxHzyAbi8mh0l_t7LW4Cj4lodFPqrkgM1nxlMzkKI53-6xb6XfptlOBSTTxL-glTjajPAEsVDzU6GeQ1DSK0rj3zEw89ImSjRIdBtjEqTD0Z6ZjFKctL_r-_Zc5oETSQ4wpCxRMRcEF3pACxRMyHLnvZFIDm2O3Bs4lkRWBCPTgHSJm--X1C40OwMGjR9VzObKGLsaQbjvrfzBZ182__g8r061hQj8WChTDm0hQjkYjG594YiDmEMVdrL2sTBB6Rd760GA4e28IrrkzGTjNPu-lBSy1B4WyBeOPGAQHqDH7-fP3GIqQB1ZlZQjNKasePxU4V-WUllkJJMovnpsWv4DBycqPiZoDngIJSNYJ8GlVsmTvMvWBpW2VEoWEFqp3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=DiNNtzq8oBli8tvRDnLl0b3z0pmg2N7QUurZJCtvayi_FFMpEY3scaqISmsqrj87WbOnCdTTbFZNQESOKT89myqZ-GUSnqmCUvhjxgr6TLBR-OQfoqAWOO9NsXXNygQ78xtM1w3FIuuRA9TQVCKHSYrJI0Q5AT5FpZwE6I0idXS9IRQHuGaH45gR8W5jr7raSl6UBKTdi8wLAH6gMOemAgfnvraber2rLGxIQauxyRXpDSTT1ji0oUBPpehmCg2mQwiipqvf57CWG3RhVa233xka_YXZeA1q5LEb8-z5XbZgx1mdSzHdJg5N7PcHWSnI0QY0kMTGs7v4qeuJ3IU4cTm41jvyFleW76i6E8Oq1-kd8wENd6EBHOr1GquFtPVd829ydplt2AmG7d3sN6jvZf_I1NY2TVa1opi7keIye0y4TUpTNAVWjIl0cdQ0k9Qra-mJ5i-xrsIc2eu1aZw1d8p8r21TzRO1Jx0pt-Z6-QnbU_U76iqnAq9kSEiCf6jlFil3wZOOoT6vyzD1syij060JaE4CV6ZJH6gtKP2m0lTIA9vY4dDK903jwNXEQx02x9KTYOyQ_9cqxiia1t8RsXmFFLpb10bSPIJQINkXDohk0pME9k6_ztp9NiAFZwMIBsx_tnoagVSNAnYjutpU_A9Hkcj4hXkJvJCTvJ3tb8c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=DiNNtzq8oBli8tvRDnLl0b3z0pmg2N7QUurZJCtvayi_FFMpEY3scaqISmsqrj87WbOnCdTTbFZNQESOKT89myqZ-GUSnqmCUvhjxgr6TLBR-OQfoqAWOO9NsXXNygQ78xtM1w3FIuuRA9TQVCKHSYrJI0Q5AT5FpZwE6I0idXS9IRQHuGaH45gR8W5jr7raSl6UBKTdi8wLAH6gMOemAgfnvraber2rLGxIQauxyRXpDSTT1ji0oUBPpehmCg2mQwiipqvf57CWG3RhVa233xka_YXZeA1q5LEb8-z5XbZgx1mdSzHdJg5N7PcHWSnI0QY0kMTGs7v4qeuJ3IU4cTm41jvyFleW76i6E8Oq1-kd8wENd6EBHOr1GquFtPVd829ydplt2AmG7d3sN6jvZf_I1NY2TVa1opi7keIye0y4TUpTNAVWjIl0cdQ0k9Qra-mJ5i-xrsIc2eu1aZw1d8p8r21TzRO1Jx0pt-Z6-QnbU_U76iqnAq9kSEiCf6jlFil3wZOOoT6vyzD1syij060JaE4CV6ZJH6gtKP2m0lTIA9vY4dDK903jwNXEQx02x9KTYOyQ_9cqxiia1t8RsXmFFLpb10bSPIJQINkXDohk0pME9k6_ztp9NiAFZwMIBsx_tnoagVSNAnYjutpU_A9Hkcj4hXkJvJCTvJ3tb8c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=TxbJaGPGYhYSQDB-tApQO0qpxmP6grSNJZryJOJYrp3sP7MtbiYNC5_sHlzn-5BC6OdbfovYNxAqTWd9JERX_UjLG2KCtciIRfwENk-X9VvlXCDli93Cmt2NFygr2GklpX6mhsMhT6hkVwxlV9uP6Q6AKPtqeQc659dkJD9jGWIBCJ5kmHQtjMSeelDBQEc5dUEaBsOS7cmoTMxRkoyv1KqptTFVG3P6jdeDM0kKAKJ1FBj5_vOFdr_mOhZ6AJwUsxJApU2CO1aBE5UjSkNm7N4411yTKqU91G0UwWx6SleWKFVvi-B3pjs25Djn9cXT53XuQeIwwsUYMmus4riyAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=TxbJaGPGYhYSQDB-tApQO0qpxmP6grSNJZryJOJYrp3sP7MtbiYNC5_sHlzn-5BC6OdbfovYNxAqTWd9JERX_UjLG2KCtciIRfwENk-X9VvlXCDli93Cmt2NFygr2GklpX6mhsMhT6hkVwxlV9uP6Q6AKPtqeQc659dkJD9jGWIBCJ5kmHQtjMSeelDBQEc5dUEaBsOS7cmoTMxRkoyv1KqptTFVG3P6jdeDM0kKAKJ1FBj5_vOFdr_mOhZ6AJwUsxJApU2CO1aBE5UjSkNm7N4411yTKqU91G0UwWx6SleWKFVvi-B3pjs25Djn9cXT53XuQeIwwsUYMmus4riyAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=eOJVw5OsxBjwWgpM4cZtfpNgEh2oeBoB7KWqY1DKzS9lILplMFX9UFiOTH307FIlUiCSPUifPUMMuZUohigM_FWDEH-PdxKV-czviCmwjkIfKONkTl53N4-BOORZR119MugZ0PctefoYAzBRWvR4O82Ql1-LkNfJpecXdLdCF79ioRDlNPAfDEgaiBa6bYrQzbVfv0xjtMQCCFdm2nMdxUvDNOzQQMVwD7qF_pUMaoAb6kpcyEX0aHiK-x6_wwIpWH9PgsT_pbKMGL3Lx-objYFzHxdBY-5j06cW71Hb3w4_06226XteqjyzseWOZHj6oyVIAWIGt4g_-NYCMMU5mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=eOJVw5OsxBjwWgpM4cZtfpNgEh2oeBoB7KWqY1DKzS9lILplMFX9UFiOTH307FIlUiCSPUifPUMMuZUohigM_FWDEH-PdxKV-czviCmwjkIfKONkTl53N4-BOORZR119MugZ0PctefoYAzBRWvR4O82Ql1-LkNfJpecXdLdCF79ioRDlNPAfDEgaiBa6bYrQzbVfv0xjtMQCCFdm2nMdxUvDNOzQQMVwD7qF_pUMaoAb6kpcyEX0aHiK-x6_wwIpWH9PgsT_pbKMGL3Lx-objYFzHxdBY-5j06cW71Hb3w4_06226XteqjyzseWOZHj6oyVIAWIGt4g_-NYCMMU5mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=SMDMKpe89am08MAwEBxGmmZY2XUaVr7mX_A_d8qBhavgNUbVJDP8lyDB2_sOPwBtzMI3bP_l7xCL_okEIuGJlkxeRWG3Jgg7I1mWlloR5GoUqDlIKr8DZ3_1AOfvDg3NF0SXnqNHTHsnKoxF6FU2RoessTqFsikCi_HMYyR1wAMVk7HWJdWzhZ0GLgionKIFc950-8tCq3ehxf-NW_HHmPHmBolbW9pC4UbPC4Ry1WEQRXVrIy4wnnIl4v-IHBSjZhkf7c0RveFjahm_hct3P1bDFztKz1l56XWiRoY4fzzr4HjMbtX8XJmVQIaRi9Cwd3SCGV6_n75q54H4fX-G4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=SMDMKpe89am08MAwEBxGmmZY2XUaVr7mX_A_d8qBhavgNUbVJDP8lyDB2_sOPwBtzMI3bP_l7xCL_okEIuGJlkxeRWG3Jgg7I1mWlloR5GoUqDlIKr8DZ3_1AOfvDg3NF0SXnqNHTHsnKoxF6FU2RoessTqFsikCi_HMYyR1wAMVk7HWJdWzhZ0GLgionKIFc950-8tCq3ehxf-NW_HHmPHmBolbW9pC4UbPC4Ry1WEQRXVrIy4wnnIl4v-IHBSjZhkf7c0RveFjahm_hct3P1bDFztKz1l56XWiRoY4fzzr4HjMbtX8XJmVQIaRi9Cwd3SCGV6_n75q54H4fX-G4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=vuKyq4WPP9XLT00W3Hud9EQoQfUX8YsQS90vlDq-eG0rS3oSk75qadE-oqo6s-q221PPxPoqhofsgccG4pBpDKluUo0Apnn46B5Z4dmcWAoEm_Nd0mwACs7qteh8dvYJIxH_b8cHhm9lXeVS-y14WfwbNDJDP045WYmZmNb7LkvCrO7uQlh1MDuo5nMn3DhPV-8xBF0LeEx5aCDcUkxBJh6-Slxk9EjEyQ6HVQoqx5z7VlZAo_wq0eVSrBlcjiQV0zKZ4c3AqQDIOEy9fX7Q7rR8SeihkBP-n45y-quZq6-PaLLTW_3qtK9blp7TmI1Ctb8HuI3JkFK70s4VKotjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=vuKyq4WPP9XLT00W3Hud9EQoQfUX8YsQS90vlDq-eG0rS3oSk75qadE-oqo6s-q221PPxPoqhofsgccG4pBpDKluUo0Apnn46B5Z4dmcWAoEm_Nd0mwACs7qteh8dvYJIxH_b8cHhm9lXeVS-y14WfwbNDJDP045WYmZmNb7LkvCrO7uQlh1MDuo5nMn3DhPV-8xBF0LeEx5aCDcUkxBJh6-Slxk9EjEyQ6HVQoqx5z7VlZAo_wq0eVSrBlcjiQV0zKZ4c3AqQDIOEy9fX7Q7rR8SeihkBP-n45y-quZq6-PaLLTW_3qtK9blp7TmI1Ctb8HuI3JkFK70s4VKotjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=uUBfMfMY_SnlG08HQcMuFb1I1E_ExiO5B7ME-fwKFhtgKmUD2gFv0GyTl0Ph76rjJoAzPsNUmSjeD4eCNO9ajK0WS5Jd2xn60np2LjprNVZ1C8VHgnY1X17cKvmtJXGwYC6_raGuKXy3_yDVSKoe-vUHpxKyVZPZN8_7rpoD6EUrMl40nToEoWrlGVdwqSs14wTKOTt1d-6ORaCw4eYMab39NqxKxhYFivmFKqir9ePDdk2xTRW7fpClzGWOSx4OyRaNeXhHAFGa6aHojrOMDEsgGYNzLhyNv_-9dB_nxc_HkBypy76QkM0DdVKFzdu_JJgACA8nSVrurJJxUsuFxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=uUBfMfMY_SnlG08HQcMuFb1I1E_ExiO5B7ME-fwKFhtgKmUD2gFv0GyTl0Ph76rjJoAzPsNUmSjeD4eCNO9ajK0WS5Jd2xn60np2LjprNVZ1C8VHgnY1X17cKvmtJXGwYC6_raGuKXy3_yDVSKoe-vUHpxKyVZPZN8_7rpoD6EUrMl40nToEoWrlGVdwqSs14wTKOTt1d-6ORaCw4eYMab39NqxKxhYFivmFKqir9ePDdk2xTRW7fpClzGWOSx4OyRaNeXhHAFGa6aHojrOMDEsgGYNzLhyNv_-9dB_nxc_HkBypy76QkM0DdVKFzdu_JJgACA8nSVrurJJxUsuFxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mb8gBcIZuUE0DhvTzcTQ2uY1rQJLi3NiYPvDDUVsbCy0tbr6W5mQCJw3h1gIGYKcqpkEUYp9p6KLYIgxFb-ueQj3v2QEpN3g0S2lxW5UIBEP7BdizwyMXqMpCHT8Q317JpMcDDXqC5evmZLZQ_IB6jvrTfFQ-U3u4wiQQ5RA0yVLxW8i0oSd551-h33lTHkxW2sA4D9q-Ku1nXUviVp2KrzgKqKqlR08WrimCLQ5428yBzO-R5MuTBEELEvV0xpt12EPgU-BqeY8ei3MbaqikhDZtqHWv_PUq3-mSx1hrjDF20PgVq67wjCLLylcDvasxp_fEFX2PibpilitDsU2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mb8gBcIZuUE0DhvTzcTQ2uY1rQJLi3NiYPvDDUVsbCy0tbr6W5mQCJw3h1gIGYKcqpkEUYp9p6KLYIgxFb-ueQj3v2QEpN3g0S2lxW5UIBEP7BdizwyMXqMpCHT8Q317JpMcDDXqC5evmZLZQ_IB6jvrTfFQ-U3u4wiQQ5RA0yVLxW8i0oSd551-h33lTHkxW2sA4D9q-Ku1nXUviVp2KrzgKqKqlR08WrimCLQ5428yBzO-R5MuTBEELEvV0xpt12EPgU-BqeY8ei3MbaqikhDZtqHWv_PUq3-mSx1hrjDF20PgVq67wjCLLylcDvasxp_fEFX2PibpilitDsU2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Vjgp391vg-7i7kxF5dNdM_OUdJQuZ11yIttR_9bQzxE8dhc3vSbTdGXwJ5HcetaQVd7-uBMDtAclLCiToFmJ_Z-Y2V7jC5VGi3wOrf4sTFZYIHYicxUiYXKSBjgFvzmIO9Kw4pZ0pACLZg0RprbpWeOjIAe8PBXvY-5p7oDfiT53cdUc4vI_6wjIhSnFCFtJ-EgJhMD0IG1TXqDZIB2366akdIOX0G068zgydkCtTgNCI1mulyrcBlGZhNLxKhFFRZxhLb-jDafqPFBGPxk744Io-Xag1r-Ej4U1oLHSWNpMT3mvHwDiqgFl7y8cQuMhTsuExHJLxPF4IQA-4_fGNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Vjgp391vg-7i7kxF5dNdM_OUdJQuZ11yIttR_9bQzxE8dhc3vSbTdGXwJ5HcetaQVd7-uBMDtAclLCiToFmJ_Z-Y2V7jC5VGi3wOrf4sTFZYIHYicxUiYXKSBjgFvzmIO9Kw4pZ0pACLZg0RprbpWeOjIAe8PBXvY-5p7oDfiT53cdUc4vI_6wjIhSnFCFtJ-EgJhMD0IG1TXqDZIB2366akdIOX0G068zgydkCtTgNCI1mulyrcBlGZhNLxKhFFRZxhLb-jDafqPFBGPxk744Io-Xag1r-Ej4U1oLHSWNpMT3mvHwDiqgFl7y8cQuMhTsuExHJLxPF4IQA-4_fGNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMYxUfDC-UirnFXkBm8XTMV9VHBeY3u0E19_S8Ps0KlG7rGWKR2AcNvgNOXovozT8bU_pR8zdrPqBwx7_-MgqLoJcKKyfp_kq2LsZUZdbWbZpHDefOG2BQ72pbBwc2QZTozEr99obyR9vuUNsq2YprpnPav2XYhxqQ0fdJkK6Y6XkegvRtbHbxP8Ch43oho4cxLz5l8ksMCrQDLN0PJbk6npS_sc9MNFy2kZD6ngkLI2HI0Qk4bvzGsJbvbKll_jyt57XHJrTrJc365wssd3-4biORPDax65eT0gxYQmSm5qmn22RO5PCyoFCx_4fjtnQjSWoCJHuJNOSul5-l1UtQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=mo93cKpUu35lHtLM_TKvO8_iMlamHdE2Igvm3qfE3naPSISxb_jWpKbceV7lX0a_ibDIeOs0s5DUQQPpAx74DIqvPfSYvbmRrSEpWaJHa2i_yREuEJO9qbuiBivbrByNykej-csDJxZd-BWmGbwzGNzT107fsZiZHXtPntfWbpjFQ7nAzj9fl2fRUgOOs-BwDoYzbyy1FHMq5xJpwz4VRUOGwfP2qkfowUmFLzIfEExCKgEYf14NGyABexbOVR0XSzR6MM8AoHJvYNFHJdRQuKGgu2wLFFy4IM0LY7ln_i8JqCbF9690qNOp9BxT4hm5bmCi7ARc3VEBU3TDhiDCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=mo93cKpUu35lHtLM_TKvO8_iMlamHdE2Igvm3qfE3naPSISxb_jWpKbceV7lX0a_ibDIeOs0s5DUQQPpAx74DIqvPfSYvbmRrSEpWaJHa2i_yREuEJO9qbuiBivbrByNykej-csDJxZd-BWmGbwzGNzT107fsZiZHXtPntfWbpjFQ7nAzj9fl2fRUgOOs-BwDoYzbyy1FHMq5xJpwz4VRUOGwfP2qkfowUmFLzIfEExCKgEYf14NGyABexbOVR0XSzR6MM8AoHJvYNFHJdRQuKGgu2wLFFy4IM0LY7ln_i8JqCbF9690qNOp9BxT4hm5bmCi7ARc3VEBU3TDhiDCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=p7okBkPJkspdG_z5gMMQG3pNmrHT0FIpBIHcRhPRkVF0EZQ5HwiIUyk0iVj1vqSnEmvstGM-uXVWXNFdTMOpgmWZTcOIdQo4e6CgTKvEBywHF7-UuQ4psaEOjEH1D53HkVsh9joFtEVIWR0SKCxHY385m7snN1jYpwoUjJgfJNavoKC8K-mfezdkU6IfyvT4JiFrk3n6MXF2GUCzaiuPeJnXRwWIUrlJhPIcKmwLJHLgppbDV8M-6DSbCmrTfYO4wx17lra-r9J5sCQBCDDAMIzJvaGz51t8_p2gsxGiGC5wnQhB3Eua4G_1PtV__Lud_NuH4NvrO7vD-435tHq-Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=p7okBkPJkspdG_z5gMMQG3pNmrHT0FIpBIHcRhPRkVF0EZQ5HwiIUyk0iVj1vqSnEmvstGM-uXVWXNFdTMOpgmWZTcOIdQo4e6CgTKvEBywHF7-UuQ4psaEOjEH1D53HkVsh9joFtEVIWR0SKCxHY385m7snN1jYpwoUjJgfJNavoKC8K-mfezdkU6IfyvT4JiFrk3n6MXF2GUCzaiuPeJnXRwWIUrlJhPIcKmwLJHLgppbDV8M-6DSbCmrTfYO4wx17lra-r9J5sCQBCDDAMIzJvaGz51t8_p2gsxGiGC5wnQhB3Eua4G_1PtV__Lud_NuH4NvrO7vD-435tHq-Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dnDqAOLzShFrbicd_neUFbn_cwrohR5ob9dfBmFJ4nDHbH6g7FAWlkFEDApYSvwfUyDnN3yd7sB49fd4EVF9Wd_JDbl7Q4GLj4730GfdZYLWD30buz7H0Gjw1Snos9kyY3hAIdqtqLAOVVmC8cUL4OOe1MoD2BYKPxZpXC2gz3EIEi_pP22Vxzv1ScoJ3N7Lpa1bF1dFyoW-KwuUKh1--8MGAxbKItuxNgWIBUyPq8VPRZxn2L-93YxtdRDdsrQapzJBFGcSCNNMuvvR-P_shj3EfZEjk0ukhiVZuNqwRYQ_I48KqYxei61UALbzbWeuzyFZOyOkE3JYCW2wWQLsVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dnDqAOLzShFrbicd_neUFbn_cwrohR5ob9dfBmFJ4nDHbH6g7FAWlkFEDApYSvwfUyDnN3yd7sB49fd4EVF9Wd_JDbl7Q4GLj4730GfdZYLWD30buz7H0Gjw1Snos9kyY3hAIdqtqLAOVVmC8cUL4OOe1MoD2BYKPxZpXC2gz3EIEi_pP22Vxzv1ScoJ3N7Lpa1bF1dFyoW-KwuUKh1--8MGAxbKItuxNgWIBUyPq8VPRZxn2L-93YxtdRDdsrQapzJBFGcSCNNMuvvR-P_shj3EfZEjk0ukhiVZuNqwRYQ_I48KqYxei61UALbzbWeuzyFZOyOkE3JYCW2wWQLsVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rKvqYa1KW6VFxzYv8WD7WeQDCCMJM7mWACBFi2RYPYN9CNBwHzOVzLjd2agg8ld08iH0rbg16wIELafXOwCf7KfaS039ctLqNFMP5fC-PpPwTSjJEXRirhlT5vhgH-0WRbzQzbZxfXC1JMw5xtC0H4pAIlaFM_YHEAmXQraEFRdmFBxdZGMhgIDFVS0RcQzC8l4iZCVg3a7gjxlYCMlP01z-X1UNsp5aOq2HeV2f8armRE4oAxitd6m-i98QNH8sgij74cHnxGLLhcNwst-cNtDAux63bzK_Bp1Of0xZAmhoQ7-SkC00FxpCxcnIvnBl3tcpFSGOAD5Fn9Ct6Himvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=rKvqYa1KW6VFxzYv8WD7WeQDCCMJM7mWACBFi2RYPYN9CNBwHzOVzLjd2agg8ld08iH0rbg16wIELafXOwCf7KfaS039ctLqNFMP5fC-PpPwTSjJEXRirhlT5vhgH-0WRbzQzbZxfXC1JMw5xtC0H4pAIlaFM_YHEAmXQraEFRdmFBxdZGMhgIDFVS0RcQzC8l4iZCVg3a7gjxlYCMlP01z-X1UNsp5aOq2HeV2f8armRE4oAxitd6m-i98QNH8sgij74cHnxGLLhcNwst-cNtDAux63bzK_Bp1Of0xZAmhoQ7-SkC00FxpCxcnIvnBl3tcpFSGOAD5Fn9Ct6Himvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u88ACuIYyY3_7hgc8JYBN907s9ANMPULUo9aVIK6uFZBmk3Hlvw_jF4kCDFKEql10YKmr4XQY5mACEw1CKZKmX94G1dpUuJZ-t0svmJ8-cVQecYgBQSJLBZy_kcZ_o63cAlG8_4U8ECfH-RhIFvwFMcZaP6tN0qpi52duFhtbFErJH9Qtv4okdczcAkiBXkq2UZ__xCmtxEMTktIDZ6vxW3DJk5efv3xPyPpIp5LN-tvbrsmtCJ0Mlhhf9LoyqjW7mHWqQ_n3XILJZP9qNkoI3GupZKZ38BIjXrXzXlzf0nnHprKI8efFUxXPlrCVY98j5mduHxHw4wZJamEWXeI1w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=IzxpvWRBBv7k2eH4keia3izNQC_Co01gtsEZ41e2WLwv994gGeoz6kZTMdfz06BNDzEZKGjreWRmPLivGq3WjGdxYKG5FkX8Qmgi6WV-9REANWx_-exthUETOciDYbvyGPBVkYHHvIsQnYKGL1CYOZ-G5Eu5dIitr6KlVWm_3-IZE84At3kxONxx9RnA2GeDt4FKiMpwm-Z1rt02Npwed0QrHi2G0Jh1Xy_VucYdsMXldvXb1SOELbWcyxEVvITU6-5WT0y4OiqCgZCKv0_hmjFM-SJbGkD6iCsgn-BPuPKKnh7jwKP28DsoD2xd7JWdke2tlXCqhUUddrsBbR__-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=IzxpvWRBBv7k2eH4keia3izNQC_Co01gtsEZ41e2WLwv994gGeoz6kZTMdfz06BNDzEZKGjreWRmPLivGq3WjGdxYKG5FkX8Qmgi6WV-9REANWx_-exthUETOciDYbvyGPBVkYHHvIsQnYKGL1CYOZ-G5Eu5dIitr6KlVWm_3-IZE84At3kxONxx9RnA2GeDt4FKiMpwm-Z1rt02Npwed0QrHi2G0Jh1Xy_VucYdsMXldvXb1SOELbWcyxEVvITU6-5WT0y4OiqCgZCKv0_hmjFM-SJbGkD6iCsgn-BPuPKKnh7jwKP28DsoD2xd7JWdke2tlXCqhUUddrsBbR__-oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=WJjT_LzNcAqXWDrVoQCbAVjzJEdkG6omE7jR6qn8GSjyQv34yhXqkQTeUXERktPtwVHxmGpar_rhPtF1z-eOVp0qOeNGpe1RUe6xD-YtmgdErFxupxh9B-uY7CGOePy19DaqxfeDUdQDiYx5bdtpAzjqJak3VS_cdyk7vALG2jVaCrU6gKjOZzXzycUHLm_BbMThPRY9a1FEqLy-JX_TPql-vpXvrJxWXOkltot237rTTduHUi_gYFAmmcYFBcJJd6Bmzen3njGMPmoTu3y8BKcRpN-IEDxx8byUOtR6HbHldradRqZGxRQdXtJI_3RTeVMJaIwQqZsKx34c4sVjLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=WJjT_LzNcAqXWDrVoQCbAVjzJEdkG6omE7jR6qn8GSjyQv34yhXqkQTeUXERktPtwVHxmGpar_rhPtF1z-eOVp0qOeNGpe1RUe6xD-YtmgdErFxupxh9B-uY7CGOePy19DaqxfeDUdQDiYx5bdtpAzjqJak3VS_cdyk7vALG2jVaCrU6gKjOZzXzycUHLm_BbMThPRY9a1FEqLy-JX_TPql-vpXvrJxWXOkltot237rTTduHUi_gYFAmmcYFBcJJd6Bmzen3njGMPmoTu3y8BKcRpN-IEDxx8byUOtR6HbHldradRqZGxRQdXtJI_3RTeVMJaIwQqZsKx34c4sVjLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qP1c5zVhtpLTY59MFrcAdHreBeZNb0n1BsvnW6gRbFlapkwDFH4rsTSV1N2TMh809rwsGoeOKSvzOjwYZUqoWwQ4OhdIIGNTjOeEILXCXx3yb5vDfDcyhEZ4G3rTtETZZ2TuVTViMWnThou0IpiAse7zx5zP5jI2sdKMZUWl3i9leJLFAiyR5zCVfygHmPpx6RjpJ08RyFNlqwJ85nrNcnZUAcGL_U50Uv5INPng7LAaBWFMLPjgqIxXQkTyXTJKyKFGeunC6AAmpN3ftsMOOxIfUoCRR3sNa1RO8BlfpWRu_j-Loo6MyJx2rJxPdHh4TIGJY_YoDtnCC5ZinJNh-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T1GYVld5b92ONw5Mchj70_2HQi758h-ZE-VddGNT7AdrLee-Qi_rm85S61aUrslCOF-XNDADXwu1tfLdR6irEthditvH3EnDFWsDXnszkgGm7-8TbNOZ7bJKEEFqw-dqMzljpTj1n30bLqcR27xTqDmxk91gyIgqZF_qZfYuGfB-c_lH_4mVxnfbi8bGvVmFIFhmiTowxeuRXRNk7Zh0pvviXkkxuWBnI1VNNDRzEXHzGoKRPYFuazF-hWLIzVJvso5iFgV8qMIzVSUa70MumX4JCd9uBq8Woz4qSEmlPTU2QajssBfykL9WVlDRJLUJjKjIVs3jgMWGKygBgJBOtg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=baqhxCm3WWC_3oHWdZiYWV_-Hqwl-FzPdZXuj2pPqEErAyx6SgQSKS7pvHuhWuxISur8Hysw_Hxk9Vq-zkVk26HgHYIpQcWs6JtUocvoTwzUJCfzrwJRGzR3Q2b6n6sl9hS9vt3__u_6TuJVavvygt3VFRY2LFozfPe4AF-bLjpYS89Sg7zXcDFWQKLSr8fd4EpKh0CnwsvtUuzGN-0UaIP6qML3YM7vIcl8gYaOTYNAFp7_D0J6pms_Qjk5vyR51GkxdFaNWgjAjC0A7GBhn3gKRIxcUM2KLRGx4kHu-jNTg8F2YRctJ8wcDl8dCI2oafPGWdIofSjSlDYN3ipkEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=baqhxCm3WWC_3oHWdZiYWV_-Hqwl-FzPdZXuj2pPqEErAyx6SgQSKS7pvHuhWuxISur8Hysw_Hxk9Vq-zkVk26HgHYIpQcWs6JtUocvoTwzUJCfzrwJRGzR3Q2b6n6sl9hS9vt3__u_6TuJVavvygt3VFRY2LFozfPe4AF-bLjpYS89Sg7zXcDFWQKLSr8fd4EpKh0CnwsvtUuzGN-0UaIP6qML3YM7vIcl8gYaOTYNAFp7_D0J6pms_Qjk5vyR51GkxdFaNWgjAjC0A7GBhn3gKRIxcUM2KLRGx4kHu-jNTg8F2YRctJ8wcDl8dCI2oafPGWdIofSjSlDYN3ipkEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
