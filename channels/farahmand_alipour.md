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
<img src="https://cdn4.telesco.pe/file/Ap2dIyLJJxsjTQJa2uYo3f3HH1Y-D3UitnQ1yWnV3-eyAFhB2SOBv2AF96Y7uiExZ2MurwzbgRKpW39u-IvVTFcuzTVJDFFU-X10jyzEL0D1Z0wkO7XSdbL9byqWMsiA_71d8XhiFpzo2YIsZlZPpKbx4d4Fj7a0NF-eLlbI2KSkrNI6FNxbfZoARZn9nE0yIpVSERBcSQ3YagU7ILxJo9ns7aONpe26t-kEPZlrcak59158LmSeZYMy_10somPLqv5muMONGsMkm4rV16hdkqxf5UvLO8Avt1CU7SGcjZCvkjVEvyc4WFdtJ5aL1xYwtnmPHGOv88b6tAKvcNXhnA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.3K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 05:31:08</div>
<hr>

<div class="tg-post" id="msg-6810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1M_TANJoAIQhWOyhiaAsy2jtomelBt_cFN9Y6vX2dpGvYO8to8Eq-EnDICOICxgmtSYArzVufaK5ietHCMcb_83Y_o2FThz97BS5Tftfhn6hMjTQA_1ekaz48BDjr1fLPPBT6OkRFqCLHMXFBS0hLx4ypyOQvkHe8U0vktuIopuDYSvyqcQiJUJPsvHufg9Ts-ybdg652jw_jQT_SdCFRI25J2ohu2J-E8M5wTJ7YTVli_uOJ43c0UN7Q3W3aNS8Nyo1OpSO4-wEISNPRZxLTynDqfrX2ifE3AXd_daf1zmwjSxxzScSzpFFymabtaUrb22XRZUdhTplV-noY-IQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام آگهی استخدامی «خلبانی » ارتش جمهوری اسلامی گذاشته.
یه نفر زیرش کامنت داده « جنگنده باید بیاریم یا خودتون میدید »
🤣</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/farahmand_alipour/6810" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6808">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=EJcYm06O3RU-gGvVB2GOBeLcq-4XUgvPC_izq7UmcK5LChWuaZS7aQs3pIx7KUSNRIEPCoQU6ZPO3rnJNW5ZydJTjw8-obWPBD6xHE842oiZ21NthuFmOsTIDs0sJr56x0lDp1wJfbqRVJ31O78JostGrRKokL0r72duWJrNfBCT6u7bsbKQKSztf7yQMagQhn26ZrlXKhhyzLkDogA98wt3yXaTy3FNpQcxWlfGvwLt7vntWzsTYyLeT_pB4FqtUXza59o5ycBMV7f1KhST2LhNxW67OtTLx08GH2uoG2ZcwG4A_qZ6UxQ0KpCq0r-0QeFGexVTM1bJcvBr-UDhmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d04fba3efc.mp4?token=EJcYm06O3RU-gGvVB2GOBeLcq-4XUgvPC_izq7UmcK5LChWuaZS7aQs3pIx7KUSNRIEPCoQU6ZPO3rnJNW5ZydJTjw8-obWPBD6xHE842oiZ21NthuFmOsTIDs0sJr56x0lDp1wJfbqRVJ31O78JostGrRKokL0r72duWJrNfBCT6u7bsbKQKSztf7yQMagQhn26ZrlXKhhyzLkDogA98wt3yXaTy3FNpQcxWlfGvwLt7vntWzsTYyLeT_pB4FqtUXza59o5ycBMV7f1KhST2LhNxW67OtTLx08GH2uoG2ZcwG4A_qZ6UxQ0KpCq0r-0QeFGexVTM1bJcvBr-UDhmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9CkvVaVmzpIvxMcsldzN85wp9cchB41V0pCS6D8yN7VVFB57jCL2CLRaZ-wPYLUqq7kOYq1Wt7j4ykPeG0P0SYzhtsPwXjZ0hiDDSlXDIpYW7EPjeo4AzzHKH62X_lT24ubinWBzn_KNSy2Nz5xGZJfr9AjIoiBDWia1fi3yMh_yBRl_PRXq112cZbVxiBI4PTI75lSQ8BLQd6PxCgWVXNXymZlKZXNB5IMpf4l9k3wlwxFWOi409MZQtuixXCeMNHz-575EDR5QLWwCADR3r-Y-wgM2SqlaRSpa-9CG2jRss_P7k4obMIELciHnKsheJjNzfYuXTmelrUXI193Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=Si4_GF1m3IS05eQNtkQfgKRtNdwKRfK1qrl4o87L2NnCOaEJI4RLxviw8BwXT4zeZvu-CO-uVKROaJ5EEJIrkR_WxgE8vSy_5rZX1QP2Z0nU9TUAg6aw9Osy4_x8kTDqbEB06rUICTwYbx8bK1JSg-sBROZ8FnYOdU7eB3YfGYNQ_W6mSIefsOCZ4pBYZX_ZnRoWZBIAJWBx-XTM3-fiLSHJArvSBW-6ZuQOYWt-Nx-Cw2EP-C4QZTcRoPBj9FKRwMdOggqjju_ZidPpOg_4poSEmpexPNJqVyR6s4lKDAdg7SeDM6ottOU8ohWAR54dMyXThBZ3wFxqfQOGiswANQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=Si4_GF1m3IS05eQNtkQfgKRtNdwKRfK1qrl4o87L2NnCOaEJI4RLxviw8BwXT4zeZvu-CO-uVKROaJ5EEJIrkR_WxgE8vSy_5rZX1QP2Z0nU9TUAg6aw9Osy4_x8kTDqbEB06rUICTwYbx8bK1JSg-sBROZ8FnYOdU7eB3YfGYNQ_W6mSIefsOCZ4pBYZX_ZnRoWZBIAJWBx-XTM3-fiLSHJArvSBW-6ZuQOYWt-Nx-Cw2EP-C4QZTcRoPBj9FKRwMdOggqjju_ZidPpOg_4poSEmpexPNJqVyR6s4lKDAdg7SeDM6ottOU8ohWAR54dMyXThBZ3wFxqfQOGiswANQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjttljYjeM-1CKkWnTeHaeEFfJ7Q26e7x1pUHTHhC-zMb6OfAH2kLkahxpFMj4_KVE37c8lZU9qwbSqVDRJEVXvmsoiSDdohVMCvkRvIKwvjY0iz5SbdCKPWCHM68vQcRHQJnwlNDFpMZJf0l17MvsZKSBft8-dsF2W6-3Bwyi5u7dJcE4NQAbYtBVZIMU_TO90dDZmYuF0BA8Jd4XohFBCT6Umg-el0QzR7A5gD_Wm3fgThtJJwsBwX_Ny_5ai4vWNRyBQiDnytCFXnFcFYgOsKtcE9T0EY4LFH1xcWkG2MwOoPb5gpfb8tE2aCncUHZW7WzXDScgsm-Fupqyduhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYzjxjsIQYy8NX58WCqayj_HoOPsdR4vRQQCNJfPqwcD57gFe_Q_ZfqDRGA0Z-kAI0Oge4r1uWgIJYqzDGXOsi2DOG9L95RGgwMuv3fTJxAWAv-n_qlHUY-1eVQW9UX--95PB_6T406NSV1LUbGxHu8lbqkr-1cafU9lsFIM5wJFQNYrc6_YqPBe4LM4YEpkoIwKN6rMXVBqPHs2l9aa-VYYj6fs6kOahmdD50KssWMkwXuR7i4mFVnL-Q98SorFnWKDuNklxbEW7d0fKrG4V82ZotvKYmVJGqq4jG8qGTyNwDJm3-x6hC55yjQ-35QSjYtqPMMpbkMo86gCjy_FlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZ42-yVLMJFWUXLWcGFCbl2GIOe1J054tAsBDePygZ4KzrmZvxF3s4G2jnrVvlU5EAneBtA-FwOP0c0YmvwHeT7YPow-bQJCB4k4Jj0u-OZBBEZiQOxQ0_dVWjZPeDvJa1-gpVlYT_4zIGb1PjFDJUXsuSwiCl7xtPfx0wHgcXslFL5QwifF5tQHzgHXN7g-Zh0r3Wn408ntCqgymExUxiobAJljB3gi-MWxMJnaOLgeeeXvFZ_P5kI0_C58VzH0EWG4QkEBq-vA0qxaevmMGV5O6kD9i_yviqB7SVhAxlNnb4fubpd4SSX2OObuLvmI8rOVBaBy1Nz9eWMlR5vaJw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFq2qR7uTRK4vOlxJWHsUxME7-i2DmtKIt6QlWQvS_speaAV5OJEsTIta4Jf8gm5815lT1UqVCn9DUrRe9eIeImrybPb3rKFs8lfvpqjc8dUlbQ06wjf4KQkLDGbvtMkzdCE8-B5-Ht-irqjLVeIky-pJRodqEStxr1lsjIqj6PsGDzw4syajJoB6tCq3U60ja6uY5E9QEctfiZW882B6tq0rQptRZT6JUSXlCcQBZSdKLTZwWV95j5Wmt2DoYgi1veMvdhpAEPqJaZXhYO1gd1pqAzw18eTmtNRfiLycbZPP4-r16ijPC4iw_0y0MADaPh4dPtRV575wkcWwaRGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQRAfF2odkbLJlyoBht73QRDARtK-8QapL5jwtMRoG4K5KRrt2gZ_0n-SZEA8LpxuahDWgab2gXYzdwut_vimtBZNUXW7s2AB3DHFXG5NwQWWsUqS8YlOqMCuEMnuLNOKIIgJSW-innmTDf35U26V43I6ySH-qznAZipXvJix32_BWNy85KhB12X_PG0N2ppcPiVjQdeGxi9YC0AMray7xchi6iARX6T-kDb5qaRSn32b6bVUuRaTQhpRNbcnL2ESS_8IsvoHmLZ2Yx1gtCAtpgQoi3g5fovgLguYmvSkPAbVyHoMwa4NVUHMNfhsOoNlse_x_PE0o9UjlbRvuAydw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=gyvlaCbW-KC7RxvBeDWSn0TV3JVgtQTynfoIYwtwIECHw47kk4rTth0J8HcvveLk2gKmauezjxaxZhdl8dNwZsrx6bXsfze9dVoGSE6ioSnDUSLk1qFtbuefGQHOZ9GVTS2F6og52Ut3cfAtmorJPsYQZKVc99oroOvcwNFREuE1ucbG5vsTQiPuL-FTSBo5bHalxg3D-aWptNKQCcswHHvO9rRgeYJGsMQCMhUROqCU3-ZdyJXEWGljEHfVUGNySK7VpIk2BGDDteb33EvP1LYeB0mIlV9prLGdWYH8siwgVzrobJiOf95CLwGUKQrutilItuSqqWAI9BJrsLB90w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=gyvlaCbW-KC7RxvBeDWSn0TV3JVgtQTynfoIYwtwIECHw47kk4rTth0J8HcvveLk2gKmauezjxaxZhdl8dNwZsrx6bXsfze9dVoGSE6ioSnDUSLk1qFtbuefGQHOZ9GVTS2F6og52Ut3cfAtmorJPsYQZKVc99oroOvcwNFREuE1ucbG5vsTQiPuL-FTSBo5bHalxg3D-aWptNKQCcswHHvO9rRgeYJGsMQCMhUROqCU3-ZdyJXEWGljEHfVUGNySK7VpIk2BGDDteb33EvP1LYeB0mIlV9prLGdWYH8siwgVzrobJiOf95CLwGUKQrutilItuSqqWAI9BJrsLB90w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=OBjLBV8LpytTNmm9sSwmz8tEvrSNOwtXSQ0QSB4CV-jvjKnAX3kPrqvCaSG9PdqF3ZT-T0wEYU_xDQ4TxzsslgiiK1GMHhPwObYpsk1vp5Ys_CylxVhVgV6cGd1BKjbRuADG2wPmPe_2Y_SPaENe6BGXaUtB8MgEzi_HGfatuAVgrOVrEneptmYScU5GnHLWHrI4znBQUh1XkMBbgGIzD-TJ9hSm5c3aQyoBWqwSRf4nYpoYdauBQNBp5YwGtJIR_04_qZV6XMK0Il-T_kXz8qSnDZHcmRA5-KKlfkGE1eSljB_W0AnjhTfPIyBVkweMwdTLJXBVxHlegpZMpKw8uFK1fB4eLjWUXL1bNHJ-xhJk2iOVFOKVdNpPyokjxj4AcV3WAGqOYsg3WHTl3k1HXY71L42UNOvEjUZY2SnotEK_tom-PdpmoXwa_Z4gpbkmnQMwJOOunJucDH7TNjvB2NjzYNYIheuRA0B9Tni14HzYhR8Tw5IQ_l2UtllTzKQrlCOpDJ8cYG9bythAu5HM_1E3GLiB-IEODw3uRSSPXg6MOGdYZI7amQZpv7HvqHfip-tyD98lhCKuo070T1vsEqJGwrwbhDQcYcNZ3572Q-AZq_vwfvbHImmSBGPXGHTGZmM8DnpPR-tXcJhYtKBO2XCZsfpZaWV_WVVRC_Tay7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=OBjLBV8LpytTNmm9sSwmz8tEvrSNOwtXSQ0QSB4CV-jvjKnAX3kPrqvCaSG9PdqF3ZT-T0wEYU_xDQ4TxzsslgiiK1GMHhPwObYpsk1vp5Ys_CylxVhVgV6cGd1BKjbRuADG2wPmPe_2Y_SPaENe6BGXaUtB8MgEzi_HGfatuAVgrOVrEneptmYScU5GnHLWHrI4znBQUh1XkMBbgGIzD-TJ9hSm5c3aQyoBWqwSRf4nYpoYdauBQNBp5YwGtJIR_04_qZV6XMK0Il-T_kXz8qSnDZHcmRA5-KKlfkGE1eSljB_W0AnjhTfPIyBVkweMwdTLJXBVxHlegpZMpKw8uFK1fB4eLjWUXL1bNHJ-xhJk2iOVFOKVdNpPyokjxj4AcV3WAGqOYsg3WHTl3k1HXY71L42UNOvEjUZY2SnotEK_tom-PdpmoXwa_Z4gpbkmnQMwJOOunJucDH7TNjvB2NjzYNYIheuRA0B9Tni14HzYhR8Tw5IQ_l2UtllTzKQrlCOpDJ8cYG9bythAu5HM_1E3GLiB-IEODw3uRSSPXg6MOGdYZI7amQZpv7HvqHfip-tyD98lhCKuo070T1vsEqJGwrwbhDQcYcNZ3572Q-AZq_vwfvbHImmSBGPXGHTGZmM8DnpPR-tXcJhYtKBO2XCZsfpZaWV_WVVRC_Tay7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teebaCauRlQV9MLciMxU3xDk5XZDNRMGK4qMEZHUud4aOBLpbtD7WaV7db-oxDYi9RsT3FEaFbfFY3qq0jZaP-3LLzvRz1ODjJxKMMhEv_ogkIEeYF9wsuZtkTgjkCqQhYmbznNPOOp4iah_rvEf8tTZlrJXOZjDwIJQVdWVyX6zx8jx5LqxyVnqtlFJYXjPSybP3TFph5kG3o43R4ibbtAKFwI5JyffMBAgcfcYErRFmbIRfh4Ffp7dt_3gwyPMxj-hK5HL3gtvi08aGyZRY_jXVSyMZNTDXQ0NSLn4GYyx51jzuxw7v3QCFtiwQQ3w79j98WHO0FB9_S13JdPINA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwENosq7_G7CJAJ9KrucFYNl3Uke0Xq1HM2h1JB3WzA_yoqayHk0f-h3RH1KSbhqa4NrUrXHAdaaFt2i3p36Uft3zemF0zsl4H3qtUVhq-EVd8Jvax0OaMHmKMLjR_FV08uPbY35DbNrrkXchIScauzRqFBwTwnXpu-UrNSgbJhAb0npBmeT8U_RmRWT_s77RDNd_LtMgIQEzbw2qzSd63vYIZB00QokNKkSjCAPIaqo5jYXI9fHqTBttF-qifYiiJym_LjbTXBsoD2pGtx_Ub0DJPuWOAu0Db8mGgdlaJod07VzTSvAaudhxRCTT1iZjWkMrHMty55Zpiaey9fChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMqDBz9e_nKBIUaGsBrd4_Jbg8ag9mV9Xm7I5fDXU1IRY2xQRIi1CWMBcPMprpDvUFqQpjjP3EhAdxMTgMFp2uBOX_uSBn2KU2MrCP20T_yHjNBdQtV8NJLgDrP9Uuvk3axP0Fyfpy27YqrWlyoudXT13xEf65leMzjltCLB4Vkv97OnvxbhFtCaJTB70iMqdfppltqeZbmeE8R1SVMrBhkRizPKfzKEjDmsZZ4WP39yr750FEoqWRObZR2Z9BHi0F81O6ra34c7IVPFohYt5EGRHwREJ0F6vd-5qzv-rz2wPJjZxX4j0ztmI6S1ajw0NXtEGay3oiPYzmmofCd2uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=NyThVrHLEQZujgZiu7KojTwZjZ3kPMZohWT7j-1Bk3U0GHVOJyGPEqgsHiGktmpGukca9FRT68k5q1j-US7ThdkImsszTdqx-dZk4IGRwvUQ31Z0U5KFLKhww-eug5enuu-0FO7v3b2p5ueFISKSZrO3uusLc3T8ggaBXzldJI90nVTVYZ91DDKFVFhEtjkPOwau2o7jqooJr_ANctbS-05fLzWLBqabotf6j_Yd8K4MCeGNdLSMW6WlJdWw3rwa9V3U1FAuJTC7pAU6EZ5akT8JVFRn244yRPZfUdI3Od6huv-fyWf6yGjXIjkdPJyjIf81h_0LMbr64l6tXOI7ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=NyThVrHLEQZujgZiu7KojTwZjZ3kPMZohWT7j-1Bk3U0GHVOJyGPEqgsHiGktmpGukca9FRT68k5q1j-US7ThdkImsszTdqx-dZk4IGRwvUQ31Z0U5KFLKhww-eug5enuu-0FO7v3b2p5ueFISKSZrO3uusLc3T8ggaBXzldJI90nVTVYZ91DDKFVFhEtjkPOwau2o7jqooJr_ANctbS-05fLzWLBqabotf6j_Yd8K4MCeGNdLSMW6WlJdWw3rwa9V3U1FAuJTC7pAU6EZ5akT8JVFRn244yRPZfUdI3Od6huv-fyWf6yGjXIjkdPJyjIf81h_0LMbr64l6tXOI7ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=rTtXMx3w6fm7L8NO4Nr48fQ3iCSDKQdT0UZ8aWOujVi3dfD6bUNcRDIe_6-Mr8DRAh5LqZhUvmv7qfQX1lWVAvkrIl7hiLhXmEe31j0Iw3RKf3-yO2yVhVIELvAictD41Z3xZZGWGzwFNy4aghuZkrt9YGBKxxCB_4MhQ-Q2hvhnzToozwms3YQwEdO4Y2V9H7gLfQWRFN7GKOYyANQ9oWK1tYnaM9x5_zW41OtWG2G6P1KEiGSZTsT7TmK-mGjNWBjRThBgyGkA6QTBMx95nyYbV0Y0hPPoZvN5VZ__mWKJ2P0_NypfInMw9DBPyrzk340pGs4X-hz9_21OCufU-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=rTtXMx3w6fm7L8NO4Nr48fQ3iCSDKQdT0UZ8aWOujVi3dfD6bUNcRDIe_6-Mr8DRAh5LqZhUvmv7qfQX1lWVAvkrIl7hiLhXmEe31j0Iw3RKf3-yO2yVhVIELvAictD41Z3xZZGWGzwFNy4aghuZkrt9YGBKxxCB_4MhQ-Q2hvhnzToozwms3YQwEdO4Y2V9H7gLfQWRFN7GKOYyANQ9oWK1tYnaM9x5_zW41OtWG2G6P1KEiGSZTsT7TmK-mGjNWBjRThBgyGkA6QTBMx95nyYbV0Y0hPPoZvN5VZ__mWKJ2P0_NypfInMw9DBPyrzk340pGs4X-hz9_21OCufU-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4L9S21v_seTgbV2xj3LvE4M2-Ehy9wFEpvXcg_DicZ9pgYJNqoQCFVpXnqLdE9YvX97SeT2H2m2obEfmcO3si83cU5FLFAZ2C0bDdDqSg2ucXAmScJUbBwThl_c8_WL8_8yT7E1F9DZiLK4iAFFYCeydZcztPsuhTmGHC20tyAeMPX7NOJlytRlapz6qjS9CFztOjFBY8Y9rmy4dsfpTu68-TMrd8k3vax5ryO4JDzArMU1wdHuIcjEYgxq2w8ynwZajz6gSfE6Vvt4_5l40n6EZH3RgCd-Pap_0jFIefARHJCNQIjiKw_FIzOsYjSiLdsxpUSeFn60dEw-ueTHzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=kRLeFEcnjA8P3rRuZMHaAN0HHaJkROlv8Niida7nFpxhBSRVbrpCoPtg88T86-HcIzgbPz_3oc2ArTDXjRL1tQkSJxiakWiN_mgTw8fRwh0K63gpYF0u-xC6LFNdZrYFSGa9Ucci8jY5_EeJh4rIfMsKKKCuaUO6nJULVHAzFruJd2XWpNSYbMTbm38XmA3gB3iywjSyywYn_nJuztVmfTYnMs6TLAEsSOeLAhNjVZtxU1Sx5Blj_M2vKPoHmv2n-YhcR8RH6Tkdqn174FjeYc3d7rB4BabCdJEtzRxYbSysMNijedWyjgzxxpGVwoFckXOl-KdHH6FYg5KG09yeJTxCPiKq-_b1bprtGG4B7jpJFaOJ-tnV8Oxt6uTgkVrkf1F200KMJy8yT8nGqdDlQ1Pu_A_PAuX0x0u_3gi3-PIIhxALNUdyLSO4-Fadky6L0PPpPPbcih-gjbaJyuQjEdswtSk-Rn8gv-bjF4nViahGRa7xreTTabHg6QBYUcfNel4yPYp3GKeTyunBwKTrf8VLr0LhaXp5h7sbMigO3rlWKxbszNfGYqkhfXbKjrvm6fu3qODHXCvwAk1a0n7Sby82u6BItnBSpSWEHAqByeDQCmAVqLw7JvOIKQvmI_QeGKY-bjkEb092f4xUss6h5zXK1ko9K8VbqQt47aohEU4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=kRLeFEcnjA8P3rRuZMHaAN0HHaJkROlv8Niida7nFpxhBSRVbrpCoPtg88T86-HcIzgbPz_3oc2ArTDXjRL1tQkSJxiakWiN_mgTw8fRwh0K63gpYF0u-xC6LFNdZrYFSGa9Ucci8jY5_EeJh4rIfMsKKKCuaUO6nJULVHAzFruJd2XWpNSYbMTbm38XmA3gB3iywjSyywYn_nJuztVmfTYnMs6TLAEsSOeLAhNjVZtxU1Sx5Blj_M2vKPoHmv2n-YhcR8RH6Tkdqn174FjeYc3d7rB4BabCdJEtzRxYbSysMNijedWyjgzxxpGVwoFckXOl-KdHH6FYg5KG09yeJTxCPiKq-_b1bprtGG4B7jpJFaOJ-tnV8Oxt6uTgkVrkf1F200KMJy8yT8nGqdDlQ1Pu_A_PAuX0x0u_3gi3-PIIhxALNUdyLSO4-Fadky6L0PPpPPbcih-gjbaJyuQjEdswtSk-Rn8gv-bjF4nViahGRa7xreTTabHg6QBYUcfNel4yPYp3GKeTyunBwKTrf8VLr0LhaXp5h7sbMigO3rlWKxbszNfGYqkhfXbKjrvm6fu3qODHXCvwAk1a0n7Sby82u6BItnBSpSWEHAqByeDQCmAVqLw7JvOIKQvmI_QeGKY-bjkEb092f4xUss6h5zXK1ko9K8VbqQt47aohEU4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ev3gnYGIVGNzMi5-lsopAY3LKqVUlkzwRHmYivPecQg8vzgArn9FVEgdADZZPwImdR-OEhFzJl1MalE1RmYWMFyNFF2P8OfdOgerkwPY28fNjpuRI5CiYt5-iLrba-Fka_q8LjYbJ-wAhRg6erNx8k6j-EJ5m6oE8nBTCaVkf6E9QoNOT1qcpnP1W63FU5-H6S-eFzKn6oSezjlUaUpxtujRFYXaovBeunPLKN-QEbjGk0w2eylN0-KFNBnNKHGCTPNaEwZhTbzDpJv8BfKvWzM8sGIosPbk6FdCr9ydxFmy7aP--0fzdhqFbpDQ4cvKU7256nWPgdXqa8GQlQYhNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ev3gnYGIVGNzMi5-lsopAY3LKqVUlkzwRHmYivPecQg8vzgArn9FVEgdADZZPwImdR-OEhFzJl1MalE1RmYWMFyNFF2P8OfdOgerkwPY28fNjpuRI5CiYt5-iLrba-Fka_q8LjYbJ-wAhRg6erNx8k6j-EJ5m6oE8nBTCaVkf6E9QoNOT1qcpnP1W63FU5-H6S-eFzKn6oSezjlUaUpxtujRFYXaovBeunPLKN-QEbjGk0w2eylN0-KFNBnNKHGCTPNaEwZhTbzDpJv8BfKvWzM8sGIosPbk6FdCr9ydxFmy7aP--0fzdhqFbpDQ4cvKU7256nWPgdXqa8GQlQYhNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEj4TZxe9panYzZDLO_q_hQf3eAqTDmmXA8hgDumBbnsBWHCLDMkluMb4dZrgPIr2Hu_1J_A6MPuE2r7_dwja-hov6ZMfEyd0ZKeGwYVfQui87T68LUu_2Bn-et_kyzniJifMpWHkhIfiV-Bo-hlFRwOy-oZuJG4b3YycDRrnRyt8VZ3xxYGa4IYDGtC7ivNY-cMrhF_wW22vplLmhaJ148YS7avAL5K1wgQ2SOI2rIxh-WNypLfL58UDZOt8773NRdVmzpTSMrjvzhqWWWggap0kIwzVq_kETF30z63IWdv7626l1NYDAtoIOd9_hj3hiF5bbT2tj7wu7aBdyQxww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=gm0T0trDYqg0i5iabCJvymV7Mtp8P2JjcrnzUcs5KGjYNcGiCmOpODCxyiijYKlavGpSQYkvpMCL0v57jwNfdmU2rRE3idC0brN8R2s2YFfPXWYe8QJJ0AMjii6TrTu4AhRiBSVQ1_rsr6GxUqv_oSJ-9wHvI2x5-T1YGPnYNRF1VzdQsuT0hfxFC8I3mC2odd-cudd-gN0kHMN_U-ff199WMtxDFjf1g05fOP2fT5JBM2AgAfUIlNxJMBUzME6s0lY3yc5A2K64vk8RmHkl_q06y4XHdRPnbVr2GVuBK1DrdMiCyH3JyJmuoYsfBWWQ63nlz6C3I3JP98db95g8rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=gm0T0trDYqg0i5iabCJvymV7Mtp8P2JjcrnzUcs5KGjYNcGiCmOpODCxyiijYKlavGpSQYkvpMCL0v57jwNfdmU2rRE3idC0brN8R2s2YFfPXWYe8QJJ0AMjii6TrTu4AhRiBSVQ1_rsr6GxUqv_oSJ-9wHvI2x5-T1YGPnYNRF1VzdQsuT0hfxFC8I3mC2odd-cudd-gN0kHMN_U-ff199WMtxDFjf1g05fOP2fT5JBM2AgAfUIlNxJMBUzME6s0lY3yc5A2K64vk8RmHkl_q06y4XHdRPnbVr2GVuBK1DrdMiCyH3JyJmuoYsfBWWQ63nlz6C3I3JP98db95g8rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dauow18RiV_uv3rCznF9DgVfnJtiq_FufAfwhBEvt1tPKU3UH2Dm9H_KVkpYdJ1SIuisyxHM6s8IyfJJmH_-sU2IE45SM70EGJ3JYE2W_-HDZWBcXrtqUYj_JjpJs3izhQfUBwkekVjQMfzq3NXD5H9O56EqSE8nKFQkaIIYPHrZ_BcbJMsDPscL7JzE-oT2lxqpxCcKQrhpHLzGOfhpSZ4G-6cT1s-oywoUL1ERJBVKnLWcUtu-A96oV6Gh7czfTYMq5elb0KaVMZJ_0sGRfLEscGduKfY1nVS1dM4FeEUeDlOTyO8ly1v7xdXlehExuSX5YtfpVUeHNEu0DdHohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dspOcOYtdiAEYP_zzwVRgi399QU9n7-kXNuogwOT97H50ufsjD-maw4y9h7hSON9DBpsMcNXnMIcoB84sX6Q3V1Yuo1Z05vHb0LdqtPPzNXMAg0WhmgRwd0na_yQTeKwZGh0MhXMfLB22ZfamQjCUr1qJIQ_Fi9Gh7pcuSmgbHRG9LYc2_oGXBk_6F3pYEOJ1Af-r4gvFkDRTqjrWlHY8bypNi7wk-F5UcrueZxQ9Y3lGKB7VNa-QJPbAOnowfHw33Fakde-POHGwqnhCuMJ4wBirAThgRLE-B-V9vv2wdspr4bn-q3wO81JZuZ0ax2t4-KC2-fbohq1UqOiEAcXfQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=qONWFFTE3TNUx8rgY2ILaC4zBcxXf5uZXGoJwz1Ccfo057_fZKGrRzQpAGJwe1R6x3nqxnFczZeH3fHNljeIn1F1nzrF1W5DBg9X-JdHYeYFQX68VFAzoiZOulT-733Wyj8XYsn_dDcdDa4LjTrsN_gK9WpwTPQNQxZPrJ1LThHOd8b7faq5wzxOB70MRNyIcikDV9j7wi1w6Uog9pmWNdudpxA5k92OjMSLz85oQ_sP4UZRhsD6DRftj0bt9OBtvBTligbgh5naI-ZfeKcrLWNTqePmSjoOPycQAzojfhdZxhFSHfBGM6nCPtsxpxU-itq58xiLBagrcmht5QZTBVtO6o09JvtPcSItgxdodkKP01CEJeqekWdrplD6mh7ETeE8bTjIEg5PIvC5no2POJtkV-qqINKUsTDsgjaNr_PiDkNRH4aNk8ejMyin5w1gGNDZRvhkY8Q-SMT0QIle9ufzQzicUBydWNdrQE7bTpA8KinzLTgF5mMsojawM9OUGNo5VsW7xsw7RpRMKQfp6DW3lM_tazDqp4ZpnoVWybDpwOA1By8EGyG_ghaViDdehwbB4NE5AbG-rQA1YIGQ-0tk5t9883nJR4TkgUt6CacLIaiitgLly31Frv9bOlmbGKkxzVhTlVUl6ynRn6aJMcxDyGb8MJ1wCCQ4eL_OTTM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=qONWFFTE3TNUx8rgY2ILaC4zBcxXf5uZXGoJwz1Ccfo057_fZKGrRzQpAGJwe1R6x3nqxnFczZeH3fHNljeIn1F1nzrF1W5DBg9X-JdHYeYFQX68VFAzoiZOulT-733Wyj8XYsn_dDcdDa4LjTrsN_gK9WpwTPQNQxZPrJ1LThHOd8b7faq5wzxOB70MRNyIcikDV9j7wi1w6Uog9pmWNdudpxA5k92OjMSLz85oQ_sP4UZRhsD6DRftj0bt9OBtvBTligbgh5naI-ZfeKcrLWNTqePmSjoOPycQAzojfhdZxhFSHfBGM6nCPtsxpxU-itq58xiLBagrcmht5QZTBVtO6o09JvtPcSItgxdodkKP01CEJeqekWdrplD6mh7ETeE8bTjIEg5PIvC5no2POJtkV-qqINKUsTDsgjaNr_PiDkNRH4aNk8ejMyin5w1gGNDZRvhkY8Q-SMT0QIle9ufzQzicUBydWNdrQE7bTpA8KinzLTgF5mMsojawM9OUGNo5VsW7xsw7RpRMKQfp6DW3lM_tazDqp4ZpnoVWybDpwOA1By8EGyG_ghaViDdehwbB4NE5AbG-rQA1YIGQ-0tk5t9883nJR4TkgUt6CacLIaiitgLly31Frv9bOlmbGKkxzVhTlVUl6ynRn6aJMcxDyGb8MJ1wCCQ4eL_OTTM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fLfqOjpKMC-J7Kg_UfgNghz4wFPZyv9Jpyg68MuZGNbk0k6XNMROsESAflI88Mxd2LDiR6wDu-N2QO8ek6bDdMnNKMZVyAwA-SWKS66azY1GfD7FvKkMo6CNWpUp2fsvjEADtuWju6YMauGLLlD9bT1NPsCIey0nfwTI_R56qgtyLUraBteYvByldoLqjQ9UQUq-WVtxMRhy9CfxOa9oJTl2rkqOVHKZ0N3KwzA7_32mCO-axhm0FqbM4b6Az9N5y4XER9gg4VGWsK3G7med39CsZIxjuwue9r0XFDo96OKkQjMGQO9nb-ZI2He7KCDwfvg2vGJDaRMhYaKtISW60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlOFCOzxBhO-ge3z5nYxmZ54lF7_oX4-qdCUv5t1ClMeUCZuRpEerxb1LUOxH11DiO6BepAlMHkwY2u7PsUs6s_C2KsFnWgSAxR8qUBKwelB702JDy937C-HE8Hw0niUFVa3CkfXRx0JAy9MGDbnw6fj4Y_bJaFVrerxAKxsDH2dAmKbEi_FDONU5vZtbSbYQnr1706OSwHRPm78Uy_FnL6cosSeSypwq3q-zdFWRZKosfXq5g2-gVOiG6WAvsitDA522UEoe6niN387zXBvXMjin6OrEy4hBs2Gm79qjxhmZr2HsYcohk4UYAsfYKed_nYkxLSY9d-EtvQgJP3grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=UTfUpDqIz-SfIHPckgee8c7IhSyoEow_4mcNUedfaDIcy8J5PVsa2NB4ypnrMFFR0X2AxWqVo8FABCu6qn6m2IckCeaJIDA7qHJDDy_b7c5EgMpTY30GAbiIBe414l5EJ6Fzql-8WHmzFqOxPkkKFZffdJ302YwF03cS2HdLoXtr1Hl6z1aQIFCVgyglcWZeHVM09Faeck_PkbDsbKIHNljIprbd2DFE853To2IK5zWRD3O23ui7prI3bDVkVE6HjKJVCJJ7kwsrQyW16isfxTcE5O5s9V0Ae_VZkXAuf7uLXftwehRNjHTDXiBk9tTbhWcel-djM26CwNB9npIJqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=UTfUpDqIz-SfIHPckgee8c7IhSyoEow_4mcNUedfaDIcy8J5PVsa2NB4ypnrMFFR0X2AxWqVo8FABCu6qn6m2IckCeaJIDA7qHJDDy_b7c5EgMpTY30GAbiIBe414l5EJ6Fzql-8WHmzFqOxPkkKFZffdJ302YwF03cS2HdLoXtr1Hl6z1aQIFCVgyglcWZeHVM09Faeck_PkbDsbKIHNljIprbd2DFE853To2IK5zWRD3O23ui7prI3bDVkVE6HjKJVCJJ7kwsrQyW16isfxTcE5O5s9V0Ae_VZkXAuf7uLXftwehRNjHTDXiBk9tTbhWcel-djM26CwNB9npIJqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=CIkoDW0JEKzjL2bedbhTU4fbCkheQR38pIBhoc2l_UPMKexRy0yG3J9eBq5agTAGFDFtDfdUk26agzawh7iHTiHtFf_laGpyJTys8dTcXG278eGCIakeqxYofRuhgHIACCKLYyqVlx9DgWUNAmtpRWYTucN0V47Tne6YlpvAZutyxdS1hD-HNWuyn7BjMMcg0RCwfxW4CtimCmEO2UbmMFrthgkKkkbAx2Am_sttjd79GbJXRYlF6Ui-acDUCoALlgldtft3AFXv18NvOPNgUhknJQ--RLtUQlXSFv5XzgP1YdwglLGf4lzTWuSHlIhinJLfyLUT0PhUy_LZGctmPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=CIkoDW0JEKzjL2bedbhTU4fbCkheQR38pIBhoc2l_UPMKexRy0yG3J9eBq5agTAGFDFtDfdUk26agzawh7iHTiHtFf_laGpyJTys8dTcXG278eGCIakeqxYofRuhgHIACCKLYyqVlx9DgWUNAmtpRWYTucN0V47Tne6YlpvAZutyxdS1hD-HNWuyn7BjMMcg0RCwfxW4CtimCmEO2UbmMFrthgkKkkbAx2Am_sttjd79GbJXRYlF6Ui-acDUCoALlgldtft3AFXv18NvOPNgUhknJQ--RLtUQlXSFv5XzgP1YdwglLGf4lzTWuSHlIhinJLfyLUT0PhUy_LZGctmPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FFSjnFCefryqPeNzwPGo8dO_VhFMbSErtj1nRv-C9WRIUg-MvuXOlObSTNKY2Y9hEpKh3tq-EGe9DQ-Fi21ASbV6sto2nPMP3EHg0P7EI2GsjBnCf8m8IYKBMYVfbhKtywhkWVjaeyMGABoL9459YT3GtQqJgJ1U-nyBEVaBZt3wVankhuC8rFbSd9Xl5JxKm6HWM36ibnM_6Kb6JqwoBZ3lRJIBX58fNr5560n4ieKa97SoHEH3XdtlW8XASnu2kVsNgqmUy7Txa8QkSteXpLLddHMOu3VlQc8CfISBkdRp09afxCkRZ2hDWSDNJIjUaFTozZ7DtNp6T_V5lKl76A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FFSjnFCefryqPeNzwPGo8dO_VhFMbSErtj1nRv-C9WRIUg-MvuXOlObSTNKY2Y9hEpKh3tq-EGe9DQ-Fi21ASbV6sto2nPMP3EHg0P7EI2GsjBnCf8m8IYKBMYVfbhKtywhkWVjaeyMGABoL9459YT3GtQqJgJ1U-nyBEVaBZt3wVankhuC8rFbSd9Xl5JxKm6HWM36ibnM_6Kb6JqwoBZ3lRJIBX58fNr5560n4ieKa97SoHEH3XdtlW8XASnu2kVsNgqmUy7Txa8QkSteXpLLddHMOu3VlQc8CfISBkdRp09afxCkRZ2hDWSDNJIjUaFTozZ7DtNp6T_V5lKl76A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MrHCKHUaBnCy14u0hXrZERsc54wmpY3MsSezhQXRTRztYWGAHcTrBV6VXiO-t10d9aDgoTQsi7X0yQCBwmFViloU9cVS-4eefOn6M1uU5QfmFvDZCQLS3CciJ6ZQg4bpZbDyTS70ozXaND9NfkZjSCM3ViswnJ009aiChwSMPIisbp4dh7xVL-BMvnFyQpqYRm7izF1x-VkrmYG8oqbN-AytLLHPRS4U4lxzJ2WFqK84B8AxPYRrcXx3003G-x8g4HCqLSpjTPENIm-yh9rYXWm14YpbDrZvuKpUDvsk0-y8fmXiUiLFHmU1L9vY2OCaxun7gNPMpJww_I9cp6KRYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBroxBq93oWrI7_nsi0T8epfmVI56jjXn8zV_3icEXYb8gkryJdCv1dSHvFh12aDCuwSpecQMEL_5CVjPUjqkQrZqjXIOrOeUz5DckmrqQ1R7QY0QEi18xvPBR9QWyy0pAo6qz2Ntz5lmLLdMdLWg3TAXdQ8aH11Dua5R10QXhLkDZi6Fh-n7m4xrqZN0HTbwJ8wDNs_7aBxV4L65UfFEdWCA0Jy2irBWGCD77DuFPdV2g-fP1dIfCFrffW_I3oXGiUqut7bljhcwr2DP_oBvdu1e-DNRQbITihyTQs1Uc8xZqvN63Tlp5zvu4vy36MlHEop7k803MYfBhB1qAYIwQtMKo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBroxBq93oWrI7_nsi0T8epfmVI56jjXn8zV_3icEXYb8gkryJdCv1dSHvFh12aDCuwSpecQMEL_5CVjPUjqkQrZqjXIOrOeUz5DckmrqQ1R7QY0QEi18xvPBR9QWyy0pAo6qz2Ntz5lmLLdMdLWg3TAXdQ8aH11Dua5R10QXhLkDZi6Fh-n7m4xrqZN0HTbwJ8wDNs_7aBxV4L65UfFEdWCA0Jy2irBWGCD77DuFPdV2g-fP1dIfCFrffW_I3oXGiUqut7bljhcwr2DP_oBvdu1e-DNRQbITihyTQs1Uc8xZqvN63Tlp5zvu4vy36MlHEop7k803MYfBhB1qAYIwQtMKo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=WA3YnceiEwElMPqd94U_1aYJ8wQZAGb0rFzwhr2xOfm2Xmaya9yrL2d8NzlxP3-vKUpBEtp-abpSBz3NWA3f8GWD9of5q2hHIG7dSeVqqvi9Ep_-5pGypSjvyBniMDdbR6Hb0RLhizjpDtrgsdVomqfPc0e9OWLS0CBEeKJJxhON1sJqLq0fpOzw7shB_ipWr6dBsh9W5gzOjiYp-FQCUJgBUYIcJ4L_KLCYzq-R2PASEcEanX1K9Cvu5JoFzfJURjfoVeOoHPK20emSF6-KHj8-nkUwiJBOiM9gzea9fqlEfSA2IEvclIQSJMW68aRpeRMahriy420dYT5Yvk5FFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=WA3YnceiEwElMPqd94U_1aYJ8wQZAGb0rFzwhr2xOfm2Xmaya9yrL2d8NzlxP3-vKUpBEtp-abpSBz3NWA3f8GWD9of5q2hHIG7dSeVqqvi9Ep_-5pGypSjvyBniMDdbR6Hb0RLhizjpDtrgsdVomqfPc0e9OWLS0CBEeKJJxhON1sJqLq0fpOzw7shB_ipWr6dBsh9W5gzOjiYp-FQCUJgBUYIcJ4L_KLCYzq-R2PASEcEanX1K9Cvu5JoFzfJURjfoVeOoHPK20emSF6-KHj8-nkUwiJBOiM9gzea9fqlEfSA2IEvclIQSJMW68aRpeRMahriy420dYT5Yvk5FFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX9RraHGL5j8YWtwBwuqv0VtE_8bVRw8dIQOQlr1j7LSiwU6T1Y_Jspn1AP4pwzRmlLm9bUxsotFgWhiBo1oosO9dN11ZHizVO60WdmCVqXHDyme56bUcptJVwv8t8aXknjakKGCex2SCJwLaimud-CAK3iP1qQ47Dau54CjEqXLML3QIRtyj1JQkij1Lvbd4GGW9v-XLRNU3LY22h69LGm4xovkWdexBU7xCmEcodmi8q9bO4hdYWrCqwhuaWwRBOa2FqFb09zFniIevybkHXDYjKNDduT5oIm_0Ggu42pNoEUzhHcXggU1xCyiA0lFwSjop_RhqiExzqEoMmpDTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CthD3j-_zhGB2hjyp6NvxPtVpReETuANRUHju7d2OLBwVb3t35G7FJfcza32Q0r7zaXJX3K4fyqV9ZZQMKESuvku7c48uzLmIvsSRWKu3l8JpDgUM-sSEJnBP-Px-qdpLDVULUCgb3EliX6xFd1RIgufA0Cu7kjmF8sbn2Pfgo2_IB3zrXWY7ZPrYV_UNwz75oui0qGcyjiB0JafgrYNVc41RgPllGgVsu91hwcovcTv3YHCE0aXGKzfL4OSp9Mwz4r1ZpBdlQNG2zGlOoId1Kw-3hYwXi1eI4lt8Y-BRv94S2CfDp7aTd7BTvcdGymdmnyDXvTXja4_AOfRySqnk6Ce57XinL_PtPjyqUWuA5QAbDVkU3qprXJ9Nrk3SuNHmRT-874ueW_AQ7Obvgv6wJ_7oAY8YKebxoIUSjnTuXhAvrzUcGsoOqh1pSLliWoEyJB64yLdATIjcbZIUt4sT4N-Wm6BoVmzUt0Gi6rNdg0VgQl0IpoQmBkuP2bWo4lWg4cEruAJtL_tczR_HBNx6MO12oonxXj2EbB6S_66BRHz2DtZ3z9Qz1BlmJ7_CWCnkdcwG4dIyZLgD58PdwKeNBEh_nAGilYS7HQE1qRvJ_k15oPjwlPjHPfjf1vEgKxFgJx1tH6I9hvZC2BXnv9I3tZ06e0zh4ZyGJ4yHlMxpb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CthD3j-_zhGB2hjyp6NvxPtVpReETuANRUHju7d2OLBwVb3t35G7FJfcza32Q0r7zaXJX3K4fyqV9ZZQMKESuvku7c48uzLmIvsSRWKu3l8JpDgUM-sSEJnBP-Px-qdpLDVULUCgb3EliX6xFd1RIgufA0Cu7kjmF8sbn2Pfgo2_IB3zrXWY7ZPrYV_UNwz75oui0qGcyjiB0JafgrYNVc41RgPllGgVsu91hwcovcTv3YHCE0aXGKzfL4OSp9Mwz4r1ZpBdlQNG2zGlOoId1Kw-3hYwXi1eI4lt8Y-BRv94S2CfDp7aTd7BTvcdGymdmnyDXvTXja4_AOfRySqnk6Ce57XinL_PtPjyqUWuA5QAbDVkU3qprXJ9Nrk3SuNHmRT-874ueW_AQ7Obvgv6wJ_7oAY8YKebxoIUSjnTuXhAvrzUcGsoOqh1pSLliWoEyJB64yLdATIjcbZIUt4sT4N-Wm6BoVmzUt0Gi6rNdg0VgQl0IpoQmBkuP2bWo4lWg4cEruAJtL_tczR_HBNx6MO12oonxXj2EbB6S_66BRHz2DtZ3z9Qz1BlmJ7_CWCnkdcwG4dIyZLgD58PdwKeNBEh_nAGilYS7HQE1qRvJ_k15oPjwlPjHPfjf1vEgKxFgJx1tH6I9hvZC2BXnv9I3tZ06e0zh4ZyGJ4yHlMxpb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7d0qQvJSthdOkB5eXYAGt0wiHF4IbEREESikG7KKYrG6HlS82hpguXkQe7XSc9ECdfhi5HYD8cGEk8iyh7xldr-gxOcxZ9PyI7E5XqZeSnIY_o5g1eDDFPIAbjAV-fmhM7w444k6xM7Cg0187Edf48DtCm1jLV4SeW9SnL5PGCiNL7SlGlWtNVjnvhq79fHL5wxqMSJluedsL39VZPnyWcF_Osm6JctaUqrQ19YJ6lQoUS5t7lgWFXPJNOePE55Urqox75nvIns2ZszmN0o9W3YvQD3ffIsHKJ8ttKmmWd6av0bUdluSq-oHwdvax7iywtx94JRMaeGiVjcgoW4Cg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=o7PLL0PweB_wMNQDVI-S_0SpLt5dJnM8JU2gCry04KNHDQ2vBDXDW-wQFagD7-X23btMZqtGskTbvH2rd4BEIy0uODaRz6_Afc_tngUq8pqXUgvq45JT0J9kWxvn5jKC0AnOpMpaD9CKYIRiGyyiSpeK2zylTLKjFHleJfI-rIHHpxWvjEsHGM5_WXOFzYJyh8fU9VwAp_DpqI7iKYIbDoUfT36vk0JUlSh9V6u4CddYr1UIvnAJ8xblgPxCHut7zONIi2Qfo1yMpiEdebcxmuaQ23YWLlFh8MxCNb46xm1A-rMOp6WWvsG0z0vgC_7EJNz5vaRM1X_Lcv2XJRFXuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=o7PLL0PweB_wMNQDVI-S_0SpLt5dJnM8JU2gCry04KNHDQ2vBDXDW-wQFagD7-X23btMZqtGskTbvH2rd4BEIy0uODaRz6_Afc_tngUq8pqXUgvq45JT0J9kWxvn5jKC0AnOpMpaD9CKYIRiGyyiSpeK2zylTLKjFHleJfI-rIHHpxWvjEsHGM5_WXOFzYJyh8fU9VwAp_DpqI7iKYIbDoUfT36vk0JUlSh9V6u4CddYr1UIvnAJ8xblgPxCHut7zONIi2Qfo1yMpiEdebcxmuaQ23YWLlFh8MxCNb46xm1A-rMOp6WWvsG0z0vgC_7EJNz5vaRM1X_Lcv2XJRFXuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-YDIav1iMi3cL003NykyLfKl6N-7JoPh3-ifcajrny19HYXGPm0MhQ5Euz4bbiRLqxZNW3FtsStJSnnWk567fpGs75cZDXLtw3wf0ILyzeH6qktHi_1JxcBsBE_5yH2FH9Xat2pFuPxXELec5w9rM1TZ5XGr8Rz03Qf6ngWM5c6JzMyer4KvBsyFbHjENrOU6tHgGZNY24fBbgwrWUFQx6kSiCGUb_liM2xMW5-YdKbwhAFKgcrm-RAKLkldYp7c8e4d6DGeizgU8wzILh3xayhgF1vRNnFEBFBIBZr7JWeFQZDCi-LYvO3p56EzVA4LfseRFaILWRSYQf4XWT_UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4ReA_q-U6Vynp-T4V1aGOjOSwfZCxPJPekjZNuqAgCzlDb9AFXyXVsLCXK2gULSpvg_0edMU6zmpijuCiUyuFi6XuO7L0KJPgno4x1gqAJxQM1RuoaSpvt9jKP8HJ4LOXK0-jIWYgYcvpVVocxLRvPPeOXR7Ach8C2mncEqZ29krhtrxpe9tuEW0PQV4sIX7i68kP0QihTyaVIzwaDILYN9P_E6Uim_OHzC0eb81kcxcxCAqsoqqfqKUlfuDo0p2rfGZuSDeiKJkMqZ7E8d2Bn_GG0J1jo7ETKH_xtvRMnmus3oq9Hfn1dI8TP7fmLBq2GwisSYfxeH-2dOAORm-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Et8yZ8tyNhLnevagspiQwnvTIO99yCamssuhumQSjIkH-oC7cRk1i48N42RfycSSsYt_llijvuTy_91jhmlgKqpDcL3hvDaKdPSb8LTazrr_HDIbZDS_YY08VFsbRwJFdAYtodydAFfOYBnnEKDB8a03n87RySx0jA018EqoaskiJ4R6NtIhdbcvzCnkxqyoKn89sXm08S7TRSJ28HV5l1jhgqriMQHz8ATamt3AXTpcxdZt808_DCf3U8NOQ9Rl8_QgYsjX6aUliyjNXW_E-0HbtMn15kI0T2DF3sNkvfacSwWl3meJ5umjIn6pz8ZsyMb_0vbfrYNkFXW3qPRqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=CpuDKVPfPuzKdHbVTX9lOB2ETIFBBmXg2Jr6q9Io735VXV_L-d6F9hUlZEhVsxu9N8GAH6K2-eQ6rT29Bm1d3b5jmlDDAs9BDenpXhtquLIDVAHU7cogOlDBpceNv7qqOcTTWRQxAJh3axEBJ-6tjF8mv7l7IxbuhgGr8Yx2TRkfW-ELBU27dpmmKA4k5CoXEniDDEntndwRHQLf1lsC9dkW5BzayM-qw80vMXUpLN-yBqzvu_Vq_J9IENMv_e9HrsK3-I9oWjUoDcsiER5S3_H_2jgg8lYKbvVoJt5dLFmLftle5-1toUZ6m8F129JC2p1BeWjeZK8dYCeBF0qxCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=CpuDKVPfPuzKdHbVTX9lOB2ETIFBBmXg2Jr6q9Io735VXV_L-d6F9hUlZEhVsxu9N8GAH6K2-eQ6rT29Bm1d3b5jmlDDAs9BDenpXhtquLIDVAHU7cogOlDBpceNv7qqOcTTWRQxAJh3axEBJ-6tjF8mv7l7IxbuhgGr8Yx2TRkfW-ELBU27dpmmKA4k5CoXEniDDEntndwRHQLf1lsC9dkW5BzayM-qw80vMXUpLN-yBqzvu_Vq_J9IENMv_e9HrsK3-I9oWjUoDcsiER5S3_H_2jgg8lYKbvVoJt5dLFmLftle5-1toUZ6m8F129JC2p1BeWjeZK8dYCeBF0qxCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZPy67c21-pnmPV37xAcJ7_baELT_xSFJd0K0CEenPXM53jkKRTFchbv5LU7CE735B0Ey65N0XtgbZHteoG9WrPCZCq-_UuGvUChAhR9fv2f0TAX0SdHw4BxWNavn8J9VAcstdl79nB9rt_wqNCDbHcAQK37IFWJr2ELDbcrRoZBoyxmuGY0ag9U0ka92IJ3UKEX7Y1sVdiTP2BunJtm40wj4MLp0piNhYfQRqcQ7pikRMTNPfPua9S1JLtepR2KgpoGYo6yoiPjOdYsq4SEqTiymd3ISWeIspJex5vQJJkrMEPB1X84fGbF4jvOmiwEZNNKsrp6CYsn68WkmcK-_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuxt6CEY0leu_K4a0zlvX7UNQFE5CmJlTovNTO3t1ffaVObLxOUo37sy4o4jCGnghHGaIIGp2qjcl23AmmhYobwbwjy15E9kagbiQmnJ3kMyLlK0CtJYFvnjKFrEseWjQ6XMxAPK92XeQkeGMVY-UubedzFk6bXaFJfuhyI649K6Lb4HHbucdxoi5hGxNNJCjLaun5gpW4gXNIdpE9w-VtDZsehkPILi-XcS5wOD-4kXyNXg4OB8-dBj01k0fxVFOdD8EO5V7APmoAZyjEuYtlJWQYUWEr22MxpXcNw7B7gAJwSrU0iSGNvVAfPIZTeFkGWcJdtlyn_XDhGDlHCitHQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuxt6CEY0leu_K4a0zlvX7UNQFE5CmJlTovNTO3t1ffaVObLxOUo37sy4o4jCGnghHGaIIGp2qjcl23AmmhYobwbwjy15E9kagbiQmnJ3kMyLlK0CtJYFvnjKFrEseWjQ6XMxAPK92XeQkeGMVY-UubedzFk6bXaFJfuhyI649K6Lb4HHbucdxoi5hGxNNJCjLaun5gpW4gXNIdpE9w-VtDZsehkPILi-XcS5wOD-4kXyNXg4OB8-dBj01k0fxVFOdD8EO5V7APmoAZyjEuYtlJWQYUWEr22MxpXcNw7B7gAJwSrU0iSGNvVAfPIZTeFkGWcJdtlyn_XDhGDlHCitHQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=d1IWqeYzKoAkLMMqzVFSuknbqBrSsNEHjLfxf1wGzPvr7gry6ayaRXiQ3vze4MtgRj0-mxvrAYb0xsXz4uyO5ZdJMksgunJcQQdMZnIkMNXit1sjB6j5JbXzA_EKFjXTvGrkNl5qL6_DdUXIGno2KoEdUsz0jE2OtEMpGvRaDJ162DPwZdwotNqT7SczLrlKJmoSGdHuFAbzVXkrmF5hNyjhSs0Nbo_Sv0i93bNf_p7OEBLEdU8QrHp_6LP1A7Dq7k_1JJp568d3j9FDTeAFSLqU9EGi0xWe5v-7I1Ap4qBG6AwYpwKF_eUYqDPdoWPkXrlI21dGwSMoOdiu0_1xhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=d1IWqeYzKoAkLMMqzVFSuknbqBrSsNEHjLfxf1wGzPvr7gry6ayaRXiQ3vze4MtgRj0-mxvrAYb0xsXz4uyO5ZdJMksgunJcQQdMZnIkMNXit1sjB6j5JbXzA_EKFjXTvGrkNl5qL6_DdUXIGno2KoEdUsz0jE2OtEMpGvRaDJ162DPwZdwotNqT7SczLrlKJmoSGdHuFAbzVXkrmF5hNyjhSs0Nbo_Sv0i93bNf_p7OEBLEdU8QrHp_6LP1A7Dq7k_1JJp568d3j9FDTeAFSLqU9EGi0xWe5v-7I1Ap4qBG6AwYpwKF_eUYqDPdoWPkXrlI21dGwSMoOdiu0_1xhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=uAAc1yvFHvWIlaAVv0iolnmYPYhLPr-P5Eeib8X6a5KUFdoqNx8rODXzKgiHGyWcUbceFRJZJnKbz5IAHig1_vJbi61y9s0Dag2y2u9N4YWsX_hGstWw5q4lDqUXLx849Jsvz5OClr65KxkK-tRGXXaeo2pOvbxwOfX3BhcIxNVmAadeUavJlV6GF-wjsTBGnK_8w7HUfm-bmVSYEH8SSvfEbNQ4R0IFjnGV01570SlUaz0_Learhe2FIQMVTcCc-dwajMtvSa_FeMsv1c9QnsRY-Iome-hApdM5V40B2bTIEVqH5J_6xLj3M6-rDqmqaaqa858-Zwvu_p_-oABTRybHY_IP_9Kgn8bg2ToW8tc3C7Zk-L0iZ3Tbh1bu8tkTim9OzIrT2GFjc7wgANlHQ69MJwWoB24ns0dyuXHrZoRZ1smm4Tn0X8XGEdcjkqqYFyh-3iypzMB0tDZtNcYvvKxqc2l1N9RiU2lPY7FWIGBrp2iZkqfHLd11fOz6E4R0vLiB8ks4jPJYUVqKKBbf9AMWdT5ZeDWHyzlAEtu-S2Hq8m0kMjSOKboHKrsLz9Nok__P-GAlVE0_gJbVs-xxhQTWK1DkKTDvsJC2A6IuYBZSfpfzpn-WVQgceqLGqmGbLZbZYAPGto96sSp5bhhIvQArRA9hTP3wq9Dtpzwjh4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=uAAc1yvFHvWIlaAVv0iolnmYPYhLPr-P5Eeib8X6a5KUFdoqNx8rODXzKgiHGyWcUbceFRJZJnKbz5IAHig1_vJbi61y9s0Dag2y2u9N4YWsX_hGstWw5q4lDqUXLx849Jsvz5OClr65KxkK-tRGXXaeo2pOvbxwOfX3BhcIxNVmAadeUavJlV6GF-wjsTBGnK_8w7HUfm-bmVSYEH8SSvfEbNQ4R0IFjnGV01570SlUaz0_Learhe2FIQMVTcCc-dwajMtvSa_FeMsv1c9QnsRY-Iome-hApdM5V40B2bTIEVqH5J_6xLj3M6-rDqmqaaqa858-Zwvu_p_-oABTRybHY_IP_9Kgn8bg2ToW8tc3C7Zk-L0iZ3Tbh1bu8tkTim9OzIrT2GFjc7wgANlHQ69MJwWoB24ns0dyuXHrZoRZ1smm4Tn0X8XGEdcjkqqYFyh-3iypzMB0tDZtNcYvvKxqc2l1N9RiU2lPY7FWIGBrp2iZkqfHLd11fOz6E4R0vLiB8ks4jPJYUVqKKBbf9AMWdT5ZeDWHyzlAEtu-S2Hq8m0kMjSOKboHKrsLz9Nok__P-GAlVE0_gJbVs-xxhQTWK1DkKTDvsJC2A6IuYBZSfpfzpn-WVQgceqLGqmGbLZbZYAPGto96sSp5bhhIvQArRA9hTP3wq9Dtpzwjh4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=jdl_fbkvIUkCUYjM-nUqpzJ06mkBAImiEFV0Bnkpe6yPZ_r8pw1DiH6JQAEngKnDNv3tPKdZGTInum_2zCC9MKe8ld7g1croXWndDr6UgtEcc1CnwNDG2Y39U0Qqhc8bj2KgYhaAsTkbbTia7Uw_jYlJRtMDy37mhxnpBvgZPueo45Q_mql6WQqLRDAv33BTJ9cPSzfX7KDoSY-r5WfZ-yCxMeRnQEl2Lt6SawBJkT26pM5qQleh0Si01eB70V-uRDNHrqWPuQ0TGdp5VqpZScvNErqI3nSWWQu9UoH7DeO8kxtWFrCKBu0G9DO8QV0bNsHJ5hu7cOfovrLBmlqJVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=jdl_fbkvIUkCUYjM-nUqpzJ06mkBAImiEFV0Bnkpe6yPZ_r8pw1DiH6JQAEngKnDNv3tPKdZGTInum_2zCC9MKe8ld7g1croXWndDr6UgtEcc1CnwNDG2Y39U0Qqhc8bj2KgYhaAsTkbbTia7Uw_jYlJRtMDy37mhxnpBvgZPueo45Q_mql6WQqLRDAv33BTJ9cPSzfX7KDoSY-r5WfZ-yCxMeRnQEl2Lt6SawBJkT26pM5qQleh0Si01eB70V-uRDNHrqWPuQ0TGdp5VqpZScvNErqI3nSWWQu9UoH7DeO8kxtWFrCKBu0G9DO8QV0bNsHJ5hu7cOfovrLBmlqJVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb6WvF04whAJkJLSGSzKDyIadW_R6DNOyHNRAvLRYE5dDH4lQkHrJKDVgzXfWOO6u4SHzkC0qwWGKI0R3uJIauQVVFfwGCGq1H9C_6ve6d9V0l8EQ8ow-ShVBHqk7SaOFbssYg40JNR-w43zl8djIj7P9YnZVaK91Pzq7RqT6YT9vKBqlahd6RUTzwpKlui5L-QZXAGxVn9HuTwFD_gyAR-mQ5_KPy4DoxwZtTb-HrEw_zmgLfuvgVVdOFK-e0oK3acOxIAFNFxJdd8tnpJvHbHx2bimLTAzINgAG96pafK_PBsHDPuR_yACQNB2yH-ItOWYiH3_5WscrfzPGtPlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=prXAagujLPfYdcMSW0jNDbj0QFpfkGMRUmvIWNXyC4vx9DSEMY-vqIEdZkddXGy9YWIr1qFDwbx9UUKI01lTCMy3hUQa-9vR0Debrn8jXbBiyHxGumqpdZyVcOL4Jw1IASw5DvUgKJcaTbN-Yo9aK3OOKce6vYjhdB_gWXo7Hlf4Ahp7PuJWIJ8AaHT0CkSxbX5AzsLgwn5ws1Uxh661ncJmiQ6MJPBGWmd2RBQuvd197fV9JTW2lOnWFXgFi5Z83vpuiLyrI9CaVm2jfZ14h9TP9Jf9atiq-0JeI9kqRiDLxqb2bm97HJWOqZqQJNHwxbFoJ6XhLCcVUm6pHPQMsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=prXAagujLPfYdcMSW0jNDbj0QFpfkGMRUmvIWNXyC4vx9DSEMY-vqIEdZkddXGy9YWIr1qFDwbx9UUKI01lTCMy3hUQa-9vR0Debrn8jXbBiyHxGumqpdZyVcOL4Jw1IASw5DvUgKJcaTbN-Yo9aK3OOKce6vYjhdB_gWXo7Hlf4Ahp7PuJWIJ8AaHT0CkSxbX5AzsLgwn5ws1Uxh661ncJmiQ6MJPBGWmd2RBQuvd197fV9JTW2lOnWFXgFi5Z83vpuiLyrI9CaVm2jfZ14h9TP9Jf9atiq-0JeI9kqRiDLxqb2bm97HJWOqZqQJNHwxbFoJ6XhLCcVUm6pHPQMsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=vv-NzUv16nJSHZTCG-lfSrRSMRCQ9XQjXcZDEip2SXED9fBSNVWTVOPcqgiUPY1h5Rlto6r2ghCLI5CwYuVDvfFKXQRKr4nnimEMigXJNqrCs7DQ-i-QEX7j6TAayH4u6u_A-tTnwxvvsyVidTC0fsdOMMK24Dokr3CT6jZRO1fygg54cGKfnBDuY0COr3RV7aJYdeJ21Cnxt5kHg1t4PRXw6iSIRZhN36gppWyle6pSZCcqzDjb8pKmIpjWQgapbGlobcVP1yWV4uL5HCDC8UvUHjNn6M9PD9DVREVuxsQh0ZL_qaj3xLzrpg7cw2QQeRMW12eTmfdTItd1NkWdY5bhptnFtMLC6g7u5ErUCLNU28dCpRnOUD0P4Za4bg8FThUowSGQM6Y5y3P3fqkALHYFiyRA_X70noqjzVorMfdO2eD1wVQzuwTz4r-g86ja82IU0SxFY09-RNaQG-iaq6FD59t-9xv-nAPmNk2m4fiTELvXto3-e-4OBEBUdp5yWkOtF1BmItWBEetZY7taw8zXPmXMzZOB3aOvO520X6ky5rG20temXuFJtK_E1ol4VPoFJECbEcGNWqe06pIEK1fVz425PYWSiIzJiiipxyhlTc5KCfoP7KLszIfyGrVW4hYtz-JoZzMPZqvcxKOU4zgQXOTEPViPtVv2eeQFyFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=vv-NzUv16nJSHZTCG-lfSrRSMRCQ9XQjXcZDEip2SXED9fBSNVWTVOPcqgiUPY1h5Rlto6r2ghCLI5CwYuVDvfFKXQRKr4nnimEMigXJNqrCs7DQ-i-QEX7j6TAayH4u6u_A-tTnwxvvsyVidTC0fsdOMMK24Dokr3CT6jZRO1fygg54cGKfnBDuY0COr3RV7aJYdeJ21Cnxt5kHg1t4PRXw6iSIRZhN36gppWyle6pSZCcqzDjb8pKmIpjWQgapbGlobcVP1yWV4uL5HCDC8UvUHjNn6M9PD9DVREVuxsQh0ZL_qaj3xLzrpg7cw2QQeRMW12eTmfdTItd1NkWdY5bhptnFtMLC6g7u5ErUCLNU28dCpRnOUD0P4Za4bg8FThUowSGQM6Y5y3P3fqkALHYFiyRA_X70noqjzVorMfdO2eD1wVQzuwTz4r-g86ja82IU0SxFY09-RNaQG-iaq6FD59t-9xv-nAPmNk2m4fiTELvXto3-e-4OBEBUdp5yWkOtF1BmItWBEetZY7taw8zXPmXMzZOB3aOvO520X6ky5rG20temXuFJtK_E1ol4VPoFJECbEcGNWqe06pIEK1fVz425PYWSiIzJiiipxyhlTc5KCfoP7KLszIfyGrVW4hYtz-JoZzMPZqvcxKOU4zgQXOTEPViPtVv2eeQFyFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3Y40QnCpw1xF85JWQaccH3OtHzDV3PV5aOz2LTuzTQHnmCUmPrrfmy5V8rBvytQytIqBRSjrbGx7dN_cCFeeO0m7Juc99TPCV1jVjHCoM-bmNiK0Wq02nTu4owwv0srosjMRA4qwC7DPWBzDGwzZfRvrPw2Knq5zzAEbdBWVXfdp28MNhz901iwi6tbVMSwY8xty-cbgX_8YpA6c_MkXhZKLYurmiHQJa0DPXqv2Jk6l-2yab2Z97Q_CRQ1FWIzdrvv4UcuDCGdEia8mqA1bQYbuBvrJy-pxqLvd5ERNLwDB_-KGNt54jNU-dg9xaEHVuEpznshnyAQSCeCgni5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=HTUjbFzvdqnnEOZgncnVdq5fXof3BTrb456JjTN-T1PJrQjBJwnoYvdTbwCssx0dU3PX_RVFnyl7H26QtANyFuQG03jFbW_sj3gszCtcPKzJiquXb0NESKJbTqatrPfdDidxZ9T_6pMMBfBjvz0rYmRovSm9pyKwe5nM6kp7oYoyXjAM_1et2rfTwuy6yJa2ogSpdBbv2P_d6-z_Vt0KfZLu1X0dTRYNwce-YGRFKZWs52lmWrBymIjISYUmWF6H3UEH0zQf3ZiKcU6zYDvYWm-PESRmoR8ZRd0XVXJgRNdSP9Xoi1kh-7L6kmOtwv2TxQwpmdQmQCCykPQAKNNRtmR4xVOdwilcHjtCp3UNuAzyeJSnZ8HOYyOmG5Ts8-t8oWu1_r6o4NIkoCJu479IAqLAbBS1E5fuD2o5em1I2DejumtnLEsC4m9jzh9Tq3fFj13WanSov2bBkI07AHVkM-IKu4kRSdbAuMv6ZFAut3jw7UbXwXTZr2KX6bvga0NukBPZCsH8u6z8Fex-ehpY5tZm74CokSSb_nAqqAp1SyxLI82qsNXn_zCWTH04lYSH9c32Z1ZUIYzZjqMHJIEtm1zQDw8jMTF-rUx1x41Ddq09RtMx3RLu3fTYEhIdq-PWzBCkuwkyScQfq2evNYjBrMynNjP0jy0aznA-X7cLArY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=HTUjbFzvdqnnEOZgncnVdq5fXof3BTrb456JjTN-T1PJrQjBJwnoYvdTbwCssx0dU3PX_RVFnyl7H26QtANyFuQG03jFbW_sj3gszCtcPKzJiquXb0NESKJbTqatrPfdDidxZ9T_6pMMBfBjvz0rYmRovSm9pyKwe5nM6kp7oYoyXjAM_1et2rfTwuy6yJa2ogSpdBbv2P_d6-z_Vt0KfZLu1X0dTRYNwce-YGRFKZWs52lmWrBymIjISYUmWF6H3UEH0zQf3ZiKcU6zYDvYWm-PESRmoR8ZRd0XVXJgRNdSP9Xoi1kh-7L6kmOtwv2TxQwpmdQmQCCykPQAKNNRtmR4xVOdwilcHjtCp3UNuAzyeJSnZ8HOYyOmG5Ts8-t8oWu1_r6o4NIkoCJu479IAqLAbBS1E5fuD2o5em1I2DejumtnLEsC4m9jzh9Tq3fFj13WanSov2bBkI07AHVkM-IKu4kRSdbAuMv6ZFAut3jw7UbXwXTZr2KX6bvga0NukBPZCsH8u6z8Fex-ehpY5tZm74CokSSb_nAqqAp1SyxLI82qsNXn_zCWTH04lYSH9c32Z1ZUIYzZjqMHJIEtm1zQDw8jMTF-rUx1x41Ddq09RtMx3RLu3fTYEhIdq-PWzBCkuwkyScQfq2evNYjBrMynNjP0jy0aznA-X7cLArY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=WPT0cCV7E5LUaKZQiLCpgduJmS3GwkDSQbs1pT-hJlA0yiD0sB1ZnK3QcVOd7GpgG4MH3XwOya_uuEHsM3cnvSpZeh1ZysA0E3lncM2_c7MCpm0vxgSuWQr4Ttuv2K6V0Tqx_6YHVdsbw6RGUV7hEublzici6GcGOd-mMtYRJKRn7JRiVjHopTw38mjAjiwIMLwznaWau1RwXtsCT5jF9bYXmbZ_mIyFmZTKVC2rSzPTzl7wvza6fUEOKOOiPfMQDdWEv47sPZHrytkGrxyHhtXWT9KSERULr66ONZ7r3b3iFWAHrILMLuxti_MundP__fke9WV4BY6J3ShQQl5_gGgnRKVVQ7c_BLe2dxviBz30uDCIsTrug7qeUdq9GMyCfuQgVebiP9QFiOea90XONqAuyst-C16NN8a-edOnMXIAaA291aAGQGveySGRyWngCZl7HsucSiol-p8sA4ymQN5omSP9AtDCgoMyQzoAfnxU0OU28LV9ZPQwxTstx4SQzKifUd_KQ-xB5XTOe6gnLpPhjRAye5d5lo54B2Ss1o_fFl-Nfy69d9bKJNeI8TOMOnyxoO6dIeEqm94hkdxLVGog5PLQbzf9rXTM35cBXo2qhhGut614BNf5CGB7v7AZxg7_hj3-PfHvfwFKnIn5cwj90g9GC3kzqYvxHaeMKXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=WPT0cCV7E5LUaKZQiLCpgduJmS3GwkDSQbs1pT-hJlA0yiD0sB1ZnK3QcVOd7GpgG4MH3XwOya_uuEHsM3cnvSpZeh1ZysA0E3lncM2_c7MCpm0vxgSuWQr4Ttuv2K6V0Tqx_6YHVdsbw6RGUV7hEublzici6GcGOd-mMtYRJKRn7JRiVjHopTw38mjAjiwIMLwznaWau1RwXtsCT5jF9bYXmbZ_mIyFmZTKVC2rSzPTzl7wvza6fUEOKOOiPfMQDdWEv47sPZHrytkGrxyHhtXWT9KSERULr66ONZ7r3b3iFWAHrILMLuxti_MundP__fke9WV4BY6J3ShQQl5_gGgnRKVVQ7c_BLe2dxviBz30uDCIsTrug7qeUdq9GMyCfuQgVebiP9QFiOea90XONqAuyst-C16NN8a-edOnMXIAaA291aAGQGveySGRyWngCZl7HsucSiol-p8sA4ymQN5omSP9AtDCgoMyQzoAfnxU0OU28LV9ZPQwxTstx4SQzKifUd_KQ-xB5XTOe6gnLpPhjRAye5d5lo54B2Ss1o_fFl-Nfy69d9bKJNeI8TOMOnyxoO6dIeEqm94hkdxLVGog5PLQbzf9rXTM35cBXo2qhhGut614BNf5CGB7v7AZxg7_hj3-PfHvfwFKnIn5cwj90g9GC3kzqYvxHaeMKXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Xm_ud6x0tMn9rnzSbN7BKnPT-Pqr2279JH3QDygl4zZh5JSRL4OMpnl0zcBcGLWdnW46LnDZspNtokUIAQApp9uXt-jL97U53uPkNon_YSNKE0oX97OKDtxI9wryZtm1VYfZPP3Z6megC1YyjGfo4vhKsK8qVdwd2iT53kEO-A8VU___tm8PycVxnlNDDISM-qnrnTNzDSLsBbm4jzZjJAulrYmP9vzbs2jUuwH522AoFxjWZGmBOlyGst2unjwZu739Y0AZPqK_FAYoZpBQg7E_Rqv_6HzmHMpEIURHDBrTRvcxJ_VM-pavYm2HYe1NI40rezNXm3Il3zkQP-Q1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=Xm_ud6x0tMn9rnzSbN7BKnPT-Pqr2279JH3QDygl4zZh5JSRL4OMpnl0zcBcGLWdnW46LnDZspNtokUIAQApp9uXt-jL97U53uPkNon_YSNKE0oX97OKDtxI9wryZtm1VYfZPP3Z6megC1YyjGfo4vhKsK8qVdwd2iT53kEO-A8VU___tm8PycVxnlNDDISM-qnrnTNzDSLsBbm4jzZjJAulrYmP9vzbs2jUuwH522AoFxjWZGmBOlyGst2unjwZu739Y0AZPqK_FAYoZpBQg7E_Rqv_6HzmHMpEIURHDBrTRvcxJ_VM-pavYm2HYe1NI40rezNXm3Il3zkQP-Q1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=qCwqVWYHWsZn49vR9bHStL6Xo5r1SDMtsY1fwmdrcIkoxJ66Dqrn_6oDe1MwZ1S16uaHDf1DkeIqoXnnhWTckcIq3yTCx_3-K3dqM5qG5kVmhvKEXnlUhR8aUFax6p5iBP9ZjOZ2v_dQA4f92mZqlPiO7Dgw99ADkAWnCFL54KQFIphdqleHdKmeE9DGR2D5kCFMn7NSBg3qmzW9KjfduFP54jVZl4Wyv8gjwd5x1_nxThtCRMenVqxAmt-Y0Ja2jnJswNKlW_78VhrUuJXzPs13MtA2ku9i6ukSOraBIz4fuM3HW9QzeUbFzJ5Zg5muhga92udiyETiv1ytw25lcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=qCwqVWYHWsZn49vR9bHStL6Xo5r1SDMtsY1fwmdrcIkoxJ66Dqrn_6oDe1MwZ1S16uaHDf1DkeIqoXnnhWTckcIq3yTCx_3-K3dqM5qG5kVmhvKEXnlUhR8aUFax6p5iBP9ZjOZ2v_dQA4f92mZqlPiO7Dgw99ADkAWnCFL54KQFIphdqleHdKmeE9DGR2D5kCFMn7NSBg3qmzW9KjfduFP54jVZl4Wyv8gjwd5x1_nxThtCRMenVqxAmt-Y0Ja2jnJswNKlW_78VhrUuJXzPs13MtA2ku9i6ukSOraBIz4fuM3HW9QzeUbFzJ5Zg5muhga92udiyETiv1ytw25lcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=NqZm_ypvPURJA2PZ_5QRhHWGM08RqWofPp9RTuD0YW68tD88MIS5LmZyOrwpjjZea1UlMPz98Tgl02BlKqpfZ6nw4ImyOwtakQNWLcEra32mmlJNxzNMppm9nIK5D4TxZBNlKL6Oge83wo-AZLHxnwxp6yEaucrL5GmBWAhld85eTPX7fJYCnXqa5qNvIY4J_PCRI_5bM33Slx40GKkbHguttrhNLY5CyDStAruP8Sd3HGLaAgBQBXWuTVPG5PfSpnyz-CDxm_oDheX3LInCXIu74sS9EQrNkVAPCnJOryWuTsLG9LtsAP7U8HE7mEaEqiMtD-x9EJqDFlfMZID8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=NqZm_ypvPURJA2PZ_5QRhHWGM08RqWofPp9RTuD0YW68tD88MIS5LmZyOrwpjjZea1UlMPz98Tgl02BlKqpfZ6nw4ImyOwtakQNWLcEra32mmlJNxzNMppm9nIK5D4TxZBNlKL6Oge83wo-AZLHxnwxp6yEaucrL5GmBWAhld85eTPX7fJYCnXqa5qNvIY4J_PCRI_5bM33Slx40GKkbHguttrhNLY5CyDStAruP8Sd3HGLaAgBQBXWuTVPG5PfSpnyz-CDxm_oDheX3LInCXIu74sS9EQrNkVAPCnJOryWuTsLG9LtsAP7U8HE7mEaEqiMtD-x9EJqDFlfMZID8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=gCcBGbikzUlFbl7qTCZdTD820PF9a0xb3Zq4_cpFwU17iUKSPq_wOtEC9Jm4q2Abf3fBtI5fgT6DYy-GrRQlwn6HXoQUY14Qq1-XBXkJu4VQuhr6CCpwzdc6kzXWaNxrB2y4Dd9gZ5wywQEu-tjC-uEByLdrveHlEq0nHRChsJ2yhgwRVKHJX5q4X9dZmoV9U1AeUEsIR0ryd1-2obQzXtu8LpmeyJurt_0vh4WJLMSKBx3uSBOvwuTQJ6amxc-SYSBhdTvZzC3Pu-qXm0o6W5qYK8xBTAsBkZ8eOhd3G-zVsRh2DnSr1GGE2BSBqMi29CoVgT546sa_8da2ICXlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=gCcBGbikzUlFbl7qTCZdTD820PF9a0xb3Zq4_cpFwU17iUKSPq_wOtEC9Jm4q2Abf3fBtI5fgT6DYy-GrRQlwn6HXoQUY14Qq1-XBXkJu4VQuhr6CCpwzdc6kzXWaNxrB2y4Dd9gZ5wywQEu-tjC-uEByLdrveHlEq0nHRChsJ2yhgwRVKHJX5q4X9dZmoV9U1AeUEsIR0ryd1-2obQzXtu8LpmeyJurt_0vh4WJLMSKBx3uSBOvwuTQJ6amxc-SYSBhdTvZzC3Pu-qXm0o6W5qYK8xBTAsBkZ8eOhd3G-zVsRh2DnSr1GGE2BSBqMi29CoVgT546sa_8da2ICXlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=dIhDX1EnSG2qx5LWHQJop6s_1USLGyVQ1qIfCjMEn4i2CkzKNoFm2Dtz7bTuw6BUC50pokHk6nKUo5qGKzzVcIRKyZljPHx4kVd998DZSqVVDBE0J2Akw2lbfaxaA0cdrTG_QjcjNV8PmkI_yiiaay-n8j-_gp1zBS3o1P8HiGVAF5xFS6ml5tD27vKpDhbtl5jEPspArK-5pHdiGC6nE47WWs6p2K9BrF-XSyBczX9XqWSex7SsFYx8RHgy9RhdR19Wj3fT3mnRDMS0SyfuHVu8cPNKzKdU5JfXdod-KNFWABLnACyY3xgsDBxUUQUt0G_e6r4nw1Z9LsKIv3adlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=dIhDX1EnSG2qx5LWHQJop6s_1USLGyVQ1qIfCjMEn4i2CkzKNoFm2Dtz7bTuw6BUC50pokHk6nKUo5qGKzzVcIRKyZljPHx4kVd998DZSqVVDBE0J2Akw2lbfaxaA0cdrTG_QjcjNV8PmkI_yiiaay-n8j-_gp1zBS3o1P8HiGVAF5xFS6ml5tD27vKpDhbtl5jEPspArK-5pHdiGC6nE47WWs6p2K9BrF-XSyBczX9XqWSex7SsFYx8RHgy9RhdR19Wj3fT3mnRDMS0SyfuHVu8cPNKzKdU5JfXdod-KNFWABLnACyY3xgsDBxUUQUt0G_e6r4nw1Z9LsKIv3adlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=czIOofUoANSoQfQ5Lig66xsRUmSc4HIoApRsVHVDnT3PZr0znYtnMWT56Fa1xx8C7OLRHNKgSvYXkuu5D4QCWLczVySB0lm9dQxeZ2Y7Pxg2of4EeNuG0TNDrfjGaVd61GRqxo9unK5kMgYvaID6s1AbSBIBnxeYZ1VtBm6Dd_uEf0YzKGxsVQxCwdcvfEpIFpTIsqR2MsdOV0NLa3a15N0N2jEeVQVvOgOTmQQWGvYek3l8Ks3x_V4tFXhxpA0z3NWcWdMLhabNaKio9wjSq1U22eMOwpZ-1v7La2XXbFLHqI5QVBtUHMk_FfCN_yxdFQEovlIu4sB4Ea3KWo-pqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=czIOofUoANSoQfQ5Lig66xsRUmSc4HIoApRsVHVDnT3PZr0znYtnMWT56Fa1xx8C7OLRHNKgSvYXkuu5D4QCWLczVySB0lm9dQxeZ2Y7Pxg2of4EeNuG0TNDrfjGaVd61GRqxo9unK5kMgYvaID6s1AbSBIBnxeYZ1VtBm6Dd_uEf0YzKGxsVQxCwdcvfEpIFpTIsqR2MsdOV0NLa3a15N0N2jEeVQVvOgOTmQQWGvYek3l8Ks3x_V4tFXhxpA0z3NWcWdMLhabNaKio9wjSq1U22eMOwpZ-1v7La2XXbFLHqI5QVBtUHMk_FfCN_yxdFQEovlIu4sB4Ea3KWo-pqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=aPkI4nEz0VNUyWMc2fNSxfDFE4aI5ZqeZ7yvu6Lm1K52AIi4xAGLz03oE45w7uO4Fa2DmQE-_ux4aZ_6SUZYtryXopCzuW0bZhJ7cmhpMJihLSvUrNGUNBNjRNMpp_X51S1_1HhWPPiZLWdVz8xphwGxit9LufvY4eis2T96ZtSSBogeop6-qPT5aFtjP1JfqzYaDJjNRN0R2l0WsQYjysesnBpeHVRjPS1HDhn-LByvDi5n7b_OTSNPLSpNho16QVkLdiDF9pAvaqFtmK8FjRzT8RYAyNndCPQFfAeF0O9dK1U8lc4dMI4xwWifDV0tyy7ObheBCVE5M4RgQ6d-pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=aPkI4nEz0VNUyWMc2fNSxfDFE4aI5ZqeZ7yvu6Lm1K52AIi4xAGLz03oE45w7uO4Fa2DmQE-_ux4aZ_6SUZYtryXopCzuW0bZhJ7cmhpMJihLSvUrNGUNBNjRNMpp_X51S1_1HhWPPiZLWdVz8xphwGxit9LufvY4eis2T96ZtSSBogeop6-qPT5aFtjP1JfqzYaDJjNRN0R2l0WsQYjysesnBpeHVRjPS1HDhn-LByvDi5n7b_OTSNPLSpNho16QVkLdiDF9pAvaqFtmK8FjRzT8RYAyNndCPQFfAeF0O9dK1U8lc4dMI4xwWifDV0tyy7ObheBCVE5M4RgQ6d-pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJ9AT7h6DrXnkjwWUIFzU-jDG85L75-lUol7tCxNOwtuDaJ6BX1etieaP053zSFn7i_BemzCTPGWbMoDN36eVnq8__QnSpDtxj6avrDfqWcYvcNTPNo5dh0Vq9InRzoV65yeOSh45X-OWTNLmbMIAK4omYHs4yGclsdBsr_IdLqRKS_fB2I531aY8ERQgqfPp7NeaEkPXuDWeAVMrz4F6HifxuM73_-Kjn69gEKpOiEqqayFk17XIjUkViD0MpgXuDEhK7GkCK37FbeE1btZUe5b-3v8XwKBs3M5wZs4zWQBtM0FvPIolfeBZDHGY-siAn8T9_HNNUE7-8R02BQr2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=UUW_p5beS99ndavCKnCXgyO9NQ0MXq3bb6CAGeFtJkW4exgv2ntTEwJx2GLCx-YRom52vU6W-UoOMFBtZqzKqnIYKQqPxb-vhy5Bnk9ZXDlEPt03qNOJon48vpUKkDd274MLF8VBdFDq3T9jhGmik14ah7Lumpvr5FqdtGbCTvlo9t68EKqjzYWhVK-eGVpwSINaAjgLX1P366DMZSWbd32Y0W2orVnT2C11kZZuIVqIhTSTE3_bzSSpl9b4IYB6jp4FtvNsYzJ0fN0_74bMm2t_1R7hiG7GYdgy0blpIprH84I7MceJTYDXN_1YD7djaINOexps--h4zEABIWONRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=UUW_p5beS99ndavCKnCXgyO9NQ0MXq3bb6CAGeFtJkW4exgv2ntTEwJx2GLCx-YRom52vU6W-UoOMFBtZqzKqnIYKQqPxb-vhy5Bnk9ZXDlEPt03qNOJon48vpUKkDd274MLF8VBdFDq3T9jhGmik14ah7Lumpvr5FqdtGbCTvlo9t68EKqjzYWhVK-eGVpwSINaAjgLX1P366DMZSWbd32Y0W2orVnT2C11kZZuIVqIhTSTE3_bzSSpl9b4IYB6jp4FtvNsYzJ0fN0_74bMm2t_1R7hiG7GYdgy0blpIprH84I7MceJTYDXN_1YD7djaINOexps--h4zEABIWONRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=mmHX1GuuRhccBqwtG7A6yh5UMbB0izpIbxO97EF1ygmFQgerOa04lys9QseykGi8r5-JG8IUKcrsSOwbZ2I3vyoA1I2kD8SZy1Sgtueex2Qn6mHhiPnhhwyg_84BnnA-cpLYHvakfBOZ0EwC7WgZIm7twicDTJQpTRcA_zgm8yGkoH_QwNZtcwu_dyllu37RRHpHWybHQh0utH6hIxtixCcmteoxJ6bXwOwazqeHAj3k4GPwY3WNkmACCFbpqopWYnTMxUr8ripY6LcvJRPV2Nbs0mpLZ_-HsWk3cSGh3bKWor2HoLymrgLPFdEIM2QH4s-sdFLj7LQ9m5w1FHgeiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=mmHX1GuuRhccBqwtG7A6yh5UMbB0izpIbxO97EF1ygmFQgerOa04lys9QseykGi8r5-JG8IUKcrsSOwbZ2I3vyoA1I2kD8SZy1Sgtueex2Qn6mHhiPnhhwyg_84BnnA-cpLYHvakfBOZ0EwC7WgZIm7twicDTJQpTRcA_zgm8yGkoH_QwNZtcwu_dyllu37RRHpHWybHQh0utH6hIxtixCcmteoxJ6bXwOwazqeHAj3k4GPwY3WNkmACCFbpqopWYnTMxUr8ripY6LcvJRPV2Nbs0mpLZ_-HsWk3cSGh3bKWor2HoLymrgLPFdEIM2QH4s-sdFLj7LQ9m5w1FHgeiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=BFXrkJvbr75QTmzOcHFRw4RfVAjnseyzdo8e9ceIwLvQ7wjBu5TyVO8q3NR9rJtAlh9ZwAjBs8lqB3i6IO-Z3v_YyFIuteEkfW35gxByCvbWVJbwXMSK3g-5hb-TyN9b0QdCcYr_9tANAh1TUZus95W7a0_9CXpA0E26TX1x2QWFFno0V8vFctSLRz0IT621mZbFEFlAzj1AvCdVrNfAVy539biSqi91Lh7gfcuIRt---KxwLdWfNuSON6QsnC9VmS5sDk1vQP330W7nnP4mtbguQI_0qyNqP0SCivzaSbgqCqILQuBOrTr5VA53zNNeNg9-sEOOKouENxLTg2T7lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=BFXrkJvbr75QTmzOcHFRw4RfVAjnseyzdo8e9ceIwLvQ7wjBu5TyVO8q3NR9rJtAlh9ZwAjBs8lqB3i6IO-Z3v_YyFIuteEkfW35gxByCvbWVJbwXMSK3g-5hb-TyN9b0QdCcYr_9tANAh1TUZus95W7a0_9CXpA0E26TX1x2QWFFno0V8vFctSLRz0IT621mZbFEFlAzj1AvCdVrNfAVy539biSqi91Lh7gfcuIRt---KxwLdWfNuSON6QsnC9VmS5sDk1vQP330W7nnP4mtbguQI_0qyNqP0SCivzaSbgqCqILQuBOrTr5VA53zNNeNg9-sEOOKouENxLTg2T7lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L9MtXjasXZoXjxohAuzS9606dA22hvXwtZiFk9mCEXLQppGiEqBHtZBvHOafow1yoWambILFW_cf5KH6z5mfFkQFfhZ-iKLvFTQGGlP5ksaYiUIEImZ2Zi_PxRAWC2k6RO7TJ2R0n3xTlBqVUQhBQBt7IhLBxn1Na25PKlcCIwzdq1E2sjz7u0XBrBUeF5W7yjOW6p7WW5n1F3yzev3IEUwaFoF4k8-LSzbSukQHDFDyZjwkwz6Srx1QCuYjAGFFUMw8TFHHGrTWYr2lj2PHnttQ4bW8T8-h3D9p2hNEtylOSXsL5KS8FKzmCGGJSYuo5MfQWhp6pD7LsqR6s8UOEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L9MtXjasXZoXjxohAuzS9606dA22hvXwtZiFk9mCEXLQppGiEqBHtZBvHOafow1yoWambILFW_cf5KH6z5mfFkQFfhZ-iKLvFTQGGlP5ksaYiUIEImZ2Zi_PxRAWC2k6RO7TJ2R0n3xTlBqVUQhBQBt7IhLBxn1Na25PKlcCIwzdq1E2sjz7u0XBrBUeF5W7yjOW6p7WW5n1F3yzev3IEUwaFoF4k8-LSzbSukQHDFDyZjwkwz6Srx1QCuYjAGFFUMw8TFHHGrTWYr2lj2PHnttQ4bW8T8-h3D9p2hNEtylOSXsL5KS8FKzmCGGJSYuo5MfQWhp6pD7LsqR6s8UOEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mfubORenvwQlinVOu8KGCS97r-KOHeuxACPtTjJ02w3oPwKXQQk5IEPTDTzrGr0iKdcaM_A2mxBlDP3XMGqHYPABGGUYWrf5USMBfUA4w0Tkut-BOCjfpU1-SKBxG3L-FIGs1HTKkmSOVrRVrW7o_-5jZ2Gouzl-wAMO-sM4rchv9RHsy1lVO8Qsgkks4bhDMARdW0IITbblr8Mh85LL_5nAfS8KpMhDumKAoyabHAR69yPqzCCbxMx9WtbUnWSK1vAxl6oGPk6vbNSbfoLUEpd4u17uKbITRQqtE39eurhkjX_wdbfJYcYdo7rUH9KyG6FJFyNCtLGOwmyiv7dPIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=WcxD8Hy8k_YW9UI7A7VtSvbQ-1X9kPPVSc2U2fHMNOUkSs4F-iTEtSABe8MLFZCGknFt3Qa2gpBG6ZjYM6MQQ2agfGNzXqeIBUtMMJcQdnNkPOxF0b41myVyoGmOlKao4bdPxOxkzSqq6S2Y6ubim2XWQZltMtT4t6uiu95o2DyU9mIWUiHhvVQ0YyFxyqDZ_p8CT4YE4n0GGlPcx0vfKW0jIqxMSQ9MoiA0JZkVgXRBpk6sgX32AeEb-uLCz2gc1feeZi2is2Pa4JNhyWwIy-Uo9vrSwcGCqik48OTCw9BYFWHARH8nk2z7nP_wpVctgm1CC5N4Cih5sL7xcrgDDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=WcxD8Hy8k_YW9UI7A7VtSvbQ-1X9kPPVSc2U2fHMNOUkSs4F-iTEtSABe8MLFZCGknFt3Qa2gpBG6ZjYM6MQQ2agfGNzXqeIBUtMMJcQdnNkPOxF0b41myVyoGmOlKao4bdPxOxkzSqq6S2Y6ubim2XWQZltMtT4t6uiu95o2DyU9mIWUiHhvVQ0YyFxyqDZ_p8CT4YE4n0GGlPcx0vfKW0jIqxMSQ9MoiA0JZkVgXRBpk6sgX32AeEb-uLCz2gc1feeZi2is2Pa4JNhyWwIy-Uo9vrSwcGCqik48OTCw9BYFWHARH8nk2z7nP_wpVctgm1CC5N4Cih5sL7xcrgDDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=TtZnvCRl2up2PLNn-1fhjQ8zEfKJvw9McwKIF-eCNhWvvI1b3DLkRikkHUkmnWihtjN8OLJLsop8BPCMYK6tm8AbsFif6UyS8Gu7PuAEo4vCu8EqF93I6lWw_6O4Pf4hsxT4WN7NqVbiYOa3wWDGNpY2q9PudWdTwgiEXasXxyXX1bcSWt7GU5YDVn2_X2eLhyh41MJok20nu7uU7aCI-3sUDpvwv_lRNWJYu1Y4L-t4Q-eiL4mpmbahyiOquw2vZUNLdTR4VYJkik83rKDV7h8KFEQl28XmshPasiQQx4XldhngXzUhCMUVA93qXSLfCadJm0z_r3AnqWBKjln66w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=TtZnvCRl2up2PLNn-1fhjQ8zEfKJvw9McwKIF-eCNhWvvI1b3DLkRikkHUkmnWihtjN8OLJLsop8BPCMYK6tm8AbsFif6UyS8Gu7PuAEo4vCu8EqF93I6lWw_6O4Pf4hsxT4WN7NqVbiYOa3wWDGNpY2q9PudWdTwgiEXasXxyXX1bcSWt7GU5YDVn2_X2eLhyh41MJok20nu7uU7aCI-3sUDpvwv_lRNWJYu1Y4L-t4Q-eiL4mpmbahyiOquw2vZUNLdTR4VYJkik83rKDV7h8KFEQl28XmshPasiQQx4XldhngXzUhCMUVA93qXSLfCadJm0z_r3AnqWBKjln66w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rDtP52_7RH5HmUx85RWCaIVDJodYm0_AO24twEOVBi_RBxPSSje6pVIq2JbhIfr-TgDarlg0F-YpWS5q7lEAPyOk-ZwJOTcw3BOvCGvHTsIK64HZI_nPhZBW0qfz_vmPIOMlmKcso_oxwd3pqOksLbUOeu0o5zHFBsb6nj7ktkXn5AL9PNQvfD-Qz0kaS_kB1SUGqIDr9OBoSd1NDYM6ly4iB-Fh0dENpxyHAmSQbV5QIg71ktlHjeUOZ7MLJvgU_q0S2IqxgyZOsk7jysGiV9EAlZKFjdF4vG4B08QsGwcNfuo-5K5w-Vf9hkgrs08JCDXCauQhtru2-TUyQmn2xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mqR8RTDAsuROPXmbbQTnwpo67qeeHLz4mfsObxiQ_ha-w4zrNRYlzl4ppNcVNTXNkSVi6HF4u_VMPyuDBbPjdwoT6ETVkTe5TbrhHgpn8t3W8HGbrgBeCNohg5eSJlnphdfOJqbGtUYUa9N5IQeuZ32haoCG_ZLWJaFsK-ZTaXVB86YCCViVDr39KyfHU95JhkvIGbM-L4NCV66IW4pq-ye2dfcrhMj01hFA1rgIjZqQdk1fMJvSx_hh8wMJCP0vmw_WoYQrmuFzU4pLrIDoUc-ZnAHt5CTQptpZCKS6u999-Is9mZrSa9pKg7OgnudfzWNkCnbKospC1G5KSayxaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
