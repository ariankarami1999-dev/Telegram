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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 21:42:35</div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/6804" target="_blank">📅 15:30 · 16 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUzlKjZUcbYA4IzdPxIuqKtpY7J0OoehndKL3r7HbJ9OtUWmS6GOVEyZOkjyH2xFjP2vwd6ziUunNT8C4yuwZKr0x-L67w7VniZXRGw7aMeZaccsqh18IJo2ouWDUGnRa51ffJRWXJjdXuZxua4p-ZnPZGIVk5Z-e9NwJHB9UX4p8Od3ZQaPyG2EKAqd4WsxHZwzarbDgXqBMTcmhgiI2JhnERIXVj5m33gIplTkDHtZtYcWBLqcAHDH8kW4tGwPU6lTtw1ejIpL7N-PRtJLkYu-fh3bQ5ueBHTFueQEg2h9f-PAnxxz4z44YScM2Ti6ul0Q9FVj-ahyREm-r8tHbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sW9IUlZBXrTPkik42qPcrrqnoZWQXvi1GSgRjC1tckaEyTC4IHl6ZgzractlFw30s58-BfLEJWXxtl1_mrmlLfn4Geiy4gMF1wGewkaaeYE4AKYGRi8WtY9JJOiuKtwLXt1hw2_AUknp-PMM8lJmdKh9bFpEponQ1MP2fJ4lXQR9rO7YJcykgTImv3Eb5wLFapymDdHX0r6tHytD2pbH0Y995094UCoUE1Omx9rGtunkrS7jid32P_M2IAM1ydHarh21E4OaqL3WQvyXaBoe7fSXnNyME24mLjTJg2P3kjOxQBAYMBcMz0Gkirk3O0uA1Z0HqJmspZxxZUYCe08S3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NFGxiQ6iwOKBE9yZ2V3yn--wlnJsbYnSlYHl7LIdChdEt9PwKB3vsSX82l8Vpb8SYQlFYC4HhRLokkW02LXjKllztrmC7Et9ESRVyrPMNVYFOAm3K16ONhVyDQnGjLZXqvKcAg8vfaYvxDkf77oD_yR4e0Jwr5foa0Ej42SA0vvrLOjiSYl7nOxtsk0yhbZJnWUD53UDL25MxiMDQ4gjVTFFtxnNQa1SMYQ1JUuI3KiO3HlXKEHilgPJoX18iKKEpfIqDd5ENFr2p80JCNTpHwZZAcO8sFjDGtOXCcGnHzr_jeoLpWtp_skQnaByuB_5E4Te5-GXLr-7uywUnIW-0w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4BSPmaH5P__Rp5Hf040jODtY0SEUPFVBXSrmkotIKB_K_hqiPrzI0-K-2X_DAaj1wkLTWCJYehF7zS7OkmHauaOSgrFZSgJJhGyPbfijV8BCgnnVGudubNMDaW6A0GkC42fZDI5Efrl48uaeTHa3DeGyIKdhBwtvONuS74cJDZZZh7tw36wO091Q7h1g223DNNUlQVxeQubCVObppO0Ti80mp5caUGk4zl9SvaZqzlUTV9b1_KPXvFT_3Dfj9kIFHapxFEk74TKMf8XUAHfEjShEKTEd4pHO_elqtXDy-BU7-EAhmAJsJX7mJ6RwxhRxMIIiLDzGESYq-Ic3_iupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=mnwbvAxhKzJAlQNYFHvKBNVPZpKQCO2p99RYvr4ncYAmzZPf7vticeZrpWg8dVtPr46U6iB4NJqoBiLtrv8otlxhG-BB90jK0VNPhje46QTR4sReJEhK_-wfUE8j5xcPceQLjj-cSYW6gs7zSnqZxXYREYdfbwFPR-dvrKYAYQ9iypx5scQU6KrBzZ5ncfD4erL1eWd9QjrrDlRCDuixNnfDEwb-B0UeFUA-AQTEc_y4G-NEYhJF59ut7jBwu7ZqMS5vJRfeyWeg3UDOUXX6zsetyZ814zBZ8gNZsHjJSHbfXwaJpaH4q3U3K3M3lQcPGPB8wSKQjACFvsnxsPcqqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=mnwbvAxhKzJAlQNYFHvKBNVPZpKQCO2p99RYvr4ncYAmzZPf7vticeZrpWg8dVtPr46U6iB4NJqoBiLtrv8otlxhG-BB90jK0VNPhje46QTR4sReJEhK_-wfUE8j5xcPceQLjj-cSYW6gs7zSnqZxXYREYdfbwFPR-dvrKYAYQ9iypx5scQU6KrBzZ5ncfD4erL1eWd9QjrrDlRCDuixNnfDEwb-B0UeFUA-AQTEc_y4G-NEYhJF59ut7jBwu7ZqMS5vJRfeyWeg3UDOUXX6zsetyZ814zBZ8gNZsHjJSHbfXwaJpaH4q3U3K3M3lQcPGPB8wSKQjACFvsnxsPcqqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=rgs7hK7E6bo5ld53zGqNJgkVoV3CQVpeu8TDuWV3ymy4g5LhCgiKa5HwZRmInX_tNZ6oUOa7-e102sxe3wLyEhNEoaoF6TGSikayWGHQ9TEjqpK5-uC9d3tgqT21huToSkvacRsKwPQHHoVZrMkns33dcMt_IdY-PU3t-UMmEZBSnlE4NV3hOe06TYjs3ic7QyUu4GX0vt4LKZ3iSxzkcbdYu30zc8o5k6lKBlBacpTXhl96hS7JfDxkctsdSc_OVTbbwtxe04gT-YFvaAm0VUoq-jopTG_GciIxnqTHbDCynnj2PXjxSh-TNJmuX9IVFJA6lUnxU6l3bKs_JnFbjacTJcD5GT-WgQcOnPklc9oZgmXHSFtSmIKqj7pCEeQPWsQSNwK_uLcILrTD_45KWisfmD5Es5DOpwSJYNrGbmvo4xDvNR5jhNqPux41lBhcsrT6kX3FLB5lRsWmSl308PLJ9fGgo-0dGFnFTK22CXabcmzNLcVypNHes5PWJkqXdS2u7W8JgJI9_wxGYQPDcwY9UhhNch-yagLr0F0xgccx8n32eNCELdXlTE6qYial4ZgUkZA0CLFNz_Le0-tAkX5uuVi5ICLvFowqyR71Uk97rfptWaq5V5Gy1hDTAKKZBKMXZTCQYJpH1ex06wTVBPn7BxYACauSHzjCMN5vMaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=rgs7hK7E6bo5ld53zGqNJgkVoV3CQVpeu8TDuWV3ymy4g5LhCgiKa5HwZRmInX_tNZ6oUOa7-e102sxe3wLyEhNEoaoF6TGSikayWGHQ9TEjqpK5-uC9d3tgqT21huToSkvacRsKwPQHHoVZrMkns33dcMt_IdY-PU3t-UMmEZBSnlE4NV3hOe06TYjs3ic7QyUu4GX0vt4LKZ3iSxzkcbdYu30zc8o5k6lKBlBacpTXhl96hS7JfDxkctsdSc_OVTbbwtxe04gT-YFvaAm0VUoq-jopTG_GciIxnqTHbDCynnj2PXjxSh-TNJmuX9IVFJA6lUnxU6l3bKs_JnFbjacTJcD5GT-WgQcOnPklc9oZgmXHSFtSmIKqj7pCEeQPWsQSNwK_uLcILrTD_45KWisfmD5Es5DOpwSJYNrGbmvo4xDvNR5jhNqPux41lBhcsrT6kX3FLB5lRsWmSl308PLJ9fGgo-0dGFnFTK22CXabcmzNLcVypNHes5PWJkqXdS2u7W8JgJI9_wxGYQPDcwY9UhhNch-yagLr0F0xgccx8n32eNCELdXlTE6qYial4ZgUkZA0CLFNz_Le0-tAkX5uuVi5ICLvFowqyR71Uk97rfptWaq5V5Gy1hDTAKKZBKMXZTCQYJpH1ex06wTVBPn7BxYACauSHzjCMN5vMaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BfpTbyWXhILCmZvNzWJiek0TLSyADDwb7FCxtHrW6uEzD0mnQimLrmigyH3ULe_YMRSqX4YbrF88I1EKsW6d5EJZCU5sH9-PDTQxw9UUlmITexTWRD-hliaRnUnyBHrCLredCJrA5IeQzFuAdyc59f_c40SQlv_nz2Xt_9zOCj2TFsZGLnjPsSd9OwbgvtBGxCx12p5Z6zb4t5tTJMiX1eNJjWj2h6oAeFUSSD1SNVK1NcOshV8QMORkJrO1twV61F1692sljra3Uxh1amZymHxHYFrWoB0mw7NZc_zDX0mpR91xuSOLmqS0hnecLrZS1lRXKExAstQECrrP6MVvUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGxtySyIHWLZNlWfbeRxURPv_bEUFqs8643ULZYYJ_iOCuCX_ceczpFWglUjsGSfg_iavQl5tXx5Ub751BF4RuS7pRRKejfSwRn6KfukRKZXSZZtf4FQke95lMkT6MM_Vo70NyPA9e1crRT88SGSHD6JNY7o2XEkdQ_3xWuGAnpP9SYpPcAQlVIsAn-iqZ_h96pi29D-5id2b5Az3wInVKRmg0nb4gG5A7HNLb5U-9Hz5LNh0-qz5kynpZNE2lqfWkea-GkLDmkKB4lcCtn-pRjIlje20JleUZXtehYaYXLJZipXKWorXX-RbjlcDDLF0OYKzUGW6DP-8_IZslj94A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GyeyP_P-hegTRDQRRGRuYdSyHwZv9V7SUXyPn8D-eKHy6Ew5N_f2_CIGXUhUbaL_X4YNPjLZ664oBNSukv3rsyoPjJFF7y1s_mDakq7HdRnwOrorYWo29ojMLXlHuqPwlUAKNhEYZM9NQayUsynEViJrnz2fm6eLCEIJCLl2kjuLDXulJMjDfkueIueGfayQ8ksyoCdi3wiHUcyhcCbDusMMZ9Y4XqADSq4aZX6SEpj3Ifqqj7af76g5yjTu8SoNUBSTYuzK9LMrPQXDmYMikKpt-6QLhijbTX5RBjNs6BU2majRiJDQ1E1qqjSUAzMfuT_jQs8Oe_4fu1E_0AtwnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=eKf9XpezTTv0X6QC2zvDPnx0BpCHdH_sVbWk3btSTle6H6NSD0L16EKNJBGL9yemWKc_jRV6O61vAD7P3uLYy7xqvjQzxon7UxO7yXEJ315Wdfx981_9CrRRsTFjHDZ5f1ruC_0LxWocQ6VlW0cCaCHhMOCq-q94vO1GMKsZxvcd8B0y1M_Z1IOv7ynAHwXdPMlFhKA23EMfKqYV1OrTFs8A-4rTMr2KtpPLUEkWdY2FGi_KfGn_6QBD1CvFk6SqhuhuZq4zVU1ZmQrloB9JAOv3WnwEnGWYL4zou7OwHonPZQsswInomH1xwHBhWnNaykIBsU3Dzha2QHmKSLv6VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=eKf9XpezTTv0X6QC2zvDPnx0BpCHdH_sVbWk3btSTle6H6NSD0L16EKNJBGL9yemWKc_jRV6O61vAD7P3uLYy7xqvjQzxon7UxO7yXEJ315Wdfx981_9CrRRsTFjHDZ5f1ruC_0LxWocQ6VlW0cCaCHhMOCq-q94vO1GMKsZxvcd8B0y1M_Z1IOv7ynAHwXdPMlFhKA23EMfKqYV1OrTFs8A-4rTMr2KtpPLUEkWdY2FGi_KfGn_6QBD1CvFk6SqhuhuZq4zVU1ZmQrloB9JAOv3WnwEnGWYL4zou7OwHonPZQsswInomH1xwHBhWnNaykIBsU3Dzha2QHmKSLv6VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=L9VrWrQMacfuRk8NqsH1CkDDBbDBbebNupKfZx1JO1tvVVjem-_Yenm5s2HxJ0qPCLX5EUIl7Z_2NcPWAf1H_Ntq6H7PGiX1zO6c5sErZK0HOa0m32IRhHqOjVlPyhwplHkj1fKIrTKSp2BJw1aGn2XaYNXYeM_pjEWFsFi9A8CZWFNkG5GhyuaGwu927DKq6YWppQhzVpe4KRINoIL7eCGLHXTztyLTZ95CwhcyspvEK1d6ec2JB_rNuDklR2i07Ma28ZdBBsuVR5ZdiXQidkm-nG77Y8K9VVfhgkiySN56DTwcz7MrRw_biKIYuZJ4TTaMiKZ5yPpqT1e0_nRIug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=L9VrWrQMacfuRk8NqsH1CkDDBbDBbebNupKfZx1JO1tvVVjem-_Yenm5s2HxJ0qPCLX5EUIl7Z_2NcPWAf1H_Ntq6H7PGiX1zO6c5sErZK0HOa0m32IRhHqOjVlPyhwplHkj1fKIrTKSp2BJw1aGn2XaYNXYeM_pjEWFsFi9A8CZWFNkG5GhyuaGwu927DKq6YWppQhzVpe4KRINoIL7eCGLHXTztyLTZ95CwhcyspvEK1d6ec2JB_rNuDklR2i07Ma28ZdBBsuVR5ZdiXQidkm-nG77Y8K9VVfhgkiySN56DTwcz7MrRw_biKIYuZJ4TTaMiKZ5yPpqT1e0_nRIug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wbh9Zb3TSkAcYD9Z0fi3C3OrDZ0w2Bk-Ae16rhQXj1FhJaySDugqyIidruuTFiwJlM1YCXlbJqw-_W9m3b1aLPtf6kUGI9lLSKIyNSay8KJi2YC2oTINfuNCDW37F8esVJLwCs1xrIRdpXiyCNporjXxDYKmoNBfYh5rJhm2HR64BSlzFTSslC9T90R0f4BckdhltyYglIF3CIfKfpmEFc5mjNrwBEFMG3dmN7gn01DWHMrGiqeaT07NIXbCIoUOJnHTn1b96MJSdWK6P2NXjLw9GewL8RZjwhNs1GpacsyfkutRxXVzpkuDvGPf1KTS62C485tic_PiFfGm9ADrng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=N-48roTvM0aExjFKiEvjz-E4SImndzlN8Qs9Q9jfH1IfyRV-8TK0t5xJqu8u0z3HuKu750GGjL-PRW5Aaos5f6n4qLbag7U47EScLEy2Q9qha3pYV1Gwsp4SsDjY5sH68rXtqHSHhVa__qZ5_pOziwAOPypBhYv9b8YwOpvSEJmiL1aXnjLbbzY3osunoOX1TJdgKBTUC4mrYplSshSBQgQS_cIvnjIZS987x9TPncBCwZQFNomXxzDE6IAPtWawjnt598qbydD9Jvbl2BcohhiKsPj1xvAm5dcXh5oFj9KLkpDnurGI7w867j4i3TSJSgXfGvqQITpe-qXh205_q1HzCQQ0fMXQ2BDSS7DK_vqNq3ONiXjsYo4ne-r73bjSLKK4G6IgoZumNXq3VfQhN34BRvEaMWsNifQmIG3YApZs3mAfVv86NpDrlfqhnbYBGrG1m7S6iIfqrJDqLMeXRJxvAMUt1ur6Xh78XteMxwN5X6VO3QnWAFGQCDJ-MjTLyufbDhWhjNG_qqMQsXd8-0Q4JHz-Xs7wWLExrZHBlcVMeBX5HpP31T-GbW4oocKjCkNrsxx9n8ZGOK8J-ZYzAiz2T6dMzJKZoPGCsl863vYM-omnraNB4diJwqp7T9EYRAy4q9wiKshoa4NQdsaeruuw4OrEsy4Mm-iOaeNodE4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=N-48roTvM0aExjFKiEvjz-E4SImndzlN8Qs9Q9jfH1IfyRV-8TK0t5xJqu8u0z3HuKu750GGjL-PRW5Aaos5f6n4qLbag7U47EScLEy2Q9qha3pYV1Gwsp4SsDjY5sH68rXtqHSHhVa__qZ5_pOziwAOPypBhYv9b8YwOpvSEJmiL1aXnjLbbzY3osunoOX1TJdgKBTUC4mrYplSshSBQgQS_cIvnjIZS987x9TPncBCwZQFNomXxzDE6IAPtWawjnt598qbydD9Jvbl2BcohhiKsPj1xvAm5dcXh5oFj9KLkpDnurGI7w867j4i3TSJSgXfGvqQITpe-qXh205_q1HzCQQ0fMXQ2BDSS7DK_vqNq3ONiXjsYo4ne-r73bjSLKK4G6IgoZumNXq3VfQhN34BRvEaMWsNifQmIG3YApZs3mAfVv86NpDrlfqhnbYBGrG1m7S6iIfqrJDqLMeXRJxvAMUt1ur6Xh78XteMxwN5X6VO3QnWAFGQCDJ-MjTLyufbDhWhjNG_qqMQsXd8-0Q4JHz-Xs7wWLExrZHBlcVMeBX5HpP31T-GbW4oocKjCkNrsxx9n8ZGOK8J-ZYzAiz2T6dMzJKZoPGCsl863vYM-omnraNB4diJwqp7T9EYRAy4q9wiKshoa4NQdsaeruuw4OrEsy4Mm-iOaeNodE4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=gtqGdd5_b3Taep6X7Au7Ua5rWisLyC7MXpU2r-G9mSfgg_o64x6HEqQaZyctKXrs0VGnSVL5RrJ467KGPtMSqGeX3qfu38WreN9l02UdbAicoDjSxvYZMBIYnHMPtyN6fuP0U8CcAdDQMLwD6wuS9ZZmzIaofHulc2fcJ_WrBAlQ8HbckYd2iybncFxsGpIil7UqmgdTjS2anDsnyzXB6Xf21JuEp-yNMW0pkhLvIXvQUS4eV21WMD92ZdP3DoiuwyItGqL79gzs2rabwKjod5GNCv3Xc4tU20XEDwl4Kdz-6GMfY4HEjrz6RL74U6QZ3DAJ5fumslkWxB3ksiDYQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=gtqGdd5_b3Taep6X7Au7Ua5rWisLyC7MXpU2r-G9mSfgg_o64x6HEqQaZyctKXrs0VGnSVL5RrJ467KGPtMSqGeX3qfu38WreN9l02UdbAicoDjSxvYZMBIYnHMPtyN6fuP0U8CcAdDQMLwD6wuS9ZZmzIaofHulc2fcJ_WrBAlQ8HbckYd2iybncFxsGpIil7UqmgdTjS2anDsnyzXB6Xf21JuEp-yNMW0pkhLvIXvQUS4eV21WMD92ZdP3DoiuwyItGqL79gzs2rabwKjod5GNCv3Xc4tU20XEDwl4Kdz-6GMfY4HEjrz6RL74U6QZ3DAJ5fumslkWxB3ksiDYQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJHIy-BQrbM-N2mHeJKs7VDhL6NAG5lDcWYxdya3eeKBSQZuLxyxqWO0FKMNmLgg49NNY4xfgy3n8iSzeLNzJM8PHpX32MWYE_CcAowKLrTOtHo9p5NQaHcYdx1lTfuWFVonwj-IlWsLnpMn84RO1nJYICM8V-eZLlIJImpKTUuqAusByuwbm95KKRU11d0almjXxzGUOUL87hCX1bf83XiWWX19rcDSxMkoulzoCiNRzzsHgWoKLePpnPRMWm36Sm19u1NgqFaC4OjZmh5B2d9bk-ZNmxrskoAiXwylpnRICYogtcZxUFXc5OWOVGSvfTYkCmXa5XIfwow_GzSJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=UgJWlILW3frHlEY8HheqLYovW8EmwwJDn8EDzNFZFNAuSg975zz3tFmuWo_I0qRzsrNZOTDxDhkRs46EmirfyHg-1gleULVhISfp8FkkdktOhCjh7nALSg5GSrdkA9YOQBa7i68dPYVqE-gE6meKkt0Mqdwl-JtTMIFItjlYjiAX3ieqhEWCWCsVO828Wtefc01P-R_9QOKlLPcuEhnCJeMuNNQGoT3BGFbOjmalSmqjNw8PV2hVYXmsMTY3e7e1KVKw3zn6XGE_m89d6w16VIn-_8agVjv3_jl5SdIJbs_poYiZYUYdEAdYkwN65cGU4QZPHrMtLbS0UeXNlENEXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=UgJWlILW3frHlEY8HheqLYovW8EmwwJDn8EDzNFZFNAuSg975zz3tFmuWo_I0qRzsrNZOTDxDhkRs46EmirfyHg-1gleULVhISfp8FkkdktOhCjh7nALSg5GSrdkA9YOQBa7i68dPYVqE-gE6meKkt0Mqdwl-JtTMIFItjlYjiAX3ieqhEWCWCsVO828Wtefc01P-R_9QOKlLPcuEhnCJeMuNNQGoT3BGFbOjmalSmqjNw8PV2hVYXmsMTY3e7e1KVKw3zn6XGE_m89d6w16VIn-_8agVjv3_jl5SdIJbs_poYiZYUYdEAdYkwN65cGU4QZPHrMtLbS0UeXNlENEXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhXCEPeibeLtcW_lxJueuuDUYt7uH2HkEeAacNwyaldpXaRk6KJn5gSnz-f-8mYxuHczNDQXKCev2jTLex3T860WYE_0NWIlSH5FknjqM9-8iToWLMSpx3rWlN_09TIriVX0b1sN3Fnm6sXfa2qQCzrWvLAjr2T3uX74eQZBsApds9ff-NPYxHcuTCtWAlvwwZlGGalxdKipPnAr6xNWvtsUgwOcBRljFuJAJYTXGNSkYleqxJOjG86AaCRSiMmKTnYFLvbqO7n2M0d9tr1ulec3r51863FI1ftfU3forawzukNs7J6WxzlEz1gMyWhs3lnTO3gUAtK7SQRwKuYUoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQm9TWqjUdkDZoGVuQhdMOo7chNUAd-eIw3Z3Dsyuh4p9bay2yjGoifXACf6oR3oBYVamIGvBuF4AF7FjbeMm_2bNOe7HW7CBWHcx306xmhCtI8hWUBkJMVOpS5Qlt8ayWNP8LMh4yYXpqMH-lPn8bQL-9I-81-ADTZ1SVixJ9Sd5-Mkn3wBcCO1WX5DnI8aUWAGBsmXszpiMPgX23W4BT0lNCqgpePiAvTwVRBeT-abTAxNfY6pUny8o0zoLMGpDXxSw_6gwU-bCXmGXFDgsNUppohYuJ7shbHFRUBHdkEETRW1f0WquEgk_LfaGT9qmDaJzFlvC0ULQlmqYkizKg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=kPDZfTfB1tsM3FkO67tpueYiNlLIQ1MDPq0Q1hJc06v5CAXkTaTXKRChCvLnmr3rWYtVdtN270XRgauy0940D6RQSTibmKQ3RDNVSbVayx9IGLUIJBkXcG5ys4pQvAznluKP9Fqmat6MC4KOx3rzWMAG7kHiy3q7b7BpC-eAP1c2urlKYlCIlG0B5isD4iX90wCf6FtSHIYA-RiokidfADQmH8GPVF_POuZ5kWV7BGbXL59vv4kjtlTSS9_UrFUAlRFZ5uCRkgYLH7sLGuNna-UV_uuCOnz20qTZDM0E-4VfMIYsaHbUAYa1PH48tRKTdznTdFK1OuJNYhmr71fAB2ycpL2K5QjV1a1mn6lC9Ppz6BC5W8_nLIThulmsVPboTrXB-G_0KJHWqAeTe9T26C8TurjHMbFOmkABgXG7UotLLaQUjFAIRyGglCVeapMmgcFFzDTSjgxhHw6r9eBDGuVwfOArnCQBiQPemeV_lBkCu-iAORoaUVcl9_XvDC29Ya3uK6O8f1MFyK2L9f_s942pmKB9yi0OZqgRNU4tS_qRpTIpF--nHriLxlbS0BxSnetmU9IwL1BitEsFyqqcy-VhEScyOPgl8NzfPEQD6ApKQjAedDX9HXYZEd2lDgpgcUPVNP_LjDmn7M_VpHnenGdeF4LFr6-owCFwLCmmdrE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=kPDZfTfB1tsM3FkO67tpueYiNlLIQ1MDPq0Q1hJc06v5CAXkTaTXKRChCvLnmr3rWYtVdtN270XRgauy0940D6RQSTibmKQ3RDNVSbVayx9IGLUIJBkXcG5ys4pQvAznluKP9Fqmat6MC4KOx3rzWMAG7kHiy3q7b7BpC-eAP1c2urlKYlCIlG0B5isD4iX90wCf6FtSHIYA-RiokidfADQmH8GPVF_POuZ5kWV7BGbXL59vv4kjtlTSS9_UrFUAlRFZ5uCRkgYLH7sLGuNna-UV_uuCOnz20qTZDM0E-4VfMIYsaHbUAYa1PH48tRKTdznTdFK1OuJNYhmr71fAB2ycpL2K5QjV1a1mn6lC9Ppz6BC5W8_nLIThulmsVPboTrXB-G_0KJHWqAeTe9T26C8TurjHMbFOmkABgXG7UotLLaQUjFAIRyGglCVeapMmgcFFzDTSjgxhHw6r9eBDGuVwfOArnCQBiQPemeV_lBkCu-iAORoaUVcl9_XvDC29Ya3uK6O8f1MFyK2L9f_s942pmKB9yi0OZqgRNU4tS_qRpTIpF--nHriLxlbS0BxSnetmU9IwL1BitEsFyqqcy-VhEScyOPgl8NzfPEQD6ApKQjAedDX9HXYZEd2lDgpgcUPVNP_LjDmn7M_VpHnenGdeF4LFr6-owCFwLCmmdrE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xh5SU5GntViMUv4e2nlYf2rhrRh2FV-Ey5L_R24vO1viTkwGony-CkAzO-dsnoZSgdHa601vMLup_abPYZjthjzt65Lv1oIaMaXULRABtFQIUH3Ih6IPuGo6Ty8P4GxrKb_Zz-DXV-prSzudCqLo_TTpKeFGv16ZOn9RdQW1ub3TA6-oB5vX04-fJVysT7uFa0ePOu58OJ4vzTdlL3W8mJ6YYJNvc1VM-sgkMcqlXihcSZrBXMLhbXwoSz8we9-2vdxy9K1CVPJfnT8dJx-_YqAjqxugJCn2XbFca2Xgjets3ClSHCOnHwHKf3K2EtpMmzRuBITS5OwcPAqQp1Fx2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSPOE0ofxwGjDBV06ZmsTLV9ouefVVeAjxUwbebw-npbGSCSEk1JVfnog42ZBYpWOFXvwNDm4wDmQt0oSI9_h5BIiAvhOO43-xvDszQiMsIcSRN5UE1rw5dKBu6lKIYauTXnMvRKL4pV3ShmawfavzmgXy7qIi3_3Lf_l77NgBLS5L_Z6GuctD3hbTp0YRb5tuEAW0abcPScCbISZD7Us1NxwtLQajfvs0uUoms04vXD_qzs35BoDz4BDRkz6vYS1o1Fi06dMSV057j1ZpuIzgCnq9F3WQwu5Qjrfi9sOC7PNgN5ZnFGBzXfWY2SLN7ktIZXnqVups_r8U3jxNJHvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=vbuTRKiKgQuEnUrYo62Lmo1D5WY-ND23oqxv1-OcuNAZvQykvhjWqTi8mHtPWr3pnTNMo6MoCrUSovK-z33S7h6JrigXZKsGUijUJQ5UDxrPOaFs6w2xEi0HFG5pOWVyGm1sLdHtlKPCmSnhNXk26VQ9FMHhl_es2ywuYOsFqzuHv3bP5AVxStRL0J8DaqnZHDJUt5_n-4_kNxolEtkMbXPRtKfAO0bzqWc5FJHeQ8mefx15Lg1P8uvFXmvOEdgDTdN-aJSMmgXqTjyq-gNsGB1frxlux43Jomj2iDB_XOGGXSoBvaDikQ1tVBZPvpP4-U7aQf_mRm7F1Dx69BStow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=vbuTRKiKgQuEnUrYo62Lmo1D5WY-ND23oqxv1-OcuNAZvQykvhjWqTi8mHtPWr3pnTNMo6MoCrUSovK-z33S7h6JrigXZKsGUijUJQ5UDxrPOaFs6w2xEi0HFG5pOWVyGm1sLdHtlKPCmSnhNXk26VQ9FMHhl_es2ywuYOsFqzuHv3bP5AVxStRL0J8DaqnZHDJUt5_n-4_kNxolEtkMbXPRtKfAO0bzqWc5FJHeQ8mefx15Lg1P8uvFXmvOEdgDTdN-aJSMmgXqTjyq-gNsGB1frxlux43Jomj2iDB_XOGGXSoBvaDikQ1tVBZPvpP4-U7aQf_mRm7F1Dx69BStow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=BcOfAPO0CC9JpdXpLqe7jvfaQJrp2kJq-Nq0rV70FRfzpHE8faALCIzSavfD3Yio5ba3JDbSgTU5eVLQCFJJU_RXnEw51s0F2QcwvJSknflejBGXjmOdwJDjnx_7-pjrrTScjvNBg5stLg4wbx5SYwCJKzk_mADFBVcnn5xbB7mttK1QMd0KK9oSwOvB2HAWqOgeLtMw8UVfOhLZTSr5GbMVqbYlfjaIqYDdsBB2P41J9vP6ggMYFetme8OOZdHix1Kh8Cg-dQs5B3OLyh9ymacv9CW-ihleUKnEYPBN9Q3pUO5QyAijO0dN45BNIdz5DJSrfV7n303No7MvZrnIPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=BcOfAPO0CC9JpdXpLqe7jvfaQJrp2kJq-Nq0rV70FRfzpHE8faALCIzSavfD3Yio5ba3JDbSgTU5eVLQCFJJU_RXnEw51s0F2QcwvJSknflejBGXjmOdwJDjnx_7-pjrrTScjvNBg5stLg4wbx5SYwCJKzk_mADFBVcnn5xbB7mttK1QMd0KK9oSwOvB2HAWqOgeLtMw8UVfOhLZTSr5GbMVqbYlfjaIqYDdsBB2P41J9vP6ggMYFetme8OOZdHix1Kh8Cg-dQs5B3OLyh9ymacv9CW-ihleUKnEYPBN9Q3pUO5QyAijO0dN45BNIdz5DJSrfV7n303No7MvZrnIPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=CvJ69Yd-bI7oTmcIxVcfPeg-6Gn1DENv8BCjgnjss7XYkj_ogPwsKVqFbT4jTotxxgBM0hgNSIMBqfS6J_Q2tmNSuo0TxtszQbKTJOzbgE2TWG3I1Ptt_bYbFTZt1Gr9cexthYm8fYHGXbilnCTstVzURNcfqD42ZdzejN7i62I4rVy68RoBndvknFi-sDb_Y2UEwqMsm9rYuiqG1atJGLm-e2IayfPBjpJCwIJaKvBr9o5khtDttl-wyf_v6lPoEUbNWL3LCpuBSIuNHNmpOuk5aYCewOLch83kd5EiVoKzWePfWLBhgGjhv0aH4Z59AImIIzi_JNS1eilAlcfX9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=CvJ69Yd-bI7oTmcIxVcfPeg-6Gn1DENv8BCjgnjss7XYkj_ogPwsKVqFbT4jTotxxgBM0hgNSIMBqfS6J_Q2tmNSuo0TxtszQbKTJOzbgE2TWG3I1Ptt_bYbFTZt1Gr9cexthYm8fYHGXbilnCTstVzURNcfqD42ZdzejN7i62I4rVy68RoBndvknFi-sDb_Y2UEwqMsm9rYuiqG1atJGLm-e2IayfPBjpJCwIJaKvBr9o5khtDttl-wyf_v6lPoEUbNWL3LCpuBSIuNHNmpOuk5aYCewOLch83kd5EiVoKzWePfWLBhgGjhv0aH4Z59AImIIzi_JNS1eilAlcfX9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWuOQNTXxMPojWcEM_Qi6jhC5XWtzhGR9Mz6KufhKxMzRTpOve-Bj7NNIuSEMf6UKu8UfwC0ODdjRYOWFWOaorjmjiaalRKEigF7oxb9wt9z4fBu7bc7LTctSU1CdCOcC_ZkEv8jgX6i3R9F7ktGjRf6NsURJzmg4_n5vYXDeCJCIv6BfTbihhGgIpjHWlkQCKfqbbmu0H4TDon22Oe4N1DjADO44GzNG1Ke_Zdp8OoB4w6rMCpfzaApkqiV9JLyFngHNfNOyy9sK0js_XSlj9TUzBQ1xIpBGUGc2v3IcwY_EQKAQc_5Dy13sppMkVuwfDOOKQWL2WT-NtYFKDre6g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro0J4o5vXUEzr_IWjMxKnCuhxH-6fIUW_MMpm5AbGPVfE59rVAqGvS1ilqas67_nJS40cRZn9rGZaozSRCg1PQPENkF_AsvwegqlzdQUo-63jmS0i6yxtRjEoovSLZc3mH243xb02rTz9Tgvrzugl5Zg7Y1kW8PSxQIhIgfbMBqqUerXzpclQ8Iv6iTeBI4SctH5VhvRCqyZAjQsY1W_pa9WzAw72IeFiNCzjCYs5iqrr6n-tE93jCNiNlnutPWb46nqNkx6WPEuUL4YrwXwaPWx-XdgMcVtKro12qAMoi61tw4uUffyreL0TX74XEMANQKBMCtvYmTFtTcd1EU4ugqI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=EfWAXC3-4Yvhj3Lxg0J3N7lrRB-cK4iZ3MJNILpdLfYokVh2EZ0y2k_Z_uAnLFKa5I3TvlBhm6iIigLl-VwPojnUogzOTMuhWTCmXEQkQuGbrQrkAwxv4mggbz59kXYoa1nhg6N5k0f7WJmArpP8tDzyZaDh7Gbw4MYsvQqHmyKF40JeGADugs9W8z_nYCZHSC4mHV5OHwRBZ6y1FuLCj_5uvcv9fmdrlNy_IvztYktNgnkJK5sg4pxdGJ3EzRrgilnr7jfjBZMohAtfpyebx_NcjAXBnpDDaqEVyLiJfT1_ymO3w1id-d-WAxy5aD_lVcCTdPhHkRRnftDzRUBro0J4o5vXUEzr_IWjMxKnCuhxH-6fIUW_MMpm5AbGPVfE59rVAqGvS1ilqas67_nJS40cRZn9rGZaozSRCg1PQPENkF_AsvwegqlzdQUo-63jmS0i6yxtRjEoovSLZc3mH243xb02rTz9Tgvrzugl5Zg7Y1kW8PSxQIhIgfbMBqqUerXzpclQ8Iv6iTeBI4SctH5VhvRCqyZAjQsY1W_pa9WzAw72IeFiNCzjCYs5iqrr6n-tE93jCNiNlnutPWb46nqNkx6WPEuUL4YrwXwaPWx-XdgMcVtKro12qAMoi61tw4uUffyreL0TX74XEMANQKBMCtvYmTFtTcd1EU4ugqI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=uN9D42OQZjQCTWrUAX1euNUZz0XYqJC-gT_DlBpikIs3OyXFQIpOuSRtrHmWDEZvTcp6GX0Vp2yDpO5XH0J3B0KmOACoHu6LWRjWsm5I7NK-RFs8CCA6t9n3N4lTASqCPRptKyjcSLHhlJA_-uaVder7eRKLAPaiEWzO4NDa0sa9Q6zhmxtUQ8D-eMbtXF54ZWsXFwUramk4_Xw7ncWJbKmpPSlQcmpj93YmWPMvT7CfJGEoFFEs_keJb9OLmZG6pxW573ixODHbEP-WZnISlwzs9pE5OWm7wMZi-g3c8sgMbBNSaCZXjhHWcgqEHyBQ1kL0h4N2SNuESLX7KlRA-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=uN9D42OQZjQCTWrUAX1euNUZz0XYqJC-gT_DlBpikIs3OyXFQIpOuSRtrHmWDEZvTcp6GX0Vp2yDpO5XH0J3B0KmOACoHu6LWRjWsm5I7NK-RFs8CCA6t9n3N4lTASqCPRptKyjcSLHhlJA_-uaVder7eRKLAPaiEWzO4NDa0sa9Q6zhmxtUQ8D-eMbtXF54ZWsXFwUramk4_Xw7ncWJbKmpPSlQcmpj93YmWPMvT7CfJGEoFFEs_keJb9OLmZG6pxW573ixODHbEP-WZnISlwzs9pE5OWm7wMZi-g3c8sgMbBNSaCZXjhHWcgqEHyBQ1kL0h4N2SNuESLX7KlRA-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQGH13Ir3nE3RKhseAOKCXkdVB2RcEfk3bT1_JjDPCJVPlqyPD7qcOD7F48Hmh-YLzecaNpUjUcAlrSBv9ddfZGGzLZpjJ-LW3QkB4UjDPbpizFC9yh8xHRWTAdRXcnjwzlYXwK2jNIATBEyJGWXzhx8Qqjtz1xevDQ1YPcHwweGRSDlx1ztPouRrZQx7lqU8h77eYNv8GU1SAxi-Nlriz3n1HTkX51LM8zk8DaQl8VH72gDl6ItXkTIYpcQOXBea5NgenN7-AnN-h3ya-WgOnmzMKbLvtfBcdmrJu-WRmqwZXBANoq_w7CirGHveLhRvnpdDdhunuifgS5YJvkYvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ZiMdnMvDa7LWOK9ufBUR0oG8GzU-t-3aF3q2byhRUi0Ja3Lr4RuexJ9_RhbX1Iibq1uTTr5DiGrXD4nbVQw403iOamFVWsU4U4FBQ9KHcMLe9eEQItJ7j-B-3CLH9uKaOuhxlpTaNlaUIHTSxV9VjOgJFhQpMBlZKKD26nz_hTl0OuOqEkj8kl4Q6l5iKpRmzrwibB-YNeZGw0gHU5RpSwjbcmKkUDzQ-lNaqkBOsgzV1lG-LmJNQLtVHu_Io8qua0XysFBD6HT-4KTps588k6AwetdaW6xOcvcKnFzlxuZiv4z06_rELJxxmrDwlowlmuOMPy3tUXgrw6AKajtBZ1PNro4KKjkn-2m0wLbby7Yvjrwcd-IwME190T0JLmvBc_9OT_GxKgBQWPEBPe4RgEvpYqiBmrMAS762GKpmKJnj5YdijAAUL5BMvHaUhQEgEAou21C9i5n06Od2gbMV2HbrPUogAmUnrjxkZBZaWYrmzwdMF7dBLPC8EnMaycNbAevO2T_ZjWaRm2O2qeyAJgxe7vsCWoyZKEB4Rvu2ufLe0fGMUrxfuzR69d0Idew5mvlgU_hXkCtdxb0Fom91-6ijNcU8w7mzrLi2qwltiiDxMoRk7z8QMI6k-059Irl9SIYIgdpn2UGLy70z90-v8LcVqaIsCgyg4WLLxKV_HiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=ZiMdnMvDa7LWOK9ufBUR0oG8GzU-t-3aF3q2byhRUi0Ja3Lr4RuexJ9_RhbX1Iibq1uTTr5DiGrXD4nbVQw403iOamFVWsU4U4FBQ9KHcMLe9eEQItJ7j-B-3CLH9uKaOuhxlpTaNlaUIHTSxV9VjOgJFhQpMBlZKKD26nz_hTl0OuOqEkj8kl4Q6l5iKpRmzrwibB-YNeZGw0gHU5RpSwjbcmKkUDzQ-lNaqkBOsgzV1lG-LmJNQLtVHu_Io8qua0XysFBD6HT-4KTps588k6AwetdaW6xOcvcKnFzlxuZiv4z06_rELJxxmrDwlowlmuOMPy3tUXgrw6AKajtBZ1PNro4KKjkn-2m0wLbby7Yvjrwcd-IwME190T0JLmvBc_9OT_GxKgBQWPEBPe4RgEvpYqiBmrMAS762GKpmKJnj5YdijAAUL5BMvHaUhQEgEAou21C9i5n06Od2gbMV2HbrPUogAmUnrjxkZBZaWYrmzwdMF7dBLPC8EnMaycNbAevO2T_ZjWaRm2O2qeyAJgxe7vsCWoyZKEB4Rvu2ufLe0fGMUrxfuzR69d0Idew5mvlgU_hXkCtdxb0Fom91-6ijNcU8w7mzrLi2qwltiiDxMoRk7z8QMI6k-059Irl9SIYIgdpn2UGLy70z90-v8LcVqaIsCgyg4WLLxKV_HiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df9w6-tSGn6aQeRSZ65QibW6rfk0QgBcOjUEd6Ec0TB-eyuTKWBaLXNRsFKIwEcAkpHNV97nalZyp2tjKYnW8AR99MTrjr_ZLvTaT2E1HkkkzAKyKwrCKG_zrL9iPXoz434_YNAICCyWpOEOOqOm9QwxDZ2MJonT82at4welG2fre0ks5fZt5CykheEvUNo5413Fq5vyqABvZ1Dj8Ekfyui9_4ALh23SPlUx35P4vYsN97Djt8jIzRO2MLF0eG-8eRindz61XfydmOpaghWKJyA7WCSr5F28Ih82jd0Rc2gIlTZla_GjMijBKpB0AJTp_7AGM7uYlzWdWikPAYr2Gg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JJ_By9YTF6i8oKlc_1SIgTeCC61BtVuFuBWzsLLibZn1RHMoHhWgGSLzroqmYyTk9NyLV5UEwgdbZqPFF3meQ38ZCZDlFEze-2tAtytCHovPP9ROner3W7e8g4r1FoY7yU34O7JSA738-Q0bxD5yb5_LWRyK93Tz1ub3wNSpu_lxO1_3IeaX-0NxE1siZiaME-IYx8NabouSpWjHcKV8XkiXX0SmCuO1E8HVFo3BNsUbClfStF2Ld-DvGmfCIfmhcgE5wqwd9kyvz3cbMFKCHvZ2CX1dn3mvB62CzOS5EYHnvdn986futlM1oBerstEO6vLa0Y456LgeAlDEFJ6xiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=JJ_By9YTF6i8oKlc_1SIgTeCC61BtVuFuBWzsLLibZn1RHMoHhWgGSLzroqmYyTk9NyLV5UEwgdbZqPFF3meQ38ZCZDlFEze-2tAtytCHovPP9ROner3W7e8g4r1FoY7yU34O7JSA738-Q0bxD5yb5_LWRyK93Tz1ub3wNSpu_lxO1_3IeaX-0NxE1siZiaME-IYx8NabouSpWjHcKV8XkiXX0SmCuO1E8HVFo3BNsUbClfStF2Ld-DvGmfCIfmhcgE5wqwd9kyvz3cbMFKCHvZ2CX1dn3mvB62CzOS5EYHnvdn986futlM1oBerstEO6vLa0Y456LgeAlDEFJ6xiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQzetZPXlxOSiaEUeeTqKQMrXt2oiBZ47e-TCX5DM_usAoLYM20VZiupmt-18R5WzSgf5qg3VrnI9SPS2o4TmmpCN2B2Ry2adAjUx9-4OLZd29NFGdawEmJaN87AfxGigkUzl9usuTPDVprkKdC1Les6ZMktSwrnGWdl2NhPzXJKaqcAjOP_NfWqZflw9oH5pOIipnBcGvM8r9JaeNR7xQbuMBW-hD30gQollo2wtWv__uCo5fz6YQNrwJOKMliRBwE9M03CjHDLn1QHkcAMKrgonoN91DlVjq_2dtJ_Zq4_BYA0GX5U5nDN9BPr2Oo58vK4xA-Qib316eVYCLqA5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ts1reGdOYVZ4GQ3O0fwXOGpFO1BgODB_Ud94AAMbAw2K-0K4fpXMlaPJyVy9Gx4HY4t0LfBjSWCBby8mFx51JhEYMRvXjWcK4tufsazELJKUUsPNIdbyFO_mrW_Ft9Z3WYiTctomwmj4gGo-gerYvA2DxhKydjZE5mrKkTx9ZRiRsP4vhNpktwRVOMzteGdrx0Ml0gTZoWGLC6aMKrdLjZuWGKI6r15jquGJnwjJHCEky5oChsIEedT5149pU11VGgzTn_XpIhKOnU4VpkPRaJ-v-HawO_TMipTRWa8gT9VRllh6dVTXgSPILzIbrth2xej7QZTZ-CvggMociqc5RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulbuaaZ1a_fpO2bLvpWVORu622Qx6-CZlAxt3ujysRohO88r5ec8ySemB0rymsS2Hz8Dn4ikFDVPj3O4qVG_dzdrkB_9y9I0Bwx4WrVbScsAUCGDRWhsYPCzn_VQ0En5cv1dDQEXVCgdry61iokIOOF3_hTvtU3UwBeIOw20QOiJkjM0qeIZusdxZnPgASC9ppVRXG96UBJ4vyy7FGv4F2igcEfDTKe8US9eeUcGRfbtygtLFgalMBVapsbakPFN_JFL3kZY5HopkN1qufG3ck7hMyODmoCGmR-NEnSKTt-D35B-HbNccAbN7xWdcLihnVjTch3RhoM1pV8rmtExpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=iWn915zVGXZlG-XUfsZ9aCu_QTpZqDzMZGTDB5_z0fGh2CRZh1KGecuoXR4dmsCiXRKSmBcyCA_ETnS6GuLf4sVHJ5g1G3n1K_0M6TSlxtkNWevv2cxwFuCMkEh9z5WQcV-A_-mfCe6hP0Nmh_9YuA4J7LCFweWEe9l8ma1t4PxZlF6KhdNap_Py4MxL1Jy4fNdWc2T6VPnZY1RHEOIMZnj9xLXUjixnxQLA1LOyXv_lNMotrynZ9YsA9dNss8PFAEfvvIf-5KzaBoZ1w6rHE-jaH20K1eleRr0liNc2X50EMtnhqE6WIBjMIgP8cmZUnX09Qk-4bIh-O17TrPC1Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=iWn915zVGXZlG-XUfsZ9aCu_QTpZqDzMZGTDB5_z0fGh2CRZh1KGecuoXR4dmsCiXRKSmBcyCA_ETnS6GuLf4sVHJ5g1G3n1K_0M6TSlxtkNWevv2cxwFuCMkEh9z5WQcV-A_-mfCe6hP0Nmh_9YuA4J7LCFweWEe9l8ma1t4PxZlF6KhdNap_Py4MxL1Jy4fNdWc2T6VPnZY1RHEOIMZnj9xLXUjixnxQLA1LOyXv_lNMotrynZ9YsA9dNss8PFAEfvvIf-5KzaBoZ1w6rHE-jaH20K1eleRr0liNc2X50EMtnhqE6WIBjMIgP8cmZUnX09Qk-4bIh-O17TrPC1Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeLa50Jy6wfVUaQdFXyH_dzbuRmSlZ_6mlOuo9BDWGDy1watxz4j0CB1CMeymHYVjMD1UtnrjEmBDMi6T354elQIJ7KUBuJsc9pWmMKy-xLcJCzfNmO8GiZwd1XKD2JBEgrYXNKCY3pQ8bhZbl6L0PG_IrQGwaPyZv2ES440mY-36lHGR6BaxzNivBcjG2ZpsnALMXGZ1guOV_a6W2A8R2qKLM2DSjOwTcVf-oafFYLDL44lUEvJuePQOLtLd9_oLajSh9xkWOCwtGSSsRO83Igwb52nyW9UwHZ71c0vyEEc-wDfAuv-IwuhT2l58NtRHPTgNLX4S7ehWQqrwBDEwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6fWhjr8-I4l3kxYq2wXIfj2wWXMdmZS30TGUta7s5HNxvW5wOwBCa2De-Wab4J4lhxAA7HCUWrdESdsid44DtsqHiHfjANrbJWU3-vuR1lhFZ9w3X_W-QSdWuwg-TdRZVcZKg-DtRsylHZiQPYxllzGb0vfonaWdpeXipNfkJBUwSMZOCXZ5iOUlRM67yAMLl9B75RMHVVcihYuzrECl3z0Ck1pYNSp7kI1elRlkD-PWJ50feBsWtF_FjOrEeFZSaCq0jEmIRHVG4OxaiIeLpCNV3WtLGFGb9itP1rFr9wll5Iicz3Ydo1e8ugxq74v0hhR8pdQ2jY4LLdg81oNz6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu6fWhjr8-I4l3kxYq2wXIfj2wWXMdmZS30TGUta7s5HNxvW5wOwBCa2De-Wab4J4lhxAA7HCUWrdESdsid44DtsqHiHfjANrbJWU3-vuR1lhFZ9w3X_W-QSdWuwg-TdRZVcZKg-DtRsylHZiQPYxllzGb0vfonaWdpeXipNfkJBUwSMZOCXZ5iOUlRM67yAMLl9B75RMHVVcihYuzrECl3z0Ck1pYNSp7kI1elRlkD-PWJ50feBsWtF_FjOrEeFZSaCq0jEmIRHVG4OxaiIeLpCNV3WtLGFGb9itP1rFr9wll5Iicz3Ydo1e8ugxq74v0hhR8pdQ2jY4LLdg81oNz6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=WEp2DPzXWke9UAHQ2NqW0eR2Zwzc0tVcoxLCPPzotibnLVCBNVt6AmJgH-tk-BUXI4CxFv1ABqDgiw7KEvc1UCCo_yBX4OZ0_aJms7aW7w-MumsJ9o_0z6phbKXlyz5gktl8-2Rj31YCCQ9up1uvXKJ_FINM77tW-wEKUfWd7ks2_CGRTe98qSb6fUIdFsAbAouc3lDw4L2uO5wdmNaPZjZt09lfSAMtlSPni4gMkFiMs7bgUJdIXZDrwuFjnfChVRjQVQTg8REnMlFbnIlbw0AlREGLV3PkLr8HCMKhWKDbXIcVvHgam0PTMYFcuUBsW9SjIiAlRpXyC3L244Q5JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=WEp2DPzXWke9UAHQ2NqW0eR2Zwzc0tVcoxLCPPzotibnLVCBNVt6AmJgH-tk-BUXI4CxFv1ABqDgiw7KEvc1UCCo_yBX4OZ0_aJms7aW7w-MumsJ9o_0z6phbKXlyz5gktl8-2Rj31YCCQ9up1uvXKJ_FINM77tW-wEKUfWd7ks2_CGRTe98qSb6fUIdFsAbAouc3lDw4L2uO5wdmNaPZjZt09lfSAMtlSPni4gMkFiMs7bgUJdIXZDrwuFjnfChVRjQVQTg8REnMlFbnIlbw0AlREGLV3PkLr8HCMKhWKDbXIcVvHgam0PTMYFcuUBsW9SjIiAlRpXyC3L244Q5JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=JpHnr-FP3UEAYA3tzD4LrrxkgnIcedpu-QWNCDSsh0UW-kgq6K_rSBdnRbzaFpPYhsNhHmS1dmAMy5H5yCRsXCrX2xtBbILQcSoD43lxc9FblBsSTmKdOYujJKDPk56ka6hLCq4BgQbwkUQzwZTyCT7MkdHUDMuyJGmGGWgBZU1T2eeDwILafUV5dOr_UYc0qSkmKuZBLwKLTj1mC83sMRFB1OCTUnZ5YyiFNTjn26zZnwmtN5onSd02Lauisx7-r96mYAPsb57cGIip3ruLWax48oUrmRztOzdRwqT-ALwWF-DJ7AARz-DpXjWB0M24MsbWEkhfTjTsEnaVeeLhXBzItnyh56ZZgPKxa-yIPj-aI1q5JrQwTtuJzVRABNqJ2Crroa7jp6NlQw1RhAda_VkoGO1MiylXznSyop44zXKXY_W4hVe4DH7B1DI6LbPLukD0FCybYjT-DPNwIdPC6cZ_IHCIAWDqazEkYtAiytQsnBYNhosHpo2zmOCtvLXq2I9O_Zk0D9pV8kog4f5Lv4xgacj_aN3qaDpHBc1sq7zdxkLyZbS0UdLJigozSaCNBqyV-l7SDjKfgS3DtImhMWhj8j4LQVqSNUS0td106kJPcEvxIUrTOTTgfpqldXz-9TKwDg5fWgWLSLjuxO0Ni3YKwcP3a2Zg5zoW6KCujCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=JpHnr-FP3UEAYA3tzD4LrrxkgnIcedpu-QWNCDSsh0UW-kgq6K_rSBdnRbzaFpPYhsNhHmS1dmAMy5H5yCRsXCrX2xtBbILQcSoD43lxc9FblBsSTmKdOYujJKDPk56ka6hLCq4BgQbwkUQzwZTyCT7MkdHUDMuyJGmGGWgBZU1T2eeDwILafUV5dOr_UYc0qSkmKuZBLwKLTj1mC83sMRFB1OCTUnZ5YyiFNTjn26zZnwmtN5onSd02Lauisx7-r96mYAPsb57cGIip3ruLWax48oUrmRztOzdRwqT-ALwWF-DJ7AARz-DpXjWB0M24MsbWEkhfTjTsEnaVeeLhXBzItnyh56ZZgPKxa-yIPj-aI1q5JrQwTtuJzVRABNqJ2Crroa7jp6NlQw1RhAda_VkoGO1MiylXznSyop44zXKXY_W4hVe4DH7B1DI6LbPLukD0FCybYjT-DPNwIdPC6cZ_IHCIAWDqazEkYtAiytQsnBYNhosHpo2zmOCtvLXq2I9O_Zk0D9pV8kog4f5Lv4xgacj_aN3qaDpHBc1sq7zdxkLyZbS0UdLJigozSaCNBqyV-l7SDjKfgS3DtImhMWhj8j4LQVqSNUS0td106kJPcEvxIUrTOTTgfpqldXz-9TKwDg5fWgWLSLjuxO0Ni3YKwcP3a2Zg5zoW6KCujCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Z6doy9WkIVpF9-5vKyYMrVqYgWD9jQk2Wc_CupCAqCnAm5R04ZVyD4M1AU-yVJag-RDnzn0bHh7FBYbkwbShAnA_Gv-iQ0-u6QAmJ0lCKh9fYqmF8MCaZKgduSuqSzpGo1FzQwcpRx-2e9CZN40n0bMpRveCUDaSZuYhaQiZNZIEjvuwnt7lu2W8LsPLTBCm8ac1hyXFoNcEqpUddx8Fe-hLpHgXnra0MbMGxIRkQX1xZoXRoFXar6SisDk4hDC3Lxm6cUDdSscYX4Utf-oWAy7KsV1_e9sPwtFnIDRDkbJs7Gf8wwtPoemqn5NasyQBr1aVtqJWod3BJA1U3Y9zRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=Z6doy9WkIVpF9-5vKyYMrVqYgWD9jQk2Wc_CupCAqCnAm5R04ZVyD4M1AU-yVJag-RDnzn0bHh7FBYbkwbShAnA_Gv-iQ0-u6QAmJ0lCKh9fYqmF8MCaZKgduSuqSzpGo1FzQwcpRx-2e9CZN40n0bMpRveCUDaSZuYhaQiZNZIEjvuwnt7lu2W8LsPLTBCm8ac1hyXFoNcEqpUddx8Fe-hLpHgXnra0MbMGxIRkQX1xZoXRoFXar6SisDk4hDC3Lxm6cUDdSscYX4Utf-oWAy7KsV1_e9sPwtFnIDRDkbJs7Gf8wwtPoemqn5NasyQBr1aVtqJWod3BJA1U3Y9zRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rO7sGHwSIM9Akkzl0tgGG82PbguGVlxX3Zt_WOyKL2IRXkT5TzHTn6-1_izpDci2yq9IR8oIPX3cESKG_mwurxWX8PLOFuYaiSGXl7YlKXZqILy1ucerwHUu_8PUW9_cfQjNeDAIJn5VvGzt63WBFTTH8np7YiBDgEua6kLBi_bQh2cUTqk0VML6VXxerYjmMRJIaCtZHED0R6qJ9d73z0Rfau5S80Kwtj_ma_VhxCW8IewZ5J3kMYBYz3UdQP1PBYgA0tCB2Xg0IgxJhqOOD6DTrsfvNhkiLrPWe2Ts2oBkO_WuWpLd_5Uw7zMsQ2QZryR9REWeYOR4M7ST_T2pDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=O8BRT46p39B_V5JA1OPq9LFoyRH-EDZSen43g5uhBToM9nZUA-byTNW2o13Mwfw7hDZeXdyqA3yyQHIJwF2IRMRx-PsC5Pugw5JBkrdeslX2TuYnDmLBD08CpRhY_ZHdrabuBXx_RYDEY3l66dKUVkddOksyRs6TdEShzk89R-vE8sOJGXcjB3jmRGRGA8jPibHxT7yzbJD4q_S7sUsBDwWRp4dNxzcYK0PFuudBElelJZdz4XSk8O53pFZyP_ZNvZJqtUAwKwMMfd42NaWE_KBLyAdIkQlyGtHbWbdRjmG3B6VWTeTaEQyg-dvGc0Xj5MU8KZhDWdPaQArMxM9law" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=O8BRT46p39B_V5JA1OPq9LFoyRH-EDZSen43g5uhBToM9nZUA-byTNW2o13Mwfw7hDZeXdyqA3yyQHIJwF2IRMRx-PsC5Pugw5JBkrdeslX2TuYnDmLBD08CpRhY_ZHdrabuBXx_RYDEY3l66dKUVkddOksyRs6TdEShzk89R-vE8sOJGXcjB3jmRGRGA8jPibHxT7yzbJD4q_S7sUsBDwWRp4dNxzcYK0PFuudBElelJZdz4XSk8O53pFZyP_ZNvZJqtUAwKwMMfd42NaWE_KBLyAdIkQlyGtHbWbdRjmG3B6VWTeTaEQyg-dvGc0Xj5MU8KZhDWdPaQArMxM9law" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=XsJn59dcxiBW8rPEkYL9x5pa2rDKYskr6filihK02cSGslZO28x6nDi7JMwcMGun78Q_8YTah0uFcDtj6QEZGimGEnBsxWFQovJe_so5ySQVYhnXWVzmAuZjgUskuRyo10bc7WAxTiEvQWJjV3pIpSGT9f3y77S5KwxvJAM-0TO4ukK0jk38ckR5FZ_O7ohpCGiQKeUBG5cbURkcQgEDbKtS4znURFmsSBPUNMkqDFfEvMnUg3ynvcc1stCVwXv6crTepp8lrksDv7zl0X7Xo8b6mR2HUY_7CoRVtNAztptyxm8xCrsqarb_j74Y05a1FvShdU-EeVFIzwRlnj4UJYGmsweVRpTrEov3NoBmJVeXZcuWkq3S-E_SfHvJehzjR827eOEh7OpnEQhUq-5kwJpFRQW_ps4dfW5YOaPTNLJ27Fe-SlJd4UWc5Me8oGC1KJPAya9OhWPuRpLvgu2jgM8X0D_-ob2N1mzsc2XdeYwdPfF1u8gv2TZawPE4BTSbL_9kWo36ZueKxkPdxO19QPF13ajCKnotCERt1pFhNtV-u3uiwM3wE6bWGN9Gb41EN42KMuKX0dwJulYiyilt1whO5cF7Zd0O_NOAX_MYG-snTK6nqHsHkfjKziOjXCXsppamBMii12jdrH-VSekDGQiSN1hnfiIYMRNFKPSnFVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=XsJn59dcxiBW8rPEkYL9x5pa2rDKYskr6filihK02cSGslZO28x6nDi7JMwcMGun78Q_8YTah0uFcDtj6QEZGimGEnBsxWFQovJe_so5ySQVYhnXWVzmAuZjgUskuRyo10bc7WAxTiEvQWJjV3pIpSGT9f3y77S5KwxvJAM-0TO4ukK0jk38ckR5FZ_O7ohpCGiQKeUBG5cbURkcQgEDbKtS4znURFmsSBPUNMkqDFfEvMnUg3ynvcc1stCVwXv6crTepp8lrksDv7zl0X7Xo8b6mR2HUY_7CoRVtNAztptyxm8xCrsqarb_j74Y05a1FvShdU-EeVFIzwRlnj4UJYGmsweVRpTrEov3NoBmJVeXZcuWkq3S-E_SfHvJehzjR827eOEh7OpnEQhUq-5kwJpFRQW_ps4dfW5YOaPTNLJ27Fe-SlJd4UWc5Me8oGC1KJPAya9OhWPuRpLvgu2jgM8X0D_-ob2N1mzsc2XdeYwdPfF1u8gv2TZawPE4BTSbL_9kWo36ZueKxkPdxO19QPF13ajCKnotCERt1pFhNtV-u3uiwM3wE6bWGN9Gb41EN42KMuKX0dwJulYiyilt1whO5cF7Zd0O_NOAX_MYG-snTK6nqHsHkfjKziOjXCXsppamBMii12jdrH-VSekDGQiSN1hnfiIYMRNFKPSnFVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpPw-e51Ldux8chXixXL70q46vTEyhA9UGDzqTgJa-phNoHIyvoB7mYyh0p_Sbm17RVpGXbEyb30s1Y6OR2OZvgeIw581jxkj7V93BDU4Ia142XVtYQpN4urBlQSYPx4cM9WjfoxnuDGcQ-v19hSfadQ4wGqidnW-f8zcs3-XMLJt58kr0nl_ltUESCML-ukW0QTMgEexqX6R2rYFPWPlGHHaRv5sirlg_ZSySoiht09YBjsxTDnMTe0JeK26A8zVx4Z3kjEcmXr9qxkPOBlq12bCc5c_WYK07_l0cR7p_7BaeJaXWc9tYM8vC6c3EHZU4H0FBRyytT1Sqh_kWH2qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MR2Kni1imB5L-hvZSnIntiLDJJBbV4pMmwPL4fwN5dIQObjwSfeRFEThAVhfmQsYfw7LFWge49c-sGP81CS-I7lFDpSMU-2i0Xyq_b5LrcYww1X-fCJPZe1z8XzhnoaLIjmtSjbiat74C2aXnei9VCSsBvgEE3s1GDlfXmWCBXNfIaYkikkTmdD8qPNU6VUgUB2mWUgNN0ax9Plcmr9hcAybEX37HmKIKvIXDawYyIREPl8sCX7XQfn4GULhhs1nfxxOb1ktg5SSkrPARpjxxBLo2eYIzguPWLvaPgAamY6DNPDYHW1xeAAMM2p0OcpYIKhsmpa-YXoT99cuTME_NzFb5OVFj2gU052u3wbHl38bjxvOubjAw4j2Cdmq9ToUuzUFO_X49YMqxeatMggi2rwdLHl07zl09gqeexbLT9R7QqTvrTau7zzYb-o5ZClYtIpgq8dEoQVBxz-pIZoslEnMxoAhDnJQ_iEE4Y16nNqtHuXOj3rH8LnSu_g4AyjjKdu9cwzOuDosZ6ofA7ixQQpOnIeRM27MwEJ-Ta8KyZYh3Z9mTkqQ9a5nWLk7R348DSeyXXTbivdUvdRvIQbNYUcJzDkho4jecVAI2iRJOQwLfltDpJZEiRnhdZobtbHffgyQInjHL6-VADc4rzbWcKxfmoBY6Y2kJU5qDFBYIjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=MR2Kni1imB5L-hvZSnIntiLDJJBbV4pMmwPL4fwN5dIQObjwSfeRFEThAVhfmQsYfw7LFWge49c-sGP81CS-I7lFDpSMU-2i0Xyq_b5LrcYww1X-fCJPZe1z8XzhnoaLIjmtSjbiat74C2aXnei9VCSsBvgEE3s1GDlfXmWCBXNfIaYkikkTmdD8qPNU6VUgUB2mWUgNN0ax9Plcmr9hcAybEX37HmKIKvIXDawYyIREPl8sCX7XQfn4GULhhs1nfxxOb1ktg5SSkrPARpjxxBLo2eYIzguPWLvaPgAamY6DNPDYHW1xeAAMM2p0OcpYIKhsmpa-YXoT99cuTME_NzFb5OVFj2gU052u3wbHl38bjxvOubjAw4j2Cdmq9ToUuzUFO_X49YMqxeatMggi2rwdLHl07zl09gqeexbLT9R7QqTvrTau7zzYb-o5ZClYtIpgq8dEoQVBxz-pIZoslEnMxoAhDnJQ_iEE4Y16nNqtHuXOj3rH8LnSu_g4AyjjKdu9cwzOuDosZ6ofA7ixQQpOnIeRM27MwEJ-Ta8KyZYh3Z9mTkqQ9a5nWLk7R348DSeyXXTbivdUvdRvIQbNYUcJzDkho4jecVAI2iRJOQwLfltDpJZEiRnhdZobtbHffgyQInjHL6-VADc4rzbWcKxfmoBY6Y2kJU5qDFBYIjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=UmCvDmlKZufX5OxqFWKIIX8BoKU7bn4ZO2PPGTeFqPFSCRI9HmZJe3HND9MxwASejuiVji85kHaL6hVQEPfztResUhQa_h2bPELl_4HldrSFvZF7JJPBQzOO9cLe5DOyr3RcYSkete2H4HD9uK6Tcsrgu6d6lD88s29_TDL9JsBiTWaU0S7Au9tap0qkDBOjijQgRHoZaCih_wEebszMqm1TU9GjvqvYy4-ga75or9VCsWbbgwGaiGVjWEkj26YIvUAqQMjIk3ZfS5hx05fw_HZlTNKbUTkGayTM5f6VdEI9rmjPqvlxKfypzS4tXMZTDeY8n_cUWbAxMfD3gxJxQaYzN7MSaKycKXMhUMvlmSspRy8S8FL4e2NZvDKrJzkoECeS8rxlTXxfbwzmwn-dwyiUVbaGgOM7PmyTDNvwObbeprvBYdbO2mnMRigZFDI_kb6xwSnDv8iIqyyi5AdxEMthpQOQxaoBJyoKd2KFDZeIrjekE88jbK8LDC0qlvWs8bvuU4ou5O8a73AWDXSpaf1ka3Bqhz-eGHMlDJmPZEvOoHKqBmr2oCD0vwrLAu1EeYUUgHaLPT02xNObJDMc4bBZcZCASo1WQxM7xU7eHvu3M3h087V7GsLC4BkS9l3nYyzdLXcMQIvsLWhNxibk9Zxp_hHhvg8NmajTwOcdtqE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=UmCvDmlKZufX5OxqFWKIIX8BoKU7bn4ZO2PPGTeFqPFSCRI9HmZJe3HND9MxwASejuiVji85kHaL6hVQEPfztResUhQa_h2bPELl_4HldrSFvZF7JJPBQzOO9cLe5DOyr3RcYSkete2H4HD9uK6Tcsrgu6d6lD88s29_TDL9JsBiTWaU0S7Au9tap0qkDBOjijQgRHoZaCih_wEebszMqm1TU9GjvqvYy4-ga75or9VCsWbbgwGaiGVjWEkj26YIvUAqQMjIk3ZfS5hx05fw_HZlTNKbUTkGayTM5f6VdEI9rmjPqvlxKfypzS4tXMZTDeY8n_cUWbAxMfD3gxJxQaYzN7MSaKycKXMhUMvlmSspRy8S8FL4e2NZvDKrJzkoECeS8rxlTXxfbwzmwn-dwyiUVbaGgOM7PmyTDNvwObbeprvBYdbO2mnMRigZFDI_kb6xwSnDv8iIqyyi5AdxEMthpQOQxaoBJyoKd2KFDZeIrjekE88jbK8LDC0qlvWs8bvuU4ou5O8a73AWDXSpaf1ka3Bqhz-eGHMlDJmPZEvOoHKqBmr2oCD0vwrLAu1EeYUUgHaLPT02xNObJDMc4bBZcZCASo1WQxM7xU7eHvu3M3h087V7GsLC4BkS9l3nYyzdLXcMQIvsLWhNxibk9Zxp_hHhvg8NmajTwOcdtqE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=XNTIDE6QwStZ-VAXQ_RV5ZWKpdLIYHGYb-DAYsxu1dWhrR5k7Zoqo_IHJjxvdkiKPc-mUm47xe5Mcy5Td15iOLjyhgOfZfpvV5rNhsmswKJ_IHDlPjczdfJr7vYA8j-iXrDGUn3hnkEpuAqdZcsqpuKIjZX-zkzRbkwa2RhPMeE8QwsfvRzZJwAtFaLTbB7YSyi4Yl1KqupqV3glYN1Y1dreBtCNWMtbMOuqg7f4n38AzquijAr1wsvXDYGQ2p9G9I0kAnexQ9Ub1GE0Xb1pV6XmXSEVSiKpkGd9mD2bM-nvCCzn6YpOXvQ8GbRu9ma51AVbE_y1_mAoYyzNGqwNyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=XNTIDE6QwStZ-VAXQ_RV5ZWKpdLIYHGYb-DAYsxu1dWhrR5k7Zoqo_IHJjxvdkiKPc-mUm47xe5Mcy5Td15iOLjyhgOfZfpvV5rNhsmswKJ_IHDlPjczdfJr7vYA8j-iXrDGUn3hnkEpuAqdZcsqpuKIjZX-zkzRbkwa2RhPMeE8QwsfvRzZJwAtFaLTbB7YSyi4Yl1KqupqV3glYN1Y1dreBtCNWMtbMOuqg7f4n38AzquijAr1wsvXDYGQ2p9G9I0kAnexQ9Ub1GE0Xb1pV6XmXSEVSiKpkGd9mD2bM-nvCCzn6YpOXvQ8GbRu9ma51AVbE_y1_mAoYyzNGqwNyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=Cgk94FBI5hw33j_guJy9s4yvgxcmBZabYQVV2CXMDPJ-H8ig9nuXvuMp9Yo3Bx2mAJG53IpBhoFdkAAcnjcG08QUTF69nTOaS_30yDaaGTs3H_zwxu-AjK9K9WPX4RhQHYQPlBK87zzgFQu2ocEM1Foo4owjyXZnrQf5ZJUZEvCnTlcOnARUd29F3Onqjhfy14tPEBA5lqMulHUIkLoqzVeU11_YyrTwOw9mA0LtgRbmtm_w9Gg_1abL9IOcrDxSob97ef4Jr2D15vdxTkZ7dgMTuwVujScIWP2eenY-L-ltJx5AohBWtsC36ZtCY_igPUjwCkJkTmMsMHAqV3HfDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=Cgk94FBI5hw33j_guJy9s4yvgxcmBZabYQVV2CXMDPJ-H8ig9nuXvuMp9Yo3Bx2mAJG53IpBhoFdkAAcnjcG08QUTF69nTOaS_30yDaaGTs3H_zwxu-AjK9K9WPX4RhQHYQPlBK87zzgFQu2ocEM1Foo4owjyXZnrQf5ZJUZEvCnTlcOnARUd29F3Onqjhfy14tPEBA5lqMulHUIkLoqzVeU11_YyrTwOw9mA0LtgRbmtm_w9Gg_1abL9IOcrDxSob97ef4Jr2D15vdxTkZ7dgMTuwVujScIWP2eenY-L-ltJx5AohBWtsC36ZtCY_igPUjwCkJkTmMsMHAqV3HfDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=n6y-oy8uf028oUJv1cYuxv2jT97pXXarLyVgV1u45smuic2lx7GeDqYgE9lk8saF_sEAXZF0JcFsZvKTP8a7oZpOCJyPmDEx5LeoEXkQTRvIH1fg5xfVYcp6kg19kmMBA-He2eL285xHD1PIoLyNCE0n_BDanZnjnoNh_xit2TDR4xBr7OARRDjUX-QK29UjKV7h-Cwf3MTxt2ahzWtGtpPre8jFCG47Dbsjb_2zcaY0ztSc_-dxjaOGbAy_1SotbiPbjt0vTqfZiOROwMolIFsLXPZjR69AA8yS6naBeSoZj7HJJ5UTQcPOezajxJtCWtLuT5vZWjCXZfMs4RrmTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=n6y-oy8uf028oUJv1cYuxv2jT97pXXarLyVgV1u45smuic2lx7GeDqYgE9lk8saF_sEAXZF0JcFsZvKTP8a7oZpOCJyPmDEx5LeoEXkQTRvIH1fg5xfVYcp6kg19kmMBA-He2eL285xHD1PIoLyNCE0n_BDanZnjnoNh_xit2TDR4xBr7OARRDjUX-QK29UjKV7h-Cwf3MTxt2ahzWtGtpPre8jFCG47Dbsjb_2zcaY0ztSc_-dxjaOGbAy_1SotbiPbjt0vTqfZiOROwMolIFsLXPZjR69AA8yS6naBeSoZj7HJJ5UTQcPOezajxJtCWtLuT5vZWjCXZfMs4RrmTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=V02WOzkEPSfxnoijc97ZrjrodZCJjyT2YWPyiD7W4lXXq2lnC_YQf0-JriG-oade7lZGKdLcBX8PrzLJp_-u_LsBbHPKSXlWSy9m04--Eg8mo9LUJXkDUVbOUZY3BTcHjcDy5uZGwbMWYKl4cvt_emKh53J022zJvWd5lG2Ba-1KcWhDqbsHfl4ZorvIGZT1RWVs73XICUrBLN4eUVQ0d-G0T5LKJgcQygtef2oulfqro9ff5uIvEOVF2GIOJnjKW91PMYvN8vHtI41vLYuVpTonSCIrD3CFNM0gaC1qY77WsDXvvAhI5z3IhRj0zqYfdj9tftm0udeEqH6uMlWh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=V02WOzkEPSfxnoijc97ZrjrodZCJjyT2YWPyiD7W4lXXq2lnC_YQf0-JriG-oade7lZGKdLcBX8PrzLJp_-u_LsBbHPKSXlWSy9m04--Eg8mo9LUJXkDUVbOUZY3BTcHjcDy5uZGwbMWYKl4cvt_emKh53J022zJvWd5lG2Ba-1KcWhDqbsHfl4ZorvIGZT1RWVs73XICUrBLN4eUVQ0d-G0T5LKJgcQygtef2oulfqro9ff5uIvEOVF2GIOJnjKW91PMYvN8vHtI41vLYuVpTonSCIrD3CFNM0gaC1qY77WsDXvvAhI5z3IhRj0zqYfdj9tftm0udeEqH6uMlWh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ddY9nnAvwWqWoS3zyIq4LtvLVBK0AQX51pdOrmwHuR5JgF97kuC3PH0iPxFQWdRmeOXH2UeVFJ8pYe0s0YcSWzkzYufW3Wwyt5iKp-yPfy2bufF2g3Mk13CNrEu0eb708ZuTwP0ZP2LFHgotDNgBYtGxeU0m612NOAJQKFoxKCcyLjyhKiO0FaKkpwu0UW0qzXS9uana5hpK3aV9kfatX7_jujd5a5Hz_8Q-H88YdvvHMJFNXPYbi7t-3p9QPVZaWQQ4yf9HiTfo2VzQ9hhwzJ14nlFfqeYNMjoJdS3mS86kbUN5DO5vARkTabcrPHrzlDx-isRK3MsyCfnV9CCkkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=ddY9nnAvwWqWoS3zyIq4LtvLVBK0AQX51pdOrmwHuR5JgF97kuC3PH0iPxFQWdRmeOXH2UeVFJ8pYe0s0YcSWzkzYufW3Wwyt5iKp-yPfy2bufF2g3Mk13CNrEu0eb708ZuTwP0ZP2LFHgotDNgBYtGxeU0m612NOAJQKFoxKCcyLjyhKiO0FaKkpwu0UW0qzXS9uana5hpK3aV9kfatX7_jujd5a5Hz_8Q-H88YdvvHMJFNXPYbi7t-3p9QPVZaWQQ4yf9HiTfo2VzQ9hhwzJ14nlFfqeYNMjoJdS3mS86kbUN5DO5vARkTabcrPHrzlDx-isRK3MsyCfnV9CCkkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=u-A6aChHaNaw3bstr4M0h36Zzg4ChcQHs03tl-hAfve1XxnQSLwZ9gGnj3Z1h0er46pJMtoHWDKMuD68n_brU-rX2rDrnufASuq39XypBNnmZJEdFdn5WkjHEwqfkyQ_hxGhWuDsslZdUBX2LJDosTsf3hgA1sSfMNORQh4GNr6xHLzWMwkGkkpBav6_Z8YIVtAXILDx8wvMD63XHp1Dd4VnkfRe4ZzEmubJoVk6MN7ST0VtuIAK6z7lIMBsrAjExcqVCPz_Bb5AZ4WueMGMfSQUU4Y5ly-Hms8slVbhkZ11xiwJafrtPr10-Gm-_d-tvW8cu6EUvHK7Yw-uHMfFeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=u-A6aChHaNaw3bstr4M0h36Zzg4ChcQHs03tl-hAfve1XxnQSLwZ9gGnj3Z1h0er46pJMtoHWDKMuD68n_brU-rX2rDrnufASuq39XypBNnmZJEdFdn5WkjHEwqfkyQ_hxGhWuDsslZdUBX2LJDosTsf3hgA1sSfMNORQh4GNr6xHLzWMwkGkkpBav6_Z8YIVtAXILDx8wvMD63XHp1Dd4VnkfRe4ZzEmubJoVk6MN7ST0VtuIAK6z7lIMBsrAjExcqVCPz_Bb5AZ4WueMGMfSQUU4Y5ly-Hms8slVbhkZ11xiwJafrtPr10-Gm-_d-tvW8cu6EUvHK7Yw-uHMfFeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=JRNt3kDPyfxXJkzEs8WK7pFWVUltL17QMW9MU7kXRb94gJ1TqbyN4WxkXkxrvFHm9pmADLQbbC5G2OuFzeAl1KyzjM4CcX4JZVxsHcTUKyApwPNKZD7OSrmmMTaTRxWfd_cCsFxNX-gaasydrnQeA3XbNV3MNcxYkNudbRa4ilbxZQEKPD5Mt8fVBCIb5BNLP-i2Db7LGkrHWkPN28mZqrIArK7t06-WRXbUja96jzBcPpZ8oAyph4yfuHaZC-QBbbVy9kgs6pk1J_G05GKqXqaUQkeBWpbeHl2y-wPPLBgbA_t8gV6P_d4G7GSdNDTLdU-jwKrzg817bEBCA5jOLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=JRNt3kDPyfxXJkzEs8WK7pFWVUltL17QMW9MU7kXRb94gJ1TqbyN4WxkXkxrvFHm9pmADLQbbC5G2OuFzeAl1KyzjM4CcX4JZVxsHcTUKyApwPNKZD7OSrmmMTaTRxWfd_cCsFxNX-gaasydrnQeA3XbNV3MNcxYkNudbRa4ilbxZQEKPD5Mt8fVBCIb5BNLP-i2Db7LGkrHWkPN28mZqrIArK7t06-WRXbUja96jzBcPpZ8oAyph4yfuHaZC-QBbbVy9kgs6pk1J_G05GKqXqaUQkeBWpbeHl2y-wPPLBgbA_t8gV6P_d4G7GSdNDTLdU-jwKrzg817bEBCA5jOLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEVGuP55yfYeAE31pCDdKrkLgK-CIotvR-deY6p31JTwAPScT4CLxbVbIE7vuXyYAkoOOgGLlyyu6pdF7lYb84rRC5fn4x02Nx94UuRVWLkGG2V8vj7xnPS60EY0eDqSYMmKXVEBoEJSdj5ywceVYJ-nysh3Lw-Fm8x23kXebi5L78VUcXfkqDI5pMx4WyI5ooW_QgVQ0r7IdfgYBQchz4XKVl3JQ4rFFkt5QdAdHZcB8MEJUoD4ze8ssfpZq-prATO6wW58_7xJUxg5ySU4X9EyHYyysya7YtfoIoOmt-y2lavjpwrrbz4WuuiGnqgqlCoD8FkgIBRCbIcRayteSA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=PqBpR6Gn0GZeBVLXzeUKOFE_lIrrbfKSg2G1CjQ0g8el3dPF1qAN80FDRO51VYcBIv3ljpJjVm-JJpAtpTrie-GkcfXaKUuPs3mV2gkaUIZ_OVK0MCjaxf6yfzoL4uHCdw00I9sh-U_bdyZFojfamgzgVWzu50CG6FbPsmA24MALMggdhFyeG8tpbfluY6PbDQJMu4ES45iswnDqW7DSR3zYsXN9vz9XOkPwtfi24NXaeJEdQUqRFGOQdsZgDxbJ6pkrpnjiwVEG0NAdeHgV173XuLRQU1EM9EBptHz9nMrXCP3dH5mKIX4GpQuw_50aTgRzvCYnEFtiis0AlKVoSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=PqBpR6Gn0GZeBVLXzeUKOFE_lIrrbfKSg2G1CjQ0g8el3dPF1qAN80FDRO51VYcBIv3ljpJjVm-JJpAtpTrie-GkcfXaKUuPs3mV2gkaUIZ_OVK0MCjaxf6yfzoL4uHCdw00I9sh-U_bdyZFojfamgzgVWzu50CG6FbPsmA24MALMggdhFyeG8tpbfluY6PbDQJMu4ES45iswnDqW7DSR3zYsXN9vz9XOkPwtfi24NXaeJEdQUqRFGOQdsZgDxbJ6pkrpnjiwVEG0NAdeHgV173XuLRQU1EM9EBptHz9nMrXCP3dH5mKIX4GpQuw_50aTgRzvCYnEFtiis0AlKVoSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Cev22LYnKUy2X5lehamRlB--twab_iM2532thm4nwfgp1O4JDJBQtenUJgnOH9yTXa2fHd1SaZVjxggBPq6WtWs4G4HLGWqxbgExjhJRlflEGdmDIPNIoGCxMWqxStS1LCyw6h8aYGkVtM9LljdnGvrNmZRd_DdeJE51arjsUsaYMp63assqQWCTulKY_TZtnBXL2FMb_hLjxf5GPCZO_4WvyXnPSj8-5J4aYwbAQbn8B9naOJmn8mqGTfWH2KMGXk7zpPCtkVqkovO0uMV6v7ZBGn0lNkNrHxqWOmIpjs106rT7vzn9R344Bkdy9XwExromFOB5n13FdY4srRKKxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Cev22LYnKUy2X5lehamRlB--twab_iM2532thm4nwfgp1O4JDJBQtenUJgnOH9yTXa2fHd1SaZVjxggBPq6WtWs4G4HLGWqxbgExjhJRlflEGdmDIPNIoGCxMWqxStS1LCyw6h8aYGkVtM9LljdnGvrNmZRd_DdeJE51arjsUsaYMp63assqQWCTulKY_TZtnBXL2FMb_hLjxf5GPCZO_4WvyXnPSj8-5J4aYwbAQbn8B9naOJmn8mqGTfWH2KMGXk7zpPCtkVqkovO0uMV6v7ZBGn0lNkNrHxqWOmIpjs106rT7vzn9R344Bkdy9XwExromFOB5n13FdY4srRKKxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=DcDToLd-ULa1P4JdMvc68ifrqMF0anqKc0jWnK4xZdtx8rwuT3pdLV6zTWc36tQyF8lecDVmZjqHJF3UbtyKZgZzSH40uHCQu9_276cT9dLU46UGPH_celfvo-Lgdhlcx8e1OM2ogaHVt424EqbMkOuF7sB6-Z2bJ8GSEa4VvJXEk1WC9f42QW0SM7aep1NSJ_WquVfUOHZOPjc8urbUsEQeGaKEQnF7fvF8Xov_u7BFpmLjf2fw7CiNZr2xH85OzR92GBf0PI44Av8GMu1uohcNz1VgvttxGq95ir-d9igjAIo3iQFb0n_T2S-63t8dgSV1cTv26sjzzEoL7AH90g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=DcDToLd-ULa1P4JdMvc68ifrqMF0anqKc0jWnK4xZdtx8rwuT3pdLV6zTWc36tQyF8lecDVmZjqHJF3UbtyKZgZzSH40uHCQu9_276cT9dLU46UGPH_celfvo-Lgdhlcx8e1OM2ogaHVt424EqbMkOuF7sB6-Z2bJ8GSEa4VvJXEk1WC9f42QW0SM7aep1NSJ_WquVfUOHZOPjc8urbUsEQeGaKEQnF7fvF8Xov_u7BFpmLjf2fw7CiNZr2xH85OzR92GBf0PI44Av8GMu1uohcNz1VgvttxGq95ir-d9igjAIo3iQFb0n_T2S-63t8dgSV1cTv26sjzzEoL7AH90g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Ug9hhmT339ftm6Do8mIcsH-eKLJl4WUK26AaTOS9R57OFKwNfyEKC7AQH14dhtcAzoxV4zskiVEpGw9Y23rd-KKqzwvLscod02MziOyQoCmRED3EQSdtaW0yJ_m2IUJxMORWRQFwb4KqP6rdI2_o0G1Er3gYNFTpvJP2eNkJlNgyAovkAbOE0duAi-gpPPEd9xVvo6IgEt81Lyw21_mVyQAw0iNVay6t37qXUZB6WYOb7lmKADwwEgYc-fvFM1ttPDPFSsTZs7pxjVADz8jjKYRmJfpm9AxxtgYa1GbC6PnWjxhtO83xIsTVetx2RUwioHDa7PFXREh7UOA9Pq9Aqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Ug9hhmT339ftm6Do8mIcsH-eKLJl4WUK26AaTOS9R57OFKwNfyEKC7AQH14dhtcAzoxV4zskiVEpGw9Y23rd-KKqzwvLscod02MziOyQoCmRED3EQSdtaW0yJ_m2IUJxMORWRQFwb4KqP6rdI2_o0G1Er3gYNFTpvJP2eNkJlNgyAovkAbOE0duAi-gpPPEd9xVvo6IgEt81Lyw21_mVyQAw0iNVay6t37qXUZB6WYOb7lmKADwwEgYc-fvFM1ttPDPFSsTZs7pxjVADz8jjKYRmJfpm9AxxtgYa1GbC6PnWjxhtO83xIsTVetx2RUwioHDa7PFXREh7UOA9Pq9Aqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oh0FNkh-sLsqJ0xZXhq3SVQj3S4m43Wd_LkLmvWB-eIuyHbk205PfyazJTHphThgNwepGIM_3AXA5aIxL4KOkKkVvfcVhoZymCkHk8933pOz7e3B3bTnKDQU37aUHs38VQDac9CeMuMUuA4X4CrD8vSCgaf46SJkMdhKgWb7qBCWmDQn1wao8_3TrLTVVJL6e2NpgcYnAOv7KdGTXTfP0GMTzCeGoQ7AGoe69z4b0ApWEcNSb8kkCdxhs6rgCi6-7n0AyyQdfMjHqvOjFIg48maTnE7PZLc6cl-AEBP99Qb-KpqUF_08IkpHTd5xihBaFhbwl5FmEU-XPtQe5K8_Eg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=umcUMK1MzHZ0pfeBUQlaJg_l-MmjX_yDBOA2M1TQrQfQVC2blRBfCPXHvpqFy48mz6hLzcZkwgFBVK7PTogPXE1pPdk3KzKQn7JgmIPLjS9RkEEymHdK46yNKK1Dx8ll_bF2dNzw4aVAc7s-BsKs8wAZzVpCKXU7tlS73gtZTl4c65I0ehDuyR-0nq43rqAxYdq35vq8iOByvmR8ySp37FyTM8Tb6duJNHdPypPMquVsbk_g6dy_UYCxyQcZfqqvbcTt2SRrktjEHnJgUSbGqLpXjcz6LtCM4m5mLVHmR8iIE4ugkt2a678RkxkljoUeXSVh8fW-Fi3MUGZDQdvZcIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=umcUMK1MzHZ0pfeBUQlaJg_l-MmjX_yDBOA2M1TQrQfQVC2blRBfCPXHvpqFy48mz6hLzcZkwgFBVK7PTogPXE1pPdk3KzKQn7JgmIPLjS9RkEEymHdK46yNKK1Dx8ll_bF2dNzw4aVAc7s-BsKs8wAZzVpCKXU7tlS73gtZTl4c65I0ehDuyR-0nq43rqAxYdq35vq8iOByvmR8ySp37FyTM8Tb6duJNHdPypPMquVsbk_g6dy_UYCxyQcZfqqvbcTt2SRrktjEHnJgUSbGqLpXjcz6LtCM4m5mLVHmR8iIE4ugkt2a678RkxkljoUeXSVh8fW-Fi3MUGZDQdvZcIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=PgFrvoXbiiDVF8qO3T4TbrXDUVYCpZhDCbsRzxQwzrLXSQ6zAJLTRpJ3uBR16i1UwLFT-8HeEC23tdPDmhQ74sAweIpK99tHs7SDIcu2O5sf_mLuugjR-kIUqeF51jE5Bx2JxeK6-KSFaXRyzWs9TzQmKoR4uULTys1VVDpb1_iHTUMlp3VBNKEzqZv0okc3GySPEO4c1cQ4IK2EWGIjOYw2iyGaLlZtOUHiupkOHZE4MQl1oM_CqaCTmn03qqXhw5Wz3tKpRzeafyIIUdHhyIU3JJojqMei39HYQ_2cVZN6XPW9WmO3L_Yojp7cqWohLF3B4AKUUfODDoo7oN-RBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=PgFrvoXbiiDVF8qO3T4TbrXDUVYCpZhDCbsRzxQwzrLXSQ6zAJLTRpJ3uBR16i1UwLFT-8HeEC23tdPDmhQ74sAweIpK99tHs7SDIcu2O5sf_mLuugjR-kIUqeF51jE5Bx2JxeK6-KSFaXRyzWs9TzQmKoR4uULTys1VVDpb1_iHTUMlp3VBNKEzqZv0okc3GySPEO4c1cQ4IK2EWGIjOYw2iyGaLlZtOUHiupkOHZE4MQl1oM_CqaCTmn03qqXhw5Wz3tKpRzeafyIIUdHhyIU3JJojqMei39HYQ_2cVZN6XPW9WmO3L_Yojp7cqWohLF3B4AKUUfODDoo7oN-RBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tAgQSUTb2-nuwanY3PFTxX_heZ8XIagSxr8Xv1Yognjox5VTnwqzDer-z9DKe2ZbERuWa7unLQ4OepSm_MKnFhHTR1hrgjZttWYIuai9KEV05_BcircgyuorLmZYvlpiS8DoYv_RcTwKp_DrCrK4zZI7ZkBXAj30jcnKvX4lHKDILwD4fzTn5EOWWFj_80xidza2qAylTe_7ydxCmezB6gGAECh5rqFa9_CYqudt2Zh_ckFQTFckWfGPsxD4F-5SrSN2NHTSyP3XRzXRXIknyclUeWImcTSYikbLnTkVaFbo6B_6gF1rXHq2-akIy7csakUB5b6OudHE2MZ7FDnM0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C__cysXhTwtftjG-qMEuZgVCI-0FUg6Fp4mUVQw-OzzTRFXUaO8QmCyuWlzMxbrSC_Bszpzgh3NKn5IldmV3bvFQGqrPyiCMyl-MERqXD-wozLxfxJ08rSQOe9Cd_XhQxe-FBNBTBN3oyJ1fYrPvGEvBEeJs09P6iIzcMb-WiXXz01hD0SJ6ProL4CKOpC7nkZAxdAWsjMsezM-eGJgu160nb4m52w4bIhZHBW1Iq6UeE9ZXMF7F8ZelbtUL_dFA4SWtT_EpsiNJwzEb3tsC6Eat6u5kioKUKgNCcijaV8hJhZBzrqiKCE27ZyiNMuUXGH4WmpMI4y1FlOTg_v-zcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=KHbMaaJ8UD-B3J6qHpViKRl2DpsvUBWPDliGS2gf7fLXo_YymW8wiPhlmFo7KlOni425oRwjQMbrATx7uJrH55HQ0ztF9gFaP9zRKrfBo71x54A9R7Iua2tdEg62jDLNAmKSshmjnHYlD1Sk-3iZrPH3iSGQ-Prc0Rsmf7MZfUks8tVW-ag3vhCsccswBVY2kZ45s7r8AFbL1JtfTqoYB5tPa0LiWGUarq4JQX9a6cjglNQLI0Cxs8f_0Gn0b35Zzla4eJ-QqIrzVswOOUbdF153oU4d3zUwIBsMqrrKa3MRHk7fuRgnR4F-jhSjLwf3BJZzUrsp0wC9dQOXED6xhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=KHbMaaJ8UD-B3J6qHpViKRl2DpsvUBWPDliGS2gf7fLXo_YymW8wiPhlmFo7KlOni425oRwjQMbrATx7uJrH55HQ0ztF9gFaP9zRKrfBo71x54A9R7Iua2tdEg62jDLNAmKSshmjnHYlD1Sk-3iZrPH3iSGQ-Prc0Rsmf7MZfUks8tVW-ag3vhCsccswBVY2kZ45s7r8AFbL1JtfTqoYB5tPa0LiWGUarq4JQX9a6cjglNQLI0Cxs8f_0Gn0b35Zzla4eJ-QqIrzVswOOUbdF153oU4d3zUwIBsMqrrKa3MRHk7fuRgnR4F-jhSjLwf3BJZzUrsp0wC9dQOXED6xhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udS5IqN8Xc_Wp8LWkYXCjgz7WK-14alGrXVPdENnc9VF0YEmML7ZGX0ebQ_qpYZ6HI-By3mITcN4DzfA1jN14HiGUt4PT-oOu0s0q-n4kZllECt0RQV2kD1DHmkndWw60BpIfWnii31R0S-P336XWzCbyze42YG_JwKF3alLPRNkV7iATbmqd013pcimHhVxE8QLIN4gU-DzAIKph_IoLADnb9TEojqJP9UqlI9yvtN4F6rlewEtAzszXzLJfC20gDnczjuuFFUEYxuheapPbFrZs8SMtDCh0nO1C9CIswnhVOf8KwLBNwapqIMKFQ-VvqlphhkFEeOQkfj9iagiLA.jpg" alt="photo" loading="lazy"/></div>
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
