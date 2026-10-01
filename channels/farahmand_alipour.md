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
<img src="https://cdn4.telesco.pe/file/n6-fUugsXe0iKAIfJ9iPtpahB8taKUpwUVnF2fYKqi5Ku3vWkeNov9CFwjcQgORACVpqXt9fUFveex2qi9ptp1_ngEp_Y4FufNulLouPgE8GxVNmqhTv2wBwc6HEyBYpi2OehvKGVVYQNybObnJLZGBVQg8-RI0LJk2JZQswSnUjaYHWn8NGWFtJZe4I_x0Ggs6B9sY8xEP4MNFBUn8sTs6maQ4t7IRPDEks5J8O3DRX6EtZrbNtqk5gQdCjB5_i6jjuQDi1TpDt5fLnhkWMWQfpWM1KdobjoDT9n6iULEEwEJIpPPm8YOmDpO1cKRjMhO5TJdbSgSoKnQJt8AQEqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-09 03:46:48</div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIxwKw9u1wKVi0le3sqPFXJ3CxsF1knfLf6mNDFc0QMEfDEnyoTWDWIcxmug7nrVAoG0YilGx548apFZ-Zj41EHFoTSW35j3jTyHyHTh_TShFp_IrNO7oqMxOgnInCivZqCMVJj2JHL71X9Q2ZN0n2NAyZwl7Yg-dFW9zpebWRNciy9cHlGdkVfrDgFVNRa0eCqk0QNhJxmA2TgITHvL9zof5OHPL4HglFUgbeNJIifrwDbPu38jqHL6PVnnJIwEw9yOCZIqhJCxLgLKIH0lBRgXa6naMBzoTF2dddu0otKs7BgQR8GS6Y2Lp6v18q3ExCve41eW8y9yXUgz8payoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RklkcfQFscNLvTRMtxfQDpX7HmsafMqDKZaOfl3bPp-2rEagjGovguMYT_RRgjX923HhxgveBTaPjtkafB54pI0XFnNvILVekEBd6T7bC6_iPFAG0X-N3IQN-8vjtcaMOZ1pC-yUgeodJozJGCxUZE6iq1-Y2sSdqwaliYu1sEXEu2-mFNKQnynOZYujDL5sLol7-JBT9iFUhRFmeHdJ0ROXN1YWLVUD1LjN_zNHWAltrvqyo2OXehiRoYkzguWuOahwbWVYBvrrrQQGoZ4s40BluHBkvrg6vf1-5_LGQ3vwvAS-IyzVdLUEOgAHgxLmv9xBRTxCOUafAetxsjk6JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
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
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UtH0058xIV8rNmAxOAMPfOuUSMsfuAYvcT3jFhfk3B1ZAY8qQ0T2NDcf1wi_iv4n6zpl_-Ex-oeZUZsdhPfaVSinhwMNUYdxGgYbQbQyHUsOBpq9q9gzcX1Xbp7qvfrathlmn4uonmT8uPsbewJgV8GERASwtWhVWh3P3Q278jZ2zl9aUjc5x61t07LUHgNWAECaJ8GBWV91GH_GAFJZ88kEDVd9-zsq8J6fxs4dJPMG4Q3m_ZfD0l-z1eNLhzFEA1bz-r694TzFcz5vBnVAOf2hbcrK4RGwht8kbm-b6xGJkp33s7Y1IBDu_Lljb2fwjXANoX6fnWhEANwSAqJ9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=UtH0058xIV8rNmAxOAMPfOuUSMsfuAYvcT3jFhfk3B1ZAY8qQ0T2NDcf1wi_iv4n6zpl_-Ex-oeZUZsdhPfaVSinhwMNUYdxGgYbQbQyHUsOBpq9q9gzcX1Xbp7qvfrathlmn4uonmT8uPsbewJgV8GERASwtWhVWh3P3Q278jZ2zl9aUjc5x61t07LUHgNWAECaJ8GBWV91GH_GAFJZ88kEDVd9-zsq8J6fxs4dJPMG4Q3m_ZfD0l-z1eNLhzFEA1bz-r694TzFcz5vBnVAOf2hbcrK4RGwht8kbm-b6xGJkp33s7Y1IBDu_Lljb2fwjXANoX6fnWhEANwSAqJ9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bLwfjWkOLfmNB3vHoDXdCt6Rb7PaungLdXnEO0OQ4Asl_vFhJu1lOhYWoHozFm5F6tXP9X29VWSyxpeVXmXBZVwMRkLOKjOzkhUeFFBH6-o-B8EEdMWLgXvZnhtXhsDLJHRG1wX6AsP6zdpebDWkE0JTCsCerT1Tw_aSTM6QH5RONrQCl97UdIkg3SOCz9BwUN73QjUdpgSxUaGAZPLHD4bJ2bq_i8Ip6uX5eueO3x8iPCUQ_xppdIsr1c65YABxDYd4tp8IhR1E-K4NwhXCNFBOsjsdSrCcUydzNHnzgZ9rsUVb8Ja-YxIgEmOO4rvXdg8oDa7zBPylExWIWyQytA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=bLwfjWkOLfmNB3vHoDXdCt6Rb7PaungLdXnEO0OQ4Asl_vFhJu1lOhYWoHozFm5F6tXP9X29VWSyxpeVXmXBZVwMRkLOKjOzkhUeFFBH6-o-B8EEdMWLgXvZnhtXhsDLJHRG1wX6AsP6zdpebDWkE0JTCsCerT1Tw_aSTM6QH5RONrQCl97UdIkg3SOCz9BwUN73QjUdpgSxUaGAZPLHD4bJ2bq_i8Ip6uX5eueO3x8iPCUQ_xppdIsr1c65YABxDYd4tp8IhR1E-K4NwhXCNFBOsjsdSrCcUydzNHnzgZ9rsUVb8Ja-YxIgEmOO4rvXdg8oDa7zBPylExWIWyQytA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKPgROEd_zajWY4A45ucZ3VfI7dCnVxWHAsR8gEZVwHQPqCdVsrVZP72f6eso6i2d3IzrcYhnQIFmHFxZ_4MNEV5IqyoSYS1cEhKii1ZNydQL-2pJriNuE0NvDkCOJT8dI11BzFbPsKzIoGZnohS28U-kwoA2uU4uXXz33euLEVIShFxVQyG4iOXfjf2bjtBAXU-9iQeDWfLSgQf8_Zr296Si2Y0lsrsmiyccq5Xmzr3zQJQcbT5ez_oTmTofFAIYv5nTe1SmWnq1jP3zTUPVYbREW1EHw2h10H5Pv1XaoHM47-MVWHl6nrC2NfMOQXxCIdhji3SxGM7yAYzDnSoXw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Ht0NaVWCJKQO6P2dVfZBnqKnOEPYTP1P7QK8dEQzBRnvDvfrMeOSE9MCqlxn3DGMrDw4PBXxjo0u67PxOEktzCep2lmWVta0CDi9Xr9TqWd7SlZNRNauBu_Anzq0Y2osIfDdiIQ5Gvq9kYM_yLwrYAsOyx5XxhNaKgAvsNbD9jPMD2RcJEjzEjl7OAXQm8WlM1N5dRj85N1FWU60E7JKOx_4EQeTf7uq7fAl017pY4gWFa3ZVuCrxvN92YZnLDN3ewTgtt__VJMtnBQJf2ePsaQjQqVwadXjR-Ol7PVgdrgxW3euu7YM2xQheRYYRp7tEqlzq3VwGE9FaDxL1VkjA0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8Ht0NaVWCJKQO6P2dVfZBnqKnOEPYTP1P7QK8dEQzBRnvDvfrMeOSE9MCqlxn3DGMrDw4PBXxjo0u67PxOEktzCep2lmWVta0CDi9Xr9TqWd7SlZNRNauBu_Anzq0Y2osIfDdiIQ5Gvq9kYM_yLwrYAsOyx5XxhNaKgAvsNbD9jPMD2RcJEjzEjl7OAXQm8WlM1N5dRj85N1FWU60E7JKOx_4EQeTf7uq7fAl017pY4gWFa3ZVuCrxvN92YZnLDN3ewTgtt__VJMtnBQJf2ePsaQjQqVwadXjR-Ol7PVgdrgxW3euu7YM2xQheRYYRp7tEqlzq3VwGE9FaDxL1VkjA0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=kqtmgBCvUXYwXv6RoA65FsccwGX856BRxw103exP9OJgdLQw8KqIbaQoKdmTqFP8_mUA9CjTsbzXE__aliQ2GuGmSIU9n3Zvql3xMd-xut2qwaVxJn0vgULPYQ4BlY0oTxbn8xFpfZ_pTcpTrYknHxFSuGPQk8I1y2fOLSIIqYN2rz0QWFgAq7QCX3qXpB6ltlPK-B9dMyen7_gTalS0DuPyVfPaRdPV1KByio5bXUbydF93qrlDeZocz_tMZ2BOGzXg3ftfkKVdHm_UpJ494XCCbXZPpK13LTNshcwhrmmuG3C4mdbfjBFx2FhKr--tvxVaGcLVbWyRboc-yQ_TsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=kqtmgBCvUXYwXv6RoA65FsccwGX856BRxw103exP9OJgdLQw8KqIbaQoKdmTqFP8_mUA9CjTsbzXE__aliQ2GuGmSIU9n3Zvql3xMd-xut2qwaVxJn0vgULPYQ4BlY0oTxbn8xFpfZ_pTcpTrYknHxFSuGPQk8I1y2fOLSIIqYN2rz0QWFgAq7QCX3qXpB6ltlPK-B9dMyen7_gTalS0DuPyVfPaRdPV1KByio5bXUbydF93qrlDeZocz_tMZ2BOGzXg3ftfkKVdHm_UpJ494XCCbXZPpK13LTNshcwhrmmuG3C4mdbfjBFx2FhKr--tvxVaGcLVbWyRboc-yQ_TsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/df6w-3sBNnlOUrqvMvnYkPPh2xpcmC6OgIw-sJtduj56-SI7iHOfeVtNJbYT1nwT0QkdAQMfIHzVef2UbMWuNIB5fINgjqoe7xupnRmfq78rlYHCUrCwjDFXs_TOqXtdxkzy-0CqPRBX-b5i0NeFRhnVapqizdycX2-C5SYCN-rf2lhAY83ehE2AOVppSAc8wP8j_MpGn7HNrB2JZI-z7ObqFwJLe7YeqaNdZzOJUQtxM9OUms7dnDaZteDoyIgtywNzTv4rKBgV-h1MTqgiSPEXM07x3PUN2n3OdCbdRM3P10uHq8spy_EevLhNqmSp9JJImgvn9UqBYr9xzdqt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=dLb-Wf04XhA2WD63esuhkViM_wDRGBx0OMaNVPCGgkcYSTPs_7Mh7xe9kTHLPoroFVOJjMuTPqR7lYypR79m6Nh3r0bl9QflX09AF_aik_K5QPF9FnD5mZ4964mT2kfrstRF_PHZ9dPWeDaMP4z-fPl7SbY2DAqsXwkGEd3K29nyKnKXPef_eXe3OCPNGZlyWHOyWEeD_10MjL93Pme1n3--C-9x0hv6WDX9eM0lw0kQ3p4qlifxHTE_k0z1xh5OJvmUJNIqbmK-Z2UNXjZLRIJliYChoeacC0Odntw-5chjQe4N1UctmucozHn_vEHozORuyXcYQahgLDEf5t8hdkXUzNVY0TojUu5sPTiBsEfpu0zFxsuhMpvjljqUOFQxwiWyEW6VO8msnWT9oOzmSwwnco9D2d3NsUwgkfvF0YXD7zHjB59TSKc2J5UOs2D7cG1fa68ZJNzlQnJ2C8MdVtInc_yh6839VmAKfS91zKzBmbE3xuUjm0J3onCvTAf6MexQVFs5iMJdllYGeY1XG29xzovobACK0tCvuK_sYXMmBXJNFq-qPd-Qq2uXm4mB0ddiKmXfQvMoXKXs2-o_oKRfLlsqWLGNUhEb8TmMUvyhed9otWTJR0XYKmZZKzaOjsshkqpLErwBomTVLdsJx_W2Oq4z8Ax2ME4Zp4GQb9M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=dLb-Wf04XhA2WD63esuhkViM_wDRGBx0OMaNVPCGgkcYSTPs_7Mh7xe9kTHLPoroFVOJjMuTPqR7lYypR79m6Nh3r0bl9QflX09AF_aik_K5QPF9FnD5mZ4964mT2kfrstRF_PHZ9dPWeDaMP4z-fPl7SbY2DAqsXwkGEd3K29nyKnKXPef_eXe3OCPNGZlyWHOyWEeD_10MjL93Pme1n3--C-9x0hv6WDX9eM0lw0kQ3p4qlifxHTE_k0z1xh5OJvmUJNIqbmK-Z2UNXjZLRIJliYChoeacC0Odntw-5chjQe4N1UctmucozHn_vEHozORuyXcYQahgLDEf5t8hdkXUzNVY0TojUu5sPTiBsEfpu0zFxsuhMpvjljqUOFQxwiWyEW6VO8msnWT9oOzmSwwnco9D2d3NsUwgkfvF0YXD7zHjB59TSKc2J5UOs2D7cG1fa68ZJNzlQnJ2C8MdVtInc_yh6839VmAKfS91zKzBmbE3xuUjm0J3onCvTAf6MexQVFs5iMJdllYGeY1XG29xzovobACK0tCvuK_sYXMmBXJNFq-qPd-Qq2uXm4mB0ddiKmXfQvMoXKXs2-o_oKRfLlsqWLGNUhEb8TmMUvyhed9otWTJR0XYKmZZKzaOjsshkqpLErwBomTVLdsJx_W2Oq4z8Ax2ME4Zp4GQb9M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qKmSt9xl1ZoEsSKDaxgtl6FskPnUgu_UkOVAXh6LqUr0_O3ujjGQqVNf9hRwEqldApq9wsoUKXm492sQjGJyUBuknn2rqDeRxz2RJEoHjUopH3ez2MIXY1Vj8dyg73BDyT66ryTJ7thRnKQuaylTB52nlhdjjWpBu4adYDvsL3NLnQTfyBfS65q7mg4qODFraUO7w7jGTqo3D459a2Yfco4iifgxlIwkzW0BE73Wat5uGsxfTMJOdS4_ybZ0wzloMbPBWUKG5DToMwADMEyhF72XlLuESIOujBnHfS4wMQMjGZf-rtnfj5bplVQhIpsppqHGex6guqm592jQaeJyrQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGbyNr735xUO_r_66RxPfTmV7qyp8OfYt9HA-Jx0YvJTKHcHMTA35DmjVN571Or7vETdexpcCO3Tq8LCLHN8E9ZpIUPN-UZ8N1mT5YgSQolMl37LXbtkQ86gO4uclfJD6kJIUONCMxqqnwf3Sl_Q9QvA0OA-qK3gaZuE1taT3IpopV2QSpm2Gzkx51BeFa7FziQCGM1DDjr1tH369TUVxEEBt7BJKVOAWbirjPDT_4udgWeQLDezv-J9ox6QGv4B_ZiIk6JB6dXK-yG2flcMFeAnMHHa4M64UovuZqdR_1pg-5zNFcomQxXroj2ngc2CvfXJcalN0A9-38TmKEOulg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8HPaRcVYg8QK-zl9nvaiyWzBDYfNL5KNSCcvYt64LDInrLbq9BBsu-ku7TBPcV71g8QEpLE6M-w-aYA2-JTHoJBFBkFEfvqMkqyeJmseCiGrPUykAWlfbS8jJSktc2A5uIwgoPPSB2tm-b1MRegHZWFGA3LhM5eLo9TuISSvuMte3OnAUn2PmyYHF3H64YCGtwDIOTVnkhJ-QjdNu796OCQgNg2bpR2ORV8lNKOzUz6fjUnmj_fIMUXliaGvMbsxo6KSvqgJftFPa_BO_4W7tPHkSSe11CXpm0v2l12OPLimEPXbOGov2byjkpQy-NIS25XL9KlgpM8--lQ11bRPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaP-gWeW0JnieNJ7873ousGb7KXzO4dw08MhUCHffuuRm9GmkBVP7QMG3-ezXtQK0E78SJ0RAWqX7jvRSlFGcj2GQlWBhaHafrJORO1FbZjUwJL_QCT1WNbs8ZffkkJftAhZI2qkQ_ngv3g-yabXU8oRcqn-QZE74F4lob1mtmr3b_QOyxrpAE1l9By65DyEJjidx2aF3r5e9fGSDmOgwLLMKFyVF_57mmfaJId9XKqchZBPezyMS862A-gyNv-Fz6Le5rr5qK2Bxnjvc4Yx3pLYSml838UGb7I5T04hnj6YNvElAeR-XCU7YncHgajc7SlR8N7Om60JPaSPjGlBmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id9QG_YEbFliTzJC5lRRQPrrmlFmFFmpR5A14p9G6MlT9MRPWeSw_jtY8aJ5qT-yfRpiqO5jTj-pyTi-N60BZX5UGt96WSOXN6SvY7nzbFNRvAy_Pp1N9jSQauGulgUEgbblhC5ZrQtypNt85Xlbf9ufVXuiDbkwBQmPF5b3gLCk2k31p54dp15_5zFy8hv5p94xwLO9mhw4fOPyJ9iKIgnzMjFJGGFIqA9k0jiHQDqGpLRR9XYsfz-joc8WOR45xAO3N1gZ9DtpVa34vpx70HK7nQyCW3AMNDi2zgCa75IDrZ9eNTmdQ7Wnw_9nTtWVNE0ssM_4xMYOdQNoL0XAgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6TY_YcZzrySnNHaGvzYIfykv4SD-utbJhY98D4sq6_hx8u38dTdu4pRzFf8kmqJgPaU-SlmbjA0eJ_9ynYr8oERgot6V5a-Ywah-qvfzTs6bIY0M3G-YeOsBl6WshPIkKlIh3juTn4dQGhdbD-aKuP6S98UlUtQNks6pRrqE4AUMmYX_7M2ztWzDIzEdJneXWZ3RK0304_pkyLVtIJnXjyhjsSUBCg681vpxEKmgs6drbFKro1bt_cEQrQNmuJmLOc6DGmZuWfMMQtJYSlpO_JEHVqsNXSXOBErIJ9WRyQ2vsWr9wvc7tMYugkF0RH2zDLmcvfL8F2khNON5HVf8_DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=ngcFTQTvxuoQfUrDutcjYcKZffNOkgkpsP-BdNILgwKsRjzwCQ6XSq5GaFXhXn0ElqgtYb64z3LvdxIC1Gd3COObywVDJiti89knzBQot5dl0lyqeNF7-F7Lh5BzIhaaVA4irAfuQ8-4oH5eAnCdquDWboweXGukPhtB-Jo7TigSSWj2c313k8U9vILbzMQ4Qdz3foaZQzqqCVX3wyJ2-0MTb5NDejwncmqItAe6rUe525C98yiqxRZZFYHqFHVN9MrDE_RKObPluBJ-FvSRQp3o4rrwR33DcOgtMdg18c7MnlNOdUIsC0BNEwPyQOgoXWZuLZoI4DWe4cdFXAzp6TY_YcZzrySnNHaGvzYIfykv4SD-utbJhY98D4sq6_hx8u38dTdu4pRzFf8kmqJgPaU-SlmbjA0eJ_9ynYr8oERgot6V5a-Ywah-qvfzTs6bIY0M3G-YeOsBl6WshPIkKlIh3juTn4dQGhdbD-aKuP6S98UlUtQNks6pRrqE4AUMmYX_7M2ztWzDIzEdJneXWZ3RK0304_pkyLVtIJnXjyhjsSUBCg681vpxEKmgs6drbFKro1bt_cEQrQNmuJmLOc6DGmZuWfMMQtJYSlpO_JEHVqsNXSXOBErIJ9WRyQ2vsWr9wvc7tMYugkF0RH2zDLmcvfL8F2khNON5HVf8_DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=R90NigNlGyEMGwaUAUWFCu30GfwJ9Mz-5UAsqWV8ZS1kCUOyb0oS5gVUzOV78kIWnXvbFirCv2iLjVA7BH_KYR10Q8N-uLHRDnoa730xBKkQqo4kIS5H1fnqi4WQps6-3ok8-arJWN_7HcpZ6dX28cTapXjO06PQMrZ2k8Rm7GETt1njWEr6wf8vjaGRLIRYCwB-YDq2movTA0hvIg8hS5s3UcrJwnQzb1bGjce1rs2Q2jDxE6MTVgGaMSqG0UMXnerEwbSFylSiv6MYH4Blb16TY6-lMlvD2Wrq9l2-BoUXcWuk5o33HeYjavu6lMeb3H6jJUJV-w1Nwe-zoUMSyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=R90NigNlGyEMGwaUAUWFCu30GfwJ9Mz-5UAsqWV8ZS1kCUOyb0oS5gVUzOV78kIWnXvbFirCv2iLjVA7BH_KYR10Q8N-uLHRDnoa730xBKkQqo4kIS5H1fnqi4WQps6-3ok8-arJWN_7HcpZ6dX28cTapXjO06PQMrZ2k8Rm7GETt1njWEr6wf8vjaGRLIRYCwB-YDq2movTA0hvIg8hS5s3UcrJwnQzb1bGjce1rs2Q2jDxE6MTVgGaMSqG0UMXnerEwbSFylSiv6MYH4Blb16TY6-lMlvD2Wrq9l2-BoUXcWuk5o33HeYjavu6lMeb3H6jJUJV-w1Nwe-zoUMSyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VTQHTWp4oYYRijKx1KrJPIveiDDa_tHXrp9Ipj_4sXPswIPkoPtTCF2SGa35rYA9YxogeALw67VTJ5dxpdSoudRdBC3U0OAUMcGRTuCGOSYR50B4-4vJh2USqyFYL3TthWp1P3T9ikl7z_lKZw8KXqwXh5z3SeTI9a6N2wHEV5qmKbk-9eMJTGhm-R1w67b4qzdqtO1tHr0pxMjjG2HgSL1nNnGGc8SOH00735k6lhyYeFJCKjKDIab21bX3wNWjow8IsFlldb3TLGeqxw2cPs73CrTXu-tOLUJ6Qar10mx9htR7whK7I8-MsJSIEpkB0ZXbzTYE3LiRB5pJwdvfQnLZZZaytuVpCDJLhpj_GvXK52dRv-5DCqktVJ7gB8ypYoK3DqT1UVYnyUVUP_F6lcF9rjrTMACrPto1kkK9T4aPsE5jc9vPAq55c3F3bcGiBCbxXhNQLuOLeeFh1JhhLIF5qBnLi6EKf9H-yob6XvvX3cP2IZnON-T0QutQhmGopOKT9q70mjvd_Fpre4BjiYw4Xv6-N4HpVHDtG8GxHGxX1wAZ_eXT6IRsh_cQb6ykaNTln3ztaTrFjw5adphNt9CWAWga2vDPYBGfUFG-3wxQPfcf6XYQQxVKD6Z4oNH32HdoIiOvrpKjfWlRubG-1Dw68EfVP0kTMLV-LKYEzJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=VTQHTWp4oYYRijKx1KrJPIveiDDa_tHXrp9Ipj_4sXPswIPkoPtTCF2SGa35rYA9YxogeALw67VTJ5dxpdSoudRdBC3U0OAUMcGRTuCGOSYR50B4-4vJh2USqyFYL3TthWp1P3T9ikl7z_lKZw8KXqwXh5z3SeTI9a6N2wHEV5qmKbk-9eMJTGhm-R1w67b4qzdqtO1tHr0pxMjjG2HgSL1nNnGGc8SOH00735k6lhyYeFJCKjKDIab21bX3wNWjow8IsFlldb3TLGeqxw2cPs73CrTXu-tOLUJ6Qar10mx9htR7whK7I8-MsJSIEpkB0ZXbzTYE3LiRB5pJwdvfQnLZZZaytuVpCDJLhpj_GvXK52dRv-5DCqktVJ7gB8ypYoK3DqT1UVYnyUVUP_F6lcF9rjrTMACrPto1kkK9T4aPsE5jc9vPAq55c3F3bcGiBCbxXhNQLuOLeeFh1JhhLIF5qBnLi6EKf9H-yob6XvvX3cP2IZnON-T0QutQhmGopOKT9q70mjvd_Fpre4BjiYw4Xv6-N4HpVHDtG8GxHGxX1wAZ_eXT6IRsh_cQb6ykaNTln3ztaTrFjw5adphNt9CWAWga2vDPYBGfUFG-3wxQPfcf6XYQQxVKD6Z4oNH32HdoIiOvrpKjfWlRubG-1Dw68EfVP0kTMLV-LKYEzJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JQRXOCCNHkCDPitBtcw0X06Oa2Kj3mEu9j5X1MKyElw60FImJ1HQuQr7aOj3IfgzUb_GvVxRuWZyUZLhSYiSXp1qOQyCGEjcSNQ-1SLr38YcqfrpqQ9skC6TIiYoYRFHsch0IbWpdzWBV8mv9avytpxAmryOAvQFsrj3uHktwfZhZRVB_LIfCB9BRcAa9mZV8fJ7_DWEaEhTfiUExnie3Z69MaL9WJouGL9jT9x_zFfVHkiP7nTFPQ95_xEIxJih0tY-p5YRWFLmCiUPMzSsUN4nviD_8rq7vuWjEIxzgN8-oaXubDY6gtZ_hBS0-wff85INWrSPjpCWHlN4Q48l-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=JQRXOCCNHkCDPitBtcw0X06Oa2Kj3mEu9j5X1MKyElw60FImJ1HQuQr7aOj3IfgzUb_GvVxRuWZyUZLhSYiSXp1qOQyCGEjcSNQ-1SLr38YcqfrpqQ9skC6TIiYoYRFHsch0IbWpdzWBV8mv9avytpxAmryOAvQFsrj3uHktwfZhZRVB_LIfCB9BRcAa9mZV8fJ7_DWEaEhTfiUExnie3Z69MaL9WJouGL9jT9x_zFfVHkiP7nTFPQ95_xEIxJih0tY-p5YRWFLmCiUPMzSsUN4nviD_8rq7vuWjEIxzgN8-oaXubDY6gtZ_hBS0-wff85INWrSPjpCWHlN4Q48l-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iff7Zenla54lAZPX7dgCKk9ItIq3adRM_yKC1fhJL4v7NWXF9en7oCcNYi8Sb62Hl-2XJTszGmq24JRlwyWUj97ZljDw_HFP0mfiOdrz_P2P51--9NltATPge6cDcOJek-QYHFz9tTxlGE8g_JMATrB7uf9IROcckLaXW8KP6ud-_1Vr1H-4HVmX9C6pUJHJFtYC9Oy8ZURZ4mTdh9J3umer83DMPnVDBkawW8OJk_DjIP8lnWVlmhHheCL9sqa3mC0-MIPCjFZ7Ge5ENv9_fkgg_H96ypHO7an70CvK6rTPLhkizKEaCcgjFX0BocjgTk_cLdaS2HckEvgGtZ2V4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=SGYFMleYS6p5B5syIZcQUGhBfIiMuPr1RmzhRzUV7F9MxE4MRj5tYR3mNs9RrjaTeD_f2HS5c6SfNSD8_BSJc1IzpE1V7Aj-nV6dniHRDz8kx5-GMGaxDOb8C2RlNf0-1VaX_RScIXM57nybK_UJmKSd1f7xn9GE5CER4ct91t9Gl8xsmzoMQUdttkI1R8s2W0ecrIztqefBY_fjYZnWSisCOrFrrVZmAxbLE8E_alfc_6GoTF1kJSPj-MEboWbpwZTXPw5RM7uzteiL2CzPsxUFYMCHlEMlATjVgnI1BB_3Tvex0K6C-vxPMwnP4OP7B31jCade6uMIll5y_AyAXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=SGYFMleYS6p5B5syIZcQUGhBfIiMuPr1RmzhRzUV7F9MxE4MRj5tYR3mNs9RrjaTeD_f2HS5c6SfNSD8_BSJc1IzpE1V7Aj-nV6dniHRDz8kx5-GMGaxDOb8C2RlNf0-1VaX_RScIXM57nybK_UJmKSd1f7xn9GE5CER4ct91t9Gl8xsmzoMQUdttkI1R8s2W0ecrIztqefBY_fjYZnWSisCOrFrrVZmAxbLE8E_alfc_6GoTF1kJSPj-MEboWbpwZTXPw5RM7uzteiL2CzPsxUFYMCHlEMlATjVgnI1BB_3Tvex0K6C-vxPMwnP4OP7B31jCade6uMIll5y_AyAXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=PN1-QqneB3ZvmwglQYVXh-Sb3h5-mVmJf0lNr9JKMDJrBH1VCaehCodnEMSK916jD3RJcfckCi06SyHd9u-EXl7rk90TIqNdABC7SSEfWMEd-CyU6K77pRxNgHcHuu8fzeE9ta9lHPX3L9XBJZCm46EY4UxuxdHaFRyDIfhiz87cD219LPBLI8-Y_TZYjZQsAVxHwHZWPmr9vPMhg6lfXWCZBLKFQELFWXY2EaQDRweoiKLYs6loZdZOCzYtGBK64Sw7S56ka_xepNWsQGhDz32trC52rlrnlph2CdaJYqLSVo9gf4NHKOY6RTnCmJ-yq9GuQeSU_sKGeftimG_KgTqgomQCPSTdwZxxcNgiGw3pyRUQpjK5NE1fk7LOp6z6zAaf7xI8QcTxMHSRvpBlRaw_SpXVLAnkXxObouIbFEFgqpECCr0-40zpvrzJ_B84NO6eBSTV7AYuez_w_UsDn1D9L_doSEjl9d4ticTAHwI8WJKzINw--Zf_NR0FbqcYhyXD_Y3uE8Uh-f3AWP4IkiBzcRCfq67eUQ1SUruV9UvQk0d78nKY41k3qKzFjJfyGfH5wonjd_4t7nwD15W6z6LP0eA-S5S84u49y9LEAQlVMkfvky_UNRCCaJ5Nw4bggbuwD4TsfaYoxqfe0sGzgGfJGmRdgPVNEbl1Jm8K2I4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=PN1-QqneB3ZvmwglQYVXh-Sb3h5-mVmJf0lNr9JKMDJrBH1VCaehCodnEMSK916jD3RJcfckCi06SyHd9u-EXl7rk90TIqNdABC7SSEfWMEd-CyU6K77pRxNgHcHuu8fzeE9ta9lHPX3L9XBJZCm46EY4UxuxdHaFRyDIfhiz87cD219LPBLI8-Y_TZYjZQsAVxHwHZWPmr9vPMhg6lfXWCZBLKFQELFWXY2EaQDRweoiKLYs6loZdZOCzYtGBK64Sw7S56ka_xepNWsQGhDz32trC52rlrnlph2CdaJYqLSVo9gf4NHKOY6RTnCmJ-yq9GuQeSU_sKGeftimG_KgTqgomQCPSTdwZxxcNgiGw3pyRUQpjK5NE1fk7LOp6z6zAaf7xI8QcTxMHSRvpBlRaw_SpXVLAnkXxObouIbFEFgqpECCr0-40zpvrzJ_B84NO6eBSTV7AYuez_w_UsDn1D9L_doSEjl9d4ticTAHwI8WJKzINw--Zf_NR0FbqcYhyXD_Y3uE8Uh-f3AWP4IkiBzcRCfq67eUQ1SUruV9UvQk0d78nKY41k3qKzFjJfyGfH5wonjd_4t7nwD15W6z6LP0eA-S5S84u49y9LEAQlVMkfvky_UNRCCaJ5Nw4bggbuwD4TsfaYoxqfe0sGzgGfJGmRdgPVNEbl1Jm8K2I4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=vMCryKaOzaZ8CI4nUuOKyCT3gEuMH_KMXKL3-CsCXR3XsfKIIkqh4R0rPeIQW6hz_-waxC8JFW_pyEPDSSIplFydtTB01vPSlnOcAZ3XahYU0AlbkVOitE-0L_OVKXGKkDuOVqJPo-CNwqjeaUKEXTgzgavO8OIA6LIz279bjPyF09CEYFxUrz8VY-pUAcaGBTPdkIYAJcn6RGMp-JzopTNHeDUl2t4SWSZhr3y6MwcsVQKQ6pl5iRhem4beYbNK-1Hp-5Ciiim5Y-DQZNV_C_hmNcNpm6UkehJwRZ80YWiNN_UNzKlwGlHXY3SAg4hpadhOOxXf2h7GQcWfvH5Ms0rTwbfvUw6bZ8Eg46xU7pU480nxAmKWl20mOeWysdiUJYoSzho1LHLOSma4Hegg372wbJoigfyOkU5FUYxL0s1KyPEmGQvWqYdKUZ7Xw9J5mPALEINQ68kFr3JG8dlER8gA70yPuMd8UZCJ5GL2aF3-hmRUS9GcrWOAQwtCTtmPgPBsaub3ue-_XkHSLDpFQaXCwb4MRcjDB32J1eBViUu2wgVZoeSekplEZj8wn9APj3np0TFKGCYju5KcwAMFMdCdinIV99G8GOKshFJRJvVS4wF9gcg0FIEKhfXU7nOe_G20I14iG_vLS4TqdqlfRGXr36ozHMFn8uL-6Wg5kh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=vMCryKaOzaZ8CI4nUuOKyCT3gEuMH_KMXKL3-CsCXR3XsfKIIkqh4R0rPeIQW6hz_-waxC8JFW_pyEPDSSIplFydtTB01vPSlnOcAZ3XahYU0AlbkVOitE-0L_OVKXGKkDuOVqJPo-CNwqjeaUKEXTgzgavO8OIA6LIz279bjPyF09CEYFxUrz8VY-pUAcaGBTPdkIYAJcn6RGMp-JzopTNHeDUl2t4SWSZhr3y6MwcsVQKQ6pl5iRhem4beYbNK-1Hp-5Ciiim5Y-DQZNV_C_hmNcNpm6UkehJwRZ80YWiNN_UNzKlwGlHXY3SAg4hpadhOOxXf2h7GQcWfvH5Ms0rTwbfvUw6bZ8Eg46xU7pU480nxAmKWl20mOeWysdiUJYoSzho1LHLOSma4Hegg372wbJoigfyOkU5FUYxL0s1KyPEmGQvWqYdKUZ7Xw9J5mPALEINQ68kFr3JG8dlER8gA70yPuMd8UZCJ5GL2aF3-hmRUS9GcrWOAQwtCTtmPgPBsaub3ue-_XkHSLDpFQaXCwb4MRcjDB32J1eBViUu2wgVZoeSekplEZj8wn9APj3np0TFKGCYju5KcwAMFMdCdinIV99G8GOKshFJRJvVS4wF9gcg0FIEKhfXU7nOe_G20I14iG_vLS4TqdqlfRGXr36ozHMFn8uL-6Wg5kh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=aRRo_noJRkU5APUVW7cLfeP0Q_6kI7JJneKbvUI_o3cw1j0_HJtgbjeE-GJ1u3I289hyTVFACol3y6QdY8MJikAO7quucfuwbC_qpXKCW6had4aWP7bsOsWafMb8kDulHf6QiKGlZ6P4TDwHZIKy8CULoPrqBcB7MWOOzS4KDeSu8brhuIGTlJApDqWErydwUQavJV43Nd-7ONxggFkx3HxUacYbc2m3rXATwzDiC4sCerP0EhzhUpoDRrCYBPYlVT-pnjrl4g80s13jvR9t8HDzT-1i_nhDPTMrLHkIIlF6gCuFSr70lbfxWXKT5BZ09p96JXagEwUpNGzisLDLgYehxufFmKAivx0g26g7Wpv_RkKVcIKFcqdJnWICDaK9Rkd6KueqlI4pTIy5wChwmupbN7K2nbSFpFlE8_f25lH8S-_Pkc5QEjaJa7v3t8Xkg6Cb65RUB_b6ZbkUvullRBV_1vcG9yiGv49Zno4P2bZbXuHlzAmlLPHsQ0OhjOh6qk-Zk2JarCdyFVmEvJk6NSq7K5Z5Mi6RH4Aw3oXl2OajUKu9VzQUYaviT33c2ejopfJIgjQcTJTPmsHEcV-m6smCJGkztfdcoyJ09kPdK2xD8D3lN2LBP4gNsbF3oOD6nGsbNN2KgF3x166ZN4f2cGtBRbNxkPwwNGQFNCE28hU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=aRRo_noJRkU5APUVW7cLfeP0Q_6kI7JJneKbvUI_o3cw1j0_HJtgbjeE-GJ1u3I289hyTVFACol3y6QdY8MJikAO7quucfuwbC_qpXKCW6had4aWP7bsOsWafMb8kDulHf6QiKGlZ6P4TDwHZIKy8CULoPrqBcB7MWOOzS4KDeSu8brhuIGTlJApDqWErydwUQavJV43Nd-7ONxggFkx3HxUacYbc2m3rXATwzDiC4sCerP0EhzhUpoDRrCYBPYlVT-pnjrl4g80s13jvR9t8HDzT-1i_nhDPTMrLHkIIlF6gCuFSr70lbfxWXKT5BZ09p96JXagEwUpNGzisLDLgYehxufFmKAivx0g26g7Wpv_RkKVcIKFcqdJnWICDaK9Rkd6KueqlI4pTIy5wChwmupbN7K2nbSFpFlE8_f25lH8S-_Pkc5QEjaJa7v3t8Xkg6Cb65RUB_b6ZbkUvullRBV_1vcG9yiGv49Zno4P2bZbXuHlzAmlLPHsQ0OhjOh6qk-Zk2JarCdyFVmEvJk6NSq7K5Z5Mi6RH4Aw3oXl2OajUKu9VzQUYaviT33c2ejopfJIgjQcTJTPmsHEcV-m6smCJGkztfdcoyJ09kPdK2xD8D3lN2LBP4gNsbF3oOD6nGsbNN2KgF3x166ZN4f2cGtBRbNxkPwwNGQFNCE28hU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=EeQZULK_EZsn47P-z199yPcuBrNK4tZhw_k6I5CaLBIy06Gu1g30-B4wYXSOIAUeyK71Rq8DQXl0js_lOGoir3W86QNsx5amyBxVf69f5WI5oIpEhrykwqUpBALNO3l6UieDqjYUl94c4ukQ4VnkOaVBD3Zu56cFDvAJozffiTRkuqNAfi722Fg6jGKBO3jfqeQ2r3zBliDEjQ6Lr_7J3BdL36jhqgtp55d_ocqD41ESTAEzSbXRxi_AbERvoCHZh-GXfNWjvC05_BE7iCMDkEt2NveLgg6Ke7wYdDLG9gZ7DpW147sXQUqcfeC_fe12kNVxvC0W5hxbifdBekyHLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=EeQZULK_EZsn47P-z199yPcuBrNK4tZhw_k6I5CaLBIy06Gu1g30-B4wYXSOIAUeyK71Rq8DQXl0js_lOGoir3W86QNsx5amyBxVf69f5WI5oIpEhrykwqUpBALNO3l6UieDqjYUl94c4ukQ4VnkOaVBD3Zu56cFDvAJozffiTRkuqNAfi722Fg6jGKBO3jfqeQ2r3zBliDEjQ6Lr_7J3BdL36jhqgtp55d_ocqD41ESTAEzSbXRxi_AbERvoCHZh-GXfNWjvC05_BE7iCMDkEt2NveLgg6Ke7wYdDLG9gZ7DpW147sXQUqcfeC_fe12kNVxvC0W5hxbifdBekyHLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=TH4QnDH2GppgDrkaIqm7hPU5GDgVAWdqHQu0wmsHxKnSKiHpmOKrKcrP1fzzWF-GDs48l5HChWLPhGVBQBDl0M7bwZ_sEdrZ5grDtVsgB11CvBXXxpj1wyLYejT6vJBHM3arjBVj5hTKhIVilxPo-F687tfSblZ08rzB_06S4KlwFqIow7cwEb8gQh3Cg3tV8xpVIOvRfoM_VAdsNYjEEpoD4S3cR89YstoP831r__1gr4CDiwtugL4et6mZXJQX-LZF2CbNEGevSW87KdxwPHY3GckY0E5BzdKdHqe3f48ptIzWwxDkrvriOjx59DsyJ5OppwyVRZTOIyJHL1jaIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=TH4QnDH2GppgDrkaIqm7hPU5GDgVAWdqHQu0wmsHxKnSKiHpmOKrKcrP1fzzWF-GDs48l5HChWLPhGVBQBDl0M7bwZ_sEdrZ5grDtVsgB11CvBXXxpj1wyLYejT6vJBHM3arjBVj5hTKhIVilxPo-F687tfSblZ08rzB_06S4KlwFqIow7cwEb8gQh3Cg3tV8xpVIOvRfoM_VAdsNYjEEpoD4S3cR89YstoP831r__1gr4CDiwtugL4et6mZXJQX-LZF2CbNEGevSW87KdxwPHY3GckY0E5BzdKdHqe3f48ptIzWwxDkrvriOjx59DsyJ5OppwyVRZTOIyJHL1jaIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Gqsts_xCy36YZ-PjjR9BJa9zARKYCnEjbMFPKdR_8-WA92tF55zJInGeEeN6AOWqzx1lDEd8EJU_MixdlTPVYNCjxtDIM1IU6eG8ObhJA41tGoXukMEw8u_NuuJIsVXZHIeHF-jzY61WAd5DRl4gyA7Xuh1Cvk-v-s8rzRqseEXlFjIOR1A7POhQf3hkgvgohNO2usZZmog1dcB2dZhywHUrXcKbe99RZ22hcDMOWMHPX4JtbrtAdPPx1Kej7VJy8eyx3AqHgJJdITdfSHYJ--sA66wYse-TvYdAiF32D3sparxBt-fYFN9AK0nPVMMvaLVeFQjVbx62l8mbrpv87g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=Gqsts_xCy36YZ-PjjR9BJa9zARKYCnEjbMFPKdR_8-WA92tF55zJInGeEeN6AOWqzx1lDEd8EJU_MixdlTPVYNCjxtDIM1IU6eG8ObhJA41tGoXukMEw8u_NuuJIsVXZHIeHF-jzY61WAd5DRl4gyA7Xuh1Cvk-v-s8rzRqseEXlFjIOR1A7POhQf3hkgvgohNO2usZZmog1dcB2dZhywHUrXcKbe99RZ22hcDMOWMHPX4JtbrtAdPPx1Kej7VJy8eyx3AqHgJJdITdfSHYJ--sA66wYse-TvYdAiF32D3sparxBt-fYFN9AK0nPVMMvaLVeFQjVbx62l8mbrpv87g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=dfeI_4Rb7gZff14vIHARilA7sj3l0SfUC_8VVsakeZ4ncfAv2FgFSjoY_pmN53Fjr11EI3JODugSGRYyzSIfe0eyqCzIjMgaIOws6cHNdC6kK1klxXJ3eY3GaghapuDe-a5fgiBpLqaIzevDDj6NrH-lsd_vpaFieflz1zi4LRjR5Z8DCqK7NkLOX7xIuBYAfoRkqO3BPeSr5Ox-7LG-jpdU5ENyLnGQqp9POpOvQxT6objjYJzzNsYIJFEgg1u3_WDEmu40wtQSiMTNWiu-4J6iKIUhTEnO4afDDITWCF0OkD35lLCqhvD7eLYKKjzRf8sqhhgGgQAUQdSiF81pIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=dfeI_4Rb7gZff14vIHARilA7sj3l0SfUC_8VVsakeZ4ncfAv2FgFSjoY_pmN53Fjr11EI3JODugSGRYyzSIfe0eyqCzIjMgaIOws6cHNdC6kK1klxXJ3eY3GaghapuDe-a5fgiBpLqaIzevDDj6NrH-lsd_vpaFieflz1zi4LRjR5Z8DCqK7NkLOX7xIuBYAfoRkqO3BPeSr5Ox-7LG-jpdU5ENyLnGQqp9POpOvQxT6objjYJzzNsYIJFEgg1u3_WDEmu40wtQSiMTNWiu-4J6iKIUhTEnO4afDDITWCF0OkD35lLCqhvD7eLYKKjzRf8sqhhgGgQAUQdSiF81pIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YzLuW5oN1oMoZajxdlu0-dUpKeqyf-Hj_rTVNU6Iaa7fb5KKDoMrjiRiHWTbSovrqnluczBDUNleUY04rtmyJrS3vgmLCbFYr5bXy-frBoQFI5yCJzi-ZAqF602cYL1q3_3LqmrNie8jUJhJ-yKT8gy8xGUpkwFSnywVBC2AqZWqSp3SWJ2Br3zJ3fzVGlV9sqSXnVvHFtFwKTmwb753qmkwOw10i3M4i2KV-CYPSTXKv3qxs-ySfK7hbror_ddnwfVa8NjNm6NEgvvHog7KQ66xQa1dPf_tl8uKwo7kvjqKHXCvnFMxP-tElMoRu0eDCQxhbrlqJSAs3y7mwuWyOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=YzLuW5oN1oMoZajxdlu0-dUpKeqyf-Hj_rTVNU6Iaa7fb5KKDoMrjiRiHWTbSovrqnluczBDUNleUY04rtmyJrS3vgmLCbFYr5bXy-frBoQFI5yCJzi-ZAqF602cYL1q3_3LqmrNie8jUJhJ-yKT8gy8xGUpkwFSnywVBC2AqZWqSp3SWJ2Br3zJ3fzVGlV9sqSXnVvHFtFwKTmwb753qmkwOw10i3M4i2KV-CYPSTXKv3qxs-ySfK7hbror_ddnwfVa8NjNm6NEgvvHog7KQ66xQa1dPf_tl8uKwo7kvjqKHXCvnFMxP-tElMoRu0eDCQxhbrlqJSAs3y7mwuWyOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=j72RE4evbNYO5EPEP6kLe_bfbT56ZDuDenLRwbAeRLvXZOEpiNzocrfcWb4uCqpvs4CXEd8Kv55AEZbjQaxVPTV8pQ4KBc43vrpUya9nPS9v53e5qM3fnAjtrf6h3NQs1irSQRb3ttk_D3Go7zxdBkbw_JEZi1h6SXh1-Z5IymAlGxJyq6NKObah8cifEuJ9X5ddHm6vzWEP-Malix_zaByg35RkZe5e6O_dUupSp1MjNGsCIgQE3XEWSZcE8X_SkLhL5_d7NeeMatYeudEeJN-hOV-rGRZK119gX1FqO7Ccak5kNpI9wQMPKOvGRUNGT7UJGiqK5-tAtVvsiF5wEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=j72RE4evbNYO5EPEP6kLe_bfbT56ZDuDenLRwbAeRLvXZOEpiNzocrfcWb4uCqpvs4CXEd8Kv55AEZbjQaxVPTV8pQ4KBc43vrpUya9nPS9v53e5qM3fnAjtrf6h3NQs1irSQRb3ttk_D3Go7zxdBkbw_JEZi1h6SXh1-Z5IymAlGxJyq6NKObah8cifEuJ9X5ddHm6vzWEP-Malix_zaByg35RkZe5e6O_dUupSp1MjNGsCIgQE3XEWSZcE8X_SkLhL5_d7NeeMatYeudEeJN-hOV-rGRZK119gX1FqO7Ccak5kNpI9wQMPKOvGRUNGT7UJGiqK5-tAtVvsiF5wEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=pHEj6_rAs7RtZY3z21MtZ5lwdkGoLaJ0mDctXgOneWBz46HHpQkR5MQcExrRJ26TFCjE29xPf-EbXTYi0YUmU2JcO3W_8z-zVH1n0YSs1e2ttzOFP8Hr5JnIBThHi-ful9ToE9l55fepx_dIuAE3yUJyrne3xDtOfXcA0WHSCNwNsx4Y_bT41AmzeGBZK8WPdvb7O2wlLPPyCCazeiLiwS0z9LCo5ss4sxwYbJWu2m18Y2c7yV9KHtCIUZHfFz6B6ZjLBzqBn4Z-6pFyqN8mIHNYzCCw29alhMfCWEgldRkuhLOnjRWKxyAd1CZbvQwtXlM9oU1s9a2DVc92wuEHgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=pHEj6_rAs7RtZY3z21MtZ5lwdkGoLaJ0mDctXgOneWBz46HHpQkR5MQcExrRJ26TFCjE29xPf-EbXTYi0YUmU2JcO3W_8z-zVH1n0YSs1e2ttzOFP8Hr5JnIBThHi-ful9ToE9l55fepx_dIuAE3yUJyrne3xDtOfXcA0WHSCNwNsx4Y_bT41AmzeGBZK8WPdvb7O2wlLPPyCCazeiLiwS0z9LCo5ss4sxwYbJWu2m18Y2c7yV9KHtCIUZHfFz6B6ZjLBzqBn4Z-6pFyqN8mIHNYzCCw29alhMfCWEgldRkuhLOnjRWKxyAd1CZbvQwtXlM9oU1s9a2DVc92wuEHgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=AY_E5v1yDAzjMi6sjb4CNHASniOqF7khPdesmQGQAgx21ZuNb7g9hpY1qX_0MQFQut3bM21T-1_NLInZiDmDJpjNFNIvcTc8LFxcPai75LBRCn-4qsReAzk7VYT0OD7TmuaDCCk3rvC7eIaBeYfk4sogqE3gsRiXQbGdsTFThlE4hOCbGAaozzgjFzJ4PhKEIpNLgZwoDoaU71lsg9ijCT0o_tnfj56vD296zXWchhTtnvUHiT1tKz91NT-oFAJ69bou3aDRfF5rG6Y3beWwz2x3lzm5L-L8E-_pdNYVAZv0T451O-fgJZEqFKTdR8iPqLgrybXjJbZdXWVj9rF-TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=AY_E5v1yDAzjMi6sjb4CNHASniOqF7khPdesmQGQAgx21ZuNb7g9hpY1qX_0MQFQut3bM21T-1_NLInZiDmDJpjNFNIvcTc8LFxcPai75LBRCn-4qsReAzk7VYT0OD7TmuaDCCk3rvC7eIaBeYfk4sogqE3gsRiXQbGdsTFThlE4hOCbGAaozzgjFzJ4PhKEIpNLgZwoDoaU71lsg9ijCT0o_tnfj56vD296zXWchhTtnvUHiT1tKz91NT-oFAJ69bou3aDRfF5rG6Y3beWwz2x3lzm5L-L8E-_pdNYVAZv0T451O-fgJZEqFKTdR8iPqLgrybXjJbZdXWVj9rF-TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VMA2E4dGCJdyo6ed0yIgPvmdOwjr0b6d68-5xZQsozg_PwMinejOZT6uh7io1y4ew9BUHrAGGLFPn1X2bUiyGeSlon0lz0WYQ_c7cpVc486aX1NrbAnnZYvoDFt_M3gWKHUWwwzURoO-xWRg5RFKBi_C_tr-9nBR1OhGZ23JdOqBl07HAW87_SUfN2OXoNaD7sI4G1mnQG4sCsgeA2Jt1p1ug6PqqS-IHHok3euwnpJkEcKB-9ZSX64yMMbW2gSwtwiT_Q04HzvGd5Y4GHZXsVgsYdn-c6lwQ4k4dBoRlkpVNakKsuUpD0kWzgiC4HjfVH1d-WHY_Z2R1MJ1D5vw4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=VMA2E4dGCJdyo6ed0yIgPvmdOwjr0b6d68-5xZQsozg_PwMinejOZT6uh7io1y4ew9BUHrAGGLFPn1X2bUiyGeSlon0lz0WYQ_c7cpVc486aX1NrbAnnZYvoDFt_M3gWKHUWwwzURoO-xWRg5RFKBi_C_tr-9nBR1OhGZ23JdOqBl07HAW87_SUfN2OXoNaD7sI4G1mnQG4sCsgeA2Jt1p1ug6PqqS-IHHok3euwnpJkEcKB-9ZSX64yMMbW2gSwtwiT_Q04HzvGd5Y4GHZXsVgsYdn-c6lwQ4k4dBoRlkpVNakKsuUpD0kWzgiC4HjfVH1d-WHY_Z2R1MJ1D5vw4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=nH6jFgUTNOT2sP0UGg2mF1rqgXCmzJGz18D8CwcyucTzal3cf-yiuGCQxszb9VWmcMe03XcrwCtSOGl4AU_ukf9Th0EDhsWW7jYqWmTEeBtmkRnGFeEcouG_1W7IA8Xb0PIxvpeNXgDq21e-xh1cO7IaYl_PiQi5cJ5WzZ0TMdcpf5m1D2JoO5G95qkbIgGArbtTXYP_2-kLRUY4ul1RbBbLqfWzN_ZOY4YkRIiTCba3Xg6XPBOgAdbFDwtI3hcBXFSekGDX5uI95DTGhE6Yhgg5peA0JOPIYq__vl4A59mHTKHfluG3A7IjcMIiGeBtelMl6OiCd55BtY7fCQky1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=nH6jFgUTNOT2sP0UGg2mF1rqgXCmzJGz18D8CwcyucTzal3cf-yiuGCQxszb9VWmcMe03XcrwCtSOGl4AU_ukf9Th0EDhsWW7jYqWmTEeBtmkRnGFeEcouG_1W7IA8Xb0PIxvpeNXgDq21e-xh1cO7IaYl_PiQi5cJ5WzZ0TMdcpf5m1D2JoO5G95qkbIgGArbtTXYP_2-kLRUY4ul1RbBbLqfWzN_ZOY4YkRIiTCba3Xg6XPBOgAdbFDwtI3hcBXFSekGDX5uI95DTGhE6Yhgg5peA0JOPIYq__vl4A59mHTKHfluG3A7IjcMIiGeBtelMl6OiCd55BtY7fCQky1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oaOCLlRaXwOHneZ4IeQSHvhYgrV6AL7tW71haJu_0HSTAkCPbHwzzZMCeRWLOjhz0sMT4K1UblNiKpi8YfTREZwY2sxDAXU8NxUWC93lLut_TKKXNKcdnAb5f-0-0Qyza3vt3mXXaCNV747YlpiEqur_5WinF3M5uFwUJpRzOG6l4Dtwjm2yfFoLHea2oOfVmAtQDZrOSx1KgW0CF1NdX13fNjpGIpN0aXN_LfQAuccfigYtJleOHJeaEaGayxZ12ciCaFeHIzPkW9TFE4FZ6ee55qE3-a0YtGRmgDI1T4GFz1rXIRNDnjkzz--0T83Z6nrGfX5LlKTDxQOGw98D8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oaOCLlRaXwOHneZ4IeQSHvhYgrV6AL7tW71haJu_0HSTAkCPbHwzzZMCeRWLOjhz0sMT4K1UblNiKpi8YfTREZwY2sxDAXU8NxUWC93lLut_TKKXNKcdnAb5f-0-0Qyza3vt3mXXaCNV747YlpiEqur_5WinF3M5uFwUJpRzOG6l4Dtwjm2yfFoLHea2oOfVmAtQDZrOSx1KgW0CF1NdX13fNjpGIpN0aXN_LfQAuccfigYtJleOHJeaEaGayxZ12ciCaFeHIzPkW9TFE4FZ6ee55qE3-a0YtGRmgDI1T4GFz1rXIRNDnjkzz--0T83Z6nrGfX5LlKTDxQOGw98D8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3H_hbZR0-VbCtRWhbksN70T-JU7Kzl2Sf-5VeOV0upS71mpssYW_EXTQEtKTAFUwJitEgry-uCD7GFtpHI9Y336-uwRe_vSlDlD9rcj-kI8pwK5hoPnF1LpKf_ww6vPQcvhk8OlWFh9yAAIhId-PKnKTowyYdncyvIH-CJSy6rOh-4ae3qAdMZO9HbovjWCnWN6_7fo6P5-h_p8P-OCr6nA5Hwc4nwa4ycdmn7T5RHUvOs7sxKLw0WHpDnjVMFZzfi9IXgPPQlhhcLPcJ6UU8ZtS6UWA7aD256SULJkBXZwFDHdh-FhzbAaB7lPE0e0EEO_JHThrmgvwFCP-07DVQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ry9qO4Ae_mG4Mv6C30KQmOz1n6ehSDAm28537Jw_DJUW-gp72l9wk5WfWU1jAiF6PYhOMlMn2npgHzEjXFtjQyQKh4Dv9ke-k3FvrQwI75Z36KCs2Jnt-PMUgcrEVUX4ZM3E9c7NejzBqZIfSZQd31CDDw4r_Y0GD59ZaJyNmTOPW4SSCVc-896b3rjPz38dT-EbcEMrhyMvbKkZ3U1ai_MWpuZ5hvTOF9nu_pWWcE5qGVCnWzQ1pFTFJpHdTiPWs-4ZXCkss09J-plZh-D_L_fbUxTGuJJkWoBsH-RP-TiB7i2trqOR1AtUBxCdF6-uB1-wkOlzRbVRlPS5q7MDzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ry9qO4Ae_mG4Mv6C30KQmOz1n6ehSDAm28537Jw_DJUW-gp72l9wk5WfWU1jAiF6PYhOMlMn2npgHzEjXFtjQyQKh4Dv9ke-k3FvrQwI75Z36KCs2Jnt-PMUgcrEVUX4ZM3E9c7NejzBqZIfSZQd31CDDw4r_Y0GD59ZaJyNmTOPW4SSCVc-896b3rjPz38dT-EbcEMrhyMvbKkZ3U1ai_MWpuZ5hvTOF9nu_pWWcE5qGVCnWzQ1pFTFJpHdTiPWs-4ZXCkss09J-plZh-D_L_fbUxTGuJJkWoBsH-RP-TiB7i2trqOR1AtUBxCdF6-uB1-wkOlzRbVRlPS5q7MDzTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=vq7jFRKlkHcXx1rcQ4WxgihBLqlE1W6lUGnx4pO1eHZT86PXGb4Qrk4il9zgtOP4_HhXQmomfwasj2hBIclxINszoo-KYTUqtYgD0ilbzmxYbPmmoD27q6Bb2QtpSEYANDPMJ85shp15SF5hAQv8N6sIqDbpFv4eVZiRcKZ3SaC2jA6BHAzCpYE1mXkbTtZ9rUd6A2NUfFU-SHa_wlmgWBGfKu9x8YHXJwjoTQB6PmPVGaGQ6Lqs4p6sykP27EZbQ4Gv3pnVapVOeQ1qI4Wc_BTCLl9o32Gre8Wcm4wJvLsDHy_mgsw2IRurUNQ6j8PoW8xr0v0_q1Dd0pCjBsqYVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=vq7jFRKlkHcXx1rcQ4WxgihBLqlE1W6lUGnx4pO1eHZT86PXGb4Qrk4il9zgtOP4_HhXQmomfwasj2hBIclxINszoo-KYTUqtYgD0ilbzmxYbPmmoD27q6Bb2QtpSEYANDPMJ85shp15SF5hAQv8N6sIqDbpFv4eVZiRcKZ3SaC2jA6BHAzCpYE1mXkbTtZ9rUd6A2NUfFU-SHa_wlmgWBGfKu9x8YHXJwjoTQB6PmPVGaGQ6Lqs4p6sykP27EZbQ4Gv3pnVapVOeQ1qI4Wc_BTCLl9o32Gre8Wcm4wJvLsDHy_mgsw2IRurUNQ6j8PoW8xr0v0_q1Dd0pCjBsqYVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kbM2NscHwpkJBvBCpdgfmInDSNWu55nkjiG6PzHgaisv3sExllLqTQlhMn94-j7kFltiqwyZJQyVsjSPP4t1k5ADtQ2Czf88IZnEIjIzPIoryVZExDLX75xK27qS6jDTI4zrCVYDjFc_9wVIxcBo9Paa23pO1MuGWFWepKQCOK6bKRuqTulYJAAA7aABszJmO8l2geYRcRYG59BEzfj3SYGDgtVnqA-AITu9fe5gzYaLOLjSijmDURCJPwPnBl12ptM2NISbktUGUk9XyUiy80YaD9O9ABpDZHmEkw7V-yRulgshGvCzg2fdzIrJrqEvGuYbGCxgq7sYquDn-3Q-5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3IGZz5abBR_uLF73HYv2rbpiI9V-g6t8DKli_O5uflvBuAFyW37nVvW1_DBqjune80K5eLgpzx2whfQYA6-nIAa2mY5ljH80OJrw4Sqlw0MV3sV8Ax8xaDQ-AMrrY7k-x7_B-_ePOu8SWMN1ZXMuphFyDxyILBcbZdERVZ8BZRYeeJAeJbOeTZR26uN7n702nyz4krZkpyJuLF9nxXlC32-dSKRYsJ9Z_htw6BrImcO8ZUs8OCevnW86hTZEJSO25eTbkvyLbuyP0jbdYPVf0h-HYMT0lWNO4ScDvw7MR7bHnU-OUooYzboEi1rolEAIK2o7_zImVd0iHm870N8yQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=eHSyh61cROak51TwIqSqfXHiu2ILMRQ-DYaHzr1sNPCOkj_VS-Zgi1IT1JxFDBzfNpaPfek5paxspbQXHXwOehvnSyvfRdMC44a1M8yTewHHN5XAoHRd7Po-5vXxjNe9ndKTHnq5AH9-udRExWawW530NDDfKgF_UPBbEh0UVQCecIjuE9oCxfHFeP05ROD0_afJDH3ACQISJc79RTo4wyx9mkVjKYLkNuuYgANfiBw1WUj3ck8ZGJXP4J8Tk8Ey9sZiKSaQKLIPwsFAGkfi2XOFQdaDLOXjPWZduFtuoXUuSjXhuw-ptcn7YJKLv7Mse9ce6wt4Sh_ScdVOFh8Kvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=eHSyh61cROak51TwIqSqfXHiu2ILMRQ-DYaHzr1sNPCOkj_VS-Zgi1IT1JxFDBzfNpaPfek5paxspbQXHXwOehvnSyvfRdMC44a1M8yTewHHN5XAoHRd7Po-5vXxjNe9ndKTHnq5AH9-udRExWawW530NDDfKgF_UPBbEh0UVQCecIjuE9oCxfHFeP05ROD0_afJDH3ACQISJc79RTo4wyx9mkVjKYLkNuuYgANfiBw1WUj3ck8ZGJXP4J8Tk8Ey9sZiKSaQKLIPwsFAGkfi2XOFQdaDLOXjPWZduFtuoXUuSjXhuw-ptcn7YJKLv7Mse9ce6wt4Sh_ScdVOFh8Kvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSBWXdnzsnRYh2thQjYqjrCup7ZJo-NAnG0YmsDUO5aI2jE-4RZK95mv71UF2C5YaLpi3lkdVcasxsG0ngrIzaax88v_SqtAAVKetG6TsrAQi7PsqSnYIbhEZS7Y4GZwI9dsolwKB0xTlu94cw4A3ipWiamNamLCQgx_NPOADKGC-KWGCDRX2KnKWOTFwTLLV6MT1bK6Rhyyqi1yhIcDLNAmL4qcVVc3Xzp_3DsMB_b7V_RR8V3M3He0Me_tL--VS5Oc6dYf2G40Sn7Xo5AGc9FvBsemZOLeq82G5CwfUOkoablRV4jhFlDHH2IUCvB1EfWlBlkkR6VqWJIO_-e0kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2sYRluxStk3-9R0e9Bj_02tHRlMN5YtW3QSxeIPZEDZpogOaJLWIaW7jgIAYiqx3eThPyrWrZbmpY3PuPxvjx_qorGzhjz2GIvT39d2I-E8sE_zihiyYqMtrhKgeLGawV-PmBVJtf4pOScsj9j6LZvwTpPjtHq0VvGgFGuarktAHu1oI9LqJIhVNeuZHtDKOdScL-FlrQvayC4FjoHngfRleAQs_7l1YCgGKKXJCUm61dpYX1r73d7kiC7rbvIYJK0WuAqAvnfTbSBz6jindoBbJ5nMQR_rcRkHz9I-WELULITHfKoUyq3U9koIlyamVj9Ua_w7WHXxhGgNQLPdNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mb8vHPHPqX6xmty-1sDt5KdyqlsK0jWTAwKkJUAdKt4i4PNdY1dVmyAqsh97LBMOuXaI6I6psC6RLT5HX04Mf0f0JMRk5ZsiTl80sN8udmFHXzr4Xd4xF8fZAdn8t6yTA2UnnWwDYJCD7j1buTuA86iQ7E8FD4s0oIFEhL-q0GdY-O8VgHHU05I67p0Bk3QJEPv5nD_Znh7imL7SfcaiZqnr7f18v4cFFYUNvNrOSE3OCKvaN921j1Jtfb-usF1aEbHjVMhbG0cKPhBntMy4YjVDJJpyJoh8Aor9rX0ZHjvRtGWEMjxBzl3UQpOW-gkfubh5Y7NypWOUWoe00HvovQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lnUlyfpaghHeFPSu4Q2k7WCdZZOKnfye5gSxObuBN2qj_MWylSSC4JHlAiQKcqjG0nrayJiEU91uLRc7Ak8FKXM0rmhhX7r082dBI5Zxc4YWUumzN4-bnr4cOoi-NTzNhxa2oiuttA9-E6lMrWtjoAvCEIStDafIoOG78Sj25vH7A4toLNrfkDoF5Alshm4bNyYjguWBSJpzkvCDcHdJKIOEGEmWxFPqLf_5txipmEwI89WrUVTDTmsNo2rm6VTPuHBxEJwTeVF_eqNqC4jfQDyBLK2-RK43r--bAWve1sd2p1jYLWLkIy51tlQSvFxU3G4IkVqJ-gYMezNxVl3Uyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=lnUlyfpaghHeFPSu4Q2k7WCdZZOKnfye5gSxObuBN2qj_MWylSSC4JHlAiQKcqjG0nrayJiEU91uLRc7Ak8FKXM0rmhhX7r082dBI5Zxc4YWUumzN4-bnr4cOoi-NTzNhxa2oiuttA9-E6lMrWtjoAvCEIStDafIoOG78Sj25vH7A4toLNrfkDoF5Alshm4bNyYjguWBSJpzkvCDcHdJKIOEGEmWxFPqLf_5txipmEwI89WrUVTDTmsNo2rm6VTPuHBxEJwTeVF_eqNqC4jfQDyBLK2-RK43r--bAWve1sd2p1jYLWLkIy51tlQSvFxU3G4IkVqJ-gYMezNxVl3Uyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=mOAHvVloRE2uJPGDiYDWx4QB8EFOYEQCYs2ojOVdVL5B4gVyFPjwN8jFqDgwk09Qh6UdoBaA9qgcxOwUJRRf9FHnHMG4cyhSlh9BVze92EOPMdSo9n5nk-pO6fPO-2Q_aXU6IC_4GXbFIAyIhPF6PPS65I0OCJhJ8CBmrLTsGCPBoyNLkN0hHCOgBwsO6EdAplLhgkwxjTT2ftnGe1gwg4nrvBfCnYkrhrsRZoxqOs-ZvwLVzZJlDiTFcCYvXWfFtMJYCwtTNWBfeltBO86uGaGCppPkGy6e6W91Jy5ykEnZHle42SBw8aXuwCE3vUBGQPz7Vi4-amKjbLkxK-Oyiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=mOAHvVloRE2uJPGDiYDWx4QB8EFOYEQCYs2ojOVdVL5B4gVyFPjwN8jFqDgwk09Qh6UdoBaA9qgcxOwUJRRf9FHnHMG4cyhSlh9BVze92EOPMdSo9n5nk-pO6fPO-2Q_aXU6IC_4GXbFIAyIhPF6PPS65I0OCJhJ8CBmrLTsGCPBoyNLkN0hHCOgBwsO6EdAplLhgkwxjTT2ftnGe1gwg4nrvBfCnYkrhrsRZoxqOs-ZvwLVzZJlDiTFcCYvXWfFtMJYCwtTNWBfeltBO86uGaGCppPkGy6e6W91Jy5ykEnZHle42SBw8aXuwCE3vUBGQPz7Vi4-amKjbLkxK-Oyiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=lgLelFhunQ6hMGoLikg4Yfka4AoVd3JqMsAA_m8FhiiYkFB-NTUfnUtk3Ry05pYmGaBp29EOqCd0cwGHvLJ2aLE9JPUaC-_D5wa6Aj0eWS5Tv5ddBTP4JNRwkGUIkefzh8yPxZJk_bvHprcpk0jZXu2diVYqhx1hjqeEOw1udC_7zo-8OhAPcVOBjis_Ok4sYZV8f73xU1cRoXNF2NWeAN_xQpOsWwUvQzonml8e76tSlzxonlzzCnQChzFz2ovRaUoAmdZT-js1N3UvTJa7rcecZvsRH4TNN8ltoEyMy1U_Xd7uPVHJEyQhONprXWm0XbwXhs-H7UKtmH8xI5Xwbyraz-gLa86EZq9_BcsdDR1uuLi4Vf6vGVmQvM2har0XCrMTKTGtBO2zW9JeE8X17DpI0acEGta5Mw5x1CCwnK-osxfRjgFT9JCMdWP3QS5ZIy9aZMP1L9BrBuhTT-N2Q0wd8yEwnJBWbZHnA_uEff8h1EadCvcgAelpgQk0HWARlbr0-iY1uD0PDkA6DsFhF41BRskw9kGoLJwrwOXguemN5K9bK-p87nDkzZjfjqEauTP8RJ4xh2nZsxTpoocgrAJHwNZzykg6U3RAed72Nh042Yyw0MgpN-Q7-lHeZDgINqmvgc_Ti4426xXW4wJAcJWyGM9EbCnluL_QIxbcRGY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=lgLelFhunQ6hMGoLikg4Yfka4AoVd3JqMsAA_m8FhiiYkFB-NTUfnUtk3Ry05pYmGaBp29EOqCd0cwGHvLJ2aLE9JPUaC-_D5wa6Aj0eWS5Tv5ddBTP4JNRwkGUIkefzh8yPxZJk_bvHprcpk0jZXu2diVYqhx1hjqeEOw1udC_7zo-8OhAPcVOBjis_Ok4sYZV8f73xU1cRoXNF2NWeAN_xQpOsWwUvQzonml8e76tSlzxonlzzCnQChzFz2ovRaUoAmdZT-js1N3UvTJa7rcecZvsRH4TNN8ltoEyMy1U_Xd7uPVHJEyQhONprXWm0XbwXhs-H7UKtmH8xI5Xwbyraz-gLa86EZq9_BcsdDR1uuLi4Vf6vGVmQvM2har0XCrMTKTGtBO2zW9JeE8X17DpI0acEGta5Mw5x1CCwnK-osxfRjgFT9JCMdWP3QS5ZIy9aZMP1L9BrBuhTT-N2Q0wd8yEwnJBWbZHnA_uEff8h1EadCvcgAelpgQk0HWARlbr0-iY1uD0PDkA6DsFhF41BRskw9kGoLJwrwOXguemN5K9bK-p87nDkzZjfjqEauTP8RJ4xh2nZsxTpoocgrAJHwNZzykg6U3RAed72Nh042Yyw0MgpN-Q7-lHeZDgINqmvgc_Ti4426xXW4wJAcJWyGM9EbCnluL_QIxbcRGY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LE1eEK2aFYsr3yG1hTZDGC1CskrNpZlbd7g6LOOrvbQ8ogwRvgVsM7_pzpzqShXrtqS-dGg8UKkbxONltkDIl135oN5kD3sIsOWgMoevKHlmFBJJRHh2IaNQqfKgbytqgTHTam1sEL2oom_Pe4VwzMaqCXDB7mBzreTjiMGvH37qQwmyrnDHicoONzHMbW3O96Gr_AIqo74Rt-tb4XVrI3JOEikGmIkZN-QlRCs1qbTsvo8_HyIKq-2pTYzxk062JV7xM-0Yy4W_uKeA8dlzO6JCkwWpFPVg3W0PsOYs-rrk9icGZfz9v7Nn4VB9eWQJGn4PTAYUYUY1ufTwSFSf9mKB9KpRa09dVBzWK-W4HZ_cn8MN2QT6sI90HlZfzXEu5PPNvFE7JrPwannQjBMZ4hKmFK2VfGS8Xg4-UCHbR-xiBHQlkDS7BPPdtw_tc2qCdssadJ1_-H8Y7jOHU0-ZnVolR69pMy130zsWLTQM7BaZZUJ1Z0o6MOpArsyhPFzJI8eNyIUvxkR-AzTukNq8PgjNuerCeYM-H6_1-MN32GWfIwJraeMJEeyKsLvu0BP991rR67g2MjDrMmWIlo8H-hxua1_Oz5Bg2XGLImo9_HURyQsSMppAS7IbdqorwnQHWQ-WNBN3Z8Mfg4s6QF5arcxEHcrzBFaYNuTxVRGI65w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LE1eEK2aFYsr3yG1hTZDGC1CskrNpZlbd7g6LOOrvbQ8ogwRvgVsM7_pzpzqShXrtqS-dGg8UKkbxONltkDIl135oN5kD3sIsOWgMoevKHlmFBJJRHh2IaNQqfKgbytqgTHTam1sEL2oom_Pe4VwzMaqCXDB7mBzreTjiMGvH37qQwmyrnDHicoONzHMbW3O96Gr_AIqo74Rt-tb4XVrI3JOEikGmIkZN-QlRCs1qbTsvo8_HyIKq-2pTYzxk062JV7xM-0Yy4W_uKeA8dlzO6JCkwWpFPVg3W0PsOYs-rrk9icGZfz9v7Nn4VB9eWQJGn4PTAYUYUY1ufTwSFSf9mKB9KpRa09dVBzWK-W4HZ_cn8MN2QT6sI90HlZfzXEu5PPNvFE7JrPwannQjBMZ4hKmFK2VfGS8Xg4-UCHbR-xiBHQlkDS7BPPdtw_tc2qCdssadJ1_-H8Y7jOHU0-ZnVolR69pMy130zsWLTQM7BaZZUJ1Z0o6MOpArsyhPFzJI8eNyIUvxkR-AzTukNq8PgjNuerCeYM-H6_1-MN32GWfIwJraeMJEeyKsLvu0BP991rR67g2MjDrMmWIlo8H-hxua1_Oz5Bg2XGLImo9_HURyQsSMppAS7IbdqorwnQHWQ-WNBN3Z8Mfg4s6QF5arcxEHcrzBFaYNuTxVRGI65w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MlcuvqCdNIIvNTmM_NKMvVmUWfw2Bd5YdfCn-31Q7WTFbTCZ9k4yY0A6Fuw-go5AIWZQXshDgq5Y7_J1T1b5I4K5BcWQXSv-0TvQaSbiqRcw443AicU2VVVCS5dJDD6n6jeHgd6XjGABDZsc2P_tke9Mjhz-X_NBkL6PDaiADYjxXGgWrC-JMnmYbZCYdtPcqI3_BIhAzowXZpVpp3TiRywlgxUReyIXTa8pFRs2X9gx2JshMa7yx7NLcmDYBnFVeOvWqgB3x72VYcRg6ITTy7aq0VqLN2_lQFMqZdTG2zTtPttC80NpF8k8YA6wlVk0n_yOaSI21SN36lEU59WIaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=MlcuvqCdNIIvNTmM_NKMvVmUWfw2Bd5YdfCn-31Q7WTFbTCZ9k4yY0A6Fuw-go5AIWZQXshDgq5Y7_J1T1b5I4K5BcWQXSv-0TvQaSbiqRcw443AicU2VVVCS5dJDD6n6jeHgd6XjGABDZsc2P_tke9Mjhz-X_NBkL6PDaiADYjxXGgWrC-JMnmYbZCYdtPcqI3_BIhAzowXZpVpp3TiRywlgxUReyIXTa8pFRs2X9gx2JshMa7yx7NLcmDYBnFVeOvWqgB3x72VYcRg6ITTy7aq0VqLN2_lQFMqZdTG2zTtPttC80NpF8k8YA6wlVk0n_yOaSI21SN36lEU59WIaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XxanmYacILSU2yiV_CXhN09nj_T2GPuze_GZJZ18ezZovfDDlePo4ZipCJQsCp-jam7G17ztcYAEN_QZNqqFxUnfj_n6dyW3KrWdlE9B8SyHr9shexTcNKa2tS9ac4O-ZZb4_KF9g7gpZOEo9s0MBI9fT1CYlhl-dcy3eUp3dLqqCw73ohLOTgTTFkKlxK7adtFaSu2GCIqhfkf1PtE5nV3rxKjE7fGo-HqFwIJuCLqqx980w6r_KtU_XBsA2eFJTHBHvFkPnXfM0bIfAPRBlTRZxNtYYW38SYctzQBxBH1Aznz9KYjlxJGAriTwc_S8X4zHk78Dq9odsMlso-Tm3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=QWg7OUYG5DKS3k9Skjc93pPh3y0wQpQ19ejO6f3UMAA-NU_gIZCjHbXEk0go5EO9rK_hrDFgllENo8LjqeKFNAhMs7YT-rppc_KXhxS4XyraWyrx0PU5PSWHgYW0A4l57pH-GOmhp479_0rCqUs2ULzoDLDIOFVUnXML7RAIvGyQyMhhnQ6kJDYw_GqIMdpEw-PChl9W2Ig8WlQ7_GMSfPK3MfNjsnoP5jQFi3ZrQ6-TnegdNU5MtzKuBT3xXrUE_h7Uuw5uC_CC-tm8yo7x7iCVHzidaWc6lRsItu58hNnqzoj0RaGUbY-CQgAcjjndsrkhpxd3EgjRVAOS33e0DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=QWg7OUYG5DKS3k9Skjc93pPh3y0wQpQ19ejO6f3UMAA-NU_gIZCjHbXEk0go5EO9rK_hrDFgllENo8LjqeKFNAhMs7YT-rppc_KXhxS4XyraWyrx0PU5PSWHgYW0A4l57pH-GOmhp479_0rCqUs2ULzoDLDIOFVUnXML7RAIvGyQyMhhnQ6kJDYw_GqIMdpEw-PChl9W2Ig8WlQ7_GMSfPK3MfNjsnoP5jQFi3ZrQ6-TnegdNU5MtzKuBT3xXrUE_h7Uuw5uC_CC-tm8yo7x7iCVHzidaWc6lRsItu58hNnqzoj0RaGUbY-CQgAcjjndsrkhpxd3EgjRVAOS33e0DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=thRIPJpcZdD1H2JRwsLe1gMjb6i7YhOtcQ7EKJ4S8_LihbBKyep4fNMpbT5ZSVh2hv9HEmGMaj_ASXDRJXwhekPBMQNpSukAF0bDnhSW1Y9A1nC9uVbQbnj8_8eJ-SCYonWFkJ1tHtQypzoHdg7edUVEMg4yRNkr9UY65fLQ8F9rn2jm2YNoOEG_TCc-ud12FpNtIv7c0kMO1GFCeWsZ5V_GcupMkRAdUaw0LhIjjygb5tfKFTlJt1fGKXCge7-lrZoFw7j7MWYXPJwBNRDIrhfo00Vz422kY6yDskAEUCztf7lJosNTYvGxYXFe8RaB941B1-xcgkPmQh9zodO2GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=thRIPJpcZdD1H2JRwsLe1gMjb6i7YhOtcQ7EKJ4S8_LihbBKyep4fNMpbT5ZSVh2hv9HEmGMaj_ASXDRJXwhekPBMQNpSukAF0bDnhSW1Y9A1nC9uVbQbnj8_8eJ-SCYonWFkJ1tHtQypzoHdg7edUVEMg4yRNkr9UY65fLQ8F9rn2jm2YNoOEG_TCc-ud12FpNtIv7c0kMO1GFCeWsZ5V_GcupMkRAdUaw0LhIjjygb5tfKFTlJt1fGKXCge7-lrZoFw7j7MWYXPJwBNRDIrhfo00Vz422kY6yDskAEUCztf7lJosNTYvGxYXFe8RaB941B1-xcgkPmQh9zodO2GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l-sv6HFzzGU-0juopmK4vvbDrTdvgGVdlo-5y2meBDIMgCYdtkNAKgKwiRcP4eGuCk1KMAYCYLt5Ic3jE5ua_ZP3JIRlY0GwcxjdFWuv-sTU3BoIkZL8-g4kQC60IlYRRaoox0HLfDw7vRbAdAIwRGvhxNdqU_QP2eTFteeNHWwpufVg1SPPQmaNhf5b6O_oCPixd_ZCwtl3hC_HNBrYv6o4o7VL9BJZ9jPrkNjCbpMQ1LyaL_g4SS1eRXSbbCdJN4WUVBEBz-FcQf40fewLlvWMhIs5-CXK6ulukEM1w_Fku39sy-puE3P2WA7Pe-Y98VgeNdWGjbXnQiR8BbGfuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K2t5Fev-vhanGaVWuOM8Hrl_B8rN5Q4yBDsehLuGMsA3z_sphBakm6rLD2b5uHTW-rMZ9fXkDnWdatd_q_6C6RuCeHXP1C50mjw_2NEYypxnU5z_vd9hIuUgvmCnhaSSVKUDxUkFrBTX9hR0uT8N4dpl19TSW-U_QxpGPXLLrQZbWv_aCVXSxESDS-ihThspmnM4Nu8x9jHIYH3PSpfDBMyy8zVwY9zDAuklSL1SKKxCJ058fiq4akwTkw4y8l0J0BnrYq3RjkbZDSIhss1tqzSqakWmbsWdnWHCMACevXh53Stm4er_MStdgpjJjYbU3WUvY1Ar8u4XDw-molweLQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3XCpib15kblyNum3kvmmGUWO1bYzg9LMyhG3D6qaRUelkN9CuoRPXOBpIcE8A7X9T2rLbpwQIwkYe50yutxK8u7LmNwJYzL3FlaJL8dG1kn8Xr0TNMQL__oMGJA0Wspv0MpJlrI-BnYMSwZ0_Zp1K58p0J3m7S9hq3K_Q1JYawzn7h-1lsMZTkHLw0UXYfvNc1H1dLOXmhMHULy6gWS0jYqdaXzl0yIl-KiWygVptko6fI-xwhFbytWRbLjmH82zG03trtMO21ZSMJOoxkPThafT92qEsfpEnlU-vsavNKVGQaQs8c98PkYl10KYMifESm7BOfu1BGllQuac44LKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG9jCTUxnZWwshpqM-4v3u8wzSBfT17FNFtaV9lsAT3vl0GCObrUDgmjsORWe-AEB077s8HvUAuUiLYHqpcU6TcC4EuIbq6EUh1PiKUqVwCF2Zs5zuJm2-JUkA9i1kYQATz185wiw4gES6fd6E4raVFUJhUftb_PYvQ0eoKaT6FSdymz3-ZbIyZ8Baiue_G7Hx12nj_JvhKVlQw4CmMGtFnqzO0JrjTIwtWKr60vI4CT2P2jkeocUEcDsl084bXgb5Z9NWXvGSOX2wSfmCqBqeWApG0gaE-oPbbUmhcJGvYz-beJfpmWeaNfYhJn_xXbLIYppv5cZds65LYoMwTPBg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tW92bMQvxGD7ZgFf2jSr9G4HScy357MKkdf4DKVRvRj01j5A1YX7K_gg559g0rgl26eRKyCbBKwu47IV3Y-3AT4x17r-nGYbAZNZMmQWrcizbaiBx944NsLLnQW4l_za7YXF_NIcwv1rweGSX58mp4EXLYJH5CUOI0j-o_NmsJEDE8BTSZYZ5QPDdJaN6jAK8wN8-g3ynKKdGyxD4YzQImmtN3-v59ZdGWJJPxxaH0iBO9O_sXRdp7jOJ9mykTmOarsumjhx7cyNOf2n_48fGOR6KQMQLZBujqCCTG5y4md9zshjbUbbBJtxYGlL9IGjuJCyMwFmEta-9fcZXiK8sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EBiWPwzuWpn2FNSAZJjTMzhrecXtFHbE9qLqbnLP3VlX2pJccyhnjT3YnybWqZtmh2q8ZvAo44gzU4tpczy9iToN_DfN9qjYJ3tvjx8k4QC_0GkJtYmf36hKBYtmfRZpiiPM0Smra8XTjBNKBQiAg2lgjsUYACT11Kb5HHFLiEvn7wO-Jnny6sud161u75rcOzVtmupaxsAP0WLGYtyTIanlpAyfbrZu2dY__Mwx0DvURZmGQbYg7upcSoPu8KB46SmcFtsEvHj7EHiF0R-uX2YyGR-3K69B-_UrHHpQmfGXaf9xelCNNt_RI-GeoPYv_QYBhEXvZzOq5eieCrFXtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vh4ipLkxitby4Mfb09lwcszT48icDvik1e-HsOO1GFpDPLTlS6_Junp5OFRLSMbWTSVaPuyK1pCvlVUBGkVq5aEJaXsMg9QUjsGWoH814yE0ox-s5ZIxueSwfTOZBwJvpGaWxIHa3K6bjaKFiee2FH4aYFQdRYsXeTyjMjGi0SC2ZEFzYFni143fttpHcUqzQnQpjkfcEh-gtyNUM8jb6IKVh3AifMn0jWszpOjAzJbltcO1nXvVecX8IZRn2QrdO9Z3xf52Baw4poWWJbmLM4rRMY12CvNF5yzuids9dgocqpGtszEJZwkEa-w-OZuAWXh2hwuqXuz895xvjpxobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HkOM13euCmndowf_1NFEIX-i--hrswy2aoGLcdr8fp6ULBLQ6mASM-cRapogaSm55TZMRUzMrs8A9lnlez0OIanl1Z0FQDp439T8vizsU3serk22RqE0v2ymkwpyICEA6WIkMDSouCGRPIsOVbQGyMeLnUs1xKltpsX3JnzxsuSMcmixxZtgmxAyvy9TuXNyThshOim1Pjx9K2DIz1dJ2YrBfFMyMAbqqPdJRLj0JuPazqPkgdb4dIv1DkH_iBdCMOFl2ME3TyHL4pfTnFo0y8oBufIQgzppWysvesHbP_BnR3Dn1DLBUk0nFKfCrlvYbDSght1IhWYXfCJ1iqVYsw.jpg" alt="photo" loading="lazy"/></div>
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
