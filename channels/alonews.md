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
<img src="https://cdn4.telesco.pe/file/KeFNhqeTxV4U7KRpuCe5uyTrpfgEjEM5hakugEWK2nadMCT2YLemJ3hf9eN2wc9T0G-xCiihO9YvH1cJGhtf_6M8u7rJv3X-ROTMBGJAwVsbGA4wvyv2-hrdi8Vhn9V4uaTbxYze6QwxhWxjobqqmn5hdNl4ZusHCB_QNJNVCjKdUAKj8O0PlnbW17Jiopof-N7Q8ihu0CTbyQZrrBRHPx_mc-x1HYt-0tSCpnWUVlHJnscEynbsYa02qzbf9WxBbSMV3yZFyZzIUrGdG3_P_1av0OxS5-94NjCdr6Rd4dXZ0yfveZC9BAxDqtPfhaiiAyZQqmIAKYRFYQ3FQXwkfw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 971K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-19 15:17:58</div>
<hr>

<div class="tg-post" id="msg-140945">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2DOdmdaQbUTkApYDSJnJ6pedb9txXy-o-euBqMq9Xdmo9_je-B9LRBw49IlfIka3ntMZkaJ1QMXY0gQjHjX9nnRk2qjFD0VlJBY0LhMwMIpoTXwfCYcMRjwGc_nSqdXxkVMyBoMvddtM4tH8OXBCBKMe4z4I4tKUPi-VY1eZAXYAdkNbYrUyGsLh82u5N_92YnyCIH5xYQmMzYwQamFdd1oUoeYL-v-yj9WidF9_C0SFSLijyb5Af6QzLvfH6VAQ7ND96kA_0TCZQIFLV5Q3IvjFu-7wIj13D7lc2duuBxCCxfY-NDMm1s0c-VIBwlzxKNuBpJQOyYYP0z4RwhNOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شهرداری تهران از آغاز خرید خانه های سانتی متری خبر داد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/140945" target="_blank">📅 15:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140944">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
فرمانداری سیریک: مهمات عمل‌نکرده در بندرکوهستک امروز به‌صورت کنترل‌شده امحا می‌شود و احتمال شنیده‌شدن صدای انفجار وجود دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/alonews/140944" target="_blank">📅 15:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140943">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
به گزارش بلومبرگ، شرکت ادنوک امارات در حال بررسی ساخت پایگاهی برای صادرات گاز طبیعی مایع در مسیری خارج از تنگه هرمز در ساحل شرقی این کشور است؛ زیرا جریان انتقال آن ماه‌هاست مختل شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/alonews/140943" target="_blank">📅 15:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140942">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
واکنش بقایی به حرف ترامپ که گفته بود مذاکرات چراغ خاموش و مثل یه بازی شطرنج داره جلو میره: به هر حال چه چراغ خاموش و چه چراغ روشن، ایرانی‌ها شطرنج‌بازان مطرحی هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/alonews/140942" target="_blank">📅 14:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140941">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/trXSok7Vc9XD9qLCjp9TwmMMUqFqV0FCqN8mxDlIrNJRLII1ScxKYloIuTQKnZxdMGTMyBMS2j6GDgc0ZeM1WP9VDYuAFvm3rIXbEcROKcN63CrWSaZAMYLjhRWAn4ekscHz1S1Ze41IglkIZdQYSz6H79i_oFrUkwEGQdl9OXLCtttYqOZeV-GVSIUbM0R9EsvpmRG18uOLy8_KQhBV3fEF4Lue1nzSAQ0RrjE6i9lla1fZJxZBo0IwrRThgnucUcQfvsD9uMeyqMvntur9jGz0l_07lV0hleW4_uI3hvlk7LgtQ1BAKgVSdkk0IDX4BOU2LxZ_y_TsJeQh2iBlvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جرجیا ملونی، نخست‌وزیر ایتالیا، در آستانه انتخابات که احتمالاً در بهار آینده برگزار خواهد شد، با افزایش چالش‌ها از جناح راست، لحن تندتری در مسائل مربوط به مهاجرت، امنیت مرزی و هویت ملی اتخاذ کرده است، به گزارش نشریه پولیتیکو
🔴
حزب "آینده ملی" که توسط ژنرال بازنشسته روبرتو واناکی اداره می‌شود، با کسب بیش از ۷ درصد آرا، تهدیدی برای جذب رای‌دهندگان سنتی جناح راست از ائتلاف ملونی محسوب می‌شود.
🔴
با وجود این مواضع داخلی سخت‌گیرانه‌تر، اختلاف اساسی بین ملونی و واناکی در سیاست خارجی همچنان وجود دارد: ملونی از اوکراین و ائتلاف‌های غربی ایتالیا به شدت حمایت می‌کند، در حالی که واناکی رویکردی ملایم‌تر نسبت به روسیه را ترجیح می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/140941" target="_blank">📅 14:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140940">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88110a2e13.mp4?token=nYLt1HWv_OOiv_Qb90md76c3VuKTWgYpHWjms1hioZNOnitivVfrLPF7Yptz4M77JJ1H27ilGUpHOnsHq7Pa_-zfPIFry-_aOH2dk92ChiN8W9YwuMXeUj6BlNrpLLHNeBKBQi9-5wrX5KvAmwPsqNuhuhIUZEuhyakvg_41p4YI_9XtZyYNEx3IdeQ1neqhDS73AuaZzotK_JKPBdz7fuyy6gvfx-bCzlEuX4CR7q1ARYMpZ1JfGLaddCk5iloFTFCwWnP42_AmCRTDzXBROYuxgrKjV4a3baJEDDB7PvFNXAhW3fzWvuHm5ojDUQesP0VDN3PnCjBDA56jNF6KTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88110a2e13.mp4?token=nYLt1HWv_OOiv_Qb90md76c3VuKTWgYpHWjms1hioZNOnitivVfrLPF7Yptz4M77JJ1H27ilGUpHOnsHq7Pa_-zfPIFry-_aOH2dk92ChiN8W9YwuMXeUj6BlNrpLLHNeBKBQi9-5wrX5KvAmwPsqNuhuhIUZEuhyakvg_41p4YI_9XtZyYNEx3IdeQ1neqhDS73AuaZzotK_JKPBdz7fuyy6gvfx-bCzlEuX4CR7q1ARYMpZ1JfGLaddCk5iloFTFCwWnP42_AmCRTDzXBROYuxgrKjV4a3baJEDDB7PvFNXAhW3fzWvuHm5ojDUQesP0VDN3PnCjBDA56jNF6KTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دستگیری پزشک قلابی عمل‌های زیبایی در شهریار تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/140940" target="_blank">📅 14:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140939">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">👈
قیمت تتر امروز با کاهش، به ۱۸۵/۵۰۰ تومان رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/140939" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140938">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L9flFYgJlWUotwrgdbk-FWlr88skvhJldhMglTmHioA8816Rq197DzFupPX9mBcoi5PLUUu7Km7HeIo69y-oSgtV62luY_A1v6h61wm-ddSLAlqe87_DEwg8f_VGUXJcTN0hy20j_CF7-8MuIH8-FBS_V_eUGjTduBUwVHI4eNFeLoJmNm-n09j5Dtd4jYW70rrCbQDHfZpEt72-WCiEZ-DrDdB_P1G5-2sW4kiZN0LV79yTEgyRbDZ9L_a3rj0hmGTr1i3_N3zvZe22N9a7ERm7L1A1eCJw9w9mlMcARLvYIRABxYGVg2eIURcrxwEHT6hFH4uj6V7Mrxu9i93-Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گردنبندِ ایرانی «گردونه میترا» که در کاوش‌های باستان‌شناسی در کَلورَز گیلان پیدا شده است و دارای قدمت حدود ۳۰۰۰ ساله است. کَلوُرَز، یکی از روستاهای رستم‌آباد در گیلان است و در بخش مرکزی شهرستان رودبار قرار دارد.
🔴
این گردنبند طلایی زیبا دارای سه نمادِ سواستیکا است. و نشان از رواجِ کاربرد نمادِ سواستیکا در ایرانِ باستان دارد.
🔴
سواستیکا (卐 یا 卍) یا گردونه خورشید، یک واژه‌ی سانسکریت است که از دو پارِ "سو" به معنی "نیک" و "استی" به معنی "بودن" ، تشکل شده و معنای «هستی نیک» دارد؛ که در آئینِ مهر، نمادِ خورشید یا در آئینِ هندو نمادِ ایزدِ آفرینش است.
🔴
در فرهنگ هندواروپایی، کاربردِ این نشان بر روی اشیا برای خوش اقبالی و نیک بختی بوده است. استفاده از این نشانِ باستانی برای هزاران سال نه تنها در ایران، بلکه در یونان و سایر تمدن ها متداول بوده‌است.
🔴
متاسفانه به دلیل سوء استفاده حزب ناسیونال سوسیالیستِ آلمان، از نشان سواستیکا، به جایگاه این نماد صدمه زیادی وارد شده است و لازم است تا با جداکردن وجه والای این نمادِ باستانی ایرانی از جنایات حزب نازی آلمان در جنگ جهانی دوم، نشانِ سواستیکا را به عنوانِ یک میراثِ جهانی پس بگیریم و معنای والای آن را بازسازی کنیم.
🔴
این گردنبند باستانی در موزه ملی ایران نگهداری می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/140938" target="_blank">📅 14:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140937">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
ترامپ ۵ میلیارد دلار ثروتمندتر شد
🔴
فوربس برآورد کرده ثروت خالص دونالد ترامپ تا ۸ اوت ۲۰۲۶ به حدود ۶.۵ میلیارد دلار رسیده؛ رقمی که در سال ۱۹۸۹ حدود ۱.۵ میلیارد دلار بود.
🔴
بخش مهمی از ثروت او همچنان از املاک می‌آید، اما در سال‌های اخیر رمزارزها، صدور مجوز بین‌المللی برند و دارایی‌هایی مانند مارئه‌لاگو سهم بیشتری در درآمدش پیدا کرده‌اند.
🔴
مسیر ثروت ترامپ بدون افت نبوده؛ او پس از بحران املاک و افزایش بدهی‌ها در سال ۱۹۹۰ از فهرست میلیاردرهای فوربس خارج شد، اما در ۱۹۹۷ دوباره به آن بازگشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/140937" target="_blank">📅 14:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140936">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frdQyD9orlFyF_hbQVBm7adog6CGhI-ATepOliwFudeuSGS7R8115PDM2fz9HNlzNPuYP_FFmoHMNzT_qR94zPcVSoMCDdjnoRO_jvq8bxwFc65P0dTMPZ5y0CMkmXD0TDlJle3rG2jMX_WOXqLsDUJQixl7dFG0RE6V4w5mjSJurKrFxZTEMKpjIrZT-RaGeXdmQJ_SKPq0sdKjKz_UM0Ju2gB_8N1auVL8RQ3LUtPDK7xjlTZ5gJ7IE2U9i7ZC2IAS-aUil_0VWNaRcUgb3c6o3qAKx97AMD-bWHZ7CTjvrFLWD1a9FymoGKsmKWHJpFgFyNJd6_Q0V3dJuO24IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات سایبری گسترده به بخش های هواپیمایی، انرژی و آموزش کشور امارات
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/alonews/140936" target="_blank">📅 14:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140935">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‏
👈
پزشکیان:  در موضوع بنزین نمی‌توانم دستور بدهم که از فردا فلان اتفاق بیفتد؛ چون ممکن است کشور را دچار مشکل کنیم.
🔴
باید هم در داخل دولت و هم خارج از دولت با دستگاه‌ها و مجموعه‌های مختلف گفت‌وگو کنیم، دغدغه‌های آنها را بدانیم، آنها نیز دغدغه‌های ما را بدانند و در نهایت به یک راه‌حل مشترک برسیم.
🔴
ما تازه به یک تصمیم رسیده بودیم و می‌خواستیم آن را اجرا کنیم که موضوع استیضاح وزرا مطرح شد. اگر وزیر دیگری می‌آمد، دوباره باید با او می‌نشستیم، گفت‌وگو می‌کردیم، مسائل را توضیح می‌دادیم و به زبان مشترک می‌رسیدیم.
🔴
در این صورت، عملاً زمان دولت برای اقدام و اجرا از بین می‌رفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/140935" target="_blank">📅 14:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140934">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان:  چین و روسیه در مجامع بین‌المللی از ظرفیت خود استفاده کرده‌اند و در مواردی قطعنامه‌ها را وتو کرده‌اند.
🔴
حتی در رابطه با قطعنامه‌های مربوط به تنگه هرمز نیز مواضعی اتخاذ شده است.
🔴
در مجموع، تا جایی که آنها امکان دارند و ما نیز می‌توانیم، در حال تعامل و استفاده از ظرفیت‌های موجود هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/alonews/140934" target="_blank">📅 14:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140933">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
رئیس جمهور:  حجم مبادلات ما با پاکستان در حال افزایش است و از حدود سه میلیارد به سمت ۱۰ میلیارد در حال ارتقا است.
🔴
ارتباطی که اکنون شکل گرفته، استثنایی است و قرار است این روند نیز تقویت شود.
🔴
ما اختیار داده‌ایم و اجازه داده‌ایم که دستگاه‌های مختلف مستقیماً با کشورهای همسایه ارتباط داشته باشند و آنها نیز این کار را انجام می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/alonews/140933" target="_blank">📅 14:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140932">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
وزیر ارتباطات درباره خبر «ضریب دار کردن» اینترنت: این موضوع خط قرمز منه اگه این فرضیه اثبات بشه، شخصا برخورد جدی با اون اپراتور می‌کنم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/140932" target="_blank">📅 14:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140931">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAhW_rbLe5dHYByzn5wGYMGIt40Z0d7bdFIwBO2okh9Ij7TAOc3nyM3Qr0VEh6kpztHMQ_LqcTWccGVfwgPeuglj9yB7jaHJ5CX5PzQqFr3QX99XaTVyxGgrqtXJmUk1tjqn-_wK8p0krOrVacGErO1RmBXcphPpUw8fxHSFkT9arR46w1KfEmHn5gcP-wybLUrRCgIxjXQN3O3DimCLxgmGQGy-eci4M0Q8cUPLLrFc62tzyC8lFJyM3gvs52flE3XLzzgxmXkr29BE7To1LF7W_z8iUp5VZddR6UmJ5IYaei-acAtcN242ZOHCikow4NbtQNolQnJBAu5Jm3rIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اوکراین : یه سامانه جنگ الکترونیک ضد استارلینک روسی رو زدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/140931" target="_blank">📅 14:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140930">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سخنگوی دولت عراق: «ما از بمباران مقرهای حشد الشعبی توسط عربستان و آمریکا اطلاعی نداشتیم و یادداشتی را به شورای امنیت سازمان ملل ارائه خواهیم کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/140930" target="_blank">📅 14:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140929">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پسر اسماعیل خطیب: بابام ۴ بار از ترور در رفت، ولی بار پنجم دیگه نشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/alonews/140929" target="_blank">📅 13:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140928">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجار در پاکدشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/alonews/140928" target="_blank">📅 13:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140927">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرگزاری رویترز به نقل از یک مقام آمریکایی گزارش داد که ایالات متحده قصد دارد پس از دستیابی به توافقی برای از سرگیری تردد بدون مانع کشتی‌ها در تنگه هرمز، محاصره بنادر ایران را لغو کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/alonews/140927" target="_blank">📅 13:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140926">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
بلومبرگ: دونالد ترامپ، رئیس جمهور آمریکا، مدعی شد که آماده است به جای حمله نظامی جدید، اجازه دهد فشار اقتصادی بر ایران افزایش یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140926" target="_blank">📅 13:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140925">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/005fed10cc.mp4?token=b6VJiXJt7dkHYhG4myOs-Z_48HQwrgP9478hyep4hLMMLx6uV70Lk5jOVe_-oPzIDMQ-LPhEQ-t1saOMXDRDkqs2xVKSwJQmaSOdj4F9yvwMvi8tCmzC5RY9gmjZ2PhNj-WRzqFuMm2ggvkSY-dOCm-zZ0xixmHzh103kp7Yu9_f2JNTr9olQm3DviQfL-HHSd6NQL93gz4Xsrig6_2JL3yRgYQVx0iYge_diVSlQMESUznK2Udyo4eWnzEiir8PKZJCsatgWH_V-k8N_wfeN5v0gRbbWYizYcmKcl-zTjET1QKErgAh5yqx1gySB7dB_0gBI0kQ30uzUKJdZflwrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/005fed10cc.mp4?token=b6VJiXJt7dkHYhG4myOs-Z_48HQwrgP9478hyep4hLMMLx6uV70Lk5jOVe_-oPzIDMQ-LPhEQ-t1saOMXDRDkqs2xVKSwJQmaSOdj4F9yvwMvi8tCmzC5RY9gmjZ2PhNj-WRzqFuMm2ggvkSY-dOCm-zZ0xixmHzh103kp7Yu9_f2JNTr9olQm3DviQfL-HHSd6NQL93gz4Xsrig6_2JL3yRgYQVx0iYge_diVSlQMESUznK2Udyo4eWnzEiir8PKZJCsatgWH_V-k8N_wfeN5v0gRbbWYizYcmKcl-zTjET1QKErgAh5yqx1gySB7dB_0gBI0kQ30uzUKJdZflwrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صبح امروز و برای بار اول پس از سقوط بشار اسد، جنگنده‌های Su-22 نیروی هوایی سوریه بر فراز مناطقی از جمله ادلب پرواز کردند.
🔴
غیر از هواپیماهای آموزشی-رزمی L-39، این جنگنده‌ها نخستین هواگردهای بال ثابت مسلحی هستند که در دوره دولت جدید سوریه عملیاتی شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140925" target="_blank">📅 13:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140924">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
الجزیره: ممکن است که ترامپ به حامیان خود بگوید «دیگر نیازی به حمایت از اسرائیل نیست»
🔴
الجزیره نوشت: ترامپ در چند مصاحبه اخیر گفته است: «اسرائیلی‌ها به من احترام می‌گذارند و کاری را که می‌گویم انجام می‌دهند» و «من تصمیم می‌گیرم، نتانیاهو تصمیم نمی‌گیرد.» بنابراین ترامپ در واکنش به رد طرح صلح غزه از سوی نتانیاهو، می‌تواند دست به اقدام بزند و به حامیانش بگوید که دیگر نیازی نیست از اسرائیل حمایت کنند. او تقریباً کنترل کاملی بر پایگاه سیاسی ماگا و جمهوری‌خواهان در کنگره دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140924" target="_blank">📅 13:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
نیویورک‌تایمز: تنگه هرمز به «شمشیر داموکلس ایران بر فراز سر ترامپ» تبدیل شده
🔴
مقام‌های ایرانی نگرانند که اگر تنگه باز شود، ترامپ بدون اینکه احساس کند نیازی به حل و فصل این بحران دارد، از آن خارج شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140923" target="_blank">📅 13:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140922">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEXFp7EI5F_uRdzkYY_oJWymowywvitMWtSRiCAiVm1n0gAhcfjVzJIHABS4kykODaqq90Nfk-iAs4sB9nzgLgMlkYthCgZC49W20T3OQO5aZM2FfE698Uz-Yg6j3AFhiDJ9Nvx9dkWCu499M8n4Db65JP78yae3TYWuvZotA6EADKAIhYdXOrL7i1vYoUpZLUX0nLT1IKp8fj5JMVD3TPjCwRPhEGLO-FYnaxxugSiAGu8zkAK2Ft-RmDFnRnr1ByXOZjkbLTk1xSy3JIdTpgM-zF6RE763mwpoYXpYem8MzsxUJh6-7fsU5pkqkjg8lbMDN5kUVbclj4WHGw9BlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رشد ۹۴ هزار واحدی شاخص بورس
🔴
شاخص کل بورس با رشد ۹۴ هزار واحدی در پایان معاملات امروز به ۵ میلیون و ۶۵۴ هزار واحد رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/alonews/140922" target="_blank">📅 13:24 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140921">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
نایب رئیس مجلس: بازگشایی تنگه هرمز هیچ راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/140921" target="_blank">📅 13:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140920">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل:  کاتز، ویدئویی منتشر کرده که توش اسرائیل چند کشور رو بمبارون می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/alonews/140920" target="_blank">📅 13:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140919">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_AWk9KPBvg8kwAhrCyGclvnnvN9qBI7DFd387pa6B01O1fRMsbHJu6BgCr0SSJ14yzubcFVqaplKofofzWA-gQqB7X8G66Wiwk2sxFWkl6MLm5buS8KTak9hL7Vwov1GhLphhGE-M7DEAxlcm25GeLXw5LBKAt0FwFSF5d1GGXZHjZgSWltym9uQNSY1j1g6UtQaKUwKoWDScZDv-3E35H76NKWB_RDAD4WOUvxrO1XgFOQbV0V5XUF2qHkkcRC9-SDltFYckQ5zeJHTU4uBA1PstuqZxLsOyyC1AJY5Hsy7DVG2ESNL3L_T6dg79H27MDl_4bvno1C0RiYJVLiNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزیر امور داخلی عراق: تمامی سلاح ها باید به دولت تحویل داده شود و از این به بعد هر کسی بدون مجوز دولت، پهپاد به پرواز دربیاورد، به عنوان تروریست با او برخورد می شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/140919" target="_blank">📅 13:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140918">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
۶۳ نماینده مجلس به توسعه اختیارات رئیس‌جمهور در فضای مجازی اعتراض کردند
🔴
طبق این اعتراض رئیس جمهور نمی‌تواند هروقت که خواست به قطعی اینترنت پایان دهد و یا برنامه ایی را رفع فیلتر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/140918" target="_blank">📅 13:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140917">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
مایک والتز، سفیر آمریکا در سازمان ملل: ایران بیشتر از اینکه هز وزیر جنگ آمریکا بترسد، از وزیر خزانه داری آمریکا می ترسد، چون او کسی هست که آنها را تحریم می کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/140917" target="_blank">📅 12:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140916">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3eecf6773.mp4?token=de0kRoNIwwjNhTWwpXboz7XIba3MeDbXkfdtiCixEnqOW5ViKvwZO3ulIAG0fWqBnhJyLZt3Wu1NO_U4vQieEbyt8zQxtVZ7fp9Cck0aBBMcauaOLcIG_qAb44LsaZ_0f1xAnrRIai56RFxHnpIT5Vdl9dSCDERX_kc-S7Db7Bpb1w4r492Ia0lC1deW8q01b1UC9Xwe9scHcc0VqCD5kfroICvhacQm9QboIkrhOccBvAAa6wXV6kwbbGYvuAVRo8fTwflLGxk5Xd8GKpZHCU-i3OCcGX3j5pgxXweu7RbV1ht0UzCzGDZy2qKuoph49ECi6TRBV7iFo_RZ16Sj_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3eecf6773.mp4?token=de0kRoNIwwjNhTWwpXboz7XIba3MeDbXkfdtiCixEnqOW5ViKvwZO3ulIAG0fWqBnhJyLZt3Wu1NO_U4vQieEbyt8zQxtVZ7fp9Cck0aBBMcauaOLcIG_qAb44LsaZ_0f1xAnrRIai56RFxHnpIT5Vdl9dSCDERX_kc-S7Db7Bpb1w4r492Ia0lC1deW8q01b1UC9Xwe9scHcc0VqCD5kfroICvhacQm9QboIkrhOccBvAAa6wXV6kwbbGYvuAVRo8fTwflLGxk5Xd8GKpZHCU-i3OCcGX3j5pgxXweu7RbV1ht0UzCzGDZy2qKuoph49ECi6TRBV7iFo_RZ16Sj_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مدیر عامل شرکت توزیع برق: به ازای کشف هر ماینر ۳ میلیون تومان جایزه دریافت کنید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140916" target="_blank">📅 12:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140915">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd3d7d8977.mp4?token=Y5rg4gUOxJGxo3Yps8c7P1cjTwQpWUHOb2pFb4pmMara45B3TllA0Z1XolINtGAUCzzlmuDoEaLJiVPshsTpgohSdVa8jxBFefqQLFHvvlk2jJsHdSN_G6k5fZdqE__gehcwX7jGdk1mCZm0kCDvGsJurCzdhn0Y2SUy6aVXYGztW3Zqv2v_AydDQF4dTaSL6WP1FFl1e7heFR9RGTmJKy_Qvi5dHsln2ZP2ErtdtfAG6EIivh6S1_f7d2aHchSfsOD7U2zQdBLuO6Bte_dR5TJYL1hDaTncI2yKfT_JbhXC_nl4eZyUrahWYZ6xKB6w4stZ2ymBWmKVLJ_F0rF27A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd3d7d8977.mp4?token=Y5rg4gUOxJGxo3Yps8c7P1cjTwQpWUHOb2pFb4pmMara45B3TllA0Z1XolINtGAUCzzlmuDoEaLJiVPshsTpgohSdVa8jxBFefqQLFHvvlk2jJsHdSN_G6k5fZdqE__gehcwX7jGdk1mCZm0kCDvGsJurCzdhn0Y2SUy6aVXYGztW3Zqv2v_AydDQF4dTaSL6WP1FFl1e7heFR9RGTmJKy_Qvi5dHsln2ZP2ErtdtfAG6EIivh6S1_f7d2aHchSfsOD7U2zQdBLuO6Bte_dR5TJYL1hDaTncI2yKfT_JbhXC_nl4eZyUrahWYZ6xKB6w4stZ2ymBWmKVLJ_F0rF27A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برگزاری مراسم اربعین در لندن
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/140915" target="_blank">📅 12:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140914">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a8c9073a.mp4?token=PavfA8qzgajI7iA6T2ZhHgBXvCj0TIsdhqOINYiT162JtS74v4MwVyY3H0KDuzf6LNVs_B7tHJvdvljYoBPDmx92G5weZovAlV0ESM9wL-RCE-NNjvaLDY2cTbjinwTmXjUgrwO9xOxf1ETcfQk7rOevSy0oBAtYY_mdnMbn2jPXIkRuypfzFJxDSjodRHLH5WpYSzNeWdepTV91CcDaHDGl7qdWEIajOlCcbjgmzpx1IyLex3V7xGGc7_hwg8Got7gDge1l37E1APuKsSVj6YoKEn--E6lK3ydteDahUsym7QZf5cwvszUw3VHkCTKCDyocKuBQNOYeTFQvSJE7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a8c9073a.mp4?token=PavfA8qzgajI7iA6T2ZhHgBXvCj0TIsdhqOINYiT162JtS74v4MwVyY3H0KDuzf6LNVs_B7tHJvdvljYoBPDmx92G5weZovAlV0ESM9wL-RCE-NNjvaLDY2cTbjinwTmXjUgrwO9xOxf1ETcfQk7rOevSy0oBAtYY_mdnMbn2jPXIkRuypfzFJxDSjodRHLH5WpYSzNeWdepTV91CcDaHDGl7qdWEIajOlCcbjgmzpx1IyLex3V7xGGc7_hwg8Got7gDge1l37E1APuKsSVj6YoKEn--E6lK3ydteDahUsym7QZf5cwvszUw3VHkCTKCDyocKuBQNOYeTFQvSJE7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجید شاکری، مشاور قالیباف: ترامپ با ما توافق نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140914" target="_blank">📅 12:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140913">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
رئیس سازمان هواشناسی: احتمال وقوع پیوستن پیش بینی ها تا این لحظه ۷۰ درصد است.
🔴
بارش و ترسالی احتمالی سال آینده نمی تواند خشکسالی چند سال گذشته و کمبود منابع آبی را جبران کند.
🔴
مردم خبرها را از مراجع رسمی اطلاع رسانی پیگیری کنند، خیلی از پیش بینی های منتشر شده در فضای مجازی قابل اعتماد نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140913" target="_blank">📅 12:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140912">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
بقائی: ادعای نتانیاهو درباره ماهیت برنامه هسته‌ای ایران دروغ‌پردازی است/ ادعای بمب هسته‌ای ایران دروغی ۳۰ ساله است
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140912" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140911">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6c2ee8a2.mp4?token=tt2aC4x4DqytTLMmBCPcaVYO1eR7huIWnT-5WU2TUPKHJV8boNXMU6kEdRrq4jogp_aXICKpFOa4GNfiOiX75nADAeeEzg1YHBgOPn9hY2L152hgec_HPdFTsrWUbJMp_d-ijAwu3B7sK4QNJHACmmrVZf1y5Rq9B40NYQmSZQe4CTnHoTiu1pGOFmqs0f9wfexEZuzGWE8GATm6fV9KJCLsj1eCh5Bljt4OHXhpXGh6viYbYufgk9xonLTpP1eTT4Ofwe8lNACN_pqlyB4DG43UV-RN_j8ShZDiXlud7GkBGgg8kLldctSoil59tnkrOERgFKSSl2cXKZeGi-grpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6c2ee8a2.mp4?token=tt2aC4x4DqytTLMmBCPcaVYO1eR7huIWnT-5WU2TUPKHJV8boNXMU6kEdRrq4jogp_aXICKpFOa4GNfiOiX75nADAeeEzg1YHBgOPn9hY2L152hgec_HPdFTsrWUbJMp_d-ijAwu3B7sK4QNJHACmmrVZf1y5Rq9B40NYQmSZQe4CTnHoTiu1pGOFmqs0f9wfexEZuzGWE8GATm6fV9KJCLsj1eCh5Bljt4OHXhpXGh6viYbYufgk9xonLTpP1eTT4Ofwe8lNACN_pqlyB4DG43UV-RN_j8ShZDiXlud7GkBGgg8kLldctSoil59tnkrOERgFKSSl2cXKZeGi-grpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تراکم کشتی‌ها در تنگه هرمز کاهش یافته است، به طوری که تنها ۶ کشتی در ۹ آگوست از این تنگه عبور کردند، و بیشتر آن‌ها از مسیر مشخص‌شده توسط ایران استفاده کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140911" target="_blank">📅 12:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140910">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: رفع وضعیت تنگه هرمز مستلزم جبران همه نقض‌های یادداشت تفاهم است که آمریکا در حال انجام آن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/140910" target="_blank">📅 12:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140909">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-Pm9N2kEw_AEC8NZ7Ap3aXfexAqBJzhjqWT0rexccaRO4Dq4DB3ze5YZC1rntWnl-jQ66nBStriZZ0Af2eRUlmkAk-Bd0g4engikAwa4bdwP2oT9lx35VZ390y11JmHc-ZXGWIU__Sm0FgBeYx0UgxlVruwHQ_vHiG1SxkwhnGnrZUHUvnr7SmUxynWTN3Nzvt83T4gcdST_rjOAQ9b-Wlb5a2hvuH7Cl_CNH4eIXkiw5knpNMuofB2VisP4_VRfdL6aWqyKH5oLdE-xRu0Fvdaek4HeU2EanCie0a6b37ngww9SR25qMtHJRixhlXdKmwOoKz6Mz7Gqr2q0M8sVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ۱۳ میلیارد دلار خسارت، صورت‌حساب سنگین حملات ایران برای آمریکا
🔴
از آغاز عملیات «خشم حماسی»، ایران بیش از ۲۰۰۰ حمله هوایی، موشکی و پهپادی به پایگاه‌های آمریکا انجام داده و به ۲۰ سایت در ۸ کشور آسیب زده است. خسارت وارده به تجهیزات و تأسیسات آمریکا ۱۳ میلیارد دلار و ۴۲ هواپیما منهدم یا آسیب دیده است.
🔴
با این حال، آمریکا آمادگی کافی برای دفاع از پایگاه‌های خود را ندارد. گزینه پیش روی کنگره و پنتاگون روشن است: یا حالا برای حفاظت هزینه کنند، یا در آینده با مشکل جدی‌تری روبرو شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140909" target="_blank">📅 12:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140908">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MXlkQ4JvGi0v7jcWr_tK0qUlwoHRbAxJJo9kRIZx8pVEGLAw7mj9siz5wPSGpZQU6JjNDxjtASmooW00wF77iKT9ylB0XlmFeDhuf7coL1PnmC7kzeRqJRGT6Rt0Xazrsys1OangnCQo5ZSewYBqXYlKz_x9y1QWKkWCp8P2aNVi4JW1toQJwCuLGEZ484NerZNMm6duQHJXdAm4PWuOnuw8BsNmj5yMBS5vaH1InT-uys4KFRmNRZAbiT3TYceUFJf46rzr5zA-kggpnOlbpAKPbvgwKpPBWLceqJ8rLa51CzhBOjGvOqiFMMEu5oN9Fl0UAdXcG1Kxl-xPG6tGqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حضور محمود احمدی‌نژاد در جلسه دیروز مجمع تشخیص مصلحت نظام
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140908" target="_blank">📅 12:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140907">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: به هیچ گزارشی، چه مثبت و چه منفی، در مورد میزان توانمندی نظامی آمریکا اعتبار نمی‌دهیم
🔴
موضوع مهم برای ایران حفظ آمادگی خود در بالاترین سطح است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140907" target="_blank">📅 12:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140906">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
سی‌ان‌ان: شروط ایران برای بازگشایی تنگه هرمز قیمت نفت را افزایش داد؛ برنت به ۸۴.۵۸ و نفت آمریکا به ۷۹.۲۸ دلار رسید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140906" target="_blank">📅 12:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140905">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
یک مقام ارشد اسرائیلی گفت به کانال ۱۲: هیچ شانسی وجود نداره که ما اجازه بدیم قطر و ترکیه به عملکرد ما تو غزه نظارت داشته باشند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140905" target="_blank">📅 12:01 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140904">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=rHkaDW1Q9rHbXeEA2aVdCx_TEdGeFxJA0l2KyhYkA7g4vmH0HKziEyAoTBwZUCB1IlyxuAWB9K5Y3PyC4gfm6CzmQhM-vZdeRcEvMhHLRFp94hYOE8yYJ90yIjE_Nmgxcbxq05SV2trKPOSnMcOAcuMI4ZT4ziV5CC1jOzi4F_FECylObeG9zuiuX3Yc_5blNMa0cKfk5XlSGg_xA7SGSrem0dQP8bUEZhg_xyX6gaEUZzqnnBiU3-YMqRUg4gLEaFy0--jnqJl5HpxcS5no5zh3uwOf0x71h1ALQgj8qv0c6ZzBLRyWt7VBJUkmSv5CG-oLB-R4PwDpr16CZ4i4VmbUfMmBVLJ0Bnxlu4SmaSZmfV56qvxAJa-4SWO0edJ4GdvuJJCpE4lSeTNoOIrhDAn1sKGGvtLM_JDDSCgfGmFLCuztoHhRB397FettmRp8rlUU1ZfmqPssbfSnlopGaDTH5gNkdec_lj5rC61-CpK-wNnEsWA9NbOgwG-pshPi3KRGiizWK0sBhxHwURFdEMWzZoxXeP3a5Bss0d_SnXAmAWEKfKFnB9iMIQ-b1D7BCFT3XHPdyM9f2CmzZu2nsULA9Q08RvWSPEKcN08dMckkI6JzPo3UDpQFarKK7-Fez0-jkGHRSMd8B_aPz4VIR2ulsWYmkHqZKszkYXwh6cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37165ac1ad.mp4?token=rHkaDW1Q9rHbXeEA2aVdCx_TEdGeFxJA0l2KyhYkA7g4vmH0HKziEyAoTBwZUCB1IlyxuAWB9K5Y3PyC4gfm6CzmQhM-vZdeRcEvMhHLRFp94hYOE8yYJ90yIjE_Nmgxcbxq05SV2trKPOSnMcOAcuMI4ZT4ziV5CC1jOzi4F_FECylObeG9zuiuX3Yc_5blNMa0cKfk5XlSGg_xA7SGSrem0dQP8bUEZhg_xyX6gaEUZzqnnBiU3-YMqRUg4gLEaFy0--jnqJl5HpxcS5no5zh3uwOf0x71h1ALQgj8qv0c6ZzBLRyWt7VBJUkmSv5CG-oLB-R4PwDpr16CZ4i4VmbUfMmBVLJ0Bnxlu4SmaSZmfV56qvxAJa-4SWO0edJ4GdvuJJCpE4lSeTNoOIrhDAn1sKGGvtLM_JDDSCgfGmFLCuztoHhRB397FettmRp8rlUU1ZfmqPssbfSnlopGaDTH5gNkdec_lj5rC61-CpK-wNnEsWA9NbOgwG-pshPi3KRGiizWK0sBhxHwURFdEMWzZoxXeP3a5Bss0d_SnXAmAWEKfKFnB9iMIQ-b1D7BCFT3XHPdyM9f2CmzZu2nsULA9Q08RvWSPEKcN08dMckkI6JzPo3UDpQFarKK7-Fez0-jkGHRSMd8B_aPz4VIR2ulsWYmkHqZKszkYXwh6cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: تنگه هرمز از زمان حضرت آدم تا 9 اسفند 1404 باز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140904" target="_blank">📅 11:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140903">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7feda1ed7d.mp4?token=GYNDuCtq0C9OY9LcDCHDFoGELk_iqM5x_kFu9TR8yO5vr2nBaJ-zBOTYgKI0m1-c9cZyO8kUOgBb4Tok7X2PEyczNEu6iCECsbrXETDo1118PfoOJKauYt9qmo4hiyehpeQsczHExUFzq_VBFp-79vhcQn0EoU0Wbe8fkNvu1j4rwOOHnGnSmsiC1tLFgXOT3xgnzZSqY8x1xlKJyl__0eclZti9iyRbdXehFA_D_KJ4OoWUZxHkYcUYQHNOtNplIhWcr5_kEJqu1GYHM2VsCoiJzhx-sCOfCpm-Gshx1Ar-GeFpzADSAlNX8egfdJ-LDDxNeLiS4oDE15w06ZTwcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7feda1ed7d.mp4?token=GYNDuCtq0C9OY9LcDCHDFoGELk_iqM5x_kFu9TR8yO5vr2nBaJ-zBOTYgKI0m1-c9cZyO8kUOgBb4Tok7X2PEyczNEu6iCECsbrXETDo1118PfoOJKauYt9qmo4hiyehpeQsczHExUFzq_VBFp-79vhcQn0EoU0Wbe8fkNvu1j4rwOOHnGnSmsiC1tLFgXOT3xgnzZSqY8x1xlKJyl__0eclZti9iyRbdXehFA_D_KJ4OoWUZxHkYcUYQHNOtNplIhWcr5_kEJqu1GYHM2VsCoiJzhx-sCOfCpm-Gshx1Ar-GeFpzADSAlNX8egfdJ-LDDxNeLiS4oDE15w06ZTwcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی در پاسخ به ترامپ که گفته بود «داریم با ایران چراغ خاموش پیش می‌رویم و مثل بازی شطرنج است»: چه چراغ خاموش و چه چراغ روشن؛ ایرانیان نشان داده‌اند که شطرنج‌بازانی حرفه‌ای هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140903" target="_blank">📅 11:47 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140902">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
سخنگوی وزارت امور خارجه: دعوت‌نامه‌ای برای سفر آقایان عراقچی و قالیباف برای سفر به پاکستان واصل شده و هر وقت که زمینه مناسب باشد این سفر انجام خواهد شد.
🔴
اوکراین باید اقداماتش علیه ایران را جبران کند در غیر این صورت ما جبران خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140902" target="_blank">📅 11:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140901">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/32938bccc0.mp4?token=A-y6OtzKdMfr_aD6JRbon0RkEjVdZ1EtdgqjjrCT_RQTVdqj0RAqFICNA6IKQgYFJK2QJz4FiziTMcrYS5juNA6KMMXFXfJ1aLCMsF_cHRxEDmdcBcUcq_ytI2j8CAi8zkMS1tWZs7Ud7yz9VSWA4OKBAQsof3fELsR7fmum2wkNoDT4o0zAxaqN4pM8PIkXXhpclS8tXb2W_4V3zd-PrEFnPV1ed30BSkdFMenhukCsUUl-accSZKCfR_MAnX3I24jf-i-LZv7Y6rhCdL7STEheyvGy_wFaOzTa5uuD0qN8HqnxvFkeqyaHUiLzcnofhCWBPrlbQQWmBfpR7jaF-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/32938bccc0.mp4?token=A-y6OtzKdMfr_aD6JRbon0RkEjVdZ1EtdgqjjrCT_RQTVdqj0RAqFICNA6IKQgYFJK2QJz4FiziTMcrYS5juNA6KMMXFXfJ1aLCMsF_cHRxEDmdcBcUcq_ytI2j8CAi8zkMS1tWZs7Ud7yz9VSWA4OKBAQsof3fELsR7fmum2wkNoDT4o0zAxaqN4pM8PIkXXhpclS8tXb2W_4V3zd-PrEFnPV1ed30BSkdFMenhukCsUUl-accSZKCfR_MAnX3I24jf-i-LZv7Y6rhCdL7STEheyvGy_wFaOzTa5uuD0qN8HqnxvFkeqyaHUiLzcnofhCWBPrlbQQWmBfpR7jaF-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقایی: دلیلی وجود ندارد که نگران باشیم پیمان سه‌جانبه پاکستان، ترکیه و عربستان علیه ایران باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140901" target="_blank">📅 11:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140900">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8c0fb174.mp4?token=wAG80PF1v-DVZTnXIfksMBYuTj9_y6aZOMOzD-XXI0BkHYLvAjCrJTM4DW22JJOEyKfrU2NrsWgJwrDG7hZXLBnHmSZ2KyfmM9ZUBKkL_Qz_OqeUAGPLJfpxyXfA5-26TcKpcvctjdtMhc_WEq_WIRaQFn3ud-UU51PnVKdoSnu7_kkRQEkuwFBFgXZTzvDuHeqNh5APFIePW6foWKsnaap6Lo-ciHnYoHVsi3R_MBPFruNNJ_ZUTb-uHKRJx9qgue7X0-rkpDXIO7juFe703zVWhCbXuhF9LuNFHf1BbGt9jC8bOxdU75EGFyVeViBkssaAaNN1pk0OjRj2BnDbpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8c0fb174.mp4?token=wAG80PF1v-DVZTnXIfksMBYuTj9_y6aZOMOzD-XXI0BkHYLvAjCrJTM4DW22JJOEyKfrU2NrsWgJwrDG7hZXLBnHmSZ2KyfmM9ZUBKkL_Qz_OqeUAGPLJfpxyXfA5-26TcKpcvctjdtMhc_WEq_WIRaQFn3ud-UU51PnVKdoSnu7_kkRQEkuwFBFgXZTzvDuHeqNh5APFIePW6foWKsnaap6Lo-ciHnYoHVsi3R_MBPFruNNJ_ZUTb-uHKRJx9qgue7X0-rkpDXIO7juFe703zVWhCbXuhF9LuNFHf1BbGt9jC8bOxdU75EGFyVeViBkssaAaNN1pk0OjRj2BnDbpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تهدید یک تروریست به سبک ریگی:
حالا که مداح ما رو شهید کردید؛ از این به بعد هرجا ما شما رو دیدیم میزنیم مبارکمون؛ هرجا شما ما رو دیدید بزنید مبارکتون. ما مثل شما ترسو نیستیم. منه مجتبی اژدری دارم علنا تهدیدتون میکنم هیچ غلطی هم نمیتونید بکنید. این دفعه بیایید خیابون به جان امام شهیدم؛ به جان امامم سید مجتبی یه جوری میزنیمتون که پزشکی قانومی جنازتونو با کاردک هم جمع نکنید. جنازتونم دیگه خاک نمیکنیم؛ میدیم سگا بخورن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140900" target="_blank">📅 11:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140899">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
آکسیوس: کاخ سفید از رد طرح ترامپ برای غزه توسط نتانیاهو ناراحت نشد و آن را بازی انتخاباتی می‌داند.
🔴
یک مقام آمریکایی گفت: «ما نیازهای سیاسی نتانیاهو را درک می‌کنیم. مشکلی با آن نداریم تا زمانی که به آنچه می‌خواهیم عمل کند»، به‌ویژه در مورد مهار حملات. اسرائیل حملات را متوقف کرده و در حال عقب‌نشینی از خط زرد است، در حالی که آمریکا و میانجی‌ها حماس را برای خلع سلاح تحت فشار گذاشته‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/140899" target="_blank">📅 11:21 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140898">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: تصمیم قطعی درباره سفر رئیس‌جمهور به نیویورک برای شرکت در مجمع عمومی سازمان ملل اتخاذ نشده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140898" target="_blank">📅 11:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140897">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
بقائی: بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140897" target="_blank">📅 11:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140896">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
بقائی: بازگشایی تنگه هرمز به لغو محاصره دریایی آمریکا مشروط شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140896" target="_blank">📅 11:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140895">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174bcc983.mp4?token=S0BzPbzKwTeQCurl2gOMdAVzpte2vHSB_6gC3_MhQ0uVplyJrUYZD70EjhuTtCTOuWA1MbrP--WDHlwSuNj_tE6bBtLAXahNH5pcfa6PsFZL3l0a3nbjmbwxWih7zKRESCz_J0nP5qmIPjdn3gLsyki0ejMEI8dn6ZCdzM5RIn9kYzvWBgnJ1YxlVzYD20M2O05t0hlgTSR_-a7R47K_z4LzfpiTinTT0wrQ_A1eWIzsh2eRFZ3ZNz08LVHtPAh9GmU24ngFMnwWNR9jOgZ7jUKnjzlSglYVUeDwBVBG5oCrAnb5vH2QQpduSmyQmTTMGPyUHizAuzapDcg-m1t6QjysgvpegLcJzow1yKyWCEULRioBIc2CUXdtsk4oO22e0_Ou1tRBI9OxjXlw5ju2N9R9r7nyPvd6ivjR0MLDmfAwep20dYVL9v2R7QD89ydYlDgx6Co2PPiTccO7xXnbIkRl4uUuKgz1ioK-0Caind-0ETT6bByOCY0YfHIa5IdexoZ5hHD91jW8DmWe8LP-q8lh8nppEeUr4nQ6_eCYkvzqZztli_9cGkr2WQG1SfC5_DuYzsQNcl9VB0rVnr8dMYDxP0aQqIFKmnqpCIU-ExnUxSvzUymmdycE-9lGydcV2s0_l8qNI3hed_KG9dEVXataTFUGnLuZlqjdA6scHFM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174bcc983.mp4?token=S0BzPbzKwTeQCurl2gOMdAVzpte2vHSB_6gC3_MhQ0uVplyJrUYZD70EjhuTtCTOuWA1MbrP--WDHlwSuNj_tE6bBtLAXahNH5pcfa6PsFZL3l0a3nbjmbwxWih7zKRESCz_J0nP5qmIPjdn3gLsyki0ejMEI8dn6ZCdzM5RIn9kYzvWBgnJ1YxlVzYD20M2O05t0hlgTSR_-a7R47K_z4LzfpiTinTT0wrQ_A1eWIzsh2eRFZ3ZNz08LVHtPAh9GmU24ngFMnwWNR9jOgZ7jUKnjzlSglYVUeDwBVBG5oCrAnb5vH2QQpduSmyQmTTMGPyUHizAuzapDcg-m1t6QjysgvpegLcJzow1yKyWCEULRioBIc2CUXdtsk4oO22e0_Ou1tRBI9OxjXlw5ju2N9R9r7nyPvd6ivjR0MLDmfAwep20dYVL9v2R7QD89ydYlDgx6Co2PPiTccO7xXnbIkRl4uUuKgz1ioK-0Caind-0ETT6bByOCY0YfHIa5IdexoZ5hHD91jW8DmWe8LP-q8lh8nppEeUr4nQ6_eCYkvzqZztli_9cGkr2WQG1SfC5_DuYzsQNcl9VB0rVnr8dMYDxP0aQqIFKmnqpCIU-ExnUxSvzUymmdycE-9lGydcV2s0_l8qNI3hed_KG9dEVXataTFUGnLuZlqjdA6scHFM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بقائی: تصمیم‌گیری نهایی درباره سند دریای خزر به مجلس واگذار شد/الحاق به اسناد بین‌المللی صرفاً بر اساس منافع ملی صورت می‌گیرد
🔴
سخنگوی وزارت امور خارجه:تصمیم‌گیری درباره تصویب و الحاق به اسناد بین‌المللی منحصراً بر اساس منافع و مصالح ملی انجام می‌شود و ارتباط‌دادن آن به تحولات بیرونی توجیهی ندارد.
🔴
سند بین‌المللی دریای خزر (شامل ۵ کشور ساحلی) که در سال ۱۳۹۷ امضا شد، پس از چند سال بررسی همه‌جانبه در نهادهای ذی‌صلاح، جهت بررسی و تصمیم‌گیری به مجلس شورای اسلامی ارسال شده است.
🔴
لازم‌الاجرا شدن این سند مستلزم تصویب و الحاق هر ۵ کشور ساحلی است؛ از این رو تمایل ۴ کشور دیگر برای تسریع در روند اجرایی آن طبیعی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/140895" target="_blank">📅 11:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140894">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b558b46621.mp4?token=oqfRqvVcEzsdYbvyQoL8JgaBVVJPY34G86O63yZ8CHMCxQH7cGQ7lcBO27ZoYwTLiydJZcgjWUfiOEpIzWQb_Oq8zkwLAGgsdKDdqb3jIdK9qk2wd7QGQs8rb33MJgX1AZQyjMlFLjZV9z-PDEICpa_RXecHEjosmlDLSpXkZwJDchci1q2Pyu2VpPPiCw1u3Shon1CyH3avq_slGkK1TiKxzn2vTJqUBBM51WrDqKMaCAT-GpaAQA1fyHLpuvXOJs8j7plToUsjg0y0l-F9r2l3PzGhvrdQmGYvevqzDpbBOQCa-Rl9RdpcR6ODstrRETTCMA0xRUsWxeIQoCR6TT8UZ9SedW_9NFUqstR4PxoCLYsovxKLhTWd1KBLSnXx38KqQ8yasMOn-0AhilyEh1Jlsp014XSb8rKi3gojUTM9LdPSvRByA57aKN5Lth6GJRZjWhQlc1pZbMX7wWiMTBEbuK3btFvOT1QWiL8oRy3z5BO09QcDTRUOLIOF8TbvF8jZIK4X1_lS8GjKlB6W5Wl9arRcuPPs79CFjnhDRf_OqzR8hh1t7G9i9hMj39llzEcxr_8qtAOQgtY6-2SzxbYl_VZbYVk7sceDILLex8NDeYwWHEhR-JFG3C7Oq2tzBDuVvY3g7W7vZZt4DeaYSS0Nc92gGq5TWGRN36e_iAc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b558b46621.mp4?token=oqfRqvVcEzsdYbvyQoL8JgaBVVJPY34G86O63yZ8CHMCxQH7cGQ7lcBO27ZoYwTLiydJZcgjWUfiOEpIzWQb_Oq8zkwLAGgsdKDdqb3jIdK9qk2wd7QGQs8rb33MJgX1AZQyjMlFLjZV9z-PDEICpa_RXecHEjosmlDLSpXkZwJDchci1q2Pyu2VpPPiCw1u3Shon1CyH3avq_slGkK1TiKxzn2vTJqUBBM51WrDqKMaCAT-GpaAQA1fyHLpuvXOJs8j7plToUsjg0y0l-F9r2l3PzGhvrdQmGYvevqzDpbBOQCa-Rl9RdpcR6ODstrRETTCMA0xRUsWxeIQoCR6TT8UZ9SedW_9NFUqstR4PxoCLYsovxKLhTWd1KBLSnXx38KqQ8yasMOn-0AhilyEh1Jlsp014XSb8rKi3gojUTM9LdPSvRByA57aKN5Lth6GJRZjWhQlc1pZbMX7wWiMTBEbuK3btFvOT1QWiL8oRy3z5BO09QcDTRUOLIOF8TbvF8jZIK4X1_lS8GjKlB6W5Wl9arRcuPPs79CFjnhDRf_OqzR8hh1t7G9i9hMj39llzEcxr_8qtAOQgtY6-2SzxbYl_VZbYVk7sceDILLex8NDeYwWHEhR-JFG3C7Oq2tzBDuVvY3g7W7vZZt4DeaYSS0Nc92gGq5TWGRN36e_iAc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
واکنش سخنگوی وزارت خارجه به پیمان دفاعی مکه
‏
🔴
تفاهم‌نامه سه جانبه امنیتی میان پاکستان ترکیه و عربستان سعودی نشانه تغییر در ادراک کشورهای منطقه است؛ کشورهای منطقه با توجه به تحولات دو سه سال اخیر دریافتند که «امنیت» کالایی قابل خریداری از دلالان دروغین نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/140894" target="_blank">📅 11:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140892">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fbac70904.mp4?token=iyYH6OwfknX_w4geA-xWTetuc6zM8NvTDqFtaTg6udFax1rpwCBAU-eXDMMRWmh0a9akU3kAesQ-dUghfvpbxROiGgOBsbhWIbGO7xMNL0HFupyj81HNz74f1uQVZYqNpFMJD6mbtD_0cBNJlpKO8zIOFS89L36MxMRMTbS0OKtx6IRAhePkBUfUSlVE4jx84G86pfYwiOoReiCnU55lp_Kty-598qCpSLtYpj3XTDPztZUBWq3UHThfB8ZGh9WhpHmmo3tmMi16H42Q2JzhxCTxkltEIOsP7qK6V81IB7ihTe6qBR5VdLErEvMg64FlXxYzGeSuN6FyUJVIDVrIbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fbac70904.mp4?token=iyYH6OwfknX_w4geA-xWTetuc6zM8NvTDqFtaTg6udFax1rpwCBAU-eXDMMRWmh0a9akU3kAesQ-dUghfvpbxROiGgOBsbhWIbGO7xMNL0HFupyj81HNz74f1uQVZYqNpFMJD6mbtD_0cBNJlpKO8zIOFS89L36MxMRMTbS0OKtx6IRAhePkBUfUSlVE4jx84G86pfYwiOoReiCnU55lp_Kty-598qCpSLtYpj3XTDPztZUBWq3UHThfB8ZGh9WhpHmmo3tmMi16H42Q2JzhxCTxkltEIOsP7qK6V81IB7ihTe6qBR5VdLErEvMg64FlXxYzGeSuN6FyUJVIDVrIbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پهپادهای اوکراین، یه پالایشگاه مهم تو تاتارستان روسیه رو زدند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/140892" target="_blank">📅 10:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140891">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZkXuf294WW4ISwDTAQX2_kSs5M-qdGwjosMM4f7rtfFK5EUUJzUZkkW_Rann3AWCC4lmyFEkMbLSgzvh3dz2PdDCCkYinmnA1sqSYyEOKGrO-NLlBHH0sl0RiMrVXgVlWXQpg6xSs_RGrdTBVYN0j6qASCjKBD3Ra5xPJaILXZimE5oiZGuhB8ZGbupqc8HkfiviMlqnBi1hvNFoUMw8xaJJUXFSfiv-YvuyMqlLRQMjqQaa1OxZf_3d_BSxvoxm7LGUiu6RH2MtCkP_u24Qym5q0TWF0Av34CN5ROoN-cVfKDURZ4BWV60a8ZmOiz52pZIJ0wuEp9oG377D10jzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک فروند هواپیمای جدید هشدار زودهنگام آمریکایی E-3B از آلمان به پرواز درآمده و در حال حرکت به‌سوی پایگاه هوایی شاهزاده سلطان در عربستان سعودی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/alonews/140891" target="_blank">📅 10:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140890">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
باراک راوید، خبرنگارآکسیوس: کاخ سفید مخالفت نتانیاهو با طرح صلح غزه را بخشی از فضای انتخاباتی می‌داند و نگران آن نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/140890" target="_blank">📅 10:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140889">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
الجزیره مطرح کرده در صورت ادامه مخالفت نتانیاهو با طرح صلح غزه، ترامپ ممکن است به هواداران خود پیام دهد که «دیگر نیازی به حمایت از اسرائیل نیست».
🔴
به نوشته این شبکه، نفوذ گسترده ترامپ بر پایگاه سیاسی «ماگا» و جمهوری‌خواهان کنگره می‌تواند چنین چرخشی را به اهرم فشار قدرتمندی علیه نتانیاهو تبدیل کند.
🔴
اختلاف بر سر غزه، در این صورت می‌تواند از تنش میان دو دولت فراتر برود و به رابطه سنتی جمهوری‌خواهان آمریکا با اسرائیل سرایت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140889" target="_blank">📅 10:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YoCKuH2VqdZrxaLD9n9dHfBhGdDxw-_y43O02e6zKALnVmFf2XJ9pPdlKDP7RRWN8COkfQFwizi3mb14S1j5PSxc4qCzIrBwXWuDyvMXXurPQtQp36mufyxxb6q-HGW44Ux4THzRXDiK4ccpr4DBoGvc-s_qz2Nm2_ZjiMkVqbrEznRnYvJSxu4x_shIKS62pV4rR76JZwAVelsGpeVraQ8dZIlkEvUZUhiYxJLpjV7NibFNI9vDI75So2V10tMpvl6Q9LeONRcpqdzDeaNC22IKR8PH5q22bJjGYbfrBGUMGpcktfC_Q7FOVIfjzjUGqgGmM5EzOtRSPvnzAEtp4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ouYLVt4VJ0YiP9nrKMmk0vaTo9OlPJlgQPgzKSEMzhKDACmRk3UyHVDNVWwmWw1d0CIf4eJIRMTq0Gf2qgXzvU1Tk655KMTB-LYinvf3mxArz3j2e7LtpwOamLGUAXcn4_J_dKcc3-mk4A1A1Yyh6eWZeiuyGSme2rt2jdY0dn-VBtIYBnIgH9PxD3KskwqF6vPw-eWNzOZ1v0YEeFI83q-g2juhMzgkWmAGcwMvb4Mo7uJP4t8oF1XVFi9-mH6k7eHHoA4FnX2MLZuV4sd92iB5lq8w8Kt40cML0IsY2hwAaTtzn_6NHRpP8CjgKdQNZzM-Czs6njYi7P4dcuxRMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
معامله‌گران در پلتفرم Polymarket احتمال پایان محاصره دریایی ایران را تا ۳۰ سپتامبر ۲۰۲۶، ۶۶ درصد و تا ۳۰ دسامبر، ۸۳ درصد برآورد کرده‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140887" target="_blank">📅 10:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
سپاه اصفهان از احتمال شنیده شدن صدای انفجار کنترل‌شده مهمات در حوالی این شهر خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140886" target="_blank">📅 10:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140885">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
پزشکیان: عراقچی اگه شبا خوابش نیاد، تا ساعت دو سه نصف شب تلفن میزنه و جواب تلفن میده، چون روز و شب ما و اونا (آمریکا) برعکسه، عراقچی بعضی اوقات نصف شبا هم کار می کنه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140885" target="_blank">📅 10:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140884">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639af17896.mp4?token=qGJJ8WkhBaBqUTNvH4MiRFHMqnl1IwM5Hd5HpQXV6IYDqzQ5E4Pw_W2ntOTEAV5mJBNBqB3pUDuVvm1jiCzmZwSrMkIFJIFzqrsJgZ6UBAGB7b9WRGu3AB1AUa83sd29FlCUZ-fENy0Yi8uQRB6LtHL-sxS5ekwdI6M4IqSUA0dovYr1zwWi-C4m4GTXkvWSgq7Jpk-rZqQBfR23X23VFufVFmVPefw5ItSQjlCo-66CkKFChCVQA0luFlE8jD2tppUr-M9x_pp1uMn39Bzur3KnT3IP_t68TP2TC0gZv0JOJcSamKrj-q5TKL9auELWUTymnipIqm37WAQay9cwuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639af17896.mp4?token=qGJJ8WkhBaBqUTNvH4MiRFHMqnl1IwM5Hd5HpQXV6IYDqzQ5E4Pw_W2ntOTEAV5mJBNBqB3pUDuVvm1jiCzmZwSrMkIFJIFzqrsJgZ6UBAGB7b9WRGu3AB1AUa83sd29FlCUZ-fENy0Yi8uQRB6LtHL-sxS5ekwdI6M4IqSUA0dovYr1zwWi-C4m4GTXkvWSgq7Jpk-rZqQBfR23X23VFufVFmVPefw5ItSQjlCo-66CkKFChCVQA0luFlE8jD2tppUr-M9x_pp1uMn39Bzur3KnT3IP_t68TP2TC0gZv0JOJcSamKrj-q5TKL9auELWUTymnipIqm37WAQay9cwuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای، خسارات وارده به یک پایگاه نظامی آمریکایی در حسکه، سوریه، را در پی حملات ایران در جریان جنگ نشان می‌دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/140884" target="_blank">📅 10:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140883">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzUu_c2IjrM5Yp8UcpppmtLhup1SBLv8kZEktKCcw6E_48CQ8sLovJXc3A-tB4hcWmVZJ_uxy8i7eFbhxmc9Yup4rRT6g9skAlN-RUAhlEhpjBaiX_CXrYb4B6KIjyogZLsJwTUyUEXAmFhdch5gCm470f5_2ESiohdqia_11Fq9ThtCWFBs5V3z--2_5ILn9ts22IVsPJYUjYu58XHxnMsyukodzJRFckTlrn5AHXv3G1SQifbk2SlJ9WYcWd7ImOhjxe7W6vaaBiMqKi5pke6FxgdMcJFb-Tt5sbPaaT4G3YMPXIo4YS0twxLvbIhXTMY8BmEKh4WSo6F5SxvASQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در مجدل زون، جنوب لبنان، به دنبال فعالیت‌های تخریبی اسرائیل، انفجاری مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140883" target="_blank">📅 09:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140880">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f202621736.mp4?token=PBHkrYfbk90Bmv4ILMQAjYgcDuG-0PvgcAqNOqrwUL_ua1tJ4W2T-bm05QQBqpYCcv6lgNYsAm3JQaeU5OTOkzkOj7d21JEDr_iMbwLnSFFNLxFgs3DKjSzTmp_uUPOKvkL9ncvIWoTz4SsAJzbhhpxIhHumsEK6TSVqj1rhOp5VHVSne3Lz4JmibJSkuZdVxcBQ_PDJ2nbR-URg7tO8ht0FjE0PJmbuo1ncJunG0cYq85EooVyPmSZPr3R6YOWsv4aa8bzoJayG_V55qGYNOVFFGsL4eBFInvLR03mBMvzLs-wqyVoMwBj1if6N8X8yHJvUIWHZY5kTcl0kn_pyww" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f202621736.mp4?token=PBHkrYfbk90Bmv4ILMQAjYgcDuG-0PvgcAqNOqrwUL_ua1tJ4W2T-bm05QQBqpYCcv6lgNYsAm3JQaeU5OTOkzkOj7d21JEDr_iMbwLnSFFNLxFgs3DKjSzTmp_uUPOKvkL9ncvIWoTz4SsAJzbhhpxIhHumsEK6TSVqj1rhOp5VHVSne3Lz4JmibJSkuZdVxcBQ_PDJ2nbR-URg7tO8ht0FjE0PJmbuo1ncJunG0cYq85EooVyPmSZPr3R6YOWsv4aa8bzoJayG_V55qGYNOVFFGsL4eBFInvLR03mBMvzLs-wqyVoMwBj1if6N8X8yHJvUIWHZY5kTcl0kn_pyww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
از ساعت ۳ بعدازظهر به وقت کلمبیا، درگیری‌های شدیدی میان نیروهای ارتش و گروه‌های منشعب از فارک در مناطق روستایی ال تامبو، در نزدیکی مرز با کاخیبیو در استان کائوکا ادامه داشته است.
🔴
گزارش‌ها حاکی از آن است که غیرنظامیان نیز در میان درگیری‌ها گرفتار شده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/140880" target="_blank">📅 09:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140879">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت دفاع روسیه: پدافند هوایی ۴۵۶ پهپاد اوکراینی را در طول شب سرنگون کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140879" target="_blank">📅 09:48 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140878">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
الجزیره: در بحبوحه تلاش‌های ظاهری دولت نتانیاهو برای تثبیت قدرت خود در انتخابات ۲۷ اکتبر، نگرانی‌ها درباره آینده دموکراسی در اسرائیل افزایش یافته
🔴
نظرسنجی مؤسسه دموکراسی اسرائیل نشان داد که تقریباً سه‌ چهارم یهودیان اسرائیلی، درباره سلامت و تمامیت انتخابات ۲۰۲۶ ابراز نگرانی کرده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140878" target="_blank">📅 09:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140877">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=F_Ts9EvPlBNecXdbQRL6b5WvrSLLb4TY-Mh4VBKGslRBAdmAWOxjXahz-VCX8ekEYtBEhu1cGRE2vSTYDNvPme6xbLZtSniJhZwWawalPsPwtUF8BSuxKs6Y6q58HuBJV9XuVIoGJwwks32MqdNvy2xkoQbAYr8jV5fewujCIUJlng5cC_AvuJwNBF-0x2a9v6TMT1pyFIlzsTfxUxsttKIba_SEm6_eawraF1ofuDQm5zF3zHgG1NJxaFY4jb3nACDhbpdFtguO66WGJ5Gw591WamjpDzBhnyDfQAsgqxkpEhjbO2c-GSO1SGm875lcRhmIl57Yw0XRd1vsvyzbfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e68930a72.mp4?token=F_Ts9EvPlBNecXdbQRL6b5WvrSLLb4TY-Mh4VBKGslRBAdmAWOxjXahz-VCX8ekEYtBEhu1cGRE2vSTYDNvPme6xbLZtSniJhZwWawalPsPwtUF8BSuxKs6Y6q58HuBJV9XuVIoGJwwks32MqdNvy2xkoQbAYr8jV5fewujCIUJlng5cC_AvuJwNBF-0x2a9v6TMT1pyFIlzsTfxUxsttKIba_SEm6_eawraF1ofuDQm5zF3zHgG1NJxaFY4jb3nACDhbpdFtguO66WGJ5Gw591WamjpDzBhnyDfQAsgqxkpEhjbO2c-GSO1SGm875lcRhmIl57Yw0XRd1vsvyzbfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مردی روستایی در چین این بازوی مکانیکی غول‌پیکر را فقط با ضایعات فولادی و کار دستی ساخته؛ بدون هیچ پرینتر سه‌بعدی یا تجهیزات پیشرفته!
✅
@AloNsws</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/140877" target="_blank">📅 09:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140876">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd1d57d3f5.mp4?token=V-EWam6n0RJNWSNmewQvlaapVgLeEIFlEzoRlXDtXfarlzron01aUhts4gUKOXEyf28PP3E9Nwp1CGeRUgwHz0kbtqlissmrTlo3HWLWgRqZSA9PUjE8XQvXlt9j5E8IFHj5p5cP1btGLmlZZBVj2j5plfKxgxygNcQHwdXkIRX7OZsrEjgTekpJBkJxY9a1wx168iltVMQeGMKDAbY1N4wzXYpav0Hf52--AQE-Qz6dxTIeRceCQIksCRJR3Setr3tNqdNp2bR9emrO5nDPkLulZGPyaV4IOTlIXpGeHDYdIuQgD5svhdu7eTROH7pGF1iqOuhMUNQJA1JHlXJ0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd1d57d3f5.mp4?token=V-EWam6n0RJNWSNmewQvlaapVgLeEIFlEzoRlXDtXfarlzron01aUhts4gUKOXEyf28PP3E9Nwp1CGeRUgwHz0kbtqlissmrTlo3HWLWgRqZSA9PUjE8XQvXlt9j5E8IFHj5p5cP1btGLmlZZBVj2j5plfKxgxygNcQHwdXkIRX7OZsrEjgTekpJBkJxY9a1wx168iltVMQeGMKDAbY1N4wzXYpav0Hf52--AQE-Qz6dxTIeRceCQIksCRJR3Setr3tNqdNp2bR9emrO5nDPkLulZGPyaV4IOTlIXpGeHDYdIuQgD5svhdu7eTROH7pGF1iqOuhMUNQJA1JHlXJ0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گلوله‌باران توپخانه‌ای اسرائیل در جنوب لبنان همچنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/140876" target="_blank">📅 09:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140875">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dffbdce4c3.mp4?token=tLYJZTvOU78ALY0Jvtb96l596IwG5RtZVOP8q7prH0bOu-ZDMpHKUiryXS7NraxnL7eaQQMb3PkTlwXo3ImY-W8nVTkAWPruvQfeuI4htrRS_nSNXUSIYKCpa_W3U6FxokjEamp01U8WFz0Vu4VZWyY21gX0ICjEkdX7CW0wik5J7Lo08Ergxvu-t0d1cJTf9lzqzA2wZJw1Ca0MAUecVfCVg88UcEW8gcEdg8sXc9CHLRTbIY8NxMAymep-N62ufJL090HejdrM6DXRmo_9c6xq9NAHjGwJmrzSSdKNJucShHugwrxp0yodTuz2KM_kMeCcIRy2mZv83KTbeR795w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dffbdce4c3.mp4?token=tLYJZTvOU78ALY0Jvtb96l596IwG5RtZVOP8q7prH0bOu-ZDMpHKUiryXS7NraxnL7eaQQMb3PkTlwXo3ImY-W8nVTkAWPruvQfeuI4htrRS_nSNXUSIYKCpa_W3U6FxokjEamp01U8WFz0Vu4VZWyY21gX0ICjEkdX7CW0wik5J7Lo08Ergxvu-t0d1cJTf9lzqzA2wZJw1Ca0MAUecVfCVg88UcEW8gcEdg8sXc9CHLRTbIY8NxMAymep-N62ufJL090HejdrM6DXRmo_9c6xq9NAHjGwJmrzSSdKNJucShHugwrxp0yodTuz2KM_kMeCcIRy2mZv83KTbeR795w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخی منابع عربی با انتشار این ویدئو از هدف قرارگرفتن یک کشتی متخلف در نزدیکی سواحل عمان خبر می‌دهند
🔴
شبکه راشاتودی گزارش داد، شعله‌های
آتش از فواصلی دور بر فراز آب‌های عمان قابل مشاهده است اما علت آن هنوز مشخص نیست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/140875" target="_blank">📅 09:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140874">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
احتمال شنیدن صدای انفجارهای کنترل‌شده در خارج از محدوده شهری دزفول
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/140874" target="_blank">📅 09:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140873">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رویترز: قیمت نفت در شرایطی که همچنان درباره بازگشایی تنگه هرمز ابهام وجود دارد، افزایش یافت
🔴
نفت برنت ۹۱ سنت بالا رفت و به ۸۴ دلار و ۴۶ سنت در هر بشکه رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140873" target="_blank">📅 09:11 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140872">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
سنتکام: در چارچوب محاصره ایران، مسیر ۵۵ کشتی تجاری را تغییر دادیم
🔴
فرماندهی مرکزی ارتش آمریکا مدعی تغییر مسیر بیش از ۵۰ کشتی تجاری در آب‌های خلیج فارس در چارچوب اقدام این کشور برای محاصره دریایی ایران شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/140872" target="_blank">📅 09:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140871">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKktVCz2ijxx8gnWOF4ZJhsL0FV9iMZl7UQhnWkwCbhCWEbvHE22hQWmTrCE8rBOSUN2v9h-4H96pz4hYafZmRNNmE8vYa0It1vAN9dHrafIxPa1pF3kA7oYNeLSiOPDndZ7GlFPaz41qPaOmirF7sFBBbsFB_JBOjcX57tH0f4snHwvwiMK_XCNHUNUSAefQ-OF4wOLHyhlkHfY0xkGg500b0BS9UOug0_qGvcrCyKIuxt4D-eRdHyKkqVedoC5NkVqLYNi6XiLTcDQDSmOszjj-rU52AJnvPQyviQI-nmZUNxS6Nx4NAtxB1iwfVBxO6rsAbUf-m3YKr4qhsAY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت تتر
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/140871" target="_blank">📅 09:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140870">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e48ea88a19.mp4?token=aTFDw2omLOfgLUO65w4mqdsX6aaFJ3Hmj7vok5TvxUQxmxi7SC5pv0BIG8PqY0LcfUDLgo2lqaa6pTcksk5NZAS1b4CMVthtQmgv8qpFJulqwNek_01W7y7Up2A6baWjhkPWU0dTCODqOuulRbw1xVKP_d567oq6bHiWFdhd5IfJIHoQQyyN4yq7C1REYNQTU1AYMPhlV1TUvjIxIznJuGY60bqv8SKCYguNkvB6625EDGaIyQWs43x2NP2fO9kXEjRQD2ZVJbmSzm6EyiulhRwVhTxx17aYz-fBUkYtfh1IWIEutEK1oFfUc6ri6WdgOyvgY0saU48Xjx0foB2SqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e48ea88a19.mp4?token=aTFDw2omLOfgLUO65w4mqdsX6aaFJ3Hmj7vok5TvxUQxmxi7SC5pv0BIG8PqY0LcfUDLgo2lqaa6pTcksk5NZAS1b4CMVthtQmgv8qpFJulqwNek_01W7y7Up2A6baWjhkPWU0dTCODqOuulRbw1xVKP_d567oq6bHiWFdhd5IfJIHoQQyyN4yq7C1REYNQTU1AYMPhlV1TUvjIxIznJuGY60bqv8SKCYguNkvB6625EDGaIyQWs43x2NP2fO9kXEjRQD2ZVJbmSzm6EyiulhRwVhTxx17aYz-fBUkYtfh1IWIEutEK1oFfUc6ri6WdgOyvgY0saU48Xjx0foB2SqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
برخورد نزدیک دو هواپیما در فرودگاه سیدنی
🔴
یک فروند هواپیمای شرکت جت‌استار در فرودگاه سیدنی استرالیا برای جلوگیری از برخورد با یک هواپیمای قطری که توسط یدک‌کش در حال جابه‌جایی بود، مجبور شد ناگهان ترمز کند. دو هواپیما در فاصله‌ای بسیار نزدیک از یکدیگر متوقف شدند.
🔴
در این حادثه یک عضو خدمه جت‌استار بر اثر توقف شدید هواپیما زخمی شد، اما هیچ‌یک از مسافران آسیب ندیدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/140870" target="_blank">📅 08:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140869">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
الجزیره: ذخایر موشکی و سامانه‌های دفاع ضد موشکی ایالات متحده به شدت کاهش یافته
🔴
این کاهش به نگرانی جدی برای ارتش ایالات متحده تبدیل شده، زیرا نیاز به حفظ توان کافی برای مقابله با چالش‌هایی فراتر از خاورمیانه دارد
🔴
وضعیت ذخایر نظامی ممکن است بر گزینه‌های واشنگتن در برابر تشدید تنش جدید و [احتمالی] با ایران تأثیر بگذارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/140869" target="_blank">📅 08:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140868">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgYiFx7Tojsu95-OmB1kzQxy4_a30Hr0BR8WrT3iGmuBoXYyi6y8VoO1PsWYIMiOtWqsr-dKmjkIzZkARnaSsNrJrUvrpIoltNWmVJwTCNA15GH8KsHrlHYFjmlQ2Isf0EYEjfRi3zzUP1u0PdrOeTGop6Md2SvXcf9ykXaD4pyLHvlPwwugNcwmEaBVGUQH2QKm-XsN87C5Xee6NJySbuXtGTs18tP-mFUTqwE3SMaPqWBi8jzTPoNsr7jP0hQo9X1WdIMtdiZ94n16mTRGd0N3KfLShfS5AZ5xwpTFhYO0T4TzOOd8Lb5cbxnYvUZsH9KoLJ_aoVo9rTexsQmgnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در پی حملات نیروهای مسلح یمن؛ عربستان همچنان پروازهای فرودگاه‌های جیزان، نجران و ابها را تا اطلاع ثانوی به تعویق انداخت و این فرودگاه‌ها بسته خواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/140868" target="_blank">📅 08:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140867">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
رسانه‌های اسراییلی به نقل از منابع سیاسی:  بروز اختلافات میان آمریکا و اسرائیل بر سر سند ۱۵ ماده‌ای درباره نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/140867" target="_blank">📅 08:46 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140866">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اسرائیل هیوم به نقل از منابع نزدیک به نتانیاهو: ما وارد طرح ۱۵ ماده‌ای نخواهیم شد و اسرائیل عملیات در غزه را متوقف نخواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/140866" target="_blank">📅 08:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140865">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
سخنگوی وزارت کشور: از فروردین ۱۴۰۴ تا اکنون، حدود ۲ میلیون اتباع غیرمجاز از کشور خارج شده‌اند.
🔴
اتباع مجازی که در کشور حضور دارند قدمشان بر چشم، اما باید بخشی از هزینه‌های زندگی خود را تأمین کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/140865" target="_blank">📅 08:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140864">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
بهای نفت برنت دوباره صعودی شد و به ۸۴ دلار رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/140864" target="_blank">📅 08:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140863">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9012d16498.mp4?token=LL8-PJ1rprKIYHs_Z4QDK-ihjSnuQUO9sXA2yxRzgrUwj0ghOCvYeFO5Dy-FZsuvRUBPBqkbNuZjMICdB_FtHY_jKV8-RjR4YRD2LcHZRzxBog3-1vyyw6N8KSjOixJsXJIDDWKfiF8ncbgJpn2GIMt5gGM5hab2FGvx4J1VTBj4LrzBnTAbPRnF6ofQnEuXEFyi0rukqEFHhnpyk0MvxIQSV8Xwb3g9MaLwZGjQj3pGYZKYWTHX-riNzHS56Wn9Jlao2quV7cwQeJxY7BB3W3CoLxPWTUI1ArqFnD3w_3Ct0Fbez9YXwWAjh0-cpv2AQshvLY_SGb2pddwXnOZ-aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9012d16498.mp4?token=LL8-PJ1rprKIYHs_Z4QDK-ihjSnuQUO9sXA2yxRzgrUwj0ghOCvYeFO5Dy-FZsuvRUBPBqkbNuZjMICdB_FtHY_jKV8-RjR4YRD2LcHZRzxBog3-1vyyw6N8KSjOixJsXJIDDWKfiF8ncbgJpn2GIMt5gGM5hab2FGvx4J1VTBj4LrzBnTAbPRnF6ofQnEuXEFyi0rukqEFHhnpyk0MvxIQSV8Xwb3g9MaLwZGjQj3pGYZKYWTHX-riNzHS56Wn9Jlao2quV7cwQeJxY7BB3W3CoLxPWTUI1ArqFnD3w_3Ct0Fbez9YXwWAjh0-cpv2AQshvLY_SGb2pddwXnOZ-aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
جشن امشب مردم ترکیه بخاطر توافق مکه:
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/140863" target="_blank">📅 07:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140862">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feeb36b6ca.mp4?token=A3TIqQNGcozlWcSz5OAEmdyrvLaHGvivkd19klKdTxz2atuw-SstebpPsYnKKDjAanWAMzWxTFF_CfgI_ajhLLXtb-7vbVO3myp5JhZcLinxuvdKbjeGaQY4PEotZjOH5k8hYg7HuJB2D3g2WRGJYUGpAkSrIK1rXNhl95t3bs7fV681uVAr3dTHernbMQf4Z_au128ETQz8i06uFOXEfBaZwrSMLkdEkYusDrJvMJ_3sej3KgTFxtf77VEABml30D2kyUedd_7tJDRQSZwiKmOb1S5RV0xHLe66Kn9vs-69ULdXRC_30YZoPk5hLdN1LvrPVudYTSz0zK23S3JDIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feeb36b6ca.mp4?token=A3TIqQNGcozlWcSz5OAEmdyrvLaHGvivkd19klKdTxz2atuw-SstebpPsYnKKDjAanWAMzWxTFF_CfgI_ajhLLXtb-7vbVO3myp5JhZcLinxuvdKbjeGaQY4PEotZjOH5k8hYg7HuJB2D3g2WRGJYUGpAkSrIK1rXNhl95t3bs7fV681uVAr3dTHernbMQf4Z_au128ETQz8i06uFOXEfBaZwrSMLkdEkYusDrJvMJ_3sej3KgTFxtf77VEABml30D2kyUedd_7tJDRQSZwiKmOb1S5RV0xHLe66Kn9vs-69ULdXRC_30YZoPk5hLdN1LvrPVudYTSz0zK23S3JDIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طالبان کاملا جدی برده داری جنسی زنان رو قانونی اعلام کرد، از این به بعد مرد ها میتونن مثل کالا زن هارو بخرن و مثل برده جنسی ازشون استفاده کنن
این در حالیه که حضور زنان در مدارس و تحصیل همچنان ممنوعه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/140862" target="_blank">📅 07:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140861">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">💢
💢
🔥
🔥
💢
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات goldonliveeeee@   لحظه ای قیمت میزنه  منبع دقیق قیمت لحظه ای طلا و تتر
😀
☝️</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/140861" target="_blank">📅 01:41 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140860">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">💢
💢
🔥
🔥
💢
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات
goldonliveeeee@
لحظه ای قیمت میزنه
منبع دقیق قیمت لحظه ای طلا و تتر
😀
☝️</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/140860" target="_blank">📅 01:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140859">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwjqNstYTeXd_CFqERGQ2MUQRyQtzZZkLsLLWh0ie-C4C84JVEpa92qLxVvARnN_Ya8SCOyuQF-IucrXo_B5-lAqOfylol9KQYGcOSAdM5LJXyQZvT9ws9hSlsw6-bPS78x6q45UvEPhADrHvcVDlRipEI-CUoL_PGHh5S8K74Q-vulS4qzpSEgWqsh09lqu01zwJ78_Y06xqwKHgrNyGLJPK9fbjuIkCNKMXvsj60GBaZ7MFJFcn_vdrP-XGEu5mWyYBVgPMsUJFezbTETB2La5aWpX87xMpyIsVQX8DWjENzAMROwJ5xQgjDmWx5dtsHrjvOEdQuL7PprrMSJG1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرد که نیروهای آمریکایی مسیر ۵۵ فروند کشتی تجاری را تغییر داده‌اند، ۲ فروند را غیرفعال کرده‌اند و به ۲ فروند دیگر صعود کرده‌اند تا از رعایت مقررات مربوط به تحریم بنادر ایران اطمینان حاصل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/140859" target="_blank">📅 01:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140858">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‌
🔴
فوری/ بلومبرگ:
توافق درباره تنگه هرمز اکنون دور از دسترس است؛ ایران با مذاکرات مستقیم با آمریکا مخالفت می‌کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.2K · <a href="https://t.me/alonews/140858" target="_blank">📅 01:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140857">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کیهان: اردوغان و شهباز شریف مثل روباه مکار و گربه نره بن سلمان را سرکیسه کردند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/alonews/140857" target="_blank">📅 01:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140856">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cd2301599.mp4?token=IDVRJ71VJ8w5vCuNvuZXhfHcLpcgdwROwSyu0irFGzZwZTGqTH9jtR4TUQOGnIrCPQd05ywQxx_YaCt3loT5V4WqraB99xbmKaTICXfwNnpe-gnWVKvq8qIlc7TW3uICF7DCOZL9EVfNKW2hesKWUEJlEKFfUJzkykDPV2bY-vKoTqLZMWkgjPblx_7zzpP8j3U0XtdESpdnqUy1yGfxC4lqOBILdox6hpQ9a2dcAFGZ_7EUQ5mtbxGCkUW-wnnAo9Pp7nj_29ZiXfTZxpYUiRWszqpTqRr9DyTR1j9AXy4hRV7PiXq828elDj4Y65YcI5ceCO75ogUYAZONmbnvCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cd2301599.mp4?token=IDVRJ71VJ8w5vCuNvuZXhfHcLpcgdwROwSyu0irFGzZwZTGqTH9jtR4TUQOGnIrCPQd05ywQxx_YaCt3loT5V4WqraB99xbmKaTICXfwNnpe-gnWVKvq8qIlc7TW3uICF7DCOZL9EVfNKW2hesKWUEJlEKFfUJzkykDPV2bY-vKoTqLZMWkgjPblx_7zzpP8j3U0XtdESpdnqUy1yGfxC4lqOBILdox6hpQ9a2dcAFGZ_7EUQ5mtbxGCkUW-wnnAo9Pp7nj_29ZiXfTZxpYUiRWszqpTqRr9DyTR1j9AXy4hRV7PiXq828elDj4Y65YcI5ceCO75ogUYAZONmbnvCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یه پهپاد رو تو جنوب کشور زدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/140856" target="_blank">📅 01:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140855">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efvjJmrr5e9W8xv3cKuak8De7ykH_zaatduV00rQhlPGfMv65FyKzR-YZCe8QhdA20lVmahAL2r2A6TBOu0aG5LbnCwdkBv3RHGwv08CxA8M2X15ouD2O8xpN27goeFsKH9slloDJbRNpPC_hqMUwcTwMgbOufnQUrmZhb2HNuWIJxYRVQC5nmO7V371t0raif7eboK3kFH4MJKx4fk0VjxwWuF-RqNqAitVBAzqYB8gY_l-KSMFajPSC00-NzzNg4fs8HhEcvPjCWCDX9bNM90S419xT4KB_ybkomvuwdTfxG_3dxVkFN9hZfsLdlPkfTiTA8TvNyO_qyFCSgDCfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
میثاقی: علی دایی در حد فوتبال اسطوره هست و الا تو سیاست و روش زندگی کاراش خیلی چیپ بوده
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/140855" target="_blank">📅 01:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140854">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EU_BhTmmXvi3Ox-KSgGilveyrpwGrnm3R722BT5q_uFmomap5Z1rKWzYrda7ysp6zQIYCQqR58HRXahiuHmoUPB9cayU2vIX8htzO-YCXiZEBxR56xxWaNmmflDDu7sTTNidpnxREQsUIgQIvYjYb-NpuqBe7x3aF3R1UBvfCbHqW-AmwLRaIX_RgkL4bUnOFDMLl5LTy1kUwYONx3Ghrl_fUHYij_TR5HUjdMbW3JzTEtBmyKVmsVeNxCO7uD_ReJqDntUk51zHWCevEInOeK_G04zXXgftmEYk5xJw3aGFBlhulCexBe-XQwb-REKUbtVXiKSTqvR2O5V8tVI4QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه نفتکش تو نزدیکی عمان هدف حمله قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/140854" target="_blank">📅 00:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140853">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">💢
این وسط فیلم مسیح علینژاد و دوس پسر سیاه پوستش منتشر شده که.........
💢
مشاهده ویدیو</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/140853" target="_blank">📅 00:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140852">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGt83eBx34yDhn8gxiOhzYMeNEPE4su1q9ukxtnuhRWzeWYZIojk9MpKBN3GvTNkd90KgJXe_2mFTWSLObP-txxwqStHfzwKYmtv9Y5pfrW7Ly-XxzpYcl92tz_Go3_mbUweWE4soeJxxt1R3AcgkLtfDhegUwT4RVq1Egrus0TgeCi0o3DR1QTO24X9TcQx0cfonraFBkF2maG2FV0Wo_8iQLJ_RqVZT1onBjYBO8HCnaRAB3fxzLgMZ5F3u51rHrVZ7QkMHac4EJeqP8j_EQsJ2YfoCc3-vBC2HvC08uYQG2TicItRp0ym1KI4GB8DjbQThjJD0ogtcjr9fRTUQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
ترامپ: 51 سال رفتار نامناسب ایران!
🔴
جالب اینکه چندسال آخر شاه رو هم رفتار نامناسب میدونه!!! و فرضیه اینکه غربی‌ها تو رژیم‌ چنج دخیل بودن رو قوی میکنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/140852" target="_blank">📅 00:39 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140851">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaa90a135.mp4?token=aXDVbbqnhSyUq8nQIr7IuXut6axh1tqsDsIEBnogv01GmT3IVlgUle_0_M04zyxUNGfGAnWQMZY2S7VfRueCRUF5BLTzDUSc-82Tx0zeG-KFUFj8-o4YRQFDGiRM0MaWI-0-ZeB8qkMvq8TzfL5zkPj7ivNhvMaHfDINeX0HSuPrA7LgmRVscp_RdVBcmiyGzXwwyiR_UQsrBTbgHMhZf4XpGRWqaPRyqH4MGSyWUChDw3InpHpJ_UOteQx2ap-Omp6XJcxgl8ufEQo27Cws7ZASeKYrcq9uLquaW0_Oue3BSHGtuXTyU94qSOVY2XHPbbC_uPwMaeDhn-VtzOwcmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaa90a135.mp4?token=aXDVbbqnhSyUq8nQIr7IuXut6axh1tqsDsIEBnogv01GmT3IVlgUle_0_M04zyxUNGfGAnWQMZY2S7VfRueCRUF5BLTzDUSc-82Tx0zeG-KFUFj8-o4YRQFDGiRM0MaWI-0-ZeB8qkMvq8TzfL5zkPj7ivNhvMaHfDINeX0HSuPrA7LgmRVscp_RdVBcmiyGzXwwyiR_UQsrBTbgHMhZf4XpGRWqaPRyqH4MGSyWUChDw3InpHpJ_UOteQx2ap-Omp6XJcxgl8ufEQo27Cws7ZASeKYrcq9uLquaW0_Oue3BSHGtuXTyU94qSOVY2XHPbbC_uPwMaeDhn-VtzOwcmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
این زن چادری اومده اینطوری انتقام خون «رجب زاده» رو میگیره
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/140851" target="_blank">📅 00:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140850">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pCHPVC4xnHlpv4AYQjQMTundqKjo7rqA038YV8yw6KwkEhpGezxIiXJh-d1Ug49_H7FxgfyuZJshnr5-WfgrUVBVEoDfjSvdOSEX1Yyg3u_n9BLhS1srFCVN42Z0BY-DmPFNXG79kPChRLkXmfDn7xvpHd47jEwrngUt6qY9TH--4taLmP-KfOsesBBCMonoy3kyDSe_60l5cnMxMbaTmoCSWtIu5JGi71S3rjNZ79NHNnedrrBJxbAJtjjf668PHgvWp9N4w8wVRAasuIG6YCNeMW4HLOqEfJ5mDz3wulUCGW-ymDrHDmf0cgtOuzuWpOZCF0nf_VP6QqoTELSlHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرح
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/140850" target="_blank">📅 00:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140846">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iHB2HrL_Yte4v5MfiH8M7Mc7NUiRjPs6w3j-m2IButlYoF9V-ptn4NuBIsTR-Q2_39oNjzqu53VYFYajiA_5soS4koqrCmBnYUGWYgXJXg9RB5__70cIrhRGK3xGLsSg91bNvcQu3qsEjPkTholautTy2276Ft3iMXydseRjoUYBS-KFG3qpVoFM1ejujKJDgpjIgz_W9QcnxVPx0qHPKRKu0JVYzqq66JTtubGsNK9ZTYEW6r0WxZpjA2l2yqjJugUAPiAAo3dFbiZYbJO9ZFqnpbh_FoOxAyzNN32nANUpwmF-Z-JGloCqt2EOyFEkymuOg4AUaQEZknJtHRbIDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_mG3SGiZnDwvJFnyAqlXwKtI052oh7ywMxp0yulsh-9-riWn1VbI__IjHzsYngN4gLmf0Oa8v1ZHbYQ_C4BIUpV0CcvR8g14dOeK_V61zyI3VXJt1DiOiTy85A0xJcqx2OOk162yGhVOI-GiGvJ7biwEiYi9H4WDK2_1EX4p_ADtSTNU4m9yp5KNIBNKqXoX-Bex9KuAdP4pDbXmB6GkZUKlN3_bIecJI7no5ZLsAgNRDg5xkEjuG2i6rtvNNheFQhHggtXasoIjXfeg9TwBK4eOjBSCiYmiFhW1E16TNGuHS2A9B1vYoguv7axHKi5akKK66Pi0S4Zwqj66Uf1tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d-Wza_coCWAUIpjHtQEeaFn_EIqIpoDma7sgLFFfNBPJ8NbrczPdbnAODMbd_mTafIZEsolEVY3GvTMdwSRMsSlDczTaz342qkz55wivcB3_ShUdOJRJLKO8exVlO1YISsEwnEfBYVQf_EnPvqYK2jcnqpLE_JrkIwNr6jwrU9p_TimWtHMMT6b4SuYTnLAN2v-pkAoRKTW_gnW8BQZgClwpq-YFxlReeF_-VvvxqwtcIofUoRZt_TAAg65Muyw2_jixxSTkFa8ERLcFvFNsnNAmqbQ5CieVi-JOLeksH2PJkx7GMMjy1ZIc93Rp2u2E4ch8kKF7L2PRLpWSFpemTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
یگان‌های پدافند هوایی ارمنستان با استفاده از پدافند هوایی مجید ساخت ایران که اخیراً خریداری شده و سامانه موشکی هندی رزمایش آموزشی برگزار کردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/140846" target="_blank">📅 00:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140845">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">‏
👈
اعتراض شدید کارشناس هواشناسی: هواشناسی جای ترسوندن مردم برای بیشتر دیده‌شدن نیست
‏
🔴
ماجرای ال‌نینو را جدی نگیرید!
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.3K · <a href="https://t.me/alonews/140845" target="_blank">📅 00:04 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140844">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67f191ecf5.mp4?token=dPFt4VxL1YEVdbNT_EpxtAQWEIJHPQy9U_sZp3uDDqcQ1GlfIrOgmjH1NgB2GqZiHbDeJq8im5DEU34lrhloXEL42wCXGVSLQ0L8dRcvGca_pFr1VCNMa_2KSOT3RRxQlDsC-rmJE3BAqjUbZHoswEeryC_H9B-zccG-Lt3bRbVWN832ymTqR4i5rPSr2bx6_kdZpBYwjnQ48w8zS3QYb8-GZPgSUHPMz8EZUak9-SAjkLpaaGKkpbGqWN5zh_Afr-oT2ZzBhbyv_VPFupJUBLBipS4UJlARJPjD6pKWN0ayUlPn1OYaMGakdDQffukbDqbSGhhkqlA1cjZsWQ0zEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67f191ecf5.mp4?token=dPFt4VxL1YEVdbNT_EpxtAQWEIJHPQy9U_sZp3uDDqcQ1GlfIrOgmjH1NgB2GqZiHbDeJq8im5DEU34lrhloXEL42wCXGVSLQ0L8dRcvGca_pFr1VCNMa_2KSOT3RRxQlDsC-rmJE3BAqjUbZHoswEeryC_H9B-zccG-Lt3bRbVWN832ymTqR4i5rPSr2bx6_kdZpBYwjnQ48w8zS3QYb8-GZPgSUHPMz8EZUak9-SAjkLpaaGKkpbGqWN5zh_Afr-oT2ZzBhbyv_VPFupJUBLBipS4UJlARJPjD6pKWN0ayUlPn1OYaMGakdDQffukbDqbSGhhkqlA1cjZsWQ0zEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش سوزی گسترده در ایالت بریتیش کلمبیا در غرب کانادا
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/140844" target="_blank">📅 23:57 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140843">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TlcbuJQw1xqc29u_vSqZpRc8ZvPn9vgUwConYExEzb7nsnNtctX8z1xu4xmEMI-xp6MqDQD_7dWc7JEDtRVsxhpi4T2_gshznNE67MRswWRwJOZxEXEl5aPfhVcUHFbeC61s0O3jAJGSQUsNqszhSSh1tuI-pREoUtEqThHfSLJfbEdLVwl0Hn8rTWuSFZaAXV5F2THE1527zQKTvHCGtJTx-PxkmjMAhxHbK0Cbh3LEkRz5LAE9jx8XXKtP5ts3CjYy2HbisCFRIzSHOt0Bq5e44nYkyDD2QInx-RvpNWA9jGdOjGE0ItLWpREIQAHBeLzkN-PPmBZqf9IZnwpaeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان 730 تیر موشک PAC-3MSE به همراه برخی ملزومات ( فاقد رادار کنترل آتش، پنل فرماندهی یا پرتابگرهای اضافه) به قیمت 9 میلیارد دلار خریده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/alonews/140843" target="_blank">📅 23:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140842">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4403cc9061.mp4?token=boh8-i1Kso-Howy0YxA7qaYfttpSBC-_vzZYQ1ypFWdKGVSY03X2zIRVq7yjRVyowpcSWGZO26VnuPFi8d-Yvz15zf2A8rjh_HQNUPXugRWLKv6mFWOl1Ex0tsmSSjqHIpACmBerigw9M6wXahd7kE-96HHbiu2vM6oI17FRyypwlw8CHXhCRhQsMZejLJBf76qb23p5C8QSgTiBBh4aMIZUs7O5V_s8zn_3hOEo8O7AJpqVnT7xBDwDQ-cwiQC-i7MsBzAj7pizstQwn4XbL5ahyZUxK6QRnnynaVDfPo-4aCEpj8IAPUpI8Ppc9UrarE8pD_s0xJpcSRh2DClDgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4403cc9061.mp4?token=boh8-i1Kso-Howy0YxA7qaYfttpSBC-_vzZYQ1ypFWdKGVSY03X2zIRVq7yjRVyowpcSWGZO26VnuPFi8d-Yvz15zf2A8rjh_HQNUPXugRWLKv6mFWOl1Ex0tsmSSjqHIpACmBerigw9M6wXahd7kE-96HHbiu2vM6oI17FRyypwlw8CHXhCRhQsMZejLJBf76qb23p5C8QSgTiBBh4aMIZUs7O5V_s8zn_3hOEo8O7AJpqVnT7xBDwDQ-cwiQC-i7MsBzAj7pizstQwn4XbL5ahyZUxK6QRnnynaVDfPo-4aCEpj8IAPUpI8Ppc9UrarE8pD_s0xJpcSRh2DClDgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: [مذاکره کنندگان] در حال گفت‌وگو هستند تا انشاالله مسیر را پیش ببریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/140842" target="_blank">📅 23:46 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140841">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
زاکانی، شهردار تهران: با اصل مذاکره مخالف نیستم، اما مذاکره باید با شرط و شروط باشد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/alonews/140841" target="_blank">📅 23:41 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140840">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔥
🔥
⭕️
قیمت طلا و دلار فردا سه شنبه ریزشیه
👇
سایت رسمی اتحادیه طلا و جواهرات
goldonliveeeee@
لحظه ای قیمت میزنه
منبع دقیق قیمت لحظه ای طلا و تتر
🚨
☝️</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/140840" target="_blank">📅 23:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-140839">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIkjy8qXQIPoQgroxKNH32uS4X7NJSnq51uFSp0GYwcXfi8geTfPXarTgjNG2E7PezYrt1iuowf-ZxlPWQZIXODd7swXulpdBEiC4gbuZOr5ie-H9NIEYU0Qx_xxdJpyV2Au77BpGs6CpwUaCHfDL-7lXowbLHwuIiVlOssFXXdIu2bFK-HvxweG8hWWddZuIEmO_KG3fsPszay265q06LbhVREcHKOJXhFIoHzD4_n-4nXhCaCjvOgEf5vdq1L9NmuX-zwB1Lgro-rGHdw1LrwWWAqR_e6OZsQL3b2opceRRNRXO5C3ptkq7lsy5k66CyfRzvOlc54aA4gdnbQSBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علی قلهکی: افرادی که در چند سال اخیر _خصوصا پس از ماجرای ۷ اکتبر_ مهمان جلسات خصوصیِ «فیلد مارشال محسن رضایی» بوده‌اند، شهادت می دهند که تمام اتفاقات بُهت‌آور این روزها را «محسن رضایی» به‌ دقت پیش‌بینی کرده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/140839" target="_blank">📅 23:30 · 18 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
