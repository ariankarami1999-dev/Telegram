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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 11:11:52</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyaxen8k8EL6XqQG9f0XvZYSurP9g-0TQBaYv1Lz474tTCveyKNP4hsEvlOJth1t33u0k4GDpogbu-i1vJoVJtogTxz83Odo-36hS0BWv3U84CpUv9AUrfhJniR_AGe64VDiPHSSXnEQH9IAWorb84tjreS7fqrnyIM6UvEjkx-y7ZLKO0vzVJFbPs3qZTCytUxz78TsXMbJKGxiYanXS9ydSJMegWnE1mxbOIKWFEnF-5O0KGYLNmp263hNW-69OcVOkqE84ouToZ8-4V5tH8EbgmgDizppvEl5otVj2LEByWADPABttubcw9DRDdyG7TnQYPp8AcCp1kCTLgrfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sZtmwIXUWjm8mqPUuGMMMrHiu1XQgOylI5bRCef1XW4mg6in_FkGZQW2pcg8EFFm_geso9yE-F4t1sKcbUL3nIF9lp07WcsIMbrRR65P1OrjDelof0hMOFPEEXSKWz68lpFLjj1uwcBml153XVgge7TER3T-z6tHmhv18tRsl3QvkzrFDoTwf_HJ21ZG4EJNdndrYNC6ImMQpD46nQrbbxPgeV1YJ5yucYw8_ikND24H71jR_52_jkOaqPJR6TneNQ71uxfNV9rfVRQmdDTau_B44yp6Q0tunCrOkMyQu02ouwwlP36pGFV7ZIsuLg9PPIRSyJNSyq1VB3y8BKY5_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cVhLmecOyOYfd8pYO8LXyJ8wHzRv6Fe2kG-xgojOd6cbE_6XjaSnl-mwXXBiKDVbSIN77cBcap_rss8jd2bLF3VzGwUirhIzp8BmRnp9iZi5JSMrDx0a2yzTiT53oMY2GyRkzz7fMAgG5bxtN2gRUttYhACdRzYk0Ynjkb8PL-GwSg9xLvLT9jBPI5TNxsZhNLgcV99isaqwYzICi3BOur__m4WH_9YtXNveo8P89eUjkqxZckFi1S0lFa_pF-nyU6QN44mAhKWqSd67JPF5IYAmyo7kpyh-HHlG5AnFteNo-OOk-sEaU8ICqiq3W9UnXl4Zqe3EKMKpDBCZXRgEDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=KMPp148PEWRH3o0-DDAgZ_a38s5kEs3FSr03ofbfGj5PPkpPihiEzzgb0Zi2hlkr5n2rPQ4GnVLO25gbHuBJvIf9tTvJzrS8FKO4_z1YxZ29JxlJvVbpNhcy9wQ2NslrFKvWRa4evIYkFyxxug4QD4q0yoQOy2F7XsABXq0NNZCIYPHsVZjCeJJL_2uyZiv8usw1wwVQuu2z_fqa3A72c9B0rPDIWBXTHBgZs5cEDj2OHLcon3VEmg2orNJjpm5qxdSvP0Gx-i1T92_-H7EyUVC8e5Yt2Or1SQhcllhKweKuWSRAnPTcpUZ2hUgbSkOPTVzW3yaDFf-_X1mwhd_Qg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca5f42c66.mp4?token=KMPp148PEWRH3o0-DDAgZ_a38s5kEs3FSr03ofbfGj5PPkpPihiEzzgb0Zi2hlkr5n2rPQ4GnVLO25gbHuBJvIf9tTvJzrS8FKO4_z1YxZ29JxlJvVbpNhcy9wQ2NslrFKvWRa4evIYkFyxxug4QD4q0yoQOy2F7XsABXq0NNZCIYPHsVZjCeJJL_2uyZiv8usw1wwVQuu2z_fqa3A72c9B0rPDIWBXTHBgZs5cEDj2OHLcon3VEmg2orNJjpm5qxdSvP0Gx-i1T92_-H7EyUVC8e5Yt2Or1SQhcllhKweKuWSRAnPTcpUZ2hUgbSkOPTVzW3yaDFf-_X1mwhd_Qg4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چهره اصلی اعتراضات دانش‌آموزی فرانسه
با چفیه فلسطینی که در یک ویدئو
رهبر جناح چپ افراطی فرانسه را می‌بوسد.
ائتلاف ارتجاع سرخ (چپ) و سیاه (اسلامگرایی)
همان دو گروهی که عامل انقلاب ۵۷
در ایران بودند و سیاست خارجه و داخله
و جنگ و بحران و تنفر و انزوا
و عقب افتادگی  رو برای ایران آوردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RD6eBFiRQ94BoEAXNqoK0YVJM0vaWDrRuuntHikuKMxpVm4-eOkOhdC20Fs52R1t59cyQDMZCnQytihtj6j3B5Pu0b9qkxU9uDFBtI2MyX0Je8cfqHraDiAcgeG8Y-MYZ-RZ3rlDk_CI3xi5jbel6oxL2OBBr3kKRC81kYjrPL2i7X_0ntalvJpctCukbLz_IdMKWvOOQVcP0s2hAJW54Mx-fcFL4x6qN_HAmwH48J2shF-5yDYnk6ah1OfueqO1IglCUFr0k_fdvyxSJ9s6jQlNZwxV_gkap9EjP2fqh7avAldaKwITOPdwuUR5V70oxaGnv17l475cwAzRzHj2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=pa9OfQzI2km2O54vG_SeMbDMKxDKks_P1HkFPTHIvL0E2jPoeu8JS_Rnd9sLV63ro2lC6-PgGUwYfXu8nh7TVykld0lrmombBQufqnHrEVMB1QcQ1vXo44HIpsFUhQHPVytudPDHIasJCPIY3c2rWLM4fDTJJBe7RrsgdynHAKZgTX-8LavpvFEP_RiZbtqLeROwMMThsoQRsXGUROCgjUleT0-4IH7dISGz7IPr_g465w-5UIwRgxOirGRGRm9OKQ86TvNmNIsduoa5tWJiMmeu82wV9se7g6Asza-S8bvlkTHeMW3Zq-hSQUj1d-e1lUOiX3foaDS3lFov87kALGgFZusP-TdUjprj3rxIZfgZXLt1AY4tL7BpKzbAtyR9B1zrbGHHTN_vUazDDpjta9G6VnMJjCaSsBrazgGN_33Uuc674Sndty_V3G8MAKCFEUcll0giPHckSTWRrbTeTKR4mFxD2c1n8GphjCfrmceJDr9TFvdIW4lCrahXYjxevgGhxKg6fpCTnvn99lET8Q_fWgW7Fhk1iNXG8EFEqF9eBTBuC-zd39KPeSz_iOZnwe6_Ra1RMYbqCUZOmVN_Gx70hUmEL1-1mgAaL5k5YfGqUie-TwWN60UXWZ-WLnwV9FH80dWPxQSzWZo8t__RKNBU0ZP0evNltprdbAN2UIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=pa9OfQzI2km2O54vG_SeMbDMKxDKks_P1HkFPTHIvL0E2jPoeu8JS_Rnd9sLV63ro2lC6-PgGUwYfXu8nh7TVykld0lrmombBQufqnHrEVMB1QcQ1vXo44HIpsFUhQHPVytudPDHIasJCPIY3c2rWLM4fDTJJBe7RrsgdynHAKZgTX-8LavpvFEP_RiZbtqLeROwMMThsoQRsXGUROCgjUleT0-4IH7dISGz7IPr_g465w-5UIwRgxOirGRGRm9OKQ86TvNmNIsduoa5tWJiMmeu82wV9se7g6Asza-S8bvlkTHeMW3Zq-hSQUj1d-e1lUOiX3foaDS3lFov87kALGgFZusP-TdUjprj3rxIZfgZXLt1AY4tL7BpKzbAtyR9B1zrbGHHTN_vUazDDpjta9G6VnMJjCaSsBrazgGN_33Uuc674Sndty_V3G8MAKCFEUcll0giPHckSTWRrbTeTKR4mFxD2c1n8GphjCfrmceJDr9TFvdIW4lCrahXYjxevgGhxKg6fpCTnvn99lET8Q_fWgW7Fhk1iNXG8EFEqF9eBTBuC-zd39KPeSz_iOZnwe6_Ra1RMYbqCUZOmVN_Gx70hUmEL1-1mgAaL5k5YfGqUie-TwWN60UXWZ-WLnwV9FH80dWPxQSzWZo8t__RKNBU0ZP0evNltprdbAN2UIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyDDm3alipq_ITj7Br5iPhhHc1w5OHimhif2xx6rrY4P3ZAOcj45YGjpVfq2Ek94D9pDhufcrOIGy_xSKdBjxU2IZNgv91q5pK5QSeb7M4JQ0jC1ou7acQydndEdTJKB5d4PtfwQQJkE_4AZHGC8y6nIPtQt5Ijh-MQ-IibukN4HrnC0iXlQRM_BCJcfKzQqRxOPTRTgxC30kd_lPTBeheU_J7rV-IK3itvilQUsTlwq7BEuURjQkKmfMB7zLI1biUQK18DgEYp0IuKvFq_01pxWrK3pFY3YREsApbq_yDzaZQnBz-ighpu-L989gk11CyjZlajLxDhUJE3nJsq7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oSq04e45HWqKbiJ8mviGeJPtccbUSDc423T-GKPQbfXlg03HKxX_Tjj4ttDJvJ0A_qf54EK2HVBDnskbPJM78FYDEXNy8bWqWlBwkMiZ2mQwV6xrrOWa4scrg1GUouS2tqywj9AoKL2NYZ9QeNhqgXRsb2JjQV0Wo3Llu1fy4tnQ-pUDDd50qYguUEAKECGR5PIIjM1-YSZZ3V04PUObzsf_zRr9L256nb1GaPG6b-xedyN2d_htCS1JCYvxMDsnBeNilIHrVoncFXHB4PiaUD1McAFtbGy_NEfGkcsXmj-WULdegEL04UqpWVyDuuD2YiOePshutWG5MbryW-ZekQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNiZdMD6z6XueHPk2-AQOD5tiQXhS0iEpKwyVU8LMY98o7SJ8VychWkQYmYbut8rDCjGlRr05XwPXabKL28YCQ-YJVro09mZAEkEIDa-jcySnM3f0VWMn5FEM1s-bcKjqyK3P8lSpcOyYHHPve3mZqTeuCV2_O-PpY7pgEpgnP9J7JkiogY8AI0_szGodcpYPrwsHWLS_AlGf-JBeKacLxvB0WWZGndIbXM8AKOSekogi-3T2bwT34eb_s5XZzd5bxGK7d-m8nsIqpqTjiUjcEatxU2zhJZVIiI21IIQFUOrt9fA0C_aU1G9NaR-OBQxKtgF5lGEy4swDMRG23wuvw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CVaxc1H4SmbpaDzugRk_c2KbhL3RhXQ6E99a_6jDpz_y8OzrqarhaIoorKOhHfRvmGXDV6b5JJsXQpopVDH-op7CqGmvIhrHQ1H8RGPwRuwLaekgBV-oPloODZQNzrp7XdoVoabTeeotIkM5nFWwOw7cpsLu4_FwfQ7C8TsTTxGWpJCYNWhQ1gb8OE_ON8Ahp8Rg2W15ErE8_m6pmb_lVU0ZggITtOxoGLlClWIBETwO3Mvbb7HGcoyzfTeZPsv4oM7MhIQ_D616J12srLdoHfk-_xkyke589wKZVfVvgzTCp_qnUlNkdd8NKg8Gv6S9fD7-I-m6KwEsqhyly6VSdg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY-gs2rFz5usUE4uSTOQvFHoaNODBmrhDYpOOlDuGw6mjzF8eS1KgbDRaO2T9nNVaf2mx9BStKZyxn-RXA0on6LNkp4RT9d8J-4jEa2rzEoOHKluxbTcf12OuXZsGHPM_AhNgz90D6k2330m8XB9dZIX5FQqht8gjUHmOwppCjSBUi2a8uu1R3wrG3DPHdYv6hEtt8kRQm_EwE4jq1HiD4Si-BzzLcueANIAtIIVXlCYNBUtM1msUzHK9oW1Unf-6Mf0R0SfLXJOkcD4uAxiDM9u3vRn5Itr6QQw7hGHxt5eA7drer4EQkYtzVhh31iWauIUqL51-DxshVDNA6yuIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnRSXpSr-RNnsxQDxhdRjWagjCWDcVteC0zwK-asfVgBgGgB-R4JHhDqVtlB2TDBtVntn9Qrlff4JtugyNA2f1p99xOj7BE3QR9hR3JmJor7wEZ-iMqZD7zZRHh7D5HwlQitp2M0mi7o-MEtxQUG2qD7PC46U6ELUo7UTKvdlP9LbpgDdokjvX2gm8oT_2ApGXRSzExiFus39QViC7f0xnoYrVSwOyc7dQ2in9d2X4t8StQo6EGd0Oj8WdEzNuChM8TetGNuvwFZnbM9Aff0dIXKBD1teKlia4UkZRo0XSuU6VldRWIopjB2osE7UjCAb5iVvXdo4nYUXIP8sGbeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=O5iHyCcPN2fHT4cvc14bC6GgRdF5LL5ryGpL3x4h9EkkFSlx05vkTua9EDUxjjapQnuIudhUAZNll5rfXkhnfJ1izC2FLh1jNIxRXEf9IhJQnBudwcHTqFFg_yM_gpyQt4VEiTzIjm87nSH9TyGlWLCAoK7yk9aptbURojqefa21Vz6hfsb40SARn1yN0gceu55iCN0514WUXvxz2x0mASYR0OFzX57C4JoAQFS6HTy0d59JdDL99h72alOJAnUm-PELgr30XA9aVfL-C_mVUnooKnbaodhTgPPo3NlOemoqPJ1QALVyrsRYLUSooqNymFnPkYZ6EhsoJovFjJq-7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=O5iHyCcPN2fHT4cvc14bC6GgRdF5LL5ryGpL3x4h9EkkFSlx05vkTua9EDUxjjapQnuIudhUAZNll5rfXkhnfJ1izC2FLh1jNIxRXEf9IhJQnBudwcHTqFFg_yM_gpyQt4VEiTzIjm87nSH9TyGlWLCAoK7yk9aptbURojqefa21Vz6hfsb40SARn1yN0gceu55iCN0514WUXvxz2x0mASYR0OFzX57C4JoAQFS6HTy0d59JdDL99h72alOJAnUm-PELgr30XA9aVfL-C_mVUnooKnbaodhTgPPo3NlOemoqPJ1QALVyrsRYLUSooqNymFnPkYZ6EhsoJovFjJq-7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Z1Dhf6PJjHnExooiWnqLi_NHpMEWXAb1Jb4zxn-9UGIackRSs_Et2Ae_ADK2VLoL3oUOYzY6j2S_IWvMzKOJteCNvys8UnV_Z0zbDJLSPKpemkMRxpJUT_gA46wtspat95RdYu_mY58Px7AhDckmA17SCTSHWLyqRthyEQuhoFlRDYslpJA-jI3WZlKP1QCw7OGoimbw0y7mUXuIzG5gCwcDPY9UVcjzW_sBizU-V070vlcmsWTvDQYwXTglFPGNxvkkX1EE5r_QVRSPjMeAaW_MpBwg3aOed_fgPiE3qbxcfBRKD5HkTZ86Ogu39wimVsU3gtJ1v3Ba9vumMxO7PHlukRgRE9ESsBUAaIHsZSTwGEBUiiMcsmnAHhkDiS825MN8atDYT-S4WulQlihqUizWOpB1ey1Xh5AetChbIH3_NA1VuE7_nCo0Qk8Ofi7h9sgHyBZA6ovOsKSuJgEtGHG8QLbIVV076-ETmSEyNz4ggLVO-4e64EtkeLlXTlUFit_NtqPiR5aqAIVLZRQQRvoK5m45v_3niaNebXxM0pUQ0diwQzKg8JpP7YJIkq4O-lCC4AXLtyhKYG2HFEKqCBPVpI2EnUiNenLT5w1Pf5EVfKnSolEJzwmax8blrmq9jwVhLW0PxyIPi04zs-t5tFDmIpRdt35lnSdTOuxPvqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=Z1Dhf6PJjHnExooiWnqLi_NHpMEWXAb1Jb4zxn-9UGIackRSs_Et2Ae_ADK2VLoL3oUOYzY6j2S_IWvMzKOJteCNvys8UnV_Z0zbDJLSPKpemkMRxpJUT_gA46wtspat95RdYu_mY58Px7AhDckmA17SCTSHWLyqRthyEQuhoFlRDYslpJA-jI3WZlKP1QCw7OGoimbw0y7mUXuIzG5gCwcDPY9UVcjzW_sBizU-V070vlcmsWTvDQYwXTglFPGNxvkkX1EE5r_QVRSPjMeAaW_MpBwg3aOed_fgPiE3qbxcfBRKD5HkTZ86Ogu39wimVsU3gtJ1v3Ba9vumMxO7PHlukRgRE9ESsBUAaIHsZSTwGEBUiiMcsmnAHhkDiS825MN8atDYT-S4WulQlihqUizWOpB1ey1Xh5AetChbIH3_NA1VuE7_nCo0Qk8Ofi7h9sgHyBZA6ovOsKSuJgEtGHG8QLbIVV076-ETmSEyNz4ggLVO-4e64EtkeLlXTlUFit_NtqPiR5aqAIVLZRQQRvoK5m45v_3niaNebXxM0pUQ0diwQzKg8JpP7YJIkq4O-lCC4AXLtyhKYG2HFEKqCBPVpI2EnUiNenLT5w1Pf5EVfKnSolEJzwmax8blrmq9jwVhLW0PxyIPi04zs-t5tFDmIpRdt35lnSdTOuxPvqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDGGxCPOSYTDq6mWhX4ypUanYmxxg05CdIFSpIs8tilp95GWRQ6AU8ZqswoUKOTAFS8epcl2tar0mSHTo4R71LWjKitsA9PDh13tsuS5W6TPfdjzgTMfbsR4EQ7UIdwp-h7-pLGdOiIJqYWipTJK7ToMaG8F3cIOOeERnuAWZ0ctZ-_N9_EhHrdRUm2tGfyJ7IYx5e9ZK6aRpCBf36bpSP7j6bgC_wINA7sv50PRxHeKzD7SDaJgQNjLv0ABv6MzeQAQqGjMOx2zRRtmDcmoBP1dNWPgZ6Lv0jOsVOKvkOn6cHi5Zfmn6H4eK12tTOYG-h5up63KSEmV7He5WjUVxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i_I87zqluPbdUM_AVQai7gklcfs1nl_Qrd64pJ0xeQSrpmNE-hanrbM9iXvk1Hxld3qRRe25H_ublB5BaUC4PQXsLj6ECe1naPiIoAyNgIEDVzhzOKNKxC7b9iSYMPzkH0avQvL6D64tr_L6-ObTTV_qYRp-MXwQSC-LUBsXes6NxlqkDRGAgLtp5RrtmDebnZWVuZ46gCf9pNp9Z-KWoNwtQ4MuB_c-ei6G8_zXY4s33Pf27KxT7jOh41-FL2bnGbAOq87G8zmutnhNfZAHQxnTfKG1UEZ0_RhP4cTnqbtLsEVinZfZg9rVTiyZvK5srmp2u9Wpzsbt3s_LcVXWXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgUvrLffcjOkswdI6NQGeCdhnJteV8AJUEWrDY1GvpEx5Gp2azd9y9HN4aRY_OmWpSRBjjV81gkLIoN_rfuFTedwVTbafnraGOtpdNtB2fFE6thUBNE8ehILlgMBeYkwT0qgYDvlj2OBsbtNACXz2dBDWdKyjigDCYs1gNtteTEVi_XWIVAyVcQi0jQsMWq6jOivHG8sYJlvn1kDrNcQsH9W0sTgoGq23ZQdUP7OXjIgd6drniFwwxGU_do5sbviPPre0smAF7XFA7uaPzyounvCso0Y76rQ2hfPDbJvlJwNCrd-C3jqGYakesjlmSpnI_AlyhCK9CXk6G3CDhD-_Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=pso1zpvCPfvVGA1oX_sGuQbxNNiFBDIti4YJ1FfjgnCMqTBmLIWsEjAYbcWdINjWYd77SZ3KvMg82mfWFB0EbOngznZEAYOyLVpwE_HSMzwcqAW-_oCgbBp6nGahyTKZS30AwMPn4x1xfQgj5B0uJPgej1DVMa8bpJNDUazvSxf8Qb-1S-ZOkt94Amb2CvBYVEzczNO2Kb9CElWSguHI8ZZWRaiTLQqJ-XX9mu2tPplb-EljnoioxZGdtE8WO9d9hvOyh9CmjNtmK8A1W3X-vgFNT0bvMxttPztr6WQxSTTZ1vFisYd08lt8H1KBfnUkW2X4J9rxxMAls6cLWRlnhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=pso1zpvCPfvVGA1oX_sGuQbxNNiFBDIti4YJ1FfjgnCMqTBmLIWsEjAYbcWdINjWYd77SZ3KvMg82mfWFB0EbOngznZEAYOyLVpwE_HSMzwcqAW-_oCgbBp6nGahyTKZS30AwMPn4x1xfQgj5B0uJPgej1DVMa8bpJNDUazvSxf8Qb-1S-ZOkt94Amb2CvBYVEzczNO2Kb9CElWSguHI8ZZWRaiTLQqJ-XX9mu2tPplb-EljnoioxZGdtE8WO9d9hvOyh9CmjNtmK8A1W3X-vgFNT0bvMxttPztr6WQxSTTZ1vFisYd08lt8H1KBfnUkW2X4J9rxxMAls6cLWRlnhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=udcmw8OCcHmGYd0Ayva2Dd39-L6HxAc7jTXflXzt2Zb9EX5snDPw0Tr3IAvMm9x8ofr2CqyN1KnOncHiLVSYrAIb_tLFm9XZfYC_8PxXNyiS7CHgIGoLn4dFPDnEMzfOojMnssZ7OCJVSsKWr09_pMAQxHOTAx7X-lUkKlt1TC9BTdfm6Dzkl-s2oPhO-j6yXzu09RLowlDaDeadGjbB9bezAXH_LohiYLp_ZjO56FEF4G3QJQh-N6jIjB2ZR0V0X6y35nQUReIlzl9U-PnreRzYhp2riABTLC475Tpxqchiezhbx_7FR-WnmG8vXDpht-OouZW34Bm2n9t4fx0Zlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=udcmw8OCcHmGYd0Ayva2Dd39-L6HxAc7jTXflXzt2Zb9EX5snDPw0Tr3IAvMm9x8ofr2CqyN1KnOncHiLVSYrAIb_tLFm9XZfYC_8PxXNyiS7CHgIGoLn4dFPDnEMzfOojMnssZ7OCJVSsKWr09_pMAQxHOTAx7X-lUkKlt1TC9BTdfm6Dzkl-s2oPhO-j6yXzu09RLowlDaDeadGjbB9bezAXH_LohiYLp_ZjO56FEF4G3QJQh-N6jIjB2ZR0V0X6y35nQUReIlzl9U-PnreRzYhp2riABTLC475Tpxqchiezhbx_7FR-WnmG8vXDpht-OouZW34Bm2n9t4fx0Zlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYs6tv0U2kWgM0r6PvrKCHq84WljISpcDkaCAf9CHIHN-baGaparyJKJeQeqyNy_H4kFRxv6GSqzjTBlsTQQSjYAtyN6XBKl1Y7GA-2p6mQkKb47Cx1IqICx5AOUQZ2sSS777Fd7BJoujRwrpG8qZsn5gQT4KmYGP198fOvIvIUYBOZ-NeBopSFy-faV9rDSuKXuKhuo6Q7rS3fVZsMSTFskCO3wqJcqhSL8K9P-KrV-dgUAVyp9i418B0cNGEcqhXXo0lFnrb7rNvAt_QD4aD8_oQfcGLXxFTVo7FO15n2UHToZh9cnMTpzim2GspeIRbOJN8fyQZ5Vss8eQsSU7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=p6RRMg8-VV0eW7Q2Q9r03_YUSwdCNhPe6fH5k3a4Mgu5jrgPKra2WThTjzCQcv0TW9dd0v95w7ZWdURH-1-DeVwIjLYXBJsRB9-PqL1dUI0VSi3LgzSiFGLbRrUcwgDkrkYMrX0dp_AGP5JUSuIU60FcqLilSXXggLx8pFpb8QeYAK9E-6ecH-ATZ2q91uH6XdxB4bDrX9vd-mrP94qj5I7JmF_pO9PpNpLdkQGiHLbyJ2LGxvoWxeq_OQLwvW_0yGTHDsVKxv6wluizN7C_H6RAAUUmEnyvx6_XwAyLf9muWGbaYa-U65YtcelDbPlZOX5tc_l6DVXivFLy-qzXkicS_JNGVku6wdnuzC3CZryU7CXCtjRGEx-oiU9kLpZAYG7IxC3hSVJsVm-C4wjaXkhlnzDKZEYuiebxIq1oCwu9JvvntPTrVKvGqNJdS8AGue08l3FHYtEguIMND7MPMJWisCW_QWSOsn3RK8OkUPjL9ohb6hjAEvsyt2FSWOBJcdNVuW3LceOuOYCZbXOkV_QkfMv5RqR5RS565nSQw8V6z4iKJ6ECJkJkwQZNvbIlXkb6qaag8BU1C1l6F3F7LYD5s0yGt05IHhAGbLxWHjFQkUv2hnHDCPrwIh5K9qqDcYDF5KCcNMLlz2hgEJE21UBMRE5L6By1gviohmKj-qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=p6RRMg8-VV0eW7Q2Q9r03_YUSwdCNhPe6fH5k3a4Mgu5jrgPKra2WThTjzCQcv0TW9dd0v95w7ZWdURH-1-DeVwIjLYXBJsRB9-PqL1dUI0VSi3LgzSiFGLbRrUcwgDkrkYMrX0dp_AGP5JUSuIU60FcqLilSXXggLx8pFpb8QeYAK9E-6ecH-ATZ2q91uH6XdxB4bDrX9vd-mrP94qj5I7JmF_pO9PpNpLdkQGiHLbyJ2LGxvoWxeq_OQLwvW_0yGTHDsVKxv6wluizN7C_H6RAAUUmEnyvx6_XwAyLf9muWGbaYa-U65YtcelDbPlZOX5tc_l6DVXivFLy-qzXkicS_JNGVku6wdnuzC3CZryU7CXCtjRGEx-oiU9kLpZAYG7IxC3hSVJsVm-C4wjaXkhlnzDKZEYuiebxIq1oCwu9JvvntPTrVKvGqNJdS8AGue08l3FHYtEguIMND7MPMJWisCW_QWSOsn3RK8OkUPjL9ohb6hjAEvsyt2FSWOBJcdNVuW3LceOuOYCZbXOkV_QkfMv5RqR5RS565nSQw8V6z4iKJ6ECJkJkwQZNvbIlXkb6qaag8BU1C1l6F3F7LYD5s0yGt05IHhAGbLxWHjFQkUv2hnHDCPrwIh5K9qqDcYDF5KCcNMLlz2hgEJE21UBMRE5L6By1gviohmKj-qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ov_8bz_9AKFfrWcl0XfkXf9cuZ9h-r4zOjV3qSMdajIN9mh9yT9GgOqgENyZkQI7i3mBslgp-XFp2Naeea_oopwhpWjyGDms-H6R4Ti5ByERvPvFlC7JjOnOGrZupKMMcMaAr8GzmwNA4s90Sv1TSbqdDNwUWOGUF9373Zte-K1cfUAhlt7sSteGp8LT6Xe8ekGwiSIdrg6Ua7HyqOL6SldceXj6GPcEpXEfjTGsl5HPz9ig8323v53LJwtCO9Fl0FxpMJlXeBXOz_deSpI5jMxXtGDGmBUauZN7Wnu53zqUn0km7RaLdlDpXZ4UDMzYV-LSlP7MV_omveisXI_wIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=Ov_8bz_9AKFfrWcl0XfkXf9cuZ9h-r4zOjV3qSMdajIN9mh9yT9GgOqgENyZkQI7i3mBslgp-XFp2Naeea_oopwhpWjyGDms-H6R4Ti5ByERvPvFlC7JjOnOGrZupKMMcMaAr8GzmwNA4s90Sv1TSbqdDNwUWOGUF9373Zte-K1cfUAhlt7sSteGp8LT6Xe8ekGwiSIdrg6Ua7HyqOL6SldceXj6GPcEpXEfjTGsl5HPz9ig8323v53LJwtCO9Fl0FxpMJlXeBXOz_deSpI5jMxXtGDGmBUauZN7Wnu53zqUn0km7RaLdlDpXZ4UDMzYV-LSlP7MV_omveisXI_wIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSIWnjpLSpC_5dj2pGzYLqduseW-mJshE9pCoiYRTafH2wFcfoQLcNN5HcmXei3Tpwfxgm_BUn1fauxN9JRLxpF9jT6ZUlnmiYy2BxI9TeGtYbr65SniA6TX9-C6AuWuMBBOf_PdiNfhAQ4RC0TQvKXKTKYb4ohQCXcC1uHeVacR0VshYrGnZmwngvB41AQEjwydT8smt1GtsgQBrJD62gLj_yDNLYvTXkyf47rzY0bHk2spFAlrIvdZzlcXcBBLzwCnmaso2d1eG8cbPtunAt-zBXhmNNNubPf7fRM9lQqzYLujop9AhqTa6D9fTk3ZrTGqg9D0c-lX01QyCrQubg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=e_M-4T_h_jZ5XB0-icyN1R06W6TOycTByM9qqP1BOEDCw8ZonsBHLFpyliHzfuN_yuDWngZLhgi7ED2nDF1bja-DqzFNV2jyK1TPDMG4v5p8rwZJVxAzl9Vwm1IVf7rQdeiw2JHt2zV7GrLCcu7ORqdBHQrW0u-vqv88CeIpCB7PZ-ByuHvRK2YoGVAlD9gbq9SMeaxNDFG07QYodmdh_NUYsM-RRXs-UnwAqEu3sqXUrUIF4Kke5IT6KEJ1MOQD9aGxFe9KtJvIBzBqUF2V58ViIwgoK64Niq9r7fMwdepBccusOTEIyyNqUIIkvVHf102icYQWXmwNX6A8g_iXNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=e_M-4T_h_jZ5XB0-icyN1R06W6TOycTByM9qqP1BOEDCw8ZonsBHLFpyliHzfuN_yuDWngZLhgi7ED2nDF1bja-DqzFNV2jyK1TPDMG4v5p8rwZJVxAzl9Vwm1IVf7rQdeiw2JHt2zV7GrLCcu7ORqdBHQrW0u-vqv88CeIpCB7PZ-ByuHvRK2YoGVAlD9gbq9SMeaxNDFG07QYodmdh_NUYsM-RRXs-UnwAqEu3sqXUrUIF4Kke5IT6KEJ1MOQD9aGxFe9KtJvIBzBqUF2V58ViIwgoK64Niq9r7fMwdepBccusOTEIyyNqUIIkvVHf102icYQWXmwNX6A8g_iXNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zbw9HxlhiXDeZF_9j0KI_DM4ig_lVVGfRB6rc_iFpxcbB6weFepli7zvwFslNMgNWOSJSpXaYndIdHyCg4aur4tJpXMkAHpETkGyDw40FenbB9UUZOYsXcsmrsG0nr3Q2pWPaSTRs_5rcr_HelPVbyDDGgPyf1TjyH7GouXsO-RM-vJK6Y1aW1ABAGk8iMArdPnMNJLfDlnaIsg4vuG2p6PvIIBqjaFpbzUADqID7ef8aPazJbwXCVD1WIrhHTjikd9vUN1syTLfwpZOTuYjWxEdXy4pZ-t--Pw55_Hx_AdcWGMC40ayqDFWwZVnolXW0XfyTn-0knTr7qs5uZO7fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sswFXCmvBfLZkOmZWPNOTDskrPkIgIrnZI8pOj0kySKxmzoYlTLqn-mR01_kpKRdjZB_x212GHyX5C-6FVx8h6nvputl3B5_2lHY-EAilZzPqi3-vRaItQIIoWG40G-_sWYDDVCSYjQpKTvkqbIoYcagDaq0b7sW4nZyjBYvd8Q5lLRJijycFwrK72OfbtjPPrygPzjByKwX7jsQbDEIqH1aLsYZExeJ7Vr5hQ6geJ0qF1W260eAFHngY1PhsaDGR9RaI05XrmSklWmj2XA8bW2FSfScnPBA4-M-EnNz5SRWCtrWZz_zJ0FUFsOQ_gel9F1HZjJPsNYCCCx5ULRK4g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ESlReqNcsEyM4ZRErCq8vlpi5i22-QmxXKERvNhVyfVGwM_sRPMcWNt5BYNPCUnoZWu1PnXY4qYv7XWoYc-jyViLUvGinJ7Il7DDrWZkC2gTV5VBQG9iL4r8b1PpyXbfgKTt03OAD7diTYtRUGiJyNhwTonSLHY-Bt2AORvKj5e2mPcbBG_6rvf3l7js0_zxftkG_iYvxHhMUQPavT_IkoEk6UySXU5fHYW2dUD3lha-3Z_tTFiOs23BlBvKDeg5RFJrz3BzJh_8zPoO7W0kiVZ0xAe7p2ZLwPd-51LyE2CKtix6Vvr5IX8XlWI1g4S2BsRY1UxwIBVLejkt8Q_2LYmnMLSLWzGA4yq_WuuW28W1ExOKbTBKbR4YgmAwkrGJka5gxyCmw1gCaOs0pqLT2VCylbMJx2YpWt_bv-e0ZDtgE6lPRr0lTKcOj9k_qU7NhKMhfGSRSQsx65s50U08MtDxBjpVpcEH4drBH5yGC9IGzat-zA1Dzwu_MXt90MG18Fm_KOhTU9THmDA_ZXuzJivtWLCMsv8ipz3UksXw1J6hzNXT0N0HFUWGU76HAdrO6A7e4RKT4SlvlMeqEk_qA3VVYzv4OsUbYcRQQEiLhwuBKeaxnF_Fg0UWaqj2UqrflryVAbYvBES4sFusHFrio6JnxLvVokSAV4gri2ePt0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=ESlReqNcsEyM4ZRErCq8vlpi5i22-QmxXKERvNhVyfVGwM_sRPMcWNt5BYNPCUnoZWu1PnXY4qYv7XWoYc-jyViLUvGinJ7Il7DDrWZkC2gTV5VBQG9iL4r8b1PpyXbfgKTt03OAD7diTYtRUGiJyNhwTonSLHY-Bt2AORvKj5e2mPcbBG_6rvf3l7js0_zxftkG_iYvxHhMUQPavT_IkoEk6UySXU5fHYW2dUD3lha-3Z_tTFiOs23BlBvKDeg5RFJrz3BzJh_8zPoO7W0kiVZ0xAe7p2ZLwPd-51LyE2CKtix6Vvr5IX8XlWI1g4S2BsRY1UxwIBVLejkt8Q_2LYmnMLSLWzGA4yq_WuuW28W1ExOKbTBKbR4YgmAwkrGJka5gxyCmw1gCaOs0pqLT2VCylbMJx2YpWt_bv-e0ZDtgE6lPRr0lTKcOj9k_qU7NhKMhfGSRSQsx65s50U08MtDxBjpVpcEH4drBH5yGC9IGzat-zA1Dzwu_MXt90MG18Fm_KOhTU9THmDA_ZXuzJivtWLCMsv8ipz3UksXw1J6hzNXT0N0HFUWGU76HAdrO6A7e4RKT4SlvlMeqEk_qA3VVYzv4OsUbYcRQQEiLhwuBKeaxnF_Fg0UWaqj2UqrflryVAbYvBES4sFusHFrio6JnxLvVokSAV4gri2ePt0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mAb04DXk3Xazt_3--ckiIbg2bOE8V0oHiPMzvHof6C5-4TCpObpGJp5Epj4Q2qzbq6Qvk5IEFqm5JeZt877agHBsamSwNOUuS9ZPKBGKK8haMGgMeF3e22jRlls0IUqaRLYmPy0PviLTghmZ3T0Rj8_i5oXT9MsQcsr2Zb79NiEJMivL608NhuChLsqDIU-IJq4MxFtYR1y6KpvGmk-oqY7g8CZ2OSKC8h3fEDtOlwtpaTrVRcTmcE66nTEXP16Vz-IUNGwP0PSXJeNmAzTyzz99bJAkTZ85JKmUaB06lCdn9rpd7-ktLRBT4ockLDBoAtJG2p7JykkuU88EP1DBYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhM-E7tU_AnGCeOIJSldYiy5smgslDhIaTlMiydgJn2we-hRE1pYtVgL-7BR8SiCAResmO31l6JMZylKHHfUC_giVfQhD-7tM5fi1GFU2Uh5WzanEPzbHK4frpXBTGS7MECGx4YhpMZiDdXTPa6TOSyGXh8oPrWhFqnCe0BHzYRA2LM4YMhc3A9_-BO9KUNHi3nO3bhQV0AAQH1k0LwdL6I7RJgxJdrfdVyXmra6s5y7Sy0QQYPKVdvSRMNj4LOMBtR4qLVdpvKbP74WfGBnub2Y5pFqTkqw8TW5qC8y-g-0l9LHbPOL6JIXVF5LEfOo-wt4APpugGMihjA3F06Vlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=bGmw6bN41o4S_VYo8r4UT9PpD8s605YTIQ9ZVCflDIBZEmBZNaCMciTAy56Fx02KHxJ0uvXMLcuI7xNdHTbzsZRK4MGEQOIBqGAqQMn-mQ-1iScWszYwAoTwuUHDdb4Q_BeAN1mBagGgjzlqgoO5caGU1trnLkgl8Vdulwd821xJgFeLSCGR0uWcdcjfWJ2AjbcR0cfaTJMwqqERhH3xL6a4yjxIdHLd6J2lzkLmDsV2WwebxPJBiJgOtSb6GNWjCjfMQTnktRLXnGbMyJueMPNkXlD92vuvxJYc6qB2mZQ3o8spPM9MbFr9y1f38qdXX6UnHDkd7bG86myzEGdJNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=bGmw6bN41o4S_VYo8r4UT9PpD8s605YTIQ9ZVCflDIBZEmBZNaCMciTAy56Fx02KHxJ0uvXMLcuI7xNdHTbzsZRK4MGEQOIBqGAqQMn-mQ-1iScWszYwAoTwuUHDdb4Q_BeAN1mBagGgjzlqgoO5caGU1trnLkgl8Vdulwd821xJgFeLSCGR0uWcdcjfWJ2AjbcR0cfaTJMwqqERhH3xL6a4yjxIdHLd6J2lzkLmDsV2WwebxPJBiJgOtSb6GNWjCjfMQTnktRLXnGbMyJueMPNkXlD92vuvxJYc6qB2mZQ3o8spPM9MbFr9y1f38qdXX6UnHDkd7bG86myzEGdJNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=RU79v4OngAOKf0hz0F9MhtUBMlddUtpbbvTHJJdPMV5Qsw7GkdM85Cbb0sPvrxBlInubJ1BaxJpeSE8Uhu78Axl7UcQNYjTj_R47R204n2TQcUyls-6NOrwcVx8KYTws35AsYjGgjpnY06m0KNcW-7qxSGWc3LBla2yniq3uIkUZI0VbtNpJbVJ-LWUZeoSoOZuahgQa71u7QJDlsUMy_-OZTChXMr5FlHTBLPcSDLY7y9MwWhtrc9I8yGU8mwKVgwnd6e3f0DSuv-j6dgFELB_oa59druOVqjz-IoZmB0pr58GzlI5Z8DChDVzY-ykJCkvtwDAvXsRaKF8WwYN1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=RU79v4OngAOKf0hz0F9MhtUBMlddUtpbbvTHJJdPMV5Qsw7GkdM85Cbb0sPvrxBlInubJ1BaxJpeSE8Uhu78Axl7UcQNYjTj_R47R204n2TQcUyls-6NOrwcVx8KYTws35AsYjGgjpnY06m0KNcW-7qxSGWc3LBla2yniq3uIkUZI0VbtNpJbVJ-LWUZeoSoOZuahgQa71u7QJDlsUMy_-OZTChXMr5FlHTBLPcSDLY7y9MwWhtrc9I8yGU8mwKVgwnd6e3f0DSuv-j6dgFELB_oa59druOVqjz-IoZmB0pr58GzlI5Z8DChDVzY-ykJCkvtwDAvXsRaKF8WwYN1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=nSoU6fMKqzM-BlzNNjtzeJ0Zku2WO8zlCx5_V84X6ZgAHVUQ5ZmX1Bg9CiQphwsHUFKO4NK51W4xgTPu7eEG3tJYtYOV1fvOeghYX9pbeOhYTpY4ds1kf8awRoQN66dRU_jMCYryFL-ItT7Aep2NjTkNuEu2KLWrcXhbY9C-PAoEFt58fhg0P_pIDQ1oHE-UbByBMFycpi2-HyG8-Th61k28BkAWVeLL4FzJB61KMOWjyOkxDchSWm5R6-c6DbJ30RjYcYq7lEOF3I1PVM4fku2RgtAfoqSj-Tlz1WUOVp34_LeYfb3uGPu9ON0ebvfns_13hwv2fUZ0-NpYN-WmTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=nSoU6fMKqzM-BlzNNjtzeJ0Zku2WO8zlCx5_V84X6ZgAHVUQ5ZmX1Bg9CiQphwsHUFKO4NK51W4xgTPu7eEG3tJYtYOV1fvOeghYX9pbeOhYTpY4ds1kf8awRoQN66dRU_jMCYryFL-ItT7Aep2NjTkNuEu2KLWrcXhbY9C-PAoEFt58fhg0P_pIDQ1oHE-UbByBMFycpi2-HyG8-Th61k28BkAWVeLL4FzJB61KMOWjyOkxDchSWm5R6-c6DbJ30RjYcYq7lEOF3I1PVM4fku2RgtAfoqSj-Tlz1WUOVp34_LeYfb3uGPu9ON0ebvfns_13hwv2fUZ0-NpYN-WmTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vwMxKDQrR7tidlAQCQU3zAW_gxOn41vorYyHU7s4uaCn7JzzrkSpWsy2NSx6j0-lyKmaJKQaG9FngksmDnIRNkuksU2yYcvxAGuPRnHFv5BKSwhIA86NeYQrlvNs1Q5a3HMEces51v7VhWoCeIks4dMyNfw9j2m0t5LeJZCZC46iqqGaCNOf5pFP72ChAApBATURlL_J31a2IDijb6X7s8ie8m3-PECtkCOsYkAaKsfDk-iRYpwQVWKdjyIRSra6ASbRPglzjOMSqhyO5GJ30sC6w5fyelG3tyk-v9SnTdvBAJTjM-T60FeTjYr9WIG-fcij1dZZPqXTRG0fz7Fokg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Jpq8dv1ti0TQ9xUhd1CyGKvfsbWgVfa0C8DF4Lvakjq0el61U2IVVE7VSLXHt-NFs0BvCa7mE9oPfr_wNGbgCVjjvpL4XTZYfhX1jhNwdFSZvlboqR9m6OqxlKWDpyvN0iEtLlYUw_6ajndOjA_sNHnZMWNTyKDiXQzapW0Q2S7HHxlDlF0kOEK07CvRkCsbZRL2t51FmYx8EeELiND0n3BYeCwmhlsw5zbFlCWQzdcll3_Hnk0WIkze2Vs0s3GNbNcOqm0oQ9eaAygLSXn4rWPm2jJZC4CNhRyBiLDmn4J74JJHubkyj91Z8lFyAcnohz6yy-8L6I4u4Qk9ijAtgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Jpq8dv1ti0TQ9xUhd1CyGKvfsbWgVfa0C8DF4Lvakjq0el61U2IVVE7VSLXHt-NFs0BvCa7mE9oPfr_wNGbgCVjjvpL4XTZYfhX1jhNwdFSZvlboqR9m6OqxlKWDpyvN0iEtLlYUw_6ajndOjA_sNHnZMWNTyKDiXQzapW0Q2S7HHxlDlF0kOEK07CvRkCsbZRL2t51FmYx8EeELiND0n3BYeCwmhlsw5zbFlCWQzdcll3_Hnk0WIkze2Vs0s3GNbNcOqm0oQ9eaAygLSXn4rWPm2jJZC4CNhRyBiLDmn4J74JJHubkyj91Z8lFyAcnohz6yy-8L6I4u4Qk9ijAtgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FknvXB-OQNo3pPTKJ0H4AAiZQyB2rSMjDIDPgF1ZQw71XYdwWgWlliL-FDglviEVZyPSvS8xCrfbCMuF6dbJKsXYzdqbi2FlGj0X7FM8GCg71w1AZedKMS9wELlX4N4zR6mW4IVkTo6XJt7rcMguBpsq0dvOXPbYf3y49eKWB9Xnd1dhoJsrvFX4MHgL_jis0JUNMTPAx3B5eh6hz8vRuVbUFGndA9DVRsy6R_aC5qpnVAxDGpPVrpdHrA4Ypkumfqm7OO9EKoxFyh6rkiKjt-vqkpNoBlO4KrN9Of_B-ij6o2quTwBZNWnxEQ3zE7mjWJvXEdIc9pJOtK6SyyKIgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=FknvXB-OQNo3pPTKJ0H4AAiZQyB2rSMjDIDPgF1ZQw71XYdwWgWlliL-FDglviEVZyPSvS8xCrfbCMuF6dbJKsXYzdqbi2FlGj0X7FM8GCg71w1AZedKMS9wELlX4N4zR6mW4IVkTo6XJt7rcMguBpsq0dvOXPbYf3y49eKWB9Xnd1dhoJsrvFX4MHgL_jis0JUNMTPAx3B5eh6hz8vRuVbUFGndA9DVRsy6R_aC5qpnVAxDGpPVrpdHrA4Ypkumfqm7OO9EKoxFyh6rkiKjt-vqkpNoBlO4KrN9Of_B-ij6o2quTwBZNWnxEQ3zE7mjWJvXEdIc9pJOtK6SyyKIgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7PbngB9ZY3Gjea9WAw-UrbKIF01fIa5WU0Cc_jnnaSy3DLyU486GkZn-5JuvICDXhudpDn4vvOr_k5C9RDc4IVI88nvWLpAfOdmi38p-hM0RquOvPbNUYyDL1X6rIHTsQn55SmO1qhp9IzijVUu_A6pNzIDEdQ50UNF9TmCIN8ATOwYwCMNa7wl6Vs06nN0_FP_MpYKUfUaYc8Mxptmsx4ojxKD0Rqgy9O8IU4nx17UTvEqFMxlPxUS7rBhRBr2Ok1P1aQLMxt2eQbaeu2-SWZ3kYYq-RvTSC0Wp9akOdLcZns20o05ofeGCJkY1ADy08k2krBnyRXXpGi2v89qGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=K6Y1Pc6mwIWEIxblxROzUB58GKgI1-Y0WCqM6ofuBq_mV6C1639xxpDecJ9eBBdkFN4GuYWS0QEihq7VwP9A3wZl-XKhZwhxySOp8OcRCGeyTa3SdN3IeDDClEm0IzphOvCnhbvefFIMcIsLtK_jZiQXd7AKGNVGrYUUXZG3O_93bUNdEvOY9MkYZqCcpBv4D9OOPPIeKEDrs2_Du7Ds8N1VqflPcugrfUIaCEMAX9yPy3eYeE2kDk-xgQJI4sCcPfmfOG00FoccyNCC4TXtjWsptg5fewhbg0RqJil0cmbXk0lgleri-qt_OO3y-k1Tkf9TUvIFHEDH4riaRlIz3rL0auwPwMeyN3J4cesE22pFeoRDgUJ4ukMQCZ_grIqKeeW63amACOCowWNTpRTjubrI4qwiEu-gxmGK6K65g5S38RkQqFLWTO1XUdJzd-m4fUirVznUy3Zie94ztJJz9wAH_qjAZ7suWST5dMERnPuikjNHP8PDgZtPQ_hllNO0KyILwT_Znv6TkxoKsOtwlCrGQ_NewlbkGXNmzyx-wqIZau1DyV__Yh4Vslwb6WcdCwugDg-mp30gevZdGmw7ze3WYiUY1m2hhFZlYNbNCggvCIjRvDMbvCJQJsVmRdfK75VCkWS0RASwxeDf86w7MQaK-N9L1Mr1gWuajr_BLlY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=K6Y1Pc6mwIWEIxblxROzUB58GKgI1-Y0WCqM6ofuBq_mV6C1639xxpDecJ9eBBdkFN4GuYWS0QEihq7VwP9A3wZl-XKhZwhxySOp8OcRCGeyTa3SdN3IeDDClEm0IzphOvCnhbvefFIMcIsLtK_jZiQXd7AKGNVGrYUUXZG3O_93bUNdEvOY9MkYZqCcpBv4D9OOPPIeKEDrs2_Du7Ds8N1VqflPcugrfUIaCEMAX9yPy3eYeE2kDk-xgQJI4sCcPfmfOG00FoccyNCC4TXtjWsptg5fewhbg0RqJil0cmbXk0lgleri-qt_OO3y-k1Tkf9TUvIFHEDH4riaRlIz3rL0auwPwMeyN3J4cesE22pFeoRDgUJ4ukMQCZ_grIqKeeW63amACOCowWNTpRTjubrI4qwiEu-gxmGK6K65g5S38RkQqFLWTO1XUdJzd-m4fUirVznUy3Zie94ztJJz9wAH_qjAZ7suWST5dMERnPuikjNHP8PDgZtPQ_hllNO0KyILwT_Znv6TkxoKsOtwlCrGQ_NewlbkGXNmzyx-wqIZau1DyV__Yh4Vslwb6WcdCwugDg-mp30gevZdGmw7ze3WYiUY1m2hhFZlYNbNCggvCIjRvDMbvCJQJsVmRdfK75VCkWS0RASwxeDf86w7MQaK-N9L1Mr1gWuajr_BLlY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-Yv-72PRfbUnILRd_vIvlRnf0Zgrtt4qjayrz0_ZquOdXBFbXL_TjWzuT3baOrmcvYeO4YBTRYIQ5MB2pRxXpGhKd8uOYDmTkgURx5GzKzY_M8-uuiBE9AOF3e408Bc49fxfn2lOmm9uimW59Tb1PDkSLCpxamUCTW-5cfkZyzyE-_SSppwYjy2Jkp46YdIgkZUcWZT0HeXT10PiHffv94IL66EjdxD-uUJrSja6kq6W33N2eTg5UA55x11fJT3Xlc-3uj8gLpwfN2m5UMhMR9WMm_r4LX5EEXPJA5NevSe6bHax49ksW6JNYDVsgJhhhzm_xYWFaLmdIsv8xmn9g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JJ_9T3XYU4LvpWSkEoT5audaHYtwAESC5p9smiiQuiKKFPqHdQ5VSahzgraW2PmSQpy-XM_6GAuMMIEk68B_EiUiZWy417FM8FrOHiUHnqS8criSL3GgvpDx3kT8YVmjhIcjEFXpUzI8QQ8cMlCE54JiQoy29Fdwy3RBbKIPPoJPlHHkxlrglqODhc3BXp6guxjdcxeDs0VF5iudii-_zmj2_NIJFLuZY5qd-hc5XJeCCe1tw8QUhNSYal80yEUrXkdgomrSb3CFsbSxTqMXUHoXlqQaMwBC3M7DmZcHssqPPBIM-vl4V6V3J7oVt23qsIyw2NFZjaGTFWFO1_Ta5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JJ_9T3XYU4LvpWSkEoT5audaHYtwAESC5p9smiiQuiKKFPqHdQ5VSahzgraW2PmSQpy-XM_6GAuMMIEk68B_EiUiZWy417FM8FrOHiUHnqS8criSL3GgvpDx3kT8YVmjhIcjEFXpUzI8QQ8cMlCE54JiQoy29Fdwy3RBbKIPPoJPlHHkxlrglqODhc3BXp6guxjdcxeDs0VF5iudii-_zmj2_NIJFLuZY5qd-hc5XJeCCe1tw8QUhNSYal80yEUrXkdgomrSb3CFsbSxTqMXUHoXlqQaMwBC3M7DmZcHssqPPBIM-vl4V6V3J7oVt23qsIyw2NFZjaGTFWFO1_Ta5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RONRNdFC8ls_jCpNeG1bpVpxj5H7qFn-XLazpbhxVrhmdZMpmW5FG8sXRw3-8YIPHdTCd8OnfxneVmqbkb9vinqIVXoXI-bmmPIcPVwsDAbDZbY9ASIkUnUWoT_fkzCY_ufd7EPo7SufDp8GguB4HRPJ0O9tABGz5wgsKT0EdWKyol7y6Rs0gO5nTNYVdWKpr5yuoAfivaIqGx50x8CLNiPG6tblTM19sc-p3sziJbC6iCBlIxN23vHmohEyQb5cBYjqVOP8Q9KwwWXaPYYD5WWyk510vTkvbo7Y2ZQbnq7S3fTIDKZFswO5qIbxhkOhmNP8MTxYWJln3K8oCUWZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5ni3b9UkPM-5ob_7-OhTUkO0JF0CrxgxVGqyyvf0ziiuHd6EEeM6Sq2FzvDC17eBbxIsMDK61HJP4zH-k3SyW7jYtf9Oxy8DPvnPgenbeUkHuuzV6tNbdwj8kos2_zBT-AGfv-olt4IlVsNLAsIfqIls6t6joniiqfHog0_RWb_k66iju9zM_G5TqCfwTFJViIGwyEQexQo6SlUV70QaJY68ryhz8lOdJ8ZxxuiOvKt3iGPf64Z5axNNVmOtudu5yaqQhKwlgH0hDvYZnQ43WwN7ISzhBQPFgg_bFxg9tHPzKmL8vEKv7g0iLpSfoxVtDKssjjxcAn84LWeoJQu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBjAPFeGbgcxuqaX6w9elFuY5uKyozivKm-aXcfwBu_ldfU5APCUQ3SuampJWqBa5uYe85lXDh7UPGPTxBylnYKxCVd19u3T4nl9SDmiK5KWfAiWym6RKxsPwZCyZIV9JB4AuZZSOjAd4PIqCBBGDVu5xPq6NIV-i0hMzFHYRjSH1wa30wrKKbXeERD2z13FegkeGwuhruvuRic62tLiw2NZvfK6J0E9Fb21ohdyTSquDhNq09z8yNK61bu8iMrq4RrbBLxIj3FyRCvPL_lGX_PgB8qwCkzk-6sBUrK-D-7NiZZjR0bosX7_yEnCNpvvroggDBU7nDA84d-0HMm4-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=GO540D1ZlGiSHd0EGB7r5Y74d0jTjHALJa99bsPU2vbPvnv5-TYC5aQLnZEm13D85xQPw1mUGRhjpL1UmOdYa4aAjYayP7VJ7tr5LQJ2Yb6AuAbs6KyZa6AbkG_rnELMzSj4HbXZDkgdQxzT2pcFX5Q-rclCARW7c_DrN9-IEU5JKuNVMGB8f74lPmDvOhUw3w7kC4YCLyjMJo1DItJ9mKoeEBbHYjrYTaELAcTpb82rjZiNgqz4022g4Ob-91s1DEX-_ntEFF-S3T743ijs-NwEhD17li4AMKRx2fljVtTK3pMEtL-xexIa8So8ioUMIHcJ-azAyxxTLynW59kgIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=GO540D1ZlGiSHd0EGB7r5Y74d0jTjHALJa99bsPU2vbPvnv5-TYC5aQLnZEm13D85xQPw1mUGRhjpL1UmOdYa4aAjYayP7VJ7tr5LQJ2Yb6AuAbs6KyZa6AbkG_rnELMzSj4HbXZDkgdQxzT2pcFX5Q-rclCARW7c_DrN9-IEU5JKuNVMGB8f74lPmDvOhUw3w7kC4YCLyjMJo1DItJ9mKoeEBbHYjrYTaELAcTpb82rjZiNgqz4022g4Ob-91s1DEX-_ntEFF-S3T743ijs-NwEhD17li4AMKRx2fljVtTK3pMEtL-xexIa8So8ioUMIHcJ-azAyxxTLynW59kgIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODec9y-5o6SqySLwJS76zhLI1beug_d-E0S2ThqJxJvwTzFe6QmtAaFVDQ4NMBF1yyz2BJ18fA7fJygZ-MCAcN4DSB2QjnfxPpcUb_5ztjk9bWZoEbwIMLcdc9dN1vbmIw2_22PwPpunD3oX_x9txFHcvi-7gqjBjd_yv6Fg8mNoYvWMkB22W63sWf7GvAMZw9UTrRh7iRE75M1QJl3y5DgYheOQgD9f5ueVlcs6GZi7zuWmfZU4dw9ScCY_f64-58ocjLR56u-Ns4P0MkZKbqeYpCSenIAyEYOsHi6YFw0y76idwzvifTdl4NiOYWe2cpnMHGq6m45Pjy3gd8cTeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu33OgKzUa0hqdrXiqnOKFlZFTHnWu9uCwsFXelJNTqt6Qz7-Khiks6ayBVuGtt8amOgHNtuRnXoffQ11q47WjfM9YOsx6Sq50lLiDPopPzaJgbUd_K4hNw74t47HA__Bop7eZsPxxYbySYjgyhAHZot0o7rcKq8eW4gNKf71vKy4QH6rynNiejE_lYykG_vfNsekzEXKJ9zwt1px1rQC7uNGZ-q1M_yCwVoaFrN4DzBvqt7n_k2Z0QVOU5gYeYeChWXjfDPkv1kJzWHFk8t9z7XX9N2KZe5U3XzyjP9Jh-lNaNhFnF9PHKZQa9UIx1FRj_hdo5a-eODfhFsqqj3jvBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu33OgKzUa0hqdrXiqnOKFlZFTHnWu9uCwsFXelJNTqt6Qz7-Khiks6ayBVuGtt8amOgHNtuRnXoffQ11q47WjfM9YOsx6Sq50lLiDPopPzaJgbUd_K4hNw74t47HA__Bop7eZsPxxYbySYjgyhAHZot0o7rcKq8eW4gNKf71vKy4QH6rynNiejE_lYykG_vfNsekzEXKJ9zwt1px1rQC7uNGZ-q1M_yCwVoaFrN4DzBvqt7n_k2Z0QVOU5gYeYeChWXjfDPkv1kJzWHFk8t9z7XX9N2KZe5U3XzyjP9Jh-lNaNhFnF9PHKZQa9UIx1FRj_hdo5a-eODfhFsqqj3jvBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=iG_XTvEBOZEPRSsE64gK1lxxn4mosqNmCb1FwlGoMetUa0JoyF3j0U_khOhj8AtnUg_nlJR3gV6sOq6ZXkGGbAc-xFmFaCSpIbR97Ut8RcTs3BQJqQWBSkRAZBthA2s9W_a2hKPzXjdD698R54-wop1p5UzNiEDBTiZjlQOAwIIzFLr6xmZBaJ2Y46p9P4xA4hlzGX6ZHPHg9e9CN2hHh7lIi8_we3lC6iI-LpvGVWlf513YKMeHM_sQiJrMx0f38KF_amqye-KuhXFDSXQky9T5qyjhx6UrKmgPBUCo3nFG9mkXFoEl8v3bMy9JQhDr72MVjzfu6-0LitgnhikkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=iG_XTvEBOZEPRSsE64gK1lxxn4mosqNmCb1FwlGoMetUa0JoyF3j0U_khOhj8AtnUg_nlJR3gV6sOq6ZXkGGbAc-xFmFaCSpIbR97Ut8RcTs3BQJqQWBSkRAZBthA2s9W_a2hKPzXjdD698R54-wop1p5UzNiEDBTiZjlQOAwIIzFLr6xmZBaJ2Y46p9P4xA4hlzGX6ZHPHg9e9CN2hHh7lIi8_we3lC6iI-LpvGVWlf513YKMeHM_sQiJrMx0f38KF_amqye-KuhXFDSXQky9T5qyjhx6UrKmgPBUCo3nFG9mkXFoEl8v3bMy9JQhDr72MVjzfu6-0LitgnhikkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MvofuhJsIuZ9iu0acpqgn9cHPDY80qhuL-guU2y1BlCTz30kbghrMiOZSIl_d7miW0abGnZI-mGhLAb_75BX8hmiCNLysuugg30vho4BUESJntjNA-PY-s36R3NZsQHg1eK4U0z4OJe4SnoN9d9Mk92c-MXpPkFE6tx4DmKqypxnD67PG-qtGEROsyAULmE_VMy9VgOlDFBsHF0VdoQTQ0AZyiCHkLS9Vz2cofbpYDzF9bBFhDPJZhkmhcp9CIec-qcdHng1luudkdQUXOfvXZrBtfUgmr4RCf5MJZk-KXu3KHG01JVG_PJZc9rZQ4p8JxoAvnFXxKY_jih6ozLR5SBEFwkwFCEQijWejCI7mawoQTgWTpraMPJpQ0zDaH_WEKjK1AbXWepMaDRcS5ZC4lGHQaxx-_ultdtvQmUIsEYXTmD5JS2oaJWej_DfwU-xAwYKv67xhmFPAF03lfulOXhxAhEwP2rkBrGLdkXXzgY4K8FZkVOYDl8Qg8C2-Lo-rWPuVwl5RWSQlCij5N9RP6Vwf-P2gbtoQu7CBz5od1EL98v8qOZHOeKJmYydqeTqebjZrxR8MC52TDqTzwsWGzfZa5m2TZJBTZdnc3giAHt7MlopMXNtXovY32ZDhd2dnx0jMe_sDLBpxyO5ks2nwgXOHw_Jodz_vQNjapNoV7o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=MvofuhJsIuZ9iu0acpqgn9cHPDY80qhuL-guU2y1BlCTz30kbghrMiOZSIl_d7miW0abGnZI-mGhLAb_75BX8hmiCNLysuugg30vho4BUESJntjNA-PY-s36R3NZsQHg1eK4U0z4OJe4SnoN9d9Mk92c-MXpPkFE6tx4DmKqypxnD67PG-qtGEROsyAULmE_VMy9VgOlDFBsHF0VdoQTQ0AZyiCHkLS9Vz2cofbpYDzF9bBFhDPJZhkmhcp9CIec-qcdHng1luudkdQUXOfvXZrBtfUgmr4RCf5MJZk-KXu3KHG01JVG_PJZc9rZQ4p8JxoAvnFXxKY_jih6ozLR5SBEFwkwFCEQijWejCI7mawoQTgWTpraMPJpQ0zDaH_WEKjK1AbXWepMaDRcS5ZC4lGHQaxx-_ultdtvQmUIsEYXTmD5JS2oaJWej_DfwU-xAwYKv67xhmFPAF03lfulOXhxAhEwP2rkBrGLdkXXzgY4K8FZkVOYDl8Qg8C2-Lo-rWPuVwl5RWSQlCij5N9RP6Vwf-P2gbtoQu7CBz5od1EL98v8qOZHOeKJmYydqeTqebjZrxR8MC52TDqTzwsWGzfZa5m2TZJBTZdnc3giAHt7MlopMXNtXovY32ZDhd2dnx0jMe_sDLBpxyO5ks2nwgXOHw_Jodz_vQNjapNoV7o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ZNjrNDmpm0_Dtc8UxvWIBoB8rP7qhP-kKOERcz_mE1Hc_cDGq_LhPD_CucdZshY_vIG4xXBbUvtL0mxjExCQVSHdvmS9gAVnbQ0EIywvGeW5hcakftmGL6ABt7SEWhxV-IlRTmMKmu47UAzgp38BX8E1dkycAITDghjZIkB9DubK3vBQ5TkN5N7dmRLcbWWAihEFCLOX1sDKGqbLn3jIPE3mlFPJ966aDarIO0VdJVzHcVmLrZB0hKrytJHErpusGmgsXRNHvGDh8OQDN7BLIOOY5cLpJt18rDS5C4A6daRBGd35hTChs5ES1CQV5BT_2uAFsRaHZcoA1QiqOJSg2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=ZNjrNDmpm0_Dtc8UxvWIBoB8rP7qhP-kKOERcz_mE1Hc_cDGq_LhPD_CucdZshY_vIG4xXBbUvtL0mxjExCQVSHdvmS9gAVnbQ0EIywvGeW5hcakftmGL6ABt7SEWhxV-IlRTmMKmu47UAzgp38BX8E1dkycAITDghjZIkB9DubK3vBQ5TkN5N7dmRLcbWWAihEFCLOX1sDKGqbLn3jIPE3mlFPJ966aDarIO0VdJVzHcVmLrZB0hKrytJHErpusGmgsXRNHvGDh8OQDN7BLIOOY5cLpJt18rDS5C4A6daRBGd35hTChs5ES1CQV5BT_2uAFsRaHZcoA1QiqOJSg2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bmoXCPXt8rDEnQa88OBn65g_pnd6gML2nGVSM9ivujQQ1KQwxFBZ3unyts__S2bA5z0Ca9YYIQEr_0ctWeu8sBk9JVNsO8SZ4VU-ziLy-lkuCXnW4C01do1kDdE8CTS7ovd7wzz9TFzOYlz-1RKfz1eiB5MI-7F3Ibm5WwqYvMwEp5KL0_5ASjeILMO1GPMRcxdEVYmn8WJRO-8xZTFKg-Jd4xNmW5XXA-P3hVgbNR8UI9dw1GQcxQEPFe7ZHQOG9RwODOOG2KtSxTEtBx-EVBo37bGgd9IwkqYDYvQnWSqCF0slSWGdLa5iDC5NOLP7kNQKC8UkAfb8b6lw-Pva0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jCUwdoQAAXIgHMrqABZmFyiyGWpArblqtbq4sl6yiYLFRLjoFNpJg_HS7OOv9BCWTEbTURTrUdxj8lt9gTOXmwWWAINfq_NH1ZVmb44kchuamYm79SYmaYRJYVb1p7u3UOqWM2HqJSI8RoLU56qCAN19xMHNn2EW7WyVD9DNYm-Kg8iuqBiXhzrQisM235NswsWF-3givku4EoIcmeuv_sS44cQll65btqeo3QafJf_S2YAMBZ__PY-2r2tZ4zre7ruU_J5Qh1nZlvDgE6LGwcbJnwoJ_cFdVX0TYU1-GBxMBeluutQFQMZKOyNMOqrN0ZThDfzVPMUkcSpyunCvZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=jCUwdoQAAXIgHMrqABZmFyiyGWpArblqtbq4sl6yiYLFRLjoFNpJg_HS7OOv9BCWTEbTURTrUdxj8lt9gTOXmwWWAINfq_NH1ZVmb44kchuamYm79SYmaYRJYVb1p7u3UOqWM2HqJSI8RoLU56qCAN19xMHNn2EW7WyVD9DNYm-Kg8iuqBiXhzrQisM235NswsWF-3givku4EoIcmeuv_sS44cQll65btqeo3QafJf_S2YAMBZ__PY-2r2tZ4zre7ruU_J5Qh1nZlvDgE6LGwcbJnwoJ_cFdVX0TYU1-GBxMBeluutQFQMZKOyNMOqrN0ZThDfzVPMUkcSpyunCvZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=GnRFmyzsVcXw1uW5g7xj-y4n0iHATFprU_09JSQ8YHarVnwaA5k2OhgbzXRXAtPycoMiyYj9M89Z2nxV8rQKrKf8cpG-vX57d9q-RE6eoncMECSpw8zbpS4QYTz1ys7NzEkqnEmjxdCdMqzhxa-EqlasKBO5yXB3ZbBLCEFwAfXfLjbLQ_J0lgXSqI8ycPORqzOU0_W1RIfwA8moQNVRXACjP7NsM5UVuklxMZzIggSmh9m7Wl3Gr5MIZckybYEPhjajmoNcIKpSXl0M26yVsj6496rcJoL7sRSEzfir6oFZE-tXhPFKTompdFqYtC5qRCQCeoIiiPjktqkJq0oNHQJ-dTjthpG0SdNhRLklsm-Ghz4zo4RxSB1k5UhX2ZjJPg8YhoIMEDhE_GzQ-9NUpbj4CsSzyir2FOVpMynKHRai1WLQ2lYlyAJWe1n-UTPtxhgxsgLWiH-Adgwf3i6HDGKKfu4KNSwbARFIugV4eRRz-NuHLMVZ1fWDS1bHxCczU-G5_5XEphjSU7MNgiwA8gs6oLrJsrYzFl1rs9AYsLB5b35keZ6GLWXP9_zEtzrdWKTmXsd5qHTY6jvQHPGaYmYpSvNYk-kY2gOgcSe_PR7KdHYcN8CLkF5ZuNo5YQQ31FVeU1nwcIQtbX15MjoXaRZUlIA1f9F1e_S1846x5TM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=GnRFmyzsVcXw1uW5g7xj-y4n0iHATFprU_09JSQ8YHarVnwaA5k2OhgbzXRXAtPycoMiyYj9M89Z2nxV8rQKrKf8cpG-vX57d9q-RE6eoncMECSpw8zbpS4QYTz1ys7NzEkqnEmjxdCdMqzhxa-EqlasKBO5yXB3ZbBLCEFwAfXfLjbLQ_J0lgXSqI8ycPORqzOU0_W1RIfwA8moQNVRXACjP7NsM5UVuklxMZzIggSmh9m7Wl3Gr5MIZckybYEPhjajmoNcIKpSXl0M26yVsj6496rcJoL7sRSEzfir6oFZE-tXhPFKTompdFqYtC5qRCQCeoIiiPjktqkJq0oNHQJ-dTjthpG0SdNhRLklsm-Ghz4zo4RxSB1k5UhX2ZjJPg8YhoIMEDhE_GzQ-9NUpbj4CsSzyir2FOVpMynKHRai1WLQ2lYlyAJWe1n-UTPtxhgxsgLWiH-Adgwf3i6HDGKKfu4KNSwbARFIugV4eRRz-NuHLMVZ1fWDS1bHxCczU-G5_5XEphjSU7MNgiwA8gs6oLrJsrYzFl1rs9AYsLB5b35keZ6GLWXP9_zEtzrdWKTmXsd5qHTY6jvQHPGaYmYpSvNYk-kY2gOgcSe_PR7KdHYcN8CLkF5ZuNo5YQQ31FVeU1nwcIQtbX15MjoXaRZUlIA1f9F1e_S1846x5TM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v0C7Dzz8th1YnOGzaHGnKniboztNFWW2s0TAxRUsm8HCvnuuL1y7ahyGO_KbNO_bOqrhvZ6GJbau_P1jDoNQ2eT49ScMmhTPQwWB9WW3ZmvB1vRZUShgDC5FDFy8SaOinPqc8CKEl52d4O3gTBCoqfI9QfOvdZqSD-GO5bMc0cBNHoafU1F5jhgfStlLjbcQgpyPxOePL06_yM61hYxFpaSmxJo-MLZN-khTTtB04Zar7kVwTUq7c4Odb_tUD9FpdP7VX3bkkyg1iOc2xXVrOS1wQskcwqSbX4uMMuJyZKdywOypB1Jx_tkr2Q-GqnKMEhzlN2EXlFIEP-u6iV7Gcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=iumETry7uDC6fTNXtFVDX-rPQ5K256HNizSXkZdok8Z8Xw8VGOnsZtHnA4O84AZYRmUy9HLzuC1cxMQAuqLXcTAvudKU0a-K2lbe2VnGVYx_MsAOJvqSi8yUSQs7LahDKY1mXZmjjn109cLrqksTeRKT7kiss_QVX73yG7TEN-r7A8BNMEL_Llja6aZUDOihdZkIBDmfPiQMDU6HlHhHNxPsocDmCdOdM-n_FsbLyibDizvl6-8uwNJnHYu2Y5TsUImL2irnMVBLQtgIoHJ3gnbAtlXe0Pjof6KNwuP4BAaKLsWduwxDDoyP_kS8IG5TTAskMG1Fg-wKzlYQ4DkQ-glxQTBv-TDlsROf-SmNZKOoguX-coeyLxPmSTgzsVkIK7QR5QIT9JE_jplKV8bTU7QuIBNAey0qPXsydYrffnN5lrW1iLSSYsxK0muTeBkI3KlzVORIlEJN-zyJDNnwDvpaFmzadPYH1Wrsm7h3d6JbvMBzktDUw5IzFmUR7quRbjWRVaym-MAh3UkHeg2nSUXG91cpJET2hvOg5C1K1v5wGW4S99OfDsbul4z3S8TEKDFiGktYBukCGLRRh-Pr-SiytS7nqjaMCjezVN9ZrHS2vUGB1CyMx2jUYgwxgIBD20xhEH2e8d0AlOmIM1QS7AavZnt8DYbThhz8Gq4hLxE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=iumETry7uDC6fTNXtFVDX-rPQ5K256HNizSXkZdok8Z8Xw8VGOnsZtHnA4O84AZYRmUy9HLzuC1cxMQAuqLXcTAvudKU0a-K2lbe2VnGVYx_MsAOJvqSi8yUSQs7LahDKY1mXZmjjn109cLrqksTeRKT7kiss_QVX73yG7TEN-r7A8BNMEL_Llja6aZUDOihdZkIBDmfPiQMDU6HlHhHNxPsocDmCdOdM-n_FsbLyibDizvl6-8uwNJnHYu2Y5TsUImL2irnMVBLQtgIoHJ3gnbAtlXe0Pjof6KNwuP4BAaKLsWduwxDDoyP_kS8IG5TTAskMG1Fg-wKzlYQ4DkQ-glxQTBv-TDlsROf-SmNZKOoguX-coeyLxPmSTgzsVkIK7QR5QIT9JE_jplKV8bTU7QuIBNAey0qPXsydYrffnN5lrW1iLSSYsxK0muTeBkI3KlzVORIlEJN-zyJDNnwDvpaFmzadPYH1Wrsm7h3d6JbvMBzktDUw5IzFmUR7quRbjWRVaym-MAh3UkHeg2nSUXG91cpJET2hvOg5C1K1v5wGW4S99OfDsbul4z3S8TEKDFiGktYBukCGLRRh-Pr-SiytS7nqjaMCjezVN9ZrHS2vUGB1CyMx2jUYgwxgIBD20xhEH2e8d0AlOmIM1QS7AavZnt8DYbThhz8Gq4hLxE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=fJ6LKtvGznzoyHcLYgK68xmes8Hn_jqZAMmYdDIUl0Ic6aCHBzNHpKyTwmhp-BJ-LesYZSK-3td6GrMicO_mM0vs6FaoGFnxBuMKdeRyKYD4QSH3bsAOWYKICmvig4UCWbH9MeU8jLZflK_ficwi-3EuMCywNXI7xkkvd-t_LGRCH3SXZOnKSzLicfFmKxTUZusUpClaqi9S9lD4kts0Zril_8nT0JVybPljZ-3eWuo2ht6RlxOskDXxcapYfFyKQI7ZkPnMJyDsmAlo5kIA_KhuvmzlWW4RKgBHQAoXfvbUukF7qLZCgRoHrU9xZ0De-1PpXILimYqKqW1651gtnR9ruE7e4J3G3dj0qBvc7IPT-aEM4CM3QdO5q8utsHGPCvDsFqW1W7ove8EMoNMDMADnosUlWUnEKtyzlYZ7uwL8TDgXtGybIrLa7CIiWDPFBn1Q04g_4hY6v1iF16u9ZcYlo2T0B2_U0F0jfCNGBA8rm-_-wKYkxBs7BCPU-1da6tN7YfnixHYUsENmT4Ejea99_cItGGBg_GqFMfAMRuU0CRxeWTfa-g7fZ9vi8Im1sSKYJT0J_HYXQbHsVrfp2-wFRjTjzF8vMXifk6Q97R2m9hBjF7yhrQOqn_H5kgSHhhUTOQWZF8Mo9KXWo58iJnBzNWC4_UCUqBmpJrC5MSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=fJ6LKtvGznzoyHcLYgK68xmes8Hn_jqZAMmYdDIUl0Ic6aCHBzNHpKyTwmhp-BJ-LesYZSK-3td6GrMicO_mM0vs6FaoGFnxBuMKdeRyKYD4QSH3bsAOWYKICmvig4UCWbH9MeU8jLZflK_ficwi-3EuMCywNXI7xkkvd-t_LGRCH3SXZOnKSzLicfFmKxTUZusUpClaqi9S9lD4kts0Zril_8nT0JVybPljZ-3eWuo2ht6RlxOskDXxcapYfFyKQI7ZkPnMJyDsmAlo5kIA_KhuvmzlWW4RKgBHQAoXfvbUukF7qLZCgRoHrU9xZ0De-1PpXILimYqKqW1651gtnR9ruE7e4J3G3dj0qBvc7IPT-aEM4CM3QdO5q8utsHGPCvDsFqW1W7ove8EMoNMDMADnosUlWUnEKtyzlYZ7uwL8TDgXtGybIrLa7CIiWDPFBn1Q04g_4hY6v1iF16u9ZcYlo2T0B2_U0F0jfCNGBA8rm-_-wKYkxBs7BCPU-1da6tN7YfnixHYUsENmT4Ejea99_cItGGBg_GqFMfAMRuU0CRxeWTfa-g7fZ9vi8Im1sSKYJT0J_HYXQbHsVrfp2-wFRjTjzF8vMXifk6Q97R2m9hBjF7yhrQOqn_H5kgSHhhUTOQWZF8Mo9KXWo58iJnBzNWC4_UCUqBmpJrC5MSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=sa5eqH7Av4VjFHv8oy9SeSIRQhOtMFCwpY0DK81vkN_x6mAZS2PldUy8GeV8uavZFDoTj8Hek4ZyfZnAUiHTxvovE8xpetNIk4yBau5HmJlccE5ppNKwkESEK09HW-my1D_5Jjhbzq6DkR6Fcujhh4t2m4HCeuBeGPYJc3MvSt5iSg4Q33p5-nPjXeL0Z2jYc95tjnXOzVAMlBnj9OA-Bz8XdmgHHDKYGSszSKVXHOxkXCXwyLQqdfllMwHVAuosU91t1pa1frAavvj0z0kjLTeZg2YzXQp9ce_JznMUEUiucz095FB7i8SBdjI6JGCA8Am-Pb9IKiHC8EysYc2qlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=sa5eqH7Av4VjFHv8oy9SeSIRQhOtMFCwpY0DK81vkN_x6mAZS2PldUy8GeV8uavZFDoTj8Hek4ZyfZnAUiHTxvovE8xpetNIk4yBau5HmJlccE5ppNKwkESEK09HW-my1D_5Jjhbzq6DkR6Fcujhh4t2m4HCeuBeGPYJc3MvSt5iSg4Q33p5-nPjXeL0Z2jYc95tjnXOzVAMlBnj9OA-Bz8XdmgHHDKYGSszSKVXHOxkXCXwyLQqdfllMwHVAuosU91t1pa1frAavvj0z0kjLTeZg2YzXQp9ce_JznMUEUiucz095FB7i8SBdjI6JGCA8Am-Pb9IKiHC8EysYc2qlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=vpeveUSDtxW77SPe0Bc76cUbyVG8DaUCQV1JgG5_vX_yUk5idOM8jzypK5M5GvGHXx95OaIYpEAyJUP9As3fOdvyZ5-ZvZe7cwdL9TjgPQygZfGr63pzSBuCOtqAsqRcT0fZFyi5-R0uDqUXDW7t602zRGDgkJzhtAxBulaXJezdIt3dIZnz4lZlGcrwj3tP3A8hzkMPfaqc7RQ7lZBaJJSm6uRuQJjANYLDZ9EmRp-EV7DxiP6WDgY5k_oxCT7HzIi27DAmdwDYFnbC8-5MNsbj1h8T9Pd27i9zuUTUyN-kTAP5d_LmJSPKzm1EKaaCl6Y6FzOYyaQqG43SkexMhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=vpeveUSDtxW77SPe0Bc76cUbyVG8DaUCQV1JgG5_vX_yUk5idOM8jzypK5M5GvGHXx95OaIYpEAyJUP9As3fOdvyZ5-ZvZe7cwdL9TjgPQygZfGr63pzSBuCOtqAsqRcT0fZFyi5-R0uDqUXDW7t602zRGDgkJzhtAxBulaXJezdIt3dIZnz4lZlGcrwj3tP3A8hzkMPfaqc7RQ7lZBaJJSm6uRuQJjANYLDZ9EmRp-EV7DxiP6WDgY5k_oxCT7HzIi27DAmdwDYFnbC8-5MNsbj1h8T9Pd27i9zuUTUyN-kTAP5d_LmJSPKzm1EKaaCl6Y6FzOYyaQqG43SkexMhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=oyqFQ4hFc1Kn7AfgORS9_rNjRk5Da9R9sl4ovev1AH6v-SOyy5TKUdKyhOxRIT2JehO-8dve9ZI_MKABBqSENnlvPUolErPOq_EnpMeo4_XLOmHDyghDKMDHHsIkpN7k964X9hcAIw6NDSE7rRJRBJMcoJ-FH051cezL8mtG1wBoBsvv5GcrUcLJzVOpg3dwWjcpgSBYce2IS6sPnobxLksqUVOz0kgiwd3t70VgbNpi_I5Rvn3TRGWr-KJnnittk1xTFfOlU3k9cFOIqdyxPs1sO56A72XsDNeQX1NX2NOuGjM4lUC4NbsGCHQRFtkpzG7Axn9jBsf8-25Rv9Dhag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=oyqFQ4hFc1Kn7AfgORS9_rNjRk5Da9R9sl4ovev1AH6v-SOyy5TKUdKyhOxRIT2JehO-8dve9ZI_MKABBqSENnlvPUolErPOq_EnpMeo4_XLOmHDyghDKMDHHsIkpN7k964X9hcAIw6NDSE7rRJRBJMcoJ-FH051cezL8mtG1wBoBsvv5GcrUcLJzVOpg3dwWjcpgSBYce2IS6sPnobxLksqUVOz0kgiwd3t70VgbNpi_I5Rvn3TRGWr-KJnnittk1xTFfOlU3k9cFOIqdyxPs1sO56A72XsDNeQX1NX2NOuGjM4lUC4NbsGCHQRFtkpzG7Axn9jBsf8-25Rv9Dhag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=HjNGcVemelql30YYXCzjamsG1FbQ4kKgvgRzIJqIAGmNDsZoyOVbUhr_E5xhuIJFsXN51f8YZGaKkNMrhDZ2K8HGlNWs0EQDWXADVnpvF3UQay36fjXVvXaEJxcCcryJ2nNfPn6a7gOfcSU7bl94rdWorgoXWi57qgufK7NCAAeeIiYFWvs-k7N3PX4p7dHxO201rMzd37lkyW9mWoKMCUdTLcNhLFsrsWeWpvei8A9y4uad_o5IPoJn2sLPryJlOG2XP7yl6bJYEsu1YLY-WtFmm2Btw_GycKvInvhr8jam7RbMTfxDyk5vq0mZB3w2d4mkyK4uWvrO4BvglFgCZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=HjNGcVemelql30YYXCzjamsG1FbQ4kKgvgRzIJqIAGmNDsZoyOVbUhr_E5xhuIJFsXN51f8YZGaKkNMrhDZ2K8HGlNWs0EQDWXADVnpvF3UQay36fjXVvXaEJxcCcryJ2nNfPn6a7gOfcSU7bl94rdWorgoXWi57qgufK7NCAAeeIiYFWvs-k7N3PX4p7dHxO201rMzd37lkyW9mWoKMCUdTLcNhLFsrsWeWpvei8A9y4uad_o5IPoJn2sLPryJlOG2XP7yl6bJYEsu1YLY-WtFmm2Btw_GycKvInvhr8jam7RbMTfxDyk5vq0mZB3w2d4mkyK4uWvrO4BvglFgCZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=TNQum7yRU1JFHk8UimX2QLzSYs6ATETOiSzIYJM3Thmg4jMxwaeef1y-6WX_qCiB4TrxyYnWZVpHRbtsg8AVVTsJeikQHhNWSOICfIBwZtY6WaxdXydRZVCn5Fn7jCJI0ri6QDzONbnD7W-K62Z1W1hqhfyo_DQ8hkQ1Ta9oMaz-TMldQEI1gWPuOyF9v4JEQvHX4DyTAKLqBJfF1hBNwwazPDa0r3aTTMo1SMUOv3woJy94FmrmuXEji2GRcqfmMnf5j65kdevcfoCZie0UsLnxiN2rvOGtKyTOwDOpCYAx3wWN5nw1MHgZ5DQWNJ474qOfGXgA2WhS5lD2ER-hWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=TNQum7yRU1JFHk8UimX2QLzSYs6ATETOiSzIYJM3Thmg4jMxwaeef1y-6WX_qCiB4TrxyYnWZVpHRbtsg8AVVTsJeikQHhNWSOICfIBwZtY6WaxdXydRZVCn5Fn7jCJI0ri6QDzONbnD7W-K62Z1W1hqhfyo_DQ8hkQ1Ta9oMaz-TMldQEI1gWPuOyF9v4JEQvHX4DyTAKLqBJfF1hBNwwazPDa0r3aTTMo1SMUOv3woJy94FmrmuXEji2GRcqfmMnf5j65kdevcfoCZie0UsLnxiN2rvOGtKyTOwDOpCYAx3wWN5nw1MHgZ5DQWNJ474qOfGXgA2WhS5lD2ER-hWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=AQkKkc0sfnJbFFuOZqGlKnJh4ep5zjkYAJezJM81HppHnXruTkX2zy47iZ55SxDXcNttLWMFkMrrFrTI92NCop1dhJ2WbYnfNoGBehOd9SBRLUPLIT_FlAKTsUyuVT2qdS-OoJUbIkExPp1rFZrNX2iKgMVcmtauXp81BhTph-ssVAiHsQBQ2BDEZc0dlEEbEEJoqV0TV3sR2dLjfIy89zINGujytVDDlDBP0DcagCAQWBcwJ3owg04U9k-jtesV93xjitCxbv8_Pcfbr44kQaE82kNt1eB5DcK7VMrMKjwPAXLqblaukCsQeOJChfl7nuZuEBHjwzNnue3H0KZ8hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=AQkKkc0sfnJbFFuOZqGlKnJh4ep5zjkYAJezJM81HppHnXruTkX2zy47iZ55SxDXcNttLWMFkMrrFrTI92NCop1dhJ2WbYnfNoGBehOd9SBRLUPLIT_FlAKTsUyuVT2qdS-OoJUbIkExPp1rFZrNX2iKgMVcmtauXp81BhTph-ssVAiHsQBQ2BDEZc0dlEEbEEJoqV0TV3sR2dLjfIy89zINGujytVDDlDBP0DcagCAQWBcwJ3owg04U9k-jtesV93xjitCxbv8_Pcfbr44kQaE82kNt1eB5DcK7VMrMKjwPAXLqblaukCsQeOJChfl7nuZuEBHjwzNnue3H0KZ8hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jgPhfUtqi9_TCVHFtlItimIS3iv-69WfJU8XR6Ipqk7txo5XIf-5FTJnIE0kN-1SurLwFEW8EiQOBaHt1OQcE1tdan0tuw6oMYQMlMTNy5QRKtTeM6uXj6BCkrsvWOPjD9S740hAfhNRGma0s4hkhKRLwtPixcGkv-m8ng_o9MUXe5LckfUOhaOJmgKpMEjXVGglQVHuYm4W_o3Xw41WGRuO-z13IObyQaOcj-jKEPXKEPVEaiUgh2AHcu-Y0DCgzTxjTQuZ8zcKt9gKR3uLlSvZgt7OjJH2b3zv059fdZjEy774QL8mgdhTofnRheqF_QRawnBWQL03s8VkvYww9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=jgPhfUtqi9_TCVHFtlItimIS3iv-69WfJU8XR6Ipqk7txo5XIf-5FTJnIE0kN-1SurLwFEW8EiQOBaHt1OQcE1tdan0tuw6oMYQMlMTNy5QRKtTeM6uXj6BCkrsvWOPjD9S740hAfhNRGma0s4hkhKRLwtPixcGkv-m8ng_o9MUXe5LckfUOhaOJmgKpMEjXVGglQVHuYm4W_o3Xw41WGRuO-z13IObyQaOcj-jKEPXKEPVEaiUgh2AHcu-Y0DCgzTxjTQuZ8zcKt9gKR3uLlSvZgt7OjJH2b3zv059fdZjEy774QL8mgdhTofnRheqF_QRawnBWQL03s8VkvYww9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXALvGf6Z0SCgPwyur2mOheAHRIkprYL8_FQf7csIOQrahBjkh4mif3ku5dMSBzqAQfizk5OHECMgNOIaA9Jl0MVAfsL3mnCtpazTLecPMnaLGKKbWxFXmlkue9xyjbOJiCPBvIf50dGrFbpmJXaFixlfuHbvNfS1kcJPvLa7W2F0iM9PHWCv-gozj5XJiGMIryqxni2519TYPc-GthwJqkDhcwxWAiweBblFuYdfyjlr02oRqvdEt_hjLeCP3l0_SYwrMy1G-DJF6-zEwAGfpUklkHKksgrw3AWEnW8sbq_oWIX9tIeMnfP6-58vWlHq76t8ZXNK3PZMO4QCco3hA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=AUVQvTLjsr0LxojVXN67QXPxT7kbioocqiSSkWJCXNjuGQGs5FIsw2u6GjBptcKO3uVZW6FBRL_2h6QW_ctBe2pD3yfdviywzizNthyJxQBU66iMVKsDPms2S_obrtWJRh27ivCa6L4Y8UFyAoUfAijyNHg6C6WkGTM7149Qm3L7KysvBFpH7IodcWA8mOdV2rTtWkm7IdSyMu-jRNNhhZVNEjXVrF0d2_oEhj17HM0s9DoVvpDsxgnbu6yqJD0zuyamMjL9zFceAzCYeAGosEtmyrJpZNEyVIJY2f1XxlFB9mk2Ssx6_62tbt9AonhW079ESmiG-QWEWWsL468B5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=AUVQvTLjsr0LxojVXN67QXPxT7kbioocqiSSkWJCXNjuGQGs5FIsw2u6GjBptcKO3uVZW6FBRL_2h6QW_ctBe2pD3yfdviywzizNthyJxQBU66iMVKsDPms2S_obrtWJRh27ivCa6L4Y8UFyAoUfAijyNHg6C6WkGTM7149Qm3L7KysvBFpH7IodcWA8mOdV2rTtWkm7IdSyMu-jRNNhhZVNEjXVrF0d2_oEhj17HM0s9DoVvpDsxgnbu6yqJD0zuyamMjL9zFceAzCYeAGosEtmyrJpZNEyVIJY2f1XxlFB9mk2Ssx6_62tbt9AonhW079ESmiG-QWEWWsL468B5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Zve6cGdurjYyyDLiBStUoZuq8a4bFeNRZZ925UNpLWLBhuOJmBSxGrSfEsY0RMRuYZ50rMLSgS8njzoU29cZMgZc7uHaOJ9_6cjQwrwee7P9XfcrbI7myns5-OaCQgfIg4yEZhXaNwpUD3WhXjcVM5GnBXU7NxjdQQtlZ1YGmB8Xeeu6xj-pd62TO0furieRArFRR0iCGZTl_jzkB-ktgknRZkc86ZAJKJPTFkH0JMeRY6zejjAgai05wBtYz_YZlAELYtc4_clj1EXyrPn3nHLejcEt-gsHH6pSC7jbAk4sYlCJA1QevMs4uhFum-uLTJ50Idmr5qJ_DLUeaS9ahw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Zve6cGdurjYyyDLiBStUoZuq8a4bFeNRZZ925UNpLWLBhuOJmBSxGrSfEsY0RMRuYZ50rMLSgS8njzoU29cZMgZc7uHaOJ9_6cjQwrwee7P9XfcrbI7myns5-OaCQgfIg4yEZhXaNwpUD3WhXjcVM5GnBXU7NxjdQQtlZ1YGmB8Xeeu6xj-pd62TO0furieRArFRR0iCGZTl_jzkB-ktgknRZkc86ZAJKJPTFkH0JMeRY6zejjAgai05wBtYz_YZlAELYtc4_clj1EXyrPn3nHLejcEt-gsHH6pSC7jbAk4sYlCJA1QevMs4uhFum-uLTJ50Idmr5qJ_DLUeaS9ahw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Upl-B_LNizmrzbZWtyD6YvHd3K57HN30j12qfWvnL2SOAYfCnm6XVcp0oFxAMswt4fABdbECy-T3ISTvtGTFjQXJaZ0bAInK56Oun4CZw172rCcYMV_FPrplOs4z6qgiidGzyj2XIUPUMXTlKvgtSFkc9abtWponX2-bVajKYYh0F7LjJoqqLBbVr1kg918h8KPhjTv2fv3pdA6nrJk_vKEf1oW4CWHh4Mnk0eM2Svg51OzMTteJD4ZViXAyLCoF_X2kO6FUf4yqTZSAtNdf_WVT-rouuRAk4CYn1rC8FckSycpDxb7RXnTV3yLrLovtxx7QuJis-6xt4uT3lKM9sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Upl-B_LNizmrzbZWtyD6YvHd3K57HN30j12qfWvnL2SOAYfCnm6XVcp0oFxAMswt4fABdbECy-T3ISTvtGTFjQXJaZ0bAInK56Oun4CZw172rCcYMV_FPrplOs4z6qgiidGzyj2XIUPUMXTlKvgtSFkc9abtWponX2-bVajKYYh0F7LjJoqqLBbVr1kg918h8KPhjTv2fv3pdA6nrJk_vKEf1oW4CWHh4Mnk0eM2Svg51OzMTteJD4ZViXAyLCoF_X2kO6FUf4yqTZSAtNdf_WVT-rouuRAk4CYn1rC8FckSycpDxb7RXnTV3yLrLovtxx7QuJis-6xt4uT3lKM9sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L4heQ82rsNls0A-LG2r_Ui-K0ANbMspGEuV67nJd3x41oOjCQB4ulUlVIFoaIeIeA1EKcva2RyMTW5nfXspR07nRDjnF8hzmY-b1_QOV5nflrLOjeZr3eab_NE4WSHKXbUdHF58zHpcYUJWThmOPfe-6uNkADuCQesHccBal3-JppmBrQ3GAruovppUFGc4aNiI8mZDLS1UHUMu4P3wSGPN8T7RrCHW2OMwqB-B9f7w6OaiQN9pHPtOQEx3nfyCeRFJDxSB1MvXP9C0QqI_x9GKGDdVF086HvZjcSdVsNNAVHLkZvZOouhKigYprWs7DVEpsX1sZKJ4S29D-XFS7Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L4heQ82rsNls0A-LG2r_Ui-K0ANbMspGEuV67nJd3x41oOjCQB4ulUlVIFoaIeIeA1EKcva2RyMTW5nfXspR07nRDjnF8hzmY-b1_QOV5nflrLOjeZr3eab_NE4WSHKXbUdHF58zHpcYUJWThmOPfe-6uNkADuCQesHccBal3-JppmBrQ3GAruovppUFGc4aNiI8mZDLS1UHUMu4P3wSGPN8T7RrCHW2OMwqB-B9f7w6OaiQN9pHPtOQEx3nfyCeRFJDxSB1MvXP9C0QqI_x9GKGDdVF086HvZjcSdVsNNAVHLkZvZOouhKigYprWs7DVEpsX1sZKJ4S29D-XFS7Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AIzPFoTM7yor1no4jmHJi43_aUraTUyL2mIwZxaN2wAWrldJoHkbi1ho9ncc57FnH8mjsS1CJwAG5OBXbzV2o97uuqyW9MsPCzSBjqxlsZQHjbnhvvjwHt_HFJWNIbgcfj6YCAm2DuDfMpedZLYZLNcXGxPeiPtkvcbWBuHCF8rLR6kLiNBuLgybFJG3-jNbEOoxfb4ErPxFDihHR40-Z3nmBX6txwC_g8OH4yxxSm6eOKHScYb0WczZxKIsGxltG4128tCYMEL6uG2LlziFnNNi-FTLZpPQP7wa1TFjTZ4kctDFWGyX1FBuFfA-nm0ZfcwrhDHFexIyIIrGRyo0SA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=M07VR3-Q6TQuWpQ8Ljzj9SomzMvhv4I681yVlNXUVKcxCKkKmeAq0qoS_6M2jM5A2aZLMOMKU-jaWJHS8GhRQwqZhE6b7IWYbJMiVNIAlpeA_S82dOU-iNN8sdRwTiYHbdT-SSj8uJpaZ7k-vSYnt_rYsccoeor1wqP_Or7I_l7DO7iOcgMFkJhrpSBr90U91PGYQYlZm2CDttktjYD1TjnqKnswsHJ8BiUSaAPqKsTTVkkXEBZyzxn8dbLPnz3hnrYZlhy743Jqu2jvopm1AWwG9VHKmkq33PIIg9WCqlQJPhHBPt3PxEekBdVN01avK_J-XVGPSEcEzxVQl1jcQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=M07VR3-Q6TQuWpQ8Ljzj9SomzMvhv4I681yVlNXUVKcxCKkKmeAq0qoS_6M2jM5A2aZLMOMKU-jaWJHS8GhRQwqZhE6b7IWYbJMiVNIAlpeA_S82dOU-iNN8sdRwTiYHbdT-SSj8uJpaZ7k-vSYnt_rYsccoeor1wqP_Or7I_l7DO7iOcgMFkJhrpSBr90U91PGYQYlZm2CDttktjYD1TjnqKnswsHJ8BiUSaAPqKsTTVkkXEBZyzxn8dbLPnz3hnrYZlhy743Jqu2jvopm1AWwG9VHKmkq33PIIg9WCqlQJPhHBPt3PxEekBdVN01avK_J-XVGPSEcEzxVQl1jcQYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=j0_OLaHk3_4LsHhvduVn33Tgp7EteMhc6Q993-WbR92zcbItAqvXj6Fe_oYl-MXb4FDIKqBZ4t5GMLEMTrkriGGj1WsKTIoLFJNG0A_kWwVV7A9myRc2wAsG8jta6dTBBGWunGfXUCQNk2xmZ3cpr_ly7u72dRhJ6D3uPevXzY_UeDckW2w8fWEItAD0vRpviFRJ4wV6NKccTUyvPlM0mOldL3aA_FT6NgpmXvaHAW_TxG7GDwEpEQJu_1g29Lxzh93Ctc9I-BG3oewrI7klal0kkGABUxCcnyfAfG73qrfi99-wHFGG3qVZr6hQlvql4aSh7_1Fb-6NcU6YjTq5Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=j0_OLaHk3_4LsHhvduVn33Tgp7EteMhc6Q993-WbR92zcbItAqvXj6Fe_oYl-MXb4FDIKqBZ4t5GMLEMTrkriGGj1WsKTIoLFJNG0A_kWwVV7A9myRc2wAsG8jta6dTBBGWunGfXUCQNk2xmZ3cpr_ly7u72dRhJ6D3uPevXzY_UeDckW2w8fWEItAD0vRpviFRJ4wV6NKccTUyvPlM0mOldL3aA_FT6NgpmXvaHAW_TxG7GDwEpEQJu_1g29Lxzh93Ctc9I-BG3oewrI7klal0kkGABUxCcnyfAfG73qrfi99-wHFGG3qVZr6hQlvql4aSh7_1Fb-6NcU6YjTq5Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dCZSefMKB34fiVBFPf4aNjpCIZsDY8Yi3s4cjfrd29iTisbDMToiD6rsGKqidFR-maV_ZPCRjkdCt6DnnQrZ12s0XJvQB8pC8SvxOLX4F0FFgCBe9v3b0-Lv-2hUiWgtTxM7dh5GUvIpPmWa8ErcR5Q_tN1QZAWqWLLKW5-HIAolExLTuMb8WUgG8nzmn1zBDsStYlyqHrAFr_ddICpzPRzOf2iYbTMGrBSKbu0O-tSJXoeDOktW3mJUPB2HT-VC8ua3E27TgtrwTE18iYZhLt3t0GWYF7uQQOAcxBGf22_AOVi5uppRH7QvbsQF4spAZp1Xuys4Iwmi6_aY2GwhWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uohSclD2r5_nivA4a1OjXmnzc1teNQbtDqKcaSsGKqqAy8iWoKe9_EkwUwVykQ2fKjhrqjdrocdFly0RQDyG4b3zO_HrQwnGeW7VxlgF5pYMmfU_YM7NMZd95C0vxOdOWXTBLDFFIgS1bIHt7Zk0GbRh0YZam_dpPe-QoZmXWc5N0ICADR4LSwk-WlVQDCWvXRPv9jmhZ2xwevE58kjjyUfAiLFqKiy-qXl5KGQkKSK-w4rs-fwINR1eRkItBdfTwbtVehKi2-Al5-KkNO39qbxp79yNTNxqcv4eAbthTc2aFtYtbVWJSkOPVjJIHs1oRAHmkacYs_7fPVcXfUciRQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mZ_6rmVqpSMRC2aSeHALzyyLUDYWQl_ycNdNTTm4qYntOq0zkuUGyGHhJ21A6uXXRkpOcJEJrE_XY10nJwJ5WhUiL4fBDvdzpn_XvtpXI5U7Mk0AVyvhGDAjsKcPJshtXo8jmAP4Mqt3cbQiz-e5z8BH1P1rga9i01TJxJsxR9xaWrwYVelxY4IETjUa5mfkw8aL97CjvaOi-uYl3VwFRHr12QUB1xQfeFUveY_KhbWldnUvwJys8AluykjDvwYjZ6ixTMj-EnHGOcTQRr0IcK8kyB95bkZuQHFDBqNlsvuaBjDKJ4wXH-C236xXh1VmCC4BUufHRxT5pUyk90KfGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=mZ_6rmVqpSMRC2aSeHALzyyLUDYWQl_ycNdNTTm4qYntOq0zkuUGyGHhJ21A6uXXRkpOcJEJrE_XY10nJwJ5WhUiL4fBDvdzpn_XvtpXI5U7Mk0AVyvhGDAjsKcPJshtXo8jmAP4Mqt3cbQiz-e5z8BH1P1rga9i01TJxJsxR9xaWrwYVelxY4IETjUa5mfkw8aL97CjvaOi-uYl3VwFRHr12QUB1xQfeFUveY_KhbWldnUvwJys8AluykjDvwYjZ6ixTMj-EnHGOcTQRr0IcK8kyB95bkZuQHFDBqNlsvuaBjDKJ4wXH-C236xXh1VmCC4BUufHRxT5pUyk90KfGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
