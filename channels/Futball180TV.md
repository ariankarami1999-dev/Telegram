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
<img src="https://cdn5.telesco.pe/file/JkBV9mzjV0n9C3fXO9niaoF-EThvUJAf-izogvPo62qWN5ACUwmvBQruXYpdaXvU2uWGQWjZD9_-l1GqLP6ULrwej-KlEmAC9UPWWtB32t-HhSvrm7klRVE8ZVo3Svi5UFzUxioQqiWcfaP7pVYAiKPYVQJS1NUDzB16TpoW4t-X0yPHSmN0CLfucMUz5SvV6fR0kyA4D9SmOuzuqPLa7I20jmx0XQP4CDpGybqKns4kHDbK_AR2xW0ANSsBGRpBUDXq645M2Setl_KAijGaoErbpHX0LXuD6yUpWdyUGGxptAgW2PCSZ_BPPl_0x_qCkza3qpQlnCFCigQEmgK19Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 396K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 19:40:29</div>
<hr>

<div class="tg-post" id="msg-107562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=G27Y32x6QbcvqT-SjyZf86ZBAIi5bKCfUYUly5ghsvX_Tyi4Hu43GC4kECWrc8rEXEvjeyAplQFEA7sK9kwFrloezNvfk1y5-TVZLe7IsY9NBKAj9NQhHNLMUhPJj3um5twFBzm7qrXfa30yXnASRMUaxtWYYDUhD9J6BLG2-vNG04422fjYl81PdpsLoM0aSDSJB0yYd444x1Mtjv_prI0hDi01hyP46gTatQyD7dyeWPKj7b6Nm8D-9ctDMH82SZyHnsWYXLvVSLVdvGECIbBQoW_30cGYm1PqDqhF2MzT2P7P_4uhJ2xLbZVMYVLluCkuY-dtXj4fKJ2MS8ZTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a3b8520f3.mp4?token=G27Y32x6QbcvqT-SjyZf86ZBAIi5bKCfUYUly5ghsvX_Tyi4Hu43GC4kECWrc8rEXEvjeyAplQFEA7sK9kwFrloezNvfk1y5-TVZLe7IsY9NBKAj9NQhHNLMUhPJj3um5twFBzm7qrXfa30yXnASRMUaxtWYYDUhD9J6BLG2-vNG04422fjYl81PdpsLoM0aSDSJB0yYd444x1Mtjv_prI0hDi01hyP46gTatQyD7dyeWPKj7b6Nm8D-9ctDMH82SZyHnsWYXLvVSLVdvGECIbBQoW_30cGYm1PqDqhF2MzT2P7P_4uhJ2xLbZVMYVLluCkuY-dtXj4fKJ2MS8ZTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
دیس ژوله به قائدی و قیاسی؛ ژوله وسط برنامه زنگ زد به قیاسی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/Futball180TV/107562" target="_blank">📅 19:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvaI2WKINaW2L4un51WnMaBUA_2bn8duQPyWYEy20K6H2Ay_tBDv_ip5YefpJ8Q-zbSDh050-KxvOYHiUneDl8oOVE8ci5hm4gBFBGxj-JZTuGRChE_EYQWf9VQhdEbNO8nMLZ7D5zq-xAIsfE0rZxLwrzNczkzSrNMifiFOwyOF15I-jumNNel8lGw6t0LmYsld2VWQSwgaBXNsJdR2B56upIxjI00FFeorUx_O_SS9TXN_jhhDrgXsma1APBRL7UbiyD0_dmz7fv_A4Yv3lIK8Cz4gLmpc8KBSzUmOpMWhXN440rqaA1uWsWvN9w-zpYvzqijVEs1rOF3REmpKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
ژرژ ژسوس سرمربی پرتغال: رونالدو در بازی فرداشب مقابل دانمارک بازی نخواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/107561" target="_blank">📅 19:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=urHcw09aZGjwONGeLRcttK-qs3k5qwTWnIAens8qQrTG4vivf9oNbRuh8F_u69U6cav1lV-Nis-TQZZm5rTkGhO2jbPTEPxhBHDKvg-OGVLtSODUqWdA2bQwxBHTSHhJ972QdEMwUIWe4zFmB1cAu7PFO7OD7mpNXGgd3xm-ir1_asPObEtNHFK__E-7eBhEQ_ycPyZRbv6rgn8RliEeucjD4zvLZ_m4_1VFPRxDH-sCmC8JMfecaMOai6RMgmsuZCHvWHEbQiUers66OpSYXUIfWs_Dsy5nHlLTbVWXZz_tdOqluZ2BOPKTdepBKCfc2AmejYAEK7m_IcC1WQgSiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d3104ad6.mp4?token=urHcw09aZGjwONGeLRcttK-qs3k5qwTWnIAens8qQrTG4vivf9oNbRuh8F_u69U6cav1lV-Nis-TQZZm5rTkGhO2jbPTEPxhBHDKvg-OGVLtSODUqWdA2bQwxBHTSHhJ972QdEMwUIWe4zFmB1cAu7PFO7OD7mpNXGgd3xm-ir1_asPObEtNHFK__E-7eBhEQ_ycPyZRbv6rgn8RliEeucjD4zvLZ_m4_1VFPRxDH-sCmC8JMfecaMOai6RMgmsuZCHvWHEbQiUers66OpSYXUIfWs_Dsy5nHlLTbVWXZz_tdOqluZ2BOPKTdepBKCfc2AmejYAEK7m_IcC1WQgSiYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های ژوله‌درباره جنجالی هوش‌مصنوعی در ارتباط با سربازی علیرضا بیرانوند
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/Futball180TV/107560" target="_blank">📅 19:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=J5O2KgHwk_UJdfQB-y3oI0YhV25si0xnMbUt5leguxBd6isZQUlyXdDXRfKhPeQXFHqJJZ-J7o37NoCO0kalPecpIv6SBWqBtkpyn_zJx9Ow2yw32p_-0nrc5sSWUIpdCWMJQjfbxINTmGHtm3VNie0GOyY9DRGwe97ExwTmhDSn2M84u6NFeOh1UAwF254AvXj4g3rSqPYJ5jSOpylh5NM4w9m0SbF9LUT9dMMlztf12gxWWIrnjZVx7wa58iqeZbIlDeCe9mN6FVuXJQXuynIZL05Io1XOu53Z7t8AtCut0FyJrVfoHeDKzHlI5N5Ng1RWyM4kq7ImTpFMAk4qUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80e7cfe3bf.mp4?token=J5O2KgHwk_UJdfQB-y3oI0YhV25si0xnMbUt5leguxBd6isZQUlyXdDXRfKhPeQXFHqJJZ-J7o37NoCO0kalPecpIv6SBWqBtkpyn_zJx9Ow2yw32p_-0nrc5sSWUIpdCWMJQjfbxINTmGHtm3VNie0GOyY9DRGwe97ExwTmhDSn2M84u6NFeOh1UAwF254AvXj4g3rSqPYJ5jSOpylh5NM4w9m0SbF9LUT9dMMlztf12gxWWIrnjZVx7wa58iqeZbIlDeCe9mN6FVuXJQXuynIZL05Io1XOu53Z7t8AtCut0FyJrVfoHeDKzHlI5N5Ng1RWyM4kq7ImTpFMAk4qUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🎙
🇮🇷
شهریار مغانلو بازیکن تراکتور: زندگی کردن خیلی سخته؛ مردم نمی‌تونن خرید کنن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/Futball180TV/107559" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107558" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/Futball180TV/107558" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ugEbri3wXs9opFf_32OLeF7cLtciq-7ZBuVFWYYz6tBSWt7lCTq36rJ9wwfa5PXSBmlxt5tKiWIu8wkTQQVb1bbpu75QYBKCn5nByBaosQCswCgW5m1CBhMhI_MsC10J66MVb6RRSYG-A8CgnE9HSFwyxNBGLcpe_bSZlO-ondP6w_Z53TpViSCDKgSOOtFr8_Zlp5aMTdwqz0T2PmRPJoenW9AjsTEoVYhJKAu89iq2cNgUR3lz4uBaeDk2CMzlwSE90CXc90rZsxYf0YUTLLWqZ46ImFdgZonk8sG-WSS8-8fa3oP4qifNGsR4GfAemm1eTDDY-KfKgluiJ9bqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/Futball180TV/107557" target="_blank">📅 17:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‼️
آخرین وضعیت ورزشگاه مخروبه آزادی تهران!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/Futball180TV/107556" target="_blank">📅 17:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=LtmYLoDFXnFfNyN9unfkp4uiG5NzUz2dscn6v1qk-WXIKA7ZFDiqrcHLzEcqqQvYFJUEZ8luENMmWHqRTBF04rQ_be7vYaCtE0ur_Y8Wn3ylHV5vN07BBTdRdWOrTjn_vLBseLLqxNMiKS-f54dL8ndQxdcUdHUGLCvUq7ny1lY1vJ6pB0bBfzGo9Sx3hdkUc6itLGNZgf9g1vRfPwm37JAyQvbFeINmg8ohiBYkjnV0RI-cV3S1l0bVeIA6c6o1yRkGxWFMLLBgZt6Dm1-MSE1tZtsN9mB7oeGJergbJnZD7ZOtChxWpEOp0CctwzH24rfKLVmPH_DoIEWTJ_Kf8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2b8aa84ba.mp4?token=LtmYLoDFXnFfNyN9unfkp4uiG5NzUz2dscn6v1qk-WXIKA7ZFDiqrcHLzEcqqQvYFJUEZ8luENMmWHqRTBF04rQ_be7vYaCtE0ur_Y8Wn3ylHV5vN07BBTdRdWOrTjn_vLBseLLqxNMiKS-f54dL8ndQxdcUdHUGLCvUq7ny1lY1vJ6pB0bBfzGo9Sx3hdkUc6itLGNZgf9g1vRfPwm37JAyQvbFeINmg8ohiBYkjnV0RI-cV3S1l0bVeIA6c6o1yRkGxWFMLLBgZt6Dm1-MSE1tZtsN9mB7oeGJergbJnZD7ZOtChxWpEOp0CctwzH24rfKLVmPH_DoIEWTJ_Kf8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
دیس‌سنگین ژوله به حرکت کنعانی‌زادگان روی گردن عارف‌آقاسی در بازی دربی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/Futball180TV/107555" target="_blank">📅 17:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=Bh9gt6kUfnh-El4rSsB0U_NvvvdpNqjz6uHMpLKXlw9L_HkcEgLJ9uy8WyLjO6It1KaVC4eA0tcPTUl7-uvYvPw_ar7pV_BhPpIYUZdZ0JWts6ElMTo6sGlnqoB2k-6T-DobKlug1qnI570lRdy78hC1UdvmoWXKprzI05e2UF3vIajo88D90TFv6BOqt2-02mYfAmgf5cSDaLZ1png5UZMSJ919Xmn3I7fmReMO64pWeckfdNn0oiUB6IeaPopF1-3vYz2SyG7XE9hry7bwtpg5Fm0U55frdiztCSw085QfDjYiC2rDTdeUXkvbqqhr0H77jckSZepGp-zR-QRlUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71c4e91ce5.mp4?token=Bh9gt6kUfnh-El4rSsB0U_NvvvdpNqjz6uHMpLKXlw9L_HkcEgLJ9uy8WyLjO6It1KaVC4eA0tcPTUl7-uvYvPw_ar7pV_BhPpIYUZdZ0JWts6ElMTo6sGlnqoB2k-6T-DobKlug1qnI570lRdy78hC1UdvmoWXKprzI05e2UF3vIajo88D90TFv6BOqt2-02mYfAmgf5cSDaLZ1png5UZMSJ919Xmn3I7fmReMO64pWeckfdNn0oiUB6IeaPopF1-3vYz2SyG7XE9hry7bwtpg5Fm0U55frdiztCSw085QfDjYiC2rDTdeUXkvbqqhr0H77jckSZepGp-zR-QRlUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
واکنش‌ ابوطالب به صحبت‌های مسخره حسین عبدی پس از شکست ایران مقابل کره‌شمالی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/107554" target="_blank">📅 16:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=Ew5VT77OUNgncY5OHEmTJvK-ykLKRwzsS4IrjLnC0DFoV1vBKqUcvk3TKN3Q_RKE4MdJmXESVo0CJ8COTzbVOSKJ4vbFLssDdVwcmn_WEUgAGmCF3gLQWUNBwkrb35qWUbgHE4UQfNG0ovFtofQYwpv0GZSzEGV5I3MJCJ6ktdboKXIkz0_FHbSI4dnEVpo_DT9y4bPzbLX88f00_WeZpqSAmxia0Q3HOSTkdWPmhOYm54BsdH2mpOIRF7uq0BVxh1D5-lm4ApgtHbK01to587S0dHxqyvqfVxf_cB7P1a-e7b2Twf9FO5PI4WbTjqCXJVjm3WTLPCZYxGVzda8BUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d381cb7a98.mp4?token=Ew5VT77OUNgncY5OHEmTJvK-ykLKRwzsS4IrjLnC0DFoV1vBKqUcvk3TKN3Q_RKE4MdJmXESVo0CJ8COTzbVOSKJ4vbFLssDdVwcmn_WEUgAGmCF3gLQWUNBwkrb35qWUbgHE4UQfNG0ovFtofQYwpv0GZSzEGV5I3MJCJ6ktdboKXIkz0_FHbSI4dnEVpo_DT9y4bPzbLX88f00_WeZpqSAmxia0Q3HOSTkdWPmhOYm54BsdH2mpOIRF7uq0BVxh1D5-lm4ApgtHbK01to587S0dHxqyvqfVxf_cB7P1a-e7b2Twf9FO5PI4WbTjqCXJVjm3WTLPCZYxGVzda8BUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🚨
همسر بیژن مرتضوی خبر از بازگشت این شخص به ایران را دقایقی‌پیش اعلام کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107553" target="_blank">📅 16:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=mp21hRhfOFYgbXEzPOo1lfe9pcRncyMiOD4BoEwnFEOlWdYSapjzhbMzRkrsYlQFv8B54MCtFdgVRAOvvkr567uX_lGxGSN2iYPAx6t_If4y7UloDtIj_2ExOPOltdtKQu71QJSPhMfRImsn34tX_kt0g9PB3XgkE2KWdKO0aYYhXHWDGoHMFFiL7RMfid-grVHpx7ZFNehGBSY6QLP96eMnxvWr8LpPJJNvwVnmaRps8Hcxz_WnaumQjG918nftVJ1Sts7nv4n1yqG7K4R-LcQGDxPXpliQY1emgfMGQ97robykakTJ2fNwBiA0RDptZ5iJiW50qdwc8Coo2GwDhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a63edbd38.mp4?token=mp21hRhfOFYgbXEzPOo1lfe9pcRncyMiOD4BoEwnFEOlWdYSapjzhbMzRkrsYlQFv8B54MCtFdgVRAOvvkr567uX_lGxGSN2iYPAx6t_If4y7UloDtIj_2ExOPOltdtKQu71QJSPhMfRImsn34tX_kt0g9PB3XgkE2KWdKO0aYYhXHWDGoHMFFiL7RMfid-grVHpx7ZFNehGBSY6QLP96eMnxvWr8LpPJJNvwVnmaRps8Hcxz_WnaumQjG918nftVJ1Sts7nv4n1yqG7K4R-LcQGDxPXpliQY1emgfMGQ97robykakTJ2fNwBiA0RDptZ5iJiW50qdwc8Coo2GwDhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
قلعه‌نویی میدونه ترند چیه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107552" target="_blank">📅 16:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qlQA2MEE2TuktWdZ-T8fpvI0J_6UxWt4OKSpsDI_qbqY1_mNlvhTlqTuV60X3wxTgnTcGqTbwuPHnSvJULv1CJY5or5IIaeHVDXA7Qg9Z0aaSNCgnMS_Ivs3yrzfPLzlsbWQecOQ6lf1o6kUGLCAxJ9LOxgVVFnpOdyCmXIbGYxL5mbjhRQZZVAtyPNGiVntz1w9OnOaNI9RgskfqzVDtLVTo0QN0_ne3rP6fRIJ7a04QvKsx09-DYhnPvnhEaVSnRXshIpojRjCFAx6cu2WdJc8smIZYwBwtDwUuxenzTwZs16DWDhU0DpUkOZKTTe4z3RxPzf5vS1BAPsl0ot88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
⚽️
برای اولین بار از زمان رقابت‌های یورو 2008، کریستیانو رونالدو در تمام طول یک مسابقه، نیمکت نشین بود و حتی یک دقیقه هم برای پرتغال بازی نکرد.
🇵🇹
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/107551" target="_blank">📅 15:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=W299f2woqk-JuW8xK-IWuez5PbcHpUwTDtFq_x-6sYrxu2603owmZF3nteJgIRK7mbYCwVw5npu8UGIdmAQQpK9XN873eSmlV5U1TGQqP2mkDLciOynWEJueYkwuwi5VOGMKzP0lZXzwd8FUzQqApVHYeU9iP5JDHlhch8wiop3SzM3uIeLyRBCQ6BLCOJUL0ivG_y15Lc5t4qq5BmyVbJhN0tsqv5tMS_2Qj_H5jQT9IlMnNawgSmV8HIFzAcNqEi4fSdBZ3qKD2f6OCOXTqsau2cf3hRtHCe7Yj_5_essrCE7pvPK7WpPF-GOpM0g9-XtqAr3TP4zqdTzonGptzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0610e8bf78.mp4?token=W299f2woqk-JuW8xK-IWuez5PbcHpUwTDtFq_x-6sYrxu2603owmZF3nteJgIRK7mbYCwVw5npu8UGIdmAQQpK9XN873eSmlV5U1TGQqP2mkDLciOynWEJueYkwuwi5VOGMKzP0lZXzwd8FUzQqApVHYeU9iP5JDHlhch8wiop3SzM3uIeLyRBCQ6BLCOJUL0ivG_y15Lc5t4qq5BmyVbJhN0tsqv5tMS_2Qj_H5jQT9IlMnNawgSmV8HIFzAcNqEi4fSdBZ3qKD2f6OCOXTqsau2cf3hRtHCe7Yj_5_essrCE7pvPK7WpPF-GOpM0g9-XtqAr3TP4zqdTzonGptzYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
دیس امیرمهدی ژوله به جنجال خداداد عزیزی نسبت به پاهای پرانتزی امید عالیشاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107550" target="_blank">📅 15:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=o3o3lPKreoRlgn313s1JXWB06w1x9KwJZ6RCVqLrvQQPV0DTq_vMxbsqMnkzwQ-JeNjo_yr4zW3A9bjz6ThS-i4kLPFWTM-6piuEBSLqf5QjZB8hgGvjTaUwi_SL2BIsTMURFtPGE4JqIdBrhOvhYSz2fMJxbCXvKqMYgOqQcFYb6g_sbhvsZwLp_s30aAsufkEo71vCQm_jw-ClzexL3UkI3xtFyThm4QVRxKB6LTdhAkq5EcvhNyaiBJgrXOOnIpFMoHEXfaJuuFaVez-DmFb3wylW9hbZd2QAAV6x-LvSHy4_0gp3CgyM_I8rZ5vofWoR557Rfpz4M1xUyQ9OBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a12598c8c6.mp4?token=o3o3lPKreoRlgn313s1JXWB06w1x9KwJZ6RCVqLrvQQPV0DTq_vMxbsqMnkzwQ-JeNjo_yr4zW3A9bjz6ThS-i4kLPFWTM-6piuEBSLqf5QjZB8hgGvjTaUwi_SL2BIsTMURFtPGE4JqIdBrhOvhYSz2fMJxbCXvKqMYgOqQcFYb6g_sbhvsZwLp_s30aAsufkEo71vCQm_jw-ClzexL3UkI3xtFyThm4QVRxKB6LTdhAkq5EcvhNyaiBJgrXOOnIpFMoHEXfaJuuFaVez-DmFb3wylW9hbZd2QAAV6x-LvSHy4_0gp3CgyM_I8rZ5vofWoR557Rfpz4M1xUyQ9OBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
‼️
جام جهانیه یا مسابقه‌ی انتخاب کراش جهانی؟ کنایه ابوطالب به لیست نفرات قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107549" target="_blank">📅 14:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=FnNPJ0CEb9iIQRAEiC5o7qjUjt7SaBc8yrdN0ywrVB8h7CKFr-rGT6eFMlrwGRFxShzP-WoD5ysIgOCCX6W_iA0sjvi9SNF63sI9ie4ru83wARU0ma069du5nb8RNA10KeWGhGzg6-01wlPw2Uy6lsodwa2EXr9wIPlZIjnNqevIehOCkI4O-gQA8qlUvNVOGAJDyZ8MyKaKUx_yN2X1DVL8afrVBVKPl9O4Mb21DxTojsAps901tyWciJyL8NFtsbA-JUsQf87e5cJ7CtwIfmMV8M8M2oJuy8leWWHO1nr2qNtMB0AiSIpOq1bgepTbT6-WG-2rpRP7sZfcvpWzGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c539f4e6f.mp4?token=FnNPJ0CEb9iIQRAEiC5o7qjUjt7SaBc8yrdN0ywrVB8h7CKFr-rGT6eFMlrwGRFxShzP-WoD5ysIgOCCX6W_iA0sjvi9SNF63sI9ie4ru83wARU0ma069du5nb8RNA10KeWGhGzg6-01wlPw2Uy6lsodwa2EXr9wIPlZIjnNqevIehOCkI4O-gQA8qlUvNVOGAJDyZ8MyKaKUx_yN2X1DVL8afrVBVKPl9O4Mb21DxTojsAps901tyWciJyL8NFtsbA-JUsQf87e5cJ7CtwIfmMV8M8M2oJuy8leWWHO1nr2qNtMB0AiSIpOq1bgepTbT6-WG-2rpRP7sZfcvpWzGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
پاسخ ابوطالب به انتقادها از برنامه‌فان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107548" target="_blank">📅 14:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107547">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=BKMOXOQcmdpBAxN42gsWAUOUySCXbRHZpzxxe08Uo-y94-uXl2DFz0igQ6_UHxsF1PQHnjh7gI0Gnt9C8WlAIc-A5hlejheVCh32tywctQWusxpYQSf9aVFqynz-4RC_frIjQPUosWtGeSH2jaH0GCUf55P-KJWGPgbt_UQGkNxkHd3ysT6DhSdPjvvQlsqU-6jasFWRAeEQGSFWLEpZH1MOdkrOcJBDlIoYfIG3PbQQZWWA44uGhvROotG4R5AqAiMPzN1ru49oEwVOzeAp5yHqMPoO8AEjnauC18svrCzweVYy2vQM-R3Q71MRrjMMw5O2Xiu2hWNssPXr9Inhh038qTZMwf6pR4n8aIjZHOxnxZ1TANXSqZ3nH3UC_SaavDar2Kam9BHmn8PwDI0MnmdGeUDcuggKgye_M56F-2dkQDoERhpL-Kce3gDQG5XMzTKBraQ3o6lAL9mGcYvdDp61P3o92PDGm2FI3eEwbM-b58PtWG11xnfsnC5CP0ApHnUCtCeAz4Yu-1LI9D73_nb1OgPX3mdIW86_OO5A4eWaWhryzuhEozM7qkWAbUeTE6UIX5DgqBTgwfEGYcevi9euWGQEa5FEIlaWxlasafKrdVe5VrCRDbZ6KTg-3qwMvgm_jFqaORsljH6nJ_XDHWF59J2biUt_q2MpCRZPmgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dc4546c8d.mp4?token=BKMOXOQcmdpBAxN42gsWAUOUySCXbRHZpzxxe08Uo-y94-uXl2DFz0igQ6_UHxsF1PQHnjh7gI0Gnt9C8WlAIc-A5hlejheVCh32tywctQWusxpYQSf9aVFqynz-4RC_frIjQPUosWtGeSH2jaH0GCUf55P-KJWGPgbt_UQGkNxkHd3ysT6DhSdPjvvQlsqU-6jasFWRAeEQGSFWLEpZH1MOdkrOcJBDlIoYfIG3PbQQZWWA44uGhvROotG4R5AqAiMPzN1ru49oEwVOzeAp5yHqMPoO8AEjnauC18svrCzweVYy2vQM-R3Q71MRrjMMw5O2Xiu2hWNssPXr9Inhh038qTZMwf6pR4n8aIjZHOxnxZ1TANXSqZ3nH3UC_SaavDar2Kam9BHmn8PwDI0MnmdGeUDcuggKgye_M56F-2dkQDoERhpL-Kce3gDQG5XMzTKBraQ3o6lAL9mGcYvdDp61P3o92PDGm2FI3eEwbM-b58PtWG11xnfsnC5CP0ApHnUCtCeAz4Yu-1LI9D73_nb1OgPX3mdIW86_OO5A4eWaWhryzuhEozM7qkWAbUeTE6UIX5DgqBTgwfEGYcevi9euWGQEa5FEIlaWxlasafKrdVe5VrCRDbZ6KTg-3qwMvgm_jFqaORsljH6nJ_XDHWF59J2biUt_q2MpCRZPmgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آنالیز بازی انگلیس مقابل اسپانیا که حاوی نکات بسیار دیدنی برای علاقه‌مندان به فوتباله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/107547" target="_blank">📅 14:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107546">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">✔️
رونمایی فدراسیون از معیارهای تعیین رده‌بندی و قهرمان در صورت لغو فصل:
🔻
۱-در صورت برگزاری حداقل 75 درصد مسابقات رده بندی بر اساس جدول موجود.
🔻
۲- در صورت برگزاری کمتر از 75 درصد رده بندی بر اساس میانگین امتیاز در هر مسابقه.
🔻
۳- در صورت اختلاف فاحش تعداد بازی‌ها استفاده از میانگین امتیاز به همراه تفاضل گل و نتایج رودررو.
🔹
تبصره: سازمان لیگ می‌تواند با تصویب هیئت رئیسه روش عادلانه‌تری را جایگزین کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107546" target="_blank">📅 13:53 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107545">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=Gl43g-iu7I7EVZbEeewxHfKJ8d_30UYkSxf8Jxz4yfHrAJuz0pConFNEoCAi4pqVRjy_5BRpBZrKvpq4_BFMC5PCLMMR8JYGtNQCwoDBIfvv1MubcyEj2RnAU20BdJ_AsG2E1kt58SbUdJJk5giBt3lCYxhvxsaxmA9BAuDhZQYOhTH694440C75KfWBej5x1ZZC-QgmjGPKC_6BMIUTIPmXtunHeNQybDPYiI18Kz8D0o3q_iCkeLn0ei3ncU_MVMD2Te02IcPq_hcjE97HEH0BAAjVZcEWBAo07eMUt3YWDgMqWnuGSgaylWOmvZZ6FAVwjJl4SDEaKqPkxQ8ZFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95a2f6b70b.mp4?token=Gl43g-iu7I7EVZbEeewxHfKJ8d_30UYkSxf8Jxz4yfHrAJuz0pConFNEoCAi4pqVRjy_5BRpBZrKvpq4_BFMC5PCLMMR8JYGtNQCwoDBIfvv1MubcyEj2RnAU20BdJ_AsG2E1kt58SbUdJJk5giBt3lCYxhvxsaxmA9BAuDhZQYOhTH694440C75KfWBej5x1ZZC-QgmjGPKC_6BMIUTIPmXtunHeNQybDPYiI18Kz8D0o3q_iCkeLn0ei3ncU_MVMD2Te02IcPq_hcjE97HEH0BAAjVZcEWBAo07eMUt3YWDgMqWnuGSgaylWOmvZZ6FAVwjJl4SDEaKqPkxQ8ZFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
تصاویری از علیرضا بیرانوند با لباس سربازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107545" target="_blank">📅 13:42 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107544">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=iGv_pdPokiNJ5cW7r01OHsL1EoahTpozRvyD7uxGDTeCcnHGLZLD7eI0GdTyfMpYuta3hdwB0ou5DVtH8kWJ8tJisCafAOqxnlQG1hGYEL8Z9XdAaRf99SQMqC8ZQGy6jDrVNTW9QqC_t1eopoLNERQQotNd-qvroyTkpAMpoLfdTeiB4RajijIi0rMR1x-kVW-KYTmaD9ayrBTbFp0D-ZqDE309PlSY5ub-e78L8o85Ol2R7MoMBSScoQ4JtWhdxya1uweLpsPbzO4CTvmtbfgE9Cec8b8TOE7c4dq5kBY2p9_UwtqoHOF2_0RptH46hjSXwak_BUEaxqGPiwdM7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6d3e68068.mp4?token=iGv_pdPokiNJ5cW7r01OHsL1EoahTpozRvyD7uxGDTeCcnHGLZLD7eI0GdTyfMpYuta3hdwB0ou5DVtH8kWJ8tJisCafAOqxnlQG1hGYEL8Z9XdAaRf99SQMqC8ZQGy6jDrVNTW9QqC_t1eopoLNERQQotNd-qvroyTkpAMpoLfdTeiB4RajijIi0rMR1x-kVW-KYTmaD9ayrBTbFp0D-ZqDE309PlSY5ub-e78L8o85Ol2R7MoMBSScoQ4JtWhdxya1uweLpsPbzO4CTvmtbfgE9Cec8b8TOE7c4dq5kBY2p9_UwtqoHOF2_0RptH46hjSXwak_BUEaxqGPiwdM7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚽️
توصیف امیرحسین قیاسی از امیر قلعه‌نویی: جوان‌گرایی و تاکتیک مناسب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107544" target="_blank">📅 13:35 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107543">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=lhukTe-2RDLky5BONssmPwxwXxFQbWug-PPjVi0NPU9wkn_mcRxY6OEOm6K_-2hOWms8YnngRaaVQwELC0Ve0_1ksQv-0F0FVK2YWhFrLvpWw26yrWsjfh3_P2L_nKFoWRMeuYN5GzG7oXbOqwVBQN95pvs55nVSazill3magRCnVkoVIrWRps88ZY_GwgNEfcNr0xCdc-M9KyR0QwTH9gKy3jSIDxgnrlfgXXbAEuKUt6r-Lk7oi2MkGCMgnBhzW1zsSY_qBcn6GAHIVgUdzS_EX8b6ExL8_w0bpPmQ4Y44fdPP_KT5x5_a6wk2m710o53FqCw74pKPtLS4MwjiuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad2b061cd6.mp4?token=lhukTe-2RDLky5BONssmPwxwXxFQbWug-PPjVi0NPU9wkn_mcRxY6OEOm6K_-2hOWms8YnngRaaVQwELC0Ve0_1ksQv-0F0FVK2YWhFrLvpWw26yrWsjfh3_P2L_nKFoWRMeuYN5GzG7oXbOqwVBQN95pvs55nVSazill3magRCnVkoVIrWRps88ZY_GwgNEfcNr0xCdc-M9KyR0QwTH9gKy3jSIDxgnrlfgXXbAEuKUt6r-Lk7oi2MkGCMgnBhzW1zsSY_qBcn6GAHIVgUdzS_EX8b6ExL8_w0bpPmQ4Y44fdPP_KT5x5_a6wk2m710o53FqCw74pKPtLS4MwjiuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های امیرحسین‌قیاسی درباره سفارش غذا ۶۰ میلیون تومانی برای مهران‌مدیری!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107543" target="_blank">📅 13:10 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107542">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=c6SJo9rX1D8osbd6XRzOEoe8c30X8M9TR5zIc54VugRb9cAHdYPZKPKdFz-6Xl0ePZQk4OOzRZ1F42tTqWOJe4ArQs7widO3YdAzYPJ8LnTILpKebIPtwj4NNWk9YZTwNtLfB-_oInxwvaOm31WDKTOVA4mngLbV0wW9HlAXzoU4lBRbG4TQBnMkNmRKaJuKnfGdLrCYJDwUNZ6aHrNY4KX5wqMeChQKotSzGWbhDM2IuFsVi6ELV4mEv4NfjgNYBYniZukEUb1gI25MFpkWX-oMfQLJpQOjygdr5kV3rAKqKMKXG71vJZNWvZgwGnTDclDjRab1dX1Ug6qo8Tp9j0QLFE5XZSyjSYZoDTmiIYsWVWrqfM9XztmoW_KO0wtAT2KGEfX1LGReUUC0RKZowLHhqB0pVno2fbTL9EgvgqxN1PLrzXA_u5dbaKfKF91zyror8LYJQxmHgJvWY_fSNLmWh-wQoxUHDbKV2KpLC_C03OykDnn-87w_O15CLou2tqd8r3965Dayosgw8XOfhH6DolTwEpU7YsVksr7K3y5iAddt24m-vhwmYufysDBkU7gYI69CMgkpR9cjxVT459oR4Q7dym2ixbYESj3KvKtSGovkuOURQ-i-3rVRKqWl3zi6GtkVMxlqyg3hLx0xrjdfIuNVwLJaLvn7lEt93QU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9a4a5cb83.mp4?token=c6SJo9rX1D8osbd6XRzOEoe8c30X8M9TR5zIc54VugRb9cAHdYPZKPKdFz-6Xl0ePZQk4OOzRZ1F42tTqWOJe4ArQs7widO3YdAzYPJ8LnTILpKebIPtwj4NNWk9YZTwNtLfB-_oInxwvaOm31WDKTOVA4mngLbV0wW9HlAXzoU4lBRbG4TQBnMkNmRKaJuKnfGdLrCYJDwUNZ6aHrNY4KX5wqMeChQKotSzGWbhDM2IuFsVi6ELV4mEv4NfjgNYBYniZukEUb1gI25MFpkWX-oMfQLJpQOjygdr5kV3rAKqKMKXG71vJZNWvZgwGnTDclDjRab1dX1Ug6qo8Tp9j0QLFE5XZSyjSYZoDTmiIYsWVWrqfM9XztmoW_KO0wtAT2KGEfX1LGReUUC0RKZowLHhqB0pVno2fbTL9EgvgqxN1PLrzXA_u5dbaKfKF91zyror8LYJQxmHgJvWY_fSNLmWh-wQoxUHDbKV2KpLC_C03OykDnn-87w_O15CLou2tqd8r3965Dayosgw8XOfhH6DolTwEpU7YsVksr7K3y5iAddt24m-vhwmYufysDBkU7gYI69CMgkpR9cjxVT459oR4Q7dym2ixbYESj3KvKtSGovkuOURQ-i-3rVRKqWl3zi6GtkVMxlqyg3hLx0xrjdfIuNVwLJaLvn7lEt93QU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
مارادونا: ۴۰ تا بازیکن از تیمای مختلف ایتالیا روی هم،  به اندازه یه توتی نمیشن!⁣
اسطوره رم ۵۰ ساله شد.
🐺
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107542" target="_blank">📅 12:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4869197932.mp4?token=jY50wJQ93VhSfqzH1D8CoZYi9GyH4Rms7L9cZYk7A7rAjnlrwo_9YQtFK_x6SEA6MTE9hpvUvTx08HghNVzPZW9dPJGqOScRT5RGsHaC1oKYe_lIx89vpfTLwn-A-PPDurX5LCXaMAl1jQhx9Cfsnov8UvArg6_dXEnJwpHJin5-d9leH2Mn6_4TqvAQGwIc1TDn-_w8wDIaD_EEAfMF4rdGQKY8hRdQ4MKP8QxbAbJebrocUyjduTOyBywfsMPa5REC5tqEtg7pxO12jQNPKoWq5ccFpnqfiWqXqcMYoNHcQZRr_eD53m6lsJPBf000u2DvGkFLvibA02T6fOL0SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4869197932.mp4?token=jY50wJQ93VhSfqzH1D8CoZYi9GyH4Rms7L9cZYk7A7rAjnlrwo_9YQtFK_x6SEA6MTE9hpvUvTx08HghNVzPZW9dPJGqOScRT5RGsHaC1oKYe_lIx89vpfTLwn-A-PPDurX5LCXaMAl1jQhx9Cfsnov8UvArg6_dXEnJwpHJin5-d9leH2Mn6_4TqvAQGwIc1TDn-_w8wDIaD_EEAfMF4rdGQKY8hRdQ4MKP8QxbAbJebrocUyjduTOyBywfsMPa5REC5tqEtg7pxO12jQNPKoWq5ccFpnqfiWqXqcMYoNHcQZRr_eD53m6lsJPBf000u2DvGkFLvibA02T6fOL0SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇪
🇳🇱
یک‌ماجرای جالب از فوتبال هلندی - بلژیکی!
خانواده آقای فن‌بومل، خودش، پسراش، زنش و البته پدرزنش⁩
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107541" target="_blank">📅 12:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=QfGecErjrDAb7LwhMt6vYd2ym0p3IUKYoBwxT-SK-wdlwk9XZBwt2TpmbAgLD0pF7cFXgg_8VXSodkva2_NA3NUYDGgrx0Zl3CoU_TAu9iAJ5K_H3sC3yuNdVr8X7wU-bmcF8QG9owF9vEvAa8FLKbngwf6PUQe9tLXuawGHP2xEnwr9Q_MxPWCTstXm3N133-XDXuz3KczwlEx371jDo8ZKRkdIx6IY8Sspg6eRriJzVk3f6jvBc90hllDZP1QuhsqLT_USLYq59iVsqO8UKc_Ebw8311LcBKcEX6sqaIbambGSpOvh1yNi29KIEm_XARp2EjpDtq8DkNjZk0Nvq7nHrUxqjK-9VUQGYxA9_nLzjG3IKDDRicyEMu8cQhYq1WHuGkUdSfHhCmP4Adky2Nj358jQbTe3M5PmypnM1C9AtcjRxgn9-Q5IKPJAOIjx466fZ6067uYJgFokjx_O2CpBtIU2J8ncEPohysJ2B5h0vxBOHPfDMYgSg_Y62TytaSlmcGiUc78pftZMo-AotBidL-bwQB3jzZHYay6SUIfet8BP1skiC-GW6-q5XTTAiikTByV_pjHHFKz1DO-OUw1ab7BNWXhLU7iRJqCIFxhuCGmAWZyWE1Wfa2XYHlh3H8Yj5EyNEh9igzulVtfT2jNP9Y7puKjTDig2N3dZQG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/621d1efcf6.mp4?token=QfGecErjrDAb7LwhMt6vYd2ym0p3IUKYoBwxT-SK-wdlwk9XZBwt2TpmbAgLD0pF7cFXgg_8VXSodkva2_NA3NUYDGgrx0Zl3CoU_TAu9iAJ5K_H3sC3yuNdVr8X7wU-bmcF8QG9owF9vEvAa8FLKbngwf6PUQe9tLXuawGHP2xEnwr9Q_MxPWCTstXm3N133-XDXuz3KczwlEx371jDo8ZKRkdIx6IY8Sspg6eRriJzVk3f6jvBc90hllDZP1QuhsqLT_USLYq59iVsqO8UKc_Ebw8311LcBKcEX6sqaIbambGSpOvh1yNi29KIEm_XARp2EjpDtq8DkNjZk0Nvq7nHrUxqjK-9VUQGYxA9_nLzjG3IKDDRicyEMu8cQhYq1WHuGkUdSfHhCmP4Adky2Nj358jQbTe3M5PmypnM1C9AtcjRxgn9-Q5IKPJAOIjx466fZ6067uYJgFokjx_O2CpBtIU2J8ncEPohysJ2B5h0vxBOHPfDMYgSg_Y62TytaSlmcGiUc78pftZMo-AotBidL-bwQB3jzZHYay6SUIfet8BP1skiC-GW6-q5XTTAiikTByV_pjHHFKz1DO-OUw1ab7BNWXhLU7iRJqCIFxhuCGmAWZyWE1Wfa2XYHlh3H8Yj5EyNEh9igzulVtfT2jNP9Y7puKjTDig2N3dZQG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
روایت عجیب و غریب میثاقی از معافیت پزشکی برخی از فوتبالیست‌های مشهور!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/107540" target="_blank">📅 11:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=iIk4c6J6NvIAF7_pGJZbD3H5O6Xu0mqy_k3KxSy6pybCQuYD6fKHct2qQly-Ns44HhsR2EzQ1BpV2uf13UO2cblGrMWVbhBpaseDTZHEzO-vq1xjIjfsOjpYc0cnx6BnoktKDLpBfU-NafBqD-aC6-LDEXWKdup0xIEOfiu0uzKwNocX5xUc0UYo86MG1-rvAcrSuWUPUakt-I3TjH5OaC5TbA_8am2b2N-y8OsdFoLEyO2W84HQvf2YO1Ouk4nBEXUfMGXnrHE89D_bkJOnxR9g5u6hMbVLCrG-_hp1G9rJhZOFHCXBJz29zvluSnmkSwZnp_TIQhlN0-il_mobJ6fwVJJ-2ka3oJLJ-mAvOgZf_X7NtPlcYWNL-dEaEbF-A169kwXW4M0q5m9zlA0eiLBy5Mzy_C3o1-XEWFi3ifREjGqO3QEp9bjj9kf9IXVDQV1Cif1-9njSMgJ7b7ZxQvJ9tOno_kmzDEc8PjBTq72al0i-SWPh9yK7GdlpYENS2ijuqrcBaHbPVoGnBRi-CJ5SlFdbV29Fmrx7ulfsnXthdBHxWUfsWJSM7zhJEPe8KdV3jf8WJQs7UFXSGpUSNCc9ngn8Ktfw4kOl9_JUwDHPgzq-AnxzQ64yT105ukSyI_uEDHvcR4yHlCGuRgoAx3lLtXhYfWllUqMBl-3sPKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/884ca354f5.mp4?token=iIk4c6J6NvIAF7_pGJZbD3H5O6Xu0mqy_k3KxSy6pybCQuYD6fKHct2qQly-Ns44HhsR2EzQ1BpV2uf13UO2cblGrMWVbhBpaseDTZHEzO-vq1xjIjfsOjpYc0cnx6BnoktKDLpBfU-NafBqD-aC6-LDEXWKdup0xIEOfiu0uzKwNocX5xUc0UYo86MG1-rvAcrSuWUPUakt-I3TjH5OaC5TbA_8am2b2N-y8OsdFoLEyO2W84HQvf2YO1Ouk4nBEXUfMGXnrHE89D_bkJOnxR9g5u6hMbVLCrG-_hp1G9rJhZOFHCXBJz29zvluSnmkSwZnp_TIQhlN0-il_mobJ6fwVJJ-2ka3oJLJ-mAvOgZf_X7NtPlcYWNL-dEaEbF-A169kwXW4M0q5m9zlA0eiLBy5Mzy_C3o1-XEWFi3ifREjGqO3QEp9bjj9kf9IXVDQV1Cif1-9njSMgJ7b7ZxQvJ9tOno_kmzDEc8PjBTq72al0i-SWPh9yK7GdlpYENS2ijuqrcBaHbPVoGnBRi-CJ5SlFdbV29Fmrx7ulfsnXthdBHxWUfsWJSM7zhJEPe8KdV3jf8WJQs7UFXSGpUSNCc9ngn8Ktfw4kOl9_JUwDHPgzq-AnxzQ64yT105ukSyI_uEDHvcR4yHlCGuRgoAx3lLtXhYfWllUqMBl-3sPKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
‼️
سه‌ سال و نیم بدون رشد و تغییر در ترکیب نفرات دعوت شده توسط قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/Futball180TV/107539" target="_blank">📅 11:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If3DVxdN1tA6Ew0t7RnsIbmRFsP2sjwgJbPfXDPCYzgjokQgEsEgmcVHGGRr-Z1XxK1kN8yZRVQMKiSa8d9b7CemBzn4CYdLNE6P8IFJCIqvg-WAAoKQaxRA8YBRSG1gYcaSoQ6AjY_nWhH7wgbhpTL_8jtNpOxq50lvsyC69YJewQ0dWTfPA6SOapNNmfl-bgcFy0VY2fipeUpDe1iKppTxzuRB9dX71UmPU2RPBK0Y13cLQIj9GUaOr3ArAzM-Mu4lvHny_s7HSFlGtA_0cM1dL3gzM1PN-o-S2bMzD1EtBGrY-sGgOnA2FlG4APMmtzArUrUXbQROybxDG3SYsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
📊
ترکیب منتخب دور‌دوم لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107538" target="_blank">📅 11:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
🎙
صحبت‌های شنیدنی رسول‌مجیدی درباره کیفیت آکادمی‌های فوتبال اسپانیا که زمینه‌ساز نسل‌سازی‌و قهرمانی در جام‌جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107537" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107536" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/Futball180TV/107536" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7gwlW9lAES99BaaGcYkN1O_44FA7TlBTJSzCHSZ2Oy_NXJ96vluGCK9B3UVLmyKLEvREcjygL6xntnn5VmXP7RBO60SuBc-RKTuhnjN7Rm0i9fipDt_audksCqV-AeREBStWTLlxLpL9FtPLn_g7tJo0TwXQeRbL5_J8nTS_lMISRepQc6AQn4au3C9w2GL-eksd3tA2kp53anL1swNhoZONkvknwPpS5a-OmhT3C41G59fmXJksQKR9kTDEf4_hFH6XSGCVQeYx7-DqA20n8EAmxovndLERyyb-tuWukAsMPFVc8tYAK-q7oyWJy6iXMwWEZM3DemycsqlABfzhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط ۴ روز تا انفجار در قفس
🦖
​ناتالیا سیلویا در مقابل وانگ کونگ
جنگ سرعت و تکنیک؛ چه کسی قهرمان جدید
UFC
می‌شود؟
🦖
​شانس‌ات را در
TrexBet
امتحان کن و روی قهرمانت شرط ببند!
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/107535" target="_blank">📅 11:03 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nUqoA6PdmefKnrXfGCEOTif8FOwKpS4ZzPqRU-SqAnvBDfmk9Jy6z56-mpBkqNHZ155BVrxqYRdZPiElo5zAq0u5thUic39FJ284rgKio4YPE-UIydroL8VI7UlKt6xV18Pi_up75R3lY2uRWbyiTRj8ulkJBVdIkTcYy9jKH7kyOGs1DLDH-OSYODv5Xn4WcJdZfgHyyz9QBiOcLAtutks-FmI_ConINux3dGiiYh8S70XECBogr2FEesR2Rv6btAH84sOoDOsTopigGWx_DKgDZOg4Qus1js_zN9ODyfteg5fKL4_hLK6arQ9XCTlqkpPAn3YB3R_hOPtGVoy30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
🇪🇸
رومانو: رافینیا اردوی برزیل رو ترک میکنه و برای مراقبت بیشتر به بارسلونا برمیگرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/Futball180TV/107534" target="_blank">📅 10:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gFP_vNoEDbHEWPME5qVz6Ta1jzVjaJ9-onQQWTgVol0EplfrZKXOII_LX_UofOXpy-XkvpByXf8Jgfe3vCRZ3gWLR2lRbBLE7LhmBNF4TPIVNxizbIejfzeU2Y2U5jk6SCKivC1AnS1r3lgmiBrxjp5OUKN9Wsqk5-8DCIWOATi7h_AOPqlDc6CxnTux14BwwnbdCDm9Bm-M6qFxwyUO40kuFljSgAe7qr8FHh2hRXLPgxNd7mq3o-2iuRvqy0mqDRR3PYGS2qntOgif3FvpgYV8VI1jmcytPRFY6Ckt_SmrnM6emF-9ypcUuoTh7OYdlxeLr5F4LMw6z-ijOKDc2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
👀
🇪🇸
اسکاتلند تنها تیمی که توانسته اسپانیا تحت هدایت دلافوئنته را در یک بازی رسمی طول ۹۰ دقیقه شکست دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/107533" target="_blank">📅 10:40 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M12P2rm5g3yQh9WhaYRmsLSYE3Ap9OM3wG37aRS8OkbGpbDPfdWywPGOmyDys1lF4JLXQsavujYLuUs_NP8ggOVKVrU3H5XNQLwaeHyLdfbZQBKd4sEQ_3_vuxAL-n0mBqa8_NQwBWChTHIklwhBMp2tuVXlHuFOtVBcuqN9LXf5lqQaDVknmQZKO0qkAFby6QqbxC5yjXYuPLNrG8bseRYIPNryysJQVw6Jm4Lo9XJWEG9kisQQwUP-i6cgXJ4eVgnRxCxQeYkVTGuCnVugIDtZ89sKs2tYDnusACgzqrrolljE_UEhDZwA29SfbM5M5atBMijCyc7mqVk6buyxqYEf9FrlqChgQq-czIuO6wvb-hav-5hDgqa3bBLWOf0iF0CT6nbNg52IYy5v-cdE2YHv41GsOMJrnCTsDo2fH48ZgPj3GgaDTY4FEWL5PRcX_NIdb-BjGbrj5rLQK9zOqjVfVRU7yHHH34xhGcrhALveq76w_Vcc1duRvaHeBFx7APsGUlSr5iNc3HdSDhWymdqEKuaKkCbuyplP5hpULiiW9dfuW80_AsnnFKLM8MRsdxf-S9iyZw24jQU_BzQdpH4m72vMM0-PLZz7rYxTH77Dk1lQMIgZ-8k7q_46dbREwlwBV0GIDxJiJUJ3Ho5W7J0tHYlanyQITnAgfZvMD8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78614739b9.mp4?token=M12P2rm5g3yQh9WhaYRmsLSYE3Ap9OM3wG37aRS8OkbGpbDPfdWywPGOmyDys1lF4JLXQsavujYLuUs_NP8ggOVKVrU3H5XNQLwaeHyLdfbZQBKd4sEQ_3_vuxAL-n0mBqa8_NQwBWChTHIklwhBMp2tuVXlHuFOtVBcuqN9LXf5lqQaDVknmQZKO0qkAFby6QqbxC5yjXYuPLNrG8bseRYIPNryysJQVw6Jm4Lo9XJWEG9kisQQwUP-i6cgXJ4eVgnRxCxQeYkVTGuCnVugIDtZ89sKs2tYDnusACgzqrrolljE_UEhDZwA29SfbM5M5atBMijCyc7mqVk6buyxqYEf9FrlqChgQq-czIuO6wvb-hav-5hDgqa3bBLWOf0iF0CT6nbNg52IYy5v-cdE2YHv41GsOMJrnCTsDo2fH48ZgPj3GgaDTY4FEWL5PRcX_NIdb-BjGbrj5rLQK9zOqjVfVRU7yHHH34xhGcrhALveq76w_Vcc1duRvaHeBFx7APsGUlSr5iNc3HdSDhWymdqEKuaKkCbuyplP5hpULiiW9dfuW80_AsnnFKLM8MRsdxf-S9iyZw24jQU_BzQdpH4m72vMM0-PLZz7rYxTH77Dk1lQMIgZ-8k7q_46dbREwlwBV0GIDxJiJUJ3Ho5W7J0tHYlanyQITnAgfZvMD8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
⚪️
واکنش فردوسی‌پور به مصاحبه‌های فرمایشی و سفارشی ملی‌پوشان: سردار آزمون، با سابقه بازی برای مورینیو، وادار به گفتن چه حرف‌هایی شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107532" target="_blank">📅 10:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4481359e02.mp4?token=q3Yv8SmMX_TOEOISrVBPnkPmqYwY1J2FGKBBuQ1Cs4P2qvEwaFhnKNLaIqDr0xefOO_3Nanpllzicx5ZtM-WRuyeHBCHx-yIi0GVuug3LfkkpSNhSt-aaEogvdsXp9zMd-yQZd1g2qwoadXuo6r2NfJCb8XCpcEYGNke931dmso9OSbToAXfALZ3yxebCZfYa5u8Vn_mGo3HA5qLq12EtYsvq1aOPz9xGmRIcybvRNt3Gy7NjkLKy5Bo2xToCf7rV5ztL2w-DguoYJhxR9NyHGVrPdXXL9yQ0l23YqZIKMluYQjTQijM1iNnXnTv1G9pg1T-fsOirngpUt3mmzu7Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4481359e02.mp4?token=q3Yv8SmMX_TOEOISrVBPnkPmqYwY1J2FGKBBuQ1Cs4P2qvEwaFhnKNLaIqDr0xefOO_3Nanpllzicx5ZtM-WRuyeHBCHx-yIi0GVuug3LfkkpSNhSt-aaEogvdsXp9zMd-yQZd1g2qwoadXuo6r2NfJCb8XCpcEYGNke931dmso9OSbToAXfALZ3yxebCZfYa5u8Vn_mGo3HA5qLq12EtYsvq1aOPz9xGmRIcybvRNt3Gy7NjkLKy5Bo2xToCf7rV5ztL2w-DguoYJhxR9NyHGVrPdXXL9yQ0l23YqZIKMluYQjTQijM1iNnXnTv1G9pg1T-fsOirngpUt3mmzu7Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
شهریار مغانلو و دانیال‌ اسماعیلی‌فر:
🔹
چند روز پیش بیرون بودیم رفتیم یچیزی بخریم، یه نفر دیگه هم اونجا بود و خواست خرید انجام بده و پولش نرسید و رفت؛ بنده‌خدا اینقدر عزت‌نفس داشت نموند که ما واسش حساب کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/107531" target="_blank">📅 09:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=SbVYWUDI9a7FtwRvDuvB7CapsR_He8o_QTzVMVd-X7wVZKasyWvc8U67-l099x8nPJZq8r3aFwQaWnlakYCL1lUzbNJcRFDxgV7kOPvovV6q1pRV5bwwct0LPE1nql46M3jl4qTv-Hj08bP5kkbZ0fBQOYYkIpnB9cWw0uiJhgCX31Z0ylTudG8Pvkyp24791jwhQhj7D5fErE8anzRbYifX2EPq0cyTSiP006xIkmGClnFb46XDGsFEdC2SqPh6zB-erNI37UPOecbhdvd021XKIVmT4DtGdoPT4PH9wb-E3lZm1HJmLm2jpInPABAm_msJsHIk_KHIUIRSnqkv0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5234add2e9.mp4?token=SbVYWUDI9a7FtwRvDuvB7CapsR_He8o_QTzVMVd-X7wVZKasyWvc8U67-l099x8nPJZq8r3aFwQaWnlakYCL1lUzbNJcRFDxgV7kOPvovV6q1pRV5bwwct0LPE1nql46M3jl4qTv-Hj08bP5kkbZ0fBQOYYkIpnB9cWw0uiJhgCX31Z0ylTudG8Pvkyp24791jwhQhj7D5fErE8anzRbYifX2EPq0cyTSiP006xIkmGClnFb46XDGsFEdC2SqPh6zB-erNI37UPOecbhdvd021XKIVmT4DtGdoPT4PH9wb-E3lZm1HJmLm2jpInPABAm_msJsHIk_KHIUIRSnqkv0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🎙
میثاقی: سردار تو وضعیت سربازیت چطوره؟ معافیت تحصیلی داری؟
‼️
سردار آزمون: نمیدونم ولی میدونم دکترای فیزیولوژی ندارم، اصلا چرا باید بتو جواب بدم به نظام وظیفه جواب میدم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107530" target="_blank">📅 09:25 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107529">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=d7WAqO4ufrljVdOO5JW1jznvNUK_0_xaLQlZlgWhh4FL6Juq2I_GA6lMfd3aAuM5V8P79K1S2DY_8zwV6cIinHI1qOLUTHLmR_2VUPXJvqksho3Ym-JrXL8RW4CaDx_xbgcIiQXTm8gABW3pZOE_RWOtT4pP9fwZfItVKGN5qLhAR9TXlDd1Ja_7QNA9Yco-oejHGUieusAESvWorJn4PE06LV4BmMTmMktSrfdD7g5pf3IcNCYLlkczopCFkiLoykG1EeT5u3NSRvhfb0Opt6hrGi9v1turBJgpNxeuoqGN-cFYbNAq_ZCPEQmdcVYI-KiJlleANn22IfK8JhqvlT3BELtC1Jz4qutcdBrDH-Di7LHG_KkZbd0_MBUfX7u5Hhaurtk3JDQnG-_rdmOPK9B-73xhgn-iPM_LiQ1LNqylVIX25NaseUkte_3PXxqatEPmLI6kfDtLXP8vAvTJ_sARRX4vs7um8s6vzb2hKDBqNE2hXm3aXYz1GNwu5OLzrv3LKOysvuIVbtka_FwWcHjzEukoYmOQyib9dY4yTvyVtvV6jC_Uf_CLVMhQkqeMiD6_UUGDZH5hAJQfD2CIuQeDc98ebhfoeDJBimJ96BbycDFstfHHvsgaIGtqM4UAub6qIBcfoiJhLZOiIG8gP2-JKHzs9zZYnOVchl9OblI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c02612ddc0.mp4?token=d7WAqO4ufrljVdOO5JW1jznvNUK_0_xaLQlZlgWhh4FL6Juq2I_GA6lMfd3aAuM5V8P79K1S2DY_8zwV6cIinHI1qOLUTHLmR_2VUPXJvqksho3Ym-JrXL8RW4CaDx_xbgcIiQXTm8gABW3pZOE_RWOtT4pP9fwZfItVKGN5qLhAR9TXlDd1Ja_7QNA9Yco-oejHGUieusAESvWorJn4PE06LV4BmMTmMktSrfdD7g5pf3IcNCYLlkczopCFkiLoykG1EeT5u3NSRvhfb0Opt6hrGi9v1turBJgpNxeuoqGN-cFYbNAq_ZCPEQmdcVYI-KiJlleANn22IfK8JhqvlT3BELtC1Jz4qutcdBrDH-Di7LHG_KkZbd0_MBUfX7u5Hhaurtk3JDQnG-_rdmOPK9B-73xhgn-iPM_LiQ1LNqylVIX25NaseUkte_3PXxqatEPmLI6kfDtLXP8vAvTJ_sARRX4vs7um8s6vzb2hKDBqNE2hXm3aXYz1GNwu5OLzrv3LKOysvuIVbtka_FwWcHjzEukoYmOQyib9dY4yTvyVtvV6jC_Uf_CLVMhQkqeMiD6_UUGDZH5hAJQfD2CIuQeDc98ebhfoeDJBimJ96BbycDFstfHHvsgaIGtqM4UAub6qIBcfoiJhLZOiIG8gP2-JKHzs9zZYnOVchl9OblI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇫🇷
آنالیز تیم‌ملی فرانسه تحت‌هدایت زیدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107529" target="_blank">📅 09:01 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107528">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107528" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107527">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107527" target="_blank">📅 01:02 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107526">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=BewH5ZKKfeIj-wXakqM_Drjz0YQowr3P9ojVGXE8pMlI3pLwt4CVcK8jjdMI8t1t560CpYHBGfCMm_xPsWlV1BDyb6c7skyxHmEDCQuPS-tAFN0U52g00xGRrAErkGBXskUYbI0zgnDtes-fPnNaIc5bAOGxDBmcAAfR2GgZqpFOPC4oXOfbbfW1YOK4_gmZtEg5gcVO_Ew19_ZR4T7EqohT-knUmCUcCGTHLndjstqNlNoThsAoYCrS10FN55tfK_C6JVSGl4FZBMJykNvSeZgXiNrk2gcSnxp5bwBYQjfsrNyMLkieE5ZXNCAymLDV4QzIQ4aDOP3o1PgZp0jTlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57b621a66f.mp4?token=BewH5ZKKfeIj-wXakqM_Drjz0YQowr3P9ojVGXE8pMlI3pLwt4CVcK8jjdMI8t1t560CpYHBGfCMm_xPsWlV1BDyb6c7skyxHmEDCQuPS-tAFN0U52g00xGRrAErkGBXskUYbI0zgnDtes-fPnNaIc5bAOGxDBmcAAfR2GgZqpFOPC4oXOfbbfW1YOK4_gmZtEg5gcVO_Ew19_ZR4T7EqohT-knUmCUcCGTHLndjstqNlNoThsAoYCrS10FN55tfK_C6JVSGl4FZBMJykNvSeZgXiNrk2gcSnxp5bwBYQjfsrNyMLkieE5ZXNCAymLDV4QzIQ4aDOP3o1PgZp0jTlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🙂
کنایه‌های سنگین ژوله به امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107526" target="_blank">📅 00:45 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107525">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPZkrRFl3p28dJrAac-HaZreGiCUhET_9lbm6ZzMVVW3GQNQwRWYUnFd2klqY1lvEYNi1OPp52dfI77o5QAmHtTPlKdcTAT1xriQTb3HvuewuH0-mwkY-ju1rUkUpiA54KeFsNiUeMYCjEw3jvqB500yTZjGB3yi_roVa_2cTPvtV5KX4zdzZuNzTVzpePK9OX1Oqh1YwSvtxkOjohe92ZLqJ0283ifmlwETY3a0ABKl6regcNwaCYHMni1myJOa0n-RG6JXoQLGeg1BW_sxROaS2aNe_Xu45n3wSY1YDU_q24muuX3VIKrGSp5kbQGim7NH_CZDk2WyPCcOny64HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعتراض میثاقی به باخت امشب تیم قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107525" target="_blank">📅 00:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107524">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MomElupu4cGDQnaC9Kr9BBPg5zYXDww_DiX2FVGRMkqlyIw1oHJuy0iuUzIbCwS4s9CpuvJwujL4b2ETvr8CBVHK7Gk-KJcDJuoetRyfVtsH40EC8rmrEe8TdvbBb4OK4qsjEXKxp9ty-QuawYRIFWr4BR-RLOq5-TBDi9ExFHPfPJ-lYg5DFWw4UjgBcQONAk67aHlyo1x6Sv4Wq8MchhBW6VmF7NoP3_DVWO-dbSAkvQPiiRUk64F4MlaaAqA7PGUn4CxhkbleUgcn9p7wsPj00bVQX8QK0Wo1wpx5CyGnrkrsBRTU58AB08YjrbDUsOZlNaeOo-m9OTYKuZlA2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
پایان بازی؛
🇪🇸
اسپانیا ۴ - ۱ کرواسی
🇭🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107524" target="_blank">📅 00:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107523">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=XZjs7puGz5LBNFtbT_5lkzMcBII7tNN2q_-rpfqY-Rr30i532Oci4TnRIzJ3ZyEEfEChhMTjHw9R9Hv2dJZlkK7n_Z6bmRzDJiDrk2jluuOK3pozGFC9HzycKBcvpcK2mgUJHOqBNfA_jC3kBfTcFy_j2fbKwfiky1Db9ff95l9VWKOkk1-lk32JSeTf3cdXLXR-LhL_n-p2ONr9v-pramt4AHK0N19CLneDVsAiNQL35RC8lZWE69grqft0iXtNvKjq6zcCsMKmXqaYSy3NHfB4azZg85z-LmlZDc5CkN94AZsI5pmSc6_c1pMlyCVblhQCRTnFfnsEicDWGLF0pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5febf615d8.mp4?token=XZjs7puGz5LBNFtbT_5lkzMcBII7tNN2q_-rpfqY-Rr30i532Oci4TnRIzJ3ZyEEfEChhMTjHw9R9Hv2dJZlkK7n_Z6bmRzDJiDrk2jluuOK3pozGFC9HzycKBcvpcK2mgUJHOqBNfA_jC3kBfTcFy_j2fbKwfiky1Db9ff95l9VWKOkk1-lk32JSeTf3cdXLXR-LhL_n-p2ONr9v-pramt4AHK0N19CLneDVsAiNQL35RC8lZWE69grqft0iXtNvKjq6zcCsMKmXqaYSy3NHfB4azZg85z-LmlZDc5CkN94AZsI5pmSc6_c1pMlyCVblhQCRTnFfnsEicDWGLF0pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل‌سوم اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107523" target="_blank">📅 23:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107522">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گلگلگگل سوم اسپانیا به کرواسی بازم یامال
😐
🔥</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107522" target="_blank">📅 23:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107521">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ehoXbl2yrVn2y4DpcjSNF0RU2lL_vbIEqVr-JKsQciy9a7asLzyi_Ui0uNdRIPgIaM-W9YIUbJFnaVLFcGBeuCbvEYKj6CstjbfQWtq6TfAPzXhMif37hSZ1qaT0b8jHkrAi4K7WWelk_RcEZJhRWm4JwSU31yWqH1JDLSX_dxDZDgwmBZxmpZ-8y7QwE9KCyHh-58n3iaJi2VcDAi4hgyeK-KkLtEsVRwUahJ1UPSXdz0qnHA2RVTHKsp5zM0ANwsyzbm_t9KaPCsqHVCXe4tqAa0vVrb6pGTlqaBuDtWrHk_7l6bpaczfgpvFe37DY-MTvRHsxRPmPXMGeFjtwxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/713c4da9c1.mp4?token=ehoXbl2yrVn2y4DpcjSNF0RU2lL_vbIEqVr-JKsQciy9a7asLzyi_Ui0uNdRIPgIaM-W9YIUbJFnaVLFcGBeuCbvEYKj6CstjbfQWtq6TfAPzXhMif37hSZ1qaT0b8jHkrAi4K7WWelk_RcEZJhRWm4JwSU31yWqH1JDLSX_dxDZDgwmBZxmpZ-8y7QwE9KCyHh-58n3iaJi2VcDAi4hgyeK-KkLtEsVRwUahJ1UPSXdz0qnHA2RVTHKsp5zM0ANwsyzbm_t9KaPCsqHVCXe4tqAa0vVrb6pGTlqaBuDtWrHk_7l6bpaczfgpvFe37DY-MTvRHsxRPmPXMGeFjtwxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
⚠️
قلعه‌نویی بعد از باخت به روسیه: از برخی بازیکنان در اردوهای بعدی استفاده نمی‌کنیم
ای کاش از خودت هم در اردوهای بعدی استفاده نمی‌شد، آقای قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/107521" target="_blank">📅 23:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107520">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
‼️
⚽️
امیر قلعه‌نویی: دو بازی اخیر ایران بسیار مفید بود و توانستیم پلن‌های تاکتیکی خود را به نحو احسن اجرا کنیم. انشالله در جام ملت‌ها دل مردم عزیز ایران را شاد خواهیم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107520" target="_blank">📅 23:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107519">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=jbPN44yLoRgf2fOGbgxC1S4qVny4Zp54__Xj_BeNDYwWL176ZXxuzmBJNyChzai2w7tC6vwVCMxHCTFeaO3uxMOUFueiiAb9QnoR4zWUYT8J9ru5RcfPeH6bOfZ18v4oB7sp2tJZ1P31abQ-1mJUra2knZBaCdGFjQnU2CYRPtlGyaR-wg7GyxnvWktuT0FTIILle77rNxEju-Wnt8zulyfuec9Ol_8h5u70xIY31yMchoH9M1C4jR7eCFds7s9XhQKaHCEqvlBMa_Jxm-Hf6zax4fZGeDHn2mNDBijcpqtkK9bWDodIWOVkwenGR7lrt3TegVTnfsheK_JQvBYzsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d86c5f06ad.mp4?token=jbPN44yLoRgf2fOGbgxC1S4qVny4Zp54__Xj_BeNDYwWL176ZXxuzmBJNyChzai2w7tC6vwVCMxHCTFeaO3uxMOUFueiiAb9QnoR4zWUYT8J9ru5RcfPeH6bOfZ18v4oB7sp2tJZ1P31abQ-1mJUra2knZBaCdGFjQnU2CYRPtlGyaR-wg7GyxnvWktuT0FTIILle77rNxEju-Wnt8zulyfuec9Ol_8h5u70xIY31yMchoH9M1C4jR7eCFds7s9XhQKaHCEqvlBMa_Jxm-Hf6zax4fZGeDHn2mNDBijcpqtkK9bWDodIWOVkwenGR7lrt3TegVTnfsheK_JQvBYzsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
پاس‌گل لامین‌یامال روی گل دوم اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107519" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107518">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=uQmUCRGDSeCu6RizbRvgPpPLHvFecKOhpXzj2oLhFDI4M5of0VIIrCswGY6bkLARDYqCiQxVAVr8qwgSH-35uqifxS_4mkCLhzgFkLN_M5NrnDcJX5Ve6uUaPWw0ZEXCOCbQxbb2vd8ZyJMMEMDgpCarrdlm_ItpZa2oeEff3y1XL0gSEHe7LOGA_blJzDwkPdngdJBwQ3OlMKLwBeTMGMEkQgkV3HFO24DMkq9ntrJ79QQ-5EzlEmVFDBamNEKM4NZ8mN3qr0qCkkRhcbkV44zv-ajnzdpghpKFeR05PDnMJQqEGlOFUxVxaah1Lg87z_VEBlza2IN2iF9LhtWPkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2651377ca2.mp4?token=uQmUCRGDSeCu6RizbRvgPpPLHvFecKOhpXzj2oLhFDI4M5of0VIIrCswGY6bkLARDYqCiQxVAVr8qwgSH-35uqifxS_4mkCLhzgFkLN_M5NrnDcJX5Ve6uUaPWw0ZEXCOCbQxbb2vd8ZyJMMEMDgpCarrdlm_ItpZa2oeEff3y1XL0gSEHe7LOGA_blJzDwkPdngdJBwQ3OlMKLwBeTMGMEkQgkV3HFO24DMkq9ntrJ79QQ-5EzlEmVFDBamNEKM4NZ8mN3qr0qCkkRhcbkV44zv-ajnzdpghpKFeR05PDnMJQqEGlOFUxVxaah1Lg87z_VEBlza2IN2iF9LhtWPkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول اسپانیا به کرواسی توسط لامین یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107518" target="_blank">📅 22:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107517">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلگگلگلگلگ یامال بازم گل زد برا اسپانیا</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/107517" target="_blank">📅 22:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107516">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38f859d863.mp4?token=Ia3WZnCm5WaG9RXOomityYtk82vcd6sRKx7_jh_nV5CRdXOq406-5cgas5U3v97MY6FSztjM9nrtJnXhey0jDO16N1FBtP1YiHNGfd7falQfHUYS9UTxuJhUJPF06JGZh0zM3UBGuobxsymkHJLhPsYSjMJ7DGnBdGMTB5efERFIpoAKr1Fww5fSi11HQZ0kKPkzPXJIVlzNptpQi808aP0y9tG64M9NuW9w9qEeaI4CCyrSTi20V3y0ezs3jivY7efNW1g3LkGu8qVhdsQ9By_SGzss3uveUVWuOT9EjaF-AsWJ6rSpMBxnB5jSN5LBWRnLakKDa_kjI8ePxVyyXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38f859d863.mp4?token=Ia3WZnCm5WaG9RXOomityYtk82vcd6sRKx7_jh_nV5CRdXOq406-5cgas5U3v97MY6FSztjM9nrtJnXhey0jDO16N1FBtP1YiHNGfd7falQfHUYS9UTxuJhUJPF06JGZh0zM3UBGuobxsymkHJLhPsYSjMJ7DGnBdGMTB5efERFIpoAKr1Fww5fSi11HQZ0kKPkzPXJIVlzNptpQi808aP0y9tG64M9NuW9w9qEeaI4CCyrSTi20V3y0ezs3jivY7efNW1g3LkGu8qVhdsQ9By_SGzss3uveUVWuOT9EjaF-AsWJ6rSpMBxnB5jSN5LBWRnLakKDa_kjI8ePxVyyXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
دیس ابوطالب به فان 360 فردوسی‌پور: فان واقعی اینجاست و هیچ شعبه‌دیگری نداره!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107516" target="_blank">📅 22:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNWD6nthcZNVvEPlUGLfwhjxEoZo9fqgz-RogqTZWrYrhjvubRIjHCgBSfGYoGOqDMVA0uaIsTVFX8QzarojRj_jesrZq6EWP8h7ZjS8Mu6rSF1hYA2PeYb66jlb_luuiXAfs2W82Qwpw2ocR99rAkIo_rcNFrT_7w2t66511-evJHnz85pr0uWYnJ3cG3A2HACW9eJk-cpBvy6_xEy8foUqaIvOmXbdFeOARVk-hte_f7OA-IkYjiINxwAvLJnkkuEP3j2LnVBhlgUebE_7zm1nDtASPAXk5TU5OLntDNZ6AGIAMxRApWmSACqIr01lYHGqhjQb1zTaxyDUsSiDCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان بازی؛ روسیه 2 - 0 تیم امیر قلعه‌نویی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/107515" target="_blank">📅 21:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
پنالتی برای روسیه</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/107514" target="_blank">📅 21:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L7IgmNzkHnmgrzXTtcBEAORKTSD-bsKhP5I8jxnZjuRej93TfV_zVo0zBXPImu4Qq8LYvJ3xvfS5uD2QmDdukrhvY2WYPmIF8GBPBee42RRqyy7UCRyOOA4z_yQDzNnv_2O_iWw4vOWZpzDQnovfGii-uy-PAh-33fN68zQhfclDwF8UhcS3I2M4eSS8oJp2ZIf9fp6xilJvYrg0R46Zg9xCGvN6S8sTEDbt52MDYKTPEZJBZ1VJOyhYWEr_pjqWZ3HzoZK14NIdlBxCXXxJMaYICBxWVWM5upfZrE7LYjwHVJlBPTFAXwmP1bZqvi_V_mCeQy1sYl79MVDWKJ4mGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
⁉️
وضعیت پات چطوره؟ ران پای راستت خوبه؟ همه‌چیز مرتبه؟
🚨
🚨
رافینیا: «خوبه.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/107513" target="_blank">📅 21:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=BQin_zp8HzGGVTjwlyQOi7Fu4vmAedL2t6nekqHUuBlya4fsP-jy_ukOQ-GBazUSJzIt_nynxaNkZmKtZsF832X3P_6txgbYLzKOdFVks_Ahej6_PKorcyLTDEeycguJik888VG9Sv-nQowmtv5WVmCWhdk5t24EPuhtGKwF-Cw4b3QvfCjSvHtx_l4b8QpBPY9GK8FisBJHm8jYQiIiGFkN457xmWs3iQCgVoFJsuQOdg_mm3so662cQ8Yz-aUD5G6Utlsq1b4eNhR092lQF08b90qjTN-2hLJ5ofJ6dGELhI2g7LMo-04AihIvFMW98ro6bBJjIZz5HvlD4RG_IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c98093c1e.mp4?token=BQin_zp8HzGGVTjwlyQOi7Fu4vmAedL2t6nekqHUuBlya4fsP-jy_ukOQ-GBazUSJzIt_nynxaNkZmKtZsF832X3P_6txgbYLzKOdFVks_Ahej6_PKorcyLTDEeycguJik888VG9Sv-nQowmtv5WVmCWhdk5t24EPuhtGKwF-Cw4b3QvfCjSvHtx_l4b8QpBPY9GK8FisBJHm8jYQiIiGFkN457xmWs3iQCgVoFJsuQOdg_mm3so662cQ8Yz-aUD5G6Utlsq1b4eNhR092lQF08b90qjTN-2hLJ5ofJ6dGELhI2g7LMo-04AihIvFMW98ro6bBJjIZz5HvlD4RG_IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤍
‼️
چهره درهم قلعه نویی روی نیمکت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107512" target="_blank">📅 20:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XK6xkIAvrxroYmEtQFzq5Y-ExbMxSxCqdgrGsF-SjtJdUwJtK6TRSR633IKIn1DiQhAYI0OsYFt2vIoXT3wHHLWn_Eof1Y4lFtYLfhEnDZsh18-PJ9sPgTiihOz445KfhGfAQH5EoFzRiXyeADq24aetTpmROcdEYrvuaZcFkEbXs4MPeoz5iGJOI2kJrA5CAciwS0RoMtkouQbfsJp4pEvfxbuOEUiYEAD2RI6eSn-PEqZxDcIFzhNFK2f9RcmZL6VIwTPvnyBvIYkrBnjx2bKpp0-i80WioJ0_7n8kX91Vh77QC4kRVeVj9IQ7mcs2v0z23AqzUza-R27VV0enqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
🇪🇸
اعلام ترکیب تیم‌ملی اسپانیا مقابل کرواسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/107511" target="_blank">📅 20:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6OhfIp8a3TnmZJREKqwZztJYQDJIVm2umOqod0jROy6BIQ675wioHLgLx2rwmISKluxh5Vub2wqLd9KQUIR8-AtNamybxUZ_ES_XYNKkMKmDHdUBvJKMcH8hXr-p_NzsQlr-btyMUjFbCwNKhcTLwWV3uYX0kylhH18kYSVu-6w8M2L_-frUtVp2X8sP3CwmWuaHsPF4ulD-Q4mIzHAgSJ6w-BJCsJ01McmcHogmgAvREUBr2Q92he4rvi1cGagcdPW3_VWDwAJOCX0kNsDvanvkqgsdlfId2_gtWI1Ptij2no3VvZkyw55qD8VevISk-YGbAkJeACfVZgIaFDRQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال ایران حالا بهتر درک‌ میکنه که این‌ مرد چه نعمتی برای بازیکنان داخلی و لژیونر بود و فوتبال ایران رو از حالت کیری الان نجات داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/107510" target="_blank">📅 20:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=Z462B7vqOiWXa0vC_M_msT64zclnqatBLxs84dIwr8xR4CUWSpE_CbmIZBT72nK3aenGuj7A3dvOtjXVT5uC7oCufPb6Wft1W51owbzn-xoIZX2MkDk2tagUW9wltsP4k71UYtJXmyF6-1p4jrX3nl-HowK5hU54GEsBsd4m8czxa3UeiTSOcYjZw9hntKSu-lYxSgDB_-m25ld5mLDlVcVwOJh0FHOE9fVszhaQeyOlex4IWkQ-jB1Uko7ml0dw98Rhw2V8zJX9WCaybAqUguhUooCj02ygSUdUn9Yp9e32NDjApW0OOb52IVyRQWMloWeccCsM2YQTQKdMvM4Z-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fa93705.mp4?token=Z462B7vqOiWXa0vC_M_msT64zclnqatBLxs84dIwr8xR4CUWSpE_CbmIZBT72nK3aenGuj7A3dvOtjXVT5uC7oCufPb6Wft1W51owbzn-xoIZX2MkDk2tagUW9wltsP4k71UYtJXmyF6-1p4jrX3nl-HowK5hU54GEsBsd4m8czxa3UeiTSOcYjZw9hntKSu-lYxSgDB_-m25ld5mLDlVcVwOJh0FHOE9fVszhaQeyOlex4IWkQ-jB1Uko7ml0dw98Rhw2V8zJX9WCaybAqUguhUooCj02ygSUdUn9Yp9e32NDjApW0OOb52IVyRQWMloWeccCsM2YQTQKdMvM4Z-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل دوم روسیه به ایران توسط گلوین (35)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/107509" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">‼️
گل‌دوم روسیه روی سوپر کاشته حریف!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107508" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=Mn-olcKgun9qvqf2NoDf-PjNcgZ6WoaSE82hzJvlrOLM1znO54pa2zQcEvO71oFKUBQITNuE6ecrjPpKorNrPUdBo-B25IawZ4hb4OQrodbgPepz1KVVzecypjPHdqkXbO0gVVinZcfTDY7p_QZJ_fnwT9u_9cdrFroyvVqsyOzJ4ryaKRMjqWfdsWCRmdryxG1hZarlpEwGBMUq-lmOMe9mPGKwDQbTQcQhI3BnVDQTpz5G0wZ9fh0keEVnYLg2z61Yx0JO9X6TT7rvqUSSozki9MJE_wGVYLXu65gThOaFg7Uw6pkVLfUDF-NCpCqjVq-hgiV7AvAn5SQGd5dKgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/117f9ab643.mp4?token=Mn-olcKgun9qvqf2NoDf-PjNcgZ6WoaSE82hzJvlrOLM1znO54pa2zQcEvO71oFKUBQITNuE6ecrjPpKorNrPUdBo-B25IawZ4hb4OQrodbgPepz1KVVzecypjPHdqkXbO0gVVinZcfTDY7p_QZJ_fnwT9u_9cdrFroyvVqsyOzJ4ryaKRMjqWfdsWCRmdryxG1hZarlpEwGBMUq-lmOMe9mPGKwDQbTQcQhI3BnVDQTpz5G0wZ9fh0keEVnYLg2z61Yx0JO9X6TT7rvqUSSozki9MJE_wGVYLXu65gThOaFg7Uw6pkVLfUDF-NCpCqjVq-hgiV7AvAn5SQGd5dKgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇷🇺
گل اول روسیه به ایران توسط گلوین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/107507" target="_blank">📅 20:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">روسیه یکی به تیم قلعه‌نویی زد</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107506" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107504">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENHNZVGX5wO1mZdoS6NJeJS7LtB90jKU49i5dY7xEqtoL5I5q7-plwoA0J3UexIOLpSRtui62vGZVdAoyU4_wmXnPdPLgTlpQW9yA3Z-lu4PofY3pJMYWLCoOQvyQpBsqEZxYX81g9SN_tR4gw8RaCrWFHyQKey6mpJ-Of7_Y3kNfCXKQZ92kJARormmhSPOQXjp6AkqPqti54WLsz193MMI57hNXgv3wup89xPwyhOVwOPUIe7-cuQzci3JKdL5_S2fRpP4r8AdNZwICL2_GmC8PPRk-i79bYFS-fhKRGhh_M5u_j46bZ1IgYoA2r0HVrFhxJ_XtzVTsOxFoqEOGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد  این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:  منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107504" target="_blank">📅 19:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107503">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIVDOxD3TAylE1BNDoRyO7oGIz-dSJ9zibIqGr2_Dk5VDPBhy68ghazPFa6zdlC6hRTTsSBv7TJpEGdnOX8WmrFRw7KRLFjlKD2gECL2OmgRrwzZeJCx3T1_k36EKC0BYRtjgT58jkmKgMFgDHGlXAJFaMLjOR37CPNTJKFH1ESjELpfgMIGs7_5qIy3Baa4meuz9ftOAFLIGv5CmvK2WxttphIyWwsWtyyisqfEuT3pv13LsgLVZV_MBIM-wcE7UXmkRIbI9HLhedjo9NOp2Ooc03krXKkNLs7KjxBI-RXvq7-rXo5FtkX8QqTd1cXHfACtHP-ju1BB61_P0UcF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لیگ برتر تو یه بیانیه جزئیات تخلفات منچسترسیتی تو فاصله فصل‌های ۱۰-۲۰۰۹ تا ۱۸-۲۰۱۷ رو تأیید کرد
این جزئیات تخلفاتیه که تو بیانیه لیگ برتر تأیید شده:
منچسترسیتی با تعدادی از شرکای تجاری خودش قراردادهای جعلی‌ای تنظیم کرده بود که توافق واقعی میان دو طرف را به‌درستی منعکس نمی‌کردند. این باشگاه همچنین به توافق‌های «صوری» دیگری نیز اتکا کرده بود تا درآمدهای خود را به‌صورت مصنوعی افزایش و هزینه‌هایش را کاهش دهد.
این باشگاه صورت‌های مالی نادرست ارائه کرده و وضعیت واقعی مالی خود را از حسابرسان و نهادهای نظارتی فوتبال پنهان کرده بود.
منچسترسیتی به‌طور قابل‌توجهی محدودیت‌های هزینه‌کرد مالی لیگ برتر و یوفا را نقض کرده بود. در جریان تحقیقات لیگ برتر، منچسترسیتی چندین مورد از وظایف خود در زمینه همکاری با لیگ و رعایت حسن نیت کامل را نقض کرد که از میان چهار مورد ادعاشده، سه مورد تأیید شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107503" target="_blank">📅 19:51 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107502">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=EzuzUVhsOYVTtTDp4Pp7vX-_dTnnhi07ruD7zJVq-V5sFFgmUGm7b-QpQbA-g98gwzHcToAE40tag2SyM6LPznvADLuyV560gcOVxJNR9N4YJFqjQjqg905XX5oEfps914N1vWAEPAUsRrTssLrVCE9cdFcBkPLg-rJhbi3gZN9oNTGWmKUG9RBgh5W4Ux5KisBNY2rv0MdLrvGCkk6PrLFGXsnxlyU7IWpFZCwu-Pgh9lRK5NIygJW3uzgFR7pMYKKdSTN-MzVvRO5SyuwwfU_CEBoEjy3OCqCatfKuuW0AMhSFMSP-G9qQjMCfgg2Jb081nWPDJCcSNZiTtU7Rkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11a09194b9.mp4?token=EzuzUVhsOYVTtTDp4Pp7vX-_dTnnhi07ruD7zJVq-V5sFFgmUGm7b-QpQbA-g98gwzHcToAE40tag2SyM6LPznvADLuyV560gcOVxJNR9N4YJFqjQjqg905XX5oEfps914N1vWAEPAUsRrTssLrVCE9cdFcBkPLg-rJhbi3gZN9oNTGWmKUG9RBgh5W4Ux5KisBNY2rv0MdLrvGCkk6PrLFGXsnxlyU7IWpFZCwu-Pgh9lRK5NIygJW3uzgFR7pMYKKdSTN-MzVvRO5SyuwwfU_CEBoEjy3OCqCatfKuuW0AMhSFMSP-G9qQjMCfgg2Jb081nWPDJCcSNZiTtU7Rkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باهم ببینیم قطعه ی زیبایی که استاد جواد خیابانی برای گلر تیم ملی، علیرضا بیرانوند تو مترو خوندن
🗿
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107502" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107501">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107501" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107501" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107500">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQHTtFKRHkLGBkIFdlRWXyI348y0_Buuk58urKSvG4_aZmCi7lbRqGH6f_mJcJTxO-A_bvYSzaZS3Y0QTFeNGCe4CTVR75rIba07eu52_hP-a-pFUubbCNOCvomfSQ4vLGHZ5Dw5Wq4gGygXsIuZsKKHbm4zuo_vj0VGbmqqCmsAV2q-ViDMn5bgcFqIBjJ3Un6aNNewmNzL21KLPdXhpeTHK40pI79JbwzdUMx1oA7urkujXl21XYpRcD_FT8gluq4K4_o9Bo6vysQV4Xr2Fdn2byMIygLsHjZ7r24UW53CTwGec_J4pH5l2DcvqqFaf8zhdzvV68M6oXrPAnCF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز کرواسی
🆚
اسپانیا را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
کرواسی: ۳ برد، ۲ شکست و ۸ گل زده
اسپانیا: ۵ برد و ۹ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107500" target="_blank">📅 19:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107499">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3gs-QY2dADj8o6ZNSBH-PBJBrZY50VxzElBYZLXU2ibTWMjOSolxRvXqqyA8Bu789AQQPsceKeSCBKJAlncMETBEtcfH8Z1MPKi5a3FJBgg9Wu2prO4MSTMHh-UOi1WY8EmzhQqpTe22ZQMO0qUWhFVQB0rlbtfp3FkxvkFjRfwUqAv2IdGN61V69rfD5vwaEpgLJDhVRHGVjL6oq52K8gAUW_iRIg8YfAHZm4p0_sbTtovLRPv5w5m3MZeAMor5zq6x-KoHDUI1vT6xx8Dl9BYV1184TnCCqh4LDyKMS8F1ZE9QdOSdlZJo0Pf_Jks9oqWJk3SlrNsXreOorpInQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇵🇹
رونالدو بدلایل نامشخص در تمرین امروز پرتغال حاضر نشده. تیم ژسوس قراره فرداشب با دانمارک بازی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107499" target="_blank">📅 19:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=t52EUDpwOCrRrABSwL1CbWkScDK3eHd2DK7uD6FRPevyNdXO6exO9sOAY-t1lSWbf6OIFXreR4yGBf5OA0n46Xd9tW0FtDo4yx9mrg_eucrC7lEs5j3SyM7kK2ngDJHluiYeoA8AWnqpFXEaOpyQZicWTcosVyesh8kgWWGn4QhYzeKhtRigRMHO8D8qO6h4a47GdyHcxsIjkzOx4uUkf9uXv123lctW2fMxl-MTuoz6vtTQOvOHM5721n6XtjcZwD0rzV9gVW1WliQeSShqO85eQA7YV8EiSUU5ROpvyosojANNcHbgveayKK6te7HqRTHFAve6DOCiWLmqm0fzdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68583cf71d.mp4?token=t52EUDpwOCrRrABSwL1CbWkScDK3eHd2DK7uD6FRPevyNdXO6exO9sOAY-t1lSWbf6OIFXreR4yGBf5OA0n46Xd9tW0FtDo4yx9mrg_eucrC7lEs5j3SyM7kK2ngDJHluiYeoA8AWnqpFXEaOpyQZicWTcosVyesh8kgWWGn4QhYzeKhtRigRMHO8D8qO6h4a47GdyHcxsIjkzOx4uUkf9uXv123lctW2fMxl-MTuoz6vtTQOvOHM5721n6XtjcZwD0rzV9gVW1WliQeSShqO85eQA7YV8EiSUU5ROpvyosojANNcHbgveayKK6te7HqRTHFAve6DOCiWLmqm0fzdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
صداوسیما والیبال را هم از روی آپارات پخش کرد/ بودجه ۴۰ همتی برای مخفی‌کردن لوگو!
📺
سازمان صداوسیما که به‌خاطر پخش قسمتی از یک سریال تلویزیونی در کانال آپارات کاربری عادی به نام نفیسه‌جون، از این سایت شکایت کرده و دنبال جریمه ۳٫۵ همتی است، بازهم برای پخش مسابقات ناگویا تصویر زنده آپارات را بدون رعایت حقوق ناشر تحویل مردم داد.
🤯
جالب این‌که همچنان سانسورچی به‌دنبال محو لوگوی آپارات است و مجری تلویزیون قطع پخش را به ارتباط با مرکز(!) مربوط می‌داند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107498" target="_blank">📅 18:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYxUCNQ-SO9UA83AFdiEOIzCAkqUhso-yODk9-Pt5wBt-n-4xigWVuajhddZSjctoUZxMqDmWwvWEu-TyuWXMDJ2WqsRWEs09ibWuYQxrxpJ6848c92koGG-AorVoreKPrwz9W6n2GskYmbwHk1Q4n0T-USpZHflXQwYRaeNyRbL5nc5GAugmcE6Vwivay7g_0NiAQhHP7k9WxyTlZ1Vk3YmBThQ_soHZMQWOkYzfNcQ2bDrg9JdguuWNcjFBmZxff_TdXr7-mvBQLPAzQySnLOPZu-TpnO6LxZNyGWMLgFyicNqqQx_4RE7a4kycqfk07t9Bp-WiWVcKhM5F2r4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ترکیب تیم ملی ایران مقابل روسیه
سید حسین حسینی، شجاع خلیل‌زاده، علی نعمتی، صالح حردانی، آریا یوسفی، رامین رضاییان، سعید عزت‌اللهی، محمد قربانی، محمد مهدی محبی، سردار آزمون و مهدی طارمی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107497" target="_blank">📅 18:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107496">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5PpF9DMXNpPcAa32SVKBGBSXkVRj670csLtWiXc9ZyNhbjfWVUUgwuzFBIhF3l2iXhAEMV2fz9hb7QjEOv1-QUW8DijQ9H-t1qepN9HbT4Zv3RW_4Ii5C55emjQoORVn9yucd20MpCZ4hxjjk-EeLx6EF6L7zl_tkCWSBAaV6NkLjPcSU9-HzsLrq_hwPuc5uAqRHxhAuyTxVSZbGpQIF8slW8NMH6Hv4QAIFdzycvuWclGhi7aDHwUd8wRmNpMZLMsItbfCHap69ggwyOhiWvFBTmoaagSzpAQqVRfpznOdJwzx_FHfSrPAtnItpwJa38xJpPkkaZoLYkUnc37yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚑
مصدومیت های کریر رافینیا
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107496" target="_blank">📅 17:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107495">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30660fe341.mp4?token=fLTECIdm_c9AvDw-jomH9z10wZE9B0dq794TUt5uSskH7xkbn3UFZH3KlnZ8VSPJT31jpSfhJyWhJUiAfo26wVQLinshODt1k3aqsAyKeqjVbLLHNxVgc6vOTwLGG9zprglz5iFqDR5abAgU01rDt-A5fSrLlrGarCrdb_YjV3ED8mKz-qo6-BHbVK3Kw2ybo5lte62xkhzOi8SxHKalbX_cwO2VZZ5JQg84V3zUs6CYNG6_hNu9Yx1LrYbLPQ4KlGlDnEOgqJTaK1FrVCoGgdf4Xb-i7z-_OzTICHaxojmQC9qyAcMb-8LwkWTt90lBehxz5l3fb_A4UpjqvTMj2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30660fe341.mp4?token=fLTECIdm_c9AvDw-jomH9z10wZE9B0dq794TUt5uSskH7xkbn3UFZH3KlnZ8VSPJT31jpSfhJyWhJUiAfo26wVQLinshODt1k3aqsAyKeqjVbLLHNxVgc6vOTwLGG9zprglz5iFqDR5abAgU01rDt-A5fSrLlrGarCrdb_YjV3ED8mKz-qo6-BHbVK3Kw2ybo5lte62xkhzOi8SxHKalbX_cwO2VZZ5JQg84V3zUs6CYNG6_hNu9Yx1LrYbLPQ4KlGlDnEOgqJTaK1FrVCoGgdf4Xb-i7z-_OzTICHaxojmQC9qyAcMb-8LwkWTt90lBehxz5l3fb_A4UpjqvTMj2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
على تاجرنيا: با والتر ماتزاری به دُمش رسیده بودیم اما پیام های داخلی برخی هواداران پرسپولیس باعث شد قراردادمان امضا نشود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107495" target="_blank">📅 16:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107494">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=MnH59JeXIeUHNoAHyDeObmW7LIlRz45z6Gn2Fj3k3BGxe9FUWg9sWm_Yev-_xzf6kfdnmn0BrILt6RS0w5o1nL5rcxrQquUrxqq2a90V-sNSs1KM1UAkIwVF1xSyauYYZlJ9vlH7-FjHEoviGnJQzwS5SVBwGGOyT3H256BCt7IQlH3W6mAxPVd49fbMut-JuCl9dLGu-TBxeQPcKaQdkxKxmup9lgjtOnln5bvADX4AxWNdxMootplo8yGSiNn4EMtOHM_A7KMiPh1_-VlkHYjR0gCoKlj5H8fSvLVYDOxs2aejcQJh_Y2b7ZRLTPBt_zb8TGJJ3kMbxed9o0O_Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa385d1d9b.mp4?token=MnH59JeXIeUHNoAHyDeObmW7LIlRz45z6Gn2Fj3k3BGxe9FUWg9sWm_Yev-_xzf6kfdnmn0BrILt6RS0w5o1nL5rcxrQquUrxqq2a90V-sNSs1KM1UAkIwVF1xSyauYYZlJ9vlH7-FjHEoviGnJQzwS5SVBwGGOyT3H256BCt7IQlH3W6mAxPVd49fbMut-JuCl9dLGu-TBxeQPcKaQdkxKxmup9lgjtOnln5bvADX4AxWNdxMootplo8yGSiNn4EMtOHM_A7KMiPh1_-VlkHYjR0gCoKlj5H8fSvLVYDOxs2aejcQJh_Y2b7ZRLTPBt_zb8TGJJ3kMbxed9o0O_Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
وقتی امیرحسین‌قیاسی با چندین یوتیوبر مصاحبه و از درآمد عجیبشون سوال میپرسه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107494" target="_blank">📅 16:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107493">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=lg1iMftpejYrlNHQdEzZychIphIJCrswbly5VXG1rwO8nM0C5Q6V4DaS1zatv3OMTHF03vZ1pyBTtcM3ER-a-hU9Y9LhNFeCEsLAfM4MmYTLMZKCP40OKFAfh1A5ixr4MwiAlssxjCgy-a5Bq9pnmxc-ymDt64UEh9Iy_xXy_CRJg6F_z4FW5IV-23gCeyoeg3sXjrriHe33pnRwXHQe9WIad3gQ9vGyHnP-JaeZXopYDwziqg769xG2qcOGrR6-QFxoNgTfLtW1SdNDvV2_niDlCQxmDGAAiScMKIAe_nfSDyiwjBjYSvE8v5WEIvILG_ynHTJCyUfWVP8O8YohYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/39b949da6c.mp4?token=lg1iMftpejYrlNHQdEzZychIphIJCrswbly5VXG1rwO8nM0C5Q6V4DaS1zatv3OMTHF03vZ1pyBTtcM3ER-a-hU9Y9LhNFeCEsLAfM4MmYTLMZKCP40OKFAfh1A5ixr4MwiAlssxjCgy-a5Bq9pnmxc-ymDt64UEh9Iy_xXy_CRJg6F_z4FW5IV-23gCeyoeg3sXjrriHe33pnRwXHQe9WIad3gQ9vGyHnP-JaeZXopYDwziqg769xG2qcOGrR6-QFxoNgTfLtW1SdNDvV2_niDlCQxmDGAAiScMKIAe_nfSDyiwjBjYSvE8v5WEIvILG_ynHTJCyUfWVP8O8YohYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
#
نوستالژی
؛ درگیری تاریخی علی‌دایی و محمود فکری درباره تیم‌ملی در دهه هشتاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107493" target="_blank">📅 16:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107492">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW3kbURZ4n_5SGi7II0H5MXuphlWuPR5qWgucJnfA_0cmQ_M5G6UkEJTtWZUUr_7r3CkLhequ6MQYb1RBFbqGl8n6yBn60NGWPIue4ptKRRqjjqnQIQBp2p0TCuFheont6a5EqXKRu0IRob92BqDE7pRbrAdN6fZwnGIsx9Ex8ekHTih0Tz032D80FWDBDjX6RJGOH300qSCL1eK6O4Vk1P6SdE9AKAYOxdgv7IiDFA1aygeyyBImviiicylBdYvg_PLNScYzZZb5uFKhBVvDCH8RSLcRNvO1ORx1KefGR8oPu1Z3lBQ3W3wgY-xTD8t8dE0Cwa91d6AJvKPLsWqAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📊
🇪🇸
میزان دوندگی تیم‌های لالیگایی با رتبه فعلی آنها در جدول مسابقات این‌فصل!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107492" target="_blank">📅 15:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107491">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
بررسی پرونده فساد مالی منچسترسیتی به روایت دقیق رسول‌مجیدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107491" target="_blank">📅 15:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107490">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚑
#فوووووری
؛ رافینیا در بازی امروز برزیل از ناحیه ران دچار مصدومیت شده و از زمین خارج شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/107490" target="_blank">📅 15:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107489">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=YMkkk_vmOLKi5Ndh9NnKDBsSDVK30zmYGshid6t_PFfEpLLl4QssPGhW7ue5twxGtplZQbygRDwkfMkY4JAfsUgcaaDZ-C0s5gxrv1aN4nn8IFHyqSfZ1Ds8u5GQFJLJ-m7aaha2mLWikjrz85eiuU3_bYb1o7JGhJQSpn4XdUfW53-gvac2m5aPh6iPNzFG8XHqA7wBFEToLPiUNlBMm1NJVr0elaCGuLhtRdvaJRvn0kkbm55Zj8Iyd9q6Cn3L9jbGEXN8ltOLjuREADQBhBNDfOmxFuk6Hl5Im2qeMW_HZuIanVlSwqZfDO2mV5a8D-MpcVn342zuvmp2ZbHVH3ErA7FIuJgBTdkQe3q6UgWdl4qmSC5QQheTjBAgAhHxBmMzheTOYpkUjkdY1wYgIpWvVOCmtAkGUCrYiXYgzy-yr0nDAJlJ1DlksMNsWBWxTWdkO-zX9njnI0gSd8WfN9zXwKQm0khVqO8z8F6D8tW2OTTHXGl3F81VvQrHWi0N0yJhyVH0rfIO92KHgZk_8OEiEU95J6jpRDhblbeye5BUVCoG5-CdbXz2JN0L7K2xfTCUsuYz7-HtOqen6okvceEBJXk22VFUatdsl21AtDsJ68rlJESbEtqgfj30L6hMOXe1ftBI1AFYfygMu2QHD77pxt54Ikk79dKq235kUmc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11af8c0994.mp4?token=YMkkk_vmOLKi5Ndh9NnKDBsSDVK30zmYGshid6t_PFfEpLLl4QssPGhW7ue5twxGtplZQbygRDwkfMkY4JAfsUgcaaDZ-C0s5gxrv1aN4nn8IFHyqSfZ1Ds8u5GQFJLJ-m7aaha2mLWikjrz85eiuU3_bYb1o7JGhJQSpn4XdUfW53-gvac2m5aPh6iPNzFG8XHqA7wBFEToLPiUNlBMm1NJVr0elaCGuLhtRdvaJRvn0kkbm55Zj8Iyd9q6Cn3L9jbGEXN8ltOLjuREADQBhBNDfOmxFuk6Hl5Im2qeMW_HZuIanVlSwqZfDO2mV5a8D-MpcVn342zuvmp2ZbHVH3ErA7FIuJgBTdkQe3q6UgWdl4qmSC5QQheTjBAgAhHxBmMzheTOYpkUjkdY1wYgIpWvVOCmtAkGUCrYiXYgzy-yr0nDAJlJ1DlksMNsWBWxTWdkO-zX9njnI0gSd8WfN9zXwKQm0khVqO8z8F6D8tW2OTTHXGl3F81VvQrHWi0N0yJhyVH0rfIO92KHgZk_8OEiEU95J6jpRDhblbeye5BUVCoG5-CdbXz2JN0L7K2xfTCUsuYz7-HtOqen6okvceEBJXk22VFUatdsl21AtDsJ68rlJESbEtqgfj30L6hMOXe1ftBI1AFYfygMu2QHD77pxt54Ikk79dKq235kUmc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
اگه‌یه فرد سیگاری هستی حتما این ویدیو رو ببین و برای دوستات بفرست؛ تاثیر مخرب سیگار روی سلامتی از زبان دکتر رهبری...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107489" target="_blank">📅 14:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107488">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=GG9NiRO_kxLZ3eXVrmUAKrPELYklKlEBGl2kZPkEwRnjdeUnlayUCH1z-e4gsEJEsr-5edjKRyaOUhMH8PxVID9Mwy2c2eeEK6KAUoCWZdkA4q6ynrtsGJPq65VaQ3YTUI4_65EdvLEn2ZMVqfcCDfjSf3ynYxiGUha43bfGyD60ACoTqm6Y1BcHodTBueMCggpq_fUADSYNOkPQREVVzPw7gsUIqriNPx0XYWIxKDZ5M6IBSvAPtsVAOHdT9Kv5PvKNLaSwBkduu9_XBQYtNGD-S5eh6UkjcCndXT3nEpa_4hwJinWvBUW0SF_eT7FwNOzDSycEWGHsfzzvGwz1Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd91aee857.mp4?token=GG9NiRO_kxLZ3eXVrmUAKrPELYklKlEBGl2kZPkEwRnjdeUnlayUCH1z-e4gsEJEsr-5edjKRyaOUhMH8PxVID9Mwy2c2eeEK6KAUoCWZdkA4q6ynrtsGJPq65VaQ3YTUI4_65EdvLEn2ZMVqfcCDfjSf3ynYxiGUha43bfGyD60ACoTqm6Y1BcHodTBueMCggpq_fUADSYNOkPQREVVzPw7gsUIqriNPx0XYWIxKDZ5M6IBSvAPtsVAOHdT9Kv5PvKNLaSwBkduu9_XBQYtNGD-S5eh6UkjcCndXT3nEpa_4hwJinWvBUW0SF_eT7FwNOzDSycEWGHsfzzvGwz1Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
🇵🇹
پیام‌واضح ژسوس به رونالدو پس از نیمکت‌ نشینی در آخرین بازی پرتغال مقابل نروژ!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107488" target="_blank">📅 14:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107487">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=oh5DpS8pXYL0-IJ6WyIvZCJhSxW6zoMfwb5lpQecZRsKZJ6M4nFJAzTd0JwcA5N9OiclLaTy7imLfqhcYOSj0gZhYmCMH8mCUrKd3c2JKp9Zf1vUYHpqPphSlbMv-hSGXO7QNEF2dX0iN0yR6egs1iccJKou4Om0dpZA_3RJ3No9HGo4NQydCFLAyEcWwansbOEIbhrM6xBxUgiaZbif5xWwcvmIMn1LA14DtbF7ngPTJyZ_EM6v5cv9swBQ2ovElfpcYz73-Bb4cjAp8JdN1xNhSz1TvWAF0x5d8RDJJ3y98mgYTia1L8znYFfEGZORs9izwKIeRLh_L8ILrNS7yoUz82UU0YpPBym_DQl3pzdjWzUfJqjeNijqwKh6_OkH63CiwDefgiYzQkx1bzeS4_nzXdptmo47_MK9QmPBJ9YTIOY6emGgVA7jDhAfFdVHD02FhMbQ2ydz88-8HcYA5WX4NaIiVuC8J1f6o9k4OGFOCrfxOPTXHsr88dH9KPdpL5tz0XIC-w5ZZ70CQu6LB6GD_9s0IUgN_KzUPtx6766GOECS6RGOK8Yx7QUL1LzTfffX2tYCRwRKvjIAbWXufyWpfUcaamO9Ydw-FdrcVhhvqsJjSQCRymszD0gvw6yU314008Ol5Cdugb7cd3hyI4z4YAMIc8T5a97UCpoSSS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bf450995b.mp4?token=oh5DpS8pXYL0-IJ6WyIvZCJhSxW6zoMfwb5lpQecZRsKZJ6M4nFJAzTd0JwcA5N9OiclLaTy7imLfqhcYOSj0gZhYmCMH8mCUrKd3c2JKp9Zf1vUYHpqPphSlbMv-hSGXO7QNEF2dX0iN0yR6egs1iccJKou4Om0dpZA_3RJ3No9HGo4NQydCFLAyEcWwansbOEIbhrM6xBxUgiaZbif5xWwcvmIMn1LA14DtbF7ngPTJyZ_EM6v5cv9swBQ2ovElfpcYz73-Bb4cjAp8JdN1xNhSz1TvWAF0x5d8RDJJ3y98mgYTia1L8znYFfEGZORs9izwKIeRLh_L8ILrNS7yoUz82UU0YpPBym_DQl3pzdjWzUfJqjeNijqwKh6_OkH63CiwDefgiYzQkx1bzeS4_nzXdptmo47_MK9QmPBJ9YTIOY6emGgVA7jDhAfFdVHD02FhMbQ2ydz88-8HcYA5WX4NaIiVuC8J1f6o9k4OGFOCrfxOPTXHsr88dH9KPdpL5tz0XIC-w5ZZ70CQu6LB6GD_9s0IUgN_KzUPtx6766GOECS6RGOK8Yx7QUL1LzTfffX2tYCRwRKvjIAbWXufyWpfUcaamO9Ydw-FdrcVhhvqsJjSQCRymszD0gvw6yU314008Ol5Cdugb7cd3hyI4z4YAMIc8T5a97UCpoSSS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
دیس دکتر ابوطالب‌حسینی به دکتر بیرانوند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107487" target="_blank">📅 14:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107486">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=p0ntQ4r0TXUF0_Gi2_45nTtZozbXECw1lpnQPwWDdWuSjhnKzX_J1b2wWjnmQ5Oi7wcovOCmjlS8gexrCWKnQ_jwiRMQiZ5C5s8vnxIDCaNiO05wwrsnLc7EBOs8xF9JU0tGH5JuRDMlta9K0JcRIK9Jay1tuiWqwXib1ay6TaewBC8trtUykGx5-YzbGnksiwfX6C-i2Ah9rJGGbIpBmpVemSlKFSgnfmZsSizNOOyehyj4gZfI-XV7pW0WU63lICPGKdpjOwmp_XRjWRI1UBmpJkFtEW1IYqNhFSTTKdN459acPdLeQnYyZHYNE1T-AT21aNvhUI19a4mWJUurCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09a02722eb.mp4?token=p0ntQ4r0TXUF0_Gi2_45nTtZozbXECw1lpnQPwWDdWuSjhnKzX_J1b2wWjnmQ5Oi7wcovOCmjlS8gexrCWKnQ_jwiRMQiZ5C5s8vnxIDCaNiO05wwrsnLc7EBOs8xF9JU0tGH5JuRDMlta9K0JcRIK9Jay1tuiWqwXib1ay6TaewBC8trtUykGx5-YzbGnksiwfX6C-i2Ah9rJGGbIpBmpVemSlKFSgnfmZsSizNOOyehyj4gZfI-XV7pW0WU63lICPGKdpjOwmp_XRjWRI1UBmpJkFtEW1IYqNhFSTTKdN459acPdLeQnYyZHYNE1T-AT21aNvhUI19a4mWJUurCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🎙
عادل: ناکامی تیم ملی مثل داستان تورم شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107486" target="_blank">📅 13:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107485">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=X1kcPBvdtf7ddNT0K4wXuWOAcGTnezK04xUQDuF3P1mKskXmWkcFxq3Q-3WYTHi0vo5QjYy20qCjOxHEzJ3Hz_eptyqBoGXQPjHwhyR1Ot-T3aIsFIoTlMC_SIa-cXWfDMEvNWshlYPlLh0qThOeTMo0CgUSEiOX7MzgoV9SiP2EPHRhWSJFJAZY8DpRlBOey0gFUj3jieR83IS78kXMBhelFrydRaxgEIQu4Pt2-0YoVVOekOQXd13dZeYxgyhfyQspTjNLGQ0rAwxnoFLgDgojH4BPGrO5qq0hb1W7pp_A7oee-MgRetvvq0Osb4NsWigqcOyCxdRRcAcXKUx5Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a1ee940a4.mp4?token=X1kcPBvdtf7ddNT0K4wXuWOAcGTnezK04xUQDuF3P1mKskXmWkcFxq3Q-3WYTHi0vo5QjYy20qCjOxHEzJ3Hz_eptyqBoGXQPjHwhyR1Ot-T3aIsFIoTlMC_SIa-cXWfDMEvNWshlYPlLh0qThOeTMo0CgUSEiOX7MzgoV9SiP2EPHRhWSJFJAZY8DpRlBOey0gFUj3jieR83IS78kXMBhelFrydRaxgEIQu4Pt2-0YoVVOekOQXd13dZeYxgyhfyQspTjNLGQ0rAwxnoFLgDgojH4BPGrO5qq0hb1W7pp_A7oee-MgRetvvq0Osb4NsWigqcOyCxdRRcAcXKUx5Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
📱
پست‌جدید سعید صادقی بازیکن سابق پرسپولیس که خبر از ازدواج‌خود می‌دهد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107485" target="_blank">📅 13:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107484">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‼️
نیکولاس‌سوله مدافع سابق بایرن و دورتمند این روزها مشغول دروازه‌بانی در لیگ‌های پایین آلمانه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107484" target="_blank">📅 13:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107483">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=SZ1EDb52vBSC5vr_NjSanzUVBb39HqilXrZ-j-ubcZSCpqoIEFq438SL-jbMMpRECq4UC3fvwbuEE7qhuKRFVlQRAWuznBEqucrDfs0WzRVqlzou9NpOBBnxbFhdKZbGwcqNyUCXegW2OLkfYx-f9ZfHHK2oEbqGkR6JacwydKpDz-wT6IY6zE-3i_jOoj5sBP6rHD3jEZrrCL5S5Iigk1f1jkrsHEjPcheAI2Ls1GRxhdgIYTsqpiXKu-vAEaPc3RI0lQHyu3Ee1o3s3VUUP7YulXRd7xKLxcCyNIdjla3LXTRsrXH8c-CHyjRZ90aUhGu6AbSPYwOTvX5mst4iLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf7aaba1.mp4?token=SZ1EDb52vBSC5vr_NjSanzUVBb39HqilXrZ-j-ubcZSCpqoIEFq438SL-jbMMpRECq4UC3fvwbuEE7qhuKRFVlQRAWuznBEqucrDfs0WzRVqlzou9NpOBBnxbFhdKZbGwcqNyUCXegW2OLkfYx-f9ZfHHK2oEbqGkR6JacwydKpDz-wT6IY6zE-3i_jOoj5sBP6rHD3jEZrrCL5S5Iigk1f1jkrsHEjPcheAI2Ls1GRxhdgIYTsqpiXKu-vAEaPc3RI0lQHyu3Ee1o3s3VUUP7YulXRd7xKLxcCyNIdjla3LXTRsrXH8c-CHyjRZ90aUhGu6AbSPYwOTvX5mst4iLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
👀
وضعیت وینیسیوس در بازی با استرالیا:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107483" target="_blank">📅 12:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107482">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZB2xlZRpsS8tCfeUzNbc3v22kxcvkqX9CthskxUVyotMLPu9kHy7jk3M0ACAU5NW9_1TO2XwSVQErY3wsdHfjT-MroS5pj190XEpcJfLrnDAVSXN7JKqGEQBWfpwBrmOfB_YEhKAbdjIBtWG8247er3E0olukTYbYkux9N2gTbXzBeiwEw6kjdD2j0MvUpXaLfXav1dEDGEqzV66C23IolZ3f2rVAKb4RUkIEJm-dugtemhOA2AbokWhZFOjrH4fDp7djiZX74ko5Pj_1eem7xYxeT845Kn8PbBBCR8nl02EOrTS3Spb6hKMkRTJNqf5ka1n6e0csUShIqN_ytMeNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
⚠️
علیرضا بیرانوند به دلیل تاهل، داشتن دو فرزند و شش سال فعالیت مستمر در بسیج، ۱۵ ماه کسر از خدمت دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107482" target="_blank">📅 12:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107481">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=Q--eFy8Eb84IgFIkC_18hbQkcjIOCnPcfoJc5ANlrWkN8Gtf9-lSTFvYuhC-pKaLxqSdqMk2M0vJOS6BBkzxpEyYlfwTF9Oxsktp2rlkg4ycBksVRn177dWUqX5d7-SZawLx79uUgwRKewSmQx_uDab01ENsM4wZ_SjKCwsPlo7AbhCdipncJW-gQEodzx6osLh_1BNSX7pTrVhtaj7BbTXB2MTuSNWKInj-AyHp26-duqLaL1RRHKoHIGo8xq1pkGL7vbj7oxgqXyDMR-rHyqMi-WzyvIBJId4GUspOYM8QE0c2uvFneojLnMxI4szSkABRxnlNaLfWga-SU6TERw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2592f7770.mp4?token=Q--eFy8Eb84IgFIkC_18hbQkcjIOCnPcfoJc5ANlrWkN8Gtf9-lSTFvYuhC-pKaLxqSdqMk2M0vJOS6BBkzxpEyYlfwTF9Oxsktp2rlkg4ycBksVRn177dWUqX5d7-SZawLx79uUgwRKewSmQx_uDab01ENsM4wZ_SjKCwsPlo7AbhCdipncJW-gQEodzx6osLh_1BNSX7pTrVhtaj7BbTXB2MTuSNWKInj-AyHp26-duqLaL1RRHKoHIGo8xq1pkGL7vbj7oxgqXyDMR-rHyqMi-WzyvIBJId4GUspOYM8QE0c2uvFneojLnMxI4szSkABRxnlNaLfWga-SU6TERw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
‼️
خاطره خنده‌دار امیرحسین صادقی از سوتی وحشتناک حنیف عمران‌زاده مدافع سابق استقلال وسط مکه
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107481" target="_blank">📅 12:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107480">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/deHyc_-g7ofsUyq4SPkmSLq4m32zhi7IjUtcfSZ7Rws7mcm5HTWWTKl6DO4-Zfvf2rQd8b6FGcIHlId6fVbspmB61F_WdG-B_mSj-n8rpvtVu1ukfSGj7uBi1PZp0xtTvZcOAWQhS0Q2cg6Dh-7NlXAcK-lqpIHo6j4v6UnVHhU3HHruZCovkkJxQlfX9BsVD92DplRAqqjb_paZwyba5UrIcY0J3Trtjbc51_8f0lhjSbevFfTw4DD6je3jEsROJvn7R5RtSK8CvTrU6-wnz_Z1b8OWWhmTFPDtcaQDuwt7xUe2q9igYgNnghWCCLUvKEWYD-7Qlr5CWEh9E1YslQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/107480" target="_blank">📅 12:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107479">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=s2JxWsAvpPyH8fBYfsNVO4vcnQ-sfXTvUFgZ_mzWvTbx7zsIrA5iqeSAkdr31GFxAq5AqqHuvWP3OuX9MH0HAnzDDmhcjXSvtuRQrCVo1VfZn8GqRAJETWfdn8cqBRGlVpSYcmILBxFIyaG0vkRNBwhGCzXEop1DDAlqdNuIAJ1w4j60RwhI86tQ4nT75OGfolYzleNL9ZCQMYQ_i6X83Kl9fC55DItJXpJJQxccV-lRkzkduAWxiDq-1gsoJScW-tMf8vaMQjerYYMuNcuYtbUjIPrC0ZURUbxmpp_zjrBpwPlslTkMdWvvVhprZ_Teb9DI2s5N9yFkXB0Hh9U_mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6f4de836.mp4?token=s2JxWsAvpPyH8fBYfsNVO4vcnQ-sfXTvUFgZ_mzWvTbx7zsIrA5iqeSAkdr31GFxAq5AqqHuvWP3OuX9MH0HAnzDDmhcjXSvtuRQrCVo1VfZn8GqRAJETWfdn8cqBRGlVpSYcmILBxFIyaG0vkRNBwhGCzXEop1DDAlqdNuIAJ1w4j60RwhI86tQ4nT75OGfolYzleNL9ZCQMYQ_i6X83Kl9fC55DItJXpJJQxccV-lRkzkduAWxiDq-1gsoJScW-tMf8vaMQjerYYMuNcuYtbUjIPrC0ZURUbxmpp_zjrBpwPlslTkMdWvvVhprZ_Teb9DI2s5N9yFkXB0Hh9U_mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
تشکر عادل فردوسی‌پور از ابوطالب‌حسینی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/107479" target="_blank">📅 11:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107478">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jYAx-hMWEa50z_7y-npyJtCbe1MpNBgI59O3FX4zBFUKESClZck61mFZREkzuL4vDZTw6keCuKtJHrsxzllcoGkvL2j77J-c3t2Rs4JKzW4pGM8DW4aQEYb8VGB5lrrWSel_o23esdHzIaGqIGf3yEygjIYHuz4LTPwOCR1jOcyWUXLxJu4UAaUQst8nvS3kE9rPY1C-5sY7T8N0h1Qvz5cVRsoybZ4Rk70Ui_kOH5-BqD3xlYAc67DkQMMPGDoxNRLuKQQnxOIJWmjbddcqtymBlgAzG9ievDjcN2XcHl-st45NJx0RtLv1LTBX853lSFoHHiabTI7vI42Hsu8w6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
💵
وضعیت دلار تا این لحظه: ۲۵۰ هزار تومان!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107478" target="_blank">📅 11:43 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107477">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vV7Lu2_HrnowXCHlI7tSvCISo71eu5iYpzIjIJiPLboEGsnLyHGJUhzP7jr0AwvY4b3AgQ6QokmvkCKB1kT-QLk2qcoh2_JbcBoSMhZYNBwN0kXdtBc8tbmohG1k4bV7UyfobYJL-X9jgcP1HSNfsPkqVRi9EVYg7XrwRE0MGZWZqLxFL-M42E2iAGyoDKE9EqfEPKRCklyjf-YupnLTPiwvAhclUQ5jZxUK2giEKooXsqvimnXsDv5m2PI2FaCLNDFZajqoF7AkeQwBfd81B9xjTtkSCyMXhyjfunupv825eDF85qFF87W4nD8OaZa8azMPmuy7I9tFPowo32CKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
‼️
🇪🇸
مقایسه آمار رافینیا زیر نظر فلیک‌و ژاوی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107477" target="_blank">📅 11:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKsxxw-X4lBxOuHgElo_J3WCbG3QcgqQgPSBzdoI3WPxgTPrx0dXuttiEENO8DIfFlL5BHSmfKbdE5aZE9MDg9BWrBC0CgwTmrvnADvwuzAUsmRM7jkWt_qih-dj1FG4Oupl7XoRKhPW6xYtyDe1y9YZFWdEs_5Gd2apBAPmemUopj3BR2MmbcOQ1Q1vzC3R5_4NdM8YEDt8qpDpjtmfBsxFRYNuKy7rdZOWDe38n--Wwm_y9D1a-K4BTwGQp1A6vfPBtslx_HNOuC2ukDXE1lHiOMStiCY56Dl8mLWVbOSYUqvcHb6BS_v1EjTivPQ8U8rEvpowNqywIeiDayr11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
بازیکنانی با بیشترین گل‌زده از روی ضربه آزاد در تاریخ فوتبال؛ لیونل‌مسی تنها دو گل تا تاریخ‌سازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/107476" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107475">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107475" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107475" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107474">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEjxu67QpmkYPpe_0JERlVPMsBstFG1m6P9GAC6zp2Jbs4SkpzmLC0x3FHXSo7sEH7_6NMAqjKpzUEgYKAXNwhS2gpzX0A-IDeZ_NZwXrJW1jF45xY_sLgXcqgdxYNCpU52PDOLwpJoJlZr1L7zz-_-iFICd_f7FAujCtsGfsKolJwm6CDfe1NW0vF4OnpRdL-Liiey1NnyB6EL0lL5mZBbhzSenRijkVtaNZLm_twCoTlbvdjfsyrhrcmZSkS8W8BUekpOBNM4bSF7GFogqFc0jFzJbmY7FX8XDz5ilS-jVGOnds_gQLXTMxMk8SNkVxIb02SJjk5nEGvkMEyu87w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
انگلیس
🆚
چک
کرواسی
🆚
اسپانیا
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107474" target="_blank">📅 11:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107473">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3862876082.mp4?token=XklZ6-zAh9ofC87Z8htbt-uRibSSYtQNPZpLueaTS4mjaJ7xJ19mb-VTBcNusYeQ7_4KrJY4WGW6SZxvqJ2EMaaav2GOunOCJyNpquRlx_-CFjj8NnnZvfccRMmx_JJ1rMCOBMhXJTGJdTyzSaDZM2kKgMNLzOOEMv4oddVETJHMGGSgEaZFkwRcJc97pPAnKfGyAExunWhyhb8nMRLM0-ryY5u1pPFyBTvoId4sU6p9PTOaBw-hOHsEPTHu1NJe9Duti-weNe17jb62iZLJDZk5cC6_z3tFuYLdTyitkW_ycw2PTvcqEw_E_tcX0r2VVJny9P2RFRdby8QUx_cX-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3862876082.mp4?token=XklZ6-zAh9ofC87Z8htbt-uRibSSYtQNPZpLueaTS4mjaJ7xJ19mb-VTBcNusYeQ7_4KrJY4WGW6SZxvqJ2EMaaav2GOunOCJyNpquRlx_-CFjj8NnnZvfccRMmx_JJ1rMCOBMhXJTGJdTyzSaDZM2kKgMNLzOOEMv4oddVETJHMGGSgEaZFkwRcJc97pPAnKfGyAExunWhyhb8nMRLM0-ryY5u1pPFyBTvoId4sU6p9PTOaBw-hOHsEPTHu1NJe9Duti-weNe17jb62iZLJDZk5cC6_z3tFuYLdTyitkW_ycw2PTvcqEw_E_tcX0r2VVJny9P2RFRdby8QUx_cX-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
😐
انجام پدیکور فرشاد احمدزاده بازیکن فولاد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/107473" target="_blank">📅 11:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
‼️
⚠️
ضرب و شتم دو نوجوان سنندجی بدون گواهینامه توسط نیروی انتظامی که‌در فضای مجازی حسابی جنجالی شده!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107472" target="_blank">📅 10:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=qK4HURCre8eVu4c1LIdQCR1W4T9wWCzb56dxUOVu9GBldVaG5OjjByZKGMi_0JaOJmh_U7efLNTgSdXfZtMUfkH9R1nJijHxxeaaUNA6tN8rEfTTCZVZDOBvGkLA1N36tjBRb5C3AHkfVf2fdx-9jfe0oln0tv-SglwZF_Wn98pG9Sx-9jn9eCjZKVHusIM2NZKdQBqXS2NqLJKrrP9G1GI4C-yKSmhE6T7kVzKUeZU8zXkPOBPHXrd-fgrT_P9AABdKtkzv719t7YxVGc2YyUG279xNlBVhBzCb9n4ig9jloIcunGrpUXrtPnH4mv3wpJHuY2o0Y2Gcxc448nyjpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae822cab56.mp4?token=qK4HURCre8eVu4c1LIdQCR1W4T9wWCzb56dxUOVu9GBldVaG5OjjByZKGMi_0JaOJmh_U7efLNTgSdXfZtMUfkH9R1nJijHxxeaaUNA6tN8rEfTTCZVZDOBvGkLA1N36tjBRb5C3AHkfVf2fdx-9jfe0oln0tv-SglwZF_Wn98pG9Sx-9jn9eCjZKVHusIM2NZKdQBqXS2NqLJKrrP9G1GI4C-yKSmhE6T7kVzKUeZU8zXkPOBPHXrd-fgrT_P9AABdKtkzv719t7YxVGc2YyUG279xNlBVhBzCb9n4ig9jloIcunGrpUXrtPnH4mv3wpJHuY2o0Y2Gcxc448nyjpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یکی از عجیب‌ترین مصاحبه‌های امیرحسین قیاسی که پس از یکسال مجدد وایرال شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/107471" target="_blank">📅 10:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107470">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=oHcXMpkV41LtMdf_CsyUES0fXHlbuyC5GVPF3Uifld_7aCxPwW0l8kSTW4zPtoHCTeYcwJNScLe-eF5O8RJ2Nqnk9Lo67134dgoIgVRw84ECnF3b_awwXNQ0URYCajCTIoMVrTwYI5TvluaXYaZ3utsMl2F173MHEUuEg_sllau25tpoYwhphV2LIGPLdQsEyZuZMyW3uMNUzNJph9G-zsXGZAj_3bUQPODSa5FJlfgBSvcRJgwfjeKfcltEIUiR18CGmfCEJOT0i6NwX4lGFqaKFmJYOt0uJ_C7Z5k_QOofJj8l__3pHfgMwh_-X9uLNwHClbAjmLj5FLUxwSzejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a5a16dba.mp4?token=oHcXMpkV41LtMdf_CsyUES0fXHlbuyC5GVPF3Uifld_7aCxPwW0l8kSTW4zPtoHCTeYcwJNScLe-eF5O8RJ2Nqnk9Lo67134dgoIgVRw84ECnF3b_awwXNQ0URYCajCTIoMVrTwYI5TvluaXYaZ3utsMl2F173MHEUuEg_sllau25tpoYwhphV2LIGPLdQsEyZuZMyW3uMNUzNJph9G-zsXGZAj_3bUQPODSa5FJlfgBSvcRJgwfjeKfcltEIUiR18CGmfCEJOT0i6NwX4lGFqaKFmJYOt0uJ_C7Z5k_QOofJj8l__3pHfgMwh_-X9uLNwHClbAjmLj5FLUxwSzejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
محمد نصرتی بازیکن سابق تیم‌ملی: آقای قلعه‌نویی آن مصاحبه مهدی‌قایدی را نادیده بگیر!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107470" target="_blank">📅 09:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107469">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=HmNaWhiCe2znyAlfmvNByk9n1BfDeM0DJjWjLrlmBUpBKgeAIz5Df4bVF7hcsf3BmxT2rU0eVswPixzp4iQ6RSFP11s8vA_RHybpE6U7mTRidGw9B9mUlKUpoFDaWEJbGS1yPHpWSBG8XguHg8EhIPEf3XAoAql8HFOe1AVrDWUM5xzjghhSGwv57H7aQfRWebeyinIBQ0ko9QX-q4Qt1inEV0M-FTnGsNSfFV3jQjmQQr7xHRJMJcjFxi4paeqMTUStkE8Qp1ahy5PJWFdP03Z_8IqAHxfp0uE9HEMPe5ISCYB6rK9Cecg16pN2hRBqxl_2W_gcsjNUVtZJf-D2Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e0c6152c5.mp4?token=HmNaWhiCe2znyAlfmvNByk9n1BfDeM0DJjWjLrlmBUpBKgeAIz5Df4bVF7hcsf3BmxT2rU0eVswPixzp4iQ6RSFP11s8vA_RHybpE6U7mTRidGw9B9mUlKUpoFDaWEJbGS1yPHpWSBG8XguHg8EhIPEf3XAoAql8HFOe1AVrDWUM5xzjghhSGwv57H7aQfRWebeyinIBQ0ko9QX-q4Qt1inEV0M-FTnGsNSfFV3jQjmQQr7xHRJMJcjFxi4paeqMTUStkE8Qp1ahy5PJWFdP03Z_8IqAHxfp0uE9HEMPe5ISCYB6rK9Cecg16pN2hRBqxl_2W_gcsjNUVtZJf-D2Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👍
🎙
تشکر هانی رامبد از مردم ایران بابت‌ حواشی اخیر: مرسی از حمایتتون!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107469" target="_blank">📅 09:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107468">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TE2J2HLmRCAo1ftABnJ_sPuDLHMgfel5xD5AY48UF81flwckQyL-lCwzoJXRFSChOrKsxXrd6DrogtLWJN9unPixem4Tkj-ytC04dfZvBpFq8tJ2gAZnFdBWML8D7EZ4OjSYMhbG3jMu5Y1Cz7Qsfd09LhCIFqWs6bzoattyr-z5c7VkWZOaWY_ODDXUjKYEDvTA4ojtMar34tVb2X2xyKKFZ1Qnp4U2Xojx9YmgS9gLM8_jtIOnWDKB6BpY9j6rotT0CwsomcqQFQz2cD7XrwKT2z8PZ7630Z2CUo-vl9da3TYdNZ1ZlJwMRfbnajXXj9sNUwIw9jqpZjW5Fa7Q5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
‼️
تیم ملی اسپانیا هیچ‌گاه در دیدارهایی که لامین یامال را در ترکیب اصلی داشته، شکست نخورده :
🔴
۲۹ بازی؛ ۲۳ برد؛ ۶ تساوی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/107468" target="_blank">📅 09:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107467">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=D43d2LVAJRNp8E-E0tYSmaxS1Uhv3YDgJhftwoSJwgaTjEvxsbqx2ij6yhfoIjH_ShQsemmDbhi2WkD-tgl12Oqg5qsP14r1uKZiB47OcPrcrapkpso0P3vnOp3WqxCRIRc_Y24KmxQ9IOoOInX8FZaGvHC_wRvc6Ux-P4T7qtUPcsIoiegXPeY3IKw-8dJkcF7JlBKr-BVqzfGWaMVdVAQbcDIIOapUZpKX0A-hf1UhDYtjuPSuhbje1kxnE10aMpmR_0u3NjgDsqiukfysFPb3F6UNswmJnbJkQNQuy7ltYrxvZX14AVH7aKdbykYfOuagMqpHF3CqNM4-kFxISIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd2d848cb.mp4?token=D43d2LVAJRNp8E-E0tYSmaxS1Uhv3YDgJhftwoSJwgaTjEvxsbqx2ij6yhfoIjH_ShQsemmDbhi2WkD-tgl12Oqg5qsP14r1uKZiB47OcPrcrapkpso0P3vnOp3WqxCRIRc_Y24KmxQ9IOoOInX8FZaGvHC_wRvc6Ux-P4T7qtUPcsIoiegXPeY3IKw-8dJkcF7JlBKr-BVqzfGWaMVdVAQbcDIIOapUZpKX0A-hf1UhDYtjuPSuhbje1kxnE10aMpmR_0u3NjgDsqiukfysFPb3F6UNswmJnbJkQNQuy7ltYrxvZX14AVH7aKdbykYfOuagMqpHF3CqNM4-kFxISIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇮🇷
پرونده قهرمان فصل نیمه تمام؛
جنگ بر سر جام نامرئی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107467" target="_blank">📅 08:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107464">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107464" target="_blank">📅 01:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107463">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KzZeWl0Zbj4KkJx1UUYHMMKjlOfrXXA39sl8up3H7qCOBStsicXQIzTmzTJh9FgtfKyUHqO384bOea0MaW9808_1ku-KNPl-BvC4PixxBbDDuZP2BV8YkNr0-sqAS_bx60ijL5XDL7I8YQKqg0AXCwA-nGtqRKbno6O1fKPJtHbuWXHszEoo_9CiAeyQw-_g4iAf7R9-UI2JACCJN2ocN8bq-XsKZo8dSAKiSZtLFH0gs89ZI-lw_Vduarxsd4wm3tKFTiEx_QNIh6x4MVIGA3ofCoLalnE7Qr-NhRyCor7Z6c64o7_snCRQ-6vEMDtHijrNcBeHKmyKro3OsuB_Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
❌
⭕️
🇮🇷
با اعلام سخنگوی فدراسیون، قراره جام فصل گذشته لیگ برتر به شهدای میناب تقدیم بشه و استقلال یه لوح یادگاری بگیره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107463" target="_blank">📅 00:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107462">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=G6Q3GMxRDrd44HbDtvGHqlp3PkXl1PIHw7pSuUHcGT7Hbuoya5tojwD71qjP_DjUic9-PUP6EwT65Bz42l1ycyqiLEqHuHpXYCig46bwXUKSy8fcVXxezqLbHVtwHDusNbudy_-5f4HHpQ0ta17bEmLHivN_a2hlQr6ZrOpKfjZzafqaAogL52fcjQgeDLwzbll7yW1FDhK_1hMSQjgH4NVHsS0QBRG_251SMzYnlU1MU2vwD6x6ImZzCUwXE9IP38M8F6CSgXF4XqYiIINdex9w7v1WtVSwq8T9SB4pKi9CocwVxgon2S08lkNlVcqASAaNR2SLVfL42qC889XdeJ6tPucaRbkcSUoViynEB2L1CRq7TrSaFWLPvl-Mvbs7vIDR3RyNNWc1WeyLNyq0wGalt5dVcpxSXpxsxmZkfKC_2D6NPGjI5W48WSVXz7Lof8VTCBSzlJ12L6Desj_6b5U0F5boGBWS6ubaBkBahxYEvDGKdwoJD2JeD0L2SeVMY0D4Bm5R-yIujWcDA-8i_2OsK0x2_a_SKBoT3XF2Klscy6t_4-Kkm9S9UVQWPCcJIKmpJxDsfh9XSxKCt0ZU9sRcXBk8DpNFcNV6JBZ4WIgKLlkSxY3iPeVRfra-fW9Idu7WCiMl3hInvdq-1q3k1koH4CN0VPsKVF9Jw7m37yY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/950f5d5e0b.mp4?token=G6Q3GMxRDrd44HbDtvGHqlp3PkXl1PIHw7pSuUHcGT7Hbuoya5tojwD71qjP_DjUic9-PUP6EwT65Bz42l1ycyqiLEqHuHpXYCig46bwXUKSy8fcVXxezqLbHVtwHDusNbudy_-5f4HHpQ0ta17bEmLHivN_a2hlQr6ZrOpKfjZzafqaAogL52fcjQgeDLwzbll7yW1FDhK_1hMSQjgH4NVHsS0QBRG_251SMzYnlU1MU2vwD6x6ImZzCUwXE9IP38M8F6CSgXF4XqYiIINdex9w7v1WtVSwq8T9SB4pKi9CocwVxgon2S08lkNlVcqASAaNR2SLVfL42qC889XdeJ6tPucaRbkcSUoViynEB2L1CRq7TrSaFWLPvl-Mvbs7vIDR3RyNNWc1WeyLNyq0wGalt5dVcpxSXpxsxmZkfKC_2D6NPGjI5W48WSVXz7Lof8VTCBSzlJ12L6Desj_6b5U0F5boGBWS6ubaBkBahxYEvDGKdwoJD2JeD0L2SeVMY0D4Bm5R-yIujWcDA-8i_2OsK0x2_a_SKBoT3XF2Klscy6t_4-Kkm9S9UVQWPCcJIKmpJxDsfh9XSxKCt0ZU9sRcXBk8DpNFcNV6JBZ4WIgKLlkSxY3iPeVRfra-fW9Idu7WCiMl3hInvdq-1q3k1koH4CN0VPsKVF9Jw7m37yY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
تاجرنیا، سرپرست مدیرعاملی استقلال: ترجیح می‌دهم به خاطر بازی حساس مقابل تراکتور فعلا درباره مسائل قهرمانی فصل‌گذشته سکوت کنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107462" target="_blank">📅 00:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107461">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=WQ-2UI0e2W1dDnY0DEWOs8jMLr3bzEcZqjev9QNhpUxm5Ayh3k34W2xN01GhYCWCnfY4Yw9n34siWJIdMRi9sTv5VekFMMr5RcYQvQx9XuZifuMahBHiakHwbdSHsafokWUJxgXHKKgdkCevHb2n7IyOBuCglOcZCai-uSwdHmvMLrhuCj_nrioUW1pU_2ESmLnnpEcZ0V9C80mhTg5BkA_nC4m4it7lFwPpNZud68GGfoDyyv9c2wT9gNVGbeKuMTM0xCXHKzqHLMYTxl-2AGVwaGF_V3gq_rdUAONoCRwOEknT4sKrEaYzKd6oQKHddowtGiyZvtxSKXZLg2k5gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe4b115fa.mp4?token=WQ-2UI0e2W1dDnY0DEWOs8jMLr3bzEcZqjev9QNhpUxm5Ayh3k34W2xN01GhYCWCnfY4Yw9n34siWJIdMRi9sTv5VekFMMr5RcYQvQx9XuZifuMahBHiakHwbdSHsafokWUJxgXHKKgdkCevHb2n7IyOBuCglOcZCai-uSwdHmvMLrhuCj_nrioUW1pU_2ESmLnnpEcZ0V9C80mhTg5BkA_nC4m4it7lFwPpNZud68GGfoDyyv9c2wT9gNVGbeKuMTM0xCXHKzqHLMYTxl-2AGVwaGF_V3gq_rdUAONoCRwOEknT4sKrEaYzKd6oQKHddowtGiyZvtxSKXZLg2k5gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
علیرضا بیرانوند: اصلا دنبال معافیت پزشکی نیستم/ دوست ندارم به خاطر پرونده سربازی من، نظام‌وظیفه روی خیلی از بازیکنان دارای معافیت پزشکی لیگ زوم کند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/107461" target="_blank">📅 00:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107460">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
💵
⚪️
🔵
افشاگری عادل فردوسی‌پور از ماجرای پول گرفتن ۷۵۰ هزار دلاری فدراسیون از باشگاه استقلال، قبل از اردوی ترکیه تیم ملی بزرگسالان؛ نامه شریعتمداری به تاج برای برگرداندن پول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/107460" target="_blank">📅 00:29 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
