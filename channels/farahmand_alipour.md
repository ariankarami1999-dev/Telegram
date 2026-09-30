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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 00:24:30</div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdmttvCvkjPut4MmtPjCdR6VkrrVjppZZMJGMajbNBT-4TmeKLH09QcInaI0pFOnFPzqKKKIY9WhcLW4isTMkCwYrVn1U00IvwK4ZCNOOahZvkBVbe2II8grqEtohtVAIbA_RJtx96d1_AiCnY9PJC14amv-a-gV_iFIPn3g_su1eXuLgUt5JVpLtK8mDGbBvxBAQR1Eumbzf4VPKw1q-vqPYeyU0rSMT9Lponr_PEQZ1JLFNvqgw0vWmGQSwTjJJqBQ1h4D0etORADB3KfXRUbUEY67VfGKVhnU_cbCTTLWeiZg9osnSsBNe07Wkp0Eun72bRPNti4uL8vjxUQt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RklkcfQFscNLvTRMtxfQDpX7HmsafMqDKZaOfl3bPp-2rEagjGovguMYT_RRgjX923HhxgveBTaPjtkafB54pI0XFnNvILVekEBd6T7bC6_iPFAG0X-N3IQN-8vjtcaMOZ1pC-yUgeodJozJGCxUZE6iq1-Y2sSdqwaliYu1sEXEu2-mFNKQnynOZYujDL5sLol7-JBT9iFUhRFmeHdJ0ROXN1YWLVUD1LjN_zNHWAltrvqyo2OXehiRoYkzguWuOahwbWVYBvrrrQQGoZ4s40BluHBkvrg6vf1-5_LGQ3vwvAS-IyzVdLUEOgAHgxLmv9xBRTxCOUafAetxsjk6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHNpc1P7GHBgG0nR2QHt7CKmyP9kp7vcmaTBoBcitY0Q2eMs_r6h54kueQTGgGl2RdQVJtRGsymQDCqqllc1HMcnYvX8N-j7922cVI8BQnBaAC16In49N_cA1M9QGPHM2ahSWYLdbWbnFDRW_oi-GN_VY-clsUWo-563-8cEO021zePcygMqm7t485lmiI9oWyQ3caQsyC-a6AM5ot1boDYaqmonmgibTgU_RreaqjWy9VVd65R9MjU11UX1LUmkUGYCpDP9iP_QHK8LTkn0giBvwEADwbQvo1nxBE_jW68fatjS8ygovF0syXRga6irbqS4tFSOGZdldJqv0vHUhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRPQv5xDhns-4YvXiy0gr8mJ7MKvVdGzc8IOMEWkaSlQgqXU7aImd1l5XNAWoH2ynQYB4ouWN_p_wOtiPrs2-wCpEnNhDGYHSjYKoTX9j3qWINOzZNJtA9jhxx6sXzsrhzLz7ybjv_ZXgnHQC4ByE_PSLSjfyQyMCBEFC0O-BEotzyFFW2aCeOiB9zJTe2tmii2fk9Bla6ejvjIvYgAYbnb8LA9X4zIp2FsMfKXSnRUS-2q0lr6LqoR_JIaEuec8jIyFC1t6oENLqv_6KdOijultHywpk7OYiNO_kMH78vcMQl7zdyS_8HVZnDKXQg6cdlcolc3s8HX1Xt84O_oWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcxI0EEZ6AhqXI4ueTpVCvQbv4RP0WqZ-_8dWQX8bjy21ErK61Z00-huT-bmiYiBd099FfE88kKK0nyfS9pDG9OWrSm-LjOtzvNNb7ystnl-t-TQWxU3MKkmbQVsrbqMFYtsmsqkNLOowQSyvkt6w9Bs8jv7cyxMM3UQ12WbX9L2n7eH9af8m3BSlSXcd9xh5sKdQCwnciRdSUUCofKbT6rQ5OULzTqwm1p7yXNhx6pfeh4dJDpgIY9oyL5zkzaxUnbArlCMnEaG2K8aEeL0v_HQg5p-zT1ESXJ81yZW3tnuyCVPZ427l0V0V2GxZ-ncW4aKX_yDXz3KjNfaRcnTww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=QTbtSfvc_4NwyZXDBlICwQXDY30uNft7O6Z-4Rt8iklQuLkBsn_WXiFyWC0PPJTPaM10Eu2bV_e7gCT2PW_AlHjgAZeSVlC_4NFlg2w8v-8yDDxGr2mJ2lDNuy0DlsUuvOEddRbXLDasR6u_Z9uuTQxhYSFN7WM_AXVZEHvhlHneMUe1ANg67MURv2bnAYW0hlDip2_GS32irFDgVmnL9iFNfitRfBhdfOMB9__JMp3BG_bfgBR4dL1UBAEqp7Xzgf7kRZlrfUQPIAIlx4_c8l74a8Buyt4HfR8bpEtN1gF9-lRE0MVuyibkYWpm6kILs6CmaeXUx9GVM8t-ly8Luw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=QTbtSfvc_4NwyZXDBlICwQXDY30uNft7O6Z-4Rt8iklQuLkBsn_WXiFyWC0PPJTPaM10Eu2bV_e7gCT2PW_AlHjgAZeSVlC_4NFlg2w8v-8yDDxGr2mJ2lDNuy0DlsUuvOEddRbXLDasR6u_Z9uuTQxhYSFN7WM_AXVZEHvhlHneMUe1ANg67MURv2bnAYW0hlDip2_GS32irFDgVmnL9iFNfitRfBhdfOMB9__JMp3BG_bfgBR4dL1UBAEqp7Xzgf7kRZlrfUQPIAIlx4_c8l74a8Buyt4HfR8bpEtN1gF9-lRE0MVuyibkYWpm6kILs6CmaeXUx9GVM8t-ly8Luw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=J4EvKUbUJoNAei6GUZmh_Y7r5tmtcoXWWyGsv158nt2nvH-iyrVHQO_1uOimLJ_CVARqVEXApMX945FsC42rD2MDvde-M-LsqSG0TAz7J5CIqg6ykDIe1OqD8x4UuhRSHAoRmcsaNycs9F20eG3p3mp4Lx9VZaWUyy_xvweo9BUXqSGhmPJAghAWXBqF5EkPA6LToxXphGPjolx390RPkaKTFTrDmwBwNioZEHcM4iHKnYcSHwWwo2b7yYsI640mxlz9BCETLhBnAViDPhfYJq4Lyq_3oYXn74lRxxRzBAr3_bE0Zp0SXniceezCkJQg0os05rcNOpumsmbRDFJpIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=J4EvKUbUJoNAei6GUZmh_Y7r5tmtcoXWWyGsv158nt2nvH-iyrVHQO_1uOimLJ_CVARqVEXApMX945FsC42rD2MDvde-M-LsqSG0TAz7J5CIqg6ykDIe1OqD8x4UuhRSHAoRmcsaNycs9F20eG3p3mp4Lx9VZaWUyy_xvweo9BUXqSGhmPJAghAWXBqF5EkPA6LToxXphGPjolx390RPkaKTFTrDmwBwNioZEHcM4iHKnYcSHwWwo2b7yYsI640mxlz9BCETLhBnAViDPhfYJq4Lyq_3oYXn74lRxxRzBAr3_bE0Zp0SXniceezCkJQg0os05rcNOpumsmbRDFJpIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSrWr5ztZy7OM2jxz1tUUuLKwUOffVdlelsq5v4pvFk869gQOWqULelRej8HAmmvIXbjwQ2C63zYaA75enxH1G_rBn_kF9TSLTXStFy6dBLdHpL1mYEqfM8HYzjagH52zZEOHFwCXWZy-fPHvYbVGquFJWfIfPXc7aNAr1YVv-4DrNrmrzdQ0EqmX-fvYPpRXLoicgtgGpt_6lOn2lGy8dz_ItF0EaafgOmPFO25pOgNPi8z26DjlmK0TzFnAq1WT3KFCO4qU0nJULh-WP3i3nni0TH7K9ZLPm7jmYgmEXxus96LMVBjalnLCbCbq197BWpq3YmRRtT3EBX5nHCnfQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EILykd2_cSMa0Zd245IELI_I9YOBK1s7qn3dg_saw69bcnwQ-efFNdUn9y_r3UqUqxujh9OaXcQPtQizwcrwW3O4rpXE8ttfVTOz0YTbJe7-Tg6er6luNvlbzfxCmBHzkIiD3sW_FcsS9mdjSUIG0mldYBc8BIb-HNOcvAir322eYn_s7fLSWesMMtS4Goub51gcuz9QdQ7GM7SdxoeFeslslxmGGmnEctGpjv8NbyFb4M5kdsox2i8S4rjYOfX0GVPGzciLjkddSk1Swf1B4md_BwfhRK2nCmfvqG3Ep31d4LqKPG1GpZ8JBXN3DpvcTByXBwiqTfQmVtlFN0dzew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8EILykd2_cSMa0Zd245IELI_I9YOBK1s7qn3dg_saw69bcnwQ-efFNdUn9y_r3UqUqxujh9OaXcQPtQizwcrwW3O4rpXE8ttfVTOz0YTbJe7-Tg6er6luNvlbzfxCmBHzkIiD3sW_FcsS9mdjSUIG0mldYBc8BIb-HNOcvAir322eYn_s7fLSWesMMtS4Goub51gcuz9QdQ7GM7SdxoeFeslslxmGGmnEctGpjv8NbyFb4M5kdsox2i8S4rjYOfX0GVPGzciLjkddSk1Swf1B4md_BwfhRK2nCmfvqG3Ep31d4LqKPG1GpZ8JBXN3DpvcTByXBwiqTfQmVtlFN0dzew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aHohMciVm8GSSnZD4NUevBs9ajxm5fZlmzpqMjUxwry5Bx6doutN7V1R6wtw7_GuQDs-Uvr5f25LYrxqybKP87yKDt3r65UpwRIgeliOVu6jpiho6kYtHp50_0ImobzHOfT7g2oclPqWrbbN_1FeCebtWR7Zpfr8WcLv4BlYIIky9hZuCPUOdEIYaum72MbJ3ESoXTDWxtqI9h4NrZIQLWt-32whEa2IIOh5qB999cYHl7dO8NtGRazqI3T5mZPB301mgyEXuiznZiGYl8ctDeQekv50f-Atnsg7vbt2MR2_XVdNBpJDiIFDMMfLHrf4TlmrqLsuXdDmN_l432hDyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=aHohMciVm8GSSnZD4NUevBs9ajxm5fZlmzpqMjUxwry5Bx6doutN7V1R6wtw7_GuQDs-Uvr5f25LYrxqybKP87yKDt3r65UpwRIgeliOVu6jpiho6kYtHp50_0ImobzHOfT7g2oclPqWrbbN_1FeCebtWR7Zpfr8WcLv4BlYIIky9hZuCPUOdEIYaum72MbJ3ESoXTDWxtqI9h4NrZIQLWt-32whEa2IIOh5qB999cYHl7dO8NtGRazqI3T5mZPB301mgyEXuiznZiGYl8ctDeQekv50f-Atnsg7vbt2MR2_XVdNBpJDiIFDMMfLHrf4TlmrqLsuXdDmN_l432hDyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLiS6pYHhlo-BFLm7Nr0w91RA1mxrlGVDWYHuoIuYvN9Ru4qgsPz5UDGmNEY3eRlYOCT2p1XTx9gZKpuRbZjw4poQvHwX93-vyCbebvBiBVLEFGSdHa381U_Ymw1Ze5f5VpO7H8pppZKaScL-nMMRHuLN0WqxZcVP0EYdFGbsV7RNHKGJtNgRLjN3ZlsjZ5ajMBKpPusSEgcFBUda-i-PSS004PuygtLY4xiRKFm0P9b_AGcmYgBH7IgOuPJI93YnR_-UNCa5mw1Lsl3BTRh8EZhj-ysMsZzfqhCoRto85kRytcgHvnX5WB62JWorn3n1NxiDb5vKaKGvE8_cpZVrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CYf52Unh-xSqcRv64_rB2qBqkFRbdeP4nORphhbJugp7NIAaHLnbQ_dLxGHijhZATQsGHWCRkyH6u3A2OZWw8GnzkEMg6FT931rmJIpGbgW_6OKxAJ6CVK_faLP-tq8ZE7cYf1I8DV3TJtSforS3iu9rYU68NPNjJL6-PipnZl6oCkMqcY-rqd1axQWCrSmdIbLSAEHh3dBeukQhox66Ez6o8yg0RWN4jG25aIOkO7xmsw8jW9OPKKH5JjOSsB98wnno1H8rDRPjmeEl1xJBM7PdJdrXjRmr7zXKaHEqNTp9S4764_O7D9AWy215tS4PV8B6ERfR1-oJuPTBu25DW4HWFr0SxGe9IBCSRBuYKSH-VWYH56yrORGo1u1Eq3sck7TFYW3CEZDqj3z5L7pWJ3B5pFGEd3j-ESyvGlTRoVj9xtJ0Lq6Z0q-y8oz1MeIFxcz1B7NiSkKQPsRHQhyD60FEWctdAHupM6r7PiOs9m925CMYzAi1jFyObinLdWx4xHRe_NF9p9oCVZT0k1HnknWfP_4J1onbBdAwFvOzpzVkRJH5d9a37E1iGp_7q9Mv3KQLu_ZNQdHqpmXmXNfeGFCG5K1MlHa6h568aNCR9YrHbtuFvCHKrj-xRdo-AYHRb4quiVr6Gfd8p75eBNGJ35bp4ddd7cNzD6IjVuRVjCE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=CYf52Unh-xSqcRv64_rB2qBqkFRbdeP4nORphhbJugp7NIAaHLnbQ_dLxGHijhZATQsGHWCRkyH6u3A2OZWw8GnzkEMg6FT931rmJIpGbgW_6OKxAJ6CVK_faLP-tq8ZE7cYf1I8DV3TJtSforS3iu9rYU68NPNjJL6-PipnZl6oCkMqcY-rqd1axQWCrSmdIbLSAEHh3dBeukQhox66Ez6o8yg0RWN4jG25aIOkO7xmsw8jW9OPKKH5JjOSsB98wnno1H8rDRPjmeEl1xJBM7PdJdrXjRmr7zXKaHEqNTp9S4764_O7D9AWy215tS4PV8B6ERfR1-oJuPTBu25DW4HWFr0SxGe9IBCSRBuYKSH-VWYH56yrORGo1u1Eq3sck7TFYW3CEZDqj3z5L7pWJ3B5pFGEd3j-ESyvGlTRoVj9xtJ0Lq6Z0q-y8oz1MeIFxcz1B7NiSkKQPsRHQhyD60FEWctdAHupM6r7PiOs9m925CMYzAi1jFyObinLdWx4xHRe_NF9p9oCVZT0k1HnknWfP_4J1onbBdAwFvOzpzVkRJH5d9a37E1iGp_7q9Mv3KQLu_ZNQdHqpmXmXNfeGFCG5K1MlHa6h568aNCR9YrHbtuFvCHKrj-xRdo-AYHRb4quiVr6Gfd8p75eBNGJ35bp4ddd7cNzD6IjVuRVjCE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTd1EijWbuZPmUccFZ821UD6oG0NHWvs6RktuBxBGXT_TCNZLnwinWS0S8HIVsXCXN4V-i_X6-CbeYAZl3NBE5G4uQUyDuxJgHOENLWDthJsO4WQDkVaIKv7uxHndj6oBnv5zn214kj_s9R7udbdge5T6Rwo55OirXQOdjV4PGKi7BTkyLhi4D6iNcaVM7V8q-fvkYzTG3wmvhi3qv1lCI3F-nvmPw3XXn6PuFGdHT1PbOVJYJT_Okw-d0bQ110pvkCfJdlFDvT1EuNWJqlGNUTT3uEjLZqZyL7rJPdDVAksXrA8U8tYWbKUtD9TALI7Y4xsRuAxZPD_8zDmjKP-ng.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=khM6gEworYu116JVmodLCtYt-kvJbZX9USW64OFf_qr263PKn4t88baLbW1rjo5NOQYx_Tvqm5D0JTMXHRo4BHiNPuPk4bHNnfo80Qtt205rb0yCSUzCNzHzFfRZGgJnc9u1hN7yPjPICawnQPNMfl-_yEY7xnVg44QKFF4vVf6s_g2eVKgrYwMsD-rmKd1u5d1IbI7N92v7Ua-rxuoXJP42d55Oh19mPsHKkSEDNNQDTql5PSPYS259J5Eo83ezI1dX4v_6TxIq28G3Y37JvPOoL-7eJVE9bjrTwxJYnrlgWN9QNixfDObXlKsE14IAige1wiAk5vdPfmXNmQcTUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=khM6gEworYu116JVmodLCtYt-kvJbZX9USW64OFf_qr263PKn4t88baLbW1rjo5NOQYx_Tvqm5D0JTMXHRo4BHiNPuPk4bHNnfo80Qtt205rb0yCSUzCNzHzFfRZGgJnc9u1hN7yPjPICawnQPNMfl-_yEY7xnVg44QKFF4vVf6s_g2eVKgrYwMsD-rmKd1u5d1IbI7N92v7Ua-rxuoXJP42d55Oh19mPsHKkSEDNNQDTql5PSPYS259J5Eo83ezI1dX4v_6TxIq28G3Y37JvPOoL-7eJVE9bjrTwxJYnrlgWN9QNixfDObXlKsE14IAige1wiAk5vdPfmXNmQcTUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQXyruq-yX0UNmcnbi6Q55takYw6RDLQ6xvMK6Bn4BHIe1tu9bs9yvEPRYSclZru9SboWesGBgBPRoj6L1qBKKSzhcdKwUdW1UvrBeGKgYj-_efxT0z9kt798v3Px8Vv-mSTnoa0jq_UffJykKF_kzmOe7u59asS7QsJYvMeuOUduMtbH3RY0TZVbkLCjUMNQDm-_aBLjB0XJikV_HC9KCxuL26hszI-_OhDKnHtycztJWuwaO1nmsKS5ao8piStFqroDN0jjJtPaT-q6i-mPq9nupNGypKrq5k-wh4RABHgVcH9SiAJQ8tvrBPdzfLIKLq7K_bKXLXpbbcEBNcgYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rte5_WE3PYIHxBSo2jdWFBKgOcxM4tNFrz3ZcbpjLJWLBf6JnUgEImDhCNenyDw_6OLb0j3Q61ecKQSBNoXRJgym_J8zGSfBkJp9iI4pT9LQZFMsgoz74tTbwDCocAu0ZvjGMCKCtNaOQS3b4EXNoTDhDRy_6ahocE_DKa5W0-dqn-ndLNyX53cwT9haNcn7hvfdJH2eLQ7by3JAHHVcmJu__mcSkrDmPBCWSUFQmiqLYsgGDMwfnPvtd3A-7sH9GDTaAWwWhc6eErXyvPcj5nwLtwD0oTe48RxTgwjsnQEpVbwCJZHbO24aU71rPjWNzAwj9dLov8gEDDIe7LQB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrmMorI80g06ikFzaD2IAgKYmklhzH2W2ODQzUUNhWnxLqNVg_N-eW9lrZTp9wA9aXO12jPpffDB024BTBnSJ2NyVklx2np0bnjUmHVOn89Y5i1kY6PEOG-i6Npl0eeEMIwbYb_GEgkXSJNNbQxcK4T-G_e2qvhjgAKFc9ZAw93guHJNI0qtxQD4ouDXR0urAeGiYzF1cAUeS0460xEEKIDzZLs-Yias-gVv5DhE_5AzW8io4EiuiDs_vsgvvChkI6ECkrYe4CXKMJ3f1-BnkBtKs6l_06lMEEz8kCDaNtpVmEjDlhH-9ykqccoZOpRzXkHdT6G93omMZrQ2VvxbUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sfJcgG4BR0_kjshpYpcrY7oWV3tjHqzDYRYnGHtdD8f7tX7bues0uvZAUtiCz49VeFT-gqZp3Cv40cEcoFmS2Z2m8UU8-eoBdwwKJpu7rsqcOh0QH3_dm96FYxowOj_X9JstEgu5qddsgxV7Xz2v1V1nPmCiUwT7nbf6ZPCvbBLyRTKAqQfshM_831wq3ZhXaZrQuuTpx2E4W66g8KDqzO7b0gXFPYAQTMNjjdC8cgelhypSm3oukYzH-DHgqcr4cVLedZ5FOeC9BoDHKr3sKYTmfVVmkJZW7EIXFv7mv-df-w6z2PIZps6Ria9d0ahV6dBOnc_PtmEillQqWQd6NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=sfJcgG4BR0_kjshpYpcrY7oWV3tjHqzDYRYnGHtdD8f7tX7bues0uvZAUtiCz49VeFT-gqZp3Cv40cEcoFmS2Z2m8UU8-eoBdwwKJpu7rsqcOh0QH3_dm96FYxowOj_X9JstEgu5qddsgxV7Xz2v1V1nPmCiUwT7nbf6ZPCvbBLyRTKAqQfshM_831wq3ZhXaZrQuuTpx2E4W66g8KDqzO7b0gXFPYAQTMNjjdC8cgelhypSm3oukYzH-DHgqcr4cVLedZ5FOeC9BoDHKr3sKYTmfVVmkJZW7EIXFv7mv-df-w6z2PIZps6Ria9d0ahV6dBOnc_PtmEillQqWQd6NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxeUwck78MiliAv4Ju4MhvZ-SdAdtvrRG3sykiGzwUo6Cp5GLwsiEcxsPjthWa0XH3hNmhhz-kbT5y7HIYa71maUhGv8Wai7-ZBqJo3wV0t_qIP_q0CybKaX2OB5sp4PHMhVqZrqz49FMeoH-zka8gUJ_U_vWJXfbZfdTzN_hm_nJoo_lqPywxTKL3XzA2z4MoWR9Re1lx4WV6dYdz2wPmQYrWv2oBujB5QRtHCFnS1-O5-EV-oSulrc5bVhjwpj_FD2SnW4uFpXLpmE6R7bOuzUHemv0XmPii5g7QEfVns3oJDfOvoVxvVBvqo5yL7EOSasdYgL-JK8z6VdVve8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFL8AA1upGuyMQnZYmHb2ot2u1xJ8CL4nr0R7vTOovKCRAhxVETpWqVJLG2qjrvPkJ2raDiMOI7NKg-jrJorN5VhlyYNq0Xtjlc9j_JE2brNyYMUKBFbbHQkdXX7W6b4YTkCvgM0--CwnZn7S2UosgClQENSHA6SjNHSIQMDUdEc7_XZv5lZYlcxtZj3UC0hRMLGQzMbzmnr-fU2DMp4soypze4nw526wyXnxFhJlVKRObLxcGW89ENnVLdH7eQIWMssQ_Hywy5XngS8wN4JmY6PPHY3Y4p7eNmybFskZKfP10rwu0_4lEA3zPsCKMOLMtvxIoaTnnPy3rlIqPoY5OKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFL8AA1upGuyMQnZYmHb2ot2u1xJ8CL4nr0R7vTOovKCRAhxVETpWqVJLG2qjrvPkJ2raDiMOI7NKg-jrJorN5VhlyYNq0Xtjlc9j_JE2brNyYMUKBFbbHQkdXX7W6b4YTkCvgM0--CwnZn7S2UosgClQENSHA6SjNHSIQMDUdEc7_XZv5lZYlcxtZj3UC0hRMLGQzMbzmnr-fU2DMp4soypze4nw526wyXnxFhJlVKRObLxcGW89ENnVLdH7eQIWMssQ_Hywy5XngS8wN4JmY6PPHY3Y4p7eNmybFskZKfP10rwu0_4lEA3zPsCKMOLMtvxIoaTnnPy3rlIqPoY5OKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=GZ2USdptMm0BxjNF6_iHxOEQCMHFaaY2_p5VkO8POZ-HXAZc4pY3_3ZaiPuAudaVHvgk3dkSYg8VAeVeXuCqDiktwYkjRJxWC6-SIsIGUf8-5Lh317Zgtt2NTtS-CQ8xgo0-HCmmBRNG1gM-KGDGkGICkP1O4OEcKBtVkKz5L9DOeKObwoOkfsxzKJtZDlZAGQ_k57y38PwLpfSHTAFa0H0Mv4GbtYXvc-4K-vCYaQupsIjw4laA0-cswa5VdnlShgFaPC8z0NXy9Rcwrqt5sxOc53lAkmhBuCQEhw5VSkA7i4uLlUVYjh8-N5ri9pT_8Cg4Crrp92wK77dSyGiE3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=GZ2USdptMm0BxjNF6_iHxOEQCMHFaaY2_p5VkO8POZ-HXAZc4pY3_3ZaiPuAudaVHvgk3dkSYg8VAeVeXuCqDiktwYkjRJxWC6-SIsIGUf8-5Lh317Zgtt2NTtS-CQ8xgo0-HCmmBRNG1gM-KGDGkGICkP1O4OEcKBtVkKz5L9DOeKObwoOkfsxzKJtZDlZAGQ_k57y38PwLpfSHTAFa0H0Mv4GbtYXvc-4K-vCYaQupsIjw4laA0-cswa5VdnlShgFaPC8z0NXy9Rcwrqt5sxOc53lAkmhBuCQEhw5VSkA7i4uLlUVYjh8-N5ri9pT_8Cg4Crrp92wK77dSyGiE3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=PEkQ81KwRd6pFx-wFVYjQeeE9zVMm3AuodtnNnNteJYBwGUL6Js5luQTgSTij-sAwOMVb6yFzARsauzI_HRvkUVOGlJXWrndDNFUTwFKoBd14mh39l3PxBF34vzO9twgI8eBpHZ4Y0YT7fRbaWO6RkXcZYGaJFrePQV1Z9cED9qK4VqDGGxhzmXfKCbT3itFcnZgVTW1HwnKXJD_GdfRv1Z-8rYpQl-o0c-rTUqMQN0-ajtCmG9dEUsn39gDDBK1dPE3SiT1JnHXkuH9linW4MLk1So6rJC6SsAjGMaHeJCpiHdFjcPrNuQ8IR3J-VAhiH8vwqJee8QhRRf_Ay6gzGSFahoRDB4GaOw-5xN8faLCn1U1gpl4S9pHy_2TSK_g-idSbQD-0eH2brR7FU5zfH_Os0mfvbxgYWwI4hsIIhPUII4eEUPd4jXvLJryx--4GM8ptHgdwI7otB5kLXsvNMDic1P2oh9-crMnk79d7mkBAGPpa5Kxns1w2P2VuXwlRGqHBWOnjj0vMuvvHOHEVk15WYrQT1JQGmsTLNcngoPeymwkj0vfTx8KdcgR3kNC8GK5uJhQckwumlnyaALFSmlE9pBVlpx6-SDYK1OmMsvcMWOMjtxOrVlH4xjbuzNs_VmcVN6o1VfZoNOS8Xapm2W9D4S6p4_wVRPDrSd1ZZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=PEkQ81KwRd6pFx-wFVYjQeeE9zVMm3AuodtnNnNteJYBwGUL6Js5luQTgSTij-sAwOMVb6yFzARsauzI_HRvkUVOGlJXWrndDNFUTwFKoBd14mh39l3PxBF34vzO9twgI8eBpHZ4Y0YT7fRbaWO6RkXcZYGaJFrePQV1Z9cED9qK4VqDGGxhzmXfKCbT3itFcnZgVTW1HwnKXJD_GdfRv1Z-8rYpQl-o0c-rTUqMQN0-ajtCmG9dEUsn39gDDBK1dPE3SiT1JnHXkuH9linW4MLk1So6rJC6SsAjGMaHeJCpiHdFjcPrNuQ8IR3J-VAhiH8vwqJee8QhRRf_Ay6gzGSFahoRDB4GaOw-5xN8faLCn1U1gpl4S9pHy_2TSK_g-idSbQD-0eH2brR7FU5zfH_Os0mfvbxgYWwI4hsIIhPUII4eEUPd4jXvLJryx--4GM8ptHgdwI7otB5kLXsvNMDic1P2oh9-crMnk79d7mkBAGPpa5Kxns1w2P2VuXwlRGqHBWOnjj0vMuvvHOHEVk15WYrQT1JQGmsTLNcngoPeymwkj0vfTx8KdcgR3kNC8GK5uJhQckwumlnyaALFSmlE9pBVlpx6-SDYK1OmMsvcMWOMjtxOrVlH4xjbuzNs_VmcVN6o1VfZoNOS8Xapm2W9D4S6p4_wVRPDrSd1ZZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GUlXu3Jm86XmmYxW_sF8OoYlyAgpXzXYT64xESYkdNMa8zCKM2DMHwhDg7mViN6RAm54Ek8mbiAFvMv_jF0OX47m20y-O93CKu4Y8CwUIT0Qlx2PhlKvNafjVeDZnvsylcrS5s4yK85mL4-CJDprO6MNKJ-hqJK7MjnU-BqBC6vbwnne8ddyRXAtjPp6jBsZqvI7Z4bjGhxROSCk0JWgmzKrPllCrig7-ftlaFeLRYyWSrI9QF1Nx1u8H3QREfBPpioQq1g0KZ6-ecu7TXn7w7ST0M9fWEA0lVjWPmg-MGWi48KanVVbRZo6gM_2uSQ7NcNvy4BJ-El3Kbpo2LyLFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=GUlXu3Jm86XmmYxW_sF8OoYlyAgpXzXYT64xESYkdNMa8zCKM2DMHwhDg7mViN6RAm54Ek8mbiAFvMv_jF0OX47m20y-O93CKu4Y8CwUIT0Qlx2PhlKvNafjVeDZnvsylcrS5s4yK85mL4-CJDprO6MNKJ-hqJK7MjnU-BqBC6vbwnne8ddyRXAtjPp6jBsZqvI7Z4bjGhxROSCk0JWgmzKrPllCrig7-ftlaFeLRYyWSrI9QF1Nx1u8H3QREfBPpioQq1g0KZ6-ecu7TXn7w7ST0M9fWEA0lVjWPmg-MGWi48KanVVbRZo6gM_2uSQ7NcNvy4BJ-El3Kbpo2LyLFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fQT876P15o1OMrpdJSaJLppII1I4cIWFMgNN20HmHYZbJPXsQVIuc496I7txaaz9jHEL5cMYVJwJvDm77jMuR-LLjHDr9g_B_SdS0sQ-KpJQzQauaA61yuO91FsF9HVbSPrDXa1wfEp4rRXjrxcY_yoCZRSsKITWVG8UCsCESfwrcoiYYMZDytaNy3RBqE2ni9Ezj4tHoe4QjBSsyKiEoLZQT19kq_oDV3A5npENXsJLmUXzwGstYxqG_QA2eve1vQnm3aCdBjc87bCfV1mowqRhRu_v93cARYbTPo0G9yoj_Xwv1Q-NuYkbd_hYZGNXjk5lsiCXwDeASEp4hL_pKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=faFvpyoupQINN0HNN6CiKQq9gxbEtaiPc6-jrNOQb_w-TrBE6p8G4_bzlGRrR1oSdirx9QY5ba0ayS6OH7LCWwg24Juo1i2Jl47V-CsCg9MZfamqVV30FA-Lp3z-AzLSgOjIWa_tfHqyuqlOKeViCSLv-EPcx9d66dq9VCJTGkyAUqG4f8kb_nXcc6s9UvN24NnyvNplidzCdg5wzF9DOXkc375hZXZaOWAjbFPm6NSYHIZZmHBJmgi1kufelHubSjMXpPTdDGTsfDtFTbzP05c9ofH8VKuogCOzXdU5MUnxC1snV9Eb13kQ86TbR3EvX0RAdYgzwNPiBBzXpJiqow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=faFvpyoupQINN0HNN6CiKQq9gxbEtaiPc6-jrNOQb_w-TrBE6p8G4_bzlGRrR1oSdirx9QY5ba0ayS6OH7LCWwg24Juo1i2Jl47V-CsCg9MZfamqVV30FA-Lp3z-AzLSgOjIWa_tfHqyuqlOKeViCSLv-EPcx9d66dq9VCJTGkyAUqG4f8kb_nXcc6s9UvN24NnyvNplidzCdg5wzF9DOXkc375hZXZaOWAjbFPm6NSYHIZZmHBJmgi1kufelHubSjMXpPTdDGTsfDtFTbzP05c9ofH8VKuogCOzXdU5MUnxC1snV9Eb13kQ86TbR3EvX0RAdYgzwNPiBBzXpJiqow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Kc72fB1W-oZthFBpSprA9gUVNq_oXqF3O8Q4K0x11j4MRBhjXs1aPP8-SqupLrf1LbwgNOC5aBm225abUg6LXg92cafD8hgoTumcDbQzsZSaKvUxzKXZQKaYsDzAPfvauefY5_bsVcWLjVR4n8DCKdCg9atvWot595m95LGKqKH254z3P2ARuzIPtGbaD4R3jV_CHXUEDCieODovXJcku9_qkBD7FivWvylGEWj6zwSXiAdMrziXNK3-7LSkbae3JNTq78E2J8pGULdByaqB6BGMKdz0LfYo1WFCPb_oawrVpNqBhZqzmQFSTdxahC7BOa4tuVlu4U_W_nJQvjLVGHZwiIwHcKTA3fIvMPEj6ed6AxfzoiTHTfzNpfG1ixYxT5kBDgFr001Dblm25Fxvau_paiw2IV6u4mw1U9R4FMCavKP6bVQo7NG88ogI4HGoIDriIQLZ-sjHQp4TIy0_yiz4cw2vkuUYfgyFWxmMSwFTkrcFvHnj9jMQn5liqPURWUR_ii9a8CFlp8CiuPMh8a_BvAxYHZYvi2JLseBlzGPdwHU5igGIp_-8Gu72-RRdklhVcnvvfrNbxfqdDbgzdTw21wDCMq9AEdFxEzdvyqUm4uMc5KKMNOC58hDTHw5zHhZjMli6VNvvBN_m9RmEkdFrQigiH7eadq_LW8EgRnU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=Kc72fB1W-oZthFBpSprA9gUVNq_oXqF3O8Q4K0x11j4MRBhjXs1aPP8-SqupLrf1LbwgNOC5aBm225abUg6LXg92cafD8hgoTumcDbQzsZSaKvUxzKXZQKaYsDzAPfvauefY5_bsVcWLjVR4n8DCKdCg9atvWot595m95LGKqKH254z3P2ARuzIPtGbaD4R3jV_CHXUEDCieODovXJcku9_qkBD7FivWvylGEWj6zwSXiAdMrziXNK3-7LSkbae3JNTq78E2J8pGULdByaqB6BGMKdz0LfYo1WFCPb_oawrVpNqBhZqzmQFSTdxahC7BOa4tuVlu4U_W_nJQvjLVGHZwiIwHcKTA3fIvMPEj6ed6AxfzoiTHTfzNpfG1ixYxT5kBDgFr001Dblm25Fxvau_paiw2IV6u4mw1U9R4FMCavKP6bVQo7NG88ogI4HGoIDriIQLZ-sjHQp4TIy0_yiz4cw2vkuUYfgyFWxmMSwFTkrcFvHnj9jMQn5liqPURWUR_ii9a8CFlp8CiuPMh8a_BvAxYHZYvi2JLseBlzGPdwHU5igGIp_-8Gu72-RRdklhVcnvvfrNbxfqdDbgzdTw21wDCMq9AEdFxEzdvyqUm4uMc5KKMNOC58hDTHw5zHhZjMli6VNvvBN_m9RmEkdFrQigiH7eadq_LW8EgRnU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxOKswDrDY0jG9XSeT6KZs4_fxOgaGPuVOtL4hU7Hozs9bpEzHv_of9M3xajSsrcVsYnC16MlLJcJcqYZHOcAOhGdGQPzSH_e20YtMOUCTwX7utf33QYx_KjaBDxLQwvE83JdRDbJmScMZBlnx59qmw10I0ywtm_2cnimbxrZK7CeF_T_C6kGcUCFMalDq2r_7iXwAgshyq-EWWbHMJqvDZHlSoR_fSyfF53Dycq4KJMoWZEkE6AZxWo3o6JLQykkh3DbQfOcf7PS7Ojmbi8dw2uLD5Sa17iiM96aU2jdz1ELBPPQ_Ero0J4RibvHtv2HyJJVIEC4OHRj-D0vuzOjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=BFaxeCir87lLmoF7Qy7rqBw463VgIw-r7KmaFeLl1QwV1IVHOcFoxgWwzuXhHhTKWEHeDFXt0Q8QjId3LDA-2G3WFjqBQcrTy6e9XwuV20WOSWwJVXEa_oC91b4UffQA4lYq-xt6U8_j2jGczUjH1ZXnCndJv6r57XEqk6WyJ7ae3Xn8P2Z3F6KmFJU77ZVSzBU8yFL_qoxhAUJzX0pi3ol6KjrEVnNUmzi4Rqh6wCc2BgHnJtH_dsf2aYiKOdh36V9IxabfHSdRubJ5gnLazMHJecH-Oui2fGGQuvAf3W2NgorleTRoSZhDJ08W9KWfcpYWYLbVtO6jIEEy6Un3fZAYlSAC3c1p85B74Zh638l0Za67VCPeMeJtkM972p-lz6-mjKZs1FCnjQTdIKTQwA3AxNIqAE_3Wty1aH3HqnZweduswnyzzun-T0nJRpt61dqPp-cURxXyDcnmud4fba02xNV73p6N4609CkCHhVi1dXbh3fcsXuApUiuHasK7MDHRnOMwbEFSF-zDD6_ZqD752huEZuFXKQumug0HdWvzq50WrhQ9m3YdysUUoI15NJPx881-sI65POrqq9foE1q2g5IxZniPm2AA-QCXAqOfFdeYsP7v5EftfS5DDcJNl3VcuYp0baqlHJveEJ9xLnA9IZtImTcR-y_Jr_As4Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=BFaxeCir87lLmoF7Qy7rqBw463VgIw-r7KmaFeLl1QwV1IVHOcFoxgWwzuXhHhTKWEHeDFXt0Q8QjId3LDA-2G3WFjqBQcrTy6e9XwuV20WOSWwJVXEa_oC91b4UffQA4lYq-xt6U8_j2jGczUjH1ZXnCndJv6r57XEqk6WyJ7ae3Xn8P2Z3F6KmFJU77ZVSzBU8yFL_qoxhAUJzX0pi3ol6KjrEVnNUmzi4Rqh6wCc2BgHnJtH_dsf2aYiKOdh36V9IxabfHSdRubJ5gnLazMHJecH-Oui2fGGQuvAf3W2NgorleTRoSZhDJ08W9KWfcpYWYLbVtO6jIEEy6Un3fZAYlSAC3c1p85B74Zh638l0Za67VCPeMeJtkM972p-lz6-mjKZs1FCnjQTdIKTQwA3AxNIqAE_3Wty1aH3HqnZweduswnyzzun-T0nJRpt61dqPp-cURxXyDcnmud4fba02xNV73p6N4609CkCHhVi1dXbh3fcsXuApUiuHasK7MDHRnOMwbEFSF-zDD6_ZqD752huEZuFXKQumug0HdWvzq50WrhQ9m3YdysUUoI15NJPx881-sI65POrqq9foE1q2g5IxZniPm2AA-QCXAqOfFdeYsP7v5EftfS5DDcJNl3VcuYp0baqlHJveEJ9xLnA9IZtImTcR-y_Jr_As4Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=h-9hWClsezqbQQwdcXE875bH7iiIey01eJu6stEfLeV1tgjxiKjU6UBFooNDi1iiI3bKwzHc-W471BYdlJvKD0b_nSC7FHiE8PaK3iTF2Did36li1NijcgiH7WYZaKE4lXLzvbSfLEuCYe-Bhmc9VmIF03NbUCTtJVuvoxzH6r-MdtMkMxOF3T9CyliL0nXqSdjdo0ykzlt6q2UOoDmiokWAMGv9Z-Xwp8Ja6fYw6QjJ1y1HrX45kQTmrOLNAvv6DSyv0Oicnx369nLuo66ZQLBaZIHRTijnaSwiVfOPoxmvRTWNcmn-Lo9RAw5s46rLtd4jNUTaAYTLj4gwSnLTdzhswdU_x0tGsHhe3RxypBBLFEhNNByHiJ0uaH8lAiD45xqPb4B5DwIsofEm7jfYbPGBM_gU4i3apeCm56yXBAcPqTsb9VRCGIT5R3ZrntEn4gIQe0GETsWBWsyK4fBTWvARiuUH8byIF-6gw6snOzcEue6mJixke-tbW74-HCJEFlB5DFyBfNG8PpXgBe9vFZDPo07GD8o0lIx6Uun5Cl6bf_g_xvH4-QwwNNWv6P8xd7QQwBcYOrsHJr8_IkuFo1TX_epgIQaaKPSvWh28DtCmqavgsq28S3VbTbe5S0PGs3h-VH-0OdbIjP4GCtOwKEJJbS7Jqb4LHTnKISWGpUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=h-9hWClsezqbQQwdcXE875bH7iiIey01eJu6stEfLeV1tgjxiKjU6UBFooNDi1iiI3bKwzHc-W471BYdlJvKD0b_nSC7FHiE8PaK3iTF2Did36li1NijcgiH7WYZaKE4lXLzvbSfLEuCYe-Bhmc9VmIF03NbUCTtJVuvoxzH6r-MdtMkMxOF3T9CyliL0nXqSdjdo0ykzlt6q2UOoDmiokWAMGv9Z-Xwp8Ja6fYw6QjJ1y1HrX45kQTmrOLNAvv6DSyv0Oicnx369nLuo66ZQLBaZIHRTijnaSwiVfOPoxmvRTWNcmn-Lo9RAw5s46rLtd4jNUTaAYTLj4gwSnLTdzhswdU_x0tGsHhe3RxypBBLFEhNNByHiJ0uaH8lAiD45xqPb4B5DwIsofEm7jfYbPGBM_gU4i3apeCm56yXBAcPqTsb9VRCGIT5R3ZrntEn4gIQe0GETsWBWsyK4fBTWvARiuUH8byIF-6gw6snOzcEue6mJixke-tbW74-HCJEFlB5DFyBfNG8PpXgBe9vFZDPo07GD8o0lIx6Uun5Cl6bf_g_xvH4-QwwNNWv6P8xd7QQwBcYOrsHJr8_IkuFo1TX_epgIQaaKPSvWh28DtCmqavgsq28S3VbTbe5S0PGs3h-VH-0OdbIjP4GCtOwKEJJbS7Jqb4LHTnKISWGpUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KxvOhisygLOirMVygVj8YiYcnOKccpnT9R_FYACYiQ9ZCZoaMxjagV0X_eJRjKflaXpIBaofTSvvoewTkP_P3U2S-B5i2mA77-VJAugoH3Y7FEXXlnOZ0QczWegBXZPK8Ds7YqvIW5DlSZUb20bMFFP0B_9nRUrB8L6SeMIRwwIJgmlsCEKsGV89Qd1HiqKutxz_maeOGakw9hOfhVkrq5FghK8K7cTIqLczr5aFbdUTTcq3xgEuZ4GRcEQOK4QgqVuh2hxn8xs4S_pVo6GHgAfNSFbWg5LqgTFWUZAYkqMoMjXDxh6XxQ9n9U9WyMGKdBDyvBGF4Q90HDi5pD004A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=KxvOhisygLOirMVygVj8YiYcnOKccpnT9R_FYACYiQ9ZCZoaMxjagV0X_eJRjKflaXpIBaofTSvvoewTkP_P3U2S-B5i2mA77-VJAugoH3Y7FEXXlnOZ0QczWegBXZPK8Ds7YqvIW5DlSZUb20bMFFP0B_9nRUrB8L6SeMIRwwIJgmlsCEKsGV89Qd1HiqKutxz_maeOGakw9hOfhVkrq5FghK8K7cTIqLczr5aFbdUTTcq3xgEuZ4GRcEQOK4QgqVuh2hxn8xs4S_pVo6GHgAfNSFbWg5LqgTFWUZAYkqMoMjXDxh6XxQ9n9U9WyMGKdBDyvBGF4Q90HDi5pD004A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=uz72sJguYRMIvjAIbbY0DAWUndWEgnAdn51GjFHo-FM3IGKu8VQsJ2SAtL1C2791b7oBxGaqT9QlWwrz41QRSrT-ryHJH2XAFY8FSbeInKLUuC8eFBqUCttLjLQy02fraTTyfOTDPxhUejeFUUYOu5GibvQID7UUQnUI0rqJCpSCcnKXveQPgp6j9BUvUpypQRJZxr1YvOCv2WPwC5y1ZNV0b1Yy9sqnKqDfcBC6U7nHGs442-El87UNmgSlzX48T-bu4y7fa_DMq9CDSgL41NVflvtGBChN9SUJZLgNstUonAHIkLFwDROf6EldJxb4ajdUVkJy1AxKmlYuHvjSpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=uz72sJguYRMIvjAIbbY0DAWUndWEgnAdn51GjFHo-FM3IGKu8VQsJ2SAtL1C2791b7oBxGaqT9QlWwrz41QRSrT-ryHJH2XAFY8FSbeInKLUuC8eFBqUCttLjLQy02fraTTyfOTDPxhUejeFUUYOu5GibvQID7UUQnUI0rqJCpSCcnKXveQPgp6j9BUvUpypQRJZxr1YvOCv2WPwC5y1ZNV0b1Yy9sqnKqDfcBC6U7nHGs442-El87UNmgSlzX48T-bu4y7fa_DMq9CDSgL41NVflvtGBChN9SUJZLgNstUonAHIkLFwDROf6EldJxb4ajdUVkJy1AxKmlYuHvjSpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=n7R1D4S5s072iwUpJG7KSe6MM0Zn8AXYV7IGpQUjZoxlkjWdB8EdrvXzLfXT6PAEwe8nBmjKizJJrkmz7t-Zh_ZoHEWXnvYp30-tsrYbcDGo_SlALeb4wg0y89W0ISA0XIlARO8ngvNbJHxM_0WQCwz85yYTxeWKnkuln2qp02B5EFnLDy3UJFPDGU2lbK5_JEhApcfiN_hGku5mrZ81oukTKE2WiNcxZY0-tp2l8cJGxjv_uCYikT6K1AMo0KAB2U6HGQwUdiwzzgzx6-DZm-RFa2w3S9YIJgwVmuyycJUobjtaMPyB0GKkXwHfdd6QgnOCLfLrB6urWHFMSr9psA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=n7R1D4S5s072iwUpJG7KSe6MM0Zn8AXYV7IGpQUjZoxlkjWdB8EdrvXzLfXT6PAEwe8nBmjKizJJrkmz7t-Zh_ZoHEWXnvYp30-tsrYbcDGo_SlALeb4wg0y89W0ISA0XIlARO8ngvNbJHxM_0WQCwz85yYTxeWKnkuln2qp02B5EFnLDy3UJFPDGU2lbK5_JEhApcfiN_hGku5mrZ81oukTKE2WiNcxZY0-tp2l8cJGxjv_uCYikT6K1AMo0KAB2U6HGQwUdiwzzgzx6-DZm-RFa2w3S9YIJgwVmuyycJUobjtaMPyB0GKkXwHfdd6QgnOCLfLrB6urWHFMSr9psA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=pY-w76yM24joinuNjwaCS-swJhs-w3Yq0ETJ0QBb5aptJmwpWyPjYd2mdI-Ci0qzt0gBM1b2HiRtZSUy0Nqz4QFQ7zz0Xu5K_RSGZlnHxdccl12gGZGZ9nY-p3aLeROeZ-2e4H4jOD4PfoqYF65BHDoVbsPZnzUg5kjpsPt4dWYaf8Dqr663QaVLLof5KDtT33wtJokY1tH2Gg8LmJGxtMZPgHPPf9_bxhpS5I5UpUD1tveYdGMmCichqMyKTDlBYjILa9FRcBR7OFYFevG-WntrV9UyJz-4Syo6JQo_uz-l1km2ZRZh3NrYyHPOVJkfnq6ec0F6H2-LEbA3WB1Low" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=pY-w76yM24joinuNjwaCS-swJhs-w3Yq0ETJ0QBb5aptJmwpWyPjYd2mdI-Ci0qzt0gBM1b2HiRtZSUy0Nqz4QFQ7zz0Xu5K_RSGZlnHxdccl12gGZGZ9nY-p3aLeROeZ-2e4H4jOD4PfoqYF65BHDoVbsPZnzUg5kjpsPt4dWYaf8Dqr663QaVLLof5KDtT33wtJokY1tH2Gg8LmJGxtMZPgHPPf9_bxhpS5I5UpUD1tveYdGMmCichqMyKTDlBYjILa9FRcBR7OFYFevG-WntrV9UyJz-4Syo6JQo_uz-l1km2ZRZh3NrYyHPOVJkfnq6ec0F6H2-LEbA3WB1Low" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=j-gCkqtcuReU5I8p6mXugzHACFmSSgPTAx1wAGlTJjWW8gUT6XSN7q26SXl_Et4Ij66rN-vhBHFK5GXTuxaBJuY8dx66GdCNA4OsFHuSF_2PxpwSQnBy9HjRFaILvsEwdnlzyNv3fO6w49ptpKDQbI63qLnvyw-gdYhzT0KB6ko9wrK2IRkbP5oIdzPokYBoO4eifajLqzvR1xJ9peBRZxgxuEKFN_s8RKS7NezbGdU8973c4291XPK1YeTkMmIWYzs8WfcdkDdpsm_FmlbC0ELVyqtZBaVMITlo1Vg7-gMUQGHSwQKrLNNVFmAmTiOrzWZZpwGTNdQ7UfWgdDd_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=j-gCkqtcuReU5I8p6mXugzHACFmSSgPTAx1wAGlTJjWW8gUT6XSN7q26SXl_Et4Ij66rN-vhBHFK5GXTuxaBJuY8dx66GdCNA4OsFHuSF_2PxpwSQnBy9HjRFaILvsEwdnlzyNv3fO6w49ptpKDQbI63qLnvyw-gdYhzT0KB6ko9wrK2IRkbP5oIdzPokYBoO4eifajLqzvR1xJ9peBRZxgxuEKFN_s8RKS7NezbGdU8973c4291XPK1YeTkMmIWYzs8WfcdkDdpsm_FmlbC0ELVyqtZBaVMITlo1Vg7-gMUQGHSwQKrLNNVFmAmTiOrzWZZpwGTNdQ7UfWgdDd_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Nn_O3AkaEJ0nlOLMVbaq-I7bmm_Zmvg3hRWm77dpLRH6k6t4WXEQbBMbNqo9xNKW7NN8nEDChvSbHk5ks_IR35ASSd-lIkPs6CU_YEasCkoeBPFbp3OZnplPoVoGWECUN0NZp2isgFeHdjZFUsE7Vu2BL5m1DgfOO5Cqc2cAbmlKyojgYR7Ou1UdnNjixfIWcTuEjz2pX3PaETKf27xCNK1B58_tBNsaTHwl2Iu4FbTcufF06bJJYe3pA-HlGd9k8RG0JIwv_ffGgYlyn9M6N6oB7Ps9H5en5Ixh-w40njPvphdmvUN4e6zYkBq2c5pG727Ld-P_4He-stOqOKX81A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Nn_O3AkaEJ0nlOLMVbaq-I7bmm_Zmvg3hRWm77dpLRH6k6t4WXEQbBMbNqo9xNKW7NN8nEDChvSbHk5ks_IR35ASSd-lIkPs6CU_YEasCkoeBPFbp3OZnplPoVoGWECUN0NZp2isgFeHdjZFUsE7Vu2BL5m1DgfOO5Cqc2cAbmlKyojgYR7Ou1UdnNjixfIWcTuEjz2pX3PaETKf27xCNK1B58_tBNsaTHwl2Iu4FbTcufF06bJJYe3pA-HlGd9k8RG0JIwv_ffGgYlyn9M6N6oB7Ps9H5en5Ixh-w40njPvphdmvUN4e6zYkBq2c5pG727Ld-P_4He-stOqOKX81A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=PI3VQN1u3MITZpSmTJ_ZYDrfIEm9iNDHUn9f10zhhayNN4OoQ1MVGf_nn4cvb-fjdNzL0hDSe_a2ySVDkEQnoeRFAPjzQIzEaqdJkuxEyv9F6Gfm9lLl-Jb_nil89r1VUXdWHocufyRMDT2NVh_0uqzEwNy5LM9oRI15JVnznPboLxphg8H2fKjOgE9MiFV9C1ub1_t3fmnu8eFdk54gUTYlGMBJTj9MZxZiritUCh7Gvs_u8sGKRk6tENHNM6g1Tvmbqsmu7dRreT-dCyBwgu528fR0kJKChyX1IYdtyjZJO_onwDYB1lRceHbtMv4GFt26PW6WUmFyH1wb3bnQSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=PI3VQN1u3MITZpSmTJ_ZYDrfIEm9iNDHUn9f10zhhayNN4OoQ1MVGf_nn4cvb-fjdNzL0hDSe_a2ySVDkEQnoeRFAPjzQIzEaqdJkuxEyv9F6Gfm9lLl-Jb_nil89r1VUXdWHocufyRMDT2NVh_0uqzEwNy5LM9oRI15JVnznPboLxphg8H2fKjOgE9MiFV9C1ub1_t3fmnu8eFdk54gUTYlGMBJTj9MZxZiritUCh7Gvs_u8sGKRk6tENHNM6g1Tvmbqsmu7dRreT-dCyBwgu528fR0kJKChyX1IYdtyjZJO_onwDYB1lRceHbtMv4GFt26PW6WUmFyH1wb3bnQSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vD5ThH9Uulp8ZQNFDzNQKEM4d5hBexG2NhXI54AU-CzKcBf99mVjafl2oiiNN4XBlJLDocm-elYHtxGUYhdtajCPmZjsfpDsxC5qYSHWI07ELM9lk9NrSesbZm4K6LwAouRB8cD5TxcbtuV4nTzFVALQ0jeY3QfeuOyOK1w8OY4QcTslLm9joCig2hHJsZnUrV-mroPMA5kAoEXF9zIZ44Mfq-LYja-zNZlDZVP3RqhYmQnKeZu_Q40oZekGfHOAuY2PMhoStOJf2qyHAlpvlrjIKEvBi1tF4ELgV_d18H_7Y9J8zcyyPilOrY2_vcbhMSB40MZUlgQG1tUS4M4DvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=iX3nZrN4TXF5yBlbXU82SIZwM-b7FqZSrKDEuU9O27YsAQX3Qv4rOP-gNBaiTioHwDMQVZP9RgrMMh7jIvlksthdoZbNur9ogDcQ5voN-9I64KnxWy7dgVZsyzIMiGAMeUkHZUj_TRF8eSmA2GWXGRLC2FqHpv4GPl4ZIiOuHzuKOmipQdwvvCtZGcD_YMNE7ZoKBOEEiledFeqsjLLz142hKTUH-uWA93NVWcnWG0U3zo8wp7uV9FPoMa87x-xkR9h4V5Ooi73zPjWPwaRme_9zDdTb2iNhmXzrvk6_XSvhTcbzrh6Fpttw7heJMt3wHVweesDNjDnsK0Ac04ZRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=iX3nZrN4TXF5yBlbXU82SIZwM-b7FqZSrKDEuU9O27YsAQX3Qv4rOP-gNBaiTioHwDMQVZP9RgrMMh7jIvlksthdoZbNur9ogDcQ5voN-9I64KnxWy7dgVZsyzIMiGAMeUkHZUj_TRF8eSmA2GWXGRLC2FqHpv4GPl4ZIiOuHzuKOmipQdwvvCtZGcD_YMNE7ZoKBOEEiledFeqsjLLz142hKTUH-uWA93NVWcnWG0U3zo8wp7uV9FPoMa87x-xkR9h4V5Ooi73zPjWPwaRme_9zDdTb2iNhmXzrvk6_XSvhTcbzrh6Fpttw7heJMt3wHVweesDNjDnsK0Ac04ZRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GJMIuYLMtNdWa_8PLKWyPIYGC5zcZu_WYLDOOyum7JOpYJJEdimA_dJ-WGJ6mXOEEiOf1aRH6aLOwzaN-35a7KuivQLtuGkOG6viXhmvvhZg7T0R6rlbRQRANKBIaoA50REpJG3fuV6vFIjppprEkYQ5hEgphW26lW-t8Ow7S-sRUFskluAn1qCoyP_52-5x6eCDbpKXMEysKbmVNnHrBZvxjETLOmYJD47Mb80_3AFk9aLSarjlU0lpSVL42nQznimFit2g_ALMllAmthxtaH23tZoca9eSuPk4l_1D_9Y4zNn08hWq09Cq8Q_lugnEZLJDa8nFF9RWV8NTWEammg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=GJMIuYLMtNdWa_8PLKWyPIYGC5zcZu_WYLDOOyum7JOpYJJEdimA_dJ-WGJ6mXOEEiOf1aRH6aLOwzaN-35a7KuivQLtuGkOG6viXhmvvhZg7T0R6rlbRQRANKBIaoA50REpJG3fuV6vFIjppprEkYQ5hEgphW26lW-t8Ow7S-sRUFskluAn1qCoyP_52-5x6eCDbpKXMEysKbmVNnHrBZvxjETLOmYJD47Mb80_3AFk9aLSarjlU0lpSVL42nQznimFit2g_ALMllAmthxtaH23tZoca9eSuPk4l_1D_9Y4zNn08hWq09Cq8Q_lugnEZLJDa8nFF9RWV8NTWEammg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=A_CtWf9uIbSU8ayIdJBb12T6GbXlaRoad0P5vXdjsCE-r-RaEk3DMA8SpP-mpniu1sElSeQ8RT6CPBmTE_g0MWAJ0_hja9phMCCJTn9hqohHAEDDPLh8sqxZimqjdcWzsD3UTXvP0oiFOESVcnKfoFrliDUgJtDHdAdUx7EOZRiIrxT-zwKCPVoBXeKsm6L-Ibjy-dToiBjFOYzNDiAQyrGzivbsNQDI_bRbxHPBSGwPpX-DMt-CK5q03JicAFAU1m8uw-gwRFvCCT_iMMqBr7jP12P9hSNLwmk5iXnmfgZbZ7AlTUuthLknUZpZoh5ET40qiCA-uUBTZgyud8LMSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=A_CtWf9uIbSU8ayIdJBb12T6GbXlaRoad0P5vXdjsCE-r-RaEk3DMA8SpP-mpniu1sElSeQ8RT6CPBmTE_g0MWAJ0_hja9phMCCJTn9hqohHAEDDPLh8sqxZimqjdcWzsD3UTXvP0oiFOESVcnKfoFrliDUgJtDHdAdUx7EOZRiIrxT-zwKCPVoBXeKsm6L-Ibjy-dToiBjFOYzNDiAQyrGzivbsNQDI_bRbxHPBSGwPpX-DMt-CK5q03JicAFAU1m8uw-gwRFvCCT_iMMqBr7jP12P9hSNLwmk5iXnmfgZbZ7AlTUuthLknUZpZoh5ET40qiCA-uUBTZgyud8LMSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=kXwuq1WstofTYb2Rq7U35JAMy8Yh5bqAEtr0lm3zX7tCEL-gGff4f-sr7ZNY6xAwfO24kSwu2m2j9FILU8jSh9OlL44X3u0kEkk28fkxjWMS8uYy7d28vsGEB61jFqtWS5d4IazoMtUMJ9g5eXKmjFSB_CEBvdeK3jqz0zjGe9_giBVYPEXWIj8gCKN0xT9F-hUeGUZm8HuuE2J52FZtBDEj2TFwZ6YdRu_fJdEZLoX5tLkVpEV6ZeqKlmd6TE9a1W2_Fqj7CVakT_3L7o9BWaFrqk33WRGyE-3E1eCMVEuY5T0boaxl7pY2iiac_OtwSTbsgPA8P0wvoOyhsFgDog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=kXwuq1WstofTYb2Rq7U35JAMy8Yh5bqAEtr0lm3zX7tCEL-gGff4f-sr7ZNY6xAwfO24kSwu2m2j9FILU8jSh9OlL44X3u0kEkk28fkxjWMS8uYy7d28vsGEB61jFqtWS5d4IazoMtUMJ9g5eXKmjFSB_CEBvdeK3jqz0zjGe9_giBVYPEXWIj8gCKN0xT9F-hUeGUZm8HuuE2J52FZtBDEj2TFwZ6YdRu_fJdEZLoX5tLkVpEV6ZeqKlmd6TE9a1W2_Fqj7CVakT_3L7o9BWaFrqk33WRGyE-3E1eCMVEuY5T0boaxl7pY2iiac_OtwSTbsgPA8P0wvoOyhsFgDog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grtLrpuPMISc9zgfl69hdCs4s9Z9vUt_7_QU4kU5o2uDhZkozUVB9kuoBvrt-AYOGXskH06AlXIcaH3S5N3Igap41HZswmlzpGKP54pm3CgdoEx7HNuy4UIxzJWejd_z3j6IvacWLu7kf5Leqt6YSk2imdKTqyDOKgSoBe37R_wUDC0Oleh6XFN3xwnFOMhcZiKHh9rM9lKXHhcnEyHzEAhHleQrqrDuxd_K-Bu83TpqZ_tQHB8Zvgnp0gpLqCbeXLLst-jIHBckWaod9xpJwuE5iMAizYVLeEF25t0Za0IcM2Y4j80dGNhA4ZxtdHSp6dryGWWoQ6ljgFY6-pa7nw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=C0fg2-hxVj8ryZ_fbTRH2faE-e6joQh0fG5DhdvoJbFxjflso8fnfCFprFWtkr6OFQ7gRfBYYzrolKiq_mqKfd_l-pgnRee1bUMLdLVfg_p1YDNHjU3qetOI_KGGE_aiLcMYGpLkjZEX6u1mHKY1-lNLnOCcKF1ie5vNrJZwM0yqlLQrOIU4OYvWPmP4UcMrrV2iS8jy0YSDuRDcrxcu8CtXaXySkbIm32LHH4Zg-GPgGPSHhlFv61_b3mbVPnbzzK9emEHDhiK1IEwAa8aE7IQbLMqFlQ-vHW818mm3jYiJcXP-0VstHIlX7X0nE7tXCqQHRhWooBJfNqFlpz7jK4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=C0fg2-hxVj8ryZ_fbTRH2faE-e6joQh0fG5DhdvoJbFxjflso8fnfCFprFWtkr6OFQ7gRfBYYzrolKiq_mqKfd_l-pgnRee1bUMLdLVfg_p1YDNHjU3qetOI_KGGE_aiLcMYGpLkjZEX6u1mHKY1-lNLnOCcKF1ie5vNrJZwM0yqlLQrOIU4OYvWPmP4UcMrrV2iS8jy0YSDuRDcrxcu8CtXaXySkbIm32LHH4Zg-GPgGPSHhlFv61_b3mbVPnbzzK9emEHDhiK1IEwAa8aE7IQbLMqFlQ-vHW818mm3jYiJcXP-0VstHIlX7X0nE7tXCqQHRhWooBJfNqFlpz7jK4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=aGSJjrdzV4IN3taEwxopeU6GoSXLT7vOX8_13fbe1-ma24aHvj9UuccbtOLDRDFl5e8fzds2dBRxTNtY_gz2Y_kFt3Lnu8rTpeX6pWU4z5XeHu2uiEtatIYZWvTfWX5kYakvrMqqu26o_Qft7REjdpV-cLvM2zus9npKg25sKdzJ6ati2lMDJdeQqISVKa8BKTOwAZcgmqrl8c6tyMuIXQNNxf_x3CI86kPrlGYsp8GPFPJLBXICBFOFh0nEZAl4HvCDX-cQOE9QybJq7zQ8hhZ0bG-_-SHdTKqqiXxyUFr6rIiFaO3Ce0fJdVSMRd6dTrCElXOrd0hszKTW4nUVHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=aGSJjrdzV4IN3taEwxopeU6GoSXLT7vOX8_13fbe1-ma24aHvj9UuccbtOLDRDFl5e8fzds2dBRxTNtY_gz2Y_kFt3Lnu8rTpeX6pWU4z5XeHu2uiEtatIYZWvTfWX5kYakvrMqqu26o_Qft7REjdpV-cLvM2zus9npKg25sKdzJ6ati2lMDJdeQqISVKa8BKTOwAZcgmqrl8c6tyMuIXQNNxf_x3CI86kPrlGYsp8GPFPJLBXICBFOFh0nEZAl4HvCDX-cQOE9QybJq7zQ8hhZ0bG-_-SHdTKqqiXxyUFr6rIiFaO3Ce0fJdVSMRd6dTrCElXOrd0hszKTW4nUVHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lH1s12D324K5nbNX9Br5nUjGYPvPj6EyHeKWHCJYWsrRAwCHjjGK3fjeoEn6GQy3IZoFSNJPib6eR_bT28MO3Rk8IkPvah9jVZSr9RzjXj7CEkmP-Hh0WGAszrkECmwhZHjDdMhib7EZ75Igc_T-EnjKuZ-wl58oVmPFQ0aCFApmkE81PfwkWnyM17On1LrTZSopBRfK3iIb-WtHiCyXcs_wlj62WFGLXe69YtIiDozfx4Hc03k2WBlyxVjx3j5J9-UzRPXICVngRaDlUKQlN0YW2hk5VixkIUy2hJ_Wptu_B8slnn5GmUxraP-WsbJ8EMxfYLIkvFqC_d8MnL_zbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CCfvNzpv3JerTwckaITYC4zSF3UxRpXKfXZSrmhZ75CZvcZb7--Q4YF_ibbG7PELuTM8461raR7HZ0s8BGmCcwdU4vzFQXrzXVZJkDyRKFikDFcKOH06km4Qzflcf2jwiWAJbLniGPnQ-R2w4FOBI8g9wFZ47u7V1gPSuELUCdek8ocucwNXB6Apk7dDW-1SJ7EixRShGiqDwCpSzZfqvvntT_tVo2B9gFnh_3IFuY2UZs1cGiOfczw6LsncOoY4gswQv5OfYS4fmhS6y7Q6Elp4ssQckYz6hlVkMO7aKYbIPQxS0DVKayNnB4rQSTvpIo6jrwBYXpONI8TVEuisZg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=bhZi773Ehaz0c4cpkNf95_xqnArLzqKPZEoVCPzJoZVEYWKkqsv8Tnt_XRCMypUH2XDoPv_wZFjYn7b4SKMuce5hWAQGq_vstSNg4bADkPZ6sVfJMu29B5WNq2L8v0XHUGcDD994Dv4cU2nQHd_Z-MaLRe8bOD881iGAI_-wjlGrufrrSDlM7qmPnq0O5lkUhxQbITaNU8c93YsnJC1OhY9SEBHkVCwDrykewfn2aq3OdlsrisAIhwByPZ8EVfZWeCofIKDgp0SO87WlMl8lA-ygghzV_PzgdblunkSbglaRQc1kreGricY3C8j6NhxgMdeR52iwDw-DeyKJ14V46Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=bhZi773Ehaz0c4cpkNf95_xqnArLzqKPZEoVCPzJoZVEYWKkqsv8Tnt_XRCMypUH2XDoPv_wZFjYn7b4SKMuce5hWAQGq_vstSNg4bADkPZ6sVfJMu29B5WNq2L8v0XHUGcDD994Dv4cU2nQHd_Z-MaLRe8bOD881iGAI_-wjlGrufrrSDlM7qmPnq0O5lkUhxQbITaNU8c93YsnJC1OhY9SEBHkVCwDrykewfn2aq3OdlsrisAIhwByPZ8EVfZWeCofIKDgp0SO87WlMl8lA-ygghzV_PzgdblunkSbglaRQc1kreGricY3C8j6NhxgMdeR52iwDw-DeyKJ14V46Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HajjHXuW5wUQb-_Ry5HeE4QYLmPfEFhsW4lY9roFcf1FVnMwCKQEDMuSx80ZUwFRFynq9ecELTLXRu8NlZmii9ygWhSbsn2Rpc-xMpHqe1rYE_AFPfUH_AOnAXJKtaOd3IaLm3won5HAKhWhJRTwO8MXuA4dAcAj16PYjR7n8julmKgXyBjr2LD1fLJDe8PpcNalTXj6m5lZtiNleq-qWF8uVYcwKImn_D5fr83jeR4_C1XNJ7lXLuMxpqYqTNfWsBzHm5U9BmILgeVXvxD5kpf0rijXAeCUYRGbRdreUs5iYrFqIfVx8RM40Ym4ydattP3X20Z_YVRbBFIz9uNzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7qifzCGGaoI6R3kGdEuc6L2BMmXOIDXEDLKjE_JnBB3gTlUh-9K5cLIC_qwvKdmW73_13hu9nx3CX7ZdMen4IrGF187DUuXDNbHLLnkguPZGdaKD16ONh9w6aokNEtYPrhZoNFV5_ldb-wDqPUKk9u5LLukxtKjQsWHEifXQSeejIA6YjYPRY4uFR4dpaOjPxA6gLx8jQCe2UgMosTsD9wALsJUolLgP1vY2KMl4VSR2GdFBFWJskccEALcCmlZb0YWs4IsYGThtN7lX8J_m7bkR1AnL6DsmJ3YsVrpIz3XBW7w3XgqdwuZhZjXU9DVDsVBFRZ4DUioj7YG8cRB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy8Hj--znBiSoPAhtlxRJXxJMEmImcoiuS6YABmaXYq28RzTAPgqt8ShNcb_Q1rwfWZGmknCwxe2gD4Ss8cYOmIVl7ZhqKSdcmHd9efASU7fuIAc9c3H__H5AAfqwqVKOrkPGSHJhc3yUnJ0CZ6dRWVt7ZT_3w2wyQdiUUtuw8wo2Vl-VRHZfSejHV7HJkypV0lD_gyZPaAjQfTJ6v7_rdlwzRsMB9cgS17GVqNA99fixsRq-KTJ96REzrIuagvoD1pNh5g88dRGxl88hoB6VSXtqoS_0sEfY341sEPcCQgMq5BItHAGr8OXHpE4b3_NiyRz_oP5Bbe_kmyt998R3A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ebEQgDQ6I9yuMUJenX9D26nBb1QpJm-cNd0dRtGhXPk551_DXxQQkxatOskwBnaqp9j2Ed-L7Nnak1uomNM22rZ0u5rbINDqXWztIQ5Ut71yeHYlz2O2jssSMSWvPO4wvJPtf1Zaa6LEbayoWPbBTwTgqOKqDSjBJ-pGjpqfEm71C9zo5NiriuwYQz6M4-Ow4yc7jmzYBPR0z4DyAwd-bBY7mK0Lccm_Lt0HZ4TSQuMtKcGVPBc93ugBp0ZcoopwDlde9QMSG_b2E_xVGIqgs7F6SDMzHXiDb2GllfxqPuSFSk9MWPSQwWGl_pkssuqDJIUs6X74kE71o0MDj0Y9gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=ebEQgDQ6I9yuMUJenX9D26nBb1QpJm-cNd0dRtGhXPk551_DXxQQkxatOskwBnaqp9j2Ed-L7Nnak1uomNM22rZ0u5rbINDqXWztIQ5Ut71yeHYlz2O2jssSMSWvPO4wvJPtf1Zaa6LEbayoWPbBTwTgqOKqDSjBJ-pGjpqfEm71C9zo5NiriuwYQz6M4-Ow4yc7jmzYBPR0z4DyAwd-bBY7mK0Lccm_Lt0HZ4TSQuMtKcGVPBc93ugBp0ZcoopwDlde9QMSG_b2E_xVGIqgs7F6SDMzHXiDb2GllfxqPuSFSk9MWPSQwWGl_pkssuqDJIUs6X74kE71o0MDj0Y9gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=iXPEV_QST9DNk8fPcOglU9IkQI_AFuznCU_GQ2xSLfxKK9h9C5_-iBQrZ4QjdI2Cigq9ZsvSD5GtcL2vUx9PVHXISckxBdGdSiQWSK76WHgSOtSLQH5zjqqOJGDTnBdFtvCeincsaDAJroM1csQptydG2ChIC1p-WfwsqTE5D9p8bGnDpj9b8HwRGELOcTFkUPLFsFr-LGsuTvrfAw1BonXJWXozN0TygM-8HuzqXFW8G9-ZPl5ArNKsb-nTubv47lcS7_buJjxersMeOqzl0nS2etsb6iiO_F3qMm6nJkFTzgbTgkgpHhJli5PRbuZ9JfP9Sg3OzYkxFQpyZSZrJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=iXPEV_QST9DNk8fPcOglU9IkQI_AFuznCU_GQ2xSLfxKK9h9C5_-iBQrZ4QjdI2Cigq9ZsvSD5GtcL2vUx9PVHXISckxBdGdSiQWSK76WHgSOtSLQH5zjqqOJGDTnBdFtvCeincsaDAJroM1csQptydG2ChIC1p-WfwsqTE5D9p8bGnDpj9b8HwRGELOcTFkUPLFsFr-LGsuTvrfAw1BonXJWXozN0TygM-8HuzqXFW8G9-ZPl5ArNKsb-nTubv47lcS7_buJjxersMeOqzl0nS2etsb6iiO_F3qMm6nJkFTzgbTgkgpHhJli5PRbuZ9JfP9Sg3OzYkxFQpyZSZrJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=k_Y-k-8HOvn_sXXM8ykg_fPTSQXVHLvHQE-2F6cKyYStW11uxNc9t3KaVHohnxFaqDGjECjIAbRIFLAaFIugDJiY2ldhHE3SFz0DTLkNRY1D6PoRG1qbdk8rhHTKcZumSWf64xPZLFWiEE9HiPFuIRxBjf-qhBcp6PqrtElOISf87iqPCRaFVg-JfGoek2gbfTQakDXh1v3c3wiu2WHoSAqOlhSgCmFRT6ebNWgthT8ysn3VaWT70G2m-CM5XTGoBywC3BQt0Ir7xJOtE7a4OIJDWkcyElyIK917TPBTm8Ik8PS22DANTwlqkKY3xMSLlTs2lb5Vcc0didnr0HwTZylExOMDbZj76ve-gPK1rn_BO8HdXpzkSlpoYxudEyOCyGzfMFsU-kLHgDQsybSKOYbriqKgVSlTOjVlaiSXVHHzwyDvpuDYBeWMy7OUUNYyBkIb_cFhr_d9HlA4MTu1KprNNswb9wePo49oP3MWbm8GIO99MILpjKopS6sYzE30nIs1O4fR8p0G436Y9nJODz2Np5yVIWGdyTp8FRrRGPbdwERjWNvlq7ExZMBcXruxgeNOSZO7rdXCQC_xCvgBz3Iwp7tmmMrlFvL6HcbxqFYjeZPI9PXoFeNN6FU9n5CjfQ2dgP7DcthNoUczJPC-oFJiGHlmak18SPGsRtnk2Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=k_Y-k-8HOvn_sXXM8ykg_fPTSQXVHLvHQE-2F6cKyYStW11uxNc9t3KaVHohnxFaqDGjECjIAbRIFLAaFIugDJiY2ldhHE3SFz0DTLkNRY1D6PoRG1qbdk8rhHTKcZumSWf64xPZLFWiEE9HiPFuIRxBjf-qhBcp6PqrtElOISf87iqPCRaFVg-JfGoek2gbfTQakDXh1v3c3wiu2WHoSAqOlhSgCmFRT6ebNWgthT8ysn3VaWT70G2m-CM5XTGoBywC3BQt0Ir7xJOtE7a4OIJDWkcyElyIK917TPBTm8Ik8PS22DANTwlqkKY3xMSLlTs2lb5Vcc0didnr0HwTZylExOMDbZj76ve-gPK1rn_BO8HdXpzkSlpoYxudEyOCyGzfMFsU-kLHgDQsybSKOYbriqKgVSlTOjVlaiSXVHHzwyDvpuDYBeWMy7OUUNYyBkIb_cFhr_d9HlA4MTu1KprNNswb9wePo49oP3MWbm8GIO99MILpjKopS6sYzE30nIs1O4fR8p0G436Y9nJODz2Np5yVIWGdyTp8FRrRGPbdwERjWNvlq7ExZMBcXruxgeNOSZO7rdXCQC_xCvgBz3Iwp7tmmMrlFvL6HcbxqFYjeZPI9PXoFeNN6FU9n5CjfQ2dgP7DcthNoUczJPC-oFJiGHlmak18SPGsRtnk2Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=HQr2ZPLAyIpqu3zl_FnnxdeaFb-8mVQNv3X9e7lPA2pVzq9gbgfxXmNyYMhPolZnaRx_L9P10sWCgwolAV1rFcZv5vX3r7s2v0CL2HlGNZS1LXyvL6NYgCcu742DW-PR8I8ijJmjvqcPeGIuMbdPrlmqWis-YoQCKzpoKANJEcropCVihew2g3MEcUUTpxojjKt2nSl_GsTj2ycecJga7E_0ewkjKZ_X3SOYcM04JdHXhnWORLw323M-GrCqxQEkitMEqWYTFojY-a8wxQzoXnPRNEPXrkwQT6h7B-tfLzd2fWSOjS1qUUe8piL6aWQJf5cR6nM7FkyEuFQl6z-VSznu4rR6Gkt2orftqnuzl5_dGx6mtZZS8KhWiXswAcJDu59_JmsRHFLMmpGJuU7VykxJrYeDn6WtLLIH7K2lHYz8Db3bUrWuCW8_yMsvHjr8vCa--lB0xtkHSiWIRCg6EK0GPOfKf7_JawzQurxxNSQYIGfXoPhwlB-5oTQin26GrPQ5fQM85_0MYVVkcLbVZRNQWRSSP3dmzPP8iitRkyTeiMUKgkNtl8EMjZRKMBryXyigwjBbLFIibtdLX256JKiIPCmEOKXXm92V83SjJRiDixiu17eTQ7izeP0opMjxYni7iXv-snyz1TSdNhxVWq-jfx09x-zc5NFtJuM7yoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=HQr2ZPLAyIpqu3zl_FnnxdeaFb-8mVQNv3X9e7lPA2pVzq9gbgfxXmNyYMhPolZnaRx_L9P10sWCgwolAV1rFcZv5vX3r7s2v0CL2HlGNZS1LXyvL6NYgCcu742DW-PR8I8ijJmjvqcPeGIuMbdPrlmqWis-YoQCKzpoKANJEcropCVihew2g3MEcUUTpxojjKt2nSl_GsTj2ycecJga7E_0ewkjKZ_X3SOYcM04JdHXhnWORLw323M-GrCqxQEkitMEqWYTFojY-a8wxQzoXnPRNEPXrkwQT6h7B-tfLzd2fWSOjS1qUUe8piL6aWQJf5cR6nM7FkyEuFQl6z-VSznu4rR6Gkt2orftqnuzl5_dGx6mtZZS8KhWiXswAcJDu59_JmsRHFLMmpGJuU7VykxJrYeDn6WtLLIH7K2lHYz8Db3bUrWuCW8_yMsvHjr8vCa--lB0xtkHSiWIRCg6EK0GPOfKf7_JawzQurxxNSQYIGfXoPhwlB-5oTQin26GrPQ5fQM85_0MYVVkcLbVZRNQWRSSP3dmzPP8iitRkyTeiMUKgkNtl8EMjZRKMBryXyigwjBbLFIibtdLX256JKiIPCmEOKXXm92V83SjJRiDixiu17eTQ7izeP0opMjxYni7iXv-snyz1TSdNhxVWq-jfx09x-zc5NFtJuM7yoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=oAd1YC0so52gBh4d23LSyg-Hb24ef_OIq6l_3SssMaZiAIOggoucTl4qZdOIqZ4PPBGVDv3L0VxWsy1FkC99M-GcZL0oF6lfHA0XT_tPkLSDSct_XMfI9_KyA4_7Rr91-TUTr7lxZAoEWWxsjLCFmqZT80kqh25oHHsxRYiCZ8StF0A5egv93ujhKUURrdhwioALRFDdYhlsmshPE2QiQK5Ec_VJ1iaXHivnbJeV9Odb-kAcUZBf5mAHoV1MPC-4OloFXpge6ekdDDi2TfAzjECKwTClhX9h9wGqV81D8BmxOOTXfGSjfGhT9Oq2e0Anp5LnXy0xdaDdd2VnQC56eQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=oAd1YC0so52gBh4d23LSyg-Hb24ef_OIq6l_3SssMaZiAIOggoucTl4qZdOIqZ4PPBGVDv3L0VxWsy1FkC99M-GcZL0oF6lfHA0XT_tPkLSDSct_XMfI9_KyA4_7Rr91-TUTr7lxZAoEWWxsjLCFmqZT80kqh25oHHsxRYiCZ8StF0A5egv93ujhKUURrdhwioALRFDdYhlsmshPE2QiQK5Ec_VJ1iaXHivnbJeV9Odb-kAcUZBf5mAHoV1MPC-4OloFXpge6ekdDDi2TfAzjECKwTClhX9h9wGqV81D8BmxOOTXfGSjfGhT9Oq2e0Anp5LnXy0xdaDdd2VnQC56eQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDuBCveP2prOiD1i2t5PZqu9AyfIA35mneVsCd2Kq0-Tiu8E0InheoYcFthtAmP7Q4V8z-AY10FUKi0EhrSRMPqSPhFzm_h1DO-CqsdPVye8tDdlcLVfFA6cgv3DuKuI1uZzGGF8tK0AYN7gjquE2cBDPOGLUNVmoRF8t4_R4Jh0hosD8aAz9ZYWDeM0B4hE_e2kSLGs3BYnP2aPafGWZXZ_G6LUCeuXUdk8PvTYHOc8Ivx-1BC_R5hJaCBzPIoCe2NdKvAT3hyoe4k0pK97W8BalB1UGrrRKQlw75f4096QO44Xcjtwgk__2NMZSocJQe90M7D2JqRKPSDxJVOYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Kye79a1z7Vjik3Yb2REGb8bmaLqozbBF12y5-Ko0b4bGs-jsTl8E_XZpfSi4qy81mGvqqWuLohEfbFTcE3eOw6fJc1iLEsgtRYiLK8twwsrOKPIu6tJlzoRgvc1ZfB1YTCHkCoJz_278IURTViuD3L5tR5QivbBRvrHLUbsu3ApEV5WBO1Kmwn4Ft6bktdPrecOYBiYNX2y5QL3YthUn-TNmohGqXf0ctLvkPuiV2dYbRodiJ08LbULLycUb_JqWB56jCqeSm85TZaPpdWXsPhtkpefokQGDGEr4KuT4BC2mQP8koDqDq9ZrIGKfpuF1IVVbRedEebm6IK5xhIPbgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Kye79a1z7Vjik3Yb2REGb8bmaLqozbBF12y5-Ko0b4bGs-jsTl8E_XZpfSi4qy81mGvqqWuLohEfbFTcE3eOw6fJc1iLEsgtRYiLK8twwsrOKPIu6tJlzoRgvc1ZfB1YTCHkCoJz_278IURTViuD3L5tR5QivbBRvrHLUbsu3ApEV5WBO1Kmwn4Ft6bktdPrecOYBiYNX2y5QL3YthUn-TNmohGqXf0ctLvkPuiV2dYbRodiJ08LbULLycUb_JqWB56jCqeSm85TZaPpdWXsPhtkpefokQGDGEr4KuT4BC2mQP8koDqDq9ZrIGKfpuF1IVVbRedEebm6IK5xhIPbgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=hgASj0YOk9ZuYCJPxBb-MGOSnaq-VE7N91q8t59ongkvoD_ErDZQJY8chEvYhCuUWRrUNExEsLaymteNXXuVNuVrX2ZqOlYSJwzK8UUqB6-Xy87RgDu3lWmG8555UKpYv4T-63L2rQYpUgYeNaYx_wMFwNSbed08OxVpEt9OjHhou21GP5gISRayzJIXOsztKaTVD7iOs4mNDSERrnfTIlkkNyc58PaosGKZoSNEQ-VIcr1LpuqOqMNuTbW5tObNCroitA2kXWuwwT82GbPwcEtyoOYoo3l78Ip0pUvlL4Bzf56dNrq8i1_p7g0VXq4igQrx3gbK5B-Q6vMaF6AdYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=hgASj0YOk9ZuYCJPxBb-MGOSnaq-VE7N91q8t59ongkvoD_ErDZQJY8chEvYhCuUWRrUNExEsLaymteNXXuVNuVrX2ZqOlYSJwzK8UUqB6-Xy87RgDu3lWmG8555UKpYv4T-63L2rQYpUgYeNaYx_wMFwNSbed08OxVpEt9OjHhou21GP5gISRayzJIXOsztKaTVD7iOs4mNDSERrnfTIlkkNyc58PaosGKZoSNEQ-VIcr1LpuqOqMNuTbW5tObNCroitA2kXWuwwT82GbPwcEtyoOYoo3l78Ip0pUvlL4Bzf56dNrq8i1_p7g0VXq4igQrx3gbK5B-Q6vMaF6AdYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPzdn2MzBeZqcoGTuYxYF9PTIfUkPJKTJH9Km064yRyFGxAb71O6yVlJolHIQ6E91JNWpPUkd1bsvo7IkVzKxmtc5f2Y3x6K8bkpZTdd-vaeMnyZyar97nNHYovqcbKs0q5LbqvUQkOuwCwT6ps7cbSwfJuo1GDSL8_bQ5GHGn9SHZJ0BTSy9aXC472_OVxFAoZB96IPSBjLR1Z9BuhgEadYgjLC7FAy4KyZXamHS3Zyghbz7ZIVK0zTeNyUrgi-5jkj1TlMoO5yofBxjf0aSG5W_JL9hPo1wzauxy5cgXNDAa-f991_tim_d-6H0lmu5tP0JK1tow6kBeetdt5KDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CuGgNghzkEmmCctsYfWuG9KcH4HszLSWE3RU3jbMhjF5ztnwvgOxpEpZT6DEQ3ba1V0sOk2-NSZV5idqDb4aiuelTb2vAyupcZpjqWDH6YE31z1GRUfNHq8W7XHto6waFY4S_lGLOEWhtM6m57qzzUxaHBZWRtvczRKhBnxql7fb5ryJFtGF6n9ddaGdL4e-bGD7SxcTB6HAyUIzXeARe3wvpHzIAxspzao9WAxQ6PrCO_Hx9v9LY7ITlmW_XU-7wrn4ql0gKJnXpCqDJpMcvlUmUphlNoRk-YYFJQtmyckZbRKHTgrXdg5Gdos01_hNeYC_LOpj8LwgHqfMWw7Bdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csRNvF2mkSVzhBjWVK2k01eYZCPlU4BhK3vXamZ-sBhFkPdH-avW0BajjRawVa7jju6pAIniBjFUESRKwB9qv4E1JZP9VBDdGYwD0L09PBrL6WgZv6LwLoN_OnUygO2Wd78lAQEk9qvPjb-mrGy0lWQRR3Ivd7u8I1qRJyaHHultMiMomqir-r1t0H6GrTDhBrynKjLPVjE-WJyQVg24k8PGwBb8j_vP0rKsTfDIBeyYwnxKtytrYgl9AG59RDSFSF2aG4QUx2dp7boffjqwMIA4gnHUFn4v2n0rVfox8_smZaivWpxI8Fjsq6ApFjZ027RFDo-kI-oVhGXBHvuCWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HMcV689R7nQUBjK4MB1nVFxxtWyAbBlCC5a7INaY-jlAeAjVbEOvitGPhNKFHJJXhp_FNZi3HY2mXaCeAv5oPSAznbdz1nU7THxij4KbawGR5y5Dg_iA1vwfbe6OQTqTTTw2UQrPJ8OOP7Sqve_5jftNjGCnAPJJSSJjP6GMGjYqWGJ1sWEBUxWfoyVdpksMa2vzc-I3-kRtnU3Dj7CfJ5OJO2xuTuOmhY736g73bB9ulEMMbnOwl_JuyleAGT_wwl0PrBiKh91pxHXJBQ_xqcZqOVFDH-BqPITChWutFY7lKf7s0nXj5Ac8q_schw8IT4au07J0_6uk299Tza_68g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b2VOSqyexToO_-ArPmcrBBjtVZ4KwWMIWbfN7jDnWkAHXxLsutdA7KaxHK-LwPJgW76o-tI7zBQHxm4nnt5tH9ucHtSLnqo-20lGWHV1iXansPZC6yLSvTNe-ogTDQNz0bZPNQTwiaWMxdV2WsDOMRswOa9b78F5ZMb49ekw0MgGR8GZSWxHnIEp_inO8xSXFeB4Ss0xWEK1wVzYwW3pesbPlgJTaFcGkMnjjNsJEa1gl6F0zQTLtMyB14Nuqk-MwyDEGhQ32CvOynhfw7WRbosKeLWZL0UUTtuwoZmoPcwclO_qkZjVPHKFIPGSDdkBKZlewMhBdwb20V8NcuQ-Jg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGRszHufm478DBfXIvKJjwjK0foFrj9OKS-J2S8lXLZjBLyCQ7oukCKaK5mJaSCYCjJ36vmavIKuhng21P7JQ7DC3pdRwpGTs-8cktmSC1AXmtTYcR9tJKD1rXJj_lQGyUh3r7pHIyJvu1v3dSIafR8_Qpi8UhK0gAV7wka234fevXVa8P1UkuexIW31BdWqFNG8SNb_gHSAYZUHTpD3z2HmlUWV-RbV6qIHiPaeiamkiXBlb3XXUM6vo4QqwkjbpH47YW1yl15UBWvauQ5d-MQo6aQnbjq52-c_bJMHjLHMyz0jY9Pe79HnvOAa2E3t0Su85psNLj-SW44_0i9CfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/COdP_GyURHiPy87KlvAXd4xxA40aAJTGGvk3rck5UruGGhTpwY5p1KUN9gmSB5X9TgPEDf-aaW4-28qcgDVmSiTkjMCqyUZ1POK0qQqFeW0O0PCYl0pTMBsulnrWaMvw2s10HKDa_d0sXZErvYioT0H5IVrC-06iqoT-xqtRCn3azVC5JCpmSrsctX4njGuuPLZKSEgtf9izIJUyGh-cjGO1EqIhAH6JELZbPVrLRgKK9kDTA4VRbo3_Jj7Nfi5ln8vzjID8XvkW_lPdlfGi8uBa8rC-AhjembxEm9ai-KkH_tjMFNPjgkqNXdWa9ZWA5OBnW-TcM2LkcNIIPQ9ndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFOZPLGnkwNsJcyGNvE8bRTboZUvJO3D0jAHBzYhA4x54Ek5bjhhmQpHyVlOoK-TbSePz7Wem-gkL4dQKVor-PjjpQlw20pG9zbQKP0YhWKUPuJrBByzpr1s7pTi-dt_qI0WYLNwvu1ZHcZxl8W_dweAwSPKrBQBPkXMRcqeVxDV1elqdkxE4b2vNxYI7t27V0ffJ7pRHC9tOyAcDZr0lKrsmMo4iCRT2l1ZI-venH9aG24OLvwmku5DPjGxNeFA5JDP09A4BfxBfUjDUzd-EUk9reCR8cmUMR0VYVtJFyPpjRDBbch14CAUV7xac5XiYu29lj9nONUvE9HVrLQ97w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EHZyILe8km1xOPAuFJq51r6_XsIPgyqdsQzR0Xncf4QBC6kiaUUOGZoQzR6Ho8ViBdEHgSg8hGF9pnOTTyYfUPmjQAK0bJTsoM3VJAKocQ8v8PElezlbR1QeRj1kERQwTeSPIsPsbUMm51QsiujIGhD7nwF9uUC_XW6yfoQBt7IfXDsjU2rfGrrlpay3FxTS-PSKXcmjt7Y4YZoRYP60hI5ICpyjMNrlbhL8r8qlZJwl8J9jw9Iw1svBawOUBS13ToORVgF4w34rOgL4YYpvJgF1MnBk0UZVacEL45XW-fOJMDq83IMqJYpL3oslqIzAYnx5AbmCQEdGKETTrGbI0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OaOwVhg37Rsq95wpskvrJ90vOOlrX6AHyR6jxUdpO-qPpT-5aC3F8rL6ou6JOpcYaVVCoUYK97RfKnETCp5fzMLJDiIA74fPRyXmgT-35Vabk8Nuc-z5XJVTQIvZVR8AS8CoiwxFjQpS0mZa9KPtkQDAHg34EsLC95CpFBjr9naFGDV7UFzu68vKw5FHxoOEf7fT182ajvcUKM9_ZEb3sJKafapcYxtoNmLmw-qtcO-JTyJYb2bBI4QehrY-RLWuQB2Qu_7ftukssATLAk3SSKwKhtMOTEykiqRR_9JYUTZ3Ip5KKhNX-hjttrUqWizx6-Fbkr7EyOciNARJyGbHKw.jpg" alt="photo" loading="lazy"/></div>
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
