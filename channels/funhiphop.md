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
<img src="https://cdn4.telesco.pe/file/B2g8qpBPbOZbGgIEA7yodNbMZg4prkUUAeC9QXOkjivxfkCHT9Nc6eK5CwE0ybva8XB4N3agcRYRzlaAe9t0IQkgxkS9nTmT5HhF25D6EjgnbT91HyGuQNCCYf7Y1AcFLAHPEwm0qsRGQm6pDatlTdMZ5V3jhSAuClSczCbUMZtIhVfNwAepEA2ePUtKBrVEBPwmc6YOn_fVxgJO_IrFrz7ltvW48n-6N_bdTl53Ml0AX9KosOfKAhqJ3TnFZmGLwEpnQ0de9f28XXu0NOmkQ5aNz7S0gnU_k2C6wwke5K9_4C4E2xyDAtjCGyBqxeD-LMYG19JPPMAdhIveLtjLzA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 252K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 18:44:52</div>
<hr>

<div class="tg-post" id="msg-84189">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfSR-boixScPlwen9McCa34o2DJxbbmIoF-jc2e4dm_IcnjEPEK0VN7xR9dPLpcsJvh0Uk5K3uJsKxzp28JPSo_SK5gN9WqjN8BXxZT0zVMHc0lot8_IalH1ICgXrtI3sRSyCvfSs8-pWC5-R_3KFFEmQeX-lVp5lqPAKKrKOgWHpcV9ZRT6npEOtuNfNawuhQosJZfitYUSGnVHqPE9U8jN6r9Z8GqJWNwbryJyBYPAVOdcHWWjq1rspfRkX7FhOSeJOzDlUcm58hM3iwLUdov2hbS2MWZ7DPROevS7TVy1Og15AcMk6lar2MNuObO-DS07HbVjsOUUp6kigV_msw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرون و کاگان به نام "انکار" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1.57K · <a href="https://t.me/funhiphop/84189" target="_blank">📅 18:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84188">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 2.37K · <a href="https://t.me/funhiphop/84188" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84187">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udlPWh5c-TZjraFKua5GVggXvwSICsDk0ImM-wo5qpkasoCudGALdj7wJBflNlXYEprAo0bFK8jltHW85WiTJhTfEwE7mb_YTJhADkbwJbmz420JS3bR4y40_AIqelG6oK9oEci5gT55-1bXHWPkQoZE9Ac72sThYG7NIhxeVRkqUlTQ7mojT8nq16dnD4oRidwrRfeoZd0rMAKgh2ewpTN0eeBWhYmDBqVtiiFarWHTCIjOw-MvE4JzrrqmHWpu47Ww0ei20Hb_6dVdlojwxOAlrcxplqjtI9Niz3HwssaahXTQqREP9gBnGNUrrMu5FxuqWIvUKDrGfdwYpGN7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد لیتو و بیگ شگی به نام "1.6" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.49K · <a href="https://t.me/funhiphop/84187" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84186">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4Pz6UITZwjxvHgmW5davWDS6pneLB8wjEjTZzjJgXp44Xe4Lt4vGnHge0L9c6cKBDcP-mzrlzW1KnxLKokM9yUribl-R9dcRDsnCXL-bUimXkWNIeqR4h5mCeMOiyyTE_s1YAMuosIUJwAFLrC5djGtg9yfW9lSF-vZxoE2F8_Bl2POm3L2Mlh_-w8vTNvK0z1mhA3vSK_w1YSKYA0tQZozfVW7pg3c6gB1jWIUbOf4zTfW-X__AeAPlubOOKmAZuN8TbldwELZe0kKuA-b1VBC0aMquOX929-XChYncQOvHJnLva5jKTxzHQC_ir2G65t61sXcJjCI4H4SvQWPrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاره شدم این چرا اینجوریهههه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/funhiphop/84186" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84185">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=dt78gj6XlN0EUM5xAmpOIIJzvVg0_CQs5f8FWNWw7-AI1rtoizDcqax5N2rz2UqxqVsD2G2qoZw-PE01qdcqAR1iD2YUlw8t5eJtCnZ8SVu6UnODA84sO6Zpu242WwDPk9TQyVQ2b0mBJtvIST8IXBR8GIu3-vZhTLKTQT30n3PbYLiKpqJGNWV-Icq9VhGOharFHXvZxBOBPTImf61RkNioDlzyCoYKXi4EJ61GoAeToUDj09dnGL4saeG0MaiHAr6W6yLYSGsXNVAhs3myt7B9s1qslbfN8_dP7euRX2gI_BQjPYQ27W2HNpc3q9C7UfacWKJxahTbxfrR8i23Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862ec698b.mp4?token=dt78gj6XlN0EUM5xAmpOIIJzvVg0_CQs5f8FWNWw7-AI1rtoizDcqax5N2rz2UqxqVsD2G2qoZw-PE01qdcqAR1iD2YUlw8t5eJtCnZ8SVu6UnODA84sO6Zpu242WwDPk9TQyVQ2b0mBJtvIST8IXBR8GIu3-vZhTLKTQT30n3PbYLiKpqJGNWV-Icq9VhGOharFHXvZxBOBPTImf61RkNioDlzyCoYKXi4EJ61GoAeToUDj09dnGL4saeG0MaiHAr6W6yLYSGsXNVAhs3myt7B9s1qslbfN8_dP7euRX2gI_BQjPYQ27W2HNpc3q9C7UfacWKJxahTbxfrR8i23Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هادی چوپان: یه ساله دارم کابوس میبینم؛ باورم نمیشه دیگه محبوبیت قبلو ندارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/funhiphop/84185" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84184">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84184" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/funhiphop/84184" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84183">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fxZZqxLBDM28LFfnUKl7i1if3nI-XvquDSBiA53WBdDIO2hpkGQmPjKFR1LE84F5dUVXOXU91TESy8QxLfwlRRrsKAKcqzTD0HPJtfcrDN4e9ucXMLbnFXWBel65_srXl0G08W4x0YNyEAe6ir0ZvFLgCcv5tBLb8XXcjFERsFEfqBX1hHP0QsOR7-1aa-ZQ8ZvUQVOcCvnY_v_AUlzo8EJd0S8yKdiqFlS-CW5UI-gwfeX3psRCExiGruLXg7TVl4gW8OIf8KRstJrkb8Pfo_E812FTaYf-_BeZaM-Qe9I9QdbSYQazF-oLKd5woomAXG6RSYq-y8NbtVQDbRiFdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g7
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/funhiphop/84183" target="_blank">📅 18:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84182">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ادم اخه طلا رو مجازی میخره</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/84182" target="_blank">📅 17:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84181">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">معلوم نیست کی خورده ولی نزدیک ۲۰۰ میلیون دلار اموال مردم تو میلی گلد بگا رفته و هیشکی پاسخگو نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/funhiphop/84181" target="_blank">📅 17:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84179">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=k3sGGbOBvN0q5ADJPowy5E7UzV4l54BeAGtPFQGERije3PJTknfNOD29yuR1rfStFDtVl-btoBvG2U8Lp3eldd1YqkrDI1CDIXYdFzN-R1xk1vDk6niJTnPCvIOJ-pFOW2-vZaW37SAhPy4JypLkVOZdZHEbNKyJo1JNrXL0U3Epw2ftNjjcW4REj6LMmQ-boHDIN_VAFLp9kBvIWQ2Acq2vEfDGLOqA9dcXqfUpxYasJehkyc9A2HlXMj4t3tQYy0lPRaZ5HHLWGiMbQVElQLg5OzUL6_J0J5zmnp-FXQAI908wXKlqh4PgnZmL8IRJXBtwUQboW-4G_ieCL7Csxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adf73bf24d.mp4?token=k3sGGbOBvN0q5ADJPowy5E7UzV4l54BeAGtPFQGERije3PJTknfNOD29yuR1rfStFDtVl-btoBvG2U8Lp3eldd1YqkrDI1CDIXYdFzN-R1xk1vDk6niJTnPCvIOJ-pFOW2-vZaW37SAhPy4JypLkVOZdZHEbNKyJo1JNrXL0U3Epw2ftNjjcW4REj6LMmQ-boHDIN_VAFLp9kBvIWQ2Acq2vEfDGLOqA9dcXqfUpxYasJehkyc9A2HlXMj4t3tQYy0lPRaZ5HHLWGiMbQVElQLg5OzUL6_J0J5zmnp-FXQAI908wXKlqh4PgnZmL8IRJXBtwUQboW-4G_ieCL7Csxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خارکسه حداقل بدون لهجه فارسی حرف بزن بعد بحث وطن و وطن پرستی بکن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/84179" target="_blank">📅 16:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84178">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">یه زمانی خارجی ها مسخرمون  میکردن بخاطر کالا برگ ۷ دلاری الان چطوری بگیم  شده ۱.۱۷ دلار
سخنگوی دولت: خبر خوش دارم اونم اینه که الحمدالله بحث کالابرگ حل شد و از نیمه دوم مهر کالابرگ رقمش میره بالاتر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/84178" target="_blank">📅 16:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84177">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">در همین حینی که قالیباف گفته اگه ما نفت نفروشیم هیچ کشوری نمیتونه بفروشه تو ۴۸ ساعت گذشته ۲۲ میلیون بشکه نفت از تنگه هرمز خارج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/84177" target="_blank">📅 16:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84176">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvNIQN3aS53vUI64aoC6KYa31wTXinA3X2ETLBG_oO3IHLUZSwRgymmJG8YcVc2gxSk8rWOhUcR6Kz4Q4CMHbEND8TOuszAiOtQnEZ5RxYgxYbLT4p79QClWIPYyJY-DmcJPrXlBVCVufl7bJHj8G9FIKNH56SwOJuLH4H-JneSgrXMCGwZaJ4OLRgTpRAAxba8GXG-5K6oCC1-nhLreLVEtCmOqG7oqh0V6f3UN2kdrEXqeY9NyQ4P_SaOlhpsGBduUbB5t76Cuqe8VUW3E1xO5GS-z9wOaJkmtpFroDD3wvPJBTkD_YCkh3fMKa3cCn9iLpkazA9_tL23uQ6mHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلار دیگ ترکراری شده لیر رفته بالا ۵ هزار تومن انشالا تا اخر ماه دیگ ۱۰ هزارتایی شدنش رو جشن میگیریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84176" target="_blank">📅 15:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84175">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/84175" target="_blank">📅 15:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84174">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آمریکا بعد از تحریم کل خطوط هواپیمایی ایران، الان فقط یه مجوز یک ماهه برا پروازای ایران و عراق با کلی شرط صادر کرده که توش فقط می‌تونه مسافر زیر نظارت کامل آمریکا بره نجف برا زیارت و باید از همون نجف هم برگرده ایران.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84174" target="_blank">📅 14:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84173">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">به کسی که حمایت نمیکنه ازتون فحش میدید به کسیم که حمایت میکنه ازتون و بگا میره میخندید
واقعا آدمای کصخلی هستید</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84173" target="_blank">📅 13:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84172">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84172" target="_blank">📅 13:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDCSrTO59RIujVOvfmXYvaU2nSF6qAPr1MsAhUCJ42vLa9JEosgd2neWvBXs-wpxFnoJ38Fei_eZYGx1q9UtbUUNL7ThM4ALp3-QMb7ouai9SzeBhw5dKPclJuHeVIqgwqc6nKX8KwMxv1cVi0O1jFUGc9zO7I0JXzUDdg46GLLsvWnu7drGsbkBKrNcqgG6BOhzFWWznKuynB7mYerKLOI7AUFoAU4bSTkwbJLVS4inN1CVcimnuAXRS_b6-lFdzJo3wd04xp6js11T4leL8_ubjucSnjUrc1thsfEKrl0aQLmSAebeEMzBcMm520L79eKYVM8n5pbGww3NAtOO4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هردو فروشگاه لوازم آرایشی بهداشتی ربکا قادری داخل ایران پلمپ شد و تمام اموالش داخل ایران مصادره شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84171" target="_blank">📅 13:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84170">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
مردم آمریکا تحمل کنید کمک در راه است
سپاه یه نامه زده خطاب به مردم آمریکا: حساب خودتان را از اشغالگران فلسطین که خواه ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند، جدا کنید، ما می‌توانیم همزیستی مسالمت‌آمیزی با هم داشته باشیم.
دولت یاغی، کودک‌کش، شهوتران و بی‌خرد را کنار بگذارید، امور خود را به‌جای اراذل به اندیشمندان بسپارید و به آنها یادآوری کنید که دنیا عوض شده است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84170" target="_blank">📅 13:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84169">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=UW8OzQLvXAnpAXjR_mUCfwX9kAlM1NVxwWK609wsbZbWHUVcZSeRKZFPxZQktEhtW4m-riTWRT9CmFueZbdHlxQWffgENHZ4Kud_RuvX0gV8egKKNYy3dX_MngwJPNyioVbJr3vPg4oqtSvd12UE666K34H3ME8oFh59p4WJQ58dxczjZ-f7nRajOZz4vHyqQLjKs0nodPE6dc_XmR561YzXXrPuhJuPE21-6ezy0IIV8qokG6pK4U5mvVItjlZMBHdpZBBg9bFVeRyavfV9VsRo12XdPl6FXx39gcaFHQPtjjXSm5tQSDhRvRtHom4LOlhhcpFZAW-ReVzwjwKrug" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7e6ffd31df.mp4?token=UW8OzQLvXAnpAXjR_mUCfwX9kAlM1NVxwWK609wsbZbWHUVcZSeRKZFPxZQktEhtW4m-riTWRT9CmFueZbdHlxQWffgENHZ4Kud_RuvX0gV8egKKNYy3dX_MngwJPNyioVbJr3vPg4oqtSvd12UE666K34H3ME8oFh59p4WJQ58dxczjZ-f7nRajOZz4vHyqQLjKs0nodPE6dc_XmR561YzXXrPuhJuPE21-6ezy0IIV8qokG6pK4U5mvVItjlZMBHdpZBBg9bFVeRyavfV9VsRo12XdPl6FXx39gcaFHQPtjjXSm5tQSDhRvRtHom4LOlhhcpFZAW-ReVzwjwKrug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
به نظرتون ویناک به داریوش چی داده که داریوش حاضر شده چنین شاهکاری رو خلق کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84169" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84168">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تو این دوسال آنچلوتی که سرمربی تیم ملی برزیله بیشتر از سرمربی های رئال به رئال خدمت کرده با مصدوم کردن رافینیا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84168" target="_blank">📅 13:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84167">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mfw5-QTJrVRqglykazqEIipyKuXVkkMmpREFZBF4mfIuYnoEvFzbgn52qTSvYMa-7tksdzlf5C36GLb00ErjOJel0xu4sUZm01oW_dXn4_L5z_wiCIgjTfbG9o0QckKPrqxvahl8Gd_H8vOLU6EXvMzX5U74CCw5J0hrQS_JUDvRIzZkSmuc3Vsl2CPsLrINHPcrKUpsECtxIgIswASmPF9Uc3cJfCAPLTzlGzadHFdSN2fdsDhdfMpsPI4vZOpxm-YzaCPlfQxhk0aTaQhEkAtHNoKpOdG5tpvACzfDyFYpbEzJJIyc4h7vurJwwD4K8A36-c_mTUQhKIih3z301Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو دین یهودیت چیزی به نام تغییر دین از دین دیگری به یهودی وجود نداره، هرکی یهودیه باید تو خونش باشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84167" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84166">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/84166" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VBumJgzxc5h-haNafgKnpCVnk3h084v8H1e3dRGxUhKzA5qvO6OWFB9PUWfRNP4amfNK8Bqo4CQtP4nuOSfSK447wQMY8I2R9QMAMmpZx77zsvwn_oiO5HENFyB3pR4hpiUVZWqx44-AlRjA4V5F58nbRC2pMNJRV15qI3zx33Xab10jjhV6ZTXd2RD-m8YLLPzkh9sI2t3nJ_4stLpn0r2HPaVI2W7vzp2pu3w2_-K2ZBuBjiaG1lY-dIdqx1yRsPkvEcrHokg4TIqlFMER0lFMbYfk6dUEauRHOTlo2_6H_xSF1Aiv3FwUxB9DY65reM0k02zr4ln-8ld48d8Abg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
نبرد حساس یوزها مقابل روسیه در دیداری دوستانه
‼️
🇮🇷
ایران
🆚
🇷🇺
روسیه
🕔
ساعت 20:00 به وقت ایران
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r7
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84165" target="_blank">📅 12:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">سخنگوی قوه قضاییه:پرونده حقوقی ترور سردار سلیمانی در دادگستری تهران تشکیل شد که سه هزار و ۳۱۷ نفر شاکی داشت
رأی این پرونده دو سال و نیم پیش صادر شد و بر اساس آن، سردمداران دولت آمریکا به پرداخت ۴۸ میلیارد دلار محکوم شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/84164" target="_blank">📅 12:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ما میگیم اعدام فوری بیرانوند دور میدون آزادی شما میگید بره سربازی؟</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84163" target="_blank">📅 11:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/398fe520da.mp4?token=rxxQyj7JwOyk7fX1ihdlr4PY57f919_lzLZFL1m7ZINmjBknf7eio9jtfM95_b74ZNcAtLbULPMQS7uxUYkIQQVowr5peVWO0ABzawOMMfluKUefxbxI-0scN884PsN30gWg9H8blIrEWN6Xs25a_qQfG_aGDTt9o0U2VgqE1GV74ttXR75Fk9HOipLIrouNKUxM4bI94ST4Yse8LDMVB6tfVHEbaAntHM6ti33YZIDgF2xIW_ruzXHkBDzW9K94cknk_peJPJAOzTu-3P1bIVGic5KZq6zEDiXi83JK9O0_1Matq8BYY-7QumCQGnRJCnUFP5_wW7bnCaWYJe7RrrUFHcK_zX6XFIAUjeVmqbhlaSuZ2VshiWgnXdFTgf0WnLT-Ls1-PioHmg4lH7bcMF1YPfK2tc8VmjZLTC4_3aMafhzBJfr7HowaXQrECVTgw0L1SDf1XgS6TStwKGv2w4J4NmqDPmq4OEt7K8Bt3rl5pulQFHxdImb__mktLuz0NsUvXZLNixdanev6OC8BqM3hnoKOeeh_2jKO8zDz_SLCKjd6JwsrlXkAFpsfpxoBgQczQI87WfgMighnoNKO-MrzmdFnet6qhCTgCR7UAfOdhXoVBsvKINWAGD5jMsmkvzXIc0hPH9lmnpCMtZsT7t5mS9Wcy4hafo4PmH6mpbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/398fe520da.mp4?token=rxxQyj7JwOyk7fX1ihdlr4PY57f919_lzLZFL1m7ZINmjBknf7eio9jtfM95_b74ZNcAtLbULPMQS7uxUYkIQQVowr5peVWO0ABzawOMMfluKUefxbxI-0scN884PsN30gWg9H8blIrEWN6Xs25a_qQfG_aGDTt9o0U2VgqE1GV74ttXR75Fk9HOipLIrouNKUxM4bI94ST4Yse8LDMVB6tfVHEbaAntHM6ti33YZIDgF2xIW_ruzXHkBDzW9K94cknk_peJPJAOzTu-3P1bIVGic5KZq6zEDiXi83JK9O0_1Matq8BYY-7QumCQGnRJCnUFP5_wW7bnCaWYJe7RrrUFHcK_zX6XFIAUjeVmqbhlaSuZ2VshiWgnXdFTgf0WnLT-Ls1-PioHmg4lH7bcMF1YPfK2tc8VmjZLTC4_3aMafhzBJfr7HowaXQrECVTgw0L1SDf1XgS6TStwKGv2w4J4NmqDPmq4OEt7K8Bt3rl5pulQFHxdImb__mktLuz0NsUvXZLNixdanev6OC8BqM3hnoKOeeh_2jKO8zDz_SLCKjd6JwsrlXkAFpsfpxoBgQczQI87WfgMighnoNKO-MrzmdFnet6qhCTgCR7UAfOdhXoVBsvKINWAGD5jMsmkvzXIc0hPH9lmnpCMtZsT7t5mS9Wcy4hafo4PmH6mpbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84162" target="_blank">📅 09:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">صبح دلار ۲۵۰ تومنیتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84161" target="_blank">📅 09:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">یسری رسانه میگن عراقچی قبول کرده تسلیم بشن و اورانیوم هارو بدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84160" target="_blank">📅 00:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مادر ترکیه گاییده شد که</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84159" target="_blank">📅 22:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قوه قضاییه: حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84158" target="_blank">📅 21:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDx4FvteXwj9e4OF20fpm-7umRycAPYN5LqWpB58d7HV5l2sUwP5g9J_hiMnfT5R6xs-nAiciWFjwoG9tC9Id77metNc9PL-qKv8A3bJUxlCKRT9piah5R3mJR-vhLhJr0lOsbawPFqurq6tMg7jtFhOSEGHlQxCP-EGP_qN2c6agpdWC5uTwX3NzmrBmrW1PTez1E3rAH6wAQCTMdhothVqkJS_dD1N6N7H1VObbnYt6xQWivGTQvvrOZnNFDCYzuty4avsr4RwsoZm8ymGk5hR3f50HtidoydIcfmGGEPwycb3yHhPfNSUl3tzy5Lzf1D0MsvF2SnZmGbJsmz4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قوه قضاییه:
حمید رسایی به بند ویژه روحانیت زندان اوین منتقل و رسما زندانی شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84157" target="_blank">📅 21:33 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_c6DVzRJt-Viev7AGwHNN5l4JYEKGjXa53xOg04Z6JIGALUEZksPmvIOkOzL5oXt5sFVaHVoE_DMpag5lB5lTkPp200SQsNEfFzgzEjismH1ShVQejIxxz9MI6yXKl6FENbAXHCkvvAO75AHOKzdTLQI7qPKl1wCIMIx7gxyQcjq2ExsdQLk0HTClLqBTcOo9a4_eL--nrGuLru5Dg6MnggasxGRxfNKEfNMnJO2fVquz-xagkMqosTr45fGgZ9Jc-Bo5pVhzI9Y7w1y8Pjhm8U6L5YNsb-7H03AZibqb08vf6Z3bJF8EBAmlcEp6Gsc-RTGy1XInFr7wp5RVJGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من وقتی یبار تصمیم میگیرن رو فرانسه بزنم بعد عمری
واکنش زیدان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84156" target="_blank">📅 21:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwS_gLwSmBv6Ph5Bbu6K1FHgy2fYhw1PNHZAOmD3P-8jeWDbLeaig7FFJBh8-iyc4zAjUASvvQMzcSJUyODWwmaB0MQocegyqY39m4V2jA_yGWyyl2-ZbPvOmK0wuos1a371TRFK4uZTSVOwD4llfPayNEqr4gzU5Nr6q8fKzqfBgABRQz0ShtYnfBKwafuoIqZqFPwOU__8JQsZf6iyqoEetnkiTvmu5EiyWN2igmggKKosxyh-lzocW1fGUksH_wBDm_3llqAiTrklkiLqU8rHknQkHx8wzaJpI3r7h8M2mIfi2rMGldaQoIxbMx05TjPa_lhec7dWNkj_Z199Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تسلیت به دخترا
ایسم عکسش با زیدشو استوری کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84155" target="_blank">📅 21:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84154">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان
⭕
با تست رایگان + زیر مجموعه گیری با هر دعوت شما 10هزار تومان هدیه هم به شما و هم به طرف مقابل…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84154" target="_blank">📅 21:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LEyBYjlr2icLExFF12j--ZWBFOi1T9KK22yCoAu8vHaHCmJXYe6vvQGH7deJxvEmXTbowqz57uMBtR_QpCxHFfb1Jd5z4WWKS7Ku9ndvCn8ggCNSqW45WqH_OLi7EiOhtuk25meGqySsbUxYdJxD3hcGoo88reMi0dEuGTqw2Y9gsHWLNDaBq-I4rEjpSp9cL7LOSmaIJwDULZ9O0TO5A6O1vJ544oufzGwvfPtYr77k5rB9keDyEFJGtE5HSxTaT2M1044Ip_yq74-HOvHvl6TQE6pdz2uw5c_SjlT2EcI3Ci_ek69ejy7YLIT7RpuZuW7MkXTbBT0lHK1viFdOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین کیفیت کانفیگ V2RaY با تخفیف و قیمت استثنایی
☑️
فروش ویژه کانفیگ های تانل با کمترین قیمت تلگرام همراه با ارائه  نمایندگی ویژه جهت فروش
❤️‍🔥
🟢
گیگی 2200 تومان
⭕
با تست رایگان + زیر مجموعه گیری با هر دعوت شما 10هزار تومان هدیه هم به شما و هم به طرف مقابل تعلق میگیره
🤩
🔖
جهت خرید و مشاهده محصولات:
@HyperPing_VPNBOT</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84153" target="_blank">📅 20:57 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=HbDmMvDH-qPowresK81ErXd0fGBm1_0tntAvRROrFy0TWmdPGOVrHQjP5YQ1VE7uqmUItA-RqylMGHp3VCfq4NS28eQs_JPStuxiY9d0qyL8UftclNssrKSRsnsZKKl84NAGb54P7U5mfl6MMzDGlZzI1SY5TYI_scIGuwtpcfHv4Zn9OZh5LSMB3LEpf5RYaGad_5HnMRig5COKuZFqyz_UChJ-8BKWl3krJA9ER1_G5u42mVgkN3N0rjJ7_qgGPQPA6voa7bJhMOvZ4LlJ_Kwm97TQhVpOwPjnxBYJrxMV2dQl8YYVJX598n3nln7dyNZgFaV5DiUkqf2iPWyPcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff9d6bc22.mp4?token=HbDmMvDH-qPowresK81ErXd0fGBm1_0tntAvRROrFy0TWmdPGOVrHQjP5YQ1VE7uqmUItA-RqylMGHp3VCfq4NS28eQs_JPStuxiY9d0qyL8UftclNssrKSRsnsZKKl84NAGb54P7U5mfl6MMzDGlZzI1SY5TYI_scIGuwtpcfHv4Zn9OZh5LSMB3LEpf5RYaGad_5HnMRig5COKuZFqyz_UChJ-8BKWl3krJA9ER1_G5u42mVgkN3N0rjJ7_qgGPQPA6voa7bJhMOvZ4LlJ_Kwm97TQhVpOwPjnxBYJrxMV2dQl8YYVJX598n3nln7dyNZgFaV5DiUkqf2iPWyPcjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حلال ترین استفاده از هوش مصنوعی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84152" target="_blank">📅 20:09 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسنپ پی روح و روان سالم چهار قسطه نمیفروشه؟</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84151" target="_blank">📅 19:38 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84150" target="_blank">📅 19:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwaQwsjtfE7PpnH3G8_FKXfiYNbofEeW5RO2qJhHfonX7kJPl0Q0L5fto64gG-w-3F-rp6AdXGz0O1MWvjIH70Im-63nckzZPQeOlPzhfr9Sch7v1F21p_hVJ_WYn4Uwaq6hvm-62dYEBnmkrTc3N9rCtBCR_6Mxe338cF7rsHYgNJT0hfVrKVfKsp91jbuzx9mU1eHQffIgFvA3-cqyU-G1tlxtfh9O2H21wfebwJGEDyWJMZDLT6Cqol_k6a5YjCT_COzZ6XfqLyybSowIjZB5-a9JbS2QYMe_dFeqouzL5wrtksIXIQ94zGo8EihNubRRXggXvtNlvEy87-RcDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید ناجی به نام "استار بوی" ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84149" target="_blank">📅 19:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AQfBktLklesjR50NFCeTfPRccp4C-m3tpZp6N8Gpt0QZQLU1zM0W1OI4yXjOt6i4MwNh-1KlpUzD8oanUXMCZHyte_7sZJFeyT06RPsUR7rC8T4Mv21mkaRXqrE_J81Pa9_I7e9wk61ZX6TGxjRUeef19TCq8giQXDkmTN9J9JIpVOQMm-EFAorXpX08FPE2YanRESam79HlQCXjFZ3X3VOAusDO19SYrg_clDx97bwLSKaUuiagmDAjNJ_zDj1e0RFqEm2oIZIRcAxRJXS7Hw-rPQVCwprbFrDF4E-FXMd8Z4EaV_4y5miARnsfUgKGsrhtfwivC_4KVfxRi8CszA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/213569f829.mp4?token=CXiLD4MoOH3tdBMXSayMUEuFi6uNHDte79JM8ZhZuFm5SvKEb0NmP9tmwpgKjFMWOeTxvuBbQ5K_PWd--04IlYCCSw2hvYSMbkQWsxQ1eO7yxkyEaI-6AaMQOoYAbNMjbRnbDYKM2XKFJZLMDv5b_bc88ztU1nnCSdmK8y8AQ-ATaAA3sJHdLRywLwNetjRbhKJUBmFyOrgrqK3seh2-6o5IHt8RhSZmuIRAndxqaUnteYfKVwvUdrnGCBuDMrIGlqpf51VJkRM_2IsVozdLcyYRQB8iFp_HGankBl0EmMoxHQUhxyTw-nQVA7BvXr1Ei8UVzlB0CMtxox-KPllzvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/213569f829.mp4?token=CXiLD4MoOH3tdBMXSayMUEuFi6uNHDte79JM8ZhZuFm5SvKEb0NmP9tmwpgKjFMWOeTxvuBbQ5K_PWd--04IlYCCSw2hvYSMbkQWsxQ1eO7yxkyEaI-6AaMQOoYAbNMjbRnbDYKM2XKFJZLMDv5b_bc88ztU1nnCSdmK8y8AQ-ATaAA3sJHdLRywLwNetjRbhKJUBmFyOrgrqK3seh2-6o5IHt8RhSZmuIRAndxqaUnteYfKVwvUdrnGCBuDMrIGlqpf51VJkRM_2IsVozdLcyYRQB8iFp_HGankBl0EmMoxHQUhxyTw-nQVA7BvXr1Ei8UVzlB0CMtxox-KPllzvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به این داداشمون دابمسش های دخترا با موزیکا علی گرامی و سجاد شاهی رو نشون ندید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84147" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84146" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84146" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84145">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u_Iwr7OTwvKREyQ9sPQotCvMUc8HJdVen3qdvCY7ENIktTYmFVTGuceCcLeTj7Pa_rTnks5rnRHqDByYzo0v8PaRBTXvycFL5-2NPtK5XlItEEiRkcRYbUswDF91mB1Z8hc-FN3oj1aAM5Ql628eMgcrkh1K-SV-N_WC1cnP5G0oPxwXiIJfot7TxI7YO-umbRKMbWnvgpjjFoGyUKqn9ynWmXWaQvN3UtVyNgvSJ6_89xzc2yiZK0mZI2kJbPwJjNYx4V_mMhV9MPJzI8BvlM-oHU1IVrmele2c-7nAbu-HPsaHoJspG3ihgDvrqlGJd21eji34xErwHdxnVhgz1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
برتری با کیست
⁉️
شاگردان زیدان کبیر در فرانسه یا کوین و رفقا در بلژیک
❓
🇧🇪
بلژیک
🆚
🇫🇷
فرانسه
🕔
ساعت 22:15 به وقت ایران
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
g6
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84145" target="_blank">📅 18:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84144">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">باز قیمت دلار رند شد ملت یادشون افتاد دلار گرونه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84144" target="_blank">📅 18:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84142">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نمیشه به دلیل تقلب های سیتی یدونه قهرمانی آسیا هم به پرسپولیس بدن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84142" target="_blank">📅 18:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84141">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ولی این انصاف نیست کانیه وست کیر خورد پسر عموش کیرش خورده شد کاسه کوزه ها سر من شکست</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84141" target="_blank">📅 18:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84140">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNo happy</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzL7M0xoocwvuvASOYGxTM63qFyXZffGY_0UC_ZNd4CxV6atFfe6vA9IwYg8yojChqfPozzlzkmcwJm61GJPx8z6JWu1OqXVheq6yRff79dfX8WdoVVn60h7usICc9s-GMYA5kBm4o_NaGC25XJCUDswIP4HoN01JKUl88Qmq3b695oHjv5bC3PG4pvWs1EFBGTcpUF8lw07Teq3GMTxTnRkBNJrhfbDR2w_MwNSyi_YNECdyD96W5M2-hruVeIG0TsSU5_favxGpX4SIvM5q9icKelOB8o1iKrLta-iUf_KJNKTaebeZoUtiFxQBmgUlR1hLt4GmPAHnt-d5WlBkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلم مهدی رسیدددددد</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84140" target="_blank">📅 18:10 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84139">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مجتبی خامنه ای: امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.  اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84139" target="_blank">📅 18:07 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84137">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مجتبی خامنه ای:
امروزه، برخی ما را به عنوان چهارمین ابرقدرت جهان معرفی می‌کنند. البته، آن‌ها این را بر اساس محاسبات دنیوی می‌گویند.
اما از نظر محاسبات الهی، ما به عنوان قدرتمندترین کشور جهان شناخته می‌شویم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84137" target="_blank">📅 17:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84136">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=Ne2M3O3GpxHuMxlAv9G2U3d0xZUMG09ypa37dlebBUCcYPXpwEcyiOhEs8PenLqP2bMY52wVqwz7SwSbf683GDa8MkyNkYxJhBUVzYm2MW2YcFiOZrcDArI_l35mdLUjYuIAnNQaYAP-msvMSKutRpHQj-uAp2H4z7Q9RVDsYil2Fv3NQ14fa0cjQ1b8dzO-BETytM1ALlmwZT7bVNYYO9WC547_4SR8qfdl5Gh13hk6R3NApnmB7mRLEJjElmKQK3TaG9HzWfaqzVYzNPz32SlR13dLG4Arxn0twb_-zjBhhsPEpa6igPuDAKrgXgSwhJ10AYjCdK_aG35TsCVXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f73abc8dd.mp4?token=Ne2M3O3GpxHuMxlAv9G2U3d0xZUMG09ypa37dlebBUCcYPXpwEcyiOhEs8PenLqP2bMY52wVqwz7SwSbf683GDa8MkyNkYxJhBUVzYm2MW2YcFiOZrcDArI_l35mdLUjYuIAnNQaYAP-msvMSKutRpHQj-uAp2H4z7Q9RVDsYil2Fv3NQ14fa0cjQ1b8dzO-BETytM1ALlmwZT7bVNYYO9WC547_4SR8qfdl5Gh13hk6R3NApnmB7mRLEJjElmKQK3TaG9HzWfaqzVYzNPz32SlR13dLG4Arxn0twb_-zjBhhsPEpa6igPuDAKrgXgSwhJ10AYjCdK_aG35TsCVXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول دونیته ها
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84136" target="_blank">📅 17:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84135">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۶ تا F35 دیگه جهت استحکام سازی پایه های مذاکرات از آمریکا به خاورمیانه اعزام شدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84135" target="_blank">📅 17:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84134">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دلار ۲۴۵
ترکوندی مذاکره، عالی بودی مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84134" target="_blank">📅 16:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84133">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">استاد بیژن مرتضوی اعلام کرد که نه بابا ایران کجا بود و نمی‌خوام حتی یک نت از موسیقی من... و از این حرفا.
ولی خبرنگاری که امروز صبح خبر برگشت استاد رو منتشر کرده بود خیلی اصرار داره که استاد همون‌جوری که تو اجرای جام‌جهانی تونست خیلی خفن بین جمعیت پنهان بشه، الان هم داره خیلی خوب پنهان کاری می‌کنه و همین خبرنگاره قراره ساعت ۹ شب یه سری عکس و سند از استاد پخش کنه که ثابت می‌کنن استاد ایرانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84133" target="_blank">📅 16:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84132">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwUNvnLYCWZERwa-EaXvzSPDR-6KOQXO4N8ODoKbfrINwYoYdBybRTb5FMHh2koOZpgayJc6P3xBKKOluWZco4z42EJ5dDzw1URrISfyRox3WiwEYJKCIG4-8_az7AX_o7oX1THPDWTum5_v1tc8W_3U6dfMF4d88VE1dflAGfDJmu4mf4FQqHsXwQq3ebQRhdgvscU5dS7rwudt2Xc9Tpp4-S2xdl9jcTNqUSyu9Bdefnj0kLbnAzhSw5gVqU2bXD90-JFcV25aNO56clnWaAaZ1hNrn-GBWyks2o9J2f4rG9KBVVgxbdOkmVnNbGQeso629navEy4M8tqNLZh1_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم کشوری که ای کیو چهارم جهان هست
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84132" target="_blank">📅 15:47 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84130">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به نمایندگی خبرنگاری فان هیپ هاپ سه نفر اول به این بازیکن ها رای دادم
1 بلینگهام
2 مسی
3 کواراتسخلیا</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84130" target="_blank">📅 15:18 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84129">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=MXhFQckvkfVU20tTSV9gzEIQ2T6FyKtdyMqmAYtfv_yLvy27bvRqIJs6fa2b_b8Dbo5U0pVQW0LJKxSLdFl3lTvPd_lwO853tw0Fb0NVqsJtSQgs2J-JqxCP8K668XDTfQ_Gm9ywqeEZDVrw7C6r6_oRjsqr4UTHWvAwujCh-ZCRKZY-Su8UhMq6ku5vmAX0xpIcrMRj40q0RVn5Z4qul_DS1e5F79N1shQv_9j3xTdbhqDVr2U6GDOVEmv_vBzRAq195LRXQ85p2OdTF8wjSJcCdP7dYiQBqboHu-X7EC61tXM5MNBvKsutIvc7a9YjGm--YShsuGKhsQ-FfLo6iIGd_for1VXjk_X0UPWwlAHYDpkwPHQBf8Y8S22_7hT1l_Gr0MqUFzJRNKarj-qlOvYyKwMZXufJ5f_LsLgHZ5_6opMg_bKjkjOx5lZXQoFisDZBc8AbhvUV6v7kyTia1qvQECD68bmFj75QCFsYrSaH2N51yvvWFK0oyBK3ReTWDPV76FiQC_lNEIthar8uooVS3cSbHIyCLAOorET7V6cKCvvvx2JUpiBzCfkeH1SzL3YYJXHee2jzWN1XIGW9qO4N9lCtKPQ-yLVbNw_tRt6UMzMXHOpzZfKv6MrahFnz2rOOchUrzUzHrll60VSwYgJCkXPKGo5SEQIfxfY0rH0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee4b03712b.mp4?token=MXhFQckvkfVU20tTSV9gzEIQ2T6FyKtdyMqmAYtfv_yLvy27bvRqIJs6fa2b_b8Dbo5U0pVQW0LJKxSLdFl3lTvPd_lwO853tw0Fb0NVqsJtSQgs2J-JqxCP8K668XDTfQ_Gm9ywqeEZDVrw7C6r6_oRjsqr4UTHWvAwujCh-ZCRKZY-Su8UhMq6ku5vmAX0xpIcrMRj40q0RVn5Z4qul_DS1e5F79N1shQv_9j3xTdbhqDVr2U6GDOVEmv_vBzRAq195LRXQ85p2OdTF8wjSJcCdP7dYiQBqboHu-X7EC61tXM5MNBvKsutIvc7a9YjGm--YShsuGKhsQ-FfLo6iIGd_for1VXjk_X0UPWwlAHYDpkwPHQBf8Y8S22_7hT1l_Gr0MqUFzJRNKarj-qlOvYyKwMZXufJ5f_LsLgHZ5_6opMg_bKjkjOx5lZXQoFisDZBc8AbhvUV6v7kyTia1qvQECD68bmFj75QCFsYrSaH2N51yvvWFK0oyBK3ReTWDPV76FiQC_lNEIthar8uooVS3cSbHIyCLAOorET7V6cKCvvvx2JUpiBzCfkeH1SzL3YYJXHee2jzWN1XIGW9qO4N9lCtKPQ-yLVbNw_tRt6UMzMXHOpzZfKv6MrahFnz2rOOchUrzUzHrll60VSwYgJCkXPKGo5SEQIfxfY0rH0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رای گیری توپ طلا هم تموم شده ۴ ابان برنده رو اعلام میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84129" target="_blank">📅 15:08 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84128">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dduh8uLbdsmuGh3pHjj4q0OHeGo_N2uUuzypY-xx2DLwfDj87maa_B3oiukdsR_tvBWYIlcTNNr9UQnc8WtjOpNTNjYJFSV7wgb9tyRWRmU4j-kvAVAMhG3hAFRCKx06sxGzqoqXLTrqW10sPn6f1xQq5zzyuZ6cAeXa2TxV1A-lv-_4hiyrdLSid0fYhL-Phg6aK_weBALm6KzqpdwrdTTLwn7Hr2kekoSHnRx8flphThDhBYSYUaLChu7bnC8iOJRAB76BPd6QRHrJC8Dou1PvbkFjDM3-aoKV3Z9rlppRR-KkvwsmFp-DVET18d4vIBI88vBksF4wRZE4bnfQyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما که راضی هستیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84128" target="_blank">📅 14:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84127">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=IZEFXncTCc0Pl4UhnBBEce2EjX-gVpgZwI4F1XVPmfsaoDMjS-5_SCAtLfw0zlcq81xHArMsWBy0_NsDR22ek93HHLqYERYPiy0NG9TgPIdIV6CSq2ZhuY96Y3jcoHrOVAO1OEmiT1cltDfhQJGXi31q8FmeB4Lasp_-4k7KK2ZGsF591npkXkSSO8p7H-HjcH5ketaq89eH2vh3A-6oa4jnBbACDRWe6nPBXG5cIyzxTgqHQgSPGpHRaMYZPZH6W8ZxxWue54cI1CCBe_ixu3DwPz5mVK2jwS40JRG9av1Fczb31TM7mZThHKTHu1xG880OZcomk5aO9DOkm66IJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e988dd3baa.mp4?token=IZEFXncTCc0Pl4UhnBBEce2EjX-gVpgZwI4F1XVPmfsaoDMjS-5_SCAtLfw0zlcq81xHArMsWBy0_NsDR22ek93HHLqYERYPiy0NG9TgPIdIV6CSq2ZhuY96Y3jcoHrOVAO1OEmiT1cltDfhQJGXi31q8FmeB4Lasp_-4k7KK2ZGsF591npkXkSSO8p7H-HjcH5ketaq89eH2vh3A-6oa4jnBbACDRWe6nPBXG5cIyzxTgqHQgSPGpHRaMYZPZH6W8ZxxWue54cI1CCBe_ixu3DwPz5mVK2jwS40JRG9av1Fczb31TM7mZThHKTHu1xG880OZcomk5aO9DOkm66IJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش امین تیجی به گل کاشته‌ی دیشب مسی و فحاشی ناموسی وی به کیرستانو رونالدو
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84127" target="_blank">📅 13:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84126">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IC7V2NR9Y8P1pJ_-itOkWCI_wgUIB9hQWEKS4n8m4nLrYclJ2uev4fur6MqWjQ3WkP9ExoEcD0HBL8LdsbMvNmtYJimKu84_ma2FtFs-G8d0mr4fG4ExaoXI7lbOPCZl6hgQa5BmC1Fwq2gDCn1vHmUadAvjpLsoCoZy3cL0eid1hh-3ZBZWnhqBzZqPhXmP7hBSIF0DUpFQ__Se4UYW6j83Byx_13yi0iIaNskGQpgY25x6oyN6ES94Nc8ASOq5LbTnUnIRmF_b5rfrsJS1zaypZq5jV4wlcajCiR7GQxsSY-L6rd3QVgUVbA_qoD6VW1NW2zZYIbttfWrYOx6glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخجون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84126" target="_blank">📅 13:45 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84124">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e46577007d.mp4?token=sJO_xOC-LMGUKr8mPLN7derI7DoBSfOjD-xR3rLN2ujANGHFap-l-cayevh7e6tBzZzwZYfb3JyfYfvfbLK_4aZ8H8v6CKRUhqJuTsobpkxXbELXjwDzLOZOuoqkgjZc6ZIIPrwWnFWLAGSJuPvsKKt1I3g4hA7GIOaCW8XXt-lE3q6YaNIZ9Q-c_o9SKT2tdtnYiQlyieu0VUkn9uQZjxskblbWyQbepLkd0JoZlMOTHXu1M7go0IPDf6tm-aPNXmFGOo9r31aWupixjuff81MZhv9v-abhTeaDr4yG1so64ClIkIFXgYPlnzsKFpxms8rGR9l_3lS6zXfjm0Z7Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e46577007d.mp4?token=sJO_xOC-LMGUKr8mPLN7derI7DoBSfOjD-xR3rLN2ujANGHFap-l-cayevh7e6tBzZzwZYfb3JyfYfvfbLK_4aZ8H8v6CKRUhqJuTsobpkxXbELXjwDzLOZOuoqkgjZc6ZIIPrwWnFWLAGSJuPvsKKt1I3g4hA7GIOaCW8XXt-lE3q6YaNIZ9Q-c_o9SKT2tdtnYiQlyieu0VUkn9uQZjxskblbWyQbepLkd0JoZlMOTHXu1M7go0IPDf6tm-aPNXmFGOo9r31aWupixjuff81MZhv9v-abhTeaDr4yG1so64ClIkIFXgYPlnzsKFpxms8rGR9l_3lS6zXfjm0Z7Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوس دخترای چرسی و تیجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84124" target="_blank">📅 13:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84123">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=FsgfajTI5TBf_evuSxq525iEv8ilt6Z54Ut6rT8tWonJ-5b3C2UqntC8WPpOFmvJsmj7C_Uhk-n9GZWM4Ux6y8-TUq-z6GaEqHUvczHJSud4JwrwHXIL6_c0q6_JAyI-mHGOi6fMEpjuOTpgR7tBilv_84Mvh05lClPemyQUEbKnI2lIyzmr-1-9tbX9LrxlNVXoMaQaM4W4RXAjwOLqrSWpgls5q8w_QDiOqd5-f7tVuGaY-0_HYTaONYJqr06E2QAcKC0E8mrPgOsazTGFZyGyPqRnLvyo1zcBSR1hbAvY5q-jNZJIrNoXed7elXjpYwa7_pisD1BAGHIf7zWAfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00bebdd4e5.mp4?token=FsgfajTI5TBf_evuSxq525iEv8ilt6Z54Ut6rT8tWonJ-5b3C2UqntC8WPpOFmvJsmj7C_Uhk-n9GZWM4Ux6y8-TUq-z6GaEqHUvczHJSud4JwrwHXIL6_c0q6_JAyI-mHGOi6fMEpjuOTpgR7tBilv_84Mvh05lClPemyQUEbKnI2lIyzmr-1-9tbX9LrxlNVXoMaQaM4W4RXAjwOLqrSWpgls5q8w_QDiOqd5-f7tVuGaY-0_HYTaONYJqr06E2QAcKC0E8mrPgOsazTGFZyGyPqRnLvyo1zcBSR1hbAvY5q-jNZJIrNoXed7elXjpYwa7_pisD1BAGHIf7zWAfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از ۵۰۰ بیلبورد دیجیتال در خیابان های منهتن نیویورک خطرات ایران هسته ای رو نشون میدن،
احتمالا این اقدام برای آماده سازی افکار عمومی و برای شروع یه جنگ بزرگ صورت گرفته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84123" target="_blank">📅 13:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84122">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ناو هواپیمابر یو اس اس تئودور روزولت CVN-71 راهی خاورمیانه شد
تئودور روزولت قرار است جایگزین ناو هواپیمابر یواس‌اس جورج واشنگتن شود. مدت این استقرار بیش از ۷ ماه پیش‌بینی شده و خدمه برای مأموریتی طولانی‌تر از حد معمول آماده شده‌اند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84122" target="_blank">📅 13:05 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84121">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mhVwOMtRHrYBGtkwQ6CGM8IkJoHIicYI3ut0DTpOr_jO9dLj2AguDNgiWd0O8MJhX6ZQi7NJDurfRI5wf99sFJp409LbPEbI5CGo-ApOMYxKOe70lj103xxlp122DUyLYhrdBnixhfrggJKfHFLV0lM1xy-YUJurgNX_qwDf-O9D584_pyPkdra_TQpCBOrX-OkIVAPG6rjoqWSASijJhIBWzTKMs1k7mY6TKG8YwCRrrQTivrKU6OxJ4Yatt0WzoQ56TyrywRt3bSDRir9GLGKc5rcfd4wHk9QK4ev_hP7pFhMWIbi0I0z625MzQZnVojxPh_84wHLcc18H6ijvRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بوی جنگ میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84121" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84120">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ritzobet.apk</div>
  <div class="tg-doc-extra">45.3 MB</div>
</div>
<a href="https://t.me/funhiphop/84120" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84120" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84119">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI3QrGopc3SCkleuh56BPhy7B5R5Hh3NjcD1QGn5CVNh6yCcUELR19zBOAOHKpbPoImkHqAvPDLgE4ZkiL-IgUsYEU0WU73IBi5nehbWG9mXx8Jzd3fXqVFGVNO8M-A7t86jKoFFx89eb1m433rMLs5W6Ao1oUyGfbTW2kdabqn4bBWNVeilxbeNQNGQyPDkYhD82DevdPZ_R8rkAjzFz8XQjjbCsdNfOofMbJ_1f7YSq4fV8JNeBkOrxbFbwsAKIrERe-OqdXHgDfOWJY3_W-xOzQmHCy_OhVydHc8UFBV4LCO_MgrcoT6UaLTSlqEvxqwku1V_jnzYiGPZYQsmzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👏
یک بار شارژ کن ، دوبار شارژشو‌ این طرح اختصاصی ریتزوبت برای کاربرای فارسی زبان خودش رو از دست نده
🔵
اولین پلتفرم جهانی و اسپانسر لیگ هلند محیط امن و حرفه ای برای عاشقان شرط بندی فوتبال
⚡️
واریز آنی با کریپتو
⚡️
تسویه‌حساب سریع و مطمئن
⚡️
دسترسی آسان و بدون دردسر
⚡️
محیط حرفه‌ای برای شرط‌بندی و کازینو
🚀
همین حالا ثبت‌نام کن و تجربه‌ای متفاوت از شرط‌بندی آنلاین رو شروع کن.
📲
اپلیکیشن موبایل برای اندروید
🌐
https://RitzoBet.com
پشتیبان فارسی سایت ریتزوبت
👇
🅰
r6
⚡️
@RitzoBetsupports</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/84119" target="_blank">📅 12:50 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84118">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">حتی تصور نوازندگی بی‌نظیر و پشت صحنه‌ی استاد بیژن مرتضوی تو کنسرت مشترک استاد نامجو و قیصر با حضور افتخاری مینا نامداری، چشمام رو اکلیلی می‌کنه.
🥹
🫠
همیشه می‌دونستم آقای پزشکیان از خودمونه
❤️
#فرق_می‌کنه_کی_رئیس‌جمهور_باشه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84118" target="_blank">📅 12:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84117">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMn1PPuKyBeSE5vFZvGII44fsgzVYELTDHUJzNBqogalJtDWskw-0Dumjkynu5RwVAAhy7FaM9qukG6BW6REQMyTyHg1G9LHybnUtEVqTDLOrGK9xIuNDFJ8OhK7vCp-V3bOUBp1BWn9nd0F_7gPGysXVJlzaDyAYxsCQHAaQzR5EhmbNSsWHJnNIf4tBbLfmphLoXhhA33yTM44pyNKIwOKiR_4M0zp_gR0F3AdWA4pzeKh4pZ1qcvEYaQ_-BEaSkHfavRzQ7LZQ3loWA7w9PXbAcOkNySqnFkEJH1Ib_c4-4j_EVJG2lYQVp0oumwTvNBcfyYwGjN5vwxBquDj_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری و حمایت هیپ‌هاپولوژیست از کنسرت اخیر بیگ‌شگی که خبر از احتمال همکاری این دو نفر در آینده‌ای نزدیک می‌دهد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84117" target="_blank">📅 11:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84116">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f68DosT2dMSGcaKb3GV551O1QGum0rb5zny51HVgIF-hFFjTVb-Vq_itTSuNOjgqIi22r1Ke3RRr1S65R3273xE6KV5dfVi7J_0jR3ZrGHqo10r7PJA3B6PwJiLdNjOX7EiVwNPqgAkDfv0M5sj9_LeBGKK8xg-0uxuJXPP0103Zj6qlCMTT0igYIQpmwTu66E0XXFY5wUrKmW6qumOlxoZK3l2RUzdUMruCsexfi6QSq7kI6BrRXDdASY30_fBr-woEd5m11lRtFLVcgzRhkm7AegCKxp3E3iE7JzX0vYD0UVDdga_P3I_xzZSsQXJ-xxmKNbuQMgpQkJnRmgOCQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستانی که نگران مهاجرتشون هستند ذره‌ای نگران نباشند و گول تبلیغات رسانه‌ای دشمنان رو هم نخورند.
دریای خزر هنوز با پذیرش خطرات کاملا احتمالی تقریبا باز هستش.
در کنار کلاس‌های آیلتس و تافل و خوردن ۸ لیوان آب و قوز نکردن، کلاس شنا رو هم با جدیت پیگیری باشید به زودی تورهای فرار و استتار در اعماق خزر با امکانات و قیمت‌های ویژه موجود میشه می‌تونید بدون محدودیت شرکت کنید.
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84116" target="_blank">📅 11:23 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84115">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ناو هواپیمابر تئودور روزولت آمریکا هم پس از نهایی شدن مراحل آماده‌سازی راهی خاورمیانه شد تا نشون بده دکتر عراقچی حتی تو نیویورک هم با تعهد کاری و تکنیکال عمل می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84115" target="_blank">📅 10:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84114">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DyRxNJSyc4i8c9Fe0iCVY8bJDH21Lx8LT287Nvd9kivJ3-GCaMA1OMm9lH4hTNe1nURK8SRVwuRObBXSPwcDK-mpuDyMwgSYcappcscyVzNgnf4KUjneYe1T_bYMsheE3V2TGf32Bgaw51aHO4xTQkpzecA6rUfFDJbrMdSxgAwO_SiFhCAlTx0y9Qj6mkojU75-yCFN96Xf_lvCGgPwLBD7Luqrw-QrBtUlzHUxhfkaHRnId5elatF9qaFLi_kdLVD88oUkbFoSWOqzf1R73kwGiejhP4AAkSxUFu1hsMkQdFWWa55Nb5XZCJ1clR3T7AUylu6W5xH3N6MO3hqK9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر حیف شد وارد مارکت ترکیه نشدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84114" target="_blank">📅 01:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سلام بیایید چنلم
https://t.me/+q5Ml6Hl1Af5lMTI0</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84112" target="_blank">📅 00:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84110">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aqyLWy_FPwtrjZPshrPqSvAMfiBrvBAqK3GnRXbyO-OYTy8hhEbwiYQhDsS6PKvhSF0e0hwNUyfAVbOTMlLPIlApfejVR71FL12RQi0BIFLLLO352vkO4589FeCFLgDxogjNendkrlPH9xabcVW4aErdIZ5ZYL7cKJXtDoLH738fuTC0HoXCm4Y8qCHD-VpDSXK3jFfDoZ1vCVMFIHp75BFyrR1mrouryflCK0OwUKBoJ5MtH6GOhhWi0Gx2J9bb4ujj5-4xnrU1a4jAG6SqzWWl11NIC7iuaVR7clPzh1SPhUHi942h5BGArt0CKz0M72-OhmfnsTghG8TxXR-oXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vaVAwVKuRXAbrVBtwwEybxCIS8VfYaHki1oKndrR--MuZLSEcAemVRJvQ-cmMXQHEBIt-zh8hQnROVjyFcD-Pv1isCv3Q9wrLtFPpFyYQFA-bswkRe9pC0BH56HRxheN4lgsmhr2vi9RzmF2QrkdOKdxa_buNEILkHtmQnUM7gk7wHqtNuoraCbIzrZhc74TEkoI8mooCdsGGhqghyXmmMAF4It8534eV7zMpMpLWfMoT3HkAgSY4Gw_3OYr1wVnFwMYKmyQNfI7wvXdaXfSskRDzV9-sBVLD-ACHlQderjwANW13SPWb2ix9KhqbD8a1m2MH0FDzPEVXQqLL8CSTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به مناسبت شاتای جدید سیدنی سوئینی موافقید کیری اورریتده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84110" target="_blank">📅 23:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84109">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZNsA-yK-PBzIS2VxgXQorUBRnYvknn_3LGOG5hnJU2Z2tU2FIm7PWsE5mlz6joN41S30SjcNnKpXOmZNnl24lFLQQ2BrduuoIIo7dtDRHbpTTCyxe8_O2PiJaiy7eBKoPbq671Pduh7MlfQvaUvkj-y7BY9j4jb5h-TjEffd1iCh0StfgeCFaOwr5sCwydIBYqOBRkGLkbUoZZl9gKYMb4mkuyX-FzNNY82D6CwDx-HajJVnlYZBJCYYCskbycB13pJaBenNAhTzaFBQjOcMU8kHdWfCOhqte945qpyFmGrdQ10KoFGBWpznijRti8fJe2NRBBSNXV7cwuDeTKxUSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشبینی ایلان ماسک از آینده‌ هوش مصنوعی:
2029: ربات های اپتیموس از بهترین جراحان جهان پیشی میگیرند.
2030: هوش مصنوعی از هوش ترکیبی تمام بشریت پیشی میگیرد.
2031: ربات های انسان نما از صد میلیون فراتر میرود.
2032: اقتصاد جهان دوبرابر میشود.
2035: درآمد تضمین شده بدون نیاز به کار کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84109" target="_blank">📅 22:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84105">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">عراقچی:
غنی‌سازی ۶۰٪ غیرقانونی نیست و برای اهداف صلح‌آمیزه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84105" target="_blank">📅 21:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84104">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">از روزی که وزیر نیرو گفته ناترازی برق نداریم و دیگه قطع نمیشه بجای روزی یبار روزی دوبار برقمون میره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84104" target="_blank">📅 19:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84103">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=rc8Sq9FBa2ib_zwhnb-ck_sr2gnbgw4axkpsgBwi9UIHMoKsFktdGN6AxRbD1jfiZnTbmiwyebs6mSlweXO1CSxI2dFbyq2DZkZgVbAJ_31rghXV7TI-9TSEIum-2XwiKMmCo8QJ0eYqV5BinPBEf3ndNxOuVUySqN6QMv3yNY_L4z2EmCavSPbdv0O2dDD4YUqba6tnLPcBq1TUU4KdYwItYU6Y1uii42p2EKhJiiJXpyj1-0_gN4PurWrgwgsKDfPdpwkVqpIAWZGsLB7O8i61F20qhGm17iqRGhCyDBYT0tRStuEBda1M5TVLRpbJtb4R_B7YjjpxhW2jhf2s3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ce0419e2.mp4?token=rc8Sq9FBa2ib_zwhnb-ck_sr2gnbgw4axkpsgBwi9UIHMoKsFktdGN6AxRbD1jfiZnTbmiwyebs6mSlweXO1CSxI2dFbyq2DZkZgVbAJ_31rghXV7TI-9TSEIum-2XwiKMmCo8QJ0eYqV5BinPBEf3ndNxOuVUySqN6QMv3yNY_L4z2EmCavSPbdv0O2dDD4YUqba6tnLPcBq1TUU4KdYwItYU6Y1uii42p2EKhJiiJXpyj1-0_gN4PurWrgwgsKDfPdpwkVqpIAWZGsLB7O8i61F20qhGm17iqRGhCyDBYT0tRStuEBda1M5TVLRpbJtb4R_B7YjjpxhW2jhf2s3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی برنامه دیت ناشناس، یه دختر مدعی شد بلده یه طوری نگاه کنه، که باهاش می‌تونه مخ هر پسری رو بزنه
و در نهایت این شاهکار رو خلق کرد:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84103" target="_blank">📅 19:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdiyar</strong></div>
<div class="tg-text">کاش اسم منو میذاشت</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84100" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGqkTsv-dK17GU6nVZiJ7MNcsjAOE3DqvOLrNRbbdTsU2JyD-apwjFGWpnKBprQHyFwMklUWIrn3lMgyxgszXV69lZzdK3SPOMkj6KvHrB7JN5cNpduvX59M57AA8T9HD9rmLiBEjupcc1nUYqK7w0iSQsgr8EkLDFg14zyVAXrkBzTHKcCs5IA8g202NKSu_ypxUZa1HUqJwpSR3O6vwWjdJCv0pF0_HDwtd2rRgRHrJPWWN5qLuLUhYx5aM7xPtG8Rg6cfhgY2NlLg8KFlNN6p_vU4j7v2XMktCK6rCBUAh6qns7FRK2nLhu1QemN3hsHb-YsHxdEknqK5K-Ij5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممد ناراحت نمیشه لنا اسم پتشو گذاشته تونی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84099" target="_blank">📅 17:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84096">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mIiWwuLEsWre-bUh7hqOXxE8ewPs8RvBuXvurSjCmQJdp_xH3Jxbtz6HX1TjbaYc8fvEw0uLAqZcKben_PJbV99NuMLm3aEzWrBwXOsDc4fhhaXmHD2ShuR2j2aFb46U7YjSnE3Ndmqg36UwCdj0fdrWbwnLrY_GDIRZuiKCypInGZ7035pDWNm0tcvuIs8iBayBtv_b1nYdDqTXECWhgQVBNAq_5UjT_6qU6dfATMK2ATIdzjyyeM8NPjztZxBU-ONHGd0cHGefGh-GFAE-MBSZzzWnirpB_fDiFfa-o2OZaJJOcszDG165uYc-dHNP4YrMgkAWM6K1GsuDxNFriA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vJcU13UyJg4Qh58bjObV7sJpKBAfPPCU7KJtxHKIPUiJ-3xxdbgl1qs3PYJ3ATUy4jR7DPYP6YsNIwPC-1RjX0Fvws22k3Ztv2ftoE4Bp7o5sQP8njaKpa_kQiCP9l184BcvK7kZTl9I4OnJtkQkAns8mXM-W1v8gcANIpu-RigDJC_EWo8ItrqUubICDnEHLNdozpTS8DjYNtCZpZdmPbvPVlSdYj_met6aiU5WBaLj0UELUQNHKpgq85vzYXvuNx-tQ_o-paqfjkfKey2T29BsjQT8_bA4qkHOA4ICD7__Tv4FvYEjhbFJTSAebddwATDmPnmdNzhU2sd6DAy1mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SIVqzGJgQC3GZvMzVas5Wbv2UU2-6H7Hz3fCDjxUH-TvXjw7s_cmXI9BZJzLGKPKRI7Fu50qpil3u9lZ7Drsh7RWd77NLxcxG2wWWYuBNAIUYnVKFzgX5j57XUxb60VoRCH2LaHD5nM14aunbdYut4asChrWp0YdiJSAxJQuYkgwbiB-ImjXNQWGD8jDjpqwZuUjEmmqQl3GL1--vzITJQTK83w-8700OIoWOzL1ukdqKAe2LfWYy7FqHjX6K-WDcy7v6EILB9e6-vOze4scDVVJ_79xo2MaHI-uKiP3C7F_iztOFdMTLs6T7Zm5XweLSMXwGkdEQWwXxEAVH_G-kg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست جدید ریری و کامنت های فرزندان فهیم کوروش زیر پستش:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84096" target="_blank">📅 16:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84095">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84095" target="_blank">📅 15:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84094">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MJFbdX7cfEVd2NLnGXzVpCAJDnV9xsmWn7sVfy6PoVrGElXFe3YsL_wIfRBRm4Q2QRIb-ydQJEPmL59f5PZ-NGtY-FIeLYtCWP0PJnKfQMFu05VoB7HO8H0BeXQw-65pIU31bhWzlz2nYK0TnUcWQx9erSjYxj80iidh3fvo8hqJ4TAvMbvHA_zh6Lvx21KNfFeauZFPaD46GqpzwKJ7Z8aacgEtUjKpu4brJQjb-zCgwP05lv_vYGimRK1CqSbWGPOJf3PJ0baep7RQc3X2kNz0aMgUmbqCoEiYCInjCRxtg7hTbeSRy2GhsX-ZbDuBkjjlws-2vTDxaVILf9HITw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هانی رامبد تو دایرکت هادی چوپان:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84094" target="_blank">📅 15:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84093">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=NVmQPcfUu2II0hLvOwo8ncvi8aw7fkaY4F-REyaLL0dLHOp-4X47PpO-fYssrD5674bWZ0OF5H-h8EGUlroTW_bH8IZVdXpk4yKcOkQZH7u0XWmujg0AgIaODjlflR0dPzEUcJK8UW8yr6_cpSD8-xgWEF7Zbzf68zsDMCntb3ziLV222c4aBydDIXdnHg8vTO5dtTnB-rOonsll2qts0YEd9LwgzAkDVszD6p1OWauJaUzSE-0W66hj94ZKqwiRKrsCJEewzox2QQA_tOh9kRriSB4wEiNOVbHug740Rqw_AUywbLTtdR3k0s3HqxsyvxKfK4X0H5nteDuRmwMEHH8xlVRf_Ax1HnguImnojEh8X5Aqrvl2PockLbQm6J84O1b3G17loCrP65RI3kgerzIcZyI0PAzmF6hQHeM12sPqykkohigcZUt6m3U98zzCBSTDRqy52vFmY_iZL5kjj4jL5LSTE2JsybPfkhqr_YYvk7brQOA6qbovIzRy_T1a24V5jQirEyVXxOZVsAyama5TYWYiost--4hALiOTCb87DV0hpar4Za6DbebM0p_Ct2dunopKm8KDQUFKHRRGL5a4znsqEt-Uh9tOuSEwh9XkEQ5GeNXK0OZKTbuH6hJ7p2OprsAZ8U2ZtR34rGNobvWWwTq9YJ5gujbCL1S5l5E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b331c3393f.mp4?token=NVmQPcfUu2II0hLvOwo8ncvi8aw7fkaY4F-REyaLL0dLHOp-4X47PpO-fYssrD5674bWZ0OF5H-h8EGUlroTW_bH8IZVdXpk4yKcOkQZH7u0XWmujg0AgIaODjlflR0dPzEUcJK8UW8yr6_cpSD8-xgWEF7Zbzf68zsDMCntb3ziLV222c4aBydDIXdnHg8vTO5dtTnB-rOonsll2qts0YEd9LwgzAkDVszD6p1OWauJaUzSE-0W66hj94ZKqwiRKrsCJEewzox2QQA_tOh9kRriSB4wEiNOVbHug740Rqw_AUywbLTtdR3k0s3HqxsyvxKfK4X0H5nteDuRmwMEHH8xlVRf_Ax1HnguImnojEh8X5Aqrvl2PockLbQm6J84O1b3G17loCrP65RI3kgerzIcZyI0PAzmF6hQHeM12sPqykkohigcZUt6m3U98zzCBSTDRqy52vFmY_iZL5kjj4jL5LSTE2JsybPfkhqr_YYvk7brQOA6qbovIzRy_T1a24V5jQirEyVXxOZVsAyama5TYWYiost--4hALiOTCb87DV0hpar4Za6DbebM0p_Ct2dunopKm8KDQUFKHRRGL5a4znsqEt-Uh9tOuSEwh9XkEQ5GeNXK0OZKTbuH6hJ7p2OprsAZ8U2ZtR34rGNobvWWwTq9YJ5gujbCL1S5l5E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی یه ویدیو از پابندش گذاشته با کپشن"یادگار دی ماه"
و حالا کامنت های مردم:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84093" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84092">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84092" target="_blank">📅 14:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84091">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDRRFowk9Sl0Uq3zCEpI1Iur9Ue296Vz0iOTVFRiAJzwMmqNjch8av83wkW5TKWbCmj0vj3d6uIGElQrfKUgeJKbzYwRa4ymFVjAU-odl1SGy3jgSOwDD8DOBIeYXF7--i9tX7E14xUSyf5eS_KStj0l_TcvQa7vSREWvqrJzimLsy4s-oYAj_sHPuGZ3ZFttZZ51Tf-pVGuUJ1O1SSY4tqhISGvMoodRjY4Dk5-1_GsAzJczC_nroN6J7F_aWx0BzMrVGyBCTC8CJRuAGoC45X01Hr6ti6Jx7poxp9AA04x35vGkNczd24jNM4FmiPEbwJARv5d_gPzxQIT4ba-Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بانک کارگشایی یک تن طلای مردم که دست میلی گلد بود رو بالا کشیده و میگه دست ما طلایی نیست، حالا میلی اومده به محسن رضایی نامه زده که پیگیری کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84091" target="_blank">📅 14:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84090">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9NLtiWZBUqJZul_sFMe4sU0aaKBZlXDI2s5jAYBLx4eESaR4W5mr7dCm1T0ejQoH9d_WSVBlTdvSDScORXmAVT8HNHu4spgIBnr743omTURTRvVh5O-iwYgOqc2v3zY1bukfYRn1swJaCANYbN05vrHwbDApLiEvB4UkdU4KhFoGG9BEb_B9ZSrM_3OI9Gbz3y3vrA3DQH9D9sLh-9osKWLP2UQDIAxqIHm_5z27hMz2Sc9zqef2uOZfnBMyKMzpKbNedP90tjRncIy6U1OIlsmXTyx8HzKtXu0PV1lU5J3JyhXJW3GqJqihumGtaH6ygZi6UXD9Cf5ZctZajRETQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد همین نیما و دارو دستش تا یه چیزی به آرتیستاش میگیم میان میگن نه هیت ندید و فلان، وقتی ما میگیم هیته وقتی اینا میگن انتقاد سازندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84090" target="_blank">📅 14:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84089">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=bsmpAtM4iT6yIqXQ9jYEo3gAtGtgqpJJbuZLVrkTI9tNTfU5u5DmRcHtSGIx2yWaiakBbrUXLNdCrcBq2XF2yrfoGa1f48lp_Op71LCSCdWcOjMuDErttrGk20CWMcuv-tox48Xz0AGAh1Dl8_wwtY4LpasL5ANkRl0XK1dSAUPnqIyIrsgrxo7yYhrBrKE7JxsThdjBHr2uL4u8Qp2uMk0mruBzAyUbmSMAkMqrkkAWOK3THm_TBOJDC_i_vi1lClz53iTSkKjZmxRZZ-rVStjVICnZECiIsOCsouF9sHd4nKpkA2rUUCf9tivWFiCRjNe5O9abcEetFk19SQguVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e6331f6cc.mp4?token=bsmpAtM4iT6yIqXQ9jYEo3gAtGtgqpJJbuZLVrkTI9tNTfU5u5DmRcHtSGIx2yWaiakBbrUXLNdCrcBq2XF2yrfoGa1f48lp_Op71LCSCdWcOjMuDErttrGk20CWMcuv-tox48Xz0AGAh1Dl8_wwtY4LpasL5ANkRl0XK1dSAUPnqIyIrsgrxo7yYhrBrKE7JxsThdjBHr2uL4u8Qp2uMk0mruBzAyUbmSMAkMqrkkAWOK3THm_TBOJDC_i_vi1lClz53iTSkKjZmxRZZ-rVStjVICnZECiIsOCsouF9sHd4nKpkA2rUUCf9tivWFiCRjNe5O9abcEetFk19SQguVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسئولین لیگ برتر به تاجرنیا گفتن خب قهرمانی فصل پیشو میدیم به استقلال ولی به کسی نگو تا موقع اهدای جام که نتونن اعتراض کنن
تاجرنیا چیکار کرده باشه خوبه؟ اومده مصاحبه کرده گفته به من قول دادن جامو بدن به استقلال، حالا کل تیما دارن اعتراض میکنن و احتمالا دوباره کنسل میشه و جامو نمیدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84089" target="_blank">📅 13:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84086">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4ew9L5Sm_2Q-XfTdbdmk6Btwy00Roo_YrYNeNArYkztuv6PcUkL3uHTY-CQM-Hg7vpx1BtpI1TIbSQznSDh2tZwb4WDDnMb49sAs9Ms4qCZtzmERDAiF5kP9HfF9fO6TG6mTf3624O-wcl1o04WUayzRT6TrA-mVKcPLkedvZFGfA_HpsFiN9CXTO6meC9NjqdJV3mHwiKhbUJTLh4q_kuc9t72r6j9Jv0m4KdeKxrm_ox2g869Tufp_s0YkTa98wKWKCPTsQ5lHGJqd00_i04bGuytdUoxYyvNu2w0UDaJCuG24kUNxVRitTTbK8IVPr77qsgEqMrvECC6kd5Alg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسطوره حمید رسایی برای اینکه سال ۱۴۰۲ تو کانال تلگرامش به محمدباقرشاه گفته بود دیکتاتور، الان داره می‌ره زندان.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84086" target="_blank">📅 12:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84085">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6182180c47.mp4?token=GEl-I6N5Az4yMslfGtK2mgeVEBNI-IYO8M-iDamqBzIH51g7XAHgvJi0IGc1M8mLYny_WBVXzH7rMRIAiui4R-aHbgMvKWzCdngZbIMyqJxtiXkUjmL6aaX0txc2i69wwKSUD7ib3fRMDf-NGrD4cwNG4WTMWfw133svYwTl70cFix3oTS8r3w2w0Ios2buDiQY6aWCPc8XfWNxAi0wFXYLu9kgtfIYzqPgGgMRFErhYb-S-uhoR9kFROj8RbjPHnSHkls4-zDze1qfahiNDMIqlyBaMqgIQPu1oqegm2oArHSpWs9F_FKmEVMM3OsshV6jNakRCpttMMvijP0zRXaFe1BoEOsjnOnxgQNgsoRGRDqQ7MZsrwsauNh6CWpuLxeZA8yB72YGXUYRiwNMOwqJ9o4R0QLnYKxazJLc6ORJmO5hYG7sU7iLZd2bzYH7tB-bKH33_vA-EQh5O6nVMZULec3pOWYIrTY0WJ494KERxFD-JCOnROhncpYRzy6l7h1qribXUjzMdnQLksPSheA9ofRwadH8y8CDmtyCE5JL3S0y_zfhcihIDIMtV4hXhcQbHwqTU6gx-fX_EF--QUVmVOto91DVFEPynWaA1-TSpzgAySXr1z_0ZKG2lvH3aooBTNeiXXTLuDJyOW7SUV9U2XGEXvD0TkpEj04bowyc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6182180c47.mp4?token=GEl-I6N5Az4yMslfGtK2mgeVEBNI-IYO8M-iDamqBzIH51g7XAHgvJi0IGc1M8mLYny_WBVXzH7rMRIAiui4R-aHbgMvKWzCdngZbIMyqJxtiXkUjmL6aaX0txc2i69wwKSUD7ib3fRMDf-NGrD4cwNG4WTMWfw133svYwTl70cFix3oTS8r3w2w0Ios2buDiQY6aWCPc8XfWNxAi0wFXYLu9kgtfIYzqPgGgMRFErhYb-S-uhoR9kFROj8RbjPHnSHkls4-zDze1qfahiNDMIqlyBaMqgIQPu1oqegm2oArHSpWs9F_FKmEVMM3OsshV6jNakRCpttMMvijP0zRXaFe1BoEOsjnOnxgQNgsoRGRDqQ7MZsrwsauNh6CWpuLxeZA8yB72YGXUYRiwNMOwqJ9o4R0QLnYKxazJLc6ORJmO5hYG7sU7iLZd2bzYH7tB-bKH33_vA-EQh5O6nVMZULec3pOWYIrTY0WJ494KERxFD-JCOnROhncpYRzy6l7h1qribXUjzMdnQLksPSheA9ofRwadH8y8CDmtyCE5JL3S0y_zfhcihIDIMtV4hXhcQbHwqTU6gx-fX_EF--QUVmVOto91DVFEPynWaA1-TSpzgAySXr1z_0ZKG2lvH3aooBTNeiXXTLuDJyOW7SUV9U2XGEXvD0TkpEj04bowyc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیک واکر با شکست سامسون داودا به مقام اول مستر المپیا رسید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84085" target="_blank">📅 10:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84084">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kfw_ct1EcZ3Hv1S5xhRH0bnSJ_HNgeZJDOwk5gRvEks6WYNn1Yh0OL8_7iHbQ3ffHH_mjynaR_3zWwUNXfNNK8CSypdXiMoan97V_BAsny3hCy8czPgf5-WPyyNt3GL0VM6U2e75wRwtR_ExS_F1KbjgGivH7NeMH_swj8LZBmwt8pY3v4Hbsq2Y568j0xqRtr8AgQtAPy9LthvOdMLvJCNAKGpTB7LghPcKh9t_mSfG5kBxqxjuwQN8Vhxxu5Y8VyGm_Q4sDPLC1-l_L1YU4sLLODjWXc7Knw-23_XFxHdkhmNvosczyrfEOTWIxKh016yaOycATqBqpxdI_tmt7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلخون بد جلوعه حاجی
ناخوناشو تتو کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84084" target="_blank">📅 09:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84083">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">گوگل ایران رو تحریم کرد و دیگه نمیتونید جی‌میل جدید بسازید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84083" target="_blank">📅 03:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84082">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">این باز مست کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84082" target="_blank">📅 01:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84081">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiAPvlzS5Am0vTVuROsBVVFjHC1fW8CraVJMS88Xk6xArb2RSb8gwqXw2snen-jZOF7GxI5zx7CwW9PW3FsemfNDkn0Vu3sL89ndxMxYD3tDIOurDowXQaFlw8CsbKHXDpoWoXTflwAm22wdeEepNjZYaw8n2tVfWWyvQDD-xmQIyvVBzHoQex7CQGa0UNkwtrdjpFTeFNZrrXZf7VgVr1rXIPyqqzJcDcJh-1RVWWXSZ_T_w_0UpudEsPHg3kB6eowfgljb867Z03Gu7ZbnL7j3aNQru4qdA8SR8ubPActOOFtrLqJ9IkxNf_uuLer-c1rPYi1c2Z2z-D8W6gF3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا رسما هرچی تیم اسم و رسم دار تو دنیا بودو تو سه چهارماه گایید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84081" target="_blank">📅 00:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84080">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">تنگه هرمز بکن بکنه</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84080" target="_blank">📅 00:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84079">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KukFLuohOCBkDSJMtRQjkqen9p_Jllil70YQGjYPbZlZohiTbf-E7FtHs52lV_w2h-hjy0qhXu7K3u7Jl8CMhcQxWzx-ecB0g5YCqKjxgtEKgfGeBz-S5JqP_fSRu_AZiCN8iqZx_n15HbVHnvMZBXTlk1vJGvjJzcm_i4mRwYSpn9si6TbifQ6Wh1qR0FHrMBhLW6dc81fg6j6u2jeTZub-tgS-9onWXOz8AcxdGQltQl95xA_TnrtH-H_EfCXuNOOLK3W37uWhfnWRoHA5qdAItGMIbhaEV8NmT4THrIxqI9i3jPPShAlq9rb16o6QsNz42gGYkWiTqQSIch1bmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مترو مناطق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84079" target="_blank">📅 23:30 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84078">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">کوکوریا زنتو گاییدم</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/84078" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84077">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.  YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84077" target="_blank">📅 22:45 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84076">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بابا کیرم دهنتون بچه ده ساله هم بلده که همراه با یوتوب از ساندکلاد حداقل بده بالا، شما با ۳۰ سال سابقه بلد نیستید</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84076" target="_blank">📅 22:42 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84075">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tO2zDJzbfBgPNTdDFe32mQAuEChPYl9Qbm_k_hX-PkpI3ZGbnxuES6C7fdtNlqeiimAGSXJUN-B_CtDYhuPxkPjXlhnqefqAMAxeV3Q-0D_SrwubaGSuuc3tJ1-tPkiWsCy2VyrRnoxEM5YDcfUsSff-Lcm8hVj1Yzv5M8RsstaLjquUjq2mQ-3_lkoUuwrrNKmaxykidJH0LmZ2_bGs6YLut-ylqfHvChhUdhMEaNHpacRTZNtSUNTB1Cam_mnhix77lQWrXXqelz7AMx_0V4jPQlgJ-kb6SFCU7m1uMnGqF-IU3U7f3yBqq-l9ELwnQgiCcU3Yalo72M4K9jW_nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید پیشرو و تهی به نام "رفیق" منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84075" target="_blank">📅 22:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84074">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پزشکیان:
نتانیاهو زورش به غزه نرسید بعد میگه میخوام حکومت ایران رو عوض کنم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84074" target="_blank">📅 22:31 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84073">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=XXPGzNpRFa-MAD8TpYO1p8CmRqLAwZQEWkKi5r_-lyI5NKrfPwVCSkZRT0ClM83go41Ipge0QZDL2jk1ylmEwQTCybdaDX1iNSdYLT1hsbJ6cZnMwRIO0k4zSkuqOHwjXWgqzzepMvUfrt-Rdl58oAsSy8NDF1b_zFQS99Xoqsuq20lB-hRRcly1MrtseXDM32NmyFkKEDZB2RPo5dcaY9ziv-gDqZkFecJXkvnYtYTCZDVU4eIqrTURoT9tSE2fhcTg8hSsJI8MqpFulX_P8jmzeMub-Wf4LrXJ1kjeeVPr3jvuhkMyeFNFZVaD_S_7qW92UlcSSWMQF7jnLDuLYw" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/1a8faead30.mp4?token=XXPGzNpRFa-MAD8TpYO1p8CmRqLAwZQEWkKi5r_-lyI5NKrfPwVCSkZRT0ClM83go41Ipge0QZDL2jk1ylmEwQTCybdaDX1iNSdYLT1hsbJ6cZnMwRIO0k4zSkuqOHwjXWgqzzepMvUfrt-Rdl58oAsSy8NDF1b_zFQS99Xoqsuq20lB-hRRcly1MrtseXDM32NmyFkKEDZB2RPo5dcaY9ziv-gDqZkFecJXkvnYtYTCZDVU4eIqrTURoT9tSE2fhcTg8hSsJI8MqpFulX_P8jmzeMub-Wf4LrXJ1kjeeVPr3jvuhkMyeFNFZVaD_S_7qW92UlcSSWMQF7jnLDuLYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کرمانشاه یه مخزن سوخت خارجی F-16 Sufa اسرائیلو پیدا کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84073" target="_blank">📅 22:20 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
