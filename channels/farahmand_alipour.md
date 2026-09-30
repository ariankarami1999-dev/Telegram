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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 13:22:45</div>
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
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdmttvCvkjPut4MmtPjCdR6VkrrVjppZZMJGMajbNBT-4TmeKLH09QcInaI0pFOnFPzqKKKIY9WhcLW4isTMkCwYrVn1U00IvwK4ZCNOOahZvkBVbe2II8grqEtohtVAIbA_RJtx96d1_AiCnY9PJC14amv-a-gV_iFIPn3g_su1eXuLgUt5JVpLtK8mDGbBvxBAQR1Eumbzf4VPKw1q-vqPYeyU0rSMT9Lponr_PEQZ1JLFNvqgw0vWmGQSwTjJJqBQ1h4D0etORADB3KfXRUbUEY67VfGKVhnU_cbCTTLWeiZg9osnSsBNe07Wkp0Eun72bRPNti4uL8vjxUQt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RklkcfQFscNLvTRMtxfQDpX7HmsafMqDKZaOfl3bPp-2rEagjGovguMYT_RRgjX923HhxgveBTaPjtkafB54pI0XFnNvILVekEBd6T7bC6_iPFAG0X-N3IQN-8vjtcaMOZ1pC-yUgeodJozJGCxUZE6iq1-Y2sSdqwaliYu1sEXEu2-mFNKQnynOZYujDL5sLol7-JBT9iFUhRFmeHdJ0ROXN1YWLVUD1LjN_zNHWAltrvqyo2OXehiRoYkzguWuOahwbWVYBvrrrQQGoZ4s40BluHBkvrg6vf1-5_LGQ3vwvAS-IyzVdLUEOgAHgxLmv9xBRTxCOUafAetxsjk6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=ma2uJKp6PZcxlrViC-II5dg_ezDlYczUUdxypC-Uh4BnV8pFY08BxZZiXOjiTaYpjPDf7YCnae8qK0xg85DlU4LWdtk0Jgjy0ISfuccKQx69eKUjyah2vvngWk6eJzuI3seroZ9CRGnBVQHqXWOxH0qXhMOKGrF2jphQ-hPGVWAv56Q7xG1UBrTt83phZx0CrXC7uaXjSA88FF7fjClBUfw3-7JmZ78GDPhPTvkMgh0ngPypa-yuHIJX0t2UcB1ym1RXRPPHtw556YPwrniaRbbaG7uEKwQNOgIawQHqGC3LDl7FtQFXzjsURhDMO6wUsvu1Ny7zsS52XbN22-QDRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=ma2uJKp6PZcxlrViC-II5dg_ezDlYczUUdxypC-Uh4BnV8pFY08BxZZiXOjiTaYpjPDf7YCnae8qK0xg85DlU4LWdtk0Jgjy0ISfuccKQx69eKUjyah2vvngWk6eJzuI3seroZ9CRGnBVQHqXWOxH0qXhMOKGrF2jphQ-hPGVWAv56Q7xG1UBrTt83phZx0CrXC7uaXjSA88FF7fjClBUfw3-7JmZ78GDPhPTvkMgh0ngPypa-yuHIJX0t2UcB1ym1RXRPPHtw556YPwrniaRbbaG7uEKwQNOgIawQHqGC3LDl7FtQFXzjsURhDMO6wUsvu1Ny7zsS52XbN22-QDRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAPSocpFObkt1MUgplWWx8XGOM5L8Y8ScDY8IMHswscFwJDgIRBKmbWnGWW7F-Ude7XCLcQr2IcovB8ty61dStubH7Xp-AmxGMZW98l5WydpnQ8vZf-jmuLQpKPpMi-7468ZEFbkISg5JmDESsC0R21xBH5jtZFGHkIhjUZ1uC4jf15gPqOXxKtdYCTphcLPx4oRIeH0VCOzdk4PJxexMEKEELbz6yXRlExNaTg4j9S0UMIZx29Mq0RmDcUrSOS72yTAOu8ej98rq9gLDfKV55-flKj3JcgnxLsvLzNjaxN2j3zuf-PptBGPetGE3kkGC93-McTD2g083clmQ6NDGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=inYnV8pSmbgoBnBe5UgCgCPACLo7URtVlPUBnLN41SxC_yVJzmcUenItn9rsIzGryyKyCDWZfI1XRjqh4BfngyV_DH-zg2ioYIAwF7IH-DEW2UuGkCHtcpnVJb-Enf8Z_8VWHkwI8RWtJUGSkgsy6zpmk5wq_sYZDmIWBoWz2a_Ktfye-R6PyqD9tFPGBYXhQBlrUuVMyz416v1zzyneL5stMmsxSZcCuEkL1dQVNV9GBXwk5srcEB5KvHt5S_PjJmYEtJQN9Xv4KE3uS56o2fIrwhgzWyyl-5H0gRs9CwpaBX_KGCjP3nctKwhkUriPuMbDKZ1P-TsQu7MvgtbLRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=inYnV8pSmbgoBnBe5UgCgCPACLo7URtVlPUBnLN41SxC_yVJzmcUenItn9rsIzGryyKyCDWZfI1XRjqh4BfngyV_DH-zg2ioYIAwF7IH-DEW2UuGkCHtcpnVJb-Enf8Z_8VWHkwI8RWtJUGSkgsy6zpmk5wq_sYZDmIWBoWz2a_Ktfye-R6PyqD9tFPGBYXhQBlrUuVMyz416v1zzyneL5stMmsxSZcCuEkL1dQVNV9GBXwk5srcEB5KvHt5S_PjJmYEtJQN9Xv4KE3uS56o2fIrwhgzWyyl-5H0gRs9CwpaBX_KGCjP3nctKwhkUriPuMbDKZ1P-TsQu7MvgtbLRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRPQv5xDhns-4YvXiy0gr8mJ7MKvVdGzc8IOMEWkaSlQgqXU7aImd1l5XNAWoH2ynQYB4ouWN_p_wOtiPrs2-wCpEnNhDGYHSjYKoTX9j3qWINOzZNJtA9jhxx6sXzsrhzLz7ybjv_ZXgnHQC4ByE_PSLSjfyQyMCBEFC0O-BEotzyFFW2aCeOiB9zJTe2tmii2fk9Bla6ejvjIvYgAYbnb8LA9X4zIp2FsMfKXSnRUS-2q0lr6LqoR_JIaEuec8jIyFC1t6oENLqv_6KdOijultHywpk7OYiNO_kMH78vcMQl7zdyS_8HVZnDKXQg6cdlcolc3s8HX1Xt84O_oWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxC2mpdAok1zvNECl5tm6Jq0U7K9NKoktP7VZKWe21DJIfC_5gciGMu-YpLpOyQC6wLLBBILtvBRF6I9ZmEOY3ChQLkUz3_Ypv601OVy7bxQy_Z3k-I8ejdjOvadaAmT4ipPXfF5RKyZ7ZiVcbDeBf_y0RZxL0juljYwDjgNeQxRTj0ShvejKZ1c0wtp13kMsKNI1VJSxrHMB2Dj5kV-x76WKRIoSqSdhEhKy7Fs89f7MB4_f8yDiSfUrObRUPd6I40h2lEXKyoG7S1hxfIQIVyyrcGVtSpcn4n6_uzwvgtSIqSM8sVV6itMwTO_eo7855onK_e6PE_qyT0bOupysQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMAa19cw3HO0gru0V10RtFSTfd8QzC2tQPzLOHZn0JnU1Zy9o3WehVfMLgh-0aV6DThsgdzJTLjuH9LA0LRDzWxatVn1vPNX0z93Lax8vsJSuGGxAW_a1uB7_Kd7aHa-KP_vxUe1yEoBQWFfs_tPyQFeJKkXm6fFON9J3aZwlkc5EPxsQFnm27TgElIJwb8igVZMaID5pusagGsw423yn4s-IMlu1M2lGl4NwkJc7fhD53qOA3FB9dhZ2YMlUZJ1SGitFbhi-VxSS-87ipMK-ckko4OI_kia4FVaim6cjPRSkHvgc0bVCrFexMksCnwZlX9l3LytTvuSCkDBHQENbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Lp0LNQSt56ZfHx7eh_W2jFJmdYOQCmwF1WzCM8V62vfnqsFY5uc4WMfPsYSB-63t-1zadwmqwb0Wquf_wHk6sr5kOi_PM1O0x1YzyMfQOwQQ59iTaUf1bGgVNk1wSCrB2h_AE-DaGLxt0rD5V9JHk5qOTaUpTOK3FqF8LxwJuG8aaARTrXXhnAP77gaXHucNG_CsPWY3kjUOcXc5HudXPJdsfSbO4BSubr2BYx5RElHtnKyFuMoYVuAhQyoV-g6LFH0hGjIUL7yTCmIk-huHAILsmc0u2nzSOEXmbtAfEgjvT-2b2WQuY702H5Qn7wg4w03J0zYiK6OHuRzAnXZ5QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=Lp0LNQSt56ZfHx7eh_W2jFJmdYOQCmwF1WzCM8V62vfnqsFY5uc4WMfPsYSB-63t-1zadwmqwb0Wquf_wHk6sr5kOi_PM1O0x1YzyMfQOwQQ59iTaUf1bGgVNk1wSCrB2h_AE-DaGLxt0rD5V9JHk5qOTaUpTOK3FqF8LxwJuG8aaARTrXXhnAP77gaXHucNG_CsPWY3kjUOcXc5HudXPJdsfSbO4BSubr2BYx5RElHtnKyFuMoYVuAhQyoV-g6LFH0hGjIUL7yTCmIk-huHAILsmc0u2nzSOEXmbtAfEgjvT-2b2WQuY702H5Qn7wg4w03J0zYiK6OHuRzAnXZ5QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=JWDuM9ysWK0XXdfq-qGiJo4WMbuRu7kSTHkV6Auqyz-0vV-faDe6cUENB7-5K69NTt5vnOBAXIOP3VEropAdQ8I-Kl3dyM5s1E6Iukowe1e-F2r3RTzxShTsDEdmlZd8avn3XUyQmfvdQRYWquZXGFk9GryZxCXqOiamfthiKCKYPDwMI52fAwOUd_2Ss3fAPNR0SncDfbbTNzxZnnsFvf64w3dW9XtlC_346HTlFhClvZeHajhPysxJgyacYvYEexxq2cMRyowBVOkB3QgmreRm9bnVVcBrNx7fj5zGQOQYfj0zgbszXDJ4sCagv0hy6jGT2QvHFMJ8VFqISCHHUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=JWDuM9ysWK0XXdfq-qGiJo4WMbuRu7kSTHkV6Auqyz-0vV-faDe6cUENB7-5K69NTt5vnOBAXIOP3VEropAdQ8I-Kl3dyM5s1E6Iukowe1e-F2r3RTzxShTsDEdmlZd8avn3XUyQmfvdQRYWquZXGFk9GryZxCXqOiamfthiKCKYPDwMI52fAwOUd_2Ss3fAPNR0SncDfbbTNzxZnnsFvf64w3dW9XtlC_346HTlFhClvZeHajhPysxJgyacYvYEexxq2cMRyowBVOkB3QgmreRm9bnVVcBrNx7fj5zGQOQYfj0zgbszXDJ4sCagv0hy6jGT2QvHFMJ8VFqISCHHUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=WFVWH8ZJ6q3jLd6UJGo0VYZG5PiNWJos961TYcBMBj3uA53Z4LQiw6hFneNY0RduQOxKoNiFR1z4NjvMPZIupsNUo1DKKVlUqecCI4_-PT9s8aMLVbj6qoGowR0RkyPAMu2mdnMrgT3BSQ3fU6r_o-iNAznzKNej80ek8nGPpQoLY9HYRAnVhcsn21usyKGN5pDqzOrmMjCtZjE0cIF8lGpFGu5hsB6YqB0vesSJ2DXq65rl9lRg_6caf0S5jpnH4gEEyRZglSXzl4DDf_y0hWFyO00JZSLiUV_nb4JdKUjBOp6hDcjT4qrINip4F8LgWSERx9IiAYZEc4TA4_28Mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=WFVWH8ZJ6q3jLd6UJGo0VYZG5PiNWJos961TYcBMBj3uA53Z4LQiw6hFneNY0RduQOxKoNiFR1z4NjvMPZIupsNUo1DKKVlUqecCI4_-PT9s8aMLVbj6qoGowR0RkyPAMu2mdnMrgT3BSQ3fU6r_o-iNAznzKNej80ek8nGPpQoLY9HYRAnVhcsn21usyKGN5pDqzOrmMjCtZjE0cIF8lGpFGu5hsB6YqB0vesSJ2DXq65rl9lRg_6caf0S5jpnH4gEEyRZglSXzl4DDf_y0hWFyO00JZSLiUV_nb4JdKUjBOp6hDcjT4qrINip4F8LgWSERx9IiAYZEc4TA4_28Mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZjJI1AtQ14wjxYj674DUDmj3CXbJDR8K6JyLFRW3xrIQge337hZPCQLw4ucX6S2-NAzenNDi10PqaPYcHwDj4sYQ89V12sMZpAG0bwyptw82JRnrMqIAjKzMHyAtKSiSyytB_KJ_OgDyBXZcZUDf4PQdKRpaxrjHmFbtaiXME2p7hSv84lKvlYB6WH9LYhO3V9_PI4ObN9-0BICo2HSCBUbJBP5Y2n7rfMe1sBKYCCTua2vBlEg22XpdMrmKnPd8SyGW6pOe9SKb0wrHpO-rCPkU_b2odfn-MLx_6Iao1VFL0w76pGTtSoZSHynmhoF7b7HZwTAZK_n6AHBJzZlsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8AHdQ2GhhuqW0wObz4pJC_Jyh5YaQPexMvd1fCajOgA9qMHxgg48fjBIwcthBvhELKjIwaWV_fncYVDBYuwPW8GtPpQ2LkA47MMiLwuZQjLNq1k5bmvYxRIvQKoI40YP0TBQ5gq3CCQgEU89Jw5XSIF3HnQw6Npu547TaadeI0goItDMepXVxudmXCtAy7h0FmzhltINQPQ-mgtv6mVVNvKVvmuJHNl-QCwOyYa3XZxLlQDWaByQMiRexEPqdjRxMaj3hFID3dGZmLdmBpRXNDk1yO1-GlyM7-CojJQBEEc2H4HpuKI4jph2lgrpnF9W3P4nthOiB6o2davOEYFJ1VE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8AHdQ2GhhuqW0wObz4pJC_Jyh5YaQPexMvd1fCajOgA9qMHxgg48fjBIwcthBvhELKjIwaWV_fncYVDBYuwPW8GtPpQ2LkA47MMiLwuZQjLNq1k5bmvYxRIvQKoI40YP0TBQ5gq3CCQgEU89Jw5XSIF3HnQw6Npu547TaadeI0goItDMepXVxudmXCtAy7h0FmzhltINQPQ-mgtv6mVVNvKVvmuJHNl-QCwOyYa3XZxLlQDWaByQMiRexEPqdjRxMaj3hFID3dGZmLdmBpRXNDk1yO1-GlyM7-CojJQBEEc2H4HpuKI4jph2lgrpnF9W3P4nthOiB6o2davOEYFJ1VE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=qavVU_VfCE2NB30Ma_88gn3IbonYbpMami4GBtd6PXcfaRMBPAiSQYVpzxdXn0-eBrClfMVtFXo6hhyjTmhGN0BMHobUJVcsCXzpU39cmc15pqS8rcYvFVdTtWPVHGMTf5wTu8tzZ-N7NSZ4hmRNrSjuD7MA-NxuDv5y7MZe8uhi5CmJ0sBeise72utdl9mtyaMC1jLL_umLzzDUaggj_OUDQqGjzFBKwYjyIWM7TJHPBz5Lhf1CEbW3dyL0T_YdcHy7fsTXb2p4HjXmZ5bV54EoZ2AC3txFcERnWk-mzFn_NfREKfHkSozNtNvUV4FmnWIQvpVfYElSIBxsNCDebw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=qavVU_VfCE2NB30Ma_88gn3IbonYbpMami4GBtd6PXcfaRMBPAiSQYVpzxdXn0-eBrClfMVtFXo6hhyjTmhGN0BMHobUJVcsCXzpU39cmc15pqS8rcYvFVdTtWPVHGMTf5wTu8tzZ-N7NSZ4hmRNrSjuD7MA-NxuDv5y7MZe8uhi5CmJ0sBeise72utdl9mtyaMC1jLL_umLzzDUaggj_OUDQqGjzFBKwYjyIWM7TJHPBz5Lhf1CEbW3dyL0T_YdcHy7fsTXb2p4HjXmZ5bV54EoZ2AC3txFcERnWk-mzFn_NfREKfHkSozNtNvUV4FmnWIQvpVfYElSIBxsNCDebw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-CiSY6nRUM50sNPbjxsECzofA09emskfQEOdeXBsxlXdIm4kDJLOYYf0xE3-wI_zon9zzqhZhvRG9gs2wRvWM1W9CK3qHb-kq3aFEvar-igxBH2C43JqRlJMrz5V9froXTakLdraktwZ0e0HkOcMRLv8fbwiXY19dXMj0VocjLD96jlC1CDP_UfazBxGIv-MAfR8Fr7ThBrUvDSgo1VM09HopvgUl2Skn2UMy3CuYICxafPfiTs4fOyTwIDemVAcl-0hxRvWfXa7Vv78cP4VnUfqzuFTbhgtx0HugTEk86KwHnHk93J6_JCAgwzFCePSZ6JQSedDDiQKMu2-Ex8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=tLglvAdIOSnM7cAqy0bpf09KBgVZ3oW8W3utnVecX4hcjvK-Go-6A-VsQbDCG3PXR6VsH8CmN5AeA93_knG-CuabSY0tL5EV8kPqArb1Wu4X2Ns7jJid3GldxMKmYZjjZSRdfdU8wg5TWMH66y28HjMS9gqCzS_A3O0TuD_v4igSJ-xA35DgSCfSIr_VEvE5NYzej96K5diSFbLUFLv2cxmnDpqCapNi2aAToDcXV5XDR6-aArCzAtZC6e0X13v64qnzaEdtQAy_Y3uGo0HBlLCPJB7SKflnJCujh910kf2Q8rzIZo7MkgXMisx_j9VJuTwM23ZGNxM1OxRmUWqjMJlYEib_AH8idwZ2eht_kCWmSVO-CSMaJic_WMh9yC9B7QxoNZHQlPbBG2TALnoG1q6WoOY35TZIAhw1sDdR_oB04PQjbTFq6GrOHYBjdB503TipYN6aaa5aYKip-768I4z1BAIQlHX3G4SZKNUmSbKYn-qrJYGehVJObAO3Wvf1TSt8QH0YF0UwL9MywVrHBP1GtSRFUJVqtit7VyHWhSXv00_F8HHke8CWEk_AftWNrf0VMIHCoVfcjQtmmuBPEfsF5VVtPSMhblHtAdRDV1EGS2znUlJLHwgf4xLkj3i7A4E6_iCOqKOy6vh4UR-R1_D1WVDdevwpfbaxfLnpBPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=tLglvAdIOSnM7cAqy0bpf09KBgVZ3oW8W3utnVecX4hcjvK-Go-6A-VsQbDCG3PXR6VsH8CmN5AeA93_knG-CuabSY0tL5EV8kPqArb1Wu4X2Ns7jJid3GldxMKmYZjjZSRdfdU8wg5TWMH66y28HjMS9gqCzS_A3O0TuD_v4igSJ-xA35DgSCfSIr_VEvE5NYzej96K5diSFbLUFLv2cxmnDpqCapNi2aAToDcXV5XDR6-aArCzAtZC6e0X13v64qnzaEdtQAy_Y3uGo0HBlLCPJB7SKflnJCujh910kf2Q8rzIZo7MkgXMisx_j9VJuTwM23ZGNxM1OxRmUWqjMJlYEib_AH8idwZ2eht_kCWmSVO-CSMaJic_WMh9yC9B7QxoNZHQlPbBG2TALnoG1q6WoOY35TZIAhw1sDdR_oB04PQjbTFq6GrOHYBjdB503TipYN6aaa5aYKip-768I4z1BAIQlHX3G4SZKNUmSbKYn-qrJYGehVJObAO3Wvf1TSt8QH0YF0UwL9MywVrHBP1GtSRFUJVqtit7VyHWhSXv00_F8HHke8CWEk_AftWNrf0VMIHCoVfcjQtmmuBPEfsF5VVtPSMhblHtAdRDV1EGS2znUlJLHwgf4xLkj3i7A4E6_iCOqKOy6vh4UR-R1_D1WVDdevwpfbaxfLnpBPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov71Ck0UDe9b8wYswzyloYBggvcWiyo_ROyzt_ZalASXJh3Rkk4HdLP3TL9XcHPH7W3VUAf6hIEYUqUC6E7IlyhcOvoWwQQhyH8W-O6owsvQUSusYV-dZsD8q1erf_D0A6T_2VSbYNaqo2Z_8Cxk0ihQ4effWlf8zEh2SPfFCPe88lNEWQXrEoFF8phEOtZbJmXcHLstbyDiFAxWe08lG2uYVfSpkhirem3svT0LDTdA-1b81JJTa2A9JoV6S5xHWTVmXZ5HFuT61AO7NVrakoN2Bg_4jreY1vwOmXScyEytZsK8CQgZ4j1SzFFZMjcKTj2mOrMFhq0BGZarLGMT-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=oHjE_l4fnPyJ9JtkFI7Y2f7z5lVeGaw2T4NjPfInoR3IKDTUwmNlNA36iTUMKVKx2aMqAChf68p6ymc-lgpxf1ANXK7lJvGfefv8zDEI7beRy62W5Gz5LiSJpV6h5goHYsaCrG6p34hbIvBaULd-SXH5tQUMRaqimO72agEYF4CPm8eS_B6gBYjDYDkW_zxSSFEArzWldrF8PY-1UJ_wXFUgg0NlhJBbHY-Z7FyyIVwwYmXwrWoyfdeqQvLFKGHGxQeUSJc4ndlvmQxPujMWv-ADXpHhWckQZUrpCbsmCDJksGd_IYRMsX5cLCd0XRFmQqxKIH4hPiNlSqGApmFaDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=oHjE_l4fnPyJ9JtkFI7Y2f7z5lVeGaw2T4NjPfInoR3IKDTUwmNlNA36iTUMKVKx2aMqAChf68p6ymc-lgpxf1ANXK7lJvGfefv8zDEI7beRy62W5Gz5LiSJpV6h5goHYsaCrG6p34hbIvBaULd-SXH5tQUMRaqimO72agEYF4CPm8eS_B6gBYjDYDkW_zxSSFEArzWldrF8PY-1UJ_wXFUgg0NlhJBbHY-Z7FyyIVwwYmXwrWoyfdeqQvLFKGHGxQeUSJc4ndlvmQxPujMWv-ADXpHhWckQZUrpCbsmCDJksGd_IYRMsX5cLCd0XRFmQqxKIH4hPiNlSqGApmFaDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjLuoKxY1GrrcRsza9_MXxbdiHwBeelacZiX0qo4Ss6ZKPi-2wP9aHNSGFArjjO_nxqogqErxkWQZIRXfbmZPt5msgmNcQCsjo8N5eJTSNTei3LCv5m6UCH29Bqwn5Afa92htrHo3RpHAPp-tncZCpMX08RNUnBAm_5NCHkca7AX1bBRyujni9f1I_Jb99443o8QPyyZJ-T_B8vKpJ5pex_cbpCvZjCTxYT-QI8UwRPp2Su1_ozeFKPrz8CUa6rHE4TlMPYGVo--YWo3d05fA5qArGDt8h9OaybDhwNUspfhReZLccQgJeMiy8QQuPoErDHF023VqXcZ087JIPxCHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkK9hbd8aNuVion5D6VbImtjukXRWk2vfzb0moF7iiPW6ht3Kr8YhnTFqc-7DK_7gSzTDQ2kdgGI_QKQ818NAc5_EDUS_QsvEw9tY0ojdq3G_uZPw14s-32DkCeRBRxnS9U8cKokH1HFAUXb8ImhOjJR21WX3dt6p_xZ-8ZVYX5dCQu4jhP_xtrRNEyABZYStuE3v6oxrk-JxQlcKJJoBy-m4HK4CGMydtZWiKgs7rxWxA58h1Rf55TgzUiPi39kC8pd8YmjSGm3XLYBP_F6y3EPuumN217C42ggBG2RDTeqkK3OCJxFedVAzK16FkMgfnwrYhuXAjmzFg_eL6KbxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwDIQiy_ZZXbgxhqzvzeoqcrOb8g0h5V2UttMZ5GYB-2iuCgCvrHWI8gIagno7GyDZildpq2WXYnvihV2RYhZfo1HoTQphHmMvQmapJFDnZK0BuE9ogq95L_Re4tz1jEtf9nyJeBM5t6S5OGhqsSPET2XgEHLSM1zOHFg7OcOVjISaDqpfvph423ktZC_R8rET4lKTk0pAw3S8SVrqEfgV-O-1asGFTTcWhtu0z9V3S_tlra1hyl0mUBFYaphToULs_9JLTjGLyX9Bl43oGILESl_sYC50pv0FsHWbEhKeeHO9Y5ts4XFftsRSeEcP-ZHX9VZIWMBQQbfGmsKaH9ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=lnwRSLtAPwQz10d_lkpqRBIQZelG09o8ycq_KZX93sqxuYW9WmeopHST7LBH7C-VEw59qnNCfNdiWnH3An-oHxHj6cFBwU08kWm3GLnT0pQnMGyIPEvLcS8y4EqRR0yFCfhxr8IpCq638X6RWQVF39jhUOZKBQ8SmZ2sSYUQtaQwngWO-jSStE24rcZoj7rpBQsLtf6QwwbL78Cb03IyNCN59CcLJm2pRus6Qht2VU7O2dk1_HZ_M6ev0uDM61LvgXzIAk0qaippt5L4-sqvVgUp3MKXTOk_esq42PSiXCgZordyf3MwswplEsHHc72cnlbxoMqTCLFX7hvMUmuH1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=lnwRSLtAPwQz10d_lkpqRBIQZelG09o8ycq_KZX93sqxuYW9WmeopHST7LBH7C-VEw59qnNCfNdiWnH3An-oHxHj6cFBwU08kWm3GLnT0pQnMGyIPEvLcS8y4EqRR0yFCfhxr8IpCq638X6RWQVF39jhUOZKBQ8SmZ2sSYUQtaQwngWO-jSStE24rcZoj7rpBQsLtf6QwwbL78Cb03IyNCN59CcLJm2pRus6Qht2VU7O2dk1_HZ_M6ev0uDM61LvgXzIAk0qaippt5L4-sqvVgUp3MKXTOk_esq42PSiXCgZordyf3MwswplEsHHc72cnlbxoMqTCLFX7hvMUmuH1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H4NEWxivNBTWb6j1LPGlmsR8n-7tVj-cO62JxEYpk2Q2uTPlU-_GNkCWQn4C-j2Ud_xR-e8iK0banaaNP7rIqW6pVIWMybL186KrFGRe_R_QddL3_ROoyPalPnOE3lnJV4pIb_gGsAWPe3OZ_NqLDs944BuTe7ViWgdYungm_rZB8wQpRItIVyDUEJrOJ3q3NDWGsdwRyk2rk_MTX2RVpKRDcDvWhlrj-vUa_5XPNxf9qhg4Aqml7YYpBW8flVTe09dSSbxE9w0wTC3pX54n2QBRaOnjd4E3xtzv085Zc3s5Hm8KanA_6X6_n31QEVepQoXbcbw30QTi0NsT8TuDUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuxMtbe8ztnzD5WBX7VX4Izr_bjlZnTV3rP6u53xmLhKorLSrP9UzKWSUKcC45oK9aBYJp7u41XA0Hg5Vfzd-PmIrdPViv5HQGuxcpEanRNYlryxULvP0ByxdssXK521adGr1KqWnDkmR-tNzgTRsUWPLizZaZ9ozlfL9xj1wzPzdyxFBU6hyZTEy_hEQ-eH8MXUfXT5UBwYDdLkyZ15B7t9V-6nHrI4hn8Bt8hGOQtA697sRzaW0nHdlFXRDWHYuEgMw8ksNaLEUyYpSDLmss2BlJGu-aLp0Hf1D0VfGEFj5Onf7E3paN2gMkV81OYr9vm9LKM-Hhiz8E5VMUeY1tyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uuxMtbe8ztnzD5WBX7VX4Izr_bjlZnTV3rP6u53xmLhKorLSrP9UzKWSUKcC45oK9aBYJp7u41XA0Hg5Vfzd-PmIrdPViv5HQGuxcpEanRNYlryxULvP0ByxdssXK521adGr1KqWnDkmR-tNzgTRsUWPLizZaZ9ozlfL9xj1wzPzdyxFBU6hyZTEy_hEQ-eH8MXUfXT5UBwYDdLkyZ15B7t9V-6nHrI4hn8Bt8hGOQtA697sRzaW0nHdlFXRDWHYuEgMw8ksNaLEUyYpSDLmss2BlJGu-aLp0Hf1D0VfGEFj5Onf7E3paN2gMkV81OYr9vm9LKM-Hhiz8E5VMUeY1tyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6Jj7jwx8UVe9_gJS--eoWf6qKIfMmMS8pT3dQUy47YY-AnSV-vGuLhYN70yZ-Oohi1ka_b-n4LsSQXPLCXpzPVpM2vKVb-9p3n4Z7lcl2hAuMUo8K-2amvsV4KM1iwdM-i5QC2e8hJWYhLXYkngvtdGde5eaRJLlxjk1wBA8HBVJSF6ic3VB3Rdc3Ix_DzHbf17jnBgAeSqQVklsxRub-p69AVnISgYdzMqGh62LqlGIqYa_fl16vKLdZcilb1_XFvgge1Z1IbUKYeboZN-iwJywiSWIusko6ZM7oWI7_Kf2ZQYVgKy599JmNUI_lV35HHJwhTcYt2RgNEyuf0dPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=p6Jj7jwx8UVe9_gJS--eoWf6qKIfMmMS8pT3dQUy47YY-AnSV-vGuLhYN70yZ-Oohi1ka_b-n4LsSQXPLCXpzPVpM2vKVb-9p3n4Z7lcl2hAuMUo8K-2amvsV4KM1iwdM-i5QC2e8hJWYhLXYkngvtdGde5eaRJLlxjk1wBA8HBVJSF6ic3VB3Rdc3Ix_DzHbf17jnBgAeSqQVklsxRub-p69AVnISgYdzMqGh62LqlGIqYa_fl16vKLdZcilb1_XFvgge1Z1IbUKYeboZN-iwJywiSWIusko6ZM7oWI7_Kf2ZQYVgKy599JmNUI_lV35HHJwhTcYt2RgNEyuf0dPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=JJ7CiSikXawaXAAeTJprecyTu_OyDHac4oSQMe0u4AEMTtN2YU13R8mDy5FlSIHTJ1fR0QY8E2-Loy7nXhvktwGociUAHXV8JMxnWgmNhpMkptMRvxLHRXfqYlYCy4cHgtgAhsPGmRbNtSDZgK2-kviid6GE3ruGKGnMFIbGFwDXSvkxfyouoQxPd6t318tD804jnK2OFzDT_MMcRHhSvJiOpnVCzA-Yb_zSR2dnfhFHOtNuJNZjdmzxjzN_ckTNPR3y5UCAiMqLUh410QH6GGh6t81WsCptXxVio2iTamb-2d-7MhBCQhPNByV9E1SYPejCiQ6vTYW3aK4Zn6qt140OKIhoSIuavNNV1zLzLvUKTxtVQpETt46PIfg_IDE6kd5UFYMNYivYLBGNkuY1fKnjOjLUu7-u0GudkBuyZdqXFEIbgCST2s1Iqgr-1fUN8HjPj-UR2ZrrF9p_UFJEyHo7Zb-RNfO91vb3SuvbuvotHE687rjuekUVuKOTM_3Y--0xhleVbTOOWcy0SSq35uHWxnQ9VLidGUN9lYG6CFPSLaD9Dv5tQb1giiVH2A9BTt5DjwP5fUc5YgBtXxhjGm0J7mTwDbgamergsiqR5Tf_xQ0LvixxkH_LOEgtL7sQk40JKx4Pse4sdx5P9S1OyvVC4RH7bpp3OeZTMV18vCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=JJ7CiSikXawaXAAeTJprecyTu_OyDHac4oSQMe0u4AEMTtN2YU13R8mDy5FlSIHTJ1fR0QY8E2-Loy7nXhvktwGociUAHXV8JMxnWgmNhpMkptMRvxLHRXfqYlYCy4cHgtgAhsPGmRbNtSDZgK2-kviid6GE3ruGKGnMFIbGFwDXSvkxfyouoQxPd6t318tD804jnK2OFzDT_MMcRHhSvJiOpnVCzA-Yb_zSR2dnfhFHOtNuJNZjdmzxjzN_ckTNPR3y5UCAiMqLUh410QH6GGh6t81WsCptXxVio2iTamb-2d-7MhBCQhPNByV9E1SYPejCiQ6vTYW3aK4Zn6qt140OKIhoSIuavNNV1zLzLvUKTxtVQpETt46PIfg_IDE6kd5UFYMNYivYLBGNkuY1fKnjOjLUu7-u0GudkBuyZdqXFEIbgCST2s1Iqgr-1fUN8HjPj-UR2ZrrF9p_UFJEyHo7Zb-RNfO91vb3SuvbuvotHE687rjuekUVuKOTM_3Y--0xhleVbTOOWcy0SSq35uHWxnQ9VLidGUN9lYG6CFPSLaD9Dv5tQb1giiVH2A9BTt5DjwP5fUc5YgBtXxhjGm0J7mTwDbgamergsiqR5Tf_xQ0LvixxkH_LOEgtL7sQk40JKx4Pse4sdx5P9S1OyvVC4RH7bpp3OeZTMV18vCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=O0AtLv5yuvKs00uYtOGhIZ9yR6zFAImCfhs62pZjs4CnZXWMNPGoOQKyCawnD2zp40TPYjjYJK48gTCWYHQx5bGqxet0c61EF-p38aYH3zMFH322P7k1UcWEDVWGOrP0ANRv4Y7kq-X3-7Fl5JiE2_Kn-GRsvv_cwQToTdcku_V4tjU4ZRZDibIf8RxPPN0jWIRwQEMrEmIpIs6DSn_6MMmnQ1VJCZxrCP3lUvT0gEmF2HRP5DelPv2ttroB23VHHwkWGtCHUVPKD3yxvr52qPF1ezfe6TS8Kd1X4XJLPq4c8x5QtR1C62CBCP6ZC-LjQUzQ1E2dYcvr7W1LjUzNaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=O0AtLv5yuvKs00uYtOGhIZ9yR6zFAImCfhs62pZjs4CnZXWMNPGoOQKyCawnD2zp40TPYjjYJK48gTCWYHQx5bGqxet0c61EF-p38aYH3zMFH322P7k1UcWEDVWGOrP0ANRv4Y7kq-X3-7Fl5JiE2_Kn-GRsvv_cwQToTdcku_V4tjU4ZRZDibIf8RxPPN0jWIRwQEMrEmIpIs6DSn_6MMmnQ1VJCZxrCP3lUvT0gEmF2HRP5DelPv2ttroB23VHHwkWGtCHUVPKD3yxvr52qPF1ezfe6TS8Kd1X4XJLPq4c8x5QtR1C62CBCP6ZC-LjQUzQ1E2dYcvr7W1LjUzNaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lq4D6SA9hYjhmA2bjZgIAwt8INSYaQ9Wzq9nB3_RihHqrnMPXaDm4oshldxxG_MaXGNx8hJZN-nXByas9SMGRI2RO0hLU9AR5wKS-KxiYFo-XldWLa5Ge5zz8XjtvcZTG4bpiHpMR-xnazBDoM4aZtVaQPnlOzjfTq-IzkR3QokY9e12jne7uo06NZlxSZSz9nC6ewFRmWXlp9cocbqzHKpW5RIClATk5kA7LeNpSxcYBxwAaDUpeqg1grkwQWyTqGZ8PuAw8xBcF_YWDw5rz-VsYnBHUMOfczY2cqTnKR6mi_nYDuUr2RcgHZqfKMiKhQ30zFnK3vezzybxi_O6EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=d7Z0WgPUSWhTckqYerV1okghb3GOXeAP0J-SvmJvvGMX_Mcc73wPjmyG2f7nZkeh1EmXhoZnjpPPd4DDRLY4Tr6XU6Z-twfoJmA-N5MilECDN85vu8glNbVGgVjst7jrRq2FUGa08HjH_mGJ7I5eisgYfOqp490qYFwOfIw5udf_Yg6u0b_Cq6LkfQvI1xi6ikdJpds3-6KJwtvoaMIp6emYBqjAoeArsLV4_ofh7yL6ice0LpEukvHn2mgQZuMztejx6enLyfJIN_zoKVYRGvm-FW2ToEDAV28V36UNWkR9qUjtA_tASJUZPYptrETn4Lj2Fq87N3Pjw4daVm8Mqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=d7Z0WgPUSWhTckqYerV1okghb3GOXeAP0J-SvmJvvGMX_Mcc73wPjmyG2f7nZkeh1EmXhoZnjpPPd4DDRLY4Tr6XU6Z-twfoJmA-N5MilECDN85vu8glNbVGgVjst7jrRq2FUGa08HjH_mGJ7I5eisgYfOqp490qYFwOfIw5udf_Yg6u0b_Cq6LkfQvI1xi6ikdJpds3-6KJwtvoaMIp6emYBqjAoeArsLV4_ofh7yL6ice0LpEukvHn2mgQZuMztejx6enLyfJIN_zoKVYRGvm-FW2ToEDAV28V36UNWkR9qUjtA_tASJUZPYptrETn4Lj2Fq87N3Pjw4daVm8Mqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Y6FBeyY4YbGJXw4cocHK4CWCQkxjXSDUcftCYHzu9vvQlgWS-xswk8K6ENeCvLP0LB2areoJDQr7-bCTjUAXyZkaiQhnTn1a6NbP4NpgPz65QvuakJiYgXS4DqK5hXWau_CO24JQMSVprK6jmRxZdG9dzz-EyrJkZWEmu18URNtt855__Ts855wiGFdVLCbf9Q8gogdcVdkog-kaWcowmjWk6Az90_cy9n417uk8X4zcQ8ocJN_wx9yj1u5c1MRbODRZDz6LFjesRHVob8LAnHjvpQPvwjCTzfJHZbRItRiPwxosQzG31QKC5e54Vo4HBqCy5oGuniI_XCMMxKvyh07lXyH_AS5J9va_c2R0Is-kgPcOymNgbz08JAmdhseCNy34a-aNbIFTgtaj1ATNfO-fbyVi_O0oMMKM4cA0oOa76zEOf5i6qeyi-HgIkbP1sQ9xJNkxSBVdofUUuXxqdUDdAQOj891Iiywb8PRhbhS3zhYKwmFejs93izOnhFk84TCzBcpNhdV5w8fOhk7rRbxQ0HmiQcpL9oEMfKmcI1FfqbgAk9cC4jrwbBtCPj9l1Xhxjb5iXEpUscQditwEQ7v-Hcgkcvy6AYKI0VOl9XRimn73-5r2xtqNwnBwNgTwcXkFioptv4J24WsL6UTkk1TIuI57SQvrOGwen2BXHQc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Y6FBeyY4YbGJXw4cocHK4CWCQkxjXSDUcftCYHzu9vvQlgWS-xswk8K6ENeCvLP0LB2areoJDQr7-bCTjUAXyZkaiQhnTn1a6NbP4NpgPz65QvuakJiYgXS4DqK5hXWau_CO24JQMSVprK6jmRxZdG9dzz-EyrJkZWEmu18URNtt855__Ts855wiGFdVLCbf9Q8gogdcVdkog-kaWcowmjWk6Az90_cy9n417uk8X4zcQ8ocJN_wx9yj1u5c1MRbODRZDz6LFjesRHVob8LAnHjvpQPvwjCTzfJHZbRItRiPwxosQzG31QKC5e54Vo4HBqCy5oGuniI_XCMMxKvyh07lXyH_AS5J9va_c2R0Is-kgPcOymNgbz08JAmdhseCNy34a-aNbIFTgtaj1ATNfO-fbyVi_O0oMMKM4cA0oOa76zEOf5i6qeyi-HgIkbP1sQ9xJNkxSBVdofUUuXxqdUDdAQOj891Iiywb8PRhbhS3zhYKwmFejs93izOnhFk84TCzBcpNhdV5w8fOhk7rRbxQ0HmiQcpL9oEMfKmcI1FfqbgAk9cC4jrwbBtCPj9l1Xhxjb5iXEpUscQditwEQ7v-Hcgkcvy6AYKI0VOl9XRimn73-5r2xtqNwnBwNgTwcXkFioptv4J24WsL6UTkk1TIuI57SQvrOGwen2BXHQc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqGZAfgiNIGmMXgGvxmkYD8M8YOmZVsRXC9whXT-PwcchM01-wdqWO8xSgoz8naHko6LML_jPdA5YPCydADd68sBftpHvm_22QrsGYy8T5MtK5pkfptKrex8rCn7AlJ6LjX_Dzx1t9xU3AOyDl4pLoAY9CuHEawxHveOv91-xhT5c7MK95BtimoZohIPTab1Ub0RkcCUMKH-8k7KgdSA4GgptGTXzt3eqT-BK9FNgUCxSGK-ZKzltuqf4ejN1xwE4_f8a9GCoWCa8TwfdHy3jyWxIAE6-xlaIhPDK_dxtEJvA70BiyPjnTUTFsX6gJDwIyKbRyeF50vOborLvxAvKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=LkVSrSCWbV5Ba0koLb2uLaSO4wBKjL2cBzp5YK5U--Ocki8SzJhFi_olNUliPQ5Js72A69uvOqQoO7gE8f2ZFZf6XZg2AicNjnN3BZIr4Szl0szoDNz53GCSmApGUbu6zCJ11Rfzeq6CrQ8ffMfk-mGKx0xmf8_AAdhkG7J1unC3PlgcOfLHjwmOnt14TUY_boJ-ji6u9GyVkgmmzjwufh6qUgmgq8UrgX2tK0VKks7cfRFpTdKkrT9TQBgGHppd5IdLb2CDxx1JfdoFclxpA6mI72cFqGQLmb0l1tvHSwjsVUybXPlbWX2v4EhuhjkdKuGVeHXldqns0s-_30Km_0rYe35IkmcpclSReOgrSFfD9FaB64DrsJRnyJt_P6rY2lLpk9R-eOWiOSY3NE8hzOoPp1bH-dBa3AiRXQlkajqoH6eqMYGCIMJ70xES86S0pCvNo7djME0MibbkTP8s5raIyuJUo09llqjJDQsfur4Oilt--a9lLUe_lT-oWWnnaVH8GhdzKPG4d5ShCZyphdaqIOIGeRwIZI83wwd5PIdxmi2U5kG6wDUqEtLj4b-e8WvImkzesbQ9LEHRQOy87sRT6U6P8hju3qWfpgI2y-8-GXv17GBIIqZaF_hQOzLMX2Thwsq343Aw3VIDEON00pPwkoYWA8302p6CIqpST8E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=LkVSrSCWbV5Ba0koLb2uLaSO4wBKjL2cBzp5YK5U--Ocki8SzJhFi_olNUliPQ5Js72A69uvOqQoO7gE8f2ZFZf6XZg2AicNjnN3BZIr4Szl0szoDNz53GCSmApGUbu6zCJ11Rfzeq6CrQ8ffMfk-mGKx0xmf8_AAdhkG7J1unC3PlgcOfLHjwmOnt14TUY_boJ-ji6u9GyVkgmmzjwufh6qUgmgq8UrgX2tK0VKks7cfRFpTdKkrT9TQBgGHppd5IdLb2CDxx1JfdoFclxpA6mI72cFqGQLmb0l1tvHSwjsVUybXPlbWX2v4EhuhjkdKuGVeHXldqns0s-_30Km_0rYe35IkmcpclSReOgrSFfD9FaB64DrsJRnyJt_P6rY2lLpk9R-eOWiOSY3NE8hzOoPp1bH-dBa3AiRXQlkajqoH6eqMYGCIMJ70xES86S0pCvNo7djME0MibbkTP8s5raIyuJUo09llqjJDQsfur4Oilt--a9lLUe_lT-oWWnnaVH8GhdzKPG4d5ShCZyphdaqIOIGeRwIZI83wwd5PIdxmi2U5kG6wDUqEtLj4b-e8WvImkzesbQ9LEHRQOy87sRT6U6P8hju3qWfpgI2y-8-GXv17GBIIqZaF_hQOzLMX2Thwsq343Aw3VIDEON00pPwkoYWA8302p6CIqpST8E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=lRzDgCgrdyys6ZUkVvtUktXjNZNQE0faH0Sz7fn6xJehiFOgSugDStti3Cv8ZDIkdImneILPrwTK5Ea_8dYq4QZbYAwYV33ts6oBKDxc7cNBo-F6d_9P_FJIT0C_cLvkpPrmtOmEIzN5-0uqlRiu7XuPjlj58ib8xhAORPXvjclrGXX3k7bXSBydBUXOqvDwtUjylhidrDRaJMtjvOhwvu9V3sGDXlyABZXI3lT9B9_Bj30Acn6DsNaixx49ctm_flgYWOa5_g2aPVjFFXKM2SMHBSFI1Q1IhxoQe4iMbsOwNvUcBpraSsBUjKA5nIaMC5hg0_sNYiMoXWwMTlfkV3rdKHrEmO5ojN_o8lyQOahtAf16DQYmkuU2HMrM39U-P9SLebyifEg9wEFc7jjyfk4XOcYsvrGS_U2-na4pyzphKtcwtAFG6luzt9MXSJeuyA8yVmw79j1v_w5u7l-8rFZuVmE9CnSyzqR0tcVfXD9i-cUmL5er9Ht6iws9XiDxc8mnCtirKTEo9jovusLYEnMT3PsO2bimWLDqLuhpDdexMwpT5Nqm159atEbtJ4WamX4zoCCd-50H2Ao9DyK3mKB5Jv9okD1d2G-sHhgno64DjjJnmTh--Kfu_eXE4T8ieT7lKSh5OuqDm5rGqsi1_7mAxwC7Jt6MsKO-TO0huQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=lRzDgCgrdyys6ZUkVvtUktXjNZNQE0faH0Sz7fn6xJehiFOgSugDStti3Cv8ZDIkdImneILPrwTK5Ea_8dYq4QZbYAwYV33ts6oBKDxc7cNBo-F6d_9P_FJIT0C_cLvkpPrmtOmEIzN5-0uqlRiu7XuPjlj58ib8xhAORPXvjclrGXX3k7bXSBydBUXOqvDwtUjylhidrDRaJMtjvOhwvu9V3sGDXlyABZXI3lT9B9_Bj30Acn6DsNaixx49ctm_flgYWOa5_g2aPVjFFXKM2SMHBSFI1Q1IhxoQe4iMbsOwNvUcBpraSsBUjKA5nIaMC5hg0_sNYiMoXWwMTlfkV3rdKHrEmO5ojN_o8lyQOahtAf16DQYmkuU2HMrM39U-P9SLebyifEg9wEFc7jjyfk4XOcYsvrGS_U2-na4pyzphKtcwtAFG6luzt9MXSJeuyA8yVmw79j1v_w5u7l-8rFZuVmE9CnSyzqR0tcVfXD9i-cUmL5er9Ht6iws9XiDxc8mnCtirKTEo9jovusLYEnMT3PsO2bimWLDqLuhpDdexMwpT5Nqm159atEbtJ4WamX4zoCCd-50H2Ao9DyK3mKB5Jv9okD1d2G-sHhgno64DjjJnmTh--Kfu_eXE4T8ieT7lKSh5OuqDm5rGqsi1_7mAxwC7Jt6MsKO-TO0huQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=cGz2QmlEBhFljJzgjEo44QnuQR9PqJ3suP7IZMKXZMS2b-Epf6Ow96uv9F8psZ-IDPy2fmaLvM8-__CrygV_LZ-hu1HQV-4iUPotFi33JzuaFTgvV94c22Y35S-N7qvamEXSaDvyfIdF2xAvsMneixBSEWswmljv-RR1MN2iIHPKljypJdMcgviQf57ZD_Gfhb2EuMR1yGyy-Z7WqrGuZME01SBQvMo9NPM3Q9Zv-XrpQzQrgyM-K1oR0I013Pzk7lqZppqvsG_oNJ-83LwdMT_MK3IrMhUyIKidpUDqc5aEBV-SfnDLx1uVKRHbZ6U6eWVO5ZqxJ5wBMNMyYg894g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=cGz2QmlEBhFljJzgjEo44QnuQR9PqJ3suP7IZMKXZMS2b-Epf6Ow96uv9F8psZ-IDPy2fmaLvM8-__CrygV_LZ-hu1HQV-4iUPotFi33JzuaFTgvV94c22Y35S-N7qvamEXSaDvyfIdF2xAvsMneixBSEWswmljv-RR1MN2iIHPKljypJdMcgviQf57ZD_Gfhb2EuMR1yGyy-Z7WqrGuZME01SBQvMo9NPM3Q9Zv-XrpQzQrgyM-K1oR0I013Pzk7lqZppqvsG_oNJ-83LwdMT_MK3IrMhUyIKidpUDqc5aEBV-SfnDLx1uVKRHbZ6U6eWVO5ZqxJ5wBMNMyYg894g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=jtaT--_-VriM00QciYtmXsKsGgTjEaRJoFasPmaPeETJxQPuqNUT2g7zSXFeUnmt6bGdV5nUh803SJvdlIQZRcj3oFxuyoMYogq2i4JZUyTDG29E7QdQ8ukvchHJJCmaBDu6z-cakM-lT0lXJSDznJM5bNOm8JxumCOeDwSwclgD7QOfwj-yd4h81Cz_pbkR15bkX1GK-i388jYnhyRAoSddSP7m52-qbAPhyh5zqRUWJsdlScdd5_VAas1ATS3x9yMsYg4eAMk5vH9G92v8NcyORRxbmS46aM2gpQdRnSYuyR25iyyxtkDhAAJg4ZL-H0mSMU67whNcKHxeJdk-Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=jtaT--_-VriM00QciYtmXsKsGgTjEaRJoFasPmaPeETJxQPuqNUT2g7zSXFeUnmt6bGdV5nUh803SJvdlIQZRcj3oFxuyoMYogq2i4JZUyTDG29E7QdQ8ukvchHJJCmaBDu6z-cakM-lT0lXJSDznJM5bNOm8JxumCOeDwSwclgD7QOfwj-yd4h81Cz_pbkR15bkX1GK-i388jYnhyRAoSddSP7m52-qbAPhyh5zqRUWJsdlScdd5_VAas1ATS3x9yMsYg4eAMk5vH9G92v8NcyORRxbmS46aM2gpQdRnSYuyR25iyyxtkDhAAJg4ZL-H0mSMU67whNcKHxeJdk-Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=E1f0xgJjGsPxcIlzrnqwUG3axHmO0IacWt8uLSWeTAQEqMhJH_t-0Vh_QnD6vcOIr8qke7X2P1HBx8YPlemg99omg8kVcGALx_LkB6Qh9pIKQBxNHbJxEp3n0Dzv18Rv8XluvPwA8Go7DB6HB49twNiTB_et3oZ3T2ZNYgx_vAmj1yVC7i1IjwwDGIwphHdwAyJCeRAeBJyiLsltsJ3fwVc2r8C9FBxO1FB0YgdQeZUyaGAa8eHsPGRsvMUy36CpUvcm2aEbK-uW39Fwd526XTrx6wsbLIcA1IEJxb0KB1392g6sg9Qu5gFw9lQqWt1tAnraYs2mklyVkHMl0vgYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=E1f0xgJjGsPxcIlzrnqwUG3axHmO0IacWt8uLSWeTAQEqMhJH_t-0Vh_QnD6vcOIr8qke7X2P1HBx8YPlemg99omg8kVcGALx_LkB6Qh9pIKQBxNHbJxEp3n0Dzv18Rv8XluvPwA8Go7DB6HB49twNiTB_et3oZ3T2ZNYgx_vAmj1yVC7i1IjwwDGIwphHdwAyJCeRAeBJyiLsltsJ3fwVc2r8C9FBxO1FB0YgdQeZUyaGAa8eHsPGRsvMUy36CpUvcm2aEbK-uW39Fwd526XTrx6wsbLIcA1IEJxb0KB1392g6sg9Qu5gFw9lQqWt1tAnraYs2mklyVkHMl0vgYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=n-DiDJr3_E3RzaJlMZn4-rqfoHAYyXKAR5MWujwjni0RXsBp5joxkZyEF55DX3HZqhNGnmlDk7s8mPjco1HbfBEFRp-VmjaPaVMLye91tDNKPq4ze7bfZViozIAlNlHygbT2Qf9Ffv5kWECq69ITLI-EzW6SczIF-OS13A0gMJwWFm5JGYWFh8WR-zTBAHU9uyqzvBHxmMKcz9LN2rbNXTFbq9UwSzqPdA___7fDlR9H59-suMEJUUB_FmXj5WFF_Lj2gXHTPTzTt9BCwXJVwaA2erSzCoLupi57jGj3HmvnLVB3oXpoeJcMSvrt6ORurJtvKWmkzad2KBkqUXvf9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=n-DiDJr3_E3RzaJlMZn4-rqfoHAYyXKAR5MWujwjni0RXsBp5joxkZyEF55DX3HZqhNGnmlDk7s8mPjco1HbfBEFRp-VmjaPaVMLye91tDNKPq4ze7bfZViozIAlNlHygbT2Qf9Ffv5kWECq69ITLI-EzW6SczIF-OS13A0gMJwWFm5JGYWFh8WR-zTBAHU9uyqzvBHxmMKcz9LN2rbNXTFbq9UwSzqPdA___7fDlR9H59-suMEJUUB_FmXj5WFF_Lj2gXHTPTzTt9BCwXJVwaA2erSzCoLupi57jGj3HmvnLVB3oXpoeJcMSvrt6ORurJtvKWmkzad2KBkqUXvf9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=GDcQFqn1otWgb4ebWERHyluMdZU0DRwE7t84cSU6cdDfqxuvCBTZybj9wwlMdS3evfQ_Ljxzk9Fj0pM0tdW0viE_hrun722JzOPZ7EsgZFBCCSzvrJ_bwHqCSpygqUgZIJyNF8cL-WczIuni_bed3YtYYn8I0faHZXAYIB5Itl9HCj7sla-40tU1smsB4EoceBAJdiUT7n0hU4wpr76DU-ww5lj1xW4lewBU-O0kSkOzova4cgtZM2BmpkwmthP7V6W3hlg5RfNxcRdi_OZZnEZOAGmxGrGNbtZL4Whl5PeJdseh0SJ7LLp8Xx-91OXWjTKpMYxMM3jHdcITh46dag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=GDcQFqn1otWgb4ebWERHyluMdZU0DRwE7t84cSU6cdDfqxuvCBTZybj9wwlMdS3evfQ_Ljxzk9Fj0pM0tdW0viE_hrun722JzOPZ7EsgZFBCCSzvrJ_bwHqCSpygqUgZIJyNF8cL-WczIuni_bed3YtYYn8I0faHZXAYIB5Itl9HCj7sla-40tU1smsB4EoceBAJdiUT7n0hU4wpr76DU-ww5lj1xW4lewBU-O0kSkOzova4cgtZM2BmpkwmthP7V6W3hlg5RfNxcRdi_OZZnEZOAGmxGrGNbtZL4Whl5PeJdseh0SJ7LLp8Xx-91OXWjTKpMYxMM3jHdcITh46dag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mqIpiuXNRjMDoVD7hJGp8VVcqYb2HAcwoOFW3i6hn1uO_tsCqCXcKqeeyPYbnwYGo0MhiidOqi1HZnWUG-p_EgWPlzkQpalvuHCEgKP1deD4ev1jCaL8FU95MtCSdNU0PsVTaA9RjYzMKHWq76OvbVm0Djqc_9WEJTEhqyJdAC6qtuuGq_ZcTNgACw14aBAxS9yw1f7wY4SFmL-FasDcmEERVBqd77e7QriNgpn2RdetTJrtfu43x8xoZmD6Jv5MbFz9JmTTByhpQfiA3xCSprufyMUisvSruyQRSj7r9ijSOvhqe7wF4X2Fz6Av9tnjOcym2Zd3BxorN6BisAgfqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=mqIpiuXNRjMDoVD7hJGp8VVcqYb2HAcwoOFW3i6hn1uO_tsCqCXcKqeeyPYbnwYGo0MhiidOqi1HZnWUG-p_EgWPlzkQpalvuHCEgKP1deD4ev1jCaL8FU95MtCSdNU0PsVTaA9RjYzMKHWq76OvbVm0Djqc_9WEJTEhqyJdAC6qtuuGq_ZcTNgACw14aBAxS9yw1f7wY4SFmL-FasDcmEERVBqd77e7QriNgpn2RdetTJrtfu43x8xoZmD6Jv5MbFz9JmTTByhpQfiA3xCSprufyMUisvSruyQRSj7r9ijSOvhqe7wF4X2Fz6Av9tnjOcym2Zd3BxorN6BisAgfqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=O_wppjAktuJM1Co0VZHPx2pQRJVQIk1n_VuhlNsQXCW4nhqU_rNDvwiaprQMCFErhp-euaJw9bWAZfwQCldz4NjVYSnDFlE3mgTOKFa1FCAxATIHnyG_EHX_oTKAc1WgblVfRJJCq8XshFC57aCKs06VuS5kaz6_PlYBNaJDSbmMFdY-ajyT2tIQM73F4W4e0RT-oCsw6wLcmdBasrGpPey6EdrI6B3tGA_sbN5VriqQJ09wZqu7bIFgIvayOzm4eZTj-kv_HGKOFZ1vjToT30vQJbf8P7GMOMr4jfShJXmlH086zPPcUHhFnrydq-vIIxCQ7zehvE_qOUThY9ImIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=O_wppjAktuJM1Co0VZHPx2pQRJVQIk1n_VuhlNsQXCW4nhqU_rNDvwiaprQMCFErhp-euaJw9bWAZfwQCldz4NjVYSnDFlE3mgTOKFa1FCAxATIHnyG_EHX_oTKAc1WgblVfRJJCq8XshFC57aCKs06VuS5kaz6_PlYBNaJDSbmMFdY-ajyT2tIQM73F4W4e0RT-oCsw6wLcmdBasrGpPey6EdrI6B3tGA_sbN5VriqQJ09wZqu7bIFgIvayOzm4eZTj-kv_HGKOFZ1vjToT30vQJbf8P7GMOMr4jfShJXmlH086zPPcUHhFnrydq-vIIxCQ7zehvE_qOUThY9ImIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEpLDzvryhlb-9zeNqAQIdurxVgUf6xhUeE-LxvTlmJPXY0mvuD1-XGoas7am1mHiXbj__4JjVz3ifmNBTRoVMwjgKANT5i4cdaYRqqzn4wImWZbdUyzXHloILRmMrA6l280LtCySMAV5ZB_TgcRZYnYEsQhaai23VIqPSkm4GlowwrlB1dfKtarqmZzVsIyTRNBUVmfOkne2sCHhXymJKtPfTICSV3NGxWhmgJXjYVOxlxB09HwT5EZ5PJz1wVr6OrUHnb5Rl3xgvzkttXviG9z_b6zMAKFpOHGtE0soE00FtI7het3lxsE8oadfYflQFGOoS4o_jVvrMu9ur4Zjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=WMTiFTg_OSvuHjUHSS9VCmcEhP6Jx5-43L3ljAfZactEHQ6Hihv4G0Gq1OyEpKbN89jzqAZ-7Y_MzZ995Cw_hOybuVw67jhGrUahHLaNd80cFavuUa2NkysKoGFOfpplc6UfzT_Ir8NxvBknmlFejGEQT7PPxNDQzkzifEW7jMArnTsU3ifsPSOpSzw1UFz79jctZNxqWLVLCAr3Br1tsp9xqxnqkgI_AdE5HSoKm7e_k04wNLpwoTBn0ODXW0eGQ5qQbt04lFC_23kV1dnHSuB20zma3x_eF-9aHJKJcABNHPhKEx3Xaw2SfwAeokwMZcvBeiCrkQSRsz8hmh1Q2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=WMTiFTg_OSvuHjUHSS9VCmcEhP6Jx5-43L3ljAfZactEHQ6Hihv4G0Gq1OyEpKbN89jzqAZ-7Y_MzZ995Cw_hOybuVw67jhGrUahHLaNd80cFavuUa2NkysKoGFOfpplc6UfzT_Ir8NxvBknmlFejGEQT7PPxNDQzkzifEW7jMArnTsU3ifsPSOpSzw1UFz79jctZNxqWLVLCAr3Br1tsp9xqxnqkgI_AdE5HSoKm7e_k04wNLpwoTBn0ODXW0eGQ5qQbt04lFC_23kV1dnHSuB20zma3x_eF-9aHJKJcABNHPhKEx3Xaw2SfwAeokwMZcvBeiCrkQSRsz8hmh1Q2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=X6wTZpKdxQ-5f1R0AL_60aK_vuebXxsb6dmeMEQCEdr53ZCi2gU6Hp_6cKZzCKwEMIWnjhJ4pwE9Vs5kyluZOeyBK2u5EOyxd-UAlkbB2w6g6wocpRllYN9ay8lJItA_eqBSLB9mQJoyik8jDW3PsBe0jbgrj2X6wXCq8sAfY5kbhPauKCNgHHFQzGMA5CFEZOlnhBXBPWKleA85EuYK7EuD5OJo7K-_7SNlb2Y-Oo7OBG7l7HL0j2H3o4ik8zuiMb_67gM-u_KS3JQTybriFZ8EP4e94MEHqS8A4lxM7Sb1GpDA-8Ie_jDFs03p9jdO0N8h2PktTD0OpeXMM0RWnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=X6wTZpKdxQ-5f1R0AL_60aK_vuebXxsb6dmeMEQCEdr53ZCi2gU6Hp_6cKZzCKwEMIWnjhJ4pwE9Vs5kyluZOeyBK2u5EOyxd-UAlkbB2w6g6wocpRllYN9ay8lJItA_eqBSLB9mQJoyik8jDW3PsBe0jbgrj2X6wXCq8sAfY5kbhPauKCNgHHFQzGMA5CFEZOlnhBXBPWKleA85EuYK7EuD5OJo7K-_7SNlb2Y-Oo7OBG7l7HL0j2H3o4ik8zuiMb_67gM-u_KS3JQTybriFZ8EP4e94MEHqS8A4lxM7Sb1GpDA-8Ie_jDFs03p9jdO0N8h2PktTD0OpeXMM0RWnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Q-D9jU4HZ7drFRXXrL0X02gBaJpafk8Yae8D3E1mv0rWXeWpDhpDPgSZRyeKT9e46hX-9UH8C8xetVEkc-dosozik_W_zXfmnWQH0DVNgJJ_LdxE_lf9MU6oqYewNJ3C8FVvk3CSMIplzZTiwu5tYSBfp6qQu47juq_708OlFNlYcvRK5jNCx5ONmdyFTfu-ONHRNxUY_YO8tzk0YBRKCKWlgNg9gZRq8R4EjVXN7aqyj6U7d6fDVs1d5cdsD3X6IjPLodt_h6EaynAwU8Bg2Su1ilwVCWS-HXbZ2PRWQxdt3XqJv0W9kL4JQu3O1no9Lamx_HhrgkAqojN0eA5DmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Q-D9jU4HZ7drFRXXrL0X02gBaJpafk8Yae8D3E1mv0rWXeWpDhpDPgSZRyeKT9e46hX-9UH8C8xetVEkc-dosozik_W_zXfmnWQH0DVNgJJ_LdxE_lf9MU6oqYewNJ3C8FVvk3CSMIplzZTiwu5tYSBfp6qQu47juq_708OlFNlYcvRK5jNCx5ONmdyFTfu-ONHRNxUY_YO8tzk0YBRKCKWlgNg9gZRq8R4EjVXN7aqyj6U7d6fDVs1d5cdsD3X6IjPLodt_h6EaynAwU8Bg2Su1ilwVCWS-HXbZ2PRWQxdt3XqJv0W9kL4JQu3O1no9Lamx_HhrgkAqojN0eA5DmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Eia8FGfqEyguLaYau31cwswCdowVy9BDqoYLYSEZCTVnhPw3-U76txJSK0oipOG4VvOzW9jLOquiIBtGzZmwyQzuKRkL3mzq98DkcwERnGj-WCy6Vj-g71uXM4od1QJib0MyXkt1cl8kPKbcC76x01OFsIpARmPwzltfSwy8Ik4iVdP1M_q7Pq2WhhebEphUkvMuhR-Ojiiibxg_vM5aQDT49tz-fxwwKK8vo9lCZU73GOYWgWBmhgqV-irZy_yzISBe17Udlg-9QOhQn4yy9AJqhN0_oNmqooAFvp58HmpuE5qIriIAC_m7o3Og7NRGIibHxobjWZljaEf-ZnFrvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=Eia8FGfqEyguLaYau31cwswCdowVy9BDqoYLYSEZCTVnhPw3-U76txJSK0oipOG4VvOzW9jLOquiIBtGzZmwyQzuKRkL3mzq98DkcwERnGj-WCy6Vj-g71uXM4od1QJib0MyXkt1cl8kPKbcC76x01OFsIpARmPwzltfSwy8Ik4iVdP1M_q7Pq2WhhebEphUkvMuhR-Ojiiibxg_vM5aQDT49tz-fxwwKK8vo9lCZU73GOYWgWBmhgqV-irZy_yzISBe17Udlg-9QOhQn4yy9AJqhN0_oNmqooAFvp58HmpuE5qIriIAC_m7o3Og7NRGIibHxobjWZljaEf-ZnFrvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rBfl91K-R3yYMaRwnubZEHqbbeHmkqNxeWninbXiJCWzUKxfELIYahnnW5Bs7zsS6TOqCkRv0AJJ4tI5BIp6ge9YBlnktTOwkewMF0IUvYH1WiDPotxwVb2gzkE9-PcLq3ueiiKnReVHaghM73qFBdEXoeewf2Gp9dBnbCbWVhRtT8XF229R8n6DwD0TvJUasS3sM0r3eUx_VMj-1qa0nJPmWEjh4JieyRA2e566ov2n7OGbRdd2aEWj4T4w0xguqQrvGfi9C-QBlfew0dVWzf9RXYqz0OK7gp9z6XtR6qjVLug3HaVKYog-CRWsjqRS-LtwvO17RAogWA1uYYg2gA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=jYdD8utReopGWiEdMDsIL4MxUL2VRZvf94tqL5wgo9kmBLx8UZJ3naKCdKvzedpMsxqAj2CV6UzPcI6GmBx3PsddtSw0OeQoaLJ3dgj64y2CnRgclJ8QkCtxeFhDqAFgjBwioc-wpnDEr1MNcc0sIqocncgXlyhPv0y77CGu7vZGxVOpghHIgc8A44yREBWKTnNmD-E8xygluAkHgGBZajd-AvokHElP5NraWofpMdVd3JqeHHtKwL12NO4ZeNLszy0ckcgN6snXVR0D9gDqW6mLEynoL9GRLibTZ-wHlRby0tWKgMweHaqU6YVQ0F1IAeN1pwmGRu4DHJ0yE99KFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=jYdD8utReopGWiEdMDsIL4MxUL2VRZvf94tqL5wgo9kmBLx8UZJ3naKCdKvzedpMsxqAj2CV6UzPcI6GmBx3PsddtSw0OeQoaLJ3dgj64y2CnRgclJ8QkCtxeFhDqAFgjBwioc-wpnDEr1MNcc0sIqocncgXlyhPv0y77CGu7vZGxVOpghHIgc8A44yREBWKTnNmD-E8xygluAkHgGBZajd-AvokHElP5NraWofpMdVd3JqeHHtKwL12NO4ZeNLszy0ckcgN6snXVR0D9gDqW6mLEynoL9GRLibTZ-wHlRby0tWKgMweHaqU6YVQ0F1IAeN1pwmGRu4DHJ0yE99KFzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=gH57fXCxR2UB-ffz6hZNLnB9ifmPzjUfURqlPCS17CVjZWo1KM5bBCqpWA9S5REvhSpGdnoIAJuCe-bFaClWTz-8msxYxs5eizRfw7C8ZgQt78MpM0yubeq8G1UWV-vdpezpy15L7OOW3CguwMGVndI_f_2uSpByDxRalF5oEelt0XvAZIUuDWQgh6lbVk8y7ScyOw5Muz_QbddIzBzwJy9EFr4DHaHWOO26Jwfc_cjq0l3jMhGSxOcj_oJ4zno4Kw7khhI5_JmTgEkF1lA4RqcvJiXG5cUNZpooraroNr3f_1zQa4OGEPornQEZvAGYm-Nf7xQCT_V4wF3V-7MuXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=gH57fXCxR2UB-ffz6hZNLnB9ifmPzjUfURqlPCS17CVjZWo1KM5bBCqpWA9S5REvhSpGdnoIAJuCe-bFaClWTz-8msxYxs5eizRfw7C8ZgQt78MpM0yubeq8G1UWV-vdpezpy15L7OOW3CguwMGVndI_f_2uSpByDxRalF5oEelt0XvAZIUuDWQgh6lbVk8y7ScyOw5Muz_QbddIzBzwJy9EFr4DHaHWOO26Jwfc_cjq0l3jMhGSxOcj_oJ4zno4Kw7khhI5_JmTgEkF1lA4RqcvJiXG5cUNZpooraroNr3f_1zQa4OGEPornQEZvAGYm-Nf7xQCT_V4wF3V-7MuXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IQCstQPfNSkSOcmCRKWcGHJSjFefE02trMeshDp4qnJToX4L9BTDQuvYzQEUm1iahzwaXSHGy6y7x-RxiCsDrcZ03KoahQ9yKWANL_BhSwzZUSnJ3TCks177UsfTbXExJG6qWhNSNkQG9ZaMd1eQcE_8hcVY-yrk28GjkPNSIwVUi1aRr7x7aaKAYVaz6W8zg4uRiog2qBJ6kUQavBkIsxMQqJm7r6Evdv1TR9M_YI-GN4hWSTbz1ep6dG81JFuw9WmvhxS4afaofyI-QiSsaJFVXotiDV1oTbPV54zF2K9S8uwLWNTGRfWdi4i-A63OXgQVO4bXg_GUA4sK8BLPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DrX2nSoNishVhDTzs71bHPL_zhhRUspezlZydoWDGbD_e9_nw_BqMZvg2uC9yz0xl05Hd5CDbFNyHWi04gid-EXMfKxTmKSyuqZTDRM7PQO9Qa4P7UauoCeWbdaR-ufSn3nOTgZ-JqFGA4wOETaB5k1dH4tK7w8BmgPuefjjJ88x443fvJ9cR4PpYu_-QXwRq9_QsLxvNez1Z8p4oiYfDZ2oAOsHNoBic7HMs1ESx8kyesVblOFkzMGFwaiIpVaSC-wdJ_KG_DimCEXT0NzNwEoXOKZQwocrwWpv7jc__JZvZVO_tWs46F_u1rVLowOuEzdEXXsI85bDDvrrCPPo5A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=WPrXcVe2FsPJvgs4GO_Kb6oZ2OSLZzdIOeXB1OSRt0iF2ANLiMcKB-QKiIj3GL33OVB2d5nbvauFhAllS20ZNF7RaW-VdOBKxpiHAWhC9V9TuGArpKzXhyb1h-5SRlOy0OWJZdoR4OOQzJkiuj_HL_CuK3bScmOObMrMRD5IWnET3apMSRxAWgZftWTdteMpSRKNxyEdMbKEDp4vzuodyKzWCjKycEJqUEn4X-6IDlDW5kiTJDrPuZXqgJ9vbxei5er1t_t575S2PPNarJL_pqQoAa6WaRK4R8s0YSfstvcypgIHCtGh9SsnhfQj6WPoRiJk_iIO3dY85_f9n-Tlnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=WPrXcVe2FsPJvgs4GO_Kb6oZ2OSLZzdIOeXB1OSRt0iF2ANLiMcKB-QKiIj3GL33OVB2d5nbvauFhAllS20ZNF7RaW-VdOBKxpiHAWhC9V9TuGArpKzXhyb1h-5SRlOy0OWJZdoR4OOQzJkiuj_HL_CuK3bScmOObMrMRD5IWnET3apMSRxAWgZftWTdteMpSRKNxyEdMbKEDp4vzuodyKzWCjKycEJqUEn4X-6IDlDW5kiTJDrPuZXqgJ9vbxei5er1t_t575S2PPNarJL_pqQoAa6WaRK4R8s0YSfstvcypgIHCtGh9SsnhfQj6WPoRiJk_iIO3dY85_f9n-Tlnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IK7mVKkdENm63mHJ45FVFWRH9cLlNcu8i4-wht9e-7MJbjatKb6Jky3sof59vhSfdJZ4KUSr-s-le6ETUGWIvYWfAnxf5UIcxhNh8zK9R-oc5YZ7XgE7y-rts0i_icUZoWu8wpmvTwhOE9P7kJuuean_fT8GP3y0d-UUFP09DW1bW_BZcFNTr2SgNvnt8Hotv4U75Qu5eKpYksreD_iZG2PSgGxqthPW8iMBOD-A-MnuO-1IiLnWP7CbFVP1VEkKHuVeX3t1KKJGBUsRCg3Gg4VF3mlxpqcl3G8YQfADhJUBYqK5lCSV48vmBYiTU9gSEyAaQADeONYuz8IDn0PEqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L3FEJ5NlxA-vdotueGlhZAlxafqTXqOvjOVGn_Lr3HevhUn_wug8oEhDHLfWvjtQzQmKE8CmzB_QunJ6eNnNNmA_gQC8hf7ZBJ4I9n1t6JeDcw9B5Q0P6wek8dC_kFE7_IPOPaqGH7N4Nxjp_RoCfsonm_rpJ1BUa-XxFXlweC3yprW-P-9WIFKzqT4FK0vFl4d19ZucqijXuUvfBH42gM2P1gH_FMSb9ZlF01uIxmYVVa-FBFaVnK5Go2VtUPQmi1nt2fbWG2zbQnjcoL__MkcVLOPdXAj6IxbcoWzdRPbv47DgCklcC7GFvleJbj9f_EFoULFPNQ1XcR79Ue8Yzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kMV552vuvouI8TkdjgO8Rq4VhAZ9q85TBnbTGoYGtMTSU2HA8e8VWZuwvdmg3x6V8idr4PerPBgdoMmZ7VXyErf9sqHDC75Qbkm7cyNkECU-JsNBwTGxIixb2c3_X84Kjily1PX5bSiWG-7PYJgmMz_dAiRGr1fhtwii_9h_Dp-UNNE8cgVmvq0k3omGgaOgsyXzI_Fy68dOw18q0HYEPa5C5pVRkYDBggeSsn5JWAicL5kkG7DWNe6xEIuhcHwI0jzvobmFh2n9iYnIeWubkKZSi1rSEJBh551e__zlV1YZUJsFKKfyVrrc47rD_1RDXcRLANjw8tmUYC0cmvJwNg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MypKpfzEfmbc3qfaeUN7PV4_1uuHlqgRggsNQznGd9PvvK9uJ27_3qhzB9ewWhE5EMVwdTGLWsZRtid9n-wfDu4lQyMQSI9l2PxnDroSaoo9njfS5SCBVggiMe5CCLcv7wW85Oi-O5B3w4WMia30Rh-ssnsO8PPQOeCL48vld0EL15ZhMrjGo974-v2_-AN3EIr6GLMC_GEotSEWNdYc_FEfCJC0zDZ2b_ogH3sjJ6lwdFz0YEAz7tTNm0q-LFy89shMiTgNf0JTd1zfOJO17gj2pau6Ee9elC9BD6_MezM93H9GMdMPy6AeLFQduh_PJe4NFkiXGk0eikWXvefTug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=MypKpfzEfmbc3qfaeUN7PV4_1uuHlqgRggsNQznGd9PvvK9uJ27_3qhzB9ewWhE5EMVwdTGLWsZRtid9n-wfDu4lQyMQSI9l2PxnDroSaoo9njfS5SCBVggiMe5CCLcv7wW85Oi-O5B3w4WMia30Rh-ssnsO8PPQOeCL48vld0EL15ZhMrjGo974-v2_-AN3EIr6GLMC_GEotSEWNdYc_FEfCJC0zDZ2b_ogH3sjJ6lwdFz0YEAz7tTNm0q-LFy89shMiTgNf0JTd1zfOJO17gj2pau6Ee9elC9BD6_MezM93H9GMdMPy6AeLFQduh_PJe4NFkiXGk0eikWXvefTug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=YC8mPKOm0Ox56WqlVU9JW0NUuPIEUzX3RLSKozQJ0Imhay6JEsIAf6loWA3Vv7Gz63dj8V2kwfaY7bWxrFTu0Lx6nOXYZV6nVzsfbrYzatB-pqfDOzk2HO-A0j1H0DzqkvAHFukOFcRr3o6vetHiiw8e5E_kO5dkP_qhtHO0IwQEISw6QMySilL8R65Bj6hFmA5VJkFTa5_vbNF5btM71Rj8c7ZygAbPLqxzUyZOUgLjctiLnOXgij7vSlF_ozXV2-9tXU48g2WpLvBdV2GlQotvIL5b7ZavRMUco0HAKdNYMWsyGij4FKpyCABPSFUQlXLDEHTfq1EzLmaHkg4mUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=YC8mPKOm0Ox56WqlVU9JW0NUuPIEUzX3RLSKozQJ0Imhay6JEsIAf6loWA3Vv7Gz63dj8V2kwfaY7bWxrFTu0Lx6nOXYZV6nVzsfbrYzatB-pqfDOzk2HO-A0j1H0DzqkvAHFukOFcRr3o6vetHiiw8e5E_kO5dkP_qhtHO0IwQEISw6QMySilL8R65Bj6hFmA5VJkFTa5_vbNF5btM71Rj8c7ZygAbPLqxzUyZOUgLjctiLnOXgij7vSlF_ozXV2-9tXU48g2WpLvBdV2GlQotvIL5b7ZavRMUco0HAKdNYMWsyGij4FKpyCABPSFUQlXLDEHTfq1EzLmaHkg4mUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JJ6MsN-uzLg-Dz9FRTgtzWBFA91jsi-84xob1so8SEKTh2l8stqRhtVQA845DpJCLpfD7NNp1ck9Jbbsn4omvbw4GRLTpJ0yIl2-9QMGt92HacAfvk3_6HaQtOoBAdIJzDzp91eLl3v568Jgb7q7zm653dy3t3ONrI2Eeohy6EFMVe__Sb9vFVUlElx1zGmNvB3RHZ1nPmyP702Dnd6CQLWYUnn4L8wUmhW-qBO_3nQrABVZpp9RELecb_ChYm71NmarnsSSzGQHuwUHa8NQE410Av1ONCFF07URbLaPW79R3vfglXRcN7yUD5Mbv7PO1nIdliOlvfSSF7YBknQHOJtf1TCs2cpTfEwOLRex6KGGc3L4F_7dwolyilE8wBd4UARZCJr7PPUmiLWntrwOV-V5xs8k522Rx_TL3ds-9nluax9FsUj7pMreeA5IN5zDetHYKhaHanpJHQx9YUcNCLjUYQffBoejoFThfSR1Wk5Jq8EXVTyIxzvAiQal8h30KBgiwqhnnLY1RrdjfP-CZHHoXr8sWg_nhZKS8b9vU5EuGLCHYjnUhmCCgHrf7KwlpXAeDFAZy3bysjb8A7M7vaCskDSg9Jbpd2ZQf_Efns6L8RNt6cUI3wQ8lklup8xKPI0a6vsOYFElzLXeEEB5gwkKbX-K-gVjnFva5aRyQV8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=JJ6MsN-uzLg-Dz9FRTgtzWBFA91jsi-84xob1so8SEKTh2l8stqRhtVQA845DpJCLpfD7NNp1ck9Jbbsn4omvbw4GRLTpJ0yIl2-9QMGt92HacAfvk3_6HaQtOoBAdIJzDzp91eLl3v568Jgb7q7zm653dy3t3ONrI2Eeohy6EFMVe__Sb9vFVUlElx1zGmNvB3RHZ1nPmyP702Dnd6CQLWYUnn4L8wUmhW-qBO_3nQrABVZpp9RELecb_ChYm71NmarnsSSzGQHuwUHa8NQE410Av1ONCFF07URbLaPW79R3vfglXRcN7yUD5Mbv7PO1nIdliOlvfSSF7YBknQHOJtf1TCs2cpTfEwOLRex6KGGc3L4F_7dwolyilE8wBd4UARZCJr7PPUmiLWntrwOV-V5xs8k522Rx_TL3ds-9nluax9FsUj7pMreeA5IN5zDetHYKhaHanpJHQx9YUcNCLjUYQffBoejoFThfSR1Wk5Jq8EXVTyIxzvAiQal8h30KBgiwqhnnLY1RrdjfP-CZHHoXr8sWg_nhZKS8b9vU5EuGLCHYjnUhmCCgHrf7KwlpXAeDFAZy3bysjb8A7M7vaCskDSg9Jbpd2ZQf_Efns6L8RNt6cUI3wQ8lklup8xKPI0a6vsOYFElzLXeEEB5gwkKbX-K-gVjnFva5aRyQV8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ZqNMhbC7-xZOwhlhGU8jmUai-17gPmMVT_eFUiGzImUVPvV89OQs2fxhjvqrw06F-tEeUH2CNH6ifx1mXfT3Oxn12XZeagNEFx6f8x_DPk6t6XKKIlTMOG6HR5yBudg7gTMT3PRLLtddxk8ML0S7CotpHvnoXRzjX2M-blJKR42AFuA492siMmpnOul3QL6uqSmG5Z8OLz8fnc-QBo9YSA22cQKc5KVkYtmTA1nPh25UDVq9bsNFNCSoV3Q5jP8IqiMcJ2ujfCcwUdLoqgOiMfVTd4hLqgmTBFlYOWDhQnqolAggy_JCFwe4feDBEVQbTUxA6ykBBNf-5wXYX73_ABUH31zSGrymCr8lcYz0wNXtBobZuz2Ao6poEUfnj2CVNg6A9Vb8wWRf4mzxW1iK0XFMJZPGxRbXKa6iJmRr1ynKy0x_xZLA45d-wHe_17kyjhl7wAg1pC3fMtlC2j_Ndnu8BOcUZFIJJajn4lMblv47haVfWVbAMJ-27TPfGRsGH46UAByHk4V45CXq8QToJLU_yIj7o7CxEq8H54eDR12xxC4hY0ycmehwvrCnRlQs-43cihR-XXhzdvSOcFninkJgOD478iZMZWUqTeT_YnsS5SC7GmQgpqIO9Md4Xk3sdzSa3lKkKatVrghmzcnwforDHm_MWw7_3med3kA37IY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=ZqNMhbC7-xZOwhlhGU8jmUai-17gPmMVT_eFUiGzImUVPvV89OQs2fxhjvqrw06F-tEeUH2CNH6ifx1mXfT3Oxn12XZeagNEFx6f8x_DPk6t6XKKIlTMOG6HR5yBudg7gTMT3PRLLtddxk8ML0S7CotpHvnoXRzjX2M-blJKR42AFuA492siMmpnOul3QL6uqSmG5Z8OLz8fnc-QBo9YSA22cQKc5KVkYtmTA1nPh25UDVq9bsNFNCSoV3Q5jP8IqiMcJ2ujfCcwUdLoqgOiMfVTd4hLqgmTBFlYOWDhQnqolAggy_JCFwe4feDBEVQbTUxA6ykBBNf-5wXYX73_ABUH31zSGrymCr8lcYz0wNXtBobZuz2Ao6poEUfnj2CVNg6A9Vb8wWRf4mzxW1iK0XFMJZPGxRbXKa6iJmRr1ynKy0x_xZLA45d-wHe_17kyjhl7wAg1pC3fMtlC2j_Ndnu8BOcUZFIJJajn4lMblv47haVfWVbAMJ-27TPfGRsGH46UAByHk4V45CXq8QToJLU_yIj7o7CxEq8H54eDR12xxC4hY0ycmehwvrCnRlQs-43cihR-XXhzdvSOcFninkJgOD478iZMZWUqTeT_YnsS5SC7GmQgpqIO9Md4Xk3sdzSa3lKkKatVrghmzcnwforDHm_MWw7_3med3kA37IY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=el2NgsPxrYkmjbw7sja0IiKU0S-rrGm80hnVikNF-Wg4n1Bbyc2YqnO15fdNZH57hBtozc_uARImAggC1EymS5dtJ51WHLtaDDDBFudLomgbSI9sckQiW3xd2THWI6qX04jCnPWrc2AvcTxOZgzOS1Fno3Qu6Db2R7rHVHp885Al_ncbd0BWqth2hx6zb3aVvcLynP482uQsbeARIpkXYerBcQ4U-V0NdR0COoUj-sLuYyWRxY4w83aY26lH4KDhh-kRXZBse_n3cJvOBPjQyNC5BYs-3jvvs0EJBb3it4qt0FiSdH7w-2hFxJ8-sHw0Kiam5MaFg60arvl6r4v1wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=el2NgsPxrYkmjbw7sja0IiKU0S-rrGm80hnVikNF-Wg4n1Bbyc2YqnO15fdNZH57hBtozc_uARImAggC1EymS5dtJ51WHLtaDDDBFudLomgbSI9sckQiW3xd2THWI6qX04jCnPWrc2AvcTxOZgzOS1Fno3Qu6Db2R7rHVHp885Al_ncbd0BWqth2hx6zb3aVvcLynP482uQsbeARIpkXYerBcQ4U-V0NdR0COoUj-sLuYyWRxY4w83aY26lH4KDhh-kRXZBse_n3cJvOBPjQyNC5BYs-3jvvs0EJBb3it4qt0FiSdH7w-2hFxJ8-sHw0Kiam5MaFg60arvl6r4v1wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRnqhEhja7AlsrBtxG-dTQXkr3ySOTX2o9ZtuoVpvWLNOyEFbKuz2fRrihNqCwtmH8Sy-61BcenBSsJb-j_vkB6MUV39aqy7l70NExBLeNbsiibsMRpcNjEEeDpqvBmcjeBJ6YoTHSrZFa37iDvUik18uhsVPgRXBe4RnQ_weJf4Wl1t6r8ZYYnQq6-VoqfcXADW1_abQ091lghfKrvl9BvxWviopPA9UOqur18BxL8gygJygQYE6D4KUCNhbkSzFNAzmvg0yktvdIoOylvR60091SMakQvTd0DpI_8QhHUPql2kSKH8lne65d_amgytY8IdmQ32kxuU3BcIg2hxhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=J0Jd3RPQM0M90T5qyIYeqGnfW87HngKS-IhhFv_vOdA3cmCJAu3BvhTQ-SGbdFNsu_xvw_rR6Y-1aYSZB6p2YzOGEKZy0A_1aj-VOulSKAGrnBLZ3DYjgRKjN0Uy1Oe7v8IbzZGoAfDEpTrNE2dsJfqh98tUHVcPLtjLmCx-FkZEIZO4DnyPqQoRhSBcqePffnhM51RS6nVuq_DU0HGa9BaJIp60BtPdXqYDcSbu4-bU15SVMO0EbWJlErCJfQu_ucJksbrx-tHWVhUfLU0uf6vAvNAK4rZvzRWXCr_cBe1RTFYWyzKisobKR2Q9IwRj7a-sbiSVA3r0lSHL3ZeunQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=J0Jd3RPQM0M90T5qyIYeqGnfW87HngKS-IhhFv_vOdA3cmCJAu3BvhTQ-SGbdFNsu_xvw_rR6Y-1aYSZB6p2YzOGEKZy0A_1aj-VOulSKAGrnBLZ3DYjgRKjN0Uy1Oe7v8IbzZGoAfDEpTrNE2dsJfqh98tUHVcPLtjLmCx-FkZEIZO4DnyPqQoRhSBcqePffnhM51RS6nVuq_DU0HGa9BaJIp60BtPdXqYDcSbu4-bU15SVMO0EbWJlErCJfQu_ucJksbrx-tHWVhUfLU0uf6vAvNAK4rZvzRWXCr_cBe1RTFYWyzKisobKR2Q9IwRj7a-sbiSVA3r0lSHL3ZeunQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=HI0O2QnBYhpdQ4Z2TGkV3d60mAmYxggAefohhBhdJCuNM2_NACqwhtsXvHzkG3E_bV6On29HLiFU2GNkAayMiN2lHELUSq78ZcifNINw2F7OD5OwLCbB90uUB_bWyTzluNwGqxCXEPsf78RlJnrSyUsqxL0eYbIG5fXeGSvJV8mBGh5uM4MHboah3avngEvscNfBLcrVcpBEu-k7DKMYrTSBZN_dtaTbHZeDiCuUYo9MWkb9l2awGluzWESCl0fBwJt0TRPuVl8g15QylUhuLXYY_yCM_jWMHtCJ2GlaZ3tut9NIvJ5z12D4W1Fc5fq6xnQKAWCqUY3Oji4KZGXxbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=HI0O2QnBYhpdQ4Z2TGkV3d60mAmYxggAefohhBhdJCuNM2_NACqwhtsXvHzkG3E_bV6On29HLiFU2GNkAayMiN2lHELUSq78ZcifNINw2F7OD5OwLCbB90uUB_bWyTzluNwGqxCXEPsf78RlJnrSyUsqxL0eYbIG5fXeGSvJV8mBGh5uM4MHboah3avngEvscNfBLcrVcpBEu-k7DKMYrTSBZN_dtaTbHZeDiCuUYo9MWkb9l2awGluzWESCl0fBwJt0TRPuVl8g15QylUhuLXYY_yCM_jWMHtCJ2GlaZ3tut9NIvJ5z12D4W1Fc5fq6xnQKAWCqUY3Oji4KZGXxbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXAna6hFGuUxmPEdHUakilV9uLuLRaNtScOvETT1XKLsr1kSAwP0MrHscHrysQFhQgfOpKJPaI5N9m2Wj9mzNkFsZS626Lh5wF9R-QspiqBzXLXli0u_eDWE1yEZSanpG7x5zsl9cOLvBC3FvE8AU6ZKOgya67RRr4iWnlE2IJT9puMoWB-78FlqFy0VYxmMxaQT8xamT4_2LyXnn4FcOcRu0GRoFuLxHeB0nJbaBDK1u7_Nvc4iC5RsUSHd_TicJeeGDCguHtSN1f6bd00j1MU7pzJVEaJogQLs2UtItSbacNXEGk31pEmryxLYuiB3JqPW4WEHAR5bf8QbHBywTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiMaxKkvSfWU1Pfck4niLOsbE97Slz_Y-7GqkR3n6mcFBf8vfWIKhCMY-lMRQFwTS-mwM0SalcPCTf6smqdqpTi5P8t1zPZFMtwW9DowyDV29tQgtvCGkz9-ONmi3lXi3wsb-aFISjqS1Ddv7hZM5FkwyJ_iWLCU3_GwNessPgUav1NGx_vZEEijzGb8lOr6ZjgjOEH-QkWbvuFeO7Rm9ENRXkLieN0EMxZCo191v3-3TqEIVUzApBBvjpC66Y4QSqwPl1_dMRo9TVKLWCYQ_yEEsQAJI-pRcg2DiicK55jrWKnk-0tnxuic_W7vkloyJJKE678Qe54WIRNLMG32Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gki6My8Tud8WExSHnP-PPHYmqJtY1IU9vc69BTEV0uNotHIw9sd1bDt2h74YaBLV0i28httabJpG0my9eDY1yXee7N8t2HPrUbVhSWg1lMnGzbBpHNZIQ2Jhp_gIMADtj1A0kj0AaPg91VzexMKciDM-QUvDgI-CoCDT0RMajdvCmMSECcnzbF9caZStKC9tNE8QalZnD6cAS0nNv_v-slEUkkjhZLECLcfWbBXlOVkc1refJQK8UMV-2OjN4gqiA3akabOj5AGMToHuvXnahmZwy68lFuJ61xsO7wPo2gHTtRTNnsD9I35sB3ZeXPNbmdEdqYmPjmXJC-9_-ElC4A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MLzVuV0yfvvhdraqgO2sgXQ75N8-dYJtOqxgsxM_Y7msHcnIQHume5oZewIIN2tQKrbtmwfC9K98OBzb12YdCGalGfIudq8rmpJAf8r_-LMXapLjTruo9y7RInwG0LOgivWWuIpsbv3D1mwr3FILSDE-tReaYZXQKmj6OpG7fDRpCfJnjFUJ5DxJBtu0bauRQPPe_BTm6IXN2ZJvf-Jy5MHeSIN36KFCsac4c6awjKul7hJqY2q9Fask_iKz7dwYqgtud8g6YUJVwxnT9I_ezSeihh6OOXWN9wrOzODTUx7dyBp6TJ2qk1qiSxT1shGrl8giraxl7xuHjrh2LQk_Bg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cuheqZ2GEbhE6L6YeQBjeR16N-nk2Pnbkbk7rAqZfRdVFztmmja41i0jkCrfHfWgjLUqV_F4NHpdBxztBPcrxWNXy2BNSeEJVThgVoRhLP75nxt-pGhLvUWmpogp2w1WPolOpWiM0m7BUYw-_qcsJOzKOdqh4mV1NWtkWbY0mi94ciPiacayNTbOyO6off7OzGXw93YM49UmEbiRlPItBCyjocFq1yLqgkW_9SP_40yd8RFwL0a-Q5OyM-Ke1XcmQsNc4TNwp9rq8xeaBGMiPuK17FmRBuUKHmfjwir6E73iSY7RCP304ugQlBNwYF4ARxKzYt72T1E86Vpdxk7Xzg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If0hqAWFGyszPsLacF5Nx0EupdbNy6Qm9y9xF-WElNL-eKijcIqu0Myoqu2Fdia-IUJVgi6M-Tn0fW2y4N_3AM9oFCTXPZY2KnJGcSQs62tVtmJX2gooSsLsKroKhEF735LsZM0JFH1pyRaCgHnmpcvjSRKuQEGmOeSeyn7xtItLNgvVYRIgkJ0wfbFA0n4cbwgG9lQ7iWQfC1vc3Jd_IG2ZbGcBZVaYZkXMisRLv1d_EC4QZgeoL6bM5cz3RyGbzLvbuHTOmjLZoTaJz0My0JBj5wVIwr33mHPrbHIkSP4FCJFaKyufSBbRQruJYEtaFGiXSfeUNVY-1IMHHbn5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EaxwNZEiaBIXbMqhKrykYwqdDbXB7SO8cA2XaebgT7YN2_YBkMqFvFUouU_96Z5uH6TRFFTowWt3KuFTd2gHkjaZ6hLguLz-3-0fAI9tVouiCjEdjB84D-mgaI6397Yo-A2qQF_CmVNUqE8_xXI-WNrExp-KYEgVZaCXXB6Ji4Pyqif8E3aIGRH7Jsz2jWQIv-22bFF12GSfp2EY2RaFj7JXn0YmpUMTManUZACfTLgLwg4f5gn0CZvRs0zt14iIY86HdPIZBlUDN2aDqy5_YT0sPFIhPi6sDfVgB6eG9suiBCdcBrc8mycsIcO9DmX-TSPtMYogJ-IyIeTgD9GbpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCGYMHe1UAYk7NAPDwlGWXFYlSwoIpLh-s26EG0jAPCFJpVncCXLVZdirv_G76rz6XBau4Lakf2-DinpZc_LSUHpTekmvOCAozX1YO5UNT5LD7O4WbCW2XBWxHxFHomWdwmrs1fym0F01ZiY6Q4-cK1ndrcc9q5VTqXQ2uajjj2N1KLYElb4x19qccfd0G4vYbU0t2LlPOlJjJZxE-4BAdGkiIhPlsXgAMbftxc6lA2rymRVD-iKjb4JSlyNrcNyfOwdwpVjk-9kHXCoorJiDYDrGxB9FaPkVO-1dP1oaScKzz0EppArVMM0kTauqPsBqRJZDe27KoSCiEbW6eTh7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kNCwqh7Yt2ArQSDJynEY934peAq8KjKZFJGVxTztwcZhlihaaMAk3VMwbputCzhvp4TnL_qqrrgCe7k8ItgSUPtELt-KqMTQC8d0BnMEhTppP8E_j-uWWcTLNhozoYmX1r886kmBBQtiinbv-2NpyBp88pSlmlf21vwNKcVsT76nHU-LnlAbMD6pPUldUHJFS5Vgm1HxVgxGMYxiwMXVhRczpaim0nzDT_-EeJFaNX_E4qqTzlFGT55_5BBbNr_YzzAcHxP2bh13xPjG9qOOKgJloznfvHoJQgYVTdr-9d-scaGD-Dsx8cO9y1worm4Iel4ljr6hd1SQzAV0QV60Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tGBBoynB5FYU_2cTIVmBTWAopfQE7jkA3WxBIBrn4aniKJbqjnM5lYc1rayqIkuKzfYkIL51YCYrRYRdWgns-qgrinnw75BLmhI_9VxpA7kZB6yIz9n6E07HPbZcktNh2Pr09egNMFrAWQBCohEFEmjvCFDDFwBX8ww97Aw_nqI8pAHh6ZcFVE6EK5KQXD1ueWVL5hpa36ZRFo3zl-f6KxYc0erQdkZIQBQV9tqZ-sXhZzpzVgkCSEYfQug7gSvkvDvebuM1qDju7zrKFu84RZbL31Ct-sc_o9qVdb43MlQEp9KxP_h_LEcrm0xvvsaoALZa29DHaxjW_UWXmItiFQ.jpg" alt="photo" loading="lazy"/></div>
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
