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
<img src="https://cdn4.telesco.pe/file/GeJG2unAENGvcz9OFwsX0HPiYyaeOUDDtriiKi_zw1Tq0WOEtcKTXmoHmIf_QbF3YNkhTk3YTUnIGtmc-P43N__Vnbr7TGMEYh1xK_sBj-e_x4EWo5mS_9e639Nw0SeFewdKgS9KxplIlGEs5TltdtNmryNB5A-DWbRikEq69ydkl2wiV6FDomKnlllKPUK5dobBiPyhreM2oqqKVNQ1hP6oXnPq5zMP-OUV-yQpOpmJ0bLH5_PmpRA-XjajV3R2bj_-UXBnulEJgA79j17HjMTMBvEiSP8_eL0PhroF_2JzAYDB5jN6iSli4xWMpFpL0gUarWPhMC_L_3C1Koc6iw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.06M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-29 17:37:05</div>
<hr>

<div class="tg-post" id="msg-682826">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKFIy3I-ZtPCtN3ajypmWchIh7BDK-ih7jEzmS5Qq41b4-2-kIvxT3b5t1CEbQ3UxqUMJBkS-tNwD800QIJCb9tMqUJt-jXSpmdpvR7FBvUqGKP5yrk080UyceQOYpD-jagd5vWRJLB8BOjIO7EGGyUHZD0JUO7cwzYtbPnuCA5dLkqVFUwbEbyzIeMTexrzTGGTjxBfFvzWnqmvdaGPvRlUMJJ0cmw0HoSYzE9YVBeMFvw8oFE6-zTRczkWnZnfvRwPuzteNm7o3H9rlcRTiWyqAYUwSYggvDwQvI9bg-Y85e6eUuFeDenJXBKPmp1eGXz5CU22zsJ1mSIjbf1EtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tzaoVRQbdDIDL6dyNCUcoXvTMmw5619pJj9ofB8cy6UL_Tg7rLVAwbrWGOCFvKXaP5Qk31m_--5tnHuqxGbzxJwB8Ug6nuPiccococK6z39JCoaro9HHpXmVIQ9XWz1xHFZBAeTSvziLfyLfkkta5_9P_70DeggzrUI2aelHNnvneQzNzhKZs-TYdajGnXBRRK_Wsl5WpH5igCP-XoUZrSNIm1mEXPf3OvlSrEhHtTmWYuUyZL6fDLVWzjhX0luwSlJnome2DSPNIy9ETXut7zLZJe8i-whhtEkyMglwjdp0GD3Qodd1WmUYkcrnMa1YgZ3ljh7d9eQHwSZzWaGNag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AsSh8-A7AK0UjLuwtJ8pOZ7-CFp1f5gWmg68IM7uV4dDSE4BMGUKTew4xiL2x9pmeNEfmhEGxLkX4WCkIck9vq0mA09purxMqEP9jd8ZASCfba0Y9RAXqY0ksiszZFFUdDbmbSCC_fsK8hR_8IWLNCi2kyc4viORZcU15EvO-oRKnHd0TObI0tfxStDuOoeNyfDFHBoeYO2Ad_PLWEmHfNm_zxGmnliQWP9TDMY5JgxkgxeMgWpyNkV_TmCQxYUZoXcW0LJaRHTO04WYaDuoEVRNZlHutOR4RRyhbvAJbGIPyK5YCIvtc_CR58pqXj47cWaqmSk8n77W2BEnRZHQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJVY9QTxVI2JCukyXzYTn1N9axjHyIp7snrheWB_8ZNkAT4m62y9Uq7m0sKzSX59pxHCtTVcDPM9JS80BzShE5UkKpa5BwYbrVz4-xPAAa-ygqxeULd8I9JH1tsswveV5X9maZMou0-qD9qPnTtAyENTQSM7Hrw4prMfyQ7uQapAWRi5-VN4rLlwRX4Wr0tSa4zZ_ZT-e-eQRmu9jk9G3vQAJGk020spZE9eF_xvtdGF4HxlBPPdFEPbRBR87Oi-KXiV0GEkrs61KP2Z-zMUuBeM5EXU_C_Dkx6bth22gbTeo4fspmoAvQo7krdRPn5bhiywoOG5czMFJA2Octdrww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MTFeJq7WklhgY3usRhGtBaecxylo3YASSpRn35yxG-1okn6n-Q6gD5TZb5s24AiUIysGC6d25fLNd3yhdyuJhJz9Q5u1AK37l-7AImVi1yg6MRk6VMORls10LF8F9uZw2JSrOXDNrHG-4vVYJJDhID2fXZyB2GYC_oHjbh71S7oJhR0sIbzuV_1oWsVSNji2xofm4bZmm3WpHwaN5BaNBYVx9Zj3P9eO9SPcaL98Ep6iimNU06mc24Oa2MAey7nZr2XBoBdfImMw5i1hnRAycmDSh61s5OrECNrgnStyMHY8IoMRyzXau7F2HidunghTn7HsSSxGLD7zMZWDHk5o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/czTNFgQROZjV3Ad5XBVsphnmQ9TWKftNGNcWRqVxs3hTcX6KBB81VqbgD_5rUW-atWp3psn1RLNvE-GD2ylZajjopMfGS71ovbvBF-qAU6sdO3Zq34tkYG7nHp_8ts6DGP0hFZE1eZWrwoQSj3Pkb9sLg3G89dnMIa0FNFVFTqH2detZscE-wIJV40qT8GK338UioRgWDTZkmEEQfiSZE1ixRPDhogdP4JQwbTe7P0bDVSpWnNWLw75zIIHZZMBJ2s1kK2RjXO2VeyViaWJbTCmXJWHP-crUhGpRllUwisxjg8pUJl_88zrvcBJ-1Wl0Ks_8_yMVdMTQIy6nMdT8NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YWK-5o_P90eL9LAdATBwM6RVbGak5es5QThZ8hcq74IFyAd2PiPJa5jBQSVPOJzm3kHoVM90HGyy-aQyxTFJUqIQeMghXqmxu9dCz1E7OX5cr3jFxK62C8kNwkaEcPmVwPhk5_ATqnwnATbfeHJiXOxaIBw9Udx9URmZg8t_pU2i7EzeF2J_0dCQcO9eawNYlSYx6KxA78Jb84QqDLjWe4t2_ghePVgeDmjNdggJfEKhbu4s6eWVFbly7tIFF3unvcXfFqm06_nuyGtMOkUUAHbu9e98GdW36ZRxbcj-a71DhdV_q0ToS2SiK_Lc7P_Q9CTghJ-71B9_JV9oCQjGoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSg9I_GGKdjlek0D0hGlZIlfHqsGR7bVX4tEBupa4oBtbUxrf-0rdhOOzJvbENHkzFhH4OZGOPmd9MLR7JqDLjpHhqDbsq4FrkjHupQLZBhjosdr10hT0Ig4hL9BbddT1lexzK0xJ3ngjR4zjJIUYJybZygG6RdbhM7oGSCaPmr7XiGx53GezUV3190sg9KpjDhGvKoJA4y25ruA44mqcPWSUoWxK_0dRWuAsGjdbIt4eTpn2jBWy7JMRpqGxEIdTyP-7j_W04ta5RgHaud5lhORVDcBmLpOZexlAv4RMhvT5ERLaQeTXCSGJsE25GBo433f9gwTLBi-HabndOe1Xg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نوشیدنی‌هایی که باعث خواب راحت می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/akhbarefori/682826" target="_blank">📅 17:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682825">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDm5F-Sttg2nyXKr17piuhtC8l8C1MwlDpNVlCHuJbnuzjSp7Ct2757l1rKSeEa0wqpTwJddY5OfWwZ6hVSKJiyFc2WprwF8b3k4bjw4vST_JH5oVNjleegflnICC-pbdDlw1GKu4R9SE3Qujdb_5qe0E38fLL3EoGsUTCzEgFyVY2kPaK9vcHHZOtL83yTeeQU_XC79G5tVfQ6xfOz-DavI6l20HbcB8FNqaOJ-QG1NNuvpoZ-X7017bYenkVj8M0Lp7OON27AHvqIHiiEY8OCncbVEYwkKVbGFTcBKBQEVaf-AzwlrRG9IsYQv4PolJnkB0F8ZyjfbVSWhD6G7KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بیانیه بانک کشاورزی در پی احقاق ۷/۵ همت بیت‌المال
⚖️
قدردانی از دستگاه قضایی برای اقتدار در صیانت از اموال عمومی
🔻
بانک کشاورزی با صدور بیانیه‌ای، ضمن قدردانی از رأی قاطع و منصفانه دادگاه تجدیدنظر استان تهران در پرونده مطالبه ضرر و زیان ناشی از جرم، از تلاش‌های قضات شریف، پاکدست، شجاع و مستقل دستگاه قضایی در صیانت از حقوق بیت‌المال و اجرای عدالت در پرونده یکی از متهمان کلان اقتصادی و ابر بدهکاران شرکت کارگزاری بانک قدردانی کرد.
🔻
در پی صدور رأی قطعی مبنی بر محکومیت این متهم به پرداخت ۷۵ هزار میلیارد ریال، بانک کشاورزی در بیانیه ای، صدور این حکم را جلوه ای از حاکمیت مطلق قانون، اقتدار و استقلال دستگاه قضایی، دقت در رسیدگی و عزم نظام قضایی برای صیانت از حقوق عمومی و منابع متعلق به مردم دانست.
🔗
مشروح خبر
🔸
🔸
🔸
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/akhbarefori/682825" target="_blank">📅 17:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682824">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
حمله پهپادی یمن به نجران و آرامکو
🔹
نیروهای مسلح یمن با استفاده از پهپادهای تهاجمی، فرودگاه نجران و تأسیسات نفتی آرامکو را هدف قرار دادند که بنا بر گزارش‌ها، این عملیات با موفقیت کامل همراه بوده است.
🔹
این حملات در واکنش مستقیم به نقض حریم هوایی یمن (استان صعده) توسط پهپادهای سعودی صورت گرفته است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.22K · <a href="https://t.me/akhbarefori/682824" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682821">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9920553d6.mp4?token=lm_9fW7JzhO-vEqC6FxzM2da74W9vfW516gXwaXSFgT78tvaZxfeiF3XHcy9psafD9q-EEIKOGM9-6sPdGIlbuBaR-6H3Yma3S3kiiW3ypoKIBkMpXV6ckaDldvmLmoUzYkfpzB-UeUkoJNSXCCZDICXwwrQrB4H622xAScnGet92Rub_BABrFfzUcYtj4NUp0w2Genwju1X-hkijzZxRoZpkTbNcr1fr2A2K1fl1AtmoFMdT9c4fbKYMhMjyOuBGRrdVvwslz7-SdBePHohlcPQQqc0WmNWWV7NL4ValyZ1sLhD7SssyE-QjXRvBG97J55tUoZ36vKOE_31A3WMOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9920553d6.mp4?token=lm_9fW7JzhO-vEqC6FxzM2da74W9vfW516gXwaXSFgT78tvaZxfeiF3XHcy9psafD9q-EEIKOGM9-6sPdGIlbuBaR-6H3Yma3S3kiiW3ypoKIBkMpXV6ckaDldvmLmoUzYkfpzB-UeUkoJNSXCCZDICXwwrQrB4H622xAScnGet92Rub_BABrFfzUcYtj4NUp0w2Genwju1X-hkijzZxRoZpkTbNcr1fr2A2K1fl1AtmoFMdT9c4fbKYMhMjyOuBGRrdVvwslz7-SdBePHohlcPQQqc0WmNWWV7NL4ValyZ1sLhD7SssyE-QjXRvBG97J55tUoZ36vKOE_31A3WMOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای خانواده کنکوری‌ها مقابل دانشگاه امیرکبیر
/ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.13K · <a href="https://t.me/akhbarefori/682821" target="_blank">📅 17:33 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682820">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f68LWi8YCwe87DKfNiqs8qOdtbN5ihE7GxXTsl5KMPBTfbLUEB3DAmSD0cnnA0PzS8DYhQ_Jqd2UbyAv18ucmwIIIFUCVfc8U-CqkUrr7KVThhI39ka80dFmIlsqaeArCrdDEMWjJFddakRnqATlc3MDt5JfTzL320oE6z0l-dyfbtuWNWYr9AzcNHqtwVuq0a88VgWt-51znjCmPSRoe0oZpGQU7ATRXcSD322jnoGiWrc5-LDuExH8wVL54WhZfnH9ndwkCsHkZuAdZQntjtesT-Byyudo6Y6G7qb-XipHF5XEqjkSUeO7uKze4hXhHu7tEICU6-NppmNsddoHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقایسه کلی دو قدرت بزرگ؛ چین و روسیه
🔸
چین با جمعیتی حدود ۱.۴ میلیارد نفر، ۳.۵۹ تریلیون دلار صادرات دارد؛ در مقابل، روسیه با جمعیتی حدود ۱۴۵ میلیون نفر، ۳۷۷ میلیارد دلار صادرات دارد.
🔸
در بخش مالی، بدهی دولت چین معادل ۹۴ درصد تولید ناخالص داخلی GDP است؛ در حالی که این رقم در روسیه به ۱۸ درصد از GDP می‌رسد.
🔸
از نظر بودجه نظامی نیز، چین با بودجه دفاعی ۳۳۶ میلیارد دلاری، فاصله قابل‌توجهی با روسیه دارد که بودجه نظامی آن ۱۹۰ میلیارد دلار است.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/akhbarefori/682820" target="_blank">📅 17:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682819">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
نوری: دولت خسارات ناشی از جنگ به قایق‌های صیادی را جبران می‌کند
وزیر جهاد کشاورزی:
🔹
براساس گزارش‌های دقیق کارشناسی، روند جبران خسارات وارد شده به قایق‌های صیادی در جریان جنگ در هیئت دولت اصلاح شده است و پیگیری‌ها برای پرداخت کامل این خسارت‌ها ادامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/682819" target="_blank">📅 17:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682817">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">به وقت ایران ...
❤️
گاهی باید از فراز آسمان به ایران نگاه کرد
🔸
آن‌وقت می‌بینی این سرزمین، فقط مجموعه‌ای از شهرها و جاده‌ها نیست؛ قصه‌ی میلیون‌ها قلبی است که برای ساختن فردایی روشن، در کنار هم می‌تپند.
ایران، با همدلی ما روشن می‌ماند.
🇮🇷
#مصرف_بهینه_برق
🆔️
@tehran_roshan</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/akhbarefori/682817" target="_blank">📅 17:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682816">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
میراث فرهنگی
:
فعالیت تمامی معادنی که در ارتفاع بالاتر از ۱۷۰۰ متر، متوقف شده‌اند/ صدور هرگونه مجوز برای ایجاد معدن جدید و حتی احداث راه دسترسی در این ارتفاع ممنوع شده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/682816" target="_blank">📅 16:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682815">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07174a3739.mp4?token=dtyRN0YCRpxcuHCRyK65wbzeoRqJI3PI474nur_DH5Kb5Gh_sqvBEm2LrJVtkn3grmrRurAa7gOtQoHvv2WL7Z59yiVnrhQKEF6-2o0VVWH1Ab0JX4BJUvYdppF-f73SIe2mBVDXnr4lkubtMUoAjdpxqMFMOnU7X_tqOPCZaY3ghki66Y5UbmRSzRgxJ79QUdXAEjrf34RTeKICWQbxuIzlrvWwC0HOubmucYB37ZL9KL0MmMCzg68g43JENFndoHxZV1bwJ19XGmH5_cIwlCBdzpOyCI4wo9-FVI4SLpDzZRkZsiXiowRxK38TSuZKbXONP8CAWupuDTXs-wuPNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07174a3739.mp4?token=dtyRN0YCRpxcuHCRyK65wbzeoRqJI3PI474nur_DH5Kb5Gh_sqvBEm2LrJVtkn3grmrRurAa7gOtQoHvv2WL7Z59yiVnrhQKEF6-2o0VVWH1Ab0JX4BJUvYdppF-f73SIe2mBVDXnr4lkubtMUoAjdpxqMFMOnU7X_tqOPCZaY3ghki66Y5UbmRSzRgxJ79QUdXAEjrf34RTeKICWQbxuIzlrvWwC0HOubmucYB37ZL9KL0MmMCzg68g43JENFndoHxZV1bwJ19XGmH5_cIwlCBdzpOyCI4wo9-FVI4SLpDzZRkZsiXiowRxK38TSuZKbXONP8CAWupuDTXs-wuPNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام یک پهپاد در نزدیکی میدان گازی «نپتون دیپ» رومانی
🔹
جنگنده‌های F-۱۶ رومانی در عملیاتی ضربتی، یک پهپاد انتحاری دریایی (USV) را در فاصله چند صد متری پروژه گازی «نپتون دیپ» در دریای سیاه منهدم کردند تا از بروز یک فاجعه در زیرساخت‌های انرژی جلوگیری کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/682815" target="_blank">📅 16:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682814">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
اسوشیتدپرس: اسلام‌آباد برای ازسرگیری مذاکرات، با ایران و آمریکا در تماس است
🔹
مقام‌های پاکستانی می‌گویند رهبری سیاسی و نظامی این کشور همچنان با ایران و آمریکا در تماس است تا تلاش‌ها برای کاهش تنش و حرکت به سمت ازسرگیری مذاکرات را بررسی کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/682814" target="_blank">📅 16:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682813">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1cf80d568.mp4?token=oOyWEwhYE0NwsHP4iZwbwX8BcDaXZlMZS5PzdhlTR_9zJai5em_cdiAS4i00NLAz_EEEZ-pdFBeQXVPDgZVvRdwGTFRxvPAj91UJKyZCj5-aE-aFlyRP8nO8q_XqLmneUrOVwrYymkfZAAler6jARC789HassY2UMl8np6HROe5nZTAdaJiWODyzLYnmp1wR2EX3ndQPws8n4dBcEgw27E19hT1QomHkQfDgCQcIMlYwJ6XQ6vt9eoKXPztj22bQa9Tcu3kkdwov3RlFmINXw2-oLVaEK8fa0NQOrlW2P_V9UvP2pDv4h86cRbLPE5a4hHD21d0BiUBiPyfYCLO9uhg43RaCQsaVELugKuGjH7nvf3X3D-g7GZQkma8mcBM61so4OhgBWv4Z2fRDrB6ipNb1wOTHSnKdOD8bNZOk2DCJFa_vsqDV7wBy8Fak6pmJyJesTPDJxCl1PqiiW7ZaeYDqIf1eaoRclBJz3PtaOXA9PMa6aYuOlngNvVwFHoF4OyUCaBluT1Juh2UMs5zNoj2C7NUWKrcXORBrISf-Vtdff_yeqkJRksWFRT-o-KI644OATaUGd7rjrlHCbN99VuD56bLJZ2vVssw_f31eOWvssnaSIBRP4fA6ae5_mqWRWpD9eCbWvIWJIvR3Sle7y02fvWNrmE9xENpVlZJw2I0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1cf80d568.mp4?token=oOyWEwhYE0NwsHP4iZwbwX8BcDaXZlMZS5PzdhlTR_9zJai5em_cdiAS4i00NLAz_EEEZ-pdFBeQXVPDgZVvRdwGTFRxvPAj91UJKyZCj5-aE-aFlyRP8nO8q_XqLmneUrOVwrYymkfZAAler6jARC789HassY2UMl8np6HROe5nZTAdaJiWODyzLYnmp1wR2EX3ndQPws8n4dBcEgw27E19hT1QomHkQfDgCQcIMlYwJ6XQ6vt9eoKXPztj22bQa9Tcu3kkdwov3RlFmINXw2-oLVaEK8fa0NQOrlW2P_V9UvP2pDv4h86cRbLPE5a4hHD21d0BiUBiPyfYCLO9uhg43RaCQsaVELugKuGjH7nvf3X3D-g7GZQkma8mcBM61so4OhgBWv4Z2fRDrB6ipNb1wOTHSnKdOD8bNZOk2DCJFa_vsqDV7wBy8Fak6pmJyJesTPDJxCl1PqiiW7ZaeYDqIf1eaoRclBJz3PtaOXA9PMa6aYuOlngNvVwFHoF4OyUCaBluT1Juh2UMs5zNoj2C7NUWKrcXORBrISf-Vtdff_yeqkJRksWFRT-o-KI644OATaUGd7rjrlHCbN99VuD56bLJZ2vVssw_f31eOWvssnaSIBRP4fA6ae5_mqWRWpD9eCbWvIWJIvR3Sle7y02fvWNrmE9xENpVlZJw2I0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانشکده فارس، مسیر درست ورود به حرفه خبرنگاری
ثبت‌نام بدون کنکور دانشکده رسانه خبرگزاری فارس آغاز شد.
این مسیر شامل:
آموزش‌های تخصصی
کار عملی در تحریریه خبر
رشته های تحصیلی  شامل :
🖊
خبرنگاری |
📸
عکاسی |
🎥
سینما و تدوین |
🎙
گویندگی |
🤝
روابط‌عمومی
📌
روش ثبت‌نام:
📱
ارسال عدد ۱۴ به سامانه ۵۰۰۰۱۰۱۴
🌐
ثبت‌نام از طریق لینک زیر اقدام نمائید
futurix.ir/go/rxDxXO
مهلت ثبت‌نام محدود است.
✅
اولویت با متقاضیانی است که زودتر اقدام نمایند.
🆔
ایتا:
@Farsnewsfaculty
🔹
مرکز آموزش علمی کاربردی خبرگزاری فارس
🔹</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/akhbarefori/682813" target="_blank">📅 16:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682811">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fb044920a.mp4?token=jQvfajsqGqsqlMuuXqMncM4Gn-7-GsFor3zxkIYSphSFthljMp5X8TVv7PaAuodvsAXe_34g-ZrPpLzJ-1PGFpdweb_cGzgZql3l45xstCGG_MPZVMEGubiTc0K5mHvdJQimu2xDhv6xtdt8JBGzim50AKylmND_JAbTlx7KQLlbIWaoqS4wnzW0pNcp9XueyUXO_GgQLb_r0aR1hkPrdEfsue58rc4aTrLWy_Jel_ns0tiQ9_d4mgs5E5kqbWDhEM6-zfycVk7umh5C02-GohACkMKQppJfNgsnFig-dRbDICC1S6mlXwqDaHEf1hVbhJg4zEZDgNubMVaJW9TL3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fb044920a.mp4?token=jQvfajsqGqsqlMuuXqMncM4Gn-7-GsFor3zxkIYSphSFthljMp5X8TVv7PaAuodvsAXe_34g-ZrPpLzJ-1PGFpdweb_cGzgZql3l45xstCGG_MPZVMEGubiTc0K5mHvdJQimu2xDhv6xtdt8JBGzim50AKylmND_JAbTlx7KQLlbIWaoqS4wnzW0pNcp9XueyUXO_GgQLb_r0aR1hkPrdEfsue58rc4aTrLWy_Jel_ns0tiQ9_d4mgs5E5kqbWDhEM6-zfycVk7umh5C02-GohACkMKQppJfNgsnFig-dRbDICC1S6mlXwqDaHEf1hVbhJg4zEZDgNubMVaJW9TL3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
بازتاب دغدغه‌های واقعی؛ روایت بدون پرده شما از بحران اشتغال، هزینه‌های سنگین و بن‌بست‌های مسیر تاهل.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/akhbarefori/682811" target="_blank">📅 16:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682810">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
جام جهانی ۲۱۱ تیمی به‌خاطر اسرائیل
🔹
نشریۀ اتلتیک از طرح محرمانۀ اینفانتینو برای «جام جهانی زیر ۱۵ سال» با ۲۱۱ کشور یعنی تمام اعضای فیفا پرده برداشت.
🔹
رئیس فیفا در این طرح قصد داشت بازی افتتاحیه را میان دو تیم فلسطین و اسرائیل برگزار کند که مورد قبول بسیاری از اعضای فیفا قرار نگرفت.
🔹
این طرح هرچند در ظاهر منابع مالی خوبی برای ۲۱۱ عضو فیفا داشت اما در پشت‌پرده به‌دنبال عادی‌سازی روابط فلسطین و اسرائیل بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/akhbarefori/682810" target="_blank">📅 16:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682809">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e8f254d3f.mp4?token=kAp-9G0-kP4t8yQAoInY91hUCf2oZyE5GPVRcYLAQjDKCRP1HP9AwYu66fdcvTNr-H7yLBA1G53zOqIpPavyH6quOi9K-XN23XzOvMJELTOqcnZiILZq8bnx6pnhcEi4N9QQMK6cINGfZQdAk3Zg_JqSAJola3IxGqXBBv6r-PYjSuGgCbTE16LDH_tN7EFC8EyMueGlMjPF8VV4UBe_ioz4oTfxsXWGpUsbhK-QbAWYzYwiUoCnly-W1tmb9sahCCAXE93mQECEQ9sbEk3BR8g-nbmsSUTBicaFcaDT50DXg9fUFc2L_BN7JrnBqBEzoNp1d-U-EyOaUgJaRFpaCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e8f254d3f.mp4?token=kAp-9G0-kP4t8yQAoInY91hUCf2oZyE5GPVRcYLAQjDKCRP1HP9AwYu66fdcvTNr-H7yLBA1G53zOqIpPavyH6quOi9K-XN23XzOvMJELTOqcnZiILZq8bnx6pnhcEi4N9QQMK6cINGfZQdAk3Zg_JqSAJola3IxGqXBBv6r-PYjSuGgCbTE16LDH_tN7EFC8EyMueGlMjPF8VV4UBe_ioz4oTfxsXWGpUsbhK-QbAWYzYwiUoCnly-W1tmb9sahCCAXE93mQECEQ9sbEk3BR8g-nbmsSUTBicaFcaDT50DXg9fUFc2L_BN7JrnBqBEzoNp1d-U-EyOaUgJaRFpaCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصادف عجیب دو دختر نوجوان موتورسوار با تریلی در ابهر
🔹
دو دختر نوجوان موتورسوار روز گذشته در میدان ترمینال ابهر با تریلی پارک‌شده برخورد کردند و مصدوم شدند.
#اخبار_زنجان
در فضای مجازی
👇
@akhbarzanjan</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/682809" target="_blank">📅 16:16 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682808">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
پلتفرم طلایی مسدود شده، مربوط به جنگ ۱۲ روزه بود/ پلتفرم‌های طلا به فعالیت خود ا‌دامه می‌دهند
رضا الفت‌نسب رئیس اتحادیه کسب‌وکارهای مجازی در همایش زرآتی اقتصادآنلاین:
🔹
یک سوبرداشتی در رسانه‌ها شده که نگرانی‌هایی را برای کاربران ایجاد کرده است که می‌خواهم شفاف‌سازی کنم.
🔹
موضوع پلتفرم مسدود شده به جنگ ۱۲ روزه برمی‌گردد که در آن زمان حساب‌ها مسدود شد. مجموع این اختلالات منجر به این شد که فعالیت پلتفرمی دچار مشکل شده، متوقف شود.
🔹
این که در خبرها آمده مبنی بر اینکه ۲۰۰ هزار خالی فروشی صورت گرفته، چنین چیزی را نشان نمی‌داد؛ بلکه ۲۰۰ هزار کاربر داشت و شکایاتی هم که به اتحادیه رسید کمتر از ۱۰۰ فقره بود/ اقتصادآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/682808" target="_blank">📅 16:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682807">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58c0e4ce1c.mp4?token=SNyIQwrH_V8D5twoKlg2Ozy_5gkLOkeAin6SI2VqOQUzzRd_tLH10W6Dk6jqXrZ9gXWA_47xrH_y93jpzJtDZIPernO10FoPtAn21ITJoEPI6HCcTlM7qJH0YJU1v6JUPr9Y_gsOjN465jGgpsta45vM0DZU9HXiUe1DIV8k_Rc6LFl3dqjPILYTzUb5CE6CwMf6h__7JCcZoqjDRTYXOGiAWmWS-ULMccy_QH66IIEoeQ9UPbHNp3DBB83ptw7t9PqScY1nZEQolU8o4twQbuXzdRAWRaramBOdoAzKErxFKFboVX5Ztw6UJeY4M-l7K-c42Pte2unA6ztZld1QRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58c0e4ce1c.mp4?token=SNyIQwrH_V8D5twoKlg2Ozy_5gkLOkeAin6SI2VqOQUzzRd_tLH10W6Dk6jqXrZ9gXWA_47xrH_y93jpzJtDZIPernO10FoPtAn21ITJoEPI6HCcTlM7qJH0YJU1v6JUPr9Y_gsOjN465jGgpsta45vM0DZU9HXiUe1DIV8k_Rc6LFl3dqjPILYTzUb5CE6CwMf6h__7JCcZoqjDRTYXOGiAWmWS-ULMccy_QH66IIEoeQ9UPbHNp3DBB83ptw7t9PqScY1nZEQolU8o4twQbuXzdRAWRaramBOdoAzKErxFKFboVX5Ztw6UJeY4M-l7K-c42Pte2unA6ztZld1QRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مهم‌تر از درس‌های مدرسه، اموزش این پنج قانون مالیه که آینده فرزندتون رو‌ می‌سازه  #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/akhbarefori/682807" target="_blank">📅 16:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682805">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">♦️
بانک مرکزی: در ادامه اجرای حکم دادسرای جرائم اقتصادی؛ اسناد انتقال دارایی‌های تعاونی اعتبار منحله مولی‌الموحدین و بانک ایران زمین به بانک مرکزی امضا شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/682805" target="_blank">📅 16:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682804">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55cbce766c.mp4?token=W24XJ9n8mHl6t9oi5w2tj-t1svqDdmP5y3O2FLZKuG6S376z6QgY70H3mmr2svMkt-wynyRQtCv7ZtYXNyhY5BWM8WNVlUQMGPT9-1xKZHRFCRRdUp0wQQNrZs34ryAbiQoQ22YgyuabtALeCBBcSG2LRYJNg3rU_sPDJGzDCWzsNNaibZ40tADudMLJK7dkQ6mQu1wW-sBXwFNdWWa6fkF9uSOEEgkQy2XGSjSC4YY5twJx_0BqQuEp5GXMete_AwXHYztO8FLTezMkDmZrF4RFNnyA7R4Yp_hs5HHRe2DSXv-2Ptx9VCjk34a1zvCRQxnwWqZxGCOvSBXFYng-gYgCEvcFzKpmn7lin0cGPymVReElVsT9V2qdQKnF_qVKvXjcOociudffZlW_3QG6Xmy0cVWyYOC0v7ugyqZRspfpBft1DTWPhMYlHeHpLlMvAibO8venMjIaRSaaPJ3y9Vx8fCfrwAIC7Zs141RitrZgAlGK9-pRnOYI9N8ZiwAEe4q8w4scMOVYD14dv4MY5NhF-zdtLAQudBQkGROiNTNV5LwiUEOAaEd2LiH-0U7zKVmvV7V-IYCE7XxyOug1lAsh9rcwKz9eErjWQMDvsXJ-SIqluJlVQBSvK13awfgopjQ5M36m09M1x9TWolmoyqTjz35npjyJOYNzRj-R-oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55cbce766c.mp4?token=W24XJ9n8mHl6t9oi5w2tj-t1svqDdmP5y3O2FLZKuG6S376z6QgY70H3mmr2svMkt-wynyRQtCv7ZtYXNyhY5BWM8WNVlUQMGPT9-1xKZHRFCRRdUp0wQQNrZs34ryAbiQoQ22YgyuabtALeCBBcSG2LRYJNg3rU_sPDJGzDCWzsNNaibZ40tADudMLJK7dkQ6mQu1wW-sBXwFNdWWa6fkF9uSOEEgkQy2XGSjSC4YY5twJx_0BqQuEp5GXMete_AwXHYztO8FLTezMkDmZrF4RFNnyA7R4Yp_hs5HHRe2DSXv-2Ptx9VCjk34a1zvCRQxnwWqZxGCOvSBXFYng-gYgCEvcFzKpmn7lin0cGPymVReElVsT9V2qdQKnF_qVKvXjcOociudffZlW_3QG6Xmy0cVWyYOC0v7ugyqZRspfpBft1DTWPhMYlHeHpLlMvAibO8venMjIaRSaaPJ3y9Vx8fCfrwAIC7Zs141RitrZgAlGK9-pRnOYI9N8ZiwAEe4q8w4scMOVYD14dv4MY5NhF-zdtLAQudBQkGROiNTNV5LwiUEOAaEd2LiH-0U7zKVmvV7V-IYCE7XxyOug1lAsh9rcwKz9eErjWQMDvsXJ-SIqluJlVQBSvK13awfgopjQ5M36m09M1x9TWolmoyqTjz35npjyJOYNzRj-R-oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیر؛ یک خوراکی کوچک با خواص بزرگ!
🧄
🔹
سیر سرشار از ترکیبات مفیدی است که می‌تواند به حمایت از سلامت قلب، تقویت سیستم ایمنی و حفظ سلامت عمومی بدن کمک کند. بهترین نتیجه زمانی به دست می‌آید که در کنار یک رژیم غذایی متعادل و سبک زندگی سالم مصرف شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/682804" target="_blank">📅 15:50 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682803">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzNh3UFM8GZD0WvJnbD0_bZswjZzdj8lg3Ov7u8XAOj020RzncGG9_ChQahCfU2wq5gGuXies2Z-HDDeDfY2LJOPxKOgd6baniPhqmDULbWSVFso9Fizu4rd0dzpdm4-8nsijCQlEhM1_toDwS9_Lo8mb4Vj3wVh6RagV8z-qxBUTBJbPmgj6YRp11AXRT_Z8MkurBEVze_rYBY0yqiNNpPGKz5BoU9jCtLPLPNjgzMr61SF0O8D7aix6hTfuvMpLq4BinYQxeY56UlZbFPWB-DMK2DIwjpVkjqQfrt98Eb3coDugCVwfneX6TxPux4kusPnw6ArIehNu6S8S1CVKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عکسی از دنسه هتل گیلاریا، فینالیست Architecture Photography Awards 2026 شد
🔹
عکسی از دنسه هتل گیلاریا که توسط امیررضا دهنادی ثبت شده، به مرحله نهایی رقابت‌های Architecture Photography Awards 2026 راه یافته و در میان آثار فینالیست این مسابقات بین‌المللی عکاسی معماری قرار گرفته است.
🔹
راه‌یابی تصویر دنسه هتل گیلاریا به مرحله نهایی این رقابت، در کنار حضور آثار عکاسان بین‌المللی، بازتابی از معماری و فضاهای اقامتی ایران در یک رویداد تخصصی جهانی عکاسی معماری است. این هتل در استان گیلان، بندر کیاشهر واقع شده است.
🔹
برندگان نهایی Architecture Photography Awards 2026 قرار است ۲۲ آگوست ۲۰۲۶ معرفی شوند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/682803" target="_blank">📅 15:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682802">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یارانۀ ۳۰۰ هزار تومانی مرداد به حساب سرپرستان خانوار دهک‌های ۴ تا ۹ واریز شد
.
🔹
رئیس مجلس به کربلا رسید.
🔹
روس‌اتم: به ساخت نیروگاه‌های هسته‌ای در ایران ادامه می‌دهیم.
🔹
دفتر زلنسکی درخواست وزیر دفاع سابق برای برگزاری انتخابات را رد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/682802" target="_blank">📅 15:41 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682801">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
مزدوران سعودی اینترنت استان مأرب یمن را قطع کردند
🔹
منابع محلی در استان مأرب گزارش دادند که مزدوران وابسته به عربستان سعودی در ادامه اقدامات ضدانسانی خود، دسترسی مردم به اینترنت و خدمات ارتباطی را در این استان قطع کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/682801" target="_blank">📅 15:24 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682800">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07c271daa3.mp4?token=ptlKBkYhyCM9xex3omyhLJmKQNICRqLas7s-0L6CmcZt7j3e_yaguOrDSak_SuboyzCfcmqI7fzXaA3lilTw-w7Az6cCTpGx_5k1ULABsOimDG-UuMEQcPWoBuu6tGQ9USPRw-fkB3UfhvkM3WzJZlKysBopYWkUdb5PizsG-pTIUso6dI7-Vhfgppsk0m-ALpE2LNuE3lNEjTE3umTgSCb9h5oI0zYBFacYMMRWW0j8PsKqDDIzwUfbFVNnuoJow7Iifc52hDmPexhyiB5beOtMITxoc3FCLs2YgOTHYhsIgsYf2aovNkqLLx-wIg-gIFkgpgQ3DwgHhpHpOfXM3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07c271daa3.mp4?token=ptlKBkYhyCM9xex3omyhLJmKQNICRqLas7s-0L6CmcZt7j3e_yaguOrDSak_SuboyzCfcmqI7fzXaA3lilTw-w7Az6cCTpGx_5k1ULABsOimDG-UuMEQcPWoBuu6tGQ9USPRw-fkB3UfhvkM3WzJZlKysBopYWkUdb5PizsG-pTIUso6dI7-Vhfgppsk0m-ALpE2LNuE3lNEjTE3umTgSCb9h5oI0zYBFacYMMRWW0j8PsKqDDIzwUfbFVNnuoJow7Iifc52hDmPexhyiB5beOtMITxoc3FCLs2YgOTHYhsIgsYf2aovNkqLLx-wIg-gIFkgpgQ3DwgHhpHpOfXM3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتش‌سوزی در شهر نجف
اشرف
🔹
دقایقی پیش گزارش‌ها از وقوع حریق در یکی از ساختمان‌های در حال ساخت واقع در محله «عدن» در شهر نجف اشرف خبر دادند. تیم‌های امدادی و آتش‌نشانی برای مهار شعله‌ها به محل حادثه اعزام شدند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/682800" target="_blank">📅 15:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682799">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromموسسه نیکوکاری مهرآفرین پناه عصر</strong></div>
<div class="tg-text">📹
حوا و دخترانش سال‌ها خشونت را تحمل کردند و امروز با ترس دیگری روبه‌رو هستند؛
بی‌خانمانی.
🌿
پنجشنبه مهرورزی این هفته ؛ برای تأمین ودیعه مسکن مادران و کودکان در معرض بی‌خانمانی همراه می‌شویم.
💳
6037991199529904
💳
6037991199506100
💳
6037991199500038
🔖
IR710170000000216780692009
📲
*780*35260 #
📌
کمک مستقیم به حوا و دخترانش، واتساپ و تلگرام:
📲
+989101785282
🔻
پرداخت مستقیم
Mehrafarincharity.com
⭐️
مهرآفرین باشیم
|
اینستاگرام
|
وب سایت
|
پرداخت آنلاین
|
❤️
@mehrafarincharity</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/682799" target="_blank">📅 15:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682797">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df6be216f.mp4?token=AZA2LogkdEq_-svB48mIYI4bysRMevO6VCNRhSqbrcLFXrI_pSMFmJRaH_JkV346blvKAFBpGzgw52_6hYp9ihxs_8xnbfnmd8pzhKEajA-XYgAklwNkUoZsCrJZrTaUkkokcyYxkimCU6mrgds76697Q12fkyMvqGdBclcYy30LdGXQqWM6xMzvC45bnuCaNQ9_BOMXDvfMKEXn45K5nytDNpm65TPVsF_VFF0YfZQkmSWUKrQxKqj7N0AY_RAx00K3jUBQ6sE_xj0S2Ws4I5UfLDYXt-ClTLi9mIrYZSRcuZxuyj2UPLfAbT0o4pFRoM3laraCxd-jUZLd3YAE3AcQhq1gw2irxwJY17VFqVi4hiw5Wkqg7jhH-_aBYE7ojnT4WsUTNFPL7CkqJ3xw6SwFUaaB1onVcBxyinybfWXPjxTwYYLOj7LcZ-AHjX4DeZiarYoomnwygaZSnm5FXcwyZw9s91kNYXCA8w4UxZPyGGw77u8sOUaGXWRV_IP6Xw-JF5AO87FZA7R4JpV1CtlPFf6aqOb8LK09RbC3VQeXrcv0aF0ZA1eJiFR8EYXm6HkvtaijTkHMQWX27RKMHRMcZEDmQH58o3pY7o8WElB0b_VFlCJiQQdr4XqMhqQ_1zoh5n-vDWnX3Z7pCecE3Q4q9D35W3mC5Ie4wJYpA8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df6be216f.mp4?token=AZA2LogkdEq_-svB48mIYI4bysRMevO6VCNRhSqbrcLFXrI_pSMFmJRaH_JkV346blvKAFBpGzgw52_6hYp9ihxs_8xnbfnmd8pzhKEajA-XYgAklwNkUoZsCrJZrTaUkkokcyYxkimCU6mrgds76697Q12fkyMvqGdBclcYy30LdGXQqWM6xMzvC45bnuCaNQ9_BOMXDvfMKEXn45K5nytDNpm65TPVsF_VFF0YfZQkmSWUKrQxKqj7N0AY_RAx00K3jUBQ6sE_xj0S2Ws4I5UfLDYXt-ClTLi9mIrYZSRcuZxuyj2UPLfAbT0o4pFRoM3laraCxd-jUZLd3YAE3AcQhq1gw2irxwJY17VFqVi4hiw5Wkqg7jhH-_aBYE7ojnT4WsUTNFPL7CkqJ3xw6SwFUaaB1onVcBxyinybfWXPjxTwYYLOj7LcZ-AHjX4DeZiarYoomnwygaZSnm5FXcwyZw9s91kNYXCA8w4UxZPyGGw77u8sOUaGXWRV_IP6Xw-JF5AO87FZA7R4JpV1CtlPFf6aqOb8LK09RbC3VQeXrcv0aF0ZA1eJiFR8EYXm6HkvtaijTkHMQWX27RKMHRMcZEDmQH58o3pY7o8WElB0b_VFlCJiQQdr4XqMhqQ_1zoh5n-vDWnX3Z7pCecE3Q4q9D35W3mC5Ie4wJYpA8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عظمت کیهان باور کردنی نیست
!
🌍
🔹
محاسبات علمی نشون داده که عالم ما با این عظمت و بزرگی فقط یکی از بی‌نهایت عالم ممکن است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/682797" target="_blank">📅 15:14 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682796">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مشاور امنیت ملی عراق در دیدار با قالیباف: بغداد بر تقویت روابط راهبردی با ایران مصمم است.
🔹
آنکارا: تهدیدهای نتانیاهو علیه ترکیه و سوریه، نشانه انزوای اوست.
🔹
آلمان و ایتالیا همکاری‌ها برای مهار هجوم پناهجویان را تقویت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/682796" target="_blank">📅 15:08 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682795">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بینی‌مو عمل کنم، خیلی کیوت میشم!
🔹
فقط بینی نیست، وقتی عمل زیبایی از سن کم شروع میشه، خیلی وقت‌ها بعدش یه ایراد جدید پیدا میشه و دوباره نوبت تغییر دادن یه جای دیگه‌ست.
🔹
انگار این روزا بعضیا تا وقتی چند جای صورتشون رو عوض نکنن، باور نمی‌کنن خوشگلن!
🇮🇷
✊
…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/682795" target="_blank">📅 15:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682794">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
نگرانی امارات نسبت به تبعات اقدام ضد ایران
🔹
روزنامه وال استریت ژورنال به نقل از منابع آگاه گزارش داد که آمریکا از امارات خواسته فشارهای اقتصادی علیه ایران را تشدید کند.
🔹
این در حالیست که مقامات اماراتی بیم آن دارند راهبرد آمریکا در قبال ایران به بخش‌های اقتصادی کشورهای حوزه خلیج فارس ضربه وارد کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682794" target="_blank">📅 14:55 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682793">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
اعتصاب کارکنان، فرودگاه بن‌گوریون تل‌آویو را به تعطیلی کشاند
🔹
منابع خبری از آغاز اعتصاب گسترده کارکنان در فرودگاه «بن‌گوریون» در تل‌آویو و ترک محل کار توسط پرسنل این فرودگاه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/682793" target="_blank">📅 14:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682792">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6073d64997.mp4?token=GJg4IIQ-62Os8KoNQbxAoId8hmxmvaHLUwVfAuQ8FjyX0RjX0vLfZSaCIgwdj0sj7qyJ09EuBWuyk_6RXqVoyXRh8C6aNZWRnktoDy-YYUNPFS5WRQb4sFgbGXe9J1q7VN61Sf3t-R9sfalIBuN8vOdAUYxsmHv24_FSALja87OcGCoM4mNTPhjRlc_RIXg1rycHO8oDW31EjS5DqR4e1e7W05mTo-CSp_em0DWnx0Z3KeZUUaOQefDjroXw31FwxUQIUF0FYMger4f2Ja1L1tQsK-DTEE2hvqwUwGUkx7_h7EtxlnRWdhGJxN9J_UE4iFaNqC-bgHql3I0hNsROtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6073d64997.mp4?token=GJg4IIQ-62Os8KoNQbxAoId8hmxmvaHLUwVfAuQ8FjyX0RjX0vLfZSaCIgwdj0sj7qyJ09EuBWuyk_6RXqVoyXRh8C6aNZWRnktoDy-YYUNPFS5WRQb4sFgbGXe9J1q7VN61Sf3t-R9sfalIBuN8vOdAUYxsmHv24_FSALja87OcGCoM4mNTPhjRlc_RIXg1rycHO8oDW31EjS5DqR4e1e7W05mTo-CSp_em0DWnx0Z3KeZUUaOQefDjroXw31FwxUQIUF0FYMger4f2Ja1L1tQsK-DTEE2hvqwUwGUkx7_h7EtxlnRWdhGJxN9J_UE4iFaNqC-bgHql3I0hNsROtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هانتر بایدن پسر رئیس‌جمهور سابق آمریکا: ترامپ اصلا نمی‌داند تنگه هرمز کجاست
🔹
من عمیقا نگرانم که چطور کسی که این‌قدر جاهل و نادان است در دفتر بیضی کاخ سفید نشسته.
🔹
فقط این نیست که رشوه‌خوار، بی‌رحم و فاسد باشد. او یک احمق کامل و تمام‌عیار و جاهل مطلق هم هست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/682792" target="_blank">📅 14:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682791">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39f16043.mp4?token=GKZKvDImTyJ_bi-X8y-hFtQDE6MThaKRQKBx619X42wHypR4kf8t-x79qQrdtyhTve2IryeF8vDZv7a2alKANRmH0jxesvjs3ur_fCK1GGuaAp7SvWifAt-mqbEAUXLNQlOOTxhBCVhb0Dr0mvRPLRJEVG2_ARLzy3Y2CU1-idOVpJ0fehWIgwFVzwQJg_cjeAvOHLyTLazHGo18SxetVlrDlSoBtRaDy1AnAixfQPc1BoZdZs63rVaCrLnq9Sa7qOTc_vG6Hq2wvjR3TQHvVMsPSbES3hJb0z4m9NOAlEYnbSPUlk87t1Ni4KKJf9mbg7bZVcS4zhuYe_-W9GGceIhmSZFfxKE54XZI1r8eqvPJPLUDnUur61QgIeKJHw_XW4Rci6gfO4hViMoQV1SWT-yrl6db0pLmymG9VRSwp6gGH229xdXBT86euwqDE552ictLa7DXzGp2hutj-zG2vt_dpD4mWpwx1QX2x8vNL-8asY1ByNVSn7DNmCF33lxoXeRzKFKZ3PEblonJi9by-ifhhmGsYaHuJzj5JTDQNtgLfLDGU-wbVEIvGauanJh0nvDZVk75zpaIXb8yzUN9gVqMSs625o-hPmy3ijcmtECXGoq070sQgyp2a-3oiKPhzLUcvZVFTUMcgEHki5yJ80BRSuRcBMPXtD4Tf5fwwQE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39f16043.mp4?token=GKZKvDImTyJ_bi-X8y-hFtQDE6MThaKRQKBx619X42wHypR4kf8t-x79qQrdtyhTve2IryeF8vDZv7a2alKANRmH0jxesvjs3ur_fCK1GGuaAp7SvWifAt-mqbEAUXLNQlOOTxhBCVhb0Dr0mvRPLRJEVG2_ARLzy3Y2CU1-idOVpJ0fehWIgwFVzwQJg_cjeAvOHLyTLazHGo18SxetVlrDlSoBtRaDy1AnAixfQPc1BoZdZs63rVaCrLnq9Sa7qOTc_vG6Hq2wvjR3TQHvVMsPSbES3hJb0z4m9NOAlEYnbSPUlk87t1Ni4KKJf9mbg7bZVcS4zhuYe_-W9GGceIhmSZFfxKE54XZI1r8eqvPJPLUDnUur61QgIeKJHw_XW4Rci6gfO4hViMoQV1SWT-yrl6db0pLmymG9VRSwp6gGH229xdXBT86euwqDE552ictLa7DXzGp2hutj-zG2vt_dpD4mWpwx1QX2x8vNL-8asY1ByNVSn7DNmCF33lxoXeRzKFKZ3PEblonJi9by-ifhhmGsYaHuJzj5JTDQNtgLfLDGU-wbVEIvGauanJh0nvDZVk75zpaIXb8yzUN9gVqMSs625o-hPmy3ijcmtECXGoq070sQgyp2a-3oiKPhzLUcvZVFTUMcgEHki5yJ80BRSuRcBMPXtD4Tf5fwwQE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گاهی یک تصویر، بیشتر از هزار کلمه حرف برای گفتن دارد؛ روایتِ آدم‌هایی که برای ایران، از دل و جان ایستاده‌اند
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/682791" target="_blank">📅 14:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682790">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
دولت فرانسه نیلوفر شادمهری، رایزن فرهنگی جمهوری اسلامی ایران، را از این کشور اخراج کرد.
🔹
عارف: شوراهای عالی نباید در امور اجرایی دانشگاه‌ها دخالت کنند.
🔹
سفر وزیر خارجه سوریه به پاکستان پس از ۱۹ سال
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/682790" target="_blank">📅 14:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682789">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🧠
شما چه تیپ سرمایه‌ گذاری هستید؟
تصمیم های مالی ما همیشه فقط بر اساس منطق و محاسبات نیستند. ترس از ضرر، هیجان، اعتماد به ‌نفس و میزان تحمل ریسک هم میتونن روی انتخاب‌ هامون اثر بذارن.
به همین دلیل ممکنه دو نفر با سرمایه و اطلاعات مشابه، تصمیم های کاملا متفاوتی بگیرن چون شخصیت و رفتار سرمایه‌گذاریشون یکی نیست.
یک تست جالب هم برای شناخت همین ویژگی‌ ها طراحی شده که با چند سوال، تیپ سرمایه ‌گذاری شما رو مشخص میکنه.
🔗
https://ifrb.ir/rknt</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/682789" target="_blank">📅 14:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682788">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df511ba0d.mp4?token=hPyvqhn7Df--GAGtN3tQkrqvYmTno_FEUcVsMc55ko99V-_XuqoskbYK8dvbV8x9bxYfx00zz6DRIEQejfs-fBUVOTZSKQJ6AlzAAj28Xx8WjtdneJIRLg4H-tVUbMXBfGiWBibcXw6g7yoknuO9NFp81hzJ43zR7yn5LwQOq47NuDTq-Ft77SnhkGCSsUF1G9U9CTa-A9umK14POmMRrUQEpr3xcRqM876SoI2OrQklWGQaJ6XB9qpn4cXFOtLcQ3qLdwcRswJBU7BEY1KIt5h1kSIckJjcyT2qKRWC6IYKRSjX9CMy_abPzvfFI7aXV7rDPdfdTFLnMWoAcfbLVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df511ba0d.mp4?token=hPyvqhn7Df--GAGtN3tQkrqvYmTno_FEUcVsMc55ko99V-_XuqoskbYK8dvbV8x9bxYfx00zz6DRIEQejfs-fBUVOTZSKQJ6AlzAAj28Xx8WjtdneJIRLg4H-tVUbMXBfGiWBibcXw6g7yoknuO9NFp81hzJ43zR7yn5LwQOq47NuDTq-Ft77SnhkGCSsUF1G9U9CTa-A9umK14POmMRrUQEpr3xcRqM876SoI2OrQklWGQaJ6XB9qpn4cXFOtLcQ3qLdwcRswJBU7BEY1KIt5h1kSIckJjcyT2qKRWC6IYKRSjX9CMy_abPzvfFI7aXV7rDPdfdTFLnMWoAcfbLVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتصاب کارکنان، فرودگاه بن‌گوریون تل‌آویو را به تعطیلی کشاند
🔹
منابع خبری از آغاز اعتصاب گسترده کارکنان در فرودگاه «بن‌گوریون» در تل‌آویو و ترک محل کار توسط پرسنل این فرودگاه خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/682788" target="_blank">📅 14:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682787">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
احتمال جاری شدن سیل در ۵ استان کشور
سخنگوی سازمان مدیریت بحران کشور
:
🔹
برای جمعه، احتمال وقوع سیلاب و آبگرفتگی در استان‌های گلستان، خراسان شمالی، شرق مازندران و ارتفاعات شمالی خراسان رضوی و سمنان وجود دارد.
🔹
رگبار شدید باران، آبگرفتگی و بادهای شدید پدیده غالب روز جمعه در این مناطق خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/682787" target="_blank">📅 14:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682786">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
آزمون گروه‌های هنر و زبان‌های خارجی کنکور ۱۴۰۵ آغاز شد
🔹
رقابت داوطلبان آزمون سراسری ۱۴۰۵ در دو گروه‌ آزمایشی هنر و زبان‌های خارجی، بعد از ظهر امروز، پنجشنبه ۲۹ مردادماه در حوزه‌های امتحانی سراسر کشور آغاز شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/682786" target="_blank">📅 14:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682784">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzrHyTjHhfWc3pVMASSHf9qSgdVnBgYCcemW19NNRPYFRf24uC47fqtKWViisoIfOREnRcKRSJwyuRdJ6ulLASdVGsRLXyf9GRKIfZI4wKxlZXSKnBqNJjFHin3Bnoelp9czje9txfUZCOgJnUfTLXw580SCjtxfFvV1erWlW5tjjNqRYkhewafuWoP29ng_AoS1XIB-tNOy5Ctnu79yNPpT5v9blhIJFj2-oaENhY1c7KNplWYiP9THqZ2GLWueI2wfD3AEq6y7wW6khPElvkI5ieojN5jKz3UqpFSBNDz35gECPR0GCBGADq13nB7dgYIMDkhHmf93iA0SVW76nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
طبیعت زیبای ترکمن صحرا، گلستان
#اخبار_گلستان
در فضای مجازی
👇
@AkhbareGolestan</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/682784" target="_blank">📅 14:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682783">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b81RmSTUvPe0zjnm_VSviqVzfAOOciazU76QYpqCuYxCEa2H07IZHc9HjdUfc8_6f-cr5q7caak28kn6iOmCUgALUSdY5jXBhiS4FN1TVUT-otJYbJO3OpZCWi9FfDlqwb9Iha6cuzrs0HY8LcgirDEYnUoGe3GN0kiRZeOcFBqEMT3HGtKYgbzj8gRrt3zpKgemGs9td5wBufqUb-e-VvYhnfpkhAjB64otMs-T_7cuMCaBble98l2rY7_1Ko55YJV6bTA8oZ7a5i6A2k4gL3x2u8Bc_2k4OQqa79HcwhoBZG0r23zpHe8sbvU8sLgRrDOz0U6kHjYTYFgaaSf6Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ست‌های رنگی خاص مخصوص آقایونیه که می‌تونن شهر رو زیباتر کنن
#فوری_استایل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/682783" target="_blank">📅 14:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682782">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
۷۶
هزار لیتر سوخت قاچاق در آب‌های شمال خلیج فارس کشف شد.
🔹
دفترچه سوالات آزمون گروه آزمایشی علوم تجربی منتشر شد.
🔹
دفتر نتانیاهو: اسرائیل با ورود نیروی بین‌المللی به غزه موافقت نکرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/682782" target="_blank">📅 13:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682781">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ec60087df.mp4?token=pLTVaDBMbEj9H_Jq6-V390vRwIcorkkCQ3ddICeCXm2UiOebs2sN3pJXPycbuLuB_b8qyCbBaRk_pbt0hQZ3VTDQaTTJYEuN-F4Vbp4snFZzzTPvgHI84dzQvtRhDfWwgKnq06lVwIikkzlK8zDV3EUFbT4uNUAh6miCNrIyBahvr_Uh2ic452UblQsx3PLBlASpIV3SuyGleqlgO9l6P3I3icxO3XmlLdc_cwtloJrBZCfMsYViiHtky6DHxY3lRJ99TkyFjUaRj0jcP_wM51LmUH13exFuCu8kBvGQ22mMVPulERZxcJb98RdLvEpwZlR9HqD5am71PhXuAPDpOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ec60087df.mp4?token=pLTVaDBMbEj9H_Jq6-V390vRwIcorkkCQ3ddICeCXm2UiOebs2sN3pJXPycbuLuB_b8qyCbBaRk_pbt0hQZ3VTDQaTTJYEuN-F4Vbp4snFZzzTPvgHI84dzQvtRhDfWwgKnq06lVwIikkzlK8zDV3EUFbT4uNUAh6miCNrIyBahvr_Uh2ic452UblQsx3PLBlASpIV3SuyGleqlgO9l6P3I3icxO3XmlLdc_cwtloJrBZCfMsYViiHtky6DHxY3lRJ99TkyFjUaRj0jcP_wM51LmUH13exFuCu8kBvGQ22mMVPulERZxcJb98RdLvEpwZlR9HqD5am71PhXuAPDpOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رانندگی خودران؛ بهتر از راننده انسانی؟
🔹
راننده یک خودروی مجهز به سیستم خودران می‌گوید این فناوری حتی بهتر از خودش رانندگی می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/682781" target="_blank">📅 13:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682780">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
ادعای مقام‌های آمریکایی درباره شکست مذاکرات ایران و عمان
ادعای سمافور به نقل از یک مقام آمریکایی و یک مقام کاخ سفید:
🔹
واشنگتن معتقد است مذاکرات ایران و عمان درباره تنگه هرمز چند هفته پیش شکست خورده است؛ احتمال وضع عوارض عبور از هرمز و شکل‌گیری مسیری جدا از مذاکرات ایران و آمریکا از عوامل نارضایتی ترامپ عنوان شده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/682780" target="_blank">📅 13:39 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682779">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSr4RCAsKqcrR-PaCFtorVwweap7BjgQ1QtMfQgesWGaAahMr_xmXFcBGAjnd8v9Ooel6amQo8O_wCtaAoF_bs0gKo8N3PRzWPw5n4MXegQTX8AuZh-5bxYBdkM8OVAqEBJgg9nWW56dSnS_D3O_S1mhNX7PzIa3hIMeM4cAlFG2dcvqiOzaGMVSQhCxMt2HhGVYrGfVgMmYIC8-cx6fTx5j7OUEttZHLyoORoJIn_8E1O6yP89Ba1igvmJhYf_ae7pLjo3Hf6tunniYxKeiAOrGgOfIIZymR_8AQIKB0SwwTW3_sYU544k7mZ9zgKHAr_hc9jPgwYNaMX994lk0YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر متفاوت از آزمون سراسری در دانشگاه امام صادق(ع)
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/682779" target="_blank">📅 13:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682778">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_5pzOIRJfGU_9X4C5yZj2k-A6pSM9rjjUuSHnqBiuQm_nGLosoaR0FsXuIgL5q-L-4rib3EUXTFdvxjohKIOjziqCnaMj-5IFRZliJIYql7mM94sG0_q-Hdox9zBhIFHSc2IAwaxiubF1Kc5PjPXTL0dnrz7cUdkF-7pM23FnScXZvyjX1x9yimQaiyg8JEeECYxseO--TbAv0M6hPpPsVStPUhH_sFGXmKv3aoF9ENVKWhHrXfC_2BXainrHpQb_OtPlRsPl_FA-2mlzymco6FtOs22n38RT-mRRqEeX3A4p9W2Rk9EGqUjumNIPj1fRHrhmGDA4VoKgZFPnpDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۲۹ مرداد ۱۴۰۵؛ ساعت ۱۳:۲۰
🔹
بازار طلا و سکه امروز با روند افزایشی آغاز شد و هر گرم طلای ۱۸ عیار وارد کانال ۱۹ میلیون و ۸۹۲ هزار تومان شد و سکه بهار آزادی نیز به سطح ۱۹۵ میلیون تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/682778" target="_blank">📅 13:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682777">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrzvUl1a4ypqVgDkIoVREgT7fkhNiHwuE3sZj2O0t4N05ReBDmWgU6b0gPeK4esjDaCfjHoygct7Hpq-IllyLfj9y4ZkgUwNY-BHHH6x1xtg99C3G2UIGTQDKY_zLypN0pkGWEc3kBUv863lP0aXRsmo7SFHVH00JoJXmLQ4OFd07UNNVKKFiSQCtRbJn63z0FuXK44TSNHY5rTnBkplFDkfL8oFc3eFqNyxISG6QkjlLhTnjx_g8jpXyLtUq9JQqYfIkvCVejrIAVvAcwIdMOJmI8yNDKHRYgqAeKq5HfCKFJCFcTPC6X0AAlYRP6Sg5z087sSM5a_YBCsxK_aYWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه امنیتی در نزدیکی سواحل یمن
🔹
این منابع عنوان کرده‌اند که قایق‌های کوچک به یک نفتکش در شرق مکلا در یمن نزدیک شده‌اند و نفتکش درخواست کمک کرده است.
🔹
سازمان عملیات تجارت دریایی بریتانیا هم اعلام کرد گزارشی از یک حادثه در ۱۳۶ مایلی شرق مکلا در یمن دریافت کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/682777" target="_blank">📅 13:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682776">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5e038ed65.mp4?token=t9kmUA-g6MkeIAotGRKJZnB2liDGn_Dgog63fp8D29Lpw7Ss9lVnK1qcZzAfvBD1V9OC-nsihW_8vq2Yg0-JPx0Fbm8dQMipVlrFuFNGbXqVHx7X9NGWEMM92vc9aDLm2zN0TnCXAJp_ius9iEg7R9Y_xO1toTbj5j-E4GjGMKQiKArfcBYDCp0cmDwLJyzGlzcV3o0u58aIikLJQeQcGBtQpXw5Ogu3NxEMZTB-w-Jn6htXIAwTQDXm7Ipu7sEuGTIJo90UwZNDoEY8rHkfNlpGELDedstWwBfXvtYLXn1ez6DzGY0CmpQ1RXN-AWbCSVBD1bbzpGOixI53Y7M_8Y6TH4DM9rGXvkSnMsOJPqmg7qG0Y6liqDOKcNcnjRXzmLl2NRh2ep9BkA-RcudnPfUCzsgAK6t5YfiZv_gaMYZahwoyTOH8CaNGgkLQv65WEbtJwfBHjwx1Lt8IFAiB1GLdZTg0M9c5NiBx4z1qflj0jCm6yEbh2nfm03npu_Z_5jKJbHFUb4jEHvf8qbs_VsPdtbW4CrODp61j2oEeZUPlWLw4S1tLzUg7wjsFSaOuxu-xOZCpuShXhCtlkLzvF3Q7vXxXuVm5jdJGbdwQl5cayhXBAFPns_13QIFyd5YcmPeW-v2XOXZuml3yH5ciDhPcnIfWZtzDV18pRqp50sU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5e038ed65.mp4?token=t9kmUA-g6MkeIAotGRKJZnB2liDGn_Dgog63fp8D29Lpw7Ss9lVnK1qcZzAfvBD1V9OC-nsihW_8vq2Yg0-JPx0Fbm8dQMipVlrFuFNGbXqVHx7X9NGWEMM92vc9aDLm2zN0TnCXAJp_ius9iEg7R9Y_xO1toTbj5j-E4GjGMKQiKArfcBYDCp0cmDwLJyzGlzcV3o0u58aIikLJQeQcGBtQpXw5Ogu3NxEMZTB-w-Jn6htXIAwTQDXm7Ipu7sEuGTIJo90UwZNDoEY8rHkfNlpGELDedstWwBfXvtYLXn1ez6DzGY0CmpQ1RXN-AWbCSVBD1bbzpGOixI53Y7M_8Y6TH4DM9rGXvkSnMsOJPqmg7qG0Y6liqDOKcNcnjRXzmLl2NRh2ep9BkA-RcudnPfUCzsgAK6t5YfiZv_gaMYZahwoyTOH8CaNGgkLQv65WEbtJwfBHjwx1Lt8IFAiB1GLdZTg0M9c5NiBx4z1qflj0jCm6yEbh2nfm03npu_Z_5jKJbHFUb4jEHvf8qbs_VsPdtbW4CrODp61j2oEeZUPlWLw4S1tLzUg7wjsFSaOuxu-xOZCpuShXhCtlkLzvF3Q7vXxXuVm5jdJGbdwQl5cayhXBAFPns_13QIFyd5YcmPeW-v2XOXZuml3yH5ciDhPcnIfWZtzDV18pRqp50sU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای تکان دهنده ربوده شدن السا فیروز‌آذر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/682776" target="_blank">📅 13:23 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682775">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7MLfO6Q8_qav0SrbCQZGlQ--Z8iglV-cymYi6ZPyjUVCP7xdwviNihmxe76lo_syBClwfD4c7jbKUcJowfgl9yEiCcRIVzsuGrMe1jyWZE5YupVLzgvVJ8XUVIpQQNpsy-NDsBHv_hn8FJAEClD2ZSwanLze1A7DKybfQ7uKVLs7iLm3byLFpGoXH8Do5DpEXximyDYrG2EIO8oKFX02GClonUww-ItgMV6UDx2pZb2Sue5dW8-wCyvSIDCm6UKM-ZETZE_5S6g7A_WUrGgcGjNy3IvxEnDXCXl_JDQOcnpcXuk9r-u2Wg7vZJ4s0MCP4Rcsr7mtNerXcEla8vL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت برنت به ۹۳.۷۸ دلار افزایش یافت
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/682775" target="_blank">📅 13:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682774">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2JEFvCiuzbjHU9MNn5ZvT_ZCBqbtyu1l2WKMzRE5RzOHgOhJiVilorHPkfWc6T9OwSG__mU17dfGYHSYdA54WIg4jcePzynYc1aLr9HztSqEBtFMiBBAQoZ9PgsEz6WaMWTtnPOPCne2qNbGZ1bJHnsrvUQEa6zgWhq588uPROPQ7Udk42mPm6RuAs4sbo3nHYSpbAU6qGPfZGRv-Ys_WSMwz4I0DUePHXKlrUHS6kwM1aWWLj1tUK8SjE8OzYu4kWFbhu48YIBdkZeWBg4EQCwPtRfyOH4BcakH_77DhHH1Jwb_WR6KUk47K-r3pzE-2390O4CFuxxlDRt_yDx_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/682774" target="_blank">📅 13:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682773">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uS6hd7zMK_eKVZybyLcC0rnlbe4K3ccQIUpUcDrwed6oAfsKEJwqZxejXrdUcQA7o7V0hO6tVC4AEVWE6Tx-3XTJmfM-7m9GZqlIJ0szb7fNWCM8X5rrfJ_IOs3WWpYp0nKu1Fe08s3AEgZUmPMOBeBx9g11SPmxesnL4VtaI0xXHrcZH7M2quNLG9F18O1pzhaL-cracK0Lk-A9DTUlNNv_MXO0jX5JtQcu7QzoslnI5pmRfViMuXVGSmyS40XRlM5kv3iUMnTKgCVE5qOwYMJdUnO7I-nSLK2Fuu4QAZbJM5dAZOBEsRcKbZPf8EZ9zaNOLxk6mHtHpu__JUR2jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت هر واحد بیت‌کوین به بیش از ۷۱هزار دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/682773" target="_blank">📅 13:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682772">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef0460a09.mp4?token=Zw82hAvY0pFtDFxywAVlT5ZMrRm0WuQnnl9Mg9P5I92OvPVGN57OTsVan_lAlpi2J44CgBXo3BSOKtF2R2FyKn7hZqOylZMddAb5zbRpt_vyXd1ycvlWsFMro_cqNANteqrgkCk6A4BGf_cAElahwpzzXBnE5n7_rfC5qiyXQgOcPszOnMAYKwiOlcE1FLt3U0ACx5Tta3aWPBB_7L3TtDNWl9GiBoTl5rx-lZjA-_cJlTN85yqiqwL0g71mFy7_i3TMxyxHhRF5k1ZqYD6EXavjj8J12AL1qmC76I2yjME4qrSQnJRoVr5u6cl5yoFy5y1lLQ2h8f3Uq1kSU9jUP2Zd4otOhzwrH7xzOYj0SiLa81CVL5z2l-tIe2vSMdjeaTZcagT1qBCxJ50WPr8OMqipHSvZ2cy_hx3NW1W8GiHu9KvUggnOVg4pe_xn7muogQCg1ehhqs-WKorn4RoIpdw7dBsrB_tHgRxQho6Aozkepcq53m6ZVOWMuVOfNDtfE5Yw8-1yNn0uHiChzOUFeSe1UTRb2QwcuKuKtkVltATXC37OoQjkbnP1lEraiTF4_i58kn6kBL2Yx_XWT60Q_J5Y_24FbOqjTR33QA1g0DnrdoPAXhpjFgd_zHBXjlvrX2S227566ef2UnbmAMikYrpJt8s6xW88f6c5VxQtjgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef0460a09.mp4?token=Zw82hAvY0pFtDFxywAVlT5ZMrRm0WuQnnl9Mg9P5I92OvPVGN57OTsVan_lAlpi2J44CgBXo3BSOKtF2R2FyKn7hZqOylZMddAb5zbRpt_vyXd1ycvlWsFMro_cqNANteqrgkCk6A4BGf_cAElahwpzzXBnE5n7_rfC5qiyXQgOcPszOnMAYKwiOlcE1FLt3U0ACx5Tta3aWPBB_7L3TtDNWl9GiBoTl5rx-lZjA-_cJlTN85yqiqwL0g71mFy7_i3TMxyxHhRF5k1ZqYD6EXavjj8J12AL1qmC76I2yjME4qrSQnJRoVr5u6cl5yoFy5y1lLQ2h8f3Uq1kSU9jUP2Zd4otOhzwrH7xzOYj0SiLa81CVL5z2l-tIe2vSMdjeaTZcagT1qBCxJ50WPr8OMqipHSvZ2cy_hx3NW1W8GiHu9KvUggnOVg4pe_xn7muogQCg1ehhqs-WKorn4RoIpdw7dBsrB_tHgRxQho6Aozkepcq53m6ZVOWMuVOfNDtfE5Yw8-1yNn0uHiChzOUFeSe1UTRb2QwcuKuKtkVltATXC37OoQjkbnP1lEraiTF4_i58kn6kBL2Yx_XWT60Q_J5Y_24FbOqjTR33QA1g0DnrdoPAXhpjFgd_zHBXjlvrX2S227566ef2UnbmAMikYrpJt8s6xW88f6c5VxQtjgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
داستان کنکور محمد بحرانی
🔹
محمد بحرانی از آن چهره‌هایی است که حضور و صدایش برای بسیاری از مخاطبان به‌تنهایی لذت‌بخش است؛ حتی فارغ از کیفیت نهایی کاری که ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/682772" target="_blank">📅 13:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682771">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aX6W_cIen2eUMYppAjE43TKqwytQh0XCT1rEhV3wmy6yEPEGMtT3cwwdb46sqrYhBEDim521hBaULtfP-wNXnpWyKx5LMyhtr93snNeDeclQijcR5QSCtwnSbtQoaSQmgrAa-dBBekboOoYpNdkNJv1q8gX063wflEpkKudtfm6rx1JESGVPyYNPdvm7uPw2x-k0SoI8Ek39tCnZifm3BRCKODubynJcTBycqM17tNTtNvdSghZCRHZ5ldBWvd-LJbeXQtIcBzyOx3ajjJ44UGIQZsvtNe674N1akSkfvOBiO3-ayW9tYQldXsK3dmuZDPYlHT2AbsXo0gExVhRkTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
دفینه در صدر صندوق‌های طلای بازار
🔰
صندوق طلای دفینه با ثبت بازدهی ۴.۴۲ درصدی ارزش خالص دارایی‌ها (NAV) در یک ماه، در صدر صندوق‌های طلای بازار قرار گرفت؛
عملکردی که با توجه به سابقه کوتاه فعالیت این صندوق، توجه‌ها را به روند عملکرد آن جلب کرده است.
📎
مشاهده خبر
🔘
روابط عمومی هلدینگ مالی و سرمایه‌گذاری سینا
🔘
🌐
سایت
📲
بله
📲
ایتا
📲
تلگرام</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/akhbarefori/682771" target="_blank">📅 13:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682770">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ccDN0Cu8XxqmcD6nF6NU_gnsofzm_LZk6OifgrKhaSI0GCr-FYhjb3vXC526M3DKScjCekvt1XbjZw-ObQc3RM5eHw6hppuzI9P_DxCyQfsUlTZxrI_PWMg2SIgJU3oCEfCwTwe-SzAicROKJjwzv_8JDnkYY4zXpj24o1bI2lqdVB3rxWnCnCGEhJtgOv3A-ntkqNJA6klHqdoJSDCFAcDTtMw2hfarUaFszBxmtRb06dohCEqdXEpH_i2M00yqrs7oT_EHwaA7BXE636_t6lTb0oLSHa70rBQPvoqMr9impFosMzq-xXHUotKetbIpBC0RWOI-XzZ1w3mwxtChbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
طلا در یک قدمی ۲۰ میلیون تومان
🔹
به‌روزرسانی قیمت طلا و سکه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/akhbarefori/682770" target="_blank">📅 12:56 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682769">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYoiyuFNAakDpw8WZ3hIZI9Z4xaqXbXhhjiZxxGU63DNjzNpIzQggqEaMbX7NsuOuU6gJOB3x_BTWDUk67l9HPX7tnWYKJ7yzSCmd0Jfmt_5loWeVXhkeT_zUkZ5ulC-xUibDHuCiUQQ20W9NYtMBSMgerYVBnvsGbQh-2g9aAoHSAkZuqw9EQVzXARhvyNWH2P8ymS5BQ2c14qj9zLHMEOJRwHVL8CF_gOwnURkwiwsSVpZzb6OZU3Geb9y5w0-IeE7adbw7v9pma0yYng8ggbZxk-yn-ToO82xrT1pYT2hqY_bhhu6WZQY9Cfp4NHTDGJ91aKIyK2UBFASEid1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیدبندی لیگ قهرمانان اروپا ۲۰۲۶/۲۰۲۷ مشخص شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/akhbarefori/682769" target="_blank">📅 12:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682768">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عمان: عبور امن از تنگه هرمز از امنیت منطقه جدایی ناپذیر است
.
🔹
چین: تشدید تحریم‌ها علیه ایران به حل مسئله کمک نمی‌کند.
🔹
روس‌اتم: به ساخت واحدهای جدید نیروگاه‌ هسته‌ای در ایران ادامه می‌دهیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/682768" target="_blank">📅 12:45 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682767">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec88211ffc.mp4?token=tAnzOhjk5jACAx9mKRPI4Vm7ZWw2_4tHR7jrRT7p7OVtFKMGWgjoXLKHeRdL1zonAvr8U-WYGGnrnWheihUZTXSyirQFq2S6IaFL7UvN-15EdPXzOOkkKmctgmo7y3VqeCNRYaeMWjXcqPbLTROPjUK5CaRE2K0UBbvFbygFb_fGvxddfB3hhW11A6vokxZHEZpqy4N4Hmy3qb7bVVcjyZnsLlKB87ZbHr_zgFkVXVqX9c-tk6v89Jqeenn2uSknQoJ_txsNBecTpJ0SLXQvC6VtBNqQqOqF4QRyLTMnkeYuJWr_yX_aQpmK_Ub-QXGB8SfweLRLgtJUAhFVCXVz8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec88211ffc.mp4?token=tAnzOhjk5jACAx9mKRPI4Vm7ZWw2_4tHR7jrRT7p7OVtFKMGWgjoXLKHeRdL1zonAvr8U-WYGGnrnWheihUZTXSyirQFq2S6IaFL7UvN-15EdPXzOOkkKmctgmo7y3VqeCNRYaeMWjXcqPbLTROPjUK5CaRE2K0UBbvFbygFb_fGvxddfB3hhW11A6vokxZHEZpqy4N4Hmy3qb7bVVcjyZnsLlKB87ZbHr_zgFkVXVqX9c-tk6v89Jqeenn2uSknQoJ_txsNBecTpJ0SLXQvC6VtBNqQqOqF4QRyLTMnkeYuJWr_yX_aQpmK_Ub-QXGB8SfweLRLgtJUAhFVCXVz8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
موش‌کور؛ نابینایی با یک «رادار لمسی»
🐭
🔹
موش‌کور تقریباً نابیناست، اما گیرنده‌های حسی بسیار حساس روی صورتش به آن کمک می‌کنند محیط و طعمه‌ها را شناسایی کند؛ این حیوان هنگام قرار گرفتن روی زمین نیز به‌سرعت خود را زیر خاک پنهان می‌کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/682767" target="_blank">📅 12:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682766">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=KZKLVvRIwIUPP18ozg2UyJfEVHX9qS4rz5hxh7SuFQXtoC2Av8C0EwIpQBG8dxpE9noEvnuegLSRzJI79DUpOfiM6NQwSQfvv3SHfASYBCxFb83Vcz9eMnU6u6ATKGyRlnASRxmZo3pplq8ZEYvgF3-rZlwRd7MR38lSPEZw1tgrdpWCllOIEqDRVJp3zkdgi4mxeHocrY9hKHD7LHmlrIeP0fmGDrPMSsTTD7H7vrdFA6Vu7OQHDcVTQY2o0PdsCEAjUcECJWi91nlHTB1fjvivj6UALfI3fmdnMTizZ--emo5wSV0TZHM8hjUVjx0k9h1RYDao9-H2KQvxOHwcWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546529e1b2.mp4?token=KZKLVvRIwIUPP18ozg2UyJfEVHX9qS4rz5hxh7SuFQXtoC2Av8C0EwIpQBG8dxpE9noEvnuegLSRzJI79DUpOfiM6NQwSQfvv3SHfASYBCxFb83Vcz9eMnU6u6ATKGyRlnASRxmZo3pplq8ZEYvgF3-rZlwRd7MR38lSPEZw1tgrdpWCllOIEqDRVJp3zkdgi4mxeHocrY9hKHD7LHmlrIeP0fmGDrPMSsTTD7H7vrdFA6Vu7OQHDcVTQY2o0PdsCEAjUcECJWi91nlHTB1fjvivj6UALfI3fmdnMTizZ--emo5wSV0TZHM8hjUVjx0k9h1RYDao9-H2KQvxOHwcWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سردبیر پیشین نشریۀ خلیج‌تایمز: کشورهای منطقۀ خلیج فارس از ترس موشک‌ها و پهپادها، به تعامل با ایران روی آورده‌اند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/akhbarefori/682766" target="_blank">📅 12:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682765">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJoa2J2W7fPbAjlbWClF32YbgxuzjQxYSFjAdJQovZxPKUDiV5jg2dLcywdrwYUyUg-yxLfsOmGaq6cDhqI5Ma3qVJdk9zsK0qdH9h5mhBciVrmHwf4kBiv4o_4sOq2p8TZFji639-Hat5BYmdiDWF1iGRpUMoiLH3ohkBEcFbVymPexTxqOjyGBw5Y0UY43TSlRi5FYNx7_ug4ZPyxF9_W7M-Q-gPY8dN_E1KYZqM8CApb0Z36AjwDct9Eowiitj255RU4l-_W8AJjbigX3Eoiybq9rLcsVpphNYrA63nZYci7N65iq-kHAepdBixhHn_NnNOfUNpYjPFx8Y278xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/682765" target="_blank">📅 12:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682764">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e2f7760b8.mp4?token=blGbn9C-GxmGVFeu5HwaDLpehi1ezg2jlBsr_RBnvQPxgaEiztAEYjRa1sy_PJZoJTgvDwGDRJJrxHvSxoI-PcyxvoyeOfhSIpEXwzKvJYGzVkDlgP9aXp56nzMoA8QN-NO1zT_580ueXzKqCTG61o97IVOtOEki5jeaX2wkUnJeNFYmsf5xfpCrfXQi9kGiK-9dGaLPPslIN4BKp-OoRCQPgjfVZO_lc1JFs9IrfKyFF0niiuBF-DGLyxuiblXIV1QWoG9XPhyJwg6O7NxeFzm6jhDyQbOuMgUH_v9pmmaUnJGjF5yrnqyQwImBVBBLpYP0DS0rVme8XcGHNY7iyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e2f7760b8.mp4?token=blGbn9C-GxmGVFeu5HwaDLpehi1ezg2jlBsr_RBnvQPxgaEiztAEYjRa1sy_PJZoJTgvDwGDRJJrxHvSxoI-PcyxvoyeOfhSIpEXwzKvJYGzVkDlgP9aXp56nzMoA8QN-NO1zT_580ueXzKqCTG61o97IVOtOEki5jeaX2wkUnJeNFYmsf5xfpCrfXQi9kGiK-9dGaLPPslIN4BKp-OoRCQPgjfVZO_lc1JFs9IrfKyFF0niiuBF-DGLyxuiblXIV1QWoG9XPhyJwg6O7NxeFzm6jhDyQbOuMgUH_v9pmmaUnJGjF5yrnqyQwImBVBBLpYP0DS0rVme8XcGHNY7iyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از زبان ‌علم بشنوید چرا بین خانم‌ها و اقایان این‌قدر تفاوت رفتاری وجود داره؟ #سلامت_روان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/682764" target="_blank">📅 12:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682763">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3XEaFqI4fhAECdMlUeeiWjozo-sOAfzo-1Q8Tj_DLhk2gT0en6eLYrRQqpqDzMx6wK8YOAz0GWzG3QIZw309RVTBFMqJEw7L_momW0cY-PlKeJDwAHBur2lI71VFVG_Y_MGDPQgKqX9tu7yiVVtiua9MasJ02hyPV5uS_5YXz1j5nqdkdBXi_0qZm41oB7Abt7ITOa8UX3ds0fanmhTAaq3aNh7BHjmqWyhA-GZCzEVQ0wRRcQybKNgVxCNsQUWWtR_m7QqWOQecTiWdL89Ui2CNSFmtWdLwv0P7kHUCqS86uQzgiBOnCzSUB4ASVorhFI7TajiupabLzGILczczw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۴۰ لغت کاربردی که اگر بلد باشی سطح زبانت B1 هست
✨
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/682763" target="_blank">📅 12:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682762">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2XeStgCsV0Wd14EgHqcP5CvmVwtuR6Po12FvBR3TnZ_a6fEn8hcGcyIX9LrO1WD4UBK1Kpt40ZzsS489tkXpGjXkRjFqODUZ2Qkpy8rBVCEFv20wrO_21vF9FUmdwDY7TK0SOLn8QhZ4_8jzdQ9Kl4V5qxAC6jbzmvLoOjzyjVPIyUHb0mJf4jDYeBdDI6crJLL5bQPDX-H5fdOnLuu4vQHoZf6CjgJ_fpXscuVNHcCnRspNj6lc25ArUylz1gC2iaot5epamSFaPEif8Wu3m3s27JHuXzGuBFoc9CJMq3b1f-UiPRnJjX_GLz00K8Ezi0dYH64vr8Q2WhMq1kenA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
تا 70% تخفیف در جشنواره mono!
👠
صندل، کفش، کیف، البسه، اکسسوری زنانه و مردانه
‼️
امکان استفاده از تخفیف بیشتر فقط در ۳ روز پایانی مرداد ماه:
💰
1000000 تومان تخفیف بیشتر با اسنپ پی در خرید آنلاین: PAYCVCCK
💰
500000 تومان تخفیف بیشتر با دیجی پی در خرید حضوری: DEAKJM
💳
پرداخت اقساطی با اسنپ پی در خرید آنلاین
💳
پرداخت اقساطی با اسنپ پی، دیجی پی و زرین پلاس در خرید حضوری(مشهد، اصفهان، شیراز، اردبیل، بابل، بابلسر، کلارآباد، زاهدان)
‌
🆔
@monofashion_co
🌐
www.mono-fashion.com</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/682762" target="_blank">📅 12:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682761">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=d9pX6wRe_FLsyS1uBeAqMfiLExiVUV7spSWFi-EurnL_4iz_Cfz2TpZ2b7zZy8jAwo9PxHc7TSu01FIyBcDmaOlGfM25SIBgqgU1LNUvWtq0Ph8r67_YRU_hq_p07Pt2sFwjhc-GO6KnIshopU5CTZTdTtQ_ty6QFohJkXT91uW0lv_xcTS1ml2kaM5wNp5UJd92bE-IO5KMK92jiK2l44YvZRTEJwvn9HUZqOXMIPxYfwf074P3c1Q_UV8UkFwENnQS-eCr4HP_K6SHISdIoiOdOZ2loEbKln5P5L1p2dKDfyKYNSb5ZvtD0SDYPjSZfJF4qO0m9YYQHle9kUNCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf1830b1bd.mp4?token=d9pX6wRe_FLsyS1uBeAqMfiLExiVUV7spSWFi-EurnL_4iz_Cfz2TpZ2b7zZy8jAwo9PxHc7TSu01FIyBcDmaOlGfM25SIBgqgU1LNUvWtq0Ph8r67_YRU_hq_p07Pt2sFwjhc-GO6KnIshopU5CTZTdTtQ_ty6QFohJkXT91uW0lv_xcTS1ml2kaM5wNp5UJd92bE-IO5KMK92jiK2l44YvZRTEJwvn9HUZqOXMIPxYfwf074P3c1Q_UV8UkFwENnQS-eCr4HP_K6SHISdIoiOdOZ2loEbKln5P5L1p2dKDfyKYNSb5ZvtD0SDYPjSZfJF4qO0m9YYQHle9kUNCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسین پاک، کارشناس حوزهٔ مقاومت: اهمیت اصلی علی‌الطاهر لبنان، علاوه‌بر موقعیت جغرافیایی، به تأسیسات استراتژیک آن برمی‌گردد/ در میدان نظامی درگیری‌ها لحظه‌ای ادامه دارد و حزب‌الله همچنان با تمام توان درحال مقابله با دشمن صهیونیستی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/682761" target="_blank">📅 11:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682760">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf4e744901.mp4?token=JH1fOn4fZdcZxBn_6yGWFHiXA4wJpjsQeKnE3NtY_AhJ9589LLFab0NGDlg8W5G-fopgAqelGC_BaYprNsoAbuchPKypwPkKba9c6xVDDNd3OWuNez1OC51Z680BjPEbVokVE3IY12BnqB-UR8uFYTaAkBA8VhoHSiluRi0JZs71Pq50LCa3_539eCSzI5O3_z_dqqgecF_UpVDJ5esyQHuogFPy4hPw9P3WPqreViKoGVo1QQv5c34vhTl0OAwlsdQir39oqmiqQPE9IpxbyDPUHEq42g4229YoKb6ExbWl-xjxww3-TJwDmB11QprlhuEH-wjkaFFvtSPT22EFxxPdP3T0azfpSIVpB4p16JpL7z3F-0iVgmcsinjZIRUXl11Ek7UVPG2IB03vBiHdwPHd7JSXzYI2g0jwEa-xMeeg-9QoS1RR1S7DEZ8j0UTRf3-r86KI88TDUBHBgBQlKLfIxAeNXF1j8i1EPKLcBic0duGHcIOLwn69nBa1B3qtjfKkhfK_uAzyt5pgufzvKnyf8xJ9h_gvfHPzny4Ux2ATTH2ZS0_el6tBt262TfPWyaLhy7vqYKziSyJyuILrr_EFSQ2q_s53ruWpU9DcG3JS3-AM8n8gqgXTucI9Up7-RhPmCc1fjawIwk5acpdGY7MsTVu45uJVg7ImvIl2X7E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf4e744901.mp4?token=JH1fOn4fZdcZxBn_6yGWFHiXA4wJpjsQeKnE3NtY_AhJ9589LLFab0NGDlg8W5G-fopgAqelGC_BaYprNsoAbuchPKypwPkKba9c6xVDDNd3OWuNez1OC51Z680BjPEbVokVE3IY12BnqB-UR8uFYTaAkBA8VhoHSiluRi0JZs71Pq50LCa3_539eCSzI5O3_z_dqqgecF_UpVDJ5esyQHuogFPy4hPw9P3WPqreViKoGVo1QQv5c34vhTl0OAwlsdQir39oqmiqQPE9IpxbyDPUHEq42g4229YoKb6ExbWl-xjxww3-TJwDmB11QprlhuEH-wjkaFFvtSPT22EFxxPdP3T0azfpSIVpB4p16JpL7z3F-0iVgmcsinjZIRUXl11Ek7UVPG2IB03vBiHdwPHd7JSXzYI2g0jwEa-xMeeg-9QoS1RR1S7DEZ8j0UTRf3-r86KI88TDUBHBgBQlKLfIxAeNXF1j8i1EPKLcBic0duGHcIOLwn69nBa1B3qtjfKkhfK_uAzyt5pgufzvKnyf8xJ9h_gvfHPzny4Ux2ATTH2ZS0_el6tBt262TfPWyaLhy7vqYKziSyJyuILrr_EFSQ2q_s53ruWpU9DcG3JS3-AM8n8gqgXTucI9Up7-RhPmCc1fjawIwk5acpdGY7MsTVu45uJVg7ImvIl2X7E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چین در سال ۱۹۱۷
🔹
فیلمی تاریخی از چین که در سال ۱۹۱۷ میلادی ضبط شده و تصویری از این کشور در بیش از یک قرن پیش ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/682760" target="_blank">📅 11:54 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682758">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
ادعای «الحدث» به نقل از منابع آگاه: ترامپ دستور داده است مذاکرات با ایران برای چند هفته متوقف شود و احتمال تمدید این توقف نیز وجود دارد/ انتخاب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/682758" target="_blank">📅 11:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682757">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
ترس از ایران، بازی اسرائیل در عربستان را لغو کرد
🔹
مسابقات «جام ملت‌های ورزش‌های الکترونیکی» که قرار بود در ریاض برگزار شود، به‌دلیل شرایط امنیتی منطقه تا سال ۲۰۲۷ به تعویق افتاد.
🔹
این تصمیم در حالی گرفته شد که قرار بود اسرائیل برای نخستین‌بار تیمی را به یک رویداد ورزشی در عربستان اعزام کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/682757" target="_blank">📅 11:35 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682756">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe6b7f22ee.mp4?token=NzgyUQ0nx0hppyltYoDPwBOAvW5Xiw0eDjOcllMAgVG5hz5mHCCRjsQWr6nfhlSVglDNNT2uXmg2LO1_Bv7Z2OY1rtjV7GhaBQWC--Ahx6vy9exPp2S9dvqnP5BKKMemc090KshTj-RJO2eKV0CFFAmWWG_ZfvHNUYTjtGTbW1GX2pqD0M_UKKkkDbmjJ3ScTnTwR45sWKqyMLu4GAnS2Z1KZMgtNlZEDVAY5pkVBaftniQVTnM1HKLcP2ZhRD4K7KwOHl5eoIE46IpWIRuw75gHTT1EyMNEDApbTG2tnGNAQ3U3fRrRTzQs_OfcxxNOccg-_l1uDywKTub88jQEnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe6b7f22ee.mp4?token=NzgyUQ0nx0hppyltYoDPwBOAvW5Xiw0eDjOcllMAgVG5hz5mHCCRjsQWr6nfhlSVglDNNT2uXmg2LO1_Bv7Z2OY1rtjV7GhaBQWC--Ahx6vy9exPp2S9dvqnP5BKKMemc090KshTj-RJO2eKV0CFFAmWWG_ZfvHNUYTjtGTbW1GX2pqD0M_UKKkkDbmjJ3ScTnTwR45sWKqyMLu4GAnS2Z1KZMgtNlZEDVAY5pkVBaftniQVTnM1HKLcP2ZhRD4K7KwOHl5eoIE46IpWIRuw75gHTT1EyMNEDApbTG2tnGNAQ3U3fRrRTzQs_OfcxxNOccg-_l1uDywKTub88jQEnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر شیشه عسل، حاصل میلیون‌ها گل
🐝
🌸
🔹
هر زنبور در طول عمرش حدود یک قاشق غذاخوری عسل تولید می‌کند؛ برای تهیه یک شیشه ۲۸۰ گرمی، حدود ۶۸۳ زنبور روی بیش از ۱.۱ میلیون گل می‌نشینند و مجموعاً حدود ۵۲ هزار کیلومتر پرواز می‌کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/682756" target="_blank">📅 11:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682755">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/597578ac3e.mp4?token=FTqG4-VOLxihAaXXyDqlMUuesecVKLPOwjZWspXCw71JaYhbI1v8SLP_4uf_XNBOxSfmi4-pGzlSK92alr8IDNyZORrgSG6_KPJJcpC0UVG-JJyzYORAmG_8G1mM8bqCbuGwub3myNYKMDZeg6PGmln8dcfdDBXOaLndx1QMbb7UJLMpiiZQey_iE05PiMbQBOkDs19Zy6skdp_aZN8D8XGuOCD_YCdTU1k-x-XK7gGRAOJPVIyLW5xC86N5xtip9MwYqedjzJxRtMe07QQYsYWxNd8yEgiGAMHDSfZlF-DDCDY8PNSm2vGBsFim9LTx15IE2IXFiUHF6KNH3Gdamw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/597578ac3e.mp4?token=FTqG4-VOLxihAaXXyDqlMUuesecVKLPOwjZWspXCw71JaYhbI1v8SLP_4uf_XNBOxSfmi4-pGzlSK92alr8IDNyZORrgSG6_KPJJcpC0UVG-JJyzYORAmG_8G1mM8bqCbuGwub3myNYKMDZeg6PGmln8dcfdDBXOaLndx1QMbb7UJLMpiiZQey_iE05PiMbQBOkDs19Zy6skdp_aZN8D8XGuOCD_YCdTU1k-x-XK7gGRAOJPVIyLW5xC86N5xtip9MwYqedjzJxRtMe07QQYsYWxNd8yEgiGAMHDSfZlF-DDCDY8PNSm2vGBsFim9LTx15IE2IXFiUHF6KNH3Gdamw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دود غلیظ جنوب تهران ناشی از آتش‌سوزی ۲ تانکر بود
روابط عمومی پالایشگاه تهران:
🔹
حادثه برای دو تانکر هنگام بارگیری نفت سفید رخ داده و آتش‌سوزی در کوتاه‌ترین زمان مهار شده است؛ این حادثه یک مصدوم سطحی داشت و تلفات جانی نداشت.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/682755" target="_blank">📅 11:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682754">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
بدهی عمومی آمریکا برای نخستین بار در تاریخ رسماً از مرز ۴۰ تریلیون دلار گذشت!
🔹
داده‌های وزارت خزانه‌داری آمریکا نشان می‌دهد که رقم بدهی داخلی دولت این کشور از زمان دوره اول ریاست جمهوری «دونالد ترامپ» در سال ۲۰۱۷، دو برابر شده است.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/682754" target="_blank">📅 11:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682753">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
اجاره در مناطق لوکس تهران؛ ماهی معادل ۲۰۰ میلیون تومان
🔹
براساس قیمت‌های پیشنهادی موجران، مستأجران برای اجاره آپارتمان‌های ۱۰ تا ۲۵ سال ساخت در مناطق گران‌قیمت تهران، به‌طور میانگین باید حدود ۴ میلیارد تومان ودیعه و ماهانه ۷۸ میلیون تومان اجاره پرداخت کنند.
🔹
با تبدیل ودیعه به اجاره، هزینه کل سکونت در چنین واحدهایی به حدود ۲۰۰ میلیون تومان در ماه می‌رسد؛ رقمی که فاصله بازار مسکن لوکس با توان مالی بخش بزرگی از خانوارها را بیش از پیش نشان می‌دهد.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/682753" target="_blank">📅 11:17 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682752">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
عضو کمیسیون امنیت ملی: بهترین واکنش به تشدید جنگ اقتصادی توسط ترامپ، خروج از پیمان منع گسترش سلاح‌های هسته‌ای (NPT) است.
🔹
تکذیب حمله به دادگستری بهبهان؛ فیلم منتشر‌ شده‌ قدیمی است.
🔹
وزیر دفاع کره جنوبی: برآورد سئول از زرادخانه اتمی کره شمالی بین ۸۰ تا ۱۲۰ کلاهک است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/682752" target="_blank">📅 11:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682751">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apbdh9HOwDg5tygzl10U6ufYh-rP6W3yElIP1ktsVLXJ1z6YgisO_RTu03cj14j6FMbwXjXKI5ztbymknOGTg-OtS6y3jleeC8mUyCRpEt_5nRxR9mZLEthhpbDID3uVy-4jxLGRAxkYboYGr1BePaHsiDAiWUnanPNQmhCirbDwnpa8sg_tZ_I-7NYL0lPWYkWPUJATyZF-mE-ihhYzgXQzuGUzazRTElMcfsEFDJiimfvSbEQmZARKfJyLUTQfuefa57WF7ajUQIngIcXIW_AjoplSNG1P-RcsWpp58f-AjtkNA8tH0cmQPUEyPpWp0sfyJoWB1NU6ksGRhwjZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682751" target="_blank">📅 10:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682750">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAth-MXOnQ4hyy2mk7D9zGt8CgESjmjzJUA3nLV3VrkupROxVTXKXWwuNCGjkgefszcDK3b7wO1IuYRX-k-O-nNJGB7IZqqmxqUzyHJeiBBYmJXenJH1Knv6C1MD_V5w4HHSSi_oGU3Fi9HX15VxY7f7Ib67w3LslqVXSbFuD_oaaLfW-1pjFtmp9YIMuw56kxQBqEJ3XnpPNPANsIZmVgK2ePQuW8_5YDdBIPAW0WLtEj1O2A2wQ3HviuehwEjOn_l_vOY_--tsv_tYn6Iw2vQZnckglcnlNZmB7nikR9ZSVGaxlezFvZXxu_ecjZn1Fq6k0dHovuQSgXODpBGxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی تماشایی از خلیج گواتر، سیستان و بلوچستان
🇮🇷
#ایران_زیبا
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@akhbar_sob</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682750" target="_blank">📅 10:51 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682749">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ede4a3da96.mp4?token=Z6z5HNs8EkJRLV9m3zYpbKVDx4E-tpwgha4ROZJGzYvrDjClCZb4ggwZ9UIq4NDA-pfIesRd_FBB7WkGCmkNQGkYh0wDVqlYD2Md8rMqlBcRH9D8aJrNfD5x5kO7As6iazd5T4EKyWZV-jnV7OC_3Wu5eLqOYixYZsOEWfvy4cuTzLeBV15YtT0xEGx915JLc9gQ1MLwPjP0qvuXfBiSyiPh-GXj2mED0evYVNkwR9COcbDcQGxIDXtulkSWYXCkzotWWiDP4gtr44PvBg4NN24Tnxtb_wAKe_-SKtvfFBYruZXDWWkMXq4B5NuIFtlhMrJf4917C0cOLKoqsMpsAWZ5_yNoRA6QDT2AmKILqz9ENE9fxm6eJS_lRVwE3xKKHDJMFORWMaAw3N9WH5hAOm_CdeVopqzy5cnQ0d-y48mSDS4DySnZKjk3atoAtL7dhPjsvkxVa9e_bv9A6zozGnQhDJaa7pq7XbE2fKibUJN6yfuYpSYaVtDheoyuaT_wcQaFGTfXUuak8uthrrOPbm1r9YrMtoi3Bs223QGNsSGDn8wLk5Bq967CAg0XWihFxnCyanWKob-S94wVkTbDRCLyV8XnpKr3OzJt2FkSSgrW_4jGVEspHtYcrFiv5gJu-3NGeA4RTF6OxCsWmTDXdLypan-uUFj6YNIlOTs7Yjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ede4a3da96.mp4?token=Z6z5HNs8EkJRLV9m3zYpbKVDx4E-tpwgha4ROZJGzYvrDjClCZb4ggwZ9UIq4NDA-pfIesRd_FBB7WkGCmkNQGkYh0wDVqlYD2Md8rMqlBcRH9D8aJrNfD5x5kO7As6iazd5T4EKyWZV-jnV7OC_3Wu5eLqOYixYZsOEWfvy4cuTzLeBV15YtT0xEGx915JLc9gQ1MLwPjP0qvuXfBiSyiPh-GXj2mED0evYVNkwR9COcbDcQGxIDXtulkSWYXCkzotWWiDP4gtr44PvBg4NN24Tnxtb_wAKe_-SKtvfFBYruZXDWWkMXq4B5NuIFtlhMrJf4917C0cOLKoqsMpsAWZ5_yNoRA6QDT2AmKILqz9ENE9fxm6eJS_lRVwE3xKKHDJMFORWMaAw3N9WH5hAOm_CdeVopqzy5cnQ0d-y48mSDS4DySnZKjk3atoAtL7dhPjsvkxVa9e_bv9A6zozGnQhDJaa7pq7XbE2fKibUJN6yfuYpSYaVtDheoyuaT_wcQaFGTfXUuak8uthrrOPbm1r9YrMtoi3Bs223QGNsSGDn8wLk5Bq967CAg0XWihFxnCyanWKob-S94wVkTbDRCLyV8XnpKr3OzJt2FkSSgrW_4jGVEspHtYcrFiv5gJu-3NGeA4RTF6OxCsWmTDXdLypan-uUFj6YNIlOTs7Yjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
به نظرتون چرا امروز یه روز خاص هست
⁉️
🔹
چرا امروز همه باید حواسمون به مصرف برق باشه
⁉️
🔹
چرا امروز چند ساعت بیشتر از روزای دیگه مصرف برق رو مدیرت کنیم ؟
🤝
همدلی امروز ما
✍
آرامش فردای فرزندان عزیزمون رو رقم میزنه
برای آینده آنها، امروز با آنها همدلی کنیم.
❤️
قرارمون همدلیه
🫶
📚
#کنکور
♥️
#قرار_همدلی
⚡️
#مدیریت_مصرف_برق
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/682749" target="_blank">📅 10:49 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682747">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/682747" target="_blank">📅 10:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682745">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b404884170.mp4?token=EnMT2hlRbyT3zRCcVqxPrE4CRiBrbfCIK2fxIi3Lj2-IOgm-yyAyxpkC768g0G22Q_sLvzsjc5CNwAZwwAj3XyPsmwzWxdJf_I_5L2oHl7YugKGwPrvTDpd20ldPRrMbbwXBYtoFLh4Gz6KQNnecwKcaL87K1QINIe1cMFQZjBH3QFsjmCHFd1wVin6_r5m-cskI1wkftom25zoYWUifFE6igirmERRgTsjFTHVZRFN0Ws4XNSgCTiElMdi4YA4X-o3NOf4iXsUqo7DSVLOmUhmzfdrA2AL3B9CsyyHlOQVCMjJZnZQUPP1vZq6Y-nNzkMfWc80tKHSVz0FKhqy1ApZEAj1LJdYHJF2KxaI52stUSPNTmmCDFjZp3b3tMs2gINy6qpcxSnyGpz2HdfDflrVs2UAmJeBGsHN_vGuBLmiVZvc8HRA8n1Lbq5N397CFrjrv0q69D7za3PaaZPNyCE9Qdl94R4mV21PG4YzUWl_bZwvopJl7hBguzqy8RqSPWXfTdfJYhYzWGgYLXQnPJSeJo3pRTLsm9Nz88i5FaFf_kRImW6SeDVvYLb955B_22NhZ6Bmt_r6Bu96Cdno0dueqw4QuW0PysU02cA2TiPj39iyw_llbM1skoDgf36avkfhFitOmpcVQnXHmj21azZ7pLFBGdrj6g--BPupXR1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b404884170.mp4?token=EnMT2hlRbyT3zRCcVqxPrE4CRiBrbfCIK2fxIi3Lj2-IOgm-yyAyxpkC768g0G22Q_sLvzsjc5CNwAZwwAj3XyPsmwzWxdJf_I_5L2oHl7YugKGwPrvTDpd20ldPRrMbbwXBYtoFLh4Gz6KQNnecwKcaL87K1QINIe1cMFQZjBH3QFsjmCHFd1wVin6_r5m-cskI1wkftom25zoYWUifFE6igirmERRgTsjFTHVZRFN0Ws4XNSgCTiElMdi4YA4X-o3NOf4iXsUqo7DSVLOmUhmzfdrA2AL3B9CsyyHlOQVCMjJZnZQUPP1vZq6Y-nNzkMfWc80tKHSVz0FKhqy1ApZEAj1LJdYHJF2KxaI52stUSPNTmmCDFjZp3b3tMs2gINy6qpcxSnyGpz2HdfDflrVs2UAmJeBGsHN_vGuBLmiVZvc8HRA8n1Lbq5N397CFrjrv0q69D7za3PaaZPNyCE9Qdl94R4mV21PG4YzUWl_bZwvopJl7hBguzqy8RqSPWXfTdfJYhYzWGgYLXQnPJSeJo3pRTLsm9Nz88i5FaFf_kRImW6SeDVvYLb955B_22NhZ6Bmt_r6Bu96Cdno0dueqw4QuW0PysU02cA2TiPj39iyw_llbM1skoDgf36avkfhFitOmpcVQnXHmj21azZ7pLFBGdrj6g--BPupXR1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درمان غیرتهاجمی لرزش پارکینسون با اولتراسوند
🧠
🔹
یک بیمار ۷۲ ساله مبتلا به پارکینسون پس از سال‌ها لرزش شدید، با روش اولتراسوند متمرکز و بدون باز کردن جمجمه، در چند دقیقه بهبود چشمگیری پیدا کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/682745" target="_blank">📅 10:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682744">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
سخنگوی سپاه: با وقوع جنگ جدید، تسلیحات مخرب‌تری به کار می‌گیریم
سردار محبی:
🔹
قدرت تخریب سر‌های جنگی به‌کار رفته در موشک‌های سپاه بسیار فراتر از نمونه‌های استفاده‌ شده در جنگ‌های پیشین است و اگر جنگی آغاز شود، تسلیحات ما در تمامی ابعاد با گذشته کاملاً متفاوت خواهد بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/682744" target="_blank">📅 10:26 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682743">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c23aGKpAJ0lshfmNpDRHN1SrWntX4w8uYepWPFDLwGVdCraNxQNKQnk4yBaa6Mt1NoHYnE3ln2ZcaEHBL34jYg-RzFyd6FdGm7BQw2Wj4qRyiDruK9FF3B81MzIWKHyqbCq72imheAH6gDXG0ItGwRZktfhgz18WcbwvyPy2qFRkjJge6epLPb1Dx3Y93liO7Ts0oDdIt-OopxAu2qvO5UvMTHedcCDJtysvlVAnLWYvy4XpFh1ikQ37eg6mIggZJ-297W6CjULzaRab3A2kQSemQkoeC6bHqG4RJuUGF4uPp7DUsPLRvWy9oD10Xh_EML464zUW42S_2LZ-OsAz7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/682743" target="_blank">📅 10:22 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682742">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
نتایج نهایی کنکور و آزمون پذیرش دانشجو معلم نیمه دوم آبان اعلام می‌شود.
🔹
قالیباف با مشاور امنیت ملی عراق دیدار و گفتگو کرد.
🔹
سپاه اصفهان: امروز صدای انفجار در محدوده جنوب این شهر شنیده می‌شود.
🔹
وزیر جنگ رژیم صهیونیستی: اردوغان ترکیه را به ماجراجویی‌های خطرناک در سوریه می‌کشاند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/682742" target="_blank">📅 10:19 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682741">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9NWij8E4KuWTSPUhYFWwHuQSDNNNF8sy5lYQ8m37OBo7dh4FHgEvFEMnl68WHxdn3IKb0BZ8ODTgA7zgr4UuLZMPUhce8hTBNsJGrix43mZTeq6uuSQbODI05tGWxR0FxpV13sE1ZWxRZwAQD21uEzJseb82WLJ2WkGAF7PdUbXQiPIhYgkIyCTDJX5N7QX2GRz9dBomchNv9gYrFh1eG7Tg-XWfbPsQkfu21XtwckqSRetDHyoQ1WQnlFFXeLYstsff6AYkZRDvRjRW9L16EFTdOjKp6_OXuLj6Vc3s0vHR_mQMF1rxTSH0nyaur6ubdf9268WADQs2gGfC4-HRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند
🔹
آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/akhbarefori/682741" target="_blank">📅 10:12 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682740">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ffdc10f45.mp4?token=uUl6p_XRXKa1hHRtnP6lOlmXv90pZZ5ky8Lqs2d5Qo0SzqYsbei2BwDmrcktgtrGGmUGY6CBj8tgC49PeLcWt8i5CuncbsnyjyJX5e4PfxtLMCKPiKyBMbH_IROkVXzjvVB9S8Dwhq13AAiKGxumXSG1bZJ-17bbEpRwQgU6v_Hf-t4NrulpXa3ovLsT7MZtB5NB75u1pcH5w3mX1boBf_KPvc3I1VjTqo0vkfP6eL3WpSNdRo1Iip4GsgNITZEKuuc6TwCzhQVeNkOCeGbzBeeJEL1rHykD310_F0hRihs0diPMnSmSoijffNZwZZJ721nh5ckh1luFPAdRgpqtCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ffdc10f45.mp4?token=uUl6p_XRXKa1hHRtnP6lOlmXv90pZZ5ky8Lqs2d5Qo0SzqYsbei2BwDmrcktgtrGGmUGY6CBj8tgC49PeLcWt8i5CuncbsnyjyJX5e4PfxtLMCKPiKyBMbH_IROkVXzjvVB9S8Dwhq13AAiKGxumXSG1bZJ-17bbEpRwQgU6v_Hf-t4NrulpXa3ovLsT7MZtB5NB75u1pcH5w3mX1boBf_KPvc3I1VjTqo0vkfP6eL3WpSNdRo1Iip4GsgNITZEKuuc6TwCzhQVeNkOCeGbzBeeJEL1rHykD310_F0hRihs0diPMnSmSoijffNZwZZJ721nh5ckh1luFPAdRgpqtCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بیاین با عطر این دمپختک باقالی بریم به خونه مامان‌بزرگ‌هامون
😍
مواد لازم:
🔹
۲ پیمانه برنج ساده
🔹
۱ پیمانه برنج دودی
🔹
دو پیمانه باقالی زرد
🔹
۱۰۰ گرم کره
🔹
۲ قاشق روغن مایع
🔹
۲ قاشق پیاز سرخ شده
🔹
نمک فلفل زردچوبه
🔹
۲ پیمانه آب قلم
🔹
۴ پیمانه آب آشامیدنی #آشپزی
🇮🇷
…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/682740" target="_blank">📅 10:04 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682737">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mIY5l6_q6ceCTgi6qh_dKMB0vgxdnl2m-wKCgLNLMfCdwJunF7FIdQYKRLN8-_7bJX2gH4KDX_LYmQMw36K0_8YRwsOZlPhB-fwgGKXJrTho0N8WZMHt82XMulBe6yqHiUkZmcjXYv4S6ZpswgSfo9fUsAKaVtEn_x2P3gvAGVhVFrxfBDzhIq9-19I0q2g1Qo560f1YDXyiADm5Qf4YOhHuLBTQUkN7jrMtMRno-fchUnOFnLailNxCJGaMWbxG1mer3oABZzFtQNuqLCXW4anNHCi8l91UZIhBiqZCR7fPP3ZKC9wu7fDIS0w9xA8i4soQS4cuLrWKiE_4ZIHmFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۱۵ گیاه که می‌توانید از یک برگ تکثیر کنید
🌿
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/682737" target="_blank">📅 09:46 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682736">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xji5Fb-YqzSSzI66fYOZab60RW5LSKPK9qdG-XaMheQXF1mXjkG2fLYGv8B05RXkxveaPpbqd78-Vft596cW9SCucfYn-WsRhcru-oYwlgl3jIiJY81hrUQVth-047Tuz2CpLf_NQPht3RRx3yqAQ7zcHK4X86gjntyLBsFT37RV1HyUth1ZVg6CRm04wUX1GC3jQ5qyg_RMJvUViTbTYLLOytdr3R9U3C-YWbDYqteAtyMXuDVrQg7GdUTrvTrbziwjZovbixUTBjhFKhdKTX-HecwCIlakGdoVL-_3MEl8vVIBPJl39PUEhLHEw4dUVCdlbDrcYpFV8ZtkgrcqDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد  رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز…</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/682736" target="_blank">📅 09:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682735">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1IDDbLLPr-G3DKuhQvLZt3FvA9ndCsZRFPhMsyfNEGt-oZzGnZdjhXa9T8cuXDt-hMhV9jA4cJyqH1yvVSHIpc-IXTJR_C8l535aaOm2qVG-n2yuEKf4ww0TGyAttGtgB5nPQKZYss_8E4w_QwmRf7S7OUDTKnRH5w6OPEqdNSjHygkh9yrDHhFjCqIMrL3Wyy5JjZsVGGEa-RF_FV8cM1-TCF7OB6VIsiHGIp91F9AlVF9Wenbrd0OC_xLVyvJUrGOy2YGVutT6CR1krlSkyYW1LLiadhsfOj-SaBNoFN59_vjM2x-LLseDfwEWsq6xH01PCGKSd79-iKkWz7Ktg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در جهان ۲۶ درخت وجود دارند که عمرشان بیش از میلاد مسیح است؛ یکی از این درختان سرو ابرکوه یزد با قدمت ۴ هزار سال است
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/682735" target="_blank">📅 09:36 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682734">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cd9558ed7.mp4?token=uKu-TttrGM2OojXDuNh2p49q-XIq5kA_RKApqV6pDu_aUinFlstXxUo6xPKChC31AfUql55BJ-NGmIKV4LkBnywelgUaoVZkhkWNH8FCF-k4AZkzGgl2knSNYcslBKjqpci3Pbf3CLlQHGFgbZt6PuKCSjErG-ZZNs3YOU9CAW3v3Hh1ZM8gYo2tpSfmmokRoVUVOeudZ2jS-y_1qNxFcQhwsTkXooi7kL6nTJQFGeDDVtQJGbW8Q8bLz8K-qhfpKb_A7F381JXayuzOBegVwnuVn9WY8I_KSDw9mU6--anC3_qdClz4kuxB87lQghSmxpwZdd9zvtSMv24chAUEbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cd9558ed7.mp4?token=uKu-TttrGM2OojXDuNh2p49q-XIq5kA_RKApqV6pDu_aUinFlstXxUo6xPKChC31AfUql55BJ-NGmIKV4LkBnywelgUaoVZkhkWNH8FCF-k4AZkzGgl2knSNYcslBKjqpci3Pbf3CLlQHGFgbZt6PuKCSjErG-ZZNs3YOU9CAW3v3Hh1ZM8gYo2tpSfmmokRoVUVOeudZ2jS-y_1qNxFcQhwsTkXooi7kL6nTJQFGeDDVtQJGbW8Q8bLz8K-qhfpKb_A7F381JXayuzOBegVwnuVn9WY8I_KSDw9mU6--anC3_qdClz4kuxB87lQghSmxpwZdd9zvtSMv24chAUEbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا ملوانان ناو آمریکایی خودکشی می‌کنند؟
🔹
وضعیت بحرانی ناو آمریکایی پس از ماه‌ها حضور در جنگ با ایران که اخیرا مجبور شدن بهش پایان ماموریت بدن!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/682734" target="_blank">📅 09:30 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682733">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lUPPSzH9yuin69oX4AKBlj8RB-3ZqBIes-7g40CRgW3mHtp-KAy5WRBBCCdv4Dw0lcJDdFgWVuSIvAgRiXlamWd04en7SZ1k2_OHcc3Gh6wI5b4sduGqM81LQHbKy0R_CX7dxUOJ20ivGd6FlniVfSVCDs7ux9_UzQNhx6_cZi4qCUnT2FD-fpLvyZvdEYuYXPXuBOxUlt_Y7TWBo6-0tUAdVAw418rHA6yJsE4HoxzEVLHybx28OcaAshmYEAibUDy_4Q7Pzb6-sW-aC_92tFpCNAj7gfiMLQ8260x3yIF50FgVnaZ0ED2T6IXpjwKoUUY-MD9EjMcgC21PF64gqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حکم اعدام تبعه خارجی دخیل در جنایت میدان علیخانی اصفهان اجرا شد
🔹
قائم حسینی، تبعه خارجی و از عناصر دخیل در جنایت میدان علیخانی اصفهان که منجر به شهادت مظلومانه چهار نیروی فراجا شد، پس از رسیدگی به پرونده و تأیید حکم در دیوان عالی کشور، به جرم کشیدن سلاح و ایجاد رعب و وحشت، ایجاد ناامنی عمومی و ناامنی در حد وسیع، اقدام علیه تمامیت جسمانی افراد و امنیت ملی به نحوی که موجب اخلال شدید در نظم عمومی شده بود، پس از طی روال قانونی به دار مجازات آویخته شد.
🔹
قائم حسینی به پیکر شهید نیروی انتظامی لگد زده بود و جهیزیۀ نوعروسان خیریه امیرالمؤمنین (ع) را به آتش‌ کشیده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/682733" target="_blank">📅 09:25 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682731">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
مقام ارشد امنیتی ایران: محاصره دریایی آمریکا، تجاوز نظامی به زیرساخت ایران تلقی می‌شود/ محدودیت تجارت نفت و کالا در انتظار کشورهای منطقه
اسپوتنیک به نقل از یک مقام ارشد امنیتی ایران:
🔹
محاصره دریایی آمریکا یک اقدام تجاوزکارانه است؛ نسبت به واکنش منطقه‌ای ایران هشدار می‌دهیم.
🔹
اعمال محدودیت برای ورود کالا به ایران یا افزایش فشارهای اقتصادی در شرایطی که محاصره دریایی آمریکا به مثابه اقدام تجاوزکارانه علیه ایران ادامه دارد، از سوی تهران به‌عنوان تجاوز نظامی به زیرساخت‌های کشور تلقی شده و موجب واکنشی خواهد شد که پیامدهای آن متوجه کل منطقه به‌ویژه همدستان و شرکای امنیتی و تجاری آمریکا خواهد بود.
🔹
جمهوری اسلامی ایران تحمل نخواهد کرد که کشورهای منطقه که به انحای مختلف در بروز وضعیت فعلی نقش و تقصیر داشته‌اند آزادانه به تجارت نفت و کالا ادامه دهند و ملت ایران به‌ناحق مورد فشار، تحریم و محاصره قرار داشته باشد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/682731" target="_blank">📅 09:09 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682730">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
زمان اعلام نتایج نهایی آزمون ارشد اعلام شد
رئیس سازمان سنجش:
🔹
نتایج نهایی آزمون کارشناسی ارشد اواخر هفته آینده بر روی سایت سازمان سنجش آموزش کشور قرار می‌گیرد.
🔹
پذیرفته شدگان آزمون کارشناسی ارشد سال ۱۴۰۵ از اوایل آبان ماه سال جاری در کلاس های درس دانشگاه ها حضور خواهند یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/682730" target="_blank">📅 09:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682729">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند
🔹
آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/682729" target="_blank">📅 09:05 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682728">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
میزان تاثیر معدل و سهم آزمون در کنکور ۱۴۰۵
رئیس سازمان سنجش
:
🔹
در سه گروه آزمایشی اصلی، ۶۰ درصد نمره کل متقاضیان از سوابق تحصیلی و ۴۰ درصد از نمره آزمون سراسری محاسبه می‌شود.
🔹
سهم سوابق تحصیلی پایه یازدهم در سال جاری به صورت مثبت اعمال خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/akhbarefori/682728" target="_blank">📅 08:58 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682726">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tC8kEWtLNq7oe8z67w10I3qOV1xnKUaoh1pDxBILHmWTc7K8BisSm1FL9AQMDBlrc14iCa9OndonOpuzg5U9m62x0It4oRV5mq9o-ut2GjHy98_IcYufcTAhJaFrtI9m1g2JIXIZ9Zy73hn74CC9A1eg5n6dls-axm67EL1fZSKbAuHofbpN4zegGz0PqaZ91iTFI9VTt8LLIsLQ3OmuwD0M8xfdYsBpBaFJTFcY-_vGoVq33WtuZw-QXVnbqqzu-Jlz1xo2kn4m6--zQ_NcGbfkhZdrXI6gGsKu7Q-cnKNXKgezPH3Gg-6bmDNdDTtwTSHftoeHZHIuHy3KZQdfCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالعمل ارزشیابی پیشرفت تحصیلی تربیتی و برنامه آزمون‌های شهریورماه ۱۴۰۵ اعلام شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/682726" target="_blank">📅 08:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682725">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/081eab3852.mp4?token=mvrF_yiDps9G7_9PlumorQ9nxN6VSAuYJnnGkcE911zbICKhQGFsoge2LiHPkfCVfdDUrMRXix8D4nliFE2SCdw3MfjDwVmahN2hPae4zFvdPXvggFOsIX2OAo65HxYB8b8OEIlND0yjbLb3oGddNVF2SgnHTp5OtIpoxnj6nKuodMS6_2nUNZUQ4YAhNsaMYLJ5_RGMSjb-LfI2q89sCJN7iWbdfhmp_PJ-o5e1ichmjrEf_Jv37uIKzrZshCX37KA_DFBpBPA59T2NGr7wVLcPuRsowVfJIpOSpUOVCTF-gpu5Etwi9J4jJQKDgqNYT0EJAbIBTOAvfMOJJYXmwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/081eab3852.mp4?token=mvrF_yiDps9G7_9PlumorQ9nxN6VSAuYJnnGkcE911zbICKhQGFsoge2LiHPkfCVfdDUrMRXix8D4nliFE2SCdw3MfjDwVmahN2hPae4zFvdPXvggFOsIX2OAo65HxYB8b8OEIlND0yjbLb3oGddNVF2SgnHTp5OtIpoxnj6nKuodMS6_2nUNZUQ4YAhNsaMYLJ5_RGMSjb-LfI2q89sCJN7iWbdfhmp_PJ-o5e1ichmjrEf_Jv37uIKzrZshCX37KA_DFBpBPA59T2NGr7wVLcPuRsowVfJIpOSpUOVCTF-gpu5Etwi9J4jJQKDgqNYT0EJAbIBTOAvfMOJJYXmwDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بندر چینی در گوانگ‌ژو؛ باربران مجازی کشتی‌ها را از راه دور با ۵G تخلیه می‌کنند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/akhbarefori/682725" target="_blank">📅 08:38 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682724">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5df29aeb07.mp4?token=QvFypjhaX-1Eq599OBTVdLpA36N2pSNAmOrFkNc7fYucM0D4edRBJI0d1Bcefc4mhHeRRBn4NIf9BYPZpDnJUUboaI5D3ZcJe5KHadKHi0Q11Kil_dEEKAfDk8dLmO9nWnQkJTya4mdB-MdZBRw6qSycxMC29zKmxwJXu3MLXf9e8lCVPfItV2dlFJ_e9TmPR2QGkyHQj1O58oXrZ_sD8WtESqNpOC0UjqV8Pffi2UjmO_oFlSAfjcqbj4GFKmGIhsLbqf0jlz5qWaas9pJj0fQeZ0RQ04aZCeE_Ctotr7Fin-LbOetmKmIgTpwLgXh_DaqIlfcYbtJuQJcCquzCbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5df29aeb07.mp4?token=QvFypjhaX-1Eq599OBTVdLpA36N2pSNAmOrFkNc7fYucM0D4edRBJI0d1Bcefc4mhHeRRBn4NIf9BYPZpDnJUUboaI5D3ZcJe5KHadKHi0Q11Kil_dEEKAfDk8dLmO9nWnQkJTya4mdB-MdZBRw6qSycxMC29zKmxwJXu3MLXf9e8lCVPfItV2dlFJ_e9TmPR2QGkyHQj1O58oXrZ_sD8WtESqNpOC0UjqV8Pffi2UjmO_oFlSAfjcqbj4GFKmGIhsLbqf0jlz5qWaas9pJj0fQeZ0RQ04aZCeE_Ctotr7Fin-LbOetmKmIgTpwLgXh_DaqIlfcYbtJuQJcCquzCbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر علوم: در کنکور امسال کارت ورود به جلسۀ ۴ نفر از داوطلبان صادر شده بود که در جنگ اخیر به شهادت رسیده‌اند
🔹
آغاز نیمسال تحصیلی نو ورودها احتمالاً در آبان‌ماه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/682724" target="_blank">📅 08:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682723">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
آزمون سراسری سال ۱۴۰۵ تا دقایقی دیگر آغاز می‌شود
🔹
امروز داوطلبان گروه آزمایشی علوم تجربی در آزمون سراسری حاضر شدند در این آزمون ۴۵۱۵۲۲ داوطلب شرکت کردند که در این آزمون ۶۹ درصد خانم و ۳۱ درصد آقا هستند.
🔹
همچنین بعد از ظهر امروز آزمون سراسری زبان‌های خارجی…</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/682723" target="_blank">📅 08:13 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682721">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa0d09f26.mp4?token=vEvIZ9Mti-V_IyuIbLA1AfjdU8ClWVkR7nYrJutK6OdgSXo-HdC5-22NDkjn0jIM2eQmmBAX6WoOkngtBy6JRRqDAli6cRcHfy5FBQbp_Pwt41cj9On1Y58rEMkBdbZw9EEPuGO3I9UhehhjFBsvdVPvyxY6aDkH_vhM60_rIG9jYdD-z12kmRggn9kH0TPqOx-JaIjrmVUUSQKNcsGXCY2vXEaQv3n8GJVYC8wwhZHeHCpjDqulB9N4qMbybiAYEyothEVWEwlZjWGJwWP_TigT814a5sAeJJbcYsAOaxfE-B4dq-EX7J4giLPBymm3N3LgUpWixIPbokilrkbD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa0d09f26.mp4?token=vEvIZ9Mti-V_IyuIbLA1AfjdU8ClWVkR7nYrJutK6OdgSXo-HdC5-22NDkjn0jIM2eQmmBAX6WoOkngtBy6JRRqDAli6cRcHfy5FBQbp_Pwt41cj9On1Y58rEMkBdbZw9EEPuGO3I9UhehhjFBsvdVPvyxY6aDkH_vhM60_rIG9jYdD-z12kmRggn9kH0TPqOx-JaIjrmVUUSQKNcsGXCY2vXEaQv3n8GJVYC8wwhZHeHCpjDqulB9N4qMbybiAYEyothEVWEwlZjWGJwWP_TigT814a5sAeJJbcYsAOaxfE-B4dq-EX7J4giLPBymm3N3LgUpWixIPbokilrkbD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این چند حرکت رو توی خونه با استمرار انجام بده و تغییر رو ببین
💪
#ورزش_صبحگاهی
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/682721" target="_blank">📅 08:00 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682720">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
کارشناس چینی: در جنگ فیل‌ها، سبزه پامال می‌شود
کارشناس چینی:
🔹
برخی کشورهای منطقه در ماجرای جنگ با ایران مصداق بارز این ضرب‌المثل هستند که «در جنگ فیل‌ها، سبزه پامال می‌شود».
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/682720" target="_blank">📅 07:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682717">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
آزمون سراسری سال ۱۴۰۵ تا دقایقی دیگر آغاز می‌شود
🔹
امروز داوطلبان گروه آزمایشی علوم تجربی در آزمون سراسری حاضر شدند در این آزمون ۴۵۱۵۲۲ داوطلب شرکت کردند که در این آزمون ۶۹ درصد خانم و ۳۱ درصد آقا هستند.
🔹
همچنین بعد از ظهر امروز آزمون سراسری زبان‌های خارجی برگزار می‌شود در این آزمون ۹۰۱۷۳ داوطلب شرکت می‌کنند که ۶۹ درصد اون‌ها هم خانم و ۳۱ درصد آقا هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/682717" target="_blank">📅 07:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682716">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcWXASBLWvaW6C2yXJLG4k5hiJYA6K8q2NUO1aPjqeCa7PkGxRdOI98QzIYo-ZGZ79fqOQgWnPwwkhA67LNbxGdd2neX-ex5JaO7rtQ1onZwY5Bz2XElnE9ch2Js2FcWVB8fNeMMMV2SbkkGD8Q5VFGAz_zTklGEjnXkNBymbI7QYhx8flfw1m2c6CQcrGiKDi5BHh80-MAbfUP9ZcZRe5oBxY6ey6Aol4-Ok7IN3mHeMyIyR4z4O_ymvOY-vp1F6cH5OVGUmR5IZ8fe46a_ijwayUteoPx4uWx22Te51jtx7SjbRSbBAtVtkz7txckukaHFhQN511r2joS4vPOEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۲۹ مرداد ماه
۷ ربیع‌الأول ۱۴۴۸
۲۰ آگوست ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/akhbarefori/682716" target="_blank">📅 07:31 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682715">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muSula1_bj5ad10DiunjrVQYOXxlrPGKlS-rtP4ttjteHkrxLsO15FgK7q1lCCSP8yQY4kx5WCtXONfFp_Vgn-frLDmymcTZeS-pq4cZiBEHdhsEjlVEGPNjnYyxQ8gbDGe_PG2O1KktSjR7OsU0u8KVFCiFDhJOb05lZaOL2z6wpDgRp7z7Eb3I9t--h3MQ4zEMBnRsNGDG1j3A36YaoHjilOAitwrcaeKJ-G9GFC8kGC7dIRowHGsXJqFMInqhVayGHXU6KMQPayGrq60iXvsymO8nZkZ-BHV_Awhg2TKsmACmdci0bHFDY0_uV0bfz0kUNsMgCDYatmilTKsTtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز توی سوپرمارکت دیجی‌کالا آتیش‌بازی تخفیف به راهه!
🔥
➗
کد تخفیف ۵۰۰ هزار تومانی
➕
تا
۹۹٪ تخفیف
روی کالاهای شگفت‌انگیز
🚚
با
ارسال رایگان
و زیر
۴۵ دقیقه‌
🔥
هرچی برای خونه‌ات میخوایی از  کالاهای
سوپرمارکتی و نان تا پروتئین و میوه
، با تخفیف ویژه موجوده!
🛒
کد تخفیف ۵۰۰ هزارتومانی ویژه کاربر جدید:
DET555
⏰
فقط امروز
⏰
بزن بریم خرید از سوپرمارکت دیجی‌کالا
👇
dgka.me/ATTISHBAZI
dgka.me/ATTISHBAZI</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/akhbarefori/682715" target="_blank">📅 03:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682713">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LajcW-5vxOyBJYKg5Eeb0z_oI20LXcWh0ezeJ5d8-XBItfUz31ZzqhoXR1o8FD6A9K7Lo2tBGMzGX3H5HCoLW5z-tXv-_1ziW_OnC8Tzwud4HCBrTGhFuyTUlihcrG27d7GWnYm9WePluHnVdRfjBqPLADTLCTmh9At_ZRmt9aIEGWTSDk7c32TnmvyE5lcc3BDo959ogHfN0bTg849VMx7XRCKQbogUFbm7CVEhuE17LquSAJeOo1_rPBhy0R69Cpglczk87AKgL-WG0dDklHCMegVSBeITb7Ng6ADV5YVX0ONDVS3Tb8Yg_XrNeUeUcWa2uvrv3ekuBgOUB-tEvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ شیاد مدعی آغاز جنگ اقتصادی علیه ایران شد
رئیس جمهور جنایتکار آمریکا:
🔹
هیچ‌کس به اندازه من فرصت بزرگ‌تری برای دستیابی به یک توافق در اختیار جمهوری اسلامی ایران نگذاشته است.
🔹
متأسفانه برای خودشان، نتوانستند از این فرصت استفاده کنند. بنابراین امروز اعلام می‌کنم که سنگین‌ترین عملیات اقتصادی‌ای که تاکنون علیه هر کشوری انجام شده است، آغاز خواهد شد.
🔹
این یک جنگ اقتصادی و انزوایی در مقیاسی بی‌سابقه خواهد بود.
🔹
امروز همچنین اعلام می‌کنم هر کشوری که به مؤسسات مالی، شرکت‌ها، فرودگاه‌ها یا نهادهای دولتی خود اجازه دهد هر نوع راه نجاتی برای ایران فراهم کنند، خود با پیامدهای اقتصادی بسیار سنگین روبه‌رو خواهد شد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/akhbarefori/682713" target="_blank">📅 02:44 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682710">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c1ae5df3.mp4?token=bc0pvqDFIWO9_gysrqHpBiV633rtjo2CQO9yaXp1kBYS2MvaSAFMuJbCUrMe3gf3ynEF3sECVj6LS6j0sTPim7zwTy-da-wWl9eGaSS8sNdGzhDlQ7YNPyPrzMoKjDyfyzNwx06iXtvnZOzcYNGpKmWb6T6EjDupubTvzMJMrXLsRpOUkEx-jFB4gw0YY2rk8vi4EUp4hLoaIqECry1fiVjc1_c5xtwHhTxlkw-ujGQKj34ZxCzWR2DH3C-i22Mid_aOpWRs-cT97koirvLSM6fJBfFhWsC0ccCNAR6JZ_2mBeH9r_9eDwkWG82OUyv_j0Hjlw894VFkRuKOWXLT1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c1ae5df3.mp4?token=bc0pvqDFIWO9_gysrqHpBiV633rtjo2CQO9yaXp1kBYS2MvaSAFMuJbCUrMe3gf3ynEF3sECVj6LS6j0sTPim7zwTy-da-wWl9eGaSS8sNdGzhDlQ7YNPyPrzMoKjDyfyzNwx06iXtvnZOzcYNGpKmWb6T6EjDupubTvzMJMrXLsRpOUkEx-jFB4gw0YY2rk8vi4EUp4hLoaIqECry1fiVjc1_c5xtwHhTxlkw-ujGQKj34ZxCzWR2DH3C-i22Mid_aOpWRs-cT97koirvLSM6fJBfFhWsC0ccCNAR6JZ_2mBeH9r_9eDwkWG82OUyv_j0Hjlw894VFkRuKOWXLT1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات موشکی روسیه به پایتخت اوکراین
🔹
رسانه‌های اوکراینی بامداد پنجشنبه از وقوع چندین انفجار قدرتمند در کی‌یف خبر دادند.
🔹
گفته می‌شود حداقل ۱۵ موشک بالستیک و هایپرسونیک شامل اسکندر و زیرکان به‌طور همزمان از چندین منطقه روسیه شلیک شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/akhbarefori/682710" target="_blank">📅 01:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682708">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iL5dZiPA_fsoopmMPNNDmTrX8Lh3x4U47vQh6LCAtc-4K0YjUEvJYxZzbfI_QEowJqw-zu3zDpe9e2eptB3cf3MbNUmCA5NuJUTFODJZsm_cxmKhfMPwv72wiCdhlg4zZGwkNbS4HM7ZUhqf8x8zMM8k0PrjWl838vl2JMSXDt1z5iIrcQ17US1SVuMSR5_ejMVhOakprOamoafoReea9keDy09Zy31j4OpsW0smQxjSqjQH2dWsGlzlnZAjXhdW5nhS-ZY1DYK23glmG3GAJ4iNgxcrTwE1lCoO8-Ga5w3QVpXEd4dhKaCW6tXIqWEvCyoV0g08Wtt0mcVlzYEsww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آمریکایی‌ها واشنگتن را پیروز جنگ می‌دانند یا تهران را؟
🔹
آخرین نظرسنجی اکونومیست/یوگاو نشان می‌دهد ۲۷ درصد آمریکا را پیروز می‌دانند، در مقابل ۲۲ درصد ایران. در حالی که ۳۵ درصد معتقدند فعلاً هیچ‌کدام برتری ندارند.
🔹
۵۴ درصد جمهوری‌خواهان معتقدند آمریکا در حال پیروزی است، در حالی که این رقم میان دموکرات‌ها تنها ۹ درصد است.
🔹
در مقابل، فقط ۳ درصد جمهوری‌خواهان ایران را پیروز می‌دانند این رقم میان دموکرات‌ها به ۳۴ درصد می‌رسد. همچنین ۲۵ درصد جمهوری‌خواهان و ۴۴ درصد دموکرات‌ها معتقدند هیچ‌کدام از دو کشور فعلاً در جنگ برتری ندارند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/akhbarefori/682708" target="_blank">📅 00:53 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Od40Z0AtopeKzNh3g_Ha3tXoOifv_gaMpnIJYYAHn35yakVRpjvWJwSfK3_rPVi5WpyBCYViVLAj_t2n7rqnvKUnqMj7DezH-G24yy7wAiyHJpA2V2Qq3wsPKYxi0W-6_w08SLyrFPZZPGERNGpjOFaEhHL1LAmdrUVPnrFWTNyNGKZbeRHvu7T7-3Z0gurFWpXCV4MG5k44lgO8T6f4fpJ11pI-dfZm7Ry8PfsrEcIwnXjRb4Yt7Z7r6JvB9ynJIELP4jtaYutEqkuPqMFS98h_Z91NNAzt3fctdae2yhp8jNx1JXqYLXXSxyrCBBKDDuzGig-8lOugFN0WkEMonA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FfeTANbjBY1P7-MObHDytvc0uA-W_x2Lk3sjatqWQErcl7RGMh06Rgjaa8cQWx93lKGS65ACsFTKs-fsCS3pyLaMvY9ZvTkDdlz4UrU8RXb-jfOM-9YIqsj-0zzwEgujDjndjePCLrxccgFW1ybsloDlHsWoFCrSXJ9WRVwr_jJczRpWVxUfq36vLfZE0mWqleSfuIPeqHWw-mRSY0Gru6jubgfTy2CzlwwPKPhda5HiucqDak078chRX4NGZNt6bl3fdRRedEV-PZDoLhiYsXRd86tFYL92MgVaEIKQTsYAd3OFx6P8PceZ471a8RvSepnu63jWbK8DmKn2g5_s3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCa3lIZapG-wJk0s8iWgf3azNrJxmldZTJ6TgvqG4GFmT9CjM6SwDRf4ZJXxfTFUdq9RYR9AbbLcrcHRf5XVjMbt2eR_EHCYL_9j6nV6EcWorb63QLAbyscYHnsZzb0fZNWc5nckkL9F8Lgkbv-MOunwfP6aNRUdJmdMYhakOVDPvjX0VSBid3p4kntwrCyLIVOBnrAjggq9U3t75JtQDR10g-a_wUhH9NKKxmjEMOFlcSKoQ1ohrDyOOWMKxr46knJAJS5cp5VTqE6Cs0dvMRUVqHhouwCv2Sdjy5jFzAhG41B80wEHaZlcfm7zWpbGYjQDZLuc7JZhddKMMoOYyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QAmXGCfuBJfu6kOjB0idaj64YhW3z38OHuZtE4kTEVs1Dx51tCEU8ll5KHFzJletqHnyIx0SRoQBxcX6Sy-vSbRrWk3nc5a0kjIXxk4XSL8FOV8pIZ415MnghMOwhdhMqTCtJUgXdYSyY03LP-5OZZhbnJVXMhrDxze8DZ7gMhaiLObghOBKTKgBaKRcYp65cAzgaCUxF4jnOilyIivTIFctS0ZA-BBnrc2QmiuzTqEmUeILT10WzCoRnSlgbZGx4pYwtItEfumSvjKfoMn9KMUH5q4yBPbgW43_FfMu3MIzISwQoN8dOB8_vsW27gSN5WrvC_tTDQWSGJZkJuENzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9qdIk9-TUfv482AKcgzKdlpw_dF8JMba0xHNtVutKQVQNpyrmWAaVsLkwiBCgziqc-H-bv3TXgTpnUVpYeTUiO8cp9s7cq1LPnUQFe6aYAoJb2wCojawN86pau9uB0himEyNFVgVGdZu6c8IhX67FLco_Dh2HRja2zeioAl8isuU8m2p0ERMmadUqxaXIE4Q9zDmK_tRHNF791PH7wbUizM9gg8ulqAi-eT-uSs5IymVi8w8ZP7x_0EVSkICFVUeZLl0-G46wFA-DBKbQI9uMEpV5xIj0gnjveaxYItyBlkarFaxApsui0UFTCWiqQHPbLeqMnqZ-5emXP8ZYhf2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D-o9JfanO1V5uCq8k_O6YvcUj6Y77uam6Z-uFkc03hNjV7nCkrhIPxkJ7ZP6BVgZoFiW2db3DFVisBG5gGNbYKDsgQ5oDmGwdIIsQbFG6UOx5D0-qR7QYVU4TG-1g-2Fwd96D5UKCfCeMQm_cKE66E-lC8u08OKller5GMfymDF-f1i-5HawVRio3eeSsaKukf9bf-6xIpXrQflVDFcn5ZzImg0phJTftg44uiKyOz0VYc5nyTeL7Kql1N4u4pwyCFRdP3d7tWx5JzqPX4tOi9npgsErAIOIjpMxrXS1XeFFn5inarNguwhdYMou_dJPUojX8v6UXhtEkgN9Z10sFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نقشه جدید اروپا در جنگ ایران و آمریکا
🔹
اروپا در جنگ میان آمریکا و ایران کجا ایستاد؟ اگر جنگ جدیدی شکل بگیرد، اروپا چه نقشی خواهد داشت؟ پشت خروج ناوها، واگذاری پایگاه‌ها و تحرکات دیپلماتیک، آرایش متفاوتی در  اروپا در حال شکل‌گیری است.
🔹
در این اسلایدها ببینید.
@Tv_Fori</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/akhbarefori/682702" target="_blank">📅 00:48 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-682701">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGHcG-NNfI9wZlpSFnQXrugOUbFgUyCHVugUHJHEJm7qxsCFnCe_xCf0wjRPpjmrLz6Qn_GGpXdwC0_8kjDiG58UTxxXHpot9H9P0WpuRxKgTimysNHq388db08elAtanU94y7C1cKhb_ELKqS3VewuMmaJjyvMya0iMMcyT5KS6w01G_G4f9Q7-hPKWJKitvqCZEPiyPFM6gXFhe6Q1PtP7D78LZ3qPcYCzZpsI8oK-nfstfwqgKVul63mX-O3T5hkSRPRPu8fAT9lx6AjqeVYfpR1qB93iWWdtFKF_740c3vLXx2D3bbqI5cS_bJZF65FSObq71LjnLtUTkvrNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روبرتو کارلوس شایعات مربوط به مسلمان شدن خود را تکذیب کرد
اسطوره فوتبال برزیل:
🔹
من برای دین اسلام احترام زیادی قائلم و دیدن اینکه همسرم نماز می‌خواند، بسیار عالی است.
🔹
اما شایعاتی که در مورد مسلمان شدن من منتشر شده، نادرست هستند.
🔹
کارلوس به تازگی با زنی مسلمان ازدواج کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/akhbarefori/682701" target="_blank">📅 00:46 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
