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
<img src="https://cdn4.telesco.pe/file/tKjgkr8ZBMbrIiHqtyU0w0aT8KExDs-KZueiyBkT5db9_dETSNOJO1lyyTMx0rqG5trob9VxbIfHQHNp_82x-HjZIIOfkLIDOp5VVovkZ0Tdz8Yv_w50K5yexnz9amaDQsBqhxCb7pTsgEzTho_sUQHyl1saUEzUYkMYuBcf-dDBIWPTHl8wsMy-Nedjgemk3ToxSGTgUD3rxTX5fHjE4ygUIzwKVHnnWAWe_N-GAV2GlZ7QT2K05fWAEsO8cYrG_tJVsgDkW-6q32Hsd97xdeZYtlz9_8o-TZl5y3uUirnYa8BoO1bUr-CWQYyX4qppfG_EC1yFjeCWFfkHoCPQxA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.02M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-08 06:39:04</div>
<hr>

<div class="tg-post" id="msg-150131">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی: ممکن است ترامپ پس از انتخابات دستور بازگشت به عملیات رزمی گسترده علیه ایران را بدهد.‌‌
🔴
ایرانی ها اعلام کردند تا زمانی که واشنگتن با بازگشت به یادداشت تفاهم موافقت نکند، امتیازی نخواهند داد.‌‌
🔴
هیچ پیشرفت محسوسی در مذاکرات…</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/alonews/150131" target="_blank">📅 02:59 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150130">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
آکسیوس به نقل از مقامات آمریکایی: ممکن است ترامپ پس از انتخابات دستور بازگشت به عملیات رزمی گسترده علیه ایران را بدهد.‌‌
🔴
ایرانی ها اعلام کردند تا زمانی که واشنگتن با بازگشت به یادداشت تفاهم موافقت نکند، امتیازی نخواهند داد.‌‌
🔴
هیچ پیشرفت محسوسی در مذاکرات روز دوشنبه حاصل نشد و ایرانی‌ها چیزهایی را طلب می‌کنند که واشنگتن نمی‌تواند آنها را بپذیرد.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/alonews/150130" target="_blank">📅 02:38 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150129">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oO0wZv0WzeDadT2xy5fKRrog3k4tT-pzGUEs-7q050pjGlclN7WQY47aoxGWYXA_jv6JmOkHki3oENCJpbWYyfRTB_F3bNQ2dCV-YP31AEpbU9oHDSElTI9fhwvrF4H9k3bH5VWqeGVdkwvbdHN0OlnvsxEOXXUT33uaxlrCgAUlX3WrzBzxPfPTvxhHeEys2WhwfVYI5hJS_8cfmgTF2QmAF27gNjDZwngqXTr51ukVRprB_aJ5qbhYdUjb6E8-WGAd-CFRg5BfQx40B7gJgkQDVk7FNquJaliSC0lF4oaNxySLs94evNn5T7VakcB0TjGAKeTM8kKTAClKWqpeiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
پاییز برگ ریزانی خواهیم داشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/alonews/150129" target="_blank">📅 02:05 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150128">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
ایلان ماسک:
هوش مصنوعی در آینده خیلی به نفع مردم قراره باشه، بخصوص باعث میشه درآمد مردم بدون کار کردن هم افزایش پیدا کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/alonews/150128" target="_blank">📅 01:52 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150127">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=SeVhtJsohqpA-3Zg4gf1LPwmNkyy21mTdAOMqhUsYieZ2uUaboLmTSaWIsybmiXU3agVvnO-uYoWCEQfDTrwkSTqopPZdOKk00jEFV2D8o41PlioO6DM8z2_0bz2Ye1PQRCr0J5LtMlfw9Q-EKSRDHxHLHrOqIlIPyNDBvCFcETVOM8Tl7XvxQZIf1JoHGlCAuBwZyGB2MHGW5I1QUYOVNUsUZSRR1i1LBDVaYBkfyiZXarhqRRSlBKiVLOW5VFTk1q6vGqZzeKCh0ELgOq4FCutjVpTD6S1NO-9xezLSyRS1MUkMdpApE6wBSRqtFlKqPdAtHkKnEryDlenT1_uXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/165b51a72c.mp4?token=SeVhtJsohqpA-3Zg4gf1LPwmNkyy21mTdAOMqhUsYieZ2uUaboLmTSaWIsybmiXU3agVvnO-uYoWCEQfDTrwkSTqopPZdOKk00jEFV2D8o41PlioO6DM8z2_0bz2Ye1PQRCr0J5LtMlfw9Q-EKSRDHxHLHrOqIlIPyNDBvCFcETVOM8Tl7XvxQZIf1JoHGlCAuBwZyGB2MHGW5I1QUYOVNUsUZSRR1i1LBDVaYBkfyiZXarhqRRSlBKiVLOW5VFTk1q6vGqZzeKCh0ELgOq4FCutjVpTD6S1NO-9xezLSyRS1MUkMdpApE6wBSRqtFlKqPdAtHkKnEryDlenT1_uXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تتر 259 هزار تومان
‼️
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/alonews/150127" target="_blank">📅 01:27 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150126">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">‏
👈
وال استریت ژورنال:
به احتمال زیاد به زودی سپاه برای بازپسگیری کنترل تنگه هرمز حملات پیش‌دستانه علیه آمریکا را آغاز کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/150126" target="_blank">📅 00:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150125">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVs3v_KDOuzjBCT2lgO_GtnLYWKnmG1J-xRWB73tR1kFHFEkU7yM02yvQcyUu8AMbQ71ExAq39yRYD3xk0TTXtO7QI63Cz9PsBehO34NMtAKDjzjYvZbmGRkIR-_VphNkXYs7vSz2rnffwo8h_FjA5QPfJwU9Fx6CkB10xGeqWA2tY95vus5gPlO0RwrV5ewtkG2Mc8kdSH2gEdTYX6JTjetLBOIxehysp1S9-O82oODFrUimlFLfFRhhKcalI9R7tKaYTp4ZK-_Ffq4M5ErSh4HJDrAgt2c7ZzffPHa9AvRscnAM-Zr_BfZ8WzJwu4CMCtDUXOUgMo6098pbix1OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میرباقری: فرمان ظهور امام زمان صادر شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/alonews/150125" target="_blank">📅 00:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150124">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb12dc46c5.mp4?token=aTNhDFTB7Uz9160A2LrJPtzfKGW9bkVGmDvxbpSVN-cwUcm8wne3-eIiuTUkdL5vS60mjiK6BE81tZ5AnKQeadkj1peW2KiVDZ1JFCNaItjqiDKskh9cREr4um2IEIUwku6rmZWpzNJNDgGiO3Ka-Nu5TJNB2twLRA9by3L4Am-zljQDc4xkNnOX8M3eqZNEBW8MJA53Bj8ZSHGWMmN8BHjYaOZzipz9lNu1Zw1iAEV876cWe95icKmnjafzDiLcbVrrC8rm9bGQcEN8lLvTO3n1lzp_vEGYP4xuzFu0b8zxL5wafuYYVo9rPG2eD9X-yA38sn-pgD2LTxUokOtD1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb12dc46c5.mp4?token=aTNhDFTB7Uz9160A2LrJPtzfKGW9bkVGmDvxbpSVN-cwUcm8wne3-eIiuTUkdL5vS60mjiK6BE81tZ5AnKQeadkj1peW2KiVDZ1JFCNaItjqiDKskh9cREr4um2IEIUwku6rmZWpzNJNDgGiO3Ka-Nu5TJNB2twLRA9by3L4Am-zljQDc4xkNnOX8M3eqZNEBW8MJA53Bj8ZSHGWMmN8BHjYaOZzipz9lNu1Zw1iAEV876cWe95icKmnjafzDiLcbVrrC8rm9bGQcEN8lLvTO3n1lzp_vEGYP4xuzFu0b8zxL5wafuYYVo9rPG2eD9X-yA38sn-pgD2LTxUokOtD1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آموزش زنان جانفدا برای مبارزه نظامی با ارتش آمریکا و اسرائیل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/150124" target="_blank">📅 00:28 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150123">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R0jXziD_Zyzlw18KlCxu_IDxo_-IrT2vx1-ynDHGHLa0N9k0OOKOKc0ADDJqMyG8HeNMaasosD_93hFXOzNF89T0NQ6fQAH4GAROIJKcSRrGYREnlsSsT7AYm-p1wNmkHaGIiLTNEWYprkZeYbc04pQxJvb2nntrboTO_Podg-5Ttoz_Vg8Y3xyyxY4L-SLCFU91yatuXPo8cec6Bn2DrM2nbR4Da45Gpn9MfKDfd7SGC_YHS-4FOf9BHciNqollfabFCZ8LSvOrR8WPVxpJI3GmwvbTSiDvkSGiGk_bCLRlcB8AHFjH9euygxyTJmwoHgOlLCK4XahEQ2xqnUB73w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیانیه میلی‌گلد: بعد از پیگیری‌های میلی دستور آزادسازی طلاهای میلی از بانک کارگشایی صادر شد
🔴
خدمت تسویه و تحویل که به علت مسدودی دارایی‌های میلی در بانک کارگشایی مختل شده بود، فردا عصر پس از دریافت طلا از بانک کارگشایی به روال طبیعی بازخواهد گشت.
همچنین طبق دستور دادستان، محدودیت‌های اعمال شده بر درگاه میلی رفع خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/150123" target="_blank">📅 00:20 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150122">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
دختری که پاشو میداد پسرها بخورن و فیلمش رو منتشر میکرد، بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/150122" target="_blank">📅 00:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150121">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEhqHpXlK8rO2LxOhFpAjKRZ1LlnTF0EcY--m8CA4tTUG5S_UZ7NMheZr8innY29-BYZHkx9mV4CbDbM_MTtWAx6b2YmPivOluGDK2ezj-iP01CbDL27b3fIYyktKu9dQgk4IRZ1pAKdKBzdx0TtGaWCiuTmjL9GMjhDUcwVc6DWqgpVU4rflYlFRB_dRet29BWB3Le4h06Hs96AhgjsVEtqgvbahwHvC2r08YLjiG8V-rOIO0WpzplODeCpUMucisqvQF-bXVQbHKCd97JzAXIhWpOpy9vxypMunDcPJi-0Q1PPXTTS5YNkCMNn5Wpfmph15LGmnN2P5BtY3ki3pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دختری که پاشو میداد پسرها بخورن و فیلمش رو منتشر میکرد، بازداشت شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/150121" target="_blank">📅 00:08 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150120">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🔴
فوری/مارک لوین:
آماده باشید، سوپرایز در راهه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/alonews/150120" target="_blank">📅 00:00 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150119">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/elypAIm_xcVmFy7ZLbG0LbfJu6uMzC7_YzmthWm2R9EYrmXZBjnV_Ewsegdxz6MEDV6ZUtiVIWcycF_9ItVd4D5joH48GP0lYYj2NWLzpAipQrEptw25KTbUUec3dkeA1zTbB3s8PrCEXCNiZIFYweWp5wsO1xOwJDibcnW2dVar9cheEbM23IyCB8D5Bq7bhgBGWBqW6go0uN5qhB5B1QnJ_GN0KLKsV_0J9tAvHZq5RWUOAtZMswit7IFmBVNqIGe1kw6RAebmnfJA75G7mYS4PcC4cOoTEqh_JK82wd5tvpoxGEsleoNyN6j00E7j84cuymrVHR0Rz03dfs-okQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی خبرنگار نزدیک به حکومت: آیا غیرتِ «لابیِ امارات» در ایران، این‌بار به جوش می‌آید و می‌گذارند «اسرائیلِ کوچک» را در جنوب کشور، کمی تنبیه کنیم؟!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/150119" target="_blank">📅 23:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150118">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: ایرانی ها خیلی فقیر شده اند / ما ایران را از داشتن سلاح هسته ای منع کردیم / تنگه هرمز کاملا باز است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/alonews/150118" target="_blank">📅 23:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150117">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e6dab3e8.mp4?token=oUuRkT2OKmRq8YkYe8eNI2apYO-B-aaf0QykpZa_5gIzP-aSekoEVVXq6vPTN8yZeBJnrzyYAmjZivNsxdAy98I9G0FYNzYjM6BDBI56_PAkZczGlei91m0TuWtDH75wgEB2dqvcpvq-P0dwaexEQD_93GSktBDHfdGsuTtgtARM-H7lJHtfyZ5TdJlJz-ckYYzqKeN05d9SERZ-RxSrooVXGwomUjBUm6_IZugrCEBSR5sW5S4SUF9pUajXDyQwmonBlzeUggCOjwnL2DViQnXz3KnZJNvHMAmn7I3rEsIhd9OoX7Iz4y_-czq-M6L0LLVV07GXTXmfIvFzYLml8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e6dab3e8.mp4?token=oUuRkT2OKmRq8YkYe8eNI2apYO-B-aaf0QykpZa_5gIzP-aSekoEVVXq6vPTN8yZeBJnrzyYAmjZivNsxdAy98I9G0FYNzYjM6BDBI56_PAkZczGlei91m0TuWtDH75wgEB2dqvcpvq-P0dwaexEQD_93GSktBDHfdGsuTtgtARM-H7lJHtfyZ5TdJlJz-ckYYzqKeN05d9SERZ-RxSrooVXGwomUjBUm6_IZugrCEBSR5sW5S4SUF9pUajXDyQwmonBlzeUggCOjwnL2DViQnXz3KnZJNvHMAmn7I3rEsIhd9OoX7Iz4y_-czq-M6L0LLVV07GXTXmfIvFzYLml8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد هوش مصنوعی
:
این باور وجود دارد که باید میزان قابل توجهی از خودکنترایی در این زمینه وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/150117" target="_blank">📅 23:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150116">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ae5795165.mp4?token=lJqmFih0wAnNPonyfQRvrlXXiIIBv7NjZpIZBkHpf5xDvznuD9XrJZNVzYqn-2HiGzxpTTJw0HF2pIu2GKKvlFxe6XEyB-oxJGSawj-FhEq2lrxMml1rfahCHLff1ZTEqMgD3FBahX4RycDx63U2hUjDzXuuL7gfEE-ZLfNqVa5_JoYl0543Kub74x8Oxrnl--rgKZ4gU-gPsMhIBpQdEyDmr-7oL7lZt0TR3ecxc7nEwKMmUGVj_bHIfRge91XeefoPW02zcGWtrfJ3dEufxjPSoUgtEE0MshCAMWGXRqfiJZ0sIIYzIYWaQMJYjGEdt1cNoWaizmGHlH-hwDEaOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ae5795165.mp4?token=lJqmFih0wAnNPonyfQRvrlXXiIIBv7NjZpIZBkHpf5xDvznuD9XrJZNVzYqn-2HiGzxpTTJw0HF2pIu2GKKvlFxe6XEyB-oxJGSawj-FhEq2lrxMml1rfahCHLff1ZTEqMgD3FBahX4RycDx63U2hUjDzXuuL7gfEE-ZLfNqVa5_JoYl0543Kub74x8Oxrnl--rgKZ4gU-gPsMhIBpQdEyDmr-7oL7lZt0TR3ecxc7nEwKMmUGVj_bHIfRge91XeefoPW02zcGWtrfJ3dEufxjPSoUgtEE0MshCAMWGXRqfiJZ0sIIYzIYWaQMJYjGEdt1cNoWaizmGHlH-hwDEaOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سوال خبرنگار: شما گفتید ایران نمی‌تواند سلاح هسته‌ای داشته باشد. چرا کره شمالی می‌تواند سلاح هسته‌ای داشته باشد.
🔴
ترامپ: چون تو یک رئیس‌جمهور متفاوت داری. کیم جونگ اون. او دوست من است. او ترامپ را دوست دارد. من او را دوست دارم. تا زمانی که من هستم، او خوب خواهد بود. می‌دانی چرا؟ چون به من احترام می‌گذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150116" target="_blank">📅 23:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150115">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: طی دو روز گذشته مقادیری نفت از تنگه هرمز خارج کردیم که از میزان پیش از جنگ بیشتر است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/alonews/150115" target="_blank">📅 23:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150114">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d28b81ca12.mp4?token=lkYQVMVZL9jyqcyf6hvKUYJvwFYqZC-OgIpDFk3WnnxLiF4rCNoepFOJnHMjmK-XwR7qS-YSZ1VcEXd1-Myn4gkFcuxKMBKLJ3fxzswKBgL_tZw9yOnzgtzD-c-On53UAb0tpGM4cVkb4w7RRAVJA4uUlFMQMgy07W4e2dhSSfvP4h9fWOelxqSJm0imsUStU5jbfXPEPv5TbyWEI3GU8C6BlHiDnG9LyDbDkGEV-RXnMujFhPG41xFgKaaIa0rUkTtz34gxYu5mfT30NugaEZAofd8En3wzCAhdhJn4cX5F9xF2TeZIbPRGmzftGkEnqrzMPrheTXwd0phPfHbMmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d28b81ca12.mp4?token=lkYQVMVZL9jyqcyf6hvKUYJvwFYqZC-OgIpDFk3WnnxLiF4rCNoepFOJnHMjmK-XwR7qS-YSZ1VcEXd1-Myn4gkFcuxKMBKLJ3fxzswKBgL_tZw9yOnzgtzD-c-On53UAb0tpGM4cVkb4w7RRAVJA4uUlFMQMgy07W4e2dhSSfvP4h9fWOelxqSJm0imsUStU5jbfXPEPv5TbyWEI3GU8C6BlHiDnG9LyDbDkGEV-RXnMujFhPG41xFgKaaIa0rUkTtz34gxYu5mfT30NugaEZAofd8En3wzCAhdhJn4cX5F9xF2TeZIbPRGmzftGkEnqrzMPrheTXwd0phPfHbMmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: بیل گیتس می‌گوید هوش مصنوعی می‌تواند یک میلیارد انسان را بکشد؟
🔴
ترامپ: الان دیگر چنین چیزی نمی‌گوید.
🔴
خبرنگار: او یکشنبه این را گفت
🔴
ترامپ: خوب، برای من مهم نیست یکشنبه چه گفت. دیروز اصلاً چنین چیزی نگفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/150114" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150113">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ba82f7739.mp4?token=WQ1IxREERN1IKNUMZvGI2GytbDM7qEbJSk0v8YtLbX2aEi9QWuRxemYBShp_bG8de3p51YywGNFYQZlGi8XNOHqgC0dcMtz08e_2aydjbK-W6t_KqqH-o7ZnnggHRrsRdXH7OD2AjzN2k2DqOzqIH0g8k-ZX-4q9-8EJzb_4CupdI5oIQMK3A66Gcy_0b6eVXBHguJRt3EaxkQmzOf5RkrHuV4nEuix3snz1dx-wnNkMS-v_49CbG80MQGJyNWIE99av_K4D5VsY2TjUFJlvldljbz5j9KeTEHE-Brx3wqdIuQSjF2SmYNztE4RyH-p9nvUQIlsk1cYZc_uUCFTB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ba82f7739.mp4?token=WQ1IxREERN1IKNUMZvGI2GytbDM7qEbJSk0v8YtLbX2aEi9QWuRxemYBShp_bG8de3p51YywGNFYQZlGi8XNOHqgC0dcMtz08e_2aydjbK-W6t_KqqH-o7ZnnggHRrsRdXH7OD2AjzN2k2DqOzqIH0g8k-ZX-4q9-8EJzb_4CupdI5oIQMK3A66Gcy_0b6eVXBHguJRt3EaxkQmzOf5RkrHuV4nEuix3snz1dx-wnNkMS-v_49CbG80MQGJyNWIE99av_K4D5VsY2TjUFJlvldljbz5j9KeTEHE-Brx3wqdIuQSjF2SmYNztE4RyH-p9nvUQIlsk1cYZc_uUCFTB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: وقتی عامل‌های هوش مصنوعی مرتکب جرم می‌شوند، چه کسی باید مسئول شناخته شود؟
🔴
ترامپ: اسمش AI نیست، SI است
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/150113" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150112">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: ایران وضعیت بسیار نامناسبی دارد، نمی‌دانم که آیا آن‌ها هنوز قصد تسلیم شدن را دارند یا خیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/150112" target="_blank">📅 23:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150111">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PPP3cWl5eO7eEbX_DGS9BJIAPKIJuOE_4hNnt6Xq8u2umWWuIYe0owFZaeMjOl-X4Pyi9_kVFMgOUaNEjXdipUxjwJRXHC5YOvS-SEs4jrHg9WecLZA5_jZOeqYYkMGzZsWDnVVpwkgQ4u6azKnIA2zsghqDXbFa34xnewPo3OJBPDmkXJLOcEikmHxZZpF2Q9QoAxP-7GbfSsgdWbJzyXxhhZD-6NPWGwIxHV-m1jeLAYKnJpYzmXdfAzo2ndtV2KEo6XkhP72kZXdRrq7mweMjqlmNZHQAiUYbIJZvLi7kiQVOTPZ-k_UnPFfS3A1yQgvPPAMRH5kJszECnVXLCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارما یعنی این
‼️
🔴
طبق معمول چند سال قبل بسیجی‌ها گنده گوزی و ک... نمک بازی میکردن که زمستان سخت اروپا نزدیکه و بیایید چوب کمک کنید
🔴
حالا قراره گاز کشور تو زمستان قطع بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/alonews/150111" target="_blank">📅 23:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150110">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
منابع عربی از شنیده‌شدن صدای انفجار در اربیل عراق خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/150110" target="_blank">📅 23:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150109">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b186b209ea.mp4?token=P7LLgCxXfpqTwy-TKOOrf3ysZhq4sROPN5X1ajWLsMgC9_QA1ZQIqkid4UeAR3t_ns6Auh1Qg9Lpxq4T541RhYXv8eKeUh2DpBtI-dN6Rzq7OYfYpPiYrbguyPIxeeyCCteM1mkt6W_oy48udRsDjtsFtEhf97kCiBMg-VdZym14uIoaQzeXxzdSeVmc7FYzQZnuEZBlP7XnF3r4l1eQbd2ed5-EL-IsR6zf2Bv2YnbBCHF8ugyWRB6L6DSs8DIN5FL0J_o440KbqssaCiCRSqm9Ygzp777q8wMADTXYVo4-x79TnpY6SdDY-kGzPw3eZWGZmDkbhONAnZIMt9nNcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b186b209ea.mp4?token=P7LLgCxXfpqTwy-TKOOrf3ysZhq4sROPN5X1ajWLsMgC9_QA1ZQIqkid4UeAR3t_ns6Auh1Qg9Lpxq4T541RhYXv8eKeUh2DpBtI-dN6Rzq7OYfYpPiYrbguyPIxeeyCCteM1mkt6W_oy48udRsDjtsFtEhf97kCiBMg-VdZym14uIoaQzeXxzdSeVmc7FYzQZnuEZBlP7XnF3r4l1eQbd2ed5-EL-IsR6zf2Bv2YnbBCHF8ugyWRB6L6DSs8DIN5FL0J_o440KbqssaCiCRSqm9Ygzp777q8wMADTXYVo4-x79TnpY6SdDY-kGzPw3eZWGZmDkbhONAnZIMt9nNcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شبکه ای 24 نیوز: «آمریکایی ها با ارزیابی نتانیاهو مبنی بر وجود نشانه‌هایی از یک حمله احتمالی علیه اسرائیل پیش از انتخابات پیش رو، هم‌نظر هستند، این ارزیابی به تهدیدات احتمالی از سوی ایران و نیابتی هایش در منطقه‌ اشاره دارد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/150109" target="_blank">📅 23:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150108">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IG-jWdclv4HLXvME-Fn5P7GOrvhiEwaBkoIVxhHSXGlZo6TyeObOVycTxj8B6ZRqINBUkI4Wz7XCSMqoqGiFnLhN06YailoC4zvhJ3hE6dPGyninMAriKM3RiYp3aR5-iHpntszQa_stOrzHIBvfJPRQkHZOSOJrjM2Xh0lTQSald33O7CCixXlgR42b_a25EEqFBjLUSa2G1_4x4En6BaAW2JgvPjb4fZOM5lS2VMXlSsMWfpZrUn83GWAtbMfohkB9mX4tcLB2a1EJYvlN4qSqS83wt-iIq3cVa6Zjm5S3Mc3qk0M_aPDMYm98K8AADYEj05QsM3FHMDmpY5bdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هر دینار کویت از ۸۲۰ هزارتومن رد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/150108" target="_blank">📅 23:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150107">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رسانه‌های اسرائیلی گفتن تو سفر دو روز پیش نتانیاهو به امارات نماینده‌های ۱۰کشور عربی هم حاضر بودن و در مورد ایران حرف‌های مفصلی زده شده   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150107" target="_blank">📅 22:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150106">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
بلومبرگ: آمریکا عرضه حداکثر ۴۰ میلیون بشکه نفت خام از ذخایر راهبردی نفت خود را اعلام کرده
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/150106" target="_blank">📅 22:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150105">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
امیرحسین ثابتی: حق اقای رسایی که واقعیات رو گفته زندان نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150105" target="_blank">📅 22:47 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150104">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqmpwqBUjbbleIjHiSVE-2wDLvm5lkXwFKv4FajXHpCDiZvT7nDkqMIWwtqkY3ackdYpyt-lYKqeHoNwfeQYEaeyW90oiQUOSYt89-hqIaV2YooNDPhy_uR4Lf-Y0ZYcZ6dcIv9_GnhQep7toDe8pLWQMfUnUcDdChAhgJPv0rEyDsmeWexUgIl45yBtyerAGPtFBPXyAuE8Xa8vauY2efXj1euCH6GOP520XueuE6ThRKuGxdfbccYBwfab8Lrzpye2Rqi2rYTZdQoJNSrZO6wYOaCHY9VNfyNjv0uOvu9KFOHqSXsR1FcX-23imB5utXlLtG8m8lv7qWU3blyafA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نفت تگزاس به ۸۹ و نفت برنت به ۱۰۲ دلار رسیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/150104" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150103">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
فایننشال تایمز: میانجی‌ها به‌دنبال توافق موقت میان ایران و آمریکا
هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150103" target="_blank">📅 22:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150102">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09ba0150e.mp4?token=HXqbv1mhC5BEIZmHJFNcSiqF6jvuZ-qj52mAQUpBN-9I76n6YGA1kGbWgUAf_mcdoRIbbghgkD15VGvU6h_jH_IYYU1yBy4fLwpYimcFGg7HuRAFDZHx4qGb9CI-dLzHKNQtvh_4CdI7i9HnhF_-fMgfDkLSIpvTIHNb8BTHhwzUznpfkSmKRBkwO7diEqNi8dDPyjKGGGt1PvJH9ko4zzAmPVeuQ2BWqFIpdk9FsvaMjqYQ-cZDhjkGwp2iuTH7HHLhdXCsuLgck_x1i5mMiaP_30Gdk_7X-V7iS7_2QytspYdEzifMGvP0auw1R_vD3KBbEwLhdD18T8Rs7nPd9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09ba0150e.mp4?token=HXqbv1mhC5BEIZmHJFNcSiqF6jvuZ-qj52mAQUpBN-9I76n6YGA1kGbWgUAf_mcdoRIbbghgkD15VGvU6h_jH_IYYU1yBy4fLwpYimcFGg7HuRAFDZHx4qGb9CI-dLzHKNQtvh_4CdI7i9HnhF_-fMgfDkLSIpvTIHNb8BTHhwzUznpfkSmKRBkwO7diEqNi8dDPyjKGGGt1PvJH9ko4zzAmPVeuQ2BWqFIpdk9FsvaMjqYQ-cZDhjkGwp2iuTH7HHLhdXCsuLgck_x1i5mMiaP_30Gdk_7X-V7iS7_2QytspYdEzifMGvP0auw1R_vD3KBbEwLhdD18T8Rs7nPd9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
اعتقادی وجود دارد که باید میزان قابل توجهی از خودکنترایی در این زمینه وجود داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150102" target="_blank">📅 22:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150101">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf413cd42.mp4?token=hLZM1DkhUlHYLqdCvRmu9c1XQJHcCJkbeMHQL47QgVe-UKnSmiRo3zdeDSrWYqL4WZsSG4X1_xhGGcLBdEtz1_rL0IM2fTaYk2qYqtb1gSE6bTJeF6BIfvQMOxb2FGvhicPoimCZvw-HVc86_mb6okb6ixR3G4JyCNOqshOkOlIi6yp6KQFHk-VUJbkjcofW5J1BTc7ajkrjuyNZD3EKJJSHs5XMAvjpn5gx1rj-LTYqGX5qXSEaNw52QOF67Ks1wjtpA6A1bSkFExDW3hPC4V-4bv4GHT0xYrsIyHY703picO7G0coN-C4w-jyI6y8MokfpBJI-1AEJweNovi8zFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf413cd42.mp4?token=hLZM1DkhUlHYLqdCvRmu9c1XQJHcCJkbeMHQL47QgVe-UKnSmiRo3zdeDSrWYqL4WZsSG4X1_xhGGcLBdEtz1_rL0IM2fTaYk2qYqtb1gSE6bTJeF6BIfvQMOxb2FGvhicPoimCZvw-HVc86_mb6okb6ixR3G4JyCNOqshOkOlIi6yp6KQFHk-VUJbkjcofW5J1BTc7ajkrjuyNZD3EKJJSHs5XMAvjpn5gx1rj-LTYqGX5qXSEaNw52QOF67Ks1wjtpA6A1bSkFExDW3hPC4V-4bv4GHT0xYrsIyHY703picO7G0coN-C4w-jyI6y8MokfpBJI-1AEJweNovi8zFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : شما خواهید دید که مراکز داده (data centers) بسیار محبوب خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/150101" target="_blank">📅 22:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150100">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b122f6a38c.mp4?token=cYwW7Weto0H4LJDb5ioKZ7-56Fwrr1YU4V_N4yDB4RZZyBaol9_s217_D6uxMsxZ4E58_8rOAbicr7ZQ-vv9NsgfgtCFoB1xoCp54bJ1OdTj0WapstJ4PdfJOJpVHFjVOGrQo4taNTi5qMrYxmCZyjFWPjewbpfXtZSFGiVW-GQuECPnZXjvi-5L8nUwVjvuIO0IupYV4-FLOU4gmS5z9UV4ak5BQzLhapSbccCCK8lJE5kKYKm-_64tS4gzR4Yi9NidQkSI9rXco2FECDsxMvpBH-nzkA3ZtwemAvPV5vpHrAzZRdfwgmPYuE5UIHPaB9r4AgnF4WO3RdN-wvLppw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b122f6a38c.mp4?token=cYwW7Weto0H4LJDb5ioKZ7-56Fwrr1YU4V_N4yDB4RZZyBaol9_s217_D6uxMsxZ4E58_8rOAbicr7ZQ-vv9NsgfgtCFoB1xoCp54bJ1OdTj0WapstJ4PdfJOJpVHFjVOGrQo4taNTi5qMrYxmCZyjFWPjewbpfXtZSFGiVW-GQuECPnZXjvi-5L8nUwVjvuIO0IupYV4-FLOU4gmS5z9UV4ak5BQzLhapSbccCCK8lJE5kKYKm-_64tS4gzR4Yi9NidQkSI9rXco2FECDsxMvpBH-nzkA3ZtwemAvPV5vpHrAzZRdfwgmPYuE5UIHPaB9r4AgnF4WO3RdN-wvLppw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
امروز، ما یک سند را به طور رسمی امضا خواهیم کرد که طی آن، نام "هوش مصنوعی" را به "هوش فوق‌العاده" تغییر خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/150100" target="_blank">📅 22:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150099">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/086c0eef0d.mp4?token=N0N9Y2vfdf6mpZ_GZfLc6VuYHHkAhCRsg54mX7XjeThRnmWmhqhTJ6yP7nHXaWcGktwA9P31-nHKOXy3rAV76PWZnfFK47MBdBldN-b3PUKsreisXAwL5mb_RloRI4goAV8nvYxT-0m1Vqav2ONiSl_YAadMaS4yydUvU8jAx_EaA-Rn2oMXHbh_8y-OIohGbUz253_3y5pyRg4Zag0vhyZryV59jQ8mIu-8QCPz-EYw9EVz2jcDwdeU847829Ua7InKk2ynw47cvFzh6P8N6GWUxatuZzgZK2Q7Txy4unyCqs3VS4l1veZ_p1cJbHtcSfSr6ixxA3XAHFEazUDWzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/086c0eef0d.mp4?token=N0N9Y2vfdf6mpZ_GZfLc6VuYHHkAhCRsg54mX7XjeThRnmWmhqhTJ6yP7nHXaWcGktwA9P31-nHKOXy3rAV76PWZnfFK47MBdBldN-b3PUKsreisXAwL5mb_RloRI4goAV8nvYxT-0m1Vqav2ONiSl_YAadMaS4yydUvU8jAx_EaA-Rn2oMXHbh_8y-OIohGbUz253_3y5pyRg4Zag0vhyZryV59jQ8mIu-8QCPz-EYw9EVz2jcDwdeU847829Ua7InKk2ynw47cvFzh6P8N6GWUxatuZzgZK2Q7Txy4unyCqs3VS4l1veZ_p1cJbHtcSfSr6ixxA3XAHFEazUDWzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره هوش مصنوعی:
ما در این زمینه پیشرفت بسیار زیادی داشته‌ایم و قصد داریم این برتری را حفظ کنیم، و این یک موضوع بسیار مثبت است. این یک صنعت فوق‌العاده است.
🔴
برخی معتقدند که این صنعت از انقلاب صنعتی بزرگتر است. من نمی‌دانم که این درست است یا نه، اما به نظر می‌رسد که همه اینطور فکر می‌کنند، و ممکن است حتی بسیار بزرگتر باشد.
🔴
ما در حال حاضر پیشرو هستیم و قصد داریم این وضعیت را حفظ کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/150099" target="_blank">📅 22:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150098">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
دقایقی پیش وزارت خارجه دانمارک از تمام شهروندانش خواست از سفر به ایران خودداری کنند و از دانمارکی‌های حاضر در ایران خواست فوراً ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/150098" target="_blank">📅 22:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150097">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjVccyBZ3gC-z0CB7tYmIAFcP-R1VMWOV-BIHXXLcOUEzXF-FJrlGkP0wHdWIV1sMbNE1gDRV7rk4oV7CVJBIrbWy9UyhyVvznfR319eWmtCHSccSbHjby1VNpXcdThSe8IcUS57twdbGIF9l7WqBE7DX9K-1c8aL6NolqYXzliIWyjR7vyUHaGQEXtDUQItymARFSraFqNnflpRM0NAeje4U49c8ENm0zPCXKyVuP68LU9ZOClXL5lo5S05WcAfej2MAAoWrIbLV_-2xiekeyS9_3PPp_jQaBRABewICqTLCJVyZ4Q51YEXmg3vMuyCQ5LWRNbB5Ey-DSJeEv1YyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی بعد باخت به روسیه:حاضرم تمام افتخاراتم رو بدم اما ۱دقیقه جای ملت مبعوث شده تو خیابون باشم
🔴
بازی به بازی ایشالا بهتر میشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150097" target="_blank">📅 22:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150096">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XAIWUtsdRy1qZVnRFTZuJXd_9yKtKrf2L_6yTp2uPyZhHn_8seFefLdrt2WMcCP0yB9cBuRdkKReRx8n633X11UQ6gWs-gMrOVMaI4nBsYt48zKAd2GP3eTJGG7mQ5B8ZAO0xmK3N16dVv0qzxBo8ujtNuIN12n8XK3pUIqjmL-0mJXzVMqmLOE9svy-oRMl25u_R8bR4fALkP1pl6mOnDf6J6j-9OrBeIZrzhyR0n1yeiS9xYwH4tufBYmHvVu8olBnrYSqu17Pasy4OtiDMTrBEhHcfv3JpUhg0iiqbC9sp-QNJ-aXKpSmP-WCV2DWb0Bhdy9TfLNsbnH0-_dxLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نجمه جمشیدی ؛ روزنامه نگار: امسال سخت ترین زمستان رو تجربه میکنیم.
🔴
گاز بسیاری از شهرا قطع میشه. به دلیل مازوت سوزی کل کشور شبیه اتاق گاز میشه و ریه ها رو داغون میکنه. خدا به داد مردم برسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/150096" target="_blank">📅 21:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150095">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b253481a4.mp4?token=dwe4SeBDyZ0buJXRPyHYfxc0po0JaUHq1C4zWGhhnzQiIdnsij1Yn-q8ouP3xCjMWUXL9MiGB8IHm0h7KSWPzykVa5JgcwxJH1HAx1EWa8GS8Cnoe5P985QmiW9ifGIGwp-pWLz13U3L6vBeeuYe0KqpE62BinZFrhrjkTdCwO1DYBP4R7N01d3eWuO8hKNAhKCHUJrgUxaP76_3rDSdCftjjFDTf9ztYMCBaac--_PUjCzvvz8ORUjUY75-Sm1FLvzB3F2nMGr-a-21Ar3UNnNMphFipb3iY-YRdMb8WPdmUVsVSNvQglAIkZEHyf791J16hPeBI3W5XnDsKlLm3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b253481a4.mp4?token=dwe4SeBDyZ0buJXRPyHYfxc0po0JaUHq1C4zWGhhnzQiIdnsij1Yn-q8ouP3xCjMWUXL9MiGB8IHm0h7KSWPzykVa5JgcwxJH1HAx1EWa8GS8Cnoe5P985QmiW9ifGIGwp-pWLz13U3L6vBeeuYe0KqpE62BinZFrhrjkTdCwO1DYBP4R7N01d3eWuO8hKNAhKCHUJrgUxaP76_3rDSdCftjjFDTf9ztYMCBaac--_PUjCzvvz8ORUjUY75-Sm1FLvzB3F2nMGr-a-21Ar3UNnNMphFipb3iY-YRdMb8WPdmUVsVSNvQglAIkZEHyf791J16hPeBI3W5XnDsKlLm3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پی‌رز مورگان: آیا برای شما و همه افرادی که در تلاش برای رسیدن به توافقی بین ایالات متحده و ایران هستند، آسان‌تر خواهد بود اگر رئیس‌جمهور ترامپ در شبکه‌های اجتماعی کمتر فعال باشد؟
🔴
نخست‌وزیر قطر: برای ما بسیار آسان‌تر خواهد بود اگر تا زمانی که به یک راه حل برسیم، هیچ خبری در رسانه‌ها درباره این موضوع منتشر نشود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/150095" target="_blank">📅 21:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150094">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43a5034505.mp4?token=vFnaygWfPwgWdKT7qA1ffTElg46cYi0PWJF3evhzVoQwWISrY3SFlno8hiOoE_vfupK5uUt8tc-hziaDCVuhyurUteAvbtt_Z6Vh6TAUYWapqPuwIGMjDdXJa-wAGFHoTlp6upu8gTPGu7pC2wDMsT-f2Q279p150g5SkMvL2SOBftxwdQFPKRJQFiTYtKiJv145bleeH3R4qntwdni-WuMH3DXUtY0bOYrOKHsCZKgW-oXmGfiRbg1dRROGBWZMK_euMJBzOQGHLasFG2Ws5kDYuGy6yi2p1aJ45X2Dn0Rsibb97A_b5Zl9Hz-ptL8etNZBU2axi3oXEDUHZkhCFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43a5034505.mp4?token=vFnaygWfPwgWdKT7qA1ffTElg46cYi0PWJF3evhzVoQwWISrY3SFlno8hiOoE_vfupK5uUt8tc-hziaDCVuhyurUteAvbtt_Z6Vh6TAUYWapqPuwIGMjDdXJa-wAGFHoTlp6upu8gTPGu7pC2wDMsT-f2Q279p150g5SkMvL2SOBftxwdQFPKRJQFiTYtKiJv145bleeH3R4qntwdni-WuMH3DXUtY0bOYrOKHsCZKgW-oXmGfiRbg1dRROGBWZMK_euMJBzOQGHLasFG2Ws5kDYuGy6yi2p1aJ45X2Dn0Rsibb97A_b5Zl9Hz-ptL8etNZBU2axi3oXEDUHZkhCFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست‌وزیر قطر: اکنون، صحبت در مورد این که [ما] از اخوان‌المسلمین یا جنبش‌های داخلی آمریکا حمایت مالی می‌کنیم، کاملاً نادرست است.
🔴
چرا باید بیاییم و از گروه‌های داخل ایالات متحده حمایت مالی کنیم؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/150094" target="_blank">📅 21:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150093">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پزشکیان: اگر گروهی فکر کنند که تنها آنها عقل کل و تصمیم گیرنده هستند، ناخواسته باعث تضعیف کشور خواهند شد
🔴
[در خصوص لغو پروازها] ترامپ از آن سوی دنیا تهدید می‌کند و دستور می‌دهد و برخی از کشورها هم به دستور او گوش می‌دهند؛ همه کشورها به فکر منافع خود هستند
🔴
عراق، افغانستان، پاکستان، آذربایجان و دیگر کشورهای دوست و همسایه با ما کمک می‌کنند اما محاسبات خود را هم دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/150093" target="_blank">📅 21:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150092">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d4148e692.mp4?token=voQYa-EQfu75IXwP-FnxTDM3xRkvAMcPnCJR_N4YhPdQ7x68t9dCb1A22slgd2KtmnrDb8s_VdCkfU50P45NYhNVku7LAl4DFPrwc5pmRggqC3IBvIGVLunH1E1Sk53xCHAqQMkso5vGi_ZOddflimrSmR4HCg0fK7eAWYaY0tMGJsjbeLj4fsv7HP2ujTlQrtnwYzxoJV6HeAHs6J12ScbPYQWtvTSErmeBWTA53F5lrees8pEWRZ4MGPeq4m0aelomPD6GKSn4YecLUE633MjRieIB8hO5xzOQyME0DBr6ChCgeqiRR2EfvXTKehp_kuxikpZKhgD2EXdZpxzDtgrNO3aDRnSGifIgUIn4ZiYPYKlytzsstmU_HYfQSUvt85AXSsuuTiDUU_WtGiSa4O808YV3UFWRjCjcUmYDWHc1ndUOnF-jXh-qm_nZYHxmd5pCYlVXU13Xp1UkYcgSG5bCJxo8cSFB_Qow4s9iQH1MzV8n1hTT0By7cxQ8ppGGDGKoYFzVLeKlEtZb7Ee38Mon9aLa-1tkImv_xXzjXGrBgZwniyo3MhZnMAwxbvx8rvu9Rx34lrmvDtb9Im5A1AygT_kmWlRwXr4lU_NrREmiXWlHrxw4AfRApIWlj7MQ12ejCZlfwnat5_It_9MpkcILDRCnRi8_0zcH4ry1BVo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d4148e692.mp4?token=voQYa-EQfu75IXwP-FnxTDM3xRkvAMcPnCJR_N4YhPdQ7x68t9dCb1A22slgd2KtmnrDb8s_VdCkfU50P45NYhNVku7LAl4DFPrwc5pmRggqC3IBvIGVLunH1E1Sk53xCHAqQMkso5vGi_ZOddflimrSmR4HCg0fK7eAWYaY0tMGJsjbeLj4fsv7HP2ujTlQrtnwYzxoJV6HeAHs6J12ScbPYQWtvTSErmeBWTA53F5lrees8pEWRZ4MGPeq4m0aelomPD6GKSn4YecLUE633MjRieIB8hO5xzOQyME0DBr6ChCgeqiRR2EfvXTKehp_kuxikpZKhgD2EXdZpxzDtgrNO3aDRnSGifIgUIn4ZiYPYKlytzsstmU_HYfQSUvt85AXSsuuTiDUU_WtGiSa4O808YV3UFWRjCjcUmYDWHc1ndUOnF-jXh-qm_nZYHxmd5pCYlVXU13Xp1UkYcgSG5bCJxo8cSFB_Qow4s9iQH1MzV8n1hTT0By7cxQ8ppGGDGKoYFzVLeKlEtZb7Ee38Mon9aLa-1tkImv_xXzjXGrBgZwniyo3MhZnMAwxbvx8rvu9Rx34lrmvDtb9Im5A1AygT_kmWlRwXr4lU_NrREmiXWlHrxw4AfRApIWlj7MQ12ejCZlfwnat5_It_9MpkcILDRCnRi8_0zcH4ry1BVo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نخست وزیر قطر : ایران همسایه ما بوده و برای همیشه همسایه ما خواهد ماند. ما جایی نمی‌رویم. آن‌ها هم جایی نمی‌روند.
🔴
ما دهه‌ها رابطه بر پایه احترام متقابل با آن‌ها داشته‌ایم. همکاری‌ها به دلیل تحریم‌ها محدود بوده است، اما ما تمام تلاش خود را برای حفظ این رابطه همسایگی خوب به کار بستیم، هرچند در طول این دهه‌ها و در بسیاری از سیاست‌ها اختلافات زیادی داشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/150092" target="_blank">📅 21:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150091">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
#فوری | تحریم‌های جدید آمریکا علیه ایران  وزارت خزانه‌داری آمریکا روز سه‌شنبه از اعمال تحریم‌های جدید علیه ایران خبر داد.  طبق بیانیه وزارت خزانه‌داری، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری (اوفک)، ۱۰ فرد و نهاد جدید را به فهرست تحریم‌های آمریکا علیه…</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150091" target="_blank">📅 21:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150090">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دقایقی پیش وزارت خارجه دانمارک از تمام شهروندانش خواست از سفر به ایران خودداری کنند و از دانمارکی‌های حاضر در ایران خواست فوراً ایران را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/150090" target="_blank">📅 21:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150088">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ونس: ایرانی ها با شلیک به کشتی ها مرتکب اشتباه بزرگی شدند و توافق را نقص کردند
🔴
وقتی رویدادها را می‌بینید، با شواهد روشن و مشخصی روبه‌رو می‌شوید که فکر می‌کنم ایرانی‌ها متوجه شدند اشتباه بزرگی مرتکب شدند.
🔴
ما با آن‌ها توافق امضا کردیم و آتش‌بس داشتیم؛ قیمت انرژی نیز کاهش یافته بود و همیشه این امکان وجود داشت که اگر ایرانی‌ها رفتار مناسبی از خود نشان می‌دادند، از رابطه بهتر با ایالات متحده بهره زیادی ببرند.
🔴
اما آن‌ها رفتار مناسبی نداشتند و شروع به تیراندازی به سمت کشتی‌های تجاری کردند.
🔴
اکنون می‌دانیم که افراد زیادی در ساختار حکومت ایران وجود دارند که نمی‌خواستند چنین اتفاقی رخ دهد.
🔴
آن‌ها معتقد بودند بازگشت تندروها و آغاز دوباره حملات به کشتی‌ها اقدامی احمقانه است، اما این اتفاق افتاد و نتوانستند جلوی آن را بگیرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/alonews/150088" target="_blank">📅 21:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150087">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f617699456.mp4?token=SzGwlsq66LhPpn0zE2hgdLvypkgSTMhaG5LH3JmhAz7cfKJ_-a4GqVuaiSAyFiGCVt6cKefAAlzzRFOAj-TjwCddlyNlIiEwF0HNMGS6v_OrE7NjpgWJL_WUYuCXeGnULkREmyXztXOYdnHWRYScm_c2vT-vESXMe2vEwrhGmn5dckpQnJ5tsI3lglT1hVc5UOWDZ0dN9MMqOc4lzWA_delY-J4fHBsxMw2CcgY5K9jh0XlVM6zuv00oHZs_vhAG_RpRga778NYREk3NV9ziXtbF519LyDY9Frgae70zxgB5cL9NcCVkdDx4yDHnJw1BXt6-fT209A0rUM-IhZiKKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f617699456.mp4?token=SzGwlsq66LhPpn0zE2hgdLvypkgSTMhaG5LH3JmhAz7cfKJ_-a4GqVuaiSAyFiGCVt6cKefAAlzzRFOAj-TjwCddlyNlIiEwF0HNMGS6v_OrE7NjpgWJL_WUYuCXeGnULkREmyXztXOYdnHWRYScm_c2vT-vESXMe2vEwrhGmn5dckpQnJ5tsI3lglT1hVc5UOWDZ0dN9MMqOc4lzWA_delY-J4fHBsxMw2CcgY5K9jh0XlVM6zuv00oHZs_vhAG_RpRga778NYREk3NV9ziXtbF519LyDY9Frgae70zxgB5cL9NcCVkdDx4yDHnJw1BXt6-fT209A0rUM-IhZiKKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیو وایرال شده از حجم مورد نیاز زیاد پول نقد برای خرید آیفون ۱۷
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150087" target="_blank">📅 21:09 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150086">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAzizz Vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NK0IfMzjGuFBaZh8AYRbpE55M9P2hEtljfn71aIX1r1Cxr1wkQzi4hnm93p2a6kYxr6Jt5WFbSgVm66lPGsa6c_YlxmZM59DuOuTn8ZSHAnYpSwCg24Rv01ubxdExMGIo0_7-ikKSp7LiXj-T87xIYwMGZEzGeWA2l01KKrXA__Im1C8b7I12hRC86gEtEhxeJAwPKtRqPNYuFGViBs2MpbSjY3qjiETIGlzIkK0K4a3bIo2FoyE5mrC95p6hcktzn9NZOW6GXkRoSMsespYlwb9umqnFQizGS6As-S3Fr1tJFV_7fBpf5vwMzzAA-dWNiPRQA0mf6f3mShgSJXHmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
دارای IP ثابت
💥
سرعت بالا و اتصال پایدار
💥
اتصال پایدار حتی در جنگ
💬
تعرفه ها
🔸
سرویس نیمه عزیز
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود نیمه عزیز
▫️
تک کاربر — 180,000 تومان
▫️
دو کاربر — 230,000 تومان
🔸
سرویس عزیز
▫️
10 گیگ — 30,000 تومان
▫️
20 گیگ — 60,000 تومان
▫️
30 گیگ — 90,000 تومان
▫️
50 گیگ — 125,000 تومان
▫️
100 گیگ — 250,000 تومان
🔹
نامحدود عزیز
هفتگی:
▫️
تک کاربر — 129,000 تومان
▫️
دو کاربر — 149,000 تومان
▫️
سه کاربر — 169,000 تومان
ماهانه:
▫️
تک کاربر — 240,000 تومان
▫️
دو کاربر — 360,000 تومان
▫️
سه کاربر — 450,000 تومان
🔸
سرویس اختصاصی
▫️
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 275,000 تومان
▫️
100 گیگ — 500,000 تومان
▫️
200 گیگ — 800,000 تومان</div>
<div class="tg-footer">👁️ 70.8K · <a href="https://t.me/alonews/150086" target="_blank">📅 21:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150085">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: ما ۱۰ فرد و نهاد را که در تهیه سلاح و قطعات آنها برای وزارت دفاع ایران دست داشته‌اند، تحریم کرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/150085" target="_blank">📅 21:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150084">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
پزشکیان: از همین ماه رقم کالابرگ افزایش خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/150084" target="_blank">📅 20:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150083">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
آذربایجان استفاده از خاکش برای حمله به ایران را تکذیب کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/150083" target="_blank">📅 20:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150082">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4692677be6.mp4?token=Wc7rHd0NC_ytZfpqzNBNbZTEKxZE2lniqeKfM0iIIab8aprVaVwpbR-hJTJnVdJ4aHdFbgGBMBzz26CceFuGluy8mE9kRDwWI9kPcefBo8paYW_0EUM4fdnoe96lsahQCCF4v6qpEIuT0e7sRGb3eUkaq__QBUovtx1d-iCCi6Ja6Ot7qa7E9SYwS1cmUC9tKNgaYFAgLScDYq0YrnQip3AmKGvlwc4ABBKxG2_oBzttvfkAq2T7ADPsis-OyC_2yXydhEoqG27vsFmq0gCrtRgkY6fUx39JK25sFx-c_-AWXxUYui45fjRhgHUbzuttvwwKTdHtTTbtmaxf8KnFpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4692677be6.mp4?token=Wc7rHd0NC_ytZfpqzNBNbZTEKxZE2lniqeKfM0iIIab8aprVaVwpbR-hJTJnVdJ4aHdFbgGBMBzz26CceFuGluy8mE9kRDwWI9kPcefBo8paYW_0EUM4fdnoe96lsahQCCF4v6qpEIuT0e7sRGb3eUkaq__QBUovtx1d-iCCi6Ja6Ot7qa7E9SYwS1cmUC9tKNgaYFAgLScDYq0YrnQip3AmKGvlwc4ABBKxG2_oBzttvfkAq2T7ADPsis-OyC_2yXydhEoqG27vsFmq0gCrtRgkY6fUx39JK25sFx-c_-AWXxUYui45fjRhgHUbzuttvwwKTdHtTTbtmaxf8KnFpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی.دی. ونس: ما در این بحث پیروز شده‌ایم. تفکر "ویک" (Woke) مرده است. دموکرات‌ها به طور واقعی از موضع‌هایی که دو سال پیش برای کسب قدرت سیاسی اتخاذ کرده بودند، دوری می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/150082" target="_blank">📅 20:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150081">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سپاه:  درگیری ها شکلش تغییر کنه سلاح های جدید رو میکنیم برای دشمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.1K · <a href="https://t.me/alonews/150081" target="_blank">📅 20:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150080">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
فیلد مارشال محسن رضایی: شروط ایران به آمریکا اعلام شده، اما ترامپ قادر به تصمیم‌گیری نیست و آمریکا از سر استیصال در جنگ نظامی به محاصره هوایی روی آورده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/150080" target="_blank">📅 20:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150079">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzW3dIrEUsZeMk7n_ReZLiwzIy5lz17FF8CqKFUJ4WiOxiorLBfdjiHGuJG7T4gt6Snqi3YNAaGhcatJ-nqCdtb8acyqxxWaY53VJkD-XaCJE3gKPdgHcxCLuStMm98elBCaBITXDf9tPf3aqEZQmTEg9G47tJMHXCUCpAnJTQloU4y9F-URlD_gCIkfuewW5r1zc14XcnJOezGS3c1qFRtwhnMhKNbJ5Gw80VJWzcgVByEvbbNfTZuASeGh8y63BmaerhHXLtlTUTVxi6BvYOJDN-mHIfS4KVEKzq8KM_gbnhRwd2FhEKUciHAHbioXLcH3Hd0HnTKlbJLpOIZikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا طلای فیزیکی که میلی به مشتریاش میداد هم ناخالصی داشته
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/150079" target="_blank">📅 20:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150078">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44dc04051e.mp4?token=Pa9Saky4Gx18DNXqbPYEfzVEr5MCRpVx_6na2ssKBlPVNp5M1B62UQkV6LyGupcymBAvZteLRSC2g9RXNiSs0-ApOsBpAT5PGRoPOHY4lAXx0kvemjijBHHsMwIn7xpK_UygQDLbPCKN-BIFG-NUDxHYFI3alstNvvh9iksN3bC9Xjl3U1_wRPftYw89feuKYdUTYpyNmhq2muXNN4uiD4lf7_ba97R654lhiJ6a0SpJCnn_s-ohYwMw9j1RnMgEfmrvuEZ759_n_4vYNpAZcTdqa0n3oXrbmdx8nPY7snVFLC3VJCUA1gMpI6gd1Ku7ynZdQOq1oAm0v0nCC6Y4Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44dc04051e.mp4?token=Pa9Saky4Gx18DNXqbPYEfzVEr5MCRpVx_6na2ssKBlPVNp5M1B62UQkV6LyGupcymBAvZteLRSC2g9RXNiSs0-ApOsBpAT5PGRoPOHY4lAXx0kvemjijBHHsMwIn7xpK_UygQDLbPCKN-BIFG-NUDxHYFI3alstNvvh9iksN3bC9Xjl3U1_wRPftYw89feuKYdUTYpyNmhq2muXNN4uiD4lf7_ba97R654lhiJ6a0SpJCnn_s-ohYwMw9j1RnMgEfmrvuEZ759_n_4vYNpAZcTdqa0n3oXrbmdx8nPY7snVFLC3VJCUA1gMpI6gd1Ku7ynZdQOq1oAm0v0nCC6Y4Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی‌ ونس، معاون رئیس‌جمهور آمریکا درباره‌ مجتبی خامنه‌ای: ما فکر می‌کنیم او زنده است. البته نمی‌دانم. من هرگز او را ندیده‌ام. اما بهترین شواهدی که در اختیار داریم نشان می‌دهد که او زنده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/150078" target="_blank">📅 20:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150077">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
هم اکنون گزارش شلیک موشک به سمت تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.9K · <a href="https://t.me/alonews/150077" target="_blank">📅 20:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150076">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">آکسیوس گفته شکاف بین ایران و آمریکا اینقدر زیاده که واسه توافق معجزه لازمه!   @shahab_gold_trading</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150076" target="_blank">📅 20:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150075">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kCTwYjT7SDlECKgZtwlKjgaGrMqM9Ca45dz69-7FjJJekz0LTcyThFwBfQ17E7u3ztp2KP1q2mzWJ9xZvIVdd9srz6OrLlACgntfLuxKFJFq-Ed7Jq9SE-awGfsO-tVn0ZI-WLyuGmFksY4yHC9fLkX8Bk9-j2WgUH7kyNurFKNr9Bs70bqUyZ_GlIGm-AjOMQH059jeF2SDSg76WnJVGjrqHFe1-vgOWjrJ0Wmvr2W-rsagIF-8aMQ8PrSwyN-PgrYEST4uRg1qEd75rhM5_mj_y1vQ5Uy_M8bauKCSHWGC1RR3drycgXrlUsf5SgsFjwKFbTilI46lS3255VefBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گزارش اویل پرایس: با از سرگیری مذاکرات آمریکا و ایران و بهبود صادرات عربستان، نگرانی‌ها در مورد عرضه کاهش یافته است.
🔴
با از سرگیری جریان خط لوله شرق-غرب عربستان سعودی به حدود ۳.۵ میلیون بشکه در روز پس از توقف ۱۰ روزه، قیمت نفت برنت به سمت ۱۰۴ دلار حرکت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/150075" target="_blank">📅 20:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150074">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
مدیر میلی‌گلد: فرار نکردیم، برای امنیت دورکار شدیم و بزودی کارمون رو شروع میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/150074" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150073">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
هم اکنون نتانیاهو اعضای شورای امنیت ملی اسرائیل را برای یک جلسه امنیتی اضطراری درباره ایران فراخوانده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/150073" target="_blank">📅 19:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150072">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
دقایقی پیش صدای انفجار در جزیره قشم به گوش رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/150072" target="_blank">📅 19:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150071">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DnZXocuGKMua_C5NLB3ZAWuBUynbeFcBDorrgXa3TYN5WamcotPxPq88QET_Oxdq_kXGTPSgfDD4cp3zrJmqbmqEjy3BxQRTT_duwMfoPR9k-y6C05IQ5zAtovgSNTueAFjUqDuJjiv_wvqSay6O8WrgDZrUOc0cbPg3Fa1OC0UwrD4xfYmvp6aJ8YuNgHWZJ5-YQbYsT7_yooFV4FcbnnWZ1yvTqWSol7ERDZtYISndUlvmDwJd0JCQn_OoWw3Gbz7T-Wh7q234vOKkW58JhJFXEssh9C4bs8LjGbB4G1uauCahIHyvIE-cVrWk6cH8C9n2sHP1KlVzxW2DRj-Ppw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آکسیوس: سناتور اریک شمیت از میزوری، جمهوری‌خواه دوره اول، که پیش‌تر دادستان کل ایالت بود و اکنون نایب رئیس کمیته مشترک اقتصادی است، به نایب رئیس‌جمهور جی‌دی ونس نزدیک شده و به عنوان هم‌لیست احتمالی او برای انتخابات ۲۰۲۸ شناخته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/150071" target="_blank">📅 19:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150070">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ترامپ: فکر می‌کنم یک اسم جدید پیدا کرده‌ام. دیگر عبارت «اخبار جعلی» را فراموش کنید؛ از این به بعد می‌خواهم آنها را «اخبار مصنوعی» بنامم. این اسم را دوست دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/150070" target="_blank">📅 19:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150069">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بابک زنجانی: ایران دست بالاتر رو داره نسبت به آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/alonews/150069" target="_blank">📅 19:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150068">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f9212c852.mp4?token=Kd8lvL2xyt5rIozzcTt8oTyHhVLoRZRaaGOZb1Sn-GgNULN8ckns_GJtoAfMhpOLuua8h02-LW29buIr3OBKfG4oHZB-e2OIIPenA02WIhlZXjy3vZaXeufphEdomitO98g0o4d2ZHQR37ILh8s36_vIdrmVjKgMV90_ApPj551B6hd17S27zFhDnH_3747PDffbEB8RaULj80ZqTRDDCkfOhsAQ6UgOj84PqGZZAEX0_66-7adcNR9BTBMHZR5z_gOD7JBS79PfnopSMwaYSal9vT2oIKn9-9DCEOeAaXap5wPFW9qY-qxGIKaeRnkrYu8PlkmsP4Dgn0e0heg91Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f9212c852.mp4?token=Kd8lvL2xyt5rIozzcTt8oTyHhVLoRZRaaGOZb1Sn-GgNULN8ckns_GJtoAfMhpOLuua8h02-LW29buIr3OBKfG4oHZB-e2OIIPenA02WIhlZXjy3vZaXeufphEdomitO98g0o4d2ZHQR37ILh8s36_vIdrmVjKgMV90_ApPj551B6hd17S27zFhDnH_3747PDffbEB8RaULj80ZqTRDDCkfOhsAQ6UgOj84PqGZZAEX0_66-7adcNR9BTBMHZR5z_gOD7JBS79PfnopSMwaYSal9vT2oIKn9-9DCEOeAaXap5wPFW9qY-qxGIKaeRnkrYu8PlkmsP4Dgn0e0heg91Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس درباره ایران:جهانی وجود دارد که در آن می‌توانیم با تهران توافق کنیم. اما این امر نیازمند آن است که مقامات ایران رفتار مناسبی داشته باشند.
🔴
این امر نیازمند آن است که مقامات ایران به تعهدات خود در قبال ایالات متحده پایبند باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/150068" target="_blank">📅 19:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150065">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/029d7d5229.mp4?token=CTtErQ-dEnR7aoKOf9nHwhzEEGCVEJ5GbnFEf4ymKEtJxusFL-nPgeruUx2az_M-gdaYTSHI6J3YfPBvwKmXqqG8bNWKAG_dDyS48qpv80LkybreMsbOMEq9YmKX85lSXTfAM9v2jxICJdZiWKpEQ04xbduC3icCKwJr7PmRi4sOVjyM3dnBuCAowBVTrPFv8_eSCdI-HrMWSC1zIAjJoWIYhgSeyTvvOziyL1JUFqBVSWfe0TdlVPCL0-VdtUTnt2UBG8hHn_9JHAeLGXTQqfzuHA8_e2k375KjVgEdIGqhDQSmkcpKyrTxdCZQE_OE7efFakX0l4vwDR0VRaHdwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/029d7d5229.mp4?token=CTtErQ-dEnR7aoKOf9nHwhzEEGCVEJ5GbnFEf4ymKEtJxusFL-nPgeruUx2az_M-gdaYTSHI6J3YfPBvwKmXqqG8bNWKAG_dDyS48qpv80LkybreMsbOMEq9YmKX85lSXTfAM9v2jxICJdZiWKpEQ04xbduC3icCKwJr7PmRi4sOVjyM3dnBuCAowBVTrPFv8_eSCdI-HrMWSC1zIAjJoWIYhgSeyTvvOziyL1JUFqBVSWfe0TdlVPCL0-VdtUTnt2UBG8hHn_9JHAeLGXTQqfzuHA8_e2k375KjVgEdIGqhDQSmkcpKyrTxdCZQE_OE7efFakX0l4vwDR0VRaHdwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری دیگر از تیراندازی شدید مسلحانه در ایرانشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/150065" target="_blank">📅 19:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150063">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c98e502792.mp4?token=sY8XAp57lfeMQE1-JB-01B75oa8IOSRBFbd8zZMylxzcc9ZYKSFJx9e8btCKNk5y50gWkQ8bdlpyYjqX4ZkjKVUvqJ0YWrD24b6C5P5y2ae4BfHMTbjU0bVT_5cBZQZs0R6FG4b1Dzfc0W_sH5gvF3PzxsH7UTAhsYF5dE0xJxTAhTFORhe64sJreKhz8JoUTr3hl2MYu4HtbtzAcxXnlahuP1Xx1K_lMBAinvdz56X8_f_JxiEez0X7oP2Doeu4r7fQiv2muOne-zpPQLfvSXkZZiACLuOjx4SQS2S0ph23lj1JPrU0AX5qNYyBnu1Yj4qhhsCZAL4Ft0nLm0F7Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c98e502792.mp4?token=sY8XAp57lfeMQE1-JB-01B75oa8IOSRBFbd8zZMylxzcc9ZYKSFJx9e8btCKNk5y50gWkQ8bdlpyYjqX4ZkjKVUvqJ0YWrD24b6C5P5y2ae4BfHMTbjU0bVT_5cBZQZs0R6FG4b1Dzfc0W_sH5gvF3PzxsH7UTAhsYF5dE0xJxTAhTFORhe64sJreKhz8JoUTr3hl2MYu4HtbtzAcxXnlahuP1Xx1K_lMBAinvdz56X8_f_JxiEez0X7oP2Doeu4r7fQiv2muOne-zpPQLfvSXkZZiACLuOjx4SQS2S0ph23lj1JPrU0AX5qNYyBnu1Yj4qhhsCZAL4Ft0nLm0F7Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/تصاویری دیگر از تیراندازی شدید مسلحانه در ایرانشهر؛ گزارش‌ها از تبادل آتش میان نیروهای نظامی و افراد مسلح
🔴
به گزارش الونیوز/ شامگاه امروز سه‌شنبه ۷ مهرماه ۱۴۰۵، گزارش‌های دریافتی از شهرستان ایرانشهر حاکی  است از دو ساعت پیش تاکنون درگیری شدید مسلحانه میان نیروهای نظامی و افراد مسلح در منطقه غریب آباد این شهر است.
🔴
بر اساس گزارش‌های اولیه، از ساعاتی پیش صدای تیراندازی شدید و آر پی جی در این منطقه شنیده شده و نیروهای نظامی با افراد مسلح درگیر شده‌اند.
🔴
منابع محلی در این‌باره به حال ‌وش گفته‌اند، که ده‌ها دستگاه خودروی نیروهای نظامی و یک دستگاه تانک جنگی به محل درگیری اعزام شده‌اند و در جریان این درگیری از سلاح‌های سبک و نیمه‌سنگین استفاده می‌شود.
🔴
همچنین نیروهای نظامی از پهپاد نیز استفاده کرده اند. و همه مسیرهای منتهی به محل درگیری تا فاصله زیادی توسط نیروهای نظامی مسدود شده است.
🔴
تا لحظه تنظیم این گزارش، اطلاعات دقیقی درباره هویت افراد مسلح، علت آغاز درگیری، تلفات احتمالی و خسارات واردشده در دسترس نیست.
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/150063" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150062">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/488280f6be.mp4?token=guOgPYyReGAtnm3wpw3s6uS5JV7qMqtaAy9uB98AlO7VT6DQZmcZhQvOlT6hTDZ34r1yI8k3uL5xa4fx-F9oU5DINeZGIv_WpYVN7Fsm3f4p-pYc67eQeL0s8pz5ZYA0BrMU3N2ce3zRJysVVywXqsHZSFIET6LUdRpvCbqqy5Y2YX0PRFuYaXQ7gzJ2Q10IscA4I8yKMP4nt1c5fjTeNN6dU8LedIhXlUw8XwF11ZbSVK5SvH8xPlsQSAse1QGgEH03czIVImZZsZqIhgvZTh-TlaKPiyjmpe6rkb5wq9D1LjkE_kIJUvcu68VC2br4vq1dky8n2LKZ8QYOlr3R-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/488280f6be.mp4?token=guOgPYyReGAtnm3wpw3s6uS5JV7qMqtaAy9uB98AlO7VT6DQZmcZhQvOlT6hTDZ34r1yI8k3uL5xa4fx-F9oU5DINeZGIv_WpYVN7Fsm3f4p-pYc67eQeL0s8pz5ZYA0BrMU3N2ce3zRJysVVywXqsHZSFIET6LUdRpvCbqqy5Y2YX0PRFuYaXQ7gzJ2Q10IscA4I8yKMP4nt1c5fjTeNN6dU8LedIhXlUw8XwF11ZbSVK5SvH8xPlsQSAse1QGgEH03czIVImZZsZqIhgvZTh-TlaKPiyjmpe6rkb5wq9D1LjkE_kIJUvcu68VC2br4vq1dky8n2LKZ8QYOlr3R-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی دی وانس، معاون رئیس‌جمهور، درباره‌ی مجتبی خامنه‌ای:
ما فکر می‌کنیم او زنده است. البته نمی‌دانم. من هرگز او را ندیده‌ام.
اما بهترین شواهدی که در اختیار داریم نشان می‌دهد که او زنده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/alonews/150062" target="_blank">📅 19:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150061">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
طبق گزارشات  دقایقی پیش میلی‌گلد همه دفاترش رو خالی کرد و همه کارمند ها مدیر هاشو اخراج کرد و رسما میشه گفت ورشکسته شد و پول مردمو بالاکشید.  @shahab_gold_trading</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/alonews/150061" target="_blank">📅 19:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150060">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJI_i_alL-QQQg-FNvk-Ox81QcNe_5wJxbdXpMWUINTblC1maJU2GuADsxDMkGpfVR7mfQqmF9Adeb2k8dh6k9GT-OizrpFifPT6dEOFsVYb6k-ilSXz32ZdsxWha78QQBxeOA8AOkfEwf7Ytr5S2CrfukMTiuoldyyoHa4JNC2kCZ-qn4hT3cBML7opjBYIzt8A9-cwrsoFtdVYw42pAxpWJOHDnFl7W98ex55SIBwxc_6MoWee8e6AKQGm_Uq-m_FzixCAo1z4wwmTkvju4Mo3MUyuq0to8Y9wp9wH8zxj-NeRKeBN12FpDx-Rr3-Ug891BhYK7F1bM3qigA9PMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مجوز فروش گوشت الاغ و اسب صادر شد
🔴
سرپرست دفتر نظارت بهداشت عمومی با نامه‌ای فروش گوشت تک‌سمیان مثل اسب و الاغ رو مجاز کرد. الان میشه گوشت خر و اسب رو تو بازار خرید و فروش کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.9K · <a href="https://t.me/alonews/150060" target="_blank">📅 19:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150059">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx5d7-DoHRXW76V-Li9zZL5k6gIhu5h4bf4xJIVYJ9X1UEKOb-S01IDr3jFDbrTW29VWFnHyRDIjlJ00aBLPPZBIreb8aleZ25DC9gat7Ukv9nAS09-nPMVeI_pNpcbFgT5iGiC6ghXZKYuliBUXJOmjXBOK6t_wlP4HyXaKPd8l-3YuJdMnr9D3zHzIocqexnk4Z0-zPw7P_BZ3uXbC50VVG6vo7s6qrwU172JOXGH1CFhlYHKmkX7thhcPyMtC6W2dRbMvAeCvyA4Fxbrv1zKSB4kg8iliptueba_iQ0CjC39S19XfDlLMclyUY8waaoZxEVgryYAnP4pU6MqhZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواداران رسایی:
خطر ترور بیولوژیکی رسایی وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/150059" target="_blank">📅 19:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150058">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏
👈
ونس: اطلاعات ما تایید می‌کند که مقامات ایرانی با هدف قرار دادن کشتی‌ها مخالف بودند اما نتوانستند تندروها را متقاعد کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150058" target="_blank">📅 18:55 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150056">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/هم اکنون گزارش ها از اعزام ناگهانی گروهی جدید از جنگنده های پیشرفته F22 آمریکایی به سمت خاورمیانه،
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/150056" target="_blank">📅 18:38 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150055">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
ترامپ: ایران به شدت در حال شکست است و به زودی از بین خواهد رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/150055" target="_blank">📅 18:36 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150054">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5c82cd4c9.mp4?token=SJRDASObdDdk8_uiaNTVd3AZQiFYHGEMg5VASzOdf9EBs--bI1vDf84fKTE-PtkqFz29GY9IUg9XP0lZjRVMAhBUaf7fmSWw0Xp6bF2BzOGYYmIqBFfr3hv9cDzj2RgzDcQr8sme14eSdp5RgFnCJVyWC9td6lG0tLzhVoxZgjjeDzp1lgTJCnFPYRCpt_mXqJS6w4aI8S4Gs94-vEc6KDQsUc6eU1yq1cJ7XBbnvh0G1ocZ35xoQ3mOFy5JGJd28rKGv7ZbEf8-MExmLrBGnX7T0eoa2c9-Cl8K1eXFntpGjegBUEp8jW5WnIlYry47Sn9j87JZ7LP7TFfHNrXIig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5c82cd4c9.mp4?token=SJRDASObdDdk8_uiaNTVd3AZQiFYHGEMg5VASzOdf9EBs--bI1vDf84fKTE-PtkqFz29GY9IUg9XP0lZjRVMAhBUaf7fmSWw0Xp6bF2BzOGYYmIqBFfr3hv9cDzj2RgzDcQr8sme14eSdp5RgFnCJVyWC9td6lG0tLzhVoxZgjjeDzp1lgTJCnFPYRCpt_mXqJS6w4aI8S4Gs94-vEc6KDQsUc6eU1yq1cJ7XBbnvh0G1ocZ35xoQ3mOFy5JGJd28rKGv7ZbEf8-MExmLrBGnX7T0eoa2c9-Cl8K1eXFntpGjegBUEp8jW5WnIlYry47Sn9j87JZ7LP7TFfHNrXIig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
ایران سلاح هسته‌ای نخواهد داشت، و آن‌ها خیلی بد، خیلی بد در حال شکست خوردن هستند. این ماجرا خیلی زود تمام می‌شود.خیلی، خیلی زود تمام می‌شود. آن‌ها سلاح هسته‌ای نخواهند داشت.قیمت نفت به‌شدت سقوط خواهد کرد، درست همان‌طور که قبلاً بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/150054" target="_blank">📅 18:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150053">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/027b715ab2.mp4?token=JbZR2d0b9pki51QOHCxs1WIan6WP5ivzr9-Js4T-OtZQp3ZZ80EfDS5A9K2hYfNF_xR1n2o7Ep3vLpF4rUexHaj77ZrcPWomcT_0AWDsHE8EJ3bDHSvC1BZ6OnFYckxeQe7i1st-XncODd3uEizF93iEv40URfK8PqpfRZ4XwJvAhgiHUwoiTsyHwbDPM1XvpF-f9FhwO08Iu-GLEHafqSEkvzxmsDSwvZdAiwm52Eudf5CYirfIQ5f07rY120LojMhn1HevNYeLK6JjhDse-J1Pt2oPCTMTDAYWVlxYTk77pEMNQ7DDJA7NvwWqjtW-ISMKIXu6BFtfZwqUVoKKGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/027b715ab2.mp4?token=JbZR2d0b9pki51QOHCxs1WIan6WP5ivzr9-Js4T-OtZQp3ZZ80EfDS5A9K2hYfNF_xR1n2o7Ep3vLpF4rUexHaj77ZrcPWomcT_0AWDsHE8EJ3bDHSvC1BZ6OnFYckxeQe7i1st-XncODd3uEizF93iEv40URfK8PqpfRZ4XwJvAhgiHUwoiTsyHwbDPM1XvpF-f9FhwO08Iu-GLEHafqSEkvzxmsDSwvZdAiwm52Eudf5CYirfIQ5f07rY120LojMhn1HevNYeLK6JjhDse-J1Pt2oPCTMTDAYWVlxYTk77pEMNQ7DDJA7NvwWqjtW-ISMKIXu6BFtfZwqUVoKKGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران:
در سال‌های پیش رو، آن‌ها تاریخ کشور ما را خواهند نوشت و خواهند گفت که جنگ ایران یکی از مهم‌ترین کارهایی است که ما انجام دادیم.
🔴
این در واقع یکی از مهم‌ترین کارهایی است که ما انجام داده‌ایم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150053" target="_blank">📅 18:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150052">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
ترامپ:
جنگ ایران خیلی، خیلی زود تمام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/150052" target="_blank">📅 18:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150051">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
عضو کمیسیون امنیت ملی مجلس:
اطلاع داریم که کشور های عربی حاشیه خلیج فارس با تأمین مالی آمریکا و اسرائیل برای جنگی تمام عیار علیه ایران موافقت کردند و در حال فشار به روی ترامپ برای آغاز هر چه سریعتر جنگ‌ می‌باشند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/150051" target="_blank">📅 18:03 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150050">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی سپاه: ناوهای آمریکایی به ۵۰۰ کیلومتری تنگه هرمز فرار کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/alonews/150050" target="_blank">📅 17:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150049">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
نیکزاد: مجلس طرح سه فوریتی خروج از NPT را بررسی می‌کند
🔴
نایب‌رئیس مجلس: ما اصلاً به آژانس و مدیر فعلی آن اعتماد نداریم؛ چرا که وی صرفاً بازدیدهای ظاهری انجام می‌دهد و گزارش‌های منفی علیه ایران ارائه می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/150049" target="_blank">📅 17:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150048">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bccb61d2ea.mp4?token=hD7RL6hvMFXQ_PI1KFZsPd7diyM1XL7vw3lODgqONW1P1X08iJaKbkoqx28TbxGGtEtXnMhohwN4gzMlWcm3BQXMMQ5N6q4FvSSxirsia1m0KIhoeSyk7Klr8yJD7vF669Aw_uQWRNED5VIRNqdlfTiCm4Mc7gyIiqvOEQ6paAuY-xSNuyd46D7GxjvxuBFqwzzXn0-nTGlarjEpCuKdSasmZXMRekkPOvUvlZVIFLk_6lgI1sEbYZtloCLtN6unIfDUMOEzMtLec-dwLWUbf6hBjCoJJ66RIRrR4cyA86rxiUbPIdpkdzUfTMX3EoTmjRypyXnM1TLM1Nq3vn8qfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bccb61d2ea.mp4?token=hD7RL6hvMFXQ_PI1KFZsPd7diyM1XL7vw3lODgqONW1P1X08iJaKbkoqx28TbxGGtEtXnMhohwN4gzMlWcm3BQXMMQ5N6q4FvSSxirsia1m0KIhoeSyk7Klr8yJD7vF669Aw_uQWRNED5VIRNqdlfTiCm4Mc7gyIiqvOEQ6paAuY-xSNuyd46D7GxjvxuBFqwzzXn0-nTGlarjEpCuKdSasmZXMRekkPOvUvlZVIFLk_6lgI1sEbYZtloCLtN6unIfDUMOEzMtLec-dwLWUbf6hBjCoJJ66RIRrR4cyA86rxiUbPIdpkdzUfTMX3EoTmjRypyXnM1TLM1Nq3vn8qfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
شعار دیشب تو شب نشینی‌ها:
چرا به‌جای دزدان/رسایی رفته زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/150048" target="_blank">📅 17:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150047">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnkdxm_vzQgwGI1Sm6MDmP114bfXz75j2XhRE1_yy1URrljbu8McZDwffKHKQ9tTSMXHNCJyrhaIU6PFArwgW-AlNxw9mId9rqosH3eSMwLhTrlnt4FT4jZlrwJ_Oxt3-NP0V-iOuFXnwFhKOfQkK60z13QW6bjx98b1kvZMCmrY3j9ljuoJymNk1WbYFum96KMAltVNb5BIfdSupsC09ioxYydNbr-Jv679VwGkHW580daIi2EDHugwvdQYhgQ4j1GUi2hbrziL0USQnjANpodGEdGFqXhYfJnBCBNvdEB6IG3rehkXtdmSovFxfw2b7MmQjmT0MVvoNwwQLYbcEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز هفتم مهر، تولد پزشکیانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/150047" target="_blank">📅 17:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150046">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ecf3ef8bb.mp4?token=gwRoQxxGQDk4UF7P50t1lRTIVCHe3o-VB_OByT6aJ_uBooodxmFfLQ6RMLWJpsoFazch4BNIL5CuudN3J2wXZ-CYsEaSI9cV8aCOGPYB2arKalTmnAmNkFrs7o4z97WY5nsoIy6SpNdKCTVyrOmkUrIxUCUGYgkJ8zdMy3Y8iaqtLi8hC68s0jvolo-pAV4kc9LoAU15qovcUGM2-_i9erTO7smpCP16P0z3BmZKts6X64ddOAwblWZWVBjs2V0Bx3Br1BLo8LWnf84mp4ORfVRK2TNdaHajwyCU6IxiS6S3eM5SwOOkYUNnFubPvH3UQhoERkd_L7FxLnuCJKl_VAow28Wmq9ugnxmqKAAwrWgNWfkZ_UHCZsoqOkp1XWouclJZmvGsgWuMuJWh2qKperKsn_G6g1A1vFRmA4Qtuua78NpxhGswfmvJVbTfklpkuO8Gq5Zd6T9a7_u9EoaurscLmDoedx8zNlV64aIEqUj2Fq-KpV6_GYCeoiR6jINrvmHLTnzcwt0gFtQtCO2q-chsWdnUxaewLzlLeSrVjSoycccZguFwiUnNsXHMXyHI_bwSyq3POybtWw9QtAZ2eegCSw1qzLaks-8OwhVJw_MXwMNybOHhKfEEa8J-muOL7_MLUZZ8-YIuW8lFZ1X35p22R9jW94SKCxfE89uKmCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ecf3ef8bb.mp4?token=gwRoQxxGQDk4UF7P50t1lRTIVCHe3o-VB_OByT6aJ_uBooodxmFfLQ6RMLWJpsoFazch4BNIL5CuudN3J2wXZ-CYsEaSI9cV8aCOGPYB2arKalTmnAmNkFrs7o4z97WY5nsoIy6SpNdKCTVyrOmkUrIxUCUGYgkJ8zdMy3Y8iaqtLi8hC68s0jvolo-pAV4kc9LoAU15qovcUGM2-_i9erTO7smpCP16P0z3BmZKts6X64ddOAwblWZWVBjs2V0Bx3Br1BLo8LWnf84mp4ORfVRK2TNdaHajwyCU6IxiS6S3eM5SwOOkYUNnFubPvH3UQhoERkd_L7FxLnuCJKl_VAow28Wmq9ugnxmqKAAwrWgNWfkZ_UHCZsoqOkp1XWouclJZmvGsgWuMuJWh2qKperKsn_G6g1A1vFRmA4Qtuua78NpxhGswfmvJVbTfklpkuO8Gq5Zd6T9a7_u9EoaurscLmDoedx8zNlV64aIEqUj2Fq-KpV6_GYCeoiR6jINrvmHLTnzcwt0gFtQtCO2q-chsWdnUxaewLzlLeSrVjSoycccZguFwiUnNsXHMXyHI_bwSyq3POybtWw9QtAZ2eegCSw1qzLaks-8OwhVJw_MXwMNybOHhKfEEa8J-muOL7_MLUZZ8-YIuW8lFZ1X35p22R9jW94SKCxfE89uKmCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
اندی برنهام، نخست‌وزیر بریتانیا:
افراد راست‌گرا در بریتانیا دربارهٔ بازپس‌گیری کنترل صحبت می‌کنند.
🔴
هرگز اجازه ندهید آن‌ها این را فراموش کنند که خودشان ابتدا این کنترل را از دست دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150046" target="_blank">📅 17:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150045">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بنزین سوپر لیتری ۱۱۱ هزار تومان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/150045" target="_blank">📅 17:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150044">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
بر اساس گزارش واشنگتن پست، شبکه‌های CNN، MS NOW و نشریه Politico از یک دادگاه فدرال درخواست کرده‌اند تا دستور ممنوعیت دسترسی رسانه‌ها به کاخ سفید، که توسط رئیس‌جمهور ترامپ صادر شده بود، تمدید شود تا زمانی که دادخواست آن‌ها در جریان باشد.
🔴
ترامپ در تاریخ ۱۸ سپتامبر، دسترسی این سه رسانه را به کاخ سفید قطع کرد و آن‌ها را متهم به انتشار "اخبار دروغین" کرد، اما یک قاضی فدرال به طور موقت دسترسی آن‌ها را به مدت ۱۴ روز بازگرداند. این دستور در تاریخ ۸ اکتبر به پایان می‌رسد.
🔴
این رسانه‌ها اکنون به دنبال صدور یک دستور موقت هستند که به آن‌ها "دسترسی یکسانی" را که قبل از ممنوعیت داشتند، اعطا کند، و استدلال می‌کنند که کاخ سفید این محدودیت‌ها را "به‌طور غیرقابل پیش‌بینی و ناسازگار" اعمال کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/150044" target="_blank">📅 16:54 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150043">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
ایتالیا اعلام کرد که تمام نیروهای خود را به طور کامل از عراق خارج خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150043" target="_blank">📅 16:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150042">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcff1ecb14.mp4?token=BLsm34_biR-VcMw4dGvBhGiMHwTRWacYkYdhI-k5Ceivarnos7kgzH3EZ2t8-YTc9GbZYP6x95Irel633CXrKek-NuRIUeZI9lyTVyURyEOs4B4SOnqY8XUmfSM5JOG5gd_1AYBNuKpzclxXqyZrmpkte7i0C5Alx2BfOeOJ6RL6LewXa6hD5Pv4-PyEIO7Y8Q9Jkeow21tehJ441gy0tRn7x_Pe7vfrj4T5HBx1Nz58499WmRkdc0HfqaA_J17Lq7OtuEuLEzbZWVu_h9_pjKxdAheTNcrzP-opbfoGKsAoBp7_veGVLlE8Awd8je6W2iExyL349f6H3l5fa5U8PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcff1ecb14.mp4?token=BLsm34_biR-VcMw4dGvBhGiMHwTRWacYkYdhI-k5Ceivarnos7kgzH3EZ2t8-YTc9GbZYP6x95Irel633CXrKek-NuRIUeZI9lyTVyURyEOs4B4SOnqY8XUmfSM5JOG5gd_1AYBNuKpzclxXqyZrmpkte7i0C5Alx2BfOeOJ6RL6LewXa6hD5Pv4-PyEIO7Y8Q9Jkeow21tehJ441gy0tRn7x_Pe7vfrj4T5HBx1Nz58499WmRkdc0HfqaA_J17Lq7OtuEuLEzbZWVu_h9_pjKxdAheTNcrzP-opbfoGKsAoBp7_veGVLlE8Awd8je6W2iExyL349f6H3l5fa5U8PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دوربین نظارتی لحظات پایانی بمب‌افکن راهبردی تی‌یو-۹۵ام‌اس را پیش از سقوط در استان آمور ثبت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/150042" target="_blank">📅 16:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150041">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دلار هم اکنون 255,000 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/150041" target="_blank">📅 16:37 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
ونس: ایران باید رفتار خود را تغییر دهد تا اساساً امکان هرگونه توافقی وجود داشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/alonews/150040" target="_blank">📅 16:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150038">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HNLHi0AKPWPxfcltjWUulV5KyNgjNd9th4In9lsamfaGi8YmMWPoMX0Og6XWvpFKjHeO2cH30rOLSoZ93RyTXYAe7T-4XzRWqTVWfVPYa7i-C3yyqGcZGOcEnSEUgOyIioljuz7c8JEqv_g-7Z0s9suj0pBFve0yJF4OAX_29h7IEXEdqlwJf8yp2nOaw68OIqIHyNPa43FHcjMB2RlKPbkur_z0pLNMzrKKWek9vVpSEh23fm8wSdaCL1DIMubtPOFqJjqbuPdxC5Dh5IWIn2p0YDPNXIv7ZBRo4j4-qLVMs2lJHMimkRXW4Z1sXlmYcqiRv6hWMHFYGEiIbxiEFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0587d8651.mp4?token=tJcvPt4U9nvAxSw9IkHheYMvIvpNFVLIX-eEsHgS1pTNrVe3lbPHRZ3pIfzGwtO5W1fY6DvmYJXxMQ2-Ggv4uatBxXsAyA2urwRzwKHxIyz7DKgwEdr5w7an6Brxj4YWakhkim_o-qhx99zRTPZgPtSZo0qR_BocUchJK1_TuHhzroz_EA3kSkZ8fh8YFZyQa2N_T0tpdqqRKz_jpqdH4mbD2NRvqsFimjQHl5y3Vv0z5GmozalUp4A9znnp6aDMpmze-cHS57taHO9gFt591LzHd8mtY3Zgg1hXkii38fm10P1Z0L7IQqI59rZVbT3Ph_xCXuLtbNZ2h2mCJmLKyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0587d8651.mp4?token=tJcvPt4U9nvAxSw9IkHheYMvIvpNFVLIX-eEsHgS1pTNrVe3lbPHRZ3pIfzGwtO5W1fY6DvmYJXxMQ2-Ggv4uatBxXsAyA2urwRzwKHxIyz7DKgwEdr5w7an6Brxj4YWakhkim_o-qhx99zRTPZgPtSZo0qR_BocUchJK1_TuHhzroz_EA3kSkZ8fh8YFZyQa2N_T0tpdqqRKz_jpqdH4mbD2NRvqsFimjQHl5y3Vv0z5GmozalUp4A9znnp6aDMpmze-cHS57taHO9gFt591LzHd8mtY3Zgg1hXkii38fm10P1Z0L7IQqI59rZVbT3Ph_xCXuLtbNZ2h2mCJmLKyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سقوط هواپیمای نظامی توپولوف ۱۵۴ در روسیه
🔴
یک فروند هواپیمای نظامی Tu-154 روسیه امروز، در منطقه آمور در شرق این کشور سقوط کرد. برخی گزارش‌های اولیه می‌گویند ۷ نفر در هواپیما حضور داشتند و ۶ نفر جان باخته‌اند و یک نفر زنده مانده و به بیمارستان منتقل شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/150038" target="_blank">📅 16:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا به دولت عراق اجازه می‌دهد پروازها بین عراق و ایران را تحت شرایط آمریکا انجام دهد:
🔴
پروازها فقط از فرودگاه بین‌المللی نجف
🔴
پروازها فقط به مدت یک ماه
🔴
پروازها فقط از طریق هواپیمایی عراق
🔴
باید اطلاعات تعداد مسافرانی که جابه‌جا می‌شوند، نام‌ها و شماره گذرنامه‌های آنها، و مبالغی که هواپیمایی عراق در ایران برای سوخت، تعمیر و نگهداری و سایر خدمات هزینه کرده است، در اختیار آمریکا قرار گیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/alonews/150037" target="_blank">📅 16:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
طبق گزارش کانال 14 اسرائیل، که به نقل از یک مقام ارشد اماراتی به این موضوع اشاره کرده است، نمایندگانی از 10 کشور، از جمله امارات متحده عربی، اسرائیل، عربستان سعودی، ایالات متحده آمریکا، مراکش، کویت، بحرین، لیبی (هافتار)، عمان و مصر، در بخش گسترده‌تری از دیدار نتانیاهو و محمد بن زاید که روز یکشنبه برگزار شد، حضور داشتند.
🔴
نتانیاهو و محمد بن زاید در ابتدا به صورت جداگانه ملاقات کردند و سپس مقامات کشورهای دیگر به این جلسه گسترده‌تر پیوستند.
🔴
بحث‌ها بر روی تهدید ایران، همکاری نزدیک‌تر بین اسرائیل و کشورهای خلیج فارس، مسائل اقتصادی و سامان‌های دفاعی اسرائیل متمرکز بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/150036" target="_blank">📅 16:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/siiOjlOyKCfs1hGhUAngRPqZISRsG_xXwKaj-4UH9AXdCnyV0eOIu72Z467gKvS6IQE_KKOvmE9dBjSqw9nDgQEwfAM5zlu7xfX1pW9t8wIajY2f_Yf-8Q2xJwVUi-8iTN66b6mYiegmy0Umu7otjeB-c4jcVmJJPjxpsFKCb4aXzJyIytUCSNlbpNYu6FkXUsKnSgPQu8cDTxwD7RD3wSKricD2jbwlaAJ3lrdtJxRdX912naNtA3TATmvO6FyotfkZ5ASSHW4J1FWtRQgKepRX6K4IEq7v9rklebqMNyL826fycMaLEU757gAVw9hjLlZ4H83Ij7vGkITsLIjuOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش لبنان ۴۷ هاموی و ۵ کامیون از آمریکا دریافت کرد
🔴
ارتش لبنان در چارچوب برنامه‌های کمک نظامی آمریکا، ۴۷ خودروی هاموی و ۵ کامیون دریافت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150035" target="_blank">📅 16:00 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=AbUf9ahi1U2tLtOgHtgy_7h1vJQio_AEz6b18A4QE9sHpfjiiW4HF707g9IT1ZzQlEaR9wqPMiGZpT74uIPeE9jlCsULCg4abfm5syRpvcw4lQF-io-zplDjQX8RBb_iCE-U5Meh31FxwgnJqcYVwxHalIzUfQF6ZIkiMvoQAmSDizdbMilpj2qGgfwbwDFkruE3z0VGReOoNMRtbA-gvgKrUWmY_OoXysfJfQhGUO4IPhu0uL8hGIQlMQ2G5cQ4Qd9sKMOmJMAnv-DjKKQzhWYZrwKsQzA-z3qDAHZps9yuuCpdOVhH4phKXc5IYND4qYlNtHC06jF7uZW8ZbFOoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3194b055f.mp4?token=AbUf9ahi1U2tLtOgHtgy_7h1vJQio_AEz6b18A4QE9sHpfjiiW4HF707g9IT1ZzQlEaR9wqPMiGZpT74uIPeE9jlCsULCg4abfm5syRpvcw4lQF-io-zplDjQX8RBb_iCE-U5Meh31FxwgnJqcYVwxHalIzUfQF6ZIkiMvoQAmSDizdbMilpj2qGgfwbwDFkruE3z0VGReOoNMRtbA-gvgKrUWmY_OoXysfJfQhGUO4IPhu0uL8hGIQlMQ2G5cQ4Qd9sKMOmJMAnv-DjKKQzhWYZrwKsQzA-z3qDAHZps9yuuCpdOVhH4phKXc5IYND4qYlNtHC06jF7uZW8ZbFOoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/150034" target="_blank">📅 15:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150033">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80338390ae.mp4?token=X603y5H_mVtvB-IjsbMCV_aMJYEV4mFIcmY38D_riB9cA7e0ylgdFk6JZ_9FvbobpyGnPcSoYMihdxDMYTumuTIgJ-D1nGm7WXqbiDwstr7lSans9762-uU1iYVUCbcS1jV_B0pm7S-_Y9VIMpezvd6KVCAMU-IrEf0-2pajDBl06dR-JU9GYf34rqlx4DtCgXQChiqTGx4mk3grAY2SJpvtS6kI8LwfuUUflET4KNhb3z5VPQ1De3I79Fy0LTD1cvor5w1Zmam17dHzPj6OeDY6h52DEYInsKKU_T4qvydngKeMSh25hF5P0IyZEi9M4UxTwGduhzu22YExJbAUdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80338390ae.mp4?token=X603y5H_mVtvB-IjsbMCV_aMJYEV4mFIcmY38D_riB9cA7e0ylgdFk6JZ_9FvbobpyGnPcSoYMihdxDMYTumuTIgJ-D1nGm7WXqbiDwstr7lSans9762-uU1iYVUCbcS1jV_B0pm7S-_Y9VIMpezvd6KVCAMU-IrEf0-2pajDBl06dR-JU9GYf34rqlx4DtCgXQChiqTGx4mk3grAY2SJpvtS6kI8LwfuUUflET4KNhb3z5VPQ1De3I79Fy0LTD1cvor5w1Zmam17dHzPj6OeDY6h52DEYInsKKU_T4qvydngKeMSh25hF5P0IyZEi9M4UxTwGduhzu22YExJbAUdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: دشمنان ما ممکن است پیش از انتخابات به ما حمله کنند
🔴
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
من در پایگاه نیروی هوایی، در کنار خلبانان قهرمان و نیروهای زمینی فوق‌العاده‌مان هستم. ما به‌طور مداوم در همه جبهه‌ها در حال عملیات هستیم.
🔴
در مجموع، طی چند هفته گذشته بیش از ۱۰۰ تروریست را از بین برده‌ایم و این فقط مربوط به غزه است. البته در لبنان هم در حال عملیات هستیم؛ یادتان هست که در ارتفاعات علی طاهر چه کردیم.
🔴
دستاوردهای بسیار بزرگی داشته‌ایم، اما فشارهای بسیار زیادی هم وجود دارد. این فشارها برای عقب‌نشینی و کنار گذاشتن دستاوردهای بزرگی است که به‌واسطه شجاعت نیروهایمان به دست آمده‌اند.
🔴
من اجازه چنین کاری را نمی‌دهم و نخواهم داد.
🔴
یک نکته دیگر هم وجود دارد: نشانه‌هایی داریم که دشمنان ما ممکن است پیش از انتخابات تلاش کنند به ما حمله کنند.
🔴
بنابراین از اینجا، از پایگاه نیروی هوایی و از بازوی بلند دولت اسرائیل، پیامی برای شما دارم: با ما درنیفتید؛ نه حالا و نه هیچ‌وقت. بازوی بلند ما هر جا و هر زمانی که باشد، به شما خواهد رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/150033" target="_blank">📅 15:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150032">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا به دولت عراق اجازه داده است تا پروازهای بین عراق و ایران را، منحصراً از طریق فرودگاه بین‌المللی نجف، انجام دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/150032" target="_blank">📅 15:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150031">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6MBO-6Tr8iix5QqcTUDyHD7G-e9aKLch6DDLDQfpTVOjedrjrzrUtieNwcVwNxoOlDzMyN4qQ3jO4e0OgGTz3L_0IhsoLNtd7v82_YAI4PMSYY6RhHpZ2JDEUHvYAFjuZnew3v3cNgMOJ9Sb3DpE98QDw0PIuyZySmZCvyxQT3DG9jXxToIAFTSdBAQId72o_RSIEHWvVsF9qKuXS6hq0EcJEzxOCX2Cb2MGShmPiS5jsBUvVfYSdR0QqwEMuQjvc0PdysuTmJsZdx_Ds64KCT4_S5AQixzUwWBlyI7Q8PDfQBy11HZmp5t93gfHoBKzbZjLHdy53I0FLTOjuaqeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر تسنیم از آموزش دخترای جانفدا
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150031" target="_blank">📅 15:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150030">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fed1510120.mp4?token=V9ly7n4z4xyN_FGBGvMy5ShOgte-VhL9MJekH-5AdUjYbmow65umYI9ILJAoUFpyE5w1V8gx8YGGo9XoiNKMCsAfbLCMNUNkIcyrAdPx-fcram9l-tby8xR33UC-3VJXnLDCJqZ6bQGG_jzQG7M12liPLUM0wUwHZVOE69xgstNLdNCdJseuwfog6LCAHjlaUi9CuuEy_MD4rW64WI8niqF3otfsvm-PBw2rKIKvYCvuAlTUZIiZTntfHXdl8xvuNrQlFaig95OICmHgK2fIFktGHO1_n-rZ6XfgYkG0j9q3oTe_98QpVAdsT2HCMSbb4XKSDDxs6zxvTdPuz3mA-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fed1510120.mp4?token=V9ly7n4z4xyN_FGBGvMy5ShOgte-VhL9MJekH-5AdUjYbmow65umYI9ILJAoUFpyE5w1V8gx8YGGo9XoiNKMCsAfbLCMNUNkIcyrAdPx-fcram9l-tby8xR33UC-3VJXnLDCJqZ6bQGG_jzQG7M12liPLUM0wUwHZVOE69xgstNLdNCdJseuwfog6LCAHjlaUi9CuuEy_MD4rW64WI8niqF3otfsvm-PBw2rKIKvYCvuAlTUZIiZTntfHXdl8xvuNrQlFaig95OICmHgK2fIFktGHO1_n-rZ6XfgYkG0j9q3oTe_98QpVAdsT2HCMSbb4XKSDDxs6zxvTdPuz3mA-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نماینده ایران در سازمان ملل : ایران بار دیگر بر حاکمیت کامل خود بر جزایر ابوموسی، بزرگ تونب و کوچک تونب در خلیج فارس تاکید می‌کند.
🔴
این جزایر همواره، اکنون و در آینده بخش جدایی‌ناپذیر از خاک ما بوده‌اند و حاکمیت ما بر آن‌ها غیرقابل مذاکره است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/150030" target="_blank">📅 15:17 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150029">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5A3BKpV8nHdcq2UszXXWngO85Qxj-0lWlQFxQBZ7H8un4MF2SFryaQhKR8FzHRYb1JdLYpEcVVv7CoGudytKKOKP7pXDOW0IBn84zm8CAoAgVFjmNWqpWScfRu0DjIPodN8-ex-VNhBVLmndtFpL3-rT-ccn7kfdfXddiAAlTyX1o_rnLEUptdbejNn1uKGstjYjW0nG6PdANy04J7BW_p5NB6vXzS7iK-J8von4g8LCTR1YKG9ZnIRpp-DaBspdecaOfQ8AWMEngUZPeUZlyrsx7a0s-4SRB3wABo2nSGfWaDhvxCismwbLvI5cCRymXY4n8V80JCNKjUI4DOSsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: آقای اژه‌ای چرا شما پرونده رسایی رسیدگی کردی و بقیه چیزا ول کردی
✅
@AloNews</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/alonews/150029" target="_blank">📅 15:12 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150028">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
الحدث به نقل از منابع دیپلماتیک مدعی شد: واشنگتن و تهران "از نتایج مذاکرات فعلی ناامید شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/150028" target="_blank">📅 15:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150027">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
منابع دیپلماتیک به «الحدث»: کانال‌های ارتباطی میان واشنگتن و تهران «همچنان باز است»
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/alonews/150027" target="_blank">📅 14:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150026">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03578ba96b.mp4?token=gw6zWjkSn6S0o9fVBjcZiYvCZNdY8rpkhuHF55by37bzn7Iqzfca-co5PLtJ6S9y0J3qj8l3vSEeKQxPl5qkEUXt2yUKSL5Kntrv2f3HyJtHuBgb7JyLxrCzx7l2G80t_V-G1SxKqH-DbDMvRk6cHcaVGQFJP1HqadRtKlWk9Sv1Pc7FJxqMFX2_nKsCuVDIt0PHaPcvWQ55bpalxB0c6JPZnDY9MZDNQxUVaJB4fZchMfR5NgY-9M8CICvKk4IgCKindoP4s95FomjR4MFvhcYljz2YLgN60Ib2Sho4nF5XMhD5IEzfMrzekgOgccPz5t943PVDoeKJk3pKy4Gymw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03578ba96b.mp4?token=gw6zWjkSn6S0o9fVBjcZiYvCZNdY8rpkhuHF55by37bzn7Iqzfca-co5PLtJ6S9y0J3qj8l3vSEeKQxPl5qkEUXt2yUKSL5Kntrv2f3HyJtHuBgb7JyLxrCzx7l2G80t_V-G1SxKqH-DbDMvRk6cHcaVGQFJP1HqadRtKlWk9Sv1Pc7FJxqMFX2_nKsCuVDIt0PHaPcvWQ55bpalxB0c6JPZnDY9MZDNQxUVaJB4fZchMfR5NgY-9M8CICvKk4IgCKindoP4s95FomjR4MFvhcYljz2YLgN60Ib2Sho4nF5XMhD5IEzfMrzekgOgccPz5t943PVDoeKJk3pKy4Gymw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گویا میلی گلد دفتر مرکزیش رو جمع کرده و کلا رفتن و سرمایه ملت به باد رفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.3K · <a href="https://t.me/alonews/150026" target="_blank">📅 14:53 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
