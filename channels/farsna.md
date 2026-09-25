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
<img src="https://cdn4.telesco.pe/file/JnpM3YVN64uN6jPkbTswR9taA5G22TE8y8I3sAfvxEdY6j_c1uaoaU22rPRc1lOE2MZudya2H31X3V639shbgttLARl0clpa-YAHxYnqmSR3NSTKAH3ocM6WQgkZ2ViVd1mHZ1Kfxq0nGU_qumRrQ9shkixIMNjU_y-q2lqyKngGmyQ-rhsIPV_gTZexlhMmrodpd2ffcIpu9ZMN_ONxOfZxlQF7JLHVWUIlIakRDt6RI9wmx4fywRS9daTdvbDUvDKtcIaWDK4ipXqLFdJSDLe3gaqaOd7lnZ_Lw1aqqhpxL-MjQBMREYBHA5wKbrkZCdO2UtQUgP4Gs8wIbX80xA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.78M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 09:47:03</div>
<hr>

<div class="tg-post" id="msg-464296">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_WhAiyA2QsI3gu9Nr2I1lrVJURwcgca44NRj8QYobH8vIIqKHmON73Q2CS9KzSmt6fQcNqRnFFiTw80SaQh8QfLC2EKkFc2Fqy-x8jRmEmAFxMmoWl4ILHvfaYWSwwrqCgM0wKV454jOolvl8z-w5RMO3X76_7G9LAcc_zbVFhyNnGerIm6EwiIC2hyLN_rgZvp8VWTAAHcadRNms_7Y4qNPq7yoUBA4MQ4Q25eNNgmEs_kgLYm6JPY1BG-rcBuw2GB1qnhlWAU-fM0IgzKpcSsaWXVeVTvb9irhLP9saRo6NfAJ2h-oYHCgyrCwuuYNzxqWGILKeudGTWVNJ0WvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسکتبال ۳ نفرهٔ ایران به فینال نرسید
🔹
تیم ملی بسکتبال ۳ نفرهٔ مردان ایران در مرحلهٔ نیمه‌نهایی بازی‌های آسیایی ناگویا مقابل قطر با نتیجه ۱۴ بر ۱۱ شکست خورد و از صعود به دیدار فینال بازماند.
🔹
ایران در دیدار رده‌بندی به مصاف فیلیپین می‌رود.
@Farsna</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/farsna/464296" target="_blank">📅 09:36 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464295">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GnWOKq1MwPmGgdT4kl8H5o8cg0JKrl_fQODK21QZ_Rc6zk10tLLi2wEoZFrkZTARmmI29bbQr-pHhl2cfmU9tlubDg2suKay_sSkXrctrS1VBgBTFAZmUQf9cya8j7zxyXCrlStFbFkw6IVfbi3WO4Sgx1Wxm3ZVQuA7jMc8XpegIXVHUywhUtlIoXRCiNrSjmKnIRTlpWvWFTVOPVBBUovsZTQaOzoPFBlolmCh2H6urpyKafmhrhMYCUaYd6FBWl3qnnAIesD8mmrjXiQPlQwnYBuNrPQN6bccDgg6mHFFAh24AbKMC2h28pUEamUblHXMUjzLhDF3Z_m2_nCOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینهٔ سفر نفت سعودی ۱۰ برابر شد
🔹
هزینهٔ بیمه جنگ نفتکش‌های مرتبط با عربستان در دریای سرخ نسبت به چند هفتهٔ گذشته حدود ۳ برابر شده و به حدود ۳ درصد ارزش کشتی رسیده است؛ نرخ بیمه برای کشتی‌های عازم بنادر جنوبی عربستان نیز ممکن است تا ۷ درصد افزایش یابد.
🔹
با احتساب بیمه، کرایهٔ نفتکش و سوخت، هزینهٔ هر سفر حمل نفت عربستان دست‌کم ۱۰ برابر قبل شده و در برخی مسیرها افزایش بیشتری داشته است.
🔸
این درحالی است که بارگیری نفتکش‌ها در بندر ینبع همچنان از سر گرفته نشده و تهدید علیه کشتی‌های مرتبط با عربستان در نزدیکی باب‌المندب و حملات اخیر به زیرساخت‌های نفتی، ریسک استفاده از مسیر دریای سرخ را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1.65K · <a href="https://t.me/farsna/464295" target="_blank">📅 09:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464294">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EvBTOkSkwOuTACdBtzlT0eh9OSvCumbuIIZjAShfjNelN3OUkBlIa0N9pK61f6MMT_0KbTM961jBMcA-aaYXNcMRyQ_n4dQQaW45RGPkxTSRkBQRr8275PGtJFDvfpXmdhcfjNzzW8Sq7v43nLpZRut23k82JuXZTKoCi36vEn33tsB8f87mVrUsGqIqxeO_YDnUt7c1y79J_tsMDty45yatPCO9DrP2Bm0nrKXaw-EC9rXWapDCPVyU7tG2Q8TMbSkycfmEco1S0hpzF5Q3nRrqzJ3vt-NXbi4YlyHDhXteXOn5Acd4LUfmIJamEoj1UICkECg0ofvaj7HwAqoEFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشاد عالمیان به مرحلهٔ یک‌هشتم نهایی تنیس روی میز مسابقات آسیایی ناگویا رسید.
@Farsna</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/farsna/464294" target="_blank">📅 09:28 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464293">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac963e738.mp4?token=mCX7aDID9JJIRjBO9um1bd9-Ms30wR-iJukw7Derw0hx9XK694tiJqpD1kPucfC-VSDaaimZUANTRZRkEC0RvHYqf-Ak3jjDPUoFqzK5VNgEftF5tw0xu2GSWiDK0FHRQzImmRkDj8pPIEQUvWuh9H1yOGIRuBrea-E-p7svbaTN772tSDYS6Yfv4j7s8qfasOaMBudhDKCmkXK-5-lt3ewoqAl-atXJseGqynhEPruyCyVQtgO7_PYnfD0JLk6Ypbubi5pOjJpsD0wjKt_sD3YD6BtJjH4gTg-SmrBG8_QbBjEDzWm8rcmPx_u40Om1EzkiuolRrFc9pqWIuzfqGZv7KHOl8SfNTWSu-5hQe1KVH-GyrZQDM3I9OY8JOxw4VEpGgMW8fPGgxAoeou4O5wjz1sYpncm3ZZqRR919kCtDb0khCkWR13WUBfxPaPn0ZCeR-VYWKZ9iGfOypdtd44l9TdM6dwyv9K8TweXwHTWj25_BVk7y7bIkCNzqWvsYkiSYCXyVGjQMuai1fCghdQCdVzTB1pEf3WURK1sF59r0n0BBW-B_3VTY5ss-9Z9-ACpvrQ9P2ke-wj7Bhxv4CLXUrKw3kKD6PMDqTrINDhbSt4CSrvVAx8Ixa4SscNWNpaK9Ui8MplvTcmo76r8kY6c9YWkfMXhTQnJ4KOLjg-M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac963e738.mp4?token=mCX7aDID9JJIRjBO9um1bd9-Ms30wR-iJukw7Derw0hx9XK694tiJqpD1kPucfC-VSDaaimZUANTRZRkEC0RvHYqf-Ak3jjDPUoFqzK5VNgEftF5tw0xu2GSWiDK0FHRQzImmRkDj8pPIEQUvWuh9H1yOGIRuBrea-E-p7svbaTN772tSDYS6Yfv4j7s8qfasOaMBudhDKCmkXK-5-lt3ewoqAl-atXJseGqynhEPruyCyVQtgO7_PYnfD0JLk6Ypbubi5pOjJpsD0wjKt_sD3YD6BtJjH4gTg-SmrBG8_QbBjEDzWm8rcmPx_u40Om1EzkiuolRrFc9pqWIuzfqGZv7KHOl8SfNTWSu-5hQe1KVH-GyrZQDM3I9OY8JOxw4VEpGgMW8fPGgxAoeou4O5wjz1sYpncm3ZZqRR919kCtDb0khCkWR13WUBfxPaPn0ZCeR-VYWKZ9iGfOypdtd44l9TdM6dwyv9K8TweXwHTWj25_BVk7y7bIkCNzqWvsYkiSYCXyVGjQMuai1fCghdQCdVzTB1pEf3WURK1sF59r0n0BBW-B_3VTY5ss-9Z9-ACpvrQ9P2ke-wj7Bhxv4CLXUrKw3kKD6PMDqTrINDhbSt4CSrvVAx8Ixa4SscNWNpaK9Ui8MplvTcmo76r8kY6c9YWkfMXhTQnJ4KOLjg-M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محمدی: برخی کالا‌های ایرانی با تغییر نشان آن به برند خارجی ۳ برابر قیمت اصلی فروخته می‌شوند
🔹
عضو هیئت‌مدیرهٔ انجمن صنایع لوازم خانگی: قدرت برند یک واقعیت انکارناپذیر است و نشان‌های تجاری داخلی توان رقابت برندی با غول‌های جهانی لوازم خانگی که پیش‌تر در ایران حضور داشتند و اکنون رفته‌اند ندارند.
🔹
از این رو بخشی از خریداران تمایل دارند حتی بدون گارانتی و به شکل قاچاق، برند خارجی خریداری کنند.
🔹
به‌همین‌دلیل محصول ایرانی به مناطق مرزی برده می‌شود، در آنجا کارتن و نشان آن تعویض شده و سپس با برچسب برندهای نامدار جهانی به متقاضیانی که حاضرند ۲ تا ۳ برابر قیمت کالای داخلی برای نشان خارجی پول بپردازند، فروخته می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/farsna/464293" target="_blank">📅 09:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464292">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4WlJ9vOhTRvO3kmS-1A2d6VPPfKbG_56EjxoCqHib8KBUG6z3EY4ur6e9WCi-bJ89lwnCInfw8stcBEXw8bGAP9YLn8qtOwmJiKAe-cGkCpCfJHKlQxsQqXZtAeL-ctMRysiqGUChDfncXE3K73KG2-DUaWnFMSvQ-wLRfOIcvJfPn4KX_Zp-iMiHg0-1t_kzjMjDE-hwEl7Yjauq_xrbRHNwq7Nk7YLW2KPKe4doL2P2A4jfGgyHFmkqr_BX9ZLFfkyyGoORk0m1xm325ZA3ustVsQa-PTCxMJwBmBRfN4HNbu0SBmUCcofUBnak0D1I-iDzjozcD8GJFWo_pr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محیطی‌زاده دیسکالیفه شد
🔹
فاطمه محیطی‌زاده نمایندهٔ کشورمان در مادهٔ هفتگانهٔ دوومیدانی مسابقات آسیایی ناگویا در بخش پرتاب نیزه، به‌دلیل استاندارد‌نبودن کفش‌هایش دیسکالیفه شد و از جدول مسابقات کنار رفت.
@Farsna</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/farsna/464292" target="_blank">📅 09:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464291">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v8hPfYxxUHeG5oLRV47JS5fuHgI6aC76e4BGPgdFOGwMI8L6ZRLMfih9sTFn0DElnM2VrWYU2W6vlJHTSMuUBzESA9HOnD5lGfT14lOBRD9WFB1uIllqCN-JpIFonCjJFP3_e324n_i9gx6PdDK29Nyu8PxxnEMK6wp2aG_1qV9tSnE_X1ZnL4rgeJ6HqoXTXe8TcFSR2gkRFcEWOATp_dPNWb4GSEMET32ZVroLjAi75LlJbB6eiayQCQ1N5jZCNbcbCqRGuHMqX-927D-7sibBI-qOUgGUNFoMB4KMgmdeUOoQR-VE3hKBMs5fbYx4NPIAFcgezOkb7yFbEbcDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جملهٔ خنده‌دار نتانیاهو: متهم‌کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است!  @Farsna</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/farsna/464291" target="_blank">📅 08:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464290">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6b73b98f4.mp4?token=PKXHxhqTOA1xPZBt7MHqc3zwFVrzs6RGFm6Qz_Oxq6yTmeVv-0CYKAfmle1TG8hUYUNkIED8CgTOrj1b_gWV3acn3qUUHrPK1wg92jRymxyD8AydaWcgItlBZeF0mhMaCWhL5gAl2ntFBeB3NR9LP468E2YnDke8P1NQJio4zQbJr0-WOuKFUxplw7SJsz7Ea2mpE-DIYQtDfa2_nsMfD7ga6niAkiV1MOjKPzJBWw1755rpHuhxFgjpaD92HAMup6V_2NsaGk7cI4c2wt6csSKWxc2Mc8JyPZWLdu7bN9vCq_t2AprYhoDW4Ss9sitTxiT_JzrRqXG8NWHZA3qCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6b73b98f4.mp4?token=PKXHxhqTOA1xPZBt7MHqc3zwFVrzs6RGFm6Qz_Oxq6yTmeVv-0CYKAfmle1TG8hUYUNkIED8CgTOrj1b_gWV3acn3qUUHrPK1wg92jRymxyD8AydaWcgItlBZeF0mhMaCWhL5gAl2ntFBeB3NR9LP468E2YnDke8P1NQJio4zQbJr0-WOuKFUxplw7SJsz7Ea2mpE-DIYQtDfa2_nsMfD7ga6niAkiV1MOjKPzJBWw1755rpHuhxFgjpaD92HAMup6V_2NsaGk7cI4c2wt6csSKWxc2Mc8JyPZWLdu7bN9vCq_t2AprYhoDW4Ss9sitTxiT_JzrRqXG8NWHZA3qCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایلوخانی مغلوب پینگ‌پنگ‌باز ژاپنی شد
🔹
در مرحلهٔ انفرادی مسابقات پینگ‌پنگ زنان آسیا ستایش ایلوخانی نتیجه را به هینا هایاتا از ژاپن واگذار کرد و از رسیدن به مرحلهٔ یک‌هشتم‌نهایی بازماند.
@Farsna</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/farsna/464290" target="_blank">📅 08:18 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464289">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e5b48ca2.mp4?token=hV71cZtgxFtzRrxoHKXrX62yon0im2vKmQN33wyYq_7KGAIxBv3ST4DM7Hxa-UMk6mRSrpaf1GvQveSuv_8Ka1Jc9x_UGoq6ZGmhHWVsxtpWyHR9g8HFqQjYBHjpWC5BZcEl4v1SE-q8bj-MFv2CoiFDarpG-dvWu8Jq58P_O2igkGpPdx2bcUdwnbldQiZ3D6t_kLvGBqqwNLstYdZ4Q3hdrBR_CdaKQ5DgSyEpwt-itIQiKliWQ2r8MO-HDYk8I9RlABgRYM_deTemellpRNCqNhN6TREl87WHJowZ_xLqt6Ihaedoj6ALPuG-fJDj8ZN97Bb-5Naq4nKWsUi-vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e5b48ca2.mp4?token=hV71cZtgxFtzRrxoHKXrX62yon0im2vKmQN33wyYq_7KGAIxBv3ST4DM7Hxa-UMk6mRSrpaf1GvQveSuv_8Ka1Jc9x_UGoq6ZGmhHWVsxtpWyHR9g8HFqQjYBHjpWC5BZcEl4v1SE-q8bj-MFv2CoiFDarpG-dvWu8Jq58P_O2igkGpPdx2bcUdwnbldQiZ3D6t_kLvGBqqwNLstYdZ4Q3hdrBR_CdaKQ5DgSyEpwt-itIQiKliWQ2r8MO-HDYk8I9RlABgRYM_deTemellpRNCqNhN6TREl87WHJowZ_xLqt6Ihaedoj6ALPuG-fJDj8ZN97Bb-5Naq4nKWsUi-vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
آمپول‌های لاغری ممکن است به چشم آسیب بزنند
@Farsna</div>
<div class="tg-footer">👁️ 5.94K · <a href="https://t.me/farsna/464289" target="_blank">📅 08:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464288">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/828d529c11.mp4?token=jXm-nTYLHc4JLt-51e9DWIZ3QJK9kQK_h9-YevjGSFS9HOEn_TJ8Ie2kF-CcIP6a-dWELN0dvrTCJf66A3oLZN6bnk7Bbq_3wp2wMRmiNNoykJv_d99uzbA9k3SjkBfj7gS2DrIzGU841hm97kdoAJSL39HKhlgqD1G9P3paTMZnf--_K1Po82yPRjBrz7ChqY-QvAog0c5RqGdjQSQjyPlidBZYWNAo6tZD_YP0AKHJnuVXesJUilxxGHS72Ax3kr-5bY5h145CFptrpyYnqJHzbz7RNenxJEuzEqL7K8Vx-H2GlyJbECo5hWf9Vap9RTu4_9UMcmFMA6TAVLDE3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/828d529c11.mp4?token=jXm-nTYLHc4JLt-51e9DWIZ3QJK9kQK_h9-YevjGSFS9HOEn_TJ8Ie2kF-CcIP6a-dWELN0dvrTCJf66A3oLZN6bnk7Bbq_3wp2wMRmiNNoykJv_d99uzbA9k3SjkBfj7gS2DrIzGU841hm97kdoAJSL39HKhlgqD1G9P3paTMZnf--_K1Po82yPRjBrz7ChqY-QvAog0c5RqGdjQSQjyPlidBZYWNAo6tZD_YP0AKHJnuVXesJUilxxGHS72Ax3kr-5bY5h145CFptrpyYnqJHzbz7RNenxJEuzEqL7K8Vx-H2GlyJbECo5hWf9Vap9RTu4_9UMcmFMA6TAVLDE3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز برای تیم تیراندازی ایران
🔹
در ادامۀ رقابت‌های تیراندازی بازی‌های آسیایی ناگویا ۲۰۲۶، تیم میکس ایران در مادۀ تپانچۀ ۱۰ متر با ترکیب وحید گلخندان و هانیه رستمیان به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/farsna/464288" target="_blank">📅 07:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464285">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PngnEIJJItAodKzgkxT3RMfGIyuMdhQzLpkqPJhrgqvYEQqnQXIcgj2YAR_Qm_tsw6I-I6qNgTiv-vQ7QCaulWtT4DK7xHgs1hXA_EeBnQqsi68P1GXHd7ajPzCsN-6oeX7kzD-oj-BdLxKAAZId9mVLxRK2FO1_4mEYsbEx5Vm6BYOF_CWrvnRgQWQwgecMXFFQHoQxdxX95l_MSnEzJfq_cvGvG2agGzFMm5SPvp9dsUNzCS5KDRmG55KUUIpt3fanSeZrvMKyaw8CHyqj-knDwBqy_IB2CPZ5uHl2jPLUtH69lXeTs65sHMMH0WsI6GOEEc1QKh9StBeZMP93YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qDlduPLE_vmvLUc0l3xNJ0x_lmcR6dGbcdfGA2mB_iC4Zy5ZYekzdAYVE-2LPaOPe0NcHFZFxNgZf1plSD5As0Ac6Iyy1d2u8PM31kRoxZsgF43gGhXnJX-_ae-aPE3gt3dz3d6Fx-WLzZLO2tYuC7l4SuDWeFJuWW-8OrLeqgQc9GjVs0hQVKhgEqRhywIY3An6PEg1FMOq4Ygrc7myGR_xK2IATitkz1oY2vsgp9VIB1i56WnOD3AzfXTOuV-_KJaeefaOgIRqdvLS_alMn9Iecoj33mSS9ePU332WNkNPgtRKCsyTyWtOXZZCDOyjw_QwMtNn2nhADyR3urX5Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCF3au7eYgp-HLpmkIw-Att2THz0WzpJX2WOy99AyizVCloYP7LDUU0N8aUE-ii7-yLXyZzOEEJ0x2HgykxjVZ5uyU2ziZJu4RFbg0ZmbZnqhHu40dmJH4ePFEn6avAIN4YSTIvNCX1gXvSSo97UwuGpWi2VLaKK2AP4ZYa7hmEGJIgAaP7UVWUeVIuXkQ51MytjYvzyZOv16dmo-sYpTUViQMq8ll5BgdlLh_NiivwzShDebOaX4CfGYK5gYuXfTcleLqPo0KRYkamZw1wRwyoEifh64rkE9L2rsdA4Ty9W7AsJiEXXBXLHl5UFegeCC1Om3uF_6IHsskrZxFBd8Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار عراقچی با وزرای خارجۀ پرتغال، قبرس و برونئی، در حاشیۀ نشست مجمع عمومی سازمان ملل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/farsna/464285" target="_blank">📅 07:49 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464284">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q6OGjuYNGCDi6HIxZALhJfMSZm81WfyZ1_ukb4B6InqVCE9HkHGATM7qQnmuh81Ci-k8ZM469JjrioNpS66BldLjmtEQ2WomhXHoq_wiJ5_Uv9XN0BNMY4LNMi7OShf8XdQeOUxVAToE9LtCpya7fpmF8oFF6jHOfuctymBCj7ysXxLILniJdRcxl_Oc4SlWpw5eIYk-I1bhnA82hR6W56_niEPz3hkWaYFyLmquXT2L1xEkmgtZh1KRlYRUd9fDR5FoWnVEk6C07tTDfG05nWA8nD1b5Sdk9bgHROCG693GhzSAzCJQsyKq34eRkfYmaAoNUPBbJ8PI48Hu06zFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استعفای عبدی پس از فاجعه در ناگویا
🔹
حسین عبدی بعد از بازگشت تیم امید به ایران و در فرودگاه از سرمربیگری این تیم استعفا و اعلام کرد که دست فدراسیون فوتبال را برای انتخاب مربی باز می‌گذارد.
🔸
تیم ملی فوتبال امید در آخرین دیدار مرحلۀ گروهی با
شکست سنگین ۴ بر یک مقابل کرۀشمالی
از بازی‌های آسیایی ناگویا کنار رفت و حذف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/farsna/464284" target="_blank">📅 07:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464283">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RAjWRLd0-MlHK7oT8IrZSKW7snoiIJgxaSSAhCaUWy7isbHJqZ-5F62Nx09bSlOB6dvnrQbd8sqeFMSV4pJMIHmnPs1esSt5xZcrxQ4Y-QjABOFEZRxPvZ71MQkiSd7i8FFPrT5pXI4ekDDOcYBZP8NJ-FhokojP3WsEaAH3U_-F6g23mdOkRoIklBS32fDfYIHoKjMBT69fW4vd-Fe8mUnj-GJ8wFZZ1yX0zFG2HHQpWfAzhAuU6zuWtm0N0REr8TsbTFPWl2cS82SPOanJAgCuSGdG-WbpSuBX-Eksedia5JJhcmVchyUPfHwX4bfmUZZRxLHuZVbv0rgfmt1Ngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو: قطعنامۀ ضدایرانی شورای حکام آژانس شرم‌آور است
🔹
میخائیل اولیانوف، نمایندۀ دائم روسیه در سازمان‌های بین‌المللی در وین، در یک نشست خبری از اقدامات ضدایرانی شورای حکام آژانس انرژی اتمی انتقاد کرد.
🔹
او گفت «شورای حکام در ژوئن به ابتکار کشورهای غربی یک قطعنامۀ ضدایرانی تصویب کرد؛ اما کمتر از چهار ماه بعد، علی‌رغم وجود قاعدۀ «ممنوعیت طرح مجدد یک موضوع در بازۀ زمانی مشخص، و پس از گرفتن یک تصمیم» قطعنامه‌ای جدید ارائه شد.
🔹
این صرفاً نشان‌دهندۀ شیوۀ غیرمسئولانه‌ای است که شرکای سابق ما که اکنون رقیب هستند، رفتار می‌کنند. آن‌ها بی‌کفایتی کامل از خود نشان می‌دهند، و شورای حکام هم همراه آن‌ها شده است. این قطعنامه کاملاً شرم‌آور است.»
🔸
شورای حکام آژانس بین‌المللی انرژی اتمی اخیراً با تصویب قطعنامه‌ای ضد ایرانی، پروندۀ ایران را به شورای امنیت سازمان ملل ارجاع داد.
🔸
پیش‌تر وزارت خارجۀ ایران هشدار داده بود که استفادۀ ابزاری از آژانس بین‌المللی انرژی اتمی برای بسترسازی فشار سیاسی و توجیه تجاوز نظامی علیه ایران، اعتبار آن به‌عنوان مرجعی بی‌طرف و مستقل را بر باد می‌دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/464283" target="_blank">📅 07:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464282">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">مدال برنز برای تیم تیراندازی ایران
🔹
در ادامۀ رقابت‌های تیراندازی بازی‌های آسیایی ناگویا ۲۰۲۶، تیم میکس ایران در مادۀ تپانچۀ ۱۰ متر با ترکیب وحید گلخندان و هانیه رستمیان به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/farsna/464282" target="_blank">📅 07:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464281">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">مدال برنز برای تیم تیراندازی ایران
🔹
در ادامۀ رقابت‌های تیراندازی بازی‌های آسیایی ناگویا ۲۰۲۶، تیم میکس ایران در مادۀ تپانچۀ ۱۰ متر با ترکیب وحید گلخندان و هانیه رستمیان به مدال برنز دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/farsna/464281" target="_blank">📅 07:08 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464280">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">مدال برنز برای قایقرانان ایران
🔹
تیم کایاک دو نفرۀ ۵۰۰ متر مردان ایران با ترکیب علی آقامیرزایی و پیمان قویدل در جریان بازی‌های آسیایی ناگویا ژاپن ۲۰۲۶، با ایستادن در جایگاه سوم به مدال برنز دست یافت.  @Farsna</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/farsna/464280" target="_blank">📅 07:07 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464279">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-text">بازی‌های آسیایی ناگویا
پیروزی برادران عالمیان برابر قزاقستان
🔹
در مرحلۀ یک شانزدهم‌نهایی رقابت‌های دوبل تنیس روی میز دوبل ایران به مصاف قزاقستان رفت.
🔹
در این دیدار تیم ایران متشکل از نوشاد و نیما عالمیان برابر تیم دوبل قزاقستان قرار گرفت و با نتیجه ۳ بر ۲ حریف خود را شکست داد و به مرحلۀ یک‌هشتم نهایی صعود کردند.
@Sportfars</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/farsna/464279" target="_blank">📅 07:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464278">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">‌ پزشکیان: هدیۀ ترامپ به مردم ایران موشک و ویرانی بود
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ترامپ مدام می‌گفت می‌خواهم برای مردم ایران هدیه‌ای بیاورم، اما هدیه‌ای که آنها برای ما آوردند، موشک‌های هدایت‌شونده، تسلیحات سنگین و ویرانی بود.
🔹
آنچه…</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/farsna/464278" target="_blank">📅 06:47 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464277">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پزشکیان: ما آغازگر جنگ نبودیم، اما اگر بخواهند به جنگ با ما ادامه دهند، پاسخی قاطع خواهیم داد
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ما به توافق رسیده بودیم و چارچوب تفاهم امضا و مورد توافق قرار گرفته بود. همچنان مایل به پیشبرد توافق با آمریکا…</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/464277" target="_blank">📅 06:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464276">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rd09bc-cuchPq8aLT8m4FhHKjigg-be0g8Ddxt7X8m0G_3t3-zXnaz4KofyKa_yMrCb8pJLpg3iynuBRC3e-zuTT2C_DZ_HWbQSVGpxj3P7XfSG6cKaF-MMpD_wTzNdkfLvEL9XyS7ednmvxdKJjJWn8ek8gSLBGhUxTUXaW8DC55n-fZ_PK9FtlOFGZWkSSRerv52xRIoScgfPNqn2t4yA3ZIFjHXRwi8SX-FVd3qck5zV9HW6zHDPI1tOhrnOlmi2dfEF-dLmyn7lNDzNtI9NIqFr7Pi3rOeqmQyRdp7vDfE3oCzlt9AzeTdZjfiKbOoI-lRwUcGwevaDLErppug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: ما آغازگر جنگ نبودیم، اما اگر بخواهند به جنگ با ما ادامه دهند، پاسخی قاطع خواهیم داد
🔹
رئیس‌جمهور در گفت‌وگو با شبکۀ آمریکایی فاکس‌نیوز: ما به توافق رسیده بودیم و چارچوب تفاهم امضا و مورد توافق قرار گرفته بود. همچنان مایل به پیشبرد توافق با آمریکا هستیم.
🔹
به تمام تعهدات خود در معاهدۀ NPT پایبند خواهیم بود و اورانیوم غنی‌شدۀ ۶۰ درصدی را در چارچوب حقوق بین‌الملل و معاهدۀ عدم اشاعۀ هسته‌ای کنار خواهیم گذاشت.
🔹
ما خواهان ادامۀ جنگ نیستیم. این آمریکاست که باید انتخاب کند آیا می‌خواهد به این وضعیت پایان دهد یا خیر.
🔹
ما تنگۀ هرمز را نبسته بودیم؛ تنگه باز بود. آن‌ها بدون هیچ توجیه یا چارچوب قانونی به ما حمله کردند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/464276" target="_blank">📅 06:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464275">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9061ad4a.mp4?token=neSdPobXmCL0NPxHOlRiNqql-XTsbSPHD3pqywNgBUJtKe7kxFePMh2KlGswbK_XR8o_i0khNFWOkBhk0qOySvES5GVcSaAqaKdP2Rm_D7DjlBXQeXpJgyC8NYDhF1YH8JazLXXqjRI-rZnOLjhlAkIuGlXriGuaF-w0kMzU1B3t65WWVGwxE1Xx43G4nyT_qXned3SSANnfFFmvfV3qxWlSWLQdbmK-n8pTkh8iNg7yJoAlesQJo2dBNvesM7Aks7R3R0sATGvC6MmoMcmVIrAGW8e7gPCeMIL6ovtqNf_QWvvhXp5W5MFp7oCWY9aEFdU__WNB_3hoCCot5u1Zfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9061ad4a.mp4?token=neSdPobXmCL0NPxHOlRiNqql-XTsbSPHD3pqywNgBUJtKe7kxFePMh2KlGswbK_XR8o_i0khNFWOkBhk0qOySvES5GVcSaAqaKdP2Rm_D7DjlBXQeXpJgyC8NYDhF1YH8JazLXXqjRI-rZnOLjhlAkIuGlXriGuaF-w0kMzU1B3t65WWVGwxE1Xx43G4nyT_qXned3SSANnfFFmvfV3qxWlSWLQdbmK-n8pTkh8iNg7yJoAlesQJo2dBNvesM7Aks7R3R0sATGvC6MmoMcmVIrAGW8e7gPCeMIL6ovtqNf_QWvvhXp5W5MFp7oCWY9aEFdU__WNB_3hoCCot5u1Zfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدال برنز برای قایقرانان ایران
🔹
تیم کایاک دو نفرۀ ۵۰۰ متر مردان ایران با ترکیب علی آقامیرزایی و پیمان قویدل در جریان بازی‌های آسیایی ناگویا ژاپن ۲۰۲۶، با ایستادن در جایگاه سوم به مدال برنز دست یافت.
@Farsna</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/464275" target="_blank">📅 06:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464274">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb8090fbb.mp4?token=uVuvP_RN7-C9HIG7vG_80D0wqBbDBioEVa0IRI2wmT66gPUcmS4-4BGpSMDH68n7P36fLY2COGoWudxrQG2pceT2P1thRCmQszgO6qAF_kNOYj0XuhjA1DR6xoiaixczkt7XdrrF4Wt7-4dQzUMy0VG8bKz2JXjdJqbZ-uhCFZ1FUDSWKwp3cgP62xEe7XpuB6AwU2GjrFIpkwUr5gz5RZS5ayPqgECBZ3mwnyeVgISbBnhQjYgH7ErrhzdmlPTY0HrvvnwoFesOHHp_LUqIYTUunbL7IgZDVk75dlhb2XI9og2XLxMrxOpCRvhMSIpJ8Xz8Blia-D01dpjZtgdajQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb8090fbb.mp4?token=uVuvP_RN7-C9HIG7vG_80D0wqBbDBioEVa0IRI2wmT66gPUcmS4-4BGpSMDH68n7P36fLY2COGoWudxrQG2pceT2P1thRCmQszgO6qAF_kNOYj0XuhjA1DR6xoiaixczkt7XdrrF4Wt7-4dQzUMy0VG8bKz2JXjdJqbZ-uhCFZ1FUDSWKwp3cgP62xEe7XpuB6AwU2GjrFIpkwUr5gz5RZS5ayPqgECBZ3mwnyeVgISbBnhQjYgH7ErrhzdmlPTY0HrvvnwoFesOHHp_LUqIYTUunbL7IgZDVk75dlhb2XI9og2XLxMrxOpCRvhMSIpJ8Xz8Blia-D01dpjZtgdajQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عراقچی در حاشیۀ نشست سازمان ملل با همتای پرتغالی خود دیدار و گفت‌وگو کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/farsna/464274" target="_blank">📅 06:06 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464273">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XaQAiukP_uzyNe_sDNKmNXa9o0ag0WxipUA6AR9zXXuecJ6Sj9And2nBHmaYcJQu47OaVZ8KGRyu39N-BeBPGL7amb9Frm6xRG_xNkanAIEdN-epXx53Qul_snHK1kEmN3XlJPYFBt1ZoZz2uNBk15oBgBtnFWp8WA2ewb1mlFZn0lBEdwDS0FxcDek0HX86TLX6AQrMN8g8Lm7Chz38lBQMlyFvGgMyUuIgsp-0KI4pNlMZxpy6Ddr6L2lNNPCwl5D5KLrmZQxWk6K9ZBOFwbI5lG48xfgjdAQaIOhGq3ID0CtH7kcWJ7mZuolywPjIS79h9-tMrorKS5mDaxybNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش‌های ایرانی دزدیده شده شناسایی شدند
🔹
۳ نفتکش حامل محمولۀ ۶۰۰ میلیون دلاری منتسب به ایران که به ادعای تانکر ترکرز توسط آمریکا ربوده شده‌اند، شناسایی شدند.
🔹
این سه نفتکش در اردیبهشت امسال واقع در دریای عمان ربوده شده‌اند.
🔹
بر این مبنا نفتکش مجستیک ایکس و تیفانی در سواحل شمالی برزیل هستند و نفتکش لنور به تازگی دماغۀ امید نیک را دور زده و به اقیانوس اطلس جنوبی رسیده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/farsna/464273" target="_blank">📅 05:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464271">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cvuiUCX4r2VZYbjrl38x7QgSNnCTZRHr-xYJxPTAbzcvfCvRUFlHNcwHdAk8cHTESBlDmP38K1onYs2-FKoXZgSd63a8MiPem5fTBqJI-eP5Ac55yxafFdOTWYkDaUOVHHHTmQUHIBvEjJRLLxpYtFVaS9eOM9XxeAlu9MWP82X6PPtNJSiEN7dgD5v8_JLSALAfm-jmn_XOxGaa-my3_aopi7UgLPvbaiVIHjIkgwS2gIaz9ZkjiBf6eYfTR06UnIg3fp8Mypma61gYdxRnbNSkyQIJxpw_3oeqN5cERW_rPXi1vg4QAfdV7D7fj94j7fVJtCld6MpSv3_TMOuRew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cjWiqnF1o2dvCkXI8UEafs-NdFXJZhwGLwBsRiwTVF3WsEE9oBhy2SYBdNEM3LD7JT5X4-hhhwCKSREogvubmO96wVlZWxEHo4c6ZcGB_ojVsTYWJdMaqS3Td8BvfXC6oIN6P2uAK-CFhtNW-RJ-kAzSI9TMOFjsAhB8pp46X7r97w4zE8TnkMo9IUahoD3PNWRCxfYtjAwtzfro9EL8CK5C4C3opXDA_ZZBROi3TnSYZ8ui4H_izctjflaXLLSDfc1KGPeFfRVLKkMp0NuQA6I52yQbbVS7isZmCyl7PODwzwmo90IE_C-afXdvP-godY78Hj3CMgK9a6Z6mUxnIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❤️‍🩹
هانیه خندان، داور بین‌المللی تیراندازی در مسابقات تیراندازی بازی‌های آسیایی ناگویا با پرچم ایران و نماد کودکان میناب حاضر شد
@Sportfars</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/farsna/464271" target="_blank">📅 05:11 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464270">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/764d1162f6.mp4?token=oz411r6-jz0nF8YWSrGi8CvMYmvbNz38IOEiQwKSwA9Auw9sC286fLK5IaPEMrlYe6EXlug1Hy4TW7h0qCAFvBdRSknvQOU6CiIfgcdQYGA2zJ4uIkCM70Kn66PR_cTGnJ14OcQtFTZoriq7abaUiS1nAlfXbzH7i8p__SdbfWdOHuQSlsPXUGoSMpkHgkN5iwgr_ccKoNna_8QqKdMpXP74wURk1n-35530Qph3THp9_5_Ey-G1fMAS51DlrYThy4LnScyH1JYKd9mGIrGlBJNd2EfcNqvsiIehHJjkcvyQZbnehZidhFtKNDmQPBFyKXdQ9L39W7uQDfgxOMYxgAIX2SaavoQUKKXR1HjwVeVy4ckti6b19LyevomW32WysVWmyUxz7j8afACX0J3VXZ5sJtimBp_Y514xKGs3O-VBGEyw_ln_ZzhKLCfWKtjylzY4F6ECMEyezKCSHfyCHQBlMFET6OCmcMZ8clU5ezSqiJVT7wA6XIKIYnPFDdtaxYwR0G2ks8ZxqQ1V8q_0TRL-tUChgYpK6MXHrv5zrVzD2Htz9pTSVqTHVmASkYDSRTCXHUF68gzjgYNSJ1GgiL_CMELpNWXNegEHj0ESMN5PckEBnMTgT23VrglbJiX-0fIWJR2ZXlLATE5KQf7CdhwlIPzghcMk-FZIQ2vgCXM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/764d1162f6.mp4?token=oz411r6-jz0nF8YWSrGi8CvMYmvbNz38IOEiQwKSwA9Auw9sC286fLK5IaPEMrlYe6EXlug1Hy4TW7h0qCAFvBdRSknvQOU6CiIfgcdQYGA2zJ4uIkCM70Kn66PR_cTGnJ14OcQtFTZoriq7abaUiS1nAlfXbzH7i8p__SdbfWdOHuQSlsPXUGoSMpkHgkN5iwgr_ccKoNna_8QqKdMpXP74wURk1n-35530Qph3THp9_5_Ey-G1fMAS51DlrYThy4LnScyH1JYKd9mGIrGlBJNd2EfcNqvsiIehHJjkcvyQZbnehZidhFtKNDmQPBFyKXdQ9L39W7uQDfgxOMYxgAIX2SaavoQUKKXR1HjwVeVy4ckti6b19LyevomW32WysVWmyUxz7j8afACX0J3VXZ5sJtimBp_Y514xKGs3O-VBGEyw_ln_ZzhKLCfWKtjylzY4F6ECMEyezKCSHfyCHQBlMFET6OCmcMZ8clU5ezSqiJVT7wA6XIKIYnPFDdtaxYwR0G2ks8ZxqQ1V8q_0TRL-tUChgYpK6MXHrv5zrVzD2Htz9pTSVqTHVmASkYDSRTCXHUF68gzjgYNSJ1GgiL_CMELpNWXNegEHj0ESMN5PckEBnMTgT23VrglbJiX-0fIWJR2ZXlLATE5KQf7CdhwlIPzghcMk-FZIQ2vgCXM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امتحان الهی یک نوع حل معما است
🎙
حجت‌الاسلام پناهیان
@FarsMaaref</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/464270" target="_blank">📅 04:52 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464269">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نشست اضطراری فرماندهان نظامی ترکیه، پاکستان و عربستان
🔹
عربستان سعودی، ترکیه و پاکستان در نشستی با حضور فرماندهان نظامی خود، دربارۀ حمایت از ریاض بر اساس توافق دفاعی مشترک میان سه کشور گفت‌وگو خواهند کرد.
🔹
بر اساس بیانیۀ وزارت خارجۀ عربستان سعودی، این کشورها قرار است پس از حملات انصارالله یمن از آنچه «حق ریاض برای دفاع از خود» خوانده شده حمایت می‌کنند. این نشست «فوری» توصیف شده است.
🔸
برگزاری این نشست در حالی انجام می‌شود که بسیاری از تحلیلگران در قدرت اجرایی پیمان نظامی میان سه کشور موسوم به «پیمان مکه» تردید دارند.
@Farsna</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/farsna/464269" target="_blank">📅 04:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464268">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دو پرواز دیگر از مقصدهای ایران حذف شدند
🔹
سخنگوی سازمان هواپیمایی کشوری اعلام کرد فرودگاه بغداد و مسقط پذیرش پروازهای ایرانی را از آغاز امروز انجام نمی‌دهند، و در حال رایزنی برای تغییر پروازهای بغداد به فرودگاه نجف هستیم.
🔹
اخوان تأکید کرد که لغو پروازها…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/464268" target="_blank">📅 04:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464265">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XshJ3CJR7SrCQg7rA97f6JyLnOhZSBJHK_AiTynGxIplyPIKroezBNs7P_xYqLFjKbTNmBVOt1u8HpjoQueR9UpQCjF9Wd74voQzR3pQQEiPlv_cwLUnDU6W-Dfw5nni86OldwReITxXEe_svDTTZsYBKFKlelRTHKAXo82qeWP4l97zVUD8dAa1h0O3e_oaTa8pZberIAYBCFwDuQ8HrGUo3NFA1IGyIHqCGA7n_PqbgQx1uyHXPTY4AZ_zIVAyXfcckh4LfHOfUe75jM-BckZvdro971R3wN-X7KBZz3hG8BUD0idhtJGexxZd3QbGb425DSVHuSMjPZ5xLf8pSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27db3e2672.mp4?token=vWZkCNIOnDaOieFS0oPsbcsGFulhGcaLTsdGdh57d1VBTnK-SkPThtYFjNK3Nsz5FQ0c2jlviSu1JU8Pq1GjkZpGEpfjsZqdGxmuRQYFMp7QboYDK7o9sho5JG10ptR9r5RkeC_f07kRuZDqX1X2Y-XcfU0cpfgekbbXZPQnsl1oSob68BdH4I7bQrWQiDaS0w-9pZduBRAv5ZyIGoBZlESroXw4R_VgQavzh8rdVqkJG35PYRi_omWaZh553yT4P20n9f_SiiWazkbDGVOHSGHEtcvrdyrIaoOySZgcOdoZmO_4OEMpBbr1S3odNmu3rTGZvrsx1Q1V4Bv9tr4EhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27db3e2672.mp4?token=vWZkCNIOnDaOieFS0oPsbcsGFulhGcaLTsdGdh57d1VBTnK-SkPThtYFjNK3Nsz5FQ0c2jlviSu1JU8Pq1GjkZpGEpfjsZqdGxmuRQYFMp7QboYDK7o9sho5JG10ptR9r5RkeC_f07kRuZDqX1X2Y-XcfU0cpfgekbbXZPQnsl1oSob68BdH4I7bQrWQiDaS0w-9pZduBRAv5ZyIGoBZlESroXw4R_VgQavzh8rdVqkJG35PYRi_omWaZh553yT4P20n9f_SiiWazkbDGVOHSGHEtcvrdyrIaoOySZgcOdoZmO_4OEMpBbr1S3odNmu3rTGZvrsx1Q1V4Bv9tr4EhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر رژیم صهیونیستی تلویحا از برنامه‌ریزی برای آشوب و اغتشاش در ایران خبر داد
🔹
نتانیاهو: «می‌خواهم یک خبر خوش به شما بدهم؛ اتفاقی باورنکردنی در ایران رخ خواهد داد. روزی که چندان هم دور نیست، حکومت ایران سقوط خواهد کرد.»  @Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/464265" target="_blank">📅 03:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464264">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🎥
عکس حاج قاسم جلوی چشم نتانیاهو در سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/464264" target="_blank">📅 03:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464263">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fTh58vV7Cg-ENca2npkGq97mxbq1Q1996uUgL4T224zQ9qpZPA-LKceOGnauCX9hkrSi7PPWKR_8iDBrM4ejEltZw-Lw0DOgnj78PnywEu5x5LoiWNaFpzO5TflRhYQHWRfqBW-p68UyenV-CRq49WHpvCoM8VdAq2wx94VwbQhqJG2-ccM9Dfqvqct8vr-ssLmYf4FIkllx2cGEKLpXWrU0hSHW7z52yQckiaNENU5ST7Z6ITi7WIihJ8WUv-KrrhLusygQCWv_wqt1YJTyqh0_OEs_Pf6BE24w5MCARbcqgao9eqgHKm6LXfwlpJDRrY_7vLJQZ5ROMmBdVe2M0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستگیری بیش از ۱۰۰ نفر از معترضان به نتانیاهو در نیویورک
🔹
پلیس نیویورک اعلام کرد بیش از ۱۰۰ نفر از جمله چند چهرۀ سرشناس و مقام منتخب محلی، روز پنجشنبه در جریان اعتراضات علیه بنیامین نتانیاهو، نخست‌وزیر اسرائیل در منهتن نیویورک، بازداشت شدند.
🔹
از جمله معترضان، سوزان ساراندون، بازیگر آمریکایی، بود که همراه با دیگر معترضان حامی فلسطین، بود.
🔹
بر اساس اعلام پلیس، «چی اوسّه»، عضو شورای شهر نیویورک، و «الکسا آویلس»، عضو دیگر این شورا، در میان ده‌ها نفری بودند که توسط پلیس نیویورک بازداشت شدند. پلیس نیویورک اعلام کرد تعداد بازداشت‌شدگان از ۱۰۰ نفر بیشتر بوده است.
🔹
«داریالیزا آویلا شوالیه»، نامزد انتخابات کنگره نیز در میان بازداشت‌شدگان بود.
🔹
معترضان در طول مسیر شعارهایی مانند «فلسطین را آزاد کنید» و «بی‌بی نتانیاهو، جنایتکار جنگی، را بازداشت کنید» سر می‌دادند.
@Farsna</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/464263" target="_blank">📅 03:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464260">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28eef03fb2.mp4?token=tr_HW0eFzV04tQ1Tojj5dFbzyiqnNYZNpj4lyvESHTbwnd-3CxdsgBWH2t7VhVtl9Ocj8MzWn15-jjbjIDDsDmjiNPIlUhNBVwQjtnb-fbhZtm3le2fSSz-H4Wc-vlSFaXcvXoZyeNeaBvus89_DfCT3UcUpvJ0u33mVjYZB4y3-XMMou65aB7X3C_m4WlJ8xgnV9xo6Bs-_qcNsetgaKT44LlxpEitHCh6A5ReNzGbLRoI9r0MHnQRey4KEGqqOTnTaN7IaDigIt6YdVuarxqHvzPN25Hs7D2BnfGW7rihYUv-gm-LKXyHh6PYzHtT7g0CWDy_VapyPRPRJZ4Sgfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28eef03fb2.mp4?token=tr_HW0eFzV04tQ1Tojj5dFbzyiqnNYZNpj4lyvESHTbwnd-3CxdsgBWH2t7VhVtl9Ocj8MzWn15-jjbjIDDsDmjiNPIlUhNBVwQjtnb-fbhZtm3le2fSSz-H4Wc-vlSFaXcvXoZyeNeaBvus89_DfCT3UcUpvJ0u33mVjYZB4y3-XMMou65aB7X3C_m4WlJ8xgnV9xo6Bs-_qcNsetgaKT44LlxpEitHCh6A5ReNzGbLRoI9r0MHnQRey4KEGqqOTnTaN7IaDigIt6YdVuarxqHvzPN25Hs7D2BnfGW7rihYUv-gm-LKXyHh6PYzHtT7g0CWDy_VapyPRPRJZ4Sgfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار عراقچی با همتای مصری، در حاشیۀ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464260" target="_blank">📅 01:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464259">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtqqh8Eg5EaeSTapwdym6jigimcTeQFxjw-CgjCvtM5XQJ5aspNX9jPX3WEiStRPkY6YRaP-ArzohPLqYSuDb0pwriAZlA9Ne1earJpu9EPmQ7SQx6PBDK39AJt4lf5EHKRfnAYW3heuhJL7cRNpUEop3X8y6CSdYJHZo9wyS62FD396CvXzw85SgECyys2tj0gOYd_fFjxz0vQGxf8UTAebs-w0L0vcprutJ-9EVJTiO6mS5NlWEHFeaCaKdxOpBc9nQwrJD24q0jjlQU_Yjy43jOkOhZOJThv9-VpS2NmCFaazCW5NPIPiByYLAGoe-6-jYDwJ5q-Jblk2osoWQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار فرانسه به ترامپ دربارۀ ممنوعیت صادرات گازوئیل
🔹
مکرون رئیس‌جمهور فرانسه به ترامپ هشدار داد که ممنوعیت احتمالی صادرات گازوئیل آمریکا موجب افزایش قیمت سوخت خواهد شد و این تصمیم را «بد» توصیف کرد.
🔹
مکرون گفت ما مستقیماً به نفت آمریکا وابسته نیستیم، اما چنین تصمیمی باعث افزایش قیمت‌ها خواهد شد.
🔹
به گفتۀ مکرون، فرانسه کشورهای عضو گروه هفت را دور هم جمع می‌کند تا بررسی کنند آیا لازم است بار دیگر از ذخایر راهبردی برای کاهش فشار بر بازار استفاده شود یا خیر.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/464259" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464258">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d59a9154d0.mp4?token=RgN1u21Ngqrs-i9J6EiYzu6ZFlUEl6OtNo1agB4pzX4zq5Y6fn-QJmcEw31kiHCw-u6Nzf3UEw_7uVY9ltAQxbX_wopBWpyHcoCP6OEwr5jBnLOaYCdsQGHccVaLWAb9bPC_wuhJLs_sEeFnH6EPDMNMJR7B9sk6AjNo21kZ5eeYJdLf0zSZDv8VNv1Uioig8u0NttWJnDxNh9KdRcXHFFC0-WP3o3xB3YM0v1FuCfVHHOW7uOT5cVS3jzqgM8L3ItgMGwg-AYES6OzemR1ybkC2cnEGgkXn_Jb-hAIn9mTBaTSBt1UMLcKA89cYh_UI9pkyOyNEK5ANHU5eXvZz2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d59a9154d0.mp4?token=RgN1u21Ngqrs-i9J6EiYzu6ZFlUEl6OtNo1agB4pzX4zq5Y6fn-QJmcEw31kiHCw-u6Nzf3UEw_7uVY9ltAQxbX_wopBWpyHcoCP6OEwr5jBnLOaYCdsQGHccVaLWAb9bPC_wuhJLs_sEeFnH6EPDMNMJR7B9sk6AjNo21kZ5eeYJdLf0zSZDv8VNv1Uioig8u0NttWJnDxNh9KdRcXHFFC0-WP3o3xB3YM0v1FuCfVHHOW7uOT5cVS3jzqgM8L3ItgMGwg-AYES6OzemR1ybkC2cnEGgkXn_Jb-hAIn9mTBaTSBt1UMLcKA89cYh_UI9pkyOyNEK5ANHU5eXvZz2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت شهید حاج قاسم سلیمانی از فداکاری و ایثار شهیدان در دفاع مقدس
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464258" target="_blank">📅 01:20 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464253">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UC4cCozRHKtL4c6HiGSNly_0l0lrcI-McmJJYYClO2SsBpb6I5rN4UZ7f4t9ioDyxZqAM1uAEIIEXmHX6uBejxaDZmJOvxf8byOPC8hPFBF_0EYY7zdyb9H4pLsIZWPjGHFUKZtRmcm5pounJm0LXNSKOB7X4YDJjvcdhZjam3cNXb7DPbBxmmooNirhSKzfEi3gPtSASJHLrqGJXnRJMt12lmnptMkJedFCPUHsoE_c4xaP72cP-savglxeXL0oGFcfQoyTECv66tBSUfLC4dLKrillffrxwYQoghbCPjXhEsi-DLEcKUDYrq3xeHi2h4wQOLP6Jmye_5s3h74ajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GsnRYPqIme__kgUHQ16gA4b8zk3-_eHdryG5189N_RfMR0KgwWcDM3rKgvAklplSmLRwwXfZwnNrBx26t04JgVnWGcb0-THNEpE9m30zu5mYcg1CFlLlx_hxqacal5zja7P905bnpP4ABJoN-yfy7GrCpAsLSmQXdQXOFgj7tPOFVt4v3B6FOkE3LrxFitjInPHEE1c3mDxG2cIZ0XCO2KFaSZUesiQd3jylzmSXQJdV0eVakVnUzRmDfrx0LjIe6KZIb0GNnr2HVxjv1F2bH72wl37ss3Nl2JcJJBE2TR6Tb6zECiQBpPSFeZmHiKYkbiRMEju1OYh8MuCNE6qGHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q1kTkVsGPdyc7sEnqIO83Voq4N3hrE-DU0wE14V7gLcfQlcX5djV81S_Xq3X8_35FY4VhxtKGI73Qqd28RtAZ12IGRKszqiWGEiUFvk50A-xQ3kg6P4YBwkz8Ks77rrOB-zlZl62CP8eWJoIA9uQ6-wTxRFnsmiI7Pq1zKKt4PwSoz7SmM6nGIJEhSeuqAqpfbt1GdMY10fF5U7E0-S2uYn6ioI04qAgdvIlojftv-39uKdnGLzyUbhVvpeatstEJa_rUaTQKskJsIQShzuLC3O7WqjntfmQCetkZ01ve-UsXgvZToQXNnNSXqL2wXFjmFPD9eR1eCdYnjKG1aKeQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jl8oPOfmUt1m2RKfPQTCO7UXSllRlvn-65uhboYUL4SP3M3BX6X1HCZawQut3RTLl1UsuM9vvKeqbJtfW1YECoRFmVYqMjLh41Ay-aLYBprYj9mfDeJ_BICB3xZM-NqoAhlUHb5BE2UapJjVryPQe2Ix3mSe8TBZUMyVy_GVZlbGBgR3ZXE557O0-6YCmdduErgKxqEmI5_g5pVV6AUhbtTFlRzN90nOYLX5xN8l6EpgzV7J-feP2VviBU0PKqwyZMkFjGGtntl9MkzEI6FXSAZkj90OpyC9f7oNypbA3-4kQDVu1KogOElEXA81OXcqv_HSmE4mPXDmHRY_sV95hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fIlMALo1_gVbCgE77KvheXtR7pu5f3NcKspP6V1RU5JwHTSLK4XLT4ohUZ6-vA-6k1KneuGgAdnhHJG2ydFkuOH8V08nL-GsU6iKvWpJildGuW4TSM7UOoGymMghGrRUIJAWkaJ44ZC5gpdYlu4oMDPmWy52d93JGjUt0TpSJx5dHFgRJ4V1Tq_Std7zWUIzlwF9JfXJIS3Hj5v1NCg1gbn1VC57Xv7-_X5wi6Go6mFwjb1R_wphC3pVA2czGGxa9sxUCVDTyf8jXYT_1dRgQbe3PBQ_Srr9LlRfCeb2j2ESq-80WsHXMZzYiGENDo6N_0QomYMOX0SXjOTcVXF77Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم ترحیم آیت‌الله شبیری زنجانی(ره) از سوی آیت‌الله سیستانی در قم برگزار شد.
عکس:
حسین شاه‌بداغی
@Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464253" target="_blank">📅 01:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464252">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5594361bcd.mp4?token=IgIkHGUOTAsuhZ2ban-Jig4Kcgnw53jir15spP9lTTjgGE8kXG_KlB7OVIFs-L7y8ZOl-280ujLecTjWnr_Uoi9HI8N9p25J-kp2LueBL41HgaKr5FY0wxfx7dHPbJ5HVznFVzKyVWJqw2INfTDMBa4KlDA3ryEM7AUc3KQHI6hNQGUlwRB-bIPB-UYzT1kkFx1jYMNFtkDYXHSpCRB6Hh7HClsjuGu8yQdlSFcval0ncuJJXW9mVxydYdP_kroFOVXfpWlPDEUED-2mw_NYgMDS27SnOTWF-qHkcvZq8PdV5FgJ7VX2a5JZZWwHT4cWopTq8bZgPFzl676D3SzqfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5594361bcd.mp4?token=IgIkHGUOTAsuhZ2ban-Jig4Kcgnw53jir15spP9lTTjgGE8kXG_KlB7OVIFs-L7y8ZOl-280ujLecTjWnr_Uoi9HI8N9p25J-kp2LueBL41HgaKr5FY0wxfx7dHPbJ5HVznFVzKyVWJqw2INfTDMBa4KlDA3ryEM7AUc3KQHI6hNQGUlwRB-bIPB-UYzT1kkFx1jYMNFtkDYXHSpCRB6Hh7HClsjuGu8yQdlSFcval0ncuJJXW9mVxydYdP_kroFOVXfpWlPDEUED-2mw_NYgMDS27SnOTWF-qHkcvZq8PdV5FgJ7VX2a5JZZWwHT4cWopTq8bZgPFzl676D3SzqfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نوحه‌سرایی پرشور آهنگران در جوار مزار رهبر شهید انقلاب  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464252" target="_blank">📅 00:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464251">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LLwTOMbq8gxu6QtG1RMwufXkXzXkvfDG4QOjKapw4n7A3mAbQqnu-cANZMm7aYpCirpJ_HuQ2pq-mQE6lX5P00QxR7uePNRo2b7q9lm8YhMm5-ByOoeJ_KYzLSxhagyx6BArmwMu0ufHc2S5_0u99r_WXwYsERh0NCwUowGeHOECUII-P3iKxnVKxNL6QF_uRtK4EKXahB-pKMltKowEzDXG4wDJfzSnjso5EfVm9XnnLhq4TTnblArc-AmEJK7f8-GYitkW2hKbFKtw5pTypCtcqZSI9L-3O0YlQ__0Tze_jIeJ51MPnb31UpnwfZt8ujMn06gt3RisHxQDktiVqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
پزشکیان با نخبگان و صاحب‌نظران اندیشکده‌های مختلف آمریکایی در نیویورک دیدار و گفت‌وگو کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464251" target="_blank">📅 00:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464250">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEEpR5_oPYN5ANgtJPEdbi2_eeAFudz4Ew31zSjwKGj34W_cZ_HBlq0soqbSzGfJ-0uOayZ5bz9E2jD-_nZZUvKZ3Z_PYv7wV76cQPNlDl4uYQGUWlT5CxdxtxjxW7fcXaBQA77MBwZyRbGgsYHZQYOu-bO6I_hIYosGPoMlhP3ayVtLqhbXy7qJZacTj5mFBGP2Z42WJg6Du64aQq_8kL8QLhqVKbC2ft96UnmtlWilkxrVgF7i0qCwjdY5VPdfjnWLc3suwzXkhEkXZIbB3M2LwyaXJUl1zutsr0RBVw0mNRnckYqnQ_aX9BRoKPATWxqvtRRswSG_MSdJ5GVEAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی سپاه: آمریکا با وجود نیروی دریایی گسترده، نتوانست تنگۀ هرمز را به شرایط موردنظر خود بازگرداند
🔹
شناورهای آمریکایی از محدودۀ تنگه هرمز ۴۰۰ کیلومتر فاصله گرفته‌اند و همچنان در بحرین مستقر است. این یعنی پیروزی بزرگ ایران.
🔹
این وضعیت نشان‌دهندۀ تغییر معادلات منطقه‌ای و افزایش توان بازدارندگی ایران در خلیج‌فارس و تنگۀ هرمز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464250" target="_blank">📅 00:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464249">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSMM76rWEBprBd8u-msGznaVFTJFuddEG-xE_cay9ZZjxVtNGwetkkw2acUdTqcJ4W35QbpQLhhPJVyE64BpWip7SJNoBQ5stMmbZAws-sv4X2eYHaGkVKTu_h_XKeP8_30GPt_5YA-FKVMCvuJQRVM5ATsVaIA3qGNi0jYwF9WdWIqDMGg7ZwCfCgYnajaXge3lJ_eXDeaVXRyV9OV1_T5OfUJkDRaJc3pWpus59UUhrWnSlIkKRyy6LP9LF7liLWSVGRVapyxgvUd38Cmn7PpJwYX-voJvzNo5aKs3P1e6GkKBH8abjob2cIM5ypAX0H9EBEAF-jTOdKvGrinmmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرط دزدی
🔹
مردی هوس کرد دزد شود و برای اینکه این کار را حرفه‌ای یاد بگیرد، به نیشابور رفت؛ چراکه شنیده بود در آنجا دزد ماهر و باتجربه‌ای زندگی می‌کند.
🔹
وقت وارد خانهٔ دزد شد و هدفش را گفت، دزد ماهر او را پذیرفت و تحویل گرفت.
🔹
سپس سفره غذا را که پهن کردند، مرد دست راستش را پیش برد تا غذا بخورد، اما دزد جلویش را گرفت و گفت: «با دست چپ غذا بخور!» مرد سعی کرد با دست چپ بخورد، اما چون عادت نداشت، نتوانست و دوباره دست راستش را درآورد.
🔹
دزد به او گفت: «فرزندم! در این راهی که آمده‌ای، اولین قدم این است که دست راستت را قطع می‌کنند؛ چون حکم شرع برای دزد همین است. وقتی دست راستت را ببرند، باید بتوانی با دست چپ غذا بخوری تا سختی نکشی.»
🔹
مرد با شنیدن این حرف به خود آمد و متنبه شد. با خود گفت: «به‌خاطر به‌دست‌آوردن کمی نقره و سیم، عاقلانه نیست که دست به این ارزشمندی را از دست بدهم!» پس همان‌جا کلاً خیال دزدی را از سرش بیرون کرد و از این کار دست کشید.
#حکایت
@Farsna</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/464249" target="_blank">📅 00:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464248">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ولیعهد کویت: ایران از تنگۀ هرمز به‌عنوان برگ برنده در جنگ استفاده می‌کند
🔹
ولیعهد کویت مدعی شده که ایران از تنگۀ هرمز به‌عنوان یک برگ برنده در جنگ استفاده می‌کند.
🔹
او بدون هیچ اشاره‌ای به تجاوزات آمریکا و رژیم صهیونیستی علیه ایران گفته که اقدام تهران «نقض قوانین بین‌المللی و قطعنامه‌های شورای امنیت» است.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464248" target="_blank">📅 00:23 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464247">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyVBi0yEIM8WMphN5pdMXU0dcKGaDYWKJLMJnQTXwzX29hRMowf85AdsJ2fAtEaSHLhToxol785IbAG5A2nvou5SyBin3TfTDsnE9dMSN8yVZr92zBhYr-nU7ngR3QmL3f1cJajm2CukOLPl0msAHyNEZTBF95GLmBAOlV8m9HG__OQo3KyCyIA3PhBd0oK2ebu3hSEi04CbwCkjc1c2vs_tt06Frr9g3xitZF7Evtp9LTbcvwfD2uEgY5QAAMBC78N9hATAuEVVzBQdFgrjPDac12rn8dOK2azZgpMLfUneAL3QKGO8g0u0_0YAvUOKUfiVIxPDL9S_w7RBHeOPMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دیدار عراقچی و وزیر امورخارجهٔ انگلیس  در حاشیهٔ هشتاد و‌یکمین نشست مجمع عمومی سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464247" target="_blank">📅 00:21 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464246">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tttAD_5EI1iyHsg-lUJJ-9HijIVqIb1p8L2L96fZMs0MwYAc-g9F9eQA5_X8rEv4e9q_MmtzQ6HWDBuO0xxj_7kxDNNVCSpAJobppW8DI9gRslC4KFMFP2h2Jkt2HLaPunOfzaS7unEpJAdgFC8o7OWnTBfM7YdspDhRWflCDXDAL_OD8YYgFk5nvuD4TUo12BrfL6tJcr9_bUto8t-MB3XRcxEV5VAoOJXaLLQXraitkB72Mp8vHUKF6ny0RQlQwfZB6fJKom3kEbbmp4c2m_dRUxJRvU3jEpvLUPqu3qO1G6-j0Jv7R8mrZ1NoZa-Kog5ODAONTq_1LxNbWouSpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ اخبار تکمیلی از حملۀ آمریکا به پل‌های جنوب؛ ۵ پل مورد اصابت قرار گرفتند
🔹
استانداری هرمزگان: در ادامۀ حملات تجاوزکارانۀ آمریکا به استان هرمزگان، متأسفانه علاوه بر پل کهورستان، پل‌های دیگر شهرستان خمیر هم مورد اصابت قرار گرفته است.  کدام پل‌ها مورد حمله قرار…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/464246" target="_blank">📅 00:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464245">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=DxuUygCo4E-E5g1QSHWposjZQ1tb_b8jXe8koAC1LWlkohAmeKlYZ04mJ-62y8NXTTYjaL1E6Xzn9cnldaocQRm7aybnYeg-BM2szJP9O6GbStwLO68892CqyE5UnKKqitpFNj2DYoqDg4i6eaBXcbnGG0i41NsNuW4M8y2a8NrHAQPgKdTF7Ei7UW1arwKOHIGtamjnpqAPcgIbTm9JkX8qdp67DIA06fotn7RsEZWkh6HgKmTk9w0iQHNognl3ewBfWDPFPapk1tvN8dRtjeiQ2EEf6cKHkdCXrBy7-eHiZV5GbzLYJuGOay43CWviScDvlBfk8W-fdNmUAtUCUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9464a14b0d.mp4?token=DxuUygCo4E-E5g1QSHWposjZQ1tb_b8jXe8koAC1LWlkohAmeKlYZ04mJ-62y8NXTTYjaL1E6Xzn9cnldaocQRm7aybnYeg-BM2szJP9O6GbStwLO68892CqyE5UnKKqitpFNj2DYoqDg4i6eaBXcbnGG0i41NsNuW4M8y2a8NrHAQPgKdTF7Ei7UW1arwKOHIGtamjnpqAPcgIbTm9JkX8qdp67DIA06fotn7RsEZWkh6HgKmTk9w0iQHNognl3ewBfWDPFPapk1tvN8dRtjeiQ2EEf6cKHkdCXrBy7-eHiZV5GbzLYJuGOay43CWviScDvlBfk8W-fdNmUAtUCUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مسیرهای تنگۀ هرمز همچنان تحت کنترل ایران است
🔹
کارشناس شبکۀ ۳ با نقشۀ تعاملی بررسی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464245" target="_blank">📅 00:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464244">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🎥
مردم در میدان انقلاب تهران یک‌صدا فریاد «اتحاد» سر دادند
@Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464244" target="_blank">📅 23:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464243">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/727c2319e4.mp4?token=YNitUCIpQxEzLcAQb_lq0YjYmb0wG-Lm5wqLGBSULfYN2ulkxojx2YFYmjN5HJs-wzTTi9SF3FUzweIUr8CUEACaZ0bltVVjZBOHtmsxYN1qQ5GkPIIjCKFGopnuLAR7YoQFBp1z3GNplAQZ9TFaNUr0w4clAW6N4hfnwQY7hgNJK4KYLTuKVi7pS40z7dkAm_a_DhKj8YfQBP4xwMikvDl2IabCfxRnZUc9PECUtF33wMHo1YHW64NUTy0r3Ich9ircu8zSIR65WMlosAgcc3brMrD97TDEoJnGB8O9n4tLRoCTFZwhPncEPMIhbREIJ8EvGqi_vi9LxCDj9LTajA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/727c2319e4.mp4?token=YNitUCIpQxEzLcAQb_lq0YjYmb0wG-Lm5wqLGBSULfYN2ulkxojx2YFYmjN5HJs-wzTTi9SF3FUzweIUr8CUEACaZ0bltVVjZBOHtmsxYN1qQ5GkPIIjCKFGopnuLAR7YoQFBp1z3GNplAQZ9TFaNUr0w4clAW6N4hfnwQY7hgNJK4KYLTuKVi7pS40z7dkAm_a_DhKj8YfQBP4xwMikvDl2IabCfxRnZUc9PECUtF33wMHo1YHW64NUTy0r3Ich9ircu8zSIR65WMlosAgcc3brMrD97TDEoJnGB8O9n4tLRoCTFZwhPncEPMIhbREIJ8EvGqi_vi9LxCDj9LTajA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم به سخنرانی رئیس‌جمهور در سازمان ملل چه نمره‌ای دادند؟  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/464243" target="_blank">📅 23:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464242">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e7fb8772c.mp4?token=oqpX8__KO0oA8ZDjMPBukTL5YxHZxtvDmU7n7BSVi_2P3HGS1MRPZMQJj_Lf9RBUrN56jQ8ZHD5ILx0mmDPK_Vyxyu7Ed7x-9hilTgtKcZ-xNYW0qQeUn2WlWaIWQmYt01Kyi_gb4BA_X0_qFTzA5X7FZ8c-7jTA3oM2AoNC9j4xMBVMbdVEUzof70sGEBGZW5CODm_AbwzQIRNdyHINyv9239Ms1telIrI2CsyqPBgc4xLf6Uq2d7-xvu808tpqQejXs0jbnmGHxW1c6pJ2N9CZzzx9kXiXcvBZwcXN6AY5wfSPqJMmoNlLlHS5lg4HTVVvjDsuUGfDnmvYsBQe8lI84fVlnF1YV0gqVh52PLazh-D3Bem4Gjjc2sf3GgV2xzI9Uk0iyazWyGDKFYfSmKgaGb2a86OgZRau7T5nfys7WrSGbY7vLlU8HsGMmeBAfyoiNOXTAmQKS2jbqS5qd8yGm_8EbWJUEv0MTKHyzBugRt5ZUvXRVrU8Sr1uvPo9o7J68DHQRu8K_99uWL7TeTKIHdxPE5-Oy9Axx9dOKZRWrX-FMItY7Pgj5yRcpt9MBYE0sZdQqg7gc61ct068Dcy92yP-WnS5yjR2woSIAKpxev20H65jcx7gZhF1I0p2jMivV7uCG3uJUib2XzMO--zpKMRKPmNZRRR7-GR7JCo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e7fb8772c.mp4?token=oqpX8__KO0oA8ZDjMPBukTL5YxHZxtvDmU7n7BSVi_2P3HGS1MRPZMQJj_Lf9RBUrN56jQ8ZHD5ILx0mmDPK_Vyxyu7Ed7x-9hilTgtKcZ-xNYW0qQeUn2WlWaIWQmYt01Kyi_gb4BA_X0_qFTzA5X7FZ8c-7jTA3oM2AoNC9j4xMBVMbdVEUzof70sGEBGZW5CODm_AbwzQIRNdyHINyv9239Ms1telIrI2CsyqPBgc4xLf6Uq2d7-xvu808tpqQejXs0jbnmGHxW1c6pJ2N9CZzzx9kXiXcvBZwcXN6AY5wfSPqJMmoNlLlHS5lg4HTVVvjDsuUGfDnmvYsBQe8lI84fVlnF1YV0gqVh52PLazh-D3Bem4Gjjc2sf3GgV2xzI9Uk0iyazWyGDKFYfSmKgaGb2a86OgZRau7T5nfys7WrSGbY7vLlU8HsGMmeBAfyoiNOXTAmQKS2jbqS5qd8yGm_8EbWJUEv0MTKHyzBugRt5ZUvXRVrU8Sr1uvPo9o7J68DHQRu8K_99uWL7TeTKIHdxPE5-Oy9Axx9dOKZRWrX-FMItY7Pgj5yRcpt9MBYE0sZdQqg7gc61ct068Dcy92yP-WnS5yjR2woSIAKpxev20H65jcx7gZhF1I0p2jMivV7uCG3uJUib2XzMO--zpKMRKPmNZRRR7-GR7JCo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رستاخیز وطن در شب ۲۰۸؛ روایت اقتدار و مقاومت کاشمری‌ها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/464242" target="_blank">📅 23:09 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464241">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpGbleDLXPi2COZx1JPkzbnq9vKvQdcEh2t-DJQLk6ReoMzwceu0vY1Gl2m-iLZyaqpEFA07mTvp0o40iTlUaSF6QX1TbJHae1uLGIhJFHeTjvNDrUDStVYQsQ0GYQZ7ylI4t1Y2Iuugd2mA-atAwSCKSRf31F0abBr1alkToNQMvhBsX3HC8811q7me35iT7CdWes1Pa1dc4nlK6Y6iYEzdnqXJ2hwIYaX_JzGh8IGUrFuyl7wztSRuVjEC-5o2dIqSs3tiSLlRqbm_8vrlAKHS1XccfnOt7xCPQj1Ewu91O2l6j-dLamUA8Lh3WJ_s-l0oOA4GEskgz995NDdYOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس‌جمهور در امور زنان: پیگیر وصل شدن کالابرگ و یارانهٔ زنانی که به تنهایی مسئولیت فرزندان را برعهده دارند، هستیم
.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/464241" target="_blank">📅 23:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464240">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1e3d63db.mp4?token=ph7NEtBAC4FqffOg4IIyeuzBzTf6-w0IxwpRFjAwiDxSr_E9w3IBlmklQOM6n4fDSDknQA-ykc3jXbsV3E7Tchgm9PnCCcY-wmAAjilRj10vg6bgDn7rkAwtB2WFWqlppkA0-28oVs4kspeyIIaE3gYzwNYmG3SfAw-683qIP7eqMeod03jc4D1-wcgKuIqmkhkdl3XWMgzj2_RtMhoIPCymGwGsklwuUfGnIUKE5RObDEkaQmua8ifh06svQAYOui4mQeXIWbUPgWrA9S1iStaiTfEg5-DsLJs6vxITgiDyL4-X5LE3Cu1cSKnKW5tL55pI2UiZApwgfNzzdBjuig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1e3d63db.mp4?token=ph7NEtBAC4FqffOg4IIyeuzBzTf6-w0IxwpRFjAwiDxSr_E9w3IBlmklQOM6n4fDSDknQA-ykc3jXbsV3E7Tchgm9PnCCcY-wmAAjilRj10vg6bgDn7rkAwtB2WFWqlppkA0-28oVs4kspeyIIaE3gYzwNYmG3SfAw-683qIP7eqMeod03jc4D1-wcgKuIqmkhkdl3XWMgzj2_RtMhoIPCymGwGsklwuUfGnIUKE5RObDEkaQmua8ifh06svQAYOui4mQeXIWbUPgWrA9S1iStaiTfEg5-DsLJs6vxITgiDyL4-X5LE3Cu1cSKnKW5tL55pI2UiZApwgfNzzdBjuig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
احمدی مقدم، رئیس دانشگاه عالی دفاع ملی:  صدام هم فکر می کرد ایران را یک هفته ای از پای درمیاورد، اما ۸ سال در این باتلاق ماند
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/464240" target="_blank">📅 22:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464239">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQhzIEzDVGT6Wcm_6tF0qPjKRTOFuK_gCX2LqmXwHyJR7z0dDiXUt9SwoXr1fz3B05Fc3vX9gXNP2z5ZkI2Owi9q7TSQM_uRd5RyyYTLtYvo06Z3owutWVxAXZ95-OHVxpyDokESXI_Yu4PaB8bEIWIE6DmwW4TpHGNPprGPXZnr2KNs0drl4gAnwyBy_ig57uSzL98ZE6CGLS5vtV7OD0uPuQb9aHwwiwl1qaPJVwK-b2lQu_p2tS4nZBULPc_prraOHj9dLqwKdc7ThIa9HAzuPPhROOhAiR8RPCeRzbyZujFdxo9rKW3i4s8tjd_BpKzCk30nquJiXqdlUN8EQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
غریب‌آبادی: مشارکت اروپا در تجاوز به ایران بی‌پاسخ نمی‌ماند
🔹
اعتراف دبیرکل ناتو به انجام ۵۰۰۰ سورتی پرواز از پایگاه‌های اروپایی در حمایت از تجاوز نظامی آمریکا علیه ایران، نشان داد اروپا بخشی از زیرساخت تجاوز بوده است.
🔹
دولت‌هایی که قلمرو خود را در اختیار آمریکا قرار دادند نمی‌توانند از مسئولیت شانه خالی کنند. این مشارکت بی‌پاسخ نمی‌ماند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/464239" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464238">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🎥
عکس حاج قاسم جلوی چشم نتانیاهو در سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/464238" target="_blank">📅 22:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464237">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsppmZWc5uL7nM7etlR5uRuztL2GwXDubuYkbV5r-37IVkgiV6LxIXY_HLC-DzHmPc3UT-NPrNuw5bTcKW7gjxcVsPx2fYhYCqbO3aBr_a2wQQQUmAACon7FB8VUyhwi69Z1KGb41mXViSz2nhp03Xy_UV6Mj7E3n6u3UZGDUU-vdw3YzdC4QWNgKlZ4hdW_QPjMqelSzdnVdt4V5xILkKuyWRmnn46S2msjHbdF5raEMK7--25bIsdL1gk_-_aIju7AsTyfHCVj64zN0Rmd-iA-c11spkfVu0EehExxqDpx6htmD1RZu0bUxMVJrwR_0p5qVyT1k8fjkzFipsoaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملات ارتش یمن به عمق عربستان سعودی
🔹
سخنگوی نیروهای مسلح یمن شامگاه امروز از ۲ عملیات نظامی در خاک عربستان سعودی خبر داد.
🔹
یحیی سریع گفت در این عملیات‌ها، یک مقر بسیار مهم در ریاض و تأسیسات نفتی آرامکو هدف قرار گرفته است.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/464237" target="_blank">📅 22:39 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464236">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa14fb258.mp4?token=KcA3qAxDo-_XEZ8URlwu6Fr9-tQA7xSbxYkRoYAl2FeOzICJ8qUWKKRWtqmaxytKylGmFvlSJAIrBYyABpswiZ_kJ2EBNhFTPawS_dUHPrnfNAqRT18DBEa-pukH-ku8RZCMmBvcoTHqi5Xh74Jxp748bAMoDbnBkDhh7SAnRQcotDpSymShEKMItDFBEUKNSjU_YBAi3ZsAotj1gQqB1dxMjP5V_TipmOnjgEwbAD9SsZY1QQaCl8zT37iyyYzauNW0D2J-fNlCQRvajjQ2FdUvBG0wD3-w6pYRQZCYQFRXPM3EWQZhQ3eSXxo70HkTaq5H7H6wTKe2ROgYAHm_Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa14fb258.mp4?token=KcA3qAxDo-_XEZ8URlwu6Fr9-tQA7xSbxYkRoYAl2FeOzICJ8qUWKKRWtqmaxytKylGmFvlSJAIrBYyABpswiZ_kJ2EBNhFTPawS_dUHPrnfNAqRT18DBEa-pukH-ku8RZCMmBvcoTHqi5Xh74Jxp748bAMoDbnBkDhh7SAnRQcotDpSymShEKMItDFBEUKNSjU_YBAi3ZsAotj1gQqB1dxMjP5V_TipmOnjgEwbAD9SsZY1QQaCl8zT37iyyYzauNW0D2J-fNlCQRvajjQ2FdUvBG0wD3-w6pYRQZCYQFRXPM3EWQZhQ3eSXxo70HkTaq5H7H6wTKe2ROgYAHm_Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دستاورد جدید محققان جوان ایرانی در حوزهٔ سلامت؛ داروی درمان کبد چرب التهابی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464236" target="_blank">📅 22:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464235">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb318597f.mp4?token=YOlPNz7sNKCkJt5irPqRoNW10RxyFLk1mqI0Cg7947jOwZWcW5vbdXgZ11Ta_P5zxrbxfy6ikr3G7CGsxwh5c-_MDZYw9bCfiYgwVWtNF2rf2X3uRNtl2UlzbwzPSOlD9D08okevW6DKX9oRVE1xzhl-vZcGGPyv1TnuOuIqP4iLZvXQGhhMNtWNO1O83923_UFSLKB399hJK25rziO69OBUhPrW6zQY3yMsp_h8udKGRXG0QhNISzfBjST7t_YXPKbSjOx3XyYnSkUKRUnEKIKruJG-b4CZp202bGCYqBH2cuDGzwG1eT9hQF8tZdAHvVkC0hrx3wcEIquPRCcBKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb318597f.mp4?token=YOlPNz7sNKCkJt5irPqRoNW10RxyFLk1mqI0Cg7947jOwZWcW5vbdXgZ11Ta_P5zxrbxfy6ikr3G7CGsxwh5c-_MDZYw9bCfiYgwVWtNF2rf2X3uRNtl2UlzbwzPSOlD9D08okevW6DKX9oRVE1xzhl-vZcGGPyv1TnuOuIqP4iLZvXQGhhMNtWNO1O83923_UFSLKB399hJK25rziO69OBUhPrW6zQY3yMsp_h8udKGRXG0QhNISzfBjST7t_YXPKbSjOx3XyYnSkUKRUnEKIKruJG-b4CZp202bGCYqBH2cuDGzwG1eT9hQF8tZdAHvVkC0hrx3wcEIquPRCcBKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار گرفتن تصویر شهید سلیمانی روی میز هیئت ایران هم‌زمان با سخنرانی نتانیاهو
🔹
رسانه‌های عبری تصویری از محل استقرار هیئت جمهوری اسلامی ایران در نشست مجمع عمومی سازمان ملل منتشر کردند.  @Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/464235" target="_blank">📅 22:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464234">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee49a98248.mp4?token=DShJxSRcsJZfieKe2CZQQvYUr6ejG4Rldzz76XMrlQKXiFEp8aBwZSJqVKL5OrM7Ho0zjiKWXbDD61Qma3iECTC-D_P_X4cFeLv5IiwOxk3ax9tUZecg-ZBamo5pu5wHWUIY0rEbyfetWrc7Erk0oahCpoyFe_VvX-PXhEjGG2SMMb0AosO3Fe4b7KRwFkYHE3dkGq5ugO6N54gC0tQ9vl3twX0v5fdzSYwbaNHYLx1hSOq4BmiVjtIee6coMPryPiFkHbZMDVi_nRaPPMzhBgiRI_GaomIKK4t2hXdNDyil724VcqnqVuev2TJ50J9ZKlNYgnn232dowKGDLECpNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee49a98248.mp4?token=DShJxSRcsJZfieKe2CZQQvYUr6ejG4Rldzz76XMrlQKXiFEp8aBwZSJqVKL5OrM7Ho0zjiKWXbDD61Qma3iECTC-D_P_X4cFeLv5IiwOxk3ax9tUZecg-ZBamo5pu5wHWUIY0rEbyfetWrc7Erk0oahCpoyFe_VvX-PXhEjGG2SMMb0AosO3Fe4b7KRwFkYHE3dkGq5ugO6N54gC0tQ9vl3twX0v5fdzSYwbaNHYLx1hSOq4BmiVjtIee6coMPryPiFkHbZMDVi_nRaPPMzhBgiRI_GaomIKK4t2hXdNDyil724VcqnqVuev2TJ50J9ZKlNYgnn232dowKGDLECpNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جملهٔ خنده‌دار نتانیاهو: متهم‌کردن اسرائیل به نسل‌کشی، بزرگ‌ترین دروغ قرن است!  @Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/464234" target="_blank">📅 22:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464233">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDqMl8tv5LH1t29Tuc0S7RTsJ2baRsY6GpBTua0877w4wrwbQjzxFnt1LPQpWX7LtnhyG16RSu_8PTfDGA6969FKQEeON3_SxSM25LzkwfqODSp2X5vZykKrUARyYg4KLRp6YM9Doci7xpa2GkTcaqrD1S6SFFQn9SbuQdQVEDJcaTEQtQTwUFdHXzcLV8ouzM-9rQTMQ7NHHow4GipgA81wSk4Z8m-i925m1KqpqbI9I_UJ8vHNR9fgEuC-q-2psazegwDR7ixnJUGZDYFhge_bWnuAvDL5IcO5MJIFvxNgtwuqFhAVruKjqORn1ARGPeLAgQ6qIaB9UVTZZoJ1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنا بار دیگر از جنگ علیه ایران حمایت کرد
🔹
سنای آمریکا امروز قطعنامه محدودیت اختیارات ترامپ در جنگ علیه ایران را رد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/464233" target="_blank">📅 22:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464232">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3e8ded099.mp4?token=Zbu1uciT31hAylImG8ngo0eYMmqBFuUa0bvU2Gzohof2IwqpcF-E6XSi4rViFqJzVA8xpP-PLj-u2OfxDrJDek5N--2ytkzMkjUNNM-XOYvTWd1GSyJJ0YSEDlfgHg7xLYdlhXM8MGU6FbcAzS2EDAv-jt14-qlfOS8s-wERiUElsoGDbo8H0Vi4re7g8FBFfaneQGDMbpfbl3pcTeRK3_coRhRDcJ_t_ZxszcVTV1eMGReGFhxY9_YbPrITZiIdsflt1Apl5o2CuSOglyzzso1-xRbY43dgQLbIBpiwy_lfCPVi3YlJtgB6lvVQKxwj6E8FZ_pj--kGiAmKQFpoYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3e8ded099.mp4?token=Zbu1uciT31hAylImG8ngo0eYMmqBFuUa0bvU2Gzohof2IwqpcF-E6XSi4rViFqJzVA8xpP-PLj-u2OfxDrJDek5N--2ytkzMkjUNNM-XOYvTWd1GSyJJ0YSEDlfgHg7xLYdlhXM8MGU6FbcAzS2EDAv-jt14-qlfOS8s-wERiUElsoGDbo8H0Vi4re7g8FBFfaneQGDMbpfbl3pcTeRK3_coRhRDcJ_t_ZxszcVTV1eMGReGFhxY9_YbPrITZiIdsflt1Apl5o2CuSOglyzzso1-xRbY43dgQLbIBpiwy_lfCPVi3YlJtgB6lvVQKxwj6E8FZ_pj--kGiAmKQFpoYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
قاتل ۷۳ هزار زن و کودک اهل غزه: اسرائیل مرتکب نسل‌کشی نشده بلکه از نسل‌کشی جلوگیری کرده است!  @Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/464232" target="_blank">📅 22:19 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464231">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea3bd5cad7.mp4?token=MdbqtJBCDMQT2nU6rFij14Z4wpJCkE81ndjsxd3FZjS57copYJ1bXLwqEILYhxtSb_Q0sp7SkRQtGMd_SLvN6MfOPY3PlXjjtkseOmXYc7FeKFqXY2b2yc2DCVA7u4XQLRP73XRLgQh1URPUOXQcsapK43AUsYAJ4TvKvUMn_9hdUTn6FBwULssnoc5kC2SLiTEbATkMjrTAHM-4KRa7UC3jRDSkVQuL0RWXvONwmL0zTLMSG-4o365YXMhmK1il3jY066G3E7lsFfjSGeUlvEHtTtItdPoDW6PD4C4cYu5E-xhBrh1byIjEG0nUkbz8eMmRIPVnduwV-u7Z8KLoZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea3bd5cad7.mp4?token=MdbqtJBCDMQT2nU6rFij14Z4wpJCkE81ndjsxd3FZjS57copYJ1bXLwqEILYhxtSb_Q0sp7SkRQtGMd_SLvN6MfOPY3PlXjjtkseOmXYc7FeKFqXY2b2yc2DCVA7u4XQLRP73XRLgQh1URPUOXQcsapK43AUsYAJ4TvKvUMn_9hdUTn6FBwULssnoc5kC2SLiTEbATkMjrTAHM-4KRa7UC3jRDSkVQuL0RWXvONwmL0zTLMSG-4o365YXMhmK1il3jY066G3E7lsFfjSGeUlvEHtTtItdPoDW6PD4C4cYu5E-xhBrh1byIjEG0nUkbz8eMmRIPVnduwV-u7Z8KLoZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نخست‌وزیر رژیم کود‌کش: ارتش اسرائیل، اخلاقی‌ترین ارتش جهان است!  @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/464231" target="_blank">📅 22:18 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464230">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njIXv_T8mmGpMfFpD4upJp4NH4xOw9W6nAg3XyUAVRapwqRVcYcoR0tP3xLUtmNfFxJm87bWsIeL-n_r79pW0UcX8-9B3bmy3ZsTD3hZQlznXwXzlrUJsbVDPWgDjIA21GoVflNK-6qXfb3V-abkRjsehxpVdTOvNd3TMEHIoqCHW4nMbOZnsMyQCMqwoG-xfg7dEdNdS0C_E-rGvKo-wTm58m44dD_RDaGoPf8s33nDOQfXa_LiDMekDanG39IsW-sfFvc834sPtsSbYZf67u0xzzeB5T9OpeI4yowqXVipzPAD4KAwoefEvaFMzEgrU9AuLltHSBEpE2_YVZ_n5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ امارات پای صحبت‌های نتانیاهو نشست
🔹
درحالی‌که هیئت‌های بسیاری از کشورها حین سخنرانی نخست‌وزیر رژیم صهیونیستی سالن سازمان ملل را ترک کرده‌اند، نمایندهٔ امارات درحال گوش‌دادن به حرف‌های نتانیاهوست.
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/464230" target="_blank">📅 22:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464229">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89a10092a8.mp4?token=HA2bGCakrGkRn9Yc9HH5kf_HlxFude3G1rmzClFbR64OAjjUb1DO2pCud7QO8SLhbyw_GaIO1K1H3MloNDUGp9aHnOGYjHsEosDa1dBdSQcBhoYl9aFsfa62VdgrTChqDcM6syUgDF6_TBTE8M4zIShIV4jFztskX7jQaa5lfUJj-l9Par34WUb6OUUWgxVf3-WBc2kUBiRzFj7cm10DkSCQowtr4L7QEgnPNU8N6CVqJiWF3ozc-u-r4N1yWGzBxE4ioywKcAOITzFj4mhvcop91atsJs3QMJVgHafuNZvaxll7PBRNTjSuKZ-HNaxekICLF8CMXPzfZWanIMonDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89a10092a8.mp4?token=HA2bGCakrGkRn9Yc9HH5kf_HlxFude3G1rmzClFbR64OAjjUb1DO2pCud7QO8SLhbyw_GaIO1K1H3MloNDUGp9aHnOGYjHsEosDa1dBdSQcBhoYl9aFsfa62VdgrTChqDcM6syUgDF6_TBTE8M4zIShIV4jFztskX7jQaa5lfUJj-l9Par34WUb6OUUWgxVf3-WBc2kUBiRzFj7cm10DkSCQowtr4L7QEgnPNU8N6CVqJiWF3ozc-u-r4N1yWGzBxE4ioywKcAOITzFj4mhvcop91atsJs3QMJVgHafuNZvaxll7PBRNTjSuKZ-HNaxekICLF8CMXPzfZWanIMonDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نتانیاهو با نمایش پیجر در سازمان ملل به اقدام تروریستی خود در لبنان افتخار کرد
🔹
نخست‌وزیر رژیم صهیونیستی: پیجرها را به یاد دارید؟  خب، این را می‌توانم به شما بگویم که حزب‌الله حتما آن‌ها را به یاد دارد!  @Farsna</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/464229" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464228">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DoarZbpeJvndBgwTAOD538LTC3hon4sIIdyp6nb-LN91lqrzDTtzoo0vj83q5FGU0rsFAyLkjMdAhU4YRDYo0WFcQqln8Frc2mIzYSo3R2r6VDRVHzxTjCLPvzheqFqVuJX6xIiENnpBjcVyiU83kEUW40MtduxZR5EMj77KoyIWzNkB-ZgBCM05p-0JnNXOZg2S3JfxoT2q_ZYlaIG5Qo0Uxc3iLPkBCb-BQ9-NHvl_PZ2Mwxj0mtf5xM9c9v2txlE_mE6P7VnR4kXuKA2Ge0nXLk55N7RAk-sRUEmLmRNrFHoGi9JppNKrSY86d_Pa16GNVqIn5cjcGrNwnNPySg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قرار گرفتن تصویر شهید سلیمانی روی میز هیئت ایران هم‌زمان با سخنرانی نتانیاهو
🔹
رسانه‌های عبری تصویری از محل استقرار هیئت جمهوری اسلامی ایران در نشست مجمع عمومی سازمان ملل منتشر کردند.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464228" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464227">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d84ce924d3.mp4?token=FwO8oqxWx5ODGy_VuYPUbmU_Hr5IOOcElawB62F_EvKT1Pk4GC0R7Kdi8llWGZ3qz3p3pzZulbJ9S0Tk9lUM-l6ygKaZwzkcRV4zqfdzjWH8CkTIm5xNt1RPU0XlnRB9lOiqQyZRSc2mLlskz48lUQJfWrhmsptfksEJegK1SKWyqZhQhkHexa5Xaxyw88I_Xe7UZrqN2KVz2XVE70boOEOxqe58epXEppzyyk0IOlFAeRF1Qrg4W5AXI7Dher6lOanacVnxfty36Dmqw3ey_0_KuX2Mcxh1sh7mBr39XlJ70juPBy8tNK3uX1mqB1QqfNsQ4DahkyEbxdWg1L7MvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d84ce924d3.mp4?token=FwO8oqxWx5ODGy_VuYPUbmU_Hr5IOOcElawB62F_EvKT1Pk4GC0R7Kdi8llWGZ3qz3p3pzZulbJ9S0Tk9lUM-l6ygKaZwzkcRV4zqfdzjWH8CkTIm5xNt1RPU0XlnRB9lOiqQyZRSc2mLlskz48lUQJfWrhmsptfksEJegK1SKWyqZhQhkHexa5Xaxyw88I_Xe7UZrqN2KVz2XVE70boOEOxqe58epXEppzyyk0IOlFAeRF1Qrg4W5AXI7Dher6lOanacVnxfty36Dmqw3ey_0_KuX2Mcxh1sh7mBr39XlJ70juPBy8tNK3uX1mqB1QqfNsQ4DahkyEbxdWg1L7MvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توجیه نتانیاهو برای اشغالگری اسرائیل: یهودیان از زمان حضرت موسی در بلندی‌های جولان بوده‌اند!  @Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/464227" target="_blank">📅 22:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464226">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
خانوادۀ ما هیچ‌گاه نتوانست برای سهام عدالت ثبت‌نام کند.
همسرم از کودکی در خانواده‌ای روستایی با کار کشاورزی بزرگ شده و بعدها به خیاطی روی آورده است. با وجود ۲۲ سال کار در یک شرکت، در ۵۱ سالگی فقط ۱۲ سال سابقه بیمه دارد و پس از تعطیلی شرکت دوباره به خیاطی مشغول شده است. سؤال ما این است که چرا فردی با چنین شرایطی که نه بیمه و بازنشستگی مناسبی دارد و نه وسیله نقلیه،
از سهام عدالت محروم مانده
است؟
🔹
بیش از سه ماه است از
آسیاتک
خط فیبر نوری، بسته یک‌ساله اینترنت و مودم خریداری کرده‌ام و قرار بود حداکثر طی دو هفته نصب و راه‌اندازی شود اما هنوز این کار انجام نشده است. هر بار هم با
پشتیبانی
تماس می‌گیریم، می‌گویند درخواست ثبت شده و تا دو روز دیگر وصل می‌شود، اما همچنان
خبری نیست
.
🔸
چرا با وجود اعلام مصوبات دولت دربارۀ
سقف افزایش اجاره‌بها و تمدید قراردادها
، در برخی موارد دادگاه‌ها
حکم تخلیه
صادر می‌کنند؟ این تناقض باعث بلاتکلیفی و نگرانی بسیاری از مستأجران شده است.
🔹
مدتی است
سایت جست‌وجوی متوفیان بهشت زهرا(س) قطع شده
و امکان استفاده از آن برای مردم وجود ندارد. خواهشمندیم شهرداری تهران و مسئولان مربوطه برای رفع مشکل سایت اقدام کنند.
🔸
دربارۀ وضعیت
بیماران اعصاب و روان
، به‌ویژه افراد مبتلا به اختلال دوقطبی، گزارش و برنامه خبری تهیه شود. بسیاری از این افراد، به‌خصوص جوانان
از داشتن شغل و بیمه
مناسب محروم هستند و افزایش هزینه دارو نیز فشار زیادی به خانواده‌هایشان وارد کرده است.
🔹
ما حدود
۳ هزار دانشجوی سال آخر
هستیم که در
آزمون مهارت‌آموزی آموزش‌وپرورش
شرکت کرده‌ایم. از بهمن ۱۴۰۴ آزمون دادیم و خرداد امسال نیز مصاحبه تخصصی انجام شد اما حدود
چهار ماه است برای اعلام نتایج در بلاتکلیفی هستیم
. آموزش و پرورش می‌گوید نتایج را به سازمان سنجش ارسال کرده، اما سازمان سنجش اعلام می‌کند چیزی دریافت نکرده است. بسیاری از داوطلبان نیز به‌دلیل وضعیت سربازی، قبولی در مقطع ارشد و برنامه‌ریزی برای آینده، با مشکل مواجه شده‌اند. خواهشمندیم اگر می‌توانید این موضوع را پیگیری کنید تا تکلیف ما روشن شود. ما فقط یک تاریخ دقیق یا یک اطلاعیه ساده می‌خواهیم.
🔸
لطفا در مورد
خودروهای ثبت‌نامی سایپا
پیگیری ویژه‌ای انجام شود. ما در تیرماه ۱۴۰۴ ثبت‌نام و در بهمن‌ماه همان سال تکمیل وجه کرده‌ایم، اما با گذشت حدود هشت ماه هنوز خودرو فاکتور نشده و هیچ پاسخ روشنی نیز دریافت نمی‌کنیم. برای پیگیری به
تعزیرات
هم شکایت کرده‌ایم، اما اعلام شده این موضوع در حوزه مسئولیت آن‌ها نیست. ما یک سال پیش برای خرید خودرو طلاهای خود را فروختیم، اما اکنون
نه خودرو تحویل گرفته‌ایم و نه کسی پاسخگوی ماست
.
🔹
از
پیمانکار شهرداری منطقه ۱۰
خواهشمندیم به ایجاد
جوی غیراصولی در کوچه دلخواسته
، نبش سلیمانی رسیدگی کند؛ چراکه این جوی باعث تجمع لجن و ایجاد بوی نامطبوع شده است. همچنین از شهردار منطقه ۱۰ درخواست داریم با حضور در کوچه دلخواسته، مشکل تردد خودروها را بررسی کنند. با نصب پل، تردد خودروها در این کوچه افزایش یافته و آسایش ساکنان سلب شده است.
🔸
کالابرگ ماه گذشته برای برخی اعضای خانواده ما واریز نشد
و متأسفانه کالابرگ این ماه نیز برای آن‌ها واریز نشده است. با توجه به شرایط مالی خانواده، این موضوع برای ما مشکل‌ساز شده است. لطفا پیگیری کنید.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/464226" target="_blank">📅 22:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464225">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b138f38651.mp4?token=Zu7V9SHXeyayW3dJPM-AGmbqs7SfdPOsEJfJYpWZlQS775N846Xh51ZeweAzA8YsSXsLvJ2onewmnF6ii2L7iKfbTJAZZgzLpKCMo5hQ5YoZcD8SyjyhaOV3viT9LX6hnLLE9ZI5cxHW7AgLr4NY2z-tG_idwXSunTfS1JGQ5gWR_zxuknyKEi4Kr-7jcS5UUqsORrJ-KxBIYIauCbVHMvgwPIRu9iYzoclZuyTxaYiCa1wcZ46vyR5IVoHZm2Gop0fISV_m9FbFR5yzSm7bl9odk6kXVbHgkmPFdy2cdJNhpimnB4Ln3n0Ob0i8pY0u-AdNbdxJqVp7EmhwbzrVlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b138f38651.mp4?token=Zu7V9SHXeyayW3dJPM-AGmbqs7SfdPOsEJfJYpWZlQS775N846Xh51ZeweAzA8YsSXsLvJ2onewmnF6ii2L7iKfbTJAZZgzLpKCMo5hQ5YoZcD8SyjyhaOV3viT9LX6hnLLE9ZI5cxHW7AgLr4NY2z-tG_idwXSunTfS1JGQ5gWR_zxuknyKEi4Kr-7jcS5UUqsORrJ-KxBIYIauCbVHMvgwPIRu9iYzoclZuyTxaYiCa1wcZ46vyR5IVoHZm2Gop0fISV_m9FbFR5yzSm7bl9odk6kXVbHgkmPFdy2cdJNhpimnB4Ln3n0Ob0i8pY0u-AdNbdxJqVp7EmhwbzrVlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هم‌زمان با آغاز سخنرانی نتانیاهو، سران کشورهای مختلف سالن سازمان ملل را ترک کردند  @Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464225" target="_blank">📅 21:54 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464224">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🎥
هم‌زمان با آغاز سخنرانی نتانیاهو، سران کشورهای مختلف سالن سازمان ملل را ترک کردند
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464224" target="_blank">📅 21:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464223">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UoM-yKo4iENm-8ChIoE67gBK1iRPEUqcIkWZHnrxoiZrISoUYl75BmHUu3KvMYGcrx-6pGHSGNeq0bZ8zQHxY-akI-n4-rli_afHokqJgCN3MIfb923dCdpXqDNQFc1r3_C3GHAppG4SWoaWVSR2Ksl9J9_zYQYSQ3RibEj4jgf3ANHWAk35oK0BLf4oearFLmvI6D-daW4kHldj7SZCcgeuLaz8KQslpYP60in2K1O-9kOfFeztxQ3KvNXEQFElmApBYUmNslxch0-ptZz1L493Cd_itV3O_W_eW8xkhKE4u81Ha9mg3PayKLthxhrJo1YZ4dpH2sM_-oFxwXP0Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار یمن: مرحله بعد، برای عربستان دردناک‌تر خواهد بود
🔹
وزارت خارجه یمن تأکید کرد که افزایش شدت جنایات روزانه عربستان سعودی در یمن و هدف قرار دادن مراکز غیرنظامی و منازل شهروندان، ایجاب می‌کند «با این رژیم با زبانی که می‌فهمد سخن گفته شود».
🔹
این نهاد یمنی هشدار داد اگر عربستان تصور میکند که می‌تواند از مجازات فرار کند، در توهم و سراب به سر می‌برد.
🔹
صنعا می‌گوید به خاطر تداوم فعالیت‌های خصمانه و اقدامات جنایتکارانه روزانه عربستان علیه ملت یمن، مرحله بعدی برای رژیم سعودی دردناک‌تر خواهد بود.
🔹
وزارت خارجهٔ یمن از هرگونه تلاش برای صلح که منجر به رفع محاصره این کشور شود و به اشغالگری عربستان پایان دهد، استقبال کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/464223" target="_blank">📅 21:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464222">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">جدال بابک زنجانی و وزیر صمت بر سر سایپا
🔹
وزیر صنعت می‌گوید در واگذاری سایپا حفظ اشتغال موجود باید توسط خریدار تعهد داده شود اما بابک زنجانی می‌گوید مسئولان باید از شعارهای پوپولیستی برای تعهد بخش خصوصی عبور کنند.
🔹
فرآیند واگذاری سایپا به بخش خصوصی از حدود یک‌ونیم سال پیش آغاز شده است و نام بابک زنجانی نیز در فهرست متقاضیان خرید این خودروساز مطرح بود و پیش‌تر مدعی شده بود با پیشنهاد ۲ میلیارد دلاری قصد خرید سهام سایپا را داشته اما منصرف شده است.
🔹
حالا زنجانی در واکنش به شروط وزیر صمت مبنی بر ممنوعیت تعدیل نیروی انسانی و تعهد به عمق ساخت داخل، این مطالبات را «شعارهایی تاریخ‌مصرف‌گذشته» عنوان می کند و می‌گوید خصوصی‌سازی نباید فقط به انتقال مالکیت محدود شود و باید با محوریت توسعه فناوری و افزایش بهره‌وری همراه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464222" target="_blank">📅 21:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464221">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cac0ac8f6.mp4?token=C8_F3-h9dyBq-vBSP7KIOrl2aGZNy50O-zkBBmzphAehA6SwkDAHMY-bbOLcODymSvneef5CKolcWGLc8wCSMgOkkaMjhDz5AQJ8bUHzWtMdeuW2e-0oXvDagixx36dZpjIN2pyVPkQEQG0TS2xIfWiGSeeS8f6bbFHHpzxLtRVgxS4PwtT2bgvbWbnAc-MA6ojuh2f8noVqZmu5HGP2TU2kUy1JOH9PgqQT6xM9IKUGyCaOGVAKUL2wZfs7xod0PXsEcbQVLawKW2yMV9E6HuEZCieplLt5VLsTpFsfDHOenoN8gOD4uAYwZv_7J9LGXCm7gaWJWMgMKyJdA67WuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cac0ac8f6.mp4?token=C8_F3-h9dyBq-vBSP7KIOrl2aGZNy50O-zkBBmzphAehA6SwkDAHMY-bbOLcODymSvneef5CKolcWGLc8wCSMgOkkaMjhDz5AQJ8bUHzWtMdeuW2e-0oXvDagixx36dZpjIN2pyVPkQEQG0TS2xIfWiGSeeS8f6bbFHHpzxLtRVgxS4PwtT2bgvbWbnAc-MA6ojuh2f8noVqZmu5HGP2TU2kUy1JOH9PgqQT6xM9IKUGyCaOGVAKUL2wZfs7xod0PXsEcbQVLawKW2yMV9E6HuEZCieplLt5VLsTpFsfDHOenoN8gOD4uAYwZv_7J9LGXCm7gaWJWMgMKyJdA67WuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جان‌فدایانِ کوارِ فارس حماسه آفریدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464221" target="_blank">📅 21:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464220">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10289f5082.mp4?token=M4-bKNLfAd4c_PxT_dZKGWSQRUo0l5-gfTULcj0IYL7qQ7wegmQ1zFHtPVG8oI7pTQxZQpux91toLwQBLPDzCdOhYt3Yp1CYDWJNXbMOm9d1njZ8sGCbcT5zQQDZODT2J4CwOyptCteQInZSgKEZ0BPvAcfLLo-eH6cI_ATI75w7bAAUIG-IxwvKb7wyZy8kN8bRKFMMZcTQ7g6YAoYjR6mZI363eLA4bY1FVj854Gpl52lpdETwNP_wpvPGXXbHvM-2rdTP3_OQGaJ3UUq6MRM317EPyNipt3UK9MH8fTXHrlRFgYtxUN36djzMG5ZqTpW6a6Y3H2dbzhhfUkPFMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10289f5082.mp4?token=M4-bKNLfAd4c_PxT_dZKGWSQRUo0l5-gfTULcj0IYL7qQ7wegmQ1zFHtPVG8oI7pTQxZQpux91toLwQBLPDzCdOhYt3Yp1CYDWJNXbMOm9d1njZ8sGCbcT5zQQDZODT2J4CwOyptCteQInZSgKEZ0BPvAcfLLo-eH6cI_ATI75w7bAAUIG-IxwvKb7wyZy8kN8bRKFMMZcTQ7g6YAoYjR6mZI363eLA4bY1FVj854Gpl52lpdETwNP_wpvPGXXbHvM-2rdTP3_OQGaJ3UUq6MRM317EPyNipt3UK9MH8fTXHrlRFgYtxUN36djzMG5ZqTpW6a6Y3H2dbzhhfUkPFMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار و گفتگوی عراقچی و ژینبک کولوبایف وزیر امورخارجهٔ قرقیزستان  @Farsna</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/farsna/464220" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464219">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سازمان اطلاعات سپاه: ابتکارهای نیروهای مسلح جمهوری اسلامی ایران، معادلهأ میدان را تغییر داده است
🔹
حساب مجازی سازمان اطلاعات سپاه: مقاومت و شجاعت ایرانیان و استفاده هوشمندانه از جغرافیا، الگوهای پر هزینه و کم خاصیت رزم ارتش آمریکا را از طرفی با بن‌بست مواجه ساخته است؛ و از طرف دیگر، تخلیه و غیرفعال‌شدن پایگاه‌های سنتکام، انتقال نیرو به اردن با تصور «عقبه امن» و تحمیل تلفات، عقب‌کشیدن تجهیزات اطلاعاتی و نظامی به نقاط دورتر و حرکت به‌سوی استقرارهای پنهان و زیرزمینی، هزینه سنگین حفظ حضور کم خاصیت آمریکا در پیرامون ایران عاری از تهدید را برای مردم امریکا به همراه داشته است.
🔹
ابتکارهای نیروهای مسلح جمهوری اسلامی ایران، معادله میدان را تغییر داده است؛ پایگاه، باند، آشیانه، هواگرد و هر چیز روی زمین و آب را از جمله ناو های آمریکایی را در معرض ضربه مستمر و مداوم قرار داده است؛ در مقابل، تداوم قدرت آتش ایران و راهبرد شلیک مضاعف، منطق افزایش نیرو و تجهیزات آمریکا را با یک تناقض مواجه کرده است:"افزایش حضور،اهداف بیشتر و تلفات بالاتری ایجاد میکند." و کاهش حضور توام با اصرار به ادامه زورگویی، مردم را علیه آنها بسیج می‌کند.
🔹
همچنین، دستاورد راهبردی را باید در کاهش آزادی عمل آمریکا سنجید؛ اصابت ها به نیروی دریایی آمریکا، تحمیل تلفات در اردن، از هم گسیختگی شناورها پس از پاسخ‌های کوبنده، آسیب‌پذیری، انهدام و به‌ غنیمت‌گرفتن تجهیزات بدون‌سرنشین و افزایش اهداف در دسترس ایران، آمریکا را به سمت پراکندگی، اختفا و «حضور حداقلی» سوق داده است. معیار اصلی تغییر موازنه، صرفاً میزان خسارت نیست؛ میزان آزادی عملی است که از دشمن سلب شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/464219" target="_blank">📅 21:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464218">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a8d6c21a.mp4?token=th7sc5SWt2fp_P8u7iQu-GMDrSfb2ObS-H7ySHN00iu3_cqO1IWKMnjikk3F40qV83wCrfUsQ203lRrPBFAx4VqdJK3wnBDLTNubZdFzPoZbL--sEUj6knQA_rymcH7YVol4vQAbON9GpRyLa1SgvrV9H3k0TG3BbVFHRV0efiZiB4xlrnMzwztHHlcu4wdAv_qDKyzPTsw5pXj5NPUXRlt3FQ1o4q3FoNexyhI2MJ6C1SqLmulrxx0zjL99Lq9-UfY6ik4H_i9N9-FMfwcHuq9JyVhEanYNhx53Qc-c3lYI6Bte7ksHo1DSSC3yvc5nLzj-WREISZ7CtSr-HmwQWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a8d6c21a.mp4?token=th7sc5SWt2fp_P8u7iQu-GMDrSfb2ObS-H7ySHN00iu3_cqO1IWKMnjikk3F40qV83wCrfUsQ203lRrPBFAx4VqdJK3wnBDLTNubZdFzPoZbL--sEUj6knQA_rymcH7YVol4vQAbON9GpRyLa1SgvrV9H3k0TG3BbVFHRV0efiZiB4xlrnMzwztHHlcu4wdAv_qDKyzPTsw5pXj5NPUXRlt3FQ1o4q3FoNexyhI2MJ6C1SqLmulrxx0zjL99Lq9-UfY6ik4H_i9N9-FMfwcHuq9JyVhEanYNhx53Qc-c3lYI6Bte7ksHo1DSSC3yvc5nLzj-WREISZ7CtSr-HmwQWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عددهایی که این روزها از آمریکا تا اروپا شوکه‌کننده شده‌اند
@Farsna</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farsna/464218" target="_blank">📅 21:03 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464217">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4a681fb1c.mp4?token=P8aa0n43dopyZqHfkoEIDgLl30xjS07Kk-PlhxZr1_JsMMmdzE9rDRT0weTDXHVLOKeW_zhcmbrJe07-bxsi88R0dPpj7RuX5Nsa95ruccdbdZ6vQS33ZlO5Jj9Vvvbkt5aaYtcpBiclF7exl1M2sahekVB6iyG-9woHBOABOepxzHjo6o-debDAfvPRTZXWwZl3fl_9Ij21xt618Y6-5CR3oMchojOpnD3wBi7067KCN63kFlV14wERRfse_MxTI4cDSEkSc1I9nY6o6MpnZt54rPZqovWpmQcw0pY5IivvQgdlndKOWQcVORW6YkmcZGfp6lvaifUWWZwlPkvvJZWpVtoYdxoJsouVDuqEwdmWYeiqohBoI2ZStDXQcarWPg8w0u52AemjagN2g0fy-OJCWHgI3HQvnEZlKBsN777mm24jpSmES2yhnaeVhd-mTC9ZE3_6edcP8FGUKtW_MuUMwkKbhX3V35WG_3qnu5tfQzp1hoUOOAC81g6aMdHZmHa-P4Hzgx6Jyqo7Qca4nF8AL09RI791d0g2MuXzhULrJX-NC2eiCVnOp7uPZ5rO7_N8SLIOVYjInoaaUmTWO-rkddRdpafejZgRSHA9UBIFVDRTgEvhoUklgBhZLJ_E7uMyRO9xioAnGGNfFQwtJ005siYqJtxBZzAvXASTIIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4a681fb1c.mp4?token=P8aa0n43dopyZqHfkoEIDgLl30xjS07Kk-PlhxZr1_JsMMmdzE9rDRT0weTDXHVLOKeW_zhcmbrJe07-bxsi88R0dPpj7RuX5Nsa95ruccdbdZ6vQS33ZlO5Jj9Vvvbkt5aaYtcpBiclF7exl1M2sahekVB6iyG-9woHBOABOepxzHjo6o-debDAfvPRTZXWwZl3fl_9Ij21xt618Y6-5CR3oMchojOpnD3wBi7067KCN63kFlV14wERRfse_MxTI4cDSEkSc1I9nY6o6MpnZt54rPZqovWpmQcw0pY5IivvQgdlndKOWQcVORW6YkmcZGfp6lvaifUWWZwlPkvvJZWpVtoYdxoJsouVDuqEwdmWYeiqohBoI2ZStDXQcarWPg8w0u52AemjagN2g0fy-OJCWHgI3HQvnEZlKBsN777mm24jpSmES2yhnaeVhd-mTC9ZE3_6edcP8FGUKtW_MuUMwkKbhX3V35WG_3qnu5tfQzp1hoUOOAC81g6aMdHZmHa-P4Hzgx6Jyqo7Qca4nF8AL09RI791d0g2MuXzhULrJX-NC2eiCVnOp7uPZ5rO7_N8SLIOVYjInoaaUmTWO-rkddRdpafejZgRSHA9UBIFVDRTgEvhoUklgBhZLJ_E7uMyRO9xioAnGGNfFQwtJ005siYqJtxBZzAvXASTIIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هفتهٔ دفاع مقدس امسال آمد؛ اما جای او میان این همه خاطره خالی‌ست
@Farsna</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/farsna/464217" target="_blank">📅 20:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464216">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea3a76081.mp4?token=C74JpNKRl547hK9EqbbVcZ4b3o-ft63qVVXDIBnRcbYUEpB1rTbjoCgz9Ya3qgPKgmVwWKuIuNLoYZS8pvR2QILiVqZSiOR1iT_zj7YDJEXN5jfIHLdU-SsqgAqize9CFWRj9nch-yweIN-8Y753a9v6hDJA3Igs8lA7_2w58XMmkwP7tWSN48AqFODiZxbQOSR5Fte9N_WLICuIYO6NWGJl9eYv0HM7CpU9NhPK7m9W82bhVwPdcWbq6SdEU7PYfdAyunvgVbIsnvZviN-B0yo3dH_nZiyqq2YfIeadMUHj201rnOQuX4rG04B_Y0LIbeDLk3-Os09-uNDjEBcy2YgqsPDn4nXrZ1h33xVNXCIwN-G2iCFDKg6G4Cf2On6GxP1mMI3KAWPNfp06wURmLBC29yRpg_-YgB2o1dgdc3tkrUbLbeQ4qwuMwGivnqmlTYhO008uYkxZ2JEMXdd9-XGBb5W0X07KCGlS0dE2gmKNBIQWqWodpJLZtESwo4FzJILPtlPYxERRA3G7hHkXQfmosPiixXBLSXo36nGFtkh0Bfg7pDh5guZpw4W87K-TFlZW3Mhp0QJ2Zm6RgjsD3x97gSlucM9BnESebXPI-L4DMEH5g7cCQ83_xYJ1Nhf9-LL_SOsnyhnbvpTMNI7G0uBFTxPExBML4PnGdcPkI-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea3a76081.mp4?token=C74JpNKRl547hK9EqbbVcZ4b3o-ft63qVVXDIBnRcbYUEpB1rTbjoCgz9Ya3qgPKgmVwWKuIuNLoYZS8pvR2QILiVqZSiOR1iT_zj7YDJEXN5jfIHLdU-SsqgAqize9CFWRj9nch-yweIN-8Y753a9v6hDJA3Igs8lA7_2w58XMmkwP7tWSN48AqFODiZxbQOSR5Fte9N_WLICuIYO6NWGJl9eYv0HM7CpU9NhPK7m9W82bhVwPdcWbq6SdEU7PYfdAyunvgVbIsnvZviN-B0yo3dH_nZiyqq2YfIeadMUHj201rnOQuX4rG04B_Y0LIbeDLk3-Os09-uNDjEBcy2YgqsPDn4nXrZ1h33xVNXCIwN-G2iCFDKg6G4Cf2On6GxP1mMI3KAWPNfp06wURmLBC29yRpg_-YgB2o1dgdc3tkrUbLbeQ4qwuMwGivnqmlTYhO008uYkxZ2JEMXdd9-XGBb5W0X07KCGlS0dE2gmKNBIQWqWodpJLZtESwo4FzJILPtlPYxERRA3G7hHkXQfmosPiixXBLSXo36nGFtkh0Bfg7pDh5guZpw4W87K-TFlZW3Mhp0QJ2Zm6RgjsD3x97gSlucM9BnESebXPI-L4DMEH5g7cCQ83_xYJ1Nhf9-LL_SOsnyhnbvpTMNI7G0uBFTxPExBML4PnGdcPkI-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم به سخنرانی رئیس‌جمهور در سازمان ملل چه نمره‌ای دادند؟
@Farsna</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farsna/464216" target="_blank">📅 20:57 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464215">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1585d33210.mp4?token=qZvA_RSpOLoinTBvP31_44zkjCczfMD2bOIKq8lhmjlRu5T8xu8CyWbaXgZXM4l9vAECCQBNS6d9xvHpNNgLuEfR8k9-cqxmPTN_GpUlnPd7OkfzXOC4FL6Zku5fCB-ICoFo7L4O1_GyORFIzdBIRBXQ0Tcppa8yK6_dHGxq2kiTo7I2Z4Rn6abyyBWT0h1__vgWqCaE8xJJfS_FR8D6umsjV64iN8iC3y102pGoLUDODmO3ykU3A0q8r0x7OSxF9EbR6uZNNIM5EZAw-h8TkyKWUmqyg8dkdqjf9nSXHRfZhbfPxpo6okTYeTRQgGz-Q7IXi1DN8vp50bHgsTOdr2LYfjGyocN2kKVnw6ZjqSa4hGl4nZWUyp1LZP3nmOp-0sGcdW46EoDMOigdlWxILRx-JidMxb7OCDwLGvbCukW7qIGAb2BIuRmz-6aCtS2OsE5wnL_fyJv6n_Wdr5vBHgo74w_lmUvDiDrgz7T2fmFAKg210_HxpAyjyKgtCXJPfs0X2XI_ZewH4bsIs-R0ItwdjDDETKcMIeTNZFQwQj3qVspV_cj1CX6rOKRM5WZVv6KEQtWdnj_RU66mUE7f5uDMV2CL9P0Xxcr4M03rdCBZRnC_u-xnqeGqvou7WvCmHeclLzHMohGgQOfLfCJIf6LAuWXhLrtA4SLnOvNNgC8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1585d33210.mp4?token=qZvA_RSpOLoinTBvP31_44zkjCczfMD2bOIKq8lhmjlRu5T8xu8CyWbaXgZXM4l9vAECCQBNS6d9xvHpNNgLuEfR8k9-cqxmPTN_GpUlnPd7OkfzXOC4FL6Zku5fCB-ICoFo7L4O1_GyORFIzdBIRBXQ0Tcppa8yK6_dHGxq2kiTo7I2Z4Rn6abyyBWT0h1__vgWqCaE8xJJfS_FR8D6umsjV64iN8iC3y102pGoLUDODmO3ykU3A0q8r0x7OSxF9EbR6uZNNIM5EZAw-h8TkyKWUmqyg8dkdqjf9nSXHRfZhbfPxpo6okTYeTRQgGz-Q7IXi1DN8vp50bHgsTOdr2LYfjGyocN2kKVnw6ZjqSa4hGl4nZWUyp1LZP3nmOp-0sGcdW46EoDMOigdlWxILRx-JidMxb7OCDwLGvbCukW7qIGAb2BIuRmz-6aCtS2OsE5wnL_fyJv6n_Wdr5vBHgo74w_lmUvDiDrgz7T2fmFAKg210_HxpAyjyKgtCXJPfs0X2XI_ZewH4bsIs-R0ItwdjDDETKcMIeTNZFQwQj3qVspV_cj1CX6rOKRM5WZVv6KEQtWdnj_RU66mUE7f5uDMV2CL9P0Xxcr4M03rdCBZRnC_u-xnqeGqvou7WvCmHeclLzHMohGgQOfLfCJIf6LAuWXhLrtA4SLnOvNNgC8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کالای غیرضروری جای کالای اساسی را در واردات گرفت  @Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/464215" target="_blank">📅 20:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464214">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/482f2ca9fb.mp4?token=XysJtAzInpxU8qDyCl7trOH6zhThgeOjlu3ED2r4plQeOzwUBZ_jmKv-5Pq2orfoEJlw76Ola52Ri27yY_wRSfoW436AIH-BCw2J3FzCZswgmmuRlhkTrYhnL-0j5pxR5x-QpEKkbCyuNJ879OvtpSA0aLYoW-5OlDqDU2wM6VbL_wU9lPzAsZXD0AkYsZWEybL3dGbI5YJASGCKmYpV04Es8_iNfZVo-FHhPwAqZYaj2kjB0jmzw5HirjKwwC7IHnPl0Oqeto_Z_Mdoc5fxme8Tk_a6tS4wI-ggOHBtBsC6dHInWjrA_9ybMqZlqdFTs4K0Zwc1mttuh46MpkGxMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/482f2ca9fb.mp4?token=XysJtAzInpxU8qDyCl7trOH6zhThgeOjlu3ED2r4plQeOzwUBZ_jmKv-5Pq2orfoEJlw76Ola52Ri27yY_wRSfoW436AIH-BCw2J3FzCZswgmmuRlhkTrYhnL-0j5pxR5x-QpEKkbCyuNJ879OvtpSA0aLYoW-5OlDqDU2wM6VbL_wU9lPzAsZXD0AkYsZWEybL3dGbI5YJASGCKmYpV04Es8_iNfZVo-FHhPwAqZYaj2kjB0jmzw5HirjKwwC7IHnPl0Oqeto_Z_Mdoc5fxme8Tk_a6tS4wI-ggOHBtBsC6dHInWjrA_9ybMqZlqdFTs4K0Zwc1mttuh46MpkGxMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار عراقچی و وزیر خارجهٔ اردن در حاشیهٔ نشست سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/464214" target="_blank">📅 20:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464213">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEzEOKfxPMOAayS8GglezOXT1MjP_85HJisprBP7aZKx2BuElkmQc-L5raanmKw68vdVqgYuIXuy9ntB1vsIa7Rlr9338ov6r8_me0i2ccXqi9gkKRAQY4CXFa2LAZo5a6_VGlbdkh2vAyzXcx-I31On9PtS26awsXBhBUIPnE6lfGyv_-rurt0Lb-DA9nH1SZy5uS9YRT9X1Ldh41XBb0eLAzxOCK7MelX7HhjIYAuuolQUbkVhVDKHeKvv_fbu6zD_cttq1YGiK5JnmUXG9iFjcascvCRVeTT6skr1C2YJpSp3nYree70EbK3oNKFH53opDeP7BtV0ybLqa2AxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پروازهای ایران به این کشورها برقرار است
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/464213" target="_blank">📅 20:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464212">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmQs0aOijiymgRlmJmO8oIzmWRtSw-BK--Y8_BElGjvYRwBhp9j1tkuhWMh-yeIjoabofp3NIqZPUb3-TkhhNwrtz7xbaoMgMP__C2n1FbyO7g8DN2W9VifNohlYELDy6r4L-nUUUWaeXHRm6A7iTHk0c3XgbbmJE3WtBXncmw32y9-sAbMBqPMZ69m3ZbL3uJ4b0-RZmof0pwj65kUbiCX6Qc7UjhJCin6RvNLauCLztFgt7axb-45NovtoEOyaJ8kRqywa7hpBYVs8Uj_VmZKNHx-APuVk5OCFCh--yctqnZyniSM2J2DInxDoDlxKaRlCJdfqJixwNoFRC0CJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف یقهٔ بسنت را رها نمی‌کند: رکورد زدن بازدهٔ اوراق قرضه مبارک!
🔹
قالیباف در واکنش به رکوردشکنی نرخ بازده اوراق قرضهٔ آمریکا در حساب کاربری خود نوشت: «آمریکا! سود ۵.۱ درصدی اوراق قرضه ۱۰ ساله‌ات مبارک! ماشاءالله.
تازه باید جشن هم بگیرید، چون برای ۲ سال آینده، اوضاع از این هم بدتر خواهد شد.
🔹
دلتان می‌خواست ایران را به عقب و به دههٔ ۱۹۷۰ میلادی برگردانید؟ کسی به شما نگفته بود که درافتادن با ایران، کار آماتورها نیست؟
🔹
حالا ما خود شما را به وضعیت دههٔ ۱۹۷۰ برمی‌گردانیم؛ با همان نرخ‌های بهره‌ی بالا، قیمت‌های سرسام‌آور بنزین، کمبود گازوئیل و البته شلوارهای دمپاگشاد! از این نوستالژی حسابی لذت ببرید!»
@Farsna</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/464212" target="_blank">📅 20:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464205">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZpvIaE4rvQLtPR1HOoL2NXRE9uaMF9LAn4-G1w4a_01Kb5V_Un9INZVDlr81MkGRlY6U89wJNuHzUk_zyQ_zFWSw2V0YWzGSqnp-oGj5f-0gVAqvH7xSrAkiRQBhmixo5F1MAZD2im-q2z7B7rk1_LfFRZb-e796HTcdSDbyAmCHs8zUAxP8SXe7WFROMrt8UzLMCIbKhcLKaopALQ9Oble9RcS7EYAQJRX3LdAla-t2a9nlD95hS7yLJ55osWourLl3GfPlRmHZz1_-b_cVQgwRYcsWPJf2jHHRNHBVlwaT8ki6-jbYs_69LigDD6CT8fXQMqgZPQUVceq7DLVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6Gd173Gg2lMBIx1_wI0Yn5PG5gHhfQF00nc811PHFmDgN23Ii-hIfWGdtVPL-YE9cZtUyk4H6eJ5ycXzgTEdg-fnJnz-NlJBM_rXtiaBWc6ggIZG2eT3Ei4Vne647DLeDxAoo_5m-l_LPY3flpSaI4HD8sKVurBqfPGZbqLgsVS3cp-FyPdbgpM05EUk4dLWCiOH0NXxox7Bvzxuv2hC9LmTHJ9cOZrntPGtK1jjG-4imgqBmB8fZVJlr0QiCtxy3XLKmJMwkzMFsTuEwtpPJeM6tIrLpfIpkV1X4vphtPbqUD7IsCCIWhiP2d5q-f_OTDT3Plmk9HxWDUC6_C8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V5ZQu8Duolu2CSbCXcqDYwng_tzEs2mait92hLWIZW8urnCQ8D3ImtzpCy0kEPPLoCaohOp65lXr4_KqeJEf69VBSwO9ANgpdrbI-bCUgKux64Db7eZSGQElVouwJJ8604KkkMB7cgXfbfNJQA9JmHSfRkuh8j3gDfeFtc_1aCS-XoNwKX4QBbS8Aa67Lq0wkQibBt28U6Gq1lC7pC7KXg1jNKhaasl-EHtJtNF1uLRyl8U_5zgCzoALjuZckb3miC-oYJRbWI5Gl0VSSHfdC05jJyxB86q7V9oICEWI_wQQ-9M3d9lzqxBjq08t2pfvASABP6Fhz3q3QiFgKWAikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DcYmAdp7EApUFaHTuFQGmFkFLPv34DvSEvTk-z0H9sCNk4KBv4F6U4Y8CHccTAO9H0GUazEYCbAQk5okRcfKpaHH7uzxYJRyafLIWIhEeu9BB_q9UcCJAAxLtU0h4n8FZ_3hBL_e1UMYYwVd75fKkFuER-k7ZZsXXUen6L9hiU7hx3jojqQHR7oz2-X7TIHXHPefniJtXF5cCDV9P16vTm91W_eJ_0xt_S8bvCRYGv_u76CaJfnaRS9JbVlSqxz-TcOD34D1QTd7Cb1bTb1NgYN9fiPhmXDGgi74feSUiYe23Qz8nWB2YdtP05NJWQCjXLkCq_O8bxV8pYEwdVcCOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CBX315nTjkYsqLjf9mkqpcoPEN29_x9ubTi9okbi7_ZbPSFMc_b18Gb4UPfI5AQvTETHUUo0A0QXekiX4tjks22kaM-R3dr_4S5A0yEVM9FTT9vA0htkZiIybH5tXuKiOX1wqV2t1uslxkzi0_fgfKZ0cM5md2nPIUr3bwEVDQh_rELpYYqrEI17BdmXug4lfzPTDygTK2n6jY85GS3JNTN2klIRQH7Z1JG5BQriCpFDUZeYltWmI5eYNochujKGuaXVcpsSm8OssoAEUqGosam0Y1Fe6K8wtZtANV0excSqcgAVtWBuD6fVI_6UsUPkib44LNVK1oVa1tQ0uT7z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/awiSqefUG_gfEXxgS37KVsF-hWOZuY1oUYLqdFOM6mfCgGOJJF40lC6SENA4GKrsxQr_P2Do5yV2hrK-24za4P4rcoWyN5nW8I6rCvey_gCe_KjhpV4fO-svLuxytV5SPxSkofrmjQGtE9I_MFm5CFZu3PL0SAJN-Ky4m70IGNsnQiruwvQPuTaP2I6AYKNEga3UBABELfNfv7fPXj3IpbJTijcaqu44POwGPyF8O1W5aj0oBQUj-4ZSC0SekaiL-90TeLCEWR4oh91QpVYilCtMD0VtUyvCEYY0hZqFXbFBVbFvZMlVJtDfSSTdIw9UScnHKYN1NRWPRqHvyxuW7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DAo7A62C2cFQwjGASYy7qq4B7Ve5r356VAlRr2VTLAWP5DV5U-yzw5Xc-9oAH2Y__Ynr-70L4MjlsoQMsNkfHwF5-Y6MLdSX42DNO3WQep2lhh-kixRsWjqepishe0uVh265AHJ5m8JaRM_w9xNWyfrR89j7OdYpFklIZnSx9xHPvuOQqRqzhaJWTC9cooVYrjrheqJYyfGJHCCCDWiKDTKHb6ne0dwpz9gvPCodQAcjp_JflAnZSSMYcP_Bmq62BFwV5H40MAEDyJ9_SHsMfmu9wD0iYxA36_fZ6xrUs-W2cGWO9ktW2hTtOtMZvHpHZD4XWVTJtGTtJpAdlZx1Yw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
غبارروبی مزار شهدای دفاع مقدس در اهواز
عکس:
محمد‌ آهنگر
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/464205" target="_blank">📅 20:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464204">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f1971f1.mp4?token=UNW7sQFoF0ZYFK2BTJ_9gymzAGalzx62cRHy37uVpexfN_pAShHzuWWQZeqhK-li1kRw6-nfHoJhyzllrzAoYNMf-wvJsu7xYZz_CR3L6ayDr7jk-w0oeCu-ZbY4qSUBJHz3Be40k_lLUOb9_kS8LeTSaqYbDMeBP5lFN6jgF0airMxTLsBIybHQQw4be3RI6qCf8_YCCuKtYCIRO4sXxB3IE-TaTvcV4SRRIq0qEhAK-s-R3_Qe4oX0An3Yjz5b4SM_4mjiSWKriOlfP91HRj1guuDxS_ZRk_wl8V17FYFdRxLdI8SsF7L_zAyf2czI9SxglAMQMAMxoIlsPag5FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f1971f1.mp4?token=UNW7sQFoF0ZYFK2BTJ_9gymzAGalzx62cRHy37uVpexfN_pAShHzuWWQZeqhK-li1kRw6-nfHoJhyzllrzAoYNMf-wvJsu7xYZz_CR3L6ayDr7jk-w0oeCu-ZbY4qSUBJHz3Be40k_lLUOb9_kS8LeTSaqYbDMeBP5lFN6jgF0airMxTLsBIybHQQw4be3RI6qCf8_YCCuKtYCIRO4sXxB3IE-TaTvcV4SRRIq0qEhAK-s-R3_Qe4oX0An3Yjz5b4SM_4mjiSWKriOlfP91HRj1guuDxS_ZRk_wl8V17FYFdRxLdI8SsF7L_zAyf2czI9SxglAMQMAMxoIlsPag5FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار عراقچی و وزیر خارجهٔ اردن در حاشیهٔ نشست سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464204" target="_blank">📅 19:51 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464200">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhucCpZ7AkgoN2FtGcGYJnk5i05PML8qhwrl_5GYSyUyubIwVyWUmRtX3n4KHez5KHypTOmR5oLNybLvRv0gNi9laVv1S2UkanF6EBopCQdBjbyxdWKR2adedxoX_GzESpigub7PYOB8d--imKvdva0P1OpxIqCWArBipADFfrTtR9iGyeb50XIudg3ljTVqmFkfaRAOdYTtgaTW9RVWjRn1W8uTZBMKpDsb0FBb8u5UvWCMp8immk17FpxMhzBiX40LAjYGRSY7Hq2FFc1QGCxlpv1WUQgNUvGmaM-_mKoA862SbDG5tdDuxm7hXXWlvfkA0yn8mmcvB3JSoVPSlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XfryDbfqhFZoz48TzJTbxVoC-oA0Ma_at9yBMXCBwL34ar_RFJG7e5i0c5kBdLul9i9_ivtMSl2mZb4wjmxcG0Jxb29lSScaunqPUs-l47Ztm514BOefX8cisag7Tvt6v3T1Ky1fbE8fzPkep528-wyZ_Pm_K-UE4oVlUyAM2LfdaeyKU6xFlFpmyuObLLoT2Nn8CZh6S4wnvo_trdnIhBlVKHi_9XWSgTuggyAzc68LD8VuI3Eb44tLM-3TrktTKd_9jPokv6U-ln9zcQn7BS4JVc4TDW01cntffbjfBo_uCfTsYq61FcNMY_2Dzx9cOCu8xIOP-vvNO_G3yS4RkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X2WXZyFRWnJYvrrQiNoqDAn39eJ4ImPQDIqBuQMHPiPiA2cbx0U-Gnph2z7pmLNlZYTQaOJJXlyCmS6Ao-exb7ZZVi4u27Sdfe3qKWsyo50Hzs_wUo1RrthTZXOGp1L6B9hMMM03eoiVRxyCNUC0LEP7rU1tZUfV0wRjRJCmSIm0LTwIgKRYQnyWSDpqUe0Jv_dGicI2iRAqEmlt5lsWPbt8ycwzT1IVV-eN5W4ecDBKS-z5cNf6TuvjBmSMjU0gK-DnY7HYIQL0zhS_0POO0BBePm0dzSfGonO26r27qNXMWy_PyMzhw844lZn536hOno44xggjqv0Kl3sycuWLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fm3irtmvbAbl5PE5ILMm1gMU7CZvw39bODmoER4gAyZIkbmwJdqYCRC4GjT25IdcMA7Q162F0vRZc362EokYGkMNrjeIo5G5u2Z8luLoIIApMk0HlESXYbOTpkoD_aUazrRonka5Y0cBz01959_yfdLqOf-D8nLoww4smMAij2uqZNd_o25nnb_4c1XI_6Cw0wSWs3RbNqDxfEDLrcU2wXQrrEDdP2ZzUcUWS6vfkZJsL-XEdQNfy4FSeKGEoK4oOYdHxZZDRInc8q73zdczZr0MKL952bRR0yvvxwEi2Q3vm9WgkVURN9sP6chOnasC0vqQwrh_kFtbccKmGNdfKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/464200" target="_blank">📅 19:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464199">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AdbJU26H4zKzITXruD5-Kg5dRqyp6FJGMOYEZYu9r_zhmoBoJ0kAqXX5vecrKVnkpDXsYgBXZ6MJmsXoYTP7Ca7b4_mkdf5aFpYvI_iNrtI9pJYd_Hlun40sme4DTbDKWyzbn41efnu3faZwybh-hJc99qrDJ4Ij8Z1rCAsSb1e8t4RrRvXW1Sb-kRjwlaJoeEtGU9--FrxsjgzRkyGHfjMoK391mZ3sijXO916G6EEDEemOO5DFiyq-3IaRE7RC8WNyWUOF89mkt5kdeGAl02RkTO4m7jRt0MoJFImTLHLYSIgXQmJt5kopKcBLpJ2QN-_z1UhSYgQq9aIqCXCqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران باز هم مغلوب گربه سیاهش شد
⚽️
ازبکستان ۳ - ۱ ایران
@Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464199" target="_blank">📅 19:34 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464198">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sxj8lM1DqOxrfcXL5zBCWUfsHmE0LXZkusI8D8hYK790osSXFx5EOiTEEf1GoHVVt9N9j0tj_5DgbJX_Jems57kLJZZ9T8KB5qi9Cpn8D6964TeyD67bIdTi-J22cfGA22U5McCBEZhilGz6FBcP477Uou7VR_PSOoc039nPwzziUESDmQGhOJ7nCdU6_G3cy5KyXyikUhWVT6ZryNLao9Iso68LfVGV7iaLmrkxXh2Rl-vL9DDYaqMJXIhHukmZ64oTmNOUrbiveI2W3ZaWmlTvua37CGpu3Jgl_S8SEVuX8hbTb9ZNpb6UN7W76JUuST0MwNiacjFKrly-RUYi0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقچی در دیدار با همتای پاکستانی: نقض تفاهم اسلام‌آباد از سوی آمریکا سبب تشدید ناامنی و تنش در منطقه شد و آمریکا مسئول تداوم پیامدهای این وضعیت است
.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/464198" target="_blank">📅 19:31 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464197">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=c6Z06_I11WzfdGoh1MBVpjzLy-LaMZCmSINzTgB3LlR0ayI9lXfxHX1aRYOUjx9YtuJ4-Pd3WZUbte-EUyBQUDDLieVKfyCNxnBX049b-fxPRSABse87Kh5-zdKKpC3NClDGxKSgzbikUtiSede20q33HQIo_1Be5jLSGGMCdIctpxrMazFLoe2RtNC6andiWJc5C15TjH_6hnpYd1lXHePP_RfMvORFoQvnrkUGLI4wPKYPFyKhu2Q5ZoopTNeawuNME-eXp88HQ_he_M8xsWgAnqoxUJQ639h4jJaIrnOmZ24JWa06pfITkgas1kVau605YTvGcD1dZPpIQB4Ouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/deaf5a7be3.mp4?token=c6Z06_I11WzfdGoh1MBVpjzLy-LaMZCmSINzTgB3LlR0ayI9lXfxHX1aRYOUjx9YtuJ4-Pd3WZUbte-EUyBQUDDLieVKfyCNxnBX049b-fxPRSABse87Kh5-zdKKpC3NClDGxKSgzbikUtiSede20q33HQIo_1Be5jLSGGMCdIctpxrMazFLoe2RtNC6andiWJc5C15TjH_6hnpYd1lXHePP_RfMvORFoQvnrkUGLI4wPKYPFyKhu2Q5ZoopTNeawuNME-eXp88HQ_he_M8xsWgAnqoxUJQ639h4jJaIrnOmZ24JWa06pfITkgas1kVau605YTvGcD1dZPpIQB4Ouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دیدار و گفتگوی پزشکیان با نخست وزیر پاکستان  @Farsna</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/farsna/464197" target="_blank">📅 19:26 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464196">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p2-bijeb5NXyCrEZK_6expdgMSE7VwCN7PQslYmrcmatJ2OACkb4S_l6uE6nBqIXWSnvwHpsuh78jzKtL_mws07dpCJqHnlRKIICH7FeAIeiJqZ1CSCnSB14k_L3kxG_u6vKto_wcxteB80NRsMxwinS3nPbvuvvbLPxAmzLiNA__MHhHfJe1gWb9BTHd8JKB_PZ8Gdd-KBMHqSpet2ZLm4k2AHsLiQX68UT4IppDt56tgAg50YJfuqg4rGC68eZzpHM8NlWc0_OGjm8wpRuLuAXvaOnucLZ6qOcNOyiYHeomk82oaH0eSo_I8jqobmjWJ8Pp8LBPN3_kKnM1c_pqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو منزوی‌تر از همیشه در سازمان ملل
🔹
فضای سخنرانی‌های انجام‌شده در مجمع عمومی سازمان ملل متحد نشان می‌دهد که استقبالی سردتر از همیشه در انتظار نتانیاهو خواهد بود.
🔹
رهبران جهان در سخنرانی‌های خودشان در مجمع عمومی سازمان ملل حتی پیش از آن‌که هواپیمای نتانیاهو به زمین بنشیند انتقادهای علنی تندی را نثار رژیم صهیونیستی کرده‌اند.
🔹
شهردار نیویورک نیز پیش‌تر او را به بازداشت تهدید کرده بود. علاوه بر این نتایج نظرسنجی‌ها نشان می‌دهد نتانیاهو اکنون دوستان کمتری در هر دو حزب سیاسی در واشنگتن دارد.
🔹
۲ مقام آمریکایی که خواستند نامشان فاش نشود به وال‌استریت‌ژورنال گفته‌اند ترامپ و دوست دیرینه نتانیاهو هم هیچ برنامه‌ای برای دیدار با او ندارد.
🔹
حتی اگر نتانیاهو بخواهد این سفر را رویدادی عادی نشان دهد، صرفِ حضور او در این نشست، تنوع و گستردگی مخالفانش را در کشوری که اسرائیل بیشترین حساب را روی آن باز کرده است، برملا می‌سازد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/464196" target="_blank">📅 19:23 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464195">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/119444cb53.mp4?token=EBAhBwoe7L6kttz2CdXp98OWj18DQeHw-zqvo3qXSXWm5iC_kfpDR_3wyRzidUdr4ct9_SawDIv-IQaroLC8nguYUo1M_O7FWiQWgd1vHmGGXz-fEt801sodI3y04A13kmMNQVwxEUy3K-E63qVHj1cZk0IbMW7gEbpF6vythpaLJfaUUYVOrLx6v3v0ORv8F4ToTemEZftes7bH0LnB4M4nzZx1X-HUd89EsloBw95LSm1rj-MQtPA7eKYOTUBWQEh01yOAE8KhDp-FDLmG9AkDi-E75RMQR8hl_9eyTKZTeJzCCrebx_N5fnWaR9fKoJvm_HQxdXqy_wjjDcmxQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/119444cb53.mp4?token=EBAhBwoe7L6kttz2CdXp98OWj18DQeHw-zqvo3qXSXWm5iC_kfpDR_3wyRzidUdr4ct9_SawDIv-IQaroLC8nguYUo1M_O7FWiQWgd1vHmGGXz-fEt801sodI3y04A13kmMNQVwxEUy3K-E63qVHj1cZk0IbMW7gEbpF6vythpaLJfaUUYVOrLx6v3v0ORv8F4ToTemEZftes7bH0LnB4M4nzZx1X-HUd89EsloBw95LSm1rj-MQtPA7eKYOTUBWQEh01yOAE8KhDp-FDLmG9AkDi-E75RMQR8hl_9eyTKZTeJzCCrebx_N5fnWaR9fKoJvm_HQxdXqy_wjjDcmxQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل دوم برای ازبکستان از روی نقطهٔ پنالتی
⚽️
ازبکستان ۲ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/farsna/464195" target="_blank">📅 19:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464194">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e7c9509a2.mp4?token=jbSO1EhFSk6WraeqbrjNO8_WdGLfGwSzWxQMWjJuxUX3VDZprHRCMIQ1VsmIG3tSR30p8E3MlsJcIadcjVPo4LioswQKxDsgXkNBh340L3_lT4h7Gc_fzuE1m_t3vLFEBL4FBkPLl1X19ImdWQOumRfPwSMD6-fU7mYx7NOQeoEFIa6NoGX8NOFpHJnRafaylP3sh8xq_aolkIc2zYpmkNnFAKqbHNF6Ro6J_dz9SeAVBdl1c-LO9Y-rkSW1jDiG5MCC1Wj_JYgpK6ZkIABGa-VJrDTj8cF1VlRuTgTPxBoacvnrjVdbYqLU2BAt8B9odJuiMTLqPc6a89rPZO_jVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e7c9509a2.mp4?token=jbSO1EhFSk6WraeqbrjNO8_WdGLfGwSzWxQMWjJuxUX3VDZprHRCMIQ1VsmIG3tSR30p8E3MlsJcIadcjVPo4LioswQKxDsgXkNBh340L3_lT4h7Gc_fzuE1m_t3vLFEBL4FBkPLl1X19ImdWQOumRfPwSMD6-fU7mYx7NOQeoEFIa6NoGX8NOFpHJnRafaylP3sh8xq_aolkIc2zYpmkNnFAKqbHNF6Ro6J_dz9SeAVBdl1c-LO9Y-rkSW1jDiG5MCC1Wj_JYgpK6ZkIABGa-VJrDTj8cF1VlRuTgTPxBoacvnrjVdbYqLU2BAt8B9odJuiMTLqPc6a89rPZO_jVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار پزشکیان و نخست‌وزیر هلند در حاشیهٔ مجمع عمومی سازمان ملل  @Farsna</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/464194" target="_blank">📅 19:04 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464192">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be55119aec.mp4?token=R2zsemhst-2Q7BWuh2UuJAAMOYUW1r-1s9Ijf2P5k-3Z9rLVhCZfNYM3zrCerFhLDMyxOTxTQPz-6jsfqfglqc4lQK-1oTKXD3nqnKvy9YW11tT8r3EX7N2rKSs8ikaC4kUeOdvDDx8EnKb6BNx_Yf23XXUL8y8xwvlZwUftAGp7fzupzSzin7EywWJz16ajFhz5rH-xGZLo4lQskQlSikf9sTcMIzkok77AEKT7z2D6a8FLTSf_85bVQBBUKIhOOUxu_7yq_K3hkaeaH5muj7DC716kbiGycAnBmgzfN1fM-9O1iPKLGIxelJUBAG4RzgGP-fRLBqe0ROAqubgMuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be55119aec.mp4?token=R2zsemhst-2Q7BWuh2UuJAAMOYUW1r-1s9Ijf2P5k-3Z9rLVhCZfNYM3zrCerFhLDMyxOTxTQPz-6jsfqfglqc4lQK-1oTKXD3nqnKvy9YW11tT8r3EX7N2rKSs8ikaC4kUeOdvDDx8EnKb6BNx_Yf23XXUL8y8xwvlZwUftAGp7fzupzSzin7EywWJz16ajFhz5rH-xGZLo4lQskQlSikf9sTcMIzkok77AEKT7z2D6a8FLTSf_85bVQBBUKIhOOUxu_7yq_K3hkaeaH5muj7DC716kbiGycAnBmgzfN1fM-9O1iPKLGIxelJUBAG4RzgGP-fRLBqe0ROAqubgMuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور چین به کاخ سفید  @Farsna</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farsna/464192" target="_blank">📅 18:59 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464190">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ycwu1R5x-c0G8WuLJIRDrQUkZ2RN9VDd5zeIpbEbtPviU-Sqi5iWz4675O84n2sVgXjm0Sl-IerwWqJq2LMIvtjaKXpxwAlGTXh6EOzdsR0byicXTELYH2ilm2BbOAB5JklxyLeBbOd_gtsaTkRJK81R30vZf5FhMig39q3cdbTxenhRWkVGxeP-6ABdYjF1e9bFvCjr0HcVMtPAAxeRAzn9NJWKibdewlrxTM-RRnVhL3-rP8P-xWw_5UkLNJj5LlBdL6_pMf-TaQZBjZ8NILzvzbMn0aB18Ep1KrWjNaMY6CUIehZna3Eej7eqRlMM060kWrg_BGcWlmf75_RXaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c-zSXD5MsbwmWp2qU-p5GYgvLbuCY3YqWE4bh4x4Jbzwwllz3GF1zG-2k5kAFUILISEec5DKvAQiNtGv-IbxxLJYjaZ6JEQpHV2wjdUIjUCfTzPzmMizQuddYyW6JCbCLtQ1DuI3QuwiGAVUrgYH9hTcQj9TVFJRVQLDQXL05WT9Al4J2E91JTbdiVFr7h5vQ-8A-PjhxgMEiRW3GifjDiA8dVwGni9xm3vB6N6slI2vb7XE7mpKzeNCpR162wON194prDaNIS90kx6N1NGECmN50JK7OeGOp2wBUKtJYyvjUpMfgKxSHfL7-4HLceAjXUKYV3n9Q85D52QmW0dMAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حضور قالیباف در منزل شهیدان خادمی و نصیرزاده
@Farsna</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/farsna/464190" target="_blank">📅 18:52 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464189">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f3c3356fb.mp4?token=DIJLMP4qTTW6DEhAOFauQUFXOZr-1GoYzrAHCnls6MhigosTlNYeVEhitpWRkGJWg7pLFaAST72Nd06igGKTEd8EFL3S712OAsq6cll3DbQj28pdv-Tdd1uYA3vGpQsZItO6M09m_A8474kgDF7oIxtduexDRgXo_-MUukCbGatCrzxEzu9kJIKagTb9nE1kIvqy-NSO8Wkq9gKAQ-wERbuTsVJb9-0aTr9zbijjoProDBce7w2EyCnDoujmfB_1pjaLxpOcqo2WcbhRYV1KK26XWJhR07hbBNj_dj-m4aXoKykKaQLKBTMJF9ih9_k7sq-CpEuBNLjUjlWa0XYr2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f3c3356fb.mp4?token=DIJLMP4qTTW6DEhAOFauQUFXOZr-1GoYzrAHCnls6MhigosTlNYeVEhitpWRkGJWg7pLFaAST72Nd06igGKTEd8EFL3S712OAsq6cll3DbQj28pdv-Tdd1uYA3vGpQsZItO6M09m_A8474kgDF7oIxtduexDRgXo_-MUukCbGatCrzxEzu9kJIKagTb9nE1kIvqy-NSO8Wkq9gKAQ-wERbuTsVJb9-0aTr9zbijjoProDBce7w2EyCnDoujmfB_1pjaLxpOcqo2WcbhRYV1KK26XWJhR07hbBNj_dj-m4aXoKykKaQLKBTMJF9ih9_k7sq-CpEuBNLjUjlWa0XYr2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گل تساوی توسط رامین رضائیان در دقیقه ۴۹
⚽️
ازبکستان ۱ - ۱ ایران @Farsna</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farsna/464189" target="_blank">📅 18:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464188">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df85455efc.mp4?token=m8quk2lwOkF_rqb9OJTY_V2c8hvSQyQZ-LXSNz65QSojqVcBgRaw0aQ-Vs9qWebdQEqkoMTJ9pBC21R3jM91MXc7Vp_1gdSOdGkxAFyQP7p9CdvlNBOS8T5zX5pdZOSQS3aA-brlVfWNdDB9ab-8eHvu4g09PgH79u9pQc9r6OwB4PO30t_wxwmEoKcvbsbMTCgfBm2vfwOflYmgP2Qk4KR3qBGhj4Odd0hXqQTjMSDH2wnSvZxe6sDXBDCEV_EHgY7aqy2ZwFyvGc6KOe09GsOFHXUxCXGRPXOfLO3LdToXheB3dzdJpLcTqv5APyn-y8d5_zXTCpwOsbk1tCkLLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df85455efc.mp4?token=m8quk2lwOkF_rqb9OJTY_V2c8hvSQyQZ-LXSNz65QSojqVcBgRaw0aQ-Vs9qWebdQEqkoMTJ9pBC21R3jM91MXc7Vp_1gdSOdGkxAFyQP7p9CdvlNBOS8T5zX5pdZOSQS3aA-brlVfWNdDB9ab-8eHvu4g09PgH79u9pQc9r6OwB4PO30t_wxwmEoKcvbsbMTCgfBm2vfwOflYmgP2Qk4KR3qBGhj4Odd0hXqQTjMSDH2wnSvZxe6sDXBDCEV_EHgY7aqy2ZwFyvGc6KOe09GsOFHXUxCXGRPXOfLO3LdToXheB3dzdJpLcTqv5APyn-y8d5_zXTCpwOsbk1tCkLLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج‌صفی سازنده گل شومرودوف در دقیقه ۱۰ شد
⚽️
ازبکستان ۱ - ۰ ایران @Farsna</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/464188" target="_blank">📅 18:44 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464187">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG1bUlHgOtl_W0iTrtESf6U9SbT7UFPDgfNEn-QzeXjgLsgLL1ZKp4LLTOzGsIiE11VvwnY8_WtNvh1EGzYtsW0_oxsm4mWKFTz8JA1CKOL7BtAzppLIMh7B9zjzybX6L-8_3_N48csVqFOpWAqfhcSagyBNRQEl-a1AdEgI-TW3cT01o9lfmJLVrI4XF0Q3zTu0VBO9azPMfQhbOtx99tfI-43Rwff7f6t51ecLIOmmqGfG8EPuUpw2GIKCYrOK4lReuG-A7j6krwwUBUyJSjaDR1Or3DPmOuR8iV5DZQsI3P6odKnDchjwDtpNeZD34texgMeCn2B5CAycdkICTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: عملیات پیش‌دستانهٔ گسترده‌ای علیه نیروهای سعودی در جیزان اجرا کردیم
🔹
سخنگوی نیروهای مسلح یمن: یک عملیات پیش‌دستانهٔ گسترده را با ده‌ها فروند موشک بالستیک و پهپاد علیه تجمع نیروهای سعودی در منطقه «الطوال» در جیزان اجرا کردیم.
🔹
این…</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/farsna/464187" target="_blank">📅 18:36 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464186">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU0nN_e8X-RNpSawdI9M-PGwuynAFNM8jM7mxnl-a3nIRqWO97YulfG25GJMeBn561RZKFWg9woOEhdNoAGuLctGwpsqZflK6OlZei6SFp04OTaBgabK9xzgnVo7SCtA8r-yQD-hzIF36Q3CPhYGt9c_PhPuNy8vugiqhwgYebVHxBb1kBSCub0jDl6weFdAklVKn6uxcWKDPIVIV3qIAGbd96yDa1HTEOjhj8LYo2NMR7MyGOI5eKdYYRQcLvUF4mLSp_qCbavJ3V14nTNUZsz08FsF7QwplEQrJQbnS6IccZrWWZ6rbeWiPWg893TSQ8Mc1NECoIRLJjb5ZHk7cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی نیروهای مسلح یمن: عملیات پیش‌دستانهٔ گسترده‌ای علیه نیروهای سعودی در جیزان اجرا کردیم
🔹
سخنگوی نیروهای مسلح یمن: یک عملیات پیش‌دستانهٔ گسترده را با ده‌ها فروند موشک بالستیک و پهپاد علیه تجمع نیروهای سعودی در منطقه «الطوال» در جیزان اجرا کردیم.
🔹
این عملیات، اتاق‌های عملیات، مراکز فرماندهی و کنترل، انبارهای سلاح و مواضع مهم دیگری را هدف قرار داد.
🔹
مواضع و سکوهای پرتاب موشک در اردوگاه «الدغاغیر» در جیزان را هدف قرار دادیم.
🔹
در این عملیات همچنین چندین پایگاه متعلق به عربستان در منطقه جیزان را هدف قرار دادیم و اصابت‌ها دقیق و مستقیم بود.
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/464186" target="_blank">📅 18:30 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464185">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ha3Bj7eZyyEh7cOrkrtpRJF96aIJF8OniWpmeLKRCftKLdSnwS4PZG8H4Pc3fy-no7pGx4r8FCo6KGtXbL6_ScaQB3npDKBc2o3onCPsCVbaHFaa0Z1W77gZC8vy5NS84Yxqe0D4FNt8In7lHBQZAUcuun3YSMf__phEd51osQWtDMQeQQKBA_D95jKLo5J9ghJkVzuez22X8NOpj01zjPfavaMCunV0ybvdIWDsTzMhsufln4tmW2fUQWOBG_9JQh07Pw7abCbSZcv0s34xfnZLH7I9-DZnkUdnLpcJ4V2NrFoJEhyfUMp0p0oc5CUzw7itX53jqYlLiNYN8vk6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان برنامه‌وبودجه: منابع ارزی موردنیاز برای تامین دارو از همان ابتدا توسط بانک مرکزی کنار گذاشته شده و ارز دارو همچنان ترجیحی است
.
@Farsna</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/farsna/464185" target="_blank">📅 18:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464184">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ded4f96c1a.mp4?token=LoxJDMbx8m7pCwPaB4mYXpH6OvlB3yePcX8cm9mH3pFgxfWitIeJaOAnk5b5BW1Dmn30GkhHYVccgP8QPg8V8IgzG2q-zVFJrFBAMhhjPsH8urZYb6Y9QMZYGo17NU-yQyUEys4DhEPOjFwkEx76eFf37OKPTXrT-EhNL57IaO5OxOINkPMxZ3JnL_r2PPrMMAndhjbtyKDqOFcnq65xP3oU_gGWPXzCvaeItpabm3dIjiX2q6ZeyLoZ9VtrBN-AmP2_qT8ISrz3OzbF0slczDoEafetgvE83L0knX141j_Q8Z_5tM76kYEpPcXFfZH_GHIzoATlMTIHRkVSMtPqeoV913dRoKEoSWIKxBisxsLLJML9-c3Ur2Gd7giW9BdJ3dOKq9SWemgB3v3sFhoSFuywj7lBb_fvMAr5q5dkRQq5gBfIY4rtArHLmQ909qlTXRHVTTJl9zFn4vqnW4G_YJfEY8-PZOVtKwr-ecH-yK6wXvTzFzzwSxE1sHMH0ITicwnDA5gIkcuMfOVn1wFUQqdg5mBNdno_yJwI3XtXxJz9n8OqB2kRURRvWNFCz5OA1MGAfag8q_vguxFdY7tOT7d-DY6rueIWDGWyY_FJdR-2o9gH774hcXL5cDpO3n85YjkjLyAUiua_5PyDZ5Ue87gonUC5IJKnTP7O_hjgBQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ded4f96c1a.mp4?token=LoxJDMbx8m7pCwPaB4mYXpH6OvlB3yePcX8cm9mH3pFgxfWitIeJaOAnk5b5BW1Dmn30GkhHYVccgP8QPg8V8IgzG2q-zVFJrFBAMhhjPsH8urZYb6Y9QMZYGo17NU-yQyUEys4DhEPOjFwkEx76eFf37OKPTXrT-EhNL57IaO5OxOINkPMxZ3JnL_r2PPrMMAndhjbtyKDqOFcnq65xP3oU_gGWPXzCvaeItpabm3dIjiX2q6ZeyLoZ9VtrBN-AmP2_qT8ISrz3OzbF0slczDoEafetgvE83L0knX141j_Q8Z_5tM76kYEpPcXFfZH_GHIzoATlMTIHRkVSMtPqeoV913dRoKEoSWIKxBisxsLLJML9-c3Ur2Gd7giW9BdJ3dOKq9SWemgB3v3sFhoSFuywj7lBb_fvMAr5q5dkRQq5gBfIY4rtArHLmQ909qlTXRHVTTJl9zFn4vqnW4G_YJfEY8-PZOVtKwr-ecH-yK6wXvTzFzzwSxE1sHMH0ITicwnDA5gIkcuMfOVn1wFUQqdg5mBNdno_yJwI3XtXxJz9n8OqB2kRURRvWNFCz5OA1MGAfag8q_vguxFdY7tOT7d-DY6rueIWDGWyY_FJdR-2o9gH774hcXL5cDpO3n85YjkjLyAUiua_5PyDZ5Ue87gonUC5IJKnTP7O_hjgBQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ورود رئیس‌جمهور چین به کاخ سفید
@Farsna</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/farsna/464184" target="_blank">📅 18:08 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464182">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NXdBMoL-g7roi1jAmmYwCoQQb5eTTtMmERGgtmbOlFg0xinTcFmt1uBMLqGn0ZEOyobXf4JXsSirCboP-Ai0QPWPUNw2IadnZEyXKEfmOAGC31-P3582TLJG-fwy1cRzSJIS63dqXrCymXeQxc1aYacco2fKyYjwm4m0BX2U2ekQyQ5ajAIXi9sfomE6fNqP-TobpprHVz4mOB8a2Oo48XItm650DH8Ant1TR9P_vGMuSbAqXedCewKeKAfXtXksqb11YAhf99-cP7rmTWqHg4PiFLGGya6JzcURuCLxxOtJDtMjGWf9gZZfRoCq9_l3Xou7UX5Ef8OuOxSItbX9Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TG04C4cEtf72cVcIjDgi9lrx0hZFSlvVuvulIk7EYZU_DnDjGGtd6oPnZa75UlmyXFE5fIt6xgrtSIoDJv1qih-v-er1NPa1l1_M-r-RzjrAZBckmckO6dvdhIAOUrDO5N4HJ48FK3SU35L8UVNtnkHfJCXLU1jVQPv5kM4ocQ5-EvFtUyQKWimDIMNpTgxEs-oHCl6vdyoJu5_gLOx2pu3JK6nJ1_lftJBxolX1ldM-b64SAqp2IHOBGZ7CrfaAMhLICrc5qR-3To1vbi9EqvNHP_bGmlw6VqoY9c_Fl1qiqIu90I1kA1yPy4QxP7PMkHFv6AUj-BVBI5haLQxVlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
دیدار پزشکیان و نخست‌وزیر هلند در حاشیهٔ مجمع عمومی سازمان ملل
@Farsna</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/farsna/464182" target="_blank">📅 18:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464181">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۳۸.pdf</div>
  <div class="tg-doc-extra">3.1 MB</div>
</div>
<a href="https://t.me/farsna/464181" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۳۷.pdf</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/farsna/464181" target="_blank">📅 18:01 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464180">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31bb417428.mp4?token=Dmm3h4kVC_B52j-7FlqVRln6CkqGX6WDwAIPIN436ULo5OY-rqcrmClLiGcze_eabSxw5UZlU9qRC7JhufIgD1SRSfD3V81hc01O9Mr0u6Yv4Pv9P_7wINj-o29SYvsDn2vEKEZ-9DY31YowSptI_osu30Uiqxn2VhwaM9fb8i15gqCOkWJGtSufv7J380Te1NmK00W6aR2KNW199ah86UUFP8OB5j2ytQ1zYq_FP98IL7uQzBRWEg6nPkNdATxTzDHNYLU1xI5SYuImBfcdjBFlfr3auNQd-kWu5GUdM18QHkjEVjmswrMsRHpLwJHtuAnoxCdm4Hzu3kB8EJChyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31bb417428.mp4?token=Dmm3h4kVC_B52j-7FlqVRln6CkqGX6WDwAIPIN436ULo5OY-rqcrmClLiGcze_eabSxw5UZlU9qRC7JhufIgD1SRSfD3V81hc01O9Mr0u6Yv4Pv9P_7wINj-o29SYvsDn2vEKEZ-9DY31YowSptI_osu30Uiqxn2VhwaM9fb8i15gqCOkWJGtSufv7J380Te1NmK00W6aR2KNW199ah86UUFP8OB5j2ytQ1zYq_FP98IL7uQzBRWEg6nPkNdATxTzDHNYLU1xI5SYuImBfcdjBFlfr3auNQd-kWu5GUdM18QHkjEVjmswrMsRHpLwJHtuAnoxCdm4Hzu3kB8EJChyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر نیرو: ذخایر نیروگاهی در وضعیت خوبی است
.
@Farsna</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/farsna/464180" target="_blank">📅 17:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464179">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">الحشد الشعبی یک طرح تروریستی را در غرب عراق خنثی کرد
🔹
سازمان الحشد الشعبی امروز از خنثی‌سازی یک طرح تروریستی برای حمله به مواضع نظامی در استان الانبار خبر داد.
🔹
این سازمان در بیانیه‌ای خبر داد که یک گروه از تیپ ۵۵، یک مأموریت امنیتی و بازرسی را در محدوده مسئولیت خود در استان الانبار انجام داد؛ این عملیات شامل مناطق بیابانی در جنوب بزرگراه بین‌المللی بود.
🔹
به گفته الحشد، در جریان اجرای این مأموریت و با استفاده از دستگاه‌های کشف مواد به‌جای‌مانده از جنگ، تعدادی گلوله خمپاره و تجهیزات جانبی که برای حمله به پادگان‌ها و مواضع نظامی آماده شده بود، کشف و ضبط شد.
🔹
این سازمان خاطرنشان کرد که مواد ضبط‌شده توسط مراجع ذی‌صلاح مورد رسیدگی قرار گرفت و اقدامات قانونی لازم طبق روال و دستورالعمل‌های مصوب انجام شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/464179" target="_blank">📅 17:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464178">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a005a31d8.mp4?token=aZoEJLc32qw4XDQcGG4pki-fmka2EWBBkmWaz7eTJhCc1nHESJkjLbe_36iCS3GXPXu81M8LsdbUZf7ADuAuYZqgncQx5DXXxkuKAPfQXa_CX9LXsvmWsTaVHbIBfdtOhk5_VHOGLxXWR8UK0bLiF7nk-KrfrXQXM9SpUvwRTzvDL31l2TUXyaup1zO7wJcSYBO-Kt4txce4MEGS1wVGDA_asolKjfKsce9xPDNfUyij8F73UhZ2bXS-mPgsh-2fQbQKqdVd4W_3McM62-ttHhuHIsmy68hh38sJVbekq44cucKfoGoLaD3cczmXyDC2ZupcdjfPDgPgvEn2RMaIKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a005a31d8.mp4?token=aZoEJLc32qw4XDQcGG4pki-fmka2EWBBkmWaz7eTJhCc1nHESJkjLbe_36iCS3GXPXu81M8LsdbUZf7ADuAuYZqgncQx5DXXxkuKAPfQXa_CX9LXsvmWsTaVHbIBfdtOhk5_VHOGLxXWR8UK0bLiF7nk-KrfrXQXM9SpUvwRTzvDL31l2TUXyaup1zO7wJcSYBO-Kt4txce4MEGS1wVGDA_asolKjfKsce9xPDNfUyij8F73UhZ2bXS-mPgsh-2fQbQKqdVd4W_3McM62-ttHhuHIsmy68hh38sJVbekq44cucKfoGoLaD3cczmXyDC2ZupcdjfPDgPgvEn2RMaIKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاج‌صفی سازنده گل شومرودوف در دقیقه ۱۰ شد
⚽️
ازبکستان ۱ - ۰ ایران
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/464178" target="_blank">📅 17:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464171">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uDuB93sf_uU-xha5U26dOuVfF_Sm5haMqMrcUCf6Lty4SxoPZeGym4dpfWEORHIXZzUFPW0RXj1VNM3EWhRgK7B---AfC2u49BxQv33ep2vjcnbKpCYgXaJsRYA65peQfKas8cqYzb3rigtnpIh9Y3hMgpRWN3SfpmfDpgKACEUToD-tac-cuBhl3IpURwBs_a4gKcnS1vlXg_wQvaZVieqtXdbQ3KZTOLSP7DGQ46qPtQTgGJOKjkniit_da_xhZfaCf7nOzR9HsTrrHmR4ohRsUjkCpSEuIAsOlDHxtPguk9MfV7Klb7LNZhIchGI6e0tppJzsA1qVv9CfG_kn0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXPBeyhQrlol4m4QNYbVnOxCe49DezhBUJmM-n7rn-mCEJNvqdmKbWD58HIgeMEsPwzAIg1hT577Sh7Ys0yyDcwhIM1s5QlEqhqh6gpzqT-bWogkuMzDuA5Vs42LRwRy_IlLC0ia7iv5ciTkancnQ-pm0-CZA8MLeO_0S5jI4uTyJ2tf-1t8zwx-2XlOCnsUiyhgqwaatdTRv_POlTNt_lgHlmATP3png3gBpYjWx-k8VZ9JOLMwiqrd757Toof7z8-tEbgrGc_Xp8fu_D3oOw_Q6F9OH4ONG2SaJaZ26woewggAakINVhXTemHnKRGa3SlU2sZCuOHALZUJWBGG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HG9c0IAQg6-3sMOq3WQTd9lSgZEZQrEojwYc_z-w5K4Nzlm5s-ZI0q4hx5tl47uIhfMwetm9LM67Yy6MENPNelwpNuksYgDUnu6voqui8r06P03r-0-c8jDaql-z1qnzlFb_OysbAIL7DVT_6Rve5rCzPMnBsxcUsYhQ_8Gy3k8BM5rAIrL3FAxjoW5xW1h1HNYZCw07wquQ2ONCdk1oK0e56No4k3VGYemFSx6d6U4f03papwcYaQRsvHwMLyWi1AlKhF8rHWEyj2A6yP7MwmQnu3v9Z0exw3RL5uGcCmYOx2DVA88p4URGD9WQs6Unyf5iVXwqrZK1kC7zTpAeLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eqeOHrWGRIPJCw7KwyqzQBqmd7ITyUesDUKHqofzLqjj-E4SsW1cq3cixLl1i4hzpEPcFf1YWnPjSJROv7cM2yfFf3NW3a-8hObP8MwRoxniPWPWYQVJjzrIbHNxHDkJswIl5sLPeTvsoqQtj_gIm9wiRQFGP3UuDspKrA9JH3BdgN6L_qSPq2dcqQtX9vya2pou5FLdVBrrNDj2NEkEH9XG9YK-2kDwo8-t1fNMUq0_7vrOR5PMRVkYTN-kno7vGLn6TFuD7aDBhPWC0yNT4Ru_fWW347EZoXD6OuxakwiCBgmaf-8cZhBp-wds7I-kNUH04zNiB0rQkkDP7Yv65g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_JTluAu0Piq3m2FIdSl7TxK3x6EQYKIasL610W39mkkuEsnAYSIvsoHYNdEphhfXYLiTwcRO1x59Ggsz4Ejfbc4KMqPfRnrxinj-4DCLwdwJcDn4jhG0LDgK9TsDYfce0uarbnwMz6E_SJdlrYyWUnMaJQVZ89n28VuCCVAfytvTdGxFCObpkMQEDpC8fyb4kZrZo1MgKCRYOXGWAvIXPR9v-7KjL0lTxSgfpStpsk5mbn4kjjpM3YM4rrTs3dM_KmgiGj59ujIrePAKRfM4rZYP_4-RKED3TwNsOZ3xLMxPeGwMbF9f2JyNjfNL39WhVCKBKyuVlSYda9f-PT_qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tG_sHeyR63R_VQwjLNt234PYYsuRaFfAxvriN3BS4_CAKSIoGJG25ZsGEPjsdK0hZZqIiEEfo5FEjt08hC-bgCa6QdzPqk-CiYdQfU6Kjz8OBY_3iGUw_cIuR1T-z2AjfS4jSXEAUpcN-FdUNKOWFilov0tc_mFQZXXRHS9NZ8QOvlm7DJx0kZ9iFu2syvfaJX_VJ3CVZe1kyhMQvSibU396BEREqQpNd5WotJ9W_G-XAK-kxr_Bv2VItxKsd23aP5ERJ64i8TQvxaJQayxbFGCxY3S_F6YhrjwaKewOP6NJGkdhbhXsR3M_AbLv1gNobQkDp5aauE3QOcf0fDUdgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RKGs_SHGDa8Ol3p2XeoRLK26DOkBcSLBRy-1O_BguUBYNJSjLljJvZMa0KVAKnUp30doySu10B3Av5kK9qr_EGhcAVvxEBDqXtobLbP8JSonfJp508S4m2FQ7KkBwB2vOaSYwtfyRv3GnzFLSNxJBNK5YTc30rFMHPNwB8NNdgpY16JmdBJi7ZsAkcCLZw9AiJQ8S2Sah_vwKS8ED_dEeSZdVArcw6zPWlfohfp_FJZPszTTGEWbYYdiKQgQL_PzIwbiXdZNdsu0SrPt0t-TI9SBTl8_TB8f-ACuulC-Qw2tZFJn0DuZAlzW9QDlITqgG7h6VxbG8MdUXF1omH4Vzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مسابقات کشتی آزاد خردسالان در همدان
عکس:
مبینا لطیفی
@Farsna</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/farsna/464171" target="_blank">📅 17:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464170">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lh8D6DwtWbbFayzZrJvpVTghqtU23cScwOjb_KCwd2j0Xa-Kn06vvj9EFdGEskGOYdl-1c00pEWfmgUPNq9dhwd8MC_GLXu7N20-qpO3h0EDbOdA4IJYuETfErDs0tYQSmvmMMljh6xEsJ5FDbMU4lxeWXYS4YV3bQXseagjH_-v2MMc6urdiwJQJDwWWPkVDlhoCatPIY5FxqIkz_jGgMktBr0Z0YOwoxMhGwaHyPuaftWJlyd8Gh2Md9vDTHgFcG9XQ3_ZKfT7-pN-P87Zd2aZIao0f91P03RkCyS_Mu2rgtjB0F0msN_09P6GimqMcYB-z9k1jaRc8RlhWexPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«کوله‌ات را کامل بچین»؛ پیشنهادهای ویژه همراه اول برای شروع سال تحصیلی
🔹
همراه اول همزمان با آغاز سال تحصیلی ۱۴۰۵، کمپین «کوله‌ات را کامل بچین» را با مجموعه‌ای از خدمات ارتباطی، آموزشی و دیجیتال برای دانش‌آموزان، دانشجویان، والدین، معلمان و اساتید اجرا کرده است.
🔹
این پیشنهادها در سه مسیر «وصل شو»، «مجهز شو» و «مسیرت رو بساز» ارائه می‌شوند، از سیم‌کارت‌ها و بسته‌های ویژه اینترنت و مکالمه گرفته تا تخفیف خرید مودم 5G و 4G، گوشی‌های به‌صرفه و فضای ذخیره‌سازی ابری.
🔹
در بخش آموزشی نیز تخفیف‌هایی برای «آکادمی همراه»، «فیدی پلاس»، «آی‌نو»، «چی‌بخونم»، رویداد «کی‌بُرد» و پلتفرم «کدیکا» در نظر گرفته شده است.
🔹
در پایان کمپین نیز از میان خریداران قرعه‌کشی می‌شود و ۱۰ نفر هر کدام کمک‌هزینه خرید لپ‌تاپ دریافت می‌کنند؛ هر ۱۰ هزار تومان خرید نیز یک امتیاز قرعه‌کشی دارد.
http://mci.ir/-GHNE9B
@mcinews</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/464170" target="_blank">📅 17:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464162">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/udLAj9uw1xAOvJWgThMsAfKlTz0nzcb4PCCZUX2e50iPj9NXo7aUe-MdK5tYu6hTs0GphXHN5cgA_0QNWg1UHJka30Kh3LlyaJS5NG5biTXMiU439wEoEectP2tVsIzz9fzP7KqWwNth_Y-DjfzreYVozntEmJvfY4NhpKxqXa2U5v03zg1w5SLjXTwyB_HQ_-y1Uab6LUaxIlEOJNSwqbf0cV9zJ35uL8LjUxEsbzHB9RnO7JZmkQKreMmqCVdhwtjtBhwaMVMJGASaROFM4Qk0ZHcacn5RAjYARhvBiuByAfjBZ8uzZxr-nIyt3J244NfV2zbltBMmiCWGSznoyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1XJopN10jgS-x0KYN2E5kGhMJU5SlPhWnEZVAv8AggdoDEEdqvPd0DjCZqI6wI3XepuG-Hyjb4P--Zh1HvFfQxk8vq9oS24WBhQvvJS92aQuZxZIZh_Av5jxgZZ5l8VVFKn0e5Qq51KPCuJsUUdyzh5DujFPQKI-O6T7P6j0pxPLA1rczDuyFoS1YNZlz0FuC-51CnSAogAx0czkxkdA2DDCO5f4RTmfwisdVG0_vltPERBGMEIjSTDaxBCLONA7RBgfVzw3FpJq8PllodmT0eLBqX61MrqTW3M0dZlmCFYgcA6tFuE7iw7aodJzS34OKWMEWHm4RGsqnVIxkAQGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jh6M6qBdo08ggHbBGYiSCp6hXSqXDmtDunc1K7Nqu3HIMc86tqcyz1sG88S8x043lWckk5Ox6UAqRufz0RNj7b5hU-62oeggNeM6JSyiBRxpxlHaOkywh8jvURFZezjiGO31_VaDwu8fXoNHJVVMVAfYjceC8ySfqgkJNoyUMW6tw0Tde7_hLzIQEOqfJrK07GErEEdgNWJgKBnq3uskYK-MLiUvWa4kDn2Buf2-neBFppzlzZ90RY2Bs5izyefdGK-MsgDDNCC5J3Rn0Z8Kc_4m1N1Pl47XMWi1V6qRlPT_LFxqr6nZ-iSzHe04zIxX8ue98hlM8BBBf8q2ADoI-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y-TH02axlFNOanvoH5g_90qRfExaRM-jdb6wj9vwbNcwdEbrm5CZPbot9NwiVoTEmcofd08EIlMUOjGleFyVvMz1r6dLYoDFUjtLEgZTJdk9gvkEtocoV-EriWOdIVdl--0K3_27un5XtCn4PDIHXo7UfRjs9qRzb3IwE4siZrhEDU7kcrznV-fbQxUG6Y9ES9oiqlW8Lk1e8qP1_hqtUH4bySzKyhz622s4LEHsxZYK8G-wYAul-Osa5nUH9XvKrbMN-yjHG6S_vOkP-AsyC00Wdtq6ZzEegPYwbzUvAnGwI8HSbkpJmTIUAc9a4SaWPI7zBtO5FUISkzeri3Hq3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUd_9xdrFyi45DN3jIZEjyneGWDH1NY7VxfjWptSqBConrxpD2f1ZHJ2G6S9_OHBNYLtSlDIUTY9xsyuvYnHzR-L6CnZvS481t24PT4Ihiw2T-HWld5Wavq77Pk-sSmWeD-JZOITZ7daeLDHmUqizYCZocCjCjkzr-I2WNSzUWctnmZ1h2xkA2oJMHS2_4NSkqrkI-FlqWdBrRqWT5awTbyE0liwkMks9ymj4tDFFtZrKxlbgujhurb0C44uAtAG47Myp2la66ck0vQ3yvt07UmxDIuQOJ7YBiq9vpgZuMv195joxUnUGG7kGNWzktMHwv88MZHZn7mMWrGhEWbgvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oym_pbplSDeDip9mVjBARbemtzp2s5WNEFoCYg8YqEJas73TkXoueGU0LXjnaFD42yyOChA4qek5RNY1jDfCsX6tjmZyJ-s74B5uG3xnP7AGzfllbCdRoxmHzsRT24Z9baVC7X0lROQ8-rkmGt7J2OalKoTgmDCOsC5wtAaqm9f7S7qUkw8aSepa6D492DvVH0JD6qiRQdM4I0ald2qx51T_n0lMQaJ6A2rgwnl7Bp1g4Bm0ZvI4Zfo6Vl19ZZ-uZ7Hb7wHJQHF8xQhTRS9cUkIFLJxiMUACGKPRYZ2pBlA20NKqoErydhQU1nbgX90egLpzrniRGPsrpm3ndIjWPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nicfMOM-mYdcFTedsF9wdM3qc1-JeoTLwPLWpB92AHTN8shRKWh9ZXIHM0ldPEB_DyBac0eul3p2ySa1SNf6A6UCUhzpTT-xgJuVYcH93XJkHvb8qRSLPp3w3ts36ONgYvPlW-ierbpmpyBOcixLV54ot0niXJ_g0bV392ObNIRqXnpZDMhA9Rz0VCbcbZjt3qub47FfmgO50Oj4q_lwaCSShCfGq-FKDOeHhin0hFTLEwinoO0dXaa2V8rHkIMRZ29Cl0GQFfXkOYF367ePsFApkdghv-fyTeSeIffutxgy0Xx9D2BfLqfpu0AVjfRy2dbUzoGrU-hBWoEadJ787g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHNNdxJLKvOU4cDopMR1UCgA96W4x_uOIIQi7fobKU58AIo-uiDbTK5-3hVGM6huWeta_dOMzivuvceTU7kdOH5mfRKuNe_lStRJkXm8HXJTSA1gW7DlMQWGIbnMc3fuhiWXeAbRK0P862t4rp_1LRfsUPAmYDgo5y1gHNVunQY56RASVg-8UjT7MSdTqh3g1_32i8oXxtow96QuO073tAAJZHBXm8pxkQ2YfqwdozX8io2C538TXVJsmIZfzPnD4Y50x7BIZ8etrgQfgEvRBI5rdskfD9CeUZ0S4autQS9cekhnMlQ3E0OQwCuwYQe1vIyJs854wpoNTy5Wm1PzjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔰
فرش قرمز مترو برای دانش‌آموزان
🔻
به یاد دانش‌آموزان شهید مدرسه میناب
➕
@metro_farhang</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/farsna/464162" target="_blank">📅 17:37 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-464161">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/farsna/464161" target="_blank">📅 17:36 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
