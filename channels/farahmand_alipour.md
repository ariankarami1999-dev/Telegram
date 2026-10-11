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
<img src="https://cdn4.telesco.pe/file/eVw7Ido8aogrHNgn8Av5g1WwFbg4MUAtsWcUsdFWfoDvvfKmm1SE20uPVp_x4Hb73CBJ3QeZ9lugl4_ryMySa2zC2Y1VXxq8yIqRS6xJbE91gE_RC366k8ChW0HdcN0MBd8MwabV4Dfl1CalJaaTJYkhDfCrnOKLv_iAgHQVQYhEwUBRRbLNT3CaqZu8FFTcWIbPCM-pyP8AlnlAzViC7FryDU2Dy9fCUcYbMBzk0JihOUCKxCb8mbazWQU3rhkY1cKpYCvXsRUU-wzGEiEyOfIgFR_ueUU-ZCNYHlCaRcZf8kWFoC4w352MbsXfzMwRjNBt5SxXoqPNAK_3VRB3YA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-6804">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=WNQJI3kcMcaBf8kWJ8WanvTMuowjVvLMpCOmiCzVmnZhqtl61eKgs0y4EzM3JcH_E8J_Qmd4EhBGoZfjSLPUwep-MNsWJ0oWM-kGRecl6cV6kZ7RdAaMldKPVHdYQga1hBDKc_VRuZDNxm7UNfvUAFDn-7Cd3eOBV1NlIBeg3qrvrYS9lT-2IxdPdEq_X74Kmq1M2X6Vv7EOkkka1_w4ihGmjjwhiAm11RN77SxY50OggI8Tb1p8R039JtmNU54rU_Ddi8hqg_0WiU-Vu40NwuKyXS3c20XZa2UQrskZBOru3vjrsB6LC6ydE8LV1TF5RrgAAxZDYccgA4sP2djKpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=WNQJI3kcMcaBf8kWJ8WanvTMuowjVvLMpCOmiCzVmnZhqtl61eKgs0y4EzM3JcH_E8J_Qmd4EhBGoZfjSLPUwep-MNsWJ0oWM-kGRecl6cV6kZ7RdAaMldKPVHdYQga1hBDKc_VRuZDNxm7UNfvUAFDn-7Cd3eOBV1NlIBeg3qrvrYS9lT-2IxdPdEq_X74Kmq1M2X6Vv7EOkkka1_w4ihGmjjwhiAm11RN77SxY50OggI8Tb1p8R039JtmNU54rU_Ddi8hqg_0WiU-Vu40NwuKyXS3c20XZa2UQrskZBOru3vjrsB6LC6ydE8LV1TF5RrgAAxZDYccgA4sP2djKpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUzlKjZUcbYA4IzdPxIuqKtpY7J0OoehndKL3r7HbJ9OtUWmS6GOVEyZOkjyH2xFjP2vwd6ziUunNT8C4yuwZKr0x-L67w7VniZXRGw7aMeZaccsqh18IJo2ouWDUGnRa51ffJRWXJjdXuZxua4p-ZnPZGIVk5Z-e9NwJHB9UX4p8Od3ZQaPyG2EKAqd4WsxHZwzarbDgXqBMTcmhgiI2JhnERIXVj5m33gIplTkDHtZtYcWBLqcAHDH8kW4tGwPU6lTtw1ejIpL7N-PRtJLkYu-fh3bQ5ueBHTFueQEg2h9f-PAnxxz4z44YScM2Ti6ul0Q9FVj-ahyREm-r8tHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OyDDm3alipq_ITj7Br5iPhhHc1w5OHimhif2xx6rrY4P3ZAOcj45YGjpVfq2Ek94D9pDhufcrOIGy_xSKdBjxU2IZNgv91q5pK5QSeb7M4JQ0jC1ou7acQydndEdTJKB5d4PtfwQQJkE_4AZHGC8y6nIPtQt5Ijh-MQ-IibukN4HrnC0iXlQRM_BCJcfKzQqRxOPTRTgxC30kd_lPTBeheU_J7rV-IK3itvilQUsTlwq7BEuURjQkKmfMB7zLI1biUQK18DgEYp0IuKvFq_01pxWrK3pFY3YREsApbq_yDzaZQnBz-ighpu-L989gk11CyjZlajLxDhUJE3nJsq7pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOiXfk_UW1IjgmYwaGIdPhmGwfgx0XqeKvU897gQrSQZrK2LluCRO2lSmYsBnXCSwOX6Sp9TtPcJNmAkvLVzo6VXN3rBPIjGFCqRJFDVj6qOwaO9Gw1am94zTNuY_spCJ3Q95blbZ5khfw5k160g-LGPY2jZ5-mZs8WVrk0qZ0E4ruWcrGFEquyACmJ8zRrjun3XYrLeIXfN6zWI8gr4TmjlsAfK5BEJK-rODCJ8szjLTSmTMhjxVFb_NHqaSZs4VMyHzFXyHgX60GhdD0DS6apF1v36nlFsmygPUN8nZNgjKGCQt7_7JlGrUE_hagmoMOiu57p_0I6Yr5G1g2kI-Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2cKeyh5Ygk-OIGO_UNeF63uNuOlLX260_FoMxbz4FwgcGcJ9sSbHQ-MmgiSOCEiQ1asq0U2lobDTwKtQz3-7nmFx4P3WqTn0kEtE_jCNruf6-naaHyjoHAKzmpV0QGXdTMsqakD11AOQWYOERxMeq8s1tx8MlkdVPlboptxwElS4nEWkNmIL2D2LuEg_KilNPD-UHQlYzdNY4kAhDt7bYYk2ab9L-npcg1RRl1i-WJXeGwpj3nyKaUuupzTXqu0Waz5qCrGhL59SAtRPQ_OfqVCgFTYctZWfhPn89ZZhP18sLQgd8-RVroRH-hhX6px0XB2mhezYNQjBn8tClq8zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzDBs5pxgVJYqKDzQ0YfzztkDZXukrFToFmqFwGawn5P25Sa9KRPmypW5l0SHl-kdQrkFc7lW99SdMcZYIlf1RisUq-EZ0tOcvkU24xFZeDGLnlRTFNei9L19S--IVIwsYmxN13uCDV-TSTkfp_YkcqwTtylihraAC--kV2Swvx7wuilvE1CHYvXp7Y1KZIGDattCIqlhkcXa4UyK_iAFxY6BbKBOBc1UuGu7M5TfXrqc6k6wGWLcSeUHfCgDqjig3C0eU9PfgVDvuaVe55olRMsPSfNVXNzY83uPbXzRB29bRhPYN6rPY9xzYS5LteTsrCmx2mp2G219IJeGqMn-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=LjCHXnh27DpxhqekrhVRGS5FkMGXw94weREgpyguXs5KnkxmtiUYVXoCXDFAQrX-burJ441wsydC7e8cz7MhdOekGR5o-J9J5jjbc3QbbPprusEt-dg4t0cf-UlrHH1UWfCv-BNro-ZXoPknN5XAIGRdSHu2090C6tqw9eAzAdQdA44oXXbg1TInDCenHc3KhYOc0a5NmyBMKq-QrJGQSafwDtMIrmSgH4Ny9QU-OciAp8yAZxtyaG0ObYVSZ41TtnAPdbaGM5YGLcr-JMiMbJdqOE6E30654IcLFxnxR3LCUQ52OnC0rzoOj9_-CJodteyHGfOW8pY5FODmowmDlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=LjCHXnh27DpxhqekrhVRGS5FkMGXw94weREgpyguXs5KnkxmtiUYVXoCXDFAQrX-burJ441wsydC7e8cz7MhdOekGR5o-J9J5jjbc3QbbPprusEt-dg4t0cf-UlrHH1UWfCv-BNro-ZXoPknN5XAIGRdSHu2090C6tqw9eAzAdQdA44oXXbg1TInDCenHc3KhYOc0a5NmyBMKq-QrJGQSafwDtMIrmSgH4Ny9QU-OciAp8yAZxtyaG0ObYVSZ41TtnAPdbaGM5YGLcr-JMiMbJdqOE6E30654IcLFxnxR3LCUQ52OnC0rzoOj9_-CJodteyHGfOW8pY5FODmowmDlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=AGoDvmi8Pt8CQ1BiucUf0NDkn-gLBwJca3QqVwUF-zu3Dqy6ZANE_Ms3lKmKD_cWGiADOfXu9mz_ti-GrZafNMRPMt66KFF7WIrZ8eyC0Y-xlV2IIa5SNOCbwxrDCA1j-vMY2Jx69x3RE7WCztMIq8IJZ3ekp8CBNb3u4PJshOEkA7dQ1SCnl-I0lQLoGF3P-T_xboX9IrbmXf4TBSlriNlZYjd_LJr9fQ3qQ5Do7awLBHclxTiw1T18Q4Roba46ZIZaAQDQQU60IlXmKoKAR-YAuSvt2WWscxShdGspLPv8c_rx-uaYqN0HslpCfv6vnXDL95aBzctUrMN58xR2uxxmBfgxmn1WxvVCwsdFl3cXioTC9zuXTVCy_VVk8WcF7ZnxnQjOtZfLwxG74VfMhj13smRYg9X3-rX7cGxp9lzkN4nmogzYeazu4QD6wKh4z4QHle3HPeWbhppMjxD63z-903lJVzJDvjISNmtuJUfa5fUCgz2g0NhDRxr9N0wz-J_WPw941gctjcVIEf3LuiexQLVQ_oIDLaIUQguaExKLsvXkSwY9gI0KQd1peAlSm799GVOZGYi64HqlFbKBdxFMxPcSYCdV4g45rIOn99zwkq1sJleFIhWmBbfBw51bWoHYw66ZRbB8K9Oo8asiJPMkUHpnGKPyJs2Q74v5SoI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=AGoDvmi8Pt8CQ1BiucUf0NDkn-gLBwJca3QqVwUF-zu3Dqy6ZANE_Ms3lKmKD_cWGiADOfXu9mz_ti-GrZafNMRPMt66KFF7WIrZ8eyC0Y-xlV2IIa5SNOCbwxrDCA1j-vMY2Jx69x3RE7WCztMIq8IJZ3ekp8CBNb3u4PJshOEkA7dQ1SCnl-I0lQLoGF3P-T_xboX9IrbmXf4TBSlriNlZYjd_LJr9fQ3qQ5Do7awLBHclxTiw1T18Q4Roba46ZIZaAQDQQU60IlXmKoKAR-YAuSvt2WWscxShdGspLPv8c_rx-uaYqN0HslpCfv6vnXDL95aBzctUrMN58xR2uxxmBfgxmn1WxvVCwsdFl3cXioTC9zuXTVCy_VVk8WcF7ZnxnQjOtZfLwxG74VfMhj13smRYg9X3-rX7cGxp9lzkN4nmogzYeazu4QD6wKh4z4QHle3HPeWbhppMjxD63z-903lJVzJDvjISNmtuJUfa5fUCgz2g0NhDRxr9N0wz-J_WPw941gctjcVIEf3LuiexQLVQ_oIDLaIUQguaExKLsvXkSwY9gI0KQd1peAlSm799GVOZGYi64HqlFbKBdxFMxPcSYCdV4g45rIOn99zwkq1sJleFIhWmBbfBw51bWoHYw66ZRbB8K9Oo8asiJPMkUHpnGKPyJs2Q74v5SoI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7FLpLoTASSKhV5eU1TjnnNqFcXdqD2Zrvan0zhASChqC4ITTOO1CF70SnRAiMC90rbiyOaRTeMiYikkf_yBEsV5I90AESC0rFk_XsTtlveLpYgtm7abNTlJKmUbcrPVF6qh1nMXoQvpsM7zGBQIFFKsLL8ZmpkMDZrulInRP3DS1aSUrK1GAcP1pgiMoFr0f-ZZniwhT3voftbpfzC6oXyFZ0ZmoPRtnCStC6MvjPbMWBstVy_oNhCOeSBCSllEIjJMhoVpeiXWwOAxBBlA2mJ7NL-w6V1_5juNz7QsyD5MWC04kjm-a4WqomPQf9-H5conIs2LwaGgNM2FqtAxTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WpDcLAjFowXWhJXyuks_v7cgy8nKZ0i7xP3Jw36hKJk20vnZAuhjt6QvsbYPmARO1w0FKButEPL4-ONDYP91xh9xXa5TsBtS03eGXGo43MJtHCZH46bGYtrnyZVVfm9JvyUicLNaUkflUfa-Je-3Hb5hmAT3-9kkr4AYu0ao4yrGLPu9MkSXFb9X0vU-qx7Y5qWOyVmDlWQpQL6TKYyPRUM6teM-n4PEF10_w58TY5HV3oSynogywouxYeft5Qx9FaknViC2XONErbVMsS2pg3k7vUqnUuYj1Sh29i_ueibnW1gf9PfTbnzZXF3r82V2zJcOSfQkbsqvyRSezaQ4UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DGVc29GScIqX29xKitXiiHPvcp3jH-VSL2wM609ROBfefpBm2CGBHER5vggMtcVJgscQ6swFf1Vd9tPUh7cBrc6oV5Hz5xuASy0vHSAJDyEGB3KCWA-hJLYAYGLvu6R_uxvu6g8jDpSmCOCIvu0_nZRAbCqmvwxxTL4OI-d8iGI23xzpsOeEeG8f1W-twDuECcvp4yCfhv91ZsptFAF1h4ATssGcIDAYU_Nzk09m7RlNi3abZboNacY022bL26mdNtEMBqtKfKVFOjpjAwSXftBxI0bltS80eRpcdTZJ6NUCz5e81S0ykoNhA-sbin1_o_6EvxL4NpC4MrOF2h7fIA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=oPqaZSk-yqSlga3ctKLDLaE1l48g-E4N8_2Gw7wpNZvbI3P0MsaUP9m3BYrHKy4UEyMMfnbXtbKC3xkryvGNLTxGykBAUaRWsbc_BBbTDu6N-y6oCz5bnjURCSoK2y6yNEdpBJF5Bu4abOKHkMLuMBqnBPwx3-l2RAwjndAnC2zwnKcGUPZgQ2cKh-RmEftqP2tjEiCLXtEx6ZHpfDzqwwUe7NR8YIeIGQr3r1kxbXvHrK8_JIhpoVcVp2vYymiO5tKYWuAqHWeZNhd6KpJAgUidaFwhbGqDkg4Wt_HeIphIhaKNWnqQtjwdPOulASfXnW1cTyL5gjMMC0-tyeEbTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=oPqaZSk-yqSlga3ctKLDLaE1l48g-E4N8_2Gw7wpNZvbI3P0MsaUP9m3BYrHKy4UEyMMfnbXtbKC3xkryvGNLTxGykBAUaRWsbc_BBbTDu6N-y6oCz5bnjURCSoK2y6yNEdpBJF5Bu4abOKHkMLuMBqnBPwx3-l2RAwjndAnC2zwnKcGUPZgQ2cKh-RmEftqP2tjEiCLXtEx6ZHpfDzqwwUe7NR8YIeIGQr3r1kxbXvHrK8_JIhpoVcVp2vYymiO5tKYWuAqHWeZNhd6KpJAgUidaFwhbGqDkg4Wt_HeIphIhaKNWnqQtjwdPOulASfXnW1cTyL5gjMMC0-tyeEbTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=rJQNka3JRCYr12Ee2BEP4hyCcPVfwFdfrL5uLsPOSJMZL5jaB40CRxaiCrpUm_SOqu7I6Fj1rTBw4wwzaxTQrQJZPLlkDZN-3Fi6DrYaKntJ-1tysMbMrKk_6VZ5ZmifuK9wfsn6OhQOnpd5b7lALyc5yn9zm2f3jtZOHc1FLNpy0qNvCpL6dk4YJxP4iw0zvTs6Th-FBSqwcckGcC6irnjNatyrwIWRxM1yz6EqQGv1Gdtj8KmL0XqX1tfNkQvHOXaunaH2E3Z7ckncSKH0SQEFVWZPzNz_X59eVlXnQ7sqOxsE5m9i4Igaqb5dHPAlXFwSQYZttuomyc4XeJUhBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=rJQNka3JRCYr12Ee2BEP4hyCcPVfwFdfrL5uLsPOSJMZL5jaB40CRxaiCrpUm_SOqu7I6Fj1rTBw4wwzaxTQrQJZPLlkDZN-3Fi6DrYaKntJ-1tysMbMrKk_6VZ5ZmifuK9wfsn6OhQOnpd5b7lALyc5yn9zm2f3jtZOHc1FLNpy0qNvCpL6dk4YJxP4iw0zvTs6Th-FBSqwcckGcC6irnjNatyrwIWRxM1yz6EqQGv1Gdtj8KmL0XqX1tfNkQvHOXaunaH2E3Z7ckncSKH0SQEFVWZPzNz_X59eVlXnQ7sqOxsE5m9i4Igaqb5dHPAlXFwSQYZttuomyc4XeJUhBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si_xAEL_wQ9hPzz8OegnDSK0z32nfauQBCn1hgL3lHLi-hd-1z4fr7qqm2SRFPKFmZfpwQaFws0VbmEtn6yq-eZKV0xx54vlp69OfPfO4o2GyHlabqLD3NkjocPR5bkrbwDm3i-rVoarCUYT5oQSXnnEPfK75iiPc7kmVvWnQ3iCwbEQAGt4YfyZs3aIPbG8M1fy9Cr12JMTqG9i6F8zuLktJipAsXsw8EGdNP3WmtQckbIp7Jhw0lhN63qJ_xPT98qxFJEiN_VNJIDYxzIvVvdaAZ_cqczU0wRls3QX_51knjHQFlML1dSJxmU6YZwmS8Q5IrN0bf4PSrFkY10-UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=gOQQy0wnakm9Y5JBDDaohxthCH4NkH9XxrTy9y2FebY7Zhtrk3lYSD3fC1JtvZPGi47Hxi5yqYaMoL7HKFijN2lNjSSzhNo7BxZM6v6W8p5G7paCFg9UZ525ZxVPtRC67iE7_Y7dJRWrS5vYu7WaTtWatYoD7qNkCYr_21D_GMBXFyM-MlEXYv1melUgKI6EHLMVS_qSK4gfK7bBRnYQcWbYiLUO2IRiCh5cO8Buf7tLosDTjaENHJ7kuz-yndeIDVYzlFNy-0DXMg5PHpjzd5uZVOMzr3FgS-fPngByg4PyitgnU5KiAeFRws_eosOtRFv0-coC5oQPNDGhV615-0qewuwj2B0dwEu5AEhSY-xJEBeCIrO-uFROs1EDBWNVVT1qqCVYZZG_IQThqeKdrtzQX44y3y0sbd1OWIIM8r14TZ6PLYK0a06FMfZ6IdrcBepADB8BYsOfnDxd96kh79cyPPJ482y4SyRSwi5BBpDMS3cXYLgO3rBeCmr6FqPZ6hvpUdsGD4aCd7ukqP_wYEG9ZMLsZzICELciq5rXdwcBhwa3djywfc-gXL3A139x_WQUATOi-5o-fPucNDCXXUe3VPmHv5eIoEtFLU3BwZGVO8rRoXPivENQHWHCiW0F3waz98j5IG49W46H-u6qO9HmNiVZX40lUvUUnHeZL2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=gOQQy0wnakm9Y5JBDDaohxthCH4NkH9XxrTy9y2FebY7Zhtrk3lYSD3fC1JtvZPGi47Hxi5yqYaMoL7HKFijN2lNjSSzhNo7BxZM6v6W8p5G7paCFg9UZ525ZxVPtRC67iE7_Y7dJRWrS5vYu7WaTtWatYoD7qNkCYr_21D_GMBXFyM-MlEXYv1melUgKI6EHLMVS_qSK4gfK7bBRnYQcWbYiLUO2IRiCh5cO8Buf7tLosDTjaENHJ7kuz-yndeIDVYzlFNy-0DXMg5PHpjzd5uZVOMzr3FgS-fPngByg4PyitgnU5KiAeFRws_eosOtRFv0-coC5oQPNDGhV615-0qewuwj2B0dwEu5AEhSY-xJEBeCIrO-uFROs1EDBWNVVT1qqCVYZZG_IQThqeKdrtzQX44y3y0sbd1OWIIM8r14TZ6PLYK0a06FMfZ6IdrcBepADB8BYsOfnDxd96kh79cyPPJ482y4SyRSwi5BBpDMS3cXYLgO3rBeCmr6FqPZ6hvpUdsGD4aCd7ukqP_wYEG9ZMLsZzICELciq5rXdwcBhwa3djywfc-gXL3A139x_WQUATOi-5o-fPucNDCXXUe3VPmHv5eIoEtFLU3BwZGVO8rRoXPivENQHWHCiW0F3waz98j5IG49W46H-u6qO9HmNiVZX40lUvUUnHeZL2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=R71jIV9Ks7s6m9rbZuPTtYMElw46BUl_UovX1j1rDN7MOX6VT-URihoT15Pc3R_mYn8F0Y3yEoE6LrClIGHaT2e_OORvLYUmRcqESfiK6ZWyStahs1GPnkMnK2-11St5nzQGRPvs6Fy99x7-7wgPFErTbVrKrRUT6CacuBKwL71KWIithXW2Ax4CQJwXmd5yIT6Un7xhO4O8bush9teL_gL-bQ1q0EXnPv-C0UOZCQTE-GIHFWnBuHaMKFHiXf59VWenaljaZQvbFiL7ewKXiJyoKVJphZ7f9KSnadQrLQ9EqpNyLhqZkSAO9wsRuV_uPVCsbuFGJm2dPY9ooSjsJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=R71jIV9Ks7s6m9rbZuPTtYMElw46BUl_UovX1j1rDN7MOX6VT-URihoT15Pc3R_mYn8F0Y3yEoE6LrClIGHaT2e_OORvLYUmRcqESfiK6ZWyStahs1GPnkMnK2-11St5nzQGRPvs6Fy99x7-7wgPFErTbVrKrRUT6CacuBKwL71KWIithXW2Ax4CQJwXmd5yIT6Un7xhO4O8bush9teL_gL-bQ1q0EXnPv-C0UOZCQTE-GIHFWnBuHaMKFHiXf59VWenaljaZQvbFiL7ewKXiJyoKVJphZ7f9KSnadQrLQ9EqpNyLhqZkSAO9wsRuV_uPVCsbuFGJm2dPY9ooSjsJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p16s-8ObCgt1xZwQdPOzgD0QIvdNcSRDpa8G4Hlg8zMI1jHYSenjZ0jefUQm7bsheUO8Hj5k2WzycXr4VqagP3Zp1fIH5AG4WMcrYsud2JKcetqjh84YG5CzWwyKD6qbN9wGDf_Gmo1nKDXRvDUa8vvA-kKKIkmyk5yVlfO60obF9ducHrbZ19fufVwsbhDqV4ZatoCX24alzzTO5hQf4HMqgbnYpGV0MHsHGOJcmw14r_Bsj-e2c903GW5lUz5ew7R-igFo5bPS5eY6wpz-Xk1yVuaSJIyKdneqn3N2hSj_GESeuzSIb4rXsFMwsPvdAHcFpe3ADNaQq8AsZA1eKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=kNjhB7H_lS2UYBlwCx2eMzVxpLuDNOgUcHGppX8gNF4fOBCppiXxIjEmVU3Y9aDoips5Cra-o_akVNWLFF6dpMlTMgCkxgfe3dqxVVumV8yUC6GlHxpRcugYhaowangl43sfgtoEAkVMFwxgrPtPqRcfzB9JvaJJiaZRKZ60OpgsA7O8dxqKbjGCFDVxpTACQgVy_F2DXkfFPLh5_U-oT-aSaykUA7-9DTLJbWYQKVgT1WWIQxbqx7L0sRHAbm-5yYu15sBkJSpmP3SZCFF88qKTYxiJ29xFHfdsflmaCEx5IiIwxxiXVw45YuCh0yJFuzaBFHDp459AFiKDU4SMIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=kNjhB7H_lS2UYBlwCx2eMzVxpLuDNOgUcHGppX8gNF4fOBCppiXxIjEmVU3Y9aDoips5Cra-o_akVNWLFF6dpMlTMgCkxgfe3dqxVVumV8yUC6GlHxpRcugYhaowangl43sfgtoEAkVMFwxgrPtPqRcfzB9JvaJJiaZRKZ60OpgsA7O8dxqKbjGCFDVxpTACQgVy_F2DXkfFPLh5_U-oT-aSaykUA7-9DTLJbWYQKVgT1WWIQxbqx7L0sRHAbm-5yYu15sBkJSpmP3SZCFF88qKTYxiJ29xFHfdsflmaCEx5IiIwxxiXVw45YuCh0yJFuzaBFHDp459AFiKDU4SMIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SAaotrxg4eYfFmBV4Qw8OY7qLBWWKEqZM0tt6FZveZkaFbVR4jpKJ_KwSTunqgyLO3F9JnDH1G8YCwTr8WWm_k1TR5BrnaNEd4tp6scPyWWgL2Q3ck5W_H26i9hOC2f-v8ba6GuJS7ND965MuigAwn_tTy14_WemoWs0g6QvNsiUEUKHjHn4cR-6cInO71cfbIT7N1tI4V5-WwGKB4sqMof0OKM2G7ul0A-zKGEmN57PNc5JwmbEXbtOD0SldXDIIkHPrKV4cmmsdXgQH98NW8VNB-u8kVc6U1I9ZKWjQ36rnPfIirhldGqBdkSkvh3TY1RPKunJCFVq9v6FsriYyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnfM_Bem9HcCXY0v0Owkce4MGypJhPg4INuv3e4oiGV9EVNNolHeI863g9CwBkveLfevnCL3B80G7i2P_PnIlVTUAJrrQXpVsRSPmFACWhZ6gkbGp_MNpqDmw65yfUqyIqVWttGIwoNvjVlJIvhqQ1-h4IHWe0F4RWJ8Zv1eZ2wzIMFNcU-4g8sbFhF35iRWmR4hEO_6TzBDPwnNEtx32eh_W3KGb-mzNa6bUcLclN54BdO3DPioLIpm_FGl6qUZrhlO6pTVi-RDuKFsUDpNbbXSNpokD4W3FaBqxZroRF7sxRSemJR2aBrdty7w44A4bseyD7VlQ3dcZkcsRz5bAQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=kJNbLsEY55p4UIzR0WhEoOabNyZ1VAutmeNN-EczcYKR0QffEKDlw0pAH3l-b2_pdcCBWWgUaG8YrmfKIGB_IIj30jwCM-cIvPXs_tZiTNyJHUgs77LJFxU_uO3dFUzbi4BgJyzLG6Um4S7fc23KprrtqB5dJlCAgDF_FbzoJtnq2rIZSOGtYZVc9Kxub4tt9Yw2XdVy-oIYSH1Zr-PA5Pj6ii317zAaHWIMyrh1ULwWbCcw4lRoy-2TFbps7kQ7Ds9IBiOyAf0N-wm-OZnd7l-ogDPu9ouVc1TbPFhYrYgy-4onxeh_RO3KLGqF0TLzsEHvFyelMD9O8e7EZDw4AgwgCXgJ78snabGbjHoUSll4lhrpAmng-tFfGMjnQwKPrgOCVMYMn4JeWsmXy--X9enVA9Ah1ufTX90NpdDR1iqJ0LW1-zzJOmS3pvNN0Tc3nG2Rucu60gw1AhrLwDb9WRDtYhyQ8t8h-jzgI6Hf8QM7kL73AOuLiTEcNorpR1IpsKXCnKQDlP8sKCO-8ngilqqgD1l35TMaB-XLcbGwIbGULrTOaURnD5dpLf75umIrEY8Vxwlo-B-ugzmqAX8ABcWpWPFKZOo0URpj5sTGrRBQXJ3Pj9DQ00m1XU9pIrJebe8Bnt-nzGOdAx4nFhdeaY8h6CTIWJi2CeV9X9qJRAM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=kJNbLsEY55p4UIzR0WhEoOabNyZ1VAutmeNN-EczcYKR0QffEKDlw0pAH3l-b2_pdcCBWWgUaG8YrmfKIGB_IIj30jwCM-cIvPXs_tZiTNyJHUgs77LJFxU_uO3dFUzbi4BgJyzLG6Um4S7fc23KprrtqB5dJlCAgDF_FbzoJtnq2rIZSOGtYZVc9Kxub4tt9Yw2XdVy-oIYSH1Zr-PA5Pj6ii317zAaHWIMyrh1ULwWbCcw4lRoy-2TFbps7kQ7Ds9IBiOyAf0N-wm-OZnd7l-ogDPu9ouVc1TbPFhYrYgy-4onxeh_RO3KLGqF0TLzsEHvFyelMD9O8e7EZDw4AgwgCXgJ78snabGbjHoUSll4lhrpAmng-tFfGMjnQwKPrgOCVMYMn4JeWsmXy--X9enVA9Ah1ufTX90NpdDR1iqJ0LW1-zzJOmS3pvNN0Tc3nG2Rucu60gw1AhrLwDb9WRDtYhyQ8t8h-jzgI6Hf8QM7kL73AOuLiTEcNorpR1IpsKXCnKQDlP8sKCO-8ngilqqgD1l35TMaB-XLcbGwIbGULrTOaURnD5dpLf75umIrEY8Vxwlo-B-ugzmqAX8ABcWpWPFKZOo0URpj5sTGrRBQXJ3Pj9DQ00m1XU9pIrJebe8Bnt-nzGOdAx4nFhdeaY8h6CTIWJi2CeV9X9qJRAM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neP32kYIR-ARhm7UmCbJcPL3l6s72qU44_UTbYCW2ZAwlpyGPzN2H1zbTvFM3NwNGo1I7xKTWnYRBRqhl3coXPXFEKANanbfJE50jtNktzGAoZ7tRIhQUy-C73bN7QkLywvwvmPcUbLN_lc6l0ej-Uk-cNB5mFvKa6uDHvViKyhNifmc2HUzxftw08EX2htnt9i1oSzQlR0nOc6e_I03V68zSBiKPsNFwcEP2DE6cSc2Dfz-BUguB1PLC4TtoFU5zyyMNMNG1SzBu6v6OD-4I7A9iQlhp7TFu13i4sSWA9rKvQR6qChbFgzJF8ifw1zQSLKwKEseMaCrqhNu_YvAmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_D50x89NewD6IV-tYzFWpi5L3JozsQMURx_XEMpuP6vn5l9kRnZxgzNrTHb8k-w7-SocNn49z1N6cW_cKQCfb3elLS4BFe8ZF8f8-4RanznaiVTLw3QhcNxFx73gD_Thy8BlGpvfe_5iuCfTtsRlFMeACZlm5CzF6E5WDqX9jRZx7jTFWylg7VG3KWSo9InTWiCeYkQfB-OLhURAtWaYEZNrmI7PydWRdTuo6gEMjXQoJveIO-B_-hnC91g_zuhV9x2P1BjmZwIVJW4XK1VDlYG5-jphMSV1DcAKENlB4sLutSNeh2yeaSjKXp31UAQzobdqWopQcit5VlXbjdXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=rn5aHYeGlDE4eUrLG2QUkrtXDitWzeSlX3AT34FmhfBVbL7vB5be-9DHKI3ujR-vpQJway9iqfbV4NEJ7OJEKshPjK3IhktVTqVLOzCRUjNvWHFJC0Fj7k3yT6AlJC1UbWc_RGy-K1gMOoQGoiPw4Q3x58kf1zWA6u__jsY01xUKkxIbxckKUrVlJnZpQTCMsbgtFmwnpSBohgrgCr1foSZYuXIlCfxyslRVIcyWlTmlMDRkqzS2Q6eDleDcVJbUs2HS6T9fiEpmK8hQx3sB5Q9LvSDTsLsnuU5C7Sn0SppbiulGngjjUfntkJL0FY3SR9uonH-BqNmtTsh6ZTW1SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=rn5aHYeGlDE4eUrLG2QUkrtXDitWzeSlX3AT34FmhfBVbL7vB5be-9DHKI3ujR-vpQJway9iqfbV4NEJ7OJEKshPjK3IhktVTqVLOzCRUjNvWHFJC0Fj7k3yT6AlJC1UbWc_RGy-K1gMOoQGoiPw4Q3x58kf1zWA6u__jsY01xUKkxIbxckKUrVlJnZpQTCMsbgtFmwnpSBohgrgCr1foSZYuXIlCfxyslRVIcyWlTmlMDRkqzS2Q6eDleDcVJbUs2HS6T9fiEpmK8hQx3sB5Q9LvSDTsLsnuU5C7Sn0SppbiulGngjjUfntkJL0FY3SR9uonH-BqNmtTsh6ZTW1SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=vU4qoR8IooQqVCxmaAOrvQ_zv8h5vT4WBWlGyv1yOyx4Jl-4y5P9qb8vwFdklCnbKKGmVW2gsKh6KLkgoxhyKSr6tyeVZc6kSjXwVXD7UJ2IZFR--Dmf7varwe0aS0cgXvlyZjYEp-zTMzT6QMiFz3ao2pA58xtUA5rUgNdXXTObHIF0xSfaqZjEJkILoDmGP8lgIRxh7zCuxfJLOYgvJFLJqwVCuQyFyc93xJfra6tdeYR1stMXrTcCQEjLNxp58IeWj2-fnoj6U1bpaQckNwlILAoFKvj_tOp6K3ryLloFiTl7muBE2sSXaru6Zz0aKANRR-IRH4w7xrGwx976Lw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=vU4qoR8IooQqVCxmaAOrvQ_zv8h5vT4WBWlGyv1yOyx4Jl-4y5P9qb8vwFdklCnbKKGmVW2gsKh6KLkgoxhyKSr6tyeVZc6kSjXwVXD7UJ2IZFR--Dmf7varwe0aS0cgXvlyZjYEp-zTMzT6QMiFz3ao2pA58xtUA5rUgNdXXTObHIF0xSfaqZjEJkILoDmGP8lgIRxh7zCuxfJLOYgvJFLJqwVCuQyFyc93xJfra6tdeYR1stMXrTcCQEjLNxp58IeWj2-fnoj6U1bpaQckNwlILAoFKvj_tOp6K3ryLloFiTl7muBE2sSXaru6Zz0aKANRR-IRH4w7xrGwx976Lw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=IBFbfgjFu1m97j4F_QGJ9HtHX4E9rVsszbF8FBQmfC5jD_6ebTKDXVbFqG1cFRECMoQLiLZgcCTgwT4K1ots7iMdvJUNmIyECwkTa0FN47TFiVGT4LXukkxXwR4z9MRjVTvYA4ztgSPgQSpzLRBVH-m4qfPft1B4izYQp8RQRdnXgznqW3tlCo4M3nh4vq_p12fVMAfi8jFOBLccKnuw-0XrOgYbFvzJliejgycrQRaue37MFb3MsJQC37_5PKj2ZbwXcgHz88vN2Q4hb3T-2hGq5OKGHBvTU5TxKGx3QuNbirMoZIMtlVkiWq8elmBVnTAsDk_Lwqg56SGqReGWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=IBFbfgjFu1m97j4F_QGJ9HtHX4E9rVsszbF8FBQmfC5jD_6ebTKDXVbFqG1cFRECMoQLiLZgcCTgwT4K1ots7iMdvJUNmIyECwkTa0FN47TFiVGT4LXukkxXwR4z9MRjVTvYA4ztgSPgQSpzLRBVH-m4qfPft1B4izYQp8RQRdnXgznqW3tlCo4M3nh4vq_p12fVMAfi8jFOBLccKnuw-0XrOgYbFvzJliejgycrQRaue37MFb3MsJQC37_5PKj2ZbwXcgHz88vN2Q4hb3T-2hGq5OKGHBvTU5TxKGx3QuNbirMoZIMtlVkiWq8elmBVnTAsDk_Lwqg56SGqReGWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P6eqpAXmqMYvc5GOrJ_0SIQuQgMX199nBxnAqupBlBzQD68XHIk9DLRamtfofTr3c7d5nfi59PXb5yggm-CCbw9RGR8Bdjj-MKWa9J6QhaBxAwYy4LX4Rp4ZQv2B_kzxUlOlacPAa2lbLRStvk2Exr5WvCdhzBTAuRrlPs2MZ4Bh3Rp_0CvubY-hbWOCJO1dJZmZXMGK2GYlfc8BBEnxxXbUzB5i_8iXvv1gh6sTSgzmf_UAQkd8ZyE5P01QJcuD_O_y93Rg0_NiMgf7yVuuv5Qe7j5u5lC4Y2kkzH8czrJn4NrZ_OHL86uL3SAugXSGlOvhfzMT4gdLcmsJ3Iqa7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsicteUWwPcJDcG5SsLx-gMnTLZ4ulUv3zT-EhDbK7-L3ZH8EJBxBCpURiE2rmPWwuZbgf66fbS_Dzl7u953KmFqgOf5cSG2yYCfNfLVVUYVPyl3YzyS-NQzKAbV4AJUFsBYaSlwzVvJLgrJeAQxZP5mALEOaqFnOB5ECcVnmYe0EOzIZz6-YAIvCkxK5GoGFzQu0NeKuv3sszvmx78D20aEjA-cM-8M7Tnk7RIykZSh_Y4k_8ia_UrsMYWSnDUj3QqXs_5ztb6iV03sef2eqhtZ0RKLrlyEjo1x5jrQKMtrFuCys68Z0CCuTxkRhCtBdNmZZ8MXNJtm6rlZEBmmRQQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=iBPJTasIy0Omreh7UoLpcYCZ9hANpU3NMY9zAb955Q3237mFhmzSKwXkWlqBv0929FdaZR-Qwd2GBy8hwFo5kcPbXOlxlU-LTeG4cF_dO-ClW8wQsUd2i2v8Yyg_l_8HuKGQ5VXUpq_KoPc2g9CQL3y5hzu96cIjOnD0__6E7SfuijHnQDxpu6YnYWLHXZ5t2-Ij62XIaCYrMQEOJ-0tc2r4NOI66kQ5MER6lF4Ior1e7vIBJg8RKMvXBwXAzOY8uvJbdPLsG2lI1xttYvkfSdwJYu2DUiA6NoSz-dBAr1mROg9Z-seMC5XigkIk022bqyHR-Lfd4PXvVR-UkZeOsicteUWwPcJDcG5SsLx-gMnTLZ4ulUv3zT-EhDbK7-L3ZH8EJBxBCpURiE2rmPWwuZbgf66fbS_Dzl7u953KmFqgOf5cSG2yYCfNfLVVUYVPyl3YzyS-NQzKAbV4AJUFsBYaSlwzVvJLgrJeAQxZP5mALEOaqFnOB5ECcVnmYe0EOzIZz6-YAIvCkxK5GoGFzQu0NeKuv3sszvmx78D20aEjA-cM-8M7Tnk7RIykZSh_Y4k_8ia_UrsMYWSnDUj3QqXs_5ztb6iV03sef2eqhtZ0RKLrlyEjo1x5jrQKMtrFuCys68Z0CCuTxkRhCtBdNmZZ8MXNJtm6rlZEBmmRQQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=hqtBmbkcGPhFxNJNL9Z9ydPOpD6J7K3w6ZImbR8CjA2506As1IJK6O4_gsLdEM2RA5XuBnOp1Ar5b0ZEFs9CftkUM2XExddkxQT6eVMGUcrDVM-AgndDRKokOXIp7HrkxBpFPdw_2WZi2dA0Qc5oFwV1YMRCGVTMgt_N-YNH2-PjGv5SViSFHaOXqjt43rpBG-tX1W-px-cyJObroiX1X5Ma-4n5_W1GlNbCscGv5FyzYAnOvPBPjHvU-XAEOYlQMqQlUHcw-GU3-RJMX27RVFVVrePhIeug1dfOAHQfBKDVgL5fLX2N328UVtobDoxe9jz4KP2qLux1_ceP98Pqrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=hqtBmbkcGPhFxNJNL9Z9ydPOpD6J7K3w6ZImbR8CjA2506As1IJK6O4_gsLdEM2RA5XuBnOp1Ar5b0ZEFs9CftkUM2XExddkxQT6eVMGUcrDVM-AgndDRKokOXIp7HrkxBpFPdw_2WZi2dA0Qc5oFwV1YMRCGVTMgt_N-YNH2-PjGv5SViSFHaOXqjt43rpBG-tX1W-px-cyJObroiX1X5Ma-4n5_W1GlNbCscGv5FyzYAnOvPBPjHvU-XAEOYlQMqQlUHcw-GU3-RJMX27RVFVVrePhIeug1dfOAHQfBKDVgL5fLX2N328UVtobDoxe9jz4KP2qLux1_ceP98Pqrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fhgUE8szqxPxxi6p5R7MwaHrmatUYNJrnuYUKUBj4jrjrPvee3xy7HcvcniojScNMUK9eAvpDFEEIzsTbzR6Pa2Y1HoctWpo5KBcKxTeCnQg_FZLhAS-6xNTEkVE0qXcbaqMKEQussRkJ9E-J0-x_n8fPCLGJqk88PmyEaTv5U3wSltYxfJtxM1mGNBic77ibzqnpMOAlMGUxIjogI1NAfhGi7mjYfV1RvXo9TsrxgYxsFcMCXtNd5tc35t9o0QnPf76uR9ZYtQ7betUAC17ji6cHx39wNDVN6b7t19B2Eq6DLi0HI2-MDouJ9WHd3u8iL9KMF8UBqd7PXe3MteqCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=E1TelIfG5ljnZ25g2FcvBYDr5VBwPSAtJ0DcxhxXfmeEx_m7Urxt69vGBIZkeosr3MvXFtdV9G1Sc4DaTnprghMtnaE46egwdHWmwVwgyIyzD0pR9ab9HoMb0bbJGkAegFFioCP_uOy8EmtC3GIldUfpfKm0rNciJJTE0iO-5J489vxkUXHxhXVpdXVgv2dd7hBT2p1fJ-3cehnslckTXGQBGdMy5IiYnrVYcMEQxhaOvR1g11gVCKrYiEuepdhXqnqeWg9BmV2BjixAk57a-FSZFAncS9537sI4W-jvFhUFReUYo8MFLkOtxkag_nia7SJ_gpRjuwktMQlmg8is5afHd8MoqTAsOdAWL9DNUEgKWlegkcSl4jSB5gJQP5IfxOwxtVWbR2vKtbySBljTTRyIw7n5PzGTOhXDIzohCxuqXsKrHRre-KRi1W-WHz5Eaa2HYBLRjcD2ixZe1A_JUnHSyrOTPjcjwzdG1-k8A8QjezRQYaFQyYF9t2YaqkQTE2muBiVHaGWNr8L9eRibSyEAnrLMaB0gYsFRWpq9IulEYKD5hjZasB43FWwzfSDJKz_OAlTnxZ0kwKr6FUmlBr4Tt2G2cIcm9JBlKHIFD-yyYPQRWLrqNIfaj6rd8hZ3PVz2uJsnxwPE6ER1WS5Ox4Y_Oznkd8R4c5ya9PN1Z8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=E1TelIfG5ljnZ25g2FcvBYDr5VBwPSAtJ0DcxhxXfmeEx_m7Urxt69vGBIZkeosr3MvXFtdV9G1Sc4DaTnprghMtnaE46egwdHWmwVwgyIyzD0pR9ab9HoMb0bbJGkAegFFioCP_uOy8EmtC3GIldUfpfKm0rNciJJTE0iO-5J489vxkUXHxhXVpdXVgv2dd7hBT2p1fJ-3cehnslckTXGQBGdMy5IiYnrVYcMEQxhaOvR1g11gVCKrYiEuepdhXqnqeWg9BmV2BjixAk57a-FSZFAncS9537sI4W-jvFhUFReUYo8MFLkOtxkag_nia7SJ_gpRjuwktMQlmg8is5afHd8MoqTAsOdAWL9DNUEgKWlegkcSl4jSB5gJQP5IfxOwxtVWbR2vKtbySBljTTRyIw7n5PzGTOhXDIzohCxuqXsKrHRre-KRi1W-WHz5Eaa2HYBLRjcD2ixZe1A_JUnHSyrOTPjcjwzdG1-k8A8QjezRQYaFQyYF9t2YaqkQTE2muBiVHaGWNr8L9eRibSyEAnrLMaB0gYsFRWpq9IulEYKD5hjZasB43FWwzfSDJKz_OAlTnxZ0kwKr6FUmlBr4Tt2G2cIcm9JBlKHIFD-yyYPQRWLrqNIfaj6rd8hZ3PVz2uJsnxwPE6ER1WS5Ox4Y_Oznkd8R4c5ya9PN1Z8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE0MvM84DQQQ5PAi2gAS_6rD4kKmbMrqsYEJynmHG1mefUbKPjqwxyfy-Qiin10Ac-QiLMSYitUPHoBzF5aJv4rZvFOvnP_7L6ty7SBJfNpUJ8anLDsV7-3uH2W5R2zKSoUIhDlY5FaaYIYSPzqO0HMArclMwnmcDTu5CYhC1S-b9OmGq4k-F9fPR-M16f2GZRKYAQdGA4uyGXEcHUR4WfaRlHg3C8hl1zDW7NMSYXG_DVgq-eNbW1stv1CU1XdYrYLXpFxoGI9adk975zoZS_TcSd92R3cuEcgJvVHmP5eTX-E3bsRTJTPCFEHbLZEvV0geiMYSFfzobr1-xfjw_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Lr2fJ7RCIWhlKim1vcwliGQ12CG7Nhr9bDgyRnT-0zyQUn8qkM_PK6bxPqYNsuuEA9fpyLkf4FZNCqm3ya-ANpLMWqmEPhL6y1jtb5HvSlYinJ4VZdX09M8XQHlZigwkT25Y1da3NKneN2PlLI7vqA9fwNc1CmMqjZATUFb9rFCZOhF_yW84WZxz9r6aq-E0mqwy8gYY5uCkU_9RfFg32EJoWPyto91SqOGTd5aH1Y_obgxVf-b1YTSnDkVkVzs6WiKz9HQdMsxVnAOVnZ-JkIJzqsnfbO8C279t7wpPxF8lYqirz-T5C3UCsrukKIQ0kSvwn96Ytn-w1lViMbMzEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=Lr2fJ7RCIWhlKim1vcwliGQ12CG7Nhr9bDgyRnT-0zyQUn8qkM_PK6bxPqYNsuuEA9fpyLkf4FZNCqm3ya-ANpLMWqmEPhL6y1jtb5HvSlYinJ4VZdX09M8XQHlZigwkT25Y1da3NKneN2PlLI7vqA9fwNc1CmMqjZATUFb9rFCZOhF_yW84WZxz9r6aq-E0mqwy8gYY5uCkU_9RfFg32EJoWPyto91SqOGTd5aH1Y_obgxVf-b1YTSnDkVkVzs6WiKz9HQdMsxVnAOVnZ-JkIJzqsnfbO8C279t7wpPxF8lYqirz-T5C3UCsrukKIQ0kSvwn96Ytn-w1lViMbMzEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e91o6M6I_3DBU0dVoPL_JEZzJO6AVKvS4r-SRvB6j11WdsRERoeYGxhe3bzRS5033rlVMuHvy6jqSPNOuaAjhnMCbf-QdLmlK22ns0nWmQ1xKOscSM0TNWL25eSQ-KCXyIUVKzj1ktLH6UI8hdxoMUv2sgCP8umPgVtexxyUymvl0iqHljpTVEyLUQCDJ_VZieCcpOBBJSaZhjg6ESSZERJnwPEb0Kb-gZTAnJqVweFsEj5vlswrF6YimtMHTUQLKwQtEnysx7VLJsEH0Gq_YCKUzN1yWQOmequh7txBtcgV0MVOcRuvR5uXZsuyaScMkTfFyXuPdvCFkquqe_Ua9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tp8Gt5GVurfIVsd3uCTn5EEuPlsMdAzkyiggsgCGR-4DJ31-b2Dfaee5FoJCi842KDJZL6yimHHMH5Yea21-U5skSLURCdFr5b70GmlTf9XbHFVRJMe_9NK1wLF5bnIkuJVnsrjFkw8dHrmBndpjKtsTanr47-sX_j1HivQqQm87NGzgscAhbZk5RYL4tABtVUvlmc_YTOHO-EBVSuQwXrnWILOc1WfCZCJiCK4z4rjWrYU_X1vtNPya9400BsLXLDqzChPylqvEgB7i9W6PeBfg6ejQOmDejH_tIYU5G9bR0HG1Ck4PynahfMrBDXtmsI6w4d6zGk6yWLmwWna9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7baPLQRgbQNoncCFoDrrBuNdRMquY5WBz4nb2t-InE6EVUpV5MThnvwUuxozcL5cypq_TMrSfrNQ2o7w67cUA3Fpo6CLtKHntOGziihKqOf2PTz8ew_MY-cFEC0qBJKSPRqcP0I7N2-eCkJZ38gGJEWHy0TWcxD8Ld28fq5TMgxwNapE8U48GSnMWw59HLPup7DzyqW4dGtKOhPDo7qSyr7Zp1oEWwORoFODeiCsd2hDLlk1Dv65z1TFKHcPaRdR8vu_ZQDbR7yTsFT34VfJAy77T2x6Ybq-S3NWE94J3jKGWHnmW0QkDvLgRRHK-kaB6oPynEjbnXeHYBlq3Se5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Qp6jxWF_B59ou0tNvRhi9cTiRcLbPdWvFp9HEY8Vj5BRBiH4iP6EN51pP3ANWaCe63ZHWv4jw1_A_75ZZpfaOnOk9FBtYOYVZmkKjbWEsVXBlTAaSmvb4lYJHcNzo5oJiozUndJgD55WCJAPIG7Pi5XBN6B6IAV0djqo3cso4dvWvXvRveAzOB1R-sGpDLxXeUPg1qkTiuOVmtC52BD9ycpe8yo81C3KErkFvpTLWeTvT_h6lsTmLTOITC_mZkRal346UE8eCJ6RCN7mOp3WZrTMfw75aqYCIo7iAq2oUQN5Wo18kwiQB_zsUCuqEMSORJIHwyJ5RmujBAq4gYLGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Qp6jxWF_B59ou0tNvRhi9cTiRcLbPdWvFp9HEY8Vj5BRBiH4iP6EN51pP3ANWaCe63ZHWv4jw1_A_75ZZpfaOnOk9FBtYOYVZmkKjbWEsVXBlTAaSmvb4lYJHcNzo5oJiozUndJgD55WCJAPIG7Pi5XBN6B6IAV0djqo3cso4dvWvXvRveAzOB1R-sGpDLxXeUPg1qkTiuOVmtC52BD9ycpe8yo81C3KErkFvpTLWeTvT_h6lsTmLTOITC_mZkRal346UE8eCJ6RCN7mOp3WZrTMfw75aqYCIo7iAq2oUQN5Wo18kwiQB_zsUCuqEMSORJIHwyJ5RmujBAq4gYLGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOgtPZqRx4n6VLXH-tmSyzNL4fsmiQxOscTq0vN4KlMAfcJcC1kNO8JkSEPRAIcpZkcp0py8-UZP4zx-QL824pgv-MKB87AzkL5ddjxz4fLPfYhSfD2CdIU8pHannzHAxA0S1pUSSVil2byqWa2Czv1eG5fGCTd9eH3TEK98oMxHtEyK6tuGVpxvZN7uvu3MkplInz_gSlkDdAF5uhxx7MLtUitmPXGkk4y65GLIruwQqfRWAw-XPYG0AHzx-tlmqgW4pfVFIC7vreN_f485lbQdg5oAz8mqZwLAyCd0TFv-WFnuJPWyzE7_t7_uW49AqloLMlQRyOmNq4qzEL1-ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFLUdA-BNlqC_SmFJkEWduuRa6Fg28SRw2-z5TG1sThY9Ch7Gc-U5NRYY_KU3rl2QlukjPygdU7vom9TE6w35gDw9KMPO1Ps2T0lz_UptubS-aR2UVy7g-u5roWzRG7qRY7S0B9XOxn4-rYTnTqcH1cKfRZgw7sxDKJ8v1eE-B2Pt9ObxqFimNgBkkGZkOPki1zBjTCGe_FVA-mS-91YQMMS0eKNoS78S7CbSUIlYTSxNVKbLYoapkHQE_U35C8pwgaVfQuEMaWtLNmFRImuHauOYlMiIm4MKWSozUx9H9bbhHxuzruQJk1M1T1bUC_LgqPmG9TDTPC_JlnPUCWTXSqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFLUdA-BNlqC_SmFJkEWduuRa6Fg28SRw2-z5TG1sThY9Ch7Gc-U5NRYY_KU3rl2QlukjPygdU7vom9TE6w35gDw9KMPO1Ps2T0lz_UptubS-aR2UVy7g-u5roWzRG7qRY7S0B9XOxn4-rYTnTqcH1cKfRZgw7sxDKJ8v1eE-B2Pt9ObxqFimNgBkkGZkOPki1zBjTCGe_FVA-mS-91YQMMS0eKNoS78S7CbSUIlYTSxNVKbLYoapkHQE_U35C8pwgaVfQuEMaWtLNmFRImuHauOYlMiIm4MKWSozUx9H9bbhHxuzruQJk1M1T1bUC_LgqPmG9TDTPC_JlnPUCWTXSqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=A7kq3lbUQpAVix-jwNoN8y2QqThsExr_DNXojz0jO0Bu4KuJw2t-3WqwlwGPw3VQhsU88Fn6txteBcbEBqW6ZDgYcHi8fdR_Cfn8fwC_FIy2Z5hSBFeXMg7QE58ksQmrZSmMlPolI9-QAPQTC26NM-BtGK72V9uPbJk7BukWbzdrvedh_ow63x50Po5mmxS7_a_N6spsLOPE50C_Sw-Uu7YUuqF6tWGrSw0KfXfEjS1LiEAp0QJvVqpxlmEQNRpqvQ7pU1smHM9Fp49LQDRryGj2k9hL9FvJKL5OeFOmsTbUK10LOqlyjQBKfzg-M8SaINhRyzOVVChyMEx7zrNilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=A7kq3lbUQpAVix-jwNoN8y2QqThsExr_DNXojz0jO0Bu4KuJw2t-3WqwlwGPw3VQhsU88Fn6txteBcbEBqW6ZDgYcHi8fdR_Cfn8fwC_FIy2Z5hSBFeXMg7QE58ksQmrZSmMlPolI9-QAPQTC26NM-BtGK72V9uPbJk7BukWbzdrvedh_ow63x50Po5mmxS7_a_N6spsLOPE50C_Sw-Uu7YUuqF6tWGrSw0KfXfEjS1LiEAp0QJvVqpxlmEQNRpqvQ7pU1smHM9Fp49LQDRryGj2k9hL9FvJKL5OeFOmsTbUK10LOqlyjQBKfzg-M8SaINhRyzOVVChyMEx7zrNilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=rcLwEMuitJbUQNBKN9DaCtFoBVLmK3GlN_0yhVz0PUAaXf1lTnHDmTpXyVr-Ndbi6ZiZlIhzMblbBQVpnReeknvdwz8zEOwMXDmiopq55LCejViFD3bx15lfB4Lk2oZhuDy1K2YCSo1cmqshd11XoXNCVrTC19Lgd8BoIqCOy3DyZvsIrFhc8tBEmrnIINXqJisQzcaeVTL-Aah7p3nIYDHgkZlGRVRaaUH8UtVbx_rkJ7L7EH9Z8claZXDedeW3kGlZQGx3-5xnPiu9yiVZyhDdh8TCTcrwvPHpxHXcXkfrE9E9_IowsmtDN0MTtWWKMhtl4wcEVuwLJG0c0LFUl5X9zeWZP-Lf5pecOfccuQnYWljHCiE-DEVVS28RLaoFiC5MTjasQp7amsssH1C1GN2w5E3R1FH_hBRzJqeID1Dh2GYDm26tmQ3_MbjFC8lN6b8d4RrtZmc5D8yR8z8qA6kFxnH8lM07UIBZPR4gbe2VG0Z6Wpmgj1gD9_FrcyEhylibmzAndOudJQDO07ZgWRSFuHq1UAf52sKKXqCM-LnQRYnGCwFg8aEeCwN-wbuzMv-M4qyGvqg87FZDCqNcPOTAHJHa1TN08xsWh0gO0AKgbXabDubtkRiy9kiFZ0Am7XtOjEdCeRTG36zYM5UgKaI4dIVMFDcYvNdc3SQ4oms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=rcLwEMuitJbUQNBKN9DaCtFoBVLmK3GlN_0yhVz0PUAaXf1lTnHDmTpXyVr-Ndbi6ZiZlIhzMblbBQVpnReeknvdwz8zEOwMXDmiopq55LCejViFD3bx15lfB4Lk2oZhuDy1K2YCSo1cmqshd11XoXNCVrTC19Lgd8BoIqCOy3DyZvsIrFhc8tBEmrnIINXqJisQzcaeVTL-Aah7p3nIYDHgkZlGRVRaaUH8UtVbx_rkJ7L7EH9Z8claZXDedeW3kGlZQGx3-5xnPiu9yiVZyhDdh8TCTcrwvPHpxHXcXkfrE9E9_IowsmtDN0MTtWWKMhtl4wcEVuwLJG0c0LFUl5X9zeWZP-Lf5pecOfccuQnYWljHCiE-DEVVS28RLaoFiC5MTjasQp7amsssH1C1GN2w5E3R1FH_hBRzJqeID1Dh2GYDm26tmQ3_MbjFC8lN6b8d4RrtZmc5D8yR8z8qA6kFxnH8lM07UIBZPR4gbe2VG0Z6Wpmgj1gD9_FrcyEhylibmzAndOudJQDO07ZgWRSFuHq1UAf52sKKXqCM-LnQRYnGCwFg8aEeCwN-wbuzMv-M4qyGvqg87FZDCqNcPOTAHJHa1TN08xsWh0gO0AKgbXabDubtkRiy9kiFZ0Am7XtOjEdCeRTG36zYM5UgKaI4dIVMFDcYvNdc3SQ4oms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=UDj4-MHlVPXZhBZO6yr9aV9kkJyNWC9sjEtvSGxrps7HCmOlygvHHSeit1hVtfX60x0P5daZKs8R_kXLQCg40QtAARRT6hPS-Bh31gSfeKAq4TWFyFnWdPfAlPyK1oiCgAgKiTCSoFWXt4I89SwXTj2UZAYCyHxzKMxkE9m1haJMpPYl0u7iS_oG02vmtch6LyvFDYNFLhWhFmfTGoe2uVmfRcoA0Y-fB-bgHnsjPZ0ENshNcjkMQI2XI5DA-Fud1QucB6nI0SX62XzdRQVFG40zX84UK5mbPIBElBkkSE2eVGEs2drKCFqrHWd2g9V5fW0vFcYQ0s7NwExbA9-hAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=UDj4-MHlVPXZhBZO6yr9aV9kkJyNWC9sjEtvSGxrps7HCmOlygvHHSeit1hVtfX60x0P5daZKs8R_kXLQCg40QtAARRT6hPS-Bh31gSfeKAq4TWFyFnWdPfAlPyK1oiCgAgKiTCSoFWXt4I89SwXTj2UZAYCyHxzKMxkE9m1haJMpPYl0u7iS_oG02vmtch6LyvFDYNFLhWhFmfTGoe2uVmfRcoA0Y-fB-bgHnsjPZ0ENshNcjkMQI2XI5DA-Fud1QucB6nI0SX62XzdRQVFG40zX84UK5mbPIBElBkkSE2eVGEs2drKCFqrHWd2g9V5fW0vFcYQ0s7NwExbA9-hAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzXdAlA8X1TLOHpSQnUag9JA_Z3eW7YXOkIUXRnY4O4dYuwPb4qFXnUk2t47AP23KUFPtIVWbHY9DYYjMFR2OtJIBWUSTche4otg49HNWA_OSNK3RUVuriBKlhavdts88GU1d5_djQekfjjtTGccWU8kbZA5uS9X9rUxTcb6WXWQwSYBg9L2vQg2wyIfSMToe7cE-GJzuySC4ed8H-sb1jQc2Zr9P5hUZEE9HTWvmvsZe83raakNaZVDv_qsdIgFXvf_R6-1fgohgzbj1JO0zLS3ZtyDALJ8-sVtdx5dir1qM2BSl_xjD9zLFUe-gXV4Q6gIoSmAcd5vC-a8JR5XTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JdEZvmaY4otuvdH1Dv9YRJmpNi6hRDiWH82zs2kJ7vZnpMRGyHqIKVBpC_77wZNgf02kKMWhsy7JVeoyDz8OOmNujDnE2tn1idOqsJpxuFdv-Fby0Jv9vzLA8kx-_HAYhhr-nKpIFZXWv3lg1GELRoV4s489ZuWKBtLGB_6A1EiBBO78Ram4xYx_CV00YODy_MjF42NrX1RcIKLZK6j2qOjsA4nhuCu5WHVQgURJ70laBfhQ9A73nzE8eG4K_VNURo6TeW_v3bfCMHu-WgDVP6njRxPRzMGcH-DLbJnwPP9kXvxQp3F1jQkTzrFczoRW_mcOUB8ynr_gxabTvMTm9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=JdEZvmaY4otuvdH1Dv9YRJmpNi6hRDiWH82zs2kJ7vZnpMRGyHqIKVBpC_77wZNgf02kKMWhsy7JVeoyDz8OOmNujDnE2tn1idOqsJpxuFdv-Fby0Jv9vzLA8kx-_HAYhhr-nKpIFZXWv3lg1GELRoV4s489ZuWKBtLGB_6A1EiBBO78Ram4xYx_CV00YODy_MjF42NrX1RcIKLZK6j2qOjsA4nhuCu5WHVQgURJ70laBfhQ9A73nzE8eG4K_VNURo6TeW_v3bfCMHu-WgDVP6njRxPRzMGcH-DLbJnwPP9kXvxQp3F1jQkTzrFczoRW_mcOUB8ynr_gxabTvMTm9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MyH1K86ZEzH8DKXaiodh4ejBe3JjAW_DSuC1A9kkA-yGWxxw2m-ZnEWei1w2GkB9hl9U2xUWKIHMW_mdUtkUc5ukFVO4xw0pdaZMsrHWJWIdIQ1FeMmXxZ3l85_4HN5-G1vRUaL76HKDiWnwY69-d7Z3u_-5GWkxUlG5bSU8z9Z0dEfJheDXK9bLKPNijeBDS0gsUktju8iTaAAmLn-LxK0qytm5RxKryPX75vzWLTYw8zEi23mecym1N0jY3LI6HxcZxwv7J9LE_5w51HTmagfOPjj_kf5_M-i-ccS4k7aV_yr9Qd_jonJEEJTRCzhPDGvZxFgis9asDuQdVXPJIl3h9fUZjmFlLFBLeg44i-iSCClTvd-bF3zfLPwtn0cvnm7YvDpVT1LAkMyDBLiXhhjXgFUyEDh-vgeKKKVrWs5-IaXR6n-xd6ZJYZsAOUKhfv9DV-SUjj7f956Zphs1VV7i6wAcWyTDGAlx5YGuPKcd0xMFtD_HPTHEie6Fg69fmUKgP0IV8Aqr1PPPxNhIswoBXDj5_jhsuMG0hHbw5g0SDcP26livv3x8HZsmt0-fbOQtpeM50ySCD7QB_M4oPFVw7mw5TOUKR4gBjcnpZOPOK7UWiKrFldGVVgS5Xx6-Kxm3yVJnpVSCBFAAiFL2BGKUehbuhU-XJIXm0Q2cVmo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=MyH1K86ZEzH8DKXaiodh4ejBe3JjAW_DSuC1A9kkA-yGWxxw2m-ZnEWei1w2GkB9hl9U2xUWKIHMW_mdUtkUc5ukFVO4xw0pdaZMsrHWJWIdIQ1FeMmXxZ3l85_4HN5-G1vRUaL76HKDiWnwY69-d7Z3u_-5GWkxUlG5bSU8z9Z0dEfJheDXK9bLKPNijeBDS0gsUktju8iTaAAmLn-LxK0qytm5RxKryPX75vzWLTYw8zEi23mecym1N0jY3LI6HxcZxwv7J9LE_5w51HTmagfOPjj_kf5_M-i-ccS4k7aV_yr9Qd_jonJEEJTRCzhPDGvZxFgis9asDuQdVXPJIl3h9fUZjmFlLFBLeg44i-iSCClTvd-bF3zfLPwtn0cvnm7YvDpVT1LAkMyDBLiXhhjXgFUyEDh-vgeKKKVrWs5-IaXR6n-xd6ZJYZsAOUKhfv9DV-SUjj7f956Zphs1VV7i6wAcWyTDGAlx5YGuPKcd0xMFtD_HPTHEie6Fg69fmUKgP0IV8Aqr1PPPxNhIswoBXDj5_jhsuMG0hHbw5g0SDcP26livv3x8HZsmt0-fbOQtpeM50ySCD7QB_M4oPFVw7mw5TOUKR4gBjcnpZOPOK7UWiKrFldGVVgS5Xx6-Kxm3yVJnpVSCBFAAiFL2BGKUehbuhU-XJIXm0Q2cVmo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mMkBVvfX4DHwo9SUZqC9aYGveiP-xbX8AqCvS_Sfvhz1x8wJ6E3qdFUA8U_FytdOCjfwUEhnKlpfaZ9NztUjIiZiEnxr9Knx00KRObPADOU59vitYpaarJ_YKca9CsxerneDu9M2ogcil4fUX-bzv0IXtzIjqfFawVEOPba1RugCt1fmzVtQ9oy1QczWbbv4QtYU_Zvqb5viN4sdiRLDhkljc5hWsHfxkfdPgLfMYvDMEx60heqBLbVGsUR81QKumwZRenRulhKAl5mGbtqbu3IT0iijPwhEA4XZXZIP6jzVrxieY285LhxOLlqesd8Pn2imz5mlTDt9TgpbtuG5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=HDaNQ40FIw4UiRetN-RbAwGgCvvqbrnrruDKNcCSYZFvwqF_3O82RojTZFcQUu8eyCkVXzwfsBmR1RXpX1uVHe0OfD0VObb7z_AjIN5p1-Nha5492GCIVOvWmpHK1eRkwxd1ZNAm_ZL5Pd0lKkvL6ceAUx2zkXA9Cx-1lRLhEkSdqXHtiC2XlAI3b-FSaGNK0pKQ4296BNFRgBFezJWBdFnqf_u8Hy3amD_O00yOyu0YUscJ1gggdKOtC3uoYkx1U1fqeBicIcy525BxBm4Q4tZyLoIlq-2n0B_M7EPdCPA1VBtzLgSXttKhQdr6D6AkjndPkuHM7VKIoGJsw85uPQqowQgSQ6YfypUDoh1oQdXX2PZpp225JT05fFT871WUKgLzP_1UbzOy7jJnwExp0keqO5fNm7sX6U2FMP7IdURZ8igwJ11GWLIsyND6hiWSB1U-at6YGm5IjdsQFkFf2lHB_-vd_hnbEzrce2NsDK20wVIf45UQvopQm43csH_bqLSRRBIc6ggU2MdwsZcgWCCMnQyOX-nH7HTdvfuUVbCKoHmw6RDWUGoeFJjRFYseqWnJa3Lb7efI22MdMw6Fi_QiAqXhshMbJPsevTtWOE-sd68uX5SUjAcpGwzlZ3Y-SVeZAEP3bCCv-ItcRUyTon4OS6XvcalU4LMuYocSpiM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=HDaNQ40FIw4UiRetN-RbAwGgCvvqbrnrruDKNcCSYZFvwqF_3O82RojTZFcQUu8eyCkVXzwfsBmR1RXpX1uVHe0OfD0VObb7z_AjIN5p1-Nha5492GCIVOvWmpHK1eRkwxd1ZNAm_ZL5Pd0lKkvL6ceAUx2zkXA9Cx-1lRLhEkSdqXHtiC2XlAI3b-FSaGNK0pKQ4296BNFRgBFezJWBdFnqf_u8Hy3amD_O00yOyu0YUscJ1gggdKOtC3uoYkx1U1fqeBicIcy525BxBm4Q4tZyLoIlq-2n0B_M7EPdCPA1VBtzLgSXttKhQdr6D6AkjndPkuHM7VKIoGJsw85uPQqowQgSQ6YfypUDoh1oQdXX2PZpp225JT05fFT871WUKgLzP_1UbzOy7jJnwExp0keqO5fNm7sX6U2FMP7IdURZ8igwJ11GWLIsyND6hiWSB1U-at6YGm5IjdsQFkFf2lHB_-vd_hnbEzrce2NsDK20wVIf45UQvopQm43csH_bqLSRRBIc6ggU2MdwsZcgWCCMnQyOX-nH7HTdvfuUVbCKoHmw6RDWUGoeFJjRFYseqWnJa3Lb7efI22MdMw6Fi_QiAqXhshMbJPsevTtWOE-sd68uX5SUjAcpGwzlZ3Y-SVeZAEP3bCCv-ItcRUyTon4OS6XvcalU4LMuYocSpiM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Y4GeDhKJOnpGY6Elcmra0wWTkooOJRrZs4H6B9J6QBskvZj_SgP942uTBXE-6GPuhLFjBgKQ_WCucS_oeSAPbzAERcma10pmlQDOccZ6S0SBk7ogeX6b-QGxQZdyl4Vc7u1D1Wr8APgZksBs-lq6Ape7YsbPeC19hGqf5Vd0QPyztAQvzCpPlQ1bt-Txi66r0wv5yRz-jOCvyMWEG1YggzUSlfikppgo4mLeiAA_qjSLeOpsTI3MYbqtqtGogzEQ7f0Cmt9kIQiKqvYASTp_TySP9EixLPzOuIhrGQXr7V7es8aE24eqgLahPhO7WCXJW33WV0o-PiAYd2hNLFKC5R8I7LPxTvBed2BaflY0jVNkUPgyw_okpEDFOKzU3BzkeEKNmXNgVV2TH0DKy39ueaZXCDvJgFgXL355Wl6-b9zegL8RMWaeUbNSQK3IyPbFk6DIWa-1ljMbySJMQwJhJwpYTMskeVC8q8oqTf3aAhi6DBF74HCe_ICosnVb2JlnvwumtQTaDH24mIX8xOetLJlShqp0LFbn40urfxqfeXdO_94_Rpb_FKy9IYbUnCDcly7aqbu69zSDuCBzNY5IGWeMgsCeoleaA7aBkxv52oahx3chy6rBD-MwqY-TJp7Oz0jIpgWwYMGXQjZ9T48IjnEQXU6MLzhhnToeAJGt_rs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Y4GeDhKJOnpGY6Elcmra0wWTkooOJRrZs4H6B9J6QBskvZj_SgP942uTBXE-6GPuhLFjBgKQ_WCucS_oeSAPbzAERcma10pmlQDOccZ6S0SBk7ogeX6b-QGxQZdyl4Vc7u1D1Wr8APgZksBs-lq6Ape7YsbPeC19hGqf5Vd0QPyztAQvzCpPlQ1bt-Txi66r0wv5yRz-jOCvyMWEG1YggzUSlfikppgo4mLeiAA_qjSLeOpsTI3MYbqtqtGogzEQ7f0Cmt9kIQiKqvYASTp_TySP9EixLPzOuIhrGQXr7V7es8aE24eqgLahPhO7WCXJW33WV0o-PiAYd2hNLFKC5R8I7LPxTvBed2BaflY0jVNkUPgyw_okpEDFOKzU3BzkeEKNmXNgVV2TH0DKy39ueaZXCDvJgFgXL355Wl6-b9zegL8RMWaeUbNSQK3IyPbFk6DIWa-1ljMbySJMQwJhJwpYTMskeVC8q8oqTf3aAhi6DBF74HCe_ICosnVb2JlnvwumtQTaDH24mIX8xOetLJlShqp0LFbn40urfxqfeXdO_94_Rpb_FKy9IYbUnCDcly7aqbu69zSDuCBzNY5IGWeMgsCeoleaA7aBkxv52oahx3chy6rBD-MwqY-TJp7Oz0jIpgWwYMGXQjZ9T48IjnEQXU6MLzhhnToeAJGt_rs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=vhm-0rOC713mDhGyI1I1FL0MSHzikwU58L_IDaW18NPZ_NV_PgbyxsDGLrzpxFca_AxZUIBB5EQsUjI0-i6ivh3NJ6udNq2zgCTm29wQe_z_q_nLsQ-ujV5MKOfvQHNp-89J-vlCIYcsgISRQqLglKY4Evro9iFNGW_Mo40JLgLSSIFfR2HcTkoUmzb6JIC0ZtwQSCnKHF04_gZF1-aYR-kxQr0nkU3C3dkgZBAEOYNbOsrnLWwnohPPLDrOCucY1XyD_LYpvMIn7O4PLOopz9q5B1-n8EiIvyB9I9UJUiaVrW-lrq2l4Z7zelOQNXwtld_hMA-N0vclnlrKhyJMZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=vhm-0rOC713mDhGyI1I1FL0MSHzikwU58L_IDaW18NPZ_NV_PgbyxsDGLrzpxFca_AxZUIBB5EQsUjI0-i6ivh3NJ6udNq2zgCTm29wQe_z_q_nLsQ-ujV5MKOfvQHNp-89J-vlCIYcsgISRQqLglKY4Evro9iFNGW_Mo40JLgLSSIFfR2HcTkoUmzb6JIC0ZtwQSCnKHF04_gZF1-aYR-kxQr0nkU3C3dkgZBAEOYNbOsrnLWwnohPPLDrOCucY1XyD_LYpvMIn7O4PLOopz9q5B1-n8EiIvyB9I9UJUiaVrW-lrq2l4Z7zelOQNXwtld_hMA-N0vclnlrKhyJMZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=amGF-qCBD2u2wdE8cy-7ElyP1vTU7JTN8a_AwBTYPSokZGfPWC2NIM0L6msTT0vR6qtPjcIQUM8GoIYnU0UkKszcT3h9cillxwAUMPEOqjT5y8TXJhaq4QHxCxUVuZqtxrE3co9g19pI_st1R8UxOydu4kVqzSHMG6IXqC3Ioj4x2MofDbWjdKVGAzH8feaSCdRTqjXDRg7SSUiY7NWDomcy9hPGicH--O33o94zbznareJZ9LghGxuHqlhBcnYL0LHFHZt5unkgLRbSoZ9-ZnSBCssezziyL1mtlBsqVgMyDDhRL2pUHx1Wqz9uPJlw4ydJpSugbbZ7x5pa1S6wVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=amGF-qCBD2u2wdE8cy-7ElyP1vTU7JTN8a_AwBTYPSokZGfPWC2NIM0L6msTT0vR6qtPjcIQUM8GoIYnU0UkKszcT3h9cillxwAUMPEOqjT5y8TXJhaq4QHxCxUVuZqtxrE3co9g19pI_st1R8UxOydu4kVqzSHMG6IXqC3Ioj4x2MofDbWjdKVGAzH8feaSCdRTqjXDRg7SSUiY7NWDomcy9hPGicH--O33o94zbznareJZ9LghGxuHqlhBcnYL0LHFHZt5unkgLRbSoZ9-ZnSBCssezziyL1mtlBsqVgMyDDhRL2pUHx1Wqz9uPJlw4ydJpSugbbZ7x5pa1S6wVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=cG6sc3Dh2-KKa3H--lNQRM9v-hTD7a9Qcpr5zxMaYLJ7raxMOh9aL84bXyrKFmUWhzqFE2l4IW2kapAiF2nYc8Jo75d7Yl6uGtCRqDpvIZuvtwRGSc2l3wZ1maal96jwcwc5l6m89rXDy3nzPph2dsKRlGV6lYs-xmGbqBfQlqwJvqb_6jFpfLWyEE3FJqGJLxWqAhxEqObhrWfSdH5HiWYko_JVBHO00E12-rAe4kjc0kgPJJFQajY_zbTvfb2lwuuRcwwXsO9XguBrLceV25lLWaSUxGjxMVV5xU7R9EavQOncnNZAotcoSnhUaU5P2O5Yva03YuFzLp1ggl5l4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=cG6sc3Dh2-KKa3H--lNQRM9v-hTD7a9Qcpr5zxMaYLJ7raxMOh9aL84bXyrKFmUWhzqFE2l4IW2kapAiF2nYc8Jo75d7Yl6uGtCRqDpvIZuvtwRGSc2l3wZ1maal96jwcwc5l6m89rXDy3nzPph2dsKRlGV6lYs-xmGbqBfQlqwJvqb_6jFpfLWyEE3FJqGJLxWqAhxEqObhrWfSdH5HiWYko_JVBHO00E12-rAe4kjc0kgPJJFQajY_zbTvfb2lwuuRcwwXsO9XguBrLceV25lLWaSUxGjxMVV5xU7R9EavQOncnNZAotcoSnhUaU5P2O5Yva03YuFzLp1ggl5l4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Usi_pvj99vqMV5UGKQfW_LGLIvmnfa1fzvCmckkAUeyAPLk89g-R2MZrMHVDR2_OAL73AkDFrWQP0PlTbArgb5WwBDEoc6HmaR1pFia1GrThSyBlzwDPogBwlPca5_O9tXvc6rJPl2AgLl8rbpU93yHyeGPxu7nlAD96eYXGsQMGB-KIKcYFAP8s9vD-yR5-nt_WULSNpaD9V4mPguAnEsnqqCDi6PDaY8UXOo6WmWt7hEPOl5_MF10XKr5fx8S7tfDnoKyynEZ0t8iR0y83KhGyJQX3oXX8iEmgE8E9ivLhJoUGuOljjZXBYpdt6sACuGMB5UvkYgtWnEKJL16Qbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=Usi_pvj99vqMV5UGKQfW_LGLIvmnfa1fzvCmckkAUeyAPLk89g-R2MZrMHVDR2_OAL73AkDFrWQP0PlTbArgb5WwBDEoc6HmaR1pFia1GrThSyBlzwDPogBwlPca5_O9tXvc6rJPl2AgLl8rbpU93yHyeGPxu7nlAD96eYXGsQMGB-KIKcYFAP8s9vD-yR5-nt_WULSNpaD9V4mPguAnEsnqqCDi6PDaY8UXOo6WmWt7hEPOl5_MF10XKr5fx8S7tfDnoKyynEZ0t8iR0y83KhGyJQX3oXX8iEmgE8E9ivLhJoUGuOljjZXBYpdt6sACuGMB5UvkYgtWnEKJL16Qbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=uddInA6rSTPsNmsV3sn01kCnqUx3cIPcyK92O_JsK6AOX8FcquwhEVvInQYC22Xj7Q-Z0Px_T3KqEfZsBgLBJVmcvFC40YGWwpTe6tlTKLe3DwBKJF9ng59pWpW9NXvZtKTbaOpdDQ1CKucBcpiOP6y-yVCq_BGiIxDDpYsHKm9BSUVfeOLmPoFDCECHa2UjK7KW4g5QovO7oi35SRzECMnlym3pxJQ3QmExKThlrGRCCva3J78yssynhQWNRWpeFhgZhMmSjy_rxRbGlnfg54mvbdVUZO_XYYGf-H9qn_6XHDtgVM4P8KD9KH1ayzuCTm6VvrBM2maqL9z7rSO5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=uddInA6rSTPsNmsV3sn01kCnqUx3cIPcyK92O_JsK6AOX8FcquwhEVvInQYC22Xj7Q-Z0Px_T3KqEfZsBgLBJVmcvFC40YGWwpTe6tlTKLe3DwBKJF9ng59pWpW9NXvZtKTbaOpdDQ1CKucBcpiOP6y-yVCq_BGiIxDDpYsHKm9BSUVfeOLmPoFDCECHa2UjK7KW4g5QovO7oi35SRzECMnlym3pxJQ3QmExKThlrGRCCva3J78yssynhQWNRWpeFhgZhMmSjy_rxRbGlnfg54mvbdVUZO_XYYGf-H9qn_6XHDtgVM4P8KD9KH1ayzuCTm6VvrBM2maqL9z7rSO5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=KdN6Ue2k9PRoFO727qq5Y0oHhOPtwExt08ULwRVlTxwgT3TmufpV_kHD_mITl6ejH2XCU4_jzFCeflJXhGpaG_MOFiD9IiSLuPr3AyMOSEyYqeoI034ntp6aaVDEXsuAN4tLmP22D7OKWCgbgwOr6oru6DLRZMGUuY5brx6qqn8wy3OEM72i8jRStYTLSFrYs794PNIhi7NqCN7bDJEfE9FUAxCZVUqs3vuW1y7eG9c7Wv5umwLeS25eM6TwdMkFZb7SgBe-GJUqGrEemCfTx6pAs5cekzOBbQ7o00xod3v_cEy3iAEWqkPVz3eBXG2DbeQBBNsnKr1rX4bTh3cqxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=KdN6Ue2k9PRoFO727qq5Y0oHhOPtwExt08ULwRVlTxwgT3TmufpV_kHD_mITl6ejH2XCU4_jzFCeflJXhGpaG_MOFiD9IiSLuPr3AyMOSEyYqeoI034ntp6aaVDEXsuAN4tLmP22D7OKWCgbgwOr6oru6DLRZMGUuY5brx6qqn8wy3OEM72i8jRStYTLSFrYs794PNIhi7NqCN7bDJEfE9FUAxCZVUqs3vuW1y7eG9c7Wv5umwLeS25eM6TwdMkFZb7SgBe-GJUqGrEemCfTx6pAs5cekzOBbQ7o00xod3v_cEy3iAEWqkPVz3eBXG2DbeQBBNsnKr1rX4bTh3cqxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=IkwG7tNgL7tm7y2UOucvrPcXDe1MYQnnr6qyB_6Fh0vOwjG0aL_19s4vIUJAb9mLzJltsCpZ54wYd12oITlWrJAO8KwXWqNuX1YXbvh0ZC_kYtfC6yAQHiJ_CUsUqGXLavMdmpF3viwyqI8CUzPUxaWZpYSGOP7wjbxHK9yMoSIg7E42x8wzra72Wvh7f0RBJx3Fjbx__5lI5mstc7uIYL94DYpHj9YzlJtz3H2BkDMQ9t7nSp0lyQ0_7664VCWnsO34lnma93_MwP9pNjMjFbHwYniK02TLerSkWxnVgF0zTJ3bNRKzs2S08tIza5fkCv04n1nKyyVne_J_wNKxpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=IkwG7tNgL7tm7y2UOucvrPcXDe1MYQnnr6qyB_6Fh0vOwjG0aL_19s4vIUJAb9mLzJltsCpZ54wYd12oITlWrJAO8KwXWqNuX1YXbvh0ZC_kYtfC6yAQHiJ_CUsUqGXLavMdmpF3viwyqI8CUzPUxaWZpYSGOP7wjbxHK9yMoSIg7E42x8wzra72Wvh7f0RBJx3Fjbx__5lI5mstc7uIYL94DYpHj9YzlJtz3H2BkDMQ9t7nSp0lyQ0_7664VCWnsO34lnma93_MwP9pNjMjFbHwYniK02TLerSkWxnVgF0zTJ3bNRKzs2S08tIza5fkCv04n1nKyyVne_J_wNKxpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYdSNs-kdMHK-evC5int2kU8rkZrPXAHynqEz57u8wg84z650yr8Y1yqxTfmulyb4pUbnKHfZpAdH9tiRCn6YRTCpmClBkfvTTZ_WxAVMHyhb3s4XqwT56Uzb-iWSqXHpw-40CnrV4jDFPTsGBDdL6X8q8GykGZJaiyWsrOcV-MV3xhfQ6iQXr-tJN05lpiD9mpGhTijnlQtuiIugC5rG1PDGcE1GvMPHWokVn_3n9lIMJ5ms1SB-WG7-sEVHy8ePuqTDlONb1sxgFatS0_IRGcuWaLKgznms6ciGEGkAwVdUKbVLC3kcD3PeymWH_4oxIgldy5H5ziN2q2aHqHFtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=e6iyobEk_AIkxybmkXYOhJUTo1Is__Do4Khp-8FgNtQBs7kSq_EAo-nTbAlJOOXYPXVIXz6M5ZrKWcPltsqpxnMEGouehDAJNuVf-P1c-z2ygwgXozDhPCfyR1cVQAUQu1PS0KG0H6-DlT_4JAfehG6QL3JEt2zGXjCduv38RMV_XOmUTE_m-zM8KZOdhG0sstLtNQFFOa_H4KeUX1PykLa0TUeeEa0cn_-QYvimXa7Yr9AM5wAfG5qH6mOZPLMnsTTde1to5f_KbS8cJYSWXELxHASA6VklpBh5L_qQJIhRhDybRl1eooTqpRQjqPDNtYqXBDd4NJOWjuYd7WAz5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=e6iyobEk_AIkxybmkXYOhJUTo1Is__Do4Khp-8FgNtQBs7kSq_EAo-nTbAlJOOXYPXVIXz6M5ZrKWcPltsqpxnMEGouehDAJNuVf-P1c-z2ygwgXozDhPCfyR1cVQAUQu1PS0KG0H6-DlT_4JAfehG6QL3JEt2zGXjCduv38RMV_XOmUTE_m-zM8KZOdhG0sstLtNQFFOa_H4KeUX1PykLa0TUeeEa0cn_-QYvimXa7Yr9AM5wAfG5qH6mOZPLMnsTTde1to5f_KbS8cJYSWXELxHASA6VklpBh5L_qQJIhRhDybRl1eooTqpRQjqPDNtYqXBDd4NJOWjuYd7WAz5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UrYjqvBnlosvdr6cyxRYswN0cNKlDGRAcIN2Zf9ld3E1iDiG8e61rP1hD8yD83MenHVaDVdWkSumNDiw536nmJq-L-18snDq-xcFoiEUvjGHZ040hmkL-pn6K8hyIdR0KLHt3S0XVeG_kGEsUbzW2RD-RXtkuETmT2Mt1kYFALP_qAFh8uuUWtv23FWIXKbD1eaFyeA9DbZqrUi-sZOz8NPvRhdIoEj5rlDxNP9eSmNGsbObUp2_BLzKVJ9lWLyq6zxEGtfvBIF6X1RGB-G9fNF6aaruwmwt0tYql5yItOorgklfgkysOoCW_WsEf1M2CblsUW0VAnCPwHAddLXbNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=UrYjqvBnlosvdr6cyxRYswN0cNKlDGRAcIN2Zf9ld3E1iDiG8e61rP1hD8yD83MenHVaDVdWkSumNDiw536nmJq-L-18snDq-xcFoiEUvjGHZ040hmkL-pn6K8hyIdR0KLHt3S0XVeG_kGEsUbzW2RD-RXtkuETmT2Mt1kYFALP_qAFh8uuUWtv23FWIXKbD1eaFyeA9DbZqrUi-sZOz8NPvRhdIoEj5rlDxNP9eSmNGsbObUp2_BLzKVJ9lWLyq6zxEGtfvBIF6X1RGB-G9fNF6aaruwmwt0tYql5yItOorgklfgkysOoCW_WsEf1M2CblsUW0VAnCPwHAddLXbNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=unyoRgXgbbtiV_VAIuR9G1l0m0Ua1gqbF0rXj9typBrc2xaX_LiI9-gOX_tKEBOBA3XcNIo4tqNYeJvOWRQpqVasqLt8enVbHNPC4s8cSMtwm0cHDuRX2LewENpedRoL5GiTM_WCUAMLoLMi5G273BmNQ7iC4RiIGHwsZYEFgCNegQFx3Eu4rknyq8drYN7woIIhL496N_YGSLI-PayEPvoa_Bnx7EVJfnUGuEFdfV9KIIgHylsmnv7G9TQz3WjZWYja8eGFusvNPQJATSVxrKNKB9qfkbH8AxXw0seo_ll22Q5Zw7LVKU7aqtsWJLWGdcLuAyM2kFVHxu2uAatU8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=unyoRgXgbbtiV_VAIuR9G1l0m0Ua1gqbF0rXj9typBrc2xaX_LiI9-gOX_tKEBOBA3XcNIo4tqNYeJvOWRQpqVasqLt8enVbHNPC4s8cSMtwm0cHDuRX2LewENpedRoL5GiTM_WCUAMLoLMi5G273BmNQ7iC4RiIGHwsZYEFgCNegQFx3Eu4rknyq8drYN7woIIhL496N_YGSLI-PayEPvoa_Bnx7EVJfnUGuEFdfV9KIIgHylsmnv7G9TQz3WjZWYja8eGFusvNPQJATSVxrKNKB9qfkbH8AxXw0seo_ll22Q5Zw7LVKU7aqtsWJLWGdcLuAyM2kFVHxu2uAatU8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=bVV84rq3Ks1yHWh6kW2lSuzdo3jwVCrUpEHPolr3t4iQSXViN36AAk3plSDgYXkeE8T5M29WqC2EjozdGa2bAyHxMjKOwJMXHwo6paGQx9K2UDkOTVBOWGJEAxm_nNUkeLUeYrcMchGyWafM8rebQqHbP5OkGbEzJBsYXiyxi60lFG2WYbyejN1y05gWrYnWhfalp4onczYjX8L8g59tTXzKSYf-zpEdoSQpC9kJ_WtrMIeebskVnyRdA-tu3HlgM9JLs2y3Z3lRapmaxZxa_Y-9gRGetvUSGcPrLy0QgScGVbmTv7t7uS-c4TSD2EG3fFe_4-r66w7hFZBr7pxrBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=bVV84rq3Ks1yHWh6kW2lSuzdo3jwVCrUpEHPolr3t4iQSXViN36AAk3plSDgYXkeE8T5M29WqC2EjozdGa2bAyHxMjKOwJMXHwo6paGQx9K2UDkOTVBOWGJEAxm_nNUkeLUeYrcMchGyWafM8rebQqHbP5OkGbEzJBsYXiyxi60lFG2WYbyejN1y05gWrYnWhfalp4onczYjX8L8g59tTXzKSYf-zpEdoSQpC9kJ_WtrMIeebskVnyRdA-tu3HlgM9JLs2y3Z3lRapmaxZxa_Y-9gRGetvUSGcPrLy0QgScGVbmTv7t7uS-c4TSD2EG3fFe_4-r66w7hFZBr7pxrBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzHbNgIKbqJUwJeFqtFNyXTSYQHBhBO9BRHkBMuOcDVZEcvMfxf-H1vK-y8Xj01Jx94uWh-iucUpqdwdFbCHiFOdqovniqAkik8rpbG9RSqEKfPYJOtlYgkjwvTriJdoqw3mfxv01Bct_1eMptEJwRcMK2PP8-_V-H9q1F4Fi_v5kN_LWz52ynKPp-4hFKBYdBB1oNM5VHLRxQl13fD9q7L0spDWr6lPfY9mTh_ARiL5F5_HPYhX6kPW-k-XtMXo8jwF4H9TDN9WC9q4i91QtrrZF33256Btg7mC2S34LGu3NKJYPs0lANPd7V5lofcYZ6mvznm3mCYzEk_Azlmd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=VE5xFuGb563R17gJZHRd472NpzrE-OWcJ-drL2j43jKOVwdgvK2__pZpnDIHOeRucy2rpWhgYkiaRBaA3unOFUiuExJpjiG3fVlvv489Rf7ciN6Nb5xi9By4ouOKrzFOgdJvJn71_-_2GcoJu6YkrZjVXgOmsGpIoH_weiFpU1ic5QV78Gwt06sfGs-j-ycPSTAY0lmuKEnXAkpV2J3p06qmoX2mmKy_E05fJpQ9tsMApo6B7eELZAXvrISnJp7lhjvQu5RYSOIW5qC2jVTeM9qgXQ986QCBfFTDz-2go2SqC72S--Ml90BIfjs0P2ofO6PMMusL-M7fyEj00eGfhoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=VE5xFuGb563R17gJZHRd472NpzrE-OWcJ-drL2j43jKOVwdgvK2__pZpnDIHOeRucy2rpWhgYkiaRBaA3unOFUiuExJpjiG3fVlvv489Rf7ciN6Nb5xi9By4ouOKrzFOgdJvJn71_-_2GcoJu6YkrZjVXgOmsGpIoH_weiFpU1ic5QV78Gwt06sfGs-j-ycPSTAY0lmuKEnXAkpV2J3p06qmoX2mmKy_E05fJpQ9tsMApo6B7eELZAXvrISnJp7lhjvQu5RYSOIW5qC2jVTeM9qgXQ986QCBfFTDz-2go2SqC72S--Ml90BIfjs0P2ofO6PMMusL-M7fyEj00eGfhoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=aDZI3PHGnR7WwTrqP4axN3Uj3N-WpIDM7_HR0Mjok2eQt0I3Tqr63J3bLKyQllWFOsTQ4OxaPkSvEDnIK8Jda1Kn5dLaltlRd7YuTgCbI-6AThXztUTlUSiV_9IYd-CL-v-C2pQXBtLFqgGQX4zaoQcVerTfZtVzZgRmCDrZyz4mPjqkfOmNuftlHwRQDGFSSzva2pH14XgCGq3YqW0WsGp51wl9NFV3_3SYkdShXxZDxACYfLhufvPwsclz3nPho-3tp2SgyhtZk1G5oOH8NlHw7F_-KotzHy8xhd0acldSxRaMjxFg6kFyI7q8dKRS05K036bnggCairAEHhZk6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=aDZI3PHGnR7WwTrqP4axN3Uj3N-WpIDM7_HR0Mjok2eQt0I3Tqr63J3bLKyQllWFOsTQ4OxaPkSvEDnIK8Jda1Kn5dLaltlRd7YuTgCbI-6AThXztUTlUSiV_9IYd-CL-v-C2pQXBtLFqgGQX4zaoQcVerTfZtVzZgRmCDrZyz4mPjqkfOmNuftlHwRQDGFSSzva2pH14XgCGq3YqW0WsGp51wl9NFV3_3SYkdShXxZDxACYfLhufvPwsclz3nPho-3tp2SgyhtZk1G5oOH8NlHw7F_-KotzHy8xhd0acldSxRaMjxFg6kFyI7q8dKRS05K036bnggCairAEHhZk6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VrBRCZhXhN93EcbdhTghARSdoAEYkxuRci-J1RBiAdMvQYkiztQ0CM2gnet43p1KIsweOXcwLLyMk7zKV3MIriCoaHm9EaLbYOoYcNUvUfAqubgCoPypshRw7GrI51MXjWH5z3T2n9iBgr2LMaJAa1Oontes3GUfRWpBirnaTq1JpYax14_7qyLSBzPNQ1rVnPiKfT-N6tdVG0IKNJRzRhaTQ3SiMx0vvIX-huijjc8chldSnGsh0lPnz7YGb9mPj9s-9u9E9P1zI7mLU5moxGXZiOSZhbVma3vQ0D98wBsKdq6gimHbVcK0VtTrqm1SDbe71S16kgBeAv773tsB_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XgYICRtvs7HRjcUAy_ZBwsYtko-ciQUghiX4BPApbiXe5DeImH1UXxpq74Fu_fBwerKLZBWPyoCToA0gqkb2aLv7iEERnYnI4HkJES89A4SperEf5aGRu5fQWKWcSDmNIYOOLbjxSWACf1BceLMY9tmeAjHzOqJSMmbJByHKWzjGKnD-FDSYx9HdoNSXRkkoF3QLiFxQrp42om4_5eayoRDAV8HARQX_6vBALmpkYV6QQ-6e6wBtsv263WxlsJRisKCWgUdzMo5xLLDqln4-v48FcsRdgJgxer2OcUFDRs25fgmfvmXyZkGOT_hb8bGLqJrnmLQIjth0TRKPhv-ihw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=P2kulqP6ybv10IjffqExmV5ROnAzbhNrzdBYu8HLv2gA5BsEQ71u3MpC72Ah3plv5m4_xQ3ieiL_yUin2u6GaKs_knxcyP342IC3LdDd696QbRGqaE9BY6Y9T6tF2I8svEOjQiT19H4tMQJPp9icOyp-QXJkktcTuE6bmXiT4qV4Ppjq21z_uqWGKiGTj9pNBX_kZKxbDE_9vajus2a09f-oQ6Cqv7ngVB2uc5Yvnh5et6nLD_Lfs7cy_9WF3Oz633PSyUcX-e0jbMz2UxseyXG-BtS1AumFwZ4HgVe9A09bE-kgBByhvL0dsGcsy8KA9FS5DG5jB6DtmjiE-O9qdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=P2kulqP6ybv10IjffqExmV5ROnAzbhNrzdBYu8HLv2gA5BsEQ71u3MpC72Ah3plv5m4_xQ3ieiL_yUin2u6GaKs_knxcyP342IC3LdDd696QbRGqaE9BY6Y9T6tF2I8svEOjQiT19H4tMQJPp9icOyp-QXJkktcTuE6bmXiT4qV4Ppjq21z_uqWGKiGTj9pNBX_kZKxbDE_9vajus2a09f-oQ6Cqv7ngVB2uc5Yvnh5et6nLD_Lfs7cy_9WF3Oz633PSyUcX-e0jbMz2UxseyXG-BtS1AumFwZ4HgVe9A09bE-kgBByhvL0dsGcsy8KA9FS5DG5jB6DtmjiE-O9qdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRZUqFii5Y3Sdz4PYFn572EWpugW_hcQAFqG2wByT5UJSPAHIT2gxSYouXlYvxRqBI-tHPnUOZ-zwOmMIasF-_xH80LFEM3jebLI_W0w0RvStxWNQXDU-nB_ooq2tLJAaVTXCYlEICoLku_YmhStzRwifpFMwX8YPeYNj4MLoHKsGJP_Q_pXjj5lIR5ORQIGk8o3LjiMxQN0boXAkkKYIh4BpbSqQiG0sOyTYGlSvJKLrC3OqXGbmOevRWUU8GriKDrOBMzwcKEc7N-8kyENCPymdqwNzYImOpM7wHnSF4tGXJ90GcjXmwdmL2Ojb97jpK9ame-kKh_Ng0PlshJzBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
