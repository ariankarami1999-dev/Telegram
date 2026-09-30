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
<img src="https://cdn4.telesco.pe/file/VhX5BUOlv3ZtcGgtiB_Ja58wSLX2xQzC_Y_h8BHimUyim00q8aR9ZHR6ht65msNdgeX5t42-XxhYlzjOc43WRRqtNsOEetU8kn4jWL6MVm2C_KlinlHTlwgNkAqqJzA9iX8dza_hdbvBwRtWISSzQX1dL6uVSyhod3EV4rLrTuk6TvjgJLF29Sp7OB8c9Q2UmKjHUAp05VTPpzwdrUoaGo_B3HJXM0nGdAY5gZovQPPni8U5MzbTk8MhHys_FvVmQetcHWqB1AxqCavYgwdZvlVc_z2m--FnKzmvupiFUGnjV0iCw4m86PxCvZXvyiAv4W3kmbjndgo4jhMQwof73A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FSu-4TaghJ_qUA2eTi01pVr2YjBEhRe3kPey-jVrGuiCynzibqxlLWFLywaKQxevrHHlO0sAapqG8pnHrUrOwxznrwGkmrqGtLmRNMQLYsA94MM7e-rNajYRNbflDIelMtaZgolhExkKfrOcHKl7rTWtOeoU_wgHVFg89Vmn3nyE4p0JlK7OJtYVbdG6t7cvxNJD9fcnxO8v3K-O6f6TQgTc8oZySL8vP2wqINPT7m3FzDsmgFQh9tAT8GMWtRhZoElt8Y0lnkKsXmVYcTdCA-uyyl_-WEFOX-aoAqTLb-f_L8HVeOf5XVLHAsctNgKrBUxOOyB-0SI2WV7zqkW_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upL-cUjmxO9iR7T9FcCZVnqFZqPEAM76RyWFzDCHGYLi3OIAaHTycFQhFtdHPIWKCGty4fVBMU5o9AY9YvlGJwko9N1BRwJLmo9Eb2IOqMJ-tLbNhGiuE8M3C8c5Aqkr3UFfTs0GQQZKwpkbaLdre4js6RnY342QOPUmYZqF7BoDDPc0a9RTMpRLAPyOQ2xVKBv-xmRZ6jE58SBC4VtYry7uAn75q2oKkbkjr87tGI-mVHtMWOFI00BQfL8QE3OZ0Lm03vK5r11LzlRGsCUEFrWAWerD6x0Z9-N7wMTUwKXbN6cNvnyo1vmLgn_Pw3trqWOugf-3GNlTY9NCozFr7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=u47RjGutzISdVwJwkmb8-d0S-QEAEpI--UQUJ8s0L3gMfJpc7qBlK4nZBDRl8Oy1ubwlR_f9vB--huX-YRAqZLhGrKvB3Wk207kw0hNipE14njVmZr4R1lRvS1kCLGZPoOxuxCXI_aVTIqeHrvrVSCn6Nj23cyJeiKg5KPIVVOhCcVZ0KBgk-b8BjrYbKLfbsKh1X9aYbDBG1gwrUJWNvPDhy7nhWcCOyTQBG9nedSRyPDUU1a8bb6eXp2kBD_gCxoBIFohg1K2_JAbbg6KyGnJ5KiEEkm6Fg7mC5RURH2H1zWZDCaaOcrVU_9EES3wVPWDNEXnk6poJgFY4UNufMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=u47RjGutzISdVwJwkmb8-d0S-QEAEpI--UQUJ8s0L3gMfJpc7qBlK4nZBDRl8Oy1ubwlR_f9vB--huX-YRAqZLhGrKvB3Wk207kw0hNipE14njVmZr4R1lRvS1kCLGZPoOxuxCXI_aVTIqeHrvrVSCn6Nj23cyJeiKg5KPIVVOhCcVZ0KBgk-b8BjrYbKLfbsKh1X9aYbDBG1gwrUJWNvPDhy7nhWcCOyTQBG9nedSRyPDUU1a8bb6eXp2kBD_gCxoBIFohg1K2_JAbbg6KyGnJ5KiEEkm6Fg7mC5RURH2H1zWZDCaaOcrVU_9EES3wVPWDNEXnk6poJgFY4UNufMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=PLzv8mMU_SLb8vDfbjkPntnj6wtYwrtUb26VxwK-2bFiJk2S0wkfHcFVSajnjQF_GNvkCqrMpRevUwrKbm2LJ0gABbpkgQhJ1k23T2LTQ4N1atyxrUVxMoATs7cGS0_mTuCEBCvP_6IjZQrdOVlqMKqa-2uuOKNBCkhMIQbEfAtF-hFNUDROrib4jIvykXbwjdvu-ftydyIrQCozAJjU9bkh-S6Y9EhpJ9r9ldHh1GToibzylXft49DmaIJMLQKIqRfVsg1aKldbPyOU4zZrwHdcrqlIy6Qv65EK9YSBd-NRo3SNWgZtinrsnC5-5VeYuAajkwCnrX0FeuICoq1ACixb_SgssZiUW8wUhM4xFf5yXpAK5NZkXo-AgZ0XDUS6tmFfESf_Y88o8V1ULuy8niSJJpAIQBD9Lk5HZnkybncTnymvddRee7I3UgyjIDl3E3_elW4SdPucr8AaRuki2d22jr4ulrs-9uOn2uPvPFjN1tPywO-hYMxwN_Bli6lJE7E2lEJFKMbiZgVZK5Z47A-VXtWtwIIABS-nMyFuLooZQsZy86F1jEGMA7B44sp8RgOR8wmWsYAuDkjtVVVkfMIG5PwBQ-IwcbO3H80zMjuITy9j2TN_gTcT9qohz_9b4r6r32jMj7tHHwfX0sccLXjhZRsNKIiKAH-OApXcgGc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=PLzv8mMU_SLb8vDfbjkPntnj6wtYwrtUb26VxwK-2bFiJk2S0wkfHcFVSajnjQF_GNvkCqrMpRevUwrKbm2LJ0gABbpkgQhJ1k23T2LTQ4N1atyxrUVxMoATs7cGS0_mTuCEBCvP_6IjZQrdOVlqMKqa-2uuOKNBCkhMIQbEfAtF-hFNUDROrib4jIvykXbwjdvu-ftydyIrQCozAJjU9bkh-S6Y9EhpJ9r9ldHh1GToibzylXft49DmaIJMLQKIqRfVsg1aKldbPyOU4zZrwHdcrqlIy6Qv65EK9YSBd-NRo3SNWgZtinrsnC5-5VeYuAajkwCnrX0FeuICoq1ACixb_SgssZiUW8wUhM4xFf5yXpAK5NZkXo-AgZ0XDUS6tmFfESf_Y88o8V1ULuy8niSJJpAIQBD9Lk5HZnkybncTnymvddRee7I3UgyjIDl3E3_elW4SdPucr8AaRuki2d22jr4ulrs-9uOn2uPvPFjN1tPywO-hYMxwN_Bli6lJE7E2lEJFKMbiZgVZK5Z47A-VXtWtwIIABS-nMyFuLooZQsZy86F1jEGMA7B44sp8RgOR8wmWsYAuDkjtVVVkfMIG5PwBQ-IwcbO3H80zMjuITy9j2TN_gTcT9qohz_9b4r6r32jMj7tHHwfX0sccLXjhZRsNKIiKAH-OApXcgGc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdmttvCvkjPut4MmtPjCdR6VkrrVjppZZMJGMajbNBT-4TmeKLH09QcInaI0pFOnFPzqKKKIY9WhcLW4isTMkCwYrVn1U00IvwK4ZCNOOahZvkBVbe2II8grqEtohtVAIbA_RJtx96d1_AiCnY9PJC14amv-a-gV_iFIPn3g_su1eXuLgUt5JVpLtK8mDGbBvxBAQR1Eumbzf4VPKw1q-vqPYeyU0rSMT9Lponr_PEQZ1JLFNvqgw0vWmGQSwTjJJqBQ1h4D0etORADB3KfXRUbUEY67VfGKVhnU_cbCTTLWeiZg9osnSsBNe07Wkp0Eun72bRPNti4uL8vjxUQt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUCuLTF1ky5S1NKzLdt_8yhlFL-NCcTGTXzgzJ3fcAixrdQg0rUx_lGX4bsFubvcH3SLVaVJdEZUWSlMMr4-Zs16H3pPQZKdR8f69tAkrfrKKY1liSkJheJdILvZikinRbQ3sKI1x49zcE8U2klM-yMtkXdLfEkwUxB4lW4zUMhDXT2K2xJNXd6T5P81U_yaBvQyv4lX72N3KL49jJJTLTmvi9iVyzw3Iprwi3TJs16OOQqPe7xbyZ3_TFz3sIOhgmPlTeiusCxbs5SvXFd9lRZsvzbjQr21t8jHG3OQN1ICWVfdO0ztNq77YBY7QJiLlQugJvMtvlBe9FAknLNUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LYOevLWCoTMtE5K8XzPY7LPgpiL915mzOLv9pUmpaBF0eoFwiFNUtpQFeHNJhx0z4UF3oTRjlFoR4-xfXVTXpQ6pe9L6r9zWm7eADOAPKu820f86_Hwm-kwve23d6CJux-Zr4dA4gbMO-ZPEZdKQUM_2G8KB3Fr542qoa5sj2PRzFc6w7rldSl-9Nite74LWzPrKqc7Ose--4x468eULgKvxc0IGHZ6hCRPImSiJWiPP-uohp4BVQxqk3kYcWIbs9pB5u3ot3SdbPiE651t69sI78ouUA9UUanHTkgTaK9QGCvPBKjqW5JoLNEnQaNlcQMBCwBIx1jAcPQ6DbydTvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=B2tHj07MxDvFQcTVft9a5zpxqPypwRpd91L3VBEcsF9zn3vU3Vd7vKgJF5PCWjr-mBVQOGHwiF17ua_7PopPQw0BvRwPeM_36iAexAUihXX1m2JhspHvPGXiWYtPI6hi2nNEkznOAReJ7EUTlceavdhpZLuxoAhrX8IGjVjrTI6sW-Png6XbuyK2OWu7EjQ61v22neawTit3YOSyTCqe4r6q4r8OEsboOcXyTrJvd9zUgNAG6UoLZPz5jH5zzpgR9aiidNimtiOz-Zkxfo1T9krcGOln8fvQF-vDj-3i40ZpDL567hD8Z4Yu9WSXZn8Je1YyROLagH9pzT5qp1oEZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=B2tHj07MxDvFQcTVft9a5zpxqPypwRpd91L3VBEcsF9zn3vU3Vd7vKgJF5PCWjr-mBVQOGHwiF17ua_7PopPQw0BvRwPeM_36iAexAUihXX1m2JhspHvPGXiWYtPI6hi2nNEkznOAReJ7EUTlceavdhpZLuxoAhrX8IGjVjrTI6sW-Png6XbuyK2OWu7EjQ61v22neawTit3YOSyTCqe4r6q4r8OEsboOcXyTrJvd9zUgNAG6UoLZPz5jH5zzpgR9aiidNimtiOz-Zkxfo1T9krcGOln8fvQF-vDj-3i40ZpDL567hD8Z4Yu9WSXZn8Je1YyROLagH9pzT5qp1oEZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=RDXZGP56DfcskABrCZq7mOK9f1Fbr2DhwliEJyti2rKVQjkl6Nt3p1SvMwwZ5_xs2wpp_VilU7WnbOPScApLX10QQAlqDbmlRGjYB493khkmsPK5chlrV2RX7C5_VnNIShHt7ERiWL6sRtcLzjfWfgX8qndILJQJGRyJz9z3hWkccSEWQHkHMIOjDLeGZ7rO-yG8XQbs5UNYeD200ElRzYZNH3iIqK3T_Ud9mviZr1u5FiEYgZSULuA0hdVs9G-sc1-J-xWIAYe_0wqz9WmhXOIqmU2ZuwYshTpn4MHhHMFeQzmd4HTRrYY_ju9dDoBU52b3MFIFn3O3GfsP1iGnqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=RDXZGP56DfcskABrCZq7mOK9f1Fbr2DhwliEJyti2rKVQjkl6Nt3p1SvMwwZ5_xs2wpp_VilU7WnbOPScApLX10QQAlqDbmlRGjYB493khkmsPK5chlrV2RX7C5_VnNIShHt7ERiWL6sRtcLzjfWfgX8qndILJQJGRyJz9z3hWkccSEWQHkHMIOjDLeGZ7rO-yG8XQbs5UNYeD200ElRzYZNH3iIqK3T_Ud9mviZr1u5FiEYgZSULuA0hdVs9G-sc1-J-xWIAYe_0wqz9WmhXOIqmU2ZuwYshTpn4MHhHMFeQzmd4HTRrYY_ju9dDoBU52b3MFIFn3O3GfsP1iGnqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RklkcfQFscNLvTRMtxfQDpX7HmsafMqDKZaOfl3bPp-2rEagjGovguMYT_RRgjX923HhxgveBTaPjtkafB54pI0XFnNvILVekEBd6T7bC6_iPFAG0X-N3IQN-8vjtcaMOZ1pC-yUgeodJozJGCxUZE6iq1-Y2sSdqwaliYu1sEXEu2-mFNKQnynOZYujDL5sLol7-JBT9iFUhRFmeHdJ0ROXN1YWLVUD1LjN_zNHWAltrvqyo2OXehiRoYkzguWuOahwbWVYBvrrrQQGoZ4s40BluHBkvrg6vf1-5_LGQ3vwvAS-IyzVdLUEOgAHgxLmv9xBRTxCOUafAetxsjk6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=UFsQ0OidagncQGlC4OPq6L11xfzpgz9Oo1rX1jGNtMIjCH8_iV0CNaa4bs6NpEil7JscZ2gV0USWA7utwRgg_INg7HNaoA63qh4CYTIWhczAdFuWcHZhtHMinKZlZ328ifesveeORwWwv_NyTR0JSTm7n_qnvsyOldWY2C8pFyZ2tXsTOu2RH3rxqLisaI3kTQWYdwR1xfuZ9pNKF57UXNmrfvrhNmhQhx-rMAuJbnkOCgp6l5jvh7syy5jxfuzwp_uEtEbMCaJv8NUlFAyd6SkIRJ6jfJtjNcNgFDKi7-j5gq_e1Dx7U9urvUi5wJRQE_kWbpwTDp1qrec6vnARJ6OpqXTgUVj10LYQrwC8P7eGsX7YFONk7btopTvKwYq-hhraSvE_fmsbMT7QCjf0g1Z3FklkWsDSzOy5O4DNx07yn-XW8t5zlE0UxIvLh0xQIE-q3AVRlpSyComgCDAFDQWr8cN7-jSuNHFP8nXFSnUJPYB3Apd0z0shk5XjTjAe_SobLME3Eq25kr9GsMWxKoZRGBHMzBFYYVlchI1Cq0He_NYxWri-L72L2u-RLa0POxpr8kOIXkuQhckAyVCBvABVl5l3NHsfQVwVpV-l4MuRNgLeSJnd02-kZk7Hlh0bacXBX0ICsiqZNlea9MehYhdGJrL-Y4GfU_JIUkaglXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=UFsQ0OidagncQGlC4OPq6L11xfzpgz9Oo1rX1jGNtMIjCH8_iV0CNaa4bs6NpEil7JscZ2gV0USWA7utwRgg_INg7HNaoA63qh4CYTIWhczAdFuWcHZhtHMinKZlZ328ifesveeORwWwv_NyTR0JSTm7n_qnvsyOldWY2C8pFyZ2tXsTOu2RH3rxqLisaI3kTQWYdwR1xfuZ9pNKF57UXNmrfvrhNmhQhx-rMAuJbnkOCgp6l5jvh7syy5jxfuzwp_uEtEbMCaJv8NUlFAyd6SkIRJ6jfJtjNcNgFDKi7-j5gq_e1Dx7U9urvUi5wJRQE_kWbpwTDp1qrec6vnARJ6OpqXTgUVj10LYQrwC8P7eGsX7YFONk7btopTvKwYq-hhraSvE_fmsbMT7QCjf0g1Z3FklkWsDSzOy5O4DNx07yn-XW8t5zlE0UxIvLh0xQIE-q3AVRlpSyComgCDAFDQWr8cN7-jSuNHFP8nXFSnUJPYB3Apd0z0shk5XjTjAe_SobLME3Eq25kr9GsMWxKoZRGBHMzBFYYVlchI1Cq0He_NYxWri-L72L2u-RLa0POxpr8kOIXkuQhckAyVCBvABVl5l3NHsfQVwVpV-l4MuRNgLeSJnd02-kZk7Hlh0bacXBX0ICsiqZNlea9MehYhdGJrL-Y4GfU_JIUkaglXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=DtKrZAywixEMLCnVJ3jQRmHpfzXn57OA4ayiQmfbW-1m58Ac6U1N6CbMEGksTxKTL_IaxeiCYRs2OMh-j_NG2TwrosmyyJwImoCAzw6K4akwlFivZHJAyhmUssq8Rsqg8ajTnwlviuEwBYmydvL28YfxQvaFmmAkAiR2SGi61KhrUFLGf59Z99arqlzu9w_utpOGzJwfTp427ehprk5n8e-WpxC9D-z8tRvuRGnPpURkg8ohdxdF1z3d8vyM2u6rkf8DhexAz1zk4eMppbAT7uNHT7hvTPckBJdInlq5wP-7MIbz5XwrAmHfCMlCtk0wjDpV6SMx9vfTplLSx7RaEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=DtKrZAywixEMLCnVJ3jQRmHpfzXn57OA4ayiQmfbW-1m58Ac6U1N6CbMEGksTxKTL_IaxeiCYRs2OMh-j_NG2TwrosmyyJwImoCAzw6K4akwlFivZHJAyhmUssq8Rsqg8ajTnwlviuEwBYmydvL28YfxQvaFmmAkAiR2SGi61KhrUFLGf59Z99arqlzu9w_utpOGzJwfTp427ehprk5n8e-WpxC9D-z8tRvuRGnPpURkg8ohdxdF1z3d8vyM2u6rkf8DhexAz1zk4eMppbAT7uNHT7hvTPckBJdInlq5wP-7MIbz5XwrAmHfCMlCtk0wjDpV6SMx9vfTplLSx7RaEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHNpc1P7GHBgG0nR2QHt7CKmyP9kp7vcmaTBoBcitY0Q2eMs_r6h54kueQTGgGl2RdQVJtRGsymQDCqqllc1HMcnYvX8N-j7922cVI8BQnBaAC16In49N_cA1M9QGPHM2ahSWYLdbWbnFDRW_oi-GN_VY-clsUWo-563-8cEO021zePcygMqm7t485lmiI9oWyQ3caQsyC-a6AM5ot1boDYaqmonmgibTgU_RreaqjWy9VVd65R9MjU11UX1LUmkUGYCpDP9iP_QHK8LTkn0giBvwEADwbQvo1nxBE_jW68fatjS8ygovF0syXRga6irbqS4tFSOGZdldJqv0vHUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SjIdX94_OXXl_08uvTHqLo95Uii97JdR06J-0xwghAQ8_TYM2t_fGQx8Q3z7SzzkLj5huKW_7ySszX0EUZSRrIIfVy1aVEeHS5d5Kl3nLNvIM1l5MzzDdKCV2HCxG23A9-rcnJJ0baFLYKz4tIxARnRMKLodkc3eLREcdX_LNS0a0zs5wbsLBuy3T7f8dy7uI23e6CMtFGKD2hrQedrJmN4z4waK_l74LzFStF6xOeQWhfYB3o9-JkB29IhJuQqu7H22Ja7rUCN6QAFjqwQAq_sJ7kuppr8lp9cUdd4eo6kocsYw9-dzwkQ8LlBdHHDY-O4wMetMQDYNrTtCMfoYjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=SjIdX94_OXXl_08uvTHqLo95Uii97JdR06J-0xwghAQ8_TYM2t_fGQx8Q3z7SzzkLj5huKW_7ySszX0EUZSRrIIfVy1aVEeHS5d5Kl3nLNvIM1l5MzzDdKCV2HCxG23A9-rcnJJ0baFLYKz4tIxARnRMKLodkc3eLREcdX_LNS0a0zs5wbsLBuy3T7f8dy7uI23e6CMtFGKD2hrQedrJmN4z4waK_l74LzFStF6xOeQWhfYB3o9-JkB29IhJuQqu7H22Ja7rUCN6QAFjqwQAq_sJ7kuppr8lp9cUdd4eo6kocsYw9-dzwkQ8LlBdHHDY-O4wMetMQDYNrTtCMfoYjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRPQv5xDhns-4YvXiy0gr8mJ7MKvVdGzc8IOMEWkaSlQgqXU7aImd1l5XNAWoH2ynQYB4ouWN_p_wOtiPrs2-wCpEnNhDGYHSjYKoTX9j3qWINOzZNJtA9jhxx6sXzsrhzLz7ybjv_ZXgnHQC4ByE_PSLSjfyQyMCBEFC0O-BEotzyFFW2aCeOiB9zJTe2tmii2fk9Bla6ejvjIvYgAYbnb8LA9X4zIp2FsMfKXSnRUS-2q0lr6LqoR_JIaEuec8jIyFC1t6oENLqv_6KdOijultHywpk7OYiNO_kMH78vcMQl7zdyS_8HVZnDKXQg6cdlcolc3s8HX1Xt84O_oWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMql1NspM8lT3550nkb1cNNloGu4N65KYsrQWHarKwNB0YPC9Hcp0vckjnOskQsgW4omdHPEtvbRpiLErxPxSAxr6s1z9O0E6Xj0UDgvGsYTfFNstRDeRYkQ3VIS7O2o9QKbD6f1hK-HhbjCUQ6VfWDTmaDFxVxHIWUTsNFLqRoS1qhaYu_Dao0-YKfFNtvlf8kCgaBuu5Naxvl2mG2TZP2OyZb7siUAFj33-5e_xIQ4uYS8IidLSpH9K2_96SnwLGqqU2oMobcQdcNPE3KygEaLTVF675LfcIC-iHkDFu_BlS7BCdYUA9EeRRy6YZ9SlHBfTzpNcTnu3ztpNyaY3A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tB6nNWVhVZDDPG705m2_pW-qoDIoXnIpVvbGW62eDvw409A3zwiPmzyj3AZOVOk3gFRzgNP7fcee69QAmd7gY2dHKFO7OyTOByZHYks6sXWtwMFubicDn8kKVg30CvgEHEBiKnOYh3JloswoaQWPJsTxE4sZ96cWrV89kTD_p85aOwF6FuYkdKzrXXY7TXRYRWNpB4k0ucpWct5xtnDOCE7ljN5uBW1WrMCnIyZANlqQ4DiAIrRqTD5WvmhwY991WPOTKV_hdfQwD-2GxDklRL_jb3ZAq9z6N9M4Ex0dT2L-JLxGV2dC06ftECw4CWA6_39LlguX22hsN50pGzbJ4AmExEDhooDONpFB3XTFmau26A9R84gFHrc4_lDgZOnaN1O9mMN3zMJKFCoXko8SBAQChB-1OGiVoysQzx71jhHCd_7kx2yS-xd2onREG2fNFEcCKnIi4WKulj-a98K-Mq01hcRztO1O_MZ4OlLwJz5qwRxG1S0VU4ds2wIF-FtX05tRxvL7btEeT8J4KlI4oLyE5MRUYluYxNRq8vMEmYdvgG-LvhdHHDtU7YPStNIW90invmpYCKgWFQTym4x3jnl8IUi30ufCSekYAiMA1t4NZ8hTTGaqS-DidJKaegvXDqAcu4YYyfKJ8_VnrlAdXjp6iXSSW6S1GZ4wvyYqvK4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=tB6nNWVhVZDDPG705m2_pW-qoDIoXnIpVvbGW62eDvw409A3zwiPmzyj3AZOVOk3gFRzgNP7fcee69QAmd7gY2dHKFO7OyTOByZHYks6sXWtwMFubicDn8kKVg30CvgEHEBiKnOYh3JloswoaQWPJsTxE4sZ96cWrV89kTD_p85aOwF6FuYkdKzrXXY7TXRYRWNpB4k0ucpWct5xtnDOCE7ljN5uBW1WrMCnIyZANlqQ4DiAIrRqTD5WvmhwY991WPOTKV_hdfQwD-2GxDklRL_jb3ZAq9z6N9M4Ex0dT2L-JLxGV2dC06ftECw4CWA6_39LlguX22hsN50pGzbJ4AmExEDhooDONpFB3XTFmau26A9R84gFHrc4_lDgZOnaN1O9mMN3zMJKFCoXko8SBAQChB-1OGiVoysQzx71jhHCd_7kx2yS-xd2onREG2fNFEcCKnIi4WKulj-a98K-Mq01hcRztO1O_MZ4OlLwJz5qwRxG1S0VU4ds2wIF-FtX05tRxvL7btEeT8J4KlI4oLyE5MRUYluYxNRq8vMEmYdvgG-LvhdHHDtU7YPStNIW90invmpYCKgWFQTym4x3jnl8IUi30ufCSekYAiMA1t4NZ8hTTGaqS-DidJKaegvXDqAcu4YYyfKJ8_VnrlAdXjp6iXSSW6S1GZ4wvyYqvK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC2mpdAok1zvNECl5tm6Jq0U7K9NKoktP7VZKWe21DJIfC_5gciGMu-YpLpOyQC6wLLBBILtvBRF6I9ZmEOY3ChQLkUz3_Ypv601OVy7bxQy_Z3k-I8ejdjOvadaAmT4ipPXfF5RKyZ7ZiVcbDeBf_y0RZxL0juljYwDjgNeQxRTj0ShvejKZ1c0wtp13kMsKNI1VJSxrHMB2Dj5kV-x76WKRIoSqSdhEhKy7Fs89f7MB4_f8yDiSfUrObRUPd6I40h2lEXKyoG7S1hxfIQIVyyrcGVtSpcn4n6_uzwvgtSIqSM8sVV6itMwTO_eo7855onK_e6PE_qyT0bOupysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFRvNqbTy3pzJkzuhbg_0c-odcwHCLWScwtJ5W-2yMv5ha5tC7lS_1R5rSfp6jPpMAEKK2elN5xcjUV8U0ussS-cQ0yXrBw6r7hMM6H4g4VflZzR6b-f16qJgyC_J8DT6N0wtF6_wee6HvELU28PpCy8yEdj2bxnx7-oqANbGi028NzVEUNU0FlJV7dBiPtjL9GiezhrofYH9xDHiJyL9WhDa5G7WUTBYpzVjtRGKMxw2vZ_7yedV36AxMk0066kA93f57-mcoUMR5P0mMQgcTedV2fMJBgeP9vdLkqWOhK5SYciG7yN3BwEVwaFlJP97OTHJGM9bnyStR0ZmGF5qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=R8tUScCWPOPvrQaRZGjbpzyukmBLar765CvbSadmOmX6k4Wcmjd2J_vC5bQFLxgndPbAOmYmbjYb10h9bFJz8k5Rl4braheBgTEK6XvhXGr4CfkxS0DfIFhIHRY0_xOSL1R-thzUdxJlzUSoaJzl6XzTGibifSDAJNHJMf_hcxNdlrbgfM-JEejY0h-wPMydDMy4roIdzq_sbhUUxXh0CIM7LddJvdzp_93uAkzbc7RI-YIdB1pp7UyCjkvus8itNYEVyaeC0eCYP3u045AasiBGQOSrk-GKaHpWYb-egGx_zlhFEuvhEvMonFSkU7vlvEoN8d2eMWejc-IUov1KLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=R8tUScCWPOPvrQaRZGjbpzyukmBLar765CvbSadmOmX6k4Wcmjd2J_vC5bQFLxgndPbAOmYmbjYb10h9bFJz8k5Rl4braheBgTEK6XvhXGr4CfkxS0DfIFhIHRY0_xOSL1R-thzUdxJlzUSoaJzl6XzTGibifSDAJNHJMf_hcxNdlrbgfM-JEejY0h-wPMydDMy4roIdzq_sbhUUxXh0CIM7LddJvdzp_93uAkzbc7RI-YIdB1pp7UyCjkvus8itNYEVyaeC0eCYP3u045AasiBGQOSrk-GKaHpWYb-egGx_zlhFEuvhEvMonFSkU7vlvEoN8d2eMWejc-IUov1KLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=loj9XsiR3gzGr50LyYYReKoquld6uGuU4GubPuyEX8Qks0EFCgQYZZidAwIw4bkUDn4UZ4donSSZBfuTpwIZwFnRZ684U2USaInbaAfxFPuXL6uhqoW1ZoICV6SXYLjup7tr9pLbMUrNHLwImOdCcUq1SHR3bIowN5QUbO45CBTSxScaMuITjJnlXnUD91G_Yu5HAFqy1LJtxX94co6H-5bPKrX32vL8itmh_MSj8e6kUqf6Qk0F4DWUCZt2CEEF2gaLUjqCB6epKnyzgFtrsOGKoFUmlUySUS5HYksrF9wZHXLJTJAx1tZA2C7Y9ty9-cj9CD3I-j7cNFQdd2PBFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=loj9XsiR3gzGr50LyYYReKoquld6uGuU4GubPuyEX8Qks0EFCgQYZZidAwIw4bkUDn4UZ4donSSZBfuTpwIZwFnRZ684U2USaInbaAfxFPuXL6uhqoW1ZoICV6SXYLjup7tr9pLbMUrNHLwImOdCcUq1SHR3bIowN5QUbO45CBTSxScaMuITjJnlXnUD91G_Yu5HAFqy1LJtxX94co6H-5bPKrX32vL8itmh_MSj8e6kUqf6Qk0F4DWUCZt2CEEF2gaLUjqCB6epKnyzgFtrsOGKoFUmlUySUS5HYksrF9wZHXLJTJAx1tZA2C7Y9ty9-cj9CD3I-j7cNFQdd2PBFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=hetMrOmWJzW0zDf5GCB1OqBKXlcb_IZjC4VEHSCxNMc1OXf8MWbyg6U0VpUthIBKKqUoJHHJepiYO8GGEJSunMfh_cinYaVIbjS74l0cACfykTC9-msGVSslzAxAnkLmwNHZKM48G3FlG90-h2DG8AFLlxahXghw4E5KmQDiP4Svt5TN6Cz1RrwXzP3S4an6ucoMmjSHKgeE6tXrJ7XjGkHAqyoCpomeo24TsRXWFa15_8plcuZPOyNd6BDdOE_bHcAvcBr2xSSacyBhwzanCBZRxIFMaB4YMRdQFue0sjzD61ckauxMT4jTcjm_cvRTv1KELcYZ-tuK7KEP1gFM1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=hetMrOmWJzW0zDf5GCB1OqBKXlcb_IZjC4VEHSCxNMc1OXf8MWbyg6U0VpUthIBKKqUoJHHJepiYO8GGEJSunMfh_cinYaVIbjS74l0cACfykTC9-msGVSslzAxAnkLmwNHZKM48G3FlG90-h2DG8AFLlxahXghw4E5KmQDiP4Svt5TN6Cz1RrwXzP3S4an6ucoMmjSHKgeE6tXrJ7XjGkHAqyoCpomeo24TsRXWFa15_8plcuZPOyNd6BDdOE_bHcAvcBr2xSSacyBhwzanCBZRxIFMaB4YMRdQFue0sjzD61ckauxMT4jTcjm_cvRTv1KELcYZ-tuK7KEP1gFM1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bCFKShvPRgCsuKhlz8s3p1oVfJ58Hab3CClsj91jI-gdY2r9dhkY2VyMQv2khDNKLJtURq83ceqCq82SmUPOs62doCSXKZVa4Rl21wpaCtqxdQrgUqL_f5DQcjitf7EFeemu9lrz2C8RklMg1UAUZXnYIZGSe0HarBXJ0VeatgbSjVyggkHQOxgcopJAbGsV7vv2Vx171ROTs7lzbJ3Wdnxnwws81_LxHSmSQXXxTR133op5vlaCuyjQdlxlh-vDazrIrGE285EdQA_uvDRT_PT2rhz2Y1sXJ_nSigRfp4vANwkcTjQh7aro2qB9YudQvd1zTs0xJqcXAj6XsRU9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DmTZdKNhXA-7eKcV6yfrP6fTebnmIeZNVRtXIS0oSVz3IlJ656DAW-ZZ-HLvh250nxCz2S7rqk17yTmyy3Gj4B2pPOM5c_DVg0YmCsXBE4ECuGPHPS-x1OZsvj8G0-Lu9gUSI2WI7Eqy1CYgN6YzwPtZ8vdAYMxMHq7DcK2T-AUVrJ-iYoFUDxwsQhKOBhOHqw5XvRky4yzQNJXbXGCFAZ6gbYzE-_0FiWYI1z-dBS7a1U8yeNfHeBUpWYhK1mSUdC2TN2L5H1tPjm9B3UzaIZD99zMoYupEXySYq4VzYFBctcWwwnglxYDtnrjL-AlaI8Xagr1tsbqWAWZV31NtNs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8DmTZdKNhXA-7eKcV6yfrP6fTebnmIeZNVRtXIS0oSVz3IlJ656DAW-ZZ-HLvh250nxCz2S7rqk17yTmyy3Gj4B2pPOM5c_DVg0YmCsXBE4ECuGPHPS-x1OZsvj8G0-Lu9gUSI2WI7Eqy1CYgN6YzwPtZ8vdAYMxMHq7DcK2T-AUVrJ-iYoFUDxwsQhKOBhOHqw5XvRky4yzQNJXbXGCFAZ6gbYzE-_0FiWYI1z-dBS7a1U8yeNfHeBUpWYhK1mSUdC2TN2L5H1tPjm9B3UzaIZD99zMoYupEXySYq4VzYFBctcWwwnglxYDtnrjL-AlaI8Xagr1tsbqWAWZV31NtNs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=urDCE2sopizXyl4UARrfqrSdYD8k9Ab5SmFwuX2E9vzMZ_ULD8dJsOoylMzL8OWsbxJ_rU3E97nuRLyd0c5GI3VoKwyCcYiuNiwnkAARKnKJTqZUxRmNq7PLw0kinRUS-qDCLOIlo0qTXM_dxmEFBeKMwMXZtjRZvXVucMRxnZEPRzQqwTOuHwReJNyQimxorERjhFYm4dsA_m0NL2KAV3iVdACHGG6Ydtm1CmUkzwxORMdR6h4-WtEACOs-c9HlnzUgU3N4ZnSOOnL33K4dsS00lC700ajZSl6WMNgq__29TAWOImFphjG68xOQo-09Tf89VHIjusavngqGwVyy6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=urDCE2sopizXyl4UARrfqrSdYD8k9Ab5SmFwuX2E9vzMZ_ULD8dJsOoylMzL8OWsbxJ_rU3E97nuRLyd0c5GI3VoKwyCcYiuNiwnkAARKnKJTqZUxRmNq7PLw0kinRUS-qDCLOIlo0qTXM_dxmEFBeKMwMXZtjRZvXVucMRxnZEPRzQqwTOuHwReJNyQimxorERjhFYm4dsA_m0NL2KAV3iVdACHGG6Ydtm1CmUkzwxORMdR6h4-WtEACOs-c9HlnzUgU3N4ZnSOOnL33K4dsS00lC700ajZSl6WMNgq__29TAWOImFphjG68xOQo-09Tf89VHIjusavngqGwVyy6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFE7vKcnfycAcXOSzh6TBBL7B8jdoPMB4ZI0Mn4Sc16XxUEIjDNd8cAse5rD_Wv9WNgyjW9f9CBzPfIHuHNNwYUG7kubm-IBE40VuNw8jij4v_vf2msBW_ACkRIVtd1pMrIBuIk2s86yGYwRNS5PGSI59ThlZ3Q14TUArNeg0ghCLDaD6Z93RYGQG_YEmMnLAs1W2T78dVzXC7VScSy-BC4D3T_wAaIrl7pUNNGQyNbagyLaXirTOr_er5ulGQH5cByiLvVdSFm9rWjZu_OPUTg9aFTNanDLsNGGOqEDg4FSVRnobZHBonPaaRPSzwqKOQlvMd09wKfOP0inUCdTcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=LLxaBvRZYLpXNoOpiqfAtZx9S5QcfEILfhsHpjWLMIOOOiYkfAFaHrwUhPgy9MWVF-mC_JjjIeGUx7L1KHCZRVGNDLv95g2d6biKClR4YWNf61-dJg9zwFzlmGZv3m1sEUDLFkRPnbaj_zIbtnX0qvBfNRcV1KiudGkmf3eHLIYpH2N6sXD7bwsgTwARGM1NeiiERyIPLo-j3Y5LGKqdqHFw5QQ4_CTHkV58-v9O9nR9jDyxWBXxyXrB-181MV_vCAHd5evPuDLlG_JnQnP-y4n1nGX5GpT9nKDlzBRLJ7wq8f3b0u9HxZCK-V5UyrtoICVQYzntUM0tQrLpWTASvaHs9zSpcRuxBAeAeEMWHzybK9xRszqCTAlnb2W9a8BTEYCS4e7uJy4inErrcAmdrLcVdA2Fh1NO17Z0xd4fO1C7rk3NaR7q7EWr6JAqUsL3syoJodfRxPs-P-mkWLmymKrOMPFvNSKludfqvJQkguxSsjHS_nx7wEAq_-84d9aIY_2inz1Vyigffpg0YRi6fYHZrIUbpDbIbT2OOfstSqH6-j3s-1IxOm0OZHHy8oEVgvDm3phvrU46XU5X2FReLW8j1vECMdasvSHjkEW63cc8NIyt7e6J2uouXBNqh984TQKhKEbpqq0uRYvPmp8t7rvKSgNYxWitsLS-R0uHM6o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=LLxaBvRZYLpXNoOpiqfAtZx9S5QcfEILfhsHpjWLMIOOOiYkfAFaHrwUhPgy9MWVF-mC_JjjIeGUx7L1KHCZRVGNDLv95g2d6biKClR4YWNf61-dJg9zwFzlmGZv3m1sEUDLFkRPnbaj_zIbtnX0qvBfNRcV1KiudGkmf3eHLIYpH2N6sXD7bwsgTwARGM1NeiiERyIPLo-j3Y5LGKqdqHFw5QQ4_CTHkV58-v9O9nR9jDyxWBXxyXrB-181MV_vCAHd5evPuDLlG_JnQnP-y4n1nGX5GpT9nKDlzBRLJ7wq8f3b0u9HxZCK-V5UyrtoICVQYzntUM0tQrLpWTASvaHs9zSpcRuxBAeAeEMWHzybK9xRszqCTAlnb2W9a8BTEYCS4e7uJy4inErrcAmdrLcVdA2Fh1NO17Z0xd4fO1C7rk3NaR7q7EWr6JAqUsL3syoJodfRxPs-P-mkWLmymKrOMPFvNSKludfqvJQkguxSsjHS_nx7wEAq_-84d9aIY_2inz1Vyigffpg0YRi6fYHZrIUbpDbIbT2OOfstSqH6-j3s-1IxOm0OZHHy8oEVgvDm3phvrU46XU5X2FReLW8j1vECMdasvSHjkEW63cc8NIyt7e6J2uouXBNqh984TQKhKEbpqq0uRYvPmp8t7rvKSgNYxWitsLS-R0uHM6o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBD9mGGGLbvjc0F8Ysp7eynz-HEpjTGFzd7Sxgo6t4fSAFeGWzyjOigXhM3tQUaGdFbn2OhmA0rfLpqzj-2Dyw2uy4jqW9m0D65fLMM6jznxklEDEk7IN2XTQPxg0FeHhZcM50A6pPGchDRKb_Ne3YGAaRaywyU7u8Qr_1oSZsQc4djiGPaULJGso76sbTfk6Le-uTCMHTUfitKYjA9zTd6gOqyEn-ohaizEugaO11MIxtZIJE8LG86QEV2mCQqbLCtOWXxUFVtTTwaDKxi1EBFtOfB3zJuM0N12sKYjNEKtfknejt8EYj9KKqr-tugtfjTFJ9PY70sF8FPP0Q8UbQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=fbCVDBKvblQJeIquKAKI8M-LboF4KgO9lSdv8NzZiW1X5SCNGjvUhafIO-CKlQk0No7iyvkUvZUMHxsnyPjmsTfw8OIxNc22VG6eFBcQdrC82zBYVj_7Mho7p9TZ32zIsMq4yOyPwJh1Tz2tdxu2HoNBQMdMP3ukBb-uDc_OTZQyZUJ0nWAE7swPcGm2xYCsaaJ2UXWoEmqR3LaEqb281pNbZzkg6S1YLcYZZLHpvGe0o9BUPCvsBw6xpghS1kohrM85u656uP4XMF6FsHZjGnaXPe0kBFAqApn27FYKYhwt3ZCW3pGTzJeFInwt6BimNcu7Mrg_wMWOBtnzBYnI_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=fbCVDBKvblQJeIquKAKI8M-LboF4KgO9lSdv8NzZiW1X5SCNGjvUhafIO-CKlQk0No7iyvkUvZUMHxsnyPjmsTfw8OIxNc22VG6eFBcQdrC82zBYVj_7Mho7p9TZ32zIsMq4yOyPwJh1Tz2tdxu2HoNBQMdMP3ukBb-uDc_OTZQyZUJ0nWAE7swPcGm2xYCsaaJ2UXWoEmqR3LaEqb281pNbZzkg6S1YLcYZZLHpvGe0o9BUPCvsBw6xpghS1kohrM85u656uP4XMF6FsHZjGnaXPe0kBFAqApn27FYKYhwt3ZCW3pGTzJeFInwt6BimNcu7Mrg_wMWOBtnzBYnI_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG4IAByIU4b_-ejk-USJ5OOtXvH3KufAoTKJn75xogXjMADz_F-LHp5uP5-0BAfHXZGi0suzGZBYb965d5JFbw4B4n8xXnjgIiI-jGPx3UIXQDpa_Y7vGgZLeAbCedgMshZ5vrar9bEJV9xhlv9F0OYv7GiR0eWRmdkBqnb9Zc3ns0bhuZNmAM0_KtMkQOv4O-dlgtUnCrTnE0ASuLAtF5cTBlc87kWYovD2S4_8-JrKH-q03clmw0RFdm8wY4YuI67ujI-1vY0nqXQOWu9ZQIBCo8mqaag-63urG3cq7pbtavQ30ZYe0tLJTdW8lpR7m9Bxd-QYvgaNUoqBYyaysg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hj3SiwEJbsGAkX8pZBbccdINtHH0UPidE5T8raSCGibBU77c2zs0HEkf2Y5UmnO8pirwRzInQsCjSS6qjgwnp2-538m-INtWvINRt4p958wGG_qVB7AM87GHRurIxKOavSiBkxpFmONP23Yde9obry_U-P1YXsd1h3bYZtLtVZhz3XxuYM4oMX6_Z1TsfopXochAi05vCUI_oual6b4KZpEgRjDZ2WcL86P8I9m8BxUSFQcP233_IRY2D9xD3puqaALaRGwfm0Vu0YDc1iNDTmhX_N8t9ojmKm0mVkGEYUFgWBCJtlMDUja2w33Wydh_hyrhoetokqV7FrQAUrtaOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HcInOYuMOpvRQLLWGTejVIPI_BfBhpaUTByE-sq9sGq5TQp5I3usDot9tmtqInFaju_N5WS19jZp4o6u9TVDohFwDWKvTPzBgpj6QQGOAYtlcdFzy1oXIxuXXRETWh5DKvHSxfWtO8gbkpobfpFwTtKuALskz6y0JySgjXuQKLoiNcTTb4yuPcownrclu_n1JFx7y6GhBYE1R4U-PD6P3R2gYRsaFOQatt8BMuzvRdWkukPlV0vOnfeXfgge5BoHJy3LrDR2DNQD2ge7pDvMR52q3XAhNC7I3GvLj_9XLU482f30qh-rgDGf_I_XLgpltfcw0Rm9IAR2vNxNPzyBeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=nKZ-WHmqNpeA9vi5ccRElU4OMt_DF3dV_VzfTGaaMgzMzDD1rPkPeC0iSC9o29elTDfDZ37GYw0S1jIrbM-Yz1HjIpr2xwovV2tlvYFeCXE3Rvgh5fsu6SvLTmowpqZUAg0fH1vf0H9lUgTC9BA2iYc1Clm6qqoN7Nu_69GmM4Sd6BPfwnuQoH_fIZszTAHi5NF79HXVw4amhONhK0YBpg20GCiU8m3omIWngY4RLQFMO8w8ccIEhm_FcZvUxU1-mCYmOuSFjkpJQK0JWiDaqdU9N1HbjqdyjZO2mEcUWEa2mvQLViXjk7xbunbE-4Ivuc5bh-0-wwM_2v2EZ8ymAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=nKZ-WHmqNpeA9vi5ccRElU4OMt_DF3dV_VzfTGaaMgzMzDD1rPkPeC0iSC9o29elTDfDZ37GYw0S1jIrbM-Yz1HjIpr2xwovV2tlvYFeCXE3Rvgh5fsu6SvLTmowpqZUAg0fH1vf0H9lUgTC9BA2iYc1Clm6qqoN7Nu_69GmM4Sd6BPfwnuQoH_fIZszTAHi5NF79HXVw4amhONhK0YBpg20GCiU8m3omIWngY4RLQFMO8w8ccIEhm_FcZvUxU1-mCYmOuSFjkpJQK0JWiDaqdU9N1HbjqdyjZO2mEcUWEa2mvQLViXjk7xbunbE-4Ivuc5bh-0-wwM_2v2EZ8ymAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkhwXu9HFBm0Ut9DJyQutABvFNuP2lDXzx5hSJuEpfS_zOqfEECcBS6MnCVU_uYg318dC537voXz2i9hdOJ8kSceV7iCCOCzTbjbw7tFvNp3wWxIvImfen3SleV4Q-3IxitC5w4Uwz_yM2RTuIsEAAOZLNwj9NmRToVL5bmXLB1YcqPn9xGK3DHdvstH8De0MkMugT-KgidfZcfj07KQMfYfo03SVpRe5j4Erp9Ouzjk0OxC5ei_6AgYh3MlkMr_WgoW_74eMqFJcxaK3jKcgUDe28P6xQOLEEMVAmUppvczJcjtMNxE-Y6oJLJthXWKgx8AJTSUdO7l1KHtfxK3PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5bb8B4ja_5iSazX9W_WrBdqqpBRw7pf49XAY58a-V2G0saMDnyvp6wiyenC1z1I8JjNAa7jAyBMsFhGc35QfVXmb8qYIC8rTbkpKGeT5d6hi7hkpB43qzvRF1XgnSPYApwaQjTAr68j8qu5NTlfj5jkv63YO7yRHs0_pkNiYYO9LBDey7ELXSJ7GltDww9SPLjBwnImBTITH8ZxG38mQttEjuOcHicZTRso9Z18KA0MLaMl__Xvb-jnBJl41Zh1HaYxKT7fmSpYYTD4QjtVqfi4IG2mrD1FiVAW5Cn9R3Mb5temYoFgujGKfx2144cQoCdsC2rwys_jU7lC9OFU-dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu5bb8B4ja_5iSazX9W_WrBdqqpBRw7pf49XAY58a-V2G0saMDnyvp6wiyenC1z1I8JjNAa7jAyBMsFhGc35QfVXmb8qYIC8rTbkpKGeT5d6hi7hkpB43qzvRF1XgnSPYApwaQjTAr68j8qu5NTlfj5jkv63YO7yRHs0_pkNiYYO9LBDey7ELXSJ7GltDww9SPLjBwnImBTITH8ZxG38mQttEjuOcHicZTRso9Z18KA0MLaMl__Xvb-jnBJl41Zh1HaYxKT7fmSpYYTD4QjtVqfi4IG2mrD1FiVAW5Cn9R3Mb5temYoFgujGKfx2144cQoCdsC2rwys_jU7lC9OFU-dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=iq6-_9ocThucfFgK6ZImUk1bHQfyCviLJ_MUkTY-ag9s5ooz70u1GDRaa4rKIqH2t3fesyhryNYGX_R9X9XHowc_SVhllFWIYWN2e7YK1_ut22tjDMn8lZc-te-ybin7tq1nw09fDTFHW0DC5digjhCT6EnFaI4LbQdHh05fhI1YbrweB6ia7JRHTJNQPBaVeWT9OnkzG19a0O7BnZvrGmpd5GmgEuEH6OtAljSvd4pFbXTxB5P_GoUMMaeyBfe7z6Qc8mREOw7WcOwRseZyxlJMsDOC3vyqbRN8jjfKX98KvxMM2VWK0iZYhvlY6GFTB-zTjZYduuPH3lkLQjMGEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=iq6-_9ocThucfFgK6ZImUk1bHQfyCviLJ_MUkTY-ag9s5ooz70u1GDRaa4rKIqH2t3fesyhryNYGX_R9X9XHowc_SVhllFWIYWN2e7YK1_ut22tjDMn8lZc-te-ybin7tq1nw09fDTFHW0DC5digjhCT6EnFaI4LbQdHh05fhI1YbrweB6ia7JRHTJNQPBaVeWT9OnkzG19a0O7BnZvrGmpd5GmgEuEH6OtAljSvd4pFbXTxB5P_GoUMMaeyBfe7z6Qc8mREOw7WcOwRseZyxlJMsDOC3vyqbRN8jjfKX98KvxMM2VWK0iZYhvlY6GFTB-zTjZYduuPH3lkLQjMGEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=mBLAgqfThbIGu-XWuAf9ioxbkjY58xbzxszufNk9i_9BZmUCvlzIo7GG_-B_rQoIxeztQpGDYqiDW42m4CbUsSgXsVODCY2xS_9SisRl36NgT9TDw9MbXiH8dvLMyfeIE4JMkdS6A8P_WA6Em-dAWRssCJqSWEzeAplS1kJdp--6CHjbqvlkqMzhh3EExIKk6SCIwFqK3WM5eJ-C1-1YLOqTN3wwSwVhFWwcnRIV1nYtOhYPjrR84uZZ1VL0esRBeJ8GdVAMW8CZeXwrmdZSzLOMLYJD0Pep7M25HwLY8ZUX1xMe44kHzDqptokRW7nkPYkdu3vllF24B6MhfAbFKIvs-gmf8S_JKipjohsyaToOSJZx62E02F03Hklq_k94OQ9mWXexsvYmN6A3i8rj2-6ajCIMrc-P7Uf9CivBChu7wMvxIOzdEK89ccOUDrVWjG541S4XeBgioRtOZVbrHpA3sDTW3TPbOGdymVqOotf4_Z1D-cyV_dpqulXKC9p6pDG-w3brsdqtrrzPClaHukenf_Dgy8L0qOsha3cxm6x8iVbYTBo3sx4BLKzQc8pt27YXDWOyWOLjsMbkvP137qK8sSfjBB8ni43M4aietfsOvvptPAdRB63UDp4ckj9uGGpuDzH5sdqzTnh4CGciuJqkubJyiJbML0lbZUTVPjM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=mBLAgqfThbIGu-XWuAf9ioxbkjY58xbzxszufNk9i_9BZmUCvlzIo7GG_-B_rQoIxeztQpGDYqiDW42m4CbUsSgXsVODCY2xS_9SisRl36NgT9TDw9MbXiH8dvLMyfeIE4JMkdS6A8P_WA6Em-dAWRssCJqSWEzeAplS1kJdp--6CHjbqvlkqMzhh3EExIKk6SCIwFqK3WM5eJ-C1-1YLOqTN3wwSwVhFWwcnRIV1nYtOhYPjrR84uZZ1VL0esRBeJ8GdVAMW8CZeXwrmdZSzLOMLYJD0Pep7M25HwLY8ZUX1xMe44kHzDqptokRW7nkPYkdu3vllF24B6MhfAbFKIvs-gmf8S_JKipjohsyaToOSJZx62E02F03Hklq_k94OQ9mWXexsvYmN6A3i8rj2-6ajCIMrc-P7Uf9CivBChu7wMvxIOzdEK89ccOUDrVWjG541S4XeBgioRtOZVbrHpA3sDTW3TPbOGdymVqOotf4_Z1D-cyV_dpqulXKC9p6pDG-w3brsdqtrrzPClaHukenf_Dgy8L0qOsha3cxm6x8iVbYTBo3sx4BLKzQc8pt27YXDWOyWOLjsMbkvP137qK8sSfjBB8ni43M4aietfsOvvptPAdRB63UDp4ckj9uGGpuDzH5sdqzTnh4CGciuJqkubJyiJbML0lbZUTVPjM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SiUwarNQJTsg4rHp25_n6Mr4N3EyWl8sGXmbsbcXkcqWFLFbyjXcVdVenMNEz-O1gQo8_U5FwO_Hi7swtf-Zlqte_xb7DegUGFZ8WmXhy1b_M1jbdLL5bfPU1a5UVPBQsbQL0KVQUngDOmVq9Qu7upux-V9YdJVhCxF_ESM7NodwnQdFU6ifXVhJemiSzUtH5HQtABQgC-MaQYoMdAkp_YkIadoACgIF5MmKFFexbhqinZiTLHnnGX1vdXvzQuEt-43oaQZ8LY6blIOzdSHGPPDXPky3rj0_bhvyyBH1dLODrBN9m2NFVo0NlNuyhr_Aq8K4FyKpUnMqHT60imp9HQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SiUwarNQJTsg4rHp25_n6Mr4N3EyWl8sGXmbsbcXkcqWFLFbyjXcVdVenMNEz-O1gQo8_U5FwO_Hi7swtf-Zlqte_xb7DegUGFZ8WmXhy1b_M1jbdLL5bfPU1a5UVPBQsbQL0KVQUngDOmVq9Qu7upux-V9YdJVhCxF_ESM7NodwnQdFU6ifXVhJemiSzUtH5HQtABQgC-MaQYoMdAkp_YkIadoACgIF5MmKFFexbhqinZiTLHnnGX1vdXvzQuEt-43oaQZ8LY6blIOzdSHGPPDXPky3rj0_bhvyyBH1dLODrBN9m2NFVo0NlNuyhr_Aq8K4FyKpUnMqHT60imp9HQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvLjLB-BwDdSBK5EeKyOM--3MQdgM7ApnLifOT885ya64RzqJmGIm3qWz2y1i-7hej1oWvzvr4oypMFLWx4Z3AQWuz4794IQeY6KoqdCybvxLfnkkelYFy2l9UIZJ6Y4CBlDHMmBfsK-rVQen0y6E-5poZHLYSIg2Sc5C_vESl-ibnguCpNyZ67bNxWKBqiQMBu86njYwH-FOmkUJPLa8ygHUpeDKuwO84X44-Uvs9R5ekF5_BGuo7AipiGN5YoK4XoszfC7vRMPbVCg9um6YP4CrNaOaJfIbCy3IyQNu6IXg3e9kpFvfw0CdLPqV9IErZxycbVks8uC1cbN6Acaqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=TBo_ymIR2sFLCM5ALC4DvfCL2eDhroPaFzBtYt_tukDExJisFWB1EUD79Y6RfND0Ut63IDg2x9KWGdlRazqgAzMiQtIWt5U7escIxJ1g6U2NwPY_v_km9sYyIIclH4RX8S6Zr2rtom5PHBieaNCTxL5Q15qre8zhqUIKulk4h0ZRjAtSTEjR3VgtsZuzxw1UGKxs-lyttKoq-Jkzsasx7G-TQeRg9-53K01i8bnFac4gvPsZrbWcf6QlZnRYelCYc11ykOuhdSu-rb3pVXGYm02JnLOCEsg8gPK77zCLw0lBnPbFaicBWs5wmEAgOR1IE15NOKJE0_CVSST6SldHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=TBo_ymIR2sFLCM5ALC4DvfCL2eDhroPaFzBtYt_tukDExJisFWB1EUD79Y6RfND0Ut63IDg2x9KWGdlRazqgAzMiQtIWt5U7escIxJ1g6U2NwPY_v_km9sYyIIclH4RX8S6Zr2rtom5PHBieaNCTxL5Q15qre8zhqUIKulk4h0ZRjAtSTEjR3VgtsZuzxw1UGKxs-lyttKoq-Jkzsasx7G-TQeRg9-53K01i8bnFac4gvPsZrbWcf6QlZnRYelCYc11ykOuhdSu-rb3pVXGYm02JnLOCEsg8gPK77zCLw0lBnPbFaicBWs5wmEAgOR1IE15NOKJE0_CVSST6SldHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=ZDb70xTH9M4ebDpC2Cdo4DSIasQT6EoOkKEFC7q4WautA53DFdpl5YRRJ89FN8YTDhuxipcgFBMFJd8Y-zWFJpdDFhEwIIPfY8A0vsAojtaSO0_zAwVu02Lg-1LfL6ZoxNeSvAfnLTs2Lx3SVROwqGAc13wlAoPk66sT8jJowmLs5UVpeyXo-XIn69Acp5EgmRzErJADcwgi20qmyVroOAJ8R_Mt9dgq0d3glDkvMIn6ndy4zkkoLGY5al_7t4eA_cUj7Z6yvJS1i6HIL-_VbwJyZXGsa6wUm58htb6W7bCa2slwzJcZ8ZbV4DOjYLpxL_UzzvS56N-SFhfmFaGaPwsA-Rva1ZAT6l8Wvbn2BXTyJDh4xa6WrRY_5JRNDcVNmy8gF9vcnOhHjvQwLi_gRZ2JCkQPHC8jlCGzumno0KeGcCp4yqkZglm-jWATNPlQgCKhLfxQuub14_L8LN-_tg3ZvP7q9iX7myCftHesM88UQ7FXns5hhjZTiefuNbm3RejPY_ERgu-bv8cJP63QIDXQaRDHZztnxU_Qxhhavvo-JPZ2xZBV-CslKJn9NLXavZS1dM5Hd9sy0GA9TmqAE_pimxL6oXZyE9QmS5rGioZ8hTcg9IfSM23QCmr9bYVrgAYh1zGeOHLACoxxRdaCWKG2aovE0IKy9rK1S9mPbhI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=ZDb70xTH9M4ebDpC2Cdo4DSIasQT6EoOkKEFC7q4WautA53DFdpl5YRRJ89FN8YTDhuxipcgFBMFJd8Y-zWFJpdDFhEwIIPfY8A0vsAojtaSO0_zAwVu02Lg-1LfL6ZoxNeSvAfnLTs2Lx3SVROwqGAc13wlAoPk66sT8jJowmLs5UVpeyXo-XIn69Acp5EgmRzErJADcwgi20qmyVroOAJ8R_Mt9dgq0d3glDkvMIn6ndy4zkkoLGY5al_7t4eA_cUj7Z6yvJS1i6HIL-_VbwJyZXGsa6wUm58htb6W7bCa2slwzJcZ8ZbV4DOjYLpxL_UzzvS56N-SFhfmFaGaPwsA-Rva1ZAT6l8Wvbn2BXTyJDh4xa6WrRY_5JRNDcVNmy8gF9vcnOhHjvQwLi_gRZ2JCkQPHC8jlCGzumno0KeGcCp4yqkZglm-jWATNPlQgCKhLfxQuub14_L8LN-_tg3ZvP7q9iX7myCftHesM88UQ7FXns5hhjZTiefuNbm3RejPY_ERgu-bv8cJP63QIDXQaRDHZztnxU_Qxhhavvo-JPZ2xZBV-CslKJn9NLXavZS1dM5Hd9sy0GA9TmqAE_pimxL6oXZyE9QmS5rGioZ8hTcg9IfSM23QCmr9bYVrgAYh1zGeOHLACoxxRdaCWKG2aovE0IKy9rK1S9mPbhI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uDdsQkZQsFhDdpUbo6Lpl8b1DezteyW-XhYHcEjthGIgMp4x_KrP5jaoCr3k52_-xhV860FVqpXDHhWGU9V6WAMbGkKXCbRllQD_pCV4uaEJiJuP7NE_HOUX3iV4leShLH864as-cs2Qh7o2gQD-UBoORGKuzqTxl_7VYIhlNykPC8poTbFP8j9RfXNAXSorYevN0-M_3EbqRH6_gg8IfgNSamUWCdEOj9Yf4Vbof8zRtZzKISW-8LH7FlPDyXBWzV9TfnuRDpUZ9at-5Wtwgwg81cHg2rjxkFs87Zy_IRjlXAQxFF51j7FzBZycLvDaL-iy5icFfpuqMtkp-ToQqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=OIhQK-2iz7sRi9fGnHvIf64NZDc6s9S7dVQr3NEpYgiFVCA2QObhRaCeZukDsnmdKNkZRae7RdxRaLBiutLxm5AyttuEtPtdJyRWM-DAOMavFMwOaCNVQowzxl52swi4TDxIRKavyGohhmJgVgAgWYNkQgN3DP46_h7C5DxK9vjhRmJBm4ZiawQjliwb5mv_8Ud54PJGYwiqfbzkNZjL4b1rXEXmz3OaS-u2nKcub4wWYfs3nhU78um9-OdwK8rhs4wRVPM-y26aD2GFwxtfpaxvhQabBgIMVEnBgZjwXiJer8ECdYH4cQdBFg1cjUX8zAJAaMMRQrhONQnLz4L0P7JMoFNZLSjd7h2DxO6gE71ZJs5uGDWCjhGw7l0IVOCkg0mQTr0InAju1tw4f8XnWAHdg0bo0VExuP7lNk8iVgPhF37xZeVADFHMo9S8t2MENqpS0LyGqSUxYA5nVAzFg08ElQ3DChVhY1aLYZiZAS-_Lcx8r6J7BL6QzpRh3enHSaSo-0peVfZT9fMFWKQLgOp7j6w07kvLC1KMSS-yMqTQYle0cMNK53jIu8VzrDZtSWB_PEzJoP6UjMwETcy6aTT9v3jXJ8ZrbtCPVwZApRaAI2qPYV-jQnRH-IWMCdzlTVYJC_WknS-2n4ZDZpJdqkIwvD0MDYJse7xDREcp8V0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=OIhQK-2iz7sRi9fGnHvIf64NZDc6s9S7dVQr3NEpYgiFVCA2QObhRaCeZukDsnmdKNkZRae7RdxRaLBiutLxm5AyttuEtPtdJyRWM-DAOMavFMwOaCNVQowzxl52swi4TDxIRKavyGohhmJgVgAgWYNkQgN3DP46_h7C5DxK9vjhRmJBm4ZiawQjliwb5mv_8Ud54PJGYwiqfbzkNZjL4b1rXEXmz3OaS-u2nKcub4wWYfs3nhU78um9-OdwK8rhs4wRVPM-y26aD2GFwxtfpaxvhQabBgIMVEnBgZjwXiJer8ECdYH4cQdBFg1cjUX8zAJAaMMRQrhONQnLz4L0P7JMoFNZLSjd7h2DxO6gE71ZJs5uGDWCjhGw7l0IVOCkg0mQTr0InAju1tw4f8XnWAHdg0bo0VExuP7lNk8iVgPhF37xZeVADFHMo9S8t2MENqpS0LyGqSUxYA5nVAzFg08ElQ3DChVhY1aLYZiZAS-_Lcx8r6J7BL6QzpRh3enHSaSo-0peVfZT9fMFWKQLgOp7j6w07kvLC1KMSS-yMqTQYle0cMNK53jIu8VzrDZtSWB_PEzJoP6UjMwETcy6aTT9v3jXJ8ZrbtCPVwZApRaAI2qPYV-jQnRH-IWMCdzlTVYJC_WknS-2n4ZDZpJdqkIwvD0MDYJse7xDREcp8V0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Lt6FKMNe7Ie2rDSYppc9N_OQ9DBv1-HIv8ZVMQlYYJaK69fkux2CD6S-DGvvHiYmSJ6rMBxJCmbDRZ9CuVlR_AgrfDnPB9IuMjkGNhQ_RO5-HjkGNdFY95o3CQ5krXc7VRzfUMgaJFl2neF6spqDloZWCVYEF1pqv-6KSbMo_TAe6GgIFYH_Dd_mwDlDdaRs-tTvFOqivv0_hURPslm713DCjcwVPuIzV5rVgMD5HGX53L2toorh2UqUUych5i1opQ_2Va5127NZV5oncB9LB1veRS_tTbH2WLJyrbvgZ1TUvc2Xor25qlUDAjNgwufpf971V8cBDNKBVpvijDmH5zUoOv5NTkI0LD7KByOj5LEUzelM6bHDD0LpyHK0-Rbdk72eLsDhD0JE_Mg9mNtxZL1YetTe2tN5jSdFvGAtY3QgPhmLSjQETUvU7jA6e8FglZTtZuzSM7KBdmM8AB-1Kb3NgRnDk_ClK8mpf-0yEi9KN_NDgOZrCSy0kL7szhXddNSHO6F3OBkCkWVmQGE1dwEc3kXPh72lg-S4558lpH0hN1sgc30aihTvIaETSUX7ESRWB2HW3J9IHWeVTAjbOvz1FwQwRHnWocP9bPtTcN_qAymDkc14_UWEC2eGk3CbRp8MHoM3qUG-j_drHtq0dbuMHMjFCYdhylGQ5fIRlJ0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=Lt6FKMNe7Ie2rDSYppc9N_OQ9DBv1-HIv8ZVMQlYYJaK69fkux2CD6S-DGvvHiYmSJ6rMBxJCmbDRZ9CuVlR_AgrfDnPB9IuMjkGNhQ_RO5-HjkGNdFY95o3CQ5krXc7VRzfUMgaJFl2neF6spqDloZWCVYEF1pqv-6KSbMo_TAe6GgIFYH_Dd_mwDlDdaRs-tTvFOqivv0_hURPslm713DCjcwVPuIzV5rVgMD5HGX53L2toorh2UqUUych5i1opQ_2Va5127NZV5oncB9LB1veRS_tTbH2WLJyrbvgZ1TUvc2Xor25qlUDAjNgwufpf971V8cBDNKBVpvijDmH5zUoOv5NTkI0LD7KByOj5LEUzelM6bHDD0LpyHK0-Rbdk72eLsDhD0JE_Mg9mNtxZL1YetTe2tN5jSdFvGAtY3QgPhmLSjQETUvU7jA6e8FglZTtZuzSM7KBdmM8AB-1Kb3NgRnDk_ClK8mpf-0yEi9KN_NDgOZrCSy0kL7szhXddNSHO6F3OBkCkWVmQGE1dwEc3kXPh72lg-S4558lpH0hN1sgc30aihTvIaETSUX7ESRWB2HW3J9IHWeVTAjbOvz1FwQwRHnWocP9bPtTcN_qAymDkc14_UWEC2eGk3CbRp8MHoM3qUG-j_drHtq0dbuMHMjFCYdhylGQ5fIRlJ0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=v97R32wyKOPK9cV6gW5BBpKO9IvJM3XkgiYUlmB-FzGbnqNzUU0424qBNQ8q4YeIp9VD2a751OYxCQNO7dxl64ncg3PvlTTcEV_GhJd4GnARcEC76PkoZeBu5U4DZmpXqTkpd01JBwMPOOvErVLAefU38xcXSot4Ey9XqjBSFA_O20xpgezakrLMISI_2O5BkQ0xQ1UxcuCBxzc0UwfepCTsHAeaFzYDujBnZIAH1Wk8-eWD3Ql7lyVqIlG0rEyYdRdooQMcUSpaA9ohWdOqyWXYSV0t9tQiuPMCIAX7OADgdibvbMeOSwFsHkZxMblzpbGaCQM5v2psEiLjm8DDHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=v97R32wyKOPK9cV6gW5BBpKO9IvJM3XkgiYUlmB-FzGbnqNzUU0424qBNQ8q4YeIp9VD2a751OYxCQNO7dxl64ncg3PvlTTcEV_GhJd4GnARcEC76PkoZeBu5U4DZmpXqTkpd01JBwMPOOvErVLAefU38xcXSot4Ey9XqjBSFA_O20xpgezakrLMISI_2O5BkQ0xQ1UxcuCBxzc0UwfepCTsHAeaFzYDujBnZIAH1Wk8-eWD3Ql7lyVqIlG0rEyYdRdooQMcUSpaA9ohWdOqyWXYSV0t9tQiuPMCIAX7OADgdibvbMeOSwFsHkZxMblzpbGaCQM5v2psEiLjm8DDHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=UsOetLP7dxTNxtlXIH0rX23byBwT7KGCcqrZUCT2geTEH7FAKTHGmdyQhW1tckoZSQb6p9EtRt1YnG_H_J3L52JwtPT_nAPMqCrSVfEN-XTWb-SXIS7tqKrMrfxXXfASxQGMvcrzdUznWXDvxXBhHG_8UxiGBrKXmYK2AH198WDO2ahqrBKH-h_SOzVDTeH7mQOG_lLvH0Xq0rPf9lAA0QrGtqgZ9JR5OA9z20NeoXAbjw1V4B9-DD-loFkFro7m3n8MARSDDF2oif0ehyHHwL61V4yIylNTsvi_zfxivmrvB-EwclyCXieev3cRowUmpNF_wtzKYBXdWprRfzw4nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=UsOetLP7dxTNxtlXIH0rX23byBwT7KGCcqrZUCT2geTEH7FAKTHGmdyQhW1tckoZSQb6p9EtRt1YnG_H_J3L52JwtPT_nAPMqCrSVfEN-XTWb-SXIS7tqKrMrfxXXfASxQGMvcrzdUznWXDvxXBhHG_8UxiGBrKXmYK2AH198WDO2ahqrBKH-h_SOzVDTeH7mQOG_lLvH0Xq0rPf9lAA0QrGtqgZ9JR5OA9z20NeoXAbjw1V4B9-DD-loFkFro7m3n8MARSDDF2oif0ehyHHwL61V4yIylNTsvi_zfxivmrvB-EwclyCXieev3cRowUmpNF_wtzKYBXdWprRfzw4nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=elLCgO3-m8wjQ59Vu8zftlLKtW4Rqf1FuXfQZxIWNhjPwTKSanWQDIq7Ifto0rojFUs5tH1CDgYn6u8yhstO7tcCcO6Xu6P1CyqfNiyq9wBcrw_sftuJLlH9ffLxo5ZRMX4jX_P5eJgj1onVUP2ckD1fMSWrKKOKmDFiR8qzkAZM17szMySnSPFA8CCxBHR0jBRFPAVstJYkVJfQbH6xcugZfcYj5VBN469VHHh_6j5mvmVLfbHLSVrcIKb_fKcduKJ0zt-QMExYfQZLfFHDh-v5zgbSBf12x4d4AUmNMGHRvDGMMt6wt_9XGk7gQcMXy4x92IGzhH4yLt4B2JXPAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=elLCgO3-m8wjQ59Vu8zftlLKtW4Rqf1FuXfQZxIWNhjPwTKSanWQDIq7Ifto0rojFUs5tH1CDgYn6u8yhstO7tcCcO6Xu6P1CyqfNiyq9wBcrw_sftuJLlH9ffLxo5ZRMX4jX_P5eJgj1onVUP2ckD1fMSWrKKOKmDFiR8qzkAZM17szMySnSPFA8CCxBHR0jBRFPAVstJYkVJfQbH6xcugZfcYj5VBN469VHHh_6j5mvmVLfbHLSVrcIKb_fKcduKJ0zt-QMExYfQZLfFHDh-v5zgbSBf12x4d4AUmNMGHRvDGMMt6wt_9XGk7gQcMXy4x92IGzhH4yLt4B2JXPAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PdmQTZ43gclGh2qeOt1259BM8fr_GIuSzBOLaQgvO-kIkv_bWnw7lRuyb1MVbnyNAtbv57ULpxjQaGsmxXsIebsc57LQnlP-QrCya0sbHdkjiZ_PN-GizuSX2SM0Gqm8Za8rBStAL0in1jA2a_iODYf9oeZHPJ50U_d_16K03_fCWqxB_ha696RIm09Cv5JNOzY2zyDg16UcxdKBZhtZU2miGn-_TQatrjiBn5zDwkpQaWNYfij22aRZbfUGfDAIXgICYKly63apYp5KBeKbA3elRIHux7QTCVH0yTtkByzLkd_YrnF-5rviStHKYCbaN9lkO2PGP0VGzVGMZF95-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=PdmQTZ43gclGh2qeOt1259BM8fr_GIuSzBOLaQgvO-kIkv_bWnw7lRuyb1MVbnyNAtbv57ULpxjQaGsmxXsIebsc57LQnlP-QrCya0sbHdkjiZ_PN-GizuSX2SM0Gqm8Za8rBStAL0in1jA2a_iODYf9oeZHPJ50U_d_16K03_fCWqxB_ha696RIm09Cv5JNOzY2zyDg16UcxdKBZhtZU2miGn-_TQatrjiBn5zDwkpQaWNYfij22aRZbfUGfDAIXgICYKly63apYp5KBeKbA3elRIHux7QTCVH0yTtkByzLkd_YrnF-5rviStHKYCbaN9lkO2PGP0VGzVGMZF95-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=qkerrEzAYaqLINPysM_pyPBAjjCnNgySwjezaSMwD4jG6RZsLDu6UWh_ml43WYmpsW-6KwRZi_9cbyrmqNVDn_w2zcpfEQ4_G18POXhgXc_AwkKIio2jy68JAVtvAs9thqeD8t9mt9GoxBn2pQq_nQUsYMmQhlxPdOd4VB_PsNbwk18XU4YiagxKJNRs-yJ0AR-uf4OeTvgbYs0_KSHaPxjxYUgD7GbuizBj5yk6GVGFiWnb99L1t2bjzYf1N7wt7zU1_z2Ucm66KW0Kxm4EarR7-qHXfUEfqduPzeB0R4xlsj93LAcOjar70GPmBS88w0LkujNlssqPB7EYVmdzgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=qkerrEzAYaqLINPysM_pyPBAjjCnNgySwjezaSMwD4jG6RZsLDu6UWh_ml43WYmpsW-6KwRZi_9cbyrmqNVDn_w2zcpfEQ4_G18POXhgXc_AwkKIio2jy68JAVtvAs9thqeD8t9mt9GoxBn2pQq_nQUsYMmQhlxPdOd4VB_PsNbwk18XU4YiagxKJNRs-yJ0AR-uf4OeTvgbYs0_KSHaPxjxYUgD7GbuizBj5yk6GVGFiWnb99L1t2bjzYf1N7wt7zU1_z2Ucm66KW0Kxm4EarR7-qHXfUEfqduPzeB0R4xlsj93LAcOjar70GPmBS88w0LkujNlssqPB7EYVmdzgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=C2AniM4svylquyKtDRB2Ttb9Y8JotZbnULjZM3TfNv9BORZlPBwBko110CaDzUg76wLQf44yc70R3JZV5H3sdDOZSQ3LpNDp2r04voK8hKO3iZIoSncpfYr4N9xCy2sgQUNGsKsNAl-eJCMzTK5ZZDdecN2dkeQbXG1kQVPrkyaXTgfw3t5cicXFgubOdEsg9ooDI818UWwE75hCIhW-vl5uxBczuNe5rnv3cLuSAhmm35ZOSgZyE2cvna8y3Bz0JrX_GTFzFgPsAfp3o_9t3iireMt-9HqczK0Jg93D54FI2Hk3SzxGOtm_QDoNKermhNzeCBbgbuCOJYR8xbuqlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=C2AniM4svylquyKtDRB2Ttb9Y8JotZbnULjZM3TfNv9BORZlPBwBko110CaDzUg76wLQf44yc70R3JZV5H3sdDOZSQ3LpNDp2r04voK8hKO3iZIoSncpfYr4N9xCy2sgQUNGsKsNAl-eJCMzTK5ZZDdecN2dkeQbXG1kQVPrkyaXTgfw3t5cicXFgubOdEsg9ooDI818UWwE75hCIhW-vl5uxBczuNe5rnv3cLuSAhmm35ZOSgZyE2cvna8y3Bz0JrX_GTFzFgPsAfp3o_9t3iireMt-9HqczK0Jg93D54FI2Hk3SzxGOtm_QDoNKermhNzeCBbgbuCOJYR8xbuqlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=tstjI8T8pcjHy9tEUznzf-jbTSRuamQNGMu33V6AA4ABnfrZ68_cF7zjBitW7pbLBhl3880ag0cyARJhsCbpr2wPglme07aPJXEaOiEVQH1MDBbHg780584lEezo8VHFGfHwwJKeO9x646D7ln7WuiyrssBfgVCIbClaeFraJ5LUk_IWJiXBnElx_E5VdN0oF6NVOQz2iup-BHI-dthYOAhN6RlT0tgCUkj3QWwLm3i_j8msFu8AZ3adWxk-xnmC2j-PdAKZ9kKClUo-NDdu2Q9wxAFf3iSlQ4RkL3y4aSGRWvnaH3v2AesJfMm90Gdn6pxawUHOPEY3K8slkTDUgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=tstjI8T8pcjHy9tEUznzf-jbTSRuamQNGMu33V6AA4ABnfrZ68_cF7zjBitW7pbLBhl3880ag0cyARJhsCbpr2wPglme07aPJXEaOiEVQH1MDBbHg780584lEezo8VHFGfHwwJKeO9x646D7ln7WuiyrssBfgVCIbClaeFraJ5LUk_IWJiXBnElx_E5VdN0oF6NVOQz2iup-BHI-dthYOAhN6RlT0tgCUkj3QWwLm3i_j8msFu8AZ3adWxk-xnmC2j-PdAKZ9kKClUo-NDdu2Q9wxAFf3iSlQ4RkL3y4aSGRWvnaH3v2AesJfMm90Gdn6pxawUHOPEY3K8slkTDUgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccZ5G_9TIpVo-MEqFdZ8Zo3WbDvOWhltmgY_kGp8RUTywW5d1Uww-VQdJ2sSfAjWgSYSpkgEdyo6sCU9Qd2JsUJlsXkiyYbjKQTguZfIrA0Ch2RbPRbp8T1V7aGQsuCbO6eaG7272SqYeYv5HOJARCjGRnRqamiBRekGM_Ra93riD0jkFLYmGqgQv9H7JkjS3LWP_hCOp_0MvVnJQBkk8rPabRHrwDydVQ5OPOMYziHd7yJJczLpXwgsXsOHlc6QIW84QifHZtkYjeRlyNMT1SWPiaNdWtrszzIgV0cDD0jHG8V31CZ5hwpJa7Kg66S9mjnoO2IeNQ5JXTc3JokFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=gi_5gOtPwdcdK1pZX_SamCnGYxTcNTt25liX98zkm0PoPf7GCQxQD3E_881jmKkx0lwEcYk3DQgUi1lPyzUxt9sal--NVwRHN4AKw2RDoBWuWXZ_6cqMl2yZqvlxPOB9Nd8Rky7nULou2RAgb59QKceKlnTPgRC_nUE9sfvHYnze2XqZ-9NjeMKjGJ0UPitN56fsH91eryyXI5tbAVwLXSunyGA5QFhkbNoHfy5kuTtpz_2Yk_KUezHWqqfriOUR0dKKXwiiJGEUNEr4ZzyvFHV8M2Pw37BYVZkE5lMpBQ5-gPx0jJirkQEOHErpyUC5xx0K60BJL71-UrcxL6-mKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=gi_5gOtPwdcdK1pZX_SamCnGYxTcNTt25liX98zkm0PoPf7GCQxQD3E_881jmKkx0lwEcYk3DQgUi1lPyzUxt9sal--NVwRHN4AKw2RDoBWuWXZ_6cqMl2yZqvlxPOB9Nd8Rky7nULou2RAgb59QKceKlnTPgRC_nUE9sfvHYnze2XqZ-9NjeMKjGJ0UPitN56fsH91eryyXI5tbAVwLXSunyGA5QFhkbNoHfy5kuTtpz_2Yk_KUezHWqqfriOUR0dKKXwiiJGEUNEr4ZzyvFHV8M2Pw37BYVZkE5lMpBQ5-gPx0jJirkQEOHErpyUC5xx0K60BJL71-UrcxL6-mKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=DnTn72NrjoY8d1-S70y_nZE8fn-ls-Dq2V7P4YOtjBSF7bHFEcLuEVBuwRe8U7SMK0D2cRr-VAGiICdpIzZdpg3WnIlO35geJu5FVjpnzy4fPL0geVZ-Sirp0PHA848k6b4yu4oMungNm1On6GlSd2YzgQ9z_ZB46-Ob5zN1d9Ggg5xIgjAYbspp7SrB1VbsyjSerp1U5caZbSPn0CSpcAAhf1NfyZLqe15pYEkZKNtqxWSlhH5D1gRmhLoWdz-zd_bwO2U_oMA1qhLlinPaFUe3PyG4hXjqugp2qm0qS1OT2K6Fjv71oW1xSOiR0zSpd11DF-E7yCU4OukiUY8WKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=DnTn72NrjoY8d1-S70y_nZE8fn-ls-Dq2V7P4YOtjBSF7bHFEcLuEVBuwRe8U7SMK0D2cRr-VAGiICdpIzZdpg3WnIlO35geJu5FVjpnzy4fPL0geVZ-Sirp0PHA848k6b4yu4oMungNm1On6GlSd2YzgQ9z_ZB46-Ob5zN1d9Ggg5xIgjAYbspp7SrB1VbsyjSerp1U5caZbSPn0CSpcAAhf1NfyZLqe15pYEkZKNtqxWSlhH5D1gRmhLoWdz-zd_bwO2U_oMA1qhLlinPaFUe3PyG4hXjqugp2qm0qS1OT2K6Fjv71oW1xSOiR0zSpd11DF-E7yCU4OukiUY8WKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=rdy-3jcFxn-XPtU431gLCnqf64W9OdTrUuXF4B1vni2s6ByQI8W6MxED8EAMPVU2byrMAr0ejVHwTJ47cp2ccPtMDImrEd6CyoImhRRBA7KXX8JPzDcmwk4EVSSZ_z8iIcL9zaERzD-oZIv17R5OC3uIeHBrOLaqlLA1syfdPcwMYIpI1M-HgZpPVZHEk9jqzCYmtpyjFaxnChWGV50Q2GiSALo4VOrI1syBXii7bmerHllqCwROdqx6ipIp_Y1XyFi8SCBW0iS7txE6EH8WaPLVMilWdhxyszRcXW3mjJB-HbI5Di76ZQwwqknSB-HI2uCENbxIl_80m52ALcEPUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=rdy-3jcFxn-XPtU431gLCnqf64W9OdTrUuXF4B1vni2s6ByQI8W6MxED8EAMPVU2byrMAr0ejVHwTJ47cp2ccPtMDImrEd6CyoImhRRBA7KXX8JPzDcmwk4EVSSZ_z8iIcL9zaERzD-oZIv17R5OC3uIeHBrOLaqlLA1syfdPcwMYIpI1M-HgZpPVZHEk9jqzCYmtpyjFaxnChWGV50Q2GiSALo4VOrI1syBXii7bmerHllqCwROdqx6ipIp_Y1XyFi8SCBW0iS7txE6EH8WaPLVMilWdhxyszRcXW3mjJB-HbI5Di76ZQwwqknSB-HI2uCENbxIl_80m52ALcEPUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Mj_NcZobNPjTSQmCVS5LauvIOypl8x6sZkwFUbnDKiSCwVPtMglBYzQ24jDyxcKNQ69xs4nCy0ezIYMfEsU08ydBk0CVlu9W24887ClrO4gQeJClXCqMPumz0yZfbIaTotvlo9iyJvvAj_x4DIe27YXGO-6YtppoShL2U6fHWKtJSji2t2oWZyTW-PiTlNhrYZWZytpqswuNc-AcDvhEORtrKN31-yEwFNzDzCZNTWENR1bSGtMTq2Lyxs_tOKi7M82BoE6JxeookkMfB6GKiSg13nRjbnF5cCIBrdwpJcgt6aqQq9Xj_iFoPsztzYi0ee8YPn9f7oM-SZXdRbz8cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Mj_NcZobNPjTSQmCVS5LauvIOypl8x6sZkwFUbnDKiSCwVPtMglBYzQ24jDyxcKNQ69xs4nCy0ezIYMfEsU08ydBk0CVlu9W24887ClrO4gQeJClXCqMPumz0yZfbIaTotvlo9iyJvvAj_x4DIe27YXGO-6YtppoShL2U6fHWKtJSji2t2oWZyTW-PiTlNhrYZWZytpqswuNc-AcDvhEORtrKN31-yEwFNzDzCZNTWENR1bSGtMTq2Lyxs_tOKi7M82BoE6JxeookkMfB6GKiSg13nRjbnF5cCIBrdwpJcgt6aqQq9Xj_iFoPsztzYi0ee8YPn9f7oM-SZXdRbz8cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DabjiUrd-07Bnt_hPwqOdZelq2_p_5AgiFlX6oGlHvmevRaY3pjmOZG37aMa7rDQWzkGlnR6g7W01XUw5uhS_yeYoragl4espiEB6O-17ms4zZmGPgLNULBQ_bTSm3QIHyok1w8f7eynUIdU57jqBuOaTYmIHt9OvifVmqPraDeJYUO5XBVYN_mq-P5MA3s7KOiuAzm0o8wiX_0U24vi56zRrw0zFNPqwAQwH_T0qxZnCfkW_BURwOfFgx2pOPVo_X9-qJtKGyhNRqNWvswvqAtOyKjXFS_UfwenabBZXK7PHiyI3xLUdXnKTRdTYwyeslp1XHdnFJ52SCPS8LU27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HcHXkvq1P5FeCjjgi7ym-B--vQ61M4HtRCUQty2dGvc1VYk_pXbU5xiOeiiKbTqyJi6I03aTg4UoZ1nVijh6jZbNAuH-u3MmNf24KYgckS9Pb_PrTpXP7Xs_KMo0jGJRdArk-TUUVDEyCP8ninEGm7v_BygdPLM-X9pc87nlibC8JWn5KB_4FH2S3d9-zeMt10Y0xDjn-YbWmnO9iZ3qEPosKlgJfB9cfeYlwzzaLuo3HaD6sBmIJpwWeojMN0DqzmX9-qBcU_kUo6E80mAZVd7tHH9Q1Kvzk10UMLmhADJQ6ioZKsCT-e8viNFQOP8M0ufGmzDMvAbmAnMyzVTDDIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=HcHXkvq1P5FeCjjgi7ym-B--vQ61M4HtRCUQty2dGvc1VYk_pXbU5xiOeiiKbTqyJi6I03aTg4UoZ1nVijh6jZbNAuH-u3MmNf24KYgckS9Pb_PrTpXP7Xs_KMo0jGJRdArk-TUUVDEyCP8ninEGm7v_BygdPLM-X9pc87nlibC8JWn5KB_4FH2S3d9-zeMt10Y0xDjn-YbWmnO9iZ3qEPosKlgJfB9cfeYlwzzaLuo3HaD6sBmIJpwWeojMN0DqzmX9-qBcU_kUo6E80mAZVd7tHH9Q1Kvzk10UMLmhADJQ6ioZKsCT-e8viNFQOP8M0ufGmzDMvAbmAnMyzVTDDIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=n-cadRlFaPE9RqLQeqq5Vhqja92IwprgLew9nqoPHwakKQc06hwR8xRt7mCJexSA5kLY0kQDI1iSwahjpB9NICrRJoUWsUJi7KdKBCkE9Z7VULC37WqXDrqDU8HaFdr-ApTn5QaB0qRhj-sxrGzlScADEqDcRYzS2LjOeRV8FRPYD8Cj-OHZ4W0t5wEUw2AQx2rNB3bBaVmyqrS_KbguWXg5cRnYYPvaYEZRJuQw5oWaN42kObMmCPOrliauThNsHUHDUoUjEiHnaYdI7CCYePua0s16hcQOIvx7ntG4dcS71eq6oD7UFrFNkU6-LSv_zwUTNDRatIOku869IGx_-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=n-cadRlFaPE9RqLQeqq5Vhqja92IwprgLew9nqoPHwakKQc06hwR8xRt7mCJexSA5kLY0kQDI1iSwahjpB9NICrRJoUWsUJi7KdKBCkE9Z7VULC37WqXDrqDU8HaFdr-ApTn5QaB0qRhj-sxrGzlScADEqDcRYzS2LjOeRV8FRPYD8Cj-OHZ4W0t5wEUw2AQx2rNB3bBaVmyqrS_KbguWXg5cRnYYPvaYEZRJuQw5oWaN42kObMmCPOrliauThNsHUHDUoUjEiHnaYdI7CCYePua0s16hcQOIvx7ntG4dcS71eq6oD7UFrFNkU6-LSv_zwUTNDRatIOku869IGx_-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l896RI5emiyLmVOfnb_kHjAkbYoCCbw0-gYJYNCdn6vc3OkMzb98SIhYGoBkWE6ztdLt8bU09kMZpCPMEUDIBE8Enoi-pxvPTiJ3h7XYJfYjPFB5DVVOXBtt2We0hkBgQvUyE3tRaWmI1eSbpIuSqQtMP3t0dKmm5Y9QFUvvqiZ3s7ySS7SWRenqq0eOaoaJcjN5YlZEpTGUOB7M0bryp_BVy0TPNzyEmFUfywLj-HBI8lmMyB31ouHHtV8i6nphvtf14uXEmtkmgDMx4I7X3K2CSKstm_DP0ahbSX736Ayiie9eZPfX4IzeQxnXa4MYWFcO358bm9fsEBD6j6WmGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JjLvhVRvQZkwePuPg-OKO0mQqX8BlxPoVoUQt-j60hVUC4tWl9E92pvHnv4U9UPMnN6dlFHXlGgCahmtsRTxUO5MW6WMzSgACViBSbyWBoRKoNN_0sUzfLF00871Rd971cJpnpN5Ut2PpiyCSkfGfue9ldku1qlOgqTqpF-PXlpePL-yzTLj6P6SkGM5pnGC8gmLZhGLpdUFFhh7MPB3QX16avnkmuYQD8DZoNJuhgmoUqfYKqn14PbKZNzc6Ld5Wk6aBK7qBg1b4cPvdioy_yFoccQxoc1O1R7EX2Q84Fbs41l8kAQyx_hbK3zjN1c6Y82Fu183xAciKJt-kmh0nw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dt47Bl-3rv8xG--t1GeoSa1rovzD5Z45GCtGt9E_904iBWnrbt70SuxRhBJDgah2-uJH4B7xM7aCVQsbawVcn6ntu0mUqV7VR0q7uHUZ1h0aRmwVs-9QgAyXyBLiztT7oHtxiB04rT9o-BsNvHgjbwSEARKjPka5O3ulalaKNMbX8SQFphgWpwkYL9PilvMcXyh_MIKJfdek9cnVlVFIS9tYTGqCZlC-anIl5GzzIgVmHWwsKOIk-TBKaE3lgYjmKftzKP8OUG2d7G1THkMvyazoeCpvWQjbR68lFKwsbk8-rvmHFH493UFFFRVffSsTXku0bYXWB6yjCuokkxsO9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dt47Bl-3rv8xG--t1GeoSa1rovzD5Z45GCtGt9E_904iBWnrbt70SuxRhBJDgah2-uJH4B7xM7aCVQsbawVcn6ntu0mUqV7VR0q7uHUZ1h0aRmwVs-9QgAyXyBLiztT7oHtxiB04rT9o-BsNvHgjbwSEARKjPka5O3ulalaKNMbX8SQFphgWpwkYL9PilvMcXyh_MIKJfdek9cnVlVFIS9tYTGqCZlC-anIl5GzzIgVmHWwsKOIk-TBKaE3lgYjmKftzKP8OUG2d7G1THkMvyazoeCpvWQjbR68lFKwsbk8-rvmHFH493UFFFRVffSsTXku0bYXWB6yjCuokkxsO9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j-rIihv9hyCU8iIohqwYljfCJELIbGuCG7EQV6WN7x6ajYfmWUbLBSZaiNsqtV4svCfbz6JcbI-AxaGB7SG-2is_3p2V1rB4187YBvALx4MspBj-UcJBexsGd56bu3_AAZi99nviWzfSP9okd_SArNHKqD3McawYIuGhPaUzttTfxshxf1wUpldTqJEfro_gU39ndW8wEj3hlf_lFB9x1DQpD2FxrvDFDHcrdF8w6M7m6RlQPpUfJM2Dk5XivJsp2dZDYx3JRiH0XEGqUtSoY1Z6DuuUVNPnKXEGPk69eszxaRxdJY2MDhvDa3Dcf50ky4_-E8wkLphFFh8MK_QFTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWH-DkB0OsvIJa1s3BpQBouolsv5VMmy7h-VdQvzzwjuWNTv58iaVlkfc2Kb812q3HM6-1MaZqno5GMTff8NznmyTgDYmPo6pCdVaglTGjdJW27WCQhNCUXtHRBPg6YxYLwtPIhFgHKnGzXfa8mhJSRYDzXdPFrS63jW1F1UyqpipvM2Zm77aSBvV_TB6b6mA3QMGLOgZWIawpz1siKeaEZkTVjCzFTehlfGOB-hAxIYwAHhoBXPcB1-eQi3jHF3TO8UksMmRgPSpBW4hegb0KPS2lNyCpY6pytU58zDswwcSocn_Hogf9hG1bsCR2a1iZetkB3U5XK82vwnj0RlGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJcnHVLnB9z0YM5933HU_j84oOU6SvXHm85Gh3ht18sGtsLTU9F4FI-MteICjb0OmmI7bLOLCeqddx8KsHfhQsM8vp6kduZtNmuua3n3CwgNM_0BDrR92Jo_aMbXwcHDCQVYfpjdAk1fXJ8gsL4YS_XszGSyxbK08wir75b5PAbMPz51Ugw29SYIN5l5ck9xAuvp9KdpkIPeOcKns1N6k9hZc8drBhSNg_RX4-Gf1rvPTjLCgdJ1pA36wQozbnf4dLAsqIjAolNnlvL5pfsk36mtGbZRVSfpZVnxdNYzUFtpHb57z1pVIADWmQbCJ1cT_0FiKBFsrdh2OtssGMggPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=XdDS2e5RaeoA9C27AslpfltXvcec90ekoJrPIbiRabJTIOci00RijtPGvUMAuSo1vZOPqbxExTYC23WLDC8TPKqj3CzlfjaY5rYfsVkgG9HmorOSJgTxBSXIPpWLs1F6R8u4L1FsWzA0LYbvjhuUXylLf1k-T1FQdd_5r54m_4LRJhYFlOUkEvoTYp6FwIfyrzrimEabfZnH48kDgFdgk-_8197PFrNYs14_dVY2SzdEDVoo52wXL4EEbk1faIh971XzZqkjTpHRA6glVCZD7j89wAmCFp7vcfD18TppxQF47mVBQcDZO1d8SOOWyrLOZX3CJmFOy3F40JcmpUCISA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=XdDS2e5RaeoA9C27AslpfltXvcec90ekoJrPIbiRabJTIOci00RijtPGvUMAuSo1vZOPqbxExTYC23WLDC8TPKqj3CzlfjaY5rYfsVkgG9HmorOSJgTxBSXIPpWLs1F6R8u4L1FsWzA0LYbvjhuUXylLf1k-T1FQdd_5r54m_4LRJhYFlOUkEvoTYp6FwIfyrzrimEabfZnH48kDgFdgk-_8197PFrNYs14_dVY2SzdEDVoo52wXL4EEbk1faIh971XzZqkjTpHRA6glVCZD7j89wAmCFp7vcfD18TppxQF47mVBQcDZO1d8SOOWyrLOZX3CJmFOy3F40JcmpUCISA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=heiOn0IvtUYALyyD2j-x4ymmVSyIlEEJ7LrUcKUK5iL7LWcBI5p7SDV6KkylQFdidmAazDTzOPeT5UioqwyaJAEoiJcnnJqqYSAa5vj9OVcDFvCQVAGOYGRI5FDwDkPWIPnKrJn6-5tSys_g7FDTEuIJ0Gb2OFpNQC2YKxVmz7Ee9GUhEO5Wqe9irmI8g02lWSk3zkXTagGkFeubc-jwekbog65feQxrSDYYbp_L3-LIKDWADgFzEkdb2X0Lc-dKyzgLmW7SIQs0I3Gu9NCWbpZY0MFFiAgdT9uM4fh6CTzPED2BeE275vUb82Jw8vecSeYWXM8Vkap1oYK-fpqc1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=heiOn0IvtUYALyyD2j-x4ymmVSyIlEEJ7LrUcKUK5iL7LWcBI5p7SDV6KkylQFdidmAazDTzOPeT5UioqwyaJAEoiJcnnJqqYSAa5vj9OVcDFvCQVAGOYGRI5FDwDkPWIPnKrJn6-5tSys_g7FDTEuIJ0Gb2OFpNQC2YKxVmz7Ee9GUhEO5Wqe9irmI8g02lWSk3zkXTagGkFeubc-jwekbog65feQxrSDYYbp_L3-LIKDWADgFzEkdb2X0Lc-dKyzgLmW7SIQs0I3Gu9NCWbpZY0MFFiAgdT9uM4fh6CTzPED2BeE275vUb82Jw8vecSeYWXM8Vkap1oYK-fpqc1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=FAzcljoFP1jWr9Z6OZ1rlDY0FX6S6_eZ5iDXRsZIh9L8GnXsM8buxTti-QFK0u0lFYpSIQ5wyZRGx5_5-EwBm9dqz1GgHkGJqqKUf7Xe5VuE-eG0d5pSq9PR0_IJQrvK3jWJoxokNOuNvL8lCrCjRk33AZ2xWlEh5nVD9B3A-VxBdg7J4pbwVJrSSI-HLnznTsEbtTANrxEFo3wjWx3nG09smbiY3JtFelG_0B8HnydxiEYFWRw8gt_sqpDR6uky7JQ2VIFCA0j5AfVZ6fxLrtanG7UPOXq_2DmCUO9G4OIsKEOQxo5oIosFmvqx2tFF52Bdwn2vedqCrFmoo5Uysr1xN68eAU6qAPpy0jVVAgyfd-prGaf-XO-tVb_8xYYu6gnT7Va_YAhPBKkG6d6jaxdkMoS7UmWes6uXX9i5VsalUWG6d1ta2lMTPdg8Ll54yZR5ZupXGzw-58OjOPG0fDscxNFV5O_fLQ9QDB6Haly8EgRwVal9G2PpGPIn9S442pKs3YwY4CDuTzOkKcuS6zRcpFsqAy1vVtC-UJN27bvYO_WYaXtqAQ5_7Yvne_-dY-yZbybLP9kxQIHNNPhgtwJmJ3ZXNYdxGsOrMTNUa5au8z9xkzShxvd0zGHve2-FwGrGoxjCBq3_gesp4wmMgkg099H3U8XYEO1ENNkEiAk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=FAzcljoFP1jWr9Z6OZ1rlDY0FX6S6_eZ5iDXRsZIh9L8GnXsM8buxTti-QFK0u0lFYpSIQ5wyZRGx5_5-EwBm9dqz1GgHkGJqqKUf7Xe5VuE-eG0d5pSq9PR0_IJQrvK3jWJoxokNOuNvL8lCrCjRk33AZ2xWlEh5nVD9B3A-VxBdg7J4pbwVJrSSI-HLnznTsEbtTANrxEFo3wjWx3nG09smbiY3JtFelG_0B8HnydxiEYFWRw8gt_sqpDR6uky7JQ2VIFCA0j5AfVZ6fxLrtanG7UPOXq_2DmCUO9G4OIsKEOQxo5oIosFmvqx2tFF52Bdwn2vedqCrFmoo5Uysr1xN68eAU6qAPpy0jVVAgyfd-prGaf-XO-tVb_8xYYu6gnT7Va_YAhPBKkG6d6jaxdkMoS7UmWes6uXX9i5VsalUWG6d1ta2lMTPdg8Ll54yZR5ZupXGzw-58OjOPG0fDscxNFV5O_fLQ9QDB6Haly8EgRwVal9G2PpGPIn9S442pKs3YwY4CDuTzOkKcuS6zRcpFsqAy1vVtC-UJN27bvYO_WYaXtqAQ5_7Yvne_-dY-yZbybLP9kxQIHNNPhgtwJmJ3ZXNYdxGsOrMTNUa5au8z9xkzShxvd0zGHve2-FwGrGoxjCBq3_gesp4wmMgkg099H3U8XYEO1ENNkEiAk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Qquykw77HkM-iAFOkIhRbgOFu_pV4EsqW0B4D75WhkQGDe6tTqwgiAT5oyzWpB-Z7kdMM3XRRpvfwt92ZefNcwqrquX5VyyakEeT8mG8NzRHujjVIPSI1rM8xoICffX9xvOnxAGKmGSFjpIZGdlv5sP-cv0Zks0MQJMK8iOE9KoZ0qpKv_8M6K36tmriGQFxFoYuyVMSXUNJnFV9IE7jM9nSBzVSjHK9yrFYS3RDOJ6w69Mmh9lC_wpZ_e5z95GQ3uG5i2BBF-ehxpsxKX-RH0y-oNTwgaN6-Rka-RK_fogUjnhlSk2ZwOgORFqdzhueUBmYIRkuF15sB7t79hyImHRUo1cyUOu_ClCuNYD0uZAxoaxk4TEq2FjzjFk-CehNth8pGMUo4Cklmpn7JoyKLfWkqh24-MjH8YicMPKNYr2UHITELc853u3suN_thPQ-4JO2jymE8yhMibnQhJeFNRdwaXi-N5B9brb6zfHi_I1APyJqnkb6bAGDFFHH71ahKmD9i3s6lHKwWYpgO03jJjazoEIEIi8b8yiLwOUrNe7YznVCRJVi2xtXt2aZuK2QADE41_cZE7EXETaG2vp3lczaRW5qaHeEIobp8jQLzj_7fdnOm13YLQAivYGYW9y7rMzcHTxA0_ZsruYLkuN2dD1aXG4P5a2nbil7DU8NthM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Qquykw77HkM-iAFOkIhRbgOFu_pV4EsqW0B4D75WhkQGDe6tTqwgiAT5oyzWpB-Z7kdMM3XRRpvfwt92ZefNcwqrquX5VyyakEeT8mG8NzRHujjVIPSI1rM8xoICffX9xvOnxAGKmGSFjpIZGdlv5sP-cv0Zks0MQJMK8iOE9KoZ0qpKv_8M6K36tmriGQFxFoYuyVMSXUNJnFV9IE7jM9nSBzVSjHK9yrFYS3RDOJ6w69Mmh9lC_wpZ_e5z95GQ3uG5i2BBF-ehxpsxKX-RH0y-oNTwgaN6-Rka-RK_fogUjnhlSk2ZwOgORFqdzhueUBmYIRkuF15sB7t79hyImHRUo1cyUOu_ClCuNYD0uZAxoaxk4TEq2FjzjFk-CehNth8pGMUo4Cklmpn7JoyKLfWkqh24-MjH8YicMPKNYr2UHITELc853u3suN_thPQ-4JO2jymE8yhMibnQhJeFNRdwaXi-N5B9brb6zfHi_I1APyJqnkb6bAGDFFHH71ahKmD9i3s6lHKwWYpgO03jJjazoEIEIi8b8yiLwOUrNe7YznVCRJVi2xtXt2aZuK2QADE41_cZE7EXETaG2vp3lczaRW5qaHeEIobp8jQLzj_7fdnOm13YLQAivYGYW9y7rMzcHTxA0_ZsruYLkuN2dD1aXG4P5a2nbil7DU8NthM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=WYR5qZT0f6njEv-zI2DRm2fcGCGgj92xYw6mEjf0wSTMHUqcVXtJcv_xp55AwmFZ3Cfoq6X66vYkhMoYrFLKiNiUoJI5cQ1w3zE2_ESv99a4PPOgvGgN7wgmasTZSypQNLuLn1jgo7EmOEoW3StbOwCKACRPXLreswqXn3i0p4Vr3xkcNtlmGnBmZDwQgVdSsmVqklQmf6HxZ4ujNow1UpMHjYVSF0NdH7OQeWSlkfauZlVAKnZsXNnyOHzzqUg6VfzX-wYqiPf4AmrAtgzUKoMqMru3cHCSIGP5cWRbDIpGwfnOqNNLpUOkNmi6MpdKhnIUvdeOXI5KL_XTe07WSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=WYR5qZT0f6njEv-zI2DRm2fcGCGgj92xYw6mEjf0wSTMHUqcVXtJcv_xp55AwmFZ3Cfoq6X66vYkhMoYrFLKiNiUoJI5cQ1w3zE2_ESv99a4PPOgvGgN7wgmasTZSypQNLuLn1jgo7EmOEoW3StbOwCKACRPXLreswqXn3i0p4Vr3xkcNtlmGnBmZDwQgVdSsmVqklQmf6HxZ4ujNow1UpMHjYVSF0NdH7OQeWSlkfauZlVAKnZsXNnyOHzzqUg6VfzX-wYqiPf4AmrAtgzUKoMqMru3cHCSIGP5cWRbDIpGwfnOqNNLpUOkNmi6MpdKhnIUvdeOXI5KL_XTe07WSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbwCiipooZtVp6cZxZwVG8ROE1uy3AGdjvDpx5Z-QPd-IDZ0n5kyg99LWx2REhBKr6W3cGQhYxnaTEmlm58wwzKy6gX8oB7hKUoNbAzqoZSALz3sHimOW3ApFLo-MrCtqTNVu0JIqym4xZQHDCigzaswzlWHcb2eX9dPTMBYLqssdc-xZZUfSeRGVnB_-or2qnYUISH03BWNTzYsEE0MptPl3nOGvhe7SMuxIjTObygPeO3HZKEGdxi4rHO0UBUvFUO7C3_uUFKVHzqOKPI4kGU2UilBSRzB5FLkDqZij-FaXCBQLcFccnk3lqDvCk6OhVmpd1eEh0e5F6jWvY3ZDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=n_c0sH11ELR8JBgzCpOYXLyI7F1Sl8hddoq8D6ss93q3yaQUJNGppPGc78FT-AcE8EV0cK9xfjkN_veArolzuUoZE5-_oJz6t9ZOdSbw9mvgexR_FbQD4oY3L3xqOi-8D7IszzuHfPscF-sa09GmNhBf6xu4__jvYFFiqs2kK_d24Rp4eAWUGfPsK95h9Q15Fc89Y4EhLKvwR8i3E-GcF0WTNi3NGEyBAKTjTUO4bOICBR-25LCftCIuNke5BhoWH5lZOIMaspPcaYO1z_ihL1XpaHQfqoLX44XkOU4DTsqJEx9_PIOk9bogBpX6TTrw06k33vjbAl5tW9ilQVP5gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=n_c0sH11ELR8JBgzCpOYXLyI7F1Sl8hddoq8D6ss93q3yaQUJNGppPGc78FT-AcE8EV0cK9xfjkN_veArolzuUoZE5-_oJz6t9ZOdSbw9mvgexR_FbQD4oY3L3xqOi-8D7IszzuHfPscF-sa09GmNhBf6xu4__jvYFFiqs2kK_d24Rp4eAWUGfPsK95h9Q15Fc89Y4EhLKvwR8i3E-GcF0WTNi3NGEyBAKTjTUO4bOICBR-25LCftCIuNke5BhoWH5lZOIMaspPcaYO1z_ihL1XpaHQfqoLX44XkOU4DTsqJEx9_PIOk9bogBpX6TTrw06k33vjbAl5tW9ilQVP5gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=B20yqSdwPZbpGu0Pyfv5_1GywTGbjqeJSDpM8CEJ8sXCWPjCkoRYp4n1mBoIwQCpbxe8CLoIkza5fMpzfdGBEVYux1iCQtgVPh_2eFWj2GDbnh4op1cuWNzr-M2lVAAb3rghP15sIENjoSdCXXhV7s2VLqsY-K45Yuzy66ERniKwdNEPnjSXsEZmbOVgk1STELoh9jEOhIitacgtH7Ze7EI6IU9cBM0ZRaN_k42roi-sQo6YjKyZ4rb-B3XMsP9Mgzcw59virIxo23__emrvWqv34FDq3YNET7b3rr4ZZM7k8RcjDT1G0iHk07nPKlVPceZl25SPC26W-wnAZb16YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=B20yqSdwPZbpGu0Pyfv5_1GywTGbjqeJSDpM8CEJ8sXCWPjCkoRYp4n1mBoIwQCpbxe8CLoIkza5fMpzfdGBEVYux1iCQtgVPh_2eFWj2GDbnh4op1cuWNzr-M2lVAAb3rghP15sIENjoSdCXXhV7s2VLqsY-K45Yuzy66ERniKwdNEPnjSXsEZmbOVgk1STELoh9jEOhIitacgtH7Ze7EI6IU9cBM0ZRaN_k42roi-sQo6YjKyZ4rb-B3XMsP9Mgzcw59virIxo23__emrvWqv34FDq3YNET7b3rr4ZZM7k8RcjDT1G0iHk07nPKlVPceZl25SPC26W-wnAZb16YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyiPMSrKCyiEQPJ5m-wm25HiCCh46h2bcPbxhskvWT_xzH6SsRxPHcj22h8PrjbeikohfuZ8sUK-d7zrzcH8lT8nSr-XWjxZf4O5Vbpw9ko-Pdj-DToPrI_1pxv_IorC7nv94SkXnn7VJ4ZLpvtWLug4uAhVcjUOrGYwYVUNH1GVEwSmnXKIUisdNTijlvg-iABdeH5b44gZsEeQ1mqO_pxtfLWax7agOO3WrsbNfnU1U3XTRpYb1q6-XwM0zpiPvqpC7oBCT2iTXT4048pyFpxtrQCnuLdGqLFV2N9wAtR72XlEII4urFoSeLL00rJuUVP_PMaKapf3b3sikA1CTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MILmBRDGuEPnE5KROoylPID1mxwHUNctPQ6UAhZuLpZkVURJWAqFuah-__serWPwGnOvDzZSnE_nFP10-wgfxwL8sUHshCihaKQRNtwwfjSbIdq9m6rCvyYE_xAGTG6D1c0OzqWt1Zil4KOvnoQznu0ZqFAS6I4sC3os5Un8BE7Rnxhx45x-lMYUtDJI-pi5eaTp6_BZmH-EXI3beP4Z9tYF1VXTLVs7V6hQ_v9isghR2pQ4tZaqmqFz8I5MRwNwf-8YUL3NSbiOy-7hakjOmhtZ5AHlxlgOVRGc8jyZgIwqooyel68D0-iz_DZXtWaHdo66F2PSYU7hFHmzgmYFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/suc1YfXli9S_tCNilY5nZxoqum3mqWml3BNmp_YRU06_0-eTh6bB66bWaJ6MycxlLlVGpiBqiYkwhJhJ93svSG1gneCQGSIkMXTf26NjFfIvmU-unXvuSvAB70n9FGFXoxdyso6BPQq7ZPj58eZO_5mHpk7kO5TVeb2rlvRqvoR3aSyg2OuHlgGxckx0aGqw83XrzLH4rev-tSeg7j6Z2o9VlQZXQC4rXudUklK3M4oX46eM0BRLTN3UJeSOmCWSOkPxHWg9g5GasWm78YRUOR9gHP3dbW9B69d21GO-Pt6N0tvKzy1cQBTYCkFYEO8m-8TECbZz0sA3BA5CLBx6aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vegB3GPYfQCMduoAjaTbIesTGh8tn-VaWGyBE2SdsGZcWXGf1KErU5xDUT2NY-hQ3RbFIIwvW2EIiNq3qKPPtNYN8SrL61lY58J7NIzQDnlMkvW1I3TUA8ZRuuH7wyqZre2JYinOGIjO11iPfD8epDHFEtQ7i7xwgv7jwFkxe-HsjWSm3dhrdgTalkHZDH8OQQ-Z6MfqQ4GW7tuCgMgH5CXKAjNGvE7khnXiS2nJWBhSB3IS4Rj3yY3V-1hiaOTdOyMNlbAZlCyc47e6pQvUZzReBypVXf9sdjmM5lfHDdoa8A5eBZLESS2cZqi1lbXU_WqNgoQuPm02p6WG23scHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bn8Y1VuygGpR_3XA6MTOJDiVR7JPc0Q2f71SKLRoL_O-AB3bYo4hHFzedkVValZyUxKzMcC_-zPfhEunVdO6oRO2uF-Axju3ZXoFvKC1CSXg65py_XnrzHKM1WkwZp-7u34NeLgrBx86pDWb1Ko0_qY5pTQc3ruJ6vzxPyNAgSN_gUacydT_7BaRneWGzAv-SNjZhKvU7g0xVJGbOaVnWL-Fn3ow71I92Tq8Q8gv8SpECNMaf09fWjmJO-gknTTbO0OHj1Jrq_NiJklM8vSZ9BbwyfD6KKTgB-MbFD8hkEVBJCbEwCRf88Bson_ttlDs2ePjwiVWn9p5STenJnOJ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvN2_4ZB1-DlqYbbr0Ceny9SNw-b78oCJpp56CV8AwvMlSFtILClZCudx7kQoTiyAEXsh3mgE2qjd5is2t1llS9x76nu6l5vN64mchB8ljxJc_8ZXTSv-wi0TaJoFaMEgO7lWABf2wNBQTlFWjQ1d8E_JRuGBhZG67havwaVNDCpGp_uqZRQgdG7bbEjUrs3htMFIXN7p6-uIRs7FSkRaWp-xdyT5Y_cj_gGL_MKs8epg42FEOPF78KlSseXWUsAyMWPZO6khT3seh9WoRGFnD9xMejsLNliiP9Pn-kC90wzNmkfCobzHtbbRAvUf_n-SOZehQfFKnMSkhf9KoT6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP3WCF-dr0KPUJT9Csv5ZfJuNoc1WpYCxRgBj2tcvoNCS3iGEa1ZGt5eaeUTspdsC_XebbeLOQwsnwxK-6TQvy2aP70_aFMcp_arwgRN1uowfHD8Pll34msAqVVwsmLXBy-W9pUSMvEDIUQ0Ty2izAvZ_wt6ZVNSu1ZXqS8b3vvzQVYJLSGHx9zo92gnlHBoMiRlTcRMSPx2TAK6Tp0w-Cu9-dNR8K5Gc5JVQzdEXwza1HFOgY5XquFZcwdcNDn5N1Tn8Q1wkVmvOzLcmb7H68iSv9fa91qTLscMZWln4JVcFjJ843tPiKr2Hyq07gNBQ6-_r9ItUqJVb1ps9OSU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5ps68HO4uFo2jF31YAacRJSOYSTpQeGKZuceGEEEqCp1J0nltVJXcNZojjcs72mHm57h-yFGei6LwV1XOL2f86HW_nYkcXjC0ZY1Ib0iVhqaeochXJMa6UuYvmKXTwZbviGK28IEWD-rKbjNjUb-_bgHm2HUKaRVW6lx1mKXf2-_RPWZl0TJbtdXc3y-uUSsNUyTkxXV8FwLUTzfiI7iDwdqDG1u2ogCnclQAbXx4IaBsnovv8_HZDe_7WtT5ZoSB8PdvnSfxAY-ZgFlQ9LQyw0cA2UtVSBm_gRYki2A2JqzQYEcP-Mt7OgC9AGUv-dT3MPNixchIs-TtDTyPKZ3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mKPQxFTc-8Xwr9FjIScgeftqL0WdxA43rqt6Sm2c5mina05J-HUAC0c0IeFEpQnyLwLjpUvmJ7NYL1E8SXHqYwGPJKk1XNhMK4ox3f2_-fjLQvn_FSyQ5rLLo_7Ozms5gZBUgUjgsGV1DKNYouQHbNeGsoBI6R8xSitkzjn-jYzJ0jfdIn9BxDuWUZCrEV4U7eTriDhroaV2Vkf4Jrqg9bbLYydMOs5CpXlaL0M1MB0_GEUqIikJnaiJHeu0Tsb059rmeclbrPgfonWIEVEyr7yQ7_TVO-pYH80ksxOQJeF5vlYW3euxqUnlO7fSYr2aNBFycUInLaVzAhxjfU-27Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0GGJqOVxyOo-0-dO2_imBpS-asQBKqbpilAtSq7cD2muStncB5YXtYJRSFo5tUnrY2xCr32vvDjwMGobL5SUETl7AvftSvi8hvROi-_tpA3PA7OJvpEpF-8ZrLkQShmTrqJFc7pf1cSeFLRnsmG5p4qgctscbtzD5UJBw9B49zdu_TM2asB6Hju0VMNdIeE4nbrLzv50_DomJoV9iSYn0o9TPu2M2dHCNBNcsMS4EQ1lCA3wC3TPU7dfRASWSLekQ1pPgOacZqqUMicHX55CMbvAYjTzAKeZtyVxVHT--PC3iah9UJ8C8LWNDK69b9Db0iOhcCdELgsaLRH3HgBcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
