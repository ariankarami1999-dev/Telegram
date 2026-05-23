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
<img src="https://cdn4.telesco.pe/file/jVsoh1bFgrvecqjwEdrPWzmID6ZMXtk-B6wJ07ZVGluEX97op3sPXLSYJMi4B-0rQQ-OmwR4c0xpbk0pQWB01n5x11hr5SJApwinok1u9t0drV-MmkF56BxkIyLgIKk7qBZrquGBpgdioFX5s8dV0tYJz-4Echm6OEG_BEglJiFKutnxc7vb4dzmwbZEeg9DQ9Zfw-MBoJtXcOlKJTVF_j6xfV_Yv8uh6lGzZCPvXR0JIRDPMBWR4yrgjHKIFubGXZiPxLGuyyKg7vsGJNl_zoL8tc3M8zXngS-qipWvm6XrpA5eKXsj1dPQWaMnTybSUQUrbdY8DKRmnKIbAdFUDw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.92M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-02 20:25:29</div>
<hr>

<div class="tg-post" id="msg-653680">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رسانه‌های اسرائیلی به نقل رویترز: ترامپ گفت‌وگوی گروهی با سران عربستان سعودی، قطر، امارات، مصر، ترکیه و پاکستان درباره توافق با ایران برگزار خواهد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 274 · <a href="https://t.me/akhbarefori/653680" target="_blank">📅 20:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653679">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
اکسیوس به نقل از مقامات اسرائیلی: نتانیاهو نسبت به توافقی که در حال مذاکره است، به شدت نگران است و ترامپ را به انجام یک دور جدید از حملات تشویق کرده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 748 · <a href="https://t.me/akhbarefori/653679" target="_blank">📅 20:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653678">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06609fc3d1.mp4?token=sexhduwTkHgZ9Xi3kWLX8LOskNgzCRR-_xeu1qViX3xW0o20FWkz28qXmSrXoUw1-4uvyn_j6MWsorx9AtZc-938tLKvDYmE9YoEjW8t3xbbyRL6t5m01NuH79qZ7Mp_Voo6KSOundv0LRro8FA3-y2EtL7tsYjNLDe4wyG00cVmPuLVpdvQmW78NOQqt7ih8uFfys7wu3ZgKw6O17loBLw3QXd01JfxmeYvza7eywVrMSfz3ioZTyCRyhOqHVyDtI-kUGzIp0E9coRxCsKqDffK_PyePS5HVPY4cR6VD7xEvb3m1Cgky9lVKlP9uKCzG-NC2advSKRFoxm7Kq5pug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06609fc3d1.mp4?token=sexhduwTkHgZ9Xi3kWLX8LOskNgzCRR-_xeu1qViX3xW0o20FWkz28qXmSrXoUw1-4uvyn_j6MWsorx9AtZc-938tLKvDYmE9YoEjW8t3xbbyRL6t5m01NuH79qZ7Mp_Voo6KSOundv0LRro8FA3-y2EtL7tsYjNLDe4wyG00cVmPuLVpdvQmW78NOQqt7ih8uFfys7wu3ZgKw6O17loBLw3QXd01JfxmeYvza7eywVrMSfz3ioZTyCRyhOqHVyDtI-kUGzIp0E9coRxCsKqDffK_PyePS5HVPY4cR6VD7xEvb3m1Cgky9lVKlP9uKCzG-NC2advSKRFoxm7Kq5pug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر جنگ آمریکا:
🔹
ما از نیروهای هوابرد و واکنش سریع خود خواسته‌ایم که در هر لحظه برای اعزام به خاورمیانه آماده باشند.
🔹
این نیروها به‌عنوان یک سپر آهنی در برابر عوامل نیابتی ایران، از پایگاه‌های آمریکایی و جان شهروندان آمریکایی محافظت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 875 · <a href="https://t.me/akhbarefori/653678" target="_blank">📅 20:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653677">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nCBd7LhiENDRpBdqUa96X2QiKmpNS0YbMqbgdQlL3t7TahoVAHWEtAbmF6hsMfMi3tp376fG93Gb5zg1inTvtfKkiUgNGhq-8HyuHBfTA_WsbrpcD-NgiAHxfs44uSfdk0WVxo3dhj-lAShO9NHhiIjvzfVUUr8qOqPwmICtve6O4IURWCj6ZU7rc8yVNcRRuMNX2h-yQFsY7QLB1E0Rkq743DgFe9LQbuVjZYnwGzBFSdZjYGtwZS-cSbfwrB_VnzFgQKmDFrMSkD1Fc6ajxSSsyW1JVDIfgIBBXVh9yNX2DEZ_ZTd9gQjw7S7r6l0Dj896K48FFmVP3zD9ywVLMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
محکومیت شدید جنایات رژیم صهیونیستی علیه لبنان
🔹
سخنگوی وزارت امور خارجه، ادامه حملات وحشیانه رژیم صهیونیستی علیه لبنان طی چند روز اخیر، که منجر به شهید و مجروح‌شدن ده‌ها نفر از جمله چند امدادگر و یک خبرنگار و عکاس لبنانی -احمد حریری- و تخریب گسترده زیرساخت‌های این کشور شده است، را به شدت محکوم کرد.
🔹
سخنگوی وزارت امور خارجه با اشاره به نقض‌ مستمر حاکمیت ملی و تمامیت سرزمینی لبنان و شهادت بیش از سه هزار نفر و مجروح شدن بیش از ۹ هزار نفر در حملات تروریستی رژیم اشغالگر علیه لبنان طی ۳ ماه اخیر، بی‌تفاوتی و بی‌عملی شورای امنیت سازمان ملل متحد در قبال این جنایات را شرم‌آور دانست و بر ضرورت اقدام عاجل جهان اسلام، خصوصا از طریق سازمان همکاری اسلامی، برای توقف اشغالگری و جنایات رژیم صهیونیستی تأکید کرد.
🔹
سخنگوی وزارت امور خارجه با تمجید از صبر و مقاومت مردم لبنان در برابر تجاوز و اشغالگری رژیم صهیونیستی، به خانواده‌های شهدا و مردم و دولت لبنان تسلیت گفت و بر همبستگی کامل جمهوری اسلامی ایران با لبنان در مسیر دفاع از حاکمیت و استقلال لبنان تاکید نمود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 843 · <a href="https://t.me/akhbarefori/653677" target="_blank">📅 20:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653676">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad6a5fa78.mp4?token=HOUTUSVs9cf71lSr-vmZDRvnM2F9m69e6FXd6ZET4MSXwjObUx3IVaRWmEGGoRfizJNR005XPZldHpAwAgpCGUhB_-B3X5UNyO-MS3ZTBL98NjfdLrIRFyOoIyMEl1lSTARcSJ5SiNGRWM7235zwezkeOnH2K2kuEbGXHhLdFLwxBcFlYOFZGe5cAdXf14iVXxe4KG8JJ1X0dPCZd4bREvD8jZI-Y5_v72OzjGUOQ5tyA5zwgHphE-CP4tfbJsKqlirkOrSKfdK20nV2pljtZ8IbMMS1Ouk5qwiWI66MZffIBn-UwNMOcqBKa31R9EpFCdrZo1SbPqbZDkvNqLttxp_WMl16SXTFpW3u44cfBaMpfYnDH8EnrpIU-GJv2ImIXBJi9p_LGHG6Q5T5x1oGnA3x2CaRamnB-MqPSIcXKabD2jlDEj06QA5UN229QKYQZnmDR6rrfklTIh9f4US8MTXVXQs-NPRVdFiJm85_oNqvu7MFac9ielpzIxwwPZaiEh7xVb5MKAIfqs-_f1bg2slO3Lv-mDlhun-xK114XfHQyo2Zl-rggoV8d0LnEZterPLzner50DK2sjrke_c97QF1ImSIX4aqYEMHrwl8uYP8fTQ38KTKvYAAA_fBvyDPg7NsDEiYHPGRG6bJt_h9hFzoxpbQgvSGTdndqzrln4Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad6a5fa78.mp4?token=HOUTUSVs9cf71lSr-vmZDRvnM2F9m69e6FXd6ZET4MSXwjObUx3IVaRWmEGGoRfizJNR005XPZldHpAwAgpCGUhB_-B3X5UNyO-MS3ZTBL98NjfdLrIRFyOoIyMEl1lSTARcSJ5SiNGRWM7235zwezkeOnH2K2kuEbGXHhLdFLwxBcFlYOFZGe5cAdXf14iVXxe4KG8JJ1X0dPCZd4bREvD8jZI-Y5_v72OzjGUOQ5tyA5zwgHphE-CP4tfbJsKqlirkOrSKfdK20nV2pljtZ8IbMMS1Ouk5qwiWI66MZffIBn-UwNMOcqBKa31R9EpFCdrZo1SbPqbZDkvNqLttxp_WMl16SXTFpW3u44cfBaMpfYnDH8EnrpIU-GJv2ImIXBJi9p_LGHG6Q5T5x1oGnA3x2CaRamnB-MqPSIcXKabD2jlDEj06QA5UN229QKYQZnmDR6rrfklTIh9f4US8MTXVXQs-NPRVdFiJm85_oNqvu7MFac9ielpzIxwwPZaiEh7xVb5MKAIfqs-_f1bg2slO3Lv-mDlhun-xK114XfHQyo2Zl-rggoV8d0LnEZterPLzner50DK2sjrke_c97QF1ImSIX4aqYEMHrwl8uYP8fTQ38KTKvYAAA_fBvyDPg7NsDEiYHPGRG6bJt_h9hFzoxpbQgvSGTdndqzrln4Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هدف‌قراردادن خودروی فرماندهٔ تیپ ۳۰۰ ارتش رژیم‌صهیونیستی توسط حزب‌الله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.18K · <a href="https://t.me/akhbarefori/653676" target="_blank">📅 20:17 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653675">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان به نقل از منبع مطلع: بن‌بست در مذاکرات میان ایران و آمریکا پایان یافته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/akhbarefori/653675" target="_blank">📅 20:14 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653674">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenelli Motor Iran</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apGMN_zAoY0_XCMl_QryNmzS-ROk0ruQpq59JTlRSvnvxghB7K-N7T7oCNyGDxJb6o7xUzYa5XWPvvmT4ykvur4g8b5l6hI1G1hqOOm2Ak9qLGL0NJag5XSK3JmAx4bu6HzzLEI56kNbfNUIUJdgQ5yzKP3TZ4llsDl_qxGPrdeNl9umbOi4gZZ31dMH34iotl8_7pmRM01ucwr1qGQXRVs8hyLMbAUDJq-aCfGAd_g-9sp4Gu42xwodIliS_4IDE-k4m9M7uI1e5eEFNuWgJ-TusaNVCQgHoEBSMuYGRlRilxLK7RLHhZA4MC25rRU6U-Jr5uud7JiHYsvZImxA-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موتورسیکلت بنلی TNT15
✅
در کلاس شهری
✅
انجین بازطراحی‌شده برای یک سواری راحت
⭕
5 درصد تخفیف
⭕
اقساط 24 ماهه
جهت مشاهده قیمت نقد و اقساط روی لینک زیر کلیک نمائید
👇
https://l.nikrun.com/ei1
🏍️</div>
<div class="tg-footer">👁️ 2.12K · <a href="https://t.me/akhbarefori/653674" target="_blank">📅 20:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653673">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
هنوز بر سر موضوع هسته‌ای، پول‌های بلوکه و کنترل ایران بر تنگه هرمز اختلافات جدی پابرجاست که اگر حل نشود مذاکره انجام نمی‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 2.56K · <a href="https://t.me/akhbarefori/653673" target="_blank">📅 20:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653672">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
تناقض‌های آمریکایی به روایت سی‌بی‌اس: دولت ترامپ علی‌رغم تلاش‌های دیپلماتیک مداوم، در حال آماده شدن برای حملات نظامی جدید علیه ایران بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/akhbarefori/653672" target="_blank">📅 19:55 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653671">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
ترامپ به سی‌بی‌اس گفت «پیش‌نویسی» از یک توافق با ایران وجود دارد که قبلاً آن را بررسی کرده، اما از گفتن این که آیا آن را تأیید کرده یا نه خودداری کرد و گفت: «نمی‌توانم قبل از این که به آنها بگویم، به شما (رسانه‌ها) بگویم» و اضافه کرد که مذاکرات «بسیار نزدیک‌تر» می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/akhbarefori/653671" target="_blank">📅 19:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653670">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
جلسه وبیناری مجلس با حضور وزیر بهداشت برای بررسی مشکلات درمان و دارو برگزار می‌شود
🔹
گودرزی سخنگوی هیأت رئیسه مجلس: نشست وبیناری مجلس برای بررسی مسائل حوزه درمان و دارو فردا (یکشنبه ۳ خرداد) با حضور وزیر بهداشت برگزار می‌شود.
🔹
گرانی‌های اخیر در حوزه دارو و مشکلات درمانی مردم، محور اصلی این نشست خواهد بود و نمایندگان مجلس به همراه وزیر بهداشت به بررسی راهکارهای رفع این چالش‌ها می‌پردازند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/akhbarefori/653670" target="_blank">📅 19:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653669">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sCU1HsIkojEtyrs4fOweeIiY7Qx2-gjgxKIJSukedcXs7-3pg2B5PfmQEDjDvnGSL1N4kZYYkB5Fymg7Kw8LmwyqkCbN-h-L-WkfRtbjyUlVPNsVvsaKC7iLi5rvMq9vNkQD2hNZhZEDzIMM63b8ve0w3_ZWlZtSmKxhoONTlOWtnD3Pqd_XdNqd2T7PC7uHxswZGkHQxzdwTRxUnWPFzpgDI3239Kge6YL-uooN1zGbunwm3m5F8-PK5IRNzraFDI-Xgmsq6UMEOYjYwAweYIs2QaD8XcHEawB_30kptAJ_ZmmLlqbvtnLx81uv7QYbdWGsrihWUr8lu8Hb3HFGMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلند شدن ستون دود در پایگاه نظامی صهیونیست‌ها
🔹
رسانه‌های صهیونیستی از وقوع آتش‌سوزی در یکی از پایگاه‌های نظامی ارتش این رژیم در منطقه الجلیل غربی خبر دادند.
🔹
بر اساس گزارش‌ها، دود غلیظی از داخل این پایگاه نظامی به دلیل اصابت پهپاد حزب‌الله مشاهده شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/akhbarefori/653669" target="_blank">📅 19:26 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653668">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
ترامپ: تنها توافقی را قبول خواهم کرد که سرنوشت اورانیوم غنی شده در ایران را مشخص کند
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/akhbarefori/653668" target="_blank">📅 19:16 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653667">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d9a4dd220.mp4?token=D9C4GW3vanaP5opkuEwWVZ_nFr2SMg19xtl5hBFYAdeGfI8e41g0ukff6fl1OEmeC-HNAYPGJPQ5P2z0MiGquqX9-8JEqXEZdPSpzIJ-ryK8KIL-Zck-OJli--V7Wmxx6f6clpoXuZOynQtRmxrPh1R6QpPlIl7zPEg3DFqSERiykxDR7mpMosjkmB0M2tkC9C46fQ0QzHTqBXM2slbZSNCYHAdszoj_0v-hYgxNt1Hieu9w5OUzeKKR2grAARyqbek3_g81Mj-xkVCGmyPl0jYffoPy0qB686wJs_srUXxK--1Qhj2abRfRb7BijADxEYSNUHqKmjcHG8wP5TlV-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d9a4dd220.mp4?token=D9C4GW3vanaP5opkuEwWVZ_nFr2SMg19xtl5hBFYAdeGfI8e41g0ukff6fl1OEmeC-HNAYPGJPQ5P2z0MiGquqX9-8JEqXEZdPSpzIJ-ryK8KIL-Zck-OJli--V7Wmxx6f6clpoXuZOynQtRmxrPh1R6QpPlIl7zPEg3DFqSERiykxDR7mpMosjkmB0M2tkC9C46fQ0QzHTqBXM2slbZSNCYHAdszoj_0v-hYgxNt1Hieu9w5OUzeKKR2grAARyqbek3_g81Mj-xkVCGmyPl0jYffoPy0qB686wJs_srUXxK--1Qhj2abRfRb7BijADxEYSNUHqKmjcHG8wP5TlV-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقی‌پور، نماینده مجلس: شبکۀ حیاتی کابل‌های فیبر نوری جهان از تنگۀ هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/akhbarefori/653667" target="_blank">📅 19:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653666">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
فوری| ترامپ به اَکسیوس گفت که شانس «۵۰-۵۰» برای این موضوع وجود دارد که یا با ایران به توافق برسد یا جنگ را از سر بگیرد
🔹
او گفت: «یا چنان محکم‌تر از همیشه به آنها حمله نظامی می کنم که تا حالا مثل آن را ندیده‌اند، یا توافقی خوب را امضا می‌کنیم.»
🔹
ترامپ روز شنبه با استیو ویتکاف و جرد کوشنر دیدار می‌کند تا آخرین پیشنهاد ایران را بررسی کند و انتظار می‌رود تا یکشنبه تصمیم‌گیری شود.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/akhbarefori/653666" target="_blank">📅 19:06 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653665">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ILzQKENc4VxuQ8RrDDE790LptgoehVbFqXC3ldOwu9f_t1GkUnyFnVzX1bAEfuSHOMd-0gmOJDFvFyy-iQONra8aycmi1mhQKxqscLtC-qct_HME2wZpUxKXkjI9ydaGOJz5wzCxL8n5i9QOsO2GylSpoCnab2-wWQRhy4R89JOuJnS1SefUL5g-994KOUwLdOvJLUU5-vQzBGJrQz9HuKaN9moYrs3EdvaYTcoXlc2LmIu8adkpuDX9itD7vee4OQM4oroB_d2QjoO2I5HPTk-tibuSK3ErcUU99zMa_7DdTeYOexqQouaLlIXI3iB3x0ApfIWAHEFSw7i86_j5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفتگوهای تلفنی وزیر امور خارجه جمهوری اسلامی ایران با همتایان قطری و مصری
🔹
سید عباس عراقچی وزیر امور خارجه جمهوری اسلامی ایران عصر امروز شنبه در تماس‌های تلفنی جداگانه با شیخ محمد بن عبدالرحمن آل ثانی وزیر امور خارجه قطر و بدر عبدالعاطی وزیر امور خارجه مصر، درباره موضوعات روند آخرین تلاش ها و ابتکارات دیپلماتیک برای جلوگیری از تشدید تنش و خاتمه دائمی جنگ تحمیلی امریکا و رژیم صهیونیستی علی ایران گفتگو و تبادل نظر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/akhbarefori/653665" target="_blank">📅 19:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653664">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFYImi93wRYahFi-u3xodruTgXJfSbR2FDeRwL4moOO7SU2mqH8fZ3rMOy0UT-NYIvbyytedzuKQgNITKslOeObLUypZBdBiRBhS-Eu5RQNfF-AmEA4L-G-nRhdu4hDbQYWC_v4G1TnfZlz35clTcsQ6kdzPTi4sD7-uXkamv53D2SgDhZvQcG9aFwdQBb3cUNrrNpgA-U7JdYEHjkD2-vLQsQucADqRZtdxF9Py2br5utluz2mqJ97eSGpz_a9Uw79JsttCpZUJbQkDPL1OsarUgmSZN925D1OpKWpyDIN6n8srDuIPDgVYqRDE191g9zWvNaLmWnKSN-hqvazY9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: تکبر اسرائیل در حال تبدیل شدن به مدرکی علیه خودش است
🔹
ویدئوی بن‌گویر (وزیر امنیت اسرائیل) از آزار و اذیت فعالان کشتی‌های امدادی [کاروان صمود]، نشان‌دهنده حکومتی است که آن‌قدر به مصونیت از مجازات عادت کرده که حتی ظلمش علیه غربی‌ها را هم مستند می‌کند.
🔹
در این تصاویر، بن‌گویر در حال تمسخر فعالان حامی فلسطین است که به اجبار با دست‌های بسته روی زمین زانو زده اند و پیشانی خود را به کف اتاق چسبانده‌اند؛ رویکردی که پیش از این نیز در گزارش‌های متعدد درباره شکنجه و آزار جنسی فلسطینیان مستند شده بود.
🔹
انتشار عامدانه این تصاویر نشان‌دهنده اطمینان کامل مقامات اسرائیل از عدم مواجهه با هرگونه مجازات یا پیگرد قانونی است.
🔹
با این حال پس از انتشار این ویدئو، موجی از محکومیت‌های بین‌المللی علیه این اقدام شکل گرفت که نشان می‌دهد افکار عمومی جهان به‌شدت علیه تل‌آویو تغییر کرده و حمایت بی‌قیدوشرط از آن به یک بارِ سیاسی سنگین در غرب تبدیل شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/akhbarefori/653664" target="_blank">📅 19:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653660">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
اسلام‌آباد تلاش دارد دور دوم مذاکرات مستقیم بین تهران و واشنگتن را محقق کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/akhbarefori/653660" target="_blank">📅 18:28 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653659">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
فعال اصلاح‌طلب: اعتراف می‌کنم در نقد به دکترین دفاعی رهبر شهید اشتباه کردیم
🔹
علی باقری، دبیرکل حزب عهد ایران در گفت‌وگو با: رهبر شهید، معمار بازسازی قدرت ایران در جهان بود.
🔹
عملکرد ایران در جنگ‌های اخیر و مقابله با قدرت‌های بزرگ نظامی، نتیجه دکترین دفاعی‌ای بود که رهبر شهید طی سه دهه طراحی و تثبیت کردند؛ دکترینی که امروز قدرت نظامی ایران را به واقعیتی غیرقابل انکار تبدیل کرده است.
🔹
مهم‌ترین میراث ۳۷ سال رهبری ایشان، ساختن «ایران قدرتمند» است؛ کشوری که توان ایستادگی و مقابله با دشمنان خود را دارد.
🔹
این دکترین سال‌ها از داخل و خارج مورد نقد بود و ما در جریان اصلاحات هم به آن انتقاد داشتیم؛ اما جنگ ۴۰ روزه و پیش از آن جنگ ۱۲ روزه نشان داد این طراحی دقیق، هدفمند و کاملاً درست بوده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/akhbarefori/653659" target="_blank">📅 18:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653658">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfmn1VvKIUnpd8MCuS3tjuZ7NN4OMrwpW-9n95zR1WTPkpTmunYE6NSvzMAn88HqKHwp559cwjqGBgvownkEFppg6DN91eCJFTUTAofkP-DvZZ2N1BHsn4rIhG9uGm4Z1iCkwYaWEIAlD1Eo5I_mHcVPqvZcR8SrwNP1qaaZ2rqwWk-0EOnvzDynbkYwoMZaZUymmoYcrgodpwlz-PEGk2VJnv3fYKvTPq_uy1yANcTSHNXi_aVSIt4QOkW9WfnCehogSGkItwTa8iLBIEYxXrvp4IupT79204BRKgOMfU8G66W37WIaQO4LPkVROYeC0o7E4POtVdMPoYshY4rx0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حیرت کاخ سفید از «اشیاء مرموز» در تنگه هرمز / این سلاح مرموز ایرانی بدجور آمریکا را ترسانده است
🔹
بررسی تصاویر ویدئویی منتشره از سوی کاخ سفید نشان می دهد که اشیاء ناشناس همان «قایق های تندرو ایران» هستند که در آب های خلیج فارس در حرکتند. این قایق ها با تغییر کاربری و موتور، دارای سرعتی بالا (حتی تا 200 کیلومتر در ساعت) شده اند و به همین دلیل، تصاویر ماهواره ای آمریکا نتوانسته پی به حقیقت آنها ببرد و گمان برده آنها اشیاء پرنده ناشناس یا حتی یوفو هستند.
دراین‌باره بیشتر بخوانید و ببینید
👇
khabarfoori.com/fa/tiny/news-3217248</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/akhbarefori/653658" target="_blank">📅 18:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653657">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/854eb6914b.mp4?token=EDv3cnJnPFAgDeXQfUDl-1ZVqj1f3slsyq8UBr8-RutuoAMrzUGgwuAOUXBOcZ2BUATIOax6fMJuub8FkCwwCNMQPwcBCiQow7vULs2NX7P5f0bu06YGdIfsSj3JDhy_lgbxz3GU8OL5UmEyMDWGPpQ7z342B1C_eEpg3yXzr_AywTNcr5nYLG1koIaMU5RPlu1Exbu6ttcM5obZmb8B4--7Sf4IxRBUp3gzrpwqd21LtiZEzCuyzyUfr_473vRGgwGAo_rprTKXzdQHnGriaLgAH6vJ_Nw0zd_dkZzaGxe2xz4lma_AX3D_m0bKkwIpKXDCWhqayVxlPUf6lr2EL7apPNcE029pWHXI-cKurn07UrA4m0HG2KGIuFNr9pkIXLkLC5Yg9KzQokXPUZv1RJNolpPT3SLtD76t8wVrXMIB_LfVWsI0IFIQ_Taq9IMw-NI2qWl4iEIbt5husxqVxQ-Yw2Y3IoG2oKiiJbqypjK80bteKyCR1Eegs4ue92WnfngVB3IYdfp5IGLpResWOE8ZbC7fZfekwTxz_dRzDOSrnaOanAoAb6XdDccpaiFtYiliwIfVCeFlWuHHGKcrz4cqQXtGsVTzn1uSAcmMbHZGB45bQxRMqAL_lYY_FZJtFWqiubFPBls3p_IsQ67wmB1JGT8GcchJEKzAtgKFVc8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/854eb6914b.mp4?token=EDv3cnJnPFAgDeXQfUDl-1ZVqj1f3slsyq8UBr8-RutuoAMrzUGgwuAOUXBOcZ2BUATIOax6fMJuub8FkCwwCNMQPwcBCiQow7vULs2NX7P5f0bu06YGdIfsSj3JDhy_lgbxz3GU8OL5UmEyMDWGPpQ7z342B1C_eEpg3yXzr_AywTNcr5nYLG1koIaMU5RPlu1Exbu6ttcM5obZmb8B4--7Sf4IxRBUp3gzrpwqd21LtiZEzCuyzyUfr_473vRGgwGAo_rprTKXzdQHnGriaLgAH6vJ_Nw0zd_dkZzaGxe2xz4lma_AX3D_m0bKkwIpKXDCWhqayVxlPUf6lr2EL7apPNcE029pWHXI-cKurn07UrA4m0HG2KGIuFNr9pkIXLkLC5Yg9KzQokXPUZv1RJNolpPT3SLtD76t8wVrXMIB_LfVWsI0IFIQ_Taq9IMw-NI2qWl4iEIbt5husxqVxQ-Yw2Y3IoG2oKiiJbqypjK80bteKyCR1Eegs4ue92WnfngVB3IYdfp5IGLpResWOE8ZbC7fZfekwTxz_dRzDOSrnaOanAoAb6XdDccpaiFtYiliwIfVCeFlWuHHGKcrz4cqQXtGsVTzn1uSAcmMbHZGB45bQxRMqAL_lYY_FZJtFWqiubFPBls3p_IsQ67wmB1JGT8GcchJEKzAtgKFVc8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مدیر شبکه افق: برای اولین بار اعلام می‌کنم که حضرت آقا تجمعات را از تلویزیون دنبال می‌کنند و از جمعیت زیاد تجمعات خوشحال هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/akhbarefori/653657" target="_blank">📅 18:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653656">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88702db038.mp4?token=h7JO0UveaQt4zGpL61GVsPLWZQvKPiuJOGESfvibbNUv952Kljn22Lqe83m8f7rk4CewFuDIm8ECwzTq9baiFkhx5jN7GxTDZFb0EDPF4_JjbPXYKbzY95fjyUBwtENsR4vQyyCff59Ir2GycEscQUwoLZhZr_ptrUbBwkD74lfmZ19yfIKGYuO8m4QI26V-YgdZcOZ-Lhy9lFHg8VvLe1DfK5DQzuaTKN3ca6iFFxK_0Z697Dw2glhOY2_1GH7KX0ZUqRXnW_SLvw_eSoRthjU2xuAFVn5tYl3F-p_jldhe7mQMFNkatql4MdCU258pesE4Y8gSjZbbdoKzR2ZdCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88702db038.mp4?token=h7JO0UveaQt4zGpL61GVsPLWZQvKPiuJOGESfvibbNUv952Kljn22Lqe83m8f7rk4CewFuDIm8ECwzTq9baiFkhx5jN7GxTDZFb0EDPF4_JjbPXYKbzY95fjyUBwtENsR4vQyyCff59Ir2GycEscQUwoLZhZr_ptrUbBwkD74lfmZ19yfIKGYuO8m4QI26V-YgdZcOZ-Lhy9lFHg8VvLe1DfK5DQzuaTKN3ca6iFFxK_0Z697Dw2glhOY2_1GH7KX0ZUqRXnW_SLvw_eSoRthjU2xuAFVn5tYl3F-p_jldhe7mQMFNkatql4MdCU258pesE4Y8gSjZbbdoKzR2ZdCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تا پایان شهریور واردات کالاهای اساسی توسط همه اشخاص کاملاً آزاد است
🔹
وزیر کشاورزی در نشست دکتر پزشکیان با استانداران: حداقل تا پایان شهریور ماه به دلیل شرایطی که در آن قرار داریم، واردات کالاهای اساسی توسط همه اشخاص حقیقی و حقوقی و بدون هیچ محدودیتی از همه مبادی کشور کاملاً آزاد است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/akhbarefori/653656" target="_blank">📅 18:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653655">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pOFDBD8LgJ-CxVJy9e3EIEZ6h_GTIUivfIK-NHLM3xrvrsAj37r5x3qhRcbTDIYEjeKuVpkpUAN-8MR6hCPuIQ-p7-q9AhPxRwcd9K1QeXwyAR4jp68QENKqsO7dBublJuF78MTbY7w4i8LJXblAfA9N7kBV8h4ip8vAHgh42rzdUX-gGeXjfqjak4oBNieGRKhgXds62j8ZmdLt0oXFrAg2XI7L8esb8YcDCXi2526Cgpk7sQLFbaxBqaI2tHf4zjOotjKPQeduubIGBvDMSNz2b9U0NYzcRw0OfM9EmHDbix44KW8XnkUJeXI1VVLQhRV4VkSI1uSQc35QhtwpBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فائو: تنگهٔ هرمز بسته بماند، جهان با یک بحران غذایی مواجه خواهد شد
🔹
سازمان کشاورزی ملل متحد: ادامه بسته‌ماندن تنگهٔ هرمز آغاز یک شوک ساختاری در نظام غذایی جهان است و آثار این شوک طی بازهٔ زمانی ۶ تا ۱۲ ماه آینده ظاهر خواهد شد، به‌طوری‌که یک خانواده ۴ نفره در اروپا برای خرید یک قرص نان باید پول یک وعدهٔ غذا را بدهد.
🔹
افزایش قیمت انرژی، قیمت گندم و برنج را نیز بالا برده است.
🔹
کارشناسان پیش‌بینی می‌کنند در ۱۲ ماه آینده قیمت نان در جهان ۳۵ تا ۴۵ درصد افزایش یابد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/akhbarefori/653655" target="_blank">📅 18:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653654">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">♦️
ادعای العربیه: تهران در ازای پرداخت غرامت از سوی آمریکا به ایران، پیشنهاد بازگشایی تنگه هرمز را ارائه کرده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/akhbarefori/653654" target="_blank">📅 17:49 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653652">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
فعال شدن آژیرهای هشدار در شمال اراضی اشغالی
🔹
ارتش رژیم صهیونیستی اعلام کرد که در پی نفوذ پهپادی متخاصم، آژیرهای هشدار در شهرک شلومی واقع در شمال اراضی اشغالی به صدا درآمده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.43K · <a href="https://t.me/akhbarefori/653652" target="_blank">📅 17:43 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653651">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
مصوبه جدید دولت برای حمایت از آسیب‌دیدگان بندر شهید رجایی/ رشد ۷۵ درصدی اعطای وام ازدواج
🔹
سخنگوی دولت: موضوعی که در دولت به تصویب رسید؛ تضمین‌های مالی تودیع‌شده برای فعالان اقتصادی آسیب‌دیده از حادثه بندر شهید رجایی بود که تا پایان مرداد ۱۴۰۵ با آن موافقت شد.
🔹
سال گذشته میزان اعطای تسهیلات قرض‌الحسنه ازدواج ۲۰۰ هزار میلیارد تومان بود که امسال با رشد ۷۵ درصدی به ۳۵۰ هزار میلیارد تومان رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/akhbarefori/653651" target="_blank">📅 17:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653650">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
ادعای روبیو: پیشرفت‌هایی در قبال پرونده ایران حاصل شده است
🔹
مارکو روبیو، وزیر خارجه آمریکا:
🔹
تنگه هرمز باید باز شود؛ ایران نباید سلاح هسته ای داشته باشد؛
🔹
ایران باید ذخایر اورانیوم غنی شده خود را تحویل دهد؛ معضل غنی‌سازی ایران باید در مذاکرات در نظر گرفته شود؛
🔹
خواسته‌های رئیس جمهور به هر شکلی باید محقق شود؛ اولویت ما مسیر دیپلماتیک است؛ امیدواریم که از طریق دیپلماسی حل شود؛
🔹
احتمال دارد که امروز، فردا یا طی چند روز آینده مطالب قابل‌توجهی برای گفتن داشته باشیم.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/akhbarefori/653650" target="_blank">📅 17:25 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653649">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6590e81384.mp4?token=OH59cV-ijUeq-v1VQxaeIVFhujerbFmphr5ByOhmhpqy8A-OLYFDmMOC_3egKQuYw89ylLRkU8KwUhUL6TpBPJCJxobd0qlXZFiKGfEL7m-scAd0p0DtnXOiS1kC6KqMLV61qxZu1eNlf6p4QoZH-pNnO8aWACDR6NwBNoiA7ijnFJZQhAU-gocAlE6zuN_MOW8DnSKvWD8cWPY0THzk0_eJeZET1y-SZp8OfcB3rLlm_fT3BxN8cS86EABUk5C4NfJEfeBLufpmTL_tf0ckzgrn_orzZ1uENJNGuSNLJMa7UXkiS_4k7NS7dVKotvg2ePoeNpuE814c8Guf_jH5vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6590e81384.mp4?token=OH59cV-ijUeq-v1VQxaeIVFhujerbFmphr5ByOhmhpqy8A-OLYFDmMOC_3egKQuYw89ylLRkU8KwUhUL6TpBPJCJxobd0qlXZFiKGfEL7m-scAd0p0DtnXOiS1kC6KqMLV61qxZu1eNlf6p4QoZH-pNnO8aWACDR6NwBNoiA7ijnFJZQhAU-gocAlE6zuN_MOW8DnSKvWD8cWPY0THzk0_eJeZET1y-SZp8OfcB3rLlm_fT3BxN8cS86EABUk5C4NfJEfeBLufpmTL_tf0ckzgrn_orzZ1uENJNGuSNLJMa7UXkiS_4k7NS7dVKotvg2ePoeNpuE814c8Guf_jH5vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پاسخ موشکی رئیس کمیسیون امنیت ملی به توئیت تهدید آمیز دستیار ترامپ
🔹
موشک خرمشهر در جواب ویدئوی بمب افکن B۲
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/akhbarefori/653649" target="_blank">📅 17:18 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653648">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hCvybRcWcOlPup3NY1ABTyRf2bpVoQKxXC1w_PsGXyTJvxRV_WnURVpPgeCwsgJFQ4oMEsLij1z9KKcEDbejJVBG3RU9NJl20SBgVNALa3Vw8U4bsjp8-Q9I5C4Ed7HvikzBvXHhEWtfu5jk84w5eWSo42GW5NffxNAWZfVFBeCm0iKMsc2FOIz8P_fQQUKhndHvtQ1_IVxqrSdtDOrm2wuwV1fgXj8CyQ5cT2UCDo2ToIMQb_Uj8bqazJlfKbyWzaK-JVsbJ-rurcd2QRVGI7colygZFkzy7gY91CcfDNox8FRmc2ovK011NKPmPg5Y52GlGYX6mf29-noDjb-jYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پست جدید ترامپ متوهم: ایالات متحده خاورمیانه؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/akhbarefori/653648" target="_blank">📅 17:07 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653647">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
بقائی: ایران بر خاتمه جنگ در تمام جبهه‌ها از جمله لبنان تاکید دارد
🔹
موضوع هسته‌ای در این مرحله در مورد جزئیاتش صحبت نمی‌کنیم.
🔹
می‌دانیم که موضوع هسته‌ای بهانه دو جنگ تجاوز علیه ایران بوده‌است.
🔹
ما این تجربه را داریم که دو بار در طول مذاکرات هسته‌ای مورد تجاوز قرار گرفتیم.
🔹
مسئولانه و خردمندانه تصمیم گرفتیم که موضوع مذاکرات را بر خاتمه جنگ در تمام جبهه‌ها از جمله لبنان قرار بدهیم.
🔹
اینکه در ۳۰ روز یا ۶۰ روز وارد موضوع هسته‌ای شویم مربوط به بعد از این مرحله است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/akhbarefori/653647" target="_blank">📅 16:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653646">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پیام وزیر امور خارجه به دبیرکل حزب الله: ایران دست از حمایت حزب‌الله نخواهد کشید
🔹
سید عباس عراقچی، وزیر خارجه در پیامی به شیخ نعیم قاسم، دبیرکل حزب‌الله تأکید کرد که جمهوری اسلامی تا آخرین لحظه از حمایت جنبش‌های مطالبه‌گر حق و آزادی دست نخواهد کشید و حزب‌الله مقاوم و پیروز در رأس این جنبش‌هاست.
🔹
عراقچی افزود که از همان ابتدا که برخی کشورهای منطقه برای کاهش تنش میان ایران و آمریکا وارد میانجیگری شدند، ایران پیوند آتش‌بس لبنان با هر توافقی را به عنوان شرط مطرح کرد و این اصل تاکنون به عنوان یک مبدأ تردیدناپذیر باقی مانده و در زمره مطالبات حقه دولت و ملت ایران است و چنین خواهد ماند.
🔹
وزیر خارجه ایران تصریح کرد که در آخرین پیشنهاد ارائه‌شده از سوی جمهوری اسلامی از طریق میانجی پاکستانی برای توقف دائمی و پایدار جنگ، مجدداً بر گنجاندن لبنان در آتش‌بس تأکید شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/653646" target="_blank">📅 16:52 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653645">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FkhzxVUWPszfhmu0hr2yKhE1ZwPGTNAqAhR2uBheFWVBIyRlqWYr_nChUxfzWIf72SqP_IsklxJ84X8qMvsk9FzS2oHAl2Cf1BH1eQd_IAqFdaipp9zyO8AGbbECjOS2FFjHq1c2afL_wzcpxemAxKt6hM3Ite2kUeJ_sAieXd-UilUgxTxSvhFpw2jKGII8_UqA2f2s-cy5_rZsSMefMOu1AEkfFvICF9YNqALFHgN1fAaeH0l02zxs2wNcuFoFkYIVZsWUlvPn5f332FyHJiW7jCsh7wROw28TDz3T2xTa1cAMStAgJGFc6tprVJEOP0MaUycUEBDRwQTvms5Xig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پول دولت به گندم‌کاران نرسید
🔹
رئیس بنیاد ملی گندم‌کاران:‌ دولت هنوز پول گندم‌کاران را که هفتۀ گذشته قول داده بود پرداخت نکرده. این در حالی است که آنها برای کشت بعدی نیاز به نقدینگی دارند.
🔹
سه‌شنبۀ هفتۀ گذشته جلسۀ تعیین‌تکلیف مطالبات گندم‌کاران به ریاست معاون اول رئیس‌جمهور و با حضور وزیر کشاورزی و رئیس سازمان برنامه تشکیل و ۸۳ هزار میلیارد تومان بودجه تامین اعتبار شد تا ۲ روز دیگر پرداخت شود.
🔹
در جلسۀ پنجشنبۀ هفتۀ گذشته سازمان برنامه به دستور رئیس‌جمهور مکلف شده پول گندم‌کاران را سریعتر پرداخت کند با این حال به گفتۀ کشاورزان پولی به حساب آنها واریز نشده.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/akhbarefori/653645" target="_blank">📅 16:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653642">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8aK1havUQFgpU3PMO3yv_gaTUXuJVj9YNqod_WZlICd3vSlf8qOcRglr8aPhuaB1WPeGirKlMYasnK4UEyXJNdNdmsR4stYFpVC3-vjeiLeibPVa9z0XMro3pYxLpD7mRUfrBoICm-i3LeH9iA3WyKC8jj9cfoDvhtZn9n_Lgl2IZ_dPykcIIVfTnONzgUdP1MUIG9taF9dacPu2eOLnH2V7ee2BgE68rE2EzNB3jExkBk1O1NeDHvMYk3w1PnXUEjbNGYlWVj8-XyLn8nEKXhpZu-ZeTfQfX3wGvXx8Du_65D-nliI6GoxG3ePAfSzaFDemcNf13QUldTtmbFpxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MRr58xC8qAWaDL29QSwOnqDKUiRjJngUJ4mZD2gEJw9kjR7eOOXF7xvkbQb9D3BGuFDBughbt-brijjFro7_6l68qcZaVnEXui4S1ToWxaVXG2ZrafSGrNHYIyxzfSeYDc7XRc0Tl9df0DgcaxDHK5NponjrLWendvOutJPzYHPJ9T-Gxk940LQKYaWgxnJtVJ1Cn3vzxtE7zeVHWERT8bOthkZBwXVoWw37RLLLRlY-sR-3KaUkAn5lMJseAvyfWgdl8BaZtjTgEOx-gSmN0ABOkppgkH5lyBV8w4jvIv7OnFJli0aNIFI6d02yCOTJgmkkZL0ygI5l8tokr50kMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پزشکیان: سابقۀ مذاکره با آمریکایی‌ها حکم می‌کند نهایت دقت را به عمل آوریم
🔹
رئیس‌جمهور در دیدار فرمانده ارتش پاکستان: ما صرفا به‌دنبال احقاق حقوق حقه و قانونی ملت خود هستیم، اما سابقۀ و تجربۀ مذاکره با آمریکایی‌ها به ما حکم می‌کند که نهایت دقت را به عمل آوریم.
🔹
جنگ هیچ‌گاه برای هیچ کسی منفعتی به همراه نداشته، آمریکا در این منازعه پیروز نخواهد بود و این کشورهای منطقه و جهان هستند که متحمل خسارات جدی خواهند شد و رژیم صهیونیستی تنها طرفی است که به‌دنبال تامین منافع خود در منطقه از قبال جنگ است.
🔹
با توجه به بی‌اعتمادی مردم کشورمان به آمریکا به‌دلیل نقض عهد مکرر، حملات در حین مذاکرات و ترور مسئولان، جمهوری اسلامی با اتکا به روابط برادرانه با کشورهای دوست از جمله پاکستان، در مسیر مذاکره قرار گرفته، اما هدف اصلی ما صرفا تامین منافع ملت ایران با راهکارهای مقتضی و مناسب است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/akhbarefori/653642" target="_blank">📅 16:30 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653641">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aNsgkIDf0oW6rTS8_NssGueBOygLnlFpLTCdVJi2GxDvvOBY8Imxyu53HR6aUpEwexAfeWXtSavV98G-9V0dyHZuTIAb88MT49YKNBpTAuBq98vWIVdiKEYXWjyxdetuICUIkiw-qYCbWemwfljaJrn2SBjPHIkTPE93cdJDtHNDygQ8SGKpWZdLV7eC5HowyER8pjxhd1GSrH767OlYfjtut8Ij8gfD7s_JOXXER8EfjdFw1Dp3ngPLMkJIUftDpoEfYWUGoeGLL7knL9k1gpnNa8dIupfyY3QxcyazB0Bni9Pc33jvKwtsEU1iIrXKwSBEhRD7JYfb-Qf7DSMLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
لاوروف: هم‌اکنون جنگ در سراسر اوراسیا جریان دارد
🔹
وزیر امور خارجه روسیه: در منطقه اوراسیا، این جنگ هم‌اکنون به‌ صورت گسترده در جریان است، پس از تجاوزی که کشورهای غرب با استفاده از اوکراین علیه روسیه تدارک دیدند و تلاشی دیگر برای تضعیف کشور ما و حذف آن از میان بازیگران کلیدی جهان، شاهد درگیری نظامی در خلیج فارس و تنگه هرمز هستیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/akhbarefori/653641" target="_blank">📅 16:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653640">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
ارتش: آمادۀ مقابله قاطع با هرگونه تعدی دشمنان هستیم
🔹
بیانیۀ ارتش به‌مناسبت سالروز آزادسازی خرمشهر: فتح خرمشهر، ثمره ایمان راسخ، مجاهدت خالصانه و ایثار بی‌بدیل فرزندان این مرز و بوم بود که با تبعیت از رهبری الهی حضرت امام خمینی (ره) و با اتکا به قدرت لایزال الهی، توانستند معادلات دشمن را برهم زده و مقاومت و ایستادگی ملت ایران را به رخ جهانیان کشند.
🔹
ملت شریف و نیروهای مسلح ایران، به‌ویژه ارتش غیور و سرافراز ایران، امروز نیز در پرتو همان روحیۀ جهادی و با بهره‌گیری از تجارب گران‌سنگ دفاع مقدس و جنگ‌های تحمیلی و ناجوانمردانۀ ۱۲ و ۴۰ روزه، در راستای تدابیر رهبر انقلاب برای مقابله با دشمنان، آماده و هوشیار است.
🔹
ارتش با تمسک به آرمان‌های رهبران کبیر و شهید و تحت فرامین حکیمانه رهبر معظم انقلاب، با عزمی راسخ و اراده‌ای خلل‌ناپذیر، خود را برای مقابله قاطع و همه‌جانبه با هرگونه تهدید و تجاوز دشمنان آماده نموده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/653640" target="_blank">📅 16:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653639">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
امیر سیاری: آماده خلق بیت‌المقدس‌های دیگر هستیم
🔹
معاون هماهنگ‌کننده ارتش به مناسبت سالروز فتح خرمشهر: ارتش جمهوری اسلامی ایران و سایر نیروهای مسلح گوش به فرمان رهبری و گوش به زنگ اشارات این فرمانده مقتدر هستیم.
🔹
در پاسداری از تمامیت ارضی و استقلال کشور، مهیای خلق بیت‌المقدس‌هایی دیگر در برابر هر فتنه و جنگ تحمیلی هستیم و این را دنیا بداند که هویت ما با ایثار و وطن‌پرستی گره خورده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/akhbarefori/653639" target="_blank">📅 16:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653638">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
لحظه حملات پهپادی حزب‌الله به مقر ارتش اشغالگر در بلندی «العجل»، پادگان آویویم، رامیم، راموت نفتالی و معالیم گولانی
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/akhbarefori/653638" target="_blank">📅 15:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653637">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
بن‌گویر از ورود به خاک فرانسه منع شد
🔹
وزیر امور خارجه فرانسه: «ایتمار بن‌گویر» وزیر امنیت داخلی اسرائیل از امروز از ورود به خاک ما منع شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/akhbarefori/653637" target="_blank">📅 15:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653636">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7WOwkT0cZC121CIq9eeSmti5r9eWUXZncoEZhEo3Prn-Xj6603fCQDf8tVr6PIKshJfOA1gsdtr6FiCEDjBymjizYPLlOFHLAG9PUWXeT9bF9m_TLKkQKB4mX0Se_J0cLytn3A0_MEcJVBCRnr1Uaywr7pX_W9W6obIb6CblR4oPcrGrYvYbPzeupc4D_cenbz0w4z1oT-Y-Uva-p3qNQvHJs_-OoDgHauEUpHc7XMXUqjH6LRb8y9HABI6yQTqnvhYKVVzbUJW6ybKfWim9WTJ4BkkF7cxTgw_nhBEfsTjrD6N48-NDqB0EhrxE8veFeK6i1bp2IdaSMNcBtkaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۲۴۰ کشتی در انتظار اجازهٔ ایران برای عبور از تنگهٔ هرمز
🔹
تصاویر ماهواره‌ای نشان می‌دهد که حدود ۲۴۰ کشتی در آب‌های خلیج فارس و در پشت خط مرزی که ایران آن را به‌عنوان منطقهٔ تحت کنترل خود در آب‌های خلیج فارس تعیین کرده است، جمع شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/akhbarefori/653636" target="_blank">📅 15:45 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653635">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uWaWvEJ-SfkrFN3gnFwZ4KxV1w3dXgrX33svLsNAJ_lpb48-ePm_83OnRqbMYfPsQ2h-yN1cD8quvg66YOBgnqoYPZQCC7a1bTal0w-piT8PycVx5Hz1P0WZ9X__WkLXDfEV3fjHXKRg81xu1XFwBvykhinij_Ym1J-BIURBgIPAs0NUhd99DidPpkSXtbn149DHCd-sqF7EtnOFq8V-wItNiKEt0i7AX48ReyP87MDzJcFY3YFYJS6AalA6HwAv6SvPR_5HM9pzl9NTu2uUzzC-6poYypo4DZ-EgSj-wobKCxPnN91V7iVOXf5SadDO3-turVxyj4peaVt3aS9NKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقلیم «جبل باشان» اسم رمز اسرائیل برای تجزیه جنوب سوریه
🔹
شیخ حکمت الهجری، یکی از رهبران دروزی‌های استان السویداء (جبل الدروز)، با پخش یک قایل ویدئویی بار دیگر بر طرح جدایی از سوریه و تشکیل یک اقلیم خودمختار تأکید کرد.
🔹
او همچون چندین اطلاعیه پیشین خود نام این منطقه را «جبل باشان» گذاشت، نامی عبری بر مبنای متون توراتی که ادعا می‌شود بخشی از منطقه «کنعان» بوده است. طبق متن تورات، « جبل باشان شامل حوران، جولان و اللجاه می‌شد که همگی از صخره‌ها و خاک‌های آتشفشانی تشکیل شده‌اند و خاک آن بسیار حاصلخیز و آب آن فراوان است. در آن گندم، جو، کنجد، ذرت، عدس و خلر کشت می‌شود».
🔹
نکته قابل توجه اینکه رژیم اسرائیل پس از سقوط بشار اسد دست به بمباران بی سابقه زیرساخت‌های نظامی سوریه زد و حدود ۸۰ درصد دارایی‌های نظامی این کشور را نابود کرد؛ نام آن عملیات نیز «پیکان باشان» نام داشت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/akhbarefori/653635" target="_blank">📅 15:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653634">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rs98Hjv0vHioMM2UrDPJZPz94bN6Mt4VH3o-2r4_MgAve0mPDOAC4YgSwCEv6jXOCseAb8NFAXb3CCjgBkOuD61JESWY-Gb2gLTY1_jf4dY-expl5hI0Z0ytETddHD73iVZH1OYMr08DnIp52V3JmZz9FuibwxYNxL1bR_5l6YaLFyxVgAO__VwT0ItYwsCnVd9XrLupJr6ZjNftkLCgjSp5GQ80quP9Gsvk6y5lrzT7yWrUKawumZAfcVX-6iIUwQLAqlViNhmAF9QseNRTWrPR7CBTbQFYGFGzqKylPeVMW_zb8AirqAkb8Y-4KxNCCTtrdFM-PC_oceL_YxmNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وام ودیعهٔ مسکن از اجاره‌بها جاماند
🔹
با وجود افزایش چشم‌گیر اجاره‌بها در کشور از ۵۰ تا ۷۰ درصد، دولت سقف وام ودیعهٔ مسکن را حدود ۳۳ درصد افزایش داده و خبر می‌رسد که سقف تسهیلات فعلاً تغییری نمی‌یابد.
🔹
امسال سقف وام ودیعه‌‌ مسکن در تهران ۳۶۵ میلیون، مراکز استان‌ها ۲۸۰ میلیون، سایر شهرها ۱۸۵ میلیون و روستاها ۷۵ میلیون تومان می‌باشد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/akhbarefori/653634" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653633">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIyTpl1CY3uAi5kLmOepeTmTIdcbAp_emRWqHsUJI6pLlvgqv9k_QqQfjlLHfCAs0ajRS3IxgpxLnNELb2zs_Tf2IN2bVJinj4SpT8HjQwfOitAP3qHkY3CWC84Cle5bAtHaKFaPc7blTi_sSdndiU5A_Mo6gdpMhUX87execD1m6z8A1uzie6v_kJan6fS4fsW5Q_ECRcQDwIrjs0MU6aEyc-XHXxDXWoNMrUNdLwdFk350vkh5V_eslpuY-efun1Vx0XaM_LfYZlTGtne_6EAFHtmtbFzDVhiGnjyG6be9FVMOdxqYbBAQWlAWTN-NyK_BsoGsDdRzODJq1nPv-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تکاپوی بیشتر پاکستان برای یک توافق؛ اختلافات پابرجاست
🔹
سفر فرمانده ارتش پاکستان عاصم منیر، گفتگوهای مربوط به توافق بین ایران و آمریکا را وارد فاز جدیدی کرده است، اما همچنان برخی اختلافات به قوت خود باقی است. تلاش‌های برخی دیگر از بازیگران منطقه‌ای از جمله مقامات قطری هم تا این لحظه، نتوانسته واشنگتن و تهران را به یک توافق برساند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/akhbarefori/653633" target="_blank">📅 15:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653632">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtHKcicpj-UEqZtJgfPcJnA40bI5bsI7xNnko5_vA6guiub8VrNa3ddJeoxUomAUqUudhXgyUBbdhY-MfrV3sC53gdtZw1K-oLtPU-KJPINtBzGP2qZYuMUjBAVo1V3JsW838ovW21aNBCHABGi3DLZteTUHaFgx87ySDTIoGnYiAZlCSFVIwc3hoFdxEKX3tNqaJtSRUzSNkfBpptBNZExsS7FldZU_hwbid0BFi4ppwNASIhEF725lmtqKgXk676c7XDxmbhtJFDHEO7w96OmwYWvtI5NOgaRi0-tEHD2qwBfgHo92iAM4zZp0bcVoZt8qTUb9MLy-QKznZhHRLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترور ایوانکا ترامپ توسط ایران | بازخوانی توطئه‌های ترور؛ تلاش واشنگتن و تل‌آویو برای جبران شکست‌های میدانی؟
🔹
همزمان با تشدید فشارهای سیاسی و نظامی بر محور مقاومت، در هفته‌های اخیر دو خبر امنیتی با محوریت «کشف نقشه ترور» توسط رسانه‌های غربی منتشر شده است که بسیاری آن را تلاشی برای برساختن «مشروعیت تهاجم» به ایران ارزیابی می‌کنند.
ترجمه گزارش دیلی‌میل را در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3217212</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/akhbarefori/653632" target="_blank">📅 15:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653631">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
ادعای خبرنگار الجزیره: یک شخصیت بسیار بلندپایه منطقه‌ای از ایران دیدار کرده است
🔹
یک چهره بسیار برجسته منطقه‌ای، بی‌سروصدا از تهران بازدید کرد تا آنچه را که بسیاری اکنون «شکاف‌های غیرقابل عبور» می‌نامند، پر کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/653631" target="_blank">📅 14:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653630">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
تماس تلفنی امیر قطر با ترامپ درباره کاهش تنش‌ها در منطقه
🔹
دیوان امیری قطر از تماس تلفنی امیر این کشور با ترامپ ،رئیس جمهور آمریکا خبر داد.
🔹
دیوان امیری قطر افزود که امیر این کشور درباره  تلاش‌ها برای تحکیم آتش‌بس و کاهش تنش‌ها در منطقه صحبت کرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/653630" target="_blank">📅 14:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653629">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/646a9bc335.mp4?token=OT9anw2BA8t1ii6wqJPR_LAv-Xc-2rDVMEaVefK8D7d8oTRp-GiJpGN5QTEgY55yJw6a3uLE7blD3iinv3QZy7ZW24EJ1TMastzz0Hyhqk-RWJCQD-qRuTCU_itVfGtF1V2jrjjexLJEqZRtJ7N0b2vthc_rNg5wCExEzxKOQyj72MwPeiLv3byRIlteKvDUmNpJrbAeqL5TVdmp4daOI12sr9zh09fGUx2yh5JDWVN8lPS-ZoJhYBnYkp12UjNAA0oSDzp_6Wu82NaVcK4rNtypIm7DYwPNMnNfsBOoGgJklGKSPf0VBjuAlLflSXve7dCuyTFPX0F9jBjx-isDvRB4nYIZCtHzqTBKIOK_k23O4WHmKwovINXGRe5i3hxckD-DrXD4F62rBwyN9rorHTgAq7zAglbRcP3KNKvtjGe7ziJ6jdUw698y_s4aQJaq1lRCaVzzmSI8Z_v_p7cY0LNeaIeByW0yNnp9xNCWCKrGtQ3w407a7efMvDP4x2RC4rH8xShgIwfU-4KG4jsx3Nxz47xUA0MSSWcGuE8IyKIuL8DWuWND9KSYK4K4BWsLXX-Fn6bsVDgghhX0VpBuu5Gpq_-ELBYN0rq5CYm7bSTJi602w6xISRX-KWDx4tIBFi0p2wlyExtHKBOI6A-u0OLJpsKgeDCXFT7orJI5kjc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/646a9bc335.mp4?token=OT9anw2BA8t1ii6wqJPR_LAv-Xc-2rDVMEaVefK8D7d8oTRp-GiJpGN5QTEgY55yJw6a3uLE7blD3iinv3QZy7ZW24EJ1TMastzz0Hyhqk-RWJCQD-qRuTCU_itVfGtF1V2jrjjexLJEqZRtJ7N0b2vthc_rNg5wCExEzxKOQyj72MwPeiLv3byRIlteKvDUmNpJrbAeqL5TVdmp4daOI12sr9zh09fGUx2yh5JDWVN8lPS-ZoJhYBnYkp12UjNAA0oSDzp_6Wu82NaVcK4rNtypIm7DYwPNMnNfsBOoGgJklGKSPf0VBjuAlLflSXve7dCuyTFPX0F9jBjx-isDvRB4nYIZCtHzqTBKIOK_k23O4WHmKwovINXGRe5i3hxckD-DrXD4F62rBwyN9rorHTgAq7zAglbRcP3KNKvtjGe7ziJ6jdUw698y_s4aQJaq1lRCaVzzmSI8Z_v_p7cY0LNeaIeByW0yNnp9xNCWCKrGtQ3w407a7efMvDP4x2RC4rH8xShgIwfU-4KG4jsx3Nxz47xUA0MSSWcGuE8IyKIuL8DWuWND9KSYK4K4BWsLXX-Fn6bsVDgghhX0VpBuu5Gpq_-ELBYN0rq5CYm7bSTJi602w6xISRX-KWDx4tIBFi0p2wlyExtHKBOI6A-u0OLJpsKgeDCXFT7orJI5kjc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واشنگتن پست در گزارشی ویدئویی به بررسی آسیب‌های وارد شده به پایگاه‌های آمریکایی در منطقه پرداخته است
🔹
در گزارش این رسانه آمده است:
🔹
۲۲۸ سازه یا تجهیزات در ۱۵ پایگاه نظامی آمریکا در خلیج [فارس] هدف قرار گرفتند.
🔹
میزان خسارت بسیار بیشتر از چیزی بود که اکثر مردم تصور می‌کردند.
🔹
برخی از این انفجارها واقعاً عظیم بودند.
🔹
این نخستین بار است که یک دشمن توانسته تقریباً در لحظه، تصاویر ماهواره‌ای از خسارتی که به ایالات متحده وارد می‌کند منتشر کند.
🔹
این موضوع از این جهت مهم است که ایرانی‌ها توانسته‌اند اطلاعات را در سطح جهانی کنترل یا تحت تأثیر قرار دهند و نشان دهند چقدر به پایگاه‌های آمریکایی ضربه می‌زنند
🔹
این جنگ احتمالاً طولانی‌تر از آنچه دولت تصور می‌کرد ادامه پیدا کرد و توانایی ایران برای حمله به پایگاه‌های آمریکا بیشتر از آن چیزی بود که قبلاً درک شده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/653629" target="_blank">📅 14:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653628">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZGlftL6WgzsrTvjJpZsxK33nhta29GWvCQBHnKltbzodbM2a321cZhUHHFnnkgGzt-PY7YXdd3zFH9VJ4HQ-d7-dFAk4oTvesUTr77V_eGVlwps8nbu8bT7ZfXDq31UJSq5mvE2l18wF3DNAg0DizeORRO-fdUVvW-3eBLUHYmr9lZCNmdljMWY5z0wVx2ktQIk2CIdPEhEwgMdqHYTFn8ozQqG8jV-xcfg9H_2ECxq5Ezvtrnof7EnHaFbstOSEOaNWkVjQY3V9VyTUvIo0DsxLAuU0iA4_9ZACNjmzu0PhktK4mUy0nr7bdHNI57ldN4ksS5CImKNNZeVCFpR9kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه تحلیلگران | هرمز؛ برتری ژئوپولیتیک بر تکنولوژی
🔹
از منظر ادبیات بازدارندگی در روابط بین‌الملل، هرمز ابزار «مجازات مستقیم» به معنای کلاسیک نیست؛ ابزار تولید ریسک سیستمیک است. ایران با حفظ این اهرم، آمریکا و اسرائیل را به این نتیجه می‌رساند که جنگ علیه ایران نمی‌تواند محدود، قابل مدیریت و بی‌هزینه برای نظام جهانی باقی بماند.
🔹
آمریکا برای اثبات کارآمدی قدرت خود باید امنیت عبور از هرمز را به طور پایدار تضمین کند؛ ایران برای تضعیف این تضمین کافی است نشان دهد عبور عادی، مطمئن و کم‌هزینه بدون لحاظ کردن منافع امنیتی تهران ممکن نیست.
🔹
به بیان دیگر، هرمز به ایران امکان می‌دهد میان دو رژیم امنیتی پیوند برقرار کند: امنیت ملی ایران و امنیت انرژی جهان. آمریکا و متحدانش تمایل دارند این دو را از هم جدا نگه دارند؛ بدین معنی که ایران ناامن باشد، اما جریان انرژی امن بماند. منطق هرمز این جدایی را رد می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/akhbarefori/653628" target="_blank">📅 14:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653626">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4582342fa.mp4?token=anOIB_NpYx56VAjscGRgzCL_xUBrRBxY7HCH5_Y38ivbdqMMX7p9UlrqVZ7tY8_pqqCVX_gPdsHk08phNDKzqSMTEYcgNw9dxyfpaZ__u6v7esbCwFQvIuxDPopAIkcTf0RkmCkXDrUQx4eP-7rGARih8FH5Nq5fC0JOugtUmt2xY52_sRvgterQPjooFhc5zTJTia9HVITf-e2mlqm5etZoaMsXFofJ-vuXR4GDDyr29LjPheisDLkZANshiVKOIGmZQJjfaSh8xJQ0YMUHoBq-juimFaLmsSfpEWyRuCjHRT5KSzdguQpYzwxZIUkG-QeUuPJAncSZbPO14qrSkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4582342fa.mp4?token=anOIB_NpYx56VAjscGRgzCL_xUBrRBxY7HCH5_Y38ivbdqMMX7p9UlrqVZ7tY8_pqqCVX_gPdsHk08phNDKzqSMTEYcgNw9dxyfpaZ__u6v7esbCwFQvIuxDPopAIkcTf0RkmCkXDrUQx4eP-7rGARih8FH5Nq5fC0JOugtUmt2xY52_sRvgterQPjooFhc5zTJTia9HVITf-e2mlqm5etZoaMsXFofJ-vuXR4GDDyr29LjPheisDLkZANshiVKOIGmZQJjfaSh8xJQ0YMUHoBq-juimFaLmsSfpEWyRuCjHRT5KSzdguQpYzwxZIUkG-QeUuPJAncSZbPO14qrSkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تداوم نقض آتش بس/ حملات سنگین هوایی رژیم صهیونیستی به جنوب لبنان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/akhbarefori/653626" target="_blank">📅 14:42 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653625">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
قالیباف: در صورت حماقت ترامپ پاسخ ما کوبنده‌تر خواهد بود
🔹
نیروهای مسلح ما در دوران آتش‌بس به نحوی خود را بازسازی کرده‌اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده‌تر و تلخ تر از روز اول جنگ خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.9K · <a href="https://t.me/akhbarefori/653625" target="_blank">📅 14:37 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653624">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
قالیباف: ما در حال مذاکره بودیم که آمریکا جنگ به‌راه انداخت و حالا می‌گوید برای پایانش مذاکره کنیم
🔹
در آتش‌بسی بودیم که شما واسطه‌اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا به‌دنبال برداشتن آن است!
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/akhbarefori/653624" target="_blank">📅 14:34 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653623">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
قالیباف: از حقوق ملت و کشورمان کوتاه نمی‌آییم
🔹
رئیس‌مجلس در دیدار فرمانده ارتش پاکستان: ما از حقوق ملت و کشورمان عدول نمی کنیم، مخصوصا با طرفی که اصلا صداقت نداشته و اعتمادی به او وجود ندارد.
🔹
ایران همان‌طور که با شجاعت و اقتدار در میدان نبرد از کیان ایران دفاع کرد در عرصه دیپلماسی نیز با هوشمندی و قدرت برای احقاق حقوق حقه ایران و تامین منافع ملی کشور کوشش خواهد کرد.
🔹
نظامی ها بیش از دیگران و بهتر از همه ارزش صلح را می‌دانند، اما همان نظامیان هیچگاه اجازه نمی دهند، عزت و حقوق کشورشان لگدمال شود.
🔹
ما در حال مذاکره بودیم که آمریکا جنگ براه انداخت و حالا می گوید برای پایانش مذاکره کنیم.
🔹
در آتش بسی بودیم که شما واسطه اش بودید و آمریکا با نقص عهد، محاصره دریایی کرد و حالا بدنبال برداشتن آن است!
🔹
نیروهای مسلح ما در دوران آتش بس به نحوی خود را بازسازی کرده اند که در صورت حماقت ترامپ و آغاز مجدد جنگ، حتما برای آمریکا کوبنده تر و تلخ تر از روز اول جنگ خواهند بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/akhbarefori/653623" target="_blank">📅 14:31 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653622">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
حزب‌الله لبنان اعلام کرد: ما با یک پهپاد، یک سکوی پرتاب گنبد آهنین را در پادگان برانیت در جلیله هدف قرار دادیم و به هدف خوردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/akhbarefori/653622" target="_blank">📅 14:27 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653621">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjgOURoqikfD_auN47euU8Gy2QePsljdhiiZpIP-0Vm-Jwmvf4zEDM4BHzAZhDF21RZOHgB1yC0TjtOLMsfxmdEH63hdiDghuj9S8qEwbZZdo1irkLGzFfTgJVpAqfaa8qV_WI04ypwoqbVT2s2bSRzmPCaiYK8Lz0JpCY7B8k1CJfvxboJ82uUvqsx-0o0hhfd6GKMnR1or273BtvZ5A_wC_CF3go3e1mRteXhUwIyuKhkBcQnMT4e52I_DYTN_dNcnS7FeGTt5d-DC6YuWyys69srt2F6PtPxcCbFyo9yGVSE0krYlLx-AIkuLv1HAE0WYTfbahcZcmUFmErXLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
رضایت اولیای دم برای اهدای عضو همچنان ضروری است.
🔹
طبق آمار، ۹۸ درصد خانواده افرادی که کارت اهدای عضو دارند، با اهدای عضو موافقت می‌کنند.
🔹
این عدد برای افرادی که کارت ندارند، تنها ۴۰ درصد است.
🔹
به پویش «نبض ماندگار» بپیوندید:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از دریافت کارت، تصویر آن را برای ما ارسال کنید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/akhbarefori/653621" target="_blank">📅 14:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653620">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7eb03297a.mp4?token=c-9E19w1l9_K_NkyjWrJEQobQN6vfLBTykdVNj0TS21IF7DA4lbv7fSmlqXXK8xql938szG2PnE219QiCRmuEfXE5NsSFqb2Y1KdItT62z3cNy0R0EdWJnWWaoUBTUbBfj1lzefD1HzO4pQDyYutBdGr8Df6hUu24kEiHGLlEscscN6OdLUNb3hYokjfDnk_tHu5RfdugnHAXR2sDKiOqgZLPYuCc1by7-Lk3JAXzSf8_wA3k8fV1UavPZe_oLcq3gq3WVDG4hBFaoHTtphDJ427IasNTM9j1qzYMtXrqv3CPbMQnos5yR5AYNoVQVsZd52Org8v83dRYfVZWHm8AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7eb03297a.mp4?token=c-9E19w1l9_K_NkyjWrJEQobQN6vfLBTykdVNj0TS21IF7DA4lbv7fSmlqXXK8xql938szG2PnE219QiCRmuEfXE5NsSFqb2Y1KdItT62z3cNy0R0EdWJnWWaoUBTUbBfj1lzefD1HzO4pQDyYutBdGr8Df6hUu24kEiHGLlEscscN6OdLUNb3hYokjfDnk_tHu5RfdugnHAXR2sDKiOqgZLPYuCc1by7-Lk3JAXzSf8_wA3k8fV1UavPZe_oLcq3gq3WVDG4hBFaoHTtphDJ427IasNTM9j1qzYMtXrqv3CPbMQnos5yR5AYNoVQVsZd52Org8v83dRYfVZWHm8AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شمار قربانیان حمله اوکراین به خوابگاه دانش‌آموزان به ۱۲ نفر رسید
🔹
شمار تلفات ناشی از حمله پهپادی نیمه شب اوکراین به یک خوابگاه دانش آموزان در لوهانسک به ۱۲ نفر افزایش یافته و ۹ نفر زیر آوار مفقود هستند.
🔹
لئونید پاسچنیک، رئیس جمهوری خلق لوهانسک، همچنین گفت که روانشناسان و کادر پزشکی به کار خود در مرکز اسکان موقت ادامه می‌دهند و والدین حمایت‌های لازم را دریافت می‌کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/akhbarefori/653620" target="_blank">📅 14:19 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653619">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
تقدیر رهبر انقلاب اسلامی از میدان‌داری مردم سیستان و بلوچستان
🔹
زاهدان- رهبر معظم انقلاب اسلامی با اعزام هیئتی ویژه به استان سیستان و بلوچستان از میدان‌داری مردم این استان تقدیر کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/653619" target="_blank">📅 14:09 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653612">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TLlbsgDJV_f7fzqqx8gdNRlFtKKi7IlcTjVq_j1o_EOC1iM9-AXap7od701WxniPpj47sWbWgtr6f-5EkSQ-tUAX5McUlX_7AKPMolEdetSrULvURYGiX4a98q_txccFeYOK_6KH96r6L0jedmloAZZG1rPTzxGEAS5-Bh5xHEaeZxvSMRubI-_7FnFWYOL5lqv8dlVhiQJeMtpA6W5F3aHqw6kqeiml4aJeOhNgfNWgKLZ5gpCTHnppqC4EW1jbqKWFBwMff8LJ8WTuLIG5hgX1ix1K_wXGJkuxQW3HLYEwgZ-U7LnKMrlKvuYxJZ9411N3SPF55SmHQr3ruX3WdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vncKMXAVClrxZgUNBryD24tvLegPe9KbGXduOIkia5Me4Km4gIm0XJeXyQ7nIbl60Xm-1w2kj-FRM7BiNkL36qVEOROdSLl-hBK2kBpfiW3Aouqdvz04_LuCtxc3eFEShu8FiZKaCTcQU4mI7-z9mi31bEY9Tn8TF4MKNnD1xMPAW7b7A7_4MXrEpm1iFoSyTXGQ7QURW4n6py9hJu4xP5pe2gzz4b3hLqAdFwqdIYfZ-G6QfEqo3v9Nw7KQmFuvyQmTFDMbpjRmE5WYWsiau_5dRzac4Au_rSN2BII8cYRhpv1ly3m0AadZEyKYC7RA-vnaunKqn_NHfWi8SZun-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXeSmsS1DVty2lmBsXCiXFDftRkN6etipHJkE7gWmSGEWb8kRmrTRt_mvVqgliTglKSxHFouuY4oTP8Fe6tanN7JP9Q50WlNun3UInmppofpX1TCMgoqPIRdVdVrAoLin7eDKHr87w9p4ebU9qfojLkH1NwP2SRRyzTg6ZfXjZJn4yVOveYEScxJxZIuc5XOvlWqrXJk7DiF9eK8zG6AvC6b9Fx3Br0hiCaMi_0u10Wu8Dl2Yd16g6eip_DUWVqOzRBdRvUhS9KRlIuFPOzD5jZCtig8GSbu2M_fnEVSe6PaFyoUJdzN-oE8SaptGGHaJ3ElhBLXnOmhRnr_3diLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ooh5BwT6dktOmhEcqxC45zoss-jPGhxpOCzJox7BkwPU4MyawzEX6ewxbgO56DQykMFa0cm32-0unOmFywYVrCB9wXxUN4sEcWBA1_JLQhXWFfGScKNkGi5DAk8yTcHzGXbIMpgJ9UT6fMy7ke6X3j51-sRM_0SxDgTfsge8esUIGtZxOYQ0l1zphipq6YV0p6MD_Ev1wdIZhQftMxpOG8MQEwnIxR77XICyDta0P-QtY_KBXxM4GzegDlQfSdWFy0X98iO6KBdEQ1PCwjVX5DrDMyzgfttaFyDIewE0Zxhf6hfSutDBOZl0PTyS9APbNqjLFoXPtn8BUUAxz1QNPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m7IXQt8qFvUjKr24ANns3ADV-6MdI0ZuFhdZwXhUGi0k3mFLawO6485Ss-ZFY-KMC8P9EgVbWtzRrG5nSEATe25bGtLLvkdLFKYzAaazlRx6L4Cm80NUHgPRWFkdc93AxFKGZ9Meudpvn7K2Ome3lAJTtCDY0NkSaCrDwtf6-ZfDgpTrN6VPAu2ZUIH15NL3JbcDtIJa1Ui2WjFzLjB_boHUL4i0jmjfj2djYwu58DyWrKOO2XPzphMwS8IbJWPddVpmDhC3i58b1NZsXsNi_JsHb4zdYum_eFeguW4RSLZ4HTUvRdgXuRdESHXDkzJ8Y2CQTw95GOatY6DKQ2Sefg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iL7BoW-4d3fdAhwga--2PO6k0pLgALyB2Q8dJvV_T2i-y6m1ZrFAqeSHEHGx33fGX8E9YLpUWXQgeTAihnSxv70tWiDr5MPfk9Oz7qvM_2CfuaB127TigYXdB5K-sYdAEM_byR3mm8qvU9a8s2y4ntJ_UuNM3ho25QgNm2K2pkHAbjJwDWdttj__q11KC5pzWAHrUSQNWJ-Gk-aT-eO9KF2e8aEgkmjB1L3g-4uuaGLdaQjWA_dhfP6yFvERunklBAQ_Arx3_vKmGArSTsdpmcWXW21I-0N00ps-rUQwpfbo9C9XIfEG8KKIFuM23I1zyHMVoPfxwx9ZcGo-Z6hmiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hh-bDCy8whbm4mHZBeeT30Y74XAr9Q6AjtuJDY9lEj8biEGGjsOmqVjDA-vQVP1KgMVNBXDe32286iwAi3mf4Xlma2w2rwFg901OoJ5p8YVNC5eXWIUpYci8BxENnXObm6OKIkugj6oONVuxnWuWtkn3xWa-V6koU-RUdNe_1kln4g5LpZEB6uiyxLOutPVzLsfmbsehxyhcBFSBoJh8C5OlpgwdmOxHuaviDWZirIBVGa2gS8Zcj7P-ZHc74RQibhGVwv61SBZNabMu83xCeUBLFyj3sHDZEmepnXkGcW9ULeE7Jxonr8_QuzIoYnVUrmyT58sZm2q_-d3Mfe920A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کارگاه موشک‌سازی در همدان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/akhbarefori/653612" target="_blank">📅 14:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653611">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ejse1BIA5Ky_Zr-931pec02KPAeZlu9bjLGtC3tQbNWmfK03G3Lxy1Fray-kEr25gEKDSiDWKcddeHOOqcCHFI8de5vzgsHyS8GMZ6VBSnOsvBCyDuBat9qgeA92mmPsEcjbb3YAMeqOel05i0BIdZKLuXts5EkspbKdgEPPrY687ntG0o473u_HMD-FI2GfPdWXIZPNNUX4jrtUCJL5yqEAVl2U6soP0BuHgYRJSMdiadCo7ZSO9SMyGnAT1E6fqiwr-SDEq3K_6rxRtiQSN9y1h7Ek7vzTDQtc947-3Vna4DCtI0jjYoHtEoQxF_b45DCnRq5EgTQMi3IkY1OxUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شمار شهدای غزه به ۷۲هزار و ۷۸۳ نفر رسید
🔹
از زمان اعلام آتش بس در ۱۱ اکتبر ۲۰۲۵(۱۹ مهر ۱۴۰۴) تاکنون ۸۹۰ نفر در غزه شهید و ۲ هزار و ۶۷۷ نفر دیگر مجروح شدند.
🔹
با احتساب این شهدا، شمار کلی شهدای غزه از هفتم اکتبر ۲۰۲۳(۱۵ مهر ۱۴۰۲) تاکنون به ۷۲ هزار و ۷۸۳ نفر و شمار مجروحان به ۱۷۲ هزار و ۷۷۹ نفر رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/653611" target="_blank">📅 13:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653610">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
نورالدین الدغیر: وساطت‌ها بین تهران و واشنگتن به مرحله‌ای رسیده که یکی از سران منطقه‌ای به طور مستقیم برای پر کردن شکاف‌ها وارد عمل شده
🔹
ظهور قطر در این لحظه حساس به طور مستقیم و بر اساس اطلاعات و منابع موجود، نه صرفاً به عنوان نقش کمکی برای پاکستان، بلکه به عنوان نقش محوری است.
🔹
منبعی می‌گوید که احتمال دارد یکی از میانجی‌ها به واشنگتن سفر کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/653610" target="_blank">📅 13:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653609">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SyIrjuSEk4LQ3vswJ6B5xtoBSJYQpYgStljrVsqz1kKCYvDwmx8Gdw0d_hF8WKc6tZLXVw3PWAZqlIvXDKG5AXIZVwsMuPaWzb1wq0f9v5OPZOzwAptfnLAT85Fg42rAgZf8IVM2192e_O2dRL10z_OsIwXmE0SsQxtkUR8fi4TVkW97TVCmU6Ow8jyz6TEJm3zjdkvmH4e4CbU0FdBdG3c55JUDIfLq2ILXAEAojYtbpLV1WE-I1oa6WaPtdvmAfZwAfW_vb8ljQJPlJhgyOGoIJznRXeZJKxkVGJa2qKFpwrrw-UDnyrRfPZULKUJ-zmYanCWq-vHRwH0BS9tMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حماس: ادامه حملات به غزه نقض آشکار توافق آتش بس است
🔹
سخنگوی حماس تشدید حملات رژیم صهیونیستی به غزه را نقض آشکار توافق آتش بس خوانده و از حاضران در شورای صلح خواست تا برای توقف فوری این جنایت ها وارد عمل شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.41K · <a href="https://t.me/akhbarefori/653609" target="_blank">📅 13:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653608">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db37a199e0.mp4?token=EOAd3sst-ANlzUXKoYC7VUnBQsybEup0RygKHr8Kn3PA3wQBkzpO2oMu2TeJF5qBzBBcWup9azj-zApYtJiOzBwUGSyE-VdGbDFn6UuwkdFv-LehNUdqz7cdVNj0CEtHV5gpEsfR7ZONbJuF354KSnmn-NMYu-Xj65PFogxoAz_1emEWs3mnK5xKU9eduT8RaEppI5Nfl0gm8_cM7lIn6rChK6WiAEA5DzC0fO3-OlJJJL56VBimr0-R29NH4R2Jvk2rBqLhCpsuGhKXUbbE0y6CD51vHrG601f2GoUFoR-naHHOY291QqkvENfQZo2wKirSDwscExsRoK6GnpAU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db37a199e0.mp4?token=EOAd3sst-ANlzUXKoYC7VUnBQsybEup0RygKHr8Kn3PA3wQBkzpO2oMu2TeJF5qBzBBcWup9azj-zApYtJiOzBwUGSyE-VdGbDFn6UuwkdFv-LehNUdqz7cdVNj0CEtHV5gpEsfR7ZONbJuF354KSnmn-NMYu-Xj65PFogxoAz_1emEWs3mnK5xKU9eduT8RaEppI5Nfl0gm8_cM7lIn6rChK6WiAEA5DzC0fO3-OlJJJL56VBimr0-R29NH4R2Jvk2rBqLhCpsuGhKXUbbE0y6CD51vHrG601f2GoUFoR-naHHOY291QqkvENfQZo2wKirSDwscExsRoK6GnpAU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا تقی‌پور، نماینده مجلس: دنیا باید به هوش باشد که گلوگاه اقتصاد دیجیتال جهان در اختیار ایران است و اگر جمهوری اسلامی ناامن باشد، اقتصاد دیجیتال آن‌ها آسیب می‌بیند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/653608" target="_blank">📅 13:11 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653603">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VpQavGD914Qlj45tXtJpg_v1Ki_ablXxrQRtVCDND7LANigmoWs6w4oJOGwuGtSxdAPOz3EbIZDMHYgmfG-4IyBitUMucKAIB_gHYYQYYGf82rjYdGeGbLpiz9dT-NdUuhJGRwZcaHJrFaxjCKBNI8ntAWl_HcxSfUrbpc-trAlxHGD8vsKfvNzVJFVUVSyJNKZNu605Lamxj_t-j3X-kMpwGHbfRXrFYCqDWxWpsyLHAtCgLqSTye77uzcl4c50X-U0GSsLsQk2A1u9-z9AchbczGx5Xve-aIJSSFuIr2griXTsSgb-3qTxaDFqx9hD0sF0SSGp5d1z7x50Ni29TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rm4-SS8uNTwErm7VVOgsw1IEWl8SchT2gvQV_SI8y5mTZoN1cQxDVXYyPNbVAJAdStl4gxe73Gpf-EywJmID46P9Lr7AGT0EoXr4lTuWc3Fn7BoOR1q-vda-YJ0fIhC-jiylU4ZkfOborzCLMpNXImqB4Ti5lLy-TX2MgX1HDu6OPYgf4hzgRS2OPMObs3Fq8LASlukLL5LjCohLCOxhJC2oxxXdycBdjkNbzntjKl-7aPGnEoSzrGcnDLmXw6WHwYO8YJGn90e3ctC0wutSihVkJlPgg5a-0-DEL-24CXrh7nEMmwKNhOWl7bK4Mk0IzZi0SeXEExs8kzbd46rBDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_c4_j1TA1SYGSdkDyI3IJTttKzO7Vxm0eVnkNL7wRwjuR2Igd4-oeJ4EkGMHxykhW1mIda26mBQWhl-aSS6Ge0Er2PR-T5OwfEq08GumAyjZfu2JP196Fwo8FRQMZrRG0C6ERAAab7bSkVmO-MqpdrW8f76-lO2aMxfT9hxzvbM-5GrUAzOjeD7yGMxbS_kk6V1Fdsf9ijnsFk-P3zxTf4QxWb53wDbmHHD_BRiC4bSWrPeIXdBBU1Ep4ul5qra-_rArv_QXlaVceDvbToVa70Ru6E05Ur4OBUBd0zObxng5Fhx6YK_vtDaoE9oxs4-eDLSHIzudiHZltj-vsicag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzCXLyW6qZJ0YTvWgLLslGju8q2G8huyROteC281_IMR-rSovp7mAShfh15PiA4Cj4D-oBLaG_s0QhPwSrPzfBwdXvKIblRRhqduWeaBs3eb4zBlAqvx0Y0NqLP1nK6XLS1tpJJIonO23dpgBpTnn4MLhgRnnLSE8RSb4n7wnGjMwLzMnXaAX2Fi3opRjhZSB393Q-yIIji2Xy1U8AYEPczf7uNA-tJfusIz87UtKmTDEBHEgXWjEa9_LMwo84pvPdNatoHGjxsmPlvn9mjEqWekZrfxlCPru2WXeQGXxLDktRI0jEfaPrFr62dz_U2143xLuDuj9-ZwVD5aRsDncg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLybAnprUaG1RLkjWQkAxdR785YnS2MZCjcMpRyBkYbxRFgDByVL-YxzqY6a2Q0Uada0sbHj6ELXeXmWBFemihlwGeSvJAII6wX5baLN2TdwKtLDn_3njQk1HYX6eAzpnvxl97iU81nRGwfwiM5AbuvOVgRPMf34iqeJoaQh2TA5flP20DMANSpEEhKoWz9J4UdanXvMK7GtU76XPAEfpHvBOSMH_k9pqao1hwvB54kGM_bWMnP3wGYKb-IV3buu0MRNEvigHuC84gSjpQYZ_M1Nzz4sHvf8_BDy56wuHCNQyGGHor-9MDyAlwrozvaww-NLZoEk7YTZH2vCSijTjQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌‌
پویش مردمی نه به پلاستیک
🔹
مشارکت و همراهی شما در این حرکت اجتماعی، می‌تواند زمینه‌ساز کاهش مصرف پلاستیک و ایجاد آینده‌ای سالم‌تر برای نسل‌های آینده باشد.
شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک
@na_be_pelastic
@Alo_fori</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/akhbarefori/653603" target="_blank">📅 13:08 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653602">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iwfbtdNCtIm_EXt3bDtDBMK0BIvw_Tg7P6RseTOCpbyx44jCj991yvlvOWvY5kJWrtaw3buV1W_b7oDc7XC0_X3TxCaGBb0TTCrthe2K7SGBwwMiCGsYLuwqXpFoTh_7wAZlHnrWxdaMdfN69_KAHtNTeHf5pv94eMqU8qj8IY1X6Ao9fVXItiPFtvqjieeaNy5jeR0rN-Wl68g6FGEoW3gj0SaZcg8fu1EJU70o0-5cpEAqkY5WvUbLP13xyTQgchhj9_WI2N9R0gC6cZQxIJUckckRv9TSMN6_gmlrhxXn8x4huK7t0aE5o3ICfTFuXu2fHCd13-SRL-pbr0m3Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت طلا و سکه
🔹
سایت رسمی اتحادیه طلا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/akhbarefori/653602" target="_blank">📅 13:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653601">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbJf1HpwHbKtVaau52cr0apz9OHd7Lr1bMIqZGYRaosGEm8zu8y3ArGvG_8cG_bajSDGxuhx6DrmVdo7MmBsJ5PzIKLTlUppfqVEhWNGK_BUKgnNlVsq76VkORRuVsBYM2qsR1K0mz6X3jocwh6_pK47uvb24kveOLSYjZVj_4VMjzMn8hm6pfnVdUqYPOCt0qez1gshHJgpoS1qL8wBtn1WIy1zdv7Ke674FwNOGiDZdOGwuGtISyR-mregChM0oOHZtee9vAKH_Dds6rdpWwIoiaXSVg2RGRAhMrMu-LUnF94NfZB71yUbhxYliK72_0ZkEzO1P6VEXtu_l-JmXgkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df35f5dfa.mp4?token=N5GoB83MpXb7tAGWIKIVyG2pNvR6Hg7mwUASH3VKmFG-pazz8GSYxEUFWRZnzjbVyU7wTVZZdkvyo9MPRdy4_--yXXowPdXNJ81-al26PnPMJs6JZeBoAvvi4xqX5MzGgpHz4iHu2h2a9KTY-CrU13cwNa6GXJBKidUCjKSXuxptviuqB3cTfi-522vKv8G0Ukf-AZrXak7BxjBuZZdYIe9RCmV6rpQI3hQNylH4kkQevRoVNU9ZxCYJkk_iS3yFyQZaFmIYiQOZixWYpANtaiPoSC0PWg2OmaEOq0X69qn1Hk9vULaPB5mJw9Or9xXS7Ib9AbaQzfDDqvHzhqpqbJf1HpwHbKtVaau52cr0apz9OHd7Lr1bMIqZGYRaosGEm8zu8y3ArGvG_8cG_bajSDGxuhx6DrmVdo7MmBsJ5PzIKLTlUppfqVEhWNGK_BUKgnNlVsq76VkORRuVsBYM2qsR1K0mz6X3jocwh6_pK47uvb24kveOLSYjZVj_4VMjzMn8hm6pfnVdUqYPOCt0qez1gshHJgpoS1qL8wBtn1WIy1zdv7Ke674FwNOGiDZdOGwuGtISyR-mregChM0oOHZtee9vAKH_Dds6rdpWwIoiaXSVg2RGRAhMrMu-LUnF94NfZB71yUbhxYliK72_0ZkEzO1P6VEXtu_l-JmXgkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا تقی‌پور، نماینده مجلس: شبکه حیاتی کابل‌های فیبر نوری جهان از تنگه هرمز و باب‌المندب عبور می‌کند و ایران می‌تواند این کابل‌ها را قطع کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/653601" target="_blank">📅 12:59 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653600">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LaN2aZd8CVWdTherKMLlsp8GoQY_RMgt9wD00xwWXV1l_2ULrizRC6TmtEMqRc_u4wOavN7CyfbiJTDApIkFA_FbbeGfMwbbEX5pIHn4_QVz4pW7kRiVdQkTh8lbyOkM5Q3Ik8LnViBRgZo5szdAQJrr6mR2IHBd5OzAZRDpnpWyEIgevfim2beZPXqbZt3k_Sl99PHbJ-RKAsMBgV7JvnAQyIhykCVQldztaqYW0u9W06-f4PTsoI3BIlIcsKFwwz9es5Tegx_NDP5UjEZdQKQ5jO1r9ORJKSVgyebFKhtg7gdyMXdtwoT7W-XyJS54cTr4z3MDWDzs-ZV8m_79xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
انتقاد افسران ارتش صهیونیست از نبود استراتژی در جنوب لبنان
🔹
در حالی که حملات پهپادی نیروهای مقاومت علیه نظامیان صهیونیست در لبنان به تهدیدی دردناک تبدیل شده است؛ روزنامه عبری «هاآرتص» از ناامیدی در صفوف ارتش اسرائیل در جنوب لبنان خبر داده و اعلام کرد نگرانی‌ها پیرامون فقدان اهداف استراتژیک در لبنان بالا گرفته است.
🔹
نظامیان در اظهارات خود اذعان کردند که از «استراتژی حقیقی جنگ» بی‌اطلاع هستند و نمی‌دانند که آیا رهبری سیاسی و نظامی واقعاً به دنبال پیروزی نظامی است یا دستیابی به آتش‌بس.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/653600" target="_blank">📅 12:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653599">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO5nEF_k04I-_jVXPoLMswhSJE3UWeH0HvCuFDTyXDJ2t6t8G_4S3wWRkrm5rYFK29_3DRF-5FpU7f0ZN-ipbu00dKZcAxPY0o8DRNvVj2s3tZpkA0eiINjzSAcBVQ7f9kU9rOOrO1XLbIs8qx9fOGJIdLb6DgY4n5ThyM5Q1Pp8fLG466XI9IQOKysr_Jts6Na5Na--9_ODEfD3etoxB7dovSof2KsFn1rZwD2tITrkrW9auAHYIvy-ML48j7hW-E5lyuX4tYbYa9Yb6TESf7VnkiDGRnYss3fKvaZSXTYJMaVYI-X-yl_MsL0HnrYxG6-uhqDNtzQ8pYyw3V9JAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جهش ۶۹ هزار واحدیِ بورس
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۶۹ هزار واحدی به ۳ میلیون و ۸۳۰ هزار واحد رسید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/akhbarefori/653599" target="_blank">📅 12:44 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653598">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67eb0237ed.mp4?token=G4tokEEc3mN0ChOftx7N37zeidkPEqClOG8lmcb3_2JJM2F-bsPCWpxQckOpOfU4gtC25-_imUxazNGgj4PqA1vBUffKfeZU97zKuYqL1ic9b60peqCmXkUHhPVp8prk_GnFMhTvyCrHuJnDfMSpDtQ9wZ5z3Hvz0VjCyBaOSNyJ6W0AzxCZtvn_gfgxgHiOAEhMfjXdmMbUZW0ddWHYOV1neY9dIIid_v-uJ8QtEniCCD8POKpgjB_apEEw_xbIVHC9estWE6nvIAzscN2C5p5LYUiWtDZZUCjr8SLspeP6Fem3UF-4oPq2RNVLDnO7gHUrxtgQtb-JqhlJV1VdKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67eb0237ed.mp4?token=G4tokEEc3mN0ChOftx7N37zeidkPEqClOG8lmcb3_2JJM2F-bsPCWpxQckOpOfU4gtC25-_imUxazNGgj4PqA1vBUffKfeZU97zKuYqL1ic9b60peqCmXkUHhPVp8prk_GnFMhTvyCrHuJnDfMSpDtQ9wZ5z3Hvz0VjCyBaOSNyJ6W0AzxCZtvn_gfgxgHiOAEhMfjXdmMbUZW0ddWHYOV1neY9dIIid_v-uJ8QtEniCCD8POKpgjB_apEEw_xbIVHC9estWE6nvIAzscN2C5p5LYUiWtDZZUCjr8SLspeP6Fem3UF-4oPq2RNVLDnO7gHUrxtgQtb-JqhlJV1VdKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباسی، نماینده مجلس: عده‌ای دنبال این هستند که در مقابل رفع محاصره دریایی، تنگه هرمز باز شود/ تنگه هرمز اصلا قابل مقایسه با محاصره دریایی نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/akhbarefori/653598" target="_blank">📅 12:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653597">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
هزینه دریافت گواهینامه رانندگی با ۵۶ درصد افزایش به ۱۵ میلیون تومان رسید
🔹
رئیس اتحادیه صنف آموزشگاه‌های رانندگی تهران: در حال حاضر، هزینه آموزش رانندگی با افزایش ۵۶ درصدی به ساعتی ۶۰۰ هزار تومان رسیده است.
🔹
بر این اساس، مجموع هزینه دریافت گواهینامه رانندگی در شرایط فعلی حدود ۱۵ میلیون تومان تمام می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/akhbarefori/653597" target="_blank">📅 12:20 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653595">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BuqGwLxrevmp6YxBwtfS-JvfquIkG2Fp6JdcEC7JGGVRXm643g4jAFHS53IhOtMUT2r4J9ysTrNouNl6QxEZPnFupylsGIzq9hnYjnXp0cSB8H-fN06Vukv0X2DI4GZdVlKQDO2S_XVjkjsrcr9mSnDR1lcaVv_TOW8qK4LYOSK7GX7nFD-sfVbvC2Kaw86thtNT88Jr6sv9FYDG2N1_kgcMFuhLIGzK840QwnREZwad2kFNu8xyPqwPOJnz1uFc0MecvLlZthTv4ffErz8Vj_cirSm75ZkevaisanDhDqO4_G23TQDkBF0t-2oMAZYsW_vnMDn_y8r4_Qbm7y1tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازار مسکن در تله رکود تورمی؛ زمین، سوداگری و جنگ علیه خانه‌دار شدن مردم
🔹
بهزاد عمران‌زاده، کارشناس سیاستگذاری شهری و مسکن در یادداشتی اختصاصی برای گروه مسکن و شهرسازی نوشت:
🔹
بازار مسکن ایران در شرایط جنگی با فشار مضاعف روبه‌رو شده و رکود تورمی عمیق‌تر از گذشته ادامه دارد.
🔹
سهم بالای زمین در قیمت مسکن، سوداگری، کاهش قدرت خرید مردم و کند شدن اجرای قوانین حوزه مسکن از مهم‌ترین دلایل بحران فعلی عنوان شده است.
🔹
این کارشناس تاکید دارد بدون اصلاح سیاست‌های زمین، مقابله با سوداگری و مردمی‌سازی تولید مسکن، هر شوک اقتصادی یا سیاسی می‌تواند دوباره بازار را وارد چرخه التهاب و افزایش قیمت کند.
🔹
عمران‌زاده همچنین بر استفاده هدفمند از زمین‌های دولتی، حمایت از متقاضیان واقعی و کاهش بروکراسی ساخت‌وساز برای بازگرداندن تعادل به بازار مسکن تاکید کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/653595" target="_blank">📅 12:10 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653594">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OrKzn02J9Df-XX-PBSNCLEYgrRUeWfUPVzcccPXC-rXAoET_FvifK5kVwK_a5C4LOaG-s8b1zFJ-nWiiJIM_HBHT415X3xXQdb2waiQrh2gT5ffaFtogTEtBDQutE5LYAaaXENJkECUpRTaZaTFWKfI3sijahsrD_ZjtpINJ1ySgOWsqEdqdkFq_qBezpCZUEYjppDVTLAclWCaiqEOwoQWKMUBSKmFJ0nbx2fm1SbHNaGeauaoWGPrmEFbEBzBLZKZ3ztXXm5O-2b6hsbSziep9jf_P4By3V3GdNwgvyvQiry7PeRbmpgn_0EXpp26N423LkZtJRxx3HnSDzXPVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رویترز: ترامپ در باتلاق ایران گیر کرده
🔹
سه ماه پس از جنگی که قرار بود در عرض شش هفته با یک پیروزی قاطع به پایان برسد، ترامپ در باتلاق ایران گیر افتاده و قادر به یافتن راه خروج آبرومندانه یا گسترش حملات نیست.
🔹
علیرغم حملات نظامی ایالات متحده، ایران سقوط نکرده است؛ کنترل مداوم آن بر تنگه هرمز - که یک پنجم نفت جهان از آن عبور می‌کند - همچنان اهرم اصلی آن است.
🔹
رئیس جمهوری که به پیروزی‌هایش می‌بالد، اکنون با چالشی روبرو است که می‌تواند جایگاه جهانی آمریکا را بیش از هر درگیری در دهه‌های اخیر تضعیف کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.07K · <a href="https://t.me/akhbarefori/653594" target="_blank">📅 12:03 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653592">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
ابلاغ تسهیلات قرض‌الحسنه ودیعه، خرید یا ساخت مسکن
🔹
سهمیه تسهیلات قرض‌الحسنه ودیعه یا خرید یا ساخت مسکن در سال ۱۴۰۵ به مبلغ ۲ هزار و ۷۰۰ میلیارد تومان به بانک‌های عامل تجارت، ملت، صادرات و پست بانک ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/653592" target="_blank">📅 11:57 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653590">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
توقیف اموال ۹۶ مزدور دشمن در قزوین
🔹
دادستان عمومی قزوین: اموال ۹۶ نفر از مزدوران خارج‌نشین و داخل کشور توقیف شد؛ برای ۳ نفر به اتهام جاسوسی و برای ۶ نفر به اتهام انجام اقدام اطلاعاتی، کیفرخواست صادر شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/653590" target="_blank">📅 11:54 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653589">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KuMeZ_PNzaq2tj9TpGQY7NSagDXdSEfnBLgj6ycBwAIyrnOnSC-4i7pUEwwdVJs4WHZrivviLACyvmCu8YLgRuzpuS2abbFqB0rFFOHnKMB0tW1Z0I7NcNIdJweuf9hCWXiskbKXSaHq9dYtaRWV8Lzsey-JDu8AeqFW3QJpImHXq7DXj8ttCrcfWI2ROi54e8u1LZ6tEvCtsuEY_qNvS0qlVUJBURI2q_lvpJqUr8n1FKHkeJ0lb-g7gV_jIfGEAEdgEdEyrmLS5bp3ayTxDLwEVC2-bxZJ6PvjT8EF6iQZrNxCGbUGsUM7N1wT4qTNjx1GJk2lW2a8Wc3h_9YsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای سی‌ان‌ان: هکرهای ایرانی به شرکت‌های هوانوردی آمریکا حمله کردند!
سی‌ان‌ان:
🔹
پژوهشگران شرکت امنیت سایبری پالو آلتو ادعا کردند که هکرهای منتسب به ایران در جریان جنگ اخیر با آمریکا و اسرائیل، با انتشار آگهی‌های جعلی استخدام و نرم‌افزارهای آلوده، شرکت‌های هوانوردی، نفت و گاز در آمریکا، اسرائیل و امارات را هدف قرار داده‌اند.
🔹
مهاجمان تلاش کردند با جعل هویت شرکت‌های هواپیمایی آمریکایی و انتشار آگهی جذب مهندس ارشد نرم‌افزار، به شبکه‌های داخلی سازمان‌ها نزدیک شوند و عمدتاً کارکنان فنی و مهندسان نرم‌افزار را هدف قرار دادند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/akhbarefori/653589" target="_blank">📅 11:50 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653588">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JIigFHWfh6Tbj4nVYLNd2rW3W09JydvWn6D83D61Gstu2SH86rb80-iH7A6Ym4dxRXSZ2o53V_CySWHzlHbCCO1efhoeiGn23JZIN-rcEi_rqyp-7TaD6QbjCIKMgRq25TZRY2eIDEvWQWVnIjwre8ALQrYSOsVVLeEGNoboly3JsYg_b18ypoLcC61zoN47t5V9J6QzGn7VgqUF39Jo4Ig7VpvT7L7pzTwLQxiRbgjZKzt4rkOZoezLHGyYK_-UTEFnBph6EPGyPT0TXpboDT7KzTEBBTbKOQ2L19-uYLKhJ81EO-slqlXQtzPpd3nfUNhPgE4So406qcz17YTNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عضو سابق کنگره: ترامپ ممکن است جنگ ایران را بهانه لغو انتخابات ۲۰۲۸ کند
🔹
قانونگذار سابق آمریکایی هشدار داد که ترامپ ممکن است با الگوبرداری از اوکراین، از جنگ ایران برای لغو انتخابات ۲۰۲۸ ایالات متحده و تمدید حضورش در قدرت استفاده کند.
🔹
گرین در مصاحبه‌ با الکس جونز، یکی دیگر از حامیان سابق ماگا، به اظهارات ترامپ در دیدار ۲۰۲۵ با ولودیمیر زلنسکی، رئیس‌جمهور اوکراین، اشاره کرد که از برگزاری انتخابات ریاست‌جمهوری به دلیل جنگ جاری با روسیه امتناع کرده است.
🔹
ترامپ در این جلسه به زلنسکی گفت «پس می‌گویید در طول جنگ نمی‌توانید انتخابات داشته باشید؟» «سه سال و نیم دیگر، منظورتان این است که اگر با کسی وارد جنگ شویم، دیگر انتخاباتی در کار نخواهد بود؟ چیز خوبی است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.36K · <a href="https://t.me/akhbarefori/653588" target="_blank">📅 11:40 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653587">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رکوردداران عبور از تنگه هرمز معرفی شدند؛ چین، هند و پاکستان
فداحسین مالکی، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
صحبت‌های وزیر خارجه‌ افراطیِ آمریکا (مبنی بر اینکه هیچ کشوری حاضر به پرداخت هزینه برای عبور از تنگه هرمز نیست) فرافکنی است.
🔹
کشورهای چین، هند، پاکستان و برخی از کشورهای حاشیه خلیج فارس که با ایران همکاری داشتند تا به حال بیشترین عبور را از تنگه هرمز انجام داده‌اند.
🔹
خرده فرمایشات آمریکا به گونه‌ای است که کار را سخت‌تر می‌کند و تمایل ایران به میز مذاکره را کم می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/akhbarefori/653587" target="_blank">📅 11:36 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653585">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc676252b1.mp4?token=V3cd-7FzEms9rIdWB5pYqE3naHL8L2_K1x_G4XsPCBe9RFTWQk8nO_F_wzYNXyJfvDphyvRoOHiSZaB5_B4h69IewKI6X_nBNpN-0xMeBgPF3JSUIxgFBLl_-S0IW-IacF5VxrANRV7YfDDsbElOI_9H9ziRllMWfUH5QOGuCOQH3bkt4ZYodomwer3K1Vb7y9pUIXMdZvZmsivYuR3RIualsfBAh43s8JxQ7hCRJsCPw2-xhocuQmVSLxJIRmZdP_5M387y8uD2SZIEeDZpRdVPRk6gkTuZsp0N43Y_7VQFb9IdU7Bz5FWLmfFSQMYDEKdRXoze6tY_BkGhL67pfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc676252b1.mp4?token=V3cd-7FzEms9rIdWB5pYqE3naHL8L2_K1x_G4XsPCBe9RFTWQk8nO_F_wzYNXyJfvDphyvRoOHiSZaB5_B4h69IewKI6X_nBNpN-0xMeBgPF3JSUIxgFBLl_-S0IW-IacF5VxrANRV7YfDDsbElOI_9H9ziRllMWfUH5QOGuCOQH3bkt4ZYodomwer3K1Vb7y9pUIXMdZvZmsivYuR3RIualsfBAh43s8JxQ7hCRJsCPw2-xhocuQmVSLxJIRmZdP_5M387y8uD2SZIEeDZpRdVPRk6gkTuZsp0N43Y_7VQFb9IdU7Bz5FWLmfFSQMYDEKdRXoze6tY_BkGhL67pfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئو حاوی تصاویر دلخراش
🔹
کشتار کودکان توسط سگ هار آمریکا در فلسطین، همچنان ادامه دارد...
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/akhbarefori/653585" target="_blank">📅 11:00 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653584">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GAX8vtEKtLznPc5H_WtyeaUToPKMVUOOj4t0IL9sGD2Zsnuk8XMNyOpR2wPmg1OXoeA18_D8cBZhZYlcFpwRX3GH6olrKXGqTqS47jM3tUhhWivpTnAhYBdWyscWxQQIcgaMlsf1AEGBxPp4aJgKWXGOalfpxfy9HF9CtJuixS5wiDYlWpfLgnuguc1Q-rLVwE6rl2Ogxh9MqI0hHq0muQ1ecvsV4ZLTdL_K9m2U2m7r_o1pNnBxL6OGaaPef_Coi5JaYy7AjFuWKTWxP-pLnmz0MXhDaEB4JEQNTnwbyOxvKk_wNEqEqXMpeN8SHUOGuemRA1ut4g2KYgf7tEaZdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پشت پرده خبر توافق قریب الوقوع چیست؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653584" target="_blank">📅 10:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653583">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
خبرهای داغ را به انتخاب مخاطبان وبسایت خبرفوری مرور کنید
♦️
🔹
لحظه به لحظه با احتمال امضای توافق ایران و آمریکا | دیدار مهمی که امروز برگزار می‌شود
👇
khabarfoori.com/fa/tiny/news-3216870
🔹
یک تحلیل عجیب؛ حمله به ایران در میانه جام جهانی؛ از حمله پهپادی به ورزشگاه ها تا گروگان گرفتن اعضای تیم ملی | جام جهانی «خونین» می شود؟
👇
khabarfoori.com/fa/tiny/news-3217004
🔹
روایتی تازه از متن توافقی که ممکن است ایران و آمریکا امضا کنند
👇
khabarfoori.com/fa/tiny/news-3216986
🔹
حکم بازداشت شاهزاده صادر شد!
👇
khabarfoori.com/fa/tiny/news-3217011
🔹
جنجال حضور سلنا گومز در فیلم ۱۸+ | هواداران با ستاره‌شان اتمام حجت کردند
👇
khabarfoori.com/fa/tiny/news-3216860
🔻
ویدئوهای منتخب را در آپارات خبرفوری ببینید
🔻
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653583" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653582">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
۱۰ انفجار در شمال فلسطین اشغالی در یک روز
🔹
رادیو ارتش رژیم صهیونیستی گزارش داد که در ۲۴ ساعت گذشته حدود ۱۰ انفجار مشابه حملات پهپادی در شمال فلسطین اشغالی ثبت شده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/akhbarefori/653582" target="_blank">📅 10:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653581">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
استاندار خوزستان: محدودیت‌های تردد کانتینرهای تجاری ایران به مقصد عراق، با دستور معاون اول رئیس‌جمهور لغو شد
🔹
موالی‌زاده: کامیون‌های کانتینریِ ایرانی می‌توانند بدون محدودیت در نوع کالا و بندر مبدأ، از تمامی مرزهای خوزستان، به‌ویژه پایانه بین‌المللی شلمچه، وارد خاک عراق شوند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653581" target="_blank">📅 10:05 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653580">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTRLgSDPww6FgnLjRdcnvloiJBLIiG5zBZxpDwBxqEmbmJw_mX-hVx4e1ojTyLrBvbczU8VakyTIoTq0xeUwwW50WGFRPaX95lNcWdN01SAECrlRgQ54KNVvWNtZkabL1JT8kQK4N3ZYCEqGM57gs8WSjm60wPvjavy3lWgBrxkIG8E8JGE8E14GFyrk1cDkBrtAqw2JLMv6f9UDFv1oW6-fy9M6tKaggO8NJl5-D5J4tsz9IIJSojXPGfD2ZZXckTPUOlTEMbZ0vhMu9yNYpYOABi3TwJCrSP9RmxPFoiBjKRltMugM4MBaUdkWuhdhIg-fXuICkbVosMjPaUkULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معاون رئیس جمهور: صرفه‌جویی صرفا یک انتخاب نیست، بلکه مسئولیت ملی ما در این «جنگ اقتصادی» است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653580" target="_blank">📅 09:56 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653579">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1hhvix8EBf2ti2NsCbpblTyQ5Wejv47uS7UYLW6F302eKsaUqBW-dWhZjFo-g_R94JOrS9t9eepCD5kc7LVI_jh8qN7Qd926Y-OnAL8HeRGXL5W-xmtx5ovxEzy9Akzd-In05WwMbt2kTNGynigixBUhnR9934dAQK6DVPGEzgbgaytJny3XjKxjzONEssa52nrxfkaXXevr0-hjnVSNpTpIEl1nWoN_v0V5K9ZHAzl63uWgdPs295eNWCeRZDoHm_dBez_BF4FrEMmXdRNGM_FAjLEuQDZ5Hv48Dik74k1uKY5LxsDZX54YqVYPz6WkRGxaQrD1e72MC3ftDpZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستورالمعل فوری مدیریت بحران دارویی ابلاغ شد
🔹
دستورالعمل ۶ گانه مدیریت بحران دارویی، از سوی مدیرکل دارو و مواد تحت کنترل سازمان غذا و دارو ابلاغ شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653579" target="_blank">📅 09:32 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653578">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4bd9f809.mp4?token=P1pW-neFMcBUzaMGDcF09TwxlCCE21buG2zHusL1dn89EUR9Aufsa9WhE0Dq1rHz8nXkoI-HwvD-TyFGH9qCXQBXZ9cD3M1Lpc0mB7oRDA9MvALkc_Jh0vFuyXyRb0Mxh-JUC5tHz9JoBe6OM12dwc-76VPFqu-cgaUn0eQRzqVgeqPeQKvPx5u0cHun5pAv4Nj-DQ2DhK03fUuZQR2g57obEprGmqSMIN9BFZySykNJJk1j5P_cQKj_aw7cpRHzC71C7RE0lQ9CuSVTASqpPQRsBIBhvreInDDTseP6255o-meM8Go8T1_6KzCc_ZtwP3VAxfAOAM7lR-PM2Kl44Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4bd9f809.mp4?token=P1pW-neFMcBUzaMGDcF09TwxlCCE21buG2zHusL1dn89EUR9Aufsa9WhE0Dq1rHz8nXkoI-HwvD-TyFGH9qCXQBXZ9cD3M1Lpc0mB7oRDA9MvALkc_Jh0vFuyXyRb0Mxh-JUC5tHz9JoBe6OM12dwc-76VPFqu-cgaUn0eQRzqVgeqPeQKvPx5u0cHun5pAv4Nj-DQ2DhK03fUuZQR2g57obEprGmqSMIN9BFZySykNJJk1j5P_cQKj_aw7cpRHzC71C7RE0lQ9CuSVTASqpPQRsBIBhvreInDDTseP6255o-meM8Go8T1_6KzCc_ZtwP3VAxfAOAM7lR-PM2Kl44Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صف‌های شبانه برای یک قرص نان در سوریه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653578" target="_blank">📅 09:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653577">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
فعال شدن آژیرها در کریات شمونا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/akhbarefori/653577" target="_blank">📅 09:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653576">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
ایروانی: دولت‌های خلیج فارس موظف به جبران کامل خسارات علیه ایران هستند
🔹
سفیر و نماینده دائم ایران نزد سازمان ملل روز جمعه در نامه‌ای به دبیرکل سازمان ملل و رئیس شورای امنیت به برخی مکاتبات اخیر کشورهای حاشیه جنوبی خلیج فارس و ادعاهای بی‌اساس آن‌ها، به اظهارات علنی اخیر مقامات آمریکا، از جمله رئیس جمهور آمریکا و فرماندهی سنتکام پاسخ داد.
🔹
نماینده دائم ایران در این نامه، مسئولیت بین المللی دولت‌های حاشیه جنوبی خلیج فارس شامل قطر، بحرین، کویت، عربستان سعودی، امارات متحده عربی و به همراه اردن، به خاطر مشارکت و تسهیل تجاوز علیه ایران مطرح و تأکید کرده است که این دولت‌ها، به‌عنوان دولت‌های مسئول، موظف‌ هستند جبران کامل خسارات وارده به ایران را به‌عمل آورند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653576" target="_blank">📅 09:12 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653575">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سازمان ملل خواستار پاسخگویی درباره رفتار تحقیرآمیز با فعالان کاروان غزه شد
🔹
سخنگوی سازمان ملل متحد: کافی است ویدیویی را ببینیم که توسط یک وزیر اسرائیلی منتشر شده و رفتار تحقیرآمیز با افرادی را که در کاروان بازداشت شده‌اند نشان می‌دهد.
🔹
افرادی که همچنان در بازداشت هستند باید آزاد و به خانه‌هایشان بازگردانده شوند و همچنین افرادی که مسئول این رفتار بوده‌اند باید پاسخگو شوند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653575" target="_blank">📅 08:35 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653574">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">♦️
حملات گسترده رژیم صهیونیستی به نوار غزه و کرانه باختری
🔹
ارتش رژیم صهیونیستی در ساعت گذشته حملات گسترده‌ای را علیه مکان‌های مختلف غزه انجام داد و به مناطق وسیعی از کرانه باختری یورش بُرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/653574" target="_blank">📅 08:04 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653573">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdSMMBG00QWQ9us89ALOrNzYOTDZPFUlvBN-1iRz599RHS6jRgrg4SumhrW-anuG7LOjkssvCO0JiBTK5e-xONLrW0DJ5giiJLyB75_d4LMUF3oavGB8Mjn85wQRjnZ3lenChvDmsYtWcyjohrDDUx37W4uymNgn5q6O2UVihqlKoQH6KRmjFMALOhybC6d1HTZdXoj2QaXYibz0yYp_BAKcpcEfVAaB-m2Kx069AJ4cl-B29l2VQZ4u7IzQOC__r5XjwF3grcQZFtLUA1sMfDUQT5a6WlgBh4TqdY24tDU3ydnsmA11xTUXbN53LEpvJe8Tg-pTHAIx-_NzA_tVcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وقوع حادثه برای یک نفتکش نزدیک یمن
🔹
سازمان عملیات دریایی انگلیس امروز از دریافت گزارش‌هایی درباره حادثه امنیتی برای یک فروند نفتکش در آب‌های نزدیک جزیره «سقطری» خبر داد.
🔹
طبق اعلام سازمان عملیات دریایی انگلیس این حادثه در فاصله ۲۰۰ مایل دریایی غرب سقطری در یمن رخ داده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653573" target="_blank">📅 08:01 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653572">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKBTeLuYcmlFstYJY9Zwp4uXFR8TDgWUJEVB2YlyyyMRVwaQI8ygc9TbCdCWGNlym_9AwiZQiUmjTWB9YR71MNDDBJybXNA4aGsj9RWb1JPUlMmL6wgONqv4UBK5thbYYo7IvSS3H3ZbbCdcn6LYOkVy3Jp-jNXlKacE7kHNG47SX3G0lW7q9XlnlaL5zyB9LfaZUep84C2LSKlrvr7SoPR8mpfXn6F5PJ18s7NuijlrBdkzoJ5WBk2kpGlGg_jGkOI1Sj950MDhe9HBGw_HyIyQoDrn-xZIuIMKYJGApZoc3RtCAsDwanp4ULXuR_HyJg94Z8V8AdblogSLYGFc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زیاده‌خواهی آمریکا عامل سومین شکست متوالی کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای
🔹
کنفرانس بازنگری پیمان منع گسترش سلاح‌های هسته‌ای برای سومین بار پیاپی به دلیل کارشکنی‌های آمریکا و متحدانش نتوانست به سند نهایی دست یابد و در نتیجه، رئیس کنفرانس با اعلام عدم حصول اجماع، متنی را برای تصمیم‌گیری ارائه نکرد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/akhbarefori/653572" target="_blank">📅 07:46 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653571">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
ادعای اکسیوس: برخی منابع نزدیک به مذاکرات همچنان بر این باورند که طی ۲۴ ساعت آینده فرصتی برای نوعی پیشرفت وجود دارد
🔹
دو مقام آمریکایی به اکسیوس گفتند که ترامپ روز جمعه صبح جلسه‌ای با تیم ارشد امنیت ملی خود درباره‌ی جنگ با ایران تشکیل داد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/akhbarefori/653571" target="_blank">📅 07:24 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653570">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
یک منبع ایرانی به الحدث: طرف ایرانی خواستار تضمین‌های روشن در مورد دارایی‌های مسدودشده و تحریم‌های نفتی است و این‌ها مسائل اساسی هستند
🔹
ما از تلاش دیپلماتیک کشورهای منطقه قدردانی می‌کنیم، اما توافق به ارادهٔ صادقانهٔ آمریکا نیاز دارد./انتخاب
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/akhbarefori/653570" target="_blank">📅 07:23 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653569">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gayTU-rAp4doRNqdyl67cLk6yaQz6RPF4YnNiLPo_VWbA0FexrniQ7X0GOsHtGs9l9kmRVJP2l1GRtgTOyTPB0Qg_z3GZ9ZC4daYTRWo_Pp4ZH3XtQkHsUIosmLiQTGEoX_mlvz5frJnRrsA6pxKNscGS7vl9v6xrheYJX90yzE2HGLVYd92rN9b091JfKerqKlfT0p8RBRTKCGrBu4JYnNEVtK9EH26gD8eS3AvUgfyUI0f6AZkX_LmkgLWwvn42xCwEtrsWhmbPsIQsQFyXihXEomM3HqLln924u78pTHD6le08R6yimZt5hf4LbWQdJceVzd-hvqfdjNyqf9nCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز شنبه
۲ خرداد ماه
۶ ذی‌الحجه ‌۱۴۴۷
۲۳ می ۲۰۲۶
شنبه‌ها
#دعای_عهد
بخوانیم
⬅️
متن و صوت دعای عهد
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653569" target="_blank">📅 07:02 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653568">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8NexX61G3-M9e3Sd2OVdFQ6z7nDIX3Nz4LuyuwMg520CXyr0klviEYjXCFZ8sSU2YZ-24sgNX0Fmn29AvJyz_QWDfuvAZ_TDfl79ykhgC87BT9K7PWu1WbpKsc_G15t0aJ1XYE6EDAxCknMMGFUl_8qtSQnMkw74yEN8hqDe8D-3YgmnmOqHd2izylcn57CHIHuKRJQhi7aAvVK3oRWvx-DRyj6OMHMnBQeAQc3AEqps-ndL6c6yql2KRx5Ru-h00UTj5TfLIoOmPntvrgCSgyxIBY-9fuR4buirPvmie1rViDieArkcW64XYcsWcLQckAY2TdvhuFybbKF17_jUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
توقف صادرات خودروی ژاپن به خاورمیانه در سایۀ بسته شدن تنگۀهرمز
🔹
طبق داده‌های دولتی ژاپن، صادرات خودروهای ژاپنی به خاورمیانه در ماه آوریل، به دلیل اختلال در مسیرهای کشتیرانی ناشی از جنگ علیه ایران تقریباً به صفر رسیده است.
🔹
براساس گزارش رویترز، این فروپاشی در تجارت، پیامد مستقیم جنگ آمریکا و رژیم‌صهیونیستی علیه ایران و متعاقب آن، مختل شدن کامل مسیرهای دریایی در تنگۀ حساس هرمز است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/akhbarefori/653568" target="_blank">📅 05:33 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653567">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXRt1Bc5l-T6iiSWjNos1ckQhUbllp8rzr8hRk0UxsfeE53LdsNE5AOEn_-9ofAqUHtvC6DVc9fDNtnoDzbXUdUZ7HKXL_voiJZhnlhDiQ12-_5gYxop_jTIkXIl41jcv1UhcW-_ueUCBqJtdqHZ8JB9FCrU6WonHxFmzu76k0B3i8TLdKt76jDEStQd2BXmo4dOhrkGQKXBBl2zNPbowceXaIYmKKPM9WM6bYgbJ8OXUTMYF7KheRJJdAYhbdWhDjTM5OponWRPP_qm_Kgwash138B18qa5-QL1TBeJwxiBa-A62XHU4ZQK_f62J1VvgQDEbEvGWGjB2YiLkDx1NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کنفرانس بازنگری ان.پی.تی بدون نتیجه به کار خود پایان داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653567" target="_blank">📅 04:47 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653566">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">♦️
گفت‌وگوی وزرای خارجه ایران و عراق درمورد مذاکرات تهران - واشنگتن و ثبات منطقه
🔹
وزیر امور خارجه عراق خطاب به همتای ایرانی خود تاکید کرد: عراق چشم‌انتظار شنیدن خبر پایان جنگ و بازگشت ثبات به منطقه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/akhbarefori/653566" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653565">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
نماینده ایران در سازمان ملل در نامه‌ای به دبیر کل و رئیس شورای امنیت، اتهامات آمریکا درباره حمله پهپادی به نیروگاه باراکه امارات را رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/akhbarefori/653565" target="_blank">📅 03:21 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653564">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
محکومیت حمله اوکراین به خوابگاه دانشجویی در روسیه
🔹
پوتین، رئیس جمهور روسیه، حمله کی‌یف به خوابگاه دانشجویی در منطقه لوهانسک را محکوم کرد و به ارتش خود دستور داد تا گزینه‌هایی را برای تلافی علیه اوکراین آماده کنند.
🔹
به گفته او، در این حمله شش نفر کشته و ده‌ها جوان زخمی شدند و ۱۵ نفر دیگر نیز هنوز مفقود هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/653564" target="_blank">📅 01:53 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653563">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49b200640b.mov?token=JjQdbxoIgSIeua8BYLgVDMR3CnachoUzct5tVJD0Gt-0BaW8GHN9RSgQlUyjHLsksA25rIf_tcD3oaNzVXoX49FGYpi44GlK4SkGTbWjSKvMXJ3f0cCSwZeDy9jwCAlpblHSwtip9iVjPcDi2JnCIbP3IZhcd4cvvZbPYbtQ1foF9H-ApxMvOhQV1hl4WRO-5rM2lFop04i_F_U6XRKUAcO5aTLa1h131EPuzo1w1zhlZBdKwLMjX829wJSWKyjw2RGdwYSCMEaFp734BRe95awK1bf3d_25hicTSeqllVM_mYvZduAqmSkVRcbSpurmT8UFL1Fdj4QrgWWZbvKA4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار جالب امشب مردم در میدان تجریش خطاب به دشمن
🔹
رسیدی به هرمز، بزن رو ترمز
🔹
ما عاشق نبرد با یزیدیم اورانیوم به هیچکس نمیدیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/653563" target="_blank">📅 01:51 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653562">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kgdZqEf1dYfCMkAEpDZO3yyQtnBUbwgQIDQ2kAJbtK7SlYSOVurkULTiemkaplKkvR4X_EbTxjVcb0Qpsq3ImpBxSGADz0-TZ3D3ap_Ai3tJ5o4yPM4a2Z08gXCnkkxIYlZWuqeQf41PCYEuE5ZtwfBD4weLdNmjg4QJ3lBDeGOCxYicPCUVM7qyoz4uWa8D6u2YAiZm2tnm20VGNAc-Uww_OcZk4-O7dQgJ_XVAn5sxAjrVokyKAhHL0-Qv4q5gisTJ7-s7uciUwqBvx1X5iyUCKOfWWP--xp5xqiYfnvl9NN0345PlCGrsr8jApHi0FiZjsH3GXLKHsdMCwP4Fiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آملی‌لاریجانی: دشمن در صف‌آرایی مستقیم به زانو درآمده است
🔹
رئیس مجمع تشخیص مصلحت نظام: ایستادگی ملت شریف و نستوه ایران، دشمن را در صف‌آرایی مستقیم به زانو درآورده و او را به سنگر تحریم و محاصره کشانده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/akhbarefori/653562" target="_blank">📅 01:38 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653560">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94cec408dd.mp4?token=Q9LlAGbJPIx5GIMF0QYwm0QfSPWmlsp3onCcM7kEvmO3UcgRvyBk4Ur_EnW_0HBlXGaWPcPLuoOSyuZslakSHZAbWLDOD14-L6VPIIgco35r0rE0ndaQ802sZso7dmK7KIJ6SjArz7kf5ETRA6yMSzk7u7SKTxWHAnMQVAjmPlNv_72buqKSZe9IOKn33JVYB8jMdqmzH7yQh5-R6j40HYHdByCWrxziKoP7CtIHtH_AOolqBI880-4teN4sb8keS1WBOhIDcHy-ERAC3AahljlLOdXRRNuPeXVLxLwbuWr8KUTDY4P5F08PGbpHyGb4PY8v_zfIR2mMGXTTLKN0BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
همکاری اعضای ناتو برای بازگشایی تنگه هرمز بلندپروازانه است
🔹
روبیو، وزیر خارجه آمریکا: «نه، این خیلی بلندپروازانه خواهد بود.»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/653560" target="_blank">📅 00:22 · 02 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-653559">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af58dce728.mp4?token=pnA-n6gj7LkwpV__bH85JoWKVbdfbI0yKbxHz6nFyLvwl9-AEjDSfPR1HYH3OiR-DwuvAx2bE6mXHMRxruDdIUt6AgElRz_SPcgy-M5Scx8qQiCB3Z3aRYC8TQvg5xscXZigmZG_Jn1WO4E3E-9khnvgSqtADdkFhzSUNNj6rOGnof-HaYIzOTZHtoA7BeUu9tQFyaXDS1ERhyauYMKRu0qgcgaZsBheg_QSg7SrS_hPPMtgc16OOfkiHJpbbe8BvQ63RQesPufcf_vAW3w02gJC8tsopjvvIKtI1WXkJxaTMLxfApqmPa95XowWg6aQ44mhrwEh19Lx39SH5ees7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای ترامپ: ما ایران را متوقف کرده‌ایم. آنها هرگز به سلاح هسته‌ای دست نخواهند یافت
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/653559" target="_blank">📅 00:15 · 02 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
