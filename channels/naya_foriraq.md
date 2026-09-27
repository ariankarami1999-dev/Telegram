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
<img src="https://cdn4.telesco.pe/file/PfPTM9mKw1PJwmlnjabEUJ3Woe7WhauD6RB0LZEj1x04yxHEYV8gaTvQaZKcoKiBb8zgwsKWsABJdY1Q9JhpWsY5sKTaPhRRDPGOX82EItCkcuIMxGwlxqvWyXbGFYIpGUWTeDndnBJh4T-wHG0MZog7-_IFaHhK7t9BpwPPVP-zt5EMYpZleR7R_5bpHEl-oYZsW7aT0TKpPReymiR72unVY5t-H1C4c26yNlDxcD3CT8-J5bJ49TvFZXQbU7R8Cv1B62QJhl74vFPDWqiG6j5F7vh6d5jAaP7Q6WqpbfxDSibLZFZkj7jJUyBq5iSriXsPoUenZEuOzcZ3x7Rcpw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 266K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 00:08:05</div>
<hr>

<div class="tg-post" id="msg-91810">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca41f5abb5.mp4?token=MA-qfsvkRTr6wjYRr1D-qBOK9xxPLpYhHn00Nb0secR8c3-exOVNphMGmzG_nl3P3y4AKf7PoCIiVSKXSNwdZqGjKCk-nZGM1y_vAw2I_3VKjMKs4wJ71udNcFO7_O1Z52qsZ2clAT1cFf19LppLKlXdmCct9VmuoCR-necH7-MmZlicdabK9piS8SQ2FxdgEfsQYuWWE7f5W_3NMgio854MDlp5hzhlpHpyiS_AnTSKm2Xu1iEOJXJlXMNTIDOXUH29Gz6qRPhasnoNM2KCOFxLxU41VIHK69q3V8yqbGHXUdLdoECU_-2PUiSgxcGYOWfvn4ATdlM7uIFLrT9ymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca41f5abb5.mp4?token=MA-qfsvkRTr6wjYRr1D-qBOK9xxPLpYhHn00Nb0secR8c3-exOVNphMGmzG_nl3P3y4AKf7PoCIiVSKXSNwdZqGjKCk-nZGM1y_vAw2I_3VKjMKs4wJ71udNcFO7_O1Z52qsZ2clAT1cFf19LppLKlXdmCct9VmuoCR-necH7-MmZlicdabK9piS8SQ2FxdgEfsQYuWWE7f5W_3NMgio854MDlp5hzhlpHpyiS_AnTSKm2Xu1iEOJXJlXMNTIDOXUH29Gz6qRPhasnoNM2KCOFxLxU41VIHK69q3V8yqbGHXUdLdoECU_-2PUiSgxcGYOWfvn4ATdlM7uIFLrT9ymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇮🇶
قوافل الاحتلال الاميركي تستمر في الانسحاب من محافظة اربيل الى خارج العراق.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/naya_foriraq/91810" target="_blank">📅 00:03 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91809">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eff26c4ef.mp4?token=tTxAPmhBvclrAofBZvI9aHy0X7FxqFrVOiDYWOwekx5-XirAIw3_yQFE-u_eyPW8dj_EvakvxVoxW7QV6NN1yUZC-HKdGcSh1uGwj4ZFaqA4OBEre9WC3GN_Ee5BjfGjnhI9Wnu_KYTTtWdlrjNXj83-iRzxJ0JuZlPvclgi2cGivnw0IvKxFr5B19uZVsthWAq-lV5_qEnB8CBX2hJwYvXubXn1UBCCQJM019FiLY0k_hdGi_WiM-lWKjvrypfn8fEf1Q-VObXlbfG9FU3tsYWcKGpdHRNe2BGrl7M791EsYK6dmomKHAtyo4cAuvSqwYErHUXZ9_WFQdiWSrlpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eff26c4ef.mp4?token=tTxAPmhBvclrAofBZvI9aHy0X7FxqFrVOiDYWOwekx5-XirAIw3_yQFE-u_eyPW8dj_EvakvxVoxW7QV6NN1yUZC-HKdGcSh1uGwj4ZFaqA4OBEre9WC3GN_Ee5BjfGjnhI9Wnu_KYTTtWdlrjNXj83-iRzxJ0JuZlPvclgi2cGivnw0IvKxFr5B19uZVsthWAq-lV5_qEnB8CBX2hJwYvXubXn1UBCCQJM019FiLY0k_hdGi_WiM-lWKjvrypfn8fEf1Q-VObXlbfG9FU3tsYWcKGpdHRNe2BGrl7M791EsYK6dmomKHAtyo4cAuvSqwYErHUXZ9_WFQdiWSrlpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مسعود بارزاني: في حال انسحاب القوات الأميركية لن يكون هناك ضامن لمنع عودة تنظيم داعsh الإرهابي.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/naya_foriraq/91809" target="_blank">📅 23:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91808">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">كوريا الجنوبية:
وافقت كوريا الجنوبية على إبقاء عملية نقل أسرى الحرب الكوريين الشماليين سرية بسبب مخاوف أمنية ودبلوماسية.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/naya_foriraq/91808" target="_blank">📅 23:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91807">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f241fbcd.mp4?token=RMvMeg-f9Co6F9aES_p4WNSmsuhHqYLjDxub_cCkDNCtDgtrNZRynQyvJPYqGVfyPs50l0ijSnYBHwlWaMU86a-ytXwVOBd9DVEY2pG12g6uJryZh9bT1eFy0PBnJLJEt1Ur2Zqd6GqNscdQN1S1LAtzU63bNomac5w23YDJcl6mCQftdh87wMHDB9pd6_MVTGQXxVaTWvazKNLOjLOmEn10bZuO0Be2crRCJZTysLaFbVUYAuPyZNg-PhaG0hu5FFPqJLdFIfnLXIbGod7dESoOUocp-xIM22kZ2XtZfGLE3eZGRmPRjdrJsue7WIq8Zv7f1nZ2JFUGcQdGIzBnNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f241fbcd.mp4?token=RMvMeg-f9Co6F9aES_p4WNSmsuhHqYLjDxub_cCkDNCtDgtrNZRynQyvJPYqGVfyPs50l0ijSnYBHwlWaMU86a-ytXwVOBd9DVEY2pG12g6uJryZh9bT1eFy0PBnJLJEt1Ur2Zqd6GqNscdQN1S1LAtzU63bNomac5w23YDJcl6mCQftdh87wMHDB9pd6_MVTGQXxVaTWvazKNLOjLOmEn10bZuO0Be2crRCJZTysLaFbVUYAuPyZNg-PhaG0hu5FFPqJLdFIfnLXIbGod7dESoOUocp-xIM22kZ2XtZfGLE3eZGRmPRjdrJsue7WIq8Zv7f1nZ2JFUGcQdGIzBnNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇸🇾
العراق يستورد أول شحنة بنزين عبر المواني السورية باتجاه المعابر الحدودية</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/naya_foriraq/91807" target="_blank">📅 23:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91806">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14c7c2387b.mp4?token=PVkaE2psPzRduM2m31LyVM6C9VY-Nb43R9uuFpXSX_MuRIVdqhTbxlXlzMMKj04j27uyMNyg4oV1xkzERT4T7PZTFbv1BlvrmjbVUoxv0r6V1yj0iO7xVNthQ9KkHArJxmbH5MAp54DgtLCYp-iYmPZ1HmTHLgA4LFZiGzYXKlHNMSkHqNG5mD5npDzzwWlFwc3P1Z07_SuXhEWXBrLxRuDUeOujTD0GXJ0nzEnUty8ArdnZdMzJ1jP5CD39lukr7xO8qxAzdeWKA4O7cZALE3mY74pc-SAGXVmvGQLdURe0OIHxYfj-Se0mDbI4dW43UhPsjN15v17hYy9aHj5vLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14c7c2387b.mp4?token=PVkaE2psPzRduM2m31LyVM6C9VY-Nb43R9uuFpXSX_MuRIVdqhTbxlXlzMMKj04j27uyMNyg4oV1xkzERT4T7PZTFbv1BlvrmjbVUoxv0r6V1yj0iO7xVNthQ9KkHArJxmbH5MAp54DgtLCYp-iYmPZ1HmTHLgA4LFZiGzYXKlHNMSkHqNG5mD5npDzzwWlFwc3P1Z07_SuXhEWXBrLxRuDUeOujTD0GXJ0nzEnUty8ArdnZdMzJ1jP5CD39lukr7xO8qxAzdeWKA4O7cZALE3mY74pc-SAGXVmvGQLdURe0OIHxYfj-Se0mDbI4dW43UhPsjN15v17hYy9aHj5vLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد تصريحات مسرور برزاني الاخيرة والاشتباكات التي حصلت بعد التصريحات بساعات.. استمرار وصول التعزيزات العسكرية إلى محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/naya_foriraq/91806" target="_blank">📅 23:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91805">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/naya_foriraq/91805" target="_blank">📅 23:11 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91804">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇶
اشتباكات مسلحة في محافظة دهوك شمالي العراق اصابة ١٥ شخص كحصيلة اولية.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/naya_foriraq/91804" target="_blank">📅 23:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91803">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇮🇱
الاعلام العبري:
سافر نتنياهو اليوم إلى الإمارات العربية المتحدة للقاء الرئيس محمد بن زايد.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/91803" target="_blank">📅 22:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91802">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">إعلام بريطاني : الهجوم يقف خلفه عناصر من استخبارات الحرس الثوري الإيراني</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/91802" target="_blank">📅 22:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91801">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
الخارجية العراقية:
القوات الأميركية أنهت انسحابها تماما من العراق، ويونيو المقبل سيكون موعدا نهائيا لإتمام عملية سحب سلاح الفصائل.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91801" target="_blank">📅 21:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a9584f77.mp4?token=tv-6zkSSoIXTWlTNqZA94SPsJqBQwAKBoU1SnIu2VxMnUre1Wml7grqIo3GRCcb-SU0I2qy8b1W8r4f3fPrPsi-FguP6rGjXbiQrekZubkRkoQDc9wTraEpbxuznyQRb_oByJYHDTFlnAZoQuT-5wrfBmMglYAGtH4twf062ayA8ROZIBo923O818n1vpalsCcIJlBYpmbAMeaTUOfCvEgtOu0FgCfVQjfmvm2l9sPXQsGLgv_iAV1MTDhgMyx9R4bBGgnFS7EOqQBgVDEatBUyDkMh8XjuoUUXdXHV3RxzzTjOFd9rO-gb18b39wD7kIBJkVM3FPcVgvNcuw2H9mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a9584f77.mp4?token=tv-6zkSSoIXTWlTNqZA94SPsJqBQwAKBoU1SnIu2VxMnUre1Wml7grqIo3GRCcb-SU0I2qy8b1W8r4f3fPrPsi-FguP6rGjXbiQrekZubkRkoQDc9wTraEpbxuznyQRb_oByJYHDTFlnAZoQuT-5wrfBmMglYAGtH4twf062ayA8ROZIBo923O818n1vpalsCcIJlBYpmbAMeaTUOfCvEgtOu0FgCfVQjfmvm2l9sPXQsGLgv_iAV1MTDhgMyx9R4bBGgnFS7EOqQBgVDEatBUyDkMh8XjuoUUXdXHV3RxzzTjOFd9rO-gb18b39wD7kIBJkVM3FPcVgvNcuw2H9mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
مشاهد أرشيفية من سجون النظام البحريني للحظة إعلان استشهاد سماحة السيد حسن نصر الله وردود فعل الأسرى عقب سماع الخبر.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/91800" target="_blank">📅 21:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مشاهد ارشيفية للشهيد الاقدس السيد حسن نصر الله والشهيد الجنرال قاسم سليماني.  الشهيد الحاج قاسم سليماني قائلا: سأضحي بحياتي من أجل شخصين؛ أولاً، القائد الأعلى للثورة، وثانياً، السيد حسن نصرالله.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/91799" target="_blank">📅 21:53 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
اطلاق عدة صواريخ نحو مضيق هرمز.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/91798" target="_blank">📅 21:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🇮🇱
وزارة خارجية الاحتلال الإسرائيلي:
ستنتهي حصانة دبلوماسية المبعوثين الهولنديين في رام الله في غضون سبعة أيام.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91797" target="_blank">📅 21:25 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537ca099d6.mp4?token=fuiLyT9G6uDAcAz_lexcb9MCm5_rIWCzQ5rs6DTDzgHkdv_7FZW-RP2bhkab612K6hAbAo8QjPR0B5NSQjMrbWpmKi7pc7aMGWDY8np8WyxKQ53sxwmS7YHn1UMJ8txlJv7I2KO_isPEgySqcl381HKORkIvFIYc0Gt15fbONVqZfH5Xiws9PgFmZ-ZhHBRpIyxeih6LNOyOTzNRzkAVu9irLr4k8l134IuapYZ7enDOD0P-gvwmxbet7dtWoUoNvGHQeFY_Pn7EBf_hJddchJaKL9JymgrQs0bhfAQtERcpFufuiXxgopR6fEjxQL179kUDok-gNBnrGkhoFLqBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537ca099d6.mp4?token=fuiLyT9G6uDAcAz_lexcb9MCm5_rIWCzQ5rs6DTDzgHkdv_7FZW-RP2bhkab612K6hAbAo8QjPR0B5NSQjMrbWpmKi7pc7aMGWDY8np8WyxKQ53sxwmS7YHn1UMJ8txlJv7I2KO_isPEgySqcl381HKORkIvFIYc0Gt15fbONVqZfH5Xiws9PgFmZ-ZhHBRpIyxeih6LNOyOTzNRzkAVu9irLr4k8l134IuapYZ7enDOD0P-gvwmxbet7dtWoUoNvGHQeFY_Pn7EBf_hJddchJaKL9JymgrQs0bhfAQtERcpFufuiXxgopR6fEjxQL179kUDok-gNBnrGkhoFLqBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ویدیو المنار از حضور شهید سید حسن نصرالله در حومه جنوبی بیروت ودر میان مردم لبنان.  @Naya_Press</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91796" target="_blank">📅 20:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🇾🇪
مشاهد حطام طائرة استطلاع مسلحة نوع "كاريال" تابعة للعدو السعودي أسقطتها الدفاعات الجوية في أجواء محافظة حجة - 27 سبتمبر 2026م
.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91795" target="_blank">📅 20:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ترامب: الاعتقالات في المملكة المتحدة تمثل تطورًا إيجابيًا. المشتبه بهم كانوا تحت المراقبة لفترة طويلة، وقد تم القبض عليهم.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91794" target="_blank">📅 20:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇾🇪
العميد يحيى السريع:
‏شن الطيران الحربي السعودي خلال الـ24 ساعة الماضية 26 غارة جوية من خلال طائرات "F15" أقلعت من قاعدة خميس مشيط واستهدفت محافظات تعز والجوف ومأرب وذمار وصعدة.
‏وخلفت عشرات الشهداء والجرحى من المدنيين
‏ليبلغ إجمالي غارات العدوان السعودي منذ بدء التصعيد 1085 غارة جويةً وصاروخاً.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91793" target="_blank">📅 20:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91792">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IpWifn8q_inei4scOcRIPRbvNEdyPiU-5-PTbAOoQMGhI0M3CAqiLvIP9TtKrQo_gLyolzs_dRjGMtL1UhZKS02nbkh8y4sIANC2a2wbM2MqcEs-wbaQ0gcb68a1755FY0C3S05qdnvMh52j4LW0SwfR-cS6CxVrmUAl6Dya9XmSdIq48JL19j6uL4XcijEGtSV1TnBFEj6E9TYBs-TNMaf5-CmHaWb3s-qlMexdofadsx-EzyzZdwNmd85IobVdvCKBh68IuUXdRsh1NE388n0KncgFGFDpPnZxU36fOmoomG7pHr1Z2orDf2_ncutsCnKf1YmjIF7F2FLm0Cd3kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
مشاهد جديدة من الاشتباكات التي حصلت في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91792" target="_blank">📅 19:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91791">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13ec925cde.mp4?token=jIXs5uu6bjP_W4wRTabeGXlWLwWZxXhbHsyPIm18QK2_0vFqKHWPT04C5bKkSnDpQ5-GJoAAPRQfKBh10hc59GvH5V0w8fwpAIZctjNMWETHpFVVOUc_mvj_e3-HYXvOJfoCRaA7EkzMEzRmmo31_Q7RZUXBzs9phwCcoL9nJRyV2J14g5v-UqaxVdYi6biQT-olJuC6KR4GnpUwn6SoK05yHhWVxJnXOowdk5ZyoNfUqjqofClAIV6Rlm89MMHRy1lmVG-QtigXojvq0NqaVtr0eTk8PYqYFFNPmlWyP-FkeC9zScD1N0cxUb5cMT-YOwxkvQXmaFPMXl0muuzCGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13ec925cde.mp4?token=jIXs5uu6bjP_W4wRTabeGXlWLwWZxXhbHsyPIm18QK2_0vFqKHWPT04C5bKkSnDpQ5-GJoAAPRQfKBh10hc59GvH5V0w8fwpAIZctjNMWETHpFVVOUc_mvj_e3-HYXvOJfoCRaA7EkzMEzRmmo31_Q7RZUXBzs9phwCcoL9nJRyV2J14g5v-UqaxVdYi6biQT-olJuC6KR4GnpUwn6SoK05yHhWVxJnXOowdk5ZyoNfUqjqofClAIV6Rlm89MMHRy1lmVG-QtigXojvq0NqaVtr0eTk8PYqYFFNPmlWyP-FkeC9zScD1N0cxUb5cMT-YOwxkvQXmaFPMXl0muuzCGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد تصريحات مسرور برزاني الاخيرة والاشتباكات التي حصلت بعد التصريحات بساعات.. استمرار وصول التعزيزات العسكرية إلى محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/91791" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91790">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29138c0f8.mp4?token=R8xlYyhnUdlv3ROSInoE4rh712UOd2-dhtJtnZYGVmkxRgtA2AgNv5y_eNLqWnMFixKqTnAqORMClmJUm_KXd-CBtK6sbu-iexbwpfeNxDaLMFqtiixqAQmcfIYQdrvLB9vt0bxoNvsyX8RkvX3lr_B3Esh6uq_pMxV9lAbSxWygDKexvE9rVzLUp2Q_6k0ee3VWHWHsyULdZhYSck8Y9UApGAF-WyiFi4QOFm8QI0zA8Ai6guO2LPuaUp0Yl828X-4ocIdChFTX2t9Srqgm9Eyxzt8KQgHgwaeWgnbNTiwMexSF6wLWk2KaJZ0AFGosEEiCaiUPE1veUMJ0gl7KiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29138c0f8.mp4?token=R8xlYyhnUdlv3ROSInoE4rh712UOd2-dhtJtnZYGVmkxRgtA2AgNv5y_eNLqWnMFixKqTnAqORMClmJUm_KXd-CBtK6sbu-iexbwpfeNxDaLMFqtiixqAQmcfIYQdrvLB9vt0bxoNvsyX8RkvX3lr_B3Esh6uq_pMxV9lAbSxWygDKexvE9rVzLUp2Q_6k0ee3VWHWHsyULdZhYSck8Y9UApGAF-WyiFi4QOFm8QI0zA8Ai6guO2LPuaUp0Yl828X-4ocIdChFTX2t9Srqgm9Eyxzt8KQgHgwaeWgnbNTiwMexSF6wLWk2KaJZ0AFGosEEiCaiUPE1veUMJ0gl7KiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثث عناصر داعش بعد اشتباكات الاخيرة التي دارت مع قواتنا الامنية في محافظة كركوك شمالي العراق.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/91790" target="_blank">📅 19:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91788">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p7_mzG-LhW7K3ns9vjb5SlIkDRXz0ymdOXB7qr8A91i6rHujqNAJ2hAAtuH3fSwaNGUwShSC0baQS3Dx31OgnZs5R2Jb0ha1oPIiSKXNOud7lTXDML8B1dJAchwdAY980ZFMPMSZflxPtY-F21vxOewWVFgGfoXy8c7av_npJ96jeIfvSe5tMm1p1EBcUTXRlyf6mz8kuZLg4o3qSR_0C2YIypr82jZrl4CVAmROLi10VMDGss4YwELLHhfmsh2neSGq0Gm3S5OgNtziAGdSeGcY1zlb35Q-vKccyBMn4-RofoTHTB1gzAWlYEqJP6dc8D5FWPQMMKkitxzY5gwdDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSoeVBF_tlEK5W9d-4tvPw13Q_ldOu6wQvQy29GojwCVi9wyLFYVzKllZLpdUFtVuNefOe9SqyOdYQgbGiHJ_wkW1IQOMYk6_pUipb1ljvYMnCCLY4PdZkx1OTipag2O-yMzFlR9ulldnJN4Cfl33AIdc_QKOszvjuSwGtqEcmQ1V6Qj04HMpmGBZfoWSrHEU4NNw9rrkDdV5Z0OX89vh3ocKqZ6Agp7LwOvgjWTTWxuqKhLQUImpVAR92UHa11bggHmG2Pcd1VRktUdbGSAD7CN4LA5pBNpiFJ8WVhICMGYWZKiGan8-lFBUoy_fVfZM_iwfqf6P2ABTjCfqwVT2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/91788" target="_blank">📅 19:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91787">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf92de22fe.mp4?token=rbzQ2peZO_r3lgYAIPvpTbSeh14xNwpo82IHUTAXQ4phhHb1zajXjKWPJRq-4G8pkJ7kja2OZvvk4e8nE-SquaGdHqDKzJOpNDj-56Nvn0lDTApNGX_E16f0XjHsn4SH1rxCpt9dO6EgppIFqPVpV6hTgAjnuwJ-PtHaids8MJve3zJQ2HFa_N3hobe9FgEVIM9rp1ogrl194ojbLGYTT8T-es-UJgFnwh0RT9S_MYbuP_h5xtsWgSxwAjSIs1ad6xHIF80Rc4Vjvr_BoBLnF5A4bJSXBRalTKRthy0pj5nP9Cw--GDkZslR8hmghX0ubMWUlkw8LPx6Pa8R8rzEwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf92de22fe.mp4?token=rbzQ2peZO_r3lgYAIPvpTbSeh14xNwpo82IHUTAXQ4phhHb1zajXjKWPJRq-4G8pkJ7kja2OZvvk4e8nE-SquaGdHqDKzJOpNDj-56Nvn0lDTApNGX_E16f0XjHsn4SH1rxCpt9dO6EgppIFqPVpV6hTgAjnuwJ-PtHaids8MJve3zJQ2HFa_N3hobe9FgEVIM9rp1ogrl194ojbLGYTT8T-es-UJgFnwh0RT9S_MYbuP_h5xtsWgSxwAjSIs1ad6xHIF80Rc4Vjvr_BoBLnF5A4bJSXBRalTKRthy0pj5nP9Cw--GDkZslR8hmghX0ubMWUlkw8LPx6Pa8R8rzEwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ویدیو المنار از حضور شهید سید حسن نصرالله در حومه جنوبی بیروت ودر میان مردم لبنان.
@Naya_Press</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91787" target="_blank">📅 19:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91786">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJABaBsML21pTZApH31QElZmjMsOBI45XIARJI6C-jCkbPknoM4PeoQ1zNQZQo7nvVCQgWWNMywLL6y1U1XGckPtUqvaG9gDVTuG1RKFT9cAWOboTpha4mYNBVFvlDdctmCVPoca-UJmDLvuwfBr0LN8o0hWEzzHdt4AEenaKEnII0B38-v2OCKxo9Rn_Krs3aVuLv095CpJP_kd8pb8bnRgDRviPBWZinOBI3a1eN_yMlnZhiRrklcDDi2bmU6FI1Uxld9q4aPDdFNieznMOnBAgusbgYDbxlRTDli7vxHfg3R1XGvzR2GkSnNujO3yIpGObUzczb1Zt8bLzaIXGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جثث عناصر داعsh الارهابي مرمية على الارض بعد مواجهات مسلحة عنيفة دارت مع القوات الامنية العراقية في محافظة كركوك شمالي العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91786" target="_blank">📅 19:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91785">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
جثث عناصر داعsh الارهابي مرمية على الارض بعد مواجهات مسلحة عنيفة دارت مع القوات الامنية العراقية في محافظة كركوك شمالي العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91785" target="_blank">📅 19:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91784">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇸🇦
الاعلام السعودي:
مباحثات وزير الخارجية العراقي في واشنطن ستبحث"استثناءات" بهبوط الطيران الإيراني في مطارات العراق. ‌</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/91784" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91783">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95cba77d6e.mp4?token=qYym3R0cRsv8HBXghhS6nHHZVCnyZ9klt3lYQhhGoWg4StvequVVJ7CTklldfBggoiE6UVldp_IVb5RZR1_jkgEuPcK_771jKlCN5x3OEHQL49LyPbrZmfwNj5cxXV6MQuXT6Awty7srg5_d4XsTfPDf-LLk-vDyGoAg8wkWbQiXbzW5OWyAuQegUpTRqF6ySkJBNdiDZiFeUL4ojQ_U7POFG5uF9A6Iqcug8Q312NOI4JX8wraoOP3HJNUF0OnL_Lzq0AloHDeJBB0LJh3yvIXEHpoyX6P6kVn5JQD8XbTil55DgeyT5I_05LMibaIoedJTF_EbNUHmwuoxPhpKnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95cba77d6e.mp4?token=qYym3R0cRsv8HBXghhS6nHHZVCnyZ9klt3lYQhhGoWg4StvequVVJ7CTklldfBggoiE6UVldp_IVb5RZR1_jkgEuPcK_771jKlCN5x3OEHQL49LyPbrZmfwNj5cxXV6MQuXT6Awty7srg5_d4XsTfPDf-LLk-vDyGoAg8wkWbQiXbzW5OWyAuQegUpTRqF6ySkJBNdiDZiFeUL4ojQ_U7POFG5uF9A6Iqcug8Q312NOI4JX8wraoOP3HJNUF0OnL_Lzq0AloHDeJBB0LJh3yvIXEHpoyX6P6kVn5JQD8XbTil55DgeyT5I_05LMibaIoedJTF_EbNUHmwuoxPhpKnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
جثث عناصر داعsh الارهابي مرمية على الارض بعد مواجهات مسلحة عنيفة دارت مع القوات الامنية العراقية في محافظة كركوك شمالي العراق.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91783" target="_blank">📅 18:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91782">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ad809475.mp4?token=Idyc8a0lgc4igvNmOPsVSGC49JV7gx0Pwab1U5zXdxgBiDcIQ9LPxOYKK5OPNICBg9uW3LvldlmzWeV4dpwRBu3doCmj7PDWMjgpE-NBvSkngS0bzncxr1AEbG1UdVds6CXB1OowSvYsamiLlfpuVKRSF_BwBihzGjFcw3v9045qEET9_2IMG3qrcnnLcm35FoLAgqL9ROOmhPy1bStIv0G7O5OvRn4IY6Qw0LDvX5_K6-8N1epAptknxTZsmF97y-4--vm3q22wHhJlkEMKRrW4KaLny6Xh6f7ptaRaKG2_xeAAkG734EpOZxdHPFREyxddQSqJMTYMmgo_DEmv5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ad809475.mp4?token=Idyc8a0lgc4igvNmOPsVSGC49JV7gx0Pwab1U5zXdxgBiDcIQ9LPxOYKK5OPNICBg9uW3LvldlmzWeV4dpwRBu3doCmj7PDWMjgpE-NBvSkngS0bzncxr1AEbG1UdVds6CXB1OowSvYsamiLlfpuVKRSF_BwBihzGjFcw3v9045qEET9_2IMG3qrcnnLcm35FoLAgqL9ROOmhPy1bStIv0G7O5OvRn4IY6Qw0LDvX5_K6-8N1epAptknxTZsmF97y-4--vm3q22wHhJlkEMKRrW4KaLny6Xh6f7ptaRaKG2_xeAAkG734EpOZxdHPFREyxddQSqJMTYMmgo_DEmv5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/91782" target="_blank">📅 18:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91781">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مشاهد من الاشتباكات في محافظة كركوك</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/91781" target="_blank">📅 18:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91780">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
ترامب: أفكر في استئناف الضربات على إيران باستمرار، والاتفاق الذي طرحته إيران كان يمكن أن نوافق عليه قبل عام من الآن، أتوقع أن يجري المفاوضون الأمريكيون مزيداً من المحادثات مع إيران هذا الأسبوع.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/91780" target="_blank">📅 18:41 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91779">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
ترامب:
أفكر في استئناف الضربات على إيران باستمرار، والاتفاق الذي طرحته إيران كان يمكن أن نوافق عليه قبل عام من الآن، أتوقع أن يجري المفاوضون الأمريكيون مزيداً من المحادثات مع إيران هذا الأسبوع.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/91779" target="_blank">📅 18:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91778">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b035464a0c.mp4?token=PXDIcMFovYU_4sfNmib0XM7m4EozXSwhHsQlmDWeHxuGK1k_FLUhDmLzCp-grXfZ_7qAZK3DDoDFPza4hc6IPc8FVgmftHl-pdDhglsRiBj_HqaQT3nPjCA7jMQ_SbC-uvQXuYw0eOO0UFphBQsfOn1A6DEvVEJGsXQnzSX0PI_KuYLcmt_MjUZjidsn8X4CMdaiDodAQd005CcFyvMUGCHNiPdovJg040daQwoAcdAwX2yolUov7Oz6L-eLxffKyMdIlm00y8D0kwILNAo1B8NRyhoAL4lAoPhrfsamCvUHzkjJ-x1ZVKMOLSPIJkqoIICXgm35c2B9NkRTS_7Bsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b035464a0c.mp4?token=PXDIcMFovYU_4sfNmib0XM7m4EozXSwhHsQlmDWeHxuGK1k_FLUhDmLzCp-grXfZ_7qAZK3DDoDFPza4hc6IPc8FVgmftHl-pdDhglsRiBj_HqaQT3nPjCA7jMQ_SbC-uvQXuYw0eOO0UFphBQsfOn1A6DEvVEJGsXQnzSX0PI_KuYLcmt_MjUZjidsn8X4CMdaiDodAQd005CcFyvMUGCHNiPdovJg040daQwoAcdAwX2yolUov7Oz6L-eLxffKyMdIlm00y8D0kwILNAo1B8NRyhoAL4lAoPhrfsamCvUHzkjJ-x1ZVKMOLSPIJkqoIICXgm35c2B9NkRTS_7Bsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اغلاق مداخل التون كوبري مع تواصل الاشتباكات بين القوات العراقية وعناصر داعش</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91778" target="_blank">📅 18:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91777">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇮🇶
جهاز مكافحة الارهاب: اشتباكات لابطال الجهاز مع فلول عصابات داعش الارهابي تسفر عن مقتل ارهابيين اثنين يرتدون الاحزمة الناسفة في كركوك - التون كوبري وسنوافيكم التفاصيل لاحقا.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91777" target="_blank">📅 18:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91776">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الشرطة البريطانية حول حادثة قاعدة فيرفورد الجوية: تم القبض على 5 أشخاص بالقرب من القاعدة وتم إبلاغ 85 أسرة بالإخلاء.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91776" target="_blank">📅 18:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91775">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الشيخ نعيم قاسم: قررت شورى حزب الله تسمية كل المرحلة التي بدأت مع معركة أولي البأس الى اليوم مرحلة إنا على العهد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91775" target="_blank">📅 18:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91774">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم للسيد نصر الله:  أنت المقاومة والمقاومة أنت وأصبحت رمزها لأحرار العالم. أنت القائد المقاوم الأممي تلهم الأحرار في العالم. غادرت بجسدك وبقيت تعاليمك وبقي النور للعطاء الذي يمدّنا بالعزيمة. لقد بنيت حزباً ومقاومة وحالة شعبية ثابتة وقوية وسنستمر…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91774" target="_blank">📅 17:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91773">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">مسرور البرزاني: يعدّ سحب القوات الأمريكية من العراق تكرارًا لخطأ باراك أوباما عام 2011، حين سحب جميع قواته تاركًا فراغًا أمنيًا في البلاد، ما أدى إلى ظهور الجماعات الإرهابية. إذا تدهور الوضع الأمني ​​بعد سحب القوات، فقد نطالب المجتمع الدولي بالعودة إلى المنطقة…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91773" target="_blank">📅 17:52 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91772">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اشتباكات عنيفة في محافظة كركوك</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/91772" target="_blank">📅 17:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91771">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔻
الشيخ نعيم قاسم للسيد نصر الله:
أنت المقاومة والمقاومة أنت وأصبحت رمزها لأحرار العالم. أنت القائد المقاوم الأممي تلهم الأحرار في العالم. غادرت بجسدك وبقيت تعاليمك وبقي النور للعطاء الذي يمدّنا بالعزيمة. لقد بنيت حزباً ومقاومة وحالة شعبية ثابتة وقوية وسنستمر على هذا النهج. حملت راية فلسطين وزرعتها في حياتنا وستبقى فلسطين هي البوصلة وتحرير أرضنا سيبقى أولوية</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91771" target="_blank">📅 17:42 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91770">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaf84221f5.mp4?token=YCJ9uip07Tlay5OXau2Bx4R-SHtU0zp7xFN1RveCuR-waWqd0guqfkiHFuFwp1XMhvpiKr5j0xXzD0GJiady0Bhd0Tzj7qOHWi_k3ZOjdklt46YD2xNJ1AK88eEM7tlIset8_1ZulQfpLs147Btfzez3wh076FUUUAN8TTLglHGD6Co9kHW98QB6RKVSFDkcY9k1HeofIbeu5nMnOQ3iY0hlqt34YLMCfnzGFNDSBuew-wTwo8607vmslXdsJDOATrh6kf3paH0nljCvMTjf3Sj5_6gxh9QyHPAS4oWupQYYTN7E3BwJTZ3T1bNxwasaaeaJEU-E2K9xXqvUxYjkfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaf84221f5.mp4?token=YCJ9uip07Tlay5OXau2Bx4R-SHtU0zp7xFN1RveCuR-waWqd0guqfkiHFuFwp1XMhvpiKr5j0xXzD0GJiady0Bhd0Tzj7qOHWi_k3ZOjdklt46YD2xNJ1AK88eEM7tlIset8_1ZulQfpLs147Btfzez3wh076FUUUAN8TTLglHGD6Co9kHW98QB6RKVSFDkcY9k1HeofIbeu5nMnOQ3iY0hlqt34YLMCfnzGFNDSBuew-wTwo8607vmslXdsJDOATrh6kf3paH0nljCvMTjf3Sj5_6gxh9QyHPAS4oWupQYYTN7E3BwJTZ3T1bNxwasaaeaJEU-E2K9xXqvUxYjkfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات في محافظة كركوك شمالي العراق بين جهاز مكافحة الارهاب وجهات مجهولة.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/91770" target="_blank">📅 17:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91769">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d2246b444.mp4?token=IWcKA2eZ7AtKIag1umQpU2ng0vWbUTKZSco-kb2BpCcFxMUkXJr3SOoBwpQvV6T2oOlpkneiyt6fTJ6wyqSwvqDkuout78OIViIIU5SaFwlbWZ_bLbbFVX0JFTwh2nRLdosPYPrYODpkQ3PI0tYzljk5RJHRa-0d_2JUK3KHbHmuczeDaWcrLWBeoftnqMTXP80A3dDXSQ5902RnSdWg-xkN6AOAbmxyh6D6nDEUj8t_vFN1mTIxtBzppHhdJQ4S0vQTPIgzsAZtXbQtnScSNuL13v6ZUET-pN4h9g4X1bAqVZHmW1OtjeIZf0BMgyEmz4_e-2cIS72R5JP6ltEreA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d2246b444.mp4?token=IWcKA2eZ7AtKIag1umQpU2ng0vWbUTKZSco-kb2BpCcFxMUkXJr3SOoBwpQvV6T2oOlpkneiyt6fTJ6wyqSwvqDkuout78OIViIIU5SaFwlbWZ_bLbbFVX0JFTwh2nRLdosPYPrYODpkQ3PI0tYzljk5RJHRa-0d_2JUK3KHbHmuczeDaWcrLWBeoftnqMTXP80A3dDXSQ5902RnSdWg-xkN6AOAbmxyh6D6nDEUj8t_vFN1mTIxtBzppHhdJQ4S0vQTPIgzsAZtXbQtnScSNuL13v6ZUET-pN4h9g4X1bAqVZHmW1OtjeIZf0BMgyEmz4_e-2cIS72R5JP6ltEreA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اشتباكات في محافظة كركوك شمالي العراق بين جهاز مكافحة الارهاب وجهات مجهولة.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91769" target="_blank">📅 17:20 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91768">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y5tZXyTbApcvLi0X1Eva1r32Zbaeko-OgtELIl9nycLrXKuZI6OtN43B6TMGjoMrz2c6wKnBTm3BzGNlQP5fELfuBG-ZiYSVkw67ZYsvfoDcQI-uulUJXwyeBb1UTsaY3nKOb0SyY8SmdyMMTsSp8tC23XKV2ywLnSrl_tZOhHhZm3om7OgaXybpFa6AAejXZJNpECv8rymjfEnZ7dwpt3ACeB2ICyqPgyk6aSx8UO-hCCEybVi4BMdDBzuli94U-vRv0758BTOoZFlM4McwOlAS1zQ_l1SdB89NZnqIRZ9D1oy7NtFlwZcw-cD39daOvtnzOM8y9HAPRhJXqQB9JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئيس المجلس التنفيذي لحركة النجباء يدعو أبناء الشعب العراقي للاعتصام أمام مطار النجف الأشرف</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/91768" target="_blank">📅 17:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91767">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇶
مسؤول عراقي:
- تعليق الرحلات الجوية مع إيران رهن بامتثال شركات الخدمة الأرضية لتعليمات الخزانة الأمريكية
- غياب الموقف الحكومي المعلن بشأن الرحلات الإيرانية يعود إلى حساسية الملف
- اعتذار الشركات عن تقديم الخدمات قبل الإقلاع وبعد الهبوط أدى إلى تعليق الرحلات الإيرانية</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/91767" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91766">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4fab36c4.mp4?token=o88yzatncC47RprHxVLQsJ3oSoPvpz1txR6FOjTnMHcRPFTao7mF6D7jqIitRtOVnWIw-_Ir2tSZk_HVthAe_dpzuj7AvJnH4O_G5h8G44_BHqPKX4NS64t-GLX0YJoh7xiqJFNe2RcYFUhyQg-FNX90J02B8Y1PXirGAJZDKapjlTW3WMYVkF8C5l5EcguBEDd_AqygLfmI0-6DtHB42Yob2M5pGe0FwWPe9ET0nX7ew9Nc1_zs4W60d7mmI8WMowsIwP01B-LLVVCtSqonNadQeWzga5tGPhGPP5kPvZhAIVb-1YgbK1Hp-kM5-gF_kGshuZVLehFpRknDp-zvui7AZ9Yw-QptOfyMwTMC3ilsd16zwS7Vhiq6-LsM4VxHk51iH9ei88y3NaxL1A-4dCavg9BBCkqx2vuSkQiv7N-k0d3qLTF-V_dI224lT5oKiH6eU4fejzgIDW0WeKPQhW16fdfJc2MqWZu6coaTVQj-KTj-6jV-DXTX2_ISohghzxwWKYFi1_gIczujrn6o0AHJilCR05FUUpQK6q9NO8aMJmDL8rvkbZ34AwTqq1U5KJXLkzHCMKiyBuwp97QTmKTrtpNKMsa0JnNRBt9803DDkHdvkEqcrWqV_jKqxfax9oM6cvci8NTwEYzm2AvxL4vTOemuF0B0HnJPKXI1VI8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4fab36c4.mp4?token=o88yzatncC47RprHxVLQsJ3oSoPvpz1txR6FOjTnMHcRPFTao7mF6D7jqIitRtOVnWIw-_Ir2tSZk_HVthAe_dpzuj7AvJnH4O_G5h8G44_BHqPKX4NS64t-GLX0YJoh7xiqJFNe2RcYFUhyQg-FNX90J02B8Y1PXirGAJZDKapjlTW3WMYVkF8C5l5EcguBEDd_AqygLfmI0-6DtHB42Yob2M5pGe0FwWPe9ET0nX7ew9Nc1_zs4W60d7mmI8WMowsIwP01B-LLVVCtSqonNadQeWzga5tGPhGPP5kPvZhAIVb-1YgbK1Hp-kM5-gF_kGshuZVLehFpRknDp-zvui7AZ9Yw-QptOfyMwTMC3ilsd16zwS7Vhiq6-LsM4VxHk51iH9ei88y3NaxL1A-4dCavg9BBCkqx2vuSkQiv7N-k0d3qLTF-V_dI224lT5oKiH6eU4fejzgIDW0WeKPQhW16fdfJc2MqWZu6coaTVQj-KTj-6jV-DXTX2_ISohghzxwWKYFi1_gIczujrn6o0AHJilCR05FUUpQK6q9NO8aMJmDL8rvkbZ34AwTqq1U5KJXLkzHCMKiyBuwp97QTmKTrtpNKMsa0JnNRBt9803DDkHdvkEqcrWqV_jKqxfax9oM6cvci8NTwEYzm2AvxL4vTOemuF0B0HnJPKXI1VI8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#ترفيهي
🇺🇸
🌟
ترامب:
أصبح النفط الآن أقل تكلفة مما كان عليه في عهد إدارة بايدن.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91766" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91765">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
اليوم الأحد بتاريخ 27 سبتمبر 2026م وعند الساعة (11:00 صباحا) اتجه تشكيل حربي سعودي نوع "F15" من قاعدة خميس مشيط باتجاه محافظة تعز وشن غارتين على سوق تعز في مفرق ماوية عند الساعة (11:29صباحا) مرتكبا جريمة نكراء بحق المدنيين خلفت قرابة الــ50 ما بين شهيد وجريح كحصيلة أولية، ثم غادر أجواء تعز في تمام الساعة (11:37صباحا) متوجها إلى محافظة الجوف وشن أربع غارات على مديرية خب والشعب، ثم غادر محافظة الجوف عائدا إلى قاعدة خميس مشيط في السعودية عند الساعة (14:00).
إن هذه الدماء التي سُفكت ظلماً وعدواناً في سوق ماوية بمحافظة تعز ستكون عواقبها على المجرم السعودي وخيمة بإذن الله وقوته وما النصر إلا من عند الله.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91765" target="_blank">📅 16:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91764">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔻
‏أجلت الشرطة منازل بالقرب من قاعدة فيرفورد الجوية التابعة لسلاح الجو الملكي البريطاني، وهي قاعدة جوية أمريكية في إنجلترا، وألقت القبض على عدد من الرجال للاشتباه في ارتكابهم جرائم تتعلق بالمتفجرات. وتستخدم القوات الأمريكية هذه القاعدة خلال الحرب مع إيران.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/91764" target="_blank">📅 16:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91763">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">نظام الجولاني يطلق سراح (59) سائقاً عراقياً</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/91763" target="_blank">📅 16:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91762">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
إسقاط طائرة استطلاع مسلح نوع "كاريال" تابعة للعدو السعودي وذلك أثناء قيامها بأعمال عدائية في أجواء منطقة الطينة بمحافظة حجة، وتم إسقاطها بسلاح مناسب.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/91762" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91760">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f6c2d4b5e.mp4?token=Gh2k5ZdCdgFY4DNMDBPFF7nRUGeMufMBuQMII1UeUg5mrfUzSjfL82z5dRN0iRMpNfOJopTfGkB3ItrocAIHc71U1FWML6XF3xU081kMHclw3mOHaxp0ssZ9tT7zMpg8Tg2BCA0TSIMKYGJVFJLZmHx8UKwfqFKIb8l-OiDayyxsyDrscWAizAhGW9qBQqLKQSBsHlHk8IdqzJplkeW2Z9w5JNz98WOzPkLtFf5jEbxoOYjFl_-TR7Z_py8t-aWF5EKk0rwSl04ZrK2OR-f9gQsvk33FYqkwTk5hXO5oFHNxzybioGRzmtPbVWXpIZSMMBip-X4p3bE3KuVD5mo1ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f6c2d4b5e.mp4?token=Gh2k5ZdCdgFY4DNMDBPFF7nRUGeMufMBuQMII1UeUg5mrfUzSjfL82z5dRN0iRMpNfOJopTfGkB3ItrocAIHc71U1FWML6XF3xU081kMHclw3mOHaxp0ssZ9tT7zMpg8Tg2BCA0TSIMKYGJVFJLZmHx8UKwfqFKIb8l-OiDayyxsyDrscWAizAhGW9qBQqLKQSBsHlHk8IdqzJplkeW2Z9w5JNz98WOzPkLtFf5jEbxoOYjFl_-TR7Z_py8t-aWF5EKk0rwSl04ZrK2OR-f9gQsvk33FYqkwTk5hXO5oFHNxzybioGRzmtPbVWXpIZSMMBip-X4p3bE3KuVD5mo1ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزارة الدفاع الافغانية:
عشرات المسلحين عبروا خط ديورند يوم أمس في منطقة كامديش بدعم باكستاني لكن قواتنا أحبطت الهجوم.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91760" target="_blank">📅 14:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91759">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcaRsMtbO-pz7DtQvASNUrHqbd72AhyFpA3d_9peDliy158W2zA4fOmXo_57W_xdtjarIyK1_ipyZBPmKEMqosSE96qCSY-tfr9fnx5njWVfQ0OqxD4A6NtHORCuhQNImCe4ecporU3Aev29n6ASeKYSe3jhWSi7qSmR3E81_GiCHrHki7M0YdBa2Yyro4tfj-nu9po4mn6Cy52UWZTChKMEayV61THQq31Xk03UY1sGY210v3z01-znFnSYihwebt_E27Fz7vKhNLH6lBQmUGDkCyy-nAIzJuFPd6rsOjnDFAp9A4SPDQkalt3BYj9V0UF26wkion4bQXuQ3YskGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
السعودية تقرر تعليق الدراسة الحضورية في الرياض وتحويلها الى دراسة عن بعد بسبب هجمات القوات المسلحة اليمنية.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/91759" target="_blank">📅 14:31 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91758">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مسرور البرزاني معلقا على الانسحاب الامريكي: نحن ضعفاء، ونتعرض للهجوم.. وأن تُترك الان وحدك دون اي نظام دفاعي مناسب، دعنا نقول، انه امر مخجل</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91758" target="_blank">📅 14:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91757">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">مسرور البرزاني معلقا على الانسحاب الامريكي: نحن ضعفاء، ونتعرض للهجوم.. وأن تُترك الان وحدك دون اي نظام دفاعي مناسب، دعنا نقول، انه امر مخجل</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/91757" target="_blank">📅 14:21 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91756">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مشاهد للغواصة الأمريكية التي استولت عليها القوات البحرية التابعة للحرس الثوري في مضيق هرمز.</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/91756" target="_blank">📅 14:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91755">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
🇺🇸
الحرس الثوري يستولي على الغواصة الثانية التابعة للجيش الإرهابي الأمريكي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/91755" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91754">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/91754" target="_blank">📅 14:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91753">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/91753" target="_blank">📅 14:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91752">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4EeRuOE45dgiigV8V-We7eW2VUE-OW62CfX2hQjfM3LUdu145cEFqcFcrHXXbLcYSk59OHGwnMzeowt0f7kvpj17zefg7gB4CcfyjnfZlm4Mp2Wdxi8NqIIqC_zYpDMubDXUN5u85f3mabNsZ2XxcsWWppgWmk67vikHSamn7Fatsrd-9UALGmLqPeSTOSZR4MTKkwhsHpkyTKjUEMQR2nrdpNXukXaQ8VRjEo-Vtjk7hU8FfULJ_eGpZVgDAYo7VDD4gviSB_ggJNU5QNfr-VX5zOKjbZNwDbqP-kYqXmKPLa0zGrc0MShQgLL0vMVrUjTYj4ejoGNBsJEA56Jcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
جماهير النجف الاشرف تدعو لوقفة احتجاجية عند باب دخول مطار النجف الاشرف الدولي يوم غد عند الساعة الخامسة عصرا لاستنكار قرار منع هبوط الطائرات الايرانية في العراق.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/91752" target="_blank">📅 13:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91751">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🇮🇶
القضاء العراقي:
تبادلنا معلومات مع الجانب الالماني احبطت مخطط إرهابي في مدينة هامبورغ.
‏زودنا إسبانيا بأدلة أدت لتوقيف إرهابيين اثنين.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/91751" target="_blank">📅 13:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91749">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NAveeC3icZ_SUj208TkiUd-N829rZprlbrwHMGo1sxu0tgbpwaxy8PLvU8xJiH0Jq4936AMJblJ0KndzTZ9Y-ivJi6I8TNng8oPY-qPdXZrn7lHd4e9n1mZ8vH_--pdbxGy-hkf1i5IQqlwfbbY8WZy8j4drW8Z84E2RQ1OCH63CTyQaHgj_PsRVKT7IgeDJCn6f8A5TEJwMsKCYfwsqOX-zBH5S1GyOMgt2z_pLbMsjygZr_s2MqeQHuj2HKr5n7Jr7YSHn2VVlBET33-IIY-SXWTJJEVR6GLX4w1AqMejxE8eTX8eQ2fdpaaK9F0KXPVt7lOR8lG3Fda8WLzSeSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMlrH_N8w-_ZA1Gpn_poc-dwD_kShEFM7y9Lz8hAOjDOy74eio3j7qIL0xODi0MhIz6bBL8AyZzNUh3m-FXXGdSipW01ngzf3pixy3W-zTWDxm-Uu-XfaH0Gy8GP-5g2_5SM7v3USTVAkPv8cuknYrAUaqJqMlh7FleFCRK0Iu1CqmQM4ORcQy1U20yQmShL8gmuBKJiCK7qZZSNY3XRuqFZ-SKgqJAhQ7TARsDkGVgZkUkdiU3Ir8XQEAgCmZ2JLYT13k8Y-0a1EiWEan4ugtXEQvyfRTvX9hYK696lWg9VLYZ2wByjAkB7dPeXK3-sRoj-VoJcF2wdPUwb_CJbdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇸🇦
🇾🇪
الطيران الحربي السعودي شن عدة غارات على مناطق سكنية عقب إستهداف مواقع عسكرية تابعة لمرتزقته في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/91749" target="_blank">📅 13:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91748">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3c348627.mp4?token=ZlB4HscPTQS6vGJ2XpgDZZMu0km8eDy8Q54tTKweBvHzWxPFVhZ_cJdHZy6_XrO9ULmVwDqlwmOMNVCB0ajww3EY1RVBfxLar7fkZZ713gnMchfzj8R_BeOU3AxxqHcGU3b4b4AqXWIC0tEwSNZ8mmv2jvXcGJwSvvyfTcOUrNfzHN7viH1IfRSHx8CZbeX5URABpfFWswFnnlbfufiogQavCOQeeYsztXf0fcW0lWeJrpSKuNht6z8kH42nyRsCd9WTW5QfPGRx4l_b1-Dcym7-PqFFqAkYNN-ne6ThtAmM6ycnqkVF_szvEj04-4TIwg-VFOMqOJn3sddNFtvJ7oseuj5Tk-U1bCFxKaVOVYSs_RPkAkIH5VKiyBK6EwEVIJNGY4Bm0hGqIettGC8iqaSc-hnzUjwXw9KN5xlzcvrZpwnqzqzN1TQF-NMHEv3lpz6GEcZkPbALkQxz7z5YQ04w3kJkleMgxSolOkg1gnM6myGop-zt0cwtMpvwsamvKHq0tRSZatK6ZY9L0Q0wuLhT2_joj2XOKSbZyg41KSF1qBkIAcefWuCoiE0HfZW_pUA28h-WsRj6hi4X44vnoAUEs3Kf87jRSF-6UZuPx9WruD_ysEfQ48vqXug-yy1SFTMQvNprFZYgHrv_R6W7aGh6vi-hIOrouPKbnUZOC4E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3c348627.mp4?token=ZlB4HscPTQS6vGJ2XpgDZZMu0km8eDy8Q54tTKweBvHzWxPFVhZ_cJdHZy6_XrO9ULmVwDqlwmOMNVCB0ajww3EY1RVBfxLar7fkZZ713gnMchfzj8R_BeOU3AxxqHcGU3b4b4AqXWIC0tEwSNZ8mmv2jvXcGJwSvvyfTcOUrNfzHN7viH1IfRSHx8CZbeX5URABpfFWswFnnlbfufiogQavCOQeeYsztXf0fcW0lWeJrpSKuNht6z8kH42nyRsCd9WTW5QfPGRx4l_b1-Dcym7-PqFFqAkYNN-ne6ThtAmM6ycnqkVF_szvEj04-4TIwg-VFOMqOJn3sddNFtvJ7oseuj5Tk-U1bCFxKaVOVYSs_RPkAkIH5VKiyBK6EwEVIJNGY4Bm0hGqIettGC8iqaSc-hnzUjwXw9KN5xlzcvrZpwnqzqzN1TQF-NMHEv3lpz6GEcZkPbALkQxz7z5YQ04w3kJkleMgxSolOkg1gnM6myGop-zt0cwtMpvwsamvKHq0tRSZatK6ZY9L0Q0wuLhT2_joj2XOKSbZyg41KSF1qBkIAcefWuCoiE0HfZW_pUA28h-WsRj6hi4X44vnoAUEs3Kf87jRSF-6UZuPx9WruD_ysEfQ48vqXug-yy1SFTMQvNprFZYgHrv_R6W7aGh6vi-hIOrouPKbnUZOC4E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد إضافية من العدوان السعودي الغاشم  على مناطق سكنية ومحلات تجارية في محافظة تعز</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/91748" target="_blank">📅 13:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91747">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e43b98bab.mp4?token=oJjGEuoyg1o6F52ZiqBU963xzZH_DsEhsKmhDIew1YUFHw1ulrQYJ0ymZNj6-vpAmVf1Iuu88tlSbCyQEvgzwRaapEagYyegtwZdwHZfldAiNYpWumSxoiFBBhYdnR-t5pONTM8MWMh_BMQ_CLQdcNbsEpajCI70WY4WmbkcFgJ7s_zrL8TvV4Yj9FCtgV3K_-Vby7w342T02RSRSb4YZkMD9bUrh5fW-ZIFrjS9Yd7LD8tSz7dLqjM0sYv7NQ1ePiOWaxDwXuebwAfDCjWc35lz5U1oDjfh0t_wHtL-KG8x0r6Woth0MT5vpqOgypPUFkdZsCE_ZgW5wnwfMbQ1FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e43b98bab.mp4?token=oJjGEuoyg1o6F52ZiqBU963xzZH_DsEhsKmhDIew1YUFHw1ulrQYJ0ymZNj6-vpAmVf1Iuu88tlSbCyQEvgzwRaapEagYyegtwZdwHZfldAiNYpWumSxoiFBBhYdnR-t5pONTM8MWMh_BMQ_CLQdcNbsEpajCI70WY4WmbkcFgJ7s_zrL8TvV4Yj9FCtgV3K_-Vby7w342T02RSRSb4YZkMD9bUrh5fW-ZIFrjS9Yd7LD8tSz7dLqjM0sYv7NQ1ePiOWaxDwXuebwAfDCjWc35lz5U1oDjfh0t_wHtL-KG8x0r6Woth0MT5vpqOgypPUFkdZsCE_ZgW5wnwfMbQ1FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
سلسلة غارات سعودية على مناطق سكنية في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/91747" target="_blank">📅 13:10 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91746">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1922d2a68.mp4?token=oLTkGYFFZ8SNBByghNiNsxZTLFrL2t6oEQrXtQr5YJg_B5oGpBM5X4QDVATyfA0ubvj3t9QLdL4zw6XKJZbeqlXfzr2h4hlO78Wz30AkWnTrOW4a8pK789NdRSlEEJD8xWh_7JcORH-KG-AX5D7w-wDJyI96nO_sPYQtFpDfUEznHKnu_yo8YxpBHwA2C3J7ISE9lWgzbWd3ZWXoduQqVm9LtcLz8XolQbZU8xaT-q3RjZYeyXi3Rk2aRUKd6Ajvj1iLy2aUXnnXiA4G4kqnl-O7xD6XBTW0gCGpeoJzHnbm7VZr33KsVidQkr99B4JDrElgsfLzCzRzEpX-asY-E5fjyET27m2vxY2khCJF_zV4bolW3K0N7DbjYJ8TkYVtQAXZVDRHM5nbFvaT9yTehKGWYfiM0HD0a1Fy3HAFwEm2xUbhYdEraCze2a0_kv3AxHXWK18zwvcizRuQ02_xHn_jiboPA-OO-H7XXYZX24FZ8aw8sPGJHkl6xV5ky62aWV97isQ_6neSUYzA4yLk-3vNazOeylxAomVCenfsQH3hwPe7x4iS-AHWWxlSuzKBuKSbjZGE1aFNcgxIuU7I81sdZ7z0fU_-ElrqmdnS2xnA5meWBC0vRM2USvGsCIhVKpDKaHbfmFSwONl9JHufmihi5xPsbhWsexoJ6xHKH6U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1922d2a68.mp4?token=oLTkGYFFZ8SNBByghNiNsxZTLFrL2t6oEQrXtQr5YJg_B5oGpBM5X4QDVATyfA0ubvj3t9QLdL4zw6XKJZbeqlXfzr2h4hlO78Wz30AkWnTrOW4a8pK789NdRSlEEJD8xWh_7JcORH-KG-AX5D7w-wDJyI96nO_sPYQtFpDfUEznHKnu_yo8YxpBHwA2C3J7ISE9lWgzbWd3ZWXoduQqVm9LtcLz8XolQbZU8xaT-q3RjZYeyXi3Rk2aRUKd6Ajvj1iLy2aUXnnXiA4G4kqnl-O7xD6XBTW0gCGpeoJzHnbm7VZr33KsVidQkr99B4JDrElgsfLzCzRzEpX-asY-E5fjyET27m2vxY2khCJF_zV4bolW3K0N7DbjYJ8TkYVtQAXZVDRHM5nbFvaT9yTehKGWYfiM0HD0a1Fy3HAFwEm2xUbhYdEraCze2a0_kv3AxHXWK18zwvcizRuQ02_xHn_jiboPA-OO-H7XXYZX24FZ8aw8sPGJHkl6xV5ky62aWV97isQ_6neSUYzA4yLk-3vNazOeylxAomVCenfsQH3hwPe7x4iS-AHWWxlSuzKBuKSbjZGE1aFNcgxIuU7I81sdZ7z0fU_-ElrqmdnS2xnA5meWBC0vRM2USvGsCIhVKpDKaHbfmFSwONl9JHufmihi5xPsbhWsexoJ6xHKH6U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇦
🇾🇪
رداً على إستهداف مرتزقتها.. الطيران السعودي يشن عدة غارات على مناطق سكنية ومحلات تجارية في محافظة تعز اليمنية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/91746" target="_blank">📅 13:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91745">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b73c6fa19.mp4?token=NTNcr_OP1u3qeYZCDuntLxWmYmKBF1_gTpLTPJqqtrC_duC9APjfcS80Ij8JPph8X1SRrg_YzKeBej-uB-YW20_iaTw9nZiZM14KAZNrqCIGk2IOdQKlqSx01vJtHBPV4S9vhiAPoyUUYvY4G4YCHFoWWONJ1FOPQoQ2Lw9eJhdnXXIK0C6Ad2dcvz_nWsd_wg6PApX5tGjD8SixUVW3oQNwxmYqjHEvKiCaS-AGyXnipkqT10D49HlqDyjMmuY7Ed3ZlkWrH2rpQRnUFqpLFrX8Cffmx9lcrLq6IDKHhRNglN5cbmOXZ0DUYo2f92QEc-iMrvxYTI5ZnpCq8csDTHzdVLvMkl97FSD16eZcc-MsmwUPkfTFUproFQjrXnaLlB5Eazg52pMieMwTm1oZ1U21RkShnCYZvrlaRI0tCJXQBqo79Y3XfgotMIQCGQ4m6Qq5H6UlsybxiyPqW_zcEBrGzWHXYGO_rCa1SDjdk1jaXrtuQQWbAV6fr4o7fFTPK0G5lPU8V6CalJYxpdavXexUTWkHa6RxclEwWAZlvUtNqNmjXVDx3mLzIEGROjtBGc7PGwb37-ymg2ecziKlpdrl_HfHs7WBVR1BY3E6CpRvH5Cy5dbXUNVJf-Kjz6008q3ia6dEXQWU7psBA7xGNa2qkU4XvhbX75yEV0J4GHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b73c6fa19.mp4?token=NTNcr_OP1u3qeYZCDuntLxWmYmKBF1_gTpLTPJqqtrC_duC9APjfcS80Ij8JPph8X1SRrg_YzKeBej-uB-YW20_iaTw9nZiZM14KAZNrqCIGk2IOdQKlqSx01vJtHBPV4S9vhiAPoyUUYvY4G4YCHFoWWONJ1FOPQoQ2Lw9eJhdnXXIK0C6Ad2dcvz_nWsd_wg6PApX5tGjD8SixUVW3oQNwxmYqjHEvKiCaS-AGyXnipkqT10D49HlqDyjMmuY7Ed3ZlkWrH2rpQRnUFqpLFrX8Cffmx9lcrLq6IDKHhRNglN5cbmOXZ0DUYo2f92QEc-iMrvxYTI5ZnpCq8csDTHzdVLvMkl97FSD16eZcc-MsmwUPkfTFUproFQjrXnaLlB5Eazg52pMieMwTm1oZ1U21RkShnCYZvrlaRI0tCJXQBqo79Y3XfgotMIQCGQ4m6Qq5H6UlsybxiyPqW_zcEBrGzWHXYGO_rCa1SDjdk1jaXrtuQQWbAV6fr4o7fFTPK0G5lPU8V6CalJYxpdavXexUTWkHa6RxclEwWAZlvUtNqNmjXVDx3mLzIEGROjtBGc7PGwb37-ymg2ecziKlpdrl_HfHs7WBVR1BY3E6CpRvH5Cy5dbXUNVJf-Kjz6008q3ia6dEXQWU7psBA7xGNa2qkU4XvhbX75yEV0J4GHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية في منطقة هان بمحافظة تعز.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/91745" target="_blank">📅 13:03 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91744">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
🇸🇦
القوات اليمنية تستهدف مواقع مرتزقة السعودية في منطقة هان بمحافظة تعز.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/91744" target="_blank">📅 12:54 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91743">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔻
وزارة الدفاع الأفغانية:
مقتل 28 مقاتلا بعد عبورهم من باكستان إلى شرق أفغانستان.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/91743" target="_blank">📅 12:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91742">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/naya_foriraq/91742" target="_blank">📅 12:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91741">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
‏أجلت الشرطة منازل بالقرب من قاعدة فيرفورد الجوية التابعة لسلاح الجو الملكي البريطاني، وهي قاعدة جوية أمريكية في إنجلترا، وألقت القبض على عدد من الرجال للاشتباه في ارتكابهم جرائم تتعلق بالمتفجرات. وتستخدم القوات الأمريكية هذه القاعدة خلال الحرب مع إيران.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91741" target="_blank">📅 11:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91740">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🇮🇷
قائد الجيش الإيراني:
الحرب لم تنتهِ؛ وعلى العدو المعتدي أن يستعد لتلقي ضربات قوية.
إذا كان هناك عدم أمن في المنطقة، فسيكون هذا عدم الأمان للجميع.
لقد رأيتم أن التعاون مع الولايات المتحدة لا يخلق الأمن. الأمن في المنطقة يكمن داخل المنطقة وبأيدي دول المنطقة.
لن يتحقق الأمن في المنطقة إلا بإزالة الولايات المتحدة والتخلص منها، وكذلك من إسرائيل، من المنطقة، وهذا الأمر ليس ببعيد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/91740" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91739">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91739" target="_blank">📅 11:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91738">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔻
الشرطة البريطانية:  حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.  اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.  إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/91738" target="_blank">📅 11:33 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91737">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba0e6879a.mp4?token=M0Iv1bYMAuaAXUZNZrV2kYh5Evo2QIih2pv-DV0o0crnZb--mg9p6eKbkENdoV53ylnk7Ve030OiCdcy-aU6wpePu2y1l9T7Zm1feW1Ih82TlsP8PXxMd0TFBiHfMRt40UjPSEtiQA64XSpteEyq7OHOCQQbUEazqpeBVKRy0Hd14nLeGbkPirTkt2eAvcXkjV7VlM2vEg2qVQzHHJpF1JTEBvfnFWsLoQ328bFOUqdKfcZEdmOfHInl3lyVPYTtajHXdhzSahxg7YH2xglg_Mf4LTff0YlhTj2Hsr0Rl2yjTpCwcywifBR2aHpj3GYKY4Q96PbFEj1B2RHcJd0s6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba0e6879a.mp4?token=M0Iv1bYMAuaAXUZNZrV2kYh5Evo2QIih2pv-DV0o0crnZb--mg9p6eKbkENdoV53ylnk7Ve030OiCdcy-aU6wpePu2y1l9T7Zm1feW1Ih82TlsP8PXxMd0TFBiHfMRt40UjPSEtiQA64XSpteEyq7OHOCQQbUEazqpeBVKRy0Hd14nLeGbkPirTkt2eAvcXkjV7VlM2vEg2qVQzHHJpF1JTEBvfnFWsLoQ328bFOUqdKfcZEdmOfHInl3lyVPYTtajHXdhzSahxg7YH2xglg_Mf4LTff0YlhTj2Hsr0Rl2yjTpCwcywifBR2aHpj3GYKY4Q96PbFEj1B2RHcJd0s6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
على الرغم من الحصار الجوي الظالم..
رحلات الإقلاع من مطار الإمام الخميني بالعاصمة الإيرانية طهران تتم وفقًا للجدول الزمني المحدد.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/91737" target="_blank">📅 11:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91736">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔻
الشرطة البريطانية:
حادث كبير قرب قاعدة جوية أمريكية في منطقة ويلفورد بالمملكة المتحدة.
اعتقال عدد من الأشخاص للاشتباه في ارتكابهم مخالفات بموجب قانون المتفجرات في ويلفورد.
إجلاء السكان من محيط قاعدة جوية أمريكية في ويلفورد ونقلهم إلى مركز ترفيهي قريب.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/91736" target="_blank">📅 11:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91735">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي في هذه الأثناء يتسبب بإنفجارات عنيفة وسط العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/91735" target="_blank">📅 10:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91734">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇱
جيش الإحتلال الإسرائيلي يزعم:
إطلاق مسيرة انتحارية من قبل حزب الله نحو قواتنا في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/91734" target="_blank">📅 09:58 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91733">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇱
وزير المالية الصهيوني:
يجب على إسرائيل الذهاب إلى الحرب في الضفة الغربية كما فعلنا في غزة.
يجب ضم جنوب لبنان والأراضي التي يسيطر عليها الجيش الإسرائيلي في غزة.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/91733" target="_blank">📅 09:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91732">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=UQXkzdMgSl9xmHONCYcCI6jFLPl-tmlUw9EgxAOIyeHq77Zm8bA0OckrWii40szjONHxT-nZfQTw0JjkbCaJrSmLyIriTiLX24nq0oD67dcRPpvX-xZwcLIOFqYJT7DchXhKRwpbl62CQdD_Fbqk5uk3FaFJyWh6DQK49djCyPVecfsorgS_9jV6i681CAcedvc2Co_2l3ijjARLpO-8hrDDS17uvmBeN3_6CYjfkwq6pCLH_bBZiSgfCVJ8edZn4aZqIJyIBuw7ZnRirBpRvUhhHvFDgYKpejWq107-Q28edOiuJ5MzI3SD5s7b2ulerZw0yVArFqwpeP7voWPZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d786ee0c.mp4?token=UQXkzdMgSl9xmHONCYcCI6jFLPl-tmlUw9EgxAOIyeHq77Zm8bA0OckrWii40szjONHxT-nZfQTw0JjkbCaJrSmLyIriTiLX24nq0oD67dcRPpvX-xZwcLIOFqYJT7DchXhKRwpbl62CQdD_Fbqk5uk3FaFJyWh6DQK49djCyPVecfsorgS_9jV6i681CAcedvc2Co_2l3ijjARLpO-8hrDDS17uvmBeN3_6CYjfkwq6pCLH_bBZiSgfCVJ8edZn4aZqIJyIBuw7ZnRirBpRvUhhHvFDgYKpejWq107-Q28edOiuJ5MzI3SD5s7b2ulerZw0yVArFqwpeP7voWPZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اللاعب زيدان اقبال: الكويتيين يطلقون تعليقات عنصرية، أنا أفوز، إذا أحتفل. هذا شيء طبيعي. لا أعرف لماذا يأخذون الأمر بحساسية بالتأكيد سأحتفل.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/91732" target="_blank">📅 04:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91731">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/91731" target="_blank">📅 03:48 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91730">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OHsD4jA6IVDqVbrZcfZ6saWjup3Yr-m9egWVFiCOdOYyPO4wYpojq7P7GeBgzSv1_-ntr__BI59taaoGMe8LHvgfxF3z0hrj2PnTp3XvRsc0l8HnaDLPMFh54gnvj2N9-jXbk3u8q8VDzCaRUVOPQjMWe9VJYQMW4ulpzXPOW6XGiiODZzRozJNphe0jojsaSDDtqhyiZFdpKONEv-A6T6TXvLgZ-sUmFwWhwhGD4N_tO3yeMwX7ZSEWKBWmaGI5Bw2ob2eQU9HFn-SUujvQdFME3714jG1kCv4aYDzvsN61ag5y-fqW5DgAU-CUsClwneWn1YU0iaSBrRWKZpvTqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">النظام السعودي يختطف المشجع العراقي (رسول ابو القوزي) وينقله لجهة غير معروفة</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/91730" target="_blank">📅 02:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91729">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=QJDdDqTqPfdz4AaeYOWa-PtXjme8WcmHrNTyidle6Xbn89O-IBvGE2lJUI6ilcEC16qlrF2xrw5iKUxQyQN_nVzl6QyxbTOL08SQOJUHoS3FM-MAW_AhJfdMlA2UndxDxiLfh8G6oc8fQ8Xow3Pbz-iNCewUbbutXZs_BbmIxA3U0lB7dSlzfovpJQQTbrDdM2zplfmRvYdu8ZNByj0zWFw0_I7ji65WPXA82vscJhIrfPhMjcdiKWfMhzZe9L__BfSV3-u3JkJh1oST_eFZa3FMPNvJ-Gv3RJXb85FRmCzSFrQKQVQqw9dN67NC7dwIJoZPAmCdw6WlB4r1wD1mNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e19c52d6.mp4?token=QJDdDqTqPfdz4AaeYOWa-PtXjme8WcmHrNTyidle6Xbn89O-IBvGE2lJUI6ilcEC16qlrF2xrw5iKUxQyQN_nVzl6QyxbTOL08SQOJUHoS3FM-MAW_AhJfdMlA2UndxDxiLfh8G6oc8fQ8Xow3Pbz-iNCewUbbutXZs_BbmIxA3U0lB7dSlzfovpJQQTbrDdM2zplfmRvYdu8ZNByj0zWFw0_I7ji65WPXA82vscJhIrfPhMjcdiKWfMhzZe9L__BfSV3-u3JkJh1oST_eFZa3FMPNvJ-Gv3RJXb85FRmCzSFrQKQVQqw9dN67NC7dwIJoZPAmCdw6WlB4r1wD1mNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🫡
هَلْ جَزَاءُ الْإِحْسَانِ إِلَّا الْإِحْسَانُ
@Naya_Press</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/91729" target="_blank">📅 02:36 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91728">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
🇺🇸
اصوات انفجارات لم تعرف طبيعتها قرب قشم</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/91728" target="_blank">📅 01:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91727">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇺🇸
الإعلام الأمريكي:
أعلنت وزارة الدفاع الأمريكية عن وجود معلومات استخباراتية محددة وموثوقة تشير إلى وجود تهديد لقاعدة سلاح الجو الملكي في فيرفورد، وقد رفعت مستوى الحماية الأمنية للقاعدة (FPCON) إلى أعلى مستوى، وهو مستوى "دلتا".</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/91727" target="_blank">📅 01:18 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91726">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
🇺🇸
اصوات انفجارات لم تعرف طبيعتها قرب قشم</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/91726" target="_blank">📅 00:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91725">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c050b97ca.mp4?token=YttThj79bHMvDv4RMTjg5Ho-s5JQrtouoOxI-Sj_a7G4zjvaELL8gzQxrT3tGswEXyGWnQWQA-VbWfNrGCIt9_dMcRwEnbzcDEvaVyky924mQRBQ6V_4BXpauKvC4xEeIDDS0zwPdnco2ZGq-wOTZMQ4sMUK89qsdGji7yxakdqJVgfWMKQW0Z-unmLvfIM4z0vsDCZljUpSlxwusTFiPhbveTKAYAnzWgNn_O5ATx6jLPNiRSKa-802URRKlRU65WbSLT01gY7bMt-_xnKdBYTQRXbB0H3oe6S-W8S8Z5_P66Fsy02qdwagYcv_4URlEVX0QSNc5e93cUj_rWnN7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c050b97ca.mp4?token=YttThj79bHMvDv4RMTjg5Ho-s5JQrtouoOxI-Sj_a7G4zjvaELL8gzQxrT3tGswEXyGWnQWQA-VbWfNrGCIt9_dMcRwEnbzcDEvaVyky924mQRBQ6V_4BXpauKvC4xEeIDDS0zwPdnco2ZGq-wOTZMQ4sMUK89qsdGji7yxakdqJVgfWMKQW0Z-unmLvfIM4z0vsDCZljUpSlxwusTFiPhbveTKAYAnzWgNn_O5ATx6jLPNiRSKa-802URRKlRU65WbSLT01gY7bMt-_xnKdBYTQRXbB0H3oe6S-W8S8Z5_P66Fsy02qdwagYcv_4URlEVX0QSNc5e93cUj_rWnN7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
تغطية قناة نايا للاحتجاجات في محافظة البصرة جنوبي العراق رفضًا لتشديد الخناق على الجمهورية الإسلامية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/naya_foriraq/91725" target="_blank">📅 00:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91724">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
مجلس الوزراء العراقي يقرر تعطيل الدوام الرسمي في مؤسسات الدولة ابتداءً من يوم الأربعاء المصادف 30 أيلول ولغاية يوم السبت 3 تشرين الأول المقبل، احتفاءً (بأيام السيادة) لجمهورية العراق.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/91724" target="_blank">📅 23:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91723">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71ffae4249.mp4?token=fOFFjUm366XVER11eTDhRZqw7yy-slWNMm-KqxP7FufcPbVPscT8tNPCNkqSH-U1_jBDo4QhT8DI12O2Xi29uJLLIV5aGoa8vE53upXVQ_azOc1EMaBq3U9KxDwxlAuopqJmB8QMhVUpgakj8odgvzvOB5kLi1NTQTSI7P6YnjhF5KfhqMrHwJDb3cUwH-KbDKQc3a_Tw4CQ4faVAZn2bJCxHMLb_md9Xd7hVb4K1hmjZulBOCbXtc4gcfbwP2Dj74DFVMQbuoG64qc4UR6-fkk5S33XPyzhjNdb10ECmhGryhe38CJPoeK2S46on79DyrHOKS8oILBrc-wNMHaCjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71ffae4249.mp4?token=fOFFjUm366XVER11eTDhRZqw7yy-slWNMm-KqxP7FufcPbVPscT8tNPCNkqSH-U1_jBDo4QhT8DI12O2Xi29uJLLIV5aGoa8vE53upXVQ_azOc1EMaBq3U9KxDwxlAuopqJmB8QMhVUpgakj8odgvzvOB5kLi1NTQTSI7P6YnjhF5KfhqMrHwJDb3cUwH-KbDKQc3a_Tw4CQ4faVAZn2bJCxHMLb_md9Xd7hVb4K1hmjZulBOCbXtc4gcfbwP2Dj74DFVMQbuoG64qc4UR6-fkk5S33XPyzhjNdb10ECmhGryhe38CJPoeK2S46on79DyrHOKS8oILBrc-wNMHaCjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
تغطية قناة الميادين اللبنانية للاحتجاجات التي خرجت في العراق تنديدا باغلاق حركة الطيران المدني مع الجمهورية الاسلامية الايرانية.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/91723" target="_blank">📅 23:25 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91722">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇮🇷
🇮🇶
الشيخ محسن الاراكي:
بسم الله الرحمن الرحيم
قال تعالى:  والذين كفروا اولياهم الطاغوت
ان ما قامت به الحكومة العراقية من سد الطريق أمام زوار أمير المؤمنين والامام الحسين الشهيد جعلت من الحكومة العراقية الحالية ذيلاً ذليلاً من ذيول الطاغوت الامريكي شأنها شأن ساير الطواغيت الذين حكموا العراق مما يسلبها كل مقومات الشرعية الدينيهة وعلى هذا فاإن اصرت هذه الحكومة على سياستها الطاغوتية وانصياعها المطلق للطاغوت الامريكي فهي كسائر الانظمة الجائرة الطاغوتية ويترتب عليها كل احكام الطاغوت ويحرم على المسلمين التعامل معها كنظام شرعي بل حكمها حكم النظام الاموي وما شاكله من الانظمة المعادية لرسول الله صلى الله عليه واله واهل بيته الطاهرين عليهم الصلاة والسلام والحكام الطواغيت الذين يجب اجتناب التعامل معهم كما قال سبحانه وتعالى ولقد بعثنا في كل امة رسولاً أن اعبدوا الله واجتنبوا الطاغوت فمنهم من هدى الله ومنهم من حقت عليه الضلالة فسيروا في الارض فانظروا كيف كان عاقبه المكذبين.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/naya_foriraq/91722" target="_blank">📅 23:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91721">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/153b76ec5b.mp4?token=jBbfWXM-OiDRKA1WtvjKj1T24hmWsRT0rhvsSVTrvVY75Bnusu0_ChgT8eqU5-WWWeiC1r2crU1iG9vsNuMYmCNFxp1nfjRNmQ9iOQBijZ-m3IFmrcF0hgxhicLooRXz-TUkrmeG1EUSYfe8Ud9_BywFfa2gU_Gy1xGu5kLw9vVqkg54Rio5CTeglAoaI-QGy2cbpxfyAuwZfwxbyQdhhTXFlTPhODLHPn3CQRwM2js5AcQOoL9I_eK-rLpgHaF5zbpUUrbRSF093FM_2SZUKyIvi_PKsUZAldaL-5RAQEaCyj7yPNjXO_nc_nsYeuYAmhLtqdgrxLfxaYifRMX1OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/153b76ec5b.mp4?token=jBbfWXM-OiDRKA1WtvjKj1T24hmWsRT0rhvsSVTrvVY75Bnusu0_ChgT8eqU5-WWWeiC1r2crU1iG9vsNuMYmCNFxp1nfjRNmQ9iOQBijZ-m3IFmrcF0hgxhicLooRXz-TUkrmeG1EUSYfe8Ud9_BywFfa2gU_Gy1xGu5kLw9vVqkg54Rio5CTeglAoaI-QGy2cbpxfyAuwZfwxbyQdhhTXFlTPhODLHPn3CQRwM2js5AcQOoL9I_eK-rLpgHaF5zbpUUrbRSF093FM_2SZUKyIvi_PKsUZAldaL-5RAQEaCyj7yPNjXO_nc_nsYeuYAmhLtqdgrxLfxaYifRMX1OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/91721" target="_blank">📅 22:58 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91720">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/003d924fe5.mp4?token=P6rLTAywyaOK4adk2GcsQdn2uYNtyqWebl5wdlxPU0Bz7cFIZpUEDDNgB4NFJgE68yKPHe26uJQCaRtcTXOk-J18wpyicALQYnNF8mwij_mzwZ5_YV_EOtREBQTpRB-ZUDmEHCRmeaWp6FSxYWEjqR1Frj-LlIaJGQLUWdBl09lDleCfWh2f3yylCGHLLS_uod22MOVVMCO1COkELL8Xv4FOURIvJSWfUzFvKgj-5U4sA9pZkekkWYTsG_K_WK0XoyLjQsdvxLafBC1lRQtCC8OVWajuhgWSRWPrzuZImQ62H1j7df1dGjzkEQivMiE8JoENb5Yri_xesk9cAWY_RSvOQfkTgIpn6E1WdyJ9VqHy1BktK4D2YmkZXF2kRuHc5TfNAgGmg_7yUKfGR1fgGe3x3xNg4ybSKbGimi7FYAgta8-WtUSi9tJXocic-zv-wdRDRQX9X7jG8vnwVfAszky1KKSndpnnCEO3Fafo6l7DrvxHPic2bgr-DVWAbveoGb0FLbzLJe0D6ymx6GbtiA9TL8FueNXP8jKeeMx-W7BYl7u3EgJZBDhc4ssMywfGwPv3r3_0LJGeVQIMYue31lC6LyQSFpuxnCmnpS3M0gGcgi1rd_AGUxzFofqCddkl8_iVPKbIUdeXnU24RVNgmZTeR3vpaV5yO_8ozJwvQTk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/003d924fe5.mp4?token=P6rLTAywyaOK4adk2GcsQdn2uYNtyqWebl5wdlxPU0Bz7cFIZpUEDDNgB4NFJgE68yKPHe26uJQCaRtcTXOk-J18wpyicALQYnNF8mwij_mzwZ5_YV_EOtREBQTpRB-ZUDmEHCRmeaWp6FSxYWEjqR1Frj-LlIaJGQLUWdBl09lDleCfWh2f3yylCGHLLS_uod22MOVVMCO1COkELL8Xv4FOURIvJSWfUzFvKgj-5U4sA9pZkekkWYTsG_K_WK0XoyLjQsdvxLafBC1lRQtCC8OVWajuhgWSRWPrzuZImQ62H1j7df1dGjzkEQivMiE8JoENb5Yri_xesk9cAWY_RSvOQfkTgIpn6E1WdyJ9VqHy1BktK4D2YmkZXF2kRuHc5TfNAgGmg_7yUKfGR1fgGe3x3xNg4ybSKbGimi7FYAgta8-WtUSi9tJXocic-zv-wdRDRQX9X7jG8vnwVfAszky1KKSndpnnCEO3Fafo6l7DrvxHPic2bgr-DVWAbveoGb0FLbzLJe0D6ymx6GbtiA9TL8FueNXP8jKeeMx-W7BYl7u3EgJZBDhc4ssMywfGwPv3r3_0LJGeVQIMYue31lC6LyQSFpuxnCmnpS3M0gGcgi1rd_AGUxzFofqCddkl8_iVPKbIUdeXnU24RVNgmZTeR3vpaV5yO_8ozJwvQTk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
مشاهد من جانب المليشيات الموالية للسعودية للصواريخ الجوالة التابعة للقوات المسلحة اليمنية وهي تتجول فوقهم تتنتضر اللحظة المناسبة لكي تنقض عليها.
https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/91720" target="_blank">📅 22:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91719">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">امر مستغرب جدا   لا موقف """جدي """ عملي معلن من قادة الإطار التنسيقي الشيعي حول ما يجري بمطار النجف ؛ الإطار هو الذي  أتى بالحكومة ؛ و لا نريد تغريدات لكون البيانات لا تغني ولا تسمن     والعتب الأكبر على من نحسن الظن بهم الشيخ همام حمودي ؛ السيد هادي العامري…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91719" target="_blank">📅 22:33 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇶
أنباء أولية تشير إلى غياب عدد من لاعبي المنتخب العراقي عن المباراة المقبلة إثر الاعتداء الذي تعرضوا له.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/91718" target="_blank">📅 22:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db08d7c938.mp4?token=ZUE_aTyXNIfcWoJH9kkzWsZ0pPvR035m43tgl4b8_KDU5_Nspx6BSIPOQtGzzC22lNJ2NcgYvasmRXQKzIqvKhD3RfzmcZFAuxWaquH1p0V5C9U1Q3J_-bYdbzaW2yD7n3dr0hbULPe25squso5g_oeXYLTxGj3oJH6_lJtmb7jbiEVwpuYvBHxYypLrDgR9zxDSbO25lBWCHfksODtOT6XBXYUdsQ0dNt6a0v_FUDE1gBJIePRt2s1VBQ50faBFwIatLRrTD4CuZHAzdnj3ZU63QIxLrpTo1puEosZ-ZkxghPuQjZBmjJxgKY4JV2aN2LUZXfW8rp0IhC-ZZ6m70w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db08d7c938.mp4?token=ZUE_aTyXNIfcWoJH9kkzWsZ0pPvR035m43tgl4b8_KDU5_Nspx6BSIPOQtGzzC22lNJ2NcgYvasmRXQKzIqvKhD3RfzmcZFAuxWaquH1p0V5C9U1Q3J_-bYdbzaW2yD7n3dr0hbULPe25squso5g_oeXYLTxGj3oJH6_lJtmb7jbiEVwpuYvBHxYypLrDgR9zxDSbO25lBWCHfksODtOT6XBXYUdsQ0dNt6a0v_FUDE1gBJIePRt2s1VBQ50faBFwIatLRrTD4CuZHAzdnj3ZU63QIxLrpTo1puEosZ-ZkxghPuQjZBmjJxgKY4JV2aN2LUZXfW8rp0IhC-ZZ6m70w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/91717" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91716">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ecfe6219e.mp4?token=lxUcOkY6OmeVwfHLZmi-HL4TDrqOwj-aaRhCbASEarNgkDNPDf2CXVFAFhGXQqxbjgoV7sm7kV6kiUDIP1zdXRVLgk1l57MIY5lTUs7bS5pbrMDqGDLMCIILL4uNqBT_JLQJ1uK8I7hgT0I0FiiQGGGJB-e31cFi7-Esn0FjEnDxeysreuKnqpN0hUpnS2TeJfxC9LYn7tJeXxWdWSDyaQqTTq96upjO-P1ITKGe_Kk1wURFViG73MUEG6sUwBJEVxBa09Wj1R2KOF3UGMjLALkLNmXhU3WXMRj_GF-DCP5mKElpPioTfEzmMDJXC1nXFlyFtmgYUW0cxKAGVOBz5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ecfe6219e.mp4?token=lxUcOkY6OmeVwfHLZmi-HL4TDrqOwj-aaRhCbASEarNgkDNPDf2CXVFAFhGXQqxbjgoV7sm7kV6kiUDIP1zdXRVLgk1l57MIY5lTUs7bS5pbrMDqGDLMCIILL4uNqBT_JLQJ1uK8I7hgT0I0FiiQGGGJB-e31cFi7-Esn0FjEnDxeysreuKnqpN0hUpnS2TeJfxC9LYn7tJeXxWdWSDyaQqTTq96upjO-P1ITKGe_Kk1wURFViG73MUEG6sUwBJEVxBa09Wj1R2KOF3UGMjLALkLNmXhU3WXMRj_GF-DCP5mKElpPioTfEzmMDJXC1nXFlyFtmgYUW0cxKAGVOBz5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر من الملعب لنايا: التوترات بدأت حينما هتفت الجماهير الكويتية ضد لاعب منتخبنا الوطني زيدان اقبال ووصفه بالباكستاني مما ادى لتوتر الاجواء</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/91716" target="_blank">📅 22:24 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/91715" target="_blank">📅 22:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">رمي قناني المياه وتمزيق ملابس المنتخب العراقي على ايدي المنتخب الكويتي وكادره الفني  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/91714" target="_blank">📅 22:19 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ab243b15e.mp4?token=o4cgihJnGzRTr6o6F7CvvTgMLNMMQnCPGvgR5CbF9u6k9sAjHWIv-YwkZfhN6NG03lCaweXkW-0Kx8Mn4oJ2XiNXOGrKEvW_-RRUF95bGY4SLHVzxnLJ9ByMa_SiTnDeXh4x6Rf3Rgv3Iwrs6MBhzrPcb9GHazFT5S0IUu7djS26C_iQbZ_MOGur3oqBkFn5d4qvNvjPQAKDpAOrYUf28cn01b02gkgIDYwp7riLMmC1MJIUB4WvRdpKmrw8bzMaEyUvZKUPe8S4AYUsyUXYVTHoTgwwdWAHnYEMzjIs_ijUXpbqn6HHQGaptxG4j8zFP_ikEI5efuRAPVW4Qi0Xig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ab243b15e.mp4?token=o4cgihJnGzRTr6o6F7CvvTgMLNMMQnCPGvgR5CbF9u6k9sAjHWIv-YwkZfhN6NG03lCaweXkW-0Kx8Mn4oJ2XiNXOGrKEvW_-RRUF95bGY4SLHVzxnLJ9ByMa_SiTnDeXh4x6Rf3Rgv3Iwrs6MBhzrPcb9GHazFT5S0IUu7djS26C_iQbZ_MOGur3oqBkFn5d4qvNvjPQAKDpAOrYUf28cn01b02gkgIDYwp7riLMmC1MJIUB4WvRdpKmrw8bzMaEyUvZKUPe8S4AYUsyUXYVTHoTgwwdWAHnYEMzjIs_ijUXpbqn6HHQGaptxG4j8zFP_ikEI5efuRAPVW4Qi0Xig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الاستفزازات التي قامو بها لاعبين المنتخب الكويتي للجماهير العراقية  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/91713" target="_blank">📅 22:18 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ع المطار يالكويتي  …</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91712" target="_blank">📅 22:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lm3LAOp9_XJ2wBpunr6BjKoZnZtHK00cGf130gAOQ5MZYD9xkyzUHKR1NfQ6uq4w4XTRI3iSFXoTpQkKGv-SnuH-3vOBKSOktSPhHbS82set60ivZBimw_wKm53pWCNJg2v_Jfqge7cUXnO1cBRViUaOnlvj-_n7sEYyz28L_VmE1iJpSazCi1UjQlzziZulXVL04q8OsRHn9H82QptWoOSXkjAJ1UYUqNV54eT3KCah0qt-mhmwSske6_AcoLnyz2TmyMqYthIE9YmV0d1zs4RFTSHtgyb9lqzveRx9gLaKCCZOL5vPLe9oAVltO-Wy4ceuN3el-ZNf5K39UJyfrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/91710" target="_blank">📅 22:14 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91709">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdGA3yuaUptYrzObZtbu7MStfZR0QXP33ioaogzMS3WIEEYE7pzA0ndw-CWo1aJwudF7pPMFPOIoCtvj7h8zt8tjc3hCQmKXNM9iY9Ys7J9YmxpETFnHdM60lDAHod3nPO2B7aq6BIJpA3kP3EdOpntaO72nK0bHthxW0BaFBwhR-Zl1TscvHkJkGLLEBPJj5afJnNXJoPiaVoryeBM7yfSRlZalFOSgPlCrGpvR1vVaAoAjoJjsLdkBYtSqPvQghRitKH11HKagC6LE4ZdO4krzmLEdNxwd9b0NRcxwPn2IVhLDzkNIOBaRUkeXMNtE93KtSLnl3tmjQrRMfKhxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واعرقااااه   تعرض ألاعب ايمن حسين للضرب والتدافع على يد لاعبي المنتخب الكويتي في السعودية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91709" target="_blank">📅 22:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91708">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e722e77e90.mp4?token=llqH5ezOqXXjgTzHxsYKgWr5URnQ2j1e-B735vlsAqKQJOqFe4tBYL8BCX8fzwLcSCi73vas-I0qZtBxkyJrj5QcqAuGe77H2rs25WLt2mf-RctcDPnFkG848SQwKBBofEqyNCSJM5H5PBpH8s0Lrp9UG5AUt1M0AS7afoeAyz3TaNfC-pYMRfSunpwoDUtqq8JtrCQ_-xSm9afy365cCa8cmPlTDCG3IqrnNC2s_aQSTLlaUKRWJ_sNQXs5ItsgdvuyGLh3SbaBw25_VARUMt5zmcAFmYcnv_7R-U2lbG0WwcWtvQj9FOGvXrAgB0ynpnoqy7BxQ92TGqS8uRbY4FX_AbvjGDNsF2o20wgvFEQ5wk7KRr_a9UsPjsHmGeQPP4pL6utvhoWQRN-MbXCAhri_VffFaOk9H1XjaKA9Ab6mTZRLeQxDl15zGvhYLIbk9TI_RN7w9tjJkpwnLpej6j33f8otfmq7QqRXlIzGP1CowGxguiaUVIcydErUEJCIiL7AjVOZz3k7X4E90q9uPTP7zjggvJoOC2bjuBmpdMB8j9Yxv37z6HILp5SFTfssQVhFJoQsJh4Qwvgb5M0z6zfAYMcP2UTi4dv4kupZeiboB6P3qrjd0HS4-WZeH0rq4uRmGMa7GmS7l5ijaP_nxDejugxKh27EA2ZVvC_l3PU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e722e77e90.mp4?token=llqH5ezOqXXjgTzHxsYKgWr5URnQ2j1e-B735vlsAqKQJOqFe4tBYL8BCX8fzwLcSCi73vas-I0qZtBxkyJrj5QcqAuGe77H2rs25WLt2mf-RctcDPnFkG848SQwKBBofEqyNCSJM5H5PBpH8s0Lrp9UG5AUt1M0AS7afoeAyz3TaNfC-pYMRfSunpwoDUtqq8JtrCQ_-xSm9afy365cCa8cmPlTDCG3IqrnNC2s_aQSTLlaUKRWJ_sNQXs5ItsgdvuyGLh3SbaBw25_VARUMt5zmcAFmYcnv_7R-U2lbG0WwcWtvQj9FOGvXrAgB0ynpnoqy7BxQ92TGqS8uRbY4FX_AbvjGDNsF2o20wgvFEQ5wk7KRr_a9UsPjsHmGeQPP4pL6utvhoWQRN-MbXCAhri_VffFaOk9H1XjaKA9Ab6mTZRLeQxDl15zGvhYLIbk9TI_RN7w9tjJkpwnLpej6j33f8otfmq7QqRXlIzGP1CowGxguiaUVIcydErUEJCIiL7AjVOZz3k7X4E90q9uPTP7zjggvJoOC2bjuBmpdMB8j9Yxv37z6HILp5SFTfssQVhFJoQsJh4Qwvgb5M0z6zfAYMcP2UTi4dv4kupZeiboB6P3qrjd0HS4-WZeH0rq4uRmGMa7GmS7l5ijaP_nxDejugxKh27EA2ZVvC_l3PU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
بعد ممارسته حقه في الاحتفال... المنتخب العراقي يتعرض للضرب من قبل الجماهير والكادر الفني الكويتي خلال بطولة كأس الخليج في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/91708" target="_blank">📅 22:12 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-91707">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇮🇶
بعد ممارسته حقه في الاحتفال... المنتخب العراقي يتعرض للضرب من قبل الجماهير والكادر الفني الكويتي خلال بطولة كأس الخليج في السعودية.  https://t.me/naya_foriraq</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/91707" target="_blank">📅 22:09 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
