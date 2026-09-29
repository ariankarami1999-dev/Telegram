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
<img src="https://cdn4.telesco.pe/file/rRy6W8AufzNDyFrtxpqDP6zFzqvpCBS-O9HoYtZBgn6QEBoXSEwfqn9x4vVifIL_XE1JFYNXSXyfPOiaMqmlrXrjFq2B3UIlL7HYKnywPp4rHXXW4D_sA52x626WjCh8hMlKHbYg15Ay8W-xHnAh5FAtv2z1B8Kuwk11j0L8pAxKjPcv4waqGQAWOc7f9byRIGbBfpb_gH21hN12oHtgiY-JAyJfD0XzauWYpo9anXwXtknPqGRRCKxx3Xcs0NDgdPXsARtcoZDxbioDeKOk2v1KFu_lzgGWPBgo-r3wIzL1igCcAQ-pe-mr-30_QjMsKnhJETWxuGEW3BqdR40REw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.32M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-07 23:34:57</div>
<hr>

<div class="tg-post" id="msg-694092">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ایران در وضعیت بسیار بدی قرار دارد و نمی‌دانم که آیا تسلیم خواهند شد یا خیر #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/akhbarefori/694092" target="_blank">📅 23:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694091">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای مضحک ترامپ: ایران در وضعیت بسیار بدی قرار دارد و نمی‌دانم که آیا تسلیم خواهند شد یا خیر
#Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/akhbarefori/694091" target="_blank">📅 23:29 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694090">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9d3b7a17.mp4?token=uv_ZElEpJY6vS845tKeN6CetCBMNxNW_EOAkLFTUWWsK1XMCun9wjO8mzd7YGKvq3AlBG_pIzdX4r3bRip0xPLGDy5uhOe2F1oXN3ZX_-21nmossa4Av02Eou14qX7rEG6DPaYvmI6hYvPaD4kp5BMjje7lyg7kxSD0LUUiYD-txNBhWcX_ov0BeK6qw_wZIZLvuFBXgoPKu1tqfoMWpxWSiB1InabiXXLZVDUHaUIMRB0--yTVdhs1L3zYNae6BvUrZ7TwYkqhKShJxHyLbuSz8r_AbpCZIH8jEKeDIYMW0R3OZMXWkwTnTxi7RECPZpzdCnS7i5UPx9KOr60fVZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9d3b7a17.mp4?token=uv_ZElEpJY6vS845tKeN6CetCBMNxNW_EOAkLFTUWWsK1XMCun9wjO8mzd7YGKvq3AlBG_pIzdX4r3bRip0xPLGDy5uhOe2F1oXN3ZX_-21nmossa4Av02Eou14qX7rEG6DPaYvmI6hYvPaD4kp5BMjje7lyg7kxSD0LUUiYD-txNBhWcX_ov0BeK6qw_wZIZLvuFBXgoPKu1tqfoMWpxWSiB1InabiXXLZVDUHaUIMRB0--yTVdhs1L3zYNae6BvUrZ7TwYkqhKShJxHyLbuSz8r_AbpCZIH8jEKeDIYMW0R3OZMXWkwTnTxi7RECPZpzdCnS7i5UPx9KOr60fVZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تحقیرهای مکرر اروپا توسط ترامپ: اروپا هیچ جایگاهی در صنعت هوش مصنوعی ندارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/akhbarefori/694090" target="_blank">📅 23:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694089">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618ee8acb7.mp4?token=YpX-bEOc3BSr6NFHkT-OPW-RsoEt9ZHrioyRhuN1wjR23i9gUOn02xkZxga8NBMVP4RO6PJTc3lZNFdHl2zFGpY-pDf0JtNilIE1XESE2fka5iLAdLFdyJcBhMhdiyTqnycpu9BCbIZ2CjKdkCFJ0s7pUoz97dAgaXviPVsB9LRr8rt2x8UyJ4MXos8VamMsUP5UBo7XVflEJAdZ0IsRKlMAbSa_7P4eeFRta_2UtZNw0CBJk7f_eVEMmi25Jms3uBcdwP5-KgNCIC98rsqFGG1Gtvu9gkA69SIiXS539rAi9BgVcJW40kW7h5VGIW3JEq3OS2c-d7SVuhBptBav7l6G1BFup6WC8sa80hPOsRmW9eI8_0_jBQRMewW6AboYhgkDLjkrnU1fspdtOy6eWRVN_WyBrVJ0Z9WUEOSR87yLJzjKQxQ1Rc4omaxqTAXI7ufbyewsNEwf7N6pgqrctmAkPzg5AnO_4bco55WQgYCC4c8wlvfdWU-wmdUf7CZEUtWzxS7Hd0Gx1xoO8LmCuBkHTcryLGY22eVTKKzyhh4rXZ06NHODjtUr8WZpS1XJIH2CO8ELw7IT6ER9OuDSOzmEh2Z971hDnxxxQ0qCsdZgj90U2fk7KFg5KmFLhG3XauEPDDFYwBNI52lUWfBD5LJbor-UAWElZFeCa_B1C24" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618ee8acb7.mp4?token=YpX-bEOc3BSr6NFHkT-OPW-RsoEt9ZHrioyRhuN1wjR23i9gUOn02xkZxga8NBMVP4RO6PJTc3lZNFdHl2zFGpY-pDf0JtNilIE1XESE2fka5iLAdLFdyJcBhMhdiyTqnycpu9BCbIZ2CjKdkCFJ0s7pUoz97dAgaXviPVsB9LRr8rt2x8UyJ4MXos8VamMsUP5UBo7XVflEJAdZ0IsRKlMAbSa_7P4eeFRta_2UtZNw0CBJk7f_eVEMmi25Jms3uBcdwP5-KgNCIC98rsqFGG1Gtvu9gkA69SIiXS539rAi9BgVcJW40kW7h5VGIW3JEq3OS2c-d7SVuhBptBav7l6G1BFup6WC8sa80hPOsRmW9eI8_0_jBQRMewW6AboYhgkDLjkrnU1fspdtOy6eWRVN_WyBrVJ0Z9WUEOSR87yLJzjKQxQ1Rc4omaxqTAXI7ufbyewsNEwf7N6pgqrctmAkPzg5AnO_4bco55WQgYCC4c8wlvfdWU-wmdUf7CZEUtWzxS7Hd0Gx1xoO8LmCuBkHTcryLGY22eVTKKzyhh4rXZ06NHODjtUr8WZpS1XJIH2CO8ELw7IT6ER9OuDSOzmEh2Z971hDnxxxQ0qCsdZgj90U2fk7KFg5KmFLhG3XauEPDDFYwBNI52lUWfBD5LJbor-UAWElZFeCa_B1C24" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: پزشکیان گفت می‌خواهم بخشی سخنرانی سازمان ملل را بدون متن و از ذهن خودم بیان کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/694089" target="_blank">📅 23:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694088">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
منابع عربی از شنیده‌ شدن صدای انفجار در اربیل عراق خبر می‌دهند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/akhbarefori/694088" target="_blank">📅 23:14 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694087">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33c102c082.mp4?token=fVORTM8qfjPQo1G5Fnuv7-xWTTpALEq0UnhgM6smCIP8REE5KKGzsDS1A3reQl3a6PPsjzOFdmcaC7xW95h-SZk7F6k2OI37q8CgYftDjTYvSv22XUxyQCr5iOvGhgU4Jvl1spNtAcfpjJuK9GyWjliOpMG3MtZj1fq1hIAu3Xdqn-RoFFbgodjc76X40dK06PT3PQ2UdJysDa-dA8BOuRg2eYp46MUQKrfiJr1kRSt6G43MPx-bBc1tX026Z4H8Mx67UNP6IjNfLWFujLHMMgOTtKvqEN_MGyJkNBplI7R0ispdU7Mj5BYzwsVqe-SV-X4MqvFbLZIb5xlaSvYxhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33c102c082.mp4?token=fVORTM8qfjPQo1G5Fnuv7-xWTTpALEq0UnhgM6smCIP8REE5KKGzsDS1A3reQl3a6PPsjzOFdmcaC7xW95h-SZk7F6k2OI37q8CgYftDjTYvSv22XUxyQCr5iOvGhgU4Jvl1spNtAcfpjJuK9GyWjliOpMG3MtZj1fq1hIAu3Xdqn-RoFFbgodjc76X40dK06PT3PQ2UdJysDa-dA8BOuRg2eYp46MUQKrfiJr1kRSt6G43MPx-bBc1tX026Z4H8Mx67UNP6IjNfLWFujLHMMgOTtKvqEN_MGyJkNBplI7R0ispdU7Mj5BYzwsVqe-SV-X4MqvFbLZIb5xlaSvYxhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نوشابه فقط یه نوشیدنی ساده نیست! هر قوطی می‌تواند حدود ۹ قاشق چای‌خوری شکر وارد بدنتان کند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/akhbarefori/694087" target="_blank">📅 23:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694086">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 1- میدان اول، توبه</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/694086" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح صد میدان خواجه عبدالله انصاری
🔹
میدان اول، توبه
🔹
در لغت توبه (بازگشت) معنی می‌شود؛ یعنی انسان در مسیر سلوک می‌بایست هر لحظه از زندگی دنیوی و زیستن در نفس خارج شود و به زیستن با روح‌ الهی و درک جان بپردازد
🔹
توبه علمی برای زندگی بهتر، حکمت آئینه، خرسندی حصار، امید شفیع، تریاقی بسیار شفادهنده، سالار بار و کلید گنج و شفیع وصال، میانجی و شرط قبول، و سرّ همه شادی می‌باشد
🔹
هرگز دچار نفس و نفسانیات نگردید و هرچه هست را فضلی الهی که نسیب حالتان گشته است در نظر گیرید
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/694086" target="_blank">📅 23:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694085">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ebb31653c.mp4?token=EU9m37Q7I20mzQ-B8oGPXs9h1DeD1bOMGMgK1DRwAx7_XG249vQM9EAENoQyLYHDWZgLPemyJZsU7DmGrM0gBXqhha2Agdzvh9iKZb1MGAtH46L9GHts0RD160MydkP4iWQxNaadxPYk3EhmT2VXId3WBRrcaZMUAtIz6leYQwsdVG1jFlgqlzYCL7wMOJSI6jrusWlQW5VEBNebC26zugzumjkwLwk6P8IU4TFE_uuz9fgbq1ZyxxGZbNxL9_xZxUCHHjutq3WFFv81GkP47SP20u0bv3ZIO5CZwj5AyItOa7y78i2hCXq9l04hyhmBvABDVAnwAOA45fmbGKe07A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ebb31653c.mp4?token=EU9m37Q7I20mzQ-B8oGPXs9h1DeD1bOMGMgK1DRwAx7_XG249vQM9EAENoQyLYHDWZgLPemyJZsU7DmGrM0gBXqhha2Agdzvh9iKZb1MGAtH46L9GHts0RD160MydkP4iWQxNaadxPYk3EhmT2VXId3WBRrcaZMUAtIz6leYQwsdVG1jFlgqlzYCL7wMOJSI6jrusWlQW5VEBNebC26zugzumjkwLwk6P8IU4TFE_uuz9fgbq1ZyxxGZbNxL9_xZxUCHHjutq3WFFv81GkP47SP20u0bv3ZIO5CZwj5AyItOa7y78i2hCXq9l04hyhmBvABDVAnwAOA45fmbGKe07A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه رئیس دفتر رئیس جمهور به افرادی که به وزیر امور خارجه تعرض می‌کنند
🔹
وزیر امور خارجه سفیر و سخنگوی ایران است و رفته تا از حقوق ایران دفاع کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/akhbarefori/694085" target="_blank">📅 22:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694084">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: فاکس‌نیوز را به‌ دلیل این انتخاب کردیم که نزدیک‌ترین رسانه به ترامپ است
🔹
بیش از ۱۰ رسانه بین‌المللی درخواست مصاحبه با رئیس‌جمهور ایران را داشتند و ما ۳ تا را انتخاب کردیم.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/akhbarefori/694084" target="_blank">📅 22:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694083">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
هشدار جدید کشورهای اروپایی برای خروج شهروندانشان از ایران صحت ندارد؛ سفارتخانه‌ها پیام جدیدی صادر نکرده‌اند
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/694083" target="_blank">📅 22:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694082">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1f3f4ad98.mp4?token=RYymt2jyTrrEG3iWUkWH_WnDM5yLzdY7rUUPPfPNK8wnoLl_52iK9WyqIM4bUZ1yKIMYUdoyRU7DpP0Gxyn2RfB9QsSdInby_9yL9byHLNCnczcmbguXAdLcmz1bddt7GdGyzpmYHkz0mSF8hLcVDbGe-RZN6FSFYGQhcAReiJVu49Mfbuw7RLYXNrWogQTmS5zT1bjTfh7IdD_FSXNfviDr3svkV5ROH6-6PNrfQUz5mEBFyLnIXG9BLjfho4BBE6iYhi5aB2UA9ZHZk9Z7gFrzXkalm_qMO0Bjpv3ROJ_hSLhJcABtWS96Mfveibfbq9XLw7hwGEKV3oJUaWkKbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1f3f4ad98.mp4?token=RYymt2jyTrrEG3iWUkWH_WnDM5yLzdY7rUUPPfPNK8wnoLl_52iK9WyqIM4bUZ1yKIMYUdoyRU7DpP0Gxyn2RfB9QsSdInby_9yL9byHLNCnczcmbguXAdLcmz1bddt7GdGyzpmYHkz0mSF8hLcVDbGe-RZN6FSFYGQhcAReiJVu49Mfbuw7RLYXNrWogQTmS5zT1bjTfh7IdD_FSXNfviDr3svkV5ROH6-6PNrfQUz5mEBFyLnIXG9BLjfho4BBE6iYhi5aB2UA9ZHZk9Z7gFrzXkalm_qMO0Bjpv3ROJ_hSLhJcABtWS96Mfveibfbq9XLw7hwGEKV3oJUaWkKbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دستگاهی که به انتخاب مکان مناسب برای ساخت ساختمان‌ها در چین کمک می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/694082" target="_blank">📅 22:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694081">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=cJ9IaxRrP6eJcy2tlI4ePdnxpApY7BWmu4DMeheo4h28hZwkZLhyebTjbppgK9ztjkEXqHPWQlmchbH_EaIW5LqoyXimVKuzZpOyu7Nfp_y1GeA2SbqDMQ-Hm21B4x7HdVHmK5QVIJLpbIIsMmN4QUtOYysHtyhvvdKJ5bHYDxNuGylMcpRNfip4Y0mLDuRYE6eNQf0z6dLsZpjh4JPCoJdO1QIn34ZYFucuTCXlFK6-z7wCjoTx1lOoZOqrfZSDxaSa3Umgv39pQdefYKqn0iCAr4H5_M5uULg5jfadBFBwUjJvRWvNkCLtNYyobf69QmmCo7Yd1Jpb8eGx2uaspQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05abcb121.mp4?token=cJ9IaxRrP6eJcy2tlI4ePdnxpApY7BWmu4DMeheo4h28hZwkZLhyebTjbppgK9ztjkEXqHPWQlmchbH_EaIW5LqoyXimVKuzZpOyu7Nfp_y1GeA2SbqDMQ-Hm21B4x7HdVHmK5QVIJLpbIIsMmN4QUtOYysHtyhvvdKJ5bHYDxNuGylMcpRNfip4Y0mLDuRYE6eNQf0z6dLsZpjh4JPCoJdO1QIn34ZYFucuTCXlFK6-z7wCjoTx1lOoZOqrfZSDxaSa3Umgv39pQdefYKqn0iCAr4H5_M5uULg5jfadBFBwUjJvRWvNkCLtNYyobf69QmmCo7Yd1Jpb8eGx2uaspQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: فاکس‌نیوز را به‌ دلیل این انتخاب کردیم که نزدیک‌ترین رسانه به ترامپ است
🔹
بیش از ۱۰ رسانه بین‌المللی درخواست مصاحبه با رئیس‌جمهور ایران را داشتند و ما ۳ تا را انتخاب کردیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/694081" target="_blank">📅 22:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694080">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf8Jxo5EkhnGTF388oL3c32-Ji29fN1-jg34xXB49tn05L_uSUT2I2UL1ZRo1YZEuUXfh-o5W5UpcwJ_Dz8C2Xl7JfSGYEbjLaODZfMVU6tBNSQQSBbkSxiN6J8OTNS7RTUfQ-Rhevi_LGqb8tQUkaE3N5fe9vjY2SKxG9qrtns4bZMpVupIQFrz2pjVx0GHdoEYSO7teYhJx8J-dPBNHcxWevF1EquCwxAh362h6c9i4q6V-h50RTgVSXw0zWiOmeP6U20W37E-Yv8JnbWbg6saIql9wuZmoH0hZrOLQLuzVNgDqs1FgchXliKfXrpYbXQcS5nCHu-8pU5yxEPKpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیانیه وزارت امور خارجه درباره محکومیت حضور فتنه‌انگیز نخست‌وزیر کودک‌کش رژیم صهیونیستی در منطقه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/694080" target="_blank">📅 22:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694079">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1670e8c287.mp4?token=T3MxlLnHe_Ha_4la07PlCkEXjNQUDBuRV6JvHoEopuSCs1p-LfOeWFKe0qdrz0Jq_wu8VDpf86wNrA0MIUeE9lB9WQChjW2RZLLczqrkP32szxZFkJGhehbHKAOE_ucEgVjfFS3QI6yKfoDbQ4cCrr9oh4iLfL4JNSfdXTf917F46Ed2ZfqAI0b9Yn_P-mcYv2MzN2NvfgIsSDP2NrNDTMVkfFURzHSr9ncKJDZFaToXqWXuY7SD8-1shqlvN1vxFIFzeplqJ1wGqQ6lVf0u7IVpi54JRcYHjmbVEZZNE2ZbTT1uxlzHcksXB4RfMGLfUGI2byOqZYVUO-JGdTgWdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1670e8c287.mp4?token=T3MxlLnHe_Ha_4la07PlCkEXjNQUDBuRV6JvHoEopuSCs1p-LfOeWFKe0qdrz0Jq_wu8VDpf86wNrA0MIUeE9lB9WQChjW2RZLLczqrkP32szxZFkJGhehbHKAOE_ucEgVjfFS3QI6yKfoDbQ4cCrr9oh4iLfL4JNSfdXTf917F46Ed2ZfqAI0b9Yn_P-mcYv2MzN2NvfgIsSDP2NrNDTMVkfFURzHSr9ncKJDZFaToXqWXuY7SD8-1shqlvN1vxFIFzeplqJ1wGqQ6lVf0u7IVpi54JRcYHjmbVEZZNE2ZbTT1uxlzHcksXB4RfMGLfUGI2byOqZYVUO-JGdTgWdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نصیحت طلایی درباره ازدواج؛ فقط یک مجرد شاد می‌تونه یک ازدواج شاد داشته باشه و یک متاهل شاد باشه...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/694079" target="_blank">📅 22:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694078">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f8f25764e.mp4?token=m3zN7h-kCy9uihesVao2gxB0Z8uSe67LkGrjE0cwnmfzDuffDEMIwDjDWkPD1eggto4FkANT6--Fwh2ILI5Xr9AqxoNAsDFv_Trlcd_VyYvbANG848QtCQfumJxK-BktC1cPvzUS1JG5HrPYRyQSax1P_o0WVJhZ_c1xaA2dCnHCY7fagkK3ADUAC4uay604ZIb9z4e6bKk9P0UwsnMKqLujvOhx8Dp3rnTVHDZatjCgtc0G1Yppdh4xwN9yQvbZujpfCW0I7uwPZbzn7MWMpETezAYOmzDLhbW5GKXjZWo2wdo-o293Z62_JeEAN0hUx_NyYoejRIScRy5q9gw26g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f8f25764e.mp4?token=m3zN7h-kCy9uihesVao2gxB0Z8uSe67LkGrjE0cwnmfzDuffDEMIwDjDWkPD1eggto4FkANT6--Fwh2ILI5Xr9AqxoNAsDFv_Trlcd_VyYvbANG848QtCQfumJxK-BktC1cPvzUS1JG5HrPYRyQSax1P_o0WVJhZ_c1xaA2dCnHCY7fagkK3ADUAC4uay604ZIb9z4e6bKk9P0UwsnMKqLujvOhx8Dp3rnTVHDZatjCgtc0G1Yppdh4xwN9yQvbZujpfCW0I7uwPZbzn7MWMpETezAYOmzDLhbW5GKXjZWo2wdo-o293Z62_JeEAN0hUx_NyYoejRIScRy5q9gw26g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس دفتر رئیس‌جمهور: آمریکا روادید سفر به نیویورک را تا دو شب قبل از سفر صادر نکرد و ما مطمئن نبودیم که ویزاها خواهد آمد یا خیر
🔹
بصورت آگاهانه تمام تیم رسانه‌ای و ارتباطی حذف شده بود و به هیچکدام ویزا نداده بودند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/694078" target="_blank">📅 22:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694077">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
فایننشال تایمز: میانجی‌ها در حال پیشبرد یک توافق موقت میان ایران و آمریکا هستند که هدف آن بازگشایی تنگه هرمز و از سرگیری مذاکرات برای پایان دادن به جنگ است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/akhbarefori/694077" target="_blank">📅 22:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694076">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4017be95.mp4?token=mDzdNL6IPEg5dTy67GhfirbCViX06IwCeITFVCE7rUVuih00fqZKQwtjSDxSehZfQf7iFTy_wWMCtpbxyiPJIe5pU-Aw0BsYnDXcDs2XuiGYXlaodgIERJPCaG1aSF8cRtiVv1wB-gkr7CmT9oDE0GeFvhpyPH2-zYjDIznGLLuyMHNLD2pPYNpTVBRKjdOvuY1-o4wOlgonUCge9CwGVYljEx4XUCWykJhCueJbZi9eoOeDyvJ9TuNA785NUkE91YXD_O9IpsVyij--mXugA1-0tJ_hIppPVTVlIdD5CHgjRvewS8egpaGi28KbsRIA48ipuiT990A7SDzJRgtBNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4017be95.mp4?token=mDzdNL6IPEg5dTy67GhfirbCViX06IwCeITFVCE7rUVuih00fqZKQwtjSDxSehZfQf7iFTy_wWMCtpbxyiPJIe5pU-Aw0BsYnDXcDs2XuiGYXlaodgIERJPCaG1aSF8cRtiVv1wB-gkr7CmT9oDE0GeFvhpyPH2-zYjDIznGLLuyMHNLD2pPYNpTVBRKjdOvuY1-o4wOlgonUCge9CwGVYljEx4XUCWykJhCueJbZi9eoOeDyvJ9TuNA785NUkE91YXD_O9IpsVyij--mXugA1-0tJ_hIppPVTVlIdD5CHgjRvewS8egpaGi28KbsRIA48ipuiT990A7SDzJRgtBNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عجیب و شگفت‌انگیز مثل لوت
🏜
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/694076" target="_blank">📅 22:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD4PfGQ_Eqe5kLyUWk6emQag75VN517alhypzc-uwN8O6toQWaD7c7JQxiW_MiRInL1kcAgR2YOju1Ql9uhHXR2qpXifdaxZukvvBJFoIBaJb1XXCwkl1aDJ1TXcuM5rnkriN-bAGH0RssYekqLkWk5j5uxEA6w-WCSBzx0sPJE5GHgSjHoiB7bE3mV6Ra_KfUG7NLYESGcvT8mT9M3yEH7pjGVNG6Pm7RYjhQatkMUhca9NsWpiXt8Owprt2OM_srqjSB8kyB5GeUnQS1FdXve2S6fYg5ffmgORoYTWkPJ-8nPCZxkxKfZ4nyQD2QM3XL8nEZcq0tSy2aazxt3ZGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
برای خرید بیمه شخص ثالث، بیمه بازار داره!
همیشه تمدید
بیمه ثالث
برام یه دغدغه بود، اما این بار تصمیم گرفتم برم
بازارش
چون :
✅
می‌خواستم همه‌ شرکت‌ها رو با هم
مقایسه
کنم و مناسب ترین انتخاب رو داشته باشم.
✅
همه چیز خیلی سریع پیش رفت؛
هم بیمه‌م
فوری صادر
شد
✅
و هم چون امکان
پرداخت ۱۱ قسطی
داشت، خیالم از بابت پرداخت هزینه‌ش هم راحت شد.
👈
تمدید بیمه ثالث از بیمه بازار
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/694075" target="_blank">📅 22:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/694074" target="_blank">📅 21:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694073">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6f8cbbdd.mp4?token=OcdDuR_5aG5131lMOiyBxShY5jInMIBl2ato3Dcm4CIcqu4okZq6Eyzf04Hq5UtpL9hbdWNRpHCltjrzdgw5Cng4SYj1bjJs7Vj-XwbKLDgjMkkpzHVKWb7DCpcu6ClNMsx0CHZjlPBfnT2fDtPDb8rXlINi1LGISQ-VRnIaCI4xPLn0ncyjN7knzK4R_LfezpoUNvepNaHgnOqImKOe5nhLnUa9Hx3ouWW9KOaUXlBKqODngRpLR0IKEVD44Ah2RFRh5g-HyJJZ4V8WA-nUzgSoscLxa7Vb7xwRzeMHuVXjpbAmpAkzlfZ8gVN6NfbTtW-0FNUktSuShtlRu74YG2UMi_9kakzlLrDoORmEbai-avTIiiXGx7jmL8mHIm2SOBqaxnDPNu8WxdFhlLDF8c8el3qqZZFqLi2CzKGDq_To0r6cEGTN04WwLAon9iNVBGlOGldTAxUtdygVyZ4XuyCzxoZw1w_9r6I0XNpSr-R5_7rJOBiYMMviYT9mgKJSs9JmZelQiVV59Zl1V2c-oprAm3DOVH7vGggGUGe5KZcftdAX6itIDH3asp8y61m2-7TMDDDHtZ1KlAcRCwvf9DdQI2pr06g1jec9AeOUc_IKmI9XsRM_AaFdCBHY5ELfgR6JX8yDD5hmukh4GAm4ax8x1sOtXzkNSFASo-DbRJM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6f8cbbdd.mp4?token=OcdDuR_5aG5131lMOiyBxShY5jInMIBl2ato3Dcm4CIcqu4okZq6Eyzf04Hq5UtpL9hbdWNRpHCltjrzdgw5Cng4SYj1bjJs7Vj-XwbKLDgjMkkpzHVKWb7DCpcu6ClNMsx0CHZjlPBfnT2fDtPDb8rXlINi1LGISQ-VRnIaCI4xPLn0ncyjN7knzK4R_LfezpoUNvepNaHgnOqImKOe5nhLnUa9Hx3ouWW9KOaUXlBKqODngRpLR0IKEVD44Ah2RFRh5g-HyJJZ4V8WA-nUzgSoscLxa7Vb7xwRzeMHuVXjpbAmpAkzlfZ8gVN6NfbTtW-0FNUktSuShtlRu74YG2UMi_9kakzlLrDoORmEbai-avTIiiXGx7jmL8mHIm2SOBqaxnDPNu8WxdFhlLDF8c8el3qqZZFqLi2CzKGDq_To0r6cEGTN04WwLAon9iNVBGlOGldTAxUtdygVyZ4XuyCzxoZw1w_9r6I0XNpSr-R5_7rJOBiYMMviYT9mgKJSs9JmZelQiVV59Zl1V2c-oprAm3DOVH7vGggGUGe5KZcftdAX6itIDH3asp8y61m2-7TMDDDHtZ1KlAcRCwvf9DdQI2pr06g1jec9AeOUc_IKmI9XsRM_AaFdCBHY5ELfgR6JX8yDD5hmukh4GAm4ax8x1sOtXzkNSFASo-DbRJM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا ساخت بمب اتم جلوی جنگ را می‌گیرد؟/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/694073" target="_blank">📅 21:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694072">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
انفجار غیرعادی در ملارد رخ نداده است؛ مهمات عمل نکرده دشمن در حال خنثی سازی است
🔹
صدای انفجارهایی که امشب در برخی از نقاط شهرستان ملارد شنیده شد و ادامه هم دارد مربوط به عملیات فنی انهدام مهمات عمل‌نکرده است و هیچ‌گونه حادثه یا وضعیت غیرعادی در منطقه رخ نداده است.
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/694072" target="_blank">📅 21:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694071">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
تیراندازی در ایرانشهر؛ مقابله پلیس با سارقان مسلح
🔹
نیروهای انتظامی در جریان این عملیات با سارقان مسلح درگیر شده‌اند و این افراد در دام نیروهای فراجا گرفتار شده‌اند./ تسنیم  #اخبار_سیستان_و_بلوچستان در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/694071" target="_blank">📅 21:41 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694070">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLj6hHBc24VoVdAdgFtgKRj8EDNo_WpEJdp4NHCwJEYsS5rk0YPDphrqp-HSEZTwWt5eeubOcRS0yCSMQeq2sXa_KG7nCCeEnezj2_rmRqq5KqczY-e5EFEiXeSaLSse7RrsKdcL1eBbRpH5nTbISrEpcCQcfmsRCOlbHj4J2hJ_NYWgfHj_SxFvR66oNlH8MvUGUFe0LYExTC6MiFQdE96GiS1PWVUJ9gNqDtzc7_PX5MMwCYN-abl8dqQb5Q6BWAMcDpAaKKIJITam6BACWcws-u50tpDbPANYuUucM2wvJ6E5kqJ_oYHEjZTmnI7YjOoQDLuWg4FUncKyt1bocg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عرضه
اسکناس ۱۰۰ هزار تومانی با طرح مدرسه میناب به بازار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/694070" target="_blank">📅 21:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694069">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bJ6cYd66e9DfY17iPeK86lrjH_0h1eBbUZP-HqM2Qhs3w2_jD4fGQF3pIfG3jXYCkDs9YEGixvToo0bnbZ2HZTAX2a2AE3eyoHhggQvJ0l2j-0vzCJ-kc1Qe2QZtP737OCZmG3RvcdhiTKFzqrZZoRTsmbWBlx2C2cTucy6MIDJ3ZVR8vbGGe_tVAAt22t_7vl8k8X7Tt37Hob4L3spyuEmlB2CXyFe8cFi6FuWhfUF4stZp7jLeG_TSAstDbPRguRzRtF2O-1cJKvM9C0ossbQ-x6Oz_jGyk5pqzzGXe-wkOgLrcb5IKRMulo8U_8kBFGEqfq-mfIEKE9SriGUxtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چهرۀ درهم امیر قلعه‌نویی در جریان دیدار ایران - روسیه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/694069" target="_blank">📅 21:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694068">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
نخست وزیر قطر: ایران همسایه ما بوده و برای همیشه همسایه ما باقی خواهد ماند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/694068" target="_blank">📅 21:30 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694066">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
پزشکیان: [در خصوص لغو پروازها] ترامپ از آن سوی دنیا تهدید می‌کند و دستور می‌دهد و برخی از کشورها هم به دستور او گوش می‌دهند؛ همه کشورها به فکر منافع خود هستند
🔹
عراق، افغانستان، پاکستان، آذربایجان و دیگر کشورهای دوست و همسایه به ما کمک می‌کنند اما محاسبات خود را هم دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/akhbarefori/694066" target="_blank">📅 21:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694065">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ifWYWBr4wrcA6ac-id32A7mY3b8xWMhq145gOycywvPnr_txR5LEIMWxTevhnWTpv8pRjox4tm0ec-vtx3dAd_u-mprOioZeXHNMXlABP6eDKrxRi-gKjilSiK4wzASzg3Pcrzw1gaXjiY-6GmCtILLa8gscS80ZK2RnP3lovMB7NA5HgKMOmyqF-YgAveGkXRVjvn97KJzSWcXpVyyEHS6PukSa0FEQHc6IRwScunoX8X0VST_-MTSLAJwNdcRF_JzFzMa0E0Os1mGPC3Wn58UMzudvtpqcdEEqKvDiqS9OkFAn6lJCa7A6GtPuMYNQBdAQa5-tA7_ctvI9bnSR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هیچ مجوزی برای کشتار و عرضه گوشت اسب، قاطر و الاغ صادر نشده
سرپرست معاونت بهداشت سازمان دامپزشکی:
🔹
تاکنون هیچ مجوز یا موافقتی در زمینه صدور مجوز برای کشتار و عرضه گوشت تک‌سمیان، از جمله اسب، الاغ و استر، صادر نشده و موضوع صرفا در حد یک درخواست اولیه از سوی برخی اقلیت‌های دینی در تعدادی از استان‌ها مطرح شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/694065" target="_blank">📅 21:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694064">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
داشتن گوشی هوشمند در ۱۲ سالگی می‌تواند به اختلالات خوردن منجر شود
🔹
پژوهش محققان روی نزدیک به ۹ هزار نوجوان آمریکایی نشان می‌دهد کودکانی که در ۱۲ سالگی گوشی هوشمند شخصی داشتند، دو سال بعد بیشتر از همسالان خود علائم اختلالات خوردن را گزارش کردند.
🔹
علائم بررسی‌ شده شامل پرخوری، اختلال در خواب و تلاش برای کنترل وزن از طریق روش‌های مضر مانند استفراغ عمدی یا ورزش طاقت‌فرسا بود./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/694064" target="_blank">📅 21:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694063">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خبرگزاری رسمی امارات، سفر نتانیاهو به ابوظبی را تائید کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/694063" target="_blank">📅 21:21 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694062">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eebb7f141a.mp4?token=PSsWvYa3yZZpKP6pIpDWx4CVUDYtbIIXPabMnmyQiedblT7pHV40YZx1yHAOdC873A8gMiomaG-xRDYjb80cDmFi4zwMF31BxrXiPPoILnKrb2WQ5-X3xqzUyKabr6osnMwuWaIZ4pxwSyp7nDBBQx301MZCBterjP9QbDMtuKFH2k1XwUyH8CogLbH6TsAlcU8Tl8Y51jjt6FkA9JtYSyFrJ-b3bDajdw1y2GFku81mb0vRAm9oH5deWkUDjeJ7dr_LffBF9uB3q3RlFSvwUKhv-8nyhFatjwhzIvBOw4qVf79E1g1QEWyCuGDeS8Glu6UBI1PPuHD0MDliHQF3Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eebb7f141a.mp4?token=PSsWvYa3yZZpKP6pIpDWx4CVUDYtbIIXPabMnmyQiedblT7pHV40YZx1yHAOdC873A8gMiomaG-xRDYjb80cDmFi4zwMF31BxrXiPPoILnKrb2WQ5-X3xqzUyKabr6osnMwuWaIZ4pxwSyp7nDBBQx301MZCBterjP9QbDMtuKFH2k1XwUyH8CogLbH6TsAlcU8Tl8Y51jjt6FkA9JtYSyFrJ-b3bDajdw1y2GFku81mb0vRAm9oH5deWkUDjeJ7dr_LffBF9uB3q3RlFSvwUKhv-8nyhFatjwhzIvBOw4qVf79E1g1QEWyCuGDeS8Glu6UBI1PPuHD0MDliHQF3Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آسون‌‌ترین و کاربردی‌ترین هوش مصنوعی‌ها رو یک جا براتون جمع کردم!
#هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/694062" target="_blank">📅 21:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694061">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/873fd74c39.mp4?token=duL7mSoz53oQr6ZKQD-TrP5RDF0wcWJr_LkTRslAZh8rQLBJo36lJK06OTLe7aq_6vT0bAaaxniLRBQ6FWXs75H2-EQDEtBvWkDHM4lj8m92uiDIoq7CEtUeE1PuRkEh6yogyZL4cCacY0305nWK4qF5MRi9oDONYMGSUP15MEb6fnUhXnPNI-gIOE50mb4xKF80Ap_o_c7rh2tBqH4ZbObKlDexgpVnZAP0TN33Q0FHPYA4MdpDBLsWzS3XFfOvs5rdfpiB2Pf64B_agSF-l7vFxLWjzZTNZocNfiCSO1SGg2jN5dH_PZgTsA1_htaz9VqZTQMme7H_OQap8wst5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/873fd74c39.mp4?token=duL7mSoz53oQr6ZKQD-TrP5RDF0wcWJr_LkTRslAZh8rQLBJo36lJK06OTLe7aq_6vT0bAaaxniLRBQ6FWXs75H2-EQDEtBvWkDHM4lj8m92uiDIoq7CEtUeE1PuRkEh6yogyZL4cCacY0305nWK4qF5MRi9oDONYMGSUP15MEb6fnUhXnPNI-gIOE50mb4xKF80Ap_o_c7rh2tBqH4ZbObKlDexgpVnZAP0TN33Q0FHPYA4MdpDBLsWzS3XFfOvs5rdfpiB2Pf64B_agSF-l7vFxLWjzZTNZocNfiCSO1SGg2jN5dH_PZgTsA1_htaz9VqZTQMme7H_OQap8wst5jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سوال از وزیر راه چطور سر از صحن علنی درآورد؟/ گلایه نماینده الیگودرز از رییس کمیسیون عمران
🔹
بنا بر اظهارات حمیدرضا گودرزی نماینده الیگودرز؛ سوال از وزیر راه و شهرسازی بر اساس آیین نامه داخلی مجلس، نباید در جلسه علنی امروز مجلس مطرح می‌شد. این سوال شش ماه پیش در کمیسیون عمران مطرح شده و بدون آنکه برای آن رای‌گیری شود؛ امروز در دستور کار صحن علنی قرار گرفت!
🔹
سخنان گلایه‌آمیز گودرزی در انتقاد از عملکرد خلاف قانون کمیسیون عمران و گلایه از رضایی کوچی رییس این کمیسیون را بشنوید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/694061" target="_blank">📅 21:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694060">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
جمهوری آذربایجان استفاده از خاکش برای حمله به ایران را تکذیب کرد
/ تسنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/694060" target="_blank">📅 21:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694059">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df685498c4.mp4?token=EmlkuC0DfvoNs1Z2xvVHQ0mfSt0ow0w0QoaBLNtjc_vhsHbJX06yCk2xOSrdhapM-uSgZ7Qevcfs3KrF2sSNAoB-HRewnf5fvn_NLDyq6-1eewI7ZZj1MM2GoLBKsnibCF7qr8CgBZAEOWWkKjm0RuLjoU4Z6eCpvCV1QNthshdFYdwYRuiuSn2-OehQVdFjSur19E62fCEi-fnnMcVCeNvgAhkM42Rouxq7YEWqNeBpMn5zCAfZtdCZdfFFs6fB79sEJ8S5erooEViMxyFuFoWHrmf2CqXSmRLpz8q1JNqAiGMIURcM4DZ9MiwKwsBhjfh0QvGL9NclQCQeDpKspQktxJpvsB2msNGW8x4hirQicCYoyeMlQ2G3Kwy-m6sLAsK0owKzUP9-iv5hVTskpS1m30nTdLJc-CoiIvSN2i3mQ6FPpbr0HllxFAfDmDuJ0UliIhRMtNDpjeeY4Fef3VUhzdzhBXnuWweTOp_9aaoxgnIM9muVFxwKt9zmTrvx-IHSF9_SCtAXqscL9TnEHRqZJbjoIX1i6oyt02sA9SFKDiHxOmfMWa5KsMFNZEl9Wl3QEegXjIER6RLL4RbuGNri4j6YBCfwRt9S03c4ngyLOzhdrmbAnPyo6sEJRrHz20QQ-NBzYDdkUMCV1mDBgaW2sUxAECrzfH8TYsfDhY0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df685498c4.mp4?token=EmlkuC0DfvoNs1Z2xvVHQ0mfSt0ow0w0QoaBLNtjc_vhsHbJX06yCk2xOSrdhapM-uSgZ7Qevcfs3KrF2sSNAoB-HRewnf5fvn_NLDyq6-1eewI7ZZj1MM2GoLBKsnibCF7qr8CgBZAEOWWkKjm0RuLjoU4Z6eCpvCV1QNthshdFYdwYRuiuSn2-OehQVdFjSur19E62fCEi-fnnMcVCeNvgAhkM42Rouxq7YEWqNeBpMn5zCAfZtdCZdfFFs6fB79sEJ8S5erooEViMxyFuFoWHrmf2CqXSmRLpz8q1JNqAiGMIURcM4DZ9MiwKwsBhjfh0QvGL9NclQCQeDpKspQktxJpvsB2msNGW8x4hirQicCYoyeMlQ2G3Kwy-m6sLAsK0owKzUP9-iv5hVTskpS1m30nTdLJc-CoiIvSN2i3mQ6FPpbr0HllxFAfDmDuJ0UliIhRMtNDpjeeY4Fef3VUhzdzhBXnuWweTOp_9aaoxgnIM9muVFxwKt9zmTrvx-IHSF9_SCtAXqscL9TnEHRqZJbjoIX1i6oyt02sA9SFKDiHxOmfMWa5KsMFNZEl9Wl3QEegXjIER6RLL4RbuGNri4j6YBCfwRt9S03c4ngyLOzhdrmbAnPyo6sEJRrHz20QQ-NBzYDdkUMCV1mDBgaW2sUxAECrzfH8TYsfDhY0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یزدان‌پناه عضو تیم رسانه‌ای قالیباف: کسانی که کمپین نه به اعدام راه می‌اندازند با کسانی که می‌گویند چرا رسایی به زندان رفته است چه فرقی دارد؟ دادگاه جمهوری‌ اسلامی‌ پرونده‌ای را بررسی و حکم صادر کرده است همه باید از آن تبعیت کنیم
🔹
رسایی بجای اصلاح سخن اشتباه خود و تمکین از رای دادگاه‌ جمهوری اسلامی، مقابل قانون گردن‌کشی کرد؛ گفت نه شرمنده‌ام و نه عذرخواهی می‌کنم! و وقتی هم حکم حبس او صادر شد گفت دادگاه رأی سياسی صادر کرده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/akhbarefori/694059" target="_blank">📅 21:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694058">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162161cf0b.mp4?token=AL972-nQfr2LpwAgJZ6fcfCkhVtKG8xxwL7GSLBQhG_0yfa9QynS1B7GHwN6nB_xF88tzBjMm1BE6XMyEB95BJy3ErYuJR8oPIfcWhXvFCUt0jBN67zxHVc1jAaZKOu0U1F1nZcRP5jpNEZm0gBfs7t4QSDa19nJsYBZHMzhiyadPh3JgaB2t4A8JshVSUjcfpafKZArViI3PWVVHowcNGNBkXOQxh4gJ1O0y__8XiVOJQVenrp0zqKB9b5taX3qczZxjzk6RRvOuxIMlKD5CT-H8hdfb0i6V-4xGeyT3dPywBG_SSMjuyu1SBf8X7pb8AEbkQV8mYAJh3eHVxUD8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162161cf0b.mp4?token=AL972-nQfr2LpwAgJZ6fcfCkhVtKG8xxwL7GSLBQhG_0yfa9QynS1B7GHwN6nB_xF88tzBjMm1BE6XMyEB95BJy3ErYuJR8oPIfcWhXvFCUt0jBN67zxHVc1jAaZKOu0U1F1nZcRP5jpNEZm0gBfs7t4QSDa19nJsYBZHMzhiyadPh3JgaB2t4A8JshVSUjcfpafKZArViI3PWVVHowcNGNBkXOQxh4gJ1O0y__8XiVOJQVenrp0zqKB9b5taX3qczZxjzk6RRvOuxIMlKD5CT-H8hdfb0i6V-4xGeyT3dPywBG_SSMjuyu1SBf8X7pb8AEbkQV8mYAJh3eHVxUD8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل دوم روسیه به ایران
🔹
روسیه ۲ _  ایران ۰
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/akhbarefori/694058" target="_blank">📅 21:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694057">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f256c543aa.mp4?token=rwNjKRmwIz7tURkL6-dO6140rK02rg--kZyf4CvMFvBwFYooHvvD0mtDa_OX8s1hXBhVm6HCMD3CML7HYtmw65eVOU9oCLHfi55mli1Lx8s--_3jDsz6CuXxIDUviWa6CKzWSmpEVhbA2uNu7DBTQQM-TTxArPnOA6_vTUNDYnk10tm6VeNBy32_tx37XiY6Yv4P0IS0H1UOk-xiMocjpRt486_UU8tAYaP7aKsLXdyDxl00UQrl3xTmNQgSVaublNjnN0jM66eotWfthBWj9TAdOkQYX1JqgVJ2KMKAU_Xe_zBhAWljph8nZXf6enEqmGfBd0x0be0FOvIkSxObHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f256c543aa.mp4?token=rwNjKRmwIz7tURkL6-dO6140rK02rg--kZyf4CvMFvBwFYooHvvD0mtDa_OX8s1hXBhVm6HCMD3CML7HYtmw65eVOU9oCLHfi55mli1Lx8s--_3jDsz6CuXxIDUviWa6CKzWSmpEVhbA2uNu7DBTQQM-TTxArPnOA6_vTUNDYnk10tm6VeNBy32_tx37XiY6Yv4P0IS0H1UOk-xiMocjpRt486_UU8tAYaP7aKsLXdyDxl00UQrl3xTmNQgSVaublNjnN0jM66eotWfthBWj9TAdOkQYX1JqgVJ2KMKAU_Xe_zBhAWljph8nZXf6enEqmGfBd0x0be0FOvIkSxObHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخست وزیر قطر: ایران همسایه ما بوده و برای همیشه همسایه ما باقی خواهد ماند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/694057" target="_blank">📅 21:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694056">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
ادعای دروغ اینترنشنال درباره تجمع دانشجویان دانشگاه علامه
🔹
رسانه ضدایرانی اینترنشال کلیپی قدیمی را به عنوان تجمع امروز دانشجویان دانشگاه علامه منتشر کرده است. این کلیپ هیچ ارتباطی با تجمع امروز نداشته است.
🔹
این تجمع در حیاط دانشگاه برگزار شده و عمدتاً شعارهای…</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/694056" target="_blank">📅 21:05 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694055">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeBvO2qEgkauYCt6L5YY2D_bw7FuvQgb9IC4_JhQFHuBaYBrlutNCnQphMY8BNkh5eV79poCWrTkGmPyitV-LwUBSlIoEeACiqeBomkxOt2QHc3aZu7FcwsLx8qVzedAOTNno1uhE3bJkMZGL0pAMFwRoZ3hR9VwfJO2Bvg-AyGrOsa-Rv2TtplyUgqxSZa-N3Uikym2HEVPvsp4CwEfZ726tyy4IBsVhkhbsvDXS2pcsmyEQibCrhhzXZpD4OjE_wlMlYkYRIIZUKIN3IqbnlsUOtAu7Lb8AC1hL_7Xz1HJ-82x3JH3dxuMMfyxEjGJSPjfO8qTGCKjz_uaS39T-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقت دنبال کردن همه خبرها را ندارید؟
لازم نیست بین ده‌ها کانال و سایت دنبال خبرهای مهم بگردید.
📲
«خبرفوری» مهم‌ترین و فوری‌ترین خبرهای روز را با پیامک مستقیم برای شما ارسال می‌کند.
✅
سریع
✅
خلاصه
✅
بدون نیاز به اینترنت
👇
مشاهده شرایط عضویت:
http://mediarise.ir/sms-news</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694055" target="_blank">📅 20:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694054">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/151c442d45.mp4?token=c0l6kdksHtdMWg6Q5n81lbDMrdWfMFvSreuK1iXhlXB4SxVNXtLpJBibDz8dewb54YZthSFvD0agiZBEWKDmtv9MmOv6MqB2CGI9h_xdc63TQqitfYj-EUDtOAmazoStZ5EyAyf-PHeJSQpdZdb2I7MWQ6OE4gpi49F7S_lKAbXeBzWBKabsSdwvEIVqXLb5QneS3QaYle-lkiQYkZAGtDZ2F9OLV_6EeCSy02tm10Tf8Wf2qAjzq_NgdoyKZB8KUdf-9x3vIlnJ2JuD4bbIKIlCb5mjj1Uuddr0iu9LgXLn71Qz_3SKc4cVUkBPCYj5cmqKLO_26HPU5-JARURWcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/151c442d45.mp4?token=c0l6kdksHtdMWg6Q5n81lbDMrdWfMFvSreuK1iXhlXB4SxVNXtLpJBibDz8dewb54YZthSFvD0agiZBEWKDmtv9MmOv6MqB2CGI9h_xdc63TQqitfYj-EUDtOAmazoStZ5EyAyf-PHeJSQpdZdb2I7MWQ6OE4gpi49F7S_lKAbXeBzWBKabsSdwvEIVqXLb5QneS3QaYle-lkiQYkZAGtDZ2F9OLV_6EeCSy02tm10Tf8Wf2qAjzq_NgdoyKZB8KUdf-9x3vIlnJ2JuD4bbIKIlCb5mjj1Uuddr0iu9LgXLn71Qz_3SKc4cVUkBPCYj5cmqKLO_26HPU5-JARURWcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش نظامی جان‌فدا در میدان امام حسین جریان دارد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/694054" target="_blank">📅 20:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694053">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecf4b39e63.mp4?token=kAOrdDc3Z_xmJ0S-UmPXD2wzvb7L5Owp1kTsYMJlKcA_aX2zPkiD9zn11vFeNmbfzeqd-FnuS4CqaXV7XNOIqXRGyNKj36n3V1akB0o-MdjdWYxyganwI5R_487HAkc3c_9d-63guNDK-h7llu28WVfpUn07JLYaYwSDWKo9LAPv0KJ_LOTvldLNUXbC4a0emqMZxbdJj10nIZIKA8tgZfBmCJd6OGcSQsyG8ZZIwpmHiPgJgzOjAy-s7PA_i511MzzHJ18WleqLV0xyfJ0EizMLYmvMQGqoEQq3MgvMlpq4iWVvQ5DhQ5i8TeXIy-E5IWwJj9ISxEeMri1Ez3vWiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecf4b39e63.mp4?token=kAOrdDc3Z_xmJ0S-UmPXD2wzvb7L5Owp1kTsYMJlKcA_aX2zPkiD9zn11vFeNmbfzeqd-FnuS4CqaXV7XNOIqXRGyNKj36n3V1akB0o-MdjdWYxyganwI5R_487HAkc3c_9d-63guNDK-h7llu28WVfpUn07JLYaYwSDWKo9LAPv0KJ_LOTvldLNUXbC4a0emqMZxbdJj10nIZIKA8tgZfBmCJd6OGcSQsyG8ZZIwpmHiPgJgzOjAy-s7PA_i511MzzHJ18WleqLV0xyfJ0EizMLYmvMQGqoEQq3MgvMlpq4iWVvQ5DhQ5i8TeXIy-E5IWwJj9ISxEeMri1Ez3vWiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اظهارات وقیحانه ونس: ایرانی ها با شلیک به کشتی ها مرتکب اشتباه بزرگی شدند و توافق را نقص کردند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/694053" target="_blank">📅 20:57 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694052">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
اظهارات وقیحانه ونس: ایرانی ها با شلیک به کشتی ها مرتکب اشتباه بزرگی شدند و توافق را نقص کردند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694052" target="_blank">📅 20:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694051">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83d357ee4a.mp4?token=WKtW6xOCMp9O6Gb7NCM2ksqpMz6NznrWWetOVXzG4pXB-ebCfJrRbHzB80FC6bHlJQAdGJRQTb_5cL_9oxF2hJqKb9ua7lsUYNYEa_8Es-c7iHCWOgYO4CHcrmMwPUmugGqbWfb4wUBzoh7XtKFSI75LkX3FcSSJtNzGPRx9_nxKzo34kd6FvTZN19ongdkUv-yQ3nr1gEPNtww81p6StnCbSXEM1-UETYIYnOeBoTmy56idOpZcWBS67PpZQy_oh6HGFE2DWYFaX_5jyjuzQ2fVOOa04bMlT_03NOi_UuzecIGTk3jY2yx6GnCIzT0tRI2uvVNeLDqJYUFIIerDFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83d357ee4a.mp4?token=WKtW6xOCMp9O6Gb7NCM2ksqpMz6NznrWWetOVXzG4pXB-ebCfJrRbHzB80FC6bHlJQAdGJRQTb_5cL_9oxF2hJqKb9ua7lsUYNYEa_8Es-c7iHCWOgYO4CHcrmMwPUmugGqbWfb4wUBzoh7XtKFSI75LkX3FcSSJtNzGPRx9_nxKzo34kd6FvTZN19ongdkUv-yQ3nr1gEPNtww81p6StnCbSXEM1-UETYIYnOeBoTmy56idOpZcWBS67PpZQy_oh6HGFE2DWYFaX_5jyjuzQ2fVOOa04bMlT_03NOi_UuzecIGTk3jY2yx6GnCIzT0tRI2uvVNeLDqJYUFIIerDFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با هنر «آنامورفیک» آشنا شوید؛ هنری که تصاویر در نگاه اول بی‌معنی به نظر می‌رسند، اما از زاویه‌ای خاص، تصویر اصلی نمایان می‌شود!
🎨
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/694051" target="_blank">📅 20:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694050">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
پزشکیان: از همین ماه رقم کالابرگ
افزایش خواهد یافت و درآمد حاصل از افزایش قیمت بنزین به طور کامل به مردم پرداخت خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/akhbarefori/694050" target="_blank">📅 20:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694049">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
طبق بیانیه وزارت خزانه‌داری، دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری ۱۰ فرد و نهاد جدید را به فهرست تحریم‌های آمریکا علیه ایران افزود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/694049" target="_blank">📅 20:52 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694048">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJ2ei9Lhm9D4T2N9K93evfGLUtGYt6-iXfHexrsm9Moo7_Y2QIQCIKwtPLxxbs6KFPj2eYs_87mNjKfx5PMy2OloGoEhTr_MW_69VoFcYk84SgYfa9l7W4x3VmBbuOL9OL26q_drwQHZrP1Mp1603nHgueRYRDGfKRcFEux1v9d6d-PclZuzl5TIC9Tg8fnkivuRF3OE4DzJIq3wmOTMOb0fTSKWkSgGjcG_23R7UWcBFqw7cCq-DYC5Yggx5J6tAzi1I8OokPDR6TxFNzqOzC2tJWVhatDjQBp_5M0tW3_KinKqKUVS2QoPIGzV_azCI4d4MIe9EdOhI_wZT1kAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایم مرده روزت رو تبدیل کن به مکالمه انگلیسی!
روزی ۱۰ دقیقه تمرین، کن تا شش ماه بعد زبانت فول بشه
نصب رایگان ویژه ۱۰۰ نفر اول
👈
سریع جوین کانال شو و از دست نده
https://t.me/+dg7n9zI_nvBmODg0
https://t.me/+dg7n9zI_nvBmODg0
https://t.me/+dg7n9zI_nvBmODg0</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/694048" target="_blank">📅 20:48 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694047">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDxoRWYlv5YU-wUAEJSo3WV7N9PGHRRFqMSAIYsxlORy5mCR9ZuaC71g6mpqQzleVERbYrVUudexP67TRAIeQwWF9XBAZubNnx5MqZE-T1uMvR7hmtzTxgsICJptz_2MZlYK4hHwd67848eBtXy6iaU7WJzhuLzWj3Y2E85ZQIGqpZ7SdpG-YCY2Ryky8jBOeLyicdFqJthyX-HuKwkw_0wZ09a5b3hi17H4C4xzZqdt-Y4FAX6tYe8PYAw--tAjMkg6l1jk-RCUWWlAqnJfbW0LlVo3W4nTf-Aoqx85f3DuHc-btQvWnRyv1hDc3QU1KMZw8E2-uSwMXM8cd-FfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👜
هیچ چیزی از چرم‌دوزی بلد نیستی؟ از صفر شروع کن!  دوره جامع چرم‌دوزی با پشتوانه ۱۲ سال تجربه؛ از یادگیری مهارت تا راه‌اندازی کسب‌وکار و فروش.
🎯
✅
۱۴ جلسه آموزش مهارت + کسب‌وکار + فروش
✅
مدرک فنی‌وحرفه‌ای و قابل ترجمه
✅
۶ ماه پشتیبانی
🎁
پک ابزار + ورکشاپ…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/694047" target="_blank">📅 20:44 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694046">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
محمدجواد لاریجانی: بند اول یادداشت تفاهم اسلام آباد به نفع اسرائیل بود/ تفاهم اسلام‌آباد برجام دوم بود و از برجام هم ضعیف تر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/akhbarefori/694046" target="_blank">📅 20:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694045">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3554b54f7.mp4?token=C3el0tvFen_A-MaNMrycxbvmw6QxNj7kXbe5X3RP0HK38EdUOMrs8f8TaAnsDwdyox__u3gAK6ASLQVj13I-OoHc3gsnj-ExvJlFg7VWgGxpC78RD71PTqaAh_98S_SJyuC4p57tsmbpKq1_pwTU_Cr8lzTDnwVvo_My__8YnYSpfUhlX8f3mUfYZrauYQgVNpkmxOSvbAne9Q4uVkTiS-tdUyAMz5wT06h3aXXee2uvzEnQ7TOKYlHb6h-pOziry5gx3T_cFWCzpV5VVK0f1XB6j9C4IBpB8ndNnakfsvdMFjwYy97XI0Z5gsbpy4ioXG7LCHYnzdx6LNr45WsDWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3554b54f7.mp4?token=C3el0tvFen_A-MaNMrycxbvmw6QxNj7kXbe5X3RP0HK38EdUOMrs8f8TaAnsDwdyox__u3gAK6ASLQVj13I-OoHc3gsnj-ExvJlFg7VWgGxpC78RD71PTqaAh_98S_SJyuC4p57tsmbpKq1_pwTU_Cr8lzTDnwVvo_My__8YnYSpfUhlX8f3mUfYZrauYQgVNpkmxOSvbAne9Q4uVkTiS-tdUyAMz5wT06h3aXXee2uvzEnQ7TOKYlHb6h-pOziry5gx3T_cFWCzpV5VVK0f1XB6j9C4IBpB8ndNnakfsvdMFjwYy97XI0Z5gsbpy4ioXG7LCHYnzdx6LNr45WsDWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اجرای رقص سنتی شمشیر عربی توسط ربات‌های چینی در سفارت چین در عربستان
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/694045" target="_blank">📅 20:39 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694044">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjnCU0X7AIc9M3bSHGHdvUKWOlfoLcBmwxZffO8_K2AcRK_hWs9LQczgDNQ6ml17zVpmHQFQYd05uvA2hPrNZOkJUKoHJ3Tua-2DksxZtMDdldZ-sdH6afFQyYo1GXJVr6z_AbXeVAba9wY6W9cGeRiMeJCTGjgju0d_bEvAeRPmfQl5vqtVOXXyg34jvGWOfKe9S9F_guRHzVYnAV0QOcV3rU-7m32rFoH975ikVoBl0xmcUft2zT6Z7wRf0u_tQLfV3sOLsYS4v7ZSsx30VCrHY0Q8pL45i9E9eNrB9szFQ_K-tz0AuVhllPGZKG0hAz_7mAHj6bozVFfZ0N05Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
والتر بلومبرگ: آمریکا آماده است تا سقف ۴۰ میلیون بشکه نفت از ذخایر استراتژیک خود وارد بازار کند
دان وینسلو، نویسندهٔ پرفروش آمریکایی:
🔹
فکر می‌کردم تنگه باز بود بلومبرگ؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/694044" target="_blank">📅 20:31 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694043">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcpBThhwnK57CKM_h9rM_YTq5Li6jl3sVIaDlIKxxCOvrP-pTUkj2B4FAq_CXZBoPKeIP2oX2epDSBpxb4N2dPYEBdOKbcGCA6hpCuNDmKFvFdYIVuEiykGhaKylCwiPuJ21BzOOUbt9gakp4aUTIOSb6gJh9G9rOGP-rl4wVEHgsylA9FsLb9MfC8Noiae-iWIzZXvd9UQkXrexqW7d17CQFQCo3fkKN0EP7G9PB09Kf215ku9MtFecRrH38DKdTEn9Bh8rJpQSJfL9MisCMDELyaF6jwHmOJwVCejCfbVBEinbyUJWtz2ZqOBXvnPPapg2D00IZPWyFuWe17CoMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برای سلامت بدن خود این نقاط را روی پا خود ماساژ دهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/694043" target="_blank">📅 20:24 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694041">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
محمدجواد
لاریجانی: بند اول یادداشت تفاهم اسلام آباد به نفع اسرائیل بود/ تفاهم اسلام‌آباد برجام دوم بود و از برجام هم ضعیف تر است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/694041" target="_blank">📅 20:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694040">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
روابط عمومی سپاه هرمزگان از انهدام مهمات عمل‌نکرده دشمن در محدوده هشت‌بندی تا رودان، از صبح چهارشنبه ۸ مهر، ساعت ۶ صبح بمدت ۷۲ ساعت خبر
داد
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/694040" target="_blank">📅 20:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694039">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
سرلشکر محسن رضایی: ما شروطمان را گفتیم اما ترامپ قادر به تصمیم‌گیری نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/694039" target="_blank">📅 20:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694038">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/417c734abb.mp4?token=TL1fJlmXjW46MVjauU-UVEoiZsIRR7M1ftwcC8XayUlA3aIrCXJcyxNZhyIrQGyNHKsXWDD4cqyYkVf18GST74g9wQX68sJxkeOlsIH0KUprTA7w2mnJQ_QECbu-WcYLRiKq4kh6BfVS3D1QE3OV6LLqfcqugseb9gngfeeVeDnqI1L-rsMmypi0oRbwMMrHw1YcvPX9tupNoxx4qIDC4VD92vpuXGsLuGN7uyBN2qCCJHAhf4jgER-L2hnYfpM8p5VAVZe_hZZDN1tOJR2DrJnpL9Zsbs15uQwzZcZUf6JTRB65os7vDyCuFE4DljSvtG69JWZTbftAMIjGgx6Vhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/417c734abb.mp4?token=TL1fJlmXjW46MVjauU-UVEoiZsIRR7M1ftwcC8XayUlA3aIrCXJcyxNZhyIrQGyNHKsXWDD4cqyYkVf18GST74g9wQX68sJxkeOlsIH0KUprTA7w2mnJQ_QECbu-WcYLRiKq4kh6BfVS3D1QE3OV6LLqfcqugseb9gngfeeVeDnqI1L-rsMmypi0oRbwMMrHw1YcvPX9tupNoxx4qIDC4VD92vpuXGsLuGN7uyBN2qCCJHAhf4jgER-L2hnYfpM8p5VAVZe_hZZDN1tOJR2DrJnpL9Zsbs15uQwzZcZUf6JTRB65os7vDyCuFE4DljSvtG69JWZTbftAMIjGgx6Vhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول روسیه به ایران توسط گولووین
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/694038" target="_blank">📅 20:15 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694037">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
صدای انفجار در قشم شنیده شد؛ این صدا از سمت دریا بوده و به نظر می‌رسد اصابتی داخل جزیره رخ نداده باشد. / مهر  #اخبار_هرمزگان در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/694037" target="_blank">📅 20:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694036">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f156289df.mp4?token=U2FBYfhVikxcZVoaWnNyecekvercP2X9DADYHgDBpeYEFiY-ky1cl2Mu-T8LZS4kB2Mfr6E7H8mVgB6htFd1hCB4_yZL97XVdDxjyF7DbGJGT0IQfXCzBANjkllhdUmlr7l3Bqz2o3Omt_S1UPGT9XtnjAqkrZpeqLO6lND4cJudnRNKg_2d7A1Qs9mtTr5rcL48As5_sxRFkGKfdnDcWKbeury7qVkjCTUpCynBL3aZFGAugrfIN3BNU-7kXK5UfRgUQ9C4jPmrVF6aNrexwn0OjZBiQ1Ct1J9MSri1XA4D98C2Z_-5O8kv5Cf3wFQ7VCyRH1J-vbEW-9IwU9-ElQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f156289df.mp4?token=U2FBYfhVikxcZVoaWnNyecekvercP2X9DADYHgDBpeYEFiY-ky1cl2Mu-T8LZS4kB2Mfr6E7H8mVgB6htFd1hCB4_yZL97XVdDxjyF7DbGJGT0IQfXCzBANjkllhdUmlr7l3Bqz2o3Omt_S1UPGT9XtnjAqkrZpeqLO6lND4cJudnRNKg_2d7A1Qs9mtTr5rcL48As5_sxRFkGKfdnDcWKbeury7qVkjCTUpCynBL3aZFGAugrfIN3BNU-7kXK5UfRgUQ9C4jPmrVF6aNrexwn0OjZBiQ1Ct1J9MSri1XA4D98C2Z_-5O8kv5Cf3wFQ7VCyRH1J-vbEW-9IwU9-ElQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل اول روسیه به ایران توسط گولووین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/694036" target="_blank">📅 20:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694035">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">20-1 Ane Manaee (1404-02-07)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/694035" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیستم؛ بخش اول
حجت‌الاسلام امینی‌خواه:
🔹
مروری بر دوگانه‌ ایمان و کفر، و هدایت و ضلالت در سوره محمد [01:50]
🔹
تفسیر آیه ۲۰ به‌نقل از علامه طباطبایی، توصیف منافق با ظاهر مؤمن و باطن کذب [05:17]
🔹
مرزبندی شفاف قرآن در تفکیک مؤمنان، منافقان و بیماردلان و موقعیت بینابینی بیماردلان! [08:48]
🔹
توصیف بیماردلان از منظر سیاق آیات؛جاهلانی که مؤمنان واقعی را سفیه و ایمان ناب را به سُخره می گیرند! [13:23]
🔹
ترفند منافقان، ،برای به انزوا کشاندن مؤمنان و انحراف مسیر حق در لوای اعتدال نمایی [19:05]
🔹
بیماردلان و مؤمنانِ بی‌هزینه، هنگامه عمل و جهاد از ترس مرگ بیهوش می‌شوند [23:46]
🔹
ترس از مرگ، محکی برای ایمان حقیقی و مرز تفکیک مؤمنان واقعی از بیماردلان [33:07]
🔹
تطبیق وقایع پس از انقلاب با سقیفه و صدر اسلام، و تقابل میان یاران صادق و چهره‌های کاذب رسانه‌ای [39:43]
🔹
ورود در حریم ولایت الهی، شاخص خروج از حد حیوانیت و بهره‌مندی از هدایت و تقواست [44:26]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/694035" target="_blank">📅 20:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694034">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeae6876df.mp4?token=oDATo9XnaxwQ8xxGglw3VlVazhqhL_obqkeLZ1RwZAxwdEExR4q03ErVeBJADfuv3Z83XyxjWpSRkOSJSeGYba7SZGG7T1g6enQ-KH6g_YTyJRqARmcPQmd_BGqJ2kNxBXNrg2x9viueU8YqAaP3I07Mf4_SNdccSr5Tk3QkEUA6IYdCiGDGPFpYZNKlUL-by5vW1yLKdUCI9DW_AJoM6kbd9RNCTFY_bNZ1vY75V6nRmATZQQZKcOQUJROCrlVWjYGtoaqZBSfaEWIdpWksx3eTC2oBw0WjBUFzz7L3qXNB9JszuNQOsYhKVAaUqKFVGs2ry07srH510zhWGz6G9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeae6876df.mp4?token=oDATo9XnaxwQ8xxGglw3VlVazhqhL_obqkeLZ1RwZAxwdEExR4q03ErVeBJADfuv3Z83XyxjWpSRkOSJSeGYba7SZGG7T1g6enQ-KH6g_YTyJRqARmcPQmd_BGqJ2kNxBXNrg2x9viueU8YqAaP3I07Mf4_SNdccSr5Tk3QkEUA6IYdCiGDGPFpYZNKlUL-by5vW1yLKdUCI9DW_AJoM6kbd9RNCTFY_bNZ1vY75V6nRmATZQQZKcOQUJROCrlVWjYGtoaqZBSfaEWIdpWksx3eTC2oBw0WjBUFzz7L3qXNB9JszuNQOsYhKVAaUqKFVGs2ry07srH510zhWGz6G9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معجون ضدسرفه و گلودرد، یک درمان عالی و فوری برای سرفه‌های شدید
🥣
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/694034" target="_blank">📅 20:06 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694033">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47274e3da.mp4?token=MMXx0qPz__yveEzNmh8BoRwRFEoGyQ39uSNtLchD08iUu6Z6g0rugQ1jBYEHaHxFlByjMAfU3kAQQdqWCRtaQTNwSejjmYnxPuaDmfuAE5AtzghPAOh8-f8XNg0WpcCAOMRp8ArmxQS2T1SO3xBuoOegaCIZ5B-E2jt-PuKMM_cRaQhFQH_5Gd3M0bw8SBXAa3fU8oob1DpyjBbWeNdwurZiysLqvqBgC7UCVmlSBOPAGSNAK_-q_IBibviTGJdoj0ZR9anymLomdIOADDIJg3R-O_peOmwF-SuHv708J0D4GGp6oj3sCNOmr6dP-w0SBwxPxVdg5BDzy07vglqdOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47274e3da.mp4?token=MMXx0qPz__yveEzNmh8BoRwRFEoGyQ39uSNtLchD08iUu6Z6g0rugQ1jBYEHaHxFlByjMAfU3kAQQdqWCRtaQTNwSejjmYnxPuaDmfuAE5AtzghPAOh8-f8XNg0WpcCAOMRp8ArmxQS2T1SO3xBuoOegaCIZ5B-E2jt-PuKMM_cRaQhFQH_5Gd3M0bw8SBXAa3fU8oob1DpyjBbWeNdwurZiysLqvqBgC7UCVmlSBOPAGSNAK_-q_IBibviTGJdoj0ZR9anymLomdIOADDIJg3R-O_peOmwF-SuHv708J0D4GGp6oj3sCNOmr6dP-w0SBwxPxVdg5BDzy07vglqdOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افتخار نتانیاهو جنایتکار به جاسوسی با موبایل
‌
🔹
‏نتانیاهو با افتخار می‌گوید که رژیم صهیونیستی چگونه می‌تواند هر کسی را با هک کردن تلفن‌های همراهشان، به عنوان دشمن جلوه دهد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/694033" target="_blank">📅 19:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694032">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
صدای انفجار در قشم شنیده شد؛ این صدا از سمت دریا بوده و به نظر می‌رسد اصابتی داخل جزیره رخ نداده باشد. / مهر
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/694032" target="_blank">📅 19:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694031">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
تیراندازی در ایرانشهر؛ مقابله پلیس با سارقان مسلح
🔹
نیروهای انتظامی در جریان این عملیات با سارقان مسلح درگیر شده‌اند و این افراد در دام نیروهای فراجا گرفتار شده‌اند./ تسنیم
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/694031" target="_blank">📅 19:53 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694030">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار آذربایجان شرقی</strong></div>
<div class="tg-text">♦️
دیدار شمس تبریزی و مولانا یکی از مهم‌ترین اتفاق‌های زندگی مولانا بود؛ آشنایی‌ای که مسیر فکری و شخصی او را تغییر داد و اثرش سال‌ها بعد در شعرها و آثارش باقی ماند.
🔹
در این ویدیو، بخشی از داستان آشنایی، همراهی و جدایی شمس و مولانا را روایت کرده‌ایم.
🔹
۷ و ۸ مهر، روز بزرگداشت شمس تبریزی و مولانا گرامی باد.
@azarbaijan_Sharghi</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/694030" target="_blank">📅 19:50 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694029">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9e0e2a3c2.mp4?token=nbZ5ZfDGJ1ztPWWXD7Bo7GOZxBc8K237F8RPKTye1JX_pe0y2asAxne95iumhiqYITVofumhzNwq0NfyRhM_0LMC_GDCPF-bDl5QJK_LPXWyR8HoRuxx1czj9aSFx3KWtLIafUhJ7AQQfBQCMZjraq0jKllASCjOL_f92nsXpcvEm18VcOB00VcbnbdtVdkcJ90gvVgWBiMawTEcWeLu5Im6loFKZsX7n4PfnThVx0c5mWWpl2fQcy2YUmllUpoCSlsXHmPh3oNCsv1W67utUk21WeWizocoRHEP4jBmsloVYv9hIzNWsuYNrZWgLmyJZmWM3BQGPbtm66gRRj0Tkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9e0e2a3c2.mp4?token=nbZ5ZfDGJ1ztPWWXD7Bo7GOZxBc8K237F8RPKTye1JX_pe0y2asAxne95iumhiqYITVofumhzNwq0NfyRhM_0LMC_GDCPF-bDl5QJK_LPXWyR8HoRuxx1czj9aSFx3KWtLIafUhJ7AQQfBQCMZjraq0jKllASCjOL_f92nsXpcvEm18VcOB00VcbnbdtVdkcJ90gvVgWBiMawTEcWeLu5Im6loFKZsX7n4PfnThVx0c5mWWpl2fQcy2YUmllUpoCSlsXHmPh3oNCsv1W67utUk21WeWizocoRHEP4jBmsloVYv9hIzNWsuYNrZWgLmyJZmWM3BQGPbtm66gRRj0Tkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه گویی ترامپ جنایتکار: ایرانیان در همه عرصه ها در حال شکست خوردن هستند/ قیمت نفت مثل گذشته پایین خواهد آمد!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/694029" target="_blank">📅 19:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694028">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ترامپ: فکر می‌کنم یک اسم جدید پیدا کرده‌ام. دیگر عبارت «اخبار جعلی» را فراموش کنید؛ از این به بعد می‌خواهم آنها را «اخبار مصنوعی» بنامم. این اسم را دوست دارم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/akhbarefori/694028" target="_blank">📅 19:49 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694027">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/248479f455.mp4?token=jpEJedik8WZnzqc3nP1_z7Bp88vHZNMGGSHW_Do5dw3GyRbgxu5tImUNK2v2QF00XNt3swMEvSpiOPbJofe-q0h-Q6rCzkauhUUqsTf8U0SOWCNRvdsAwkHkXCkHEwFjzPQUt695Y_KyFCjM8BoECanRLDKW_VGfjC6v8OI8uxt3Zs_vB5Ao2q4sBI0axRHGmkH0qq3ofE64LL0xLOsnzAdX-VT46LcGaypmbM1Wnt0nmgbeUGssMEfV4OdSY1ZbTvfIBVAPiZPs-erMhn6b1iBmd07RBs08vqYJglXkfjDQwCDeZSyFnCEdYzyC7Ctdx5Q3cI5JpNOpPvcMPEAbi0ogPRXmyQbfElj0zy9xjCcN54OZUGGPDER4Ea64d78RStE_nsB8B3yt-RUGJCknD2GQ45hcmjK8lYtwnALz0BjYaNzOBWnb55w49GlynWGc8GqdQlDQ9qnSZX20_5582edPHGQDQZ7lty60-t-eqndIN6UPiYozpU3uVFUF9AL1mQtEFke0pjYS_zamvBuk5Jdo8G8vRH-af6BnQhbLetBTGYRxaZ0-QmVzcGT-oHSXKCij0v4DL1H4X1__QNJtKUdCa6Ynk2VsHEROrYZ1PzOPOd3UpHI-UrTCOIrs3f0eJ6CYGxB3amatjpcIW_3tdLDNv5bU-URW8OSXlBPZnqo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/248479f455.mp4?token=jpEJedik8WZnzqc3nP1_z7Bp88vHZNMGGSHW_Do5dw3GyRbgxu5tImUNK2v2QF00XNt3swMEvSpiOPbJofe-q0h-Q6rCzkauhUUqsTf8U0SOWCNRvdsAwkHkXCkHEwFjzPQUt695Y_KyFCjM8BoECanRLDKW_VGfjC6v8OI8uxt3Zs_vB5Ao2q4sBI0axRHGmkH0qq3ofE64LL0xLOsnzAdX-VT46LcGaypmbM1Wnt0nmgbeUGssMEfV4OdSY1ZbTvfIBVAPiZPs-erMhn6b1iBmd07RBs08vqYJglXkfjDQwCDeZSyFnCEdYzyC7Ctdx5Q3cI5JpNOpPvcMPEAbi0ogPRXmyQbfElj0zy9xjCcN54OZUGGPDER4Ea64d78RStE_nsB8B3yt-RUGJCknD2GQ45hcmjK8lYtwnALz0BjYaNzOBWnb55w49GlynWGc8GqdQlDQ9qnSZX20_5582edPHGQDQZ7lty60-t-eqndIN6UPiYozpU3uVFUF9AL1mQtEFke0pjYS_zamvBuk5Jdo8G8vRH-af6BnQhbLetBTGYRxaZ0-QmVzcGT-oHSXKCij0v4DL1H4X1__QNJtKUdCa6Ynk2VsHEROrYZ1PzOPOd3UpHI-UrTCOIrs3f0eJ6CYGxB3amatjpcIW_3tdLDNv5bU-URW8OSXlBPZnqo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ تروریست: جنگ علیه ایران یکی از مهم‌ترین کارهایی است که انجام دادیم   ترامپ:
🔹
در سال‌های آینده، کسانی‌که تاریخ کشور ما را خواهند نوشت  خواهند گفت که جنگ علیه ایران یکی از مهم‌ترین کارهایی است که ما انجام دادیم.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/694027" target="_blank">📅 19:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694026">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفروشگاه قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twCYeM-JmriNPc_deFL4Zqa-GOVhMhM-g7iMs2cmpOwWM-4y4zicotLqHjG4n8cSFZHW0wkAD0wrubEsnpPt0ThOhO2__eZoTpyi3tic_8WB3PVsceiP_0GLtk5qq2SceItNEkPLw_GU8kYzstm2H-z0l-zu8CQx-d653EV7Xc2PQeqK37rBu9Chj4cEgZu4yX91Ruxdy7rYX_8wJAsCqNaez8zAs2s6ObEV7xlUJFTfvALK8aFcQNsecltvqr9j9b8juyBB_e2j8T5IQyjxImkLiyJZ85oCQ424chuN-ydRRp7sp-CVmyTJm3fG2RZdLcKkw3KHVvCghg9_wHE5Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕊
پک_سوغات مشهدالرضا
🎁
مجموعه‌ای دلنشین از یادگارهای معنوی حرم امام مهربانی‌ها؛ هدیه‌ای ارزشمند برای عزیزانی که دلشان هوای مشهدالرضا دارد.
✨
مشخصات محصول:
▫️
قطعه فرش متبرک حرم رضوی
▫️
عطر خالص حرم رضوی
▫️
تسبیح ۳۳ دانه فیروزه‌ای
▫️
مهر تربت مشهدالرضا
💰
قیمت اصلی: ۱٬۳۹۷ هزارتومان
🔥
قیمت با تخفیف ویژه: ۱٬۱۹۰ هزارتومان
⏳
موجودی محدود؛ برای ثبت سفارش، همین حالا اقدام کنید.
📩
سفارش:
@gharar_order
🤍
هر خرید از «قرار»، سهمی در مسیر خیر.
@ghararshop</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/694026" target="_blank">📅 19:45 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694024">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44dc04051e.mp4?token=q7VOsg4jc2Vw9IAfblqUmA3qZqY2l_GXt2322Hzh4uAeFQTwIbS1S8Hwn8-nbgpLB1iYWepcXd7ADmoFdrngENcH94MGOZzB2noUc6Wn8eJ21tJ8wpJ8BCaWCtrqWtJw99IBEMKqAim7DtnayAYOvv1eGlklRpfg7k_2JSifu9LT6qHh7l4a9LiX1wY7Zg4JcwItqyHX-dig50TTGalmYT4JWOWPUxTG_07irm8Nq6VIjQP_PoVYnR2GJ9UD9YH4HrFPo0Pr8lnz43v--zaasL9HpF_rAdz6aksW2dzTKh9V3C33jt3OWqZNSWy1p7X98IOyuTolKOKHwN0TgbBq1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44dc04051e.mp4?token=q7VOsg4jc2Vw9IAfblqUmA3qZqY2l_GXt2322Hzh4uAeFQTwIbS1S8Hwn8-nbgpLB1iYWepcXd7ADmoFdrngENcH94MGOZzB2noUc6Wn8eJ21tJ8wpJ8BCaWCtrqWtJw99IBEMKqAim7DtnayAYOvv1eGlklRpfg7k_2JSifu9LT6qHh7l4a9LiX1wY7Zg4JcwItqyHX-dig50TTGalmYT4JWOWPUxTG_07irm8Nq6VIjQP_PoVYnR2GJ9UD9YH4HrFPo0Pr8lnz43v--zaasL9HpF_rAdz6aksW2dzTKh9V3C33jt3OWqZNSWy1p7X98IOyuTolKOKHwN0TgbBq1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جی‌دی‌ ونس، معاون تروریست رئیس‌جمهور، درباره‌ی رهبر انقلاب: ما فکر می‌کنیم او زنده است. البته نمی‌دانم. من هرگز او را ندیده‌ام. اما بهترین شواهدی که در اختیار داریم نشان می‌دهد که او زنده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/akhbarefori/694024" target="_blank">📅 19:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694023">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
تهدید روسیه به حمله اتمی!
🔹
روسیه هشدار داد که هرگونه تلاش انگلیس یا ناتو برای محاصره منطقه کالینینگراد، با واکنشی با استفاده از تمام ابزارها، از جمله تسلیحات هسته‌ای مواجه خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/694023" target="_blank">📅 19:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694022">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
رئیس کمیسیون آموزش مجلس: هر معلمی که سی ساعت کار بکند همه مدارس مکلف و موظف هستند یک حقوق کامل به او بدهند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/694022" target="_blank">📅 19:26 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694021">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">♦️
حذف نام ترامپ از وب‌سایت نامزدهای جمهوری‌خواه
🔹
نیوزویک گزارش داد که شماری از نامزدهای جمهوری‌خواه انتخابات میان‌دوره‌ای آمریکا، هم‌زمان با کاهش محبوبیت دونالد ترامپ، تصاویر و اشاره‌های مستقیم به رئیس‌جمهور آمریکا را از وب‌سایت‌های انتخاباتی خود حذف کرده و تمرکز تبلیغاتشان را به مسائل داخلی و هزینه‌های زندگی معطوف کرده‌اند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/694021" target="_blank">📅 19:25 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694020">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
به هیچ‌وجه صورت کسی را داخل کیک تولد نکوبید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/694020" target="_blank">📅 19:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694019">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GKka-kFVmY2wSli2pwqsLjURgb9m79Wb1AtNMPWTD5MSfOonawfXq6ByBJoYx_Y6SY5OCd32BNfrDugV2o5PC2c0APch56JGwKsuaJUki_Z69OMZd2hbUeYHzq_WcJb07jEPHeuwOneVXE1pygk-8qiDrat6zspJdFSauELibCKGeKd8NCw4ZspNHrGbmra_td6uhxOejU9sCzVeln4-1j3tcvidszVlYer8o3q4DBp7CO_AqlNt0uOHenGuaMpxHnzD6lYoRGBy3-zI1C56WRf0zlkNSTXXBEuuOIeICney3SzCa6J2kUPPX9ma0AfeP5FvuHz7EtoM0wzdKdqFCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خطاب به مردم شریف آمریکا
🔹
سپاه پاسداران در نامه‌ای ۱۸ صفحه‌ای، به مردم آمریکا از آنها خواست که حساب‌شان را از اشغالگران فلسطین که خواه ناخواه باید آنجا را ترک کنند و به کشورهایشان برگردند جدا کنند. سپاه پاسداران اعلام کرد: ما می‌توانیم همزیستی مسالمت آمیزی با هم داشته باشیم و آن کسانی که می‌توانند این سرنوشت شوم را تغییر دهند، خود شما مردم آمریکا هستید. مقصود از شعار «مرگ بر آمریکا» در ایران، نمی‌تواند مرگ بر ملت آمریکا باشد، بلکه مرگ بر حاکمان ستمگر کاخ سفید است و دولت یاغی و شهوت‌ران آمریکا را کنار بگذارید.
🔹
هشتصدوهفتادوسومین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/694019" target="_blank">📅 19:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694014">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NpYn75_aPulWg7HK9chzM47vhA729288fUOYcA3MY9FNcxADb27c65cizR-TW9x6koyAndIZtpXlPNj0P_Zs_3Ct8I-9JyJ4bPy6m6vdMoXWFPmev4t6uqVQxfx-VxpdYn9v0XhLXsY2QOVS2qmgRvYkQ7P7N3bJ_BtDgHQIs1-ZZm_SMIWkkdBhna9Wd-JYqK66g_06h3_R4-FP4a5S7C1b5BlZYhdf9LrjDcCD-qmDt7b4n_ZZKOddyafzZiG_nazFjHQ4miiTy7C2TuEQf8i4_LBLjsVIy5EodI97tzwACubbQGK_ryM-4-gO-CugnXGqWAk9T7meJCaBXiZ6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txBuAX2e2kc-Ifcj-rZyLpxYNJMPfUg61W_1Gr3vSIq9fm0vIYHsj4dHya1dURW-YLMOTGLbTXFJkicq_5mOmV2svXYuBySHqqmZASTJFJ4r-Gu94O6x9wNQK-DEURZKvpskvJf5JTGHOpq5c7GGlH9UgcE6Sg1TMNAJu-KvOYX4Tc-IeGiDt6sdhflhdeE0wOk8xttG0fGl6x-HRDuqD8emYEk34GZBNFnUihqsYNMHBziOBKyzj-T_Tc_8hteP1jlhW_AR1Y-EjpkPMnTTGtKfSDllgidTRjsYjfr39vT9_Mck-a7ybYJ2FzSHd_QPkVY9t18wEIXj2nR4jW7Qdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JR5NTj4oTQoQlGr79iUTpDtefkUSeQCXgwO4PVjstsfrLwXiMV0GHjzC_BgSX5ty5cz-1ynq5A0OnejdB1lFCjdjKRDb1t1n52G79aPODffcZECSzkzYLg-zdKKyllPRu7SVI8Vg0SHhrJxbcoor-xNlQIeoygaKEdT-652ym1foQ3If2bDBqrcDSMtY9yEf32IWLbUnG50JKm6d_fmp9EvIkJPQYyYSYq0c6XvyJNOFLstd8-kNZONkXWfMFsOtiUlkQe11Cwe9nuQA2DDJtdA6a6X9-m1EOqZsJWfxlt_lN-g7emriiiTO62Q6ws7TSUayesb0nQ_eQQANUjmwBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qw3SOL9JXWmdlykDsQbTNop3bcqaz_vqxBBgAbqSJcVZlq1agrDnKrmWGfjsbS9zruy8nRxRxnGOAA3pE-jAVWmgajxXb9k2AoMocuZTriWZ1hgl2Zp9STAYkoUvcD3TddiTfDSBjy4MASwCJroRGTKa02qRFKBDJI0hUE4V9n4YPwdfT8u-YRjc-FVcROQwCOTX0dtvkYN202_GLRI6F3BCqoS_3c9PWh4qBS5cUb4pC1waFIk3Xd7DEfvkBs_t4gLYJgwlyxNa0Ask_6ZqfmGk5ckcjuP7BvLcO7Co3OJxdMiTrFLjsZbjoJHFeaXUb0hZUSgvuAxX8vdNDtBauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QxdeL5mMiTlAPx-ngr37qeVIHbNBMDT8V5_Xwgb8tL0C9Oo4X-QupztK9nQltPWy1_hbh3_ao33qS_jrr7RJtmSJbaLvz3_hhd0wctUsOKski8Z9B-mYjsPH3N3LhFTNrqOFhKVQQ6zFn3CaXJFcnWMmWvFdqjaa6JlDihRf6UdfS7mMlLnfaZnqeE96A6sLvUrlq7JubFZqmR8mCcFqCLJLehuIoa-s_LmpXmW2PTmCv_MVJTmq-JcVHPZWy_8nkHcb7ZHTPf5-CoXLs3smKArvzi6atzYeCWEhEW1TCWoxkxWQLOBNqG3ojMchxMdsRoJMo-sklY2LzTqn44zr4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چند مدل
نوشیدنی پاییزی
🥛
🍁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/694014" target="_blank">📅 18:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694013">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a854c09381.mp4?token=QLL7LNPh4c8JmJ8diMuxmxSZ3NRRrCcXikHy_Gtu22yi_bcYDrlBJyiFESiCLl0WmXFAnLpJ77wUfGPXS_l7b7-z18f4un97Sj7vf9bhL_r1Z2rTIBtOAAo0K48ppWxhfdzEWutd2-UYBClPk8EpPcHILWY4SOlEzfgiyJqkV2_VPjiVkXfbhqHAc15v2p1byDVqcBxHHwuGKoqTJtmb_lJO-o-GEUZMf2O3YmZpuT7bfN6cpglcM2FMZGcGkHjatMleepdj9iZP_O83_YOVCd84NnJaoDXSAyJGoiHfCOiymO5_t4na4t0Aqg2oJ03lmbT2m0dCKsZGXrERcaNvBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a854c09381.mp4?token=QLL7LNPh4c8JmJ8diMuxmxSZ3NRRrCcXikHy_Gtu22yi_bcYDrlBJyiFESiCLl0WmXFAnLpJ77wUfGPXS_l7b7-z18f4un97Sj7vf9bhL_r1Z2rTIBtOAAo0K48ppWxhfdzEWutd2-UYBClPk8EpPcHILWY4SOlEzfgiyJqkV2_VPjiVkXfbhqHAc15v2p1byDVqcBxHHwuGKoqTJtmb_lJO-o-GEUZMf2O3YmZpuT7bfN6cpglcM2FMZGcGkHjatMleepdj9iZP_O83_YOVCd84NnJaoDXSAyJGoiHfCOiymO5_t4na4t0Aqg2oJ03lmbT2m0dCKsZGXrERcaNvBzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایران چگونه محاصره دریایی را دور می‌زند؟
/ تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/694013" target="_blank">📅 18:56 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694012">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hxc1mim7R-DvJr7A2Td8lgESO0TTddcbXNOyziMnh3ZEh0LmBPpn3ZM6lOnIWF4Fy_KzxuNnNC1X0hDXewRa3mYBeVwJ4YEqoxS_0JcrZuH8H4f1wnNt2h_rAh_07pWMfW2xr3Rv2GzqUM3amaBxLWT0hb-dJaAhJ02rtuNtS0x2FGfojICgpuUSTrXoIHOFa374wv0f9dHZcQqCDrljvnxf_C5HV5tCkD2pr8XQFEWOjHCtga8zPqc9yI_H3zfgVDqrOakGMpxZUUf7mlY95BrjPZ0oxVu-I_ZsJgoW5NZxcQKm1gtqWm-gcfLgjtfVdieHp9xOw6cLO4LS7Ged_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش آمریکا شروع به بازگرداندن هواپیماهای سوخت‌رسان و قرار دادن آنها در فرودگاه‌های بن گوریون و رامون کرده‌است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/694012" target="_blank">📅 18:42 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694011">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m0MLR0TB7vrNs4iItArCpHFmnM8J5Gfx7YnPpCKhSxnqOeyE50vWnuwSd-6azZchc8NVwaSPcWGUWFpRpSFluJoXU-sy-6v4yll0fUZEU0gdF0BK1hkC78jCexU7GHYLTbbzm3Ca8Og8lRzNfmbbI0JuyFgJS02lh2wRnD21zMWZTOhzaGDXTL1Y4UbfvyegL17LvbYOk_LnJgeCEyg2N2LVRsUGm65MzNCvJ6LJtVcS6Dm_3r3i6w5eygYgeT3oRJAEcXftEkPH7rBBOW_h9QrvfRRncBuAdak3Eqa1FPG65r9TFeovSVOrp-N0ckCRnm8rmTleK1hdD4ORmGE69g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تحلیل شخصیت از طریق گروه خونی
🧬
🩸
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/694011" target="_blank">📅 18:23 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694010">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnUVIfRK7AXd9AzcW8IBlZbBevJg9czYMKP1qurekbJzjdYmUyVg3BzH1yIi7VE259wC6eHnhjQJNeSbvryzRrxY434oM7ocMN-t4MyTzGooWFTrN3jZLVHdoz_Bc8X5Hlbt7Uyd8gu3SSJwgCJq1ZJc3PwlZIB-XLq-S-RvgUJeADig0ur_RJRZiPZVVc-XVEStvxqjRYEZRtA97G9fAG5IsknkaJp4E7480sFv9d8eYqEeK6PoFt1HQmx2vyPx1lEOxA4Cd5G1VHC3VkBBFMuQ14Q_g2xI0jpF4pKhTQvG7d7zkUZX5lDlk5eLkjdtUnxm7PsSi1zPzNbRfr9VGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درآمد ریالی اپراتورها با هزینه دلاری شبکه همخوانی ندارد
🔹
علی ذاکر، رئیس هیئت‌مدیره انجمن کارفرمایی شرکت‌های سروکو، می‌گوید درآمد ریالی اپراتورها با هزینه‌های دلاری توسعه و نگهداری شبکه همخوانی ندارد و افزایش‌های مقطعی تعرفه هم نتوانسته این فاصله را جبران کند.
🔹
تورم، نوسان نرخ ارز و هزینه‌های ناشی از قطعی برق، فشار بیشتری به اپراتورها وارد کرده و توان آنها برای نوسازی تجهیزات و توسعه شبکه را کاهش داده است. نتیجه این وضعیت هم در افت کیفیت خدمات و قطعی‌های مکرر به کاربران منتقل می‌شود.
🔹
اصلاح تعرفه‌ها به معنای گران‌کردن خدمات نیست و این کار، برای حفظ توان سرمایه‌گذاری و بقای شبکه ضروری است.
🔹
در کنار اصلاح تعرفه‌ها، تنظیم‌گری بهتر، اشتراک‌گذاری زیرساخت‌ها و جلوگیری از سرمایه‌گذاری‌های موازی هم مهم است./خبرآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/694010" target="_blank">📅 18:22 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694009">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
ادعای
اکسیوس درباره ایران و امریکا: شکاف‌هازیاد هستند. فکر می‌کنم رسیدن به یک توافق نهایی برای میانجی‌ها به یک معجزه نیاز دارد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/694009" target="_blank">📅 18:20 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694007">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/492bab73b4.mp4?token=aGZaasGZ5t7SWSuLmwosqtKwaR5bUC3vtQhNLASV0kb4fH6M1brUWVTG5NVqcyXp2ldBiTQH0iZT_MVzGZnWud4guSj2tKtwBliR8L4qlkwNFUKIAEuBDL9NLSd4xSEpbEn2PeG7StgPNQZ8l9Bg94glXBa-rKr2u43D79WgNpeU6eOpwVRZe6UcSyZrI9xjsVdsYnMdOnAGYFQRmOwxhdC6Kk8oA08tYRA0Mk14dJsBrLoTF4D8XkCCRW8J7g0e6Q5WwkUwQGasZbh8Su_ipt27E5-gKiuHGu2QMb61Pm_R8_wBhF8trOoEghY-TENQScBP47d4J5lkZOflyAurEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/492bab73b4.mp4?token=aGZaasGZ5t7SWSuLmwosqtKwaR5bUC3vtQhNLASV0kb4fH6M1brUWVTG5NVqcyXp2ldBiTQH0iZT_MVzGZnWud4guSj2tKtwBliR8L4qlkwNFUKIAEuBDL9NLSd4xSEpbEn2PeG7StgPNQZ8l9Bg94glXBa-rKr2u43D79WgNpeU6eOpwVRZe6UcSyZrI9xjsVdsYnMdOnAGYFQRmOwxhdC6Kk8oA08tYRA0Mk14dJsBrLoTF4D8XkCCRW8J7g0e6Q5WwkUwQGasZbh8Su_ipt27E5-gKiuHGu2QMb61Pm_R8_wBhF8trOoEghY-TENQScBP47d4J5lkZOflyAurEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ تروریست: جنگ علیه ایران یکی از مهم‌ترین کارهایی است که انجام دادیم
ترامپ:
🔹
در سال‌های آینده، کسانی‌که تاریخ کشور ما را خواهند نوشت  خواهند گفت که جنگ علیه ایران یکی از مهم‌ترین کارهایی است که ما انجام دادیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/694007" target="_blank">📅 18:18 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694006">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6b96753e.mp4?token=UsDT3HbsdU1QGPTYkbbS6lrtX0LQOoj2AArNssA6whZNvqzxOYlvd-4dT4BMYCnBkviYyBgO7PX-KY4TXpsb1wJnuLlkUmMJl-gSB-A5TppRVid3x_5Y4JbMIGkhZO9J6Ei7Nw9ESzIe0dqgbUHbNxwVqusns5fjGtznhq-V1xsvDfvG9UwVCZuDlKhnvO0w0HTOqCuCLFpuz-YJiT0O9iRonFYDilKFjhvN_Xu5R97h6ZL5r-EGM72kpe-o-PsvfABOnXATFa9hezkgJeWL-DD_mPxpjp81HdghTsEEFIv444nbp1f4VGiN5t7HSx9m-eyOU76_5-l-ENhLujZurw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6b96753e.mp4?token=UsDT3HbsdU1QGPTYkbbS6lrtX0LQOoj2AArNssA6whZNvqzxOYlvd-4dT4BMYCnBkviYyBgO7PX-KY4TXpsb1wJnuLlkUmMJl-gSB-A5TppRVid3x_5Y4JbMIGkhZO9J6Ei7Nw9ESzIe0dqgbUHbNxwVqusns5fjGtznhq-V1xsvDfvG9UwVCZuDlKhnvO0w0HTOqCuCLFpuz-YJiT0O9iRonFYDilKFjhvN_Xu5R97h6ZL5r-EGM72kpe-o-PsvfABOnXATFa9hezkgJeWL-DD_mPxpjp81HdghTsEEFIv444nbp1f4VGiN5t7HSx9m-eyOU76_5-l-ENhLujZurw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اکرم خانم، خواهشا حنا روی سر او نگذار؛ خواهش عجیب سردار آزمون از همسر بیرانوند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/694006" target="_blank">📅 18:16 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694005">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/694005" target="_blank">📅 18:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694004">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ویدئویی از لحظه انفجار در حلب/ هنوز علت انفجار مشخص نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/694004" target="_blank">📅 18:08 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694003">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
سخنگوی ارتش: اگر بفهمیم حملۀ دشمن نزدیک است، حتماً عملیات پیش‌دستانه انجام می‌دهیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/694003" target="_blank">📅 18:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694002">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
رئیس کمیسیون امنیت ملی مجلس: روز پشیمانی کشورهای همسایه بزودی فرا می‌رسد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/akhbarefori/694002" target="_blank">📅 18:07 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694001">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeyHNXgKnVdE3o0Y1H8LUi3uNhp_NX8uT1Y-sHdNuwUYZ0LfqsgEaZO_x759YN4twns8u8wE_Ml9ER1at_kFUzjApWH-HIYEbjLvcBitUyIy1zXnJOkrqUXpw560y4lp5npQZMlaO4uwXL7NqS49lM9r3U3KnPjreSKQNMik5LXJPh8hMbTN09M5OHptsUKutZlh_GqC-7lz3r2QQyooNpcrUsuXxe3bW8V96rXRBJIW71ueNCExXpW2Rsm5a9umoHHIktaeDmQRYUF4OZ5EwMzXj6MOF7c3piT2J5BMhLOKpi3Y7P3NhXO_GjnXr5jAtbZcjvLWtKUwEC1nSsKUYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در این پست با چند جفت کلمه‌ پرکاربرد آشنا می‌شی که خیلی‌ها فکر می‌کنند هم‌معنی‌اند و اشتباه به جای هم استفاده می‌کنن! #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/694001" target="_blank">📅 18:04 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-694000">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fff281272.mp4?token=l02R6K-h7Ra_Rf-nO3WENuelR6UsBYOrEdCxZDjfS8x99r0X5Jh0vV3jk5RBAmcLUWNqM7DnoIibedJtzcXl5EfzHdBzV5jUq-tVILKURoBk4PG-0v-Mcm-iR8VgodDmCOHdraS1_RDWZThp3Z4xpJhvJu3xTh6jSAXa83AxqtVLMWYg3_8jtEFefA7fyX8PZ5DEIFfOGpXp3Wh9vKStDQG70kGhJywYPu4ILINymh54Zq7i2U7bFJs_3mJxmRvKjufR9mRS2ZGqxJGVjUbxkI_hzC6b7L7fYROMVVl4QrDPdceSOwtQDw9d8IIUp2rdrC4l_WwkfB_OUJFfaF_Icw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fff281272.mp4?token=l02R6K-h7Ra_Rf-nO3WENuelR6UsBYOrEdCxZDjfS8x99r0X5Jh0vV3jk5RBAmcLUWNqM7DnoIibedJtzcXl5EfzHdBzV5jUq-tVILKURoBk4PG-0v-Mcm-iR8VgodDmCOHdraS1_RDWZThp3Z4xpJhvJu3xTh6jSAXa83AxqtVLMWYg3_8jtEFefA7fyX8PZ5DEIFfOGpXp3Wh9vKStDQG70kGhJywYPu4ILINymh54Zq7i2U7bFJs_3mJxmRvKjufR9mRS2ZGqxJGVjUbxkI_hzC6b7L7fYROMVVl4QrDPdceSOwtQDw9d8IIUp2rdrC4l_WwkfB_OUJFfaF_Icw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه در کمتر از  یک دقیقه به خواب برویم ؟!
😴
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/694000" target="_blank">📅 18:02 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693999">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YvJKrIRvfywTyjOe1waWAJpqVUpXYiPjFu5u-pXbm4JoBkrCD3wTe7bhiddEF7kthEw0ux3_s2gSxoo20UdIEVxa9qAFmYCiGIZ2GemZdstCRqN-TDM3Yw0rRIGDzdCQPp-RmEBEWOq9FYnF9cTs3hh-OUkWFbvIkRpbcA5GsW-zL5jzFKeF4m4_lxZuvIB1nukNez_05-wMwDPUKvT6edR0_XtI-j6O-gF5uKg_AgmgmNiJFDzFoAUalTFkgWFfCFe926ySK56IHcCHjYHa7PtfyuCfN3hQyeEJEng2WbniNDAeleWPVnKvCNLMvlNDJAfqbcSyxhGH1p9OEnnWJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
بر اساس گزارش عملکرد سامانه «فواد ۱۲۸»
بانک کشاورزی رتبه نخست سرعت پاسخگویی در شبکه بانکی کشور را کسب کرد
🔻
بر اساس گزارش عملکرد سامانه فوریت‌های اداری (فواد ۱۲۸) در شهریورماه که از سوی علاءالدین رفیع‌زاده، معاون رئیس‌جمهور و رئیس سازمان اداری و استخدامی کشور منتشر شد، بانک کشاورزی با ثبت رکورد ۲۸ ثانیه در رسیدگی به درخواست‌ها، سریع‌ترین عملکرد پاسخگویی را در میان تمامی بانک‌های کشور کسب کرد.
🔻
میانگین زمان رسیدگی و پاسخگویی به درخواست‌های مردمی در کل شبکه بانکی کشور طی شهریورماه «۲ دقیقه و ۳۷ ثانیه» و میانگین کل دستگاه‌های اجرایی «۲ دقیقه و ۴۶ ثانیه» بوده است. مقایسه این ارقام نشان می‌دهد سرعت پاسخگویی و رسیدگی به مطالبات شهروندان در بانک کشاورزی بیش از ۵ برابر سریع‌تر از میانگین نظام بانکی و دستگاه‌های اجرایی کشور بوده است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/693999" target="_blank">📅 18:01 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693998">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYJYBCCYFk6VYwSB56SHv7MsKFjCm2cEDjHhAxWTwfjoO-KYX_eGKqbTeguRgZ5oS-HY99Gij0srBStjBDNf3WUT7WKix9q_6NGjoK2ENs6eD7u3iv8KqwqFE5RGHcO6CoGbBkjTM4ovpuZjbuoT_VoCVmxfoxdn2sk-TSPFAdU3kKdl87c14k2C0OsyQHyZIUEKP5XILROpGX_eVzkvLuIXyQWOlIp7k6hMD1_dYMIYJLCCtOJXaMGNzxAXtovTfnlD44J-bMBec_Sy4Wr9EHJfjusN6HfgKLsNsXubzQ6sU28yPBYgkjHHu-FJNn5GYfABn60mr8bpeLxA5FtoPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محمدبیگی: هیچ مدیری حق ندارد در مسیر تولید و اشتغال مانع‌تراشی کند
🔹
دکتر فاطمه محمدبیگی، نماینده مردم قزوین در مجلس شورای اسلامی، با تأکید بر حمایت جدی از سرمایه‌گذاری و تولید گفت: مدیران دستگاه‌های اجرایی باید حامی تولیدکنندگان باشند و اجازه ندهند بروکراسی، تعلل و ناهماهنگی اداری، اجرای طرح‌های تولیدی و اشتغال‌آفرین را کند کند.
🔹
وی با اشاره به احداث کارخانه دانش‌بنیان ۷۵ هزار تنی آب اکسیژنه در قزوین افزود: این پروژه با بیش از ۶۰ میلیون دلار سرمایه‌گذاری بخش خصوصی و حدود ۵۰ درصد پیشرفت در حال اجراست و پس از بهره‌برداری، بزرگ‌ترین ظرفیت تولید آب اکسیژنه کشور در قزوین شکل خواهد گرفت.
🔹
این طرح ظرفیت ایجاد بیش از ۲ هزار فرصت شغلی را دارد و می‌تواند در کاهش واردات و توسعه صادرات نقش مؤثری داشته باشد.
🔹
محمدبیگی تأکید کرد: وظیفه مدیران، حل مسئله و برداشتن موانع تولید است و مجلس نیز با استفاده از ظرفیت‌های قانونی و نظارتی، عملکرد دستگاه‌ها در حمایت از سرمایه‌گذاری و اشتغال را پیگیری خواهد کرد./نمایندگان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/693998" target="_blank">📅 17:59 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693997">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
نقدعلی، نماینده مجلس: بانوان فعلاً نباید از موتور استفاده کنند، زیرا هنوز قانون آن مصوب نشده
نقدعلی:
🔹
اینکه بخواهند با «راه بیانداز و جا بیانداز» کار را جلو ببرند، نمی‌شود. گواهینامه موتورسیکلت برای بانوان، یک موضوع دست چندم است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/693997" target="_blank">📅 17:58 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
امیر حیات مقدم، نماینده مجلس: در بحث توافق، وقتی رهبری، شعام و حاکمیت تصمیم می‌گیرند، سایر اشخاص باید از آن تبعیت کنند، نه آنکه با طرح اظهارات بی دلیل، مردم را به جان هم بیندازند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/akhbarefori/693994" target="_blank">📅 17:46 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
روس‌اتم در حال بررسی چندین سایت جدید برای ساخت نیروگاه‌های هسته‌ای با ظرفیت بالا و پایین در ایران است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/693993" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c80d548650.mp4?token=YznCsExgUDbW5dkFWgMZxelWDM0SOp9YFU4BfD575L65yPWxjPQsiUbu5Pqi-wAIpy9gJuDfpM_0Dh3rHhlTbOHSfb7WObjboQQoEWnvDsHl-9LtEJUjvfyaUsWh4JPC3o97ZLuFUekSElEBRWsynLg6zXIP-acUYTeOlRbkMoPwsOa3CdkvRsaYwJdkUGvJ3o0MBdLIK4QZcNQI1XGOZX-pBUX4JxRkJLvAIFWQtcFhemYKJ5520uAB1OyGK1ihvDrNLdnmsTp571SbRJzfZwsIT5oWgLM__186YWuSPwLjS9GgGSm8P6fhN7NdBGpn5_bYbfC0R8c1qowxqIj2Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c80d548650.mp4?token=YznCsExgUDbW5dkFWgMZxelWDM0SOp9YFU4BfD575L65yPWxjPQsiUbu5Pqi-wAIpy9gJuDfpM_0Dh3rHhlTbOHSfb7WObjboQQoEWnvDsHl-9LtEJUjvfyaUsWh4JPC3o97ZLuFUekSElEBRWsynLg6zXIP-acUYTeOlRbkMoPwsOa3CdkvRsaYwJdkUGvJ3o0MBdLIK4QZcNQI1XGOZX-pBUX4JxRkJLvAIFWQtcFhemYKJ5520uAB1OyGK1ihvDrNLdnmsTp571SbRJzfZwsIT5oWgLM__186YWuSPwLjS9GgGSm8P6fhN7NdBGpn5_bYbfC0R8c1qowxqIj2Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کنسرو‌های عجیبی که وجود دارند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/693992" target="_blank">📅 17:40 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
هیات مقررات زدایی وزارت اقتصاد:
موجودی طلای وال‌گلد، مورد تایید سامانه ناظر و قانون‌گذار است.
🔹
به گفته مجتبی قاسمی، دبیر هیات مقررات زدایی و توسعه فضای کسب‌وکار وزارت اقتصاد،
وال‌گلد یکی از دو پلتفرمی است که به سامانه ناظر بانک مرکزی متصل شده است.
🔹
سامانه ناظر برای جلوگیری از خالی‌فروشی و اطمینان از وجود واقعی طلای فروخته‌شده طراحی شده است.
🔹
بر اساس توضیحات قاسمی، هنگام خرید کاربر، سامانه بررسی می‌کند که به همان میزان طلا در خزانه وجود داشته باشد. پس از خرید نیز معادل طلای خریداری‌شده برای کاربر فریز شده و از موجودی قابل فروش پلتفرم کسر می‌شود.
🔹
در نتیجه، یکی از مهم‌ترین نگرانی‌ها درباره خرید آنلاین طلا، یعنی وجود پشتوانه واقعی برای طلای فروخته‌شده، قابل بررسی و راستی‌آزمایی می‌شود.
🔹
به گفته وزارت اقتصاد ورود وال‌گلد و طلاسی به سامانه ناظر، پیش از الزام عمومی اتصال پلتفرم‌ها، گامی در جهت افزایش شفافیت و اعتماد در خرید آنلاین طلاست.
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/693991" target="_blank">📅 17:35 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693990">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">♦️
سامانه رسمی فروش خودروهای دست دوم راه اندازی شد
🔹
سامانه رسمی فروش خودروهای دست دوم با هدف ایجاد شفافیت بیشتر در بازار خودرو، به‌صورت آنلاین آغاز به کار کرد. در این سامانه، خودروها پیش از عرضه، به‌صورت تخصصی کارشناسی شده و در قالب مزایده و با قیمت‌گذاری منطقی در اختیار خریداران قرار می‌گیرند.
🔹
یکی از مهم‌ترین مزیت‌های این سامانه، کاهش نقش واسطه‌ها و دلالان در معاملات خودروهای دست دوم است؛ موضوعی که می‌تواند مسیر خرید خودرو را برای مشتریان کوتاه‌تر، شفاف‌تر و مطمئن‌تر کند.
🔹
برای ورود به این سامانه و مشاهده قیمت خودروهای کارکرده از طریق لینک زیر وارد شوید:
https://mashinaaa.com
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/akhbarefori/693990" target="_blank">📅 17:34 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSUOB5B7RdALWskoXLY2OW9ZAcLPk4Di_B9pEqkG7vu3w6Ju3D-poDZj0wL9Ap_d4trOLkrqMZWiXE9ugSld9yFmNRJo5pquHST_iarI913vgH-ZxEipnT22mhVyozv4Le9vF1p0BP9cdnYLuWNjlqKyXUQZmQITsHO0JQZavoDNdjAFh02oDMzwcRNWbiqp_jk6GO5sVu88Uhzo4mQY5eijMeXc9FM87Wl1BYc7yQAq6uTNUVpmc-HfTQQJwU9vcJfwBUpgVdMawiulosNzbTCUt3j7DXWvayvEgsrH_RleKGcTeafmQjvT70FrOJXRh6XPga3eMOZ4P66Q6Fb_1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اولین علائم هر بیماری که نمیدونستید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/693988" target="_blank">📅 17:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
امکان افزایش 50 درصدی صادرات گل از ایران
غلامحسین سلطان‌محمدی، رئیس اتحادیه گل و گیاه در
#گفتگو
با خبرفوری:
🔹
ایران در تولید گل و گیاه رتبه ۱۷ جهان است اما در صادرات رتبه ۱۰۷ دنیا را دارد، یعنی ظرفیت تولید کشور بالا است اما زیرساخت‌های صادراتی باید تقویت شود.
🔹
در صورت رفع موانع صادراتی و زنجیره حمل‌ونقل صادرات گل و گیاه ایران می‌تواند حداقل ۵۰ درصد افزایش پیدا کند.
🔹
ارزش واردات لوازم مرتبط با گل و گیاه حدود ۵۰۰ برابر صادرات گل است و هدف باید تغییر این نسبت از واردات‌محوری به سمت افزایش صادرات باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/akhbarefori/693987" target="_blank">📅 17:32 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c1d4fe451.mp4?token=dQ7_zo5N-6zndpxlXH5yXYaMAWaHbEVZ5iaZgTTfyaFkKGNI0T6f8YlmdxP_ocNeYcZ3OWblHc5r19XXhdVzw7CTt7sfLwwUMVUVl8jC4sWPgUdgwTCSBnO_MjJgXmXKzEngo3mlB66w8PfWXaOYs9dREOwXohipj82ZCseSUgFroDmxq25PGhan3qtQeLiMU7HSAUVb93YDJam0Y1OvztlEHWN2bCD9_OleOrxh66nqHDnzxICU61HLIFA0846Zgq8mXyTa3zwpkIk7bC9I8TnCMiPzSXHLuPStloc5DDjqJE0RdoA6cjXw_uxzGt_ASTaj3BHC6FigtHKzEv_AslkvrYhTAhbeHWr5WBWtuu31JzRokBJ1lBEsDYn2wob06ZFA4jH7Dl9Kyl8bVU08MM3pyMTdh4GhBXmsiACAfCRftxbMrjauKH9QOYH-BaJypGDgUDirTvnPQGgMWDzhltx9mbEh0p5mAHI8yUFKjZ63NcRwNnDCaqI3CU9A1Mm8o13bO1iT9Y0_ixWRSAhgY-ECdarbBx-jGKO8pRZZq8RP53zrjoMvGAhZ1nJGIKs23hgo74STe4GD5MmSPzQMF7hGkps10VpO-lUUwCyvc3WTIQ458aEV5zMhN2Z5YaaQwAo1oTWaFqtwI9M0J9n6bpCfrfVTQ3rt_nDUvSAyxdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c1d4fe451.mp4?token=dQ7_zo5N-6zndpxlXH5yXYaMAWaHbEVZ5iaZgTTfyaFkKGNI0T6f8YlmdxP_ocNeYcZ3OWblHc5r19XXhdVzw7CTt7sfLwwUMVUVl8jC4sWPgUdgwTCSBnO_MjJgXmXKzEngo3mlB66w8PfWXaOYs9dREOwXohipj82ZCseSUgFroDmxq25PGhan3qtQeLiMU7HSAUVb93YDJam0Y1OvztlEHWN2bCD9_OleOrxh66nqHDnzxICU61HLIFA0846Zgq8mXyTa3zwpkIk7bC9I8TnCMiPzSXHLuPStloc5DDjqJE0RdoA6cjXw_uxzGt_ASTaj3BHC6FigtHKzEv_AslkvrYhTAhbeHWr5WBWtuu31JzRokBJ1lBEsDYn2wob06ZFA4jH7Dl9Kyl8bVU08MM3pyMTdh4GhBXmsiACAfCRftxbMrjauKH9QOYH-BaJypGDgUDirTvnPQGgMWDzhltx9mbEh0p5mAHI8yUFKjZ63NcRwNnDCaqI3CU9A1Mm8o13bO1iT9Y0_ixWRSAhgY-ECdarbBx-jGKO8pRZZq8RP53zrjoMvGAhZ1nJGIKs23hgo74STe4GD5MmSPzQMF7hGkps10VpO-lUUwCyvc3WTIQ458aEV5zMhN2Z5YaaQwAo1oTWaFqtwI9M0J9n6bpCfrfVTQ3rt_nDUvSAyxdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای نتانیاهو جنایتکار: دشمنان می خواهند قبل از انتخابات اسرائیل به ما حمله کنند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/akhbarefori/693986" target="_blank">📅 17:27 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
سخنگوی سپاه: هیچ شناور آمریکایی در خلیج فارس باقی نمانده و شناورهای آمریکا دست‌کم ۵۰۰ کیلومتر از دهانه تنگه هرمز فاصله گرفته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/693985" target="_blank">📅 17:19 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b29cf3393.mp4?token=o1OoOh6kg35LoIPSZ4lcpuAiYKueODQ2EzOx4toGQdG6cTE6MFOBwRXE-bPWVHFqRQhgyudAHEByNfJPCmmh4olH6n902xq85dGVpPvhtmILsSF9iIHeZ2d4PtFUq2QJp5MnaDhTpQ_lEEKGm7XGhjEWUxIGb06a8rEmX7crITuOij2YOSEN3U8KzW5ra7V1oYGanCbwe19jjDPQImuWmeBFUklj2CV8v13u-I6d6v3d6WmgiKkPfyEtiyge58voQkgXrSmTPic-CLGFNi5W62hsvWzGnkuaer70-9TRcS9zLmKlwY66eNsN6BeiBS6XW9GrWWLxyWXK9FvcuJ6jCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b29cf3393.mp4?token=o1OoOh6kg35LoIPSZ4lcpuAiYKueODQ2EzOx4toGQdG6cTE6MFOBwRXE-bPWVHFqRQhgyudAHEByNfJPCmmh4olH6n902xq85dGVpPvhtmILsSF9iIHeZ2d4PtFUq2QJp5MnaDhTpQ_lEEKGm7XGhjEWUxIGb06a8rEmX7crITuOij2YOSEN3U8KzW5ra7V1oYGanCbwe19jjDPQImuWmeBFUklj2CV8v13u-I6d6v3d6WmgiKkPfyEtiyge58voQkgXrSmTPic-CLGFNi5W62hsvWzGnkuaer70-9TRcS9zLmKlwY66eNsN6BeiBS6XW9GrWWLxyWXK9FvcuJ6jCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی از درگیری فیزیکی مسافرین در یکی از هواپیماهای کشور
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/693984" target="_blank">📅 17:11 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVvHAlTXUFxdS_bE-VKY-HPj3EW5M2ydE8vRgiikRtn4kbXGhAfC4KHAHOX_axtrW-NvGXVbRjus26hhivyKIzMjuKzQvBXQJOr0lx_S4h2m4HPPWqqmxcpPyar8JfNKe2qwBgLOFaf7iOR58Zu6DM43vQEM--cFHXZlMqQdwRheUMroJ3qyMRxpBaJuWZhINKUFIDpsguhmfE56fjrMrqh-Rd2pCko-8Cfh2i4-iLoJKVON8Jl1MuSwJboJnzQnEmmiLQOFfjSHcHqq8iVvosXH74jUEhlnAGKyyJTfXYWxqFkhRrAw3zUdnqOjM7zrx1DCmrcAal1HEZZPFdQ0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتبار ۲۰۰ میلیارد تومانی برای خرید آثار هنری در دست طراحی است
🔹
سیدصادق پژمان، مدیرعامل مؤسسه کمک به توسعه فرهنگ و هنر، از طراحی ابزارهای جدید برای تأمین مالی و توسعه بازار هنر خبر داد و گفت: برای رونق اقتصاد هنر باید هم‌زمان عرضه و تقاضا تقویت شود و زیرساخت‌های لازم برای شکل‌گیری بازارهای جدید فراهم شود.
🔹
به گفته پژمان، توسعه نظام اصالت‌سنجی و شناسنامه آثار، ارزش‌گذاری، بیمه و امکان توثیق آثار هنری از جمله برنامه‌های این مؤسسه است. همچنین استفاده از ظرفیت بورس کالا برای عرضه و معامله آثار هنری در حال پیگیری است.
🔹
مدیرعامل مؤسسه کمک به توسعه فرهنگ و هنر همچنین از طراحی مدل خرید اعتباری آثار با مشارکت شبکه بانکی خبر داد و گفت: در مرحله نخست حدود ۵۰ میلیارد تومان اعتبار برای این طرح در نظر گرفته شده که امکان افزایش آن تا ۲۰۰ میلیارد تومان و بیشتر وجود دارد. هدف این طرح، تبدیل تقاضای بالقوه به تقاضای بالفعل در بازار هنر عنوان شده است.
https://www.tfarhang.ir/_تسهیلات_خرید_آثار_هنری_تاسقف۴۰۰میلیون
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/693983" target="_blank">📅 17:10 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-693982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecbe0f8dec.mp4?token=T1oeHYRayOYubd7SkgxcbQ2jcH7qAneE_fVG8b8zn4FXTYTnzvR77lpEjDWpKseGMDzBLiUe8StXTlgoTmeJe8hh8md0R5TMNsV1O-Z5Ti_MReC44vopygGNkmAFHwf7AbIi--1HT_Pk1PDb-1OdMKoQVhXOJZESodpdGMwd1J9Z8i9dGa_ITOP3-yaeZ3UysAFnILWrYvkjxXFFeWCeOYnwXWxzzZBO_fz71LdaTKbYnMs5qx7ig6ruOzAMQZ885YgUtpBu_7yXZI4_ekC6GI7kZzLMraDIVpc4UOQyt3azJbLyIHXuaupHI2wYmsLdifo9XaMVErItFVon4qAFgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecbe0f8dec.mp4?token=T1oeHYRayOYubd7SkgxcbQ2jcH7qAneE_fVG8b8zn4FXTYTnzvR77lpEjDWpKseGMDzBLiUe8StXTlgoTmeJe8hh8md0R5TMNsV1O-Z5Ti_MReC44vopygGNkmAFHwf7AbIi--1HT_Pk1PDb-1OdMKoQVhXOJZESodpdGMwd1J9Z8i9dGa_ITOP3-yaeZ3UysAFnILWrYvkjxXFFeWCeOYnwXWxzzZBO_fz71LdaTKbYnMs5qx7ig6ruOzAMQZ885YgUtpBu_7yXZI4_ekC6GI7kZzLMraDIVpc4UOQyt3azJbLyIHXuaupHI2wYmsLdifo9XaMVErItFVon4qAFgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه به شهروندان درباره استفاده از طلا و زیورآلات در معابر عمومی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/693982" target="_blank">📅 17:05 · 07 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
