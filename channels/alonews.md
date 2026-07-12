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
<img src="https://cdn4.telesco.pe/file/gXs83xBQpDXPTAqlZDYhWUt60pjHZsJ3-lP-AfDUV1sLWUUTvi5S4xI3MSzmiWmhQx-QDjROtaqChyKSYV55Q37UjIPUfneFozFeX2dYBT26v8cu03LTgnz-8GVCsOmh4x1sKrbAkaiodE9QFDiJGvYYzu8_-z-Dtsngohpf4rAWyM432soQhKaie7WoWGmHxJnJ7cM8kJV2WTyX7DcT7PsPGbZWWjPEqWacLjQwJsH9AF5A_ETaqDDKDAUFZ4eU_6rDNAVhga1E3vmRyQ3Uw2dLqBsgXAgTAdbKn8MZmqG00PuSxKozVhlZT0tlkasbU-hu2pNwimt6meE948vQ8A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 920K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 11:09:31</div>
<hr>

<div class="tg-post" id="msg-133402">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
یک منبع امنیتی اعلام کرد «چندین نقطه در استان مسندم عمان هدف حملات پهپادی قرار گرفته است.»
🔴
استان مسندم، یک منطقه کوهستانی عمان است که بر تنگه هرمز اشراف دارد و با امارات متحده عربی هم‌مرز است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/alonews/133402" target="_blank">📅 11:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133401">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/080aef9062.mp4?token=e7dfwcbeb_Y8qTyYDV110D6b7wDshw6VEVkXtT4WNC7vxL_hHoyMezqnq2nTFVck6kN1_Iso_xlISW8a-Q0-UoIwrb3x8-Bz87fXBk17nDc95EDsD15ETn2cwFswDUwmTl9PJ159kENmSYPGOkGA9FlDgd4zVouH8eQXxewTJ-tUtPEW1rUU5c-jp9oOVdp2NGHBBE_Wd6BAGc61quzuZPR4IjhxZcEjB8vG1aQIW2UstQMnFWYmqSARSUIUsey1NZUjhlxvoosmYi6mWMYQIzZJK_vG2lfpSPZU4UBElqiUJA9Z5Uk3HQumiXFkt_se2WotZ5lnUGKvo0I1xx0Mwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/080aef9062.mp4?token=e7dfwcbeb_Y8qTyYDV110D6b7wDshw6VEVkXtT4WNC7vxL_hHoyMezqnq2nTFVck6kN1_Iso_xlISW8a-Q0-UoIwrb3x8-Bz87fXBk17nDc95EDsD15ETn2cwFswDUwmTl9PJ159kENmSYPGOkGA9FlDgd4zVouH8eQXxewTJ-tUtPEW1rUU5c-jp9oOVdp2NGHBBE_Wd6BAGc61quzuZPR4IjhxZcEjB8vG1aQIW2UstQMnFWYmqSARSUIUsey1NZUjhlxvoosmYi6mWMYQIzZJK_vG2lfpSPZU4UBElqiUJA9Z5Uk3HQumiXFkt_se2WotZ5lnUGKvo0I1xx0Mwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صدا سیما : «به درک واصل شدن لیندسی گراهام را به ملت ایران شادباش می گویم»
✅
@AloNews</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/alonews/133401" target="_blank">📅 11:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133400">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lj1YFv_sA5jhHBYi4_02e_Dq7O6pcMSV_c9Jb84PopwBKkBI_lysU2uOnKYsHrmAjqb2OZc6LlPigsTvVRzY1fJbDrxJ2r-oS_JdOBfVq5Onf-BoVKMtthpKLJMqxdK25eWquO8JpknFd97FM5kfyGlTjJLcWp3jgz_CGI13bGFlU3IQ7fadciK6nFQYFHUKeqNSaMzyr4UxsKoW0GdALMr5pMLG4mTRQsjSbdGjPl0G6Xw8Q-Mfuo6LeWCEW150buqKZv9dB3_iWZvKXF0rfDWxVFElh49-17F1LLHXn1SGL6recKnAqTn3SedXuBwf6NP7FQt5KAvBZ5KHwEyRAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
لورا لومر خبرنگار نزدیک به ترامپ با بازنشر تصویر توییت سناتور گراهام که اشاره به حذف فیزیکی وی توسط سپاه پاسداران داشت خواستار تحقیقات در مورد مرگ ناگهانی این سناتور جمهوری خواه شد.
🔴
لومر نوشته سناتور گراهام چند روز در منطقه جنگی روسیه و اوکراین حضور داشته و کمتر از یک روز پس از بازگشت از سفر به آمریکا، خبر مرگ وی اعلام شده و احتمال مسمومیت (ترور بایولوژیک) باید بررسی شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/alonews/133400" target="_blank">📅 10:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133399">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALWU_7ABQA3XuSeIS6hJ_qfi5cVsGDb5baBxGeeqPKuYFVj9bKzsYHkvgIRS4WSOq6NCS4dxCLhXgqoyMO72aCnBC-mHUqDdQC7nR5_X20htMZUi9_SCsd6Taplt7qBCpvir0fZmZBE2l5ShSA7XuxoPSfpTYEPF2CvE-Ua7mMLuJ9gGMCxwwzq5Lf7Yk8oUO8K353l8G67g47ZfFMibBwxqhhqPAundRs05kafo2G5gUDzn-KXuuLfAvQEmdwQQEmrh_NFGaUWwC8Yh18-LY1EMH6yZaezAR-yrCJKD-NQUE2UTOlxKewSZue_ArOOLNxBMKTaCzcvcbB2ytqGbPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: سناتور لیندسی گراهام، یکی از بزرگترین افراد و سناتورهایی که تا به حال شناخته‌ام، درگذشت! او همیشه در حال کار بود و یک میهن‌پرست واقعی آمریکایی بود.
🔴
جای خالی لیندسی بسیار احساس خواهد شد!!! جزئیات و ترتیبات بعدی. خیلی غم‌انگیز است! رئیس جمهور دونالد جی. ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/alonews/133399" target="_blank">📅 10:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133398">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
منابع خبری از شنیده‌شدن صدای انفجارهای شدید در نزدیکی فرودگاه بحرین خبر دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/alonews/133398" target="_blank">📅 10:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133397">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a07524e3d2.mp4?token=vEGKcFta4J5jXwWALS00Z8NGC9ST7QSdURtZmc_sAkzQeE_kDcLm4e2RwWCVDQu-9wnrpBDlMjeGaohz0AoXl3IhxcW3t1eD08jfeLr66LDci2YeSMkx-6L-LQ3Tgz6WoHKVmafpwRj4POww-olNHzrzqur8dgzAjKY0RjAhbXtdQGpANE0jp-UHJIZXsd7oXv8XcO-p4t6-t2sHnBb2Ra8Lg_0maK1vkxeGFL14JhgGWHn3Md-EH9HLwRJ9zkIypUXMltP3AybfzILxRIkNuR-7dQ3wkVAbU9Cf5A4JHp31maIKgEIPjQU2vx0wp0iC5cVm0MZ_4hKqZYPa9-nyjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a07524e3d2.mp4?token=vEGKcFta4J5jXwWALS00Z8NGC9ST7QSdURtZmc_sAkzQeE_kDcLm4e2RwWCVDQu-9wnrpBDlMjeGaohz0AoXl3IhxcW3t1eD08jfeLr66LDci2YeSMkx-6L-LQ3Tgz6WoHKVmafpwRj4POww-olNHzrzqur8dgzAjKY0RjAhbXtdQGpANE0jp-UHJIZXsd7oXv8XcO-p4t6-t2sHnBb2Ra8Lg_0maK1vkxeGFL14JhgGWHn3Md-EH9HLwRJ9zkIypUXMltP3AybfzILxRIkNuR-7dQ3wkVAbU9Cf5A4JHp31maIKgEIPjQU2vx0wp0iC5cVm0MZ_4hKqZYPa9-nyjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور لیندسی گراهام در حالی ساعاتی قبل از دنیا رفت که دو روز قبل در اوکراین با زلنسکی، رئیس جمهور اوکراین دیدار کرده بود. او همچنین قرار بود تحریم‌های جدیدی را علیه روسیه به تصویب برساند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/133397" target="_blank">📅 10:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133396">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
بمباران توپخانه‌ای نیروهای دفاعی اسرائیل  علیه شهر کفر تبنیت، واقع در جنوب شرقی شهر نابتيه، لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/133396" target="_blank">📅 10:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133395">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OEiMvKWIGpraMo2uz_Y9t5ENlLKd9L2JPbCiFBUarSEUoV4Xo51hxKllBLkjN2cBxxR1IvmSaqeNlRJ2muaGVZGwqzfZKk9A7w9r4XYkDqoMjcX5vxgvU1T810Xt1Rjd0kBofmYT7lVDrwMEDPZ-ERULwoyeB7SM7MulEfya6o5A0fDMAoBjljvRsuW7fKV-PeXCbyv7ZrNCZmohHRTCbcuTJgCv0iqkjebZu_mLT1aQRJUa7NVaC7ZJOJVCaI_0iJmL4GfoerFVRSbov3EP4LDjGrrzNXObuoOoPHfz6uXZjtgXKnwwUgtK587cLUPsUZrbo-bTIrpMnmyoyDLDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بنت، نخست‌وزیر اسبق رژیم اسرائیل: قلبم از شنیدن خبر مرگ دوستم شکست؛ اسرائیل یکی از بزرگترین دوستانش را از دست داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/133395" target="_blank">📅 10:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133394">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
هم اکنون وضعیت در بحرین عادی است. به احتمال زیاد، پهپادها در خارج از فضای هوایی بحرین توسط هواپیماهای بحرینی و آمریکایی رهگیری شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/133394" target="_blank">📅 10:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133393">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpdZZRmGUPF07v-nWWlFTRZAvTsdOGH7vbse9q4dXECJzmMXFsmt4WN_2j78Vk4AfD2xy7rxb0w9dnoeIiVQ9XyvEjHGGchtho1TdX7Cjoe6Lc3RHZlbo_I_kIT_ib-WTFoAFaYxs2psNjFZCwYdkDGxE2NmRd70Xch6tkJaASQZxVrXtEQeZrQbazhLtYsfocU6vKWgixrqLYkqbAEC2bHg5UDNqM066JJk0SPLhrHAEHOeMv6wc_mT58mQ0VUgNvwB7GQM6nVF7MQOXkhdDlLlN9isLPkCjgrZNkLLdC-hiCNXR2u5L_ElbZaZtVJ8M4b5ArHv_4EU1K8aPB1MwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت کشور قطر اعلام کرد که سه نفر، از جمله یک کودک، بر اثر برخورد بقایای رهگیری موشک‌ها و پهپادهای ایرانی ، مجروح شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/133393" target="_blank">📅 10:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133392">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
وال‌استریت ژورنال به نقل از مقام‌های آمریکایی گزارش داد اطلاعات اسرائیل نسبت به احتمال وجود طرحی از سوی ایران برای ترور دونالد ترامپ هشدار داده بود.
🔴
با این حال، این مقام‌ها تأکید کرده‌اند که تهدید ادعایی در ارزیابی آمریکا «کاملاً معتبر» تلقی نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/133392" target="_blank">📅 10:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133391">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kAvPg8_Rak1Bj1bC4Qox6cFCrOjGQs42ADY7H_n3b_oY0eqk8_iU-sdzXEgWPh0h9XAsLzSluG4tOpm_ih4LQXDk5GMci6MoUIzfD5q5C_sL9RM_oAyBfRhvbkdfkr17ODHi0PH5lnHhvObk6r0USAPXr-W4YJBoAq6_sRvU0SY2nZWk0_T5xog80iaFZTMQK66tuMwuyu0XsGlp_IEYkHnyQ40g7OP0ZMM3OA3_k0CBQDY2yjw-aMH9RW_qLauKyWXTGrU0GMCxMAjGps2ZJnMpRnoB4_nlYhkkx6NBnBuV9admN-cUUvHhMz4dClj1c69rtdGHDX7QP07_lv83jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بن‌گویر، وزیر تندروی اسرائیلی: اسرائیل یکی از بزرگترین دوستانش را از دست داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/133391" target="_blank">📅 10:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133390">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
برخی رسانه‌ها از شنیده شدن صدای انفجار در کویت و بحرین خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133390" target="_blank">📅 10:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133389">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوری / مرگ ناگهانی سناتور جمهوری خواه
🔴
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/133389" target="_blank">📅 10:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133388">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
استانداری کرمان: هدف قرار گرفتن یک دکل ارتباطی در ارتفاعات جنوب استان در حمله آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/133388" target="_blank">📅 10:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133387">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mpodBFVtdKcyk6fkzg_dgxH4Be5LB1TFvQLoc-guigSzUcfzCGNXUQw4VFM0xKE5fnzxtZZxyA2_b44PQAwjcfya1PE0JgmBSUy_B4PPo1chZHMzwTfTgqQJ-5xyhmgSupWFTO3X9h4ETh2bO5nM_Mw1ht75i_GSC_eEg6yrqQnKsYffFX3WjGXJ1zzfD24cFuPuOg5nFfxxeoxAPvjJvBzLz4hCrUclYX9Skl7eqV7Cxd35xtGce_NMLEh8u8J3JpUVBMzAa9wx1owxZRWepLhkNK2T_JXkfwjC6CEu5DaRRFPRZn-u9IV2TPKR_S90WQgtQ8i8X-KdYDFYvOo-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ارتش اردن مدعی شد: سه موشک ایرانی بدون برجا گذاشتن خسارت جانی در کشور سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/133387" target="_blank">📅 10:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133386">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/ وزارت کشور بحرین از فعال شدن آژیر های خطر در این کشور خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/133386" target="_blank">📅 10:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133385">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff7e8ac85b.mp4?token=pJnx-y0f3mL0ip5RExcGv4p8_1gVWkpSF0aY1XQFnogdToLBGF1-D3eY1aSBmnDXbhK67gxQms6BisjVzKGBOUUXLEa_tQG6Lm1-4ovqWGROA3qN4fyHaUuhUOKuab5Sg2rI8Luw-CLGeFPEb0-BJoBhJrSEtGSfToF-uHxg7thP_bdM_YnjyszRlOo5_QjGORe6ortIpi5Kj5eqHszfz2MDELwPWpaGQrOywYZTnz7cKNYOzUncV-6Iy36d0_GzuDtt7u78UK3nJvbZGJ8bmSsNXBwnJDCYCiYvt-2Xz50Ta7_FgJQU-o44Le1PQ_KmY1YsVgsOJQ_iBtjKgbfuuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff7e8ac85b.mp4?token=pJnx-y0f3mL0ip5RExcGv4p8_1gVWkpSF0aY1XQFnogdToLBGF1-D3eY1aSBmnDXbhK67gxQms6BisjVzKGBOUUXLEa_tQG6Lm1-4ovqWGROA3qN4fyHaUuhUOKuab5Sg2rI8Luw-CLGeFPEb0-BJoBhJrSEtGSfToF-uHxg7thP_bdM_YnjyszRlOo5_QjGORe6ortIpi5Kj5eqHszfz2MDELwPWpaGQrOywYZTnz7cKNYOzUncV-6Iy36d0_GzuDtt7u78UK3nJvbZGJ8bmSsNXBwnJDCYCiYvt-2Xz50Ta7_FgJQU-o44Le1PQ_KmY1YsVgsOJQ_iBtjKgbfuuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سناتور لیندسی سناتور گراهام، مصاحبه با فاکس نیوز در سال ۲۰۱۸ میلادی:
🔴
«قصد دارم آزمایش DNA بدهم ... احتمالاً در نتیجه تست ایرانی باشم و این وحشتناک است!»
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/133385" target="_blank">📅 10:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133384">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرگزاری عمان: یک منبع امنیتی اعلام کرد که مناطق واقع در استان مسندم کشور عمان، مورد حمله پهپادها قرار گرفته است.
🔴
دولت عمان این حمله را محکوم کرد و اعلام کرد که تمام اقدامات لازم را برای حفاظت از کشور و ساکنان آن انجام می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/133384" target="_blank">📅 09:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133383">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شیخ حمد بن خلیفه آل ثانی، حاکم سابق قطر، در سن 74 سالگی به دلیل مشکلات قلبی(احتمالا ترس از صدای موشک های ایران) درگذشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/133383" target="_blank">📅 09:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133382">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRJx8xJdTibMRsmJIZguQmmi-iNz6xawbefwjn5Nao8gPkYTlmf2-MKVes58bK6XEsAEOEE3JPNH7P1pD4rcA6gcm4F-_KvmK1Rnd3t-2HPQx8C7zrlPcOYUN7Zv03rMM3W55THPE3x-b7gneOvHcN961N2cHlDW9NRAuxv580rvXwf4IM_6Rkl998jKgTAsU5RG58_tbblUK9Pc4MME8yTJbpPfd8AvfTOrmHBKEOWPsEpDtVy_8zxmTVz7umz2DsKnXWQp9M_T9PcIk-CboiTWq721uU4r95S6X1uDz123HmbAJIPuXJTh7cf32fbv2SdVF48Ldtm-KuPlaoGCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / مرگ ناگهانی سناتور جمهوری خواه
🔴
دفتر لیندسی گراهام، سناتور جمهوری‌خواه و جنگ‌طلب آمریکایی اعلام کرد که او بر اثر یک «بیماری ناگهانی» مُرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133382" target="_blank">📅 09:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133381">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sFjsqenhNw2MVxdUN7WhuMjve7LiSyrjeQiNHqLOa7DWKIrVgq45twaKa1x1nTzlmtblypnI5Uco3NpDZEABybGpKlylapKJji2Anvoo9grOQGBUvI7peQjMUTSJfda3NSkQK3M-1VkbVRsl1bqgUzAlhSTL-bDSRLpEqYCmFb11Zi_e0F4kO2P365EFvv_O-Tmv7DT_tDKexiiVmB7hIi7LnXDKI4cxY4NcYWEWxciQsgDUpQCabTarcROKkbnFvvUAw2v1pSMAdrUz1zcekP2KC6v44Tjn6hXUkhKB-LrnSPnc2R7qXLC7_Lb6HnKocbDPHERPSM4ZSha22ilcnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون امنیت ملی: تنگه هرمز را با قدرت گرفته‌ایم و با قدرت حفظ خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/133381" target="_blank">📅 09:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133380">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
تلاش سه کشتی برای عبور از تنگه هرمز؛ اصابت به دو فروند
🔴
طبق تصاویر ماهواره ای شب گذشته سه کشتی بزرگ قصد عبور از تنگه هرمز را داشتند که ایران دو فروند را هدف قرار داد. یکی از آنها از کار افتاده و سرنوشت دومی همچنان نامعلوم است.
🔴
سومین کشتی تحت اسکورت نیروی دریایی ایالات متحده آمریکا موفق به عبور شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/133380" target="_blank">📅 09:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133379">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی انگلیس اعلام کرد گزارشی درباره وقوع یک حادثه دریایی در فاصله ۹ مایل دریایی در شرق سواحل عمان دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133379" target="_blank">📅 09:37 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133378">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
اهداف حملات امروز ایران:
🔴
پایگاه امیر حسین در اردن
🔴
پایگاه هوایی العدید در قطر
🔴
بندر شیخ در کویت
🔴
پایگاه دریایی پنجم آمریکا و منطقه الجفیر در بحرین
🔴
بندر الدقم در عمان و مخازن سوخت ارتش آمریکا
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/133378" target="_blank">📅 09:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133377">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hC3RYMKqdjZb8Obb31H9cxJuiOxIpQ5OA02oEsTAeXps0kWzrQFGqEkxpVosjCPMpq6Qh2Opv0E3Sd-EH5y-lJpJktGXlGrMSlFWDUjytn9cTBjtidiITO_OCu4XZJ7h8L5z8AqJ0Q4jwjHEPk_A5wTdDlOYlwFqQbiZCuT-D_Ki2DQa0BjTK2wy_K6Ueo_RDHWwpwIor35lnt6llk-Gu7DYX8SxO73KO58hKI6yMur1axLoLeojUX3PGxQUME14ZPxEfYOo7kJ_C539oqT_l5FMunPufRX9EixDgj4HJlFPkRLPFvKuMYc0GSD64BRJzAwQkcijGF7N4PqlZS04xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر هدفی که در نزدیکی شهرستان خنداب استان مرکزی مورد اصابت پرتابه امریکایی‌ها قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133377" target="_blank">📅 09:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133376">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
امروز؛ آغاز امتحانات نهایی دانش آموزان یازدهم و دوازدهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133376" target="_blank">📅 09:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133375">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fR9swTCZt02SqdIIHhl5_FsXGhQq0Sg9Uf-aFnStf2BhYysO_4iJyt5R3gc0__56xANEduPHyiriITc8CG6K-PClsAjL22rhF9XV100DrO3b2KwqJpvxZZu5aWSoxr9t_EdJIRGuu3lvoxUpNKgWkGYcD6QZlBLY86a1sohEZR-ub_w3ei-DzbDaurcjoFX2ZSnzVSdcDbyR77mSBfzHA6hoIwsqVqEpfFuzlkYang-AnSVfcTWj5GdCHihB41vMgcsM_ZvEo4_E_VJkNv1CmffosHtEOLD327pbN6yYmo6wFbJbpTTtlFkKSv_hRkL2H3kIvuciB0EWRX6eEYe0MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / سازمان عملیات تجارت دریایی انگلیس اعلام کرد گزارشی درباره وقوع یک حادثه دریایی در فاصله ۹ مایل دریایی در شرق سواحل عمان دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/133375" target="_blank">📅 09:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133374">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqXRklZ0j24xffHw8-2xkWTu0aOjJGCwa_xtlGBc889xyYHbqiihps5ZiWxU14YVz_V4LPd-tSf4H-QtET_5NcEN9DDXtk1svkvbPmPTFZyH8-GtHXHxN6t6hVW2ujxk-i2ChmQD7C29C0eWHRE8jQ-xmrgm8QiJPunsirPOQRzAifYJ4TNMK96STT16WK3W-psIfjMxOeWOy777sfEfqjutlx4gE6FWUAqTYvzfGg2bFS-xCr2jh8ocKtGpTphCD4SrWn_NiNfKyd1Ryjxl71UdgWRXH8dPsr5aqdtlijncxGNDOrkwvX0pbqVQ6tZNVuXoC2AoRmRkNYoXUXS-Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ستاد ارتش کویت اعلام کرد پدافند هوایی و نیروهای نظامی این کشور در این لحظه در حال رهگیری و مقابله با اهداف متخاصم و بیگانه در حریم هوایی کویت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/133374" target="_blank">📅 09:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133373">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6496896d1b.mp4?token=ABtlvm5qckj5HQr__r_xBLVuyqXclwWxbwT8LAypIjNUfgj7VG8U1Hjt0wxNvi6Xa0q8dVsvlFtlUVj9xd2XvwQ1_XY1lmK9RLid-ywAtSGJ3cVmOyK2fKfHrInsvnzsCsDRxkZmdxOqxxYVuo0debMGbi_bUagXBaISvTBAAW6zKdj1B_4b2-TUMgKgwG2EuXvfiSwGbZjomBdOMp7Hi4EWv2krx2upuCL7KBXYAX2h7dqDLG-zVRnbHPno7Gs2GEtUQgX61TS3jNHkbm3Ay94nz-A9io3TdNzR7u-7oMJ6zLZI913bRs6hHjr8XcuRr2qae3ku7emRcv84cvHjoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6496896d1b.mp4?token=ABtlvm5qckj5HQr__r_xBLVuyqXclwWxbwT8LAypIjNUfgj7VG8U1Hjt0wxNvi6Xa0q8dVsvlFtlUVj9xd2XvwQ1_XY1lmK9RLid-ywAtSGJ3cVmOyK2fKfHrInsvnzsCsDRxkZmdxOqxxYVuo0debMGbi_bUagXBaISvTBAAW6zKdj1B_4b2-TUMgKgwG2EuXvfiSwGbZjomBdOMp7Hi4EWv2krx2upuCL7KBXYAX2h7dqDLG-zVRnbHPno7Gs2GEtUQgX61TS3jNHkbm3Ay94nz-A9io3TdNzR7u-7oMJ6zLZI913bRs6hHjr8XcuRr2qae3ku7emRcv84cvHjoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری / وزیر دفاع اسرائیل از عملیات مستقل قریب‌الوقوع علیه ایران خبر داد
🔴
یسرائیل کاتز، وزیر دفاع اسرائیل اعلام کرد به دستور او و نتانیاهو، اسرائیل به زودی یک عملیات مستقل علیه ایران انجام خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133373" target="_blank">📅 09:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133372">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDEgZKn3tAbZrWcxYOk0uhvPPBAuz9q3tf5lrQgky8UDT1Jej7i64eJwN9keTPJad8Rx9nKn-8kAkcOdkjHeghPrRuIspCXCHVOk4XyIZUi1F3xpelqGoRa4Lk8-VGc--1XN60n7VlPFvs0JK0_65E3Cgm3_XWaBvuGctYCD3DhiFqO9eEjlf5FlAEytO-8xkJGmIp1KYeYhwdR4EXE9KLJD_NyHgjUv_FPvf6ZFiMg8PM6J_l0mVAhY3IhHKUiKh5FEhx0XKOBmgjt0yPUkmyz30Px4r5QyZqIky0F8Hf_ud4TuhdePQRuP13wUE84-m31JBFv55daVGTAz8b4tbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت پروازها در آسمان منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/133372" target="_blank">📅 09:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133371">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
استانداری لرستان: صبح امروز یکشنبه شهر ویسیان از توابع شهرستان چگنی دوبار مورد حمله هوایی آمریکا قرار گرفت
🔴
این حمله تلفات جانی نداشته‌است و هم‌اکنون شرایط عادی می‌باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/133371" target="_blank">📅 09:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133370">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
این دور از حملات ایران بندر دقم عمان نیز هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/133370" target="_blank">📅 09:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133369">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
شهر هایی که تا کنون مورد حمله ارتش آمریکا قرار گرفته اند
🔴
بندرعباس
🔴
سیریک
🔴
کنگان
🔴
بندر دیر
🔴
عسلویه
🔴
چابهار
🔴
کنارک
🔴
بوشهر
🔴
ماهشهر
🔴
مثل حملات اخیر، تمرکز آمریکا به جنوب و خط ساحلی ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/alonews/133369" target="_blank">📅 04:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133368">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
انفجار در ماهشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 94.7K · <a href="https://t.me/alonews/133368" target="_blank">📅 04:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133367">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کان نیوز:
عمان به آمریکا اطلاع داده است که ایران پیشنهادات مربوط به تنگه هرمز را رد کرده است.
🔴
در پاسخ، واشنگتن تصمیم گرفته است که محاصره دریایی و عملیات نظامی علیه ایران را از سر بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 95.5K · <a href="https://t.me/alonews/133367" target="_blank">📅 04:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133366">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFH_iqE7BWEcbnZhHXa6_1d0qe9ACIfFfTWL3LVwMmGwydlZ1xTqaBd8gnWjDc1VLq7b-p707_hq0Fw_VbWm1btF7DjDGH0Eov0HGI-cNH4ncoWByk98n0q38BDYCu3NQs-U8ZgEmdtSQ6BbwA09YJBUnH3ZDWMXFpoH-yKkcEoYckmpSoxZJ3u9q0mYUqgMlWILiripj7Yd3F8A1TNXlxG6sp-zvYXQZlExwLt7YISAj7d5diyysZHil3EuZficRWq_ZCdKD5LISxHy3ZJyG3i1e2amUPtR8919Fx848tA5K-kxet_DZyLB8OVQiyZmCDANhpL7pSjSVgOHo0ZoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شلیک موشک های آمریکایی از کویت به سمت ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/alonews/133366" target="_blank">📅 04:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133365">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
حمله آمریکا به پایگاه هوایی بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.4K · <a href="https://t.me/alonews/133365" target="_blank">📅 04:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133364">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔴
فوری/انفجار مجدد در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 87.3K · <a href="https://t.me/alonews/133364" target="_blank">📅 04:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133363">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
گزارش رسانه های عربی:
هواپیماهای نظامی آمریکایی به طور مداوم به سمت ایران پرواز می‌کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/alonews/133363" target="_blank">📅 03:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133362">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
یه کشتی میزنید، ۲۰۰تا نقطه بمبارون میشه!
🔴
هرطور فکر میکنم عقلانی نیست و حماقته
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/alonews/133362" target="_blank">📅 03:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133361">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
انفجار در جاسک
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/133361" target="_blank">📅 03:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133360">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
چند انفجار در بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133360" target="_blank">📅 03:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133359">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0U4DfkXeB7IuMQALnVdiBsvaoR8H4lJ9TmYYUxWqgu8l8I1woBNYPyLv1K0ztsyxvdkjREzuOsPzfob5pRFuUc-d2kxmJueSG8IJgoOoxWWHtwsb2-fLKlu85QN-E4nlkRyoSs_JIbPqVKgEz5Z1-rpUphXvJmuNd5eyZJPXRufFRVNyTxtvvQiigDA48qJVVzv-f-9aChCM0YH4pp7lCm4hss5QDhRp2Hp98qDpx-97cdAJIAfZ1JcqmUXhJkHI1oc3bSOPG2-vRfiE5lLlRfZZUVE2s51l1dtpHx_0-rb283NoH4G5poVxyxH4O4YRPKbrk0kv0lwttg9ekDUmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی: الله اکبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.8K · <a href="https://t.me/alonews/133359" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133358">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری/گزارشات از حمله ایران به یک کشتی دیگر در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.9K · <a href="https://t.me/alonews/133358" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133357">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ee80a6069.mp4?token=gFl8S8NfkarKHJKcJY6IGfWtMAfRtd0NSKGgga2vnuZQ5X550fnda6-nBFh03g1K_QPkqdG8Ikdzj35u8g3oyE7NLNOdstk6rVVcM72k1TLgEy3D6eW0DOxlSRLQx57kH4Kmu42jWmfPRXK4mF2BbNrsZ0KgolSijgfFsVnmBdcMEORcHjw6_3P2lnS9TmDRD_YjVs2PCWe01rYpRdaltUrwzPeRmuUQ_m0fNkMZ7hDdofYPCfu5GMIAUHXWwTczVBFC_PeeIgpW72eiDfd_XBVkxXmX6GVQ_Z2MZnqKnr6TQex339xNFVBD6vGiaplQQj7Z6bDRWAoeXGYzohqdHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ee80a6069.mp4?token=gFl8S8NfkarKHJKcJY6IGfWtMAfRtd0NSKGgga2vnuZQ5X550fnda6-nBFh03g1K_QPkqdG8Ikdzj35u8g3oyE7NLNOdstk6rVVcM72k1TLgEy3D6eW0DOxlSRLQx57kH4Kmu42jWmfPRXK4mF2BbNrsZ0KgolSijgfFsVnmBdcMEORcHjw6_3P2lnS9TmDRD_YjVs2PCWe01rYpRdaltUrwzPeRmuUQ_m0fNkMZ7hDdofYPCfu5GMIAUHXWwTczVBFC_PeeIgpW72eiDfd_XBVkxXmX6GVQ_Z2MZnqKnr6TQex339xNFVBD6vGiaplQQj7Z6bDRWAoeXGYzohqdHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/دیده شدن پهباد در آسمان تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/alonews/133357" target="_blank">📅 03:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133356">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
فوری/پدافند ماهشهر فعال شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/133356" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133354">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">💢
فوووووری/پرواز جنگنده بر فراز تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 80.1K · <a href="https://t.me/alonews/133354" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133353">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
انفجار در عسلویه
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/133353" target="_blank">📅 03:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133352">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/پرواز جنگنده در قزوین به سوی تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 86.7K · <a href="https://t.me/alonews/133352" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133351">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
نورالدین الدغیر خبرنگار الجزیره در تهران:
اگر وضعیت کنونی توسط میانجی‌ها مهار و کنترل نشود، تنگه هرمز می‌تواند به نقطه آغاز یک جنگ جدید تبدیل شود.
🔴
به نظر می‌رسد ایران پس از پایان مراسم تشییع، دیگر از آن محدودیت‌ها عبور کرده و اکنون بر مبنای آمادگی برای همه سناریوهای احتمالی عمل می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/alonews/133351" target="_blank">📅 03:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133350">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
انفجار در کنارک
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/133350" target="_blank">📅 03:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133349">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdwE7rI8BVFouu_ynxN81U0TUk2yCixabc7E2ZmIa8Sz1sv-qBUVV-8ztUrFGNRQLzzXOE9yuRCmOHCesntgiv_BWl8wMmtEmXnQ1ruBzfdxLRAPvnl2ism7jhEBBFestPAl80XO-dKiF2DAUITrOw52YixasCLyYmeA4bQL5FSl9r_SWqIHNL2O9K1Ch4SdBpS-8e6ZCs4r5dS47cWE5l-7irYBhBv9Jmfsfe1dQqxZrhCtSr-_9g0dIiltmhrzJQqFPcLezbEAtUem2BNWO4Ivx_DbmOlj2f_9Y4_h5MiKAA2FjceBI1TPExOYBtApaLFFKILQEXZBS1k1a0g0tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/هگست،
وزیر جنگ آمریکا :
- ایران انتخاب بدی کرد، حالا باید تاوانش رو بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/alonews/133349" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133348">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
انفجار در سیریک
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/133348" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133346">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ic4A505jhWb1CwC_r8wvrlc4ju3-yukzF11MAvHgEWzi8iE6zkF-k3iJghPKdZbMNdz8bMVymPTPjPk-gjyIes_YnSNTCOWFiM5Qy03RbAklihW-HCV7VjXTSc7MwDv-gBaDwuIWgSkJN6gQYYBtqRO6uRBZ-V6d6zytkOkeEoeZC2N7G6qsArZdLLLaD4SHSSvAzkwxFyORHAU3aeAKpEEPnLbB91dkT37sUn0OFEW8IqlpG-nW8gQ1IegGZYXcttTlM9Q6114eIpA2z3sgXmoj9H0XoiPoDDlUmTmTvwRXbH9neDhu_DSItZiZYHW5ahFJ7Z_z8Eo27UNCCih9ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ساعت ۷:۱۵ بعد از ظهر امروز به وقت شرق آمریکا، نیروهای فرماندهی مرکزی ایالات متحده پس از حمله آشکار نیروهای سپاه پاسداران انقلاب اسلامی به کشتی کانتینری M/V GFS Galaxy با پرچم قبرس که در حال عبور از تنگه هرمز بود، دور سوم حملات خود را در این هفته علیه ایران آغاز کردند. یک خدمه غیرنظامی مفقود شده و کشتی به دلیل آتش‌سوزی در داخل و خسارت قابل توجه به موتورخانه قادر به ادامه سفر نیست.
🔴
پس از آنکه ایران به خاطر حملات قبلی به کشتی‌های تجاری مسئول شناخته شد، اما دوباره شکست خورد، فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم به ایران داده شد.
🔴
در پاسخ، ایالات متحده با ادامه تضعیف توانایی ایران در حمله به دریانوردان غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، هزینه سنگینی را تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/133346" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133345">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned «
🔴
این چنلو حتما داشته باشید زمان جنگم پروکسی هاش همیشه وصل بود  @proxynab
»</div>
<div class="tg-footer"><a href="https://t.me/alonews/133345" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133344">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔴
فوری/بر اساس گزارشات، ستاد فرماندهی نیروی انتظامی اهواز، هدف یک حمله هوایی قرار گرفته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/133344" target="_blank">📅 03:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133343">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن  اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی پروکسی |  پروکسی | پروکسی</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/133343" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133342">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انگار نتا یکم ضعیف شدن
اینارو داشته باشید تا در صورت قطعی متصل بمانید
✅
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی
پروکسی
|
پروکسی
|
پروکسی</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/133342" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133341">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37792480c.mp4?token=n50fFsZp0pGpVzHMNPTM_rMdACl3lJOr31x9L8SEn0nZfms-ZZj9Qb3AoaDyuPxHI2sccPQ5eYJvTD59Z6Yt_YzP8_p_4veYoCFiMBtg4QNUHMaKcb9GO3bII9pZ4pcwlFNEYzVfDcESg8FtJiZmZ08C3FEF9JwKcIYTZNmd43JkX-iIZlogVAyqa18etLmtqPf891Sf5vCfWKqBWQqZCLwrb6VKOkbV2yhIdQepFEz531-RKuIjAdCRLjfcR7Zo-wG1SlUZVBwLET1b2d8A66BD5ZGfYXVIIyUdbBp0EPMr799vOji9WYAYZH45Rl6jiAG9TNlUiuZMaCV_mtGYvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37792480c.mp4?token=n50fFsZp0pGpVzHMNPTM_rMdACl3lJOr31x9L8SEn0nZfms-ZZj9Qb3AoaDyuPxHI2sccPQ5eYJvTD59Z6Yt_YzP8_p_4veYoCFiMBtg4QNUHMaKcb9GO3bII9pZ4pcwlFNEYzVfDcESg8FtJiZmZ08C3FEF9JwKcIYTZNmd43JkX-iIZlogVAyqa18etLmtqPf891Sf5vCfWKqBWQqZCLwrb6VKOkbV2yhIdQepFEz531-RKuIjAdCRLjfcR7Zo-wG1SlUZVBwLET1b2d8A66BD5ZGfYXVIIyUdbBp0EPMr799vOji9WYAYZH45Rl6jiAG9TNlUiuZMaCV_mtGYvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جوری که دانش آموزا صبح باید برن حوزه امتحانی:
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/133341" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133340">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
انفجارهای پی در پی در جنوب کشور
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/133340" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133339">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">💢
فوووووری/پرواز جنگنده بر فراز تهران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/133339" target="_blank">📅 03:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133338">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
فووری/سی بی اس: حملات به تهران هم‌میرسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 90.8K · <a href="https://t.me/alonews/133338" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133337">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
فوری/انفجار در قشم
✅
@AloNews</div>
<div class="tg-footer">👁️ 89.6K · <a href="https://t.me/alonews/133337" target="_blank">📅 03:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133336">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7sVCytAoU85DGm_Ctr0tqZLkS-pPEpXHyN4EdWklkstZ3VxPDTkX5i5iJ2seqPV3nAd_4vMmr9rsf6F3_KCq3RYwEZIabZsBuzS8DRJ08tLO1OZNsmZlD2OCzJLgFKKQlylGwiP1H2FC-ScUPq_lDXqXf2o6Zr8J04-rMv74_VPG2YgnXN3ZLzRtD_5sXih_Fp7zFCIV7VUuy0hxqHOCY4XhAwnbxkwkieTojf3R84xuy1gtE_Jo95n7eWqyEjm-8j0UW1p334Ktvtu2a-5sUEgbavtNmjfNza8cYUxlpvUH4NNJ42OtBDILraTy0zsjhl0kgVACXYRRafeN55m0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/انفجار شدید در بندر دیر
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/alonews/133336" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133335">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/133335" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133334">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری/انفجار در اهواز
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.2K · <a href="https://t.me/alonews/133334" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133333">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری/حملات به تمام خط ساحلی جنوب
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/133333" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133332">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36c2812772.mp4?token=qH9v7jDAjMWKuy2LMdP65JSlh4Rrbv_8i9Xccf1zwh_35-4p0SzjnVSQzAD76-9cvLbkHNypL7Sg-RcFXA3JnmmU8eZ2f2EVAUqsG0H3ZISGgrTLP6Ru3QGPgHsrt1u3RFEejVecehreHMdqyveLJ7i39hHsh4Rs_b6PH22p0rbWIrjPXPLucyUTkSj_AipY6S6sKiwmK9pQmFP9D52bihdWufwRuoHFUFTfYodFMCoTqaqkJ5jH_2b5jMT6Rt3ezLka50pcmkKj8AFLbE59OVc_ahhVAPUUfPWyCvLKjYprAXtoouamR-cPa8xFNUOdEIB_NeKlh4APtclAyFsp0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36c2812772.mp4?token=qH9v7jDAjMWKuy2LMdP65JSlh4Rrbv_8i9Xccf1zwh_35-4p0SzjnVSQzAD76-9cvLbkHNypL7Sg-RcFXA3JnmmU8eZ2f2EVAUqsG0H3ZISGgrTLP6Ru3QGPgHsrt1u3RFEejVecehreHMdqyveLJ7i39hHsh4Rs_b6PH22p0rbWIrjPXPLucyUTkSj_AipY6S6sKiwmK9pQmFP9D52bihdWufwRuoHFUFTfYodFMCoTqaqkJ5jH_2b5jMT6Rt3ezLka50pcmkKj8AFLbE59OVc_ahhVAPUUfPWyCvLKjYprAXtoouamR-cPa8xFNUOdEIB_NeKlh4APtclAyFsp0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/آسمان بحرین، دقایقی قبل/ظاهراً مبداحملات به جنوب کشور بحرین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133332" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133331">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در دیر و کنگان شنیده شده است/احتمالا اسکله دیر مورد حمله قرار گرفته
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/133331" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133330">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
فوری/گزارشاتی از شنیده شدن صدای انفجار در عسلویه و بوشهر
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/133330" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133329">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🔴
فوری/العربیه :
هم اکنون تماس وزارت خارجه پاکستان با دو طرف برای کاهش تنش در منطقه در حال انجام است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/133329" target="_blank">📅 02:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133328">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
فوری/اولین تصویر از موشک باران تنگه هرمز
مشاهده فوری</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/133328" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133327">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
تابناک مدعی شد: گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
🔴
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/133327" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133326">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9lP7YmL0dh83dWEDq7hFyL_H2iahCPAUtjFqIEERtYJX6HMV1psKRKBa_csTGkpHccgkjfkdV3wZr6Tse6hDYMVTqP2Jp9glUuDy-YjnAC2kBMbcPERUs8l0vUiTqTj7e5GQfBL9WMgORKCJDPAQeQcT-wLSc2ZRGt8f_2Yd0YeFT_8g-gmpLE7i0EyuREea4ajDLJFWRxw5V79WB5phB2dEstb0ZrhBZsd0lcGm6vb4dap9Ut9bniWo3-a2gWCF552Tae_qvBo9LM2-Vpet_MgTzRxD4trAlNaa9YpOlWlc1MzPXRRc3xRh6spDfoUbtyA89FtJ30qTrBahUkUJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کانال 14 اسرائیل :
مذاکرات به بن‌بست خورد؛ ایران یه پیام جدید برای ترامپ فرستاد و گفت: از این لحظه تنگه هرمز رسماً بسته‌ست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/133326" target="_blank">📅 02:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133325">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">💢
فوووووووری/پرواز جنگنده‌های آمریکایی در مرز ایران
🚨
@AkhbareFouri</div>
<div class="tg-footer">👁️ 71.9K · <a href="https://t.me/alonews/133325" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133324">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
فعالیت های رادیویی شدید در خلیج فارس توسط ارتش آمریکا.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/alonews/133324" target="_blank">📅 02:17 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133323">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
کانال ۱۴عبری: پس از اقدامات امشب ایران، ترامپ ممکن است هر لحظه چراغ سبز حملات به ایران را نشان دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/133323" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133322">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLMVH5knlCyuam4L2ARcoV1a8O2ixUtB36wO18PvQdVGkjAeTv3UpQYKNS-UGte8DTKQHxIglKBSu-5jwkvJ_pFWwSBpXWpfwRC9bSu14BhXu4SKDERVGwxsy5FSN8WgkpaSM1ZNBHIy2Ags8EmC_Y94SXQohl31hcrJmj_2_gUG61kSEknDqx_ZkLByV-fNbS_u91ZLLssCuVHgiQX0JU4VkH3epr6rrmggoOOf7AjaQVuDOwJtx36tZ1aLSP_ToKsOf2gkYNAfQEE7SEXFFS0ndtxczHrLTdl0TZrialZ4PVcv9FqK9-uylOJa41S-4x9tEKG4-yhucaUtMKX0FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
همین الان ترامپ که رفته بود گلف بازی، بعد از شنیدن این خبر زمین گلف رو به مقصد کاخ سفید ترک کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/133322" target="_blank">📅 02:13 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133321">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFhc_uGOb57QSAqvC_-Uv0klZhUGvKDQyOxfs4o9VjgqGquyQToTQ_nfXdiwWSv9vhRJo6dovICQXJPzHnu-T0eLnqAI29tqG3DSDlubBqN6U3sw3AyOFrqd6EjuGzKmqBcgOFgROcoKDHYJa0T5MbchuDH-EEyCGgT1GibDcxX4pDNabE86B6eLCYx4Z0PI3yw8PAkchkFXx8vf0--H-__o5xOm35nD8--72h5sIOhyIqw_MmNWiAkbNq1kW-9Y5BHh9VKPVano52SwNnlGoe-10bhsX0GzuV7R8hjtO9LLRnfJd3VnKdlufSnCvQ_Rc4Epah7-NBq2DMBKlYDp8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون زیرنویس شبکه خبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/133321" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133320">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
آکسیوس:
ایران ساعاتی پیش به یک کشتی تجاری در ورودی تنگه هرمز موشک شلیک کرد،
موشک به کشتی اصابت کرده و باعث ایجاد خسارات گسترده به کشتی شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/133320" target="_blank">📅 02:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133319">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
منبع عبری: رهبری و نیروهای مسلح ایران مانع بیانیه تسلیم تنگه هرمز شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 83.9K · <a href="https://t.me/alonews/133319" target="_blank">📅 01:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133318">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
شبکه خبری آمریکایی «سی ان ان» به نقل از یک منبع: عمان اداره جریان کشتیرانی از دو مسیر جداگانه را پیشنهاد داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.6K · <a href="https://t.me/alonews/133318" target="_blank">📅 00:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133317">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کارشناس فاکس نیوز:ترامپ ضربه اصلی به جمهوری اسلامی را برای بعد انتخابات مجلس آمریکا (آبان) برنامه ریزی کرده است و تا آن موقع تنش‌ها در همین سطح باقی میماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.6K · <a href="https://t.me/alonews/133317" target="_blank">📅 00:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133316">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9_tv91Df3A4Qd9aLTDX3ASLfADfJeA16-zXDH5hdVw4lh34c-ChZ-RPAmMjDH6jfeYqQhaVrH7t59gvSz9KRpMdFW8-OTCgJ-ZyqBGg4K1lHgBgr1nFxw8jmJ1h-dNU4bS6gV37d2EJnxB0jXiJJGLLmCsI_0p2e3aBJG2huJLvxAXo38YMJevNatQ78S-4EY0R1F3BtDPN8GogOyeiaLJhFU5sGsg5aEmBTeAkQtbEiSARHr_5x6E5c-Y7-Izt1HdbC_QQkQSRxn5b5wReoc4yxN45uQg6dvQGTUmyXAP95R17dObnLQdyqL6mYZsm71Sy8HKWeXxkQ0MPoV7lbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری C14: ضرب‌الاجل ۲۴ ساعته دولت ترامپ که جمعه ۱۰ ژوئیه صادر شد و از ایران می‌خواست حملات در تنگه هرمز را متوقف کند و ناوبری آزاد را تضمین کند، ۳ ساعت دیگر منقضی می‌شود.
🔴
این توییت برای 2 ساعت پیشه و 1 ساعت دیگ مهلتی که ترامپ داده بود تموم میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 91.5K · <a href="https://t.me/alonews/133316" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133315">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
نیروی هوایی و فضایی روسیه، در یک حمله به شهر چورنومورسک واقع در استان اودسا،  با موشک های کروز حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/133315" target="_blank">📅 23:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133314">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / گزارش هایی از فعال شدن پدافند هوایی در اصفهان
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/133314" target="_blank">📅 23:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133313">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQQqqWM71mXFpxLhqy5XvJ2cG_fIygoHtVdKZ_IFcWjA5tJ3fAzb2BluDkLm2OmAk_3HBwG0QhCu3_BQjGa0BhhD1J9L1xBghqo_qSY-moWH1Fk-VdMXHsMOZygR0ZoHaVEsRj7AWM84hgx4mRYnTMtAizZCL7HAOGQ7OGC8wWOgGuAr8caRB29AnOC5XLDWlBmoF6ygsK7XZCAZmxeTFT1RUm5aafIyeOVmThREm52B1Qs_p2Kx4HBurUErCcxu9ElU-8-1wh7iNWFlUDhe0BF5SIob60JDKkz_5Yy2aJCm6N81-tVU62lW5r6eED_YtBaBOGo2F_QhPGZPheolKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واردات LNG اروپا از آمریکا
🔴
وابستگی اروپا بیشتر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 82.2K · <a href="https://t.me/alonews/133313" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133311">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obg6-e3T9TsXTmfok22vZIzIC_tC5eMGKWviTDX2W51Gny9Rne5rY6w0ggEWw3bqQgy0HyYkpCl7vKNmqV9V9qosApQ_bpB-ZW64ma6dxJ52EA6v_2mQmKninArrs3Z8RVlvBSz-zUiiEZiAr1okSuXzTq8axy2qyCK2Y49TbGthmSGDRnbyh-meJzmQ3shBk6bxcb65cSyo_ykejA9cIANS_HAx-D3G_w2Dp7xTtlhAssAq4bvhd41YniSGGgoEwcbQHSvgr3Y1U0lxAMnE1aJePe0zHXVONE_GZ-XY5XNFcg2rset2wnQCTS64uD5JhIkiosBCVauYNqsUY9K2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
داده‌های کپلر نشان می‌دهد تنگه هرمز قبل از درگیری اخیر به سطح قبل از جنگ برگشته بود و تانکرهای پر توانسته بودند از تنگه هرمز عبور کند و نسبت تانکرهای پر به خالی به وضعیت تعادلی برگشته بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/133311" target="_blank">📅 23:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133310">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
سفیر آمریکا در اسرائیل: سرویس اطلاعاتی اسرائیل به ما اطلاع دادند که ایرانی ها توطئه جدی کردن برای ترور ترامپ.
🔴
اونا 47 ساله شعار مرگ بر آمریکا میدن و بنظر من تغییری نکردن، اگر یه نفر بتونه رفتار اونارو تغییر بده اون فرد ترامپه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/133310" target="_blank">📅 23:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133309">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
شرکت توانیر: از این پس اطلاع‌رسانی مربوط به خاموشی‌های با برنامه و اضطراری، با هدف ارائه خدمات دقیق، سریع، شفاف و هماهنگ به مشترکان، صرفاً از طریق درگاه‌های رسمی انجام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/133309" target="_blank">📅 23:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133308">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
مقام‌های آمریکایی ابراز نگرانی کرده‌اند که اسرائیل اطلاعاتی ناقص یا گزینشی را در اختیار دونالد ترامپ قرار داده باشد. این موضوع ممکن است به ازسرگیری جنگ با ایران منجر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/133308" target="_blank">📅 23:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133307">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuG0wGNcYTajn43jTfORGs1AWbLCyy7djVKTzrwFZQo1lFLe7pvHUWRkviv5lrzhNuu4-yr9s2931bombtlbmy01qzZBytth89J_bMiQdnD_bVKhIcfiOYWraxGyfl7rZHMsHpcnggK3jP5Fz2yHOeUjEDNKueYzh8OPoTTdUw_Dr0EriDp4sbdq-AJAjgb4Lql9jr4Vu76TKaiY6uLQtTRnOEn4-txwws0S-U0B7B8cQgCei-4FM73q6I-4TAHqU8Wcqq5vOpbCccsjjhKuME005w_wrnKcaPiMIkJbkH9hO0rfhmRgZmBf3A3WWLwBfQ7-lm6Ino9KzIh09Ime0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی تقویت شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/133307" target="_blank">📅 23:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133306">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG50cnsq8kUwFRNOpfTszOlalegAbT-p-BpekFZL_kC19S5Kldnf9CRZIfmGYLAVNAXZBiGpverzFD421pLsPg5Z85MGoGxpHobLIEZOufX-ew0fCClEqfnc-5BUTCkclThay7v3OT2VsXQUFIQqEBb9AiW89Nsk3j9zsZzu5hAfR44H7Srsl2k97Egdroc6bVDC4GOXTbUeWsINH0FyToHIxn5C3nvjubxZ5vOCOTRSPGhM6sRHea8Kq8l3DvsmtYAhW-Fg3fsmfxA2G47OrYA0yIv5hX7OS42apUunGFYjeU_bg__-FsNcpQN2Hz-iwRA3jYlZd3YCmyISdCyx_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جدول اطلاع رسانی خاموشی لارستان منتشر
شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/133306" target="_blank">📅 23:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133305">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
مهر : اختلال در شبکه بانکی همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/133305" target="_blank">📅 23:06 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133304">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
شرکت برق منطقه‌ای تهران: بر اثر حادثه فنی در یکی از پست‌های برق، برق بخشی از مشترکین ساکن مناطق شرق تهران دچار قطعی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/133304" target="_blank">📅 22:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133303">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
سخنگوی آب و فاضلاب استان تهران: هیچ برنامه‌ای برای افت فشار و نوبت‌بندی آب نداریم، چون وضعیت پایدار است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.8K · <a href="https://t.me/alonews/133303" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133302">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فوری / نیوزمکس:  ترامپ در حال بررسی ازسرگیری محاصره دریایی است
🔴
دولت آمریکا دو ناو هواپیمابر و بیش از ۲٠ کشتی جنگی را به سمت منطقه هدایت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/133302" target="_blank">📅 22:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133301">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19bcae33a6.mp4?token=SoesGmJkQLB8qeJ6BkuT5HZ-zzgmiBtsQPcAB1HuWqTFhmYxmkqykoBgOvLwcs9DUJE3HGZKd2An5GkFXznc6Uym4BoPxck4hJLiosGbi99WdNQD_JXjgK5hRx-vubqR5QLjvjJfNB4pW-8lxmK3XbZJwqDN44HjkHpoicTGXGRqFirTn4-Q5urKLQcfFE9flaTOg6aqScoofGYKBostAk969W11TaPQVmWIIiV3pkeF43nNzz7DyZBrCFHv85JV6Jl-bnxnzACKTwlNkEaIpfG22Y23hOPHp6ye7r0McJsOzBVBuoopqdxkBQ7q2CQGC2_dtIdAU9jFmzm4kveA0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19bcae33a6.mp4?token=SoesGmJkQLB8qeJ6BkuT5HZ-zzgmiBtsQPcAB1HuWqTFhmYxmkqykoBgOvLwcs9DUJE3HGZKd2An5GkFXznc6Uym4BoPxck4hJLiosGbi99WdNQD_JXjgK5hRx-vubqR5QLjvjJfNB4pW-8lxmK3XbZJwqDN44HjkHpoicTGXGRqFirTn4-Q5urKLQcfFE9flaTOg6aqScoofGYKBostAk969W11TaPQVmWIIiV3pkeF43nNzz7DyZBrCFHv85JV6Jl-bnxnzACKTwlNkEaIpfG22Y23hOPHp6ye7r0McJsOzBVBuoopqdxkBQ7q2CQGC2_dtIdAU9jFmzm4kveA0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ضرغامی: این مذاکرات مانند خوردن گوشت مردار و میت در مقطع اضطرار است
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/133301" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-133300">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/udKC4c3M62nBoFaRWa4D2QnYzH9mtWpsT_P2OPq31u7XRKwxffnFPfEdZ4b9bha2gbU0mh0nTLB9CvlTgttVKXx6sVT6F9-KV9E0FZYUU82TqwLYXxjx8qEoYp_y8vO9jte_JUeVnbHRINLUrSJ93XiV0KZlwa12cUqFhA1O23cEIadhc1a-yyAtP8qWTjjFUE1SWZIJYIGyJjIIHpSlMf6fZlmOIZ-rL17OaIt17CkBzicbmMt0Nr1_Sid_9wVIbW2zyCB9-A8uLUlj_HnrPRs04-XdtBGh5OG1NlsJ15cALhjoTWpUaaXvL4FTb3uehvRs1YVmCevITI99K3jGnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
باراک راوید : یک دیپلمات آگاه از مذاکرات گفت : در جریان مذاکرات امروز در مسقط
عمان گفت مسیر ما مانند قبل باز خواهد بود
🔴
این دیپلمات گفت : ایرانی‌ها نتوانستند این پیشنهاد را در جلسه تصویب کنند و مجبور شدند آن را برای بحث‌های داخلی به تهران ببرند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.6K · <a href="https://t.me/alonews/133300" target="_blank">📅 22:53 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
