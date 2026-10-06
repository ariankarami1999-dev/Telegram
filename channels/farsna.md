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
<img src="https://cdn4.telesco.pe/file/Kf6X10OmpU7k1z3AVH3pgA-EZOwDlkelak9C82BUzd5M0V0_QWNdF6B841ZM8Exp56nSN5GUO5EN1jknCiXOkWwRYbz6gjWzokedGtaVLHA6PArgEVx5RsvZqQKPJt2VfB1uxhbz6owrGcMU7nkuiRP8TVham-H_M8kBJpSXvJmoqlMX-vxbzM-E-eGy01iWYN-yhiaSsUU7W-3U4fE22LqDd_s0Qub_tZFYXYRWoac7LlXhEPyC33XEnmn7NaW9rCvN6NDw99jCKMO69U1XiHpRH58_XYqiiaU255FS2DPI7bti6KtsMg2yDvEoMi3KVQ8qWbfXwDnkEoRCCAxM4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.87M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/farsnews.agencyتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 22:44:37</div>
<hr>

<div class="tg-post" id="msg-466727">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16848e6038.mp4?token=eCUtK3jXMdDpiP8ofAZYyrhBmXAa_1bqzVZ6L1dQb3XtGzQuj9SNoHBBmzxtZCVx22xy_t6Wim8xn1KgQncoPCtNIbGliREajDlQgZoPcEGLw7iHNK9eXuPaWcbx3okfPwEauObIQT84SVOzuGKotee7cgYk9HqNLk0nQPbe8WO6mJIOhN0mjHIi2BIZjh4W-oJGhXZ0xWibDlD60oAoiCVI3T3cuDafNKLCdDjmXbxB8jWPbLDN1SdHpae6CclHk1olwXpSjCG33CtTZf-v6okhAYaWtzSgdCY5WnrJyZVrLOl26aHmNMcPD7cx70JQdKhBbe4i9YLKwhlRDYY9Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16848e6038.mp4?token=eCUtK3jXMdDpiP8ofAZYyrhBmXAa_1bqzVZ6L1dQb3XtGzQuj9SNoHBBmzxtZCVx22xy_t6Wim8xn1KgQncoPCtNIbGliREajDlQgZoPcEGLw7iHNK9eXuPaWcbx3okfPwEauObIQT84SVOzuGKotee7cgYk9HqNLk0nQPbe8WO6mJIOhN0mjHIi2BIZjh4W-oJGhXZ0xWibDlD60oAoiCVI3T3cuDafNKLCdDjmXbxB8jWPbLDN1SdHpae6CclHk1olwXpSjCG33CtTZf-v6okhAYaWtzSgdCY5WnrJyZVrLOl26aHmNMcPD7cx70JQdKhBbe4i9YLKwhlRDYY9Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: علت این‌که ۲ میلیارد دلار ارز برای بازار تامین کردیم این بود که به ترامپ و وزیر خزانه‌داری‌اش بفهمانیم مشکل تامین ارز نداریم  @Farsna</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/466727" target="_blank">📅 22:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466726">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcscpaCoxHV1v0CRXiwQFwubDq84MJeKwkfzEHuvgaIqYyn6opqdiXRrYnA356VBgngHm9UST9jF8ADLXOJUUq36pENgtuWTf9CaxRN5LjOQ66tYdLaAwyWq2pGCP6UckOYT4ckdWiAF8keTkKqMOKe9zG2zl21IJ6QjsZBaVXV1AlwdOhmH2bUTPA_LpZz2mcX0aG0jnZ7hZNGeHZ7MiecvIqNRreDLEMkzbPhqve9z3joXyEZ5rX62n_p4xc-eZDNiPhIH5fAZ4Q_HhWZ3IsTTjWAplm9RnTVGW2D-URohMW3UgbgDzdLXECrMq1ang3V0nADv0mAwPW9putLhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساقدوشی سلبریتی‌ها برای یک قاتل وحشی
🔹
برخی سلبریتی‌ها با انتشار مطالبی در صفحات خود، به حمایت از علیرضا سپاهی، قاتل جنایتکار میدان علیخانی اصفهان پرداختند.
🔹
«مهشاد و علیرضای عزیز پیوندتان مبارک.» این متنی است که حامد بهداد به تازگی در صفحه شخصی خود منتشر کرده است. شاید تصور کنید که او این متن را در واکنش به ازدواج یکی از بستگان نزدیکانش به اشتراک گذاشته است اما این‌طور نیست.
🔹
استوری بهداد هم، پیام تبریکی برای علیرضا سپاهی، قاتل قسی‌القلب میدان علیخانی اصفهان است؛ آن هم برای خبر کذبی که روی خروجی رسانه‌های معاند قرار گرفت و از ازدواج علیرضا سپاهی معدوم با زنی به نام مهشاد در زندان حکایت داشت.
🔸
علیرضا سپاهی به عنوان یکی از عناصر اصلی جنایت در اصفهان، یک مامور امنیت را از موتور پیاده کرد، بعد چاقویش را در کتف او فرو برد؛ او را وحشیانه روی زمین کشید و بعد، لباس‌هایش را از تن درآورد، در همان اثنا، همسر مامور امنیت که ازقضا باردار هم بود، با شوهرش تماس گرفت، علیرضا سپاهی تلفن مامور را جواب داد و گفت داریم همسرت را سلاخی می‌کنیم.
🔸
این پایان ماجرا نبود، علیرضا سپاهی بطری بنزینی که همراه داشت را روی مامور مجروح ریخت، فندکی زد و آن شهید را زنده زنده سوزاند.
@Farsnart
-
Link</div>
<div class="tg-footer">👁️ 969 · <a href="https://t.me/farsna/466726" target="_blank">📅 22:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466725">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb9e04075e.mp4?token=qqe_5AUBdCe9kQOIJ8QPAxRrKxbnn3WIPhBWii2W1seMiz2AIURvfX0_vokPVX7do1Wu0wqtOrgbKEev-IrFkqFafN_gxOhCG1YigNUpS5xoWfZXA-wgEKgd2kdfOwq7oG0y6eSt-hnMkLKAJmCWGUicoQWJ4BE7oHErUXjYOe4kC51xvwyN4w5Uu6AVZbIVZZKVmT21zciERgxP3N9VE9f-taIJ8nRoeai7WK3nkfv90f9zgmST2ra3TMDDdamIsYxEz3KjloXGhR3VkPCoJpl9bagOS1KL7BOqOWs4h8vtIkRiIXVM1EbQhGavv_pEsVmNLH3ovq68g5E0amq2ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb9e04075e.mp4?token=qqe_5AUBdCe9kQOIJ8QPAxRrKxbnn3WIPhBWii2W1seMiz2AIURvfX0_vokPVX7do1Wu0wqtOrgbKEev-IrFkqFafN_gxOhCG1YigNUpS5xoWfZXA-wgEKgd2kdfOwq7oG0y6eSt-hnMkLKAJmCWGUicoQWJ4BE7oHErUXjYOe4kC51xvwyN4w5Uu6AVZbIVZZKVmT21zciERgxP3N9VE9f-taIJ8nRoeai7WK3nkfv90f9zgmST2ra3TMDDdamIsYxEz3KjloXGhR3VkPCoJpl9bagOS1KL7BOqOWs4h8vtIkRiIXVM1EbQhGavv_pEsVmNLH3ovq68g5E0amq2ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: به رهبر انقلاب پیام دادیم که خیال شما از تامین کالاهای اساسی برای مردم راحت باشد  @Farsna</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/farsna/466725" target="_blank">📅 22:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466724">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8807350c2b.mp4?token=UHnr2V8Avzkh3S8oNhAhVnMnAHiFkqMwTJOh_vDC21MIC5RyqpYSWL24dLVtKByDfBdrsy_Zk51TGfRCXovMcCmVbsK6kA0VxCXz1ySaANABHH9e0QL9oY7PbGyXftiRDijg9b6ZlUMXLM0CHJfTG7zs7umc-j-KP1uTNlYBSOOE0bACn3QMqQ-y6vfQEaIqc1rym32mlkLowmpYJ4Jby8tuwuuKLqSlSsu6SzrRLqIN4aqTdP2DSwJgQS_BIPkEJP9boyqmFOi6F0mTYJATYir_fB6QBGmTyuQtZhrgN4DmCP4wGY_zPx7lg1Lg8Ygx8Zuf25aneHvaaQ56eoc36g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8807350c2b.mp4?token=UHnr2V8Avzkh3S8oNhAhVnMnAHiFkqMwTJOh_vDC21MIC5RyqpYSWL24dLVtKByDfBdrsy_Zk51TGfRCXovMcCmVbsK6kA0VxCXz1ySaANABHH9e0QL9oY7PbGyXftiRDijg9b6ZlUMXLM0CHJfTG7zs7umc-j-KP1uTNlYBSOOE0bACn3QMqQ-y6vfQEaIqc1rym32mlkLowmpYJ4Jby8tuwuuKLqSlSsu6SzrRLqIN4aqTdP2DSwJgQS_BIPkEJP9boyqmFOi6F0mTYJATYir_fB6QBGmTyuQtZhrgN4DmCP4wGY_zPx7lg1Lg8Ygx8Zuf25aneHvaaQ56eoc36g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: مردم مطمئن باشند ما برای اقتصاد کشور برنامه داریم
🔹
بانک مرکزی در مقابل سناریوهایی که دشمن علیه اقتصاد ما به‌کار می‌گیرد توابع واکنش دارد. @Farsna</div>
<div class="tg-footer">👁️ 2.59K · <a href="https://t.me/farsna/466724" target="_blank">📅 22:36 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466723">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbac7b4685.mp4?token=ZFt3yG5Z8QbUbrI1SM4R1AsOlSJXCpKWaGIhmctug1--p7LR88r5lwdml4ZRoTl3qW0DStrBx4hKZFHuNLFR4CTcutYJAyZ13YVq-si97xu9UNhkBnYKuzsKLOBCpq69DFlKqVlDgqzMc8UFDIZjZ7uarNdzF_hBDn6tTTUrH5Rhty2Vy52ynKoliBxu8qb921hN-2OlV0GQHWzXXdJM9gxAWrWMFuARdKj3BRZ8U3NV1IRJcTJf4TYYBIGg-CdDgB1MEzH1S8JFs4gpdpmZ6dGY83iu99PVUJpU2S2bY5A2G3ObdvkP90eIO32_-FnURqh1SwcoujqT5eyw1cDMlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbac7b4685.mp4?token=ZFt3yG5Z8QbUbrI1SM4R1AsOlSJXCpKWaGIhmctug1--p7LR88r5lwdml4ZRoTl3qW0DStrBx4hKZFHuNLFR4CTcutYJAyZ13YVq-si97xu9UNhkBnYKuzsKLOBCpq69DFlKqVlDgqzMc8UFDIZjZ7uarNdzF_hBDn6tTTUrH5Rhty2Vy52ynKoliBxu8qb921hN-2OlV0GQHWzXXdJM9gxAWrWMFuARdKj3BRZ8U3NV1IRJcTJf4TYYBIGg-CdDgB1MEzH1S8JFs4gpdpmZ6dGY83iu99PVUJpU2S2bY5A2G3ObdvkP90eIO32_-FnURqh1SwcoujqT5eyw1cDMlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: رشد نقدینگی در نیمۀ نخست سال کاهش یافت
🔹
رشد نقدینگی ماه شهریور تنها ۱.۳ درصد بوده است. @Farsna</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/farsna/466723" target="_blank">📅 22:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466722">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28ec0eb94d.mp4?token=Qvh5S6bdaot0B-QBW3toBOCniJ7td3Op2vYx67Zrq0B2tsZABQ1Kmvmm6vUqp0rDL_bLfGPysIf7z6vSmxl2PtY1fUT-0UDSA0yjSsUkdXILFn4xIaSegvP1ztKjbtxmiQKaKkTb8RDcEiPTYCcQ6qp69gFcJpiQEv9N9VY4tUXRIfWkDev2Fuukyx2cJRH-6aMtrr4LeWoa5gfk6WLwgc6u2Pv8nYXrfug0W-pBFsP2ZZ3F6L0eXOJ-iXB_kj1olGjV5myITa3xMi0eaujNefk42l4SILrrqiWhXQoRzJqJrJ4_YDTJyIiXRr0ouSOsd6cOt7EIQ7khg_QN29j-Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28ec0eb94d.mp4?token=Qvh5S6bdaot0B-QBW3toBOCniJ7td3Op2vYx67Zrq0B2tsZABQ1Kmvmm6vUqp0rDL_bLfGPysIf7z6vSmxl2PtY1fUT-0UDSA0yjSsUkdXILFn4xIaSegvP1ztKjbtxmiQKaKkTb8RDcEiPTYCcQ6qp69gFcJpiQEv9N9VY4tUXRIfWkDev2Fuukyx2cJRH-6aMtrr4LeWoa5gfk6WLwgc6u2Pv8nYXrfug0W-pBFsP2ZZ3F6L0eXOJ-iXB_kj1olGjV5myITa3xMi0eaujNefk42l4SILrrqiWhXQoRzJqJrJ4_YDTJyIiXRr0ouSOsd6cOt7EIQ7khg_QN29j-Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
همتی: رشد نقدینگی در نیمۀ نخست سال کاهش یافت
🔹
رشد نقدینگی ماه شهریور تنها ۱.۳ درصد بوده است.
@Farsna</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/farsna/466722" target="_blank">📅 22:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466721">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار تهران - خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pacjebBEdvUmxPnaVVuXxphNITv88_uqiwCiHYf2NilsqkUuFNlZnrrmWz4CocayEr1sv4b1edB-Ext2ObiVZWdvIIFjAFcW8GU1ovJjVkIOjXENDpgpshiw7jqz_xbJnuxbAvdYIgVDFQ1IWD5fqKm29PF30CpLRZ40d4Z3E0Hb-C-QM4q3bHivlx9Y3AL-16CjUy2ZkYaisBpBiH5uiIy5C7x9IrCnXfUAlLjAcXGkHHzH19PYyF0_pqNDZXXwkcf3A09-ZHHaeKYrgN8FsZh5etnjYAnPUT-AhpA9af5jb2tR_6VEF3r-vvRAVFYhLmj0zt4DWfYf3At-jOFARA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قاب کج آقای مدیر در هفته فرهنگی پایتخت
🔹️
انتشار تصویر یک زن بدون حجاب در صفحه عبدالرضا چراغعلی سرپرست مرکز امور اجتماعی استانداری تهران، آن‌هم در آستانه «هفته فرهنگی تهران»، تناقض آشکار عملکرد یک مقام ارشد با برنامه‌ریزی‌ های فرهنگی و اجتماعی را به نمایش گذاشته و موجی از انتقادات را درباره رویکرد دوگانه مدیران دولتی را به راه انداخته است.
🔹️
این اقدام دقیقاً در مقطعی رخ داده که مساله حجاب به یکی از دغدغه‌های مردم بدل شده است، مخابره چنین قابی از خروجی عالی‌ترین مقام اجتماعی استانداری تهران، این پیام مخرب را القا کرده که در درون ساختار اجرایی، مدیرانی با نگاه و استانداردهایی کاملاً در تضاد با گفتمان انقلاب اسلامی بر کرسی‌های حساس تکیه زده‌اند.
متن کامل خبر را
اینجا
بخوانید
@TehranFarsnews</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/466721" target="_blank">📅 22:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466720">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZhgC_A-kaaFOqBQPEysuQ2WFiWcUvIir-TzKuMTS1fiIMPFR4hoR8_dIVHrXAyP_WcTngx9HQtbx3n9VIpSS80gZOFxzWBORm9OByXu-8RlA-teavZjKU7624asnmTa9bXAF0W5xr16alaa6TRHWZuBpB36l2YAsmPnUxgDQWQj6jZwrAPv9oR3iyz63WuGG2aKkQfpwb8Ts7ojBHivggwHyIdqS8WLObcifQuUY8ebWmPv9ErtLa-UMGy-9UZCkXb5wtBjhTm7IBQZCYXwdpMgDRgkMzfFpV3lLFEqLoc5U9PmgwrMFf71KL_phtJREsmsElELGz7NMph4P8HzxCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
روی هم، اندازه ایران نیستند!  @Farsna - Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/466720" target="_blank">📅 22:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466719">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f70bd7ae4.mp4?token=hkEy3Xjazhk6PARhy8qnkkrxlfg5DA-eRGzhQE4-T1giDPcNX05oxfeWknShkIcMBtWRdWCwY6KdwPAWbVeiYX1588sN6jRJALYx4Dg_UbkfZ9FwGpEyptKbwELssT6SZb1bDeEWgmgmzf7KuU6WyuBTHy3a1As7wVY3O6WK4kDsX4i_xkxwAej3y1CdYp83r_F_4otTwlsrpSTx6xztQiyjm15v_8iY7OorQseKd5WstKAa5JkpSAYK-e7iK-4Odu_zYrhPjxVZQpddsJ-OQTeKJnZza7EKVRTURIseUHoW_t3v5C3FlBw3qBeVWrUSCKCqWvmjISiCgmNYc57CZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f70bd7ae4.mp4?token=hkEy3Xjazhk6PARhy8qnkkrxlfg5DA-eRGzhQE4-T1giDPcNX05oxfeWknShkIcMBtWRdWCwY6KdwPAWbVeiYX1588sN6jRJALYx4Dg_UbkfZ9FwGpEyptKbwELssT6SZb1bDeEWgmgmzf7KuU6WyuBTHy3a1As7wVY3O6WK4kDsX4i_xkxwAej3y1CdYp83r_F_4otTwlsrpSTx6xztQiyjm15v_8iY7OorQseKd5WstKAa5JkpSAYK-e7iK-4Odu_zYrhPjxVZQpddsJ-OQTeKJnZza7EKVRTURIseUHoW_t3v5C3FlBw3qBeVWrUSCKCqWvmjISiCgmNYc57CZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه: طوفان‌الاقصی آغاز پایان صهیونیسم بود
🔹
این عملیات نه تنها افسانه شکست‌ناپذیری ارتش صهیونیستی را برای همیشه فرو ریخت، بلکه جبهه مقاومت را در سراسر منطقه به یک واقعیت راهبردی غیرقابل انکار تبدیل کرد.  @Farsna</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/farsna/466719" target="_blank">📅 22:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466718">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56020e833f.mp4?token=s0c35VAfc3UiwvgAcgkvyll0xo1amUooJCwRDUofkzr2XmFwvs9tMpqM2JTfw2xU0K0ZXoEOlWcNynm_GFxeFI9iVxzH6UioiFcbJKtE6NMFfQI3dvSpLzRBQKljgefndJijngYpXHdKBD0K8hlZmSDIsViIUeiesHVknWn3_0EP2LEi0e2lfi6gBp6tgIKKbXYpqXhpvux9kCl-UGoZJRMtzyFCD1BpoBrqx6-0nhOy3Jl0NOeTFAn0P0VSH_AUyuFAOQEpeV-6UWKYpHtik4f-pWXpuzEHpWAeKbSPgU4N4wSBDa8I9JkguRr5ZdnCCmPMYcpf8hfxSVC7X4YA2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56020e833f.mp4?token=s0c35VAfc3UiwvgAcgkvyll0xo1amUooJCwRDUofkzr2XmFwvs9tMpqM2JTfw2xU0K0ZXoEOlWcNynm_GFxeFI9iVxzH6UioiFcbJKtE6NMFfQI3dvSpLzRBQKljgefndJijngYpXHdKBD0K8hlZmSDIsViIUeiesHVknWn3_0EP2LEi0e2lfi6gBp6tgIKKbXYpqXhpvux9kCl-UGoZJRMtzyFCD1BpoBrqx6-0nhOy3Jl0NOeTFAn0P0VSH_AUyuFAOQEpeV-6UWKYpHtik4f-pWXpuzEHpWAeKbSPgU4N4wSBDa8I9JkguRr5ZdnCCmPMYcpf8hfxSVC7X4YA2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سیل جمعیت آرژانتینی‌ها برای خداحافظی با مسی
⚽️
لیونل مسی بامداد فردا آخرین بازی خود با پیراهن آرژانتین را مقابل بنین انجام خواهد داد و پس‌از آن برای همیشه از فوتبال ملی خداحافظی خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/farsna/466718" target="_blank">📅 22:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466717">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IdWLA_7ClEg3cv2Y852aZF5051526WckwKuAG0CaL3G-9pgsbmoZQ36hMNhIBoI_cNkbJ7sXqMbEJatzC3binceQ6S7Xajs7xiGptR4MjPjkQreRJHmRuV7cLDnIZU5iy3Wi71s6mW5P88xvKud0jXB7fKLEp3iUXD7j2jtJWmDAKOspPRP4iO_zNjjfrTr2ErLXO0TqlMXnk2EA7Czysh-gZB4SVpxrliEeae9z40hiEUAKjYrSjArugHfE2meT8IRN-7Pc_iRxHcDakVnfOfPPM9GTEcCwa1rJ5hhrMrckNcctHyNOQy8Nw2N6ILNdNGYONkEfFGo1TnT-ENi0GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف: شبح وحشت در انتظار اقتصاد امریکاست
🔹
قالیباف در واکنش به اظهارات وزیر خزانه‌داری آمریکا، با انتشار یک میم اقتصادی نوشت: «آماده‌ای تا روح تو را تسخیر کند؟»
🔹
در این تصویر، نمودارهایی از قیمت نفت و گازوئیل تا اعتماد مصرف‌کنندگان و توان خرید مسکن، کنار هم شکل یک شبح را ساخته‌اند؛ با این کنایه که برای ترسیدن، لازم نیست منتظر هالووین بمانید؛ گاهی کافی است صفحه اقتصاد را باز کنید!
🔹
در تصویر دیوید زرووس، مشاور ویژه جدید بسنت و حامی کاهش نرخ بهره، دیده می‌شود؛ همان کسی که گفته بود تا فدرال‌رزرو نرخ بهره را پایین نیاورد، موهایش را کوتاه نمی‌کند!
@Farsna</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/466717" target="_blank">📅 21:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466715">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyAN_JuY8S6mTI2VDpzoWxuK1v7sVF-XB2feBRLu2swcEVxMC-0t2e9m7Ge0YDJDFUT22MxdmvBm8opc08uGFcSf6v9ClMIkImaVjA0iSKH2ziirNyhkwv-fSG0_sk-TmLHRMNoV3aZ1_coBVCwODgbyPgVtC0llINpZXe7_bpH_aZA0YTKnKMGuc5mvPPTC71D5lLmoCkpe1Jx0J3RUum9xIcZA3yBqRbtycF6uNuIatMZeQtGMT-eJugqb32X8tzFRxCVjDeSZxNbvSOG_E9mAkiFiq8B0B05g6gLt_X7hNzcai05CtZWVZebXMupHIVZ9KcjR2XB0jqp3bip7Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنهان‌کاری جنگی آمریکا؛ وزارت جنگ آمریکا کریس مورفی را به العدید راه نداد
🔹
کریس مورفی، سناتور دموکرات آمریکایی گفت وزارت دفاع آمریکا در جریان سفرش به خاورمیانه مانع دسترسی او به یکی از پایگاه‌های مهم نظامی آمریکا در قطر شده است.
🔹
او این اقدام را بخشی از…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/farsna/466715" target="_blank">📅 21:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466714">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس علم و فناوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/allfikjMlIEqBc3cClMDxNIZoh01qqGzEdf6fCBqGfxNrWeAtFd4FZfE-2dSIZPDsYunFiB8C0MDE74mUpn8jR49UBvbpLupifECia7FvDHcXg1fSFtNO6QBWuBvgDi6Df8OGe-J7FiQjVha8GVjc62yW45SjQxt8kEiKMAHLrfI9R_nCNYBST3DR6GxDoQg1u_VUjAleHtpOiZww__rkitZs4K50bJXalZYPbal920CETxA8IMXnljqQi7M2Bvsj51qbvaEeQo7wPouah_IzC3BNfgAbjopDeFQg3h5x6mNUC2V1zSCIPgUieuK4FGovG7BAf3saQBx8AsNKKGOPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثبت صدها اختلال اینترنت و موبایل در فرانسه
🔹
براساس داده‌های سامانه پایش اختلال دگروپ‌تست، امروز ۴۲ اختلال اینترنت، ۱۲۰۱ اختلال موبایل و یک اختلال تلویزیونی در فرانسه ثبت شده است.
🔹
در میان اپراتورها، «فری» شمار قابل‌توجهی اختلال در خدمات اینترنت و موبایل خود ثبت کرده است.
@FarsnaTech
-
Link</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/farsna/466714" target="_blank">📅 21:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466713">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4TIFZ6KNayZVz-s81w05vAjOZZt22zMtXgRee9EoSqY0iJDr8mUMyXBvVwvWakNJMa9CVSLBUMSqOiiMfpCiCIlVuFlt3OFJhKcoNQZW86Czi4or3eWkixEiHGVkNteVJY80cOKN7RW3J9IKo-7UZq0ZzKhMLbvX0F0Q-oTM5CvIBi2l7rrwnns9TOI8-rqkxLJ0Qgzf01J7eQZHNeIdvsCunrcsYwgrsY-9w7HdOz6GEWM8bhigCbhoz4pKY-O0yDNCHxxkMV-JnxL2rf2IZmW_mxg381g4z2MA_i19RLggvyuOudsgPTG8SZ_U8uRxj2CU1od-vYGC8I4IzAY5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماجرای «طاعون» در روسیه چیست؛ آیا باید نگران باشیم؟
🔹
در روزهای اخیر، گزارش‌هایی درباره مرگ یک کارمند آزمایشگاه در منطقه ایرکوتسک روسیه و احتمال ابتلا به طاعون منتشر شده و نگرانی‌هایی درباره احتمال شیوع این بیماری ایجاد کرده است.
🔹
با اینکه اطلاعات قطعی اندک…</div>
<div class="tg-footer">👁️ 6.17K · <a href="https://t.me/farsna/466713" target="_blank">📅 21:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466712">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">‌
🔴
سپاه: هرگونه خطای محاسباتی و تجاوز مجدد علیه ایران پاسخی دردناک و ویرانگر خواهد داشت
🔹
آمریکا و رژیم صهیونیستی در همه جبهه‌ها شکست خورده و در دستیابی به هدف کلیدی خود یعنی تضعیف، شکست و تجزیه ایران به عنوان قدرت منطقه‌ای، ناکام مانده‌اند. @Farsna</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/farsna/466712" target="_blank">📅 21:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466711">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iksO6j3QTpQB8ZXVxHyU02siPJ2_IogokR8Dy6w7ADkZ6QqZAxCo10hoqrUdQiKZyBl5-dJ46Q7Yo3uDLKpF3kENBl0SHaGvUoEs8w1Bxrk0O5mc5y3bzPwT9-EygtGeVUXZmJfT3Vk2vK9c-buo2pjoPY6K4hZPRu2B5HYsViA7GudIRxQahlNtKahCwIIxxWgJ9coAR-NttvpdZHOGRVRXDqkMCMB7XYeOYYmpQppR4BbbD-f1CigzgMDyhIGgmGV4fMdPYfJj3MwPQIpkmTW9kPWsKGZsHo-j9jJ8Jz1LgDw9ZzWQ-9WaNhoN4T_63OHB5Rqe84FKy3l20Qm-Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳ درصد کاهش مصرف، ثمرۀ تغییر نرخ سوم بنزین
🔹
مدیرعامل شرکت پخش و پالایش فرآورده‌های نفتی: اعمال نرخ سوم بنزین باعث رشد ۱۲ درصدی مصرف سی‌ان‌جی و کاهش ۳ درصدی مصرف بنزین نسبت به بازه مشابه سال قبل شد.
@Farsna</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/farsna/466711" target="_blank">📅 21:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466710">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سپاه: طوفان‌الاقصی آغاز پایان صهیونیسم بود
🔹
این عملیات نه تنها افسانه شکست‌ناپذیری ارتش صهیونیستی را برای همیشه فرو ریخت، بلکه جبهه مقاومت را در سراسر منطقه به یک واقعیت راهبردی غیرقابل انکار تبدیل کرد.  @Farsna</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/farsna/466710" target="_blank">📅 21:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466709">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EGOk1ZwwjJy_3eunN3bD-Kgl8isadXMaOztg4_HCMVCTRp_ZbPhq5udn9BlGsntBluonUaxtdBVoz9lSSe9hAuGqxv0G9k_04C4oEFx6-EdmMOlNzbscIxGaI6xsWfNcNby5ELAh5WxT_Oowel1_pdkkQbvA9GXauVw9PeKhkQEd9xaMUm8r5k2k-l50T5noN9R7_nTzZ2vAGImqBSahyLhOIkL0HnGGWWz0FZPyoNCA9R-XQxrSm_jPh8Feh5WVFwaigix4sbPSUie7LjohFZf7gH9AdGf0TEtwS2vIJDBFGr4Pl05UPnncT7D5Ix_ifxUbl2ZUScH-_kNCUZUoZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه: طوفان‌الاقصی آغاز پایان صهیونیسم بود
🔹
این عملیات نه تنها افسانه شکست‌ناپذیری ارتش صهیونیستی را برای همیشه فرو ریخت، بلکه جبهه مقاومت را در سراسر منطقه به یک واقعیت راهبردی غیرقابل انکار تبدیل کرد.
@Farsna</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/466709" target="_blank">📅 21:30 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466708">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0b03d96f4.mp4?token=JrAScbT0T3X-RwMgtvsBU5JpvpmaipIt0LmOnsxzqGl79CyDswnzo8HbeIS3jm24lZDEsb27erdFz_Lb5zXmnBSxQk1HeOQtSrfv5OUzWfdVPzqm6vXFLxrQppSn7R8F34931bJ1KUmf7tdxoXq3ygBe3qb2iaAyPniO8fY-ymtz9UthuX0iHE81S0ZJG1SyfUD7SSLrXBu4D3DNdYhNZ-DnuC8XJ24zVgYt4TJYnOsLKurJS9F28mHcdjcky81gFLA6-CFaBRUyWXHGglmJs4n7lnGaOMi7WwjSeV_SmtGs9CWori3oJP2PV-To3V-FL8iH8wNaudyh0iZEaQpPBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0b03d96f4.mp4?token=JrAScbT0T3X-RwMgtvsBU5JpvpmaipIt0LmOnsxzqGl79CyDswnzo8HbeIS3jm24lZDEsb27erdFz_Lb5zXmnBSxQk1HeOQtSrfv5OUzWfdVPzqm6vXFLxrQppSn7R8F34931bJ1KUmf7tdxoXq3ygBe3qb2iaAyPniO8fY-ymtz9UthuX0iHE81S0ZJG1SyfUD7SSLrXBu4D3DNdYhNZ-DnuC8XJ24zVgYt4TJYnOsLKurJS9F28mHcdjcky81gFLA6-CFaBRUyWXHGglmJs4n7lnGaOMi7WwjSeV_SmtGs9CWori3oJP2PV-To3V-FL8iH8wNaudyh0iZEaQpPBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی نخبگان نجوم، مسافران هواپیما را به وجد آوردند
@Farsna</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/farsna/466708" target="_blank">📅 21:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466707">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mab30xsw9UTMLFw1cm8Q2Ud0Y1qo8Lc2IQlOwUyC4Yl72eTMnv2Pphg72aFs7Mqb5jj3BmGhKY0TTtX3qI_nkLks34JvpWrNm6uwPCyi1TTuie-eXRz73QY_cDU2XcGR668d1nsJP25mJsJju4N2O2XHIZd2r35Rfq_7e2GO1LI7ufGJ7pNkfJ9YcOSOsmnwywEwjuremAPudLw9uil4HVQcPU0VLZfCL3C1ICuamJzih2d5CdSwEBcrGV67PH_b3QttKHYDcBR--fOhynpYLFZUxISUCeJ85qGJsKc91v9VWddJ6zMnnCRw409sI1Uj52NCPxxhTF4jYJGsh1wPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان: یک کشتی در مسندم هدف حمله قرار گرفت
@Farsna</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/466707" target="_blank">📅 21:18 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466706">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس من</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTPCQ1Y2hvD5-E50S7uMPyPJdqMSsBwHuC6NPaF3r65Ub7bHK6nPcmmfh_jTfakVwOupKgUZb_1v_thlontDaAxI4yhqeLLDrpsSYKJcQWpEs6MtbPgqsErgjoYJEnlqERFmGpI9ZNH6WbJ9vbkizqu-qY9L_L0FeFyrOUK4ETmsgaI1O5ehR5-6zqC3jGCC00klWPyWaZ6wf3ctb0OQIJyWAoJlgoWZr3iG9kMSvwSEBcADnEIean-jMrKx2Z2esiyJ9qCU_S9uBfEgRaOs5JcXPuT4PkRGQ26JHSWlgRxMJONYdru4mM6VFDDsB2l2TxeNVXucQsbBd970sqS3wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طرح تورم صفر به اصفهان هم می‌رسد
🔹
رئیس شورای شهر اصفهان اجرای طرح تثبیت قیمت کالاهای اساسی در این شهر را منوط به تأمین سازوکارهای لازم و حمایت دستگاه‌های حاکمیتی دانست فروشگاه‌های کوثر نیز می‌توانند یکی از ظرفیت‌های اجرای این طرح باشند.
🔹
مدیریت شهری اصفهان با تشکیل کارگروهی راهکارهای کاهش فشار معیشتی بر مردم را بررسی می‌کند و امکان اجرای طرح تورم صفر برای کالاهای اصلی و ضروری سبد خانوار را نیز در دستور کار قرار داده است.
🔗
متن کامل خبر
«
تورم صفر به اصفهان هم برسد
» را اینجا بخوانید.
@Farsnews_My</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/466706" target="_blank">📅 21:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466705">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎥
روایت یک طوفان تاریخ‌ساز
@Farsna</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/farsna/466705" target="_blank">📅 21:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466704">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDyELkmcG8ovLSHnRyGxKETcy2XpX_PsEPHNlqe6-2ws73GVzZQvvlElwqCK1FQDBd_bMx3aVtWrYuD6ew8-s1CqMme-KuBu8gRUqWC89sanO2AZTo2PWa-YyusGZ72NTjYb8D0_j_CP9HYtUcvhOa2dH5thBCfeF4XrKbbrRuloB8RSt-EJTxN73RTZ1ttZORgEQSkZpJq4g-QhLDCBNAULpUWd2vwCC1JHPT7Wq9eIdPRnmTrEKdehx63GWmbetVdHayQ2O5XU7pjpmmbcXb_x2Xfhmt2gQ5l23Q2cCfOaOWvKttbznX7y_JPH7jeyZZ_iI7mGILK1A3o2KpXiiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ای ستمگران صهیونیست! عامل طوفان‌الاقصی خود شما هستید
@Farsna</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/farsna/466704" target="_blank">📅 21:04 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466703">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/435c6bd438.mp4?token=XNdRDhTKsCANUwIn1Rc1m2sHm0VFiAZ_yewqmNcuq4-mWBj3l5Tq4vLnca3JyH8NJg7lob5GgghZAhkKlmDwIyhX2aaR3b8EB0BO1vdESP5T98uuRboMkmGJkMtfK9MCg7SQeuGHkksN96OFIUKKherZj0vvv7dToHQoPCkxx6fgtBe4GspI-UQcbMPgFSKDni17BIIg2MmWepeSn-0UeBRmEcZDLlJRFskpH3g_1UmezrDFDK5dUlfmyp1SSM_CpShjxo5Bmd7F9pwXSx_UI6zRJ7dwMle5O-8imaye8Wd5HyISD6fbvQ9xCAob8KmvAHuLJBtpS65E1svkQdVyng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/435c6bd438.mp4?token=XNdRDhTKsCANUwIn1Rc1m2sHm0VFiAZ_yewqmNcuq4-mWBj3l5Tq4vLnca3JyH8NJg7lob5GgghZAhkKlmDwIyhX2aaR3b8EB0BO1vdESP5T98uuRboMkmGJkMtfK9MCg7SQeuGHkksN96OFIUKKherZj0vvv7dToHQoPCkxx6fgtBe4GspI-UQcbMPgFSKDni17BIIg2MmWepeSn-0UeBRmEcZDLlJRFskpH3g_1UmezrDFDK5dUlfmyp1SSM_CpShjxo5Bmd7F9pwXSx_UI6zRJ7dwMle5O-8imaye8Wd5HyISD6fbvQ9xCAob8KmvAHuLJBtpS65E1svkQdVyng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر دادگستری: چرا هنگام دریافت حق بیمه قانون اجرا می‌شود اما در پرداخت خسارت و دیه نادیده گرفته می‌شود؟
@Farsna</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/466703" target="_blank">📅 20:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466701">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b48e8b9f39.mp4?token=g4VTPn0JUVKYSO6OFxO5hAvrXoqUCeWtyoajPvV7joHfKKnIjvhk4rwv3bg2DQ0eZ1TqAhcjL1iRf9qYGfEiL7CsII6r8OxuTnul7Yls9rUKkozuOQBE1Vyu7KTsmMrl_57E6yMENrR_SSeM2odZ27U6gyRBftHbGPAftfQchq4CHklyyZcfjgI7-F0AjCwAA0Yh9tOSfwxZpxyFWUlL4fug-yPUrwXN1HFiT2MsqSg_zFgWaTDzo5TL3CylTbRp0tEixHFJuG-rSa2m0Hx9ZotG6xQm-rtvkbumUHZJIG74rAl-1iZ1BPH6xvBghLa4lMvFEJfXt2CrlwgxWQtpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b48e8b9f39.mp4?token=g4VTPn0JUVKYSO6OFxO5hAvrXoqUCeWtyoajPvV7joHfKKnIjvhk4rwv3bg2DQ0eZ1TqAhcjL1iRf9qYGfEiL7CsII6r8OxuTnul7Yls9rUKkozuOQBE1Vyu7KTsmMrl_57E6yMENrR_SSeM2odZ27U6gyRBftHbGPAftfQchq4CHklyyZcfjgI7-F0AjCwAA0Yh9tOSfwxZpxyFWUlL4fug-yPUrwXN1HFiT2MsqSg_zFgWaTDzo5TL3CylTbRp0tEixHFJuG-rSa2m0Hx9ZotG6xQm-rtvkbumUHZJIG74rAl-1iZ1BPH6xvBghLa4lMvFEJfXt2CrlwgxWQtpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت دوگانۀ اینترنشنال؛ از پلیس تهران تا پلیس پاریس
🔹
اینترنشنال که همواره با تخریب پلیس و نیروهای امنیتی ایران، هرگونه حضور آن‌ها رامساوی ترس، اضطراب و تجاوز به حریم افراد می‌خواند، این‌بار حضور گسترده و برخوردهای وحشیانۀ نیروهای امنیتی در مدارس فرانسه را «مایه آرامش و امنیت» معرفی می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 7.25K · <a href="https://t.me/farsna/466701" target="_blank">📅 20:48 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466700">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCPfv0pumOa8Mp6QJe4CBpArMUZjhun-uZq4F0h9ng-yBq3O8jBfjk_Uy5iNHQNU3BmED_Yt5fMDWWKr5Fs6OvtKkxXRq0n9NuYMGEW2kriHy83lXAZgiLsPSQ5gwJQ4B3x8mpX9blWaPA7vm4BZ5B85EFW2bCIjAjlR_D98C9AVGNifyV2IYGy1aAeo8ZD1Qzs2qIRVPfi9IqR7f3EuF0qzsGQ2-PAepCFj6u4ohd7FdnYGzSMr00JMbl0b6CsmxdUXc4ymhXCgn-X52WyXrWowUNpx_X1HKMDWAxr1tysVO9hISHk321QOJYnZR6dze4gbYjA5oqhl9ABaWE-9Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمار حسرت‌برانگیز هواداران استقلال و پرسپولیس در آسیا
⚽️
کنفدراسیون فوتبال آسیا آمار میانگین تماشاگران در فصول ۲۰۲۴ و ۲۰۲۵ را در غرب و شرق آسیا منتشر کرده است.
⚽️
در بین ۱۰ مسابقه پرتماشاگر آسیا دو دیدار استقلال و النصر عربستان با ۷۵ هزار و ۱۳۰ نفر و پرسپولیس و النصر عربستان با ۷۰ هزار و ۳۵۰ نفر پرتماشاگرترین بازی‌های قاره آسیا در این ۲ فصل شده‌اند.
🔸
این آمار افسوس فوتبال‌دوستان ایرانی را در این فصل بیشتر می‌کند چون ۳ تیم استقلال، تراکتور و گل گهر، به‌عنوان نمایندگان فعلی ایران در آسیا از میزبانی در کشورمان محروم هستند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/466700" target="_blank">📅 20:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466699">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5219cb68c.mp4?token=OdYJTQvW-ehZPeVTKva08n-KKvYI_kJ3uuJjBxfPWhu212f3rN9fSvhleSRpbAq75Bn_m7dGqABX9-0U2bI0ZlBpMfG4hdMqAoF3J5rbgaW8-VD-y3ipwBMOfaZKOblr1IYCDOFXS3zRA2N-D9FZp4-ONI_QOoiDx4Luaubv7pVtglH1AsfHyEub1OF7GZVBOyr0PCrI7G1sXNnMs3UVfhyKFoTufTRPg5QuUOex4Zwp0goWDky4Z6HLnip0tSotRvK1ZQVK24arNEFOAT-au5NMz1MESpwwuU_3JWIp92I5OHxVKUtozpbRWMo3iOduA6C-CkPhAGBwICIIxjDblaiWPg-trZ-SyigE-H6Gg-QZW7nLAVLmiWN8nzoH0swupYu7pI_jDhLS3cJ4MbbmTGBDydyphEy0fHqQBiAxjiNldZP4dwdgOSxpScSs_CQLCKaoJwiycuNh6gP03lz5ddVpmNlv24FhHgQLN-sf7P7dkxZjKhZwSZNGyQzNfme9E1xja6BQXZCRukopVo4q8y1hI2AGzieM2eQU2of9ytTvDO2QkWGpDGV3VpuQRBFh2S1GIm216ufIrYqvdj0bEI2q0AkVyjtWSj5xbk9ggiyl70WYrlt2JUOBhbwcqXUDqRw3GRmjgEeiH2TXqOzq84hU9C5Xh2gMu3YIAJJznp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5219cb68c.mp4?token=OdYJTQvW-ehZPeVTKva08n-KKvYI_kJ3uuJjBxfPWhu212f3rN9fSvhleSRpbAq75Bn_m7dGqABX9-0U2bI0ZlBpMfG4hdMqAoF3J5rbgaW8-VD-y3ipwBMOfaZKOblr1IYCDOFXS3zRA2N-D9FZp4-ONI_QOoiDx4Luaubv7pVtglH1AsfHyEub1OF7GZVBOyr0PCrI7G1sXNnMs3UVfhyKFoTufTRPg5QuUOex4Zwp0goWDky4Z6HLnip0tSotRvK1ZQVK24arNEFOAT-au5NMz1MESpwwuU_3JWIp92I5OHxVKUtozpbRWMo3iOduA6C-CkPhAGBwICIIxjDblaiWPg-trZ-SyigE-H6Gg-QZW7nLAVLmiWN8nzoH0swupYu7pI_jDhLS3cJ4MbbmTGBDydyphEy0fHqQBiAxjiNldZP4dwdgOSxpScSs_CQLCKaoJwiycuNh6gP03lz5ddVpmNlv24FhHgQLN-sf7P7dkxZjKhZwSZNGyQzNfme9E1xja6BQXZCRukopVo4q8y1hI2AGzieM2eQU2of9ytTvDO2QkWGpDGV3VpuQRBFh2S1GIm216ufIrYqvdj0bEI2q0AkVyjtWSj5xbk9ggiyl70WYrlt2JUOBhbwcqXUDqRw3GRmjgEeiH2TXqOzq84hU9C5Xh2gMu3YIAJJznp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
این افتخار همچنان ادامه دارد
@Farsna</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/466699" target="_blank">📅 20:40 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466698">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spAjt9BlpIeFxJTR31KqcT-J_EFlCqXlwO-dfAt4rPA0UGh_1DXXf9Bu0SideRcnE7cA_6OgbAZ4Ixh1vIYi1Lyf7PFngifl-IwOMKBErHNbTY7FhGh87JDHoe_T_fzGvoNmkhZOwBXpo4MtMb5YUNedMh2yZZxaEducc_S7E3fF1NXHyMjmhOgvGg8Y80PrD1AsiaSsV35E6KLt-Rjsc_S4aGy0FdIYA15wWC7CdqQQpFZWjOVDEwWipf_LJ-wSg5KpGnKQA4jXMABJDHD7WYLS9RxJXoaObhcWy29gmvw8cEDCRQ4PESMP-ng5VZD3EsKdR_y-eWz4UEOHhKk_BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتین با پزشکیان دیدار می‌کند
🔹
دستیار رئیس‌جمهور روسیه: ولادیمیر پوتین در جریان سفر خود به ترکمنستان در ۹ اکتبر با رئیس‌جمهور ایران، دیدار خواهد کرد.
@Farsna</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/farsna/466698" target="_blank">📅 20:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466696">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hqvM-pwaVztfYCDoGz5Yl2X4537jvvW9jBkkP0euKbCiNoNuVlNW6hN3etjlww2oeaIAdfRhciPS5AtNtfbjof787DF0_cF2sv0yqA6GICqK-H3-oXaU3HdwSS_cs0P0sER8yTH2TP49978zI15xHIwnu98QhXgkvqup3wgKbTcyMcr2NQ3_WCr3e0it9_UAgYdnsq7Zi5o-owcM3ea0oCGA1pNggkTynVZetoz-nfe7YfvuH0SjNbENehwcSdP5HzkSZ5Q21ZjX5mPl-Qr5NETcJ9W_7ztyoc0MbmScu0h9zQ0mY3uq_1YXbdIW5PD4Jujbc2YUZX9znSD8CEcEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهدید دبیر در مورد ویزای آمریکا کارساز شد
همه ویزا گرفتند
🔹
فدراسیون کشتی اعلام کرد که آمریکا ویزای ۳۷ نفر از کشتی‌گیران مربیان، داوران، فیزیوتراپ، ماساژور و همراهان را برای حضور تیم ملی امید در مسابقات جهانی کشتی آزاد و فرنگی امیدهای جهان صادر کرده.
🎙
پیش‌تر دبیر، رئیس فدراسیون گفته بود:
اگر حتی یک نفر از اعضای تیم، به‌ویژه کشتی‌گیران، ویزا نداشته باشد، قطعاً تیم را اعزام نمی‌کنیم.
🔹
به جز کمک مربی که مدارکش ناقص بود، ویزای همه صادر شده است. اعلام شده آمریکا تلاش می‌کند تا ۴۸ ساعت آینده ویزای این کمک مربی را هم صادر کند.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/466696" target="_blank">📅 20:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466695">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">‌
🔴
سخنگوی نیروهای مسلح یمن: چند نقطۀ تجمع نیروهای دشمن سعودی با موشک‌های بالستیک منهدم شده و شماری از مزدوران در این حملات به هلاکت رسیده و یا زخمی شدند.
🔹
در الوازعیه نیز پیش‌روی دشمن ناکام ماند و تلفات چشمگیری به تجهیزات زرهی و نیروهای مزدور سعودی تحمیل…</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/farsna/466695" target="_blank">📅 20:19 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466692">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cEglamYnT0n-DvcbbGm7hhkG7HOSQycPER2-xu7v1UQ0B3MXbTkiHO4wAbqEsV71oBYzM1arBwheSWAkODDTvA0UuKVXgzHZEqEGTHLyY8lrrjvuiaryJkHdMzlubvf5nHQ_lBoZtAJQ-qs0678RsgoT83f0CFya1ilkA9_5rIZpbCiZJGbf8hAMmwiHfXpZ9eKpcS0_FkKKkIREDtAtiKArugfeBJjc0RLNDjJCc2Eh-pXZh65S2d3qIdo-N7JC2myuk1A85HRvxDeRGknfKb6jm9M1yZPWUGrXhN2KYKB5rkr8o64gIl60TVt5IvTgcYDDAtOacZ8x6og3qjERJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراق «وِیز» را ممنوع می‌کند
🔹
وزیر ارتباطات عراق از تصمیم این کشور برای ممنوعیت استفاده از اپلیکیشن مسیریابی ویز Waze از ابتدای سال ۲۰۲۷ خبر داد.
🔹
تصمیمی که بغداد دلیل آن را ارتباط این اپلیکیشن با رژیم صهیونیستی عنوان کرده و هم‌زمان از وجود جایگزین‌هایی مانند گوگل‌مپ و یک اپلیکیشن مسیریابی عراقی خبر داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/466692" target="_blank">📅 20:14 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466691">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhkXHC5z4vZwtUjljahD8iugEZ-Uym7VWgfdednmGfI4w936_34uWIej_fXNd-6uI-VDjnQ0HIoZCk5_NUdDx14RB4MeY5rvSMIha3-7_Wv7jCGxx5Wbq1lpznA67ps8qvof3IGPKOMO-SZHyf_JYmppHK3wd1tJES0sa098TMFM4jeqGJW5niuViRK1lGKZK2QjAdhY94HhFoMFlLYZFPBKirqsS-ygngF7wPhEyy3QxVr-Ob5_2IF1FSDuSlIpiGnbWGPU-vwXfYsghqdGuvz5Q5OFKSfoWQ26j1imPe2wBOIesJbDZX4iDmngUYzSZGQ-3CeNe6GZYi2-_129ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رایتل به فروش گذاشته شد
🔹
شرکت سرمایه‌گذاری تأمین اجتماعی با انتشار فراخوان مزایده، از واگذاری ۱۰۰ درصد سهام رایتل خبر داد. قیمت پایه ۱۳۰ هزار میلیارد تومان اعلام شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/466691" target="_blank">📅 20:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466690">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">‌  عضو دفتر سیاسی انصارالله یمن: توانایی بستن تمام فرودگاه‌ها و بنادر عربستان سعودی را داریم
🔹
البخیتی: عربستان نمی‌تواند با گسترش دامنۀ جنگ و ورود سایر کشورها به جایی برسد و ما آماده‌ایم با هر دشمنی مواجه شویم.
🔹
جنگ علیه یمن هزینه‌های بسیار سنگینی خواهد…</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/466690" target="_blank">📅 20:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466689">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">البخیتی، عضو دفتر سیاسی انصارالله یمن: زمانی که سعودی اخبار پیشروی در تعز را منتشر می‌کرد مزدورانش در محاصرۀ نیروهای مسلح یمن قرار داشتند.  @Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/466689" target="_blank">📅 19:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466688">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUtthH6BUIWphrwzJ1M1AhiFDOfPcW6042_4ZEpaP761rFmzX0tW-q2aRXaOIsWG4ZFhbX3T_U3KX6j043WYupdjzqZw6y0yMKROPgA1GQrwu5VadgvdtzuP7GfpABY_3E0JXOP9ngJBLSHS7N0KmJBcVNWUKlrIMGDmfXIdkQLM3oGTOpIeyZ1V6Pm4cAzM79YVLB4IaVouADNMp4IV4_pqShM5notrpuXQTq5QTRxkqtBAzMYoC5hjWPT-vyBuAI7XpRayYFJJfD64MhvJKTqjb90pbqkspNM4Oulu9zG7q19BiZj2DYc0gSmVc9ebIkZ2d3Ls_n9iFYXfKRlB1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقام ارشد انصارالله: تعز عملاً آزاد شده است
🔹
عضو دفتر سیاسی انصارالله، با تأیید محاصره کامل تعز پس از آزادسازی مناطق اطراف، این شهر را عملاً آزادشده خواند و تاکید کرد که این پیروزی با مشارکت نیروهای بومی استان و حمایت مردمی به دست آمده است.
🔹
حزام الاسد در…</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/farsna/466688" target="_blank">📅 19:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466687">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7295eb324d.mp4?token=HLl_yDFf8PxvNcqX7JDrpOJAHm9NP1RtE9_zGO9926LwKLNoexxaDTv4oEEqECFlRZwLlMyND36kZiQk9sHDwVTeMvRlS7g5JSPslmikuqqQhDrIhp_gHR9XY3PV4Ajqv70yhliSh_71RU_F_HtKIDOIQLPqgyhJ2IgPtkcLRWo1PaucdVEc5yO_iZnGRszEC8RY4A6imyCFl3_7AC422r_5FibaPboNrgb20dOQzDs9Kvx1v3ok0oZHA-PK8Zz1Y3dWuJd4W1Nm-BRxXIVzNtkej6b403uLyOHJCz2cZN2DIbDmGJ7iYZP80A6S5LSwviptbk3DPuL5MUaFBJVIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7295eb324d.mp4?token=HLl_yDFf8PxvNcqX7JDrpOJAHm9NP1RtE9_zGO9926LwKLNoexxaDTv4oEEqECFlRZwLlMyND36kZiQk9sHDwVTeMvRlS7g5JSPslmikuqqQhDrIhp_gHR9XY3PV4Ajqv70yhliSh_71RU_F_HtKIDOIQLPqgyhJ2IgPtkcLRWo1PaucdVEc5yO_iZnGRszEC8RY4A6imyCFl3_7AC422r_5FibaPboNrgb20dOQzDs9Kvx1v3ok0oZHA-PK8Zz1Y3dWuJd4W1Nm-BRxXIVzNtkej6b403uLyOHJCz2cZN2DIbDmGJ7iYZP80A6S5LSwviptbk3DPuL5MUaFBJVIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رتبۀ ۷ کنکور انسانی ۱۴۰۵: از دفتر رهبر انقلاب تماس گرفتند و مرا مورد لطف و تفقد قرار دادند
🔹
گفته بودم موفقیت خود را به رهبر شهید تقدیم می‌کنم و ادامۀ‌ راه ایشان و شهدا را وظیفه خود می‌دانم.
@Farsna</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/466687" target="_blank">📅 19:42 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466686">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db3a347327.mp4?token=qMumuZV8E2BYSbFboXut4GA2ePj9bhx8dWCgUmR0q1ZD6aIpwUZM-TDehnCK-A67tkHHOyMSwN85tK4lcWEuHthVQhe89jo9m5aI9uSSA6cUJUUfbQRMZui4lY7j90qTSnPgafmDQCXb-70sQVKJGRzghcWEHr7vPHVqJ3JOG8jTxQUK5ijK6e-dcNCSgBxq9rU4u_BwIUN5KadS_pocDQl2jJZWfsUDUaCniCstCZ8LGlylfFJ4z_vU0-pWsx2L5JcvQtqYQBvlKD9i-U-cnlQEEpGIQL8YeiiJhUDmRYo8gJ1pmETHbgSrzcFOnaIv0x52fKF1pBbN6OwR_5qxwbPfsnVpMCJJK9vHjkD5GhwPJ71c322xSALCF2T78Gf4S2EvlgcZOpDpyh0dNgd6I-EL2eeeXq2R_gmWOjKzrdJokzRDwi_Wue-PhxXEzPwZ5hqa9osPU6CPTf1x_mA3Sc2UuOke9C5GkBMemkKni3qHVbazy2I9qYf9zhdG1bUI0s4Xx5c9myLtyOGC3IPcHr9UxPZYfifYY-58AZ3vT9e1x0YaLUjM10_v1KvLLGLvS5hjjdFNC2WoNe2kXXIbaJZ9epAwlL0_UHarMtpRuO5LMnO_gjdhsKFPz_BEuE7WPEWBSghBjV6YFAdliB0aeizDAe8A2MP8ZGwjLgc2Kv8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db3a347327.mp4?token=qMumuZV8E2BYSbFboXut4GA2ePj9bhx8dWCgUmR0q1ZD6aIpwUZM-TDehnCK-A67tkHHOyMSwN85tK4lcWEuHthVQhe89jo9m5aI9uSSA6cUJUUfbQRMZui4lY7j90qTSnPgafmDQCXb-70sQVKJGRzghcWEHr7vPHVqJ3JOG8jTxQUK5ijK6e-dcNCSgBxq9rU4u_BwIUN5KadS_pocDQl2jJZWfsUDUaCniCstCZ8LGlylfFJ4z_vU0-pWsx2L5JcvQtqYQBvlKD9i-U-cnlQEEpGIQL8YeiiJhUDmRYo8gJ1pmETHbgSrzcFOnaIv0x52fKF1pBbN6OwR_5qxwbPfsnVpMCJJK9vHjkD5GhwPJ71c322xSALCF2T78Gf4S2EvlgcZOpDpyh0dNgd6I-EL2eeeXq2R_gmWOjKzrdJokzRDwi_Wue-PhxXEzPwZ5hqa9osPU6CPTf1x_mA3Sc2UuOke9C5GkBMemkKni3qHVbazy2I9qYf9zhdG1bUI0s4Xx5c9myLtyOGC3IPcHr9UxPZYfifYY-58AZ3vT9e1x0YaLUjM10_v1KvLLGLvS5hjjdFNC2WoNe2kXXIbaJZ9epAwlL0_UHarMtpRuO5LMnO_gjdhsKFPz_BEuE7WPEWBSghBjV6YFAdliB0aeizDAe8A2MP8ZGwjLgc2Kv8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یمن: عملیات زمینی برای سعودی‌ها خودکشی است
🔹
سرتیپ «عابد الثور» مشاور وزارت دفاع یمن هشدار داد هرگونه عملیات زمینی برای عربستان سعودی، خودکشی خواهد بود.
🔹
وی با بیان اینکه کنترل تعز به معنای سقوط آخرین برگ برندهٔ مزدوران است، گفت: حالا عملیات خارج از خاک یمن…</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/farsna/466686" target="_blank">📅 19:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466685">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA78EOOUFU90va5Y5EVfvrTBIIkwqrBWr3ywXy68TYgyI2qNZznzdIuCL47PCI_Ay3VJU7L-C-bambVyT8q0F8pqFTjoqdmRcUWPlVP_bXhjjTBNtp8oQjzc5w033S6OANSmRz5I33cRLM4iuj4dYKldMNhGFn1kAyUR737HV2NqKt6QhouNRzm6sKUFBLtrPvJ32KmrMJKYK9NVhmLwgXGHS4W9QET5hdZ30dui_JjGoCnU7y9sO1cE8FmLeAyE0y2gONjKxXEV_cobTbpp8LZDrFCFP-GeOND5_6SKD5dR5uOIIeKurjVOsqOzU0RF3VdUmStJ5pTm0JVFpMorvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ احضار سفیر فرانسه به وزارت خارجه ایران
🔹
در پی برخورد خشونت‌آمیز دولت فرانسه با اعتراضات صنفی دانش‌آموزی و موارد نقض‌ فاحش و گستردۀ حقوق بشر، امروز سفیر فرانسه در تهران به وزارت امور خارجه احضار شد.
🔸
اداره کل حقوق بشر وزارت امور خارجه با یادآوری تعهدات…</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/farsna/466685" target="_blank">📅 19:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466684">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q90jt_yvqWucMuWugCnIi4dMvfVU88Wxpv1TMyLBo1KpyZ4FrLdljwaPBEF2pDHe2U5Pybm9JCVFKZkHt93qY2Be1wWc8Ff-9YMXci3aByXbOsTik4Juy8DMrpgKQXjXya87_rd4Jfm4WBPfQYaXozUu8a8VM_H5b46k2W3LJleZsyiScXiNGQucdzI1tVlXHfwKl1TIt0NFflfxQDvApq-xgdr2rmcKHD4uniYDTPHQ6IF3zjFHudjPKpA8lVZ6uW7MLFUPcoSQR6tkqyCTaejdGl2HYFesl_CVhVuXYxnHphNDJ61g1P0RsmoQQCgCtsMaAeTBABo2TvFcT-zLDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نایب‌رئیس کمیسیون اصل ۹۰: باید در بانک مرکزی معاونت مقابله با جنگ ارزی تشکیل شود
🔹
حاجی‌دلیگانی: باید در بانک مرکزی معاونتی مستقل برای مقابله با جنگ ارزی ایجاد شود تا تمام تمرکز آن بر خنثی‌سازی اقدامات و فشارهای ارزی دشمن باشد.
🔹
وقتی مقامات آمریکایی از امکان کاهش قابل توجه ارزش پول ملی ایران سخن می‌گویند، باید در داخل کشور نیز یک مجموعۀ مشخص و پاسخگو برای مقابله با این اقدامات وجود داشته باشد.
🔹
دربارۀ وضعیت موجود در بازار ارز، این دیدگاه وجود دارد که نحوۀ فروش و مبادلۀ ارز در چنین بازاری با اشکالات جدی قانونی مواجه است و آنچه تحت عنوان ارز آزاد در این بازار معامله می‌شود، نیازمند بررسی دقیق از منظر قوانین مربوط به قاچاق ارز است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/farsna/466684" target="_blank">📅 19:31 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466683">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhmbkLd5u23K5UwY_oOhh3j6cQV_Co6jMojJZ2IydxGEYBJ3BfyEBM26EtWUTJLYqdSVnLyyxF8C7QtulsV8ndgi2scbKX1tiOb7i8AXW6wPvEXXZ4Qrs73BCbUZZNrKshMR_9WkkHS6g-vDZ-lzGQnesjd8lbKdVusEuk-rBM0LPuPRdUesQ-xEmiPT3HUDdSeFYASOIw_XNQn5Zc9woP1Ia53PyrjmeVhiys7w_hUPYsMNN57L3o6N8hlSJgRCZwWRwg9uogvoNGE12BHgiIWBI0OBgxRaXu7PZkbVj09T-DBcqdeWClNwgBW94ayLh1KvUtXUHK80oTJLRjoLgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرماندار کالیفرنیا: ترامپ دیوانه و خطرناک است
🔹
فرماندار کالیفرنیا در واکنش به اظهارات اخیر دونالد ترامپ، او را «دیوانه و خطرناک» خواند و گفت رئیس‌جمهور پس از فرستادن گارد ملی و تفنگداران دریایی برای اشغال کالیفرنیا، اکنون خواستار هدف قرار گرفتن لس‌آنجلس و سن‌دیگو توسط دشمنان خارجی شده است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/466683" target="_blank">📅 19:26 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466682">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
مزدوران سعودی در راس‌العاره توسط موشک‌های یمن صید شدند  @Farsna</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/farsna/466682" target="_blank">📅 19:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466675">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhaAsVRMWecmo1tuX7m3VUCei2i7RKA9ipMHR9wT8gMk6ozeajl9aR0mjeah39c9TuNdAOd5myr4xe1SaBSjj8Esi8Q2Slvk_cM7cUA40etnlhYp3RSIBhP3jyCBxB4yMNJn_3_Xe3tx39FCrw-la_JbTUQYIX7OTsLqm_eF8C74JsDefTh-zt3o5CETF2iMglk8kSjX65v8Gt5FWHd5TFTH84LcG5ICuKopwEMO7QuS_dLCMkh2ebOw35gHemTTQNtPOkpLHRBcYNvgraLSooIp3odikN620gmIFuds1DLpQgVjzdUDwKduDPX2VyYYn2LlpkcKG80eKnUEltwhpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FyG6uSB8u9Li265pHQoT38TsAMZ6Xyh4YpcoK_mudkd51puwXvuNkCj2f2jxq_B1ug0RgUw8Cus4-XuB61W1WZIi4UtmfzKhzp1CvWNJ3L43OolfyptJat4ywnuhqsnAWyJH5YzBNKErfftuG6RZ0mzMRp0v5G2wD5_4Y8-ZD4TrplJ3PDd9ir9eTE28NmGjCUWVsxIl85lhSNLN0YsKPFo5ZI-2VZwKMtvUU22pvDSKF79wXWN64xdxeVODMcam7TODamUzNtsWBeIxhG8oVSrHQhS6FunLGCp6aTxKuUknAw4eehjm968CNud58eA62B6HFPdsCIDHoEnJ3CCEsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZLM8L0KS2AdPwtYz4ku4qKgCjTUgTl8sdEzQD1dLGblNv6-zqn45Dk58KOHCGarVQdnezd7cB7XxTqx8Ye3SYZAIRYP0u2fPvuM-QBgqzzphwjlPYr5HX3MU1EGnzLf8eLL0hD2BZKrBE2VWbhPFqPXBLDWt6QdpOmtg33tIRUsYoOjfuPflnQFqhR1LvL0XgKXb6SKnvibZnUQO4Aa4IN8w1Ge8cKFJHaj2WTe9ihzBiBUojVHtmGU8w_jx-0qQMwm85pkjcUbOE-RgP7mgLtczYthQckJPBN6mTwYA2-jW_FI--JTTsdFJlQzbl_vbrhiePyuibXFlQNHGosxO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hEpktdd6h6XQiGT9Qb5UNaN9UNfC2xVZ95x-kHJ2muTXS7dxxGcXRO2cz4mGRuAJWZYnCgoJ90sFR_5eft1BawAPJOHaB4U6_GvOdqCGKqtN4PI8NumkIKdJIpCmzbnRktTaZT99CN6Bnb9wA05sY3xyEQwL_7ggSCSlF78721UF8q8EG9eTnw4BfrVIqMGt_j6K-m_Sm_7XQ-nYNhgN0ctOJZ6Lw176Vf-37vJFtm_LPxaYw_Cp8xVJP9Ibrf0DROPJVkgQHTFboxUKIPrub5MfS_ppv4EP1iA_zYdmPiiwNXkFK_Ron7Rhi-IOlwQYuzjoT8SwD03zcyAdb7atQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLFW8z8WurkYXXNQtQnySUjy23v8rHOKgjLHvpCO_bvs7NOWCgb8LlMJbn6QjDBcds-1SO54GJJrFOCDO8D5vQiYHrP2tJv9vaKXmsg2RQxv80yei-X6qaJ1hkPD1pj61cmeXQDOBPnERFhd7u3WYLFD3CcjkYzCEOWYIUJ1_oUPzC0spR3ZciBcto4va5OZUhPl9g0yjfG_02nhTKbaMuOE3CgGof1kW05S9rdKTGlBxhg4hafGhAvdfUPCt1lroQ0t3EkeP0uqHpOtkRQD2YKMskuTutXsgH6Kd64wj7G9_K5Nwkvfq8OzxIkeheXMEnYz3sljr6jyiEY5ATlDPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Clc0iIqXEXH9duMyXHQSBAjxy-MxUDovzwAXrreX5_HAzlHTuF_1qM2lyJ_iLGCvpGh1jjlv5X0v9m3OKEYr2IOyYAZoBsC4diyVjO71WEffNEH9-9HgGv_T1knNXSGfpTblB_sQJH-mR6buvVB9W6h7RN0TurCCWLA3uQy69xSEpuaddQ8-GDb3sUgZf3S4scoTahR5PaDQCouuZjkw8QhmgHoxCb6mc5WqGo-89I3u_shHEXWz9xoJLeYZk4IeMGC2AmpegaWG96He6BAFSRIIOgFB_zLEmypycwMaoPv5Tx41UBRoXPlDl6QDLWRgsWZYpKPofI21bcSxBRU-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQTroVewvnhv--VX_NzT4PfQz004Bzxa_rwruPxiPX71Yb4yXQpMALdnUNYg0kqwOxASaJ9fHHuT7RmPwM1kXgxK2j7NGux_48qawuDfikN3mqgyTiMaIS0g_4Xv7JXoHbqG_d_jvWmeEz0QuL4fm4tkYkWB4FeqAsbS7x3GQlwNgJX8axT91P6f5HpPSZf7cALWVZXY3ylWlXjKInXxIoZ60UwmkQ2HLUz5DykrlXgHvCWEXqnWcWO6kQsfIJg7vkSNWsWinsuW8SUAwbP5bmWiuoppaAtJLXpVL2SassETYqJBxwZL5LLcGUtON9auvJ5fvpY30_2XQkzH-qJdmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازدید رئیس انستیتو پاستور ایران از خبرگزاری فارس
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/466675" target="_blank">📅 19:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466674">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVtD_1ky2MDB2HUTDT0AwXBr4Wz9DvIHGBYQMh9dzmmWW5ePPrJQCY5MRNmO3djxFpEyb0xySCUyznb9-pxpB2MidX0XoCf6r0Oq12SzzztgGlA6GBLMp97YaMif9Rj1hlLSqMuQZM7sa5ZG_Nxxw00m-0aezpV0Vic_8yESRg41rq63ScRs_nCeZgxJg_NgQHXu7yns2EJNYnSfLKQ6GX-ZAZHxVMXibgISOS_k2X5FYKWZjymrXueyI9kLazDkJJznzJ4rymlYLxe38bHOaZEsSByvtvgXjFQLr9eeGPl9VtgR3hA93SSIpnd-e-aNQ40p5y_d817NdE8Iv32ORA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفتکش اماراتی برگشت خورد؛ اسکورت آمریکا کارساز نشد
🔹
منابع اوسینت امروز اعلام کردند که امروز نفتکش اماراتی «DRAGON FORTUNE» علی‌رغم اسکورت آمریکا توان عبور از تنگه را پیدا نکرد.
🔹
براساس گزارش‌های میدانی، این کشتی پس از دریافت هشدار، مسیر خود را تغییر داد و سامانه شناسایی خودکار (AIS) آن نیز روشن شد.
🔹
روشن شدن AIS این نفتکش نیز نشانه‌ای از تغییر وضعیت آن از حالت «پنهان‌کاری» به «پیروی از مقررات اعلام‌شده ایران» تلقی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/466674" target="_blank">📅 19:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466673">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2a807b5c7.mp4?token=EYR8g4y0avlRba7zXO_2_CSxrspzhwu2fp8rub5tWTpTYD7mDIl2lIjbPl3dW7-PBRbQ3QTM5xS84rr3nq44WK4QvWWwrziCmk8xTN0UCDYbTwnb7gesnG4KjRcPm9KkPx73alUOtFIYu_oh3KvKjVXCs1aVCrF9D-DcRF19OGQjOoCeZYmgjEPrmVIvJeUYAqMn8I5-HNmdAKi89jhnk65tiB-rxw9qfCU5ut4L3H1emPurOm-WauhY2lZ3OHlbHX8qfiShNaNtAgNoqAHnE5sCbPs4YFmFSIKfsQlZ7DN0B_2l-oaDAvzaxyYtoSEoHGvdoehA6MyD74d8tH5e-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2a807b5c7.mp4?token=EYR8g4y0avlRba7zXO_2_CSxrspzhwu2fp8rub5tWTpTYD7mDIl2lIjbPl3dW7-PBRbQ3QTM5xS84rr3nq44WK4QvWWwrziCmk8xTN0UCDYbTwnb7gesnG4KjRcPm9KkPx73alUOtFIYu_oh3KvKjVXCs1aVCrF9D-DcRF19OGQjOoCeZYmgjEPrmVIvJeUYAqMn8I5-HNmdAKi89jhnk65tiB-rxw9qfCU5ut4L3H1emPurOm-WauhY2lZ3OHlbHX8qfiShNaNtAgNoqAHnE5sCbPs4YFmFSIKfsQlZ7DN0B_2l-oaDAvzaxyYtoSEoHGvdoehA6MyD74d8tH5e-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش باران پاییزی در اردبیل
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/farsna/466673" target="_blank">📅 19:09 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466672">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mdkw-lZ0fuKuvXOrvxNbWs94u_Wjhk3IgXbNp6IgH8blFm7FvO1rHj1NRxjZM9P_izmPsJlPQEgge3IoTK2l4nnmW5vfyw3SmMpgDYUk8B_b-KW0zHOClpXz6bc9gMzLnzkZguUO2PRtdhlSFarYWDmjCm3tUsEb5yg4h-N3vztFfRcOMkgSp0kkjrVrExZQG-b_A5iUc_glQcC_wjJUdZvKiZogqfDsdNfGHO_zrFOQOJMV26OxppKtGomGdXWwWPKh3w0fASFPNXm2xlBll1HmCQrjVitqyRzHgMyQD9Y5sZkRN5SeDqQpHKBS8JUDFL9S2V3Q1kxZWLO3opZs-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
۶۸ بار حمله به یک پایگاه؛ چرا العدید مهم بود؟  @Farsna - Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/466672" target="_blank">📅 19:02 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466671">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGsNKpFHWYb8t76UqY8MrlcBwf2Y-O3BwP7X4ByAUrs_Qf43x3Pf7AFuL6LiB4EfdgOSTFkQeJw8VjJQHvHOBrYoq9X9gmKZtC88cqCp0QP3pM1r0JYY_lAuzrNtLbm8hlFgbnDHMN6r1e6Es4JDOZ9GkgGF4pqmatTHA6e2_NHlS-3jLix90k-XkvTlNGCxyITV4hriS2zBh0pJ5MB0FCVvvMuwA0xx3Fi8FdoAWQhBLA7903wnztc5SQ9Pe4kW4Jt5am84kk9zaJ018t61tt1IqkvFgObd7K4LBGJqHD77uBFSlqTn3NZjt65Luh4NpKpNdYqTKOXsK22S6kIWUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«چوپان دروغ‌گو» تاکتیک نظامی آمریکا در روزهای اخیر منطقه
🔹
در روزهای اخیر، آمریکا در چند نوبت، آماده حمله مجدد به ایران بود. در همین راستا، جنگنده‌ها و سوخت‌رسان‌های آمریکایی در جنوب خلیج‌فارس به پرواز در آمدند. اما حمله یا عملیاتی انجام نشد.
🔹
این ماجرا می‌تواند مشابه آنچه باشد که پیش از انجام عملیات طوفان‌الاقصی در ۷ اکتبر ۲۰۲۳ رخ داد؛ وقتی حماس در چندین مرحله رزمایش‌ها و مانورهایی را به‌طور عمومی انجام می‌داد و اسرائیل از آن‌ها مطلع می‌شد.
🔹
حماس در این رزمایش‌ها حتی تمرینات پاراگلایدر و عبور از حصار مرزی را تمرین کرده بود. تکرار چندین باره این اقدامات، باعث شد که اسرائیل گمان کند صرفاً مانوری بی‌اهمیت و طبق روال عادی است.
🔹
یکی از مانورهای مهم و گسترده حماس، درست یک ماه پیش از ۷ اکتبر انجام شده بود. در ۱۲ سپتامبر، ویدئویی نمایشی منتشر شده که حماس با استفاده از مواد منفجره، ماکت دیوار مرزی رژیم صهیونیستی را منفجر کرده بود.
🔹
درنهایت زمانی که حماس برای عملیات اصلی آماده ‌شد، اسرائیل گمان می‌کرد مانند اقدامات پیشین، صرفاً مانور یا نمایش است؛ این داستان، در میان ایرانیان به قصه «چوپان دروغ‌گو» شناخته می‌شود.
🔹
این‌روزها در منطقه اتفاقات مشابهی رخ می‌دهد؛ به‌عنوان مثال در ۲۵ سپتامبر گزارش‌هایی مبنی بر سطح بالایی از فعالیت نیروی هوایی آمریکا منتشر شده بود که یک مورد آن، هواپیمای شناسایی در نزدیکی جزیره قشم بود. همزمان با آن، فعالیت جنگنده‌ها و پهپادهای آمریکایی نیز گزارش شده بود.
🔹
هرگاه دشمن آماده حمله می‌شود، طبیعتا نیروهای مسلح نیز برای مقابله و پاسخ، آماده می‌شوند. هدف دشمن از روند مذکور این است که باعث فرسایش و عادی انگاری اقدامات گردد و درنهایت زمانی که گمان نمی‌شود، عملیات اصلی انجام شود.
🔸
درنتیجه تهران باید هرباری که دشمن برای حمله از خود آمادگی نشان می‌دهد، برای تقابل آماده باشد. حتی اگر این فرآیند، ده‌ها بار و به‌طور روزانه تکرار شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/farsna/466671" target="_blank">📅 18:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466670">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/okWxYQUxeVHhvPqXqJ_iASGqgMvpXERu85kcDLUb2sRjiZDjHsTV7DG0cSlf28VYW6Dp0H2JXA5s44ptonYCg8wo7cc2k75w98OeK_LuK5T5C7eYB1fRTGLSeZ9cVFez7hB_M07TKJTcGiU4qrDVuPCcp3BgerLiJz05-twisb7DShIB9VBCGSQ7t2kDtkkUqhN0DpVViR2F9TnsX0ZjIA9Yb0WBCRE9Tu2gOKeI9g6jQQB7hPBTVE6vrSWqCP9sFBQ-2LhgpWjEsBZrKRqLXdbo-eNr_2X9Lu-S5Ebm1-jyxjM9KkUc4-URf0EzZqaYbd0ahzrAVN4ImUkkThrWag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاهش دمای تهران از جمعه شب
🔹
هواشناسی: از بعدازظهر چهارشنبه تا روز شنبه ۱۸ مهرماه، افزایش وزش باد در نیمهٔ جنوبی و غربی و مناطق مرکزی استان تهران پیش‌بینی می‌شود.
🔹
در بعضی ساعات افزایش ابر و گاهی بارش پراکنده در نیمهٔ شمالی استان خواهیم داشت و در دامنه‌ها و ارتفاعات نیز احتمال رگبار و رعدوبرق وجود دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/466670" target="_blank">📅 18:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466669">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9vEuZn0LiTmjcW8IhI01rhRuq9b6HzBwK9rhgmmvKsqp4ZAGWa2ObrPw_OhH7vkOduqoTHR6XvA40Zi22hKvuwXIbuuPnAYsNXSSvGyW7yoxO6ogMnZLSwbJFFgsJnOgU2E4rW9ItbAhZYIs9L5ZLYUUgVOL-htQLCZf4Qc9f2ndncnRkh6IzJrpOocATej8FhLIn21DGkL6cbB9AGArAqa2HXoaPHLQuDC9pqnDmXAXpdhjykEy7LbTxi2R4_2EDW5mAqe8UnXlzimyS6FB1N_qN90dwk1_2zAC56mpLsmeO7RJDiAeAAOPTb2UsSYIuaqmGkNf-EIbg1Fe6BiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حذف کالابرگ ۳ دهک، خطای سیاستی در اوج فشار معیشتی
🔹
رحیمی، کارشناس اقتصادی: «حذف کالابرگ سه دهک درآمدی با تکیه بر دهک‌بندی فعلی، ممکن است بخشی از خانوارهای نیازمند حمایت را از این طرح خارج کند.
ایراد دهک‌بندی کنونی چیست؟
🔸
دهک آماری لزوماً نشان‌دهنده درآمد قابل‌تصرف و وضعیت واقعی معیشت نیست.
🔸
داشتن خودرو، ملک یا گردش حساب می‌تواند خانوار را در دهک بالاتر قرار دهد، درحالی‌که درآمد جاری آن برای هزینه‌های زندگی کافی نباشد.
🔸
در مقابل، بخشی از درآمدها و دارایی‌های غیرشفاف ممکن است در پایگاه‌های اطلاعاتی دیده نشود.
چه موضوعات دیگری باید درنظر گرفته شود؟
🔹
قرارگرفتن در دهک ۸ تا ۱۰ لزوماً به معنای ثروتمندبودن نیست.
🔹
هزینه‌های مسکن، اجاره، آموزش، درمان و حمل‌ونقل می‌تواند بخش بزرگی از درآمد خانوار را مصرف کند.
🔹
افزایش اسمی درآمد، در شرایطی‌که هزینه‌های ضروری سریع‌تر رشد کرده‌اند، الزاماً به معنای بهبود رفاه نیست.»
🖼
اما برای بهبود طرح کالابرگ چه راهکاری وجود دارد؟
اینجا
بخوانید
@Farsna</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/466669" target="_blank">📅 18:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466660">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">‌  دبیرکل حزب‌الله لبنان: آماده همکاری برای حل مسائل داخلی لبنان هستیم اما بدون دخالت‌ و دستورات خارجی
🔹
شیخ نعیم قاسم:  راه حل مشکلات لبنان با خروج ذلیلانه اسرائیل و حامی تجاوزات آن در منطقه، یعنی آمریکا آغاز می‌شود. @Farsna</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/farsna/466660" target="_blank">📅 18:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0fjFItsRydmLyKT2M4LA6EUNE4c3kT906xtgV9yuvFz7PND9hd9DFmHju1H4d5S3gyJqLSi3TiV3rIi4_a4H4js32GiSpyvkqt7HbZ8vaHrpmNgNh3GqTzGNifX6iFG1Ox3fj91Yl9-LRgfgYLoc8o7cHSW8rkE9dfK8G2Rky9IwWNZhVcGIYsEnxD3KV-SBPf9oFQtrSEPt-lp0oypZbdcW1XdwFX08QShorG7igQgul8VegFr8gYQj7LGi5L_0-IWyEE6cU7o7cOQ_FrFWLOtBK5dkCicu77OW3BAfwsOJF9PcGkoMUNdrOSabFxW-NvDERcTvUCBERvvqmnk0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحقیق انگلیس درمورد قابلیت جدید اینستاگرام
🔹
رویترز: نهاد تنظیم‌گر ارتباطات انگلیس، موسوم به آفکام، اعلام کرد بررسی رسمی خود درباره متا را آغاز کرده است.
🔹
محور تحقیق این است که آیا متا پیش از عرضه قابلیت «اینتنتس» در ماه مه ۲۰۲۶، ارزیابی کافی از خطرات این قابلیت انجام داده بود یا خیر.
🔹
«اینتنتس» به کاربران اجازه می‌دهد عکس‌ها و ویدئوهایی را مستقیماً در اینستاگرام ثبت و با دوستان و دنبال‌کنندگان خود به اشتراک بگذارند؛
🔹
محتوای ارسال‌شده پس از مشاهده ناپدید می‌شود و امکان گرفتن اسکرین‌شات، بازنشر یا فوروارد آن وجود ندارد.
🔹
آفکام می‌خواهد مشخص کند متا پیش از این تغییر مهم، ارزیابی «مناسب و کافی» درباره خطر انتشار محتوای غیرقانونی و همچنین خطرات احتمالی برای کودکان انجام داده است یا نه.
🔹
در صورت اثبات تخلف، آفکام می‌تواند جریمه‌ای تا سقف ۱۸ میلیون پوند یا ۱۰ درصد درآمد جهانی مشمول مقررات شرکت، هرکدام که بیشتر باشد، اعمال کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/466659" target="_blank">📅 18:15 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‌  دبیرکل حزب‌الله لبنان: آزادی جنوب لبنان را با چشمان خود خواهیم دید و اسرائیل هرگز نمی‌تواند حتی برای مدتی کوتاه در جنوب باقی بماند.
🔹
از ما نپرسید چه خواهید کرد؛ زیرا تا زمانی که این دشمن وجود دارد، راهی جز مقاومت نداریم. @Farsna</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/466658" target="_blank">📅 18:13 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دبیر کل حزب‌الله لبنان: جهاد عاشورایی از اصول فکری شهید سیدحسن نصرالله بود
🔹
شیخ نعیم قاسم در افتتاحیه دفتر حفظ و نشر آثار سیدحسن نصرالله: اگر بخواهیم مقاومت در دوران معاصر را تعریف کنیم، باید بگوییم که نخستین شخصیت مقاومت، سیدحسن نصرالله است؛ زیرا او پایه‌گذار…</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/466657" target="_blank">📅 18:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOQ1VwIdspU5MC9mrgBsEpSlfb5r-VQ9Ez_ql1gvZ8hJ4sChvYAYtIMvMz17pFHAQXIQ2-o1nAJ5l0XqvquB8019rFcd6U74q9WAOaRIK-VEOQAUL-3oGp6Zs6_ztxpogkEUAA1xa8ciWSVZfWpAbkam8yYry0jjid5VD7KVi5I9xXzmQ5v697cCxHnbaHnJ9cOBKCaGdzt27YY6MtLkZU7SxhGEXsOf789y6d0bRapw5v75hMWpJD82mtTminwWzEwoqBougWqcwZgdG5ICchRFgCshkHV4CWE9V5js7XW-RoFeygdBYmmJLtGfeNl_8Dkgf-TVfJbK9YdtDan0Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دبیر کل حزب‌الله لبنان: جهاد عاشورایی از اصول فکری شهید سیدحسن نصرالله بود
🔹
شیخ نعیم قاسم در افتتاحیه دفتر حفظ و نشر آثار سیدحسن نصرالله: اگر بخواهیم مقاومت در دوران معاصر را تعریف کنیم، باید بگوییم که نخستین شخصیت مقاومت، سیدحسن نصرالله است؛ زیرا او پایه‌گذار دفاع و مقاومت بوده و با تمام گروه‌های مقاومت در جهان برای ایجاد وحدت و تعامل همکاری کردند.
@Farsna</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/466656" target="_blank">📅 18:08 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WQR4zsGAUkXeklzdQ2Wj5kD4JzNDQy8ysaE4q5tJI7dW3c5hVUxOc0E0vL2Vf_JRIAp9baXPjgTowtmhx_11k373R1_v_xHAAPL0oDaAier-uhA-tInzNet6EHFTUto1HqILFq6vSvCTyp59l0HoUE-p8TInKiPPLGtvumMoLT3Dy84hXNJcnG0J7M_Q0TF05feC4_sayr-5JuHK7co5LPlUpY6sotMGdH432_3AQsc0WO0818ywA0t0f4l5j0oOhEbr0HSyqRCCH54Cewb7NU8CelWH2rAHZCbbTBRqSsWTJ1DQfBW5WypJ89fTtmefFNfnZACDFCtnJNuz04TBiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعزام هوایی به عتبات آغاز می‌شود
🔹
معاون سازمان حج و زیارت: سفرهای عتبات در مهر بدون وقفه و به‌صورت زمینی ادامه دارد که تاکنون ۲۳ هزار ظرفیت برای سفر عتبات ویژه مهر باز شده که همهٔ آن‌ها زمینی است.
🔹
ماه گذشته اعزام‌ها هم زمینی و هم هوایی بود و حدود ۵۰ هزار ظرفیت پیش‌بینی شد که نزدیک به ۷۰ درصد آن تکمیل شد.
🔹
تا نیمهٔ شهریور نیز حدود ۱۰ هزار نفر با کاروان‌های رسمی راهی عتبات شدند اما در مهر تاکنون ۸ هزار نفر برای سفر تا پایان ماه ثبت‌نام کرده‌اند.
🔹
پروازهای ایران به نجف بعد از ۱۰ روز دوباره شروع شده و پرواز کاروان‌های عتبات هم تا حدود ۱۰ روز آینده راه‌اندازی می‌شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/466655" target="_blank">📅 17:56 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chSoNDrBX11TAJK7d1z4mabNNQTGHLTHWvJGodaXPx_na4CXUwLz_jqREyG-5eteH5RxKTXhSyR8JMlZ8KRpvhCgeBrWt9znd20ajjjJf0pkd-njyxSZW_xU3p88DG2nLyJZ3mDDqdrOnSyypvRwdMiMXuYGEyqT9uKTYqkl4xPVhuCHnw8-fUaF2MXXT1B7TduTWUhjLrAWfaXXBzK5-P9f29zjOzLWqio1aQD-BE7lXzUYL0hsbxaU_Of_MEAnjG46xqVSF3jJtafZaxD_4VOgLeVicC45SD119vxoAj7EKhSw3fLi9X8T7jGTd11dqmN1kXrExxqlpRHs6nmevA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باشگاه نخبگان همراه اول میزبان ستاره‌های علم و ورزش
🔹
همراه اول در قالب برنامه‌های باشگاه نخبگان از جمعی از افتخارآفرینان علمی و ورزشی کشور تقدیر می‌کند.
🔹
اعضای تیم ملی المپیاد نجوم و اخترفیزیک ایران با ۵ مدال طلا و سومین قهرمانی پیاپی جهان، ۳۰ نفر از رتبه‌های برتر و تک‌رقمی کنکور سراسری و مدال‌آوران ایران در بازی‌های آسیایی آیچی–ناگویا ۲۰۲۶ مشمول این طرح هستند.
🎁
هر یک از این نخبگان یک سیم‌کارت دائمی ۰۹۱۲ ، مودم پرسرعت 5G و یک سال اینترنت رایگان دریافت می‌کنند.
🔹
باشگاه نخبگان همراه اول با هدف حمایت از سرمایه‌های انسانی و همراهی با مسیر رشد و موفقیت استعدادهای برتر کشور فعالیت می‌کند.
http://mci.ir/-NYKQCE
@mcinews</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/466654" target="_blank">📅 17:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTechnolife.com | تکنولایف</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0katb6Mo_ioz-cJASe8vg_T0OR6e2JWWTiDmKqel76eGG6upaYTtWdON86L_3MuZcSOJlXDpX4oEE__4IRQY7sbwO3AHDR0ViInZKiQJ2VEJcsuaN8ij0RKGeLMQPC-luz_xKdMElQhxBvQfwv42hEeG6-BIOkAyqTsMzpfNOEqjk5IJHmoHJ8UWRll28UrFp4qdwwg1b3gw_u2qlS1ZG0V3zFwxVCBKcg8eliO1liAwszROcav6C3sM1VGNWCTapXtdCN8_ch339w1qfyJC-CIuwZqxQLUiHc2usMfRkiJu4wbVUfhoL25I2uJ6seZWhjSHSFPoXLgPNIu-jF5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
از
تکنولایف
با
اسنپ‌پی
قسطی بخر، آیفون ۱۸ پرومکس ببر
✅
تا ۲۰ مهر
، از تکنولایف با تخفیف‌های ویژه و قیمت‌های کف بازار خرید کنید و شانس بردن
آیفون ۱۸ پرومکس
رو از دست ندید.
✅
اگر پرداختتون رو از درگاه اسنپ‌پی انجام بدید، هم قسطی و بدون کارمزد خرید کردید، هم شانستون رو برای بردن آیفون ۱۸ پرومکس
۲ برابر
کردید .
http://tchl.ir/scl
http://tchl.ir/scl
http://tchl.ir/scl</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/farsna/466653" target="_blank">📅 17:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/farsna/466652" target="_blank">📅 17:53 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ib6NP4bjk4KmGvr0EawBFqVpwrmid4paj9YpvjKhww3yvFYKGYIHaQuHAxLMQbo33YATaHnZtiyP56J5Dzy-dVr7BZQmkMe7R1BjHvTxH9jEiQitwtaWL87jtqQEMQHkQEtXxGvfW9yiH_GhHh1xKpNrjyGBJjVqE5mS787j9utmeQtFI2ZU3xbljAT_fIx5WT7c-sx67z4SoqumIurYojMb6brUec31TSGpi8DJKZTC2sGY1rEflZ0dVLtSgnOFEoU6zHCXfz7Oj3TJDu16Q7s0_7Ucodxn-elZe3Xuez7Glc4qX4rp3LMNV6skBexkng0amZmwPatubcnn_KDpSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
پلیس فرانسه به جان دانش‌آموزان افتاده است!  @Farsna</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/farsna/466651" target="_blank">📅 17:37 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0321937f38.mp4?token=DA3R7U-P0NCKM0ArKKTdN_34zy3s1BdhEL-Kbpf5wU4EcL4jiFq3VNcxsqFx2kXB30Xh7g1iwzfOncShQmk1jaZv7cIlVqv7XxhtoUPUW-zooDd3pvbSma8HivIObjSLWLT3UqBlweAApm23KpYLgieFnRS20DMYPs39vtQ8XVFmGqZFOLtAP8UTeGhM0_79zmxwvkAyheoRE0bQA3zkuxUZLJ5QDaIymWyj9gkFQ2_NRWUfS9gWgPxLoRkq9S_mlp76WOGV3q4om-5Q1EbdHKcTNeL64_RNbCIl3L6DGqWpFPXJTAvUSjWZPEuy1uBLs00_oEHos4RHFEgODb0Evg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0321937f38.mp4?token=DA3R7U-P0NCKM0ArKKTdN_34zy3s1BdhEL-Kbpf5wU4EcL4jiFq3VNcxsqFx2kXB30Xh7g1iwzfOncShQmk1jaZv7cIlVqv7XxhtoUPUW-zooDd3pvbSma8HivIObjSLWLT3UqBlweAApm23KpYLgieFnRS20DMYPs39vtQ8XVFmGqZFOLtAP8UTeGhM0_79zmxwvkAyheoRE0bQA3zkuxUZLJ5QDaIymWyj9gkFQ2_NRWUfS9gWgPxLoRkq9S_mlp76WOGV3q4om-5Q1EbdHKcTNeL64_RNbCIl3L6DGqWpFPXJTAvUSjWZPEuy1uBLs00_oEHos4RHFEgODb0Evg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون اول رئیس‌جمهور: افزایش رقم کالابرگ همین روزها اجرایی می‌شود
🔹
هنوز سقف نفراتی که بناست کالابرگشان افزایش پیدا کند مشخص نشده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/farsna/466650" target="_blank">📅 17:32 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSnxygi8EpJ02wMHNP-4QpQB2IcAdF5X0Kkq9or2XFx76ue39hTGrnmWk84b9bLCdfuTS7CI_eGqpkvrw6F-rckFN-5rMaDBUqvTtKrEyr9Rv-LpE514U6IjYfYK8dyqwRKRQMt_B2MIH5kFyIWs2pbDZvo64vA0dOdtFixs0iyJ5UVPFbhNiavhu1s7nNrH9TJ7XQjfaZuEWhXyztFlnQeo4kn5qrSABF_EoTu8UT202oxtLMJUT124z_THJeffmfQel2-Xl0d9DKv_EwCO89bhIBQDfSxIwwHSLUsmQmWb5MsPoH4aDvMq3nYDENsTanEjuDCkmyJo2hw9WxAVIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرارت آتش بر فراز بزرگ‌ترین میدان نفتی عربستان
🔹
تصاویر ماهواره‌ای گرمای غیرمعمولی را بالای بزرگ‌ترین میدان نفتی خشکی جهان یعنی میدان «غوار» در جنوب‌غربی دمام نشان می‌دهند.
🔸
در ۲ روز گذشته تأسیسات آرامکو در ریاض و خریص و همچنین پالایشگاه رابغ در نزدیکی جده…</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/farsna/466649" target="_blank">📅 17:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش‌ها از سقوط بالگرد آمریکایی در دریای سرخ
🔹
یک فروند بالگرد «سی‌هاوک MH-60R» متعلق به نیروی دریایی آمریکا در نزدیکی آسمان بندر «ینبع» پیام اضطراری (۷۷۰۰) ارسال کرد.
🔹
اطلاعات راداری، ارتفاع نمایش داده شده برای این بالگرد آمریکایی را صفر متر از سطح دریا…</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/466648" target="_blank">📅 17:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PglajCuZ_gP6qQDU9Z69Amu4lFodAj-P-qJVJR77EyXfaXQBH_SROJ_t9fZP-09t6VKIqoTs_p1mP3e36LOu18bN_ffbmsRAT1J8i82Xkyb2Br51YvGQNPAFkaN67ZXkqfqpxdp3aONMTZU6v2cYe0IZdIGXkalcBQE0cPoa7KQoem95R7parotejKlJS-K8KNVvdvvtMNNURae16_4o9QzWfoxtFlpUPfwAhTGlyiWEFZU_SKLfyQ7asOoXK0-Whd8odeiO4EovBxySTdHAwW0oO_UNJVfzcZ6nag75GMaEV9EaNPJAfGiN8F7CkrNEW7IQTGC2uDFglN3C7ctwug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۶۵۰۰ صندلی پزشکی در آستانۀ حذف
🔹
همزمان با انتخاب رشته داوطلبان کنکور، پیشنهاد کاهش ۶۵۰۰ نفری ظرفیت پذیرش پزشکی در سال ۱۴۰۶ امروز در صحن شورای عالی انقلاب فرهنگی بررسی می‌شود.
🔹
حاجی‌دلیگانی، نایب‌رئیس کمیسیون اصل ۹۰ مجلس می‌گوید: «کاهش ظرفیت پزشکی و دندان‌پزشکی با اهداف برنامه هفتم توسعه و نیاز کشور در حوزه سلامت مغایرت دارد و نباید نیازهای واقعی مردم تحت تأثیر تصمیمات کوتاه‌مدت قرار گیرد.
🔹
تغییرات مکرر مصوبات، اعتماد عمومی را خدشه‌دار می‌کند. تصمیم‌گیری درباره آینده صدها هزار داوطلب کنکور باید براساس مطالعات کارشناسی و نیازسنجی دقیق باشد.
🔹
اگر شورای‌عالی انقلاب فرهنگی با کاهش ظرفیت پزشکی و دندان‌پزشکی همراه شود، مجلس در صورت لزوم برای این حوزه قانون‌گذاری مستقل و بلندمدت خواهد کرد.
🔹
ظرفیت پذیرش باید بر اساس نیاز کشور، جمعیت، پراکندگی پزشکان و وضعیت مناطق محروم تعیین شود و تحت تأثیر منافع صنفی یا لابی‌های خاص قرار نگیرد.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/farsna/466646" target="_blank">📅 17:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ba9921587.mp4?token=Gxt0FfDIMpf2Xrl49ns13T1v-1tKTVDMVFxqrFGvtZGriQJdyEFEtgqrqEU350wyrzhx5E-SE5Xsc13ikcsUYxlZAhvHvQTCkP-H92xesZu3cn5JiQiz5tsKEmgbboP-4CSxPKLa46seUPdS-QzvHSAxGe2eGj3YDEoqSi3LGkwL17gnTUngzO5IbxLGbeh6G042WByIWcuIkosXXbRR8IImRu9RnkujkXKfLRuFkMo2pe0xpOHjb56bH40K2DiEdkXhyucyRMy3G9LP3XOOCa91P35qdmciHbyeQqnaMnJbY8mb_nN35lC6n_YgdZwCnriQ_GGxdTZIUi6NQIeHRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ba9921587.mp4?token=Gxt0FfDIMpf2Xrl49ns13T1v-1tKTVDMVFxqrFGvtZGriQJdyEFEtgqrqEU350wyrzhx5E-SE5Xsc13ikcsUYxlZAhvHvQTCkP-H92xesZu3cn5JiQiz5tsKEmgbboP-4CSxPKLa46seUPdS-QzvHSAxGe2eGj3YDEoqSi3LGkwL17gnTUngzO5IbxLGbeh6G042WByIWcuIkosXXbRR8IImRu9RnkujkXKfLRuFkMo2pe0xpOHjb56bH40K2DiEdkXhyucyRMy3G9LP3XOOCa91P35qdmciHbyeQqnaMnJbY8mb_nN35lC6n_YgdZwCnriQ_GGxdTZIUi6NQIeHRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت رئیس بسیج اساتید از نقشه دشمن برای التهاب‌آفرینی در دانشگاه‌‌ها
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/466645" target="_blank">📅 16:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ماجرای «طاعون» در روسیه چیست؛ آیا باید نگران باشیم؟
🔹
در روزهای اخیر، گزارش‌هایی درباره مرگ یک کارمند آزمایشگاه در منطقه ایرکوتسک روسیه و احتمال ابتلا به طاعون منتشر شده و نگرانی‌هایی درباره احتمال شیوع این بیماری ایجاد کرده است.
🔹
با اینکه اطلاعات قطعی اندک است، گزارش‌های متناقض فراوان‌اند؛ از نام کارمند آزمایشگاه و سن او گرفته تا اینکه آیا اصلاً جان باخته و اگر چنین بوده، علت مرگش چه بوده است.
🔹
با این حال، مقام‌های روسیه اعلام کرده‌اند یکی از کارکنان مؤسسه مبارزه با طاعون در منطقه ایرکوتسک به «ذات‌الریه با منشأ نامشخص» مبتلا شده است.
🔹
باکتری عامل طاعون معمولاً در جمعیت جوندگان وحشی زندگی می‌کند. انتقال اصلی این بیماری به انسان از طریق گزیدگی است.
🔹
باتوجه به اینکه این خبر در کشور ما باعث نگرانی شده، مرکز مدیریت بیماری‌های واگیر وزارت بهداشت ایران نیز اعلام کرده که هیچ اطلاعیه یا گزارش رسمی از سوی سازمان جهانی بهداشت دربارۀ شیوع طاعون در روسیه دریافت نکرده و فعلاً نمی‌تواند صحت خبر یا میزان خطر احتمالی آن را تأیید کند.
🔹
در روسیه نیز «سازمان نظارت بر رفاه انسانی روسیه» اعلام کرده وضعیت بهداشتی و اپیدمیولوژیک منطقه پایدار است و مردم باید به اطلاعیه‌های رسمی توجه کنند، نه شایعات.
🔹
نادی اونیشچنکو، یک متخصص بیماری‌های واگیردار روس نیز احتمال ابتلای فرد جان‌باخته به طاعون را بعید دانسته و گفته است طاعون یک عفونت باکتریایی است که با آنتی‌بیوتیک قابل درمان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/farsna/466644" target="_blank">📅 16:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466637">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F2Xb-fkTFQ4ZR1DIIaMbr4OQgbJ1O3m6ovJxmz_fTEIAtMpjg0A16MzJyUVyQ7_3ew9uf5BphkWlmCaHMZcHFMHvWYZWTx7oCOhCIoYgWQYapuOwZFaaQXJYq3nAQdopnFatZiGeFb16FfWcA1Xe80DzjK-8ZWgtuKreooC_roiJPXzNdZ2kaUolWQGQR_htdBzByVwfY7Ouw-PnaqZHz0bT5yXo87qux_AIVOEaov6rq0bJr-A9Xp7O7GIwUAylg9TNptEhS-i3moCEjnX7JsaP-MmZ4a_bA3W7zu3Z33yBJV4BKkFmKGioe4Wl9wWoHP-ilvalL-ZOQC1xzEzPkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aLVDSVZQ3pUS59W1C5FPyl7eQRoY4pzsVJgGnKT0MwlmuHzPffAqwUqFpcv4qRbUwbvlFiQNgivCyE15ZbTNQZIHS8byf3Paoz8DmWR9CaxMPekAaMU4MAbESQEHBR4EnaVQ8mvNWRFHK5pooHHTpY3ICftqgKZV90eTqd1Yq3bLGLKKnjlsuvkbCmgX4tKE0wgAWCmX41-H_MkwKGhMj7-cJXT0E5oiOcd4xS4L8w2XA0UAXcnhxazfiGoDfKuE3cMeTEqFh8OP3nhmFFHZsdUrpxIeCNLt_UV9sw0SMFPq48ALhdeC35il2LYOVAFR046FxQUftlISXV8Qp-NkPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Na1UHo6AwEWqa8THCDgSqnxJY18iVex5csi9wB0aEu6c-rgo02nSkTRZOsKpnPKrPIKnC-TmozD1UvyImnor8Q2tPz-ROqWZP1akYE3XLEZX158WF8-ppW885bLTWYDVkDr-M3kuLS6FSbkzsjHVqQz-xt9JVdsk-rJ3lPQkvKifsRw2a7b1SHDbeJuLlhkS8jYGFq8wrNdK5VHd-suIOG3lL0SIsGlKtvSnzz1a4Qncdr8YTOWkk0939ZRLbbKtNdUkBP4qShjQVdZ6CHH1ovmCxnemGsfkz4tjERZiTYwJX3MwRd2a9aUyjUcrWHX4ttTFivQYIge180xYyS_Eow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G0zJaUFIkUKO_B-s1YZ9THvPxHRAU5SrZf_E7JNKr7l1zyVD5XBiyTi4b3oNZdj02ZFQf-wfHtzW7M7uXPzSOoRf-QYMElBtKWmGkYINvgNRRlrmJ0l4NxykMbN-8sh_65iGTYJK3cijE_hhrNKwt5vUDrzhfnBJInHvLsg5nhO9xMlxRzxBM6NwqFmWfLSWn-I_gdwKBtfBEwXt9cJVz2HsmY5PsS1X_aMKyiUjN8On1A8IdmgDZccVS3VEEyqC8bJEFOFgQCve-52_UVsfPvUuoJdIFc0hdbZChpJ2LEoxjSJNQjKAibYCv37Qcu7lERNI1Zxb9X8-i-XcQXsevQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_kQTGM_7cWO8Dse37s6Xltv5I7seIrOPsSFKhOsxFvCqM9PVQYLq35X31n3JfnXAoKccPiZfh5aYzVI5xzZs0CMSdUK_b_PA_Eda6ViGqiXrGUCxEkHTB8JGgZWduyIe3C3BVSKSfErdcMTMJMX3EFivTBNWZEL4KB95NG0NbdUrInqusrhSBrOGaNQwZsEVQaipAyIDSavn95V7UKAWTLNYeVTwCBNEW30IFPYHuJr4bQDZ-NCP85IxQjhCOAOp9mN_-apxdvLMZ-gbzLz_gD3Xd0V0GrjYEuOVar4O8QDccCR3Ykj1jrr9LjmicobNVoQ8WFxu4LQ0WIz9wGp7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PQ0a4EUYUQgRXSvs2errTbsQDDCyfpC3apmA0Dyry5r2Yw2zQjXg2ybVDxp26MfhM0yuNKCMaBHkTl-ZR6FIfU_iKXjs1gGwaTd4aY1zVXH_cK7FVfJkQyjRqslvug6zP_4fKbc7n5fyDXb_ss0VO0fEVFFJ8FrSXeY6uIaGfVsbUZ2agchDRfV0vxwgk2sRlGXrydabUwO_dB7uIasVWjdQHkzUNADTwEn39ZJj66IxiTfPPcRj8UwqnghsSeWUBXTVTLm7COwqMnrJxcgtTegxoqLjGyYukMtSWjeG9lQ2UJ09TMNxG9HN-vTR76-vegVkoIsO3WCqAy25UDKx6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aWXqQOR5Lau3kse1IMKxEBgYBaI9cIZIX7goIcHkx1s_wOLA9W0OlABf78MjlN3OKNQXpiJun-Nt338mdilAcWcPLnxpWHtc2ZH8BluhHpASMhTfeh152RI2xtN6SOqafZgP17l0vKD4EXKUe7IGk4rLAxAp3XdrSjpizb79fJr75MQ-9i9JmUg98qT05aWbz2Bvji13W0khqgNSVU4Z3iYnjDHIGCK173KD7w5BtPq4XJQf-0kX2d3VhBZZcP2TXdLliJDkEjuEO9RiF0FgetE5GSx7FUKEPI4e18hwnugv5lHAgBSCltSKV-nLzC9GmJ9qVFIU__rWhXSa5B9cXw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
رزمایش جان‌فدایان ایران در خراسان‌شمالی
عکس:
رضا خبازان
@Farsna</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/farsna/466637" target="_blank">📅 16:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466636">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY-V2i3ukNKvmkWzpiGjx6yANVlhunYRGaOI85yVtq-cYWOZMIzDO8VUwZIaLEaaqSX2DJ2RtH5kPf8XOYUTNuWn7kfKpV6CsyhaCeYHfN9RWUlxmZGUn76vFy8c4pBbj8UcsCprKYJCrkWhDwj0R-B65eJAHNXMuhEhzzlocHd_qPXx2Q8-bHBNy5RMVo6l8JA3saNLxs1CBjOv6pXSyr3Y3sMbzVdTLzRcwVMnwaIcRZUbquDkEOJpmosWKOmMLzdU163RCJ_RUEYsCs209wpeJ-FzPA7lTf3m4A8sh7AjVVtlqs5n7okHC25SHjlr5qC13nrlAm0ZwtF4Z998zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت سعودی به جای دریا دل به بیابان می‌زند
🔹
ناامن شدن مسیرهای دریایی و حملات به زیرساخت‌های نفتی، آرامکو را به بررسی انتقال زمینی نفت عربستان به عمان و صادرات آن از ساحل دریای عرب سوق داده است.
🔹
عربستان درحال حاضر برای صادرات نفت خود به ۲ مسیر اصلی یعنی تنگهٔ هرمز و دریای سرخ وابسته است.
🔹
هر ۲ مسیر در سال‌های اخیر با افزایش تنش‌های امنیتی روبه‌رو شده‌اند و حملات نیروهای یمنی نیز هزینه و ریسک عبور نفتکش‌ها را برای عربستان افزایش داده است.
🔹
به‌همین دلیل، ریاض به دنبال گزینه‌هایی است که نفت را پیش از رسیدن به مسیرهای دریایی پرریسک، از طریق خاک عربستان به نقطه‌ای امن‌تر منتقل کند.
🔹
عربستان می‌خواهد بخشی از نفت خود را از شرق کشور به‌صورت زمینی به یک خروجی جدید در ساحل دریای عرب برساند و از آنجا راهی بازارهای آسیایی کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/farsna/466636" target="_blank">📅 16:25 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466635">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyq5rkWoqunuIsFfGdolQMOGYjKVZThSj539FNAEN13ocrRMQPCQOqo7qSo7bSon55UCQg8OqYs7btQVZyWwuiSZXACnISPOITJMdOTEOeuM0bKdylYjJUx-nebDLhKu5BGQkYI_NAaTUKELjNH8sh-N4LO6aW-sLpMiVfvU6bpuPfddYXm5LYHP5SWRWWF4wIUkSI3lw8SKx00x1dkr1ht0GIaUO15-BfsqwCq3YH4qsOIUN7Bm-mw756E9X_AHpjSBROQlVkV8SpLD-WjBuZUgjD78Z40tHzmLiKuhJ3Z08SRtYEMDkce3b9z-3t7KqH1u71xUQd6fJVhpgCs-kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر نفت استعفا کرد
🔹
معاون اطلاع‌رسانی دفتر رئیس‌جمهور: با پذیرش استعفای محسن پاک‌نژاد، طی حکمی از سوی رئیس‌جمهور، حمید بورد به‌عنوان سرپرست وزارت نفت منصوب شد. @Farsna - Link</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/farsna/466635" target="_blank">📅 16:23 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466634">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FukuGBICLZges6jHYs_TN8PSxo6T09lbmiEBjiXxPXkdUyCs6xvql7UMzhy2d-i-74dA40CPoPIrX57cw53wTMrp104k3S--HfFjg2FlZNdmymwV9grGk1YMOd2CUwH3mA-rvzZG04MvnjnUkL5b1-qH77oBdpXYVAm30flGWIJk5zKKK5e_nLEIwQ-tDn-m-Qvtsr5GFOfN8HNEettwwI6AjROV_3T_Bh5w2iOsmygIahP_htoWG-SV3ThTkkb1x7ghZRNxol8RZe3UE1qCCpeGCM-5Y8hPOljyl6wS_k9-ME7fsXtyt2EzCZSIzO6wHw7yx5VQmFksaz2aDVJxjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
دبیر شورای‌عالی امنیت ملی خطاب به آمریکا: ایران عقب‌نشینی نخواهد کرد
🔹
پیش‌بینی‌های توهم‌آمیز بسنت از همان ابتدا هیچ اعتباری نداشت. تبلیغات اخیر او نیز به همان اندازه عمر کوتاهی خواهد داشت.
🔹
شما در جنگ نظامی شکست خوردید. در جنگ اقتصادی نیز شکست خواهید خورد. تنگهٔ هرمز با تهدید یا فشار باز نخواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/farsna/466634" target="_blank">📅 16:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466633">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c79e7f6ebb.mp4?token=B640PDSejec0y6JedwL0HMpgRzZEszzRLbgznXNrBAh7rRJUv1y1vIezRPMRteNLq30yktXaib7arSQtyO07GlK9LIXI43Uck3A3XBm72acICQBN6O0HiF69QIgPmC7SG_K0S-1k5_iJR1YJnl7JsGwDZZ7vXmn8bjM4xfywch5sSmxg6keLa6Q0yoGkrDbHrwrgs3otV_IGSNHDXANAeN3W6AI0HOFHgMBDqSpQr3VRRW4kYNKn6SqJeXTj0hDHP-k9hG7XQaxsNibuflIcRPnXz0khHrWo8FuwWDovNIFHOYrlEDikVTaJg6YfxozeT86hXjy8IAxYR59PlqH0jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c79e7f6ebb.mp4?token=B640PDSejec0y6JedwL0HMpgRzZEszzRLbgznXNrBAh7rRJUv1y1vIezRPMRteNLq30yktXaib7arSQtyO07GlK9LIXI43Uck3A3XBm72acICQBN6O0HiF69QIgPmC7SG_K0S-1k5_iJR1YJnl7JsGwDZZ7vXmn8bjM4xfywch5sSmxg6keLa6Q0yoGkrDbHrwrgs3otV_IGSNHDXANAeN3W6AI0HOFHgMBDqSpQr3VRRW4kYNKn6SqJeXTj0hDHP-k9hG7XQaxsNibuflIcRPnXz0khHrWo8FuwWDovNIFHOYrlEDikVTaJg6YfxozeT86hXjy8IAxYR59PlqH0jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملۀ مرگبار به کشتی ترکیه‌‌‌ و اعتراض هند
🔹
روز گذشته مقامات رومانی خبر داده بودند که در نتیجه حملۀ احتمالا پهپادی به کشتی رویاد ممدوف در دریای سیاه و در نزدیکی سواحل رومانی، ۲ ملوان کشته و تعدادی دیگر زخمی شدند.
🔹
حالا امروز وزارت خارجه هند با انتشار یک بیانیه این حمله را محکوم کرد و خواستار آزادی دریانوردی شد.
🔸
به گفتۀ وزارت خارجه هند مجروحان توسط مقامات رومانیایی نجات یافته و تحت مراقبت‌های پزشکی قرار دارند؛ ۳ تبعۀ هندی که از خدمه کشتی بودند، در سلامت کامل به سر می‌برند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/farsna/466633" target="_blank">📅 16:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466632">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/401d1ab6bf.mp4?token=LyEQekNFSuydShI3BzzKzZhKVHOW5TYWNB_-l5i1QVcx9ZslcWOy8xSOSuhOcoUhbn7LFKtfb4M4kWtA8VGBTf8XJYZFJ8UK5D0qkqyE0jDjIzUw_xFph_vBFEW77jt0qFVqPy-oueKWLJuJrESn3jJpoBwlz_eLzFiZIKUx9B6lFbzYIBpchqSYLDb1il2XH3m8_DDr9VUwTocZZpBoyh15IqHtzOxCCnDcT_dwMq6Ffkg8W9-od9FDoK66GMUa7HWrr7LN4oRrahphyOK6oJvLgu5oep_LLyPFJVWhzLba7igicRR2fwKEnamCFkc_SURdeaG6E50DZ3hwn0zJ9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/401d1ab6bf.mp4?token=LyEQekNFSuydShI3BzzKzZhKVHOW5TYWNB_-l5i1QVcx9ZslcWOy8xSOSuhOcoUhbn7LFKtfb4M4kWtA8VGBTf8XJYZFJ8UK5D0qkqyE0jDjIzUw_xFph_vBFEW77jt0qFVqPy-oueKWLJuJrESn3jJpoBwlz_eLzFiZIKUx9B6lFbzYIBpchqSYLDb1il2XH3m8_DDr9VUwTocZZpBoyh15IqHtzOxCCnDcT_dwMq6Ffkg8W9-od9FDoK66GMUa7HWrr7LN4oRrahphyOK6oJvLgu5oep_LLyPFJVWhzLba7igicRR2fwKEnamCFkc_SURdeaG6E50DZ3hwn0zJ9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مزدوران سعودی در راس‌العاره توسط موشک‌های یمن
صید شدند
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/466632" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466631">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرسانه رسمی هلدینگ تاپیکو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WETyyo3Kuc1NKIQpfPJp5VTkP_eSSCZ4zetvYuJrv_VccKhoSK5O_9UVSYPZoyYXKFC8xCZ6FfeR5WW5Bz7lHlb8wyMl_M7AKGcSh3tNgTP2r_vsuZGyfjWGcEfNlYnvxiOY1mB9yfct7Fc7Ebs6B3kRpF_MjLbDVMHC1tYZF6tve8oF8u94tpy9WhA0me1Are-TjYAf0SU74ksY6zF411RPy6kTAEtGESoybGfNC34AIqMrUwa0apMwxY6lWayRrudbBUfIcxNZ4JLkxKD8_-oUSldRLUxZPQd2olzSsNKJYCzALaJBcIwuFUGLP8NfkcsIP0yQc4LmmJ0fDOdw8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از تز تا تولید؛ نقشه‌راهی برای توسعه فناوری افزودنی‌ها در صنعت روانکار
✅
روزنامه دنیای اقتصاد /اکبر میرزاپور/ سرپرست شرکت نفت ایرانول
🔸
صنعت روانکار یکی از حلقه‌های مهم زنجیره صنعت نفت و از نهاده‌های پشتیبان حمل‌ونقل و طیف گسترده‌ای از صنایع کشور است. در این میان، افزودنی‌ها (Additive) اگرچه از نظر حجمی تنها بخشی از محصول نهایی را تشکیل می‌دهند، اما نقشی تعیین‌کننده در کیفیت، عملکرد و امکان تولید بسیاری از روانکارها دارند.
نقشه‌راهی برای توسعه فناوری افزودنی‌ها در صنعت روانکار
اینک بخشی از افزودنی‌های مورد نیاز این صنعت از طریق واردات تامین می‌شود؛ وارداتی که علاوه بر ارزبری، با مسائلی نظیر تامین و انتقال ارز، محدودیت‌های تجاری، حمل‌ونقل بین‌المللی، طولانی‌شدن فرآیند تامین و محدودیت دسترسی به برخی تولیدکنندگان و فناوری‌ها مواجه است.
🔹
[لینک متن کامل یادداشت در وب سایت](
https://www.tappico.com/NewsDetails/d925c49b-d925-4e5b-9056-08df237183e6
)
@tappico1381</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/466631" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAJqaRXiFOuDaUVH1rDG3qU_s8UJwHA_jOesjhOszAX2yJI_wPyToLIsp0kEvwn0GKP0sN-4abPLwkBf8mfqmsXr0yoR-oBR1G9JtYOU2HaZlkTRnEWT8JnLXs8a3tj5-BggheYjy357lPH7WbtVIEtEBLih3uU_gimQClyLMYiV_0xBRlQqfXUbA3puzUhFB8QKp1yVhGM1O40PkusLzmOUVLDJX4WMQNnszY24l6wzqG0jk1bq7s9AXmTGuPRNpDJO7Hfkj2EokxrfHggbYwD6zQnE5GD3r1apYS6iCiayGKWUl85Rkz-AmbuayUvZui8UFjlw_MvQMBU2hgnHbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
طی شش ماهه نخست سال ۱۴۰۵ صورت گرفت؛
رشد ۶۳ درصدی پرداخت تسهیلات بانک کشاورزی / تزریق بیش از ۱۴۶ همت به بخش‌های مولد
🔻
بانک کشاورزی در نیمه نخست سال ۱۴۰۵ با پرداخت بالغ بر یک میلیون و ۴۶۰ هزار و ۹۵۴ میلیارد ریال تسهیلات به متقاضیان واجد شرایط به ویژه فعالان بخش کشاورزی و صنایع وابسته، رشد ۶۳ درصدی را نسبت به مقطع مشابه سال گذشته به ثبت رساند.
🔻
شعب این بانک از آغاز سال ۱۴۰۵ تا پایان شهریورماه، در مجموع ۳۱۷ هزار و ۱۰۳ فقره تسهیلات به متقاضیان پرداخت کرده‌اند؛ رقمی که در مقایسه با عملکرد شش ماهه نخست سال ۱۴۰۴ ، از نظر ارزش کل پرداخت‌ها ۵۶۴ هزار و ۹۰۱ میلیارد ریال و از نظر تعداد تسهیلات پرداختی، ۵۴ هزار و ۲۶۵ فقره افزایش یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/farsna/466630" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/farsna/466629" target="_blank">📅 16:12 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7afb904f50.mp4?token=djhdipiVFdAVdi5-TeYQQaTlmXy4xBtIh_eikf0awmrIcltRAzKfCNn7EPHNSo5bbAIyyee2bDA6X5IqZad4Iv0lC4hHSYKL9O8IEsLWbgrIxDcANV00kMYuSzxq7YKtpvevZeDXwqTn1pgkWXcELq_0ekdVHkMmJQUXg5pKhM90y15SIq16GsTOWMh9bL6xpzRQX5-1cGyUwWS_z8NTETRMyUw-vrQ_RQWfKFX_9JbTaHIJNNuoGEQtey6FhaOt8vfQYG8ow5tCYMe5bDEEOCN8S51gekWEZ0mC9nx5H3Iv3vxd0lbDA8dfTU0zbhdv27Du6MIpn8XMs80IaP0vKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7afb904f50.mp4?token=djhdipiVFdAVdi5-TeYQQaTlmXy4xBtIh_eikf0awmrIcltRAzKfCNn7EPHNSo5bbAIyyee2bDA6X5IqZad4Iv0lC4hHSYKL9O8IEsLWbgrIxDcANV00kMYuSzxq7YKtpvevZeDXwqTn1pgkWXcELq_0ekdVHkMmJQUXg5pKhM90y15SIq16GsTOWMh9bL6xpzRQX5-1cGyUwWS_z8NTETRMyUw-vrQ_RQWfKFX_9JbTaHIJNNuoGEQtey6FhaOt8vfQYG8ow5tCYMe5bDEEOCN8S51gekWEZ0mC9nx5H3Iv3vxd0lbDA8dfTU0zbhdv27Du6MIpn8XMs80IaP0vKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدارس فرانسه به دلایل امنیتی تعطیل شد  به دنبال اعتراضات دانش‌آموزان دبیرستانی در فرانسه شمار زیادی از مدارس این کشور که در کانون بحران قرار دارند تعطیل شدند.  @FarsNewsInt-Link</div>
<div class="tg-footer">👁️ 6.75K · <a href="https://t.me/farsna/466628" target="_blank">📅 16:10 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dg0DN2Pc4IfZlkSOCnbDgB4NAOuAlxjX4P0R4RNBPDcPNJVwuMk_7mv8l2hcpkAecJv5EI_bFT_BMQYZFSLPWC0246T_PR3e_QdsZtmRKgZ15jjJEC_caogxmbwBH47094r102rPevfUws-8ymk8kefa1uMpMxbXZKSBHAPaN6gDmh2tu9rfhcnUHSY36wb9OP4242goSq89VI_Iz6mnQA8mOv0tgI8nyIQqYs6ffovZ7O__6ISrru4-RKeiXQnbXYg9SU1THD3WhWqQFQp8UaWtKCGesnN4ahXE_mD7uW-yO1lnPkEMQEDjRyOjE8N2ini2jl6RT-gcF-pEDc_AGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیمت واقعی نفت به ۱۴۰ دلار رسید
🔹
کمپ، تحلیلگر ارشد بازارهای نفتی می‌گوید که قیمت نقدی نفت خام فورتیز (Forties) بیش‌از ۱۴۰ دلار در هر بشکه یعنی بالاترین رقم از زمان آغاز جنگ علیه ایران است.
🔸
این نفت که در دریای شمال معامله می‌شود یکی از بزرگ‌ترین اجزای سبد نفتی برنت است.
🔹
قیمت ۱۴۰ دلاری نفت درحالی‌ است که ترامپ و وزرایش می‌گویند که عبور زیاد نفت از تنگهٔ هرمز و خط لوله‌های جایگزین، صادرات نفت خلیج‌فارس را به وضعیت عادی برگردانده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/farsna/466627" target="_blank">📅 16:05 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L_vFSSFxeoHrJ6aSV5HYiQviFn8pSsamZT71sLgHK_4W_nA9oEn1QrivfcU178OeqtkR-gLgm40TUf2Gi84PDsSZoOGEpfv2mAp2hcMSgo_HQQNowZrR9i_5Ib7oJ_9BIFjrr4tUqVSd460VfZThs_7LzuKgC_nVRQqQGo5ZtdC2_Hjk9DtmDgz3G3HRE7OFQLzCbf3WbS2dxpOOfa_COkfr_mA3tcFudoAH8QlyXkMZAGsVqt06mjiW9O_coNiSGT-hXMhdUem2IGjs0ObOSYuyjY2Emez6zoA336EBsnPZtaCxEhm6zwjMgR7yxYc7wPhIjIQ6UEHVUquoDkA1SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۶ ریشتر در عمق ۸ کیلومتری زمین، امیریهٔ سمنان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/farsna/466626" target="_blank">📅 16:00 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHmKSYJ3_eOOZ9C0QK3e35zdgi5PTPs9D3twh_av09EoLRgFILxOv2tryWm7yJIvEYeTbQ_sS2xDEuyRVnyTCUFTJFgLzXwR4V_vtD48LWBJDfTXicf72luzAqnwvw--znHAimiSmGErTAoYxQ9STj8hyvY4fNag5IuJ_gB2mAyOgx6rbhJmYkL-5Yf26OwTCfCpPBceyKB_W7YiRUgkNGwTUhLEZ9uygrFLxqZWNUBYfppYagOVWc9GjCWkDj6sMnp1-E_q8LLtsXJywNUMPTcfBrn_PueFGYEFbZZHUSMoV9H9atUkSmTlWzbKf-lSxHScvt7OzwYrxsnmwIN7_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان تجارت دریایی انگلیس: یک نفتکش در تنگهٔ هرمز هدف حملهٔ یک پرتابهٔ ناشناس قرار گرفت.
@Farsna</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/farsna/466625" target="_blank">📅 15:51 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466618">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ro55vBwG__Xqh1IXylfttxwsd7sW0TTjYOnGp9NdyQgxBOfcaYoMTtpYAbpg2WN-QkthmP8RYHfz6H-Q35tilLd8hI2F307Mob6BxZOlz_E9cB8EcX65Q1GtoBU0-XrPMQJUhZu1qt2-W4LblKqJpwuP8boNPOMd54pE6i89Cr9dxALY4lj5K8h0qe3063dXBi2UTU8MSBFn-Epw6FnBxn4HwzqvGs1uea_i8JJVW1LhZ9iGqvNB12Dgf1WqFBE5_9m67bwkSq9U-MJTbBMubFk2yBUCSePKxBHCSGrtc1KZ5HIdHc7ZARuPIsk1bkDdNV02Jm8tFHTZuWW1dhc5og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOxrdFIcfchXxcPX883Py5Ec3DRTZWINmiTWn0N9Cr-D4QUvyFgkS7GcVeOdKb_30EXGfc3FQzAw67lfgqKzb3Hk1ysAYz-I3vwsVP5b6vTR9pd5hbdowpTql8t3MIvxd58FMMbUe86AK0pc--kMf891oH5O-VCv-X8uq_dxzFRD3mm18JY0pRE4ePxL8kfFJgzlBurpodG2sK8vCqUhzqk4HOfugzfCd0vVkjUN9gY3k5s5Vbzqsbc3Sy9UJnXUwXYXK27KYascfVU-03tNPKropwQZsvqiat7fs-jW320Kpf8zfMyduPsKOY6YgoGEX7rjsVM5Oy7gweUvTfuFzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGUCOLzezE8HxhxGnTWJqstysFxNpG3v9pj6qnGST-YjeNr2rCyLA_VRYuLjoQMGFAQYWWaMOFKNEGjT1v4IacWgdXoQuUvylsgkNZyC7JZ0Pd7ITVyevAkrTu9iP-6izCgpWqj0gO352ZX57t9127VBUSyxc5QdB6e6xGsCOcr3IeBjgurltE9nnWuji_LzbL1ALF-ogJRUluRUepbxsQzYzZQoVWtjZlzF2lw6itpItiNwqHVYmFdgUNDYNGs4zumC0ClqV3Zt3Oxe_Ek4c8qRG4vRrzTSAd3hnKcOv8vq87xBqPkKIHpBQwr_Sl9oNRvWeWckumcLtofH28bmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGUCOLzezE8HxhxGnTWJqstysFxNpG3v9pj6qnGST-YjeNr2rCyLA_VRYuLjoQMGFAQYWWaMOFKNEGjT1v4IacWgdXoQuUvylsgkNZyC7JZ0Pd7ITVyevAkrTu9iP-6izCgpWqj0gO352ZX57t9127VBUSyxc5QdB6e6xGsCOcr3IeBjgurltE9nnWuji_LzbL1ALF-ogJRUluRUepbxsQzYzZQoVWtjZlzF2lw6itpItiNwqHVYmFdgUNDYNGs4zumC0ClqV3Zt3Oxe_Ek4c8qRG4vRrzTSAd3hnKcOv8vq87xBqPkKIHpBQwr_Sl9oNRvWeWckumcLtofH28bmzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV6-WG9U_xq0YRWbcclzFG0qD4rqoMHxoBgyx_Um3sdp6Me-b_lNvJ_UYCcM-PqWin-YZR9UATrGBvXDt0XByZJRXsPI0BYMMCidwGiDRMWGXzA_vTUGK2TDrdp-6CA301lCnYo8qhbmblosvhnGqhd26AUNHokPan-jYAT77MOkCVnSwCzYa4Luqlroj7eoUfVJEs4yWJwOodqLkyggyN9qzalY3lpA5R2uPDwE5QhqoOiqj2Fxi9J7pBGHIfheOeMPsGvE6Q31NRpJT487hQFrMH4-XvLsvS4WJBnlc-qDxOKI1GR1p4RrZK3uFlJ55CH-jhesayO-JPrTYqJoxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EizZhGyqTCWyDgYJiOiLQ0RWhGZDlcBs872c7cfu8aYG3_ibxllqzTO7HAmhPlNhBikKQoRUDH7tnT4bMGQ8ln-9WN6GtF14WoTSI1TtjeStA4_DM_TIGND3b9O_NYljEuKW4WAE6eH5vC511DtmF0O7VxT9cnbUcCkSJIp24aFPhURSSRjyZSAcG7YuhvW_3ktjht3K8HDPazsGobnDILXvrlDjYmD5szdjytDuLbyMcDbUO8nIPMeL1TgLgt1dWxawvlvroWWh4dvVDaWaFR_1WViHw_39mCIZgdHeGKIH8Ni0RcdvMJiF5M1wwpZvssCemDCXdYY7W4PbHnJmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RRkLt8-iIh2rSN07pdsjMDlZ0cBWXroXnRtyeNBjZnYUNI1IQmvzI3o4UZKVV_CBnpIMGSsHvDhK_SeONqklsrf4IIBj8-KtBZnIyBzZKTGIqNVofIdmRTlcWQbr4sHqfEcEOfiLcKkjJjSZbHElVApY9Jtrmi-N1dygzk62VLybsfu8qRjfdqi8jP-U7WMdF-A7LcFMlvzdruBllKirTn7Uvs5xefc_Wuu9RU_jCXKZGcxv3-mN1OmbfbzYymur2rU5oWmaxLDSoHeW_6c2I9W2iH3AGcohYGcLj8QlePGZpHhzzisbhtzRdPz929XsV6QEYcGP5zcL-jYxZCyawA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
جنگ رمضان روی جلد کتاب‌های درسی آمد
🔹
امسال طرح‌هایی مرتبط با جنگ رمضان و رهبر شهید انقلاب به جلد کتاب‌های درسی اضافه شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/farsna/466618" target="_blank">📅 15:46 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466616">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مقام ارشد انصارالله: تعز عملاً آزاد شده است
🔹
عضو دفتر سیاسی انصارالله، با تأیید محاصره کامل تعز پس از آزادسازی مناطق اطراف، این شهر را عملاً آزادشده خواند و تاکید کرد که این پیروزی با مشارکت نیروهای بومی استان و حمایت مردمی به دست آمده است.
🔹
حزام الاسد در…</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/farsna/466616" target="_blank">📅 15:34 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466615">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b7acecaf4.mp4?token=J2jE3ccUmwmNclvhMb591I5HU7LDdn708uQg9nHD2Cmo_Knjua5y7TpwEvh9aJWKAvqaz4DiocooJ6TjyEh12GJVBNJgtI4AjJRJFHtIL6hqswFZDZrWuS8jy3hRoF9x9AAr6OslS0olsnkQXe4Lq4a-34SX97mIGvDqIbMxydPwsF5xWom6O2_klCIW67lhd2JLg3jk_NVsPUDirhXEWwk-3okAQb4gRyjLzmRczmt5IBFvOukyFOzHxSkzejMWboS724zfnfnQnf1YQadi6zEhVwjwZU27d3a9BQtVpf1pDpqcxBXNyQURpAECiFTVyEvTEghRmGQSpqKX3z_TmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b7acecaf4.mp4?token=J2jE3ccUmwmNclvhMb591I5HU7LDdn708uQg9nHD2Cmo_Knjua5y7TpwEvh9aJWKAvqaz4DiocooJ6TjyEh12GJVBNJgtI4AjJRJFHtIL6hqswFZDZrWuS8jy3hRoF9x9AAr6OslS0olsnkQXe4Lq4a-34SX97mIGvDqIbMxydPwsF5xWom6O2_klCIW67lhd2JLg3jk_NVsPUDirhXEWwk-3okAQb4gRyjLzmRczmt5IBFvOukyFOzHxSkzejMWboS724zfnfnQnf1YQadi6zEhVwjwZU27d3a9BQtVpf1pDpqcxBXNyQURpAECiFTVyEvTEghRmGQSpqKX3z_TmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتصاد فضایی کشور
روی ریل پیشرفت است
🔹
رئیس سازمان فضایی ایران: تبدیل داده‌های ماهواره‌ای به محصولاتی مانند تصاویر پردازش‌شده و نقشه‌های تخصصی، می‌تواند ارزش‌افزودهٔ چندبرابری ایجاد کند.
@Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/466615" target="_blank">📅 15:21 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466614">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cveo2Yq3mmI3QbWtCFwdnRCFUPoHRfj5NU0GwGgeNDhplwFDhF3GKgw6AUMCh_FpYE5uuhltKYLP5rS2VOulH1i8O85y7xcPPJyrm_MfzJT0IhPudU1pHAXZi1rNgAhaso6mxLjN1irhyNaURFY7FZ7KrXLKX1707W9zpllxEgfEf0uQngoP32Y6-32cwaP5kHYnQw04LapdBxo7XTL35-uDMfoBwvGlKA71DiihUTYE-khFfqx-kpi9EC8VktmvMeVLkYXwz_6E8t5B38Q2qA5yTRE9UMbn4haSAWx5u6TKkpfwKD5GBtI4VqFucC8K21l4aEJM5-gYRLjDIcReDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ساپینتو: تاجرنیا به من گفت فتاحی می‌تواند کاری کند که داوران با استقلال مهربان‌تر باشند
⚽️
سرمربی سابق استقلال در گفت‌وگو با فارس: تابه‌حال مدیری به شهرت‌طلبی علی تاجرنیا ندیده‌ام.
⚽️
از روز اول تاجرنیا به رابطه من و مدیرعامل وقت آقای نظری جویباری حسادت می‌کرد…</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/farsna/466614" target="_blank">📅 15:17 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466613">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‌ سخنگوی وزارت دفاع: همکاری دفاعی ایران با روسیه و چین ادامه دارد
🔹
همکاری‌های دفاعی ایران با روسیه و چین متوقف یا کاهش نیافته و در برخی زمینه‌ها نیز تقویت شده و ادامه دارد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/466613" target="_blank">📅 15:11 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466612">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc17e016e.mp4?token=duPmXTw7IN6eA-qJVYftT1ftzqXe11h8k6xcPpW7B-pwS5wHzttbpGo-SlSHVoRcehINuCniJ1mpZfaNfXjq0YT1CVS1tZid9sw5i8F0GoHCu6t45bfk56bVTnJ2jnllxUHzVk9tXi7rtWjXN-JqPm5kQzDjVQwsFmRgLb_HCJABhe-wiiThxj0XFdrO5dbTs_ErsDCh9XNQUnaHD7dYc-MmuKgNYY2CEG-rFV5ysQ7Ep2rsxJNpdYoQ28HQRy3sgwg-3i1mYQK8vAw9JQcn_N8Ay3RJX3KTWby8znTPXKH_NdpWNewLsfVx0-5mAJn4MX9XUHQaC_CILsv89CpL6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc17e016e.mp4?token=duPmXTw7IN6eA-qJVYftT1ftzqXe11h8k6xcPpW7B-pwS5wHzttbpGo-SlSHVoRcehINuCniJ1mpZfaNfXjq0YT1CVS1tZid9sw5i8F0GoHCu6t45bfk56bVTnJ2jnllxUHzVk9tXi7rtWjXN-JqPm5kQzDjVQwsFmRgLb_HCJABhe-wiiThxj0XFdrO5dbTs_ErsDCh9XNQUnaHD7dYc-MmuKgNYY2CEG-rFV5ysQ7Ep2rsxJNpdYoQ28HQRy3sgwg-3i1mYQK8vAw9JQcn_N8Ay3RJX3KTWby8znTPXKH_NdpWNewLsfVx0-5mAJn4MX9XUHQaC_CILsv89CpL6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
هواشناسی:‌ امروز در بخش‌هایی از شمال‌غرب، سواحل جنوبی دریای خزر، دامنه‌های جنوبی البرز و دامنه‌های جنوبی زاگرس شاهد بارش هستیم.
🔹
این بارندگی‌ها منجر به هشدار سطح نارنجی و سبب آب‌گر‌فتگی و بالاآمدن سطح رودخانه‌ها و مسیل‌ها در آذربایجان غربی و شرقی، اردبیل و کردستان شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farsna/466612" target="_blank">📅 15:07 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466611">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aaJtcEG-59xFVWzfsTJZmXv1G-ic74NcX2M8LWBbjiRhvOh80PVIiBmJmfkMPwG6d24FG4CzD5Tl6w9Fpo0sLN4aLLVJV2sEABzF8hTlWdRrVmVXD5PwluWjubXyc-EjzJwXTm_Cb0vTGlRUhwNW9OtB5goOghKYY_Uqw2aDpleRWtbkKBskYKJhmk6FZdlo_Qc3ir0QFTaOKux-V9-vjDu4cIIQUg_3brqyKOFVF-woBf7VkMe-rMS6lJ5_wBDUVEE7JNZV__bCVbqYUTWHBJEAD1AAghRbKGuHXNWPlljYFP1iCeUSux2YIeIxIF2pkUvTpqvYjx9OfSb37NPlDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیادت رئیس دفتر رهبر انقلاب در قم از آیت‌الله نوری همدانی
🔹
آیت‌الله محمود محمدی عراقی رئیس دفتر مقام معظم رهبری در قم با حضور در یکی از بیمارستان‌های این شهر، از آیت‌الله العظمی نوری همدانی از مراجع عظام تقلید عیادت کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/farsna/466611" target="_blank">📅 15:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466610">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364de1749a.mp4?token=fbicKpZJWBiWscz7MechRp-2d_hfBkRQWqAd1KLqc1oABhuNzxm3OUny7G4BxoTHci0C3VfIYI4PGUShk8itdsTmsd7VPtMl2AkDxA8HtgIv-Wn3qMd0GhoG1_Qvnqo1MkGDVwIAehYq8RmPBAt-rYH8YTOd2f-MNOmANIfui4Y0d3DyPs-WMxEUnpieLjgTcwleID-BOhEiuaHyhsSiIv0JQGiC8fuhgHmkgXHUrNrugexHZMRXKkrMm5aTUFABDe7D2r_SHkIVuJZbIh9sdl_lY3x6MPQUf4LwUTjhYa9iFT7vGJFO5hjyXIw5IdTWHXqMG1QHaje8UZ907aEeew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364de1749a.mp4?token=fbicKpZJWBiWscz7MechRp-2d_hfBkRQWqAd1KLqc1oABhuNzxm3OUny7G4BxoTHci0C3VfIYI4PGUShk8itdsTmsd7VPtMl2AkDxA8HtgIv-Wn3qMd0GhoG1_Qvnqo1MkGDVwIAehYq8RmPBAt-rYH8YTOd2f-MNOmANIfui4Y0d3DyPs-WMxEUnpieLjgTcwleID-BOhEiuaHyhsSiIv0JQGiC8fuhgHmkgXHUrNrugexHZMRXKkrMm5aTUFABDe7D2r_SHkIVuJZbIh9sdl_lY3x6MPQUf4LwUTjhYa9iFT7vGJFO5hjyXIw5IdTWHXqMG1QHaje8UZ907aEeew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وقتی جغرافیا معنی آشوب و اعتراض را در برخی رسانه‌ها تغییر می‌دهد
@Farsna</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/farsna/466610" target="_blank">📅 14:57 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466609">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1a5676575.mp4?token=dXcubmuYx0GsRThXYC2guzLYPDh8guM8F6XE3CGsMlp0n8Lfas6AJzFUCk2sRMnAjvZXt3l10X_nMjzP0mo9KiK61nZPsjs_QfpLGxDMlBU5KzAErLaGC5JCXMOF15i7iv-erYNXYZ1lcRei4YA4_kIlXaa5_45-MPZ8H2BHnaLLJhqs_7Idru1xs-K4200PI3WpY8WCbrFd8IpN4R3arSTyI9mQsUWPgNsjfOHHDxX-u2TpA0IKnWcEIagqi_5CQPWzrVDDU2mDDwhM_K118STg5vkm-VIveRO-cQ2_xTHJ_PxnNgibYFOWrGvJKR-zijqOplJAfhytfFFzwiUilQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1a5676575.mp4?token=dXcubmuYx0GsRThXYC2guzLYPDh8guM8F6XE3CGsMlp0n8Lfas6AJzFUCk2sRMnAjvZXt3l10X_nMjzP0mo9KiK61nZPsjs_QfpLGxDMlBU5KzAErLaGC5JCXMOF15i7iv-erYNXYZ1lcRei4YA4_kIlXaa5_45-MPZ8H2BHnaLLJhqs_7Idru1xs-K4200PI3WpY8WCbrFd8IpN4R3arSTyI9mQsUWPgNsjfOHHDxX-u2TpA0IKnWcEIagqi_5CQPWzrVDDU2mDDwhM_K118STg5vkm-VIveRO-cQ2_xTHJ_PxnNgibYFOWrGvJKR-zijqOplJAfhytfFFzwiUilQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ذخایر سوخت
نیروگاهی به ۹۰ درصد رسیده است
@Farsna</div>
<div class="tg-footer">👁️ 8.19K · <a href="https://t.me/farsna/466609" target="_blank">📅 14:50 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466608">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ظرفیت تولید تسلیحات دفاعی ۲.۵ برابر شد
🔹
سخنگوی وزارت دفاع: ظرفیت تولید تسلیحات و تجهیزات دفاعی کشور نسبت به پیش از جنگ رمضان ۲.۵ برابر شده و در برخی تسلیحات، میزان تولید بیش از ۳ برابر افزایش داشته‌ایم.
🔹
برنامه‌های تحقیق، توسعه و تولید تسلیحات متناسب با…</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farsna/466608" target="_blank">📅 14:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466607">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572d31cc4d.mp4?token=BzHo_SyiTDfzF74y_Znch0_lYXfPhidhsmpIqtG5vh6K_8ZdHUNLKwx6l64Fvcsc3UaqCv3hRneig8E4GzGwc7SrIxrDNa8ce2dYVUtX2qQQwq8p-Zb_TaahD4RmL9uv90PEQcYDENmzwVUxQCQwWJvi37SGEBmpQuL6Ks2mlTDIhG6wT4hSvpXRthduOT5aAI73xAmC3joKUEa5CArb2pA1WoXCxsbcC7P_odwBoPUOxq8de3jaKs3jIRLn6oJv3E-XjkpudX_MwDwARGmAQRy-gxYgb63zka-GtLDfzWVTeGNjuatzQDES_0joiaKBZzvI1ICr7MLvj4i5JKsxaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572d31cc4d.mp4?token=BzHo_SyiTDfzF74y_Znch0_lYXfPhidhsmpIqtG5vh6K_8ZdHUNLKwx6l64Fvcsc3UaqCv3hRneig8E4GzGwc7SrIxrDNa8ce2dYVUtX2qQQwq8p-Zb_TaahD4RmL9uv90PEQcYDENmzwVUxQCQwWJvi37SGEBmpQuL6Ks2mlTDIhG6wT4hSvpXRthduOT5aAI73xAmC3joKUEa5CArb2pA1WoXCxsbcC7P_odwBoPUOxq8de3jaKs3jIRLn6oJv3E-XjkpudX_MwDwARGmAQRy-gxYgb63zka-GtLDfzWVTeGNjuatzQDES_0joiaKBZzvI1ICr7MLvj4i5JKsxaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بحران قیمت سوخت دغدغهٔ اصلی کاخ سفید در آستانهٔ انتخاب شده است
@Farsna</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/466607" target="_blank">📅 14:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466606">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ظرفیت تولید تسلیحات دفاعی ۲.۵ برابر شد
🔹
سخنگوی وزارت دفاع: ظرفیت تولید تسلیحات و تجهیزات دفاعی کشور نسبت به پیش از جنگ رمضان ۲.۵ برابر شده و در برخی تسلیحات، میزان تولید بیش از ۳ برابر افزایش داشته‌ایم.
🔹
برنامه‌های تحقیق، توسعه و تولید تسلیحات متناسب با شرایط جنگ و اولویت‌های نیروهای مسلح به‌روزرسانی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.9K · <a href="https://t.me/farsna/466606" target="_blank">📅 14:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466605">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدانشکده خبرگزاری فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meUNCe0AL15b8vLE-JD6Ud48OHxkncmTzk1AW4Vsa4PhOHVOUldMo-6P4jiI_JUyRd8Na-3iJ3tRN0-rRrvylSybNG9Iz0KZSkjk5lwDAMcuLLgM3TQ76a2jGg792ancnALN98PaHXoEInGA6lxiErVNvPIb9uJz-KUPLNaF48kaVx792gRU3_PxFqRCc_T5rXk5JUxqIJicM_9oRQQf3igrga9aV2TsEQRpNNiA52SXeyQIuNIZp5GwQ7E6R0G1rZrb1AAyo9mI_79DNu6AH8szOG5tYcQjLRGoyAPHYlFqswU8tz3Gm0HpAlSFigozAAtcg2i7b-tvJ0SkH-hfBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔰
مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره های کاردانی و کارشناسی ناپیوسته دانشکده خبرگزاری فارس تا ۱۵ مهرماه تمدید شد.
🏷
براساس اعلام سازمان سنجش آموزش کشور، مهلت ثبت‌نام و انتخاب رشته در پذیرش دوره کاردانی و کارشناسی ناپیوسته دانشگاه جامع علمی کاربردی
از امروز تا۱۵ مهرماه تمدید شد.
📚
رشته‌های تحصیلی:
🎙
خبرنگاری
📸
عکاسی خبری
🎞
سینما‑تدوین فیلم
🤝
روابط‌عمومی
🎤
گویندگی و دوبله
ارسال  عدد ۱۴ را به شماره ۵۰۰۰۱۰۱۴
🌐
لینک سایت ثبت‌نام
🔗
futurix.ir/go/rxDxXO
☄️
☄️
این فرصت رو از دست ندهید
🎓
مرکز آموزش علمی کاربردی خبرگزاری فارس
🎓</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/466605" target="_blank">📅 14:33 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466604">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6520f38466.mp4?token=AL6nGQiC1cRBd8UDRwgDdX4m1LKHb_sG6EjpqJFpe8AGc7tlCG5YoDalteV6YoBzStP_OYlx1-7Iu-hJlgwRv8I8q__3ga45qJuZo6tEFBHvT-2GZQIcFs79xHGW3hsOias_kabvzNZHhJxMFCzElWoQHBhwpkJA1fKP1D4kSmy1ynJMrISjqOPcLPK85Td894McjOj8Bwq70EpIYsSJdfHuw43KvoJVTCUmJvZqc8Ge8SoUNXR7jrsTOw-l1KhpnljKypL75agD2ppTAJ-VLY1oDyxrBKYSbazs3DbW6FRM0uyTeGseGYcf5X5wu_uMM_h3etKZ0_pkBlXVNIKUnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6520f38466.mp4?token=AL6nGQiC1cRBd8UDRwgDdX4m1LKHb_sG6EjpqJFpe8AGc7tlCG5YoDalteV6YoBzStP_OYlx1-7Iu-hJlgwRv8I8q__3ga45qJuZo6tEFBHvT-2GZQIcFs79xHGW3hsOias_kabvzNZHhJxMFCzElWoQHBhwpkJA1fKP1D4kSmy1ynJMrISjqOPcLPK85Td894McjOj8Bwq70EpIYsSJdfHuw43KvoJVTCUmJvZqc8Ge8SoUNXR7jrsTOw-l1KhpnljKypL75agD2ppTAJ-VLY1oDyxrBKYSbazs3DbW6FRM0uyTeGseGYcf5X5wu_uMM_h3etKZ0_pkBlXVNIKUnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از فضاسازی‌های رسانه‌ای تا واقعیت‌های میدانی میان یمن و عربستان
🔹
خبرنگار شبکهٔ العربی: نیروهای انصارالله توانستند مسیر اصلی عدن به تعز را به‌طور کامل قطع کنند؛ همچنین بیشتر مراکز نظامی، امنیتی و سیاسی در مناطق شمالی عدن از حضور نیروهای مخالف انصارالله تخلیه شده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/farsna/466604" target="_blank">📅 14:29 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466603">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bdd7169e.mp4?token=nC5UmsFcqMvPeaY6ECzOcKhxQE6GtIWsFiZDOvikKWlAHzFldcIEiNbTNEL71wQCvt4us-y6mGlHjQT0Edex3ko-L68l9eC9O4WAjXcFV_wEnulmVT51tZVE5Iaf59FGDsnnu26eZ1plihIF8LFC1OfXPghpw5olhD92tKz6w59238--pTMEnX0W-WNnRt-a6OIX3gB5pkF0N3gMeqpUReGRrXSleyXAwei_m4GYvt-xOiBqslrrA0hd54E_kXuLDw_MpKc4l6q43hC4y4P-Gzme3637e4ub3nVj8AOzvT2-cntD5kAYiyxUhKl24fxbiFgjgVOmPyq57FN6x5z09YcEbuL4NDN2f_ckwFU7C9qz7e5GeycDCMlQlZjWSrpS7ACDdbTPl1_uLtvg9DmonEW6ctfOEU_F-nfsW_jWBy13QsYQKVC-YMlnkrpuOg9T6ydG79lw1fxFL3xQOweqAtcnrlms15VW_l5ihdLFoleQDawKxq2d3KUUtlK_7buaaf2zFSiuwjGtmqxaAiAd7xRDTpsz6aSoFdnh-o66YJd1va2zzZPJ7fSnUrP7r0hmhdVb9DRcHroD5pZaGeCl0dyqlLKdtaJ_LEafkQkjoLrSy7nOIpfhQ9KGHaQrfAoHTrDLF9OTIqOy3su-PWUhfEc1MAVev0fmM6q9fqyu87U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bdd7169e.mp4?token=nC5UmsFcqMvPeaY6ECzOcKhxQE6GtIWsFiZDOvikKWlAHzFldcIEiNbTNEL71wQCvt4us-y6mGlHjQT0Edex3ko-L68l9eC9O4WAjXcFV_wEnulmVT51tZVE5Iaf59FGDsnnu26eZ1plihIF8LFC1OfXPghpw5olhD92tKz6w59238--pTMEnX0W-WNnRt-a6OIX3gB5pkF0N3gMeqpUReGRrXSleyXAwei_m4GYvt-xOiBqslrrA0hd54E_kXuLDw_MpKc4l6q43hC4y4P-Gzme3637e4ub3nVj8AOzvT2-cntD5kAYiyxUhKl24fxbiFgjgVOmPyq57FN6x5z09YcEbuL4NDN2f_ckwFU7C9qz7e5GeycDCMlQlZjWSrpS7ACDdbTPl1_uLtvg9DmonEW6ctfOEU_F-nfsW_jWBy13QsYQKVC-YMlnkrpuOg9T6ydG79lw1fxFL3xQOweqAtcnrlms15VW_l5ihdLFoleQDawKxq2d3KUUtlK_7buaaf2zFSiuwjGtmqxaAiAd7xRDTpsz6aSoFdnh-o66YJd1va2zzZPJ7fSnUrP7r0hmhdVb9DRcHroD5pZaGeCl0dyqlLKdtaJ_LEafkQkjoLrSy7nOIpfhQ9KGHaQrfAoHTrDLF9OTIqOy3su-PWUhfEc1MAVev0fmM6q9fqyu87U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم در شب ۲۱۹ کاروان پاراالمپیک را برای بازی‌های آسیایی بدرقه کردند
@Farsna</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farsna/466603" target="_blank">📅 14:16 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466602">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12adc89d93.mp4?token=Uamoi2BdQDQi9u8VVbAQqBCI8EZW4yKA0X5oJbdd-gGRnTMJQoHRtdkgsD8arDBMFuyDe8LOMXD3_ppwKtpxPWPRF-dTFDPMu5qS6VJs9CNyTJEHu6FRNEK83l5lGkZ8Lt6jmjN_8QqrPLAfEu3G_6yPLRSIjF7fZZGBRQjBCVGoWaA6A19Ne_ttmVsII3LnJAqodK6wmAbNkmhsDEKVfbIxdpJmuXCY8zbOTYHPanJjC-BpjuWqXt4fqBHHVr0-H0Daq4HBc6rJGmRdkUyrdnxMGQd_xPrLBBXXchXJJYh-fa_XVY_W1FVEzQcGGjlFnuUhKOGAdL40FFxyskqA5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12adc89d93.mp4?token=Uamoi2BdQDQi9u8VVbAQqBCI8EZW4yKA0X5oJbdd-gGRnTMJQoHRtdkgsD8arDBMFuyDe8LOMXD3_ppwKtpxPWPRF-dTFDPMu5qS6VJs9CNyTJEHu6FRNEK83l5lGkZ8Lt6jmjN_8QqrPLAfEu3G_6yPLRSIjF7fZZGBRQjBCVGoWaA6A19Ne_ttmVsII3LnJAqodK6wmAbNkmhsDEKVfbIxdpJmuXCY8zbOTYHPanJjC-BpjuWqXt4fqBHHVr0-H0Daq4HBc6rJGmRdkUyrdnxMGQd_xPrLBBXXchXJJYh-fa_XVY_W1FVEzQcGGjlFnuUhKOGAdL40FFxyskqA5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت دفاع: ریشه‌کنی نظامی تروریست‌های آمریکایی و شرورهای صهیونیست از منطقه تکمیل خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/466602" target="_blank">📅 13:59 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466601">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDJ2JR3HyVYaHTKvuWxR8qzQ676Ls025RH81m2tJ56ZhahxG_x_kMGGM7lCJTIz7ktm2S7v2Aq9kvU5ULta9kjInvbNsDcDUpe7S8uR-0ieYlSksNV1W0P6fUyYlYnYsZV5OC_exeX0fuAdfdwKDM3r8hVp2anTM5mUny-DxoSwkyFjZAg2fCoXGyZNIMwPKQ3xOZOg_6NkC5WpBRRH9Xku9cHNblsXrxcAZQ6HkWaBOhWxVaDEY0TPFiM2uGG--Djg5n4hv4-pD4EgTu_R5p0t1ql-NmlMoEmzEDLPUSWPdoMySOiphwMCxTISXH8iEhibT3UvF66FY_HXJJGm7Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برندهٔ نوبل فیزیک اعلام شد
🔹
جایزهٔ نوبل فیزیک ۲۰۲۶ به فرانسیس هالزن برای مشارکت در رصدخانه آیس‌کیوب و کشف نوترینوهای پرانرژی کیهانی اعطا شد.
🔹
این دستاورد راه را برای نوع تازه‌ای از اخترشناسی بر پایهٔ مطالعه نوترینوهای کیهانی باز کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/466601" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466600">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X01-U_LFNdbs1uYba8WW9xg_xyAwg7Dw3b0oDLUQrzsP7IA-9tfbNvZuwVm5d_QaL1ECePpbcjFzYPmN1n11e9koRPGt2Xsp6MpmX7BSX6l0fzkQChaCh8crv4OJg8jRb1h7jPVKGrLaosTQ4FtmyE3F7m8ilipHXh5NbHylcQtXFDFU_Qi82m_T2OSwfZ8Fa_65-I-fo-CRXrFpJOnJVFA_V_8svPpBx2a-ImWP7oKI54b8Pk4nGRfAyB22upvpuV9Q4TWXsz1ADESG44aWn6hv2D6lUz_k_gCK05NERLPDoC1QrTzQ4qGuNokapfN4Gl9r1qxctQLuiy5xLeXvQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گام بزرگ بومی‌سازی: تولید لایسنس PVC2 اروند به ۶۰ درصد رسید/صرفه‌جویی ۴۰ میلیون یورویی و خروج از وابستگی خارجی با همت نخبگان صنعت و دانشگاه
🔹
با اعلام مدیرعامل شرکت مهندسی نوآوری و ساخت فن‌آوری‌های نوین خلیج‌فارس، تدوین دانش فنی PDP پتروشیمی اروند به پیشرفت چشمگیر ۶۰ درصدی رسید و به‌زودی نهایی می‌شود.
🔹
این پروژه ملی که توسط نخبگان صنعت و دانشگاه در حال پیگیری است، یکی از مهم‌ترین دستاوردهای خودکفایی در صنعت پتروشیمی کشور به‌شمار می‌رود.
🔹
این موفقیت بزرگ نه‌تنها کشور را از وابستگی به خرید لایسنس‌های خارجی رها کرده و صرفه‌جویی قابل‌توجه ۴۰ میلیون یورویی به همراه داشته، بلکه زمینه صادرات دانش فنی با برند معتبر گروه صنایع پتروشیمی خلیج فارس را نیز فراهم می‌کند.
🔹
بومی‌سازی و تولید لایسنس PVC برای نخستین‌بار در ایران در آستانه نهایی شدن است؛ دستاوردی که ایران را از واردات این فناوری بی‌نیاز می‌کند و گامی مؤثر در مسیر استقلال صنعتی و توسعه پایدار به شمار می‌آید.</div>
<div class="tg-footer">👁️ 7.37K · <a href="https://t.me/farsna/466600" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466599">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromرفاه خبر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sx0GuNSvYSjsyzVoAFfPuEBtKzvrsP8c-D1mL4jtajybfVYX3PNjoC2LLuqqiWR1tMMBMzinMzUdZXb78QMV_AhHTWxVZckkjnjyGNG-oHoYqRJHmEj6l1IpB25wqdNG5pAEr7Za4OXtmotx2HUhXDwLPBgcb-dgi-iiWncht7tiyABM1MbQgF4AHs9cWlMhAR33zPssn85-WsCF3g9s5x5USw2YJdnyPGvkHsXpM5IX9lUx-WNRgn81h2kJTJhI9n5Toai1FM2INEg29SzMNyn2i0UHXX5HB4Csgcxs1qf8kGeFdBTLNrDHrrNlaOzILmVTzTjK3wmRDqiiIrYY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
دکتر للـه‌گانی: بانک رفاه کارگران با ابزارهای نوین تأمین مالی، حامی شرکت‌های دانش‌بنیان است
🔹️
با هدف حمایت از استارت‌آپ‌ها و شرکت‌های دانش‌بنیان، تفاهم‌نامه همکاری بانک رفاه کارگران و شرکت نهادین‌آرمان از شرکت‌های فناور فعال در حوزه نفت‌، گاز، پالایش و پتروشیمی امضاء شد.
🔹️
این تفاهم‌نامه طی مراسمی که روز دوشنبه 13 مهر ماه در محل این بانک برگزار شد به امضای دکتر اسماعیل للـه‌گانی مدیرعامل بانک رفاه و مهندس همتی علمداری رئیس هیئت مدیره این شرکت رسید.
🔹️
مدیرعامل بانک رفاه کارگران طی سخنانی در این مراسم هدف از امضای این تفاهم‌نامه را حمایت از شرکت‌های نوآور اعلام کرد و گفت: این بانک در سال‌های اخیر به روش‌‌های مختلف از این شرکت‌ها حمایت کرده و در راستای ایفای مسئولیت‌های اجتماعی همراه و همیار این شرکت‌ها در پیشبرد برنامه‌های اجرایی بوده است.
🔹️
وی افزود: در مسیر توسعه کشور، پشتیبانی از این شرکت‌ها از اهمیت فراوانی برخوردار است و منجر به بومی‌سازی دانش فنی در صنایع مختلف و قطع وابستگی به واردات می‌شود.
🔗
متن کامل خبر...
#خواهیم_ساخت
#بانک_رفاه_کارگران
@refahkhabar
| بانک رفاه کارگران</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/farsna/466599" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466598">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/farsna/466598" target="_blank">📅 13:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466597">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzt3YDOnH-IJdpWSXmlVahJUfQ0o3JF3BuFrZi4HfhGXjpEeJY4PIA7viYIg5DXovo-u_KZBqERR5_vsWwtR9rB5B-6eJsV8wIKt9eH_eF8rDItfvD_ZVNXjH-hRGyh7dbfQxnuTMfxodPnCqKUbtjyJWdmxf4H0YwJH2JqzaXQETivd4Gjtrt12kZEIEuAdX433axpCpErZyNkWZcji_rYdnIi7qAhLNYaYaPyGkuoRQ3eLrHebn-ff4BsaYsAhiq-s1Li3E4vdgcLwsyNKm-TsLRXH8fDp7x7fq3g7-JMhPwbYDMHmhLSkiTTpCkzgCzcSrQSNbAP7kBDjWCFcHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابت موشک‌های یمنی به ریاض
🔹
منابع محلی از شنیده‌شدن صدای چند انفجار در پایتخت عربستان سعودی خبر دادند.
🔹
رسانه عراقی «نایا» گزارش داد موشک‌های شلیک‌شده توسط نیروهای مسلح یمن، ریاض را هدف قرار داده‌اند.
🔹
به‌گفته این رسانه، انفجارها در محله «المصفاه» در جنوب…</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/farsna/466597" target="_blank">📅 13:44 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466596">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YX-Ih-o3LuUPHgw__r4ETXd045GZvrnO6CTZRNBRo_RoPtBpqyi2m2H-JtZUIOmfSJoFYqn5Xf49U7oX8Xbllf0ZvbdWzwNdpez_rkSW9Kgfhs7ZbXcWGaxXG_kQoEV3eHVe1Ow9Ul-nOButUHyaqIRFBoBVkHT7dTOXxc0ITavzbvTDAs3ai7oygGdLWfCzL90RgwQLAT9Er8KmlJQeR3BJlG0lsWQ5TPdB-l-qXixbc6ufbAeo0uGK6lkHfS2iZTgvftN7q54tkz3KFyDtbqucgPoYDho34MUhDGpIZ5FBPrnT1H_1FXY-Tr10MnHpeAHGsYQXtLuOv0KwTgTvRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن فرودگاه أبها را با موشک بالستیک هدف قرار داد
🔹
نیروهای مسلح یمن طی بیانیه‌ای اعلام کرد که فرودگاه بین‌المللی ابها را با یک موشک بالستیک هدف قرار داده‌ و اصابت این موشک دقیق و مستقیم بوده و به توقف حرکت پروازها در فرودگاه بین‌المللی ابها انجامیده است.
🔹
نیروهای مسلح یمن در ادامه با صدور هشداری به همه شرکت‌های هواپیمایی جهان، از آن‌ها خواست که از ادامه پروازهای خود در آسمان عربستان خودداری کنند.
🔹
در این بیانیه بار دیگر هشدار داده شده که آسمان عربستان به میدان عملیات نظامی نیروهای یمنی تبدیل شده و آسمان مناطق مقدس مکه مکرمه و مدینه منوره از این هشدار مستثنی است.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/farsna/466596" target="_blank">📅 13:39 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-466595">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انهدام باقیماندهٔ تیم‌های تروریستی در سیستان‌وبلوچستان
🔹
روابط عمومی قرارگاه قدس نیروی زمینی سپاه: تیم تروریستی تکفیری که در ترور علمای اهل سنت استان، شهید مولوی یوسف گرگیچ و شهید مولوی محمد انور ریگی و نیز ترور ۲ نفر از نیروهای خدوم فراجا در قطار خنجک زاهدان در ۱۹ شهریور دست داشتند، به‌طور کامل منهدم شد.
🔹
در ادامهٔ شناسایی سایر عناصر و پشتیبانان تیم منهدم‌شدهٔ در منزل‌آب زاهدان، ۲ نفر دیگر از اعضا این تیم دیروز به‌هلاکت رسیدند.
🔹
در مجموع ۸ نفر از این تیم تروریستی به‌هلاکت رسیده و ۴ نفر دیگر نیز دستگیر شدند.
@Farsna</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/farsna/466595" target="_blank">📅 13:39 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
