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
<img src="https://cdn5.telesco.pe/file/d8FMdeVjuv8LA-TrPQ7By5mi-gnmKO12JacByxiSGIREAuZl3OlK04IMWDx-HoZEd_-0vE5wW5hETgz9GIji41EZDVnR2FVOrPZy70IvNbEFVwTDQPfO7CkY-LkbehH9SwEv7ti9RPtVx-LDdO_0dWWP9bQIbfbUDtCJ-lqmpyiWDkYGMbZ52WPMKlfYtNGn3XMYt-YzZ6d2uXrERmdikaaM_knNDpjcCXfibgqACK9XL9tEgOqZLE0yViOirAroPwjhxQtu2O-cU2KtXn2MPq5ATvL8R4pLTCFW4dLLwUToIgWV-FBKzIqmrkat64yHmpqHnpR8H5U96IleP3o4Sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 689K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-96093">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbxjoNe4R28HVhkEcX7ljBj765X1MTOKW2m6oSHyt1p48YE21fpXDTqwR_zqGXROsfnsxi4xH9t2QF7Chulp6x-s-itJ_BcjctUeGHN_M82DB9svkqLBvKSk_ljkSr2eruGXABzIPvED3oqV1vYlLol4yR2F4A2juq3359OjSHkXoFb8f0-wk2JMjmYQnLpolTkp1bFU9aie8_FLlcjryNqCKriPkWOwzQ-Xg2n_01ZZk8b_to5ZYEgdLmSabySbKEdTrBgP90EWwNLhJRxXTVaE4AS9jqzKQYPFlutmTT0C3cvN-6pqr6VN3o2m4A5CZjthDOBGLXoIOaDfqb5upg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇫🇷
💸
#تکمیلی؛ میلان برای تکمیل قرارداد رقم ۵۰ میلیون یورو پرداخت کرد و قرارداد تا سال ۲۰۳۱ خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.95K · <a href="https://t.me/Futball180TV/96093" target="_blank">📅 20:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96092">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/Futball180TV/96092" target="_blank">📅 20:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96091">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A53f6AKXzEaEP69DSwDbPmcY-p_J6L7elAPp5LXY3AJj9sfiizj3WQre1vUMhFo85TvwE1QBFixzFzpGGbtJcs6BL7VVr3ZVtcbf9kG0Vh858cXZJcYBIoZAFDumT3LlBaQjhKXMp_fwK6HmihjamOcKVy9uDJvg-drYcC3x8tJLhg-zdieVcl424Lg37p3rz__AZVmMCBRLsSgFGQ4ur-iffVQwYiUudpbktWMJV8aW9Mt4mJqmDZ5JYCgp7i6rbQxemmWl5OkGD9770h97-gJS3vVSc5Wpgrin7yKl3d91-QSIpfXgo3soajR3ST2ykSi7oEFV6XO48vIqVHAIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری
؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/Futball180TV/96091" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96090">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXpswmY-IlhTY343ze_aW4gLFnmQwxsARDdHPyUDm4lvvKs6ufU3p8duRmr1XyuJAKHB78ml6QjF_Odfjl3jLlA2NML9OxtgYOSkrZQJH7aaSxJXHpzjXOzXpV2vwTUTT3s0wwQXgVKTD-SFPsgZaLjDWaG9OXDSX0IO_Qe-BkZXlg9xFNB1qQGHtcVh4DxPD6LLWoZXzLhe0p6k2uG-YtONFvbslby36e7zSMx8XSAEHkYTa87xtlW4HgblA3VwvDzGIU2CzAKne8MpozsMgFT_iwvGe8eBwGEhxJs15yfMSfZE13C7XLVSy25IoqgKG1cckhOgvd65V4r96lab2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🔺
۱۰ سال پیش در چنین‌روزی لیونل مسی از تیم ملی آرژانتین خداحافظی کرد.
🎙
مصاحبه لئو مسی: «من تمام تلاشم رو کردم. چهار فینال بود و نتوانستم برنده شوم. هر کاری که در توانم بود انجام دادم. این بیشتر از هر کس دیگری مرا آزار می‌دهد. من بیشتر از هر کس دیگری می‌خواستم با تیم ملی قهرمان شوم، اما متأسفانه این اتفاق نیفتاد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/96090" target="_blank">📅 20:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96089">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKop7afHF2K_bRlhLEd-He6GXFMGHX9UaiF4vaJhdI1uqnQCafWzaWXKfLsjGLFLQEKee3AiX3RoG3aRnHPn42lC1sUbRl53SAzWFstBW3OpyAyFtXnqp5ZAwWnQpxLW8kSFzqrLoJai3DU4612ovXXq8vwltqwPduHjnnrsqu7NilRhUd9JSjLPH92JkAwU6ivq8mjqTzL1GgG4yz1mTe4jhb0OC60s9wRvSew39Ge20E8OPAmO-8Q6YGgts6_3gHxziAR04CWIuSB26jwWnHXE3cBOjgNfj4rnIhp-9RAHOQhShCxNOg8dULV-j_VNap--qE55QGzDXl2bJaKVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ نیوکاسل یونایتد با ارائه پیشنهادی به ارزش ۸۵ میلیون یورو بدنبال عقد قرارداد با انمچا ستاره تیم‌ملی آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/Futball180TV/96089" target="_blank">📅 20:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96088">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgPalmdBZ_Y652rNXy178GYE7hMjBAjgkkwoXpljKl5dz9wjZsuUxxLzed-z4X1R6O7ZCMiDy03vLzVEYa-roy7CA2zVWerDBAAbnYk-Gw2DUuAGzOGBlmzTEpesKYbb0AQujGFICNOo26Y9qsQLLn2QWQeV1KGDI_wGcooa0vUU4shMjuijfUlc-32wjHUKhPOTTQWwpR9c9xwlAJd-_2682X2e_bbI1zGi827TFbBR2fUaYT59s3Dpe2g2dv_ubx03o3N7Z9OKSW8ZJIuO2nCkl4OoFO8LCN20AjFOZxB5VXc2ZO1HqEZZw-mZfQvVMOBJV0yPgZ9g7LAyrIe0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به بازیای جام‌جهانی ببره
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.32K · <a href="https://t.me/Futball180TV/96088" target="_blank">📅 20:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96087">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏐
❌
ست دوم هم ایران باخت.   ژاپن
2️⃣
-  ایران
0️⃣
🇯🇵
25 | 25 |
🇮🇷
19 | 19 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/96087" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS8Z909ypHlHC6lTYVyKwKQ9c2LMyZXvl1tvSa9Peh8rmX-8OuoX2CkfkcdnkOIqMZm6YP_W5Rs9Hi4tLfclS190ZAWZAjkSW68ryXFFApVLS7VDr5dExgXrKmo77FiOHQhlMY3Vgs-yRHM4Ssq0W1alpCjvLIqEek51rskUYQtH1Snk30lKV6lpMISjWVKQzZ-CH3HdeowqCbDPyYkHY8re4XB9DqpV2tBcv8ZqmL-diG8orkLntYsED_DCmwberWw4MzBEPovKIKcm8iTklQ-hEn5yaP1WgfslMLYVy3PgP0imiksbcMzShP3puRe0K008_7S0GUPxNRzSJ-lwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/howNci1C8YQ2kiTBvEEmvWQmMko_twoMk7kYQXOn-x_s0iKBGGOwJsTHlcFL4TaJrXBfVJJ7Mj-yEliPu8Rm9a6p8VyKshf7zdELiLvrWl3Nod1Xb74AsXYw-RvkJMe-GbtiZpY_B6ad3HCobkH_SHF85ZF0DAAlGa5J_zKTXByWxNFCel3nVC7zaitXVVoMJjvHxHiGtBYfAzszsm7-xVz1M9_a_PSgGwZTwGfu3HJ0-V6qsMkJH6T4JkZdu4ENrDRgQDJkej49ILEY7BA0KdnyVxQyMMHvQwXJO-gf6WaukxFhphn-xkRCSuXt_ZEUQNr1XUu-kVmH_-F03tztBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پشمامممممممم
برونا مندوزا مدل ترنس برزیلی گفته که حدود دو سال با یکی از بازیکنان تیم‌ملی برزیل به صورت مخفیانه رابطه داشته.
🔺
به گفته او این فوتبالیست ترس زیادی از افشای رابطش داشته در حدی که قراردادی 500 هزار دلاری بسته تا رابطشون محرمانه بمونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/Futball180TV/96085" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96079">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZFkZhsr39uLFmc5AP4FiM77aFR-7eZFWhlxNLx26PSzXAybOLTMQZOcomYiiyhW3VLLT39ziATYDioP4e2dlkVEhXBEdywWob5SvD8tC03LlY-ITLU39tPijouzzibBnSucUJLJK3OKPOQ7medQPxGC_g4ggb96_tPmqYRlGWGgBPOFDIpjbcUkwyB1e--mhK6ZvHXIU0LjIW5uGbO60FYhV098suGNXAoODriM1ZATvxE4OaHbdUves6YmvW98gmVjlViRLFpu7YyFINOeg-HElDuzK65guVmilXWjVoXXgAizqT06ZdCKbdK4eyj-mw9NWi3qbpCn4UjtSXsLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlTAHx_kSk7uKy9MWlMN8vTjIu2B0OecDMVzxRUymF88Sh3ZaVIyGdvTwBFKOXC6OF0WzMypp1tw34fjtaG5d0Zj11CXHwGb9rEiBgnoSqzkHjJIakuEu7jx3keNXn3cBplFoSg-Oi7GyI-k_A-VKzLpR0TUmIbBYrmVbGFmAP-POl8c-pB_hx8baqtXYUHsy3GSFQNrYLjT0R1wb5am3FU8eStCEDiiT2tIOhE2Ro6G2Ll-9oZPAX6NUdaMIc-7ux-gorg8FO6hoBdZN1ZVvBdoy9Nt-AgvXb5Yg3LJAaKdBI8EHky6eoFciZ3GWVPOe89k2QhWkpXY5JhYUlGQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8AIn9YzkfYkaMzxfzfnjmMir26iIywTlOXeu6tJm0ykiaH5RGFpn-KVYRXO3n7uflue_Z8-_07Oyh8D67o6fCjwtCUY5ZEWA8mGBPCyzqLmxP145JPnjb0Yu6LMJKjxVmf5f8pW0EdLBl-pIzH5KWX2REYw4a8a1_bsZMWS8yT41elbmgwyr_DjPc8RRGOwYHeJJKjdkTUegHqs1TYBDJNC0195g555XxQdhYXm2mbUe7ksk5JbOWY5VyIAK07aXemvd8fUaCQu2exLn_Mx4_FtGYrj9nOw6swsT0xGRC4GUVvdq6neIWotJy30X4WMxwGQ3vh6Q62BMpxxDAxK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCm9zY0WqTa0T2n_C_QXyGOFa-PINAck1nVBF4LhvRoEINHEMgsoRKg81v8l0vE1Z13MsmivGWJTDHGYGH0Sx0pYv83wJdbTKO1UZZlhmXNNHOjbyA6g0AffJMQJD3lo8xMiCKfI6BqDGWKgnQixavftrMUxqDZXSKsVQySbgyRFNqwoVAhWRhGS7jVCzoanhpKKfPEAWD_-zJDPri7jA97o4jiFSQ8TeEII1_L1qn-k3wqzOpSfrKrXT4_99KRUk2ljHwi9gZY4w8MBW0BvntolCjRqszcBwsIJqGE83DHYhC7mgKJbNLwkYf-GwKASvwSWwlrPk8390ZDJqLggDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=iW_ErVzodVI56hLeJgJwYLdyXiDHUQzsQEVkpOo5O6gprXUWNm0tNj-jI5aWmxmtQ9D3WGeBUnGFc0sBpNNBeS10W_TY0b3itWc9xNXfonCEjKMsjuryrMjvP3V0cvq7XJIc-AaFSYZhuvf7QUBEwaLcdQbJD2y6WiPb2w_PkyYYnU8EC1ATPI_tMg-6Bw_wq5yiPNtIyAaGd9d28bnBFBPtpFDFHlPhv7HiR1VNLJqxM7tllwfWrYQi-HpPPOa5DVUHLD3u3Uw2EEmxcPZr9pOywRQVuXjP84ZSMFWj9VLtPLzHJRe-CwpM4nxIQu2Zd5j26njVvceIlULkks8uHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=iW_ErVzodVI56hLeJgJwYLdyXiDHUQzsQEVkpOo5O6gprXUWNm0tNj-jI5aWmxmtQ9D3WGeBUnGFc0sBpNNBeS10W_TY0b3itWc9xNXfonCEjKMsjuryrMjvP3V0cvq7XJIc-AaFSYZhuvf7QUBEwaLcdQbJD2y6WiPb2w_PkyYYnU8EC1ATPI_tMg-6Bw_wq5yiPNtIyAaGd9d28bnBFBPtpFDFHlPhv7HiR1VNLJqxM7tllwfWrYQi-HpPPOa5DVUHLD3u3Uw2EEmxcPZr9pOywRQVuXjP84ZSMFWj9VLtPLzHJRe-CwpM4nxIQu2Zd5j26njVvceIlULkks8uHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👀
یکی از خفن‌ترین قابلیت‌های گرافیکی GTA 6 سیستم نورپردازی و بازتاب‌های واقع‌گرایانه‌شه.
نور خورشید، چراغ ماشین‌ها، بارون، شیشه‌ها و حتی آب، همشون فوق‌العاده طبیعی به نظر میان.
از اون طرف انیمیشن چهره و جزئیات محیط هم انقدر دقیق شده که بعضی صحنه‌ها بیشتر شبیه فیلمه تا بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/96079" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96078">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/96078" target="_blank">📅 19:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96077">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSe42LyAzPbOK408WJlkxSxZSwHSnieoT5duNrn0Ctq0sVHJIwXx4HCdqR8MEc_CtWFIHfxR_vL_iPT0SV4tpBEa4SzaRkVXZj65pvY9xWD9vvzoK0ouHFrkjApxl0aUbkN7Yh0xRndI3oUOHNq1NFIKnVkJl-5qBhvcqkYf2lgfoRGoPoICOVCt8hKIP-c2yR4GKP9zoCSUbY5UxHojJ43elWOpgLoUo5bevYpRWRVP4kPEn0pgsBjDCZH_qwy4FLMKTLXWOeUj_TAccCqC3zStAveswnEREZQokt0norkkIbstdixnUFsxSaoHpCqMRzlzLnfhtJGsr2eSm0iw4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🤩
لیست‌کامل بازی پرسپولیس و چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/96077" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96076">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🇮🇷
🇪🇬
فوری: تیم‌های ملی مصر و ایران اعلام کردند که در صورت مشاهده هرگونه شعار غیرمجاز یا نمایش مرتبط با جامعه همجنس‌گرایان برای بازیکنان یا کارکنانشان، از زمین مسابقه خارج خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/96076" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96075">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96075" target="_blank">📅 19:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96074">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YCWLhp40VNZe6J1kPx-cAvXhmEFkhtBB5Y0iwQTnubUKXJolQJQJRz_aWUNfQksUGh8kZDjZo2OcAFR1ChbY4JXbNxWuudWa30P0scGKPLzCnQT90Dfkvr1YtpnDSsHZJE7lmYJx7r387f6O3b-ybr6qQM1ha_VeLon5VHDVwbLBYoIdHfVLCJwsU9QC-gPqFjeTUZsk-XrvzJJXtuEu_R7A2xmm9sLNkBduIP2bS1ItBKIiIb_K1hCR-dGQEuBA5dJixpQTD6mDs2hweJiCvU5ic_8hQdrCiz7LTgSn2NUNWmkKJf1WIfQFXSGCrMLN_RfsUj45YxwWDqdO4G8Ldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
اکیپ:
نروژ با ترکیب ذخیره مقابل فرانسه بازی خواهد کرد. 10 بازیکن از جمله هالند و اودگارد استراحت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/96074" target="_blank">📅 18:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96073">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kn7QuGqOdAbxY6sLanQm1--QZnwT8gDLdPisoz-TtjpoLZm7X6WA7SvffwHmuFalOza5wJgThhtauWC8ogefloBuFwUbRh87mtdTDTOXEnbPbnmyFZE3czHQjdVlukTM4qCQiQ1QR95RqwV2q-Yn-O4i3AQpAL1fuz9YSl44GT2w1UPEwEGT8dawEpz6tcMGhAV5O-d5hRuk7UhjAJjjMdGNgRiG_yP0CY7vVLE3zWnSPOb3tem3xaetydG3K5pL4QCkJ8Mp49Lcj3VC49K-zchO-jK654XjyiQaDVFmrH-GsN12UCAkByr-atcXgYSc9QSmKqDsKLYnknybgCjJIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو دیاز خبرنگار برزیلی : پدر رافینیا از حق‌وحقوق مربوط به تصویر و تبلیغات پسرش سوءاستفاده کرده و حدود 80 درصد درآمدهای اون رو دزدیده، ظاهراً این موضوع زمانی لو رفته که رافینیا و همسرش میخواستن یک عمارت بزرگ بخرن و متوجه شدن با مشکلات مالی روبه‌رو هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/96073" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96072">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEORirRH8TX4ZLKpZ5cZp-X9JQLqgwxAzdPopl16rA-gyc84xRdHHl-O6VITj_EHw03EPewAlkZyI88pTCphjQ7RgZWBxdYTk4Pmqb2l7Syc9HLzO9ABn4jTTqFyNoMc_UiYzE3-0rQjduKbzT9_hBo8HQO-z1DnTP_0-S82uZaSzWI8w51MkjA6SA6056bDc3QdFk5El_PVG2nH-c1M7KwG_SwXT29RMxTZO3HEYMSYqmC_cFDdgEJhJYDLPq1TaU2olr7Ibsyn3le6LuqS75LkxEg0MXIl3gjSpA1vu_5g4jjriMyeLsGPI1CXFcICCcURpA1F8w1gEwqEbrhfgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی
18 گل در 5 جام جهانی
5 گل در این جام
34% شانس بردن کفش طلا در پلی مارکت
⚡️
در برابر
⚡️
🇫🇷
امباپه
16 گل در 3 جام جهانی
4 گل در این جام
31.5% شانس بردن کفش طلا در پلی مارکت
⚽️
حالا پیش‌بینی کن چه کسی کفش طلا می‌بره؟
شرط بندی روی بازارهای پلی مارکت از تلگرام تو کمتر از 30 ثانیه
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/96072" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96071">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M1asEkpYe3iXl-6Rwp4YwqC8lV8cGAlqPp_vwXvwAhcZywBS7w4dMG0_9gZPEx317fphujB9VVAsu2RwooWVjaZz-Eh3eHB3yI0FmKq3lMwN3-09YXumotjZCH_SzDgMpIlZPKO_TwS2Yr-EEpU-fSOpky8hcL6WX6zZob-VGhj0LbyA0ep-hBfgUiqqIaHGjslCuuCqEpIVeZGX_OiBKLlJefpEFeNllZcvKAKMzpZDdqHdd37_FK-Jpz7lh_SoaNzxn-yhPw8LzAIhdU3q1M0iVcFEtfv6Up8NQXIsRDUHJw9ufxLKnvDAtQZ3BkUlg5hx_ScN3qleYDlr_NLf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت ترکیه تو مرحله گروهی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/96071" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96070">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=Jkvwna4B63vcTHEJHGCYZfYvCuTOqYH7pj7so3o0Vf1oZmGk5qOtAxcczE_HKDRaAysUgs1MCb-6WS2CwPL-wexiOY0JiIN4YqS5QMTnort9_f3aCgI-xLUZ2Rsh11EcGLrtR6liSIcq5IoEa0-VdVX6xCatj45RyFr7tGuDPrOs6CJN5JlSLgtgEnRlxBCp2VFRo9kv5qTORLAd5ugmcgRT_-T8wt5Spu40RsX_S3qabjWPYIoh_of50oUZxyByLSZS7h5w-cFjMFHcp2EncJXJeCwgnowL_5bgE6SpFwDiIuqIByYBW-cJtJlwgYXxj4fhzau_8yGOB3Hrng3cAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=Jkvwna4B63vcTHEJHGCYZfYvCuTOqYH7pj7so3o0Vf1oZmGk5qOtAxcczE_HKDRaAysUgs1MCb-6WS2CwPL-wexiOY0JiIN4YqS5QMTnort9_f3aCgI-xLUZ2Rsh11EcGLrtR6liSIcq5IoEa0-VdVX6xCatj45RyFr7tGuDPrOs6CJN5JlSLgtgEnRlxBCp2VFRo9kv5qTORLAd5ugmcgRT_-T8wt5Spu40RsX_S3qabjWPYIoh_of50oUZxyByLSZS7h5w-cFjMFHcp2EncJXJeCwgnowL_5bgE6SpFwDiIuqIByYBW-cJtJlwgYXxj4fhzau_8yGOB3Hrng3cAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکوادوریا به این شکل تانک آوردن کف خیابون تا صعودشون رو به مرحله بعدی جام‌جهانی جشن بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/96070" target="_blank">📅 18:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96069">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQpDik0ZgdaymK_ZiJFkgoZMEA1pKZhEM6L0sKQ0RRaL39Hhmj-tpjPWIkW9k7EQKRiproUMPVwbuuYHxPZy8XlOaKsktnMvG8qgm1TPUhM20pbeSZsrVLLaGVTt7mt3lwkszITPxEotwx97BKl9SQKtBBQJdALZnqkKHsgqt2RE1KEOvX15UmkZgAse3TulMhdpLl1lObSkTFd7BlAgi1at9L5hug88xAY8ujxYgG-ZAz_sSdtobSMWB3ZD701FNVWvidLTdI4ZbOqY9WKqoETyBr20RENF7LNzUpOolKUWeFv5n0oQFNnt91fzYWRkH5HEE2oJiWqFBQGt-hvYlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
⬛️
🇺🇸
#فوووووری
؛ ایالات متحده آمریکا بزودی با ارائه برنامه‌هایش کاندید میزبانی جام‌جهانی ۲۰۳۸ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/96069" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96068">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6FgFHqiE6mJDUZXwTBoWTNSITdR5wlk7g8czFeLE2zSPMYAM62U9u_hY4TN38ypK31xICl1BOyDKCjvN11DxEbf6zopLhfaFDhsChG0DUktBHxFRH_6_1lhlzmRapXDOmnJ-3gAi0dSFbqriIg4O1MfASAomfX2OSec06TWygvFSsK-zGCRxd2SGbsKe_qXd_rWne6qIRam8vvQajoDy1T51q-XbQ_f4BmW6TPwxIitaTRoLk2hsTgQCbFMHORXXLf8XtpJ0ioHyOx83Mzoe2_A_VW8lISPfM8w-7G_Ujcr4tjB-mVZ-KeDs8RT0zVdrYjMzR_8IXU1WJxBhxDO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
هنوز کلی وقت تا شروع بازی ایران مونده ولی رژه همجنسگرایان شروع شده و هر خیابون رندوم تو سیاتل این شکلی شده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/96068" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96061">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TC7RDRAr7TcQSj0PPGdAKm0rAPms_tUjfZ9mfjnGZZEhGtzaWabr4tjnrvJwS02fvMBRzqRCJX2uzwzLXB4GGVS3dZ5oh-uUaED4HxV8zuCL-8lFymeKTvLk9RpWQCTl-WztBk7wEoszMCI2xSMHFzO8Faj4JfOKzKNHscQuV65np7WlSdBnXhTLQ4-itITBhVL1dXYxfPnrf5PcUd0lF21v0FgM4GewxcwAs5ALtmZ0Ft7WFHWETvlaRjmdHgq_7g3AeFSvws0NrRyfZM3Opc8SQOvTrX6pwV-qNNBcXbM3V6ik5QKwfjkZWG2BqmDmto5Uj8zsdS-b_TTLHDVjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWorjxboXlb1kMWdgAld3ysbPawcuGx0MX_oGCpsf8Fd9-HbDSc8aK6oNgyIJT94qV5nhiHCjWUrv6D0Ufd3LLWcECWtn2I6AA5BOWTBtxG8bZHWfFJs4SE0dgp2xeyh7eZ2FEZA0lUJSOwRgd0AY-tBA7mZ5pCgZjClvCpVOwpbaofeXb78D96Hek9V1VH0RlK6hNvJbrtFFjnjKNKwSMGlaD9TFjutJso32x8KhH4Rlr0pJ2Sz2FsJbGIBvQRhZQO5WzC0Sa8uzk2ZCp6K-4j3d0PAPzkC8G-lQJkC9wr4A85CQCTKwgGWIMsgwzvTe3n24avv2JfgN8xKc1G6Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1p9BsknG2bc5sHtwsoF7vVcxjL9z8K0W7aUrbFDod4hGa-xuEv6bDV074Hwc9Z59goTyX_-j6CqqIR76F2UD5H2RzCN5iHFL6l2R-ArSsBS0zBYc0vOHO_m70VLy6iCbcA1rOFvOR5RFoHtFmP_CWQG2TH1Dh_OUUxSTtdEOp0zFM57o-cdNpc8XfzU6KmYMe0QWXFdrA5bE4At-wuT2LDx37CHmKNpzUdEglQ_4ONUFRYbZii3Ns4Zuq0LruFjCNLXlJEFRvo4GL6snB8lQV-TF_KyOrICv4ICDG--AXGIjEzRZ0f0RRGAcoSjLM0Wr6QfqNq8Nxp5SBe2UhxbDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U3GKlR3L70QUaOT6tNTNo1Tk0Ay0aL1d4un2iPteWy4xoEfIs5WLMhP0qTa5HWb4PfaBGFw-NcFMhJwgQ5x9QyaO6txXOfuI3hiXzlx8jWdYOFEotL5adtS4v5Eu2dGYM-OQg78vh6zrG1H8rS6ceE1dfhXATJqSXVTwW2PfqjANZSTu2gHX7WQSt1mOk-sGCicFA-oOCdSHeQAKqBQmpklXqKpOnVBMzDSxiILeskjxgccNg3pnbx15q0MqVb8gHiNiOfAQw5ZxXnJZR4s0S_EbZyPY4aUbmQySp5jwatOdJOXOYDGDf1bdpHipMy_F02Gzs-AWtVNXNEUAg0lNtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adITU7qKDzGycBgrsvpTdFwOhKYRVUor496RbqZg7fkm8iC4JXRmPhX4BeqL0unf3fdNUQcAjOt-cxgD2Byw59hCHmXNme39WXmYk2689KH0EDBcsFtPZ3osxQOtNXOkqW8OEeo2RV6n4YDmjR7m5PcxjLTSvU8ZKhBVN4PZQayO64yNweQ0ZeixAMdC4FEBB43FUkTezt_7Hh4kbUUFz3ewMYVCo58-G-YnNd5Ya6CMUrXqAA84ocib3L-_plsOyugD5IKgTfikSLRp15hRbOvQVTk6yQ_PmBIpRZUtTQ6Csu06Q_bJ8CiMI5OBZz5OhgFfkE2yA8Hr7PVvlJzGZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s9SQMW6xx1ftz1SGU1q4ML_oIdJ9gPjo7viilWjQWrBXVblbDAvm7Vj3teqbTaHgpwvAWuz4s6fX_UuJ1ASB954LPbbCifhQjh7-K4VBH6GZfymwD9mzZCeAIl7uK2wEIpEHxUTyTr7ETlbeucUa7IujJcGE9gm0cyVxTcEHm1cPilo9AU8EmoAjwRPxfc7tq19vbFvxJKA6G31Ni3Wgds0RhBJ_h6wfdtqn01V-pQsKg47AMgFEOFPDr27GSXA0bxLaeaRUUdGY6lsoaEzYZYdHPioQWWa0sSamggEgB30LdY4zGlWNWWqLjEkkyZIpY6NKj1fI_SJe5NNK7pqCaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/up-MvLnan69d5wa5ZOUDVzERjGNCSO2HTcp2wZKbJ61urpcg7XULx9pG2cnfXmlthGWgPvXvvaPw42fzUcZhQKiMSsAoRnlMP4kOGZfeY85scjO7MGXy4_rCwMN6Bpm2LE9IQOhk7lYmhMI4Mja52ZbspzzgP0csIGweAFt96zmd4u7SQMmdpFKkwYQXEfFhMkEGoFmePwqiyawA9fgjAWv0UHNLDuQ8mPSVLJNgQEHD24dvI59FcBmjmbYDPajIArolA0sdCDJlxNHl-AVvJk9vUbw10pJAkMQM3CTcyr8a_SuL77oqhKAFmQgxq2_MEtDI8D03psw_WeyuriF9Ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای نروژ - فرانسه و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/96061" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96058">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XvgB4O6Ub6-0VjYk1YVo89LkwNTA-MpYa6bew897BiMoZUczqYFDLIWzhFgXlxivUKmMrV5Neo-BoFrnZKp7STH_x_pzDd-kCaw9j7rqNiPhZIwhf1wKUJsjUKWZqDZ1n25sstjkNKTWb8TRautKIoa9Ru9YT72vNsiTqFS2BveGJrLk96ogJ2WLze-WcvW6qy1zhRnr7Q-pbR8kcI-oAz6zMm4Wv1ELI2EufZ20nEgpOt453L6TFXIr9ZKhBL_UEHH4WpFm3SAOs-JRZPHvpIz7OOnsXVTnLGyq3dEdZyjJeqJmNR5JtsFcFn1kG8VHC2Xrn-WxNVyvEhERfZZzYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jX4WWcMCKRSxfvLhJI7yLtIXWJIxI9yOxXgnQOUClQvQwBN1XQHfhR8KuL_4tiJvxgR0HvrG97iOW_6veohUomEFISdJhW7Q1r5suP9-Qbz6dAId_vIum5TyMQEYQgwt3q-l03C15FzKoCU0GvfuKU-JovIvU5V1cKjn_UwHNDopq9koGxFvPGEHSauzZH4d07smQk802fbJHR8Uq_FCjWWZQO65g5bVsojuHpleVEGFzF36V-GARy1W4t6bxkCPrHPHJrCfzEMBE9WDxoR1eFe-vOsFOidDVoNxAa1vnwZxOuMEWWTVf7jlHbUqAIXr-lKwUR14hCCRqJePlvC7uw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
هینکاپیه بازیکن تیم ملی اکوادور مخ سابرینا کارپنتر خواننده معروف آمریکایی رو زده و تو بازی اکوادور - آلمان هم بازیو تو ورزشگاه تماشا کرد تا زیدیو تنها نزاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96058" target="_blank">📅 17:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96057">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0cd7304b.mp4?token=qFVfYeisgdOOkJSRpi6pzvCUmoMZb_XfcPEWxbgd9Bk8fSp50Ca9Q9wnJGzj1CpKUq6gxOekWgXh-LMNekQ4oqvbpiG2q1J-yXrWybTRAvdkG1VmqcLOp0NuNZ0sLrudlF2C2a1e0S4dbj31JY-rXd9bhgRbFH3S290qba7kSuAAZvFF2VOlKE-NjpdnSFAtKrUYERTJf1uZs-8dFLyN0fZ2k-U-OxywEFb_OwhqHQlDN5Bpia1BYe2au7a4wWPe6heMJofPcmrZhDpzDkxp_g6MWOkjGR-MTle1qWmwSKhedD07RYdYpvYYww0wVkIwZAX_QEM6mL35CzrKLc2K1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0cd7304b.mp4?token=qFVfYeisgdOOkJSRpi6pzvCUmoMZb_XfcPEWxbgd9Bk8fSp50Ca9Q9wnJGzj1CpKUq6gxOekWgXh-LMNekQ4oqvbpiG2q1J-yXrWybTRAvdkG1VmqcLOp0NuNZ0sLrudlF2C2a1e0S4dbj31JY-rXd9bhgRbFH3S290qba7kSuAAZvFF2VOlKE-NjpdnSFAtKrUYERTJf1uZs-8dFLyN0fZ2k-U-OxywEFb_OwhqHQlDN5Bpia1BYe2au7a4wWPe6heMJofPcmrZhDpzDkxp_g6MWOkjGR-MTle1qWmwSKhedD07RYdYpvYYww0wVkIwZAX_QEM6mL35CzrKLc2K1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
پیروز قربانی: احمدرضا عابدزاده و ناصر حجازی از لحاظ قبال اجتماعی متفاوت بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/96057" target="_blank">📅 17:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96056">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ekhjmqr7XanedVftLD2ISQKPswU6TxviQXlNGvWLnFkV06c8KIPVU-cNd2f6BQEfPmEMMkGlNC5-wJjNR7NlRJ3caRzx9rUZl8y_EtkY54H22ht8r34KbDluHaWXvRFyRM8d7XuSWeTWshP6zfwq8K01XvfGmLRL7c966r7FLi18XkB-6kMvqH3FiGL1jP6LNqHGPhBC-ixG0nDvr1iemlcGSmjpMIFZFBuhdhqvIhoEZCHfMUW_C6lyYjUrI91e9Tq_VLpyMXk_dUrptVGlW5KINMnW_StdVZwG4jjiU-Y3mO81FS3ObyCIyxDJjkLzpfvbmCKJNPIuTC9KyGG6-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رده بندی‌ خلاق‌ترین‌ بازیکنان جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/96056" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96055">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DKw_aC_vILnWhsrYMRHz-wR9ZuzqCLKdjQHSGTUU8EeP8vCE59IFnoEwpWeM9e3WmiiWQ85V2ZYbLKYn_N222gFENZh6z5H04e2oApAvyk_4YTniuVr7Ag-gmOe5i1iJjixZRuWt9caHMMagbIIz4Al6hxAhLc_qBu5YMge2Xz4wByxyvvdZGgkphUBXMxj9prc1m6pF3euvBUCkYje9k9OizSd1iwW1jN6KxafzpaCgwWCkF5fb7H6lzLi6jrSJWR9Bs7ZDiqoCL7I6ORFPdhO2SZ83dE_aIydWE6E87AlGDq-1OHh0R3Xz40CcDiCzUTSMIWcptpW7n0Jc5xhM5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پرجمعیت کشورهایی که هرگز به جام جهانی صعود نکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/96055" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96054">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_NqOQc75e9KEC78gJyYy82kNlc6gXWEzTA7HmvyFlTDDyJrxead--NttztLTYVBevxF5-kQpA8Upb2b_l_lDrI-EC0L1ZPBgHa6-90XFLQpH3mwJyWV2Serguwm4-zuTj5DlZ9iqZTsPr5zy95Sc_rI4Yr4qEPg_YBvSdsBO7fLfxioAYu_HbWY50abm4UWc5KG85JLbVqMaJ-b9RMnbLmpNMDMqOUOMAYZ38IghMR2QI2TNhViI19BsNhgZ7fDc2au5Yok9Qf2cdGEsk9YPD_U7uWD6Tuv5vHH043W5wI_IegpDLsEl3K3cGyj9Rkg0NUl0fEQasNbbKdCRpTTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه همراه اول به ایرانیان با صعود تیم ملی
همراه اول در اقدامی ویژه برای حمایت از تیم ملی فوتبال و همراهی هر چه بیشتر با تماشاگران بازی‌های جام‌جهانی، در صورت صعود از دور مقدماتی این رقابت‌ها، یک گیگابایت اینترنت رایگان به تمامی ایرانیان هدیه می‌دهد.
در صورت صعود تیم ملی فوتبال ایران، می‌توانید طی سه‌روز با مراجعه به اپلیکیشن «همراه من»، بسته اینترنت هدیه خود را فعال کنید.
تیم ملی ایران، شنبه ۶ تیرماه ساعت ۶:۳۰ صبح مقابل مصر صف‌آرایی می‌کند. برد در این دیدار، صعود مقتدرانه و صدرنشینی ایران را رقم می‌زند. در صورت تساوی نیز شانس صعود از مسیر تیم‌های سوم برتر، همچنان برای فوتبال‌دوستان ایرانی زنده باقی می‌ماند.
همراه اول ضمن آرزوی پیروزی برای ملی‌پوشان کشورمان، تمامی مشترکان را دعوت به مشارکت در پویش پیش‌بینی «جام‌جهانی ۲۰۲۶ در اپلیکیشن همراه من»، امتیازگیری و بالا بردن شانس برنده شدن مجموعه‌ای از جوایز متنوع کرده است.
http://mci.ir/-VK6ZFX</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/96054" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96053">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffafe3e9dd.mp4?token=nJpZ9y8RXRLkhSOnW_AcjL86Nr_c3hyuTMLch8VJEduYIPil1pDT5ecOrpCyVm6w_M7G4Uprew4pm5AtuWMGn88n7UfBjlgLfHaFpO8XU5X5p1Bm9hT15WlgmQL_4ikpcOjVta2cLprDjYr2AXg8ldXQJXW3Ru7F5b0Kutiy4DpsuBtQPKigGjtHUQQTZ8RWAg-BEfrWV1W4g_JDQEMkp3ex7K5yic5SCJrMuyrhx4BTineoag-koTniiI8NcHtLUS3pSttEdtU99CumMPKPqy3ugaeDBVJibitlR9Alw5h98RlcCpGIBaJa_rTbQXynhyUn2o6o1_3t2m1KOkeklA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffafe3e9dd.mp4?token=nJpZ9y8RXRLkhSOnW_AcjL86Nr_c3hyuTMLch8VJEduYIPil1pDT5ecOrpCyVm6w_M7G4Uprew4pm5AtuWMGn88n7UfBjlgLfHaFpO8XU5X5p1Bm9hT15WlgmQL_4ikpcOjVta2cLprDjYr2AXg8ldXQJXW3Ru7F5b0Kutiy4DpsuBtQPKigGjtHUQQTZ8RWAg-BEfrWV1W4g_JDQEMkp3ex7K5yic5SCJrMuyrhx4BTineoag-koTniiI8NcHtLUS3pSttEdtU99CumMPKPqy3ugaeDBVJibitlR9Alw5h98RlcCpGIBaJa_rTbQXynhyUn2o6o1_3t2m1KOkeklA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: دوست دارم بازیکنای رئال مادرید در جام‌جهانی ببازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96053" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96052">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45704079cd.mp4?token=cFvzOxucVVEQe-ETPMDN1lqT7Uo0FL0LQLhi1BYE-BmKLsvEACvkTMvk5gYedQWdBtB-5gX0l-j0frLGYeKW7JYLGvbu-y3dUjo1UXRLTril1f4wnH8UIs0zGd5QlpxHglKGUakXYUWBrJdh-KhAkY7fcFoWXfP9ImOVL3lBQPg-52Tzz4RuNM-fqJ-DRqxW71JITIR7NCl0Xa22nT0WbHsN1LNQ2kCjsV12-yS6favGsAb7WkS78QLfGdNV9tiay5xpgOpa9V667TqS9kqp1ForxrRr0QMYxFHk_UFeKUIOahQ3awOevOB9CrPJ2VXZltlmSji_A8RgLHmziCSI7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45704079cd.mp4?token=cFvzOxucVVEQe-ETPMDN1lqT7Uo0FL0LQLhi1BYE-BmKLsvEACvkTMvk5gYedQWdBtB-5gX0l-j0frLGYeKW7JYLGvbu-y3dUjo1UXRLTril1f4wnH8UIs0zGd5QlpxHglKGUakXYUWBrJdh-KhAkY7fcFoWXfP9ImOVL3lBQPg-52Tzz4RuNM-fqJ-DRqxW71JITIR7NCl0Xa22nT0WbHsN1LNQ2kCjsV12-yS6favGsAb7WkS78QLfGdNV9tiay5xpgOpa9V667TqS9kqp1ForxrRr0QMYxFHk_UFeKUIOahQ3awOevOB9CrPJ2VXZltlmSji_A8RgLHmziCSI7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇧🇷
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند - برزیل و دوباره زلزله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/96052" target="_blank">📅 16:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96051">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-hiRxG3gpnBRnMD7bjstafJWhfVoeM9iSCAaZ7TNWP3RQLoOuRjTT8woa-BFHebEhHNkU7V4d6WTRtZ92hPrYbm-akjZgvbd4JsGpiirDrd-gazKc3bfAz0j2XAusThxVxneXU_oPVRRylEHDeKceZLExEzL9vVa_jDp9nnVMa_xS1v-LV0rD-duGp3t9NoYCYIDTUYxhMI17JgZjdABBItOURaSzNZhS4HLBy6KlzZZSqgloqcMeJPI3eZ-8SXA2EcRXM-OKJKTB4lc69eJ2dCKg7B8W949o92E1r4JRriBR_pZ3Gd-4MxpjIOiPjb8wVqMhAZrYt6enWZRbtSWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتو ناگاتومو 39 ساله به اولین بازیکن آسیایی تاریخ تبدیل شد که تو 5 دوره جام جهانی حضور داشته و بازی کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/96051" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96050">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vnu1SK-Jyt-CA2YGGjWb_WUw6aKjwnvxffdAvb9zyGpku8KKY8gYlES_zwVorSVUl-ziddWaXL95qgidpPO4ihUY-fQQTC_ZnRdM9pZR39IaXWqB_UzXNeZFsfPj9sY4BFAsrhV7WrQZzaEy933ADEU-rahz84EEpW9aKaK7IjLylev2Ny2sv1hiQbd8oIhJs-r2wtwMPOIoCKBlrOv9gBlEwt-yHo45RTUNx6YPjO7aBhs_WhtrMaciBBG4BQMY_bJMNhJXtRElBnUOPrtEmM8pvp6KLH8SqyOZgHw0eFCJMP_rFtjfGX-DprmFEIpQ3rCd-ntX19JnBkdNgq-9Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
💥
سرویس‌های مولتی‌لوکیشن موجود شد
💥
🔝
🛡
کیفیت - سرعت - قیمت اسثننایی
🦸‍♀️
❤️
🎁
فقط و فقط گیگی 8,000
10G
▶️
80,000
👑
20G
▶️
160,000
👑
50G
▶️
400,000
👑
🔥
بسته ویژه:
⭐️
100G
▶️
600,000
(فقط گیگی 6,000)
🛍
حداقل خرید: 10 گیگ
📍
لوکیشن‌های متنوع و پرسرعت
🔗
همراه با لینک ساب(برای دیدن حجم مصرفی)
👥
بدون محدودیت کاربر
متصل روی تمامی اپراتورها
🛜
🛜
🛜
متصل روی تمامی سیستم‌عامل‌ها
❤️
🤔
👩🏻‍💻
جهت ثبت سفارش و خرید:
✅
@Trust_VPN3
تست رایگان هم موجودِ
❤️</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/96050" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96049">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VweBvNy4ryHIRtuTGhWF3toABAIbaTgFiUJjlmEIiv7kTrtKIqSDgrFsJt5WQv7qVC_eCR8Uq-_mRxSukkkywWHoWxikAmCvpjfHhzyBQBAJJA9TrAEiWgzz-WeleZjB2w6uOQiusuLW1sdfAfGRwbe4dhvZtt2Et49d9Av8hfmqWMqQ6uaZAztUUR_oPDOf8JWR7NoDEwTIf2JIhOsWl1km6YQ0n_MLNDt5DtNpLFOEGHWdOoq83hx7yWX1lI7eYE_ZsmBLchCVrCp3bsyy1_vnw4yjkaJEVu5apgtscmxpeE0-cJQ17HUKhyf0u7H8SbmDQ2fJgywFMqvSH4AdhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گلزنان جام جهانی 2026 تا پایان روز شانزدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/96049" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96048">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sr4ww5sBFuq-rXBGBe_rrjio8os-Vt0UNY0PsCeCwvB98RZoGUvsJwpqENFWJ2BwWuiFbIm0UoBetUA2M9EoIao5jQ8u1gZosfLh0MkcIjtO9chFudqVBzDmG10nljKG54n81RmXFuuimy3na0jhmQGbncbZ_MFZ8upj0Go-hrctOWWLhliLxNACZtkCoUbYmTUix76ZzvjCLR7P9IsQ74axOvx6rDcKueCIw7rMN38oiUtQmp0jsFW8WzxwucCdInk6YfXdRs-M_4QCFLpvKu-FzPILeUgWVzHl-IMzyrOV5s15J5086AqANrSiF1o8mTp8Kv4zd3PZu3-zBIViNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیته سازماندهی جام جهانی، هتل تیم ملی مصر رو با پرچم رنگین کمان نورپردازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/96048" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96047">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/96047" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96046">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=PMMc2Nctw0GcoyrP6aOGxU59fefW1LyeBTVS8lro4QJMKm9dG2kHQxIktfVSCPPiiBLhPDXshYDnyqDZETLi-K5rBFfHXXf8HNUtyz2l_cSvLLIfLOHsMlZ-gfXt2pDgWOw5ifzI8lbZuyX1eW-tSXnNe5MGkvTbOLUB3giV-oKKAgof2Ffz3IJdTEc4B0mUyyWW-9ZxgrtCCg7frPxeamSHWwl5jqUID4-ysr02eWbZYzupPfMVaoNt4TOlI3J6yby6_Om6jX0O2l8tJ4u9PXHqIx0v6fdGowcnDjKR1IBINy9k5vRnwB4pkKpCDy9nTQZk2OPfEj3QlOfEeI3dlC6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=PMMc2Nctw0GcoyrP6aOGxU59fefW1LyeBTVS8lro4QJMKm9dG2kHQxIktfVSCPPiiBLhPDXshYDnyqDZETLi-K5rBFfHXXf8HNUtyz2l_cSvLLIfLOHsMlZ-gfXt2pDgWOw5ifzI8lbZuyX1eW-tSXnNe5MGkvTbOLUB3giV-oKKAgof2Ffz3IJdTEc4B0mUyyWW-9ZxgrtCCg7frPxeamSHWwl5jqUID4-ysr02eWbZYzupPfMVaoNt4TOlI3J6yby6_Om6jX0O2l8tJ4u9PXHqIx0v6fdGowcnDjKR1IBINy9k5vRnwB4pkKpCDy9nTQZk2OPfEj3QlOfEeI3dlC6bmYClwXArweG4pJTpZugnVwJV7a3STV-vsNZK-h58x2PZsBWEijzis63C7qtprDjha5Lw7Al8RIn_qylsVH_MDWQ6RtGiKdniUenZyhQb2BPAphA5VTccidlUrqIOgIFcWaqPPehu37ldi55A7hoXK_1ADq4dYu-2GFARjlYXN9X64awIlskk2p1Pw_nUnwhPFEkLzNlMJMvT3dDHmgD39FNCDWIooPfJt4061PqJIyt_Uox_tDPqSsOAHv3WaLOPw336lA0IH-bj2m2_9WXvRddDpopU1uNniuDmyi2s5X83GQI5D2DwYaW6f9hfhr865Wf6aX-7Rg5d-mpGWYM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96046" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96045">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15632d71c.mp4?token=VlpjbFr-10aHMc7IfgPlm4QJ46ZQrYEkuB73u-Q9UaQ5EkyGvrJTCSK18IyagehE5FQxEscnSqZLnhs-7irrnQFNMPFBEvFDHVLy0B6g9kpfajle4TnzkoA27EEH5Tx6AwuzH0X9rwVNyNJj1DsqvDOQ7P62hh-1eU4MjG4bCjKQFigK96vp4Iqael2LSgQaMWwT0EQ7gW8njoeo3G6M5tLBZviNosp-hgxtEezB8p51Ay2mLTAb4HYSZibVfqFSDkNssjmCU7F5BvdC5qrX_cmFBdAOi5oJKpXwRo_tdI7FSeu9wQ0EISef2E6sxbni1bPAWTMK2Z8qI4tjz2lLHoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15632d71c.mp4?token=VlpjbFr-10aHMc7IfgPlm4QJ46ZQrYEkuB73u-Q9UaQ5EkyGvrJTCSK18IyagehE5FQxEscnSqZLnhs-7irrnQFNMPFBEvFDHVLy0B6g9kpfajle4TnzkoA27EEH5Tx6AwuzH0X9rwVNyNJj1DsqvDOQ7P62hh-1eU4MjG4bCjKQFigK96vp4Iqael2LSgQaMWwT0EQ7gW8njoeo3G6M5tLBZviNosp-hgxtEezB8p51Ay2mLTAb4HYSZibVfqFSDkNssjmCU7F5BvdC5qrX_cmFBdAOi5oJKpXwRo_tdI7FSeu9wQ0EISef2E6sxbni1bPAWTMK2Z8qI4tjz2lLHoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
ارتش هلندی‌ها در جام‌جهانی؛ حقیقتا پشماممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/96045" target="_blank">📅 16:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96044">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkRzx2NJQ2-7MEluArPzGvpzinnGLLQBxiVTuF_O4f7zFvWBgZLQGgMYLUHmO_BdrP_wCRkDsYcfKB6_DlwOvYhYPookvGn4JA658vZlC9SnQkI7QMiXLz4lcND2cJ39wf3WwzkXjDdULrRp59LLx5FdTenIGL1jWkFsI_8blZauD92nuxrYNvove2WEFs1pGKhG_ZithBfSSTeSKREQJZ_En8WDbphTNjJrY-RSpEvd0zWf6pf_XWFd0oa09TIxRC3DOYeaep8juDXzYp0p2yz-ntJ9GgrEL2H90589lZxU450s9Fm3o3LyLvCBnr_GyS3EeWSstDfSfg1KgphDIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کومو با رئال بر سر خرید دائمی نیکو پاز به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96044" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96043">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u7trhZmdNzQOrDZrxK8nQ-v4bfQ5Y8YYX7HHpImLN2al1J6OCdH-X6Hd2DIRj0NcL2KSTvbqJLpBI0JIUiSlCoP2Zo2rGa1kpufX7GErlmkBMDE0XlnSM8fLMc_oUMaKSJ_7wvsWtpq3YsBPdH2WdgVIupaS0KjYAFZEqcr3wVG0W68SA15PZduxn1dVjVdS13EQ95QTiTDAipTAgLb7zt-ykowNeUeOX_8q4sS6mBnT7bGa49vh10VuX0CNjTP2pR3PWXSWhIcGYkq9HFhd7RJ5K7IGKX6wOaDScpl5amroLH28BXlSSzt_HD5BEOHGf2ywGrco1yawndK6q6l7fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنان کدام‌تیم ها در جام‌جهانی گل‌بیشتری زدن؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/96043" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96042">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1pAfgFYvEqRsJbtgVXVo5GQA8XVP7cniwsCKQnyKlF93KgFImWtX0bO-nzK0jg92atH8eLgs9skqDc4pD_UaTStXA2kBeosA-4kWqxtlZ1CXHFwVv4LftRnREuwzJPfV-qnUfy2T4017k6EUS2gYkIIqUHgNzl-Hrp7lFTe-47qVjIICJcQ5Gj3to1oYld11lfZSXKMBtDvMli5q9Ej_gNukg27av3qxqz0aNyaffV-tnp9SsXQmmdzVaxM0fovfABF0l3zhdijZfmQRYY8XZi-P-9SYyxBn2Sx9eP1vOwfaVt1jriUVchMgP5BHTJjsyUj3Ih8EgCehkjlGHL4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🏆
🇧🇷
تیم‌ملی برزیل در ۴۴ سال اخیر همواره در دور گروهی جام‌جهانی صدرنشین شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/96042" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96041">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c2067f79e.mp4?token=ElraGLgr2OLL7WhQDOEfCo_mX2X_qRFE47dlnG5GgipLey-D0vUcOXRjg26oT6_RwRMPPoPHjOwM7-4ibdTymVwmme8I_kJt0eqZ2QCpVMm0EdTzKok1b8OigKRgoRTRJH7q8gOpeU3alOOzlWjYK5a644GoB5ZcpMVbH9RPgRRlliCBon7K0_65tjaertxZmg4aY5Sy0RswbwGk1apD5SQOVDjbsYCAaANCKq-DOMEZHJHwSYa6HfFKK4CdBn3jPi5ojaOUbLmzlgZSOhKJVarUNRrWEpLAms3cQUb10s3XUXbdbZ4Rf9_dTfMryC694xcgcgr37YM2TCoYTa666A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c2067f79e.mp4?token=ElraGLgr2OLL7WhQDOEfCo_mX2X_qRFE47dlnG5GgipLey-D0vUcOXRjg26oT6_RwRMPPoPHjOwM7-4ibdTymVwmme8I_kJt0eqZ2QCpVMm0EdTzKok1b8OigKRgoRTRJH7q8gOpeU3alOOzlWjYK5a644GoB5ZcpMVbH9RPgRRlliCBon7K0_65tjaertxZmg4aY5Sy0RswbwGk1apD5SQOVDjbsYCAaANCKq-DOMEZHJHwSYa6HfFKK4CdBn3jPi5ojaOUbLmzlgZSOhKJVarUNRrWEpLAms3cQUb10s3XUXbdbZ4Rf9_dTfMryC694xcgcgr37YM2TCoYTa666A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
▶️
خاطره بامزه مرتضی تبریزی از زمان حضور فیروزکریمی در ذوب
آهن:
‼️
سه روز مونده بود به پایان لیگ گفت تیم از نظر فنی اوکیه مارو برد ویلا یکی از دوستاش تو کرج باباکرم میذاشت کباب بازی می‌کردیم عشق و حال بود کلا. فرداش مارو می‌برد یه محله پایین شهر دیزی میزدیم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/96041" target="_blank">📅 15:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96040">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OINFAOTp4hsx8fCZGEBh-2ygqNdbuxsdiU-dhxOwj2hlJS-zRR3fIOvmi2xOvM4EwWMeYELWI-AiAY8609TrDYZI-N2n3tIrobbaDz1njs6BwtjLpewXgwh0lyDejNft1xrycw269gzVa5LQAn8b41s2KgvBoG_xaV1Cejpwlo9oLaLOXR1vSSIJj3Y2SIYkHhxjqJHlxE1NlYgrC4oGdQ04x1Gszgj8XOeiMG5TJCX5O_t2FXDp9JVIouFLEZg0m70uraorbfDNaGZPVpCK8rLacfuQesZx3G9lPr_4pK24Je8vT_fju9IQAUS7iTNLyuZEFIO8RpB6aobBrTXAEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فنای تیم ژنرال رو ببینیم.
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/96040" target="_blank">📅 15:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96039">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PZISQjxR4ZSO7iPFhR7rUf885mbSYbrZKW19rEfmd6Gtj0f4MJrxW-ip53ZJaXEst8rtqAG0cI1yXG1ILXkAA3isCsXx4dqyKnA7DpBj4cWFCBZUDrc707LgAhZCnnGWoByyVl8QxVCYEDszRYNvAB7Eex6UfebkXd8E2ZOz1spBarvbdO7NPXFaBu_RWf_CHU2zF46xd8ieuDNzDych9VHPM_xUksRS8uUknoMf-uM4yYoeTp8RLb5fWGJTFYaaaak373ckfZ6Tsapv7fCzOmjJlUXhOeePi2wneSSy9yKbyT4bR01fU0egTYe675RnZY-UlCTx8JT-dqlREld8mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇧🇷
ادر میلیتائو:
تیم ملی ژاپن همچنان در حال پیشرفت است و در جام جهانی ثابت کردند که قادرند به مراحل بالاتر بروند، بنابراین باید بسیار محتاط باشیم. آنها هرگز از دویدن دست نمی‌کشند و انضباط تاکتیکی عالی و بازیکنان متعهدی دارند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/96039" target="_blank">📅 15:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96038">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74737ca0a5.mp4?token=JNLHkNq0AjAt69kBcBAgKFEuKW4zo6BCPlNJnn9-9ROophSaBr_RXN29IxmTUb5_jpxtUS92nRTSkjz_ixYZX7n4zddxtKlzOTHZNeE3eKO7-EPDSBZXyZNXLmWoPj-YMrFFtVAKZ7PTA-y-lqcOlxQ5zonOaYbCSW6rM2h11lv7ehRWM8ZMej_2erqPIeFDLXfrZ5QIzbWvKVsLqGC56LZ_AdJBarPN82UUkGz75U3rmwJRaB5c535k-t1ASVRYrMXw_DcO-2BVRXvJLx8QCjfFldsFRdctKfxA-e2y6Y-ZF_RMBtk_lgbrXpZSlFo-SsIS1f4yj7TTB9oie4Jnfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74737ca0a5.mp4?token=JNLHkNq0AjAt69kBcBAgKFEuKW4zo6BCPlNJnn9-9ROophSaBr_RXN29IxmTUb5_jpxtUS92nRTSkjz_ixYZX7n4zddxtKlzOTHZNeE3eKO7-EPDSBZXyZNXLmWoPj-YMrFFtVAKZ7PTA-y-lqcOlxQ5zonOaYbCSW6rM2h11lv7ehRWM8ZMej_2erqPIeFDLXfrZ5QIzbWvKVsLqGC56LZ_AdJBarPN82UUkGz75U3rmwJRaB5c535k-t1ASVRYrMXw_DcO-2BVRXvJLx8QCjfFldsFRdctKfxA-e2y6Y-ZF_RMBtk_lgbrXpZSlFo-SsIS1f4yj7TTB9oie4Jnfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
▶️
وقتی الگوت لیونل‌مسی باشه بایدم اینجوری بدرخشی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96038" target="_blank">📅 15:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96037">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEtIyZNFp7Z_yE1o9NnTvboFUkSTJHSNMB_zY0Nr8JFzy5SzwX0KfNnmxCmAyKGRUsLaUGC2s5bAYks2Uxw5WLg_pEkpRUgih4NuTc9bWVt0NFCb-u8xfwj_v6ETRppTb_7WuLaz1vUduZt9XodcKuG_Pvb9KGd-u7lvTF9U89pjjABS-dVj5LJXCSJN0PzO3IKyrpV4TVIucxpy6-UZ78bnLhVgCcv23XhmjXWito9GVFlGxszmBJ6rvvg8_14hzY8cWFxSwCoVemhSdiEaohM9SQ4uEVnUB-xC7YQRUsQDtdHVjyPUS2lQQuP1HuFxG_flBb2wItN5AgQy7cRUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇦🇷
🇵🇹
مسیر مراحل حذفی آرژانتین و پرتغال با توجه به نتایج فعلی مسابقات
🇵🇹
پرتغال
🌬
🇫🇷
فرانسه
🇪🇸
اسپانیا
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🇦🇷
آرژانتین
🌬
🇨🇻
کیپ‌ورد
🇪🇬
مصر
🇨🇴
کلمبیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/96037" target="_blank">📅 14:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96036">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/96036" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96035">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95d3c29823.mp4?token=gs0EcbvcTi-y8xl1PAjZhkS-_HNAMhVRieaqxCTeGYI_Xjc3DIEaH0N8m7MxlfX8IEimZj4QuE7Q_uF5GL1q6CS-43PSDK3sRi-2eSiZRdgBqvqQedummSLpI5guyzovNIHxamPG5uJibfwROcHIpMK64KnmnKNjmV7dE6lVWhUCmHCqvLQRz5f7uqeY8muDIdc2mnZcfDiIDdBZ5lZbcSs7zgUx4sF75zYcOSprkiLdsyMlNnkzQwM0xQxPHdvB40dU8FYZcvSCy6GgIZGI8v-U5MnSxNA3LBULNZsbdZA7MT7du8AUE9e-pD2-iAMdH5-9-DejT0j1vgkCdda2X0ZqBuRtumi6Obj05NxVnQ1eyWzqC_rCBivrSD6UByTVRIV0Vw0ptsBnvy8yAxwF86cVXcdAS7Kz_nzcGA09KKDzOLsUmKeSQ9VPpZmye7BBTQpHOIuDIMbNYu1_LIpfkuStNGvWMrvoqmVGbl3p_U3HCBF7-Fj89ZANZgNiRFB1xu4GBzkA3UKKvS09WJIYLNq3DWJzbn-L-9mL-yrigGo86wyYngt3WYuXXjrzCbjcAuT3ePzwmIdOfpSLA4FAKkspYe8gtkAB34x9Jx8JE6788PRNYd0AAUslI9-kgq7Kx8J7uye0lLPLM12U0BBQ1YRB9lXUERvzPMLtTHORfnI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95d3c29823.mp4?token=gs0EcbvcTi-y8xl1PAjZhkS-_HNAMhVRieaqxCTeGYI_Xjc3DIEaH0N8m7MxlfX8IEimZj4QuE7Q_uF5GL1q6CS-43PSDK3sRi-2eSiZRdgBqvqQedummSLpI5guyzovNIHxamPG5uJibfwROcHIpMK64KnmnKNjmV7dE6lVWhUCmHCqvLQRz5f7uqeY8muDIdc2mnZcfDiIDdBZ5lZbcSs7zgUx4sF75zYcOSprkiLdsyMlNnkzQwM0xQxPHdvB40dU8FYZcvSCy6GgIZGI8v-U5MnSxNA3LBULNZsbdZA7MT7du8AUE9e-pD2-iAMdH5-9-DejT0j1vgkCdda2X0ZqBuRtumi6Obj05NxVnQ1eyWzqC_rCBivrSD6UByTVRIV0Vw0ptsBnvy8yAxwF86cVXcdAS7Kz_nzcGA09KKDzOLsUmKeSQ9VPpZmye7BBTQpHOIuDIMbNYu1_LIpfkuStNGvWMrvoqmVGbl3p_U3HCBF7-Fj89ZANZgNiRFB1xu4GBzkA3UKKvS09WJIYLNq3DWJzbn-L-9mL-yrigGo86wyYngt3WYuXXjrzCbjcAuT3ePzwmIdOfpSLA4FAKkspYe8gtkAB34x9Jx8JE6788PRNYd0AAUslI9-kgq7Kx8J7uye0lLPLM12U0BBQ1YRB9lXUERvzPMLtTHORfnI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مداحی محرم با موزیک واویلا لیلی
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96035" target="_blank">📅 14:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96034">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBT2tsnYO7nEKMuw5OswSm2sVrbP0PHPzuujOkcKbZxQ9_-cCoLFy3aiyF3AUdA6EkdbBsuSmwaROlsQSqYQ0DnKXieDNPINB8OfhP-9mI7AWbGB3pZeBOXy4ZXloYox4yP5qXIV7OUOOEbB5hwai7glDAnrdLKOlyH38D1YLwODxGlHOzVoo5RHj96aFISp0wEmQFzHW2FUhW6oqQGuE0q0io0ICCrI1ohK156zO1l4_EWiLyipxM_Afx-Nemhbd9vwWnI8VmkYJqjadJJIUIdx2GsO1srsqqAVvL4fkZAH6gC0Psu0aJBkjJXvRUQt74-mhhf6RBQY8PXO7IAESg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه هالند و امباپه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96034" target="_blank">📅 14:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96033">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=lt9XiEjUNhmiP70zGTQMgT1IkCCdIpyMaMm-xVTyrMWPMWm3mK08szuLLK1oi8JQOC8H2k-ogzA326yE7cgGpdCuXGn1QMp6GlvEvl-xevbCrnhlgHtG0wtiNkOR5hiOv8q5p4vZUMemECyQTI7w0iNnrNvBXMeAjB9PZvwt8L1A8ndlmvmfawVlO3tL0XWaIRaHcqN7MrQsB09zRFERgAwQa6JXkvoyhlzHhvQw40AECJmMfx67kw6GiWopYW9vyZsVhv3suZO9xZAVre79zC2Lj4ic4amL8LNFM08vMOCg_-hcdiffDOforV0SOc01H8tuW7bqDUFjt6X9JHbUpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=lt9XiEjUNhmiP70zGTQMgT1IkCCdIpyMaMm-xVTyrMWPMWm3mK08szuLLK1oi8JQOC8H2k-ogzA326yE7cgGpdCuXGn1QMp6GlvEvl-xevbCrnhlgHtG0wtiNkOR5hiOv8q5p4vZUMemECyQTI7w0iNnrNvBXMeAjB9PZvwt8L1A8ndlmvmfawVlO3tL0XWaIRaHcqN7MrQsB09zRFERgAwQa6JXkvoyhlzHhvQw40AECJmMfx67kw6GiWopYW9vyZsVhv3suZO9xZAVre79zC2Lj4ic4amL8LNFM08vMOCg_-hcdiffDOforV0SOc01H8tuW7bqDUFjt6X9JHbUpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
💍
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌کمانی و برگزاری مراسم حمایت از جامعه LGBTQ در ورزشگاه سیاتل
:
ما اینجا برای فوتبال هستیم، نه مسائل دیگر. تمرکز ما بر روی مسابقه و کسب موفقیت است. درباره موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
﻿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/96033" target="_blank">📅 14:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96032">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIA6j3uresi62fibCutFT4KqJ4WiDo3sOh4FURF5kAKvRR30rXGXcuFKRalNpIefd08H-QcihNStJLb6xB7e3vSLsE2xO5BiZ_pZgDyMBmHzRjftojRW2-TwfT0daAe87P-0tCnii7ypVVIHsW-kddzsDheWHpFo0Yq2Kmxg0nPP9B-XUtvIwiOlBD_GZFa1tPq0TtmHxpSdYu_buzkiVD7akkka6jvSLKIVWH_bDob6WbyDlXWHIWI_rIVr0jknOryMKJCQkqr9HQcCrX5cvTA-iQvrT9RDcEWrb_CVnqvj9UFrHRM5vR8WN83rtR5wnfTkF5mgD8-2RATkc14e3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
🇦🇷
پدری‌ستاره اسپانیا: دوست دارم در این جام با لیونل‌مسی روبه‌رو شوم و در نهایت پیراهن اسطوره را از وی بگیرم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96032" target="_blank">📅 14:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96031">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/21833a49a4.mp4?token=cuZYPZbkmE5ZLtaeYkG6Wx1U7eDyWoIWMR4vhDFcKStqxnvPxlQT0JWmoQrZBt0zWkVi7w3NdMri2zJeG3JD0Y3JHKCVBsmgtOzMI2HAhdk4GLC2rruFF0vwcyQMNwm29qkGYNClUDPI2yx2RpwhjquxJhNDBjCbKSTnkXYmi5yTdRkX28r-Qnpivh9y__hfkz6Fi0b6FjOXDqrEqxXeNRt47gkNqHBHQ9MooGDfgxCJ-kVzJ8X-0hUrVW32mfzo0QcsTlFTWNzWwO1-m1vc37Wamx8rj3PolrGRrTDxBl80JbzwCOH5y-8osBjpxnUmzZlnU_9Y48jTMPcKZ_zRiqeQxe-YDh0AfByHfW3-Ls0_mM7noli_BKhpN3CGwaZD-tLWqMpDrwp9Z1g9PLyBjjkNtDYKIi5-0DmZgremZfAGTQo_rmNn4AGwLZniWSofNzAlM5-Y_3wkU5FG9V0gxwBfF8nXnycnVdaeOl0TIVut-NbaSoFuKHbwxBQFvQyoiR1scVL-Owbh6mdrPae0-7SqnO9kKfm2xqo6Ck10t_sZ1o_6FoucVZETezECqm-N-yHCj4XqKlbdTQjoFwOkzrn4fieFcbTs2ThXS46hygkIrYsi-ouUhKPcskrxKT_S2z4r0jefPEryUm2O39P6tq91EGzHkHeJgwIX1BBTNK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/21833a49a4.mp4?token=cuZYPZbkmE5ZLtaeYkG6Wx1U7eDyWoIWMR4vhDFcKStqxnvPxlQT0JWmoQrZBt0zWkVi7w3NdMri2zJeG3JD0Y3JHKCVBsmgtOzMI2HAhdk4GLC2rruFF0vwcyQMNwm29qkGYNClUDPI2yx2RpwhjquxJhNDBjCbKSTnkXYmi5yTdRkX28r-Qnpivh9y__hfkz6Fi0b6FjOXDqrEqxXeNRt47gkNqHBHQ9MooGDfgxCJ-kVzJ8X-0hUrVW32mfzo0QcsTlFTWNzWwO1-m1vc37Wamx8rj3PolrGRrTDxBl80JbzwCOH5y-8osBjpxnUmzZlnU_9Y48jTMPcKZ_zRiqeQxe-YDh0AfByHfW3-Ls0_mM7noli_BKhpN3CGwaZD-tLWqMpDrwp9Z1g9PLyBjjkNtDYKIi5-0DmZgremZfAGTQo_rmNn4AGwLZniWSofNzAlM5-Y_3wkU5FG9V0gxwBfF8nXnycnVdaeOl0TIVut-NbaSoFuKHbwxBQFvQyoiR1scVL-Owbh6mdrPae0-7SqnO9kKfm2xqo6Ck10t_sZ1o_6FoucVZETezECqm-N-yHCj4XqKlbdTQjoFwOkzrn4fieFcbTs2ThXS46hygkIrYsi-ouUhKPcskrxKT_S2z4r0jefPEryUm2O39P6tq91EGzHkHeJgwIX1BBTNK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🏆
توضیحات هوادار ایرانی برای جایگاه‌های ۴ نفره و مخصوص جام‌جهانی به همراه امکاناتش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96031" target="_blank">📅 13:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96030">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72c892433e.mp4?token=d4SEZSumTzMsBEM8WDTCEJ6B0p7vKykrK57TR9cIXwHXeip391FqGAr-sKG0jUpozTjXGchOGtZqAhvh3b9UV00ElePYvmlwGhNw7p53Ei1F496Ofc9sM7vMBNr-igYd-Z1gd2-gotKgQL4mZg4JVkZvF9SOcDJDu9zbBTJe4NgP2V2z_3lfwKkMJoZ-9IXhNOVx2ag1fSva3e7zcGVX3hP68ou0X73G55fRlndYz0eblQHg7yITj2nfpSkn49ltFzaUtgCZYsHMsUvWUDTQqNGcD3VkChfxPtMuuThPFKVpQkJc4y2NMR5BI79SnSylLS55jcagPzRmkXnQ77WB3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72c892433e.mp4?token=d4SEZSumTzMsBEM8WDTCEJ6B0p7vKykrK57TR9cIXwHXeip391FqGAr-sKG0jUpozTjXGchOGtZqAhvh3b9UV00ElePYvmlwGhNw7p53Ei1F496Ofc9sM7vMBNr-igYd-Z1gd2-gotKgQL4mZg4JVkZvF9SOcDJDu9zbBTJe4NgP2V2z_3lfwKkMJoZ-9IXhNOVx2ag1fSva3e7zcGVX3hP68ou0X73G55fRlndYz0eblQHg7yITj2nfpSkn49ltFzaUtgCZYsHMsUvWUDTQqNGcD3VkChfxPtMuuThPFKVpQkJc4y2NMR5BI79SnSylLS55jcagPzRmkXnQ77WB3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">متن حماسی که در اتاق همه بازیکنان تیم ملی نصب شده است
🔹
در تاریخ فقط یک چیز می‌ماند، آیا ایران صعود کرد یا نه
🔹
چند روز دیگر هیچ‌کس از تعریف‌ها و تیترها حرف نمی‌زند، همه فقط می‌پرسند آیا ایران صعود کرد یا نه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/96030" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkVzbrV5K8NKNwgh-Owa0TeODn151vwPEAGe57wYHokc7ndh9ZWlTKetR6JZa9tXe35W1dx57V2FBQkR7MECLf3k_U13PpukzL7GgnQgNiIRCt-VNzEqY5H85EEix0XZBKK9B2qd8t6y4D7R9yclUaNh4KINhWToPktd5k5tIBwiIDheEo-z4Ndq5w4y6Yp-QQDBBR-W0eU1G8YLG9_vnYJZw6Yy7npRW5HN77rp1CcdfOdbsLf2mIYhYkzqh9ON34bTlF-Ts2jSVshyh-c0vc59exS_BUlnZcz8QkiI9_WqSylBQZu4dL6Gh8-uk8sW_v6t2tsRbGOQOfi2Ysw4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇬
🤩
💍
حسام‌حسن سرمربی تیم‌ملی مصر درباره حواشی بازی فردا با ایران: برای ما حضور یا عدم حضور اقلیت همجنس‌گرایان اهمیتی ندارد و فیفا اختیار دارد هر تصمیمی بخواهد بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/96029" target="_blank">📅 13:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEp68S5cqYMIVlA_EQSGXitBct8UeUVR4xjhgJzE5wFcOXuFv6djbzryKXT0jOuJFyWimVdiim0jAosWPsFPck2_dKQ6idxcmsFTaQjnVFuX38k0wRGwR2o0DX7zv1bR6UMNPproGpUhvR1OzP7VYpdH2HfkMegmTQ8GuO59xR5z-zp6UqgYQ6BBVu49WIDGhzLLWXSX0EUWTO3VMAka5ULC8uWTzLDw0_RAgsqWhve2bfCHCna-zoFwt-hRloApN5j_HciVSCq_w6N9Dop3ls1T7UZcaJ8rEiNaf3w-qAKG1JvJmVeqIcKDCn9KaP15B36jJ9WFrPizsQb025HsSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
لکیپ: مکسنس لاکروا ستاره تیم‌ملی فرانسه پس از جام‌جهانی با عقد قراردادی به ارزش ۵۵ میلیون یورو راهی چلسی خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96028" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sG6r_ZFNkURetAO7Of5r1SZZTn8wNXrpWL-0p048CbBSFe0KfJ1JFVcdQitzb5GSMHRQ3Pt5FgszlBK6CPwq6TLSI7UAKEZ2djH2akiO-6QjoKL3pK0YeN7kltCvtHfRFHcyu5nP4zBaoB014gXGMQSyYH5wsUJr5_m4uXRUa5n1JXmnXpeYThqpibk5zq0mqbWHypajD6F2cK3B2xIqzGfiJq_I3wvLCC06ap8xKGjKtLgjhdbFKEYIeSnlIlTlsqoeLW8UKSA1I-LvPgu18j9lAMcU7t7vd0Vro-6uW5rtGfbcJhIJerW4Ln7OqUJypb9iQRP5JMDK8iKdK0hwIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
تصویری که لامین‌یامال از زیدش منتشر کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96027" target="_blank">📅 13:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8aae82768.mp4?token=P-KA8VLumyzat6SOndhpWP8wX0FAshP_IjMT0CXQ5LUCISwPvuQ1soLsx_WKGFR9-lDtwJHid8dZZU1FY94NUZiR0IMJ4L8DLj_nq9QpL2BVhJM8gVmEZOzxzCXm72zxwu3FTnHi8lvZb-UHSfZkxNMH9CPlLzPkXh3gmk1cHFB3w27UC2VFEiCouDw6wAz0qlbZ13cNF2SgBjJ-cAZkVLtJKnK2gQ2Ihc8WS9ctwEMWDDwI1YOI35SD4uv5nPjOXeNY7RhP4c8977AVx9lft9sO91zz0z_snF_Ng_kmqIlfWCkwXjZdJNaPmuf9skqq-wEgpS-n8DZWYmeRZt6BBk-kB3zkIY6apZVvJ56CKIxjIkFzY7uzwowJzLrF0Nfra1jlVog79CC6V9bri4TjGEj24Feqv-Ko7a50X65YMTgOy1tAa7lF3afzlRUrCCUUD9TNuFFC-Yf8oggEsHASLEmDQWS_9VBJmU5uUtzWOfcD_QXGFUd86QlnJ3kdtA3G6GsHFl0eLQMoaqmmBslQvvmPnLeHUsEkE-0zrCxkTTP_cQEEyaXO_D_g20S2svqATgao0C8_W2yxDTFBCii8VgBflZT7fgltQphubG-O5CyJCq_GdPshILOb22fKGv97VFeH2IlzQTog0fx6NelWZdwviGEnOSJ5__OlHdYGgb0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8aae82768.mp4?token=P-KA8VLumyzat6SOndhpWP8wX0FAshP_IjMT0CXQ5LUCISwPvuQ1soLsx_WKGFR9-lDtwJHid8dZZU1FY94NUZiR0IMJ4L8DLj_nq9QpL2BVhJM8gVmEZOzxzCXm72zxwu3FTnHi8lvZb-UHSfZkxNMH9CPlLzPkXh3gmk1cHFB3w27UC2VFEiCouDw6wAz0qlbZ13cNF2SgBjJ-cAZkVLtJKnK2gQ2Ihc8WS9ctwEMWDDwI1YOI35SD4uv5nPjOXeNY7RhP4c8977AVx9lft9sO91zz0z_snF_Ng_kmqIlfWCkwXjZdJNaPmuf9skqq-wEgpS-n8DZWYmeRZt6BBk-kB3zkIY6apZVvJ56CKIxjIkFzY7uzwowJzLrF0Nfra1jlVog79CC6V9bri4TjGEj24Feqv-Ko7a50X65YMTgOy1tAa7lF3afzlRUrCCUUD9TNuFFC-Yf8oggEsHASLEmDQWS_9VBJmU5uUtzWOfcD_QXGFUd86QlnJ3kdtA3G6GsHFl0eLQMoaqmmBslQvvmPnLeHUsEkE-0zrCxkTTP_cQEEyaXO_D_g20S2svqATgao0C8_W2yxDTFBCii8VgBflZT7fgltQphubG-O5CyJCq_GdPshILOb22fKGv97VFeH2IlzQTog0fx6NelWZdwviGEnOSJ5__OlHdYGgb0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🏆
یه خانم‌ایرانی خواننده خارج‌نشین برای جام‌جهانی موزیک‌ویدیو ساخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96026" target="_blank">📅 13:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u1W1nJAwDjVMnJqmOnKNJJMVpRr_eNKMvmfqvPzVytxeQnNrQHwvQr-vJ4nDR5Df_Pd5ga1PYsX5PfsqrNsd2rRkHbXDUZ6qg2coi9E1qbLyIQwzkMmNGMJcNnXbkmenoONUbgbP2sFayprW6UNt6ziB5nuq3ya5mnQHPj6vnzhMUUqNFKP0riS6ZFPrkcAlVKe6X_xbvn7wdSXa528qU7onv4o4wsDOuaemwWz5HcUU5XaIPFLbb5RhxZ6zD-hfqW2ACxTkZVaZTGiAk4o0gWKNwUX_FdCqm-tUbVm_jh9-Co8EDUzqWriicB1k0d_95lAAgkaSv17QLU3bebHOXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💍
🇪🇬
🇮🇷
وضعیت‌سیاتل آستانه بازی مصر و ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96025" target="_blank">📅 12:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96024">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53bad2b136.mp4?token=rgHAVoBA-S0F9Gm7ZgKDZelDXdbF0buUAsirth8AT9E418tHCsYCFjPhXAqEXhZvURKhIF5MrIx3HqavjSlBTSDbZZaUxmqfeZhYlqsjbVQSpYUJxjoo-8YQakdC4EBvKzmh104sAAGtuhBLXfSYUIWO8ufsEvJlMcJkqf83XoI8Zg6CjuWYOcXbs9upbqSIYowFuV1vGTmfZAYHFIO_Eoxe2n_PkyY8HgyX0nFMy-OrFTk-Mdc1bBndzVWZEDu-UQd8G7aZYdMvA5EVbCeNk_-bDjmvy7meahpVzT-efSW9WPh_G4_tz6GjPLhNNiVkdtTgs3dnMTZ3rSQj-ZvuLmx2J4MnLJVXoih53o71811jyWzxhi7_Ks0xesJuLIVElV5Zk_hODkZ0CMSx48T156CedSZGIu7zauQ0_Taij-1N6zre4JUWNUuG9LyjuLWzdvxubNUFsrA5p-VehynGJg_u0VAuWeC7GB2aKAhpxg3SkOHaQQ5Xjh9dETF9r5o1rtwK4AV1trZFHwSYISoR4XLIuXnKlzukys7r2lCQiV7wPlaWcKulFZX1O6mEu9ovJEvSIhUDmuCIC8tm7_aZs79cjBRBafHmPPYfNTEBaPr_cMp4sQpGoZJEnxgtJVujNDTgQlzCSsozrGsvmfD-aow7aOeFkNmsr_W9XrxjLHY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53bad2b136.mp4?token=rgHAVoBA-S0F9Gm7ZgKDZelDXdbF0buUAsirth8AT9E418tHCsYCFjPhXAqEXhZvURKhIF5MrIx3HqavjSlBTSDbZZaUxmqfeZhYlqsjbVQSpYUJxjoo-8YQakdC4EBvKzmh104sAAGtuhBLXfSYUIWO8ufsEvJlMcJkqf83XoI8Zg6CjuWYOcXbs9upbqSIYowFuV1vGTmfZAYHFIO_Eoxe2n_PkyY8HgyX0nFMy-OrFTk-Mdc1bBndzVWZEDu-UQd8G7aZYdMvA5EVbCeNk_-bDjmvy7meahpVzT-efSW9WPh_G4_tz6GjPLhNNiVkdtTgs3dnMTZ3rSQj-ZvuLmx2J4MnLJVXoih53o71811jyWzxhi7_Ks0xesJuLIVElV5Zk_hODkZ0CMSx48T156CedSZGIu7zauQ0_Taij-1N6zre4JUWNUuG9LyjuLWzdvxubNUFsrA5p-VehynGJg_u0VAuWeC7GB2aKAhpxg3SkOHaQQ5Xjh9dETF9r5o1rtwK4AV1trZFHwSYISoR4XLIuXnKlzukys7r2lCQiV7wPlaWcKulFZX1O6mEu9ovJEvSIhUDmuCIC8tm7_aZs79cjBRBafHmPPYfNTEBaPr_cMp4sQpGoZJEnxgtJVujNDTgQlzCSsozrGsvmfD-aow7aOeFkNmsr_W9XrxjLHY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇲🇽
مکزیکی‌ها وقتی ورزشگاه نمیرن اینجوری بازیو میبینن؛ غرق در عشق‌وحال و مستی
🚬
🚬
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/96024" target="_blank">📅 12:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96023">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🔴
🟡
دیدار امروز پرسپولیس و چادرملو ساعت ۲۰:۳۰ آغاز خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/96023" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96022">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b381fab19.mp4?token=UVtBevVlxEScRvucRYAAPXhhOb_a7foT0rDu1CnddRJguw-9yZ2Emt4A1TEB18-YSakvEYZI4AQkqSnaO5ii4Vb8VmJXhBsoeB41YRdbpIrg2tzw9AB_LwSCJCA7bSODWwGtvqxwHo5J020tCCAxdonPctMKyVaHe_dvCe6CLvYypGUP9AiPm8So1Pa6sdzPGAxUzrQ8qQC9hWswg1cUAAQbUgPF1_7v3t4GmODyfkJHY4rYgsagSPGiTaWgXIc2X6oZaZpYC7KRgoUi-3EkVkSlliRZTmLhnCkiSgCI4Mzy8gBoximQe-8JUCUW_NwzFSkzy5zd8K_G0-QmB-ikBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b381fab19.mp4?token=UVtBevVlxEScRvucRYAAPXhhOb_a7foT0rDu1CnddRJguw-9yZ2Emt4A1TEB18-YSakvEYZI4AQkqSnaO5ii4Vb8VmJXhBsoeB41YRdbpIrg2tzw9AB_LwSCJCA7bSODWwGtvqxwHo5J020tCCAxdonPctMKyVaHe_dvCe6CLvYypGUP9AiPm8So1Pa6sdzPGAxUzrQ8qQC9hWswg1cUAAQbUgPF1_7v3t4GmODyfkJHY4rYgsagSPGiTaWgXIc2X6oZaZpYC7KRgoUi-3EkVkSlliRZTmLhnCkiSgCI4Mzy8gBoximQe-8JUCUW_NwzFSkzy5zd8K_G0-QmB-ikBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
✨
▶️
همه عمر می‌توانم کنار کروس بازی کنم
مدافع سابق تیم ملی آلمان و بایرن مونیخ بهترین بازیکن تاریخ این کشور، و یک هم‌تیمی برای همیشه را انتخاب می‌کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/96022" target="_blank">📅 12:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96021">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZAQAplyZ05lsTXk8rs1wFtz3auI9xOjXaF-3dNQOeowUqkNtqFecor6_NjVrM7o7q95GCyrU4jVuGVXNVv96-tumPACxBPVtBS-BQXmWAtnVFFfZnsg64nhBBloZarD07P5J7iEvWZrnMKpsiD34RgEy4TXjoo-ApRKP71R5TyJ2YPVJDiWIOsSmAzooIDi38wiyKKCjsgf0JzMWBW2Z-3TmGbK_eKAiCfVOz1NOLkj2fhRtnvZYNAyyXG2yIItqhvp0X310-BX6s5EDkJ74r_5nY3R9Kk-dfrPIkRsmritsf-ByU4V_KaKkePoSk60mxmM87rc_A3T-SIsFBfxng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
#فوووری
؛ آرسنال اولین پیشنهاد خود را برای جذب برونو گیمارش به نیوکاسل ارائه کرد. نیوکاسل به تیم‌های خواهان ستاره برزیلی گفته که این بازیکن فروشی نخواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/96021" target="_blank">📅 12:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96020">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871d57299e.mp4?token=Ven-pOhFASDEIVi-1D-D93K2TbUYSKHT68yqCYBFyAsDikxYHFPbP2_W9h8naJAFXsb15aHnF-J7HYGHeLghiUVTHNrex_UMjYMAIxsIKUhDil24OOTfRJd7SHasjkw2E-Q0CDhyd5rtaZ0mhNiixPgkh4HvwSQg73BIvLSzRjA8B1CrfA_-i7bsKXbPVLLsFNqkG2Fe3L3-7zHyS3gZhS010LPoQHVMJSzuSSCD21o74SVJP0ULsMeQmDTSDs7ewIbYgRVjdDDt6T59MBrYNwV5B3exqKv0bUhNMQ-hnEE59lhoA15UywNT9MOTp3JyBcJwLK7AaWJvqZchQTf_bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871d57299e.mp4?token=Ven-pOhFASDEIVi-1D-D93K2TbUYSKHT68yqCYBFyAsDikxYHFPbP2_W9h8naJAFXsb15aHnF-J7HYGHeLghiUVTHNrex_UMjYMAIxsIKUhDil24OOTfRJd7SHasjkw2E-Q0CDhyd5rtaZ0mhNiixPgkh4HvwSQg73BIvLSzRjA8B1CrfA_-i7bsKXbPVLLsFNqkG2Fe3L3-7zHyS3gZhS010LPoQHVMJSzuSSCD21o74SVJP0ULsMeQmDTSDs7ewIbYgRVjdDDt6T59MBrYNwV5B3exqKv0bUhNMQ-hnEE59lhoA15UywNT9MOTp3JyBcJwLK7AaWJvqZchQTf_bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
معمولی‌ترین هوادار برزیل جلو اسکاتلند:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/96020" target="_blank">📅 12:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT5PEGW699VoqQNwqMw3R1_f2IH_j8ug7UOtzy_e85wcieo5C9vDcn73LHCZrvEwJ00_nH5U0-jH6LYv7c095VmsQMvUjLO9zkkKgHTBc46am85oE96Rp2rwvdjU1wdo8fvP0OVNmx7lZWr3HAk3ui4_9-csnKUYRUAzBJDzntljpVeki3kV32loU9tdeVqeP8D5YukSZtqwZfCOivmhnEf3Kw5RHnYsuKQ3LdzUcfGDATOp0v8riB775YY1phh5s2kamVAHJ5iAotuaoEnXzhJloXg7Omx0u_7okdezjz18s5D4y5dyBGRC9YZwzEpFw3v1VsCUaQzF-4TOlQxAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
🏆
🇪🇨
پس از برتری تاریخ مقابل آلمان و با دستور رئیس جمهور اکوادور، امروز در سراسر این کشور تعطیلی اعلام شد تا مردم به جشن و شادی بپردازند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/Futball180TV/96019" target="_blank">📅 11:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plu3nMe8uRoTqpY9DpMshLTqOB_pGCMo3LGfihwJ9b9jjFlXrgOyXkxqFFxriJGAx0MODTYDuTu_wq-51Nx71PM3-_FG-ciAbOiaLMNi3QiBeU-CmzgcDRydQRsZI6qMu9vw5XHhof4rCohytk4Snjm1J4JDW3Pi4LZ3TzdraMQ5-NQ6kkgV1l2ckxrQ_p7D7Zi1xEDvG0-ixnoR9c7E6K-Z9cV-LXlz6jxSJez8ITQELOUFHgPnW935H4E25xFW0VQTodoBzjUlgRUKHxR6XYBLEM2gST_2EH2Ts0uNIA31JDf8_gyWye8vV4g6ELf-yI-8bX4FTY8I8ykbDzyL0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇺🇾
هرج و مرج و درگیری در اردوگاه اروگوئه پیش از دیدار با اسپانیا.
🔴
اختلافاتی بین مربی مارسلو بیلسا و بازیکنان وجود دارد. تعدادی از بازیکنان از جمله [والورده، اوگارتی، بنتانکور] درخواست کردند به صورت خصوصی با مربی صحبت کنند تا به او بگویند سبک تمرینات و بازی‌ها را نمی‌پسندند.
‼️
بازیکنان از شدت تمرینات شکایت کردند که باعث مصدومیت برخی از هم‌تیمی‌هایشان شده است.
❌
بازیکنان همچنین درخواست خاصی از مربی داشتند که فردا مقابل اسپانیا با دفاع پایین بازی کنند و روی حملات ضدحمله‌ای تمرکز کنند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96018" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ab104e91.mp4?token=hYvUiaY8dttUmofq1Nsdw0nw7JDDOoHdxk9xOrm3w5bnSgw1LN9lvp07zww7MhLMI7saAwtV1q31X4-ZUDBSjDS9rX5qACDU5bsmNq1npzIeevys07XuwARQzt43a-hpi2WXN9geqOCcW_af2vCCeQAEg7ytjUNWkwtezq_GM3X07bD48qLlP3-mnm1oshyHVDV8ej97xvNwTQT0nxJOVvbBg6aZ0bGvkJlPjBFysVNCtXwzfN73vUb7zz-8fw8iDV9Yguuw8u61euhzQPjH_lthZpc63xiIxkcYkbDV-Z7A5K4J3zWPlJ8VOWbCj-zuo4jyebEXd-6_7HY6kHo2RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ab104e91.mp4?token=hYvUiaY8dttUmofq1Nsdw0nw7JDDOoHdxk9xOrm3w5bnSgw1LN9lvp07zww7MhLMI7saAwtV1q31X4-ZUDBSjDS9rX5qACDU5bsmNq1npzIeevys07XuwARQzt43a-hpi2WXN9geqOCcW_af2vCCeQAEg7ytjUNWkwtezq_GM3X07bD48qLlP3-mnm1oshyHVDV8ej97xvNwTQT0nxJOVvbBg6aZ0bGvkJlPjBFysVNCtXwzfN73vUb7zz-8fw8iDV9Yguuw8u61euhzQPjH_lthZpc63xiIxkcYkbDV-Z7A5K4J3zWPlJ8VOWbCj-zuo4jyebEXd-6_7HY6kHo2RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🎙
💥
امنیت و آرامش با حضور نویر
‌
خصوصیات مهم مانوئل نویر از زبان ژروم بواتنگ دروازه‌بانی که کیفیت کافی برای بازی در جلوی زمین را هم دارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96017" target="_blank">📅 11:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeU78BNokm3-OtzdF9O6tnw9Q9vcwSqfJBD9VWnpZPo7k3kKYbv5AwiXuuiatSJ_CWSCb3SY0RE8MdkNow6sU_m8aw_Cb85IJT9F_ai0EfbypwzdaMQsxSpKqBn2Q_UncfYhoT1sboH7_8FzZPWg1IyithUXlWHGcD0Kn9w2bj5CtbblGw5Ydgcg2GSbH6ZLei0yHiYMc9zSRuz1yU4v8AHwTgBkMcpcwZPF-xnjwn0Fu-YePVek9DaTpm5pRbIiSQ3uNHLsqPCVj1gHGPuFxLN2sCiGhL7bSSiq-P88GqA1unSm6yBg87gzPjjDSLoFYMO8trtu8-We8RVf8SKS_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
📊
🏆
🏆
تیم‌های آسیایی با بیشترین حضور در مراحل حذفی جام جهانی به طور کلی  :
‏5 بار —
🇯🇵
ژاپن.
👑
‏4 بار —
🇰🇷
کره جنوبی
‏3 بار —
🇦🇺
استرالیا
‏1 بار —
🇸🇦
عربستان سعودی
‏1 بار —
🇰🇵
کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96016" target="_blank">📅 11:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOBD8DVgCTr9tmEyQEItyE5h6bxf5ak9JrIGIDbKT3Ywuqhxr18BPGkAAeYlIbBKiY8SzG9ktakeIqEnKQyPLv3AMLpQD1d7-xe_d8KuTxt96xgkRBZvCC14XqRwpLqSsMTgluaOCuiAzMrtYZJozigxkcvxABvpnk483ipnMKDHfErbbRU8cjwT_-kw2rftC3ck-aZ7X3kLtZBgHngL3812uczCVvG9J4q8rh_9V0OgjBC4-0u2vyQv_YQKnILGoFaifOMXGfLtZKirIsFLW4fuW-avUpm96x59s_YlaOFmY-iWvI2zAw1EqW5C2bwVRCAleX20oovbM6xD5xx0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇬
🇮🇷
پوستر فدراسیون فوتبال ایران برای دیدار صبح فردا مقابل تیم‌ملی مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/96015" target="_blank">📅 11:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd157c98e3.mp4?token=jB7gn4-mlUWefLBMZSF6_G3-5at5yur6X8lFkP1euB7rHQSwPL9bQKRBGoxwDRF73dUiRAf8f208Lyntplu5dcyz4Mt7EfRsTnZ_5aLv6f2zmjyCbGR3rZ13_ujzTBkEUQMYFUOeTfdP34ISjXiP7ZebBzdxoQw0ND6qfa6wYD7AM4k7cLaFLmwdXY0Hyy_zOJCkZHjcGln65gSazdw1hmyfjWMAimMPvlBM5628sdkL5dMWgFqEnz8C5M-Qu4mUwJNl6ZtpJcxCan2fAnj20UbkubKbKWsio5pFfjG3bv8KSwMETOawLjrwGWGtx12yNaWMwKgHvU58QyZ1CAiXKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd157c98e3.mp4?token=jB7gn4-mlUWefLBMZSF6_G3-5at5yur6X8lFkP1euB7rHQSwPL9bQKRBGoxwDRF73dUiRAf8f208Lyntplu5dcyz4Mt7EfRsTnZ_5aLv6f2zmjyCbGR3rZ13_ujzTBkEUQMYFUOeTfdP34ISjXiP7ZebBzdxoQw0ND6qfa6wYD7AM4k7cLaFLmwdXY0Hyy_zOJCkZHjcGln65gSazdw1hmyfjWMAimMPvlBM5628sdkL5dMWgFqEnz8C5M-Qu4mUwJNl6ZtpJcxCan2fAnj20UbkubKbKWsio5pFfjG3bv8KSwMETOawLjrwGWGtx12yNaWMwKgHvU58QyZ1CAiXKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🇫🇷
مصرف یک چیز عجیب قبل مسابقات جام‌جهانی توسط ستاره تیم‌ملی فرانسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96014" target="_blank">📅 11:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOdRvGsKL8x5F-mqCgJa7Ierg54sbclvXDbbQBkeX0kdoIdLfRHqIyFKnwA7dNc_IgVcZYNs2mPHygEMpuy4BUNYpIgSSTxQBM6oidKRB8mFLL_qtboeyOzbEHhl-pWwgUGJrFHnjEJT4V4iwnAMTjtURFaF0SfqI23748A6Xg-JSqpgjSX9c-RL8gGlC_QHfNU0iy6r9_g3pQZTY6Z_NlA0qRAFsTomrPTSEFLJ8ajy_UUUsy-dh2EmGZSlbMJ7vRezGmxN3WB5Wo0PLQBeEKZJe82DTmljOv0cp7CfmnH0lebW7DT5VL_SQRU5kuCCcQ5l7Dn0BL4g09eIWVsefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تقابل دیدنیه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/96013" target="_blank">📅 11:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XoqSqJF7_WH_YbyAPlyKSTxjj3F-r9t_dlOnzvvPS0tNBRmC6_VZPDZS1_pou2W8yzs5vgmN6dUmE1bPyQWN4GJecWlU0W1scj8JpuOpTLiasY0PE-1EzhflfC-0voNk4x_q5ETCAFyfPOWpwPtG3I_Ehve9VluLPIn9KMpQb0q5w1C_8I1IBpqMHdwYLIHS-lDnpNlpN-6myB2Xx1dEzGq-jv5CNgYxbFrlpaXo5TcXHLarf3r323fbFWC4aO4h3mYGAn_18Kae6Ro3v4FvphIvCw5Ye3BpW1n_SAZyrLw3CXqMWpV_xYVWjk90sJtB8mvxKbun_QOf4KzoSqIJfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تکلیف دو تا از مهم‌ترین بازیای این مرحله جام‌جهانی مشخص شد:
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96012" target="_blank">📅 10:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83cfa0a889.mp4?token=oXqv7x21StJ_8P1CWogZjk6ZfME11DcoeeF23yvC5G4QI69_1w-gEhXWwa2DNLMUiosn-8R8_tSwDJUSld8i0pIWAFKhCqReuWzE55GXf3MJFfsUAk0fQXKAMYjhtAfLv_D_J2G5uX3sghmI85c9pJe0ZOHSibOzUeoIi9hu2MT4VAO-U-UNKrmTnDY0NQ7VGYS5VHn44eDOQYzK3OoWIAm-swW9F1YjqinE8_O1ATT4D6UDUtbkR0p8F0hwTSq8zkhq_N-jRhNSP-zOK47jkmiTGRbLlKvOe4px62s7GqRx49AjM4tinTAy2zW9kqnp28udAFPao6c-EKE-eeMoNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83cfa0a889.mp4?token=oXqv7x21StJ_8P1CWogZjk6ZfME11DcoeeF23yvC5G4QI69_1w-gEhXWwa2DNLMUiosn-8R8_tSwDJUSld8i0pIWAFKhCqReuWzE55GXf3MJFfsUAk0fQXKAMYjhtAfLv_D_J2G5uX3sghmI85c9pJe0ZOHSibOzUeoIi9hu2MT4VAO-U-UNKrmTnDY0NQ7VGYS5VHn44eDOQYzK3OoWIAm-swW9F1YjqinE8_O1ATT4D6UDUtbkR0p8F0hwTSq8zkhq_N-jRhNSP-zOK47jkmiTGRbLlKvOe4px62s7GqRx49AjM4tinTAy2zW9kqnp28udAFPao6c-EKE-eeMoNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به‌مناسبت حواشی بازی ایران و مصر این صحبت سمی مرتضی فنونی‌زاده رو بشنویم
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/96011" target="_blank">📅 10:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89114baf09.mp4?token=EH_r4hDuP5pzqP7UZlJDrtx_8aB4wVMHBHMGlwCK-_qNBeZSZUrKOWSKM-Fj0DyYkk0n25u76WF4ZmcWP98SkuEPk2qYjAdMO3cciDwM1hmesp1sajB3Nd6PZTIjjND3XD_smpPQ_kco9X8TZSJEZ2vmHnP6HImOMHdSVukI56PCT7fzg5BysUsBl1TQaGSNKg6uOXR2cvNfKcZ_eonpngsndZe9EKPtbIpsRYw2A0XrrEQgebEx1HCKZ4CDPTSNWZeO5fh35iIWnuCmpVoNmFmtXkm1jwc6moN60jFLC1cyqwEwLQ-n190vCjuhcXsha8EVG9P0M6LN__VuReEObA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89114baf09.mp4?token=EH_r4hDuP5pzqP7UZlJDrtx_8aB4wVMHBHMGlwCK-_qNBeZSZUrKOWSKM-Fj0DyYkk0n25u76WF4ZmcWP98SkuEPk2qYjAdMO3cciDwM1hmesp1sajB3Nd6PZTIjjND3XD_smpPQ_kco9X8TZSJEZ2vmHnP6HImOMHdSVukI56PCT7fzg5BysUsBl1TQaGSNKg6uOXR2cvNfKcZ_eonpngsndZe9EKPtbIpsRYw2A0XrrEQgebEx1HCKZ4CDPTSNWZeO5fh35iIWnuCmpVoNmFmtXkm1jwc6moN60jFLC1cyqwEwLQ-n190vCjuhcXsha8EVG9P0M6LN__VuReEObA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇽
🇳🇱
دیشب مکزیکی‌ها به هوادار هلند یه حال اساسی دادن
😂
😂
👀
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/96010" target="_blank">📅 10:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96007">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YvWKSb-jJQ6DCkvMadd-iTv-ze9bIuNeRw6EvYIXz0l7J5hurtDueDq3hoDFkutdi5TirqOgy8d866B8CVJaDhawaPeMCmKj6g9yl9R0GOq5j0DGt0eiS7IYVTpZWGqXLBUi1FrArAOtotMrNdgPFmwscOlGY3QIVaXKYSKyvTHTXajmfujg1Bx1kTR-XCiLtC67vRCApbOZd-gxZWgpT2TabYxbe35eDgy6RGB19UjQl7nTMSn7ZuqL4LIjQ9mY5jdCdc50PwZKDNVRk67SKnhJehQw_wAUOHrABGhf006DWF1rXkpa3-6tzXAEU0cWf3_Odt7AwQckGeqL6gyLAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phVierVWSZv5l4OgpW3LTobKxZdPmHwe-gTz9ICUT0QeL2imlcXnySrCBEBiWbcGAoyDmg2Cp-FusXcbXELsMzdGb9bfLNnC0bG7WKqkzq-kY7dc1-JRWHd1AqwxdJa8P26eeuKwmQaFrfs__nTXdnB4HSGGOxE_Q-WWhYEPzINKu0aqKXet8VjkTBshsPCgO91uxiHBcPYY-KiGD6fFgfi2gYUVkz9TTao-CwqK1gut-6-4a0RvU2jGSuLHCcKyNaXtzCa0WajrrCU0bYfWQS1jX1U954SlKK0TyGCyLpIJoIX56sXeI3lg9KBfOxT-XGyjuXHggBnk0uzmTOA--g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KuH7Mxzn5XTIqDCcoQhn0IWeiiWxPhkuLatEmabwPdrYQxqh5QLQKCLXRHP4x-lLdxHs-I5ub400NaB-sSuV8EIzAIZ0XD4UNmDh9iNj6hsTYKNbz4iDkDZUG5ZiL0ihH43oqhWF86eQtSwhhjqBIFLpHaexrTLitEKcAeEuaGYpliEATAsDCx3LBCL6VXZ1Yx6ZViMAMXgB8xPSvlPayzdmdZIiiNoNaxX-tHn6FNI51j1l_Ew0YP6ONViItEva56OAOuNV4-o-vjcn1qouUdebC_upJByH2WVnLL308jNmVEcIXY_CKCDCLa6TFq6DltfAYxUIpv61HHe_s56bdA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هر چی از کیوت بودن فنای مکزیک بگیم بازم کمه
🍸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96007" target="_blank">📅 09:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96004">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
ویدیویی عجیب دیروز از درگیری سر گرفتن یه ظرف نذری تو شهر همدان
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/Futball180TV/96004" target="_blank">📅 09:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96003">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=emcs9K9qzmE5Fl0k5n_DqZmiT7OnEsr4DrWShdm7KXsmP4BCqx2iUhr1NJ4z8bLasnAhVTPwP9XPMRxioUqadmShUjeAxoKVNLCTSzah9LFhctWPgY9ICb5mYNDGYi2R2-GJVj7Ce-vlYS86DO3Oi4U9L0Mii4TgqY1nMyOuTbHrw-fmBFy9mQ741vGuKXLryFJj_yWBkyiYKB5hmbZGz-hcz2Ec90cxrn2cREUGFV1WJk5w2qlcSzBAstq3GioLXz2dxzI6Vdg-KCKDpWF-dAKWUSirVSX4kl-P60qCkT4x5Cc5jEfbqrsz5DqY-7VU3nFvcbeepygNcJwFKIAZkTrr_JoDTbT3NhATVGRaGEx7vf7BN5q11BogXt767X-w8t7oxDl0cAERh5qOU5FlbP6zic-wZHE7USOQ9_yGR9yfksq8-eLwhAcKsUMm0_a5UVvbU8EIIxeww0ncOIGOzEA36bTfg-pOJzLv2rCE8a99jILRBeTnzAw-ys2A6pxHHXfAabyTGRpcYWw1sW2DXpm52CgXzFCRKkLSXtv6Z2eemDxAB_yFPOKJp-rPgfu2ABqLVikKyFi-4bs9ZafdMuRdPjujdLFYDtT9o2xADoefzqUpN5kPV5lyG_fRfQgxsRPkgmcSgJbVJ0xbfMU5aNVobEzZn8LD1AePOBsSN2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d6d7c284a.mp4?token=emcs9K9qzmE5Fl0k5n_DqZmiT7OnEsr4DrWShdm7KXsmP4BCqx2iUhr1NJ4z8bLasnAhVTPwP9XPMRxioUqadmShUjeAxoKVNLCTSzah9LFhctWPgY9ICb5mYNDGYi2R2-GJVj7Ce-vlYS86DO3Oi4U9L0Mii4TgqY1nMyOuTbHrw-fmBFy9mQ741vGuKXLryFJj_yWBkyiYKB5hmbZGz-hcz2Ec90cxrn2cREUGFV1WJk5w2qlcSzBAstq3GioLXz2dxzI6Vdg-KCKDpWF-dAKWUSirVSX4kl-P60qCkT4x5Cc5jEfbqrsz5DqY-7VU3nFvcbeepygNcJwFKIAZkTrr_JoDTbT3NhATVGRaGEx7vf7BN5q11BogXt767X-w8t7oxDl0cAERh5qOU5FlbP6zic-wZHE7USOQ9_yGR9yfksq8-eLwhAcKsUMm0_a5UVvbU8EIIxeww0ncOIGOzEA36bTfg-pOJzLv2rCE8a99jILRBeTnzAw-ys2A6pxHHXfAabyTGRpcYWw1sW2DXpm52CgXzFCRKkLSXtv6Z2eemDxAB_yFPOKJp-rPgfu2ABqLVikKyFi-4bs9ZafdMuRdPjujdLFYDtT9o2xADoefzqUpN5kPV5lyG_fRfQgxsRPkgmcSgJbVJ0xbfMU5aNVobEzZn8LD1AePOBsSN2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏆
🇩🇪
زندگی باورنکردنی دنیز اونداف
سرگذشت عجیب ستاره تیم ملی آلمان در جام جهانی ۲۰۲۶ که با شادی‌اش، اصالت خود را با افتخار به دنیا اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96003" target="_blank">📅 09:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96002">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tiWVzknIAWFqyYADe1wvCKrtdk8YtfSsgl_8ZqH5DUGWhhz04kQBDyGd4m0iuTLDFxKOefZlMG5aywGggnnYf1NxSYtAqQGFnPT0yBCL7LyQh01AQ4TL0Z_3nsh9QE5lUUxLP_i_j1-TtG3UBljqJAa6DX2qLoFj74X6dAIfJgoV-KgtvB6hHBCq4Om_cJWLaTsusYoLalp0rYv1LDfMRvUQLkdy3kVCwvwyT0wjMD6DdW_2EtuXUek3khghx1g6cQAvMcA4WAsN1pF3X9q-WE_HN27oczbVUCudkhZ7RMJYGCZDU-NbRthjo0pGuyoayNfxS55y8G5MUQPeMCn1lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👀
💥
ترکیب‌احتمالی فصل‌آینده بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/96002" target="_blank">📅 09:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7vkXKKj6YvzL34yiJpgISn27GXUKR3pRjwfKVLdyLcWKNNGsivEjpAKAUp9BjYn6nBhFlmCoAqeCtCh0GX0P3QRLWSxLlhNa63TfmKzfFHB5OJmLwphlDrOjEWqXP4Sq2qJepgTAwgHpGjSp5m9stNXWL7Q21O-EK3eQqKsgN-JR6V9fw-QTu76ncYP6gmjywTHlpN8aP7o0rSrd11Ke3WK-UovN1QId20GEooF3uVaC8PPJPzLDN3-xDIfr4TPeNMVsIhvovmdOuOcWTC8nJ_reeJAo6Gu1F2Q60XChEvnmliVoIYZFMyWgT9dqGCfbrVkGE-0F5cNOKd0GskCZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfnYnwRSKDiZWW9arXcRn_X5UqS4t5jPrIhysoSWbMoXFojLSRPc-CfaChAQMVExpcZlcfJoLemo6RN0z49jDWwbq9nc_x0R0LVDFj_feGX_Rz0Vf2ipDldW3hFPPX4FhoGinVhrgeiLALRaM94QNy0P6mMG5rqaeWOQP6biayqerzscAkGdYqS4LEhZ_8buiPsLeE9SGmEHC2MivOXQQa7Q0UMgDZHfDaXiPn0X7omMHGDB1BLLaI7oPbWaXovpFbC5AgbaQbOchlQJyeh361L8_aYsWTRnpQ-eDN1EHHBX-_7iaGQBZmHuSxv56Y0xAVzmXoJcbBIfT_Z300SbMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jiGoySb3TXSlUQmCmzhuOWmv1AEa2jUF753u1h3bF_rynIsdfUc6nAE3PEJ_Wa1RtNCxOfxEZxnL58lOz624yWQGsT4bnaklYpeC8xyKWZ8ejPFxa9PAR7aAtHEPy3miRQwbey-defMhhDDaBvHpyNxxuxHsbgn-65PbEo1VVP_5ZAhtrUN_qBLhIBHncQRw2o-DhDBgqfK3WSJz_3i4NEyjRCkTB2FiQQG4iMdZ5OF2v_2K6lauxHDw_STtvZGIHsJR_me0LGPcYGjJ2hmwg3HEEJE0DlmvkH5O0cVQzJAzhaIn8JCBNmVOZAU62e8fVW8MH5JzCeFpBrmI1JtWDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ای خار جبر جغرافیایی رو
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/95999" target="_blank">📅 08:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YKmJyAGn8SksNXeZK-kgQsRx5WO9zEEBHdAntNUY3zj1uoY4cUGEAB9LGqOEe31uNy7SQn5GdCahfu4YHFRjzQbiJR_r9g_NX1DlUzzsuLXvV6hkIoa-Y00BcI8Tfm8Zzju9PkbeXpuwvedca7YA3oMeRY2zpcBp4Ggwyu94Gpx31dFnUEd96VgehzZv4KjjEKx8F1PgiPjX1OwP_x0zXIYmFAeL6lj8bcV0MKkJJeOGw9HWCVcRSPbSG6ozRAWSlUpqyHbBcP4SdODvC4vaSrb8ybLWUCMgFleKJy3pf3mI4jl87QXCFti658zFAajMMKGdAOCtE3Mb2xaOvOpt2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
تیم‌های راه‌یافته به مرحله حذفی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/95998" target="_blank">📅 07:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVIG2ehitGVwhEIv-5WTb_sSG-2oadxw_JjiC-Jv6YpJ76NxMFar8sJ0bZ08kpFV5tTXsGYg3NTH7AjGFSCVgfagKlPcBArrVD1gVZZmULGljh4Z4dtVVwhQZXTjm6L31HM7SMLIsRkJT57xdYIH6TjHR_eoiDgV1Go028JKOEgAKxsX2IjRs70x1wE6ts0zNb7ZaCB32pkGKEfq6yFWLiYlKoHUn8JMSKOf-n-l1JJPHbPbs-bmwNscqmlfsIf8rcPezvcSQAt_OBRQQRC-ocvSTy1svTO7C5sC5EuXxZv0RRYIiQl75EsrM3-9BGxcyw7pRizD2eylqJzMcFNXuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول بهترین تیم‌های سوم مسابقات؛ سه تیم اول تصویر مجوز مرحله بعدی را کسب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/95997" target="_blank">📅 07:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldMvVSIYRPCnNQjtZzVZXLZWPHw1DmMqeekj_hx0r_mr54O3zu8TfaFWqEGIGCUeV3c-c1c7fDqEo9ZXmWI9czwE5ukq6ort8l-SvpGBapEzg_DnIZx47olwkP7NucCx7rcTplWDhqadgUUi3yjmwd4qSuoZqACw0HDwBicGJRI0t4tVQ4folKmzj5oSjmoXTT_kTRKcguCZwasYJNmzlrwNjnvsc0CvJ27tW4R7FSxp_E_V4VsYRnHnGAYxvqrdGiTXsl8JX6I0FTCMgCQg3BPSh723oiA8HkMR5vT9wf6Hj9k2qJRWGr7ge75UsHUW0qBgR1pWsl2hJ2agasb8fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
جدول گروه D در پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/95996" target="_blank">📅 07:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJPV6sXOPRc5aQ8622gTDTLFSg2GhB-pjFQxg-GytiZz3oV3M0bDk0lvV5EqGRiRpvpTxj6ub3v9IZWlC2QtProbFMvgWzEyydESeaWUIzX1UWDCpG7NLT3taSzYrTN5o1HLmA7hnWC0HNORbZG-EEcijQ1JQcGInQX3h0QqifJ9A7cftXW4pMcrhO-MkGCtM8pbmmzfu6Vo4G-wrASVACN-6y2iyEk5Bs_P-l_m-rNIa0P1pLe_WRwgIdHjgY3dnqm9pmOvFcLse2HvyJBwkmbx6ygLgXtUvR00NJngXpAMCioj55E9r2rX6Ot8NiQlcc_7YToZy3CuCmAmiWDh5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
نمودار مراحل حذفی جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95995" target="_blank">📅 07:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL9lKSTWsX_EbiDc49Pq5GpPFBo0p4QFmgln2tLx5OP7W7RnNfltZ2vepo7XUJw71yiNyCkTDFSRNpFnkESUezU8j5R5v1AYiZymjSJefjJHelubgGyvmpPIMNJmpLERIOan3dpXrDICYdx6YH5xuBsvzuu2BDgYOjFst8O2LfOfkupTk_kt3bJjWp3FlCSlGySIzd7bszm70vB_uw3KeuVAX5hzB-ZPk3HbVxakbgjqbsMUQAt-jDHxr55L3ZVT5r9N92zrtrbiZU4AcWnBqXJENjex4vEXpzn8Zrm6mB8ah7WmaXOQv48Y96zkL7b2jBnzhRDZg2ZiDyKZFGcLPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🏆
تیم‌ملی ترکیه در آخرین بازی خود در جام‌جهانی مقابل آمریکا صدرنشین به برتری رسید و با کسب دو باخت و یک برد از مسابقات کنار رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95994" target="_blank">📅 07:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی گروه D جام‌جهانی
🇺🇸
آمریکا
2️⃣
3️⃣
ترکیه
🇹🇷
🇦🇺
استرالیا
0️⃣
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95993" target="_blank">📅 07:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی گروه D جام‌جهانی
🇺🇸
آمریکا
2️⃣
3️⃣
ترکیه
🇹🇷
🇦🇺
استرالیا
0️⃣
0️⃣
پاراگوئه
🇵🇾
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95992" target="_blank">📅 07:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RsYIkywjExZcJfUDhoYXv7O62Io4x60RjOvoaXgJ_ecvHYz-4EH6SuYfcykol2XQ_C41_IhdHItkjaqgDI7xjlQR7bzNA5s7odGM95zSOdxxGV78nH6hrY5qcRvaOel00md1J6SxD-jbdHr_zrhK0g-HgjfWiBIrZd9ucYbkfAQKJfANFCUc8OysBUyNFvm0CVq9r8b0zMInCjEYn8-8slUXW7VPP2ZRVv6squwgXeNywysVZPKGWypXuswtLyU52dmhNZtPKJhChH4vaUZWBQFOgU8a3O9JcNIjN-buuTf_OJxte5iFjgj8G3CMyryAUzODHZjiOQJh7lKOl-hvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت قاره آمریکا مقابل اروپا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95991" target="_blank">📅 07:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jj-w6Q7BB2cRn-O1e-OIkgx6mcYeMkg0lfT3tg4xkgIZVQNmdczDEt4ZNgtpK3duczXiRtRNVD3kp0HGMVOlyE9xd6BvtpLz2XOer5YKTSGE_5zHn7KoUbI0sO3DrczHf9C_yqHPfmE2yBo4AF751bdOhMZirODUZySkJ7FGMppinYf9cuDkbeE0EtSeAYyzydzIZIZ1xYeA3YSob-r_O8-m_Uu5y4lLMETOx6J4LNBAd271kXGVSSfhX19Nbsrt5LhgkLHv8wp6GG9hB09V4--t3lI5u3W1XjswYwaFoG7Un4zGoyx1Dj0JNDYYFoKDLEHP2YF7f0P73dje5qB0EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینا رو ببین خدا وکیلی
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95990" target="_blank">📅 07:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a795f9561.mp4?token=A2c7OwG6TGcTdilg2dVUvsTPz5nbOPCRyLQmEmyb3hg0TOPJ5paxL_deVAhAwdMXCVB4cl2hZFbYFoJuVZ8bmB5yCj4t5aVf76e40iu-P_PvkG6Y4l821tOyIXiDsEOV9w_NqgkpMDaPPa1HfX63CjhUt4Lvc1NIQWnoHK1Aol1RXokBylo0FOAcKUe2RFQdEQPgv6iL6zs8pcXM_PiLIrbfwzSQ4OQ9KGt9j0rdwuuRQGgZ2QEJWY2sx59ZlKOC_yjQ4q54W-O3PmorPuDF25tChTDpCWW3C-V4nxHqz8XcCtENhR82sWeYNXDCEAjho_boGZJEc060Xb3QfrbsOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a795f9561.mp4?token=A2c7OwG6TGcTdilg2dVUvsTPz5nbOPCRyLQmEmyb3hg0TOPJ5paxL_deVAhAwdMXCVB4cl2hZFbYFoJuVZ8bmB5yCj4t5aVf76e40iu-P_PvkG6Y4l821tOyIXiDsEOV9w_NqgkpMDaPPa1HfX63CjhUt4Lvc1NIQWnoHK1Aol1RXokBylo0FOAcKUe2RFQdEQPgv6iL6zs8pcXM_PiLIrbfwzSQ4OQ9KGt9j0rdwuuRQGgZ2QEJWY2sx59ZlKOC_yjQ4q54W-O3PmorPuDF25tChTDpCWW3C-V4nxHqz8XcCtENhR82sWeYNXDCEAjho_boGZJEc060Xb3QfrbsOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر تقه آمریکا به ترکیه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95989" target="_blank">📅 06:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">چه فلک زده ایه ترکیه
😂
😂</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/95988" target="_blank">📅 06:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گلللللل دوم آمریکا</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/95987" target="_blank">📅 06:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80336e0918.mp4?token=RcZTgJd6LcPE9s1qzQ7aDs6svyjmT2_7qiaGPZGyNqD1l9iN_of-kndGe5bf2wSSyDOfgnM0-D0uoTQe78QdUr4Suwy-JffhpADl2AI6t5QiDJDB4l8VScRhMg8OTd8tGDHJqrSRKEGWVxlWFgzL0emKxKD-mOJVnYXQguEFEPZgr8Qq1CAP12fIsOxkymzkKcCzrcTrwUgC4m5eHO5CM5zrVObsAaNyHcHXu5SNhMGjF7KIUFLZqQ388I2HoR4UF_AJvMOOGYQ82icfQfgyxSmDNFmjOuKuvimK3LhkmQGjXX-eDU7R3Xp6O_i7af7RCgMNo0UvQiTs3H-YRkXeEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80336e0918.mp4?token=RcZTgJd6LcPE9s1qzQ7aDs6svyjmT2_7qiaGPZGyNqD1l9iN_of-kndGe5bf2wSSyDOfgnM0-D0uoTQe78QdUr4Suwy-JffhpADl2AI6t5QiDJDB4l8VScRhMg8OTd8tGDHJqrSRKEGWVxlWFgzL0emKxKD-mOJVnYXQguEFEPZgr8Qq1CAP12fIsOxkymzkKcCzrcTrwUgC4m5eHO5CM5zrVObsAaNyHcHXu5SNhMGjF7KIUFLZqQ388I2HoR4UF_AJvMOOGYQ82icfQfgyxSmDNFmjOuKuvimK3LhkmQGjXX-eDU7R3Xp6O_i7af7RCgMNo0UvQiTs3H-YRkXeEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل دوم ترکیه به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/Futball180TV/95986" target="_blank">📅 06:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kr-LwlwiyFWNsazHEdhJpB1_PzfgdopgPGmFOMXT7RhhK9QijAdYpEMut09vwhDZKXA-13nEh97479b0IOwE8WIOVPbrLm4xuhgPSymckx02RGSWVECdXsSVk5oqYizv-uvFmOup__uM9OISTWe55JHSmK5R1HbMf96gANQ6TdrWOeFWzFAXqqxQ16kpayyr_181Mcmdn5sjsMIERkR__jmOjmOLy7qDKKaVukav6WzMjRJzC9B300dddzXXiPTjq9mfF0fd8HM2Sl6fKjcfzC43ngsur57RGLS1LRAqYNMSbZGl4qV9f_mVTtAh6W0Z38DHGAZbcU3duTjsXFRlAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایلر دردن در حال تماشای بازی آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95985" target="_blank">📅 05:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=en_H2URMyCtGs4vcHDSb04aO5YMlnScyIKNIuEYSEkxVL-UNmg-62PurnEIh3Y23kYbATDcltcXMw1Nmpcji3NE4WbkNjImhw5yw2op55z0QF9QaIOnefn2l-JiesGg1s_whUZ7ki3vYU2-k0SaQlwin6Ap0CHOqG3gZIp1qmsOGEG8BRqmNo_Vpvaayfs2EaE8rRY_e8p4P1g5d8er5oFPfViRbFgVxtORaUDnWG1sRbl3kk4UXdM2Br6HiVSWnXL0kqSvNH38HC-k2qmzFEUnKCAPv-fx_REtU2GkXc1DzDfJ2OkD7n9VYZvLrrKqI20BaB77zU1iUjHZJm7Epfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cba51004b9.mp4?token=en_H2URMyCtGs4vcHDSb04aO5YMlnScyIKNIuEYSEkxVL-UNmg-62PurnEIh3Y23kYbATDcltcXMw1Nmpcji3NE4WbkNjImhw5yw2op55z0QF9QaIOnefn2l-JiesGg1s_whUZ7ki3vYU2-k0SaQlwin6Ap0CHOqG3gZIp1qmsOGEG8BRqmNo_Vpvaayfs2EaE8rRY_e8p4P1g5d8er5oFPfViRbFgVxtORaUDnWG1sRbl3kk4UXdM2Br6HiVSWnXL0kqSvNH38HC-k2qmzFEUnKCAPv-fx_REtU2GkXc1DzDfJ2OkD7n9VYZvLrrKqI20BaB77zU1iUjHZJm7Epfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/95984" target="_blank">📅 05:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=MC-fcQKx3LZHvPH-MLAqUGdiC2rGD6M60sxHVCOaQm1A4CXRcZTL9-O7eaUqgRT4bR90ZQiFVkKZTsat2R26GAA0EyVxo8g1YWReFifvC6uHYD94l62C8qGrk7P2vIQ1jKxJq-e_UgZiT2vbndPRYb6TkiN8eoHqsCNHmNc_a_P2R5qoO08E1ukJ-CW-HsbB9mI-Gjmb2XOa76uWFBqQhQP3oa_VmQBxWL0Sgr6NXJqRI2_d_jQJbHdo8ywYmCFYepIrYhzvGT8uoWxYqSXJ9_K5S0APnmTrXHloxLaBZjf5Xm21Wg5A8B4YLiQT3M_wzLYPDKc-bV4mXP_k8xGZlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72cd71076b.mp4?token=MC-fcQKx3LZHvPH-MLAqUGdiC2rGD6M60sxHVCOaQm1A4CXRcZTL9-O7eaUqgRT4bR90ZQiFVkKZTsat2R26GAA0EyVxo8g1YWReFifvC6uHYD94l62C8qGrk7P2vIQ1jKxJq-e_UgZiT2vbndPRYb6TkiN8eoHqsCNHmNc_a_P2R5qoO08E1ukJ-CW-HsbB9mI-Gjmb2XOa76uWFBqQhQP3oa_VmQBxWL0Sgr6NXJqRI2_d_jQJbHdo8ywYmCFYepIrYhzvGT8uoWxYqSXJ9_K5S0APnmTrXHloxLaBZjf5Xm21Wg5A8B4YLiQT3M_wzLYPDKc-bV4mXP_k8xGZlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
گل اول آمریکا به ترکیه توسط تراستی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95983" target="_blank">📅 05:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyZ2b4GPwg78LoXONM8ASrulrCGdkqGtBvH1CWBnurvC2TalMFMpzSFl-O0QQ9PQKm2ffA5jvkpBBWxhLUFq2cnUxcqMrqGRbZsG-LyZ8vy4tTs1uJi5Phis6_qSCrpYyTBvi6phtZanjp1qPMq8Hftko80nmhpeNkjAxyKanPm7wSiwk7NDp8i34-tE7MSdwRR6lHnpjojYspVJ6-NFPhB8ujHt4Glr164m1KYjZlXaRt_jq1HvrAFI5MZI9kvq9xZJfHWxkfid4VK_qWQKh_KR4blvmuQQRGFvCPzCYBfcU5JPV_xW1nweW-GpweYEfDGeyUP1rlqoQ_0tMtJ5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
جدول فعلی برترین تیم‌های سوم مرحله گروهی جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95982" target="_blank">📅 05:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZQcbBUD9HgMLGMNenq-Mzn1zKJ9HT-YthLM1B5ax9GHThzXZp69zN_9AXgaSvlw6MhKCDYVWBxetNksj6VJkbR9M88M7_beTUyfnChNfNQhVMeBth7oKitMEQyz21d6w0iPwYZINDKXEfc5MR0CFg-KUPityxHMkZehKPKcWHk2GajhtNIQm1dQgxZ9OLxojDvgoOYK3GDrnEzt0LMRswGsdbT93FsYHiOM4A6QBqPrW6B_J48AscqMSv2XWiI6uWWa29lgHOU8d76-IjVchXX3zc2Yy1LOKpVVS_BUwUNnL_qRxNsCL4jJQtbMPXmUhnMhLLxI-ngRylRGwAzTHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین حضور تیم‌های آسیایی در مرحله حذفی جام جهانی:
5 بار —  ژاپن
4 بار —  کره جنوبی
3 بار —  استرالیا
1 بار —  عربستان سعودی
1 بار —  کره شمالی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/95981" target="_blank">📅 05:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VR8X5TFN4OvY6d4wH4CbCdbMZjPvGX0ogVK3LJOrluX9KAzriuxR1hD2C4TLK3fe7GYpojbRiMsxq99IiPEdfD9pMV4kDDB1naTpZ97L7wjDBqe6s1mH67JixNNEBNeUU1cly1bDkIcq38c7t_MDABnziFKFi-gNDLPTevAmsgJRA7t3q6CLeQrwX-L4gqQmFnld1e_ziIG8hd4SxN_UV1efBeLLTeQG-zWL0VGsILSsHOiwsJT6O3PXCTrDWn8p1NuL2wVN0cU21NQjLplq5o3hNTdmLPM5rjM0zhjWtt0r2BPnf4U8525nt3iJ2MzQ85W-aDslGogDGFxWCrkHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🌎
بازیکنان رئال مادرید با 9 گل‌زده بیشترین گل را بین دیگر باشگاه های جهان در جام جهانی ۲۰۲۶ زده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95980" target="_blank">📅 04:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmGAxhiTohsygBg3g7eCx0hr24HyHjueV7kllqf8i53qvepqPgdx5oBae1GX9soROBbPvOxT-KJLhK3yvWdTtqODLmv8UnjymjAnu5XrFYlpL6Rev53tqZ4124H_GyJzPM33i5B-LUVQl29BCi2pGO6JdFPXSENGRUJvvcj0ld2lclCyq-Qh0G-E_bjhJa1bzHd5LvNkZx8Z-8lh3wZ0VUeDTESgyS5HHStgdWKN5Auvw13SQ_7DWri8hjpHvONeIP0_aWc3Z682y8fFhRA-YK2uTj2RzoR0k4viobpUhhT5FZYm9jf5FLK5h_hhe3-TapL_HlvFRneyFCszqSrDyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F جام جهانی 2026 پس از پایان مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/95979" target="_blank">📅 04:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95978">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TH9AhVFqCOVVHWep-MVbvTnBgSimEJoo1KemmW16wwnjwYYWmlaMdb-iVKpkS3iNjH9j-T_aVTJlFnl0Nfc_RhsBDG4bolWTIsD0kGgybSzufYw36oeIDF0xpJiE5qJf8US7OdJLflNeTb3iFNv2x5ujEubWcHlUp9rm9clecILKUKQyRawhfvbRp53K_dpes12L4-rsoJowSv5LkkhGqjYOsnQYSiCJ3IgcBzkMbhznS7bSUK2U5ml15HQWlqOla_0hBwwbvduZbC1mHXJMRG2GYeUQMwejbJEIWVFGBtoxwvTwuWH23Nk9WhrFdPUr16i-qAPNFnANXEixGEMhrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
تکلیف دو تا از مهم‌ترین بازیای این مرحله جام‌جهانی مشخص شد:
🇧🇷
برزیل - ژاپن
🇯🇵
🇳🇱
هلند - مراکش
🇲🇦
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95978" target="_blank">📅 04:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95977">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr40imLw8AaH-AvkktpN89plzr9jNXjcGKPBPX6wQY0SzUpeGBXmhaFzIWVY7TvMrMeGFYOuaUf9fTllUXZL7Xkofml9-xk1bc3MxSFBBOopPVRhv-9l9XPSHLnNkKMIMExuQBJ4jT5AEbvgh8YZiQbKWdDK5MOvT9-lMDyYnll3w-dWsr-EinvZUiPNGgtd2ZuNHNz-xyZOnm4bz6U04FwsYXl2R8YC4lnXKJB0VYFJWGyJ_JgnDMBzGafQxnlj9BUIVx9eeVDyOf1FXQ1pR_7yV6k0qzhdpJFRfH6jyHdQpbNdu0b7eJaVAYjQYVjXE8vIOwEVsivAZDcqosmREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | سوئد دست در دست هلند و ژاپن صعود کرد!
🇸🇪
سوئد 1 -
🇯🇵
ژاپن 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/95977" target="_blank">📅 04:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95976">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gtDEzOSnPnSUorewYnWU7RRyoFlW6QiCSYSr2YWQlN0DY5PmrdnSdZeLowCStOL5AYRDFz0ibuGXXC_s5hqEESmuNDctYcy0Kk3le1sB_lWPRNBrCq7n_cQDmv-5kgyLLZb6MbEOaX-emLswAyU6mLCj6jq7wejfOhorFcOYIVoQvAExRP_NAJ6zGVNXHzB3PGDTT-Itu7eJQjbrexNPJLgZcZbcWxT79kEgJimgJzlLejyG1oNndhwgsPxlxlZgg9Al7cd0afd7DuAX2Y2t2lzEBEK5LrB1Hq5b1O12cFF284lamQSdqs7KbLrjeQbRSFLE5BVbDbMkYEwEHkdEoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان بازی | زیبا مثل لاله‌های نارنجی؛ تیم کومان احتمالا حرف‌های مهمی برای گفتن دارد
.
🇳🇱
هلند 3 -
🇹🇳
تونس 1
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/95976" target="_blank">📅 04:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lMHRtY05ok6qDq9tmoNivr0y-5JGntkudKG4w-sU_hex7ZIf6yhQY9Nmeudp-ppil768b93DzTHhGQCU4goI0ZL-SFxu2TZsnku4Qoszd_twYoIv88monK4Q2QnTbxl0VAa2Pt6cH2HH9A_Dy4S0-zz794asfjgguyAVG_ozcS5bBVTXObicpnUlD_DJNdJBvVF1v7n_HSfIhXousNt1tRVIuidG1ubtMJy8Bt5dSLZLy-MT5YF2TVM_AzC4DsxHku_lKmV7ojMfjopANDvaQax2Qygp8AFiBxqA1vRQFor4_4qjLVWlsX5U1B2Xv5Y6m17u-_GYM2wUSfdoC9fdJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWOUozY0WL7Dgx_PV_h5lu9iwNhg0lmJUsaPWI0eAIoP_7DhkdBLYajDYhVyS7NnTCiRfChPfqzcdxxeFmwz-n2lMsp_tktoAQKFZOyW_UfeS9mLbdR3URkmA1VGv0IQbvg6k67XNRqw9vmFBpY_-R2vG8SapuHHibMgPyfAqtI9mX9huTDn8GE9ENl-K5QxB3JaRr4z4i8c6fiNJCxqfEuwHrPSd3hUGXd6QBmZI341qILU9ZkIebbnxY-hmOFtYzFtxljDLRq2DMPe-y8hX0LX5CLkikBglANLEhodCgLPui9HpXpkB79VRwhTbFUf-Hkuwffjwxdw314crh54Og.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
🇺🇸
ترکیب رسمی ترکیه و آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95974" target="_blank">📅 04:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95972">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bjkcyo9bOk7HmcvVmc52HlInvvLHiegpcYGb_tfWfagSibn9eLRaTIv8X51k2gHbiAwRJxB4majKJdX_KW0JZL2hD0T1zNWM67fwhckkJ-EeBXspvaJRGmpr-I7AI53POS25SrCxwAKs-mEDolP1q2h8B_lqLan287XUOsXXzPk8rHL8uypABuKPnHhnVmjsSg5adgxwhxz85yJoPApSIInR_sLUlAn8xnjMHz1QM6BpdHsWvwNtUeH1AFdmabi5hYp5Qil7LXrioMRUiciGfNYwU8hW4-kzP5lTdyO9Zncx2_ChTADe2EUs7qGWSXV1inZK_mQkq0BuveZiDruLyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gA5j_M5EBhHdb7cM-XftTYg4yiBqm6blumfzRwXBrFe8YgK76hIGOxnxn3ltaaodlKYfnm2PtVtZ-WSOwpFIyViilkDFivsNI-B24hTS_dZ9rhIIEbJyf4O6f__yrPFSQLi6XT0emzZq2w4QA5tYqUAQhhl6vYk2QJquFaecqxQSPjk5ZuBNnHGhMMZd_9kt7C2Z4ARCHOghT6NrM6bbriJIw1-d9ktWLoveSs4b0S2g7zwoGKYX_x_1iWNf5SCoNcVlmyuy6WRoy6CuCdidHC_2FQe0jHYzI9rHY-8zisIpwN0rOz6x5aLoDLgqMSa7b8vM_qNpUQnRTRnbMZcXkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇺
🇵🇾
ترکیب رسمی پاراگوئه و استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95972" target="_blank">📅 04:21 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
