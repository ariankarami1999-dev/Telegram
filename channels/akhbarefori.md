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
<img src="https://cdn4.telesco.pe/file/eBh4UXPQ2xY0-9vmDHzCdL7TwRWkS5iQfxG5VoVWK3n2Y7ziC0gol_IP-PB9mXyZ6NbdUuwKVOuVhExU6PcnbkvKXSrnqrrUvWgAFE6LycpjUwSu3lc9JYKswvW4etKcH5my_meNJ6AynkIbJGK5EVxWYZYD0-A2Kz2FurihEgcAKNlbMu_5B-uBELPQshtKVXxdcMDAumEsM58_DZ2bnwxqBgxUfXYOFJr2R5W8QJ70TWKD9YU_p7-OO93x_ifiMa-JeJfTelwMAgX6KwgmJUn2m8ACT4YJMLtoU3pIrzA8de3ocm3BbMulq6BfU5Dk116plUpcit6ajCmCGZp8JA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.45M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 21:55:52</div>
<hr>

<div class="tg-post" id="msg-668031">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d1d1a95d.mp4?token=YV9QgYcscd5iJ7Bz8HaVy43c9xl7_WlwBahJqyL_BVzYKIshxP4aQhlKxwCmqpGa-9Dt0qXNpk9-Tvs6S0_Ubgsc_Rb7qGS3bBJ_x3LH1SGnOQTnGSOEY8WdWWTZf5SrpIStRzrEnzibWpWH789Tdyc7sA3z6PXfmLErP6x_0n_oI0KiPI8NLDT3JX2YVmS8EooKYL4ttkUp4AK3pO_GpdsRBNMQdf6F3DU5hVMe2aFbLIdLwNDAP1oelWc1-CIIIHwScieGBVw9DK3HQZUQDpocFRLPhe-jY6dBRhOr4Sy7CGzZMPW0vN79hqfFVvqFjqikkCoKdQbsO-Jz4zZ8-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d1d1a95d.mp4?token=YV9QgYcscd5iJ7Bz8HaVy43c9xl7_WlwBahJqyL_BVzYKIshxP4aQhlKxwCmqpGa-9Dt0qXNpk9-Tvs6S0_Ubgsc_Rb7qGS3bBJ_x3LH1SGnOQTnGSOEY8WdWWTZf5SrpIStRzrEnzibWpWH789Tdyc7sA3z6PXfmLErP6x_0n_oI0KiPI8NLDT3JX2YVmS8EooKYL4ttkUp4AK3pO_GpdsRBNMQdf6F3DU5hVMe2aFbLIdLwNDAP1oelWc1-CIIIHwScieGBVw9DK3HQZUQDpocFRLPhe-jY6dBRhOr4Sy7CGzZMPW0vN79hqfFVvqFjqikkCoKdQbsO-Jz4zZ8-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های لیونل مسی بعد از پیروزی در مقابل مصر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/akhbarefori/668031" target="_blank">📅 21:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668030">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
المیادین: هواپیمای حامل پیکر رهبر شهید ایران تا دقایقی دیگر وارد نجف می‌شود
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/akhbarefori/668030" target="_blank">📅 21:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668029">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26e0d8feab.mp4?token=tMY_pw_aOLsFaYSDV2FRP-CGf5rwXPr1Vf0XbOdc_bwzFzQaEF0wX1YuBuG4BIpcFUn98Kw0QB_hk-oUhT3aG2KnzWda4vQ_hn9ck_FtnqHQjt5_LvZ9W1llDoN3_X6ZcaUPAeTHUpc7INjsrC5roEpuxPoOEeME6B2QU7iFylC0amP8Ts3Jr6fn3bVS5j7hJ9VTRWKsRQjIG4ESTN0S2bZ8D2UkJ27J0HhYgS5ClsUajGQr-A1E3FSpXbqyGI65ByZGSf5zY8adbqp7dULoM6q4Plbywb8jt21P0bsTWlQL9FBMuylE3OXnIFda8Qncehb6oz1_XvhWMOj6FDaQXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26e0d8feab.mp4?token=tMY_pw_aOLsFaYSDV2FRP-CGf5rwXPr1Vf0XbOdc_bwzFzQaEF0wX1YuBuG4BIpcFUn98Kw0QB_hk-oUhT3aG2KnzWda4vQ_hn9ck_FtnqHQjt5_LvZ9W1llDoN3_X6ZcaUPAeTHUpc7INjsrC5roEpuxPoOEeME6B2QU7iFylC0amP8Ts3Jr6fn3bVS5j7hJ9VTRWKsRQjIG4ESTN0S2bZ8D2UkJ27J0HhYgS5ClsUajGQr-A1E3FSpXbqyGI65ByZGSf5zY8adbqp7dULoM6q4Plbywb8jt21P0bsTWlQL9FBMuylE3OXnIFda8Qncehb6oz1_XvhWMOj6FDaQXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یحیی قاسم، عضو شورای فرهنگی انصارالله یمن: یکی از مهم‌ترین اهداف رهبر شهید ایران در موضوع یمن، شکستن محاصرۀ یمن بود/ مردم یمن به برادر خود، ایران، تکیه کرده‌اند تا این محاصره را بشکنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/akhbarefori/668029" target="_blank">📅 21:52 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668028">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab1a9a6df.mp4?token=p65iS_0tQiAQXuayGD-UIkVcoWWkmJkZR_YnGpkkhPe5D_jszLxoDLkvsE2rCwhcVHGe-EESNKE7BkinVA5FFcVdCBsNuTBigo4AxF6ReoNsUtWmeUSScc0Lpwnas8S6bceCVD170I5ttXDMKolOsy8i8F8GOqlhL7-XZEFttkRB7EUlZrQ5WG9DsPa-x7ut_jtgORGLycOKTCk6nDg8u6HIE-1BxJ-E2S_-LwA2CtJNsVtykpgzdJ2wsjpIWCE4IgrYg2n824itK94TlHSRemwdiXoazvHn1jb0AJ1YFjquByhAV6JVQIjSUpC_vunKwg7h5MeOXPBSe3vN_rp_gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab1a9a6df.mp4?token=p65iS_0tQiAQXuayGD-UIkVcoWWkmJkZR_YnGpkkhPe5D_jszLxoDLkvsE2rCwhcVHGe-EESNKE7BkinVA5FFcVdCBsNuTBigo4AxF6ReoNsUtWmeUSScc0Lpwnas8S6bceCVD170I5ttXDMKolOsy8i8F8GOqlhL7-XZEFttkRB7EUlZrQ5WG9DsPa-x7ut_jtgORGLycOKTCk6nDg8u6HIE-1BxJ-E2S_-LwA2CtJNsVtykpgzdJ2wsjpIWCE4IgrYg2n824itK94TlHSRemwdiXoazvHn1jb0AJ1YFjquByhAV6JVQIjSUpC_vunKwg7h5MeOXPBSe3vN_rp_gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
استاد عابدینی: خونخواهی امام شهید مقدمه‌سازی ظهور است
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/akhbarefori/668028" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668027">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبیمه البرز</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/292a7f2565.mp4?token=FyumLOb5cjHzFGolbmZf_ukCWhx4DKrMxuJuq3_CIhk9eXPicPx_L3Q97De1NLPvHI9ZNcbofV1y7ohwEIuTGODp5r0N4q1ySkeJNexwRge6Ptmz5LLoD_UG27B2lyjpWw1HxlfpUvvTbxYYhTYYsTFxLKXqugRMyr3kdsIkPXXvaTB__o8gRJ6JUBFBhJdfQ0Xw5BWz0Y4mXMPDpg1o8eoGjOUowXer0P2mZWe-Q4gdiLGb4dvkAAiynG-2X5m4Hl0c-GzvBhEu4NqA6tBEkzVBZpc9kcxhuVC0dY1Qg1ExU5hroI3IBiVobXs9jayeYusBT7It7_11xzz2NqQB8ZG4LE18SI-px0j5S_8bKhn9saP-iXklkdRBMrW1jRWFb1E0n6khXLSkG6vprZ4l7NIXYZz0f1JomtkvPwS2irGukg6Lp4qdBAmKd2NDUA2WAVix0XePDf7HLvqgEMNMZTgrf_t00ObDOogro0cnvNCER0cCrTz6jt-8IRFxnn8HbnfmGhJlDGOYd07DJoW5LrbJUBnQ1yzQiN5x0SyAGTFloebphBleOrpACOKN1qnesJWYaAke--_0FefNcJowrI64nUniGOjZMhb_fTAPEIEJwDBVH6CQ4uPXeJC2FmWZw7D-MVoNjuK6dQzaMxt3birvp-ngwOcQ2mq3Z4Kwbdk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/292a7f2565.mp4?token=FyumLOb5cjHzFGolbmZf_ukCWhx4DKrMxuJuq3_CIhk9eXPicPx_L3Q97De1NLPvHI9ZNcbofV1y7ohwEIuTGODp5r0N4q1ySkeJNexwRge6Ptmz5LLoD_UG27B2lyjpWw1HxlfpUvvTbxYYhTYYsTFxLKXqugRMyr3kdsIkPXXvaTB__o8gRJ6JUBFBhJdfQ0Xw5BWz0Y4mXMPDpg1o8eoGjOUowXer0P2mZWe-Q4gdiLGb4dvkAAiynG-2X5m4Hl0c-GzvBhEu4NqA6tBEkzVBZpc9kcxhuVC0dY1Qg1ExU5hroI3IBiVobXs9jayeYusBT7It7_11xzz2NqQB8ZG4LE18SI-px0j5S_8bKhn9saP-iXklkdRBMrW1jRWFb1E0n6khXLSkG6vprZ4l7NIXYZz0f1JomtkvPwS2irGukg6Lp4qdBAmKd2NDUA2WAVix0XePDf7HLvqgEMNMZTgrf_t00ObDOogro0cnvNCER0cCrTz6jt-8IRFxnn8HbnfmGhJlDGOYd07DJoW5LrbJUBnQ1yzQiN5x0SyAGTFloebphBleOrpACOKN1qnesJWYaAke--_0FefNcJowrI64nUniGOjZMhb_fTAPEIEJwDBVH6CQ4uPXeJC2FmWZw7D-MVoNjuK6dQzaMxt3birvp-ngwOcQ2mq3Z4Kwbdk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از شور، غوغا و میزبانی خالصانه خانواده بزرگ
#بیمه_البرز
در آیین تشییع و وداع با رهبر شهید انقلاب.
در این ویدیو، روایتگر حضور همدلانه مدیران و کارکنان بیمه البرز در چندین موکبِ پایتخت هستیم؛ جایی که با تمام وجود، شانه به شانه مردم ایستادیم تا سهم کوچکی در تکریم زائران و این حماسه عظیم داشته باشیم.
تقدیم به روح بلند رهبر شهید انقلاب که صلابتِ راهش تا همیشه جاودانه شد.
#مواکب_بیمه_البرز
#روابط_عمومي_و_امور_بين_الملل</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/akhbarefori/668027" target="_blank">📅 21:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668026">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7eb0eeee.mp4?token=LdIEt7pCPoUmnahTOsothlyDmbjHQzs4tJdHLBdGqH_Fz1_8U3Ow5YSBPw6lMIUpAj_oRF1UfiEq9zQ5V0oGouCIFMvgUXDT8pADpap7klm5PWXz1xwZSd3NT-rBI-TkL4Ap8173ruBDXwQrx1rIuMeluA_PvpLd-FBO_332ET2RgmZ6Lk7Zm1IpLZZn-k6mnvbx0DRhpf8rMlQ8qVR8KJ-GPFtOn1S_Cd0PC69Px6zW65112p311otb5knrA4pBK5NDm-uH63-KPujsApWRNdGc8IyYzDVderun2Gw3VV7uwqEAdjUMtpZ1N9lVUYZnpcL2ZkxnTpZgn8dZ1RDJfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7eb0eeee.mp4?token=LdIEt7pCPoUmnahTOsothlyDmbjHQzs4tJdHLBdGqH_Fz1_8U3Ow5YSBPw6lMIUpAj_oRF1UfiEq9zQ5V0oGouCIFMvgUXDT8pADpap7klm5PWXz1xwZSd3NT-rBI-TkL4Ap8173ruBDXwQrx1rIuMeluA_PvpLd-FBO_332ET2RgmZ6Lk7Zm1IpLZZn-k6mnvbx0DRhpf8rMlQ8qVR8KJ-GPFtOn1S_Cd0PC69Px6zW65112p311otb5knrA4pBK5NDm-uH63-KPujsApWRNdGc8IyYzDVderun2Gw3VV7uwqEAdjUMtpZ1N9lVUYZnpcL2ZkxnTpZgn8dZ1RDJfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عمار الکنانی، مداح معروف عراقی برای آقای شهید خوند.</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/668026" target="_blank">📅 21:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668023">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mlCTrg78pknELeOQtRE-amizyUH4p_LA52GJBeTKz82zlbVJaGs-M_zom0FqiYaG7iJh6wi1MgHJtHlifIsctyzJSGKeXMUPDDyjfUTOhMxwgW6PQbJetYLHY8gkaSDqZDFpXY0e7nKxrjP1fioJs7yhmZphAsOTMu-_-mhDXPGZyYuhx_xlyvMZRYaxAnska5rh3LE5YvwbhuGmoKGD6S8IDo3iZccnifLH2zoPa9g0BXvYj2ijf6ez_tPIGdwMz0WXtcKjy3f8Efx_WY1Fnk2OxEHgGdDfGsop84kIO9SJ1bFjgxk8GV4-Geet9DKdLfvK_hlGuRBMj1MH-rsiOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXsKDta8_Ld2kfu2Mo3PnnCStPz9qkY1NydwMXQ4si4GcHJY_TjKo5a3Z1CSqxWAXf6iBqy8s8iUs-eCRmW5J5W834Rpf7PJwufzuZKxkdndj3kucYQKHtVdfmsyawybpm-e1J-qmqlYJcQ2lTEy5MO9e0J2SFkIbNU6vudTcMIWR9Swt9jyIFRvSfg_V8nGFahXQpDWCEj5mpnPGUvF7pGwEMX2mYs3e5IRJvWHmLUMDsoaQ6rYh7W5GvLkbLgcEc8MZPp4UrDRCGzUEg2WA9oWTeApBy0WK2JVKvR-eZx9tnE4Lb1n5ApPDJ7aW721yvffF-PwJc5FJjw3VPMSIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d2b22b2b.mp4?token=mXmV1fTS6seU0DHDHckFabDHTvx3Yna9jQOMFz1-BgkSp7wU1WIfiXQYwVtpcr56FtMp9pnuflXCXPiDRmqR6iuAGZeHM9k0qhNBdIECHluz3jVsj7hutWcW9isJS7M26b6Lc51g1q3xbbyvRa1xYYMhYa8IvSxWILoOTEPEOfjLqc_yNyYJl7Rl2HOQHToo4Pil7uObOKnAQdbpgqwH0TtxcQxjXoLRdHKx0KfvxsljmmvyVYIefQCusLZsQovJ4lJmqSwAGNn4PQn4i7Pt4lcDVyRtf_SM5MR2kr0BfQh9R7tuVAzkqlnkrr0V6DzVSIOSiKtHXgteO42KFcQSrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d2b22b2b.mp4?token=mXmV1fTS6seU0DHDHckFabDHTvx3Yna9jQOMFz1-BgkSp7wU1WIfiXQYwVtpcr56FtMp9pnuflXCXPiDRmqR6iuAGZeHM9k0qhNBdIECHluz3jVsj7hutWcW9isJS7M26b6Lc51g1q3xbbyvRa1xYYMhYa8IvSxWILoOTEPEOfjLqc_yNyYJl7Rl2HOQHToo4Pil7uObOKnAQdbpgqwH0TtxcQxjXoLRdHKx0KfvxsljmmvyVYIefQCusLZsQovJ4lJmqSwAGNn4PQn4i7Pt4lcDVyRtf_SM5MR2kr0BfQh9R7tuVAzkqlnkrr0V6DzVSIOSiKtHXgteO42KFcQSrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کامبک شیرین آرژانتین مقابل فراعنه و صعود به یک چهارم
🇦🇷
3️⃣
🏆
2️⃣
🇪🇬
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/668023" target="_blank">📅 21:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668022">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00947cfef.mp4?token=FodAmwiReIdRwJCdM6Jvp_FJ6DAYljISSujYBrvFFSwHBT5DvKrvZL3MyrjD7BULSHSwnjUZDIF8g3peExMjjAY0i6X1b9oX6mhnc9t72ENxEZ9-x15-BLPMXpOyyu7bWkE3pzbkYwliRtDSo8qrbllM8PKKei8ceS3buty4KeoV97eHJ0ebWkV-QQXtRy8ZuSB82rGpqhQ6qVwnlfnKdI24zcv9jXt4Q8UZ43hkVm9OTDVm4dR92jGzttSHo02zZehZk_aHsV35HJuSCC5hzTm7-bJbdbIn7newHducutOEF45JvS_gZuvcW_RH8BzBe353Ml3Iz7nrRSrY_Ciiew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00947cfef.mp4?token=FodAmwiReIdRwJCdM6Jvp_FJ6DAYljISSujYBrvFFSwHBT5DvKrvZL3MyrjD7BULSHSwnjUZDIF8g3peExMjjAY0i6X1b9oX6mhnc9t72ENxEZ9-x15-BLPMXpOyyu7bWkE3pzbkYwliRtDSo8qrbllM8PKKei8ceS3buty4KeoV97eHJ0ebWkV-QQXtRy8ZuSB82rGpqhQ6qVwnlfnKdI24zcv9jXt4Q8UZ43hkVm9OTDVm4dR92jGzttSHo02zZehZk_aHsV35HJuSCC5hzTm7-bJbdbIn7newHducutOEF45JvS_gZuvcW_RH8BzBe353Ml3Iz7nrRSrY_Ciiew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعید حدادیان: حتی اگر رئیس‌جمهور یک کشور کوچک را هم ترور کنند کل آن کشور دنبال انتقام آن فرد هستند
/
در ایران رهبر ما را ترور کردند که مرجع تقلید و نایب امام زمان و ولی‌فقیه بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/668022" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668021">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67a0271568.mp4?token=JAG0U4wijm1nPCmlhhx_FmpuGI1IIHG2kasxkvcB0dOupP038TjDNU6gFFgvns12r1dPyCGQtUaEu_uZPii4EOymEKt5OSoqDvdFaKxT3z0Qq7rNQLjjZT72sfZL2eg1FLlrn-lnmW2Q1MJHb3wggCUaAYiCgWcaC6abLAy7imPCj4maX3LA3YRYcwfu5liBOPuZszttNG6D68Ockrdgz8ChHWJILWM5wtQiPUodtqMznGdSYb65_bs7nrXGEiJDgSEG5XGnHrRNndnHytqLagySEledTdgPBxEmkbiGYLs7CXodmvT-arU81Y5xwVahExEcJR4dLIflVtyxCwI6sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67a0271568.mp4?token=JAG0U4wijm1nPCmlhhx_FmpuGI1IIHG2kasxkvcB0dOupP038TjDNU6gFFgvns12r1dPyCGQtUaEu_uZPii4EOymEKt5OSoqDvdFaKxT3z0Qq7rNQLjjZT72sfZL2eg1FLlrn-lnmW2Q1MJHb3wggCUaAYiCgWcaC6abLAy7imPCj4maX3LA3YRYcwfu5liBOPuZszttNG6D68Ockrdgz8ChHWJILWM5wtQiPUodtqMznGdSYb65_bs7nrXGEiJDgSEG5XGnHrRNndnHytqLagySEledTdgPBxEmkbiGYLs7CXodmvT-arU81Y5xwVahExEcJR4dLIflVtyxCwI6sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور سردار قاآنی در فرودگاه نجف
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/668021" target="_blank">📅 21:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668019">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqGQ3i9SlUOVsWVpj_JiHnQ6FLJLSW_2AqTh8XV1SshdreibN_3_1-Au_WPMaJi39sxKeaU9CKj82P8tofnwChDNeC6xLzsW2n9SHE0CVARF56_iQc56bLamSrE2HCmHhjgZ8ADm87mVH7H9aK2KGm86cCVZrIXRxlrO5nr9l2ZNhMZi25m6xvujbv3O-H_Z7xw0h96yswfE8NhItT2IF6dRzOwVnd0blVQO7_DVngb49pVZ3CnaUKicKjicGcLEh4lXp7E6v5BBYjrCl9GK-jaU9DdXosIZmjGycW-1FD6DouCavfFs5xj0_lxy8nZ4WBBwX0e1FxDXCJdgMfxouw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uzKBkmTWiUrIe1jdmHw16Mo8gdApiQvH17YsrMFm_Hdhvtkt2ZU4jbAvEjnxM3m3YTW4dk_i2IkeD0GpyUVhWkhCI4m5RA4ii4aRUcMSehRPGiO8izLU4Pkw-S10xJV5Wpo0G6oiUY5ZukoPtCsFxZTcbLYLP40QNJY9g6pemFZ-miOwFoso3dPhbZU2OTMMJ8fZLAylUbpGhyOnlrg224V_jHzBRHr38V6lmwGyYfnlVM0vBGkI43qESZ33x3ZAepiAKQGE3F9GtSk3mAURf1FHhUJ53l5BpRlzkcqWGSYfWJjYxpwZHiV0oHhz-o7ih-dk_hit-Zf2qXENVt68Gg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
رئیس‌جمهور با استقبال رسمی نخست وزیر و جمعی از مقامات عالی و محلی عراق ، دقایقی پیش وارد فرودگاه بین‌المللی نجف اشرف شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/668019" target="_blank">📅 21:42 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668018">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FdigJ7orW-3oK3xL5R7TcjJxvjAL6rj82N6mngAiBJJg6HEybrOxOOgGduDEpfi2EihsmHl8HKDQxUBQ4YgQ1FuqTR0sujYHi059ty_-Ut3T8qQCQZ-1YsMgRD0mVvK3wP9fQtDeOE9pGlLNAJvEo4PGm5X9nyRpIWX2BhkE8qW9iFBrjFEKYthU6GzTAbHU_1YoxMRnX9qYQzMlw3cuwaqrPyb9vffKKxBVgrNEZK3UnJ_OzvcoLlzvHN1H3Qir7dtw43mRLOxdXiWPfFIqNw0P0jJ76myxfYOyL9G84pjYVLIScYHomL-346htTkdzwvz3fkiGB32tL1XpVS3BuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طرح جالب «بلیچر ریپورت» به بهانه صعود آرژانتین به یک‌چهارم جام جهانی ۲۰۲۶ با کامبک مقابل مصر
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668018" target="_blank">📅 21:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668017">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qf4em6_xmvqnCzy4qhzw63SVuj3JfrCnlOQeBAu17NyVpt8fPCzdrHXnoWWzPkK54YKTZpWFkcRX6JHs5otC9zaEuhqe4sTQnvs9McKVAPlBy_KwttrMhmnsged4oaQiXlXdw2YJLHh6IZ5eu84Sjd2B14hLDRP1qcOkz4bQFo9Tbs_Nv0ZrCaXxXGiGEqncEU3UHfO8OgR_pSTPPop88lRJqBG_m8JAtFkFyJU5pr8iXFWVRJw6bEiO8Qs0H3J-Y8rDkkv1fo3o3qDRQyZPBEB0ilLti_0R8eHyM6pk-tibxNOXkhQEqO0EuGsG9MjDW6najdYriYaa0z9Iv8tqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل سوم آرژانیتن به مصر توسط انزو فرناندس
🇦🇷
3️⃣
🏆
2️⃣
🇪🇬
🔹
طرح طلای بیمه زندگی پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا     #بیمه_پارسیان #بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668017" target="_blank">📅 21:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668016">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3198a22e34.mp4?token=HGlrpyGP1Y3Wr3PmKhZXRf-oa9Bu8rTI0lS47OGmBNHPlEntJSFtZ7G57ipzkqcLyIaiKfH2K7HIS_6qZsDXUTxy6It8W265ME4pfb02PRW_Yzp05srwsGsmI36wpVwcoWhAc5uUZnHrNR6zx8zQAXkLjLMQSIaIUW_wyd2kQUNvBIaZO4te5rWR3VK5qBcRpX3lGSMOrsbOPDNS0LckBPA0ONQr8WLumgmA_c4M0GYkwzX1KKLszWmhts4df2eX2nh1exGYSEPBN_VNlqAwWHNBgwaZ_qM-iCeYn7Duwph1_hiBySb-UcbPx3LvXZy6MLugi9xnNxtYWk1p95IqrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3198a22e34.mp4?token=HGlrpyGP1Y3Wr3PmKhZXRf-oa9Bu8rTI0lS47OGmBNHPlEntJSFtZ7G57ipzkqcLyIaiKfH2K7HIS_6qZsDXUTxy6It8W265ME4pfb02PRW_Yzp05srwsGsmI36wpVwcoWhAc5uUZnHrNR6zx8zQAXkLjLMQSIaIUW_wyd2kQUNvBIaZO4te5rWR3VK5qBcRpX3lGSMOrsbOPDNS0LckBPA0ONQr8WLumgmA_c4M0GYkwzX1KKLszWmhts4df2eX2nh1exGYSEPBN_VNlqAwWHNBgwaZ_qM-iCeYn7Duwph1_hiBySb-UcbPx3LvXZy6MLugi9xnNxtYWk1p95IqrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سعید حدادیان: مردم با پرچم سرخ حاضر می‌شوند تا به همه نشان دهند که خون‌خواه رهبر خود هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668016" target="_blank">📅 21:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668015">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCALY7-EnO6Yde1raiQuptUX2Wnn7_si1X6u8PT-gf4tQmGGheO7E9m_xXqpbgB9nvics_v_XaaefvSPDd3TB3mftataMMSnXdLl1rV5XGsG_ycetSmFVBCYD9v8La2r_Y0-mNEHFEdsRI6zSDci9St-shTi-UjaDqjsHhhbMmP7plwxy-PlBZd_e4D2ZSb2VuEkC30VzOdE7d1zp5uOAKp5mTI6U3TtBCJOlDEzz9uH1nvbekHAOqogKiPeXaMaCU-g58N9PlD5O0LBfhfwCqeinlQChV_ilvLsyo8fyO8S_9q944cbgxVhF6RbT6oFviPFwxvhinYwkj3-O3GBuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
تمهیدات ویژه شهرداری مشهد برای میزبانی از عزاداران/از نان گرم تا عرضه کالاهای اساسی
👤
مهدی یعقوبی، معاون محیط زیست و خدمات شهری شهرداری مشهد:
🔸
تمهیدات ویژه برای تأمین مایحتاج زائران و مجاوران هم‌زمان با برگزاری مراسم تشییع آقای شهید ایران پیش‌بینی شده است.
🔸
با توجه به پیش‌بینی حضور گسترده و میلیونی عزاداران در مشهد مقدس، تمامی ظرفیت‌های خدمات شهری برای تأمین اقلام اساسی و تسهیل دسترسی شهروندان و زائران به کالاهای مورد نیاز به کار گرفته شده است.
🔸
در این راستا، ۱۳ جایگاه موقت عرضه ارزاق عمومی پیرامون حرم مطهر رضوی با فعالیت ۲۴ ساعته جانمایی و مستقر شده و هم‌زمان ۸ نانوایی در اطراف حرم مطهر به‌صورت شبانه‌روزی، ۳ نانوایی در کمپ غدیر و ۵۰ کیوسک عرضه نان قدس رضوی در مسیرهای پرتردد و منتهی به حرم مطهر رضوی به ارائه خدمت می‌پردازند.
🔸
همچنین ۱۴ فروشگاه «شهرما» با افزایش ساعات کاری از ساعت ۸ تا ۲۲ و ۱۸ جایگاه موقت عرضه میوه و تره‌بار مازاد بر ۲۱ بازار دائم شهرداری مشهد، آماده تأمین نیازهای معیشتی زائران و مجاوران هستند.
🔸
هدف از این اقدامات، ایجاد آرامش، رفاه و دسترسی آسان عزاداران به اقلام ضروری و ارائه خدمات شایسته به زائران و مجاوران در این رویداد بزرگ ملی و مذهبی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668015" target="_blank">📅 21:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668014">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نتانیاهو مخالف تحویل اف‑۳۵ به ترکیه؛  نتانیاهو: این اقدام، تعادل قدرت در خاورمیانه را برهم خواهد زد؛ من این کار را انجام نمی‌دادم
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/akhbarefori/668014" target="_blank">📅 21:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668013">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
یک مقام آگاه به پرس‌تی‌وی: عبور و مرور در تنگه هرمز، مطابق ترتیبات ایرانی انجام می‌شود. هرگونه اقدام تنش‌زا از سوی آمریکا، با پاسخ فوری و قاطع ایران مواجه خواهد شد
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668013" target="_blank">📅 21:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668012">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f97ff1390b.mp4?token=LHbt3C8FtPaGarIlmV8RFreZY62iXfsXzbAqytV3Ah8HMEjUO_l5Yr9SPXiBEytIFa29hiN9ZgVnd3YDRjFkvbXcxiWIjS2xXfBx-EGQgvR1ZKV3XGRsh9mK_U1Jvpf8wdDWAPwFFu8ibNwRXWah1ZqEFwewRSUZXHIMGKmG743y4_ENGSDsICEEFBfUOidWm0xJjTSgl_MOoVJ7gEDM0rHNQmbQH1JaosLR6QDxtfn_fT5qZkAZwodApbvvLb-f5q-EVyBUgNOEztqbA_KB_QBMiZGuAIZ1YJQUwNR1z7-YSziLdhWl2UV_MGLqRL2Ogm4V8r6s_9ZMMi8qICURnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f97ff1390b.mp4?token=LHbt3C8FtPaGarIlmV8RFreZY62iXfsXzbAqytV3Ah8HMEjUO_l5Yr9SPXiBEytIFa29hiN9ZgVnd3YDRjFkvbXcxiWIjS2xXfBx-EGQgvR1ZKV3XGRsh9mK_U1Jvpf8wdDWAPwFFu8ibNwRXWah1ZqEFwewRSUZXHIMGKmG743y4_ENGSDsICEEFBfUOidWm0xJjTSgl_MOoVJ7gEDM0rHNQmbQH1JaosLR6QDxtfn_fT5qZkAZwodApbvvLb-f5q-EVyBUgNOEztqbA_KB_QBMiZGuAIZ1YJQUwNR1z7-YSziLdhWl2UV_MGLqRL2Ogm4V8r6s_9ZMMi8qICURnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل سوم آرژانیتن به مصر توسط انزو فرناندس
🇦🇷
3️⃣
🏆
2️⃣
🇪🇬
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668012" target="_blank">📅 21:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668011">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
احضار معاون سفیر ایران؛
قطر: حمله به نفتکش الرقیة را محکوم می‌کنیم
🔹
قطر حمله به نفتکش خود در نزدیکی تنگه هرمز را به شدت محکوم کرده، معاون سفیر ایران را احضار و یادداشت اعتراضی تحویل داده است. در این یادداشت، قطر ضمن رد حمله، خواستار توقف فوری هر اقدامی که امنیت منطقه و کشتیرانی بین‌المللی را به خطر بیندازد، شده و حق خود برای دفاع از منافعش طبق قوانین بین‌المللی را محفوظ دانسته است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668011" target="_blank">📅 21:26 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668010">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a92aa8d628.mp4?token=LOh0_l-HT48gUE-KjA0lujJUztLBNCsIiXBePbbhM-VU-AbYy6bJLIhNID6nH75jmnLRC6CdRtG3sQkTXrlXNDSnIuQmXWiq5h8LCpWeN8JDgVFt7_txIo2y2FDfnNnmScQM0qcvIlrwo7ZF240GfSBlF_7l5ZbCJ3zTn13kIHGS9ndtC-ru9XHFwCvNYDp--L5UbWCbNrgzykBvU6nTKzervY3HTJ9qg3jFXj3UvgZpfbdK52rI8uFeH4xOmQ2clT8twdww7wfClY4orYSCLT3oXOGDquazlkZBtAPuv3_sJIloXQTAt9LJIMersbVAD5MhLspHLGqpwnBqmh3qPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a92aa8d628.mp4?token=LOh0_l-HT48gUE-KjA0lujJUztLBNCsIiXBePbbhM-VU-AbYy6bJLIhNID6nH75jmnLRC6CdRtG3sQkTXrlXNDSnIuQmXWiq5h8LCpWeN8JDgVFt7_txIo2y2FDfnNnmScQM0qcvIlrwo7ZF240GfSBlF_7l5ZbCJ3zTn13kIHGS9ndtC-ru9XHFwCvNYDp--L5UbWCbNrgzykBvU6nTKzervY3HTJ9qg3jFXj3UvgZpfbdK52rI8uFeH4xOmQ2clT8twdww7wfClY4orYSCLT3oXOGDquazlkZBtAPuv3_sJIloXQTAt9LJIMersbVAD5MhLspHLGqpwnBqmh3qPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ستاد بدرقۀ امام شهید در مشهد: محل دفن پیکر رهبر انقلاب در حرم امام رضا(ع) مشخص شده است/ جزئیات دقیق این موضوع توسط خانوادۀ رهبر انقلاب به‌زودی اعلام می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668010" target="_blank">📅 21:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668009">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2b9466ee.mp4?token=eLgHdJ1knT_DlN8AUhrsnv2iiHWIvLkn8l3y-BdvdngTKawK0ghQQE-h4tYCiGkRZR0RtkU3dbUDPJDJGPquCs4i4PQmrokFl8blY_2t3p0ry3vu0WtaePn50AQ0Qo29V2NbwyMAN3GpeuzBG5NMWrDqxbSBFS_Y6ABDPCfLIFUYnAIbLxGbT59T0r7y4g6RfXRLtGMUKvoYqJy6n5cU9-xo-rFibqt7xc82gIPr2sIPwGfw9HGJqpQsA-v9t_fkHgntNL4pVgDVJUsj9qQUR7lCg1WmcUYJbwHQbyct6rReQUm7fraN7A7_H98VFVKIAaESP4d2fWSz3hadGaq48g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2b9466ee.mp4?token=eLgHdJ1knT_DlN8AUhrsnv2iiHWIvLkn8l3y-BdvdngTKawK0ghQQE-h4tYCiGkRZR0RtkU3dbUDPJDJGPquCs4i4PQmrokFl8blY_2t3p0ry3vu0WtaePn50AQ0Qo29V2NbwyMAN3GpeuzBG5NMWrDqxbSBFS_Y6ABDPCfLIFUYnAIbLxGbT59T0r7y4g6RfXRLtGMUKvoYqJy6n5cU9-xo-rFibqt7xc82gIPr2sIPwGfw9HGJqpQsA-v9t_fkHgntNL4pVgDVJUsj9qQUR7lCg1WmcUYJbwHQbyct6rReQUm7fraN7A7_H98VFVKIAaESP4d2fWSz3hadGaq48g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم آرژانیتن به مصر توسط لیونل مسی
🇦🇷
2️⃣
🏆
2️⃣
🇪🇬
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668009" target="_blank">📅 21:21 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668008">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b22b32ff8c.mp4?token=hzSe6_Ci0e0uetFGWddnnBg51da5ptAmMqDutr4vPN5VDbjLSz924qod03aBqCcCqkHS8FsG9jXXmiG9QWgEArfE53pett6l2uZvzHkJADJbbSu3Np6s1ABCv5K2tn7tfEQjDNhJTM-s5tfGEwywrIwf8ahhH5wjR3MTI9FkTB42yUWHjR0AC5oAXCecyIoFQRHgE_F271Hn2uVEz9MhJBpNkU_mcnKzPc6CAw4e2yjtJojaSi9xVX8TIaix8iAD2NkQA15LiSAe5uIb26T6O5FEbXlo2C_-SXDAudPkpcjxqybwdx3sE5PP-AneH5rvhquRe68H4aJBOaDa_e05pIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b22b32ff8c.mp4?token=hzSe6_Ci0e0uetFGWddnnBg51da5ptAmMqDutr4vPN5VDbjLSz924qod03aBqCcCqkHS8FsG9jXXmiG9QWgEArfE53pett6l2uZvzHkJADJbbSu3Np6s1ABCv5K2tn7tfEQjDNhJTM-s5tfGEwywrIwf8ahhH5wjR3MTI9FkTB42yUWHjR0AC5oAXCecyIoFQRHgE_F271Hn2uVEz9MhJBpNkU_mcnKzPc6CAw4e2yjtJojaSi9xVX8TIaix8iAD2NkQA15LiSAe5uIb26T6O5FEbXlo2C_-SXDAudPkpcjxqybwdx3sE5PP-AneH5rvhquRe68H4aJBOaDa_e05pIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول آرژانیتن به مصر توسط کریستین رومرو در دقیقه ۷۹
🇦🇷
1️⃣
🏆
2️⃣
🇪🇬
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668008" target="_blank">📅 21:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668007">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bg56H7HABVKhRx6N7ZV0qSqoh1jqzcIYll9sP6uoPAb1uxyffxVvXMD68eGK10MBiMqCoiFLHquXEqYqJgzA65-WJgCjem4Kfefkoo3ISjfNtq9L3saORqztU_e2hAun2ANXpqqa-Tljvu4SoYgzjvmL2mDcFdMsj55qYAKaM5dfIJZjKSV7pXia8uYxSFSHcLxQTloZCmyyK77eF5kP7aY6Ovmls5nK0E9qpv63xVvfwTUG9WDHJxYadDk98oZAW-vrUA346QcTaw8yTSltGeqHrA2EzziLYKmpPLcxW4pj5RCsX6F1fg2eMpT1kvQX5xeOEfzmOpW-KcR3xAPOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امارات مخفیانه در سومالی‌لند برای آمریکا و اسرائیل پایگاه نظامی می‌سازد
🔹
روزنامه فرانسوی «لوموند» گزارش داد که یک پایگاه نظامی در نزدیکی فرودگاه بربره در سومالی‌لند به هزینه امارات متحده عربی به طور محرمانه در حال ساخت است و احتمال دارد این پایگاه توسط امارات، ایالات متحده و اسرائیل مورد استفاده قرار گیرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668007" target="_blank">📅 21:12 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668006">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPTv1kxhJ14CtYn8GO6Qpn8OgO3Z-tNmBRMAleM1ZqqdgXd3JIAiw6VnenGZsli2G98PJGmh3oI26U_G1iIWcrh67czLd0Mz7kVEJ511cbFNwBzmycomDGD6vtQ02B3W-QT2VSSSVtqV3rfHTGOKIEJV8oMXGp-j_QZQ1KG0-degH3L67XZlkebQ7mxjPXlC2BR2hupM1ZbJhOau87gxQghylbucXs2NzkxuRwjFwrOOLMAt0fmUyl0xCZcv9D3cz2Y7uUpG7JLL1Mb9kRE9qEeAR34v7LgDJcGkdcNNTPy88YtiRCdc-fpt3Y16prWnCYx23jnQbC-7FWQZZEnZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در پاسخ به فروش F-35 به ترکیه: فروش F-35 به ترکیه را بررسی می‌کنیم؛ ترکیه از بسیاری از متحدان وفادارتر است
🔹
اردوغان: رئیس‌جمهور ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه اف-35، یک تصمیم مثبت اتخاذ خواهد شد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668006" target="_blank">📅 21:11 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668005">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/209e13531b.mp4?token=AiD13aUOVcPdBvJbDnPmGefzLVktGO2nt0TQmxuYLqW4WKLxY9VF87KcEx33t2L-n1f1f1erk12BusASbd76PVO7ls6gcfQ0drQoeU3P7r0_Zrf6wNzoAJv3hcBBRY9IAWa8gb78d-fjhDIyDSISuRoCzsPmgiJ42ZUGR8sqfm64WrH2MRYM-JczELSbuniM_E5Jw_VK0d3ffqkmLJ22OOHIaXbqTi5OuHucnYMMHVUF7Ufszh-e0EtLmVoE_IrTxSVUoJCAqpOYEsFToZPcQ-KkNXGB7ZLSGen351VIT8yRmmwWFyC29L8QRoQU7221Uh5qbPI7EcVKdSLMTnx_tZ2eb-ZfIA7CPxkHHI5Ep6obV9shKe02YAF12vYlL_mcYe4JuvHmS1sIOLFUAxTfqDZg_lvAEQ-mc-M4gRUVg3QgWU4IRo62wIKRdPcGQCW6iLdcYBrLNgU6uhV1oQqkDIlJPjlBnnZlGF7j9keviFOBVULejbXr4dZMgFBo0SxA4Jm3XNREbvc917tmW5EHyxN9wjnPnUfLsLDoMJkyBSy1XLeebE4Fo1PpY9CcfGhtGvkvWmuEa-XpWrzOY1EQTE931bvmzt1J0mW-Fhs_k480r7Gm2nsgyEQsrnPkemNmaTa3Cdue3sTnUtIDjYpHBkBJzxs_LNXiiFlkWnuLwQU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/209e13531b.mp4?token=AiD13aUOVcPdBvJbDnPmGefzLVktGO2nt0TQmxuYLqW4WKLxY9VF87KcEx33t2L-n1f1f1erk12BusASbd76PVO7ls6gcfQ0drQoeU3P7r0_Zrf6wNzoAJv3hcBBRY9IAWa8gb78d-fjhDIyDSISuRoCzsPmgiJ42ZUGR8sqfm64WrH2MRYM-JczELSbuniM_E5Jw_VK0d3ffqkmLJ22OOHIaXbqTi5OuHucnYMMHVUF7Ufszh-e0EtLmVoE_IrTxSVUoJCAqpOYEsFToZPcQ-KkNXGB7ZLSGen351VIT8yRmmwWFyC29L8QRoQU7221Uh5qbPI7EcVKdSLMTnx_tZ2eb-ZfIA7CPxkHHI5Ep6obV9shKe02YAF12vYlL_mcYe4JuvHmS1sIOLFUAxTfqDZg_lvAEQ-mc-M4gRUVg3QgWU4IRo62wIKRdPcGQCW6iLdcYBrLNgU6uhV1oQqkDIlJPjlBnnZlGF7j9keviFOBVULejbXr4dZMgFBo0SxA4Jm3XNREbvc917tmW5EHyxN9wjnPnUfLsLDoMJkyBSy1XLeebE4Fo1PpY9CcfGhtGvkvWmuEa-XpWrzOY1EQTE931bvmzt1J0mW-Fhs_k480r7Gm2nsgyEQsrnPkemNmaTa3Cdue3sTnUtIDjYpHBkBJzxs_LNXiiFlkWnuLwQU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای ویژه حرم امیرالمومنین علی(ع) ساعاتی پیش از آغاز تشییع امام شهید سیدعلی خامنه‌ای در نجف اشرف
🔹
حاضران در حرم امیرالمومنین شعارهای «لبیک سید مجتبی»، «هیهات منا الذله»، «الیوم یوم الانتقام»، «یا لثارات الحسین(ع)»، «الموت لآمریکا»، «الموت لاسرائیل» سر می‌دهند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668005" target="_blank">📅 21:10 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668003">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4bkTDz4Adct69JYw2JaM8ZkFhiq2npCuX5o9XOqCZOOnPvQZ-IZGBkgmSSXMjDFKQsbZIrL3VgAJ5-kJWj9yajw8-g76TFxt3Cjwq4iErcw3mGXkl3B1BwF9qu6Hvhw0scmzYLrNwsBahimYiGy04PcWcqVL_wULuRycWmgfk4eCUtouwSFCTajpjw7c2DZbzn7IaAePyaRHnTuKGsMAFWsAU2aa-jQZkiMiTAFlhes5wz7b8daSj8PVn4jhmKqGsDzuSk9f4t-6akMC3LxA3ZalPL6aK91Vm8o53FMSblSwAFRDWx8L6xUJuZbUsZzxaE-7fq7GVUarh7_9XnXiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0896a8c2.mp4?token=D7VRcCD0DYh7WsFaNLz0pE9RHUdDtxVsGHn9YOSDsP4CugfafRNq4HA3r5mPnVyysfEzAGmEiGVDXUKM6ZmaRIBG0aRuwDlHIVaKKGVQguOynSpZC02m3Gf2ZuNFRzYbQuYfxM0fue0w32Vcr2sEszl-qSEsJianAFRBAwZWHq3dlp_sHRFkNfvJCVEzC93fk7uy69WXXKQ1p07z1AzDXkyGm5Sktlo6NfenyIdLYaeCDfaYX1j7j-oCXXusRCieBhy4F-fyG6SazxxX7tbr3zcK3inIMcSgK5MgzzFOwk4a7A3rNUM32_rwo4bbPSU9VOvfXKCGRMzd3sCCVI9bKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0896a8c2.mp4?token=D7VRcCD0DYh7WsFaNLz0pE9RHUdDtxVsGHn9YOSDsP4CugfafRNq4HA3r5mPnVyysfEzAGmEiGVDXUKM6ZmaRIBG0aRuwDlHIVaKKGVQguOynSpZC02m3Gf2ZuNFRzYbQuYfxM0fue0w32Vcr2sEszl-qSEsJianAFRBAwZWHq3dlp_sHRFkNfvJCVEzC93fk7uy69WXXKQ1p07z1AzDXkyGm5Sktlo6NfenyIdLYaeCDfaYX1j7j-oCXXusRCieBhy4F-fyG6SazxxX7tbr3zcK3inIMcSgK5MgzzFOwk4a7A3rNUM32_rwo4bbPSU9VOvfXKCGRMzd3sCCVI9bKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش مسی بعد از خوردن گل دوم
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668003" target="_blank">📅 21:09 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668002">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b73f094fd0.mp4?token=cMz6H1lPTe4pb2Bhv92OO-p_Ps7Ve9J60dAHhBtSOcc3GOfj6Dp6qyB2hn00LYpoEp5Rz5HWxBMvqOm5BsLnNOlJ2c7h_tfTaHWvQkHZIiYExvsai-zXG2vXNVaiiI_XXRXE1hM-ADgay3Y0zZj8rq2CYcRTKHXzQ6XRajo5kksSgRur1Hcm2BRGoDAMqfBS69odXA1zmlH_oE4J1H1ucRlgkm2hlEX7nhPtk1W94oLhnh-zmL9lOeYGcmIo96RPnvXmhb0PWLXU_MbMbyN4tXgU31GRG1gfu026GK9UsN71VEt-IGH25NVqNM6HvEZDmsV0mxefrZwPOHst8sWJUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b73f094fd0.mp4?token=cMz6H1lPTe4pb2Bhv92OO-p_Ps7Ve9J60dAHhBtSOcc3GOfj6Dp6qyB2hn00LYpoEp5Rz5HWxBMvqOm5BsLnNOlJ2c7h_tfTaHWvQkHZIiYExvsai-zXG2vXNVaiiI_XXRXE1hM-ADgay3Y0zZj8rq2CYcRTKHXzQ6XRajo5kksSgRur1Hcm2BRGoDAMqfBS69odXA1zmlH_oE4J1H1ucRlgkm2hlEX7nhPtk1W94oLhnh-zmL9lOeYGcmIo96RPnvXmhb0PWLXU_MbMbyN4tXgU31GRG1gfu026GK9UsN71VEt-IGH25NVqNM6HvEZDmsV0mxefrZwPOHst8sWJUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم مصر به آرژانتین
🇦🇷
0️⃣
🏆
2️⃣
🇪🇬
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668002" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668001">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/genA-ovVjcl2HKR3rjcytY6TDmFj65_txWq2wBuDimifpsCzXO_2wPMNON6vnwOhGAkUvTgfCgW0nYHVafTF9rnqENoNkRfzm93MZFExiddl5pZGPr8SA8HDArc40sdJnDOWVN18UnLJnnhP-I-1J2aiOhsRlHdY2im9T2NL_pU9I947St9um8z14NR_WjgQVm3U-kNLLv7nAa3sbq-m64GBdcwJmwGOAcai64glXfABJf3hwesfwHeeWVyeHSuWc1bdw3wW9Y43FNl6J3J4DkZrOjo1nlLhysbWkRxg6WRJ_2Nbf7Ted94WgvFMgCPK96gz1-gaM_GjOliLaoMkYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نقش شما در بدرقه (۷)
🔹
حماسه بدرقه رهبر شهید، سوگ و امیدواری به آینده در این بدرقه را چگونه باید برای جهان ترجمه کنیم؟
🔹
سه توصیه مهم برای شما به عنوان یک کاربر فضای مجازی، از تصاویر قوی استفاده کنید، به واقعه عاشورا ارجاع دهید و با هشتگ‌های بین‌المللی حرف خود را به انگلیسی و عربی منتشر کنید.
🔹
تصور نکنید بین این همه رسانه بزرگ پُست من دیده نمی‌شود؛ امروز یکی از مهمترین روش‌های ترویج یک دیدگاه در افکار عمومی تکرار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/668001" target="_blank">📅 21:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668000">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTuY6Kbpzu2TiWlhjxhuZQSX7KKSjxCXi0ymcmQ22UeyVvgVjGKsN2AiqBBhK2Ph8TR0qC0UN6W4Zn7ZzIsQx4Bi8XSX7XJpPXVHK_cjHzBgVpGBoj-aA2B8ohNaEDBCLCd541Wmds0r7T3H9165bqMMCeZnSWCkSQk9oOhbTohoAk7LeZdHwAj6b6YmUjBGN0x_E_Po7dfnB2Stgb9PcF-fX68Fe-FdI3-RcU4QhYFtOj3cioTL8BqbN0-gQ9wPTjJNbGlHLz3gEezv4uLlx_5Kd1ccRdR19J8jekD423896ycQW1FK5zGorgF1JSb3Oful_61wYu4HdcDaNIP37g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی از ایران در سال ۱۹۵۶
/ اینگه مورات
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/akhbarefori/668000" target="_blank">📅 21:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667998">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cbAGLbIXlmdt3P_f5AI9w-9H8U9-Y5hjXv9hsD8tHuNJQ47lL6mXN6zoluh_jMFXtK0UBzGSg41O1b1bv0fR1ur4yI06Fimn4B1Fu5vZOLpDYjadUBqeVD_1K8LsTdwamCEBJKJDsFhzOw79LxFP5lNUTdiFWyrn8VVdCc_9bot-sSPxp5Jk7PLftEdOXCQfLD7eL7TlqOGpdrj3x1EQEL3AMJgLEEn3Iojglp3b-ONhZVG68cyvjb-LjIJ7Fc5zF6WyLo_7Iu9NgIwwc49KZdIMHtw7rlZKZkAZ7ySsrHVCBYKLody-8XkGgXfhRDzePKpwslvuZ6BsAHmehdt4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیام قم
🔹
قیام قم این‌بار در گام‌های میلیون‌ها دلداده معنا یافت. از نخستین ساعات بامداد، صفی نزدیک به هفت کیلومتر از مسجد مقدس جمکران تا حرم مطهر حضرت معصومه (س) شکل گرفت؛ خیل عظیم مردمی که برای اقامه نماز و بدرقه پیکر رهبر شهید و خانواده ایشان گرد هم آمده بودند. موج بی‌پایان جمعیت، قم را به صحنه‌ای کم‌نظیر از وداع، سوگواری و تجدید میثاق تبدیل کرد و برگ ماندگار دیگری بر تاریخ این شهر افزود.
🔹
هفتصدونودوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/667998" target="_blank">📅 20:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667996">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b914ae03a3.mp4?token=iS4yCaf5ZoB7GJtOeeaUElvl_9QoRp_lXbBkaaueIU82fIWWp8t2jfsN3uGEA7dZIcgV7zvbvb2hIbrMZcM2JcIJGydl4Bei056toDdiYU6YkkL3dAkdvGtriPaLr2Fj1JNhQVjLwnifSLUGz1aF6qK2rJTdYSqr-c9pIAVz8NKL_5JjIeIuTSd0MLvSi5-FdW9abZhqjXbnR_UlcNnKR-b7IAGp3SJDZhvjcA7EjVmOPg1uzSurwMHYhzDZoN1kB-vV2fckuUYQqowkQf_92xxr2grg1F-i-0qt6OB94pUGJ80wzTa7yCnujoPs9Z3aElGD_R9v4_LQVIMl4V8ddg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b914ae03a3.mp4?token=iS4yCaf5ZoB7GJtOeeaUElvl_9QoRp_lXbBkaaueIU82fIWWp8t2jfsN3uGEA7dZIcgV7zvbvb2hIbrMZcM2JcIJGydl4Bei056toDdiYU6YkkL3dAkdvGtriPaLr2Fj1JNhQVjLwnifSLUGz1aF6qK2rJTdYSqr-c9pIAVz8NKL_5JjIeIuTSd0MLvSi5-FdW9abZhqjXbnR_UlcNnKR-b7IAGp3SJDZhvjcA7EjVmOPg1uzSurwMHYhzDZoN1kB-vV2fckuUYQqowkQf_92xxr2grg1F-i-0qt6OB94pUGJ80wzTa7yCnujoPs9Z3aElGD_R9v4_LQVIMl4V8ddg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فرودگاه نجف آماده استقبال از پیکر مطهر امام شهید
🔹
ورود هواپیمای ایرانی حامل پیکر رهبر شهید ایران و خانواده ایشان به فرودگاه بین‌المللی نجف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/akhbarefori/667996" target="_blank">📅 20:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667995">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پزشکیان راهی نجف می‌شود
🔹
رئیس‌جمهور جهت حضور در آیین استقبال از پیکر مطهر رهبر شهید و دیدار با نخست‌وزیر عراق، تهران را به مقصد نجف ترک کرد. #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667995" target="_blank">📅 20:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667994">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f62IsRryg0j6nKy3lpEijyCWBN4bMvUJIV88iEq0aRjIKkvMSvmyhQkzNvvoOsB5niJOcojRFPGyoDjM_nNaXpl7M2t_Jpz0vQ5BJLsuTuQN__yxbnwPUdsClOlW7gNO69IH-dXyGkX_hffTpZSqLm1Ae6q9oH4QajCqlSxCUypZMxNXGyiyReeKZrUu9yEBFo2H1xv0AIR3HX6_V0hO3ay1LJt322vh-wYTRKIXSwzBgW-QKJo1eB_zjJuom8f78NBuslR0dgquNua5-FDiK2uQEvVnyqDAUfHNRI_GGQh2dMhE9zxVRNU4rKhoeFoVL4XVshiUiLOPGf4ItJ4jmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جایگاه ادای احترام به پیکر قائد شهید در فرودگاه نجف اشرف</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667994" target="_blank">📅 20:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667993">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84dddadfa9.mp4?token=dNIU5LGNVBag_WoHxE26-evDrDKZ45APsgMYgShDImyhnTVRv1nohv-8kOs3o1-Xg_2FojxX_pKbCzGv0WnupW83HJoOAwcViOrGQYPyq8ydKBsHvxVfQjH8NTQ7Ws9PBTY0lCRIwgEDX6myrXeDbF3CY67wWQNCwJhqPxLNUpUrvky4dNlGTHsT_pJnBwT5X0_vYPanKpFxhAKWsS7fU5flTXoY2kVlBqp6-ebA54rIdxhJ37gahFRTsrccAXhDlLYbEwxK72VhtPWS0OQxUdvL6dYq52BeVZl-iI8oh04VdbE47a8PjL38Ee20pMuIqiDTY0vD9vacW6lW5MOPsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84dddadfa9.mp4?token=dNIU5LGNVBag_WoHxE26-evDrDKZ45APsgMYgShDImyhnTVRv1nohv-8kOs3o1-Xg_2FojxX_pKbCzGv0WnupW83HJoOAwcViOrGQYPyq8ydKBsHvxVfQjH8NTQ7Ws9PBTY0lCRIwgEDX6myrXeDbF3CY67wWQNCwJhqPxLNUpUrvky4dNlGTHsT_pJnBwT5X0_vYPanKpFxhAKWsS7fU5flTXoY2kVlBqp6-ebA54rIdxhJ37gahFRTsrccAXhDlLYbEwxK72VhtPWS0OQxUdvL6dYq52BeVZl-iI8oh04VdbE47a8PjL38Ee20pMuIqiDTY0vD9vacW6lW5MOPsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در پاسخ به فروش F-35 به ترکیه: فروش F-35 به ترکیه را بررسی می‌کنیم؛ ترکیه از بسیاری از متحدان وفادارتر است
🔹
اردوغان: رئیس‌جمهور ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه اف-35، یک تصمیم مثبت اتخاذ خواهد شد.
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667993" target="_blank">📅 20:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667992">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e3222f9e9.mp4?token=ddxoN5q_AwOkbBbo8I77UBI3DCUJtb-3bzOChib2h0Q4mqAGB2CzgTrWyJY69Qb4RP9e_09-h6_Vjz2nKG5r8ulKzX6-NUMQm1lgP7m2xfPpnZPe9Yey8qaalXfzOlDUoIjwHyTXhfDB6tMlvGUzBlAV7hxbJHyglUULPkmnCNaOMg1IfNnNGad62Wb-_z8Be6qb2ChDu8QjxZ1W8PuORkEN4pyv0VhKXRwsNRp9gi8kkJEKtqmeiXOrdLj-NqIX09qkRCYpgowvHfdkMTYMGNWLYeO6vBybuYsBjgQreznX4REbJW42o8aY51iUfIKvYS2Fy2dK5CvdQhyzlzEb5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e3222f9e9.mp4?token=ddxoN5q_AwOkbBbo8I77UBI3DCUJtb-3bzOChib2h0Q4mqAGB2CzgTrWyJY69Qb4RP9e_09-h6_Vjz2nKG5r8ulKzX6-NUMQm1lgP7m2xfPpnZPe9Yey8qaalXfzOlDUoIjwHyTXhfDB6tMlvGUzBlAV7hxbJHyglUULPkmnCNaOMg1IfNnNGad62Wb-_z8Be6qb2ChDu8QjxZ1W8PuORkEN4pyv0VhKXRwsNRp9gi8kkJEKtqmeiXOrdLj-NqIX09qkRCYpgowvHfdkMTYMGNWLYeO6vBybuYsBjgQreznX4REbJW42o8aY51iUfIKvYS2Fy2dK5CvdQhyzlzEb5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حال و هوای طبقه دوم مصلی تهران در مراسم وداع با آقای شهید ایران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667992" target="_blank">📅 20:36 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667991">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b882d5a97e.mp4?token=YGrpeqSDtEb7BjUSf2SjOlNOx5AmMUOxBwzNdz7MB6QLjK0FN8N4uCSmMcv8avchxkLJEH-ekpcknNpOh5evnFjSc0FJNVUOZH5PL6LcvE7VJDfiN0CaFaymGOrbMqF_Dd13VyqDe4pn7kP_h0WI0QV--2FiesVbgCHmM1is2n7DSU4rBFnuVF2yvkCt_i4IxjLrPa7lGgBy-_4FlG2X13mIa0szDHx94gH3Y6RXQxWlI5GainSpVhVq9omJh32K4OefQabW10Ur7ivWw2m_q5o7WFg_dI8XdlL6Dqq4nZPVNec6Xq7eI9KbwSA8nNzy-bo0Y_3iH4jTYvcKMfQigw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b882d5a97e.mp4?token=YGrpeqSDtEb7BjUSf2SjOlNOx5AmMUOxBwzNdz7MB6QLjK0FN8N4uCSmMcv8avchxkLJEH-ekpcknNpOh5evnFjSc0FJNVUOZH5PL6LcvE7VJDfiN0CaFaymGOrbMqF_Dd13VyqDe4pn7kP_h0WI0QV--2FiesVbgCHmM1is2n7DSU4rBFnuVF2yvkCt_i4IxjLrPa7lGgBy-_4FlG2X13mIa0szDHx94gH3Y6RXQxWlI5GainSpVhVq9omJh32K4OefQabW10Ur7ivWw2m_q5o7WFg_dI8XdlL6Dqq4nZPVNec6Xq7eI9KbwSA8nNzy-bo0Y_3iH4jTYvcKMfQigw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودرویی که احتمالا قرار است پیکر رهبر شهید انقلاب در تشییع نجف روی آن قرار بگیرد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/667991" target="_blank">📅 20:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667990">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔹
00:09:30 درد گوش بخاطر دزدی گوشواره‌ام از درد تصادف بیشتر بود
🔹
00:16:00 دیدن دو موجود نورانی در دو طرف
🔹
00:18:40 آب و جارو کردن روح مادرم برای حضور من در برزخ
🔹
00:31:10 گریستن سنگ‌های داخل حیات به حال کودکان من
🔹
00:37:30 ماجرای شنیدنی از نذر کردن دوستان برای سلامتی و بازگشت من از کما
🔹
00:53:40 ذهن‌خوانی اطرافیان برای مردن یا ماندن من
🔹
01:09:00 «قضاوت نکنیم»
🔹
قسمت بیست‌ونهم (زنده مانی)، فصل چهارم
🔹
#تجربه‌گر
: نسرین جاپلقی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667990" target="_blank">📅 20:30 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667989">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
تصاویر محل ادای احترام به پیکر مطهر رهبر شهید در فرودگاه نجف اشرف #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/667989" target="_blank">📅 20:29 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667988">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
مشهد به استقبال یار خراسانی
🔹
لحظاتی تاریخی از سخنرانی های رهبر شهید در حرم رضوی و آخرین زیارت امام رضا علیه السلام
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667988" target="_blank">📅 20:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667987">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
آقای شهید ایران با خانواده عازم نجف شدند #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667987" target="_blank">📅 20:18 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667986">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a815167c7.mp4?token=YZVvJXYYBozZvFIo6ap8Tr8Yw_2AI0RnfrRvF9MXU0eNN_I2FLDtW5VcNv3cWUBduyyBqh_f3uZ-4Tw9aEIYLXOU6zAa6Evbllfoq7AmCrjzyRnuqqEo_3lyT_maLc44gwrbf3IDt0USYgoLN_tQlxfzTXPy-1NS2bfWH8-QLgRgHlu5tvrcxDHFZN3ZJ-HseaRi2aT7xSpE1iS_OJ4zKxYKNhXlH8vREFaJ1e_uITmjFETDdH9N-fHnz5-smvZ-fYdfdgrXUZVC6qw1Km4TJX4THWflCPfm6klQ9_nG2-60qgOiDcH16fmPItbe6Yyi8OSC2-df_fvTvusViGRU8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a815167c7.mp4?token=YZVvJXYYBozZvFIo6ap8Tr8Yw_2AI0RnfrRvF9MXU0eNN_I2FLDtW5VcNv3cWUBduyyBqh_f3uZ-4Tw9aEIYLXOU6zAa6Evbllfoq7AmCrjzyRnuqqEo_3lyT_maLc44gwrbf3IDt0USYgoLN_tQlxfzTXPy-1NS2bfWH8-QLgRgHlu5tvrcxDHFZN3ZJ-HseaRi2aT7xSpE1iS_OJ4zKxYKNhXlH8vREFaJ1e_uITmjFETDdH9N-fHnz5-smvZ-fYdfdgrXUZVC6qw1Km4TJX4THWflCPfm6klQ9_nG2-60qgOiDcH16fmPItbe6Yyi8OSC2-df_fvTvusViGRU8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای توهین آمیز عده‌ای قلیل علیه عراقچی در مراسم تشییع پیکر رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/667986" target="_blank">📅 20:14 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667985">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_sfhEXTCQYgSR1kmYigPbg5oFGTj55W19qhM32pBMHoU4p8Z__t1fYT2C4zfdetAr6FuIchWCFCpg55-3Gy33KqR127gStQQs0eNNgPQGeGrMhGWhEuokCwVSiKF9whBS9WJmHMfbGuR_pI1jMqBdMO8qwnRuFaGe7I0kIe6h8tlvDtgj5bTp_Mm_c7wG8hQL0NHh5zM67n--eOfFp0Vygm90HtqtvOEnJtuRZB0AkXSMhrFewuxyy199P2owBu8XLaeYFMVPut4r7U5IcveTTHfRXG_tS9-aLSmuETwzmRoDw1TnRkHW3rUtS_MoS036y7bS5bAkgEO2lWeaF8ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری دیده نشده از رهبر انقلاب اسلامی حضرت آیت‌الله مجتبی حسینی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667985" target="_blank">📅 20:03 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667984">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
تنش در تنگه هرمز؛ ادعای آمریکا درباره حملات انجام شده  ادعای ان‌بی‌سی به نقل از مقامات آمریکایی:
🔹
ایران در ۱۲ ساعت گذشته با پهپاد و موشک به کشتی‌های تجاری حمله کرده و ارتش آمریکا نیز چندین پهپاد ایرانی را سرنگون کرده است.
🔹
واشنگتن این اقدامات را نقض یادداشت…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667984" target="_blank">📅 19:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667983">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
پنالتی که مسی مقابل مصر خراب کرد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/667983" target="_blank">📅 19:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667982">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0931f23b88.mp4?token=hpKG3G27ajOj8Ff4606fC1F15lCDFpPOSvCF2dG73uDYJ9giD29ezQ2bG-7BDF35BarRsBDGR5470LV-EujOHYwp9y1b_Vt7Nr85sL1hMqqsZcNBS7jAifcB_3UynEZmQ--c_mlEDbWmfcXLB3WmmHDPdXZ5tDo5cCy7kwo1U-5PsRSG6qB9HFJAfpeqvlJiqxLiT8EEsa64XXCKPSXi1um6_2ziXFTfSMlOcqgS3OFuswpvwguPlD6MBd3NWbXETYSIEjGL6QBptAGAieKjtwUUwLnyI0Kl4C-1_I73_-OgY0b3RXCl4B8yd4npu458H40GrstH80Dz9IbUsvBFHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0931f23b88.mp4?token=hpKG3G27ajOj8Ff4606fC1F15lCDFpPOSvCF2dG73uDYJ9giD29ezQ2bG-7BDF35BarRsBDGR5470LV-EujOHYwp9y1b_Vt7Nr85sL1hMqqsZcNBS7jAifcB_3UynEZmQ--c_mlEDbWmfcXLB3WmmHDPdXZ5tDo5cCy7kwo1U-5PsRSG6qB9HFJAfpeqvlJiqxLiT8EEsa64XXCKPSXi1um6_2ziXFTfSMlOcqgS3OFuswpvwguPlD6MBd3NWbXETYSIEjGL6QBptAGAieKjtwUUwLnyI0Kl4C-1_I73_-OgY0b3RXCl4B8yd4npu458H40GrstH80Dz9IbUsvBFHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول مصر به آرژانتین توسط یاسر دقیقه
۱۵
🇦🇷
0️⃣
🏆
1️⃣
🇪🇬
🔹
طرح
طلای
بیمه زندگی
پارسیان
🔹
آینده‌ای طلایی با سود طلایی
🔹
بیمه‌ای متصل به صندوق طلا
#بیمه_پارسیان
#بیمه_زندگی_پارسیان
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/667982" target="_blank">📅 19:49 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667981">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4fc4f4f5.mp4?token=cMBqn1tpIZpe6o23yaDKgNO9s8pCcL5NzBINvgL3IHjkouGU-DdKFOAm8FsMggi7zRfFsI_qi_EPM9EHF_IMNkgiNOcttW3ey9Vx-M4c7NttNbE-uqMz2QowRuRB0RwqHnade_x975138mJA73KjeFU5Ac89PBFVIZIs_Opas8X5I54DGIItLcZo1_OclxAKpK6VHDgS4B8GzE3zeLk0viJV0lpthrzxmDG71r__epgx4PvnwU3xS2BLZSnnVWyqhXZCNsW-D7K7pNWwuYFKgTgxwseUcKQHZkm7k21uplrrBgznJNJZwhcbavXzhoSor9RRdtdFcgd6BKjTDGoBZxBVlwVnOUYUC0Q6MXuPe7AImJ0ya9G6VKnMpYYUtlCS9YL6NOMy4BwUwZk1Pxe03UOyJbv9WW0OQHieZgwfguBAchQ17p1mxNkegl1LViX35BcLmxwIkek58tPxBkuhJ_KNefJbiGfMjgrEnr5sdi40Q7uBgXCoroGB9pIurkuAT1p2WyUywwJiuLBJx4djQJ-psEjusFAPWwF1hZgYIotLrS2xDQsLvrCgEagMpFKRw449rL9AWga8_kBeQ2dJRPuOSbL8xvOhfdtCeaewO1AxZzMqY74D0EhJQGlA2YiA50sRpSfy3HOvUlLsOvsHwTAF6WSpRezB46onUtLKWks" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4fc4f4f5.mp4?token=cMBqn1tpIZpe6o23yaDKgNO9s8pCcL5NzBINvgL3IHjkouGU-DdKFOAm8FsMggi7zRfFsI_qi_EPM9EHF_IMNkgiNOcttW3ey9Vx-M4c7NttNbE-uqMz2QowRuRB0RwqHnade_x975138mJA73KjeFU5Ac89PBFVIZIs_Opas8X5I54DGIItLcZo1_OclxAKpK6VHDgS4B8GzE3zeLk0viJV0lpthrzxmDG71r__epgx4PvnwU3xS2BLZSnnVWyqhXZCNsW-D7K7pNWwuYFKgTgxwseUcKQHZkm7k21uplrrBgznJNJZwhcbavXzhoSor9RRdtdFcgd6BKjTDGoBZxBVlwVnOUYUC0Q6MXuPe7AImJ0ya9G6VKnMpYYUtlCS9YL6NOMy4BwUwZk1Pxe03UOyJbv9WW0OQHieZgwfguBAchQ17p1mxNkegl1LViX35BcLmxwIkek58tPxBkuhJ_KNefJbiGfMjgrEnr5sdi40Q7uBgXCoroGB9pIurkuAT1p2WyUywwJiuLBJx4djQJ-psEjusFAPWwF1hZgYIotLrS2xDQsLvrCgEagMpFKRw449rL9AWga8_kBeQ2dJRPuOSbL8xvOhfdtCeaewO1AxZzMqY74D0EhJQGlA2YiA50sRpSfy3HOvUlLsOvsHwTAF6WSpRezB46onUtLKWks" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگرهای خارجی همراه با ایرانیان فریاد ترامپ را بکش سر دادند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/667981" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667976">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QrvrUaH3fiDHQN_IPyVwkGieRCP0FQqztRlfS4q6aHr756beQ6pyX3dRzHxggswfmvPk1IhiosoO69076JvCafqG2uEuNkA1WH9CcI1WADqumVhC84YJqTGTsqKVFyS_5oxYXdHAvKl1XpWoVczzhr6Dzt-CeeZeULPcE2uJzQSGYS4fKmRLP5Jgjfns_XxCHpvvZCZK_Td5RRPnRxKmM0tacmrOhtiDMWt6TjxggEfQpmje4TP4DO16R8DrUCdunRoq4JSL3vML70dJc9O_Ppn_7FU6oim1s9vDQVEVht121f4_L8TkHlNIQuAiWterRncd7JDlQYzabDncKoJbYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j6MW4c6MIZPmHxoMWtA_QvDo264PjmPgfm08fe2gxt-dUgZIn9h9IZOx_BwQb9Xntsk9p4MNdJ8UfZFHAo-Dab7F6AQ5g_PUEle96UZuGUjMeYkGKaQoWtGMMpzbhX7xyaNeEgbokpC7JdXtZHWHU6MfJYrzc9Kf4325E-HIGxpKQe1B45HfUzWq4G4T7-Lj7qzCU6hDoNu3naddFVIRj5TPjnuLH07B5hGKR0s7Q50OEVFcwfE0WsxwDkwYIsiLxUOl1xw3TiAUiE39A8RKNCYft5nowhdLPzfp2TF0a_31-R2ENIAT9MyawsOv27L9Cl-5Qi9VCWO7QTO92TNkhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNo9iTq0cS9BVVDbxTHCGHAlPlmFZliA-K1I4pfNGzYleHgF9yFsSkR53DFUTUtbIXY7cqHP8XSo6RC97WayI3rNrgm1-sKHa2VVjiTgSVWb8JT2ydpvCMEM4mhK4ymLVtHSTC3is8lPaic0a2NsqAI5tosbGWDyy_WRZWrXt8v7nWxqHbjW2wx7cEqpr_w82Cux2GjAXoGMKF8ViaZmhlQDY-zTkL7m0nQzmSNvrqS9evuUNEKHskaysoVvL3Mwn6GckXz6w0JPzvTpHRzv7Pqhaj-dHZQMo7t7bpMqTgNqQgWVEN1rpOvgikGz8hnMWy2eKcoLQdjYet3SSsUMCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k9y9N3pAgwv25JsDPPioj64R2oJkWXFx2AtVZxeh0et9AJLODUlnSnQoT3IPYJZ5fDiWWW-_ChqiJwqiLbnyMHtMy7cPYytMjEex_jpNa7s0hqr6izsYG0Y6A35wv3m8oLSzHXram8xZH8k2bRsir_mZYWoS8jycJHlWL-JgEem_DAHFdPdK2r4iT9Q5hXqQLlVKL9vBwZjC6ctKkav6EXsG_MaHyxDaw91TBclcgaG-YRQOPCi5YZB7j94KzSIQDssw9_5eW2dTAK-w5Xlz795n3Uwv6zH4gaG1E2ZnAlmG4IYIoRjIO-UG_hp2MNaolBYeXhV1iIq0tTCffeJCvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QG-kKfTNf2iYqdxIdz-XtES8nCNGxa70r8UkphiOBtITUL6bVfzJrayEBMNXG-6hVtNIwZENHP9esmZSoWbBIMp5N3zAHdlKAUsqJluKtUP0BlCAOcuLE-yD-IkeKkXUnzUB7xboS6opLtPsREjBEI4X-Uz0khtBlsSW_3Lsxh5VcF_ryHhInbFmseMLh58sVh_hFny4uRew9muKKMJ65dTbMnVkbsZ2DFsuGrr0vkKGfUf_S7oo2_kSmdo4WtQH9xqwsGAwAaovi_p1W5xFmy44R-BE-LhTfS_hPoXMFa7BtAGqTVWB4h4nDBnoMQPlD0AJBeW0q6G-8oibfNe32w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر محل ادای احترام به پیکر مطهر رهبر شهید در فرودگاه نجف اشرف
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667976" target="_blank">📅 19:45 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667975">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=r_gdLqpAS3b7hbnotBonrblLHEkEgsVnJWRQz6QngfsUK9BW-6flGhYReLXxV3lDoO5oXSpU63-hP5T1d9k_7ovt4J2qMMmcpyNtibsYgCFQticEKj-SJjFs9-WK54ADmf738CvPk32Z_6_yMBPixGLDO6yCOZL2C4ROS5rFkSoT5zi9PzNY_IuseoThBVC_dWvhutdAPHxr7UYdxvBgEtnLF4BjAUyV_gdMriwMG34DNekv8t6mrGATKM4X0kM0kASuYUwScq0aSORNNax_y1DoBM9mcn4Oya_fNzdf3N2f_Qg6dgH5bxOconSL-uoUL48Y-rozfNuNwaelORE0iQYA2QDErkxHSyVIX5CkqNOq-w3V-iJSkVxk7hOgFFrMjXniyj8sExO9iMUi196WP0ssuKGutqYnjb_M9sXN5sh-OeNm4yVAfHgKwSU9FBXNg5rLc8bzDe2XxJOXB5pzY1rHYaabpdgHFFbj-D0JFNQ7iVniIXRfGNXCybHvmCW4bvIQotBaX2j9Nrwt4bnv6RChZFOf3TvBstWaV_W0fb3Q3Vau_30XtB5Aw0jvvwYdBWaUwnOAEmbLYGrusQXyNcjwZ1KVot2MJ7pP_i_5lILFB4u67CY3RB4hoNfJ_XBIuyTr_gToCecH81IRXzgKQGk1xJwovELVq_hJBOWMu-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/199cb5464d.mp4?token=r_gdLqpAS3b7hbnotBonrblLHEkEgsVnJWRQz6QngfsUK9BW-6flGhYReLXxV3lDoO5oXSpU63-hP5T1d9k_7ovt4J2qMMmcpyNtibsYgCFQticEKj-SJjFs9-WK54ADmf738CvPk32Z_6_yMBPixGLDO6yCOZL2C4ROS5rFkSoT5zi9PzNY_IuseoThBVC_dWvhutdAPHxr7UYdxvBgEtnLF4BjAUyV_gdMriwMG34DNekv8t6mrGATKM4X0kM0kASuYUwScq0aSORNNax_y1DoBM9mcn4Oya_fNzdf3N2f_Qg6dgH5bxOconSL-uoUL48Y-rozfNuNwaelORE0iQYA2QDErkxHSyVIX5CkqNOq-w3V-iJSkVxk7hOgFFrMjXniyj8sExO9iMUi196WP0ssuKGutqYnjb_M9sXN5sh-OeNm4yVAfHgKwSU9FBXNg5rLc8bzDe2XxJOXB5pzY1rHYaabpdgHFFbj-D0JFNQ7iVniIXRfGNXCybHvmCW4bvIQotBaX2j9Nrwt4bnv6RChZFOf3TvBstWaV_W0fb3Q3Vau_30XtB5Aw0jvvwYdBWaUwnOAEmbLYGrusQXyNcjwZ1KVot2MJ7pP_i_5lILFB4u67CY3RB4hoNfJ_XBIuyTr_gToCecH81IRXzgKQGk1xJwovELVq_hJBOWMu-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون اجرایی رئیس‌جمهور: رهبر شهید، جمهوری اسلامی را به گونه‌ای ساخت که در برابر تمام قدرت‌های جهان ایستاد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667975" target="_blank">📅 19:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667974">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7dcddf39b.mp4?token=TS62WfjhFPm4qvZY0T_XZTDVJXbjHeylrtMKvNDaezL2EnUPejZ0hSx-nqYL4_htnHWj_ClHA55htf0QYqR7inEQwnyv4h3aIve729A-CMdIPN9oGGidfG27KKE09KfejpT2jVaNEElx3z6scysWUaN4YmwbePWi-j5ATjUNJWTHrQIKqlsUe__CIfM9zZqeuJXaoyM9hFN1JmCOSmRF0WsAN_Zsb53BjyGi8h12zy9btfXmcYsraL0MONrEJ5os4y2QiqruiPgv1Ap7uR0vDJN1TXJfz3SUotVZataKRJe9DA97-mmb1bcUeAVtn1oTQHHgnkc22hpBuPboN8CVWyu1lGxeq-VrU1RDPPm-qw8yMiGHKo_KaX7HZKBuWtsAKz-J4Pg1FxiZe8fB_lQz0lXsOaIOgF4HQskL5t7ZE9yMGAQWrVIns48rvcA-YB-nQORtvQQ8fMkW30pUj-ekhjU3L7Me_rNcY0EUF0F3AMIzAQmmd1k5b1jrLQfPiXiy_n69L9pNpSz1toJkuE6uO9qMmNKYiaQhKn29LTu36GdNd-S7aV6SFrBFUnvbeEyF9Qr225B_5JqpkHj7Ns4qR_VKu1JBRLytXI6gBbxxBU792Ho2Gt4-bh-zttlTkdDyIaZw4G8VKNPof8MS3UlPEmziDEGnfIgNVfp-bjgIk6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7dcddf39b.mp4?token=TS62WfjhFPm4qvZY0T_XZTDVJXbjHeylrtMKvNDaezL2EnUPejZ0hSx-nqYL4_htnHWj_ClHA55htf0QYqR7inEQwnyv4h3aIve729A-CMdIPN9oGGidfG27KKE09KfejpT2jVaNEElx3z6scysWUaN4YmwbePWi-j5ATjUNJWTHrQIKqlsUe__CIfM9zZqeuJXaoyM9hFN1JmCOSmRF0WsAN_Zsb53BjyGi8h12zy9btfXmcYsraL0MONrEJ5os4y2QiqruiPgv1Ap7uR0vDJN1TXJfz3SUotVZataKRJe9DA97-mmb1bcUeAVtn1oTQHHgnkc22hpBuPboN8CVWyu1lGxeq-VrU1RDPPm-qw8yMiGHKo_KaX7HZKBuWtsAKz-J4Pg1FxiZe8fB_lQz0lXsOaIOgF4HQskL5t7ZE9yMGAQWrVIns48rvcA-YB-nQORtvQQ8fMkW30pUj-ekhjU3L7Me_rNcY0EUF0F3AMIzAQmmd1k5b1jrLQfPiXiy_n69L9pNpSz1toJkuE6uO9qMmNKYiaQhKn29LTu36GdNd-S7aV6SFrBFUnvbeEyF9Qr225B_5JqpkHj7Ns4qR_VKu1JBRLytXI6gBbxxBU792Ho2Gt4-bh-zttlTkdDyIaZw4G8VKNPof8MS3UlPEmziDEGnfIgNVfp-bjgIk6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیش از ۱۴ هزار نفر از اصحاب رسانه، خبرنگار، فیلمبردار، عکاس و فعال رسانه ای داخلی و خارجی در پوشش رسانه ای بدرقه آقای شهید ایران در حال فعالیت هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667974" target="_blank">📅 19:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667972">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rxpFzz7fKGS4LliUFfjuXiyJby9z8Vs0XUcjJVPKgeh6AA7_rZbOVWNJaJS0MMWtmFa23EveGwsJKq0iWg-xXi7pInDaCm2FK0aaXoXHEPWI-JnZyLbwY97YTfE5v1tSnOOzfdn3EpG1LBOuva2si5RRGSSnOAXdQ8FLaHwwRu-kkaW7Y0JZbmkFdMlvWTuViImFiSn9LSKUkbSHNzBIkb6ScnoS3FgJ1KTTVgL3pD0w5JUpCIiFY7yxfYZgLh5hHvEUA7ey_WhWUVczXLQoqAgrBaohUrKwgJ9eMWws57SsPd-V_hN9dKEZTYvNna126f1Aqk0-gYMwPvgdgBYuTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhiI6Oop7FAHYsvUVyYqcJbWJXKQ0iOWe2OyYU9nljcNxP3DCfJz1EBYJPhJPHfQTC1exiVQ6jxoJIkVVmMYKOvqghEe1vvAcnStpFWINWhIVvNcspB4JTvVBrZqXRCTApu-87efxxCDs8q5-OhsEH3NPs31xMpUD7vXT9rTWqOqxe9HIDa2q2SOuQD9oUFUYxQ2QEOq6Ekafxim4rGkvmKOfRBVUEXqeGEAtSEACq2gxxr22vwnXU3yDxmQ7WAtBqjEKWwfUiiDKri4Yn65SHJMrRnv2nRqBkHRxsRfvh3tLkIRGqzKGE33FPzIIqOoqfyh8SdJIkHb0DDE6zfcNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بدرقه باشکوه آقای شهید ایران از سوی شاعران پارسی‌گو
در حالی که ده‌ها هزار نفر از مردم در مصلای تهران به بدرقه آقای شهید ایران آمده‌بودند، در گوشه‌ای از شبستان اصلی مصلی بیش از ۳۰۰ شاعر در دو شبانه روز بی‌وقفه اشعاری را در رثای رهبر شهید انقلاب خواندند.
برگزاری چنین مراسم ادبی در سطح جهان از حیث تعداد شاعران و مدت زمان برگزاری مراسم بی‌سابقه است. نصابی جدید در برگزاری یک محفل ادبی در سطح جهان و عرض ادب شاعران ایران و کشورهای فارسی‌زبان به ایرانی‌ترین رهبر تاریخ.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667972" target="_blank">📅 19:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667971">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b8a5f57c9.mp4?token=jbiXcwhS4nk30kwIEQgLdLDx_XWBL3l83w8JPCU8AK6FPrW8iQcg5Xe3MtLMWWtBc0eIlHeMQpqBGzyZD9kQe4Hf-dX7KdDZz5t4DRC9nAxb1soeZx2njI7Wsx97Kn0a6MscMj4cY04J5ai_tLQePWC2lzCyBt9x2tzPBpk-4FxqkBbVHAN00xmROxLQvII2uHCwGd9oKSGCeDWnBnWQqxKv7RYc38X_Xkme5NFCIswmgTjCo5aM5b8GHa38i8WhqFlZObOM5Dk2lWlJijq7AXH2IRx3MxM30-T3d-jEa84-5ifu3lOhCHbe7JwlZ3yDzWxP_CNU_QaZkRhDRAj8vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b8a5f57c9.mp4?token=jbiXcwhS4nk30kwIEQgLdLDx_XWBL3l83w8JPCU8AK6FPrW8iQcg5Xe3MtLMWWtBc0eIlHeMQpqBGzyZD9kQe4Hf-dX7KdDZz5t4DRC9nAxb1soeZx2njI7Wsx97Kn0a6MscMj4cY04J5ai_tLQePWC2lzCyBt9x2tzPBpk-4FxqkBbVHAN00xmROxLQvII2uHCwGd9oKSGCeDWnBnWQqxKv7RYc38X_Xkme5NFCIswmgTjCo5aM5b8GHa38i8WhqFlZObOM5Dk2lWlJijq7AXH2IRx3MxM30-T3d-jEa84-5ifu3lOhCHbe7JwlZ3yDzWxP_CNU_QaZkRhDRAj8vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت کاروان‌های عزادار موصل به سمت کربلا
🔹
کاروان‌های گسترده مردم موصل، برای شرکت در مراسم تشییع پیکر شهید آیت‌الله سید علی خامنه‌ای، راهی کربلای معلی شدند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/667971" target="_blank">📅 19:20 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667970">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
پزشکیان راهی نجف می‌شود
🔹
رئیس‌جمهور جهت حضور در آیین استقبال از پیکر مطهر رهبر شهید و دیدار با نخست‌وزیر عراق، تهران را به مقصد نجف ترک کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/667970" target="_blank">📅 19:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667969">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdWU6DcvkSKyH-qWK5a1vqsElft_j3DNLZIzhW4Rmyx2pOxCtvskavRb72WHhgbNNpcweBI7M2hdL2sSV83RDeifk8xZr3BPllN0wWcnCvzwGPCIeVNeuIV9bsxfoK8pmH_hY72EMkHS0_Lpg4SMoaHLVWokh6V-LpYa4IT_E_NMiD30oklXqp1AnLpHnO2YV42Gv1TMMU1l2hh7q3bFVg3iEogRw0ID10W-9Rb033oE3kgWM7SrHrsWiq_U8pEgSdq-YcwpJ0L0u7XL3aQgJjR5uciXg7ujDezlsfVEkSTmWxpcV25nC5LrVCpir4sNvXRg2DRV8cEdmCI_UaEDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/akhbarefori/667969" target="_blank">📅 19:15 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667968">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f66462b861.mp4?token=cTLDgcgDLi-XbXNPnijOibGjM3rPUW7BJkhq0Ixiw5RnUM9uMeJIqhfHN4kHfY1aURHFozk6XdCRM7piY53a6J2N7G4dMxsZvygov38VWnboPl7mxh3PIlm1jcrdIVfuKFkhHgtdrUVlDSNB2O_8sqktUUq78CYs8I1cZFibpjh2nHrhwRjqQ1ajUmHKDaCmC6Fg77Ru3TWLBY4OLBu5X0zoR7zSxBqyLdZ4CLQDeF24UmLApl7rmSoeldey5hEeZOu8Q4J5aLampwRXg2MnWQxJl3sYz3ku_tW9apEwTnuwg6d8ibvlqfcYStKWTW5RXZ-oBzWqdVr5FZLRodTEgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f66462b861.mp4?token=cTLDgcgDLi-XbXNPnijOibGjM3rPUW7BJkhq0Ixiw5RnUM9uMeJIqhfHN4kHfY1aURHFozk6XdCRM7piY53a6J2N7G4dMxsZvygov38VWnboPl7mxh3PIlm1jcrdIVfuKFkhHgtdrUVlDSNB2O_8sqktUUq78CYs8I1cZFibpjh2nHrhwRjqQ1ajUmHKDaCmC6Fg77Ru3TWLBY4OLBu5X0zoR7zSxBqyLdZ4CLQDeF24UmLApl7rmSoeldey5hEeZOu8Q4J5aLampwRXg2MnWQxJl3sYz3ku_tW9apEwTnuwg6d8ibvlqfcYStKWTW5RXZ-oBzWqdVr5FZLRodTEgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراق در حال آماده‌ شدن برای تشییع پیکر مطهر رهبر شهید انقلاب اسلامی و شهدای خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667968" target="_blank">📅 19:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667967">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
افزایش قیمت نفت در واکنش به اتفاقات اخیر تنگه هرمز/ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667967" target="_blank">📅 19:08 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667966">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dUGvOFfHsQuHoS3QJd-H0BcXlXzPvH1WwpEUwSPSbz8MTcaQ7WUcGdlvr6_yFWUYhexftP2YEdDtJO2woBd62Ee3nrnLApERbIf-tQRbcnh7ANsTvzZCy0pJ4ZTzZIQqeO_h_j4Z6LN7Iwr4zrKVygnS2qcSxACWZAkN8uyWJ7wI0Ml7v-UvrhHtHRn_lMYQxrQSeMrXQmL21C4yBmloCMZ-F67PGRMo-i_rvISXqawSu08zJeVvTcrG2JMxUHbeBh8Wh0Y0gck-4O99F2_kUx_m_wa0Ga4PaW5Kibc41zrsbwWVXyuQ-LPlfOiRSUFUZ-L025ib7tOMETUYeJiT_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▫️
استخاره با قرآن کریم
👇
👇
#رفع_مشکلات_شما_باذن_الله_تعالی
🆔
@estekhare114</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/667966" target="_blank">📅 19:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667965">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41d98d13b9.mp4?token=OQYFAVw3MxEGFBohIoktUeKiiC3eBBks3kWMqZr8b-_f0dOkRGp_q16TTE9ArXGzuslqqOuyQDEUyDa6fjP4zf5fFudZnBtA4IbCo77-1cjZNUvSqCyg40g1R_eDuU05QO0hT-1R_mhv-RSeoxbB023nnDeOlmM0ZFXh5RS9pbS9th8b4GZZTakEoymFuQuAxsBzY2S0zGzrPws4a6LLasDFttpVAnoDm0IChTKDY5UTn1-WpeFywLUvYzD8uNEDPgeqKXunYiT39vGmbKa62wKksYni3nmXAofNP3y8M-TnV8dBMGGdCgt7j7nreFwEKWClqH2LaF_Vbus_OC8QEJ6IoLYFDAr5jUP7WVXSdISCIsCbUkn0mnxAWW-kUBc-jHOx81745MnaFBoZVwN-gH3gTDDEfMG2SWmwukK6PIAzvPfbu2yuLO8YY0H_5Z1EWPdPpLlrSE2kZszyL1DcJH9i2J1_9no_Ci7VLf-uTuInfhvi9dH_ZxMI9_6bXAk5l0h9qaO26vjtNar3bRNnjPDj5d3yhFy-0813hPHJbMceHKu3RzDKzUnse9ChBALU5zVozMDkYYPB9akv2TPoxAfYdLNMs12exEd1DjcdvgzLpzlmS0ekykcAeftUcbD_Yn-KbfJ-qkTlQ4yw2tETdmFuE9vZTOQhC8zoOMftrS8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41d98d13b9.mp4?token=OQYFAVw3MxEGFBohIoktUeKiiC3eBBks3kWMqZr8b-_f0dOkRGp_q16TTE9ArXGzuslqqOuyQDEUyDa6fjP4zf5fFudZnBtA4IbCo77-1cjZNUvSqCyg40g1R_eDuU05QO0hT-1R_mhv-RSeoxbB023nnDeOlmM0ZFXh5RS9pbS9th8b4GZZTakEoymFuQuAxsBzY2S0zGzrPws4a6LLasDFttpVAnoDm0IChTKDY5UTn1-WpeFywLUvYzD8uNEDPgeqKXunYiT39vGmbKa62wKksYni3nmXAofNP3y8M-TnV8dBMGGdCgt7j7nreFwEKWClqH2LaF_Vbus_OC8QEJ6IoLYFDAr5jUP7WVXSdISCIsCbUkn0mnxAWW-kUBc-jHOx81745MnaFBoZVwN-gH3gTDDEfMG2SWmwukK6PIAzvPfbu2yuLO8YY0H_5Z1EWPdPpLlrSE2kZszyL1DcJH9i2J1_9no_Ci7VLf-uTuInfhvi9dH_ZxMI9_6bXAk5l0h9qaO26vjtNar3bRNnjPDj5d3yhFy-0813hPHJbMceHKu3RzDKzUnse9ChBALU5zVozMDkYYPB9akv2TPoxAfYdLNMs12exEd1DjcdvgzLpzlmS0ekykcAeftUcbD_Yn-KbfJ-qkTlQ4yw2tETdmFuE9vZTOQhC8zoOMftrS8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای شهید ایران با خانواده عازم نجف شدند
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/667965" target="_blank">📅 19:02 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667964">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPjNFvTiFhX0UjKJN8s01PNa570pw6BQEMQJh6UMHsVfyYckgRWb1SCLAD9CRHu-G4LIhIBJ7b6sFfBibEUmI3rcHwhA-HKKo4HH-f2c05fhJRIS_ZCX-deDHi457OKXchgyth9ISgRxoCd3GHrWJTR4vwDaLMURJKXjOmFP4R2J4lruzz9w_XvnM-AThkT6CwJBjji5XfeT8voLYX7rLBG9SHiS2UZ_UXmtr4c_ydL1cJ7XXI89T62hH7Y3buKTHhKuriM01O8VjXNOAs9NbpQeCzp1LqWGor6l2363T0DAGAdgwCQHCQSorbS1eE66MNs4F5v-2RVV9Ez-LpI-Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/667964" target="_blank">📅 19:01 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667963">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75695327d.mp4?token=fXj9GifYrv8WOi6Ww2GnVyWOEcBnBd_1m8kVC0UJhf0iiQu-q7MWAGg30Y1Hys2qM6jeGVHifuh6OlVZy9rMa9HN4WiBhdS2WC7axTz4JPnlGi8NDJFjhJ6awSCxb13-b3rjEIW1qk-G1OB50rlLhs50byGDtSjIGzYEgbzKyQI5e-D0m3hkgWHuMUMJ9k00j0wnSAR9pOpi5z7P0WFMfpXGJTQ3cQGe1rW50rihPTDElFyZmbWBTmDzhW908Ee35T7wH9_1ZSd_uqNy_-4GElg7vOf3yMrx7uZoJvIjLVxjdISi2YdBa74fYWZzxwnnI_MTZVKGHFBYCVhZNRMU5gjxcSzEwQDiAzbrTCrlLywA7Br6BpjPCGjwPdueJl_EE3KxeArQ98PFjLQfT4Z2w0MyO0QXyFsx5JIPQWjXPHbkM3KLgqah8J96A7VC9pcMi9rdeQrts4fRkO_vJRqudjDxQO069UVZXOGVAq-4o_4PjTsN-94u7evFDblExrxbVS4zhAwIgQ-O2jwJFQsbOjLzAnKMM6KlawXLlw24EPTPdCemeDISj39YnjFJRsuUpZTR7vs6MxSKCUN61M4mDlFJa0We_l7CWXmQ9JzuuW2F-ZaMJ5MDjBqwAam8BtCzkC8k2R-A4e_9_2A0W1aFfngCIk1k0Fi2GV4zujPItGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75695327d.mp4?token=fXj9GifYrv8WOi6Ww2GnVyWOEcBnBd_1m8kVC0UJhf0iiQu-q7MWAGg30Y1Hys2qM6jeGVHifuh6OlVZy9rMa9HN4WiBhdS2WC7axTz4JPnlGi8NDJFjhJ6awSCxb13-b3rjEIW1qk-G1OB50rlLhs50byGDtSjIGzYEgbzKyQI5e-D0m3hkgWHuMUMJ9k00j0wnSAR9pOpi5z7P0WFMfpXGJTQ3cQGe1rW50rihPTDElFyZmbWBTmDzhW908Ee35T7wH9_1ZSd_uqNy_-4GElg7vOf3yMrx7uZoJvIjLVxjdISi2YdBa74fYWZzxwnnI_MTZVKGHFBYCVhZNRMU5gjxcSzEwQDiAzbrTCrlLywA7Br6BpjPCGjwPdueJl_EE3KxeArQ98PFjLQfT4Z2w0MyO0QXyFsx5JIPQWjXPHbkM3KLgqah8J96A7VC9pcMi9rdeQrts4fRkO_vJRqudjDxQO069UVZXOGVAq-4o_4PjTsN-94u7evFDblExrxbVS4zhAwIgQ-O2jwJFQsbOjLzAnKMM6KlawXLlw24EPTPdCemeDISj39YnjFJRsuUpZTR7vs6MxSKCUN61M4mDlFJa0We_l7CWXmQ9JzuuW2F-ZaMJ5MDjBqwAam8BtCzkC8k2R-A4e_9_2A0W1aFfngCIk1k0Fi2GV4zujPItGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت آخرین سلام...
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/667963" target="_blank">📅 18:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667962">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc227c095e.mp4?token=At3n8G7NLuIQDjhan6MVuBBBYOApL3QWKb1Y0Uvp8VBZT8Nge2dvr8bU5VgiQziMbJ0s6ivlwaoiyDbWS-VCy13SG_ei613dEmNuWEsHr_lD9AAyceMlkz8QHQXGDwY2tsrQrhIoflakIj2laeo_pbpy7FIsJuBEaeC7i95UJVNiaO__JPnPNymY_mLfijnS5Ily9g6fYVBw4mDHLTyz__ZWPgvgdiLc0og9mcw4JRCFKVbk0DGeUXrrtm6pwJ-_gk5M4Kputc5hXeh9MwIvdZ2z2qN1l5yowfviIsXuiMsus6C8M3LVRcDI9XlEbO-3BlOjKl720RyTv8w6e7z6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc227c095e.mp4?token=At3n8G7NLuIQDjhan6MVuBBBYOApL3QWKb1Y0Uvp8VBZT8Nge2dvr8bU5VgiQziMbJ0s6ivlwaoiyDbWS-VCy13SG_ei613dEmNuWEsHr_lD9AAyceMlkz8QHQXGDwY2tsrQrhIoflakIj2laeo_pbpy7FIsJuBEaeC7i95UJVNiaO__JPnPNymY_mLfijnS5Ily9g6fYVBw4mDHLTyz__ZWPgvgdiLc0og9mcw4JRCFKVbk0DGeUXrrtm6pwJ-_gk5M4Kputc5hXeh9MwIvdZ2z2qN1l5yowfviIsXuiMsus6C8M3LVRcDI9XlEbO-3BlOjKl720RyTv8w6e7z6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کهنسال عراقی: تحمل دیدن پیکر رهبر شهید انقلاب را ندارم؛ خواهم مُرد اگر پیکرشان را ببینم
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/667962" target="_blank">📅 18:55 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667961">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBGNQQ5JW_fAPDxBjgowLS32M91GkuGD-bv0fnyjFp47hkBtEHBdLOnrgVCYQGWMI_dlvD8vB4AN9OWMVU42M-IvfP9616Oc_ZO5sV0jom_VyIZOMiSLJPpdyGgDj3lX0FQwr-_sLxds-YwbjAP79bCgS6YpNCNz9bkgCCNw40D1IXli688mdjyKLAF9ZFT6CL2dhIKqr2kzrxNOlCxJaT8SqbpJ6E3JTc_wUCu8mFv-YAi81aa3d4hLH5W_dyCgSuHlmyEEf9krkd74vkCCnkNCpd2VKkf5urOJ_C6JRV1WIOW5f7sTIDvt8sB1F1NxawhZa4HKXvmGG36FfYYz_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این قسمت تنگه هرمز می تواند باعث جنگ مجدد ایران و آمریکا شود
🔹
اگر آمریکا و ترامپ همچنان بر سیاست "توافق از طریق قدرت" تاکید داشته باشند و نظامی گری در آبهای جنوب ایران را دنبال کنند، احتمال وقوع جنگ یا درگیری دریایی میان ایران و آمریکا زیاد است.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3228576</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/667961" target="_blank">📅 18:51 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667960">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f0c62e445.mp4?token=IxGzt40c9EyCP-_Gjqg5WTpkU_MBLubAYVlQk49V4d2N6lHwsvdM32fivNfnAStKPMIcyAuMwzzFGRGsBbVnFRAemmZpLN5nXGVyEr08ibVDg59ydGirGx2-m7jtsAC9sT0kCku25cD7vJI9iILg1GZsra88ijUSofd4lhFiYlkAZe6nq72Bt7-6nvgnZIOpbGQUdD25hNl69pdwZ_XFwyZMHx2Z5ScA7mLcK6Q4t3tFclOn05W5PGX4TguaJhRZ1ze77BHuwJ1O5l4FPWUM0NVZ2w2lrMjE_aBJVxpW3VAMPKzBbjvdNZdpEcrahF7N0YuwSBpPgNAGZGEoieoBmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f0c62e445.mp4?token=IxGzt40c9EyCP-_Gjqg5WTpkU_MBLubAYVlQk49V4d2N6lHwsvdM32fivNfnAStKPMIcyAuMwzzFGRGsBbVnFRAemmZpLN5nXGVyEr08ibVDg59ydGirGx2-m7jtsAC9sT0kCku25cD7vJI9iILg1GZsra88ijUSofd4lhFiYlkAZe6nq72Bt7-6nvgnZIOpbGQUdD25hNl69pdwZ_XFwyZMHx2Z5ScA7mLcK6Q4t3tFclOn05W5PGX4TguaJhRZ1ze77BHuwJ1O5l4FPWUM0NVZ2w2lrMjE_aBJVxpW3VAMPKzBbjvdNZdpEcrahF7N0YuwSBpPgNAGZGEoieoBmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خروج بخشی از ناوگان سوخت‌رسان تانکر آمریکا از اسرائیل
🔹
تصاویر ماهواره‌ای نشان می‌دهد از حدود ۷۰ فروند هواپیمای سوخت‌رسان مستقر در فرودگاه بن‌گوریون، ۳۲ فروند خارج شده و در حال حاضر حدود ۳۲ فروند دیگر در این فرودگاه باقی مانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/667960" target="_blank">📅 18:47 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667959">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
درب‌های حرم رضوی بسته نخواهد شد محل دقیق تدفین پس از تصمیم خانواده اعلام می‌شود   هوشمند، مسئول روابط عمومی ستاد بدرقه امام شهید در مشهد:
🔹
محل دقیق تدفین رهبر شهید، پس از تصمیم خانواده اعلام می‌شود؛ مکان انتخابی به‌گونه‌ای است که بانوان و آقایان به‌ترین…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/667959" target="_blank">📅 18:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667958">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
نقشه راه وداع؛ سفر یار از تهران تا مشهد
🔹
از تهران و جمکران تا کربلا و مشهدش
چفیه بر دوشِ امت، بارِ هجران می‌بَرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/667958" target="_blank">📅 18:39 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667957">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ادعای دبیرکل ناتو: کشورهای اروپایی کمک بزرگی به آمریکا در تهاجم به ایران داشتند
ادعای دبیرکل ناتو:
🔹
امریکا احتمالا بدون استفاده از اروپا به‌عنوان یک سکوی بزرگ برای انتقال قدرت نظامی، نمی‌توانست عملیات علیه ایران را انجام دهد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/667957" target="_blank">📅 18:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667956">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7d8d13909.mp4?token=fSQxRkFpe0yb5gSH-9KxT5piIZ8-lWpPy-JeUp2l0VRJqNfsp76wKtbDqGhj_DPcASjmIKj_XY9s_C6TVJ1SxnQVZWU2ApzVd9kwRKkeM9vunvWZ7xYUpyQUaAkQIXjwZJXdvie8KXR_AfVvLgMZCPCMW0nr67e33T1QkFDi-Dd5ntswucP200CM2jF3-kXaVUUp53twAggqvngRHXjhlXbhAWtuyQNN4BtQrTl2jn97DDm1ILo6v13h6Ggl1eRtuQGR8jt-JomZKboffjesZ8uP5kgS8Fb3G1-UYEux-YbH1RA8T5FmmdK_5Aj-t2e9AWdbAkMtNALwUkaU81A6Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7d8d13909.mp4?token=fSQxRkFpe0yb5gSH-9KxT5piIZ8-lWpPy-JeUp2l0VRJqNfsp76wKtbDqGhj_DPcASjmIKj_XY9s_C6TVJ1SxnQVZWU2ApzVd9kwRKkeM9vunvWZ7xYUpyQUaAkQIXjwZJXdvie8KXR_AfVvLgMZCPCMW0nr67e33T1QkFDi-Dd5ntswucP200CM2jF3-kXaVUUp53twAggqvngRHXjhlXbhAWtuyQNN4BtQrTl2jn97DDm1ILo6v13h6Ggl1eRtuQGR8jt-JomZKboffjesZ8uP5kgS8Fb3G1-UYEux-YbH1RA8T5FmmdK_5Aj-t2e9AWdbAkMtNALwUkaU81A6Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خودنمایی پرچم ایران و عراق در خیابان‌های عراق در استقبال از تشییع رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/667956" target="_blank">📅 18:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667955">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXDKhxmhbyMQ4LhHnz5IlAoZ-ZBSSkIHQIGPohscRDDIt5-3vz5q47yL-SLNsB9JJW-fbWY2VIMxqQ5WDQyobpfk-Ruc2hKViP36o5s3mwC7Ywe2yy90dVBL8ROJ_Ygt5W3efBx43GkwAK0Gux4jU6rBSXaXxYWHFhv9iPUfT1V8bdmHa44Tn3IeqjlT6bXQ_Z-0H8twTzTlGbcqlrb0FgC0qMhPO2_qQkympYL2zK6NQ9mSb8fzbOOJ5L3WBQkCDmxXp7HOj6wMT9ei_q0VcBvMLohDQdhZ6fagyPLnOvy3zL15azJglmhAOd34Y1U2ZNBpeKwfYq7RocYjHiD9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسیب به یک نفتکش در پی اصابت پرتابه ناشناس در تنگه هرمز  سازمان UKMTO:
🔹
یک نفتکش در پی اصابت پرتابه‌ای ناشناس دچار آسیب ساختاری شده است؛ این حادثه تلفات یا آلودگی زیست‌محیطی نداشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/akhbarefori/667955" target="_blank">📅 18:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667952">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مسیر تشییع رهبر شهید انقلاب در عراق
🔹
مراسم تشییع در نجف در مسیری حدود ۵ کیلومتر و در کربلا در مسیری نزدیک به ۷ کیلومتر برگزار خواهد شد. همچنین پیکر مطهر در مسیر زمینی نجف تا کربلا، در امتداد مسیر پیاده‌روی اربعین، در نقاط مختلف با استقبال عشایر عراقی روبه‌رو خواهد شد؛ استقبالی که نمادی از ارادت، وفاداری و همبستگی مردم عراق با این شخصیت برجسته جهان اسلام خواهد بود.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/667952" target="_blank">📅 18:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667951">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrIfwBZzBnma0F3_En0NBxzbup7Lf2eeZTC2ZVPQWvRnK3oLgUT4MfugK6XbbqMbQ9R2qumdDwCeJ2PQAwqu3Yp0d8lchkinJEgcwT9rKKil24yLg84UfFXGAQ7MnpQqzBNYtAfgdeCFAijIN0efXE6Vb53tvCG4IImEuv6BAnexT3Fgslq8ykaIFVI2ZsIIO9ASburZHLn7N2dJH8A_tiav_CNqJP0boDjCoJmhUy8fGkifEGqGE9t2WYnTPl1rTO47aoVFGS4xh-LOZJ3lqdTXzqPbV5D0CipccnpEQlUyaz2Js-DvYZanxiVSgw9mufRnMjLuEK0YmAoLoY72og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">◾️
فراخوان خبرفوری برای مراسم تشییع رهبر شهید؛ «بدرقه یار»
▪️
مخاطبین عزیز خبرفوری، برای شرکت در فراخوان
«بدرقه یار»
کافی است آخرین جمله، پیام یا حرفی را که دوست داشتید به رهبر شهید بگویید را در قالب یک فایل صوتی (ویس) برای ما ارسال کنید.
▪️
صدای شما، بخشی از بدرقه ماندگار مردم با رهبر شهید خواهد بود و می‌تواند روایتگر عشق، دلتنگی و وفاداری شما باشد.
▪️
فایل‌های صوتی خود را به آیدی زیر ارسال کنید
👇
#بدرقه_یار
@Badraghe_yar
@Badragheyar</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/667951" target="_blank">📅 17:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667950">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCSRJCo9XY7xGHFoOvr8rAByBYMv1G2s_QVwHlRpq6-LMYNzV2XMdUK1AP1mP2L6OqcDxvYtuQH_hXh-quAK-F5oq34KeVxBul5Jw8Drc8OeH-WPYjpELLrRmf1nzQvHH6wEiqBg5pBEKKQXgxAKg3NNvETI-yDO0F4Ii9TEdX6MVxqZ0ic_6aRTnogBmhgIgHPt6qU670IbhOXY6mMG7fCR2m-ktj8SP5NnwvFiy4RF8bOG6GX9ei3A7tSxeI4I8FCtO8YGfNMvjKeFCQDS2U-cTC4eekptxMF_3Rf4SgtQbt5Okch-v5RqJo_oBqO3fR2iitUOYyEtypHGrtzoQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تشییع میلیونی رهبر شهید نشان داد این ملت همچنان پای خون شهدا ایستاده است؛ همان مسیری که هر سال در اربعین از عاشورا تا ظهور تمرین می‌شود
🔹
حالا نوبت مسئولان جمهوری اسلامی است؛ خونخواهی رهبر شهید نباید در حد شعار بماند، بلکه باید متناسب با این مطالبه عظیم ملت پیگیری و محقق شود.
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/667950" target="_blank">📅 17:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667946">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qVRWI0fcASUouRXZd_0y-6DnSQ6deX-41xBj16xrYa6Zi07FSIS1Ls5vv4vvQFuRscgBm-kTETrcmcW6SbSvvo0cQbhKUFkOjRWZBMS8JoEFqd7aaSc0W7g5i8mKnBiKoay0RFtyHD2IcyY-TSX8VhpqtcGql7GJOUwJwjaKhbf13grr6FlnWrHeQGuo8o5cxtBcLanEvSFvHwPZitsAjP7Q_ph4kuWVcjdAgZ17C1FnrNvj-PECWWDYb2E0zic_fvQjBU0cHgnhaMaeh08odEXo84vRc5lFD0purd3wY7iNXYsHcYrvkxPue0NH-cqGNm5WMaJLwA69Na88q7nb8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
‏
رویترز تصاویر ماهواره‌ای از تشییع رهبر شهید را منتشر کرد
🔹
‏آن‌هایی که تا دیروز اصرار داشتند تصاویر تشییع را «کم‌جمعیت» جا بزنند، حالا با انتشار تصاویر ماهواره‌ای توسط رویترز کار سخت‌تری برای انکار واقعیت دارند!
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/667946" target="_blank">📅 17:41 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667943">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/823df792ac.mp4?token=WdIUwGPS2SsJcdjXD_5TWzcO8oeHIJu2RJpajg36SBpA4pYAFqHTnsw3-jSGO6SOOKfMftmrJ6C-axgGrIA2np3-LqXWS-F7DGwAXt6-fcHvfk-ZDoADE3neKLBfGPhZs4rCX_mMzskjWhU1IDlkB0kl3xfoYldNKEPMZJj9lsQfC_MQ8K4_4swGkYOqxQbTqy4QooVzCVInBa3CSo578mQ1M4WPgDfmMFe15jiBWgp-C_KzdnXFvGgwWtlBvt5eqML9UK_v8XO-ivvwJPAo23gnaURxkd_EzfCFY04yKfEP5j8iXVyWyZ5yfro5PGNzb6tZ8RUASFoa4SNzia6mHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/823df792ac.mp4?token=WdIUwGPS2SsJcdjXD_5TWzcO8oeHIJu2RJpajg36SBpA4pYAFqHTnsw3-jSGO6SOOKfMftmrJ6C-axgGrIA2np3-LqXWS-F7DGwAXt6-fcHvfk-ZDoADE3neKLBfGPhZs4rCX_mMzskjWhU1IDlkB0kl3xfoYldNKEPMZJj9lsQfC_MQ8K4_4swGkYOqxQbTqy4QooVzCVInBa3CSo578mQ1M4WPgDfmMFe15jiBWgp-C_KzdnXFvGgwWtlBvt5eqML9UK_v8XO-ivvwJPAo23gnaURxkd_EzfCFY04yKfEP5j8iXVyWyZ5yfro5PGNzb6tZ8RUASFoa4SNzia6mHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آماده‌سازی ورودی حرم امام حسین(ع) برای تشییع پیکر رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/667943" target="_blank">📅 17:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667942">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">♦️
ادارات کدام استان‌ها سه‌شنبه و چهارشنبه؛ ۱۶ و ۱۷ تیرماه تعطیل است
🔹
ایلام: چهارشنبه
🔹
مشهد: چهارشنبه (فقط مراکز آموزشی)
🔹
سیستان‌وبلوچستان: چهارشنبه
🔹
گلستان: چهارشنبه
🔹
لرستان: سه‌شنبه
🔹
یزد: سه‌شنبه
🔹
تهران: سه‌شنبه
🔹
قم: سه‌شنبه و چهارشنبه
🔹
سمنان: سه‌شنبه و چهارشنبه
🔹
مازندران: سه‌شنبه و چهارشنبه
🔹
هرمزگان: سه‌شنبه
🔹
کاشان و آران و بیدگل: سه‌شنبه
🔹
مرکزی: سه‌شنبه
🔹
خراسان شمالی: چهارشنبه
🔹
بوشهر: سه‌شنبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/667942" target="_blank">📅 17:22 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667936">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fM1le3U4qbxRQBoM0JRQjEJDTAX4vGcMKJw4l5-nPe_--1wAO2MwFjtptKA5L0dMyVdWMxaeHs3XNA9lp8ibLF0WHxTbp5GIne3NPPGglWKKQETmM2du36gYUfj8zO7XNueX7tMoBjFd-0rjhgLl-u0yxU3BcLPRKuxMk9VUWzaak-PRMse3d4nfubuFK7DKawHFySDvVa7pNpAu7FPEHJGJ6uvvV5SfgY4xoJzrFthwzw62CNIsPFo-RNpcDXkKeur0Lcd_1MPxjlcnkWjBI5HkLR6hcGzRIXnLiJUgKEtBztpAKjPpv2usJMomcZB2UZoPd2-bzSOJezhffpG-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین، شریک اول تجاری اکثر کشورهای جهان
🔹
چین اکنون بزرگترین شریک تجاری ۱۵۱ کشور یا تقریباً ۷۳٪ از جهان است.
🔹
این کشورها ۴.۶ تریلیون دلار تجارت دوجانبه با چین دارند، در حالی که این رقم برای ۵۷ کشوری که تجارت بیشتری با آمریکا دارند، ۳ تریلیون دلار است.
🔹
ایالات متحده همچنان در آمریکای شمالی و بخش‌هایی از اروپا قوی‌ترین است، در حالی که چین در آسیا، آفریقا و بخش عمده‌ای از آمریکای جنوبی تسلط دارد.
@amarfact</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/667936" target="_blank">📅 17:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667933">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LT2mM6EIsj8b1eYHXCOFlKzVMgdqdbUpnEYie9XkFOiq_8bXTkhP_QL9q_hrfNtOLuTTNZUhRWVEI2z99tURi2D4fR9nNq1XdbJgZGZdG5nrUzFyuugr7YP1G5JI0iUdlTA-r_hesnRy1DR5S1A7158CTYR4KMlyPj7eCj6Bu_7bQxpFQdxTSrGlHrHsMPjhE9U-WKrIyHyWTrWsqwdayq6vkz7X6FIx3NfKLNmJ7C7RYcTbHuAHU0x2xDP9NQ2ThYkwcFIJSDip7Y_oLo_lmZGeFIp7YzkYB1r-SNR1YHyYv8VZbW2yk8RReXQPAgveM0mMCIAlYdQ1WeLDCG0B_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فغانی؛ داور فینال جام جهانی ۲۰۲۶
ادعای سی‌بی‌اس:
🔹
علیرضا فغانی، قضاوت دیدار نهایی رقابت‌های جام جهانی ۲۰۲۶ را بر عهده خواهد داشت.
#جام_تایم۲۶
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/667933" target="_blank">📅 17:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667932">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jGgWEgmEWxEU_ZdzviBEPSXQxSW7raHXwtgveswKVOqspkqkxgcjBkoHfuH5XmJW8vBnhn1uLq2Ospv1BjncAbNguMqrd-QJB06oFT5pdtS_fFpHItUnuaAKzN4iOo1BiIgcveLpKezRyoPpE8Ly3vjWH-pZsyFExA1e-7ZdvtcDo1FNSeHnKWhSugHGlnGxG58wtPFrp5oY5i42Las0Jve6oQUcD20t4c1qTD59S2YcDAnDoR9ri8XtCJdrUkn3oI_uIkW8ZH_0oLwqDzX8oUYosYgJVEHy7v4IIv_EnRk65v5XwlLNAVVWctRoFqMtDfe89EGeDJHgUH33sGaldg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسیب به یک نفتکش در پی اصابت پرتابه ناشناس در تنگه هرمز
سازمان UKMTO:
🔹
یک نفتکش در پی اصابت پرتابه‌ای ناشناس دچار آسیب ساختاری شده است؛ این حادثه تلفات یا آلودگی زیست‌محیطی نداشته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/667932" target="_blank">📅 16:59 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLZ99yqcpSsQc7NdBFWJIc_TaPGTa1DIUPR00_TVCuxiTqsdxnCglNUekVW-mKK9RfP-Dc6AsrMWsC_AnvHfs7M9EAg2XjVyixsyGK4ZF8wawWKR1vgkYA6TCyZRfKLJyOjEtZko7h-B-6TpGCI41frreAXNpQTZ5a9MxorTdB98OqRQS-8eduzFfLAsTWLpGpV3mZgdODKnNoidNbkZC_XTaFo6imEp7TA1AaFUz6ReXf7thf0fsl4wEFzp4EPyGJEwvWym2wQbg9hFJSd_ar0_o8ttuLwrw1xNc7Qj3vRI6mtOvnsmYjaMN5yJKvqL3PBxbqfIq2FXNv0Kqw1U_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آسمان قم میزبان طواف پیکر پاک مرجع شهید شیعه، بر گرد مضجع شریف کریمه اهل بیت حضرت فاطمه معصومه سلام‌الله‌علیها
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/667931" target="_blank">📅 16:56 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667928">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f088ce62d2.mp4?token=KLMcl0thgb8zVLUSJHEZQgvxE2_j5ThmUtWZx6WbImMAw6y-F4bFgOy-v9wWSVza020Mzpov5DEOADfVLoCzIXFaonv2rXnq1aTbCLF6lqKY2laJkyJMt-AeOY3uEv_CEjYcJgbBlblNC0afFA1hzRZgapjD4nW-SKvSwyc3WKgP7qzAqv_lxzJp9_sfLnpsdKvcNcIho79t4A3IW050vXwiW_VEwu5GPZk-j0qipgC6mQ8OIzkwCDOj1CAyR-G4eOHExDfhxJxhbxGhRs9I9lbOOzYNymKuXDjo5OIKO2ij4etBw_mHNIYULL6XiWOHNG8KLReAW79wblzD6XxwMaNmEiyAJRgzL4f-Fxhg7YWOtuj_g8P8Ro220wOfBzonFbdu6mRZa2oDukO3Iz0LdmC_2FMwSpeKVAdinNmaGfNuY_xDgy4sJpVvnNcMIhEHG1_m6DVNyw--ynG7PV4KuwtrQ-hqxt-3Fe-kJT2pUzJKDD2uJ6R06f4FKnRbuceff-dhoaViMeqe6ahGX1hwk2CB_v12SYDaXdU4Xjl_FkWD2YSAwQItJtyOR3CwsoyLgcOiAfmc2_5IEMUrwxSJ_FLfXzAAljM1pGIDGydInmggibIFNHmxEAIP6FQGzFBtitbwytQZ7rZmr3nJRLgAt7lKthG3csr8PI-xFavesaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f088ce62d2.mp4?token=KLMcl0thgb8zVLUSJHEZQgvxE2_j5ThmUtWZx6WbImMAw6y-F4bFgOy-v9wWSVza020Mzpov5DEOADfVLoCzIXFaonv2rXnq1aTbCLF6lqKY2laJkyJMt-AeOY3uEv_CEjYcJgbBlblNC0afFA1hzRZgapjD4nW-SKvSwyc3WKgP7qzAqv_lxzJp9_sfLnpsdKvcNcIho79t4A3IW050vXwiW_VEwu5GPZk-j0qipgC6mQ8OIzkwCDOj1CAyR-G4eOHExDfhxJxhbxGhRs9I9lbOOzYNymKuXDjo5OIKO2ij4etBw_mHNIYULL6XiWOHNG8KLReAW79wblzD6XxwMaNmEiyAJRgzL4f-Fxhg7YWOtuj_g8P8Ro220wOfBzonFbdu6mRZa2oDukO3Iz0LdmC_2FMwSpeKVAdinNmaGfNuY_xDgy4sJpVvnNcMIhEHG1_m6DVNyw--ynG7PV4KuwtrQ-hqxt-3Fe-kJT2pUzJKDD2uJ6R06f4FKnRbuceff-dhoaViMeqe6ahGX1hwk2CB_v12SYDaXdU4Xjl_FkWD2YSAwQItJtyOR3CwsoyLgcOiAfmc2_5IEMUrwxSJ_FLfXzAAljM1pGIDGydInmggibIFNHmxEAIP6FQGzFBtitbwytQZ7rZmr3nJRLgAt7lKthG3csr8PI-xFavesaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ خطاب به افسران تشریفات ارتش ترکیه: مرحبا عسگر (آفرین سرباز)
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/akhbarefori/667928" target="_blank">📅 16:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667925">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95776d88da.mp4?token=dA7bvVYUKP3psEHh6BlzYn7d_bBHfDvuI5ZIUmYf3009b0NK1_DQrr-jE2oqknHBNdK0_QOaXUUT4j8faB8v1Byzw_0eI0I-wIKvqTUpO42-w4PfyMSEhRapxwmnxhtRvdYDggVaLR5uFKqeV8I7RnYTy2xbgLnUtEUIGXIrxrvtzHtpLK1yNPVBPgdGdhO_47OaigGW0F0ecwyQoyYLg0feaoipV7dLuSpSVw2sHmgGiH1G-6aWY0uZ_NyQJ6_gOeCTgI7jJGpan_uMnjIfe9KHBjb9kjArEBUx5asTBftgaawA9WE8jvVSh7OnvHdwpDYiyuMsPXxe-Fjesr1Jag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95776d88da.mp4?token=dA7bvVYUKP3psEHh6BlzYn7d_bBHfDvuI5ZIUmYf3009b0NK1_DQrr-jE2oqknHBNdK0_QOaXUUT4j8faB8v1Byzw_0eI0I-wIKvqTUpO42-w4PfyMSEhRapxwmnxhtRvdYDggVaLR5uFKqeV8I7RnYTy2xbgLnUtEUIGXIrxrvtzHtpLK1yNPVBPgdGdhO_47OaigGW0F0ecwyQoyYLg0feaoipV7dLuSpSVw2sHmgGiH1G-6aWY0uZ_NyQJ6_gOeCTgI7jJGpan_uMnjIfe9KHBjb9kjArEBUx5asTBftgaawA9WE8jvVSh7OnvHdwpDYiyuMsPXxe-Fjesr1Jag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه انفجار خودروی بمبگذاری شده در کنار هتل محل اقامت ماکرون
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/667925" target="_blank">📅 16:37 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667921">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/50945cb8e8.mp4?token=U-B1-enqwS5huWVdiep7BirIpHMXcqv2y8uKutJyZkcROvDIpSppp40vrEXGSFL02JCcVLmkx_Qqrv0toSknZqDGtgMlZbLc6Syd7nBpmLWauc6XxE35DQZVY19xw9WLUWQBmi4ICMsb9Qhu6txbXI6JmsBc257kFiYVyMD8yIh6ZUPJIq3GQvRInPNrX2DXLfUImO61OIMh1V0rTvvdbiJQwXLw4rnx6haNdp0PMw4xAOZo8o6ELOA0eHClyv4YFewmmhHW-BrHNZLiTkj4DZV4-gUn4i6E_od35DVXVzQLoVLTClYGXhB35f4ALKULugMYJAknXGd_yVFpkSox4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/50945cb8e8.mp4?token=U-B1-enqwS5huWVdiep7BirIpHMXcqv2y8uKutJyZkcROvDIpSppp40vrEXGSFL02JCcVLmkx_Qqrv0toSknZqDGtgMlZbLc6Syd7nBpmLWauc6XxE35DQZVY19xw9WLUWQBmi4ICMsb9Qhu6txbXI6JmsBc257kFiYVyMD8yIh6ZUPJIq3GQvRInPNrX2DXLfUImO61OIMh1V0rTvvdbiJQwXLw4rnx6haNdp0PMw4xAOZo8o6ELOA0eHClyv4YFewmmhHW-BrHNZLiTkj4DZV4-gUn4i6E_od35DVXVzQLoVLTClYGXhB35f4ALKULugMYJAknXGd_yVFpkSox4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت حمید گروگان، از کتابی که موجب شد اشک‌های رهبر شهید انقلاب جاری شود
🔹
در قاب《پشت جلد》از شبکه نسیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/667921" target="_blank">📅 16:28 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667920">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd7f2f09b.mp4?token=WPBi_qK-DeOGGETGfzTwdxADXJyxgw0g2ouZtZ59pKFQubB0bIzIAukygzvMxFiO1qrzSh0JlmfcQsXktIoDiTZZwUOi6he9cib11jguOWJeT-LdEp49BU76AsRaGrKVXTqqc3V-O5iwkafvZawhW7-DNpj8DriE-0cF1chtxSjxqcEru9epqKWP4BqIQiyXx4A2g01L-n2Ibp981jlZjnbwY1Aa4ZntrE5daoKCFHsLf6Pnc6Mls68jDtWuzqKH1IQ_tLkzql0uAonK2mUXeuen3TgxEwk78jgZeLL9hUVRMLQpIeAoYltJTXQZNYsNJkZ_hIk_FoXyBrCR5VXG_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd7f2f09b.mp4?token=WPBi_qK-DeOGGETGfzTwdxADXJyxgw0g2ouZtZ59pKFQubB0bIzIAukygzvMxFiO1qrzSh0JlmfcQsXktIoDiTZZwUOi6he9cib11jguOWJeT-LdEp49BU76AsRaGrKVXTqqc3V-O5iwkafvZawhW7-DNpj8DriE-0cF1chtxSjxqcEru9epqKWP4BqIQiyXx4A2g01L-n2Ibp981jlZjnbwY1Aa4ZntrE5daoKCFHsLf6Pnc6Mls68jDtWuzqKH1IQ_tLkzql0uAonK2mUXeuen3TgxEwk78jgZeLL9hUVRMLQpIeAoYltJTXQZNYsNJkZ_hIk_FoXyBrCR5VXG_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ در پاسخ به فروش F-35 به ترکیه: فروش F-35 به ترکیه را بررسی می‌کنیم؛ ترکیه از بسیاری از متحدان وفادارتر است
🔹
اردوغان: رئیس‌جمهور ترامپ همیشه به قول‌های خود عمل می‌کند. من معتقدم که در مورد برنامه اف-35، یک تصمیم مثبت اتخاذ خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/667920" target="_blank">📅 16:27 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667916">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b889e7ffa5.mp4?token=g4CY5eDmSPOKFJixuTiJ0xL6hEIjtqsvvVb0tXpowChBu_E2w07SXI2ob83Ye03JivUAU-tmM-fMNiql3rypGsjjeUdBfWrko0ggVD8kVpo3JlsQJL-QYQfXJnlLSqbG8YT2D_YlSC3hXrrYvGKsvjqlgrf5abLteqVuY6pHcNkVj0222m7jCoYyrk487OdoeBp4pEscAu7hBZbN5Hw_z0xjqUStOa8lui6nBZsedxEHszumOrmpXArbJed_A4YXPlUw9OAxe-HpfYxCZ1wSaOGG7uXxrcCC7_RelC1u02Js_uJBZ0GJqLc5-S7Khp7f0zQZbwk9_rkZUipjS-NCCEQ_QLKDNAzBtKXv5R_hy-xzw9ycnKW9ecy1Qg58Xk_1ESUo3_hp-N-tDFT0H3fu2C9j_NisdX4XGZjyrnH9IJs-7shhxKfKOdTFeccI8Qh2kFSyNHNyc70zikCdWuwHxl-_wZjXCGMBYhexYY8dGJihk6K-jkhIIWoMZynuRzj6kffg_dch-GjlZUvAxwXrTY-FgkjPZdiHUIcjCc0roGatw8UkcqfU8wfW3-OFO9_KBQvs3rjnnVvDLVTfgA62r8fMEvxgVdci3Qwk-qD0RP4P99mUL8felA5Ks08g-BxKLBhBCL3EsSHWE3RM1XXZKcM-yCGwQi01mtvpDtUA7C0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b889e7ffa5.mp4?token=g4CY5eDmSPOKFJixuTiJ0xL6hEIjtqsvvVb0tXpowChBu_E2w07SXI2ob83Ye03JivUAU-tmM-fMNiql3rypGsjjeUdBfWrko0ggVD8kVpo3JlsQJL-QYQfXJnlLSqbG8YT2D_YlSC3hXrrYvGKsvjqlgrf5abLteqVuY6pHcNkVj0222m7jCoYyrk487OdoeBp4pEscAu7hBZbN5Hw_z0xjqUStOa8lui6nBZsedxEHszumOrmpXArbJed_A4YXPlUw9OAxe-HpfYxCZ1wSaOGG7uXxrcCC7_RelC1u02Js_uJBZ0GJqLc5-S7Khp7f0zQZbwk9_rkZUipjS-NCCEQ_QLKDNAzBtKXv5R_hy-xzw9ycnKW9ecy1Qg58Xk_1ESUo3_hp-N-tDFT0H3fu2C9j_NisdX4XGZjyrnH9IJs-7shhxKfKOdTFeccI8Qh2kFSyNHNyc70zikCdWuwHxl-_wZjXCGMBYhexYY8dGJihk6K-jkhIIWoMZynuRzj6kffg_dch-GjlZUvAxwXrTY-FgkjPZdiHUIcjCc0roGatw8UkcqfU8wfW3-OFO9_KBQvs3rjnnVvDLVTfgA62r8fMEvxgVdci3Qwk-qD0RP4P99mUL8felA5Ks08g-BxKLBhBCL3EsSHWE3RM1XXZKcM-yCGwQi01mtvpDtUA7C0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایش قدرت هوایی ترکیه در آسمان آنکارا؛ جنگنده‌ها بر فراز ترامپ و اردوغان پرواز کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/667916" target="_blank">📅 16:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667913">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
درب‌های حرم رضوی بسته نخواهد شد
محل دقیق تدفین پس از تصمیم خانواده اعلام می‌شود
هوشمند، مسئول روابط عمومی ستاد بدرقه امام شهید در مشهد:
🔹
محل دقیق تدفین رهبر شهید، پس از تصمیم خانواده اعلام می‌شود؛ مکان انتخابی به‌گونه‌ای است که بانوان و آقایان به‌ترین شکل امکان زیارت همزمان داشته باشند.
🔹
هنوز درباره اقامه‌کننده نماز بر پیکر ایشان تصمیم نهایی گرفته نشده، ولی نماز در حرم رضوی برگزار می‌شود.
🔹
تدفین اعضای خانواده در کنار ایشان برنامه‌ریزی شده، اما تصمیم نهایی با خانواده است.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/667913" target="_blank">📅 16:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667908">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
| فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/667908" target="_blank">📅 15:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667907">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c8990e1e.mp4?token=i9q510oqGqd1rMoJFgkYF2bK_FWN8jnTjucWrl_G1euYEZyU7lUKY4eIt2juE8wgNMlA7YGBACuPXj96MKqGQaq-TlWVCuRSnMP_9YqmhpcCOQz_nkIv9eihsT1dMiJJ1KnPNgZRrYPMAmViWc6jI8GojFj1G6fYUIgYbgVIdIlPqFi10eXqYWuRA_IIzT4Rx6dOgKKHl7ofwZtv_TJ1oUlq49ZTMPYJDb-fYcfyoRABGxsEDVzrQ0I02s8Vzn5PvWd7DCfHhvm919qolNORHarBa9ITmhTu5bhKedMuNafEOjoDfnGN_YK5Jtp3YXQl2m5TwFCPeJfgBdIuKlwj8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c8990e1e.mp4?token=i9q510oqGqd1rMoJFgkYF2bK_FWN8jnTjucWrl_G1euYEZyU7lUKY4eIt2juE8wgNMlA7YGBACuPXj96MKqGQaq-TlWVCuRSnMP_9YqmhpcCOQz_nkIv9eihsT1dMiJJ1KnPNgZRrYPMAmViWc6jI8GojFj1G6fYUIgYbgVIdIlPqFi10eXqYWuRA_IIzT4Rx6dOgKKHl7ofwZtv_TJ1oUlq49ZTMPYJDb-fYcfyoRABGxsEDVzrQ0I02s8Vzn5PvWd7DCfHhvm919qolNORHarBa9ITmhTu5bhKedMuNafEOjoDfnGN_YK5Jtp3YXQl2m5TwFCPeJfgBdIuKlwj8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه باشکوه طلوع خورشید در پل خواجو‌ اصفهان
#اخبار_اصفهان
در فضای مجازی
👇
@akhbareisfahan</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/667907" target="_blank">📅 15:40 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667906">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJd8HLpNBaLpFqHdxvrHxXYfU_lD-VsaloaoWNAvENwbOHHsromDHZZqyIZrm8MbXqbWCnpxiBb37cpz2Ce75q0COmO7psS5y2QwmwY8SUc1E2bemDGXwk3KAgwtTvXR3838jUwuvUHyYgvw47vWlRnqCOsRDXAHaY4MX0eyrEtA8hWPD11gi8T0-MOGprog3aen4DlqXfAWE5T1Wy2HbJjwJ-lRlSrj9C5DD5IznuN_YGcqsYoYnK5mqPAovoJiXHSUXZSTAJnVt2r39dSLpfPqi-f9tbv8kwDqX4ELgfy1GH10YesOvmNadVc7Lb9qZsjzAjdd80erS5I0L5BylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/akhbarefori/667906" target="_blank">📅 15:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667902">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e252bea2de.mp4?token=PArfuHYWVvJcLIO9gZnoQ6VBHOCqm17Irgrw8aNYs0Hsai9U-Sx6Ga30mpZEKl2C56zr7gp1SXXgLoT0QnMO2euQ8YLul8RaHDjEDt2Pi3UqrMOSif--_EiCV51cwh7RndUACQTBTq5vwvX6OhtjhSfXsxgMNjyc7VTPt8zTl-zIiRCbU0c97Swwwvuif8XMw51gWgKPLFdiPvGYyzdKjSqJ0ftruGFYn0pi6ACQKRLApmT97I5lhJ5O6qlHUMKyrxOb5eLWk_RDmkK9us17oQWGmqYbJ5BCoxGo8Pm6uD1g1JXiwYL4qXHhiOI1G4WQZNxZBdpvgo9FZ3SZhJDNLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e252bea2de.mp4?token=PArfuHYWVvJcLIO9gZnoQ6VBHOCqm17Irgrw8aNYs0Hsai9U-Sx6Ga30mpZEKl2C56zr7gp1SXXgLoT0QnMO2euQ8YLul8RaHDjEDt2Pi3UqrMOSif--_EiCV51cwh7RndUACQTBTq5vwvX6OhtjhSfXsxgMNjyc7VTPt8zTl-zIiRCbU0c97Swwwvuif8XMw51gWgKPLFdiPvGYyzdKjSqJ0ftruGFYn0pi6ACQKRLApmT97I5lhJ5O6qlHUMKyrxOb5eLWk_RDmkK9us17oQWGmqYbJ5BCoxGo8Pm6uD1g1JXiwYL4qXHhiOI1G4WQZNxZBdpvgo9FZ3SZhJDNLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
روزگار سیاه آمریکای حذف شده باوجود رانت «کاخ سفید»/ شیاطین سرخ مقتدرانه به یک‌چهارم رسیدند
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/667902" target="_blank">📅 15:23 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667900">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-text">♦️
ادارات کدام استان‌ها سه‌شنبه و چهارشنبه؛ ۱۶ و ۱۷ تیرماه تعطیل است
🔹
مشهد: چهارشنبه (فقط مراکز آموزشی)
🔹
سیستان‌وبلوچستان: چهارشنبه
🔹
گلستان: چهارشنبه
🔹
لرستان: سه‌شنبه
🔹
یزد: سه‌شنبه
🔹
تهران: سه‌شنبه
🔹
قم: سه‌شنبه
🔹
سمنان: سه‌شنبه و چهارشنبه
🔹
مازندران: سه‌شنبه و چهارشنبه
🔹
هرمزگان: سه‌شنبه
🔹
کاشان و آران و بیدگل: سه‌شنبه
🔹
مرکزی: سه‌شنبه
🔹
خراسان شمالی: چهارشنبه
🔹
بوشهر: سه‌شنبه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/akhbarefori/667900" target="_blank">📅 15:19 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667898">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZwgUJAmvOvSauVLeJOi-HXC71I5-Dr5xIfQzzJVPDYqdqOUDbnFprSdKLPHVuUyqVAdQs4DFrFZDtqEsbyggN2j6QpokqAcyCHLWZ9Ze88J2JwYVUIkZAqTlM9gckfBp_Ba59WHPb41zLxa-UCTTCTw86uccfVkzhq8JKCTmqk-KoGiZbMO7x5DtaCm0azK_QNaipEhzx3cWppRBJwoXGMfpyVhsY8AbMgxQBuvxh7J8p02WqqqaPTz_rTO9cGoel6YLScJgXGU0WqFvKdUGFcfGaN5Yyg054_eCJ5DaqSkWaQS8cflv_ae1cGFXiLMBSIHn0d4riwswn-bWVMP0Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QWdxaPrR9qxWy7uLAVQolYGXP5wLJkJdjpPieuT8Egw0F8LcABkyYG4grhO0fuynb15FMG4MY7VVOttgO4ss8UBFifcoYUTI2BqGK2ayvTgR5ADvMKvfkYBNIu_OXl5ta3bEq3GWwxBXTdSG2mXpDzY5nm4R6D_WvoMPFNouX7zBV9s7Suxqg-BU2Di3dgoGBHmCVzb1BadAsSGRH41VwX48GREri0M19goKcXuAJ3Ga3b2ojNDYCDNbqT0InuyGzW2rECjhRt0xeAciVak7rzOx5UXe5_jF3uxk0KPot2mN4seoTV91TsdI5uK2s0O3t8eaSDB4CBq_7a7ToeJ9OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از ترامپ و اردوغان قبل از شرکت در اجلاس ناتو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/667898" target="_blank">📅 15:16 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667896">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a0b38e9ed.mp4?token=kfxldECpB-Svzm6hURM_XavWdRXh7_NRJ7ad6gjvEq0fLm1Yc8mU_YxLQJ8mrHwYfAMgDaDYwKstm-sxlJTCHwrG7DaYS9VmHi27nHJGi7ccvCOB3Wl8P2eY_I6ybPyYUSYKmLGPE2TgqcN7PT5XiH88NG0LpowqxXF2IMoIGbMij3AgwAlmJiwzAdFLU4KJ6OHNsk_GxT93s6tX6a3oeqD54ZIlh9WXFGfRSszKp93E1scCk8Mvf9Qi0GBwvfHQvG9n6vAUeAoapW36tHS2Oe_hd4Ww9ezz-OMtgxwGrLgfZxVBEt5x_vxZAFRSLBhtLg1CyKvgkDKgrIYfE3C3mz_qFjldHNgt1SRGbPWnTDX45xGZvO7RnEw4RWhuohQ10QxrGu0XeGoGAF__K13p0jEfKEoMsCPCV6NAD8bFR7aTb9GKh8e8jIApJ5DSyaKY1Kq3hqzgTwb_QkOCZvpI2QIXi8w9DYRbm20VKufAo6sbHh_ZWvLxT_kM_Cy3cz5omTep3Yx23g1jCgR9nW8ZXVGtdyF8BPfo169nDBtdJ6HUTUe1dAH4VU8VDaSVW3WE1Zb6SwSreKrgm3ocotrRo6Dvnm9I1FuhI5munUNXc1-59guoMirUrBe1oX_QrinsVOpWnNBPyqGrWi4F_7YOHsLgo_dPj7SfO_gd7ZupZm4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a0b38e9ed.mp4?token=kfxldECpB-Svzm6hURM_XavWdRXh7_NRJ7ad6gjvEq0fLm1Yc8mU_YxLQJ8mrHwYfAMgDaDYwKstm-sxlJTCHwrG7DaYS9VmHi27nHJGi7ccvCOB3Wl8P2eY_I6ybPyYUSYKmLGPE2TgqcN7PT5XiH88NG0LpowqxXF2IMoIGbMij3AgwAlmJiwzAdFLU4KJ6OHNsk_GxT93s6tX6a3oeqD54ZIlh9WXFGfRSszKp93E1scCk8Mvf9Qi0GBwvfHQvG9n6vAUeAoapW36tHS2Oe_hd4Ww9ezz-OMtgxwGrLgfZxVBEt5x_vxZAFRSLBhtLg1CyKvgkDKgrIYfE3C3mz_qFjldHNgt1SRGbPWnTDX45xGZvO7RnEw4RWhuohQ10QxrGu0XeGoGAF__K13p0jEfKEoMsCPCV6NAD8bFR7aTb9GKh8e8jIApJ5DSyaKY1Kq3hqzgTwb_QkOCZvpI2QIXi8w9DYRbm20VKufAo6sbHh_ZWvLxT_kM_Cy3cz5omTep3Yx23g1jCgR9nW8ZXVGtdyF8BPfo169nDBtdJ6HUTUe1dAH4VU8VDaSVW3WE1Zb6SwSreKrgm3ocotrRo6Dvnm9I1FuhI5munUNXc1-59guoMirUrBe1oX_QrinsVOpWnNBPyqGrWi4F_7YOHsLgo_dPj7SfO_gd7ZupZm4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهدی خلجی، روزنامه‌نگار و تحلیلگر سیاسی در بی‌بی‌سی: آقای خامنه‌ای قهرمان شبکه‌سازی هم در داخل و هم در خارج از کشور بود. ما قرار نیست اگر از واقعیت خوشمان نیامد چشمانمان را بر آن ببندیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667896" target="_blank">📅 15:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667894">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwmkdKww2ZbahGkHJQFEw0pSNmUwPH5RfKtP0PHbcq5fiQLrOpr-cXxT1oC8EkoIh2lA9DghPxF9rU0wl6dzinSsHFDL7MoPaHkoydBxTkDaEUw8mO5XEJ53jAmHuH91s1YvIrcTkr3egrmo8FYRgM1I2fwO-OjbWRF7yZFdYqENVEnV2m7UvrIiJNUVN0jWqDadv86cx8yWRf0lebpAJwS_lwy5sogCOCcNdM0OEEis5tIvVo_pDAhyHWJjzQMwabkefnh4-KC9AluI80ar6tmjxg2shgCZYtYlcyJgESQfpYFB8OVANbUcFCmrpWiqvqwJynVocSTQD2io1AYJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری پرچم سرخ مهران غفوریان برای خونخواهی آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/667894" target="_blank">📅 15:06 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667892">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ceba014aff.mp4?token=oDqhGSJhc0RxXVbUPRn7OX-8NKZx7OJ3eLDloFBSORDSjzFLPQ93gAxhyJFN7fQ442j3Pjr21C4Tvtltm9aWZ5lAw3xItlSp2BTAuT6De7CvClZEDNac9_5AnrHGVWDZmYCgBmP6U-PV0dz3Y9MwWW-8_EDIgqdXn-P799HLzCginh-aXYFCiGs3Tq3zXv9q4jxzW6Z2khbnfdsJ-UlVAL4nl3dC74djmMCVqMDqMtHmUWgLcfNw1CgZI7Fp9_3Oy4BknGrNp06CMK-NxoDlsyLjc811-j3e-zBlpwELbiVE4dTgL4-wrCmKZNsa3fXblY-PnHMWXk056DhhWnnlyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ceba014aff.mp4?token=oDqhGSJhc0RxXVbUPRn7OX-8NKZx7OJ3eLDloFBSORDSjzFLPQ93gAxhyJFN7fQ442j3Pjr21C4Tvtltm9aWZ5lAw3xItlSp2BTAuT6De7CvClZEDNac9_5AnrHGVWDZmYCgBmP6U-PV0dz3Y9MwWW-8_EDIgqdXn-P799HLzCginh-aXYFCiGs3Tq3zXv9q4jxzW6Z2khbnfdsJ-UlVAL4nl3dC74djmMCVqMDqMtHmUWgLcfNw1CgZI7Fp9_3Oy4BknGrNp06CMK-NxoDlsyLjc811-j3e-zBlpwELbiVE4dTgL4-wrCmKZNsa3fXblY-PnHMWXk056DhhWnnlyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رویترز: جمعیت کثیری در تشییع آیت‌الله خامنه‌ای در قم شرکت کردند
🔹
شبکه رویترز با انتشار تصاویری از حضور گسترده مردم ایران در خیابان‌های قم اعلام کرد «جمعیت کثیری در تشییع آیت‌الله خامنه‌ای، رهبر فقید ایران در شهر قم شرکت کردند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/667892" target="_blank">📅 15:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667891">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/879aed6238.mp4?token=LmpCHyfFPhK3r1ykypRiRQ5O7Vd0hoFh3Vvq3AjHbEpF3EGUdUNXz1td83X3lk0VdFGBNGKa98ak59E7aB26fis8zX--coWOwqZscr_utQNWgJfvMDeAhQhmpZeG6CM1d42G1EwbSn0avqGn0no9L4El7PiFQW3R2XlcyGCOspWL1X61a9B-7NYOcoAtGZyqwOANymV569TNvQpq9Nm3OWvKvYdv7FjxDRV9QgQWYYAn_3P5rq7xDJhNK47lxJgDDC0HEBX9jGXeI2XFaJ7Cgv72_R5RZF7benQ-jFzgArAccZjekWqeZ6M0Yquaaxty-LzR9pfTCfSRKHbLKt624g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/879aed6238.mp4?token=LmpCHyfFPhK3r1ykypRiRQ5O7Vd0hoFh3Vvq3AjHbEpF3EGUdUNXz1td83X3lk0VdFGBNGKa98ak59E7aB26fis8zX--coWOwqZscr_utQNWgJfvMDeAhQhmpZeG6CM1d42G1EwbSn0avqGn0no9L4El7PiFQW3R2XlcyGCOspWL1X61a9B-7NYOcoAtGZyqwOANymV569TNvQpq9Nm3OWvKvYdv7FjxDRV9QgQWYYAn_3P5rq7xDJhNK47lxJgDDC0HEBX9jGXeI2XFaJ7Cgv72_R5RZF7benQ-jFzgArAccZjekWqeZ6M0Yquaaxty-LzR9pfTCfSRKHbLKt624g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زلنسکی در اجلاس ناتو: ماهانه حدود ۳۰ هزار نیروی روسی را از بین می‌بریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/akhbarefori/667891" target="_blank">📅 15:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667890">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
فردا ساعت ۱۶ به وقت محلی پیکر مطهر رهبر شهید انقلاب از نجف به کربلا منتقل می‌شود
./ صداوسیما
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/667890" target="_blank">📅 14:46 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667888">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8a1fb142b.mp4?token=hYRetBUo6JJ0GkO_dm59RJ5zUjEJQHFRMO6mp_ermCHn20UR5lNYOneSVCp-7Co605ovQWWrIErh_iWrRmephTZDmvGbWql_LRE4KL2_4Qj9TBPZC_Z8CL27J_qlS0Al4NB9xYVlV7vDftu6AzE9cCA03aHbTf0gFAWSD9hb7iQmiyT2jVFXXW7hGbfQol0Li06Lh9ZYthLtds_nTWsOumwpVe8sjop-vhlQdTMnsu-UUUt0BwtqcBwVsp19jq8lu3M0HK1PD5Qr1HeuYbV2fxuTlwVNJM15S7GDZm9BqueiZhE7Q-EI0fCdnGZLUDZ5Z4pj7lBG49ASQSbI1woALKYizeJBMX8SLTxpwfdxOTEzBhMoHJShWOuZw1q5I5tjMiXzbFLzLVuoa999Fcojj0P1peIhQ7-YGiZK3yVLEYZWKNr7z37BUMOENKW91366qa5-2UAoXqzs4qAhEDA3buF0RYzYYjHWHoCRCfFU1EgotPGAiC5Fm_MWbw29F9nm-oL3RyyM0hNWegvuTP7aPopAOJQFbrDuGLyavskSYrvOW9QESIJprHGX_2SGmpdy5t2HJci_VKUZ_mHrXh3tbSobwR76_WSVZCnCLizYZDZYQi6A6R49lSNc4KjtdcKtSZ2FkTykGXobE2Wvt7U7JMKNJHJVKaZqBvOSrHVhwUY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های رونالدو پس از حذف در جام جهانی   #جام_تایم۲۶
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/akhbarefori/667888" target="_blank">📅 14:34 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNDsn4NIhLZBr8GmEEKcXxnHqLQTyGfKlOQHMzs8KwQLgkP2b6jIKr7cOAA8tLO7VH6sCmcA10bCg5FdaokvzUOaqsR5Q8KPjhPTb_oamMH62GmsxNadfBKwDUAa3dQw7idE9v081uHQbgf_nC-MOc_VRdGiupRND_TE7mt_Q3GqeyLiS0PmR46Ed-6_1MZeWG7Nbzc535-hH25eI9gyqlY-hHWTmZGWvCD2QSv-YpUafk621Qn7jfA_Tt0cGpPaklkAfckAIsDOurPQEYkCMxPz9slcPEYrc4NJnHAvRiSn1bD0_sJhgbSx9T8QgSwFsenBDVIodGPsed3BBnIglA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/htkXCYWXljam3yc8iXH_zOx4FH-xYW1_q36-cYUcUSvn7arPXBqnj--r8jW-T5_89p9c5-S3HfIv9RUk9g0h8HWdijx6-y1qsUB9-QDCnP49PsxLbxoMvXRr8iDYlr6r0qVooRXlCZ1p3Nm1Y2oJYymLzLgknwF2xACteniTYpkNvH76SJdMy2zp3JZpfrpoaucwU1RZ6ckHFqAybfVlQd-_jEMJfbdgLSh8qMUlCZ29eq5zuxXO4dSgLmdU1UEUbYac7Hde8qECHU3-SnQCZPRnYaHDB8v9UXkY9rVnk_MwFTeYnxGXoPh5IGs3fZdBU6Z94Rr_eMzSv08P88InjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KYsOwX6yc7-9QWOKqKo8xTJf-_hmUNXBJ6GlfFMFZz0I3ZkjBGSVZNQ-UHWRixFGmui1ziOmyYfpZ7pu05mMM6O1AUCstPkOe3B4HNTmuzsaRYsIZosVmnkIuUCJH1oInslN2MRTdoWEm8scAfsxZfv0FNnt7gC5KK9td3BY1GvGMZntX2yMHFhJn0Gxk1f50bBCU83rSdGr_UWY7FEPdsU-DOFqukLt1O_Fqh6RrzugRRkQldWftqtWdSKA29UQT_0KQve8QcqmISMIf3l3iALw1ss3cz166df14yMB-jcHApORaUI0vRG38R90zcPVPfgzruIYcUVtTnBk2oQ7DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j37H85Fo-ZydDNeAl_Kgqn0Ci1eaCiRGGmdMKSzfyJnwqWXd-XPweoH5xyq9-y6_466uq58RSBSg2znp-oPildqrInV6Jc2NYTKuWm3nQ_icSTB00yk1dx9QU8DWZ4OiegIO8yEHPwJwvjZDUb1duv62yOWGC5KNn1t4oucP4NluZuOh0rynqCQumXvY3-n5PQCBN5VgPrr7QBX_ufz-5yQJ0l0YbxDp4maTViXimtpwQHcloDBjej-h9xcsLCuFChj62dQ3YiXEFuq3r5vwlDY2AjQEvph9zQutsCJ7wp_nPe6HP6HXtOR7ivpeYUn_HqnosK8ZgTgn82TS97M8zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sP_9gj3a5jYjXFxfWKvYTlu6uy33cYON95YlRZKO34iEKFVKSLplgWu4C63KWIqPIHadOvhVz_h5QM2vk7P8TcUWF--WSKlojILx4EpSpsg4IPtFS0GansqNljn9MX74LrzsYP-FvJ-_ERzjrh-3-Xq865oM4f0UFd4AtQEUodrdQOZHbyxWfZdCVwep1ZWn48wrMlVHBOuHoyZklLRlRQcZSmb1ZZ4UNvuNMnsuxENo5lW4ImvxB5nqKbNJeCJNnwSn3McvgwCUHu3EvZG7oSqAvdxJX4q_3e7sPC5btuYM3gE59VeUbi0jqMWqZ6EfplEOQcSKaDmRt4ZZSkEAuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تلسکوپ جیمز وب در چهار سالگی خود تصاویری حیرت‌انگیز از کهکشان قنطورس ای ثبت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/667878" target="_blank">📅 14:13 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667876">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e09e0c86e.mp4?token=YJ8b0lK0ZNHFZplDcWIghfEbHjbdFVnEkLmDHVDB6MdIVTAi3KF8rUFgsHtd7ELXlyKr4fwxqtqmMEiH-LSta4CE0de-8N7yaVEc0jgK7281ZR_MpBE5CjzXGovxjxEnYIAEGfGdpmnA8cJXq5i9Q8scS9RhTnwNYEB3fLhmcSqGrXd3YVVa2t7hFSjI-DLZWsvDK3dW2wVzoYOLDNKq07yCTeURsAGnRdpu_OTNu8ZvzzWXUEQz5qFUqy5xCYRn4oBGCSIGTkABJE583E1Fi5ccCKPSDMh4PI1KBeTiEkGyp588lE5JoxAM7cllCejZTGDgQGY2rymowlUhfvk3fWyR4IRyLiJQT80CTFtILD9a89rfY140G75LWNeA4d7VpW4PhN9uLeBII6vhsRV3DlNhw6dIgaWW2lyEuk7udQNvaU_j5ohCC4sSzQcQMlrdeSUznE-ZrMlIsABS3aEJUOd-KveK3vxkIynNUdObm1rvtlo8waIbJXumfzVUhzD3lohSOD3vUN1456orgfJmT2hP3XRcosyQ61jwIsIK-qYA3ZYvaMsJi6xLt6CcNe8Lg0GimdDMdBkJLqCHLVSXvpRmJZhAPYCIGtgUQ2SjTK8jHI3DkNP59JCB6FV0bZXJDz7HI7kn2jIrdmpluN1EIkiqO9mSlpZtm-hDWo1ids4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرنگار خبرفوری در بین‌الحرمین: حال‌وهوای شهر کربلا، آماده مراسم تشییع پیکر رهبر شهید است
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/667876" target="_blank">📅 14:07 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667874">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌ونهم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ خانم نسرین جاپلقی که در سانحه بسیار سخت تصادف جاده‌ای، روح‌شان از جسم جدا شده و به خاطر رؤیت روح مادرشان و فضای بسیار زیبا و دلنشین برزخ با وجود درک سختی دنیای فرزندانشان بعد از مرگ ایشان، باز هم تمایلی به بازگشت نداشتند اما با نذر و نیاز بازماندگان به دنیا بازمی‌گردند اما همسر و برادرزاده ایشان در آن سانحه از دنیا می‌روند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: نسرین چاپلقی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/667874" target="_blank">📅 14:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667863">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U7UsLf3zWN76bkdsbihUbBcAZAON19JWSdU-KIUTM1kWvr7_uJY5PfUuYukbsH9VLalmmWXLsxdRrDBTD0lP82IRy--cqlO0RmhFvITPqTlMSKD3JbfNN8RBeks-9_Ex-MxZ257jugb1dC7NtYgkzus6iJtQLALRCPo5t84qsEdHGkQw9lo4Rr7MCa4QYZoqOJX8-UKuwH5rtfWDqq_X6uZV7B3Ez4Az2MLNTAYe0ZvSSH5-7RkYB0F36wDMEo3ckqZXPIguJPuMljqsko4ehV-ZI3TLsaM2x2JpgjaJfNHcw1tOp9SabrBB2_fS2oTsiOmfGjIQMz0a3Wu2H2UWgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sk-_lhli8FhaceI3tAp_N0l-4_WxHpH5LXpt-ng5JTNwwILlN18UXeH0UNz9Me60_X_Rynyz5Q9Z8-5BlLip1QwRqDV3P1Bux5cZKoOIgx5toVjwIs9EkKGsxUVoYEWZdz1WtZHbKBt_007-j2roDO3tdq9Qf8LOvAMYXkwNGEBemaxrz8OObUpezHukcs1YuIJGRTeRMvO8U3viPajmnA-Y4k6v7cYZaqTgBsvdLdMbEOb2ofKhPdQDtGyxvRTUhTEpbUcFoTD3Q1KBQxX_7DmGlY2aHaAmpOtWpM05ybymAlxInwuEkAZnCBT0KXZ6fV4073NHcgdQYWHjGMtZMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l68hoHEqcHRRyqa5WlH6289lbD3F8rvObLYnJCyh6HhwLFzqMZGmGv9juTRylxRSaqYsDwlk7lUQHIrPAU9Pi8TIXioUs80kEo_7-jttbphnKF4vRDJRr0Usw2we9f5ahzCJDlAqLwsGFHmiLoPfNusjNKJIkviKxPC8faya7EvVy0UrOZqW0fl8i_RwNd4a27eGT6jyuXGv7jChyh_XEHmuiRH6jg2vpz5vZyHzAsfhnsFCwbdoNsN11imXXg374V-Om5-tGXvqDkZ0spZSbThrsOJ19RLgY_dX4muGalEQLZf6SrPxrgxAMH5tdmwK2m9XqfiJ0iEUja9s_VNlJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERNDbZGpjoBssCQnUXdatEeVThELh_f9K6btmxVsGwa-ClB5EHXFuc6fRpk6PHeliRRJTx34MWdUMP2QT_4Zrz1f5823Guvu2M7lZkLp7F_1u-iOngfXN_8hUor14ZovetB-Jcq-uzyWuUU7EsyGKZUQcoBLSO3lW34FF14eg0kaxyD3RnMQ-R74RWasSP8YlXeeLutv495AGPXxSlV80i1IrswOlw001Y_3ebkPdq1mPD5PVVKEIXXQitRgA76fJzwUeFf5nPqTB0pMkkKtYRqi_A7ijJ6lLcUeWo6lXSHREV2EPjy7HrgOIPzivr01JsvuhCWoaKbwBszvsDEBPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q6kg2sts6EVINr1slCwqcOGGqsKpHQzLf2exvFLIUXANkdBNyroiepN6KDm5dOmHPC2OtbIyUMtdDW_YdFRSTr8xVIw4osdO_7ziodwbot1fu9ys77UxYIpjAFM8SrfCRXJlYY0pAswhg_Auf20HiAFxMYQbyvaCXyVg7Z1yPJuhtowLW_hGl15Yfo6z5glHJBaTvkIKpNwWd4X14AqVtAdfZ2Bt57IYtJCATMdp_vWruWd-5emKxkZ1CyDdskGleRIQa5h4Z3_IgT42jsQPvkw2OHdZoPG-gThv9qBEXTKNAcuVTaYNW0hPUvxCrXdLSUUqGvWN6TYzME7N2I59Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t4107eRJIfDPIALZs7ubGPnw4fBDFNvGuYBV4ddIVqXysz1Zu4mc7_cAasw_qDkrMbPNemfJi8MAxIvFb17PI1sqb1i56B8xk-4Nd5L3vLup-NTLYcrsxVrjUUNmijpkSMl2b2NLAYtZ9vkFZHonVfDl_IslmSQEeWviJmQX92Gvw-rHpnBBG3ZGZcAEySM6BldT61PmVs6Q-9wULaCWY2N2L0cZfQhv5apLgoylgcKE2bfcwnpNnK9H0m4ydI4gz1F6JeL2zNlHVcAUUTkvhb-27Pa0ntLjtTRckrsm4Lmtss0TYa9Pul75H55TIWyEXXAeaEkAtCURTqUnDsDl6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QY9JvQg4D1BiJXtjz3Xnm-sKU78UTDoXX0TVE5y2ejLGPS1PolrU2tkIgmE841iVxcW-lIi2oT7RXE4y9et9_sBEv0CcdU3ZQHlJ9dcpTeAm0GU-Sv1RFYcMymgXWwmCM56W0xdv0MWFFwtrSr451bRpa_gSKRkhls3VxjulJWSIaee9-HpKmLWAMyIpTtoaItuqmmF2PCBQv6jjgJPm_QApLrRyph-k-J_okot2M1W_C1Pymup5Ycvb7ez3NP4B7_UkjU0EooiI2gNpsbrTtRvMQejeffsWH2vaJHyGpWgBK2MWXb-n2o4i3TfAvcGIVbRhmCRak_NBWU2bJzaR0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqVP9dGUhYQMIrDLaNqMy-FnojZLXb3BS6w5kw5LjhVqxM4n5HBkV-_cqp6GsvSYVvMH0UWNt4kkVOfiPHJWbYyO1IZ63G7zwxDkNimgT2_Xp2_HjG5jSKaNaEyyqP6LQHwc1fIUZ_EkSFrY8kQbN2R_yq8bfDi-vQwSt405-h-5meSrDwWsblhdHZmziGk95hfPrf6nLdb5CqkJcwcL15iONB4G9AlDhHbV8EK1HGvT9zyd8i169j2VsjYVmkYNBs441fBFwmc7FSaxwFIUr7cGSiX7Mnr--H4NDwR_I75gLJVUf66HHXTwTp1SyKILufXrfSd8EuPY47kPREpShQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2iMQ2ngHmq2Xg3d5kdmh69tqMe8Zx7w2lfx8ffap9pN6m2yHl2if8GxlPDygaHjYjMprnlGJVmLcHHHwOerpO4eXPiiOjJxBPuf3rHHCsRTmiJqtzdxsHUTmsyntMJhIWjrIlBv3e-PFAAKqs18HIOV2RLV3Tfs0cAt0DWkwNe8H0WLXzH282Hpy9X9aWOPACIHJUx0kVELQwz4rrqlSRjR64_dVN2H_cKbRk35iSjD4_3ZETqabJcXwRl9lLYODEAojiLJY8vU0RtSsomR42SqeBT6wz7HajxvyGqPHYhKGaq6ey9O7z5w5xAvaGXouecu4xeoNyp8DnkrqCPWmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rRqnWeHQEAjG1uHeg7Gn_oODSgkyWETqBflGFAgDXZmvFAdp3wCZvun6EpaJpZNS-mqpT9hzZ_GjFrvzSxUfHEoEMyEdoPwShRSOUFYrTJKRTf-4TwYg1-64jKp0aYxa_dBHzjb0n6uk_gt919qJLEibfBRwGQqvK90L7-vFRr8l8f07oWGtWy-Xtum_QAbY2UyGauiMdgtk1JhyqlCQNlA_NYDEe5_7qf28pmHHlwEv39aSm2T9vgpiRwVMSTVBQrwrZsnUhTFxEqe1voVaTi7jtf2PNhXwM7CUbmRHXuPuVxqALBg7qjDqfY-sJdBSFzLkwBZAFk37SEJ0eaGk1Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">◾️
روایت تصویری مخاطبان خبرفوری از لحظات وداع با رهبر شهید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/667863" target="_blank">📅 13:54 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667862">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/760f4aeabb.mp4?token=qWrgMo0mbnSAJyTAK1bwYVDq8j42fbCCdQU7mdGVxRxzTYnp_YXpRe7yKjhYsbwysZr70ze_Hp1VlQ7uQRrDjEfkPjdGc6Qp3VJ13zkHnNpHtnh5UOg3S0dmm1tsNccP-GVwNsoHYYjCQbx-X-Q4U9KP-Rbn3gQBiSYejY31IxzvB4j2qAPBVhh7p0QIelVfbbZ5TcUhTuhURtva1MnM_wD1cuP-MPwoxfMX61DIBiHrjuRvWP8YH6Hbvj5ePxM7bipPM1csf13_sBepykVhpcd4qrmAoHNc9XrBuMMf6ZX6UCqzThpQQ5_HkdpQwp8ZRI2sKWxF6S-c-nGOIWvC1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زائر تشییع رهبر شهید: امیدواریم مسئولین کاری بکنند که حداقل در دنیا باب نشود که رهبر یک کشوری را از آن بگیری و هیچ هزینه‌ای بابتش پرداخت نکنی
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/667862" target="_blank">📅 13:48 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-667861">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b63dc0c5e.mp4?token=GlXj_NrpjCBWa4Q0wAuUNyTEohmUsHd3w--QMQ2WVSXIYSL6knEU4CiudpeomceQTmXPXkTk-nhGH6iW3MzsDraVL2LJDHiYGwyhjNJJ9DkSiaiUtNCR1hyaC7MaQSIidwuomNEWlqfolnqb6Rcbxs4KFlqEPj6ikyx1bx5RqwUDqvluMwpHRrE5GUOl-x_Wwwd4V0fRwTbwSFxxFBADAlRpvyW7fovI1H4CX6Pakto-_QlLjlPsTkaAIgT8_6D-leOLcEr7TawCQPTDdytRd-5_fYUboEU3Y1DEaVZisidDiFZ9lSuNczOC0VxzWp3_7f4c6g5gS7VxaGKX8LLYsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مرگ بر آمریکای جکسون هینکل فعال رسانه‌ای آمریکایی در تجمعات شبانه تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/667861" target="_blank">📅 13:42 · 16 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
