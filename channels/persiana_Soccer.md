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
<img src="https://cdn4.telesco.pe/file/dPqY9QQV9S6tjg_RMDBo9DPYTJrlqg3NYmoPyCE5hS9oQVslh8vk8g3_5JUa_N9b3D7FtlyQyQfQJQWsx1vpNPXGwRy-9C62-5VQMhplOaH53wgLj238jH7In7t1FjIuc8Sdjj_gMGGt-NNTjfCiLI6p6t9aLyjFjiaWGnv04jTAWUDHrKnyZtJ_qnwihftul86ReJ-xejRCCj_6yH1MaJBN8NIg4DRX4OvDoQHTTKPGdunrIcPHNzpKIqZo9v-B5v0q2oyvxwoNb8SCtOcbHP_u3ViRShh6VNqvq3qm4T-zVe5pgXXXKajEt9rZwiVfu7xLp13gyXfMp9wx18a6Cw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 195K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 10:53:40</div>
<hr>

<div class="tg-post" id="msg-23168">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RURlI03MOKNnZNhB2MJVYRxVNMi4JIB75csk2mGUgnG74ECVP_fvoHoTvf734nLuiYnbbdUHuc8V5oN_bPj2vIAWiTyUhR6sxGGEGC7v2HLAgfz8CTervxFMV02rRcSEAAHupdpZwiLqiQs4lE7MvyPXLcbu13ijEvkArFbo0W4oSqDy7Nksz7jHz-bnr2m2uNxu9F4lLvXL3rbYAoi4_LAuoccIj5gRoMJqhXuFZmip65UFnDo_9cTE9bN_KMmqgqzjR0jlmDFUQzBh_ESsuv3ERYa9q6Iiesm6ICIQ3oDgHCoHwDtd1O2IuqnUacvvTI39thpskVEM2A5UUvXjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛شهریار مغانلو مهاجم‌ملی‌پوش‌باشگاه اتحاد کلبا نیز از دو باشگاه تراکتور تبریز و پرسپولیس آفر هایی دریافت‌کرده و درپایان رقابت های جام جهانی پاسخ نهایی خود را به پیشنهادات خود خواهد داد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/persiana_Soccer/23168" target="_blank">📅 10:51 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23167">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22d9a8eaf2.mp4?token=VgCc_GXdzj-IjF7kLJx_RTced0-7kztpp6iUuvOZaco4xNjB0E99Z0zu9cld2O3z8yqNZHbaYKjcAc1KXdmpaJLG1VoCQJnu8iz0A4-uucX-jmdPFVXeq10XwryhvqXrYi7TfsSZ7UTpboBpr9i-r7kqdJwl_PF9_0zAfn3YmLbTp5DfsZBprDCAbh_Ll0czkqXtRt-iZuaT-GzJ0L5R6alax_IvSgZM57uUMx559tnoVGs7HRKfFtpcHMlmQpolV-_3d7z1uPstU85LVkhC0P6oYBpgOmCq5ALJZlotv2zRH2gajxSttoHOYiMS2C0WJrW250Es8LN3WcD0aPd-Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/persiana_Soccer/23167" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23166">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRpynZMVFmW316VFk9Kd1ZdpJQKR3_g6fd0y2Mby7o8ReyMXEHqSEUMNj0h-fzt8DdOSe3yn13B0FS9TPMcJGvmK6T4W2R94LRGD4C72IzNtVPTGuIZdABvyXf89T8DzsEReIWBaLBx5-ztHEgHKElQiHvLvIOTmdW7yWeJXNN13vpRXuAoGk2Bo3dCHPrUTfZHcfQzCZetAjYHhjUNNg05LIe0BFNWDHr9b3qZkU6xjWs3fsSjqe0Rgi1sSz2q9hUO-TRhLBjjuDGqiXhXY1Hic1tQ7CWJm8VWIlWvzNM8vFlJW7rVJ2wnMKuDMXK_PkXO7zVbyvzZKxbzaaygtKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/persiana_Soccer/23166" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23165">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyYFvDVEFUYq78Oa4wiCkVmSMkGW6P7kFCQZTF5Fi5VRDadhFTxPoUJEwhCR6AD9FrX3-71m5y96MgidnOWBhHcBkzR9cyvd3dYFvFGKM9tK4vaDcL60QhyU80LRtMmD1_WujzOrci-1VNZcXFxw9XAEczBb-iXYiZWrjBl5gngufZr6s9L5jdADtRbqOsFC7kHu-csaHnYarbx_Ud_IInYrUFQdk6WgZDg0bzQRwgQmoClL4AOkehG1GS6fJESH7yNK0RrlzSc9htiGNv1c1SubWxH5UxFRS5qp14Hmww027ihnLYP7Q24mji08Ey_Ij0tHiRvRhHqM--Gy-MWaNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا er21
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/persiana_Soccer/23165" target="_blank">📅 10:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23164">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKBt7-45pQc_jrqvGjzoHjgs_YZc_8Pq4gU6tjdy13NWDWChbUFKmIZGISIWR28Jp08GoyHtnTzDnBX-qrQF0gYhc2QA-FYc943y2Jy8xkoTU3K3uweSGFp-bBy3t510H4rqrAW43lsjo29QSDT_FBv65LeAfzxZ_IZbCHRbyB_f1qZOuw-fjuzjq74nR3qVMupMldp12YnEd_6NbLCXbGFUQuZjbvzrIkNvvIkehMybDx12k9apaMVDA9QJBPQOBqmntMMKIzjdrs1q2VUY6nD_VOU2KjVEs3k4lMBgXwpqVAdE0H6hYWrmca-xTnCw9zHueWBagGdrUho4vqg3gDJc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e065f47574.mp4?token=YqM7x0yONjxtyEfiOd7bQwxUtOR4gZ1cuQ9JiNQmq9k48jixPl7ExDKZAPknezrcHfBmtflTPHsTZRRdfh2WMLrKiJ5K59O3NUI4f9TSXHuXmBHjnLsh7nZlEZoHxmZRW5ZhJIQOr1aH8nr45qfKmq1SfPLjMZTDezPRTOFCF3lvDgfZq-o9Bu_vZ3cfIJgsC3h2C0Z260bXj8G8OLmb0_APwesayCXpL0G_7pniyvB4AXvFRwFwVW_xLxRkZPQnvEvlCPrZSZ8fb6vblOxEDR96gcRtdA4J1JbenIcdoj2gcwBq2pRZg1x9JgfXJ4JvXyqz4kjHrrlqr2bkYnfGKBt7-45pQc_jrqvGjzoHjgs_YZc_8Pq4gU6tjdy13NWDWChbUFKmIZGISIWR28Jp08GoyHtnTzDnBX-qrQF0gYhc2QA-FYc943y2Jy8xkoTU3K3uweSGFp-bBy3t510H4rqrAW43lsjo29QSDT_FBv65LeAfzxZ_IZbCHRbyB_f1qZOuw-fjuzjq74nR3qVMupMldp12YnEd_6NbLCXbGFUQuZjbvzrIkNvvIkehMybDx12k9apaMVDA9QJBPQOBqmntMMKIzjdrs1q2VUY6nD_VOU2KjVEs3k4lMBgXwpqVAdE0H6hYWrmca-xTnCw9zHueWBagGdrUho4vqg3gDJc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
مجموعه‌ای از بهترین آهنگ‌های ادوار جام‌ جهانی از سال 1998 تا 2022؛ کدومشو دوست داشتید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/23164" target="_blank">📅 09:48 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23163">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJEiBj2yF-RejoDEih52D4SFwnjPdAFEx7qbXMmuPQaqU1uFSYS3BVC7JH2TwcrfzlMSU1dUVAY8ui2BfI6MgBEJoMbygkWtxqn4hc0rW0336IAbMv2AEwsgOsHIt8VKguyky4Q-EFxbsRadlq267j0VLUS6G-m2FeJkWpNrGqQfOIGh1xyWeoRbl1XTAcDnZHSOv6RPsIhK-QY9CxKj2D4YpWeZ7XCXlFBDJPNhcV5-YgOxi5cMfg4bq1-Dhzbbdho6x0dT48g20IUgilCLR9RRzIlXOzcPo3imEWjmHDGxeS82S-lUD2IPtA_gutOsJyG8_DBGg7WDFfvJHt5mug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/persiana_Soccer/23163" target="_blank">📅 09:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23162">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VX_FykYT2c7ggN673H-mXYpF_Kq1kfWnA_9FmAkViWAJbhRP1r-ienkA3HZIyJtcYzqJhsq-_7KjMVRhQla2myLSDGwpDOASIAiNy7xDwi6OrKVhd91-qdUh2dnVGHvIAmp_s65PWYe19JJRXNmFU5FXFY3W6LFfBjz-9R-vHQVJVgeQHQFoS7m58xSfqXjS8xBCDyyGfefHw-TjoXnvWRw-3qAvJNnki3k_lRE3KysK0i9kbWV3iAoAMb5qAPe8B003VJlOLoAjGcTaGyqyoDb7bin1NCAPw-8oLYjKX5Se_3CZ6X0kqABmTy2GunjqX-_f1viodksDALEJXv2l6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/persiana_Soccer/23162" target="_blank">📅 09:12 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23161">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=WcigupZMUlvq7GUYh0bLfZiyUkj-mLEKhW5ljkFQRrV7ttuLXhqJbbeTFDt7_40Ttu3zZO5mu1lr2Fwi2O1viFZKxup3dP_Wi9Gp-SVMfaIz3oClNA6laxaIRTgT8tv6j7KRts90jJAa8pcLU96-1WgT_rdS3zDCBDFBCRyqbrmW-VP7kBS4ERGiWgRW9LMIaJ7UdMEBL7-9G0rMUeZEw7JtfJCn7-4zdaxqVWQ3q7rEEDXLfIl-El_GwppFL6zVSyP2zSIUGw7DqE0KvCIPVG35H9BL0YFu_045XTTdxWRxI25kt1f_DtCxELka8o64MayfDQnNADGoOdyPFOft9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1bdb0ad97.mp4?token=WcigupZMUlvq7GUYh0bLfZiyUkj-mLEKhW5ljkFQRrV7ttuLXhqJbbeTFDt7_40Ttu3zZO5mu1lr2Fwi2O1viFZKxup3dP_Wi9Gp-SVMfaIz3oClNA6laxaIRTgT8tv6j7KRts90jJAa8pcLU96-1WgT_rdS3zDCBDFBCRyqbrmW-VP7kBS4ERGiWgRW9LMIaJ7UdMEBL7-9G0rMUeZEw7JtfJCn7-4zdaxqVWQ3q7rEEDXLfIl-El_GwppFL6zVSyP2zSIUGw7DqE0KvCIPVG35H9BL0YFu_045XTTdxWRxI25kt1f_DtCxELka8o64MayfDQnNADGoOdyPFOft9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇺🇾
جالبه بدونید
؛ مینا بونینو، مجری سرشناس آرژانتینی، تنهااز‌طریق‌چت‌اینستاگرام با فده والورده ستاره رئال مادرید در ارتباط بود و قصد صمیمی‌ تر شدن نداشت؛ اما شنیدن یک پیام صوتی از فده همه‌ چیز را تغییر داد و او در جا عاشق لحن والورده شد.
‼️
درادامه مینا دراقدامی‌جنون‌آمیز و ریسکی شغل موفقش درتلویزیون را رهاکرد و بایک بلیط یک‌طرفه راهی مادریدشد تابرای‌اولین بار او را از نزدیک ببیند؛ تصمیمی بزرگ که‌سرآغاز یکی از وفادارترین و پایدار ترین زوج‌های حال حاضر دنیای فوتبال شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/23161" target="_blank">📅 09:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23160">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=Il_PLm0s4EeFfni-8W9-KGhIhddZzkJK-BhQ0E6D8GBaXepK4vmiiGnrlNhI9yn8_9987twmCTeA5VHedGcTjeGzzit1KNn6Lyba6-3ffG-RIifW0b6tzBA7ryXXXf6TxBQLhZbRDt47nJcqFu4u0SC3y2_SZmcky8s6sLs-LKrH99wkmm6fXSAc81Cq274nL8MQtNefbTxhVjfRN8Rxt9TcDX4U3y4gks7dV_Ovb3HYYmH0pa65CjVDrXJGaZcnZhr_lskYQs3HbB7mobXPv2JGuFcFhKQmfCDhFKiRtWPQ1m0zhiP6tS-4WLHOdG7jLvkRNWwGpd4K8YTL71lfYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea36e1943.mp4?token=Il_PLm0s4EeFfni-8W9-KGhIhddZzkJK-BhQ0E6D8GBaXepK4vmiiGnrlNhI9yn8_9987twmCTeA5VHedGcTjeGzzit1KNn6Lyba6-3ffG-RIifW0b6tzBA7ryXXXf6TxBQLhZbRDt47nJcqFu4u0SC3y2_SZmcky8s6sLs-LKrH99wkmm6fXSAc81Cq274nL8MQtNefbTxhVjfRN8Rxt9TcDX4U3y4gks7dV_Ovb3HYYmH0pa65CjVDrXJGaZcnZhr_lskYQs3HbB7mobXPv2JGuFcFhKQmfCDhFKiRtWPQ1m0zhiP6tS-4WLHOdG7jLvkRNWwGpd4K8YTL71lfYIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاگردان‌جوان‌روبرتوپیاتزا درحالیکه ست اول رو مقابل تیم پرقدرت‌برزیل فوق العاده شروع کردند اما درنهایت 25 بر 21 این ست رو واگذار کردند. پیاتزا درتیم امسال پوست اندازی بسیار زیادی انجام داده و بازیکنان جوان زیادی رو به تیمش اورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/23160" target="_blank">📅 07:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23159">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=TqB2oHR9AS-QUJproJsVwDB0r37pmCSQdGs9nLXm3HLo8zRGbAtgLyOQpd_SOO0IMLjW1d-a_-Uaki5fDi7W8qPsmPYcp2DD1BJQz67gm202qe80u0vaZGErRLtJouGTQiDGLUwR2Fz81u9zttfcZdheN_vnBu_YpWsyCyTY-Dw86Kal8fc3TAnhKWfwuQekr33EuCx4Fv8MIxI4B2Pbt4GeL6VHNE6aOpBFqAogtK_1Oi20f21TFtrtlO1G96VNEI293vELSUSpRv5y231LCUTWnCwtbAHuyVIKI5XvLyXqRYVGLt-9753CRtamz64q62MczQnjtwvUkVI1xfQJJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bfa3df8180.mp4?token=TqB2oHR9AS-QUJproJsVwDB0r37pmCSQdGs9nLXm3HLo8zRGbAtgLyOQpd_SOO0IMLjW1d-a_-Uaki5fDi7W8qPsmPYcp2DD1BJQz67gm202qe80u0vaZGErRLtJouGTQiDGLUwR2Fz81u9zttfcZdheN_vnBu_YpWsyCyTY-Dw86Kal8fc3TAnhKWfwuQekr33EuCx4Fv8MIxI4B2Pbt4GeL6VHNE6aOpBFqAogtK_1Oi20f21TFtrtlO1G96VNEI293vELSUSpRv5y231LCUTWnCwtbAHuyVIKI5XvLyXqRYVGLt-9753CRtamz64q62MczQnjtwvUkVI1xfQJJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
🏐
برنامه کامل مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/persiana_Soccer/23159" target="_blank">📅 03:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23157">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1uhPTxIJPwTNXSTjWNLKv7M8XAcNKxMAzWwByMBmoXLq1uEqKC0s4i6AWodHNNfbhAYdyMRAAbUm3UHfUOLTHy7THvcIKJ6-tvgFr9kcvtIX_MGxlSNYRXVFnPdHg0exH7zwYRWT92RExvXRmjKDPswIdCXjCqknnLZ38zgvrjnhku8ksQeFuFJzIogixGSs12fnQLaFyD9ydwZ4bgjlEibdp_e7KPq4kFgNFJzvPYnMkfVx-oHyAIq1boqs9xli9lxBGW7WE7YI5psGRx5PKApkPpCfbyyWYv2tnfG18mTQ00XVtqyaBUvtBXIeUIkx_a7X6iSs67ij1cqS_K1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تورنمنت جام جهانی 2026 بادیدارافتتاحیه مکزیک و آفریقای جنوبی
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/23157" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23156">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cgu-0i0HwcHnShBGk8o0SgOSl-kzkdDDhQkhVErQqObqVPPQiqvqs9ROzX7IzTUPxPbJVEi9rwEVeHqlaaUS5UEMtpYMj4G0zL9n9JT0SCCHNIP4zHeSf4RvskpscCczACYdoLn-UQTDtNWeCpgEKsDDcs5PvrrDYEodEZAu0r2HGn_HI_NTs1PAl8CYCcIkSUcQ8EI1z6goQ3wXw-kZ9qkOSwPdMeX6AOfkHtgwCaRHE3rmmUyOhMCy8dwD6JKiKumxjHB2t3CBpJyWTfL9rcruB8HF5jraoN8uMIiEfhj3mydMq6RYxsRVDVi94NxK6uhsuVjP_mqoRL0eeZgYJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌دیروز؛
برتری‌آرژانتین‌وپرتغال برابر ایسلند و نیجریه‌پیش‌ازشروع‌جام‌؛ انگلیس هم تاپایان نیمه اول با تک گل رایس از کاستاریکا پیش افتاده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23156" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23155">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3oHlPFNU0jhyoyxFY_Lb1V1gHpWiApA-0-bx_8XPCOjauQE49-ZvOE46rag6dHHIJwdeSYUiPuV5Isr4F-1ghrukMByxZynNxVl5_o82_RiKwfpF3v2s7pMsgUQG9eEVbuju-BeGYZa1f9MYcs5YYc27PskuPjS12NFPgOhCeRLaeDZ-z1Cazl6IvFVhCpJ676S6qyVt89gpccsp98FT2apqtFQr8W0WCGtIbb3JniHxBRc0zBh53IL8umcNCNhOW59ws9yqcjqTjojSZS2W7_k7x7Nqy7_zJlhYKwyCOB9U6xsNCgG_nIv6rfghWp9dpoSyZwckSErE8SAh65g1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
— سنتکام آغاز حملات علیه ایران را که از ۲۰ دقیقه پیش آغاز شده است، اعلام کرد.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23155" target="_blank">📅 01:18 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23154">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">▶️
هایلایتی‌ جدید و کامل از عملکرد نظمی‌ گریپشی فوق ستاره تیم‌ملی آلبانی که مدنظر سه باشگاه بزرگ پرسپولیس، استقلال و تراکتور قرار گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/23154" target="_blank">📅 01:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23153">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA9DAZidRSVSz4vYGL0qUWwVoQ7nD7G5ysmn7T6_rpGN2zlpmvqcIES8-fWUjKUC3Yfg1dfmturOp1uDn5Z6e0FUPax_E8BVJ4TXxoBM6FHudPlKlopbcDCzpOApMl9W6FjcWbv__xk6g7CCbFYDKP_UP9Y6XVDyiftvcKSldM9jno3UNF8vUPWXwx22mjwD7wRbTSojh4I5sDPHl3xi5HTOm1kUYX8ZxPvxtMu46u6Fy4a8ZJpzbHXRoLg7hv2np_xSJa4OqxQFLXRyBPPC0sy-pTubTQSTdmkDnpiH3knimHvLyeYn0AweKFbxOEz5NjEjFrkTtAzJw0asDrX1gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ادعای‌‌سانتی‌اونا: باشگاه‌بارسلونا ساعتی قبل پیشنهادی 80 میلیون‌یورویی برای جذب یوشکو گواردیول برای باشگاه منچسترسیتی ارسال کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/23153" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23152">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=BKnePIhP09urgLKuRajBepnoXmSPLpELWnz5FUT3hbK9EKGLr61VJXjanDKH-nsI4MesHvin8hFa183JUEVTTgpYJSHjMpGIzR3I1XyafNlc8VrHmtYSacmd_ID6W_8uFciH4BRdDzfM66LEl2F2fgAL5LBYGNS96XuAwWlzILl12zhHr8PD2ADE90WkM-fa4D4ntVBkiREEoksWbZDhKIwhwDwFcAkwHenHuYrw-y2gtJUhzR-IBqeyMnRiYpq923kwG46yPEzWP0kE8hSqqT3cQdPSuZyAibOuTtsfiJziZ_0lM-BF-BLdlODzR83L75TeoChmWApucOoMdGFqLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d36c28277.mp4?token=BKnePIhP09urgLKuRajBepnoXmSPLpELWnz5FUT3hbK9EKGLr61VJXjanDKH-nsI4MesHvin8hFa183JUEVTTgpYJSHjMpGIzR3I1XyafNlc8VrHmtYSacmd_ID6W_8uFciH4BRdDzfM66LEl2F2fgAL5LBYGNS96XuAwWlzILl12zhHr8PD2ADE90WkM-fa4D4ntVBkiREEoksWbZDhKIwhwDwFcAkwHenHuYrw-y2gtJUhzR-IBqeyMnRiYpq923kwG46yPEzWP0kE8hSqqT3cQdPSuZyAibOuTtsfiJziZ_0lM-BF-BLdlODzR83L75TeoChmWApucOoMdGFqLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادی‌ترین‌مدل‌‌موهای‌بازیکنان‌وقتی قراره تو جام‌ جهانی بازی کنن؛ گل‌سرسبدشونم که برزیلیهاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/23152" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23151">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz5JBdWJyWuLMeeuf643CLVSy7QJW2fsK4mm232zAKkWL_R0Y3NAryeOs68dyQZ0sfQ4YffXJdm29jBalwZhjKM63VW1UJ7Tc2umSkOmaDdjIOqw3NzOSMEB5na4Vs8cLipT0FGFQJFhAhbxrWgGi-qCh0sZJIcbHzKTzMtoxMzt4eyV0aadc9GXrktlVPsu8XDr4SzyGDi0UoiQnfBwlXb8JNadjMf1b6wtyT9DK3zgrLBwHElpwwskhXCpMa57TwzkJstQQi90vRiy_jzD6DdzWoFQ_odV-raG0ea5h3wwlKgqBhX2LgOtzlYH7AcxvhHwE4-bp0TVtNuIsLiD4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕔
انتظارها به پایان رسید
📃
از سایت وینرو رونمایی شد. معتبرترین سایت ایرانی
🤩
🤩
🤩
🤩
بونوس اضافه به ازای اولین واریز
🔴
فرصت تکرارنشدنی به مناسبت افتتاحیه
🔴
⚡️
هر چقدر شارژ کنی، بیشتر هدیه می‌گیری
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
و هزاران امکانات خاص دیگه
💰
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا ea20
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/23151" target="_blank">📅 00:56 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23150">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqve1OxPPhOtaXLZpqDckT92I-zgnAwIsFv2jVBWE7BF-tc1tLGq_T4mgEzww50UCtXpuCvKKCH2mr1p8VPyfRwbcMDIeTJ9EajI-2Ywl2nBBih7tlX0Bin-EMeS-YYSgeFT35xyebSBRt32qsecmIo9FXYEYWZlVXC5l3gGNSRQufF3pQFTpEteA7Mq1wisLkiTsjhZ3mJFULetrfXMOUQzvPvPbL8p9aglchXbZ0JPHmR0OrKQUQ1HcG0XhDeEBPx1uxgx8A_SbdhkQeX-HvJAWIPPTqp_J0fQrWKbfzDmVi9WXCs1twNPBpugjnIF_5dGqKkUfgvlvxgiUbcczA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/23150" target="_blank">📅 00:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23148">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxsxLPmbpPWlPAL-xJPVwqSnzhcc2FWfUX2iywuUcTLPCCtkwZpoRoE62QJi9dVe9KpmfUPgvAON4--Zv1gcV5HHG-FlLOxBBxFocqwib5bji0d1tPHWSFT-9hr8uJotZK_vZCDstlvMZTfjkO1R4mB2mpEetpzCI6dac8WWfWTCDHL-QUFvrxqJJi0CsHsUVwaSGwlOABoEuNuj5PQX1ljqOoFsJNWnqRfswsel7eqdgxYhMkYuIgxTIro6jDAnA4IKuoykCjyyW7hloiVN-NgDfYow0c8Z5N_OpHH2GfKvTBWIUTUHOS1RPovBZZU4I7VxjH_hhasD70vWdX3nPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/23148" target="_blank">📅 00:24 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23147">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=KN11WJhmwU1pbwPqVhSKtTvTj_jaO1Nd-D-zzsSSzg9fHX1rIAkPoUmn5i6zcT5NNhynQTkegypoOMm7RQsBIYjKeJRc6qPUxfFi2_qLpP-r95pu4H5q_ktONRrpQg7J7fWVDLqlPI02RlcWlw2-HRP2zg5DxhpTnARo9VjVncQH-VSD5Jvs3gk6b2s5CJHTrzRC4jpXU0r8jXGff5ErjFMQdD-5K0IhihON3cFNyDiCVduRFMP64xTcg6-_pf0hICz76zW9hEdYfvMxW3Ue2kpgUUVk3yg80gM4dqwcG9wBBYK-NcKHaQQ4aldaGdIQlYrOuzUyIepqUFKE-nZz7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ace048c41.mp4?token=KN11WJhmwU1pbwPqVhSKtTvTj_jaO1Nd-D-zzsSSzg9fHX1rIAkPoUmn5i6zcT5NNhynQTkegypoOMm7RQsBIYjKeJRc6qPUxfFi2_qLpP-r95pu4H5q_ktONRrpQg7J7fWVDLqlPI02RlcWlw2-HRP2zg5DxhpTnARo9VjVncQH-VSD5Jvs3gk6b2s5CJHTrzRC4jpXU0r8jXGff5ErjFMQdD-5K0IhihON3cFNyDiCVduRFMP64xTcg6-_pf0hICz76zW9hEdYfvMxW3Ue2kpgUUVk3yg80gM4dqwcG9wBBYK-NcKHaQQ4aldaGdIQlYrOuzUyIepqUFKE-nZz7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
از پیت‌هگست وزیرجنگ‌آمریکا:
سنتکام امشب درگیره چون پرزیدنت ترامپ گفت ما امشب ایران را بسختی خواهیم زد و این کار را می‌کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/23147" target="_blank">📅 00:17 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23146">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDGNjWOmDlIlRLpFG4bYaBtWODNtajbhPY8Dy3Ul9Os9NboJbRs4u09c4BoiSuo8gaUeTX2kPEpGEvUs5Zb27FM_IxxI0J_70PjIQQZ1x6ARqTNdZ5t7-NQhIWRce6NCoBszhHroOdcNymNxcJ370MQWhJvjdyoYWdYwMOo5GhpccQMKk6o9-Fydo4LFqwQ46l0ZGj7qG-ROY42E6sUaC2vqxfozfw0xpAcKitU_3apIBUgcnqak7qaqzPNmT4Vd3ttShMZbAho7ifthiMjVgXOkq7A15DfErWt9Yj2nhZQZ5EslH--g_z1hGwI3JIJl2hoRNlzVVENKi07iJp7NRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.3K · <a href="https://t.me/persiana_Soccer/23146" target="_blank">📅 00:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23145">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah3vV5VEdZOfy7dWIX5LJ9bkivw-N6Uuq0vU3t2aUiPCAd5HeV8A8nlnoUhFFbD4pnm0xKRPbkqNyIuSrIaf9pdDOjaCpfGC8WJh37QWUawOfdf0LINDkfK932vIGnkSTjA_c0taKns5Vc_dipcCdnLP46fuJYkC0DhwjcmgMSpjE5onm0ewHIVzKFIB4WeSm5zJil4e_sp4U2VL6Sxs_wdc_kX5uq1IHvf0_l2AYPT6tgyT1Fukg7J58AA6MzDKUKlDxqjADwDofevoXr1XiiUvMhFMCnyFRmADUxOaw931GmLUmySaYCHUvdnQzvIHaRd4hcnCoq7HXUqBQPZb6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23145" target="_blank">📅 23:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23144">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9VNgN-3F8BhGB6QbulZxPdQQuzyy0yXwc8Roc_TgHcy_om1xQHG2Xd8z9Kwher2utEUhNzb5vP21jovvIYuWBgwXt5CLDhF1YhPJc9ayf8berreAz8xiQRUsumaxv_76LghuCep4yJySKL69Al-Bda6lRfDPgc8EMbjwT4tGjQEw6gxNJQjH8ljen3Rp2FmPs1LTsH1od75FvUFyTuUnMEPSAIS8efYMJP1P3j6i12vztGH8kZA-n7yX_NVhibb3TXASTo6gxCVn1qdlFaKfkFjmadRM6F7YxhLfgCF0rt8hvo4V3-wnBS8xjYMd11rsbi_dQKzcfrKMpYdg8g5-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛شرط مالی علی علیپور برای ماندن در پرسپولیس مسخص شد.
🔴
طبق شنیده‌ها؛ ایجنت علی علیپور به مدیرعامل باشگاه پرسپولیس اعلام کرده که این بازیکن علاقمند به‌ماندن در این تیم است اما برای تمدید قرارداد خود به مدت دو فصل 250 میلیارد تومان میخواهد.…</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/23144" target="_blank">📅 23:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23143">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KY1cT6C4TyFsfj-d0FHWp1hxvNOU0X2jp5-Gm9fd6-dODNj3zSzX02XHDAK_CKXCb3dgiJm_VK75F2dDHwHL8SHLTpMjUcPEGiqd7EyOgVcG5fXiU-Qvxxub_IisMji4lJcO8GTYeSYAyuw2oVAPHOdcZ_zAr35dodG5WMktjC9NV9JrPqYIbYSfSyEzpeSV2KbY0NmdPaGUpDHap3UkeYnK2giE5nXVg4uVSayGqDV8dYgdPI4esLDd2IEeGAB9V6EqFaIyo_qWjRp8SL4LCeYSN2v1qWNL7u2E7-06ZmCH1RsRUALtITesfpTlG1Egbz2_5YPRCstS2GP7_AmwEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
💣
🔴
#اختصاصی_پرشیانا #فوری؛ رونمایی رسمی از لیست بازیکنان مدنظر اوسمار ویرا برای فصل‌آینده‌پرسپولیس؛ لازم به گفتن است برای هر پست نام دو بازیکن رو به مدیریت باشگاه داده تا اقدام لازگ برای جذب یکیشون انجام شود.
🔴
محمد امین حزباوی و دانیال ایری؛ دفاع وسط.
🔴
آریایوسفی…</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/23143" target="_blank">📅 23:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23142">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GInGKkenhZiV_NACMmmUJSLpbFQah-7hxLeA8ENiDhxV5qf3ZoIw_HXsk3GN4MBCUObISVZamxlNEZBexzYKtZ3jMFQ18d5ss5sH_T6HcfRMqpHt329e04jjh0eT6CUf7GISiZiFb5sjJ3fQ4f7WoK_jEjIrxoQ2gedr03VZ0dIK1xRFyYhXxZz7PdLpq07vnkOkmD0rXVuFfa2TkaKtVqWv-6R9YYol0_1Mab0b7-OI9SEozP5MJUNgj9rVtBiLbqvMDokRlP8sKuwnEtS_gw2VJDW1QKgudXsDesdqv3-dRY74rmnhSIZ2NQzgPgig4dFUv1I3cvDxalD_UdHi7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/23142" target="_blank">📅 23:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23141">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qy2yYeUWFrYFSLh4wQussG1jOmeqHR69evmfsgsNlwt0y1hVxR7LHFAdXLHqWKRsHMfjjin2IK3efeFdMuMvGY3k8uKI-3a02QdRNl15f3Gaer2Y7hqtvobBffy7JFE3bbkox1wo8ftoc64n5eD8yMOsf_7sFqBdX74Bk9YQtjO-cFcArnbmdRyDr5RWmZOUFZ6ndEFcSPXBlfFLB2kYpp45760WldebQXx5u5FoOZSvCMQ1ZmmhDkWC0XeznMhVSK8-0c6XbWh2QTBEP4S0IQmgmjAOd-rVATGDUBd0nQx6oyOYixbLfQEkkhc8wcU77U8GmFLqXj7eViHnTHr0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ متاسفانه اموال و حساب‌های بانکی و خط موبایل وریا غفوری توقیف و مصادره گردید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/23141" target="_blank">📅 22:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23140">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=dIgr-9L-T2m1TJjTXokXjetHb3WCgkmNlEPYRoqXke78eWMlTADWiFOZhmWpGY3TdREnnZ1k6ZLlDCsG-ZysKRsp-WPEQW6wZXEFIy5QALhtYW7BvImDZ4bwSrna0oQuAS8uJu525NHBmdA5Dk0JmjN-9eTtgvVhK5upsLfla6gy-tuaig7zRESx6lwVqZ1psrhLuRT3qT20txiNTOpj42BW6weOe_h5W0abr8jOx3UgoGQd5Y_1JC8AddpSd19fDg9l9F9U3JCUpb1pFCpMx926-sEq0EENbTlSM9SHoneG7ePDGQTiRXg6ZwX9AX3kqSEEB2SucF-S1iSqVVvcZxSzGqSBfEDU8Q3akQZWF1a42SlBzytLwOXoF4VRPCthSvgkFLBgPtytWR3a3luvUvkxS_D-uOwYDuO6CpaJPIY1J6w-aezAt9ayGHBvR1hUhkPS2FshRGRje5iQxlGQZrid0J0CIooum1e_I2VjDMYGe8mjvq7uPWGJdSO1THOsHDDB2J6XNg819UQnz05q82IOq7tTjUxKNjVbyJ7zcUBm0QYowAPyAXhw2U2C1Kkk996UB0Ud-w6eFOipYOYBsknC2qSoXymnlmobIM7D66i9XBZhmwi5UlMYkfdgZTKjgxuci9JYwoz2zeA3t8g3meWU0FpGbmzNyarGSmf_O4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64161e2ff3.mp4?token=dIgr-9L-T2m1TJjTXokXjetHb3WCgkmNlEPYRoqXke78eWMlTADWiFOZhmWpGY3TdREnnZ1k6ZLlDCsG-ZysKRsp-WPEQW6wZXEFIy5QALhtYW7BvImDZ4bwSrna0oQuAS8uJu525NHBmdA5Dk0JmjN-9eTtgvVhK5upsLfla6gy-tuaig7zRESx6lwVqZ1psrhLuRT3qT20txiNTOpj42BW6weOe_h5W0abr8jOx3UgoGQd5Y_1JC8AddpSd19fDg9l9F9U3JCUpb1pFCpMx926-sEq0EENbTlSM9SHoneG7ePDGQTiRXg6ZwX9AX3kqSEEB2SucF-S1iSqVVvcZxSzGqSBfEDU8Q3akQZWF1a42SlBzytLwOXoF4VRPCthSvgkFLBgPtytWR3a3luvUvkxS_D-uOwYDuO6CpaJPIY1J6w-aezAt9ayGHBvR1hUhkPS2FshRGRje5iQxlGQZrid0J0CIooum1e_I2VjDMYGe8mjvq7uPWGJdSO1THOsHDDB2J6XNg819UQnz05q82IOq7tTjUxKNjVbyJ7zcUBm0QYowAPyAXhw2U2C1Kkk996UB0Ud-w6eFOipYOYBsknC2qSoXymnlmobIM7D66i9XBZhmwi5UlMYkfdgZTKjgxuci9JYwoz2zeA3t8g3meWU0FpGbmzNyarGSmf_O4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رامین رضاییان مدافع راست تیم‌دعوتی امیر قلعه نویی: جرمی‌دوکو؟ من اصلا نمیشناسمش. کی هس؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/23140" target="_blank">📅 22:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23139">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eba85793af.mp4?token=Nb7_Ac5DxUhf9EiCYZmPqOO96f2ap3rC4YtfOAlff5aLDYBQbCouhII5TlzbrSm1ku5EbvlZXRAdax0IrfN49wQXaRD-o8dPIJch7M512q0TqOkB1UELd2Wai7sZYicWsd2z40hD1iGpOkoFntQJUfNQ4nhWaEdW8CGTdk2gsznlsY4eeP3FyFe-OQAAdwgSBLodSrm2sEDs7KjHSY7XlOWJtzLkleIn-0IYDQE6PzM3VIIyQhCaevmCesWWgYW4hiAnEf03NuCS-mnDyWEQ7oT4NWTxQzK7wJEGH64Kd3P5NZylGc3OsSIeoPRV87Cg4sKqGJcCJhkIFZItCpj3RH7VI6wcgb3MnEwxoPAKTEed-HMz0p0yWXBPG73Fpuul9L3dZYjei9rbFvri_m_BH0dTZCKIA9HQqeYDqcEHwLKpCilPzVkBtkmG-ughANZ-DdZpvwrOSNQTAvWZJGHT100IjVBqt9DnCev5Ji_HkUJd9a-Ke2XLk6i-hla_khA1IkC7QGkgvGoGSomjYH0fqSGmkYV5tG53MeUQPcEkE82K96IZ94LzNQok5qe2KTk-idDx7L2rgdusYR1AWnA9tgMagln0f0I0C0o_LigTCvYRXnBxtlB0-oVv2cPHegElQhXcUOUgqal4yDXDb0op6m3TAnqOM-pEbbKC-rHO-II" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
در آستانه شروع رقابت‌های جام جهانی 2026؛ جواد خیابانی رسما از صداوسیما خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23139" target="_blank">📅 22:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23138">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6TnQM1QusLFHt8f7ZC8kidELtG54WUxA6T1f919EKKvRY9SE85gk3bm5UtrdAFKy0OTDcHv4YqUEaYXhgvshYZjfZoDGqOcCMnT3KH4OI7dgrxuMr3Jl4Ftv3y_yFVOky_wpteKSo3izxBJhyf_Vtd1IwMOThioBKbjI2pi68J7TQV_5X6-LBddBfPtyy8xVJHWhvtsTWJOLmI0MPYygWmDv2pNTYyL_hEGh75kKfZzdtyA4GoxM1ZlSF9YbillgGwQzxkLTEwLYntrtQ0972j9ye1EsxjanMSwihfyuhZ_g6ArgJC_5AHMsE_sLS4AAAMkw5oIsy55KFh_k9YbyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ دیگر مجری ویژه مسابقات جام جهانی شبکه TRT SPOR؛ از هرجانگاه‌میکنید بکنید فقط از صداوسیما باحضوراون‌دومجری عنتر نبینید. از شبکه های خارجی‌ببینید از هر نظر واقعا فوق العاده هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23138" target="_blank">📅 22:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23137">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ho8H080P0JIl7NIFTOtHW4rVtMunaq3Bt11CTYZL2zKRqbZ_ypalFNvCCYI2VuRcxphhYjKTAk_ZjJfiMrpxpTWGkPm08g4rTTkatQuYYkQZ1InkoKnl327dJaO473BiKlzShduQKZWOuHDv-YpdS7P88ny2i-dqAgnwdSqluWGb43CR7tXAa8PiOhGTyzXS0JwpWy7NkSv9WC0o6hckhJ_QWdR_VsVC0-EkbPheC7qpq81RxTu49Ln1HG4odFavs-CpFmGbCL_HElL-PMOQg904hlNLMivW07BdwJhnqT-gvT9UYQybdrEZ2umKwwtsy0bFPt92xFII305lxnbetA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
برنامه کامل مسابقات هفته اول و دوم رقابت های جام جهانی 2026؛ بازی‌ها از 21 خرداد ماه در آمریکا رسما استارت خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23137" target="_blank">📅 21:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23136">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wmij3XhZs47TrPLIZco2LYSHr1xR4u5FSW-rS9Ng1iwuzmOwMAUPngkyesAcj8w4YtFqNw8DMs1LIgWTGPYVJ4cG3PxNpHfrVyVC2HhFig38TF3PfDuDkCBe_KA333yr1hyOyiZc1xwgU4duPk23-pIBsWhMMIlpeZdGjtZwU3BAXQHJqDfigMqVBra2PMNupzpHsgJ2jmWlQbaT0BVDWFzm0FBf0PRndvNiueFxWTMoyiXBBQpUzZa9WYxKSHkgDeE9jkKFPOBVhS6_sHsFszin5Bv0aFAUeSLxhprqYAedDpPLtPKPono8-W7J9SmnsL7f2Z6ydRsP7NWXhXy1xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این‌اشتباه درطراحی نیست؛
پرچم لهستان روی پیراهن هائیتی؛درسال ۱۸۰۲ ناپلئون سربازان لهستانی رابرای سرکوب انقلاب هائیتی فرستاد، اما بسیاری از آن‌ها به جای جنگیدن، به انقلابیون هائیتی پیوستند و در راه‌ استقلال این کشور جنگیدند. پس‌از استقلال هائیتی در ۱۸۰۴ ژان ژاک‌دسالین به لهستانی‌ها تابعیت اعطا کرد. اکنون و بیش‌از ۲۰۰ سال بعد هائیتی با قرار دادن پرچم‌لهستان‌روی‌پیراهنش در جام جهانی ۲۰۲۶، یاد این دوستی تاریخی را زنده نگه می‌دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23136" target="_blank">📅 21:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23135">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2aARVeflnpt7xD7_eqyeIIhqGuzlHZyDRLn2IoLLZPNrsuo5hXiils-qc80246qW-GhWpkv_Xjnc5LqfoojqzvFWZIi9MrQR_vziBOR8adaQflEtkLpq78gJXxCzdyoYgRk-2hZITDEi-NGJCbCmAHzRvwLIDPd4Q7LdJYHbp-z37r6FuXWrlrgXE4fwv3WW6lddqHJFpYSGmBUPvcpqU1JwWEiuQvfcFGdUqBe0DZe77l3QLUCD_5B_r5sXGkF5PKhjif3P7GirmYg0S5mITr6wSX-Ny99hVSAM4_Ewah9GV81IgNhVYDj2KJde-n7A6AFCYb8DO9jf2U6i6-ztQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
از امشب‌اخبار داغ نقل‌وانتقالات باشگاه‌های لیگ برتر مخصوصا چهار باشگاه بزرگ ایران رو هر شب با جزئیات کامل و دقیق برسی خواهیم کرد.
👍
بارسانه‌مردمی‌پرشیاناهمراه‌باشید.قراره بترکونیم. اخبار جام‌جهانی رو هم زودتر از هر رسانه ای دیگر در سریع ترین زمان ممکنه اطلاع…</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23135" target="_blank">📅 20:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23134">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpISbseG6uwieGEmI0IAeRpdvCYL3mklmookJjqxw5jUtVZeQ0P0DMsh1gQyj-8-IDxzI3PHfVDvnimEfkORdxD2WBmovTYqBqPA6PDsTBsFhBNPZwhZtu49FlJkgyqv5SXemgPK1qxaHAWaThNwidsuJhCIkuLrCAkKcDYgmPEE7fB3BLRWTohkJM8D-lWxpyQIRoKk1y4naN94SSq5Qwqt4R8YfBbUBo6D1BDNqnyLXRZFjIdIfTySBNcZNqJLPVn3qL7zZb-8X2lqpeIm4O75FXYBPdHfldFiMdey7dZkz-1iKLPEfg-xF3pudQj3bbnJWhz1aZ1v7z_3QqFPvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23134" target="_blank">📅 20:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23133">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rE8V1hLB6-GC3piF2Rq9i9L2nCsZcTyMpMQJa3HYCpea5aMlNdz-8-03xiTtO_JyY4pjNEym5T7-k2gFywZBlXryqnNNO5VNNLDNRJqIy0uQMdMhSoJy-EklcjUa28AKnNWe-dZ2bZh-iRzcJf6Z_ZxdRCNN31uWVyoa7a0aFpZf9n73O_lCzeYkwHq-hf6JIzEEiu7-M4F586DWpEcF4gnUS5vHbZ16rrlWInTALdHHyFnzbnFBkt-ISjHNYEdv8UglfB4sQQGVbU5-QQcJvYS8fpE24FZIfnssBOhFj6XUz4iWjUWV5AUFob82hpxYFMyd4qixolIw9YLUC1V9XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
باشگاه‌استقلال بزودی خبر تمدید قرارداد علیرضا کوشکی بمدت سه فصل دیگر رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/persiana_Soccer/23133" target="_blank">📅 20:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23131">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZqUI1Do89dJ_uJkfvBsPRWLY2qJArgivgt4SHSTai4S3b0-l64GtNVL9OG62usGe2YH7tcU7y9ghhD_i2GW9kpxO7zVdCgkAfxPAFIEvqf5ExgE1preRLNYIF4XTlNLLT107-jy6kUKF4JQhfIgjj_zuUmklqRGDEMirnKIwJB0Pcn1D2-CjG941S19cjsybAmT4Obqo49oddObIHL1Z-nuCZntZLKXE-gw86toL6zRugx1-SlalRlAHcOwaZClBN5Tae1QkpeL0h4nXYAt8hMD2Gdibq62j6E90aPjSocfxQRLb-HC74U7bobtwhzPzj2qhRLkirLvUZ_JuomSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/g-WrfYpMTcCOG9mIR-FfaXLWUkMP8dIfvl8IufvfIE8fQV81tExVosKcZCqUf2nRC0wVOs8-H_jNQS-GbNHpx1WXuj8j7PT8-hb7OXw5xXle8Kktph3ZnDY-FznKR6b4hMoffmQp8ijrfSqvISms2amezfe90cZM8jvL9BVqNSUX0KODLC1hywlflJB65aoS29B6W4l75_U0ztYaceTg0_FSoWFTx5u0ywZ5OoPflij_ruDjRCOGfU467FunbVLJmINPYtWAmpJIY54UlMAYs_VHQblKHP7tl7dKHddGYqi-OCASxW0PdrG3kHHckpBBd9Qd9fqLK_F-T2QM-IZrcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
خبرخوش: تولد و بقای پنج توله یوزپلنگ در پناهگاه میاندشت‌. ‏«هلیا»، یوزپلنگ ماده‌ای است که در آخرین زایمان خود در پناهگاه حیات‌وحش میاندشت خراسان شمالی، پنج توله به دنیا آورد. طی یک سال گذشته، این مادر و توله‌هایش بارها توسط محیط‌بانان مشاهده شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/23131" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23130">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e58078f0d1.mp4?token=U7IsHC_u1AsPEAHkQbhcITBl3qVDuYsP9RCPFSyMEoNPSPrWslA2hNPvGTbLvXEHMcha4nb-qGkD54CC05rDWkXa16Uhmawh1xxHEHdQV30i6mdxtapYSXaW7lIzai16kHMEo8ud9qfVqcFk8BHyz9o_uHDIHmrlS-G1u1rojaayBgjMVDZZIlz9CapUlkzUNAtf5jtsWNUrp5lam1u30bmV8MGzMK5i-AQJSPe6zYTFWgDWzSDVgzmOwzbWA2F1fzY-2a7q_RQeJIvn4DDTgTvv9L4_110fKz-l33ZzWnKYJ0JwWAYLsfRerWtv58oaz-itE4Q-2CB5woo9yRrUGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇦🇷
حس و حالی که از آهنگ‌های تیم قلعه‌نویی و بازیکنان منتبخش و تیم ملی آرژانتین میگیرم:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23130" target="_blank">📅 20:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23128">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZ-ggHNAAC4zyuMPWAuDmJCJQFvj4FoT1Jdk7HDX70HBzqiLQbHmcF_-d95hR2hatOAu-KNbmCcBvui5IKHr3eR98afp1HerdQsP01xOjPSCib7hEJ850ky97KUifrxSEnhrDIyzDibIEeKpJSohZbxEPmTynLeBy5a9CY7UVRLEGnHGiACdB2BxhrDl5xdTqwbyljwWohMLSami26ZgqUREf_jN6Ql3Kr3dZryzyrZ-7BLbL67adhb2g2DslTK7NdBqg4yOxdoSTfpWn3VyrbHnBROc2ncfLE8K7kDDp0CJJHgIl4xVjieYfOyperQ8fEiWNGpm_xI6k0-GRpTTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
مارکو باکیچ هافبک سرخپوشان و نماینده‌اش این هفته‌حضوری بامدیریت‌باشگاه پرسپولیس جلسه خواهند داشت تا تکلیف نهایی ستاره مونته نگرویی برای‌فصل‌اینده رقابت های لیگ برتر مشخص شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23128" target="_blank">📅 19:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23127">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVbcQ0nGdBSbbuYJOSoVDr9TylwJy9Mw_w_3AwA_fXsgUnKvRsZZWKS4Lot7In4QmJwNYfMVMS_KNSNipPdYtWbXh-iMzrlcg6YUoWkEwYYcM-jSxA0unppqSF-ghIlXo7wpCZ-V9ysDGenrGv9zJexo1I7LErilgTwVNvtxdzPrHzhmxpJQma4gNhqHDxY6dONaT1JhLnLSM75bkchEN3lEDeLuq_yL_BhoIPTWheSMR3WtHSfgSTWpJAeIX9BWyOv8iLBfNSS4A9t_zbuZ0fOOEtqm2V9YImgvlc119ZjOKQs3QD_Utp69PrTOaiX_lOWIKc1HS-8Ry44mUhBLTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇺🇾
#تکمیلی؛ خبرنگار موندو: داروین نونیز از طریق مدیرام الهلال آمادگی‌خود را برای پیوستن به بارسلونا اعلام کرده‌است. باشگاه الهلال اخیرا ستاره اروگوئه‌ای خود را به آبی‌اناری‌ها پیشنهاد داده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23127" target="_blank">📅 18:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23126">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B-tc1fid7QZA7WNLJ0R3_MBBbaezM0ztCbAb10Nau7z5MVEFIKMftHOQHFkWGn6M89mMxvNspecMdBK6q_VFH4PYQoSY_UvKYwDyummRpcvlzAqYYVgT5W7vJ2-x_M8B4I0teWl4gvVMhxZZ7rHEuQzLMxJ3OL_2b3SPyO30yaiT8Z3_l3vEUS3Kiq9Ax21S6uUcRZ4xj7Pjl8j9s_4SopgRIU1_AaI8m8Mwsrb6lC7WLQqtIAFsklSUIB-tgg-dufWFICAZsu6MvJj6jbjpZhaSTved0NWVpH_c-BFPWGNxUpnxc5vt5pJs1Ap_jfwnSxX8VZHShTHv21qhhylAhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#تکمیلی؛ رئیس‌اتلتیکومادرید: هر باشگاهی خولیان آلوارز رو میخواهد باید 150 میلیون یورو به حساب باشگاه ما واریز کند. نماینده آلوارز به ما گفته که اولویت او پیوستن به باشگاه بارسلوناست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23126" target="_blank">📅 17:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23124">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOkixufHAi4gRsE9yokVrcxsDU_IM1V_gteRx8EZJxAL0S24z1u-DtW0WGxM8eJb9d4SzYk9q3aRQYJLoAIhyPCacpfSm2g1ryvZZWCS9uVK753LUHDuXCPvnh0CZlqJaPop3_nS0oo-Sz2quAD0I6JfhBQSYjQ2gfKK7zcIG7LAd4_dI28-mb_DskJ9hEEnLEzHBdXBe8P4Y7MouKuBrrBDhrP5RZwZ_fgwhDohAXVYRnfX3QH8MxTXNRwCelfYQbsrOVgvrOy4rik3FLOxPWyiB_hFFFWBxXbrDIlTmO4k-Hh9JUgBCWZ9_YvsBKkxzILHxk-JISNI1UX3tPGn8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aeqkWxonFAn5eypWDczGj3rcuElDpiV-3N56UIVKEppgWUGfHzlKDn-D1Ahqh7XdzPyJoUG_c_5j_-wpX5LVDDOoib7gxbjJ_BOk2gUGBkJiPVH3yVBYdFyipGfinVs7ZYif1OTkll5oCpQPWO8gXCchE5YLvVI10VmFn4gME6JXJjMiNPrBcWUCBK6V5MjvKneZGvNQANjHJsAueriYkqmrT5ym1_IZDlD29uUfpIVz4ktn_xDXRmMQn9vlCzBicyfgZMXmPTD-7aWRLWcTggXNTQEoB-hEzUM1suRRmfZ2jijQNK-LTqPzhYOSL5grdf20UGbH0pDzawHKQUIyIw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23124" target="_blank">📅 16:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23123">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPvx_nKbp2P9Q9MGsJPV8hvjkvJ4Be-uiwSyApgpT4kI_EOlwKgwBPHgaAAQmkVqLYaoNGo6B_WNhV1VpWrtHdMhCSG51bIi0zHvXg2yDdCyHBNVGTMLDCMqMzvkMhWuP_hVSMo2RolvNCbEMN9qzNFm1FzTt9MO5DPcf1p1mV2a2xKaeYsG16xkCotvE9eooPH47NdPqRkTofOUb4tbYUK-YGtYHDHJ6ISL-7vbTY_xUCLhIHWHbcD14s1H0azs2qi4YvDWFKFByRjjXRL6XRLqiBIcc7VBYFG2qtnsSPeaqGG0xo5TgOwDknHprv3FtFdplkNtJi-aSU5MULA-DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درخصوص نحو سرچ فرکانس شبکه‌های رایگان ماهواره یاهست‌سوال‌زیاد پرسیدین. روپست ریپلای شده کامل ویدیونحو سرچ فرکانس شبکه مدنظر رو توضیح‌دادیم. الان‌این ماهواره‌خودمه شبکه‌ها سرچ‌ کردم مرتب پشت سر هم قرار دادم که هرکدوم رو خواستم سریع پیدا بشه. تموم این شبکه‌ها…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23123" target="_blank">📅 16:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23122">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
میراث‌ترسناک‌ضدحمله‌های منچستر که بعد از یه توپ‌گیری آغاز میشه بامربیگری کریک پس از سال‌ها که توسط سر الکس فرگوسن اجرا میشد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23122" target="_blank">📅 16:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23120">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Us4qwRZF3ibESQFJNqRZ7DwC2PbHIqr45zivE1PwnuJLoR9YhfuZ-EtFqt0g1AfS_ijRR6w7OSUnNdfXZUx7qqmc_l1L3JoEz_Y2RNXuujzPAu25VOBAcne0c7Tf2wFsuhuWrIWs7E6lPFdX_LyWPkhiEULavrjlvvck-xrpWK8AF29LcpNSjI88caZmnG1WifXtKqBLeCvlftChC7kspFnkdu2kEv2rjNGSLGAyRuiN8fq8rYY9SE34xKRq-xeINC2MnlyRUiIe6fDwzwlX9WX9A91qPMJ7O90WrhmUgsTkJuG2mAUdB_LqhYCQ_6oIW2pJS_z5lb9BL2_d4ePDvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oOxnRoe5_Gg2phmId9uzYy2TXktLOzp5Szyf9GO0LsxagUh5PXFscdIFNOeeg1y-ohPeQmyvZM3moDNR-0BLvvko19prrKoICLjCMFqXB9NOna2CKJpmt1aDYL45rCLTdX975rRZCvftgfY_wTwC5d9NZO6mYsm1uTqvACDkmmhbJyD8GfI_XhRx446QEjyOucdrLMGrpJyPXS2LeCjiExQvZY7oUT25YkF0AVkZfAVlmLwfLCL05UwX-pf8U5mGGySp842o1BK50YY5lC8IvT-Q2KsNGqzfZz_T0sKnq1Mh16v5Nn0wGtaRXxhY9NhsNStEeZIln4cGvJ2VprYNYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
مجریان ویژه برنامه مسابقات جام جهانی 2026 از شبکه معروف TRT SPOR؛ فرکانس شبکه رومیتونید ازماهواره ترکست پیدا کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/23120" target="_blank">📅 15:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23119">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9jiITwLGF7tJCNKwi7FCx_VZwRGBKpvVGNa32pAWGg_yJC0Z_OicxBXqHAHhlsLT89FZR1AhcVwZicGjfADhHIK47yZ6u_K-_T3HHRY7UEWZvEfVpeNnqZnyvHh7I8AtNeTWosYp5Tr_jGHAFbS4N0UlsMW3uvfFF6blVnq4qANvmXrWWtyho1-NZxd5kKZ5nB2Kiz81MjklsOPgzlf-XxlANHddWI9gK3knpacFs4QJ8V0kPCl6FPcrNDIlMqCgX97BjMlpNvYLz6u-YNp8kRiJT0UlIBhlksIFzspRhQF90B8XjFC5c7DXGRWMCs-zrIhah1BU-7OZnB-YUQ7mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23119" target="_blank">📅 15:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23118">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J-D08YZ12bo1MWnZa_SGzj1ly0rGMgBBArxl9WzNIHCPerG-D0yuKLLTtPDHRSsDwVfgzafdE8DM5JKM-1kHcFHhU4clis16RoG_5NTogWC8obw5drne05psEOp_2p1DvIMmkuTDVfs4KvUL0U5QGcsXlqm_CiKR028NLryPBnKa2_ald-w0_IE8xG_iCE2DTmT3Syid9OMWwMO_INhd1GE70zf2fwoA996ruJHhhSl8CZkDYm0xUewGSf-BOEzH4tmbBo45qiL7H7Sy99pSjCiA1dTAfxcBKeCbreYiV9Ghs33zv9UK8Uc7DZfHykawl9HuQ_M0RrXkHp84VG36og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
شهربرلین‌آلمان تازگی‌ها یه مکان برای شنا زده که خانوم‌ها در اون مکان حق پوشیدن سوتین ندارند! همونطوری که مردا سینه هاشون پیداست خانوما هم مجبورند بدون سوتین وارد اونجا بشن و شنا کنند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/23118" target="_blank">📅 15:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23117">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5UBAXxiz85B88tzlXNSH29ZFndYKb7w_nQckLt99Aj61vcLIoW6PEs3CYj8mMCSekZD6tWxxYbwuCvPr4NJ0ZnFgaRVNm30R0iVcAPgoKbBNOBJI3ZWGfrVoq4b1LtW9BVWBO0E_qz6LrX8by7rvUCLwJvh26tuZ4q1SRT_nXgNaLFyeVX6gaRu6mHaNW9OicvbGelaKyoBoYvvxsq1ZOZ1gqextzu1K1kCwledbqo8HdV46KrQrevCsZJjKHs9SFdOlw3nWOsG1UFJO7Qyo2HPELoqd1ICJmhHpZ6z2Qqd2i3ueP_0bM879zs0w9WHSufOUc98Dt7_AZqME-QmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23117" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23116">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t3j90AJIbOyjjxaTAJgoWL5E2roV6bWAg_hLYlxGXQo9FhJtt6byRJBlErRCa0xOstGMMwx52kZ4HIolue0dnxGD2nrUCbpFXTt99w7d5xajBAeDc-G4gBKeSHfoDDBOh7LlPV1GY2YrbSt2vSNW2drDhRbB5b_zh0luuASa4_g514Y1FMN4RRaKjihlyfHsi0irx585FYB_82rWwSPby0_dnBhRUsGMwx7TpUgbb7Fv-fOcJ9A4rYmxV1-hln06JCCL_N9fSfbXtiPAVQIMfnYrcnhKzwccbNgta_GQdtjMOiO27kk_z276eWVvp31NWARm7943k44cP6Zkev2lvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ دیمارتزیو: ژوزه مورینیو سرمربی رئال مادرید از پرز خواسته از بین یوشکو گواردیول، ریکاردو کالافیوری و نیکو اشلوتربک‌آلمانی دومدافع رو برای فصل بعد به خدمت بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23116" target="_blank">📅 14:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23115">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpnG-NOBxxR1TSuqDtrKLedZuW1DdPlP22DIFEYdWuxn77_k0xqaatBPYGxysuDFWc6JPxHVH5QxwCrI02v0gEBnLSQv0hrcceijMcIEmcnNARZSyOTVgDGOxKRrkSaLuDI_e3LcdUaEIw2G-9GaEwfysnkjAK4yKJrFzGEW5QOG203UkplqLimDpEmQtAu-tM4c5EqgI8EE0vuFkP-aJCzK9NrG9h1QVp2pD0T04i8c00hS1B8hD1_8ow3jxz4vbz3BGuKXlUXHWr34olTQkCF0qFvfj0Mw_cQccFX_oZiBXgW47xZd7rD4W5jaMu1lTKnuVZYa_nyMohrKFrZpMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23115" target="_blank">📅 14:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23114">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sp_v0N0KjYhHF2S1uBVNBsirp4U6DLOzo2giW1DaITk5LR1ccS7eweLCx-qh65hopLtgecIbWkB0uLwpbcwvDxix4kMdr6ewJ5bl23NSutT-1zcmMVb_XHen86D2YlId_-W9gUqmWtjH24OYMCwkx-TJhp6DDlF1Dl_yvZ1yhULFjq6o6bY87g8TlYhvdghyD3rg6bwzGtEHqOPYm42eKqJ66m9l4Dx-oApclbve5K2iacoIWjzLfbo0Cvh8prZPnwmnwYiG3is249pb_OFHor8SbZuYMMBe9lF3jBwrEUi2bykKpWpcpxa0Oq5oh0zqria3pyaLEUoMb3BhoqCfnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ ایجنت محمد جواد حسین نژاد به باشگاه‌استقلال اعلام‌کرده‌مبلغ 1.5 الی 2 میلیون دلار برای رضایت‌نامه حسین‌نژاد کنار بگذارند. خودِ حسین نژاد موافقت خود را با عقد قرار داد سه ساله با آبی پوشان پایتخت در این تابستان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/23114" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23113">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=si0XypqOJdbO1LKbwlDEpBU2sY0Hcp4qpGDV5LhT8HttRXI5o24KGsR40kHhAzjpCi2SzcnDOKkapudRY_tYnnoZ6iU-CB2WVp0uysTJ9g1-G9CaBwqGOr6Pe_FsCYdBp9bHP3JTHoIbx4ybK7KF_dP-UKbpXHWbol-pfizu6hBu2n-a2t-u2mfhU1L0WBNnH2UzCRERMCFcebJP93p2afa2D8KKEOKU8g_hbFSWf5-nmYqHWcR6hr8LDacX6-ADTILX1rS3m64o6sXNsYTvfUSMvdKHSjRwTCSINUZMb2Ne-vDWiftLjGfOgEbIg5P52GZIxcvekuLZt1HKKvCliYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b4b886447.mp4?token=si0XypqOJdbO1LKbwlDEpBU2sY0Hcp4qpGDV5LhT8HttRXI5o24KGsR40kHhAzjpCi2SzcnDOKkapudRY_tYnnoZ6iU-CB2WVp0uysTJ9g1-G9CaBwqGOr6Pe_FsCYdBp9bHP3JTHoIbx4ybK7KF_dP-UKbpXHWbol-pfizu6hBu2n-a2t-u2mfhU1L0WBNnH2UzCRERMCFcebJP93p2afa2D8KKEOKU8g_hbFSWf5-nmYqHWcR6hr8LDacX6-ADTILX1rS3m64o6sXNsYTvfUSMvdKHSjRwTCSINUZMb2Ne-vDWiftLjGfOgEbIg5P52GZIxcvekuLZt1HKKvCliYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اسپید یوتیوبر معروف رفته‌سرتمرین تیم برزیل؛ بهش میگن شوت بزن اگ گلش نکردی باید شنا بری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/23113" target="_blank">📅 13:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23112">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiEQUfJsfB8hzq9zkncrg2upw5c-Nw97Fz0_tGdq2D7sYPrPDcEa6tQ1LxsEwR5AhfqakCYAk1B509M-g6e7X3ANxHEoJYN_32BwHAbMTWtUX9-EYlR1Fxx9kK9f9pEBYMwCrLldgJr5qFaSKrHSFhPRBGKziEEiyIlCGoVNqOiZbP6HLNWl_qF_VuAKxw0Vz2WKb0JvQ7rfsbDw8-SUw9kTXEfszOFYY73c3tqe4B1pvz1eSapBNoOzZX8FZ50uVSV9SH3XckHQS1tBnHGRb3fJzITqRWerixGi-m_igiMBdi6nBmXp4bBE3SPsR49rq_w1hoZ_po6lqfUI1WDtvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23112" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23111">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6pznA-Cpze4EmuW034etqvqsXAQtRrj_jcOJxmLPQj6GC_P9uhUpV1hTCSheqmm5RBCKoEyIpWSZXWFiq922BBpTQ0-MBYw-7ehqJYd_-NfurZ825c3L5kJAFd8EfYgq9vcu5MR0GCSFRP7Zi3ojaxnv8MLs_bRNjeUMaq7CUapykbw418VWqP74wOpIovYhdVQ2OzTjqWshyCK2pl7yKah82iaOPxi0QX49AhKdDqvaoUNL_idh5W54xgyWA0BvcYE0c1L-rrVGHuyS1cQTzKmb9Wd5fa2p058OgC870F5gcUZd9f1rbY5rarVGkWR2rvLXWioV6aK3_IBjvNmyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|بارسا آمادس که ۱۳ میلیون یورو بابت فعال کردن بند فسخ قرار داد رشفورد به منچستریونایتد پرداخت‌کنه اما شیاطین سرخ مبلغ ۲۲ میلیون یورو برای فروش رشفورد میخواهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/23111" target="_blank">📅 13:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23110">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=jgyc9d8t-gDFe4XJcY3qbnGJ1m3W4Cyhkb4kU1riMMS6-M_Kc3-bfzN0LZ-UXO0b10jOnD25zZ0XHXYro5NlAtr2rBC7w57jLDq7H6CmoQ4LrpWZNj0enk1xlfDMPVzzjQTOdo9QzNVsEX2uiX4pp6bUBulxBv6TL2Ha08-_6KiRsreHyElgAIPdHkVZwtJ7kfFfhlpfeffqAqd3VY_95rUlYY4E3ngtHJqrwakrbdfzdFfypL_OkrNd3kyswGLypD3SVvPtvndkA8RGJEaVEqG_5qj3mz2kVp8CJ_gjR9iQTcN-2AVGaRx_q-YBycLyUol4viFOoWyXs4LIMBsSAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc9f0297d3.mp4?token=jgyc9d8t-gDFe4XJcY3qbnGJ1m3W4Cyhkb4kU1riMMS6-M_Kc3-bfzN0LZ-UXO0b10jOnD25zZ0XHXYro5NlAtr2rBC7w57jLDq7H6CmoQ4LrpWZNj0enk1xlfDMPVzzjQTOdo9QzNVsEX2uiX4pp6bUBulxBv6TL2Ha08-_6KiRsreHyElgAIPdHkVZwtJ7kfFfhlpfeffqAqd3VY_95rUlYY4E3ngtHJqrwakrbdfzdFfypL_OkrNd3kyswGLypD3SVvPtvndkA8RGJEaVEqG_5qj3mz2kVp8CJ_gjR9iQTcN-2AVGaRx_q-YBycLyUol4viFOoWyXs4LIMBsSAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌قلعه‌نویی‌وقتی میبینه باید مقابل دوکو،دیبروین،صلاح و مرموش کلین‌شیت کنه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/23110" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23109">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eenVUGkS7c8CgHa8rs4jn6STBsOg2hP-Ds0LG35vVga0YQt9lcVr_4xMumt4lLuVNaDbXVXjI8n5WC4T614CCm8fmhM4BDvcZnjIN4u62wAs-ba5Pg8TE40iAMmUCe9QO5C-o4conDm873TcEQ2JIWeiR3zd-NqTeKcwP5CybHejC4hqZxPXhG-wxjqF9d1pdAljXbG_nWd3-SNLk7B5dtY8Vl3emP5kuqHGZA3VK9Pf_F9YP63u7uACMmFnpvfxe5lFj31dE4ecU0L_zUSTAi1XQ2ObJMtRl9uZl-3T-Yb9FAi47BTqSBDUHIHHdswS2-Hx17mFcNK5xVPyRtoJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
دیمارتزیو: باشگاه رئال‌مادریدمذاکرات خود رابا باشگاه آرسنال برای‌جذب ریکاردو کالافیوری آغاز کرده. کالافیوری خودش برای عقد قرار دادی 5 ساله با کهکشانی ها با پرز به توافق نهایی رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/23109" target="_blank">📅 13:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23106">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bfi1WkYlf4RaPvoqQkK0ws06lEBe2QbiPgsnq1ZQz3RLJuyBVAWIJRUiP9NSoWJIICvjU_-L_MUDyvpkiEDSWPkUNViTAAYQ9cHfxEuajFRzP-9oLgpoJe_ajsqkSf5k2TzAqs65hUr8m4C_N_2mdpGzG4CRMX-d6xLJGQL9j-LSWf6YgK6bCGHSfN3w6nppnX5XGD0JLm-yAJGK8hFhGcAzldNWaDobWZH3r0aZ7ILJvtYkGUNvBvBKwFZ8IBr5qOzA6jyW3utYScpot7WquG6C4tDiys8VcsHFlV8lIaijpnt38Igr9rsj16UdDVAFc-xFUSSd38gJ3bSTjY2d9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرداشب و پس‌فرداشب‌ازلیست دقیق ورودی و خروجی‌هردوباشگاه‌پرسپولیس و استقلال رونمایی خواهیم کرد. اینکه‌این‌مدت کامل همه چی رو نگفتیم بخاطر این‌بودکه ویو کانال برگرده بروال طبق و همه رفقا آنلاین شن. فرداشب از لیست باشگاه پرسپولیس رونمایی میکنیم. پس‌فرداشب‌هم‌بازیکنانی‌که…</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/23106" target="_blank">📅 12:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23105">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/scpzpbvM1xjQaVRhTKa_GcDncvA6q8k4LCB_hA2geBihJsuFVi63Ng1Z7hkYa5zIUWHfHoxLbNIUpD9-vPtjffBFiSrNWNDwgagU4s4Qi0M68zR0ICfnvrzlYSlnYl0jUL0120mfc4hJ4FhQCE3k7xtIV8gRMnw5uPoAG3nuudaT_qRiz4Ud-2UmBbiciyqEvH02-hdGV-3eHk3AMN066iKbTEwcwalQyOMzesYEdHVYtDKOMzUql39FcStOiyhu7BXph9BmiPKobXpddlSdFp2jeKiq10shJdv5AexNcUd2J4lqJ2wmLCoYiibPwsAshP1wXJsKnwt_4Fsg4GjMEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23105" target="_blank">📅 12:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23103">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EUnfyRzCOMhcfUaAxx_Fr4szHa36m4jlLmKjMTPZWG_Vxusvdk_Y0FD3EyCnKZwERe_nC-mTVMD_BGwD6c9T1bJNlELfMFwxybbIvZBvCT0fL9UgCGK85_zOUE3uXzRJL7gMyF5-XVsZumfobMHL25-_gJUcd1psOIFeH5TEnwiDAhAECoeeBytw-iFTAKQ22rxecdlxZ8rE7jl6dfTkgcymwEqJLsRyl86a6mEa6bCuLqtUHPQJej2pY4aB0vyb9XEs7rRZ-Hm_cljvBs-2mLhI0yk-ZwYcxS-eE0Wxa0d5Gj1BHh1lkhGGsVik6q263HPKzoEK8bgCH-3uqJWp-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kx6Sw2ZNHi738P6hfcNtel9e237TGsBHf96hv9iGO0KR_pwpteYbfajjxbazeasqAxBLzBhSqe60xqZOxqfLDywyHocbFAOYtALlNRHtIRr_WgJHQNS6lF38gx8vq2cCoUvVNaSJiZhOVyOzNyAR6vcyqtxh8q7KxVuB_jdm8QIxR1AaDYoZpKUFULrRfM-prxxV_k1ryjhA_lmFxYlUuLb7UJHBwdGKyvPCU5ad-KaJ1aptqP9kZf4BCNEgrd04mEerjA8dRvz_AgSt1HPD2qBDljTtHts_QoxzBE_NJNjHdhIWDyHizyb9AkQtL_gKbi1-mdVWy-IYWIrutlM-aA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
کنفدراسیون فوتبال آسیا AFC نمایندگان ایران در رقابت‌ های آسیایی را اعلام کرد که استقلال و تراکتور در لیگ نخبگان آسیا و گل‌ گهر در لیگ قهرمانان آسیا 2 شرکت می‌کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23103" target="_blank">📅 11:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23102">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_ytSzCpeKx3j1HI1ozrBy-kk3qbI8UlG-o9GWWANFqHhQtCLy-So1a0_piE0xOkQooSbXj5ri2a45yqRw-SF7Pd-p_t2gmMbh59zFakvGyfh6cF3EtrJi7UKMKxTIwjf2vVXqzGR81FJnpcd80P8wOMfxURqYj2Ayw9uZi6lsj6V8Pae4kGSGDkLFcmf8PfclOtkf6izV8zY77QXm4sVX1zCSqUSFqiWKE4qNL4K1utml3GV0lcocfFPVbhAFPqTVvkGiL394xUf5ghCtGbmKVyRxijOFuwhcV4CmhxKVbpbvoRmL69vLvl5iskOHr5IdFuc2pLFHovRfu8KBMs1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آب پاک ناصر الخلیفی مالک تیم پاری سن ژرمن روی‌دست‌مشتریان‌ویتینیا و ژائو نوس: این‌دو ستاره رو به هیچ باشگاهی با هیچ رقمی نخواهم داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23102" target="_blank">📅 10:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23101">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Isnl2VcxuvWu1UGylA2-2oHI8wOU0OQtnx2Er3wW-6Oue6LriZSD3cIzz0Wkgvx8swVGN8eJ8mHGwel9E2bjnKfx0__KicgbNOWtP27oF0dE3GFuUe0MwV3Nl0jxzeNnW96ZwIgTLWqHX4KKEor4alI23X_Jt8EZTsGWgdZxaIFHC8dP2WyLtc8_bJNSLY8XHhjpNoD-W0TKZzap5uvBTa748_661YRCMLLoUwJruszNgcMDqMjyZD77LXcT7AQZhAEkmnYUDlQSHtxxfYG8DExSiYCBQgFEvFom_wrzTOjPl3bPVvz9ZunXy_d5ju1tD0DGmVE7LF4sbSuQ7723_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیل گرا مدافع‌تیم‌پرسپولیس با دریافت چهارمین کارت زرد خود، دیدار مقابل ذوب‌آهن را از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/23101" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23100">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=FyLqj-n1w9XhZWtF451cpzH3rmG-W-tKClBT-_mVTLBV8YMBHtluUVPmLHmsC28KMQyqg71S_dym879UWRF73WWTXdbFOADhaPFW-qasHql97Zh6rBrvE7CQUcKSZEiZ9A8rIVO8bIRqh68zw6N5f9pBKtDsfOq5tayTYLNDqEpZ-E6vWsANsZfF3uVKoDDqHWk1tBTASZjNwrxtKXeBkhi8_zbgnHHez90UoFlvv9oFWWvygwpjftF-A7RjLIesk64wFyjditvhR5Ez-DeAvuuZ1HwvDkWA4M9sOwiSiuotbpy-bqb0Gs2YX027CpuClTufK3zJojoaUiFf9vJhhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86dbb1bcb5.mp4?token=FyLqj-n1w9XhZWtF451cpzH3rmG-W-tKClBT-_mVTLBV8YMBHtluUVPmLHmsC28KMQyqg71S_dym879UWRF73WWTXdbFOADhaPFW-qasHql97Zh6rBrvE7CQUcKSZEiZ9A8rIVO8bIRqh68zw6N5f9pBKtDsfOq5tayTYLNDqEpZ-E6vWsANsZfF3uVKoDDqHWk1tBTASZjNwrxtKXeBkhi8_zbgnHHez90UoFlvv9oFWWvygwpjftF-A7RjLIesk64wFyjditvhR5Ez-DeAvuuZ1HwvDkWA4M9sOwiSiuotbpy-bqb0Gs2YX027CpuClTufK3zJojoaUiFf9vJhhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
درجام‌جهانی 2018، آلمان، مدافع عنوان قهرمانی داشت درآستانه حذف قرارمیگرفت و در حالی که 10 نفره بودن کروس دردقیقه 95 این شاهکارو خلق کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23100" target="_blank">📅 10:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23099">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇧🇷
👤
به‌مناسبت‌بازگشت نیمار به تیم ملی برزیل؛
ویدیویی ببینید از شاهکار‌های دیدنی او در سلسائو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23099" target="_blank">📅 09:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23098">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KENy6DWqzqPt7ylBM_9zg5K9HtoOOCsSBWRkdh6ZKFrMntakmX8zxtTvgT42Obx_6xz6qqGkMZshTzbBOG2-yV7YihnCJzJso9ej6kZY2ur1-3jT-VjxQwLx1lk84fv57t-88u4_M5TRJBBJYRs_XM2-IyFMLyUTixtPL0PVs-6yBtw_K-ylEozfh6DXkTkg72_uKpYrx_IsCALAOR_aRVg-Vk_6JAK9hYcnL3REOSevK2aZLr1vxyOCIl2a1knuRrNjbKFw48492egIJ3UCJE1UHcHfsgWCjebQ_4yo0mTcrEMnTcLFbwR7nbt8PHqAkr50SUWh2kR4ah17LYjuMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تمامی جوایز تیم‌ های ملی در رقابت‌‌ های جام جهانی 2026؛ قهرمان 50 میلیون دلار میگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/23098" target="_blank">📅 09:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23097">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTeihuZ1h37BpS0_Ljap-JsFb3D2d7LyX_hSuvQpcGHxPZZD7v0M6RIPaq6Y9xE3u1W7fKmXb8A67Hl_qqG87MR-z5OL2k3WR5qc4QW06Pz1PqhbgM3aYoAbmgv74S5-a38bBHBeAVqgr0xvL_8tihqMGuv33vGGVxI78pqrv0gfnVmgHSKgOfRGM2m2cutQAn_uIysXU4KDJ7PCGYfJgSp8NhMsGGoGT-qINcokBi_9l3WQQBP67QbclS77LTWh2xfW7DvUpTqg2TVKK9hcMfHJfIMiPjHEvsZ_xOsakVmwfzS4QK2dnJpptO-X68IqkJGkeLDPER1_an91Ro4p0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
فدراسیون‌فوتبال‌ازبکستان:
بعداز MRI مشخص شدمصدومیت ماشاریپوف ازناحیه کمره و این‌بازیکن رباط صلیبی پاره‌نکرده. براساس‌نتایج MRI، مشخص گردید که فتق دیسک بین‌مهره‌ای او عودکرده. بزودی میزان دقیق دوری او از میادین مشخص میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23097" target="_blank">📅 09:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23096">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=cK4DFC8JbU5QNQP0hdsL4zioKqDsxzvk9ccBkd1KVd9TywrbiSyAf66vsv2FPwhuisGyTKKT4vu5OxTEBMLCzeUigRuvs1-pW0fd4G4Ea0arYXtdJJMY5jsx1NF-0oxqz42_M2WNzhY6FSA3fM5ClKr60XMo-60WUrddbL-QxDKxeDcJJIFCvGB7AyJDpiQf1uZODsF6mrefT7NPwT-HnRwRcchY8746mRmEW8p3z_gLBo74Tkd1rnfCQ8jv-VBqkMZT6MyP7EP5wUTy62wBtq4Xy86YwOWgOeFvr5wIBs5BQ9CfPa_bYiMGaeDYOsqeFNnA9rR5pGlz4lzyvfYRmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b8bf04818.mp4?token=cK4DFC8JbU5QNQP0hdsL4zioKqDsxzvk9ccBkd1KVd9TywrbiSyAf66vsv2FPwhuisGyTKKT4vu5OxTEBMLCzeUigRuvs1-pW0fd4G4Ea0arYXtdJJMY5jsx1NF-0oxqz42_M2WNzhY6FSA3fM5ClKr60XMo-60WUrddbL-QxDKxeDcJJIFCvGB7AyJDpiQf1uZODsF6mrefT7NPwT-HnRwRcchY8746mRmEW8p3z_gLBo74Tkd1rnfCQ8jv-VBqkMZT6MyP7EP5wUTy62wBtq4Xy86YwOWgOeFvr5wIBs5BQ9CfPa_bYiMGaeDYOsqeFNnA9rR5pGlz4lzyvfYRmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
درشب‌پیروزی 3بر0 آرژانتین برابر ایسلند در دیداری دوستانه؛ لیونل مسی کاپیتان آلبی سلسته به این شکل موفق به گلزنی در این مسابقه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23096" target="_blank">📅 09:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23095">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=MIwE_C8_X53H_NLsNcvzvQa8g2SNjIAzOOOZx2y2ArV5yI0aPvFe6idMInsP-RTJ0yCfJzeycmZiucJ3jxyVFlf4EOigLDFB4b0TPVNP5WU5BWRfao0xrp_nWEmUR6Xqn0w-sTKm2nzjzxIeG0nIBJWocdzrotTNG33wS-ngRIolYQv-CeqwJplbyOdBAyaf57MDFPMOvMwM78UxAP-88nn0mJqUmIjyU6SDwIVBLP5hQsbHEVls2n1KoIHlX4xbSzAWZ3DWY34krUm6H5c3sFZ05KKKHhqtaNf3qHs_qEkPHfTE0cjMPNV4paNblwlY9gBQ8RQjOedQmDqQPpLZXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fc2cb234.mp4?token=MIwE_C8_X53H_NLsNcvzvQa8g2SNjIAzOOOZx2y2ArV5yI0aPvFe6idMInsP-RTJ0yCfJzeycmZiucJ3jxyVFlf4EOigLDFB4b0TPVNP5WU5BWRfao0xrp_nWEmUR6Xqn0w-sTKm2nzjzxIeG0nIBJWocdzrotTNG33wS-ngRIolYQv-CeqwJplbyOdBAyaf57MDFPMOvMwM78UxAP-88nn0mJqUmIjyU6SDwIVBLP5hQsbHEVls2n1KoIHlX4xbSzAWZ3DWY34krUm6H5c3sFZ05KKKHhqtaNf3qHs_qEkPHfTE0cjMPNV4paNblwlY9gBQ8RQjOedQmDqQPpLZXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحنه‌ هایی دیگر از موزیک ویدئو شیدا مقصود لو همسر ایرانی خوزه مورایس برای جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/23095" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23092">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oO4CzUQgsE_kwGlMzqmPiDktUsk-hDb8e_CNTPwIzTbOJtggUOk1DLfIuKoZwb7Hqr0_AkMtATi5t0dXDPe5Ono8GoRcmHcrSNfXsFlUDb9xlXKKGAjSt43qizcXec5gLDdmeCdxJUzbrqIbrm2HJGtVYMarWVciWjTga7RgEi_TaVNQhOjJcGUISwdxZkNjcvO6k06av2ufZgjT1wqJia8gq7jOvAB91HC-cmXF6ktDSi2uwzF7rp4OaPYLp9gZJTdCKzhvwGEfZ7k59naWi430_IUriXZDKmQhaFk7GPjNq9Lf-PVkkNE23IHrTS1Nw4srnUW6aHfAW2YbCZWb9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ds2L6tUo55t15jqJUd27MkxfuD34OBpvROkHmRDm1o9HPVKflB6ed0hJebjSFMSxLxE8Tti0hexJlVYParyI5KcYdWiw2Dc6qijwB81dg7eGVo3bCGYm8_lLslldOY4OZks52sLnRcCL1x6trbzsjTSzCDtdEcKIUUZUxkO_st7bOQMG-W8I2Y53OC0LiOfsW5bKu0cawCFJaqTqCpU0I9AQqA_VmUPirZGhAG6xMg2ALW9apbD5JeCmUxUJEuO-pDrm733KQSzY_z5rlq-7dFPqS_wC3aYUHNhfzqmNtN7ns9KRxE-hS7hKBBQAyJKciILZGIpLAL7m3bNeJVRUQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نتیجه تک دیدار دوستانه مهم روز گذشته + برنامه مهم ترین دیدار های دوستانه امروز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23092" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23091">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7865bde240.mp4?token=fmxKjncbbjzsXlHsUAEg7CnZoVHCBHufoOsbMRIBNm4dCkoo57Hi4tLOg2pysueU-wul1_amS7AqoZLviXNKZTREzbOzRPxerzsC8vkzda0CAxtcLYdpm80BMvl_0snFm0RdxkmTbfkXyHpHeESSKfkgSQ-jrUVH2cSmvogkAxlPDqVhxiWvKeq9v20R6fQ-QrXq5R5vnL5FoIjZFnRWB3NneQd4PWPYQPal9rasLdomFMvLneF4hurwADHDFPJXqdwDNaVQkHQutMLA-BXNk406KEHAfOsT4O7zbaQLvi12RT4NcpMGAOi2f77IWYDzwAuDvsJz2P8drJMR8h8VQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7865bde240.mp4?token=fmxKjncbbjzsXlHsUAEg7CnZoVHCBHufoOsbMRIBNm4dCkoo57Hi4tLOg2pysueU-wul1_amS7AqoZLviXNKZTREzbOzRPxerzsC8vkzda0CAxtcLYdpm80BMvl_0snFm0RdxkmTbfkXyHpHeESSKfkgSQ-jrUVH2cSmvogkAxlPDqVhxiWvKeq9v20R6fQ-QrXq5R5vnL5FoIjZFnRWB3NneQd4PWPYQPal9rasLdomFMvLneF4hurwADHDFPJXqdwDNaVQkHQutMLA-BXNk406KEHAfOsT4O7zbaQLvi12RT4NcpMGAOi2f77IWYDzwAuDvsJz2P8drJMR8h8VQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/23091" target="_blank">📅 00:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23089">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zh2JAiEqM8_Dn0JRk-jFvC_xdwT_4eEZ2iFvFDyDL1r87J0d1Y_k7YZ6JQDxBYo35tunZhM7MNpk4Dy62-SrVhQ62R2nwPrtt71c5OEXwPKULeD_TXtUSZQs95RS2V8BNiPf7YBcU2fw-u72oxjKQ6NYVuVXA58ZOW_ofgHbnlhdG7Y8r_jQWAKR7aNVARmIeGwo8C4j338UZXJhOx6vquhlVw6hFJAWrHH_OqjaVtjH_e5JIYEvMzbewrJRkTIoEnQyDoQyIxlBW7_zLJcZj0537LFx8hHZNYfE0Okv52bSyo2QWWw-9QjTPK_S5ganHhHNSwlxVSjVCWdGHjnTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IWDsv_QRa2OW9sdclsLveGPe5BIl1TPY1uNtakhgvmhdh6SKAWwoZjpHqKJHGxLbwv-T0dBArHZhGqsg3SsnB-CfFI4WhIdKjllqfnYSZ-hpcAVBsC8Y0fxYaJqrCts2xFsVdwBSPdifFOk9H_xVktoRsLu0aVmc5FoIHxmCFUsRklYGxihoiVfVwQjFDIt84P8r8LTZmhHcplv8i9iekCcWBIPxWDT7KZkZpS7IhiYAQJct8pgd3PC3GkWlsVxXpjkpukGcEK3q3sXcdmKYdgMQl9pL-CGvK4cCsXG37l8u87mvP7pcENR1hGW9ZhBbZfF_SWl7pbYksN7LAPq2Mg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول‌باشگاه‌های‌برتر لیگ قهرمانان آسیا بر اساس آخرین امتیازات کسب شده در 10 سال اخیر + پر افتخار ترین‌ تیم‌های این رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/23089" target="_blank">📅 00:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23088">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcZ0WO1nSC9Twr6-Lzuf6NpON_rLg3b0Ikp9QIOEsHJ_VnFq2fMbGCtN3jSVSwixrTabclzqEJqyRlDz8ADxJOyBicFUr0o01bliN1X_Nk8B0EVy1e-gkyTQ2JbMzA_q1GV4yTS6G2PXBix2IJE9c_XwBnA1LewN_UVY1eOu5OsJuJnvaB4fb3u0M5Ur93SZb3t2vC0gYnYtsN9qiP-k6a9aF1fyu8YdPpH-XKgzKGCjy9Pd-tq9tsK_KLlG-TjYcBKG703-2ay6ZKH63q7JPK4aEDdjaYlMyGpkIL0cp7G06_4MV51jP-kVvDoGvKWE51IceSzhX-AbmmV31QPSsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23088" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23087">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5366993444.mp4?token=RcWbFU9nqnq-JwzWMBjoXWYV-9_1gPFNS_NYJMGGDEWibfSSi15D1XWwROm1RmxIfLC4524grC4d2_eSs3JUjmp87xDIKxEjhAHdi10JTd978sS00PtrUKfHqF7wWUxY6jWfg-9IpKuaEaTO0Bp-DGt3Sl5RuKiD4LkRcVxLdCsrPcIfSsjs2BurM-vfXR31V4BBTM9svzFeF1gnXSenQTjOwnRxntGThD5hZ3rWsb03zViRNqGrs70sc10-lYbby5edrFYEF5s5gU_KNx24ueqP5rGSHxtgKho1oe67i3m4S492smGcbir8kDkTaheIwy54VMiEr6BLIZvKrpaH1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5366993444.mp4?token=RcWbFU9nqnq-JwzWMBjoXWYV-9_1gPFNS_NYJMGGDEWibfSSi15D1XWwROm1RmxIfLC4524grC4d2_eSs3JUjmp87xDIKxEjhAHdi10JTd978sS00PtrUKfHqF7wWUxY6jWfg-9IpKuaEaTO0Bp-DGt3Sl5RuKiD4LkRcVxLdCsrPcIfSsjs2BurM-vfXR31V4BBTM9svzFeF1gnXSenQTjOwnRxntGThD5hZ3rWsb03zViRNqGrs70sc10-lYbby5edrFYEF5s5gU_KNx24ueqP5rGSHxtgKho1oe67i3m4S492smGcbir8kDkTaheIwy54VMiEr6BLIZvKrpaH1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
جام‌جهانی‌داره شروع میشه اما همچنان با بزرگ‌ ترین غایب رقابت‌ ها؛ تیم‌ ایتالیا با شکست در مرحله پلی‌‌آف مقدماتی جام‌جهانی ۲۰۲۶، برای سومین دوره متوالی حذف شد و در این تورنمنت حضور نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/23087" target="_blank">📅 00:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23085">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8jp46bkE4ob3GUXgdUsheRxx8uahRtsiYh_4hetdMws51OtTikzoOg2udCuRa1CVpMS58_vF3O-8Q5LA6dnPsKjk8XWX_pbXWa6dybIzn06vevwi6QJ98kPgGWKZmMcJQuLqAdJ_mHh2DqnqpllpFih7xlek199uiVNshafkKDGDt0UAbBeWXLMH29AgiYpR0AAGerWnWLUOSXqXv4nRjP-AfkmPiYOkY0Mfx16hBhYWIYzD4p9mCreij6N79PNz4d4OBGZl6c3ASyUMfuE9AfNWA4eeprd1Ds8dgxEMcFHJeXd0wA8_H7Vdx_4QDsrj35KhHNdivl666ClzGNuzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
مصطفی پوردهقان، نماینده مجلس: بعد از رفع فیلتر شدن واتساپ و یوتیوب؛ ما سراغ سایر پلتفرم های فضای مجازی خواهیم رفت. رفع فیلتر شدن اینستاگرام و تلگرام نیز جز برنامه های مجلسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/23085" target="_blank">📅 00:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23084">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsFKxApqiWJa-bNqak3OVcYd_A8UEmdwnTcs_2SlNuHmI7N20LPp5VmVs2CaI3cmlNyYsQxiVoxbJb6GP6X4pDE81fS5sCWp1FABVcHGcIBwn86jMcm4j09dQoF1Be1tLvEIIbZQ7iCFWiCqqlZgt3VKpt9wraNiRIMhuBPaywPOlLmBu4O8IYAmkcuPY-f3PTrmmbE9wdi3NIIQ6jrzZTDPiIv-lobkeM3L9r3THVqrNdYA1VYpmqyBAGLBJp1WxAWTTgJUZS_AzQja3swuX5Wg3qgQNQ9RBdhnf59oPv6gyph3BUwo1qBjpJ3aTZBBIPzrk5_ZmenSUrJLUUSjLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
🤩
#تکمیلی؛ نشریه کوپه: پرونده پیوستن خولیان الوارز به رئال‌مادرید بعداز رد شدن آفر 150 میلیون‌یورویی کهکشانی‌ها توسط اتلتیکو بسته شد. حالا بارسا مصمم‌تر از همیشه به دنبال جذب آلوارزه. الوارز بارها به مدیران باشگاه اتلتیکو مادرید اعلام کرده علاقه‌ای به ماندن…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/23084" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MzBBpyppxzYGhL7OwJmu2lBHNm8YxKlQsaMdaHO2EeY_RnsZvInTW8Q1SDbzosZIpovDAuTfAInUEyGkwZ9UVaQLMPmyIX28s2eN8lIS9nZp8KtM4t30-AWXz-AYBQDDuerB8xidPrjFX4GZWTZUWH6lLiFWSo1-JwfxAnZf0la8pYLtHhnmraFSHQFiv5XnorqqteUX1he7O0ju_UytM2ON9eNNGH3UuoFOb1flf3ETyC4MK9oE3XkxnEUFqJe36NRZhewHHsrZFA3jV-VQ98vHVxxsXbILbqmszTtDQdBedEGdgcVGnxOT83Kfr6BgCZ_FO5HY4Rg5Od2vG26jkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ لازم به گفتنه که نماینده و مدیربرنامه های آریا یوسفی و محمد مهدی محبی ستاره سابق سپاهان و فعلی اتحاد کلبا امارات یک نفر است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23083" target="_blank">📅 23:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23081">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PptM2WyVTOtwQLgO76SBK44i5WaqpEFvPb-XYgHP40eDuI9bRx5zFwiUk-3aueOoER5raErwISieedGpQWPtLhXr0wkKJBdGE-oS5ocYxu5B9x5xrw22GnSyZeqUso49nC0oeA5p8y26PqbJN_ERXGNfakiX7Fs9dzN7swdt4N-U0zYhBICGj35dc3fIF1CkCIqqh0VwFwpEChTltYm2bdmMR5HFqJvApXhkCowDNg0vjo5Qbo7vqINVllHXApclH3ZXn5I7k8pIu1LaWsTXrCQhIdOZxibMMsLFpKlwmgaL97WyTmbHPKVf8Om6ZvVWyvz-koO5iQA_7hxdYN0I7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
🤩
#رسمی؛باشگاه‌اتلتیکومادرید در اقدامی عجیب پیشنهاد 150 میلیون‌یورویی رئال مادرید رو برای جذب خولیان آلوارز رو کرد و اعلام کرد مبلغ رضایت نامه این بازیکن 550 میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/23081" target="_blank">📅 22:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tAj2cm3VZuuMOv7QRsL86U-rMwblfyBn7j7z3ZhFk_H1hiAvGZhmh2e8i4B-UklxAJFaVYqLuNK4cNyjM7a06Ynrnv6pOoarOMtPNE6lt1nMdArBlEMvXzfjAqDF1MQjEDLjvNrEyVZqBKhRmKy3r-whHvPQxctmS7Fg_kgdpemx2FMTWH_nZvPs09mR_bQ0-4Lun9Nx2i9-kt8Utp6VN6cGmJSCR_BPUU_om0BgLY1QfEmkVF2BOmLplkevKN6rzjFGUBcZk7MJQEafmlB3tQZq9sM5v4kVrDtpD8tVzyzlxx6_djY-APznXzSqrAMFYNRux_dqsA16_6I9b7gULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ طبق‌اخباردریافتی‌رسانه پرشیانا؛ مدیربرنامه های آریا یوسفی امروز عصر جلسه‌ای دو ساعته با پیمان‌حدادی مدیرعامل باشگاه پرسپولیس داشته تا شرایط جذب این بازیکن رو برسی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23080" target="_blank">📅 22:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23078">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uvWlPIXxRxQ7BTwkqtQvZyhS7lTQPCa5H7XaxDSKY3GYPqvtpvtrks59mOfBBsmUvWyRJfFZqzj3UWePIz9WFFS_WXbXEgqu6y1ifx0Dfl6WXBhnQLQLoEpPytT6kZlQnWpsnqJjsWZejTfX30eFmYbvfxO0OcHbRt7FsPQUdjHpaJVdTSuvRUdbfAU7JbHdm-GEJ8Om0IF9U8yJxQwtam-GsP7ZdP3NywTvocb9RqU4NjqKA4m3BmhJVGC47OkZHXbhXGMhzTnRM5XoNWUxrKGp0JqkQXpgntFDlVoKgdiHd9uGj1pARGSZPdYsoJ9yATevhWLTLMbnH86lTDQ5PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QK0kZZ0SGrAfUxcW1ASHkK57gNwZuFJkd2QdSc1P_o8YlyUpVqRHybPRNMbVztgukIeXlWM2SYXKulRNMI8OcOVyo5eP4OMTUTvRTrsp5H_ky2ApDgQgJNcXecEvP7kS_cq2__54xhq4u_RAmVFJI9HzNl8mrVTh6EbmeyEEVByDkn4bLshFdw8F3pC9ATCxLIYT3anxS9sCFDggQ3utnr5EMF8Di5arHOYSkPt6qozl8Bekop4w9EGtNYU2-zja63NcTMSl04d-Xcp9M0VKbOb_5kWT5aKpHgGmBeKyrIhraCll0BKiIe26JQaeMOQx2CufXrvyn9GBZhHrKdyUCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
👤
نادیا خمز دختر پاکو خمز اسپانیایی: علی رغم‌علاقه‌ام به تیم‌ملی‌اسپانیا؛ اما بخاطر اینکه کریس رونالدو رو به شدت دوست دارم امیدوارم پرتغال قهرمان جام جهانی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/23078" target="_blank">📅 22:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23077">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_mveYRJvRrb0aqltjiMl5t5GABiobVzd6ApuvQ-T80fU-PVh77-b_Ynu8DqMQnQLFYyWB3B7ahPZ3ICkwQpRsaGBjw9EuahUkJ_HURFQ1c_ktNYgjevJrb5ZVwDwCzwtU_hQ5RDppvTfr4NnkrsOyDpYWUxhtmU4tAzijt_Sh9IiymVS5TTzS_On3C0dHUAZ82HCy2jFUuVLv7IBXe4BLzsEkt6e_-t51JueyZldqUX95bqnv9PgGfDa9szFbwGoTjCm-Uh1ac2DDznfIWHxqfwtVNUpYY5GC-kAUCuDWn7r3x72Fim7K38XA8JRVsogzISgZH9DKtN5azmNqEuTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی #اختصاصی_پرشیانا؛ آریا یوسفی مدافع راست سپاهان در بین نزدیکان و بستگان خود گفته که بعداز جام جهانی یا لژیونر خواهم شد یا به پیشنهاد باشگاه پرسپولیس پاسخ مثبت میدهم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/23077" target="_blank">📅 21:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23076">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/urxYxbIg2QrEv7nH_0DW34j8SI6Iq8ARS0BLfwI8P0VCTNXlLGIep2Qf5-6zWwZfmF2dTd0NBR0f4gZ6l1ZAESguigoYrK8Pl3oqYymIalBZr6ws98H2RLnv0MH88tW4qLRZMfY4GPzr2TDQW79zODLHHMnB4M09ddGGtu66rDRDQClkHs1elxEZqB_L1GaLtFFzQd0LplzyFhe_b-iXbUuxUUqYqNnr_feaGtFkVliFU2BrZemzX2Od00z9RwgQyr092yFfu3ZCy1DEZ10Y3fMt_zzc2LrexXucSQr8qR-WbEg0gsS1QAu3okQpU18PxJiq5MoFKOTGY6uGOYdhkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ علی نظری جویباری مسئول‌نقل‌وانتقالات استقلال با مدیربرنامه های محمد جواد حسین نژاد مذاکرات خود را شروع کرده تا بعد از باز شدن پنجره این انتقال رو بالاخره بعددوسال نهایی کنه و حسین نژاد آبی‌پوش بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/23076" target="_blank">📅 21:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23075">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWAhiiN4HAXUT-ggPNFvFS-9mbW1HXFqfZz4D-ANVjFWhGBvNNuDW3gYuHrZdKXbqoAc6IsVAC6mgTT-59KfIqJnrMynnnpRBy9JsY-dLKrBjztloBAIXeI6ps2oDXWUNXI-2AdOkKB_BfEvm3_5Br2hjMa0Xv8rTso1U0r9_8bqw5QqLVIrO2J4dIXM2Gvk5NrcULMSm0q7PgXVDSY2TI23FOBW50G6o2_IwS3ZjVuBCuYuO3FTUJ1NViHsaKzcP5Rul4LjlNVK8YGuZ-gy7mKrRkumzENWNuyoVfhtLNDAJ1H_vqUvIjcAYdD_G59scdnJR_RElKcyQRRH2Ur_tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باتوجه به اینکه هوا داره روز به روز گرم و گرم تر میشه این جند مورد رو سعی کنید رعایت کنید تا همیشه خوش‌بو و تمیز باشید. در کنار اخبار فوتبالی چیزایی که بدونم مفیده رو براتون مبزارم
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23075" target="_blank">📅 21:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23074">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiTMKeI-5FXk9QTqFC1wz7rNh94-0FTGzHxJGLfdSOzmvnd0lOYROmqIOV11yGVlIFOQxHcnSg2GML9UVpcX69r5F4Ab2fnQYQT7gPdCZgGFoQD0zzlXmlrXt6-dmXVyKs9rnNLdoVIb8kMvSc47YhUBXA5vayFQfstaU3CVMzlSD-rHPm9edHdqyBE5r0XoOzmJG-vwCrLW9oWzo1AtovXOBPWCqXW_AA3Fq9_CbP_BHuvvU2MaftLD8X_mYuO1lOFk5fUG2Cq_2_-kKGRnH_e_HBK63wcqgluAKlI1ezTnDYCUyX4BNKzUKfxJSe6_QQhzRVGdVm2zRoDxHnC2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛ قطعا یکی از این سه گزینه مدنظر فلورنتینو پرز خواهد بود. پرز گفته پستش هافبک یا مهاجمه. گفته‌بازیکن‌بسیار ارزنده‌ایه که مثل رونالدو، کاکا، فیگو ماندگار خواهد شد... یه درصد تصور کنید که‌ خولیان آلوارز رو هایجک‌کنه و 150 میلیون یورو به اتلتیکو مادرید…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/23074" target="_blank">📅 21:00 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23073">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cW_a_Q6f__x3VQMqKGIDj7mVqDvu0F303U7FpNwnvYiqJ54i6zsgPahoRWWqpaUw-p4F5oRYu_dTjeSUis6cYQbkplYoM1eaLsZjTon_11pKmSk3fKk73xlyS9LhGAvGqHMhYvYgsWDKD4eeiMwh_dB3VGMnrH5N0_nmXRP-7pdN_c09BVTWq7go1gx8iuMwdyP5IIYVtkR07je6XraA8pzQX_zciZoR2ni7rCv7s5GvV3l3kclFC8JRJ7qiRjW1Nf-B-hu9OoT6kM9M1K6O4lx0KY8eupth0YKQEWbqc97LaiwzYqssAIxMibxT3PIXVX_zBHQ4oIhF-aE7aVz2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛اسکای‌اسپورت: رئال مادرید امروز شرایط خولیان آلوارز رو از اتلتیکومادرید جویا شد. اتلتیکومادرید اعلام کرده هرباشگاهی 150 میلیون یورو پرداخت‌کنه رضایت‌نامه آلوارز روصادر میکنه.
‼️
فلورنتینو گفته دوتا ستاره 150 میلیون یورویی میخواهدجذب‌کنه.مایکل‌اولیسه…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/23073" target="_blank">📅 20:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23072">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udMp3mJSiuoDOx-hYV5UgFs0jWcNuF01MqZ_xNare4bysA4EIRTwdvWA_dIdPjSJexIB8_9duDqfr--AJzcLyMjD2vKP5tRhTWfYMxmVcJAQ8dSJDAuYBJl7vJVdpHR0sz7vNQm8pCGp2_BfDHpny1nUsnY3bzbg09SKe1KX3MSCT_CPfknlMq09D3hirujRjwHPN9D4GMG83KlzUKNMCRGkWjx4NkdT6HbaMFPDlePLY1mRdQUNoANfoDl3hiMayW7XLIW_YbmdqukiYDfTMrKV-tCjsaoP3xUQMzIzlpIqRIe_skn-S6BTfAg11zf5OshZaTOKKiSciIFfdgHxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
7 زوج‌برادر درجام‌جهانی2026؛ دراین‌دوره جام جهانی 7 جفت برادر درتیم‌های‌مختلف حضور دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/23072" target="_blank">📅 20:46 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23071">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=NxXEh_ZU3Z6wjVoRrtnj9npcjB6ctMBvJQuSugaziu0wA1S7dEJWJB2LyTWKzSxrEOn4vPmvls4-xBvQvhmYwer2_LWROGcE20BZ_GcigYWWAh3mV_yZo3Gdj2C29d0Zu6_rGrKG5AWJTiIxpXaAaqb2FWje5RLzuCHIZnIN7tFq29mSNaYo4ViLdS1NhTg3C1iYNYppZmtDFrLizxiOGacrGs04ABrOt2T3lI07Q23UabtlE2CPnPRa67EPQ3hz_Nj8BI9qq2L9C7KmrGUPNqm-iqIgG-d3Bp7go3M4JeVT6I_XvD4FZtHHkj7iGSvn4lDN8Gk3fLgVBYiumM1daA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/993bfd4bf7.mp4?token=NxXEh_ZU3Z6wjVoRrtnj9npcjB6ctMBvJQuSugaziu0wA1S7dEJWJB2LyTWKzSxrEOn4vPmvls4-xBvQvhmYwer2_LWROGcE20BZ_GcigYWWAh3mV_yZo3Gdj2C29d0Zu6_rGrKG5AWJTiIxpXaAaqb2FWje5RLzuCHIZnIN7tFq29mSNaYo4ViLdS1NhTg3C1iYNYppZmtDFrLizxiOGacrGs04ABrOt2T3lI07Q23UabtlE2CPnPRa67EPQ3hz_Nj8BI9qq2L9C7KmrGUPNqm-iqIgG-d3Bp7go3M4JeVT6I_XvD4FZtHHkj7iGSvn4lDN8Gk3fLgVBYiumM1daA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سوپرگل استثنایی کریس رونالدو به الخلیج بعنوان بهترین‌گل‌این‌فصل لیگ‌عربستان انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23071" target="_blank">📅 20:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23070">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/umL6wxofOW_cXOLst6sIk7cvHq2em_dKBzz2gi_Xbh6mkDQ-tg4cV1p1Jlm40XckAmkte4fpI5NNj3_d_n9skYbVtSQuWaEhkPB6MgsuIRFxyhxnCLeD0DSMFgNg3W7yOcIvWr269CDPNbBtLHUtzga0ol1VXGxNPRSE50iyMguWbV7bCZulsUIh83tULQy5M3rLqWkucJAR0bvxod4oWdVT0Q6w62BOEGNjyg9pjHvWD1EFj6L6OLFrqo9Tr2AFyknlJwpnnpobSeRPaW4O4vJzoRcXJr62vEK2G6Ji3T1VS7N5gnzmFruf0E0GgBQeGFMImshUTYDOqjq2Iw7xvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: برناردو سیلوا ستاره‌پرتغالی به یک باره‌نظرش رو تغییر داده و حالا هم میخواد برای انتخاب باشگاه بعدیش تا بعداز جام‌جهانی صبر کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23070" target="_blank">📅 19:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23069">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=XhJXoilqpNuv5qbgbXrRp7TVT8N5QSB_lnkyeuZT7eMYCJGGc6mFuHpLpNvbAw3xY18D9gNSKKR_cZenUU3z0qGYN7QPVniqQW0tbUl1vHTtp97KzlwpVp8i_U50csVj7xIgDfGIhxU_R-dEqZ1XR8uhKkSTVtr9gZUUmIXl4vywbIIQofxQORRWt___QAh-xKx6mAQus2o35ZI9wqHvqH4f_ixNGA5ceLQWScGRpLO1wglQoaIy9ADztnB6dzbJaceKvCA3anMoeKv3aKm30KUjKE-eOdBdb1-LqyY_cfrB1mDA5ra9lQh9Yniz3sOVceoUA_wjh_5UN8mV98TE8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bd17cf6e0.mp4?token=XhJXoilqpNuv5qbgbXrRp7TVT8N5QSB_lnkyeuZT7eMYCJGGc6mFuHpLpNvbAw3xY18D9gNSKKR_cZenUU3z0qGYN7QPVniqQW0tbUl1vHTtp97KzlwpVp8i_U50csVj7xIgDfGIhxU_R-dEqZ1XR8uhKkSTVtr9gZUUmIXl4vywbIIQofxQORRWt___QAh-xKx6mAQus2o35ZI9wqHvqH4f_ixNGA5ceLQWScGRpLO1wglQoaIy9ADztnB6dzbJaceKvCA3anMoeKv3aKm30KUjKE-eOdBdb1-LqyY_cfrB1mDA5ra9lQh9Yniz3sOVceoUA_wjh_5UN8mV98TE8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
▶️
#فکت‌تلخ؛ مردم‌ایران تنها مردم دنیا هستن که‌موقع جنگ‌بیشتر از اینکه استرس جنگ رو داشته باشن استرس قطع‌شدن اینترنت بین‌الملل رو دارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/23069" target="_blank">📅 19:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23068">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaiaIVTU53n00ccunnfoHwALj7jDzyQdu0tg7SMoO2-h82dekFliJ3S6NKziawmzFFdH5C0Qz8ujGXNb-qf8O0lJtNw-CtvPy4P3rMw8t6pDFzDITi_PyzLncQqtMRR16nLZkhJPceqvkEIp37kTX2_mBmg8EYVicwAX-Ng8RlF8irUJ943JWnwS0NycwDDEnVd4jzn7N_QeKhKEfserSKQHbglGCLNB1OfklLYpiTBK8nQ0f2rOzjXOxgHtDPr4pXIORJL1uZf4VVDnXrY8LGqsV3PnD3XaY03pDIXxj8iLXfG0TmL7TFDa3GvuejtMm7MEB0F-IIRxBw9zLWAuGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
🇵🇹
برناردو سیلوا: فکر می‌کنم قهرمانی در جام‌جهانی‌پایان‌بی‌نظیری‌ برای دوران حرفه‌ای کریس رونالدو خواهد بود؛ رونالدو همیشه‌سخت‌‌کوش‌‌ترین بازیکنیه که می‌شناسم و لیاقت بردن آن را دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/23068" target="_blank">📅 19:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23067">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LfJXAVFC-5mXxfBamRl5dC8eVG6XwFTModh4JgM22rSRHkgpc476EIsCQJgYqnliJ6ky8rgQupTjy8SvxHOICV-PaiWxdNTAuaYCSWdwyNBX_KjAhM_l-Pl_9_ldyFSwV5SPt7xk24tWWc2vW4Aemt4C8kHIUXwG4c4lgJJCUK90HVttmJg93GudHoBLNBD-k4HdKhSAus0nGUj1K7vacJWi7jBl4cIsuGtv35naBr-6QCWjYkffLfLRABK5Iug-0_8-1Er2sxw2rK35eS-m7_tUjfsdmtSU16Nb2zfcMf0Gbs7NOpqUfiZEjz_9OhfmubeqFlettC6JSrtafcsRDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
با اعلام حجت کریمی عضو هیات رئیسه فدراسیون فوتبال: تا آخرخرداد اگه استیناف نتیجه ۳ صفر به سود گلگهر رو تایید کنه گل گهر مستقیم میره سطح دو. اگه تایید نشد، ۵ تیر پرسپولیس با چادرملو بازی میکنه برندشون با گل گهر، ۱۰ تیر بازی میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/23067" target="_blank">📅 19:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23066">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v22g88Ta-xmQKtgiUaxz73yNH_JGViCW4u9hvpDARGWFegY4F7DYQoRAbdH6yHwDxV_B0JOGepzqI9fDQ5uBqm2C4ZOrvtFDCdOa0zoV-_31y19juvin3tiaRt1_znlVk0JSF32PYlqDmGih89MXYFt_-uMIzNe4ej1KzFkEI0xBhfuy-T4pPJp7pM6ekskWc9q5DSb2v0_GeHvyafNJRcBAxRvLBHu-eCPjJKWBTcSu8pg2r-YlEgzLqtYrgYXIzNLJ7jnShgrlFK4nnuKscRL2Ah1F6iwtTFUb3rV1QvNkbeH4bTdg7vxWGNxscFJ5BZm1l1f0NCZzVpsl8sbBvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
لیست‌کامل‌بازیکنان حاضر در جام جهانی 2026 باتجربه‌قهرمانی‌شیرین و ارزشمند در این تورنمتت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/23066" target="_blank">📅 18:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23065">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0_Y5IcYP0cYRxMtMKXgbaFkz2a0ZZRlc0dSPRKd74hEEZl1GuHIPF5FjxMs9Jxfl9Md7HwAmOgpuxrLqGf-Rk3-yOOMAPfiw80TzuEepY6_legx-XMEQ1VLXnpo7s_N34uCidAgCcsIvs_9TubnvJkELQ3EXfTiBElT7Ptk51DIQXXiZT1LZ773CFb0Ng5tXztKCv2FGUEJdvVM-bCtPD95mPtkwpS9kc-SXHwYdvWx6t2kD0C7zDuWRq6yaM3zkLHmrpHsiOTy4cr6ZNDvrwgsia_Du4F1nomaca2__bM1JFhRM2u7fbBYZOJCXTK52J-fAbdGGJoCFQLHZtsbdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همانطور که دو هفته پیش خبر دادیم؛ باشگاه سپاهان مشکلی با فروش محمد امین حزباوی مدافع جوان این‌تیم‌ندارد و رقم 70 میلیارد تومان برای این بازیکن تعیین کرده است. هم آریا یوسفی هم امین حزباوی مدنظر اوسمار ویرا برزیلی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23065" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23064">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/acMlDQMAp3vO8wyfWs644NQLZ6DFazucNIh29-yknW5_l5oXdmKR8G2kN8HLcdnIAKYGPigjsUoampMSg-u7EeeSi7-fRUuEW-vLLeCb_VzfMUx3xArLQWjUKTyphM5hYBCGgowucb-LSraIHrZEOHYLqeKajdf4EgtPVE_oC-Vl-qdaTNFt56lucQckC2ia4I5_svNyZ8wMO_XXD8r5ak5Do-HJHgM1EBeK5zDnvcX7or85PuuNMrdaWl9kW5Z89vmmom88Sgv7iy2J61CF7g1Fjb2u9iB6WUvtHq72JBZyIjJ0ZczXl6MVP_k1JCYFVggb2wQaksRO9UGMqIey6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/23064" target="_blank">📅 18:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23062">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucbGhpSfSIS3h6FTdCw-vq1tnz7UjjiQ-zerewgsQi1-xX-QS1dUrVNCe1drptN-kSw_m19q1J_VqExBfPl_rwvKnAFKt3ta9jl4ePX14zM44ATnI9StLoJf5C0w_3SaBYuaM5dP16MPnns0iyQ8UXN1yFraECRYr0nRr4LBvI2jH4GJOPeLSi1NTSFYXjbb8FfRKRwykVQkJNwvDqxJ84smCObunbEq0KBnlEb4n4LKUgb6k85ZKXA9hGEHpJJ3ZqD2aXsPt1wI7uOLGkPVRL4d815NDpY-41P56HKpWSpcPStwzY_1K0AUsKDPTEeAmnEjb2VbFuGGm9inYomTow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
ترکیب‌تیم‌منتخب مسن‌ترین بازیکنان رقابت های جام جهانی 2026 آمریکا؛ به احتمال‌زیاد این آخرین جام جهانی این یازده فوق ستاره خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/23062" target="_blank">📅 18:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23061">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a49850c982.mp4?token=B5gLetcllCHSwibHbrtnA7eqm7xzrDnjsOEwF1tRWNanK5MgzR5jUi5KI3r8jhU7ujx4vONGcUTceOPq5eyvA9rjA30f9Kxg1VJsOOzR1slHqoBGnSTTWpiu2_zdH4r1cs4yF3GdesTxkiRfDPfnFTmhe9CHjtw_yS903Dr3J4q7SKbZzAGnMhFyaskYMIB-9pErLT5Zg-iyWVv3tUPEV2zZ5y4VOJMf3VXq7H-AcbqHZWbAvqKiIfBSxkdMqiOJVN6k7r4zs0pLcqCEvgOq0ToyKdMjPG4uc6-H-BkwyPSTwPLtb8XEK67yq2AYGaIkHY2VRwWk6F_uFpmifREZ3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a49850c982.mp4?token=B5gLetcllCHSwibHbrtnA7eqm7xzrDnjsOEwF1tRWNanK5MgzR5jUi5KI3r8jhU7ujx4vONGcUTceOPq5eyvA9rjA30f9Kxg1VJsOOzR1slHqoBGnSTTWpiu2_zdH4r1cs4yF3GdesTxkiRfDPfnFTmhe9CHjtw_yS903Dr3J4q7SKbZzAGnMhFyaskYMIB-9pErLT5Zg-iyWVv3tUPEV2zZ5y4VOJMf3VXq7H-AcbqHZWbAvqKiIfBSxkdMqiOJVN6k7r4zs0pLcqCEvgOq0ToyKdMjPG4uc6-H-BkwyPSTwPLtb8XEK67yq2AYGaIkHY2VRwWk6F_uFpmifREZ3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇧🇪
کم‌ ترین انتظاری که هوادارای رئال مادرید از دروازه‌بان‌‌ تیم‌شون یعنی تیبو کورتوا 34 ساله دارند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23061" target="_blank">📅 17:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23059">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuWxGuqFN7jqa8PbXsTCfSVQZZnhQ0rB51eKXuymYThs9Ovgk6PlymX7BcI2uSCGzpyClJnh_fCEixKJX_q08VVZgmlVKPsxFNjhnd1FBrR1IxqyDYvn-6zWZrRwGtr7kayAKI0lDzZVaW6ob5KAIoGcGaIL-PNkJTZ-3_36gE5Bj9EbdspyxMg5BWArk5bAQM7-Ppe2BXUEc-bdNMFQfZx2QyISslDIHPC-sIHlvKhqeoQAQmvaWLqRIYvlxtDa4lgzZYSEB-8Os7Hv4kQTVyBKPwdo4T7CoA4VBgn6pbNJPq5earr0hXsHGKjgXm1rsFeu3Pr9KZaUQprFbaazWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y17A7QGjfMyXd0wFFKXAiyjhbkEoZzTAbRnFA17NgpLgMYXA5pzHpJehcoW2UnOliBrwZDey6y_Ij2k6PTEXZdZjfH-GRgG_KcYzErIOCHd7cBsxlvNLZUbDUpdNulcN6PfFAheHT4EY19xMlzzMztCzD8gdG3P-I1u_IgrhiIPOeudkJ-2SnM1-zWwoUGBLgLExM7aifLwvBrj_U2dYSNLIr_wpCVPZidOj6296g2-3k4VITm4nVdO6zKxX0gsAWYFL6Ld6LbQk26Vk8nM9OmSrTJ3RpcD22X9R_7tuC_AFTZ_GAwOFiqdZY5nW3tCnbv7zxr3sv-QbFXs2lzWxKg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نادیا خمز دختر خانوم پاکو سرمربی‌سابق تراکتور: از وصل شدن اینترنت مردم ایران بسیار خوشحالم. بسیاری از فالورهای من‌ایرانی هستند و در این مدت متوجه‌شدم که به اینترنت‌دسترسی ندارند. پدرم یک سال درایران بود که از مردم‌خوب ایران به نیکی یاد میکنه. برای همشون آرزوی…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/23059" target="_blank">📅 17:23 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23058">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7-hTkXaxw7P4j-4Q5OhftIwjKQ7FCmm38gIhDpsKuDeHx-3VshrTGB48bnRFNOqLCWKLaRIH9Ao13Ok-IAbCSy8J56TtRKNh7PuK6h3E38YZaQNL8fBmJhtVxt9mA593ghEtB74RCBG1mDWURazYROElPhxOzOr7JDy057EOnJEuRgjD6ASeM6S7xxDyvvTaCUVIMVll18xBaxcsvxIFAoJGY-ly3_BneMLPMUcOWCVzAW_bZmwIT2Nj6U7sb-u1EdI2BbTrHjf7R66VyVUc65n8Xt0ltqh8xYkz0MdKHLynaIFZGWUvaukynw64SlXDWOqgOlNwC6IpKUyYoopXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ ارگان‌های امنینی و نهادهای‌ذیربطه به علی تاجرنیا رئیس هیات مدیره تیم استقلال اعلام کرده اند درصورتیکه فرهاد مجیدی تعهدکتبی بدهد و در مصاحبه‌ای عذر خواهی کند مجوز فعالیتش در لیگ برتر صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23058" target="_blank">📅 17:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23057">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVKVrVS70Par-IR4hxOb8VyYDlBZAO0aix2N0u_Of5CJE4BwHpIl97Lr4F-3_NITPLNcO_ZGAQgGSsXcdGQJxxOCyur-sxfjZLbagdWkrkLDHReRTZoR9D43zupZ5_zsycE383FoOhHWdrk28ig36TnWCj7SU4_zlefBegH0XJHjjE38XMt9Xl_VWW52GzViQpyVuYddMtDD4XynluX4GY8JcbHR7ERVacKNTr3zWTFV35heCZ4BF6usmCSPPi7iLPWNlbhx3s70jarjtp0_ROChmkTVMfpe7F4s8JJo27Lf1qHVK9UaQLhG1NVkHjBI1YBNJeSA_MX3NK7iwMbfCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بمناسبت شروع تورنمت داغ جام 2026؛ سریع ترین گل‌ها ور تاریخ این رقابت‌ها رو مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/23057" target="_blank">📅 16:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23056">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0LjtsLPLX6BS15JqIGdkfOTLRj7xdLFfyhFb0IOBdA74uaU8-kykq2PBDt0MNnMpbWtY0XZXzXJyPZOTQRY2_BaMUwSWLUq6W2sQBmb1QzUhfNq3_-rdlwQKZhPylruu9yzvDSLuWosk09mTlgExacugvMU3XiYKSwW9GFmbyKZoYyJYbR4Y1JTWP_Xane2BU_-dNfpJoG3FG7muesgXa1s7yprQQx_jt_8G5gotENNiRAFIqVRMsKnmcSJ7BO3uPcGrwECLsNhBkUb9WKHvkPooLZjIaR-ZsnNVuCxQBdl3ffJ6h-Wp2Zptey-HCPZkgV2GmefKIpFTyEZV-jNyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فلورین‌پلتنبرگ‌خبرنگاراسکای: علی رغم تماس های تلفنی با هانسی فلیک؛ خولیان آلوارز ستاره 25 ساله اتلتیکو مادرید از پیوستن به تیم رئال مادرید استقبال کرده و گفته اماده این انتقال هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/23056" target="_blank">📅 16:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23055">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De_P6qwv_xyXuw5O3lQZkM7meB-OaSNUuvjtVLAPTDFf4ma470SJY6_jD2N0Y1FXZ4GG72Xbzx6PCMa-qodJD8Rd1Dvn3uh3CWYjLbhkzw8daKfbxl7fi5cTM16fj5QAqFl2G23KVYsKRXSXz1wYivrmfNirk1_sI5Y9PDtsTYXzv4hUlX8GzUjCgDdZZjZnBRyplTN_yMvFqw0oNVG-T7s6zSKMDeZsH5HUtjA1dCwgpZiouOam6-GniXEOL82-JNQeT1ab3VZsd0-FX6DQq_FN6YmLx6bdPoFNnSro_HxMpBXJv2S-MvRyolSA-S3MkaE6755WLxOKnfhEkQIZLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
عدالت در میدان، هیجان در جهان؛ جام جهانی با بزرگ ترین تیم داوری تاریخ‌فناوری های پیشرفته VAR و قوانین جدید پا بمیدان میگذارد از شمارش معکوس‌برای‌اتلاف‌وقت‌تا اختیارات‌بیشترکمک داور ویدئویی؛ همه‌چیز برای‌تصمیم‌های‌دقیق‌آماده شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/23055" target="_blank">📅 16:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23053">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mD-Vd1NosX76GpjLjAN0mTeohbJBSUC4yNQFIagpUENPJwjA9kak67fxQ03jWR4JXFz-WZkDjQ8erT1d5ivg8xWjhLSG_p07B7c9vCQvn0GL_ktlc4KYf_qKTmsakAQkQOAHfhyGRmzNi3Tr7MaD8fi9N0TftBGgfFwtjZVnYYCTrgkxfN2FvTRSsRQE8Y-PdKp9DOvvKMZiwvHm-BwzZ8kC4iOz_XmldDlsJVgsae46-X9OsZNHdLgL-9NojqpVfeli9JuDdeWI0LWOXsxfVQHCjQ4RXnsHO_W4qQubUTYqwqq26m9ja7YPBlPfG7mNBBdYWCo0XJmEckjUFlyqew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ اوسمار ویرا امروز صبح‌درتماس‌بامدیران باشگاه پرسپولیس اعلام کرده که به قراردادش با سرخپوشان پایبنده و به‌زودی برای پیگیری تمرینات تیم وارد تهران خواهد شد اما توقع داره که در نقل‌ و انتقالات تمام بازیکنان مدنطرش توسط مدیریت…</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23053" target="_blank">📅 16:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23052">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=Y0wcHOB2Le5VkGr3LpwgYuF-PN5WMwyweUhsl75F38VDc9FMjHlFXnw8O_96HXNVeCZQOmJkCxmrMfa7edhe1aKbevBRCmI84KLX3Wc3nbQEQ1yD-Y9mhb49mxjuk3D-J0fuITGJUOwlC8DepPY4DpDr28s97aI6CotWuGWW0pCHXV0c-cZOoL2eMXyaRxOftH4uOfDhUSq__QAmjaykmL5syYAVvPRmH0-iqiANiugfSPik601Uv9pxsSOBR4KWe6IjfzsYNfJUZ7U7m-YdYuTZku9ftpbMqmTRLMJVN8EbHVbCFkTYZNj11qGTBeMXkvtVLzfK4t8DM55o8y5JxwwAglgGiiyZWpy-5iXhdLpQY433xbwNX8eugSsGeX8YKU2NVgURev2hDnvyJfLsi_vltRA2m4AOyor8m_3JXUg4tnO8BwtLuNesNtvIi5GI5FJ66NUrnHT1SabQXMvR9OQ_VcFNKt8Fj6uhgB7butbXJSN3pGyvr0bB7QSV9pTgA8mHX7IWz0EfnnlGoyH63RKIHqWE3XLaD2fCCRV59U1Pzw-pkyGj0dWhIntgIl4nc4dIN6CtNiijiB82IJ3Ro9QpPLBXeDHDOZopIJs9UVosDizlCHuFuDJE33HDHWKpgMz7Xw-vuoBbduxid6sA0hOI--lgEseJ61Yo6yx21ys" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6daa12069a.mp4?token=Y0wcHOB2Le5VkGr3LpwgYuF-PN5WMwyweUhsl75F38VDc9FMjHlFXnw8O_96HXNVeCZQOmJkCxmrMfa7edhe1aKbevBRCmI84KLX3Wc3nbQEQ1yD-Y9mhb49mxjuk3D-J0fuITGJUOwlC8DepPY4DpDr28s97aI6CotWuGWW0pCHXV0c-cZOoL2eMXyaRxOftH4uOfDhUSq__QAmjaykmL5syYAVvPRmH0-iqiANiugfSPik601Uv9pxsSOBR4KWe6IjfzsYNfJUZ7U7m-YdYuTZku9ftpbMqmTRLMJVN8EbHVbCFkTYZNj11qGTBeMXkvtVLzfK4t8DM55o8y5JxwwAglgGiiyZWpy-5iXhdLpQY433xbwNX8eugSsGeX8YKU2NVgURev2hDnvyJfLsi_vltRA2m4AOyor8m_3JXUg4tnO8BwtLuNesNtvIi5GI5FJ66NUrnHT1SabQXMvR9OQ_VcFNKt8Fj6uhgB7butbXJSN3pGyvr0bB7QSV9pTgA8mHX7IWz0EfnnlGoyH63RKIHqWE3XLaD2fCCRV59U1Pzw-pkyGj0dWhIntgIl4nc4dIN6CtNiijiB82IJ3Ro9QpPLBXeDHDOZopIJs9UVosDizlCHuFuDJE33HDHWKpgMz7Xw-vuoBbduxid6sA0hOI--lgEseJ61Yo6yx21ys" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی‌از آندرریتدترین‌مثلثهای‌تاریخ؛
شاید اگه بیل فکروذهنش گلف‌ نبود و ژوزه اخراج نمیشد، چن جام از جمله قهرمانی در پرمیرلیگ رو بدست میاوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/23052" target="_blank">📅 16:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-23051">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGYJK-23wzCEFsyabYLfS5KEOIXLkTg1EwJ7nFIkhmjkTNsu7eiVA_dyJRJbjbu7BJdg4VccOnLxHg28k48K8HJndfZG11-YodoWWty3HWgO49bySLHHWv3CBxlLp_ObBY4CzplpbIKQZPkDaGCb70yilFy4iRkdCiOtHxCg34lR-UGTptbHi3I7wwxYW_9fWCz3fV5M2weokE-sBPyOoGJ1LgSdLp7qTo4S2beMmvf6L0GiU-pphOwiz8ywzgQYYpCJXkiNcrtUIH85GiXnDEVtxCXiPlr8CbcHx7CfF7eadDdIMPIlmY0Vbl43yxV4itSqOq-ghe50RNtSYbkwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام نماینده مجلس؛ یوتیوب و واتساپ تا پایان هفته کامل رفع‌فیلتر خواهند شد. دیگ میمونه اینستاگرام، تلگرام و توییتر؛یعنی یه روزی در آینده نزدیک میرسه این سه تا هم رفع فیلتر بشن؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/23051" target="_blank">📅 14:54 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
