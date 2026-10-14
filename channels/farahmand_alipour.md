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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 11:20:30</div>
<hr>

<div class="tg-post" id="msg-6810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L1M_TANJoAIQhWOyhiaAsy2jtomelBt_cFN9Y6vX2dpGvYO8to8Eq-EnDICOICxgmtSYArzVufaK5ietHCMcb_83Y_o2FThz97BS5Tftfhn6hMjTQA_1ekaz48BDjr1fLPPBT6OkRFqCLHMXFBS0hLx4ypyOQvkHe8U0vktuIopuDYSvyqcQiJUJPsvHufg9Ts-ybdg652jw_jQT_SdCFRI25J2ohu2J-E8M5wTJ7YTVli_uOJ43c0UN7Q3W3aNS8Nyo1OpSO4-wEISNPRZxLTynDqfrX2ifE3AXd_daf1zmwjSxxzScSzpFFymabtaUrb22XRZUdhTplV-noY-IQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام آگهی استخدامی «خلبانی » ارتش جمهوری اسلامی گذاشته.
یه نفر زیرش کامنت داده « جنگنده باید بیاریم یا خودتون میدید »
🤣</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6810" target="_blank">📅 00:37 · 22 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW9CkvVaVmzpIvxMcsldzN85wp9cchB41V0pCS6D8yN7VVFB57jCL2CLRaZ-wPYLUqq7kOYq1Wt7j4ykPeG0P0SYzhtsPwXjZ0hiDDSlXDIpYW7EPjeo4AzzHKH62X_lT24ubinWBzn_KNSy2Nz5xGZJfr9AjIoiBDWia1fi3yMh_yBRl_PRXq112cZbVxiBI4PTI75lSQ8BLQd6PxCgWVXNXymZlKZXNB5IMpf4l9k3wlwxFWOi409MZQtuixXCeMNHz-575EDR5QLWwCADR3r-Y-wgM2SqlaRSpa-9CG2jRss_P7k4obMIELciHnKsheJjNzfYuXTmelrUXI193Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=fowpGnpof8-e1e86HyeTgFWLeLjjHL6DtZ9OECz5S5blUGTENbUj5YQuOL_LhDyRK-MSMpPQ9xRMVUwrm6WAYGvJ7RBAjaG8jbTfuHftrb4WfN39-upawezHaadVBZBWp87Rpqgj51g5_45S09dNcQmKCrMmVY-k3O3Qlhu2yYAOWv52OzwcNeOhYJ4gTY0H9FXRRQOd-xqKQrQZG4Cv8sXhAdUCs7FyyRNh6_9nIvAuk4bSippPaQheU_87e5nBZqyipKtHTkOTkvc_pafyNqrzKBuwjxdfMQpUn1sR_wHcQn7ESWwbgXY2DG9Orz6F0hL8w013Tt-E5EkfIdL_JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=fowpGnpof8-e1e86HyeTgFWLeLjjHL6DtZ9OECz5S5blUGTENbUj5YQuOL_LhDyRK-MSMpPQ9xRMVUwrm6WAYGvJ7RBAjaG8jbTfuHftrb4WfN39-upawezHaadVBZBWp87Rpqgj51g5_45S09dNcQmKCrMmVY-k3O3Qlhu2yYAOWv52OzwcNeOhYJ4gTY0H9FXRRQOd-xqKQrQZG4Cv8sXhAdUCs7FyyRNh6_9nIvAuk4bSippPaQheU_87e5nBZqyipKtHTkOTkvc_pafyNqrzKBuwjxdfMQpUn1sR_wHcQn7ESWwbgXY2DG9Orz6F0hL8w013Tt-E5EkfIdL_JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1HToD-m4hufu_X1IIc5b51DafvkDO2_GMeD_Se75Ntfz24NT-5ya5nM1pTV0L7VKsxi8CraTcEoh1rGzr-CO6_kEadqXYAKv16QmQbLU8I30llX0eFL45XEKKnmx8Z1qzxgQUJKamAm81xV-gQg2dhMNmSdat1zaZxKnEwrnlkPqlLXTgbRxuvwje5xjksBgjJ4329NEl1NeIVVDr1_RDhTEwCHlw9JQaYVQIf8rieG2W9sd2fWyZ5r-9yp50iDNgLyVd9886tZ_GihOqFzICMDB42Vxvqz65JRFZl5O_8t_Mas9BE6J-jwLGYJRd4tQs1IfSDo8NzXlD40WeWIVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1ykXoZwX45pNc1-7eEf92IhhgVvrUQeAdENiHWRYRAF1huRh8L3gVreWBW8yDJo9Sj6FBxA-Z5kKXtH1LXFchoOeaBiyObb8AuGEc8Aif3K0lldAdFuiYWNGLFU2M-CBsjIkx3spSTvJ40jjpGV1BWp5CR5M8zBXYL7I_K6R8tudy3BEVlQdBvPTvCJUiTEmPu59mGmQGArRtOfn9hgLCIQcm2g2DdlvO3HS7_gm8wPYuL36KtdOzSMOWl3WDCuSRS-EOx5wKXor50KZ5G9F_ikNTSgWVpUg6Ve99I1nzEEbDpMVYaJmRPWEnoWeYjcU-BU_ROj50hp_qFx81ha3g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=SHAkWnx0tUT6kClMIHqF9fCMvAz1u88M03iHjm33tYuUZBzu0it_zFVWHHTDOa9gYKROYmoo2fR83sU-YFe8KjItfcfVKsxIiQGVajQ1VCJAYaAlTQ_G417fNfPxK9mqyeOM4W1vK9nplwyAdlCnGWA5G0WAvdNoyEZkBxAwl-ZmW_isnF1so5N_hGWjnpYTdbsXfLQ_Dsp00q2ZKyrykW566iBsJo5wocd0_X22CKPyDzLOgx7xafmEfzHkMQLzKLsp13B4U6S3Nbh60uRYDNa6C5wh_YP4M5YnW6RMncAj486dGYSp1mJgbpvoyON8J8Q_FyKEafrYvqgN_9owurG47myEzJGLl5mPOsSwXz0hwXZfBRmXy4rNYcI-z5ELweCKE-gh5AafVTAQyc4sJvW3ERF7WbENTI2aYZa41mvgBruB_zKvSSLq6WUZ9_xwJUjH-4qHKDdd_Js29Z1r-Hr94wANzcWlE8tC8Bq9pb-ZCrH1xAId0X7XQOQ8ykTA-8oshb3jfzK1oSbHyM-TXpjz1IB0c6hyaxbrCtPCoyegpMuc-9fJSZQNeLpxK_QNL15s_5Q7ehU-5rTHaUrDtfMk6OJWenCh9yI2yJZeHQsYu6QtynWRcdLmdPSzii6wkvPqbh-g1a1I3TH4dy2CytL6InFqTmAKCCpNDy9qAB0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=SHAkWnx0tUT6kClMIHqF9fCMvAz1u88M03iHjm33tYuUZBzu0it_zFVWHHTDOa9gYKROYmoo2fR83sU-YFe8KjItfcfVKsxIiQGVajQ1VCJAYaAlTQ_G417fNfPxK9mqyeOM4W1vK9nplwyAdlCnGWA5G0WAvdNoyEZkBxAwl-ZmW_isnF1so5N_hGWjnpYTdbsXfLQ_Dsp00q2ZKyrykW566iBsJo5wocd0_X22CKPyDzLOgx7xafmEfzHkMQLzKLsp13B4U6S3Nbh60uRYDNa6C5wh_YP4M5YnW6RMncAj486dGYSp1mJgbpvoyON8J8Q_FyKEafrYvqgN_9owurG47myEzJGLl5mPOsSwXz0hwXZfBRmXy4rNYcI-z5ELweCKE-gh5AafVTAQyc4sJvW3ERF7WbENTI2aYZa41mvgBruB_zKvSSLq6WUZ9_xwJUjH-4qHKDdd_Js29Z1r-Hr94wANzcWlE8tC8Bq9pb-ZCrH1xAId0X7XQOQ8ykTA-8oshb3jfzK1oSbHyM-TXpjz1IB0c6hyaxbrCtPCoyegpMuc-9fJSZQNeLpxK_QNL15s_5Q7ehU-5rTHaUrDtfMk6OJWenCh9yI2yJZeHQsYu6QtynWRcdLmdPSzii6wkvPqbh-g1a1I3TH4dy2CytL6InFqTmAKCCpNDy9qAB0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKUA-GRoYMIBI9TymAgSvJBc7czbAjaXPo_t0tcwYndrQjfLj_ZGVvLTs5221VHszc6Ri2NY2tIywF4Sy6rEXWLE2r2bkJdbcqQR2QPaf-ZkLCZqhbzeL4D5v53Q2VYKZ5L9A122plctIFjfP35WSeaclWnhpE6faUhHX1xWISwYJqfhr4SABJOPqHCQLRUtTne8WtD9Ogq3wGlrcx-pOLm0rHCIKxOgUb4RBaMvhV2LAGw4MdrTKnoICJTprg9lm5TPJUnR1RDQoHQ0ZPLAShlo71qX4rfoSqy7G2ONrFulGxqJ54vOCURdv2lJ2FUklywh8Ex_tgjdEm7R9nMthQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i2qYD6WTNndkTfF4NpcWV0t3EfoOu9M0mwqzACQbp8eBapFo3XsHxIOJkBevlsKmLUqy5WZazvM11GlaCbUJ8ndCLrgJ7jERFaZojg6EVi4QItjjBJao3YSgkBWv6H-gFV2KW5_UgALyX-_Py1kGHnzeh0N3K-t_Hm6W9iOBOZAtF1IMOUpDEWgDjwFhjD319TG5q4dx4zYUJ80xXQIj-V9Er-CKeXwepPGTybIUReOr--hhgICSkb3DglZDBPrQ3p0BpB_WkMAtjsgDxjzHRlHKBLzdk4xL-ZaAJqmd_lQHPUQeigCTlVyfGm9heikVygbkE9ChymL7RRW2CP0HSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hd3RkBWqcri4HCg_UQwpcEpgDkJptlaCvhmgLVu2V45EGmkQDf8A_2ktxkX0lrtmYyW9nb6P1BoWaZrbxpfrAmRzOqgM0abo_H1zGF39hzNm5-6HDjOSY-McbxxWZ625PKBC_-HsRjC51_gfx8ZrzpINUFWXhYpzFJv6mjhkhOUrMYQHz7nGobrgCMiVpWiPf3YdZHq8aDbropgqyX0d6eb68tS83nrUnMwuOFf8ZrREtmBoIpuwZBuDyA4RvtMJieVIQ4d1zQFQ4Ber1vOePq75jFYzPZxFJRiwbGJZ088XrpSLw8qtU4XK-zf6_cDS8ledPYfi0xKo66mHPL2zrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHm7HH1r447n8tKBUOZTrRx5ziMQNNlvFijKR0_jaAhalr30AF-Q1HApcOdyhQWOffXm6qTBEvAUo4c9f2wAtzqSUBzRYSs9tTOytVNxznvfJy-iFIymFSttkHSxV5Zgzr_NykrFyuaza4MMgYczwaXWJMgaucXizIYX3tqDNY_nRABAwff6ZwjLLn9D39-9GId7_348Scm4BjEohipjCNdTg-o6k1vtStoH6I_Ohb_MCk3-qQHXV5ONokJEWytBeZmjKevZkzqdU4nmu7N2cBenIfM1RtLqqsjnwKFFT0VY3U9JmLoCpxMR_3yOaZhB97OcrfCS9GB4BxXAwQPSeA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZWTuZJtsc8cNhtrS92O70Qf2FqGdEH1K0XnpPNQhZJUKZ7RCIHDhTCeazzjidsIrylLKir8NaMpYefG4QLC56rJ_RVKvLu8XPw6y2yRgp2HkxYXBci8ymLiHnM0O3CqJl36YTugy6ml6AWaTPDYKUfJ6ykP6xs3gdUrwK8TLmb0etiaHCn4okiLTW0T_t5JJru0gz63K_VCfE29gk4a3XupNX6zBy-UNbPZWTvb_CXaQrI8GdJ1EWmJnp00n8QQbbrklBUtlXsMJkVOCaRfPhM6BBpfN5DjxRzAAFGYab2JSJE6yYvtiZtfSCxicYXQ7VuAZWJTWLVSetcJTGWGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilpHykldU0e9xkMSn4mm_uKfNL85NCnMAt0r2AGuBOt2NFbR1zQKk4I1R_m728OzbQbB7v7LG8NhecsGCBHFyHhICZ4ahXGWc6FYeLS3vSFD1-Ln8dsZ7l93TMymEHiMzs_361hLkBRirINdJMmakCCdnjrCR2ZUonTZ5iA08cUIbiH-5gX4X3I3I1ddrL2Ebu21RwohnfYXBwPsUSfZy8ReUheZEHbjbACG3Y1C1NFcTUY9gfl5jqvxBtQGeojErtJ8EvGgYGDG5v7i04cQQzP_Huwqcx2QUzIH5W3FQ2RC3ND3pUgJAOhjzWiruYKaetHjiWETZN-1qpoWHOxh2g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=TsVo17zAViXBkfVR-tS1Wk928Xx4kK9rCHfBSfQv-Gc65WUVp0kLrtY-xql5kEQqfoCFOXc6assiuc3YFvK7tP22DD9hcEAIJhjlzPuvFHXuRmS1G96_zLXgwrw1EeFR6ubglm0efeStmoCBpuDIpDj_zcFoOTyNgJ2QYnV3SQFL4h3oU4JIoWt05desCj5bw30Y7WrHeEjgT7FoSzP9YQTrx3r50obnLOe_IKqai-3Z1VB_Cm7qDnam8hdYQBz6IADaQOH4wOGOgDmjzUg-lCt1jtxikLg1mV0lrpDPVnB_xMTeCsrH1m1VrqA5iUsNCj6vTI1GGHmEKz8nVSRXOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=TsVo17zAViXBkfVR-tS1Wk928Xx4kK9rCHfBSfQv-Gc65WUVp0kLrtY-xql5kEQqfoCFOXc6assiuc3YFvK7tP22DD9hcEAIJhjlzPuvFHXuRmS1G96_zLXgwrw1EeFR6ubglm0efeStmoCBpuDIpDj_zcFoOTyNgJ2QYnV3SQFL4h3oU4JIoWt05desCj5bw30Y7WrHeEjgT7FoSzP9YQTrx3r50obnLOe_IKqai-3Z1VB_Cm7qDnam8hdYQBz6IADaQOH4wOGOgDmjzUg-lCt1jtxikLg1mV0lrpDPVnB_xMTeCsrH1m1VrqA5iUsNCj6vTI1GGHmEKz8nVSRXOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=RxGfWcoHpx9s5QmAvGriNPIReUccqt3Tnc8oja8oUXQXct_JpPLUaApq2crxJFRhqNDfVTA_ngZHqX7J3eYHotz1j5BollwwyVSJahBrKj3f0rABzu6KBiQZG5MhPunMn6FCV1nAR82udqE_0C8nkyuLVSk83hHT0QYkb1OxRPvJCuru_2OCXT9P5mYi13VseHPRVhjybW8xMXURh2vVxf-xsD7oLJutnJfVUP9nkTbzus-oty45DcR2o_7nsRdcgVQBPNFElVfQD6q3W9U65UIrLJMqWNg4IaH-M5tDz5P7SDz0ocwCg9DQMFoK4DG5KoO8Y-tCxPtqKaCW-iWrcrHegYmW2Z0uWBgw2y3VMG2j8PAIf077mHGlD6WD3chQ0zzohlxzDs_lOXr8j75XW7aE1y3oLQBzlrqoPNVxEcZt0N4sLIapUTWrSKFy4bxXVGpwgvk88Qr1K31QP5wvhc_oBo4WzhzUSEA85hM9qpCDuUc1uvdepp58ERdqHFEuTmNwBpLOzjE-f2ojL1vuWD673TolYxWhEMxm9Hpmm2YJmVDrIuwn7wHU53pRV4OC1fJ0VYTHSmu2UQqLQsaPaOVd5IxJHcoJZllaNQdbX6TUF6cwcX0iNhq1fkHTJtg4ehEqC-G03N-v7UY40Oumgg_VvmX8BZv-x89OomZCxmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=RxGfWcoHpx9s5QmAvGriNPIReUccqt3Tnc8oja8oUXQXct_JpPLUaApq2crxJFRhqNDfVTA_ngZHqX7J3eYHotz1j5BollwwyVSJahBrKj3f0rABzu6KBiQZG5MhPunMn6FCV1nAR82udqE_0C8nkyuLVSk83hHT0QYkb1OxRPvJCuru_2OCXT9P5mYi13VseHPRVhjybW8xMXURh2vVxf-xsD7oLJutnJfVUP9nkTbzus-oty45DcR2o_7nsRdcgVQBPNFElVfQD6q3W9U65UIrLJMqWNg4IaH-M5tDz5P7SDz0ocwCg9DQMFoK4DG5KoO8Y-tCxPtqKaCW-iWrcrHegYmW2Z0uWBgw2y3VMG2j8PAIf077mHGlD6WD3chQ0zzohlxzDs_lOXr8j75XW7aE1y3oLQBzlrqoPNVxEcZt0N4sLIapUTWrSKFy4bxXVGpwgvk88Qr1K31QP5wvhc_oBo4WzhzUSEA85hM9qpCDuUc1uvdepp58ERdqHFEuTmNwBpLOzjE-f2ojL1vuWD673TolYxWhEMxm9Hpmm2YJmVDrIuwn7wHU53pRV4OC1fJ0VYTHSmu2UQqLQsaPaOVd5IxJHcoJZllaNQdbX6TUF6cwcX0iNhq1fkHTJtg4ehEqC-G03N-v7UY40Oumgg_VvmX8BZv-x89OomZCxmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q_lyT7ft_UskMxXawH5Jn6n7BMTfbZZ415783Gy4u8FT90zSo8Jx9mA_WMpv72PH19UVXOuKWgFFR6aiJNMWMYCq0_b3T-4W8xxlvIRzHqOG2PVwqOfWWop-fpoDozqQwCM381IZzXXGm4ZAYgVXUYO4Wue6KO6oj5VS97CoItFNIEd2lYd7PD99dSP8jb-EckoKy7PA8-iXAz25-TtM3d83csGWJpUZls4Vi1DThgXkmTJhGNG0jfA34zuszkYVspLdcsWVh6wR-Y7eBQMUmJXi1aYc9tcvLypn3Nu9Mj0bgCcpEd0WBfmjQwf3DBTd9ifaU9XzeCR4wWIj0O4t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iq-VsvOjr8UTreo2UoeZWb5WbQQS6HDoG1mvPuyaO61gMyhfMLtBfn-YVa48XVpGftvzRet_QFK_WRZzU3XCsLPZhwHhATyPKUQjftVPZe_PYQPxRPGQ2v9LtL8StdPwdC2XPHHN6CBQv9H0ZvnJk5qRRwdhZl6S7LB93uSTQjRocf6PzEEVYWNvqb-oR39Hwft-u89uWnnOwcK3913eaoW4DcHhBvLkxP-ivut1YGDBgNrp6cNfCbK2qDpLebW2zvrqMc5qHCKylXffB3aRXqk9PCGRibXssi_y2Vq6cqg3YuIg74GV3ihjwlkA38s8qPSqwJIKj24nbNDwjxAP4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAA1tcQGCu1Cj3SK_U39HEBZV53t8oAkCi5H2J42q8lR3_xqyzOk-8naiBPG1nBdDz6iE3Wg1Izo4AWLyk__alyKgeqD9w8xePMcvFZLjwIjZek2ZChXI4Wl9r_uWn_h7vkb4ri_7Q8U8Ft55gbVHMV7YzeIzaY_7xtYJj60cQRC78fh9nFEI4F1b0EUhCs-2RIhaCIncj3Y7k2bJ41qXcwSrcxAJsPZ0YtKBcKrDmc4gEwarsjE0RuOWNek_iZWuPx7PZD77GPxKzEif0Sb-3y8hwzuoeahW2gI-owePKi8zylvCcjdVIPw5X6GLz07L3UATBCk1e6LEUAd5H3TWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=E6BfFeukAdx4yZZfxzLuucsHwx5ItVYPlGiaAMjCy_K7BzjSlqEKq5W_O539Qhjj92CpZzdZBnCw5ac3Mpvcyfbu8quU09mdmIsI1ucpS29jjN8RDFG_ifBAPJdlUtQ3OLfTJbdU314cYOQgqMh31Lp69T6WXFXeIxE0dQJWxUQd42DhdVQl79pEtC2mUHEhu4Emjhc9W42DMZZqpFzUCGXxgEinL9sc3sFzgQCxf4uB8lTArXHZMMlTeNZFsCg4bXKIqVtAsqCOdcTUXo58AHQORfixM2Abwf9F6GbsvB8_CsGa9QWtZC7CJNZ3XmNYApNyow8Ou4kqzNQO629bYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=E6BfFeukAdx4yZZfxzLuucsHwx5ItVYPlGiaAMjCy_K7BzjSlqEKq5W_O539Qhjj92CpZzdZBnCw5ac3Mpvcyfbu8quU09mdmIsI1ucpS29jjN8RDFG_ifBAPJdlUtQ3OLfTJbdU314cYOQgqMh31Lp69T6WXFXeIxE0dQJWxUQd42DhdVQl79pEtC2mUHEhu4Emjhc9W42DMZZqpFzUCGXxgEinL9sc3sFzgQCxf4uB8lTArXHZMMlTeNZFsCg4bXKIqVtAsqCOdcTUXo58AHQORfixM2Abwf9F6GbsvB8_CsGa9QWtZC7CJNZ3XmNYApNyow8Ou4kqzNQO629bYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=gLE_s2Mk2CwlzqfqCHCNOYe6HtIpM5Nx4fPgKiQArP9Rz-0TEfUjf5ulizUfhvcWRx0NG1w_0JddH4WtmpqVhf4wfMKMy7LNTxtf4qv2V_OATsDOGWba3mTTcRnTStKSl4OO_9JmeJ5NfuFl7GMcmUljLIXAI9BqYchSMbxAut9wgZQi4UaA_LlhxlNXdqoMq4Z5Gys3qXAteIu4uXCclYEUdpobw93dC-mqx2wGW1GKDheOjgJ5k-vWQ4_AwJq68MLe-5jaGNkzcUNMDqvIafd2mLOkyORQ19tlfc-UGp2Yk5m8TE84eFwKUJbN9jSOitUnb8nm2oCqFOvKatEPgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=gLE_s2Mk2CwlzqfqCHCNOYe6HtIpM5Nx4fPgKiQArP9Rz-0TEfUjf5ulizUfhvcWRx0NG1w_0JddH4WtmpqVhf4wfMKMy7LNTxtf4qv2V_OATsDOGWba3mTTcRnTStKSl4OO_9JmeJ5NfuFl7GMcmUljLIXAI9BqYchSMbxAut9wgZQi4UaA_LlhxlNXdqoMq4Z5Gys3qXAteIu4uXCclYEUdpobw93dC-mqx2wGW1GKDheOjgJ5k-vWQ4_AwJq68MLe-5jaGNkzcUNMDqvIafd2mLOkyORQ19tlfc-UGp2Yk5m8TE84eFwKUJbN9jSOitUnb8nm2oCqFOvKatEPgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jMnChiYYGpJqg33dkxv7-mnDLRczjroSaynUw4gb6IYGMgSR3czSCWkVkBFEU5h3RejcZTlnXloYmUpg3EQEcvodiCtmVCVYb5iPc72yubwGT9Q1zwYIwFMju3mc3NL4c0FuFHwYDOiWOVBd7HlShmFJJmFDLC0jWV3IZhskcF9CEoSjpovg0yWLdY3M2obEUqUsNXYuAlSWhNOfUr55v75ekBvNQPa4FzN7d3FE5HHNgppOrVTVfX2xRvKh9tH_n-MiL2d-iFDOKqEyv6DXg1lswpn30Un6MFbaha-4k9hB9eUk9q9DL0UY7lbH3p3zvDwoQnPZXf3c7E3o5QVbBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Gi7bGisJcFnywr9EcQmlGVZQoK1kocqC6HO2twkHSMfHSYkkn9QiqEGRotnxaJVScaxxNSFmFc--mT7kYGYuJNJXHFRiR-1zwh72ZprpWA1jl6TDQqDrC4ohX6dblZra2WkdX_mO_I7fEQYysQwD-IdNihB_gvIFeuDvMy1jaXhYA_4eWmAKUCkSL1ZUsbfJ8Qy3Y2cDfA-PXdCrFt2gtWcnpkWs0cp1yBU4_f5D7L70DAaIjq_C0l4O5v2B17hRwGSVeyYdoOyCGPBZoBM6uvg6VNiDpnurb98LEMhVpa9KjkdjlZEuOOxU0WLvVtvKoy_8-vwm7sH5-_QU8Msh0bmWKnUp3kWrRl03lS4-NKY9CloJXzh7HpF5q29hhlmUj1QfNEZ1Ahfzs9GQxgXvFNMICVbZRuXZ8HfSuINbMfNa-nHtiR4TGS1kmeNMzph3mkGt6gX4Ks0D_ySGEVFE_qRe3EbNcrF8imwB9KoVpkdInkER5IdfwPh48KwGuRq4Vmx6Wl2FzYnbbko-725OMjJNqbwmKsiZ9-F6F4voppKt0j0m46VFcyH_nBxXR9BM8smPwPcjm4B6zpDslQTyv3eu-n7srDHrgMj0II_kAb_R_RK1nAkZW-4uXQNM85fYNwIfUbfbtkLihr91p7eoEzno2l778NI1mbogX-Zx19w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=Gi7bGisJcFnywr9EcQmlGVZQoK1kocqC6HO2twkHSMfHSYkkn9QiqEGRotnxaJVScaxxNSFmFc--mT7kYGYuJNJXHFRiR-1zwh72ZprpWA1jl6TDQqDrC4ohX6dblZra2WkdX_mO_I7fEQYysQwD-IdNihB_gvIFeuDvMy1jaXhYA_4eWmAKUCkSL1ZUsbfJ8Qy3Y2cDfA-PXdCrFt2gtWcnpkWs0cp1yBU4_f5D7L70DAaIjq_C0l4O5v2B17hRwGSVeyYdoOyCGPBZoBM6uvg6VNiDpnurb98LEMhVpa9KjkdjlZEuOOxU0WLvVtvKoy_8-vwm7sH5-_QU8Msh0bmWKnUp3kWrRl03lS4-NKY9CloJXzh7HpF5q29hhlmUj1QfNEZ1Ahfzs9GQxgXvFNMICVbZRuXZ8HfSuINbMfNa-nHtiR4TGS1kmeNMzph3mkGt6gX4Ks0D_ySGEVFE_qRe3EbNcrF8imwB9KoVpkdInkER5IdfwPh48KwGuRq4Vmx6Wl2FzYnbbko-725OMjJNqbwmKsiZ9-F6F4voppKt0j0m46VFcyH_nBxXR9BM8smPwPcjm4B6zpDslQTyv3eu-n7srDHrgMj0II_kAb_R_RK1nAkZW-4uXQNM85fYNwIfUbfbtkLihr91p7eoEzno2l778NI1mbogX-Zx19w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=r6TGD5Rgn3ZJRSp8A3EHFKEuOveRcY1LCj6HFCHwbh3UWfZ1aFRa31C7ANNkAQ7mqJVflWx3rWhMSBqU0xIVx3sFkM4f5AatE7gcdtHfqDareIv8-_LHeUYJ7ow-RxBLBQwmZuD8XRMnqwpqebTpE4mwOdNrUFkVYtJFbLPy-ToaFh21rb48EZitl2d8bJvZtM-elgJ7cwe1Z9yYlyQWouPS98u1vuT8QE5J66P1iULWQF6zqcalNBol61b4XtBygCusFFCKIbcsYNgGugazYDSmwTnIloj6k5DUEMQr-7KBz8SwMJdlb_IXrP7wYXS0OHPul6hlm1XxDh63rGHlkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=r6TGD5Rgn3ZJRSp8A3EHFKEuOveRcY1LCj6HFCHwbh3UWfZ1aFRa31C7ANNkAQ7mqJVflWx3rWhMSBqU0xIVx3sFkM4f5AatE7gcdtHfqDareIv8-_LHeUYJ7ow-RxBLBQwmZuD8XRMnqwpqebTpE4mwOdNrUFkVYtJFbLPy-ToaFh21rb48EZitl2d8bJvZtM-elgJ7cwe1Z9yYlyQWouPS98u1vuT8QE5J66P1iULWQF6zqcalNBol61b4XtBygCusFFCKIbcsYNgGugazYDSmwTnIloj6k5DUEMQr-7KBz8SwMJdlb_IXrP7wYXS0OHPul6hlm1XxDh63rGHlkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfLD5Rt5FftYDGzaq16tHNYYtnktgKDYL4kIym3DC1KPECGrVsD7D4YZu-EV-e-yC-pY-1ONJGT98-n5Di_p8vRMB7uE7XyZ78i7c27Te6l8PAhWrf7i2bqyCr0McxaDb4YzCqWuOfv-26Q33oVMv39aKlQyyvXMZM7LFy8UATANUW7cazKHm8ogBeYZGKOGkfs2W6vmdZXxKntaa0Q2qTQyB4kV7a7ddaCXzR77_kFzUu2hI9S2PmrS9pzDtM18_M9DhlMclkzRfD_ncb6Xnl4yNoQSNLSS8faYyX8a8rWjPjs5Mh0elxDBglrexa-pSsYrGV2cYVJKb7XrSGuNLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=Tpo_x7LSQ64e544gOrzdkzxSd9QmWFbBwZF2djgGLHaqD5zMxTONlvyfWGcZDnaC-KoQW6mSjObBY1HGDKjVzlPyUaP1GFN_cdIarZbNlhISv_mRoiskuPcytfOy-T2CquhHYm01Llr4IN_lZPkhx6k_xMn8bHee3nfy3O03h2ya-vw9Ff1uH86hGqSWCKJugH2oWowjV9hEl8w-jocW3w1ij8EeBtg5n1DZq-gnLPzZhsI5s1fZuYP2Om9Pc9Kg_t4cIpfE-tLIaD6J0w-ZjesiECE25QhlZ6DIFAqjNFp8x7N9tgXdI1F1Vy6qXeJjpIYBDIABxhQkZJ7fAZq7TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=Tpo_x7LSQ64e544gOrzdkzxSd9QmWFbBwZF2djgGLHaqD5zMxTONlvyfWGcZDnaC-KoQW6mSjObBY1HGDKjVzlPyUaP1GFN_cdIarZbNlhISv_mRoiskuPcytfOy-T2CquhHYm01Llr4IN_lZPkhx6k_xMn8bHee3nfy3O03h2ya-vw9Ff1uH86hGqSWCKJugH2oWowjV9hEl8w-jocW3w1ij8EeBtg5n1DZq-gnLPzZhsI5s1fZuYP2Om9Pc9Kg_t4cIpfE-tLIaD6J0w-ZjesiECE25QhlZ6DIFAqjNFp8x7N9tgXdI1F1Vy6qXeJjpIYBDIABxhQkZJ7fAZq7TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AyDae9--dhGkO1K2YSjWV9F3Je7e0NP15xqAh0R5R2HH9idiL0GtmQBmfLVS_jH3RIy14Ewwaqe8YTExQBlunqB0nE8V0NXnlbz96G2xQeJCr5bmGloJidUkCf3xMtFGBmu_n9_hLuYb5GLPG1LIojXiVX_WEtH61P0BF2nNIixCeJCGn1mQqE3VksFMN54Lloz88RSR9DDqqjvVdXM6BKiKKZA4iHy30UGFhRLnlNrGXFYwwSjvKRaAMuEXhFTvDmEYfFDq3CEPTqkzOk-7mdRrtehqqavERjFXtekofVsmqOpj276ioljHJO6axx9lnSyee8gg_iFr6GGIgkPMWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOric7bIjPqoeDiEXQygJHlpw1RzJe3YjJALxCQRW5EdO1gKM1U8Nl_hZ5fENFWUs8a7--4dHBDK8neT0oWchNo89XZDe3raGJaYhaDOEFcOyFPok9cSUpwRfOApasnOgM7XwEbeamW2N6aQ6LQT6pTLROGNbR7L6YhjkTcXEVH8hLgwDmCEsCdJL8t2OcO71ko7WPnXLl4q5X7J_6A1S_q6yKaQMAittLcF3glOceWS5agcNfDCBY9X7ryC3hqxgXb_btfnWJFLk5VaiSrRcoPp2hn61YVJe9KzTLMpUVu0O_5Jj3wcbLfD-t3-SP-q3s7ntTHUhH32ojMULuIu5w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=khzH1BQxavcOEh9Vubf2_gc4if71RDlRcXqDJjhW18hQzYMPWI7ctfqg7Zvi5KbCj1YxQhq0KX3YPwaJVKFvWhUMRCRWPDO0lyQcdWvD9ODeTwqqdi0Qk8XX40M3l_FRerkgYswcy0nOhrSKyZes8YZpB-XwsOBIlc6EPOXWf456Cb6H4rfLQTvCBQJEElwaFwh1MH8D6F9dnntztdhSsC1bM-9tB59oYlcVJIVlE7fSMH15hA4vHk7VUXsfftefn1GMsOLXysGolv6ED0p-zc_5mcFd62JG1X2UhwtrNon4vEmzs1xEV1ezx_iu9DGMroB7PkEaquStQS_p5kfYLpNS-F0eAUIH93JKo1BklDBvaBisEPFHf95w3p-q3DldHJLTEV_iicdYH9QhuBJQMyi6bAJrbGuIMScd1B_6W_vhbPZDESBWpRcQFN6pbIv3MOIMVXgTSvBPPxAv-s7kjckxpKluM9S_jNB39nwaaQuBrg9eCv2NAN91g-3gqxsag7Ah8qneW0PQtI1-CBWJ_nt9gfuBMIxQfjB52P503iDXrxi8Jj2Gjtyns7UQCgaaHoQEExMmwrbfhupvOGfj7AJ0lVd1Ux7nZ7L3XLtKIuyJ-wOzSu5CFedIn5_owykps2hrHas5ORew8-MW-wSZWsKCYdZd8OJ7cNf_61qe3Uk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=khzH1BQxavcOEh9Vubf2_gc4if71RDlRcXqDJjhW18hQzYMPWI7ctfqg7Zvi5KbCj1YxQhq0KX3YPwaJVKFvWhUMRCRWPDO0lyQcdWvD9ODeTwqqdi0Qk8XX40M3l_FRerkgYswcy0nOhrSKyZes8YZpB-XwsOBIlc6EPOXWf456Cb6H4rfLQTvCBQJEElwaFwh1MH8D6F9dnntztdhSsC1bM-9tB59oYlcVJIVlE7fSMH15hA4vHk7VUXsfftefn1GMsOLXysGolv6ED0p-zc_5mcFd62JG1X2UhwtrNon4vEmzs1xEV1ezx_iu9DGMroB7PkEaquStQS_p5kfYLpNS-F0eAUIH93JKo1BklDBvaBisEPFHf95w3p-q3DldHJLTEV_iicdYH9QhuBJQMyi6bAJrbGuIMScd1B_6W_vhbPZDESBWpRcQFN6pbIv3MOIMVXgTSvBPPxAv-s7kjckxpKluM9S_jNB39nwaaQuBrg9eCv2NAN91g-3gqxsag7Ah8qneW0PQtI1-CBWJ_nt9gfuBMIxQfjB52P503iDXrxi8Jj2Gjtyns7UQCgaaHoQEExMmwrbfhupvOGfj7AJ0lVd1Ux7nZ7L3XLtKIuyJ-wOzSu5CFedIn5_owykps2hrHas5ORew8-MW-wSZWsKCYdZd8OJ7cNf_61qe3Uk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0ezalXF2QYaC_gbvKLEwBDedmCIsldpVEVManRsDxhtfaBgiouYGbYWkdsAvnllj_leipZyUUuHdlSvVOJCDHH0V3NeeebTOZn9Mh5M8JdwltGHABTHA32PJlsUffF6kq_SsKcN0O2_gknGGfKjgdmXbJQb9XynxQv4zSZ8GABNRor0qipcYapUpLaZ31tVdaoFB2qENL3ZZiOUGytqmv3EWynLZ0ZugNjvkiL0pHFPpjWbRy8NxyKQ2vEu46YyVDDhFcQzeO_ufsMJ79lqjMhuu1EVKT2IbCNSxxufIH-ZIT4_hOqQ-WKiOx8QzQcyTdWVeJBu6ds5Fko0Ko1QNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBY_NB03vpBIvvvS5dlB0gZB6gg0lNvmtXnWlLFHLHJF1odDBpJUNxw4HZ3OjreLFfMDarY6wzL79xiQezqVkRK3y-_TntIES8_CKA7KXjvnA-TQVpSGuTbu4AJVSpk1W9anzBBq4bAN2J0z2j-h4E3XGg8bOHJRnU2iA33QmWyZVhjltMH2tyZ4C-1q2x1U4Hxt0hKFlWkyckUMlnezWGwZmrWPL8CWj47s-dgh8pAZAoYiXtLFwC60mX-Xqx6DG0bx6gBf7wOE0sMRoAA1BYZCVGT6RbZuSR7f3bi36UYeHuM-PMbRChPOJTyB7zU97cLyv8p3XEpjARUL9lUOlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=uddjsTjnaASTRsYsnhgOpNBryO1ra1oV-A3cwoILMd_ETLn5CpLPNIsQAGUrR0lp4uwMQy-TJWRfwM0jTTWAf48ICVuEHUyG3ZUwsw7AZqd1w4u4pFteNACqrxqwHXKjzBAF2wxjrMw0z8LKXg7hUdJaIQ2mgD2DnC82fULQ9OJz7cYBL5OPUN-rtFb_Zz-T7baj-RUnpMdmsmKOi2dBFHbmAjsZPEg-Q3cWGuZR663Iq1rhjR2Ro9RfBtVb5KN05I0guR0DiVPxAidyUPvJb2k0xKBt2PzfkxP5vgBPSgnSBxJmQCx3pzvpoMCJ0T1RWlxegFji-aAB6m7SQM1BFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=uddjsTjnaASTRsYsnhgOpNBryO1ra1oV-A3cwoILMd_ETLn5CpLPNIsQAGUrR0lp4uwMQy-TJWRfwM0jTTWAf48ICVuEHUyG3ZUwsw7AZqd1w4u4pFteNACqrxqwHXKjzBAF2wxjrMw0z8LKXg7hUdJaIQ2mgD2DnC82fULQ9OJz7cYBL5OPUN-rtFb_Zz-T7baj-RUnpMdmsmKOi2dBFHbmAjsZPEg-Q3cWGuZR663Iq1rhjR2Ro9RfBtVb5KN05I0guR0DiVPxAidyUPvJb2k0xKBt2PzfkxP5vgBPSgnSBxJmQCx3pzvpoMCJ0T1RWlxegFji-aAB6m7SQM1BFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=G-dlytmMfB48CSUc3KmFNYwAxkZicT6b7Ev4wQCYs1Gglb_Ct3nOxlSZ2O-0dmrGIi9BYZFCWQkrQ741EhPolu-IpdjmQ2ESi4lJQ5W_BwqBpm_QEVTuWoKxNCfxp0QHLTNl5Jn0l3QJjp9H15XLqsBeh61qj2QIG99bBeYHi7FFGa11EDAfOGBFvVj27yDb3wsLoyXmSO_aF2oScc-lnNXnetBMFyAShlgbL_y8yaBkI1r5_zdonLpn4ttE-v9OFkVSXkBhzWWPiLPYD0OX98HB0WmtpHlqtlmRIuCYThiMyTvv_29qheyJD1zUwqtKpnryDjaXHNVgqWg1DH9oPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=G-dlytmMfB48CSUc3KmFNYwAxkZicT6b7Ev4wQCYs1Gglb_Ct3nOxlSZ2O-0dmrGIi9BYZFCWQkrQ741EhPolu-IpdjmQ2ESi4lJQ5W_BwqBpm_QEVTuWoKxNCfxp0QHLTNl5Jn0l3QJjp9H15XLqsBeh61qj2QIG99bBeYHi7FFGa11EDAfOGBFvVj27yDb3wsLoyXmSO_aF2oScc-lnNXnetBMFyAShlgbL_y8yaBkI1r5_zdonLpn4ttE-v9OFkVSXkBhzWWPiLPYD0OX98HB0WmtpHlqtlmRIuCYThiMyTvv_29qheyJD1zUwqtKpnryDjaXHNVgqWg1DH9oPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=tdvuZ_Kmk8R_4l5Ssk2i-d4rDo31ErmVe3cEdryG0_GVefkN7oCY6mf_TIAnSZyghu_n_8Dw-HLKtwbqxa66aPY3YvCNsX5f4rQ0UjtGCgKWjX62Gm-4e8cGKIfNxOBmvsYXjkWY5vUcWP-_cwpS3jCPqi-sqc8V8soR7SFE6iK9rLGKu8u0MYE22aNcvm7ODek_YWDkUSB8uVZPfHM-o8JL3YpwIH4TCxLJPXDUkmMfIpSpfl4fnjCogHKPeUOKy-bFaPi-pRHxzKBEIP9mBtnOMR5B2HYYBtfLAHHDRlWij239RNuGl_MIABGmxQyCPKHEJvaaJJhd8mPkuqFQeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=tdvuZ_Kmk8R_4l5Ssk2i-d4rDo31ErmVe3cEdryG0_GVefkN7oCY6mf_TIAnSZyghu_n_8Dw-HLKtwbqxa66aPY3YvCNsX5f4rQ0UjtGCgKWjX62Gm-4e8cGKIfNxOBmvsYXjkWY5vUcWP-_cwpS3jCPqi-sqc8V8soR7SFE6iK9rLGKu8u0MYE22aNcvm7ODek_YWDkUSB8uVZPfHM-o8JL3YpwIH4TCxLJPXDUkmMfIpSpfl4fnjCogHKPeUOKy-bFaPi-pRHxzKBEIP9mBtnOMR5B2HYYBtfLAHHDRlWij239RNuGl_MIABGmxQyCPKHEJvaaJJhd8mPkuqFQeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ouPFVohfOT9-umR2_dGkAG9rFJAOnnt4I8u4aMSZQzLEVIdkn76w8Ks4gxT6lDS63FBUsOYWI0f5N8UlO5uNFZr7Gz3dxZv8JgsMUJpoqnKiLtexCqph1tng7-XDeFEIhAF-X3giGyyxspOwQY0qYTsO9ouM9eVshQUdpNbX5Ht__AVWPxgrayi0tjob3WppluKQwn3OIz_TDSdCah23oNeL9R_0qpNjcLccvzpRr9d4JffdS9_R6LLhTuz06jOTDP8kROJU29sRbcYCXD1LB2WKOEVNOD0GK8lK56WTdTWX46r3pRlu8bcsU0weDW2YKWZSC-Urxg9yeK1FoKnt0Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBrowvrrSTL1F5xaZwEDLB0xIZI4ARRLRkfnIZJykP53tO_4bNAvaWlyRYJo0TeMIjbUG-LR5etcI8XA40rxUVqzWqsRFRK4ECyGRY9emqGrEDuzA5CuaEyQXLeZ6GHELghX9rNkcBR1OLmQG3NbDuA4EXoud4Z9GhJGgBBYQsdP7kglCKO8-sT4MEnaRQ9d91iISht2WiLIw0oFQgv0-KVe8Ho4MES3KXC1xqdk36Fb-XBiPgRwaNPGLO6cWLFcqLnQCkI2y7Ok2YIPQd8WjkQE-ZgKMsHvCcAIGs-pAUK_hSNK4XYIXdq_H3al3wpc1WiIWFgBX_MS5dUweL907__DoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBrowvrrSTL1F5xaZwEDLB0xIZI4ARRLRkfnIZJykP53tO_4bNAvaWlyRYJo0TeMIjbUG-LR5etcI8XA40rxUVqzWqsRFRK4ECyGRY9emqGrEDuzA5CuaEyQXLeZ6GHELghX9rNkcBR1OLmQG3NbDuA4EXoud4Z9GhJGgBBYQsdP7kglCKO8-sT4MEnaRQ9d91iISht2WiLIw0oFQgv0-KVe8Ho4MES3KXC1xqdk36Fb-XBiPgRwaNPGLO6cWLFcqLnQCkI2y7Ok2YIPQd8WjkQE-ZgKMsHvCcAIGs-pAUK_hSNK4XYIXdq_H3al3wpc1WiIWFgBX_MS5dUweL907__DoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aNVACQPJmpNoEFZHgTi_V1DZcB0ja6iZukCx7BihDASToVl72YHsTJW5PEBlEvMHMrfKJtuF4ACYMxd73cAVNqUwN9hXoii030yA0gjCg_ywGNOzh6BKE9a64gQIVbcU2rFH9LxH89qkES_A_orfQwv3DZ1MnRYsm8khmhbUD6sSul4iCEGyZM1JzO2hSkP__X6ZRMR9n8k5dSrVuOjAQ45RwDblEOxSWwejrvsc3h9hlyNe39ajBrOCKqU8ByxXqQ2y6iTxZ_RIbxhqTPe1i6H6teTiyn4_Qw67uyrkNHeL7TpHu2sowgk2m3QpsVUuNLdNYGexEdqAnp59uWbUWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aNVACQPJmpNoEFZHgTi_V1DZcB0ja6iZukCx7BihDASToVl72YHsTJW5PEBlEvMHMrfKJtuF4ACYMxd73cAVNqUwN9hXoii030yA0gjCg_ywGNOzh6BKE9a64gQIVbcU2rFH9LxH89qkES_A_orfQwv3DZ1MnRYsm8khmhbUD6sSul4iCEGyZM1JzO2hSkP__X6ZRMR9n8k5dSrVuOjAQ45RwDblEOxSWwejrvsc3h9hlyNe39ajBrOCKqU8ByxXqQ2y6iTxZ_RIbxhqTPe1i6H6teTiyn4_Qw67uyrkNHeL7TpHu2sowgk2m3QpsVUuNLdNYGexEdqAnp59uWbUWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnHn3fldGURuA2iF8od5b90eecMoff2rw4x7ZwFTLw4kTq8dLtOM5tKrYtS485zA2iWZ6BX8X8xgraoIwHqsAXWl7jDi6xKDR_FbJc-X2t8Wsml2htVHLv6lJCXhrhY0LyMJVaLuVugOiVw6KpSpf2z72miFE1FyPXY7TM-PKGQTp6rBf2o5f_TV3qpa4wzUYJDnrpU0AhdphV4MzUS3i_FP3zGDyI9ur0CFXZoHDQBTGQG5A_c0I-OiTeodIR9T953SEGcbrF0wTDSQKfulVx58juLIgLDj1B6f70YlPD-JMhsVAm3deoSM8d048kOS7mL4RLguVPXukgJoNnqhSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=G7uhz9c1UxXIqe1yJGC4zltZBqyafP4ABQ6bIrInMZFiU3iySKFy0Znm6gYZe3iaf-LZUrfGo0Db1OxkcQWgwAzL4UwOYkYfwCLvLJZ7rCtxEgx4wbKQoqdrJa2S3dJWU3D3SeCKN8ySMsz-LDh3e2vLX9aSwgXUJtgqg-wJZQXdN7ZNZSrBcyzmNbgdEMNCO5c6LtgN2WamzakIv9asyr_ydWBsWTLEKiewsybFaCgjFd1ECa4IkDsdoaCMZNNG-siKFN98KGfHvi-LJuH-EUmKztBZcrQZTjgQr9kAnxzHNfOOs4LvWCJELutvI2-1T7jhG_UDzyzdYdEq-g4e0WvgCpKyA_wLba_WMTYB2c5j5E1lmvtVClCmEt-6g1s-AGkPh9E81Lfl2FHFdlwlmbXgK6Ec7wrY2eUowYQ_w5N6Dzgb5Ftha07DPO5LXRUA2R4SBh4GHZpIMvDy04ExoFMobRhA4bO_2t6uDTwB7tbpwEhhO_uZzrPTFX9JN1ld04gpzHQz-cx8o3O3DMccFPNIyzfQ4okk3ycZwsGUvZcrP6GStC6_QDNBaLMCZCWnko6SZCsPX5Hs6InB4ZJeF_lFPFVNID_KNQIj6xJ5w1DT2TopdFcOJ2RgIv3ViVkXhYynTcld9HJMfEI_jc8vACSBWw1xhGdyOQofxIL9FY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=G7uhz9c1UxXIqe1yJGC4zltZBqyafP4ABQ6bIrInMZFiU3iySKFy0Znm6gYZe3iaf-LZUrfGo0Db1OxkcQWgwAzL4UwOYkYfwCLvLJZ7rCtxEgx4wbKQoqdrJa2S3dJWU3D3SeCKN8ySMsz-LDh3e2vLX9aSwgXUJtgqg-wJZQXdN7ZNZSrBcyzmNbgdEMNCO5c6LtgN2WamzakIv9asyr_ydWBsWTLEKiewsybFaCgjFd1ECa4IkDsdoaCMZNNG-siKFN98KGfHvi-LJuH-EUmKztBZcrQZTjgQr9kAnxzHNfOOs4LvWCJELutvI2-1T7jhG_UDzyzdYdEq-g4e0WvgCpKyA_wLba_WMTYB2c5j5E1lmvtVClCmEt-6g1s-AGkPh9E81Lfl2FHFdlwlmbXgK6Ec7wrY2eUowYQ_w5N6Dzgb5Ftha07DPO5LXRUA2R4SBh4GHZpIMvDy04ExoFMobRhA4bO_2t6uDTwB7tbpwEhhO_uZzrPTFX9JN1ld04gpzHQz-cx8o3O3DMccFPNIyzfQ4okk3ycZwsGUvZcrP6GStC6_QDNBaLMCZCWnko6SZCsPX5Hs6InB4ZJeF_lFPFVNID_KNQIj6xJ5w1DT2TopdFcOJ2RgIv3ViVkXhYynTcld9HJMfEI_jc8vACSBWw1xhGdyOQofxIL9FY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aB7McvvLP0qCjYY5FjzjG8ENJp26c3f8xa2xBanB44yvhSTs2rBAsryT4A4yA2j2y0m0Xul1EieYgIdBVM9Hkx3sXMZPfvZkOGa4odEQ0XB6yf0hfRORoFZo7XGSjdHvRItW8R8UXsllXlHaN306fInRq8_wjNqRzaX6BDSQXaK9fZu39-kcWGgcmQXdHPK2ZWuDV6ljpZQM_EgcW-Hx4Jr_emHSjWOYN2ryekiGN3WaqkIOHNh_Mpr6NAXyHoD8qS1oohHu-_AwkiTDOAZ-Dq8LOifNyOJPahqedSzJAHHZXpDAqEeK5teHi-6CJZnhCPzES2XSdBNyj564RjXixg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=TI0HGONPnGeBfFupc9qEgA2Y2a25ILbkhWf0BN7xTIELXUbu3J7x7b5rOAZ83zHPrMIBCkDXQxNDIPSLO_-LlL_OWgvV6BZls62fNPBigbrRuDJ-7Dls598cM2uKl3BC63vLA7X4pV12pyWXK9RGE8tKIAfQFu-yhLDBcxYCC4oClymu1DxFd30KwC9TRSgdvLP3scnCg4B0MESaVzSU_RCq04lpwEhm7eF7VlNxvD-S9gpbRFS5ftdPCp_1zxvoUWrnWgtKziYp6cBEY48AxyD4OIiOX1-tJdHsBzd4gzKkhYHDYO9AEolXelymiP1pYiPEXz_L6968j23gFDFnmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=TI0HGONPnGeBfFupc9qEgA2Y2a25ILbkhWf0BN7xTIELXUbu3J7x7b5rOAZ83zHPrMIBCkDXQxNDIPSLO_-LlL_OWgvV6BZls62fNPBigbrRuDJ-7Dls598cM2uKl3BC63vLA7X4pV12pyWXK9RGE8tKIAfQFu-yhLDBcxYCC4oClymu1DxFd30KwC9TRSgdvLP3scnCg4B0MESaVzSU_RCq04lpwEhm7eF7VlNxvD-S9gpbRFS5ftdPCp_1zxvoUWrnWgtKziYp6cBEY48AxyD4OIiOX1-tJdHsBzd4gzKkhYHDYO9AEolXelymiP1pYiPEXz_L6968j23gFDFnmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0JhzdTKRxJ6dp5-n9cfBVgmFoadGzpkS9TrDwmFMivfxQQBpPysy5PuHGRN-Xuns0Qtr51iLH0dHunymbl0kwlzX6iHOJBKdpwlWTc-xqDDGrypAobc7_OmuYnvEAkX4q6xPROwzaEJwXV2Ue4bjTSejhdQINCBgHLAV-pZZJu9qB4LMwhz_Hx0RFxeO28VnvUT_-NygoeaY7De66Knfwe1toqgeVq5Q_UUyxfhOuj_PF-dXERMODWAvrGj3j6YzAX3z-RI2BjdY4IOZJiyOu5yQM2XYzxRVJJ9Zlg4JxNT7gpD2qm1PZdToN4At7rWZPfI-qs7aSf6-Ee8_Wbf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS2xRuCpMLGr6cv8C25TTlsDwxDiteeTsXP63V8C334Mp-2LZb5DceLMekeoeIxEnez5hbtd1UqNpCIR-fdvHAVtPM7wmq_XkwabkxLUvhO0Knsr8gonskMxmksxHoq-dsmFqr0kJiDjPVuKHB09Uvpnz5OFqhZMV1joSPxtl7nGre0hGJz2fB6w3MmC8YsTgCLYhwNt3IEfg5qmkO6LScgtyRGUVjfHTOfQ2TykqtUwjfRc78YnVelKbsUpFWN12z6buYTGRoyiQqOkEBxprt-RcVFieFeQDFRuUxvglKeCUj9zzxHZ9fvQqzFMVhRIfH-9axhJf4ArQGlUqAa-FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b3UaE7rLDNuYtB7ddbSyZzJJK8gMhz09-kpb1j4luHVog8LzsUtRnozZAdmEXF4Wnnw3u3jWqRJlW025als3ebHzFXiRGHogOHS0r_75kLS4e5B6UP4XNRvjdd3xxGmCWzvhayYIcc23SGCnvDsK2JGuzIZ0hpuJODJzdd1AOz6TScGWOAhhfITglNU_h0uSt6Mcd8IM3oed1zL6COV_eEt69t3PJ6sep2aCiBqdI9TzCjpmezmJhbA4vTkyHOkzkzGS-8kHUcQd9YssvBNpQD0hE2Hl3LgPey5Cb70lW8ul0M3l6OjvFbO15p1o4pVp1IyfoGgY7_2F9aoIpbi65A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=qOik4CgtDKziU7u70PjiwH4wSQMdi9-vHtRTjDwmgc_Nm6LUdJa3_KwJDPREty3y8VWiCbrrWsJmM4PilsqKIqUhxZ7JN5kP33KpGb8QY4VCzLQx-Ij98oP3ErSzVfOCwzcT6MfxLdj4bs5XfqODsJJ1Q6eJhFhoQ5tidAnWAqhnviMzMjAX_x_2SkyYlJ87j_ZQiopckSEjzKqC4qIbi2d8Dp84hJKj7x-iAN2pqtF1phObaBjOOBBToAEPhn-lW8qlNLw7_wDbKZ6z69rxcArirqGemkDDeUHeBuAZzpoDZgXBNE69NAjdjCysoVoue4k94aqkfGkrj0bMdlggZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=qOik4CgtDKziU7u70PjiwH4wSQMdi9-vHtRTjDwmgc_Nm6LUdJa3_KwJDPREty3y8VWiCbrrWsJmM4PilsqKIqUhxZ7JN5kP33KpGb8QY4VCzLQx-Ij98oP3ErSzVfOCwzcT6MfxLdj4bs5XfqODsJJ1Q6eJhFhoQ5tidAnWAqhnviMzMjAX_x_2SkyYlJ87j_ZQiopckSEjzKqC4qIbi2d8Dp84hJKj7x-iAN2pqtF1phObaBjOOBBToAEPhn-lW8qlNLw7_wDbKZ6z69rxcArirqGemkDDeUHeBuAZzpoDZgXBNE69NAjdjCysoVoue4k94aqkfGkrj0bMdlggZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afFU1TlVYE9Xq0aR-pXk0clF6PPIbVUCCIEDosVJaHccmhxcoNXIksGX27uKCffKr5tCYb24HRUTOSnw2JQm4MC_sQ8BTRO_zhTqNEXC4toglDoVdJPMyR0FbMEDAMMMFiKnZt1OwTUKN8kI3CZdOQNanjVt_sqdEWap90MNicwlH0lGDFAv8hXEbBu9xhSXB-w8D5WwyD4c7HQ08WYkBgU_V7WoWIWaWJElaKJaEwO_K8H5GP5ubAchyqywDGbJhksnqKn3ZDVQE1tI5j-kKsvvFfUBqHafHWLZlaG63dxa5x1Ygb5uRWHdtQos7cO9DOcv2XVENOkpnndT-ui2cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFGuqycrfQzbA0CukFU6yHR99QjBvZa1-3JzCXG0i0aF8fF_XUA7E-BPwBLNL2H2BOdzxgRL82uPYmrmtgBwcf3QJ1-BEFrW9cSJDj2a2V6DluPT2zi6oOzntx_43sqj80XGn12coZ8CoZcD3VxDaGVK31-vtfCuP0oNu9xV0IxUTgbBNvisyna0sxmEfax02-hv9-Fn7dDG4fs4MAgWwxfu6N_JVqrQt9_6WvFVytGFDrNwUiX-VxiSLW450lR4j7A71YEk05x_mKHorKbyKx2Ur2mvZwmT7Zyix7-Uj0LW-BqklsVULPYSUwqicFg-6gdizrpSo3fq6EGUki4toNj8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFGuqycrfQzbA0CukFU6yHR99QjBvZa1-3JzCXG0i0aF8fF_XUA7E-BPwBLNL2H2BOdzxgRL82uPYmrmtgBwcf3QJ1-BEFrW9cSJDj2a2V6DluPT2zi6oOzntx_43sqj80XGn12coZ8CoZcD3VxDaGVK31-vtfCuP0oNu9xV0IxUTgbBNvisyna0sxmEfax02-hv9-Fn7dDG4fs4MAgWwxfu6N_JVqrQt9_6WvFVytGFDrNwUiX-VxiSLW450lR4j7A71YEk05x_mKHorKbyKx2Ur2mvZwmT7Zyix7-Uj0LW-BqklsVULPYSUwqicFg-6gdizrpSo3fq6EGUki4toNj8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=huBwssVXESn0suCbcmizL33v0jy4jofHGVokMgfBa9q8rfWLCHIqHsB1n4mYLUVqi8_jZiF2OTfrdpfgiFBbwSjaN4PyXkxkd_ZVqI8mIp3xeipHaxgwp3HtmW-9yE4gAJR9dylxUhA9xxAOHVZKDBHQTwwwLLfK0ESoxKKZHeRGMNY0r0un_vo5lURNhUJfW4avs5RWSGUSMJ-zKv8TkfVz5AxuPYf_AQhvO_GREH4ktPBt8CmWTYEaPr8SH0GxcdyGvyd4CTvXgOjS7X6yu4R2ppJmPWkUclscfDqVngN29Sg1tljc9L4RMMrKCe-YQnxFqp5PLlBsR5bLRB0nVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=huBwssVXESn0suCbcmizL33v0jy4jofHGVokMgfBa9q8rfWLCHIqHsB1n4mYLUVqi8_jZiF2OTfrdpfgiFBbwSjaN4PyXkxkd_ZVqI8mIp3xeipHaxgwp3HtmW-9yE4gAJR9dylxUhA9xxAOHVZKDBHQTwwwLLfK0ESoxKKZHeRGMNY0r0un_vo5lURNhUJfW4avs5RWSGUSMJ-zKv8TkfVz5AxuPYf_AQhvO_GREH4ktPBt8CmWTYEaPr8SH0GxcdyGvyd4CTvXgOjS7X6yu4R2ppJmPWkUclscfDqVngN29Sg1tljc9L4RMMrKCe-YQnxFqp5PLlBsR5bLRB0nVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=cJqU6DiTf-m_FZSGasg9mKPU_DrmSYtnr0v3CK9-QbVW6aCgPBFUGIiv06cXhN8pnHx2axpOzQQk5sok9sq55oSLeapZiB46-OgKhAaNLtJhe38yHNjBRbS6lew8mppStp_XcjZ9c_Jdj8YP4azuj1NFAqpyayLGHCBABtOg6u0gWJv22sbIeha4Nr7BgHdHHnKbs284zrrYtV0lv5ek-tAukjMqOXUogpzW1PsjW22Sa2k7rlaOzK7Q3Dy9J3VE6oMkB_kKO_aGt_H8ab_-9h3gW1ogSBYiF5qKTFooqZdsTSl5eBuHW6b6HD2dGw73-80OCMt2MY5pGDM9lHH2vzncDfl2rraiixcY0MyHuaqhkPIHafCcAm1FLawnrsg0wyF2vubzOJ-vfaZi93HT-GcUTkqnJqqqhB24jmT-5xEavVRWUgoBpSaj35rlwLdo4dnAaSJDY9rY1SqsiXQNd_RBRpVx5nK7GUpZ31IJL_vlwHk7ebIpCz2Mt4ZKksuH9uTgBcIfEYZpwarattOQ4focHaHeNoDwLl4E8bmaMgT25-OmV1-3goWUo5-_07Qgzw6J1qAVErzO6eDqqxd7Vlcpu6DeJDIfljsEYgn6_ByLcN09jJNV7pOE6GBaXQabU3C_mmFuG-cfC73ZrdlndNm7pDyJ3OwYHZ8Rz6PKiaI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=cJqU6DiTf-m_FZSGasg9mKPU_DrmSYtnr0v3CK9-QbVW6aCgPBFUGIiv06cXhN8pnHx2axpOzQQk5sok9sq55oSLeapZiB46-OgKhAaNLtJhe38yHNjBRbS6lew8mppStp_XcjZ9c_Jdj8YP4azuj1NFAqpyayLGHCBABtOg6u0gWJv22sbIeha4Nr7BgHdHHnKbs284zrrYtV0lv5ek-tAukjMqOXUogpzW1PsjW22Sa2k7rlaOzK7Q3Dy9J3VE6oMkB_kKO_aGt_H8ab_-9h3gW1ogSBYiF5qKTFooqZdsTSl5eBuHW6b6HD2dGw73-80OCMt2MY5pGDM9lHH2vzncDfl2rraiixcY0MyHuaqhkPIHafCcAm1FLawnrsg0wyF2vubzOJ-vfaZi93HT-GcUTkqnJqqqhB24jmT-5xEavVRWUgoBpSaj35rlwLdo4dnAaSJDY9rY1SqsiXQNd_RBRpVx5nK7GUpZ31IJL_vlwHk7ebIpCz2Mt4ZKksuH9uTgBcIfEYZpwarattOQ4focHaHeNoDwLl4E8bmaMgT25-OmV1-3goWUo5-_07Qgzw6J1qAVErzO6eDqqxd7Vlcpu6DeJDIfljsEYgn6_ByLcN09jJNV7pOE6GBaXQabU3C_mmFuG-cfC73ZrdlndNm7pDyJ3OwYHZ8Rz6PKiaI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=PN8J_S_kKW94KO4p4RBLb3EB3eQJlxIZp6qJ_gyC2W7yxUFN5wHVXvQEAM1cY0HShZEa7H6hz1eMmtlDz__9z35Day-2HwteM3YbUzJFHS3mfhavyFGEeH5xJt4SKgojAF_X3H9mvdXj2ezLY1c2ZzaVQmZbRIeLg64uOWPitLdnUGdsmtdGi2ABUVzjgFtFME4N1wm7C4G7BIipm_K0YypXSuzvqPaTPIN6QDLZRMMF-aIvYkC8RmO0KQRI1YV-3r2TfgFDSplxTx5FsFLeaEjH4WAS2HCKFfn489LG7_NHo2bjY9uALp36WUcO_ceverpiptZSWsZhnjtLvXQU_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=PN8J_S_kKW94KO4p4RBLb3EB3eQJlxIZp6qJ_gyC2W7yxUFN5wHVXvQEAM1cY0HShZEa7H6hz1eMmtlDz__9z35Day-2HwteM3YbUzJFHS3mfhavyFGEeH5xJt4SKgojAF_X3H9mvdXj2ezLY1c2ZzaVQmZbRIeLg64uOWPitLdnUGdsmtdGi2ABUVzjgFtFME4N1wm7C4G7BIipm_K0YypXSuzvqPaTPIN6QDLZRMMF-aIvYkC8RmO0KQRI1YV-3r2TfgFDSplxTx5FsFLeaEjH4WAS2HCKFfn489LG7_NHo2bjY9uALp36WUcO_ceverpiptZSWsZhnjtLvXQU_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8jq7YZShDvyOU5IvdbUPZ8JWi7JUiAyLN2TRKIKgr6I_3Uj4fsqfvBMXp1W7yNcv3mLn7UHZmfAMtobHKJqeNtYH_kQWP9ZXUULTnT7CrokrJ_HGvHOPNMp_ibvuPhCb8OBVQSVn6CS5rsunKh1fX3-yrOQr3RuNRyEh5ysmli73kdjY_PqaZNaXM0yTigBe6hHOh6-5X1KnfwAB1cO_KveaFN6k9ISDLDZbeYqJ8JtUTo7SkGZTA2CiCL3e0wWNvSUBEZc4oJ3vld-puin2Ri1gFanh0sISAXOrm9poTIOH2zR5YV4DS6lcpNNC3zTIoqU23PHUrd_1IKQm9ikhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=sqeNHhjSPPt5SufBsHuuVrUJjFfRRXEOdVt3vn7hVslf_YQ-cvQtuh2W1DIquDdGDs4crP_oJQREmH50ar9dnnUVhpeG8CWNe8ege4kxIMW6uBssp6-He6m_KRIx3bCt-7VdGfW_AGFqwmvfAYopDqGY87DbAlMn4aW3qFvYswAA4Fl1igFaF1ez6dMe57sWHRyjOSFUWjIML8JEAFErLfmf5oTG0uMYnXzf4AddN0sbAh8gtmOQCSTy8ns7DZ2YbXYjLTpBqEdflwzifq0hbbFZ2u5F0GdSesyxG0Ev0uCE3SZeeLEep_hMkg6ZzC_2tqMOcR3ZlxvCoXxwNvXmZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=sqeNHhjSPPt5SufBsHuuVrUJjFfRRXEOdVt3vn7hVslf_YQ-cvQtuh2W1DIquDdGDs4crP_oJQREmH50ar9dnnUVhpeG8CWNe8ege4kxIMW6uBssp6-He6m_KRIx3bCt-7VdGfW_AGFqwmvfAYopDqGY87DbAlMn4aW3qFvYswAA4Fl1igFaF1ez6dMe57sWHRyjOSFUWjIML8JEAFErLfmf5oTG0uMYnXzf4AddN0sbAh8gtmOQCSTy8ns7DZ2YbXYjLTpBqEdflwzifq0hbbFZ2u5F0GdSesyxG0Ev0uCE3SZeeLEep_hMkg6ZzC_2tqMOcR3ZlxvCoXxwNvXmZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=knwkwy2OxJx-ededZdzstQK474ibzPLgSmES6OhvFzh8wF1UPPD2Y-Yd8j6U3yznOe6wL2SQwJmCgyg4oP4cd3KIXKVepLU46RPymJ87EILPxrWJ6pIDtP7vJ8uzlNSwbKiFhzEp16FH2yBBwhhrvVoqXVeVm1lN7eyTrIOXAwEA3ZqfUrqxWh9dTS67nEHUGOmIgKBhSS1eEH34FejKHxxhQLmM9f5hm2yfABhvtvI_GHjccH78YpCqQWWZg9ywK-ySDxIMbLX6YGVMtTfoQ704wWyvIrQB8PbOvv6OW9yIQIEI8vCF0lpDTB3j-IHn_Az_YYl_snYHnnNH-iV_Gy1kiXPqI8hTGcrWVngrQUiWD_hzHJ5PWpLmb6rL1x0m-GFFlVFU8naKVApoYOXC0CIm8xzzSPOqPAZjbesFQqGsCvDDyA5QoLWXLqgPBQrlYZUIC9m_n6CerBE7QFoeglnKxEfU7kyPAW9eV0DSs4MRn3HV-FVTyhR2ApV-Vyh_NYgU63TdTMlYJCG6vA1hEixBvRy_orH5J1tqsfKQ4nlnzSOT5H9UMKK9PMCw152DQ2VAZi9oHegHXLsJZxWa4nB7__GaM9l4x0LdllWewbJpO5Q4eBSNEmyuIzloxffiKveRBMOyUvW1M-QIuizjmZ3QB4UYW0JHKjZtOuvissM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=knwkwy2OxJx-ededZdzstQK474ibzPLgSmES6OhvFzh8wF1UPPD2Y-Yd8j6U3yznOe6wL2SQwJmCgyg4oP4cd3KIXKVepLU46RPymJ87EILPxrWJ6pIDtP7vJ8uzlNSwbKiFhzEp16FH2yBBwhhrvVoqXVeVm1lN7eyTrIOXAwEA3ZqfUrqxWh9dTS67nEHUGOmIgKBhSS1eEH34FejKHxxhQLmM9f5hm2yfABhvtvI_GHjccH78YpCqQWWZg9ywK-ySDxIMbLX6YGVMtTfoQ704wWyvIrQB8PbOvv6OW9yIQIEI8vCF0lpDTB3j-IHn_Az_YYl_snYHnnNH-iV_Gy1kiXPqI8hTGcrWVngrQUiWD_hzHJ5PWpLmb6rL1x0m-GFFlVFU8naKVApoYOXC0CIm8xzzSPOqPAZjbesFQqGsCvDDyA5QoLWXLqgPBQrlYZUIC9m_n6CerBE7QFoeglnKxEfU7kyPAW9eV0DSs4MRn3HV-FVTyhR2ApV-Vyh_NYgU63TdTMlYJCG6vA1hEixBvRy_orH5J1tqsfKQ4nlnzSOT5H9UMKK9PMCw152DQ2VAZi9oHegHXLsJZxWa4nB7__GaM9l4x0LdllWewbJpO5Q4eBSNEmyuIzloxffiKveRBMOyUvW1M-QIuizjmZ3QB4UYW0JHKjZtOuvissM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcIoiqXmTV7q8fDCkN_PvAvJL-f-3rr_wQLWLJzpUPNMvglnqpOs5YXH9Sh5xVyhysp-p2qJ5CeIM_DvbK1ZOE7bVeuxykOmEDSXal2bbtHMXtOEkNVqtul7AtCNDzt7O5qlWpPDB2OHBzumQRIohNUjSFSIsDuPuuDEBehpUL4BeepM77a3YFFCld9F6lcfDdpnYkakRDbD3o6rOb64pyudPYXlsR1dKzomjt39DGVvYsGyvB8p_qfEMNb3TsI0qGVuXJtVusbVtEESxEsyXov4sjfzM2B8xKD_nmdeLrl39HtGKa3GlWgUxt6N_49B6Nqfxiqdv6-jFawl7kYFUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=E_smA74Vta9uwWPT_WwIonh63HczXnj9I3afnMbSwtShLTWSko-VtV-D6ff5R7NBarDsu_bWJb9a6jhFHYxG24ejKYgpl9VdabnlgUzzyohb5XadZTkNKoVDxoctl41s038Oc09uY1HyTqnqGblMaRHNyPVZ1QxVKdElBGNFZWFkqaWDH6uIJCgTfEHk1VT0HFEJoLP8uusaNKNskPLz2ipJpHc1SIgZugaURFc-AVY-9ijexOTbTl-fE20xZdRb4MKUAUP3yURmuOsZkbe7zz_Qp0hJXigY-6n9Y5-KXdSYrGtHEgeUDu5LeRrm8-k8v1r8Pi5HYrCKbRm0i-JGHnmoQKyocIxA0DwfXAp6sQcS-v3X4AJUKw9vdkAXCF_1BfrzjhEUFYkD7uN3mbZKAfOn6JGs9tWFRJCu7Sczhm2wwXpFc5ekkLaBSnMdnU8UIgJUQyInsIpCOnwPuWUbBYNlLdFxSlaoSbS5VTWtJSktTh_cg0ufGWi7e3JcUmVoqzIw1EFemTwEC1YH0GoGNkfAVIqMoU4jtTmErbxRWgpZDrO-EloeBwnsaK5P-QeZl1ABZsBnwnvH1Z17hSZngiecPEnHY_FcAhzUV-4OZJZe4PceueBI2sreaGx6ivWEqJ79zKmwtJ0yWoZaYt0fpFmhuQn-nlptC38ub3xMebI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=E_smA74Vta9uwWPT_WwIonh63HczXnj9I3afnMbSwtShLTWSko-VtV-D6ff5R7NBarDsu_bWJb9a6jhFHYxG24ejKYgpl9VdabnlgUzzyohb5XadZTkNKoVDxoctl41s038Oc09uY1HyTqnqGblMaRHNyPVZ1QxVKdElBGNFZWFkqaWDH6uIJCgTfEHk1VT0HFEJoLP8uusaNKNskPLz2ipJpHc1SIgZugaURFc-AVY-9ijexOTbTl-fE20xZdRb4MKUAUP3yURmuOsZkbe7zz_Qp0hJXigY-6n9Y5-KXdSYrGtHEgeUDu5LeRrm8-k8v1r8Pi5HYrCKbRm0i-JGHnmoQKyocIxA0DwfXAp6sQcS-v3X4AJUKw9vdkAXCF_1BfrzjhEUFYkD7uN3mbZKAfOn6JGs9tWFRJCu7Sczhm2wwXpFc5ekkLaBSnMdnU8UIgJUQyInsIpCOnwPuWUbBYNlLdFxSlaoSbS5VTWtJSktTh_cg0ufGWi7e3JcUmVoqzIw1EFemTwEC1YH0GoGNkfAVIqMoU4jtTmErbxRWgpZDrO-EloeBwnsaK5P-QeZl1ABZsBnwnvH1Z17hSZngiecPEnHY_FcAhzUV-4OZJZe4PceueBI2sreaGx6ivWEqJ79zKmwtJ0yWoZaYt0fpFmhuQn-nlptC38ub3xMebI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=J0AIbbtbV4rExEMK3-6d8mKXtpz6lM9kyGwTK6uauGCd_-lKFEfmrvWRNaTLBl4QmGX-iqCnAK-N_dLNjqBNF4ps22QZntMTYYG5Th0G7_VoE9orXLXkZwqddDvozur9cSdNFF1akjv4-Eee4eIAiiguHZjyV9pj5ZAzH7CXKdM4eTjZOMk89o0asqM0BN-uADSGJ23uienjJnjVYnGpkfg-9YHRQxFxAcYxqbh6TexnQ_mgfllc7zSgUpJTOMRCw-Y6UYCStRiQ-WzMoSTIxCdeTmgmiYcuSqrtfnoAT8LIkqKfBQRJL6D0JaOuD7nHmwXMLJC6DPYerMzBV_nDhGw4oF8WRCielqQdsLd5almH-H5Qr98YTfR8zJduftBvPLNnI__ARD9J0piVtSTclakvA-qWIsAyyC8MPDEDe0zhfmKUzIeZJj0l1INjU7FslvpTDChbM_92RnnZLnKekO11ZxOF6pbJAvh0w5dNTuzDpIuPRN-nUub-QDP8GkEQkGEwLbl3n040DblS5x5eIdmXynk7iqDaVyFRS9QIAIww7qXYHcMptxdy3JSwAcu9Rkn-ATak-FtSN-CGFizMr_ucXsUPIBWtv27a2qlzfy0yOErJalaZDw8bDHqHngHX_xNSPNFhz2AeAOvmgnV15II2SkzOJmg7oXKIdHqk7sc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=J0AIbbtbV4rExEMK3-6d8mKXtpz6lM9kyGwTK6uauGCd_-lKFEfmrvWRNaTLBl4QmGX-iqCnAK-N_dLNjqBNF4ps22QZntMTYYG5Th0G7_VoE9orXLXkZwqddDvozur9cSdNFF1akjv4-Eee4eIAiiguHZjyV9pj5ZAzH7CXKdM4eTjZOMk89o0asqM0BN-uADSGJ23uienjJnjVYnGpkfg-9YHRQxFxAcYxqbh6TexnQ_mgfllc7zSgUpJTOMRCw-Y6UYCStRiQ-WzMoSTIxCdeTmgmiYcuSqrtfnoAT8LIkqKfBQRJL6D0JaOuD7nHmwXMLJC6DPYerMzBV_nDhGw4oF8WRCielqQdsLd5almH-H5Qr98YTfR8zJduftBvPLNnI__ARD9J0piVtSTclakvA-qWIsAyyC8MPDEDe0zhfmKUzIeZJj0l1INjU7FslvpTDChbM_92RnnZLnKekO11ZxOF6pbJAvh0w5dNTuzDpIuPRN-nUub-QDP8GkEQkGEwLbl3n040DblS5x5eIdmXynk7iqDaVyFRS9QIAIww7qXYHcMptxdy3JSwAcu9Rkn-ATak-FtSN-CGFizMr_ucXsUPIBWtv27a2qlzfy0yOErJalaZDw8bDHqHngHX_xNSPNFhz2AeAOvmgnV15II2SkzOJmg7oXKIdHqk7sc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=gRvPnyqO0RfzMScpfTw2K1rBhRLrulInQ01o6xHkHPzbINowUn4xVVJpLUpyJxG3tUZC2KMmnw5Id04Guwm6JnmjX36Bi1SlsSXQ_vah9tqd3K6jJ72MZoXnWE_nnpzgtEl5gdS6E0BpBb6l97Z_bnZPaJ3_YV-zFrzZejcuHlAdZGekPNVE08cBZ3op6KO1iXLrSUaeS89r9NWE4FqTr6kWeXV6U-lGzYE5zbPQ05_hthP1gg0VYM85hJ0Ps9_sWORhz6paGy9iMmCQ8j6et0QwkgiePPWZhc8c4u5FV7AaO_KK6wpuxI86A9HoclEfMtlOrImrwsd8MvqGZosSMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=gRvPnyqO0RfzMScpfTw2K1rBhRLrulInQ01o6xHkHPzbINowUn4xVVJpLUpyJxG3tUZC2KMmnw5Id04Guwm6JnmjX36Bi1SlsSXQ_vah9tqd3K6jJ72MZoXnWE_nnpzgtEl5gdS6E0BpBb6l97Z_bnZPaJ3_YV-zFrzZejcuHlAdZGekPNVE08cBZ3op6KO1iXLrSUaeS89r9NWE4FqTr6kWeXV6U-lGzYE5zbPQ05_hthP1gg0VYM85hJ0Ps9_sWORhz6paGy9iMmCQ8j6et0QwkgiePPWZhc8c4u5FV7AaO_KK6wpuxI86A9HoclEfMtlOrImrwsd8MvqGZosSMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=QbZwRC8K_yt5YJ6DxqWD-uBh_HdDEWhlQt-CiS3pbbWYNGI_4-sj6JYtAsNFZ_pY3GNsHGVzJ0XW5pXEkYtKG4wMf-a_t5tL3pGwH0R4wm7HRrcHUWAN1uJrwwg3s84FMfNgitH1ahG6f_h8dPNaVbf5zbjJjt4yhkTFL41Ol78aRx7H-Ubw4SQyhYtTx8x_RcnzNiQV-p4LsoU2iUC5FU6JltIPKaFDg8Ehw9VtXDMAw2IcbGvaHtI5t78QD4eyiCwGKL6xISyLWGHKoa4uqMAxqVEVCmVbDwCCw-pnu4kV6moWhur4SCO_s74D9oi2dI4wdweGcqgv-hYyeZYkgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=QbZwRC8K_yt5YJ6DxqWD-uBh_HdDEWhlQt-CiS3pbbWYNGI_4-sj6JYtAsNFZ_pY3GNsHGVzJ0XW5pXEkYtKG4wMf-a_t5tL3pGwH0R4wm7HRrcHUWAN1uJrwwg3s84FMfNgitH1ahG6f_h8dPNaVbf5zbjJjt4yhkTFL41Ol78aRx7H-Ubw4SQyhYtTx8x_RcnzNiQV-p4LsoU2iUC5FU6JltIPKaFDg8Ehw9VtXDMAw2IcbGvaHtI5t78QD4eyiCwGKL6xISyLWGHKoa4uqMAxqVEVCmVbDwCCw-pnu4kV6moWhur4SCO_s74D9oi2dI4wdweGcqgv-hYyeZYkgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=tv3RIHaA8LOP-pSLtHEuniEQP1-muhxGsTvx2Q-krwkAurPls8uN6IdCDGYUIbjBaD_ngE2RNaXidtCG8VjRHbgK9NwYz3QptQ34YygG8Zuq3rHgc-oNgYUAep9UleRkpi_4ureEgLTpsk0j6lZrJhlvs1k2oSgn-oP9a8VyxU15k3NWWUfkxjwi_CStDmvc3v-6r1nWPMkp4uKJYN0souaAg1xmdXmawTZabbd6f86BrTqimmWNGmcf6hPOkPf5gUmpUSkll1H_8qBjvf78mExk3LvJ8182czeA-1Huu0FswFjM4EGOvEYodlhJUQL3s3lEnuDY4x1_qzJeIHBpvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=tv3RIHaA8LOP-pSLtHEuniEQP1-muhxGsTvx2Q-krwkAurPls8uN6IdCDGYUIbjBaD_ngE2RNaXidtCG8VjRHbgK9NwYz3QptQ34YygG8Zuq3rHgc-oNgYUAep9UleRkpi_4ureEgLTpsk0j6lZrJhlvs1k2oSgn-oP9a8VyxU15k3NWWUfkxjwi_CStDmvc3v-6r1nWPMkp4uKJYN0souaAg1xmdXmawTZabbd6f86BrTqimmWNGmcf6hPOkPf5gUmpUSkll1H_8qBjvf78mExk3LvJ8182czeA-1Huu0FswFjM4EGOvEYodlhJUQL3s3lEnuDY4x1_qzJeIHBpvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ap9nspBcjrZRAfaTOdLSgeIF3n_PhbXg_4kSYSqFzNaAAvbfrEKp8CuhDGpNsIicMpaSKPX374lmZ99ZWh1_obqMZmd9Onew_IujIzlK_iDqu4kr_hMq12qW5oGXci__c2pi9DvjHJyVcSmbWN4b2WwHR_HcsA-_l8xqdw0kkiMd1i6JfbcsybwRgd3gzM50fK1bZwOip-V1BougqpBoVnYaPSC-8KaZ-xm4g8rwNKmon76NsDmFp5FAC5hQEVyK3gnGePxVZ-uBzV4m2a0AY6cUtk5LGPp9TF9ji-5nvvOwV0FQhbjw2njNjTt08DJbW1FjK8_epn6DYQ2uNxdutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ap9nspBcjrZRAfaTOdLSgeIF3n_PhbXg_4kSYSqFzNaAAvbfrEKp8CuhDGpNsIicMpaSKPX374lmZ99ZWh1_obqMZmd9Onew_IujIzlK_iDqu4kr_hMq12qW5oGXci__c2pi9DvjHJyVcSmbWN4b2WwHR_HcsA-_l8xqdw0kkiMd1i6JfbcsybwRgd3gzM50fK1bZwOip-V1BougqpBoVnYaPSC-8KaZ-xm4g8rwNKmon76NsDmFp5FAC5hQEVyK3gnGePxVZ-uBzV4m2a0AY6cUtk5LGPp9TF9ji-5nvvOwV0FQhbjw2njNjTt08DJbW1FjK8_epn6DYQ2uNxdutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=SZ2xfIqyAWlsccTF0EXkyXf397BUyPIePQNxAL0OZgqEUsoX5_-_t5LsqXWIG9NXjS7fk-xwz8wbLQRMCOpeGqI3pshHNJ1oxc5XVMM0cSF7ySyNaxzVud_BFmX-sMhq237kOuyu106FzcMDDr8vQJrsbS07X9_CB4CtvOQZ6-A_Rw3O-4Hw6aPB1kfB1rm-kYS10fbJ5eNi4wssPJVMqMUOUehd1YTlccgMk8QuAsXM2PaOyADhFZv5dONNpD5NCYxe7B1OqkSI0FhuWttW3W5MV9Lr3lo426FW2e-aocjMVKcgDzG9pakhjAB6zKFHFbtKxICYapWgaZQ5FDDCsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=SZ2xfIqyAWlsccTF0EXkyXf397BUyPIePQNxAL0OZgqEUsoX5_-_t5LsqXWIG9NXjS7fk-xwz8wbLQRMCOpeGqI3pshHNJ1oxc5XVMM0cSF7ySyNaxzVud_BFmX-sMhq237kOuyu106FzcMDDr8vQJrsbS07X9_CB4CtvOQZ6-A_Rw3O-4Hw6aPB1kfB1rm-kYS10fbJ5eNi4wssPJVMqMUOUehd1YTlccgMk8QuAsXM2PaOyADhFZv5dONNpD5NCYxe7B1OqkSI0FhuWttW3W5MV9Lr3lo426FW2e-aocjMVKcgDzG9pakhjAB6zKFHFbtKxICYapWgaZQ5FDDCsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=iWYPtBC5yGOBVInuNV-Z-J0718dsaixuD1GSdyVSGQBYFqY1TxUkNnDpTVXZPZxnZXRqSpCTG0bNs2YNYBCZ9RFWDzxMrtjewPbU3AeI9BPVwX7kIBtHTwDyxucGaF5H03y4whgLumZZRoS5L6289CvkUgaHCUbGgFGoa0J5VD5ylwfit4vP6SbmKOQIeY5bfMFgO0W14DjRR4xmOnx51d11bfIUkEI8R8C97R8EYWzuJrrAHsUn3-pc40aHBVbUJc8gIANkOCBlFPY-LkkpeFez-nyNraV55k26mVBwClXKAc2M6dMOvJF4XGrMty0gf1e_2_5-1PgF8Xx19vOiCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=iWYPtBC5yGOBVInuNV-Z-J0718dsaixuD1GSdyVSGQBYFqY1TxUkNnDpTVXZPZxnZXRqSpCTG0bNs2YNYBCZ9RFWDzxMrtjewPbU3AeI9BPVwX7kIBtHTwDyxucGaF5H03y4whgLumZZRoS5L6289CvkUgaHCUbGgFGoa0J5VD5ylwfit4vP6SbmKOQIeY5bfMFgO0W14DjRR4xmOnx51d11bfIUkEI8R8C97R8EYWzuJrrAHsUn3-pc40aHBVbUJc8gIANkOCBlFPY-LkkpeFez-nyNraV55k26mVBwClXKAc2M6dMOvJF4XGrMty0gf1e_2_5-1PgF8Xx19vOiCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=EAT-xeQsJXwjnV4KePmVtu7vpuBESg-zd6ijvyLhUEEWenC93A_lf9cM6mjw3K4ONiQNzC2fkLN_aTCyeIFYU4qLZctc9MjaF6-BLQMwsAXT9r-YemyjaAeIlIcFHamS5DU0pZzVXd-bCVfXgNLpiUXG8NSqzUWENnClxOBdvQqUACBQ4B731y3-zI7l8Z9xEzlUfMeJBrlNoYiX2d4j4_PeY0CR0Wz2PkBheautVZN6eCzSY3-SMaHxnAwhn5JHAqdbLwBktom31dgSEHV3rqMM3eycqtybSGSHN9gsMMqFxh4u_ozIHLpAfEs3Vw4PhMLXnD-9Fd_4m75Kl6iMNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=EAT-xeQsJXwjnV4KePmVtu7vpuBESg-zd6ijvyLhUEEWenC93A_lf9cM6mjw3K4ONiQNzC2fkLN_aTCyeIFYU4qLZctc9MjaF6-BLQMwsAXT9r-YemyjaAeIlIcFHamS5DU0pZzVXd-bCVfXgNLpiUXG8NSqzUWENnClxOBdvQqUACBQ4B731y3-zI7l8Z9xEzlUfMeJBrlNoYiX2d4j4_PeY0CR0Wz2PkBheautVZN6eCzSY3-SMaHxnAwhn5JHAqdbLwBktom31dgSEHV3rqMM3eycqtybSGSHN9gsMMqFxh4u_ozIHLpAfEs3Vw4PhMLXnD-9Fd_4m75Kl6iMNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCU9f-rWxAz13bnOaGftVutxWJhad43JkBiC2kAtV5pEjvlmiByoiWT0p_oH4SKONxuWS38Sn1E01R6-J2Rtlb8NgHvWNyF3XWOWMnFB3brPxb4RGMfArfAYImCpS76M0c_PZgH_jUj2z6g0emxu4QfXZAfbJRl1uQJMt8jZkC8PIk8npjLceRAeZKeKHXj3XMoAb_o_3-JBW0NbUJJDUoDjEI6iZGGhJ-VY1lQuW7D5qejmRx-9pWI49NiZ5CT1yHfc-SU9JNhP8YuPagdHDaK-0n0nsZDdnP72qCpWO8D1oDvzn5sO4ZLpsnpZFlbwl0v7z1TTcAuwfyM4lLCEhQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fv-LUIZT6hT77KdpP2k6G_gUIenwwdWIGSCm2OLvp3E-xu_C6EFa0h9Oo_RxI9j2KpUp1LtgqnTABm5L9e7LKry92ZpahwuS2cnivMEZnAAYH2m3AHpf8oZz8yOQBabUJqYmRJ-kxE4etIC44mtJslaQcaBsSzDyn-50kFNon_QlpraszVXIx5Qyq8GXvL9JuYvp9wqanudLg3M1ULeA8pzmybBFvuCmNR2nLVWHDfjISLiygbguCWPbJtMU-6P8B8_uonqt-H0hm0RuiufT2WsTjOzoTxW-nidH84l1hQ-bVnOAdIvR1pq-n0Ya10WrdIsHe6CfrIqlCHln6WkMKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=fv-LUIZT6hT77KdpP2k6G_gUIenwwdWIGSCm2OLvp3E-xu_C6EFa0h9Oo_RxI9j2KpUp1LtgqnTABm5L9e7LKry92ZpahwuS2cnivMEZnAAYH2m3AHpf8oZz8yOQBabUJqYmRJ-kxE4etIC44mtJslaQcaBsSzDyn-50kFNon_QlpraszVXIx5Qyq8GXvL9JuYvp9wqanudLg3M1ULeA8pzmybBFvuCmNR2nLVWHDfjISLiygbguCWPbJtMU-6P8B8_uonqt-H0hm0RuiufT2WsTjOzoTxW-nidH84l1hQ-bVnOAdIvR1pq-n0Ya10WrdIsHe6CfrIqlCHln6WkMKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=aKx9kv3WYINtOunBx7CSb4wzQwv7HK6pcL9jQdhuDF0A25gw0TztFd64kQpvuGEmtVVeOFYY_w06BjCMYOpcxDfv0pAPruzxxDuaDLXqGmxLj1BNjXhYTj1sqyxNwbOXcIV9gYRYgjTTelyuscYhGgy84kUzhiSw7rdE0YuRYvAWeoXmH7yPZ8RT5neiYdENd4ohYWcvUmRbJn78OCYa13_-KA48Fz_LxsCCo9DaoT9zRSUgNyUSflEFDiwpxEtvym4VBJMe-JQFD69m_-NEOv9jimOXiUQFUlOo5vh541A7eymjKdJVAvFKabjXDpm2hq2APBzHWaGi2YiHy1tiQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=aKx9kv3WYINtOunBx7CSb4wzQwv7HK6pcL9jQdhuDF0A25gw0TztFd64kQpvuGEmtVVeOFYY_w06BjCMYOpcxDfv0pAPruzxxDuaDLXqGmxLj1BNjXhYTj1sqyxNwbOXcIV9gYRYgjTTelyuscYhGgy84kUzhiSw7rdE0YuRYvAWeoXmH7yPZ8RT5neiYdENd4ohYWcvUmRbJn78OCYa13_-KA48Fz_LxsCCo9DaoT9zRSUgNyUSflEFDiwpxEtvym4VBJMe-JQFD69m_-NEOv9jimOXiUQFUlOo5vh541A7eymjKdJVAvFKabjXDpm2hq2APBzHWaGi2YiHy1tiQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dwzJND65Ack0aTRgNHO6FvDHAM0VQ2mu0H8Iof_c3SDjnOnN0s6V6MQkK1aB2G41ln0iQEJODc2bLAKhgZiILU6UZq5GZg9PRyIHFrBhLFH-GBni4w4zj4hVorIEmZjFcGQQJvo8ISN8JaEJhZ6lemUrs99d0DIka21nD6HlRkbYmZajtXrD9s2AVrfiksq-fhemD-YzSRCHT1hm5jI8EgGM74haH09BgUzIooaa-s5fn2cFamSGq6Hlg2L2Dn_aSbsc2CbTAp5_Rsv9TEUUwtvee_60-Cy8A3uIVjyff7EpjJa2bqKVMuPlPvDt4d3WuPJ4wnDdBE5aAaqOJ84geQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=dwzJND65Ack0aTRgNHO6FvDHAM0VQ2mu0H8Iof_c3SDjnOnN0s6V6MQkK1aB2G41ln0iQEJODc2bLAKhgZiILU6UZq5GZg9PRyIHFrBhLFH-GBni4w4zj4hVorIEmZjFcGQQJvo8ISN8JaEJhZ6lemUrs99d0DIka21nD6HlRkbYmZajtXrD9s2AVrfiksq-fhemD-YzSRCHT1hm5jI8EgGM74haH09BgUzIooaa-s5fn2cFamSGq6Hlg2L2Dn_aSbsc2CbTAp5_Rsv9TEUUwtvee_60-Cy8A3uIVjyff7EpjJa2bqKVMuPlPvDt4d3WuPJ4wnDdBE5aAaqOJ84geQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vNyxminV0pbXQ83-sPWWN52XSO3Pyayw8NBYi2rZ4J_RzAm0o6OI_kdD4t3Mp2IrsfCqILbPHpBUOjHtRiWKev3iKA7z6tNa05H-6urbXcjrFRpJLik7NruSiJPPmoQhJzpX8aIB2MenZrQyJU8ShHlLXy30EUHWKEEWsesPjP_9GNyYLTpYM3aa6ydfg6ecVGo72yUSNYs5Ehy-AW4IbOZ1QxlMn1oiUfDcYojAq-KWma41x86OC6XkwsjVwEKV-PspHnHP-cEq_vn8q3JjLdsZ_0l4HftRdbAOzLxlnNQ8R_UMq1EfhnCc2YIAL2HfQog7TfYO7pcPT6o4kkmaFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=vNyxminV0pbXQ83-sPWWN52XSO3Pyayw8NBYi2rZ4J_RzAm0o6OI_kdD4t3Mp2IrsfCqILbPHpBUOjHtRiWKev3iKA7z6tNa05H-6urbXcjrFRpJLik7NruSiJPPmoQhJzpX8aIB2MenZrQyJU8ShHlLXy30EUHWKEEWsesPjP_9GNyYLTpYM3aa6ydfg6ecVGo72yUSNYs5Ehy-AW4IbOZ1QxlMn1oiUfDcYojAq-KWma41x86OC6XkwsjVwEKV-PspHnHP-cEq_vn8q3JjLdsZ_0l4HftRdbAOzLxlnNQ8R_UMq1EfhnCc2YIAL2HfQog7TfYO7pcPT6o4kkmaFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYp9l9gME446uEcox6iLKg1HBS3AFmtgWsVlVrdYkSsLQFgw7pdTDIGI9V4AvLmA5koZRtIJA-DhIc5Fr2NGxnJMttW6bbOOBVnEY6hs9Zv8E4MVPt9Zy5H_1Zf0bBRA_b7QYIWaOD3bUc9P0DiU9-0Q4HEfeyP5keyj6NR6D0c0uuQlyjQgLkVgoSWFKB1CVcqxisaEZEe2VEn30QkDhErhWlVbTLsnhFTYDLYNB6ZL_qxGYgJMhblkgMrDtdSrBzc2E0HPDe6ysiUohXrDGZz_oKssl0LfIn1C1PGW4JkAsBtagj6JVOsq5yXmJ4RSpYAAdTy9OfPuS4Ovb5RXtg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TOPJ7nB6ZTWFda_odG0lCVXctsPd7XmVE44sJ0FYAfJ8kYKLI2Lp5JKFvQ0OXlyD4P88ZqIJUwPOFJjNooyXXeMPk6EDmsQskjkotdl6He2PHG6Wg9g0bMGGDHBpI4sIL9GIecKcGBH0RnUgCGBOZ1UB7Hu4clMosKCGyGQA6DIhe5MUBf4Kacxyzbb65_YidarZadmuyDGZZXVZbnvlwUoZPIr6jv_kUAdgMvrdDAt2XXSQ6AIx4XSEE-ytO2rw1UIv9MU0OWogzT-b-Awp74o8mb2O8HjzvQT6RJGLzjsC7wfCacWKnBP19L1nVVnE0rCJ83Hx4QaGRjA-5UvbazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TOPJ7nB6ZTWFda_odG0lCVXctsPd7XmVE44sJ0FYAfJ8kYKLI2Lp5JKFvQ0OXlyD4P88ZqIJUwPOFJjNooyXXeMPk6EDmsQskjkotdl6He2PHG6Wg9g0bMGGDHBpI4sIL9GIecKcGBH0RnUgCGBOZ1UB7Hu4clMosKCGyGQA6DIhe5MUBf4Kacxyzbb65_YidarZadmuyDGZZXVZbnvlwUoZPIr6jv_kUAdgMvrdDAt2XXSQ6AIx4XSEE-ytO2rw1UIv9MU0OWogzT-b-Awp74o8mb2O8HjzvQT6RJGLzjsC7wfCacWKnBP19L1nVVnE0rCJ83Hx4QaGRjA-5UvbazzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=DiGsX6eRugiAxYARYKcwUrxypDxfrJJkf_a8v9FbPqnX4e_YpRbZOoNexq9n5nAXH2bXRBiJh1FNsgmsQ7X1q88dTM15WlaV-Me3SJS2hyyZzwQC0cwpAItUacaaXNRVkdc_VVaWq8JDe21quCoGOrznqG0WhPiwt5d6zZgwToRMdiqfr5-P6OkBVKMZTTGZTMVCfdb_yEaNu0dST-UxTKr9J4YXWdwHihLcuCv8D3Dgl9_bHFKOFwTwR8yjPqjGRWfdWkCK5e2eBEELsHc-d6gt8ZNtoQP56ExQeAmwKA5pGqSIbleXb1PJAtKrYMvaf6rbRIR42KGbFm0qsFAqIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=DiGsX6eRugiAxYARYKcwUrxypDxfrJJkf_a8v9FbPqnX4e_YpRbZOoNexq9n5nAXH2bXRBiJh1FNsgmsQ7X1q88dTM15WlaV-Me3SJS2hyyZzwQC0cwpAItUacaaXNRVkdc_VVaWq8JDe21quCoGOrznqG0WhPiwt5d6zZgwToRMdiqfr5-P6OkBVKMZTTGZTMVCfdb_yEaNu0dST-UxTKr9J4YXWdwHihLcuCv8D3Dgl9_bHFKOFwTwR8yjPqjGRWfdWkCK5e2eBEELsHc-d6gt8ZNtoQP56ExQeAmwKA5pGqSIbleXb1PJAtKrYMvaf6rbRIR42KGbFm0qsFAqIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TMucRm_guNwfye-DL1Q_3NDDB8FpI2LKv2i2QQIGWIBosZ2AcgvIL9AEsVKlGdEcc2rkd7N5AgQC8wom_dmWDjBEfdPdd5MK0TaO9nUIgutftwv57NJnexh42znamg5xvAQ_DXFKZ1bF2K0eMmP9q1A28XwYAOQoR-rYM9kuXzr1ula_1qPT068Kd6Rc8cNtg3DQmAuTPlpTZ3x_wfQ20L0TDU6_JC1gepHUjYlflFw6-sfTsm8t3SBYR5UnM9F9KIFVrkfLGq1QKtHSuWC0QOPmYON6i3wdDRHwIaA5iDsc3ZasaOzvXG2WjD0ORC2ByU6bDF6hBogHIzOdqovk4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFh5G3dmIIJZKxn1NBYxorTg6RPQZK6h8zxzP1NZYVX_rCXvNGsfehEBxE77d3qcQLVTN7OQkcrJk_a79ndXSO_7I6VdYzwkkx2euB7TQADAFVWpx6GtUBFkLqrM9GCvtlzVdtE-bQlN3ZJcurBVFUi8EZY0-_k9VFksKdHUHxjNVHO_Re8-Bh92AE3EcY1VA5db_yKc5H9sJtq7PciTQoxqiW3wKNmmgDkDiloZuLVzO_Sgw_X1L_htofaaWJ2nXXRb70NoJwRlI-9iNsjVTnnnB-0kkpqivSRPRYGOxzjsHUxiEW9-_27hMHRv5pM-LnjSDF-q-YYHStze0ooM-g.jpg" alt="photo" loading="lazy"/></div>
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
