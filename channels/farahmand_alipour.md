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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-20 04:57:01</div>
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
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farahmand_alipour/6808" target="_blank">📅 23:07 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyaxen8k8EL6XqQG9f0XvZYSurP9g-0TQBaYv1Lz474tTCveyKNP4hsEvlOJth1t33u0k4GDpogbu-i1vJoVJtogTxz83Odo-36hS0BWv3U84CpUv9AUrfhJniR_AGe64VDiPHSSXnEQH9IAWorb84tjreS7fqrnyIM6UvEjkx-y7ZLKO0vzVJFbPs3qZTCytUxz78TsXMbJKGxiYanXS9ydSJMegWnE1mxbOIKWFEnF-5O0KGYLNmp263hNW-69OcVOkqE84ouToZ8-4V5tH8EbgmgDizppvEl5otVj2LEByWADPABttubcw9DRDdyG7TnQYPp8AcCp1kCTLgrfXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زینب ابوطالبی از ایران رفت.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farahmand_alipour/6807" target="_blank">📅 22:58 · 19 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=WNQJI3kcMcaBf8kWJ8WanvTMuowjVvLMpCOmiCzVmnZhqtl61eKgs0y4EzM3JcH_E8J_Qmd4EhBGoZfjSLPUwep-MNsWJ0oWM-kGRecl6cV6kZ7RdAaMldKPVHdYQga1hBDKc_VRuZDNxm7UNfvUAFDn-7Cd3eOBV1NlIBeg3qrvrYS9lT-2IxdPdEq_X74Kmq1M2X6Vv7EOkkka1_w4ihGmjjwhiAm11RN77SxY50OggI8Tb1p8R039JtmNU54rU_Ddi8hqg_0WiU-Vu40NwuKyXS3c20XZa2UQrskZBOru3vjrsB6LC6ydE8LV1TF5RrgAAxZDYccgA4sP2djKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=WNQJI3kcMcaBf8kWJ8WanvTMuowjVvLMpCOmiCzVmnZhqtl61eKgs0y4EzM3JcH_E8J_Qmd4EhBGoZfjSLPUwep-MNsWJ0oWM-kGRecl6cV6kZ7RdAaMldKPVHdYQga1hBDKc_VRuZDNxm7UNfvUAFDn-7Cd3eOBV1NlIBeg3qrvrYS9lT-2IxdPdEq_X74Kmq1M2X6Vv7EOkkka1_w4ihGmjjwhiAm11RN77SxY50OggI8Tb1p8R039JtmNU54rU_Ddi8hqg_0WiU-Vu40NwuKyXS3c20XZa2UQrskZBOru3vjrsB6LC6ydE8LV1TF5RrgAAxZDYccgA4sP2djKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUzlKjZUcbYA4IzdPxIuqKtpY7J0OoehndKL3r7HbJ9OtUWmS6GOVEyZOkjyH2xFjP2vwd6ziUunNT8C4yuwZKr0x-L67w7VniZXRGw7aMeZaccsqh18IJo2ouWDUGnRa51ffJRWXJjdXuZxua4p-ZnPZGIVk5Z-e9NwJHB9UX4p8Od3ZQaPyG2EKAqd4WsxHZwzarbDgXqBMTcmhgiI2JhnERIXVj5m33gIplTkDHtZtYcWBLqcAHDH8kW4tGwPU6lTtw1ejIpL7N-PRtJLkYu-fh3bQ5ueBHTFueQEg2h9f-PAnxxz4z44YScM2Ti6ul0Q9FVj-ahyREm-r8tHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfen_W1l9juy-IAuzODz7ev2S2gANKZTG3o8txW-5kV2nz_yKOOnRoPazhgi2k81MUlqdEZ4O9KGIvvFhsPmIdvl2PWhjj_T-S-R-YvXSM2HEuAXrsHffTrvbThUXWTk-ahOCrJYIrrTGrxcpsWiRwNczIT1ZkCbt1Kba2_lcC_UeL-0-jnk1HCxzEm5rIoUAXTZRtvD9TqnS9was1O85ixVVVql8pt398X2GxgmVEsAtMXhK08bIN8c1D0hztfzlHxSIUlpIdgsHIQSr-ZrusRGuMs6w38pcYFPHp5K8NyQwlVe1hyJLTW3NcFXNUficxIS-EXEUEaafbcXwbgmbg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyDDm3alipq_ITj7Br5iPhhHc1w5OHimhif2xx6rrY4P3ZAOcj45YGjpVfq2Ek94D9pDhufcrOIGy_xSKdBjxU2IZNgv91q5pK5QSeb7M4JQ0jC1ou7acQydndEdTJKB5d4PtfwQQJkE_4AZHGC8y6nIPtQt5Ijh-MQ-IibukN4HrnC0iXlQRM_BCJcfKzQqRxOPTRTgxC30kd_lPTBeheU_J7rV-IK3itvilQUsTlwq7BEuURjQkKmfMB7zLI1biUQK18DgEYp0IuKvFq_01pxWrK3pFY3YREsApbq_yDzaZQnBz-ighpu-L989gk11CyjZlajLxDhUJE3nJsq7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Batzy3MLvp-wXcvKBjEf-0tcRQAzJ6xVpgaDK9onSL5w04uDRHxlK6lp3hclL0Sj8lPOkQaqF2T2ukrsLxA0aLCu9yNdcxhx-BHmE8eiD3I--23-VjH_G8RYOhJsNSzcMGzxkjjeGCp7NETLKz2AUYJnHuYYhOlO9Q7qENwVgEo6As00kMa4_Fi-GiVmaJQ01nYy1W4AC1chFq7eZjQHyCmLLosu11fGLD4Y1zB8dRCQ9B5M9qjWftsxXvQ0AwenUtJJ5q0ci9ySGyZCQKCHmvDAOiEdJA5UScSL8o2ZuKh8-FX8OiXCEiMR7_jgGdRUJv5OpmDIRQtrDK8cmGn5nA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5yvpKGLJZ0xo2QUpPiEQDW0d0v3pzePJiQmHOIZ16s8WmL63S3SA973VwXJrP6d0kYX7JDAe-n_UOp-j3XYWsjQmqKrSZKUaEl7mvkXo38MXli4ccORZYQG9F7-_IbsVZHSg3yibzXYi8PR-E3E2jkGlLlmfshhEbBUhIvW9x18Hz35Fo_qa21pev2FLycjtauuIYhM9MOdzteCHgHYgmxkCnuhnrHOIIcSrkwKCNt3jOs-wRZqGrF8UOA2Mr5ultPvk2j3oVtxV5GK9aDqz2MCnHe3z_RCh8IcwV8fvWoEYMegyOWPlZpnsdGrm8PEGLADhCoOt_rjqWTGQnAM-w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ktXG8vyHC94JoNecEzyHXzozqrbZexeby6DIwb0NCGVWzBTWrzuIhJm4NgwGqnQcZsQDMO3wQHjUZtGX_kkU_gVk_byKPCs2b1l8HBVazBQPtyJQniOeWhY_bx9qROF8NUJ0I9XSCvVt9tdSA_JdvIMMLrXvyWQkVwJ7GlBaeSQIPxY5cFZGRvgyGeLv6j8Y-a9nHSVxU6vsVi-qZZHwamAKcDOY1565EhOWd2l7-ahautbM0otRGkN5YBA8D3JfTS3jybf_EVN41B3SP_cDcS6ci5OQuEnzn7sFxPSOk1R8fWNH4oP9p6ml1WoH7eWe_JDoTexICBgRWfQEcJoCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=L9u1zihX2qPxKBNixdHIBhJ3GMyJXpge69FKuU7HwQVeklgd8cQzX6KKsA8HDhgjw_kFG6QpvXgeGqgfsis41WrNVvEmBJ8tScwADbtzTJ6XGngWhaQmW__xecVksxCkK2WaCEZAZAfqsMh6ylBQqOFnTuv7Pjt15MXAp5p-M5FTQd3ynR3Gykg6mio-ds_w1XuquyWd4Mr6Z5Hmo1bBydTk6Qi8WFDxrlvaI2Tq9CoXKqgLoYiOmuY8t8LhiS_-HggAMxvEK2L7ipdf-KMebHcnJTBNpEopPO0hS6IEBxnnh4_NbcHsplxoQDTBPwxcPGhx6hyqVk5ALBa24d7u4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=L9u1zihX2qPxKBNixdHIBhJ3GMyJXpge69FKuU7HwQVeklgd8cQzX6KKsA8HDhgjw_kFG6QpvXgeGqgfsis41WrNVvEmBJ8tScwADbtzTJ6XGngWhaQmW__xecVksxCkK2WaCEZAZAfqsMh6ylBQqOFnTuv7Pjt15MXAp5p-M5FTQd3ynR3Gykg6mio-ds_w1XuquyWd4Mr6Z5Hmo1bBydTk6Qi8WFDxrlvaI2Tq9CoXKqgLoYiOmuY8t8LhiS_-HggAMxvEK2L7ipdf-KMebHcnJTBNpEopPO0hS6IEBxnnh4_NbcHsplxoQDTBPwxcPGhx6hyqVk5ALBa24d7u4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=QVkMyqAn3C9t8_6UKZBDFAjyscqxfpcTSjp9GQYeaiKIR_-M2ZLKw2PuxfGxinnECWZfao5n4d2ARpPKoSOHrytKL1n-LuLoabz5RhQbA490nJ83troY73PzSuEg1Xzvv-q0nXYBcKUpfMWLI3QqQv8IngbM7AO6T3NWI-3DW1lLal3hDPlTvjIHWQftWt2P6yKUwJAH9Kddkg0SzIPcB9v5bDELB8WFeOz9cHkvrN3iaCnBfb_5qathGGWwm_rZdVcqGU-pRkWfDZZAjo0p-xRCs0Be0VpaWH2lHpDBzrvV0ad60XWTF7U1ObyRUEAYm5ppW90eoc907Ol6vhpLFxL8gXxvtxQg4MHYp2-OQukz_5u7519vFdBt17MeEY2nhS-aolDJH_zp7WqRHHT1gzOQpkdRNjMmDLWKMU02DWN1mbY7rEgyJkFp-K1kXN-SDAGDKqBE9JRcciDYNBaYNSEfMUtzMA_za3HJIJK8nmuqeIGrB7l-YLjK1ossdu5JHh3BvVHQ55udfvlI_VD7-H7tuDQIxhj-yD91rwlVDfrfVJYyFb5gxRWu10GqLWfbswsEn5SEOQ2wBZwfg7aU1ArC5zMMVH-o2fzjPz6fZuc2yhZrQKcVgIbCksi_wjj37_LoOY64PqIg-MYhp_NCmc0Gjg4zpVdRlcFkGfY1XWI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=QVkMyqAn3C9t8_6UKZBDFAjyscqxfpcTSjp9GQYeaiKIR_-M2ZLKw2PuxfGxinnECWZfao5n4d2ARpPKoSOHrytKL1n-LuLoabz5RhQbA490nJ83troY73PzSuEg1Xzvv-q0nXYBcKUpfMWLI3QqQv8IngbM7AO6T3NWI-3DW1lLal3hDPlTvjIHWQftWt2P6yKUwJAH9Kddkg0SzIPcB9v5bDELB8WFeOz9cHkvrN3iaCnBfb_5qathGGWwm_rZdVcqGU-pRkWfDZZAjo0p-xRCs0Be0VpaWH2lHpDBzrvV0ad60XWTF7U1ObyRUEAYm5ppW90eoc907Ol6vhpLFxL8gXxvtxQg4MHYp2-OQukz_5u7519vFdBt17MeEY2nhS-aolDJH_zp7WqRHHT1gzOQpkdRNjMmDLWKMU02DWN1mbY7rEgyJkFp-K1kXN-SDAGDKqBE9JRcciDYNBaYNSEfMUtzMA_za3HJIJK8nmuqeIGrB7l-YLjK1ossdu5JHh3BvVHQ55udfvlI_VD7-H7tuDQIxhj-yD91rwlVDfrfVJYyFb5gxRWu10GqLWfbswsEn5SEOQ2wBZwfg7aU1ArC5zMMVH-o2fzjPz6fZuc2yhZrQKcVgIbCksi_wjj37_LoOY64PqIg-MYhp_NCmc0Gjg4zpVdRlcFkGfY1XWI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dle1zQyOhYJy-074RKFMIirsszPU2fskMMIUGmjzJKf1YrZ0fzDxfOy3XLwHH2kGq6YKmw9B5zd-690wVJWAf2oDXk4e_k9LlwrcD6meI2mEfNF2Rsylqx3OMOhhDS2H1RInYo6uFM1OJWn-hn5LZDoM1XqW_CGdYN9ohuH7qjozsxyv4x1K6zdXZqk4bOJ2vz_4df4PFfIKZaquMtgKJW3dic8l1YGyZzC2msYghePbFor6BfXTx7FvhUvEbvw_wUEOROLJnSyH8e-Eyt0e-h4RPelN7viF9Xm4HtK2MUTjapjyg9-uAUtODOGIjlRg3upb4YfADYkWhm8ypyyBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J8FC6GsCo7zmIFQeMt5ciZN7pja4Mxlv390xm-ak64ZojoHIjfYEsAnpISDjEtBxzYxRXeo0xMQFTRFFog7s82tHsz_Ok4zrMQDN607lHM8-k3cpsowzJQDCC0bQu_xHJQsG7lFwTmiAIxiLAKXiuCr0jZ3yWbxYaiLaNANIVvcSPDLgURW_8hUklbrWVZXD5pSFFHya6B8DyEoaNBaMljGUOvLwQ6uGUrHT-K1vislWwVajQTjJmFwqHldmfnURGlqKC8wgB12uGxMe1nlYAQWIRQ9phEhp6zDZtg_fr4z8B9en17xa9_c9UPuCJvpO2tzRCRGEHs4TEbBAiaofnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o90jwolDbFpaDCfgxvQ48JzRqgw8e6MyIwYAo1__3xGNZmH6OE2Eq9jfFiK9KNQcqhvpQbpR58uWGUdKMdX3JPA4RRqKzYTq3_93eAPE9Kwj7d-JJ1HR6u6uRYIiXPUDIrqi9DmX5Gg9r0UHALUj_PsSiVmWSEgciB56kycHANm_ttsDf6taHIz3G1Bam1CFg2DJJexIwlEX5lxrlJ8Nxm4u9ZV5LLxkTe1zm0Dj6JPU-2W8tSNNzZij4Iom0I7JG6wm77l-opYApfwfIK7qqncmtrFKB8jzL0OWcidEdlczGX0ubgXcJew6bDX5WUSE6dTHEo1rg64gQR9Ws-hk3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=XznshmpASGbDqcgsedOJBMpBCKtH2NM6tcJ_pEGs8y4k0y2_O_tQgii4k4ZSqnwUdHasnOIUQS3fAgDojPKvojSH6H6jvV70Zfj6UqAYofaphDeYMyxryWjfF79l7l4dJLb4I2HyWxdYQNsPiK_SePO9moRpiS0JcZ-Pgly-ktE9vsTDjQec3pfb4DrNHpoacL-RxiL1ezvU6NZH0jvu5ZMHHCNq4v39tf0_SkRny4u0EXfvCsQmCdIvsWmgf-oKSG0Eb-K25cIGLi0yR5OJCzlLB0PfWW1YxC7jPD3x3CRKcNW0p-t2S7ncVrl5Q7RFrodzaJrlJnHLrpi7-5uFyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=XznshmpASGbDqcgsedOJBMpBCKtH2NM6tcJ_pEGs8y4k0y2_O_tQgii4k4ZSqnwUdHasnOIUQS3fAgDojPKvojSH6H6jvV70Zfj6UqAYofaphDeYMyxryWjfF79l7l4dJLb4I2HyWxdYQNsPiK_SePO9moRpiS0JcZ-Pgly-ktE9vsTDjQec3pfb4DrNHpoacL-RxiL1ezvU6NZH0jvu5ZMHHCNq4v39tf0_SkRny4u0EXfvCsQmCdIvsWmgf-oKSG0Eb-K25cIGLi0yR5OJCzlLB0PfWW1YxC7jPD3x3CRKcNW0p-t2S7ncVrl5Q7RFrodzaJrlJnHLrpi7-5uFyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=moL41s8zrjmUYwQpVwpqboNdiO6AWIoiZCN5OBLKXstnqBv0FIztvIGXQ_Dhm-Kr9EIH4At8Eme-NJ1agWzUGbD8GWnd0RAL7IJEHZ93hVztct7utxM_jk_FEspHHiNgOvbP2l2mQ9LC-C_GKGoMaABmkPbzMVjbY47n7iQYS2VgVyVxCsd73K87L7mYpuaaKCg0LvOsbJLzrLeq9smzSlwVnGmI-BJ5vDMHAJwpuuIRlhVzcn_GjiMBXpmaT25RjUbaV0BgSlZPaeuF9Htp9mt_pW-zpYNhZ-iZ8j0aXw9Vf52-HA_C_QMycYFdtGK3ELz0tMh8BPZglfh9paP0zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=moL41s8zrjmUYwQpVwpqboNdiO6AWIoiZCN5OBLKXstnqBv0FIztvIGXQ_Dhm-Kr9EIH4At8Eme-NJ1agWzUGbD8GWnd0RAL7IJEHZ93hVztct7utxM_jk_FEspHHiNgOvbP2l2mQ9LC-C_GKGoMaABmkPbzMVjbY47n7iQYS2VgVyVxCsd73K87L7mYpuaaKCg0LvOsbJLzrLeq9smzSlwVnGmI-BJ5vDMHAJwpuuIRlhVzcn_GjiMBXpmaT25RjUbaV0BgSlZPaeuF9Htp9mt_pW-zpYNhZ-iZ8j0aXw9Vf52-HA_C_QMycYFdtGK3ELz0tMh8BPZglfh9paP0zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcqIMUbFgyix8cyXL4JbM3FLjH8g-7PI_ar5bWRA-KfU6YluFgWdo3oSUUFTGOmFtFikGKq-ZFsOO4UXK6sTtQmA-6ZtqBdaFCTJlR1SSHsqM5SAh58dimiTH--NlFZOsTjIV37ChIVAg3O_kIqG-fI8PVJGmcI2sbkrRj5b3_4PFODuIbLD5OBQ5sj5VNLbMjBx4qCtVewThu1g9qLsZLvt87iS4ZkIPLtwCnki9upk_T_vXP4pS8HLuDts81L4Uc5mMUKl-ESKSqdpGOoG-zMeef4jANowcWwXDXuZuMFbFGIrg-hzW3GUdvhmG7oN9Xkq2-LoxzjElSPEtJhJLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=GDeTMQwhyMfUZl9NMXFuSCly2dwvWDkN2WxmaM4dlH_1nxzGL98HYFamWC4oDCcYfFicBQulRGNPi6rgENN2iGI-J0ZK6eZCz1YCttVkg6MSQjh8Z6YD6h9Iz8Ot3VVXB85fUaGn7fOKOtAomQsuGSJ46lAkCq7qQpospCghfT7BLoY8MoZgaEVmOYi28abCBNOAumhvIXv0ulm0IzuFJV_sRe2IWfztc8BOng2c30_3BrnZJNaycD9o1MFAngicUK8n3omn_Yf3RqedvOrs7ocBKSy5mxB1tNAY03JKpF4eOBGrIVC8Sv41jEPXj7stse32qflb4GyslAT07SLGkEUANg0O45s269jFrZI0eb6AvdPhIlUg25XZv-LPlk4UFFD9taRY43E2XNb6H7MiMepcljmeh2FlRlZNTWltgoWXllb2_LbV5_PM2eKk8upWxN3Gd-2qB-qLHwS-a4DK1LLfgDoG07pMc2AJdfKPAwgcUW2TSKDbeT122xse2bgSJimJ-pY_HYWDsE4sQBQVE8p79DG2uR8yhxy3YLGs1gHhhOqY3cVsXKElTEYU_G8OuZm-RQJaLLggg-CTnw2V67C81U0bNlkOIxP-qPbWpwTZ1sQ8u2Uc6ZHbX4Wy1V6dD0aSvxw6eEBc7K758rnzAEYPUQyF8hVl8WqcDg6nPjk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=GDeTMQwhyMfUZl9NMXFuSCly2dwvWDkN2WxmaM4dlH_1nxzGL98HYFamWC4oDCcYfFicBQulRGNPi6rgENN2iGI-J0ZK6eZCz1YCttVkg6MSQjh8Z6YD6h9Iz8Ot3VVXB85fUaGn7fOKOtAomQsuGSJ46lAkCq7qQpospCghfT7BLoY8MoZgaEVmOYi28abCBNOAumhvIXv0ulm0IzuFJV_sRe2IWfztc8BOng2c30_3BrnZJNaycD9o1MFAngicUK8n3omn_Yf3RqedvOrs7ocBKSy5mxB1tNAY03JKpF4eOBGrIVC8Sv41jEPXj7stse32qflb4GyslAT07SLGkEUANg0O45s269jFrZI0eb6AvdPhIlUg25XZv-LPlk4UFFD9taRY43E2XNb6H7MiMepcljmeh2FlRlZNTWltgoWXllb2_LbV5_PM2eKk8upWxN3Gd-2qB-qLHwS-a4DK1LLfgDoG07pMc2AJdfKPAwgcUW2TSKDbeT122xse2bgSJimJ-pY_HYWDsE4sQBQVE8p79DG2uR8yhxy3YLGs1gHhhOqY3cVsXKElTEYU_G8OuZm-RQJaLLggg-CTnw2V67C81U0bNlkOIxP-qPbWpwTZ1sQ8u2Uc6ZHbX4Wy1V6dD0aSvxw6eEBc7K758rnzAEYPUQyF8hVl8WqcDg6nPjk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=P47hWyOsj9M-u2U518-GltPgoUpHJRUHaGe5chIQDHbwAZwATjjWi82S09kfE-LgW7MdENPfyGBeS9C_uNbQzLsQUl2tbXOO-LSn5e1AClRVnx6_44tGzGeo2cHmc7Qsh3Dnpm2QYPuupnrpLBdTfcIdyndCzIEjHQx2sr7a2LXvIIjkyPHZ2MxlGW_hBdWmMUKKYSf1Ysq9dgPg6kR1qr6uaYzzEpJ97y8K_o8W1Ih2blraWsK6wzc7x0qwyZZ1jWI9efVJSp8xVP8viSUAqllxJQPZTo1NKWUods4DhGIb5JrIIr_bI3ymP2qM0iNPQrzScq2c1BMXs6JBPG_5pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=P47hWyOsj9M-u2U518-GltPgoUpHJRUHaGe5chIQDHbwAZwATjjWi82S09kfE-LgW7MdENPfyGBeS9C_uNbQzLsQUl2tbXOO-LSn5e1AClRVnx6_44tGzGeo2cHmc7Qsh3Dnpm2QYPuupnrpLBdTfcIdyndCzIEjHQx2sr7a2LXvIIjkyPHZ2MxlGW_hBdWmMUKKYSf1Ysq9dgPg6kR1qr6uaYzzEpJ97y8K_o8W1Ih2blraWsK6wzc7x0qwyZZ1jWI9efVJSp8xVP8viSUAqllxJQPZTo1NKWUods4DhGIb5JrIIr_bI3ymP2qM0iNPQrzScq2c1BMXs6JBPG_5pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cc4SmjhZSy2xn2u-31VpXe8u5B7T9SMM-MRvqZou1100Y3QzZwkHMl4gxf9IE4mE2OaOwtkrDukRQrz9--Fa4tYgdWa17N_ZZMUwZlHje32nOw8JEKlN8CGYVUOYqypa9_OTekmzcpgcA0msxsR1Qjcp3v377bprDrAkfi4127Xi_VLLo2QckoghdFhKAf0xmnYyJOR_iMhWhV74ffsY8-ky2kOi1Jj_V8sWHdmoLuy8ZV6Ph4DaO_yN73PnKlGwwlk7xwS_2DyJhsc7V8RAaBicdZbEfLuEVatSN3FnxEZJbPtjTfis6Kw-F9uomrsOxYzr3lzm8vSZIAXDmWiz-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=OGBpbplTAeW78KIwpWZGvdUQsfbpPEZz_ZcaLl357mRK3D6mE0lG7HygbbI14US1k_c0vQ3cdD-Y3SsUFOSqNeTWMHz04tJ8KxRFXHF8BZS5NM1zZ8Fo33cR12v_EAstpwq7tx6t_KH9oCd5_Xt83Drxn4OcBsLiSIobjIwMxVeCTRaRpwcsClzJ18GjBUnarw8alMZhAWp7UOREXVpAbRAGFFNNz8RRBTemvpBpQD_O7a6kia794ClUF4d7BSbTLI_nZn1nNwqyKskx__sEY6m3WohUO7Xjsjqtmzr8QMM_Bv7rPBgoYbgkXEL8uMbDbFHIMxn0J32AAsaTcTMrkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=OGBpbplTAeW78KIwpWZGvdUQsfbpPEZz_ZcaLl357mRK3D6mE0lG7HygbbI14US1k_c0vQ3cdD-Y3SsUFOSqNeTWMHz04tJ8KxRFXHF8BZS5NM1zZ8Fo33cR12v_EAstpwq7tx6t_KH9oCd5_Xt83Drxn4OcBsLiSIobjIwMxVeCTRaRpwcsClzJ18GjBUnarw8alMZhAWp7UOREXVpAbRAGFFNNz8RRBTemvpBpQD_O7a6kia794ClUF4d7BSbTLI_nZn1nNwqyKskx__sEY6m3WohUO7Xjsjqtmzr8QMM_Bv7rPBgoYbgkXEL8uMbDbFHIMxn0J32AAsaTcTMrkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ram_1XG1Nv7djyBBZdZ64uq7d7KsQ5yXmuiGhmp_ryS-srjQtJC9TQVX6u6aAZQHXEDZVN_EJ0Yzfkq2NqZFHRdKb1icumKmoBpjHifo5YSLRdgjUT08H-QOPeRnxpv4kAaOww0t_thr6chM-ekxLHQI3kR1CUACQpfBX60TDOmtJ60d1S4BDukDP7BpgYcp320ebsfsXaXu8GZAkgP3oS3xquv0wriNfhf2TU2hq4ca1390rLKW1_5a8lRowNYUW2GemURzeXhcSWgkfVG0fsW3mJvfbZRpMjDbNNx-R8YLGvSvlwDHmYiq2XB9IXHBmRPgxgsmTugN3W7QyPoU7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mATTV1O2IF1o2K4mCX-CTrWY5kraC3qBbLoBocRUZCHAfgBX2eQdNB2urxzZfDgk0d_r8voWKvoUm81S3TQkAYmygjiAH8LAZOFlCceRVk7al9Zq8MxajmcN4wlzWjjTVkkgd001iRWbGACbXl0p8gq0fIC_QOA1ozQQ--QiE0hPw4ybWnp0Q4HPhxr5J81EjAyEPTc3sTQdlkHg4xOrjzeQ5LN2i1WCCXkvdsH1oBLgH5UiNw5wDE02kITLOnQsLC_nu3oLSFebIFbNfulOf774iM02TzX-MnqfUH_JyvbFyJx0TGUj1hRm4uHaAAhQJMQL7VlVPP0HAm3KvoOpAw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=W8s-dBESDS1PCtQqhKt2vK6QQku9YlhrX9glQdkB6ozYATO6r3aaUqZv5_9ldZUIhQtCtSUFFKC5lI_fbyePAI14Fxfu50hiDfRFiZrHrzSQNldYcFPuOp3wCqW75x0ixDU6Li0H-3hyuEAOIqGWNWXFq06UvCe90w8EgC-zGzTUB4Ig69EVQhTzMV-YCptMNoMDm3uAEbT5cs_fKym28rzrTeE-spVBDWY_Msv1mb7YP1rgRVTaB3gu7j9f5GladSuOxsx0kyPgzpb3gj1wgYvYrR-mf0Qe39ibQe9CYdoOXuU6_-28y6o0UZAfYw_iiE5vwFn5AdQx38nedHpREh9wERAC5VaOtAk8yWzaSt3d2-bDfxqNcmh8sCzoPebJqyqOys2jQlt4RvgKegg1tW1DioT0Bdz7HQjwAdg-Hz6FXSpX2MYoaMG4l3C1AF02S0vY6-0P9eNJc2QB7hZ56LvzqwYblP5uXn2yEhjyxCR5VwsaC00tVtI-Q7UTjT53iFMPvBL2y1tEW3Uf5mCeHyv_z7IGzFSrkyT6xNx0BsnJSlH-atT02wBr_EhODXfgf5C63KOdKb2nsEa_7VqEfnTn65llWnHiSsFDVTieo2ugjg09CMHMiUQXRTnkam2MA8Tb09FpjNCMt8sUNKON-GVgB2qUQEaWc8BogN0crXU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=W8s-dBESDS1PCtQqhKt2vK6QQku9YlhrX9glQdkB6ozYATO6r3aaUqZv5_9ldZUIhQtCtSUFFKC5lI_fbyePAI14Fxfu50hiDfRFiZrHrzSQNldYcFPuOp3wCqW75x0ixDU6Li0H-3hyuEAOIqGWNWXFq06UvCe90w8EgC-zGzTUB4Ig69EVQhTzMV-YCptMNoMDm3uAEbT5cs_fKym28rzrTeE-spVBDWY_Msv1mb7YP1rgRVTaB3gu7j9f5GladSuOxsx0kyPgzpb3gj1wgYvYrR-mf0Qe39ibQe9CYdoOXuU6_-28y6o0UZAfYw_iiE5vwFn5AdQx38nedHpREh9wERAC5VaOtAk8yWzaSt3d2-bDfxqNcmh8sCzoPebJqyqOys2jQlt4RvgKegg1tW1DioT0Bdz7HQjwAdg-Hz6FXSpX2MYoaMG4l3C1AF02S0vY6-0P9eNJc2QB7hZ56LvzqwYblP5uXn2yEhjyxCR5VwsaC00tVtI-Q7UTjT53iFMPvBL2y1tEW3Uf5mCeHyv_z7IGzFSrkyT6xNx0BsnJSlH-atT02wBr_EhODXfgf5C63KOdKb2nsEa_7VqEfnTn65llWnHiSsFDVTieo2ugjg09CMHMiUQXRTnkam2MA8Tb09FpjNCMt8sUNKON-GVgB2qUQEaWc8BogN0crXU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPyaUrKb6JBVONq2CdfYludtO8yrLevee84nV1t-nt8bAQDvigKl1jzBJel2iIj6OEIS55uz0l2f0ki7HhNChBbZVFFmWM5QAIlBHShyLxSqMMpdAYXiV5QAd4yI3Mh8eOWD_BuA5zaJNLHBsyql-iucxSFfaUr_hvI_Px13wqpQ4NpiyUoOT5aEuV3DNKGUzgcr0MDPtZc_dndu3ZEfrvxNXqcHUuAz956vs1xFUYk7NZa6NDVxu9oqQOQ1J7eBpKv4fDCDgKBdUKQeJCs9ztpI2B7E6AqiUYTU1sWH9xTofb4csrUO6byBhvpEjDfZmruShKIV691gIwgqZSaYfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LnP52NU4TNOLWJEPwIxCJDKMs-Ds_n6xxyXYPzy89PaLs2HZUTDKzywt6539G4o5Sf4wEJZCYflVSNARNZbD-7-L7l_rI6R9LN12sqAgJsS6Tf_OD-YXxNTy2L5_ymag8vmy5NiPtNYoqy3hJNv3DpqO7z1ky5hKTEO6bBNc6yrrmJkSjmZyddPmkokq02qAlxMU-MWK2j4AmEmF9dSMpiNwivr2D9CUrJwrZto4wmEXB0b2AL0b8z99nrrWQE2ggFcgUOcRiko75gbmCans2aCnXXAaJfOw5p2uiX4c3cU1i6frx6wr-6H8AMevP0UGuJvdhTsy1phxKZKzdJw9Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=b9qYaEBW8EKgEwQC0KbTSjCvyj2WliH2ZclIhVQAvCzbLhE2xWBOmhqYtJR3m04FXBcl1CXZCk5tP9r2hRdI8TIhXpT4ik2wEkrhxnEtiz7ZEUdy2ycBDgM5j55N2gPzjPuMNNfC37LMsnpAVN0gYcCJPOt3Rwpt11zkCKjOVkKEXJvrc2ilXoQkRtA_y_tYeWl736pfNkEE9NqXPN1z40WjF_a3-zkDYDOyggobZUaiILVnUBBjAgcMBVHDdybpPoXocQAj2GhyWiXFXlR8OyZDOa4xmG_lvzhO3fVBYf0U6grNfjqg-ae6OaD6r00X7pUCCF87DUdHQ4Clj2WHNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=b9qYaEBW8EKgEwQC0KbTSjCvyj2WliH2ZclIhVQAvCzbLhE2xWBOmhqYtJR3m04FXBcl1CXZCk5tP9r2hRdI8TIhXpT4ik2wEkrhxnEtiz7ZEUdy2ycBDgM5j55N2gPzjPuMNNfC37LMsnpAVN0gYcCJPOt3Rwpt11zkCKjOVkKEXJvrc2ilXoQkRtA_y_tYeWl736pfNkEE9NqXPN1z40WjF_a3-zkDYDOyggobZUaiILVnUBBjAgcMBVHDdybpPoXocQAj2GhyWiXFXlR8OyZDOa4xmG_lvzhO3fVBYf0U6grNfjqg-ae6OaD6r00X7pUCCF87DUdHQ4Clj2WHNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=Nzqi-04P2L2LIYN6hSf2UKhcQqpwtSN3UVOPigGOyg3pCIQfAqhvu5TpMY2q-XFlHKq7HSZSqDp42f8A0DZyrhs9_bU0jTuSfJ4r3DezfD-ihTeZwFxz2Jg2HWME-ZunEBZ5UW3zVWbFR5MG7k8hHxZDCFMTYFKJ_1p69QPRW_KkoM-E_CM-hIdFfcfRozgfV81dvr6SRYVHxeQiVQIvXZNAgB3X6soUrbs_5-6V1S8-s2iXbvhNvpvcs-FFFZ2E1748K_zdE8H9Z0jznPRw0wj7n9NXeNYpTQ8rshJLqIPfay5izEEJjhObzRLucpfCYUeZJpDMY8qpWd6dncxNYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=Nzqi-04P2L2LIYN6hSf2UKhcQqpwtSN3UVOPigGOyg3pCIQfAqhvu5TpMY2q-XFlHKq7HSZSqDp42f8A0DZyrhs9_bU0jTuSfJ4r3DezfD-ihTeZwFxz2Jg2HWME-ZunEBZ5UW3zVWbFR5MG7k8hHxZDCFMTYFKJ_1p69QPRW_KkoM-E_CM-hIdFfcfRozgfV81dvr6SRYVHxeQiVQIvXZNAgB3X6soUrbs_5-6V1S8-s2iXbvhNvpvcs-FFFZ2E1748K_zdE8H9Z0jznPRw0wj7n9NXeNYpTQ8rshJLqIPfay5izEEJjhObzRLucpfCYUeZJpDMY8qpWd6dncxNYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FgsECc87-ifnspXU3JEfpPrLuhxyOpq_MdqNXeoix6WpH_8TiOlV_LHi2Me0gC78TO4nPlIguvVEXiPK9Z-CusQ34dUxczmL1uxC7pg8MYuKl1VsHJ8P-6xptHTDhsm64fgGIp9TL3va8hJdvhjNw14M-UDwZgI927kjj9HHbKt3x3g_w8meL7glXDQHne4qLxzA6SPeGCnWRMZM5SJhmkAsewbqyvscR7exRT2QNgpONOEWERU7m3QePIzZODUaWEJB3Sw5e_Mp7hDLstI5h04SumWuJuhvh8QN2nxpAYcmMGR1WMj7MWZ4hTWr-_etbJ7fHpmpmUAuHDJnfVqsaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=FgsECc87-ifnspXU3JEfpPrLuhxyOpq_MdqNXeoix6WpH_8TiOlV_LHi2Me0gC78TO4nPlIguvVEXiPK9Z-CusQ34dUxczmL1uxC7pg8MYuKl1VsHJ8P-6xptHTDhsm64fgGIp9TL3va8hJdvhjNw14M-UDwZgI927kjj9HHbKt3x3g_w8meL7glXDQHne4qLxzA6SPeGCnWRMZM5SJhmkAsewbqyvscR7exRT2QNgpONOEWERU7m3QePIzZODUaWEJB3Sw5e_Mp7hDLstI5h04SumWuJuhvh8QN2nxpAYcmMGR1WMj7MWZ4hTWr-_etbJ7fHpmpmUAuHDJnfVqsaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nv7FV8FzSNMp1hTWDStfP2_MEN2WjKts7cDxZrDaUX4gTkzupDXzfyN_yfaojaO7k0l6WMN7x6fT_8JRhF2gQlp9BGDYhMLAPuAU3V3PpQ6Mag1qzeSxAkN8U7OarKaUdtKZzG61cLOhpvqXH9Cc1l4JZfN5wQ4AUXYjV4A5c2hM1knobfMqDdgsJM4srWbzN_7S8LxlrWRTGy-eegM7bjsUHoeYGRDai1wI3niTwrVO_V2vb0Lavcuvg6IhASEdAgJCNPPSwno9TzmW0429Eq4RgPlKiWmiBTf6qcB3jR9r6NKVevFuOtwK_u3nzCVbfeWgz5DVIhyhsEonU6MS_A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro5D7kgV5bwq3tGvOYpkPe_fFuSRlqAHz3lCJtyikFczEsruFk-Zc_2IxV7DOlvwS3msAFlXO-VasT76swi8brSipVMS8pTRQwl3L2GmA3wZ1L_3s9wsA9nVgvNXocGhgyXHrCNZYkDOY4Fs8vZaUFdtMN-9aHMnj25HHcTHpWlyhzMWG-Dr_gOs50srym_yGVYGwZ-iJWgsC3Jd1QH9Y1_w_C7X8xTuFzb3LJ0Rzq6_gDfYgEffLDdpMhH-M_zRuiY0Xwl5qOyjMTCmuFjtfQapER4wQrt_Wyrf9DQRUEOAEI9TOXUXKsE5AwsZTwKUSpqXIXS1oAh45x5a_CdGpPfk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro5D7kgV5bwq3tGvOYpkPe_fFuSRlqAHz3lCJtyikFczEsruFk-Zc_2IxV7DOlvwS3msAFlXO-VasT76swi8brSipVMS8pTRQwl3L2GmA3wZ1L_3s9wsA9nVgvNXocGhgyXHrCNZYkDOY4Fs8vZaUFdtMN-9aHMnj25HHcTHpWlyhzMWG-Dr_gOs50srym_yGVYGwZ-iJWgsC3Jd1QH9Y1_w_C7X8xTuFzb3LJ0Rzq6_gDfYgEffLDdpMhH-M_zRuiY0Xwl5qOyjMTCmuFjtfQapER4wQrt_Wyrf9DQRUEOAEI9TOXUXKsE5AwsZTwKUSpqXIXS1oAh45x5a_CdGpPfk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aOQHMu-6xB3s68QaEXb_BB63Y6j81y5se_2zPR6bm7Y1HEEWqg6if6zWnGpWGbeKPMyNlFcbXwgZ8EDFRKdzll0iBLZYgnAVkCkvAi0L0wDBMOm9CYUerHsnryVOutVA4OsVTuWwTd8HRL2Xgsg6vcByhgoSoZ2Me-zukwyRlKRmqaaSzwhl5iCaxmvRjuHNAFBirvpgjIQsbEFDWpAlos255PN6pes_JZzqnxcbtPyqXYXHF6n176O4_wnxm01ayOsM6Q47FfWBUO-VukIhLt0XspqNTFke9tM8XeGt5ti4CTtYTGK-WIEcM8Xz4QEJJS5mqncM0Gv9nbRRnjf57A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aOQHMu-6xB3s68QaEXb_BB63Y6j81y5se_2zPR6bm7Y1HEEWqg6if6zWnGpWGbeKPMyNlFcbXwgZ8EDFRKdzll0iBLZYgnAVkCkvAi0L0wDBMOm9CYUerHsnryVOutVA4OsVTuWwTd8HRL2Xgsg6vcByhgoSoZ2Me-zukwyRlKRmqaaSzwhl5iCaxmvRjuHNAFBirvpgjIQsbEFDWpAlos255PN6pes_JZzqnxcbtPyqXYXHF6n176O4_wnxm01ayOsM6Q47FfWBUO-VukIhLt0XspqNTFke9tM8XeGt5ti4CTtYTGK-WIEcM8Xz4QEJJS5mqncM0Gv9nbRRnjf57A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxdm5yycxOlbHqUrth1jA7PMkL_F3IoB6ZYmR0xHcZZrIHAvyjGGDkyfB--396yCFP4v6FHdomcd0eQOP_5WyGIWEUSlYqnfmP6GCJeLj_XyUh58mVDOrnmGmkK3JFh8cg2BMHZJx2zFNK-qi8DWJLEd8UHwJVFu8WHmfY-vqXA2OfPm8Tk8ACOUBJzVFbOEH1ZpES_ZaYal08EF3xL40_MzpYQCm6-o-tpB9lJ6R7yRCTwM53lR7wGtjU-_mg-WefNNIz3PLbNkHmEl3XDWi3y_b9dbTRBi8lYZqzqGEemc5hqcu3HUMEUDnPoFSbnmMtGBaCkF3YSGGTTDR_wcRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=FZD08F2gdyVPq2Q4AtA1WzEQS5Q8nwWcDaHUx_6Msev6Wg4vX0wOygvkgkbjKA0_A5D6xXhPKlJJymk3gC_9fDrxqEMWBRhN4HQyZ4yp5DAGC-C9OkWWQL5NFht_zIsc3FKY7CU8b5cwq-5lBlO-kt1r9PQIlPwo3SZE-aQSeOBGR9TZsXylhyh35kWH7wbPMW4bIh026DpdvssFwMzGdUaUJtFj4ssy_6mCi8QmnJGMuAAu-t8f-dUw2_zOF40urGY9zyBBpRIIrhPr1IIPjDo_JBsX3LAbtlfVDCvv_qxuXjMNvpkbLczA9qW-G_eoIC6U5NdZ_XaRl1lv_pZafW1TwDQ3kS_8MrVzKJ5qfA74CJcjjL54fQ_9_aMXebfFdmpgq_d9obWKKilQqHT6zUWSTmjA7uGAsIMNV2fD3aAeAQaSoBVqZxmfHJNuIks0nxbvDdKIjFE3q3BBaefRcQSObVy-EfjPrg4qE2yPv503EEUHTO-kHOI-aPtZIepN6DqlJFv_T16izdrS4oSI6vKZv_lnjpdQIY0C6OXkdF8i48ODr4I81QaH_5wTVo2zCGmZOPvn5Z9eX5q1UufWSlDFYioACGCv17vGXeImdyQSksN0zirD2ouWj2_tPZ6RqtfU9cWCyKx7YFjRnFo6CWq-gGQMQ2OechS5WkY8QS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=FZD08F2gdyVPq2Q4AtA1WzEQS5Q8nwWcDaHUx_6Msev6Wg4vX0wOygvkgkbjKA0_A5D6xXhPKlJJymk3gC_9fDrxqEMWBRhN4HQyZ4yp5DAGC-C9OkWWQL5NFht_zIsc3FKY7CU8b5cwq-5lBlO-kt1r9PQIlPwo3SZE-aQSeOBGR9TZsXylhyh35kWH7wbPMW4bIh026DpdvssFwMzGdUaUJtFj4ssy_6mCi8QmnJGMuAAu-t8f-dUw2_zOF40urGY9zyBBpRIIrhPr1IIPjDo_JBsX3LAbtlfVDCvv_qxuXjMNvpkbLczA9qW-G_eoIC6U5NdZ_XaRl1lv_pZafW1TwDQ3kS_8MrVzKJ5qfA74CJcjjL54fQ_9_aMXebfFdmpgq_d9obWKKilQqHT6zUWSTmjA7uGAsIMNV2fD3aAeAQaSoBVqZxmfHJNuIks0nxbvDdKIjFE3q3BBaefRcQSObVy-EfjPrg4qE2yPv503EEUHTO-kHOI-aPtZIepN6DqlJFv_T16izdrS4oSI6vKZv_lnjpdQIY0C6OXkdF8i48ODr4I81QaH_5wTVo2zCGmZOPvn5Z9eX5q1UufWSlDFYioACGCv17vGXeImdyQSksN0zirD2ouWj2_tPZ6RqtfU9cWCyKx7YFjRnFo6CWq-gGQMQ2OechS5WkY8QS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/boeTzZbw18bZMue-bI0nzbCNBCdXq__87uexmEWV6EPXKEV0JGZjOR9wilqayUMcZ4oijz-ZI2OQurBMp2dlm4sjHBfFQ5AGSaupa6-dTqKivG8Bhl8OfY00-lNRFZeGEqj_w3xP0lNB6R-UwughLdcmJOu5ldMK_AMtF2PCOBXKKyFBL4L6Eak3bFoNJiZNPvjiObl3fN6mbnKLpNhGjTzPNaz8Nokg9n0yxInu3VU1NW96SM92tMAsfimUZNldbY2RVcqCt3Wvsm7Dty2OozBrab-UyqhYk3J0wa7EFnNGPN8vNilSkuHMIGNKB8Q1ixF2ZZoqHO27oDIrSlWsNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=I3SoHP3fNJfbeag5IqVtYtjpiB6qtvwk3u7ATIcGNwdrpbJYbc_x1ACyc-obNWCnTifu6PeSos00DN7jdwEiKt3yX8m4gtwjb5_Tq81U65Sz5SzQ9AjeRXqpLjVDZs775lzQc9UJSeVEdkf5Jmpz8euXdz586J6wLOKKxoYvOtw9MI9SqrHn2Uib2y95pE3S-jojsv7NXEQe-saxpTlm3DFIC3PlEtr2KxD363S70PffNUA05UweSz54EheHjJeDl9P8hm2_07EHi3tWeEchoxZBZGmQevq3FHq8kv77_cUDPVPI-JFFpe7WznsRQTEMhvT0WqN3HIO6J6YmV9yP9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=I3SoHP3fNJfbeag5IqVtYtjpiB6qtvwk3u7ATIcGNwdrpbJYbc_x1ACyc-obNWCnTifu6PeSos00DN7jdwEiKt3yX8m4gtwjb5_Tq81U65Sz5SzQ9AjeRXqpLjVDZs775lzQc9UJSeVEdkf5Jmpz8euXdz586J6wLOKKxoYvOtw9MI9SqrHn2Uib2y95pE3S-jojsv7NXEQe-saxpTlm3DFIC3PlEtr2KxD363S70PffNUA05UweSz54EheHjJeDl9P8hm2_07EHi3tWeEchoxZBZGmQevq3FHq8kv77_cUDPVPI-JFFpe7WznsRQTEMhvT0WqN3HIO6J6YmV9yP9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLGfqzudj6_cjEJCwNU1n3davQz6QVoFVoz5kTMuPtui0UzY9zlVcAewO2ofw2jS0pqs0akAru4Snv1gilIq6sI0mrXjf6tKP6ZgBbwX_RBnX0OBYyHPD7UOtz4IAWsuhUeiAMngEG7_CpI4Bg73vnUgfZiYtR2ak2GftToc84MKqIlrgTiYysaMfb3qffiO2o1y3DJyr-yoghTb8hTVpdNeDE7EhQloZwz8-9ihihpT5RkcznXhbUHe0TYLct0M4m3tT6eYi1GdRxcjn2AM7PcIWVrLZv05KdpJIOGLMoC0q799tjkrCYI16Libh6Yz3Qw526crBMHko_60t9qeDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b17ZOi9a9MXRo8XjrCG-nyFX7QFtu5EqvRaLg2YD0LOWYg4oDkkqNtt13idDSyT7hil5g4Fdw6taLxB_0HGaImsD3_jRBEAJOCU_me71Ej2bNzCOmeCKknmaESc_BidYijSUFzxco5VCaNiGr4lg9NCo8KNtyqyf4oNQqYkh_NCVPUm_WjsVtNoZ3_vwyi0R_rnpbwASLD0a24m-btzprdeNP0FmGmtaNTfkS3-xw0DoMnlcdHklO8u2_vEho-at3MetbusrSVj7PI7AdV-KVOEz5O4ZelYrg3RgMU0p8hKhlOdCX512NdkonPkMHLESPwu6CZhFVfDoWr3AwaxnJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYXE5Spie3MQWpFoHsw5IeAVpN0K5q4U6v9t0_k-0OY_5Y1PDcmigX4PuHxryhs76DdCWMEZyeSpE9vK0XDYtj9Z-yw6narVK3sxhjp5fWJ6ZrL4DCatzGTOy4LdSZ1p77rOWftXxRLDYFXv4IwnHOqsx_Md2nPSBdYaKBAt-B-yiXnO-afeuUn_sujwnO6NGTBS5B1CW7x9ls1F4wjqU7rU3a9GzRdNZzviDKA_ofU-sayZ99WeDgzpFjaiN84bqXclnWdezn2cUvpsNV1R2q6UMkMLV1PybQsFAmowo3ptmzIBdO9cXOM7cSAKEGjfHOG2CUBRQ82SEevDVNTKwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=GTH3E317_s4phRG-KaI0qA2NDLOw6jEDtNmuAui2TqeOG8aB1sp8VPzR4OXKez2NH995D38P6HnbwFswk6ebjFCfaw1hdx1QfCKtXv8V2f_hxh2Wkfvluo6aM1thFsj5_Qxsq-r45aE5Kv9LEtkzSk2njg8UA1nJYZbzN1YKZGjYwTqt9UajQ2O783riahiLh_H0cri0qDMBsKAv0bMZtwQXUm160an4TAmqwladkbQOvTXy8qN3FSqmFUlOV-R1hu4uHVEtICkpbz9lgseyyUNLWQ70vAX0_kxpplaETuqfhAnKUgYdGjRZbaTCigdCYo-eKHWUyUGiVyptm8mPyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=GTH3E317_s4phRG-KaI0qA2NDLOw6jEDtNmuAui2TqeOG8aB1sp8VPzR4OXKez2NH995D38P6HnbwFswk6ebjFCfaw1hdx1QfCKtXv8V2f_hxh2Wkfvluo6aM1thFsj5_Qxsq-r45aE5Kv9LEtkzSk2njg8UA1nJYZbzN1YKZGjYwTqt9UajQ2O783riahiLh_H0cri0qDMBsKAv0bMZtwQXUm160an4TAmqwladkbQOvTXy8qN3FSqmFUlOV-R1hu4uHVEtICkpbz9lgseyyUNLWQ70vAX0_kxpplaETuqfhAnKUgYdGjRZbaTCigdCYo-eKHWUyUGiVyptm8mPyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JAL0Tc1JI6nJOudwewNCAfOyX4Wsr9kQywECAB4Pl7JEGLwzr6Ii8Ak_3zrw3CKEL1dcBSUJ0fY1XUVIaMO8NVwLyZEKK4KiEdqX1tXm65cL0-B0WmDt2RumY8zSbO1oZWuyYT5HLjiKlcYG7vmHLWykyIlHdepA2GLjACB1_4CPwp3_eKFUR8F-EQPn2Te_U-nyGYXR6R7pbiQJTFbfpdE3yOR8ZgZ8h81gvQHe9pdSHWYsbZhcwif7DGiIZ-h2UYR7vMZbpR_ThICLGPo7ySA9PVyCUxd0Ji0iCKqPghQ3IcYrgK2X4nMVlrQi87xI-fkZXcvwGpi8HfkEDhn3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFJStGWQXyiFF99MufkZpv0EXuPFWyhNzH2L6CPiEH_wL7zHCLJR6-Boq3Y1FrZzhqknBalrkK2jonQAeM6heJ_4ZTu12Utk3kRi0XFGIurNrD1OtVKTMT6ul-S-ud0-9P7N33KA-0s29f7Q6ekU6Auc589HVsLg29d05Fzr9_dB2xZSTKsU9kobE-z4Q7MsDycuqf9zkgFurZdKINiTwXzNln8C7P1RJ4_LC0D_t81vVLLCNcPMYFTRCL8k4ZRZbH2ES4zLx1AknSfJ8ntTj_R9dPHSvuC9MkEvxwoAqOJ96pzKuJHUBD9KnTebUyx8xhFvOMKexcCYdiz9hVNepL9Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFJStGWQXyiFF99MufkZpv0EXuPFWyhNzH2L6CPiEH_wL7zHCLJR6-Boq3Y1FrZzhqknBalrkK2jonQAeM6heJ_4ZTu12Utk3kRi0XFGIurNrD1OtVKTMT6ul-S-ud0-9P7N33KA-0s29f7Q6ekU6Auc589HVsLg29d05Fzr9_dB2xZSTKsU9kobE-z4Q7MsDycuqf9zkgFurZdKINiTwXzNln8C7P1RJ4_LC0D_t81vVLLCNcPMYFTRCL8k4ZRZbH2ES4zLx1AknSfJ8ntTj_R9dPHSvuC9MkEvxwoAqOJ96pzKuJHUBD9KnTebUyx8xhFvOMKexcCYdiz9hVNepL9Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=hKNororRO4qeaDQ6UCm0iZXxXZ8eRAIxIkG1kj0LEQNCbeqqzwhfa_Ql8keKoqKJhPTzc3alL5FoB9RA2ADVi8iibGHwSxk84nnphpiJRLJ6E9Yaz57p4smIayyNraV3vrMxDZ5TUSKaAyeVxFUPQ7ognIygwa3Qk-8ebilHpWvEz5dronpW1oyPnKhgPc24icd0LT6xG6dFC1Al2ck4g9kTIEmL4etc00B6wuF7Kc1WjAdp5QSfcoU5_HztePuq6uwWzFMWXaJmoBe4SnrM5u0Mcn3JSaGJ7ehxRV7mnRoFLXmpFGLNI_T_7hcVE_6VWgk3wOD_VsW_NABY3YUgVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=hKNororRO4qeaDQ6UCm0iZXxXZ8eRAIxIkG1kj0LEQNCbeqqzwhfa_Ql8keKoqKJhPTzc3alL5FoB9RA2ADVi8iibGHwSxk84nnphpiJRLJ6E9Yaz57p4smIayyNraV3vrMxDZ5TUSKaAyeVxFUPQ7ognIygwa3Qk-8ebilHpWvEz5dronpW1oyPnKhgPc24icd0LT6xG6dFC1Al2ck4g9kTIEmL4etc00B6wuF7Kc1WjAdp5QSfcoU5_HztePuq6uwWzFMWXaJmoBe4SnrM5u0Mcn3JSaGJ7ehxRV7mnRoFLXmpFGLNI_T_7hcVE_6VWgk3wOD_VsW_NABY3YUgVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=qe2JbucNn7TOD8ntNvh-_pqAdxt4Xn0Y_p1gaGeWL-61mx_racahqVc94StQbSbkJMmakFY2ertmcAQwBWr2i76bpnb_iWZS5Vf86jA8WSyjMPFBdZ4Mg27KSK-MNq8DhGFYVh9yTaHuMY5ocKXuZ9HN6e2p2W5snuqrxBg8E8CAVzf0pTEJRT264KdtfIyB5JdGwICiH_wYBs2KIJ6ufNr3gLwgRJiJBEqlSkUKAEcOb207OmEabvYU7Xi4UmUSeqrdMaOQZues-kM-Q07wncIljmR6ayGHp4oDzoqQxIKSAGHbhTIWS3GCTrpWV_xLldD6D68huDTFgfOnbblPe7UyMe8SnvxBnbMlzfBcBbZphg3NBlkPB11Rpgqv8vtbrRV0PBhv66VOjsBf_qKgsYDyFvyq7cefuAiArZVq33xtiJuSv2cOXImXoyOKF-0a4E0n0_aeoHswiywY5P-733ZPoCzSeXo3nswo-DmAHSAp6fJOLeNqqL-ZkHsaG_7Z-yJDpbYf6vt4PGlTRfYkbomZ-uGO8jfpEHtUOUsV66uekv4FIxkFIhMHOkntDEMNtfBS-XNvDtFePsuaDOs3zJnIUIOc3sYfRxRFrcX5ska-nA_KTAU36AIoXQ8FB9b_P13q9jcrlxjVBQ_ixr0wATblFhgmp_OxGU_QXEjFLUo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=qe2JbucNn7TOD8ntNvh-_pqAdxt4Xn0Y_p1gaGeWL-61mx_racahqVc94StQbSbkJMmakFY2ertmcAQwBWr2i76bpnb_iWZS5Vf86jA8WSyjMPFBdZ4Mg27KSK-MNq8DhGFYVh9yTaHuMY5ocKXuZ9HN6e2p2W5snuqrxBg8E8CAVzf0pTEJRT264KdtfIyB5JdGwICiH_wYBs2KIJ6ufNr3gLwgRJiJBEqlSkUKAEcOb207OmEabvYU7Xi4UmUSeqrdMaOQZues-kM-Q07wncIljmR6ayGHp4oDzoqQxIKSAGHbhTIWS3GCTrpWV_xLldD6D68huDTFgfOnbblPe7UyMe8SnvxBnbMlzfBcBbZphg3NBlkPB11Rpgqv8vtbrRV0PBhv66VOjsBf_qKgsYDyFvyq7cefuAiArZVq33xtiJuSv2cOXImXoyOKF-0a4E0n0_aeoHswiywY5P-733ZPoCzSeXo3nswo-DmAHSAp6fJOLeNqqL-ZkHsaG_7Z-yJDpbYf6vt4PGlTRfYkbomZ-uGO8jfpEHtUOUsV66uekv4FIxkFIhMHOkntDEMNtfBS-XNvDtFePsuaDOs3zJnIUIOc3sYfRxRFrcX5ska-nA_KTAU36AIoXQ8FB9b_P13q9jcrlxjVBQ_ixr0wATblFhgmp_OxGU_QXEjFLUo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=TA8BgWx7N8KdOxmg2XGn9ji_tQv4hemRNosDwGnyesnyGJ1VqsXTTUML7Lp7aiTbcg_n553NT_GYUoD1LiEhM56PyrWH1yH9a6KiNRNlQqrFV_QyNejc0kc5nwAQvUve5TA7LGNrLrBNqT3MgHO111XSlH2DIe5x0tWmski4ppTB-K0Xih3qvCyrNdJ95hn9ybalMISv4Ds_54lXIgI81GIhsUP7pGLhdq2pxwLwzMJKJoRSm1mlICb3R8J5ZyxSGQ6UbgafdRpJztMIYHROHVj5kXiGP1d447IICAwAWxhgJjvUgUAs_JGFmKqPHD6RDqFHKehrFrHHMYdsSlB6aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=TA8BgWx7N8KdOxmg2XGn9ji_tQv4hemRNosDwGnyesnyGJ1VqsXTTUML7Lp7aiTbcg_n553NT_GYUoD1LiEhM56PyrWH1yH9a6KiNRNlQqrFV_QyNejc0kc5nwAQvUve5TA7LGNrLrBNqT3MgHO111XSlH2DIe5x0tWmski4ppTB-K0Xih3qvCyrNdJ95hn9ybalMISv4Ds_54lXIgI81GIhsUP7pGLhdq2pxwLwzMJKJoRSm1mlICb3R8J5ZyxSGQ6UbgafdRpJztMIYHROHVj5kXiGP1d447IICAwAWxhgJjvUgUAs_JGFmKqPHD6RDqFHKehrFrHHMYdsSlB6aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HlIzA69tv7-45uGSsYZJaqIQz8qObPxnzFXoexUPIozKmSa1tQrngguEjijnKLxja5kxGWVBIkcSemm63JdJuN-bSaSJjwTfmxV7pu6yXSXsngcDBxfIrV3Xw6Jf2yWqrfjjqRvYt87OXe3XVl0nSBtScZ-EulN99h4NbDrpG_ajEOZbj2GQAZp7k6lkXycEvzF6XtwyDxQLEU8gc2tg0toU8pREUnd5OcBCfGAY9b1EHj9Yep2WO3-d3iqzuEtu3xA2N1ty3pjNw8fxSmqjAnaf6hH9U1Xbw0MGQ5c21QhqWqRas4q7Hb6wi25GXlxwoy95dEPukiO51ZjpxtwpPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=GI1o203XhtJ67VcLp81QotayvMB7SZ724auVHcblGu7yfr8-WHPx2MEf2Y21t4Jc5zHUS1gCSX7afjJVUndZKv-dHqwCf09LMn_GOX3QKHiMEDjH5YyQ2ihT-5xDk8deZwf6ydDmRlC8RnWrbyS2yhmoGoNr6JW79ZrRQrUgHu2MH9CxBYtxqMOzmRXej7pUKsWyOfS_q_fK4aW2U2B3eqfLkEWGEqxOmcPES3Qt1-ZPOLphn21nDyuRtUZaxPQfCiCXOzwHVhL8tbRT93vSuR3J1vI37u8NAXh07vgAY5w4QjIAiMm_k-QNDoZM4-sNe9Q7e4wtxclwczY-xzcbQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=GI1o203XhtJ67VcLp81QotayvMB7SZ724auVHcblGu7yfr8-WHPx2MEf2Y21t4Jc5zHUS1gCSX7afjJVUndZKv-dHqwCf09LMn_GOX3QKHiMEDjH5YyQ2ihT-5xDk8deZwf6ydDmRlC8RnWrbyS2yhmoGoNr6JW79ZrRQrUgHu2MH9CxBYtxqMOzmRXej7pUKsWyOfS_q_fK4aW2U2B3eqfLkEWGEqxOmcPES3Qt1-ZPOLphn21nDyuRtUZaxPQfCiCXOzwHVhL8tbRT93vSuR3J1vI37u8NAXh07vgAY5w4QjIAiMm_k-QNDoZM4-sNe9Q7e4wtxclwczY-xzcbQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=AF763rh8mYofWy7h_K25bF00nrwIpdzwhGhKdiBPRtsMKQ7lUJZXl_zl-BSwLvukb_Ju9YCjSCdV9e0enbrzEPnus735ihyJ3XBuJgyQrgjDYtr3DViigqRthoE_WSeZGZEtBVrhlDD4zeNXD0-P8Qz6iikpyy9pEOViH2z8cqyIPG4kXVDv1elb7m7eAURIRTUlKUREeJ-_GhhzgWxoYWpDfTfMR5jfItiF7JMEUs7lg_jRej2NQ95zluoVuqACpdLlxkLb9v7IGhN7BHH0y9YwleTzKzfgVAf8qrQ1llLD3ERm__WoDNFVdj0bZti8yblx0EjFB114DYNGYsrzPp4FAZImIkh8ZhRodOgwXWmaxUzG9qHTx_RSd83sLqDBR6ZbtBjlOg4llwzSVioJE-Cb5-zS4KgPtFO-4tBdxlpCHZe9aqLrZH4kBQ7yWd2BpGdWLgyx5vYdRvBD00RZ8BHCEIuvIG1LV-b0DEqkh95jAhZu9zz8mkKuhbILTmk82KGgVUu5MUFFLKJwqGkpdYnyhuWkTYTFtPqpt2WfJNyEve__dcRE88_7vvJISUQnCWOA1SWIQ5A76GpDqdhEgYi6naQTt1lB2-Mf9oaY1sbeVKVr5Dd5SjyonjYEtgn7HH-e7GvGwQ0AUxJJyPbU934z-asxMr6NoJ7UMjZEg-0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=AF763rh8mYofWy7h_K25bF00nrwIpdzwhGhKdiBPRtsMKQ7lUJZXl_zl-BSwLvukb_Ju9YCjSCdV9e0enbrzEPnus735ihyJ3XBuJgyQrgjDYtr3DViigqRthoE_WSeZGZEtBVrhlDD4zeNXD0-P8Qz6iikpyy9pEOViH2z8cqyIPG4kXVDv1elb7m7eAURIRTUlKUREeJ-_GhhzgWxoYWpDfTfMR5jfItiF7JMEUs7lg_jRej2NQ95zluoVuqACpdLlxkLb9v7IGhN7BHH0y9YwleTzKzfgVAf8qrQ1llLD3ERm__WoDNFVdj0bZti8yblx0EjFB114DYNGYsrzPp4FAZImIkh8ZhRodOgwXWmaxUzG9qHTx_RSd83sLqDBR6ZbtBjlOg4llwzSVioJE-Cb5-zS4KgPtFO-4tBdxlpCHZe9aqLrZH4kBQ7yWd2BpGdWLgyx5vYdRvBD00RZ8BHCEIuvIG1LV-b0DEqkh95jAhZu9zz8mkKuhbILTmk82KGgVUu5MUFFLKJwqGkpdYnyhuWkTYTFtPqpt2WfJNyEve__dcRE88_7vvJISUQnCWOA1SWIQ5A76GpDqdhEgYi6naQTt1lB2-Mf9oaY1sbeVKVr5Dd5SjyonjYEtgn7HH-e7GvGwQ0AUxJJyPbU934z-asxMr6NoJ7UMjZEg-0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JdRHhgN8L4TRdeEnnD6FMxp5dmk063FZ5sHIIIL9XNRkK3btBiVnk2ESa8vWbbIk4p_z2DWXYbB_7bzgCcwnRt7LSu6TRJpleXfeBPyx2GB_nT9HR5XyLJ2jPk_zZ8V8Cpl5adKt0lSdIXuEX63hJQfxKGgWsenypldtBNvPbnH7oDJAC8l6W5LlX49_pQEWZw8QoEiLMuKWcDZ8V88tcCN5P1tpBRAuNPX-T0W_W5sHHSfBcYNPBkI4Xcj4ZzpH64oUrhlsYxTAE2xfEUnmxgvM0dTGfx64X5ZH7AQibESf1MlniRb5F3xgpOnCFqLwerX4xDAQk7aOFScizLT5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=G7hjYT-yfWr9OUt0mK9uEY3b0QlJZRx5sJ48aIUllf0ZmHiL69nKjgSLhKZkJfjQN7ik47vuW_U2q0mgmBgsH-nVXDUPM1E-BX-GYkh3QL5UTNRo-NxPxNz1IMpddQNUedFH8AQAeAHYQ2YGEXtCUChL4kwzE7w4gLIX89jEjFQCLf2dfvgCw9YJfRTIR7Md8di4Ns5Z585v73idnV1iOn5-lsZo5_B-ZckJNVXqnT_8EL1seWuS_MWwqpFL4Wk6Sk9zJcQV35JQUX8kVSLbhzKpbbgkMOkqYrVapLM37SrXNysg-MWykNFZaeWSXnJV6rVdwPIP3N-GinM0-XkgTbuXkzrjhEhMBSGxXTqJz_VT9CjI-EsELM-rmcVV938ZZ7j17EpiuUk3s_pQafJ_GjEr8IZtldKylPw-FxtPa9yh6dTFo9B2QLCd32Kei4dfNxz4WNsZ0O-k8dqpP4kKfqbGGcSPYOBTHVzRTXzV-hTTBUz37YqhjHQucKjLIujbG5-A2i939pFlXCLm68GgE875fQfji-yZVA-ld8to4npksQbva07Vq4OBSptDtbBB-3wAKKUglhmKlLtkhl5VT80ulbqeyUPm8wP-1HJR33loeA-X4Oi8n7aPEV7NakYHJzYMXKxIRnLv0HsiEKnZd_30oZQyxAC6HYpb4IsvZD0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=G7hjYT-yfWr9OUt0mK9uEY3b0QlJZRx5sJ48aIUllf0ZmHiL69nKjgSLhKZkJfjQN7ik47vuW_U2q0mgmBgsH-nVXDUPM1E-BX-GYkh3QL5UTNRo-NxPxNz1IMpddQNUedFH8AQAeAHYQ2YGEXtCUChL4kwzE7w4gLIX89jEjFQCLf2dfvgCw9YJfRTIR7Md8di4Ns5Z585v73idnV1iOn5-lsZo5_B-ZckJNVXqnT_8EL1seWuS_MWwqpFL4Wk6Sk9zJcQV35JQUX8kVSLbhzKpbbgkMOkqYrVapLM37SrXNysg-MWykNFZaeWSXnJV6rVdwPIP3N-GinM0-XkgTbuXkzrjhEhMBSGxXTqJz_VT9CjI-EsELM-rmcVV938ZZ7j17EpiuUk3s_pQafJ_GjEr8IZtldKylPw-FxtPa9yh6dTFo9B2QLCd32Kei4dfNxz4WNsZ0O-k8dqpP4kKfqbGGcSPYOBTHVzRTXzV-hTTBUz37YqhjHQucKjLIujbG5-A2i939pFlXCLm68GgE875fQfji-yZVA-ld8to4npksQbva07Vq4OBSptDtbBB-3wAKKUglhmKlLtkhl5VT80ulbqeyUPm8wP-1HJR33loeA-X4Oi8n7aPEV7NakYHJzYMXKxIRnLv0HsiEKnZd_30oZQyxAC6HYpb4IsvZD0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=H2ssdk-QOAMD8uK4FGFkAHDktyR0-_x_jMUymQaeG1-fszlhdl7Sl_yQ_X6JhjE97opagpJaa_snrcIcW4zvM8NcTaPMZLHiL8nF6VZuyyeVl3NyXdxXUF62TqeFEalmur9j3RZeAA2gRKZx8ZUiEVmi25FiU-znHZs-uyWb-VqdJ831p3c3vaVN9ATP5tsoiUmrsLgzW-Zw68EZvHirpGIofejchbkLg4M7YVrmv_ToGMMwS23fyuiz5NgTFb-b6HdAYyJCeD1X6igtl78wjJmgzNCrMf-hrH0b69WnvjoRw9VCxEWHC5PHpXwI1FaSCKcqvj5Xt70Mkiudi7gCrnL7aOQ-HwaYh5uDbqz6v7Izsqxut9oG7tk4M4MDvL_sl3dcs-xtFBnBZVBX-XRSMBF5HSlUnLKHdvj4q4Fg59MamCW2zn86R7nrVVoVBAf3Nzv7milUDLOv6Yp5GjX-WQ6F55dk4L2azaA0jiN6JKf5uKmcccLgBL87_UgqzSHgAsSRFUikueTWxlevEFh4atkfb3YlrOMGjJ6F6oUdhn-6VghFaGdiYQf_tBX0CrDfXUME9TNf4DJgfRlSvfhzWdcVrL9Ip6K2bu4aa_SoyH-MJyd8Yvpe-a5X-42LnNMQiWSJEHlQDbGzwwocEG1y5uS2X3g3lPASgXKozhfidL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=H2ssdk-QOAMD8uK4FGFkAHDktyR0-_x_jMUymQaeG1-fszlhdl7Sl_yQ_X6JhjE97opagpJaa_snrcIcW4zvM8NcTaPMZLHiL8nF6VZuyyeVl3NyXdxXUF62TqeFEalmur9j3RZeAA2gRKZx8ZUiEVmi25FiU-znHZs-uyWb-VqdJ831p3c3vaVN9ATP5tsoiUmrsLgzW-Zw68EZvHirpGIofejchbkLg4M7YVrmv_ToGMMwS23fyuiz5NgTFb-b6HdAYyJCeD1X6igtl78wjJmgzNCrMf-hrH0b69WnvjoRw9VCxEWHC5PHpXwI1FaSCKcqvj5Xt70Mkiudi7gCrnL7aOQ-HwaYh5uDbqz6v7Izsqxut9oG7tk4M4MDvL_sl3dcs-xtFBnBZVBX-XRSMBF5HSlUnLKHdvj4q4Fg59MamCW2zn86R7nrVVoVBAf3Nzv7milUDLOv6Yp5GjX-WQ6F55dk4L2azaA0jiN6JKf5uKmcccLgBL87_UgqzSHgAsSRFUikueTWxlevEFh4atkfb3YlrOMGjJ6F6oUdhn-6VghFaGdiYQf_tBX0CrDfXUME9TNf4DJgfRlSvfhzWdcVrL9Ip6K2bu4aa_SoyH-MJyd8Yvpe-a5X-42LnNMQiWSJEHlQDbGzwwocEG1y5uS2X3g3lPASgXKozhfidL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=DnvJp1Z2ZXjrDUXCgj9EFjtQLxozIe2jgBt-WqHNowRFBXhy6MrFtocINErzkCtQ0QT6yfoddhngbKJk2DSJx_SsWJ0IDdTSuGLFR1o-bgvYpWWizgwb2KvcYfCjF6sMh5YYlhxKe5bhLEj1PXvMb9xPDHQiYh9vY0zYH3hWhavDpI5qMOGKGDKK9brBLfjRQywW3BvF6f4cuSYGXChYkM8q4McgYpQdVQnOJQuFgMWiHigsITb86bO745uV1nN2E2SlDvIe7E9E-COmrBVJOPyNeKYGECnms0fPk-PrwVlW2VD19_h-zVMWDuH7Y9DUSXbtPIF1iNPaLeY4eOYYlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=DnvJp1Z2ZXjrDUXCgj9EFjtQLxozIe2jgBt-WqHNowRFBXhy6MrFtocINErzkCtQ0QT6yfoddhngbKJk2DSJx_SsWJ0IDdTSuGLFR1o-bgvYpWWizgwb2KvcYfCjF6sMh5YYlhxKe5bhLEj1PXvMb9xPDHQiYh9vY0zYH3hWhavDpI5qMOGKGDKK9brBLfjRQywW3BvF6f4cuSYGXChYkM8q4McgYpQdVQnOJQuFgMWiHigsITb86bO745uV1nN2E2SlDvIe7E9E-COmrBVJOPyNeKYGECnms0fPk-PrwVlW2VD19_h-zVMWDuH7Y9DUSXbtPIF1iNPaLeY4eOYYlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=VsEinE4sqa3NAiHCuutt9piSAcWY3UQP7s44pWrv8VBIGj8ROoYg9tGdjbJ9eeGWerEJxR4Hq1MVtt5eKc_5PaV2EnwAhHQ1htbe0dQW2skSp-4NFu8jnGlXp8-4-KZoSGQvYPZ05Pm-i8nlszRTHh40DuDsr8IE7GBzekEU9wn9uUjUKIS034XaOlFB2Geq1WkvgYtOUnrVFNGVuFtYNATM7ZMoKFe7M0R8DARw9GUGgSrf9PMr5r2A4e2v4CTudTCf6MgxtXq7knOzv0TWCUvzHH0QyPNhkNvebVeNkAm24xMD0lpngK4SoRfx7Nlu7Y4bHGlx-gTJaBpwjNSFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=VsEinE4sqa3NAiHCuutt9piSAcWY3UQP7s44pWrv8VBIGj8ROoYg9tGdjbJ9eeGWerEJxR4Hq1MVtt5eKc_5PaV2EnwAhHQ1htbe0dQW2skSp-4NFu8jnGlXp8-4-KZoSGQvYPZ05Pm-i8nlszRTHh40DuDsr8IE7GBzekEU9wn9uUjUKIS034XaOlFB2Geq1WkvgYtOUnrVFNGVuFtYNATM7ZMoKFe7M0R8DARw9GUGgSrf9PMr5r2A4e2v4CTudTCf6MgxtXq7knOzv0TWCUvzHH0QyPNhkNvebVeNkAm24xMD0lpngK4SoRfx7Nlu7Y4bHGlx-gTJaBpwjNSFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=eY_7xkFj4RO05ZIi8Zt6xiYm8zP2EO9X_qFdCbUh5nN_8-ZoDU0CHHdoDX4_ySJKv6ZSuJkrR8yCHvhi_zfutvBXKnuXwdVazGVoPh1WVfA3y8KJBhv0cx14oWgSGC4lXAmxbo4lGXesrXcT34OONYrUCUk0KNzNKo-hk_nmJfHY3utI4964IhLw3v-YpJtbnbIOfn1SL84EEKL8-Y3V6Z5LEq5D4ZDlsOYZGGKXahml3B9GI4yufM3A_4Kd2F4cGGswgYXeDKpBrjSDQQNSqlB1m9RQ54gilVHOK6R-H-ivhKIFKNdL7Car4wpJpN3FZaDW52L-fL0Zrfms4NdO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=eY_7xkFj4RO05ZIi8Zt6xiYm8zP2EO9X_qFdCbUh5nN_8-ZoDU0CHHdoDX4_ySJKv6ZSuJkrR8yCHvhi_zfutvBXKnuXwdVazGVoPh1WVfA3y8KJBhv0cx14oWgSGC4lXAmxbo4lGXesrXcT34OONYrUCUk0KNzNKo-hk_nmJfHY3utI4964IhLw3v-YpJtbnbIOfn1SL84EEKL8-Y3V6Z5LEq5D4ZDlsOYZGGKXahml3B9GI4yufM3A_4Kd2F4cGGswgYXeDKpBrjSDQQNSqlB1m9RQ54gilVHOK6R-H-ivhKIFKNdL7Car4wpJpN3FZaDW52L-fL0Zrfms4NdO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=l6wOvtbGhekpw383kMG1MFEyKqojTbW22e49ED72iOkRRi1FQUVR3tEwzkh_2W0TS5Rhz1IQ5sK9EimRAHbGSjgwWLNgWVt0AOH4KGkScE4tBvuWuSKxRyH5U70ZVTHHHw5wIrGDkcjIrlyh7z1n5JbVhOT-LoRZp6QfIktVDX0foWkRFw2OtW_NvPx9wiUiUrTLNN1RqnT3wVsynvfWQDC3batvgKlw1xlwRfMcun0pIJM1mTrwvdxTXcCEZe7wmQca4ySgu6Oix2zcmdPIfnOaY2bZ0420Sj3iRYFbozwjrZKuKvnYhe6oA7RBMpqcnx7lG-NHxXX3MkyRZKXuyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=l6wOvtbGhekpw383kMG1MFEyKqojTbW22e49ED72iOkRRi1FQUVR3tEwzkh_2W0TS5Rhz1IQ5sK9EimRAHbGSjgwWLNgWVt0AOH4KGkScE4tBvuWuSKxRyH5U70ZVTHHHw5wIrGDkcjIrlyh7z1n5JbVhOT-LoRZp6QfIktVDX0foWkRFw2OtW_NvPx9wiUiUrTLNN1RqnT3wVsynvfWQDC3batvgKlw1xlwRfMcun0pIJM1mTrwvdxTXcCEZe7wmQca4ySgu6Oix2zcmdPIfnOaY2bZ0420Sj3iRYFbozwjrZKuKvnYhe6oA7RBMpqcnx7lG-NHxXX3MkyRZKXuyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=inj96iReQQ9AOZbe6wk78CSuurkgdcSid0V81EggQp4rpZQEstK4Sr8sTHsCzqN-kFY51XMqmmeD7yY6iQHsk4A02iy7tPZDeeh7gQh-YQKHxAa_OrybCkCr9jsSd9WzGEN3VHdg5Wr0L54M1yw6zSE_NTPdBac2tnxfZmyNiwyqHvu-joPPjswSYiah1BamYS7BY_BwydOlCyb7s0lMamSxT3nq4Lj4qLTRFKRC7A4wnLZbpKdWFaQPlVvQ5euBmCyI4r670CV_HAFn__GP_UR2qHo65uZMxI3lpVORSiwJGGHFNLAr_ixfwNFev5m0fCobCwXm2GQ1ouv-1ETKVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=inj96iReQQ9AOZbe6wk78CSuurkgdcSid0V81EggQp4rpZQEstK4Sr8sTHsCzqN-kFY51XMqmmeD7yY6iQHsk4A02iy7tPZDeeh7gQh-YQKHxAa_OrybCkCr9jsSd9WzGEN3VHdg5Wr0L54M1yw6zSE_NTPdBac2tnxfZmyNiwyqHvu-joPPjswSYiah1BamYS7BY_BwydOlCyb7s0lMamSxT3nq4Lj4qLTRFKRC7A4wnLZbpKdWFaQPlVvQ5euBmCyI4r670CV_HAFn__GP_UR2qHo65uZMxI3lpVORSiwJGGHFNLAr_ixfwNFev5m0fCobCwXm2GQ1ouv-1ETKVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GilyESAnS_8XVVnC1Ta2fNwGMJuobEhwtjdZTNdT6iFIZF8I_FlQTY6D0DMESytp78bcLFjIJnyp1XCdKyVcJT3RIHVG4Xapb8YFEifR3JccdEZ3qHnTxQG22colTigHGYn8VYiwEo8wJuHHEJ0CplKs_DiuSiuN0t5SmQYHUORyoeVKw37cHrbhjqjmu5FCklPgshNyKvKHaxZIuDU8259V5ccjB2jgU1Qc6AHSoL9Y7tcZwbTV_OUgF9FUvbpshLl1XBPfTM5ds1qXKTZhPTjVBvBrKxR6ZfJLzxvh_laJxY8mnYHXXX7m9tvQ1y-zp0Cih3WYv7PGFTtQlCA4Og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GilyESAnS_8XVVnC1Ta2fNwGMJuobEhwtjdZTNdT6iFIZF8I_FlQTY6D0DMESytp78bcLFjIJnyp1XCdKyVcJT3RIHVG4Xapb8YFEifR3JccdEZ3qHnTxQG22colTigHGYn8VYiwEo8wJuHHEJ0CplKs_DiuSiuN0t5SmQYHUORyoeVKw37cHrbhjqjmu5FCklPgshNyKvKHaxZIuDU8259V5ccjB2jgU1Qc6AHSoL9Y7tcZwbTV_OUgF9FUvbpshLl1XBPfTM5ds1qXKTZhPTjVBvBrKxR6ZfJLzxvh_laJxY8mnYHXXX7m9tvQ1y-zp0Cih3WYv7PGFTtQlCA4Og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=VbSuDy8d7IOHXnpduP-CbGidU-2VtdvfFsKsGWPzSvqZvy_FFyUh2Gtjp_DyDEoodggVPivSxBcoW2toHzIdoIGgkITRD3U8-ifUu-Gj_ezwRGj3OYLmy4vGALCC0KeRpWg5xUvMjruzbEbu-1YCdAFFmjQtawJajph6lgXXo6JKSxbvO_XAxLklg9c7pDkS81zrTd5sLyHPEARi18SAEv7xwydcwU95iI-XB-KwBqG4_Mhb9lCotW5nCKMHleM4AI91_seRYOIC1jRYdo2cUUgYG8z7WtAlBy5y2XlwIjOe7_pemniQ_DHGgj-2shk9lveGjljJiV9sAIIMlXdqcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=VbSuDy8d7IOHXnpduP-CbGidU-2VtdvfFsKsGWPzSvqZvy_FFyUh2Gtjp_DyDEoodggVPivSxBcoW2toHzIdoIGgkITRD3U8-ifUu-Gj_ezwRGj3OYLmy4vGALCC0KeRpWg5xUvMjruzbEbu-1YCdAFFmjQtawJajph6lgXXo6JKSxbvO_XAxLklg9c7pDkS81zrTd5sLyHPEARi18SAEv7xwydcwU95iI-XB-KwBqG4_Mhb9lCotW5nCKMHleM4AI91_seRYOIC1jRYdo2cUUgYG8z7WtAlBy5y2XlwIjOe7_pemniQ_DHGgj-2shk9lveGjljJiV9sAIIMlXdqcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OS8XL9Xg9bgZgaBK3ulvvWlJAG3kxLox95ZNdw5ggQnpglaveZZndZLNGinAEZqXW75J8DlqIFrBtXRaYXE3ECBa3335PzxxiVxNtzqASMfPdLt3m0lhLSXOqsCfzzpvZcSkf_wJFDZOsod75lhMMA6v5kSbo2zjevOLQ95wczwinKxeW4QHVPB2YoZ8tDxEuc7iyPvKJtfVLWstiLf6F5hJAfKboHixtYJfrhc4RgEd6F-eIcveRptbz1XWoZcyBq4weMbObXf5EEmYIMP1T93T4lnKFs5C2Q2wZOltA7xEIY2-nDQhopWmAFrpoTwWZTF_PUZltODNeZORsoqnMQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Y1y5dn0JVSaEAZODaNalGG85dxw2LwAfpO7citUmtbZt8jyxAZ3f3ymiwJN5KoXKhL6fV1R3mmCNTyoNtgNZhlcQ4dejlPwvFo3CP2VjjOXvV-rvZFvQyzYZy93PsMbArgH4TCfYExrerSbWbsni08OArhp62KBl31H7BXVELGxh4h_ziekx2kmb5r1Od51m4bSky5vNIX9kx3H9p6IJ0yGCTj8TX38kp1eYaORph6NelnyD7LdOZmcwNMOXVDeXzUb-eZW7bgNcX5-Bexe_-NajtlGw9umbtsJxzzUUkrBXqOmWRe_ke8E3PE4vpEI2iTct4ZumRcAOcoIa638kcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=Y1y5dn0JVSaEAZODaNalGG85dxw2LwAfpO7citUmtbZt8jyxAZ3f3ymiwJN5KoXKhL6fV1R3mmCNTyoNtgNZhlcQ4dejlPwvFo3CP2VjjOXvV-rvZFvQyzYZy93PsMbArgH4TCfYExrerSbWbsni08OArhp62KBl31H7BXVELGxh4h_ziekx2kmb5r1Od51m4bSky5vNIX9kx3H9p6IJ0yGCTj8TX38kp1eYaORph6NelnyD7LdOZmcwNMOXVDeXzUb-eZW7bgNcX5-Bexe_-NajtlGw9umbtsJxzzUUkrBXqOmWRe_ke8E3PE4vpEI2iTct4ZumRcAOcoIa638kcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=bELvXw8D1gLNRDW2blnQSvv480cA2NdFKHAVe3JPZ1qPMVlB2h3fvrWxpCjff4ic1uGHlX7rqiy13nm9TelW2vLsphZGkSLOCdeiBAN1EvfQ0xhjJBW9hDqu-L7VYMpn08RXZUGxd5PLKXhej6gEz05nemijl_w96GsidQgdVJW1eOf2WmwOqn2UO8BXmtYftC9LIPd43WfI3iGLJAutvZsWtAxCQ1cGdkWXrWzXJxaRjwV2ty7nuT04hH8iTtySZHs54fox07GJVR49QinxJAhWdCF63jAK-xgWSY6Oqwmv1aiHFh_rbnXNE6rZrEwqyL2pR98-LOHL5ccg88m1nA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=bELvXw8D1gLNRDW2blnQSvv480cA2NdFKHAVe3JPZ1qPMVlB2h3fvrWxpCjff4ic1uGHlX7rqiy13nm9TelW2vLsphZGkSLOCdeiBAN1EvfQ0xhjJBW9hDqu-L7VYMpn08RXZUGxd5PLKXhej6gEz05nemijl_w96GsidQgdVJW1eOf2WmwOqn2UO8BXmtYftC9LIPd43WfI3iGLJAutvZsWtAxCQ1cGdkWXrWzXJxaRjwV2ty7nuT04hH8iTtySZHs54fox07GJVR49QinxJAhWdCF63jAK-xgWSY6Oqwmv1aiHFh_rbnXNE6rZrEwqyL2pR98-LOHL5ccg88m1nA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=r_gg65orT5wz2ZKbOwzEOuU8G5yl_UUd8aKu1FTocJv3SP-xv-nB-tSZrKcdZ5-U9Zdo68cD6MMi64DzqK9KOrslX86OKjTnk7WRpPo8wzWXOajFzdfW-A1E69iFOmKXIRZFnOgP6Gs3PJQO-pTC-vX8UaCYK_0p3uuPynpxoQfYisPAOtA-jmvYW99SPni4bxh-cTroVnNqzQHYk4f7QuwVozownBMjfvRwy_lUO4DXSVCSTmzPoiNgXNDf8l_xKG2iPjAjyj1HUx5JvyCmVmMs2oMeHWflWPd4JZ16SKHMFDjMdcA28ME69Sq8rh5myutlopJY4GBndyYDQHaSOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=r_gg65orT5wz2ZKbOwzEOuU8G5yl_UUd8aKu1FTocJv3SP-xv-nB-tSZrKcdZ5-U9Zdo68cD6MMi64DzqK9KOrslX86OKjTnk7WRpPo8wzWXOajFzdfW-A1E69iFOmKXIRZFnOgP6Gs3PJQO-pTC-vX8UaCYK_0p3uuPynpxoQfYisPAOtA-jmvYW99SPni4bxh-cTroVnNqzQHYk4f7QuwVozownBMjfvRwy_lUO4DXSVCSTmzPoiNgXNDf8l_xKG2iPjAjyj1HUx5JvyCmVmMs2oMeHWflWPd4JZ16SKHMFDjMdcA28ME69Sq8rh5myutlopJY4GBndyYDQHaSOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=b1bMdETA7xyi9z7LUE0A-mThKjAJewBgHpXQzW4z1Ux6duPs6yQ_AJ3G2Zj7Q9EFYAiq8QiPG7fg1OERhbzf9pSBSO0o7IFkz-jLM3W-8G68397CKfvQ39kabqIHwbN_zPE3nQUYFeaoFF8UJ_anU8aj2yDmlYmZfqu4rCckjQ1PTA7Cr2npYLlTAo-oS6YeQpO2oyPDSUQQ5nGAnNydlJft47Jtl2Z91aVQG9kaWlofCc8y27gS_YD0RP0D-e7GwxNONr3rrYQ2tVTqhezpZ4AoBQdVAjEDqpCATpToT5_ESJ-JDP9ep27xkU4l3vFEeS8iOYalkYu3dw2GHasCiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=b1bMdETA7xyi9z7LUE0A-mThKjAJewBgHpXQzW4z1Ux6duPs6yQ_AJ3G2Zj7Q9EFYAiq8QiPG7fg1OERhbzf9pSBSO0o7IFkz-jLM3W-8G68397CKfvQ39kabqIHwbN_zPE3nQUYFeaoFF8UJ_anU8aj2yDmlYmZfqu4rCckjQ1PTA7Cr2npYLlTAo-oS6YeQpO2oyPDSUQQ5nGAnNydlJft47Jtl2Z91aVQG9kaWlofCc8y27gS_YD0RP0D-e7GwxNONr3rrYQ2tVTqhezpZ4AoBQdVAjEDqpCATpToT5_ESJ-JDP9ep27xkU4l3vFEeS8iOYalkYu3dw2GHasCiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YT_rcrz7GbNZKMjAQdIvpAszAMFAh6Gh3sqHYOUXbxbFkCd8niYBKh4KPe_1nrQielEsXmdKIHppZ15WpfwkQW3DpZNk4u8MXk9jAOxWBTqmNIfYNAbKelzvkU4QRhVX1LVHw1AW0QogJWr8z7WlKPMwwekHbYXayh6r4rtj_k-cO9b5qojTqrcfTSJ_4ouNNunJg56Zmx8HmcHK5Az87TkDse8CazY7h5LgPNtqpzo2UIPqEPFsA6y0WX6XxeW02CnvFeoHLk0qIMcVFza29nKnIeJwGKn8PXDikOmMo7n-mE_m4Ow3_x5kqtLIjZngrCJ58ch9qoeb8smq3fFIrA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=jcq4QtZszFEKoaOtHMN_VW4Coiv1-YBNBcCIV1lEjNq4iB7lDBFaBZ26a8KjnjEZMB7oIonvRNBtCclom5cOeMN7-IF3OEYdJW2YWpzapHc0bSyAadx1ocSndjDdmw7KGRaGwnao3HwvbWXk4_WSWSq9AddTPi3kPimzkFPQFTdbHQV6adBss1yThclmws3pwh7Q7ojzwRih_yO8Yu2zjNwvhDzXCnHNZhtajkx3w05gtyVywliJnE7uTCj7Lv5cCDVP0_PgoV2HXYChobseYPZun0KXHn_GL2P4R59qWyBsjvOV8FE57JINjuN76YajpS4IhpEeOg1_5vkSoicFzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=jcq4QtZszFEKoaOtHMN_VW4Coiv1-YBNBcCIV1lEjNq4iB7lDBFaBZ26a8KjnjEZMB7oIonvRNBtCclom5cOeMN7-IF3OEYdJW2YWpzapHc0bSyAadx1ocSndjDdmw7KGRaGwnao3HwvbWXk4_WSWSq9AddTPi3kPimzkFPQFTdbHQV6adBss1yThclmws3pwh7Q7ojzwRih_yO8Yu2zjNwvhDzXCnHNZhtajkx3w05gtyVywliJnE7uTCj7Lv5cCDVP0_PgoV2HXYChobseYPZun0KXHn_GL2P4R59qWyBsjvOV8FE57JINjuN76YajpS4IhpEeOg1_5vkSoicFzDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=vNW4gqy78e3Jzpe7rRfvsRyubAB_PsD3iUY8YqbUhqXkUHC2YFoalrx_FGWYnK6M5I7ZQhRHJPL1e_mcf3OJ8Bc-Os3BmFAufo2xDiCAVQAfxl38UBscdCyyzCSZEVvWOZcB92cjAk4BrsJSdJ2kamu78ule2WBRyBMEUfh-YlrTeUqmYsLPmAbJq6Xh2jn39_vsmCfT_wyavX4xXcpl2nowNnK4YKKwyIxVgO2L_y_C5U7LqIOmnOrc2CIoLjZOjLYGW_UN9SSJ7Ga6_6mbxs_1l8KMP9McMYsNP3ndmfMQ4Z66HJKZ7b1Wv4pySdKdEncX3P9Q_p9kpEQpMHzR-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=vNW4gqy78e3Jzpe7rRfvsRyubAB_PsD3iUY8YqbUhqXkUHC2YFoalrx_FGWYnK6M5I7ZQhRHJPL1e_mcf3OJ8Bc-Os3BmFAufo2xDiCAVQAfxl38UBscdCyyzCSZEVvWOZcB92cjAk4BrsJSdJ2kamu78ule2WBRyBMEUfh-YlrTeUqmYsLPmAbJq6Xh2jn39_vsmCfT_wyavX4xXcpl2nowNnK4YKKwyIxVgO2L_y_C5U7LqIOmnOrc2CIoLjZOjLYGW_UN9SSJ7Ga6_6mbxs_1l8KMP9McMYsNP3ndmfMQ4Z66HJKZ7b1Wv4pySdKdEncX3P9Q_p9kpEQpMHzR-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tbeDNEvWR18lvignYY2TU7Iccf6HzpMfn6dfNQJxJTYoqDhiUp1zUWrdTrgBAsOZ__-r_MQrMqImGCrPt9Zk6qe3Jo9QuHSvT91yEmG6jgQDJwJWs3XkKMQuHmIUiE_qOJxMyLihbxPEIxdyAU02yGvYR2PfFNOuTve_YibpDUb7A5NrHmpFiBOiXLOzKcKGNrd3uJuxA4-dnPTKcdaDx2FtbKvbIJgf95nqC44hxhpEsqdMu6_E0bhdO75biZniscxzFQrAwO9lSzxQyhproDV_-r0orB7RANFeMwWEMHSY8VelvOlA21J5q4RUz1VycpkPDLr-a20OmaabTTbiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vmJCSPmDX99t-ak-h_O4TlFf5F45zyqseC8_qprYYJsJrkMiQgyL05lXhfyeQD8TVz4gUEdXuA6mqkJnfYwQJHjIBg0bnsI2rk8dEvceh56qc_XM7sYRY5ki_HKjL9Pfp_2Qp9CwIZYR2ei9kHxvLPDue-vYsTQ90UjaeG2vheDMLlPl_460Yn8NzhH76jbkJaOUzdwwdxL3OLkgb4cXXuOLCAVW9QBiNXfZF-9c_bef4TP1UEJ1R0CKy_FxxWw8YwtJQYv6iy1qKba6UFG0AE5c9-JGrnr-HX_b4dQu7fgUglCSZoBJmiIN8BJlK7mE__zSP6YUXr99wpUd4W6JIg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=cppL-16_z3uIZmwA2eouW86ArgPYnWfCbUt_jZeSsKAX6KOj4erIcf9MB0tM2nrwmF7N7N3w6GoMzD-oB_EjJsTRhKnbcKxKR00CcJoLsIF_Rz3fX-dKVDmI0X3slW6xEvSd1BeeHrGk1ENWeVG3CEwVfEPT752wXeBwoJ4ldzfpbAoUwyU665VY4w1IjxbEIc501W2JVj2hSNkHxkJMguz4IU-EsraNSwjh8ChVof4ZdwIQQRXFkBjjqLIH7fhxTak90WjtIudPYNLN78Nna3t3Q1D1wI_7Odz3NT0DTnKPows48jRVoMZrZQiIm5339sRy0IqWQ1wp2qQVoSVF2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=cppL-16_z3uIZmwA2eouW86ArgPYnWfCbUt_jZeSsKAX6KOj4erIcf9MB0tM2nrwmF7N7N3w6GoMzD-oB_EjJsTRhKnbcKxKR00CcJoLsIF_Rz3fX-dKVDmI0X3slW6xEvSd1BeeHrGk1ENWeVG3CEwVfEPT752wXeBwoJ4ldzfpbAoUwyU665VY4w1IjxbEIc501W2JVj2hSNkHxkJMguz4IU-EsraNSwjh8ChVof4ZdwIQQRXFkBjjqLIH7fhxTak90WjtIudPYNLN78Nna3t3Q1D1wI_7Odz3NT0DTnKPows48jRVoMZrZQiIm5339sRy0IqWQ1wp2qQVoSVF2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
